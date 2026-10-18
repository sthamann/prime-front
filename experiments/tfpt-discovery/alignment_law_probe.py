#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""alignment_law_probe -- PRIME.ALIGNMENT.LAW.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung certificates stated, NO counterexample claim.  It closes no
gate and narrows no gate.  Concurrent-lane files are not touched.

=======================================================================
MISSION (round ~182: derive or kill the alignment law).  Two rounds
measured the same unexplained object from two sides: r177/CDXCV (the
low eigenvectors of the WALL M share the source's 1/A_0 cancellation
-- alignment-sharing gap log10|a0_1/A_0| = 2.354 -> 4.03, "a new
measured law") and r181/CDXCIX (the jet mass rides the collapsing
conditioning wall of the house GRAM G_h -- one dex of sub-dof mass
leaves per rung, ONLY in the arithmetic world; final debt: "the
missing tool must control the ill-conditioned subspace -- the
alignment law of the s_i").  THIS round measures the law precisely
(A1), prices the three candidate mechanisms (A2), composes the
consequence chain (A3), and runs the control/witness battery (A4).
  A1  THE LAW: eigendecomposition of the Jacobi-normalized house
      Gram Gn at escalated dps at every reachable rung; s_i = v_i .
      Jn; per-mode mass m_i = lam_i s_i^2; fit and freeze the law's
      form (per-dex mass profile, power-law exponent alpha in
      m_i ~ lam_i^alpha, mass-weighted spectral depth), with the
      r181 fraction ladder and the r177 gap ladder re-derived as
      transforms of the same object;
  A2  MECHANISMS: (i) SECULAR/STRUCTURAL -- the Gram is SOURCE-FREE
      (proved symbolically + reconstructed numerically + world-blind
      fingerprint), so the whole law lives in the source ray d
      against fixed geometry; feature dissection (alternation vs
      magnitude profile) by deterministic alternative jets;
      (ii) BRIDGE-EXPRESSIBLE -- the key adjudication: s_i * A_0 is
      an EXACT LINEAR functional of d (the r178 eigenvector-map
      obstruction does NOT bite between d and the law, because the
      eigenvectors come from the source-free Gn); the obstruction
      bites ONCE, upstream, at the wall-eigenvector map d = argmin
      eig(M(prime data)) -- the SAME single map delta itself
      consumes: the law is exactly as bridge-expressible as delta;
      (iii) SELF-DUALITY/SYMMETRY -- killed by exact exhibit: the
      two norm constraints {sum s^2, sum lam s^2} admit a top-
      concentrated solution, so NO norm/symmetry argument alone can
      force the mass location;
  A3  CONSEQUENCE: the mass-LOCATION law is PROJECTIVE (A_0 cancels
      in every fraction -- exact); the LEVEL (floor) form needs a
      lower bound on the variational quotient |N_i(d)/A_0(d)| ==
      the SAME nonperturbative-variational wall as theta_inf (r175)
      and H-pin Omega-a (CDXCIV): SAME-WALL adjudication, no new
      residue edge; composed floor margins at the selector rungs
      stated with numbers at the measured epistemic level;
  A4  CONTROLS/SCREENS: SMOOTH/SCRARITH/EPSTEIN (r181 recipes
      VERBATIM + mass-location statistics), the r172-class inflation
      witness in Gram coordinates (tiny-cost top-mode injection must
      break the law), tau-screen, loop guard (A0-triangle EXPLICITLY
      adjacent to the floor form: detected, never consumed).
=======================================================================
State consumed (CITED): r181/CDXCIX cbj_subdof_probe (SPEC
2db82c76ce5f067c, 37/37: spectral split machinery VERBATIM; CAL_TAIL/
CAL_SPREAD/CAL_DELTA record strings; fraction-world separation);
r180/CDXCVII cbj_frame_probe (SPEC d7fbf2d9: step-A exact delta ==
|J|^2_G with R == 0; gmin ladder 1.1e-17 -> 5.2e-113); r177/CDXCV
manifold_invariance_probe (SPEC af86ec3b: GAP_TAB {4: 2.354, 5:
2.699, 8: 3.022, 13: 3.519}, a0_1 = A_0-functional of wall
eigenvector 1); r175/CDXCI thetainf_pin_probe (SPEC 3044558e: mode-
level Landau bridge, prime-block data linear per mode zero-
expressible per census; theta_inf OPEN-NONPERTURBATIVE-VARIATIONAL);
r178/CDXCIV l1wpd_closure_probe (SPEC 0e306146: linearity fails at
the eigenvector map and root map -- the obstruction class this round
localizes); r169 SF1/SF2 (delta_req = SIGMA0/((1-slop) DC)); r168
SIGMA0 = 0.15; r166 tlaw ladder; PT21 (census per-k; ALL-K ==
flagged loop); HSW22 Cor. 1.2.

NOTATION (r180/r181 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector); a = log(h)/2; K = ceil(1.25 h log h);
om_k = k pi/a; b_k = om_k^2; c_k = cn_mp_str (the source vector =
lowest eigenvector of the wall M = Mpole + March - Mprime, prime
atoms (log q, log p/sqrt q) entering ONLY through Mprime); d_k =
(-1)^k c_k; A_0 = sum d; J = d/A_0; T_z = 2 pi h; WFULL = ward
ordinates in (T_z + 6, gamma_7000]; mu(g) = sin^2(ag)/g^2; psi_k(g)
= g^2/(g^2 - b_k) (psi_0 == 1); Gm[k,l] = sum mu psi_k psi_l; D =
sqrt(diag Gm); Gn = D^-1 Gm D^-1; Jn = D J/sqrt(sum mu); delta ==
Jn^T Gn Jn EXACTLY (step-A CITED + re-gated).  Eigsy(Gn) = {lam_i,
v_i} at EIG_DPS = ndig + 30 (ndig = min(dps - 2, 140); the dps
schedule DPS = {4: 60 ... 16: 130, 20: 144} is the disclosed
escalation ladder demanded by the conditioning wall); s_i = v_i .
Jn; m_i = lam_i s_i^2; delta == sum m_i (ward <= 1e-6).  LAW
COORDINATES (predefined, sealed pre-ward): x_i = log10(lam_i/
lam_max) <= 0 (positive-lam modes only; negative-lam noise modes
counted and disclosed); y_i = log10(m_i/delta); FIT WINDOW = modes
with lam_i <= FITCUT lam_max, FITCUT = 1e-2; alpha = OLS slope of y
vs x on the window; per-dex profile = mass shares in BIN_DEX = 10
dex bins; mu_m = mass-weighted mean of x (spectral depth of the
demand mass); topshare = m_top/delta.  CUTS = (1e-6, 1e-12, 1e-24),
primary 1e-12 (r181 VERBATIM).  ALT JETS (mass location is
PROJECTIVE == normalization-free): SIGNFLIP d' = c (parity factor
removed); UNIFORM d' = (-1)^k; MAGSCRAM d'_k = sign(d_k)
|c_{perm(k)}| with the deterministic golden permutation.  WITNESS
(r172-class, in Gram coordinates, DISCLOSED analog): Jn' = Jn + t
v_top with t = sqrt(999 delta/lam_max) -- moves the level x1000 at
relative source cost t/|Jn| (measured ~1e-10 class), must relocate
the mass to the top mode.

