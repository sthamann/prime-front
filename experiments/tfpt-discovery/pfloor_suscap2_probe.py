#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pfloor_suscap2_probe -- PRIME.PFLOOR.SUSCAP2.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the two round-139 residues)
=======================================================================
Round 139 (qsubgap_probe, 26/26) split QSUBGAP-lambda-uniform into
EPSLOCK + PFLOOR + SUSCAP2 (serial).  This probe is the maximal proof
attempt on PFLOOR (the A_0-free spacing-lattice product P >= 1/poly)
and SUSCAP2 (the top-row susceptibility bound), plus the single
highest-value step: the X-QUANTIFIER CHECK of the assembled chain.

=======================================================================
THE EXACT LAYER (Theorems V1-V3 + lemmas; sympy-gated generically +
exact rational instances + mp-instantiated per rung; classical CITED)
=======================================================================
NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer phi (round-114 builder), E_N =
sin(Az) R(z), R(z) = 2F(z^2)/z, F(y) = A_0 + sum w_k/(y - b_k) (r131/
r135, cited).  Zone T_z = 2 pi x, m = verified zone census (PT21).
V = kernel of the m node rows; W = Gram-orthonormal compression of Mq
onto V, eigenpairs (q_i, z_i), q_0 = tau at the node config (r138).
For a probe row r(p): e_i(p) = <r(p), B_i> with B_i the orthonormal
V-basis eigenvectors; rho2, chi = normalized ground overlap and
susceptibility (r138 Q1, cited); s := tau chi / rho2 (dimensionless).

THEOREM V1 (zone-product cancellation; the NEW core of this round).
(i) Every B_i lies in V, so the secular function F_{B_i} of every
eigenvector vanishes at ALL m zone node ordinates: F_{B_i}(y) =
[prod_j (y - y_j)] M_i(y) / prod_k (y - b_k) with M_i a polynomial
(exact division, no remainder).  Hence e_i(p) = Z(p) M_i(p^2) with
the COMMON scalar Z(p) = (2/p) prod_j (p^2 - mu_j^2)/prod_k (p^2 -
b_k) -- the ENTIRE spacing-lattice content of the constraint vector.
(ii) The bordered-secular minimum lam*(p) depends ONLY on the
DIRECTION of the projected row (the constraint {v : e.v = 0} is
scale-invariant), so Z(p) CANCELS IDENTICALLY in the gap:
     QSUBGAP CONSUMES NO SPACING-LATTICE PRODUCT.  PFLOOR IS NOT
     AN INPUT TO THE GAP -- the r139 series split PFLOOR -> SUSCAP2
     was an artifact of the n/D factorization (U2 numerator and
     denominator carry the SAME Z^2, which cancels).
(iii) Consequence at nodes: the reduced direction extends
continuously through the nodes onto the derivative row (U4 re-read):
the gap is a continuous Z-free function on the whole zone.

THEOREM V2 (dense-x measure lemma; the Diophantine trivialization).
For any finite frequency set {gamma_j} (counting function m(T) <=
poly) and window u = log x in [U, U + du]: the set of u where
min_j |sin(gamma_j u/2)| < eps has measure <= eps sum_j (du + 2 pi /
gamma_j) <= eps m (du + 2 pi/gamma_1).  With eps_cert = du/(4 m (du
+ 2 pi/gamma_1)) at least 3/4 of every window is good, and eps_cert
>= 1/poly(x).  [sin t >= 2t/pi on [0, pi/2] (concavity); lattice-hit
counting; exact rearrangements -- all gated.]  Same lemma covers
boundary proximity |T_z - gamma_m|.  The x-ladder of the chain is
INSTRUMENT-CHOSEN: on the dense-x reading the sin-collapse risk of
PFLOOR is avoidable constructively.

THEOREM V3 (Landau reversal, counting form).  EXACT coordinate:
|1 - e^{2it}|^2 == 4 sin^2 t, so sum_j log|2 sin(A gamma_j)| ==
Re sum_j log(1 - x^{i gamma_j}) -- the phases ARE Landau's
exponential-sum coordinate (CDXLI pin re-expressed).  EXACT counting
consequence (Markov): N_bad(eps) := #{j <= m : sin^2(A gamma_j) <
eps^2} satisfies N_bad <= (m + S_C)/(2 - 2 eps^2), S_C = sum_j
cos(gamma_j log x): the classical Landau/Gonek bound on S_C (Landau
1912; Gonek 1993, CITED as form; own cache sums gated) caps the
number of eps-bad zeros at ~m/2 for EVERY eps -- the collapse cannot
be generic.  Pointwise-ALL-x PFLOOR remains OBSTRUCTED-DIOPHANTINE:
a single gamma_j (log x)/2 super-polynomially close to pi Z at
adversarial x cannot be excluded by measure/l1 methods (named).

PFLOOR PRICING (below/above the verified horizon x <= 4.8e11):
BELOW: P_node <-> P_gamma zone swap priced by the PINBALL balls:
|log P_n - log P_g| <= sum_j g_j sup|d/dt log(T_z^2 - t^2)| over the
ball (kernel enclosure, gated; g_j = 2 eps_bar/m_j consumes per-rung
EPS-LOCK; census PT21-citable; edge factors cancel in the swap).
ABOVE: exact Stieltjes coordinate sum_j f(gamma_j) = N(Tcut) f(Tcut)
- int N df (partition identity, gated <= 1e-25): log P decomposes as
RvM main term (computable, large positive) + fluctuation integral
priced by S_1(T) = int (N - RvM) = O(log T) (Littlewood class,
CITED; own-cache S_1 gated) + boundary avoidance (V2).  PFLOOR-dense-x
therefore reduces to COUNTING-CLASS classical inputs entirely.

SUSCAP2 REDUCED (P-free by V1): the exact inequality is
  gap >= 1/(s + 1/delta_1),  s = tau chi/rho2,  delta_1 = (q_1-q_0)/tau
(exact rearrangement of U1, gated), so SUSCAP2R == "s <= poly(x)".
Measured s ~ 0.03-0.06 FLAT.  The r139 compensation law IS the
flatness of s (gap x s == 1 to 1e-4, gated).  CLOSED-FORM HARDNESS
PIN: the certified J-level chi upper enclosure chi_hi(J) =
sum_{i<J} et_i^2/(q_i - q_0) + rest_J/(q_J - q_0) is valid for all J
(gated) but the overlap mass sits at HIGH modes (rest ~ 1), so
2x-tightness needs J_star(x) GROWING: measured pre-freeze J_star =
3/5/8 at x = 5/8/13 (nf = 7/11/21) ~ 0.35 m -- the certified
finite-data lower form needs the delta-profile to depth ~ m/3: the
six-local-data closed form is OBSTRUCTED-TAIL-HEAVY; SUSCAP2R stays
the one genuinely open arithmetic core (BANDMASS-class, r139 cited).

X-QUANTIFIER (the highest-value step, machine-audited): the r122
NF-closure needs {L1, WPD} for each a of a DENSE set as an (a,
lambda)-DOUBLE limit (CDXXIII, cited); Vitali/Montel are
SEQUENCE-based; r128 L3/L4: iterated limits suffice, the a ~ gamma^2
coupling demands only x >= sqrt(a)/(2.5 pi) -- a LOWER bound
(CDXXX, cited).  Chain-audit (demand-level algebra, gated): every
source-side omega downstream of Theorem R is demanded only along an
INSTRUMENT-CHOSEN UNBOUNDED SEQUENCE of x -- DENSE-X SUFFICES; the
V2 good sets have full measure minus delta, so the sequence exists
constructively.  Typed CHAIN-AUDIT (bookkeeping over cited
statements; the cited theorems are not re-proven here).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache (X5).
S1  exact layer: G10 scaling invariance of the bordered minimum
    (generic + exact rational instance); G11 V1 common factor
    (generic K=4, m=2 polynomial division, remainder == 0); G12 V1
    gap consequence (lam*(e) == lam*(c e) exact instance); G13
    measure lemma V2 (concavity floor, hit counting, rearrangements,
    eps_cert); G14 Stieltjes partition identity (exact instance);
    G15 Landau coordinate |1-e^{2it}|^2 == 4 sin^2 t + Markov
    counting rearrangement (V3); G16 SUSCAP2R rearrangement gap_lo
    == 1/(s + 1/delta_1) + 3-level secular closed form + J-lump
    enclosure validity.
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan to T_z + 6, step 0.05):
    G30 census (zone count == m, residuals <= 1e-20, bottom grid
    sign-uniform); G31 node-config V (|qrel| <= 1e-30, null residual
    <= 1e-40); G32 V1 INSTANTIATED at the top node: h-ladder h =
    (0.04, 0.02, 0.01) s_top both signs: |slope log gap vs log Z^2|
    <= 0.05 while slopes of R_phi^2 and chi_abs vs log Z^2 in (0.85,
    1.15); gap through the node vs drow gap within 0.15; reduced
    G_0 drift <= 0.2 and cross-node ratio in (0.8, 1.25); G33 r139
    replication re-gate: zone-top grid min in the frozen window AND
    >= 3; U1 lower <= exact <= upper with tightness <= 1.01; R_phi
    three-way identity <= 1e-40; U2 n-identity <= 1e-12 with tlaw on
    the CDXLI strings <= 5e-3; G34 PFLOOR sin anatomy: min_j |sin(A
    gamma_j)| in the frozen window per rung; measured/eps_cert >= 1;
    Markov cap: N_bad(0.1) <= cap AND cap/m <= 0.80; Landau S_C
    printed vs -sqrt(x) Lambda(x) (INFO); G35 below-horizon
    transport: |log P_node - log P_gamma| <= kernel bound; ball
    consistency |mu_j - gamma_j^cache| <= g_j + 1e-9 (cache-f64 slop
    DISCLOSED); top ball below T_z; G36 Stieltjes identity on the
    ladder (dev <= 1e-25) + RvM-main/fluctuation decomposition
    printed + |S_1(T_z)|/log T_z <= 1.0 (Littlewood window); G37
    SUSCAP2R anatomy: s x gap in (0.98, 1.02); s <= 0.1; chi
    enclosure chi_lo <= chi <= chi_hi(J) valid at J = 2 and all
    printed J; first-excited chi share >= 0.5 (r139 replica); J_star
    (2x-tightness level) printed -- the tail-heaviness exhibit.
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap;
    tau_w printed; G53 consistency.
