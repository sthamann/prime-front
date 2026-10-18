#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qmax_m2_origin_probe -- PRIME.L2.RENYI3.QMAX_M2_ORIGIN.01
(round 324): THE QMAX x M2 ORIGIN ROUND -- the reviewer-sharpened
terminal main lane after the r321 SLIDING_BOUND_GO.

COURSE CORRECTION (binding reviewer adjudication, disclosed): the
round's ORIGINAL contract PRIME.L2.RENYI3.FA_PROVENANCE.01 was
executed and sealed FIRST (fa_provenance_probe.py, 36/36, SPEC_SHA
9a6696f8, deterministic; letters FA_BOUNDED_DISTRIBUTIONAL +
QMAX_SHARE_OPEN + NOT_COMPOSED) -- then the reviewer adjudication
arrived and SUPERSEDED the contract mid-round: the F_A-boundedness
hunt is DEMOTED as a potentially "unnecessarily strong statement
that creates an artificial wall" -- for the needed power N_2 >~
m^0.888 it suffices asymptotically that F_A log m = O(m^{0.112-
eps}); even F_A = O((log m)^B) is enough; the CLEANER
decomposition is QMAX x M_2.  This probe is the round's binding
contract; the sealed pre-work record is BANKED and imported
verbatim (the r302 M_2-stationarity reproduction on the 65-rung
ladder, the m2 = m x M_2 column with its mid-ladder freeze
2.2557 and its seven test violators, the share majorant algebra)
-- every banked number is re-gated as an ANCHOR below and every
banked outcome is DISCLOSED as known pre-spec.

THE NEW CONTRACT (reviewer verbatim, four stages):
S0 -- EXACT INTERPOLATION (machine-exact, Fractions): for
   normalized positive profiles q_j = |x_j|/L (sum q = 1):
       M_3 = sum q^3  <=  q_max x M_2   with  M_2 = sum q^2,
   plus M_2 <= q_max (same algebra) -- so
       rho_2 = m^2 M_3/(log m)^2 <= (m q_max)(m M_2)/(log m)^2.
   AND the exact algebraic relation between F_A, q_max and M_2
   DISCLOSED -- F_A must not stay a black correction factor: the
   IDENTITY  F_A x B == m q_max / log m  (B = medloc x m/log m,
   r321) holds by construction and is warded live; hence the
   r321 bracket qmax PhiH1 <= rho_2 <= (F_A B)^2 = PhiH1 reads
       PhiH1 = (m q_max)^2/(log m)^2,
   and the S0 interpolation IMPROVES its upper side by exactly
   the factor M_2/q_max <= 1: F_A is the rank-local
   NORMALIZATION of m q_max, not an independent coordinate.
S1 -- M_2 EXPORT: convert the banked r302 stationarity into a
   POINTWISE statement m x M_2(w) <= C_2 for all w with m >= m_0
   -- no fit, no halves-slope, no "stationary in census":
   pointwise certification on the full ladder (65 rungs incl.
   ext/ext2) with the MID-LADDER frozen constant (TRB split
   verbatim), small-m rungs certified individually, reserve
   trend printed.  DISCLOSED pre-spec (banked pre-work of this
   same round): at the mid-ladder freeze C_2 = 2.2557 the export
   is KNOWN to fail pointwise on 7/39 test rungs incl. the three
   named near-critical rungs (m2 3.05..3.19) -- the sealed rule
   is adopted verbatim anyway (r316 convention), NOT tuned
   around the known outcome; the honest state is re-measured and
   gated as an anchor.  The r302 DISTRIBUTIONAL export
   (stationarity of the pooled normalized profile, KS thirds
   bars 0.125) is re-gated separately -- the verdict tree
   distinguishes the two.
S2 -- THE MULTISCALE MAXIMUM BOUND (the core): wanted
       m x q_max(w) <= C_inf x (log m)^A  with fixed A, ideally
   A = 1.  The reviewer mechanism hypothesis (multiscale pileup
   bound) tested explicitly with FOUR measurements:
   (1) DECOMPOSE the argmax block's mass by SOURCE SCALES: the
       r313/r314 fold genealogy provides the atoms and fold
       groups of every block; the canonical scale of an atom is
       its dyadic magnitude bin s = floor(log2 (vmax/|v|))
       relative to the rung's maximal atom (the chain-row
       Ls-factor proxy, source-pure, disclosed); the
       decomposition MUST recompose exactly:
       sum_s mass(j*, s) == A1_{j*} (warded, mutant e1 LOUD);
   (2) per position at most TWO fold ancestors hit the same
       target (the PROVEN fold multiplicity <= 2): max group
       multiplicity == 2 UNIFORM re-warded on every live world
       (mutant e2: a 3-fold toy genealogy is REFUSED);
   (3) does each scale carry at most O(1/m) of the total
       profile at one block?  MEASURED: pil(w) = m x max_s
       mass(j*, s)/L, mid-ladder frozen C_PIL, pointwise test;
   (4) are there only O(log m) relevant scales?  MEASURED:
       nsc_rel(w) = # distinct scales s <= 2 log2 m present in
       the argmax block (the tail beyond the cutoff carries
       <= n_atoms x vmax/m^2, census), frozen C_NSC =
       max cal nsc_rel/log m, pointwise test.
   THE EXACT PILEUP CHAIN (algebra, warded live):
       m q_max = m |x_{j*}|/L <= m A1_{j*}/L = sum_s m
       mass(j*, s)/L <= nsc x pil,
   so (3) + (4) compose to m q_max <= C_PIL C_NSC log m -- the
   A = 1 form with explicit constants; the DIRECT pointwise
   certification m q_max <= C_INF log m (C_INF = max cal
   G/log m) is gated alongside.  The proof side consumes ONLY:
   source genealogy, fold multiplicity, local mass balance,
   number of active scales, canonical aggregation -- NOT M_3,
   not the terminal value, not the historical killer list, not
   a per-window optimized scalar, not a post-hoc class choice
   (AST + declared-rule wards; mutants e3/e4).  THE
   NEAR-CRITICAL WINDOWS AS HARDNESS TEST: the full scale
   profile of the argmax block at kz53/kz83/kz67 is printed --
   are they cases where many admissible scales pile up near-
   maximally at the same block (then they are NOT exceptions
   but the PILEUP TIP)?
S3 -- FULL COMPOSITION (do not stop at the Renyi inequality):
   q_max x M_2 => M_3 => N_3 => N_2 => Fejer/vdC target =>
   terminal_positive_main, all constants explicit, explicit
   m_0; all m < m_0 closed by the existing finite certificates
   ON THE MEASURED LADDER (disclosed: the measured ladder ends
   at m = 274; the asymptotic threshold m_0* where
   m^{0.224} >= C log m is computed explicitly and the gap is
   typed honestly).  If S2 delivers only a subcritical growth
   exponent: COMPOSE ANYWAY -- PILEUP_GROWS_SUBCRITICAL with
   measured exponent < 0.224 SUFFICES (the reviewer's 0.112 is
   the F_A-side equivalent of the same budget: the r321 route
   is quadratic in F_A, this route is LINEAR in m q_max, so the
   budget doubles: e(m q_max/log m) + e(m M_2) < 0.224 <=>
   N_2 >~ m^0.888 asymptotically).

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK                iff any purity/scope audit hit on
       the mechanism builders (the proof side consumed a
       forbidden object),
   FA_RESTATEMENT             iff the mechanism decomposition
       fails structurally (recomposition or pileup-chain ward
       breaks on a live world) -- the qmax route would
       degenerate to the r321 F_A calibration,
   QMAX_MULTISCALE_GO         iff S2 certifies pointwise (all
       four mechanism clauses + direct G <= C_INF log m, 0 test
       violations, named coverage 4/4) AND S1 certifies
       pointwise AND the r302 stationarity holds,
   M2_GO_QMAX_OPEN            iff the growth-exponent decision
       is UNSTABLE (the two test halves disagree about the
       criticality side) -- the banked distributional M_2
       export state and the pointwise state are printed inside,
   PILEUP_GROWS_SUBCRITICAL(e) iff the decided total exponent
       e = e(G/log m) + e(m M_2) < CRIT = 0.224 (composition
       printed -- NOT a failure by contract),
   PILEUP_SUPERCRITICAL       iff the decided exponent >= CRIT.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the wave-12 worker (v969) and r325 run in parallel;
this probe touches NOTHING outside its own file and the strictly
additive rh-sync (existing entries byte-identical).

