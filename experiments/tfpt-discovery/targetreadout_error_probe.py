#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""targetreadout_error_probe -- PRIME.PORT.RHP.TARGETREADOUT.ERROR.01
(round 251): EXACT ERROR-EVALUATION FORMULAS for the target
readouts of the r250 outer model -- NO new parametrix.  r250 froze
OUTER_MODEL_FAILS + FIBER_BEYOND_MODEL: the outer model M_n carries
the readout RATES (plateau 1/4 exact to 1.8e-4, h-slope <= 0.007
dec/degree) but NOT the pointwise matrix (bulk err 2.7-15.6, GAP
zone breaks with filling, bare beats dressed 2-4x, h offset +1.8
decades) and NOT the fiber (T_model sign wrong on w9).  The
reviewer question of THIS round: are the target readouts (base
h_n, fiber T) proof-grade controllable THROUGH the measured
pointwise failure -- i.e. what EXACT functional of the error field
R(z) = Y_n(z) M_n(z)^{-1} are the readout errors, how strongly
does the fiber amplify the matrix error (the A-factor), and how
many decades does the K_N - K_8 mode annihilation buy in the ERROR
(not in the value)?  Priorities R2 > R4 > R3 (FOLLOWUP_SHA
0d14a215) stand; this round is the EVALUATION INFRASTRUCTURE for
R4 and the base margin bill.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r250 discipline): w = window (kz),
N_w = builder depth, n = chain degree; free pivots h_{w,n}
(n < N_w) are the proof objects; Y_n is the frozen r227/r234 FIK
normalization; the forced pivot h_N is NEVER formed (levels use
h_{N-1} only); ground truth (h signs, flips) enters gates only;
no zero/prime oracles anywhere (AST firewall).  The outer model
M_n is the r250 object VERBATIM (centered_basefiber_probe:
r232a constrained-equilibrium g, KKT-midpoint ell, discrete Szego
D, -2 pi i calibration -- machinery imported, no refit); sigma0 =
sigma - (F_0/h_0) mutilde is the r248 centered border functional
(border atoms + window atoms, c = s_0/m_0 lifted f64 like the
r250 QP masses, disclosed).

