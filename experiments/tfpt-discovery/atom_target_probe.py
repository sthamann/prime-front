#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""atom_target_probe -- PRIME.PORT.L2.ATOM_TARGET.01 (round 303):
the REGRESS AUDIT of the L2 reduction cascade plus the FIRST
non-tautological mechanism test.  The r300/r301/r302 cascade froze
three target inequalities with the SAME measured margin 0.055:
NEFF_TARGET (slope(n_eff) >= +0.908, measured +0.963), UNIF_TARGET
(slope(1 + CV^2) <= +0.094, measured +0.039), ATOM_TARGET
(slope(n_eff_atom) >= +0.888, measured +0.942).  Three identical
margins are the signature of a chain of EXACT reparametrizations:
this round must adjudicate it.  Context (sealed record inputs):
r297 (SPEC e42a76eb) froze sigma <= sigma* = -0.516; r299 froze
sl_D <= sigma* (measured -0.571, margin 0.055 -- the FIRST
appearance of the number); r300 (SPEC 55218b5d) proved sl_D = 2
sl_L1 - sl_neff exact and settled the ratio half structurally;
r301 (SPEC 6f8cc404) proved n_eff = n_act/(1 + CV^2) exactly with
the count link n_act == m on 42/42; r302 (SPEC 36df9424, 30/30)
proved the coherence identity 1 + CV^2 = n_act chi/(surv^2
n_eff_atom) exactly (<= 6.0e-16 on 47 worlds), fired UNIF_DERIVED
(first DERIVED of the lane, all hypotheses typed MEASURED), found
PROFILE_STATIONARY (KS(G1,G3) 0.043, 1/N transient onto m2_inf =
1.973, held-out 0.002) and the lag-1 decorrelation rho_1 = -0.222
of the dc profile with chi = 0.63 DESTRUCTIVE and falling.  kz15
permanently closed via r270; the 6 exceptions via the r287 F2
certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE TWO QUESTIONS (both mandatory, sealed order):
(Q1, Leg A FIRST) is ATOM_TARGET an exact reparametrization of
the r297-adjacent sl_D statement -- i.e. is the 0.055 margin ONE
algebraic number on all levels?  (Q2, Leg B) does the atom-level
anti-concentration (equivalently the ONE core slack) FOLLOW from
the lag-1 mixing structure of the recursion -- as a statement
falsifiable on sealed synthetic controls?

