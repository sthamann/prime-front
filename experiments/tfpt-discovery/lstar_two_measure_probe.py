#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lstar_two_measure_probe -- PRIME.PORT.LSTAR.
TWO_MEASURE_ANATOMY.01 (round 284): the TWO-MEASURE GEOMETRY of
the missing lemma L*.  r283 reduced the full free-window question
to ONE scalar inequality (L*: for every real polynomial p with
deg p < N_w, int p^2 dnu < int p^2 dmu, equivalently
lambda_max(E_{N_w}) < 1 with E the nu-dressed mu-CD kernel; margin
measured 1 - rho_184 = 1.68e-4, three eigenvalues above 0.995,
crossing exactly at minC+1 on all seven worlds, Gershgorin dead at
21).  THE NEW COORDINATE of this round: L* is a TWO-MEASURE
SUBORDINATION problem -- nu (104 atoms on w9) strictly
mu-subordinate (263 atoms) on polynomials up to degree N_w - 1.
THE STRUCTURALLY MOTIVATED MECHANISM CANDIDATE (the Nyquist /
shielding hypothesis, connecting the r276/r278 metric lane to L*):
polynomials of degree n have resolution scale ~ (hull length)/n;
as long as that resolution is COARSER than the nu-mu pairing scale
(every nu atom shielded by nearby mu atoms with enough mass), no
admissible p can isolate a nu atom -- the subordination holds
BECAUSE the degree is capped (exactly the half-filling meaning:
degree < S/2 cannot separate S atoms); it breaks when the
resolution reaches the pairing scale.  NOT a proof round: no L*
claim, no bound mechanism, no asymptotic law -- anatomy +
falsifiable crossing formula + honest typing.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r283 discipline): w = window (kz),
S = #union entries of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = builder depth = (S+1)//2, n = degree, minC =
first n with h_n < 0, crossing = minC + 1 (the r283 monotone-
loading theorem: lambda_max(E_n) crosses 1 exactly at minC+1 --
consumed as the crossing dictionary on the ladder WITHOUT
re-running spectra there; re-gated spectrally on w9 + all four
controls this round); f = fold index (union atoms sit EXACTLY on
the uniform theta grid theta_f = 2 pi f / L, f = 0..L/2, grid
step Dth = 2 pi / L -- the natural polynomial-resolution
coordinate: degree-n polynomials on x = cos theta are trigonometric
polynomials of degree n in theta with resolution cell
res(n) = pi / n).  Ground truth (minC, control flips, census
offsets, r283 spectral records) enters GATES and record tables
only; the sealed constructors consume split-source arrays (fold
indices, weights, comb data, L, D) ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall; atom classes via the
r254 world-blind integer root extraction ODG.base_exp).
MACHINERY IMPORTED VERBATIM: r283 FS.{split_channels,
mu_chain_f64, b_matrix_f64, mu_chain_mp, b_matrix_mp, rho_profile,
crossing_from_B}, r278 MS.ctx_build, r280 BL.{union_of_ctx,
sign_chain_f64}, v881 PIK.{folded_measure, build_rung,
lambda_eps}, r243 PB.smooth_comb, paircorr PC.{Grid, gen_model},
r254 ODG.base_exp, r244 BH.spearman, r274 WD.{stj_gen, pv_seq},
r230 JF.{TOY_NODES, TOY_WTS}, v563 core READ-ONLY.

LEG A -- THE TWO-MEASURE GEOMETRY (source-pure, pre-spectral):
(a1) w9 anatomy: which fold positions carry nu, which mu; r254
  labels (ARCH / K1 / KHI + primary p, admission bar 1e-9 on the
  matched comb atoms) for BOTH channels; THE PAIRING GEOMETRY:
  pairing step s_k = fold distance of nu atom k to the nearest mu
  atom, local gap g_k = fold distance to the nearest union atom
  of any sign, pairing ratio s_k / g_k; SHIELDING MASS: mu mass
  within R grid steps of each nu atom at the sealed radii
  R in {1, 2, 4, 8}, shield ratio q_k(R) = SM_k(R) / v_k;
  INTERLACING: per nu atom the number of mu atoms among its
  (existing) direct union neighbors, plus the adjacent nu-nu pair
  count (nu clustering census).
(a2) the SAME geometry on the four dead controls (EPST / SCR /
  SMOOTH / HL2, built verbatim through the r281 channel) -- the
  first question of the round: does the shielding geometry
  separate the worlds SOURCE-PURE, before any spectral
  computation?  Sealed scalar statistics K_G1 = median s,
  K_G2 = max s, K_G3 = min_k q_k(2), K_G4 = fraction of nu atoms
  with ALL existing neighbors mu; sealed r281 distance rule
  (MAIN_SEPARATING iff MAIN's value is farther from EVERY dead
  value than the dead spread, else WORLD_BLIND).
  SHIELDING_SEPARATES iff >= 1 of K_G1..K_G4 separates.

LEG B -- THE NYQUIST / RESOLUTION HYPOTHESIS (the core):
(b1) SEALED RESOLUTION CONVENTION (fixed at design time from the
  r283 record geometry L = 734, N_w = 184, S = 367 -- disclosed,
  not fitted): res(n) = pi / n on the theta hull [0, pi]; the
  pair cell of nu atom k is 2 s_k Dth (atom-to-shield DIAMETER);
  predicted crossing where res(n) = pair cell:
      n_pred(s) = L / (4 s).
  The all-adjacent case s == 1 predicts n_pred = L/4 = 183.5 ~
  N_w: THE HYPOTHESIS CONTENT IS that half-filling survival ==
  perfect pairing at grid scale, and early control death ==
  pairing scale of several grid steps.  Sealed pair-scale
  aggregates: MAX = max_k s_k, Q90 = v-weighted 0.9-quantile
  (smallest s with cum weight >= 0.9 sum), MED = median s.
  TEST on 42 frame-A rungs (h <= 900, r281 census channel,
  crossing = minC + 1 by the r283 theorem) + the four controls
  (crossing re-measured spectrally): NYQUIST_LAW iff some sealed
  aggregate holds |log2(n_pred / crossing)| <= 1.0 on ALL 46
  worlds; else NYQUIST_ORDERING iff some aggregate has
  spearman(n_pred, crossing) >= 0.75 over the 46 worlds; else
  NYQUIST_REFUTED (break loci printed).
(b2) THE CHRISTOFFEL QUANTIFICATION (the sharp local-resolution
  version; exact sandwich, each side gated): diag(E_n)_k =
  v_k K_n(y_k) = v_k / lambda_{mu,n}(y_k) (the exact per-atom
  Christoffel form: K_n = mu-CD kernel diagonal), hence
      max_k v_k K_n(y_k)  <=  lambda_max(E_n)  <=
      sum_k v_k K_n(y_k) = trace(E_n)  = the contract's
  Christoffel sum rho_n <= sum_k w_nu(x_k)/lambda_{mu,n}(x_k).
  Measured: n_CS = first n with trace >= 1 (the incoherent
  triangle-class crossing -- expected EARLY, Gershgorin died at
  21), n_DIAG = first n with max diag >= 1 (the pure single-atom
  isolation degree), true crossing in [n_CS, n_DIAG] (theorem);
  COHERENCE PROFILE at the sealed degrees (20, 40, 120, 184):
  gain_n = rho_n / maxdiag_n (the coherent assist over the best
  single atom -- the honest name for WHERE the crossing comes
  from: the nu atoms are coupled through the off-diagonal mu-CD
  kernel, the old cancellation story in the two-measure
  coordinate), slack_n = trace_n / rho_n (the incoherence loss of
  the triangle bound), r_eff = trace^2/||E||_F^2, offdiag
  Frobenius fraction.  On the controls the same range at their
  depth.
(b3) PAIRCORR DETECTOR on the leg-B statistics (sealed r281
  distance rule): B1 = n_CS, B2 = gain_20, plus the leg-A stats
  and C1 = participation ratio of the top eigenvector of E_20.

LEG C -- THE EXTREMAL VECTOR (the almost-subordination-breaking
polynomial): the top eigenvector w of E_{N_w} on w9 (mass profile
m_k = w_k^2 over the nu atoms):
(c1) WHERE it concentrates: participation ratio PR = 1/sum m^2,
  n_90 = #atoms for 90 percent mass, top-10 atom table (fold, u,
  label, primary p, v_k, s_k, q_k(2), m_k), overlap with the
  argmax-diag atom, spearman(m, v) and spearman(m, diag), the
  u-profile: mass-weighted mean u vs the v-weighted mean u; r278
  comparison (small primes carry): SMALLP enrichment factor
  F_sp = (mass share on atoms with primary p <= 13) / (v share),
  typed SMALLP_ENRICHED iff F_sp >= 1.5, SMALLP_DEPLETED iff
  <= 1/1.5, else SMALLP_NEUTRAL.
(c2) the controls at their crossing degree: THEIR breaking
  polynomial's top eigenvector -- PR, top-atom mass, argmax-diag
  overlap; typed contrast vs MAIN (PR ratio).
(c3) the BROAD saturation (three eigenvalues > 0.995): mass
  profiles of the top-3 eigenvectors of E_{N_w}; pairwise
  spearman of the mass profiles + top-20 support overlap; typed
  ONE_BAND iff median pairwise mass spearman >= 0.5 (structurally
  related modes on the same region -- orthogonal by oscillation),
  else INDEPENDENT_MODES.

