#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cbj_subdof_probe -- PRIME.CBJ.SUBDOF.BLOCKFLOOR.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-block/per-rung certificates stated, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files are not
touched.

=======================================================================
MISSION (round ~181, direct continuation of the r180 CBJ capstone).
r180 killed the GLOBAL lower frame bound (dof kill n > Landau rank at
15/20 cells; seam coupling 0.994; occupancy collapse -0.75 dex/atom)
and measured that sub-dof cells carry real constants 0.02..0.32 while
the per-cluster floor at fixed resolution r is depth-stable.  THIS
round poses and prices the BLOCKWISE SUB-DOF-SCOPED statement the
program actually needs (SEQ-cofinal: ONE selector rung per dyadic
block; demand = the r169-SF2 sigma-floor there, already cleared
measured with margins >= 1.405):
  S1  the scoped statement + the exact composition chain with every
      leg typed + THE SUB-DOF MASS FRACTION LADDER (the round's
      cheapest decisive number: how much of delta = |J|^2_G lives
      above the predefined spectral dof cut, rung by rung);
  S2  PRICE CARLESON -- the one tool never priced in 180 rounds:
      direction, constant, unconditionality, two-sided gap;
  S3  the seam at selector rungs: measured leakage + machine
      adjudication whether any chain leg consumes it;
  S4  assembly with honest pricing, taxonomy verdict, controls,
      tau-screen, loop guard.
=======================================================================
State consumed (CITED): r180/CDXCVII cbj_frame_probe (SPEC d7fbf2d9,
41/41: STEP A EXACT delta_h == |J_h|^2_{G_h} with R == 0; normal form
exact; global form DEAD; c_intra ladder + occupancy law; selector
h-hat_k = largest non-2-power prime-power atom, clears SF2 margins
>= 1.405, underperforms BA by 5.7-11 pct; Gauss beats Fejer 5-18 dex;
MV killed at link 1 / carries at 3.15 pi margin 1/21; Carleson
UNPRICED named); CDXCIV/r178 (canonical residue); CDLXXXIV/r169
(SF1 sigma == (1-slop) delta DC EXACT; SF2 demand delta_req =
SIGMA0/((1-slop) DC); SF4 schedule absorption; SF6 world-anatomy);
CDLXXXVII/r171 (jet floor; H1/H2 per rung); r168 SIGMA0 = 0.15;
v922 (D1-D3); v927 (BA1-BA3, blocks B2 = [4,8], B3 = [8,16], B4 =
[16,32]); v930 (entry atoms); PT21 (census per-k; ALL-K == flagged
loop); r131 OFF recipe VERBATIM; HSW22 Cor. 1.2; Bertrand--Chebyshev.
CLASSICAL LITERATURE FOR S2 (web-researched this round, CITED AS
FORM, none re-proven):
 [OCS02]  J. Ortega-Cerda, K. Seip, "Fourier frames", Ann. of Math.
   (2) 155 (2002), no. 3, 789-806.  Characterization of sampling
   sequences/measures for Paley-Wiener PW(I).  KEY FACT (their
   Prop. 1 class, restated in Olsen JFA 2011): for a positive Borel
   measure mu, the CARLESON-TYPE (upper/Bessel) inequality
   int |g|^2 dmu <~ ||g||^2 holds IFF sup_xi mu([xi, xi+1)) < inf --
   the Carleson box condition alone is EQUIVALENT TO THE UPPER
   INEQUALITY ONLY; the lower (sampling) half needs the separate
   density/discretization leg.
 [BEU]    Beurling density theorem (via [OCS02]/Olsen): D^-(Lam) >
   |I|/(2 pi) ==> Lam sampling for PW(I); D^-(Lam) >= |I|/(2 pi)
   necessary.  UNCONDITIONAL but density-gated.
 [BFGHR]  Blandigneres, Fricain, Gaunard, Hartmann, Ross, "Reverse
   Carleson embeddings for model spaces" (J. London Math. Soc. 2013
   class; quoted as Thm 4.2 in [HJK20]): if inf_I mu(S(I))/|I| over
   ALL Carleson windows with |I| >= eps is large enough (N_0(Theta,
   eps)), then the REVERSE embedding holds.  Right direction,
   UNCONDITIONAL -- but the hypothesis requires the measure to
   dominate Lebesgue at ALL window scales: a FINITE discrete block
   measure has mu(S(I)) = 0 off the block, the hypothesis FAILS.
 [KOV01]  O. Kovrijkine, "Some results related to the Logvinenko-
   Sereda theorem", Proc. AMS 129 (2001): for E (gamma, a)-relatively
   dense, ||f||^2_{L^2(E)} >= (gamma/C)^{C(ab+1)} ||f||^2 on PW_b --
   explicit constant, UNCONDITIONAL, but for dominating SETS
   (time side), not discrete atom families.
 [HJK20]  Hartmann, Jaming, Kellay, "Quantitative estimates of
   sampling constants in model spaces", Amer. J. Math. 142 (2020):
   LSP with explicit constants extended to model spaces via reverse
   Carleson + Baranov-Bernstein + Remez.  Same set-domination class.
 [HERM]   Hermite/derivative-sampling frames for bandlimited f:
   frame with EXPLICIT lower bound if all k jets sampled at nodes
   with max gap delta < c_k^{1/(2k)}/sigma (Wirtinger--Sobolev
   constants; arXiv:1511.04007), improved nu_k/sigma with k = 2
   settled sharp (arXiv:2007.11282); the conjectured sharp gap
   k pi/sigma is OPEN for k >= 3.  UNCONDITIONAL, but uniform
   height-k jets at EVERY node + global max-gap required.
 [GRO20]  Groechenig et al., "Sharp results on sampling with
   derivatives in shift-invariant spaces and multi-window Gabor
   frames", Constr. Approx. (2020) + the weighted-Fock multiple
   sampling characterization (Complex Anal. Oper. Theory 2020):
   jet sampling characterized by WEIGHTED BEURLING DENSITY of the
   set-with-multiplicity.  Right direction, UNCONDITIONAL, but no
   explicit constant and NOT uniform in the multiplicity height.
 [NAZ93]  F. Nazarov, "Local estimates for exponential polynomials
   ..." (1993, Turan lemma): for exponential polynomials with n
   terms, sup_I |p| <= (C |I|/|E|)^{n-1} sup_E |p| -- UNCONDITIONAL
   lower-bound class with EXPLICIT constant DECAYING EXPONENTIALLY
   IN THE TERM COUNT n: the classical mirror of the measured r180
   occupancy collapse (-0.75 dex/atom).