THE OBJECT (r269/r287/r297-r302 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks (r270 convention); FROZEN vdC window H = max(2,
ceil(sqrt(m))); the frozen positional block machinery (r298
WBT.block_breaks + WBT.aggregate_blocks), the r299
FDP.overlap_split + FDP.cconv_census, the r300 DTP.participation
+ DTP.shared_delta, the r301 NTP.quasi_uniformity +
NTP.dc_profile and the r302 UTP.coherence_split +
UTP.lagk_profile + UTP.ks_two + UTP.fs_solve (audited in r302),
ALL imported verbatim; PDelta = Pbeta - Pomega; the round's
central objects are (Q1) the MARGIN CHAIN of the four
identity-linked levels and (Q2) the dc profile on the shared bulk
support with its lag-1 autocorrelation rho_1.

LEG 0 -- ANCHOR REGRESSION (r297/r300/r301/r302 record numbers
adopted as-is, disclosed): sigma -0.714, sigma* -0.516, sl_c2
+0.196, sl_pref +0.489 (tol 0.01); sl_D -0.571 (r299, tol 0.01);
n_eff med 37.41 (tol 0.05) sl_neff +0.963, sl_L1 +0.196, NEED
+0.908; n_act med 73.0 (tol 0.5) sl_nact +1.002, COUNT LINK
n_act == m on 42/42 EXACT, CV^2 med 1.03 (tol 0.02) sl_cv2p
+0.039, UNIF_NEED +0.094; n_eff_atom med 118.0 (tol 1.0)
sl_natom +0.942, ATOM_NEED +0.888; surv med 0.44 (tol 0.02) sl
-0.020; chi med 0.630 (tol 0.02) sl_chi -0.060; rho_1/2/3 med
-0.222/-0.140/+0.089 (tol 0.01); stationarity KS(G1,G3) 0.043 /
KS(G2,G3) 0.021 (tol 0.01); 1/N transient A = 1.973 (tol 0.01),
held-out dev 0.002 (<= 0.05); the THREE margins 0.055 each (tol
0.01, live recomputation).

LEG A -- THE REGRESS AUDIT (Q1, first and sealed):
(A1) EXACT SLACK PROPAGATION (module-own margin_chain, re-proved
  in exact Fractions on a rational slope set): with NEED = 2
  sl_L1 - sigma*, UNIF_NEED = sl_nact - NEED, ATOM_NEED = sl_nact
  + sl_chi - 2 sl_surv - UNIF_NEED, the four target margins
    m_D    = sigma* - sl_D
    m_NEFF = sl_neff - NEED
    m_UNIF = UNIF_NEED - sl_cv2p
    m_ATOM = sl_natom - ATOM_NEED
  are pairwise equal EXACTLY given the three gated identities
  (r300: sl_D = 2 sl_L1 - sl_neff; r301: sl_neff = sl_nact -
  sl_cv2p; r302: sl_cv2p = sl_nact + sl_chi - 2 sl_surv -
  sl_natom), because the frozen halves_slope estimator is exactly
  log-additive over per-rung product identities.  Live wards on
  the 42-rung ladder: dN = |m_NEFF - m_D|, dU = |m_UNIF -
  m_NEFF|, dB = |m_UNIF(block) - m_UNIF(shared)| (the qu == co
  bridge), dA = |m_ATOM - m_UNIF(shared)|, ALL <= PROP_BAR =
  1e-9.  SEALED VERDICT: REGRESS_CONFIRMED(slack-invariant) iff
  dN, dU, dB, dA <= PROP_BAR (the cascade is ONE measured number
  S = sigma* - sl_D rewritten three times); LEVELS_INDEPENDENT
  (devs printed) otherwise.  DISCLOSED PRIOR: CONFIRMED is the
  expected outcome (the three identities are r300-r302 gated
  algebra); the sealed rule is symmetric.
(A2) THE SIGMA-LEVEL SURPLUS + THE 1/2-CONJECTURE: the r297
  slack sigma* - sigma (record +0.198) is NOT the core slack;
  the audit prints the exact decomposition sigma* - sigma =
  (sigma* - sl_D) + (sl_D - sigma) with the measured ratio
  surplus sl_D - sigma (record +0.143: slope(S_F/D) falls; only
  BOUNDEDNESS of it is structural, r300 RATIO_BOUNDED).  The
  round-charter conjecture "sigma - sigma* = -0.198 in sigma
  units => 0.055 in slope units by a 1/2 conversion" is
  adjudicated numerically and algebraically: HALF_CONJ_HOLDS iff
  |(sigma* - sigma)/2 - m_D| <= 0.005, else HALF_CONJ_REFUTED
  (the correct identity is m_D = sigma* - sl_D; no 1/2
  conversion exists in the chain -- the factor 2 lives ONLY in
  NEED = 2 sl_L1 - sigma* and cancels exactly in every margin
  difference).
(A3) CORE NAMING + PROOF-LEVEL ADJUDICATION (sealed rule): on
  CONFIRMED the core is the ONE number S = sigma* - sl_D and the
  cascade is an exact DICTIONARY; the natural proof level is
  adjudicated AFTER Leg B by the sealed rule: ATOM iff
  MIXING_SUFFICIENT (the only level with a validated,
  falsifiable mechanism); UNIF/A2 (the stationary-profile level)
  iff MIXING_IRRELEVANT (the marginal alone carries); ATOM with
  the missing ingredient disclosed iff MIXING_INSUFFICIENT (the
  level with the most falsification-tested structure).  Printed
  as an ADJUDICATION, typed -- no level is claimed provable.
  CONFIRMED is NOT a setback: the dictionary content of the
  levels (count link, stationarity, coherence identity, chi
  destructive, lag-1 mixing) stands; but further "reduction"
  rounds may NOT be counted as progress on the inequality.

LEG B -- THE MIXING MECHANISM TEST (Q2, sealed synthetic
control family on the dc profile, per rung, same block
structure): three families of marginal-preserving rearrangements
of the bulk dc values (the multiset is EXACTLY preserved: a
permutation), lag-1 autocorrelation steered by seeded greedy
pairwise swaps (module-own swap_arrange, O(1) local update,
deterministic restarts):
  (a) RHO_MATCH: target rho_1 = the rung's measured rho_1;
  (b) RHO_ZERO:  target rho_1 = 0 (independence surrogate);
  (c) RHO_FLIP:  target rho_1 = -(the rung's measured rho_1)
      (sign flipped, per rung -- positive on the typical rung).
R_REP = 8 replicates per family with sealed seeds seed =
SEED_BASE + rung_index x 100 + family x 10 + replicate
(SEED_BASE 303000; collision-free by construction, gated).
CONSTRUCTION WARDS (every build): sorted-multiset equality
BITWISE (np.sort equality -- the marginal is exact); rho_1
within RHO_TOL = 0.01 of target (convergence share >= CONV_MIN =
0.95 over all builds); non-triviality for family (a): permutation
fixed-point share <= FIX_MAX = 0.2 (the search must NOT return
the original arrangement); n_eff_atom invariance <= NA_INV_BAR =
1e-12 rel (DISCLOSED ALGEBRAIC FACT, discovered in this audit:
n_eff_atom = L1a^2/Q is a pure MARGINAL functional -- every
family reproduces sl_natom EXACTLY; the mixing structure cannot
move it; the discriminating quantities are chi, CV^2 and D).
MEASUREMENT per replicate (the whole 42-rung ladder, the real
brk/m block structure): chi med, sl_cv2p (shared), sl_D (shared
block energy), sl_natom (ward), and the sigma-end quantity
margin_syn = sigma* - sl_D_syn (by Leg A this IS the propagated
end margin -- all levels give the same number).  Family value =
median over the 8 replicates (min/max printed).
SEALED REPRODUCTION RULE: family F reproduces MAIN iff
|chi_med_F - chi_med| <= CHI_BAND = 0.05 AND |sl_cv2p_F -
sl_cv2p| <= SLP_BAND = 0.02 AND |sl_D_F - sl_D| <= SLP_BAND;
family F clearly misses iff at least one of the three exceeds
MISS_F x its band (MISS_F = 2.0).  SEALED ADJUDICATION (exactly
one fires): MIXING_SUFFICIENT iff (a) reproduces AND (b) clearly
misses AND (c) clearly misses -- then the lag-1 structure IS the
mechanism and the proof obligation becomes rho_1 <= 0 (+
stationary marginal) => slack > 0; MIXING_IRRELEVANT iff (a),
(b), (c) ALL reproduce -- the marginal alone carries;
MIXING_INSUFFICIENT(what is missing) otherwise -- named per
family x quantity.  DISCLOSED PRIORS (algebraic, no scratch
run): under (b) the block energy loses the negative lag-1 cross
terms, so chi is expected NEAR 1 (vs 0.63 destructive) and the
end margin is expected to SHRINK toward 0 (sl_D_syn ~ slope(Q)
= sl_D - sl_chi ~ -0.511 if chi flattens); under (c) chi > 1
constructive; whether (a) reproduces the SLOPES (not just the
chi level) is genuinely open -- rho_1 matching does not fix
higher lags; the outcomes are sealed symmetrically.
THE CONNECTION TEST (S6, measured regardless of the verdict,
adjudicated only as a census): per-rung sign of the exact lag-1
numerator S1 = sum zc_i zc_{i+1} (count of rungs with S1 < 0,
tag RHO1_NEG_UNIFORM iff 42/42), the mean-removed sign
alternation fraction (med), and on the TWO smallest rungs the
Fractions-EXACT recomputation of S1 (Fraction arithmetic on the
float dc values: the sign statement is exact-finite).  The
derivation of rho_1 <= 0 from the three-term recursion
(adjacent-pi orthogonality forcing residue sign alternation)
stays OPEN -- this census verifies the sign exactly on the
finite windows, nothing more.

LEG C -- CONSEQUENCE ADJUDICATION (sealed map, printed after A x
B): (i) REGRESS_CONFIRMED + MIXING_SUFFICIENT => the core of the
generic L2 half is "rho_1 <= 0 + marginal stationarity => slack
> 0" -- the most precise form ever reached; formulated as THE
one target (a proof attempt on this level, NOT another reduction
round); (ii) REGRESS_CONFIRMED + MIXING_INSUFFICIENT => the core
stays empirical, the cascade is CLOSED as a dictionary, the
honest state documented (which ingredient the synthetic test
showed missing); (iii) REGRESS_CONFIRMED + MIXING_IRRELEVANT =>
the mechanism is pure distribution stationarity (the r302 A2
level), the mixing trace is bycatch; (iv) LEVELS_INDEPENDENT =>
ATOM_TARGET continues as a normal open target (derivation routes
documented).

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) SLACK PROPAGATION WITH WRONG 1/2-FACTOR (exact Fractions,
  module-own): on the rational slope set sigma* = -1/2, sl_L1 =
  1/5, sl_neff = 24/25 (=> sl_D = -14/25), sl_nact = 1 (=>
  sl_cv2p = 1/25), sl_chi = -1/20, sl_surv = -1/50 (=> sl_natom
  = 19/20): ALL four margins equal 3/50 EXACT, devs 0; the
  mutant NEED' = 1 x sl_L1 - sigma* (the halved mass exponent)
  breaks the D<->NEFF invariance by EXACTLY sl_L1 = 1/5 --
  CAUGHT: the factor 2 on the mass slope is load-bearing;
(m2) UNMATCHED-MARGINAL SYNTHETIC FAMILY: a "family" built from
  the constant-|value| two-sign profile with the same L1a must
  break the construction LOUDLY: the sorted-multiset ward fails
  AND the atom energy deviates rel >= MUT_MIN (real n_eff_atom
  != n); the marginal ward is load-bearing;
(m3) REPLICATE-SEED COLLISION: two (b)-replicates built with the
  SAME seed produce the identical arrangement -- CAUGHT by the
  pairwise-distinct ward (identical permutation detected); the
  legitimate replicate set is pairwise distinct (gated);
(m4) CHI IDENTITY WITH SWAPPED D/Q (exact Fractions, module-own):
  on the signed toy dc = (1, -2 | 3): chi = D/Q = 5/7, identity
  dev 0 EXACT; the mutant chi' = Q/D = 7/5 breaks the coherence
  identity by 48/35 EXACT -- CAUGHT: the orientation of the
  coherence ratio is load-bearing;
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key AND a builder consuming the branch
  label are both FLAGGED by the AST scope audit.  Scope hygiene:
  the new builders (margin_chain, rho1_stat, swap_arrange,
  alt_census) consume slope numbers / profile values / positions
  only (BOUND_FORBIDDEN set); fragment audit (no fit
  primitives; the swap search is a deterministic seeded greedy
  descent, disclosed).  TOY EXACTNESS (bar 1e-14): margin_chain
  float == Fractions on the m1 slope set; rho1_stat on (1, -1,
  1, -1) == -3/4 EXACT and on the sorted arrangement (-1, -1,
  1, 1) == +1/4 EXACT (Fractions re-proof module-own);
  swap_arrange on the 4-toy hits the achievable target -3/4
  exactly (multiset preserved bitwise); the coherence toy
  values (CV^2 1/4, chi 5/7, surv 2/3, n_eff_atom 18/7) as in
  r302; mp SAMPLES (dps 60): kz15 (bar 1e-8) + the two deepest
  rungs (bar 3e-6); the DEGENERATE-SOURCE GUARD declared IN
  ADVANCE (r300-a1/r301/r302 convention): on a source with
  Delta == 0 identically (self-aliased SMOOTH) the
  shared-support mass W degenerates to float noise; every
  shared-support ward is skipped exactly when W <= 1e-6 x the
  total contribution mass, disclosed per world.

INDEX FIREWALL (binding, r238-r302 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks, r299 FDP.overlap_split +
FDP.cconv_census, r300 DTP.participation + DTP.shared_delta,
r301 NTP.quasi_uniformity + NTP.dc_profile, r302
UTP.coherence_split + UTP.lagk_profile + UTP.ks_two +
UTP.fs_solve + UTP.var_decomp, r269 PBB.mask_edge +
PBB.runs_split + PBB.bound_pairsum + PBB.mp_drive, r287
L2D.blocks_level2 + L2D.bound_vdc + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack + BH.spearman, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN);
PROP_BAR 1e-9 (margin-chain invariance, live); HALF_CONJ_TOL
0.005; QID_BAR 1e-9; CO_BAR 1e-9; CSK_BAR 1e-9; ADD_BAR 1e-9;
EQ_BAR 1e-9; NA_BAR 1e-12; NA_INV_BAR 1e-12; RHO_CONS_BAR 1e-12
(rho1_stat == lagk_profile consistency); DEG_FLOOR 1e-6;
REC_FLOOR 1e-6; R_REP 8; SEED_BASE 303000; RHO_TOL 0.01;
SWAP_F 40; SWAP_CAP 60000; CONV_MIN 0.95; FIX_MAX 0.2;
CHI_BAND 0.05; SLP_BAND 0.02; MISS_F 2.0; K_LAG 8; N_GRP 14;
KS_STAT 0.125; FS_BAR 0.05; TOY_BAR 1e-14; MUT_MIN 1e-6;
TB_WARD bars 1e-9 / 3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR 1e-9;
R297 anchors sigma -0.714 / sigma* -0.516 / sl_c2 +0.196 /
sl_pref +0.489 (tol 0.01); R299 sl_D -0.571 (tol 0.01); R300
anchors n_eff 37.41 (0.05) / sl_neff +0.963 / sl_L1 +0.196 (tol
0.01); R301 anchors n_act 73.0 (0.5) / sl_nact +1.002 / cv2 1.03
(0.02) / sl_cv2p +0.039 / natom 118.0 (1.0) / sl_natom +0.942 /
surv 0.44 (0.02) / sl_surv -0.020 (tol 0.01); R302 anchors chi
0.630 (0.02) / sl_chi -0.060 (0.01) / rho1/2/3
-0.222/-0.140/+0.089 (0.01) / KS13 0.043 / KS23 0.021 (0.01) /
A_fs 1.973 (0.01) / fs_dev <= 0.05 / UNIF_NEED +0.094 /
ATOM_NEED +0.888 (0.01); MARGIN_REF 0.055 (tol 0.01, all four
levels); MP_DPS 60; MP_T_BAR 1e-8; MP_DEEP_BAR 3e-6; KZ_ANCHOR
15; runtime <= 1800 s; smoke = w9 + controls + Fractions section
+ toys + scope audits + every exact ward at w9 + ONE synthetic
build (family b, replicate 0, w9) + the m2/m3 mutants (ladder,
slopes, families, adjudications, censuses, mp wards skipped).
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r297-r302 RECORD number adopted as-is;
the margin-chain algebra, the n_eff_atom marginal-invariance
fact, the sigma-surplus decomposition and the family priors
(chi -> ~1 under (b), chi > 1 under (c), sl_D_syn ~ -0.511 if
chi flattens) are derived algebra, disclosed above; the
adjudication outcomes are sealed symmetrically -- the priors
make REGRESS_CONFIRMED near-certain (gated identities) and the
Leg-B outcome genuinely open between SUFFICIENT and
INSUFFICIENT; no rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  MARGIN_CHAIN(m_D/m_NEFF/m_UNIF/m_ATOM + devs dN/dU/dB/dA)
+ [exactly one of] REGRESS_CONFIRMED(S = sigma* - sl_D; the
    sigma-level surplus decomposition; HALF_CONJ verdict) /
    LEVELS_INDEPENDENT(devs)
+ MIXING_TABLE(three families x chi med / sl_cv2p / sl_D /
    margin_syn, replicate min..max; natom-invariance ward)
+ [exactly one of] MIXING_SUFFICIENT / MIXING_INSUFFICIENT(
    family x quantity misses) / MIXING_IRRELEVANT
+ RHO_SIGN(n_neg/42, alternation med, Fractions signs on the two
    smallest rungs)
+ CORE_LEVEL(adjudicated proof level + reason, typed)
+ CONSEQUENCE_MAP(one of (i)-(iv), the honest map printed)
+ [if a control class differs] WORLD_NOTE(disclosed).
Honesty before beauty: the margin-chain invariance and the
marginal-invariance of n_eff_atom are EXACT finite statements;
every slope, med, band comparison and census is MEASURED on 42
rungs and 8 seeded replicates only; the synthetic families
falsify or fail to falsify a MECHANISM CANDIDATE -- no verdict
claims a derivation of rho_1 <= 0, no verdict claims a cofinal
law; the exception scalar's positivity beyond the measured 42
stays OPEN; r243-r302 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 26/26 (0.2 s, no defect); calibration pass 1 =
first full evaluation, 26/26 gates, wall 51.2 s, NO amendment
(the pre-declared DEG_FLOOR guard fired exactly on the known
degenerate SMOOTH world, as sealed; every construction ward held:
convergence 1008/1008, worst |rho1 - target| 1.00e-2 at the tol,
family-(a) fixed points max 0.024, marginal sorted-bitwise on all
1008 builds, seeds collision-free); record run1/run2 after this
insertion, identical up to WALL; the only post-freeze edit is
this record-table insertion, which IS the protocol):
CAL_VERDICT = MARGIN_CHAIN(m_D +0.0547 / m_NEFF +0.0547 / m_UNIF
+0.0547 (blk) +0.0547 (sh) / m_ATOM +0.0547; invariance devs dN
6.7e-16 / dU 8.7e-16 / dB 0.0 / dA 5.4e-16 -- the 0.055 of
r299/r300/r301/r302 is ONE number to float precision) +
REGRESS_CONFIRMED(S = sigma* - sl_D = -0.516 - (-0.571) =
+0.0547, i.e. the r299 DIAG margin; sigma-level decomposition
sigma* - sigma = +0.1976 = S +0.0547 + ratio surplus (sl_D -
sigma) +0.1429 EXACT -- the r297 sigma slack is NOT the core: it
carries the extra measured S_F/D decay, of which only
BOUNDEDNESS is structural (r300); HALF_CONJ REFUTED: (sigma* -
sigma)/2 = +0.0988 vs m_D +0.0547, dev 0.0441 >> 0.005 -- the
charter's 1/2-conversion does NOT exist; the factor 2 lives only
in NEED = 2 sl_L1 - sigma* and cancels exactly in every margin
difference) + MIXING_TABLE(real chi 0.630 sl_cv2p +0.039 sl_D
-0.571 margin +0.055 | (a) RHO_MATCH chi 0.764 [0.726, 0.788]
sl_cv2p +0.059 [+0.016, +0.094] sl_D -0.574 [-0.640, -0.528]
margin +0.057 -- the SLOPES and the end margin REPRODUCE, the
chi LEVEL does not | (b) RHO_ZERO chi 1.029 [1.003, 1.068]
sl_cv2p +0.049 sl_D -0.549 margin +0.032 -- the interference
gone, the margin shrinks | (c) RHO_FLIP chi 1.342 [1.285, 1.414]
sl_cv2p +0.041 sl_D -0.472 margin -0.044 NEGATIVE: the
flipped-mixing world FAILS the target inequality; natom
invariance worst 1.0e-15: sl_natom +0.942 on every family by
algebra -- ATOM_TARGET's growth statement is a pure MARGINAL
functional) + MIXING_INSUFFICIENT((a) misses chi by 0.134 >
0.05; (b) misses chi by 0.399 and sl_D by 0.022; (c) misses chi
by 0.713 and sl_D by 0.099 -- the mechanism ladder is MONOTONE
in rho_1 (chi 0.63 real -> 0.76 matched -> 1.03 zero -> 1.34
flipped; margin +0.055 -> +0.057 -> +0.032 -> -0.044): the
negative lag-1 mixing is directionally REAL and the sign flip
KILLS the inequality, but rho_1 alone does not reproduce the
destructive coherence LEVEL -- the within-block higher-lag
structure carries the rest) + RHO_SIGN(RHO1_SIGN_MIXED: S1 < 0
on 41/42 rungs (NOT uniform -- one rung positive, honest),
alternation med 0.523, Fractions-EXACT negative on the two
smallest rungs kz18 (N 142) S1 = -0.00517079 and kz23 (N 149)
S1 = -0.00108151) + CORE_LEVEL(ATOM, per the sealed INSUFFICIENT
clause: the level with the most falsification-tested structure
-- rho_1 < 0 on 41/42 with two exact-finite certificates, chi
destructive with CS cap, marginal stationary; the missing
ingredient NAMED: the within-block coherence beyond lag 1) +
CONSEQUENCE_MAP((ii) REGRESS_CONFIRMED + MIXING_INSUFFICIENT:
the cascade r297->r302 is CLOSED as an exact dictionary with ONE
measured core S = sigma* - sl_D = +0.0547; further reduction
rounds may NOT be counted as progress on the inequality; the
honest new object is the NAMED mechanism gap -- the full
short-range structure of the dc profile (the joint rho_1..rho_k
/ within-block law), not another coordinate change) +
WORLD_NOTE(the coherence identity holds on the controls by
algebra; EPST chi 0.18 rho1 -0.34 / SCR chi 1.26 rho1 -0.05
bracket MAIN 0.63 as in r302; DEG guard fired on SMOOTH only,
pre-declared).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; identity wards on 47 worlds: count 6.8e-16,
coherence 6.0e-16, CS slack 0.0, P_shared == P_ov 6.1e-16, CV^2
equality 8.1e-16, natom internal 4.9e-16, dc == dw x f 2.6e-15,
rho1_stat == lagk 1.1e-16; r297 anchors bit-near (sigma -0.714,
sigma* -0.516, sl_c2 +0.196, sl_pref +0.489); sl_D -0.571 (r299
bit-near); r300/r301 anchors bit-near (n_eff 37.41 / +0.963,
sl_L1 +0.196, NEED +0.908; n_act 73.0 / +1.002 link 42/42 with
co == qu EXACT, cv2 1.03 / +0.039 blk == sh, natom 118.0 /
+0.942, surv 0.44 / -0.020); r302 anchors bit-near (chi 0.630 /
-0.060, rho -0.222/-0.140/+0.089, KS13/23 0.043/0.021, A_fs
1.973 dev 0.002, UNIF_NEED +0.094, ATOM_NEED +0.888).  S3:
Fractions margin chain 3/50 x 4 devs 0, m1 break 1/5 == sl_L1
EXACT; coherence identity dev 0 (chi 5/7), m4 swapped-D/Q break
48/35 EXACT (chi' 7/5); rho1 toys -3/4 / +1/4 EXACT (float ==
Fractions, worst dev 0.0); swap toy hits -3/4 with the multiset
bitwise; margin_chain float == Fractions worst 1.1e-16.  S5: m2
unmatched marginal: sorted ward BREAKS + atom energy dev 5.9e-1
LOUD (real natom 47.1 != n 116 at w9); m3 same-seed arrangements
identical -- CAUGHT, distinct seeds differ.  S8: mp wards kz15
2.9e-10, kz64 9.3e-9, kz52 6.6e-8.
READING (typed, no upgrade): the round ADJUDICATES the cascade
honestly: (1) REGRESS_CONFIRMED -- the three frozen targets
NEFF/UNIF/ATOM and the r299 DIAG statement share ONE algebraic
slack S = sigma* - sl_D = +0.0547 (invariance devs <= 9e-16):
r300->r302 built an exact DICTIONARY around one measured
statement, not three reductions; the structure gains of the
levels (count link, stationarity, coherence identity, chi
destructive, lag-1 trace) STAND, but no further reduction round
may be counted as progress on the inequality; the r297 sigma
level is NOT the core (its 0.198 slack carries the +0.143 ratio
surplus) and the charter's 1/2-conversion is REFUTED (0.099 !=
0.055); (2) the FIRST non-tautological mechanism test of the
lane delivers a DIRECTIONAL positive and an honest negative: the
mechanism ladder is monotone in rho_1 -- flipping the mixing
sign kills the inequality (margin -0.044), removing it shrinks
the margin to +0.032, matching it reproduces the slopes and the
margin (+0.057 vs +0.055) -- but the destructive coherence LEVEL
chi = 0.63 needs MORE than rho_1 (matched family sits at 0.76):
MIXING_INSUFFICIENT, the missing ingredient is the within-block
structure beyond lag 1; (3) n_eff_atom is a pure MARGINAL
functional (invariance 1.0e-15 on all 1008 builds): ATOM_TARGET's
growth is carried by the value distribution alone, the mixing
lives in chi/CV^2/D -- the r302 A2 stationarity and the mixing
are COMPLEMENTARY, not redundant; (4) the rho-sign census is
NOT uniform (41/42, one rung positive) -- the connection
"adjacent-pi orthogonality forces rho_1 <= 0" cannot be a
per-rung theorem in this raw form; the two smallest rungs carry
exact-finite negative certificates.  CONSEQUENCE ((ii)): the
reduction cascade is CLOSED as a dictionary; the honest next
object is the joint short-range law of the dc profile
(rho_1..rho_k / within-block coherence), not another coordinate.
Runtime 51.2 s full / 0.2 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (record-table insertion per
protocol; no bar, band, rule or verdict rule moved).

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
import fejer_decay_probe as FDP                # noqa: E402 r299
import diag_target_probe as DTP                # noqa: E402 r300
import neff_target_probe as NTP                # noqa: E402 r301
import unif_target_probe as UTP                # noqa: E402 r302
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
QID_BAR = 1e-9
CO_BAR = 1e-9
CSK_BAR = 1e-9
ADD_BAR = 1e-9
EQ_BAR = 1e-9
NA_BAR = 1e-12
PROP_BAR = 1e-9
HALF_CONJ_TOL = 0.005
NA_INV_BAR = 1e-12
RHO_CONS_BAR = 1e-12
DEG_FLOOR = 1e-6
REC_FLOOR = 1e-6
R_REP = 8
SEED_BASE = 303000
RHO_TOL = 0.01
SWAP_F = 40
SWAP_CAP = 60000
CONV_MIN = 0.95
FIX_MAX = 0.2
CHI_BAND = 0.05
SLP_BAND = 0.02
MISS_F = 2.0
K_LAG = 8
N_GRP = 14
KS_STAT = 0.125
FS_BAR = 0.05
TOY_BAR = 1e-14
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
R297_SIGMA = -0.714
R297_SIGMA_STAR = -0.516
R297_SL_C2 = 0.196
R297_SL_PREF = 0.489
R297_TOL = 0.01
R299_SL_D = -0.571
R299_SL_D_TOL = 0.01
R300_NEFF_MED = 37.41
R300_NEFF_TOL = 0.05
R300_SL_NEFF = 0.963
R300_SL_L1 = 0.196
R300_SL_TOL = 0.01
R301_NACT_MED = 73.0
R301_NACT_TOL = 0.5
R301_SL_NACT = 1.002
R301_CV2_MED = 1.03
R301_CV2_TOL = 0.02
R301_SL_CV2P = 0.039
R301_NATOM_MED = 118.0
R301_NATOM_TOL = 1.0
R301_SL_NATOM = 0.942
R301_SURV_MED = 0.44
R301_SURV_TOL = 0.02
R301_SL_SURV = -0.020
R301_SL_TOL = 0.01
R302_CHI_MED = 0.630
R302_CHI_TOL = 0.02
R302_SL_CHI = -0.060
R302_RHO = (-0.222, -0.140, 0.089)
R302_RHO_TOL = 0.01
R302_KS13 = 0.043
R302_KS23 = 0.021
R302_KS_TOL = 0.01
R302_A_FS = 1.973
R302_A_TOL = 0.01
R302_UNIF_NEED = 0.094
R302_ATOM_NEED = 0.888
R302_NEED_TOL = 0.01
MARGIN_REF = 0.055
MARGIN_TOL = 0.01
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
KZ_ANCHOR = 15

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


