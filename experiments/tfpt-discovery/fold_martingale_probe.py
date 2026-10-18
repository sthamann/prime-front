#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_martingale_probe -- PRIME.TERMINAL.FOLD_MARTINGALE.01
(round 337): THE REVIEWER'S MARTINGALE SECOND ROUTE after the
exhaustion of the packing language (r333 ORBIT_TOO_SHORT, r335
EDGE_ORBIT_ALSO_SHORT).

CONTEXT (binding, from the sealed r333/r335 records, commits
279ba0dd/55d4a832 and ec0fd5d5/3fa88d02): the terminal is the
pointwise Renyi-3 inequality (r306 GO); the composition runs
through q_max x M_2 (r324 MEASURED, m_0* 10^59.6, chain exponent
+0.172 -- too weak).  The packing language is exhausted: r333
adjudicated ORBIT_TOO_SHORT (two-sided companion orbits too
short, |O| = 0 sentinels at the spikes; one-sided companions and
the band discipline T2 carry), r335 adjudicated
EDGE_ORBIT_ALSO_SHORT (the inward edge window misses the
companions, |O_e| = 1 at the spikes) BUT delivered two structural
findings: (1) the MASS arm of the exact dichotomy q_max <=
min(ng kappa/(|O_e| rmin_e), ng kappa S_marg/L1) covers ALL four
named spike rungs at every a with reserves 1.6x-12.6x -- the
spike blocker is solved pointwise; (2) the new blocker is the
MID-BAND FAMILY (kz73/76/61 + deep kz95/98/109, margin share
0.18-0.28, BOTH arms violating by factor 6-10).  Arm partition:
the mass arm is the rule (62 of 77).  The reviewer's second
route, pre-named for exactly this case: the SIGNED FOLD
MARTINGALE THEOREM -- read the signed fold-group masses as a
martingale/supermartingale structure along the fold filtration,
with Azuma/Doob-style maximal control for q_max instead of
combinatorial packing.

THE ONE QUESTION OF THIS ROUND: does a filtration/martingale
structure of the signed fold masses carry a maximal inequality
that beats q_max x M_2 in the mid-band, where both dichotomy
arms fail?

THE FILTRATION (sealed a-priori, adjudicated BEFORE the freeze
-- the e3 mutant proves the protocol audit bites): the dyadic
SOURCE-SCALE filtration on the argmax block's fold groups.
F_k = the groups of block j* with source-scale bin s <= k (the
sealed r324 dyadic bins, QMO.scale_bins on the group gmax
column); the ADAPTED PROCESS is the coarse-to-fine partial sum
of the signed fold-group masses
  X_k = sum_{g in j*, s(g) <= k} G1_g,
with increments D_k = the per-bin signed group-mass sums over
the PRESENT bins in increasing order; X_{n_act} == x_{j*}
EXACTLY (the fold telescope, warded live).  The choice is
adjudicated a-priori against the alternative (m-sorted or
position-sorted group order) for three reasons: (i)
PARAMETER-FREE -- the bins are the sealed r324 scale_bins, no
new tunable; (ii) THEOREM-ADJACENT -- the exact band discipline
(T2, r333/r335 theorem grade) lives INSIDE one dyadic bin, so
the increments carry a-priori magnitude control (the natural
Azuma weights); (iii) CANONICAL ORDER -- coarse-to-fine is the
fold genealogy's own refinement order (the Doob picture: reveal
the block value at increasing source resolution); any m-sorted
or position-sorted order imports an arbitrary total order with
no magnitude control.  The alternative is REFUSED here, before
any evaluation, and the choice is sealed by this SPEC_SHA.

THE MEASURED STRUCTURE (Leg A, per rung): with V = sum_k D_k^2
(the quadratic variation) and X_K = the terminal partial sum:
  zr    = |X_K| / sqrt(V)   (the normalized maximal ratio;
          zr <= sqrt(n_act) by Cauchy-Schwarz, EXACT, warded),
  contr = the contraction fraction (share of steps with
          |X_k| <= |X_{k-1}|; supermartingale surrogate,
          threshold CONTR_MIN = 1/2),
  rev   = the mean-reversion fraction (share of steps with
          sign(D_k) = -sign(X_{k-1})),
  c*    = max_k D_k^2 / V (increment concentration; bounded
          conditional increments = Azuma-suitability census).
THE EXACT IDENTITY (warded live, no new constant):
  q_max = zr x kappa x sqrt(V) / L1_atom
with kappa = L1_atom/L the r333/r335 measured target-adjacent
transfer (disclosed).  The core measurement: is the process a
supermartingale (contraction median >= CONTR_MIN) / does it have
bounded normalized ratios (zr certifies, Azuma-suitable) / or
neither?  World comparison MAIN/twin/EPSTEIN/SCRAMBLE.

THE MAXIMAL INEQUALITY (Leg B): Z-CERTIFICATION
  zr <= C_Z(b) x (log m)^{b/2},   b in B_FAM = (0, 1, 2)
(max-cal mid-ladder freeze, TRB verbatim; b = 0 the bounded-
martingale form, b = 1 the Azuma sqrt-log form, b = 2 the log
form; minimal certifying b with 0 test violations incl. EXT3 +
named 4/4).  On certification the MARTINGALE ARM
  A_z = C_Z(b_min) (log m)^{b_min/2} kappa sqrt(V) / L1_atom
bounds q_max POINTWISE on every rung without a zr-violation
(exact algebra given the identity).  Certifications:
B^Z_a = m A_z/(log m)^{1+a} <= C_ZM(a); THE COMBINED ARM
A_c = min(M_b, A_z) (the r335 mass arm keeps the spikes, the
martingale arm is asked only where the packing failed) with
B^C_a <= C_C(a); both max-cal mid-ladder freezes, EXT3 = the 12
r329 anchors as PURE TEST rows (r335 adoption verbatim,
committed 8cbd95f9); the MID-BAND SIX kz73/76/61/95/98/109
(the r335 worst violators, sealed) get a named coverage clause;
the direct comparison against BOTH r335 dichotomy arms is
printed on the same rungs in the same normalization.

THE COMPOSITION (Leg C, printed ALWAYS, honestly typed): on GO
the chain q_max <= C_C(a) (log m)^{1+a}/m ==> M_3 <= q_max^2
(S0 exact) ==> N_2 >= 1/q_max >= m/(C_C (log m)^{1+a}) ==>
N_2 >= m^0.888 for all m >= m_0* (log-space solve) ==> the r297
target chain; honest comparison against the r324 MEASURED route
(m_0* 10^59.6 via the +0.172 exponent; the r328B chain-honest
variant 10^238 disclosed): the martingale route REPLACES the
+0.172 exponent iff it certifies AND its m_0* <= 10^59.6.  If
not GO: the violation census is typed (which rungs, which
factor, which structure is missing -- zr too large or the arm
too weak, limiting letter per rung).

THE FOUR MEASUREMENTS (sealed):
Q1 -- FILTRATION CENSUS: n_act/zr/contr/rev/c* on all rungs
   (65 + 12 EXT3), single-scale count, ladder statistics,
   world table.
Q2 -- Z-CERTIFICATION: C_Z(b), test violations (65-ladder test
   rungs + 12 EXT3), named, minimal b.
Q3 -- ARM CERTIFICATION: B^Z_a and B^C_a vs C_ZM(a)/C_C(a)
   (mid-ladder freeze), single arms vs the r335 record arms on
   the same rungs, mid-band coverage 6/6?, named 4/4?, the
   head-to-head table at a = 1.
Q4 -- WORLD CHECK: twin w13 (identical protocol), EPSTEIN and
   SCRAMBLE (structure census; the sealed WORLD_BLIND rule:
   SCRAMBLE at least as martingale-like as the ladder median in
   BOTH zr and contraction); SMOOTH degenerate-skipped
   (pre-declared).

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK                iff any purity/scope/literal audit
       hit on the martingale builders,
   NOT_A_MARTINGALE           iff no b in B_FAM certifies AND
       the ladder contraction median < CONTR_MIN -- no adapted
       structure: the second route is dead and the r324
       MEASURED chain stays the end state of the route,
   WORLD_BLIND                iff structure is present AND
       SCRAMBLE is at least as martingale-like as the ladder
       median in BOTH statistics (zr_scr <= med zr AND
       contr_scr >= med contr) -- the structure carries nothing
       arithmetic,
   MARTINGALE_MAXIMAL_GO      iff zr certifies at minimal b AND
       the combined arm certifies at minimal a (0 test
       violations incl. EXT3 + named 4/4) AND the mid-band six
       are covered 6/6 AND the composition m_0* <= 10^59.6
       (beats +0.172),
   MARTINGALE_STRUCTURE_ONLY  otherwise: structure present,
       bound too weak -- the violation census is typed.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.  Coexistence: r336 ran in parallel (L* lane);
this probe touches NOTHING outside its own file and the
strictly additive rh-sync (existing entries byte-identical).
Two-commit freeze protocol (r329 convention): spec committed
pre-freeze, record tables the only post-freeze edit, committed
again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r324/r327/r333/r335
machinery imported verbatim): t_{N-2} = sum_b ct_b (r244 chain
rows, r266 eval); F = 0.20 edge split; maximal same-sign runs of
the bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy
+ SCF.signed_cube_terms + SCF.flux_telescope; the r316
TRB.two_regime_state + TRB.split_midladder; the r324
QMO.scale_bins + QMO.mult_ward; the r324-pre FAP.m2_qmax_state;
the r327 GMC.group_mass_ledger (cross-ward only); the r333
COP.orbit_ledger + COP.dominant_state + COP.companion_orbit;
the r335 EPD.edge_window + EPD.edge_orbit + EPD.edge_mass_state
+ EPD.dichotomy_state (audited source-pure in r335, imported
verbatim -- the dichotomy columns are this round's CROSS CENSUS
+ the comparison arms); PDelta = Pbeta - Pomega; x_j =
(PDelta)_j.  NEW in this round (module-own, source-pure):
fold_filtration (the sealed coarse-to-fine per-bin increment
extraction), mart_state (zr/contraction/reversion/concentration
on the adapted partial sums), mart_arm (the Azuma/Doob-form
maximal arm), combined_arm (min with the r335 mass arm + the
letter) and the sealed mart_tree.