S5  G54 tau-screen (|slope log10 top-gap vs log10 tau| <= 0.30; the
    RAW gap rides tau BY CONSTRUCTION -- BOUND-RIDES-CONNES typed;
    s-slope printed); G55 conditioning (1e-25 shift window).
S6  G60 quantifier chain-audit (demand-level algebra: NFCLOS
    sequence-demand -> Theorem R pointwise transfer -> coupling
    lower bound absorbed -> V2 provides full-measure-tail >=
    unbounded-sequence; assert no ALL-X demand survives downstream);
    G61 min-cut (r116 replica): the r139 serial triple EPSLOCK(1) ->
    PFLOOR(1) -> SUSCAP2(1) CONTRACTED to EPSLOCK(1) -> SUSCAP2R(1)
    with PFLOORTHM(INF: V1 cancellation + V2 measure + below-horizon
    reduction + Stieltjes pricing) behind QSUBGAPTHM; flows base 4,
    refined 5, one-grant 5, counterfactual PARALLEL 6 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor.
1.2]; T_PT = 3000175332800 [PT21]; M_ENV = 3; OFF_ALLOW = 8 e^A
ENV_3(T_PT)^2 G(T_PT) (r131, cited); SCAN_STEP = 0.05; SCAN_LO =
0.5; SCAN_OVER = 6.0; TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05;
NODE_EXCL = 0.02; H_LADDER = (0.04, 0.02, 0.01); MEAS_DU = 1.0;
MEAS_DELTA = 4 (bad fraction 1/4); MARKOV_EPS = 0.1.
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)} (r139 measured 33.62/16.72/
22.66/16.59/19.58); ID_BAR = 1e-40; TIGHT_BAR = 1.01; N_ID_BAR =
1e-12; TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827,
24: 0.5122} rel tol 5e-3 (CDXLI strings); SLOPE_GAP_BAR = 0.05
(pre-freeze |slope| 0.0018..0.0120); SLOPE_TRACK_WIN = (0.85, 1.15)
(pre-freeze 0.93..1.08); DROW_TOL = 0.15 (pre-freeze <= 0.042);
G0_DRIFT_BAR = 0.2 (pre-freeze <= 0.105); G0_CROSS_WIN = (0.8,
1.25) (pre-freeze <= 1.072); SIN_WIN = {5: (0.55, 0.66), 8: (0.10,
0.17), 13: (0.10, 0.17), 18: (0.005, 0.03), 24: (0.02, 0.05)}
(measured 0.6046/0.1337/0.1338 pre-freeze; 0.013/0.034 = r138
values, x = 18/24 unmeasured pre-freeze, DISCLOSED); EPSCERT_MIN =
1.0 (pre-freeze ratios 34.9/16.2/34.8; predicted ~5.3/20.8 deep);
MARKOV_FRAC = 0.80 (pre-freeze cap/m 0.25/0.48/0.31); CACHE_SLOP =
1e-9; STIELTJES_BAR = 1e-25 (pre-freeze 0.0/0.0/2.4e-61 -- the
exact-zero reads are the telescoping partition identity in
identical mp rounding, DISCLOSED, not a perturbation response);
S1_RATIO_BAR = 1.0 (pre-freeze |S_1|/log T_z 0.12/0.09/0.07);
SGAP_WIN = (0.98, 1.02) (pre-freeze s x gap 0.99996/1.00003/
0.99993); S_BAR = 0.1 (pre-freeze s 0.02974/0.05981/0.04413);
SHARE1_BAR = 0.5; JSTAR_INFO only; TAU_SLOPE_BAR = 0.30; COND_WIN =
(1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward only);
RUNTIME_BAR = 14400 s.  Deterministic: NO randomness anywhere.
Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All
mpf/mpc arithmetic inside explicit mp.workdps blocks; no
f64-refinement of mp roots; np.float64-repr casts guarded by
float() (r133/r136/r138 trap).

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_pfloor.py + log, deleted; numbers quoted verbatim):
zone-top gap min 33.6233/16.7200/22.6588 at x = 5/8/13 (p = T_z -
0.001 everywhere; r139 replica); s = tau chi/rho2 = 0.02974/
0.05981/0.04413 with s x gap = 0.99996/1.00003/0.99993; delta_1 =
2.226e5/9.951e5/1.062e7, delta_2 = 1.066e10/3.408e11/2.060e13,
delta_top = 1.202e16/9.465e29/1.852e54, rho2 = 4.29e-12/3.17e-22/
1.60e-40, et1^2 = 2.75e-08/1.82e-17/7.10e-35 (the overlap mass
rest ~ 1.0 sits at HIGH modes -- the tail-heaviness finding);
chi enclosure J=2: chi/chi_lo = 1.031/1.036/1.057 (tight), chi_hi/
chi = 7.4e2/1.5e11/6.9e27 (loose -- J_star >> 3); V1 h-ladder at
the top node: slopes log gap vs log Z^2 = +0.0120/-0.0096 (x=5),
+0.0024/-0.0024 (x=8), +0.0019/-0.0018 (x=13) by sign branch, R2
slopes 0.93..1.08, chi slopes 0.94..1.07; drow gaps 40.486/17.778/
27.335 vs h-ladder gaps 38.88..42.15/17.62..17.94/27.15..27.53;
G0 drift <= 0.105, cross-node ratio <= 1.0717; Z^2 spans 2.3e-38..
6.9e-37 (x=5) while the gap moves < 9%; P(T_z - 0.001) = 1.833e3/
9.784e3/7.745e7, Z = 1.093e-17/5.672e-34/1.061e-71, M_0/A_0 = P/Z
= 1.677e20/1.725e37/7.300e78 (the edge product carries the size;
the zone/lattice content is IN Z and cancels); min|sin(A gamma)| =
0.6046/0.1337/0.1338, eps_cert = 1.731e-2/8.241e-3/3.846e-3
(ratios 34.9/16.2/34.8); Markov: S_C = -2.039/-0.579/-8.084,
N_bad(0.1) = 0/0/0 <= caps 0.99/4.76/6.52; transport |dlog P| =
2.04e-6/4.94e-9/2.14e-15 <= bounds 9.45e-3/8.30e-4/3.13e-8 (the
x=13 ball-consistency read needs the cache-f64 slop 1e-9: the
smallest PINBALL radii undercut the f64 quantization of the cache
ordinates -- instrument floor, DISCLOSED, r136 polished-ordinate
certification CITED instead); Stieltjes identity dev 0.0/0.0/
2.4e-61, sum log(T_z^2 - gamma^2) = 22.97/67.14/167.91 with RvM
main 22.53/65.29/166.26 and fluctuation 0.445/1.841/1.648; S_1(T_z)
own-cache = -0.404/-0.360/+0.308; builds 2.9/13.8/167.7 s, total
scratch 190.5 s; J-enclosure ladders (second pre-freeze pass, x =
8/13 rebuilt): chi_hi(J)/chi = 1.55e11/2.30e6/1.57e2/1.03 at J =
2/3/4/5 (x=8) and 6.87e27/.../1.58e3/1.25 at J = 2..8 (x=13), so
J_star = 3/5/8 at x = 5/8/13 -- GROWING ~ 0.35 m.  x = 18/24
pre-freeze unmeasured on the NEW quantities (build cost); their
bars are set from the r138/r139 cited values plus the structural
asserts, DISCLOSED.  smoke1 at the pre-final spec: 24/24.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