# ---------------- the module-own Leg A / Leg B builders.
# ---------------- Source-pure: slope numbers, profile values and
# ---------------- positions only; the withheld terminal drive key,
# ---------------- the branch label and every target-side identifier
# ---------------- are forbidden in scope (AST audit).
def margin_chain(s_star, slD, slL1, slneff, slnact, slcv2b,
                 slcv2s, slchi, slsurv, slnatom, l1_fac=2):
    """the Leg A slack propagation: the four target margins of the
    identity-linked levels expressed in the measured base slopes
    (works on floats AND exact Fractions).  l1_fac = 1 is the m1
    wrong-1/2-factor mutant (the halved mass exponent in NEED)."""
    nd = l1_fac * slL1 - s_star
    mD = s_star - slD
    mN = slneff - nd
    und = slnact - nd
    mU = und - slcv2b
    mUs = und - slcv2s
    a_nd = slnact + slchi - 2 * slsurv - und
    mA = slnatom - a_nd
    return dict(nd=nd, und=und, a_nd=a_nd, mD=mD, mN=mN, mU=mU,
                mUs=mUs, mA=mA, dN=abs(mN - mD), dU=abs(mU - mN),
                dB=abs(mUs - mU), dA=abs(mA - mUs))


def rho1_stat(z):
    """the centered lag-1 autocorrelation of a profile in position
    order: (rho1, S1, A0) with S1 = sum zc_i zc_{i+1} and A0 =
    sum zc_i^2; the mean and A0 are PERMUTATION-INVARIANT -- only
    S1 moves under rearrangement."""
    z = np.asarray(z, dtype=float)
    n = len(z)
    if n < 2:
        return 0.0, 0.0, 0.0
    zc = z - float(np.mean(z))
    A0 = float(np.dot(zc, zc))
    if A0 <= 0.0:
        return 0.0, 0.0, A0
    S1 = float(np.dot(zc[:-1], zc[1:]))
    return S1 / A0, S1, A0


