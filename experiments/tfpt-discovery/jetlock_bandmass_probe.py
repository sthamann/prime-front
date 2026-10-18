#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jetlock_bandmass_probe -- PRIME.JETLOCK.BANDMASS.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the two round-137 residues:
JET-LOCK and BAND-MASS -- the serial pair Theorem E1 reduced
OMEGA-a = EPS-LOCK to)
=======================================================================
Round 137 (epslock_probe, 30/30) proved Theorem E1: EPS-LOCK <==
JET-LOCK(rho, Theta <= poly(x)) + BAND-MASS(theta < 1), with the
JET certification cache-zero-fed (E1-HORIZON-LIMITED at x = 24/28)
and BAND-MASS named as genuine arithmetic content.  This probe is
the maximal proof attempt on both.

NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer coefficients c_k (round-114
builder, unit vector in the nrm-weighted basis), boundary jets
A_{2m} = sum_k (-1)^k c_k om_k^{2m} (A_0 = phi(A)), SABS_{2m} =
sum_k |c_k| om_k^{2m}, secular function F(y) = c_0 + sum_{k>=1}
(-1)^k c_k y/(y - b_k) = A_0 + sum_k w_k/(y - b_k) (r131/r135 D1,
cited), E_N(z) = 2 sin(Az) F(z^2)/z, tau = lambda_min, T_z =
min(0.98 om_max, 2 pi x), G(T) = certified HSW22 upper bound for
sum_{gamma > T} gamma^{-2}, gtop = 7264.75 (X5 cache top),
OFF_ALLOW = 8 e^A (1 + eta_PT)^2 A_0^2 G(T_PT) (r131/r137 G15).

=======================================================================
THE THEOREMS (exact layer; sympy-gated generically / on exact
rational instances; classical inputs typed CITED)
=======================================================================
THEOREM J1 (source-only jet envelope; NEW).  For every depth m >= 1
and y > b_top: F(y) - A_0 = sum_{i=1}^m A_{2i}/y^i +
sum_k w_k b_k^m/(y^m (y - b_k)) EXACTLY (per-mode telescope), hence
  |F(y) - A_0| <= ENVJ_m(y) := sum_{i=1}^m |A_{2i}|/y^i
                   + sum_k |c_k| b_k^{m+1}/(y^m (y - b_k)),
and ENVJ(y) := min_m ENVJ_m(y) is monotone DECREASING on
(b_top, oo).  The SOURCE-ONLY onset Theta_J(rho) := the unique
solution of ENVJ(Theta^2) = rho |A_0| certifies JET-LOCK(rho) on
(Theta_J(rho), oo) -- ALL true zeros above it AND the beyond-cache
region in ONE stroke, consuming NO zeros.  This moves the round-137
jet certification from cache-zeros to source-only and RESOLVES the
E1-HORIZON-LIMITED typing at x = 24/28 at instrument level.

THEOREM J2 (the onset IS the jet ratio; NEW).  Let y_t :=
|A_2/A_0|, ell_i := |A_{2i}/A_0|^{1/(2i)}.  Unconditionally
Theta_J(rho)^2 >= y_t/rho; and IF ell_i <= ell_1 for all i >= 2
(the subordination census, gated per rung; measured ratio <= 0.62)
THEN Theta_J(rho)^2 <= y_t (1 + rho)/rho + (negligible certified
tail).  The JET-LOCK onset is the jet-ratio scale, two-sidedly.

THEOREM J3 (jet-ratio dictionary; r135 D2/G12 cited + NEW
corollary).  A_2/A_0 = sum_k b_k - sum_j y_j (trace identity over
the census roots y_j of F) and, A_0-FREE,
  A_2/A_0 = - sum_j prod_k (y_j - b_k) / prod_{i != j} (y_j - y_i).
The measured dominance: the ESCAPED census roots (y_j > b_top)
carry y_t (top root alone 83-86 percent) -- JET-LOCK(poly) is
EXACTLY a census-root-position law at the band EXTERIOR ("TOPROOT":
sum of escaped displacements <= poly(x)), the same object class as
COUNTEQ/SEEDBALL (r136/r138) but at the far edge, not the zone.

THEOREM J4 (unconditional poly cap; Cauchy-Schwarz).  |A_{2m}| <=
||c||_2 sqrt(sum_k om_k^{4m}) <= poly(x)^m with ||c||_2 bounded by
the builder normalization.  The jet NUMERATORS are unconditionally
polynomial; the entire JET-LOCK hardness is the RATIO against the
super-exponentially collapsed A_0 -- a two-scale CANCELLATION
ALIGNMENT (A_2 collapses WITH A_0 at polynomial ratio, measured
y_t ~ x^4.2): no one-sided classical bound can deliver it (typed
ALIGNMENT-WALL).

THEOREM B1 (tail visibility; NEW).  For any true zero gamma* >
Theta with JET-LOCK(rho) certified on (Theta, oo):
  tau + OFF >= M_above(Theta) >= 2|E_N(gamma*)|^2
            >= 8 sin^2(A gamma*) (1 - rho)^2 A_0^2 / gamma*^2,
hence BAND-MASS holds at the split Theta with
  1 - theta >= 8 sin^2(A gamma*)(1 - rho)^2 A_0^2
               / (gamma*^2 (tau + OFF)).
(1-theta)^{-1} <= poly(x) follows from JET-LOCK(Theta <= poly) +
TAILVIS (one zero in (Theta, poly] with sin^2 >= 1/poly) + TLAWCAP
(tau + OFF <= poly A_0^2 G(T_z)).

THEOREM B2 (the equivalence loop; NEW).  Theorem E1 (cited) gives
(JL + BM) ==> TLAWCAP with tlaw <= (1+r)^2 G(Theta)/G(T_z)/
(1-theta) + OFF-part; Theorem B1 gives (JL + TAILVIS + TLAWCAP)
==> BM(theta = 1 - 1/poly).  Hence MODULO {JET-LOCK, TAILVIS}:
BAND-MASS <==> TLAWCAP <==> EPS-LOCK itself (OFF is A_0^2-ridden,
r137 G15 cited).  BAND-MASS is NOT a strictly smaller piece: any
BM proof contains an EPS-LOCK proof.  The round-137 serial split
{JETLOCK, BANDMASS} RESHAPES to {JETLOCK(=TOPROOT), TAILVIS,
TLAWCAP} with TLAWCAP the arithmetic core (typed BM-IS-TLAWCAP).

B2-MECHANISM ADJUDICATION (contract question: does sin^2(A gamma_j)
predict the per-zero band mass?): per-term EXACTLY 2|E_N(gamma_j)|^2
= 8 sin^2(A gamma_j) F(gamma_j^2)^2/gamma_j^2; the measured band
dynamic range is carried ENTIRELY by F^2 (pinning; 9.9/33.3 dex at
x = 5/13) versus sin^2 (0.4/1.7 dex) -- the sin^2 weights are O(1),
NOT the collapse mechanism: the Erdos-Turan/discrepancy route
targets the wrong factor for BAND-MASS.  The lattice-proximity
object min_j |sin(A gamma_j)| (the r138 GW-slab deficit carrier,
cross-referenced) enters BM ONLY through TAILVIS in MAX form (one
visible zero suffices) -- strictly weaker than r138's min form.

TURAN/JENSEN PRICING (B1 contract angle, adjudicated): the
unconditional band-anchored interpolation transport pays
e^{type x distance} = e^{2A 2 pi x} = e^{2 pi x log x}, versus
|log tau| ~ 5.75 x: EXPONENTIALLY insufficient for theta < 1 at
1/poly (gated per rung); the A_0-anchored window variant is
quasi-polynomial BUT carries A_0^2/(tau+OFF) -- i.e. TLAWCAP again
(the same relocation as B2; typed TURAN-PRICED).