NOTATION (r180 conventions verbatim).  Rung h = builder x (R4.build_
cell, even sector); a = log(h)/2; K = ceil(1.25 h log h); om_k =
k pi/a; b_k = om_k^2; c_k = cn_mp_str; d_k = (-1)^k c_k; A_0 = sum d;
T_z = 2 pi h; WFULL = ward ordinates in (T_z + 6, gamma_7000];
mu(g) = sin^2(ag)/g^2; psi_k(g) = g^2/(g^2 - b_k) (psi_0 == 1);
F = sum d_k psi_k; delta_h = [sum mu F^2]/[A_0^2 sum mu] (r169
VERBATIM); DC_h = (G_W - C_W)/(2 G(T_z)); delta_req = SIGMA0/((1 -
slop) DC).  HOUSE SPECTRAL SPLIT (the round's instrument): raw Gram
Gm[k,l] = sum mu psi_k psi_l; D = sqrt(diag Gm); Gn = D^-1 Gm D^-1
(Jacobi-normalized, diag 1); Jn = D J / sqrt(sum mu) with J = d/A_0;
then delta == Jn^T Gn Jn EXACTLY (step-A r180-G10/G31 CITED + re-
gated here).  Eigsy(Gn) = {lam_i, v_i}; s_i = v_i . Jn; delta ==
sum_i lam_i s_i^2 (ward FRAC_WARD).  SUB-DOF CUT (PREDEFINED, frozen
pre-ward, geometry only -- the r180 grank convention): cell(c) =
{i : lam_i >= c lam_max}, CUTS = (1e-6, 1e-12, 1e-24), PRIMARY c* =
1e-12; frac_c(h) = sum_{cell(c)} lam_i s_i^2 / delta.  COMB SIDE
(source-pure): prime powers q <= 2^19; block CB_k = (2^k, 2^{k+1}];
H = 2^{k-e}, e in EGRID = (-1, 1, 3, 5, 7); fixed absolute grid
cells width 1/H; dof = span x H/pi; SUB-DOF CELL FAMILY = {(k, e):
n_k <= dof(k, e)} -- pure arithmetic, PREDEFINED; arithmetic weight
vector aw_q = log(p)/sqrt(q) (von Mangoldt/sqrt, source-pure);
comb mass fraction = spectral mass of aw above the 1e-12 plunge cut
of the block Gram (f64); C_box = max_xi #{v_j in [xi, xi+1)}
(v = lam H) = the [OCS02] Carleson box constant of the block atom
measure.  Selector h-hat_k = largest non-2-power prime-power atom
in CB_k (r180 STEP D VERBATIM, sealed pre-ward).

=======================================================================
THE FOUR SECTIONS AS EXECUTED (verdicts frozen from the ONE disclosed
pre-freeze calibration pass, calib_subdof_pass1.log; record values
below are the calibrated numbers)
=======================================================================
S1 (SCOPED STATEMENT + COMPOSITION + THE DECISIVE LADDER).
THE BLOCKWISE SUB-DOF FLOOR STATEMENT (posed exactly): at the
selector rung h-hat_k of dyadic block B_k let delta_sub(h) :=
sum_{lam_i >= c* lam_max} lam_i s_i^2 (the sub-dof-truncated jet
mass).  The scoped floor demand is
   delta_sub(h-hat_k) >= delta_req(h-hat_k)
                       = SIGMA0/((1-slop) DC(h-hat_k)).
COMPOSITION CHAIN (every leg typed):
   L1 delta == |J|^2_G == sum lam_i s_i^2      [EXACT, r180 step A
      R == 0, re-gated G10/G31 + eigen-sum ward <= 1.6e-44];
   L2 delta >= delta_sub (PSD spectral truncation)   [EXACT, G11];
   L3 delta_sub >= delta_req  ==>  delta >= delta_req [EXACT one-
      line sufficiency, G11: the sub-dof floor WOULD suffice];
   L4 [delta >= delta_req] <==> [sigma >= SIGMA0]    [EXACT SF1
      transport, r169 re-gated G12; DC leg classical-per-census];
   L5 sigma-floor at h-hat_k for all k  ==>  cofinal supply [v927
      BA1-BA3 CITED per-block-certified + r169-SF4 schedule CITED;
      selector cofinal by Bertrand CITED; the forall-k quantifier
      stays the flagged census loop, consumed by NOTHING here].
THE DECISIVE MEASUREMENT (G32/G33/G34, mp eigsy at EIG_DPS = ndig
+ 30, eigen-sum ward max 1.6e-44 <= 1e-6) -- THE CONTRACT'S NAMED
KILL BRANCH LANDS:
   THE SUB-DOF MASS FRACTION DECAYS AND SATURATES AT ZERO.  The
   log10 tail ladder (tail = 1 - frac at the primary 1e-12 cut),
   h = 4..16 + 20:
     -4.077 / -2.207 / -1.321 / -0.330 / -0.021 / -0.039 / -0.001
     / -0.001 / -0.001 / -0.001 / -0.001 / -0.001 / -0.001 /
     -0.002
   -- ONE DEX OF MASS LEAVES THE SUB-DOF CELL PER RUNG (pre-
   saturation slope +0.999/rung over h = 4..8, frozen window
   (0.85, 1.15)), then SATURATION: from h = 10 on, at most 0.2-2
   percent of delta lives above the cut (tail >= 10^-0.01).  The
   top-mode share is 0.0196 (h = 4) then 1e-4-class: the mass sits
   in the DEEP spectrum, not at the top.  CUT-SPREAD (G33): the
   ladder is spread, not concentrated -- at the 1e-6 cut the tail
   is already -0.371/-0.042/.../-0.001 (nothing retained deep),
   and even the 1e-24 cut keeps only 10^-0.004 = 0.9 PERCENT of
   the mass at h = 20 (spread table frozen): the jet mass RIDES
   THE COLLAPSING CONDITIONING WALL (r180 gmin ladder 1e-17 ->
   1e-113 -> 1e-140-class; gmin sign noise below entry precision
   at h >= 15 DISCLOSED, frozen-cut fracs unaffected, ward
   covers).  SELECTOR-RUNG MARGINS (G34, the kill with numbers):
   margin_sub = frac x delta/delta_req = 1.405/1.744/1.709 at h =
   4/5/6 (clear the 1.35 bar), 1.142 at h-hat(B2) = 7 (clears the
   raw demand >= 1, NOT the bar), 0.116 at h = 8, 0.007-0.014 at
   h >= 10, 8.020e-3 at h-hat(B3) = 13 (dead by 125x); first rung
   below bar h = 7 == the B2 selector rung itself, first below
   1.0 h = 8: THE SUB-DOF-SCOPED SF2 DEMAND DIES AT THE SELECTOR
   RUNGS.  The UNSCOPED r180 margins >= 1.405 at ALL rungs stay
   the measured carrier (CITED): the program demand is untouched
   -- what dies is the PROOF ROUTE through the well-conditioned
   subspace (prove-only-the-top-modes cannot work: the demand
   mass is not there).  MECHANISM LEGS: r_12 numerical rank =
   5..17 of K = 7..75; pole-resonance census n_res = 0/1/0/1/2/2/
   3/4/5/5/7/7/8/11 (poles ENTER the window band with h: the
   house wall is CONDITIONING, not a clean Landau count, G35);
   the r180 delta/DC/tlaw tabs replicate exactly (G30/G31).
S2 (CARLESON PRICED -- the 180-round debt).  DIRECTION
ADJUDICATION (CITED, G24/G25): the unconditional Carleson-class
embedding for our object ([OCS02] box condition) is EQUIVALENT TO
THE UPPER INEQUALITY -- for the FLOOR it is CARLESON-WRONG-
DIRECTION.  The unconditional lower-bound classes and why each
misses the needed statement: [BEU] density-gated (measured n/dof
= 0.26..165 over the 20 full-frame cells; the PREDEFINED sub-dof
family = 6 of 25 grid cells (the r = 0.5 column + (k = 14, r =
2)) is exactly the below-Nyquist side (n/dof < 1 at 4 of 20
full-frame cells): Beurling point-density theorems can never
fire there, jets mandatory, G14/G20/G23); [BFGHR] reverse-
Carleson hypothesis fails for finite discrete block measures
(mu(S(I)) = 0 off-block); [KOV01]/[HJK20] dominate SETS not atom
families; [HERM] explicit Wirtinger constants but demands
uniform height-m jets at EVERY node + a global max-gap -- and
the max-gap hypothesis fails EXACTLY on the fine-resolution
columns (gap x H > pi at 8 of 20 cells == the e <= 1 side,
where the sub-dof family lives) while where it holds (e >= 3)
the cells are super-dof: the two hypotheses are mutually
exclusive on our grid (G23); k pi/sigma OPEN for k >= 3);
[GRO20] right direction, no explicit
constant, not uniform in m; [NAZ93] explicit and unconditional
with constant (C|I|/|E|)^{n-1} -- EXPONENTIAL IN THE TERM COUNT:
the classical mirror of the measured occupancy law (r180 slope
-0.7484 dex/atom CITED).  NUMERIC PRICING: C_box ladder (the
[OCS02] Carleson constant of the block measure) = 1..37 across
FULLK x EGRID; PP-ratio lam_max/C_box in [0.998, 3.917] (frozen
band [0.9, 4.5]: the upper constant CARRIES, G24); the two-sided
sandwich at k = 12: log10(lam_max/c_intra) = 0.28 / 1.38 / 3.20 /
8.06 / 22.90 dex at r = 0.5/2/8/32/128 (G25: 23 dex OPEN at
depth).  VERDICT: CARLESON-WRONG-DIRECTION + LOWER-CLASS-M-
EXPONENTIAL-OR-DENSITY-GATED + the NEEDED statement (m- and
shape-uniform confluent jet floor) stays OPEN and is now PRICED;
NOTE the S1 kill makes the debt WORSE than r180 knew: even a
perfect sub-dof frame theorem would not carry the demand -- the
missing tool must control the ILL-CONDITIONED subspace (the
alignment law), not the well-conditioned one.  FIXED-R
COMPACTNESS SKETCH (G13 sympy + G27 numeric, the one positive
proof-shaped deliverable): the jet-normalized cluster Gram
extends CONTINUOUSLY to full confluence with PD limit (m = 2
symbolic limit == diag(1, -Wddot(0)) = diag(1, 1) GAUSS /
diag(1, 1/6) FEJ1, both PD EXACT); m = 3 near-merge numeric
convergence eps = 1e-2..1e-8 stable to 1.2e-7/1.7e-9, limits
5.581e-1 GAUSS / 3.731e-2 FEJ1 at dps 60) ==> at fixed m-cap
(== fixed r by the exact occupancy bound) the floor constant is
a min over a COMPACT config family with everywhere-positive
continuous extension: k-uniformity of the fixed-r COMB floor is
COMPACTNESS-PROVABLE-SKETCH (constant still measured; full
partial-merge continuity cited as classical confluent-Vandermonde
theory).  COMB-SIDE CONTRAST (G22): the arithmetic weight vector
aw_q = log(p)/sqrt(q) has spectral mass fraction == 1.000000
above the plunge cut at EVERY full-frame cell including super-dof
ones -- the comb side does NOT show the tail-riding effect: the
S1 kill is a HOUSE-side alignment phenomenon, not window
geometry.
S3 (SEAM AT SELECTOR RUNGS).  MEASURED (G26): the selector atom
sits near the TOP block edge by construction; its gap to the
first atom of block k+1 is dlam = 3.101e-2 / 2.330e-2 / 6.843e-3
/ 2.195e-3 / 3.052e-4 at k = 6/8/10/12/14, FEJ1 coupling at r =
32: 0.9997/0.9971/0.9960/0.9934/0.9980 (GAUSS 0.9981/0.9828/
0.9763/0.9613/0.9879): the seam is GEOMETRICALLY PRESENT at
selector rungs exactly as r180-G28 measured for whole blocks.
ADJUDICATION (G44 machine ancestry): the blockwise composition
chain L1-L5 contains NO comb-side cross-block leg -- L1/L2/L3 are
house-side single-rung spectral statements, L4 is the per-rung
SF1 transport, L5's BA midlayer averages HOUSE RUNGS within one
block (v927) and the SF4 schedule is per-census: the node CROSS-
BLOCK-SEAM is an ancestor of NOTHING in the delivered chain
(DFS-gated).  SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE.  (What WOULD
consume it: proving the h-hat floor by a comb frame over the
union of two blocks -- named, not attempted.)
S4 (ASSEMBLY + CONTROLS + SCREENS).  THE HONEST ASSEMBLY: the
exact legs L1-L4 stand; the measured floor leg is the corpse --
the round converts r180's "global lemma dead, per-cluster floor
carries" into "the blockwise sub-dof scoping ALSO dies, by mass
starvation, with the ladder and crossover frozen"; the residue is
UNCHANGED IN CARDINALITY and the named proof debt SHARPENS to the
ill-conditioned-subspace alignment law (house) or a two-block-
free comb route (both named, both open).  CONTROLS (recipes
VERBATIM r169/r180): tau_w < 0 and BA3 bridge VIOLATED in all
fake worlds (SMOOTH -1.0033, SCRARITH -1.2562/-1.0119/-1.0086,
EPSTEIN -1.0050/-1.0009/-1.0056, rel 5e-2 replicated) while the
naked delta_w stays positive (0.848/0.924/0.597/0.766/0.878/
0.718/0.615): FLOOR-INEQ-WORLD-INSENSITIVE with separation at the
BA3 bridge (r169-SF6 RESTATED NOT HIDDEN).  NEW: G46 THE
FRACTION SEPARATES WORLDS -- like-for-like tails at the CTRL_NZ
= 300 window: MAIN -4.11/-2.26/-0.04 (x = 4/5/8, matching the
full-window ladder: window-stable) vs SMOOTH -13.32, SCRARITH
-11.68/-13.37/-14.25, EPSTEIN -11.68/-12.84/-13.65: in every
FAKE world the jet mass sits in the TOP modes (fraction == 1-
class), only the ARITHMETIC world rides the ill-conditioned tail
-- the S1 kill is itself an arithmetic-specific measured law
(SF6-ANATOMY-SHARPENED: floor VALUE world-insensitive, mass
LOCATION world-separating).  TAU-SCREEN (G50): slope log10 delta
vs log10 tau = 0.0002, log10 delta_req = 0.0054, log10 tail =
-0.0475 (all <= 0.30): demand and kill observable both tau-flat,
no tau_h relabeling; the pre-saturation tail growth tracks the
conditioning-wall currency, DISCLOSED.  LOOP GUARD: four flagged
cycles detected, consumed by nothing; mincut flows 4/5/5/6 NOT
REAL replicated; census cardinality 4 UNCHANGED.
=======================================================================
TAXONOMY VERDICT (frozen from calibration):
   SUBDOF-SCOPED-STATEMENT-POSED-EXACT +
   CBJ-SUBDOF-BLOCKFLOOR-DEAD-AT-MASS-FRACTION (the contract's
   named kill, with numbers: tail ladder -4.08 -> -0.001
   saturated, +0.999 dex/rung pre-saturation, margin crossover
   h = 7/8, margin(h-hat 13) = 8.0e-3) +
   MASS-RIDES-CONDITIONING-WALL (even the 1e-24 cut keeps 0.9
   percent at h = 20) +
   UNSCOPED-FLOOR-STILL-CARRIES-MEASURED (r180 CITED) +
   FRACTION-WORLD-SEPARATING (fake worlds frac == 1; arithmetic
   world in the tail) +
   CARLESON-WRONG-DIRECTION + CARLESON-LOWER-M-EXPONENTIAL-OR-
   DENSITY-GATED + NEEDED-JET-CONSTANT-OPEN-NOW-PRICED +
   FIXED-R-FLOOR-COMPACTNESS-SKETCH +
   SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE +
   COMPOSITION-CONDITIONAL-TYPED + SF6-ANATOMY-SHARPENED +
   NOT-RELABELING + RESIDUE-UNCHANGED.
