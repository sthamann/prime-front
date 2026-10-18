#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_packing_dichotomy_probe -- PRIME.TERMINAL.EDGE_PACKING.01
(round 335): THE ONE-SIDED EDGE-COMPANION FORMULATION after the r333
structural finding.

CONTEXT (binding, from the sealed r333 record, commits 279ba0dd/
55d4a832): the reviewer companion packing adjudicated
ORBIT_TOO_SHORT on the INNER interval -- because THE BOUNDARY CASE
IS THE RULE (44/65 rungs: the dominant beta/omega pair sits in the
outer BOUNDARY_F = 0.10 margin of the masked support, d* med 0.072
min 0.002; the inner orbit is EMPTY at three of the four named
spikes kz53/kz83/kz55, kz67 has 2).  But TWO clauses are certified
at theorem grade: (T2) the BAND DISCIPLINE (inside one dyadic gmax
bin the proven two-ancestor bound forces 1/4 < gabs/gabs' < 4
EXACTLY; live rmin 0.2819 / cband 3.5473 on 69 worlds; b = 0,
c_1 = 1/4) and (T3) the OVERLAP (partition-exact membership
1 <= 2).  The one-sided census shows same-key companions EXIST on
the edge side (>= 1 at every named spike, up to 25 at kz37).  The
composed chain q_max <= ng kappa/(|O| rmin) is exact (kappa ~ 3-4
stable).  All four spikes are SMALL_ORBIT + HEAVY_BAND
simultaneously.

THE ONE QUESTION OF THIS ROUND: does the ONE-SIDED edge-companion
construction carry?  Define the orbit one-sidedly (from the
dominant pair's position toward the INTERIOR, with edge-adapted
reach) so it is NOT empty at edge spikes -- and test whether T1
(|O_e| >= c_0 m/(log m)^a) holds in the one-sided form on all
rungs including the spikes, with T2/T3 still at theorem grade.
PLUS the structural lever the r333 census suggests: at the edge
the admissible source mass falls -- the one-sided theorem gets a
SECOND clause (the tent-cover / mass argument): EITHER many
companions OR small edge mass -- both cap q_max.

THE ONE-SIDED CONSTRUCTION (binding, source-pure, sealed BEFORE
any q_max sight): for the dominant pair g* (r333 dominant_state
verbatim: source scale bin s*, fold parity (nwin, sign), position
ps, edge distance d*) the EDGE ORBIT is
  O_e(g*) = all fold groups of the SAME source-scale bin AND the
  SAME fold parity whose position lies in the ONE-SIDED window
  [ps, ps + R] if ps is nearer pmin, else [ps - R, ps]
with R = THE MASKED SUPPORT RADIUS: R = EDGE_R_F x W, EDGE_R_F =
1/2, W = pmax - pmin.  The reach choice is frozen a-priori for
three reasons: (i) PARAMETER-FREE -- no new tunable beyond the
r333-frozen support geometry [pmin, pmax]; (ii) COVERAGE-MATCHED
-- from any boundary position the window reaches past the support
midpoint, covering at least the 0.4 W of interior measure that the
r333 two-sided inner interval guaranteed a centered pair; (iii)
DIRECTION-CANONICAL -- the window opens toward the FARTHER edge
(the interior), away from the edge that starves the two-sided
orbit; g* is always its own member, so |O_e| >= 1 and the r333
|O| = 0 sentinel is structurally eliminated.

THE DICHOTOMY (exact algebra, both arms warded live):
  ORBIT ARM (the r333 partition chain on the edge orbit):
    L1_atom >= sum_{g in O_e} gabs(g) >= |O_e| rmin_e gabs(g*)
    ==> q_max <= ng kappa / (|O_e| rmin_e) =: Q_e,
    rmin_e = min_{g in O_e} gabs(g)/gabs(g*) > 1/4 (band theorem,
    same bin), kappa = L1_atom/L the measured target-adjacent
    transfer (disclosed, r333 verbatim).
  MASS ARM (the reviewer edge-mass lever, "if the edge orbit is
  small the edge mass itself must be small"): S_marg = the total
  group mass of g*'s OWN BOUNDARY_F margin (boundary case: all
  groups with gpos on g*'s edge side of the inner interval; inner
  case: S_marg = gabs(g*) itself); n_marg = the active-ancestor
  count of that margin (census).  gabs(g*) <= S_marg EXACTLY (g*
  lies in its own margin), hence
    q_max <= ng gabs(g*)/L = ng kappa gabs(g*)/L1_atom
          <= ng kappa S_marg / L1_atom =: M_b.
  THE DICHOTOMY BOUND: q_max <= Q_dich = min(Q_e, M_b) EXACT --
  either many companions (Q_e small) or small edge mass (M_b
  small); each rung is typed by its smaller arm (letter O/M, the
  arm census is a PARTITION -- overlap-counting is refused, e2).
  The certification question (mid-ladder freeze, TRB verbatim):
  B^D_a = m Q_dich/(log m)^{1+a} <= C_D(a) with 0 test violations
  + named 4/4, minimal a in A_FAM = (0, 1, 2); T1 one-sided:
  |O_e| (log m)^a / m >= c_0(a) likewise; the single arms
  (B^O_a, B^M_a) are certified separately so EDGE_PARTIAL can
  name the missing arm.

THE FOUR MEASUREMENTS (sealed):
Q1 -- EDGE-ORBIT CENSUS: |O_e| on all rungs (65 + 12 EXT3),
   inner-orbit cross census (|O_in| via the r333 construction
   verbatim), rmin_e/cband_e, margin census (n_marg, S_marg/L1),
   arm letters, T1-edge certification.
Q2 -- DICHOTOMY CERTIFICATION: B^D_a vs C_D(a) (mid-ladder
   freeze; EXT3 anchors are PURE TEST rows, never calibration),
   single-arm certifications B^O_a/B^M_a, minimal a each.
Q3 -- SPIKE HARDNESS TEST: kz53/kz83/kz67/kz55 -- which arm of
   the dichotomy covers each spike, with which reserve; plus the
   COMPOSITION: on GO the chain q_max <= C_D (log m)^{1+a}/m ==>
   N_2 >= m/(C_D (log m)^{1+a}) with m_0* solved and compared to
   the r324 MEASURED route (does the dichotomy replace the
   +0.172 exponent?).
Q4 -- WORLD CHECK: twin w13 (identical protocol, exact wards
   live), SCRAMBLE (edge-orbit decay census), EPSTEIN (band/edge
   behavior census); SMOOTH degenerate-skipped (pre-declared).

EXT3 ADOPTION (git log checked at spec time): the r329 EXT3
record IS committed (8cbd95f9 "experiments: r329 record"), so the
12 fresh anchors are adopted THIS round as PURE TEST rows: the
sealed r329 selection kz42/51/54/56/58/62 (stratum B, small-gap
mid-zone) + kz96/123/125/127/128/130 (stratum A, depth), N_w
1721..2577, POSITIVE_PREFIX 12/12, mult <= 2 on 12/12 (r329
record data adopted as-is, disclosed).  They enter the
certification TEST set and every census; they NEVER enter a
calibration window (the mid-ladder freeze stays on the sealed
65-rung ladder).  Deep-anchor bars a-priori from r329: TB ward
3e-5, identity wards 1e-12.

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK                  iff any purity/scope/literal audit
       hit on the edge builders,
   WEIGHT_COMPARABILITY_FAIL    iff the exact band ward breaks on
       a live edge orbit (rmin_e <= 1/4 or cband_e >= 4 beyond
       bar) or the overlap ward breaks (> 2),
   EDGE_PACKING_GO(a, C_D)      iff the DICHOTOMY certifies at
       minimal a (0 test violations incl. EXT3 + named 4/4 +
       C_D below guard); the T1-edge status is reported inside,
   EDGE_PARTIAL(missing arm)    iff not GO and at least one of
       {T1-edge, orbit arm B^O, mass arm B^M} certifies at some
       a -- the letter names what certifies and what is missing,
   EDGE_ORBIT_ALSO_SHORT        otherwise: the packing language
       is exhausted at the edge -- the reviewer's martingale
       second route is next (NAMED ONLY, not executed).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r331/r334 may run in parallel; this probe touches
NOTHING outside its own file and the strictly additive rh-sync
(existing entries byte-identical).  Two-commit freeze protocol
(r329 convention): spec committed pre-freeze, record tables the
only post-freeze edit, committed again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r324/r327/r333
machinery imported verbatim): t_{N-2} = sum_b ct_b (r244 chain
rows, r266 eval); F = 0.20 edge split; maximal same-sign runs of
the bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy
+ SCF.signed_cube_terms + SCF.flux_telescope; the r316
TRB.two_regime_state + TRB.split_midladder; the r324
QMO.scale_bins + QMO.mult_ward; the r324-pre FAP.m2_qmax_state;
the r327 GMC.group_mass_ledger (cross-ward only); the r333
COP.orbit_ledger + COP.dominant_state + COP.companion_orbit
(audited source-pure in r333, imported verbatim -- the inner
orbit is this round's CROSS CENSUS); PDelta = Pbeta - Pomega;
x_j = (PDelta)_j.  NEW in this round (module-own, source-pure):
edge_window (the sealed one-sided reach rule), edge_orbit (the
one-sided same-key selection), edge_mass_state (the margin
mass/ancestor census), dichotomy_state (the two exact arms + the
min + the arm letter) and the sealed edge_tree.

LEG 0 -- ANCHOR REGRESSION (slim set + the r333 record,
disclosed): the r314 identity wards live; r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r316 rho anchors kz53/kz67/kz55/
kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) + C_small 1.0694
at kz18 + n = 65; r333 RECORD anchors reproduced bit-near:
boundary count 44/65 EXACT, |O_in| med/min/max = 5/0/52 EXACT,
named inner quartet (0, 0, 2, 0) EXACT for kz(53, 83, 67, 55),
named hgn quartet 14.89/13.43/10.30/15.17 (tol 0.02), d* med
0.072 (tol 0.005), inner-orbit band worst rmin 0.2819 / cband
3.5473 (tol 0.005, over the r333 69-world live set -- EXT3
excluded from this anchor by construction).

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) sealed
definitions printed; the SOURCE-PURE table (rank, kz, N, m, G,
ng, hgn, |O_in|, |O_e|, rmin_e, cband_e, kappa, Q_e, M_b,
Q_dich, arm, case, s*, d*, n_marg) printed BEFORE any
certification table.  (A2) SOURCE-PURITY AUDITS: the AST
identifier scan over edge_window + edge_orbit + edge_mass_state
+ dichotomy_state + edge_tree must be clean against
BOUND_FORBIDDEN + PHI3_FORBIDDEN + QMAX_FORBIDDEN (the edge
selection consumes group scale bins / parities / positions / the
support geometry ONLY; no block value, no target, no q_max
record); the literal scan over the builders + toys must be clean
against the sealed record-literal set R335_TABLE_LITERALS (the
r314..r327 set UNION the r333 record numbers); the e-mutants
prove the audits bite.  (A3) TOY EXACTNESS (Fractions): the
seven-block edge toy (support [0, 1]; g* = pair (5, 3) at 1/20
-- boundary case, d* = 1/20; same-key companions at 3/50 and
2/25; wrong-parity pair at 7/100 EXCLUDED; same-key pair at
19/20 EXCLUDED by the one-sided window [1/20, 11/20]; light
atoms at 0 and 1 EXCLUDED by bin): INNER orbit EMPTY while
O_e = {g*, c1, c2} EXACT (the r333 spike anatomy reproduced in
the toy); rmin_e = 13/16, cband_e = 16/13, kappa = 1, Q_e =
16/39, margin census n_marg = 5, S_marg = 151/5, M_b = 302/391,
Q_dich = 16/39 (ORBIT arm), q_max = 80/391 <= Q_dich with slack
3136/15249 EXACT; the mass-arm toy (|O_e| = 1, rmin 1, S_marg/L1
= 1/10): Q_e = 1, M_b = 1/10, Q_dich = 1/10 (MASS arm), toy
q_max 1/20 <= 1/10 slack 1/20 EXACT; the arm-partition toy:
letters (O, M, O) count (2, 1) sum 3 EXACT, the double-count
mutant returns sum 4 != 3 (break 1 EXACT, REFUSED); edge_tree
all five branches EXACT.  (A4) LIVE WARDS on every live world:
the r316 chain + NORM x cube == rho_2 (r333 verbatim); the S0
interpolation; ledger == genealogy == GMC (r333 verbatim); the
partition sum_g gabs == A1_j; THE BAND WARD rmin_e > 1/4 and
cband_e < 4 on every edge orbit (bar BAND_TOL relative); THE
OVERLAP WARD membership <= 2; THE TWO EXACT ARMS q_max <= Q_e
AND q_max <= M_b AND q_max <= Q_dich (exact algebra, bar
CHAIN_BAR); the ARM PARTITION (every rung exactly one letter);
kappa >= 1; fold multiplicity <= 2 admitted (QMO verbatim).

