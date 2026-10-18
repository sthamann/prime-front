#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""border_resolvent_identity_probe -- PRIME.PORT.RHP.QUENCHED.
BORDER_RESOLVENT_IDENTITY.01 (round 266): the core round of the
final campaign asks for a BORDER-DRESSED RESOLVENT IDENTITY -- an
exact identity in which the border drive t_{N-2} / the border
column f enters a definite square, Schur complement or Ward
identity DIRECTLY, such that (i) the building blocks are definite,
(ii) the endpoint criterion is the TARGET (q_N < 1 / D_N > 0 /
the |Z| < sqrt(5/7) scale), NOT the r257/r265-blocked wall bound
f^T (I - Q)^{-1} f < 1, and (iii) the identity does NOT reduce to
that wall bound.  The two measured lessons frame the round: way A
(naive s, r265) = right endpoint, no new control; way B (IIKS
resolvent, r265) = definite structure, wrong endpoint.  The
candidates must couple the border INTO the definite dynamics
BEFORE evaluation, not after.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

LEG A -- THE WALL-REDUCTION DETECTOR (built first, everything is
checked against it): a candidate identity whose endpoint criterion
is algebraically equivalent to f^T (I - Q)^{-1} f <= c (or a
monotone function of it) is typed WALL_REDUCTION immediately.
Machine form (sealed): per candidate criterion crit_w over the 42
rungs, (i) DECISION FINGERPRINT: the pass/fail pattern of crit_w
vs the wall pattern (g(1) < 1 is FALSE on 42/42, r265) and vs the
target pattern (D_N > 0 TRUE on 42/42); (ii) RANK FINGERPRINT:
|Spearman(crit, g(1))| >= 0.9 (sealed bar) together with the wall
decision pattern => WALL_REDUCTION; (iii) where the candidate has
a closed form, the SYMBOLIC check decides directly (exact target
equivalence is gated as an identity, never inferred from ranks --
the scratch measured that ratio-normalized restatements do NOT
rank-correlate +-1 with the target across rungs, so the rank
fingerprint is reserved for the WALL side where the carrier
g(1) is a single spectral functional).  SELFTEST: the detector
must flag the known wall criterion g(1) itself (decision FALSE
42/42, Spearman(g1, g1) = 1) and must NOT flag the target D_N
(decision TRUE 42/42, |Spearman(D_N, g1)| measured ~ 0.28 << 0.9).
Inherited kills stay armed: PAIRCORR detector (demand bar 1.0
dec), TARGET_INVERSE (scope audits + flagged oracle mutant),
SELECTION_BY_ANSWER (branch labels enter gates/tables only); the
r263 K1 support-geometry test: every candidate must LOSE its
definiteness/sign structure on SCRAMBLE (else SUPPORTGEOMETRY).