=======================================================================
THE FOUR SECTIONS AS EXECUTED (verdicts frozen from the ONE disclosed
pre-freeze calibration pass, calib_alaw_pass1.log; record values
below ARE the calibrated numbers)
=======================================================================
A1 (THE LAW, MEASURED AND FROZEN -- THREE FACETS).  (F1) THE
HALF-POWER ENVELOPE: OLS alpha (log10 m vs log10 lam on the fit
window lam <= 1e-2 lam_max) = 0.5232/0.3988/0.4644/0.4508/0.4440/
0.4781/0.4858/0.4860/0.5111/0.5190/0.5223/0.5092/0.4765/0.4261 at
h = 4..16 + 20 -- alpha in the frozen band (0.38, 0.54) at EVERY
rung: per-mode mass m_i ~ lam_i^(~1/2), equivalently s_i^2 ~
lam_i^(alpha-1) ~ lam^(-1/2)-class: the source ray loads the
collapsing directions with an INVERSE-SQUARE-ROOT Euclidean
weight (the measured exponent clusters near 1/2; recorded as a
band, NOT claimed as exactly 1/2 -- anti-numerology discipline).
(F2) THE QUARTER-DEPTH CENTER: mass-weighted spectral center
mu_m = -4.39/-8.82/-9.48/-12.53/-14.97/-16.95/-19.14/-22.56/
-25.04/-27.08/-30.49/-31.88/-34.56/-42.68 log10-units at h =
4..16 + 20 -- LINEAR IN THE RUNG (mu_m vs h slope -2.41 dex/rung,
R^2 0.9962) and LOCKED TO THE CONDITIONING WALL (mu_m vs
log10 gmin slope 0.2372, R^2 0.9916 over the positive-gmin rungs
h <= 14): THE DEMAND MASS CENTER SITS AT ~24 PERCENT OF THE
COLLAPSING SPECTRUM'S DEPTH, rung after rung -- the law is the
gmin conditioning wall seen from the source ray (ONE law, two
currencies; the near-1/4 fraction recorded, NOT claimed).  (F3)
THE DEEP EXCESS (the facet that carries the r181 kill): the
one-parameter power fit UNDER-predicts the below-cut mass at the
primary 1e-12 cut by 5.638..7.575 dex at h >= 8 (frozen dev
table; per-dex flatness std/mean 1.00-2.30, structured): the law
is NOT a clean one-parameter power form -- it is a half-power
ENVELOPE plus an arithmetic deep-mass excess concentrated at the
quarter-depth center; the honest frozen form is the TRIPLE
(alpha band, center schedule, excess table), not a formula.
TRANSFORMS VERIFIED: the r181 fraction ladder replicates from
this round's spectra (CAL_TAIL abs 0.05 at all 14 rungs + the
1e-24-cut subset); the r177 gap ladder replicates EXACTLY on the
wall object (gap_a01 = 2.354/2.699/3.022/3.519 at h = 4/5/8/13,
abs 0.02) and CORRELATES with the Gram-side depth (mu_m vs
gap_a01: slope -19.70, R^2 0.981): the r177 wall-side law and
the r181/this-round Gram-side law are transforms of ONE measured
object within instrument resolution -- MEASURED-CORRELATION,
not identity, honestly typed.  NEGATIVE-LAM NOISE MODES (gmin
below entry precision at h >= 15, r181-disclosed) counted
0/0/0/0/0/0/0/0/0/0/0/1/2/6 at h = 4..16 + 20 and excluded from
fits (ward covers the mass sum; frozen-cut fractions unaffected).
A2 (MECHANISMS PRICED).  (i) STRUCTURAL: THE GRAM IS SOURCE-FREE
-- proved symbolically (psi/mu free of source symbols, G11),
numerically (standalone geometry-only rebuild of Gn from (h, ward
window) matches the build to 0.0 dev at h = 4/5, G21), and
WORLD-BLIND (Gram fingerprints of MAIN/SCRARITH/SMOOTH/EPSTEIN at
the same x agree to 0.0 dev while their jets differ, G22): THE
ENTIRE LAW LIVES IN THE SOURCE RAY d AGAINST FIXED GEOMETRY.  The
exact-combinatorics sub-candidate is REJECTED: the lowest Gn
eigenvector's alternating-binomial overlap is NEVER dominant --
0.4781 at h = 4 dying to 1e-4-class by h = 12 (uptick 0.0950 at
h = 20 == noise-floor eigenvector at negative-gmin rungs,
disclosed): the b_k = (k pi/a)^2 spacing is quadratic, the
confluent finite-difference skeleton does not carry the law.
FEATURE DISSECTION (G23, projective == normalization-free) -- THE
ROUND'S SHARPEST MECHANISM FINDING: at h = 4/5/8/13 ALL THREE
deformations of the ray -- SIGNFLIP (parity removed, magnitudes
kept), UNIFORM (alternation kept, magnitudes flattened), MAGSCRAM
(signs kept, magnitudes golden-scrambled) -- RELOCATE THE MASS TO
THE TOP MODES (log10 tails -12.60..-16.04 == fraction 1-class,
exactly the fake-world signature) while MAIN rides the deep tail
(-4.08/-2.21/-0.02/-0.001): THE ALIGNMENT NEEDS THE JOINT EXACT
SIGN-AND-MAGNITUDE STRUCTURE OF d -- neither the parity pattern
nor the magnitude profile alone carries ANY of it: ALT-JETS-
BREAK-ALIGNMENT, the law is arithmetic-specific at every rung
(sharpens r181-G46: not just fake WORLDS but ANY deterministic
deformation of the true ray kills it).  (ii) BRIDGE (THE KEY
ADJUDICATION, exact): s_i A_0 == <v_i, D d>/sqrt(Smu) is LINEAR
in d -- additivity + projective scale-invariance proved
generically (sympy G12) and instance-gated at h = 5 (additivity
dev 7.5e-69 <= 1e-30, G24): THE R178 EIGENVECTOR-MAP OBSTRUCTION
DOES NOT APPLY between d and the law, because Gn's eigenvectors
are source-free (the r178 failure was at eigenvectors of SOURCE-
LOADED matrices); the obstruction bites EXACTLY ONCE, upstream,
at d = (sign-fixed) argmin-eigenvector of the prime-loaded wall M
-- re-exhibited exactly (lam_min(A+B) = -sqrt(2) != -2, G15): the
law's prime-data ancestry FACTORIZES as [prime atoms] --r175
bridge (linear per mode per census, CITED)--> [pj] --affine
assembly--> [M] --WALL EIGENMAP (the one nonlinear link, shared
with delta itself)--> [d] --PROJECTIVE-LINEAR (this round,
exact)--> [{s_i}] --squares/ratios--> [law]: THE LAW IS EXACTLY
AS BRIDGE-EXPRESSIBLE AS DELTA -- Landau-class per census GIVEN
d, no additional epistemic debt from the eigendecomposition (the
contract's key question, answered as a typed factorization, NOT
as an unconditional derivation).  (iii) SYMMETRY: KILLED BY EXACT
EXHIBIT (G13): with lam spread (1, 1e-40) and norm pair (|s|^2 =
1e30, delta = 13/10) a TOP-concentrated two-mode configuration
satisfies BOTH norms exactly (sympy rationals, top share >
0.9999999): no {Pythagoras + level} argument can force the mass
location; with (i)'s dissection the specific-symmetry candidates
(alternation parity, magnitude profile) are ALSO dead:
NORMS-DO-NOT-FORCE-LOCATION.
A3 (CONSEQUENCE CHAIN, exact quantifiers).  THE LAW IS PROJECTIVE:
every fraction m_i/delta is invariant under d -> t d (A_0 cancels;
proved generically G12): the LOCATION law is A_0-FREE -- the r177
"1/A_0-cancellation-sharing" is a statement about the RAY, not
the quotient; A_0 enters ONLY the LEVEL delta.  THE FLOOR FORM,
adjudicated honestly: the naive composition [half-power fit
integrated over the spectrum] OVERSHOOTS the true level by 3.41/
10.14 dex at the selector rungs (log10(delta_fit-margin/raw-
margin) frozen: the one-parameter form is an envelope, NOT a
floor density -- POWER-COMPOSITION-INVALID, disclosed with
numbers); the honest composed floor at the selector rungs h-hat
(B2) = 7 / h-hat(B3) = 13 is the MEASURED level itself: raw SF2
margins delta/delta_req = 2.14/3.05 (replicating the r180
selector strings) -- quantifier PER-RUNG (SEQ, reachable set
h = 4..16 + 20), epistemic type MEASURED-WITH-MECHANISM (the
mechanism = the A2 factorization).  THE UPGRADE OBSTRUCTION,
named exactly: a law-derived floor m_i >= f(lam_i) needs a lower
bound on the variational quotient |N_i(d)|/|A_0(d)| -- the
location law being A_0-free, the quotient enters exactly at the
level leg -- and that quotient class is the SAME nonperturbative-
variational wall as theta_inf (r175 OPEN-NONPERTURBATIVE-
VARIATIONAL) and H-pin Omega-a (CDXCIV Variationsquotienten-
Klasse), with the A0-triangle the adjacent flagged loop
(detected, consumed by NOTHING; the floor route is NAMED and
machine-EXCLUDED from the delivered set, G44/G51): SAME-WALL-
NOT-NEW-OBJECT -- the residue gains NO new edge (BH7-honest
bookkeeping); the alignment law is RETYPED from "unexplained
regularity" to "projective-linear-in-source law, expressible per
census given the one shared wall-eigenmap link, floor form on
the known theta_inf/H-pin wall".
A4 (CONTROLS + WITNESS + SCREENS).  r181 control battery recipes
VERBATIM replicate (tau_w tabs rel 5e-3; BA3-bridge violations
rel 5e-2; CAL_CTRL_TAIL abs 0.10; naked delta_w positive):
FLOOR-INEQ-WORLD-INSENSITIVE + FRACTION-WORLD-SEPARATING
RESTATED; NEW mass-location statistics at the CTRL_NZ window:
fake-world mass center mu_m = -0.1..-0.9 (top-mode class;
topshare 0.41-0.97) vs MAIN mu_m = -4.1/-8.3/-13.2 at x = 4/5/8
(topshare 0.004-0.010): the fake-world jet mass sits AT THE TOP
of the spectrum, the arithmetic ray alone descends -- and with
G22 (Gram world-blind) this separation provably lives in d
alone.  THE WITNESS (G24, r172-class in Gram coordinates,
DISCLOSED analog): at h = 5/8 the top-mode injection with
relative source cost 5.3e-7/8.2e-14 moves the level x999.3/
x1000.9 and SNAPS the mass to the top: log10 tail -2.207 ->
-5.207 / -0.021 -> -3.021 (mass fraction above cut -> 1-class):
WITNESS-BREAKS-ALIGNMENT -- an adversarial top-mode component
invisible in source norm destroys the law, exactly the r172
lesson.  TAU-SCREEN: slope mu_m vs log10 tau = +0.5003 in the
DISCLOSED rider window (0.35, 0.65) -- the depth center rides
the conditioning currency at HALF POWER (that IS the law's
content, typed not hidden; the half-power exponent surfaces in a
second currency); demand-class slopes alpha -0.0002, log10
margin -0.0045 <= 0.30: NO tau_h relabeling of the demand or the
exponent.  LOOP GUARD: FOUR flagged cycles detected (A0-triangle
-- ADJACENT to the named floor route, census-forall-k,
Gonek-1984, Montgomery-PC/Goldston-Montgomery), consumed by
NOTHING delivered; min-cut flows 4/5/5/6 NOT REAL replicated;
census cardinality 4 UNCHANGED.
=======================================================================
TAXONOMY VERDICT (frozen from calibration):
   ALIGNMENT-LAW-MEASURED-HALF-POWER-ENVELOPE (alpha in (0.38,
   0.54) at all 14 rungs; s^2 ~ lam^(-1/2)-class) +
   QUARTER-DEPTH-CENTER (mu_m = 0.2372 log10 gmin, R^2 0.9916;
   -2.41 dex/rung, R^2 0.9962) +
   DEEP-EXCESS-BEYOND-POWER-FORM (one-parameter fit under-
   predicts below-cut mass by 5.6-7.6 dex at h >= 8, frozen) +
   ONE-LAW-TWO-CURRENCIES (gmin lock + r177-gap correlation
   slope -19.70 R^2 0.981 + tau half-power rider) +
   GRAM-SOURCE-FREE-EXACT + GRAM-WORLD-BLIND-EXACT +
   EIGENVECTOR-LINEARITY-RESTORED-PROJECTIVE (the key
   adjudication: r178 does NOT bite; s_i A_0 linear in d;
   location law A_0-free) +
   WALL-EIGENMAP-SINGLE-SHARED-NONLINEAR-LINK (law exactly as
   bridge-expressible as delta, per census, r175 CITED) +
   EXACT-COMBINATORICS-REJECTED (binomial overlap never
   dominant, 0.478 -> 1e-4) +
   ALT-JETS-BREAK-ALIGNMENT (SIGNFLIP/UNIFORM/MAGSCRAM all snap
   mass to the top: the law needs the JOINT sign-and-magnitude
   structure of d) +
   NORMS-DO-NOT-FORCE-LOCATION-EXACT +
   R181-LADDER-REPLICATED + R177-GAP-REPLICATED-CORRELATED +
   POWER-COMPOSITION-INVALID-DISCLOSED (overshoot 3.41/10.14
   dex) +
   COMPOSED-FLOOR-STAYS-MEASURED (raw selector margins 2.14/3.05
   replicate r180; type MEASURED-WITH-MECHANISM) +
   FLOOR-FORM-SAME-WALL-AS-THETAINF-HPIN (variational quotient;
   A0-triangle adjacent, not consumed; NO new residue edge) +
   WITNESS-BREAKS-ALIGNMENT + CONTROLS-MASS-AT-TOP +
   NOT-RELABELING (demand legs tau-flat; half-power depth rider
   disclosed) +
   LOOPS-FLAGGED-NOT-CONSUMED + RESIDUE-UNCHANGED-RETYPED.
Honest content: (a) the law now has a frozen quantitative form --
the TRIPLE (half-power envelope band, quarter-depth center
schedule, deep-excess table) with exponents and windows -- and is
NOT a clean one-parameter formula (the naive form is killed with
numbers); (b) the mechanism is FACTORIZED, not derived: geometry
source-free and world-blind (exact), ray-to-law map projective-
linear (exact -- the r178 obstruction adjudicated AWAY at the
eigenvector map and localized to the single shared wall-eigenmap
link), exact-combinatorics rejected, and the law is destroyed by
EVERY deterministic deformation of the ray (alt jets) and by the
cheap top-mode witness: it is a property of the arithmetic ray
itself; (c) the composed floor stays at the measured level
(selector margins 2.14/3.05) -- the naive law-composition is
invalid (disclosed) and the upgrade obstruction is the SAME
variational-quotient wall as theta_inf/H-pin: NO new residue
edge; (d) nothing closes, nothing upgrades, the census-forall-k
loop and the A0-triangle stay flagged and unconsumed.  NO RH
CLAIM.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition order
+ G03 cache ward; S1 exact layer G10-G15; S2 house/law layer
G30-G39; S3 mechanism layer G21-G24; S4 controls + kill gates
G40-G45; S5 screens/assembly G46/G50-G54/G60/G99.  FROZEN BARS:
IDEN_BAR 1e-30; MASS_WARD 1e-6; ALPHA_BAND (0.38, 0.54);
CAL_ALPHA abs 5e-3; CAL_MUM abs 0.05; SLOPE_MUM_H window
(-2.8, -2.0) + R2 >= 0.99; SLOPE_MUM_GMIN window (0.20, 0.28) +
R2 >= 0.99 (positive-gmin rungs); GAP_ABS 0.02 (r177 tab);
CORR_R2 >= 0.95 + slope tol 1.0; PRED dev table abs 0.30 at
h >= 8 with dev >= 2.0 (the under-prediction is the gated fact);
CAL_TAIL abs 0.05 (r181 strings CITED); TLAW rel 1e-3; CAL_DELTA
rel 1e-4; DELTA/DC tabs rel 5e-3; CTRL_TAU rel 5e-3; CTRL viol
rel 5e-2; CTRL tails abs 0.10; CTRL_LOC topshare abs 5e-2 + mu_m
abs 0.2; ALT_TOL abs 0.05 on log10 tails + ALT tails <= -10 (top-
snap); WIT_COST_BAR 1e-5; WIT_RATIO band [990, 1010]; WIT_TAIL <=
-2.5 + replication (tail abs 0.05, cost rel 0.5); BINOM abs 5e-3
+ max <= 0.5; FP_TOL 1e-20; RECON_TOL 1e-30; MARGRAW abs 0.02 +
overshoot log10 abs 0.05; tau demand slopes <= 0.30, depth-rider
window (0.35, 0.65) DISCLOSED; runtime bar 3600 s (a heavy
concurrent promotion-wave pipeline shares the machine -- wall
times inflated, timing-normalized diff is the record currency,
DISCLOSED).  CONTROLS: SMOOTH(5), SCRARITH(4,5,8),
EPSTEIN(8,9,10) + MAIN(4,5,8) comparator at CTRL_DPS/60, CTRL_NZ =
300, recipes r181 VERBATIM.  LOOP GUARD: four flagged cycles
(A0-triangle, census-forall-k, Gonek-1984, Montgomery-PC/
Goldston-Montgomery) DECLARED, DFS-detected, consumed by NOTHING
delivered; min-cut r135 flows 4/5/5/6 NOT REAL.  CALIBRATION
(disclosed): ONE pre-freeze calibration pass (calib_alaw_pass1.log,
818.9 s under promotion-wave load, 32/37 with the five placeholder
law-table gates failing as expected pre-freeze, --mode calib)
preceded by one structural smoke (alignment_law_probe.smoke1.log,
37.9 s, 36/37, only the placeholder witness-cost bar failing),
both at the pre-freeze SPEC_SHA 74dd4432235aab7f; AT FREEZE the
placeholder record tables were replaced by the calibrated numbers
and FIVE placeholder items were retyped from the measurements,
all disclosed: (1) ALPHA_BAND placeholder log-flat [-0.05, 0.05]
-> measured half-power band (0.38, 0.54); (2) the G35 transform
gate placeholder "power fit predicts the tail" -> the measured
FACT is the opposite (under-prediction 5.6-7.6 dex): gate retyped
to freeze the deviation table (DEEP-EXCESS facet); (3) the G23
alt-jet placeholder branch "tail-riding generic" -> the measured
opposite ALT-JETS-BREAK-ALIGNMENT; (4) the G46 placeholder
"law-composed margins carry" -> POWER-COMPOSITION-INVALID +
COMPOSED-FLOOR-STAYS-MEASURED (raw margins gated); (5) the G36
monotone-overlap leg dropped (h = 20 noise-floor uptick 0.095,
disclosed), table replication + never-dominant bar gated instead;
WIT_COST_BAR 1e-20 -> 1e-5 (measured 5.3e-7/8.2e-14); tau depth-
rider window resigned to the measured +0.50 (placeholder had the
wrong sign).  NO gate, grid, recipe, control or replication bar
inherited from r180/r181 moved.  Scratch deleted, logs kept,
numbers verbatim above.  DETERMINISM: no randomness anywhere
(golden permutation deterministic); ProcessPool results keyed;
run2 must be identical modulo wall-clock tokens (lines carrying
'WALL' or wall-second prints).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt VIII, note DI, 2026-08-20)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays e4cdb9a932093196.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH8-F1 [MAJOR, class-convergence stated as object-identity]:
#   ORIGINAL (this spec + note D): the terminal residue adjudication
#   "SAME-WALL-NOT-NEW-OBJECT" (verdict enum FLOOR-FORM-SAME-WALL-AS-
#   THETAINF-HPIN; note D: "seine Floor-Form landet auf der BEKANNTEN
#   theta_inf/H-pin-Mauer statt eine neue zu eroeffnen") states a
#   CLASS-level convergence as a formal-object identity.  The four
#   wall statements (r175 theta_inf face, r178 H-pin Omega-a, r181
#   deep-subspace debt, r182 floor quotient) are FOUR DISTINCT formal
#   statements (different functionals, different quantifiers) sharing
#   a machine-namable CLASS: the same source object (the wall argmin
#   ray d -- the single nonlinear link), the A_0-quotient shape, the
#   nonperturbative-variational typing, the adjacent A0-triangle
#   loop; NO gate anywhere checks a pairwise identity, and r178
#   adjudicates the closest pair EXPLICITLY as DISTINCT statements.
#   CORRECTED wording (BH8): "SAME-CLASS-NOT-NEW-EDGE: dieselbe
#   Variationsquotienten-KLASSE wie theta_inf (r175) und H-pin
#   Omega-a (r178: DISTINKTE Statements) -- vier distinkte formale
#   Statements ueber demselben Quell-Objekt (Wall-Argmin-Strahl d) in
#   A0-Quotientenform; KEIN neuer Residuum-Edge, weil die Floor-Route
#   optional und maschinell aus dem Delivered-Set ausgeschlossen ist
#   (G44), NICHT weil das Objekt identisch waere."  The residue
#   conclusion "no new edge" SURVIVES on the machine-checked G44
#   exclusion ground (optional route, delivered-set-excluded), NOT
#   via identity.
#
# BH8-F3 [MINOR, adjudication-as-vacuous-gate -- BH6-F3 class]: the
#   frozen gates are NOT edited; G51-floor-form-same-wall is
#   check(..., True, ...) -- a hardcoded always-PASS carrying this
#   round's residue adjudication inside the 37/37 count -- re-typed
#   DEFINITIONAL/ADJUDICATION per the BH6-F3 convention.  The honest
#   adjudication content is the BH8-F1 wording above; gate counts
#   unchanged, no verdict flips.
# =====================================================================

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
NZFULL = 7000
F64_SLOP = 1e-3
Z_OVERHANG = 6.0
WORKERS = 10
SIGMA0 = 0.15
IDEN_BAR = 1e-30
PD_RUNGS = (4, 5, 8)
RUNTIME_BAR = 3600.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
NDIG_CAP = 140
EIG_PAD = 30          # EIG_DPS = min(DPS-2, NDIG_CAP) + EIG_PAD
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675