LEG D -- WARDS / MUST-FAILS (each loud): E-construction gated
against the r283 route (w9: S = 367 / 263 / 104, N_w = 184, minC
= 184, crossing 185 == minC+1, rho records at n = 20/120/183/184/
185, margin 1.68e-4, top-5 eigenvalues, diag max 0.9700; fold
split bitwise == BL.union_of_ctx zones); mp ward (dps 60, chain +
B recomputed) on rho_184 / rho_185 (rel bar 1e-6; the 1.68e-4
margin needs precision care -- mp must confirm rho_184 < 1 <
rho_185); controls minC == flips 25/21/27/25 and spectral
crossing == flip+1 (26/22/28/26); 42-rung census regression
(anchors, offset distribution == r281, half-filling 42/42);
exact toys: (t1) synthetic grid toy (L = 32, mu folds {2, 3, 5}
weights {1, 1/2, 1/4}, nu folds {4, 8} weights {1/3, 1/9}) with
HAND-COMPUTED pairing/shield/interlace/Nyquist expectations gated
exactly; (t2) JF9 rational Christoffel cross-route: the monic
rational K_n (WD chain + pv_seq) must equal the f64 orthonormal
cumulative-row route to 1e-10 rel at every n <= S_+, sandwich +
crossing range gated on the toy (crossing 4 in [n_CS, n_DIAG]).
MUST-FAILS: (m1) WRONG GAP NORMALIZATION: the shielding/pairing
ratio computed in the x coordinate with a GLOBAL mean-gap
normalization must distort the profile LOUDLY (spread inflation
>= 5 vs the theta-grid ratio -- the metric of the hypothesis is
the theta grid, not x); (m2) CHRISTOFFEL WITHOUT WEIGHT: dropping
v_k from the Christoffel sum must break the exact trace identity
by >= 0.1 rel; (m3) EIGENVECTOR ORACLE: a mutant orienting the
extremal degree by the withheld crossing is FLAGGED by the AST
scope audit.  STOP LIST (anti-gates, binding): NO L* claim, NO
bound mechanism, NO asymptotic law, NO derived 5/7, NO triangle
bound as certificate, NO posthoc window, NO RH claim; r243..r283
stand.

SEALED CONSTANTS: MAINS (9, 13, 15); MINC_OFF {9: 0, 13: 2,
15: 1}; ANCHORS {9:0, 12:2, 13:2, 26:3, 40:1, 15:1, 52:0};
R281_DIST {0:18, 1:10, 2:6, 3:6, 4:1, 5:1}; CTRL_FLIPS
{EPST:25, SCR:21, SMOOTH:27}; HL2 seed 101 flip 25; H_CAP 900;
EXT 8 / EXT2 32; DEPTH_PAD 6; CTRL_DEPTH 40; SHIELD_RADII
(1, 2, 4, 8); WQ_Q 0.9; NYQ_BAND 1.0 (log2); SP_BAR 0.75;
ID_TOL 1e-12; SAND_TOL 1e-9; PROF_DEGS (20, 40, 120, 184);
R283_RHO {20: 0.47808, 120: 0.99898, 183: 0.99983, 184: 0.99983,
185: 1.00004} tol 1e-5 abs; R283_TOP5 (0.99983, 0.99874,
0.99597, 0.98461, 0.96408) tol 1e-4; MARGIN_REC 1.68e-4 rel tol
0.01; DIAGMAX_REC 0.9700 tol 5e-3; WARD_DPS 60; RHO_WARD_TOL
1e-6; EV_TOL 1e-10; TOPK 10; TOPSUP 20; BAND_SP 0.5; DET_DEG 20;
SMALLP (2, 3, 5, 7, 11, 13); SP_ENRICH 1.5; M1_BAR 5.0; M2_BAR
0.1; ADMIT 1e-9; TOY_L 32; toy christoffel bar 1e-10; runtime
<= 1800 s; smoke = toys + firewall + scopes + mutants + w9 f64
block (geometry, labels, christoffel, extremal); ladder,
controls, mp ward, detector and adjudication skipped.  PRE-SPEC
SCOPING (disclosed): the r283/r281/v956 record numbers (S counts,
minC offsets, flips, rho records) are consumed as sealed gate
anchors; the theta-resolution convention res(n) = pi/n with pair
cell 2 s Dth (hence n_pred = L/(4s)) was fixed at DESIGN TIME
from the published r283 record geometry -- the all-adjacent case
predicting the half-filling depth is the hypothesis content, not
a fit; no machinery pass preceded this spec except record
reading; no bar, band or typing rule was tuned after any
evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] SHIELDING_SEPARATES(separating stats) /
    SHIELDING_BLIND
  + [exactly one of] NYQUIST_LAW(aggregate; max band dev) /
    NYQUIST_ORDERING(best spearman) / NYQUIST_REFUTED(break loci)
  + CHRISTOFFEL_RANGE(n_CS, n_DIAG, crossing placement, coherence
    gain profile) [always]
  + EXTREMAL_ANATOMY(PR, concentration, control contrast,
    ONE_BAND / INDEPENDENT_MODES) [always]
  + DETECTOR_LEDGER [always].