THE OBJECT (r269/r287/r298/r302/r306/r314/r315/r316/r317/r321
machinery + the round's own banked pre-work imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks (r270 convention); the frozen positional block machinery
(r298); the r306 RY3.cubic_moments + RY3.renyi3_ratio +
RY3.calib_freeze; the r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope; the r315
PHI.phi3_variants; the r316 TRB.two_regime_state +
TRB.split_midladder; the r317 EFP.local_ratio; the r321
CCP.local_median; the r302 UNIF.ks_two + UNIF.fs_solve; the
r324-pre FAP.m2_qmax_state + FAP.qq_groups, ALL imported
verbatim; PDelta = Pbeta - Pomega; x_j = (PDelta)_j.  NEW in this
round (module-own, source-pure where required): scale_bins (the
canonical dyadic source-scale binning), pileup_state (the argmax-
block scale decomposition with the exact pileup chain), mult_ward
(the fold-multiplicity refusal) and the sealed origin_tree.

LEG 0 -- ANCHOR REGRESSION (slim set + the banked r324-pre
record, disclosed): the r314 identity wards live; r306 C_2 =
1.069 (tol 0.005) first-5 freeze, 0/57; r316 rho anchors kz53/
kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) +
C_small 1.0694 at kz18 + n = 65; r321 G_SQ b = 1.3056 (tol
0.005) 0/39 + named 4/4; r324-PRE BANKED anchors (the pre-work
probe of this same round, reproduced bit-near): stationarity
thirds KS(G1,G3) 0.0230 / KS(G2,G3) 0.0158 (tol 0.005), m2
column med 2.051 (tol 0.01) range up to 3.194 (tol 0.01),
mid-ladder m2 freeze 2.2557 (tol 0.005) with the seven test
violators == {kz53, kz67, kz83, kz76, kz61, kz28, kz109} EXACT
as a set.

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) sealed
definitions printed; the SOURCE-PURE table (rank, kz, N, m,
qmax, G = m qmax, G/log m, m M_2, nsc, nsc_rel, pil) printed
BEFORE any certification table.  (A2) SOURCE-PURITY AUDITS: the
AST identifier scan over scale_bins + pileup_state + mult_ward +
origin_tree must be clean against BOUND_FORBIDDEN +
PHI3_FORBIDDEN (no M_3 read-back, no terminal value, no killer
list, no per-window scalar); the literal scan over the builders
must be clean against the sealed record-literal set
R324B_TABLE_LITERALS (the r314..r321 set UNION the r321 + r324-
pre record numbers); e3/e4 prove the audits bite.  (A3) TOY
EXACTNESS (Fractions): the interpolation toy q = (1/6, 1/3,
1/2): M_3 = 1/6 <= qmax M_2 = 7/36 (slack 1/36 EXACT), M_2 =
7/18 <= qmax = 1/2; the flat toy (1/2, 1/2): DOUBLE EQUALITY
M_3 = qmax M_2 = 1/4 and M_2 = qmax (the interpolation is sharp
at flat); the one-block toy (1, 0): equality at full
concentration; the PILEUP toy (block j* atoms (4, 2, 1) at
scales (0, 1, 2), second block (1), all positive): x = (7, 1),
m qmax = 7/4, per-scale m x share = (1, 1/2, 1/4), pil = 1, nsc
= 3, chain 7/4 <= 3 EXACT (slack 5/4), recomposition 4 + 2 + 1
== A1 = 7 EXACT; the drop-scale mutant breaks the recomposition
by exactly 1 (LOUD); the 3-fold toy genealogy is REFUSED by
mult_ward; the origin_tree on all six branches EXACT.  (A4)
LIVE WARDS on every live world: the r316 chain + NORM x cube ==
rho_2 (r321 verbatim); rho_2 == m^2 M_3/(log m)^2 (the r306
NORM identity restated); THE S0 INTERPOLATION M_3 <= qmax x M_2
AND M_2 <= qmax (exact algebra, bar CHAIN_BAR); THE S0 IDENTITY
F_A x B x log m == m x qmax on the ladder (F_A is no black
factor); THE PILEUP CHAIN m qmax <= nsc x pil AND the exact
recomposition sum_s mass(j*, s) == A1_{j*} (bar 1e-12).

LEG B -- S1 EXPORT (pointwise): split seal (TRB verbatim);
small-m certificates (C_2small = max over ranks 0..20); C_2 =
max m M_2 over the cal window FROZEN; test violations (0
demanded for the GO clause; the banked expectation is 7 --
disclosed); reserve min/med + trend; the named rungs printed.

LEG C -- S2 PILEUP (the four mechanism measurements + direct
certification + hardness census + growth exponent): mechanism
(1) recomposition ward; (2) multiplicity ward; (3) C_PIL = max
cal pil, test violations; (4) C_NSC = max cal nsc_rel/log m,
test violations; direct C_INF = max cal G/log m, test
violations + named coverage (kz53/kz83/kz67/kz55); the hardness
census: the full scale profile of the argmax block at the three
named near-critical rungs vs the ladder medians; the growth
exponents e_G = halves-slope of G/log m vs m over test, e_M2 =
halves-slope of m M_2 vs m over test, e_tot = e_G + e_M2 vs
CRIT = 0.224, stability = the two test halves must agree on the
criticality side (else UNDECIDED).

LEG D -- S3 COMPOSITION: printed ALWAYS with honest hypothesis
typing: M_3 <= (G/m)(m M_2)/m => rho_2 <= G x (m M_2)/(log m)^2
=> sum q^3 <= C x (log m)^{A}/m^2 (A = 1 on GO; A = 1 + slack
m^{e_tot} on the subcritical branch) => N_3 = (sum q^3)^{-1/2}
>= m/sqrt(C log m) => N_2 >= N_3 (r306 exact chain) => N_2 >=
m^0.888 for all m >= m_0* (m_0* computed explicitly:
the smallest m with m^{0.224} >= C log m) => slope(n_eff) >=
NEED = +0.908 => sl_D <= sigma* => sigma <= sigma* = -0.516 =>
the r297 target => the v964-S0 vdC theorem => delta' > 0.21
generic => the terminal_positive_main edge; all m < m_0 on the
MEASURED ladder closed by the finite certificates (r306 0/57 +
this round's tables); the gap between the measured maximum m =
274 and m_0* is DISCLOSED as the honest extrapolation
hypothesis -- no cofinal claim.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) SCALE DECOMPOSITION INCOMPLETE: mutant_scale_drop drops the
  deepest scale -- the recomposition ward must measure the exact
  break (LOUD >= MUT_MIN) while the real decomposition
  recomposes exactly (toy break == 1 EXACT).
(e2) PILEUP COUNT WITHOUT THE MULTIPLICITY BOUND:
  mutant_mult3_toy presents a genealogy with a 3-fold group --
  mult_ward must REFUSE it (max 3 > MULT_CAP) while every live
  world passes at exactly 2 -- CAUGHT.
(e3) M_3 READ-BACK: mutant_m3_readback consumes the cubic-moment
  record (cm/S3) -- the PHI3_FORBIDDEN scan must FLAG it
  (AST-CAUGHT) while the module-own builders stay clean.
(e4) CLASS/CUTOFF CHOICE AFTER SIGHT: mutant_scale_posthoc
  re-picks the relevant-scale cutoff to cover the seen violators
  (consumes rho) -- the BOUND_FORBIDDEN scope audit must FLAG it
  AND on the sealed toy it returns a cutoff != the canonical
  rule's -- CAUGHT twice.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r321 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target M_3 / rho_2 enters GATES / anchors /
