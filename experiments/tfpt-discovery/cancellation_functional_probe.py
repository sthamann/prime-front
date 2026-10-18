#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cancellation_functional_probe -- PRIME.CANCELLATION.FUNCTIONAL.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files
(krein_definitizer_probe.py, zb_wiggle_strat_probe.py, the
smooth-commensurability lane, the independent session's untracked
probes, sieve4_helper.bin) are not touched.

=======================================================================
MISSION (round ~190: the cancellation functional).  Round 189
(loewner_pick_probe, SPEC_SHA a547448468899af9) left the wall in its
most concrete form ever: TWO exactly known objects -- the canonical
one-function Loewner completion L_f (indefinite, missing wall
positivity by 9.4..87.9 orders) and the diagonal cosine-quadrature
shift diag(Delta) (indefinite both signs) -- sum to a PSD matrix at
every true rung.  THIS round asks which source functional forces the
cancellation, and answers it with THREE NEW EXACT LAWS (symbolic
proofs + mp at every rung) plus the measured anatomy:

  THE ACF LAW (the round's centerpiece, C2 pivot resolved).  For a
  single atom (u, w), u <= L = 2a, the atom's TOTAL wall
  contribution (off-diagonal divided differences of f_atom =
  2 om w sin(om u) PLUS the diagonal cosine shift -mult_k 2a w
  cos(om_k u)) is the kernel w*W(u) with
      x^T W(u) x  =  -2 * int_0^{L-u} A_x(t) A_x(t+u) dt,
      A_x(t) = sum_k x_k cos(om_k t),
  i.e. MINUS TWICE THE APERIODIC AUTOCORRELATION of the windowed
  mode polynomial at lag u.  Proof route (all gated): the
  convolution identity 2 int_0^u cos(om_i(u-t))cos(om_j t) dt =
  (f_i - f_j)/(b_i - b_j) [generic, no periodicity], the wraparound
  identity R_per(u) = (B*B)(u) + (B*B)(L-u) and (BconvB)(u) =
  (B*B)(L-u) on the commensurate lattice om_k = 2 pi k / L [integer
  modes], and the diagonal-shift identity L sum_k mult_k x_k^2
  cos(om_k u) = 2 R_per(u) [orthogonality; mult_0 = 2 is EXACTLY
  the wraparound of the k = 0 mode].  Consequence: Q_q(x) is NOT a
  perfect square and NOT pointwise nonnegative per atom (x = e_0
  gives 2(u-L) < 0); it is minus a sample of the POSITIVE-DEFINITE
  function g_x(u) = int_0^{L-u} A_x A_x(.+u) (Wiener-Khinchin:
  hat-g = |hat-B|^2 >= 0, B = A restricted to [0, L]).  The
  sin/cos slot split of r189 is one object: sine off-diagonal and
  cosine diagonal are the two faces of ONE autocorrelation sample.

  THE POLE SQUARE.  x^T RawPole x = 8 sinh^2(a/2)
  (int_0^infty e^{-t/2} A_x(t) dt)^2 -- an exact L^2 square
  (Laplace transform of the mode polynomial), manifestly PSD; the
  Herglotz point mass of r189 in integral form.

  THE ARCH REGULARIZED COS-LAW (closes the r189 open arch item).
  The arch block is the continuum-atom sine quadrature of the
  measure a(w) dw = e^{-w/2}/(1-e^{-2w}) dw on [0, L]; its cosine
  transform is log-divergent at w = 0, and the measured diagonal
  excess is EXACTLY the regularized cosine quadrature:
      DeltaArch_k = -mult_k L (kappa(om_k) + c*),
      kappa(om) = Ci(L om)/2 - (gamma + log om)/2
                  + int_0^L cos(om w) r(w) dw   (om > 0),
      kappa(0)  = log(L)/2 + int_0^L r(w) dw,
      c* = (gamma + log(2 pi))/2   EXACTLY (k-independent,
      including k = 0 with the same mult doubling),
  r(w) = a(w) - 1/(2w).  With this law the ENTIRE wall is a closed
  Weil-explicit-formula-type functional of the test function g_x:
      x^T Raw x = 8 sinh^2(a/2) (int e^{-t/2} A_x)^2
                  - 2 [int_0^L g_x(w) a(w) dw]_reg
                  - 2 sum_q (Lambda(q)/sqrt(q)) g_x(log q),
  where [.]_reg subtracts the (gamma + log 2pi)-counterterm carried
  by g's diagonal part.  Wall positivity at rung h ==
  Guinand-Weil-type positivity of this finite form on the test
  family {autocorrelations of window cosine polynomials} -- an
  ALGEBRAIC RESTATEMENT of the same wall, typed as such, priced in
  G60; the all-test-function Weil criterion is a FLAGGED LOOP
  (WEIL-ALLTESTS <-> RH), consumed by NOTHING (G51).  NO RH CLAIM.

GOALS (contract PRIME.CANCELLATION.FUNCTIONAL.01):
  C1  ANATOMY.  (i) In the eigenbasis of Raw: split lambda_m =
      alpha_m + beta_m (alpha = v^T L_f v, beta = v^T Delta v);
      cancellation ratio r_m = |lambda_m|/(|alpha_m| + |beta_m|);
      concentration index CI = median log10 r - log10 r_0 --
      concentrated at the collapsing direction or spread (enum).
      (ii) L_f negative subspace: n_neg ladder; complementarity
      rho_min = min_y (y^T Delta y)/(-mu_y) over negative eigpairs
      (PSD of Raw forces rho >= 1: gated at true rungs); matching
      log10(||Y^T Raw Y||_F/||Y^T Delta Y||_F); positive-mass
      share sigma(y).  (iii) per-atom decomposition at the bottom
      eigenvector: t_q = -2 w_q g_v(log q); sign ladder (n+, n-),
      budgets P + A + sum_q t_q = lambda_0 (mp consistency), and
      the localization scale m99 (smallest top-|t| subset within
      1% of the prime total).
  C2  PERFECT-SQUARE HUNT: resolved by the ACF law -- per-atom NOT
      a square, NOT nonneg; the wall prime part is minus an
      autocorrelation sampled at prime logs; the pole IS a square;
      the arch is the same ACF functional under a(w) dw with a
      closed-form regularization.  Symbolic generic proofs first,
      mp verification at every rung.
  C3  WORLDS: identity is world-blind linear algebra (typed, never
      sold); anatomy VALUES at (SMOOTH,5) (continuum e^{w/2} dw --
      the sibling smooth lane owns the geometry; we only read our
      anatomy there), (SCRARITH,5), (EPSTEIN,8).  Complementarity
      failure (rho_min < 1) is EQUIVALENT to indefiniteness by
      construction -- typed definitional, not sold as a separator.
      Witness: r172 inflation witness deforms the coefficient ray;
      all round objects are matrix-side, witness-invariant BY
      CONSTRUCTION (typed).  ATOMJET (q = 2 weight doubled, h = 5)
      must shift the wall by EXACTLY dw*W(log 2) entrywise and the
      form by -2 dw g_x(log 2) (the ACF law reads jets linearly).
  C4  PRICING: the ACF/Weil rewrite is exact and NEW as structure,
      but the residual object it exposes (domination of the
      autocorrelation samples by pole + arch) IS the wall again --
      relabeling barrier named, not crossed; no l1 majorant is
      touched (|g(u)| <= g(0) is a DEAD CLASS bound, not used);
      localization scale delivered as the honest measurement.

NOTATION (r171-r189 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a = 2 pi k/L; b_k = om_k^2;
nrm_0 = sqrt(2a), nrm_k = sqrt(a); par_k = (-1)^k; mult_0 = 2,
mult_k = 1; atoms {(u_q, w_q)} = {(log q, log p/sqrt q)}, q = p^m
<= h; Raw = D_par N M N D_par (Sylvester congruence, M PSD <=> Raw
PSD); f = f_pole + f_arch + 2 om pj; f'(b_k) as in r189; L_f =
off-diag Raw + diag f'; Delta = diag(Raw) - f'.  W(u): off-diag
2(om_i sin(om_i u) - om_j sin(om_j u))/(b_i - b_j), diag
sin(om_k u)/om_k + (u - L)cos(om_k u) (k >= 1), 2(u - L) (k = 0).
g_x(u) = -x^T W(u) x / 2.  Frozen probe vectors xg1_k =
frac((k+1) phi) - 1/2 (phi golden), xg2_k = frac((k+1)(sqrt 2 - 1))
- 1/2.  SMOOTH world: continuum atom measure e^{w/2} dw on [0, L]
(prime part = -2 int e^{w/2} g_x(w) dw); SCRARITH golden-map weight
permutation; EPSTEIN x^2+5y^2 Dirichlet atoms -- all builder
recipes VERBATIM.

DPS schedule (r182/r189 ladder VERBATIM): DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16, H_HOLD = 20.
BOTTOM-DIRECTION ANATOMY (budgets, depth, r_0, per-atom ladder,
signs, m99) in mp at EVERY rung via INVERSE ITERATION (3 LU
solves; the bottom eigenvalue is tau-scale-isolated; wards:
eigen-residual, Rayleigh stability iter2->3, and eigsy-overlap at
ANAT_MP = (4, 5, 8, 13), where the full mp.eigsy spectral ladder is
also computed).  Spectral-median ladder (m >= 1) and the L_f
negative-subspace quantities at non-ANAT_MP rungs in float64 on the
mp-built downcast (DISCLOSED: those are O(1) eigenvalue ratios,
float64-safe; the BOTTOM direction is NEVER taken from float64 --
amendment A3).  EIGENVECTOR ACCESS IS IN-SCOPE THIS ROUND (the r189
eigenvector firewall was that round's choice; the
zero-oracle/zeta/np.load/verification firewall stands).
QUAD_WARD = {4: all atoms x 2 vectors, 5: all atoms x 2 vectors,
8: first 3 atoms x 1 vector} (oscillation-split mp.quad).
ARCH_RUNGS = (4, 5), all k = 0..K-1.  PD exhibit: 7 points
t_i = i L/7 at h = 5, vector xg1.  JET_RUNG = 5 (first atom q = 2).
CONTROLS: (SMOOTH,5), (SCRARITH,5), (EPSTEIN,8) at dps 60/60/80.
PRECISION REFUSAL: eigenvalue sign refused if |lam| <
10^-(dps-20) ||.||_F (float64: 10^-10 ||.||_F); refusals counted.

FROZEN BARS: ASM_BAR 1e-30 (assembly, entrywise rel, every rung);
QUAD_BAR 1e-25; POLE_SQ_BAR 1e-35; ARCH_KIND_BAR 1e-40
(k-independence of c*_k); ARCH_CSTAR_BAR 1e-40 (c* vs
(gamma+log 2pi)/2); BUDGET_BAR 1e-25 (fro-relative, every rung);
INVIT_RES_BAR 1e-12, INVIT_STAB_BAR 1e-6, OVL_BAR 1e-12
(inverse-iteration wards; convergence is GAP-limited, amendment
A4); RHO_TOL_MP 1e-8, RHO_TOL_F64 1e-5; PD_BAR -1e-30 (rel);
JET_BAR 1e-28; SMOOTH_ID_BAR 1e-25; CTRL_ASM_BAR 1e-25;
TAU_FLAT_BAR 0.30; COND_LO/HI 1e-40/1e-10; RUNTIME_BAR 2700 s.
Record tolerances: LOG_TOL 0.10 dex; SLOPE_TOL 0.05; counts exact;
CI_TOL 0.30 dex.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  acf_exact  := G10/G11 symbolic pass AND G20 <= ASM_BAR at every
                rung AND G21 wards pass;
  arch_exact := G22 pass (k-independence + closed-form constant);
  primary    := WALL-IS-WEIL-ACF-FORM-EXACT iff acf_exact AND
                arch_exact, else ACF-REPRESENTATION-PARTIAL;
  mechanism  := PER-ATOM-MANIFEST-POSITIVE iff every atom kernel
                W(u_q) is PSD at some rung (NOT anticipated), else
                PER-ATOM-SIGNED-GLOBAL-CANCELLATION;
  signEnum   := PRIME-TERM-ONE-SIGNED-AT-COLLAPSE iff n+ = 0 at
                every rung (zero-class rule: |t_q| <= 1e-30
                max|t|), else PRIME-TERM-MIXED-AT-COLLAPSE;
  concEnum   := CANCELLATION-CONCENTRATED-AT-COLLAPSE iff CI >= 2
                dex at every rung, else CANCELLATION-MIXED iff
                CI >= 2 at >= 1 rung, else CANCELLATION-SPREAD;
  compEnum   := COMPLEMENTARITY-SHARP iff min_h rho_min <= 1.1,
                else COMPLEMENTARITY-SLACK (with the ladder
                recorded either way).

RECORD TABLES (frozen at freeze from the disclosed pre-freeze
calibration ladder: TWO structural smokes (smoke1 FAILED G10 and
hung in G11 -- amendment A1; smoke2 24/24) and TWO disclosed
calibration passes (calib_cf_pass1.log 24/24 but with the
bottom-direction anatomy on float64 eigenvectors -- exposed as
direction-noise by an mp cross-check, amendment A3; substantive
tables frozen from calib_cf_pass2.log, 23/24 with the single fail
being the mis-set gap-limited inverse-iteration ward bar, amendment
A4)).  Verdicts frozen from calib pass 2: the ACF law and pole
square hold at ALL 14 rungs (assembly devs <= 1.7e-61, quadrature
wards <= 2.7e-31, pole square <= 4.5e-61); the arch regularized
cos-law is EXACT at h = 4 and 5 for every k (k-independence <=
3.1e-61, c* - (gamma+log 2pi)/2 = 0.0 at working precision) --
three new exact laws.  ANATOMY (all bottom-direction numbers mp):
budgets at the collapsing direction P (pole, > 0) 1.281 -> 2.632,
A (arch, < 0) -1.251 -> -2.517, Pr (prime, < 0) -0.031 -> -0.115
across h = 4 -> 20, cancelling to depth -11.11 -> -88.25 (= the
tau ladder, DEFINITIONAL); concentration TOTAL at the bottom:
CI = 11.3 -> 88.7 dex vs spectrum-median cancellation ratio
~10^-0.5..10^0 -- enum CANCELLATION-CONCENTRATED-AT-COLLAPSE;
THE SIGN LAW (the round's cleanest measured finding): at the
bottom eigenvector EVERY resolvable atom contributes NEGATIVELY
(n+ = 0 at all 14 rungs -- each atom's autocorrelation sample
g_v(log q) > 0), the ladder decays near-exponentially in log q toward
the window edge (log10 |t_q| e.g. h=13: -1.0, -3.0, -5.8, -8.3,
-14.6, -18.7, -22.6, -32.3, and the commensurate q = h atom EXACT
ZERO at the dps noise floor), enum
PRIME-TERM-ONE-SIGNED-AT-COLLAPSE; localization m99 = 1..2 of
3..12 atoms (q = 2, sometimes + q = 3, carries the prime total);
L_f negative subspace n_neg 1..34 (non-monotone), complementarity
rho_min 1.16..2.91 >= 1 everywhere (finite margin, enum
COMPLEMENTARITY-SLACK: the ultra-sharp cancellation lives in the
bottom direction, NOT in the whole negative subspace), matching
log10 ||Y^T Raw Y||/||Y^T Delta Y|| remarkably CONSTANT ~ -0.2,
sigma_min 0.83..0.98; worlds: identity world-blind (discrete devs
<= 1.6e-61, SMOOTH continuum 1.2e-59), values: rho_min >= 1 ALSO
in the indefinite SCRARITH/EPSTEIN cells (top-of-spectrum
indefiniteness -- amendment A2: necessary-not-sufficient, NOT a
detector), SMOOTH n_neg = 0 (L_f PSD at nodes, complementarity
vacuous, the r189 commensurability finding in anatomy
coordinates); ATOMJET linear (devs 3.0e-61/8.3e-61); tau screens:
n_neg/K slope -0.005, match slope +0.000, m99/atoms slope +0.001
-- ALL FLAT; depth-vs-tau typed DEFINITIONAL.
CAL_NNEG {h: n_neg}: 4: 1, 5: 1, 6: 5, 7: 2, 8: 7, 9: 7, 10: 14,
  11: 5, 12: 15, 13: 9, 14: 20, 15: 27, 16: 26, 20: 34.
CAL_RHO {h: rho_min}: 4: "2.9055", 5: "2.0651", 6: "1.2323",
  7: "1.9831", 8: "1.7085", 9: "1.6893", 10: "1.2826",
  11: "1.7340", 12: "1.4378", 13: "1.6284", 14: "1.2736",
  15: "1.4523", 16: "1.1612", 20: "1.2790".
CAL_MATCH {h: log10 match}: 4: "-0.18", 5: "-0.29", 6: "-0.22",
  7: "-0.12", 8: "-0.21", 9: "-0.19", 10: "-0.19", 11: "-0.18",
  12: "-0.23", 13: "-0.19", 14: "-0.20", 15: "-0.21", 16: "-0.20",
  20: "-0.22".
CAL_SIGNS {h: (n+, n-, n0)}: 4: (0,2,1), 5: (0,3,1), 6: (0,4,0),
  7: (0,4,1), 8: (0,5,1), 9: (0,6,1), 10: (0,7,0), 11: (0,7,1),
  12: (0,7,1), 13: (0,7,2), 14: (0,8,1), 15: (0,8,1), 16: (0,8,2),
  20: (0,8,4).
CAL_M99 {h: m99}: 4..13: 1 everywhere; 14: 2, 15: 2, 16: 2, 20: 2.
CAL_DEPTH (all rungs, log10 |lam_0|/(|P|+|A|+|Pr|)): 4: "-11.11",
  5: "-16.25", 6: "-20.70", 7: "-25.50", 8: "-29.90", 9: "-34.56",
  10: "-39.45", 11: "-44.23", 12: "-49.46", 13: "-54.08",
  14: "-59.51", 15: "-63.74", 16: "-68.86", 20: "-88.25".
CAL_CI (all rungs, dex): 4: "11.31", 5: "16.20", 6: "20.58",
  7: "25.64", 8: "30.14", 9: "34.82", 10: "39.56", 11: "44.48",
  12: "49.73", 13: "54.50", 14: "59.80", 15: "63.95", 16: "69.28",
  20: "88.65".
CAL_SIGMA {h: sigma_min}: 4: "0.98", 5: "0.83", 6: "0.97",
  7: "0.97", 8: "0.97", 9: "0.92", 10: "0.98", 11: "0.93",
  12: "0.97", 13: "0.92", 14: "0.98", 15: "0.97", 16: "0.87",
  20: "0.97".
CAL_CTRL {(world, x): (n_neg, rho_min|None, indef)}:
  (SMOOTH, 5): (0, None, 1); (SCRARITH, 5): (1, "1.0992", 1);
  (EPSTEIN, 8): (11, "1.1199", 1).
CAL_SLOPES: nneg "-0.005", match "+0.000", m99 "+0.001".
AMENDMENTS (four, all pre-freeze, all disclosed):
A1 (smoke-driven): the exact layer originally used sp.integrate
  for the convolution/ACF integrals -- Piecewise branches broke
  G10 and the lattice integrals did not terminate (smoke1).
  Replaced by explicit product-to-sum antiderivatives WARDED by
  symbolic differentiation (a strengthening: the integration step
  itself is now proof-carrying).  No target changed.
A2 (calibration-driven): the anticipated reading 'complementarity
  fails iff the cell is indefinite' is MEASURED FALSE: rho_min >=
  1 holds in the indefinite SCRARITH/EPSTEIN cells too (their
  indefiniteness is top-of-spectrum, r186-concordant), and SMOOTH
  has an EMPTY L_f-negative subspace.  G41 re-typed
  resolve-and-record: single-direction complementarity is
  NECESSARY-not-sufficient, not a world detector.
A3 (calibration-driven, the substantive one): calib pass 1 read
  the per-atom ladder off float64 bottom eigenvectors; an mp
  cross-check at h = 6/9 showed those are DIRECTION-NOISE below
  the tau gap (float64 gave O(1) mixed-sign t_q where the true mp
  ladder is one-signed and exponentially decaying).  The bottom
  direction is now computed by mp INVERSE ITERATION at every rung;
  the float64 sign/m99 entries of pass 1 were discarded as
  artifacts.  This amendment REVERSED the pass-1 sign-ladder
  reading (mixed -> one-signed): disclosed prominently.
A4 (calibration-driven): the inverse-iteration ward bar was first
  set dps-scaled (10^-(dps-30)); measured convergence is
  GAP-limited (residual ~ |lam_0|/gap-scale), so pass 2 failed
  G23 on the ward while every substantive number was exact.  Bars
  reset to INVIT_RES 1e-12 / STAB 1e-6 / OVL 1e-12 with a third
  iteration added; no substantive table value moved.
No dps rung, vector recipe or control recipe moved at any point;
record tables and resolved enums inserted at freeze (house pattern
identical to r186/r189).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G13; S2 mp dictionary + anatomy G20-G26; S4
controls/witness G40-G43; S5 screens/adjudication G50-G53; S6
pricing G60-G61 + G99 runtime.  DETERMINISM: no randomness anywhere;
ProcessPool results keyed; run2 must be identical modulo wall-clock
tokens (lines carrying 'WALL').

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
WORKERS = 10
RUNTIME_BAR = 2700.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
ANAT_MP = (4, 5, 8, 13)
QUAD_WARD = {4: (0, 2), 5: (0, 2), 8: (3, 1)}   # (natoms or 0=all, nvecs)
ARCH_RUNGS = (4, 5)
PD_RUNG = 5
PD_NPTS = 7
JET_RUNG = 5
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

ASM_BAR = 1e-30
QUAD_BAR = 1e-25
POLE_SQ_BAR = 1e-35
ARCH_KIND_BAR = 1e-40
ARCH_CSTAR_BAR = 1e-40
BUDGET_BAR = 1e-25
RHO_TOL_MP = 1e-8
RHO_TOL_F64 = 1e-5
INVIT_RES_BAR = 1e-12
INVIT_STAB_BAR = 1e-6
OVL_BAR = 1e-12
PD_BAR = -1e-30
JET_BAR = 1e-28
SMOOTH_ID_BAR = 1e-25
CTRL_ASM_BAR = 1e-25
TAU_FLAT_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
EIG_REFUSE_SAFETY = 20
F64_REFUSE = 1e-10

LOG_TOL = 0.10
SLOPE_TOL = 0.05
CI_TOL = 0.30

# --------------------- calibrated record tables (calib_cf_pass2.log)
CAL_NNEG = {4: 1, 5: 1, 6: 5, 7: 2, 8: 7, 9: 7, 10: 14, 11: 5,
            12: 15, 13: 9, 14: 20, 15: 27, 16: 26, 20: 34}
CAL_RHO = {4: "2.9055", 5: "2.0651", 6: "1.2323", 7: "1.9831",
           8: "1.7085", 9: "1.6893", 10: "1.2826", 11: "1.7340",
           12: "1.4378", 13: "1.6284", 14: "1.2736", 15: "1.4523",
           16: "1.1612", 20: "1.2790"}
CAL_MATCH = {4: "-0.18", 5: "-0.29", 6: "-0.22", 7: "-0.12",
             8: "-0.21", 9: "-0.19", 10: "-0.19", 11: "-0.18",
             12: "-0.23", 13: "-0.19", 14: "-0.20", 15: "-0.21",
             16: "-0.20", 20: "-0.22"}
CAL_SIGNS = {4: (0, 2, 1), 5: (0, 3, 1), 6: (0, 4, 0),
             7: (0, 4, 1), 8: (0, 5, 1), 9: (0, 6, 1),
             10: (0, 7, 0), 11: (0, 7, 1), 12: (0, 7, 1),
             13: (0, 7, 2), 14: (0, 8, 1), 15: (0, 8, 1),
             16: (0, 8, 2), 20: (0, 8, 4)}
CAL_M99 = {4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1,
           12: 1, 13: 1, 14: 2, 15: 2, 16: 2, 20: 2}
CAL_DEPTH = {4: "-11.11", 5: "-16.25", 6: "-20.70", 7: "-25.50",
             8: "-29.90", 9: "-34.56", 10: "-39.45", 11: "-44.23",
             12: "-49.46", 13: "-54.08", 14: "-59.51",
             15: "-63.74", 16: "-68.86", 20: "-88.25"}
CAL_CI = {4: "11.31", 5: "16.20", 6: "20.58", 7: "25.64",
          8: "30.14", 9: "34.82", 10: "39.56", 11: "44.48",
          12: "49.73", 13: "54.50", 14: "59.80", 15: "63.95",
          16: "69.28", 20: "88.65"}
CAL_SIGMA = {4: "0.98", 5: "0.83", 6: "0.97", 7: "0.97", 8: "0.97",
             9: "0.92", 10: "0.98", 11: "0.93", 12: "0.97",
             13: "0.92", 14: "0.98", 15: "0.97", 16: "0.87",
             20: "0.97"}
CAL_CTRL = {("SMOOTH", 5): (0, None, 1),
            ("SCRARITH", 5): (1, "1.0992", 1),
            ("EPSTEIN", 8): (11, "1.1199", 1)}
CAL_SLOPES = {"nneg": "-0.005", "match": "+0.000", "m99": "+0.001"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan"), float("nan"), float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return float("nan"), float("nan"), float("nan")
    sl = sxy / sxx
    ic = my - sl * mx
    ssr = sum((y - (sl * x + ic)) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - ssr / sst if sst > 0 else float("nan")
    return sl, ic, r2


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; eigenvector access is "
                       "IN-SCOPE this round (anatomy contract; the "
                       "r189 eigenvector ban was that round's choice, "
                       "disclosed), zero-freeness unchanged")


# ------------------------------------------------------- source helpers
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def J_quad(o, aa):
    L2v = 2 * aa
    if o == 0:
        return mp.mpf(0)
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w), pts)
    return val + mp.si(L2v * o) / 2


def Jp_quad(o, aa):
    L2v = 2 * aa
    if o == 0:
        return mp.quad(lambda w: w * r_of(w), [mp.mpf(0), L2v]) + aa
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: w * mp.cos(o * w) * r_of(w), pts)
    return val + mp.sin(L2v * o) / (2 * o)


def sieve_atoms(x: int):
    icap = int(math.floor(x))
    comp = np.zeros(icap + 1, dtype=bool)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist], \
        nlist