Honesty before beauty: the geometry and the Christoffel sandwich
are ANATOMY of the open scalar L*, not a proof; a passing Nyquist
band is a falsifiable crossing FORMULA, not a mechanism theorem;
the coherence gain names where the triangle-class bounds lose
(the off-diagonal nu-nu coupling through the mu frame -- the old
cancellation story in the new coordinate); no verdict claims L*,
a bound mechanism, a derived 5/7 or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 28/30 -- ONE calibration
finding: the G10 toy HAND EXPECTATION miscounted the edge atom
(nu@8 has exactly ONE existing union neighbor, a mu atom, and the
sealed interlace rule counts EXISTING neighbors, so the all-mu
count is 2, not 1; the constructor was correct, the hand value
was corrected to the sealed convention); smoke pass 2 = 30/30
(0.2 s); calibration pass 1 = first full evaluation = 30/30, wall
5.8 s; after it THREE disclosed alignments, no bar, band, rule or
verdict rule moved: (a1) the code constant DIAGMAX_REC carried a
transcription slip (0.96952) and was aligned to the sealed
docstring/r283 print record 0.9700 (gate tol 5e-3 unchanged; both
values pass on the measured 0.97001); (a2) the G41 detail string
now prints the four control band devs (reporting only); (a3) the
ORDERING verdict detail carries the honesty clause on the trivial
N_w scaling (reporting only).  The post-freeze record run =
30/30, wall 5.6 s; run1/run2 identical up to WALL):
CAL_VERDICT = SHIELDING_BLIND + NYQUIST_ORDERING(MAX sp +0.998;
HONEST: carried by the trivial N_w scaling of the ladder -- the
mechanism-relevant discriminant, the four controls, FAILS the
band on every aggregate) + CHRISTOFFEL_RANGE(w9 n_CS = 10,
n_DIAG = 187, crossing 185; gain_Nw = 1.0307, slack_Nw = 50.2;
controls EPST (3, None, 26) / SCR (6, None, 22) / SMOOTH (28,
None, 28) / HL2 (6, None, 26)) + EXTREMAL_ANATOMY(PR 1.89, n90
2, argmax-diag mass 0.625, SMALLP_DEPLETED, ctrl PR 4.97..9.72,
ONE_BAND) + DETECTOR_LEDGER(ALL SEVEN sealed stats WORLD_BLIND).
Key numbers.  W9 GEOMETRY: occupancy 367/368 fold slots (only
f = 0 empty, the theta = 0 weight vanishes); labels mu 263 =
ARCH 178 + K1 71 + KHI 14, nu 104 = ARCH 78 + K1 19 + KHI 7
(admission dev 4.5e-16) -- the nu channel carries 26 comb-tent
folds (net-negative after background subtraction) and 78
background folds; PAIRING: s_k == 1 for ALL 104 nu atoms
(perfect grid-adjacent shielding), local gap 1, ratio 1;
interlacing 100/104 nu atoms with ALL existing neighbors mu, 2
adjacent nu-nu pairs; shield ratios q(1) med 6.73 / min 1.76,
q(2) med 11.9 / min 1.76, q(4) med 23.4 / min 2.82, q(8) med
51.3 / min 4.58.  CONTROLS (same channel): EPST mu/nu 226/141,
s max 2, q2 min 0.685, fullfrac 0.794, nu-nu 16; SCR 273/94,
s max 3, q2 min 0.0, fullfrac 0.351, nu-nu 38; SMOOTH 361/6,
s max 1, q2 min 0.902, fullfrac 1.000, nu-nu 0; HL2 279/88,
s max 2, q2 min 1.05, fullfrac 0.602, nu-nu 19.  SHIELDING
ADJUDICATION: all four sealed geometry stats WORLD_BLIND (the
dead spread swallows MAIN everywhere; SMOOTH sits on MAIN's side
of every stat) => SHIELDING_BLIND: the near-perfect interlacing
is a BUILDER-CHANNEL property (tent + FFT + fold), not the
arithmetic -- the support geometry cannot carry the wall,
consistent with r283 (metric, not combinatorial) and r276
(support exactness matters through the WEIGHTS).  NYQUIST: band
holds on 42/42 rungs (s == 1 and L/4 ~ N_w make the rung
predictions land near minC+1 by construction) and FAILS on all
four controls under every aggregate (MAX devs EPST 1.82 / SCR
1.48 / SMOOTH 2.71 / HL2 1.82 octaves; maxdev MED/Q90 3.06@SCR)
=> the sealed law is NOT awarded; spearman +0.998/+0.987/+0.987
>= 0.75 fires the sealed ORDERING typing, with the honesty
clause: the controls die at 22..28 DESPITE near-perfect pairing
(s <= 3) -- the support-geometry form of the resolution
hypothesis is refuted where it matters; no support-density-
corrected variant was explored (would be posthoc).  CHRISTOFFEL
(w9, the round's core finding): n_CS = 10 (trace crosses 1
early, triangle-class as inherited), n_DIAG = 187 -- the pure
single-atom isolation bound reaches 1 only TWO degrees above the
true crossing 185: MAIN's wall crossing is a NEAR-SINGLE-ATOM
Christoffel event (gain profile rho/maxdiag = 5.25 / 2.74 / 1.39
/ 1.0307 at n = 20/40/120/184 -- the coherent assist shrinks to
3.1 percent at the wall; slack trace/rho = 50.2 at N_w: the
aggregate nu coherence is DESTRUCTIVE, the old cancellation
story in the two-measure coordinate; r_eff 72.5 of 104, offdiag
Frobenius fraction 0.277 at N_w); THE CONTROL CONTRAST: on all
four dead worlds n_DIAG is NOT reached by their crossing depth
(their maxdiag stays far below 1) -- control death is a
COLLECTIVE mode far below the single-atom degree, while MAIN
rides the single-atom edge to the last free degree.  EXTREMAL
(w9): PR = 1.89, n_90 = 2 of 104 -- the near-breaking direction
is 99.7 percent TWO atoms: folds 2 and 4 (u = 0.030 / 0.060,
x = +0.9999 / +0.9994, ARCH class, v ~ 4e-6, s = 1, q2 = 1.76 /
1.97 = the two WEAKEST-shielded nu atoms of the window), i.e.
the SHALLOW-u hull edge BELOW the first prime (u < log 2), not
the small primes: mass-weighted mean u = 0.04 vs v-weighted
3.28, spearman(m, diag) = +0.788, spearman(m, v) = -0.477,
argmax-diag atom (fold 2) carries 0.625; SMALLP_DEPLETED (13
smallp-labeled nu atoms hold 13.5 percent of v but 0.0 percent
of the extremal mass) -- the r278 small-prime CHAIN-sensitivity
profile and the extremal NEAR-NULL direction of E are different
coordinates, honestly typed; controls at their crossing are
MORE diffuse (PR 7.02 / 9.72 / 4.97 / 8.29, top mass 0.21..
0.25) -- MAIN's mode is the sharpest of the five worlds; TOP-3
BAND: eigs 0.99983 / 0.99874 / 0.99597, pairwise mass spearman
+1.00 each, top-20 support overlaps 19/19/20 => ONE_BAND (three
oscillatory modes of ONE shallow-edge band, orthogonal by
oscillation, not by region).  DETECTOR (sealed r281 distance
rule): ALL SEVEN stats WORLD_BLIND (K_G1 all 1.0; K_G2 MAIN 1 vs
1..3; K_G3 MAIN 1.76 above the dead 0..1.05 but dist 0.71 <
spread 1.05; K_G4 MAIN 0.962 inside 0.351..1.000; n_CS MAIN 10
inside 3..28; gain_20 MAIN 5.25 inside 2.95..6.19; PR_20 MAIN
9.20 inside 5.38..10.83) -- honest negative: the round's
separation lives in the RANGE STRUCTURE (n_DIAG placement,
extremal sharpness), not in any sealed scalar.  MUST-FAILS: m1
spread inflation 233.6 >= 5 LOUD; m2 unweighted-Christoffel dev
1.0e+05 >= 0.1 LOUD; m3 flagged by the scope audit; constructors
+ fragment audit CLEAN.  MP WARD (dps 60): rho_184 = 0.99983248
< 1 < 1.00003660 = rho_185, rel devs 8.9e-14 / 1.6e-13 (bar
1e-6); w9 margin re-measured 1.6752e-4 (r283 print 1.68e-4, rel
dev 0.3 percent, inside the sealed 1 percent).  LADDER: 42
rungs, offset distribution == r281 {0:18, 1:10, 2:6, 3:6, 4:1,
5:1}, anchors exact, half-filling 42/42.  Runtime 5.6 s full /
0.2 s smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE.

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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import budget_localization_probe as BL           # noqa: E402 r280
import metric_stability_probe as MS              # noqa: E402 r278
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import paircorr_margin_probe as PC               # noqa: E402
import offdiag_gram_probe as ODG                 # noqa: E402 r254
import bordered_hankel_probe as BH               # noqa: E402 r244
import wronskian_dictionary_probe as WD          # noqa: E402 r274
import jfraction_probe as JF                     # noqa: E402 r230
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAINS = (9, 13, 15)
MINC_OFF = {9: 0, 13: 2, 15: 1}
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
R281_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
H_CAP = 900
EXT = 8
EXT2 = 32
DEPTH_PAD = 6
CTRL_DEPTH = 40
SHIELD_RADII = (1, 2, 4, 8)
WQ_Q = 0.9
NYQ_BAND = 1.0
SP_BAR = 0.75
ID_TOL = 1e-12
SAND_TOL = 1e-9
PROF_DEGS = (20, 40, 120, 184)
R283_RHO = {20: 0.47808, 120: 0.99898, 185: 1.00004}
RHO_TOL = 1e-5
R283_TOP5 = (0.99983, 0.99874, 0.99597, 0.98461, 0.96408)
TOP5_TOL = 1e-4
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
DIAGMAX_REC = 0.9700
DIAGMAX_TOL = 5e-3
WARD_DPS = 60
RHO_WARD_TOL = 1e-6
EV_TOL = 1e-10
TOPK = 10
TOPSUP = 20
BAND_SP = 0.5
DET_DEG = 20
SMALLP = (2, 3, 5, 7, 11, 13)
SP_ENRICH = 1.5
M1_BAR = 5.0
M2_BAR = 0.1
ADMIT = 1e-9
TOY_L = 32
TOY_CHR_BAR = 1e-10

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
    return (not bad), ("NO zero/prime oracles; atom classes via the "
                       "r254 integer root extraction; the sealed "
                       "constructors consume split-source arrays "
                       "(fold indices, weights, comb, L, D) ONLY; "
                       "record counts, offsets and flips enter gates "
                       "and record tables only" if not bad
                       else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
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


CONSTRUCTORS = ("split_by_fold", "pair_geometry", "shield_profile",
                "interlace_census", "wquantile", "nyq_predictions",
                "atom_labels", "christoffel_rows", "top_eigvecs")
SCOPE_FORBIDDEN = {"ANCHORS", "MINC_OFF", "CTRL_FLIPS", "HL2_FLIP",
                   "R281_DIST", "minC_true", "sg_true", "offs_true",
                   "cross_true"}


def scope_audit(funcname):
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
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def split_by_fold(darm, L):
    """fold-resolved split source: (mu folds, mu weights, nu
    folds, nu weights, mu x, nu x) -- the SAME folded_measure
    calls as BL.union_of_ctx (gated bitwise there)."""
    xs, ws, ufp = PIK.folded_measure(darm, L, +1.0)
    ys, vs, ufn = PIK.folded_measure(darm, L, -1.0)
    return ufp, ws, ufn, vs, xs, ys


def pair_geometry(fp, fn):
    """pairing step s_k (fold distance nu -> nearest mu), local
    gap g_k (fold distance nu -> nearest union atom of any sign),
    ratio s_k/g_k -- pure fold-index geometry."""
    fps = np.sort(np.asarray(fp, np.int64))
    fu = np.sort(np.concatenate([fps, np.asarray(fn, np.int64)]))
    s = np.zeros(len(fn), np.int64)
    g = np.zeros(len(fn), np.int64)
    for k, f in enumerate(fn):
        i = int(np.searchsorted(fps, f))
        cand = []
        if i > 0:
            cand.append(f - fps[i - 1])
        if i < len(fps):
            cand.append(fps[i] - f)
        s[k] = min(cand)
        j = int(np.searchsorted(fu, f))
        cu = []
        if j > 0:
            cu.append(f - fu[j - 1])
        if j + 1 < len(fu):
            cu.append(fu[j + 1] - f)
        g[k] = min(cu)
    return s, g, s.astype(float) / g.astype(float)


def shield_profile(fp, wp, fn, vn, radii):
    """shield mass SM_k(R) = mu mass within R fold steps of nu
    atom k, and the shield ratio SM_k(R)/v_k, per sealed R."""
    o = np.argsort(fp)
    fps = np.asarray(fp, np.int64)[o]
    wps = np.asarray(wp, float)[o]
    cw = np.concatenate([[0.0], np.cumsum(wps)])
    out = {}
    for R in radii:
        lo = np.searchsorted(fps, np.asarray(fn) - R, side="left")
        hi = np.searchsorted(fps, np.asarray(fn) + R, side="right")
        sm = cw[hi] - cw[lo]
        out[R] = (sm, sm / np.asarray(vn, float))
    return out


def interlace_census(fp, fn):
    """per nu atom: (#existing direct union neighbors, #mu among
    them); plus the adjacent nu-nu pair count."""
    fps = set(int(f) for f in fp)
    fu = np.sort(np.concatenate([np.asarray(fp, np.int64),
                                 np.asarray(fn, np.int64)]))
    res = []
    for f in fn:
        j = int(np.searchsorted(fu, f))
        nb = []
        if j > 0:
            nb.append(int(fu[j - 1]))
        if j + 1 < len(fu):
            nb.append(int(fu[j + 1]))
        res.append((len(nb), sum(1 for b in nb if b in fps)))
    fns = np.sort(np.asarray(fn, np.int64))
    nunu = int(np.sum(np.diff(fns) == 1))
    return res, nunu


def wquantile(vals, wts, q):
    """sealed weighted quantile: smallest value (ascending sort)
    whose cumulative weight reaches q x total."""
    o = np.argsort(vals)
    v = np.asarray(vals, float)[o]
    w = np.asarray(wts, float)[o]
    cw = np.cumsum(w)
    idx = int(np.searchsorted(cw, q * cw[-1]))
    idx = min(idx, len(v) - 1)
    return float(v[idx])


def nyq_predictions(s, vn, L):
    """the sealed Nyquist crossing predictions n_pred = L/(4 s)
    for the three sealed pair-scale aggregates."""
    smax = float(np.max(s))
    smed = float(np.median(s))
    sq = wquantile(s, vn, WQ_Q)
    return {"MAX": L / (4.0 * smax), "MED": L / (4.0 * smed),
            "Q90": L / (4.0 * sq)}


def atom_labels(folds, D, uu, mm):
    """r254-style world-blind labels per union fold atom:
    (class 0 ARCH / 1 K1 / 2 KHI, primary p, admission dev) via
    tent matching to the comb and integer root extraction."""
    order = np.argsort(uu)
    uus = np.asarray(uu, float)[order]
    mms = np.asarray(mm, float)[order]
    out = []
    for f in folds:
        si = float(f) * D
        lo = int(np.searchsorted(uus, si - D, side="right"))
        hi = int(np.searchsorted(uus, si + D, side="left"))
        best_w, best = -1.0, None
        for t in range(lo, hi):
            v = 1.0 - abs(si - uus[t]) / D
            if v > 0.0 and abs(mms[t]) * v > best_w:
                best_w, best = abs(mms[t]) * v, t
        if best is None:
            out.append((0, 0, 0.0))
            continue
        n = int(round(math.exp(uus[best])))
        dev = abs(math.exp(uus[best]) - n) / max(n, 1)
        p, kk = ODG.base_exp(n)
        out.append((1 if kk == 1 else 2, int(p), float(dev)))
    return out


def christoffel_rows(B):
    """cumulative Christoffel rows: cum[k, n-1] = sum_{i<n}
    B[k,i]^2 = v_k K_n(y_k) = diag(E_n)_k -- the exact per-atom
    Christoffel diagonal; trace and maxdiag profiles follow by
    column aggregation."""
    return np.cumsum(B * B, axis=1)


def top_eigvecs(B, n, kk):
    """eigenvalues + top-kk eigenvectors of E_n = B_n B_n^T."""
    Bn = B[:, :n]
    ev, V = np.linalg.eigh(Bn @ Bn.T)
    return ev, V[:, -kk:][:, ::-1]


# ============== must-fail mutants
def mutant_gap_norm_x(xp, xn):
    """m1 MUST-FAIL: pairing ratio computed in the x coordinate
    with a GLOBAL mean-gap normalization (the wrong metric for
    the theta-grid hypothesis) -- must distort the profile."""
    xu = np.sort(np.concatenate([xp, xn]))
    gg = float(np.mean(np.diff(xu)))
    d = np.array([float(np.min(np.abs(np.asarray(xp) - y)))
                  for y in xn])
    return d / gg


def mutant_unweighted_cs(cum, vn):
    """m2 MUST-FAIL: the Christoffel sum WITHOUT the nu weights
    (sum_k K_n(y_k)) -- must break the exact trace identity."""
    return np.sum(cum / np.asarray(vn, float)[:, None], axis=0)


def mutant_eigvec_oracle(minC_true):
    """m3 MUST-FAIL: an 'extremal degree' oriented by the
    withheld crossing -- the scope audit must FLAG this."""
    return minC_true + 1


# ============== gate-side world material
def world_pack(tag, ctx, D):
    """union + truth chain + fold split + geometry inputs for one
    world (gate-side; constructors receive arrays only)."""
    xu, wu, zones = BL.union_of_ctx(ctx)
    N_ = ctx["N"]
    sg, lgh, rmg = BL.sign_chain_f64(xu, wu, N_ + EXT)
    mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    if mc is None:
        sg, lgh, rmg = BL.sign_chain_f64(xu, wu, N_ + EXT2)
        mc = next((n for n in range(len(sg)) if sg[n] < 0), None)
    fp, wp, fn, vn, xp, xn = split_by_fold(ctx["darm"], ctx["L"])
    return dict(tag=tag, N=N_, L=int(ctx["L"]), S=len(xu), D=D,
                Sp=len(fp), Sm=len(fn), xu=xu, wu=wu, zones=zones,
                sg=sg, minC=mc, fp=fp, wp=wp, fn=fn, vn=vn,
                xp=xp, xn=xn, uu=ctx["uu"], mm=ctx["mm"])


def geom_block(W):
    """gate-side geometry bundle for one world."""
    s, g, ratio = pair_geometry(W["fp"], W["fn"])
    sh = shield_profile(W["fp"], W["wp"], W["fn"], W["vn"],
                        SHIELD_RADII)
    inter, nunu = interlace_census(W["fp"], W["fn"])
    preds = nyq_predictions(s, W["vn"], W["L"])
    full = sum(1 for ne, nm_ in inter if ne > 0 and nm_ == ne)
    occ = W["Sp"] + W["Sm"]
    stats = dict(
        med_s=float(np.median(s)), max_s=float(np.max(s)),
        min_q2=float(np.min(sh[2][1])),
        full_frac=full / max(len(inter), 1))
    return dict(s=s, g=g, ratio=ratio, sh=sh, inter=inter,
                nunu=nunu, preds=preds, stats=stats, occ=occ)


def spectral_block(W, depth):
    """gate-side spectral bundle: mu chain, B, rho profile,
    christoffel rows, crossings."""
    al, sb, h0 = FS.mu_chain_f64(np.asarray(W["xp"]),
                                 np.asarray(W["wp"]), depth)
    B = FS.b_matrix_f64(al, sb, h0, np.asarray(W["xn"]),
                        np.asarray(W["vn"]), depth)
    cross, rho = FS.crossing_from_B(B, depth)
    cum = christoffel_rows(B)
    trace = np.sum(cum, axis=0)          # trace[n-1] = trace E_n
    maxd = np.max(cum, axis=0)           # maxd[n-1] = max diag E_n
    n_cs = next((n for n in range(1, depth + 1)
                 if trace[n - 1] >= 1.0), None)
    n_diag = next((n for n in range(1, depth + 1)
                   if maxd[n - 1] >= 1.0), None)
    return dict(B=B, rho=rho, cross=cross, cum=cum, trace=trace,
                maxd=maxd, n_cs=n_cs, n_diag=n_diag, depth=depth)


def dist_rule(tab, ctrls):
    """sealed r281 distance rule: MAIN_SEPARATING iff MAIN's
    value is farther from EVERY dead value than the dead spread."""
    vm = tab["MAIN"]
    vd = [tab[c] for c in ctrls
          if tab[c] is not None and math.isfinite(tab[c])]
    if vm is None or not vd:
        return "WORLD_BLIND"
    spread = max(vd) - min(vd)
    dm = min(abs(vm - v) for v in vd)
    return ("MAIN_SEPARATING" if (spread > 0 and dm >= spread)
            else "WORLD_BLIND")


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("lstar_two_measure_probe -- PRIME.PORT.LSTAR."
          "TWO_MEASURE_ANATOMY.01 (round 284)")
    print("SPEC_SHA %s   (r283 FS %s / r278 MS %s)"
          % (SPEC_SHA[:16], FS.SPEC_SHA[:16], MS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 f64 block; ladder, controls, mp ward, "
                        "detector, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the theta-grid resolution "
          "convention (res = pi/n, pair cell 2 s Dth, n_pred = "
          "L/(4s), fixed at design time from the published r283 "
          "geometry -- disclosed, not fitted), the three pair-scale "
          "aggregates, the shield radii, the geometry statistics, "
          "the distance rule, the Christoffel sandwich gates, the "
          "extremal statistics, every bar/tolerance, the mutants "
          "and the verdict form; the STOP list forbids any L* "
          "claim and any bound-mechanism claim")

    # ---------------- S1 toys
    section("S1  TOYS -- GRID GEOMETRY (exact) + JF9 CHRISTOFFEL")
    tg_mu = np.array([2, 3, 5], np.int64)
    tg_wmu = np.array([1.0, 0.5, 0.25])
    tg_nu = np.array([4, 8], np.int64)
    tg_wnu = np.array([1.0 / 3.0, 1.0 / 9.0])
    s_t, g_t, r_t = pair_geometry(tg_mu, tg_nu)
    sh_t = shield_profile(tg_mu, tg_wmu, tg_nu, tg_wnu,
                          SHIELD_RADII)
    int_t, nunu_t = interlace_census(tg_mu, tg_nu)
    pr_t = nyq_predictions(s_t, tg_wnu, TOY_L)
    full_t = sum(1 for ne, nm_ in int_t if ne > 0 and nm_ == ne)
    ok_geo = (list(s_t) == [1, 3] and list(g_t) == [1, 3]
              and list(r_t) == [1.0, 1.0]
              and abs(sh_t[1][0][0] - 0.75) < 1e-15
              and abs(sh_t[1][0][1] - 0.0) < 1e-15
              and abs(sh_t[4][0][1] - 0.25) < 1e-15
              and abs(sh_t[8][0][0] - 1.75) < 1e-15
              and abs(sh_t[8][0][1] - 1.75) < 1e-15
              and int_t == [(2, 2), (1, 1)] and full_t == 2
              and nunu_t == 0
              and abs(pr_t["MAX"] - TOY_L / 12.0) < 1e-12
              and abs(pr_t["MED"] - TOY_L / 8.0) < 1e-12
              and abs(pr_t["Q90"] - TOY_L / 12.0) < 1e-12)
    check("G10-toy-geometry", ok_geo,
          "SYNTHETIC GRID TOY (L = %d, mu folds {2,3,5} w {1,1/2,"
          "1/4}, nu folds {4,8} v {1/3,1/9}), every value HAND-"
          "COMPUTED: s = %s, g = %s, ratio = %s, shield masses "
          "R=1 (0.75, 0) / R=4 nu@8 0.25 / R=8 (1.75, 1.75), "
          "neighbor census (2,2)/(1,1) -> 2 all-mu (the sealed "
          "rule counts EXISTING neighbors; nu@8 is an edge atom "
          "with one neighbor), nu-nu adjacencies 0, "
          "n_pred MAX/MED/Q90 = %.3f/%.3f/%.3f (= L/12, L/8, "
          "L/12; the sealed Q90 sorts ascending and takes the "
          "smallest s with cum weight >= 0.9 total)"
          % (TOY_L, list(s_t), list(g_t), list(r_t), pr_t["MAX"],
             pr_t["MED"], pr_t["Q90"]))
    # JF9 rational christoffel cross-route
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    nodes9 = [t[0] for t in jf_pairs]
    wts9 = [t[1] for t in jf_pairs]
    xs_r = [x for x, w in zip(nodes9, wts9) if w > 0]
    ws_r = [w for w in wts9 if w > 0]
    ys_r = [x for x, w in zip(nodes9, wts9) if w < 0]
    vs_r = [-w for w in wts9 if w < 0]
    Sp_t = len(xs_r)
    alm, bem, hsm = WD.stj_gen(xs_r, ws_r, Sp_t - 1)
    vals = [WD.pv_seq(alm, bem, y, Sp_t - 1) for y in ys_r]
    al_f, sb_f, h0_f = FS.mu_chain_f64(
        np.array([float(x) for x in xs_r]),
        np.array([float(w) for w in ws_r]), Sp_t)
    B_t = FS.b_matrix_f64(al_f, sb_f, h0_f,
                          np.array([float(y) for y in ys_r]),
                          np.array([float(v) for v in vs_r]), Sp_t)
    cum_t = christoffel_rows(B_t)
    dev_chr = 0.0
    for n in range(1, Sp_t + 1):
        for k in range(len(ys_r)):
            exact = vs_r[k] * sum(vals[k][i] * vals[k][i] / hsm[i]
                                  for i in range(n))
            dev_chr = max(dev_chr,
                          abs(cum_t[k, n - 1] - float(exact))
                          / max(abs(float(exact)), 1e-300))
    tr_t = np.sum(cum_t, axis=0)
    md_t = np.max(cum_t, axis=0)
    _cr_t, rho_t = FS.crossing_from_B(B_t, Sp_t)
    ok_sand_t = all(md_t[n - 1] <= rho_t[n] + SAND_TOL
                    and rho_t[n] <= tr_t[n - 1] + SAND_TOL
                    for n in range(1, Sp_t + 1))
    n_cs_t = next((n for n in range(1, Sp_t + 1)
                   if tr_t[n - 1] >= 1.0), None)
    n_dg_t = next((n for n in range(1, Sp_t + 1)
                   if md_t[n - 1] >= 1.0), None)
    ok_rng_t = (n_cs_t is not None and n_cs_t <= 4
                and (n_dg_t is None or n_dg_t >= 4)
                and _cr_t == 4)
    check("G11-toy-christoffel", dev_chr <= TOY_CHR_BAR
          and ok_sand_t and ok_rng_t,
          "JF9 CROSS-ROUTE: the f64 orthonormal cumulative-row "
          "diagonal equals the exact rational monic route v_k "
          "sum pi_i(y_k)^2/h_i at EVERY n <= S_+ = %d, max rel "
          "dev %.1e (bar %.0e); sandwich maxdiag <= rho <= trace "
          "at every n; crossing range [n_CS, n_DIAG] = [%s, %s] "
          "contains the true crossing 4 (== minC+1, r283 record)"
          % (Sp_t, dev_chr, TOY_CHR_BAR, str(n_cs_t), str(n_dg_t)))

    # ---------------- S2 w9 machinery
    section("S2  W9 -- E-CONSTRUCTION GATED AGAINST THE r283 ROUTE")
    rr9 = core.build_window(9)
    D9 = float(rr9["D"])
    ctx9 = MS.ctx_build(9)
    W9 = world_pack("w9", ctx9, D9)
    xs_z, ws_z, ys_z, vs_z = W9["zones"]
    ok_zone = (np.array_equal(np.asarray(xs_z), np.asarray(W9["xp"]))
               and np.array_equal(np.asarray(ws_z),
                                  np.asarray(W9["wp"]))
               and np.array_equal(np.asarray(ys_z),
                                  np.asarray(W9["xn"]))
               and np.array_equal(np.asarray(vs_z),
                                  np.asarray(W9["vn"])))
    ok_src = (W9["S"] == 367 and W9["Sp"] == 263
              and W9["Sm"] == 104
              and W9["N"] == (W9["S"] + 1) // 2
              and W9["minC"] == W9["N"] + MINC_OFF[9])
    occ9 = W9["Sp"] + W9["Sm"]
    check("G20-w9-source-split", ok_src and ok_zone,
          "w9 FULL SOURCE: S = %d (mu %d / nu %d), N_w = %d == "
          "(S+1)//2, minC = %s == N_w + %d (record); the fold "
          "split is BITWISE the BL.union_of_ctx zone split; "
          "occupancy %d of %d fold slots (L = %d, slots 0..L/2)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"]),
             MINC_OFF[9], occ9, W9["L"] // 2 + 1, W9["L"]))
    depth9 = min(W9["N"] + DEPTH_PAD, W9["Sp"] - 1)
    SP9 = spectral_block(W9, depth9)
    rho9 = SP9["rho"]
    check("G21-w9-crossing", SP9["cross"] == W9["minC"] + 1,
          "lambda_max(E_n) crosses 1 at n = %s == minC + 1 = %d "
          "-- the r283 route reproduced exactly (the crossing "
          "dictionary this round consumes on the ladder)"
          % (str(SP9["cross"]), W9["minC"] + 1))
    E184 = SP9["B"][:, :W9["N"]] @ SP9["B"][:, :W9["N"]].T
    ev184 = np.linalg.eigvalsh(E184)
    top5 = ev184[-5:][::-1]
    margin9 = 1.0 - rho9[W9["N"]]
    dmax184 = float(SP9["maxd"][W9["N"] - 1])
    ok_rec = all(abs(rho9[n] - R283_RHO[n]) <= RHO_TOL
                 for n in R283_RHO)
    ok_top = all(abs(float(top5[i]) - R283_TOP5[i]) <= TOP5_TOL
                 for i in range(5))
    ok_mar = abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
    ok_dmx = abs(dmax184 - DIAGMAX_REC) <= DIAGMAX_TOL
    check("G22-w9-profile-regression", ok_rec and ok_top
          and ok_mar and ok_dmx and rho9[183] < 1.0
          and rho9[184] < 1.0,
          "r283 RECORDS REPRODUCED: rho_20/120/185 dev <= %.0e of "
          "%s; top-5 eigs %s == r283 within %.0e; margin 1 - "
          "rho_184 = %.4e (record %.2e, rel tol %.2f); diag max "
          "at N_w = %.5f (record %.5f)"
          % (RHO_TOL, str(R283_RHO),
             str([round(float(v), 5) for v in top5]), TOP5_TOL,
             margin9, MARGIN_REC, MARGIN_TOL, dmax184, DIAGMAX_REC))
    if smoke:
        check("G23-w9-mp-ward", True, "SMOKE: skipped")
    else:
        alm9, sbm9, h0m9 = FS.mu_chain_mp(
            np.asarray(W9["xp"]), np.asarray(W9["wp"]), depth9,
            WARD_DPS)
        B9m = FS.b_matrix_mp(alm9, sbm9, h0m9,
                             np.asarray(W9["xn"]),
                             np.asarray(W9["vn"]), depth9, WARD_DPS)
        devs = {}
        rho_mp = {}
        for n in (W9["N"], W9["N"] + 1):
            Bn = B9m[:, :n]
            rmp = float(np.linalg.eigvalsh(Bn @ Bn.T)[-1])
            rho_mp[n] = rmp
            devs[n] = abs(rmp - rho9[n]) / max(abs(rmp), 1e-300)
        ok_ward = (max(devs.values()) <= RHO_WARD_TOL
                   and rho_mp[W9["N"]] < 1.0
                   and rho_mp[W9["N"] + 1] > 1.0)
        check("G23-w9-mp-ward", ok_ward,
              "MP WARD (dps %d, chain + B recomputed): rho_184 = "
              "%.8f < 1 < %.8f = rho_185 at mp, rel devs %.1e / "
              "%.1e (bar %.0e) -- the 1.68e-4 margin is "
              "arbitration-safe"
              % (WARD_DPS, rho_mp[W9["N"]], rho_mp[W9["N"] + 1],
                 devs[W9["N"]], devs[W9["N"] + 1], RHO_WARD_TOL))

    # ---------------- S3 leg A geometry
    section("S3  LEG A -- TWO-MEASURE GEOMETRY (w9 + CONTROLS)")
    lab_mu = atom_labels(W9["fp"], D9, W9["uu"], W9["mm"])
    lab_nu = atom_labels(W9["fn"], D9, W9["uu"], W9["mm"])
    dev_adm = max([d for _c, _p, d in lab_mu + lab_nu
                   if _c != 0] or [0.0])
    cen_mu = {0: 0, 1: 0, 2: 0}
    cen_nu = {0: 0, 1: 0, 2: 0}
    for c, _p, _d in lab_mu:
        cen_mu[c] += 1
    for c, _p, _d in lab_nu:
        cen_nu[c] += 1
    check("G30-w9-labels", dev_adm <= ADMIT,
          "r254 LABELS (ARCH/K1/KHI, admission dev %.1e <= %.0e): "
          "mu %d = ARCH %d + K1 %d + KHI %d; nu %d = ARCH %d + "
          "K1 %d + KHI %d -- THE mu/nu STRUCTURE DISCLOSURE: "
          "which channel carries the comb-tent folds and which "
          "the background surplus"
          % (dev_adm, ADMIT, W9["Sp"], cen_mu[0], cen_mu[1],
             cen_mu[2], W9["Sm"], cen_nu[0], cen_nu[1], cen_nu[2]))
    GB9 = geom_block(W9)
    s9 = GB9["s"]
    q9 = {R: GB9["sh"][R][1] for R in SHIELD_RADII}
    info("w9 pairing: s med/max = %.0f/%.0f, gap med = %.0f, "
         "ratio med/max = %.2f/%.2f"
         % (np.median(s9), np.max(s9), np.median(GB9["g"]),
            np.median(GB9["ratio"]), np.max(GB9["ratio"])))
    for R in SHIELD_RADII:
        info("w9 shield ratio q(R=%d): med %.3g / min %.3g / "
             "max %.3g" % (R, np.median(q9[R]), np.min(q9[R]),
                           np.max(q9[R])))
    info("w9 interlacing: %d/%d nu atoms with ALL existing "
         "neighbors mu; %d adjacent nu-nu pairs"
         % (sum(1 for ne, nm_ in GB9["inter"]
                if ne > 0 and nm_ == ne), W9["Sm"], GB9["nunu"]))
    ok_struct = (bool(np.all(s9 >= 1))
                 and len(set(W9["fp"]) & set(W9["fn"])) == 0
                 and bool(np.all(np.asarray(W9["vn"]) > 0))
                 and bool(np.all(np.asarray(W9["wp"]) > 0)))
    check("G31-w9-pairing-geometry", ok_struct,
          "STRUCTURAL SANITY: mu/nu fold sets disjoint, all "
          "channel weights positive, s_k >= 1 everywhere; the "
          "pairing table and shield profiles printed above are "
          "the round's leg-A deliverable (stats: %s)"
          % str({k: round(v, 4) for k, v in GB9["stats"].items()}))
    if smoke:
        for g in ("G32-ctrl-geometry", "G33-shielding-adjudication"):
            check(g, True, "SMOKE: skipped")
        WC = {}
        GBC = {}
        shield_verdict = None
        geo_typ = {}
    else:
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        WC = {}
        GBC = {}
        ok_c = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            Wp = world_pack(cn, cctx, D9)
            WC[cn] = Wp
            GBC[cn] = geom_block(Wp)
            flip = CTRL_FLIPS.get(cn, HL2_FLIP)
            ok_c = ok_c and (Wp["minC"] == flip)
            st = GBC[cn]["stats"]
            info("%s: S=%d (mu %d/nu %d, occ %d/%d), minC=%s; "
                 "s med/max %.0f/%.0f, q2 med/min %.3g/%.3g, "
                 "fullfrac %.3f, nu-nu adj %d"
                 % (cn, Wp["S"], Wp["Sp"], Wp["Sm"], GBC[cn]["occ"],
                    Wp["L"] // 2 + 1, str(Wp["minC"]),
                    st["med_s"], st["max_s"],
                    np.median(GBC[cn]["sh"][2][1]), st["min_q2"],
                    st["full_frac"], GBC[cn]["nunu"]))
        check("G32-ctrl-geometry", ok_c,
              "CONTROLS built verbatim through the r281 channel: "
              "minC == flips %s + HL2 %d; their two-measure "
              "geometry printed above (the a2 comparison table)"
              % (str(CTRL_FLIPS), HL2_FLIP))
        geo_typ = {}
        for nm, key in (("K_G1_meds", "med_s"), ("K_G2_maxs",
                                                 "max_s"),
                        ("K_G3_minq2", "min_q2"),
                        ("K_G4_fullfrac", "full_frac")):
            tab = {"MAIN": GB9["stats"][key]}
            for cn in WC:
                tab[cn] = GBC[cn]["stats"][key]
            geo_typ[nm] = (dist_rule(tab, list(WC)), tab)
        shield_verdict = ("SHIELDING_SEPARATES"
                          if any(t[0] == "MAIN_SEPARATING"
                                 for t in geo_typ.values())
                          else "SHIELDING_BLIND")
        check("G33-shielding-adjudication", True,
              "THE FIRST QUESTION (source-pure, pre-spectral): %s "
              "-- sealed distance rule per statistic: %s"
              % (shield_verdict,
                 str({nm: (t[0], {k: round(v, 4)
                                  for k, v in t[1].items()})
                      for nm, t in geo_typ.items()})))

    # ---------------- S4 leg B1 nyquist
    section("S4  LEG B1 -- THE NYQUIST TEST (42 RUNGS + CONTROLS)")
    if smoke:
        for g in ("G40-ladder-census", "G41-nyquist-band",
                  "G42-nyquist-ordering"):
            check(g, True, "SMOKE: skipped")
        nyq_verdict = None
        nyq_detail = ""
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        cens = {}
        ok_hf = True
        for kz in kzs:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            Dk = D9 if kz == 9 else float(core.build_window(kz)["D"])
            Wp = W9 if kz == 9 else world_pack("w%d" % kz, ctx, Dk)
            gb = GB9 if kz == 9 else geom_block(Wp)
            ok_hf = ok_hf and (Wp["N"] == (Wp["S"] + 1) // 2)
            cens[kz] = dict(N=Wp["N"], S=Wp["S"], L=Wp["L"],
                            minC=Wp["minC"], off=Wp["minC"] - Wp["N"],
                            preds=gb["preds"],
                            smax=gb["stats"]["max_s"],
                            occ=gb["occ"])
        offs_true = [cens[kz]["off"] for kz in sorted(cens)]
        dist = {}
        for o in offs_true:
            dist[o] = dist.get(o, 0) + 1
        ok_anch = all(cens[kz]["off"] == ANCHORS[kz]
                      for kz in ANCHORS if kz in cens)
        check("G40-ladder-census", len(cens) == 42 and ok_hf
              and ok_anch and dist == R281_DIST,
              "42-rung census (r281 channel): offset distribution "
              "%s == r281 record, anchors exact, half-filling "
              "42/42" % str({("+%d" % k): dist[k]
                             for k in sorted(dist)}))
        # crossing dictionary: rungs minC+1 (r283 theorem);
        # controls: spectral crossing measured below in S5
        worlds_nyq = {}
        for kz in sorted(cens):
            worlds_nyq["kz%d" % kz] = (cens[kz]["preds"],
                                       cens[kz]["minC"] + 1)
        SPC = {}
        for cn, Wp in WC.items():
            dep = min(CTRL_DEPTH, Wp["Sp"] - 1)
            SPC[cn] = spectral_block(Wp, dep)
            worlds_nyq[cn] = (GBC[cn]["preds"], SPC[cn]["cross"])
        band = {}
        for cand in ("MAX", "MED", "Q90"):
            devs = {wn: abs(math.log2(pr[cand] / cr))
                    for wn, (pr, cr) in worlds_nyq.items()}
            wmx = max(devs, key=lambda w: devs[w])
            band[cand] = (devs[wmx], wmx,
                          sum(1 for v in devs.values()
                              if v <= NYQ_BAND), len(devs))
        law = [c for c in band if band[c][0] <= NYQ_BAND]
        ctrl_dev = {cn: round(abs(math.log2(
            worlds_nyq[cn][0]["MAX"] / worlds_nyq[cn][1])), 2)
            for cn in WC}
        check("G41-nyquist-band", True,
              "SEALED BAND TEST |log2(n_pred/crossing)| <= %.1f "
              "on all %d worlds: %s => %s; control devs (MAX): %s"
              % (NYQ_BAND, len(worlds_nyq),
                 str({c: ("maxdev %.2f@%s, %d/%d in band"
                          % (band[c][0], band[c][1], band[c][2],
                             band[c][3])) for c in band}),
                 ("NYQUIST_LAW(%s)" % ",".join(law)) if law
                 else "no aggregate holds the band",
                 str(ctrl_dev)))
        sps = {}
        for cand in ("MAX", "MED", "Q90"):
            xs_ = [worlds_nyq[w][0][cand] for w in worlds_nyq]
            ys_ = [worlds_nyq[w][1] for w in worlds_nyq]
            sps[cand] = BH.spearman(xs_, ys_)
        best_c = max(sps, key=lambda c: abs(sps[c]))
        if law:
            nyq_verdict = "NYQUIST_LAW"
            nyq_detail = "%s, max band dev %.2f" % (law[0],
                                                    band[law[0]][0])
        elif abs(sps[best_c]) >= SP_BAR:
            nyq_verdict = "NYQUIST_ORDERING"
            nyq_detail = ("%s sp %+.3f; HONEST: the ordering is "
                          "carried by the trivial N_w scaling of "
                          "the ladder (n_pred ~ L/4 ~ N_w when "
                          "s == 1) -- the mechanism-relevant "
                          "discriminant, the four controls, FAILS "
                          "the band on every aggregate"
                          % (best_c, sps[best_c]))
        else:
            nyq_verdict = "NYQUIST_REFUTED"
            nyq_detail = ("break loci: " + "; ".join(
                "%s maxdev %.2f@%s" % (c, band[c][0], band[c][1])
                for c in band) + "; best sp %+.3f (%s)"
                % (sps[best_c], best_c))
        check("G42-nyquist-ordering", True,
              "spearman(n_pred, crossing) over the %d worlds: %s "
              "(bar %.2f) => %s(%s) -- controls at crossings %s"
              % (len(worlds_nyq),
                 str({c: round(sps[c], 3) for c in sps}), SP_BAR,
                 nyq_verdict, nyq_detail,
                 str({cn: SPC[cn]["cross"] for cn in SPC})))

    # ---------------- S5 leg B2 christoffel
    section("S5  LEG B2 -- CHRISTOFFEL SANDWICH + COHERENCE")
    dev_id = 0.0
    for n in PROF_DEGS:
        En = SP9["B"][:, :n] @ SP9["B"][:, :n].T
        dev_id = max(dev_id, float(np.max(
            np.abs(np.diag(En) - SP9["cum"][:, n - 1]))
            / max(float(np.max(np.abs(np.diag(En)))), 1e-300)))
        dev_id = max(dev_id, abs(float(np.trace(En))
                                 - float(SP9["trace"][n - 1]))
                     / max(abs(float(np.trace(En))), 1e-300))
    check("G50-diag-trace-identity", dev_id <= ID_TOL,
          "EXACT IDENTITIES on w9 at the sealed degrees %s: "
          "diag(E_n)_k == v_k K_n(y_k) (cumulative Christoffel "
          "rows) and trace(E_n) == the contract's Christoffel sum "
          "sum_k w_nu/lambda_{mu,n} -- max rel dev %.1e (bar %.0e)"
          % (str(PROF_DEGS), dev_id, ID_TOL))
    ok_sand = all(SP9["maxd"][n - 1] <= rho9[n] + SAND_TOL
                  and rho9[n] <= SP9["trace"][n - 1] + SAND_TOL
                  for n in range(1, depth9 + 1))
    sand_c = True
    if not smoke:
        for cn in WC:
            sp = SPC[cn]
            sand_c = sand_c and all(
                sp["maxd"][n - 1] <= sp["rho"][n] + SAND_TOL
                and sp["rho"][n] <= sp["trace"][n - 1] + SAND_TOL
                for n in range(1, sp["depth"] + 1))
    check("G51-sandwich", ok_sand and sand_c,
          "THE SANDWICH THEOREM max_k v_k K_n(y_k) <= "
          "lambda_max(E_n) <= trace(E_n) holds at every n on w9%s "
          "(tol %.0e) -- the per-atom Christoffel bound and the "
          "triangle-class sum bracket the truth"
          % ("" if smoke else " + all four controls", SAND_TOL))
    rng_txt = "w9: n_CS = %s, n_DIAG = %s, crossing %s" \
        % (str(SP9["n_cs"]), str(SP9["n_diag"]), str(SP9["cross"]))
    ok_rng = (SP9["n_cs"] is not None
              and SP9["n_cs"] <= SP9["cross"]
              and (SP9["n_diag"] is None
                   or SP9["n_diag"] >= SP9["cross"]))
    ctrl_rng = {}
    if not smoke:
        for cn in WC:
            sp = SPC[cn]
            ctrl_rng[cn] = (sp["n_cs"], sp["n_diag"], sp["cross"])
            ok_rng = ok_rng and sp["n_cs"] is not None \
                and sp["n_cs"] <= sp["cross"] \
                and (sp["n_diag"] is None
                     or sp["n_diag"] >= sp["cross"])
    check("G52-christoffel-range", ok_rng,
          "CHRISTOFFEL_RANGE measured: %s%s -- the incoherent sum "
          "crosses EARLY (triangle-class, as inherited: Gershgorin "
          "died at 21), the single-atom bound %s"
          % (rng_txt,
             "" if smoke else "; controls (n_CS, n_DIAG, cross) "
             + str(ctrl_rng),
             "never reaches 1 inside the w9 window (the crossing "
             "is NOT a single-atom event)"
             if SP9["n_diag"] is None else
             "reaches 1 at %d" % SP9["n_diag"]))
    prof = {}
    for n in PROF_DEGS:
        En = SP9["B"][:, :n] @ SP9["B"][:, :n].T
        fro2 = float(np.sum(En * En))
        offd = En - np.diag(np.diag(En))
        prof[n] = dict(
            rho=float(rho9[n]), maxd=float(SP9["maxd"][n - 1]),
            tr=float(SP9["trace"][n - 1]),
            gain=float(rho9[n] / SP9["maxd"][n - 1]),
            slack=float(SP9["trace"][n - 1] / rho9[n]),
            reff=float(SP9["trace"][n - 1] ** 2 / fro2),
            offfr=float(math.sqrt(np.sum(offd * offd) / fro2)))
    for n in PROF_DEGS:
        p = prof[n]
        info("w9 n=%3d: rho %.5f, maxdiag %.5f, trace %.3g, "
             "gain %.4f, slack %.3g, r_eff %.1f, offdiag-fro "
             "%.3f" % (n, p["rho"], p["maxd"], p["tr"], p["gain"],
                       p["slack"], p["reff"], p["offfr"]))
    check("G53-coherence-profile", True,
          "COHERENCE ANATOMY (typed, the b2 deliverable): at N_w "
          "the coherent assist over the best single atom is "
          "gain = %.4f (rho %.5f vs maxdiag %.5f) while the "
          "triangle sum overshoots by slack = %.1f -- the nu "
          "atoms interfere DESTRUCTIVELY in the aggregate "
          "(off-diagonal mu-CD coupling, the old cancellation "
          "story in the two-measure coordinate) yet the small "
          "COHERENT assist is exactly what closes the single-atom "
          "gap at the wall"
          % (prof[W9["N"]]["gain"], prof[W9["N"]]["rho"],
             prof[W9["N"]]["maxd"], prof[W9["N"]]["slack"]))

    # ---------------- S6 leg C extremal vector
    section("S6  LEG C -- THE EXTREMAL VECTOR")
    ev_w, V_w = top_eigvecs(SP9["B"], W9["N"], 3)
    w1 = V_w[:, 0]
    rq = float(w1 @ (E184 @ w1))
    ok_ev = (abs(rq - float(ev_w[-1])) <= EV_TOL
             and abs(float(np.linalg.norm(w1)) - 1.0) <= EV_TOL)
    check("G60-eigvec-sanity", ok_ev,
          "top eigenvector of E_{N_w}: Rayleigh quotient == "
          "lambda_max to %.1e, unit norm -- the almost-"
          "subordination-breaking polynomial is well defined"
          % abs(rq - float(ev_w[-1])))
    m1_ = w1 * w1
    pr1 = float(1.0 / np.sum(m1_ * m1_))
    o_desc = np.argsort(m1_)[::-1]
    cmass = np.cumsum(m1_[o_desc])
    n90 = int(np.searchsorted(cmass, 0.9)) + 1
    kstar = int(np.argmax(SP9["cum"][:, W9["N"] - 1]))
    ov_diag = float(m1_[kstar])
    sp_mv = BH.spearman(list(m1_), [float(v) for v in W9["vn"]])
    sp_md = BH.spearman(list(m1_),
                        list(SP9["cum"][:, W9["N"] - 1]))
    u_nu = np.asarray(W9["fn"], float) * D9
    u_mass = float(np.sum(m1_ * u_nu))
    u_base = float(np.sum(np.asarray(W9["vn"]) * u_nu)
                   / np.sum(W9["vn"]))
    smallp_idx = [k for k in range(W9["Sm"])
                  if lab_nu[k][0] != 0 and lab_nu[k][1] in SMALLP]
    v_share = float(np.sum(np.asarray(W9["vn"])[smallp_idx])
                    / np.sum(W9["vn"])) if smallp_idx else 0.0
    m_share = float(np.sum(m1_[smallp_idx])) if smallp_idx else 0.0
    if smallp_idx and v_share > 0:
        f_sp = m_share / v_share
    else:
        f_sp = 1.0
    sp_typ = ("SMALLP_ENRICHED" if f_sp >= SP_ENRICH else
              ("SMALLP_DEPLETED" if f_sp <= 1.0 / SP_ENRICH
               else "SMALLP_NEUTRAL"))
    info("w9 extremal top-%d atoms (fold, u, x, class, p, v, s, "
         "q2, mass):" % TOPK)
    q2_9 = q9[2]
    for t in range(TOPK):
        k = int(o_desc[t])
        cls = ("ARCH", "K1", "KHI")[lab_nu[k][0]]
        info("  f=%4d u=%6.3f x=%+.4f %-4s p=%-4d v=%.2e s=%d "
             "q2=%.3g m=%.4f"
             % (W9["fn"][k], u_nu[k], W9["xn"][k], cls,
                lab_nu[k][1], W9["vn"][k], s9[k], q2_9[k], m1_[k]))
    check("G61-extremal-anatomy", True,
          "c1 CONCENTRATION (typed): PR = %.2f, n_90 = %d of %d, "
          "argmax-diag atom mass %.3f, spearman(m, v) = %+.3f, "
          "spearman(m, diag) = %+.3f; u-profile: mass-weighted "
          "mean u = %.2f vs v-weighted %.2f; r278 comparison: "
          "smallp (p <= 13) mass share %.3f vs v share %.3f => "
          "F_sp = %.2f => %s (nu smallp-labeled atoms: %d)"
          % (pr1, n90, W9["Sm"], ov_diag, sp_mv, sp_md, u_mass,
             u_base, m_share, v_share, f_sp, sp_typ,
             len(smallp_idx)))
    if smoke:
        check("G62-ctrl-extremal", True, "SMOKE: skipped")
        ctrl_ext = {}
    else:
        ctrl_ext = {}
        for cn in WC:
            sp = SPC[cn]
            nc = sp["cross"]
            evc, Vc = top_eigvecs(sp["B"], nc, 1)
            mc_ = Vc[:, 0] ** 2
            prc = float(1.0 / np.sum(mc_ * mc_))
            kst = int(np.argmax(sp["cum"][:, nc - 1]))
            ctrl_ext[cn] = (prc, float(np.max(mc_)),
                            float(mc_[kst]))
        check("G62-ctrl-extremal", True,
              "c2 CONTROL CONTRAST at their crossing degrees: "
              "(PR, top mass, argmax-diag mass) = %s vs MAIN "
              "(%.2f, %.3f, %.3f) -- typed: controls %s "
              "concentrated than MAIN's near-crossing mode"
              % (str({cn: tuple(round(x, 3) for x in v)
                      for cn, v in ctrl_ext.items()}),
                 pr1, float(m1_[o_desc[0]]), ov_diag,
                 "MORE" if all(v[0] < pr1
                               for v in ctrl_ext.values())
                 else "NOT uniformly more"))
    sp12 = BH.spearman(list(V_w[:, 0] ** 2), list(V_w[:, 1] ** 2))
    sp13 = BH.spearman(list(V_w[:, 0] ** 2), list(V_w[:, 2] ** 2))
    sp23 = BH.spearman(list(V_w[:, 1] ** 2), list(V_w[:, 2] ** 2))
    med_sp = float(np.median([sp12, sp13, sp23]))
    sup1 = set(int(i) for i in np.argsort(V_w[:, 0] ** 2)
               [::-1][:TOPSUP])
    sup2 = set(int(i) for i in np.argsort(V_w[:, 1] ** 2)
               [::-1][:TOPSUP])
    sup3 = set(int(i) for i in np.argsort(V_w[:, 2] ** 2)
               [::-1][:TOPSUP])
    band_typ = "ONE_BAND" if med_sp >= BAND_SP \
        else "INDEPENDENT_MODES"
    check("G63-band-structure", True,
          "c3 BROAD SATURATION (top-3 eigs %s): pairwise mass "
          "spearman %+.2f/%+.2f/%+.2f (median %+.2f, bar %.2f), "
          "top-%d support overlaps %d/%d/%d => %s"
          % (str([round(float(v), 5) for v in ev_w[-3:][::-1]]),
             sp12, sp13, sp23, med_sp, BAND_SP, TOPSUP,
             len(sup1 & sup2), len(sup1 & sup3), len(sup2 & sup3),
             band_typ))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    mut1 = mutant_gap_norm_x(W9["xp"], W9["xn"])
    spread_t = float(np.max(GB9["ratio"]) /
                     max(float(np.min(GB9["ratio"])), 1e-300))
    spread_m = float(np.max(mut1) / max(float(np.min(mut1)),
                                        1e-300))
    infl = spread_m / spread_t
    check("G70-mutant-gapnorm", infl >= M1_BAR,
          "m1 WRONG GAP NORMALIZATION (x coordinate, global mean "
          "gap): ratio spread inflates by %.1f (>= %.0f) -- LOUD: "
          "the hypothesis metric is the theta grid; the x metric "
          "with a global gap fabricates edge-atom exposure"
          % (infl, M1_BAR))
    cs_mut = mutant_unweighted_cs(SP9["cum"], W9["vn"])
    dev_m2 = abs(float(cs_mut[120 - 1])
                 - float(SP9["trace"][120 - 1])) \
        / float(SP9["trace"][120 - 1])
    check("G71-mutant-unweighted", dev_m2 >= M2_BAR,
          "m2 CHRISTOFFEL WITHOUT WEIGHT: dropping v_k breaks the "
          "exact trace identity by %.1e rel at n = 120 (>= %.1f) "
          "-- LOUD: the weight is load-bearing" % (dev_m2, M2_BAR))
    hits_m3 = scope_audit("mutant_eigvec_oracle")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G72-scope-audits", bool(hits_m3) and not hits
          and not ag_hits,
          "m3 EIGENVECTOR-ORACLE MUTANT FLAGGED (%s); the %d "
          "sealed constructors consume split-source arrays ONLY "
          "(%s); fragment audit (no fit primitives): %s"
          % ("; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 detector
    section("S8  DETECTOR LEDGER (r281 DISTANCE RULE)")
    if smoke:
        check("G80-detector-ledger", True, "SMOKE: skipped")
        det_typ = {}
    else:
        stats = {}
        for nm, t in geo_typ.items():
            stats[nm] = dict(t[1])
        stats["K_B1_nCS"] = {"MAIN": float(SP9["n_cs"])}
        stats["K_B2_gain20"] = {"MAIN": float(
            rho9[DET_DEG] / SP9["maxd"][DET_DEG - 1])}
        _e20, V20 = top_eigvecs(SP9["B"], DET_DEG, 1)
        m20 = V20[:, 0] ** 2
        stats["K_C1_PR20"] = {"MAIN": float(
            1.0 / np.sum(m20 * m20))}
        for cn in WC:
            sp = SPC[cn]
            stats["K_B1_nCS"][cn] = float(sp["n_cs"])
            stats["K_B2_gain20"][cn] = float(
                sp["rho"][DET_DEG] / sp["maxd"][DET_DEG - 1])
            _ec, Vc = top_eigvecs(sp["B"], DET_DEG, 1)
            mcc = Vc[:, 0] ** 2
            stats["K_C1_PR20"][cn] = float(
                1.0 / np.sum(mcc * mcc))
        det_typ = {nm: dist_rule(tab, list(WC))
                   for nm, tab in stats.items()}
        check("G80-detector-ledger", True,
              "PAIRCORR-STYLE DETECTOR (sealed r281 distance "
              "rule): %s (values %s)"
              % (str(det_typ),
                 str({nm: {k: round(v, 4) for k, v in tab.items()}
                      for nm, tab in stats.items()})))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no triangle bound as "
          "certificate, no posthoc window, no support-density-"
          "corrected Nyquist variant explored posthoc; what the "
          "round adds: the two-measure geometry disclosure, the "
          "sealed Nyquist adjudication, the Christoffel sandwich "
          "range with the coherence profile, and the extremal "
          "anatomy; r243..r283 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = [shield_verdict,
                 "%s(%s)" % (nyq_verdict, nyq_detail),
                 "CHRISTOFFEL_RANGE(w9 n_CS = %s, n_DIAG = %s, "
                 "crossing %s; gain_Nw = %.4f, slack_Nw = %.1f; "
                 "controls %s)"
                 % (str(SP9["n_cs"]), str(SP9["n_diag"]),
                    str(SP9["cross"]), prof[W9["N"]]["gain"],
                    prof[W9["N"]]["slack"], str(ctrl_rng)),
                 "EXTREMAL_ANATOMY(PR %.2f, n90 %d, argmax-diag "
                 "mass %.3f, %s, ctrl PR %s, %s)"
                 % (pr1, n90, ov_diag, sp_typ,
                    str({cn: round(v[0], 2)
                         for cn, v in ctrl_ext.items()}),
                    band_typ),
                 "DETECTOR_LEDGER(%s)" % str(det_typ)]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy of the open scalar L*; the "
          "sealed crossing formula is adjudicated honestly; NO L* "
          "claim, NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
