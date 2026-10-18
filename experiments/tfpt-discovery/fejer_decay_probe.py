#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fejer_decay_probe -- PRIME.PORT.L2.FEJER_DECAY.01 (round 299):
the DECAY ANATOMY of the Delta Fejer energy -- can the decay of
B(PDelta, PDelta) (the r297 target sigma <= sigma* = -0.516) be
derived SOURCE-PURELY from position equidistribution (provable
terrain) plus a controllable statement about the signed mass
structure?  Context (sealed record inputs): r297 (SPEC e42a76eb)
froze the target inequality sigma := slope(S_F/M_W^2) <= sigma* =
-0.516 (measured sigma = -0.714, margin 0.198) and left two
assets: exact window orthogonality + falling boundary-position
discrepancy (D_rank med 0.024, slope -0.42) against growing mass
imbalance (+0.244); r298 (SPEC 05e831be) proved the exact
sign-preserving split S_F = B(omega,omega) + B(Delta,omega+beta)
on the frozen positional Fejer kernel and adjudicated
TRANSFER_DOMINANT: the window main term is EMPTY (med -3.94 dec,
slope -1.386), the cross term negligible (med -1.4e-4), so
S_F ~ B(PDelta, PDelta) -- THE VDC INPUT IS THE FEJER ENERGY OF
THE DIFFERENCE MEASURE; sigma is ITS decay exponent; the in-T
sign cancellation sum|t_j|/|T| (med 1.69) GROWS at +0.207 -- the
enemy of every magnitude route; the sign mixing of Delta sits in
the c-values (6 negative atoms only; w9: 367 exact position
overlaps between the unions).  kz15 permanently closed via r270;
the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297/r298 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks (r270 convention); FROZEN vdC window H = max(2,
ceil(sqrt(m))); the frozen positional Fejer block kernel (r298:
block_breaks + aggregate_blocks + fejer_bil + fejer_apply,
imported verbatim); PDelta = Pbeta - Pomega; the round's central
quantity is the DELTA FEJER ENERGY B := B(PDelta, PDelta) =
(1/H) sum_t W_t(PDelta)^2.  THE EXACT SPECTRAL REPRESENTATION
(module-own, the h-decomposition of the frozen kernel): with L =
the smallest power of two >= 2 x (m + H) (FROZEN rule; L >=
2m - 1 kills circular aliasing, L >= m + H - 1 keeps the Fejer
support intact) and Dhat(k) = FFT_L(PDelta),

  B  =  (1/L) sum_k F_H(theta_k) |Dhat(k)|^2,      theta_k = 2 pi k / L,

with F_H(theta) = |sum_{j<H} e^{-ij theta}|^2 / H >= 0 the Fejer
kernel (computed as the padded FFT of the H-ones window, no
sin singularity) -- an EXACT finite identity (recomposition
gated <= 1e-9 rel on all 47 worlds; Parseval mean identity
(1/L) sum_k |Dhat|^2 = sum_j PDelta_j^2 gated too; every term
nonnegative).  F_H is a LOW-PASS kernel with main lobe |theta|
<= 2 pi / H (disclosed structural prior: the LOW band is
kernel-favored; the bands measure where |Dhat|^2 puts its
energy INSIDE the weighted form).

LEG 0 -- ANCHOR REGRESSION (r297/r298 record numbers adopted
as-is, disclosed): sigma = -0.714 tol 0.01, sigma* = -0.516 tol
0.01 (sl_c2 +0.196, sl_pref +0.489, tol 0.01); D_rank med 0.024
tol 0.005 slope -0.42 tol 0.05; imbalance slope +0.244 tol 0.01;
the r298 decomposition recomputed bit-near: identity/kernel
devs <= 1e-12, attribution <= 1e-9, share med 0.99 tol 0.02,
slope(MAIN) -1.386 tol 0.05, slope(|T|) -0.698 tol 0.05, T > 0
on 42/42, canc_T med 1.69 tol 0.05 slope +0.207 tol 0.02,
|T_cross med| <= 1e-3, w9 support overlap == 367 EXACT, linear
window zero <= 1e-9 main / 3e-6 deep / 1e-6 controls; the r297
Parseval sum rule re-computed exact in Fractions (import).

LEG A -- THE FREQUENCY ANATOMY OF DELTA (where does the energy
live?): per rung the exact spectral split of B into the three
FROZEN bands LOW (|theta| <= 2 pi / H, the Fejer main lobe),
MID (2 pi / H < |theta| <= pi / 2), EDGE (|theta| > pi / 2);
band shares (med) + band-energy slopes on the 42-rung ladder;
the mean-vs-max census: mean_k |Dhat|^2 = sum PDelta_j^2 (the
Parseval identity -- the mean IS the B2 diagonal, disclosed)
and max_k |Dhat|^2 with slopes; the half/90-pct energy
frequencies q50/q90 in main-lobe units theta x H / (2 pi).
SEALED BAND ADJUDICATION (exactly one): LOWPASS iff
med(share_LOW) >= 0.75 (few low frequencies dominate -- their
individual decay is the provable-terrain shape); BROADBAND iff
med(share_LOW) < 0.50; else MIXED_BAND.  Fine type:
SPECTRUM_MAP(band shares, slopes, mean/max decay, tag).

LEG B -- THE DECAY DERIVATION ROUTES (the core; every route an
exact per-rung statement on all 47 worlds, source-pure, AST
scope audit):
(B1) ERDOS-TURAN / ABEL ROUTE (position x mass, the provable
  terrain): per frequency the EXACT factorization |Dhat(k)| <=
  Dpos(theta_k) x V(PDelta) with Dpos(theta) = min(m,
  1/|sin(theta/2)|) (pure geometric-sum position bound on the
  block lattice) and V = sum_j |PDelta_{j+1} - PDelta_j| +
  |PDelta_{m-1}| (the Abel mass term, v964-S0 T4 form); the
  composed bound B <= V^2 x Phi_pos with Phi_pos = (1/L) sum_k
  F_H(theta_k) Dpos(theta_k)^2 (position/kernel factor,
  universal on the block lattice); slopes sl_pos = slope(
  Phi_pos), sl_mass = slope(V^2/M^2), exact slope additivity
  gated (<= 1e-9); MASS_TARGET_FROZEN printed as a standalone
  target inequality: slope(V^2/M^2) <= sigma* - sl_pos (needed
  vs measured, MET/NOT MET); census: the r297 D_rank statistic
  now on Delta itself (sup-discrepancy of the bulk Delta atom
  positions against uniform on the bulk hull, med + slope).
(B2) PAIR-CORRELATION ROUTE: the exact split B = D + O with
  D = sum_j PDelta_j^2 (diagonal, positive, magnitudes) and
  O = 2 sum_{1<=h<H} (1 - h/H) A(h) (off-diagonal, signed);
  recomposition ward <= 1e-12 of scale; slopes sl_D, sl_|O|,
  O sign census, ratio B/D (med + slope).  Does the energy fall
  because D falls (a density statement) or because O cancels
  increasingly (then the pair phase is the object)?  Crossref
  disclosed: r287 found the BORDER block sequence REINFORCES
  ((sum P)^2 > sum P^2 on 39/44) -- whether PDelta shares this
  is measured here, not assumed.
(B3) OVERLAP ROUTE (the r298 anatomy trace): the EXACT split
  Delta = Delta_overlap (+) Delta_fresh by EXACT position
  equality between the unions (w9: 367 shared positions;
  Delta_overlap is a pure c-VALUE difference there); component
  vectors P_ov + P_fr = PDelta gated <= 1e-12; energy
  recomposition B = B(ov,ov) + 2 B(ov,fr) + B(fr,fr) gated <=
  1e-9 of the component scale; shares (med + slopes); the
  c-CONVERGENCE census at shared positions: cconv = sum_p
  |c_beta(p) - c_omega(p)| / sum_p |c_beta(p)| (med + slope) --
  if Delta_overlap dominates, the decay is a statement about
  the CONVERGENCE of the c-values (border -> window),
  connectable to the proven sum rule.  SEALED dominance class:
  OV_DOM iff med(B_ov/B) >= 0.75 and med(|B_x|/B) <= 0.50;
  FR_DOM symmetric on B_fr; else MIXED_OVERLAP.
SEALED DECAY ADJUDICATION (frozen BEFORE evaluation, exactly
one fires): route validity = every exact ward on 47 worlds;
  B1_OK iff valid and sl_pos + sl_mass <= sigma*;
  B2_OK iff valid and sl_D <= sigma* and slope(B/D) <= +0.05;
  B3_OK iff valid and class OV_DOM;
  DECAY_DERIVED(B1)  iff B1 valid and sl_pos <= sigma* and
    sl_mass <= 0.0 (the position/kernel factor alone meets the
    target and the mass factor is non-growing -- the only fully
    provable-terrain outcome; disclosed expectation: ambitious);
  DECAY_SPLIT(fired routes, rest targets frozen)  iff not
    DERIVED and (B1_OK or B2_OK or B3_OK) -- each firing route
    prints its frozen rest target (B1: MASS_TARGET; B2:
    DIAG_TARGET = prove the diagonal density decay; B3:
    CVALUE_TARGET = prove the c-value convergence rate);
  DECAY_STILL_EMPIRICAL(measured common obstruction) otherwise.
WORLD CONTROLS: the identities/wards hold on EPSTEIN/SCRAMBLE
by the same algebra (gates); the CLASSES (band tag, O sign,
overlap dominance, by the same med rules at the single control
rung) are compared against MAIN -- a class break is a disclosed
finding (WORLD_SENSITIVE tag), not a gate failure.

LEG C -- THEOREM COMPOSITION (fires ONLY on DECAY_DERIVED or on
DECAY_SPLIT with its frozen rest target as explicit hypothesis):
CANDIDATE THEOREM printed with every constant: Leg-B bound (+
frozen rest hypothesis if SPLIT) => sigma <= sigma* => the r297
target inequality => v964-S0 vdC => delta' > 0.21 on the
generic half; scope the 42 measured rungs (N in [142, 878]);
exceptions: 6 via r287 F2, kz15 via r270.  Wave-9 promotion
candidate -- NOT promoted here.  Otherwise Leg C is VOID
without substitute and the rest object is documented.