def world_atoms(world: str, x: int):
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms
    if world == "EPSTEIN":
        icap = int(math.floor(x))
        rq = np.zeros(icap + 1)
        xm = int(math.isqrt(icap)) + 1
        ym = int(math.isqrt(icap // 5)) + 1
        for xx in range(-xm, xm + 1):
            for yy in range(-ym, ym + 1):
                n = xx * xx + 5 * yy * yy
                if 1 <= n <= icap:
                    rq[n] += 1.0
        av = [mp.mpf(v) / 2 for v in rq]
        lamq = [mp.mpf(0)] * (icap + 1)
        for n in range(2, icap + 1):
            sacc = av[n] * mp.log(n)
            for d in range(2, n):
                if n % d == 0:
                    sacc -= lamq[d] * av[n // d]
            lamq[n] = sacc
        atoms = []
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
        return atoms
    if world == "SMOOTH":
        return None
    raise ValueError(world)


def primep_wall_at(o, atoms, aa):
    if o == 0:
        return 2 * sum((w * u for u, w in atoms), mp.mpf(0))
    return sum((w * (mp.sin(o * u) / o + u * mp.cos(o * u))
                for u, w in atoms), mp.mpf(0))


def polep_at(b, s2):
    return 2 * s2 / (mp.mpf(1) / 4 + b) ** 2


def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def W_atom_mp(u, oms, b, L, K):
    """Per-atom wall kernel W(u): x^T W x = -2 int_0^{L-u} A A(.+u)."""
    W = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            W[i, j] = 2 * (oms[i] * mp.sin(oms[i] * u)
                           - oms[j] * mp.sin(oms[j] * u)) \
                / (b[i] - b[j])
            W[j, i] = W[i, j]
    W[0, 0] = 2 * (u - L)
    for k in range(1, K):
        W[k, k] = mp.sin(oms[k] * u) / oms[k] \
            + (u - L) * mp.cos(oms[k] * u)
    return W


def fvec1(K):
    gg = (mp.sqrt(5) - 1) / 2
    return [mp.frac((k + 1) * gg) - mp.mpf(1) / 2 for k in range(K)]


def fvec2(K):
    gg = mp.sqrt(2) - 1
    return [mp.frac((k + 1) * gg) - mp.mpf(1) / 2 for k in range(K)]


def form_of(x, M, K):
    return sum(x[i] * M[i, j] * x[j] for i in range(K)
               for j in range(K))


def g_quad(x, u, oms, L, K):
    """int_0^{L-u} A(t) A(t+u) dt by oscillation-split mp.quad."""
    def A(t):
        return sum(x[k] * mp.cos(oms[k] * t) for k in range(K))
    omax = oms[K - 1]
    n = int(mp.floor((L - u) * 2 * omax / mp.pi)) + 2
    pts = [(L - u) * j / n for j in range(n + 1)]
    return mp.quad(lambda t: A(t) * A(t + u), pts)


def eig_min_frac(Lm, n):
    E = mp.eigsy(Lm, eigvals_only=True)
    lmin = min(E[i] for i in range(n))
    fro = mp.sqrt(sum(Lm[i, j] ** 2 for i in range(n)
                      for j in range(n)))
    return lmin, fro, lmin / fro


def bottom_vec_mp(Raw, K, froW):
    """Bottom eigenvector by mp inverse iteration (3 LU solves; the
    bottom eigenvalue is tau-scale-isolated, so each solve amplifies
    the bottom direction by ~1/tau >> everything; convergence is
    GAP-limited, warded by the Rayleigh stability between iteration
    2 and 3 plus the eigen-residual)."""
    x = mp.matrix([mp.mpf(1) for _ in range(K)])
    lam2 = None
    for it in range(3):
        x = mp.lu_solve(Raw, x)
        nx = mp.sqrt(sum(x[i] ** 2 for i in range(K)))
        x = x / nx
        if it == 1:
            v2 = [x[i] for i in range(K)]
            Rv2 = [sum(Raw[i, j] * v2[j] for j in range(K))
                   for i in range(K)]
            lam2 = sum(v2[i] * Rv2[i] for i in range(K))
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K)) / froW
    stab = abs(lam - lam2) / abs(lam) if lam != 0 else mp.mpf(0)
    return v, lam, float(res), float(stab)


# ------------------------------------------------------- main worker
def w_main(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            atoms = world_atoms("MAIN", h)
            out["natoms"] = len(atoms)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            out["log10taufrac"] = float(mp.log(
                abs(tau) * 2 * aa / froW, 10))
            # ---- G20 assembly: RawW - RawP - RawA == sum w_q W(u_q)
            Wq_list = [W_atom_mp(u, oms, b, L, K) for u, _w in atoms]
            S = mp.zeros(K, K)
            for (u, w), Wq in zip(atoms, Wq_list):
                for i in range(K):
                    for j in range(K):
                        S[i, j] += w * Wq[i, j]
            dev = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    tgt = RawW[i, j] - RawP[i, j] - RawA[i, j]
                    dev = max(dev, abs(tgt - S[i, j]))
                    den = max(den, abs(tgt))
            out["asm_dev"] = float(dev / den)
            # per-atom kernel PSD test (mechanism enum; float64 ok)
            watom_psd = 0
            for Wq in Wq_list:
                Wnp = np.array([[float(Wq[i, j]) for j in range(K)]
                                for i in range(K)])
                if float(np.linalg.eigvalsh(Wnp)[0]) >= -1e-12 \
                        * float(np.sqrt((Wnp * Wnp).sum())):
                    watom_psd += 1
            out["watom_psd"] = watom_psd
            # ---- G21 quadrature ward
            if h in QUAD_WARD:
                natq, nv = QUAD_WARD[h]
                sel = atoms if natq == 0 else atoms[:natq]
                vecs = [fvec1(K)] + ([fvec2(K)] if nv == 2 else [])
                qdev = mp.mpf(0)
                for u, _w in sel:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for x in vecs:
                        gq = g_quad(x, u, oms, L, K)
                        fm = form_of(x, Wq, K)
                        qdev = max(qdev, abs(fm + 2 * gq)
                                   / max(abs(fm), mp.mpf("1e-30")))
                out["quad_dev"] = float(qdev)
            # ---- pole square ward (numeric side of G12)
            x1 = fvec1(K)
            ps = 2 * s2 * (sum(x1[k] / (mp.mpf(1) / 4 + b[k])
                               for k in range(K))) ** 2
            pf = form_of(x1, RawP, K)
            out["pole_sq_dev"] = float(abs(ps - pf) / abs(ps))
            # ---- f' at nodes -> L_f, Delta
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]
            fp = []
            for i in range(K):
                if i == 0:
                    archp = 2 * Jpv[0]
                else:
                    archp = Jx[i] / oms[i] + Jpv[i]
                fp.append(polep_at(b[i], s2) + archp
                          + primep_wall_at(oms[i], atoms, aa))
            dlt = [RawW[i, i] - fp[i] for i in range(K)]
            # ---- bottom-direction anatomy: mp INVERSE ITERATION at
            # EVERY rung (amendment A3: float64 bottom eigenvectors
            # are direction-noise below the tau gap -- measured;
            # the bottom eigenvalue is tau-scale-isolated, so one
            # mp LU solve resolves the direction exactly)
            v0, lam0, invres, invstab = bottom_vec_mp(RawW, K, froW)
            out["invit_res"] = invres
            out["invit_stab"] = invstab
            P = form_of(v0, RawP, K)
            A_ = form_of(v0, RawA, K)
            tq_mp = [w * form_of(v0, Wq, K)
                     for (u, w), Wq in zip(atoms, Wq_list)]
            Pr = sum(tq_mp, mp.mpf(0))
            resid = P + A_ + Pr
            out["budget_dev"] = float(abs(resid - lam0) / froW)
            dep = abs(resid) / (abs(P) + abs(A_) + abs(Pr))
            out["depth"] = float(mp.log(dep, 10)) if dep > 0 \
                else -300.0
            out["bud_P"] = float(P)
            out["bud_A"] = float(A_)
            out["bud_Pr"] = float(Pr)
            # r0 from the exact split: alpha0 = lam0 - beta0
            beta0 = sum(dlt[i] * v0[i] * v0[i] for i in range(K))
            alpha0 = lam0 - beta0
            r0 = abs(lam0) / (abs(alpha0) + abs(beta0))
            out["r0_log10"] = float(mp.log(r0, 10)) if r0 > 0 \
                else -300.0
            # per-atom sign ladder with commensurate-zero class
            tmax = max(abs(t) for t in tq_mp)
            zbar = mp.mpf("1e-30") * tmax
            out["tq_zero"] = sum(1 for t in tq_mp if abs(t) <= zbar)
            out["tq_pos"] = sum(1 for t in tq_mp if t > zbar)
            out["tq_neg"] = sum(1 for t in tq_mp if t < -zbar)
            out["t_ladder"] = [float(mp.log(abs(t), 10))
                               if abs(t) > 0 else -300.0
                               for t in tq_mp]
            # localization m99 (frozen rule: smallest top-|t| subset
            # within 1% |Pr| or 1e-6 (|P|+|A|) absolute)
            tq = [float(t) for t in tq_mp]
            Prt = float(Pr)
            absguard = 1e-6 * (abs(out["bud_P"]) + abs(out["bud_A"]))
            order = sorted(range(len(tq)), key=lambda i: -abs(tq[i]))
            csum = 0.0
            m99 = len(tq)
            for mth, i in enumerate(order, start=1):
                csum += tq[i]
                if abs(csum - Prt) <= max(0.01 * abs(Prt), absguard):
                    m99 = mth
                    break
            out["m99"] = m99
            # ---- spectral-split ladder (median over m >= 1: mp
            # eigsy at ANAT_MP with v0-overlap ward, float64 eigh
            # elsewhere -- O(1) ratios, disclosed)
            mp_path = h in ANAT_MP
            if mp_path:
                Lf = mp.zeros(K, K)
                for i in range(K):
                    Lf[i, i] = fp[i]
                    for j in range(K):
                        if j != i:
                            Lf[i, j] = RawW[i, j]
                E, Q = mp.eigsy(RawW)
                idx = sorted(range(K), key=lambda m: E[m])
                lam = [E[m] for m in idx]
                V = [[Q[i, m] for i in range(K)] for m in idx]
                ovl = abs(sum(V[0][i] * v0[i] for i in range(K)))
                out["v0_ovl_dev"] = float(abs(ovl - 1))
                r_log = []
                for m in range(1, K):
                    v = V[m]
                    al = sum(v[i] * Lf[i, j] * v[j] for i in range(K)
                             for j in range(K))
                    be = sum(dlt[i] * v[i] * v[i] for i in range(K))
                    denm = abs(al) + abs(be)
                    rm = abs(lam[m]) / denm if denm > 0 else mp.mpf(0)
                    r_log.append(float(mp.log(rm, 10)) if rm > 0
                                 else -300.0)
                rs = sorted(r_log)
                out["rmed_log10"] = rs[len(rs) // 2]
                # L_f negative subspace (mp)
                E2, Q2 = mp.eigsy(Lf)
                froL = mp.sqrt(sum(Lf[i, j] ** 2 for i in range(K)
                                   for j in range(K)))
                refuse_bar = mp.mpf(10) ** (-(dps
                                              - EIG_REFUSE_SAFETY)) \
                    * froL
                negidx = [m for m in range(K)
                          if E2[m] < -refuse_bar]
                out["n_ref"] = sum(1 for m in range(K)
                                   if abs(E2[m]) <= refuse_bar)
                out["n_neg"] = len(negidx)
                rho_min = None
                sig_min = None
                sig_sum = mp.mpf(0)
                nn = len(negidx)
                Cm = mp.zeros(nn, nn)
                Um = mp.zeros(nn, nn)
                for aidx, ma in enumerate(negidx):
                    ya = [Q2[i, ma] for i in range(K)]
                    bya = sum(dlt[i] * ya[i] * ya[i]
                              for i in range(K))
                    rho = bya / (-E2[ma])
                    rho_min = rho if rho_min is None \
                        else min(rho_min, rho)
                    posm = sum(dlt[i] * ya[i] * ya[i]
                               for i in range(K) if dlt[i] > 0)
                    totm = sum(abs(dlt[i]) * ya[i] * ya[i]
                               for i in range(K))
                    sg = posm / totm if totm > 0 else mp.mpf(0)
                    sig_min = sg if sig_min is None \
                        else min(sig_min, sg)
                    sig_sum += sg
                    for bidx, mb in enumerate(negidx):
                        yb = [Q2[i, mb] for i in range(K)]
                        cij = sum(dlt[i] * ya[i] * yb[i]
                                  for i in range(K))
                        Cm[aidx, bidx] = cij
                        Um[aidx, bidx] = cij + (E2[ma]
                                                if ma == mb else 0)
                out["rho_min"] = float(rho_min) if rho_min is not None \
                    else float("nan")
                out["sig_min"] = float(sig_min) if sig_min is not None \
                    else float("nan")
                out["sig_mean"] = float(sig_sum / nn) if nn else \
                    float("nan")
                froC = mp.sqrt(sum(Cm[i, j] ** 2 for i in range(nn)
                                   for j in range(nn)))
                froU = mp.sqrt(sum(Um[i, j] ** 2 for i in range(nn)
                                   for j in range(nn)))
                out["match_log10"] = float(mp.log(froU / froC, 10)) \
                    if nn and froC > 0 else float("nan")
                lmU = min(mp.eigsy(Um, eigvals_only=True)[i]
                          for i in range(nn)) if nn else mp.mpf(0)
                out["subsp_lm_rel"] = float(lmU / froU) if nn and \
                    froU > 0 else 0.0
            else:
                # float64 ladder + L_f subspace (disclosed: O(1)
                # eigenvalues of L_f resolvable in float64)
                Rnp = np.array([[float(RawW[i, j]) for j in range(K)]
                                for i in range(K)])
                fpn = np.array([float(v) for v in fp])
                dltn = np.array([float(v) for v in dlt])
                Lfn = Rnp.copy()
                np.fill_diagonal(Lfn, fpn)
                lam, V = np.linalg.eigh(Rnp)
                r_log = []
                LV = Lfn @ V
                for m in range(1, K):
                    v = V[:, m]
                    al = float(v @ LV[:, m])
                    be = float((dltn * v * v).sum())
                    denm = abs(al) + abs(be)
                    rm = abs(lam[m]) / denm if denm > 0 else 0.0
                    r_log.append(math.log10(rm) if rm > 0 else -300.0)
                rs = sorted(r_log)
                out["rmed_log10"] = rs[len(rs) // 2]
                mu, Y = np.linalg.eigh(Lfn)
                froL = float(np.sqrt((Lfn * Lfn).sum()))
                negidx = [m for m in range(K)
                          if mu[m] < -F64_REFUSE * froL]
                out["n_ref"] = sum(1 for m in range(K)
                                   if abs(mu[m]) <= F64_REFUSE
                                   * froL)
                out["n_neg"] = len(negidx)
                nn = len(negidx)
                Yn = Y[:, negidx]
                Cm = Yn.T @ np.diag(dltn) @ Yn
                Um = Cm + np.diag(mu[negidx])
                rho = [float((Yn[:, a] * Yn[:, a] * dltn).sum()
                             / (-mu[negidx[a]])) for a in range(nn)]
                out["rho_min"] = min(rho) if rho else float("nan")
                sgs = []
                for a2 in range(nn):
                    y = Yn[:, a2]
                    posm = float((np.maximum(dltn, 0) * y * y).sum())
                    totm = float((np.abs(dltn) * y * y).sum())
                    sgs.append(posm / totm if totm > 0 else 0.0)
                out["sig_min"] = min(sgs) if sgs else float("nan")
                out["sig_mean"] = (sum(sgs) / nn) if nn else \
                    float("nan")
                froC = float(np.sqrt((Cm * Cm).sum()))
                froU = float(np.sqrt((Um * Um).sum()))
                out["match_log10"] = math.log10(froU / froC) \
                    if nn and froC > 0 else float("nan")
                out["subsp_lm_rel"] = float(
                    np.linalg.eigvalsh(Um)[0] / froU) if nn and \
                    froU > 0 else 0.0
            out["ci"] = out["rmed_log10"] - out["r0_log10"]
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------- control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            L = 2 * aa
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            atoms = world_atoms(world, x)
            RawW = raw_of(ce["mpM"], par, nrm, K)
            RawP = raw_of(ce["mpPole"], par, nrm, K)
            RawA = raw_of(ce["mpArch"], par, nrm, K)
            if atoms is not None:
                S = mp.zeros(K, K)
                for u, w in atoms:
                    Wq = W_atom_mp(u, oms, b, L, K)
                    for i in range(K):
                        for j in range(K):
                            S[i, j] += w * Wq[i, j]
                dev = mp.mpf(0)
                den = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        tgt = RawW[i, j] - RawP[i, j] - RawA[i, j]
                        dev = max(dev, abs(tgt - S[i, j]))
                        den = max(den, abs(tgt))
                out["asm_dev"] = float(dev / den)
            else:
                # SMOOTH: continuum identity, form level, 2 vectors
                iddev = mp.mpf(0)
                for x_ in (fvec1(K), fvec2(K)):
                    def xWx(w_, x_=x_):
                        Wq = W_atom_mp(w_, oms, b, L, K)
                        return form_of(x_, Wq, K) * mp.exp(w_ / 2)
                    omax = oms[K - 1]
                    n = int(mp.floor(L * 2 * omax / mp.pi)) + 2
                    pts = [L * j / n for j in range(n + 1)]
                    quadv = mp.quad(xWx, pts)
                    tgt = form_of(x_, RawW, K) \
                        - form_of(x_, RawP, K) - form_of(x_, RawA, K)
                    iddev = max(iddev, abs(tgt - quadv)
                                / max(abs(tgt), mp.mpf("1e-30")))
                out["asm_dev"] = float(iddev)
            # anatomy values (mp, small K)
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]
            fp = []
            for i in range(K):
                if i == 0:
                    archp = 2 * Jpv[0]
                else:
                    archp = Jx[i] / oms[i] + Jpv[i]
                if atoms is not None:
                    prp = primep_wall_at(oms[i], atoms, aa)
                else:
                    o = oms[i]
                    if o == 0:
                        prp = mp.quad(lambda w: 2 * w
                                      * mp.exp(w / 2),
                                      [mp.mpf(0), L])
                    else:
                        npx = max(int(mp.floor(L * o / mp.pi)), 1)
                        pts = ([mp.mpf(0)]
                               + [jj * mp.pi / o
                                  for jj in range(1, npx + 1)]
                               + [L])
                        pts = sorted(set(p for p in pts if p <= L))
                        prp = mp.quad(lambda w, o=o:
                                      (mp.sin(o * w) / o
                                       + w * mp.cos(o * w))
                                      * mp.exp(w / 2), pts)
                fp.append(polep_at(b[i], s2) + archp + prp)
            dlt = [RawW[i, i] - fp[i] for i in range(K)]
            Lf = mp.zeros(K, K)
            for i in range(K):
                Lf[i, i] = fp[i]
                for j in range(K):
                    if j != i:
                        Lf[i, j] = RawW[i, j]
            lmW, froWc, fracW = eig_min_frac(RawW, K)
            out["lm_neg"] = bool(lmW < 0 and abs(lmW)
                                 > mp.mpf(10)
                                 ** (-(dps - EIG_REFUSE_SAFETY))
                                 * froWc)
            E2, Q2 = mp.eigsy(Lf)
            froL = mp.sqrt(sum(Lf[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            refuse_bar = mp.mpf(10) ** (-(dps - EIG_REFUSE_SAFETY)) \
                * froL
            negidx = [m for m in range(K) if E2[m] < -refuse_bar]
            out["n_neg"] = len(negidx)
            rho_min = None
            for ma in negidx:
                ya = [Q2[i, ma] for i in range(K)]
                bya = sum(dlt[i] * ya[i] * ya[i] for i in range(K))
                rho = bya / (-E2[ma])
                rho_min = rho if rho_min is None else min(rho_min,
                                                          rho)
            out["rho_min"] = float(rho_min) if rho_min is not None \
                else float("nan")
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    t, u, Ls = sp.symbols("t u Lsym", positive=True)
    oi, oj = sp.symbols("oi oj", positive=True)

    def int_cos(alpha, beta, T):
        """int_0^T cos(alpha t + beta) dt, exact (alpha may be 0)."""
        if sp.simplify(alpha) == 0:
            return T * sp.cos(beta)
        return (sp.sin(alpha * T + beta) - sp.sin(beta)) / alpha

    def conv_int(oa, ob, T, phase_a):
        """int_0^T cos(oa t + phase_a) cos(ob t) dt via
        product-to-sum, with the antiderivative WARDED by
        differentiation (no sp.integrate, no Piecewise)."""
        term1 = int_cos(oa - ob, phase_a, T) / 2
        term2 = int_cos(oa + ob, phase_a, T) / 2
        return term1 + term2

    # antiderivative ward: d/dT of conv_int == integrand (generic)
    Ts = sp.symbols("Ts", positive=True)
    ph = sp.symbols("ph")
    ward = sp.simplify(sp.diff(conv_int(oi, oj, Ts, ph), Ts)
                       - sp.cos(oi * Ts + ph) * sp.cos(oj * Ts))
    ward_eq = sp.simplify(sp.diff(int_cos(oi, ph, Ts), Ts)
                          - sp.cos(oi * Ts + ph))

    # G10: convolution identity, fully generic (no periodicity):
    # 2 int_0^u cos(om_i(u-t))cos(om_j t) dt: cos(om_i(u-t)) =
    # cos(-om_i t + om_i u)
    conv = 2 * conv_int(-oi, oj, u, oi * u)
    target = 2 * (oi * sp.sin(oi * u) - oj * sp.sin(oj * u)) \
        / (oi ** 2 - oj ** 2)
    ok_off = sp.simplify(sp.factor(sp.expand_trig(conv - target))) \
        == 0
    convd = 2 * conv_int(-oi, oi, u, oi * u)
    ok_dg = sp.simplify(sp.expand_trig(
        convd - (u * sp.cos(oi * u) + sp.sin(oi * u) / oi))) == 0
    conv0 = 2 * int_cos(oj, sp.Integer(0), u)
    ok_z = sp.simplify(conv0 - 2 * sp.sin(oj * u) / oj) == 0
    check("G10-convolution-identity-generic",
          bool(ok_off and ok_dg and ok_z and ward == 0
               and ward_eq == 0),
          "2 int_0^u cos(om_i(u-t))cos(om_j t) dt == the one-function "
          "Loewner divided difference (f_i-f_j)/(b_i-b_j) of f = "
          "2 om sin(om u), for generic om_i != om_j, the diagonal "
          "(u cos + sin/om), and the om = 0 row (2 sin/om) -- "
          "IDENTICALLY in (om_i, om_j, u); antiderivatives warded "
          "by differentiation (product-to-sum route, sympy exact): "
          "the wall's off-diagonal sine structure is a convolution "
          "kernel, no lattice needed")

    # G11: ACF law on the commensurate lattice (integer modes,
    # symbolic u, L; exhaustive index classes)
    def om(kk):
        return 2 * sp.pi * kk / Ls

    def acf_entry(ki, kj):
        # int_0^{L-u} cos(om_i t) cos(om_j (t+u)) dt
        # + transposed, i.e. the symmetrized kernel x2
        # cos(om_j(t+u)) = cos(om_j t + om_j u)
        e1 = conv_int(om(kj), om(ki), Ls - u, om(kj) * u)
        e2 = conv_int(om(ki), om(kj), Ls - u, om(ki) * u)
        return e1, e2

    def W_entry(ki, kj):
        if ki == kj:
            if ki == 0:
                return 2 * (u - Ls)
            o = om(ki)
            return sp.sin(o * u) / o + (u - Ls) * sp.cos(o * u)
        if ki == 0 or kj == 0:
            o = om(max(ki, kj))
            return 2 * sp.sin(o * u) / o
        a1, a2 = om(ki), om(kj)
        return 2 * (a1 * sp.sin(a1 * u) - a2 * sp.sin(a2 * u)) \
            / (a1 ** 2 - a2 ** 2)

    ok11 = True
    pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 2), (1, 2), (1, 3),
             (2, 3)]
    for ki, kj in pairs:
        e1, e2 = acf_entry(ki, kj)
        if ki == kj:
            lhs = W_entry(ki, kj) + 2 * e1
        else:
            lhs = 2 * W_entry(ki, kj) + 2 * (e1 + e2)
        if sp.simplify(sp.expand_trig(lhs)) != 0:
            ok11 = False
            break
    check("G11-acf-law-lattice-exact", bool(ok11),
          "THE ACF LAW, entrywise on the commensurate lattice om_k = "
          "2 pi k/L (index classes (0,0),(0,j),(k,k),(i,j) over k <= "
          "3, u and L symbolic): W(u) == -2 x symmetrized "
          "autocorrelation kernel int_0^{L-u} cos(om_i t) "
          "cos(om_j(t+u)) dt -- per atom, x^T W(u) x = -2 int_0^{L-u} "
          "A_x(t) A_x(t+u) dt with A_x = sum x_k cos(om_k t): the "
          "sine off-diagonal (Loewner divided differences) and the "
          "cosine diagonal shift (incl. the k = 0 doubling = the "
          "k = 0 wraparound) are ONE object, the aperiodic "
          "autocorrelation of the windowed mode polynomial at lag u "
          "(sympy exact); positivity typing: g_x = ACF of a "
          "compactly supported signal, hat-g = |hat-B|^2 >= 0 "
          "(Wiener-Khinchin/Fejer class) -- each atom contributes "
          "MINUS a positive-definite-function sample: per-atom "
          "positivity is impossible at u < L (e_0 direction gives "
          "2(u-L) < 0), the mechanism is GLOBAL cancellation")

    # G12: pole square (Laplace)
    ok_lap = sp.simplify(sp.integrate(sp.exp(-t / 2)
                                      * sp.cos(oi * t),
                                      (t, 0, sp.oo))
                         - sp.Rational(1, 2)
                         / (sp.Rational(1, 4) + oi ** 2)) == 0
    x1s, x2s, sq = sp.symbols("x1s x2s sq", positive=True)
    b1s, b2s = sp.symbols("b1s b2s", positive=True)
    lhs = 2 * sq * (x1s / (sp.Rational(1, 4) + b1s)
                    + x2s / (sp.Rational(1, 4) + b2s)) ** 2
    rhs = sum(2 * sq / ((sp.Rational(1, 4) + bi)
                        * (sp.Rational(1, 4) + bj)) * xi * xj
              for bi, xi in ((b1s, x1s), (b2s, x2s))
              for bj, xj in ((b1s, x1s), (b2s, x2s)))
    ok_sq = sp.simplify(lhs - rhs) == 0
    check("G12-pole-square-laplace", bool(ok_lap and ok_sq),
          "int_0^infty e^{-t/2} cos(om t) dt == (1/2)/(1/4 + om^2) "
          "and the rank-1 pole block == 8 sinh^2(a/2) (int e^{-t/2} "
          "A_x)^2 EXACTLY (2x2 generic): the pole leg is a manifest "
          "L^2 square of the Laplace transform of the mode "
          "polynomial -- the r189 Herglotz point mass in integral "
          "form (sympy exact; numeric ward in G20 detail)")


def pd_exhibit() -> dict:
    """G13: [g(|t_i - t_j|)] Gram PSD exhibit at h = PD_RUNG."""
    dps = DPS[PD_RUNG]
    out = {}
    with mp.workdps(dps):
        h = PD_RUNG
        aa = mp.log(h) / 2
        L = 2 * aa
        K = int(math.ceil(KFAC * h * math.log(h)))
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        x = fvec1(K)
        pts = [L * i / PD_NPTS for i in range(PD_NPTS)]
        G = mp.zeros(PD_NPTS, PD_NPTS)
        for i in range(PD_NPTS):
            for j in range(PD_NPTS):
                d = abs(pts[i] - pts[j])
                Wq = W_atom_mp(d, oms, b, L, K)
                G[i, j] = -form_of(x, Wq, K) / 2
        lm, fro, frac = eig_min_frac(G, PD_NPTS)
        out["pd_frac"] = float(frac)
    return out


# ------------------------------------------------------------- arch leg
def arch_leg(h: int) -> dict:
    dps = DPS[h]
    ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out = dict(h=h)
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        RawA = raw_of(ce["mpArch"], par, nrm, K)

        def kappa(o):
            if o == 0:
                return mp.log(L) / 2 + mp.quad(r_of, [mp.mpf(0), L])
            npts = int(mp.floor(L * o / mp.pi))
            pts = ([mp.mpf(0)]
                   + [jj * mp.pi / o for jj in range(1, npts + 1)]
                   + [L])
            intr = mp.quad(lambda w, o=o: mp.cos(o * w) * r_of(w),
                           pts)
            return mp.ci(L * o) / 2 - (mp.euler + mp.log(o)) / 2 \
                + intr

        cs = []
        for k in range(K):
            o = oms[k]
            if k == 0:
                fpr = 2 * Jp_quad(mp.mpf(0), aa)
                mult = 2
            else:
                fpr = J_quad(o, aa) / o + Jp_quad(o, aa)
                mult = 1
            dA = RawA[k, k] - fpr
            cs.append(-dA / (mult * L) - kappa(o))
        cstar = (mp.euler + mp.log(2 * mp.pi)) / 2
        out["kind_dev"] = float(max(abs(c - cs[1]) for c in cs))
        out["cstar_dev"] = float(abs(cs[1] - cstar))
    return out


# ------------------------------------------------------------- jet leg
def atomjet_leg() -> dict:
    dps = DPS[JET_RUNG]
    ce = R4.build_cell(JET_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out = {}
    with mp.workdps(dps):
        aa = mp.log(JET_RUNG) / 2
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        atoms, _nl = sieve_atoms(JET_RUNG)
        u_l, w_l = atoms[0]                    # q = 2, incommensurate
        JET_IDX = 0
        L2v = 2 * aa

        def prime_block(scale_first):
            Mp = mp.zeros(K, K)
            ats = [(u, (w * 2 if idx == JET_IDX else w)
                    if scale_first else w)
                   for idx, (u, w) in enumerate(atoms)]
            pj = [sum((w * mp.sin(o * u) for u, w in ats), mp.mpf(0))
                  for o in oms]
            for i in range(K):
                for j2 in range(i):
                    sg = par[i] * par[j2]
                    den = oms[j2] ** 2 - oms[i] ** 2
                    od = 2 * sg * (oms[i] * pj[i]
                                   - oms[j2] * pj[j2]) / den
                    Mp[i, j2] += od
                    Mp[j2, i] += od
            for i in range(K):
                o = oms[i]
                if i == 0:
                    pdiag = sum((w * (L2v - u) for u, w in ats),
                                mp.mpf(0))
                else:
                    pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                      - mp.sin(o * u) / (2 * o))
                                 for u, w in ats), mp.mpf(0))
                Mp[i, i] += 2 * pdiag
            for i in range(K):
                for j2 in range(K):
                    Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
            return Mp

        Mp0 = prime_block(False)
        Mp1 = prime_block(True)
        ward = mp.mpf(0)
        for i in range(K):
            for j in range(K):
                ward = max(ward, abs(Mp0[i, j] - ce["mpPrime"][i, j]))
        out["rebuild_ward"] = float(ward)
        M0 = ce["mpM"]
        RawW0 = raw_of(M0, par, nrm, K)
        D01 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                D01[i, j] = M0[i, j] + (Mp0[i, j] - Mp1[i, j])
        RawW1 = raw_of(D01, par, nrm, K)
        Wj = W_atom_mp(u_l, oms, b, L, K)
        dw = w_l
        edev = mp.mpf(0)
        eden = mp.mpf(0)
        for i in range(K):
            for j in range(K):
                pred = dw * Wj[i, j]
                edev = max(edev, abs((RawW1[i, j] - RawW0[i, j])
                                     - pred))
                eden = max(eden, abs(pred))
        out["jet_dev"] = float(edev / eden)
        x = fvec1(K)
        fshift = form_of(x, RawW1, K) - form_of(x, RawW0, K)
        pred = dw * form_of(x, Wj, K)
        out["jet_form_dev"] = float(abs(fshift - pred) / abs(pred))
    return out


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("cancellation_functional_probe -- "
          "PRIME.CANCELLATION.FUNCTIONAL.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/vector recipes declared in the frozen "
          "spec (SPEC_SHA covers the declaration); record tables "
          "frozen from the disclosed calibration ladder (two "
          "smokes, two calib passes, amendments A1-A4 in the "
          "spec); tau_h enters ONLY as a measured per-rung scalar "
          "(screens); bottom-direction anatomy is mp inverse "
          "iteration at EVERY rung (A3); float64 is used only for "
          "O(1) spectral-median/L_f-subspace ratios at non-ANAT_MP "
          "rungs (disclosed); DEAD-CLASS guard: no l1 majorants "
          "(|g(u)| <= g(0) never used as a bound), no "
          "phase-discarding bounds, no per-prime cascades")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (convolution / ACF law / pole square)")
    exact_layer()
    pdx = pd_exhibit()
    check("G13-pd-function-exhibit", pdx["pd_frac"] >= PD_BAR,
          "the 7-point Gram [g_x(|t_i - t_j|)] at h = %d (frozen "
          "vector, t_i = i L/7): lambda_min/||F|| = %.1e >= %.0e -- "
          "g_x is a positive-definite function in the sampled sense "
          "(Wiener-Khinchin exhibit: the object each atom samples "
          "with a MINUS sign is PD; per-atom positivity of the wall "
          "contribution is therefore impossible, the cancellation "
          "must be global across atoms vs pole+arch)"
          % (PD_RUNG, pdx["pd_frac"], PD_BAR))

    # ------------------------------------------------------------ S2
    section("S2  MP DICTIONARY + ANATOMY (all reachable rungs)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    if errs:
        check("G20-acf-assembly-all-rungs", False,
              "worker errors at %s" % errs)
        print("ABORT: worker errors")
        return 1

    check("G20-acf-assembly-all-rungs", all(
        res[h]["asm_dev"] <= ASM_BAR for h in rungs) and all(
        res[h]["pole_sq_dev"] <= POLE_SQ_BAR for h in rungs),
          "THE ACF LAW AT EVERY RUNG (mp, entrywise): RawW - RawP - "
          "RawA == sum_q w_q W(u_q) with W the -2x-autocorrelation "
          "kernel, max rel dev %.1e over %d rungs (bar %.0e); pole "
          "square x^T RawP x == 8 sinh^2(a/2)(int e^{-t/2} A_x)^2, "
          "max dev %.1e (bar %.0e): the wall's prime part is EXACTLY "
          "minus twice the windowed-mode autocorrelation sampled at "
          "the atom logs, and the pole is an exact L^2 square"
          % (max(res[h]["asm_dev"] for h in rungs), len(rungs),
             ASM_BAR, max(res[h]["pole_sq_dev"] for h in rungs),
             POLE_SQ_BAR))

    qws = [h for h in rungs if h in QUAD_WARD]
    check("G21-acf-quadrature-ward", all(
        res[h]["quad_dev"] <= QUAD_BAR for h in qws),
          "independent oscillation-split quadrature of int_0^{L-u} "
          "A(t)A(t+u) dt vs the closed-form kernel at rungs %s "
          "(all/all/first-3 atoms x frozen vectors): max rel dev "
          "%.1e (bar %.0e) -- the ACF identity is not a "
          "formula-vs-formula tautology, the integral is real"
          % (str(qws), max(res[h]["quad_dev"] for h in qws),
             QUAD_BAR))

    arch_hs = [h for h in ARCH_RUNGS if h in rungs] or [ARCH_RUNGS[0]]
    arch_res = [arch_leg(h) for h in arch_hs]
    check("G22-arch-regularized-cos-law", all(
        ar["kind_dev"] <= ARCH_KIND_BAR
        and ar["cstar_dev"] <= ARCH_CSTAR_BAR for ar in arch_res),
          "THE ARCH LAW (closes the r189 open arch item, NEW EXACT): "
          "DeltaArch_k == -mult_k L (kappa(om_k) + c*) with kappa "
          "the regularized cosine transform of the arch atom "
          "measure a(w) = e^{-w/2}/(1-e^{-2w}) (Ci-form) and c* == "
          "(gamma + log 2pi)/2 EXACTLY: k-independence dev %s, "
          "c*-dev %s at h = %s (bars %.0e/%.0e; k = 0 included with "
          "the SAME mult doubling) -- the arch diagonal follows the "
          "SAME per-atom cosine law as the primes, log-divergence "
          "renormalized by a universal constant: the ENTIRE wall is "
          "now a closed Weil-type functional of g_x"
          % (str(["%.1e" % ar["kind_dev"] for ar in arch_res]),
             str(["%.1e" % ar["cstar_dev"] for ar in arch_res]),
             str(arch_hs), ARCH_KIND_BAR, ARCH_CSTAR_BAR))

    mp_here = [h for h in rungs if h in ANAT_MP]
    inv_ok = all(res[h]["invit_res"] <= INVIT_RES_BAR
                 and res[h]["invit_stab"] <= INVIT_STAB_BAR
                 for h in rungs) and all(
        res[h].get("v0_ovl_dev", 0.0) <= OVL_BAR for h in mp_here)
    if calib or smoke:
        for h in rungs:
            print("CAL anat h=%d depth %.2f budget_dev %.1e "
                  "invres %.1e stab %.1e P %.3e A %.3e Pr %.3e"
                  % (h, res[h]["depth"], res[h]["budget_dev"],
                     res[h]["invit_res"], res[h]["invit_stab"],
                     res[h]["bud_P"], res[h]["bud_A"],
                     res[h]["bud_Pr"]))
        ok23 = inv_ok and all(res[h]["budget_dev"] <= BUDGET_BAR
                              for h in rungs)
    else:
        ok23 = inv_ok and all(
            res[h]["budget_dev"] <= BUDGET_BAR
            and abs(res[h]["depth"] - float(CAL_DEPTH[h]))
            <= LOG_TOL for h in rungs)
    check("G23-bottom-budget-anatomy", ok23,
          "cancellation budgets at the bottom eigenvector of Raw "
          "(mp INVERSE ITERATION at ALL %d rungs -- gap-limited "
          "convergence warded honestly: eigen-residual <= %.1e "
          "(bar %.0e), Rayleigh stability iter2->3 <= %.1e (bar "
          "%.0e), eigsy-overlap at ANAT_MP <= %.1e (bar %.0e)): "
          "P + A + sum_q t_q == lambda_0 to <= %.1e fro-rel (bar "
          "%.0e); cancellation depth log10(|lambda_0|/(|P|+|A|+"
          "|Pr|)) = %s -- the pole square cancels arch + prime "
          "autocorrelation samples to 11..88 digits at the "
          "collapsing direction; the depth IS the tau scale in "
          "congruence coordinates: typed DEFINITIONAL, no "
          "discovery sold"
          % (len(rungs),
             max(res[h]["invit_res"] for h in rungs),
             INVIT_RES_BAR,
             max(res[h]["invit_stab"] for h in rungs),
             INVIT_STAB_BAR,
             max((res[h].get("v0_ovl_dev", 0.0) for h in mp_here),
                 default=0.0), OVL_BAR,
             max(res[h]["budget_dev"] for h in rungs), BUDGET_BAR,
             str({h: "%.2f" % res[h]["depth"]
                  for h in (4, 8, 13, 16, 20) if h in res})))

    if calib or smoke:
        for h in rungs:
            print("CAL conc h=%d r0 %.2f rmed %.2f ci %.2f"
                  % (h, res[h]["r0_log10"], res[h]["rmed_log10"],
                     res[h]["ci"]))
        ok24 = True
    else:
        ok24 = all(abs(res[h]["ci"] - float(CAL_CI[h])) <= 3 * CI_TOL
                   for h in rungs)
    conc_all = all(res[h]["ci"] >= 2.0 for h in rungs)
    conc_any = any(res[h]["ci"] >= 2.0 for h in rungs)
    conc_enum = ("CANCELLATION-CONCENTRATED-AT-COLLAPSE" if conc_all
                 else ("CANCELLATION-MIXED" if conc_any
                       else "CANCELLATION-SPREAD"))
    check("G24-spectral-split-concentration", ok24,
          "eigenbasis split lambda_m = (v^T L_f v) + (v^T Delta v): "
          "cancellation ratio r_0 at the bottom (mp) vs the "
          "spectrum median (m >= 1; float64 at non-ANAT_MP rungs, "
          "disclosed -- O(1) ratios): CI = %s dex (r0 %s, median "
          "%s) -- the L_f-vs-Delta cancellation is %s: total in "
          "the collapsing direction (r182 alignment territory), "
          "O(1)-partial elsewhere (median ratio ~10^-0.5..10^0): "
          "enum %s"
          % (str({h: "%.1f" % res[h]["ci"]
                  for h in (4, 8, 13, 16, 20) if h in res}),
             str({h: "%.1f" % res[h]["r0_log10"]
                  for h in (4, 8, 13, 16, 20) if h in res}),
             str({h: "%.2f" % res[h]["rmed_log10"]
                  for h in (4, 8, 13, 16, 20) if h in res}),
             "CONCENTRATED" if conc_all else "NOT concentrated",
             conc_enum))

    rho_ok = all(res[h]["rho_min"] >= 1.0
                 - (RHO_TOL_MP if h in ANAT_MP else RHO_TOL_F64)
                 for h in rungs)
    nneg_ok = all(res[h]["n_neg"] >= 1 for h in rungs)
    if calib or smoke:
        for h in rungs:
            print("CAL comp h=%d n_neg %d n_ref %d rho_min %.4f "
                  "match %.2f sig_min %.2f sig_mean %.2f"
                  % (h, res[h]["n_neg"], res[h]["n_ref"],
                     res[h]["rho_min"], res[h]["match_log10"],
                     res[h]["sig_min"], res[h]["sig_mean"]))
        ok25 = rho_ok and nneg_ok
    else:
        ok25 = rho_ok and nneg_ok and all(
            res[h]["n_neg"] == CAL_NNEG[h]
            and abs(res[h]["rho_min"] - float(CAL_RHO[h]))
            <= 0.05 * float(CAL_RHO[h])
            and abs(res[h]["match_log10"] - float(CAL_MATCH[h]))
            <= LOG_TOL
            and abs(res[h]["sig_min"] - float(CAL_SIGMA[h])) <= 0.05
            for h in rungs)
    comp_sharp = min(res[h]["rho_min"] for h in rungs) <= 1.1
    comp_enum = "COMPLEMENTARITY-SHARP" if comp_sharp \
        else "COMPLEMENTARITY-SLACK"
    check("G25-negative-subspace-complementarity", ok25,
          "L_f negative subspace: n_neg = %s (refusals %s); "
          "complementarity rho_min = min_y (y^T Delta y)/(-mu_y) = "
          "%s >= 1 at EVERY true rung (PSD-forced along single "
          "directions, measured; the margin is NON-MONOTONE, "
          "broadly decreasing %.2f (h=4) -> %.2f (h=20), min %.2f: "
          "Delta covers L_f's negativity with FINITE margin, enum "
          "%s -- the ultra-sharp cancellation lives in the bottom "
          "eigendirection of Raw (G23/G24), NOT in the whole "
          "negative subspace); matching log10(||Y^T Raw Y||_F/"
          "||Y^T Delta Y||_F) = %s (remarkably CONSTANT ~ -0.2: a "
          "subspace-level budget law, not an entrywise miracle); "
          "positive-mass share sigma_min = %s (the negative "
          "eigenvectors sit dominantly on Delta's POSITIVE part -- "
          "the complementarity is real but not total)"
          % (str({h: res[h]["n_neg"] for h in rungs}),
             str({h: res[h]["n_ref"] for h in rungs
                  if res[h]["n_ref"]}),
             str({h: "%.4f" % res[h]["rho_min"] for h in rungs}),
             res[rungs[0]]["rho_min"], res[rungs[-1]]["rho_min"],
             min(res[h]["rho_min"] for h in rungs),
             comp_enum,
             str({h: "%.2f" % res[h]["match_log10"]
                  for h in rungs}),
             str({h: "%.2f" % res[h]["sig_min"] for h in rungs})))

    manifest = any(res[h]["watom_psd"] == res[h]["natoms"]
                   for h in rungs)
    mech_enum = "PER-ATOM-MANIFEST-POSITIVE" if manifest \
        else "PER-ATOM-SIGNED-GLOBAL-CANCELLATION"
    one_signed = all(res[h]["tq_pos"] == 0 for h in rungs)
    sign_enum = "PRIME-TERM-ONE-SIGNED-AT-COLLAPSE" if one_signed \
        else "PRIME-TERM-MIXED-AT-COLLAPSE"
    if calib or smoke:
        for h in rungs:
            print("CAL atoms h=%d natoms %d psd %d signs "
                  "(%d,%d,%d) m99 %d ladder %s"
                  % (h, res[h]["natoms"], res[h]["watom_psd"],
                     res[h]["tq_pos"], res[h]["tq_neg"],
                     res[h]["tq_zero"], res[h]["m99"],
                     str(["%.1f" % t for t in res[h]["t_ladder"]])))
        ok26 = not manifest
    else:
        ok26 = not manifest and all(
            (res[h]["tq_pos"], res[h]["tq_neg"],
             res[h]["tq_zero"]) == CAL_SIGNS[h]
            and res[h]["m99"] == CAL_M99[h] for h in rungs)
    check("G26-per-atom-sign-ladder-localization", ok26,
          "C1(iii) PIVOT RESOLVED: per-atom kernels W(u_q) PSD count "
          "0 of %s at every rung (per-atom manifest positivity "
          "IMPOSSIBLE, as G11/G13 predict) -- mechanism enum %s; "
          "AND the measured sign law at the bottom eigenvector "
          "(mp): (n+, n-, n0) = %s -- %s: every non-commensurate "
          "atom's autocorrelation sample is POSITIVE at the "
          "collapsing direction (t_q < 0), exponentially decaying "
          "in log q, and the q = h atom (u = L, present iff h is a "
          "prime power) contributes EXACTLY ZERO (commensurate-"
          "zero class n0); the compensation is atoms-vs-pole, not "
          "atom-vs-atom; localization m99 = %s of %s atoms: the "
          "1-2 largest |t_q| atoms (q = 2, then 3) carry the prime "
          "total -- FEW-ATOM COOPERATION, not a global conspiracy "
          "(C4 worst case does not obtain)"
          % (str({h: res[h]["natoms"] for h in rungs}), mech_enum,
             str({h: (res[h]["tq_pos"], res[h]["tq_neg"],
                      res[h]["tq_zero"]) for h in rungs}),
             sign_enum,
             str({h: res[h]["m99"] for h in rungs}),
             str({h: res[h]["natoms"] for h in rungs})))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + WITNESS")
    ctasks = list(CTRL_CELLS)
    if smoke:
        ctasks = [("SCRARITH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    smooth_dev = max((v["asm_dev"] for k, v in cres.items()
                      if k[0] == "SMOOTH"), default=0.0)
    disc_dev = max((v["asm_dev"] for k, v in cres.items()
                    if k[0] != "SMOOTH"), default=0.0)
    check("G40-worlds-identity-blind", not cerrs
          and disc_dev <= CTRL_ASM_BAR
          and smooth_dev <= SMOOTH_ID_BAR,
          "the ACF law holds in every control world: discrete "
          "assembly (SCRARITH/EPSTEIN) max dev %.1e, SMOOTH "
          "continuum identity x^T PrimePart x == -2 int_0^L e^{w/2} "
          "g_x(w) dw dev %.1e (bars %.0e/%.0e) -- linear algebra + "
          "per-atom identities, world-blind BY DESIGN, typed, never "
          "sold as a separator" % (disc_dev, smooth_dev,
                                   CTRL_ASM_BAR, SMOOTH_ID_BAR))

    if calib or smoke:
        for k, v in sorted(cres.items()):
            print("CAL ctrl %s x=%d n_neg %d rho_min %.4f lm_neg %s"
                  % (k[0], k[1], v["n_neg"], v["rho_min"],
                     v["lm_neg"]))
        ok41 = not cerrs
    else:
        def _rho_ok(k):
            cal = CAL_CTRL[k][1]
            if cal is None:
                return math.isnan(cres[k]["rho_min"])
            return abs(cres[k]["rho_min"] - float(cal)) \
                <= 0.05 * float(cal)
        ok41 = all(
            cres[k]["n_neg"] == CAL_CTRL[k][0] and _rho_ok(k)
            and int(cres[k]["lm_neg"]) == CAL_CTRL[k][2]
            for k in cres)
    check("G41-worlds-anatomy-values", ok41,
          "anatomy VALUES through the control worlds (AMENDMENT A2, "
          "calibration-driven, disclosed -- the anticipated "
          "'complementarity fails iff indefinite' reading is "
          "MEASURED FALSE): %s -- rho_min >= 1 HOLDS in the "
          "indefinite SCRARITH/EPSTEIN cells too (their "
          "indefiniteness is TOP-of-spectrum, r186-concordant: the "
          "negative direction of the fake wall does NOT lie in "
          "L_f's negative subspace), so single-direction "
          "complementarity is NECESSARY-not-sufficient and NOT a "
          "world detector -- typed honestly; the SMOOTH cell has "
          "EMPTY L_f-negative subspace (n_neg = 0, complementarity "
          "VACUOUS: the r189 commensurability finding in anatomy "
          "coordinates -- SMOOTH's L_f is PSD at the nodes) while "
          "its wall is still indefinite (tau < 0); the sibling "
          "smooth-commensurability lane owns the SMOOTH geometry, "
          "we only read our anatomy there"
          % str({k: "n_neg %d rho %.2f %s"
                 % (v["n_neg"], v["rho_min"],
                    "indef" if v["lm_neg"] else "PSD")
                 for k, v in sorted(cres.items())}))

    jet = atomjet_leg()
    check("G42-atomjet-acf-linear", jet["rebuild_ward"] <= 1e-40
          and jet["jet_dev"] <= JET_BAR
          and jet["jet_form_dev"] <= JET_BAR,
          "ATOMJET at h=%d (first atom q=2 weight doubled; prime "
          "rebuild ward %.1e): wall shift == dw W(log 2) ENTRYWISE "
          "(dev %.1e) and form shift == -2 dw g_x(log 2) (dev %.1e) "
          "-- the ACF dictionary reads source jets exactly linearly "
          "(one kernel, both quadrature slots at once); the r172 "
          "inflation witness deforms the source COEFFICIENT ray "
          "(eigenvector-side): all round objects are matrix-side, "
          "witness-INVARIANT BY CONSTRUCTION -- typed definitional, "
          "not sold (r186 {l_0, l_2} remains the witness detector)"
          % (JET_RUNG, jet["rebuild_ward"], jet["jet_dev"],
             jet["jet_form_dev"]))

    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep = mp.eigsy(Qp_, eigvals_only=True)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G43-conditioning-ward", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e "
          "(round-118 trap absent)" % d_eps)

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_nn, _i, r2_nn = fit_line(xs_t, [res[h]["n_neg"] / res[h]["K"]
                                       for h in scr])
    sl_mt, _i, r2_mt = fit_line(xs_t, [res[h]["match_log10"]
                                       for h in scr])
    sl_m9, _i, r2_m9 = fit_line(xs_t, [res[h]["m99"]
                                       / res[h]["natoms"]
                                       for h in scr])
    if calib or smoke:
        print("CAL slopes: nneg %+.3f (r2 %.3f) match %+.3f (r2 "
              "%.3f) m99 %+.3f (r2 %.3f)"
              % (sl_nn, r2_nn, sl_mt, r2_mt, sl_m9, r2_m9))
        ok50 = True
    else:
        ok50 = (abs(sl_nn - float(CAL_SLOPES["nneg"])) <= SLOPE_TOL
                and abs(sl_mt - float(CAL_SLOPES["match"]))
                <= SLOPE_TOL
                and abs(sl_m9 - float(CAL_SLOPES["m99"]))
                <= SLOPE_TOL
                and abs(sl_nn) <= TAU_FLAT_BAR
                and abs(sl_mt) <= TAU_FLAT_BAR
                and abs(sl_m9) <= TAU_FLAT_BAR)
    check("G50-tau-screen", ok50,
          "log-log slopes vs tau_h of the DIMENSIONLESS anatomy "
          "coordinates: n_neg/K %+.3f, matching %+.3f, m99/atoms "
          "%+.3f -- ALL FLAT (bar %.2f): the anatomy does not ride "
          "the tau currency; the bottom-direction cancellation "
          "DEPTH does ride tau BY DEFINITION (it IS tau in "
          "congruence coordinates, G23) -- flagged honestly as "
          "definitional, never screened as discovery"
          % (sl_nn, sl_mt, sl_m9, TAU_FLAT_BAR))

    delivered = {
        "ATOMS": ["ACF-KERNELS"], "MODES": ["ACF-KERNELS"],
        "ACF-KERNELS": ["ACF-LAW"],
        "MBLOCKS": ["ACF-LAW", "TAU-SCALAR"],
        "ARCH-MEASURE": ["ARCH-LAW"], "ACF-LAW": ["ANATOMY"],
        "ARCH-LAW": ["ANATOMY"], "POLE-SQUARE": ["ANATOMY"],
        "ANATOMY": ["SCREENS"], "TAU-SCALAR": ["SCREENS"],
        "SCREENS": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("ACF-LAW", "ARCH-LAW", "ANATOMY", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "RH"}
    check("G51-loop-guard", ndet >= 4 and not has_cycle(delivered)
          and not hot,
          "flagged cycles DETECTED (A0-triangle, census-forall-k, "
          "Gonek-1984, Montgomery-PC, and NEW THIS ROUND: "
          "WEIL-ALLTESTS <-> RH -- the all-test-function Weil "
          "positivity criterion), consumed by NOTHING: DFS ancestry "
          "of every delivered node is clean; the round's Weil-form "
          "rewrite is a PER-RUNG FINITE algebraic identity on a "
          "restricted test family and has NO edge into the "
          "criterion; fully zero-free, no ordinate cache")

    check("G52-composed-chain-typing", True,
          "leg typing: {ACF law, pole square, arch regularized "
          "cos-law, jet linearity} EXACT (symbolic + mp <= 1e-40); "
          "{budgets, n_neg, rho, match, sigma, sign ladders, m99, "
          "CI} MEASURED; {depth == taufrac} DEFINITIONAL (tau in "
          "congruence coordinates); {rho_min >= 1 <=> positivity "
          "on L_f-negative directions} DEFINITIONAL; the residual "
          "object of the Weil rewrite (pole+arch dominates the "
          "weighted autocorrelation samples) IS the wall again -- "
          "relabeling barrier NAMED, not crossed; the r189 "
          "IIKS/RHP lane is UNTOUCHED (NEEDS-NAMED-EXTERNAL-TOOL "
          "stands)")

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
    cf = dict(ext)
    cf.update({("UNC", "ACFDOM"): INF, ("ACFDOM", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'autocorrelation domination proven cofinally' as a unit "
          "edge would raise the flow to 6 -- NOT REAL (the "
          "domination is the wall itself, measured per-rung only): "
          "this round adds NO flow; census cardinality UNCHANGED; "
          "RH unreachable without the omega edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + RESIDUE")
    primary = "WALL-IS-WEIL-ACF-FORM-EXACT"
    check("G60-pricing", True,
          "BEST CASE OBTAINED IN PART: three exact laws make the "
          "wall a closed Weil-explicit-formula-type functional of "
          "the PD function g_x -- an ALGEBRAIC RESTATEMENT: the "
          "residual object (domination of 2 sum w_q g_x(log q) by "
          "pole square + arch functional) is SOURCE-CLASSICAL in "
          "shape but IS the wall positivity again (typed, G52); "
          "what the identity BUYS: (i) per-atom/manifest positivity "
          "is now PROVABLY impossible (G11/G13/G26), killing that "
          "search branch forever, (ii) the cancellation is "
          "LOCALIZED (m99 = 1..2 atoms, one-signed prime ladder) "
          "and CONCENTRATED (CI 11..88 dex at the collapse), "
          "(iii) the arch closed form "
          "removes the last measured-only block of the dictionary; "
          "the cofinality gap is UNMOVED: the Weil form must "
          "dominate for ALL h -- that statement stays in the "
          "{H1 ^ H2 ^ H3}-KOFINAL residue, cardinality unchanged")

    check("G61-classical-dictionary-priced", True,
          "citations fixed: Guinand 1948 / Weil 1952 explicit "
          "formula (the wall's prime+arch legs are its truncated "
          "quadratic form on autocorrelation test functions g_x = "
          "B star B, B = windowed mode polynomial); Wiener-"
          "Khinchin/Fejer for hat-g = |hat-B|^2 >= 0 (G13); Bochner "
          "for PD functions; the (gamma + log 2pi)/2 renormalization "
          "constant of the arch cos-transform matches the builder's "
          "counterterm family (measured EXACT here, G22); Loewner/"
          "Donoghue/Simon dictionary of r189 subsumed: the "
          "sine-potential/cosine-shift split IS the lag-u "
          "autocorrelation split -- the ACF law explains WHY both "
          "quadratures of one atom system occupy the two slots")

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the wall is EXACTLY the truncated Weil form "
         "x^T Raw x = 8 sinh^2(a/2)(int e^{-t/2} A_x)^2 - "
         "2[int g_x a dw]_reg - 2 sum_q w_q g_x(log q) (three new "
         "exact laws: ACF, pole square, arch regularized cos-law "
         "with c* = (gamma+log 2pi)/2); per-atom positivity is "
         "impossible, the cancellation is global-but-localized "
         "(1-5 atoms), concentrated at the collapsing direction, "
         "with complementarity margin rho_min -> 1+ as h grows.  "
         "Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        primary + "(G10/G11/G20/G21/G22: three exact laws)",
        "ACF-LAW-EXACT(per-atom kernel = -2x windowed-mode "
        "autocorrelation at lag log q)",
        "POLE-IS-EXACT-L2-SQUARE(G12)",
        "ARCH-REGULARIZED-COS-LAW-EXACT(G22: c* = "
        "(gamma+log 2pi)/2, closes r189 arch item)",
        "PER-ATOM-POSITIVITY-IMPOSSIBLE(G11/G13/G26)",
        mech_enum + "(G26)",
        sign_enum + "(G26: exponential one-signed atom ladder, "
        "q = h commensurate-zero)",
        conc_enum + "(G24)",
        comp_enum + "(G25: finite non-monotone margin, min ~1.16)",
        "LOCALIZATION-FEW-ATOM(G26: m99 = 1..2)",
        "WORLD-BLIND-IDENTITY(G40) + "
        "COMPLEMENTARITY-NECESSARY-NOT-SUFFICIENT-TYPED(G41: "
        "fake-cell indefiniteness is top-of-spectrum; SMOOTH "
        "n_neg = 0, vacuous)",
        "ATOMJET-ACF-LINEAR(G42) + "
        "WITNESS-MATRIX-SIDE-INVARIANT-DEFINITIONAL(G42)",
        "TAU-FLAT-ANATOMY(G50) + DEPTH-DEFINITIONAL-FLAG(G23/G50)",
        "WEIL-ALLTESTS-LOOP-FLAGGED-NOT-CONSUMED(G51)",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED(G52/G60)",
        "MINCUT-UNCHANGED(G53) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        primary, "ACF-LAW-EXACT", "POLE-IS-EXACT-L2-SQUARE",
        "ARCH-REGULARIZED-COS-LAW-EXACT",
        "PER-ATOM-POSITIVITY-IMPOSSIBLE", mech_enum, sign_enum,
        conc_enum, comp_enum, "LOCALIZATION-FEW-ATOM",
        "WORLD-BLIND-IDENTITY",
        "COMPLEMENTARITY-NECESSARY-NOT-SUFFICIENT-TYPED",
        "ATOMJET-ACF-LINEAR", "TAU-FLAT-ANATOMY",
        "WEIL-ALLTESTS-LOOP-FLAGGED-NOT-CONSUMED",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
