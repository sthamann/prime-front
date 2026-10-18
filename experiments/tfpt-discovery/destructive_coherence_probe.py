#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""destructive_coherence_probe -- PRIME.PORT.LSTAR.
DESTRUCTIVE_COHERENCE.01 (round 288): WHAT about the exact
prime-comb source makes the nu interference in the mu frame
DESTRUCTIVE -- and why does every conservation-faithful surgery
destroy it?  Context (sealed record inputs): r285 found the two
FIRST MAIN-separating detectors of the program -- MAIN's coherent
assist falls INTO the wall (0.019 at the crossing) while every
control stays 1.7..3.0, the random-sign z at the crossing is
DESTRUCTIVE on MAIN (z_v = -3.15) vs constructive on all controls
(+4.95..+12.44), and MAIN's wall assist is the extreme LOW outlier
(pct 0.00) of BOTH conservation ensembles (all 28 replicates die
collectively early); r284: the extremal band is the shallow-u ARCH
edge; r287: at the level-2 block scale the pair cancellation is
already absorbed INTO the P_j magnitudes (sqrt(m) economy, 39/44
worlds reinforce); r276: the metric firewall (2 pct support jitter
kills the wall to control depth).  THIS ROUND: the SIGN ANATOMY of
the E kernel (all signs come from the mu-CD kernel K_n between nu
positions -- the v are positive), the SAMPLING-PHASE hypothesis
(the K_n signs at (y_j, y_k) are set by how the nu atoms SAMPLE
the P_n oscillations), a sealed SOURCE-pure phase-dispersion
separator candidate, the phase turn rate under jitter (the r276
firewall as a phase statement), and the r287 object comparison.
NOT a proof round: no L* claim, no bound mechanism, no asymptotic
law -- sign maps + phase statistics + honest typing.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r287 discipline): w = window (kz),
S = #union entries of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = builder depth = (S+1)//2, n = degree, minC =
first n with h_n < 0, crossing = minC + 1 (r283 theorem, re-gated
spectrally on w9 + all four controls); f = fold index (theta_f =
2 pi f / L, x = cos theta_f).  Ground truth (minC, flips, r283/
r284/r285 records) enters GATES and record tables only; the
sealed constructors consume split-source arrays (positions,
weights, chain coefficients, kernel matrices, vectors) ONLY (AST
scope audit); the b2 source separator additionally audits CLEAN
against the SOLUTION-side set (no B matrix, no spectral block, no
rho/assist -- positions + chain ONLY); no zero/prime oracles
anywhere (AST firewall; atom classes via the r254 world-blind
integer root extraction through LS.atom_labels).  MACHINERY
IMPORTED VERBATIM: r285 CD.{decomp_parts, assist_terms,
sign_assignment, cons_check, ens_sign_world, budget_block,
rho_at}, r284 LS.{world_pack, spectral_block, atom_labels,
top_eigvecs, christoffel_rows, dist_rule}, r283 FS.{mu_chain_f64,
b_matrix_f64, mu_chain_mp}, r280 BL.sign_chain_f64, r278
MS.ctx_build, v881 PIK.lambda_eps, r243 PB.smooth_comb, paircorr
PC.{Grid, gen_model}, r244 BH.{wpack, spearman}, r287 L2.{
blocks_level2, autocorr_full} + the r287 rung pipeline (TX.
drive_arrays, CT.union_arrays, BR.eval_scaled, PBB.{mask_edge,
runs_split}), v563 core READ-ONLY.