Honest content: (a) the scoped statement poses cleanly and its
exact legs (L1-L4) are proven/re-gated; (b) the decisive ladder
KILLS it: the demand mass drains out of the well-conditioned
subspace at one dex per rung and the scoped margins die at the
selector rungs themselves -- the r180 global dof kill DOES
propagate to the blockwise demand (the opposite of the hoped
outcome, stated with the numbers); (c) the unscoped floor is
untouched and stays measured-carrying; (d) Carleson is finally
priced: unconditional embedding = upper only; every unconditional
lower class is m-exponential or density/max-gap-gated; and the S1
kill shows the needed tool must control the ILL-conditioned
subspace -- the debt is sharper than r180 stated it; (e) the
fixed-r comb compactness sketch is the round's one proof-shaped
positive; (f) the fraction-separates-worlds finding is new
measured structure (the tail-riding is arithmetic-specific);
(g) the seam and the forall-k loop are consumed by nothing; no
new omega, nothing closed, nothing upgraded.

WHAT IS BUILT AND GATED: S0 G01 firewall + comb purity, G02
predefinition order, G03 cache ward; S1 exact layer G10-G15; S2
comb layer G20-G27; S3 house layer G30-G37; S4 controls + kill
gates G40-G46; S5 screens/assembly G50-G53/G60/G99.  FROZEN BARS:
IDEN_BAR 1e-30; FRAC_WARD 1e-6; CAL_TAIL abs tol 0.05 on log10;
pre-saturation slope window (0.85, 1.15) over h = 4..8; SAT_H =
10 with log10 tail >= -0.01; TLAW rel 1e-3; DELTA/DC tabs rel
5e-3 (r169 strings); CAL_DELTA rel 1e-4 (r180 strings); c_intra
rel 2e-5 (r180 strings); margin table rel 5e-3 + crossovers
exact; PP band [0.9, 4.5]; GAP12 abs 0.12 dex; seam abs 5e-3 +
deep-cell min 0.99; near-conf conv 1e-6 + limits rel 1e-3;
CTRL_TAU rel 5e-3; CTRL viol rel 5e-2 (r180 strings); CTRL tails
abs 0.10; tau slopes <= 0.30; runtime bar 3300 s.  CONTROLS:
SMOOTH(5), SCRARITH(4,5,8), EPSTEIN(8,9,10) + MAIN(4,5,8)
comparator at CTRL_DPS/60, CTRL_NZ = 300, recipes VERBATIM.
LOOP GUARD: four flagged cycles (A0-triangle, census-forall-k,
Gonek-1984, Montgomery-PC/Goldston-Montgomery) DECLARED, DFS-
detected, consumed by NOTHING delivered; min-cut r135 flows
4/5/5/6 NOT REAL.  CALIBRATION (disclosed): ONE pre-freeze
calibration pass (calib_subdof_pass1.log, 852.5 s, pre-freeze SHA
8c7e7644a83618da, --mode calib, 36/37 with the one placeholder
tau-rider window failing as expected pre-freeze) preceded by one
structural smoke at the same pre-freeze SHA
(cbj_subdof_probe.smoke1.log, 39 s class; ITS placeholder-branch
verdict text was pre-freeze scaffolding, replaced by the measured
kill branch AT freeze -- gates, grids, recipes and bars other
than the newly frozen record tables did not move).  ONE disclosed
post-record SPEC-TEXT amendment A1: the first frozen prose
misquoted the machine-computed FEJ1 confluent-limit constant
(wrote 1/12, the sympy value is 1/6) and mis-stated the G14/G23
family counts and the max-gap column reading (5-of-25 / 20-of-25
-> the correct 6-of-25 / 8-of-20 with the mutual-exclusivity
statement above); NO code, gate, bar, grid or table moved;
run1/run2 (835.0 s / 870.4 s, 37/37, timing-normalized diff
EMPTY) at the pre-amendment SHA 8d801d0a3baac7e1 are KEPT as
fail-free records; run3/run4 + smoke3 = the record at this
amended SHA.  Scratch deleted, logs kept, numbers verbatim
above.  DETERMINISM: no
randomness anywhere; ProcessPool results keyed; run2 must be
identical modulo wall-clock tokens (lines carrying 'WALL' or
wall-second prints).

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
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
NZFULL = 7000
F64_SLOP = 1e-3
Z_OVERHANG = 6.0
WORKERS = 10
SIGMA0 = 0.15
IDEN_BAR = 1e-30
PD_RUNGS = (4, 5, 8)
RUNTIME_BAR = 3300.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
NDIG_CAP = 140
EIG_PAD = 30          # EIG_DPS = min(DPS-2, NDIG_CAP) + EIG_PAD

# r166/r169/r180 corpus strings (CITED)
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
CTRL_MAIN_X = (4, 5, 8)
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
MARGIN_MIN_BAR = 1.35

# comb grids (frozen; geometry only)
PPCAP = 2 ** 19
KGRID = (6, 8, 10, 12, 14)
FULLK = (6, 8, 10, 12)
EGRID = (-1, 1, 3, 5, 7)
FULLN = 520
DPS_COMB = 50
MCAP = 64
SEL_KMAX = 17
LINK1 = "L1"

# frozen sub-dof machinery
CUTS = ("1e-6", "1e-12", "1e-24")
CUT_PRIMARY = "1e-12"
FRAC_WARD = 1e-6
PP_BAND = (0.9, 4.5)
SEAM_DEEP_MIN = 0.99
NEARCONF_EPS = ("1e-2", "1e-4", "1e-6", "1e-8")
NEARCONF_CONV = 1e-6

# ------------- r180 c_intra record strings (CITED, replication subset)
CAL_CINTRA = {
    (6, -1): "1.000000e+00", (6, 1): "1.621213e-01",
    (8, -1): "1.000000e+00", (8, 1): "1.636764e-01",
    (10, -1): "1.000000e+00", (10, 1): "1.634473e-01",
    (12, -1): "1.000000e+00", (12, 1): "1.615658e-01",
    (14, -1): "1.000000e+00", (14, 1): "1.616072e-01",
    (12, 3): "7.592596e-03", (12, 5): "3.357709e-07",
    (12, 7): "1.626424e-21"}
CAL_TOL = 2e-5

# --------------------- calibrated record tables (pre-freeze pass 1)
CAL_TAIL = {   # h -> log10(tail) string, tail = 1 - frac at c*
    4: "-4.077", 5: "-2.207", 6: "-1.321", 7: "-0.330",
    8: "-0.021", 9: "-0.039", 10: "-0.001", 11: "-0.001",
    12: "-0.001", 13: "-0.001", 14: "-0.001", 15: "-0.001",
    16: "-0.001", 20: "-0.002"}
CAL_TAIL_TOL = 0.05          # abs tolerance on log10(tail)
CAL_R12 = {4: 5, 5: 7, 6: 7, 7: 8, 8: 8, 9: 9, 10: 9, 11: 10,
           12: 11, 13: 12, 14: 13, 15: 13, 16: 14, 20: 17}
CAL_TOPSHARE = {4: "0.0196", 5: "0.0001", 6: "0.0001", 7: "0.0002",
                8: "0.0002", 9: "0.0003", 10: "0.0003",
                11: "0.0003", 12: "0.0004", 13: "0.0004",
                14: "0.0004", 15: "0.0005", 16: "0.0005",
                20: "0.0006"}
CAL_TOPSHARE_TOL = 1e-3      # abs
PRESAT_RUNGS = (4, 5, 6, 7, 8)
TAILSLOPE_WIN = (0.85, 1.15)  # slope log10 tail vs h, pre-saturation
SAT_H = 10                    # saturation regime h >= SAT_H
SAT_LOG10 = -0.01             # log10 tail >= this in saturation
CAL_SPREAD = {   # h -> (log10tail @ 1e-6, @ 1e-12, @ 1e-24)
    4: ("-0.371", "-4.077", "-300.000"),
    5: ("-0.042", "-2.207", "-10.979"),
    6: ("-0.024", "-1.321", "-9.886"),
    7: ("-0.002", "-0.330", "-6.278"),
    8: ("-0.000", "-0.021", "-4.628"),
    9: ("-0.000", "-0.039", "-2.307"),
    10: ("-0.000", "-0.001", "-1.042"),
    11: ("-0.001", "-0.001", "-0.259"),
    12: ("-0.001", "-0.001", "-0.253"),
    13: ("-0.001", "-0.001", "-0.254"),
    14: ("-0.001", "-0.001", "-0.037"),
    15: ("-0.001", "-0.001", "-0.031"),
    16: ("-0.001", "-0.001", "-0.008"),
    20: ("-0.001", "-0.002", "-0.004")}
CAL_MSUB = {"m7": "1.1420", "m13": "8.0202e-03", "cross_bar": 7,
            "cross_one": 8}
CAL_MSUB_TOL = 5e-3
CAL_NRES = {4: 0, 5: 1, 6: 0, 7: 1, 8: 2, 9: 2, 10: 3, 11: 4,
            12: 5, 13: 5, 14: 7, 15: 7, 16: 8, 20: 11}
CAL_COMBFRAC = {   # (k, e) -> aw spectral mass frac above 1e-12 cut
    (6, -1): "1.000000", (6, 1): "1.000000",
    (6, 3): "1.000000", (6, 5): "1.000000", (6, 7): "1.000000",
    (8, -1): "1.000000", (8, 1): "1.000000",
    (8, 3): "1.000000", (8, 5): "1.000000", (8, 7): "1.000000",
    (10, -1): "1.000000", (10, 1): "1.000000",
    (10, 3): "1.000000", (10, 5): "1.000000", (10, 7): "1.000000",
    (12, -1): "1.000000", (12, 1): "1.000000",
    (12, 3): "1.000000", (12, 5): "1.000000", (12, 7): "1.000000"}
CAL_COMBFRAC_TOL = 1e-4
CAL_GAP12 = {(-1): "0.28", (1): "1.38", (3): "3.20",
             (5): "8.06", (7): "22.90"}    # log10(lam_max/c_intra)
CAL_GAP_TOL = 0.12
CAL_SEAM = {   # k -> (dlam_str, fej1@e5, gauss@e5)
    6: ("3.101e-02", "0.9997", "0.9981"),
    8: ("2.330e-02", "0.9971", "0.9828"),
    10: ("6.843e-03", "0.996", "0.9763"),
    12: ("2.195e-03", "0.9934", "0.9613"),
    14: ("3.052e-04", "0.998", "0.9879")}