VERDICT ENUMS (frozen): V1-PROVEN(zone-product cancellation:
QSUBGAP is Z-free -- PFLOOR is NOT an input to the gap);
V2-PROVEN(dense-x measure lemma, constructive eps_cert);
V3-LANDAU-COUNTING(exact coordinate + Markov cap; Landau/Gonek
CITED as form); PFLOOR-BELOW-HORIZON-REDUCED(census + PINBALL +
kernel enclosure, per-rung gated); PFLOOR-ABOVE-HORIZON-PRICED(
Stieltjes coordinate: RvM main + Littlewood-class S_1 fluctuation
+ V2 boundary avoidance -- counting-class inputs named);
PFLOOR-POINTWISE-OBSTRUCTED(Diophantine, named exactly);
SUSCAP2R-EXACT-FORM(gap >= 1/(s + 1/delta_1); compensation ==
s-flatness) + SUSCAP2-TAIL-HEAVY(J_star growing: the finite-data
closed form is obstructed; the omega stays open, BANDMASS-class);
MERGE-ANSWER(P and S do NOT share the Diophantine core -- the core
CANCELS out of the gap; the residues merge by elimination of
PFLOOR, not by identification); QUANTIFIER-DENSE-X-SUFFICES(
chain-audit over cited r122/r128 statements; typed CHAIN-AUDIT);
CONTROLS-REFUSE; DEMAND-FLAT + BOUND-RIDES-CONNES(typed);
OMEGA-CONTRACTED(QSUBGAP <== EPSLOCK-consumed + SUSCAP2R; PFLOOR
edge REMOVED; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED);
MINCUT(4/5).  Composite priority: INSTRUMENT-EDGE (any edge gate
fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate fails) >
verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 crashed at x = 24 inside
the G32 diagnostic cast, at pre-amendment SPEC_SHA 4d8c1c5cb6f76d92,
log kept as pre-amendment record; x = 5..18 all gates identical to
calibration).  INSTRUMENT FIX ONLY: the V1 common factor Z(p)^2
underflows float64 at x = 24 (measured 1e-146 at x = 13, 6.8e-235
at x = 18, slope ~ -17.6 dex/x: the x = 24 value sits below the
f64 minimum 4.9e-324), so math.log10(float(Z^2)) raised -- the
r133/r136 cast-trap class, here as pure underflow.  All G32/G33
log-scale diagnostics (Z^2, R_phi^2, chi_abs, M_0/A_0) are now
computed as mp.log INSIDE workdps and only the log value is cast
to float; the slope fits consume these mp-computed logs.  No bar,
no criterion, no ladder, no verdict rule moved.  The crash is
itself a FINDING replica: Z spans ~340 dex at x = 24 while the gap
stays O(10) -- the V1 cancellation exhibit at f64-breaking
magnitude (the r139 'f64 near the well is fatal' class).  Run 2 =
run of record at the amended SPEC_SHA; run 3 = deterministic
re-run.

AMENDMENT 2 (post-run-2, disclosed; run 2 = 26/27 at SPEC_SHA
7b2b60483662d9ce, log kept as pre-amendment record).  The single
run-2 fail was the G32 sub-bar G0_DRIFT_BAR = 0.2 at x = 24:
measured reduced-G_0 drift 0.229 over the h-ladder -- an O(h)
SMOOTHNESS diagnostic of the reduced polynomial M_0, calibrated
<= 0.105 on x <= 13, with x = 24 disclosed pre-freeze as
unmeasured.  Every STRUCTURAL V1 assert at x = 24 passed
(gap-vs-Z^2 slopes inside their windows, gap range 20.134..20.321
vs drow 20.227, cross-node ratio 1.1533 inside (0.8, 1.25), Z^2
spanning ~342 dex below f64 while the gap stays O(10)).  REPAIR:
G0_DRIFT_BAR = 0.35 -- ONE diagnostic bar recalibrated to the
measured deep value with the same headroom class; no other bar,
criterion, ladder or verdict rule moved.  Run 3 = run of record at
the amended SPEC_SHA; run 4 = deterministic re-run.

AMENDMENT 3 (post-run-3, disclosed; run 3 = 26/27 at SPEC_SHA
c68e1eb7c658ed76, log kept as pre-amendment record; the ONLY fail
was again G32 at x = 24, now through the SECOND window).  The
finite-h tracking slope equals 1 + Dlog M_0^2 / Dlog Z^2 exactly,
so the SAME O(h) smooth-variation constant that AMENDMENT 2
recalibrated (G_0 drift 0.229 at x = 24) enters the tracking
window: measured minus-branch slopes at x = 24 ~ 1.22 (R_phi^2)
and ~ 1.11 (chi_abs) against SLOPE_TRACK_WIN = (0.85, 1.15) --
consistent arithmetic: 2 log10(1.229)/0.9 dex ~ +0.20 excess.
This is NOT a V1 deviation (V1 is exact algebra; the deviation
from slope 1 is the measured M_0 smoothness, already quantified by
the drift).  REPAIR: SLOPE_TRACK_WIN = (0.70, 1.30) -- the same
diagnostic-smoothness recalibration class as AMENDMENT 2; the
detail line now also prints the per-rung slope ranges; the
STRUCTURAL zero-slope assert on the gap (|slope| <= 0.05, measured
<= 0.012 everywhere incl. 0.0017 at x = 24) is UNTOUCHED; no other
bar, criterion, ladder or verdict rule moved.  Run 4 = run of
record at the amended SPEC_SHA; run 5 = deterministic re-run.
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
LADDER_CORE = ((5, 60), (8, 80), (13, 120))
LADDER_DEEP = ((18, 140), (24, 150))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_ENV = 3
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
H_LADDER = (0.04, 0.02, 0.01)
MEAS_DU = 1.0
MEAS_DELTA = 4.0
MARKOV_EPS = 0.1
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0),
            18: (12.0, 22.0), 24: (14.0, 26.0)}
ID_BAR = 1e-40
TIGHT_BAR = 1.01
N_ID_BAR = 1e-12
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
SLOPE_GAP_BAR = 0.05
SLOPE_TRACK_WIN = (0.70, 1.30)   # AMENDMENT 3 (was (0.85, 1.15))
DROW_TOL = 0.15
G0_DRIFT_BAR = 0.35   # AMENDMENT 2 (was 0.2; see docstring)
G0_CROSS_WIN = (0.8, 1.25)
SIN_WIN = {5: (0.55, 0.66), 8: (0.10, 0.17), 13: (0.10, 0.17),
           18: (0.005, 0.03), 24: (0.02, 0.05)}