def swap_arrange(z, target, seed, cap):
    """the sealed marginal-preserving construction: a permutation
    of the profile values with the lag-1 autocorrelation steered
    to the target by seeded greedy pairwise swaps (O(1) local
    update of S1, strict improvement, deterministic restarts
    after 5n non-improving attempts; the best arrangement is
    kept).  Returns (values in arrangement order, permutation,
    rho1, attempts used, converged)."""
    z = np.asarray(z, dtype=float)
    n = len(z)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    zc_full = z - float(np.mean(z))
    A0 = float(np.dot(zc_full, zc_full))
    if n < 4 or A0 <= 0.0:
        return z[perm], perm, 0.0, 0, True
    y = zc_full[perm].copy()
    S = float(np.dot(y[:-1], y[1:]))
    S_t = target * A0
    tol_abs = RHO_TOL * A0
    best_perm = perm.copy()
    best_err = abs(S - S_t)
    pairs = rng.integers(0, n, size=(int(cap), 2))
    since = 0
    att = 0
    for p, q in pairs:
        att += 1
        if best_err <= tol_abs:
            break
        if p == q:
            continue
        if p > q:
            p, q = q, p
        idx = set()
        for i in (p - 1, p, q - 1, q):
            if 0 <= i < n - 1:
                idx.add(i)
        old = sum(y[i] * y[i + 1] for i in idx)
        y[p], y[q] = y[q], y[p]
        new = sum(y[i] * y[i + 1] for i in idx)
        S2 = S + (new - old)
        if abs(S2 - S_t) < abs(S - S_t):
            S = S2
            perm[p], perm[q] = perm[q], perm[p]
            if abs(S - S_t) < best_err:
                best_err = abs(S - S_t)
                best_perm = perm.copy()
            since = 0
        else:
            y[p], y[q] = y[q], y[p]
            since += 1
            if since >= 5 * n:
                perm = rng.permutation(n)
                y = zc_full[perm].copy()
                S = float(np.dot(y[:-1], y[1:]))
                if abs(S - S_t) < best_err:
                    best_err = abs(S - S_t)
                    best_perm = perm.copy()
                since = 0
    yb = zc_full[best_perm]
    Sb = float(np.dot(yb[:-1], yb[1:]))
    r1 = Sb / A0
    return (z[best_perm], best_perm, r1, att,
            abs(r1 - target) <= RHO_TOL)


def alt_census(z):
    """the mean-removed sign-alternation census of a bulk profile:
    fraction of adjacent pairs (both signs nonzero) with opposite
    signs."""
    z = np.asarray(z, dtype=float)
    if len(z) < 2:
        return 0.0
    zc = z - float(np.mean(z))
    sg = np.sign(zc)
    a = sg[:-1]
    b = sg[1:]
    ok = (a != 0) & (b != 0)
    if not np.any(ok):
        return 0.0
    return float(np.mean((a[ok] * b[ok]) < 0))