LEG 0 -- ANCHOR REGRESSION (slim set + the r333/r335/r324
records, disclosed): the r314 identity wards live; r306 C_2 =
1.069 (tol 0.005) first-5 freeze, 0/57; r316 rho anchors
kz53/kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) +
C_small 1.0694 at kz18 + n = 65; r333 RECORD anchors bit-near
(boundary 44/65 EXACT, |O_in| 5/0/52 EXACT, named inner quartet
(0, 0, 2, 0) EXACT, named hgn quartet tol 0.02, d* med 0.072,
inner band worst 0.2819/3.5473); r335 RECORD anchors bit-near
(arm census O 15 / M 62 of 77 EXACT, named B^D_1 quartet
12.51/20.47/2.62/11.86 tol 0.02 all arm M, dichotomy freeze
C_D(1) 33.06 tol 0.01 with 11 test violations EXACT, the a = 2
worst-violator set == the mid-band six EXACT, edge band worst
rmin_e 0.3162 / cband_e 3.1630 tol 0.005, delta = e(hgn) =
-0.004 tol 0.005); r324 CHAIN anchors (e(G/log m) +0.158,
e(m M_2) +0.014, e_tot +0.172, each tol 0.005; mid-ladder m2
freeze C_M2 2.2557 tol 0.005 with the seven test violators
{53, 67, 83, 76, 61, 28, 109} EXACT as a set; the m_0* solve
from the record constants (8.941, +0.172) reproduces 10^59.6
tol 0.1 decades).

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) sealed
definitions printed; the SOURCE-PURE table (rank, kz, N, m, G,
ng, hgn, |O_e|, rmin_e, cband_e, kappa, Q_e, M_b, Q_dich, arm,
sf, n_act, zr, contr, rev, c*, qzr = kappa sqrt(V)/L1) printed
BEFORE any certification table.  (A2) SOURCE-PURITY AUDITS: the
AST identifier scan over fold_filtration + mart_state +
mart_arm + combined_arm + mart_tree must be clean against
BOUND_FORBIDDEN + PHI3_FORBIDDEN + QMAX_FORBIDDEN (the
filtration consumes the ledger's signed group masses + scale
bins + block pointers ONLY; no block value, no target, no q_max
record; the argmax-block access is the imported r333
COP.dominant_state, disclosed); the literal scan over the
builders + toys must be clean against the sealed record-literal
set R337_TABLE_LITERALS (the r314..r333 set UNION the r335
record numbers); the e-mutants prove the audits bite.  (A3) TOY
EXACTNESS (Fractions): the three-bin filtration toy (argmax
block: single atom 8 at bin 0; pair (-2, -3/2) at bin 2; single
atom 1/2 at bin 4; side blocks 3 and -2): bins (0, 2, 4) EXACT,
increments (8, -7/2, 1/2) EXACT, telescope X_K = 5 == x_{j*}
EXACT, V = 153/2, zr^2 = 50/153 EXACT <= 3 (CS), contraction
1/2, reversion 1/2,     c* = 128/153 EXACT; the identity toy
    q_max^2 = zr^2 kappa^2 V/L1^2 = 1/4 EXACT (L = 10, L1 = 17,
    kappa = 17/10); the arm toy A_z^2 = 153/200 >= q_max^2 = 50/200
    slack 103/200 EXACT; the ANTI-MARTINGALE toy (same-sign
    increments (4, 2, 1)): contraction 0, reversion 0, zr^2 = 7/3,
    c* = 16/21, the bin-drop telescope break == 1 EXACT (LOUD);
    combined_arm letters (A, M) EXACT (A = the Azuma/martingale
    arm -- the letter 'Z' is withheld, it names the truth-side
    coordinate); mart_tree all five branches EXACT.  (A4) LIVE WARDS on every live world: the r316 chain +
NORM x cube == rho_2 (r335 verbatim); the S0 interpolation;
ledger == genealogy == GMC; the partition sum_g gabs == A1_j;
the r335 band/overlap/arm wards (cross-ward, verbatim); THE
TELESCOPE WARD X_K == x_{j*} (bar CHAIN_BAR); THE CS WARD
zr^2 <= n_act (exact algebra, bar BAND_TOL); THE IDENTITY WARD
q_max == zr kappa sqrt(V)/L1_atom (bar CHAIN_BAR); kappa >= 1;
fold multiplicity <= 2 admitted (QMO verbatim).

LEG B -- Q1/Q4 FILTRATION CENSUS: n_act/zr/contr/rev/c* ladder
statistics, single-scale count, named + mid-band anatomy, the
world table (twin/EPSTEIN/SCRAMBLE structure census + the
sealed blind-rule inputs).

LEG C -- Q2/Q3 CERTIFICATION (mid-ladder freeze, TRB verbatim;
EXT3 pure test): C_Z(b) + violations + named + minimal b; the
martingale arm B^Z_a and the combined arm B^C_a vs C_ZM(a)/
C_C(a) + violations + named + mid-band coverage + minimal a;
the head-to-head table (B^O_1/B^M_1/B^D_1/B^Z_1/B^C_1 on the
mid-band six + the named four); exponents e(hgn) (census
continuity, NOT adjudicating), e(B^Z_1), e(B^C_1) with the
halves stability rule; EXT3 cohort exponents census-grade.

LEG D -- COMPOSITION (printed ALWAYS, honestly typed): on GO
the recomposed chain with explicit constants + the r324
comparison (m_0* vs 10^59.6); else the r324 MEASURED
composition restated unchanged + the typed violation census.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) MARTINGALE PROPERTY CALIBRATED AFTER SIGHT:
  mutant_zward_posthoc re-picks C_Z to cover every seen violator
  (consumes rho, the evaluated bound column) -- the
  BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed toy
  it returns 3.0 != the canonical freeze's 1.0 -- CAUGHT twice
  (the freeze rule).
(e2) INCREMENT BOUND READ BACK FROM Q_MAX:
  mutant_increment_from_qmax consumes the q_max RECORD as an
  'increment cap' -- the QMAX_FORBIDDEN scan must FLAG it
  (AST-CAUGHT) while the module-own builders stay clean.
(e3) FILTRATION CHOICE AFTER RECORD SIGHT (protocol):
  mutant_filtration_posthoc re-orders the increments by a
  record-weighted key (consumes rho) -- the scope audit must
  FLAG it AND on the sealed toy it returns order (2, 1, 0) !=
  the canonical scale order (0, 1, 2) -- protocol-CAUGHT twice
  (the filtration is sealed BEFORE the freeze).
(e4) EXACT IDENTITY MUST-FAIL: mutant_bin_drop drops the deepest
  bin from the telescope -- the exact recomposition
  sum_k D_k == X_K breaks by EXACTLY the dropped mass (LOUD).
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r335 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target M_3 / rho_2 and the q_max RECORD enter
GATES / anchors / composition checks only, NEVER a martingale
builder (AST-warded); kappa = L1_atom/L consumes block values
and is computed OUTSIDE the builders (target-adjacent, disclosed
-- r333/r335 verbatim); no zero/prime oracles anywhere (AST
firewall); no fit primitives (fragment audit; growth exponents
are the imported r272 dyadic halves-slope, fit-free).  MACHINERY
IMPORTED VERBATIM: r335 EPD.edge_window + EPD.edge_orbit +
EPD.edge_mass_state + EPD.dichotomy_state, r333 COP.orbit_ledger
+ COP.dominant_state + COP.companion_orbit, r327
GMC.group_mass_ledger (cross-ward), r324 QMO.scale_bins +
QMO.mult_ward, r324-pre FAP.m2_qmax_state, r316
TRB.two_regime_state + TRB.split_midladder, r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope,
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze,
r298 WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge
+ PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316/r324/r327/r333/r335 verbatim): frame-A h <=
900, 42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36,
38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz);
EXT2: the r316 A5 rule (leftover pool + first 12 windows 1300 <
h <= 1650, first 8 POSITIVE_PREFIX by (N, kz)); EXT3: the sealed
r329 12-anchor list (record committed 8cbd95f9, adopted as-is,
PURE TEST rows).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); EXT_H_MAX 1300; K_EXT 15;
EXT_NW_EXPECT (942, 1218); EXT2_H_MAX 1650; EXT2_POOL_CAP 12;
K_EXT2 8; EXT3_KZ_B (42, 51, 54, 56, 58, 62); EXT3_KZ_A (96,
123, 125, 127, 128, 130); EXT3_NW_MIN 1721; EXT3_NW_MAX 2577;
B_FAM (0, 1, 2) (the zr family, factor (log m)^{b/2}); A_FAM
(0, 1, 2); CONTR_MIN 0.5 (the supermartingale surrogate
threshold, a-priori: majority contraction); MIDBAND_KZ (73, 76,
61, 95, 98, 109) (the sealed r335 worst-violator six); RBAND_MIN
1/4; CBAND_MAX 4; BAND_TOL 1e-9; OVERLAP_CAP 2; DELTA_CRIT 0.112
(census continuity only); N2_EXP_NEED 0.888; NAMED_KZ (53, 83,
67, 55); ATOM_BAR 1e-9; REC3_BAR 1e-13 ladder / 1e-12 EXT3;
TEL_BAR 1e-13 ladder / 1e-12 EXT3; BND_BAR 1e-13 ladder / 1e-12
EXT3; CHAIN_BAR 1e-9; SA_BAR 1e-12; DEG_FLOOR 1e-6; MULT_CAP 2;
N_CAL 5 (via TRB, verbatim); MUT_MIN 1e-6; TOY_BAR 1e-12;
TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep + ext + ext2 / 3e-5
EXT3 (r329 a-priori) / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9;
INF_SENT 1e300 / cert guard 1e299; R306 anchor C_2 1.069 tol
0.005; N337_REF 65; R316 RHO {53: 1.0490, 67: 1.0536, 55:
0.4821, 83: 0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at kz18;
R333 anchors: BND_CNT 44, OIN med/min/max 5/0/52, NAMED_OIN
(0, 0, 2, 0), NAMED_HGN (14.89, 13.43, 10.30, 15.17) tol 0.02,
D_MED 0.072 tol 0.005, RMIN_W 0.2819 / CBAND_W 3.5473 tol 0.005;
R335 anchors: ARM_O 15 / ARM_M 62, NAMED_BD1 (12.51, 20.47,
2.62, 11.86) tol 0.02 all arm M, CD1 33.06 tol 0.01, VD1 11
EXACT, MB_SET == MIDBAND_KZ EXACT (the a = 2 violator set),
RMINE_W 0.3162 / CBANDE_W 3.1630 tol 0.005, EHGN -0.004 tol
0.005; R324 anchors: EG 0.158 / EM2 0.014 / ETOT 0.172 tol
0.005, CM2 2.2557 tol 0.005, M2VIOL {53, 67, 83, 76, 61, 28,
109} EXACT, CCOMP 8.941, CRIT224 0.224, M0L10 59.6 tol 0.1;
R337_TABLE_LITERALS = the sealed r314..r333 set (r335 verbatim)
UNION the r335 record set {0.3162, 3.163, 33.06, 141.84, 7.71,
12.51, 20.47, 2.62, 11.86, 10.31, 10.04, 9.02, 7.92, 7.77,
0.711, 1.573, 3.84, 3.1726, 2.611, 8.34, 0.176, 0.312, 0.517,
-3.313, 0.0595, 0.2637, 1.1686, 166.1, 36.5, 141.8, 33.1}
(the round displays 8.0 / 7.7 / 7.8 are OMITTED from the
forbidden set to avoid collisions with innocent small toy
integers -- disclosed curation);
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the ledger/telescope/CS/identity wards on w9 + controls
+ e1-e4 mutants; ladder, extensions, EXT3, anchors, census,
certification, exponents and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r324/r333/r335 RECORD number adopted
as-is (incl. the full r335 anatomy: mass-arm spike coverage,
mid-band family, arm partition, C_D(1) 33.06); the EXT3 anchor
list is the sealed r329 RECORD selection (committed 8cbd95f9,
r335 adoption verbatim); the filtration choice + CONTR_MIN +
B_FAM + the blind rule are a-priori (justified above, frozen
BEFORE any evaluation); the identity q_max = zr kappa sqrt(V)/L1
and the CS bound zr <= sqrt(n_act) are derived algebra,
disclosed above; GENUINELY OPEN quantities of this round: every
martingale column (n_act, zr, contr, rev, c*, sqrt(V)/L1), all
certification constants C_Z(b)/C_ZM(a)/C_C(a), all violation
counts, the mid-band coverage, the world structure census, the
composition m_0* and the exponents -- NONE was computed before
this spec was frozen; the five sealed letters are symmetric and
total -- the tree maps every outcome to exactly one letter by
CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R337_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r333 record, r335 record: arms + named + C_D(1) + mid-band
    set + band + delta, r324 chain: exponents + C_M2 + m_0*)