LEG D -- THE IN-T CANCELLATION LOCUS (bycatch, ONE table, no
interpretation): the magnitude spectrum B_abs = B(|PDelta|,
|PDelta|) >= B EXACTLY (window sums of magnitudes majorize,
gated); the cancellation gap G = B_abs - B band-resolved
(G_band = E_abs_band - E_band): band shares of G vs band shares
of B (med); block side: c_j = |t_j| - t_j (the r298 attribution,
nonnegative, positive exactly on cancelling blocks),
sp(block mass Mb, c_j) med + argmax coincidence n/42, next to
the r298 anchor sp(Mb, |t_j|) med.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) WRONG FEJER WEIGHT in the frequency decomposition: the lag
  recomposition with (1 - |h|/(H+1)) breaks the toy identity
  (B(PDelta=(1,-1,1), H=2) = 1 vs 1/3 -- break 2/3 EXACT) --
  CAUGHT; (m2) MAGNITUDE PAIR ROUTE (|PDelta| instead of
  PDelta): B(|PDelta|,|PDelta|) differs from B LOUDLY (>= 1e-6
  of scale on w9 + w13; toy 5 vs 1, break 4 exact) -- the pair
  phase is load-bearing; (m3) TOLERANT OVERLAP SPLIT (position
  tolerance 1e-3 instead of exact equality, toy): border (1.0,
  2.0)/(2,-1) + window (1.0005, 3.0)/(1,1), single block, H=2:
  the exact split has EMPTY overlap (B_ov = 0, B_fr = 1), the
  tolerant split moves energy between the classes (B_ov = 1,
  B_fr = 4) while BOTH recompose to B = 1 -- the recomposition
  is silent, the component shift is CAUGHT (>= 1e-6): the
  exact-equality convention is load-bearing; (m4) ERDOS-TURAN
  PREFACTOR FAMILY (exact Fractions, module-own, attaching to
  v964-S0 T4): (a) the Abel bound |sum P| <= D* x V re-proved
  on the frozen rational sequences with the toy record D* = 1,
  V = 2 on P = (2,-2,1); the DROPPED-TERMINAL mutant gives
  bound 0 < 2 on P = (1,1) -- CAUGHT; (b) the exact theta =
  pi/2 leg (e^{-i theta} = -i, Gaussian-rational pairs): the
  Abel resummation identity u = sum (c_n - c_{n+1}) E_n exact
  on c = (3,-1,2) (u = 1 + i, dev 0), the geometric position
  bound |E_n|^2 <= 1/sin^2(pi/4) = 2 with the n = 1 EQUALITY
  witness, |u|^2 = 2 <= max|E|^2 x V^2 = 162 exact; the HALVED
  position prefactor mutant (claim |E_n|^2 <= 1) breaks at the
  witness (2 > 1) -- CAUGHT; (m5a/m5b) WORLD-BLINDNESS BREAK:
  a builder consuming the withheld terminal drive key AND a
  builder consuming the branch label are both FLAGGED by the
  AST scope audit.  Scope hygiene: the new builders
  (spec_decomp, band_energies, et_factors, pair_split,
  overlap_split) consume positions + weights + chain values
  only (BOUND_FORBIDDEN set); fragment audit (no fit
  primitives); TOY EXACTNESS: the r298 hand kernel toy extended
  by a window atom AT a border position (border (0..4)/(3,-1,2,
  -4,1), window (1.0, 2.5)/(1,-1), H = 2): Pbeta (2,-2,1),
  Pomega (1,-1,0), PDelta (1,-1,1), B = 1; overlap = {1.0},
  P_ov = (-2,0,0), P_fr = (3,-1,1), B_ov = 4, B_fr = 7, B_x =
  -10, sum = 1 EXACT (bar 1e-14) -- the components are LARGE
  against their sum: the signed structure lives in the split;
  cconv toy = 2; pair toy D = 3, O = -2; ET toy V = 5; spectral
  toys at FFT precision (bar 1e-12): recomposition == 1,
  Parseval == 3, band sum == B; SMOOTH anchor (alias <= 1e-12,
  q_N <= 1e-20); mp SAMPLES (dps 60): kz15 (bar 1e-8) + the two
  deepest rungs (bar 3e-6).

INDEX FIREWALL (binding, r238-r298 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks + WBT.fejer_bil +
WBT.fejer_apply, r269 PBB.mask_edge + PBB.runs_split +
PBB.mp_drive, r287 L2D.blocks_level2 + L2D.bound_vdc +
L2D.halves_slope + L2D.autocorr_full, r297 VCP.chain_quads +
VCP.fr_symbolic_sumrule (the proven set re-computed, not
re-proved), r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r260 TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881
PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN); L rule
= smallest power of two >= 2 x (m + H) (FROZEN); BANDS: LOW
|theta| <= 2 pi / H, MID <= pi / 2, EDGE else (FROZEN);
LOWPASS_BAR 0.75; BROAD_BAR 0.50; SPEC_BAR 1e-9 (spectral
recomposition + Parseval + abs-majorization, rel scale); ET_BAR
1e-9 (per-frequency Abel slack + composed bound, rel); ADD_BAR
1e-9 (slope additivity); PAIR_BAR 1e-12 (pair split, rel scale);
PART_BAR 1e-12 (overlap partition, rel max|PDelta|); EN_BAR 1e-9
(overlap energy recomposition, rel component scale);
RATIO_GROW 0.05; OV_DOM_BAR 0.75; XA_BAR 0.50; MASS_FLAT 0.0;
TOL_MUT 1e-3 (m3 mutant tolerance); KER_BAR/DEC_BAR 1e-12;
ATTR_BAR 1e-9; LIN_BARS 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls; TB_WARD bars 1e-9 / 3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR
1e-9; TOY_BAR 1e-14; TOY_FFT_BAR 1e-12; MUT_MIN 1e-6; R297
anchors sigma -0.714 / sigma* -0.516 / sl_c2 +0.196 / sl_pref
+0.489 (tol 0.01), D_rank med 0.024 tol 0.005 slope -0.42 tol
0.05, imb slope +0.244 tol 0.01; R298 anchors share med 0.99
tol 0.02, sl_MAIN -1.386 tol 0.05, sl_|T| -0.698 tol 0.05,
T > 0 on 42/42, canc med 1.69 tol 0.05, canc slope +0.207 tol
0.02, |tc med| <= 1e-3, OVERLAP_W9 == 367 EXACT; MP_DPS 60;
MP_T_BAR 1e-8; MP_DEEP_BAR 3e-6; SM_Q_BAR 1e-20; SM_ALIAS_BAR
1e-12; KZ_ANCHOR 15; runtime <= 1800 s; smoke = w9 + controls +
Fractions section + toys + scope audits + every exact ward at
w9 (ladder, slopes, adjudications, Legs C/D aggregates, mp
wards skipped).  DISCLOSED PRE-SPEC INPUT (no scratch run of
this probe): every reproduction band is an r297/r298 RECORD
number adopted as-is; the low-pass structure of F_H and the
Parseval mean identity are derived algebra, disclosed above;
the three adjudication outcomes are sealed symmetrically -- the
disclosed structural priors (kernel low-pass favor; r297: the
border-P magnitudes REINFORCE; the mass imbalance grows) make
STILL_EMPIRICAL plausible, but no rule was chosen to favor an
outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  SPECTRUM_MAP(band shares LOW/MID/EDGE med, band slopes,
    mean/max |Dhat|^2 slopes, q50/q90 med, band tag)
+ ROUTE_TABLE(B1 valid n/47 sl_pos sl_mass composed-vs-sigma*;
    B2 valid n/47 sl_D sl_|O| O-sign census B/D med + slope;
    B3 valid n/47 shares ov/x/fr med, cconv med + slope, class)
+ MASS_TARGET(the frozen standalone rest inequality of B1:
    needed vs measured, MET/NOT MET)
+ [exactly one of] DECAY_DERIVED(B1, ...) / DECAY_SPLIT(fired
    routes + frozen rest targets) / DECAY_STILL_EMPIRICAL(
    measured common obstruction)
+ [iff fired] CANDIDATE_THEOREM(decay composition, constants)
+ CANC_LOCUS(band shares of G vs B, sp(Mb, c_j) med,
    coincidence n/42, sp(Mb, |t_j|) med)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if a control class differs] WORLD_SENSITIVE(disclosed).