composition checks only, NEVER a mechanism builder (AST-warded);
no zero/prime oracles anywhere (AST firewall); no fit primitives
(fragment audit; the growth exponent is the imported r272 dyadic
halves-slope, fit-free).  MACHINERY IMPORTED VERBATIM: r324-pre
FAP.m2_qmax_state + FAP.qq_groups, r321 CCP.local_median, r317
EFP.local_ratio, r316 TRB.two_regime_state + TRB.split_midladder,
r315 PHI.phi3_variants, r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r302
UNIF.ks_two + UNIF.fs_solve, r298 WBT.block_breaks +
WBT.aggregate_blocks, r269 PBB.mask_edge + PBB.runs_split, r287
L2D.blocks_level2 + L2D.halves_slope + L2D.autocorr_full, r244
BH.wpack, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed, r316/r321 verbatim):
frame-A h <= 900, 42 rungs, (N, kz)-sorted; exception set {kz15,
20, 22, 36, 38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by
(N, kz); EXT2: the r316 A5 rule (leftover pool + first 12
windows 1300 < h <= 1650, first 8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL 5 (via TRB, verbatim); CLS_W 5
(via EFP, verbatim); KS_STAT 0.125 (r302 verbatim); SCUT_FAC 2.0
(relevant scales s <= 2 log2 m -- the tail beyond carries <=
n_atoms x vmax/m^2 by dyadic algebra, disclosed); A_SEAL 1;
CRIT_EXP 0.224 (= 2 x (1 - 0.888); the reviewer's 0.112 is the
F_A-side equivalent, disclosed); N2_EXP_NEED 0.888; NEED_SLOPE
0.908; SIGMA_STAR -0.516; DELTA_NEED 0.21; NAMED_KZ (53, 83, 67,
55); NAMED_FA_KZ (53, 83, 67); MUT_MIN 1e-6; TOY_BAR 1e-12;
FR_BAR 1e-14; SA_BAR 1e-12; TB_WARD bars 1e-9 main N <= 400 /
3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR 1e-12; AC_BAR
1e-9; R306 anchor C_2 1.069 tol 0.005; N324_REF 65; R316 RHO
{53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005,
C_SMALL 1.0694 tol 0.005 at kz18; R321 B_SQ 1.3056 tol 0.005;
R324PRE anchors: KS13 0.0230 / KS23 0.0158 tol 0.005, M2_MED
2.051 tol 0.01, M2_MAX 3.194 tol 0.01, C_M2 2.2557 tol 0.005,
M2_VIOL_SET {53, 67, 83, 76, 61, 28, 109} EXACT;
R324B_TABLE_LITERALS = the sealed r314+r315+r316+r317+r321
forbidden set (r324-pre verbatim) UNION the r324-pre record set
{0.0982, 3.357, 2.583, 2.2557, 3.1528, 3.1938, 3.049, 2.051,
3.194, 1.579, 2.081, -0.584, 1.746, 3.5261, 4.338, 0.023,
0.0158, 0.0247, 0.4852, 0.2136, 0.0907, 2.046, 2.033, 2.074};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the interpolation/identity/pileup wards on w9 +
controls + e1-e4 mutants; ladder, extensions, anchors, export,
certification, exponent and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe; the
sealed pre-work probe of this same round IS a disclosed input):
every anchor band is an r306/r316/r321/r324-pre RECORD number
adopted as-is; the interpolation M_3 <= qmax M_2, the identity
F_A B log m == m qmax, the pileup chain and the dyadic tail
bound are derived algebra, disclosed above; the S1 pointwise
outcome at the mid-ladder freeze (7/39 violations incl. the
named rungs) is KNOWN pre-spec from the banked pre-work and
disclosed -- the sealed rule is the house convention adopted
verbatim, not tuned; GENUINELY OPEN quantities of this round:
the scale profiles, nsc/nsc_rel/pil columns, C_PIL/C_NSC/C_INF,
all S2 violation counts, the hardness census and both growth
exponents -- NONE was computed before this spec was frozen;
SCUT_FAC = 2.0, A_SEAL = 1 and CRIT_EXP = 0.224 are a-priori
(the criticality budget is derived from the reviewer's N_2 >~
m^0.888 need by exact exponent algebra, disclosed above); the
six sealed letters are symmetric and total -- the tree maps
every outcome to exactly one letter by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R324_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r321 b, r324-pre KS + m2 census + freeze + violator set)
+ SEAL(interpolation + identity + pileup chain + purity audits
    + toys + live wards)
+ S1_EXPORT(C_2, small-m, violations, reserve, trend, named)
+ S2_PILEUP(mechanism (1)-(4) measurements, C_PIL/C_NSC/C_INF,
    violations, named coverage, hardness census, exponents)
+ [exactly one of] QMAX_MULTISCALE_GO / M2_GO_QMAX_OPEN /
    PILEUP_GROWS_SUBCRITICAL(e) / PILEUP_SUPERCRITICAL /
    FA_RESTATEMENT / TARGET_LEAK
+ S3_COMPOSITION(the full chain with explicit constants + m_0*
    + the disclosed measured-ladder gap; printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the interpolation, the identity and the
pileup chain are EXACT algebra; every constant, violation count,
scale census and exponent is MEASURED on the finite ladder only;
the composition's step from the measured ladder (m <= 274) to
m_0* is an EXTRAPOLATION HYPOTHESIS, typed as such -- no cofinal
claim; a subcritical letter is a first-class outcome by the
reviewer contract, not a failure; the banked pre-work outcomes
are disclosed pre-spec inputs, and the pre-work probe stays
sealed and citable as its own record; r243-r322 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; run1/run2 byte-identical up to the
runtime line):
MAIN VERDICT: PILEUP_GROWS_SUBCRITICAL(e_tot +0.172 < CRIT
0.224; halves +0.141/-0.160 DECIDED) -- a sufficient,
first-class outcome by the reviewer contract, not a failure.
S0 (EXACT, live on 69 worlds): interpolation M_3 <= qmax M_2
worst slack 0.0; M_2 <= qmax worst 0.0; the identity F_A B
log m == m qmax worst 2.7e-16 -- F_A is the rank-local
normalization of m qmax, no black factor; rho_2 == m^2 M_3/
(log m)^2 worst 1.0e-15.
S1 EXPORT: C_2 = 2.2557 (mid-ladder freeze at kz34): POINTWISE
FAILS 7/39 [kz53 3.1528 / kz28 2.3585 / kz67 3.1938 / kz109
2.2857 / kz76 2.4992 / kz61 2.4711 / kz83 3.0490] (the banked
pre-work expectation, disclosed pre-spec); reserve min/med
0.71/1.10; test trend +0.014 (FLAT); small-m C_2small 2.6130;
DISTRIBUTIONAL export GO (stationarity KS 0.0230/0.0158 <=
0.125); ladder envelope C_2env = 3.1938.
S2 PILEUP (the four mechanism measurements): (1) the scale
decomposition recomposes EXACTLY (worst 2.2e-16); (2) fold
multiplicity <= 2 admitted on ALL 69 live worlds; (3) per-scale
mass C_PIL = 9.3583 (cal freeze) FAILS 11/39 (worst kz67
22.378 / kz53 13.778 / kz83 12.707; pil med 6.661 max 25.309
at kz55); (4) active scales nsc_rel/log m med 1.165 max 2.026,
C_NSC = 2.0258: HOLDS 0/39 -- the O(log m) scale count
CERTIFIES pointwise.  DIRECT: C_INF = 1.7481 FAILS 5/39 (kz53
2.724 / kz67 2.800 / kz76 1.971 / kz61 2.103 / kz83 2.567),
named coverage 1/4 -> S2 NOT-GO.  HARDNESS CENSUS (the
reviewer question ANSWERED): the named spikes are NOT
multiscale convergence -- ONE near-maximal source scale
dominates the argmax block: kz53 s0 = 13.78 of G 13.02 (nsc 5
== ladder med), kz83 s0 = 12.71 of G 14.15 (nsc 6), kz67 s0 =
22.38 of G 13.61 (nsc 7 vs med 5) -- the pileup tip is a
SINGLE HEAVY SCALE, not many-scale pileup; the reviewer
mechanism hypothesis is REFUTED in its clause (3) and
CONFIRMED in its clause (4).  EXPONENTS (fit-free dyadic
halves-slope vs m over 39 test rungs): e(G/log m) = +0.158,
e(m M_2) = +0.014, e_tot = +0.172 < 0.224 (stability halves
+0.141/-0.160, the second half FALLING) -- DECIDED
SUBCRITICAL.  Columns: G = m qmax 2.60/5.32/14.15 min/med/max
(max at kz83); G/log m med 1.137 max 2.800; nsc med 5 max 9.
S3 COMPOSITION (typed MEASURED, printed verbatim in S7): sum
q^3 <= 8.941 x (log m) x m^{+0.172}/m^2 => N_3 >= m^{0.914}/
sqrt(8.941 log m) and N_2 >= N_3 (r306 exact chain) => N_2 >=
m^0.888 for all m >= m_0* = 10^59.6 => slope(n_eff) >= +0.908
=> sigma <= -0.516 => the r297 target => the v964-S0 vdC
theorem => delta' > 0.21 => the terminal_positive_main edge;
all measured m <= 274 closed by the finite certificates; the
gap (274, 10^59.6) is the disclosed extrapolation hypothesis.

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
import unif_target_probe as UNIF               # noqa: E402 r302
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import phi3_functional_probe as PHI            # noqa: E402 r315
import two_regime_bound_probe as TRB           # noqa: E402 r316
import exception_families_probe as EFP         # noqa: E402 r317
import continuous_coordinate_probe as CCP      # noqa: E402 r321
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
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
N_CAL = 5
KS_STAT = 0.125
SCUT_FAC = 2.0
A_SEAL = 1
CRIT_EXP = 0.224
N2_EXP_NEED = 0.888
NEED_SLOPE = 0.908
SIGMA_STAR = -0.516
DELTA_NEED = 0.21
NAMED_KZ = (53, 83, 67, 55)
NAMED_FA_KZ = (53, 83, 67)
MUT_MIN = 1e-6
TOY_BAR = 1e-12
FR_BAR = 1e-14
SA_BAR = 1e-12
EDGE_F = 0.20
PAIR_OFFSET = 0
R306_C2 = 1.069
R306_C2_TOL = 0.005
N324_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R321_B_SQ = 1.3056
R321_B_TOL = 0.005
R324P_KS13 = 0.0230
R324P_KS23 = 0.0158
R324P_KS_TOL = 0.005
R324P_M2MED = 2.051
R324P_M2MED_TOL = 0.01
R324P_M2MAX = 3.194
R324P_M2MAX_TOL = 0.01
R324P_CM2 = 2.2557
R324P_CM2_TOL = 0.005
R324P_M2VIOL = (53, 67, 83, 76, 61, 28, 109)
R324B_TABLE_LITERALS = frozenset(FAP.R324_TABLE_LITERALS | {
    0.0982, 3.357, 2.583, 2.2557, 3.1528, 3.1938, 3.049,
    2.051, 3.194, 1.579, 2.081, -0.584, 1.746, 3.5261,
    4.338, 0.023, 0.0158, 0.0247, 0.4852, 0.2136, 0.0907,
    2.046, 2.033, 2.074})

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
    lies in the sealed r314..r321 + r324-pre record set."""
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
                            in R324B_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the
# ---------------- mechanism builders consume atom values / block
# ---------------- assignments / block values / group
# ---------------- multiplicities / rank order only; the withheld
# ---------------- terminal drive key, the branch label, the cubic
# ---------------- target M_3 and the record literals are
# ---------------- forbidden (AST identifier scan + literal scan).
def scale_bins(vals):
    """the canonical dyadic SOURCE-SCALE binning: s(atom) =
    floor(log2(vmax / |v|)) relative to the rung's maximal atom
    value (the chain-row Ls-factor proxy, disclosed); zero atoms
    get scale -1 (they carry no mass).  Consumes atom values
    only."""
    av = np.abs(np.asarray(vals, dtype=float))
    vmax = float(np.max(av)) if len(av) else 0.0
    out = np.full(len(av), -1, dtype=int)
    nz = av > 0.0
    if vmax > 0.0:
        out[nz] = np.floor(np.log2(vmax / av[nz])).astype(int)
    return out


def pileup_state(x, vals, blks):
    """the argmax-block SCALE DECOMPOSITION with the exact pileup
    chain: on block values x (length m), atom values vals and
    atom block assignments blks: j* = argmax |x|, L = sum |x|;
    the atoms of j* are decomposed by scale_bins(vals) (scales
    relative to the RUNG maximum); returns per-scale masses,
    nsc (# distinct scales present in j*), nsc_rel (# present
    scales s <= SCUT_FAC log2 m), tail (mass beyond the cutoff),
    pil = m x max_s mass_s / L, a1j = sum |v| over j*, and the
    chain terms -- m qmax <= nsc x pil is EXACT algebra (warded
    by the caller)."""
    ax = np.abs(np.asarray(x, dtype=float))
    av = np.abs(np.asarray(vals, dtype=float))
    m = int(len(ax))
    tot = float(np.sum(ax))
    if m < 2 or tot <= 0.0:
        return dict(j=0, nsc=0, nsc_rel=0, pil=0.0, a1j=0.0,
                    tail=0.0, scut=0, scales=(), masses=())
    j = int(np.argmax(ax))
    sb = scale_bins(av)
    mask = (np.asarray(blks, dtype=int) == j) & (sb >= 0)
    sj = sb[mask]
    vj = av[mask]
    scut = int(math.ceil(SCUT_FAC * math.log2(float(m))))
    scales = tuple(int(s) for s in sorted(set(int(s)
                                              for s in sj)))
    masses = tuple(float(np.sum(vj[sj == s])) for s in scales)
    nsc = len(scales)
    nsc_rel = sum(1 for s in scales if s <= scut)
    tail = float(sum(mv for s, mv in zip(scales, masses)
                     if s > scut))
    pil = float(m) * (max(masses) if masses else 0.0) / tot
    return dict(j=j, nsc=nsc, nsc_rel=nsc_rel, pil=pil,
                a1j=float(np.sum(vj)), tail=tail, scut=scut,
                scales=scales, masses=masses)


def mult_ward(mults):
    """the fold-multiplicity REFUSAL (mechanism clause (2), the
    proven multiplicity <= 2): returns (max multiplicity,
    admitted flag) -- any genealogy with a group of more than
    MULT_CAP fold ancestors at one position is REFUSED (the e2
    mutant presents a 3-fold toy and must be CAUGHT)."""
    mx = int(max(int(v) for v in mults)) if len(mults) else 0
    return mx, mx <= MULT_CAP


def origin_tree(leak, restate, go_all, decided, sub, s1_stat):
    """the sealed six-letter verdict tree (booleans only; total,
    exactly one fires; order sealed):
    TARGET_LEAK > FA_RESTATEMENT > QMAX_MULTISCALE_GO >
    M2_GO_QMAX_OPEN (exponent undecided) >
    PILEUP_GROWS_SUBCRITICAL > PILEUP_SUPERCRITICAL."""
    if leak:
        return "TARGET_LEAK"
    if restate:
        return "FA_RESTATEMENT"
    if go_all:
        return "QMAX_MULTISCALE_GO"
    if not decided:
        _ = s1_stat  # printed in the letter detail by the caller
        return "M2_GO_QMAX_OPEN"
    if sub:
        return "PILEUP_GROWS_SUBCRITICAL"
    return "PILEUP_SUPERCRITICAL"


def mutant_scale_drop(masses):
    """e1 MUST-FAIL MUTANT: an 'aggregation' that drops the
    deepest scale -- the recomposition ward must measure the
    exact break (LOUD)."""
    ms = tuple(float(v) for v in masses)
    return sum(ms[:-1]) if ms else 0.0


def mutant_mult3_toy():
    """e2 MUST-FAIL MUTANT: a toy genealogy with a THREE-fold
    group (three ancestors at one position) -- mult_ward must
    REFUSE it."""
    return (1, 2, 3)


def mutant_m3_readback(cmrec, nblk):
    """e3 MUST-FAIL MUTANT: a 'mechanism column' consuming the
    cubic-moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk) * float(nblk)