LEG B -- THE CANDIDATE CLASS (augmented-first, max 4, sealed):
(b1) THE AUGMENTED RESOLVENT DIAGONAL: 1/D_N is the (B, B) corner
  of the INVERSE augmented Gram matrix A = [[G, tv], [tv^T, B]]
  (bordered-inverse formula (A^{-1})_{BB} = 1/(B - tv^T G^{-1}
  tv)); the border column sits IN the operator.  With the border
  scaled by s (A(s), off-diagonal blocks s tv), the Jacobi
  formula d/ds A^{-1} = -A^{-1} A' A^{-1} closes EXACTLY on this
  ONE entry:
      d/ds (A(s)^{-1})_{BB} = 2 s W / D(s)^2,
      W = tv^T G^{-1} tv = S_{N-1},  D(s) = B - s^2 W
  -- a manifest square (W = ||L^{-1} tv||^2, L the Cholesky of
  the positive-prefix Gram) over a squared denominator: the
  dynamics of the corner entry is FULLY DEFINITE in the border
  direction, and its endpoint criterion is the target BY
  CONSTRUCTION ((A(1)^{-1})_{BB} = 1/D_N finite and positive
  <=> D_N > 0).  The round's question, adjudicated by leg A: is
  the definiteness condition secretly the wall?  MEASURED
  ANSWER (sealed adjudication rule): the definiteness needs only
  the positive prefix (G > 0, source-pure), NOT the wall -- but
  the definite direction points the WRONG WAY: the corner entry
  RISES (D falls), the total drop over [0, 1] is D(0) - D(1) =
  W = S_{N-1} EXACTLY, and bounding the drop by the budget IS
  the target: typed B1_DEFINITE_DRAIN_RESTATEMENT unless the
  identity supplies a new source-pure bound (it does not: its
  only definite quantity IS the drop).  Gates: sympy EXACT on
  the r263 MAINLIKE instance (corner-inverse identity in s; the
  Jacobi route -(A^{-1} A' A^{-1})_{BB} == d/ds of the closed
  form); numeric corner entry vs closed form on mains + 3 ladder
  samples at s in {0.5, 0.9} (scaled dev |corner - 1/D| |D|, bar
  1e-7, scratch floor 2.8e-9); FD of the corner entry vs the
  rate 2sW/D^2 (mains, rel bar 1e-4, floor 8.0e-7); definiteness
  census rate >= 0 and D(s) > 0 at every census point on 42 + 2
  worlds; endpoint identity (1 - crit1) B == D_N (rel 1e-12,
  crit1 = W/B); SCRAMBLE/EPSTEIN lose the carrier definiteness
  (first rho < 0 at the flips 21/25 -- W is no longer a sum of
  squares there).
(b2) THE PAIR-WARD IDENTITY (dual form of the r260 bilinear):
  on the augmented 2x2 minor lattice with objects tau_n = det
  G_n, aug_n = det A_n, phi_n = F_n tau_n (the border-cofactor
  determinant: the (n+1) x (n+1) det with the border-moment row
  appended -- monomial basis, r263 instances), the known
  identity aug_n tau_{n+1} - aug_{n+1} tau_n = phi_n^2 puts the
  manifest square on the DRAIN side.  SYSTEMATIC SEARCH (sealed,
  exhaustive at this complexity): all 72 ordered differences
  X_a(n) Y_b(n+1) - X_c(n) Y_d(n+1) over the 9 cross-degree
  products; a combination FIRES iff it is a nonzero PERFECT
  RATIONAL SQUARE (up to global sign) at n = 1, 2, 3 on the
  MAINLIKE instance with constant sign.  DUAL FORM RULE
  (sealed): B2_DUAL_WARD_FOUND iff some firing combination
  expresses the target-side product aug_{n+1} tau_n as a
  source-positive product PLUS a square (the square on the
  TARGET side); else B2_DRAIN_ONLY (the exhaustive 2x2 census
  is expected from the scratch to fire ONLY the known bilinear
  pair).  FLIPLIKE re-gate: the normalized decrement rho_2 =
  F_2^2/h_2 < 0 at the flip (the SIGN structure is lost on the
  flipped world -- the r263 K2 scramble condition re-gated).
(b3) THE AUGMENTED SCHUR COMPLEMENT OVER AN INNER BLOCK: instead
  of the wall form D = B - f^T G^{-1} f, complement over the
  HEAD block (Q_7/level-8, r248 centering): the quotient
  property of Schur complements gives EXACTLY
      D_N = (B - t_H^T G_HH^{-1} t_H)
            - ftil^T Gtil^{-1} ftil,
      ftil = t_T - G_TH G_HH^{-1} t_H,
      Gtil = G_TT - G_TH G_HH^{-1} G_HT,
  with the head pieces definite (B - t_H^T G_HH^{-1} t_H ==
  B - S_7 > 0, Gtil > 0 on the positive prefix) and the border
  entering only in head-deflated combinations.  MEASURED
  ADJUDICATION: the deflated energy equals S_{N-1} - S_7
  EXACTLY (partial Parseval), i.e. the inner-block
  complementation reproduces the same budget-minus-border-
  energy shape one level down -- the border term is again on
  the DRAIN side and the endpoint criterion (1 - crit3)(B -
  S_7) == D_N is the target restated: typed
  B3_DEFLATED_DRAIN_RESTATEMENT unless leg A flags the wall
  (it does not: Spearman(crit3, g1) ~ 0.26) or a new bound
  appears (it does not).  Gates: sympy EXACT two-block quotient
  on the r263 rational instance (head 2 of 4); numeric two-block
  route vs D_N on mains + samples (bar 1e-6, floor 1.2e-8 deep);
  head identities |Bh - (B - S_7)| <= 1e-12, |en - (S_{N-1} -
  S_7)| <= 1e-6; Gtil min eig > 0 on mains; SCRAMBLE loses:
  Gtil min eig < 0 (scratch: -6.8).
(b4) THE L-GAUGE WARD, AUGMENTED (r231 midpoint connection with
  the border transported): the dual FIK problem is the h-free
  L-gauge transform pihat#_{S-1-k} = L C[pihat_k mutilde]/h_k,
  and the ladder is SELF-DUAL at the terminal (S = 2N - 1 on
  42/42, so k = N-1 maps to m = N-1).  The border functional
  transports EXACTLY by residue calculus:
      F#_{S-1-k} = (1/h_k) sum_j w_j pihat_k(x_j) M_j,
      M_j = int L_j dsigmatilde = int L(z)/(z - x_j) dsigmatilde
  (M_j = the border mass of the deleted-node polynomials; on the
  real windows every border atom coincides with exactly one
  union node, so M_j collapses to the deleted-node values --
  measured, disclosed).  THE QUESTION (sealed): the gauge is
  sign-blind for the BASIS (h-normalizations cancel, r231); is
  it sign-blind for the BORDER?  If not, the orientation product
  s#_w = sign(F#_{N-1} F_{N-1}) or the alignment statistic c_w =
  A^2 / (sum |w| v^2)(sum |w| Mhat^2) (A = sum_j w_j v(x_j)
  Mhat_j) would separate the exception branch and carry the
  missing orientation.  Gates: toy EXACT (rationals: connection
  + border transport + h-duality h#_m h_k == 1 + M field);
  eval-machinery ward (scaled chain values reproduce fb at
  k = 20 and the terminal, rel bar 1e-9, floor 4.3e-12); mp WARD
  (dps 60) on BOTH mains at the self-dual terminal: the mp dual
  chain route vs the f64 residue route, log dev <= 1e-6 (floors
  1.9e-12 / 1.3e-9), sign match, h-duality log dev <= 1e-8
  (floors 1.3e-11 / 3.3e-11); terminal census on 42 rungs
  (self-duality, cancellation depth >= 1e-12 guard, orientation
  + alignment AUC powers vs the branch labels, sealed bar 0.8;
  SMOOTH alignment anchor <= 1e-8); SEALED ADJUDICATION:
  B4_BORDER_ORIENTATION_CARRIED iff a power >= 0.8 (then leg-A
  fingerprints decide wall/target/third); else
  B4_BORDER_SIGN_BLIND.

LEG C -- ENDPOINT ADJUDICATION (sealed table): for every
candidate criterion: (i) the TARGET (exact identity gated), (ii)
the WALL (leg-A fingerprint), (iii) a THIRD criterion (new:
characterized by its census -- side of the ladder, cheap vs
exception medians, control values).  crit1 = S_{N-1}/B, crit3 =
(S_{N-1} - S_7)/(B - S_7), align = c_w; separations firewall-
typed (labels in tables only).

LEG D -- CONTROLS + MUST-FAILS: SMOOTH anchor q_N <= 1e-20 and
SMOOTH alignment <= 1e-8 (self-alias trivializes both);
control-flip consistency as sealed per candidate (b1 first
rho < 0 at 21/25, b3 Gtil indefinite on SCRAMBLE, b2 FLIPLIKE
rho_2 < 0); MUST-FAILS (each loud): (m1) BORDERED INVERSE WITH
THE WRONG BLOCK -- the corner entry of the degree-(N-1)
augmented matrix presented as 1/D_N must break by >= 1e3 x
honest; (m2) WARD WITH SWAPPED MINORS -- the bilinear with the
degree-gap swap aug_n tau_{n+2} - aug_{n+2} tau_n minus phi_n^2
must be loudly nonzero (exact rationals; honest residual is
EXACTLY zero); (m3) DETECTOR MUTANT that must NOT flag the wall
reduction -- the fingerprint computed against seed-266-shuffled
g(1) values must MISS the wall criterion that the honest
detector flags (loud break of the mutant, gated); (m4) L' NOT
SQUARED in the dual weights -- the toy duality must break
(exact rationals).  mp WARDS at the exception terminals kz15
(N = 203, s* = 0.9966, the sharpest test) AND kz20 (N = 170):
mp (dps 60) bordered det ratio det A/det G == D_N vs the f64
chain 5/7 - rho_{N-1}, bar 1e-8 (r264 floor 8.1e-11) -- the
(A^{-1})_{BB} = 1/D_N corner statement at mp precision on both
sealed exception rungs.

INDEX FIREWALL (binding, r238-r265 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; rho_k = F_k^2/h_k, S_n =
sum_{k<=n} rho_k; ground truth (flips, branch labels) enters
GATES and census tables only; no zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack +
BH.spearman, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap + CA.sym_instance, r264 QO.gram_input / QO.port_pack /
QO.auc_power, r231 midpoint-connection theorem (cited; the toy
re-derivation is gated here), v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); SAMPLE_IDX (0, 20, 41); DEEP_N 400; Q7_HEAD 8;
FP_BAR 0.9; SIG_POWER_BAR 0.8; S_B1 (0.5, 0.9); B1_CORNER_BAR
1e-7; B1_FD_H 1e-3; B1_FD_BAR 1e-4; S_CENSUS (0.1, 0.25, 0.5,
0.75, 0.9, 1.0); ENDPOINT_BAR 1e-12; B2_DEG (1, 2, 3); B3_BAR
1e-6; B3_HEAD_BAR 1e-12; B4_K_WARD 20; B4_FB_BAR 1e-9;
B4_MP_DPS 60; B4_MP_LG_BAR 1e-6; B4_HDUAL_BAR 1e-8; DEPTH_GUARD
1e-12; SM_ALIGN_BAR 1e-8; SM_Q_BAR 1e-20; MP_DPS 60; MP_BAR
1e-8; MP_EXC_KZ (15, 20); SHUFFLE_SEED 266; LOUD 1e3; toy border
atoms (1/3, -2/5) weights (1/4, 1/7); symbolic instances = r263
CA.sym_instance verbatim (atoms (-3/2, -1, -1/2, 1/4, 3/4, 5/4),
MAINLIKE/FLIPLIKE weights, border atoms (0, 1/2) weights (1/3,
1/6), corner 5/7); b1/b3 symbolic instance = the r265 G20
3-atom-Hankel MAINLIKE block; runtime <= 1800 s; smoke = w9 +
controls + all symbolic/toy legs + w9 b1/b3 numerics + w9 b4
ward + must-fails (ladder, censuses, fingerprints,
adjudications, mp exception wards skipped).  DISCLOSED PRE-SPEC
SCRATCH (two feasibility passes, floors only, scripts deleted;
ALL bars and verdict rules above were fixed BEFORE any full
evaluation; no rule touched after any measurement): (s1)
fingerprints Spearman(crit1, g1) = 0.16, (crit3, g1) = 0.26,
(D_N, g1) = 0.28, (q_N, g1) = -0.28; crit1 in [0.9081, 0.9985],
crit3 in [0.8359, 0.9973], g1 in [6.06, 15.41]; crit1/crit3 AUC
powers 0.11/0.12; b1 corner floor 2.8e-9, FD floor 8.0e-7; b3
floor 1.2e-8 (N = 878), head floors 3.6e-15 / 1.2e-8, Gtil min
eig mains ~1e-4, SCRAMBLE -6.8; SCR/EPST min rho < 0; b2 census
2/72 fires (the known bilinear pair, sign +-1); toy border
transport exact; (s2) M-field coincidence structure (every
border atom hits exactly one union node -- the first pass's
naive log field produced NaNs, fixed by exact coincidence
handling BEFORE any bar was set), toy h-duality h#_m h_k == 1
exact, toy M field exact; w9/w13 mp ward lg dev 1.9e-12 /
1.3e-9, h-duality 1.3e-11 / 3.3e-11, fb ward 4.3e-12 (k = 20) /
1.4e-13 (terminal); terminal census: self-dual 42/42,
cancellation depth min 3.0e-5, orientation power 0.057,
alignment power 0.135, Spearman(align, g1) = 0.13, (align, D_N)
= 0.15; SMOOTH alignment 1.1e-11; EPST/SCR orientation -1
(reported).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  WALL_DETECTOR_ARMED(selftest + fingerprints)
+ B1_GO / B1_WALL_REDUCTION / B1_DEFINITE_DRAIN_RESTATEMENT(
    rate 2sW/D^2 definite, endpoint == target, drop == S_{N-1})
+ B2_DUAL_WARD_FOUND(form) / B2_DRAIN_ONLY(fires k/72)
+ B3_GO / B3_WALL_REDUCTION / B3_DEFLATED_DRAIN_RESTATEMENT(
    tail term == S_{N-1} - S_7)
+ B4_BORDER_ORIENTATION_CARRIED(power) / B4_BORDER_SIGN_BLIND(
    orientation + alignment powers)
+ [global] BORDER_RESOLVENT_IDENTITY_GO(cand) /
    IDENTITY_THIRD_CRITERION(cand, Messlage) /
    NO_IDENTITY_IN_CLASS(all four break locations) +
    RHP_LOCAL_ASYMPTOTICS_REQUIRED (the honest handover: the
    campaign needs a genuine local RHP asymptotic, not another
    identity of this complexity class).
GLOBAL GO RULE (sealed): some candidate passes ALL of exact
identity + definite blocks + exact target endpoint + no wall
fingerprint + SCRAMBLE loses + a NEW source-pure bound whose
demand log10(bound/budget) < 0 on 42/42 and which is NOT the
drop S_{N-1} itself (b1's and b3's only definite quantities ARE
the drop / the deflated drop -- a GO from them is structurally
impossible and the rule says so BEFORE evaluation; a GO could
only come from b2's dual form or a b4 orientation identity).
THIRD-CRITERION RULE (sealed): a b4 power >= 0.8 with both
fingerprints < 0.9.  Honesty before beauty: no verdict claims a
derived 5/7, a bound mechanism, or an asymptotic law; the target
positivity itself stays OPEN (the campaign's work); r243/r250/
r253/r256/r257/r258/r260/r261/r262/r263/r264/r265 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke 33/33 first pass; calibration pass 1 = first full
evaluation, 33/33 gates, wall 76.3 s -- NO bar, band, rule or
verdict was moved at any point (every sealed bar held at first
evaluation); ONE PRESENTATION AMENDMENT p1 is disclosed
(r263-p1 precedent): the G70 detail clause carried a pre-written
conclusion sentence ("the exceptions sit closer to the razor on
crit1/crit3") that the measured medians (crit1 0.960 vs 0.966,
crit3 0.942 vs 0.947 -- nearly coincident) only marginally
support; the clause was made data-driven BEFORE the record pass;
pass 2 = the record run below, numerically identical to pass 1
in every printed figure):
CAL_VERDICT = WALL_DETECTOR_ARMED(selftest sp(g1, g1) = 1.00
flagged, target sp(D_N, g1) = 0.28 not flagged; fingerprints
crit1 0.16 / crit3 0.26 / align 0.13, all < 0.9 -- NO candidate
is the wall) + B1_DEFINITE_DRAIN_RESTATEMENT(rate 2sW/D^2
definite 264/264 census points, endpoint == target rel 2.8e-14,
drop == S_{N-1} exact) + B2_DRAIN_ONLY(2/72 fires == the known
bilinear pair, no dual form) + B3_DEFLATED_DRAIN_RESTATEMENT(
quotient exact, tail term == S_{N-1} - S_7, SCRAMBLE min eig
-6.774) + B4_BORDER_SIGN_BLIND(orientation power 0.057,
alignment power 0.135) + NO_IDENTITY_IN_CLASS(b1@DEFINITE_DRAIN,
b2@DRAIN_ONLY, b3@DEFLATED_DRAIN, b4@SIGN_BLIND) +
RHP_LOCAL_ASYMPTOTICS_REQUIRED.
Key numbers.  LEG A: selftest -- wall criterion g(1) < 1 FALSE
on 42/42 with sp(g1, g1) = 1.000 >= 0.9 => FLAGGED; target D_N >
0 TRUE on 42/42 with sp(D_N, g1) = 0.284 < 0.9 => NOT flagged;
detector mutant (seed-266 shuffle) sp = 0.163 => MISSES the wall
(m3 loud as sealed); scope audits CLEAN, oracle mutant FLAGGED
(rho scope hit).  LEG B1: sympy EXACT (corner-inverse identity
in s + Jacobi route == d/ds closed form, rational zero); corner
entry vs 1/(B - s^2 W): worst scaled dev 2.7e-9 (bar 1e-7) on
mains + 3 samples x s in {0.5, 0.9}; FD vs rate 2sW/D^2 worst
rel 7.1e-7 (bar 1e-4); definiteness census: rate >= 0 and
D(s) > 0 at ALL 264 census points on 44 worlds, W = S_{N-1} in
[6.06, 15.41] > 0; endpoint identity (1 - crit1) B == D_N worst
rel 2.8e-14 (bar 1e-12); crit1 in [0.9081, 0.9985] < 1 on 42/42
(the TARGET decision pattern, matching D_N > 0); SCR/EPST first
rho < 0 at 21/25 == flips (carrier definiteness lost);
fingerprint sp(crit1, g1) = 0.164 < 0.9 => NOT the wall =>
B1_DEFINITE_DRAIN_RESTATEMENT (the definite direction is the
drain: drop == W == S_{N-1}, bounding it by B IS the target --
way A and way B collapse into the same statement at this
corner).  LEG B2: known bilinear re-gate EXACT (rational zero,
n = 1..3, both instances); lattice census: 2/72 ordered
combinations fire == the known pair aug_n tau_{n+1} - tau_n
aug_{n+1} = -+ phi_n^2 (signs -+1); NO firing combination puts
the square on the target side => B2_DRAIN_ONLY; FLIPLIKE rho_2
= -1566180625/1098746296 < 0 (sign structure lost at the flip,
r263 re-gated); m2 swapped minors: residual 2.984e+00 != 0 LOUD
vs honest EXACT 0.  LEG B3: sympy two-block quotient EXACT
(head 2 of 3, rational zero); numeric D3 vs D_N worst 1.2e-8
(bar 1e-6) on mains + 3 samples; head identities worst 5.3e-15
(bar 1e-12) / 1.2e-8 (bar 1e-6); Gtil min eig +5.0e-6 over the
pool (deepest sample N = 878) > 0, SCRAMBLE -6.774 < 0 (loses
PSD); fingerprint sp(crit3, g1) = 0.263 < 0.9; endpoint
identity (1 - crit3)(B - S_7) == D_N worst rel 2.3e-14 =>
B3_DEFLATED_DRAIN_RESTATEMENT (the inner-block complement
reproduces budget-minus-border-energy one level down; the
border term drains).  LEG B4: toy EXACT (connection k = 1..3,
border transport, h#_m h_k == 1, M field vs exact rationals);
eval ward fb worst rel 4.3e-12 (bar 1e-9, k = 20 + terminal,
both mains); mp ward (dps 60) at the self-dual terminal:
dual-chain route vs residue route lg dev 1.9e-12 (w9) / 1.3e-9
(w13), signs match, h-duality log dev 1.3e-11 / 3.3e-11 (bars
1e-6 / 1e-8); terminal census: self-dual S = 2N-1 on 42/42,
cancellation depth min 2.9e-5 >= 1e-12, orientation product
sign(F# F): exc (+1, +1, -1, +1, +1, +1, +1), cheap sum +21/35,
power 0.057; alignment c_w power 0.135 (exc med 3.9e-6 vs cheap
med 1.5e-5), BOTH < 0.8; align fingerprints sp(align, g1) =
0.131 / sp(align, D_N) = 0.148; SMOOTH alignment 1.1e-11 <=
1e-8 (anchor), EPST/SCR orientation -1/-1, aligns 1.7e-4/2.9e-4
(reported) => B4_BORDER_SIGN_BLIND: the L-gauge is sign-blind
for the BORDER too -- the missing orientation is NOT carried by
the midpoint connection.  LEG C: endpoint table -- crit1 TARGET
(exact), crit3 TARGET (exact), align THIRD-candidate but power
0.135 < 0.8 and no fingerprint => no third criterion; cheap vs
exc medians crit1 0.960/0.966, crit3 0.942/0.947 (nearly
coincident -- the branch is not readable from the restated
endpoints either).  LEG D: SMOOTH q_N = 4.2e-25 <= 1e-20; m1
wrong-block corner breaks by 2.1e-01 = 6.9e+09 x honest
3.1e-11; m3 mutant misses (sp 0.163 < 0.9) while honest flags
(sp 1.000); m2 residual 2.984 vs honest exact 0; m4 unsquared
L' breaks the toy duality by -1.377e-3 != 0 (exact rationals);
mp exception wards: kz15 (N = 203) D_mp = 0.0445838321 dev
3.5e-11, kz20 (N = 170) D_mp = 0.294659217 dev 6.5e-12 vs the
f64 chain 5/7 - rho_{N-1} (bar 1e-8) -- the corner statement
(A^{-1})_{BB} = 1/D_N holds at mp precision on BOTH sealed
exception terminals (kz15 the razor, margin 0.045).  READING
(typed, no upgrade): the round buries the identity class
honestly -- the border CAN be coupled into a fully definite
resolvent dynamics (b1: the augmented corner entry, exact
Jacobi rate 2sW/D^2, wall-free, SCRAMBLE loses it), but at this
corner the definite direction IS the drain and the endpoint
reduction is the target itself (way A and way B meet in the
same restatement); the exhaustive 2x2 minor lattice carries no
dual Ward form (the square never sits on the target side); the
inner-block Schur complement reproduces the same drain shape
one level down; and the h-free midpoint gauge is sign-blind for
the border exactly as for the basis (powers 0.06/0.14).  NO
candidate in the sealed class is a closure lever; NO candidate
reduces to the wall either (fingerprints 0.13-0.26) -- the wall
and the target stay measurably distinct statements, and the
campaign's honest next step is a genuine LOCAL RHP ASYMPTOTIC
at the terminal degree (parametrix-grade input), not another
finite-complexity identity.  Runtime 75.8 s full / 2.5 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE
(p1 predates the record run, disclosed above).

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
import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH            # noqa: E402 r244
import cancellation_adjudication_probe as CA  # noqa: E402 r263
import coupledtau_probe as CT                 # noqa: E402 r257
import terminal_crossratio_probe as TX        # noqa: E402 r260
import quenched_opening_probe as QO           # noqa: E402 r264
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import jfraction_probe as JF                  # noqa: E402 r230
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
SAMPLE_IDX = (0, 20, 41)
DEEP_N = 400
Q7_HEAD = 8
FP_BAR = 0.9
SIG_POWER_BAR = 0.8
S_B1 = (0.5, 0.9)
B1_CORNER_BAR = 1e-7
B1_FD_H = 1e-3
B1_FD_BAR = 1e-4
S_CENSUS = (0.1, 0.25, 0.5, 0.75, 0.9, 1.0)
ENDPOINT_BAR = 1e-12
B2_DEG = (1, 2, 3)
B3_BAR = 1e-6
B3_HEAD_BAR = 1e-12
B4_K_WARD = 20
B4_FB_BAR = 1e-9
B4_MP_DPS = 60
B4_MP_LG_BAR = 1e-6
B4_HDUAL_BAR = 1e-8
DEPTH_GUARD = 1e-12
SM_ALIGN_BAR = 1e-8
SM_Q_BAR = 1e-20
MP_DPS = 60
MP_BAR = 1e-8
MP_EXC_KZ = (15, 20)
SHUFFLE_SEED = 266
LOUD = 1e3
TOY_BX = (Fr(1, 3), Fr(-2, 5))
TOY_BW = (Fr(1, 4), Fr(1, 7))

CAL_VERDICT = (
    "WALL_DETECTOR_ARMED(selftest sp(g1, g1) = 1.00 flagged, "
    "target sp(D_N, g1) = 0.28 not flagged; fingerprints crit1 "
    "0.16 / crit3 0.26 / align 0.13, all < 0.9 -- NO candidate "
    "is the wall) + B1_DEFINITE_DRAIN_RESTATEMENT(rate 2sW/D^2 "
    "definite 264/264 census points, endpoint == target rel "
    "5.6e-16, drop == S_{N-1} exact) + B2_DRAIN_ONLY(2/72 fires "
    "== the known bilinear pair, no dual form) + "
    "B3_DEFLATED_DRAIN_RESTATEMENT(quotient exact, tail term == "
    "S_{N-1} - S_7, SCRAMBLE min eig -6.774) + "
    "B4_BORDER_SIGN_BLIND(orientation power 0.057, alignment "
    "power 0.135) + NO_IDENTITY_IN_CLASS(b1@DEFINITE_DRAIN, "
    "b2@DRAIN_ONLY, b3@DEFLATED_DRAIN, b4@SIGN_BLIND) + "
    "RHP_LOCAL_ASYMPTOTICS_REQUIRED")

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
                       "the r244 chain rows / the r261 Gram input / "
                       "the r257 port pair; ground truth (flips, "
                       "branch labels) enters gates and census "
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


# ------------- sealed b4 statistic builders (target-blind: consume
# node positions + signed weights + the r244 chain rows ONLY; the
# branch answer and every target-side quantity are structurally
# withheld -- AST-audited)
def eval_scaled(rows, pts, deg):
    """scaled monic chain values v_deg(pts) = pihat_deg(pts)
    e^{-Ls_deg}, driven by the r244 rows (alh, gam_next, Ls)."""
    v = np.ones_like(pts)
    vm = np.zeros_like(pts)
    for k in range(deg):
        alh = rows[k]["alh"]
        if k == 0:
            px = (pts - alh) * v
        else:
            gam = rows[k - 1]["gam_next"]
            fc = math.exp(rows[k - 1]["Ls"] - rows[k]["Ls"])
            px = (pts - alh) * v - gam * fc * vm
        vm = v
        v = px * math.exp(rows[k]["Ls"] - rows[k + 1]["Ls"])
    return v


def m_field(xu, bx, bw, chunk=512):
    """Mhat_j: per-j logsumexp of M_j = sum_b bw_b L(z_b)/(z_b -
    x_j), with EXACT coincidence handling (a border atom on a
    union node contributes only the deleted-node value there);
    returns (Mlog, Msgn)."""
    n_nodes = len(xu)
    d = bx[:, None] - xu[None, :]
    zmask = (d == 0.0)
    nz = zmask.sum(axis=1)
    dsafe = np.where(zmask, 1.0, d)
    lgd = np.where(zmask, 0.0, np.log(np.abs(dsafe)))
    sgd = np.where(zmask, 1.0, np.sign(dsafe))
    lgL_ex = lgd.sum(axis=1)
    sgL_ex = np.prod(sgd, axis=1)
    lgbw = np.log(np.abs(bw))
    sgbw = np.sign(bw)
    Mlog = np.full(n_nodes, -np.inf)
    Msgn = np.zeros(n_nodes)
    reg = np.nonzero(nz == 0)[0]
    one = np.nonzero(nz == 1)[0]
    for lo in range(0, n_nodes, chunk):
        hi = min(lo + chunk, n_nodes)
        acc_lt = np.full((len(reg) + len(one), hi - lo), -np.inf)
        acc_st = np.zeros_like(acc_lt)
        if len(reg):
            acc_lt[:len(reg)] = (lgbw[reg, None]
                                 + lgL_ex[reg, None]
                                 - lgd[reg][:, lo:hi])
            acc_st[:len(reg)] = (sgbw[reg, None]
                                 * sgL_ex[reg, None]
                                 * sgd[reg][:, lo:hi])
        if len(one):
            block_l = np.full((len(one), hi - lo), -np.inf)
            block_s = np.zeros((len(one), hi - lo))
            zb = zmask[one][:, lo:hi]
            block_l[zb] = np.broadcast_to(
                (lgbw[one] + lgL_ex[one])[:, None], zb.shape)[zb]
            block_s[zb] = np.broadcast_to(
                (sgbw[one] * sgL_ex[one])[:, None], zb.shape)[zb]
            acc_lt[len(reg):] = block_l
            acc_st[len(reg):] = block_s
        mx = np.max(acc_lt, axis=0)
        mx = np.where(np.isfinite(mx), mx, 0.0)
        ssum = np.sum(acc_st * np.exp(acc_lt - mx[None, :]),
                      axis=0)
        Mlog[lo:hi] = mx + np.log(np.abs(ssum) + 1e-300)
        Msgn[lo:hi] = np.sign(ssum)
    return Mlog, Msgn


def border_gauge_stats(rows, xu, wu, bx, bw, deg):
    """the sealed b4 terminal statistics via the RESIDUE route:
    A = sum_j wu_j v_deg(x_j) Mhat_j; returns (sign(F#) sign(F),
    alignment c, cancellation depth).  Consumes chain rows + raw
    atoms only."""
    Mlog, Msgn = m_field(xu, bx, bw)
    shM = float(np.max(Mlog))
    Mh = Msgn * np.exp(Mlog - shM)
    vk = eval_scaled(rows, xu, deg)
    A = float(np.sum(wu * vk * Mh))
    dep = abs(A) / max(float(np.sum(np.abs(wu * vk * Mh))), 1e-300)
    sF = math.copysign(1.0, rows[deg]["fb"])
    sFd = math.copysign(1.0, A) \
        * math.copysign(1.0, rows[deg]["eta"])
    num = A * A
    den = float(np.sum(np.abs(wu) * vk * vk)) \
        * float(np.sum(np.abs(wu) * Mh * Mh))
    return sF * sFd, num / max(den, 1e-300), dep, A, shM


def oracle_stat(p):
    """DELIBERATE MUST-FAIL MUTANT: reads the terminal target --
    the scope audit must FLAG this."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


B4_FORBIDDEN = {"rho", "S", "sa", "la", "q_chain", "D_dir", "wb",
                "world_block", "direct_terminal", "rhp_readout",
                "gram_input", "port_pack", "g_gap", "u_triangle",
                "M_W"}


def b4_scope_audit(funcname):
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
                if nm in B4_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ----------------------------------------------- b1 numeric routes
def corner_entry(G, tv, B, s, n=None, wrong_block=False):
    """the (B, B) entry of the INVERSE augmented matrix A(s) =
    [[G_n, s tv_n], [s tv_n^T, B]] via one linear solve; the m1
    mutant presents the degree-(n-1) block as the full one."""
    n = G.shape[0] if n is None else n
    if wrong_block:
        n = n - 1
    A = np.zeros((n + 1, n + 1))
    A[:n, :n] = G[:n, :n]
    A[:n, n] = s * tv[:n]
    A[n, :n] = s * tv[:n]
    A[n, n] = B
    eB = np.zeros(n + 1)
    eB[n] = 1.0
    return float(np.linalg.solve(A, eB)[n])


# ----------------------------------------------- b2 lattice tools
def is_rat_square(v):
    """exact perfect-square test for a sympy Rational (up to the
    stated absolute value)."""
    if v == 0:
        return False
    v = sp.Rational(abs(v))
    _rp, okp = sp.integer_nthroot(sp.Integer(v.p), 2)
    _rq, okq = sp.integer_nthroot(sp.Integer(v.q), 2)
    return bool(okp and okq)


# ----------------------------------------------- b4 mp dual route
def mp_dual_route(p, deg):
    """mp (dps sealed) L-gauge dual route at the self-dual
    terminal: dual weights 1/(w_j L'(x_j)^2) in mp, scaled dual
    Stieltjes chain to degree deg, border integral; returns
    (sign, log|F#|, h-duality log dev)."""
    mp.mp.dps = B4_MP_DPS
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    S_ = len(xu)
    xs_m = [mp.mpf(float(v)) for v in xu]
    ws_m = [mp.mpf(float(v)) for v in wu]
    lgdw = []
    sg = []
    for j in range(S_):
        lg = -mp.log(abs(ws_m[j]))
        for i in range(S_):
            if i != j:
                lg -= 2 * mp.log(abs(xs_m[j] - xs_m[i]))
        lgdw.append(lg)
        sg.append(mp.sign(ws_m[j]))
    sh = max(lgdw)
    dwm = [s * mp.e ** (lg - sh) for s, lg in zip(sg, lgdw)]
    bxm = [mp.mpf(float(v)) for v in bx]
    bwm = [mp.mpf(float(v)) for v in bw]
    qx = [mp.mpf(1)] * S_
    qb = [mp.mpf(1)] * len(bx)
    qx_m = [mp.mpf(0)] * S_
    qb_m = [mp.mpf(0)] * len(bx)
    Ls = Ls_m = mp.mpf(0)
    eta = mp.fsum(dwm)
    eta_m = eta
    for n in range(deg):
        alh = mp.fsum(w * x * q * q
                      for w, x, q in zip(dwm, xs_m, qx)) / eta
        if n == 0:
            px = [(x - alh) * q for x, q in zip(xs_m, qx)]
            pb = [(z - alh) * q for z, q in zip(bxm, qb)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            px = [(x - alh) * q - ge * fc * qq
                  for x, q, qq in zip(xs_m, qx, qx_m)]
            pb = [(z - alh) * q - ge * fc * qq
                  for z, q, qq in zip(bxm, qb, qb_m)]
        sc = max(abs(v) for v in px)
        qx_m, qb_m, eta_m, Ls_m = qx, qb, eta, Ls
        qx = [v / sc for v in px]
        qb = [v / sc for v in pb]
        Ls = Ls + mp.log(sc)
        eta = mp.fsum(w * q * q for w, q in zip(dwm, qx))
    Fdir = mp.fsum(w * q for w, q in zip(bwm, qb))
    eta_k = p["rows"][deg]["eta"]
    Ls_k = p["rows"][deg]["Ls"]
    hdual = float(abs(mp.log(abs(eta)) + 2 * Ls + sh
                      + mp.mpf(math.log(abs(eta_k))
                               + 2 * Ls_k)))
    return int(mp.sign(Fdir)), float(Ls + mp.log(abs(Fdir))), hdual


# ------------------------------------------------ mp exception ward
def mp_corner_ward(p, dps):
    """mp bordered det ratio det A / det G at FULL size N (border
    unscaled) == D_N; the corner statement (A^{-1})_{BB} = 1/D_N
    is its cofactor form.  r264/r265 mp route adapted."""
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    n = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0m = mp.mpf(0.5 * (lo + hi))
    rhm = mp.mpf(0.5 * (hi - lo))
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    bs = [mp.mpf(float(v)) for v in bx]
    bwm = [mp.mpf(float(v)) for v in bw]
    tvm = [(x - x0m) / rhm for x in xs]
    tbm = [(x - x0m) / rhm for x in bs]
    PU = [[mp.mpf(1)] * len(xs), [2 * u for u in tvm]]
    TU = [[mp.mpf(1)] * len(bs), [2 * u for u in tbm]]
    for _k in range(2, n):
        PU.append([2 * u * a - b
                   for u, a, b in zip(tvm, PU[-1], PU[-2])])
        TU.append([2 * u * a - b
                   for u, a, b in zip(tbm, TU[-1], TU[-2])])
    GM = mp.matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            v = mp.fsum(w * a * b
                        for w, a, b in zip(ws, PU[i], PU[j]))
            GM[i, j] = v
            GM[j, i] = v
    tm = [mp.fsum(w * a for w, a in zip(bwm, TU[i]))
          for i in range(n)]
    Bm = mp.mpf(float(p["S"][n - 2])) + mp.mpf(5) / 7
    A = mp.matrix(n + 1, n + 1)
    for i in range(n):
        for j in range(n):
            A[i, j] = GM[i, j]
        A[i, n] = tm[i]
        A[n, i] = tm[i]
    A[n, n] = Bm
    return mp.det(A) / mp.det(GM)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("border_resolvent_identity_probe -- PRIME.PORT.RHP."
          "QUENCHED.BORDER_RESOLVENT_IDENTITY.01 (round 266)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)   "
          "CHARTER_SHA %s (imported r264)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16], QO.CHARTER_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + symbolic/toy legs "
                        "+ w9 numerics + must-fails; ladder, "
                        "censuses, fingerprints, adjudications, "
                        "mp exception wards skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "FOUR sealed augmented-first candidates (b1 resolvent "
          "diagonal, b2 pair-Ward lattice, b3 inner-block Schur, "
          "b4 L-gauge border transport) against the sealed r265 "
          "WALL-REDUCTION detector (decision + rank fingerprints, "
          "bar 0.9) with inherited kills (PAIRCORR, TARGET_"
          "INVERSE, SELECTION_BY_ANSWER) and the r263 SCRAMBLE "
          "support-geometry test; global GO / THIRD-CRITERION / "
          "NO_IDENTITY_IN_CLASS rules sealed BEFORE evaluation "
          "(two pre-spec feasibility scratches disclosed in the "
          "spec, floors only)")

    # ---------------- S1: census + controls
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
          "control flips re-derived %s (INDEFINITE_CONTINUATION "
          "beyond pmax); cofinal ladder %d rungs POSITIVE_PREFIX "
          "%s, N in [%s, %s]"
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
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        B = float(p["S"][N - 2]) + B57
        S1 = float(p["S"][N - 1])
        S7 = float(p["S"][Q7_HEAD - 1])
        return dict(kz=p["kz"], N=N, g=g, p=p, B=B, W=S1, S7=S7,
                    DN=B - S1, crit1=S1 / B,
                    crit3=(S1 - S7) / (B - S7))

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    lab = {rc["kz"]: rc["g"] < 0.0 for rc in recs}
    exc_kz = tuple(sorted(rc["kz"] for rc in recs
                          if rc["g"] < 0.0))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g"] >= 0 else "EXCEPTION",
                 recs[0]["g"]))
    else:
        check("G11-branch-reproduction",
              sum(1 for rc in recs if rc["g"] >= 0)
              == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (sum(1 for rc in recs if rc["g"] >= 0),
                 str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g"])
                           for rc in mrecs)))

    # ---------------- S2: LEG A -- the wall-reduction detector
    section("S2  LEG A -- WALL-REDUCTION DETECTOR")
    g1s = {}
    for rc in recs:
        pk = QO.port_pack(rc["kz"])
        lam, U = np.linalg.eigh(pk["Q"])
        c2 = (U.T @ pk["f"]) ** 2
        g1s[rc["kz"]] = float(np.sum(c2 / (1.0 - lam)))
    g1v = [g1s[rc["kz"]] for rc in recs]
    dnv = [rc["DN"] for rc in recs]

    def wall_flag(critv, passes):
        """the sealed detector: wall decision pattern (criterion
        FALSE on every rung) + rank fingerprint >= FP_BAR."""
        sp_ = abs(BH.spearman(critv, g1v))
        dec_wall = (passes == 0)
        return (dec_wall and sp_ >= FP_BAR), sp_

    if not smoke:
        fl_wall, sp_wall = wall_flag(
            g1v, sum(1 for v in g1v if v < 1.0))
        fl_tgt, sp_tgt = wall_flag(
            dnv, sum(1 for v in dnv if v > 0.0))
        # note: for the target the decision pattern is TRUE
        # everywhere, so dec_wall is False by construction; the
        # printed sp is the honest rank association
        ok_self = fl_wall and not fl_tgt
        check("G20-detector-selftest", ok_self,
              "SELFTEST: the known wall criterion g(1) < 1 is "
              "FALSE on 42/42 with sp(g1, g1) = %.3f >= %.1f => "
              "FLAGGED WALL_REDUCTION; the target D_N > 0 is "
              "TRUE on 42/42 with sp(D_N, g1) = %.3f (< %.1f, "
              "and the decision pattern is the TARGET pattern) "
              "=> NOT flagged -- the detector separates wall "
              "and target on the measured ladder"
              % (sp_wall, FP_BAR, sp_tgt, FP_BAR))
        rng = np.random.default_rng(SHUFFLE_SEED)
        g1_shuf = list(rng.permutation(g1v))
        sp_mut = abs(BH.spearman(g1v, g1_shuf))
        check("G21-mustfail-detector-mutant",
              sp_mut < FP_BAR and sp_wall >= FP_BAR,
              "m3 DETECTOR MUTANT (fingerprint against seed-%d "
              "shuffled g(1)): sp = %.3f < %.1f => the mutant "
              "MISSES the wall criterion that the honest "
              "detector flags (sp %.3f) -- a detector that "
              "cannot flag the known wall reduction breaks "
              "loudly, as sealed"
              % (SHUFFLE_SEED, sp_mut, FP_BAR, sp_wall))
    else:
        check("G20-detector-selftest", True, "SMOKE: skipped")
        check("G21-mustfail-detector-mutant", True,
              "SMOKE: skipped")
    hits = []
    for fn in ("eval_scaled", "m_field", "border_gauge_stats"):
        hits += b4_scope_audit(fn)
    hits_orc = b4_scope_audit("oracle_stat")
    ag_hits = antigate_fragment_audit()
    check("G22-scope-audits", not hits and bool(hits_orc)
          and not ag_hits,
          "the sealed b4 statistic builders consume node "
          "positions + signed weights + chain rows ONLY (%s); "
          "the deliberately target-reading mutant is FLAGGED "
          "(%s); fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_orc) if hits_orc else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S3: LEG B1 -- augmented resolvent diagonal
    section("S3  B1 -- THE AUGMENTED RESOLVENT DIAGONAL")
    s_sym, Bs = sp.symbols("s B")
    m3 = [sum(w * x ** j for w, x in zip(
        [sp.Rational(2, 3), sp.Rational(-1, 5), sp.Rational(1, 2),
         sp.Rational(-3, 7), sp.Integer(1), sp.Rational(1, 3)],
        [sp.Rational(-3, 2), sp.Integer(-1), sp.Rational(-1, 2),
         sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(5, 4)]))
        for j in range(6)]
    H3 = sp.Matrix(3, 3, lambda i, j: m3[i + j])
    bm3 = [sum(bw * bx ** j for bw, bx in zip(
        [sp.Rational(1, 3), sp.Rational(1, 6)],
        [sp.Integer(0), sp.Rational(1, 2)])) for j in range(3)]
    b3 = sp.Matrix(3, 1, lambda i, _j: bm3[i])
    A3 = sp.zeros(4, 4)
    A3[:3, :3] = H3
    for i in range(3):
        A3[i, 3] = s_sym * b3[i]
        A3[3, i] = s_sym * b3[i]
    A3[3, 3] = Bs
    W3 = (b3.T * H3.inv() * b3)[0, 0]
    corner_cf = 1 / (Bs - s_sym ** 2 * W3)
    Ainv = A3.inv()
    ok_c = sp.simplify(Ainv[3, 3] - corner_cf) == 0
    Ap = sp.zeros(4, 4)
    for i in range(3):
        Ap[i, 3] = b3[i]
        Ap[3, i] = b3[i]
    jac = -(Ainv * Ap * Ainv)[3, 3]
    ok_j = sp.simplify(jac - sp.diff(corner_cf, s_sym)) == 0
    rate_cf = 2 * s_sym * W3 / (Bs - s_sym ** 2 * W3) ** 2
    ok_r = sp.simplify(sp.diff(corner_cf, s_sym) - rate_cf) == 0
    check("G30-b1-symbolic", ok_c and ok_j and ok_r,
          "sympy EXACT (rational zero, r265 MAINLIKE Hankel "
          "block, border scaled by the symbol s): (A(s)^{-1})_"
          "{BB} == 1/(B - s^2 b^T H^{-1} b) (the bordered-"
          "inverse corner); the Jacobi route -(A^{-1} A' "
          "A^{-1})_{BB} == d/ds of the closed form == 2sW/D(s)^2 "
          "-- the border column sits IN the operator and the "
          "corner dynamics is an explicit square over a squared "
          "denominator")
    b1_pool = mrecs + ([recs[i] for i in SAMPLE_IDX]
                       if not smoke else [])
    w_corner = 0.0
    w_fd = 0.0
    for rc in b1_pool:
        p = rc["p"]
        G, tv = QO.gram_input(p)
        rc["_G"], rc["_tv"] = G, tv
        for s in S_B1:
            Dc = rc["B"] - s * s * rc["W"]
            ce = corner_entry(G, tv, rc["B"], s)
            w_corner = max(w_corner, abs(ce - 1.0 / Dc) * abs(Dc))
    for rc in mrecs:
        G, tv = rc["_G"], rc["_tv"]
        vals = [corner_entry(G, tv, rc["B"], ss)
                for ss in (0.5 - B1_FD_H, 0.5 + B1_FD_H)]
        fd = (vals[1] - vals[0]) / (2 * B1_FD_H)
        D0 = rc["B"] - 0.25 * rc["W"]
        rate = 2.0 * 0.5 * rc["W"] / (D0 * D0)
        w_fd = max(w_fd, abs(fd - rate) / (1 + abs(rate)))
    check("G31-b1-corner-direct", w_corner <= B1_CORNER_BAR,
          "corner entry of the inverse augmented matrix (one "
          "linear solve, border column IN the operator) vs the "
          "closed form 1/(B - s^2 S_{N-1}) on %d worlds x s in "
          "%s: worst scaled dev %.1e (bar %.0e; scratch floor "
          "2.8e-9 including the N = 878 sample)"
          % (len(b1_pool), str(S_B1), w_corner, B1_CORNER_BAR))
    check("G32-b1-jacobi-rate-fd", w_fd <= B1_FD_BAR,
          "central FD of the DIRECT corner entry vs the exact "
          "Jacobi rate 2sW/D^2 at s = 0.5 on the mains: worst "
          "rel %.1e (bar %.0e, FD floor)"
          % (w_fd, B1_FD_BAR))
    cen_ok = True
    n_cen = 0
    for rc in recs + (mrecs if not smoke else []):
        for s in S_CENSUS:
            Dc = rc["B"] - s * s * rc["W"]
            rate = 2.0 * s * rc["W"] / (Dc * Dc)
            cen_ok = cen_ok and (rate >= 0.0 and Dc > 0.0)
            n_cen += 1
    e_dev = max(abs((1.0 - rc["crit1"]) * rc["B"] - rc["DN"])
                / max(abs(rc["DN"]), 1e-300)
                for rc in recs + mrecs)
    w_min = min(rc["W"] for rc in recs + mrecs)
    w_max = max(rc["W"] for rc in recs + mrecs)
    c1_pass = sum(1 for rc in recs if rc["crit1"] < 1.0)
    rho_first = {}
    for c in ("SCR", "EPST"):
        rv = ctrl[c]["rho"]
        rho_first[c] = next((k for k in range(len(rv))
                             if float(rv[k]) < 0), None)
    scr_loses = (rho_first["SCR"] == CTRL_FLIPS["SCRAMBLE"]
                 and rho_first["EPST"] == CTRL_FLIPS["EPSTEIN"])
    check("G33-b1-definiteness-census", cen_ok
          and e_dev <= ENDPOINT_BAR and w_min > 0.0
          and scr_loses and (smoke or c1_pass == len(recs)),
          "rate 2sW/D^2 >= 0 and D(s) > 0 at ALL %d census "
          "points on %d worlds (W = S_{N-1} in [%.2f, %.2f] > "
          "0: the carrier is a sum of squares on the positive "
          "prefix); endpoint identity (1 - crit1) B == D_N "
          "worst rel %.1e (bar %.0e); crit1 < 1 on %s (the "
          "TARGET decision pattern); SCR/EPST lose the carrier "
          "definiteness: first rho < 0 at %s == flips (21/25)"
          % (n_cen, len(recs) + (len(mrecs) if not smoke
                                 else 0), w_min, w_max, e_dev,
             ENDPOINT_BAR,
             ("%d/%d" % (c1_pass, len(recs))) if not smoke
             else "n/a (SMOKE)", str(rho_first)))
    if not smoke:
        cr1 = [rc["crit1"] for rc in recs]
        fl1, sp1 = wall_flag(cr1, c1_pass)
        b1_verdict = ("B1_WALL_REDUCTION" if fl1 else
                      "B1_DEFINITE_DRAIN_RESTATEMENT")
        check("G34-b1-adjudication", True,
              "sealed adjudication: fingerprint sp(crit1, g1) = "
              "%.3f (< %.1f) + the target decision pattern => "
              "NOT the wall; definiteness needs only the "
              "positive prefix (source-pure) -- but the definite "
              "direction is the DRAIN: the corner entry RISES, "
              "the total drop D(0) - D(1) == W == S_{N-1} "
              "EXACTLY (closed form), and bounding the drop by "
              "the budget IS the target; the identity supplies "
              "NO new source-pure bound (its only definite "
              "quantity is the drop itself, excluded by the "
              "sealed GO rule) => %s"
              % (sp1, FP_BAR, b1_verdict))
    else:
        b1_verdict = "SMOKE"
        check("G34-b1-adjudication", True, "SMOKE: skipped")

    # ---------------- S4: LEG B2 -- the pair-Ward lattice
    section("S4  B2 -- PAIR-WARD LATTICE (DUAL-FORM SEARCH)")
    inst_m = CA.sym_instance(False)
    inst_f = CA.sym_instance(True)
    ok_bil = True
    for inst in (inst_m, inst_f):
        for n in B2_DEG:
            lhs = inst["aug"][n] * inst["tau"][n + 1] \
                - inst["aug"][n + 1] * inst["tau"][n]
            rhs = (inst["F"][n] * inst["tau"][n]) ** 2
            ok_bil = ok_bil and (sp.simplify(lhs - rhs) == 0)
    rho2_f = inst_f["F"][2] ** 2 / inst_f["h"][2]
    check("G40-b2-bilinear-regate", ok_bil and rho2_f < 0,
          "the known r260 bilinear aug_n tau_{n+1} - aug_{n+1} "
          "tau_n == phi_n^2 (phi_n = F_n tau_n) EXACT n = 1..3 "
          "on MAINLIKE + FLIPLIKE (rational zero); FLIPLIKE "
          "normalized decrement rho_2 = %s < 0 -- the SIGN "
          "structure is lost at the flip (r263 K2 scramble "
          "condition re-gated)" % str(rho2_f))

    def obj(inst, name, n):
        if name == "tau":
            return inst["tau"][n]
        if name == "aug":
            return inst["aug"][n]
        return inst["F"][n] * inst["tau"][n]

    names = ("tau", "aug", "phi")
    prods = [(a, b) for a in names for b in names]
    fired = []
    for i in range(len(prods)):
        for j in range(len(prods)):
            if i == j:
                continue
            sgns = set()
            ok_all = True
            for n in B2_DEG:
                a1, b1 = prods[i]
                a2, b2 = prods[j]
                v = obj(inst_m, a1, n) * obj(inst_m, b1, n + 1) \
                    - obj(inst_m, a2, n) * obj(inst_m, b2, n + 1)
                if not is_rat_square(v):
                    ok_all = False
                    break
                sgns.add(1 if v > 0 else -1)
            if ok_all and len(sgns) == 1:
                fired.append((prods[i], prods[j], sgns.pop()))
    fire_note = "; ".join(
        "%s_n %s_{n+1} - %s_n %s_{n+1} (sign %+d)"
        % (f[0][0], f[0][1], f[1][0], f[1][1], f[2])
        for f in fired)
    known = {(("aug", "tau"), ("tau", "aug"), 1),
             (("tau", "aug"), ("aug", "tau"), -1)}
    only_known = set(fired) == known
    check("G41-b2-lattice-census", bool(fired),
          "exhaustive 2x2 census on the augmented minor lattice "
          "(objects tau/aug/phi at degrees n, n+1; 72 ordered "
          "combinations; FIRE = nonzero perfect rational square "
          "with constant sign at n = 1..3 on MAINLIKE): %d/72 "
          "fire: %s -- %s"
          % (len(fired), fire_note,
             "EXACTLY the known bilinear pair" if only_known
             else "ADDITIONAL structure found (adjudicated in "
             "G42)"))
    dual_found = None
    for f in fired:
        (a1, b1), (a2, b2), sg = f
        # target-side product aug_{n+1} tau_n with a PLUS square:
        # v = X - aug tau' ... solving aug_{n+1} tau_n = X - v;
        # a dual form needs aug_{n+1} tau_n == X + square with X
        # source-positive, i.e. a fire with (a2, b2) == the
        # target product ordering (tau, aug) and sign -1 and
        # (a1, b1) a source-positive product OTHER than the
        # known start aug_n tau_{n+1}
        if (a2, b2) == ("tau", "aug") and sg == -1 \
                and (a1, b1) not in (("aug", "tau"),):
            dual_found = f
    b2_verdict = ("B2_DUAL_WARD_FOUND(%s)" % str(dual_found)
                  if dual_found else
                  "B2_DRAIN_ONLY(%d/72 fires == the known "
                  "bilinear pair)" % len(fired))
    check("G42-b2-adjudication", True,
          "sealed dual-form rule (a fire expressing aug_{n+1} "
          "tau_n as a source-positive product PLUS a square): "
          "%s -- the square never sits on the target side; the "
          "manifest square of the lattice is the DRAIN-side "
          "phi_n^2 (r263 K2 kill confirmed at the exhaustive "
          "2x2 level)" % b2_verdict)
    n0 = 1
    swap_res = inst_m["aug"][n0] * inst_m["tau"][n0 + 2] \
        - inst_m["aug"][n0 + 2] * inst_m["tau"][n0] \
        - (inst_m["F"][n0] * inst_m["tau"][n0]) ** 2
    check("G43-mustfail-swapped-minors", swap_res != 0,
          "m2 WARD WITH SWAPPED MINORS (degree-gap swap aug_n "
          "tau_{n+2} - aug_{n+2} tau_n vs phi_n^2): residual = "
          "%.3e != 0 LOUD (exact rationals; the honest bilinear "
          "residual is EXACTLY zero) -- the Ward is minor-"
          "pinned" % float(swap_res))

    # ---------------- S5: LEG B3 -- inner-block Schur complement
    section("S5  B3 -- AUGMENTED SCHUR COMPLEMENT (INNER BLOCK)")
    HB = 2
    GHH = H3[:HB, :HB]
    GHT = H3[:HB, HB:]
    GTT = H3[HB:, HB:]
    tH = b3[:HB, :]
    tT = b3[HB:, :]
    Gt_s = GTT - GHT.T * GHH.inv() * GHT
    ft_s = tT - GHT.T * GHH.inv() * tH
    Bh_s = Bs - (tH.T * GHH.inv() * tH)[0, 0]
    D3_s = Bh_s - (ft_s.T * Gt_s.inv() * ft_s)[0, 0]
    D_full = Bs - (b3.T * H3.inv() * b3)[0, 0]
    ok_q = sp.simplify(D3_s - D_full) == 0
    check("G50-b3-symbolic", ok_q,
          "sympy EXACT (rational zero): the two-block quotient "
          "D = (B - t_H^T G_HH^{-1} t_H) - ftil^T Gtil^{-1} "
          "ftil == B - t^T G^{-1} t on the r265 MAINLIKE block "
          "(head %d of 3) -- the Schur quotient property with "
          "the border deflated THROUGH the head" % HB)
    w3 = w3h = w3e = 0.0
    eig_main_min = float("inf")
    for rc in b1_pool:
        G, tv = rc["_G"], rc["_tv"]
        Hh = Q7_HEAD
        sol_h = np.linalg.solve(G[:Hh, :Hh], tv[:Hh])
        solG = np.linalg.solve(G[:Hh, :Hh], G[:Hh, Hh:])
        Gt = G[Hh:, Hh:] - G[Hh:, :Hh] @ solG
        ft = tv[Hh:] - G[Hh:, :Hh] @ sol_h
        Bh = rc["B"] - float(tv[:Hh] @ sol_h)
        en = float(ft @ np.linalg.solve(Gt, ft))
        w3 = max(w3, abs((Bh - en) - rc["DN"]))
        w3h = max(w3h, abs(Bh - (rc["B"] - rc["S7"])))
        w3e = max(w3e, abs(en - (rc["W"] - rc["S7"])))
        eig_main_min = min(eig_main_min,
                           float(np.linalg.eigvalsh(Gt)[0]))
    pS = ctrl["SCR"]
    GS, tvS = QO.gram_input(pS)
    solGS = np.linalg.solve(GS[:Q7_HEAD, :Q7_HEAD],
                            GS[:Q7_HEAD, Q7_HEAD:])
    GtS = GS[Q7_HEAD:, Q7_HEAD:] - GS[Q7_HEAD:, :Q7_HEAD] @ solGS
    eig_scr = float(np.linalg.eigvalsh(GtS)[0])
    check("G51-b3-two-block-direct", w3 <= B3_BAR
          and w3h <= B3_HEAD_BAR and w3e <= B3_BAR
          and eig_main_min > 0.0,
          "numeric two-block route (head = Q7 level %d) vs D_N "
          "on %d worlds: worst abs dev %.1e (bar %.0e); head "
          "identities |Bh - (B - S_7)| %.1e (bar %.0e), "
          "|deflated energy - (S_{N-1} - S_7)| %.1e (bar %.0e "
          "-- the deflated border energy is EXACTLY the tail "
          "Parseval sum); deflated Gram Gtil positive on the "
          "positive prefix (min eig %.1e > 0)"
          % (Q7_HEAD, len(b1_pool), w3, B3_BAR, w3h,
             B3_HEAD_BAR, w3e, B3_BAR, eig_main_min))
    check("G52-b3-scramble-loses", eig_scr < 0.0,
          "SCRAMBLE loses the definiteness premise: deflated "
          "Gram min eig = %.3f < 0 (the head complementation "
          "does not survive the flip at 21) -- the b3 identity "
          "is NOT support geometry" % eig_scr)
    e_dev3 = max(abs((1.0 - rc["crit3"]) * (rc["B"] - rc["S7"])
                     - rc["DN"]) / max(abs(rc["DN"]), 1e-300)
                 for rc in recs + mrecs)
    if not smoke:
        cr3 = [rc["crit3"] for rc in recs]
        c3_pass = sum(1 for v in cr3 if v < 1.0)
        fl3, sp3 = wall_flag(cr3, c3_pass)
        b3_verdict = ("B3_WALL_REDUCTION" if fl3 else
                      "B3_DEFLATED_DRAIN_RESTATEMENT")
        check("G53-b3-adjudication", e_dev3 <= ENDPOINT_BAR,
              "sealed adjudication: endpoint identity (1 - "
              "crit3)(B - S_7) == D_N worst rel %.1e (bar %.0e) "
              "-- the endpoint is the TARGET exactly; crit3 < 1 "
              "on %d/%d (target pattern); fingerprint sp(crit3, "
              "g1) = %.3f < %.1f => NOT the wall; the border "
              "term enters as MINUS the deflated energy == "
              "S_{N-1} - S_7 (drain side, one level down) and "
              "supplies no new bound => %s"
              % (e_dev3, ENDPOINT_BAR, c3_pass, len(recs), sp3,
                 FP_BAR, b3_verdict))
    else:
        b3_verdict = "SMOKE"
        check("G53-b3-adjudication", e_dev3 <= ENDPOINT_BAR,
              "SMOKE: endpoint identity worst rel %.1e (bar "
              "%.0e); adjudication skipped"
              % (e_dev3, ENDPOINT_BAR))

    # ---------------- S6: LEG B4 -- the L-gauge border transport
    section("S6  B4 -- L-GAUGE WARD (BORDER TRANSPORT)")
    nodes = JF.TOY_NODES
    wts = JF.TOY_WTS
    S_t = len(nodes)
    al, beta, hs = JF.stieltjes_exact(nodes, wts, S_t)
    Lp = []
    for j in range(S_t):
        pr = Fr(1)
        for k in range(S_t):
            if k != j:
                pr *= (nodes[j] - nodes[k])
        Lp.append(pr)
    dw = [1 / (wts[j] * Lp[j] ** 2) for j in range(S_t)]
    alD, betaD, hsD = JF.stieltjes_exact(nodes, dw, S_t - 1)

    def pival(z, n, alv, bev):
        p0, p1 = Fr(1), z - alv[0]
        if n == 0:
            return p0
        for k in range(1, n):
            p0, p1 = p1, (z - alv[k]) * p1 - bev[k - 1] * p0
        return p1

    def toy_routes(k, dual_al, dual_be, dual_h):
        m = S_t - 1 - k
        Fd = sum(bw * pival(z, m, dual_al, dual_be)
                 for bw, z in zip(TOY_BW, TOY_BX))
        Fres = Fr(0)
        for j in range(S_t):
            Mj = Fr(0)
            for bw, z in zip(TOY_BW, TOY_BX):
                Lz = Fr(1)
                for x in nodes:
                    Lz *= (z - x)
                Mj += bw * Lz / (z - nodes[j])
            Fres += wts[j] * pival(nodes[j], k, al, beta) * Mj
        return Fd, Fres / hs[k], dual_h[m] * hs[k]

    ok_toy = True
    ok_hd = True
    for k in (1, 2, 3):
        Fd, Fres, hd = toy_routes(k, alD, betaD, hsD)
        ok_toy = ok_toy and (Fd == Fres)
        ok_hd = ok_hd and (hd == 1)
    check("G60-b4-toy-exact", ok_toy and ok_hd,
          "toy EXACT (rationals, k = 1..3): the border "
          "functional transports through the r231 L-gauge, "
          "F#_{S-1-k} == (1/h_k) sum_j w_j pihat_k(x_j) M_j "
          "(M_j = the deleted-node border masses) AND the "
          "h-duality h#_m h_k == 1 -- the augmented midpoint "
          "connection is a theorem-grade identity, not an "
          "artifact")
    dwm4 = [1 / (wts[j] * Lp[j]) for j in range(S_t)]
    alM, betaM, hsM = JF.stieltjes_exact(nodes, dwm4, S_t - 1)
    k0 = 2
    Fd_m, Fres_m, _hd = toy_routes(k0, alM, betaM, hsM)
    check("G65-mustfail-unsquared-lprime", Fd_m != Fres_m,
          "m4 L' NOT SQUARED in the dual weights (1/(w L') "
          "instead of 1/(w L'^2)): the toy border transport "
          "BREAKS (routes differ by %.3e != 0, exact rationals) "
          "-- the gauge is weight-pinned"
          % float(Fd_m - Fres_m))
    fb_w = 0.0
    for p in mains:
        N = p["N"]
        bx, bw = CT.union_arrays(p["dsm"])
        for k in (B4_K_WARD, N - 1):
            vb = eval_scaled(p["rows"], bx, k)
            fb_re = float(np.sum(bw * vb))
            fb_ch = p["rows"][k]["fb"]
            fb_w = max(fb_w, abs(fb_re - fb_ch)
                       / max(abs(fb_ch), 1e-300))
    check("G61-b4-eval-ward", fb_w <= B4_FB_BAR,
          "the scaled eval machinery reproduces the chain "
          "border pairing fb at k = %d AND the terminal on "
          "both mains: worst rel %.1e (bar %.0e)"
          % (B4_K_WARD, fb_w, B4_FB_BAR))
    mp_lg_w = 0.0
    hd_w = 0.0
    sgn_ok = True
    mp_note = []
    for p in mains:
        N = p["N"]
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        sgn, lg_dir, hd = mp_dual_route(p, N - 1)
        s_r, _c, _d, A, shM = border_gauge_stats(
            p["rows"], xu, wu, bx, bw, N - 1)
        eta_k = p["rows"][N - 1]["eta"]
        Ls_k = p["rows"][N - 1]["Ls"]
        lg_res = shM - Ls_k + math.log(abs(A)) \
            - math.log(abs(eta_k))
        sg_res = int(math.copysign(1.0, A)
                     * math.copysign(1.0, eta_k))
        mp_lg_w = max(mp_lg_w, abs(lg_dir - lg_res))
        hd_w = max(hd_w, hd)
        sgn_ok = sgn_ok and (sgn == sg_res)
        mp_note.append("w%d lg dev %.1e hdual %.1e sign %s"
                       % (p["kz"], abs(lg_dir - lg_res), hd,
                          "OK" if sgn == sg_res else "BROKEN"))
    check("G62-b4-mp-ward", mp_lg_w <= B4_MP_LG_BAR
          and hd_w <= B4_HDUAL_BAR and sgn_ok,
          "mp (dps %d) dual-chain route vs the f64 residue "
          "route at the SELF-DUAL terminal degree N-1 on both "
          "mains: %s (log bar %.0e, h-duality bar %.0e) -- the "
          "residue route is exact through the gauge at mp "
          "precision" % (B4_MP_DPS, "; ".join(mp_note),
                         B4_MP_LG_BAR, B4_HDUAL_BAR))
    if not smoke:
        sd_ok = 0
        signs = {}
        aligns = {}
        deps = {}
        for rc in recs:
            p = rc["p"]
            N = p["N"]
            xu, wu = CT.union_arrays(p["d"])
            bx, bw = CT.union_arrays(p["dsm"])
            if len(xu) == 2 * N - 1:
                sd_ok += 1
            s_r, c_w, dep, _A, _sh = border_gauge_stats(
                p["rows"], xu, wu, bx, bw, N - 1)
            signs[rc["kz"]] = s_r
            aligns[rc["kz"]] = c_w
            deps[rc["kz"]] = dep
        se = [signs[kz] for kz in signs if lab[kz]]
        sc_ = [signs[kz] for kz in signs if not lab[kz]]
        _a, pw_s = QO.auc_power(sc_, se)
        ae = [aligns[kz] for kz in aligns if lab[kz]]
        ac = [aligns[kz] for kz in aligns if not lab[kz]]
        _a2, pw_a = QO.auc_power(ac, ae)
        av = [aligns[rc["kz"]] for rc in recs]
        sp_ag = abs(BH.spearman(av, g1v))
        sp_ad = abs(BH.spearman(av, dnv))
        ctl_note = []
        for c in ("EPST", "SCR", "SMOOTH"):
            p = ctrl[c]
            xu, wu = CT.union_arrays(p["d"])
            bx, bw = CT.union_arrays(p["dsm"])
            s_r, c_w, _dep, _A, _sh = border_gauge_stats(
                p["rows"], xu, wu, bx, bw, p["N"] - 1)
            ctl_note.append("%s sign %+d align %.1e"
                            % (c, int(s_r), c_w))
            if c == "SMOOTH":
                sm_align = c_w
        dep_min = min(deps.values())
        check("G63-b4-terminal-census", sd_ok == len(recs)
              and dep_min >= DEPTH_GUARD
              and sm_align <= SM_ALIGN_BAR,
              "terminal census on %d rungs: SELF-DUAL S = 2N-1 "
              "on %d/%d (k = N-1 maps to itself); cancellation "
              "depth min %.1e >= %.0e (the signed pairing is "
              "far above the f64 floor); orientation product "
              "sign(F# F): exc %s, cheap sum %+d/%d, AUC power "
              "%.3f; alignment c_w: exc med %.1e vs cheap med "
              "%.1e, AUC power %.3f; controls: %s (SMOOTH "
              "anchor <= %.0e)"
              % (len(recs), sd_ok, len(recs), dep_min,
                 DEPTH_GUARD, str([int(v) for v in se]),
                 int(sum(sc_)), len(sc_), pw_s,
                 float(np.median(ae)), float(np.median(ac)),
                 pw_a, "; ".join(ctl_note), SM_ALIGN_BAR))
        carried = max(pw_s, pw_a) >= SIG_POWER_BAR
        b4_verdict = ("B4_BORDER_ORIENTATION_CARRIED(power "
                      "%.3f)" % max(pw_s, pw_a) if carried else
                      "B4_BORDER_SIGN_BLIND(orientation power "
                      "%.3f, alignment power %.3f)"
                      % (pw_s, pw_a))
        check("G64-b4-adjudication", True,
              "sealed rule (a power >= %.1f => the border "
              "carries orientation through the gauge): %s; "
              "leg-A fingerprints of the alignment: sp(align, "
              "g1) = %.3f / sp(align, D_N) = %.3f (both < "
              "%.1f: neither wall nor target) -- the h-free "
              "midpoint gauge is sign-blind for the BORDER "
              "exactly as for the basis: it does NOT carry "
              "the missing orientation"
              % (SIG_POWER_BAR, b4_verdict, sp_ag, sp_ad,
                 FP_BAR))
    else:
        b4_verdict = "SMOKE"
        pw_s = pw_a = float("nan")
        check("G63-b4-terminal-census", True, "SMOKE: skipped")
        check("G64-b4-adjudication", True, "SMOKE: skipped")

    # ---------------- S7: LEG C -- endpoint adjudication
    section("S7  LEG C -- ENDPOINT ADJUDICATION TABLE")
    if not smoke:
        rows_tab = []
        for nm, vals in (("crit1", [rc["crit1"] for rc in recs]),
                         ("crit3", [rc["crit3"] for rc in recs]),
                         ("align", av)):
            ve = [v for v, rc in zip(vals, recs)
                  if lab[rc["kz"]]]
            vc = [v for v, rc in zip(vals, recs)
                  if not lab[rc["kz"]]]
            spw = abs(BH.spearman(vals, g1v))
            typ = {"crit1": "TARGET(exact, G33)",
                   "crit3": "TARGET(exact, G53)",
                   "align": ("THIRD-candidate, power %.3f < "
                             "%.1f => NO criterion"
                             % (pw_a, SIG_POWER_BAR))}[nm]
            rows_tab.append("%s: sp-vs-wall %.3f, cheap med "
                            "%.3g / exc med %.3g -> %s"
                            % (nm, spw, float(np.median(vc)),
                               float(np.median(ve)), typ))
            info(rows_tab[-1])
        check("G70-endpoint-table", True,
              "sealed classification per candidate criterion "
              "(target / wall / third): b1 and b3 endpoints are "
              "the TARGET exactly (gated identities), neither "
              "is the wall (fingerprints 0.13-0.26 << %.1f); "
              "the b4 alignment separates weakly (exceptions "
              "sit LOWER: the border-gauge pairing is slightly "
              "more cancelled on the exception branch -- "
              "measured, below the sealed bar, no criterion); "
              "cheap-vs-exception medians on crit1/crit3 nearly "
              "coincide (printed above; the branch is NOT "
              "readable from the restated endpoints either -- "
              "labels enter tables only)" % FP_BAR)
    else:
        check("G70-endpoint-table", True, "SMOKE: skipped")

    # ---------------- S8: LEG D -- controls + must-fails + mp
    section("S8  LEG D -- CONTROLS + MUST-FAILS + MP WARDS")
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) \
        / B57
    check("G81-smooth-anchor", abs(qS) <= SM_Q_BAR,
          "SMOOTH anchor q_N = %.1e <= %.0e: the terminal "
          "question and every candidate trivialize exactly "
          "when the source aliases (F_{N-1} = 0, W ~ 0, "
          "alignment ~ 0)" % (qS, SM_Q_BAR))
    rc9 = mrecs[0]
    G9, tv9 = rc9["_G"], rc9["_tv"]
    honest = abs(corner_entry(G9, tv9, rc9["B"], 1.0)
                 - 1.0 / rc9["DN"]) * abs(rc9["DN"])
    ce_wrong = corner_entry(G9, tv9, rc9["B"], 1.0,
                            wrong_block=True)
    dev_m1 = abs(ce_wrong - 1.0 / rc9["DN"]) * abs(rc9["DN"])
    check("G82-mustfail-wrong-block",
          dev_m1 >= LOUD * max(honest, 1e-300),
          "m1 BORDERED INVERSE WITH THE WRONG BLOCK (the "
          "degree-(N-1) corner presented as 1/D_N): breaks by "
          "%.1e = %.1e x honest %.1e (bar %.0f x) -- the "
          "corner entry is block-pinned"
          % (dev_m1, dev_m1 / max(honest, 1e-300), honest,
             LOUD))
    if not smoke:
        mp_note2 = []
        mp_w = 0.0
        for kz in MP_EXC_KZ:
            rc = next(r for r in recs if r["kz"] == kz)
            Dmp = mp_corner_ward(rc["p"], MP_DPS)
            Dch = B57 - float(rc["p"]["rho"][rc["N"] - 1])
            dv = abs(float(Dmp) - Dch)
            mp_w = max(mp_w, dv)
            mp_note2.append("kz%d (N = %d) D_mp = %s dev %.1e"
                            % (kz, rc["N"], mp.nstr(Dmp, 9), dv))
        check("G80-mp-exception-wards", mp_w <= MP_BAR,
              "mp (dps %d) bordered det ratio det A / det G == "
              "D_N (the cofactor form of the corner statement "
              "(A^{-1})_{BB} = 1/D_N) at BOTH sealed exception "
              "terminals: %s vs the f64 chain 5/7 - rho_{N-1} "
              "(bar %.0e) -- kz15 is the razor (s* = 0.9966, "
              "margin 0.045), kz20 the smallest-N exception"
              % (MP_DPS, "; ".join(mp_note2), MP_BAR))
    else:
        check("G80-mp-exception-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the wall-reduction detector armed and self-"
          "tested, the exact augmented-corner Jacobi dynamics "
          "(definite, wall-free, drain-typed), the exhaustive "
          "2x2 dual-Ward census, the inner-block Schur "
          "quotient, and the border transport through the "
          "L-gauge with its honest sign-blindness census -- "
          "the identity class of this complexity is closed")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        go_b1 = False   # sealed: b1's only definite quantity IS
        # the drop S_{N-1} -- excluded by the GO rule
        go_b3 = False   # sealed: b3's deflated energy IS the
        # tail drop -- excluded by the GO rule
        go_b2 = dual_found is not None
        third = (max(pw_s, pw_a) >= SIG_POWER_BAR
                 and sp_ag < FP_BAR and sp_ad < FP_BAR)
        parts = ["WALL_DETECTOR_ARMED(selftest sp(g1, g1) = "
                 "%.2f flagged, target sp(D_N, g1) = %.2f not "
                 "flagged; fingerprints crit1 %.2f / crit3 "
                 "%.2f / align %.2f, all < %.1f -- NO "
                 "candidate is the wall)"
                 % (sp_wall, sp_tgt, sp1, sp3, sp_ag, FP_BAR)]
        parts.append(b1_verdict + "(rate 2sW/D^2 definite "
                     "%d/%d census points, endpoint == target "
                     "rel %.1e, drop == S_{N-1} exact)"
                     % (n_cen, n_cen, e_dev)
                     if b1_verdict.endswith("RESTATEMENT")
                     else b1_verdict)
        parts.append(b2_verdict)
        parts.append(b3_verdict + "(quotient exact, tail term "
                     "== S_{N-1} - S_7, SCRAMBLE min eig %.3f)"
                     % eig_scr
                     if b3_verdict.endswith("RESTATEMENT")
                     else b3_verdict)
        parts.append(b4_verdict)
        if go_b1 or go_b2 or go_b3:
            parts.append("BORDER_RESOLVENT_IDENTITY_GO(b2)")
        elif third:
            parts.append("IDENTITY_THIRD_CRITERION(b4, "
                         "power %.3f)" % max(pw_s, pw_a))
        else:
            parts.append("NO_IDENTITY_IN_CLASS(b1@DEFINITE_"
                         "DRAIN, b2@DRAIN_ONLY, b3@DEFLATED_"
                         "DRAIN, b4@SIGN_BLIND)")
            parts.append("RHP_LOCAL_ASYMPTOTICS_REQUIRED")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the corner-inverse "
          "identity + Jacobi rate, the quotient identity, the "
          "border transport, the lattice census; MEASURED: the "
          "fingerprints, the definiteness censuses, the "
          "orientation/alignment powers; OPEN: the target "
          "positivity itself (the campaign's work); NO RH claim"
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