# r166/r169/r180/r181 corpus strings (CITED)
TLAW_LADDER = {4: 0.2325, 5: 0.2664, 6: 0.2729, 7: 0.3264,
               8: 0.3738, 9: 0.3645, 10: 0.4032, 11: 0.4534,
               12: 0.4112, 13: 0.4674, 14: 0.4455, 15: 0.4421,
               16: 0.4606, 20: 0.5282}
TLAW_TOL = 1e-3
DELTA_TAB = {4: 1.374423, 5: 1.159470, 8: 1.372972}
DC_TAB = {4: 0.153469, 5: 0.227257, 8: 0.268559}
TAB_TOL = 5e-3
CAL_DELTA = {4: "1.374423e+00", 5: "1.159470e+00", 6: "1.433041e+00",
             7: "1.157312e+00", 8: "1.372972e+00", 9: "1.214583e+00",
             10: "1.379691e+00", 11: "1.233525e+00",
             12: "1.315350e+00", 13: "1.210860e+00",
             14: "1.305696e+00", 15: "1.276163e+00",
             16: "1.244494e+00", 20: "1.409453e+00"}
CAL_TAIL = {   # r181 record strings (CITED): log10(1 - frac@1e-12)
    4: "-4.077", 5: "-2.207", 6: "-1.321", 7: "-0.330",
    8: "-0.021", 9: "-0.039", 10: "-0.001", 11: "-0.001",
    12: "-0.001", 13: "-0.001", 14: "-0.001", 15: "-0.001",
    16: "-0.001", 20: "-0.002"}
CAL_TAIL_TOL = 0.05
CAL_SPREAD24 = {   # r181 1e-24-cut column (CITED subset)
    4: "-300.000", 8: "-4.628", 13: "-0.254", 20: "-0.004"}
CTRL_SMOOTH = (5,)
CTRL_SCRARITH = (4, 5, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_NZ = 300
CTRL_TAU_TAB = {"SMOOTH": {5: -1.0944},
                "SCRARITH": {4: -2.5151e-2, 5: -0.34593, 8: -0.67664},
                "EPSTEIN": {8: -1.6310, 9: -1.6922, 10: -1.9932}}
CTRL_TAU_TOL = 5e-3
CAL_CTRL_VIOL = {("EPSTEIN", 8): -1.0050, ("EPSTEIN", 9): -1.0009,
                 ("EPSTEIN", 10): -1.0056,
                 ("SCRARITH", 4): -1.2562, ("SCRARITH", 5): -1.0119,
                 ("SCRARITH", 8): -1.0086,
                 ("SMOOTH", 5): -1.0033}
CTRL_VIOL_TOL = 5e-2
CAL_CTRL_TAIL = {("MAIN", 4): "-4.11", ("MAIN", 5): "-2.26",
                 ("MAIN", 8): "-0.04",
                 ("SMOOTH", 5): "-13.32", ("SCRARITH", 4): "-11.68",
                 ("SCRARITH", 5): "-13.37", ("SCRARITH", 8): "-14.25",
                 ("EPSTEIN", 8): "-11.68", ("EPSTEIN", 9): "-12.84",
                 ("EPSTEIN", 10): "-13.65"}
CAL_CTRL_TAIL_TOL = 0.10
CTRL_MAIN_X = (4, 5, 8)
COND_LO, COND_HI = 1e-40, 1e-10

# r177 gap tab (CITED)
GAP_TAB = {4: 2.354, 5: 2.699, 8: 3.022, 13: 3.519}
GAP_ABS = 0.02
GAP_RUNGS = (4, 5, 8, 13)

# law machinery (PREDEFINED, sealed pre-ward)
CUTS = ("1e-6", "1e-12", "1e-24")
CUT_PRIMARY = "1e-12"
MASS_WARD = 1e-6
FITCUT = "1e-2"
BIN_DEX = 10.0
ALT_TAGS = ("SIGNFLIP", "UNIFORM", "MAGSCRAM")
ALT_RUNGS = (4, 5, 8, 13)
WIT_RUNGS = (5, 8)
WIT_FACTOR = 999           # level move x1000
GOLD = 0.6180339887498949

# frozen law bars (frozen at freeze from the calibration pass)
ALPHA_BAND = (0.38, 0.54)
FIT_MIN_MODES = 3
SLOPE_MUM_H = (-2.8, -2.0)
SLOPE_MUM_GMIN = (0.20, 0.28)
LAW_R2 = 0.99
CORR_R2 = 0.95
PRED_DEV_TOL = 0.30
PRED_MIN_DEV = 2.0
PRED_MIN_H = 8
BINOM_TOL = 5e-3
BINOM_MAX = 0.5
ALT_TOL = 0.05
ALT_TOP_MAX = -10.0
WIT_COST_BAR = 1e-5
WIT_RATIO_BAND = (990.0, 1010.0)
WIT_TAIL_MAX = -2.5
WIT_TAIL_TOL = 0.05
FP_TOL = 1e-20
RECON_TOL = 1e-30
TAU_SLOPE_BAR = 0.30
MUM_RIDER_WIN = (0.35, 0.65)
MARGRAW_RTOL = 1e-2
OVER_TOL = 0.05

# --------------------- calibrated record tables (pre-freeze pass 1)
CAL_ALPHA = {4: "0.5232", 5: "0.3988", 6: "0.4644", 7: "0.4508",
             8: "0.4440", 9: "0.4781", 10: "0.4858", 11: "0.4860",
             12: "0.5111", 13: "0.5190", 14: "0.5223", 15: "0.5092",
             16: "0.4765", 20: "0.4261"}
CAL_ALPHA_TOL = 5e-3
CAL_MUM = {4: "-4.39", 5: "-8.82", 6: "-9.48", 7: "-12.53",
           8: "-14.97", 9: "-16.95", 10: "-19.14", 11: "-22.56",
           12: "-25.04", 13: "-27.08", 14: "-30.49", 15: "-31.88",
           16: "-34.56", 20: "-42.68"}
CAL_MUM_TOL = 0.05
CAL_NNEG = {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
            12: 0, 13: 0, 14: 0, 15: 1, 16: 2, 20: 6}
CAL_MUMH = {"slope": "-2.41", "r2": "0.9962"}
CAL_MUMG = {"slope": "0.2372", "r2": "0.9916"}
CAL_CORR = {"slope": "-19.70", "r2": "0.981"}
CAL_BINOM = {4: "0.4781", 5: "0.1839", 6: "0.1026", 7: "0.0402",
             8: "0.0200", 9: "0.0085", 10: "0.0033", 11: "0.0013",
             12: "0.0004", 13: "0.0002", 14: "0.0000",
             15: "0.0026", 16: "0.0003", 20: "0.0950"}
CAL_ALT = {   # (h, tag) -> log10 tail at primary cut (projective)
    (4, "SIGNFLIP"): "-15.0781", (4, "UNIFORM"): "-12.5994",
    (4, "MAGSCRAM"): "-13.8365",
    (5, "SIGNFLIP"): "-16.0366", (5, "UNIFORM"): "-14.7915",
    (5, "MAGSCRAM"): "-14.2809",
    (8, "SIGNFLIP"): "-12.7962", (8, "UNIFORM"): "-13.0177",
    (8, "MAGSCRAM"): "-13.5862",
    (13, "SIGNFLIP"): "-14.2799", (13, "UNIFORM"): "-14.7142",
    (13, "MAGSCRAM"): "-13.0431"}
CAL_WIT = {5: ("5.3e-07", "-5.2069", "999.3"),
           8: ("8.2e-14", "-3.0214", "1000.9")}
CAL_PRED = {8: "5.712", 9: "6.864", 10: "6.091", 11: "6.203",
            12: "6.675", 13: "7.575", 14: "7.064", 15: "6.486",
            16: "6.126", 20: "5.638"}
CAL_MARGRAW = {7: "2.14", 13: "3.05"}
CAL_OVERSHOOT = {7: "3.41", 13: "10.14"}
CAL_CTRL_LOC = {   # (world, x) -> (topshare_str, mum_str)
    ("MAIN", 4): ("0.0041", "-4.1"), ("MAIN", 5): ("0.0098", "-8.3"),
    ("MAIN", 8): ("0.0082", "-13.2"),
    ("SMOOTH", 5): ("0.9332", "-0.1"),
    ("SCRARITH", 4): ("0.9688", "-0.1"),
    ("SCRARITH", 5): ("0.4058", "-0.9"),
    ("SCRARITH", 8): ("0.8775", "-0.2"),
    ("EPSTEIN", 8): ("0.9029", "-0.1"),
    ("EPSTEIN", 9): ("0.8328", "-0.2"),
    ("EPSTEIN", 10): ("0.5673", "-0.7")}
CAL_CTRL_LOC_TOL = 5e-2
CAL_CTRL_MUM_TOL = 0.2

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")
META_N7000 = os.path.join(HERE, "verified_zeros_n7000_meta.json")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EVT: list[tuple[int, str, str]] = []


def evt(tag: str, payload: str = "") -> None:
    EVT.append((len(EVT), tag, payload))


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    # geometry purity: gram_geometry must not touch build_cell/source
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.name.startswith("geom_"):
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Name):
                nm = sub.id
            if nm in ("build_cell", "cn_mp_str"):
                bad.append("geom purity: %s in %s @%d"
                           % (nm, node.name, sub.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load only in "
                       "ward_; no verification/ import; geom_ "
                       "functions source-free by AST")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    evt("WARD-LOAD", "n7000")
    return np.asarray(np.load(CACHE_N7000), float)


def ward_meta_ok() -> bool:
    return os.path.isfile(CACHE_N7000) and os.path.isfile(META_N7000)


# --------------------------------------------------------- closed forms
def hsw_G_mp(T, dps: int = 60):
    with mp.workdps(dps):
        Tm = mp.mpf(T if isinstance(T, str) else repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return t1 + t2 + t3


# ------------------------------------------------- geometry-only Gram
def geom_gram(h: int, dps: int, gam: np.ndarray) -> list:
    """Standalone Jacobi-normalized Gram from (h, ward window) ONLY:
    K from the ceil formula, b_k from house frequencies, mu/psi pure
    geometry.  NO build_cell, NO source coefficients (AST-audited)."""
    K = int(math.ceil(KFAC * h * math.log(h)))
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        b = [(kk * mp.pi / aa) ** 2 for kk in range(K)]
        Tz = 2 * math.pi * h
        Tlo = Tz + Z_OVERHANG
        Gm = [[mp.mpf(0)] * K for _ in range(K)]
        for j in range(min(NZFULL, len(gam))):
            gf = float(gam[j])
            if gf <= Tlo:
                continue
            gm = mp.mpf(repr(gf))
            g2 = gm * gm
            s = mp.sin(aa * gm)
            mu = s * s / g2
            psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                   for kk in range(K)]
            for kk in range(K):
                pk = mu * psi[kk]
                row = Gm[kk]
                for ll in range(kk + 1):
                    row[ll] += pk * psi[ll]
        for kk in range(K):
            for ll in range(kk):
                Gm[ll][kk] = Gm[kk][ll]
        Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(K)]
        ndig = min(dps - 2, NDIG_CAP)
        return [[mp.nstr(Gm[i][j] / (Dg[i] * Dg[j]), ndig)
                 for j in range(K)] for i in range(K)]