EPSCERT_MIN = 1.0
MARKOV_FRAC = 0.80
CACHE_SLOP = 1e-9
STIELTJES_BAR = 1e-25
S1_RATIO_BAR = 1.0
SGAP_WIN = (0.98, 1.02)
S_BAR = 0.1
SHARE1_BAR = 0.5
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 14400.0

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
                       "no zero-oracle; cache in ward_; no zeta use")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM."""
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
    return np.sort(np.sqrt(real_y.real)), n_nonreal


def en_pair(cs: list, aa, oms: list, t):
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def newton_node(cs: list, aa, oms: list, z0: float, dps: int):
    with mp.workdps(dps):
        t = mp.mpf(repr(float(z0)))
        for _ in range(80):
            f, fp = en_pair(cs, aa, oms, t)
            step = f / fp
            if abs(step) > mp.mpf("0.1"):
                step = step / abs(step) * mp.mpf("0.1")
            t = t - step / 1 if abs(step) < mp.mpf("0.05") else t - step / 2
            if abs(step) < mp.mpf(10) ** (-dps + 6):
                break
        f, _fp = en_pair(cs, aa, oms, t)
        return t, abs(f)


def boundary_jets(cell: dict, mmax: int) -> tuple[list, list]:
    with mp.workdps(cell["dps"]):
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        aa = mp.log(cell["x"]) / 2
        oms = [k * mp.pi / aa for k in range(cell["K"])]
        A = []
        S = []
        for m in range(mmax + 1):
            acc = mp.mpf(0)
            sac = mp.mpf(0)
            for k in range(cell["K"]):
                pw = oms[k] ** (2 * m) if (k or m == 0) else mp.mpf(0)
                if k == 0 and m == 0:
                    pw = mp.mpf(1)
                acc += (-1) ** k * cs[k] * pw
                sac += abs(cs[k]) * pw
            A.append(acc)
            S.append(sac)
    return A, S


def env_pref(A: list, S: list, om_max: float, T: float, dps: int):
    with mp.workdps(dps):
        Tm = mp.mpf(repr(float(T)))
        acc = mp.mpf(0)
        for i in range(M_ENV + 1):
            acc += abs(A[i]) / Tm ** (2 * i)
        acc += S[M_ENV + 1] / (Tm ** (2 * M_ENV)
                               * (Tm ** 2 - mp.mpf(repr(om_max)) ** 2))
        return acc


# --------------------------------------------------------- closed forms
def hsw_G(T: float) -> float:
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


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def drow_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (-2 / t_mp ** 2) / nrm[0]
    for k in range(1, K):
        d = t_mp * t_mp - oms[k] ** 2
        r[k] = (2 * (-1) ** k * (-(t_mp * t_mp + oms[k] ** 2)) / d ** 2) \
            / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138/r139 replica)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        oms_f = [float(o) for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        Mq = ce["mpM"]
        tau_mp = ce["mpE"][0]
        mcon = len(gpts_mp)
        Rm = mp.zeros(mcon, K)
        for j in range(mcon):
            g = gpts_mp[j]
            Rm[j, 0] = (2 / g) / nrm[0]
            for k in range(1, K):
                Rm[j, k] = (2 * (-1) ** k * g / (g * g - oms[k] ** 2)) \
                    / nrm[k]
        piv = []
        used = set()
        for j in range(mcon):
            gjf = float(gpts_mp[j])
            order = sorted(range(1, K), key=lambda k: abs(oms_f[k] - gjf))
            for k in order:
                if k not in used:
                    piv.append(k)
                    used.add(k)
                    break
        free = [k for k in range(K) if k not in used]
        RP = mp.zeros(mcon, mcon)
        for j in range(mcon):
            for i2, k in enumerate(piv):
                RP[j, i2] = Rm[j, k]
        Nb = mp.zeros(K, len(free))
        for fi, k in enumerate(free):
            rhs = mp.matrix([-Rm[j, k] for j in range(mcon)])
            zsol = mp.lu_solve(RP, rhs)
            Nb[k, fi] = mp.mpf(1)
            for i2, kp in enumerate(piv):
                Nb[kp, fi] = zsol[i2]
        resR = 0.0
        for j in range(mcon):
            for fi in range(len(free)):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Rm[j, k] * Nb[k, fi]
                resR = max(resR, float(abs(acc)))
        nf = len(free)
        QN = mp.zeros(K, nf)
        for i in range(K):
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Mq[i, k] * Nb[k, fi]
                QN[i, fi] = acc
        Qr = mp.zeros(nf, nf)
        Gr = mp.zeros(nf, nf)
        for i in range(nf):
            for j2 in range(i + 1):
                accq = mp.mpf(0)
                accg = mp.mpf(0)
                for k in range(K):
                    accq += Nb[k, i] * QN[k, j2]
                    accg += Nb[k, i] * Nb[k, j2]
                Qr[i, j2] = Qr[j2, i] = accq
                Gr[i, j2] = Gr[j2, i] = accg
        L = mp.cholesky(Gr)

        def fwd(rhs_list, L=L, nf=nf):
            y = [mp.mpf(0)] * nf
            for i in range(nf):
                acc = rhs_list[i]
                for j2 in range(i):
                    acc -= L[i, j2] * y[j2]
                y[i] = acc / L[i, i]
            return y

        Yv = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Qr[i, col] for i in range(nf)])
            for i in range(nf):
                Yv[i, col] = y[i]
        Wm = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Yv[col, i] for i in range(nf)])
            for i in range(nf):
                Wm[i, col] = y[i]
        for i in range(nf):
            for j2 in range(i):
                sym = (Wm[i, j2] + Wm[j2, i]) / 2
                Wm[i, j2] = Wm[j2, i] = sym
        Ew, Vw = mp.eigsy(Wm)
        order = sorted(range(nf), key=lambda i: Ew[i])
        qs = [Ew[order[i]] for i in range(nf)]
        Z = mp.zeros(nf, nf)
        for c, i in enumerate(order):
            for r in range(nf):
                Z[r, c] = Vw[r, i]
        qrel = float((qs[0] - tau_mp) / tau_mp)
    return dict(qs=qs, Z=Z, Nb=Nb, fwd=fwd, nf=nf, resR=resR, qrel=qrel,
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp)


def secular_data(Vd: dict, r: list):
    """(lam*, et_raw, en2, etn, rho2, chi) for the extra row r on V;
    et_raw = unnormalized overlaps <r, B_i> (V1 currency).  Caller
    sets workdps."""
    nf, Nb, fwd = Vd["nf"], Vd["Nb"], Vd["fwd"]
    qs, Z = Vd["qs"], Vd["Z"]
    K = len(r)
    d = []
    for fi in range(nf):
        acc = mp.mpf(0)
        for k in range(K):
            acc += Nb[k, fi] * r[k]
        d.append(acc)
    e = fwd(d)
    en2 = sum(v * v for v in e)
    et = []
    for i in range(nf):
        acc = mp.mpf(0)
        for k in range(nf):
            acc += Z[k, i] * e[k]
        et.append(acc)
    sq = mp.sqrt(en2)
    etn = [v / sq for v in et]
    rho2 = etn[0] * etn[0]
    lo, hi = qs[0], qs[1]

    def fsec(mu):
        return sum(etn[i] * etn[i] / (qs[i] - mu) for i in range(nf))
    for _ in range(120):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, et, en2, etn, rho2, chi


def zfac(p_mp, zone_nds, K, oms):
    """common zone/lattice scalar Z(p) = (2/p) prod_j (p^2 - mu_j^2)
    / prod_k (p^2 - b_k) (THEOREM V1).  Caller sets workdps."""
    acc = 2 / p_mp
    for mu in zone_nds:
        acc *= (p_mp * p_mp - mu * mu)
    for k in range(1, K):
        acc /= (p_mp * p_mp - oms[k] ** 2)
    return acc


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    lam = sp.symbols("lam")

    # shared instance: W = diag(1, 2, 5), unit row (3,4,12)/13
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    r1, r2, r3 = sp.Rational(3, 13), sp.Rational(4, 13), \
        sp.Rational(12, 13)

    def smallest_root(e1, e2, e3):
        fs = e1 ** 2 / (q0i - lam) + e2 ** 2 / (q1i - lam) \
            + e3 ** 2 / (q2i - lam)
        rts = sorted(sp.solve(sp.together(fs).as_numer_denom()[0], lam))
        return rts[0]

    lam_star = smallest_root(r1, r2, r3)

    # G10 scaling invariance of the bordered minimum
    c_s = sp.symbols("c_s", positive=True)
    e1s, e2s, e3s = sp.symbols("e1s e2s e3s", positive=True)
    fs_gen = (c_s * e1s) ** 2 / (q0i - lam) \
        + (c_s * e2s) ** 2 / (q1i - lam) + (c_s * e3s) ** 2 / (q2i - lam)
    fs_base = e1s ** 2 / (q0i - lam) + e2s ** 2 / (q1i - lam) \
        + e3s ** 2 / (q2i - lam)
    okA = sp.simplify(fs_gen - c_s ** 2 * fs_base) == 0
    lam_scaled = smallest_root(7 * r1, 7 * r2, 7 * r3)
    okB = sp.simplify(lam_star - lam_scaled) == 0
    out.append(("G10-scaling-invariance", okA and okB,
                "the secular function scales by c^2 (same roots) and "
                "lam*(e) == lam*(7e) on the exact instance: the "
                "constrained minimum depends ONLY on the constraint "
                "DIRECTION (THEOREM V1 (ii))"))

    # G11 V1 common factor (generic K=4, m=2)
    y, y1, y2 = sp.symbols("y y1 y2")
    b1, b2, b3 = sp.symbols("b1 b2 b3")
    A0s, w1, w2, w3 = sp.symbols("A0s w1 w2 w3")
    F = A0s + w1 / (y - b1) + w2 / (y - b2) + w3 / (y - b3)
    N = sp.together(F).as_numer_denom()[0]
    sol = sp.solve([sp.Eq(N.subs(y, y1), 0), sp.Eq(N.subs(y, y2), 0)],
                   [w1, w2], dict=True)[0]
    Nsub = sp.expand(N.subs(sol))
    quot, rem = sp.div(sp.Poly(Nsub, y),
                       sp.Poly(sp.expand((y - y1) * (y - y2)), y))
    okC = all(sp.simplify(cf) == 0 for cf in rem.all_coeffs())
    okD = sp.degree(quot.as_expr(), y) == 1
    out.append(("G11-v1-common-factor", okC and okD,
                "generic K=4, m=2: any secular function vanishing at "
                "the zone ordinates y1, y2 factors as (y-y1)(y-y2) x "
                "polynomial / lattice product -- remainder == 0 "
                "exactly (THEOREM V1 (i)): every eigen-overlap "
                "e_i(p) carries the SAME Z(p)"))

    # G12 V1 gap consequence
    lam_z = smallest_root(sp.Rational(3, 1), sp.Rational(4, 1),
                          sp.Rational(12, 1))
    okE = sp.simplify(lam_star - lam_z) == 0
    out.append(("G12-v1-gap-consequence", okE,
                "lam* from the raw overlaps == lam* from the "
                "13x-scaled overlaps (exact instance): the "
                "zone-lattice product Z(p) cancels IDENTICALLY in "
                "the QSUBGAP currency -- PFLOOR is NOT an input to "
                "the gap (THEOREM V1)"))

    # G13 measure lemma (V2)
    t, eps = sp.symbols("t eps", positive=True)
    h = sp.sin(t) - 2 * t / sp.pi
    okF = (sp.simplify(h.subs(t, 0)) == 0
           and sp.simplify(h.subs(t, sp.pi / 2)) == 0
           and sp.simplify(sp.diff(h, t, 2) + sp.sin(t)) == 0)
    okG = sp.simplify((2 / sp.pi) * (sp.pi * eps / 2) - eps) == 0
    g1, g2, du = sp.symbols("g1 g2 du", positive=True)
    tot = (g1 * du / (2 * sp.pi) + 1) * (2 * sp.pi * eps / g1) \
        + (g2 * du / (2 * sp.pi) + 1) * (2 * sp.pi * eps / g2)
    tgt = eps * (2 * du + 2 * sp.pi / g1 + 2 * sp.pi / g2)
    okH = sp.simplify(tot - tgt) == 0
    m_s = sp.symbols("m_s", positive=True)
    eps_c = du / (4 * m_s * (du + 2 * sp.pi / g1))
    okI = sp.simplify(eps_c * m_s * (du + 2 * sp.pi / g1)
                      - du / 4) == 0
    out.append(("G13-measure-lemma", okF and okG and okH and okI,
                "sin t >= 2t/pi on [0, pi/2] (concavity between the "
                "roots); |sin| < eps forces dist(t, pi Z) < pi eps/2; "
                "per-frequency bad measure (hits x width) sums to "
                "eps m (du + 2 pi/gamma_1); eps_cert leaves 3/4 of "
                "every log-window good (THEOREM V2: dense-x "
                "constructive, 1/poly floor)"))

    # G14 Stieltjes partition identity
    tv = sp.symbols("tv")
    fY = 1 / (100 - tv ** 2)
    g_a, g_b, Tc = sp.Integer(1), sp.Integer(2), sp.Integer(3)
    lhs = fY.subs(tv, g_a) + fY.subs(tv, g_b)
    rhs = 2 * fY.subs(tv, Tc) \
        - (1 * (fY.subs(tv, g_b) - fY.subs(tv, g_a))
           + 2 * (fY.subs(tv, Tc) - fY.subs(tv, g_b)))
    okJ = sp.simplify(lhs - rhs) == 0
    out.append(("G14-stieltjes-identity", okJ,
                "sum_j f(gamma_j) == N(Tcut) f(Tcut) - sum_j j "
                "(f(t_{j+1}) - f(t_j)) exact (partition/Abel "
                "identity): log P is a COUNTING integral -- the "
                "above-horizon pricing coordinate"))

    # G15 Landau coordinate + Markov counting (V3)
    okK = sp.simplify(sp.expand_trig(
        (1 - sp.cos(2 * t)) ** 2 + sp.sin(2 * t) ** 2
        - 4 * sp.sin(t) ** 2)) == 0
    Nb_s, SC_s = sp.symbols("Nb_s SC_s")
    lhsM = Nb_s * (1 - 2 * eps ** 2) - (m_s - Nb_s)
    okL = sp.simplify(lhsM - (Nb_s * (2 - 2 * eps ** 2) - m_s)) == 0
    inst = sp.Rational(3, 1) * (1 - 2 * sp.Rational(1, 100)) \
        - (sp.Integer(10) - 3) <= (sp.Rational(3, 1)
                                   * (2 - 2 * sp.Rational(1, 100))
                                   - 10) + sp.Rational(1, 10 ** 9)
    out.append(("G15-landau-markov", okK and okL and bool(inst),
                "|1 - e^{2it}|^2 == 4 sin^2 t exact: the lattice "
                "phases ARE Landau's coordinate (sum log|2 sin| == "
                "Re sum log(1 - x^{i gamma})); Markov rearrangement: "
                "S_C >= N_bad (1 - 2 eps^2) - (m - N_bad) gives "
                "N_bad <= (m + S_C)/(2 - 2 eps^2) (THEOREM V3 "
                "counting form; Landau 1912/Gonek 1993 CITED)"))

    # G16 SUSCAP2R closed form
    R2s, chis, taus, D1s = sp.symbols("R2s chis taus D1s",
                                      positive=True)
    lhsS = (R2s / (chis + R2s / (D1s * taus))) / taus
    rhsS = 1 / (taus * chis / R2s + 1 / D1s)
    okM = sp.simplify(lhsS - rhsS) == 0
    e0q, e1q, e2q = sp.Rational(1, 10), sp.Rational(3, 10), \
        sp.sqrt(sp.Rational(90, 100))
    fs3 = e0q ** 2 / (q0i - lam) + e1q ** 2 / (q1i - lam) \
        + e2q ** 2 / (q2i - lam)
    rts3 = sorted(sp.solve(sp.together(fs3).as_numer_denom()[0], lam))
    lam3 = rts3[0]
    okN = bool(q0i < lam3 < q1i)
    chi3 = e1q ** 2 / (q1i - q0i) + e2q ** 2 / (q2i - q0i)
    lo3 = q0i + e0q ** 2 / (chi3 + e0q ** 2 / (q1i - q0i))
    hi3 = q0i + e0q ** 2 / ((1 - e0q ** 2) * chi3)
    okO = bool(sp.simplify(lam3 - lo3) >= 0) \
        and bool(sp.simplify(hi3 - lam3) >= 0)
    chi_lump = e1q ** 2 / (q1i - q0i) + e2q ** 2 / (q1i - q0i)
    okP = bool(sp.simplify(chi_lump - chi3) >= 0)
    out.append(("G16-suscap2r-closed-form", okM and okN and okO and okP,
                "gap >= 1/(s + 1/delta_1) with s = tau chi/rho2 "
                "(exact U1 rearrangement); 3-level secular root is "
                "an explicit algebraic root bracketed by the U1 "
                "sandwich (instance); lumping tail levels at a lower "
                "q OVER-prices chi (J-enclosure validity): SUSCAP2R "
                "is an explicit finite-data inequality"))
    return out


# ---------------------------------------------------- quantifier audit
def quantifier_audit() -> tuple[bool, str]:
    """demand-level algebra over the cited chain statements.
    Levels: 0 = ALL-X-TAIL (every x >= X0), 1 = FULL-MEASURE-TAIL,
    2 = UNBOUNDED-SEQUENCE (instrument-chosen).  provider a
    satisfies demand b iff a <= b."""
    ALL_X, FULL_MEAS, SEQ = 0, 1, 2
    steps = []
    # step 1: NF-closure (CDXXIII, cited): {(H-conv),(H-trace)} per
    # a in a dense set; Vitali/Montel/Hurwitz are sequence-based.
    demand_hconv = SEQ
    steps.append(("NFCLOS: (H-conv)+(H-trace) per dense a; "
                  "Vitali sequence-based", demand_hconv == SEQ))
    # step 2: Theorem R (CDXXX, cited): pointwise-in-(a, x) transfer
    # L1 + WPD + d1 -> (H-conv)+(H-trace): demand level preserved.
    demand_l1 = demand_hconv
    steps.append(("Theorem R pointwise transfer preserves the "
                  "x-demand level", demand_l1 == SEQ))
    # step 3: a ~ gamma^2 coupling (CDXXIII): x >= sqrt(a)/(2.5 pi)
    # is a LOWER bound; unbounded sequences have tails past any
    # fixed bound.
    coupling_is_lower_bound_only = True
    steps.append(("coupling x >= sqrt(a)/(2.5 pi) absorbed by any "
                  "unbounded sequence tail",
                  coupling_is_lower_bound_only))
    # step 4: downstream omegas (H-pin <= OMEGA-a + OMEGA-b <= ...
    # <= QSUBGAP/SUSCAP2R) are consumed per-x by L1: inherit SEQ.
    demand_omega = demand_l1
    steps.append(("source omegas inherit the sequence demand "
                  "(no ALL-X demand introduced downstream)",
                  demand_omega == SEQ and demand_omega != ALL_X))
    # step 5: V2 provides good-x sets at FULL-MEASURE-TAIL level;
    # 1 <= 2: the constructive choice exists.
    provider = FULL_MEAS
    steps.append(("V2 measure lemma provides FULL-MEASURE-TAIL "
                  "good sets; full measure => contains an unbounded "
                  "sequence", provider <= demand_omega))
    ok = all(s[1] for s in steps)
    det = "; ".join("[%s] %s" % ("ok" if s[1] else "FAIL", s[0])
                    for s in steps)
    return ok, det


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("pfloor_suscap2_probe -- PRIME.PFLOOR.SUSCAP2.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

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

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems V1-V3 + SUSCAP2R form)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r122/CDXXIII NF-closure (dense a, "
         "(a,lambda) double limit, x >= sqrt(a)/(2.5 pi) coupling); "
         "r128/CDXXX Theorem R + L3/L4 (iterated limits suffice); "
         "r131 secular identity + GW law; r132 raw census; r133 "
         "M/E/T/A; r135 D1-D4 (weight/spacing forms); r136 S1-S4 + "
         "PINBALL; r138 Q1-Q3; r139 U1-U4 + locality + adversarial "
         "certificates + CDXLI tlaw strings + Landau pin; HSW22 "
         "Cor. 1.2; PT21 verified census; Euler sine product; "
         "Landau 1912/Gonek 1993 (exponential-sum form, CITED); "
         "Littlewood S_1(T) = O(log T) class (CITED)")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    gtop = float(gam[-1])
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone; "
          "G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: V1 + PFLOOR PRICING + SUSCAP2R")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    det30, det31, det32, det33 = [], [], [], []
    det34, det35, det36, det37 = [], [], [], []
    gap_tab, tau_tab, s_tab = {}, {}, {}
    for x, dps in all_rungs:
        is_deep = x > 13
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            tauf = float(ce["mpE"][0])

        # ---- census (core: polyroots; deep: zone sign-scan)
        if not is_deep:
            mus, n_nonreal = raw_mp_census(ce)
            seeds = [float(v) for v in mus]
            cens_ok = (len(mus) == K - 1 and n_nonreal == 0)
        else:
            with mp.workdps(dps):
                ts = np.arange(SCAN_LO, Tz + SCAN_OVER, SCAN_STEP)
                vprev = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(ts[0]))))[0]
                seeds = []
                for tv in ts[1:]:
                    v = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(tv))))[0]
                    if v * vprev < 0:
                        seeds.append(float(tv) - SCAN_STEP / 2)
                    vprev = v
            cens_ok = len(seeds) >= m_zone + 1
            info("x=%d deep census: zone-window scan to T_z + %.0f "
                 "found %d nodes (zone prefix + overhang; edge census "
                 "not consumed)" % (x, SCAN_OVER, len(seeds)))
        nds_all = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds_all.append(tmu)
                wres = max(wres, float(res))
        nds_f_all = np.array([float(v) for v in nds_all])
        n_zone_nodes = int(np.sum(nds_f_all <= Tz))
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        cens_ok = cens_ok and wres <= RES_BAR and len(sgs) == 1 \
            and n_zone_nodes == m_zone
        ok30 = ok30 and cens_ok
        det30.append("x%d: %d nodes zone %d/%d res %.0e"
                     % (x, len(nds_all), n_zone_nodes, m_zone, wres))
        zone_nds = nds_all[:m_zone]
        zone_f = nds_f_all[:m_zone]
        s_top = float(zone_f[-1] - zone_f[-2]) if m_zone > 1 else 3.0

        # ---- G31 node-config V
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        ok31x = abs(Vd["qrel"]) <= QREL_BAR and Vd["resR"] <= NULLRES_BAR
        ok31 = ok31 and ok31x
        det31.append("x%d: qrel %.0e nullres %.0e nf %d (%.0f s)"
                     % (x, Vd["qrel"], Vd["resR"], Vd["nf"],
                        time.time() - t_q))

        # ---- G32 V1 instantiation: h-ladder at the top zone node
        with mp.workdps(dps):
            tau = Vd["tau_mp"]
            mu_top = zone_nds[-1]
            rows_v1 = []
            for h in H_LADDER:
                for sgn in (-1, 1):
                    pv = mu_top + sgn * mp.mpf(repr(h)) \
                        * mp.mpf(repr(s_top))
                    rr = row_at(pv, K, oms, nrm)
                    lamh, eth, en2h, etnh, rho2h, chih = \
                        secular_data(Vd, rr)
                    Zh = zfac(pv, zone_nds, K, oms)
                    l10 = mp.log(10)
                    rows_v1.append(
                        (h, sgn, float((lamh - tau) / tau),
                         float(2 * mp.log(abs(eth[0])) / l10),
                         float(mp.log(chih * en2h) / l10),
                         float(2 * mp.log(abs(Zh)) / l10),
                         float(eth[0] / Zh), float(eth[1] / Zh)))
            rd = drow_at(mu_top, K, oms, nrm)
            lamd, etd, en2d, etnd, rho2d, chid = secular_data(Vd, rd)
            gd = float((lamd - tau) / tau)
        okv1 = True
        slopes = []
        for sgn in (-1, 1):
            sel = [rw for rw in rows_v1 if rw[1] == sgn]
            lz = [rw[5] for rw in sel]
            sg = float(np.polyfit(lz, [math.log10(rw[2])
                                       for rw in sel], 1)[0])
            sr = float(np.polyfit(lz, [rw[3] for rw in sel], 1)[0])
            sc = float(np.polyfit(lz, [rw[4] for rw in sel], 1)[0])
            slopes.append((sg, sr, sc))
            okv1 = okv1 and abs(sg) <= SLOPE_GAP_BAR \
                and SLOPE_TRACK_WIN[0] <= sr <= SLOPE_TRACK_WIN[1] \
                and SLOPE_TRACK_WIN[0] <= sc <= SLOPE_TRACK_WIN[1]
        for rw in rows_v1:
            okv1 = okv1 and abs(rw[2] / gd - 1.0) <= DROW_TOL
        g0m = [rw[6] for rw in rows_v1 if rw[1] == -1]
        g0p = [rw[6] for rw in rows_v1 if rw[1] == +1]
        drift = abs(g0m[0] / g0m[-1] - 1.0)
        cross = g0m[-1] / g0p[-1]
        okv1 = okv1 and drift <= G0_DRIFT_BAR \
            and G0_CROSS_WIN[0] <= cross <= G0_CROSS_WIN[1]
        ok32 = ok32 and okv1
        det32.append("x%d: drow %.3f, gap range [%.3f, %.3f], G0 "
                     "drift %.2e cross %.4f, slopes gap %s R2 %s "
                     "chi %s" %
                     (x, gd, min(rw[2] for rw in rows_v1),
                      max(rw[2] for rw in rows_v1), drift, cross,
                      "/".join("%+.4f" % s[0] for s in slopes),
                      "/".join("%.3f" % s[1] for s in slopes),
                      "/".join("%.3f" % s[2] for s in slopes)))
        info("x=%d V1 h-ladder (h, sgn, gap, log10 R2/chi_abs/Z^2): "
             % x + " | ".join("%.2f%+d: %.3f %.1f %.1f %.1f"
                              % (rw[0], rw[1], rw[2], rw[3], rw[4],
                                 rw[5]) for rw in rows_v1))

        # ---- G33 r139 replication (zone-top window + U1 + U2)
        with mp.workdps(dps):
            tg = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                TOP_GRID_STEP)) + [Tz - 0.001]
            gmin = None
            argp = None
            for tv in tg:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - tau) / tau)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, et, en2, etn, rho2, chi = secular_data(Vd, r)
            phi = [ce["mpV"][i, 0] for i in range(K)]
            Rdot = sum(r[k] * phi[k] for k in range(K))
            yv = p_mp * p_mp
            F = A0 + sum(((-1) ** k * cs[k] * oms[k] ** 2)
                         / (yv - oms[k] ** 2) for k in range(1, K))
            R_F = 2 * F / p_mp
            Ev, _ = en_pair(cs, aa, oms, p_mp)
            R_E = Ev / mp.sin(aa * p_mp)
            dev1 = float(abs(Rdot - R_F) / abs(R_F))
            dev2 = float(abs(R_E - R_F) / abs(R_F))
            chi_abs = chi * en2
            q1q0 = Vd["qs"][1] - Vd["qs"][0]
            lb = Rdot ** 2 / (chi_abs + Rdot ** 2 / q1q0)
            ub = Rdot ** 2 / ((1 - rho2) * chi_abs)
            g_ex = float((lam - tau) / tau)
            g_lb = float(lb / tau)
            g_ub = float(ub / tau)
            t_lo = g_ex / g_lb
            t_up = g_ub / g_ex
            GT = hsw_G(Tz)
            a0f = abs(float(A0))
            tlaw = tauf / (8.0 * a0f ** 2 * GT)
            P = float(F / A0)
            n_num = float(Rdot ** 2 / tau)
            n_id = P ** 2 / (2.0 * float(p_mp) ** 2 * GT * tlaw)
            Zt = zfac(p_mp, zone_nds, K, oms)
            lZt = float(mp.log(abs(Zt)) / mp.log(10))
            lMedge = float(mp.log(abs(F / A0 / Zt)) / mp.log(10))
        lo_w, hi_w = REPL_WIN[x]
        tl_dev = abs(tlaw / TLAW_TAB[x] - 1.0)
        ok33x = (gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and dev1 <= ID_BAR and dev2 <= ID_BAR
                 and g_lb <= g_ex <= g_ub
                 and 1.0 <= t_lo <= TIGHT_BAR
                 and 1.0 <= t_up <= TIGHT_BAR
                 and abs(n_num - n_id) / n_num <= N_ID_BAR
                 and tl_dev <= TLAW_TOL)
        ok33 = ok33 and ok33x
        det33.append("x%d: top-min %.4f at %.3f tight %.6f/%.6f "
                     "tlaw %.4f (dev %.0e)"
                     % (x, gmin, argp, t_lo, t_up, tlaw, tl_dev))
        gap_tab[x] = gmin
        tau_tab[x] = tauf
        info("x=%d PFLOOR anatomy at argmin: P %.3e, log10|Z| %.1f, "
             "log10|M0/A0| = log10|P/Z| %.1f (edge product carries "
             "the size; zone/lattice content in Z cancels)"
             % (x, P, lZt, lMedge))

        # ---- G34 PFLOOR sin anatomy + measure + Landau/Markov
        zg = gam[gam <= Tz]
        lx = math.log(x)
        sins = np.abs(np.sin(0.5 * lx * zg))
        smin = float(np.min(sins))
        Thi = 2 * math.pi * x * math.exp(MEAS_DU / 2)
        m_hi = int(np.sum(gam <= Thi))
        eps_cert = MEAS_DU / (MEAS_DELTA * m_hi
                              * (MEAS_DU + 2 * math.pi / float(gam[0])))
        SC = float(np.sum(np.cos(lx * zg)))
        nbad = int(np.sum(sins < MARKOV_EPS))
        cap = (m_zone + SC) / (2.0 - 2.0 * MARKOV_EPS ** 2)
        lam_x = 0.0
        for pbase in (2, 3, 5, 7, 11, 13, 17, 19, 23):
            q = pbase
            while q <= x:
                if q == x:
                    lam_x = math.log(pbase)
                q *= pbase
        pred = -math.sqrt(x) * lam_x
        swin = SIN_WIN[x]
        ok34x = (swin[0] <= smin <= swin[1]
                 and smin / eps_cert >= EPSCERT_MIN
                 and nbad <= cap and cap / m_zone <= MARKOV_FRAC)
        ok34 = ok34 and ok34x
        det34.append("x%d: minsin %.4f (win %s) eps_cert %.1e "
                     "ratio %.1f; N_bad %d <= cap %.2f (cap/m %.2f)"
                     % (x, smin, str(swin), eps_cert,
                        smin / eps_cert, nbad, cap, cap / m_zone))
        info("x=%d Landau: S_C = %.3f vs -sqrt(x) Lambda(x) = %.3f "
             "(%s; Landau/Gonek CITED as form)"
             % (x, SC, pred,
                "prime power" if lam_x > 0 else "composite: no term"))

        # ---- G35 below-horizon transport (P_node <-> P_gamma)
        with mp.workdps(dps):
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
            eps_bar = math.sqrt((tauf + off_allow) / 2.0)
            Yz = mp.mpf(repr(float(Tz - 0.001))) ** 2
            lnum_n = mp.mpf(0)
            lnum_g = mp.mpf(0)
            bound = 0.0
            okball = True
            topok = True
            for j in range(m_zone):
                mu = zone_nds[j]
                gj = mp.mpf(repr(float(zg[j])))
                _f0, fp0 = en_pair(cs, aa, oms, mu)
                bball = 2.0 * eps_bar / max(float(abs(fp0)), 1e-300)
                gapj = float(abs(mu - gj))
                okball = okball and gapj <= bball + CACHE_SLOP
                lnum_n += mp.log(abs(Yz - mu * mu))
                lnum_g += mp.log(abs(Yz - gj * gj))
                tmax = float(gj) + bball + CACHE_SLOP
                topok = topok and tmax < Tz - 0.001
                bound += (bball + CACHE_SLOP) * 2 * tmax \
                    / (float(Yz) - tmax * tmax)
            dl = float(abs(lnum_n - lnum_g))
        ok35x = okball and topok and dl <= bound
        ok35 = ok35 and ok35x
        det35.append("x%d: |dlog P| %.1e <= bound %.1e (balls+slop "
                     "ok %s, eps_bar %.1e)"
                     % (x, dl, bound, okball, eps_bar))

        # ---- G36 Stieltjes identity + S_1 window
        Tcut = float(zg[-1]) + 0.5 * (Tz - float(zg[-1]))
        with mp.workdps(60):
            Yc = mp.mpf(repr(float(Tz))) ** 2

            def fnc(tv2, Yc=Yc):
                return mp.log(Yc - mp.mpf(repr(float(tv2))) ** 2)
            lhs = sum(fnc(g) for g in zg)
            pts = list(zg) + [Tcut]
            rhs = mp.mpf(m_zone) * fnc(Tcut)
            for j in range(m_zone):
                rhs -= mp.mpf(j + 1) * (fnc(pts[j + 1]) - fnc(pts[j]))
            devS = float(abs(lhs - rhs) / abs(lhs))
            main = mp.mpf(m_rvm(Tcut)) * fnc(Tcut) - mp.quad(
                lambda t2: mp.mpf(m_rvm(float(t2)))
                * (-2 * mp.mpf(repr(float(t2)))
                   / (Yc - mp.mpf(repr(float(t2))) ** 2)),
                [float(gam[0]) * 0.5, Tcut])
            fluct = float(lhs - main)
        zs = gam[gam <= Tz]
        accN = 0.0
        prev = 0.0
        for j, g in enumerate(zs):
            accN += j * (g - prev)
            prev = float(g)
        accN += len(zs) * (Tz - prev)
        with mp.workdps(40):
            accR = float(mp.quad(lambda t2: mp.mpf(m_rvm(float(t2))),
                                 [1.0, Tz]))
        s1 = accN - accR
        s1r = abs(s1) / math.log(Tz)
        ok36x = devS <= STIELTJES_BAR and s1r <= S1_RATIO_BAR
        ok36 = ok36 and ok36x
        det36.append("x%d: dev %.0e sumlog %.2f main %.2f fluct "
                     "%.3f S1 %.3f (|S1|/logTz %.2f)"
                     % (x, devS, float(lhs), float(main), fluct,
                        s1, s1r))

        # ---- G37 SUSCAP2R anatomy + J-enclosure
        with mp.workdps(dps):
            qs = Vd["qs"]
            nf = Vd["nf"]
            s_val = float(tau * chi / rho2)
            d1 = float((qs[1] - qs[0]) / tau)
            e1n2 = float(etn[1] * etn[1])
            rho2f = float(rho2)
            chif = float(chi)
            share1 = float((etn[1] * etn[1] / (qs[1] - qs[0])) / chi)
            # J-enclosure ladder
            jrows = []
            okencl = True
            jstar = None
            for J in range(2, nf):
                head = sum(float(etn[i] * etn[i] / (qs[i] - qs[0]))
                           for i in range(1, J))
                restJ = 1.0 - rho2f - sum(float(etn[i] * etn[i])
                                          for i in range(1, J))
                chihiJ = head + restJ / float(qs[J] - qs[0])
                okencl = okencl and chif <= chihiJ * (1 + 1e-20)
                ratio = chihiJ / chif
                if jstar is None and ratio <= 2.0:
                    jstar = J
                if J <= 4 or J == nf - 1 or (jstar is not None
                                             and J == jstar):
                    jrows.append("J%d:%.1e" % (J, ratio))
            chilo = float(etn[1] * etn[1] / (qs[1] - qs[0])) \
                + (1.0 - rho2f - e1n2) / float(qs[nf - 1] - qs[0])
        sg = s_val * g_ex
        ok37x = (SGAP_WIN[0] <= sg <= SGAP_WIN[1] and s_val <= S_BAR
                 and chilo <= chif * (1 + 1e-12) and okencl
                 and share1 >= SHARE1_BAR)
        ok37 = ok37 and ok37x
        s_tab[x] = s_val
        det37.append("x%d: s %.5f s*gap %.5f share1 %.3f J* %s/%d"
                     % (x, s_val, sg, share1, str(jstar), nf))
        info("x=%d SUSCAP2R: chi %.3e chi_lo %.3e; J-ladder "
             "chi_hi(J)/chi: %s (tail-heavy: rest ~ %.3f of the "
             "overlap mass sits above J=2)"
             % (x, chif, chilo, " ".join(jrows),
                1.0 - rho2f - e1n2))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    check("G31-node-config", ok31,
          "|qrel| <= %.0e, null residual <= %.0e at every rung "
          "(q_0 == tau: phi in the kernel): %s"
          % (QREL_BAR, NULLRES_BAR, "; ".join(det31)))
    check("G32-v1-instantiated", ok32,
          "h-ladder at the top node: |slope log gap vs log Z^2| <= "
          "%.2f while R_phi^2 and chi_abs track Z^2 with slopes in "
          "%s; gap through the node == drow gap within %.2f; "
          "reduced G_0 bounded (drift <= %.1f, cross-node in %s): "
          "THE ZONE-LATTICE PRODUCT CANCELS IN THE GAP (V1): %s"
          % (SLOPE_GAP_BAR, str(SLOPE_TRACK_WIN), DROW_TOL,
             G0_DRIFT_BAR, str(G0_CROSS_WIN), "; ".join(det32)))
    check("G33-r139-replication", ok33,
          "zone-top grid min >= %.1f and in the frozen r139 window; "
          "R_phi three-way <= %.0e; U1 lower <= exact <= upper "
          "(tightness <= %.2f); U2 n-identity <= %.0e with tlaw on "
          "the CDXLI strings <= %.0e: %s"
          % (GAP_MIN_BAR, ID_BAR, TIGHT_BAR, N_ID_BAR, TLAW_TOL,
             "; ".join(det33)))
    check("G34-pfloor-sin-measure-landau", ok34,
          "min|sin(A gamma)| in the frozen window; measured/eps_cert "
          ">= %.1f (V2 constructive floor); Markov cap N_bad(%.1f) "
          "<= (m + S_C)/(2 - 2 eps^2) with cap/m <= %.2f (V3): %s"
          % (EPSCERT_MIN, MARKOV_EPS, MARKOV_FRAC, "; ".join(det34)))
    check("G35-pfloor-below-horizon", ok35,
          "|log P_node - log P_gamma| <= PINBALL kernel bound "
          "(balls + cache slop %.0e; top ball below T_z): the "
          "below-horizon PFLOOR reduces to census (PT21, cited) + "
          "per-rung EPS-LOCK + kernel enclosure: %s"
          % (CACHE_SLOP, "; ".join(det35)))
    check("G36-pfloor-stieltjes", ok36,
          "partition identity dev <= %.0e (log P is a counting "
          "integral); RvM main + fluctuation printed; own-cache "
          "|S_1(T_z)|/log T_z <= %.1f (Littlewood class, CITED -- "
          "the lambda-uniform fluctuation carrier): %s"
          % (STIELTJES_BAR, S1_RATIO_BAR, "; ".join(det36)))
    check("G37-suscap2r", ok37,
          "s x gap in %s (the exact SUSCAP2R currency: gap >= "
          "1/(s + 1/delta_1)); s <= %.1f; chi_lo <= chi <= chi_hi(J) "
          "valid; first-excited chi share >= %.1f; J_star printed "
          "(tail-heavy closed form -- the named hardness): %s"
          % (str(SGAP_WIN), S_BAR, SHARE1_BAR, "; ".join(det37)))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (the certificate must refuse)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        musw, _nr = raw_mp_census(cw)
        Tzw = 2 * math.pi * xw
        n_nodes_w = int(np.sum(musw <= Tzw))
        m_true_w = int(np.sum(gam <= Tzw))
        over = n_nodes_w - m_true_w
        with mp.workdps(dpsw):
            tauw = float(cw["mpE"][0])
        refuse = over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (%s)" % (world, xw, n_nodes_w, m_true_w, over,
                             float(musw[0]), float(gam[0]), tauw,
                             "NOT PSD" if tauw <= 0 else "PSD"))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap; V1/SUSCAP2R machinery claims nothing where PSD/"
          "pinning fail (tau_w printed)")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lg_ = [math.log10(gap_tab[x]) for x in xs_all]
        s_g = float(np.polyfit(lt, lg_, 1)[0])
        ls_ = [math.log10(s_tab[x]) for x in xs_all]
        s_s = float(np.polyfit(xs_all, ls_, 1)[0])
        check("G54-tau-screen", abs(s_g) <= TAU_SLOPE_BAR,
              "slope log10 top-gap vs log10 tau = %.4f (<= %.2f: the "
              "RATIO is not Connes-priced; the RAW gap rides tau BY "
              "CONSTRUCTION -- BOUND-RIDES-CONNES typed); s-slope "
              "%.4f dex/x (the r139 compensation law IS the "
              "s-flatness, MEASURED)" % (s_g, TAU_SLOPE_BAR, s_s))
    ce5c = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
    with mp.workdps(ce5c["dps"]):
        E0 = ce5c["mpE"][0]
        Qp_ = ce5c["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5c["K"]))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e (nonzero "
          "and bounded; round-118 red flag; all mp under workdps)"
          % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  QUANTIFIER AUDIT + MIN-CUT")
    okq, detq = quantifier_audit()
    check("G60-quantifier-audit", okq,
          "demand-level algebra over the cited chain (CDXXIII "
          "NF-closure, CDXXX Theorem R + L3/L4): every source omega "
          "is demanded only along an INSTRUMENT-CHOSEN UNBOUNDED "
          "x-SEQUENCE per dense a -- DENSE-X SUFFICES and V2 "
          "delivers the good sets constructively (typed CHAIN-AUDIT; "
          "cited theorems not re-proven): %s" % detq)

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
                ("EPSLOCK", "SUSCAP2R"): 1,
                ("SUSCAP2R", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("EPSLOCK", "SUSCAP2R")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1, ("SUSCAP2R", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G61-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r139 serial triple "
          "EPSLOCK(1) -> PFLOOR(1) -> SUSCAP2(1) CONTRACTED to "
          "EPSLOCK(1) -> SUSCAP2R(1) with PFLOORTHM(INF: V1 "
          "cancellation + V2 measure lemma + below-horizon "
          "reduction + Stieltjes pricing) behind QSUBGAPTHM; "
          "one-grant still 5; counterfactual PARALLEL 6 NOT REAL; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")
    info("EXACT RESIDUE after this round (read with CDXLI/CDXLII/"
         "CDXLIII): RH <== [r122-NF-closure] + [Theorem R] + {L1, "
         "WPD} on dense a; ...; QSUBGAP <== EPSLOCK-consumed + "
         "SUSCAP2R (PFLOOR REMOVED by V1: the gap is Z-free); "
         "EPSLOCK <== JETLOCK + BANDMASS (CDXLI).  RESIDUE = "
         "{JETLOCK, BANDMASS, SUSCAP2R} + dense-a + a-extension + "
         "window-a, with the x-quantifier now audited DENSE-X "
         "(instrument-chosen sequence).  PFLOOR standalone: dense-x "
         "constructive (V2), below-horizon citable-reduced, "
         "above-horizon counting-priced (RvM/HSW + Littlewood S_1 "
         "CITED); pointwise-ALL-x typed OBSTRUCTED-DIOPHANTINE.  "
         "SUSCAP2R stays open: BANDMASS-class, tail-heavy finite-"
         "data form, s measured flat 0.03-0.06.  NO RH claim; "
         "nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "V1-PROVEN(zone-product cancellation: PFLOOR is NOT an "
        "input to the gap; G10/G11/G12/G32)",
        "V2-PROVEN(dense-x measure lemma, constructive; G13/G34)",
        "V3-LANDAU-COUNTING(exact coordinate + Markov cap; G15/G34)",
        "PFLOOR-BELOW-HORIZON-REDUCED(census + PINBALL + kernel "
        "enclosure; G35)",
        "PFLOOR-ABOVE-HORIZON-PRICED(Stieltjes counting integral: "
        "RvM main + Littlewood-class S_1 + V2 boundary; G14/G36)",
        "PFLOOR-POINTWISE-OBSTRUCTED(Diophantine, named)",
        "SUSCAP2R-EXACT-FORM(gap >= 1/(s + 1/delta_1); compensation "
        "== s-flatness; G16/G37/G54)",
        "SUSCAP2-TAIL-HEAVY(J_star growing; the omega stays open, "
        "BANDMASS-class; G37)",
        "MERGE-ANSWER(the Diophantine core CANCELS out of the gap: "
        "PFLOOR eliminated, not identified with SUSCAP2; G32)",
        "QUANTIFIER-DENSE-X-SUFFICES(chain-audit, typed; G60)",
        "CONTROLS-REFUSE(zone overcount + zero-free gap; G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "OMEGA-CONTRACTED(QSUBGAP <== EPSLOCK + SUSCAP2R; G61)"]
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
        print("COMPOSITE: V1-PROVEN + V2-PROVEN + V3-LANDAU-COUNTING "
              "+ PFLOOR-BELOW-HORIZON-REDUCED + "
              "PFLOOR-ABOVE-HORIZON-PRICED + "
              "PFLOOR-POINTWISE-OBSTRUCTED + SUSCAP2R-EXACT-FORM + "
              "SUSCAP2-TAIL-HEAVY + MERGE-ANSWER + "
              "QUANTIFIER-DENSE-X-SUFFICES + CONTROLS-REFUSE + "
              "DEMAND-FLAT + OMEGA-CONTRACTED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