Honesty before beauty: the spectral representation, the ET
factorization, the pair split and the overlap split are EXACT
finite identities/inequalities, but every slope, share and
class is MEASURED on 42 rungs only; no verdict claims a cofinal
law; Phi_pos is universal on the block lattice -- the
equidistribution content enters through the block aggregation
and is measured (D_rank on Delta), not proved here; the
exception scalar's positivity beyond the measured 42 stays
OPEN; r243-r298 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 32/32 (0.3 s, no amendment); calibration pass 1 =
first full evaluation, 32/32 gates, wall 48.3 s; amendments
AFTER calibration pass 1: a1 (the G71 world-blindness
conjunction did not include the O-sign class the sealed spec
text names -- code aligned with the spec, expected and realized
effect: the WORLD_SENSITIVE tag fires as a disclosed finding;
no bar, band or gate rule moved) + a2 (REPORTING ONLY: the G55
census additionally prints the full-support overlap count --
the calibration pass showed the unions share EVERY position);
calibration pass 2 = 32/32, identical to pass 1 in every printed
figure up to WALL and the disclosed a1/a2 lines; record run1/
run2 after this insertion, identical up to WALL; the only
post-freeze edits are a1/a2 and this record-table insertion,
which IS the protocol):
CAL_VERDICT = SPECTRUM_MAP(band shares LOW/MID/EDGE med
0.93/0.04/0.02; band-energy slopes -0.758/-0.014/-0.979; mean
|Dhat|^2 slope -0.571 (== the B2 diagonal), max slope -0.444;
q50 med 0.19 / q90 med 0.62 main-lobe units; LOWPASS -- the
Delta energy is concentrated INSIDE the Fejer main lobe: the
decay is a low-frequency phenomenon, not broadband) +
ROUTE_TABLE(B1 valid 47/47: sl_pos +1.504, sl_mass +0.444,
composed +1.948 FAILS sigma* -0.516 by 2.464 -- the position/
kernel factor Phi_pos GROWS and the Abel mass term V^2 grows
too: the ET route composes away the cancellation, the r297
magnitude-wall pattern recurs at the frequency level; B2 valid
47/47: sl_D -0.571 MEETS sigma* -0.516 (margin 0.055), sl_|O|
-0.815, O < 0 on 13/42 only (the PDelta pair field REINFORCES
in the majority -- the r287 border pattern carries over), B/D
med 1.29 slope -0.168 FALLING; B3 valid 47/47: shares ov/x/fr
med +1.00/+0.00/+0.00, FULL-SUPPORT overlap on 42/42 rungs --
THE STRUCTURAL FINDING: the border and window unions share
EVERY position, Delta_fresh == 0 identically, Delta IS a pure
c-value difference measure; cconv med 0.86 slope +0.045 (the
RELATIVE c-difference does NOT fall), class OV_DOM) +
MASS_TARGET(needed slope(V^2/M^2) <= sigma* - sl_pos = -2.021;
measured +0.444: NOT MET by 2.464) + DECAY_SPLIT(B2(
DIAG_TARGET: prove sl_D <= sigma*, measured -0.571, + ratio
flatness, measured -0.168) | B3(CVALUE_TARGET: prove the
c-value convergence rate, cconv slope +0.045)) +
CANDIDATE_THEOREM(conditional, printed in S6, wave-9 candidate
NOT promoted) + CANC_LOCUS(G = B_abs - B band shares
1.01/-0.01/-0.00 vs B 0.93/0.04/0.02 -- the cancellation gap
is ENTIRELY low-band; sp(Mb, c_j) med -0.01, argmax coincidence
3/42 -- the cancellation carriers are NOT the mass blocks;
r298 anchor sp(Mb, |t_j|) med +0.69) + WORLD_SENSITIVE(MAIN
LOWPASS/O_POS/OV_DOM vs EPST LOWPASS/O_NEG/OV_DOM + SCR
LOWPASS/O_NEG/OV_DOM -- the off-diagonal SIGN class separates
MAIN from the broken-arithmetic controls at their own rungs;
disclosed finding).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13
deep / 2.4e-8 controls; block + autocorr identities worst
6.3e-16 / 2.7e-15 on 47 worlds; r297 anchors bit-near (sigma
-0.714, sigma* -0.516, sl_c2 +0.196, sl_pref +0.489; D_rank
med 0.024 sl -0.42, imb sl +0.244); r298 anchors bit-near
(identity 8.8e-16, kernel 7.5e-16, attribution 5.4e-16; lin
zero 2.2e-12 / 6.4e-12 / 5.0e-7; share med 0.99, sl_MAIN
-1.386, sl_|T| -0.698, T < 0 on 0/42, canc 1.69 sl +0.207, tc
med -1.4e-4, overlap w9 367; r297 sum rule import devs 0/0).
S3: the Fractions ET section exact (Abel resummation identity
dev 0, position bound slack 0 with the n = 1 equality witness,
|u|^2 = 2 <= 162); m4a dropped-terminal 0 < 2 CAUGHT, m4b
halved prefactor breaks by 1 at the witness CAUGHT; toys exact
(worst 0.0 exact / 0.0 FFT); m1 wrong-weight break 0.666667 =
2/3 exact LOUD; m3 tolerant-split component shift 3.0 + count
shift 1 with SILENT recomposition (dev 0.0) CAUGHT.  S4:
spectral wards worst recomposition 7.1e-16, Parseval 3.9e-16,
band sum 3.5e-16, magnitude-majorization slack 0.0, 47/47
worlds.  S5: B1 per-frequency slack -7.8e-1 (the bound holds
with 0.78 x sum|PDelta| margin), composed slack 0.0,
additivity dev 6.1e-16; D_rank(Delta) med 0.016 slope -0.12
(the Delta support inherits the falling equidistribution); B2
pair ward worst 8.2e-16; B3 partition worst 0.0, energy
recomposition worst 0.0; exception rungs in-table: sh_low
0.94 (kz22, kz52) .. 0.99 (kz39), cconv 0.70 (kz22) .. 0.94
(kz15, kz52); w13 is the only shown rung with O < 0 (-3.2e-3).
S8: m2 magnitude-pair break 1.3e+0 (w9) / 4.6e+0 (w13) of B
LOUD; SMOOTH alias 2.4e-14, q_N 4.2e-25, wards trivially
exact; mp wards kz15 2.9e-10, kz64 9.3e-9, kz52 6.6e-8.
READING (typed, no upgrade): the round DELIVERS the frequency
anatomy the lane asked for, and the answer is SHARPER than the
question: (1) the Delta Fejer energy is LOWPASS (med 0.93 in
the main lobe) -- sigma is a low-frequency phenomenon; (2) the
unions share their FULL support on 42/42 rungs: Delta is a
pure c-value difference measure -- the transfer object of r298
degenerates to ONE weight profile on ONE shared node set,
and the c-difference is relatively FLAT (cconv 0.86, +0.045):
the decay does NOT come from pointwise c-convergence but from
aggregate cancellation of a non-converging difference profile;
(3) the ET/Abel composition FAILS loudly (composed +1.948,
MASS_TARGET missed by 2.46) -- the r297 magnitude wall recurs
at the frequency level: position bounds compose away the
cancellation; (4) the LIVE EDGE is B2: the diagonal
sum PDelta_j^2 ALREADY falls fast enough (sl_D -0.571 <=
sigma* -0.516, margin 0.055) and the pair ratio B/D (med 1.29)
FALLS (-0.168) -- proving the two frozen rest statements
(DIAG_TARGET: a magnitude-density bound on ONE positive
quantity; RATIO flatness: the off-diagonal reinforcement does
not grow) would close the input gap through the vdC machine;
the sealed adjudication fired DECAY_SPLIT with this rest pair
frozen, Leg C printed the conditional composition.  Bycatch:
the in-T cancellation gap is entirely low-band and NOT carried
by the mass blocks (sp -0.01 vs the +0.69 energy coupling) --
the r297 imbalance growth and the in-T cancellation live in
the SAME band but on DIFFERENT blocks; and the O-sign class
separates MAIN (reinforcing) from both dead controls
(cancelling) -- the first world-separating sign class of the
L2 lane, disclosed as WORLD_SENSITIVE.  Runtime 48.3 s full /
0.3 s smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE beyond the disclosed a1/a2 (records inserted per
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
import vdc_chain_provenance_probe as VCP       # noqa: E402 r297
import window_border_transfer_probe as WBT     # noqa: E402 r298
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
KER_BAR = 1e-12
DEC_BAR = 1e-12
ATTR_BAR = 1e-9
LIN_BAR = 1e-9
LIN_BAR_DEEP = 3e-6
LIN_BAR_CTRL = 1e-6
SPEC_BAR = 1e-9
ET_BAR = 1e-9
ADD_BAR = 1e-9
PAIR_BAR = 1e-12
PART_BAR = 1e-12
EN_BAR = 1e-9
LOWPASS_BAR = 0.75
BROAD_BAR = 0.50
RATIO_GROW = 0.05
OV_DOM_BAR = 0.75
XA_BAR = 0.50
MASS_FLAT = 0.0
TOL_MUT = 1e-3
TOY_BAR = 1e-14
TOY_FFT_BAR = 1e-12
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
R297_SIGMA = -0.714
R297_SIGMA_TOL = 0.01
R297_SIGMA_STAR = -0.516
R297_SSTAR_TOL = 0.01
R297_SL_C2 = 0.196
R297_SL_C2_TOL = 0.01
R297_SL_PREF = 0.489
R297_SL_PREF_TOL = 0.01
R297_DRANK_MED = 0.024
R297_DRANK_TOL = 0.005
R297_DRANK_SL = -0.42
R297_DRANK_SL_TOL = 0.05
R297_IMB_SL = 0.244
R297_IMB_SL_TOL = 0.01
R298_SH_MED = 0.99
R298_SH_TOL = 0.02
R298_SL_MAIN = -1.386
R298_SL_MAIN_TOL = 0.05
R298_SL_T = -0.698
R298_SL_T_TOL = 0.05
R298_CANC_MED = 1.69
R298_CANC_TOL = 0.05
R298_CANC_SL = 0.207
R298_CANC_SL_TOL = 0.02
R298_TC_ABS = 1e-3
R298_OVERLAP_W9 = 367
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
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


# ---------------- exact Fractions section: the Erdos-Turan / Abel
# ---------------- legs (module-own; the m4 prefactor mutant family)
FR_SEQS = (
    [Fr(2), Fr(-2), Fr(1)],
    [Fr(1), Fr(1)],
    [Fr(1), Fr(1), Fr(1), Fr(1)],
    [Fr(3, 7), Fr(-2, 9), Fr(5, 11), Fr(1, 4), Fr(1, 3),
     Fr(-3, 8), Fr(2, 5), Fr(7, 13), Fr(-1, 6)],
    [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
     Fr(1, 3), Fr(-1, 2), Fr(5, 4)],
    [Fr((-1) ** j * (j + 1), 2 * j + 3) for j in range(12)],
)


def fr_abel_bound(P, drop_terminal=False):
    """the v964-S0 T4 Abel/Erdos-Turan bound D* x V (exact); the
    mutant flag drops the terminal magnitude term of V -- must
    break on P = (1, 1) with bound 0 < 2."""
    m = len(P)
    sig = [1 if p > 0 else (-1 if p < 0 else 0) for p in P]
    a = [abs(p) for p in P]
    dstar = max(abs(sum(sig[:n + 1])) for n in range(m))
    var = sum(abs(a[j + 1] - a[j]) for j in range(m - 1))
    V = var if drop_terminal else (a[m - 1] + var)
    return dstar * V, dstar, V


def fr_et_pi2(halved=False):
    """the exact theta = pi/2 position/mass leg (e^{-i theta} =
    -i; Gaussian-rational arithmetic as (re, im) Fraction pairs)
    on c = (3, -1, 2): (i) the Abel resummation identity u =
    sum_n (c_n - c_{n+1}) E_n (c_m := 0) EXACT; (ii) the
    geometric position bound |E_n|^2 <= 1/sin^2(pi/4) = 2 with
    the n = 1 equality witness; (iii) |u|^2 <= max|E|^2 x V^2.
    halved flags the position-prefactor mutant (claim |E_n|^2
    <= 1) -- must break at the witness (2 > 1)."""
    def cadd(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def cmul(a, b):
        return (a[0] * b[0] - a[1] * b[1],
                a[0] * b[1] + a[1] * b[0])

    def csca(s, a):
        return (s * a[0], s * a[1])

    def cabs2(a):
        return a[0] * a[0] + a[1] * a[1]

    mi = (Fr(0), Fr(-1))                     # e^{-i pi/2} = -i
    c = [Fr(3), Fr(-1), Fr(2)]
    m = len(c)
    w = [(Fr(1), Fr(0))]
    for _ in range(m - 1):
        w.append(cmul(w[-1], mi))
    u = (Fr(0), Fr(0))
    for cj, wj in zip(c, w):
        u = cadd(u, csca(cj, wj))
    E = []
    run = (Fr(0), Fr(0))
    for wj in w:
        run = cadd(run, wj)
        E.append(run)
    c_ext = c + [Fr(0)]
    u_abel = (Fr(0), Fr(0))
    for n in range(m):
        u_abel = cadd(u_abel, csca(c_ext[n] - c_ext[n + 1], E[n]))
    dev_abel = cabs2((u[0] - u_abel[0], u[1] - u_abel[1]))
    pos2 = Fr(1) if halved else Fr(2)        # 1/sin^2(pi/4) = 2
    worst_pos = max(cabs2(e) - pos2 for e in E)
    witness = (cabs2(E[1]) == 2)
    V = sum(abs(c_ext[n] - c_ext[n + 1]) for n in range(m))
    comp_ok = (cabs2(u) <= max(cabs2(e) for e in E) * V * V)
    return dict(dev_abel=dev_abel, worst_pos=worst_pos,
                witness=witness, V=V, u2=cabs2(u),
                comp_ok=comp_ok)


# ---------------- the module-own spectral / route builders.
# ---------------- Source-pure: block vectors (positions, weights,
# ---------------- chain values) only; the withheld terminal drive
# ---------------- key, the branch label and every target-side
# ---------------- identifier are forbidden in scope (AST audit).
def spec_decomp(P, H):
    """the exact spectral representation of the Fejer block form:
    B(P, P) = (1/L) sum_k F_H(theta_k) |Phat(k)|^2 with L the
    smallest power of two >= 2 (m + H) (FROZEN rule) and F_H the
    Fejer kernel from the padded FFT of the H-ones window."""
    P = np.asarray(P, dtype=float)
    m = len(P)
    L = 1
    while L < 2 * (m + H):
        L <<= 1
    ud = np.fft.fft(P, L)
    F = np.abs(np.fft.fft(np.ones(H), L)) ** 2 / H
    E = F * np.abs(ud) ** 2 / L
    k = np.arange(L)
    th = 2.0 * np.pi * np.minimum(k, L - k) / L
    return dict(L=L, ud=ud, F=F, E=E, th=th,
                B=float(np.sum(E)),
                pars=float(np.sum(np.abs(ud) ** 2)) / L,
                mx2=float(np.max(np.abs(ud) ** 2)))


def band_energies(th, E, H):
    """the FROZEN three-band split: LOW |theta| <= 2 pi / H (the
    Fejer main lobe), MID <= pi / 2, EDGE else."""
    lo = th <= 2.0 * np.pi / H + 1e-12
    mid = (~lo) & (th <= np.pi / 2.0 + 1e-12)
    ed = ~(lo | mid)
    return (float(np.sum(E[lo])), float(np.sum(E[mid])),
            float(np.sum(E[ed])))


def et_factors(P, H, sp):
    """the B1 Erdos-Turan / Abel factorization per frequency:
    |Phat(k)| <= Dpos(theta_k) x V with Dpos = min(m,
    1/|sin(theta/2)|) (pure geometric-sum position bound) and
    V = sum |diff| + |terminal| (the Abel mass term); composed
    B <= V^2 x Phi_pos, Phi_pos = (1/L) sum F Dpos^2."""
    P = np.asarray(P, dtype=float)
    m = len(P)
    V = (float(np.sum(np.abs(np.diff(P))))
         + (abs(float(P[-1])) if m else 0.0))
    th = sp["th"]
    with np.errstate(divide="ignore"):
        inv = np.where(th > 1e-15,
                       1.0 / np.abs(np.sin(th / 2.0)), float(m))
    dpos = np.minimum(inv, float(m))
    slack = float(np.max(np.abs(sp["ud"]) - dpos * V)) if m else 0.0
    phi = float(np.sum(sp["F"] * dpos * dpos)) / sp["L"]
    return dict(V=V, slack=slack, phi=phi, bound=V * V * phi)


def pair_split(P, H):
    """the B2 exact pair split B = D + O: D = sum P_j^2 (the
    diagonal = the Parseval mean), O = 2 sum_{1<=h<H}
    (1 - h/H) A(h) (the signed off-diagonal)."""
    A = L2D.autocorr_full(P)
    D = float(A[0]) if len(P) else 0.0
    O = 2.0 * float(sum((1.0 - h / float(H)) * A[h]
                        for h in range(1, min(H, len(A)))))
    return D, O


def overlap_split(bxs, cbs, xu, cw, lo, hi, brk, m, tol=0.0):
    """the B3 exact overlap partition of Delta by EXACT position
    equality between the unions (tol > 0 = the m3 mutant):
    Delta_overlap = all atoms at shared positions (border c,
    window -c), Delta_fresh = the rest; components aggregated
    through the frozen r298 positional kernel."""
    if tol > 0.0:
        mb = np.array([bool(np.any(np.abs(xu - x) <= tol))
                       for x in bxs])
        mw = np.array([bool(np.any(np.abs(bxs - x) <= tol))
                       for x in xu])
    else:
        mb = np.isin(bxs, xu)
        mw = np.isin(xu, bxs)
    P_ov = (WBT.aggregate_blocks(bxs[mb], cbs[mb], lo, hi, brk, m)
            - WBT.aggregate_blocks(xu[mw], cw[mw], lo, hi, brk, m))
    P_fr = (WBT.aggregate_blocks(bxs[~mb], cbs[~mb], lo, hi,
                                 brk, m)
            - WBT.aggregate_blocks(xu[~mw], cw[~mw], lo, hi,
                                   brk, m))
    return P_ov, P_fr, int(np.sum(mb)), int(np.sum(mw))


def cconv_census(bxs, cbs, xu, cw):
    """the c-convergence census on the EXACT shared positions:
    cconv = sum_p |c_beta(p) - c_omega(p)| / sum_p |c_beta(p)|
    (per-position sums; duplicate-safe via bincount)."""
    common = np.intersect1d(bxs, xu)
    if len(common) == 0:
        return 0.0, 0
    mb = np.isin(bxs, common)
    mw = np.isin(xu, common)
    cb_at = np.bincount(np.searchsorted(common, bxs[mb]),
                        weights=cbs[mb], minlength=len(common))
    cw_at = np.bincount(np.searchsorted(common, xu[mw]),
                        weights=cw[mw], minlength=len(common))
    num = float(np.sum(np.abs(cb_at - cw_at)))
    den = max(float(np.sum(np.abs(cb_at))), 1e-300)
    return num / den, len(common)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'decay bound' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * WBT.fejer_bil(P, P, 2)


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'diagonal term' that consumes the branch label to pick its
    constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.asarray(P) ** 2))