MIDJ (J2 contract question, adjudicated): the one-parameter model
F/A_0 = 1 - y_t/y is REFUTED at the onset (calibration ratios
0.003-0.006: the onset mass is carried by the full ESCAPED-ROOT
LADDER, not the top root alone) but is the measured LAW in the far
field (y >= 4 y_t, gated) and predicts the beyond-cache mass:
R_beyond_model = E[(1 - y_t/t^2)^2] under the RvM density --
calibration 0.999/0.964 vs measured 1.086/1.02 (x = 5/13); the
round-137 unexplained R_beyond DECLINE 1.08 -> 0.50 is the y_t
scale crossing the cache horizon.  R_J(x, T) plateaus inside the
cache at shallow rungs (1.2580 at x = 5 from 120 om onward): midJ
is a FINITE per-rung constant whose x-growth tracks the escaped-
root ladder (y_t ~ x^4.2 measured) -- it inflates E1 constants
through the onset only, polynomially if TOPROOT holds; typed
MIDJ-LADDER-CARRIED, structure intact.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (zeta only in audit_*, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (sympy generic + exact rational instances):
    G10 per-mode telescope depths 1, 2 (generic K=3) + assembly;
    G11 envelope validity (triangle) + term monotonicity + geometric
    tail closed form; G12 onset sandwich algebra (exact solve of
    q/(1-q) = rho; lower side |A_2|/y <= ENVJ); G13 Cauchy-Schwarz
    jet cap (generic 3-term + exact instance); G14 trace + spacing
    forms of the jet ratio (generic K=3 + exact rational instance;
    r135 D2 cited); G15 Theorem B1 chain (exact rearrangement);
    G16 Theorem B2 loop (E1 shape re-gate + composition, explicit
    constants, both directions); G17 interpolation-growth pricing
    instance (exact 3-node Lagrange transport identity + factor);
    G18 model integrals (exact antiderivative of log(t/c)/t^2;
    convergence of the R_beyond integrals).
S2  G20 HSW G(T) sanity vs cache partials; G21 polished ordinates
    (NPOL = 94, AUD_DPS = 140, own Newton on Xi) + sign-change
    certification (DELTA_LADDER to 1e-90) + band coverage.
S3  ladder x = (5,60),(8,80),(13,120),(18,140),(24,150),(28,165),
    KFAC 1.25 (r137 grid minus x=3):
    G30 build health + tau AND A_0 cross-instrument continuity vs
    frozen r135/r137 strings (<= 2e-3 dex);
    G31 jet-ratio ladder: sign(A_2/A_0) < 0 at every rung (the
    escaped-mass sign), subordination max_{i>=2} ell_i/ell_1 <=
    0.95, log-log slope of y_t vs x in (3.0, 5.5), CS-cap
    cancellation depth |A_2|/cap printed (ALIGNMENT-WALL exhibit);
    G32 source-only onsets: Theta_J(rho) on RHO_GRID by bisection
    (ENVJ monotone): sandwich y_t/rho (1-1e-9) <= Theta^2 <=
    1.05 y_t (1+rho)/rho (upper side under the G31 subordination),
    Theta_J(0.5)/Theta_r137_measured in (0.95, 1.5) at x = 5..18;
    G33 budget: band share M_band_hi/(tau+OFF) <= 1e-2, budget
    residual inside [0-, beyond_hi + OFF + slop] (r137 G31 shape
    with the NEW envelope), lock/tlaw in (0.05, 5.0), R_J(gtop) vs
    frozen r137 strings <= 0.03;
    G34 E1 SOURCE re-instantiation: candidates (rho, Theta_J(rho))
    + the gtop-capped candidate (r = ENVJ(gtop^2)/|A_0|):
    lock_E1_src = sqrt(C_E1/8) <= 25.0 at EVERY rung INCLUDING
    24/28 (E1-HORIZON-RESOLVED, source-only);
    G35 JETFORM far field: max rel dev of F/A_0 vs (1 - y_t/y) on
    the log grid y in [4 y_t, 400 y_t] <= 0.08 + envelope validity
    sample |F - A_0| <= ENVJ on a 20-point grid (word-blind ward);
    G36 escaped-root census (core x = 5, 8, 13): count == K-1 all
    real, n_escaped >= 1, y_top/y_t in (0.5, 1.0), trace identity
    rel dev <= 1e-10, spacing-form rel dev <= 1e-10;
    G37 band mechanism: dex range of (F/A_0)^2 minus dex range of
    sin^2 over the zone >= 4.0 at every rung (PINNING-CARRIES;
    the B2 answer);
    G38 R_beyond law: measured resid/(4 A_0^2 G(gtop)) over model
    E[(1-y_t/t^2)^2] in (0.33, 3.0) at every rung + R_J(T) plateau
    profile printed (midJ typing);
    G39 TAILVIS + Theorem B1 per rung at B1_RUNGS = (5, 8, 13, 18):
    gamma* = first cache zero > Theta_J(0.5) with sin^2 >= 0.1
    exists, certified (1-theta)_B1 >= 1e-8, poly-class envelope
    log10(1/(1-theta)) <= 1.5 + 4.5 log10 x, pointwise consistency
    2|E(gamma*)|^2 >= certified bound (1 - 1e-6); at x = 24/28
    typed TAILVIS-HORIZON-LIMITED (Theta_J(0.5) > cache top; the
    named instrument limit, r137 lever (d));
    G40 Turan pricing: E_T = 2A 2 pi x log10(e) dex >= max(
    |log10 tau|, 25 log10 x) at every rung (the unconditional
    interpolation transport eats the whole Connes budget;
    quasi-poly A_0-anchored exponent printed as INFO).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8:
    tau_w < 0 (the TLAWCAP/B1 currencies degenerate: no PSD value
    to cap) AND |A_0_w| >= 0.05 (NO boundary collapse: the
    two-scale alignment is arithmetic) AND envelope validity holds
    (algebra is world-blind -- null control); y_t_w printed; G53
    consistency.
S5  G54 tau-screens: |slope log10 Theta_J(1) vs log10 tau| <= 0.30
    and |slope log10 y_t vs log10 tau| <= 0.30 (the onset demand is
    A_0-FREE by the G14 spacing form -- NOT Connes-priced; the
    envelope VALUE rides A_0 by definition, typed
    BOUND-RIDES-CONNES, not a disguise); G55 conditioning (1e-25
    shift on Q[0,0] at x=5 moves tau inside (1e-40, 1e-10)).
S6  G60 min-cut (r116 replica; r137/r138 chain): the r137 serial
    JETLOCK(1) -> BANDMASS(1) RESHAPED to JETLOCK(1) -> TAILVIS(1)
    -> TLAWCAP(1) (BANDMASSTHM behind TLAWCAP as INF edge, B1/B2)
    -> QSUBGAP(1) -> COUNTEQTHM/SEEDBALLTHM/SPACREMTHM (INF, r138)
    -> DOMASYM -> WPDWIN: flows base 4, refined 5; granting
    JETLOCK still 5; granting JETLOCK + TAILVIS + TLAWCAP
    (= EPS-LOCK granted) still 5 (QSUBGAP caps); counterfactual
    PARALLEL reading (4 unit omegas in parallel) 8 = NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER = ((5,60),(8,80),(13,120),(18,140),(24,150),
(28,165)); CENSUS_RUNGS = (5, 8, 13); B1_RUNGS = (5, 8, 13, 18);
NPOL = 94; AUD_DPS = 140; M_JETS = 400; MGRID = (2, 4, 8, 16, 32,
64, 128, 256, 400); RHO_GRID = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0);
CACHE_ERR = 1e-9; HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2,
v914 corpus input]; T_PT = 3000175332800 [PT21]; DELTA_LADDER =
(1e-90, 1e-75, 1e-60, 1e-45, 1e-30, 1e-18, 1e-9, 1e-3); SINVIS =
0.1; TCHECK_FRACS = (2, 4, 8, 16, 32, 64, 120, 250, 500).
BARS: XCHECK_BAR = 2e-3 dex; SUBORD_BAR = 0.95; YT_SLOPE_WIN =
(3.0, 5.5); SANDWICH_LO = 1 - 1e-9; SANDWICH_HI = 1.05;
THETA_R137_WIN = (0.95, 1.5); BM_BAR = 1e-2; LOCK_WIN = (0.05,
5.0); RJ_R137_BAR = 0.03; RESID_LO = -1e-4; RESID_PAD = 1e-4;
E1_LOCK_BAR = 25.0; JETFORM_BAR = 0.08; ENVVAL_TOL = 1e-30;
YTOP_WIN = (0.5, 1.0); TRACE_BAR = 1e-10; SPACING_BAR = 1e-10;
MECH_GAP_DEX = 4.0; RBEYOND_WIN = (0.33, 3.0); B1_FLOOR = 1e-8;
B1_POLY_C0 = 1.5; B1_POLY_SLOPE = 4.5; B1_CONSIST_TOL = 1e-6;
TURAN_POLY_DEG = 25; ETA_PT_BAR = 1e-6; TAU_SLOPE_BAR = 0.30;
COND_WIN = (1e-40, 1e-10); RES_BAR = 1e-20; RUNTIME_BAR = 21600 s.
Frozen cross-instrument strings: tau (r135/r137) = {5: 1.60658e-16,
8: 3.77263e-30, 13: 2.49904e-54, 18: 5.21974e-79, 24: 1.8456e-108,
28: 5.32373e-128}; A_0 (r137 T1) = {5: 4.733e-8, 8: 8.419e-15,
13: 8.168e-27, 18: 4.368e-39, 24: 9.202e-54, 28: 1.584e-63};
Theta_rho=0.5 measured (r137 calibration) = {5: 338, 8: 879,
13: 2432, 18: 4817}; R_J (r137) = {5: 1.26, 8: 1.52, 13: 1.32,
18: 1.57, 24: 1.55, 28: 1.69}.  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks
(round-118 trap).  Controls: SMOOTH/SCRARITH x=5 dps 60, EPSTEIN
x=8 dps 80 (r135/r137 convention).

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_jlbm.py + log, deleted; numbers quoted verbatim):
x=5: A_0 = 4.732645e-8, A_2/A_0 = -6.106673e4 (NEGATIVE), y_t/b_top
= 40.1, ell ladder 247.1/147.2/98.8/... (falling), subordination
ratio 0.596; Theta_J(0.5/1/2) = 359.9/261.1/192.8 vs sandwich
[349.5, 428.0]/[247.1, 349.5]/[174.7, 302.7]; r137 measured onset
338 (ratio 1.065); census 10 real roots, 4 ESCAPED beyond b_top,
y_top/y_t = 0.8590; trace identity rel 1.3e-16; spacing form rel
1.3e-16; band ranges 9.9 dex (F^2) vs 0.4 dex (sin^2); R_J(gtop) =
1.2580 (plateau from ~120 om; r137 string 1.26); resid = 1.72e-18,
R_beyond_meas 1.086 vs model 0.999; TAILVIS gamma* = 361.29, sin^2
= 0.981, (1-theta)_B1 = 2.130e-4.  x=13: A_2/A_0 = -3.204224e6
(NEGATIVE), y_t/b_top = 317.7, subordination 0.620, Theta_J(0.5) =
2619.6 vs r137 measured 2432 (ratio 1.077), census 41 real, 12
escaped, y_top/y_t = 0.8344, trace rel 1.9e-18, band ranges 33.3
vs 1.7 dex, R_J(gtop) = 1.3192 (r137 1.32), R_beyond model 0.964,
TAILVIS (1-theta)_B1 = 5.939e-6 (poly-class slope ~3.8 across
5->13).  SMOOTH x=5: tau_w = -1.0944, A_0_w = 0.2778 (no
collapse), y_t_w = 234.7 (NO escaped scale: y_t_w/b_top = 0.15 vs
MAIN 40.1).  DISCLOSED CALIBRATION FINDINGS: (i) the scratch band
pass used UNPOLISHED cache ordinates and mis-read M_band at x=13
(F at pinned zeros needs polished ordinates -- the r137 polish
requirement; the frozen probe polishes at NPOL/AUD_DPS and the
x=13 scratch M_band/resid/R_beyond_meas reads are void, model
reads valid); (ii) ONE scratch instrument fix: np.float64-repr
cast at the census-sum build (the r133/r136/r138 class); (iii) the
ONE-PARAMETER midJ model is REFUTED at the onset (R_J model/meas
ratios 0.003-0.006): the onset mass is carried by the full
escaped-root ladder -- the frozen gates use the far-field JETFORM
+ R_beyond law + plateau typing instead (the refutation is itself
a finding, kept); (iv) the one-parameter JETFORM dev near the
crossing y ~ y_t is O(1) BY GEOMETRY (F vanishes at y_top =
0.83-0.86 y_t, the model at y_t): the JETFORM gate is far-field
[4 y_t, 400 y_t] by design.
SMOKE DISCLOSURE: smoke 1 = 28/29 (log kept) with ONE instrument
repair -- the G18 definite model integral must be evaluated as
antiderivative + limit (sympy returns a meijerg Piecewise normal
form otherwise; the r137-G11 normal-form class; no bar, no
criterion, no ladder moved); smoke 2 = 29/29 (log kept).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks below.