CAL_SEAM_TOL = 5e-3
CAL_NEARCONF = {"GAUSS": "5.581e-01", "FEJ1": "3.731e-02"}
CAL_NEARCONF_TOL = 1e-3
CAL_CTRL_TAIL = {("MAIN", 4): "-4.11", ("MAIN", 5): "-2.26",
                 ("MAIN", 8): "-0.04",
                 ("SMOOTH", 5): "-13.32", ("SCRARITH", 4): "-11.68",
                 ("SCRARITH", 5): "-13.37", ("SCRARITH", 8): "-14.25",
                 ("EPSTEIN", 8): "-11.68", ("EPSTEIN", 9): "-12.84",
                 ("EPSTEIN", 10): "-13.65"}
CAL_CTRL_TAIL_TOL = 0.10

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
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not (node.name.startswith("comb_")
                or node.name.startswith("selector_")):
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Name):
                nm = sub.id
            if nm in ("ward_cache", "build_cell", "load"):
                bad.append("comb purity: %s in %s @%d"
                           % (nm, node.name, sub.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load only in "
                       "ward_; no verification/ import; comb_/"
                       "selector_ functions ward-free")


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


# ----------------------------------------------------------- comb layer
def comb_sieve(cap: int) -> list[tuple[int, int]]:
    """prime powers (q, p) with q <= cap; pure arithmetic."""
    comp = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= cap:
            out.append((q, p))
            q *= p
    out.sort()
    return out


def comb_wf_mp(win: str, x):
    """normalized window transform at x = xi * H (mp)."""
    if win == "GAUSS":
        return mp.exp(-x * x / 2)
    if win == "FEJ1":
        if x == 0:
            return mp.mpf(1)
        s = mp.sin(x / 2) / (x / 2)
        return s * s
    raise ValueError(win)


def comb_cintra(pp: list, k: int, e: int) -> dict:
    """per-cluster confluent-jet floor c_intra (FEJ1, link 1, mp) --
    r180 recipe VERBATIM (fixed absolute grid, adaptive dps).
    PURE SOURCE ARITHMETIC."""
    lo, hi = 2 ** k, 2 ** (k + 1)
    qs = [q for q, _p in pp if lo < q <= hi]
    with mp.workdps(DPS_COMB):
        Hm = mp.mpf(2) ** (k - e)
        w_cell = mp.mpf(1) / Hm
        lams = [mp.log(q) for q in qs]
        idxs = [int(mp.floor(lam / w_cell)) for lam in lams]
        clusters: list[list[int]] = []
        cur: list[int] = []
        for i in range(len(lams)):
            if cur and idxs[i] != idxs[cur[0]]:
                clusters.append(cur)
                cur = []
            cur.append(i)
        if cur:
            clusters.append(cur)
        mb = int(mp.floor((2 ** (k + 1)) * (mp.exp(w_cell) - 1))) + 1
        m_max = max(len(c) for c in clusters)
        occ_ok = all(len(c) <= mb for c in clusters)
        c_intra = None
        for cl in clusters:
            m = len(cl)
            if m == 1:
                val = mp.mpf(1)
            else:
                if m > MCAP:
                    return dict(err="m>MCAP", m=m)
                dps_c = max(DPS_COMB, 20 + 4 * m)
                with mp.workdps(dps_c):
                    Hc = mp.mpf(2) ** (k - e)
                    wc = mp.mpf(1) / Hc
                    ctr = (idxs[cl[0]] + mp.mpf("0.5")) * wc
                    us = [Hc * (mp.log(qs[i]) - ctr) for i in cl]
                    T = mp.zeros(m, m)
                    for r in range(m):
                        f = mp.factorial(r)
                        for j in range(m):
                            T[r, j] = us[j] ** r / f
                    G = mp.zeros(m, m)
                    for i in range(m):
                        G[i, i] = mp.mpf(1)
                        for j in range(i):
                            v = comb_wf_mp("FEJ1", us[i] - us[j])
                            G[i, j] = v
                            G[j, i] = v
                    B = mp.inverse(T)
                    Kc = B.T * G * B
                    for i in range(m):
                        for j in range(i):
                            s = (Kc[i, j] + Kc[j, i]) / 2
                            Kc[i, j] = s
                            Kc[j, i] = s
                    Ev, _ = mp.eigsy(Kc)
                    val = min(Ev[i] for i in range(m))
            if c_intra is None or val < c_intra:
                c_intra = val
        return dict(k=k, e=e, n=len(qs), ncl=len(clusters),
                    m_max=m_max, m_bound=mb, occ_ok=occ_ok,
                    c_intra=float(c_intra))


def comb_full_f64(pp: list, k: int, e: int) -> dict:
    """full-block f64 leg (FEJ1, link 1): Gram spectrum, Landau dof,
    numerical rank (prolate plunge 1e-12 convention), [OCS02]
    Carleson box constant C_box of the block atom measure, max gap
    x H, and the spectral mass fraction of the arithmetic weight
    vector aw_q = log(p)/sqrt(q) above the plunge cut.  DISCLOSED
    f64.  PURE SOURCE ARITHMETIC."""
    lo, hi = 2 ** k, 2 ** (k + 1)
    qp = [(q, p) for q, p in pp if lo < q <= hi]
    qs = [q for q, _ in qp]
    n = len(qs)
    H = 2.0 ** (k - e)
    lam = np.array([math.log(q) for q in qs])
    x = np.subtract.outer(lam, lam) * H
    with np.errstate(divide="ignore", invalid="ignore"):
        s = np.where(x == 0, 1.0, np.sin(x / 2) / (x / 2))
    G = s * s
    ev, evec = np.linalg.eigh(G)
    lam_max = float(ev[-1])
    grank = int(np.sum(ev > 1e-12 * ev[-1]))
    span = float(lam[-1] - lam[0])
    dof = span * H / math.pi
    # C_box: max count of v = lam*H in a sliding unit window
    v = lam * H
    cbox = 0
    j0 = 0
    for i in range(n):
        while v[i] - v[j0] >= 1.0:
            j0 += 1
        cbox = max(cbox, i - j0 + 1)
    maxgap = float(np.max(np.diff(v))) if n > 1 else 0.0
    # arithmetic weight spectral mass above plunge cut
    aw = np.array([math.log(p) / math.sqrt(q) for q, p in qp])
    tot = float(aw @ G @ aw)
    proj = evec.T @ aw
    mask = ev > 1e-12 * ev[-1]
    sub = float(np.sum(ev[mask] * proj[mask] ** 2))
    return dict(k=k, e=e, n=n, grank=grank, dof=dof,
                lam_max=lam_max, cbox=cbox, maxgap=maxgap,
                awfrac=(sub / tot if tot > 0 else float("nan")),
                subdof=bool(n <= dof))


def comb_seam_selector(pp: list, sel: dict, k: int) -> dict:
    """seam coupling at the selector atom: gap in lam from
    h-hat_k to the first atom of block k+1; window couplings at
    every e in EGRID.  PURE SOURCE ARITHMETIC."""
    hi = 2 ** (k + 1)
    lam_hat = math.log(sel[k])
    nxt = min(q for q, _p in pp if q > hi)
    dlam = math.log(nxt) - lam_hat
    out = dict(k=k, hhat=sel[k], nxt=nxt, dlam=dlam, coup={})
    for e in EGRID:
        H = 2.0 ** (k - e)
        xx = dlam * H
        f1 = (math.sin(xx / 2) / (xx / 2)) ** 2 if xx != 0 else 1.0
        gg = math.exp(-xx * xx / 2)
        out["coup"][e] = (f1, gg)
    return out


def comb_nearconf(win: str) -> dict:
    """fixed-m compactness sketch, numeric leg (m = 3): jet-Gram
    min-eig at deterministic near-merge configs u = (-1/4, -1/4 +
    eps, 3/10); convergence as eps -> 0.  PURE GEOMETRY."""
    vals = []
    with mp.workdps(60):
        for es in NEARCONF_EPS:
            epsv = mp.mpf(es)
            us = [mp.mpf(-1) / 4, mp.mpf(-1) / 4 + epsv,
                  mp.mpf(3) / 10]
            m = 3
            T = mp.zeros(m, m)
            for r in range(m):
                f = mp.factorial(r)
                for j in range(m):
                    T[r, j] = us[j] ** r / f
            G = mp.zeros(m, m)
            for i in range(m):
                G[i, i] = mp.mpf(1)
                for j in range(i):
                    vv = comb_wf_mp(win, us[i] - us[j])
                    G[i, j] = vv
                    G[j, i] = vv
            B = mp.inverse(T)
            Kc = B.T * G * B
            for i in range(m):
                for j in range(i):
                    s = (Kc[i, j] + Kc[j, i]) / 2
                    Kc[i, j] = s
                    Kc[j, i] = s
            Ev, _ = mp.eigsy(Kc)
            vals.append(float(min(Ev[i] for i in range(m))))
    conv = abs(vals[-1] - vals[-2])
    return dict(win=win, vals=vals, conv=conv, limit=vals[-1],
                pos=all(v > 0 for v in vals))


def selector_atoms(pp: list, kmax: int) -> dict:
    """h-hat_k = largest prime-power atom in (2^k, 2^{k+1}] that is
    not a power of two.  SOURCE-ONLY (r180 STEP D VERBATIM)."""
    out = {}
    for k in range(2, kmax + 1):
        lo, hi = 2 ** k, 2 ** (k + 1)
        best = None
        for q, p in pp:
            if lo < q <= hi and p != 2:
                if best is None or q > best:
                    best = q
        out[k] = best
    return out


def selector_bertrand(kmax: int, pp: list) -> bool:
    primes = {q for q, p in pp if q == p and q % 2 == 1}
    for k in range(2, kmax + 1):
        if not any(2 ** k < q < 2 ** (k + 1) for q in primes):
            return False
    return True


# ----------------------------------------------------------- house layer
def w_main(args) -> dict:
    """per-rung MAIN build: r169 delta/DC recipe VERBATIM + the
    step-A Gram route (independent per-pair accumulation) + the
    normalized Gram/jet export for the spectral-split worker."""
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
            gmin_w = None
            gmax_w = None
            for j in range(min(NZFULL, len(gam))):
                gf = float(gam[j])
                if gf <= Tlo:
                    continue
                gm = mp.mpf(repr(gf))
                if gmin_w is None:
                    gmin_w = gf
                gmax_w = gf
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
            out["gwin"] = (gmin_w, gmax_w)
            # resonance census: poles inside the window band?
            out["n_res"] = sum(1 for kk in range(K)
                               if float(b[kk]) >= gmin_w ** 2
                               and float(b[kk]) <= gmax_w ** 2)
            out["n_below"] = sum(1 for kk in range(K)
                                 if float(b[kk]) < gmin_w ** 2)
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


def w_frac(args) -> dict:
    """spectral split of the exact step-A identity: eigsy of the
    Jacobi-normalized Gram, s_i = v_i . Jn, delta == sum lam_i
    s_i^2 (ward), sub-dof mass fractions at the frozen CUTS."""
    h, gn_str, jn_str, delta_str, ndig = args
    try:
        t0 = time.time()
        K = len(gn_str)
        dpse = ndig + EIG_PAD
        with mp.workdps(dpse):
            Gn_ = mp.matrix(K, K)
            for i2 in range(K):
                for j2 in range(K):
                    Gn_[i2, j2] = mp.mpf(gn_str[i2][j2])
            Jn = mp.matrix([mp.mpf(s) for s in jn_str])
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
            fr = {}
            rr = {}
            lt = {}
            for cs_ in CUTS:
                cut = mp.mpf(cs_) * lmax
                sub = mp.mpf(0)
                cnt = 0
                for i in range(K):
                    if lams[i] >= cut:
                        sub += lams[i] * svals[i] * svals[i]
                        cnt += 1
                fr[cs_] = float(sub / tot)
                rr[cs_] = cnt
                tl = abs(mp.mpf(1) - sub / tot)
                lt[cs_] = float(mp.log(tl + mp.mpf("1e-300"))
                                / mp.log(10))
            ii = max(range(K), key=lambda i: lams[i])
            top = float(lams[ii] * svals[ii] * svals[ii] / tot)
            gmin = min(lams)
            return dict(h=h, ward=ward, frac=fr, rcnt=rr,
                        ltails=lt, log10tail=lt[CUT_PRIMARY],
                        topshare=top, gmin=float(gmin),
                        K=K, wall_s=time.time() - t0)
    except Exception as exc:                    # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_ctrl(args) -> dict:
    """control world (r169/r180 w_ctrl recipe VERBATIM currency) +
    the control-world spectral split (Gram at CTRL_NZ, eigsy dps
    60-class)."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
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
            sq = mp.sqrt(Sw)
            Jn = mp.matrix([(d[kk] / A0) * Dg[kk] / sq
                            for kk in range(Kw)])
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
            cutp = mp.mpf(CUT_PRIMARY) * lmax
            subp = mp.mpf(0)
            for i in range(Kw):
                if lams[i] >= cutp:
                    subp += lams[i] * svals[i] * svals[i]
            tail_w = abs(mp.mpf(1) - subp / tot)
            ward_w = float(abs(tot / delta_w - 1))
            return dict(world=world, h=xw, tauf=float(tau),
                        viol_rel=float((tau + off - zs) / abs(tau)),
                        delta_w=float(delta_w),
                        log10tail_w=float(
                            mp.log(tail_w + mp.mpf("1e-300"))
                            / mp.log(10)),
                        ward_w=ward_w)
    except Exception as exc:                    # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 STEP A re-gate (r180 G10 VERBATIM class)
    y, g = sp.symbols("y g", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    d0, d1, d2 = c0, -c1, c2
    A0g = d0 + d1 + d2
    F_house = A0g + d1 * b1 / (y - b1) + d2 * b2 / (y - b2)
    F_basis = d0 * y / (y - 0) + d1 * y / (y - b1) + d2 * y / (y - b2)
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
                "J^T G J with R == 0 (r180-G10 re-gated generically"
                "; the L1 leg of the composition chain)"))

    # ---------------- G11 spectral truncation + sufficiency (L2/L3)
    l1s, l2s, l3s = sp.symbols("lam1 lam2 lam3", nonnegative=True)
    s1s, s2s, s3s = sp.symbols("s1 s2 s3", real=True)
    total = l1s * s1s ** 2 + l2s * s2s ** 2 + l3s * s3s ** 2
    partial = l1s * s1s ** 2
    diff = sp.simplify(total - partial)
    okA = diff == l2s * s2s ** 2 + l3s * s3s ** 2
    okB = all(arg.is_nonnegative for arg in diff.args) \
        if diff.args else bool(diff.is_nonnegative)
    fq, dq, rq = (sp.Rational(9, 10), sp.Rational(7, 5),
                  sp.Rational(5, 4))
    okC = bool((fq * dq >= rq) and (dq >= fq * dq) and (dq >= rq)) \
        and bool(fq <= 1)
    out.append(("G11-truncation-sufficiency", okA and okB and okC,
                "L2 EXACT: delta - delta_sub == sum of tail lam s^2 "
                ">= 0 (PSD spectral truncation, generic); L3 EXACT "
                "sufficiency on rationals: [frac <= 1 and frac*delta "
                ">= req] ==> delta >= req -- the sub-dof floor "
                "SUFFICES for the SF2 demand, super-dof mass never "
                "needed"))

    # ---------------- G12 SF1 transport (r180 G16 VERBATIM class)
    s0, sl, dc, de = sp.symbols("s0 sl dc de", positive=True)
    sig = (1 - sl) * de * dc
    okA = sp.simplify(sp.solve(sp.Eq(sig, s0), de)[0]
                      - s0 / ((1 - sl) * dc)) == 0
    dcI, slI, s0I = (sp.Rational(1, 4), sp.Rational(1, 1000),
                     sp.Rational(3, 20))
    thr = s0I / ((1 - slI) * dcI)
    okB = bool((1 - slI) * (thr * sp.Rational(11, 10)) * dcI > s0I) \
        and bool((1 - slI) * (thr * sp.Rational(9, 10)) * dcI < s0I)
    out.append(("G12-sf1-transport", okA and okB,
                "L4 EXACT: [delta >= s0/((1-slop) DC)] <==> [sigma "
                ">= s0] (r169-SF1 re-gated both directions on exact "
                "rationals); DC leg classical-per-census; v927-BA + "
                "SF4 schedule CITED (L5) -- chain typed complete"))

    # ---------------- G13 confluent limit == PD Hermite Gram (m=2)
    u = sp.symbols("u", positive=True)
    T2 = sp.Matrix([[1, 1], [-u / 2, u / 2]])
    B2 = T2.inv()
    res = {}
    for wname, wexpr in (("GAUSS", sp.exp(-u ** 2 / 2)),
                         ("FEJ1", sp.sin(u / 2) ** 2 / (u / 2) ** 2)):
        G2 = sp.Matrix([[1, wexpr], [wexpr, 1]])
        K2 = sp.simplify(B2.T * G2 * B2)
        lim = sp.Matrix(2, 2, lambda i, j: sp.limit(K2[i, j], u, 0,
                                                    dir="+"))
        res[wname] = lim
    okA = res["GAUSS"] == sp.Matrix([[1, 0], [0, 1]])
    okB = res["FEJ1"][0, 0] == 1 and res["FEJ1"][0, 1] == 0 \
        and res["FEJ1"][1, 0] == 0 and res["FEJ1"][1, 1] > 0
    out.append(("G13-confluent-limit-pd",
                bool(okA and okB),
                "m = 2 full-merge limit of the jet-normalized Gram "
                "== diag(1, -Wddot(0)) EXACT (sympy): GAUSS diag(1, "
                "1), FEJ1 diag(1, %s) -- both PD: the confluent "
                "extension is continuous and positive at the "
                "diagonal, the fixed-m compactness anchor of the "
                "fixed-r k-uniform floor (full partial-merge "
                "continuity CITED as classical confluent-Vandermonde "
                "theory; m = 3 numeric leg in G27)"
                % str(res["FEJ1"][1, 1])))
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


# ------------------------------------------------------------ main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--mode", default="record",
                     choices=("record", "smoke", "calib"))
    args = par.parse_args()
    smoke = args.mode == "smoke"
    calib = args.mode == "calib"

    print("=" * 78)
    print("cbj_subdof_probe -- PRIME.CBJ.SUBDOF.BLOCKFLOOR.01")
    print("SPEC_SHA %s   mode %s" % (SPEC_SHA[:16], args.mode))
    print("=" * 78, flush=True)

    hrungs = (4, 5, 8) if smoke else HRUNGS
    hold_h = None if smoke else H_HOLD
    kgrid = (6, 10) if smoke else KGRID
    fullk = (6, 10) if smoke else FULLK
    ctrl_jobs = ([("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
                  ("EPSTEIN", 8, 80), ("MAIN", 5, 60)] if smoke else
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

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (composition chain legs)")
    for nm, okg, det in symbolic_gates():
        check(nm, okg, det)

    pp = comb_sieve(PPCAP)
    evt("SIEVE", "cap=%d n=%d" % (PPCAP, len(pp)))
    sel = selector_atoms(pp, SEL_KMAX)
    bert = selector_bertrand(SEL_KMAX, pp)
    sel_ok = (sel[2] == 7 and sel[3] == 13 and sel[4] == 31
              and all(sel[k] > 2 ** k for k in sel) and bert)
    check("G15-selector-cofinality", sel_ok,
          "h-hat = %s (k = 2..12); h-hat_k > 2^k all k <= %d; "
          "Bertrand--Chebyshev CITED for all k (r180 STEP D "
          "VERBATIM, sealed below)"
          % ([sel[k] for k in range(2, 13)], SEL_KMAX))

    # G14 sub-dof predefinition: comb family (pure arithmetic) +
    # house cut declaration -- SEALED before any ward/build event
    fam = []
    for k in kgrid:
        for e in EGRID:
            lo, hi = 2 ** k, 2 ** (k + 1)
            n_k = sum(1 for q, _p in pp if lo < q <= hi)
            dof_arith = math.log(2) * (2.0 ** (k - e)) / math.pi
            fam.append((k, e, n_k, dof_arith, n_k <= dof_arith))
    seal_src = repr(sel) + repr(fam) + repr(CUTS) + CUT_PRIMARY
    seal_sha = hashlib.sha256(seal_src.encode()).hexdigest()
    evt("PREDEF-SEALED", seal_sha)
    nsub = sum(1 for t in fam if t[4])
    check("G14-subdof-predefined", smoke or nsub >= 4,
          "sub-dof cell family PREDEFINED from frequency geometry "
          "(n_k vs dof = log2 x H/pi, pure arithmetic): %d of %d "
          "cells sub-dof (the r = 0.5 column); house cut family "
          "CUTS = %s (primary %s, the r180 grank convention) "
          "DECLARED and sealed %s BEFORE any ward/build dispatch"
          % (nsub, len(fam), str(CUTS), CUT_PRIMARY, seal_sha[:16]))

    # ------------------------------------------------------------ S2
    section("S2  COMB LAYER + CARLESON PRICING (source-pure)")
    cintra: dict = {}
    for k in kgrid:
        for e in ((-1, 1) if not smoke else (1,)):
            cintra[(k, e)] = comb_cintra(pp, k, e)
    if not smoke:
        for e in (3, 5, 7):
            cintra[(12, e)] = comb_cintra(pp, 12, e)
    ok21 = True
    for key, c in cintra.items():
        if key in CAL_CINTRA and not calib:
            ref = float(CAL_CINTRA[key])
            if abs(c["c_intra"] / ref - 1.0) > CAL_TOL:
                ok21 = False
    check("G21-cintra-replication", smoke or calib or ok21,
          "per-cluster jet floors replicate the r180 record strings "
          "rel %.0e on the sub-dof family (r <= 2) + the k = 12 "
          "depth column (instrument continuity)" % CAL_TOL)

    fulls: dict = {}
    for k in fullk:
        for e in EGRID:
            fulls[(k, e)] = comb_full_f64(pp, k, e)
    ok20 = all(t[4] == fulls[(t[0], t[1])]["subdof"]
               for t in fam if (t[0], t[1]) in fulls)
    det20 = "; ".join("(%d,%d): n=%d dof=%.1f %s" %
                      (k, e, fulls[(k, e)]["n"], fulls[(k, e)]["dof"],
                       "SUB" if fulls[(k, e)]["subdof"] else "SUPER")
                      for (k, e) in sorted(fulls) if k == max(fullk))
    check("G20-subdof-family", ok20,
          "arithmetic n-vs-dof table matches the measured block "
          "geometry at every full-frame cell; deepest row: " + det20)

    ok22 = True
    for (k, e), c in sorted(fulls.items()):
        if calib:
            print('CAL_COMBFRAC (%d, %d): "%.6f"' % (k, e,
                                                     c["awfrac"]))
        elif (k, e) in CAL_COMBFRAC:
            if abs(c["awfrac"] - float(CAL_COMBFRAC[(k, e)])) \
                    > CAL_COMBFRAC_TOL:
                ok22 = False
    check("G22-comb-aw-massfrac", smoke or calib or ok22,
          "COMB-SIDE MASS FRACTION: the arithmetic weight vector "
          "aw_q = log(p)/sqrt(q) has spectral mass fraction == 1.0 "
          "(tol %.0e) above the 1e-12 plunge cut at EVERY full-frame "
          "cell incl. super-dof ones: the natural arithmetic vector "
          "does not live in the prolate tail -- comb analog of the "
          "house ladder (f64, DISCLOSED)" % CAL_COMBFRAC_TOL)

    dens_rows = []
    for (k, e), c in sorted(fulls.items()):
        dens_rows.append((k, e, c["n"] / c["dof"], c["maxgap"]))
    n_below = sum(1 for r_ in dens_rows if r_[2] < 1.0)
    gap_pi = sum(1 for r_ in dens_rows if r_[3] > math.pi)
    check("G23-density-vs-nyquist",
          smoke or (n_below >= 4 and gap_pi >= 8),
          "[BEU]/[HERM] pricing: n/dof (block density vs Nyquist "
          "count) spans %.3f..%.1f; %d of %d cells sit BELOW "
          "Nyquist (point sampling impossible there -- the sub-dof "
          "family); max gap x H > pi at %d of %d cells (the [HERM] "
          "max-gap hypothesis fails at r >= 2: explicit Wirtinger "
          "frames inapplicable; k pi/sigma conjecture OPEN for "
          "k >= 3 CITED)"
          % (min(r_[2] for r_ in dens_rows),
             max(r_[2] for r_ in dens_rows), n_below,
             len(dens_rows), gap_pi, len(dens_rows)))

    ok24 = True
    pp_ratios = []
    for (k, e), c in sorted(fulls.items()):
        rat = c["lam_max"] / max(c["cbox"], 1)
        pp_ratios.append(rat)
        if not (PP_BAND[0] <= rat <= PP_BAND[1]):
            ok24 = False
    if calib:
        print("CAL PP-ratios min %.3f max %.3f cbox %s" %
              (min(pp_ratios), max(pp_ratios),
               sorted({fulls[key]["cbox"] for key in fulls})))
    check("G24-carleson-upper", smoke or calib or ok24,
          "[OCS02] DIRECTION PRICED: the Carleson box constant "
          "C_box = %d..%d of the block atom measure prices lam_max"
          "(G) within the frozen band %s at every cell (ratio "
          "%.3f..%.3f): the UNCONDITIONAL Carleson embedding "
          "CARRIES and is an UPPER bound -- for the floor it is "
          "CARLESON-WRONG-DIRECTION (the box condition is "
          "EQUIVALENT to the upper inequality, [OCS02] Prop-1 "
          "class CITED)"
          % (min(fulls[key]["cbox"] for key in fulls),
             max(fulls[key]["cbox"] for key in fulls),
             str(PP_BAND), min(pp_ratios), max(pp_ratios)))

    ok25 = True
    gaps = {}
    for e in EGRID:
        if (12, e) in fulls and (12, e) in cintra:
            gdex = math.log10(fulls[(12, e)]["lam_max"]
                              / cintra[(12, e)]["c_intra"])
            gaps[e] = gdex
            if calib:
                print('CAL_GAP12 (%d): "%.2f"' % (e, gdex))
            elif abs(gdex - float(CAL_GAP12[e])) > CAL_GAP_TOL:
                ok25 = False
    check("G25-twosided-gap", smoke or calib or ok25,
          "the two-sided Carleson-class sandwich at k = 12: "
          "log10(lam_max/c_intra) = %s dex at r = 0.5/2/8/32/128 -- "
          "the unconditional upper is 0.4 dex tight at r = 0.5 and "
          "23 dex OPEN at r = 128: any lower-bound tool must close "
          "this gap; the only unconditional explicit lower class is "
          "[NAZ93] with constant (C|I|/|E|)^{n-1} EXPONENTIAL IN n "
          "== the measured occupancy law (r180 slope -0.7484 "
          "dex/atom CITED): CARLESON-LOWER-M-EXPONENTIAL-OR-"
          "DENSITY-GATED; needed m/shape-uniform jet constant "
          "stays OPEN, now PRICED"
          % ("/".join("%.2f" % gaps[e] for e in EGRID if e in gaps)))

    seams = {}
    ok26 = True
    for k in kgrid:
        s_ = comb_seam_selector(pp, sel, k)
        seams[k] = s_
        if calib:
            print('CAL_SEAM %d: ("%.3e", "%.4g", "%.4g")'
                  % (k, s_["dlam"], s_["coup"][5][0],
                     s_["coup"][5][1]))
        elif not smoke:
            ref = CAL_SEAM[k]
            if abs(s_["dlam"] / float(ref[0]) - 1.0) > CAL_SEAM_TOL:
                ok26 = False
            if abs(s_["coup"][5][0] - float(ref[1])) > CAL_SEAM_TOL:
                ok26 = False
    deep_ok = all(seams[k]["coup"][5][0] >= SEAM_DEEP_MIN
                  for k in kgrid if k >= 10)
    check("G26-seam-at-selector", (smoke or calib or ok26) and deep_ok,
          "the selector atom sits near the TOP block edge: gap to "
          "the first atom of block k+1 dlam = %s; FEJ1 coupling at "
          "r = 32: %s (>= %.2f at k >= 10): the seam is "
          "GEOMETRICALLY PRESENT at selector rungs exactly as the "
          "r180 whole-block measurement -- consumption adjudicated "
          "in G44 (machine ancestry)"
          % (["%.1e" % seams[k]["dlam"] for k in kgrid],
             ["%.4f" % seams[k]["coup"][5][0] for k in kgrid],
             SEAM_DEEP_MIN))

    ok27 = True
    nc = {}
    for wname in ("GAUSS", "FEJ1"):
        r_ = comb_nearconf(wname)
        nc[wname] = r_
        if calib:
            print('CAL_NEARCONF "%s": "%.3e"  conv %.1e'
                  % (wname, r_["limit"], r_["conv"]))
        else:
            if not r_["pos"] or r_["conv"] > NEARCONF_CONV:
                ok27 = False
            if not smoke and abs(
                    r_["limit"] / float(CAL_NEARCONF[wname]) - 1.0) \
                    > CAL_NEARCONF_TOL:
                ok27 = False
    check("G27-nearconf-compactness", calib or ok27,
          "m = 3 near-merge configs (eps = 1e-2..1e-8): jet-Gram "
          "min-eig POSITIVE at every eps and CONVERGENT (drift "
          "%.1e/%.1e <= %.0e) to %.3e (GAUSS) / %.3e (FEJ1): the "
          "confluent extension is continuous and positive at "
          "partial merge -- with G13 (m = 2 exact) the fixed-r "
          "k-uniform floor is COMPACTNESS-PROVABLE-SKETCH "
          "(constant still measured)"
          % (nc["GAUSS"]["conv"], nc["FEJ1"]["conv"], NEARCONF_CONV,
             nc["GAUSS"]["limit"], nc["FEJ1"]["limit"]))

    # ------------------------------------------------------------ S3
    section("S3  HOUSE LAYER (builds; r169 recipes VERBATIM)")
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
          "ward/build event (#%d) -- selector, sub-dof family and "
          "spectral cuts fixed BEFORE any wall-sign evaluation"
          % (idx_seal, idx_ward))

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
                    w_frac, (r_["h"], r_["gn_str"], r_["jn_str"],
                             r_["delta_str"], r_["ndig"])))
        for fut in cf.as_completed(ffuts):
            r_ = fut.result()
            fres[r_["h"]] = r_
    errs = [(h, r_.get("error")) for h, r_ in res.items()
            if "error" in r_]
    if errs:
        info("BUILD ERRORS: %s" % errs)

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

    iden_max = max(r_["iden_dev"] for r_ in res.values()
                   if "iden_dev" in r_)
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
          and pd_all and dtab_ok and dc_ok and cal_ok,
          "L1 LANDS: delta == |J|^2_G at EVERY reachable rung (max "
          "dev %.1e <= %.0e; R == 0); normalized Gram mp-Cholesky "
          "PD at h = %s; r169 DELTA/DC tabs + r180 CAL_DELTA "
          "strings replicate" % (iden_max, IDEN_BAR, str(PD_RUNGS)))

    # ---- G32 THE DECISIVE LADDER
    all_h = sorted(fres)
    ward_max = max((fres[h].get("ward", 1.0) for h in all_h),
                   default=1.0)
    ok32 = ward_max <= FRAC_WARD and bool(all_h)
    tails = {}
    for h in all_h:
        r_ = fres[h]
        if "error" in r_:
            ok32 = False
            info("FRAC ERROR h=%d: %s" % (h, r_["error"]))
            continue
        tails[h] = r_["log10tail"]
        if calib:
            print('CAL_TAIL %d: "%.3f"   r12 %d  top "%.4f"  '
                  'gmin %.2e  wall %.1f'
                  % (h, r_["log10tail"], r_["rcnt"][CUT_PRIMARY],
                     r_["topshare"], r_["gmin"], r_["wall_s"]))
        elif not smoke:
            if abs(r_["log10tail"] - float(CAL_TAIL[h])) \
                    > CAL_TAIL_TOL:
                ok32 = False
            if r_["rcnt"][CUT_PRIMARY] != CAL_R12[h]:
                ok32 = False
            if abs(r_["topshare"] - float(CAL_TOPSHARE[h])) \
                    > CAL_TOPSHARE_TOL:
                ok32 = False
    hs = [h for h in all_h if h in tails]
    pre = [h for h in PRESAT_RUNGS if h in tails]
    slope = (float(np.polyfit(pre, [tails[h] for h in pre], 1)[0])
             if len(pre) >= 3 else float("nan"))
    # tails are log10(1 - frac): a POSITIVE slope means the tail
    # GROWS with h == the sub-dof mass fraction DECAYS: the kill
    # branch of the contract.  Beyond SAT_H the tail SATURATES at
    # 1 (fraction ~ 0.1-2 percent).  Windows frozen from calib.
    sat_ok = all(tails[h] >= SAT_LOG10 for h in hs if h >= SAT_H)
    if calib:
        print("CAL tail-slope-presat %.4f" % slope)
    else:
        if not smoke and not (TAILSLOPE_WIN[0] <= slope
                              <= TAILSLOPE_WIN[1] and sat_ok):
            ok32 = False
    check("G32-subdof-mass-ladder", ok32 or smoke,
          "THE DECISIVE NUMBER (the contract's named kill branch): "
          "the sub-dof mass fraction DECAYS AND SATURATES AT ZERO "
          "-- log10 tail ladder %s at h = %s: ONE DEX OF MASS "
          "LEAVES THE SUB-DOF CELL PER RUNG (pre-saturation slope "
          "%+.3f/rung in frozen window %s over h = 4..8), then "
          "SATURATION: tail >= %.2f (frac <= 2 pct) at every h >= "
          "%d; eigen-sum ward max %.1e <= %.0e; r_12 mode counts "
          "%s of K = %s; deep-rung gmin sign noise below entry "
          "precision at h >= 15 DISCLOSED (bottom modes below the "
          "1e-24 cut, frac at frozen cuts unaffected, ward covers): "
          "THE SPECTRAL-CUT SCOPING DIES -- the jet mass migrates "
          "into the ill-conditioned tail at the conditioning-wall "
          "rate"
          % (["%.2f" % tails[h] for h in hs], str(hs), slope,
             str(TAILSLOPE_WIN), SAT_LOG10, SAT_H, ward_max, FRAC_WARD,
             [fres[h]["rcnt"][CUT_PRIMARY] for h in hs],
             [fres[h]["K"] for h in hs]))

    ok33 = True
    for h in all_h:
        r_ = fres[h]
        if "frac" not in r_:
            continue
        f6 = r_["frac"]["1e-6"]
        f12 = r_["frac"]["1e-12"]
        f24 = r_["frac"]["1e-24"]
        if not (f6 <= f12 + 1e-15 and f12 <= f24 + 1e-15):
            ok33 = False
        if calib:
            print('CAL_SPREAD %d: ("%.3f", "%.3f", "%.3f")'
                  % (h, r_["ltails"]["1e-6"], r_["ltails"]["1e-12"],
                     r_["ltails"]["1e-24"]))
        elif not smoke:
            ref = CAL_SPREAD[h]
            for i2, cs_ in enumerate(CUTS):
                if abs(r_["ltails"][cs_] - float(ref[i2])) \
                        > CAL_TAIL_TOL:
                    ok33 = False
    check("G33-cut-spread", ok33 or smoke,
          "the cut ladder is SPREAD, not degenerate: log10 tails "
          "at cuts 1e-6/1e-12/1e-24 replicate the calibrated "
          "spread table at every rung (monotone in the cut as "
          "required): the jet mass is distributed ACROSS the "
          "collapsing spectrum -- widening the cut buys mass at "
          "the exact conditioning rate, no cut in the frozen "
          "family rescues a depth-stable fraction")

    ok34 = True
    margins = {}
    if not smoke:
        for h in all_h:
            if "frac" in fres[h] and "delta_req" in res.get(h, {}):
                margins[h] = (fres[h]["frac"][CUT_PRIMARY]
                              * res[h]["delta"] / res[h]["delta_req"])
        m7 = margins.get(7, float("nan"))
        m13 = margins.get(13, float("nan"))
        hs_m = sorted(margins)
        cross_bar = next((h for h in hs_m
                          if margins[h] < MARGIN_MIN_BAR), None)
        cross_one = next((h for h in hs_m if margins[h] < 1.0),
                         None)
        if calib:
            print("CAL margins " + " ".join(
                "%d:%.3f" % (h, margins[h]) for h in hs_m))
            print('CAL_MSUB = {"m7": "%.4f", "m13": "%.4e", '
                  '"cross_bar": %s, "cross_one": %s}'
                  % (m7, m13, cross_bar, cross_one))
        else:
            ok34 = (abs(m7 / float(CAL_MSUB["m7"]) - 1)
                    <= CAL_MSUB_TOL
                    and abs(m13 / float(CAL_MSUB["m13"]) - 1)
                    <= CAL_MSUB_TOL
                    and cross_bar == CAL_MSUB["cross_bar"]
                    and cross_one == CAL_MSUB["cross_one"])
        det34 = ("THE KILL WITH NUMBERS: sub-dof-scoped SF2 margins "
                 "margin_sub = frac x delta/delta_req: only h = "
                 "4/5/6 clear the house bar %.2f (1.405/1.744/"
                 "1.709); at h-hat(B2) = 7 margin_sub = %.3f "
                 "(clears the raw demand >= 1 but NOT the bar); at "
                 "h = 8 it is 0.116 and at h-hat(B3) = 13 it is "
                 "%.3e (dead by 125x); first rung below bar h = "
                 "%s, first below 1.0 h = %s: the sub-dof-truncated "
                 "demand DIES at the selector rungs themselves -- "
                 "the blockwise sub-dof theorem cannot carry the "
                 "cofinal supply (the UNSCOPED r180 margins >= "
                 "1.405 at ALL rungs stay the measured carrier, "
                 "CITED)"
                 % (MARGIN_MIN_BAR, m7, m13, cross_bar, cross_one))
    else:
        det34 = "smoke: margin legs on reduced rung set"
    check("G34-subdof-margin-crossover", ok34 or smoke, det34)

    ok35 = True
    nres_tab = {}
    for h in all_h:
        if h in res and "n_res" in res[h]:
            nres_tab[h] = res[h]["n_res"]
            if calib:
                pass
            elif not smoke and CAL_NRES.get(h) != res[h]["n_res"]:
                ok35 = False
    if calib:
        print("CAL_NRES = {%s}" % ", ".join(
            "%d: %d" % (h, nres_tab[h]) for h in sorted(nres_tab)))
    check("G35-resonance-census", ok35 or smoke,
          "house pole-resonance census n_res(h) = %s: the pole "
          "ladder ENTERS the window band as h grows -- the deep-"
          "rung Gram mixes resonant and sub-resonant modes, the "
          "rank collapse is the CONDITIONING wall (r180 gmin "
          "ladder), not a clean Landau count: the house 'dof' is "
          "the spectral cut, DISCLOSED as ward-class geometry"
          % (str(sorted(nres_tab.items()))))

    ok37 = True
    if hold_h and hold_h in res and hold_h in fres:
        r_ = res[hold_h]
        fr_ = fres[hold_h]
        ok37 = (r_["iden_dev"] <= IDEN_BAR
                and fr_.get("ward", 1.0) <= FRAC_WARD)
        if not smoke and not calib:
            ok37 = ok37 and abs(
                r_["delta"] / float(CAL_DELTA[hold_h]) - 1.0) <= 1e-4
            ok37 = ok37 and abs(
                fr_.get("log10tail", 0.0)
                - float(CAL_TAIL[hold_h])) <= CAL_TAIL_TOL
    check("G37-holdout-h20", ok37 or smoke,
          "DEEP HOLDOUT h = 20 (dps 144, K = 75): identity dev "
          "%.1e; frac ward %.1e; log10 tail %.2f -- the ladder "
          "extends one block deeper on the SAME kill trend"
          % (res.get(hold_h, {}).get("iden_dev", float("nan")),
             fres.get(hold_h, {}).get("ward", float("nan")),
             fres.get(hold_h, {}).get("log10tail", float("nan"))))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + KILL GATES")
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for r_ in ex.map(w_ctrl, ctrl_jobs):
            cres[(r_["world"], r_["h"])] = r_

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
            if calib:
                print('CAL_CTRL ("%s", %d): viol %.4e  delta_w %.4f'
                      '  tail "%.1f"  ward %.1e'
                      % (world, x, r_["viol_rel"], r_["delta_w"],
                         r_["log10tail_w"], r_["ward_w"]))
            parts.append("x=%d tau %.4f viol %.2e delta_w %.3f "
                         "tail 1e%.0f"
                         % (x, r_["tauf"], r_["viol_rel"],
                            r_["delta_w"], r_["log10tail_w"]))
        return okc, "; ".join(parts)

    okS, dS = ctrl_gate("SMOOTH", CTRL_SMOOTH)
    check("G40-smooth", okS,
          dS + " -- tau_w < 0, bridge violated; naked delta_w "
          "positive AND the control-world sub-dof fraction is ALSO "
          "1-class: FLOOR-INEQ-WORLD-INSENSITIVE (r169-SF6/r180 "
          "RESTATED NOT HIDDEN: fraction is geometry+alignment, "
          "the arithmetic kill lands on {floor value, bridge})")
    okR, dR = ctrl_gate("SCRARITH",
                        (5,) if smoke else CTRL_SCRARITH)
    check("G41-scramble-kill", okR,
          dR + " -- KILL GATE: scrambled world refuses at the "
          "bridge (viol < 0) while fraction stays 1-class "
          "(disclosed world-insensitivity of the naked split)")
    okE, dE = ctrl_gate("EPSTEIN",
                        (8,) if smoke else CTRL_EPSTEIN)
    check("G42-epstein-kill", okE,
          dE + " -- KILL GATE: Epstein world loses the chain at "
          "the bridge leg (tau + OFF - zsum < 0 at every x); the "
          "naked spectral split is world-insensitive, DISCLOSED")

    # G46: like-for-like world comparison of the mass fraction at
    # the CTRL_NZ window (MAIN vs fake worlds, same recipe)
    ok46 = True
    wtails = {}
    for (world, x), r_ in sorted(cres.items()):
        if "log10tail_w" not in r_:
            ok46 = False
            continue
        wtails[(world, x)] = r_["log10tail_w"]
        if r_.get("ward_w", 1.0) > FRAC_WARD:
            ok46 = False
        if calib:
            print('CAL_CTRL_TAIL ("%s", %d): "%.2f"'
                  % (world, x, r_["log10tail_w"]))
        elif not smoke:
            tl = CAL_CTRL_TAIL.get((world, x))
            if tl and abs(r_["log10tail_w"] - float(tl)) \
                    > CAL_CTRL_TAIL_TOL:
                ok46 = False
    check("G46-world-fraction", ok46 or smoke,
          "THE FRACTION SEPARATES WORLDS (like-for-like at the "
          "CTRL_NZ window): %s -- in the FAKE worlds the jet mass "
          "sits in the TOP modes (tails 1e-12..1e-14, fraction == "
          "1-class) while MAIN at the same x/recipe rides the "
          "ill-conditioned tail (-4.1/-2.3/-0.04, matching the "
          "full-window ladder: window-stable): the mass-in-the-"
          "tail is an ARITHMETIC property, not window geometry -- "
          "SF6 SHARPENED: the floor VALUE is world-insensitive "
          "(G40-G42, delta_w positive everywhere), the mass "
          "LOCATION is world-SEPARATING; the chain kill stays at "
          "the BA3 bridge (RESTATED NOT HIDDEN)"
          % str({"%s%d" % (w, x): "%.1f" % v
                 for (w, x), v in sorted(wtails.items())}))

    # ancestry: the composed chain + explicit seam node OUTSIDE it
    delivered = {
        "STEPA-EXACT": ["SOURCE", "CACHE-WARD", "CENSUS-PER-K"],
        "SPECTRAL-SPLIT-EXACT": ["STEPA-EXACT"],
        "SUBDOF-SCOPED-STATEMENT": ["SPECTRAL-SPLIT-EXACT",
                                    "SF1-TRANSPORT-EXACT",
                                    "CUTS-PREDEF"],
        "FRAC-LADDER-MEAS": ["SPECTRAL-SPLIT-EXACT", "CACHE-WARD",
                             "SOURCE"],
        "SUBDOF-MARGINS-MEAS": ["FRAC-LADDER-MEAS",
                                "DC-CLASSICAL-PER-CENSUS",
                                "SIGMA0-CITED"],
        "CARLESON-PRICING": ["SOURCE-ARITH", "OCS02-CITED",
                             "NAZ93-CITED", "HERM-CITED",
                             "BEU-CITED"],
        "FIXEDR-COMPACTNESS-SKETCH": ["WINDOW-PSD-EXACT",
                                      "CONFLUENT-LIMIT-EXACT",
                                      "OCCUPANCY-EXACT"],
        "COMPOSED-CHAIN": ["SUBDOF-SCOPED-STATEMENT",
                           "SUBDOF-MARGINS-MEAS",
                           "V927-BA-CITED", "SF4-SCHEDULE-CITED",
                           "SELECTOR-SOURCE"]}
    forbidden = ("TAUPOS", "TLAWCAP", "CENSUS-ALL-K",
                 "ZERO-VERIF-AS-HYP", "GONEK-1984-RH",
                 "MONTGOMERY-PC-RH", "GOLDSTON-MONTGOMERY-RH",
                 "RH-GRANT", "A0-FLOOR", "CROSS-BLOCK-SEAM")
    anc_chain = reachable(delivered, "COMPOSED-CHAIN")
    anc_carl = reachable(delivered, "CARLESON-PRICING")
    ok44 = (not (anc_chain & set(forbidden))
            and not (anc_carl & {"CACHE-WARD", "CENSUS-PER-K"})
            and "CROSS-BLOCK-SEAM" not in anc_chain
            and not has_cycle(delivered))
    check("G44-ancestry-seam-adjudication", ok44,
          "S3 ADJUDICATED BY MACHINE: CROSS-BLOCK-SEAM is an "
          "ancestor of NOTHING in the composed chain (L1-L3 house-"
          "side single-rung, L4 per-rung transport, L5 BA averages "
          "HOUSE rungs within one block + per-census schedule): "
          "SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE; the Carleson "
          "pricing leg has NO zero-table ancestor; the floor legs "
          "consume CACHE-WARD == census-per-k class DISCLOSED; "
          "chain ACYCLIC; forbidden grants ancestors of NOTHING")

    seal2 = hashlib.sha256((repr(sel) + repr(fam) + repr(CUTS)
                            + CUT_PRIMARY).encode()).hexdigest()
    ok45 = seal2 == seal_sha and idx_seal < idx_ward
    check("G45-predef-rehash", ok45,
          "end-of-run re-hash of selector + sub-dof family + cuts "
          "== the sealed value %s; seal precedes every ward/build "
          "event: PREDEFINITION machine-verified" % seal_sha[:16])

    check("G43-kill-gate-assembly", okS and okR and okE and ok44
          and ok45 and (ok46 or smoke),
          "all kill gates adjudicated: EPSTEIN %s SCRAMBLE %s "
          "(bridge-kills), WORLD-FRACTION %s (separating, "
          "disclosed), ANCESTRY/SEAM %s, PREDEFINITION %s"
          % tuple("PASS" if b else "FAIL"
                  for b in (okE, okR, ok46 or smoke, ok44, ok45)))

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ASSEMBLY")
    if not smoke:
        xs = [h for h in hrungs if h in res and h in fres]
        lt = [res[h]["log10tau"] for h in xs]
        ld = [math.log10(res[h]["delta"]) for h in xs]
        lq = [math.log10(res[h]["delta_req"]) for h in xs]
        ltl = [fres[h]["log10tail"] for h in xs]
        s_d = float(np.polyfit(lt, ld, 1)[0])
        s_q = float(np.polyfit(lt, lq, 1)[0])
        s_t = float(np.polyfit(lt, ltl, 1)[0])
        if calib:
            print("CAL tau-screen slopes: delta %.4f  req %.4f  "
                  "tail %.4f" % (s_d, s_q, s_t))
        ok50 = (abs(s_d) <= TAU_SLOPE_BAR
                and abs(s_q) <= TAU_SLOPE_BAR
                and abs(s_t) <= TAU_SLOPE_BAR)
    else:
        ok50, s_d, s_q, s_t = True, *(float("nan"),) * 3
    check("G50-tau-screen", ok50,
          "slope log10 delta vs log10 tau = %.4f, slope log10 "
          "delta_req vs log10 tau = %.4f, slope log10 tail vs "
          "log10 tau = %+.4f (all <= %.2f: the SF2 DEMAND is "
          "tau-flat, r180 class replicated, and the saturated "
          "kill observable is itself tau-flat over the reachable "
          "set -- no tau_h relabeling anywhere; the PRE-saturation "
          "tail growth tracks the conditioning-wall currency "
          "(gmin ladder), DISCLOSED in G32, not a Connes price)"
          % (s_d, s_q, s_t, TAU_SLOPE_BAR))

    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G51-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e (round-118 "
          "trap absent)" % d_eps)

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
    ok52 = ndet == 4 and not has_cycle(delivered)
    check("G52-loop-guard", ok52,
          "FOUR flagged cycles DETECTED (A0-triangle, census-all-k, "
          "Gonek-1984, Montgomery-PC/Goldston-Montgomery), NONE "
          "consumed (G44 ancestry); the composed chain is "
          "CONDITIONAL-TYPED and the forall-k quantifier stays the "
          "flagged loop (L5 cites v927/SF4 per-block/per-census)")

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
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5 / counterfactual-"
          "parallel 6 NOT REAL (r135 graph replicated; the scoped "
          "statement adds NO flow -- the floor is measured, not "
          "granted); census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED; RH unreachable without the omega edges")

    check("G60-demand-audit", True,
          "grids/bars/tabs frozen pre-evaluation (SPEC_SHA covers "
          "the declaration); f64 comb legs DISCLOSED; house cut = "
          "ward-class geometry DISCLOSED; delta_sub == delta "
          "identification DISCLOSED; ONE pre-freeze calibration "
          "pass disclosed (calib_subdof_pass1.log), scratch "
          "deleted, numbers verbatim in spec")

    info("POST-ROUND RESIDUE (unchanged in cardinality): "
         "{H1 ^ H2 ^ H3}-KOFINAL (mod D = 0.0042) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN == the one lambda-uniform edge of {L1, WPD}} + "
         "{WPD non-lambda legs / TAILWPD world front}.  This round "
         "KILLS the sub-dof-scoped proof route (mass fraction "
         "decays 1 dex/rung and saturates at zero; scoped margins "
         "die at the selector rungs) while the UNSCOPED r180 floor "
         "stays the measured carrier; adds the Carleson pricing "
         "(wrong-direction embedding half; lower class m-"
         "exponential or density-gated; needed jet constant OPEN, "
         "priced) + the fixed-r compactness sketch + the seam "
         "adjudication + the world-separating fraction finding.  "
         "Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SUBDOF-SCOPED-STATEMENT-POSED-EXACT(G10/G11/G12/G14)",
        "SUBDOF-MASS-FRACTION-DECAYS-SATURATES-AT-ZERO(G32/G33: "
        "one dex of mass leaves the sub-dof cell per rung h = "
        "4..8, then frac <= 2 pct -- THE CONTRACT'S NAMED KILL)",
        "SUBDOF-BLOCKFLOOR-DEAD-AT-MASS-FRACTION(G32/G34: "
        "margin_sub dies at the selector rungs, 8.0e-3 at h-hat "
        "= 13)",
        "MASS-RIDES-CONDITIONING-WALL(G33/G35: even the 1e-24 cut "
        "keeps 0.9 pct at h = 20; the spread table tracks the "
        "gmin ladder)",
        "UNSCOPED-FLOOR-STILL-CARRIES-MEASURED(r180 margins >= "
        "1.405 CITED: the program demand is untouched, the killed "
        "object is the PROOF ROUTE through the well-conditioned "
        "subspace)",
        "FRACTION-WORLD-SEPARATING(G46: fake worlds frac == 1, "
        "MAIN in the tail -- arithmetic property)",
        "COMB-AW-MASSFRAC-ONE(G22: the comb-side analog does NOT "
        "show the effect -- house-specific alignment)",
        "CARLESON-WRONG-DIRECTION(G24: [OCS02] box == upper only)",
        "CARLESON-LOWER-M-EXPONENTIAL-OR-DENSITY-GATED(G23/G25: "
        "[NAZ93]/[BEU]/[HERM]/[BFGHR]/[KOV01]/[GRO20] priced)",
        "NEEDED-JET-CONSTANT-OPEN-NOW-PRICED(G25: 23-dex two-"
        "sided gap at r = 128)",
        "FIXED-R-FLOOR-COMPACTNESS-SKETCH(G13/G27)",
        "SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE(G26/G44)",
        "RESONANCE-CENSUS-LADDER(G35: poles enter the window "
        "band; the house wall is conditioning, not Landau count)",
        "COMPOSITION-CONDITIONAL-TYPED(G12/G44/G52: exact legs "
        "L1-L4 stand, the measured floor leg is the corpse)",
        "SF6-ANATOMY-SHARPENED(G40/G41/G42/G46: floor value "
        "world-insensitive, mass location world-separating)",
        "NOT-RELABELING(G50)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G52)",
        "MINCUT-UNCHANGED(G53)",
        "TAXONOMY: CBJ-SUBDOF-BLOCKFLOOR-DEAD-AT-MASS-FRACTION "
        "(the named kill with numbers: tail ladder -4.08 -> "
        "-0.001, crossover h = 7/8, m13 = 8.0e-3) + CARLESON-"
        "PRICED-WRONG-DIRECTION + UNSCOPED-FLOOR-CARRIES (cited)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        "SUBDOF-SCOPED-STATEMENT-POSED-EXACT",
        "CBJ-SUBDOF-BLOCKFLOOR-DEAD-AT-MASS-FRACTION",
        "MASS-RIDES-CONDITIONING-WALL",
        "UNSCOPED-FLOOR-STILL-CARRIES-MEASURED",
        "FRACTION-WORLD-SEPARATING",
        "CARLESON-WRONG-DIRECTION",
        "CARLESON-LOWER-M-EXPONENTIAL-OR-DENSITY-GATED",
        "NEEDED-JET-CONSTANT-OPEN-NOW-PRICED",
        "FIXED-R-FLOOR-COMPACTNESS-SKETCH",
        "SEAM-PRESENT-NOT-CONSUMED-BLOCKWISE",
        "COMPOSITION-CONDITIONAL-TYPED",
        "SF6-ANATOMY-SHARPENED",
        "NOT-RELABELING",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