# ---------------------------------------------- toy exact tools
def toy_spectrum_pair_et():
    """the P-level hand toy PDelta = (1, -1, 1), H = 2: B = 1
    (A0 = 3, A1 = -2); spectral recomposition == 1 and Parseval
    == 3 at FFT precision; band sum == B; pair split D = 3,
    O = -2; ET V = 5, composed bound >= B, per-frequency slack
    <= 0.  Returns (worst_exact, worst_fft)."""
    Pd = np.array([1.0, -1.0, 1.0])
    H = 2
    B = WBT.fejer_bil(Pd, Pd, H)
    worst = abs(B - 1.0)
    sp = spec_decomp(Pd, H)
    wf = abs(sp["B"] - 1.0)
    wf = max(wf, abs(sp["pars"] - 3.0))
    e_lo, e_mid, e_ed = band_energies(sp["th"], sp["E"], H)
    wf = max(wf, abs(e_lo + e_mid + e_ed - 1.0))
    D, O = pair_split(Pd, H)
    worst = max(worst, abs(D - 3.0), abs(O + 2.0),
                abs(D + O - B))
    et = et_factors(Pd, H, sp)
    worst = max(worst, abs(et["V"] - 5.0))
    wf = max(wf, max(et["slack"], 0.0),
             max(B - et["bound"], 0.0))
    return worst, wf


def toy_overlap_exact():
    """the r298 kernel toy EXTENDED by a window atom AT a border
    position: border (0..4)/(3,-1,2,-4,1), window (1.0, 2.5)/
    (1,-1), H = 2 -> Pbeta (2,-2,1), Pomega (1,-1,0), PDelta
    (1,-1,1), B = 1; overlap = {1.0}: P_ov = (-2,0,0), P_fr =
    (3,-1,1); B_ov = 4, B_fr = 7, B_x = -10, sum = 1; cconv =
    2 (|c_beta - c_omega| = |-1 - 1| over |c_beta| = 1)."""
    bx = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    ct = np.array([3.0, -1.0, 2.0, -4.0, 1.0])
    xu = np.array([1.0, 2.5])
    cwv = np.array([1.0, -1.0])
    lo, hi = -10.0, 14.0
    runs = PBB.runs_split(ct)
    brk, m, _jb = WBT.block_breaks(bx, runs)
    Pb = WBT.aggregate_blocks(bx, ct, lo, hi, brk, m)
    Pw = WBT.aggregate_blocks(xu, cwv, lo, hi, brk, m)
    Pd = Pb - Pw
    H = 2
    worst = float(np.max(np.abs(Pd - np.array([1.0, -1.0, 1.0]))))
    B = WBT.fejer_bil(Pd, Pd, H)
    worst = max(worst, abs(B - 1.0))
    P_ov, P_fr, n_b, n_w = overlap_split(bx, ct, xu, cwv, lo, hi,
                                         brk, m)
    worst = max(worst, abs(n_b - 1), abs(n_w - 1),
                float(np.max(np.abs(P_ov - np.array([-2.0, 0.0,
                                                     0.0])))),
                float(np.max(np.abs(P_fr - np.array([3.0, -1.0,
                                                     1.0])))))
    B_ov = WBT.fejer_bil(P_ov, P_ov, H)
    B_fr = WBT.fejer_bil(P_fr, P_fr, H)
    B_x = 2.0 * WBT.fejer_bil(P_ov, P_fr, H)
    worst = max(worst, abs(B_ov - 4.0), abs(B_fr - 7.0),
                abs(B_x + 10.0), abs(B_ov + B_x + B_fr - B))
    cc, n_c = cconv_census(bx, ct, xu, cwv)
    worst = max(worst, abs(cc - 2.0), abs(n_c - 1))
    return worst


def toy_mustfail_m1():
    """m1 WRONG FEJER WEIGHT: the lag recomposition of B with
    (1 - |h|/(H+1)) on PDelta = (1,-1,1), H = 2 gives 1/3
    instead of 1 -- break 2/3 EXACT, LOUD."""
    Pd = [1.0, -1.0, 1.0]
    H = 2
    A = L2D.autocorr_full(Pd)
    wrong = float(A[0]) + 2.0 * float(sum(
        (1.0 - h / float(H + 1)) * A[h]
        for h in range(1, min(H, len(A)))))
    return abs(wrong - WBT.fejer_bil(Pd, Pd, H))