LEG B -- Q1/Q4 EDGE CENSUS: |O_e| ladder statistics vs |O_in|,
margin census, arm-letter census, the named spike anatomy
(which arm covers, with which reserve), the world table
(twin/EPSTEIN/SCRAMBLE edge-orbit + arm census).

LEG C -- Q2 CERTIFICATION (mid-ladder freeze, TRB verbatim;
EXT3 pure test): T1-edge c_0(a) = min cal |O_e| (log m)^a/m,
test violations (65-ladder test rungs + 12 EXT3), named,
minimal a; T2 the exact band theorem gated as live ward; the
single arms B^O_a <= C_O(a) and B^M_a <= C_M(a); THE DICHOTOMY
B^D_a <= C_D(a), test violations, named, minimal a; exponents
e(hgn) vs DELTA_CRIT = 0.112 (census continuity with r333, NOT
adjudicating this round) and e(B^D_1) with the halves stability
rule; EXT3 cohort exponents census-grade (12 anchors, mixed
strata, r329 caveat disclosed).

LEG D -- COMPOSITION (printed ALWAYS, honestly typed): on GO:
q_max <= C_D (log m)^{1+a}/m pointwise => M_3 <= q_max^2 (S0
exact) => N_2 >= 1/q_max >= m/(C_D (log m)^{1+a}) => N_2 >=
m^0.888 for all m >= m_0* (log-space solve) => the r297 target
chain; the r324 MEASURED comparison (m_0* 10^59.6, +0.172): the
dichotomy REPLACES the +0.172 exponent iff it certifies AND its
m_0* <= the r324 m_0*; on PARTIAL: the certifying arm's envelope
printed + r324 restated; else the r324 MEASURED composition
restated unchanged with the edge-route envelopes printed.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) REACH AFTER SIGHT OF THE ORBIT SIZES: mutant_reach_posthoc
  widens R until every seen violator is covered (consumes rho,
  the evaluated bound column) -- the BOUND_FORBIDDEN scope audit
  must FLAG it AND on the sealed toy it returns reach 1.0 != the
  canonical rule's 0.5 -- CAUGHT twice.
(e2) DICHOTOMY ARMS OVERLAP-COUNTED: mutant_arm_double presents
  an arm census with one rung counted in BOTH arms -- the arm
  partition ward must REFUSE it (sum n+1 != n, break 1 EXACT)
  while the live census partitions exactly -- LOUD.
(e3) ORBIT CONSTRUCTION AFTER Q_MAX SIGHT: mutant_orbit_posthoc
  consumes the q_max record as an 'orbit coordinate' -- the
  QMAX_FORBIDDEN scan must FLAG it (AST-CAUGHT) while the
  module-own edge builders stay clean.
(e4) EDGE-MASS BOUND FROM THE TARGET: mutant_mass_from_target
  derives the 'edge-mass bound' from the cubic record (consumes
  cm/S3) -- the PHI3_FORBIDDEN scan must FLAG it (AST-CAUGHT)
  while edge_mass_state stays clean.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r333 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target M_3 / rho_2 and the q_max RECORD enter
GATES / anchors / composition checks only, NEVER an edge builder
(AST-warded); kappa = L1_atom/L consumes block values and is
computed OUTSIDE the builders (target-adjacent, disclosed --
r333 verbatim); no zero/prime oracles anywhere (AST firewall);
no fit primitives (fragment audit; growth exponents are the
imported r272 dyadic halves-slope, fit-free).  MACHINERY
IMPORTED VERBATIM: r333 COP.orbit_ledger + COP.dominant_state +
COP.companion_orbit, r327 GMC.group_mass_ledger (cross-ward),
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
(pre-sealed, r316/r324/r327/r333 verbatim): frame-A h <= 900, 42
rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the
r316 A5 rule (leftover pool + first 12 windows 1300 < h <= 1650,
first 8 POSITIVE_PREFIX by (N, kz)); EXT3: the sealed r329
12-anchor list (record committed 8cbd95f9, adopted as-is,
PURE TEST rows).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); EXT_H_MAX 1300; K_EXT 15;
EXT_NW_EXPECT (942, 1218); EXT2_H_MAX 1650; EXT2_POOL_CAP 12;
K_EXT2 8; EXT3_KZ_B (42, 51, 54, 56, 58, 62); EXT3_KZ_A (96,
123, 125, 127, 128, 130); EXT3_NW_MIN 1721; EXT3_NW_MAX 2577;
EDGE_R_F 0.5 (a-priori, the masked support radius -- justified
above); BOUNDARY_F 0.10 (r333 verbatim, reused for the margin);
A_FAM (0, 1, 2); RBAND_MIN 1/4 (exact algebra); CBAND_MAX 4
(exact algebra); BAND_TOL 1e-9; OVERLAP_CAP 2; DELTA_CRIT 0.112
(census continuity only); N2_EXP_NEED 0.888; NAMED_KZ (53, 83,
67, 55); ATOM_BAR 1e-9; REC3_BAR 1e-13 ladder / 1e-12 EXT3;
TEL_BAR 1e-13 ladder / 1e-12 EXT3; BND_BAR 1e-13 ladder / 1e-12
EXT3; CHAIN_BAR 1e-9; SA_BAR 1e-12; DEG_FLOOR 1e-6; MULT_CAP 2;
N_CAL 5 (via TRB, verbatim); MUT_MIN 1e-6; TOY_BAR 1e-12;
TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep + ext + ext2 / 3e-5
EXT3 (r329 a-priori) / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9;
INF_SENT 1e300 / cert guard 1e299; R306 anchor C_2 1.069 tol
0.005; N335_REF 65; R316 RHO {53: 1.0490, 67: 1.0536, 55:
0.4821, 83: 0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at kz18;
R333 anchors: BND_CNT 44, OIN med/min/max 5/0/52, NAMED_OIN
(0, 0, 2, 0), NAMED_HGN (14.89, 13.43, 10.30, 15.17) tol 0.02,
D_MED 0.072 tol 0.005, RMIN_W 0.2819 / CBAND_W 3.5473 tol 0.005;
R335_TABLE_LITERALS = the sealed r314..r327 set (r333 verbatim)
UNION the r333 record set {0.2819, 3.5473, 0.072, 0.051, 233.66,
54.46, 12.69, 0.0238, 0.1055, 0.4674, 0.148, 0.674, -0.004,
14.89, 13.43, 10.3, 15.17, 3.7, 6.7, 3.1836};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the ledger/band/overlap/arm wards on w9 + controls +
e1-e4 mutants; ladder, extensions, EXT3, anchors, census,
certification, exponents and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r333 RECORD number adopted as-is
(incl. the full r333 anatomy: boundary rule 44/65, empty inner
orbits at three named spikes, one-sided companions existing);
the EXT3 anchor list is the sealed r329 RECORD selection
(committed 8cbd95f9, checked via git log at spec time); the
two-arm algebra (orbit arm = the r333 partition chain on the
edge orbit; mass arm = ng kappa S_marg/L1_atom via hga <=
S_marg) is derived algebra, disclosed above; EDGE_R_F = 1/2 and
the margin = BOUNDARY_F are a-priori (justified above, frozen
BEFORE any evaluation); GENUINELY OPEN quantities of this round:
every edge column (|O_e|, rmin_e, cband_e, Q_e, n_marg, S_marg,
M_b, Q_dich, arm letters), all certification constants
c_0(a)/C_O(a)/C_M(a)/C_D(a), all violation counts, the named
arm coverage and reserves, the EXT3 edge behavior, the world
censuses and the exponents -- NONE was computed before this
spec was frozen; the five sealed letters are symmetric and
total -- the tree maps every outcome to exactly one letter by
CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R335_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r333 boundary/inner-orbit/named/hgn/d*/band anchors)
+ SEAL(ledger wards + partition + band theorem + overlap + the
    two exact arms + arm partition + purity audits + toys)
+ EDGE_ORBIT(census: |O_e| vs |O_in| stats, margin census, arm
    letters, named anatomy + reserves, world table, EXT3 rows)
+ CERT(T1-edge c_0(a) + viol + named + minimal a; T2 band b=0
    exact; arms C_O/C_M; dichotomy C_D(a) + viol + named +
    minimal a; e(hgn) census, e(B^D_1), stability)
+ [exactly one of] EDGE_PACKING_GO / EDGE_PARTIAL /
    EDGE_ORBIT_ALSO_SHORT / WEIGHT_COMPARABILITY_FAIL /
    TARGET_LEAK