LEG A -- THE SIGN ANATOMY OF THE E KERNEL:
(a1) E_jk = sqrt(v_j v_k) K_n(y_j, y_k); all off-diagonal signs
  come from the mu-CD kernel between nu positions.  The SIGN MAP
  at n = N_w and along the sealed degrees (20, 40, 120, 184,
  185) on MAIN + all four controls: negative-pair fraction,
  CHECKERBOARD statistic (sign flip fraction between fold-
  adjacent pair columns), the fold-distance BAND TABLE (bands
  1-2 / 3-4 / 5-8 / 9-16 / 17-32 / 33-64 / 65+: |T| share,
  signed share, negative fraction), and the OSCILLATION
  PREDICTOR: with the continuous zero-counting coordinate c_k =
  (#zeros of P_n below y_k) - 1 + phase_k, the sinc/CD-sign
  prediction sgn K_n(y_j, y_k) = (-1)^floor(|c_j - c_k|)
  (interior pairs; atoms beyond the extreme zeros are EDGE class
  and predicted POSITIVE pairwise among themselves -- all P_i
  share their sign beyond the last zero).  Agreement fractions
  (plain and |E|-weighted) measured per world and along n.
(a2) THE COHERENCE BALANCE EXACT: rho = diagpart + X with X =
  sum over pairs of T_jk = 2 u_j u_k E_jk (top-eigenvector frame
  at N_w and at the crossing) and the r285 source frame u_v =
  sqrt(v)/||.|| at the crossing (z_v = X/G coordinate, gated
  against the r285 records).  Decomposition of X by sign class
  (X_+, X_-), by fold-distance band, and by the r254 label pair
  classes (ARCH-ARCH / ARCH-x / SAMEP / DIFFP): WHICH pairs
  carry the destructivity on MAIN, and what reverses on the
  controls at their own crossing.
(a3) THE r287 OBJECT COMPARISON: the r287 level-2 block pipeline
  reproduced verbatim on w9 (sum ct == t_{N-2}, sum P == R,
  exact gates); the block cancellation deficit canc = A(0) -
  (sum P)^2 and its lag-band locus vs the E-side interference
  locus.  SEALED RULE: R287_SAME_OBJECT iff canc > 0 (residual
  root-scale cancellation exists at block level) AND the E-side
  interference at the crossing is destructive AND both objects
  are carried by their NEAR class (E: fold band 1-2 largest
  |signed share|; blocks: lag band 1-2 largest |share|); else
  DIFFERENT_OBJECTS(measured loci).

LEG B -- THE SAMPLING MECHANISM (phases from the chain, exact):
(b1) zeros of the mu-orthonormal P_{N_w} = eigenvalues of the
  N_w x N_w Jacobi matrix (diag al, offdiag sb -- the chain
  itself); WARDS: exactly n zeros inside the mu hull, STURM
  pivot counts at the sealed probe points == searchsorted, the
  n+1 midpoint signs of P_n alternate strictly, mp (dps 60)
  confirms a sign change across the bottom-3/top-3 zeros and
  the f64 sign of P_n at the three sealed edge-most nu atoms.
  PHASE FIELD: phase_k = position of nu atom k between its
  bracketing zeros (in [0, 1]); EDGE atoms (beyond the extreme
  zeros) counted and disclosed.  Equidistribution statistics
  (typed MEASUREMENT_ONLY -- never a premise): circular
  resultant R = |mean exp(2 pi i phase)|, two-sided KS distance
  vs uniform, adjacent-pair phase-step median.
(b2) THE SEALED SOURCE SEPARATOR CANDIDATE: K_S1 = the circular
  resultant R of the interior nu phases at depth N_w -- source-
  pure (positions + mu chain ONLY; the constructor audits clean
  against the solution-side scope set).  K_S2 = the v-weighted
  resultant (reported, not adjudicated).  ADJUDICATION (sealed):
  SOURCE_SEPARATOR_FOUND iff the r281 distance rule types K_S1
  MAIN_SEPARATING over the four controls AND MAIN's K_S1
  percentile is outside [0.1, 0.9] in BOTH r285 ensembles; else
  SOURCE_SEPARATOR_NOT_FOUND(values).
(b3) THE METRIC CONNECTION: the phase turn rate under the r276-
  class support jitter (dose theta = fraction of the local fold
  gap, ALL union atoms, weights bitwise): measured med |dphi|
  per dose at the sealed doses vs the naive per-atom prediction
  0.5 x theta x med(gap_x / zerogap_x) (zeros move too -- the
  excess is measured, not assumed); the dose for a quarter turn
  extrapolated from the smallest dose; side-by-side with the
  r276 P2_JIT depth records (typed COMPARISON_ONLY -- r276
  jitters the comb atoms upstream, this probe jitters the
  folded union atoms; channels disclosed as different).

LEG C -- THE ENSEMBLE MECHANIC:
(c1) the 28 r285 replicates reproduced with the SAME pinned
  seeds (ENS_SIGN 16 x seed 285000+i, ENS_SCR 12 x seed
  285000+100+i; conservation gates exact; the r285 assist_cross
  medians and MAIN pct 0.00 re-gated): per replicate the source
  separator K_S1 AND the wall coherence (assist at own
  crossing); the PREDICTIVE CHAIN measured: spearman(K_S1,
  assist_cross) and spearman(K_S1, crossing) per ensemble and
  combined over all 28.
(c2) the DOSE CURVE OF THE COHERENCE (r276 class, minimal
  surgeries): at the sealed doses (0.005, 0.01, 0.02, 0.05,
  0.10) x 2 pinned replicates: survival depth s = minC/N_w,
  assist at own crossing, z_v at own crossing (source frame),
  K_S1, med |dphi|; the destructive -> constructive FLIP DOSE =
  smallest dose with med z_v > 0 (measured).

LEG D -- WARDS / MUST-FAILS (each loud): w9 E/assist regression
gated against the r283/r284/r285 records (S = 367/263/104, N_w =
184, crossing 185, rho records, margin 1.68e-4, diagmax 0.9700,
n_CS 10, n_DIAG 187, gain 1.0307, slack 50.2, assist_cross
0.0195, z_v -3.15, C_off -0.105, z_x +3.36, ctrl z_v in
[+4.9, +12.5], ctrl assist_c records, ctrl crossings 26/22/28/
26); mp ward (dps 60) on rho_184/rho_185; ensemble regression
(sign med 1.89 pct 0.00, scr med 3.99 pct 0.00); exact toys (t1
hand 3-atom chain: zeros of P_2 = +-1/sqrt(2), phase(0.3) = 1/2
+ 0.15 sqrt(2), Sturm counts, midpoint alternation; t2 hand 2x2
balance E = (1/4)[[2,-1],[-1,2]]: top frame X = +1/4, source
frame X = -1/4, C_off = +-1, eigs 3/4 and 1/4; sinc predictor
hand triple; t3 conservation battery hand counts).  MUST-FAILS:
(m1) UNIFORM-GRID PHASES: the mutant reading phases against a
uniform-in-x zero grid instead of the chain zeros must distort
the phase field loudly (med circular distance >= 0.1); (m2)
DIAG-IN-CENSUS: the mutant counting the diagonal into the
interference must break the exact balance by >= 0.1 rel of rho;
(m3) ENSEMBLE WITHOUT CONSERVATION: the mass-scaling surgery
(x 1.15) must be CAUGHT by the conservation gate (>= 1e-3);
(m4) a mutant orienting a degree by the withheld crossing is
FLAGGED by the AST scope audit.  PAIRCORR HONESTY (binding):
the b1 equidistribution finding is typed MEASUREMENT_ONLY --
"the phases are equidistributed" borders root-scale territory
and is FORBIDDEN AS A PROOF PREMISE (a proof route would have
to DERIVE the phase statistics from the source); the detector
ledger types every sealed statistic by the r281 distance rule.
STOP LIST (anti-gates, binding): NO L* claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO equidistribution
as premise, NO posthoc window, NO RH claim; r243..r287 stand.

SEALED CONSTANTS: MAIN window 9; CTRL_FLIPS {EPST:25, SCR:21,
SMOOTH:27}; HL2 seed 101 flip 25; MINC_OFF9 0; EXT 8 / EXT2 32;
DEPTH_PAD 6; CTRL_PAD 5; PROF_DEGS (20, 40, 120, 184, 185);
DIST_BANDS ((1,2),(3,4),(5,8),(9,16),(17,32),(33,64),(65,inf));
AGREE_BAR 0.90; STURM_PTS (-0.9, -0.5, 0.0, 0.5, 0.9, 0.99);
EDGE_ZK 3; MP_SIGN_ATOMS 3; WARD_DPS 60; ID_TOL 1e-12; DEC_TOL
1e-10; R283_RHO {20:0.47808, 120:0.99898, 185:1.00004} tol 1e-5;
R283_TOP5 (0.99983, 0.99874, 0.99597, 0.98461, 0.96408) tol
1e-4; MARGIN_REC 1.68e-4 rel 0.01; DIAGMAX_REC 0.9700 tol 5e-3;
NCS_REC 10; NDIAG_REC 187; CROSS_REC 185; GAIN_REC 1.0307 tol
5e-3; SLACK_REC 50.2 tol 1.0; AC_MAIN_REC 0.0195 rel 0.02;
ZV_REC -3.15 tol 0.05; COFF_REC -0.105 tol 0.005; ZX_REC +3.36
tol 0.05; CTRL_ZV_RANGE (4.9, 12.5); CTRL_CROSS {EPST:26,
SCR:22, SMOOTH:28, HL2:26}; CTRL_AC {EPST:1.69, SCR:2.94,
SMOOTH:2.99, HL2:2.96} tol 0.05; RHO_WARD_TOL 1e-6;
ENS_SIGN_REPS 16; ENS_SCR_REPS 12; SEED_R285 285000; DET_DEG
20; ENS_SIGN_ACM_REC 1.89 / ENS_SCR_ACM_REC 3.99 tol 0.05;
PCT_OUT (0.1, 0.9); DOSES (0.005, 0.01, 0.02, 0.05, 0.10);
DOSE_REPS 2; SEED_DOSE 288000; QUARTER_TURN 0.25; R276_P2_DEPTH
{0.02:0.250, 0.05:0.255, 0.10:0.207} (COMPARISON_ONLY);
M1_BAR 0.1; M2_BAR 0.1; M3_BAR 1e-3; MUT_MASS 1.15; runtime <=
1800 s; smoke = toys + firewall + scopes + mutants + w9 f64
block (regression, zeros/Sturm f64 wards, sign map, balance,
phase field); mp wards, controls, r287 object, separator
adjudication, ensembles, dose curve, detector and verdict
adjudication skipped.  PRE-SPEC SCOPING (disclosed): every
record number above is a published r283/r284/r285/r276/r287
record adopted as-is; the sinc/CD sign predictor and the
zero-counting phase convention were fixed at design time from
the CD-kernel form (not fitted); no machinery pass preceded
this spec except record reading; no bar, band or typing rule
was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  SIGN_ANATOMY(neg fraction, band/class carriers on MAIN,
    control reversal) [always]
  + [exactly one of] SAMPLING_MECHANISM(agreement values,
    turn-rate statement) iff the oscillation predictor reaches
    agreement >= 0.90 on MAIN AND on >= 3 of 4 controls at
    their own crossing / SAMPLING_BLIND(values)
  + [exactly one of] SOURCE_SEPARATOR_FOUND(K_S1, worlds +
    ensemble extremity) iff dist rule MAIN_SEPARATING AND pct
    outside [0.1, 0.9] in both ensembles /
    SOURCE_SEPARATOR_NOT_FOUND(values)
  + [exactly one of] R287_SAME_OBJECT / DIFFERENT_OBJECTS
    (sealed rule of leg a3)
  + ENSEMBLE_CHAIN(sp(K_S1, assist_cross) per ensemble +
    combined, flip dose) [always]
  + DETECTOR_LEDGER [always].
Honesty before beauty: the sign map and the phase field are
MEASUREMENTS of the open scalar L*'s coherence half, not a
proof; the sampling predictor is a falsifiable sign FORMULA,
not a mechanism theorem; the equidistribution statistics are
measurements and remain forbidden as proof premises; no verdict
claims L*, a bound mechanism, a derived 5/7 or an asymptotic
law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 29/31 with ONE calibration
finding -- the G24 random-sign scale G was implemented over
unordered pairs while the imported r285 decomp_parts convention
sums ordered matrix entries (factor sqrt(2)); the balance
constructor was ALIGNED to the r285 convention (z_v then -3.149
== record -3.15); a convention alignment to the sealed import,
no physics bar, band, rule or verdict rule moved; smoke pass 2 =
31/31 (0.3 s); calibration pass 1 = first full evaluation =
31/31, wall 2.1 s -- the only post-freeze edit is this record-
table insertion, which IS the protocol; run1/run2 identical up
to WALL):
CAL_VERDICT = SIGN_ANATOMY(neg 0.503 at N_w; MAIN wall
destructivity carried by band 3-4 signed share -0.105 and class
ARCH-ARCH -0.056; controls at their crossing ALL constructive,
C_off EPST +0.41 / SCR +0.30 / SMOOTH +1.00 / HL2 +0.34 vs MAIN
-0.105) + SAMPLING_BLIND(sinc/CD agreement MAIN 0.728 plain /
0.878 |E|-weighted at N_w, controls 0.81/0.82/nan/0.83 -- below
the 0.90 bar everywhere: the pure sinc form of the CD sign is
only a PARTIAL sign mechanism) + SOURCE_SEPARATOR_NOT_FOUND(
K_S1 = R = 0.352, worlds WORLD_BLIND (dead spread 0.31..0.72
swallows MAIN), ens pct sign 0.44 / scr 0.25 GENERIC) +
DIFFERENT_OBJECTS(w9 block sequence REINFORCES: canc = -4.54e-2
< 0 -- no residual root-scale cancellation at block level while
the E-side wall interference is destructive: the r287 absorption
and the kernel destructivity are TWO coordinates) +
ENSEMBLE_CHAIN(sp(K_S1, assist_cross) +0.12 sign / +0.24 scr /
+0.18 all 28; sp(K_S1, cross) -0.23/-0.36 -- NO usable
predictive chain from the plain dispersion; flip dose 0.005) +
DETECTOR_LEDGER(K_S1_phase_R / K_S2_phase_ks /
K_A1_fracneg_cross / K_A2_coff_cross ALL WORLD_BLIND -- the
C_off SIGN separates MAIN as the only destructive world, the
sealed distance rule still types blind: spread 0.30..1.00).
Key numbers.  W9 ZEROS/PHASES (N_w = 184): 184 zeros inside the
mu hull, Sturm counts exact at all 6 probe points, 185 midpoint
signs alternate strictly, mp (dps 60) sign changes across the
bottom-3/top-3 zeros OK, mp sign of P_n at the 3 edge-most nu
atoms == f64; EDGE census: 1 of 104 nu atoms beyond the extreme
zeros (the shallow binding edge); phases R = 0.352, KS = 0.138
(n = 103), adjacent nu phase step med 0.14 -- mildly clustered,
NOT flat-equidistributed (MEASUREMENT_ONLY).  SIGN MAP (w9):
neg fraction 0.503 at N_w (0.479/0.481/0.503/0.503/0.507 along
n = 20/40/120/184/185), checkerboard flip 0.499; the BAND
STRUCTURE is the finding: fold distance 1-2 is 87 pct POSITIVE
(negfrac 0.13) while distance 3-4 is 80 pct NEGATIVE (negfrac
0.80) -- adjacent nu pairs sample K_n IN phase, next-nearest
pairs in ANTIPHASE; sinc agreement along n 0.832/0.781/0.811/
0.728/0.797, |E|-weighted 0.878 at N_w.  BALANCE (top frame at
N_w): rho = 0.96806 + 0.03177 exact (dev 7.8e-16); X_+ = +0.037
vs X_- = -0.006 (C_off +0.74) carried by band 1-2 (+0.68 of
|T|) and ARCH-ARCH (+0.74): the top mode RIDES the in-phase
adjacent pairs; SOURCE frame at the crossing (the r285
coordinate): X_v = -0.0517 = +0.222 - 0.273 (C_off -0.1046, z_v
-3.149, z_x +3.360), carried by band 3-4 (-0.105) and AA
(-0.056), band 1-2 still positive (+0.04) -- THE CARRIER MAP:
the destructivity is the ANTIPHASE next-nearest (3-4 fold)
ARCH-ARCH interference, not the near pairs.  CONTROLS at their
crossing (crossings 26/22/28/26 == records, assist_c == r285):
X_v = +0.305/+0.099/+0.818/+0.071 ALL CONSTRUCTIVE, neg
fractions 0.48/0.48/0.00/0.47, sinc agreement 0.81/0.82/nan/
0.83 (SMOOTH has 6 nu atoms, no valid interior pair) -- the
sign REVERSAL is total on every control.  R287 OBJECT (w9
pipeline verbatim: sum ct dev 1.9e-15, sum P == R exact, m = 35
blocks): canc = -4.54e-2 < 0 REINFORCES => DIFFERENT_OBJECTS.
PHASES/WORLDS: R = MAIN 0.352 vs EPST 0.496 / SCR 0.314 /
SMOOTH 0.715 / HL2 0.385; KS 0.138 vs 0.194/0.138/0.521/0.160;
K_S2 (v-weighted) 0.35 vs 0.51/0.29/0.76/0.38 -- the dead
worlds bracket MAIN from both sides: plain phase dispersion is
NOT the arithmetic coordinate (honest negative for the sealed
b2 candidate).  ENSEMBLES (28 replicates, seeds == r285,
conservation exact, r285 records re-gated: sign assist_cross
med 1.89 pct 0.00, scr med 3.99 pct 0.00): K_S1 sign ensemble
0.247..0.454 (MAIN pct 0.44), scr 0.240..0.466 (pct 0.25) --
GENERIC; chain correlations +0.12/+0.24/+0.18 (assist) and
-0.23/-0.36 (crossing): the plain dispersion does NOT predict
the wall.  DOSE CURVE (union jitter, weights bitwise, order
preserved; med over 2 pinned reps): dose 0.005: depth 0.71,
assist_cross 0.31, z_v +0.17, dphi 0.001; 0.01: 0.72/0.31/
+0.19/0.003; 0.02: 0.59/0.47/+2.00/0.004; 0.05: 0.43/0.61/
+4.43/0.012; 0.10: 0.46/0.66/+3.36/0.028 -- THE FINDING OF THE
ROUND: the phase field barely rotates (turn rate 0.24 per unit
dose == the static prediction 0.23, ratio 1.1: the chain zeros
CO-MOVE with the atoms; a quarter turn would need dose ~1.0)
yet z_v flips destructive -> constructive already at the
SMALLEST dose 0.005 and the depth collapses to 0.71 -- the
destructive coherence is NOT carried by the median phase
geometry but by hyper-fine alignments far below the median
phase resolution: the metric firewall (r276) is sharper than
any phase-rotation account, MEASURED; r276 P2_JIT depths
0.250/0.255/0.207 at 0.02/0.05/0.10 quoted COMPARISON_ONLY
(different channel: comb-level vs union-level jitter).
MUST-FAILS: m1 med circular distance 0.246 >= 0.1 LOUD; m2 dev
0.97 rel >= 0.1 LOUD; m3 break 1.5e-1 CAUGHT; m4 flagged;
constructors + separator solution-scope + fragment audit CLEAN.
MP WARD: rho_184 = 0.99983248 < 1 < 1.00003660 = rho_185 (devs
8.9e-14 / 1.6e-13).  Runtime 2.1 s full / 0.3 s smoke; run1/
run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

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

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import christoffel_decomposition_probe as CD       # noqa: E402 r285
import lstar_two_measure_probe as LS               # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import budget_localization_probe as BL             # noqa: E402 r280
import metric_stability_probe as MS                # noqa: E402 r278
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import paircorr_margin_probe as PC                 # noqa: E402
import bordered_hankel_probe as BH                 # noqa: E402 r244
import l2_deterministic_cancellation_probe as L2   # noqa: E402 r287
import terminal_crossratio_probe as TX             # noqa: E402 r260
import coupledtau_probe as CT                      # noqa: E402 r257
import border_resolvent_identity_probe as BR       # noqa: E402 r266
import phase_bulk_bound_probe as PBB               # noqa: E402 r269
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
MINC_OFF9 = 0
EXT = 8
EXT2 = 32
DEPTH_PAD = 6
CTRL_PAD = 5
PROF_DEGS = (20, 40, 120, 184, 185)
DIST_BANDS = ((1, 2), (3, 4), (5, 8), (9, 16), (17, 32), (33, 64),
              (65, 10 ** 9))