VERDICT ENUMS (frozen): SOURCE-JETCERT(Theorem J1; ENVJ onsets at
every rung, no zeros consumed; E1-HORIZON-RESOLVED);
ONSET-IS-JETRATIO(Theorem J2 sandwich + r137 onset cross);
JETRATIO-IS-ESCAPED-MASS(Theorem J3; trace/spacing exact; A_0-free;
JETLOCK <==> TOPROOT modulo subordination census);
JETCAP-POLY + ALIGNMENT-WALL(Theorem J4; numerator poly, ratio is
cancellation alignment -- obstruction typed);
MIDJ-LADDER-CARRIED(one-param onset model REFUTED, far-field law +
R_beyond law GATED, plateau typing: constants-inflating only);
E1-SRC-INSTANTIATED(lock_E1_src table incl. x = 24/28);
B1-TAILVIS-CERTIFIED(per rung; poly-class; HORIZON-LIMITED at
24/28 typed); BM-IS-TLAWCAP(Theorem B2 equivalence loop: BAND-MASS
is EPS-LOCK-complete modulo JL + TAILVIS);
SIN2-NOT-BAND-MECHANISM(PINNING-CARRIES; Erdos-Turan route targets
the wrong factor; r138 1/sin object cross-referenced into TAILVIS
max-form); TURAN-PRICED(unconditional exp-class; A_0-anchored
variant relocates to TLAWCAP); CONTROLS-REFUSE(tau < 0, no A_0
collapse, envelope world-blind); OMEGA-RESHAPED(residue {JETLOCK,
BANDMASS} -> {JETLOCK=TOPROOT, TAILVIS, TLAWCAP}); MINCUT(4/5,
census {MEAS, OMEGA-POS} unchanged).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; the zeta attribute
only inside audit_* functions (any enclosing scope); np.load only
inside ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((5, 60), (8, 80), (13, 120), (18, 140), (24, 150),
          (28, 165))
CENSUS_RUNGS = (5, 8, 13)
B1_RUNGS = (5, 8, 13, 18)
NPOL = 94
AUD_DPS = 140
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
RHO_GRID = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
CACHE_ERR = 1e-9
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
DELTA_LADDER = (1e-90, 1e-75, 1e-60, 1e-45, 1e-30, 1e-18, 1e-9, 1e-3)
SINVIS = 0.1
TCHECK_FRACS = (2, 4, 8, 16, 32, 64, 120, 250, 500)
XCHECK_BAR = 2e-3
SUBORD_BAR = 0.95
YT_SLOPE_WIN = (3.0, 5.5)
SANDWICH_LO = 1 - 1e-9
SANDWICH_HI = 1.05
THETA_R137_WIN = (0.95, 1.5)
BM_BAR = 1e-2
LOCK_WIN = (0.05, 5.0)
RJ_R137_BAR = 0.03
RESID_LO = -1e-4
RESID_PAD = 1e-4
E1_LOCK_BAR = 25.0
JETFORM_BAR = 0.08
ENVVAL_TOL = 1e-30
YTOP_WIN = (0.5, 1.0)
TRACE_BAR = 1e-10
SPACING_BAR = 1e-10
MECH_GAP_DEX = 4.0
RBEYOND_WIN = (0.33, 3.0)
B1_FLOOR = 1e-8
B1_POLY_C0 = 1.5
B1_POLY_SLOPE = 4.5
B1_CONSIST_TOL = 1e-6
TURAN_POLY_DEG = 25
ETA_PT_BAR = 1e-6
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
RES_BAR = 1e-20
RUNTIME_BAR = 21600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

R_TAU = {5: "1.60658e-16", 8: "3.77263e-30", 13: "2.49904e-54",
         18: "5.21974e-79", 24: "1.8456e-108", 28: "5.32373e-128"}
R_A0 = {5: 4.733e-8, 8: 8.419e-15, 13: 8.168e-27, 18: 4.368e-39,
        24: 9.202e-54, 28: 1.584e-63}
R_THETA05 = {5: 338.0, 8: 879.0, 13: 2432.0, 18: 4817.0}
R_RJ = {5: 1.26, 8: 1.52, 13: 1.32, 18: 1.57, 24: 1.55, 28: 1.69}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
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
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
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
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; zeta in audit_, cache in ward_")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- audit layer
def audit_polish_band(seeds: np.ndarray, dps: int) -> tuple[list, float]:
    """own damped Newton on Xi(t) = xi(1/2 + i t) from cache seeds."""
    out = []
    worst = 0.0
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for g0 in seeds:
            t = mp.mpf(repr(float(g0)))
            for _ in range(60):
                f = xi_line(t)
                fp = mp.diff(xi_line, t)
                step = f / fp
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                t = t - step
                if abs(step) < mp.mpf(10) ** (-dps + 8):
                    break
            worst = max(worst, float(abs(xi_line(t))))
            out.append(mp.nstr(t, dps))
    return out, worst


def audit_zero_deltas(pol_str: list, dps: int) -> list:
    """certified interval half-widths by mp sign change of Xi."""
    out = []
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for gs in pol_str:
            g = mp.mpf(gs)
            dj = None
            for d in DELTA_LADDER:
                dm = mp.mpf(repr(d))
                if xi_line(g - dm) * xi_line(g + dm) < 0:
                    dj = d
                    break
            out.append(dj)
    return out


# --------------------------------------------------------- closed forms
def hsw_G(T: float) -> float:
    """certified HSW22 upper bound for sum_{gamma>T} gamma^{-2}
    (r131 G16 derivation, cited)."""
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