def toy_mustfail_m3():
    """m3 TOLERANT OVERLAP SPLIT: border (1.0, 2.0)/(2,-1) +
    window (1.0005, 3.0)/(1,1), one block, H = 2.  Exact split:
    overlap EMPTY, B_ov = 0, B_fr = 1.  Tolerant split (1e-3):
    B_ov = 1, B_fr = 4 -- BOTH recompose to B = 1 (silent), the
    component shift is the catch.  Returns (component shift,
    worst silent recomposition dev, count shift)."""
    bx = np.array([1.0, 2.0])
    ct = np.array([2.0, -1.0])
    xu = np.array([1.0005, 3.0])
    cwv = np.array([1.0, 1.0])
    lo, hi = -10.0, 14.0
    brk = np.array([])
    m = 1
    H = 2
    Pd = (WBT.aggregate_blocks(bx, ct, lo, hi, brk, m)
          - WBT.aggregate_blocks(xu, cwv, lo, hi, brk, m))
    B = WBT.fejer_bil(Pd, Pd, H)
    outs = []
    for tol in (0.0, TOL_MUT):
        P_ov, P_fr, n_b, _n_w = overlap_split(bx, ct, xu, cwv,
                                              lo, hi, brk, m,
                                              tol=tol)
        B_ov = WBT.fejer_bil(P_ov, P_ov, H)
        B_fr = WBT.fejer_bil(P_fr, P_fr, H)
        B_x = 2.0 * WBT.fejer_bil(P_ov, P_fr, H)
        outs.append((B_ov, B_fr, abs(B_ov + B_x + B_fr - B), n_b))
    shift = max(abs(outs[0][0] - outs[1][0]),
                abs(outs[0][1] - outs[1][1]))
    silent = max(outs[0][2], outs[1][2])
    return shift, silent, abs(outs[0][3] - outs[1][3])


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fejer_decay_probe -- PRIME.PORT.L2.FEJER_DECAY.01 "
          "(round 299)")
    print("SPEC_SHA %s   R297_SHA %s (imported)   R298_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], VCP.SPEC_SHA[:16], WBT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9; ladder, slopes, adjudications, "
                        "Legs C/D aggregates, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE FEJER DECAY ROUND (the r298 gap object executed): "
          "S_F ~ B(PDelta, PDelta) is the vdC input; this round "
          "decomposes B EXACTLY into its frequency spectrum "
          "(module-own FFT representation of the frozen kernel) "
          "and tests THREE source-pure decay derivation routes "
          "(B1 Erdos-Turan position x mass, B2 pair/diagonal "
          "split, B3 exact overlap split with the c-convergence "
          "census); sealed outcomes DERIVED / SPLIT (frozen rest "
          "targets) / STILL_EMPIRICAL; sigma* %.3f, DELTA_NEED "
          "%.2f (r297 records); disclosed structural priors: F_H "
          "is low-pass (main lobe 2 pi / H), the spectral mean "
          "IS the B2 diagonal (Parseval), the r297 border-P "
          "magnitudes REINFORCE; ALL bars, bands, rules and "
          "verdicts sealed BEFORE evaluation"
          % (R297_SIGMA_STAR, DELTA_NEED))

    # ---------------- S1: census + controls (r298 scaffold verbatim)
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

    # ---------------- S2: decomposition + identities + anchors
    section("S2  EXACT DECOMPOSITION + R297/R298 ANCHORS")
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
        # ---- the frozen positional kernel (r298 verbatim)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        agg_dev = float(np.max(np.abs(Pb - np.array(P)))) \
            / max(max(abs(v) for v in P), 1e-300) if m else 0.0
        sf_ker = WBT.fejer_bil(Pb, Pb, H)
        ker_dev = abs(sf_ker - S_F) / max(S_F, 1e-300)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        main = WBT.fejer_bil(Pw, Pw, H)
        Pd = Pb - Pw
        T = WBT.fejer_bil(Pd, Pb + Pw, H)
        scale = max(S_F, main, abs(T), 1e-300)
        dec_dev = abs(S_F - main - T) / scale
        phi = WBT.fejer_apply(Pb + Pw, H)
        tj = Pd * phi
        attr_dev = abs(float(np.sum(tj)) - T) / scale
        t_cross = 2.0 * WBT.fejer_bil(Pd, Pw, H)
        lin_dev = abs(float(np.sum(rc["cw"]))) \
            / max(float(np.sum(np.abs(rc["cw"]))), 1e-300)
        # ---- the central quantity: B = B(PDelta, PDelta)
        B_en = WBT.fejer_bil(Pd, Pd, H)
        comp_dev = abs(B_en + t_cross - T) / scale
        # ---- Leg A: exact spectral decomposition + bands
        sp = spec_decomp(Pd, H)
        b_sc = max(B_en, sp["B"], 1e-300)
        spec_dev = abs(sp["B"] - B_en) / b_sc
        D_diag, O_off = pair_split(Pd, H)
        pars_dev = abs(sp["pars"] - D_diag) / max(D_diag, 1e-300)
        e_lo, e_mid, e_ed = band_energies(sp["th"], sp["E"], H)
        band_dev = abs(e_lo + e_mid + e_ed - sp["B"]) / b_sc
        # half/90-pct energy frequencies in main-lobe units
        order = np.argsort(sp["th"], kind="stable")
        cum = np.cumsum(sp["E"][order])
        tot = max(float(cum[-1]), 1e-300)
        th_s = sp["th"][order]
        q50 = float(th_s[int(np.searchsorted(cum, 0.5 * tot))]) \
            * H / (2.0 * np.pi)
        q90 = float(th_s[int(np.searchsorted(cum, 0.9 * tot))]) \
            * H / (2.0 * np.pi)
        # ---- Leg B1: ET factors
        et = et_factors(Pd, H, sp)
        et_slack = et["slack"] / max(float(np.sum(np.abs(Pd))),
                                     1e-300)
        b1_slack = max(B_en - et["bound"], 0.0) / b_sc
        # D_rank on Delta itself: bulk atom positions (both
        # unions, edge-masked) against uniform on the bulk hull
        wed = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xall = np.sort(np.concatenate([xb, rc["xu"][~wed]]))
        a_h = rc["lo"] + EDGE_F * (rc["hi"] - rc["lo"])
        b_h = rc["hi"] - EDGE_F * (rc["hi"] - rc["lo"])
        nn = len(xall)
        d_delta = float(np.max(np.abs(
            (np.arange(1, nn + 1) / nn)
            - (xall - a_h) / max(b_h - a_h, 1e-300)))) \
            if nn else 0.0
        # ---- Leg B2 ward
        pair_dev = abs(D_diag + O_off - B_en) \
            / max(abs(B_en), D_diag, abs(O_off), 1e-300)
        # ---- Leg B3: exact overlap split
        P_ov, P_fr, n_ovb, n_ovw = overlap_split(
            bxs, cts, rc["xu"], rc["cw"], rc["lo"], rc["hi"],
            brk, m)
        part_dev = float(np.max(np.abs(P_ov + P_fr - Pd))) \
            / max(float(np.max(np.abs(Pd))), 1e-300) if m else 0.0
        B_ov = WBT.fejer_bil(P_ov, P_ov, H)
        B_fr = WBT.fejer_bil(P_fr, P_fr, H)
        B_x = 2.0 * WBT.fejer_bil(P_ov, P_fr, H)
        en_sc = max(B_ov, B_fr, abs(B_x), abs(B_en), 1e-300)
        en_dev = abs(B_ov + B_x + B_fr - B_en) / en_sc
        cconv, n_common = cconv_census(bxs, cts, rc["xu"],
                                       rc["cw"])
        # ---- Leg D: magnitude spectrum + block carriers
        Pa = np.abs(Pd)
        B_abs = WBT.fejer_bil(Pa, Pa, H)
        spa = spec_decomp(Pa, H)
        ga_lo, ga_mid, ga_ed = band_energies(spa["th"], spa["E"],
                                             H)
        abs_slack = max(B_en - B_abs, 0.0) / max(B_abs, 1e-300)
        cj = np.abs(tj) - tj
        Mb = [Mr[i] + (Mr[i + 1] if i + 1 < len(Mr) else 0.0)
              for i in range(0, len(Mr), 2)]
        sp_cj = BH.spearman(Mb, list(cj)) if m >= 3 else 0.0
        sp_tj = BH.spearman(Mb, list(np.abs(tj))) if m >= 3 else 0.0
        coin = int(int(np.argmax(cj)) == int(np.argmax(Mb))) \
            if m else 0
        # ---- r297 census objects (anchors)
        nb = len(cb)
        nr = len(runs)
        d_rank = 0.0
        if nr > 1 and nb > 0:
            for i, (a, b, _s) in enumerate(runs[:-1]):
                d_rank = max(d_rank, abs(b / nb - (i + 1) / nr))
        mx = max(Mr) if Mr else 0.0
        sm = sum(Mr) if Mr else 0.0
        imb = nr * mx / max(sm, 1e-300)
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, nr=nr, Pb=Pb, Pw=Pw, Pd=Pd,
                    agg_dev=agg_dev, ker_dev=ker_dev, main=main,
                    T=T, dec_dev=dec_dev, tj=tj,
                    attr_dev=attr_dev, t_cross=t_cross,
                    comp_dev=comp_dev, lin_dev=lin_dev,
                    B=B_en, sp=sp, spec_dev=spec_dev,
                    pars_dev=pars_dev, e_lo=e_lo, e_mid=e_mid,
                    e_ed=e_ed, band_dev=band_dev, q50=q50,
                    q90=q90, mx2=sp["mx2"], et=et,
                    et_slack=et_slack, b1_slack=b1_slack,
                    d_delta=d_delta, D=D_diag, O=O_off,
                    pair_dev=pair_dev, P_ov=P_ov, P_fr=P_fr,
                    part_dev=part_dev, B_ov=B_ov, B_fr=B_fr,
                    B_x=B_x, en_dev=en_dev, cconv=cconv,
                    n_common=n_common, B_abs=B_abs,
                    abs_slack=abs_slack, g_lo=ga_lo, g_mid=ga_mid,
                    g_ed=ga_ed, sp_cj=sp_cj, sp_tj=sp_tj,
                    coin=coin, d_rank=d_rank, imb=imb)

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

    Ns = [rc["N"] for rc in recs]
    if not smoke:
        eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
        sl_c2 = L2D.halves_slope(Ns, eps_c2_rel)
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        sl_pref = L2D.halves_slope(Ns, pref)
        sf_rel = [rc["ev"]["S_F"] / (M_W * M_W) for rc in recs]
        sigma = L2D.halves_slope(Ns, sf_rel)
        sigma_star = 2.0 * (sl_c2 - DELTA_NEED) - sl_pref
        check("G22-r297-target-anchors",
              abs(sigma - R297_SIGMA) <= R297_SIGMA_TOL
              and abs(sigma_star - R297_SIGMA_STAR) <= R297_SSTAR_TOL
              and abs(sl_c2 - R297_SL_C2) <= R297_SL_C2_TOL
              and abs(sl_pref - R297_SL_PREF) <= R297_SL_PREF_TOL,
              "the r297 target-inequality set recomputed bit-near: "
              "sigma %+.3f (ref %+.3f), sigma* %+.3f (ref %+.3f), "
              "sl_c2 %+.3f (ref %+.3f), sl_pref %+.3f (ref %+.3f)"
              % (sigma, R297_SIGMA, sigma_star, R297_SIGMA_STAR,
                 sl_c2, R297_SL_C2, sl_pref, R297_SL_PREF))
        dr_med = float(np.median([rc["ev"]["d_rank"]
                                  for rc in recs]))
        dr_sl = L2D.halves_slope(Ns, [max(rc["ev"]["d_rank"],
                                          1e-300) for rc in recs])
        imb_sl = L2D.halves_slope(Ns, [rc["ev"]["imb"]
                                       for rc in recs])
        check("G23-r297-census-anchors",
              abs(dr_med - R297_DRANK_MED) <= R297_DRANK_TOL
              and abs(dr_sl - R297_DRANK_SL) <= R297_DRANK_SL_TOL
              and abs(imb_sl - R297_IMB_SL) <= R297_IMB_SL_TOL,
              "the r297 asset-2 census recomputed: D_rank med "
              "%.3f (ref %.3f) slope %+.2f (ref %+.2f), "
              "mass-imbalance slope %+.3f (ref %+.3f)"
              % (dr_med, R297_DRANK_MED, dr_sl, R297_DRANK_SL,
                 imb_sl, R297_IMB_SL))
    else:
        sigma = sigma_star = sl_c2 = sl_pref = float("nan")
        check("G22-r297-target-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G23-r297-census-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---- G24: r298 decomposition anchors
    dec_w = max(rc["ev"]["dec_dev"] for rc in pool_all)
    ker_w = max(max(rc["ev"]["ker_dev"], rc["ev"]["agg_dev"])
                for rc in pool_all)
    att_w = max(max(rc["ev"]["attr_dev"], rc["ev"]["comp_dev"])
                for rc in pool_all)
    lin_m = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] <= DEEP_N), default=0.0)
    lin_d = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] > DEEP_N), default=0.0)
    lin_c = max(crecs[c]["ev"]["lin_dev"] for c in crecs)
    rc9 = mrecs[0] if not smoke else recs[0]
    ov9 = len(np.intersect1d(rc9["bx"], rc9["xu"]))
    if not smoke:
        sh = [abs(rc["ev"]["T"]) / max(rc["ev"]["S_F"], 1e-300)
              for rc in recs]
        sh_med = float(np.median(sh))
        main_rel = [max(rc["ev"]["main"], 1e-300) / (M_W * M_W)
                    for rc in recs]
        sl_main = L2D.halves_slope(Ns, main_rel)
        absT_rel = [max(abs(rc["ev"]["T"]), 1e-300) / (M_W * M_W)
                    for rc in recs]
        sl_T = L2D.halves_slope(Ns, absT_rel)
        n_neg = sum(1 for rc in recs if rc["ev"]["T"] < 0.0)
        canc = [float(np.sum(np.abs(rc["ev"]["tj"])))
                / max(abs(rc["ev"]["T"]), 1e-300) for rc in recs]
        canc_med = float(np.median(canc))
        canc_sl = L2D.halves_slope(Ns, canc)
        tc_med = float(np.median([rc["ev"]["t_cross"]
                                  for rc in recs]))
        ok298 = (abs(sh_med - R298_SH_MED) <= R298_SH_TOL
                 and abs(sl_main - R298_SL_MAIN) <= R298_SL_MAIN_TOL
                 and abs(sl_T - R298_SL_T) <= R298_SL_T_TOL
                 and n_neg == 0
                 and abs(canc_med - R298_CANC_MED) <= R298_CANC_TOL
                 and abs(canc_sl - R298_CANC_SL) <= R298_CANC_SL_TOL
                 and abs(tc_med) <= R298_TC_ABS
                 and ov9 == R298_OVERLAP_W9)
        det298 = ("share med %.2f (ref %.2f), sl_MAIN %+.3f (ref "
                  "%+.3f), sl_|T| %+.3f (ref %+.3f), T<0 %d/42, "
                  "canc med %.2f sl %+.3f (ref %.2f/%+.3f), "
                  "tc med %+.2g, overlap w9 %d (ref %d)"
                  % (sh_med, R298_SH_MED, sl_main, R298_SL_MAIN,
                     sl_T, R298_SL_T, n_neg, canc_med, canc_sl,
                     R298_CANC_MED, R298_CANC_SL, tc_med, ov9,
                     R298_OVERLAP_W9))
    else:
        sh_med = sl_main = sl_T = float("nan")
        canc_med = canc_sl = tc_med = float("nan")
        n_neg = -1
        ok298 = (ov9 == R298_OVERLAP_W9)
        det298 = ("SMOKE: ladder anchors skipped; overlap w9 %d "
                  "(ref %d)" % (ov9, R298_OVERLAP_W9))
    v_o, v_i = VCP.fr_symbolic_sumrule()
    check("G24-r298-decomposition-anchors",
          dec_w <= DEC_BAR and ker_w <= KER_BAR
          and att_w <= ATTR_BAR and lin_m <= LIN_BAR
          and lin_d <= LIN_BAR_DEEP and lin_c <= LIN_BAR_CTRL
          and ok298 and v_o == 0 and v_i == 0,
          "the r298 record recomputed bit-near on %d worlds: "
          "identity dev %.1e (bar %.0e), kernel %.1e (bar %.0e), "
          "attribution %.1e (bar %.0e); linear window zero %.1e "
          "main / %.1e deep / %.1e controls; %s; r297 sum rule "
          "import devs %s/%s"
          % (len(pool_all), dec_w, DEC_BAR, ker_w, KER_BAR,
             att_w, ATTR_BAR, lin_m, lin_d, lin_c, det298,
             str(v_o), str(v_i)))

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    okA = True
    for P in FR_SEQS:
        b, _, _ = fr_abel_bound(P)
        okA &= (abs(sum(P)) <= b)
    b_toy, d_toy, v_toy = fr_abel_bound([Fr(2), Fr(-2), Fr(1)])
    okA &= (d_toy == 1 and v_toy == 2 and b_toy == 2)
    et2 = fr_et_pi2(halved=False)
    okA &= (et2["dev_abel"] == 0 and et2["worst_pos"] <= 0
            and et2["witness"] and et2["V"] == 9
            and et2["u2"] == 2 and et2["comp_ok"])
    check("G30-et-exact-section", okA,
          "the Erdos-Turan / Abel legs EXACT in Fractions: "
          "|sum P| <= D* x V on all %d frozen sequences (toy "
          "D* = 1, V = 2, bound 2 on (2,-2,1)); theta = pi/2 leg: "
          "Abel resummation identity dev %s, position bound "
          "|E_n|^2 <= 2 (worst slack %s) with the n = 1 EQUALITY "
          "witness, |u|^2 = %s <= max|E|^2 x V^2 = %s -- the "
          "position/mass factorization is exact algebra"
          % (len(FR_SEQS), str(et2["dev_abel"]),
             str(et2["worst_pos"]), str(et2["u2"]),
             str(2 * et2["V"] ** 2)))
    b_bad, _, _ = fr_abel_bound([Fr(1), Fr(1)], drop_terminal=True)
    et2m = fr_et_pi2(halved=True)
    check("G31-mustfail-m4-et-prefactors",
          b_bad == 0 and abs(Fr(2)) > b_bad
          and et2m["worst_pos"] == 1,
          "m4 ERDOS-TURAN PREFACTOR FAMILY (v964-S0 T4 anchor): "
          "(a) dropped-terminal mutant gives bound %s < 2 on "
          "P = (1, 1) -- CAUGHT; (b) halved position prefactor "
          "(claim |E_n|^2 <= 1) breaks at the equality witness "
          "by %s (2 > 1) -- CAUGHT: both factors are load-bearing"
          % (str(b_bad), str(et2m["worst_pos"])))
    toy_w, toy_f = toy_spectrum_pair_et()
    toy_w = max(toy_w, toy_overlap_exact())
    check("G32-toy-exactness", toy_w <= TOY_BAR
          and toy_f <= TOY_FFT_BAR,
          "the hand toys reproduce the WHOLE new pipeline: "
          "PDelta (1,-1,1) H 2 -> B = 1, pair D = 3 / O = -2, "
          "ET V = 5 (exact worst %.1e, bar %.0e); spectral "
          "recomposition == 1, Parseval == 3, band sum == B "
          "(FFT worst %.1e, bar %.0e); overlap toy border "
          "(0..4) + window (1.0, 2.5): P_ov (-2,0,0) / P_fr "
          "(3,-1,1), B_ov 4 + B_x -10 + B_fr 7 == 1, cconv 2 -- "
          "the components are LARGE against their sum"
          % (toy_w, TOY_BAR, toy_f, TOY_FFT_BAR))
    h_sd = scope_audit("spec_decomp", BOUND_FORBIDDEN)
    h_be = scope_audit("band_energies", BOUND_FORBIDDEN)
    h_et = scope_audit("et_factors", BOUND_FORBIDDEN)
    h_ps = scope_audit("pair_split", BOUND_FORBIDDEN)
    h_os = scope_audit("overlap_split", BOUND_FORBIDDEN)
    h_cc = scope_audit("cconv_census", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_sd or h_be or h_et or h_ps or h_os or h_cc)
    check("G33-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (spec_decomp, band_energies, "
          "et_factors, pair_split, overlap_split, cconv_census) "
          "consume block vectors / positions / weights only (no "
          "truth-side identifier in scope%s); m5a gift mutant "
          "FLAGGED (%s); m5b branch-peek mutant FLAGGED (%s); "
          "fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    m1_brk = toy_mustfail_m1()
    m3_shift, m3_silent, m3_cnt = toy_mustfail_m3()
    check("G34-mustfails-m1-m3", m1_brk >= MUT_MIN
          and abs(m1_brk - 2.0 / 3.0) <= 1e-12
          and m3_shift >= MUT_MIN and m3_cnt >= 1
          and m3_silent <= TOY_FFT_BAR,
          "m1 WRONG FEJER WEIGHT: the lag recomposition with "
          "(1 - |h|/(H+1)) breaks the toy identity by %.6f "
          "(= 2/3 exact) LOUD; m3 TOLERANT OVERLAP SPLIT (tol "
          "%.0e): component energy shift %.1f and count shift %d "
          "while BOTH splits recompose silently (dev %.1e) -- "
          "the exact-equality convention is load-bearing, the "
          "recomposition alone cannot catch it"
          % (m1_brk, TOL_MUT, m3_shift, int(m3_cnt), m3_silent))

    # ---------------- S4: Leg A -- the frequency anatomy
    section("S4  LEG A: SPECTRUM MAP (FREQUENCY ANATOMY OF DELTA)")
    spec_w = max(rc["ev"]["spec_dev"] for rc in pool_all)
    pars_w = max(rc["ev"]["pars_dev"] for rc in pool_all)
    band_w = max(rc["ev"]["band_dev"] for rc in pool_all)
    abs_w = max(rc["ev"]["abs_slack"] for rc in pool_all)
    check("G40-spectral-wards", spec_w <= SPEC_BAR
          and pars_w <= SPEC_BAR and band_w <= SPEC_BAR
          and abs_w <= SPEC_BAR,
          "the exact spectral representation on %d worlds: "
          "recomposition (1/L) sum F |Dhat|^2 == B worst %.1e; "
          "Parseval mean == sum PDelta^2 worst %.1e; band sum == "
          "B worst %.1e; magnitude majorization B <= B_abs slack "
          "%.1e (all bars %.0e) -- the h-decomposition of the "
          "frozen kernel is an exact finite identity"
          % (len(pool_all), spec_w, pars_w, band_w, abs_w,
             SPEC_BAR))
    if not smoke:
        shl = [rc["ev"]["e_lo"] / max(rc["ev"]["B"], 1e-300)
               for rc in recs]
        shm = [rc["ev"]["e_mid"] / max(rc["ev"]["B"], 1e-300)
               for rc in recs]
        she = [rc["ev"]["e_ed"] / max(rc["ev"]["B"], 1e-300)
               for rc in recs]
        shl_med = float(np.median(shl))
        shm_med = float(np.median(shm))
        she_med = float(np.median(she))
        sl_lo = L2D.halves_slope(Ns, [max(rc["ev"]["e_lo"], 1e-300)
                                      / (M_W * M_W) for rc in recs])
        sl_mid = L2D.halves_slope(
            Ns, [max(rc["ev"]["e_mid"], 1e-300) / (M_W * M_W)
                 for rc in recs])
        sl_ed = L2D.halves_slope(
            Ns, [max(rc["ev"]["e_ed"], 1e-300) / (M_W * M_W)
                 for rc in recs])
        sl_mean = L2D.halves_slope(
            Ns, [max(rc["ev"]["D"], 1e-300) / (M_W * M_W)
                 for rc in recs])
        sl_mx = L2D.halves_slope(
            Ns, [max(rc["ev"]["mx2"], 1e-300) / (M_W * M_W)
                 for rc in recs])
        q50_med = float(np.median([rc["ev"]["q50"]
                                   for rc in recs]))
        q90_med = float(np.median([rc["ev"]["q90"]
                                   for rc in recs]))
        if shl_med >= LOWPASS_BAR:
            band_tag = "LOWPASS"
        elif shl_med < BROAD_BAR:
            band_tag = "BROADBAND"
        else:
            band_tag = "MIXED_BAND"
        check("G41-spectrum-map", True,
              "SPECTRUM_MAP (42 rungs): band shares LOW/MID/EDGE "
              "med %.2f/%.2f/%.2f; band-energy slopes %+.3f/"
              "%+.3f/%+.3f; mean |Dhat|^2 slope %+.3f (== the B2 "
              "diagonal, Parseval), max slope %+.3f; q50 med "
              "%.2f / q90 med %.2f main-lobe units; SEALED TAG: "
              "%s (LOWPASS iff LOW med >= %.2f, BROADBAND iff < "
              "%.2f)"
              % (shl_med, shm_med, she_med, sl_lo, sl_mid, sl_ed,
                 sl_mean, sl_mx, q50_med, q90_med, band_tag,
                 LOWPASS_BAR, BROAD_BAR))
    else:
        shl_med = shm_med = she_med = float("nan")
        sl_lo = sl_mid = sl_ed = sl_mean = sl_mx = float("nan")
        q50_med = q90_med = float("nan")
        band_tag = "SMOKE"
        check("G41-spectrum-map", True, "SMOKE: skipped")

    # ---------------- S5: Leg B -- the derivation routes
    section("S5  LEG B: THE DECAY DERIVATION ROUTES")
    et_w = max(rc["ev"]["et_slack"] for rc in pool_all)
    b1_w = max(rc["ev"]["b1_slack"] for rc in pool_all)
    check("G50-b1-et-wards", et_w <= ET_BAR and b1_w <= ET_BAR,
          "B1 ERDOS-TURAN wards on %d worlds: per-frequency "
          "|Dhat| <= Dpos x V slack %.1e (rel sum|PDelta|); "
          "composed B <= V^2 x Phi_pos slack %.1e (rel B) -- "
          "the position/mass factorization holds exactly, "
          "world-blind by the same algebra (bars %.0e)"
          % (len(pool_all), et_w, b1_w, ET_BAR))
    pair_w = max(rc["ev"]["pair_dev"] for rc in pool_all)
    check("G52-b2-pair-ward", pair_w <= PAIR_BAR,
          "B2 PAIR ward on %d worlds: B == D + O exact (worst "
          "%.1e of scale, bar %.0e) -- diagonal magnitudes vs "
          "signed off-diagonal, nothing through |.|"
          % (len(pool_all), pair_w, PAIR_BAR))
    part_w = max(rc["ev"]["part_dev"] for rc in pool_all)
    en_w = max(rc["ev"]["en_dev"] for rc in pool_all)
    check("G53-b3-overlap-wards", part_w <= PART_BAR
          and en_w <= EN_BAR,
          "B3 OVERLAP wards on %d worlds: P_ov + P_fr == PDelta "
          "exact (worst %.1e rel max|PDelta|, bar %.0e); energy "
          "recomposition B_ov + B_x + B_fr == B (worst %.1e of "
          "the component scale, bar %.0e) -- the exact-equality "
          "partition is an identity"
          % (len(pool_all), part_w, PART_BAR, en_w, EN_BAR))
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d H %-2d  B %.2e  sh_low "
             "%.2f  D %.2e  O %+.2e  s_ov %+.2f  cconv %.2f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g_branch"] < 0 else "chp",
                ev["m"], ev["H"], ev["B"], ev["e_lo"]
                / max(ev["B"], 1e-300), ev["D"], ev["O"],
                ev["B_ov"] / max(ev["B"], 1e-300), ev["cconv"]))
    if not smoke:
        # ---- B1 census
        sl_phi = L2D.halves_slope(Ns, [max(rc["ev"]["et"]["phi"],
                                           1e-300) for rc in recs])
        v2_rel = [max(rc["ev"]["et"]["V"], 1e-300) ** 2
                  / (M_W * M_W) for rc in recs]
        sl_v2 = L2D.halves_slope(Ns, v2_rel)
        bd_rel = [max(rc["ev"]["et"]["bound"], 1e-300)
                  / (M_W * M_W) for rc in recs]
        sl_bd = L2D.halves_slope(Ns, bd_rel)
        add_dev = abs(sl_bd - sl_phi - sl_v2)
        dd_med = float(np.median([rc["ev"]["d_delta"]
                                  for rc in recs]))
        dd_sl = L2D.halves_slope(Ns, [max(rc["ev"]["d_delta"],
                                          1e-300) for rc in recs])
        need_mass = sigma_star - sl_phi
        mass_met = sl_v2 <= need_mass
        check("G51-b1-census", add_dev <= ADD_BAR,
              "B1 census: sl_pos = slope(Phi_pos) %+.3f, sl_mass "
              "= slope(V^2/M^2) %+.3f, composed %+.3f (additivity "
              "dev %.1e, bar %.0e) vs sigma* %+.3f -- composed "
              "%s; MASS_TARGET_FROZEN: needed slope(V^2/M^2) <= "
              "sigma* - sl_pos = %+.3f, measured %+.3f -- %s; "
              "D_rank(Delta) med %.3f slope %+.2f (the Delta "
              "support%s)"
              % (sl_phi, sl_v2, sl_bd, add_dev, ADD_BAR,
                 sigma_star,
                 "MEETS the target" if sl_bd <= sigma_star
                 else "FAILS by %.3f" % (sl_bd - sigma_star),
                 need_mass, sl_v2,
                 "MET" if mass_met
                 else "NOT MET by %.3f" % (sl_v2 - need_mass),
                 dd_med, dd_sl,
                 " inherits the falling equidistribution"
                 if dd_sl < 0 else ": discrepancy NOT falling"))
        # ---- B2 census
        sl_D = L2D.halves_slope(Ns, [max(rc["ev"]["D"], 1e-300)
                                     / (M_W * M_W) for rc in recs])
        sl_absO = L2D.halves_slope(
            Ns, [max(abs(rc["ev"]["O"]), 1e-300) / (M_W * M_W)
                 for rc in recs])
        n_On = sum(1 for rc in recs if rc["ev"]["O"] < 0.0)
        ratio = [rc["ev"]["B"] / max(rc["ev"]["D"], 1e-300)
                 for rc in recs]
        rat_med = float(np.median(ratio))
        sl_rat = L2D.halves_slope(Ns, [max(v, 1e-300)
                                       for v in ratio])
        od_med = float(np.median([rc["ev"]["O"]
                                  / max(rc["ev"]["D"], 1e-300)
                                  for rc in recs]))
        check("G54-b2-census", True,
              "B2 census: sl_D %+.3f (the diagonal density; "
              "sigma* %+.3f: %s), sl_|O| %+.3f, O < 0 on %d/42 "
              "(crossref r287: the border-P blocks REINFORCE on "
              "39/44 -- PDelta measured here, not assumed), O/D "
              "med %+.2f, ratio B/D med %.2f slope %+.3f (grow "
              "bar %+.2f: %s)"
              % (sl_D, sigma_star,
                 "MEETS" if sl_D <= sigma_star else
                 "FAILS by %.3f" % (sl_D - sigma_star),
                 sl_absO, n_On, od_med, rat_med, sl_rat,
                 RATIO_GROW,
                 "flat enough" if sl_rat <= RATIO_GROW else
                 "GROWS by %.3f over bar" % (sl_rat - RATIO_GROW)))
        # ---- B3 census
        s_ov = [rc["ev"]["B_ov"] / max(rc["ev"]["B"], 1e-300)
                for rc in recs]
        s_fr = [rc["ev"]["B_fr"] / max(rc["ev"]["B"], 1e-300)
                for rc in recs]
        s_x = [rc["ev"]["B_x"] / max(rc["ev"]["B"], 1e-300)
               for rc in recs]
        sov_med = float(np.median(s_ov))
        sfr_med = float(np.median(s_fr))
        sx_med = float(np.median(s_x))
        sxa_med = float(np.median([abs(v) for v in s_x]))
        cc_med = float(np.median([rc["ev"]["cconv"]
                                  for rc in recs]))
        cc_sl = L2D.halves_slope(Ns, [max(rc["ev"]["cconv"],
                                          1e-300) for rc in recs])
        full_ov = sum(1 for rc in recs
                      if rc["ev"]["n_common"] == len(rc["bx"])
                      == len(rc["xu"]))
        if sov_med >= OV_DOM_BAR and sxa_med <= XA_BAR:
            b3_class = "OV_DOM"
        elif sfr_med >= OV_DOM_BAR and sxa_med <= XA_BAR:
            b3_class = "FR_DOM"
        else:
            b3_class = "MIXED_OVERLAP"
        check("G55-b3-census", True,
              "B3 census: energy shares ov/x/fr med %+.2f/%+.2f/"
              "%+.2f (|x| med %.2f); SEALED class %s (OV_DOM iff "
              "ov >= %.2f and |x| <= %.2f); FULL-SUPPORT overlap "
              "(the unions share EVERY position) on %d/42 rungs; "
              "c-convergence census at the shared positions: "
              "cconv med %.2f slope %+.3f -- %s"
              % (sov_med, sx_med, sfr_med, sxa_med, b3_class,
                 OV_DOM_BAR, XA_BAR, full_ov, cc_med, cc_sl,
                 "the c-values converge (falling)" if cc_sl < 0
                 else "the c-values do NOT converge"))
    else:
        sl_phi = sl_v2 = sl_bd = need_mass = float("nan")
        dd_med = dd_sl = float("nan")
        mass_met = False
        sl_D = sl_absO = rat_med = sl_rat = od_med = float("nan")
        n_On = -1
        sov_med = sfr_med = sx_med = sxa_med = float("nan")
        cc_med = cc_sl = float("nan")
        b3_class = "SMOKE"
        check("G51-b1-census", True, "SMOKE: skipped")
        check("G54-b2-census", True, "SMOKE: skipped")
        check("G55-b3-census", True, "SMOKE: skipped")

    # ---------------- S6: sealed decay adjudication + Leg C
    section("S6  SEALED DECAY ADJUDICATION + LEG C")
    if not smoke:
        b1_valid = (et_w <= ET_BAR and b1_w <= ET_BAR)
        b2_valid = (pair_w <= PAIR_BAR)
        b3_valid = (part_w <= PART_BAR and en_w <= EN_BAR)
        b1_ok = b1_valid and (sl_phi + sl_v2) <= sigma_star
        b2_ok = (b2_valid and sl_D <= sigma_star
                 and sl_rat <= RATIO_GROW)
        b3_ok = b3_valid and b3_class == "OV_DOM"
        derived = (b1_valid and sl_phi <= sigma_star
                   and sl_v2 <= MASS_FLAT)
        if derived:
            outcome = "DECAY_DERIVED"
        elif b1_ok or b2_ok or b3_ok:
            outcome = "DECAY_SPLIT"
        else:
            outcome = "DECAY_STILL_EMPIRICAL"
        fired = []
        if b1_ok:
            fired.append("B1(MASS_TARGET: slope(V^2/M^2) <= "
                         "%+.3f, measured %+.3f)"
                         % (need_mass, sl_v2))
        if b2_ok:
            fired.append("B2(DIAG_TARGET: prove sl_D <= sigma* "
                         "(measured %+.3f) + ratio flatness "
                         "(measured %+.3f))" % (sl_D, sl_rat))
        if b3_ok:
            fired.append("B3(CVALUE_TARGET: prove the c-value "
                         "convergence rate, cconv slope %+.3f)"
                         % cc_sl)
        check("G60-decay-adjudication", True,
              "SEALED RULE fired: %s (B1_OK %s: composed %+.3f "
              "vs sigma* %+.3f; B2_OK %s: sl_D %+.3f vs sigma*, "
              "ratio slope %+.3f vs %+.2f; B3_OK %s: class %s; "
              "DERIVED clause: sl_pos %+.3f <= sigma* %s AND "
              "sl_mass %+.3f <= %.1f %s)%s"
              % (outcome, b1_ok, sl_phi + sl_v2, sigma_star,
                 b2_ok, sl_D, sl_rat, RATIO_GROW, b3_ok,
                 b3_class, sl_phi,
                 "TRUE" if sl_phi <= sigma_star else "FALSE",
                 sl_v2, MASS_FLAT,
                 "TRUE" if sl_v2 <= MASS_FLAT else "FALSE",
                 ("; fired: " + " | ".join(fired)) if fired
                 else ""))
        if outcome != "DECAY_STILL_EMPIRICAL":
            hyp = ("" if derived else
                   " + the frozen rest hypothesis(es) [" +
                   " | ".join(fired) + "]")
            info("CANDIDATE THEOREM (Fejer decay composition, L2 "
                 "generic half): for every rung of the sealed "
                 "ladder (N in [%d, %d], H = ceil(sqrt(m))): the "
                 "Leg-B exact bound%s => sigma <= sigma* = %+.3f "
                 "=> the r297 target inequality => the v964-S0 "
                 "vdC theorem => delta' > %.2f on the generic "
                 "half; exceptions: 6 via the r287 F2 "
                 "certificates, kz15 via the r270 exact-finite "
                 "certificate.  Wave-9 promotion candidate -- "
                 "NOT promoted here."
                 % (min(Ns), max(Ns), hyp, sigma_star,
                    DELTA_NEED))
            legc = True
        else:
            info("Leg C VOID without substitute (outcome %s). "
                 "The measured common obstruction is documented "
                 "in the verdict." % outcome)
            legc = False
        check("G61-leg-c", True,
              "Leg C %s -- fires ONLY on DECAY_DERIVED or "
              "DECAY_SPLIT (frozen rest as explicit hypothesis) "
              "by the sealed rule; no post-hoc rescue"
              % ("FIRED (candidate printed, NOT promoted)"
                 if legc else "VOID"))
    else:
        outcome = "SMOKE_NO_ADJUDICATION"
        fired = []
        b1_ok = b2_ok = b3_ok = False
        check("G60-decay-adjudication", True, "SMOKE: skipped")
        check("G61-leg-c", True, "SMOKE: skipped")

    # ---------------- S7: Leg D -- the cancellation locus table
    section("S7  LEG D: IN-T CANCELLATION LOCUS (ONE TABLE)")
    if not smoke:
        gl = []
        gm = []
        ge = []
        for rc in recs:
            ev = rc["ev"]
            G = max(ev["B_abs"] - ev["B"], 1e-300)
            gl.append((ev["g_lo"] - ev["e_lo"]) / G)
            gm.append((ev["g_mid"] - ev["e_mid"]) / G)
            ge.append((ev["g_ed"] - ev["e_ed"]) / G)
        gl_med = float(np.median(gl))
        gm_med = float(np.median(gm))
        ge_med = float(np.median(ge))
        spcj_med = float(np.median([rc["ev"]["sp_cj"]
                                    for rc in recs]))
        sptj_med = float(np.median([rc["ev"]["sp_tj"]
                                    for rc in recs]))
        n_coin = sum(rc["ev"]["coin"] for rc in recs)
        check("G70-canc-locus-table", True,
              "CANC_LOCUS (no interpretation): gap G = B_abs - B "
              "band shares LOW/MID/EDGE med %.2f/%.2f/%.2f vs "
              "energy B shares %.2f/%.2f/%.2f; block side: "
              "sp(Mb, c_j = |t_j| - t_j) med %+.2f, argmax "
              "coincidence %d/42; r298 anchor sp(Mb, |t_j|) med "
              "%+.2f"
              % (gl_med, gm_med, ge_med, shl_med, shm_med,
                 she_med, spcj_med, n_coin, sptj_med))
    else:
        gl_med = gm_med = ge_med = float("nan")
        spcj_med = sptj_med = float("nan")
        n_coin = -1
        check("G70-canc-locus-table", True, "SMOKE: skipped")

    # ---- world-control classes (disclosed, never a failure)
    if not smoke:
        o_main = "O_NEG" if n_On > 21 else "O_POS"
        ctl_note = []
        world_blind = True
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            sh_c = ev["e_lo"] / max(ev["B"], 1e-300)
            if sh_c >= LOWPASS_BAR:
                tag_c = "LOWPASS"
            elif sh_c < BROAD_BAR:
                tag_c = "BROADBAND"
            else:
                tag_c = "MIXED_BAND"
            so_c = ev["B_ov"] / max(ev["B"], 1e-300)
            sf_c = ev["B_fr"] / max(ev["B"], 1e-300)
            sx_c = abs(ev["B_x"]) / max(ev["B"], 1e-300)
            if so_c >= OV_DOM_BAR and sx_c <= XA_BAR:
                cl3 = "OV_DOM"
            elif sf_c >= OV_DOM_BAR and sx_c <= XA_BAR:
                cl3 = "FR_DOM"
            else:
                cl3 = "MIXED_OVERLAP"
            osgn = "O_NEG" if ev["O"] < 0 else "O_POS"
            ctl_note.append("%s %s/%s/%s" % (c, tag_c, osgn, cl3))
            world_blind &= (tag_c == band_tag and osgn == o_main
                            and cl3 == b3_class)
        check("G71-world-controls", True,
              "the control classes (same sealed rules at the "
              "single control rung): MAIN %s/%s/%s vs %s -- %s "
              "(a class break is a disclosed finding, not a "
              "gate failure; the identities are world-blind by "
              "the same algebra, G40/G50-G53)"
              % (band_tag, o_main, b3_class,
                 str(ctl_note),
                 "WORLD-BLIND" if world_blind
                 else "WORLD_SENSITIVE (disclosed)"))
    else:
        world_blind = True
        ctl_note = []
        o_main = "n/a"
        check("G71-world-controls", True, "SMOKE: skipped")

    # ---------------- S8: mustfail m2 + anchors + mp wards
    section("S8  MUSTFAIL M2 + ANCHORS + MP WARDS")
    m2_pool = mrecs + ([recs[0]] if smoke else [])
    m2_vals = []
    for rc in m2_pool:
        ev = rc["ev"]
        m2_vals.append((rc["kz"],
                        (ev["B_abs"] - ev["B"])
                        / max(ev["B"], 1e-300)))
    m2_min = min(v for _k, v in m2_vals)
    check("G80-mustfail-m2", m2_min >= MUT_MIN,
          "m2 MAGNITUDE PAIR ROUTE (|PDelta| instead of PDelta): "
          "B(|PDelta|,|PDelta|) differs from B by %s of B (all "
          ">= %.0e) LOUD; toy 5 vs 1 (break 4 exact) -- the "
          "pair phase of the signed block field is load-bearing; "
          "any |.|-spectrum loses the object"
          % ("; ".join("w%d %.1e" % (k, v) for k, v in m2_vals),
             MUT_MIN))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    evS = crecs["SMOOTH"]["ev"]
    okSd = (evS["spec_dev"] <= SPEC_BAR
            and evS["pair_dev"] <= PAIR_BAR
            and evS["en_dev"] <= EN_BAR)
    check("G81-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSd,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "every exact ward holds trivially on the self-aliased "
          "source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSd else "BROKEN"))
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
        check("G82-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G82-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact spectral decomposition of the Delta "
          "Fejer energy, the three-route decay derivation census "
          "with exact wards, the sealed three-way adjudication, "
          "the frozen MASS_TARGET rest inequality and the Leg-D "
          "locus table -- NO new certificate promoted, NO bound "
          "modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["SPECTRUM_MAP(LOW/MID/EDGE med %.2f/%.2f/%.2f, "
                 "band slopes %+.3f/%+.3f/%+.3f, mean sl %+.3f, "
                 "max sl %+.3f, q50 %.2f / q90 %.2f lobes, %s)"
                 % (shl_med, shm_med, she_med, sl_lo, sl_mid,
                    sl_ed, sl_mean, sl_mx, q50_med, q90_med,
                    band_tag)]
        parts.append("ROUTE_TABLE(B1 valid 47/47 sl_pos %+.3f "
                     "sl_mass %+.3f composed %+.3f vs sigma* "
                     "%+.3f; B2 valid 47/47 sl_D %+.3f sl_|O| "
                     "%+.3f O<0 %d/42 B/D med %.2f sl %+.3f; B3 "
                     "valid 47/47 shares %+.2f/%+.2f/%+.2f cconv "
                     "med %.2f sl %+.3f class %s)"
                     % (sl_phi, sl_v2, sl_bd, sigma_star, sl_D,
                        sl_absO, n_On, rat_med, sl_rat, sov_med,
                        sx_med, sfr_med, cc_med, cc_sl, b3_class))
        parts.append("MASS_TARGET(needed slope(V^2/M^2) <= %+.3f,"
                     " measured %+.3f: %s)"
                     % (need_mass, sl_v2,
                        "MET" if mass_met else "NOT MET by %.3f"
                        % (sl_v2 - need_mass)))
        if outcome == "DECAY_DERIVED":
            parts.append("DECAY_DERIVED(B1: sl_pos %+.3f <= "
                         "sigma* and sl_mass %+.3f <= 0)"
                         % (sl_phi, sl_v2))
            parts.append("CANDIDATE_THEOREM(printed in S6, "
                         "wave-9 candidate NOT promoted)")
        elif outcome == "DECAY_SPLIT":
            parts.append("DECAY_SPLIT(%s)" % " | ".join(fired))
            parts.append("CANDIDATE_THEOREM(conditional, printed "
                         "in S6, wave-9 candidate NOT promoted)")
        else:
            parts.append("DECAY_STILL_EMPIRICAL(measured common "
                         "obstruction: B1 pays the growing "
                         "position/kernel factor sl_pos %+.3f; "
                         "B2 diagonal sl_D %+.3f %s sigma* but "
                         "ratio B/D slope %+.3f %s the %+.2f "
                         "grow bar; B3 class %s)"
                         % (sl_phi, sl_D,
                            "MEETS" if sl_D <= sigma_star
                            else "FAILS",
                            sl_rat,
                            "within" if sl_rat <= RATIO_GROW
                            else "over", RATIO_GROW, b3_class))
        parts.append("CANC_LOCUS(G bands %.2f/%.2f/%.2f vs B "
                     "%.2f/%.2f/%.2f; sp(Mb, c_j) med %+.2f, "
                     "coincidence %d/42; sp(Mb, |t_j|) med %+.2f)"
                     % (gl_med, gm_med, ge_med, shl_med, shm_med,
                        she_med, spcj_med, n_coin, sptj_med))
        if not world_blind:
            parts.append("WORLD_SENSITIVE(MAIN %s/%s/%s vs %s -- "
                         "disclosed finding)"
                         % (band_tag, o_main, b3_class,
                            str(ctl_note)))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the spectral "
          "representation, the ET factorization, the pair split, "
          "the overlap partition, the Fractions ET section (all "
          "world-blind); MEASURED: every slope, share, class and "
          "locus stat (42 rungs only); OPEN: the decay derivation "
          "beyond the named rest object(s), the cofinal step H5, "
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