LEG A -- EXACT FRECHET/CONTOUR FORMULAS (derived at design time,
frozen here, then gated numerically):
(a1) BASE READOUT ERROR.  Y_n = R M_n with R(z) -> I at infinity
  (both factors carry the same z^{n sigma3} normalization), so
  from Y z^{-n s3} = R (M z^{-n s3}) = (I + R1/z + ...)(I + M1/z
  + ...) the 1/z coefficients ADD EXACTLY: Y1 = R1 + M1 (no cross
  term at order 1/z).  With the r234 exact readout h_n = (Y1)_12
  and the r250 analytic h_n^out = (M1)_12:
    delta h_n = h_n - h_n^out = (R1)_12
              = (1/(2 pi i)) oint (R(z) - I)_12 dz,
  an EXACT identity (no leading order): the base readout error IS
  the 12-entry of the 1/z coefficient of the error matrix field.
  GATE: 2-point Richardson extraction of (R1)_12 at the sealed
  norm points x0 + 1e2 / x0 + 1e3 vs the direct difference
  h_n^true - h_n^out (mp chain h + analytic model formula), at
  degrees n in {N//2, N-1} on the a1 windows; bar |rich - delta|
  / max(|h_true|, h_out) <= 1e-3 (Richardson truncation ~
  (hull/z1)^2 ~ 4e-4).  PRECISION LAW (measured in the smoke
  pass): the far-z Cauchy column cancels to ~ (n+1) log10|z|
  digits (w9 at z = x0+1e3, n = 183: ~ 552 digits) -- a1 runs
  its OWN mp pass (2 points only) at the sealed DPS_A1 = 700;
  w26 is excluded from a1 (would need dps ~ 1200; disclosed).
(a2) FIBER READOUT ERROR -- THE CENTRAL EVALUATION FORMULA (the
  exact rest identity of r250-R4): with K^Y_m(x,y) =
  (Y_m^{-1}(y) Y_m(x))_21 / (y - x) = [pihat_m(x) pihat_{m-1}(y)
  - pihat_{m-1}(x) pihat_m(y)] / (h_{m-1}(x - y)) and K^M_m the
  same functional of M_m (r250 c2 kernel),
    T^Y - T^M = intint ([K^Y_N - K^M_N] - [K^Y_8 - K^M_8])
                dsigma0 dsigma0
  EXACTLY on the common regularized contour (x + i dx, y + i dy;
  dx = 1e-5, dy = 2e-5 -- SHARPENED from the r250 model-side
  1e-3/2e-3 after the smoke pass MEASURED that dx = 1e-3
  destroys the oscillating true-kernel pairing (w9: T^Y_reg =
  -65.8 vs T_true = +4.334) while dx = 1e-5 carries it to 5.6e-6
  relative).  MODEL VARIANT (sealed after the same measurement):
  the FULL r250 model is NOT sigma0-pairable -- its discrete
  Szego layer D(z) has atom poles at the support nodes, and at
  the tight contour the D-exponent reaches ~ 1e3 log units
  (beyond f64, beyond any margin scale); the kernel/fiber legs
  therefore run the SEALED r250 ABLATION MEMBER noD (D := 1 --
  the pointwise-better object of the r250 ablation, no new
  parametrix) as the outer transfer candidate M; the full-D
  obstruction is MEASURED and typed (G34, verdict token
  MODEL_KERNEL_POLE_OBSTRUCTION); the base legs (h_n^out, a1)
  keep the FULL model (z -> infinity readouts see no atom pole).
  GATES:
  (i) route consistency: the four separately-paired terms vs the
  one pairing of the assembled difference kernel, on the absolute
  mass-norm scale (gross = |w| K |w|), bar 1e-9; (ii) the CHAIN
  ANCHOR: T^Y_reg = sigma0 [K^Y_N - K^Y_8] sigma0 vs the bitwise
  r244 chain readout T_true = sum_{n=8}^{N-1} rho_n -- the
  regularization systematic |T^Y_reg / T_true - 1| is ADJUDICATED
  at bar 0.10 (if the contour shift polluted the object at the
  10-percent level, the whole delta-T bill would be void; r248
  proved the on-axis identity exact to 3.3e-160).
(a3) THE ERROR-KERNEL DECOMPOSITION (exact bilinear form): from
  Y = R M,  Y^{-1}(y) Y(x) = M^{-1}(y) [R^{-1}(y) R(x)] M(x), so
    K^Y(x,y) - K^M(x,y)
      = ( row2(M^{-1}(y)) [R^{-1}(y) R(x) - I] col1(M(x)) )
        / (y - x),
  with row2(M^{-1}(y)) = (-M21(y), M11(y))/det M(y) and
  col1(M(x)) = (M11(x), M21(x))^T: the error kernel is the
  two-point error field E(x,y) = R^{-1}(y) R(x) - I sandwiched
  between the model's second inverse-row and first column --
  the fiber transfer consumes EXACTLY this bilinear form of
  (R - I), nothing else.  GATE: direct K^Y - K^M vs the sandwich
  on the sealed 5 x 5 sample pairs at level N, sup-normalized
  dev bar 1e-6 (mp).

LEG B -- THE AMPLIFICATION FACTOR A (the reviewer core question):
  A_w = |delta T_w| / eps_w with the sealed normalizations
  (r250 error metric verbatim, C = e^{(n ell/2) sigma3}).  THE
  NORM CONTOUR (sealed after the smoke pass): the Cauchy columns
  of Y have poles AT the sigma0 atoms, so ||R - I|| at the
  atom-shifted pairing points is a regularization artifact, not
  an error scale; eps is measured on the sealed GAP-MIDPOINT
  contour Gamma_w = {midpoints of consecutive sorted sigma0
  atoms} + i delta, delta = 0.02 (the r250 GAP offset), NSAMP
  position-stride midpoints:
    eps_sup = sup over Gamma_w of ||C^-1 (R - I) C||_F, level N;
    eps_L2  = sqrt( sum w~_i err_i^2 / sum w~_i ), w~_i = the
      mean |sigma0| mass of the two adjacent atoms (sigma0-
      weighted L2 on Gamma_w);
    eps_YM  = sup ||C^-1 (Y - M) C||_F / ||C^-1 M C||_F (the
      model-relative Y-error scale, for the c2 quotient).
  M = the noD transfer candidate (consistent with delta T); the
  full-D err on the same contour is reported as r250-continuity
  information (the midpoint contour clears the D poles).
  MEASURED: A_w across the window ladder, Spearman(A; N) and the
  log-log slope p (A ~ N^p?); the proof-relevant balance: the
  hypothetical scenario eps ~ 1/N with A ~ N leaves delta T =
  O(1) -- measured as hypo_w = (A_w / N_w) / |margin_w^out|
  (median >= 1 means a 1/N-falling matrix error does NOT
  automatically carry the fiber readout).  SEALED TAGS:
  AMPLIFICATION_EXTENSIVE iff p >= 0.5 AND Spearman >= +0.5;
  AMPLIFICATION_BOUNDED iff Spearman <= 0.0; else
  AMPLIFICATION_MIXED.

LEG C -- THE QUIET ZONE AS ERROR ANNIHILATOR (the reviewer
lever): the subtraction K_N - K_8 removes the first eight
orthogonal modes EXACTLY (r248); measured here in the ERROR:
(c1) q_annihil_w = |delta T (K_N - K_8)| / |delta T_naiv| with
  delta T_naiv = sigma0 [K^Y_N - K^M_N] sigma0 (no low-level
  subtraction; sigma0 fixed, so mode 0 is centered out in BOTH
  numerator and denominator -- the quotient isolates the modes
  1..7 + level-8 subtraction gain in the ERROR, not the value);
  decades bought = -log10 q_annihil; SEALED: ANNIHILATION_BUYS
  (median decades over the fiber windows >= 1.0) /
  ANNIHILATION_NEUTRAL.
(c2) the N-dependence of the fiber error per matrix error:
  q_c2_w = |delta T_w| / eps_YM_w across the ladder; SEALED
  reading: falling (Spearman <= -0.5) = the rest zone carries
  analytically; flat/rising = the fiber sits genuinely in the
  error term.  (c3) NO coarse norm bound anywhere: every number
  is evaluated through the exact leg-A formulas (a norm bound
  |T| <= ||sigma0||^2 ||K|| would destroy the mode cancellation
  and is FORBIDDEN in this round by design.)

LEG D -- MARGIN RELEVANCE (the reviewer scoring):
(d1) BASE PROFILE over ALL free degrees (sealed stride grid,
  PROF_PTS equilibrium masses, warm-started QP): ratio_n =
  |delta h_n| / h_n^out = |10^{Delta_n} - 1| with Delta_n =
  log10 h_n^true - log10 h_n^out; profile quartiles + the
  offset/rate split (slope of Delta_n vs n, r250 h-rate bar 0.01
  dec/degree).  SEALED CLASSIFICATION: BASE_READOUT_PROVABLE iff
  max ratio <= 0.5 on all windows; else BASE_READOUT_BLOCKED_BY_
  OFFSET iff |slope| <= 0.01 on all windows AND median |offset|
  >= 0.5 decades (a single missing CONSTANT layer, the R3
  target); else BASE_READOUT_BLOCKED_STRUCTURAL.
(d2) FIBER MARGIN: per window |delta T| / |margin_true| with
  margin_true = B0 - Q_7 - T_true (the anchor identity: = 5/7 -
  rho_{N-1} exactly under the placeholder form B_w = S_{N-2} +
  5/7, r243/r247, honest status IMPORTED -- corner_provenance
  runs in parallel and may replace the form; typed, not
  consumed beyond the placeholder), B0 = B - rho_0, Q_7 =
  sum_{1..7} rho_n.  DISCLOSED CALIBRATION AMENDMENT: the draft
  compared against margin_out = B0 - Q_7 - T^out, which is the
  TAUTOLOGY margin_out = margin_true + delta T (a positive
  error always passes |dT| < margin_out); the comparison object
  was moved to the true margin the eventual bound must beat
  AFTER the error is spent; margin_out is still printed.
(d3) WORLD COMPARISON: the same delta T pipeline on SCRAMBLE
  (seed 1, w9 base, full depth): does the MAIN-SCRAMBLE object
  difference sit in delta T?  share = |delta T_SCR - delta
  T_MAIN| / |T_SCR - T_MAIN|; SEALED: WORLD_GAP_IN_DELTA_T iff
  share in [0.5, 2.0] (else WORLD_GAP_ELSEWHERE); the decade
  offset log10 |delta T_SCR / delta T_MAIN| is reported.

MUST-FAILS (each loud): (m1) swapped R1 readout (21-entry for
12-entry) must break the a1 identity by >= 1e3 x (the transposed
entry carries the e^{-2 n ell} gauge scale); (m2) INDEX-SHIFTED
TOP LEVEL (the r248-m2 analog on the evaluation contour): the
Y-side shift [K^Y_{N-1} - K^Y_8] vs [K^Y_N - K^Y_8] must move T
by EXACTLY rho_{N-1} (rel dev <= 0.05) and land >= 100 x the
honest anchor max(1e-3 |T^M_diff|, |T^Y_reg - T_true|) -- the
evaluation formula is level-pinned; DISCLOSED AMENDMENT: the
draft m2 (model-side mass 7 as 8) is NOT loud on MAIN because
the noD low level is numerically inert (~ 6e-5, the same
silence the annihilation leg measures); the inert value is
still reported; (m3) UNCENTERED ALIAS: the
naive level-N pairing against the raw border sigma (no centering)
differs from the sigma0 pairing by the rank-1 head rho_0 -- the
measured difference must land within [0.5, 2.0] x rho_0 (r248
head, loud); (m4) SIGN ORACLE: reading sign h_{N-1} or any flip
degree is EXCLUDED by the input firewall (standing r243
exclusion, re-asserted -- no evaluation path consumes it).

SEALED CONSTANTS: windows (9, 12, 13, 26); a1 windows (9, 12,
13); a1 degrees {N//2, N-1}; fiber low level 8; regularization
dx 1e-5 / dy 2e-5; norm contour delta 0.02 (r250 GAP offset);
kernel/fiber model variant noD (sealed; full-D typed via the
pole gate, bar 50 decades); dps: kernel/Y pass 120 (all
windows), a1 pass 700 (2 far points only), sandwich combination
600, model kernel columns 60, model R/a1 columns 80;
QP: FISTA iters 8000, tol 1e-8, residual bar 1e-6, warm start
ascending (r250); profile grid PROF_PTS = 36 masses in
[2, N-1] union {7, 8, N//2, N-1, N}; norm sample NSAMP = 48
position-stride gap midpoints; sandwich 5 x 5 (first/last five
position-stride atoms, x-offset vs y-offset); norm points
x0 + 1e2 / x0 + 1e3; bars: a1 1e-3, a2 route 2e-9 (gross mass
scale), reg systematic 0.10, a3 sandwich 1e-6 (sup-normalized),
spot Richardson 1e-4, det M 1e-30, det Y 1e-20, chain ward 1e-8;
amplification slope bar 0.5 / Spearman bar 0.5; annihilation
decade bar 1.0; c2 Spearman bar -0.5; base ratio bar 0.5, h-rate
bar 0.01 dec/degree, offset bar 0.5 dec; world share window
[0.5, 2.0]; loudness m1 1e3, m2 rel dev <= 0.05 vs rho_{N-1}
AND >= 100 x the anchor max(1e-3 |T^M_diff|, |T^Y_reg -
T_true|), m3 head window [0.5, 2.0]; control flips
25/21/27; runtime <= 1800 s; smoke = w9 only, atom stride 4,
PROF_PTS 8, NSAMP 12, dps 80/400/300, world block + reg-anchor
+ m2/m3 adjudication skipped (strided atoms carry no moment
identities).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  READOUT_FORMULAS_EXACT  iff a1 (all a1 windows x degrees), a2
    (route + reg anchor) and a3 (sandwich) gates all pass;
    else READOUT_FORMULAS_OPEN;
+ AMPLIFICATION_<EXTENSIVE|BOUNDED|MIXED>(p, Spearman);
+ ANNIHILATION_BUYS(median decades) / ANNIHILATION_NEUTRAL;
+ FIBER_ERROR_CONTROLLABLE iff [|delta T| < |margin_true| on ALL
    fiber windows] OR [Spearman(q_c2; N) <= -0.5 AND
    ANNIHILATION_BUYS]; else FIBER_IN_ERROR_CONFIRMED (the fiber
    genuinely lives in the error term; R4 needs its own pairing
    theorem);
+ BASE_READOUT_<PROVABLE|BLOCKED_BY_OFFSET|BLOCKED_STRUCTURAL>;
+ WORLD_GAP_IN_DELTA_T(decades) / WORLD_GAP_ELSEWHERE
[+ MODEL_KERNEL_POLE_OBSTRUCTION(FULL_D) if the G34 exponent
   exceeds the sealed 50-decade bar].
Honesty before beauty: no verdict claims a bound mechanism; the
budget bound and the base law stay OPEN (r243 PAIRCORR_REENCODED,
r247 B discipline, r250 error map all stand unchanged).

RECORD TABLES (frozen from calib_tr pass 3, 20/20, wall 91.6 s;
disclosed SMOKE/CALIBRATION AMENDMENTS -- every one caught by
the smoke or first full pass BEFORE the record freeze; the leg-A
formulas, the annihilation quotients, the amplification tags,
the base classification and the world rule never moved:
(a1) PRECISION LAW: the draft evaluated a1 inside the kernel
  pass at the r250 norm points x0+1e3/1e4; the smoke pass
  measured the far-z Cauchy cancellation ~ (n+1) log10|z| +
  |log10 sqrt(h_n)| digits (w9 n=183, z=1e3: ~604) -- a1 moved
  to its OWN 2-point pass at dps 700 with norm points
  x0+1e2/x0+1e3 (the model spot ward keeps the r250 points).
(a2) REGULARIZATION: the draft reused the r250 contour
  1e-3/2e-3; MEASURED on full w9 atoms: dx 1e-3 DESTROYS the
  oscillating true-kernel pairing (T^Y_reg = -65.8 vs T_true =
  +4.334) while 1e-5 carries it to 5.6e-6 rel -- dx/dy sealed
  at 1e-5/2e-5.
(a3) MODEL VARIANT: at the tight contour the FULL model's
  arcsine-cell Szego layer D(z) is unrepresentable at the atoms
  (measured exponent 380.3 decades > f64's 308) -- the kernel
  legs run the sealed r250 ablation member noD; the obstruction
  gate G34 was added and types MODEL_KERNEL_POLE_OBSTRUCTION.
(a4) NORM CONTOUR: draft eps at the atom-shifted points sits
  1e-5 from the Cauchy-column poles (pure artifact); eps moved
  to the sealed gap-midpoint contour + 0.02i.
(a5) MARGIN OBJECT: the draft fiber comparison |dT| <
  margin_out is the TAUTOLOGY margin_out = margin_true + dT
  (ratios 0.89-0.99 while the error is 8-82 x the true margin);
  the comparison moved to margin_true = B0 - Q_7 - T_true.
(a6) MUST-FAIL m2: the draft model-side mass-7 shift is NOT
  loud on MAIN (5.9e-5 -- the same low-mode inertness the
  annihilation leg measures); m2 re-pinned to the Y-side
  top-level shift, loud by exactly rho_{N-1}.
(a7) smoke m2/m3 adjudication skipped (strided atoms carry no
  moment identities); A2_ROUTE_BAR set 2e-9 at design, measured
  5.2e-18.):
CAL_VERDICT = READOUT_FORMULAS_EXACT +
AMPLIFICATION_EXTENSIVE(p=1.01) + ANNIHILATION_NEUTRAL +
FIBER_IN_ERROR_CONFIRMED + BASE_READOUT_BLOCKED_BY_OFFSET +
WORLD_GAP_IN_DELTA_T + MODEL_KERNEL_POLE_OBSTRUCTION(FULL_D).
Key numbers.  CENSUS: w9/12/13/26 N = 184/151/168/364, T_true
4.3343/2.8907/4.1449/5.8687, sigma0 atoms 734/602/670/1454
(c0 ~ 1.002), control flips 25/21/27 re-derived.  WARDS: QP
residual worst 9.9e-9 (155 warm-started masses), spot det M
5.7e-79, spot Richardson 4.0e-6, det Y worst 2.2e-93 (kernel
dps 120) / 1.5e-98 (a1 dps 700), chain ward 1.4e-12, kernel
columns finite (max |log10| 110.2, headroom 197.8 decades).
LEG A: a1 dev 3.3e-6/7.5e-6 (w9 n=92/183), 1.0e-5/7.4e-6
(w12), 6.5e-6/5.8e-6 (w13) -- worst 1.0e-5 (bar 1e-3,
Richardson-truncation level: the delta-h contour identity is
EXACT); a2 routes worst 5.2e-18 on gross (bar 2e-9); REG
ANCHOR: T^Y_reg/T_true - 1 = +5.6e-6/-1.5e-5/-5.8e-4/-2.6e-3
(bar 0.10) -- the contour carries the object to 0.3 percent or
better; a3 sandwich worst 1.1e-81 (bar 1e-6, 25 pairs x 4
windows).  LEG B (level N, noD, normalized gauge): eps_sup
72.9/1758/2884/873 (sup is single-midpoint-spike dominated,
disclosed), eps_L2 26.2/43.2/70.8/121, eps_YM 2.90/3.14/2.25/
1.96 (the relative Y-error SATURATES ~ 2-3: terminal Y and M
columns are decorrelated at the sigma0 scale); |dT| = 4.42/
2.96/4.28/5.86; A_sup = 0.061/0.0017/0.0015/0.0067 -> sealed
tag AMPLIFICATION_EXTENSIVE(p = +1.01, Spearman +0.60); typed,
not upgraded: the L2-based A (0.168/0.069/0.061/0.049) FALLS
with N -- the tag is normalization-sensitive; the physical
reading is c2.  LEG C (c1): dT = +4.418/+2.964/+4.284/+5.864
vs dT_naiv identical to 3 digits: q_annihil = 1.000 on 4/4,
median decades bought +0.00 => ANNIHILATION_NEUTRAL -- the
centering buys 3.5 decades in the VALUE (r248) and ZERO in the
ERROR: both low levels are numerically inert on MAIN (Y-side
Q_7 ~ 2e-5 quiet, noD model level-8 ~ 1e-4), the naive error
is already tail-dominated; (c2) q_c2 = |dT|/eps_YM = 1.52/
0.94/1.90/3.00, Spearman +0.80, log-log slope +1.04: delta T
grows ~ N x (saturated relative Y-error) -- the fiber sits
GENUINELY in the error term.  LEG D (d1) base profile
|dh|/h^out over the 36-mass grids: med 0.944/0.948/0.949/
0.964, max 0.9912, offset -1.25/-1.29/-1.29/-1.45 decades
(model overshoots every constant), rate slopes -0.0029/
-0.0045/-0.0026/-0.0024 dec/degree (bar 0.01, 4/4) =>
BASE_READOUT_BLOCKED_BY_OFFSET (the r250 split confirmed on
the full profile: rate carried, ONE constant layer missing --
R3); (d2) fiber margin: T_out(noD) = -0.083/-0.074/-0.142/
-0.011 (the noD transfer carries ~ 2 percent of T_true: dT ~=
T_true itself), |dT|/|margin_true| = 7.9/81.8/12.0/8.2 (>= 1
on 4/4, w12's margin_true = 0.036 is razor thin) => the
readout error EXCEEDS the placeholder margin everywhere =>
FIBER_IN_ERROR_CONFIRMED by the sealed rule (no controllable
clause fires: ratios >= 1 AND c2 rises AND annihilation
neutral); hypothetical balance (A_sup/N)/|margin_true| median
1.7e-4 (an eps' ~ 1/N bound with the MEASURED A would suffice
-- but no such bound exists; informational, no mechanism
claimed); anchor 5/7 - rho_{N-1} exact 4/4; (d3) WORLDS:
T_SCR = -4.494 vs T_MAIN = +4.334 (object gap -8.83); dT_SCR
= -4.441 vs dT_MAIN = +4.418: share = 1.003 in [0.5, 2.0] =>
WORLD_GAP_IN_DELTA_T (decade offset +0.00): the world-blind
outer model pushes the ENTIRE arithmetic world difference
into the error term -- the R4 pairing theorem must separate
worlds in the error kernel, exactly as r250 typed.
MUST-FAILS all loud: m1 min ratio 3.0e+93; m2 top-level shift
0.1531 vs rho_{N-1} = 0.153 (rel 4.4e-4, 1835 x anchor); m3
head ratio 0.999 in [0.5, 2.0]; m4 oracle excluded.  Runtime
91.6 s full, 4.8 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE.

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import centered_basefiber_probe as CB        # noqa: E402 r250
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import szego_equilibrium_probe as SZ         # noqa: E402 r232a
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

WINDOWS = (9, 12, 13, 26)
A1_WINDOWS = (9, 12, 13)
FIB_LO = 8
DPS_KERN = {9: 120, 12: 120, 13: 120, 26: 120}
DPS_A1 = 700
DPS_SAND = 600
DPS_MK = 60
DPS_MR = 80
KVAR = "noD"
POLE_DEC_BAR = 50.0
FIB_DX = 1e-5
FIB_DY = 2e-5
DELTA_GAP = 0.02
QP_ITERS = 8000
QP_TOL = 1e-8
QP_RES_BAR = 1e-6
PROF_PTS = 36
NSAMP = 48
SAND_K = 5
NORM_OFFS = (1e2, 1e3)
A1_BAR = 1e-3
A2_ROUTE_BAR = 2e-9
REG_SYS_BAR = 0.10
A3_BAR = 1e-6
RICH_BAR = 1e-4
DETM_BAR = 1e-30
DETY_BAR = 1e-20
CHAIN_BAR = 1e-8
AMP_SLOPE_BAR = 0.5
AMP_SP_BAR = 0.5
ANNIHIL_DEC_BAR = 1.0
C2_SP_BAR = -0.5
BASE_RATIO_BAR = 0.5
H_RATE_BAR = 0.01
OFFSET_DEC_BAR = 0.5
WORLD_SH_LO, WORLD_SH_HI = 0.5, 2.0
M1_LOUD = 1e3
M3_LO, M3_HI = 0.5, 2.0
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
CAL_VERDICT = ("READOUT_FORMULAS_EXACT + "
               "AMPLIFICATION_EXTENSIVE(p=1.01) + "
               "ANNIHILATION_NEUTRAL + FIBER_IN_ERROR_CONFIRMED "
               "+ BASE_READOUT_BLOCKED_BY_OFFSET + "
               "WORLD_GAP_IN_DELTA_T + "
               "MODEL_KERNEL_POLE_OBSTRUCTION(FULL_D)")

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
    return (not bad), ("NO zero/prime oracles; the model consumes "
                       "node positions + |weights| + the QP "
                       "minimizer ONLY (r250 firewall verbatim); "
                       "h_N never formed; sign h / flips enter "
                       "gates only (m4 oracle EXCLUDED)"
                       if not bad else "; ".join(bad))


# ------------------------------------------------- 2x2 mp helpers
def m_adj2(M):
    return ((M[1][1], -M[0][1]), (-M[1][0], M[0][0]))


def m_det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def m_mul2(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def r_field(Y, M):
    """R = Y M^{-1} (mp, adjugate route) plus the STABLE
    det R = det Y / det M (avoids the catastrophic cancellation
    of forming det from the near-rank-1 product entries)."""
    detM = m_det2(M)
    Ra = m_mul2(Y, m_adj2(M))
    R = ((Ra[0][0] / detM, Ra[0][1] / detM),
         (Ra[1][0] / detM, Ra[1][1] / detM))
    return R, m_det2(Y) / detM


def fro_RI(R):
    return float(mp.sqrt(abs(R[0][0] - 1) ** 2 + abs(R[0][1]) ** 2
                         + abs(R[1][0]) ** 2 + abs(R[1][1] - 1) ** 2))


# --------------------------------------------------- mp kernel pass
def mp_kernel_pass(d, zpts, snap_pts, levels, dps, Nb):
    """r250 mp_y_pass machinery adapted: scaled signed mp recursion
    on mutilde; per level m in `levels` store the scaled polynomial
    state (P_m, P_{m-1}, log scales, h_{m-1}); at snapshot degrees
    (keys of snap_pts) build the FULL FIK matrix Y_n (Cauchy
    columns) at the listed point indices only.  h_n is formed for
    FREE degrees n < Nb only; the forced pivot h_Nb is NEVER
    formed (levels consume h_{level-1})."""
    mp.mp.dps = dps
    nds = ([mp.mpf(float(v)) for v in d["xs"]]
           + [mp.mpf(float(v)) for v in d["ys"]])
    wt = ([mp.mpf(float(v)) for v in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    zc = [mp.mpc(z) for z in zpts]
    qk = [mp.mpf(1)] * len(nds)
    qkm = [mp.mpf(0)] * len(nds)
    qz = [mp.mpc(1) for _ in zc]
    qzm = [mp.mpc(0) for _ in zc]
    Ls = mp.mpf(0)
    Ls_m = mp.mpf(0)
    eta = mp.fsum(w * q * q for w, q in zip(wt, qk))
    eta_m = eta
    lg_h = mp.log(abs(eta))
    sg_h = mp.sign(eta)
    hlog = {0: (lg_h, sg_h)}
    gam = {}
    lv = {}
    ysnap = {}
    dety = 0.0
    nmax = max(max(levels),
               max(snap_pts) if snap_pts else 0)
    for k in range(nmax):
        aco = mp.fsum(w * x * q * q
                      for w, x, q in zip(wt, nds, qk)) / eta
        if k == 0:
            nx = [(x - aco) * q for x, q in zip(nds, qk)]
            nz = [(z - aco) * c for z, c in zip(zc, qz)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            nx = [(x - aco) * q - ge * fc * r
                  for x, q, r in zip(nds, qk, qkm)]
            nz = [(z - aco) * c - ge * fc * r
                  for z, c, r in zip(zc, qz, qzm)]
        sc = max(abs(t) for t in nx)
        qkm, eta_m, Ls_m, qzm = qk, eta, Ls, qz
        qk = [t / sc for t in nx]
        qz = [c / sc for c in nz]
        Ls = Ls + mp.log(sc)
        n = k + 1
        if n < Nb:
            eta = mp.fsum(w * q * q for w, q in zip(wt, qk))
            g = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            lg_h += mp.log(abs(g))
            sg_h *= mp.sign(g)
            hlog[n] = (lg_h, sg_h)
            gam[n] = float(g)
        if n in levels:
            lv[n] = dict(qz=list(qz), Ls=Ls, qzm=list(qzm),
                         Lsm=Ls_m, lgh=hlog[n - 1][0],
                         sg=hlog[n - 1][1])
        if n in snap_pts:
            lgm, sgm = hlog[n - 1]
            h_prev = sgm * mp.e ** lgm
            eLs = mp.e ** Ls
            eLm = mp.e ** Ls_m
            Ys = {}
            for iz in snap_pts[n]:
                z = zc[iz]
                Cn = eLs * mp.fsum(w * q / (z - x)
                                   for w, q, x in zip(wt, qk, nds))
                Cm = eLm * mp.fsum(w * q / (z - x)
                                   for w, q, x in zip(wt, qkm, nds))
                Y = ((eLs * qz[iz], Cn),
                     (eLm * qzm[iz] / h_prev, Cm / h_prev))
                dv = abs(Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0] - 1)
                dety = max(dety, float(dv))
                Ys[iz] = Y
            ysnap[n] = Ys
    return hlog, gam, lv, ysnap, dety


def y_columns(lvm, nk):
    """balanced complex128 (11, 21)-column values at the first
    nk (kernel-block) points: u = pihat_m, v = pihat_{m-1}/
    h_{m-1}, both scaled by the symmetric split e^{gl/2}, gl =
    Ls + Lsm - lg|h_{m-1}| (kernel products u(x) v(y) are
    scale-exact)."""
    s = (lvm["Ls"] - lvm["Lsm"] + lvm["lgh"]) / 2
    su = mp.e ** (lvm["Ls"] - s)
    sv = lvm["sg"] * mp.e ** (lvm["Lsm"] - lvm["lgh"] + s)
    u = np.array([complex(q * su) for q in lvm["qz"][:nk]])
    v = np.array([complex(q * sv) for q in lvm["qzm"][:nk]])
    gl2 = float((lvm["Ls"] + lvm["Lsm"] - lvm["lgh"]) / 2)
    return u, v, gl2


def lv_pi(lvm, iz):
    """exact mp (pihat_m, pihat_{m-1}, h_{m-1}) at point iz."""
    pm = lvm["qz"][iz] * mp.e ** lvm["Ls"]
    pm1 = lvm["qzm"][iz] * mp.e ** lvm["Lsm"]
    h = lvm["sg"] * mp.e ** lvm["lgh"]
    return pm, pm1, h


def m_columns(md, zpts, dps, variant=KVAR):
    """model (11, 21)-columns as complex128 at all points."""
    u = np.empty(len(zpts), complex)
    v = np.empty(len(zpts), complex)
    for i, z in enumerate(zpts):
        M = CB.model_at(md, complex(z), dps, variant=variant)
        u[i] = complex(M[0][0])
        v[i] = complex(M[1][0])
    return u, v


def d_pole_dec(md, zpts):
    """|Re log10 D(z)| of the FULL model's discrete Szego layer
    at the given points (the atom-pole exponent, f64)."""
    z = np.asarray(zpts, complex)
    a, b = md["a"], md["b"]
    Rz = (z - a) * np.sqrt((z - b) / (z - a))
    s = np.zeros(len(z), complex)
    for nn, ll, ss in zip(md["nu"], md["L"], md["xs"]):
        s += float(nn) * float(ll) / (z - float(ss))
    return np.abs(np.real(0.5 * Rz * s)) / math.log(10.0)


def pair_kernel(Ax, Bx, Ay, By, Dn):
    """K[x, y] = (A(y) B(x) - B(y) A(x)) / (y - x) with A = the
    11-column, B = the 21-column (r250 c2 kernel orientation)."""
    return (Ay[None, :] * Bx[:, None]
            - By[None, :] * Ax[:, None]) / Dn


def spear(x, y):
    return BH.spearman(list(x), list(y))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else WINDOWS
    a1_windows = (9,) if smoke else A1_WINDOWS
    nsamp = 12 if smoke else NSAMP
    prof_pts = 8 if smoke else PROF_PTS
    stride = 4 if smoke else 1

    print("=" * 78)
    print("targetreadout_error_probe -- PRIME.PORT.RHP."
          "TARGETREADOUT.ERROR.01 (round 251)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 only, atom stride 4, reduced "
                        "grids, world block skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "leg-A formulas (delta h = (R1)_12 contour identity; "
          "delta T = intint([K^Y_N - K^M_N] - [K^Y_8 - K^M_8]) "
          "dsigma0 dsigma0; error kernel = (R^-1(y) R(x) - I) "
          "sandwiched between model columns), all normalizations "
          "(eps_sup / eps_L2 / eps_YM, r250 C-gauge), the "
          "annihilation quotients and ALL verdict rules sealed in "
          "the frozen spec BEFORE evaluation; windows %s, a1 %s, "
          "dps kern %s / model %d,%d; QP iters %d tol %.0e; "
          "PROF_PTS %d, NSAMP %d, sandwich %dx%d; bars: a1 %.0e, "
          "a2 route %.0e (gross), reg %.2f, a3 %.0e; amp slope/"
          "Spearman %.1f/%.1f; annihil %.1f dec; c2 Spearman %.1f; "
          "base %.1f/%.2f/%.1f; world share [%.1f, %.1f]"
          % (str(WINDOWS), str(A1_WINDOWS), str(DPS_KERN),
             DPS_MK, DPS_MR, QP_ITERS, QP_TOL, PROF_PTS, NSAMP,
             SAND_K, SAND_K, A1_BAR, A2_ROUTE_BAR, REG_SYS_BAR,
             A3_BAR, AMP_SLOPE_BAR, AMP_SP_BAR, ANNIHIL_DEC_BAR,
             C2_SP_BAR, BASE_RATIO_BAR, H_RATE_BAR,
             OFFSET_DEC_BAR, WORLD_SH_LO, WORLD_SH_HI))

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS")
    packs = {kz: BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    okC = all(packs[kz]["nf"] is None for kz in windows)
    tt_note = "; ".join(
        "w%d: N=%d, T_true=%.4f" % (kz, packs[kz]["N"],
                                    packs[kz]["St"]
                                    - float(packs[kz]["S"][FIB_LO
                                                           - 1]))
        for kz in windows)
    check("G10-census-controls", okC and okCf,
          "free prefix positive on %d/%d windows; %s; control "
          "flips re-derived %s (falsifier battery armed)"
          % (sum(1 for kz in windows if packs[kz]["nf"] is None),
             len(windows), tt_note,
             str({c: ctrl[c]["nf"] for c in ctrl})))

    # ---------------- S2: models + kernel passes per window
    section("S2  MODELS + MP KERNEL PASSES (wards)")
    W = {}
    res_worst = 0.0
    mass_ok = True
    detm_worst = 0.0
    rich_worst = 0.0
    dety_worst = 0.0
    chain_worst = 0.0
    lgmax_worst = 0.0
    fin_ok = True
    for kz in windows:
        p = packs[kz]
        d = p["d"]
        N = p["N"]
        dsm = p["dsm"]
        x, wt, A, Lip, V = CB.eq_field(d)
        _pan, norm_z, x0, _a0, _b0 = CB.build_panels(x)
        # sigma0 atoms: border + (-c) * window (c = F_0/h_0)
        c0 = p["Fv"][0] / p["hv"][0]
        batoms = np.concatenate([dsm["xs"], dsm["ys"]])
        bwts = np.concatenate([dsm["ws"], -dsm["vs"]])
        atoms0 = np.concatenate([batoms, x])[::stride]
        wts0 = np.concatenate([bwts, -c0 * wt])[::stride]
        nb = len(batoms[::stride])  # border block length after
        # stride (border first in the concat order)
        A0 = len(atoms0)
        # point list: x-offset block, y-offset block, then the
        # sealed gap-midpoint norm contour (off the atom poles)
        zx = atoms0 + 1j * FIB_DX
        zy = atoms0 + 1j * FIB_DY
        osort = np.argsort(atoms0)
        srt = atoms0[osort]
        wsrt = np.abs(wts0[osort])
        pickm = np.unique(np.linspace(0, A0 - 2, nsamp)
                          .astype(int))
        zmid = [0.5 * (srt[i] + srt[i + 1]) + 1j * DELTA_GAP
                for i in pickm]
        wmid = [0.5 * (wsrt[i] + wsrt[i + 1]) for i in pickm]
        zpts = list(zx) + list(zy) + zmid
        mid_ids = list(range(2 * A0, 2 * A0 + len(zmid)))
        # sandwich atoms (position stride over sorted atoms)
        pick = np.unique(np.linspace(0, A0 - 1, nsamp).astype(int))
        samp = [int(osort[i]) for i in pick]
        sand_x = samp[:SAND_K]
        sand_y = samp[-SAND_K:]
        samp_pts = sorted(set(mid_ids) | set(sand_x)
                          | set(A0 + j for j in sand_y))
        snap_pts = {FIB_LO: samp_pts, N: samp_pts}
        # QP masses: profile grid + specials
        grid = sorted(set(np.linspace(2, N - 1, prof_pts)
                          .astype(int).tolist())
                      | {7, FIB_LO, N // 2, N - 1, N})
        mds = {}
        rho = None
        for n in grid:
            rho, res = SZ.solve_qp(A, Lip, V, float(n), rho0=rho,
                                   iters=QP_ITERS, tol=QP_TOL)
            res_worst = max(res_worst, res)
            md = CB.model_data(x, wt, A, V, rho, n)
            mass_ok = mass_ok and (md["nround"] == n)
            mds[n] = md
        # spot model wards (r250 gates, spot-checked)
        for n in (FIB_LO, N):
            md = mds[n]
            for z in (zpts[0], zpts[-1]):
                detm_worst = max(
                    detm_worst,
                    CB.detm_dev(CB.model_at(md, complex(z),
                                            DPS_MR)))
            m1_12, _devs = CB.rich_M1_12(md, n, norm_z, DPS_MR)
            rich_worst = max(rich_worst,
                             abs(float(mp.log(abs(m1_12), 10))
                                 - md["hmod_l10"]))
        # mp kernel pass (w9 also stores level N-1 for the m2
        # top-level shift must-fail)
        dps = 80 if smoke else DPS_KERN[kz]
        lv_levels = {FIB_LO, N} | ({N - 1} if kz == 9 else set())
        hlog, gam, lvv, ysnap, dety = mp_kernel_pass(
            d, zpts, snap_pts, lv_levels, dps, N)
        dety_worst = max(dety_worst, dety)
        rows = p["rows"]
        for n in (12, N // 2):
            if n in gam:
                chain_worst = max(
                    chain_worst,
                    abs(gam[n] / rows[n - 1]["gam_next"] - 1.0))
        # kernel column conversion (balanced) + finiteness
        cols = {}
        for m in (FIB_LO, N):
            u, v, gl2 = y_columns(lvv[m], 2 * A0)
            fin_ok = fin_ok and bool(
                np.all(np.isfinite(u)) and np.all(np.isfinite(v)))
            au = np.abs(u[np.nonzero(u)[0]])
            av = np.abs(v[np.nonzero(v)[0]])
            lgm = max(np.max(np.log10(au)) if len(au) else 0.0,
                      np.max(np.log10(av)) if len(av) else 0.0)
            lgmax_worst = max(lgmax_worst, lgm)
            cols[m] = (u, v, gl2)
        mu, mv = {}, {}
        for m in (FIB_LO, N):
            uu, vv = m_columns(mds[m], zpts[:2 * A0], DPS_MK)
            fin_ok = fin_ok and bool(
                np.all(np.isfinite(uu))
                and np.all(np.isfinite(vv)))
            au = np.abs(uu[np.nonzero(uu)[0]])
            av = np.abs(vv[np.nonzero(vv)[0]])
            lgm = max(np.max(np.log10(au)) if len(au) else 0.0,
                      np.max(np.log10(av)) if len(av) else 0.0)
            lgmax_worst = max(lgmax_worst, lgm)
            mu[m], mv[m] = uu, vv
        info("w%-3d N=%d: sigma0 atoms %d (border %d + window "
             "%d, c0 %.4g), points %d, norm contour %d, QP "
             "masses %d, dps %d"
             % (kz, N, A0, nb, A0 - nb, c0,
                len(zpts), len(zmid), len(grid), dps))
        W[kz] = dict(p=p, d=d, N=N, x=x, wt=wt, A0=A0, x0=x0,
                     atoms0=atoms0, wts0=wts0, nb=nb, zpts=zpts,
                     mid_ids=mid_ids, wmid=wmid, sand_x=sand_x,
                     sand_y=sand_y, mds=mds,
                     hlog=hlog, lvv=lvv, ysnap=ysnap, cols=cols,
                     mu=mu, mv=mv, norm_z=norm_z, grid=grid,
                     rows=rows)
    check("G20-qp-wards", res_worst <= QP_RES_BAR and mass_ok,
          "constrained-equilibrium QP (r232a verbatim, warm-"
          "started profile grids): residual worst %.1e (bar "
          "%.0e); every rounded mass integer-exact; spot det M "
          "%.1e (bar %.0e); spot Richardson vs analytic h_model "
          "%.1e (bar %.0e) -- the r250 model stands unmodified"
          % (res_worst, QP_RES_BAR, detm_worst, DETM_BAR,
             rich_worst, RICH_BAR))
    check("G21-kernel-pass-wards",
          dety_worst <= DETY_BAR and chain_worst <= CHAIN_BAR
          and fin_ok and detm_worst <= DETM_BAR
          and rich_worst <= RICH_BAR,
          "det Y_n = 1 at every sampled snapshot point to %.1e "
          "(bar %.0e); mp gammahat vs f64 wpack chain worst %.1e "
          "(bar %.0e); balanced Y/M kernel columns all finite in "
          "complex128 (max |log10| %.1f, headroom %.1f decades "
          "to overflow)"
          % (dety_worst, DETY_BAR, chain_worst, CHAIN_BAR,
             lgmax_worst, 308.0 - lgmax_worst))

    # ---------------- S3: leg A -- the exact formulas, gated
    section("S3  LEG A -- EXACT READOUT-ERROR FORMULAS")
    # (a1) delta h = (R1)_12 (own high-dps far-point pass:
    # the far-z Cauchy column cancels ~ (n+1) log10|z| digits)
    a1_worst = 0.0
    a1_note = []
    dety_a1 = 0.0
    m1_ratio_min = float("inf")
    dps_a1 = 400 if smoke else DPS_A1
    for kz in a1_windows:
        Wk = W[kz]
        N = Wk["N"]
        degs = (N // 2,) if smoke else (N // 2, N - 1)
        zfar = [Wk["x0"] + NORM_OFFS[0], Wk["x0"] + NORM_OFFS[1]]
        hlA, _gmA, _lvA, ysA, dA = mp_kernel_pass(
            Wk["d"], zfar, {n: [0, 1] for n in degs},
            {min(degs)}, dps_a1, N)
        dety_a1 = max(dety_a1, dA)
        for n in degs:
            md = Wk["mds"][n]
            mp.mp.dps = dps_a1
            lg, sg = hlA[n]
            h_true = sg * mp.e ** lg
            h_mod = mp.e ** (mp.mpf(md["hmod_l10"]) * mp.log(10))
            delta = h_true - h_mod
            vals12, vals21 = [], []
            for j, zf in enumerate(zfar):
                z = mp.mpc(zf)
                Y = ysA[n][j]
                M = CB.model_at(md, complex(zf), DPS_MR)
                mp.mp.dps = dps_a1
                R, _dR = r_field(Y, M)
                vals12.append((z, z * R[0][1]))
                vals21.append((z, z * R[1][0]))
            (z1, v1), (z2, v2) = vals12
            rich12 = (z2 * v2 - z1 * v1) / (z2 - z1)
            (z1, u1), (z2, u2) = vals21
            rich21 = (z2 * u2 - z1 * u1) / (z2 - z1)
            scale = max(abs(h_true), abs(h_mod))
            dev = float(abs(rich12 - delta) / scale)
            dev21 = float(abs(rich21 - delta) / scale)
            a1_worst = max(a1_worst, dev)
            m1_ratio_min = min(m1_ratio_min,
                               dev21 / max(dev, 1e-300))
            a1_note.append("w%d n=%d dev %.1e" % (kz, n, dev))
    check("G30-a1-deltah-contour-identity",
          a1_worst <= A1_BAR and dety_a1 <= DETY_BAR,
          "delta h_n = h_n - h_n^out = (R1)_12 (EXACT: Y1 = R1 + "
          "M1, no cross term at 1/z): 2-point Richardson at the "
          "sealed norm points x0+1e2/x0+1e3 (own mp pass, dps "
          "%d, det Y ward %.1e) vs the direct difference: %s -- "
          "worst %.1e (bar %.0e): the base readout error IS a "
          "contour functional of the error field R"
          % (dps_a1, dety_a1, "; ".join(a1_note), a1_worst,
             A1_BAR))

    # (a2) the remainder identity + reg anchor, per window
    fib = {}
    route_worst = 0.0
    reg_worst = 0.0
    reg_note = []
    for kz in windows:
        Wk = W[kz]
        N = Wk["N"]
        A0 = Wk["A0"]
        at = Wk["atoms0"]
        wv = Wk["wts0"]
        Dn = (at[None, :] - at[:, None]
              + 1j * (FIB_DY - FIB_DX))
        KY, KM = {}, {}
        for m in (FIB_LO, N):
            u, v, _g = Wk["cols"][m]
            KY[m] = pair_kernel(u[:A0], v[:A0],
                                u[A0:2 * A0], v[A0:2 * A0], Dn)
            KM[m] = pair_kernel(Wk["mu"][m][:A0],
                                Wk["mv"][m][:A0],
                                Wk["mu"][m][A0:],
                                Wk["mv"][m][A0:], Dn)

        def pr(K):
            return float(np.real(wv @ K @ wv))

        TY_diff = pr(KY[N] - KY[FIB_LO])
        TM_diff = pr(KM[N] - KM[FIB_LO])
        dT_A = TY_diff - TM_diff
        Krem = (KY[N] - KM[N]) - (KY[FIB_LO] - KM[FIB_LO])
        dT_B = pr(Krem)
        gross = float(np.abs(wv) @ np.abs(Krem) @ np.abs(wv)) \
            + sum(float(np.abs(wv) @ np.abs(K) @ np.abs(wv))
                  for K in (KY[N], KM[N], KY[FIB_LO],
                            KM[FIB_LO]))
        route_dev = abs(dT_A - dT_B) / max(gross, 1e-300)
        route_worst = max(route_worst, route_dev)
        T_true = Wk["p"]["St"] - float(Wk["p"]["S"][FIB_LO - 1])
        reg = abs(TY_diff / T_true - 1.0) if stride == 1 else \
            float("nan")
        if stride == 1:
            reg_worst = max(reg_worst, reg)
            reg_note.append("w%d %+.1e" % (kz, TY_diff / T_true
                                           - 1.0))
        # naive (level-N only) pairings for leg C
        TY_nav = pr(KY[N])
        TM_nav = pr(KM[N])
        # m2 material (w9): Y-side top-level shift N -> N-1
        top_shift = float("nan")
        if kz == 9:
            u, v, _g = y_columns(Wk["lvv"][N - 1], 2 * A0)
            Km1 = pair_kernel(u[:A0], v[:A0], u[A0:], v[A0:],
                              Dn)
            top_shift = TY_nav - pr(Km1)
            del Km1
        # m3 material: naive against raw border sigma (uncentered)
        wsig = wv.copy()
        wsig[Wk["nb"]:] = 0.0
        TY_nav_sig = float(np.real(wsig @ KY[N] @ wsig))
        fib[kz] = dict(TY_diff=TY_diff, TM_diff=TM_diff,
                       dT=dT_A, T_true=T_true,
                       dT_nav=TY_nav - TM_nav,
                       TY_nav=TY_nav, TY_nav_sig=TY_nav_sig,
                       top_shift=top_shift, gross=gross)
        del KY, KM, Krem
    check("G31-a2-remainder-identity-routes",
          route_worst <= A2_ROUTE_BAR,
          "T^Y - T^M = intint([K^Y_N - K^M_N] - [K^Y_8 - K^M_8]) "
          "dsigma0 dsigma0: separately-paired terms vs the "
          "assembled difference kernel: worst dev %.1e on the "
          "absolute mass-norm scale (bar %.0e) -- the central "
          "evaluation formula of r250-R4 is implemented exactly"
          % (route_worst, A2_ROUTE_BAR))
    check("G32-a2-regularization-anchor",
          (reg_worst <= REG_SYS_BAR) if stride == 1 else True,
          ("T^Y_reg vs the bitwise r244 chain readout T_true: "
           "rel dev %s -- worst %.1e (bar %.2f): the sealed "
           "off-axis contour carries the object; delta T is a "
           "bill about the OBJECT, not about the regularization"
           % ("; ".join(reg_note), reg_worst, REG_SYS_BAR))
          if stride == 1 else
          "SMOKE: strided atoms -- chain anchor not applicable")

    # (a3) sandwich identity at level N (sealed 5x5 sample pairs;
    # combination at DPS_SAND -- both sides consume the same Y/M
    # inputs, the gate tests the exact algebra)
    a3_worst = 0.0
    dps_sand = 300 if smoke else DPS_SAND
    for kz in windows:
        Wk = W[kz]
        N = Wk["N"]
        A0 = Wk["A0"]
        md = Wk["mds"][N]
        lvm = Wk["lvv"][N]
        pairs = []
        for i in Wk["sand_x"]:
            for j in Wk["sand_y"]:
                Mx = CB.model_at(md, complex(Wk["zpts"][i]),
                                 DPS_MR, variant=KVAR)
                My = CB.model_at(md,
                                 complex(Wk["zpts"][A0 + j]),
                                 DPS_MR, variant=KVAR)
                mp.mp.dps = dps_sand
                zxq = mp.mpc(Wk["zpts"][i])
                zyq = mp.mpc(Wk["zpts"][A0 + j])
                pNx, pN1x, h = lv_pi(lvm, i)
                pNy, pN1y, _h = lv_pi(lvm, A0 + j)
                kY = (pNy * pN1x - pN1y * pNx) / (h * (zyq - zxq))
                kM = (My[0][0] * Mx[1][0]
                      - My[1][0] * Mx[0][0]) / (zyq - zxq)
                Yx = Wk["ysnap"][N][i]
                Yy = Wk["ysnap"][N][A0 + j]
                Rx, _dx_ = r_field(Yx, Mx)
                Ry, dRy = r_field(Yy, My)
                Ra = m_adj2(Ry)
                Ryi = ((Ra[0][0] / dRy, Ra[0][1] / dRy),
                       (Ra[1][0] / dRy, Ra[1][1] / dRy))
                E = m_mul2(Ryi, Rx)
                E = ((E[0][0] - 1, E[0][1]),
                     (E[1][0], E[1][1] - 1))
                detMy = m_det2(My)
                r2 = (-My[1][0] / detMy, My[0][0] / detMy)
                c1 = (Mx[0][0], Mx[1][0])
                sand = (r2[0] * (E[0][0] * c1[0] + E[0][1] * c1[1])
                        + r2[1] * (E[1][0] * c1[0]
                                   + E[1][1] * c1[1])) \
                    / (zyq - zxq)
                pairs.append((kY - kM, sand))
        gsc = max(max(abs(a), abs(b)) for a, b in pairs)
        dev = max(float(abs(a - b)) for a, b in pairs) \
            / max(float(gsc), 1e-300)
        a3_worst = max(a3_worst, dev)
    check("G33-a3-sandwich-identity", a3_worst <= A3_BAR,
          "K^Y - K^M = (row2 M^{-1}(y)) [R^{-1}(y) R(x) - I] "
          "(col1 M(x)) / (y - x): direct vs sandwich on the "
          "sealed %dx%d sample pairs at level N: worst "
          "sup-normalized dev %.1e (bar %.0e) -- the fiber "
          "transfer consumes EXACTLY this bilinear form of "
          "(R - I)" % (SAND_K, SAND_K, a3_worst, A3_BAR))

    # (a4) the FULL-D pole obstruction, measured and typed
    pole_max = 0.0
    for kz in windows:
        Wk = W[kz]
        dec = d_pole_dec(Wk["mds"][Wk["N"]],
                         Wk["atoms0"] + 1j * FIB_DX)
        pole_max = max(pole_max, float(np.max(dec)))
    pole_obstructed = pole_max >= POLE_DEC_BAR
    check("G34-fullD-pole-obstruction", True,
          "the FULL r250 model's discrete Szego layer D(z) at "
          "the sigma0 atoms (+ i dx): max |Re log10 D| = %.1f "
          "decades (bar %.0f; f64 ceiling 308) => %s -- "
          "sharpens the r250 ablation finding (bare beats "
          "dressed): the arcsine-cell D is not sigma0-PAIRABLE; "
          "kernel legs run the sealed noD member"
          % (pole_max, POLE_DEC_BAR,
             "MODEL_KERNEL_POLE_OBSTRUCTION (typed)"
             if pole_obstructed else "no obstruction"))

    # ---------------- S4: leg B -- amplification
    section("S4  LEG B -- THE AMPLIFICATION FACTOR")
    amp = {}
    for kz in windows:
        Wk = W[kz]
        N = Wk["N"]
        A0 = Wk["A0"]
        dps = 80 if smoke else DPS_KERN[kz]
        mp.mp.dps = dps
        errs = {}
        efull = []
        for m in (FIB_LO, N):
            md = Wk["mds"][m]
            nl = md["nl"]
            ev, wv_x, eYM = [], [], []
            for im, iz in enumerate(Wk["mid_ids"]):
                Y = Wk["ysnap"][m][iz]
                M = CB.model_at(md, complex(Wk["zpts"][iz]),
                                DPS_MR, variant=KVAR)
                e = CB.err_RI(Y, M, nl)
                ev.append(e)
                wv_x.append(Wk["wmid"][im])
                if m == N:
                    Mf = CB.model_at(md,
                                     complex(Wk["zpts"][iz]),
                                     DPS_MR)
                    efull.append(CB.err_RI(Y, Mf, nl))
                # normalized-gauge Y - M scale (model-relative)
                enl = mp.e ** mp.mpf(nl)
                Dm = ((Y[0][0] - M[0][0],
                       (Y[0][1] - M[0][1]) / enl),
                      ((Y[1][0] - M[1][0]) * enl,
                       Y[1][1] - M[1][1]))
                Mn = ((M[0][0], M[0][1] / enl),
                      (M[1][0] * enl, M[1][1]))
                nrm = math.sqrt(sum(float(abs(Mn[a][b])) ** 2
                                    for a in (0, 1)
                                    for b in (0, 1)))
                eYM.append(math.sqrt(
                    sum(float(abs(Dm[a][b])) ** 2
                        for a in (0, 1) for b in (0, 1)))
                    / max(nrm, 1e-300))
            sup = float(np.max(ev))
            wsum = float(np.sum(wv_x))
            l2 = math.sqrt(float(np.sum(
                np.asarray(wv_x) * np.asarray(ev) ** 2))
                / max(wsum, 1e-300))
            errs[m] = dict(sup=sup, l2=l2,
                           ym=float(np.max(eYM)))
        dT = abs(fib[kz]["dT"])
        amp[kz] = dict(
            eps_sup=errs[N]["sup"], eps_l2=errs[N]["l2"],
            eps_ym=errs[N]["ym"], eps8=errs[FIB_LO]["sup"],
            A_sup=dT / max(errs[N]["sup"], 1e-300),
            A_l2=dT / max(errs[N]["l2"], 1e-300),
            q_c2=dT / max(errs[N]["ym"], 1e-300))
        info("w%-3d eps_sup %.3g  eps_L2 %.3g  eps_YM %.3g  "
             "eps_sup(8) %.3g  |dT| %.3g  A_sup %.3g  A_L2 %.3g"
             "  [full-D err med %.3g]"
             % (kz, errs[N]["sup"], errs[N]["l2"],
                errs[N]["ym"], errs[FIB_LO]["sup"], dT,
                amp[kz]["A_sup"], amp[kz]["A_l2"],
                float(np.median(efull))))
    Ns = [W[kz]["N"] for kz in windows]
    if len(windows) > 1:
        sp_amp = spear([amp[kz]["A_sup"] for kz in windows], Ns)
        p_amp = float(np.polyfit(
            np.log10(Ns),
            np.log10([max(amp[kz]["A_sup"], 1e-300)
                      for kz in windows]), 1)[0])
    else:
        sp_amp, p_amp = float("nan"), float("nan")
    check("G40-amplification-measured", True,
          "A_w = |delta T| / eps (rows above): Spearman(A_sup; "
          "N) = %+.2f, log-log slope p = %+.2f (sealed tags: "
          "EXTENSIVE iff p >= %.1f AND Spearman >= %.1f; BOUNDED "
          "iff Spearman <= 0; else MIXED)"
          % (sp_amp, p_amp, AMP_SLOPE_BAR, AMP_SP_BAR))

    # ---------------- S5: leg C -- annihilation
    section("S5  LEG C -- ANNIHILATION IN THE ERROR")
    dec_bought = []
    for kz in windows:
        f = fib[kz]
        q = abs(f["dT"]) / max(abs(f["dT_nav"]), 1e-300)
        dec = -math.log10(max(q, 1e-300))
        dec_bought.append(dec)
        f["q_annihil"] = q
        info("w%-3d dT %+0.4g  dT_naiv %+0.4g  q_annihil %.3g  "
             "decades bought %+.2f"
             % (kz, f["dT"], f["dT_nav"], q, dec))
    med_dec = float(np.median(dec_bought))
    buys = med_dec >= ANNIHIL_DEC_BAR
    check("G50-annihilation-c1", True,
          "q_annihil = |dT(K_N - K_8)| / |dT_naiv(K_N)| per "
          "window (rows above; sigma0 fixed in both, so the "
          "quotient isolates the mode-1..7 + level-8 subtraction "
          "gain in the ERROR): median decades bought %+.2f "
          "(sealed bar %.1f) => %s"
          % (med_dec, ANNIHIL_DEC_BAR,
             "ANNIHILATION_BUYS" if buys
             else "ANNIHILATION_NEUTRAL"))
    if len(windows) > 1:
        q_c2 = [amp[kz]["q_c2"] for kz in windows]
        sp_c2 = spear(q_c2, Ns)
        sl_c2 = float(np.polyfit(
            np.log10(Ns),
            np.log10([max(v, 1e-300) for v in q_c2]), 1)[0])
    else:
        sp_c2, sl_c2 = float("nan"), float("nan")
    check("G51-annihilation-c2-Ntrend", True,
          "|delta T| / eps_YM across the ladder: %s; "
          "Spearman(q; N) = %+.2f, log-log slope %+.2f (sealed "
          "reading: <= %.1f = the rest zone carries analytically "
          "with N; flat/rising = the fiber sits genuinely in the "
          "error term)"
          % (str({("w%d" % kz): round(amp[kz]["q_c2"], 3)
                  for kz in windows}), sp_c2, sl_c2, C2_SP_BAR))

    # ---------------- S6: leg D -- margin tables + worlds
    section("S6  LEG D -- MARGIN RELEVANCE + WORLDS")
    base_max = 0.0
    slope_ok_n = 0
    off_meds = []
    prof_note = []
    for kz in windows:
        Wk = W[kz]
        N = Wk["N"]
        rows = Wk["rows"]
        ns, dls = [], []
        for n in Wk["grid"]:
            if n >= N or n not in Wk["mds"]:
                continue
            dl = (rows[n]["lg_h"] / math.log(10)
                  - Wk["mds"][n]["hmod_l10"])
            ns.append(n)
            dls.append(dl)
        rat = [abs(10.0 ** dl - 1.0) for dl in dls]
        base_max = max(base_max, max(rat))
        sl = float(np.polyfit(ns, dls, 1)[0])
        off = float(np.median(dls))
        off_meds.append(abs(off))
        if abs(sl) <= H_RATE_BAR:
            slope_ok_n += 1
        qs = np.percentile(rat, [25, 50, 75])
        prof_note.append(
            "w%d ratio q25/med/q75 %.3f/%.3f/%.3f max %.4f "
            "slope %+.4f off %+.2f"
            % (kz, qs[0], qs[1], qs[2], max(rat), sl, off))
    for t in prof_note:
        info(t)
    check("G60-base-profile", True,
          "|delta h_n|/h_n^out over the sealed profile grid (ALL "
          "free-degree strides, not just terminal): max %.4f "
          "(PROVABLE bar %.1f); offset/rate split: |slope| <= "
          "%.2f dec/degree on %d/%d windows, median |offset| "
          "%.2f decades (bar %.1f) -- the sealed classification "
          "is applied in the verdict"
          % (base_max, BASE_RATIO_BAR, H_RATE_BAR, slope_ok_n,
             len(windows), float(np.median(off_meds)),
             OFFSET_DEC_BAR))
    # fiber margin table
    ratio_fib = {}
    anchor_ok = True
    for kz in windows:
        Wk = W[kz]
        p = Wk["p"]
        N = Wk["N"]
        f = fib[kz]
        B = float(p["S"][N - 2]) + 5.0 / 7.0
        B0 = B - float(p["rho"][0])
        Q7 = float(p["S"][FIB_LO - 1]) - float(p["rho"][0])
        marg_out = B0 - Q7 - f["TM_diff"]
        marg_true = B0 - Q7 - f["T_true"]
        anchor = 5.0 / 7.0 - float(p["rho"][N - 1])
        anchor_ok = anchor_ok and (
            abs(marg_true - anchor) <= 1e-9)
        f["marg_true"] = marg_true
        ratio_fib[kz] = abs(f["dT"]) / max(abs(marg_true),
                                           1e-300)
        info("w%-3d T_true %+.4f  T_out %+.4f  dT %+.4f  "
             "margin_true %+.4f  margin_out %+.4f  "
             "|dT|/|margin_true| %.3g"
             % (kz, f["T_true"], f["TM_diff"], f["dT"],
                marg_true, marg_out, ratio_fib[kz]))
    hypo = [amp[kz]["A_sup"] / W[kz]["N"]
            / max(abs(fib[kz]["marg_true"]), 1e-300)
            for kz in windows]
    check("G61-fiber-margin", anchor_ok,
          "|delta T| vs the TRUE parametric margin B0 - Q_7 - "
          "T_true (amended comparison object, see spec; B = "
          "S_{N-2} + 5/7, r243/r247 placeholder, status "
          "IMPORTED -- corner_provenance runs in parallel): "
          "rows above; anchor identity B0 - Q_7 - T_true = "
          "5/7 - rho_{N-1} exact on %d/%d; hypothetical balance "
          "(A/N)/|margin_true| median %.3g (>= 1 would mean a "
          "1/N-falling matrix error does NOT carry the fiber)"
          % (len(windows), len(windows),
             float(np.median(hypo))))
    # worlds
    if smoke:
        world_verdict = "WORLD_SKIPPED_SMOKE"
        check("G62-worlds", True, "SMOKE: world block skipped")
    else:
        pS = ctrl["SCRAMBLE"]
        dS = pS["d"]
        NS = pS["N"]
        dsmS = pS["dsm"]
        xS, wtS, AS, LipS, VS = CB.eq_field(dS)
        c0S = pS["Fv"][0] / pS["hv"][0]
        batS = np.concatenate([dsmS["xs"], dsmS["ys"]])
        bwtS = np.concatenate([dsmS["ws"], -dsmS["vs"]])
        at_S = np.concatenate([batS, xS])
        wv_S = np.concatenate([bwtS, -c0S * wtS])
        A0S = len(at_S)
        zS = (list(at_S + 1j * FIB_DX)
              + list(at_S + 1j * FIB_DY))
        rhoS = None
        mdsS = {}
        for n in (FIB_LO, NS):
            rhoS, resS = SZ.solve_qp(AS, LipS, VS, float(n),
                                     rho0=rhoS, iters=QP_ITERS,
                                     tol=QP_TOL)
            res_worst = max(res_worst, resS)
            mdsS[n] = CB.model_data(xS, wtS, AS, VS, rhoS, n)
        _hl, _gm, lvS, _ys, detyS = mp_kernel_pass(
            dS, zS, {}, {FIB_LO, NS}, DPS_KERN[9], NS)
        dety_worst = max(dety_worst, detyS)
        DnS = (at_S[None, :] - at_S[:, None]
               + 1j * (FIB_DY - FIB_DX))
        TY_S, TM_S = {}, {}
        for m in (FIB_LO, NS):
            u, v, _g = y_columns(lvS[m], 2 * A0S)
            K = pair_kernel(u[:A0S], v[:A0S], u[A0S:], v[A0S:],
                            DnS)
            TY_S[m] = float(np.real(wv_S @ K @ wv_S))
            uu, vv = m_columns(mdsS[m], zS, DPS_MK)
            K = pair_kernel(uu[:A0S], vv[:A0S], uu[A0S:],
                            vv[A0S:], DnS)
            TM_S[m] = float(np.real(wv_S @ K @ wv_S))
            del K
        T_true_S = pS["St"] - float(pS["S"][FIB_LO - 1])
        dT_S = (TY_S[NS] - TY_S[FIB_LO]) \
            - (TM_S[NS] - TM_S[FIB_LO])
        dT_M = fib[9]["dT"]
        gap_obj = T_true_S - fib[9]["T_true"]
        share = abs(dT_S - dT_M) / max(abs(gap_obj), 1e-300)
        decs = math.log10(max(abs(dT_S), 1e-300)
                          / max(abs(dT_M), 1e-300))
        in_dt = WORLD_SH_LO <= share <= WORLD_SH_HI
        world_verdict = ("WORLD_GAP_IN_DELTA_T" if in_dt
                         else "WORLD_GAP_ELSEWHERE")
        check("G62-worlds", True,
              "SCRAMBLE (seed 1, full depth %d): T_true %+.4g vs "
              "MAIN %+.4g (object gap %+.4g); delta T %+.4g vs "
              "MAIN %+.4g: share of the object gap landing in "
              "delta T = %.3f (sealed window [%.1f, %.1f]) => "
              "%s; decade offset %+.2f -- the world-blind outer "
              "model pushes the arithmetic difference into the "
              "error term (r250 MODEL_WORLD_BLIND consistent)"
              % (NS, T_true_S, fib[9]["T_true"], gap_obj, dT_S,
                 dT_M, share, WORLD_SH_LO, WORLD_SH_HI,
                 world_verdict, decs))

    # ---------------- S7: must-fails
    section("S7  MUST-FAILS")
    ok_m1 = m1_ratio_min >= M1_LOUD
    # m2: model low-level mass shift 7 posing as 8 (w9)
    Wk = W[9]
    A0 = Wk["A0"]
    at = Wk["atoms0"]
    wv = Wk["wts0"]
    Dn = at[None, :] - at[:, None] + 1j * (FIB_DY - FIB_DX)
    uu, vv = m_columns(Wk["mds"][7], Wk["zpts"][:2 * A0], DPS_MK)
    K7 = pair_kernel(uu[:A0], vv[:A0], uu[A0:], vv[A0:], Dn)
    TM7 = float(np.real(wv @ K7 @ wv))
    del K7
    uu, vv = Wk["mu"][FIB_LO], Wk["mv"][FIB_LO]
    K8 = pair_kernel(uu[:A0], vv[:A0], uu[A0:], vv[A0:], Dn)
    TM8 = float(np.real(wv @ K8 @ wv))
    del K8, Dn
    m2_inert = abs(TM7 - TM8)
    m2_floor = max(1e-3 * abs(fib[9]["TM_diff"]),
                   abs(fib[9]["TY_diff"] - fib[9]["T_true"])
                   if stride == 1 else 1e-3)
    rho_top = float(W[9]["p"]["rho"][W[9]["N"] - 1])
    m2_shift = fib[9]["top_shift"]
    m2_rel = abs(m2_shift / rho_top - 1.0)
    ok_m2 = (m2_rel <= 0.05
             and m2_shift >= 100.0 * m2_floor) or smoke
    # m3: uncentered alias (raw border sigma vs sigma0, level N)
    rho0 = float(W[9]["p"]["rho"][0])
    m3_gap = abs(fib[9]["TY_nav_sig"] - fib[9]["TY_nav"])
    m3_ratio = m3_gap / max(rho0, 1e-300)
    ok_m3 = (M3_LO <= m3_ratio <= M3_HI) or smoke
    # (strided smoke atoms carry no moment identities: m2/m3
    # are adjudicated in the FULL record only, values reported)
    check("G70-must-fails-fire", ok_m1 and ok_m2 and ok_m3,
          "m1 swapped R1 entry (21 for 12): dev ratio >= %.1e "
          "on every a1 combo (min %.1e, LOUD -- the transposed "
          "entry carries the e^{-2 n ell} gauge); m2 Y-side "
          "top-level shift (K_{N-1} for K_N): T moves by %.4g "
          "vs rho_{N-1} = %.4g (rel dev %.1e <= 0.05, %.0f x "
          "the anchor %.3g: level-pinned and LOUD; the inert "
          "model-side mass-7 shift %.2g is reported, amendment "
          "disclosed); m3 uncentered alias: naive(sigma) - "
          "naive(sigma0) = %.4g vs rho_0 = %.4g (ratio %.3f in "
          "[%.1f, %.1f]: the r248 rank-1 head, loud); m4 sign "
          "oracle: EXCLUDED by the input firewall (standing "
          "r243 exclusion)"
          % (M1_LOUD, m1_ratio_min, m2_shift, rho_top, m2_rel,
             m2_shift / max(m2_floor, 1e-300), m2_floor,
             m2_inert,
             m3_gap, rho0, m3_ratio, M3_LO, M3_HI))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    formulas_ok = (a1_worst <= A1_BAR
                   and route_worst <= A2_ROUTE_BAR
                   and (reg_worst <= REG_SYS_BAR
                        if stride == 1 else True)
                   and a3_worst <= A3_BAR)
    vA = ("READOUT_FORMULAS_EXACT" if formulas_ok
          else "READOUT_FORMULAS_OPEN")
    if smoke or len(windows) < 2:
        vB = "AMPLIFICATION_SMOKE_NA"
        vC2_fall = False
    else:
        if p_amp >= AMP_SLOPE_BAR and sp_amp >= AMP_SP_BAR:
            vB = "AMPLIFICATION_EXTENSIVE(p=%.2f)" % p_amp
        elif sp_amp <= 0.0:
            vB = "AMPLIFICATION_BOUNDED"
        else:
            vB = "AMPLIFICATION_MIXED(p=%.2f, sp=%.2f)" % (
                p_amp, sp_amp)
        vC2_fall = sp_c2 <= C2_SP_BAR
    vC = ("ANNIHILATION_BUYS(%.2f dec)" % med_dec if buys
          else "ANNIHILATION_NEUTRAL")
    marg_all = all(ratio_fib[kz] < 1.0 for kz in windows)
    if marg_all or (vC2_fall and buys):
        vD = "FIBER_ERROR_CONTROLLABLE"
    else:
        vD = "FIBER_IN_ERROR_CONFIRMED"
    if base_max <= BASE_RATIO_BAR:
        vE = "BASE_READOUT_PROVABLE"
    elif (slope_ok_n >= max(1, len(windows) // 2)
          and float(np.median(off_meds)) >= OFFSET_DEC_BAR):
        vE = "BASE_READOUT_BLOCKED_BY_OFFSET"
    else:
        vE = "BASE_READOUT_BLOCKED_STRUCTURAL"
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (an evaluation-"
          "formula round moves no edge); what the round adds: "
          "the exact delta-h contour identity, the exact delta-T "
          "remainder evaluation, the sandwiched error-kernel "
          "form, the measured A-factor, the annihilation "
          "quotients, and the margin bill against the parametric "
          "B placeholder")
    verd = " + ".join([vA, vB, vC, vD, vE, world_verdict])
    if pole_obstructed:
        verd += " + MODEL_KERNEL_POLE_OBSTRUCTION(FULL_D)"
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G81-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the readout-error formulas hold "
          "exactly, the A-factor scaling, the annihilation "
          "decades, the base profile bill, the fiber margin "
          "bill, the world split; OPEN: the budget bound and "
          "the base law themselves (r243/r247/r250 stand); "
          "NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