def mutant_gift_bound(rc, vals):
    """m5a MUST-FAIL MUTANT: a 'mixing target' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * rho1_stat(vals)[0]


def mutant_branch_peek(rc, vals):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'profile statistic' that consumes the branch label to pick
    its constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * alt_census(vals)


# ---------------- exact Fractions section
FR_SLOPES = dict(s_star=Fr(-1, 2), slL1=Fr(1, 5), slneff=Fr(24, 25),
                 slnact=Fr(1), slchi=Fr(-1, 20), slsurv=Fr(-1, 50))


def fr_margin_chain(l1_fac=2):
    """the m1 Fractions re-proof: on the rational slope set the
    derived slopes are sl_D = 2 sl_L1 - sl_neff = -14/25, sl_cv2p
    = sl_nact - sl_neff = 1/25, sl_natom = sl_nact + sl_chi - 2
    sl_surv - sl_cv2p = 19/20; all four margins equal 3/50 EXACT;
    the l1_fac = 1 mutant breaks the D<->NEFF invariance by
    EXACTLY sl_L1 = 1/5."""
    f = FR_SLOPES
    slD = 2 * f["slL1"] - f["slneff"]
    slcv2 = f["slnact"] - f["slneff"]
    slnatom = (f["slnact"] + f["slchi"] - 2 * f["slsurv"] - slcv2)
    return margin_chain(f["s_star"], slD, f["slL1"], f["slneff"],
                        f["slnact"], slcv2, slcv2, f["slchi"],
                        f["slsurv"], slnatom, l1_fac=l1_fac)


def fr_coherence_swap(wrong="none"):
    """the coherence identity on the signed toy dc = (1, -2 | 3)
    (r302 values): chi = D/Q = 5/7, identity dev 0 EXACT;
    wrong='swap' uses chi' = Q/D = 7/5 and must break the identity
    by 48/35 EXACT (the m4 mutant)."""
    dc = [Fr(1), Fr(-2), Fr(3)]
    P = [dc[0] + dc[1], dc[2]]
    D = sum(p * p for p in P)
    L1 = sum(abs(p) for p in P)
    act = [abs(p) for p in P if p != 0]
    n_act = len(act)
    mu = sum(act) / n_act
    var = sum((a - mu) ** 2 for a in act) / n_act
    cv2 = var / (mu * mu)
    L1a = sum(abs(v) for v in dc)
    Q = sum(v * v for v in dc)
    chi = Q / D if wrong == "swap" else D / Q
    surv = L1 / L1a
    natom = L1a * L1a / Q
    lhs = (1 + cv2) * surv * surv * natom
    rhs = n_act * chi
    return abs(lhs - rhs), chi


def fr_rho1(vals):
    """exact Fractions lag-1 numerator/denominator of a profile
    (Fraction arithmetic on the float inputs is exact)."""
    zf = [Fr(float(v)) for v in vals]
    n = len(zf)
    mu = sum(zf) / n
    zc = [v - mu for v in zf]
    S1 = sum(zc[i] * zc[i + 1] for i in range(n - 1))
    A0 = sum(v * v for v in zc)
    return S1, A0


def toy_rho_and_swap():
    """rho1_stat on (1,-1,1,-1) == -3/4 EXACT and on (-1,-1,1,1)
    == +1/4 EXACT (float == Fractions); swap_arrange on the 4-toy
    must hit the achievable target -3/4 exactly with the multiset
    preserved bitwise.  Returns (worst dev, toy converged)."""
    r_alt, _s, _a = rho1_stat([1.0, -1.0, 1.0, -1.0])
    r_srt, _s2, _a2 = rho1_stat([-1.0, -1.0, 1.0, 1.0])
    S1a, A0a = fr_rho1([1.0, -1.0, 1.0, -1.0])
    S1b, A0b = fr_rho1([-1.0, -1.0, 1.0, 1.0])
    worst = max(abs(r_alt + 0.75), abs(r_srt - 0.25),
                abs(float(S1a / A0a) + 0.75),
                abs(float(S1b / A0b) - 0.25))
    zs, _p, r1, _att, conv = swap_arrange(
        np.array([-1.0, -1.0, 1.0, 1.0]), -0.75, seed=7, cap=500)
    ok_ms = np.array_equal(np.sort(zs),
                           np.array([-1.0, -1.0, 1.0, 1.0]))
    worst = max(worst, abs(r1 + 0.75))
    return worst, (conv and ok_ms)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("atom_target_probe -- PRIME.PORT.L2.ATOM_TARGET.01 "
          "(round 303)")
    print("SPEC_SHA %s   R300_SHA %s   R301_SHA %s   R302_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], DTP.SPEC_SHA[:16], NTP.SPEC_SHA[:16],
             UTP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9 + one synthetic build + m2/m3 "
                        "mutants; ladder, slopes, families, "
                        "adjudications, censuses, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE ATOM-TARGET ROUND WITH HARD REGRESS AUDIT: the "
          "r300/r301/r302 cascade froze three inequalities with "
          "the SAME measured margin 0.055 -- Leg A adjudicates "
          "whether it is ONE algebraic slack propagated through "
          "exact reparametrizations (REGRESS_CONFIRMED vs "
          "LEVELS_INDEPENDENT, sealed) incl. the sigma-level "
          "surplus and the 1/2-conversion conjecture; Leg B runs "
          "the FIRST non-tautological mechanism test: sealed "
          "synthetic dc rearrangements (exact marginal, steered "
          "rho_1: matched / zero / flipped, 8 replicates each) "
          "measured through the whole chain (MIXING_SUFFICIENT / "
          "INSUFFICIENT / IRRELEVANT, sealed); Leg C prints the "
          "honest consequence map; ALL bars, bands, rules and "
          "verdicts sealed BEFORE evaluation")

    # ---------------- S1: census + controls (r302 scaffold verbatim)
    section("S1  CENSUS + CONTROLS")
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
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
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
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs)))

    # ---------------- S2: decomposition + Leg 0 anchors
    section("S2  EXACT DECOMPOSITION + R297-R302 ANCHORS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d mains + 3 "
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

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
        P_ov, P_fr, _n_b, _n_w = FDP.overlap_split(
            bxs, cts, rc["xu"], rc["cw"], rc["lo"], rc["hi"],
            brk, m)
        cconv, n_common = FDP.cconv_census(bxs, cts, rc["xu"],
                                           rc["cw"])
        full_ov = int(n_common == len(rc["bx"]) == len(rc["xu"]))
        part = DTP.participation(Pd)
        qu = NTP.quasi_uniformity(Pd)
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = DTP.shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                              rc["xu"], rc["cw"], rc["wu"])
        df_dev = float(np.max(np.abs(sd["dc"]
                                     - sd["dw"] * sd["f"]))) \
            / max(float(np.max(np.abs(sd["dc"]))), 1e-300) \
            if sd["n"] else 0.0
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        W_abs = float(np.sum(np.abs(sd["dc"]))) if sd["n"] else 0.0
        degenerate = (W_abs <= DEG_FLOOR * absm)
        if degenerate or m == 0 or sd["n"] == 0:
            co = UTP.coherence_split(np.zeros(0), np.zeros(0),
                                     rc["lo"], rc["hi"],
                                     brk if m else np.zeros(0), m)
            rec_dev = 0.0
            eq_dev = 0.0
            na_dev = 0.0
            pr = dict(lloc=1.0, neff_atom=1.0, n=0)
            lags = [0.0] * K_LAG
            xb_sh = np.zeros(0)
            zb_sh = np.zeros(0)
            rho1c = 0.0
        else:
            co = UTP.coherence_split(sd["x"], sd["dc"], rc["lo"],
                                     rc["hi"], brk, m)
            rec_scale = max(float(np.max(np.abs(P_ov)))
                            if m else 0.0,
                            REC_FLOOR * absm, 1e-300)
            rec_dev = float(np.max(np.abs(co["P"] - P_ov))) \
                / rec_scale if m else 0.0
            eq_dev = abs(co["cv2"] - qu["cv2"]) \
                / max(qu["cv2"], 1e-300) if full_ov else 0.0
            pr = NTP.dc_profile(sd["x"], sd["dc"], rc["lo"],
                                rc["hi"])
            na_dev = abs(co["natom"] - pr["neff_atom"]) \
                / max(pr["neff_atom"], 1e-300)
            lags = UTP.lagk_profile(sd["x"], sd["dc"], rc["lo"],
                                    rc["hi"], K_LAG)
            edm = PBB.mask_edge(sd["x"], rc["lo"], rc["hi"],
                                EDGE_F)
            xb_sh = sd["x"][~edm]
            zb_sh = sd["dc"][~edm]
            rho1c = rho1_stat(zb_sh)[0]
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, Pd=Pd, brk=brk,
                    full_ov=full_ov, part=part, qu=qu, sd=sd,
                    df_dev=df_dev, degenerate=degenerate, co=co,
                    rec_dev=rec_dev, eq_dev=eq_dev,
                    na_dev=na_dev, pr=pr, lags=lags,
                    xb=xb_sh, zb=zb_sh, rho1=rho1c)

    all_rc = recs + mrecs
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

    # per-world identity wards (coherence / count / CS / rho cons)
    qid_w = max(rc["ev"]["qu"]["qid_dev"] for rc in pool_all)
    co_w = max(rc["ev"]["co"]["id_dev"] for rc in pool_all)
    cs_w = max(rc["ev"]["co"]["cs_slack"] for rc in pool_all)
    rec_w = max(rc["ev"]["rec_dev"] for rc in pool_all)
    eq_w = max(rc["ev"]["eq_dev"] for rc in all_rc)
    na_w = max(rc["ev"]["na_dev"] for rc in pool_all)
    df_w = max(rc["ev"]["df_dev"] for rc in pool_all)
    rcons_w = max(abs(rc["ev"]["rho1"] - rc["ev"]["lags"][0])
                  for rc in all_rc if rc["ev"]["sd"]["n"])
    deg_note = [("%s" % c) for c in crecs
                if crecs[c]["ev"]["degenerate"]]
    check("G22-identity-wards", qid_w <= QID_BAR and co_w <= CO_BAR
          and cs_w <= CSK_BAR and rec_w <= EQ_BAR
          and eq_w <= EQ_BAR and na_w <= NA_BAR
          and df_w <= EQ_BAR and rcons_w <= RHO_CONS_BAR,
          "identity wards on %d worlds: count identity worst %.1e "
          "(bar %.0e); coherence identity worst %.1e (bar %.0e); "
          "CS cap slack %.1e; P_shared == P_ov %.1e; CV^2 "
          "equality %.1e; n_eff_atom internal %.1e; dc == dw x f "
          "%.1e; rho1_stat == lagk consistency %.1e (bar %.0e)%s"
          % (len(pool_all), qid_w, QID_BAR, co_w, CO_BAR, cs_w,
             rec_w, eq_w, na_w, df_w, rcons_w, RHO_CONS_BAR,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    Ns = [rc["N"] for rc in recs]
    st = {}
    if not smoke:
        def med(fn):
            return float(np.median([fn(rc["ev"]) for rc in recs]))

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
        st["sl_c2"] = L2D.halves_slope(Ns, eps_c2_rel)
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        st["sl_pref"] = L2D.halves_slope(Ns, pref)
        st["sigma"] = slp([rc["ev"]["S_F"] / (M_W * M_W)
                           for rc in recs])
        st["sigma_star"] = 2.0 * (st["sl_c2"] - DELTA_NEED) \
            - st["sl_pref"]
        neffs = [rc["ev"]["part"]["neff"] for rc in recs]
        st["neff_med"] = float(np.median(neffs))
        st["sl_neff"] = slp(neffs)
        st["sl_L1"] = slp([rc["ev"]["part"]["L1"] / M_W
                           for rc in recs])
        st["sl_D"] = slp([rc["ev"]["part"]["D"] for rc in recs])
        st["nact_med"] = med(lambda ev: ev["qu"]["n_act"])
        st["sl_nact"] = slp([rc["ev"]["qu"]["n_act"]
                             for rc in recs])
        st["nact_full"] = sum(1 for rc in recs
                              if rc["ev"]["qu"]["n_act"]
                              == rc["ev"]["m"])
        st["cv2_med"] = med(lambda ev: ev["qu"]["cv2"])
        st["sl_cv2p"] = slp([1.0 + rc["ev"]["qu"]["cv2"]
                             for rc in recs])
        st["sl_cv2p_sh"] = slp([1.0 + rc["ev"]["co"]["cv2"]
                                for rc in recs])
        st["natom_med"] = med(lambda ev: ev["pr"]["neff_atom"])
        st["sl_natom"] = slp([rc["ev"]["pr"]["neff_atom"]
                              for rc in recs])
        st["surv_med"] = med(lambda ev: ev["co"]["surv"])
        st["sl_surv"] = slp([rc["ev"]["co"]["surv"]
                             for rc in recs])
        st["chi_med"] = med(lambda ev: ev["co"]["chi"])
        st["sl_chi"] = slp([rc["ev"]["co"]["chi"]
                            for rc in recs])
        st["sl_nact_sh"] = slp([rc["ev"]["co"]["n_act"]
                                for rc in recs])
        st["sl_D_sh"] = slp([rc["ev"]["co"]["D"] for rc in recs])
        for k in range(3):
            st["rho%d" % (k + 1)] = med(
                lambda ev, k=k: ev["lags"][k])
        nact_eq = all(rc["ev"]["co"]["n_act"]
                      == rc["ev"]["qu"]["n_act"] for rc in recs)
        check("G23-r297-r300-anchors",
              abs(st["sigma"] - R297_SIGMA) <= R297_TOL
              and abs(st["sigma_star"] - R297_SIGMA_STAR)
              <= R297_TOL
              and abs(st["sl_c2"] - R297_SL_C2) <= R297_TOL
              and abs(st["sl_pref"] - R297_SL_PREF) <= R297_TOL
              and abs(st["sl_D"] - R299_SL_D) <= R299_SL_D_TOL
              and abs(st["neff_med"] - R300_NEFF_MED)
              <= R300_NEFF_TOL
              and abs(st["sl_neff"] - R300_SL_NEFF) <= R300_SL_TOL
              and abs(st["sl_L1"] - R300_SL_L1) <= R300_SL_TOL,
              "the r297/r299/r300 set recomputed bit-near: sigma "
              "%+.3f (ref %+.3f), sigma* %+.3f (ref %+.3f), sl_c2 "
              "%+.3f, sl_pref %+.3f; sl_D %+.3f (ref %+.3f); "
              "n_eff med %.2f sl %+.3f, sl_L1 %+.3f; NEED = 2 "
              "sl_L1 - sigma* = %+.3f (record +0.908)"
              % (st["sigma"], R297_SIGMA, st["sigma_star"],
                 R297_SIGMA_STAR, st["sl_c2"], st["sl_pref"],
                 st["sl_D"], R299_SL_D, st["neff_med"],
                 st["sl_neff"], st["sl_L1"],
                 2.0 * st["sl_L1"] - st["sigma_star"]))
        check("G24-r301-anchors",
              abs(st["nact_med"] - R301_NACT_MED) <= R301_NACT_TOL
              and abs(st["sl_nact"] - R301_SL_NACT) <= R301_SL_TOL
              and st["nact_full"] == 42 and nact_eq
              and abs(st["cv2_med"] - R301_CV2_MED) <= R301_CV2_TOL
              and abs(st["sl_cv2p"] - R301_SL_CV2P) <= R301_SL_TOL
              and abs(st["natom_med"] - R301_NATOM_MED)
              <= R301_NATOM_TOL
              and abs(st["sl_natom"] - R301_SL_NATOM)
              <= R301_SL_TOL
              and abs(st["surv_med"] - R301_SURV_MED)
              <= R301_SURV_TOL
              and abs(st["sl_surv"] - R301_SL_SURV)
              <= R301_SL_TOL,
              "the r301 set recomputed bit-near: n_act med %.1f "
              "sl %+.3f COUNT LINK %d/42%s (co == qu n_act %s), "
              "CV^2 med %.2f sl_cv2p %+.3f (shared %+.3f), "
              "n_eff_atom med %.1f sl %+.3f, surv %.2f/%+.3f"
              % (st["nact_med"], st["sl_nact"], st["nact_full"],
                 " EXACT" if st["nact_full"] == 42 else "",
                 "EXACT" if nact_eq else "BROKEN",
                 st["cv2_med"], st["sl_cv2p"], st["sl_cv2p_sh"],
                 st["natom_med"], st["sl_natom"],
                 st["surv_med"], st["sl_surv"]))
        # r302 stationarity + transient anchors
        grp_y = []
        grp_m2 = []
        grp_iN = []
        for gi in range(3):
            sel = recs[gi * N_GRP:(gi + 1) * N_GRP]
            ys = []
            m2s = []
            for rc in sel:
                va = rc["ev"]["co"]["vals"]
                if len(va):
                    ys.append(va / float(np.mean(va)))
                    m2s.append(1.0 + rc["ev"]["co"]["cv2"])
            grp_y.append(np.concatenate(ys) if ys
                         else np.zeros(0))
            grp_m2.append(float(np.median(m2s)))
            grp_iN.append(float(np.median(
                [1.0 / rc["N"] for rc in sel])))
        ks13 = UTP.ks_two(grp_y[0], grp_y[2])
        ks23 = UTP.ks_two(grp_y[1], grp_y[2])
        A_fs, B_fs, pred = UTP.fs_solve(
            1.0 / grp_iN[0], grp_m2[0], 1.0 / grp_iN[2],
            grp_m2[2], 1.0 / grp_iN[1])
        fs_dev = abs(pred - grp_m2[1]) / max(grp_m2[1], 1e-300)
        st.update(ks13=ks13, ks23=ks23, A_fs=A_fs, fs_dev=fs_dev)
        check("G25-r302-anchors",
              abs(st["chi_med"] - R302_CHI_MED) <= R302_CHI_TOL
              and abs(st["sl_chi"] - R302_SL_CHI) <= R301_SL_TOL
              and all(abs(st["rho%d" % (k + 1)] - R302_RHO[k])
                      <= R302_RHO_TOL for k in range(3))
              and abs(ks13 - R302_KS13) <= R302_KS_TOL
              and abs(ks23 - R302_KS23) <= R302_KS_TOL
              and ks13 <= KS_STAT
              and abs(A_fs - R302_A_FS) <= R302_A_TOL
              and fs_dev <= FS_BAR,
              "the r302 set recomputed bit-near: chi med %.3f sl "
              "%+.3f (destructive, falling); rho_1/2/3 med "
              "%+.3f/%+.3f/%+.3f; stationarity KS(G1,G3) %.3f "
              "KS(G2,G3) %.3f (STATIONARY %s); 1/N transient A "
              "%.3f held-out dev %.3f (bar %.2f)"
              % (st["chi_med"], st["sl_chi"], st["rho1"],
                 st["rho2"], st["rho3"], ks13, ks23,
                 ks13 <= KS_STAT, A_fs, fs_dev, FS_BAR))
    else:
        check("G23-r297-r300-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G24-r301-anchors", True, "SMOKE: skipped")
        check("G25-r302-anchors", True, "SMOKE: skipped")

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    mc_fr = fr_margin_chain()
    mc_m1 = fr_margin_chain(l1_fac=1)
    ok_fr = (mc_fr["mD"] == Fr(3, 50) and mc_fr["mN"] == Fr(3, 50)
             and mc_fr["mU"] == Fr(3, 50)
             and mc_fr["mA"] == Fr(3, 50)
             and mc_fr["dN"] == 0 and mc_fr["dU"] == 0
             and mc_fr["dB"] == 0 and mc_fr["dA"] == 0)
    m1_break = abs(mc_m1["mN"] - mc_m1["mD"])
    check("G30-fractions-margin-chain-and-m1",
          ok_fr and m1_break == Fr(1, 5),
          "the slack propagation RE-PROVED exact in Fractions on "
          "the rational slope set (sigma* -1/2, sl_L1 1/5, "
          "sl_neff 24/25 => sl_D -14/25, sl_nact 1 => sl_cv2p "
          "1/25, chi -1/20, surv -1/50 => sl_natom 19/20): ALL "
          "four margins == 3/50 EXACT, devs 0; m1 WRONG "
          "1/2-FACTOR (NEED' = 1 x sl_L1 - sigma*) breaks the "
          "D<->NEFF invariance by %s == sl_L1 EXACT -- CAUGHT: "
          "the factor 2 on the mass slope is load-bearing"
          % str(m1_break))
    co_dev, co_chi = fr_coherence_swap()
    m4_dev, m4_chi = fr_coherence_swap("swap")
    check("G31-fractions-coherence-and-m4",
          co_dev == 0 and co_chi == Fr(5, 7)
          and m4_dev == Fr(48, 35) and m4_chi == Fr(7, 5),
          "the coherence identity RE-PROVED exact in Fractions on "
          "the signed toy (1,-2|3): chi = D/Q = %s, dev %s; m4 "
          "SWAPPED D/Q (chi' = %s) breaks the identity by %s "
          "EXACT -- CAUGHT: the coherence-ratio orientation is "
          "load-bearing" % (str(co_chi), str(co_dev),
                            str(m4_chi), str(m4_dev)))
    toy_w, toy_conv = toy_rho_and_swap()
    mc_fl = margin_chain(-0.5, -14.0 / 25.0, 0.2, 24.0 / 25.0,
                         1.0, 1.0 / 25.0, 1.0 / 25.0, -0.05,
                         -0.02, 19.0 / 20.0)
    fl_dev = max(abs(mc_fl["mD"] - 0.06), abs(mc_fl["mN"] - 0.06),
                 mc_fl["dN"], mc_fl["dU"], mc_fl["dB"],
                 mc_fl["dA"])
    check("G32-toy-exactness", toy_w <= TOY_BAR and toy_conv
          and fl_dev <= TOY_BAR,
          "rho1 toys EXACT (alternating (1,-1,1,-1) -> -3/4, "
          "sorted -> +1/4; float == Fractions, worst dev %.1e); "
          "swap_arrange hits the achievable target -3/4 with the "
          "multiset preserved bitwise (%s); margin_chain float == "
          "Fractions on the m1 slope set (worst dev %.1e, bar "
          "%.0e)" % (toy_w, "converged" if toy_conv else "MISS",
                     fl_dev, TOY_BAR))
    h_mc = scope_audit("margin_chain", BOUND_FORBIDDEN)
    h_r1 = scope_audit("rho1_stat", BOUND_FORBIDDEN)
    h_sw = scope_audit("swap_arrange", BOUND_FORBIDDEN)
    h_al = scope_audit("alt_census", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_mc or h_r1 or h_sw or h_al)
    check("G33-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (margin_chain, rho1_stat, "
          "swap_arrange, alt_census) consume slope numbers / "
          "profile values / positions only (no truth-side "
          "identifier in scope%s); m5a gift mutant FLAGGED (%s); "
          "m5b branch-peek mutant FLAGGED (%s); fragment audit: "
          "%s (the swap search is a seeded greedy descent, no "
          "fit primitive)"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: Leg A -- the regress audit
    section("S4  LEG A: THE REGRESS AUDIT (SLACK PROPAGATION)")
    if not smoke:
        mc = margin_chain(st["sigma_star"], st["sl_D"],
                          st["sl_L1"], st["sl_neff"],
                          st["sl_nact"], st["sl_cv2p"],
                          st["sl_cv2p_sh"], st["sl_chi"],
                          st["sl_surv"], st["sl_natom"])
        inv_ok = (mc["dN"] <= PROP_BAR and mc["dU"] <= PROP_BAR
                  and mc["dB"] <= PROP_BAR
                  and mc["dA"] <= PROP_BAR)
        marg_ok = all(abs(v - MARGIN_REF) <= MARGIN_TOL
                      for v in (mc["mD"], mc["mN"], mc["mU"],
                                mc["mA"]))
        need_ok = (abs(mc["und"] - R302_UNIF_NEED)
                   <= R302_NEED_TOL
                   and abs(mc["a_nd"] - R302_ATOM_NEED)
                   <= R302_NEED_TOL)
        check("G40-margin-chain-wards", inv_ok and marg_ok
              and need_ok,
              "MARGIN_CHAIN live on the 42-rung ladder: NEED "
              "%+.3f, UNIF_NEED %+.3f (record +0.094), ATOM_NEED "
              "%+.3f (record +0.888); margins m_D %+.4f / m_NEFF "
              "%+.4f / m_UNIF %+.4f (blk) %+.4f (sh) / m_ATOM "
              "%+.4f (record 0.055 each); invariance devs dN "
              "%.1e / dU %.1e / dB %.1e / dA %.1e (bar %.0e)"
              % (mc["nd"], mc["und"], mc["a_nd"], mc["mD"],
                 mc["mN"], mc["mU"], mc["mUs"], mc["mA"],
                 mc["dN"], mc["dU"], mc["dB"], mc["dA"],
                 PROP_BAR))
        regress = "REGRESS_CONFIRMED" if inv_ok \
            else "LEVELS_INDEPENDENT"
        slack_sig = st["sigma_star"] - st["sigma"]
        surplus = st["sl_D"] - st["sigma"]
        conj = slack_sig / 2.0
        half_holds = abs(conj - mc["mD"]) <= HALF_CONJ_TOL
        check("G41-regress-adjudication", True,
              "SEALED RULE fired: %s -- the 0.055 margin is %s; "
              "core S = sigma* - sl_D = %+.3f - (%+.3f) = %+.4f; "
              "sigma-level decomposition: sigma* - sigma = %+.4f "
              "= S %+.4f + ratio surplus (sl_D - sigma) %+.4f "
              "EXACT (the r297 sigma slack carries the extra "
              "measured S_F/D decay; only its BOUNDEDNESS is "
              "structural, r300); HALF_CONJ %s: (sigma* - "
              "sigma)/2 = %+.4f vs m_D %+.4f, dev %.4f (tol "
              "%.3f) -- %s"
              % (regress,
                 "ONE algebraic number (slack-invariant through "
                 "the r300/r301/r302 identities)" if inv_ok else
                 "NOT invariant (devs above bar, see G40)",
                 st["sigma_star"], st["sl_D"], mc["mD"],
                 slack_sig, mc["mD"], surplus,
                 "HOLDS" if half_holds else "REFUTED",
                 conj, mc["mD"], abs(conj - mc["mD"]),
                 HALF_CONJ_TOL,
                 "the charter's 1/2-conversion exists" if
                 half_holds else
                 "no 1/2-conversion exists in the chain: the "
                 "factor 2 lives only in NEED = 2 sl_L1 - sigma* "
                 "and cancels exactly in every margin "
                 "difference"))
        st["mc"] = mc
        st["regress"] = regress
        st["half_holds"] = half_holds
    else:
        check("G40-margin-chain-wards", True,
              "SMOKE: skipped (Fractions re-proof gated in G30)")
        check("G41-regress-adjudication", True, "SMOKE: skipped")
        st["regress"] = "SMOKE"

    # ---------------- S5: Leg B -- the mixing mechanism test
    section("S5  LEG B: SYNTHETIC MIXING FAMILIES")
    fam_defs = (("A_RHO_MATCH", 0, lambda r1: r1),
                ("B_RHO_ZERO", 1, lambda r1: 0.0),
                ("C_RHO_FLIP", 2, lambda r1: -r1))
    if smoke:
        rc0 = recs[0]
        ev0 = rc0["ev"]
        zs, perm, r1s, att, conv = swap_arrange(
            ev0["zb"], 0.0, SEED_BASE, min(SWAP_F * len(ev0["zb"]),
                                           SWAP_CAP))
        ok_ms = np.array_equal(np.sort(zs), np.sort(ev0["zb"]))
        co_s = UTP.coherence_split(ev0["xb"], zs, rc0["lo"],
                                   rc0["hi"], ev0["brk"],
                                   ev0["m"])
        na_inv = abs(co_s["natom"] - ev0["co"]["natom"]) \
            / max(ev0["co"]["natom"], 1e-300)
        check("G50-construction-wards", conv and ok_ms
              and na_inv <= NA_INV_BAR,
              "SMOKE build (w9, family b, rep 0): converged %s "
              "(rho1 %+.3f target 0), marginal sorted-bitwise %s, "
              "natom invariance %.1e (bar %.0e); real w9 chi %.3f "
              "-> synthetic chi %.3f"
              % (conv, r1s, ok_ms, na_inv, NA_INV_BAR,
                 ev0["co"]["chi"], co_s["chi"]))
        fam_res = {}
    else:
        fam_res = {}
        conv_n = 0
        n_builds = 0
        worst_rho_miss = 0.0
        worst_fix = 0.0
        na_inv_worst = 0.0
        ms_ok_all = True
        seeds_used = set()
        for fname, fi, tfun in fam_defs:
            reps = []
            for rep in range(R_REP):
                chi_l = []
                cv2p_l = []
                D_l = []
                natom_l = []
                for ri, rc in enumerate(recs):
                    ev = rc["ev"]
                    seed = SEED_BASE + ri * 100 + fi * 10 + rep
                    seeds_used.add(seed)
                    tgt = tfun(ev["rho1"])
                    zb = ev["zb"]
                    zs, perm, r1s, att, conv = swap_arrange(
                        zb, tgt, seed,
                        min(SWAP_F * len(zb), SWAP_CAP))
                    n_builds += 1
                    conv_n += int(conv)
                    worst_rho_miss = max(worst_rho_miss,
                                         abs(r1s - tgt))
                    if fi == 0:
                        fixshare = float(np.mean(
                            perm == np.arange(len(zb))))
                        worst_fix = max(worst_fix, fixshare)
                    ms_ok_all = ms_ok_all and np.array_equal(
                        np.sort(zs), np.sort(zb))
                    co_s = UTP.coherence_split(
                        ev["xb"], zs, rc["lo"], rc["hi"],
                        ev["brk"], ev["m"])
                    na_inv_worst = max(
                        na_inv_worst,
                        abs(co_s["natom"] - ev["co"]["natom"])
                        / max(ev["co"]["natom"], 1e-300))
                    chi_l.append(co_s["chi"])
                    cv2p_l.append(1.0 + co_s["cv2"])
                    D_l.append(co_s["D"])
                    natom_l.append(co_s["natom"])
                reps.append(dict(
                    chi=float(np.median(chi_l)),
                    slc=L2D.halves_slope(Ns, cv2p_l),
                    slD=L2D.halves_slope(Ns, D_l),
                    sln=L2D.halves_slope(Ns, natom_l)))
            fam_res[fname] = dict(
                chi=float(np.median([r["chi"] for r in reps])),
                chi_lo=min(r["chi"] for r in reps),
                chi_hi=max(r["chi"] for r in reps),
                slc=float(np.median([r["slc"] for r in reps])),
                slc_lo=min(r["slc"] for r in reps),
                slc_hi=max(r["slc"] for r in reps),
                slD=float(np.median([r["slD"] for r in reps])),
                slD_lo=min(r["slD"] for r in reps),
                slD_hi=max(r["slD"] for r in reps),
                sln=float(np.median([r["sln"] for r in reps])))
        conv_share = conv_n / max(n_builds, 1)
        seeds_ok = len(seeds_used) == n_builds
        check("G50-construction-wards",
              conv_share >= CONV_MIN and ms_ok_all
              and worst_fix <= FIX_MAX
              and na_inv_worst <= NA_INV_BAR and seeds_ok,
              "construction wards over %d builds (42 rungs x 3 "
              "families x %d replicates): convergence %d/%d "
              "(share %.3f >= %.2f), worst |rho1 - target| %.2e "
              "(tol %.0e), family-(a) fixed-point share max %.3f "
              "(bar %.1f), marginal sorted-bitwise %s, "
              "n_eff_atom invariance worst %.1e (bar %.0e -- the "
              "DISCLOSED marginal-functional fact: sl_natom "
              "%+.3f on every family by algebra), seeds "
              "collision-free %s"
              % (n_builds, R_REP, conv_n, n_builds, conv_share,
                 CONV_MIN, worst_rho_miss, RHO_TOL, worst_fix,
                 FIX_MAX, "42/42 x 24" if ms_ok_all else "BROKEN",
                 na_inv_worst, NA_INV_BAR, st["sl_natom"],
                 seeds_ok))

    # m2 + m3 mutants (on w9, both modes)
    rc0 = recs[0]
    ev0 = rc0["ev"]
    zb0 = ev0["zb"]
    n0 = len(zb0)
    L1a0 = float(np.sum(np.abs(zb0)))
    Q0 = float(np.sum(zb0 * zb0))
    z_m2 = (L1a0 / n0) * np.where(np.arange(n0) % 2 == 0, 1.0,
                                  -1.0)
    m2_sorted_breaks = not np.array_equal(np.sort(z_m2),
                                          np.sort(zb0))
    Q_m2 = float(np.sum(z_m2 * z_m2))
    m2_qdev = abs(Q_m2 - Q0) / max(Q0, 1e-300)
    zs_a, perm_a, _r, _a, _c = swap_arrange(zb0, 0.0,
                                            SEED_BASE + 1, 2000)
    zs_b, perm_b, _r2, _a2, _c2 = swap_arrange(zb0, 0.0,
                                               SEED_BASE + 1, 2000)
    m3_caught = np.array_equal(perm_a, perm_b)
    zs_d, perm_d, _r3, _a3, _c3 = swap_arrange(zb0, 0.0,
                                               SEED_BASE + 2, 2000)
    m3_distinct = not np.array_equal(perm_a, perm_d)
    check("G51-mustfails-m2-m3",
          m2_sorted_breaks and m2_qdev >= MUT_MIN and m3_caught
          and m3_distinct,
          "m2 UNMATCHED MARGINAL (constant-|value| two-sign "
          "profile, same L1a): sorted-multiset ward BREAKS (%s) "
          "AND atom energy deviates rel %.1e >= %.0e LOUD (real "
          "n_eff_atom %.1f != n %d) -- the marginal ward is "
          "load-bearing; m3 SEED COLLISION: same-seed replicates "
          "produce the identical arrangement (CAUGHT %s), "
          "distinct seeds differ (%s)"
          % (m2_sorted_breaks, m2_qdev, MUT_MIN,
             ev0["co"]["natom"], n0, m3_caught, m3_distinct))

    if not smoke:
        real = dict(chi=st["chi_med"], slc=st["sl_cv2p_sh"],
                    slD=st["sl_D_sh"])
        table = []
        repro = {}
        clear = {}
        for fname, fi, _t in fam_defs:
            fr_ = fam_res[fname]
            d_chi = abs(fr_["chi"] - real["chi"])
            d_slc = abs(fr_["slc"] - real["slc"])
            d_slD = abs(fr_["slD"] - real["slD"])
            repro[fname] = (d_chi <= CHI_BAND
                            and d_slc <= SLP_BAND
                            and d_slD <= SLP_BAND)
            clear[fname] = (d_chi > MISS_F * CHI_BAND
                            or d_slc > MISS_F * SLP_BAND
                            or d_slD > MISS_F * SLP_BAND)
            table.append(
                "%s chi %.3f [%.3f, %.3f] sl_cv2p %+.3f [%+.3f, "
                "%+.3f] sl_D %+.3f [%+.3f, %+.3f] margin %+.3f "
                "sl_natom %+.3f%s"
                % (fname, fr_["chi"], fr_["chi_lo"],
                   fr_["chi_hi"], fr_["slc"], fr_["slc_lo"],
                   fr_["slc_hi"], fr_["slD"], fr_["slD_lo"],
                   fr_["slD_hi"],
                   st["sigma_star"] - fr_["slD"], fr_["sln"],
                   " REPRODUCES" if repro[fname] else
                   (" CLEAR MISS" if clear[fname] else " miss")))
        for t in table:
            info(t)
        if repro["A_RHO_MATCH"] and clear["B_RHO_ZERO"] \
                and clear["C_RHO_FLIP"]:
            mixing = "MIXING_SUFFICIENT"
        elif repro["A_RHO_MATCH"] and repro["B_RHO_ZERO"] \
                and repro["C_RHO_FLIP"]:
            mixing = "MIXING_IRRELEVANT"
        else:
            miss_note = []
            for fname, fi, _t in fam_defs:
                fr_ = fam_res[fname]
                parts = []
                if abs(fr_["chi"] - real["chi"]) > CHI_BAND:
                    parts.append("chi by %.3f"
                                 % abs(fr_["chi"] - real["chi"]))
                if abs(fr_["slc"] - real["slc"]) > SLP_BAND:
                    parts.append("sl_cv2p by %.3f"
                                 % abs(fr_["slc"] - real["slc"]))
                if abs(fr_["slD"] - real["slD"]) > SLP_BAND:
                    parts.append("sl_D by %.3f"
                                 % abs(fr_["slD"] - real["slD"]))
                if parts:
                    miss_note.append("%s misses %s"
                                     % (fname, ", ".join(parts)))
            mixing = "MIXING_INSUFFICIENT(%s)" \
                % "; ".join(miss_note)
        check("G52-mixing-adjudication", True,
              "SEALED RULE fired: %s -- real chi %.3f sl_cv2p "
              "%+.3f sl_D %+.3f margin %+.3f; bands chi %.2f / "
              "slopes %.2f, clear-miss factor %.1f; (a) "
              "reproduces %s, (b) clear-miss %s, (c) clear-miss "
              "%s" % (mixing, real["chi"], real["slc"],
                      real["slD"],
                      st["sigma_star"] - real["slD"], CHI_BAND,
                      SLP_BAND, MISS_F, repro["A_RHO_MATCH"],
                      clear["B_RHO_ZERO"], clear["C_RHO_FLIP"]))
        st["mixing"] = mixing
    else:
        check("G52-mixing-adjudication", True, "SMOKE: skipped")
        st["mixing"] = "SMOKE"

    # ---------------- S6: the rho-sign census (connection test)
    section("S6  RHO-SIGN CENSUS (THE CONNECTION, MEASURED)")
    if not smoke:
        s1_signs = []
        alts = []
        for rc in recs:
            _r1, S1, _A0 = rho1_stat(rc["ev"]["zb"])
            s1_signs.append(S1 < 0.0)
            alts.append(alt_census(rc["ev"]["zb"]))
        n_neg = sum(s1_signs)
        alt_med = float(np.median(alts))
        by_N = sorted(recs, key=lambda r_: r_["N"])[:2]
        fr_note = []
        fr_neg = True
        for rc in by_N:
            S1f, A0f = fr_rho1(rc["ev"]["zb"])
            fr_neg = fr_neg and (S1f < 0)
            fr_note.append("kz%d (N %d) S1 = %.6g EXACT %s"
                           % (rc["kz"], rc["N"], float(S1f),
                              "< 0" if S1f < 0 else ">= 0"))
        tag = ("RHO1_NEG_UNIFORM" if n_neg == 42
               else "RHO1_SIGN_MIXED")
        check("G60-rho-sign-census", True,
              "%s: lag-1 numerator S1 < 0 on %d/42 rungs; "
              "alternation fraction med %.3f; Fractions-EXACT on "
              "the two smallest rungs: %s -- the sign census the "
              "connection needs; the DERIVATION of rho_1 <= 0 "
              "from the three-term recursion (adjacent-pi "
              "orthogonality) stays OPEN, typed"
              % (tag, n_neg, alt_med, "; ".join(fr_note)))
        st["n_neg"] = n_neg
        st["alt_med"] = alt_med
        st["rho_tag"] = tag
    else:
        check("G60-rho-sign-census", True, "SMOKE: skipped")

    # ---------------- S7: Leg C -- the consequence map
    section("S7  LEG C: CONSEQUENCE ADJUDICATION")
    if not smoke:
        mx = st["mixing"]
        if st["regress"] == "REGRESS_CONFIRMED":
            core_level = ("ATOM (validated mechanism)"
                          if mx == "MIXING_SUFFICIENT" else
                          ("UNIF/A2 (the stationary-profile "
                           "level: the marginal alone carries)"
                           if mx == "MIXING_IRRELEVANT" else
                           "ATOM (most falsification-tested "
                           "structure; missing ingredient "
                           "disclosed)"))
            if mx == "MIXING_SUFFICIENT":
                cons = ("(i) the core of the generic L2 half is: "
                        "rho_1 <= 0 + marginal stationarity => "
                        "slack > 0 -- the most precise form ever "
                        "reached; THE one target is a proof "
                        "attempt on this level (rho_1 <= 0 from "
                        "the three-term recursion), NOT another "
                        "reduction round")
            elif mx == "MIXING_IRRELEVANT":
                cons = ("(iii) the mechanism is pure distribution "
                        "stationarity (the r302 A2 level); the "
                        "mixing trace is bycatch; the cascade is "
                        "CLOSED as a dictionary")
            else:
                cons = ("(ii) the core stays empirical; the "
                        "cascade r297->r302 is CLOSED as an exact "
                        "dictionary with ONE measured core S = "
                        "sigma* - sl_D; further reduction rounds "
                        "may NOT be counted as progress on the "
                        "inequality; the honest new object is "
                        "the NAMED mechanism gap: %s" % mx)
        else:
            core_level = "n/a (levels independent)"
            cons = ("(iv) LEVELS_INDEPENDENT: ATOM_TARGET "
                    "continues as a normal open target")
        check("G70-consequence-map", True,
              "CORE_LEVEL(%s) + CONSEQUENCE_MAP(%s)"
              % (core_level, cons))
        st["core_level"] = core_level
        st["cons"] = cons
    else:
        check("G70-consequence-map", True, "SMOKE: skipped")

    # ---------------- S8: worlds + mp wards
    section("S8  WORLD CLASSES + MP WARDS")
    ctl_note = []
    for c in ("EPST", "SCR"):
        ev = crecs[c]["ev"]
        ctl_note.append("%s chi %.2f rho1 %+.2f natom %.0f"
                        % (c, ev["co"]["chi"], ev["rho1"],
                           ev["co"]["natom"]))
    check("G80-world-controls",
          crecs["EPST"]["ev"]["co"]["id_dev"] <= CO_BAR
          and crecs["SCR"]["ev"]["co"]["id_dev"] <= CO_BAR,
          "the coherence identity holds on the live controls by "
          "algebra (world-blind): %s; SMOOTH degenerate "
          "(pre-declared guard); r302 bracket MAIN chi 0.63 "
          "between EPST 0.18 and SCR 1.26 -- reproduced in-table"
          % "; ".join(ctl_note))
    if not smoke:
        mp_note = []
        ok_mp = True
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        t15 = PBB.mp_drive(rc15["p"], MP_DPS)
        d15 = abs(t15 - rc15["t_term"])
        ok_mp = ok_mp and (d15 <= MP_T_BAR)
        mp_note.append("kz15 (N %d) dev %.1e (bar %.0e)"
                       % (rc15["N"], d15, MP_T_BAR))
        for rc in recs[-2:]:
            t_mp = PBB.mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("kz%d (N %d, DEEPEST) dev %.1e (bar "
                           "%.0e)" % (rc["kz"], rc["N"], dv,
                                      MP_DEEP_BAR))
        check("G81-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G81-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact margin-chain audit (Fractions + live "
          "wards), the sigma-surplus decomposition, the "
          "1/2-conjecture adjudication, the sealed synthetic "
          "mixing families with exact-marginal construction "
          "wards, the rho-sign census and the consequence map "
          "-- NO new certificate promoted, NO bound modification "
          "of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        mc = st["mc"]
        parts = ["MARGIN_CHAIN(m_D %+.4f m_NEFF %+.4f m_UNIF "
                 "%+.4f/%+.4f m_ATOM %+.4f; devs %.0e/%.0e/%.0e/"
                 "%.0e)"
                 % (mc["mD"], mc["mN"], mc["mU"], mc["mUs"],
                    mc["mA"], mc["dN"], mc["dU"], mc["dB"],
                    mc["dA"])]
        if st["regress"] == "REGRESS_CONFIRMED":
            parts.append("REGRESS_CONFIRMED(S = sigma* - sl_D = "
                         "%+.4f; sigma surplus %+.4f; HALF_CONJ "
                         "%s)"
                         % (mc["mD"],
                            st["sl_D"] - st["sigma"],
                            "HOLDS" if st["half_holds"]
                            else "REFUTED"))
        else:
            parts.append("LEVELS_INDEPENDENT(devs above bar)")
        for fname, fi, _t in fam_defs:
            fr_ = fam_res[fname]
            parts.append("%s(chi %.2f slc %+.3f slD %+.3f mrg "
                         "%+.3f)"
                         % (fname.split("_")[0], fr_["chi"],
                            fr_["slc"], fr_["slD"],
                            st["sigma_star"] - fr_["slD"]))
        parts.append(st["mixing"])
        parts.append("RHO_SIGN(%s %d/42, alt %.3f)"
                     % (st["rho_tag"], st["n_neg"],
                        st["alt_med"]))
        parts.append("CORE_LEVEL(%s)" % st["core_level"])
        parts.append("CONSEQUENCE(%s)" % st["cons"][:60])
        parts.append("WORLD_NOTE(identity world-blind by "
                     "algebra; EPST/SCR bracket reproduced)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the margin-chain "
          "invariance, the Fractions re-proofs and the "
          "marginal-invariance of n_eff_atom (all world-blind); "
          "MEASURED: every slope, med, band comparison, census "
          "and synthetic family (42 rungs, 8 seeded replicates); "
          "OPEN: the ONE core slack S beyond the measured 42, "
          "rho_1 <= 0 as a recursion theorem, the cofinal step "
          "H5, kz15 beyond r270; NO RH claim"
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