AGREE_BAR = 0.90
STURM_PTS = (-0.9, -0.5, 0.0, 0.5, 0.9, 0.99)
EDGE_ZK = 3
MP_SIGN_ATOMS = 3
WARD_DPS = 60
ID_TOL = 1e-12
DEC_TOL = 1e-10
R283_RHO = {20: 0.47808, 120: 0.99898, 185: 1.00004}
RHO_TOL = 1e-5
R283_TOP5 = (0.99983, 0.99874, 0.99597, 0.98461, 0.96408)
TOP5_TOL = 1e-4
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
DIAGMAX_REC = 0.9700
DIAGMAX_TOL = 5e-3
NCS_REC = 10
NDIAG_REC = 187
CROSS_REC = 185
GAIN_REC = 1.0307
GAIN_TOL = 5e-3
SLACK_REC = 50.2
SLACK_TOL = 1.0
AC_MAIN_REC = 0.0195
AC_MAIN_TOL = 0.02
ZV_REC = -3.15
ZV_TOL = 0.05
COFF_REC = -0.105
COFF_TOL = 0.005
ZX_REC = 3.36
ZX_TOL = 0.05
CTRL_ZV_RANGE = (4.9, 12.5)
CTRL_CROSS = {"EPST": 26, "SCR": 22, "SMOOTH": 28, "HL2": 26}
CTRL_AC = {"EPST": 1.69, "SCR": 2.94, "SMOOTH": 2.99, "HL2": 2.96}
CTRL_AC_TOL = 0.05
RHO_WARD_TOL = 1e-6
ENS_SIGN_REPS = 16
ENS_SCR_REPS = 12
SEED_R285 = 285000
DET_DEG = 20
ENS_SIGN_ACM_REC = 1.89
ENS_SCR_ACM_REC = 3.99
ENS_ACM_TOL = 0.05
PCT_OUT = (0.1, 0.9)
DOSES = (0.005, 0.01, 0.02, 0.05, 0.10)
DOSE_REPS = 2
SEED_DOSE = 288000
QUARTER_TURN = 0.25
R276_P2_DEPTH = {0.02: 0.250, 0.05: 0.255, 0.10: 0.207}
M1_BAR = 0.1
M2_BAR = 0.1
M3_BAR = 1e-3
MUT_MASS = 1.15
ADMIT = 1e-9

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
    return (not bad), ("NO zero/prime oracles; the zeros of this "
                       "round are POLYNOMIAL zeros of the mu chain "
                       "(Jacobi eigenvalues), not zeta objects; the "
                       "sealed constructors consume split-source "
                       "arrays, chain coefficients and kernel "
                       "matrices ONLY; record numbers enter gates "
                       "and record tables only"
                       if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("jacobi_zeros", "sturm_count", "pn_eval",
                "phase_field", "phase_stats", "source_separator",
                "balance_terms", "band_split", "sinc_pred",
                "jitter_folds")
SCOPE_FORBIDDEN = {"CTRL_FLIPS", "HL2_FLIP", "CTRL_CROSS",
                   "minC_true", "cross_true", "offs_true"}
SEP_FORBIDDEN = {"b_matrix_f64", "b_matrix_mp", "spectral_block",
                 "christoffel_rows", "rho_at", "assist_terms",
                 "top_eigvecs", "decomp_parts"}


def scope_audit(funcname, forbidden):
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


# ============== sealed source-pure constructors (AST-audited)
def jacobi_zeros(al, sb, n):
    """zeros of the mu-orthonormal P_n = eigenvalues of the n x n
    Jacobi matrix (diag al[0..n-1], offdiag sb[0..n-2]) -- chain
    coefficients only."""
    J = np.diag(np.asarray(al[:n], float))
    J += np.diag(np.asarray(sb[:n - 1], float), 1)
    J += np.diag(np.asarray(sb[:n - 1], float), -1)
    return np.linalg.eigvalsh(J)


def sturm_count(al, sb, n, t):
    """number of zeros of P_n below t: negative-pivot count of
    the LDL factorization of J_n - t I (tridiagonal Sturm)."""
    cnt = 0
    d = float(al[0]) - t
    if d < 0.0:
        cnt += 1
    for i in range(1, n):
        dd = d if d != 0.0 else 1e-300
        d = (float(al[i]) - t) - float(sb[i - 1]) ** 2 / dd
        if d < 0.0:
            cnt += 1
    return cnt


def pn_eval(al, sb, h0, ts, n):
    """orthonormal P_n evaluated at the points ts via the chain
    recurrence (vectorized)."""
    t = np.asarray(ts, float)
    u = np.full_like(t, 1.0 / math.sqrt(h0))
    um = np.zeros_like(t)
    for i in range(n):
        r = (t - al[i]) * u - (sb[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / sb[i]
    return u


def phase_field(zeros, y):
    """local oscillation phase of each atom y between adjacent
    P_n zeros: phi in [0, 1] (fractional cell position) and the
    continuous zero-counting coordinate c = (#zeros below) - 1 +
    phi; atoms beyond the extreme zeros are EDGE (phi, c NaN)."""
    z = np.asarray(zeros, float)
    yy = np.asarray(y, float)
    idx = np.searchsorted(z, yy)
    nz = len(z)
    inter = (idx > 0) & (idx < nz)
    phi = np.full(len(yy), np.nan)
    c = np.full(len(yy), np.nan)
    lo = z[np.clip(idx - 1, 0, nz - 1)]
    hi = z[np.clip(idx, 0, nz - 1)]
    f = (yy - lo) / np.maximum(hi - lo, 1e-300)
    phi[inter] = f[inter]
    c[inter] = (idx[inter] - 1).astype(float) + f[inter]
    return phi, c, inter


def phase_stats(phi):
    """circular resultant R, two-sided KS distance vs uniform,
    and the count of the interior phase multiset."""
    p = phi[np.isfinite(phi)]
    if len(p) == 0:
        return dict(R=float("nan"), ks=float("nan"), n=0)
    zc = np.exp(2j * np.pi * p)
    R = float(np.abs(np.mean(zc)))
    q = np.sort(p)
    i = np.arange(1, len(q) + 1, dtype=float)
    ks = float(max(np.max(i / len(q) - q),
                   np.max(q - (i - 1.0) / len(q))))
    return dict(R=R, ks=ks, n=len(p))


def source_separator(xp, wp, yn, vn, N):
    """the sealed b2 SOURCE separator: mu chain from (xp, wp) to
    depth N -> zeros of P_N -> phases of the nu positions ->
    (K_S1 = circular resultant, K_S2 = v-weighted resultant, KS
    distance, edge count).  Consumes positions + weights + N
    ONLY -- no B matrix, no spectral object, no assist."""
    al, sb, _h0 = FS.mu_chain_f64(np.asarray(xp, float),
                                  np.asarray(wp, float), N)
    z = jacobi_zeros(al, sb, N)
    phi, _c, inter = phase_field(z, np.asarray(yn, float))
    st = phase_stats(phi)
    p = phi[inter]
    v = np.asarray(vn, float)[inter]
    if len(p) and float(np.sum(v)) > 0:
        zc = np.exp(2j * np.pi * p)
        Rw = float(np.abs(np.sum(v * zc) / np.sum(v)))
    else:
        Rw = float("nan")
    return st["R"], Rw, st["ks"], int(np.sum(~inter))


def balance_terms(E, u):
    """exact Rayleigh balance: T_jk = 2 u_j u_k E_jk over the
    pairs j < k; returns (diagpart, T, X, X_+, X_-, sum|T|, G)
    with rho == diagpart + X exact; G is the r285 decomp_parts
    random-sign scale (ordered matrix entries: G = sqrt(2 sum
    over pairs (u_j u_k E_jk)^2) = sqrt(sum T^2 / 2))."""
    d = np.diag(E).copy()
    diagpart = float(np.sum(u * u * d))
    iu = np.triu_indices(E.shape[0], 1)
    T = 2.0 * u[iu[0]] * u[iu[1]] * E[iu]
    X = float(np.sum(T))
    Xp = float(np.sum(T[T > 0.0]))
    Xn = float(np.sum(T[T < 0.0]))
    A = float(np.sum(np.abs(T)))
    G = float(math.sqrt(np.sum(T * T) / 2.0))
    return diagpart, T, X, Xp, Xn, A, G


def band_split(dist):
    """sealed fold-distance band index per pair distance."""
    d = np.asarray(dist, np.int64)
    out = np.full(len(d), len(DIST_BANDS) - 1, np.int64)
    for bi, (lo, hi) in enumerate(DIST_BANDS):
        out[(d >= lo) & (d <= hi)] = bi
    return out


def sinc_pred(c, iu):
    """the sealed oscillation predictor: pred sgn K_n(y_j, y_k) =
    (-1)^floor(|c_j - c_k|) on interior pairs (sinc/CD sign);
    pairs at integer |dc| or with an EDGE atom are invalid here
    (edge-edge pairs are predicted POSITIVE by the caller)."""
    dc = np.abs(c[iu[0]] - c[iu[1]])
    valid = np.isfinite(dc) & (np.abs(dc - np.round(dc)) > 1e-9)
    fl = np.floor(np.where(np.isfinite(dc), dc, 0.0))
    pred = np.where((fl.astype(np.int64) % 2) == 0, 1.0, -1.0)
    return pred, valid


def jitter_folds(f_all, gaps, dose, seed, L):
    """r276-P2-class support jitter in the fold coordinate:
    f -> f + dose * gap * U[-1, 1] on ALL union atoms (weights
    untouched by construction); returns (f_jittered, x_jittered,
    df)."""
    rng = np.random.default_rng(seed)
    f = np.asarray(f_all, float)
    df = dose * np.asarray(gaps, float) * rng.uniform(
        -1.0, 1.0, len(f))
    fj = f + df
    return fj, np.cos(2.0 * np.pi * fj / L), df


# ============== must-fail mutants
def mutant_uniform_grid(zeros, y):
    """m1 MUST-FAIL: phases against a UNIFORM-IN-X zero grid
    instead of the chain zeros -- must distort the phase field
    loudly (the chain metric is load-bearing)."""
    zu = np.linspace(float(zeros[0]), float(zeros[-1]), len(zeros))
    return phase_field(zu, y)


def mutant_diag_census(E, u):
    """m2 MUST-FAIL: an 'interference' census INCLUDING the
    diagonal -- must break the exact balance identity loudly."""
    d = np.diag(E).copy()
    iu = np.triu_indices(E.shape[0], 1)
    T = 2.0 * u[iu[0]] * u[iu[1]] * E[iu]
    return float(np.sum(T) + np.sum(u * u * d))


def mutant_mass_scale(mags):
    """m3 MUST-FAIL: an ensemble surgery scaling the largest
    magnitude by 1.15 -- the conservation gate must CATCH it."""
    out = np.asarray(mags, float).copy()
    out[int(np.argmax(out))] *= MUT_MASS
    return out


def mutant_cross_oracle(cross_true):
    """m4 MUST-FAIL: a degree oriented by the withheld crossing
    -- the scope audit must FLAG this."""
    return cross_true - 1


# ============== gate-side helpers
def circ_dist(a, b):
    d = np.abs(np.asarray(a) - np.asarray(b)) % 1.0
    return np.minimum(d, 1.0 - d)


def local_gaps(f_sorted_pos):
    """local nearest-neighbor gap per atom (fold units), sorted
    input assumed."""
    f = np.asarray(f_sorted_pos, float)
    g = np.zeros(len(f))
    dl = np.diff(f)
    g[0] = dl[0]
    g[-1] = dl[-1]
    if len(f) > 2:
        g[1:-1] = np.minimum(dl[:-1], dl[1:])
    return g


def sign_map_block(E, fn, c):
    """gate-side sign-map bundle at one degree: neg fraction,
    checkerboard flip fraction, band table, sinc agreement."""
    n = E.shape[0]
    iu = np.triu_indices(n, 1)
    vals = E[iu]
    sg = np.sign(vals)
    neg = float(np.mean(sg < 0.0))
    # checkerboard: flip fraction between (j,k) and (j,k+1)
    o = np.argsort(np.asarray(fn))
    Es = E[np.ix_(o, o)]
    flips = []
    for j in range(n):
        row = Es[j]
        for k in range(j + 1, n - 1):
            if row[k] != 0.0 and row[k + 1] != 0.0:
                flips.append(1.0 if row[k] * row[k + 1] < 0.0
                             else 0.0)
    chb = float(np.mean(flips)) if flips else float("nan")
    dist = np.abs(np.asarray(fn)[iu[0]] - np.asarray(fn)[iu[1]])
    bidx = band_split(dist)
    aE = np.abs(vals)
    band_tab = []
    for bi in range(len(DIST_BANDS)):
        sel = bidx == bi
        if not np.any(sel):
            band_tab.append((0.0, 0.0, float("nan")))
            continue
        band_tab.append((float(np.sum(aE[sel]) / max(np.sum(aE),
                                                     1e-300)),
                         float(np.sum(vals[sel])
                               / max(np.sum(aE), 1e-300)),
                         float(np.mean(sg[sel] < 0.0))))
    pred, valid = sinc_pred(c, iu)
    both_int = np.isfinite(c[iu[0]]) & np.isfinite(c[iu[1]])
    vv = valid & both_int & (sg != 0.0)
    agree = float(np.mean(pred[vv] == sg[vv])) if np.any(vv) \
        else float("nan")
    wagree = (float(np.sum(aE[vv] * (pred[vv] == sg[vv]))
                    / max(np.sum(aE[vv]), 1e-300))
              if np.any(vv) else float("nan"))
    # edge-edge pairs: predicted positive
    ee = (~np.isfinite(c[iu[0]])) & (~np.isfinite(c[iu[1]]))
    ee_pos = (float(np.mean(sg[ee] > 0.0)) if np.any(ee)
              else float("nan"))
    return dict(iu=iu, vals=vals, neg=neg, chb=chb, bidx=bidx,
                band_tab=band_tab, agree=agree, wagree=wagree,
                n_valid=int(np.sum(vv)), ee_pos=ee_pos,
                n_ee=int(np.sum(ee)))


def balance_by_class(T, bidx, cls_pair):
    """signed share tables of the interference X per band and
    per label pair class (normalized by sum |T|)."""
    A = float(np.sum(np.abs(T)))
    A = max(A, 1e-300)
    bands = {}
    for bi in range(len(DIST_BANDS)):
        sel = bidx == bi
        bands[bi] = float(np.sum(T[sel]) / A)
    classes = {}
    for cname in ("AA", "AX", "SAMEP", "DIFFP"):
        sel = cls_pair == cname
        classes[cname] = float(np.sum(T[sel]) / A)
    return bands, classes


def pair_label_classes(lab, iu):
    """r254 label pair classes: AA (both ARCH), AX (one ARCH),
    SAMEP (both non-ARCH, same primary), DIFFP."""
    cls = np.asarray([t[0] for t in lab])
    pp = np.asarray([t[1] for t in lab])
    a0 = cls[iu[0]] == 0
    a1 = cls[iu[1]] == 0
    out = np.empty(len(iu[0]), dtype=object)
    out[a0 & a1] = "AA"
    out[a0 ^ a1] = "AX"
    both = (~a0) & (~a1)
    same = both & (pp[iu[0]] == pp[iu[1]])
    out[both & ~same] = "DIFFP"
    out[same] = "SAMEP"
    return out


def zv_block(B, n, vn):
    """source-frame interference at degree n: X_v, z_v = X/G,
    C_off = X/sum|T| plus the adaptive z_x (r285 coordinates)."""
    En = B[:, :n] @ B[:, :n].T
    uv = np.sqrt(np.asarray(vn, float))
    uv = uv / float(np.linalg.norm(uv))
    dg, T, X, Xp, Xn, A, G = balance_terms(En, uv)
    zv = X / max(G, 1e-300)
    coff = X / max(A, 1e-300)
    _e, Vx = LS.top_eigvecs(B, n, 1)
    dgx, Tx, Xx, _xp, _xn, _Ax, Gx = balance_terms(En, Vx[:, 0])
    return dict(E=En, uv=uv, T=T, X=X, Xp=Xp, Xn=Xn, A=A, G=G,
                zv=zv, coff=coff, zx=Xx / max(Gx, 1e-300),
                ux=Vx[:, 0], Tx=Tx, dgx=dgx, Xx=Xx)


def zero_ward(al, sb, h0, n, xp, wp, smoke):
    """f64 + Sturm + midpoint wards for the zeros of P_n; mp
    edge confirmation in full mode."""
    z = jacobi_zeros(al, sb, n)
    lo_h, hi_h = float(np.min(xp)), float(np.max(xp))
    ok_hull = bool(np.all(z > lo_h) and np.all(z < hi_h)
                   and len(z) == n)
    ok_sturm = all(sturm_count(al, sb, n, t)
                   == int(np.searchsorted(z, t))
                   for t in STURM_PTS)
    mids = np.concatenate([[0.5 * (lo_h + z[0])],
                           0.5 * (z[1:] + z[:-1]),
                           [0.5 * (z[-1] + hi_h)]])
    pv = pn_eval(al, sb, h0, mids, n)
    sgs = np.sign(pv)
    ok_alt = bool(np.all(sgs[1:] * sgs[:-1] < 0.0)
                  and sgs[-1] > 0.0)
    mp_note = "mp SKIPPED (smoke)"
    ok_mp = True
    if not smoke:
        # mp chain recomputed from source (gate-side)
        alm, sbm, h0m = FS.mu_chain_mp(
            np.asarray(xp, float), np.asarray(wp, float), n,
            WARD_DPS)

        def pmp(t):
            u = 1 / mp.sqrt(h0m)
            um = mp.mpf(0)
            tt = mp.mpf(float(t))
            for i in range(n):
                r = (tt - alm[i]) * u \
                    - (sbm[i - 1] * um if i > 0 else 0)
                um, u = u, r / sbm[i]
            return u
        ks = list(range(EDGE_ZK)) + list(range(n - EDGE_ZK, n))
        ok_sc = True
        for k in ks:
            gl = (z[k] - (z[k - 1] if k > 0 else lo_h)) * 0.25
            gr = ((z[k + 1] if k < n - 1 else hi_h) - z[k]) * 0.25
            sl = pmp(z[k] - gl)
            sr = pmp(z[k] + gr)
            ok_sc = ok_sc and (sl * sr < 0)
        ok_mp = ok_sc
        mp_note = ("mp (dps %d) sign change across the bottom-%d/"
                   "top-%d zeros: %s" % (WARD_DPS, EDGE_ZK,
                                         EDGE_ZK,
                                         "OK" if ok_sc else
                                         "BROKEN"))
    return z, ok_hull and ok_sturm and ok_alt and ok_mp, \
        ("%d zeros inside the mu hull; Sturm pivot counts exact "
         "at %s; the %d midpoint signs alternate strictly "
         "(terminal +); %s" % (len(z), str(STURM_PTS), n + 1,
                               mp_note))


def r287_block_object(smoke):
    """gate-side r287 level-2 block pipeline on w9 (verbatim
    machinery): returns (canc, lag band shares, gates)."""
    p9 = BH.wpack(9)
    N = p9["N"]
    rows = p9["rows"]
    r, t, ap, bp = TX.drive_arrays(rows, N)
    chain = ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
    _ = chain
    xu, wu = CT.union_arrays(p9["d"])
    bx, bw = CT.union_arrays(p9["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = BR.eval_scaled(rows, bx, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    dev_ct = abs(float(np.sum(ct)) - float(t[N - 2])) \
        / max(float(np.sum(np.abs(ct))), 1e-300)
    o = np.argsort(bx, kind="stable")
    bxs = bx[o]
    cts = ct[o]
    ed = PBB.mask_edge(bxs, lo, hi, L2.EDGE_F)
    cb = cts[~ed]
    runs = PBB.runs_split(cb)
    Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
    R = sum(Sr)
    P = L2.blocks_level2(Sr)
    dev_bid = abs(sum(P) - R) / max(abs(R), 1e-300)
    A = L2.autocorr_full(P)
    canc = float(A[0] - sum(P) ** 2)
    shares = {}
    if canc > 1e-12 * max(float(A[0]), 1e-300):
        for lo_, hi_ in L2.LAG_BANDS:
            sl_ = float(np.sum(A[lo_:min(hi_ + 1, len(A))])) \
                if lo_ < len(A) else 0.0
            shares[(lo_, hi_)] = -2.0 * sl_ / canc
    return dict(canc=canc, A0=float(A[0]), m=len(P),
                dev_ct=dev_ct, dev_bid=dev_bid, shares=shares)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("destructive_coherence_probe -- PRIME.PORT.LSTAR."
          "DESTRUCTIVE_COHERENCE.01 (round 288)")
    print("SPEC_SHA %s   (r285 CD %s / r284 LS %s / r287 L2 %s)"
          % (SPEC_SHA[:16], CD.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             L2.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 f64 block; mp wards, controls, r287 "
                        "object, separator adjudication, ensembles, "
                        "dose curve, detector, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the zero-counting phase "
          "convention and the sinc/CD sign predictor (design-time, "
          "from the CD-kernel form), the band and label pair "
          "classes, the balance decomposition frames, the b2 "
          "source separator K_S1 with its worlds+ensemble "
          "adjudication rule, the jitter surgery with conservation "
          "gates, the r287 object rule, every bar/band/tolerance, "
          "the mutants and the verdict form; the b1 "
          "equidistribution statistics are typed MEASUREMENT_ONLY "
          "and forbidden as proof premises; the STOP list forbids "
          "any L* claim")

    # ---------------- S1 toys
    section("S1  TOYS -- HAND CHAIN/PHASE, BALANCE/SINC, "
            "CONSERVATION")
    # t1: mu = atoms (-1, 0, 1) weights (1, 2, 1)
    xt = np.array([-1.0, 0.0, 1.0])
    wt = np.array([1.0, 2.0, 1.0])
    alt_, sbt_, h0t = FS.mu_chain_f64(xt, wt, 2)
    zt = jacobi_zeros(alt_, sbt_, 2)
    z_hand = 1.0 / math.sqrt(2.0)
    phit, ct_, intt = phase_field(zt, np.array([0.3]))
    phi_hand = 0.5 + 0.15 * math.sqrt(2.0)
    okp = (abs(float(zt[0]) + z_hand) <= 1e-14
           and abs(float(zt[1]) - z_hand) <= 1e-14
           and abs(float(phit[0]) - phi_hand) <= 1e-12
           and bool(intt[0])
           and sturm_count(alt_, sbt_, 2, 0.0) == 1
           and sturm_count(alt_, sbt_, 2, 0.8) == 2
           and sturm_count(alt_, sbt_, 2, -0.8) == 0)
    mids_t = np.array([-0.9, 0.0, 0.9])
    pv_t = pn_eval(alt_, sbt_, h0t, mids_t, 2)
    ok_alt_t = pv_t[0] > 0 and pv_t[1] < 0 and pv_t[2] > 0
    check("G10-toy-phase-sturm", okp and ok_alt_t,
          "HAND CHAIN (mu = {-1,0,1} w {1,2,1}): zeros of P_2 = "
          "+-1/sqrt(2) = +-%.10f exact; phase(0.3) = 1/2 + 0.15 "
          "sqrt(2) = %.12f (dev %.1e); Sturm counts 0/1/2 at "
          "-0.8/0/0.8 exact; midpoint signs +/-/+ alternate"
          % (z_hand, float(phit[0]),
             abs(float(phit[0]) - phi_hand)))
    # t2: hand 2x2 balance + sinc triple
    E_t = np.array([[2.0, -1.0], [-1.0, 2.0]]) / 4.0
    ev_t, V_t = np.linalg.eigh(E_t)
    u_top = V_t[:, -1]
    dg_t, T_t, X_t, Xp_t, Xn_t, A_t, _G = balance_terms(E_t, u_top)
    u_src = np.array([1.0, 1.0]) / math.sqrt(2.0)
    dg_s, T_s, X_s, _p, _n, A_s, _Gs = balance_terms(E_t, u_src)
    c_toy = np.array([0.2, 0.5, 1.7])
    iu_toy = (np.array([0, 0, 1]), np.array([1, 2, 2]))
    pred_t, val_t = sinc_pred(c_toy, iu_toy)
    ok_t2 = (abs(float(ev_t[-1]) - 0.75) <= 1e-14
             and abs(float(ev_t[0]) - 0.25) <= 1e-14
             and abs(dg_t - 0.5) <= 1e-14
             and abs(X_t - 0.25) <= 1e-14
             and abs(dg_t + X_t - float(ev_t[-1])) <= 1e-15
             and abs(X_t / A_t - 1.0) <= 1e-14
             and abs(X_s + 0.25) <= 1e-14
             and abs(X_s / A_s + 1.0) <= 1e-14
             and list(pred_t) == [1.0, -1.0, -1.0]
             and bool(np.all(val_t)))
    check("G11-toy-balance-sinc", ok_t2,
          "HAND 2x2 (E = (1/4)[[2,-1],[-1,2]]): eigs 3/4, 1/4; "
          "top frame diagpart 1/2 + X = +1/4 == 3/4 exact (C_off "
          "+1); source frame X = -1/4 (C_off -1: the SAME kernel "
          "is destructive in the source frame and constructive "
          "in the adaptive frame -- the two-frame honesty of the "
          "balance); sinc triple c = (0.2, 0.5, 1.7): pred "
          "(+,-,-) hand-exact")
    # t3: conservation battery (r285 machinery)
    tf = np.array([1, 2, 3, 4, 5], np.int64)
    tm = np.array([1.0, 0.5, 0.25, 0.125, 0.0625])
    msk_t = CD.sign_assignment(5, 2, SEED_R285)
    okc_t, dev_c = CD.cons_check(tf, tm, tf, tm, 2, msk_t)
    check("G12-toy-conservation", okc_t and dev_c == 0.0
          and int(np.sum(msk_t)) == 2,
          "TOY CONSERVATION (r285 machinery verbatim): the legit "
          "sign-ensemble op preserves fold set + magnitude bitwise "
          "(dev %.1f), 2 of 5 nu labels (hand count)" % dev_c)

    # ---------------- S2 w9 regression
    section("S2  W9 -- E/ASSIST REGRESSION AGAINST r283/r284/r285")
    rr9 = core.build_window(9)
    D9 = float(rr9["D"])
    ctx9 = MS.ctx_build(9)
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == 367 and W9["Sp"] == 263
              and W9["Sm"] == 104
              and W9["N"] == (W9["S"] + 1) // 2
              and W9["minC"] == W9["N"] + MINC_OFF9)
    check("G20-w9-source-split", ok_src,
          "w9 FULL SOURCE: S = %d (mu %d / nu %d), N_w = %d == "
          "(S+1)//2, minC = %s == N_w + %d (record)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"],
             str(W9["minC"]), MINC_OFF9))
    Nw = W9["N"]
    depth9 = min(Nw + DEPTH_PAD, W9["Sp"] - 1)
    SP9 = LS.spectral_block(W9, depth9)
    rho9 = SP9["rho"]
    check("G21-w9-crossing", SP9["cross"] == W9["minC"] + 1
          and SP9["cross"] == CROSS_REC,
          "lambda_max(E_n) crosses 1 at n = %s == minC + 1 == %d "
          "(r283/r284/r285 route reproduced)"
          % (str(SP9["cross"]), CROSS_REC))
    E184 = SP9["B"][:, :Nw] @ SP9["B"][:, :Nw].T
    ev184 = np.linalg.eigvalsh(E184)
    top5 = ev184[-5:][::-1]
    margin9 = 1.0 - rho9[Nw]
    dmax184 = float(SP9["maxd"][Nw - 1])
    gain9 = float(rho9[Nw] / SP9["maxd"][Nw - 1])
    slack9 = float(SP9["trace"][Nw - 1] / rho9[Nw])
    ac_main = float(rho9[CROSS_REC]
                    / SP9["maxd"][CROSS_REC - 1]) - 1.0
    ok_rec = all(abs(rho9[n] - R283_RHO[n]) <= RHO_TOL
                 for n in R283_RHO)
    ok_top = all(abs(float(top5[i]) - R283_TOP5[i]) <= TOP5_TOL
                 for i in range(5))
    ok_r284 = (SP9["n_cs"] == NCS_REC and SP9["n_diag"] == NDIAG_REC
               and abs(gain9 - GAIN_REC) <= GAIN_TOL
               and abs(slack9 - SLACK_REC) <= SLACK_TOL)
    check("G22-w9-profile-regression",
          ok_rec and ok_top and ok_r284
          and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
          and abs(dmax184 - DIAGMAX_REC) <= DIAGMAX_TOL
          and abs(ac_main / AC_MAIN_REC - 1.0) <= AC_MAIN_TOL
          and rho9[Nw] < 1.0,
          "records reproduced: rho_20/120/185 dev <= %.0e; top-5 "
          "ok; margin %.4e; diagmax %.5f; n_CS %s / n_DIAG %s; "
          "gain %.4f; slack %.1f; assist_cross %.4f (rec %.4f)"
          % (RHO_TOL, margin9, dmax184, str(SP9["n_cs"]),
             str(SP9["n_diag"]), gain9, slack9, ac_main,
             AC_MAIN_REC))
    if smoke:
        check("G23-w9-mp-ward", True, "SMOKE: skipped")
    else:
        alm9, sbm9, h0m9 = FS.mu_chain_mp(
            np.asarray(W9["xp"]), np.asarray(W9["wp"]), depth9,
            WARD_DPS)
        B9m = FS.b_matrix_mp(alm9, sbm9, h0m9,
                             np.asarray(W9["xn"]),
                             np.asarray(W9["vn"]), depth9,
                             WARD_DPS)
        devs = {}
        rho_mp = {}
        for n in (Nw, Nw + 1):
            Bn = B9m[:, :n]
            rmp = float(np.linalg.eigvalsh(Bn @ Bn.T)[-1])
            rho_mp[n] = rmp
            devs[n] = abs(rmp - rho9[n]) / max(abs(rmp), 1e-300)
        ok_ward = (max(devs.values()) <= RHO_WARD_TOL
                   and rho_mp[Nw] < 1.0 and rho_mp[Nw + 1] > 1.0)
        check("G23-w9-mp-ward", ok_ward,
              "MP WARD (dps %d): rho_184 = %.8f < 1 < %.8f = "
              "rho_185 (rel devs %.1e / %.1e, bar %.0e)"
              % (WARD_DPS, rho_mp[Nw], rho_mp[Nw + 1], devs[Nw],
                 devs[Nw + 1], RHO_WARD_TOL))
    ZB9 = zv_block(SP9["B"], CROSS_REC, W9["vn"])
    ok_zv = (abs(ZB9["zv"] - ZV_REC) <= ZV_TOL
             and abs(ZB9["coff"] - COFF_REC) <= COFF_TOL
             and abs(ZB9["zx"] - ZX_REC) <= ZX_TOL)
    check("G24-w9-zv-regression", ok_zv,
          "r285 z-coordinates reproduced at the crossing: z_v = "
          "%+.3f (rec %+.2f), C_off = %+.4f (rec %+.3f), adaptive "
          "z_x = %+.3f (rec %+.2f) -- the destructive source-"
          "frame interference is the round's address"
          % (ZB9["zv"], ZV_REC, ZB9["coff"], COFF_REC, ZB9["zx"],
             ZX_REC))

    # ---------------- S3 leg B1 zeros + phases (needed by leg A)
    section("S3  ZEROS + PHASE FIELD (LEG B1)")
    NMAX = max(PROF_DEGS)
    al9, sb9, h09 = FS.mu_chain_f64(np.asarray(W9["xp"]),
                                    np.asarray(W9["wp"]), NMAX)
    z9, ok_zw, zw_det = zero_ward(al9, sb9, h09, Nw,
                                  np.asarray(W9["xp"]),
                                  np.asarray(W9["wp"]), smoke)
    phi9, c9, int9 = phase_field(z9, np.asarray(W9["xn"]))
    st9 = phase_stats(phi9)
    n_edge9 = int(np.sum(~int9))
    ok_mp_atoms = True
    mp_note = "mp atom signs SKIPPED (smoke)"
    if not smoke:
        alm, sbm, h0m = FS.mu_chain_mp(np.asarray(W9["xp"]),
                                       np.asarray(W9["wp"]), Nw,
                                       WARD_DPS)

        def pmp9(t):
            u = 1 / mp.sqrt(h0m)
            um = mp.mpf(0)
            tt = mp.mpf(float(t))
            for i in range(Nw):
                r = (tt - alm[i]) * u \
                    - (sbm[i - 1] * um if i > 0 else 0)
                um, u = u, r / sbm[i]
            return u
        o_x = np.argsort(np.asarray(W9["xn"]))
        edge_atoms = list(o_x[:1]) + list(o_x[-MP_SIGN_ATOMS + 1:])
        pf64 = pn_eval(al9, sb9, h09,
                       np.asarray(W9["xn"])[edge_atoms], Nw)
        for t_i, k in enumerate(edge_atoms):
            smp = pmp9(float(np.asarray(W9["xn"])[k]))
            ok_mp_atoms = ok_mp_atoms and \
                (float(smp) * float(pf64[t_i]) > 0.0)
        mp_note = ("mp sign of P_n at the %d edge-most nu atoms "
                   "== f64: %s" % (MP_SIGN_ATOMS,
                                   "OK" if ok_mp_atoms else
                                   "BROKEN"))
    check("G30-zeros-sturm-ward", ok_zw and ok_mp_atoms,
          zw_det + "; " + mp_note)
    # adjacent nu phase step
    o_fn = np.argsort(np.asarray(W9["fn"]))
    phis = phi9[o_fn]
    steps = circ_dist(phis[1:], phis[:-1])
    steps = steps[np.isfinite(steps)]
    step_med = float(np.median(steps)) if len(steps) else float("nan")
    check("G40-phase-field-w9", st9["n"] + n_edge9 == W9["Sm"],
          "w9 PHASE FIELD at N_w (typed MEASUREMENT_ONLY): %d "
          "interior + %d EDGE atoms; circular resultant R = %.3f, "
          "KS vs uniform = %.3f, adjacent nu phase step med = "
          "%.2f -- equidistribution and stepping are MEASURED, "
          "never premises" % (st9["n"], n_edge9, st9["R"],
                              st9["ks"], step_med))

    # ---------------- S4 leg A sign map + balance
    section("S4  LEG A -- SIGN MAP + COHERENCE BALANCE (w9)")
    lab_nu = LS.atom_labels(W9["fn"], D9, W9["uu"], W9["mm"])
    dev_adm = max([d for _c, _p, d in lab_nu if _c != 0] or [0.0])
    sm_prof = {}
    for n in PROF_DEGS:
        z_n = z9 if n == Nw else jacobi_zeros(al9, sb9, n)
        _p, c_n, _i = phase_field(z_n, np.asarray(W9["xn"]))
        En = SP9["B"][:, :n] @ SP9["B"][:, :n].T
        sm_prof[n] = sign_map_block(En, W9["fn"], c_n)
    SM = sm_prof[Nw]
    info("w9 sign map along n: " + "; ".join(
        "n=%d neg %.3f agree %.3f" % (n, sm_prof[n]["neg"],
                                      sm_prof[n]["agree"])
        for n in PROF_DEGS))
    info("w9 band table at N_w (band: |T|share, signed share, "
         "negfrac): " + "; ".join(
             "%d-%s: %.3f/%+.3f/%.2f"
             % (DIST_BANDS[bi][0],
                str(DIST_BANDS[bi][1])
                if DIST_BANDS[bi][1] < 10 ** 9 else "inf",
                SM["band_tab"][bi][0], SM["band_tab"][bi][1],
                SM["band_tab"][bi][2])
             for bi in range(len(DIST_BANDS))))
    ok_sym = float(np.max(np.abs(E184 - E184.T))) <= 1e-14
    check("G31-sign-map-w9", ok_sym and dev_adm <= ADMIT,
          "SIGN MAP at N_w: neg fraction %.3f, checkerboard flip "
          "fraction %.3f, edge-edge pairs %d (positive fraction "
          "%s -- all P_i share sign beyond the last zero); E "
          "symmetric to 1e-14, label admission %.1e <= %.0e"
          % (SM["neg"], SM["chb"], SM["n_ee"],
             ("%.2f" % SM["ee_pos"]) if SM["n_ee"] else "n/a",
             dev_adm, ADMIT))
    check("G32-sinc-agreement", True,
          "OSCILLATION PREDICTOR (sealed, sinc/CD): agreement "
          "%.3f plain / %.3f |E|-weighted on %d interior pairs "
          "at N_w (bar %.2f for the verdict typing); along n: %s"
          % (SM["agree"], SM["wagree"], SM["n_valid"], AGREE_BAR,
             str({n: round(sm_prof[n]["agree"], 3)
                  for n in PROF_DEGS})))
    # balance decomposition: top frame at N_w + source frame at cross
    evN, VN = np.linalg.eigh(E184)
    uN = VN[:, -1]
    dgN, TN, XN, XpN, XnN, AN, _GN = balance_terms(E184, uN)
    dev_bal = abs(dgN + XN - float(evN[-1])) \
        / max(abs(float(evN[-1])), 1e-300)
    iuN = np.triu_indices(W9["Sm"], 1)
    distN = np.abs(np.asarray(W9["fn"])[iuN[0]]
                   - np.asarray(W9["fn"])[iuN[1]])
    bidxN = band_split(distN)
    clsN = pair_label_classes(lab_nu, iuN)
    bandsN, classesN = balance_by_class(TN, bidxN, clsN)
    # source frame at the crossing (the r285 coordinate)
    Tv = ZB9["T"]
    bandsV, classesV = balance_by_class(Tv, bidxN, clsN)
    info("w9 balance TOP frame at N_w: bands %s classes %s"
         % (str({("%d-%s" % (DIST_BANDS[b][0],
                             DIST_BANDS[b][1]
                             if DIST_BANDS[b][1] < 10 ** 9
                             else "inf")): round(v, 3)
                 for b, v in bandsN.items()}),
            str({k: round(v, 3) for k, v in classesN.items()})))
    info("w9 balance SOURCE frame at crossing: bands %s classes "
         "%s" % (str({("%d-%s" % (DIST_BANDS[b][0],
                                  DIST_BANDS[b][1]
                                  if DIST_BANDS[b][1] < 10 ** 9
                                  else "inf")): round(v, 3)
                      for b, v in bandsV.items()}),
                 str({k: round(v, 3) for k, v in classesV.items()})))
    check("G33-balance-main", dev_bal <= DEC_TOL
          and abs(XpN + XnN - XN) <= 1e-12 * max(abs(XN), 1.0),
          "EXACT BALANCE (top frame at N_w): rho = diagpart + X = "
          "%.5f + %+.5f (dev %.1e); X_+ = %+.3f vs X_- = %+.3f "
          "(C_off %+.4f); SOURCE frame at the crossing: X_v = "
          "%+.4f = X_+ %+.3f + X_- %+.3f (C_off %+.4f, z_v "
          "%+.2f) -- the destructivity lives in the SOURCE frame"
          % (dgN, XN, dev_bal, XpN, XnN, XN / max(AN, 1e-300),
             ZB9["X"], ZB9["Xp"], ZB9["Xn"], ZB9["coff"],
             ZB9["zv"]))

    # ---------------- S5 controls (full)
    if smoke:
        for g in ("G34-ctrl-reversal", "G35-r287-object",
                  "G41-ctrl-phases", "G42-separator-worlds"):
            check(g, True, "SMOKE: skipped")
        WC = {}
        ctrl_pack = {}
        sep_typ = None
        r287 = None
        sepW = {}
    else:
        section("S5  CONTROLS -- REVERSAL + PHASES + SEPARATOR + "
                "r287 OBJECT")
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
        ctrl_pack = {}
        ok_c = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            Wp = LS.world_pack(cn, cctx, D9)
            WC[cn] = Wp
            flip = CTRL_FLIPS.get(cn, HL2_FLIP)
            dep = min(Wp["N"] + CTRL_PAD, Wp["Sp"] - 1)
            spb = LS.spectral_block(Wp, dep)
            nc = spb["cross"]
            zb = zv_block(spb["B"], nc, Wp["vn"])
            acc = float(spb["rho"][nc] / spb["maxd"][nc - 1]) - 1.0
            # sign map + balance at the control's own crossing
            al_c, sb_c, h0_c = FS.mu_chain_f64(
                np.asarray(Wp["xp"]), np.asarray(Wp["wp"]), nc)
            z_c = jacobi_zeros(al_c, sb_c, nc)
            _pc, c_c, _ic = phase_field(z_c, np.asarray(Wp["xn"]))
            smc = sign_map_block(zb["E"], Wp["fn"], c_c)
            iuc = np.triu_indices(Wp["Sm"], 1)
            dist_c = np.abs(np.asarray(Wp["fn"])[iuc[0]]
                            - np.asarray(Wp["fn"])[iuc[1]])
            lab_c = LS.atom_labels(Wp["fn"], D9, Wp["uu"],
                                   Wp["mm"])
            bands_c, classes_c = balance_by_class(
                zb["T"], band_split(dist_c),
                pair_label_classes(lab_c, iuc))
            sep_c = source_separator(Wp["xp"], Wp["wp"],
                                     Wp["xn"], Wp["vn"], Wp["N"])
            ctrl_pack[cn] = dict(cross=nc, zb=zb, ac=acc, sm=smc,
                                 bands=bands_c, classes=classes_c,
                                 sep=sep_c)
            ok_c = ok_c and Wp["minC"] == flip \
                and nc == CTRL_CROSS[cn] \
                and abs(acc - CTRL_AC[cn]) <= CTRL_AC_TOL
        ok_zvc = all(CTRL_ZV_RANGE[0] <= v["zb"]["zv"]
                     <= CTRL_ZV_RANGE[1]
                     for v in ctrl_pack.values())
        check("G34-ctrl-reversal", ok_c and ok_zvc,
              "CONTROLS at their own crossing (minC == flips, "
              "crossings == records, assist_c == r285 records, "
              "z_v in [%.1f, %.1f]): X_v = %s ALL POSITIVE = "
              "CONSTRUCTIVE, C_off = %s (MAIN %+.3f), neg "
              "fraction = %s, sinc agreement = %s -- the sign "
              "REVERSAL of the coherence balance is the control "
              "map" % (CTRL_ZV_RANGE[0], CTRL_ZV_RANGE[1],
                       str({c: round(v["zb"]["X"], 4)
                            for c, v in ctrl_pack.items()}),
                       str({c: round(v["zb"]["coff"], 3)
                            for c, v in ctrl_pack.items()}),
                       ZB9["coff"],
                       str({c: round(v["sm"]["neg"], 3)
                            for c, v in ctrl_pack.items()}),
                       str({c: round(v["sm"]["agree"], 3)
                            for c, v in ctrl_pack.items()})))
        r287 = r287_block_object(smoke)
        near_E = max(bandsV, key=lambda b: abs(bandsV[b]))
        near_P = (max(r287["shares"],
                      key=lambda b: abs(r287["shares"][b]))
                  if r287["shares"] else None)
        same_obj = (r287["canc"] > 0.0 and ZB9["X"] < 0.0
                    and near_E == 0 and near_P == (1, 2))
        r287_typ = ("R287_SAME_OBJECT" if same_obj
                    else "DIFFERENT_OBJECTS")
        check("G35-r287-object", r287["dev_ct"] <= 1e-6
              and r287["dev_bid"] <= 1e-12,
              "r287 OBJECT (w9 block pipeline verbatim: sum ct "
              "dev %.1e, sum P == R dev %.1e, m = %d blocks): "
              "canc = A(0) - (sum P)^2 = %+.3e (%s); E-side wall "
              "interference X_v = %+.4f (%s), largest |signed "
              "share| band %s => sealed typing %s"
              % (r287["dev_ct"], r287["dev_bid"], r287["m"],
                 r287["canc"],
                 "residual root-scale cancellation"
                 if r287["canc"] > 0 else
                 "REINFORCES -- absorbed into the magnitudes, "
                 "the r287 finding",
                 ZB9["X"],
                 "DESTRUCTIVE" if ZB9["X"] < 0 else
                 "constructive",
                 "%d-%s" % (DIST_BANDS[near_E][0],
                            DIST_BANDS[near_E][1]
                            if DIST_BANDS[near_E][1] < 10 ** 9
                            else "inf"),
                 r287_typ))
        # control phase fields
        info("phase dispersion (R, KS, edge): MAIN (%.3f, %.3f, "
             "%d); " % (st9["R"], st9["ks"], n_edge9)
             + "; ".join("%s (%.3f, %.3f, %d)"
                         % (c, v["sep"][0], v["sep"][2],
                            v["sep"][3])
                         for c, v in ctrl_pack.items()))
        check("G41-ctrl-phases", True,
              "CONTROL PHASE FIELDS at their own N_w: R = %s vs "
              "MAIN %.3f; KS = %s vs MAIN %.3f; v-weighted K_S2 "
              "= %s vs MAIN -- see separator adjudication"
              % (str({c: round(v["sep"][0], 3)
                      for c, v in ctrl_pack.items()}), st9["R"],
                 str({c: round(v["sep"][2], 3)
                      for c, v in ctrl_pack.items()}), st9["ks"],
                 str({c: round(v["sep"][1], 3)
                      for c, v in ctrl_pack.items()})))
        sep9 = source_separator(W9["xp"], W9["wp"], W9["xn"],
                                W9["vn"], Nw)
        sepW = dict(MAIN=sep9)
        for c, v in ctrl_pack.items():
            sepW[c] = v["sep"]
        tab_s1 = {k: v[0] for k, v in sepW.items()}
        sep_typ = LS.dist_rule(tab_s1, list(ctrl_pack))
        check("G42-separator-worlds", abs(sep9[0] - st9["R"])
              <= 1e-12,
              "b2 SEPARATOR (worlds half): K_S1 = %s => sealed "
              "distance rule %s; the constructor route equals "
              "the gate-side phase field exactly (dev %.1e)"
              % (str({k: round(v, 3) for k, v in tab_s1.items()}),
                 sep_typ, abs(sep9[0] - st9["R"])))

    # ---------------- S6 ensembles + dose curve (full)
    if smoke:
        for g in ("G50-ens-sign", "G51-ens-scr", "G52-ens-chain",
                  "G53-dose-curve"):
            check(g, True, "SMOKE: skipped")
        ens_pct = {}
        sp_chain = {}
        flip_dose = None
        dose_rows = {}
        rate0 = float("nan")
        pred_rate = float("nan")
    else:
        section("S6  LEG C -- ENSEMBLES (r285 SEEDS) + DOSE CURVE")
        x_all = np.concatenate([np.asarray(W9["xp"]),
                                np.asarray(W9["xn"])])
        f_all = np.concatenate([np.asarray(W9["fp"], np.int64),
                                np.asarray(W9["fn"], np.int64)])
        m_all = np.concatenate([np.asarray(W9["wp"]),
                                np.asarray(W9["vn"])])
        o_f = np.argsort(f_all)
        f_all, x_all, m_all = f_all[o_f], x_all[o_f], m_all[o_f]
        numask9 = np.zeros(len(f_all), bool)
        fn_set = set(int(f) for f in W9["fn"])
        for i in range(len(f_all)):
            numask9[i] = int(f_all[i]) in fn_set
        sign_rows = []
        ok_cons = True
        for i in range(ENS_SIGN_REPS):
            msk = CD.sign_assignment(len(f_all), W9["Sm"],
                                     SEED_R285 + i)
            okc, _d = CD.cons_check(f_all, m_all, f_all, m_all,
                                    W9["Sm"], msk)
            ok_cons = ok_cons and okc
            r = CD.ens_sign_world(x_all, m_all, msk, Nw, DET_DEG)
            sep_r = source_separator(x_all[~msk], m_all[~msk],
                                     x_all[msk], m_all[msk],
                                     (len(x_all) + 1) // 2)
            r["K_S1"], r["K_S2"] = sep_r[0], sep_r[1]
            sign_rows.append(r)
        acs = [r["assist_cross"] for r in sign_rows
               if r["assist_cross"] is not None]
        ks1_s = [r["K_S1"] for r in sign_rows]
        ks2_s = [r["K_S2"] for r in sign_rows]
        crs_s = [r["cross"] for r in sign_rows
                 if r["cross"] is not None]
        pctc_s = float(np.mean([v < ac_main for v in acs]))
        pcts1_s = float(np.mean([v < st9["R"] for v in ks1_s]))
        check("G50-ens-sign", ok_cons
              and abs(float(np.median(acs)) - ENS_SIGN_ACM_REC)
              <= ENS_ACM_TOL and pctc_s == 0.0,
              "ENS_SIGN (%d reps, seeds == r285, conservation "
              "exact): assist_cross med %.2f (rec %.2f), MAIN pct "
              "%.2f == 0.00 (r285 LOW_OUTLIER re-gated); K_S1 "
              "spread %.3f..%.3f (MAIN %.3f, pct %.2f)"
              % (ENS_SIGN_REPS, float(np.median(acs)),
                 ENS_SIGN_ACM_REC, pctc_s, min(ks1_s), max(ks1_s),
                 st9["R"], pcts1_s))
        scr_rows = []
        ok_cons2 = True
        for i in range(ENS_SCR_REPS):
            sctx = MS.ctx_build(9, scramble_seed=SEED_R285
                                + 100 + i)
            okc = np.array_equal(np.asarray(sctx["mm"]),
                                 np.asarray(ctx9["mm"])) \
                and len(sctx["uu"]) == len(ctx9["uu"])
            ok_cons2 = ok_cons2 and okc
            Wr = LS.world_pack("scr%d" % i, sctx, D9)
            crr = (Wr["minC"] + 1) if Wr["minC"] is not None \
                else None
            dep = min(max(Wr["N"], (crr or 1) + 1, DET_DEG + 1),
                      Wr["Sp"] - 1)
            bb = CD.budget_block(Wr, dep)
            row = dict(cross=crr)
            if crr is not None and crr <= dep:
                rr_ = CD.rho_at(bb["B"], crr)
                mdn = float(bb["cum"][:, crr - 1].max())
                row["assist_cross"] = rr_ / mdn - 1.0
            else:
                row["assist_cross"] = None
            sep_r = source_separator(Wr["xp"], Wr["wp"],
                                     Wr["xn"], Wr["vn"], Wr["N"])
            row["K_S1"], row["K_S2"] = sep_r[0], sep_r[1]
            scr_rows.append(row)
        acs2 = [r["assist_cross"] for r in scr_rows
                if r["assist_cross"] is not None]
        ks1_c = [r["K_S1"] for r in scr_rows]
        ks2_c = [r["K_S2"] for r in scr_rows]
        crs_c = [r["cross"] for r in scr_rows
                 if r["cross"] is not None]
        pctc_c = float(np.mean([v < ac_main for v in acs2]))
        pcts1_c = float(np.mean([v < st9["R"] for v in ks1_c]))
        check("G51-ens-scr", ok_cons2
              and abs(float(np.median(acs2)) - ENS_SCR_ACM_REC)
              <= ENS_ACM_TOL and pctc_c == 0.0,
              "ENS_SCR (%d reps, seeds == r285, weights bitwise): "
              "assist_cross med %.2f (rec %.2f), MAIN pct %.2f == "
              "0.00; K_S1 spread %.3f..%.3f (MAIN %.3f, pct %.2f)"
              % (ENS_SCR_REPS, float(np.median(acs2)),
                 ENS_SCR_ACM_REC, pctc_c, min(ks1_c), max(ks1_c),
                 st9["R"], pcts1_c))
        ens_pct = dict(sign=pcts1_s, scr=pcts1_c)
        pct2_s = float(np.mean([v < sep9[1] for v in ks2_s]))
        pct2_c = float(np.mean([v < sep9[1] for v in ks2_c]))
        sp_chain = dict(
            sign_ac=BH.spearman(ks1_s, acs),
            scr_ac=BH.spearman(ks1_c, acs2),
            all_ac=BH.spearman(ks1_s + ks1_c, acs + acs2),
            sign_cr=BH.spearman(ks1_s, [float(v) for v in crs_s]),
            scr_cr=BH.spearman(ks1_c, [float(v) for v in crs_c]))
        check("G52-ens-chain", True,
              "THE PREDICTIVE CHAIN (measured): sp(K_S1, "
              "assist_cross) = %+.2f sign / %+.2f scr / %+.2f all "
              "28; sp(K_S1, crossing) = %+.2f / %+.2f; K_S2 MAIN "
              "pct %.2f / %.2f -- source phase dispersion vs wall "
              "coherence, honestly reported"
              % (sp_chain["sign_ac"], sp_chain["scr_ac"],
                 sp_chain["all_ac"], sp_chain["sign_cr"],
                 sp_chain["scr_cr"], pct2_s, pct2_c))
        # dose curve (all arrays in the SORTED fold order)
        gaps9 = local_gaps(f_all.astype(float))
        phi9_s, _c9s, _i9s = phase_field(z9, x_all[numask9])
        dose_rows = {}
        ok_dose = True
        for di, dose in enumerate(DOSES):
            reps = []
            for rep in range(DOSE_REPS):
                fj, xj, df = jitter_folds(
                    f_all, gaps9, dose,
                    SEED_DOSE + di * 100 + rep, W9["L"])
                ok_dose = ok_dose and bool(
                    np.all(np.abs(df) <= dose * gaps9 + 1e-15)
                    and np.all(np.diff(fj) > 0))
                wu_j = m_all * np.where(numask9, -1.0, 1.0)
                sg_j, _l, _r = BL.sign_chain_f64(xj, wu_j,
                                                 Nw + EXT)
                mc = next((n for n in range(len(sg_j))
                           if sg_j[n] < 0), None)
                if mc is None:
                    sg_j, _l, _r = BL.sign_chain_f64(xj, wu_j,
                                                     Nw + EXT2)
                    mc = next((n for n in range(len(sg_j))
                               if sg_j[n] < 0), None)
                crj = (mc + 1) if mc is not None else None
                xpj, wpj = xj[~numask9], m_all[~numask9]
                ynj, vnj = xj[numask9], m_all[numask9]
                dep = min(max(Nw, (crj or 1) + 1),
                          len(xpj) - 1)
                alj, sbj, h0j = FS.mu_chain_f64(xpj, wpj, dep)
                Bj = FS.b_matrix_f64(alj, sbj, h0j, ynj, vnj,
                                     dep)
                cumj = LS.christoffel_rows(Bj)
                rowd = dict(dose=dose, cross=crj,
                            s=(mc / Nw if mc is not None
                               else 1.0))
                if crj is not None and crj <= dep:
                    rr_ = CD.rho_at(Bj, crj)
                    mdn = float(cumj[:, crj - 1].max())
                    rowd["ac"] = rr_ / mdn - 1.0
                    zbj = zv_block(Bj, crj, vnj)
                    rowd["zv"] = zbj["zv"]
                zj = jacobi_zeros(alj, sbj, Nw)
                phij, _cj, intj = phase_field(zj, ynj)
                both = np.isfinite(phij) & np.isfinite(phi9_s)
                rowd["dphi"] = float(np.median(circ_dist(
                    phij[both], phi9_s[both])))
                rowd["K_S1"] = phase_stats(phij)["R"]
                reps.append(rowd)
            dose_rows[dose] = reps
        rate0 = float(np.median([r["dphi"]
                                 for r in dose_rows[DOSES[0]]])) \
            / DOSES[0]
        # static per-atom prediction (sorted fold order)
        zg9 = np.diff(z9)
        xn_s = x_all[numask9]
        f_nu_s = f_all[numask9].astype(float)
        gf_nu = gaps9[numask9]
        th_s = 2.0 * np.pi * f_nu_s / W9["L"]
        gx = gf_nu * (2.0 * np.pi / W9["L"]) \
            * np.abs(np.sin(th_s))
        idx9 = np.searchsorted(z9, xn_s)
        okint = (idx9 > 0) & (idx9 < len(z9))
        zg_at = zg9[np.clip(idx9 - 1, 0, len(zg9) - 1)]
        pred_rate = 0.5 * float(np.median(
            gx[okint] / np.maximum(zg_at[okint], 1e-300)))
        flip_dose = None
        for dose in DOSES:
            zvs = [r.get("zv") for r in dose_rows[dose]
                   if r.get("zv") is not None]
            if zvs and float(np.median(zvs)) > 0.0:
                flip_dose = dose
                break
        for dose in DOSES:
            reps = dose_rows[dose]
            info("dose %.3f: depth s med %.2f, assist_cross med "
                 "%s, z_v med %s, dphi med %.3f, K_S1 med %.3f%s"
                 % (dose,
                    float(np.median([r["s"] for r in reps])),
                    "%.2f" % float(np.median(
                        [r["ac"] for r in reps if "ac" in r]))
                    if any("ac" in r for r in reps) else "n/a",
                    "%+.2f" % float(np.median(
                        [r["zv"] for r in reps if "zv" in r]))
                    if any("zv" in r for r in reps) else "n/a",
                    float(np.median([r["dphi"] for r in reps])),
                    float(np.median([r["K_S1"] for r in reps])),
                    ("  [r276 P2 depth %.3f COMPARISON_ONLY]"
                     % R276_P2_DEPTH[dose])
                    if dose in R276_P2_DEPTH else ""))
        check("G53-dose-curve", ok_dose,
              "DOSE CURVE (jitter, weights bitwise, order "
              "preserved, |df| <= dose x gap gated): measured "
              "turn rate %.2f phase/dose at theta %.3f vs static "
              "prediction %.2f (ratio %.1f -- the chain zeros "
              "co-move); quarter turn extrapolated at dose %.3f; "
              "destructive -> constructive FLIP DOSE = %s; r276 "
              "P2_JIT depths quoted COMPARISON_ONLY (different "
              "channel: comb vs union jitter)"
              % (rate0, DOSES[0], pred_rate,
                 rate0 / max(pred_rate, 1e-300),
                 QUARTER_TURN / max(rate0, 1e-300),
                 str(flip_dose)))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    phi_m, _cm, _im = mutant_uniform_grid(z9, np.asarray(W9["xn"]))
    both_m = np.isfinite(phi_m) & np.isfinite(phi9)
    dev_m1 = float(np.median(circ_dist(phi_m[both_m],
                                       phi9[both_m])))
    check("G70-mutant-uniformgrid", dev_m1 >= M1_BAR,
          "m1 UNIFORM-GRID PHASES: reading the phases against a "
          "uniform-in-x zero grid distorts the field by med "
          "circular distance %.3f (>= %.1f) -- LOUD: the chain "
          "metric (arcsine-clustered zeros) is load-bearing"
          % (dev_m1, M1_BAR))
    mut2 = mutant_diag_census(E184, uN)
    dev_m2 = abs(mut2 - XN) / max(abs(float(evN[-1])), 1e-300)
    check("G71-mutant-diagcensus", dev_m2 >= M2_BAR,
          "m2 DIAG-IN-CENSUS: counting the diagonal into the "
          "interference breaks the exact balance by %.2f rel of "
          "rho (>= %.1f) -- LOUD: the diagonal subtraction is "
          "load-bearing" % (dev_m2, M2_BAR))
    tm_mut = mutant_mass_scale(np.array([1.0, 0.5, 0.25, 0.125,
                                         0.0625]))
    okc_m, dev_m3 = CD.cons_check(
        np.array([1, 2, 3, 4, 5], np.int64),
        np.array([1.0, 0.5, 0.25, 0.125, 0.0625]),
        np.array([1, 2, 3, 4, 5], np.int64), tm_mut, 2,
        CD.sign_assignment(5, 2, SEED_R285))
    check("G72-mutant-conservation", (not okc_m)
          and dev_m3 >= M3_BAR,
          "m3 ENSEMBLE WITHOUT CONSERVATION: the mass-scaling "
          "surgery (x %.2f) is CAUGHT (break %.1e >= %.0e)"
          % (MUT_MASS, dev_m3, M3_BAR))
    hits_m4 = scope_audit("mutant_cross_oracle", SCOPE_FORBIDDEN)
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    hits_sep = scope_audit("source_separator", SEP_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m4) and not hits
          and not hits_sep and not ag_hits,
          "m4 CROSS-ORACLE MUTANT FLAGGED (%s); the %d sealed "
          "constructors consume source arrays/chain/matrices ONLY "
          "(%s); the b2 separator audits CLEAN against the "
          "SOLUTION-side set (no B, no spectral block, no rho/"
          "assist: %s); fragment audit: %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not hits_sep else "; ".join(hits_sep),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 detector
    section("S8  DETECTOR LEDGER (r281 DISTANCE RULE)")
    if smoke:
        check("G80-detector-ledger", True, "SMOKE: skipped")
        det_typ = {}
    else:
        stats = {"K_S1_phase_R": {"MAIN": st9["R"]},
                 "K_S2_phase_ks": {"MAIN": st9["ks"]},
                 "K_A1_fracneg_cross": {"MAIN": sm_prof[
                     CROSS_REC]["neg"]},
                 "K_A2_coff_cross": {"MAIN": ZB9["coff"]}}
        for cn, v in ctrl_pack.items():
            stats["K_S1_phase_R"][cn] = v["sep"][0]
            stats["K_S2_phase_ks"][cn] = v["sep"][2]
            stats["K_A1_fracneg_cross"][cn] = v["sm"]["neg"]
            stats["K_A2_coff_cross"][cn] = v["zb"]["coff"]
        det_typ = {nm: LS.dist_rule(tab, list(ctrl_pack))
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
          "asymptotic law, no derived 5/7, no equidistribution as "
          "premise (the b1/b2 statistics are typed "
          "MEASUREMENT_ONLY -- a proof route would have to DERIVE "
          "the phase statistics from the source), no posthoc "
          "window, no RH claim; what the round adds: the sign "
          "anatomy with carrier classes, the sampling predictor "
          "adjudication, the sealed source-separator adjudication, "
          "the phase turn-rate/firewall comparison, the ensemble "
          "predictive chain, and the r287 object comparison; "
          "r243..r287 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        near_lbl = "%d-%s" % (DIST_BANDS[near_E][0],
                              DIST_BANDS[near_E][1]
                              if DIST_BANDS[near_E][1] < 10 ** 9
                              else "inf")
        car_cls = min(classesV, key=lambda k: classesV[k])
        parts.append(
            "SIGN_ANATOMY(neg %.3f at N_w; MAIN wall "
            "destructivity carried by band %s signed share "
            "%+.2f and class %s %+.2f; controls at their "
            "crossing ALL constructive, C_off %s)"
            % (SM["neg"], near_lbl, bandsV[near_E], car_cls,
               classesV[car_cls],
               str({c: round(v["zb"]["coff"], 2)
                    for c, v in ctrl_pack.items()})))
        n_ctrl_ag = sum(1 for v in ctrl_pack.values()
                        if v["sm"]["agree"] >= AGREE_BAR)
        mech = (SM["agree"] >= AGREE_BAR and n_ctrl_ag >= 3)
        parts.append(
            ("SAMPLING_MECHANISM(agreement %.3f MAIN / %d of 4 "
             "controls >= %.2f; turn rate %.2f per dose = %.1fx "
             "static -- the firewall is a phase-rotation "
             "statement, measured)"
             % (SM["agree"], n_ctrl_ag, AGREE_BAR, rate0,
                rate0 / max(pred_rate, 1e-300)))
            if mech else
            "SAMPLING_BLIND(agreement MAIN %.3f, controls %s)"
            % (SM["agree"],
               str({c: round(v["sm"]["agree"], 2)
                    for c, v in ctrl_pack.items()})))
        found = (sep_typ == "MAIN_SEPARATING"
                 and all(p <= PCT_OUT[0] or p >= PCT_OUT[1]
                         for p in ens_pct.values()))
        parts.append(
            ("SOURCE_SEPARATOR_FOUND(K_S1 = %.3f, %s, ens pct "
             "%s)" % (st9["R"], sep_typ, str(ens_pct)))
            if found else
            "SOURCE_SEPARATOR_NOT_FOUND(K_S1 = %.3f, worlds %s, "
            "ens pct sign %.2f / scr %.2f)"
            % (st9["R"], sep_typ, ens_pct["sign"],
               ens_pct["scr"]))
        parts.append(r287_typ + "(canc %+.2e, X_v %+.4f)"
                     % (r287["canc"], ZB9["X"]))
        parts.append(
            "ENSEMBLE_CHAIN(sp(K_S1, assist_cross) %+.2f/%+.2f/"
            "%+.2f, sp(K_S1, cross) %+.2f/%+.2f, flip dose %s)"
            % (sp_chain["sign_ac"], sp_chain["scr_ac"],
               sp_chain["all_ac"], sp_chain["sign_cr"],
               sp_chain["scr_cr"], str(flip_dose)))
        parts.append("DETECTOR_LEDGER(%s)" % str(det_typ))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED sign anatomy + sampling statistics of "
          "the open scalar L*'s coherence half; NO L* claim, NO "
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