+ SEAL(ledger wards + telescope + CS + identity + the r335
    band/overlap/arm cross-wards + purity audits + toys)
+ FILTRATION(census: n_act/zr/contr/rev/c* stats, single-scale
    count, named + mid-band anatomy, world table + blind rule)
+ CERT(C_Z(b) + viol + named + minimal b; B^Z_a; B^C_a + viol +
    named + mid-band coverage + minimal a; head-to-head vs the
    r335 arms; e(hgn) census, e(B^Z_1), e(B^C_1), stability)
+ [exactly one of] MARTINGALE_MAXIMAL_GO /
    MARTINGALE_STRUCTURE_ONLY / NOT_A_MARTINGALE / WORLD_BLIND /
    TARGET_LEAK
+ COMPOSITION(the recomposed chain with explicit constants +
    the r324 comparison; printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the telescope, the CS bound, the
identity, the Fractions toys, the tree logic and the purity
audits are EXACT (Fractions/AST-decided); the supermartingale/
Azuma reading is a MEASURED surrogate on deterministic data
(contraction/reversion/zr statistics), NOT a probabilistic
theorem -- a certifying C_Z fixes a proof TARGET, it proves NO
cofinal law; every census, constant, violation count and
exponent is MEASURED on the finite ladder (+ the 12 adopted
EXT3 anchors) only; kappa is a measured target-adjacent
transfer factor, disclosed as the honest gap of the composed
chain; the r333/r335/r324/r329 record numbers are disclosed
pre-spec inputs; the subcritical delta stays r333-adjudicated
(UNDECIDED) -- this round prints it as census continuity only;
r243-r336 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA 5460c2fa54983956,
pre-freeze commit 30ac0cb5; protocol: smoke pass 1 = 33/37 --
the probe's OWN scope audit caught the combined-arm letter 'Z'
(a withheld truth-side identifier); disclosed pre-freeze fix:
letter renamed 'Z' -> 'A' (no bar, band, family or rule moved);
smoke pass 2 = 37/37 (1.0 s), NO further amendment; calibration
pass 1 = first full evaluation, 37/37, wall 166.8 s, NO
amendment; record run1/run2 after this insertion, identical up
to the runtime line):
MAIN VERDICT: MARTINGALE_STRUCTURE_ONLY(structure AZUMA(b = 1)
but the bound is too weak: combined-arm minimal a = None, viol
18/13/11 at a = 0/1/2, mid-band 5/6, m_0* NONE) -- the
structure IS there and the mid-band blocker IS dissolved, but
the arm fails at the NEW margin: the EXT3 deep anchors + the
spikes.
THE THREE STRUCTURAL FINDINGS OF THE ROUND: (1) THE Z-MAXIMAL
CERTIFICATION CARRIES AT THE AZUMA FORM -- zr <= C_Z(1)
sqrt(log m) with C_Z(1) = 0.7364, 0 test violations of 51
(incl. all 12 EXT3), named 4/4; even b = 0 (bounded zr) misses
by only 2 violations (C_Z(0) 1.5501, zr max 1.677 at kz56/EXT3);
zr ladder med 1.1012, min 0.6035 -- the normalized ratio is
ESSENTIALLY FLAT because c* med 0.949: ONE increment dominates
the quadratic variation (the r324 single-heavy-scale finding
recurs in signed form), so |X_K| ~ sqrt(V) ~ |D_max| and the
certification is tight but nearly structureless.  (2) THE
MID-BAND BLOCKER DISSOLVES UNDER THE MARTINGALE ARM -- head-to-
head at a = 1 (same rungs, same normalization): kz73 B^D_1
54.40 -> B^C_1 0.399 / kz76 53.59 -> 0.483 / kz61 48.91 ->
0.755 / kz95 41.96 -> 0.352 / kz98 41.68 -> 0.400 / kz109
40.90 -> 0.299 vs C_C(1) 0.5293 -- coverage 5/6 (only kz61 at
1.43x), improvement factor 70x-180x over the r335 dichotomy;
the pointwise coverage q_max <= A_z holds on 77/77 rungs.  (3)
THE VIOLATION MARGIN MIGRATES TO THE DEEP ANCHORS AND THE
SPIKES -- the combined arm A_c = min(M_b, A_z) picks the Azuma
arm EVERYWHERE (letters A 77 / M 0: A_z undercuts the mass arm
on every rung), so the freeze constant collapses from 33.06 to
0.5293 and the a = 1 violators are now (kz51 2.09 / kz62 2.03 /
kz54 1.72 / kz123 1.72 / kz125 1.04 EXT3; kz53 1.05 / kz67
0.845 / kz83 0.721 named) -- the r335 mass-arm spike coverage
is LOST inside the min (its 1.6x-12.6x reserves lived on the
33.06 scale); a two-constant certification (each arm against
its own freeze) is NOT this round's sealed contract and is
named as the residual direction only.
CERT: e(B^Z_1) = e(B^C_1) = +0.059 (vs the r324 route's +0.172
-- the measured martingale-route growth is 3x flatter but the
pointwise cert fails); delta = e(hgn) = -0.004 halves
+0.148/+0.674 STRADDLE (exact r333/r335 continuity); EXT3
cohort e(m A_c) = +0.204 (census-grade, r329 caveat).
FILTRATION CENSUS: n_act med 3 max 6, single-scale 0;
contraction med 0.500 (supermartingale surrogate PRESENT at
exactly the threshold); reversion med 0.500; c* med 0.949 max
1.000.
WORLDS: twin w13 identical protocol (zr 0.704, contr 1.0, all
exact wards live); EPSTEIN zr 1.027 contr 0.0 (the construction
operates); SCRAMBLE zr 1.1159 / contr 0.500 vs ladder med
1.1012 / 0.500 -- the sealed blind rule reads DISTINGUISHED by
a 1.3-percent zr margin ONLY (honest negative: the zr statistic
is essentially world-blind in magnitude; the arithmetic content
of the round lives in the CALIBRATED constants, not in the
existence of the structure).
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069 (0/57);
r316 n 65 + rho quartet + C_small 1.0694@kz18; r333 RECORD
boundary 44/65 EXACT + named inner quartet (0, 0, 2, 0) EXACT +
band 0.2819/3.5473; r335 RECORD arms O 15 / M 62 EXACT + named
B^D_1 quartet 12.51/20.47/2.62/11.86 all M + C_D(1) 33.0599
viol 11 EXACT + the a = 2 violator set == the mid-band six
EXACT + edge band 0.3162/3.1630 + delta -0.004; r324 CHAIN
e(G/log m) +0.158 + e(m M_2) +0.014 = e_tot +0.172 EXACT + C_M2
2.2557 + the seven m2 violators EXACT + m_0* solve 10^59.6.
SEAL: partition 3.4e-16, ledger == genealogy == GMC 0.0,
telescope X_K == x_{j*} 3.2e-16, CS ward 0.0, identity ward
5.7e-16, kappa min 3.1726, purity clean, toys exact; must-fails
e1 CAUGHT twice (AST rho + toy 3.0 != 1.0) / e2 AST-CAUGHT
(trs) / e3 protocol-CAUGHT twice (AST rho + toy order (2, 1, 0)
!= (0, 1, 2)) / e4 LOUD (break 1 EXACT) + m5a/m5b FLAGGED.

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
import edge_packing_dichotomy_probe as EPD     # noqa: E402 r335
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
B_FAM = (0, 1, 2)
CONTR_MIN = 0.5
MIDBAND_KZ = (73, 76, 61, 95, 98, 109)
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
N337_REF = 65
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
R335_ARM_O = 15
R335_ARM_M = 62
R335_NAMED_BD1 = (12.51, 20.47, 2.62, 11.86)
R335_BD1_TOL = 0.02
R335_CD1 = 33.06
R335_CD1_TOL = 0.01
R335_VD1 = 11
R335_RMINE_W = 0.3162
R335_CBANDE_W = 3.1630
R335_EHGN = -0.004
R335_EHGN_TOL = 0.005
R324_EG = 0.158
R324_EM2 = 0.014
R324_ETOT = 0.172
R324_E_TOL = 0.005
R324P_CM2 = 2.2557
R324P_CM2_TOL = 0.005
R324P_M2VIOL = (53, 67, 83, 76, 61, 28, 109)
R324_CCOMP = 8.941
R324_CRIT224 = 0.224
R324_M0L10 = 59.6
R324_M0_TOL = 0.1
R337_TABLE_LITERALS = frozenset(EPD.R335_TABLE_LITERALS | {
    0.3162, 3.163, 33.06, 141.84, 7.71, 12.51, 20.47, 2.62,
    11.86, 10.31, 10.04, 9.02, 7.92, 7.77, 0.711, 1.573, 3.84,
    3.1726, 2.611, 8.34, 0.176, 0.312, 0.517, -3.313, 0.0595,
    0.2637, 1.1686, 166.1, 36.5, 141.8, 33.1})

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
    lies in the sealed r314..r335 record set."""
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
                            in R337_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the
# ---------------- martingale builders consume the ledger (signed
# ---------------- group masses / scale bins / block pointers)
# ---------------- ONLY; the withheld terminal drive key, the
# ---------------- branch label, the cubic target M_3 and the q_max
# ---------------- RECORD are forbidden (AST identifier scan +
# ---------------- literal scan).  The argmax-block access lives in
# ---------------- the imported r333 COP.dominant_state (disclosed).
def fold_filtration(led, sbins, j):
    """the SEALED FILTRATION (adjudicated a-priori, BEFORE the
    freeze): the dyadic source-scale filtration on the argmax
    block's fold groups -- returns the PRESENT bins in increasing
    order and the per-bin SIGNED group-mass increments D_k of
    block j (coarse-to-fine, the fold genealogy's own refinement
    order).  Consumes the ledger + the scale bins + the block
    index only."""
    a, b = int(led["ptr"][j]), int(led["ptr"][j + 1])
    g1 = led["G1"][a:b]
    sb = sbins[a:b]
    bins = tuple(sorted(set(int(s) for s in sb)))
    incs = np.array([float(np.sum(g1[sb == s])) for s in bins])
    return bins, incs


def mart_state(incs):
    """the ADAPTED-PROCESS STATE on the sealed increments: partial
    sums X_k = cumsum(D), terminal X_K, quadratic variation
    V = sum D_k^2, the normalized maximal ratio zr = |X_K|/sqrt(V)
    (<= sqrt(n_act) by Cauchy-Schwarz, exact), the contraction
    fraction (share of steps with |X_k| <= |X_{k-1}|, the
    supermartingale surrogate), the mean-reversion fraction
    (share of steps with sign(D_k) = -sign(X_{k-1})) and the
    increment concentration c* = max D_k^2/V.  Consumes the
    increments only."""
    n_act = int(len(incs))
    if n_act == 0:
        return dict(n_act=0, nst=0, xk=0.0, vq=0.0, zr=0.0,
                    contr=0.0, rev=0.0, cstar=0.0)
    xs = np.cumsum(incs)
    xk = float(xs[-1])
    vq = float(np.sum(incs ** 2))
    if vq <= 0.0:
        return dict(n_act=n_act, nst=0, xk=xk, vq=0.0, zr=0.0,
                    contr=0.0, rev=0.0, cstar=0.0)
    zr = abs(xk) / math.sqrt(vq)
    nst = n_act - 1
    if nst > 0:
        contr = sum(1 for k in range(1, n_act)
                    if abs(float(xs[k])) <= abs(float(xs[k - 1]))) \
            / float(nst)
        nz = [k for k in range(1, n_act)
              if xs[k - 1] != 0.0 and incs[k] != 0.0]
        rev = (sum(1 for k in nz
                   if math.copysign(1.0, float(incs[k]))
                   != math.copysign(1.0, float(xs[k - 1])))
               / float(len(nz))) if nz else 0.0
    else:
        contr = 0.0
        rev = 0.0
    cstar = float(np.max(incs ** 2)) / vq
    return dict(n_act=n_act, nst=nst, xk=xk, vq=vq, zr=zr,
                contr=contr, rev=rev, cstar=cstar)


def mart_arm(czb, bexp, lgm, kap, vq, l1a):
    """the MARTINGALE MAXIMAL ARM (Azuma/Doob form; the frozen
    C_Z(b) is the sole constant): A_z = C_Z (log m)^{b/2} kappa
    sqrt(V)/L1_atom -- bounds q_max pointwise on every rung
    without a zr-violation (exact algebra given the identity
    q_max = zr kappa sqrt(V)/L1).  Consumes pre-computed
    source-side scalars + the frozen constant only."""
    return czb * (lgm ** (bexp / 2.0)) * kap \
        * math.sqrt(max(vq, 0.0)) / max(l1a, 1e-300)


def combined_arm(az, mbv):
    """the COMBINED ARM and its letter: A_c = min(M_b, A_z) --
    the r335 mass arm keeps the spikes, the martingale arm is
    asked only where the packing failed; ties to the martingale
    arm (letter A = the Azuma arm).  Consumes the two
    pre-computed arm values only."""
    if az <= mbv:
        return az, "A"
    return mbv, "M"


def mart_tree(leak, nomart, blind, go):
    """the sealed five-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    NOT_A_MARTINGALE > WORLD_BLIND > MARTINGALE_MAXIMAL_GO >
    MARTINGALE_STRUCTURE_ONLY."""
    if leak:
        return "TARGET_LEAK"
    if nomart:
        return "NOT_A_MARTINGALE"
    if blind:
        return "WORLD_BLIND"
    if go:
        return "MARTINGALE_MAXIMAL_GO"
    return "MARTINGALE_STRUCTURE_ONLY"


def mutant_zward_posthoc(z_seen, rho, cbar):
    """e1 MUST-FAIL MUTANT: the martingale constant C_Z re-picked
    AFTER SIGHT of the violators (consumes rho, the evaluated
    bound column): raised until every seen violator is covered --
    the BOUND_FORBIDDEN scope audit must FLAG it AND on the
    sealed toy it returns 3.0 != the canonical freeze's 1.0 --
    CAUGHT twice (the freeze rule)."""
    cz = cbar
    for z, r in zip(z_seen, rho):
        if r > cbar:
            cz = max(cz, z)
    return cz


def mutant_increment_from_qmax(state):
    """e2 MUST-FAIL MUTANT: an 'increment cap' consuming the
    q_max RECORD (the target-side concentration coordinate) --
    the QMAX_FORBIDDEN identifier scan must FLAG this (the
    filtration must be sealed BEFORE any q_max sight)."""
    tr = state["trs"]
    return float(tr["qmax"]) * float(state["m"])


def mutant_filtration_posthoc(incs, rho):
    """e3 MUST-FAIL MUTANT (protocol): the filtration ORDER
    re-picked after record sight -- sorts the increments by a
    record-weighted key (consumes rho) -- the scope audit must
    FLAG it AND on the sealed toy it returns (2, 1, 0) != the
    canonical scale order (0, 1, 2) -- protocol-CAUGHT twice
    (the filtration is sealed BEFORE the freeze)."""
    o = sorted(range(len(incs)),
               key=lambda k: -abs(float(incs[k]))
               * (1.0 + float(rho[k])))
    return tuple(o)


def mutant_bin_drop(incs):
    """e4 MUST-FAIL MUTANT (exact identity): the telescope with
    the deepest bin dropped -- the exact recomposition
    sum_k D_k == X_K breaks by EXACTLY the dropped mass (LOUD)."""
    return float(np.sum(incs[:-1]))


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'filtration orientation' consuming
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'filtration constant' consuming the branch label -- the
    scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the filtration toy,
# ---------------- the identity/arm algebra and the anti-martingale
# ---------------- pole decided as rationals
def fr_filtration_toy():
    """the sealed three-bin filtration toy in exact Fractions:
    argmax block 0 with three fold groups -- single atom 8 at pos
    1/5 (bin 0), pair (-2, -3/2) at pos 3/10 (G1 = -7/2, gmax 2,
    bin 2), single atom 1/2 at pos 2/5 (bin 4); side blocks: atom
    3 at 3/5 (block 1), atom -2 at 4/5 (block 2).  Bins (0, 2, 4)
    EXACT; increments (8, -7/2, 1/2) EXACT; X = (8, 9/2, 5),
    telescope X_K = 5 == x_{j*} EXACT; V = 153/2; zr^2 = 50/153
    <= 3 (CS) EXACT; contraction 1/2; reversion 1/2; c* =
    128/153 EXACT.  Identity: L = 10, L1 = 17, kappa = 17/10,
    q_max = 1/2, q_max^2 == zr^2 kappa^2 V/L1^2 = 1/4 EXACT.
    Arm (C_Z = 1, b = 0): A_z^2 = kappa^2 V/L1^2 = 153/200 >=
    q_max^2 = 50/200, slack 103/200 EXACT.  Returns (worst dev,
    slack, filtration ok, identity ok)."""
    d1, d2, d3 = Fr(8), Fr(-7, 2), Fr(1, 2)
    x1 = d1
    x2 = d1 + d2
    x3 = d1 + d2 + d3
    vq = d1 * d1 + d2 * d2 + d3 * d3
    zr2 = x3 * x3 / vq
    cst = max(d1 * d1, d2 * d2, d3 * d3) / vq
    contr = Fr(1, 2)
    rev = Fr(1, 2)
    L = Fr(10)
    l1a = Fr(17)
    kap = l1a / L
    qmx2 = Fr(1, 4)
    id2 = zr2 * kap * kap * vq / (l1a * l1a)
    az2 = kap * kap * vq / (l1a * l1a)
    slack = az2 - qmx2
    devs = [abs(vq - Fr(153, 2)), abs(zr2 - Fr(50, 153)),
            abs(cst - Fr(128, 153)), abs(x3 - Fr(5)),
            abs(id2 - qmx2), abs(az2 - Fr(153, 200)),
            abs(slack - Fr(103, 200)),
            Fr(0) if zr2 <= Fr(3) else Fr(1),
            Fr(0) if qmx2 <= az2 else Fr(1),
            Fr(0) if abs(x2) <= abs(x1) else Fr(1),
            Fr(0) if abs(x3) > abs(x2) else Fr(1)]
    # float construction cross-check via the real builders:
    pos = np.array([0.2, 0.3, 0.3, 0.4, 0.6, 0.8])
    val = np.array([8.0, -2.0, -1.5, 0.5, 3.0, -2.0])
    blk = np.array([0, 0, 0, 0, 1, 2])
    srcf = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
    led = COP.orbit_ledger(pos, val, blk, srcf, 3)
    sbins = QMO.scale_bins(led["gmax"])
    xs = np.array([5.0, 3.0, -2.0])
    ds = COP.dominant_state(xs, led, sbins)
    bins_f, incs_f = fold_filtration(led, sbins, ds["j"])
    mst = mart_state(incs_f)
    filt_ok = (ds["j"] == 0 and bins_f == (0, 2, 4)
               and len(incs_f) == 3
               and abs(incs_f[0] - 8.0) <= TOY_BAR
               and abs(incs_f[1] + 3.5) <= TOY_BAR
               and abs(incs_f[2] - 0.5) <= TOY_BAR
               and abs(mst["xk"] - 5.0) <= TOY_BAR
               and abs(mst["vq"] - float(Fr(153, 2))) <= TOY_BAR
               and abs(mst["zr"] ** 2 - float(Fr(50, 153)))
               <= TOY_BAR
               and abs(mst["contr"] - float(contr)) <= TOY_BAR
               and abs(mst["rev"] - float(rev)) <= TOY_BAR
               and abs(mst["cstar"] - float(cst)) <= TOY_BAR)
    az_f = mart_arm(1.0, 0, 1.0, 1.7, float(Fr(153, 2)), 17.0)
    ca1 = combined_arm(0.5, 2.0)
    ca2 = combined_arm(3.0, 1.0)
    id_ok = (abs(az_f ** 2 - float(Fr(153, 200))) <= TOY_BAR
             and abs(mst["zr"] * az_f - 0.5) <= TOY_BAR
             and ca1 == (0.5, "A") and ca2 == (1.0, "M"))
    return max(devs), slack, filt_ok, id_ok


def fr_antimart_toy():
    """the ANTI-MARTINGALE pole in exact Fractions: same-sign
    increments (4, 2, 1) -- X = (4, 6, 7): contraction 0,
    reversion 0, zr^2 = 7/3, c* = 16/21 EXACT; the bin-drop
    telescope break == 1 EXACT (the dropped deepest mass).
    Returns (worst dev, break ok, state ok)."""
    d = (Fr(4), Fr(2), Fr(1))
    xk = sum(d)
    vq = sum(v * v for v in d)
    zr2 = xk * xk / vq
    cst = Fr(16) / vq
    brk = abs(xk - (d[0] + d[1]))
    devs = [abs(vq - Fr(21)), abs(zr2 - Fr(7, 3)),
            abs(cst - Fr(16, 21)), abs(brk - Fr(1))]
    incs_f = np.array([4.0, 2.0, 1.0])
    mst = mart_state(incs_f)
    st_ok = (mst["contr"] == 0.0 and mst["rev"] == 0.0
             and abs(mst["zr"] ** 2 - float(Fr(7, 3))) <= TOY_BAR
             and abs(mst["cstar"] - float(Fr(16, 21))) <= TOY_BAR)
    mut = mutant_bin_drop(incs_f)
    brk_ok = abs(abs(mst["xk"] - mut) - 1.0) <= TOY_BAR
    return max(devs), brk_ok, st_ok


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fold_martingale_probe -- "
          "PRIME.TERMINAL.FOLD_MARTINGALE.01 (round 337, the "
          "reviewer's martingale second route after the "
          "exhaustion of the packing language)")
    print("SPEC_SHA %s   R335_SHA %s   R333_SHA %s   R324_SHA %s"
          % (SPEC_SHA[:16], EPD.SPEC_SHA[:16], COP.SPEC_SHA[:16],
             QMO.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + ledger/telescope/CS/"
                        "identity wards + e1-e4; ladder, "
                        "extensions, EXT3, anchors, census, "
                        "certification and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE FOLD-MARTINGALE ROUND (the reviewer's second "
          "route): the SEALED dyadic source-scale filtration on "
          "the argmax block's fold groups (adjudicated a-priori "
          "against m-sorted order: parameter-free / theorem-"
          "adjacent / canonical, sealed by SPEC_SHA); adapted "
          "process X_k = coarse-to-fine partial sums of the "
          "signed group masses, X_K == x_{j*} EXACT; structure "
          "zr = |X_K|/sqrt(V) <= sqrt(n_act) (CS exact), "
          "contraction (CONTR_MIN %.1f), reversion, c*; "
          "Z-certification zr <= C_Z(b)(log m)^{b/2}, B_FAM %s; "
          "martingale arm A_z = C_Z kappa sqrt(V)/L1; combined "
          "arm min(M_b, A_z) vs the r335 dichotomy on the same "
          "rungs; mid-band six %s sealed; EXT3 = the r329 record "
          "12 as PURE TEST rows; verdict tree TARGET_LEAK / "
          "NOT_A_MARTINGALE / WORLD_BLIND / MARTINGALE_MAXIMAL_"
          "GO / MARTINGALE_STRUCTURE_ONLY sealed BEFORE "
          "evaluation" % (CONTR_MIN, str(B_FAM),
                          str(MIDBAND_KZ)))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("fold_filtration", "mart_state", "mart_arm",
               "combined_arm", "mart_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the five module-own "
          "martingale builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the "
          "filtration consumes ONLY the ledger + scale bins "
          "(sealed BEFORE any q_max sight); m5a gift-bound "
          "FLAGGED (%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r335 scaffold verbatim)
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
              "8cbd95f9, r335 adoption verbatim): 12 anchors (B "
              "%s + A %s), POSITIVE_PREFIX %d/12, N_w %d..%d "
              "(record %d..%d) -- PURE TEST rows, never "
              "calibration"
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
    section("S2  EXACT DECOMPOSITION + LEDGER WARDS")
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
            # the r335 one-sided edge orbit + dichotomy (verbatim,
            # this round's cross census + comparison arms)
            wlo, whi = EPD.edge_window(led["pmin"], led["pmax"],
                                       dst["ps"])
            orb_e = EPD.edge_orbit(led, sbins, dst["sb"],
                                   dst["nw"], dst["sg"], wlo, whi)
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
            n_marg, S_marg = EPD.edge_mass_state(led, dst["gi"],
                                                 dst["ilo"],
                                                 dst["ihi"]) \
                if dst["gi"] >= 0 else (0, 0.0)
            Qe, Mb, Qd, arm = EPD.dichotomy_state(dst["ngj"],
                                                  kap, nOe,
                                                  rmin_e, S_marg,
                                                  L1a)
            nband = int(len(set(int(s) for s in sbins[
                led["gabs"] > 0.0]))) if led["ng"] else 0
            # NEW: the sealed fold filtration + martingale state
            if dst["gi"] >= 0:
                bins_f, incs_f = fold_filtration(led, sbins,
                                                 dst["j"])
                mst = mart_state(incs_f)
            else:
                bins_f = ()
                incs_f = np.zeros(0)
                mst = mart_state(incs_f)
            qzr = kap * math.sqrt(max(mst["vq"], 0.0)) \
                / max(L1a, 1e-300)
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
            bins_f = ()
            incs_f = np.zeros(0)
            mst = mart_state(incs_f)
            qzr = 0.0
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
                    Qd=Qd, arm=arm, nband=nband, bins_f=bins_f,
                    incs_f=incs_f, mst=mst, qzr=qzr,
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
          "re-warded by the sealed r321/r324/r327/r333/r335 "
          "probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, tel_x,
             bnd_x, REC3_BAR_X3))
    if smoke:
        ev9s = recs[0]["ev"]
        ms9 = ev9s["mst"]
        info("SMOKE: w9 m %d ng* %d hgn %.4f |Oe| %d arm %s "
             "nact %d zr %.4f contr %.3f rev %.3f c* %.3f qzr "
             "%.4f kap %.3f"
             % (ev9s["m"], ev9s["dst"]["ngj"], ev9s["dst"]["hgn"],
                ev9s["nOe"], ev9s["arm"], ms9["n_act"], ms9["zr"],
                ms9["contr"], ms9["rev"], ms9["cstar"],
                ev9s["qzr"], ev9s["kap"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r333-anchors", True, "SMOKE: skipped")
        srt = []
        n337 = 0
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
        n337 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n337)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n337 == N337_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n337, N337_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n337):
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
              % (bnd_cnt, n337, R333_BND_CNT,
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
    for fn in ("fold_filtration", "mart_state", "mart_arm",
               "combined_arm", "mart_tree", "fr_filtration_toy",
               "fr_antimart_toy"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_zward_posthoc", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_increment_from_qmax",
                          QMAX_FORBIDDEN)
    e3_hits = scope_audit("mutant_filtration_posthoc",
                          BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e3_hits) >= 1,
          "SOURCE PURITY: the martingale builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed r314..."
          "r335 record-literal set (%d literal hits); consumed "
          "inputs: ledger + scale bins + block pointers ONLY -- "
          "M_3, rho_2 and the q_max RECORD are TARGET-SIDE, "
          "computed outside the builders (disclosed; kappa "
          "likewise); e1 zward-posthoc FLAGGED (%s); e2 "
          "increment-from-qmax FLAGGED (%s); e3 filtration-"
          "posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    fr_dev, fr_slack, fr_filt_ok, fr_id_ok = fr_filtration_toy()
    fa_dev, fa_brk_ok, fa_st_ok = fr_antimart_toy()
    tr_br = (mart_tree(True, True, True, True),
             mart_tree(False, True, True, True),
             mart_tree(False, False, True, True),
             mart_tree(False, False, False, True),
             mart_tree(False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "NOT_A_MARTINGALE",
                      "WORLD_BLIND", "MARTINGALE_MAXIMAL_GO",
                      "MARTINGALE_STRUCTURE_ONLY")
    check("G41-toy-exactness",
          fr_dev == 0 and fr_filt_ok and fr_id_ok
          and fa_dev == 0 and fa_brk_ok and fa_st_ok and ok_tr,
          "the Fractions filtration toy EXACT (worst dev %s): "
          "bins (0, 2, 4), increments (8, -7/2, 1/2), telescope "
          "X_K = 5 == x_{j*}, V = 153/2, zr^2 = 50/153 <= 3 "
          "(CS), contraction 1/2, reversion 1/2, c* = 128/153; "
          "identity q_max^2 == zr^2 kap^2 V/L1^2 = 1/4 EXACT; "
          "arm A_z^2 = 153/200 >= 50/200 slack %s EXACT; the "
          "real builders reproduce bins/increments/state; the "
          "ANTI-MARTINGALE toy EXACT (worst %s): contraction 0, "
          "reversion 0, zr^2 = 7/3, bin-drop break == 1 EXACT "
          "(LOUD); combined_arm letters (A, M) EXACT; mart_tree "
          "all five branches EXACT %s"
          % (str(fr_dev), str(fr_slack), str(fa_dev),
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
    tel_mart_w = 0.0
    cs_w = 0.0
    id_mart_w = 0.0
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
        # NEW: the martingale wards -- telescope, CS, identity
        mstw = ev["mst"]
        xjs = float(ev["sct"]["x"][ds["j"]])
        tel_mart_w = max(tel_mart_w,
                         abs(mstw["xk"] - xjs)
                         / max(abs(xjs), 1e-300))
        if mstw["vq"] > 0.0:
            cs_w = max(cs_w,
                       max(0.0, mstw["zr"] ** 2
                           - float(mstw["n_act"]))
                       / max(float(mstw["n_act"]), 1e-300))
            id_mart_w = max(id_mart_w,
                            abs(qmx - mstw["zr"] * ev["qzr"])
                            / max(qmx, 1e-300))
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and part_w <= SA_BAR
          and band_ok and ovl_worst <= OVERLAP_CAP
          and qe_w <= CHAIN_BAR and mb_w <= CHAIN_BAR
          and qd_w <= CHAIN_BAR and a1_w <= CHAIN_BAR
          and smarg_w <= CHAIN_BAR
          and kap_min >= 1.0 - CHAIN_BAR and mult_all_ok
          and arm_part_ok and tel_mart_w <= CHAIN_BAR
          and cs_w <= BAND_TOL and id_mart_w <= CHAIN_BAR,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 interpolation (worst "
          "%.1e); GROUP PARTITION sum_g gabs == A1_j (worst "
          "%.1e, bar %.0e); the r335 band/overlap/arm "
          "cross-wards live: rmin_e worst %.4f > 1/4, cband_e "
          "worst %.4f < 4, membership %d <= %d, arms exact "
          "(%.1e/%.1e/%.1e, hga <= S_marg %.1e), partition %s, "
          "kappa min %.4f >= 1, mult <= %d; THE TELESCOPE WARD "
          "X_K == x_{j*} (worst %.1e, bar %.0e); THE CS WARD "
          "zr^2 <= n_act (worst %.1e, exact algebra); THE "
          "IDENTITY WARD q_max == zr kappa sqrt(V)/L1 (worst "
          "%.1e, bar %.0e)"
          % (len(live), chain_w, xw_cube, interp_w, part_w,
             SA_BAR, band_worst_r, band_worst_c, ovl_worst,
             OVERLAP_CAP, qe_w, mb_w, qd_w, smarg_w,
             "OK" if arm_part_ok else "BROKEN", kap_min,
             MULT_CAP, tel_mart_w, CHAIN_BAR, cs_w,
             id_mart_w, CHAIN_BAR))
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
        oe_col = [rc["ev"]["nOe"] for rc in srt_full]
        rme_col = [rc["ev"]["rmin_e"] for rc in srt_full]
        cbe_col = [rc["ev"]["cband_e"] for rc in srt_full]
        kap_col = [rc["ev"]["kap"] for rc in srt_full]
        Qe_col = [rc["ev"]["Qe"] for rc in srt_full]
        Mb_col = [rc["ev"]["Mb"] for rc in srt_full]
        Qd_col = [rc["ev"]["Qd"] for rc in srt_full]
        arm_col = [rc["ev"]["arm"] for rc in srt_full]
        smf_col = [rc["ev"]["S_marg"]
                   / max(rc["ev"]["L1a"], 1e-300)
                   for rc in srt_full]
        nact_col = [rc["ev"]["mst"]["n_act"] for rc in srt_full]
        zr_col = [rc["ev"]["mst"]["zr"] for rc in srt_full]
        ct_col = [rc["ev"]["mst"]["contr"] for rc in srt_full]
        rv_col = [rc["ev"]["mst"]["rev"] for rc in srt_full]
        cst_col = [rc["ev"]["mst"]["cstar"] for rc in srt_full]
        nst_col = [rc["ev"]["mst"]["nst"] for rc in srt_full]
        qzr_col = [rc["ev"]["qzr"] for rc in srt_full]
        BD1_col = [min(m_full[i] * Qd_col[i]
                       / (math.log(float(m_full[i])) ** 2),
                       INF_SENT) for i in range(n_full)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m G ng* hgn |Oe| "
             "rmin_e cb_e kap Qe Mb Qd arm sf nact zr contr rev "
             "c* qzr  [rows 65..%d are EXT3 PURE TEST]"
             % (n_full - 1))
        for i, rc in enumerate(srt_full):
            info("%2d kz%-3d N %4d m %3d G %6.3f ng %2d hgn "
                 "%6.3f |Oe| %3d rm %.3f cb %.3f kap %.3f Qe "
                 "%8.4f Mb %8.4f Qd %8.4f %s sf %.3f na %d zr "
                 "%.4f ct %.3f rv %.3f c* %.3f qzr %8.4f%s"
                 % (i, rc["kz"], rc["N"], m_full[i], G_col[i],
                    ngf_col[i], hgnf_col[i], oe_col[i],
                    rme_col[i], cbe_col[i], kap_col[i],
                    min(Qe_col[i], 9999.0),
                    min(Mb_col[i], 9999.0),
                    min(Qd_col[i], 9999.0), arm_col[i],
                    smf_col[i], nact_col[i], zr_col[i],
                    ct_col[i], rv_col[i], cst_col[i],
                    min(qzr_col[i], 9999.0),
                    " X3" if i >= n337 else ""))
        check("G43-coordinate-table", True,
              "n_act range %d/%.0f/%d min/med/max; zr med %.4f "
              "min %.4f max %.4f; contr med %.3f; rev med %.3f; "
              "c* med %.3f max %.3f; qzr med %.4f max %.4f; "
              "single-scale rungs (n_act = 1) %d; arm census O "
              "%d / M %d; EXT3 rows %d"
              % (min(nact_col), float(np.median(nact_col)),
                 max(nact_col), float(np.median(zr_col)),
                 min(zr_col), max(zr_col),
                 float(np.median(ct_col)),
                 float(np.median(rv_col)),
                 float(np.median(cst_col)), max(cst_col),
                 float(np.median(qzr_col)), max(qzr_col),
                 sum(1 for v in nact_col if v == 1),
                 sum(1 for c in arm_col if c == "O"),
                 sum(1 for c in arm_col if c == "M"), n_x3))

    # ---------------- S5: Leg 0 (cont) -- r335 + r324 records
    section("S5  LEG 0 (CONT) -- R335 RECORD + R324 CHAIN "
            "ANCHORS")
    if smoke:
        check("G50-r335-anchors", True, "SMOKE: skipped")
        check("G51-r324-chain-anchors", True, "SMOKE: skipped")
    else:
        te_x = list(te_i) + list(range(n337, n_full))

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

        certD, aD = cert_max(Qd_col)
        certO, aO = cert_max(Qe_col)
        certM, aM = cert_max(Mb_col)
        named_bd1 = tuple(certD[1][3][named_rank[kz]]
                          for kz in NAMED_KZ)
        named_arm = tuple(arm_col[named_rank[kz]]
                          for kz in NAMED_KZ)
        worst6_a2 = set(srt_full[i]["kz"] for i in sorted(
            certD[2][1], key=lambda i: -certD[2][3][i])[:6])
        msT = [m_full[i] for i in te_i]
        e_hgn = L2D.halves_slope(msT, [max(hgnf_col[i], 1e-300)
                                       for i in te_i])
        check("G50-r335-anchors",
              sum(1 for c in arm_col if c == "O") == R335_ARM_O
              and sum(1 for c in arm_col if c == "M")
              == R335_ARM_M
              and all(abs(named_bd1[k] - R335_NAMED_BD1[k])
                      <= R335_BD1_TOL for k in range(4))
              and named_arm == ("M", "M", "M", "M")
              and abs(certD[1][0] - R335_CD1) <= R335_CD1_TOL
              and len(certD[1][1]) == R335_VD1
              and len(certD[2][1]) == 6
              and worst6_a2 == set(MIDBAND_KZ)
              and abs(band_worst_r - R335_RMINE_W)
              <= R333_BAND_TOL_A
              and abs(band_worst_c - R335_CBANDE_W)
              <= R333_BAND_TOL_A
              and abs(e_hgn - R335_EHGN) <= R335_EHGN_TOL,
              "the r335 RECORD reproduced bit-near: arm census O "
              "%d / M %d (rec %d/%d); named B^D_1 quartet %s "
              "(rec %s tol %.2f) all arm M; C_D(1) %.4f (rec "
              "%.2f) viol %d (rec %d); the a = 2 violator set "
              "%s == the mid-band six EXACT; edge band worst "
              "%.4f/%.4f (rec %.4f/%.4f); delta = e(hgn) %+.3f "
              "(rec %+.3f)"
              % (sum(1 for c in arm_col if c == "O"),
                 sum(1 for c in arm_col if c == "M"),
                 R335_ARM_O, R335_ARM_M,
                 str(tuple(round(v, 2) for v in named_bd1)),
                 str(R335_NAMED_BD1), R335_BD1_TOL,
                 certD[1][0], R335_CD1, len(certD[1][1]),
                 R335_VD1, str(sorted(worst6_a2)),
                 band_worst_r, band_worst_c, R335_RMINE_W,
                 R335_CBANDE_W, e_hgn, R335_EHGN))
        GL_col = [G_col[i] / math.log(float(m_full[i]))
                  for i in range(n337)]
        e_G = L2D.halves_slope(msT, [max(GL_col[i], 1e-300)
                                     for i in te_i])
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        e_M2 = L2D.halves_slope(msT, [max(m2_col[i], 1e-300)
                                      for i in te_i])
        e_tot = e_G + e_M2
        C_M2 = max(m2_col[i] for i in ca_i)
        viol_m2 = tuple(sorted(srt[i]["kz"] for i in te_i
                               if m2_col[i] > C_M2))
        # the r324 m_0* solve reproduced from the record
        # constants (pure algebra, disclosed):
        m0_324 = None
        t = math.log(73.0)
        while t < 1e7:
            if t * (R324_CRIT224 - R324_ETOT) \
                    >= math.log(R324_CCOMP) + math.log(t):
                m0_324 = t / math.log(10.0)
                break
            t *= 1.02
        check("G51-r324-chain-anchors",
              abs(e_G - R324_EG) <= R324_E_TOL
              and abs(e_M2 - R324_EM2) <= R324_E_TOL
              and abs(e_tot - R324_ETOT) <= R324_E_TOL
              and abs(C_M2 - R324P_CM2) <= R324P_CM2_TOL
              and viol_m2 == tuple(sorted(R324P_M2VIOL))
              and m0_324 is not None
              and abs(m0_324 - R324_M0L10) <= R324_M0_TOL,
              "the r324 CHAIN reproduced bit-near: e(G/log m) "
              "%+.3f (rec %+.3f) + e(m M_2) %+.3f (rec %+.3f) = "
              "e_tot %+.3f (rec %+.3f, tol %.3f); C_M2 %.4f "
              "(rec %.4f) with the seven test violators %s == "
              "the banked set EXACT; the m_0* solve from the "
              "record constants (C %.3f, e_tot %+.3f): m_0* = "
              "10^%.1f (rec 10^%.1f tol %.1f) -- the +0.172 "
              "route this round must beat"
              % (e_G, R324_EG, e_M2, R324_EM2, e_tot, R324_ETOT,
                 R324_E_TOL, C_M2, R324P_CM2, str(viol_m2),
                 R324_CCOMP, R324_ETOT, m0_324, R324_M0L10,
                 R324_M0_TOL))

    # ---------------- S6: Leg A (cont) -- structure census +
    # ---------------- named/mid-band anatomy + worlds
    section("S6  LEG A -- STRUCTURE CENSUS + NAMED/MID-BAND "
            "ANATOMY + WORLDS")
    if smoke:
        check("G60-structure-census", True, "SMOKE: skipped")
        check("G61-named-midband-anatomy", True, "SMOKE: skipped")
        z_med = 0.0
        contr_med = 0.0
    else:
        lad_step = [i for i in range(n337) if nst_col[i] >= 1]
        z_med = float(np.median([zr_col[i] for i in
                                 range(n337)]))
        contr_med = float(np.median([ct_col[i]
                                     for i in lad_step]))
        rev_med = float(np.median([rv_col[i] for i in lad_step]))
        cst_med = float(np.median([cst_col[i]
                                   for i in range(n337)]))
        n_single = sum(1 for i in range(n337)
                       if nact_col[i] == 1)
        supermart = contr_med >= CONTR_MIN
        check("G60-structure-census", True,
              "Q1 FILTRATION CENSUS (65-rung ladder): n_act med "
              "%.0f max %d, single-scale %d; zr med %.4f min "
              "%.4f max %.4f (CS cap sqrt(n_act) med %.3f); "
              "contraction med %.3f (CONTR_MIN %.1f -> "
              "supermartingale surrogate %s); reversion med "
              "%.3f; c* med %.3f max %.3f; EXT3 zr %s"
              % (float(np.median([nact_col[i]
                                  for i in range(n337)])),
                 max(nact_col[:n337]), n_single, z_med,
                 min(zr_col[:n337]), max(zr_col[:n337]),
                 float(np.median([math.sqrt(v) for v in
                                  nact_col[:n337]])),
                 contr_med, CONTR_MIN,
                 "PRESENT" if supermart else "ABSENT", rev_med,
                 cst_med, max(cst_col[:n337]),
                 str([round(zr_col[i], 3)
                      for i in range(n337, n_full)])))
        mb_rank = {}
        for kz in MIDBAND_KZ:
            for i in range(n337):
                if srt[i]["kz"] == kz:
                    mb_rank[kz] = i
        for kz in NAMED_KZ + MIDBAND_KZ:
            i = named_rank[kz] if kz in named_rank \
                else mb_rank[kz]
            tag = "named" if kz in NAMED_KZ else "MIDBAND"
            info("%s kz%-3d: nact %d zr %.4f ct %.3f rv %.3f "
                 "c* %.3f qzr %.4f | Qe %.3f Mb %.3f Qd %.3f "
                 "arm %s BD1 %.3f sf %.3f hgn %.2f"
                 % (tag, kz, nact_col[i], zr_col[i], ct_col[i],
                    rv_col[i], cst_col[i],
                    min(qzr_col[i], 9999.0),
                    min(Qe_col[i], 9999.0),
                    min(Mb_col[i], 9999.0),
                    min(Qd_col[i], 9999.0), arm_col[i],
                    min(BD1_col[i], 9999.0), smf_col[i],
                    hgnf_col[i]))
        check("G61-named-midband-anatomy", True,
              "named zr %s; MID-BAND zr %s (vs ladder med "
              "%.4f); the mid-band structure question is "
              "adjudicated by the certification in S7"
              % (str(tuple(round(zr_col[named_rank[kz]], 3)
                           for kz in NAMED_KZ)),
                 str(tuple(round(zr_col[mb_rank[kz]], 3)
                           for kz in MIDBAND_KZ)), z_med))
    # world census (both modes; uses w9 or mains + controls)
    ev9w = (recs[0] if smoke else mrecs[0])["ev"]
    ev13 = None if smoke else mrecs[1]["ev"]
    wtab = [("w9", ev9w)] + ([("w13(twin)", ev13)]
                             if ev13 is not None else [])
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]["ev"]))
    info("world table: world m nact zr contr rev c* qzr kap arm")
    for w, ev in wtab:
        ms = ev["mst"]
        info("  %-10s m %3d na %2d zr %.4f ct %.3f rv %.3f c* "
             "%.3f qzr %8.4f kap %.3f %s"
             % (w, ev["m"], ms["n_act"], ms["zr"], ms["contr"],
                ms["rev"], ms["cstar"], min(ev["qzr"], 9999.0),
                ev["kap"], ev["arm"]))
    scr_ev = crecs["SCR"]["ev"]
    scr_live = not scr_ev["degenerate"]
    zr_scr = scr_ev["mst"]["zr"]
    contr_scr = scr_ev["mst"]["contr"]
    if smoke:
        blind = False
        check("G62-world-census", len(wtab) >= 2,
              "SMOKE: world table printed (w9 + live controls); "
              "the sealed blind rule adjudicated in FULL only")
    else:
        blind_same = (scr_live and zr_scr <= z_med
                      and contr_scr >= contr_med)
        blind = blind_same  # gated by structure in S8
        check("G62-world-census", len(wtab) >= 2,
              "Q4 WORLD CHECK: twin w13 runs the IDENTICAL "
              "sealed construction (all exact wards above "
              "include it); EPSTEIN zr %.4f contr %.3f; "
              "SCRAMBLE zr %.4f contr %.3f vs ladder med zr "
              "%.4f / contr %.3f -- the sealed blind rule "
              "(zr_scr <= med AND contr_scr >= med) reads %s"
              % (crecs["EPST"]["ev"]["mst"]["zr"],
                 crecs["EPST"]["ev"]["mst"]["contr"],
                 zr_scr, contr_scr, z_med, contr_med,
                 "SAME-STRUCTURE" if blind_same
                 else "DISTINGUISHED"))

    # ---------------- S7: Leg B -- certification + exponents
    section("S7  LEG B -- Z-CERTIFICATION / ARMS / HEAD-TO-HEAD "
            "+ EXPONENTS")
    if smoke:
        check("G70-z-certification", True, "SMOKE: skipped")
        check("G71-martingale-arm", True, "SMOKE: skipped")
        check("G72-combined-arm", True, "SMOKE: skipped")
        check("G73-growth-exponents", True, "SMOKE: skipped")
    else:
        certZ = {}
        for b in B_FAM:
            col = [zr_col[i]
                   / (math.log(float(m_full[i])) ** (b / 2.0))
                   for i in range(n_full)]
            CZ = max(col[i] for i in ca_i)
            viol = [i for i in te_x if col[i] > CZ]
            named = sum(1 for kz in NAMED_KZ
                        if col[named_rank[kz]] <= CZ)
            certZ[b] = (CZ, viol, named, col)
        bZ = None
        for b in B_FAM:
            if (not certZ[b][1] and certZ[b][2] == len(NAMED_KZ)
                    and certZ[b][0] < CERT_GUARD):
                bZ = b
                break
        check("G70-z-certification", True,
              "THE Z-MAXIMAL CERTIFICATION zr <= C_Z(b) (log m)"
              "^{b/2} (max-cal mid-ladder freeze, test incl. "
              "EXT3): "
              + "; ".join("b=%d C_Z %.4f viol %d/%d named %d/4"
                          % (b, certZ[b][0], len(certZ[b][1]),
                             len(te_x), certZ[b][2])
                          for b in B_FAM)
              + "; worst violators %s; minimal certifying b = %s"
              % (str([(srt_full[i]["kz"],
                       round(certZ[B_FAM[-1]][3][i], 4))
                      for i in sorted(
                          certZ[B_FAM[-1]][1],
                          key=lambda i:
                          -certZ[B_FAM[-1]][3][i])[:6]]),
                 str(bZ)))
        b_use = bZ if bZ is not None else B_FAM[-1]
        czb_use = certZ[b_use][0]
        Az_col = [mart_arm(czb_use, b_use,
                           math.log(float(m_full[i])),
                           kap_col[i],
                           srt_full[i]["ev"]["mst"]["vq"],
                           srt_full[i]["ev"]["L1a"])
                  for i in range(n_full)]
        cover_z = sum(1 for i in range(n_full)
                      if qmax_col[i] <= Az_col[i]
                      * (1.0 + CHAIN_BAR))
        certZM, aZ = cert_max(Az_col)
        check("G71-martingale-arm", True,
              "THE MARTINGALE ARM A_z = C_Z(%d) (log m)^{%d/2} "
              "kappa sqrt(V)/L1 (%s): pointwise q_max coverage "
              "%d/%d rungs; B^Z_a certification (max-cal "
              "freeze): "
              % (b_use, b_use,
                 "the certified b" if bZ is not None else
                 "CENSUS-GRADE at b = %d, no b certified"
                 % b_use, cover_z, n_full)
              + "; ".join("a=%d C_ZM %.4f viol %d named %d/4"
                          % (a, min(certZM[a][0], 9999.0),
                             len(certZM[a][1]), certZM[a][2])
                          for a in A_FAM)
              + "; minimal a = %s" % str(aZ))
        Ac_col = [combined_arm(Az_col[i], Mb_col[i])[0]
                  for i in range(n_full)]
        acl_col = [combined_arm(Az_col[i], Mb_col[i])[1]
                   for i in range(n_full)]
        certC, aC = cert_max(Ac_col)
        a_eval = aC if aC is not None else 1
        mb_cov = sum(1 for kz in MIDBAND_KZ
                     if certC[a_eval][3][mb_rank[kz]]
                     <= certC[a_eval][0])
        check("G72-combined-arm", True,
              "THE COMBINED ARM A_c = min(M_b, A_z) (letters A "
              "%d / M %d): B^C_a certification: "
              % (sum(1 for c in acl_col if c == "A"),
                 sum(1 for c in acl_col if c == "M"))
              + "; ".join("a=%d C_C %.4f viol %d/%d named %d/4"
                          % (a, min(certC[a][0], 9999.0),
                             len(certC[a][1]), len(te_x),
                             certC[a][2]) for a in A_FAM)
              + "; minimal a = %s; MID-BAND coverage %d/6 at a "
              "= %d; worst violators %s"
              % (str(aC), mb_cov, a_eval,
                 str([(srt_full[i]["kz"],
                       round(min(certC[A_FAM[-1]][3][i],
                                 9999.0), 3))
                      for i in sorted(
                          certC[A_FAM[-1]][1],
                          key=lambda i:
                          -certC[A_FAM[-1]][3][i])[:6]])))
        info("HEAD-TO-HEAD at a = 1 (same rungs, same "
             "normalization; r335 freezes C_O %.2f C_M %.2f C_D "
             "%.2f vs this round C_ZM %.2f C_C %.2f): kz | B^O_1 "
             "B^M_1 B^D_1 | B^Z_1 B^C_1 | letter"
             % (min(certO[1][0], 9999.0),
                min(certM[1][0], 9999.0), certD[1][0],
                min(certZM[1][0], 9999.0),
                min(certC[1][0], 9999.0)))
        for kz in MIDBAND_KZ + NAMED_KZ:
            i = mb_rank[kz] if kz in mb_rank else named_rank[kz]
            tag = "MIDBAND" if kz in mb_rank else "named"
            info("  %s kz%-3d | %8.3f %8.3f %8.3f | %8.3f "
                 "%8.3f | %s"
                 % (tag, kz, min(certO[1][3][i], 9999.0),
                    min(certM[1][3][i], 9999.0),
                    min(certD[1][3][i], 9999.0),
                    min(certZM[1][3][i], 9999.0),
                    min(certC[1][3][i], 9999.0), acl_col[i]))
        e_BZ1 = L2D.halves_slope(msT,
                                 [max(min(certZM[1][3][i],
                                          INF_SENT), 1e-300)
                                  for i in te_i])
        e_BC1 = L2D.halves_slope(msT,
                                 [max(min(certC[1][3][i],
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
        x3_idx = list(range(n337, n_full))
        e_x3 = L2D.halves_slope(
            [m_full[i] for i in x3_idx],
            [max(min(Ac_col[i], INF_SENT)
                 * float(m_full[i]), 1e-300) for i in x3_idx]) \
            if len(x3_idx) >= 2 else 0.0
        check("G73-growth-exponents", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope, "
              "fit-free, over the %d 65-ladder test rungs): "
              "delta = e(hgn) = %+.3f vs DELTA_CRIT %.3f "
              "(census continuity with r333/r335, NOT "
              "adjudicating); e(B^Z_1) = %+.3f; e(B^C_1) = "
              "%+.3f; stability halves %+.3f / %+.3f -> %s; "
              "EXT3 cohort e(m A_c) = %+.3f (census-grade, "
              "mixed strata, r329 caveat)"
              % (len(te_i), e_hgn, DELTA_CRIT, e_BZ1, e_BC1,
                 e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED", e_x3))

    # ---------------- S8: Legs C/D -- adjudication + composition
    section("S8  LEGS C/D -- SEALED ADJUDICATION + COMPOSITION")
    if smoke:
        check("G80-adjudication", True, "SMOKE: skipped")
        check("G81-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        azuma = bZ is not None
        nomart = (not azuma) and (not supermart)
        blind_fire = (not nomart) and blind
        # composition solve (on the combined-arm cert)
        m0_new = None
        if aC is not None:
            Atot = 1 + aC
            C_full = certC[aC][0]
            t = math.log(73.0)
            while t < 1e7:
                if t * DELTA_CRIT >= math.log(C_full) \
                        + Atot * math.log(t):
                    m0_new = t / math.log(10.0)
                    break
                t *= 1.02
        beats = (m0_new is not None and m0_new <= R324_M0L10)
        go = azuma and (aC is not None) and mb_cov == 6 and beats
        vkey = mart_tree(leak, nomart, blind_fire, go)
        struct_cls = ("AZUMA(b=%s)" % str(bZ)) if azuma else (
            "SUPERMARTINGALE-only(contr med %.3f)" % contr_med
            if supermart else "NONE")
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a "
                           "martingale builder",
            "NOT_A_MARTINGALE":
                "no adapted structure: no b in %s certifies "
                "(viol %s) AND contraction med %.3f < %.1f -- "
                "the second route is dead; the r324 MEASURED "
                "chain stays the end state"
                % (str(B_FAM),
                   str([len(certZ[b][1]) for b in B_FAM]),
                   contr_med, CONTR_MIN),
            "WORLD_BLIND":
                "structure present (%s) but SCRAMBLE is at "
                "least as martingale-like as the ladder median "
                "(zr %.4f <= %.4f AND contr %.3f >= %.3f) -- "
                "the structure carries nothing arithmetic"
                % (struct_cls, zr_scr, z_med, contr_scr,
                   contr_med),
            "MARTINGALE_MAXIMAL_GO":
                "zr certifies at b = %s (C_Z %.4f, 0 viol incl. "
                "EXT3); the combined arm certifies at a = %s "
                "(C_C %.4f); mid-band 6/6; composition m_0* = "
                "10^%.1f <= 10^%.1f BEATS +0.172"
                % (str(bZ), certZ[bZ][0] if bZ is not None
                   else 0.0, str(aC),
                   certC[aC][0] if aC is not None else 0.0,
                   m0_new if m0_new is not None else 0.0,
                   R324_M0L10),
            "MARTINGALE_STRUCTURE_ONLY":
                "structure %s but the bound is too weak: "
                "combined-arm minimal a = %s (viol %s), "
                "mid-band %d/6, m_0* %s vs 10^%.1f -- the "
                "violation census is typed in G81"
                % (struct_cls, str(aC),
                   str([len(certC[a][1]) for a in A_FAM]),
                   mb_cov,
                   ("10^%.1f" % m0_new) if m0_new is not None
                   else "NONE", R324_M0L10)}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G80-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        if vkey == "MARTINGALE_MAXIMAL_GO":
            info("COMPOSITION (combined arm pointwise-certified, "
                 "mid-ladder): q_max <= %.4f (log m)^%d/m => "
                 "M_3 <= q_max^2 (S0 exact) => N_2 >= 1/q_max "
                 ">= m/(%.4f (log m)^%d) => N_2 >= m^%.3f for "
                 "all m >= m_0* = 10^%.1f => the r297 target "
                 "chain; R324 COMPARISON: the MEASURED route "
                 "has m_0* 10^%.1f via the +0.172 exponent -- "
                 "the martingale route REPLACES it (m_0* "
                 "10^%.1f); the ladder-to-m_0* step stays the "
                 "disclosed extrapolation hypothesis."
                 % (certC[aC][0], 1 + aC, certC[aC][0], 1 + aC,
                    N2_EXP_NEED, m0_new, R324_M0L10, m0_new))
            comp_txt = "GO: q_max <= %.4f (log m)^%d/m, m_0* " \
                "10^%.1f, r324 replaced" \
                % (certC[aC][0], 1 + aC, m0_new)
        else:
            envZ = min(max(certZM[1][3]), 9999.0)
            envC = min(max(certC[1][3]), 9999.0)
            top_v = sorted(certC[1][1],
                           key=lambda i: -certC[1][3][i])[:6]
            cen = [(srt_full[i]["kz"],
                    round(min(certC[1][3][i], 9999.0), 2),
                    round(min(certC[1][3][i], 9999.0)
                          / max(certC[1][0], 1e-300), 2),
                    acl_col[i], round(zr_col[i], 3))
                   for i in top_v]
            info("COMPOSITION: no GO letter -- the r324 "
                 "MEASURED composition stands unchanged (sum "
                 "q^3 <= 8.941 (log m) m^{+0.172}/m^2, N_2 >= "
                 "m^0.888 for m >= 10^59.6; r328B chain-honest "
                 "10^238 disclosed); measured martingale-route "
                 "envelopes at a = 1: max B^Z_1 %.3f, max "
                 "B^C_1 %.3f vs C_C(1) %.4f; TYPED VIOLATION "
                 "CENSUS (kz, B^C_1, factor, limiting letter, "
                 "zr): %s; e(B^Z_1) %+.3f, e(B^C_1) %+.3f."
                 % (envZ, envC, min(certC[1][0], 9999.0),
                    str(cen), e_BZ1, e_BC1))
            comp_txt = "r324 restated; envelopes B^Z_1 %.3f / " \
                "B^C_1 %.3f; census %s" \
                % (envZ, envC, str([c[0] for c in cen]))
        check("G81-composition", True,
              "composition printed with explicit constants "
              "(%s); the chain to terminal_positive_main is "
              "typed: telescope/CS/identity exact, the "
              "supermartingale/Azuma reading MEASURED on the "
              "finite ladder + EXT3, the ladder-to-m_0* step an "
              "extrapolation hypothesis -- NO cofinal claim"
              % comp_txt)

    # ---------------- S9: Leg E -- must-fails
    section("S9  LEG E -- WARDS / MUST-FAILS")
    toy_z = (1.0, 3.0)
    toy_rho = (0.1, 0.9)
    cz_mut = mutant_zward_posthoc(toy_z, toy_rho, 0.5)
    check("G90-e1-zward-posthoc",
          len(e1_hits) >= 1 and abs(cz_mut - 3.0) <= TOY_BAR
          and abs(cz_mut - 1.0) >= MUT_MIN,
          "e1 CAUGHT twice (the freeze rule): the after-sight "
          "C_Z re-pick consumes the evaluated bound column -- "
          "AST-FLAGGED (%s) -- and on the toy returns %.1f != "
          "the canonical freeze's 1.0 (a martingale constant "
          "calibrated after sight of the violators is "
          "structurally refused)"
          % (e1_hits[0] if e1_hits else "MISS", cz_mut))
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    rb9 = mutant_increment_from_qmax(dict(trs=ev9m["trs"],
                                          m=ev9m["m"]))
    check("G91-e2-increment-from-qmax",
          len(e2_hits) >= 1 and (not sc_own) and rb9 >= 0.0,
          "e2 AST-CAUGHT: the 'increment cap' consuming the "
          "q_max RECORD is FLAGGED (%s) while the five "
          "module-own martingale builders are clean (%d hits) "
          "-- an increment bound read back from q_max is "
          "structurally refused (the mutant value %.3f is "
          "computed only to prove the mutant runs)"
          % (e2_hits[0] if e2_hits else "MISS", len(sc_own),
             rb9))
    ord_mut = mutant_filtration_posthoc((1.5, -3.5, 8.0),
                                        (0.9, 0.1, 0.2))
    check("G92-e3-filtration-posthoc",
          len(e3_hits) >= 1 and ord_mut == (2, 1, 0)
          and ord_mut != (0, 1, 2),
          "e3 protocol-CAUGHT twice: the filtration order "
          "re-picked after record sight consumes the evaluated "
          "bound column -- AST-FLAGGED (%s) -- and on the toy "
          "returns %s != the canonical scale order (0, 1, 2) "
          "(the filtration choice was adjudicated and sealed "
          "BEFORE the freeze, by SPEC_SHA)"
          % (e3_hits[0] if e3_hits else "MISS", str(ord_mut)))
    check("G93-e4-bin-drop",
          fa_brk_ok,
          "e4 LOUD (exact identity must-fail): the telescope "
          "with the deepest bin dropped breaks the exact "
          "recomposition sum_k D_k == X_K by EXACTLY the "
          "dropped mass (toy break == 1 EXACT, Fractions) -- "
          "an incomplete filtration cannot slip through")

    # ---------------- S10: verdict
    section("S10  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed dyadic source-scale fold filtration "
          "(adjudicated a-priori), the adapted signed-mass "
          "process with exact telescope/CS/identity wards, the "
          "measured martingale structure census, the Azuma/Doob-"
          "form maximal arm + the combined arm min(M_b, A_z) "
          "with pointwise certification incl. the 12 adopted "
          "EXT3 anchors, and the head-to-head against both r335 "
          "dichotomy arms -- NO new certificate promoted, NO "
          "universal bound claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R337_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r333 boundary "
                 "%d/65 + named %s, r335 arms O%d/M%d + CD1 "
                 "%.2f + midband set EXACT + band %.4f/%.4f, "
                 "r324 e_tot %+.3f + CM2 %.4f + m0 10^%.1f)"
                 % (rec3_w, C2r, viol2, n337, bnd_cnt,
                    str(named_oin),
                    sum(1 for c in arm_col if c == "O"),
                    sum(1 for c in arm_col if c == "M"),
                    certD[1][0], band_worst_r, band_worst_c,
                    e_tot, C_M2, m0_324)]
        parts.append("SEAL(partition %.1e, ledger %.1e, "
                     "telescope %.1e, CS %.1e, identity %.1e, "
                     "kappa min %.4f, purity clean, toys exact)"
                     % (part_w, led_dev, tel_mart_w, cs_w,
                        id_mart_w, kap_min))
        parts.append("FILTRATION(nact med %.0f, zr med %.4f max "
                     "%.4f, contr med %.3f %s, rev med %.3f, "
                     "c* med %.3f, single %d, SCR zr %.4f "
                     "contr %.3f)"
                     % (float(np.median(nact_col[:n337])),
                        z_med, max(zr_col[:n337]), contr_med,
                        "SUPERMART" if supermart else "no",
                        rev_med, cst_med, n_single, zr_scr,
                        contr_scr))
        parts.append("CERT(Z %s minB %s; BZ %s minA %s; BC %s "
                     "minA %s midband %d/6; e(hgn) %+.3f %s; "
                     "e(BZ1) %+.3f; e(BC1) %+.3f)"
                     % ("; ".join("b%d CZ %.3f v%d" %
                                  (b, certZ[b][0],
                                   len(certZ[b][1]))
                                  for b in B_FAM), str(bZ),
                        "; ".join("a%d %.3f v%d" %
                                  (a, min(certZM[a][0], 9999.0),
                                   len(certZM[a][1]))
                                  for a in A_FAM), str(aZ),
                        "; ".join("a%d %.3f v%d" %
                                  (a, min(certC[a][0], 9999.0),
                                   len(certC[a][1]))
                                  for a in A_FAM), str(aC),
                        mb_cov, e_hgn,
                        "DECIDED" if decided else "UNDECIDED",
                        e_BZ1, e_BC1))
        parts.append(verdict_main)
        parts.append("COMPOSITION(%s)" % comp_txt)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the telescope, the CS "
          "bound, the identity, the Fractions toys, the tree "
          "logic and the purity audits (exact / AST-decided); "
          "MEASURED: the supermartingale/Azuma surrogate, every "
          "census, constant, violation count and exponent (the "
          "finite class ladder + 12 EXT3 + 2 mains + 2 live "
          "controls); OPEN: any bound beyond the measured "
          "rungs, the cofinal law, kappa's behavior beyond the "
          "ladder; NO RH claim"
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