+ COMPOSITION(the recomposed chain with explicit constants +
    the r324 comparison; printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the two arms, the band theorem, the
partition/overlap algebra, the Fractions toys, the tree logic
and the purity audits are EXACT (Fractions/AST-decided); every
census, constant, violation count and exponent is MEASURED on
the finite ladder (+ the 12 adopted EXT3 anchors) only; a
certifying letter fixes a proof TARGET, it proves NO cofinal
law; kappa is a measured target-adjacent transfer factor,
disclosed as the honest gap of the composed chain; the r333/r329
record numbers are disclosed pre-spec inputs; the subcritical
delta stays r333-adjudicated (UNDECIDED) -- this round prints it
as census continuity only; r243-r334 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA a1f4c0dd97edcbf4,
pre-freeze commit ec0fd5d5; protocol: smoke pass 1 = 36/36
(0.6 s), NO amendment; calibration pass 1 = first full
evaluation, 36/36, wall 159.9 s, NO amendment; record run1/run2
after this insertion, identical up to the runtime line):
MAIN VERDICT: EDGE_ORBIT_ALSO_SHORT(no clause certifies: T1-edge
c_0 = 0.0595/0.2637/1.1686 at a = 0/1/2 with 43/40/38 of 51 test
violations, named 0/4; orbit arm C_O 166.1/36.5/8.0 named 1/0/0;
mass arm C_M 141.8/33.1/7.7 viol 17/15/11 NAMED 4/4 at every a;
dichotomy C_D 141.84/33.06/7.71 viol 14/11/6, named 4/4, worst
violators kz73 10.31 / kz76 10.04 / kz61 9.02 / kz98 7.92 /
kz109 7.80 / kz95 7.77 at a = 2) -- the packing language is
exhausted at the edge; the reviewer's martingale second route is
next (NAMED ONLY, not executed); the r324 MEASURED composition
(m_0* 10^59.6, +0.172) stays the honest state of the route.
THE TWO STRUCTURAL FINDINGS OF THE ROUND: (1) THE SPIKES FLIP TO
COVERED -- the MASS arm covers all four named rungs at EVERY a
(kz53 B^D_1 12.51 / kz83 20.47 / kz67 2.62 / kz55 11.86 vs C_D(1)
33.06, reserves 1.6x-12.6x; all four typed arm M): the r333
spike blocker is resolved POINTWISE AT THE NAMED RUNGS by the
edge-mass clause -- what now violates is the mid-band family
(kz73/76/61/60 + deep kz95/98/109) where the margin share is
large (sf 0.18-0.28) and BOTH arms sit at 6-10.  (2) THE INWARD
WINDOW MISSES THE EDGE COMPANIONS: at the named spikes |O_e| = 1
(g* alone; inner-empty rungs 6, gained 0) -- the r333 one-sided
same-key companions sit OUTWARD of g* (between the support edge
and ps), not inward: T1 in this one-sided form fails HARDER than
the two-sided T1 (viol 43/51 at a = 0), and the spike coverage
comes ENTIRELY from the mass arm, not from companions.
EDGE TABLE (65 + 12 EXT3 rows): |O_e| med 4 min 1 max 38 (vs
|O_in| 5/0/52 -- the |O| = 0 sentinel is eliminated but the edge
orbit is SMALLER in median); rmin_e med 0.711 worst 0.3162 > 1/4
and cband_e med 1.573 worst 3.1630 < 4 (T2 THEOREM GRADE on 81
live worlds); overlap membership 1 <= 2 (T3); both arms EXACT
live (worst slack violation 0.0 each); kappa med 3.840 min
3.1726; arm census O 15 / M 62 of 77 (the mass arm is the rule);
n_marg med 23 max 231; S_marg/L1 med 0.176 max 0.312; Q_dich med
2.611 max 8.34 at kz60.
CERT: delta = e(hgn) = -0.004, halves +0.148/+0.674 STRADDLE
(UNDECIDED -- exact r333 continuity); e(B^D_1) = +0.517; EXT3
cohort e(m Q_dich) = -3.313 (census-grade, mixed strata, r329
caveat); EXT3 12/12 admitted (N_w 1721..2577 exact), all 12 land
in the test set with the deep stratum BELOW the dichotomy
constants (no EXT3 rung among the worst violators at a = 1).
WORLDS: twin w13 identical protocol (|O_e| 2, arm M, all exact
wards live); EPSTEIN |O_e| 6, arm M (the construction operates);
SCRAMBLE |O_e| = 2 vs inner 0 -- the ONE-SIDED orbit does NOT
decay on SCRAMBLE the way the two-sided did (honest negative:
the inward window with support-radius reach is permissive enough
to catch same-key groups even in scrambled worlds).
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069 (0/57);
r316 n 65 + rho quartet 1.0493/1.0536/0.4821/0.7791 + C_small
1.0694@kz18; r333 RECORD: boundary 44/65 EXACT, |O_in| 5/0/52
EXACT, named inner quartet (0, 0, 2, 0) EXACT, named hgn
14.89/13.43/10.30/15.17, d* med 0.072, inner band worst
0.2819/3.5473 bit-near EXACT.
SEAL: partition 3.4e-16, ledger == genealogy == GMC 0.0, chain/
arm wards 0.0, contribution ward 2.1e-13/2.2e-12 (ladder/EXT3),
purity clean, toys exact; must-fails e1 CAUGHT twice (AST rho +
toy 1.0 != 0.5) / e2 LOUD (sum 4 != 3, break 1 EXACT) / e3
AST-CAUGHT (trs) / e4 AST-CAUGHT (S3) + m5a/m5b FLAGGED.

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
import companion_orbit_packing_probe as COP    # noqa: E402 r333
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
TB_WARD_BAR_X3 = 3e-5
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
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN = 1721
EXT3_NW_MAX = 2577
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
REC3_BAR_X3 = 1e-12
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
SA_BAR = 1e-12
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
BOUNDARY_F = 0.10
EDGE_R_F = 0.5
A_FAM = (0, 1, 2)
RBAND_MIN = 0.25
CBAND_MAX = 4.0
BAND_TOL = 1e-9
OVERLAP_CAP = 2
DELTA_CRIT = 0.112
N2_EXP_NEED = 0.888
NAMED_KZ = (53, 83, 67, 55)
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
INF_SENT = 1e300
CERT_GUARD = 1e299
R306_C2 = 1.069
R306_C2_TOL = 0.005
N335_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R333_BND_CNT = 44
R333_OIN_MED = 5
R333_OIN_MIN = 0
R333_OIN_MAX = 52
R333_NAMED_OIN = (0, 0, 2, 0)
R333_NAMED_HGN = (14.89, 13.43, 10.30, 15.17)
R333_HGN_TOL = 0.02
R333_RMIN_W = 0.2819
R333_CBAND_W = 3.5473
R333_BAND_TOL_A = 0.005
R333_DMED = 0.072
R333_DMED_TOL = 0.005
R335_TABLE_LITERALS = frozenset(COP.R333_TABLE_LITERALS | {
    0.2819, 3.5473, 0.072, 0.051, 233.66, 54.46, 12.69, 0.0238,
    0.1055, 0.4674, 0.148, 0.674, -0.004, 14.89, 13.43, 10.3,
    15.17, 3.7, 6.7, 3.1836})

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
    lies in the sealed r314..r333 record set."""
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
                            in R335_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the edge
# ---------------- builders consume the ledger (positions / masses /
# ---------------- parities / scale bins) + the support geometry
# ---------------- ONLY; the withheld terminal drive key, the branch
# ---------------- label, the cubic target M_3 and the q_max RECORD
# ---------------- are forbidden (AST identifier scan + literal
# ---------------- scan).  The dominant-pair argmax access lives in
# ---------------- the imported r333 COP.dominant_state (disclosed).
def edge_window(pmin, pmax, ps):
    """the SEALED ONE-SIDED REACH RULE: R = EDGE_R_F x W (the
    masked support radius, W = pmax - pmin); the window opens
    from the dominant position ps toward the FARTHER edge (the
    interior side): [ps, ps + R] if ps is nearer pmin, else
    [ps - R, ps].  Consumes the support geometry only."""
    reach = EDGE_R_F * (pmax - pmin)
    if ps - pmin <= pmax - ps:
        return ps, ps + reach
    return ps - reach, ps


def edge_orbit(led, sbins, sb, nw, sg, wlo, whi):
    """the SEALED ONE-SIDED COMPANION SELECTION (source-pure,
    sealed BEFORE any q_max sight): all fold groups of the SAME
    source-scale bin sb AND the SAME fold parity (window-atom
    count nw, group-value sign sg) whose position lies in the
    one-sided window [wlo, whi] and whose abs mass is positive.
    g* itself qualifies (ps is an endpoint), so the orbit is
    never empty on a live rung.  Consumes the ledger + the key +
    the window ONLY -- no block value, no target, no record."""
    gw = np.round(led["gwin"]).astype(int)
    sel = ((sbins == sb) & (gw == nw)
           & (np.sign(led["G1"]) == sg)
           & (led["gpos"] >= wlo) & (led["gpos"] <= whi)
           & (led["gabs"] > 0.0))
    return np.nonzero(sel)[0]


def edge_mass_state(led, gi, ilo, ihi):
    """the MARGIN MASS / ACTIVE-ANCESTOR CENSUS of g*'s own edge
    side: boundary case (gpos[gi] outside [ilo, ihi]) -- all
    groups with positive mass on g*'s side of the inner interval;
    inner case -- the pair itself (n = 1, S = gabs(g*)).  gabs(g*)
    <= S_marg holds EXACTLY because g* lies in its own selection.
    Consumes the ledger + the interval ONLY."""
    ps = float(led["gpos"][gi])
    if ilo <= ps <= ihi:
        return 1, float(led["gabs"][gi])
    if ps < ilo:
        sel = (led["gpos"] < ilo) & (led["gabs"] > 0.0)
    else:
        sel = (led["gpos"] > ihi) & (led["gabs"] > 0.0)
    return int(np.sum(sel)), float(np.sum(led["gabs"][sel]))


def dichotomy_state(ngj, kap, n_oe, rmin_e, s_marg, l1a):
    """the TWO EXACT ARMS and the sealed minimum: orbit arm
    Q_e = ng kappa/(|O_e| rmin_e) (partition chain on the edge
    orbit), mass arm M_b = ng kappa S_marg/L1_atom (via gabs(g*)
    <= S_marg); Q_dich = min; the arm letter types the rung by
    its smaller arm (ties to the orbit arm).  Consumes
    pre-computed source-side scalars only."""
    if n_oe > 0 and rmin_e > 0.0:
        q_e = ngj * kap / (n_oe * rmin_e)
    else:
        q_e = INF_SENT
    m_b = ngj * kap * s_marg / max(l1a, 1e-300)
    if q_e <= m_b:
        return q_e, m_b, q_e, "O"
    return q_e, m_b, m_b, "M"


def edge_tree(leak, wfail, go, partial):
    """the sealed five-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    WEIGHT_COMPARABILITY_FAIL > EDGE_PACKING_GO > EDGE_PARTIAL >
    EDGE_ORBIT_ALSO_SHORT."""
    if leak:
        return "TARGET_LEAK"
    if wfail:
        return "WEIGHT_COMPARABILITY_FAIL"
    if go:
        return "EDGE_PACKING_GO"
    if partial:
        return "EDGE_PARTIAL"
    return "EDGE_ORBIT_ALSO_SHORT"


def mutant_reach_posthoc(n_oe_seen, rho, cbar):
    """e1 MUST-FAIL MUTANT: the reach re-picked AFTER SIGHT of
    the orbit sizes and the evaluated bound column (consumes
    rho): widened to the full support until every seen violator
    is covered -- the BOUND_FORBIDDEN scope audit must FLAG it
    AND on the sealed toy it returns 1.0 != the canonical rule's
    EDGE_R_F -- CAUGHT twice."""
    w = EDGE_R_F
    for n, r in zip(n_oe_seen, rho):
        if r > cbar:
            w = max(w, 1.0)
    return w


def mutant_arm_double(letters):
    """e2 MUST-FAIL MUTANT: an arm census with one rung counted
    in BOTH arms -- the arm partition ward must REFUSE it
    (sum n+1 != n, break 1 EXACT)."""
    n_o = sum(1 for c in letters if c == "O") + 1
    n_m = sum(1 for c in letters if c == "M")
    return n_o, n_m


def mutant_orbit_posthoc(state):
    """e3 MUST-FAIL MUTANT: an 'orbit coordinate' consuming the
    q_max RECORD (the target-side concentration coordinate) --
    the QMAX_FORBIDDEN identifier scan must FLAG this (the edge
    orbit must be sealed BEFORE any q_max sight)."""
    tr = state["trs"]
    return float(tr["qmax"]) * float(state["m"])


def mutant_mass_from_target(ev):
    """e4 MUST-FAIL MUTANT: an 'edge-mass bound' derived from the
    cubic TARGET record (consumes cm/S3) -- the PHI3_FORBIDDEN
    scan must FLAG this while edge_mass_state stays clean."""
    return abs(float(ev["cm"]["S3"])) ** (1.0 / 3.0)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: an 'edge orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): an
    'edge constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the edge toy, the mass
# ---------------- arm and the arm partition decided as rationals
def fr_edge_toy():
    """the sealed seven-block edge toy in exact Fractions:
    support [0, 1] (light atoms 1 at pos 0 and 1, bin 2); g* =
    pair (5, 3) at 1/20 (BOUNDARY case, d* = 1/20, inner interval
    [1/10, 9/10]); companions c2 = (9/2, 3) at 3/50 and c1 =
    (7/2, 3) at 2/25 (bin 0, same parity); wrong-parity pair
    (-21/5, -3) at 7/100 EXCLUDED; same-key pair (49/10, 3) at
    19/20 EXCLUDED by the one-sided window [1/20, 11/20].  INNER
    orbit EMPTY (the r333 spike anatomy); O_e = {g*, c2, c1}
    EXACT; rmin_e = (13/2)/8 = 13/16; cband_e = 16/13; x = (8,
    13/2, 15/2, -36/5, 79/10, 1, 1) with |x_j| = A1_j so kappa =
    1; L = 391/10, q_max = 80/391; margin gpos < 1/10: n_marg =
    5, S_marg = 151/5; Q_e = 1/(3 x 13/16) = 16/39; M_b =
    (151/5)/(391/10) = 302/391; Q_dich = 16/39 (ORBIT arm);
    slack = 16/39 - 80/391 = 3136/15249 EXACT.  Returns (worst
    dev, slack, orbit sets ok, mass census ok)."""
    rmin = Fr(13, 2) / Fr(8)
    cband = Fr(8) / Fr(13, 2)
    L = Fr(8) + Fr(13, 2) + Fr(15, 2) + Fr(36, 5) + Fr(79, 10) \
        + Fr(1) + Fr(1)
    l1a = L
    kap = l1a / L
    qmx = Fr(8) / L
    s_marg = Fr(8) + Fr(13, 2) + Fr(15, 2) + Fr(36, 5) + Fr(1)
    q_e = Fr(1) * kap / (Fr(3) * rmin)
    m_b = Fr(1) * kap * s_marg / l1a
    q_d = min(q_e, m_b)
    slack = q_d - qmx
    devs = [abs(L - Fr(391, 10)), abs(qmx - Fr(80, 391)),
            abs(rmin - Fr(13, 16)), abs(cband - Fr(16, 13)),
            abs(kap - Fr(1)), abs(s_marg - Fr(151, 5)),
            abs(q_e - Fr(16, 39)), abs(m_b - Fr(302, 391)),
            abs(q_d - Fr(16, 39)),
            abs(slack - Fr(3136, 15249)),
            Fr(0) if qmx <= q_d else Fr(1),
            Fr(0) if q_e <= m_b else Fr(1),
            Fr(0) if rmin > Fr(1, 4) else Fr(1),
            Fr(0) if cband < Fr(4) else Fr(1)]
    # float construction cross-check via the real builders:
    pos = np.array([0.05, 0.05, 0.08, 0.08, 0.06, 0.06, 0.07,
                    0.07, 0.95, 0.95, 0.0, 1.0])
    val = np.array([5.0, 3.0, 3.5, 3.0, 4.5, 3.0, -4.2, -3.0,
                    4.9, 3.0, 1.0, 1.0])
    blk = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6])
    srcf = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
                     0.0, 1.0, 0.0, 0.0])
    led = COP.orbit_ledger(pos, val, blk, srcf, 7)
    sbins = QMO.scale_bins(led["gmax"])
    xs = np.array([8.0, 6.5, 7.5, -7.2, 7.9, 1.0, 1.0])
    ds = COP.dominant_state(xs, led, sbins)
    wlo, whi = edge_window(led["pmin"], led["pmax"], ds["ps"])
    orb_e = edge_orbit(led, sbins, ds["sb"], ds["nw"], ds["sg"],
                       wlo, whi)
    orb_in = COP.companion_orbit(led, sbins, ds["sb"], ds["nw"],
                                 ds["sg"], ds["ilo"], ds["ihi"])
    exp_e = tuple(sorted(int(i) for i in np.nonzero(
        (led["gblk"] == 0) | (led["gblk"] == 1)
        | (led["gblk"] == 2))[0]))
    orb_ok = (tuple(sorted(int(i) for i in orb_e)) == exp_e
              and len(orb_in) == 0 and (not ds["inner"])
              and ds["sb"] == 0 and ds["nw"] == 1 and ds["sg"] > 0
              and ds["ngj"] == 1
              and abs(wlo - 0.05) <= TOY_BAR
              and abs(whi - 0.55) <= TOY_BAR)
    n_marg, s_marg_f = edge_mass_state(led, ds["gi"], ds["ilo"],
                                       ds["ihi"])
    l1a_f = float(np.sum(led["gabs"]))
    mass_ok = (n_marg == 5
               and abs(s_marg_f - float(Fr(151, 5))) <= TOY_BAR
               and abs(l1a_f - float(Fr(391, 10))) <= TOY_BAR)
    q_e_f, m_b_f, q_d_f, arm_f = dichotomy_state(
        1, 1.0, len(orb_e), 13.0 / 16.0, s_marg_f, l1a_f)
    mass_ok = (mass_ok and arm_f == "O"
               and abs(q_e_f - float(Fr(16, 39))) <= TOY_BAR
               and abs(m_b_f - float(Fr(302, 391))) <= TOY_BAR
               and abs(q_d_f - float(Fr(16, 39))) <= TOY_BAR)
    return max(devs), slack, orb_ok, mass_ok


def fr_mass_toy():
    """the mass-arm toy in exact Fractions: a singleton edge orbit
    (|O_e| = 1, rmin = 1) with small margin share S_marg/L1 =
    1/10: Q_e = 1, M_b = 1/10, Q_dich = 1/10 (MASS arm); toy
    q_max = 1/20 <= 1/10, slack 1/20 EXACT.  The float builder
    reproduces the arm letter.  Returns (worst dev, arm ok)."""
    q_e = Fr(1) * Fr(1) / (Fr(1) * Fr(1))
    m_b = Fr(1) * Fr(1) * Fr(2) / Fr(20)
    q_d = min(q_e, m_b)
    slack = q_d - Fr(1, 20)
    devs = [abs(q_e - Fr(1)), abs(m_b - Fr(1, 10)),
            abs(q_d - Fr(1, 10)), abs(slack - Fr(1, 20)),
            Fr(0) if Fr(1, 20) <= q_d else Fr(1)]
    q_e_f, m_b_f, q_d_f, arm_f = dichotomy_state(
        1, 1.0, 1, 1.0, 2.0, 20.0)
    arm_ok = (arm_f == "M"
              and abs(q_e_f - 1.0) <= TOY_BAR
              and abs(m_b_f - 0.1) <= TOY_BAR
              and abs(q_d_f - 0.1) <= TOY_BAR)
    return max(devs), arm_ok


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("edge_packing_dichotomy_probe -- "
          "PRIME.TERMINAL.EDGE_PACKING.01 (round 335, the "
          "one-sided form after the r333 structural finding)")
    print("SPEC_SHA %s   R333_SHA %s   R327_SHA %s   R324_SHA %s"
          % (SPEC_SHA[:16], COP.SPEC_SHA[:16], GMC.SPEC_SHA[:16],
             QMO.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + ledger/band/overlap/arm "
                        "wards + e1-e4; ladder, extensions, EXT3, "
                        "anchors, census, certification and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE EDGE-PACKING ROUND (the r333 boundary finding as "
          "the main case): for every rung the dominant beta/omega "
          "pair g* (r333 machinery verbatim) gets a ONE-SIDED "
          "companion orbit O_e (same dyadic gmax bin + same fold "
          "parity, window [ps, ps +- R] toward the interior, R = "
          "EDGE_R_F %.1f x W the masked support radius, a-priori) "
          "AND a margin mass census (BOUNDARY_F %.2f, r333 "
          "verbatim); THE DICHOTOMY q_max <= min(Q_e, M_b) with "
          "Q_e = ng kappa/(|O_e| rmin_e) (partition chain) and "
          "M_b = ng kappa S_marg/L1 (via hga <= S_marg, exact) -- "
          "EITHER many companions OR small edge mass; "
          "certification B^D_a <= C_D(a) mid-ladder freeze, A_FAM "
          "%s, EXT3 = the r329 record 12 (committed 8cbd95f9) as "
          "PURE TEST rows; verdict tree TARGET_LEAK / WEIGHT_"
          "COMPARABILITY_FAIL / EDGE_PACKING_GO / EDGE_PARTIAL / "
          "EDGE_ORBIT_ALSO_SHORT sealed BEFORE evaluation"
          % (EDGE_R_F, BOUNDARY_F, str(A_FAM)))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("edge_window", "edge_orbit", "edge_mass_state",
               "dichotomy_state", "edge_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the five module-own "
          "edge builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the edge "
          "selection consumes ONLY the ledger + support geometry "
          "(sealed BEFORE any q_max sight); m5a gift-bound "
          "FLAGGED (%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r333 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3")
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
        check("G14-ext3-admission", True, "SMOKE: skipped")
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
        check("G14-ext3-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX,
              "EXT3 = the sealed r329 RECORD selection (committed "
              "8cbd95f9, adopted as-is): 12 anchors (B %s + A "
              "%s), POSITIVE_PREFIX %d/12, N_w %d..%d (record "
              "%d..%d) -- PURE TEST rows, never calibration"
              % (str(EXT3_KZ_B), str(EXT3_KZ_A),
                 sum(1 for p in ext3 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3),
                 EXT3_NW_MIN, EXT3_NW_MAX))

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
    x3recs = [rung_rec(p) for p in ext3] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs + e2recs + x3recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2+EXT3 census (no sealed expectation): %d "
              "cheap / %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + EDGE-LEDGER WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_x3 = 0.0
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
    for rc in x3recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x3 = max(tb_x3, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_x3 <= TB_WARD_BAR_X3
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d ext3 + %d mains + 3 controls: worst dev/absmass "
          "%.1e main N<=%d (bar %.0e) / %.1e deep / %.1e "
          "ext+ext2 (bar %.0e) / %.1e ext3 (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(x3recs),
             len(mrecs), tb_worst, DEEP_N, TB_WARD_BAR, tb_deep,
             tb_ext, TB_WARD_BAR_DEEP, tb_x3, TB_WARD_BAR_X3,
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
            led = COP.orbit_ledger(pos_all, val_all, blk_all,
                                   src_all, m)
            led327 = GMC.group_mass_ledger(pos_all, val_all,
                                           blk_all, src_all, m)
            sbins = QMO.scale_bins(led["gmax"])
            dst = COP.dominant_state(sct["x"], led, sbins)
            # inner orbit (r333 verbatim -- the cross census)
            orb_in = COP.companion_orbit(led, sbins, dst["sb"],
                                         dst["nw"], dst["sg"],
                                         dst["ilo"], dst["ihi"])
            nO_in = int(len(orb_in))
            if nO_in:
                oab_i = led["gabs"][orb_in]
                rmin_in = float(np.min(oab_i)) / max(dst["hga"],
                                                     1e-300)
                cband_in = float(np.max(oab_i)) \
                    / max(float(np.min(oab_i)), 1e-300)
            else:
                rmin_in = 0.0
                cband_in = 0.0
            # the sealed ONE-SIDED edge orbit
            wlo, whi = edge_window(led["pmin"], led["pmax"],
                                   dst["ps"])
            orb_e = edge_orbit(led, sbins, dst["sb"], dst["nw"],
                               dst["sg"], wlo, whi)
            nOe = int(len(orb_e))
            memb = np.bincount(orb_e) if nOe else np.zeros(0, int)
            ovl = int(np.max(memb)) if nOe else 0
            if nOe:
                oab = led["gabs"][orb_e]
                rmin_e = float(np.min(oab)) / max(dst["hga"],
                                                  1e-300)
                cband_e = float(np.max(oab)) \
                    / max(float(np.min(oab)), 1e-300)
                S_Oe = float(np.sum(oab))
            else:
                rmin_e = 0.0
                cband_e = 0.0
                S_Oe = 0.0
            L1a = float(np.sum(led["gabs"]))
            Lb = float(np.sum(np.abs(sct["x"])))
            kap = L1a / max(Lb, 1e-300)
            n_marg, S_marg = edge_mass_state(led, dst["gi"],
                                             dst["ilo"],
                                             dst["ihi"]) \
                if dst["gi"] >= 0 else (0, 0.0)
            Qe, Mb, Qd, arm = dichotomy_state(dst["ngj"], kap,
                                              nOe, rmin_e,
                                              S_marg, L1a)
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
            dst = COP.dominant_state(np.zeros(0), led, sbins)
            orb_in = np.zeros(0, int)
            nO_in = 0
            rmin_in = 0.0
            cband_in = 0.0
            wlo = whi = 0.0
            orb_e = np.zeros(0, int)
            nOe = 0
            ovl = 0
            rmin_e = 0.0
            cband_e = 0.0
            S_Oe = 0.0
            L1a = 0.0
            kap = 0.0
            n_marg = 0
            S_marg = 0.0
            Qe = INF_SENT
            Mb = INF_SENT
            Qd = INF_SENT
            arm = "-"
            nband = 0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led=led, led327=led327, sbins=sbins, dst=dst,
                    orb_in=orb_in, nO_in=nO_in, rmin_in=rmin_in,
                    cband_in=cband_in, wlo=wlo, whi=whi,
                    orb_e=orb_e, nOe=nOe, ovl=ovl, rmin_e=rmin_e,
                    cband_e=cband_e, S_Oe=S_Oe, L1a=L1a, kap=kap,
                    n_marg=n_marg, S_marg=S_marg, Qe=Qe, Mb=Mb,
                    Qd=Qd, arm=arm, nband=nband,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs + x3recs
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
    x3_mult_ok = True
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
    for rc in x3recs:
        if rc["ev"]["mx_mult"] > MULT_CAP:
            x3_mult_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and gpos_ok and x3_mult_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r333 orbit ledger segments IDENTICALLY to the "
          "genealogy AND to the r327 GMC ledger (worst dev %.1e, "
          "bar %.0e); gpos position-sorted within every block "
          "(%s); EXT3 fold multiplicity <= %d on 12/12 (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             "OK" if gpos_ok else "BROKEN", MULT_CAP,
             "OK" if x3_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim + r316/r333 record)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim + the r333 "
            "record)")
    x3_ids = set(id(rc) for rc in x3recs)
    live_69 = [rc for rc in live if id(rc) not in x3_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    tel_x = max((rc["ev"]["tel_dev"] for rc in x3recs),
                default=0.0)
    bnd_x = max((rc["ev"]["bnd_dev"] for rc in x3recs),
                default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and tel_x <= REC3_BAR_X3 and bnd_x <= REC3_BAR_X3,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e (bars %.0e); "
          "EXT3 %.1e / %.1e / %.1e (bar %.0e, r329 a-priori); "
          "DISCLOSED slim anchor set -- the full chain is "
          "re-warded by the sealed r321/r324/r327/r333 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, tel_x,
             bnd_x, REC3_BAR_X3))
    if smoke:
        ev9s = recs[0]["ev"]
        ds9 = ev9s["dst"]
        info("SMOKE: w9 m %d ng* %d hgn %.4f |Oin| %d |Oe| %d "
             "rmin_e %.3f cb_e %.3f kap %.3f Qe %.4f Mb %.4f Qd "
             "%.4f arm %s case %s nmarg %d"
             % (ev9s["m"], ds9["ngj"], ds9["hgn"], ev9s["nO_in"],
                ev9s["nOe"], ev9s["rmin_e"], ev9s["cband_e"],
                ev9s["kap"], min(ev9s["Qe"], 9999.0),
                min(ev9s["Mb"], 9999.0), min(ev9s["Qd"], 9999.0),
                ev9s["arm"], "I" if ds9["inner"] else "B",
                ev9s["n_marg"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r333-anchors", True, "SMOKE: skipped")
        srt = []
        n335 = 0
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
        n335 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n335)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n335 == N335_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n335, N335_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n335):
                if srt[i]["kz"] == kz:
                    named_rank[kz] = i
        # r333 anchors: the inner-orbit anatomy re-derived
        oin_col = [rc["ev"]["nO_in"] for rc in srt]
        inner_col = [rc["ev"]["dst"]["inner"] for rc in srt]
        d_col = [rc["ev"]["dst"]["d"] for rc in srt]
        hgn_col = [rc["ev"]["dst"]["hgn"] for rc in srt]
        bnd_cnt = sum(1 for v in inner_col if not v)
        named_oin = tuple(oin_col[named_rank[kz]]
                          for kz in NAMED_KZ)
        named_hgn = tuple(hgn_col[named_rank[kz]]
                          for kz in NAMED_KZ)
        rmin_w_in = 1.0
        cband_w_in = 1.0
        for rc in live_69:
            ev = rc["ev"]
            if ev["nO_in"]:
                rmin_w_in = min(rmin_w_in, ev["rmin_in"])
                cband_w_in = max(cband_w_in, ev["cband_in"])
        check("G33-r333-anchors",
              bnd_cnt == R333_BND_CNT
              and int(np.median(oin_col)) == R333_OIN_MED
              and min(oin_col) == R333_OIN_MIN
              and max(oin_col) == R333_OIN_MAX
              and named_oin == R333_NAMED_OIN
              and all(abs(named_hgn[k] - R333_NAMED_HGN[k])
                      <= R333_HGN_TOL for k in range(4))
              and abs(float(np.median(d_col)) - R333_DMED)
              <= R333_DMED_TOL
              and abs(rmin_w_in - R333_RMIN_W) <= R333_BAND_TOL_A
              and abs(cband_w_in - R333_CBAND_W)
              <= R333_BAND_TOL_A,
              "the r333 RECORD reproduced bit-near: boundary %d/"
              "%d (rec %d); |O_in| med/min/max %d/%d/%d (rec "
              "%d/%d/%d); named inner quartet %s == %s EXACT; "
              "named hgn %s (rec %s tol %.2f); d* med %.3f (rec "
              "%.3f); inner band worst rmin %.4f / cband %.4f "
              "(rec %.4f / %.4f, over the r333 69-world live "
              "set)"
              % (bnd_cnt, n335, R333_BND_CNT,
                 int(np.median(oin_col)), min(oin_col),
                 max(oin_col), R333_OIN_MED, R333_OIN_MIN,
                 R333_OIN_MAX, str(named_oin),
                 str(R333_NAMED_OIN),
                 str(tuple(round(v, 2) for v in named_hgn)),
                 str(R333_NAMED_HGN), R333_HGN_TOL,
                 float(np.median(d_col)), R333_DMED, rmin_w_in,
                 cband_w_in, R333_RMIN_W, R333_CBAND_W))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("edge_window", "edge_orbit", "edge_mass_state",
               "dichotomy_state", "edge_tree", "fr_edge_toy",
               "fr_mass_toy"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_reach_posthoc", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_orbit_posthoc", QMAX_FORBIDDEN)
    e4_hits = scope_audit("mutant_mass_from_target",
                          PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e3_hits) >= 1
          and len(e4_hits) >= 1,
          "SOURCE PURITY: the edge builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed r314..."
          "r333 record-literal set (%d literal hits); consumed "
          "inputs: ledger + support geometry ONLY -- M_3, rho_2 "
          "and the q_max RECORD are TARGET-SIDE, computed outside "
          "the builders (disclosed; kappa likewise); e1 "
          "reach-posthoc FLAGGED (%s); e3 orbit-posthoc FLAGGED "
          "(%s); e4 mass-from-target FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    fr_dev, fr_slack, fr_orb_ok, fr_mass_ok = fr_edge_toy()
    fm_dev, fm_arm_ok = fr_mass_toy()
    toy_letters = ("O", "M", "O")
    live_cnt = (sum(1 for c in toy_letters if c == "O"),
                sum(1 for c in toy_letters if c == "M"))
    mut_cnt = mutant_arm_double(toy_letters)
    arm_break = (mut_cnt[0] + mut_cnt[1]) - len(toy_letters)
    tr_br = (edge_tree(True, True, True, True),
             edge_tree(False, True, True, True),
             edge_tree(False, False, True, True),
             edge_tree(False, False, False, True),
             edge_tree(False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "WEIGHT_COMPARABILITY_FAIL",
                      "EDGE_PACKING_GO", "EDGE_PARTIAL",
                      "EDGE_ORBIT_ALSO_SHORT")
    check("G41-toy-exactness",
          fr_dev == 0 and fr_orb_ok and fr_mass_ok
          and fm_dev == 0 and fm_arm_ok
          and live_cnt[0] + live_cnt[1] == len(toy_letters)
          and arm_break == 1 and ok_tr,
          "the Fractions edge toy EXACT (worst dev %s): INNER "
          "orbit EMPTY while O_e = {g*, c2, c1} (the r333 spike "
          "anatomy reproduced), rmin_e 13/16, cband_e 16/13, Q_e "
          "16/39, margin (5, 151/5), M_b 302/391, Q_dich 16/39 "
          "ORBIT arm, q_max 80/391 <= Q_dich slack %s EXACT; the "
          "real builders reproduce window/orbit/margin/arm; the "
          "mass-arm toy EXACT (worst %s, MASS arm, slack 1/20); "
          "arm partition (2, 1) sum 3 EXACT, double-count mutant "
          "break %d EXACT (REFUSED); edge_tree all five branches "
          "EXACT %s"
          % (str(fr_dev), str(fr_slack), str(fm_dev), arm_break,
             str(tr_br)))
    # live wards
    chain_w = 0.0
    xw_cube = 0.0
    interp_w = 0.0
    part_w = 0.0
    band_ok = True
    band_worst_r = 1.0
    band_worst_c = 1.0
    ovl_worst = 0
    qe_w = 0.0
    mb_w = 0.0
    qd_w = 0.0
    a1_w = 0.0
    smarg_w = 0.0
    kap_min = float("inf")
    mult_all_ok = True
    arm_part_ok = True
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
        a1_w = max(a1_w,
                   max(0.0, mloc * qmx - mloc * ds["a1j"] / Lx)
                   / max(mloc * ds["a1j"] / Lx, 1e-300),
                   max(0.0, ds["a1j"] - ds["ngj"] * ds["hga"])
                   / max(ds["ngj"] * ds["hga"], 1e-300))
        # the mass-arm exactness gabs(g*) <= S_marg
        smarg_w = max(smarg_w,
                      max(0.0, ds["hga"] - ev["S_marg"])
                      / max(ev["S_marg"], 1e-300))
        if ev["nOe"]:
            band_worst_r = min(band_worst_r, ev["rmin_e"])
            band_worst_c = max(band_worst_c, ev["cband_e"])
            if not (ev["rmin_e"] > RBAND_MIN * (1.0 - BAND_TOL)
                    and ev["cband_e"] < CBAND_MAX
                    * (1.0 + BAND_TOL)):
                band_ok = False
            ovl_worst = max(ovl_worst, ev["ovl"])
            qe_w = max(qe_w, max(0.0, qmx - ev["Qe"])
                       / max(ev["Qe"], 1e-300))
            kap_min = min(kap_min, ev["kap"])
        mb_w = max(mb_w, max(0.0, qmx - ev["Mb"])
                   / max(ev["Mb"], 1e-300))
        qd_w = max(qd_w, max(0.0, qmx - ev["Qd"])
                   / max(ev["Qd"], 1e-300))
        if ev["arm"] not in ("O", "M"):
            arm_part_ok = False
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(ev["gen"]["mult"])[1]
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and part_w <= SA_BAR
          and band_ok and ovl_worst <= OVERLAP_CAP
          and qe_w <= CHAIN_BAR and mb_w <= CHAIN_BAR
          and qd_w <= CHAIN_BAR and a1_w <= CHAIN_BAR
          and smarg_w <= CHAIN_BAR
          and kap_min >= 1.0 - CHAIN_BAR and mult_all_ok
          and arm_part_ok,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 interpolation (worst "
          "%.1e); GROUP PARTITION sum_g gabs == A1_j (worst "
          "%.1e, bar %.0e); THE BAND THEOREM on the EDGE orbit: "
          "rmin_e worst %.4f > 1/4 AND cband_e worst %.4f < 4 "
          "(T2 at b = 0, exact algebra); THE OVERLAP WARD: max "
          "membership %d <= %d (T3, partition-exact); THE TWO "
          "EXACT ARMS: q_max <= Q_e (worst %.1e) AND q_max <= "
          "M_b (worst %.1e, via hga <= S_marg worst %.1e) AND "
          "q_max <= Q_dich (worst %.1e); chain q_max <= A1*/L "
          "<= ng* hga/L (worst %.1e); ARM PARTITION every rung "
          "exactly one letter (%s); kappa min %.4f >= 1; fold "
          "multiplicity <= %d admitted on ALL live worlds"
          % (len(live), chain_w, xw_cube, interp_w, part_w,
             SA_BAR, band_worst_r, band_worst_c, ovl_worst,
             OVERLAP_CAP, qe_w, mb_w, smarg_w, qd_w, a1_w,
             "OK" if arm_part_ok else "BROKEN", kap_min,
             MULT_CAP))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        srt_x = sorted(x3recs, key=lambda rc: (rc["N"], rc["kz"]))
        srt_x = [rc for rc in srt_x
                 if rc["ev"]["mx_mult"] <= MULT_CAP
                 and not rc["ev"]["degenerate"]]
        n_x3 = len(srt_x)
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt_full]
        G_col = [m_full[i] * qmax_col[i] for i in range(n_full)]
        ngf_col = [rc["ev"]["dst"]["ngj"] for rc in srt_full]
        hgnf_col = [rc["ev"]["dst"]["hgn"] for rc in srt_full]
        oinf_col = [rc["ev"]["nO_in"] for rc in srt_full]
        oe_col = [rc["ev"]["nOe"] for rc in srt_full]
        rme_col = [rc["ev"]["rmin_e"] for rc in srt_full]
        cbe_col = [rc["ev"]["cband_e"] for rc in srt_full]
        kap_col = [rc["ev"]["kap"] for rc in srt_full]
        Qe_col = [rc["ev"]["Qe"] for rc in srt_full]
        Mb_col = [rc["ev"]["Mb"] for rc in srt_full]
        Qd_col = [rc["ev"]["Qd"] for rc in srt_full]
        arm_col = [rc["ev"]["arm"] for rc in srt_full]
        innf_col = [rc["ev"]["dst"]["inner"] for rc in srt_full]
        sbf_col = [rc["ev"]["dst"]["sb"] for rc in srt_full]
        df_col = [rc["ev"]["dst"]["d"] for rc in srt_full]
        nmg_col = [rc["ev"]["n_marg"] for rc in srt_full]
        smf_col = [rc["ev"]["S_marg"]
                   / max(rc["ev"]["L1a"], 1e-300)
                   for rc in srt_full]
        BD1_col = [min(m_full[i] * Qd_col[i]
                       / (math.log(float(m_full[i])) ** 2),
                       INF_SENT) for i in range(n_full)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m G ng* hgn |Oin| "
             "|Oe| rmin_e cb_e kap Qe Mb Qd arm case s* d* "
             "nmarg smarg/L1  [rows 65..%d are EXT3 PURE TEST]"
             % (n_full - 1))
        for i, rc in enumerate(srt_full):
            info("%2d kz%-3d N %4d m %3d G %6.3f ng %2d hgn "
                 "%6.3f |Oi| %3d |Oe| %3d rm %.3f cb %.3f kap "
                 "%.3f Qe %8.4f Mb %8.4f Qd %8.4f %s %s s%d d "
                 "%.3f nm %3d sf %.3f%s"
                 % (i, rc["kz"], rc["N"], m_full[i], G_col[i],
                    ngf_col[i], hgnf_col[i], oinf_col[i],
                    oe_col[i], rme_col[i], cbe_col[i],
                    kap_col[i], min(Qe_col[i], 9999.0),
                    min(Mb_col[i], 9999.0),
                    min(Qd_col[i], 9999.0), arm_col[i],
                    "I" if innf_col[i] else "B", sbf_col[i],
                    df_col[i], nmg_col[i], smf_col[i],
                    " X3" if i >= n335 else ""))
        check("G43-coordinate-table", True,
              "|O_e| range %d/%.0f/%d min/med/max (vs |O_in| "
              "%d/%.0f/%d); rmin_e med %.3f; cband_e med %.3f; "
              "kappa med %.3f; Qe med %.3f; Mb med %.3f; Qd med "
              "%.3f max %.2f (max at kz%d); arm census O %d / M "
              "%d; n_marg med %.0f; smarg/L1 med %.3f; EXT3 "
              "rows %d"
              % (min(oe_col), float(np.median(oe_col)),
                 max(oe_col), min(oinf_col),
                 float(np.median(oinf_col)), max(oinf_col),
                 float(np.median(rme_col)),
                 float(np.median(cbe_col)),
                 float(np.median(kap_col)),
                 float(np.median([min(v, 9999.0)
                                  for v in Qe_col])),
                 float(np.median([min(v, 9999.0)
                                  for v in Mb_col])),
                 float(np.median([min(v, 9999.0)
                                  for v in Qd_col])),
                 max(min(v, 9999.0) for v in Qd_col),
                 srt_full[int(np.argmax([min(v, 9999.0)
                                         for v in Qd_col]))]
                 ["kz"],
                 sum(1 for c in arm_col if c == "O"),
                 sum(1 for c in arm_col if c == "M"),
                 float(np.median(nmg_col)),
                 float(np.median(smf_col)), n_x3))

    # ---------------- S5: Leg B -- edge census + worlds
    section("S5  LEG B -- EDGE CENSUS + NAMED ANATOMY + WORLDS")
    if smoke:
        check("G50-edge-census", True, "SMOKE: skipped")
        check("G51-named-anatomy", True, "SMOKE: skipped")
    else:
        bnd_i = [i for i in range(n335) if not innf_col[i]]
        empty_in = [i for i in range(n335) if oinf_col[i] == 0]
        gained = [i for i in empty_in if oe_col[i] > 1]
        check("G50-edge-census",
              min(oe_col) >= 1
              and sum(1 for c in arm_col if c in ("O", "M"))
              == n_full,
              "EDGE CENSUS: |O_e| med %.0f min %d (>= 1 "
              "structurally, the r333 sentinel eliminated); "
              "inner-empty rungs %d, of which %d gained edge "
              "companions beyond g* itself; boundary %d/%d; "
              "|O_e| > |O_in| on %d rungs; arm partition O %d + "
              "M %d == %d EXACT; margin ancestors n_marg med "
              "%.0f max %d; margin share S_marg/L1 med %.3f "
              "max %.3f"
              % (float(np.median(oe_col)), min(oe_col),
                 len(empty_in), len(gained), len(bnd_i), n335,
                 sum(1 for i in range(n335)
                     if oe_col[i] > oinf_col[i]),
                 sum(1 for c in arm_col if c == "O"),
                 sum(1 for c in arm_col if c == "M"), n_full,
                 float(np.median(nmg_col)), max(nmg_col),
                 float(np.median(smf_col)), max(smf_col)))
        oe_med = float(np.median([oe_col[i] for i in
                                  range(n335)]))
        named_tab = {}
        for kz in NAMED_KZ:
            i = named_rank[kz]
            named_tab[kz] = (oe_col[i], arm_col[i],
                             min(Qd_col[i], 9999.0),
                             min(BD1_col[i], 9999.0))
            info("named kz%-3d: |Oin| %d -> |Oe| %d (med %.0f) "
                 "rmin_e %.3f cb_e %.3f kap %.3f hgn %.2f nmarg "
                 "%d smarg/L1 %.3f Qe %.3f Mb %.3f Qd %.3f arm "
                 "%s BD1 %.3f case %s"
                 % (kz, oinf_col[i], oe_col[i], oe_med,
                    rme_col[i], cbe_col[i], kap_col[i],
                    hgnf_col[i], nmg_col[i], smf_col[i],
                    min(Qe_col[i], 9999.0),
                    min(Mb_col[i], 9999.0),
                    min(Qd_col[i], 9999.0), arm_col[i],
                    min(BD1_col[i], 9999.0),
                    "I" if innf_col[i] else "B"))
        check("G51-named-anatomy", True,
              "THE SPIKE HARDNESS TEST (which dichotomy arm "
              "covers each named rung): %s -- (|O_e|, arm, "
              "Q_dich, B^D_1) per named kz; reserves against "
              "the frozen constants adjudicated in S6"
              % str(named_tab))
    # world census (both modes; uses w9 or mains + controls)
    ev9w = (recs[0] if smoke else mrecs[0])["ev"]
    ev13 = None if smoke else mrecs[1]["ev"]
    wtab = [("w9", ev9w)] + ([("w13(twin)", ev13)]
                             if ev13 is not None else [])
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]["ev"]))
    info("world table: world m |Oin| |Oe| rmin_e cb_e kap Qe Mb "
         "Qd arm case nbands nmarg")
    for w, ev in wtab:
        ds = ev["dst"]
        info("  %-10s m %3d |Oi| %3d |Oe| %3d rm %.3f cb %.3f "
             "kap %.3f Qe %8.4f Mb %8.4f Qd %8.4f %s %s nb %d "
             "nm %d"
             % (w, ev["m"], ev["nO_in"], ev["nOe"], ev["rmin_e"],
                ev["cband_e"], ev["kap"], min(ev["Qe"], 9999.0),
                min(ev["Mb"], 9999.0), min(ev["Qd"], 9999.0),
                ev["arm"], "I" if ds["inner"] else "B",
                ev["nband"], ev["n_marg"]))
    scr_ev = crecs["SCR"]["ev"]
    check("G52-world-census", len(wtab) >= 2,
          "Q4 WORLD CHECK (census, NO claim): twin w13 runs the "
          "IDENTICAL sealed construction (all exact wards above "
          "include it); EPSTEIN: |O_e| %d vs w9 %d (bands %d vs "
          "%d); SCRAMBLE edge orbit: |O_e| %d (inner was 0 in "
          "r333) vs w9 %d -- the one-sided decay question "
          "answered by these numbers"
          % (crecs["EPST"]["ev"]["nOe"], ev9w["nOe"],
             crecs["EPST"]["ev"]["nband"], ev9w["nband"],
             scr_ev["nOe"], ev9w["nOe"]))

    # ---------------- S6: Leg C -- certification + exponents
    section("S6  LEG C -- T1-EDGE / ARMS / DICHOTOMY "
            "CERTIFICATION + EXPONENTS")
    if smoke:
        check("G60-T1-edge", True, "SMOKE: skipped")
        check("G61-T2-band", True, "SMOKE: skipped")
        check("G62-single-arms", True, "SMOKE: skipped")
        check("G63-dichotomy", True, "SMOKE: skipped")
        check("G64-growth-exponents", True, "SMOKE: skipped")
    else:
        te_x = list(te_i) + list(range(n335, n_full))
        t1e = {}
        for a in A_FAM:
            col = [oe_col[i] * (math.log(float(m_full[i])) ** a)
                   / float(m_full[i]) for i in range(n_full)]
            c0 = min(col[i] for i in ca_i)
            viol = [i for i in te_x if col[i] < c0]
            named = sum(1 for kz in NAMED_KZ
                        if col[named_rank[kz]] >= c0)
            t1e[a] = (c0, viol, named, col)
        aT1e = None
        for a in A_FAM:
            if not t1e[a][1] and t1e[a][2] == len(NAMED_KZ):
                aT1e = a
                break
        check("G60-T1-edge", True,
              "T1-EDGE |O_e| >= c_0 m/(log m)^a (min-cal freeze, "
              "test incl. EXT3): "
              + "; ".join("a=%d c_0 %.4f viol %d/%d named %d/4"
                          % (a, t1e[a][0], len(t1e[a][1]),
                             len(te_x), t1e[a][2])
                          for a in A_FAM)
              + "; worst violators %s; minimal certifying a = %s"
              % (str([(srt_full[i]["kz"],
                       round(t1e[A_FAM[-1]][3][i], 4))
                      for i in t1e[A_FAM[-1]][1][:6]]),
                 str(aT1e)))
        check("G61-T2-band", band_ok,
              "T2 THE BAND THEOREM on the EDGE orbit (b = 0, "
              "c_1 = 1/4, EXACT inside one dyadic gmax bin): "
              "rmin_e worst %.4f > 0.25 and cband_e worst %.4f "
              "< 4 on every live edge orbit -- certified at "
              "theorem grade (gated in G42)"
              % (band_worst_r, band_worst_c))

        def cert_max(vals_col):
            out = {}
            for a in A_FAM:
                col = [min(vals_col[i] * float(m_full[i])
                           / (math.log(float(m_full[i]))
                              ** (1 + a)), INF_SENT)
                       for i in range(n_full)]
                CQ = max(col[i] for i in ca_i)
                viol = [i for i in te_x if col[i] > CQ]
                named = sum(1 for kz in NAMED_KZ
                            if col[named_rank[kz]] <= CQ)
                out[a] = (CQ, viol, named, col)
            aa = None
            for a in A_FAM:
                if (not out[a][1] and out[a][2] == len(NAMED_KZ)
                        and out[a][0] < CERT_GUARD):
                    aa = a
                    break
            return out, aa

        certO, aO = cert_max(Qe_col)
        certM, aM = cert_max(Mb_col)
        certD, aD = cert_max(Qd_col)
        check("G62-single-arms", True,
              "SINGLE ARMS (max-cal freeze, test incl. EXT3): "
              "ORBIT B^O_a: "
              + "; ".join("a=%d C_O %.3f viol %d named %d/4"
                          % (a, min(certO[a][0], 9999.0),
                             len(certO[a][1]), certO[a][2])
                          for a in A_FAM)
              + " (min a %s) | MASS B^M_a: " % str(aO)
              + "; ".join("a=%d C_M %.3f viol %d named %d/4"
                          % (a, min(certM[a][0], 9999.0),
                             len(certM[a][1]), certM[a][2])
                          for a in A_FAM)
              + " (min a %s)" % str(aM))
        check("G63-dichotomy", True,
              "THE DICHOTOMY B^D_a = m min(Q_e, M_b)/(log m)^"
              "{1+a} <= C_D(a) (max-cal freeze): "
              + "; ".join("a=%d C_D %.4f viol %d/%d named %d/4"
                          % (a, min(certD[a][0], 9999.0),
                             len(certD[a][1]), len(te_x),
                             certD[a][2]) for a in A_FAM)
              + "; worst violators %s; minimal certifying a = %s"
              % (str([(srt_full[i]["kz"],
                       round(min(certD[A_FAM[-1]][3][i],
                                 9999.0), 3))
                      for i in sorted(
                          certD[A_FAM[-1]][1],
                          key=lambda i:
                          -certD[A_FAM[-1]][3][i])[:6]]),
                 str(aD)))
        msT = [m_full[i] for i in te_i]
        e_hgn = L2D.halves_slope(msT, [max(hgnf_col[i], 1e-300)
                                       for i in te_i])
        e_BD1 = L2D.halves_slope(msT, [max(min(BD1_col[i],
                                               INF_SENT), 1e-300)
                                       for i in te_i])
        h = len(te_i) // 2
        te_a = te_i[:h]
        te_b = te_i[h:]

        def ehgn_on(idx):
            return L2D.halves_slope([m_full[i] for i in idx],
                                    [max(hgnf_col[i], 1e-300)
                                     for i in idx])

        e_a = ehgn_on(te_a)
        e_b = ehgn_on(te_b)
        decided = ((e_a < DELTA_CRIT) == (e_b < DELTA_CRIT)
                   and (e_a < DELTA_CRIT)
                   == (e_hgn < DELTA_CRIT))
        x3_idx = list(range(n335, n_full))
        e_x3 = L2D.halves_slope(
            [m_full[i] for i in x3_idx],
            [max(min(Qd_col[i], INF_SENT)
                 * float(m_full[i]), 1e-300) for i in x3_idx]) \
            if len(x3_idx) >= 2 else 0.0
        check("G64-growth-exponents", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope, "
              "fit-free, over the %d 65-ladder test rungs): "
              "delta = e(hgn) = %+.3f vs DELTA_CRIT %.3f "
              "(census continuity with r333, NOT adjudicating); "
              "e(B^D_1) = %+.3f; stability halves %+.3f / %+.3f "
              "-> %s; EXT3 cohort e(m Q_dich) = %+.3f "
              "(census-grade, mixed strata, r329 caveat)"
              % (len(te_i), e_hgn, DELTA_CRIT, e_BD1, e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED", e_x3))

    # ---------------- S7: Leg D -- adjudication + composition
    section("S7  LEG D -- SEALED ADJUDICATION + COMPOSITION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        wfail = (not band_ok) or ovl_worst > OVERLAP_CAP
        go = aD is not None
        partial = (not go) and (aT1e is not None
                                or aO is not None
                                or aM is not None)
        vkey = edge_tree(leak, wfail, go, partial)
        missing = []
        if aT1e is None:
            missing.append("T1-edge")
        if aO is None:
            missing.append("orbit arm")
        if aM is None:
            missing.append("mass arm")
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on an edge "
                           "builder",
            "WEIGHT_COMPARABILITY_FAIL":
                "the exact band/overlap ward broke (rmin_e "
                "%.4f, cband_e %.4f, ovl %d)"
                % (band_worst_r, band_worst_c, ovl_worst),
            "EDGE_PACKING_GO":
                "the DICHOTOMY certifies at a = %s: C_D %.4f "
                "(0 viol incl. EXT3, named 4/4); T1-edge min a "
                "%s (c_0 %s); arms: orbit min a %s / mass min "
                "a %s"
                % (str(aD),
                   certD[aD][0] if aD is not None else 0.0,
                   str(aT1e),
                   ("%.4f" % t1e[aT1e][0]) if aT1e is not None
                   else "-", str(aO), str(aM)),
            "EDGE_PARTIAL":
                "certifying: %s; MISSING: %s; dichotomy worst "
                "violators %s"
                % (", ".join(s for s, aa in
                             (("T1-edge(a=%s)" % str(aT1e),
                               aT1e),
                              ("orbit(a=%s)" % str(aO), aO),
                              ("mass(a=%s)" % str(aM), aM))
                             if aa is not None) or "none",
                   ", ".join(missing),
                   str([srt_full[i]["kz"]
                        for i in certD[A_FAM[-1]][1][:4]])),
            "EDGE_ORBIT_ALSO_SHORT":
                "no clause certifies (T1-edge/orbit/mass/"
                "dichotomy all fail at every a in %s; worst "
                "%s) -- the packing language is exhausted at "
                "the edge; the reviewer's martingale second "
                "route is next (NAMED ONLY, not executed)"
                % (str(A_FAM),
                   str([srt_full[i]["kz"]
                        for i in certD[A_FAM[-1]][1][:4]]))}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        # composition (printed ALWAYS, honestly typed)
        if vkey == "EDGE_PACKING_GO":
            Atot = 1 + aD
            C_full = certD[aD][0]
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
            replaces = (m_star_l10 is not None
                        and m_star_l10 <= 59.6)
            info("COMPOSITION (dichotomy pointwise-certified, "
                 "mid-ladder): q_max <= %.4f (log m)^%d/m => "
                 "M_3 <= q_max^2 (S0 exact) => N_2 >= 1/q_max "
                 ">= m/(%.4f (log m)^%d) => N_2 >= m^%.3f for "
                 "all m >= m_0* = %s => the r297 target chain; "
                 "R324 COMPARISON: the r324 MEASURED route has "
                 "m_0* 10^59.6 via the +0.172 exponent -- the "
                 "dichotomy %s the +0.172 exponent on the "
                 "measured ladder (m_0* %s vs 10^59.6); the "
                 "ladder-to-m_0* step stays the disclosed "
                 "extrapolation hypothesis."
                 % (C_full, Atot, C_full, Atot, N2_EXP_NEED,
                    ms_txt,
                    "REPLACES" if replaces else
                    "does NOT replace", ms_txt))
            comp_ok = True
            comp_txt = "GO: q_max <= %.4f (log m)^%d/m, m_0* " \
                "%s, r324 %s" \
                % (C_full, Atot, ms_txt,
                   "replaced" if replaces else "kept")
        else:
            envO = min(max(certO[1][3]), 9999.0)
            envM = min(max(certM[1][3]), 9999.0)
            envD = min(max(certD[1][3]), 9999.0)
            info("COMPOSITION: no GO letter -- the r324 "
                 "MEASURED composition stands unchanged (sum "
                 "q^3 <= 8.941 (log m) m^{+0.172}/m^2, N_2 >= "
                 "m^0.888 for m >= 10^59.6); measured edge-"
                 "route envelopes at a = 1: max B^O_1 %.3f, "
                 "max B^M_1 %.3f, max B^D_1 %.3f; e(hgn) "
                 "%+.3f, e(B^D_1) %+.3f."
                 % (envO, envM, envD, e_hgn, e_BD1))
            comp_ok = True
            comp_txt = "r324 restated; edge envelopes B^O_1 " \
                "%.3f / B^M_1 %.3f / B^D_1 %.3f" \
                % (envO, envM, envD)
        check("G71-composition", comp_ok,
              "composition printed with explicit constants "
              "(%s); the chain to terminal_positive_main is "
              "typed: band/overlap/arm algebra exact, every "
              "constant MEASURED on the finite ladder + EXT3, "
              "the ladder-to-m_0* step an extrapolation "
              "hypothesis -- NO cofinal claim" % comp_txt)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toy_no = (1, 5)
    toy_rho = (0.9, 0.1)
    rw_mut = mutant_reach_posthoc(toy_no, toy_rho, 0.5)
    check("G80-e1-reach-posthoc",
          len(e1_hits) >= 1 and abs(rw_mut - 1.0) <= TOY_BAR
          and abs(rw_mut - EDGE_R_F) >= MUT_MIN,
          "e1 CAUGHT twice: the after-sight reach re-pick "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s) -- and on the toy returns %.1f != the canonical "
          "rule's %.1f (a reach widened after sight of the "
          "orbit sizes is structurally refused)"
          % (e1_hits[0] if e1_hits else "MISS", rw_mut,
             EDGE_R_F))
    check("G81-e2-arm-double",
          arm_break == 1
          and mut_cnt[0] + mut_cnt[1] > len(toy_letters)
          and live_cnt[0] + live_cnt[1] == len(toy_letters),
          "e2 LOUD: the double-counted arm census (one rung in "
          "BOTH arms) breaks the arm partition ward by EXACTLY "
          "%d (sum %d != %d, REFUSED) while the live census "
          "partitions exactly -- overlapping dichotomy arms "
          "cannot slip through"
          % (arm_break, mut_cnt[0] + mut_cnt[1],
             len(toy_letters)))
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    rb9 = mutant_orbit_posthoc(dict(trs=ev9m["trs"],
                                    m=ev9m["m"]))
    check("G82-e3-orbit-posthoc",
          len(e3_hits) >= 1 and (not sc_own) and rb9 >= 0.0,
          "e3 AST-CAUGHT: the 'orbit coordinate' consuming the "
          "q_max RECORD is FLAGGED (%s) while the five "
          "module-own edge builders are clean (%d hits) -- an "
          "orbit constructed after q_max sight is structurally "
          "refused (the mutant value %.3f is computed only to "
          "prove the mutant runs)"
          % (e3_hits[0] if e3_hits else "MISS", len(sc_own),
             rb9))
    mt9 = mutant_mass_from_target(ev9m)
    check("G83-e4-mass-from-target",
          len(e4_hits) >= 1 and mt9 >= 0.0,
          "e4 AST-CAUGHT: the 'edge-mass bound' derived from "
          "the cubic TARGET record is FLAGGED (%s) while "
          "edge_mass_state stays clean -- a mass bound read "
          "off the target quantity is structurally refused "
          "(mutant value %.3e computed only to prove it runs)"
          % (e4_hits[0] if e4_hits else "MISS", mt9))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed one-sided edge-orbit construction "
          "(reach = the masked support radius, direction-"
          "canonical), the margin mass/ancestor census, the two "
          "exact dichotomy arms q_max <= min(ng kappa/(|O_e| "
          "rmin_e), ng kappa S_marg/L1) with pointwise "
          "certification incl. the 12 adopted EXT3 anchors, and "
          "the named-spike arm coverage -- NO new certificate "
          "promoted, NO universal bound claimed beyond the "
          "measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R335_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r333 boundary "
                 "%d/65 + |Oin| %d/%d/%d + named %s + hgn "
                 "bit-near + d* %.3f + band %.4f/%.4f)"
                 % (rec3_w, C2r, viol2, n335, bnd_cnt,
                    int(np.median(oin_col)), min(oin_col),
                    max(oin_col), str(named_oin),
                    float(np.median(d_col)), rmin_w_in,
                    cband_w_in)]
        parts.append("SEAL(partition %.1e, ledger %.1e, band "
                     "rmin_e %.4f / cband_e %.4f, overlap %d, "
                     "arms %.1e/%.1e/%.1e, kappa min %.4f, "
                     "purity clean, toys exact)"
                     % (part_w, led_dev, band_worst_r,
                        band_worst_c, ovl_worst, qe_w, mb_w,
                        qd_w, kap_min))
        parts.append("EDGE_ORBIT(|Oe| med %.0f min %d max %d vs "
                     "|Oin| med %.0f, inner-empty %d -> gained "
                     "%d, arms O %d / M %d, named %s, EXT3 %d)"
                     % (float(np.median(oe_col)), min(oe_col),
                        max(oe_col), float(np.median(oinf_col)),
                        len(empty_in), len(gained),
                        sum(1 for c in arm_col if c == "O"),
                        sum(1 for c in arm_col if c == "M"),
                        str(named_tab), n_x3))
        parts.append("CERT(T1e %s minA %s; T2 b=0 exact; armO "
                     "minA %s; armM minA %s; dich %s minA %s; "
                     "delta %+.3f %s; e(BD1) %+.3f)"
                     % ("; ".join("a%d c0 %.3f v%d" %
                                  (a, t1e[a][0],
                                   len(t1e[a][1]))
                                  for a in A_FAM), str(aT1e),
                        str(aO), str(aM),
                        "; ".join("a%d CD %.3f v%d" %
                                  (a, min(certD[a][0], 9999.0),
                                   len(certD[a][1]))
                                  for a in A_FAM), str(aD),
                        e_hgn,
                        "DECIDED" if decided else "UNDECIDED",
                        e_BD1))
        parts.append(verdict_main)
        parts.append("COMPOSITION(%s)" % comp_txt)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the two arms, the band "
          "theorem, the partition/overlap algebra, the "
          "Fractions toys, the tree logic and the purity audits "
          "(exact / AST-decided); MEASURED: every census, "
          "constant, violation count and exponent (the finite "
          "class ladder + 12 EXT3 + 2 mains + 2 live controls); "
          "OPEN: any bound beyond the measured rungs, the "
          "cofinal law, kappa's behavior beyond the ladder; NO "
          "RH claim"
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