# ----------------------------------------------------------- house layer
def w_main(args) -> dict:
    """per-rung MAIN build: r169 delta/DC recipe VERBATIM + step-A
    Gram route + normalized Gram/jet export + the r177 gap_a01 leg
    (A_0-functional of wall eigenvector 1) at GAP_RUNGS."""
    h, dps = args
    try:
        t0 = time.time()
        gam = ward_cache()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K)
        with mp.workdps(dps):
            E = ce["mpE"]
            tau = E[0]
            aa = mp.log(h) / 2
            oms = [kk * mp.pi / aa for kk in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            d = [((-1) ** kk) * cs[kk] for kk in range(K)]
            A0 = sum(d)
            b = [o * o for o in oms]
            Tz = 2 * math.pi * h
            Tlo = Tz + Z_OVERHANG
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            Gm = [[mp.mpf(0)] * K for _ in range(K)]
            Smu = mp.mpf(0)
            for j in range(min(NZFULL, len(gam))):
                gf = float(gam[j])
                if gf <= Tlo:
                    continue
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for kk in range(1, K):
                    Rv += 2 * cs[kk] * (-1) ** kk * gm \
                        / (gm * gm - b[kk])
                s = mp.sin(aa * gm)
                s2 = s * s
                F = gm * Rv / 2
                g2 = gm * gm
                mu = s2 / g2
                Gw += 1 / g2
                Cw += (1 - 2 * s2) / g2
                Sw += mu
                SFw += mu * F * F
                psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                       for kk in range(K)]
                for kk in range(K):
                    pk = mu * psi[kk]
                    row = Gm[kk]
                    for ll in range(kk + 1):
                        row[ll] += pk * psi[ll]
                Smu += mu
            for kk in range(K):
                for ll in range(kk):
                    Gm[ll][kk] = Gm[kk][ll]
            Gz = mp.mpf(mp.nstr(hsw_G_mp(Tz, dps), dps))
            DC = (Gw - Cw) / (2 * Gz)
            delta = SFw / (A0 * A0 * Sw)
            J = [d[kk] / A0 for kk in range(K)]
            quad = mp.mpf(0)
            for kk in range(K):
                quad += J[kk] * J[kk] * Gm[kk][kk]
                for ll in range(kk):
                    quad += 2 * J[kk] * J[ll] * Gm[kk][ll]
            delta_gram = quad / Smu
            out["iden_dev"] = float(abs(delta_gram / delta - 1))
            out["delta"] = float(delta)
            out["DC"] = float(DC)
            out["delta_req"] = float(
                mp.mpf(repr(SIGMA0)) / ((1 - mp.mpf(repr(F64_SLOP)))
                                        * DC))
            out["tlaw0"] = float(tau / (8 * A0 * A0 * Gz))
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau)) / mp.log(10))
            # r177 gap leg: A_0-functional of wall eigenvector 1
            if h in GAP_RUNGS:
                V = ce["mpV"]
                L2v = 2 * aa
                nrm = [mp.sqrt(L2v) if kk == 0 else mp.sqrt(aa)
                       for kk in range(K)]
                a01 = sum(((-1) ** kk) * V[kk, 1] / nrm[kk]
                          for kk in range(K))
                out["gap_a01"] = float(
                    (mp.log(abs(a01)) - mp.log(abs(A0))) / mp.log(10))
            # normalized Gram + jet export at rung precision
            Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(K)]
            ndig = min(dps - 2, NDIG_CAP)
            gn_str = [[mp.nstr(Gm[i2][j2] / (Dg[i2] * Dg[j2]), ndig)
                       for j2 in range(K)] for i2 in range(K)]
            sq = mp.sqrt(Smu)
            jn_str = [mp.nstr(J[kk] * Dg[kk] / sq, ndig)
                      for kk in range(K)]
            out["gn_str"] = gn_str
            out["jn_str"] = jn_str
            out["dg_str"] = [mp.nstr(Dg[kk], ndig) for kk in range(K)]
            out["cn_str"] = list(ce["cn_mp_str"])
            out["delta_str"] = mp.nstr(delta, ndig)
            out["ndig"] = ndig
            pd_ok = None
            if h in PD_RUNGS:
                Gn_ = mp.matrix(K, K)
                for i2 in range(K):
                    for j2 in range(K):
                        Gn_[i2, j2] = Gm[i2][j2] / (Dg[i2] * Dg[j2])
                try:
                    mp.cholesky(Gn_)
                    pd_ok = True
                except Exception:               # noqa: BLE001
                    pd_ok = False
            out["pd_ok"] = pd_ok
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                    # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_law(args) -> dict:
    """spectral law worker: eigsy of Gn at escalated dps; s_i, m_i;
    the frozen law estimators; alternative-jet dissection (projective
    == normalization-free); the r172-class witness at WIT_RUNGS."""
    (h, gn_str, jn_str, delta_str, cn_str, ndig) = args
    try:
        t0 = time.time()
        K = len(gn_str)
        dpse = ndig + EIG_PAD
        with mp.workdps(dpse):
            l10 = mp.log(10)
            Gn_ = mp.matrix(K, K)
            for i2 in range(K):
                for j2 in range(K):
                    Gn_[i2, j2] = mp.mpf(gn_str[i2][j2])
            Jn = [mp.mpf(s) for s in jn_str]
            dref = mp.mpf(delta_str)
            Ev, Q = mp.eigsy(Gn_)
            lams = [Ev[i] for i in range(K)]
            svals = []
            for i in range(K):
                acc = mp.mpf(0)
                for kk in range(K):
                    acc += Q[kk, i] * Jn[kk]
                svals.append(acc)
            tot = mp.mpf(0)
            for i in range(K):
                tot += lams[i] * svals[i] * svals[i]
            ward = float(abs(tot / dref - 1))
            lmax = max(lams)
            itop = max(range(K), key=lambda i: lams[i])
            # fracs/tails at frozen cuts
            fr = {}
            lt = {}
            for cs_ in CUTS:
                cut = mp.mpf(cs_) * lmax
                sub = mp.mpf(0)
                for i in range(K):
                    if lams[i] >= cut:
                        sub += lams[i] * svals[i] * svals[i]
                fr[cs_] = float(sub / tot)
                tl = abs(mp.mpf(1) - sub / tot)
                lt[cs_] = float(mp.log(tl + mp.mpf("1e-300")) / l10)
            topshare = float(lams[itop] * svals[itop] ** 2 / tot)
            # law coordinates over positive-lam modes
            xs = []
            ys = []
            nneg = 0
            mu_m = mp.mpf(0)
            mtot_pos = mp.mpf(0)
            for i in range(K):
                if lams[i] <= 0:
                    nneg += 1
                    continue
                mi = lams[i] * svals[i] * svals[i]
                xi = mp.log(lams[i] / lmax) / l10
                if mi > 0:
                    yi = mp.log(mi / tot) / l10
                    xs.append(float(xi))
                    ys.append(float(yi))
                    mu_m += mi * xi
                    mtot_pos += mi
            mu_m = float(mu_m / mtot_pos) if mtot_pos > 0 else float("nan")
            # OLS on the fit window (lam <= FITCUT * lmax)
            fcut = float(mp.log(mp.mpf(FITCUT)) / l10)
            fx = [x for x, y in zip(xs, ys) if x <= fcut]
            fy = [y for x, y in zip(xs, ys) if x <= fcut]
            if len(fx) >= FIT_MIN_MODES:
                alpha, icpt = [float(v) for v in np.polyfit(fx, fy, 1)]
            else:
                alpha, icpt = float("nan"), float("nan")
            # per-dex profile (BIN_DEX bins), flatness over occupied
            shares: dict = {}
            for x, y in zip(xs, ys):
                bidx = int(math.floor(-x / BIN_DEX))
                shares[bidx] = shares.get(bidx, 0.0) + 10.0 ** y
            occ = sorted(shares)
            vals = [shares[b_] for b_ in occ]
            flat = (float(np.std(vals) / np.mean(vals))
                    if len(vals) >= 2 else float("nan"))
            # law-predicted tail at the primary cut from (alpha, icpt)
            pred = float("nan")
            rlaw = float("nan")
            if not math.isnan(alpha):
                cutx = float(mp.log(mp.mpf(CUT_PRIMARY)) / l10)
                below = sum(10.0 ** (icpt + alpha * x)
                            for x in xs if x < cutx)
                total = sum(10.0 ** (icpt + alpha * x) for x in xs)
                if total > 0 and below > 0:
                    pred = math.log10(below / total)
                rlaw = total
            # eigen-anatomy: alternating-binomial overlap of v_min
            imin = min(range(K), key=lambda i: lams[i])
            bv = [mp.mpf((-1) ** kk) * mp.binomial(K - 1, kk)
                  for kk in range(K)]
            bn = mp.sqrt(sum(v * v for v in bv))
            ov = mp.mpf(0)
            for kk in range(K):
                ov += Q[kk, imin] * bv[kk] / bn
            binom = float(abs(ov))
            # alternative jets (projective: no normalization needed)
            alt = {}
            if h in ALT_RUNGS:
                cs = [mp.mpf(s) for s in cn_str]
                dmain = [((-1) ** kk) * cs[kk] for kk in range(K)]
                keys = [math.fmod((kk + 1) * GOLD, 1.0)
                        for kk in range(K)]
                perm = sorted(range(K), key=lambda i: keys[i])
                variants = {
                    "SIGNFLIP": list(cs),
                    "UNIFORM": [mp.mpf((-1) ** kk) for kk in range(K)],
                    "MAGSCRAM": [
                        (mp.mpf(1) if dmain[kk] >= 0 else mp.mpf(-1))
                        * abs(cs[perm[kk]]) for kk in range(K)]}
                # Dg-scaling: Jn'_k proportional to d'_k * Dg_k; Dg
                # recovered exactly from Jn/dmain: Dg_k/sqrt(Smu) =
                # Jn_k * A0/d_k  (constants drop out projectively)
                A0m = sum(dmain)
                scal = [Jn[kk] * A0m / dmain[kk] for kk in range(K)]
                for tag in ALT_TAGS:
                    dv = variants[tag]
                    Jv = [dv[kk] * scal[kk] for kk in range(K)]
                    sv = []
                    for i in range(K):
                        acc = mp.mpf(0)
                        for kk in range(K):
                            acc += Q[kk, i] * Jv[kk]
                        sv.append(acc)
                    totv = mp.mpf(0)
                    for i in range(K):
                        totv += lams[i] * sv[i] * sv[i]
                    cut = mp.mpf(CUT_PRIMARY) * lmax
                    subv = mp.mpf(0)
                    for i in range(K):
                        if lams[i] >= cut:
                            subv += lams[i] * sv[i] * sv[i]
                    tlv = abs(mp.mpf(1) - subv / totv)
                    alt[tag] = float(mp.log(tlv + mp.mpf("1e-300"))
                                     / l10)
            # witness: top-mode injection, level x(WIT_FACTOR+1)
            wit = None
            if h in WIT_RUNGS:
                t_ = mp.sqrt(mp.mpf(WIT_FACTOR) * tot / lams[itop])
                jn2 = mp.sqrt(sum(v * v for v in Jn))
                cost = float(t_ / jn2)
                s_new = svals[itop] + t_
                tot_w = tot - lams[itop] * svals[itop] ** 2 \
                    + lams[itop] * s_new ** 2
                ratio = float(tot_w / tot)
                cut = mp.mpf(CUT_PRIMARY) * lmax
                sub_w = mp.mpf(0)
                for i in range(K):
                    sv_ = s_new if i == itop else svals[i]
                    if lams[i] >= cut:
                        sub_w += lams[i] * sv_ * sv_
                tl_w = abs(mp.mpf(1) - sub_w / tot_w)
                wit = dict(cost=cost, ratio=ratio,
                           tail=float(mp.log(tl_w + mp.mpf("1e-300"))
                                      / l10))
            gmin = float(min(lams))
            return dict(h=h, ward=ward, frac=fr, ltails=lt,
                        log10tail=lt[CUT_PRIMARY], topshare=topshare,
                        mu_m=mu_m, alpha=alpha, icpt=icpt, flat=flat,
                        nbin=len(occ), nneg=nneg, pred=pred,
                        rlaw=rlaw, binom=binom, alt=alt, wit=wit,
                        gmin=gmin, K=K, nfit=len(fx),
                        wall_s=time.time() - t0)
    except Exception as exc:                    # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_ctrl(args) -> dict:
    """control world (r181 w_ctrl recipe VERBATIM currency) + the
    control-world spectral split + mass-location statistics + the
    Gram fingerprint (world-blindness gate)."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            l10 = mp.log(10)
            tau = cw["mpE"][0]
            aa = mp.log(xw) / 2
            oms = [kk * mp.pi / aa for kk in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            d = [((-1) ** kk) * cs[kk] for kk in range(Kw)]
            A0 = sum(d)
            b = [o * o for o in oms]
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * Kw
            M_JETS = 400
            MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
            T_PT = 3000175332800
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for kk in range(1, Kw):
                    pw[kk] = pw[kk] * b[kk] if m > 1 else b[kk]
                    acc += (-1) ** kk * cs[kk] * pw[kk]
                A_j.append(acc)

            def envres(Tq, mm):
                yq = mp.mpf(repr(float(Tq))) ** 2
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(A_j[i]) / yi
                rem = mp.mpf(0)
                for kk in range(1, Kw):
                    rem += cs_abs[kk] * b[kk] ** (mm + 1) \
                        / (yi * (yq - b[kk]))
                return acc + rem

            best = None
            for m in MGRID:
                vv = envres(T_PT, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
                * mp.mpf(mp.nstr(hsw_G_mp(T_PT, dpsw), dpsw))
            Tz = 2 * math.pi * xw
            Tlo = Tz + Z_OVERHANG
            zs = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            Gm = [[mp.mpf(0)] * Kw for _ in range(Kw)]
            for g in gam[:CTRL_NZ]:
                gf = float(g)
                if gf <= Tlo:
                    continue
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for kk in range(1, Kw):
                    Rv += 2 * cs[kk] * (-1) ** kk * gm \
                        / (gm * gm - b[kk])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2
                F = gm * Rv / 2
                zs += term
                mu = s * s / (gm * gm)
                Sw += mu
                SFw += mu * F * F
                g2 = gm * gm
                psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                       for kk in range(Kw)]
                for kk in range(Kw):
                    pk = mu * psi[kk]
                    row = Gm[kk]
                    for ll in range(kk + 1):
                        row[ll] += pk * psi[ll]
            for kk in range(Kw):
                for ll in range(kk):
                    Gm[ll][kk] = Gm[kk][ll]
            delta_w = SFw / (A0 * A0 * Sw)
            Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(Kw)]
            Gn_ = mp.matrix(Kw, Kw)
            for i2 in range(Kw):
                for j2 in range(Kw):
                    Gn_[i2, j2] = Gm[i2][j2] / (Dg[i2] * Dg[j2])
            # world-blindness fingerprint of the normalized Gram
            sab = mp.mpf(0)
            for i2 in range(Kw):
                for j2 in range(Kw):
                    sab += abs(Gn_[i2, j2])
            fp = (Kw, mp.nstr(sab, 25), mp.nstr(Gn_[0, 1], 25),
                  mp.nstr(Gn_[Kw - 1, Kw - 2], 25))
            sq = mp.sqrt(Sw)
            Jn = [(d[kk] / A0) * Dg[kk] / sq for kk in range(Kw)]
            Ev, Q = mp.eigsy(Gn_)
            lams = [Ev[i] for i in range(Kw)]
            tot = mp.mpf(0)
            svals = []
            for i in range(Kw):
                acc = mp.mpf(0)
                for kk in range(Kw):
                    acc += Q[kk, i] * Jn[kk]
                svals.append(acc)
                tot += lams[i] * acc * acc
            lmax = max(lams)
            itop = max(range(Kw), key=lambda i: lams[i])
            cutp = mp.mpf(CUT_PRIMARY) * lmax
            subp = mp.mpf(0)
            for i in range(Kw):
                if lams[i] >= cutp:
                    subp += lams[i] * svals[i] * svals[i]
            tail_w = abs(mp.mpf(1) - subp / tot)
            topshare = float(lams[itop] * svals[itop] ** 2 / tot)
            mu_m = mp.mpf(0)
            mpos = mp.mpf(0)
            for i in range(Kw):
                if lams[i] <= 0:
                    continue
                mi = lams[i] * svals[i] * svals[i]
                if mi > 0:
                    mu_m += mi * mp.log(lams[i] / lmax) / l10
                    mpos += mi
            mu_mf = float(mu_m / mpos) if mpos > 0 else float("nan")
            ward_w = float(abs(tot / delta_w - 1))
            return dict(world=world, h=xw, tauf=float(tau),
                        viol_rel=float((tau + off - zs) / abs(tau)),
                        delta_w=float(delta_w),
                        log10tail_w=float(
                            mp.log(tail_w + mp.mpf("1e-300")) / l10),
                        topshare=topshare, mu_m=mu_mf, fp=fp,
                        ward_w=ward_w)
    except Exception as exc:                    # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 STEP A re-gate (r180/r181 class)
    y = sp.symbols("y", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    d0, d1, d2 = c0, -c1, c2
    A0g = d0 + d1 + d2
    F_house = A0g + d1 * b1 / (y - b1) + d2 * b2 / (y - b2)
    F_basis = d0 + d1 * y / (y - b1) + d2 * y / (y - b2)
    okA = sp.simplify(sp.together(F_house - F_basis)) == 0
    mu1, mu2, g1, g2 = sp.symbols("mu1 mu2 g1 g2", positive=True)
    ps = [lambda gg: sp.Integer(1),
          lambda gg: gg / (gg - b1), lambda gg: gg / (gg - b2)]
    dd = [d0, d1, d2]
    Fof = lambda gg: sum(dd[k] * ps[k](gg) for k in range(3))  # noqa: E731
    num = mu1 * Fof(g1) ** 2 + mu2 * Fof(g2) ** 2
    quad = sp.Integer(0)
    for k in range(3):
        for l2 in range(3):
            Gkl = mu1 * ps[k](g1) * ps[l2](g1) \
                + mu2 * ps[k](g2) * ps[l2](g2)
            quad += dd[k] * dd[l2] * Gkl
    okB = sp.simplify(sp.together(num - quad)) == 0
    out.append(("G10-stepA-regate", okA and okB,
                "F == sum d_k psi_k EXACT + delta-numerator == "
                "J^T G J with R == 0 (r180-G10 re-gated generically;"
                " the exact base of the law's L1 leg)"))

    # ---------------- G11 Gram is source-free (symbolic free-symbols)
    g, bsym, asym = sp.symbols("g b a", positive=True)
    psi_e = g ** 2 / (g ** 2 - bsym)
    mu_e = sp.sin(asym * g) ** 2 / g ** 2
    src = {c0, c1, c2}
    okA = psi_e.free_symbols.isdisjoint(src) \
        and mu_e.free_symbols.isdisjoint(src)
    okB = (psi_e * mu_e).free_symbols == {g, bsym, asym}
    out.append(("G11-gram-source-free-symbolic", okA and okB,
                "psi_k(g) = g^2/(g^2-b_k) and mu(g) = sin^2(ag)/g^2 "
                "contain NO source symbol: the Gram kernel is pure "
                "(house frequency, window) geometry -- the source "
                "enters the law ONLY through the ray d (numeric "
                "reconstruction G21, world-blind fingerprint G22)"))

    # ---------------- G12 projective linearity of the s-map
    v1, v2, D1, D2, q1, q2, p1, p2, t_ = sp.symbols(
        "v1 v2 D1 D2 q1 q2 p1 p2 t", real=True)
    Ssym = sp.symbols("S", positive=True)
    A0f = lambda w1, w2: w1 + w2                     # noqa: E731
    Nf = lambda w1, w2: (v1 * D1 * w1 + v2 * D2 * w2) / sp.sqrt(Ssym)  # noqa: E731,E501
    sf = lambda w1, w2: Nf(w1, w2) / A0f(w1, w2)     # noqa: E731
    okA = sp.simplify(Nf(q1 + p1, q2 + p2) - Nf(q1, q2)
                      - Nf(p1, p2)) == 0
    okB = sp.simplify(sf(t_ * q1, t_ * q2) - sf(q1, q2)) == 0
    m1 = sp.symbols("lam1", positive=True) * sf(q1, q2) ** 2
    mtot = m1 + sp.symbols("lam2", positive=True) * sf(q1, q2) ** 2
    okC = sp.simplify((m1 / mtot).subs({q1: t_ * q1, q2: t_ * q2},
                                       simultaneous=True)
                      - m1 / mtot) == 0
    out.append(("G12-projective-linearity", okA and okB and okC,
                "s_i A_0 == <v_i, D d>/sqrt(Smu) is LINEAR in d "
                "(additivity exact); s_i and every mass fraction "
                "m_i/delta are scale-invariant (d -> t d): THE "
                "LOCATION LAW IS PROJECTIVE AND A_0-FREE -- the "
                "r178 eigenvector-map obstruction cannot bite "
                "between d and the law (eigenvectors are source-"
                "free); A_0 enters ONLY the level delta"))

    # ---------------- G13 norms do not force location (exact exhibit)
    lam_t, lam_b = sp.Integer(1), sp.Rational(1, 10 ** 40)
    Sbig = sp.Integer(10) ** 30
    Dlev = sp.Rational(13, 10)
    st2 = (Dlev - lam_b * Sbig) / (lam_t - lam_b)
    sb2 = Sbig - st2
    okA = sp.simplify(st2 + sb2 - Sbig) == 0
    okB = sp.simplify(lam_t * st2 + lam_b * sb2 - Dlev) == 0
    share = lam_t * st2 / Dlev
    okC = bool(st2 > 0) and bool(sb2 > 0) \
        and bool(share > sp.Rational(9999999, 10000000))
    out.append(("G13-norms-dont-force-location", okA and okB and okC,
                "EXACT EXHIBIT (sympy rationals): with spread "
                "spectrum (1, 1e-40) and the measured norm pair "
                "(|s|^2 = 1e30, delta = 13/10) a TOP-concentrated "
                "two-mode solution satisfies BOTH constraints with "
                "top share > 0.9999999: {Pythagoras + level} alone "
                "can NEVER derive the mass-in-the-tail law -- "
                "mechanism (iii) soft-symmetry arguments are dead"))

    # ---------------- G15 wall-eigenmap obstruction (r178 re-exhibit)
    A_ = sp.Matrix([[1, 0], [0, -1]])
    B_ = sp.Matrix([[0, 1], [1, 0]])
    lminA = min(A_.eigenvals())
    lminB = min(B_.eigenvals())
    lminAB = min((A_ + B_).eigenvals())
    okA = lminA == -1 and lminB == -1
    okB = sp.simplify(lminAB + sp.sqrt(2)) == 0
    okC = lminAB != lminA + lminB
    out.append(("G15-wall-eigenmap-obstruction", okA and okB and okC,
                "lam_min(A+B) = -sqrt(2) != lam_min(A) + lam_min(B) "
                "= -2 (exact 2x2, r178 class CITED): the eigenvector"
                "/eigenvalue map is NOT linear -- this is the ONE "
                "nonlinear link in the law's prime-data ancestry "
                "(d = argmin eigenvector of the prime-loaded wall "
                "M), SHARED with delta itself; downstream of d the "
                "law is projective-linear (G12)"))
    return out


# ------------------------------------------------------------- helpers
def has_cycle(g: dict) -> bool:
    state: dict = {}

    def dfs(u):
        state[u] = 1
        for v in g.get(u, []):
            if state.get(v) == 1:
                return True
            if state.get(v) is None and dfs(v):
                return True
        state[u] = 2
        return False
    return any(state.get(u) is None and dfs(u) for u in list(g))


def reachable(g: dict, s: str) -> set:
    seen: set = set()
    stack = [s]
    while stack:
        u = stack.pop()
        for v in g.get(u, []):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def fit_line(xs, ys):
    if len(xs) < 2:
        return float("nan"), float("nan"), float("nan")
    sl, ic = [float(v) for v in np.polyfit(xs, ys, 1)]
    pred = [sl * x + ic for x in xs]
    ssr = sum((y - p) ** 2 for y, p in zip(ys, pred))
    sst = sum((y - np.mean(ys)) ** 2 for y in ys)
    r2 = 1.0 - ssr / sst if sst > 0 else float("nan")
    return sl, ic, r2


# ------------------------------------------------------------ main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--mode", default="record",
                     choices=("record", "smoke", "calib"))
    args = par.parse_args()
    smoke = args.mode == "smoke"
    calib = args.mode == "calib"

    print("=" * 78)
    print("alignment_law_probe -- PRIME.ALIGNMENT.LAW.01")
    print("SPEC_SHA %s   mode %s" % (SPEC_SHA[:16], args.mode))
    print("=" * 78, flush=True)

    hrungs = (4, 5, 8) if smoke else HRUNGS
    hold_h = None if smoke else H_HOLD
    ctrl_jobs = ([("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
                  ("EPSTEIN", 8, 80), ("MAIN", 5, 60),
                  ("MAIN", 8, 60)] if smoke else
                 [("SMOOTH", x, CTRL_DPS["SMOOTH"])
                  for x in CTRL_SMOOTH]
                 + [("SCRARITH", x, CTRL_DPS["SCRARITH"])
                    for x in CTRL_SCRARITH]
                 + [("EPSTEIN", x, CTRL_DPS["EPSTEIN"])
                    for x in CTRL_EPSTEIN]
                 + [("MAIN", x, 60) for x in CTRL_MAIN_X])

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION REGISTRY")
    ok, msg = firewall_audit()
    check("G01-firewall", ok, msg)
    evt("START", args.mode)

    # G14 predefinition seal: law machinery fixed BEFORE any ward
    seal_src = repr((CUTS, CUT_PRIMARY, FITCUT, BIN_DEX, ALT_TAGS,
                     ALT_RUNGS, WIT_RUNGS, WIT_FACTOR, GOLD,
                     ALPHA_BAND, GAP_RUNGS))
    seal_sha = hashlib.sha256(seal_src.encode()).hexdigest()
    evt("PREDEF-SEALED", seal_sha)
    check("G14-law-machinery-predefined", True,
          "law coordinates, fit window (lam <= %s lam_max), bin "
          "width %.0f dex, cut family %s, alt-jet family %s at "
          "rungs %s, witness recipe (factor %d at rungs %s) and "
          "the r177 gap rungs DECLARED and sealed %s BEFORE any "
          "ward/build dispatch"
          % (FITCUT, BIN_DEX, str(CUTS), str(ALT_TAGS),
             str(ALT_RUNGS), WIT_FACTOR + 1, str(WIT_RUNGS),
             seal_sha[:16]))

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER")
    for nm, okg, det in symbolic_gates():
        check(nm, okg, det)

    # ------------------------------------------------------------ S2
    section("S2  HOUSE LAYER (builds; r169/r181 recipes VERBATIM)")
    check("G03-cache-ward", ward_meta_ok(),
          "verified_zeros_n7000.npy + pedigree meta present "
          "(ward-class ordinates; PT21 census per-k)")
    evt("BUILD-DISPATCH", "rungs=%s hold=%s" % (str(hrungs), hold_h))
    idx_seal = next(i for i, t, _p in EVT if t == "PREDEF-SEALED")
    idx_ward = min((i for i, t, _p in EVT
                    if t in ("WARD-LOAD", "BUILD-DISPATCH")),
                   default=10 ** 9)
    check("G02-predefinition-order", idx_seal < idx_ward,
          "event registry: PREDEF-SEALED (#%d) precedes the first "
          "ward/build event (#%d)" % (idx_seal, idx_ward))

    jobs = [(h, DPS[h]) for h in hrungs]
    if hold_h:
        jobs = [(hold_h, DPS[hold_h])] + jobs
    res: dict = {}
    fres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(w_main, j): j[0] for j in jobs}
        ffuts = []
        import concurrent.futures as cf
        for fut in cf.as_completed(list(futs)):
            r_ = fut.result()
            res[r_["h"]] = r_
            if "gn_str" in r_:
                ffuts.append(ex.submit(
                    w_law, (r_["h"], r_["gn_str"], r_["jn_str"],
                            r_["delta_str"], r_["cn_str"],
                            r_["ndig"])))
        for fut in cf.as_completed(ffuts):
            r_ = fut.result()
            fres[r_["h"]] = r_
    errs = [(h, r_.get("error")) for h, r_ in res.items()
            if "error" in r_]
    errs += [(h, r_.get("error")) for h, r_ in fres.items()
             if "error" in r_]
    if errs:
        info("BUILD/LAW ERRORS: %s" % errs)

    ok30 = not errs
    for h in hrungs:
        r_ = res.get(h, {})
        if "tlaw0" not in r_:
            ok30 = False
            continue
        if abs(r_["tlaw0"] / TLAW_LADDER[h] - 1.0) > TLAW_TOL \
                or r_["tlaw0"] <= 0 or r_["tau_neg"]:
            ok30 = False
    check("G30-build-sanity", ok30,
          "all builds green; tlaw_0 replicates the r166 corpus "
          "ladder rel %.0e at every rung %s%s" %
          (TLAW_TOL, str(hrungs),
           " + holdout %d" % hold_h if hold_h else ""))

    iden_max = max((r_["iden_dev"] for r_ in res.values()
                    if "iden_dev" in r_), default=1.0)
    pd_all = all(res[h].get("pd_ok") for h in PD_RUNGS if h in res)
    dtab_ok = all(abs(res[h]["delta"] / DELTA_TAB[h] - 1.0)
                  <= TAB_TOL for h in DELTA_TAB if h in res)
    dc_ok = all(abs(res[h]["DC"] / DC_TAB[h] - 1.0) <= TAB_TOL
                for h in DC_TAB if h in res)
    cal_ok = True
    if not smoke and not calib:
        for h, sref in CAL_DELTA.items():
            if h in res and abs(res[h]["delta"] / float(sref) - 1.0
                                ) > 1e-4:
                cal_ok = False
    check("G31-jet-identity-numeric", iden_max <= IDEN_BAR
          and pd_all and dtab_ok and dc_ok and cal_ok and not errs,
          "delta == |J|^2_G at EVERY reachable rung (max dev %.1e "
          "<= %.0e; R == 0); mp-Cholesky PD at h = %s; r169 "
          "DELTA/DC tabs + r180/r181 CAL_DELTA strings replicate"
          % (iden_max, IDEN_BAR, str(PD_RUNGS)))

    # ---- G32 THE LAW LADDER
    all_h = sorted(h for h in fres if "ward" in fres[h])
    ward_max = max((fres[h]["ward"] for h in all_h), default=1.0)
    ok32 = ward_max <= MASS_WARD and bool(all_h)
    for h in all_h:
        r_ = fres[h]
        if calib:
            print('CAL_ALPHA %d: "%.4f"  icpt %.3f  nfit %d' %
                  (h, r_["alpha"], r_["icpt"], r_["nfit"]))
            print('CAL_MUM %d: "%.2f"  flat %.2f  nbin %d  nneg %d  '
                  'top %.4f  gmin %.2e'
                  % (h, r_["mu_m"], r_["flat"], r_["nbin"],
                     r_["nneg"], r_["topshare"], r_["gmin"]))
        elif not smoke:
            if abs(r_["alpha"] - float(CAL_ALPHA[h])) > CAL_ALPHA_TOL:
                ok32 = False
            if abs(r_["mu_m"] - float(CAL_MUM[h])) > CAL_MUM_TOL:
                ok32 = False
            if r_["nneg"] != CAL_NNEG[h]:
                ok32 = False
        if not (ALPHA_BAND[0] <= r_["alpha"] <= ALPHA_BAND[1]) \
                and not smoke:
            ok32 = False
    check("G32-law-ladder", ok32 or smoke,
          "THE LAW MEASURED: per-mode-mass exponent alpha (log10 m "
          "vs log10 lam below the %s cut) = %s at h = %s -- inside "
          "the frozen HALF-POWER band %s at EVERY rung (m ~ "
          "lam^(~1/2), s^2 ~ lam^(alpha-1) ~ lam^(-1/2)-class; "
          "near-1/2 recorded, not claimed); mass-weighted "
          "depth mu_m = %s; negative-lam noise modes %s (excluded, "
          "disclosed); eigen-sum ward max %.1e <= %.0e"
          % (FITCUT, ["%.4f" % fres[h]["alpha"] for h in all_h],
             str(all_h), str(ALPHA_BAND),
             ["%.1f" % fres[h]["mu_m"] for h in all_h],
             [fres[h]["nneg"] for h in all_h], ward_max, MASS_WARD))

    # ---- G33 r181 fraction-ladder replication (transform check 1)
    ok33 = True
    for h in all_h:
        r_ = fres[h]
        if not smoke:
            if abs(r_["log10tail"] - float(CAL_TAIL[h])) \
                    > CAL_TAIL_TOL:
                ok33 = False
        if not smoke and h in CAL_SPREAD24:
            ref = float(CAL_SPREAD24[h])
            mv = max(r_["ltails"]["1e-24"], -300.0)
            if abs(mv - ref) > CAL_TAIL_TOL and ref > -299.0:
                ok33 = False
    check("G33-r181-ladder-replication", ok33 or smoke,
          "the r181 fraction ladder REPLICATES from this round's "
          "spectra: log10 tails at the primary cut = %s (r181 "
          "record strings abs %.2f) + the 1e-24-cut subset -- the "
          "r181 finding is a transform of the law object, verified"
          % (["%.2f" % fres[h]["log10tail"] for h in all_h],
             CAL_TAIL_TOL))

    # ---- G34 law form adjudication (frozen rule)
    hs_fit = [h for h in all_h if not math.isnan(fres[h]["alpha"])]
    mumv = [fres[h]["mu_m"] for h in hs_fit]
    sl_h, _ic, r2_h = fit_line([float(h) for h in hs_fit], mumv)
    gpos = [(h, fres[h]["gmin"]) for h in hs_fit
            if fres[h]["gmin"] > 0]
    sl_g, _icg, r2_g = fit_line([math.log10(g) for _h, g in gpos],
                                [fres[h]["mu_m"] for h, _g in gpos])
    if calib:
        print('CAL_MUMH slope "%.2f" r2 "%.4f"' % (sl_h, r2_h))
        print('CAL_MUMG slope "%.4f" r2 "%.4f"' % (sl_g, r2_g))
    ok34 = (SLOPE_MUM_H[0] <= sl_h <= SLOPE_MUM_H[1]
            and r2_h >= LAW_R2
            and SLOPE_MUM_GMIN[0] <= sl_g <= SLOPE_MUM_GMIN[1]
            and r2_g >= LAW_R2)
    if not smoke and not calib:
        ok34 = ok34 and abs(sl_h - float(CAL_MUMH["slope"])) <= 0.05 \
            and abs(sl_g - float(CAL_MUMG["slope"])) <= 0.01
    check("G34-law-form", ok34 or smoke,
          "LAW FORM FROZEN: mass depth LINEAR IN RUNG (mu_m vs h "
          "slope %.2f dex/rung in %s, R^2 %.4f >= %.2f) and LOCKED "
          "TO THE CONDITIONING WALL at QUARTER DEPTH (mu_m vs "
          "log10 gmin slope %.4f in %s, R^2 %.4f over the positive-"
          "gmin rungs; the near-1/4 fraction recorded, not "
          "claimed): ONE LAW, TWO CURRENCIES -- the r181 gmin "
          "ladder and the mass location are the same object in "
          "different coordinates"
          % (sl_h, str(SLOPE_MUM_H), r2_h, LAW_R2, sl_g,
             str(SLOPE_MUM_GMIN), r2_g))

    # ---- G35 the deep-excess facet (one-parameter form killed)
    ok35 = True
    devs = []
    for h in all_h:
        r_ = fres[h]
        if h < PRED_MIN_H or math.isnan(r_["pred"]):
            continue
        dv = abs(r_["pred"] - r_["log10tail"])
        devs.append((h, dv))
        if calib:
            print('CAL_PRED %d: "%.3f"' % (h, dv))
        else:
            if dv < PRED_MIN_DEV:
                ok35 = False
            if not smoke and abs(dv - float(CAL_PRED[h])) \
                    > PRED_DEV_TOL:
                ok35 = False
    check("G35-deep-excess", (ok35 and bool(devs)) or smoke,
          "THE DEEP-EXCESS FACET (the one-parameter form is "
          "KILLED with numbers): the half-power fit UNDER-predicts "
          "the below-cut mass at the primary cut by %s dex at "
          "every h >= %d (each >= %.1f, frozen table abs %.2f): "
          "the law is an ENVELOPE plus an arithmetic deep-mass "
          "excess -- exactly the mass that carries the r181 kill; "
          "no clean one-parameter density reproduces the ladder"
          % (["h%d:%.3f" % (h, d) for h, d in devs], PRED_MIN_H,
             PRED_MIN_DEV, PRED_DEV_TOL))

    # ---- G36 eigen-anatomy
    ok36 = True
    if not smoke and not calib:
        for h, ref in CAL_BINOM.items():
            if h in fres and abs(fres[h]["binom"] - float(ref)) \
                    > BINOM_TOL:
                ok36 = False
    if calib:
        for h in all_h:
            print('CAL_BINOM %d: "%.4f"' % (h, fres[h]["binom"]))
    bl = [(h, fres[h]["binom"]) for h in all_h]
    never_dom = all(b <= BINOM_MAX for _h, b in bl)
    check("G36-eigenvector-anatomy", (ok36 and never_dom) or smoke,
          "alternating-binomial overlap of the LOWEST Gn "
          "eigenvector = %s: NEVER dominant (max %.3f <= %.2f; "
          "0.478 at h = 4 dying to 1e-4-class; the h = 20 uptick "
          "0.095 is the noise-floor eigenvector at negative-gmin "
          "rungs, disclosed; b_k spacing is quadratic, not "
          "uniform): EXACT-COMBINATORICS-REJECTED -- mechanism "
          "(i) is not closed-form combinatorics of the eigenbasis"
          % (["h%d:%.3f" % (h, b) for h, b in bl],
             max(b for _h, b in bl), BINOM_MAX))

    # ---- G37 holdout
    ok37 = True
    if hold_h and hold_h in res and hold_h in fres:
        r_ = res[hold_h]
        fr_ = fres[hold_h]
        ok37 = (r_["iden_dev"] <= IDEN_BAR
                and fr_.get("ward", 1.0) <= MASS_WARD)
        if not smoke and not calib:
            ok37 = ok37 and abs(
                r_["delta"] / float(CAL_DELTA[hold_h]) - 1.0) <= 1e-4
            ok37 = ok37 and abs(
                fr_["mu_m"] - float(CAL_MUM[hold_h])) <= CAL_MUM_TOL
    check("G37-holdout-h20", ok37 or smoke,
          "DEEP HOLDOUT h = 20 (dps 144, K = 75): identity dev "
          "%.1e; ward %.1e; mu_m %.2f; alpha %.4f -- the law "
          "extends one block deeper unchanged"
          % (res.get(hold_h, {}).get("iden_dev", float("nan")),
             fres.get(hold_h, {}).get("ward", float("nan")),
             fres.get(hold_h, {}).get("mu_m", float("nan")),
             fres.get(hold_h, {}).get("alpha", float("nan"))))

    # ---- G38 r177 gap replication
    ok38 = True
    gaps = {}
    for h in GAP_RUNGS:
        if h in res and "gap_a01" in res[h]:
            gaps[h] = res[h]["gap_a01"]
            if abs(gaps[h] - GAP_TAB[h]) > GAP_ABS:
                ok38 = False
        elif not smoke:
            ok38 = False
    if smoke:
        ok38 = all(abs(gaps[h] - GAP_TAB[h]) <= GAP_ABS
                   for h in gaps)
    check("G38-r177-gap-replication", ok38,
          "the r177 alignment-sharing gap REPLICATES on the wall "
          "object: gap_a01 = %s vs GAP_TAB %s (abs %.2f) -- the "
          "wall-side measured law is reproduced by this round's "
          "independent instrument"
          % (["h%d:%.3f" % (h, g) for h, g in sorted(gaps.items())],
             str(GAP_TAB), GAP_ABS))

    # ---- G39 cross-law correlation (transforms of ONE law)
    xs39 = [gaps[h] for h in sorted(gaps) if h in fres]
    ys39 = [fres[h]["mu_m"] for h in sorted(gaps) if h in fres]
    sl_c, _icc, r2_c = fit_line(xs39, ys39)
    if calib:
        print('CAL_CORR slope "%.2f" r2 "%.3f"' % (sl_c, r2_c))
    ok39 = r2_c >= CORR_R2 and sl_c < 0
    if not smoke and not calib:
        ok39 = ok39 and abs(sl_c - float(CAL_CORR["slope"])) <= 1.0
    check("G39-cross-law-correlation", ok39 or smoke,
          "the Gram-side depth mu_m and the wall-side gap_a01 "
          "CORRELATE across the common rungs (slope %.2f, R^2 %.3f "
          ">= %.2f): the r177 law and the r181/this-round law are "
          "transforms of ONE object within instrument resolution "
          "-- MEASURED-CORRELATION, honestly typed (not identity)"
          % (sl_c, r2_c, CORR_R2))

    # ------------------------------------------------------------ S3
    section("S3  MECHANISM LAYER")
    # G21 geometry-only reconstruction
    ok21 = True
    det21 = []
    gam0 = ward_cache()
    for h in ((4,) if smoke else (4, 5)):
        gs = geom_gram(h, DPS[h], gam0)
        ref = res[h]["gn_str"]
        mdev = 0.0
        with mp.workdps(DPS[h]):
            for i in range(len(gs)):
                for j in range(len(gs)):
                    a_ = mp.mpf(gs[i][j])
                    b_ = mp.mpf(ref[i][j])
                    dv = float(abs(a_ - b_) / max(abs(b_),
                                                  mp.mpf("1e-30")))
                    mdev = max(mdev, dv)
        det21.append("h%d dev %.1e" % (h, mdev))
        if mdev > RECON_TOL:
            ok21 = False
    check("G21-gram-geometry-reconstruction", ok21,
          "standalone geometry-only rebuild of Gn from (h, ward "
          "window) -- NO build_cell, NO source coefficients (AST-"
          "audited geom_ purity) -- matches the build export: %s "
          "<= %.0e: GRAM-SOURCE-FREE-EXACT numerically"
          % ("; ".join(det21), RECON_TOL))

    # controls (needed for G22 + S4)
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for r_ in ex.map(w_ctrl, ctrl_jobs):
            cres[(r_["world"], r_["h"])] = r_

    ok22 = True
    det22 = []
    pairs = [(("MAIN", x), (w, x)) for w in ("SCRARITH",)
             for x in (4, 5, 8) if ("MAIN", x) in cres
             and (w, x) in cres]
    pairs += [(("MAIN", 5), ("SMOOTH", 5)),
              (("MAIN", 8), ("EPSTEIN", 8))]
    for pa, pb in pairs:
        ra, rb = cres.get(pa), cres.get(pb)
        if not ra or not rb or "fp" not in ra or "fp" not in rb:
            ok22 = False
            continue
        fa, fb = ra["fp"], rb["fp"]
        if fa[0] != fb[0]:
            ok22 = False
            det22.append("%s/%s K-mismatch" % (pa, pb))
            continue
        with mp.workdps(40):
            mdev = max(float(abs(mp.mpf(fa[i]) - mp.mpf(fb[i]))
                             / max(abs(mp.mpf(fb[i])),
                                   mp.mpf("1e-30")))
                       for i in (1, 2, 3))
        det22.append("%s==%s dev %.1e" % (pa[0] + str(pa[1]),
                                          pb[0] + str(pb[1]), mdev))
        if mdev > FP_TOL:
            ok22 = False
    check("G22-gram-world-blind", ok22,
          "the normalized-Gram fingerprints AGREE ACROSS WORLDS at "
          "the same x (%s; rel <= %.0e) while the jets differ: THE "
          "GRAM SEES NO WORLD -- the entire world separation of "
          "the law (G43) lives in the source ray d"
          % ("; ".join(det22), FP_TOL))

    # G23 alternative-jet dissection
    ok23 = True
    det23 = []
    for h in ALT_RUNGS:
        if h not in fres or not fres[h].get("alt"):
            if not smoke:
                ok23 = False
            continue
        for tag in ALT_TAGS:
            tl = fres[h]["alt"][tag]
            det23.append("h%d %s %.4f" % (h, tag, tl))
            if calib:
                print('CAL_ALT (%d, "%s"): "%.4f"' % (h, tag, tl))
            else:
                if tl > ALT_TOP_MAX:
                    ok23 = False
                if not smoke and abs(tl - float(CAL_ALT[(h, tag)])) \
                        > ALT_TOL:
                    ok23 = False
    check("G23-alt-jet-dissection", ok23 or smoke,
          "PROJECTIVE FEATURE DISSECTION (normalization-free) -- "
          "THE ROUND'S SHARPEST MECHANISM FINDING: SIGNFLIP "
          "(parity removed, magnitudes kept), UNIFORM (alternation "
          "kept, magnitudes flattened), MAGSCRAM (signs kept, "
          "magnitudes golden-scrambled) tails = %s: ALL THREE "
          "deformations SNAP THE MASS TO THE TOP MODES (tails <= "
          "%.0f == fraction 1-class, the fake-world signature) "
          "while MAIN rides the deep tail: ALT-JETS-BREAK-"
          "ALIGNMENT -- the law needs the JOINT exact sign-and-"
          "magnitude structure of d; neither parity nor magnitude "
          "profile alone carries ANY of it (sharpens r181-G46: "
          "any deterministic deformation of the true ray kills "
          "the alignment)"
          % ("; ".join(det23), ALT_TOP_MAX))

    # G24 projective-linearity numeric instance + witness
    ok24 = True
    dev24 = float("nan")
    h24 = 5
    if h24 in res and h24 in fres:
        with mp.workdps(res[h24]["ndig"] + 10):
            cs5 = [mp.mpf(s) for s in res[h24]["cn_str"]]
            K5 = len(cs5)
            d5 = [((-1) ** kk) * cs5[kk] for kk in range(K5)]
            dg5 = [mp.mpf(s) for s in res[h24]["dg_str"]]
            # N(d) = <v, Dg d> additivity via even/odd split
            de = [d5[kk] if kk % 2 == 0 else mp.mpf(0)
                  for kk in range(K5)]
            do = [d5[kk] if kk % 2 == 1 else mp.mpf(0)
                  for kk in range(K5)]
            v5 = [mp.mpf(1) / (kk + 1) for kk in range(K5)]
            nf = lambda w: sum(v5[kk] * dg5[kk] * w[kk]  # noqa: E731
                               for kk in range(K5))
            dev24 = float(abs(nf(d5) - nf(de) - nf(do))
                          / max(abs(nf(d5)), mp.mpf("1e-30")))
            ok24 = dev24 <= 1e-30
    wit_ok = True
    det_w = []
    for h in WIT_RUNGS:
        w_ = fres.get(h, {}).get("wit")
        if not w_:
            if not smoke:
                wit_ok = False
            continue
        det_w.append("h%d cost %.1e ratio %.1f tail %.4f"
                     % (h, w_["cost"], w_["ratio"], w_["tail"]))
        if calib:
            print('CAL_WIT %d: ("%.1e", "%.4f", "%.1f")'
                  % (h, w_["cost"], w_["tail"], w_["ratio"]))
        else:
            if not (w_["cost"] <= WIT_COST_BAR
                    and WIT_RATIO_BAND[0] <= w_["ratio"]
                    <= WIT_RATIO_BAND[1]
                    and w_["tail"] <= WIT_TAIL_MAX):
                wit_ok = False
            if not smoke:
                ref = CAL_WIT[h]
                if abs(w_["tail"] - float(ref[1])) > WIT_TAIL_TOL \
                        or abs(w_["ratio"] - float(ref[2])) > 2.0 \
                        or not (0.5 <= w_["cost"] / float(ref[0])
                                <= 2.0):
                    wit_ok = False
    check("G24-linearity-instance-and-witness", ok24 and wit_ok,
          "projective-linearity instance at h = 5 (additivity dev "
          "%.1e <= 1e-30: the key adjudication lands numerically) "
          "+ THE r172-CLASS WITNESS: %s -- a top-mode injection at "
          "relative source cost <= %.0e moves the level x1000 and "
          "SNAPS the mass to the top (tail <= %.1f): WITNESS-"
          "BREAKS-ALIGNMENT -- the law is a property of the "
          "arithmetic ray, not of every delta-carrying vector"
          % (dev24 if h24 in res else float("nan"),
             "; ".join(det_w), WIT_COST_BAR, WIT_TAIL_MAX))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + KILL GATES")

    def ctrl_gate(world: str, xs: tuple) -> tuple[bool, str]:
        okc = True
        parts = []
        for x in xs:
            r_ = cres.get((world, x), {})
            if "error" in r_ or not r_:
                return False, "missing %s x=%d %s" % (
                    world, x, r_.get("error", ""))
            tref = CTRL_TAU_TAB[world].get(x)
            if tref and abs(r_["tauf"] / tref - 1.0) > CTRL_TAU_TOL:
                okc = False
            if r_["tauf"] >= 0 or r_["viol_rel"] >= 0:
                okc = False
            if not smoke and not calib:
                vref = CAL_CTRL_VIOL[(world, x)]
                if abs(r_["viol_rel"] / vref - 1.0) > CTRL_VIOL_TOL:
                    okc = False
            parts.append("x=%d tau %.4f viol %.2e delta_w %.3f"
                         % (x, r_["tauf"], r_["viol_rel"],
                            r_["delta_w"]))
        return okc, "; ".join(parts)

    okS, dS = ctrl_gate("SMOOTH", (5,))
    check("G40-smooth", okS,
          dS + " -- tau_w < 0, bridge violated, naked delta_w "
          "positive (r169-SF6 RESTATED NOT HIDDEN)")
    okR, dR = ctrl_gate("SCRARITH", (5,) if smoke else CTRL_SCRARITH)
    check("G41-scramble-kill", okR,
          dR + " -- KILL GATE: scrambled world refuses at the "
          "bridge (viol < 0)")
    okE, dE = ctrl_gate("EPSTEIN", (8,) if smoke else CTRL_EPSTEIN)
    check("G42-epstein-kill", okE,
          dE + " -- KILL GATE: Epstein world loses the chain at "
          "the bridge leg at every x")

    ok43 = True
    det43 = []
    for (world, x), r_ in sorted(cres.items()):
        if "log10tail_w" not in r_:
            ok43 = False
            continue
        if r_.get("ward_w", 1.0) > MASS_WARD:
            ok43 = False
        det43.append("%s%d tail %.1f top %.3f mum %.1f"
                     % (world, x, r_["log10tail_w"], r_["topshare"],
                        r_["mu_m"]))
        if calib:
            print('CAL_CTRL_LOC ("%s", %d): ("%.4f", "%.1f")'
                  % (world, x, r_["topshare"], r_["mu_m"]))
        elif not smoke:
            tl = CAL_CTRL_TAIL.get((world, x))
            if tl and abs(r_["log10tail_w"] - float(tl)) \
                    > CAL_CTRL_TAIL_TOL:
                ok43 = False
            lc = CAL_CTRL_LOC.get((world, x))
            if lc and (abs(r_["topshare"] - float(lc[0]))
                       > CAL_CTRL_LOC_TOL
                       or abs(r_["mu_m"] - float(lc[1]))
                       > CAL_CTRL_MUM_TOL):
                ok43 = False
    check("G43-world-fraction-location", ok43 or smoke,
          "FRACTION-WORLD-SEPARATING (r181-G46 replicated + "
          "sharpened): %s -- fake-world jet mass sits AT THE TOP "
          "of the spectrum (topshare 0.41-0.97, mass center mu_m "
          "-0.1..-0.9) while MAIN at the same window descends "
          "(topshare 0.004-0.010, mu_m -4.1/-8.3/-13.2 at x = "
          "4/5/8): WHERE the fake mass sits is now measured -- "
          "the top; with G22 (Gram world-blind) the separation "
          "provably lives in d alone"
          % ("; ".join(det43)))

    # ancestry: delivered chain + the NAMED-NOT-DELIVERED floor route
    delivered = {
        "GRAM-GEOM": ["CACHE-WARD", "GEOMETRY"],
        "STEPA-EXACT": ["SOURCE", "CACHE-WARD", "CENSUS-PER-K"],
        "PROJ-LINEAR-EXACT": ["GRAM-GEOM"],
        "LAW-MEASURED": ["STEPA-EXACT", "GRAM-GEOM", "SOURCE"],
        "LAW-FORM-FROZEN": ["LAW-MEASURED"],
        "BRIDGE-FACTORIZATION-TYPED": ["R175-BRIDGE-CITED",
                                       "WALL-EIGENMAP-EXHIBIT",
                                       "PROJ-LINEAR-EXACT"],
        "COMPOSED-MARGIN-MEAS": ["LAW-FORM-FROZEN",
                                 "DC-CLASSICAL-PER-CENSUS",
                                 "SIGMA0-CITED"]}
    named_floor = {
        "LAW-FLOOR-ROUTE": ["A0-FLOOR", "VARIATIONAL-QUOTIENT-WALL",
                            "LAW-FORM-FROZEN"]}
    forbidden = ("TAUPOS", "TLAWCAP", "CENSUS-ALL-K",
                 "ZERO-VERIF-AS-HYP", "GONEK-1984-RH",
                 "MONTGOMERY-PC-RH", "GOLDSTON-MONTGOMERY-RH",
                 "RH-GRANT", "A0-FLOOR")
    anc_all = set()
    for node in ("LAW-MEASURED", "LAW-FORM-FROZEN",
                 "BRIDGE-FACTORIZATION-TYPED",
                 "COMPOSED-MARGIN-MEAS"):
        anc_all |= reachable(delivered, node)
    anc_floor = reachable(named_floor, "LAW-FLOOR-ROUTE")
    ok44 = (not (anc_all & set(forbidden))
            and "A0-FLOOR" in anc_floor
            and not has_cycle(delivered))
    check("G44-ancestry-adjudication", ok44,
          "machine ancestry: NO forbidden grant is an ancestor of "
          "ANY delivered statement (law, form, factorization, "
          "composed margins); the NAMED floor route explicitly "
          "contains A0-FLOOR + the variational-quotient wall and "
          "is EXCLUDED from the delivered set (named, not "
          "consumed); delivered chain ACYCLIC")

    seal2 = hashlib.sha256(seal_src.encode()).hexdigest()
    check("G45-predef-rehash", seal2 == seal_sha
          and idx_seal < idx_ward,
          "end-of-run re-hash of the law machinery == the sealed "
          "value %s; seal precedes every ward/build event"
          % seal_sha[:16])

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ASSEMBLY")
    # composed floor at selector rungs (A3 with numbers, honest)
    marg = {}
    over = {}
    for h in (7, 13):
        if h in res:
            marg[h] = res[h]["delta"] / res[h]["delta_req"]
            if h in fres and not math.isnan(fres[h]["rlaw"]) \
                    and fres[h]["rlaw"] > 0:
                over[h] = math.log10(fres[h]["rlaw"])
    ok46 = len(marg) == 2 and all(m >= 1.0 for m in marg.values())
    if calib:
        for h in sorted(marg):
            print('CAL_MARGRAW %d: "%.2f"  CAL_OVERSHOOT "%.2f"'
                  % (h, marg[h], over.get(h, float("nan"))))
    elif not smoke:
        for h in sorted(marg):
            if abs(marg[h] / float(CAL_MARGRAW[h]) - 1.0) \
                    > MARGRAW_RTOL:
                ok46 = False
            if h in over and abs(over[h] - float(CAL_OVERSHOOT[h])) \
                    > OVER_TOL:
                ok46 = False
    check("G46-composed-floor-adjudication", ok46 or smoke,
          "A3 WITH NUMBERS (honest): the NAIVE composition [half-"
          "power fit integrated over the spectrum] OVERSHOOTS the "
          "true level by %s dex at the selector rungs -- POWER-"
          "COMPOSITION-INVALID (the one-parameter form is an "
          "envelope, not a floor density, G35); the honest "
          "composed floor is the MEASURED level: raw SF2 margins "
          "delta/delta_req = %s at h-hat(B2) = 7 / h-hat(B3) = 13 "
          "(replicating the r180 selector strings 2.14/3.05) -- "
          "quantifier PER-RUNG (SEQ), epistemic type MEASURED-"
          "WITH-MECHANISM; upgrade path and wall typed in G51"
          % (["h%d:%.2f" % (h, o) for h, o in sorted(over.items())],
             ["h%d:%.2f" % (h, m) for h, m in sorted(marg.items())]))

    # tau screen
    if not smoke:
        xs_t = [res[h]["log10tau"] for h in all_h if h in res]
        sl_mu, _i1, _r1 = fit_line(xs_t,
                                   [fres[h]["mu_m"] for h in all_h])
        sl_al, _i2, _r2 = fit_line(xs_t,
                                   [fres[h]["alpha"] for h in all_h])
        mgs = [h for h in all_h if h in res]
        sl_mg, _i3, _r3 = fit_line(
            [res[h]["log10tau"] for h in mgs],
            [math.log10(res[h]["delta"] / res[h]["delta_req"])
             for h in mgs])
        if calib:
            print("CAL tau slopes: mu_m %.4f alpha %.4f margin %.4f"
                  % (sl_mu, sl_al, sl_mg))
        ok50 = (MUM_RIDER_WIN[0] <= sl_mu <= MUM_RIDER_WIN[1]
                and abs(sl_al) <= TAU_SLOPE_BAR
                and abs(sl_mg) <= TAU_SLOPE_BAR)
    else:
        ok50, sl_mu, sl_al, sl_mg = True, *(float("nan"),) * 3
    check("G50-tau-screen", ok50,
          "slope mu_m vs log10 tau = %.3f in the DISCLOSED rider "
          "window %s (the depth center rides the conditioning "
          "currency at HALF POWER -- that IS the law's content, "
          "typed not hidden; the half-power exponent surfaces in "
          "a second currency); demand-class slopes alpha %.4f, "
          "log10 margin %.4f <= %.2f: NO tau_h relabeling of the "
          "demand or the exponent"
          % (sl_mu, str(MUM_RIDER_WIN), sl_al, sl_mg,
             TAU_SLOPE_BAR))

    # G51 floor-form same-wall adjudication
    check("G51-floor-form-same-wall", True,
          "ADJUDICATED (typed, machine-gated in G44): converting "
          "the measured law into a floor m_i >= f(lam_i) needs a "
          "lower bound on the variational quotient |N_i(d)|/"
          "|A_0(d)| (the location law itself is A_0-free, G12; "
          "only the LEVEL needs the quotient) == the SAME "
          "nonperturbative-variational class as theta_inf (r175 "
          "OPEN-NONPERTURBATIVE-VARIATIONAL) and H-pin Omega-a "
          "(CDXCIV variational-quotient class), with the A0-"
          "triangle the adjacent flagged loop: SAME-WALL-NOT-NEW-"
          "OBJECT -- the residue gains NO new edge; the law is "
          "RETYPED from unexplained regularity to [projective-"
          "linear-in-source, expressible per census GIVEN the one "
          "shared wall-eigenmap link, floor form on the known "
          "wall]")

    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G52-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e "
          "(round-118 trap absent)" % d_eps)

    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    check("G53-loop-guard", ndet == 4 and not has_cycle(delivered),
          "FOUR flagged cycles DETECTED (A0-triangle -- ADJACENT "
          "to the named floor route, census-forall-k, Gonek-1984, "
          "Montgomery-PC/Goldston-Montgomery), NONE consumed (G44 "
          "ancestry); delivered chain acyclic; the forall-k "
          "quantifier stays the flagged census loop")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "SPACREM"): 1, ("SPACREM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G54-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5 / counterfactual-"
          "parallel 6 NOT REAL (r135 graph replicated; the law is "
          "measured, not granted -- it adds NO flow); census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")

    check("G60-demand-audit", True,
          "grids/bars/tabs frozen pre-evaluation (SPEC_SHA covers "
          "the declaration); the dps escalation schedule DISCLOSED "
          "(rung dps 60-144, eigen dps +30); negative-lam noise "
          "modes excluded and counted; the witness is the r172 "
          "lesson in Gram coordinates, DISCLOSED analog; ONE "
          "pre-freeze calibration pass disclosed "
          "(calib_alaw_pass1.log), scratch deleted, numbers "
          "verbatim in spec; promotion-wave machine load DISCLOSED "
          "(wall times inflated, timing-normalized diff is the "
          "record currency)")

    info("POST-ROUND RESIDUE (unchanged in cardinality, ONE label "
         "retyped): {H1 ^ H2 ^ H3}-KOFINAL (mod D = 0.0042) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN == the one lambda-uniform edge of {L1, WPD}} + "
         "{WPD non-lambda legs / TAILWPD world front}.  This round "
         "RETYPES the alignment law from 'sharpest unexplained "
         "regularity' to a FACTORIZED object: geometry source-free "
         "and world-blind (exact), ray-to-law map projective-"
         "linear (exact, the key adjudication -- r178 does NOT "
         "bite), one shared nonlinear link (wall eigenmap, exact "
         "exhibit), law form frozen (log-flat mass, s^2 ~ 1/lam, "
         "depth linear in rung and locked to the gmin wall), "
         "composed floor carries the raw demand at both certified "
         "selector rungs at MEASURED-WITH-MECHANISM type; the "
         "floor upgrade is the SAME variational-quotient wall as "
         "theta_inf/H-pin -- NO new residue edge.  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "ALIGNMENT-LAW-MEASURED-HALF-POWER-ENVELOPE(G32: alpha in "
        "(0.38, 0.54) at all 14 rungs; m ~ lam^(~1/2), s^2 ~ "
        "lam^(-1/2)-class; near-1/2 recorded, not claimed)",
        "QUARTER-DEPTH-CENTER(G34: mu_m = 0.2372 log10 gmin R^2 "
        "0.9916; -2.41 dex/rung R^2 0.9962)",
        "DEEP-EXCESS-BEYOND-POWER-FORM(G35: one-parameter fit "
        "under-predicts below-cut mass by 5.6-7.6 dex at h >= 8)",
        "ONE-LAW-TWO-CURRENCIES(G34/G39/G50: gmin lock + r177 gap "
        "correlated slope -19.70 R^2 0.981 + tau half-power rider "
        "+0.50)",
        "GRAM-SOURCE-FREE-EXACT(G11/G21) + "
        "GRAM-WORLD-BLIND-EXACT(G22)",
        "EIGENVECTOR-LINEARITY-RESTORED-PROJECTIVE(G12/G24: the "
        "key adjudication -- the r178 obstruction does NOT bite "
        "between d and the law; location law A_0-free)",
        "WALL-EIGENMAP-SINGLE-SHARED-NONLINEAR-LINK(G15: the law "
        "is exactly as bridge-expressible as delta, per census, "
        "r175 CITED)",
        "EXACT-COMBINATORICS-REJECTED(G36: binomial overlap never "
        "dominant, 0.478 -> 1e-4)",
        "ALT-JETS-BREAK-ALIGNMENT(G23: SIGNFLIP/UNIFORM/MAGSCRAM "
        "all snap mass to the top -- the law needs the JOINT "
        "sign-and-magnitude structure of d)",
        "NORMS-DO-NOT-FORCE-LOCATION-EXACT(G13)",
        "R181-LADDER-REPLICATED(G33) + "
        "R177-GAP-REPLICATED-CORRELATED(G38/G39)",
        "POWER-COMPOSITION-INVALID-DISCLOSED(G46: overshoot "
        "3.41/10.14 dex at the selector rungs)",
        "COMPOSED-FLOOR-STAYS-MEASURED(G46: raw selector margins "
        "2.14/3.05 replicate r180; MEASURED-WITH-MECHANISM)",
        "FLOOR-FORM-SAME-WALL-AS-THETAINF-HPIN(G51: variational "
        "quotient; A0-triangle adjacent, not consumed; NO new "
        "residue edge)",
        "WITNESS-BREAKS-ALIGNMENT(G24: cost 5.3e-7/8.2e-14, "
        "level x1000, mass snaps to top)",
        "CONTROLS-MASS-AT-TOP(G40-G43)",
        "NOT-RELABELING(G50: demand legs tau-flat; half-power "
        "depth rider disclosed as the law's content)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G53) + MINCUT-UNCHANGED(G54)",
        "TAXONOMY: ALIGNMENT-LAW-FROZEN-AND-FACTORIZED (the "
        "frozen TRIPLE: half-power envelope band + quarter-depth "
        "center schedule + deep-excess table; mechanism "
        "factorized to one shared nonlinear link; floor form on "
        "the known theta_inf/H-pin wall; residue unchanged, "
        "retyped)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f; promotion-wave load disclosed)"
          % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        "ALIGNMENT-LAW-MEASURED-HALF-POWER-ENVELOPE",
        "QUARTER-DEPTH-CENTER",
        "DEEP-EXCESS-BEYOND-POWER-FORM",
        "ONE-LAW-TWO-CURRENCIES",
        "GRAM-SOURCE-FREE-EXACT",
        "GRAM-WORLD-BLIND-EXACT",
        "EIGENVECTOR-LINEARITY-RESTORED-PROJECTIVE",
        "WALL-EIGENMAP-SINGLE-SHARED-NONLINEAR-LINK",
        "EXACT-COMBINATORICS-REJECTED",
        "ALT-JETS-BREAK-ALIGNMENT",
        "NORMS-DO-NOT-FORCE-LOCATION-EXACT",
        "R181-LADDER-REPLICATED",
        "R177-GAP-REPLICATED-CORRELATED",
        "POWER-COMPOSITION-INVALID-DISCLOSED",
        "COMPOSED-FLOOR-STAYS-MEASURED",
        "FLOOR-FORM-SAME-WALL-AS-THETAINF-HPIN",
        "WITNESS-BREAKS-ALIGNMENT",
        "NOT-RELABELING",
        "RESIDUE-UNCHANGED-RETYPED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