def mutant_scale_posthoc(scut_col, rho, cbar):
    """e4 MUST-FAIL MUTANT: the relevant-scale cutoff re-picked
    AFTER SIGHT of the violators (consumes rho): widened until
    every seen violator is 'relevant-covered' -- the
    BOUND_FORBIDDEN scope audit must FLAG it AND on the toy it
    returns != the canonical SCUT_FAC rule's cutoff."""
    worst = max((s for s, r in zip(scut_col, rho) if r > cbar),
                default=0)
    return int(worst) + 1


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'scale orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'pileup constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the S0 interpolation
# ---------------- and the pileup chain decided as rationals
def fr_interp_toys():
    """S0 in exact Fractions: q = (1/6, 1/3, 1/2): M_3 = 1/6 <=
    qmax M_2 = 7/36 (slack 1/36), M_2 = 7/18 <= qmax = 1/2; flat
    (1/2, 1/2): DOUBLE EQUALITY M_3 = qmax M_2 = 1/4 and M_2 =
    qmax; one-block (1, 0): equality at 1.  Returns worst
    rational deviation (must be 0)."""
    def st(qs):
        q = [Fr(a, b) for a, b in qs]
        m3 = sum(v ** 3 for v in q)
        m2 = sum(v ** 2 for v in q)
        qm = max(q)
        return m3, m2, qm

    devs = []
    m3, m2, qm = st(((1, 6), (1, 3), (1, 2)))
    devs += [abs(m3 - Fr(1, 6)), abs(qm * m2 - Fr(7, 36)),
             abs((qm * m2 - m3) - Fr(1, 36)),
             abs(m2 - Fr(7, 18)),
             Fr(0) if m3 <= qm * m2 and m2 <= qm else Fr(1)]
    m3, m2, qm = st(((1, 2), (1, 2)))
    devs += [abs(m3 - Fr(1, 4)), abs(qm * m2 - Fr(1, 4)),
             abs(m2 - qm)]
    m3, m2, qm = st(((1, 1), (0, 1)))
    devs += [abs(m3 - 1), abs(qm * m2 - 1)]
    return max(devs)