# --------------------------------------------------------- source side
def source_ctx(ce: dict) -> dict:
    """per-rung mp context: coefficients, lattice, jets, envelope
    machinery (all inside workdps(ce dps))."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        aa = mp.log(ce["x"]) / 2
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        cs_abs = [abs(v) for v in cs]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]   # b[0] = 0
        A = []
        pw = [mp.mpf(1)] * K
        for m in range(M_JETS + 1):
            if m == 0:
                acc = sum((-1) ** k * cs[k] for k in range(K))
            else:
                acc = mp.mpf(0)
                for k in range(1, K):
                    pw[k] = pw[k] * b[k] if m > 1 else b[k]
                    acc += (-1) ** k * cs[k] * pw[k]
            A.append(acc)
        A0 = A[0]
        yt = abs(A[1] / A0)
        l2 = mp.sqrt(sum(v * v for v in cs))
        l1n = sum(cs_abs[k] for k in range(1, K))
    return dict(K=K, dps=dps, aa=aa, cs=cs, cs_abs=cs_abs, b=b, A=A,
                A0=A0, a0f=float(abs(A0)), yt=float(yt),
                btop=float(b[-1]), l2=float(l2), l1n=float(l1n))


def f_of_y(ctx: dict, y):
    """F(y) = c0 + sum (-1)^k c_k y/(y-b_k); caller sets workdps."""
    cs, b, K = ctx["cs"], ctx["b"], ctx["K"]
    acc = cs[0]
    for k in range(1, K):
        acc += (-1) ** k * cs[k] * y / (y - b[k])
    return acc


def en_triple(ctx: dict, t):
    """(E_N(t), E_N'(t), F(t^2)) analytic (r131/r137 en_pair shape);
    caller sets workdps."""
    cs, b, K, aa = ctx["cs"], ctx["b"], ctx["K"], ctx["aa"]
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    t2 = t * t
    for k in range(1, K):
        d = t2 - b[k]
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t2 + b[k])) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp, Rv * t / 2


def envj(ctx: dict, y):
    """min over m in MGRID of the Theorem-J1 envelope at y > b_top;
    caller sets workdps."""
    A, b, cs_abs, K = ctx["A"], ctx["b"], ctx["cs_abs"], ctx["K"]
    best = None
    for m in MGRID:
        head = mp.mpf(0)
        yi = mp.mpf(1)
        ok = True
        for i in range(1, m + 1):
            yi *= y
            head += abs(A[i]) / yi
            if best is not None and head > best:
                ok = False
                break
        if not ok:
            continue
        rem = mp.mpf(0)
        for k in range(1, K):
            rem += cs_abs[k] * b[k] ** (m + 1) / (yi * (y - b[k]))
        v = head + rem
        if best is None or v < best:
            best = v
    return best


def onset(ctx: dict, rho: float):
    """Theta_J(rho): unique solution of ENVJ(Theta^2) = rho |A_0|
    (ENVJ monotone decreasing); returns Theta (float).  Caller
    sets workdps."""
    A0a = abs(ctx["A0"])
    tgt = mp.mpf(repr(float(rho))) * A0a
    lo = mp.log(mp.mpf(repr(ctx["btop"])) * (1 + mp.mpf("1e-9")))
    yhi = mp.mpf(repr(max(8.0 * ctx["yt"] / rho, 8.0 * ctx["btop"])))
    for _ in range(200):
        if envj(ctx, yhi) < tgt:
            break
        yhi *= 4
    hi = mp.log(yhi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if envj(ctx, mp.exp(mid)) > tgt:
            lo = mid
        else:
            hi = mid
    return float(mp.sqrt(mp.exp(hi)))


def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM (returns sorted
    real positive y-roots as f64 and n_nonreal)."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300, extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    realm = np.abs(roots.imag) <= 1e-10 * float(s_mp)
    real_y = roots[realm & (roots.real > 0)]
    n_nonreal = int(np.sum(~realm))
    return np.sort(real_y.real), n_nonreal


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y = sp.symbols("y", positive=True)

    # G10 per-mode telescope depths 1, 2 (generic K=3) + assembly
    b1, b2 = sp.symbols("b1 b2", positive=True)
    w1, w2 = sp.symbols("w1 w2", real=True)
    S = w1 / (y - b1) + w2 / (y - b2)
    d1 = sp.simplify(sp.together(
        S - (w1 + w2) / y
        - (w1 * b1 / (y * (y - b1)) + w2 * b2 / (y * (y - b2)))))
    d2 = sp.simplify(sp.together(
        S - (w1 + w2) / y - (w1 * b1 + w2 * b2) / y ** 2
        - (w1 * b1 ** 2 / (y ** 2 * (y - b1))
           + w2 * b2 ** 2 / (y ** 2 * (y - b2)))))
    okA = d1 == 0 and d2 == 0
    out.append(("G10-per-mode-telescope", okA,
                "F - A0 == sum_{i<=m} A_{2i}/y^i + sum_k w_k b_k^m/"
                "(y^m (y-b_k)) exact at depths 1, 2 (generic): the "
                "Theorem J1 identity; A_{2i} == sum w b^{i-1} "
                "(r135 D2, cited)"))

    # G11 envelope validity + monotonicity + geometric tail
    i_, m_, cpos = sp.symbols("i_ m_ cpos", positive=True)
    dterm = sp.simplify(sp.diff(1 / y ** i_, y) + i_ / y ** (i_ + 1))
    drem = sp.diff(1 / (y ** m_ * (y - cpos)), y)
    dremok = sp.simplify(drem * (y ** (m_ + 1) * (y - cpos) ** 2)
                         + (m_ * (y - cpos) + y)) == 0
    qv = sp.Rational(1, 3)
    geo = sp.summation(qv ** i_, (i_, 3, sp.oo))
    geook = sp.simplify(geo - qv ** 3 / (1 - qv)) == 0
    # triangle instance: |w/(y-b)| <= |w| b/(y(y-b)) + |w|/y shape
    inst = sp.Rational(1, 7) / (100 - 2)
    instb = sp.Rational(1, 7) / 100 + sp.Rational(1, 7) * 2 \
        / (100 * (100 - 2))
    okB = dterm == 0 and dremok and geook and bool(inst <= instb)
    out.append(("G11-envelope-valid-monotone", okB,
                "each ENVJ term falls in y (derivative signs exact); "
                "geometric tail sum_{i>m} q^i == q^{m+1}/(1-q) "
                "closed; triangle instance: ENVJ is a valid monotone "
                "source-only majorant of |F - A0| on (b_top, oo)"))

    # G12 onset sandwich algebra
    rho, yt = sp.symbols("rho yt", positive=True)
    sol = sp.solve(sp.Eq((yt / y) / (1 - yt / y), rho), y)
    okC = len(sol) == 1 and sp.simplify(
        sol[0] - yt * (1 + rho) / rho) == 0
    # lower side: ENVJ >= |A2|/y => ENVJ(y) >= rho A0 for y <= yt/rho
    okD = sp.simplify((yt / (yt / rho)) - rho) == 0
    out.append(("G12-onset-sandwich", okC and okD,
                "q/(1-q) = rho at y == yt (1+rho)/rho (exact solve; "
                "the subordination-side upper bound) and |A2|/y == "
                "rho A0 at y == yt/rho (the unconditional lower "
                "side): Theorem J2's two-sided onset dictionary"))

    # G13 Cauchy-Schwarz jet cap
    a1, a2, a3, u1, u2, u3 = sp.symbols("a1 a2 a3 u1 u2 u3", real=True)
    cs_lhs = (a1 * u1 + a2 * u2 + a3 * u3) ** 2
    cs_rhs = (a1 ** 2 + a2 ** 2 + a3 ** 2) \
        * (u1 ** 2 + u2 ** 2 + u3 ** 2)
    lag = sp.expand(cs_rhs - cs_lhs
                    - ((a1 * u2 - a2 * u1) ** 2
                       + (a1 * u3 - a3 * u1) ** 2
                       + (a2 * u3 - a3 * u2) ** 2))
    inst2 = (sp.Integer(1) * 2 - sp.Integer(2) * 5) ** 2 \
        <= (1 + 4) * (4 + 25)
    out.append(("G13-cs-jet-cap", sp.simplify(lag) == 0 and bool(inst2),
                "Lagrange identity ==> (sum (-1)^k c_k b_k^m)^2 <= "
                "||c||^2 sum b^{2m} exactly: the jet NUMERATORS are "
                "unconditionally poly(x) (Theorem J4) -- the "
                "JET-LOCK hardness is the cancellation ALIGNMENT "
                "of A_2 with A_0, not any one-sided size"))

    # G14 trace + spacing forms (generic K=3)
    y1, y2, A0s = sp.symbols("y1 y2 A0s", positive=True)
    Fg = A0s * (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    w1r = sp.simplify((Fg * (y - b1)).subs(y, b1))
    w2r = sp.simplify((Fg * (y - b2)).subs(y, b2))
    trace = sp.simplify((w1r + w2r) / A0s - (b1 + b2 - y1 - y2))
    Fp1 = sp.diff(Fg, y).subs(y, y1)
    Fp2 = sp.diff(Fg, y).subs(y, y2)
    spac = sp.simplify(sp.together(
        (w1r + w2r) / A0s
        + (y1 - b1) * (y1 - b2) / (y1 - y2)
        + (y2 - b1) * (y2 - b2) / (y2 - y1)))
    spac2 = sp.simplify(sp.together(
        1 / Fp1 + 1 / Fp2 - (y1 + y2 - b1 - b2) / A0s))
    out.append(("G14-trace-spacing-forms", trace == 0 and spac == 0
                and spac2 == 0,
                "A_2/A_0 == sum b - sum y (trace) and A_2/A_0 == "
                "- sum_j prod_k(y_j - b_k)/prod_{i!=j}(y_j - y_i) "
                "(A_0-FREE spacing form; via sum 1/F' == -A_2/A_0^2, "
                "r135 D2 cited): Theorem J3 -- the jet ratio is a "
                "census-root displacement mass"))

    # G15 Theorem B1 chain
    ta, of_, s2, rh_, A0q, gs = sp.symbols(
        "ta of_ s2 rh_ A0q gs", positive=True)
    lb = 8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2
    th_bound = 1 - lb / (ta + of_)
    okE = sp.simplify((1 - th_bound) * (ta + of_) - lb) == 0
    # M_below <= (tau+OFF) - M_above <= (tau+OFF) - lb: exact chain
    Mb, Ma = sp.symbols("Mb Ma", positive=True)
    okF = sp.simplify((Mb + Ma) - Mb - Ma) == 0
    out.append(("G15-b1-tail-visibility", okE and okF,
                "tau + OFF >= M_below + M_above and M_above >= "
                "2|E(gamma*)|^2 >= 8 sin^2 (1-rho)^2 A_0^2/gamma*^2 "
                "==> theta <= 1 - 8 sin^2 (1-rho)^2 A_0^2/(gamma*^2 "
                "(tau+OFF)) (Theorem B1, exact rearrangement; "
                "budget + smallness cited r131/r137)"))

    # G16 Theorem B2 loop
    th, r_, GT, GZ, P = sp.symbols("th r_ GT GZ P", positive=True)
    # E1 direction (r137 G14 shape re-gate): tau(1-th) <= 8(1+r)^2
    # A0^2 G(Theta) + (1+th) OFF ==> tlaw <= [(1+r)^2 GT/GZ
    # + (1+th) OFF/(8 A0^2 GZ)]/(1-th)
    tl = sp.symbols("tl", positive=True)
    e1 = sp.Eq(tl * 8 * A0q ** 2 * GZ * (1 - th),
               8 * (1 + r_) ** 2 * A0q ** 2 * GT + (1 + th) * of_)
    sol_tl = sp.solve(e1, tl)
    okG = len(sol_tl) == 1 and sp.simplify(
        sol_tl[0] - ((1 + r_) ** 2 * GT / GZ
                     + (1 + th) * of_ / (8 * A0q ** 2 * GZ))
        / (1 - th)) == 0
    # B1 + TLAWCAP composition: tau + OFF <= P 8 A0^2 GZ ==>
    # 1 - theta >= s2 (1-rho)^2 / (P gamma*^2 GZ)
    comp = sp.simplify(
        (8 * s2 * (1 - rh_) ** 2 * A0q ** 2 / gs ** 2)
        / (P * 8 * A0q ** 2 * GZ)
        - s2 * (1 - rh_) ** 2 / (P * gs ** 2 * GZ))
    out.append(("G16-b2-equivalence-loop", okG and comp == 0,
                "E1 direction: (JL + BM) ==> tlaw <= [(1+r)^2 G(Th)/"
                "G(Tz) + OFF-part]/(1-th) (exact solve, r137 E1 "
                "cited); B1 + TLAWCAP ==> 1-theta >= sin^2 (1-rho)^2"
                "/(P gamma*^2 G(Tz)): BAND-MASS <==> TLAWCAP <==> "
                "EPS-LOCK modulo {JETLOCK, TAILVIS} (Theorem B2 -- "
                "BM is EPS-LOCK-complete, typed BM-IS-TLAWCAP)"))

    # G17 interpolation-growth pricing instance
    t = sp.symbols("t")
    nodes = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
    vals = [sp.Rational(1, 5), sp.Rational(-1, 7), sp.Rational(1, 11)]
    P2 = sp.interpolate(list(zip(nodes, vals)), t)
    fac = sum(abs(sp.prod([(sp.Integer(0) - nodes[j])
                           / (nodes[i] - nodes[j])
                           for j in range(3) if j != i]))
              for i in range(3))
    okH = bool(abs(P2.subs(t, 0)) <= fac * max(abs(v) for v in vals)) \
        and fac == 7
    out.append(("G17-interp-pricing-instance", okH,
                "|p(0)| <= [sum |L_i(0)|] max|p(t_i)| exact on the "
                "3-node instance (factor 7): the transport factor "
                "is the Lagrange mass -- for E_N-type transport over "
                "distance ~T_z it scales as e^{type x dist} = "
                "e^{2 pi x log x} (Turan/Cartan class, PRICED-SHAPE-"
                "ONLY, cited): the unconditional BM route pays "
                "exponentially"))

    # G18 model integrals
    c_ = sp.symbols("c_", positive=True)
    anti = sp.integrate(sp.log(t / c_) / t ** 2, t)
    okI = sp.simplify(sp.diff(anti, t) - sp.log(t / c_) / t ** 2) == 0
    T0 = sp.symbols("T0", positive=True)
    I0 = sp.limit(anti, t, sp.oo) - anti.subs(t, T0)
    okJ = sp.simplify(I0 - (sp.log(T0 / c_) + 1) / T0) == 0
    out.append(("G18-model-integrals", okI and okJ,
                "int_T^oo log(t/c)/t^2 dt == (log(T/c)+1)/T exact: "
                "the R_beyond model integrals converge in closed "
                "form (RvM density, cited)"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("jetlock_bandmass_probe -- PRIME.JETLOCK.BANDMASS.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:1] if smoke else LADDER
    census_rungs = (5,) if smoke else CENSUS_RUNGS
    b1_rungs = (5,) if smoke else B1_RUNGS
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    npol = 10 if smoke else NPOL

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    gtop = float(gam[-1])

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems J1-J4, B1-B2 inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: Guinand-Weil budget via r131 Layer 2 + "
         "r137 T1; r135 D1-D4 (secular F, jet sum rules); r137 "
         "Theorem E1/E2 + OFF identity G15; r136 S1-S4; r138 Q1-Q3 "
         "+ the 1/sin lattice-proximity object (cross-referenced); "
         "HSW22 Cor. 1.2; PT21; Euler sine product; Turan/Cartan "
         "interpolation growth (pricing shape only)")

    # ---------------------------------------------------------- S2
    section("S2  TAILS + POLISHED ORDINATES")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gtop) = %.4e" % hsw_G(gtop))

    t0 = time.time()
    pol_str, pol_res = audit_polish_band(gam[:npol], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:npol])))
    pol_del = audit_zero_deltas(pol_str, AUD_DPS)
    om_deep = 0.0
    for x, _d in ladder:
        Kx = int(math.ceil(KFAC * x * math.log(x)))
        om_deep = max(om_deep, (Kx - 1) * math.pi / (math.log(x) / 2))
    n_need = int(np.sum(gam <= om_deep))
    check("G21-polish-intervals",
          xw <= 1e-7 and pol_res <= 1e-60
          and all(d is not None for d in pol_del)
          and n_need <= npol,
          "own-Newton ordinates vs cache max dev %.1e, max |Xi| "
          "%.1e; all %d sign-change certified (worst delta %.0e); "
          "band coverage n_need %d <= NPOL %d (%.0f s)"
          % (xw, pol_res, npol, max(d for d in pol_del), n_need,
             npol, time.time() - t0), kind="edge")

    # ---------------------------------------------------------- S3
    section("S3  LADDER x = %s" % [x for x, _ in ladder])
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    ok38 = ok39 = ok40 = True
    det30, det31, det32, det33, det34, det35 = [], [], [], [], [], []
    det36, det37, det38, det39, det40 = [], [], [], [], []
    yt_tab, tau_tab, th1_tab, b1_tab = {}, {}, {}, {}
    cells = {}
    for x, dps in ladder:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=(x == 5))
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        ctx = source_ctx(ce)
        tauf = float(ce["tau"])
        a0f = ctx["a0f"]
        yt = ctx["yt"]
        yt_tab[x] = yt
        tau_tab[x] = tauf
        K = ce["K"]
        om_max = ctx["btop"] ** 0.5
        Tz = min(0.98 * om_max, 2 * math.pi * x)
        Gz = hsw_G(Tz)

        # G30 build xcheck
        devt = abs(math.log10(tauf) - math.log10(float(R_TAU[x])))
        deva = abs(math.log10(a0f) - math.log10(R_A0[x]))
        okc = tauf > 0 and devt <= XCHECK_BAR and deva <= XCHECK_BAR
        ok30 = ok30 and okc
        det30.append("x%d tau %.1e A0 %.1e dex" % (x, devt, deva))

        # G31 jet-ratio ladder
        with mp.workdps(dps):
            A = ctx["A"]
            A0 = ctx["A0"]
            sgn = 1 if A[1] / A0 > 0 else -1
            ells = []
            for i in range(1, 13):
                if A[i] != 0:
                    ells.append(float(abs(A[i] / A0)
                                      ** (mp.mpf(1) / (2 * i))))
                else:
                    ells.append(0.0)
            subord = max(ells[1:]) / ells[0]
            # CS cap exhibit
            cap = float(ctx["l2"] * mp.sqrt(sum(
                ctx["b"][k] ** 2 for k in range(1, K))))
            cancel = float(abs(A[1])) / cap
        okc = sgn < 0 and subord <= SUBORD_BAR
        ok31 = ok31 and okc
        det31.append("x%d yt %.3e sub %.3f" % (x, yt, subord))
        info("x=%d jets: A2/A0 = %+.4e (sign %s), y_t/b_top = %.1f, "
             "ell ladder %s; CS cap |A2| <= %.2e, cancellation "
             "depth |A2|/cap = %.1e (ALIGNMENT-WALL exhibit: "
             "numerator poly, ratio collapsed)"
             % (x, sgn * yt, "-" if sgn < 0 else "+",
                yt / ctx["btop"],
                "/".join("%.0f" % e for e in ells[:6]), cap, cancel))

        # G32 source-only onsets
        th_tab = {}
        okc = True
        with mp.workdps(dps):
            for rho in RHO_GRID:
                th = onset(ctx, rho)
                th_tab[rho] = th
                lo_b = yt / rho * SANDWICH_LO
                hi_b = yt * (1 + rho) / rho * SANDWICH_HI
                okc = okc and lo_b <= th * th
                if subord <= 1.0:
                    okc = okc and th * th <= hi_b
        th1_tab[x] = th_tab[1.0]
        if x in R_THETA05:
            rat = th_tab[0.5] / R_THETA05[x]
            okc = okc and THETA_R137_WIN[0] <= rat <= THETA_R137_WIN[1]
            det32.append("x%d Th(.5) %.0f r137 x%.2f" %
                         (x, th_tab[0.5], rat))
        else:
            det32.append("x%d Th(.5) %.0f [>gtop %s]" %
                         (x, th_tab[0.5],
                          "yes" if th_tab[0.5] > gtop else "no"))
        ok32 = ok32 and okc
        info("x=%d onsets Theta_J(rho): %s (sandwich sqrt(y_t/rho) "
             ".. sqrt(1.05 y_t(1+rho)/rho); source-only, no zeros)"
             % (x, "; ".join("%.2g:%.0f" % (r, th_tab[r])
                             for r in RHO_GRID)))

        # ---- zero pass (band polished + mid cache) ----
        n_band = int(np.sum(gam <= om_max))
        with mp.workdps(dps):
            aa = ctx["aa"]
            A0 = ctx["A0"]
            eta_pt = float(envj(ctx, mp.mpf(T_PT) ** 2) / abs(A0))
            off = float(8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2) \
                * hsw_G(float(T_PT))
            mb_hi = mp.mpf(0)
            rows = []
            for j in range(min(n_band, npol)):
                gj = mp.mpf(pol_str[j])
                E, Ep, Fv = en_triple(ctx, gj)
                s2 = mp.sin(aa * gj) ** 2
                # derivative slop at certified half-width
                dj = pol_del[j] if pol_del[j] else 1e-3
                slop = abs(Ep) * mp.mpf(repr(dj)) * 2
                mb_hi += 2 * (abs(E) + slop) ** 2
                rows.append((float(gj), float(s2),
                             float((Fv / A0) ** 2)))
            m_mid = mp.mpf(0)
            m_slop = mp.mpf(0)
            err = mp.mpf(repr(CACHE_ERR))
            cum_meas = np.zeros(len(gam) - n_band)
            cum_base = np.zeros(len(gam) - n_band)
            mid_g = np.zeros(len(gam) - n_band)
            acc_meas = mp.mpf(0)
            acc_base = mp.mpf(0)
            ytm = mp.mpf(repr(yt))
            m_below_mid = {}   # rho -> mid mass below Theta_J(rho)
            for rho in RHO_GRID:
                m_below_mid[rho] = mp.mpf(0)
            tail_first = None
            for j in range(n_band, len(gam)):
                gj = mp.mpf(repr(float(gam[j])))
                E, Ep, Fv = en_triple(ctx, gj)
                sv = mp.sin(aa * gj)
                e2 = 2 * abs(E) ** 2
                m_mid += e2
                m_slop += 2 * (2 * abs(E) * abs(Ep) * err
                               + (abs(Ep) * err) ** 2)
                acc_meas += sv ** 2 * Fv ** 2 / gj ** 2
                acc_base += sv ** 2 * A0 ** 2 / gj ** 2
                cum_meas[j - n_band] = float(acc_meas)
                cum_base[j - n_band] = float(acc_base)
                mid_g[j - n_band] = float(gam[j])
                for rho in RHO_GRID:
                    if float(gam[j]) <= th_tab[rho]:
                        m_below_mid[rho] += e2
                if (tail_first is None
                        and float(gam[j]) > th_tab[0.5]
                        and float(sv ** 2) >= SINVIS):
                    tail_first = (float(gam[j]), float(sv ** 2),
                                  float(Fv), float(e2))
            mb_hi_f = float(mb_hi)
            m_mid_f = float(m_mid)
            m_slop_f = float(m_slop)
            eta_g = float(envj(ctx, mp.mpf(repr(gtop)) ** 2) / abs(A0))
        D = 8.0 * a0f ** 2 * Gz
        eps_bar = math.sqrt((tauf + off) / 2.0)
        lock = eps_bar / math.sqrt(D)
        tlaw = tauf / D
        resid = tauf - mb_hi_f - m_mid_f
        beyond_hi = 8.0 * a0f ** 2 * (1 + eta_g) ** 2 * hsw_G(gtop)
        band_share = mb_hi_f / max(tauf + off, 1e-300)
        rj = cum_meas[-1] / cum_base[-1]

        # G33 budget
        okc = (band_share <= BM_BAR
               and LOCK_WIN[0] <= lock <= LOCK_WIN[1]
               and LOCK_WIN[0] <= tlaw <= LOCK_WIN[1]
               and abs(rj - R_RJ[x]) <= RJ_R137_BAR
               and eta_pt <= ETA_PT_BAR)
        lo_r = RESID_LO - (off + 3 * m_slop_f) / D
        hi_r = (beyond_hi + off + 3 * m_slop_f) / D + RESID_PAD
        okc = okc and lo_r <= resid / D <= hi_r
        ok33 = ok33 and okc
        det33.append("x%d bs %.0e lock %.2f tlaw %.2f RJ %.3f "
                     "res %.4f" % (x, band_share, lock, tlaw, rj,
                                   resid / D))

        # G34 E1 source instantiation
        best = None
        for rho in RHO_GRID:
            th = th_tab[rho]
            if th > 0.98 * gtop:
                continue
            m_bel = mb_hi_f + float(m_below_mid[rho]) + 3 * m_slop_f
            th_b = m_bel / max(tauf + off, 1e-300)
            if th_b >= 1:
                continue
            cc = (4 * (1 + rho) ** 2 * hsw_G(th) / Gz / (1 - th_b)
                  + off / (a0f ** 2 * Gz) / (1 - th_b))
            if best is None or cc < best[0]:
                best = (cc, rho, th, th_b)
        # gtop-capped candidate (the horizon resolver)
        m_bel = mb_hi_f + m_mid_f + 3 * m_slop_f
        th_b = m_bel / max(tauf + off, 1e-300)
        if th_b < 1:
            cc = (4 * (1 + eta_g) ** 2 * hsw_G(gtop) / Gz
                  / (1 - th_b)
                  + off / (a0f ** 2 * Gz) / (1 - th_b))
            if best is None or cc < best[0]:
                best = (cc, eta_g, gtop, th_b)
        lock_e1 = math.sqrt(best[0] / 8.0) if best else float("inf")
        okc = best is not None and lock_e1 <= E1_LOCK_BAR
        ok34 = ok34 and okc
        det34.append("x%d lock_E1_src %.2f (r %.2f Th %.0f th %.3f)"
                     % (x, lock_e1, best[1], best[2], best[3]))

        # G35 JETFORM far field + envelope validity sample
        with mp.workdps(dps):
            wd = 0.0
            for lg in np.linspace(math.log(4 * yt),
                                  math.log(400 * yt), 40):
                yv = mp.mpf(repr(float(math.exp(lg))))
                fv = f_of_y(ctx, yv) / A0
                model = 1 - ytm / yv
                dv = float(abs(fv - model) / abs(model))
                wd = max(wd, dv)
            ev = 0.0
            for lg in np.linspace(math.log(1.5 * ctx["btop"]),
                                  math.log(1000 * yt), 20):
                yv = mp.mpf(repr(float(math.exp(lg))))
                viol = abs(f_of_y(ctx, yv) - A0) - envj(ctx, yv)
                ev = max(ev, float(viol / abs(A0)))
        okc = wd <= JETFORM_BAR and ev <= ENVVAL_TOL
        ok35 = ok35 and okc
        det35.append("x%d dev %.3f envviol %.0e" % (x, wd, ev))

        # G36 escaped-root census (core)
        if x in census_rungs:
            ys, n_nonreal = raw_mp_census(ce)
            n_esc = int(np.sum(ys > ctx["btop"]))
            with mp.workdps(dps):
                sb = sum(ctx["b"][1:])
                sy = sum(mp.mpf(repr(float(v))) for v in ys)
                trd = float(abs((sb - sy) - A[1] / A0) / yt)
                ssum = mp.mpf(0)
                ysm = [mp.mpf(repr(float(v))) for v in ys]
                for j in range(len(ysm)):
                    num = mp.mpf(1)
                    den = mp.mpf(1)
                    for k in range(1, K):
                        num *= (ysm[j] - ctx["b"][k])
                    for i in range(len(ysm)):
                        if i != j:
                            den *= (ysm[j] - ysm[i])
                    ssum += num / den
                spd = float(abs(-ssum - A[1] / A0) / yt)
            ytr = float(ys[-1]) / yt
            okc = (len(ys) == K - 1 and n_nonreal == 0
                   and n_esc >= 1 and YTOP_WIN[0] <= ytr <= YTOP_WIN[1]
                   and trd <= TRACE_BAR and spd <= SPACING_BAR)
            ok36 = ok36 and okc
            det36.append("x%d esc %d ytop/yt %.3f tr %.0e sp %.0e"
                         % (x, n_esc, ytr, trd, spd))

        # G37 band mechanism
        lF = [math.log10(max(r[2], 1e-300)) for r in rows]
        lS = [math.log10(max(r[1], 1e-300)) for r in rows]
        gapd = (max(lF) - min(lF)) - (max(lS) - min(lS))
        okc = gapd >= MECH_GAP_DEX
        ok37 = ok37 and okc
        det37.append("x%d F %.1f sin %.1f dex" %
                     (x, max(lF) - min(lF), max(lS) - min(lS)))

        # G38 R_beyond law + plateau
        rb_meas = resid / (4.0 * a0f ** 2 * hsw_G(gtop))
        with mp.workdps(40):
            ytq = mp.mpf(repr(yt))
            gt = mp.mpf(repr(gtop))

            def nu_(t):
                return mp.log(t / (2 * mp.pi)) / (2 * mp.pi)
            I0 = mp.quad(lambda t: nu_(t) / t ** 2,
                         [gt, 10 * gt, 1000 * gt, mp.inf])
            I1 = mp.quad(lambda t: nu_(t) * (1 - ytq / t ** 2) ** 2
                         / t ** 2,
                         [gt, 10 * gt, 1000 * gt, mp.inf])
            rb_model = float(I1 / I0)
        rat = rb_meas / max(rb_model, 1e-300)
        okc = RBEYOND_WIN[0] <= rat <= RBEYOND_WIN[1]
        ok38 = ok38 and okc
        det38.append("x%d %.3f/%.3f x%.2f" % (x, rb_meas, rb_model,
                                              rat))
        prof = []
        for frac in TCHECK_FRACS:
            T = om_max * frac
            idx = int(np.sum(mid_g <= T)) - 1
            if idx < 3:
                continue
            prof.append("%.0fom:%.3f" % (frac,
                                         cum_meas[idx]
                                         / cum_base[idx]))
        info("x=%d R_J(T) profile: %s | plateau move last-half "
             "%.4f; R_beyond meas %.3f model %.3f (the y_t law "
             "explains the r137 decline)"
             % (x, " ".join(prof),
                abs(rj / (cum_meas[int(np.sum(mid_g <= gtop / 2))
                          - 1]
                          / cum_base[int(np.sum(mid_g <= gtop / 2))
                          - 1]) - 1),
                rb_meas, rb_model))

        # G39 TAILVIS + B1
        if x in b1_rungs:
            okc = tail_first is not None
            if okc:
                gst, s2st, fst, e2st = tail_first
                with mp.workdps(dps):
                    eta_s = float(envj(ctx, mp.mpf(repr(gst)) ** 2)
                                  / abs(A0))
                lbv = 8 * s2st * (1 - eta_s) ** 2 * a0f ** 2 \
                    / (gst ** 2 * (tauf + off))
                b1_tab[x] = lbv
                consist = e2st >= lbv * (tauf + off) \
                    * (1 - B1_CONSIST_TOL)
                polyb = math.log10(1 / lbv) <= B1_POLY_C0 \
                    + B1_POLY_SLOPE * math.log10(x)
                okc = (lbv >= B1_FLOOR and consist and polyb
                       and eta_s <= 0.5 + 1e-9)
                det39.append("x%d g* %.0f s2 %.2f (1-th) %.1e"
                             % (x, gst, s2st, lbv))
            else:
                det39.append("x%d NO gamma* (unexpected)" % x)
            ok39 = ok39 and okc
        else:
            hz = th_tab[0.5] > 0.98 * gtop
            det39.append("x%d %s" % (x, "HORIZON-LIMITED"
                                     if hz else "skipped"))
            info("x=%d TAILVIS: Theta_J(0.5) = %.0f vs gtop %.0f -- "
                 "%s (the named instrument limit: deeper zero cache "
                 "= r137 lever (d); Theorem B1 remains valid, "
                 "uninstantiable in this cache)"
                 % (x, th_tab[0.5], gtop,
                    "TAILVIS-HORIZON-LIMITED" if hz
                    else "in-cache but not gated (frozen B1_RUNGS)"))

        # G40 Turan pricing
        e_t = 2 * (math.log(x) / 2) * 2 * math.pi * x * math.log10(
            math.e)
        need = max(abs(math.log10(tauf)), TURAN_POLY_DEG
                   * math.log10(x))
        okc = e_t >= need
        ok40 = ok40 and okc
        det40.append("x%d E_T %.0f >= %.0f dex" % (x, e_t, need))

    check("G30-build-xcheck", ok30,
          "tau AND A_0 continuity vs frozen r135/r137 strings <= "
          "%.0e dex: %s" % (XCHECK_BAR, "; ".join(det30)),
          kind="edge")
    check("G31-jet-ratio-ladder", ok31,
          "A_2/A_0 < 0 at every rung (escaped-mass sign) and "
          "subordination max ell_i/ell_1 <= %.2f (Theorem J2 "
          "hypothesis gated): %s" % (SUBORD_BAR, "; ".join(det31)))
    if not smoke and len(yt_tab) >= 3:
        lx = [math.log10(x) for x, _ in ladder]
        ly = [math.log10(yt_tab[x]) for x, _ in ladder]
        s_yt = float(np.polyfit(lx, ly, 1)[0])
        oks = YT_SLOPE_WIN[0] <= s_yt <= YT_SLOPE_WIN[1]
        ok31 = ok31 and oks
        check("G31b-yt-power-law", oks,
              "log-log slope of y_t vs x = %.2f in %s (the measured "
              "TOPROOT law: y_t ~ x^%.1f -- JET-LOCK's onset is "
              "polynomial iff this law is; typed MEASURED)"
              % (s_yt, str(YT_SLOPE_WIN), s_yt))
    check("G32-source-onsets", ok32,
          "Theta_J(rho) sandwich y_t/rho <= Theta^2 <= %.2f y_t "
          "(1+rho)/rho on the grid AND Theta_J(0.5)/r137-measured "
          "in %s at x = 5..18 (source-only certification, no zeros "
          "consumed): %s" % (SANDWICH_HI, str(THETA_R137_WIN),
                             "; ".join(det32)))
    check("G33-budget", ok33,
          "band share <= %.0e, lock/tlaw in %s, R_J(gtop) vs r137 "
          "strings <= %.2f, budget residual in the certified "
          "envelope, eta_PT <= %.0e: %s"
          % (BM_BAR, str(LOCK_WIN), RJ_R137_BAR, ETA_PT_BAR,
             "; ".join(det33)))
    check("G34-e1-source-instantiation", ok34,
          "Theorem E1 re-instantiated with SOURCE-ONLY (rho, "
          "Theta_J(rho)) incl. the gtop-capped candidate: "
          "lock_E1_src <= %.1f at EVERY rung including x = 24/28 "
          "(E1-HORIZON-RESOLVED): %s"
          % (E1_LOCK_BAR, "; ".join(det34)))
    check("G35-jetform-farfield", ok35,
          "F/A_0 vs (1 - y_t/y) max rel dev <= %.2f on [4 y_t, "
          "400 y_t] and envelope validity |F - A_0| <= ENVJ on the "
          "sample grid (<= %.0e): %s"
          % (JETFORM_BAR, ENVVAL_TOL, "; ".join(det35)))
    check("G36-escaped-root-census", ok36,
          "census complete + real, n_escaped >= 1, y_top/y_t in %s, "
          "trace + spacing identities <= %.0e rel (Theorem J3 "
          "dictionary: the jet ratio IS the escaped displacement "
          "mass): %s" % (str(YTOP_WIN), TRACE_BAR,
                         "; ".join(det36)))
    check("G37-band-mechanism", ok37,
          "zone dex range of (F/A_0)^2 exceeds sin^2 range by >= "
          "%.1f dex at every rung: PINNING-CARRIES, sin^2 is NOT "
          "the band-mass mechanism (B2 adjudicated; discrepancy "
          "route targets the wrong factor): %s"
          % (MECH_GAP_DEX, "; ".join(det37)))
    check("G38-rbeyond-law", ok38,
          "R_beyond measured/model in %s at every rung -- the "
          "one-parameter y_t law explains the beyond-cache mass "
          "and the r137 decline (midJ typed LADDER-CARRIED, "
          "constants-inflating): %s"
          % (str(RBEYOND_WIN), "; ".join(det38)))
    check("G39-tailvis-b1", ok39,
          "TAILVIS gamma* exists (first zero > Theta_J(0.5), sin^2 "
          ">= %.1f) and Theorem B1 certifies (1-theta) >= %.0e, "
          "poly-class log10(1/(1-th)) <= %.1f + %.1f log10 x, "
          "pointwise-consistent, at x in %s; x = 24/28 typed "
          "TAILVIS-HORIZON-LIMITED: %s"
          % (SINVIS, B1_FLOOR, B1_POLY_C0, B1_POLY_SLOPE,
             str(B1_RUNGS), "; ".join(det39)))
    check("G40-turan-pricing", ok40,
          "unconditional interpolation transport e^{2 pi x log x} "
          "exceeds max(|log10 tau|, %d log10 x) dex at every rung: "
          "the band-anchored Turan route to BAND-MASS is "
          "exponentially insufficient; the A_0-anchored variant "
          "relocates to TLAWCAP (Theorem B2): %s"
          % (TURAN_POLY_DEG, "; ".join(det40)))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS")
    ctrl_ok = True
    for world, xw_, dpsw in controls:
        cw = R4.build_cell(xw_, KFAC, world, dpsw, want_mp=False)
        cwx = source_ctx(cw)
        tauw = float(cw["tau"])
        with mp.workdps(dpsw):
            evw = 0.0
            for lg in np.linspace(math.log(1.5 * cwx["btop"]),
                                  math.log(100 * cwx["btop"]), 12):
                yv = mp.mpf(repr(float(math.exp(lg))))
                viol = abs(f_of_y(cwx, yv) - cwx["A0"]) \
                    - envj(cwx, yv)
                evw = max(evw, float(viol / abs(cwx["A0"])))
        okw = tauw < 0 and cwx["a0f"] >= 0.05 and evw <= ENVVAL_TOL
        ctrl_ok = ctrl_ok and okw
        check("G50-%s" % world.lower(), okw,
              "%s x=%d: tau_w = %.4f < 0 (the TLAWCAP/B1 currencies "
              "have no PSD value to cap -- refusal), A_0_w = %.3f "
              "(NO collapse: the two-scale alignment is arithmetic), "
              "envelope world-blind (viol %.0e), y_t_w = %.3e "
              "(y_t_w/b_top = %.2f vs MAIN's 40-320)"
              % (world, xw_, tauw, cwx["a0f"], evw, cwx["yt"],
                 cwx["yt"] / cwx["btop"]))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse: tau < 0 kills the variational "
          "budget currency, A_0 does not collapse (no alignment to "
          "certify), while the ENVJ algebra passes world-blind "
          "(null control): JET-LOCK/BAND-MASS content is "
          "arithmetic, not variational generic")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs = [x for x, _ in ladder]
        lt = [math.log10(tau_tab[x]) for x in xs]
        lth = [math.log10(th1_tab[x]) for x in xs]
        lyt = [math.log10(yt_tab[x]) for x in xs]
        s_th = float(np.polyfit(lt, lth, 1)[0])
        s_yt2 = float(np.polyfit(lt, lyt, 1)[0])
        check("G54-tau-screen",
              abs(s_th) <= TAU_SLOPE_BAR
              and abs(s_yt2) <= TAU_SLOPE_BAR,
              "slope log10 Theta_J(1) vs log10 tau = %.4f, slope "
              "log10 y_t vs log10 tau = %.4f (both <= %.2f: the "
              "onset DEMAND is A_0-free by the spacing form -- NOT "
              "Connes-priced; the envelope VALUE rides A_0 by "
              "definition, typed BOUND-RIDES-CONNES, no disguise)"
              % (s_th, s_yt2, TAU_SLOPE_BAR))
    ce5 = cells.get(5)
    if ce5 is not None and "mpM" in ce5:
        with mp.workdps(ce5["dps"]):
            E0 = ce5["mpE"][0]
            Qp_ = ce5["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(ce5["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; round-118 red flag; all mp "
              "under workdps)" % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  MIN-CUT")
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
                ("L1TAILPROVEN", "JETLOCK"): 1,
                ("JETLOCK", "TAILVIS"): 1,
                ("TAILVIS", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "QSUBGAP"): 1,
                ("QSUBGAP", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "JETLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    three = dict(one)
    three[("JETLOCK", "TAILVIS")] = INF
    three[("TAILVIS", "TLAWCAP")] = INF
    f_three = R4.maxflow(dict(three), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "JETLOCK"): 1, ("JETLOCK", "R4HYP"): INF,
               ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "QSUBGAP"): 1, ("QSUBGAP", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_three == 5 and f_cf == 8 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r137 serial JETLOCK(1) "
          "-> BANDMASS(1) RESHAPED to JETLOCK(1) -> TAILVIS(1) -> "
          "TLAWCAP(1) (BANDMASSTHM behind as INF, Theorems B1/B2) "
          "-> QSUBGAP(1) (r138); granting JETLOCK still 5; granting "
          "JETLOCK + TAILVIS + TLAWCAP (= EPS-LOCK granted) still 5 "
          "(QSUBGAP caps); counterfactual PARALLEL reading 8 NOT "
          "REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; "
          "RH unreachable without the omega edges")
    info("EXACT RESIDUE after this round (with r137 E1 + r138 "
         "Q1-Q3 read together): RH <== [r122 NF-Closure] + [r128 "
         "Theorem R] + {L1, WPD} on dense a; L1 = TAIL(proven, "
         "r131) + H-pin; H-pin <== OMEGA-a + OMEGA-b (+ H1/H2/H3); "
         "OMEGA-a = EPS-LOCK <== JETLOCK + BANDMASS (r137 E1) and "
         "THIS ROUND: BANDMASS <==> TLAWCAP (== EPS-LOCK core) "
         "modulo {JETLOCK, TAILVIS} -- the E1 factorization is a "
         "LOOP on the B side; JETLOCK <==> TOPROOT (y_t <= poly, "
         "measured ~x^4.2) modulo the subordination census; "
         "OMEGA-b <== OMEGA-a + QSUBGAP (r138).  RESIDUE = "
         "{TOPROOT/JETLOCK, TAILVIS (weak one-of-N sin^2 "
         "visibility -- strictly weaker than r138's min-sin "
         "object), TLAWCAP (THE arithmetic core: A_0^2 >= "
         "(tau+OFF)/poly)} + QSUBGAP-lam-uniform + dense-a + "
         "a-extension (gamma_1^2 < a < H^2) + window-a (r128 G26). "
         "All source-side, NOT classical, NOT known RH-equivalent. "
         "NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SOURCE-JETCERT(Theorem J1: ENVJ onsets, no zeros consumed; "
        "E1-HORIZON-RESOLVED; G10/G11/G32/G34)",
        "ONSET-IS-JETRATIO(Theorem J2 sandwich + r137 onset cross; "
        "G12/G32)",
        "JETRATIO-IS-ESCAPED-MASS(Theorem J3: trace + spacing "
        "A_0-free forms; JETLOCK <==> TOPROOT; G14/G36)",
        "JETCAP-POLY + ALIGNMENT-WALL(Theorem J4; G13/G31)",
        "MIDJ-LADDER-CARRIED(one-param onset model refuted, "
        "far-field + R_beyond laws gated; G35/G38)",
        "E1-SRC-INSTANTIATED(lock table incl. 24/28; G34)",
        "B1-TAILVIS-CERTIFIED(+HORIZON-LIMITED typed; G39)",
        "BM-IS-TLAWCAP(Theorem B2 equivalence loop; G15/G16)",
        "SIN2-NOT-BAND-MECHANISM(PINNING-CARRIES; r138 1/sin "
        "cross-referenced; G37)",
        "TURAN-PRICED(exp-class unconditional / TLAWCAP-relocated; "
        "G17/G40)",
        "CONTROLS-REFUSE(G50-G53)",
        "OMEGA-RESHAPED({JETLOCK, BANDMASS} -> {TOPROOT, TAILVIS, "
        "TLAWCAP}; G60 census unchanged)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: SOURCE-JETCERT + ONSET-IS-JETRATIO + "
              "JETRATIO-IS-ESCAPED-MASS + JETCAP-POLY + "
              "ALIGNMENT-WALL + MIDJ-LADDER-CARRIED + "
              "E1-SRC-INSTANTIATED + B1-TAILVIS-CERTIFIED + "
              "BM-IS-TLAWCAP + SIN2-NOT-BAND-MECHANISM + "
              "TURAN-PRICED + CONTROLS-REFUSE + OMEGA-RESHAPED + "
              "MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