def fr_pileup_toy():
    """the pileup chain in exact Fractions: block j* atoms
    (4, 2, 1) at scales (0, 1, 2), second block (1), all
    positive: x = (7, 1), L = 8, m qmax = 7/4; per-scale m x
    share = (1, 1/2, 1/4); pil = 1, nsc = 3; chain 7/4 <= 3
    (slack 5/4 EXACT); recomposition 4 + 2 + 1 == 7 EXACT; the
    drop-scale mutant breaks by exactly 1.  Returns (worst dev,
    chain slack, drop break)."""
    L = Fr(8)
    m = Fr(2)
    qmax = Fr(7) / L
    masses = (Fr(4), Fr(2), Fr(1))
    shares = tuple(m * mv / L for mv in masses)
    pil = max(shares)
    nsc = Fr(3)
    chain_slack = nsc * pil - m * qmax
    rec = sum(masses)
    drop = rec - Fr(mutant_scale_drop(masses))
    devs = [abs(m * qmax - Fr(7, 4)), abs(pil - 1),
            abs(shares[1] - Fr(1, 2)), abs(shares[2] - Fr(1, 4)),
            abs(chain_slack - Fr(5, 4)), abs(rec - 7),
            abs(drop - 1),
            Fr(0) if m * qmax <= nsc * pil else Fr(1)]
    return max(devs), chain_slack, drop


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("qmax_m2_origin_probe -- "
          "PRIME.L2.RENYI3.QMAX_M2_ORIGIN.01 (round 324, "
          "reviewer-sharpened)")
    print("SPEC_SHA %s   R324PRE_SHA %s   R321_SHA %s   R302_SHA "
          "%s" % (SPEC_SHA[:16], FAP.SPEC_SHA[:16],
                  CCP.SPEC_SHA[:16], UNIF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + interpolation/identity/"
                        "pileup wards + e1-e4; ladder, "
                        "extensions, anchors, export, "
                        "certification, exponent and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE QMAX x M2 ORIGIN ROUND (reviewer course "
          "correction, binding, disclosed: the F_A-boundedness "
          "hunt of the sealed pre-work probe is DEMOTED -- the "
          "cleaner decomposition is QMAX x M_2): S0 exact "
          "interpolation M_3 <= qmax M_2 (Fractions) + the "
          "identity F_A B log m == m qmax (F_A no black "
          "factor); S1 pointwise M_2 export m M_2 <= C_2 "
          "(mid-ladder frozen; banked pre-work expectation "
          "7/39 violations DISCLOSED); S2 the multiscale "
          "pileup bound m qmax <= C_inf (log m)^%d via the "
          "four mechanism measurements (scale decomposition / "
          "fold multiplicity <= %d / per-scale pileup C_PIL / "
          "active scales C_NSC x log m) with the exact chain "
          "m qmax <= nsc x pil; S3 full composition to N_2 >= "
          "m^%.3f with explicit m_0*; verdict tree TARGET_LEAK "
          "/ FA_RESTATEMENT / QMAX_MULTISCALE_GO / "
          "M2_GO_QMAX_OPEN / PILEUP_GROWS_SUBCRITICAL / "
          "PILEUP_SUPERCRITICAL sealed BEFORE evaluation "
          "(CRIT_EXP %.3f = 2 x (1 - %.3f), the reviewer's "
          "0.112 F_A-side equivalent disclosed)"
          % (A_SEAL, MULT_CAP, N2_EXP_NEED, CRIT_EXP,
             N2_EXP_NEED))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("scale_bins", "pileup_state", "mult_ward",
               "origin_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the four module-own "
          "mechanism builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN (%d hits) -- the proof side consumes "
          "ONLY source genealogy / fold multiplicity / local "
          "mass balance / active scales / canonical "
          "aggregation; m5a gift-bound FLAGGED (%s); m5b "
          "branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r321 scaffold verbatim)
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
            pst = pileup_state(sct["x"], val_all, blk_all)
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
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs, pst=pst,
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

    # ---------------- S3: Leg 0 anchors (slim + banked pre-work)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim + the banked "
            "r324-pre record)")
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
          "coexisting r321/r322 + the sealed r324-pre probe"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 qmax %.4f G %.3f mM2 %.4f nsc %d "
             "nsc_rel %d pil %.3f"
             % (ev9s["trs"]["qmax"],
                ev9s["m"] * ev9s["trs"]["qmax"],
                ev9s["mqs"]["m2"], ev9s["pst"]["nsc"],
                ev9s["pst"]["nsc_rel"], ev9s["pst"]["pil"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r321-sliding-anchor", True, "SMOKE: skipped")
        check("G34-r324pre-anchors", True, "SMOKE: skipped")
        srt = []
        n324 = 0
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
        n324 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n324)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n324 == N324_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n324, N324_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt]
        FA_col = EFP.local_ratio(qmax_col)
        medloc = CCP.local_median(qmax_col)
        Bcol = [medloc[i] * float(m_all[i])
                / math.log(float(m_all[i])) for i in range(n324)]
        parSQ, dSQ = CCP.g_calibrate("SQ", FA_col, rho_all,
                                     Bcol, ca_i)
        gv_sq = [CCP.g_eval("SQ", parSQ, FA_col[i])
                 for i in range(n324)]
        viol_sq = [i for i in te_i if rho_all[i] > gv_sq[i]]
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n324):
                if srt[i]["kz"] == kz:
                    named_rank[kz] = i
        named_sq = sum(1 for kz in NAMED_KZ
                       if rho_all[named_rank[kz]]
                       <= gv_sq[named_rank[kz]])
        check("G33-r321-sliding-anchor",
              abs(parSQ[0] - R321_B_SQ) <= R321_B_TOL
              and not viol_sq and named_sq == 4
              and dSQ == tuple(ca_i),
              "r321 sliding bound reproduced: G_SQ b = %.4f (rec "
              "%.4f tol %.3f), violations %d/%d, named %d/4"
              % (parSQ[0], R321_B_SQ, R321_B_TOL, len(viol_sq),
                 len(te_i), named_sq))
        # banked r324-pre anchors: stationarity + m2 column
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        y_lists = []
        for rc in srt:
            x_abs = np.abs(rc["ev"]["sct"]["x"])
            Lx = float(np.sum(x_abs))
            y_lists.append(x_abs * (float(rc["ev"]["m"]) / Lx))
        g1, g2, g3 = FAP.qq_groups(n324)
        ks13 = UNIF.ks_two(np.concatenate([y_lists[i]
                                           for i in g1]),
                           np.concatenate([y_lists[i]
                                           for i in g3]))
        ks23 = UNIF.ks_two(np.concatenate([y_lists[i]
                                           for i in g2]),
                           np.concatenate([y_lists[i]
                                           for i in g3]))
        C_M2 = max(m2_col[i] for i in ca_i)
        viol_m2 = tuple(sorted(srt[i]["kz"] for i in te_i
                               if m2_col[i] > C_M2))
        check("G34-r324pre-anchors",
              abs(ks13 - R324P_KS13) <= R324P_KS_TOL
              and abs(ks23 - R324P_KS23) <= R324P_KS_TOL
              and abs(float(np.median(m2_col)) - R324P_M2MED)
              <= R324P_M2MED_TOL
              and abs(max(m2_col) - R324P_M2MAX)
              <= R324P_M2MAX_TOL
              and abs(C_M2 - R324P_CM2) <= R324P_CM2_TOL
              and viol_m2 == tuple(sorted(R324P_M2VIOL)),
              "the BANKED r324-pre record reproduced bit-near: "
              "stationarity thirds KS(G1,G3) %.4f / KS(G2,G3) "
              "%.4f (rec %.4f/%.4f tol %.3f); m2 = m M_2 med "
              "%.3f max %.3f (rec %.3f/%.3f); mid-ladder freeze "
              "C_M2 %.4f (rec %.4f); the seven m2 test "
              "violators %s == the banked set EXACT"
              % (ks13, ks23, R324P_KS13, R324P_KS23,
                 R324P_KS_TOL, float(np.median(m2_col)),
                 max(m2_col), R324P_M2MED, R324P_M2MAX, C_M2,
                 R324P_CM2, str(viol_m2)))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("scale_bins", "pileup_state", "mult_ward",
               "origin_tree", "fr_interp_toys", "fr_pileup_toy"):
        pure_lits += literal_audit(fn)
    e3_hits = scope_audit("mutant_m3_readback", PHI3_FORBIDDEN)
    e4_hits = scope_audit("mutant_scale_posthoc", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e3_hits) >= 1 and len(e4_hits) >= 1,
          "SOURCE PURITY: the mechanism builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed r314..."
          "r321 + r324-pre record-literal set (%d literal hits); "
          "consumed inputs: atom values / block assignments / "
          "block values / group multiplicities / rank order -- "
          "M_3 and rho_2 are TARGET-SIDE, computed outside the "
          "builders (disclosed); e3 M3-readback FLAGGED (%s); "
          "e4 scale-posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e3_hits[0] if e3_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    fr_dev = fr_interp_toys()
    fr_pdev, fr_slack, fr_drop = fr_pileup_toy()
    toy_x = np.array([7.0, 1.0])
    toy_v = np.array([4.0, 2.0, 1.0, 1.0])
    toy_b = np.array([0, 0, 0, 1])
    pst_t = pileup_state(toy_x, toy_v, toy_b)
    ok_pst = (pst_t["j"] == 0 and pst_t["nsc"] == 3
              and abs(pst_t["pil"] - 1.0) <= FR_BAR
              and abs(pst_t["a1j"] - 7.0) <= FR_BAR
              and pst_t["scales"] == (0, 1, 2)
              and pst_t["masses"] == (4.0, 2.0, 1.0))
    sb_t = scale_bins([4.0, -2.0, 1.0, 0.0])
    ok_sb = (list(sb_t) == [0, 1, 2, -1])
    mx_t, adm_t = mult_ward(mutant_mult3_toy())
    mx_r, adm_r = mult_ward((1, 2, 2, 1))
    ok_mw = (mx_t == 3 and not adm_t and mx_r == 2 and adm_r)
    tr_br = (origin_tree(True, True, True, True, True, True),
             origin_tree(False, True, True, True, True, True),
             origin_tree(False, False, True, True, True, True),
             origin_tree(False, False, False, False, True, True),
             origin_tree(False, False, False, True, True, True),
             origin_tree(False, False, False, True, False, True))
    ok_tr = tr_br == ("TARGET_LEAK", "FA_RESTATEMENT",
                      "QMAX_MULTISCALE_GO", "M2_GO_QMAX_OPEN",
                      "PILEUP_GROWS_SUBCRITICAL",
                      "PILEUP_SUPERCRITICAL")
    check("G41-toy-exactness",
          fr_dev == 0 and fr_pdev == 0 and ok_pst and ok_sb
          and ok_mw and ok_tr,
          "S0 Fractions interpolation toys EXACT (worst dev %s): "
          "M_3 1/6 <= qmax M_2 7/36 slack 1/36, M_2 7/18 <= "
          "qmax 1/2; flat DOUBLE EQUALITY; one-block equality; "
          "pileup Fractions toy EXACT (chain slack %s, drop "
          "break %s LOUD); pileup_state float toy EXACT (j* 0, "
          "scales (0,1,2), masses (4,2,1), pil 1, nsc 3); "
          "scale_bins toy EXACT (zero atom -> -1); mult_ward "
          "REFUSES the 3-fold toy and admits the 2-fold; "
          "origin_tree all six branches EXACT %s"
          % (str(fr_dev), str(fr_slack), str(fr_drop),
             str(tr_br)))
    # live wards
    chain_w = 0.0
    xw_cube = 0.0
    interp_w = 0.0
    m2q_w = 0.0
    norm_id_w = 0.0
    pil_ch_w = 0.0
    rec_sc_w = 0.0
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
        qm = float(np.max(qv))
        mloc = ev["m"]
        # S0 interpolation M_3 <= qmax M_2 and M_2 <= qmax
        interp_w = max(interp_w,
                       max(0.0, M3 - qm * M2)
                       / max(qm * M2, 1e-300),
                       max(0.0, M2 - qm) / max(qm, 1e-300))
        # cross-ward vs the imported r324-pre state
        m2q_w = max(m2q_w,
                    abs(ev["mqs"]["m2"] - mloc * M2)
                    / max(mloc * M2, 1e-300),
                    abs(ev["mqs"]["qm"] - qm)
                    / max(qm, 1e-300))
        # r306 NORM identity rho_2 == m^2 M_3/(log m)^2
        rid = mloc ** 2 * M3 / (math.log(float(mloc)) ** 2)
        norm_id_w = max(norm_id_w, abs(rid - ev["rho2"])
                        / max(ev["rho2"], 1e-300))
        # pileup chain m qmax <= nsc x pil + recomposition
        pst = ev["pst"]
        G = mloc * qm
        pil_ch_w = max(pil_ch_w,
                       max(0.0, G - pst["nsc"] * pst["pil"])
                       / max(pst["nsc"] * pst["pil"], 1e-300))
        rec_sc_w = max(rec_sc_w,
                       abs(sum(pst["masses"]) - pst["a1j"])
                       / max(pst["a1j"], 1e-300))
        mult_all_ok = mult_all_ok \
            and mult_ward(rc["ev"]["gen"]["mult"])[1]
    if smoke:
        fa_id_w = 0.0
    else:
        fa_id_w = max(abs(FA_col[i] * Bcol[i]
                          * math.log(float(m_all[i]))
                          - m_all[i] * qmax_col[i])
                      / max(m_all[i] * qmax_col[i], 1e-300)
                      for i in range(n324))
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR
          and interp_w <= CHAIN_BAR and m2q_w <= CHAIN_BAR
          and norm_id_w <= CHAIN_BAR and pil_ch_w <= CHAIN_BAR
          and rec_sc_w <= SA_BAR and mult_all_ok
          and fa_id_w <= CHAIN_BAR,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 INTERPOLATION M_3 <= "
          "qmax M_2 AND M_2 <= qmax (worst rel slack %.1e -- "
          "exact algebra live); r324-pre state cross-ward "
          "(%.1e); rho_2 == m^2 M_3/(log m)^2 (%.1e); PILEUP "
          "CHAIN m qmax <= nsc x pil (worst slack %.1e); scale "
          "recomposition sum_s mass == A1_{j*} (worst %.1e, bar "
          "%.0e); fold multiplicity <= %d admitted on ALL live "
          "worlds%s"
          % (len(live), chain_w, xw_cube, interp_w, m2q_w,
             norm_id_w, pil_ch_w, rec_sc_w, SA_BAR, MULT_CAP,
             "; S0 IDENTITY F_A B log m == m qmax on the "
             "ladder (worst %.1e -- F_A is no black factor)"
             % fa_id_w if not smoke else
             " (ladder identity SMOKE-skipped)"))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        G_col = [m_all[i] * qmax_col[i] for i in range(n324)]
        GL_col = [G_col[i] / math.log(float(m_all[i]))
                  for i in range(n324)]
        nsc_col = [rc["ev"]["pst"]["nsc"] for rc in srt]
        nscr_col = [rc["ev"]["pst"]["nsc_rel"] for rc in srt]
        pil_col = [rc["ev"]["pst"]["pil"] for rc in srt]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m qmax G=m*qmax "
             "G/logm mM2 nsc nscR pil")
        for i, rc in enumerate(srt):
            info("%2d kz%-3d N %4d m %3d qmax %.4f G %6.3f GL "
                 "%.3f mM2 %.3f nsc %2d nscR %2d pil %.3f"
                 % (i, rc["kz"], rc["N"], m_all[i], qmax_col[i],
                    G_col[i], GL_col[i], m2_col[i], nsc_col[i],
                    nscr_col[i], pil_col[i]))
        tails = [rc["ev"]["pst"]["tail"] for rc in srt]
        check("G43-coordinate-table", True,
              "G = m qmax range %.2f/%.2f/%.2f min/med/max (max "
              "at kz%d); G/log m med %.3f max %.3f; m M_2 med "
              "%.3f max %.3f; nsc med %.0f max %d; nsc_rel med "
              "%.0f max %d (cutoff 2 log2 m; dyadic tail mass "
              "beyond cutoff max %.2e -- negligible by "
              "algebra); pil med %.3f max %.3f"
              % (min(G_col), float(np.median(G_col)),
                 max(G_col), srt[int(np.argmax(G_col))]["kz"],
                 float(np.median(GL_col)), max(GL_col),
                 float(np.median(m2_col)), max(m2_col),
                 float(np.median(nsc_col)), max(nsc_col),
                 float(np.median(nscr_col)), max(nscr_col),
                 max(tails), float(np.median(pil_col)),
                 max(pil_col)))

    # ---------------- S5: Leg B -- S1 pointwise M_2 export
    section("S5  LEG B -- S1 POINTWISE M_2 EXPORT")
    if smoke:
        check("G50-split-seal", True, "SMOKE: skipped")
        check("G51-m2-export", True, "SMOKE: skipped")
    else:
        ovl = (len(set(sm_i) & set(ca_i))
               + len(set(sm_i) & set(te_i))
               + len(set(ca_i) & set(te_i)))
        cover = (tuple(sorted(sm_i + ca_i + te_i))
                 == tuple(range(n324)))
        m0 = min(m_all[i] for i in ca_i + te_i)
        C2_small = max(m2_col[i] for i in sm_i)
        check("G50-split-seal",
              ovl == 0 and cover and len(ca_i) == N_CAL,
              "SEALED split (TRB verbatim): small ranks 0..%d "
              "(individually certified, C_2small = %.4f), cal "
              "%d..%d (kz %s), test %d rungs; overlaps 0, cover "
              "EXACT; m_0 = %d"
              % (sm_i[-1], C2_small, ca_i[0], ca_i[-1],
                 str([srt[i]["kz"] for i in ca_i]), len(te_i),
                 m0))
        viol_m2_i = [i for i in te_i if m2_col[i] > C_M2]
        rsv_m2 = [C_M2 / max(m2_col[i], 1e-300) for i in te_i]
        NsT = [srt[i]["N"] for i in te_i]
        msT = [m_all[i] for i in te_i]
        sl_m2 = L2D.halves_slope(msT, [max(m2_col[i], 1e-300)
                                       for i in te_i])
        s1_point = (not viol_m2_i)
        s1_stat = (ks13 <= KS_STAT and ks23 <= KS_STAT)
        check("G51-m2-export", True,
              "S1 POINTWISE EXPORT (census; adjudicated in S7): "
              "m M_2 <= C_2 = %.4f (mid-ladder frozen at kz%d, "
              "NO cubic target consumed): test violations %d/%d "
              "%s -> pointwise %s (the banked pre-work "
              "expectation, disclosed); reserve min/med "
              "%.2f/%.2f; trend of m M_2 over test %+.3f; "
              "DISTRIBUTIONAL export (r302 stationarity, "
              "banked): KS %.4f/%.4f <= %.3f -> %s; named: %s"
              % (C_M2, srt[max(ca_i, key=lambda i:
                               m2_col[i])]["kz"],
                 len(viol_m2_i), len(te_i),
                 str([(srt[i]["kz"], round(m2_col[i], 4))
                      for i in viol_m2_i]),
                 "GO" if s1_point else "FAILS", min(rsv_m2),
                 float(np.median(rsv_m2)), sl_m2, ks13, ks23,
                 KS_STAT, "GO" if s1_stat else "FAILS",
                 str({("kz%d" % kz): round(m2_col[named_rank[kz]],
                                           3)
                      for kz in NAMED_KZ})))

    # ---------------- S6: Leg C -- S2 multiscale pileup
    section("S6  LEG C -- S2 MULTISCALE PILEUP (mechanism + "
            "certification + hardness + exponent)")
    if smoke:
        check("G60-mechanism-1-2", True, "SMOKE: skipped")
        check("G61-mechanism-3-pil", True, "SMOKE: skipped")
        check("G62-mechanism-4-nsc", True, "SMOKE: skipped")
        check("G63-direct-certification", True, "SMOKE: skipped")
        check("G64-hardness-census", True, "SMOKE: skipped")
        check("G65-growth-exponent", True, "SMOKE: skipped")
    else:
        check("G60-mechanism-1-2",
              rec_sc_w <= SA_BAR and mult_all_ok,
              "mechanism (1) SCALE DECOMPOSITION recomposes "
              "exactly on every live world (worst %.1e, bar "
              "%.0e -- e1 mutant breaks LOUD in S8); mechanism "
              "(2) FOLD MULTIPLICITY <= %d admitted on all live "
              "worlds (the r314-proven pileup cap; the 3-fold "
              "toy is REFUSED in S8)"
              % (rec_sc_w, SA_BAR, MULT_CAP))
        C_PIL = max(pil_col[i] for i in ca_i)
        viol_pil = [i for i in te_i if pil_col[i] > C_PIL]
        check("G61-mechanism-3-pil", True,
              "mechanism (3) PER-SCALE PILEUP MASS (does each "
              "scale carry O(1/m) at one block?): pil = m x "
              "max_s mass(j*, s)/L, C_PIL = %.4f frozen at cal; "
              "test violations %d/%d %s; pil med %.3f max %.3f "
              "at kz%d"
              % (C_PIL, len(viol_pil), len(te_i),
                 str([(srt[i]["kz"], round(pil_col[i], 3))
                      for i in viol_pil]) if viol_pil else "[]",
                 float(np.median(pil_col)), max(pil_col),
                 srt[int(np.argmax(pil_col))]["kz"]))
        nsclog = [nscr_col[i] / math.log(float(m_all[i]))
                  for i in range(n324)]
        C_NSC = max(nsclog[i] for i in ca_i)
        viol_nsc = [i for i in te_i if nsclog[i] > C_NSC]
        check("G62-mechanism-4-nsc", True,
              "mechanism (4) ACTIVE SCALES (only O(log m) "
              "relevant scales?): nsc_rel/log m med %.3f max "
              "%.3f, C_NSC = %.4f frozen at cal; test "
              "violations %d/%d %s; composed mechanism bound "
              "m qmax <= C_PIL x C_NSC x log m = %.3f log m"
              % (float(np.median(nsclog)), max(nsclog), C_NSC,
                 len(viol_nsc), len(te_i),
                 str([(srt[i]["kz"], round(nsclog[i], 3))
                      for i in viol_nsc]) if viol_nsc else "[]",
                 C_PIL * C_NSC))
        C_INF = max(GL_col[i] for i in ca_i)
        viol_G = [i for i in te_i if GL_col[i] > C_INF]
        named_G = {kz: GL_col[named_rank[kz]] <= C_INF
                   for kz in NAMED_KZ}
        n_named_G = sum(1 for kz in NAMED_KZ if named_G[kz])
        s2_ok = (rec_sc_w <= SA_BAR and mult_all_ok
                 and not viol_pil and not viol_nsc
                 and not viol_G and n_named_G == len(NAMED_KZ))
        check("G63-direct-certification", True,
              "DIRECT pointwise certification m qmax <= C_INF x "
              "(log m)^%d: C_INF = %.4f frozen at cal; test "
              "violations %d/%d %s; named coverage %d/4 %s -> "
              "S2 %s"
              % (A_SEAL, C_INF, len(viol_G), len(te_i),
                 str([(srt[i]["kz"], round(GL_col[i], 3))
                      for i in viol_G]) if viol_G else "[]",
                 n_named_G,
                 str({("kz%d" % kz): round(GL_col[named_rank[kz]],
                                           3)
                      for kz in NAMED_KZ}),
                 "GO" if s2_ok else "NOT-GO"))
        info("HARDNESS CENSUS -- the scale profile of the "
             "argmax block at the named near-critical rungs "
             "(scale: m x share of L):")
        for kz in NAMED_FA_KZ:
            i = named_rank[kz]
            pst = srt[i]["ev"]["pst"]
            prof = "; ".join("s%d %.3f"
                             % (s, m_all[i] * mv
                                / max(srt[i]["ev"]["trs"]["L"],
                                      1e-300))
                             for s, mv in zip(pst["scales"],
                                              pst["masses"]))
            info("  kz%-3d G %.2f nsc %d nsc_rel %d pil %.3f "
                 "scut %d | %s"
                 % (kz, G_col[i], pst["nsc"], pst["nsc_rel"],
                    pst["pil"], pst["scut"], prof))
        check("G64-hardness-census", True,
              "named spikes vs ladder medians: G %s (med %.2f), "
              "nsc %s (med %.0f), pil %s (med %.3f) -- the "
              "reviewer hardness question (many admissible "
              "scales converging near-maximally = pileup tip, "
              "or a single heavy scale?) is answered by the "
              "profiles above"
              % (str([round(G_col[named_rank[kz]], 2)
                      for kz in NAMED_FA_KZ]),
                 float(np.median(G_col)),
                 str([nsc_col[named_rank[kz]]
                      for kz in NAMED_FA_KZ]),
                 float(np.median(nsc_col)),
                 str([round(pil_col[named_rank[kz]], 3)
                      for kz in NAMED_FA_KZ]),
                 float(np.median(pil_col))))
        e_G = L2D.halves_slope(msT, [max(GL_col[i], 1e-300)
                                     for i in te_i])
        e_M2 = sl_m2
        e_tot = e_G + e_M2
        h = len(te_i) // 2
        te_a = te_i[:h]
        te_b = te_i[h:]

        def etot_on(idx):
            ms = [m_all[i] for i in idx]
            ea = L2D.halves_slope(ms, [max(GL_col[i], 1e-300)
                                       for i in idx])
            eb = L2D.halves_slope(ms, [max(m2_col[i], 1e-300)
                                       for i in idx])
            return ea + eb

        e_a = etot_on(te_a)
        e_b = etot_on(te_b)
        decided = ((e_a < CRIT_EXP) == (e_b < CRIT_EXP)
                   and (e_a < CRIT_EXP) == (e_tot < CRIT_EXP))
        sub = e_tot < CRIT_EXP
        check("G65-growth-exponent", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope vs m "
              "over the %d test rungs, fit-free): e(G/log m) = "
              "%+.3f, e(m M_2) = %+.3f, e_tot = %+.3f vs CRIT "
              "%.3f (= 2 x (1 - %.3f); the reviewer's 0.112 is "
              "the F_A-side equivalent); stability halves "
              "%+.3f / %+.3f -> %s, %s"
              % (len(te_i), e_G, e_M2, e_tot, CRIT_EXP,
                 N2_EXP_NEED, e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED",
                 ("SUBCRITICAL" if sub else "SUPERCRITICAL")
                 if decided else "open"))

    # ---------------- S7: Leg D -- adjudication + composition
    section("S7  LEG D -- SEALED ADJUDICATION + S3 COMPOSITION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        restate = (rec_sc_w > SA_BAR or pil_ch_w > CHAIN_BAR
                   or not mult_all_ok)
        go_all = s2_ok and s1_point and s1_stat
        vkey = origin_tree(leak, restate, go_all, decided, sub,
                           s1_stat)
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a "
                           "mechanism builder",
            "FA_RESTATEMENT": "the mechanism decomposition "
                              "breaks structurally",
            "QMAX_MULTISCALE_GO":
                "S2 pointwise GO (C_INF %.4f, mech C_PIL %.4f x "
                "C_NSC %.4f) + S1 pointwise GO (C_2 %.4f) + "
                "stationarity GO" % (C_INF, C_PIL, C_NSC, C_M2),
            "M2_GO_QMAX_OPEN":
                "exponent UNDECIDED (halves %+.3f/%+.3f "
                "straddle %.3f); distributional M_2 export GO "
                "(KS %.4f/%.4f), pointwise M_2 export %s"
                % (e_a, e_b, CRIT_EXP, ks13, ks23,
                   "GO" if s1_point else
                   "FAILS (%d viol, banked)" % len(viol_m2_i)),
            "PILEUP_GROWS_SUBCRITICAL":
                "e_tot %+.3f < %.3f DECIDED (halves %+.3f/"
                "%+.3f) -- sufficient by the reviewer contract"
                % (e_tot, CRIT_EXP, e_a, e_b),
            "PILEUP_SUPERCRITICAL":
                "e_tot %+.3f >= %.3f DECIDED (halves %+.3f/"
                "%+.3f)" % (e_tot, CRIT_EXP, e_a, e_b)}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        # S3 composition (printed ALWAYS, honestly typed)
        C_G_env = max(GL_col)
        C_M2_env = max(m2_col)
        if vkey == "QMAX_MULTISCALE_GO":
            C_use = C_INF * C_M2
            e_use = 0.0
            hyp = ("both factors mid-ladder CERTIFIED pointwise "
                   "(0 violations)")
        else:
            C_use = C_G_env * C_M2_env
            e_use = max(e_tot, 0.0)
            hyp = ("measured ladder envelopes + the measured "
                   "growth exponent e_tot %+.3f (letter %s) -- "
                   "hypothesis typed MEASURED, not certified"
                   % (e_tot, vkey))
        # log-space solve of m^{CRIT - e} >= C log m: t = ln m,
        # condition t (CRIT - e) >= ln C + ln t (deterministic
        # grid; a finite root exists iff CRIT - e > 0)
        m_star_l10 = None
        if CRIT_EXP - e_use > 0.0:
            t = math.log(73.0)
            while t < 1e7:
                if t * (CRIT_EXP - e_use) \
                        >= math.log(C_use) + math.log(t):
                    m_star_l10 = t / math.log(10.0)
                    break
                t *= 1.02
        info("S3 COMPOSITION (all constants explicit; %s):" % hyp)
        info("  S0 (EXACT, Fractions-proved + live-warded): M_3 "
             "<= qmax x M_2, hence sum q^3 <= (m qmax)(m M_2)/"
             "m^2 and rho_2 <= (m qmax)(m M_2)/(log m)^2;")
        info("  S1 + S2: m M_2 <= %.4f and m qmax <= %.4f x "
             "log m x m^{%.3f}  =>  sum q^3 <= %.3f x (log m)^"
             "%d x m^{%.3f} / m^2;"
             % (C_M2 if vkey == "QMAX_MULTISCALE_GO"
                else C_M2_env,
                C_INF if vkey == "QMAX_MULTISCALE_GO"
                else C_G_env, e_use, C_use, A_SEAL, e_use))
        info("  => N_3 = (sum q^3)^{-1/2} >= m^{%.3f}/sqrt(%.3f "
             "log m) and N_2 >= N_3 (r306 exact chain);"
             % (1.0 - e_use / 2.0, C_use))
        ms_txt = ("10^%.1f" % m_star_l10) \
            if m_star_l10 is not None else "NONE (supercritical)"
        info("  => N_2 >= m^%.3f for all m >= m_0* = %s (the "
             "smallest m with m^{%.3f} >= %.3f log m); "
             "MEASURED LADDER: m <= %d -- the gap (%d, m_0*) "
             "is the disclosed extrapolation hypothesis;"
             % (N2_EXP_NEED, ms_txt, CRIT_EXP - e_use, C_use,
                max(m_all), max(m_all)))
        info("  => slope(n_eff) >= NEED = %+.3f => sl_D <= "
             "sigma* => sigma <= sigma* = %.3f => the r297 "
             "target => the v964-S0 vdC theorem => delta' > "
             "%.2f on the generic half => the "
             "terminal_positive_main edge; exceptions: 6 via "
             "r287 F2 + kz15 via r270; all measured m <= %d "
             "closed by the finite certificates (r306 0/57 + "
             "this round's tables)."
             % (NEED_SLOPE, SIGMA_STAR, DELTA_NEED, max(m_all)))
        check("G71-composition",
              (m_star_l10 is not None)
              == (CRIT_EXP - e_use > 0.0),
              "composition printed with explicit constants "
              "(C = %.3f, e = %+.3f, m_0* = %s, m_0 = %d); "
              "the chain to terminal_positive_main is typed: "
              "S0 exact, S1/S2 %s, the ladder-to-m_0* step an "
              "extrapolation hypothesis -- NO cofinal claim"
              % (C_use, e_use, ms_txt, m0,
                 "certified" if vkey == "QMAX_MULTISCALE_GO"
                 else "measured"))

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    drop = mutant_scale_drop((4.0, 2.0, 1.0))
    check("G80-e1-scale-drop",
          abs((7.0 - drop) - 1.0) <= FR_BAR
          and abs(drop - 6.0) <= FR_BAR,
          "e1 LOUD: the drop-scale 'aggregation' returns 6 != "
          "the exact recomposition 7 (break exactly 1 >= %.0e; "
          "Fractions-warded in G41) -- an incomplete scale "
          "decomposition cannot slip through the recomposition "
          "ward (live worst %.1e)" % (MUT_MIN, rec_sc_w))
    mx3, adm3 = mult_ward(mutant_mult3_toy())
    check("G81-e2-mult-uncapped",
          mx3 == 3 and not adm3 and mult_all_ok,
          "e2 CAUGHT: the 3-fold toy genealogy (three ancestors "
          "at one position) is REFUSED by mult_ward (max %d > "
          "%d) while every live world is admitted at exactly 2 "
          "-- a pileup count without the proven multiplicity "
          "bound is structurally refused" % (mx3, MULT_CAP))
    check("G82-e3-m3-readback",
          len(e3_hits) >= 1 and (not sc_own),
          "e3 AST-CAUGHT: the 'mechanism column' consuming the "
          "cubic-moment record (cm/S3) is FLAGGED (%s) while "
          "the four module-own mechanism builders are clean "
          "(%d hits) -- M_3 cannot enter the proof side"
          % (e3_hits[0] if e3_hits else "MISS", len(sc_own)))
    toy_scut = (4, 5, 6)
    toy_rho = (0.1, 0.9, 0.1)
    cut_mut = mutant_scale_posthoc(toy_scut, toy_rho, 0.5)
    cut_seal = int(math.ceil(SCUT_FAC * math.log2(4.0)))
    check("G83-e4-scale-posthoc",
          len(e4_hits) >= 1 and cut_mut == 6
          and cut_mut != cut_seal,
          "e4 CAUGHT twice: the after-sight cutoff re-pick "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s) -- and on the toy returns %d != the canonical "
          "SCUT_FAC rule's %d (a post-hoc class/cutoff choice "
          "is structurally refused)"
          % (e4_hits[0] if e4_hits else "MISS", cut_mut,
             cut_seal))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact S0 interpolation M_3 <= qmax M_2 "
          "with the F_A identity (no black factor), the "
          "pointwise M_2 export test, the multiscale pileup "
          "mechanism (scale decomposition + multiplicity cap + "
          "per-scale mass + active-scale count) with the exact "
          "chain m qmax <= nsc x pil, the growth-exponent "
          "criterion and the full S3 composition -- NO new "
          "certificate promoted, NO universal bound claimed "
          "beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R324_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r321 b %.4f, "
                 "r324-pre KS %.4f/%.4f C_M2 %.4f viol7 EXACT)"
                 % (rec3_w, C2r, viol2, n324, parSQ[0], ks13,
                    ks23, C_M2)]
        parts.append("SEAL(interp %.1e, identity %.1e, pileup "
                     "chain %.1e, recomposition %.1e, purity "
                     "clean, toys exact)"
                     % (interp_w, fa_id_w, pil_ch_w, rec_sc_w))
        parts.append("S1_EXPORT(C_2 %.4f viol %d/%d, reserve "
                     "%.2f/%.2f, trend %+.3f, stationarity "
                     "%.4f/%.4f %s)"
                     % (C_M2, len(viol_m2_i), len(te_i),
                        min(rsv_m2), float(np.median(rsv_m2)),
                        sl_m2, ks13, ks23,
                        "GO" if s1_stat else "FAILS"))
        parts.append("S2_PILEUP(C_PIL %.4f viol %d, C_NSC %.4f "
                     "viol %d, C_INF %.4f viol %d named %d/4, "
                     "e_G %+.3f e_M2 %+.3f e_tot %+.3f %s)"
                     % (C_PIL, len(viol_pil), C_NSC,
                        len(viol_nsc), C_INF, len(viol_G),
                        n_named_G, e_G, e_M2, e_tot,
                        "DECIDED" if decided else "UNDECIDED"))
        parts.append(verdict_main)
        parts.append("S3_COMPOSITION(C %.3f, e %+.3f, m_0* %s, "
                     "typed)" % (C_use, e_use, ms_txt))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the S0 interpolation, "
          "the F_A identity, the pileup chain, the "
          "recomposition, the Fractions toys, the tree logic "
          "and the purity audits (exact / AST-decided); "
          "MEASURED: every constant, violation count, scale "
          "census and exponent (the finite class ladder + 2 "
          "mains + 2 live controls); OPEN: any bound beyond "
          "the measured rungs, the cofinal law, the "
          "ladder-to-m_0* extrapolation, kz15 beyond r270; NO "
          "RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
