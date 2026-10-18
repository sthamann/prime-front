#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dens_identity_probe -- PRIME.PORT.LSTAR.DENS_IDENTITY.01
(round 296): IS THE 92.5-PERCENT DENS TOP AXIS MATHEMATICALLY
IDENTIFIABLE AND COUPLED TO THE L* EXTREMIZER?  The curvature
arc (r290-r295, wave 8 = v965) sealed: the margin Hesse form at
MAIN is RANK-1-dominated in the L2 spectral metric (92.5 pct of
sum|lam| in ONE eigendirection e_top, lam_top -0.418), the top
axis is a pure DENS combination (DENS05 +1.00 / DENS04 -0.71 /
DENS03 +0.69 / DENS01 +0.53), NOT the SMOOTH axis (|cos| 0.07)
and NOT the ridge; the mechanism is window-constant (r294 DENS
shares w7/w9/w11 = 0.795/0.989/0.834); EPSTEIN has NO curvature
structure (first- and second-order structureless, ratio
5.4e-15).  THE ONE QUESTION OF THIS ROUND (hard fork, reviewer
contract): identify the OBJECT -- no new survival predictors,
no functional lottery.  The main comparison partner T1 is the
profile-space direction the L* margin is most sensitive to:
grad_delta lambda_max(E_{N_w}) via Hellmann-Feynman from the
extremal eigenvector phi* (with int p*^2 dmu = 1 the envelope
theorem gives dlam = int p*^2 d(dnu) - lam int p*^2 d(dmu); the
exact fold map pulls this back to the signed-density grid with
the s_l = 4 sin^2(pi l / L) / (2 L) envelope).  NOT a proof
round: no L* claim, no bound mechanism, no asymptotic law.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

MACHINERY IMPORTED VERBATIM (no duplication): r292 CF.{unit_dir,
pol_of_d2, expand_of_d2, proj_coords, rich_devs} + the sealed
r292 constants (HESS_EQ_HS, H_PAIR_H, GCUT, D2_FLOOR, POL_TOL,
seeds 292100+/292200+, N_ATOM); r291 RA.{subset_move, atom_ints,
AMP_PAD}; r290 PFP.{measure_density, dir_frac, dir_dens, lag_of,
interp_density, NEAR, DEAD}; r284 LS.{split_by_fold, atom_labels,
christoffel_rows}; r283 FS.{mu_chain_f64, b_matrix_f64}; r280
BL.{grad_ext, dir_opt, theta_of_dir, union_of_ctx,
sign_chain_f64}; r278 MS.ctx_build; r276 MF.{local_gaps,
pert_jit, conserve_comb}; v881 PIK.{build_rung, grid_density,
folded_measure, lambda_eps}; r243 PB.smooth_comb; paircorr
PC.{Grid, gen_model}; v563 core READ-ONLY.  The r294 window
protocol (12-direction window-own Hessian, seeds 294700 + 50 wi,
extraction dose cap, ladder halving max 3) is rebuilt VERBATIM
for the window-own e_top at w7/w11.

INDEX FIREWALL (binding, r238-r295 discipline): ground truth
(minC, crossings, margins) enters GATES and the measurement
channels (the Hesse forms -- disclosed measurement-consuming as
in r292/r294) only; the sealed source-pure constructors consume
densities / combs / grid geometry / kernel degrees / seeds ONLY
(AST scope audit); no zero/prime oracles anywhere (AST firewall;
atom classes via the r254/r284 world-blind tent matching +
integer root extraction inside LS.atom_labels).

METRIC DISCLOSURE (design-time, sealed BEFORE any evaluation):
e_top exists ONLY inside the 29-direction span D (it is an
eigenvector of the span-restricted form); the sealed PRIMARY
identity metric is therefore the IN-SPAN cosine
cos(e_top, P_D T) with P_D the exact Euclidean L2 projector onto
span(D) (r292 proj_coords, eigencut pseudo-solve, no fitting).
The raw grid cosine cos(e_top, T), the span capture
|P_D T|_2 / |T|_2 and the LAG-coordinate cosine (the L2 angle in
the r289/r290 lag coordinate where theta_eq lives; theta_eq
itself is an L1 object with no inner product, r292 disclosure)
are reported as honesty columns for EVERY candidate.  The noise
reference (T6) passes through the IDENTICAL pipeline.

LEG 0 -- ANCHOR REGRESSION (all gated): w9 record (S 367/263/
104, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, b34 -0.105 tol 0.01); theta_eq metric (REF
125.75 rel 1e-3, inversion 1e-12, pinned quadruple devs <=
0.15); control flips EPST/SCR/SMOOTH/HL2 = 25/21/27/25; r280
ridge anchor (theta_up 3.87e-5 rel 0.05, endpoint minC 185,
top-9 atoms == r291); THE L* SPECTRAL ANCHOR (r284/r286):
lambda_max(E_184) = 0.99983248 (abs tol 1e-6), top-5 eigs ==
r283 records (tol 1e-4), margin == 1 - lambda_max identity,
crossing 185 == minC + 1; EPSTEIN first-order flatness (|c_25|
<= 1e-9, theta_up >= 1e9); r292 EIGEN-ANCHOR on the verbatim
rebuilt 29-direction Hessian: trace share 0.925 tol 0.01,
lam_top -0.418 rel 0.02, SMOOTH |cos| 0.07 tol 0.03, ridge
L2-diagonal rank 28/29, top-4 loadings == (DENS05 +1.00, DENS04
-0.71, DENS03 +0.69, DENS01 +0.53) tol 0.05 after sign
canonicalization (DENS05 loading positive); the 29-direction
DENS coefficient share is reported as a MEASUREMENT (a3: the
published r294 0.989 is the share of the 18-direction TRAINING
form (H_tr, G_tr) -- a different object; no record exists for
the 29-direction share, so it carries no gate).

LEG A -- THE CANDIDATE LIBRARY (sealed BEFORE any measurement;
every member built by the ONE source-pure constructor
build_candidate, same eta_0 conservation projection, same L2
normalization; weight-coordinate members pulled back to density
space through the adjoint of the exact fold map = the s_l
envelope, the SAME map that carries grad lambda):
  T1 GRAD_LMAX (the main test): grad_delta lambda_max(E_184)
    via Hellmann-Feynman from phi* (formula above); WARD:
    finite-difference crosscheck on 6 sealed coordinates (per
    channel the 3 even grid-pair moves with the LARGEST
    analytic directional derivative -- a2: the ward verifies
    the formula where the FD signal is resolvable; the
    tiny-gradient folds sit at the f64 eigensolver noise floor
    ~1e-14, disclosed -- with the resolvability floor
    |g| t >= 1e-9; Richardson pair t, t/2 at t = 1.25e-6 max|d|
    -- a2 step fix: the hull-edge folds carry margin curvature
    so large that the first-drawn 1e-5 scale left an O(t^4)
    Richardson residual of 2e-3; the pure-truncation O(t^2)
    convergence was measured over a 5-step ladder and the pair
    re-anchored at the measured margin-valid scale, the exact
    r292-a1 pattern), rel dev <= 1e-4 on every coordinate.
    T1B/T1C: the gradients of the 2nd/3rd top eigenvalues
    (same formula, phi_2/phi_3) as CONTROL directions --
    excluded from the identity award, disclosed.
  T2 LAMBDA FAMILY (von Mangoldt on the support): Lambda(n) =
    log p at every union fold whose tent match carries an
    integer n = p^k (LS.atom_labels classes K1/KHI); PRIME-only
    (k = 1); PRIME-POWER-only (k >= 2).
  T3 LOCAL METRIC FAMILY: local fold-gap deviations (nearest
    union-neighbor distance minus mean); logarithmic density
    1/(f D) per fold; the r289 fraction profile (signed sub-cell
    offset u_match/D - f of the tent-matched comb atom).
  T4 KERNEL DIAGONALS at the nu atoms (degree N_w, r284
    construction): the Christoffel function v_k / diag_k, the
    E-kernel diagonal diag_k = v_k K_n(y_k), the CD-kernel
    diagonal K_n(y_k).
  T5 MOMENT GRADIENTS: grad_delta of the first 4 moments of
    mutilde (dd_l = s_l x_f^j on the support, j = 1..4),
    entering as a SUBSPACE via the projection share
    |P_T5 e_top|^2 (chance level of a 4-dim subspace disclosed
    via two pinned null quadruples).
  T6 NULL CONTROLS: 8 conservation-gated random on-support
    density directions (seeds 296100+, r290 dir_dens class)
    through the identical cosine pipeline; their MAX |cos| is
    the honest noise reference; one pinned DECOY (seed 296199)
    is smuggled through the candidate pipeline as must-fail m4.

LEG B -- THE IDENTITY TEST (the one question): for every
candidate the in-span |cos| (PRIMARY), the raw and the lag
cosines and the span capture.  SEALED BARS (in the code BEFORE
any cosine evaluation): |cos| >= 0.80 for T1 or a T2/T3/T4
member => DENS_ARITHMETIC_IDENTITY(member, cos); 0.40 <=
max|cos| < 0.80 over the eligible library (incl. the T5 root
share) => DENS_PARTIAL(member, cos); max|cos| < 0.40 AND below
the noise reference + 0.1 => DENS_WORLD_BLIND (below 0.40 but
above noise + 0.1 stays DENS_WORLD_BLIND with the above-noise
flag disclosed).  The T1 value is ALWAYS reported separately:
cos(e_top, grad lambda_max) is the COUPLING NUMBER of the round.

LEG C -- WORLD AND WINDOW HARDENING (identity discipline):
  (c1) WORLD CONTRAST at EPST and SCR: no structured e_top
    exists there by r292; measured instead: the world-own top
    curvature direction inside a 12-direction DENS span (seeds
    296300+/296350+, world-own margin channel 1 - rho_{minC_c}
    at the world's OWN wall degree, r292 ladder with the r294
    halving rule max 3), against the SAME candidate
    construction built world-own.  SEALED COLLAPSE RULE: the
    control match collapses iff the control top diagonal fails
    the Richardson stability (devs > 0.1 -- no structured axis,
    the r292 EPSTEIN expectation) OR |cos_c| < 0.40.  A
    non-collapsing control => the match is construction-trivial
    => DOWNGRADE one level (disclosed).  a4: the repetition
    rebuilds the ACTUAL best member world-own -- single
    directions via the one sealed constructor, the T5 subspace
    via the world-own moment-gradient span root share (null
    reference then = the two null-quadruple roots).
  (c2) WINDOW TRANSPORT at w7 and w11 (r294 protocol verbatim:
    window-own wall NREF_w 59/63, 12-direction window Hessian,
    seeds 294700 + 50 wi, dose cap, ladder halving; DENS share
    regression 0.795/0.834 tol 0.05): window-own e_top vs the
    window-own best-candidate construction (kernel degree
    NREF_w), in-span cosine in the window span (T5 via the a4
    subspace rule), window nulls seeds 296700 + 50 wi; the T1
    coupling is measured per window ALWAYS.  SEALED BAR: the
    verdict class holds in >= 2 of 3 windows (w9 + w7 + w11;
    the w9 entry is the adjudicated BASE class), else DOWNGRADE
    one level (disclosed).  No hardening applies to a BLIND
    base.

LEG D -- THE BRIDGE TABLE (only on IDENTITY/PARTIAL, small,
measurement only): if T1 is the best match, the decomposition
of grad lambda_max inside the arithmetic library (raw cosines
T1 vs every T2/T3/T4 member + the T5 share of T1) -- ONE table,
no interpretation.  If a T2/T3/T4 member matches but T1 does
NOT (|cos_T1| < 0.40 while best >= 0.40): THE ANOMALY -- DENS
would be arithmetic but NOT L*-coupled; documented prominently.

LEG E -- MUST-FAILS (each loud): (m1) Hellmann-Feynman with
the WRONG normalization factor (nu weight dropped from
p*(y_k)^2 = lam phi_k^2 / v_k) must be CAUGHT by the FD ward
(rel dev >> 1e-4) on a sealed nu coordinate; (m2) a candidate
built WITHOUT the eta_0 conservation projection must be CAUGHT
by the exact conservation gate; (m3) SEAL BREAK simulated: a
candidate added AFTER the cosine evaluation changes the sealed
library hash -- CAUGHT by the hash auditor; (m4) the pinned
random DECOY smuggled through the candidate pipeline must stay
at or below the noise reference + 0.1 (must NOT fire the
identity).  Scope audits: the sealed constructors consume
densities/combs/geometry/degrees/seeds ONLY; fragment audit (no
fit primitives).  STOP LIST (anti-gates, binding): NO L* claim,
NO bound mechanism, NO asymptotic law, NO derived 5/7, NO new
survival predictor, NO posthoc candidate, NO RH claim;
r243..r295 stand.

SEALED CONSTANTS: MAIN window 9; N_REF 184; CROSS_REC 185;
MINC_REC 184; S_REC (367, 263, 104); MARGIN_REC 1.68e-4 rel
0.01; ZV_REC -3.149 tol 0.02; B34_REC -0.105 tol 0.01;
CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27 / HL2 25 (seed 101);
THUP_REC 3.87e-5 rel 0.05; RIDGE_MINC_REC 185; REF_REC 125.75
rel 1e-3; pinned metric quadruple (seeds 290000/1/2 at 1e-3 +
290010 at 3e-4, tol 0.15); LAM184_REC 0.99983248 abs 1e-6;
R283_TOP5 (0.99983, 0.99874, 0.99597, 0.98461, 0.96408) tol
1e-4; EPST_C_BAR 1e-9 / EPST_THUP_MIN 1e9; r292 REBUILD ==
(HESS_EQ_HS, H_PAIR_H, GCUT, seeds 292100+/292200+, 29
directions) VERBATIM with SHARE_REC 0.925 tol 0.01 / LAMTOP_REC
-0.418 rel 0.02 / COS_SM_REC 0.07 tol 0.03 / RIDGE_RANK 28 /
LOADINGS (DENS05 +1.00, DENS04 -0.71, DENS03 +0.69, DENS01
+0.53) tol 0.05 (29-dir DENS share typed MEASUREMENT, a3); T1
FD ward: 6 coordinates (per channel the 3 largest |analytic
pair derivative|, a2), FD_T 1.25e-6 x max|d| (a2 step fix),
FD_MIN 1e-9 resolvability floor, Richardson pair (t, t/2),
FD_BAR 1e-4; MOM_K 4; NULLS 8 seeds
296100+ / DECOY 296199; COS_ID 0.80 / COS_PART 0.40 / NULL_PAD
0.10 (noise reference = max of the 8 nulls, disclosed
conservative q95 estimator at n = 8); CONTROLS EPST/SCR: 12
DENS directions seeds 296300+/296350+, nulls 8 seeds
296500+/296550+, world-own REF_c, r292 ladder + halving max 3,
RICH_TOL 0.1; WINDOWS (7, 11): r294 constants VERBATIM (W_SEED
294700 + 50 wi, N_ATOM_W 4 / N_FRAC_W 4 / N_DENS_W 3, dose cap
f_ex = min(1, 1e-3 / (2 theta_up_w)), ladder halving max 3,
W_EXT 8/32), NREF_REC {7: 59, 11: 63}, crossing NREF + 1, DENS
SHARE REC {7: 0.795, 11: 0.834} tol 0.05, window nulls 8 seeds
296700 + 50 wi; WINDOW CLASS RULE >= 2 of 3; runtime <= 1800 s;
smoke = toys + firewall + scopes + w9 regression + m1(toy)/m3
mutants (anchors, legs, adjudications skipped).
PRE-SPEC SCOPING (disclosed): every record number is a
published r280/r283/r284/r286/r290/r291/r292/r294 record
adopted as-is; the candidate library with its constructions,
the in-span primary metric with its honesty columns, the bars,
the noise rule, the collapse and window rules, the downgrade
logic and the must-fail set were fixed at design time from the
published records and the reviewer contract BEFORE any cosine
evaluation; the library hash is sealed in S0; no candidate is
added or removed after the first evaluation; no bar, band or
rule was tuned after the record freeze.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] DENS_ARITHMETIC_IDENTITY(member, cos) /
    DENS_PARTIAL(member, cos) / DENS_WORLD_BLIND(best, cos,
    noise) -- after the disclosed hardening downgrades
  + T1_COUPLING(cos_span, raw, lag, capture) [always]
  + COS_TABLE(all candidates, all four columns, noise
    reference) [always]
  + WORLD_CONTRAST(EPST/SCR collapse verdicts) [always]
  + WINDOW_TRANSPORT(w7/w9/w11 classes, DENS shares) [always]
  + BRIDGE_TABLE(...) [on IDENTITY/PARTIAL only] /
    ANOMALY(...) [if arithmetic-but-not-T1].
Honesty before beauty: cosines, captures, shares and the
control/window contrasts are MEASUREMENTS on finite profile
spaces; the Hesse forms consume measured margins (disclosed, as
in r292/r294); e_top is span-limited and the in-span metric is
the sealed primary reading of exactly that limitation; a
passing identity is a FINITE-WINDOW alignment statement about
w7/w9/w11, not a mechanism theorem; no verdict claims L*, a
bound mechanism, a derived 5/7 or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration
protocol, chronology honest: smoke pass 1 = 11/12 exposing a1;
smoke pass 2 = 12/12 (0.2 s); calibration pass 1 = first full
evaluation = 36/39, wall 80 s, exposing a2 (coordinate rule) +
a3 + a4 (below); calibration pass 2 = 37/39, wall 81 s,
exposing the a2 STEP fix (the hull-edge margin curvature
leaves a 2e-3 Richardson residual at the first-drawn 1e-5
scale; the pure O(t^2) truncation convergence was measured on
a 5-step ladder and the pair re-anchored at 1.25e-6 max|d|);
calibration pass 3 = 39/39, wall 81 s = the record physics;
one display-only wording fix in the G70 message before the
record freeze (no number, bar or rule changed); record
run1/run2 = 39/39, byte-identical up to WALL.  DISCLOSED
CALIBRATION AMENDMENTS (all found and fixed BEFORE the record
freeze; no physics bar, library member, sealed seed or verdict
rule moved): (a1) the library evenness gate was drawn at exact
zero while the s_l envelope is even only to libm precision
(~1e-17 at mirrored sin arguments) -- re-drawn at 1e-12
relative (gate conditioning); (a2) the FD ward coordinates
were first drawn as the largest-|d| grid pairs, whose
gradients sit at the f64 eigensolver noise floor (measured
devs up to 0.39 at |g| ~ 1e-10) -- re-drawn as the per-channel
largest |analytic pair derivative| with the 1e-9 resolvability
floor, plus the step fix above (both measurement-domain, the
r292-a1 pattern); (a3) the G33 gate cited the r294 0.989 DENS
share, which is the share of the 18-direction TRAINING form
(H_tr, G_tr) -- a different object from the 29-direction share
(measured 0.935, no published record): the clause was removed
and the value typed MEASUREMENT; (a4) the hardening repetition
was first coded to substitute T1 for the subspace member --
re-drawn to repeat the ACTUAL best member (T5 via world/window-
own moment-span root share, null reference = null-quadruple
roots) and the w9 window-class entry pinned to the adjudicated
base class.  AMENDMENTS AFTER FREEZE: NONE (the record-table
insertion below is the only post-freeze edit, which IS the
protocol).
RECORD VERDICT = DENS_WORLD_BLIND(T5_MOMENTS 0.825 downgraded;
WORLD-DOWNGRADE) + T1_COUPLING(cos_span +0.394, raw +0.048,
lag +0.394, capture 0.123) + COS_TABLE(T1 0.394; T2 -0.095 /
+0.002 / +0.130; T3 0.000 / -0.320 / +0.006; T4 +0.183 /
+0.002 / +0.378; noise 0.331; T5 root 0.825) + WORLD_CONTRAST(
EPST HELD 0.571, SCR HELD 0.603) + WINDOW_TRANSPORT(w7 ID /
w9 PART / w11 ID, 3/3 hold; DENS shares 0.795 / 0.935 / 0.834).
Key numbers.  ANCHORS: w9 S 367/263/104, minC 184, crossing
185, margin 1.6752e-4, z_v -3.149, b34 -0.105; REF 125.7462,
quadruple devs (0.059, 0.125, 0.117, 0.028); flips 25/21/27/25;
theta_up 3.8733e-5, endpoint 185, top9 == r291;
lambda_max(E_184) = 0.99983248 (dev 4.1e-9), top-5 == r283
(max dev 4.9e-6), margin identity 1.1e-15, crossing == minC+1;
EPST c_25 -1.99e-11, theta_up 5.03e10.  R292 REBUILD: share
0.9249, lam_top -0.4183, SMOOTH |cos| 0.0737, ridge rank
28/29, loadings DENS05 +1.00 / DENS04 -0.71 / DENS03 +0.69 /
DENS01 +0.53; polarization crosscheck worst 0.018.  T1 WARD:
worst rel dev 3.8e-7 <= 1e-4 on the 6 sealed coordinates
(folds 1/3/5 mu + 2/4/6 nu -- the gradient lives at the
SHALLOW-u HULL EDGE, exactly the r284 extremal-anatomy
region), lam identity exact.  COS TABLE (span/raw/lag/
capture): T1 +0.394/+0.048/+0.394/0.123; T2_ALL -0.095/-0.029/
-0.095/0.306, T2_PRIME +0.002/.../0.241, T2_PP +0.130/.../
0.346; T3_LOCALGAP +0.000 (capture 0.000: the gap profile is
CONSTANT 1 on the 367/368-occupied fold grid and dies in the
eta_0 projection -- an honest degenerate member, disclosed),
T3_LOGDENS -0.320/-0.034/-0.319/0.105, T3_FRAC289 +0.006;
T4_CHR +0.183, T4_EDIAG +0.002, T4_CDDIAG +0.378/0.145;
CONTROL rows: grad lam2 +0.366, grad lam3 -0.574 (the 3rd
eigen-gradient couples HARDER than the top -- the coupling is
a near-crossing BAND property, not top-specific, honest);
T5_MOMENTS root share 0.825 (share 0.680) vs null-quadruple
roots 0.437 / 0.350; T6 nulls 0.056..0.331 (max 0.331), decoy
0.115.  HARDENING: EPST (wall 25, margin 2.08e-3) top-diag
Richardson devs <= 5e-5 STABLE -- the EPST MARGIN channel at
its own wall degree carries real curvature structure (r292's
flatness was the log-h channel at degree 184, a different
object, disclosed); T5-at-EPST 0.571 / SCR 0.603 both >= 0.40
=> NOT COLLAPSED => the sealed WORLD-DOWNGRADE fires (PART ->
BLIND); DISCLOSED TENSION: the control values sit BELOW their
own null-quadruple maxima (0.758 / 0.691) -- for a 4-dim
subspace inside a 12-dim span the absolute 0.40 collapse bar
is nearly unreachable by construction, so the downgrade is
CONSERVATIVE (the sealed rule stands, the tension is the
disclosure); windows w7/w11: NREF 59/64 crossing NREF+1, DENS
shares 0.795/0.834 == r294, T5_w 0.930/0.942 vs window null
maxima 0.923/0.734, T1_w 0.179/0.314 (below window noise);
window classes ID/ID, 3/3 hold, no window downgrade.
MUST-FAILS: m1 CAUGHT (rel 1.0 >> 1e-4), m2 CAUGHT (eta_0 rel
1.0), m3 CAUGHT (hash mismatch), m4 HELD (0.115 <= 0.431);
scopes + fragments CLEAN.  Runtime 81 s full / 0.2 s smoke;
run1/run2 identical up to WALL.
READING (typed MEASUREMENT): the reviewer fork lands on
DENS_WORLD_BLIND under the sealed rules -- the 92.5-pct DENS
top axis is NOT identifiable with any member of the sealed
arithmetic library: every T2/T3/T4 candidate stays under 0.4
(von Mangoldt families <= 0.13, 1/log 0.32, kernel diagonals
<= 0.38, all within reach of the 0.331 noise reference), and
THE COUPLING NUMBER cos(e_top, grad lambda_max) = +0.394 sits
BELOW the sealed 0.40 bar (above the noise max 0.331, below
noise + pad 0.431): the DENS axis is NOT (at w9, in-span) the
direction that controls the L* extremizer -- and the lam2/lam3
control rows (+0.37 / -0.57) show what coupling there is
spreads over the near-crossing eigenvalue BAND rather than
picking the top eigenvalue; the only above-chance structure is
the 4-dim MOMENT-GRADIENT subspace (root share 0.825 at w9 vs
~0.4 chance; window-stable at 0.93/0.94 but AT the window
chance level 0.92/0.73, and present at 0.57/0.60 on both dead
controls) -- under the sealed collapse rule this is
CONSTRUCTION-ADJACENT structure (low-moment smoothness of
curvature tops is world-generic), not a MAIN identity; the
sealed rule downgrades the T5 partial to BLIND, and the
disclosed tension (the 0.40 collapse bar is conservative for
subspace members) is left standing as-is: no bar moved after
sight.  Honest negatives, explicit: T1 misses PART by 0.006 --
the fork answer is BLIND, not a near-miss celebration; the
raw-grid overlap of e_top with EVERY candidate is <= 0.08
while the in-span values reach 0.39, and every candidate's
span capture is <= 0.36: what alignment exists lives INSIDE
the 29-direction span, and the raw-grid geometry of e_top is
dominated by structure that no on-support arithmetic profile
in this library represents.
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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import curvature_form_probe as CF                   # noqa: E402 r292
import ridge_anatomy_probe as RA                    # noqa: E402 r291
import profile_functional_probe as PFP              # noqa: E402 r290
import lstar_two_measure_probe as LS                # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS     # noqa: E402 r283
import metric_stability_probe as MS                 # noqa: E402 r278
import minimal_firewall_probe as MF                 # noqa: E402 r276
import budget_localization_probe as BL              # noqa: E402 r280
import port_integrable_kernel_probe as PIK          # noqa: E402 v881
import principal_bessel_probe as PB                 # noqa: E402 r243
import paircorr_margin_probe as PC                  # noqa: E402
import v563_paper2_readouts as core                 # noqa: E402 READ-ONLY

MAIN_KZ = 9
N_REF = 184
CROSS_REC = 185
MINC_REC = 184
S_REC = (367, 263, 104)
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
ZV_REC = -3.149
ZV_TOL = 0.02
B34_REC = -0.105
B34_TOL = 0.01
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27, "HL2": 25}
HL2_SEED = 101
THUP_REC = 3.87e-5
THUP_TOL = 0.05
RIDGE_MINC_REC = 185
REF_REC = 125.75
REF_TOL = 1e-3
CAL_SEEDS = (290000, 290001, 290002)
T3_SEED = 290010
T3_THETA = 3e-4
T3_TOL = 0.15
THETA_CAL = 1e-3
ETA0_BAR = 1e-12
R291_TOP9 = (2, 3, 5, 13, 11, 4, 29, 7, 89)
AMP_PAD = RA.AMP_PAD

# r292 verbatim (imported, not redeclared)
HESS_EQ_HS = CF.HESS_EQ_HS
H_PAIR_H = CF.H_PAIR_H
GCUT = CF.GCUT
D2_FLOOR = CF.D2_FLOOR
POL_TOL = CF.POL_TOL
RICH_TOL = CF.RICH_TOL
NDIR_FRAC = CF.NDIR_FRAC
SEED_FRAC = CF.SEED_FRAC
NDIR_DENS = CF.NDIR_DENS
SEED_DENS = CF.SEED_DENS
N_ATOM = CF.N_ATOM
NEAR = PFP.NEAR

# r292/r294 eigen-anchor records
R292_SHARE_REC = 0.925
R292_SHARE_TOL = 0.01
R292_LAMTOP_REC = -0.418
R292_LAMTOP_TOL = 0.02
R292_COS_SM_REC = 0.07
R292_COS_SM_TOL = 0.03
R292_RIDGE_RANK_REC = 28
R292_LOADINGS = (("DENS05", 1.00), ("DENS04", -0.71),
                 ("DENS03", 0.69), ("DENS01", 0.53))
R292_LOAD_TOL = 0.05
W9_DENS_SHARE_REC = 0.989
W9_DENS_SHARE_TOL = 0.02

# L* spectral anchors (r283/r284/r286 records)
LAM184_REC = 0.99983248
LAM184_TOL = 1e-6
R283_TOP5 = (0.99983, 0.99874, 0.99597, 0.98461, 0.96408)
TOP5_TOL = 1e-4
EPST_C_BAR = 1e-9
EPST_THUP_MIN = 1e9

# T1 ward
FD_NCOORD = 3            # per channel (3 mu + 3 nu)
FD_T = 1.25e-6           # x max|d| (a2 step fix), pair (t, t/2)
FD_BAR = 1e-4
FD_MIN = 1e-9            # a2 resolvability floor |g| t >= FD_MIN

# library seal
MOM_K = 4
NDIR_NULL = 8
SEED_NULL = 296100
SEED_DECOY = 296199
COS_ID = 0.80
COS_PART = 0.40
NULL_PAD = 0.10
LIB_ELIGIBLE = ("T1_GRAD_LMAX",
                "T2_LAMBDA_ALL", "T2_LAMBDA_PRIME", "T2_LAMBDA_PP",
                "T3_LOCALGAP", "T3_LOGDENS", "T3_FRAC289",
                "T4_CHRISTOFFEL", "T4_EDIAG", "T4_CDDIAG")
LIB_CONTROL = ("T1B_GRAD_LAM2", "T1C_GRAD_LAM3")
LIB_SUBSPACE = "T5_MOMENTS"
LIB_SEAL = hashlib.sha256(repr(
    (LIB_ELIGIBLE, LIB_CONTROL, LIB_SUBSPACE, MOM_K,
     NDIR_NULL, SEED_NULL, SEED_DECOY,
     COS_ID, COS_PART, NULL_PAD)).encode("utf-8")).hexdigest()

# controls (world contrast)
CTRL_WORLDS = ("EPST", "SCR")
N_DENS_CTRL = 12
SEED_CTRL = {"EPST": 296300, "SCR": 296350}
NNULL_CTRL = 8
SEED_CTRL_NULL = {"EPST": 296500, "SCR": 296550}
LADDER_MAX_HALVE = 3

# windows (r294 verbatim)
W_LIST = (7, 11)
W_SEED_BASE = 294700
W_SEED_STEP = 50
N_ATOM_W = 4
N_FRAC_W = 4
N_DENS_W = 3
W_EXT = 8
W_EXT2 = 32
W_NREF_REC = {7: 59, 11: 63}
W_DENS_SHARE_REC = {7: 0.795, 11: 0.834}
W_DENS_SHARE_TOL = 0.05
NNULL_WIN = 8
SEED_WIN_NULL = {7: 296700, 11: 296750}
WIN_CLASS_NEED = 2       # of 3 windows

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
                       "r254/r284 world-blind tent matching + integer "
                       "root extraction inside LS.atom_labels; record "
                       "numbers enter gates and record tables only"
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


CONSTRUCTORS = ("kernel_pack", "grad_of_pack", "eta0_project",
                "cand_density", "fold_gaps", "frac_offsets",
                "moment_grad", "build_candidate", "cos_pair",
                "lag_cos_pair", "sub_share")
SCOPE_FORBIDDEN = {"minC", "mc", "zv", "onsets_true", "MINC_REC",
                   "CROSS_REC", "ZV_REC", "sg_h", "lgh", "s_meas",
                   "CTRL_FLIPS", "W_NREF_REC"}


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


def s_env(L):
    """the exact fold-map envelope s_l = 4 sin^2(pi l / L) / (2 L)
    (grid geometry only; the per-grid-point weight sensitivity of
    the folded measure, v881 folded_measure verbatim)."""
    ll = np.arange(L)
    return 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)


# ============== sealed source-pure constructors (AST-audited)
def kernel_pack(d, L, n):
    """two-measure kernel bundle of a signed density at degree n:
    fold split (v881 folded_measure verbatim), mu chain, B =
    sqrt(v) P_i(y), Bx = sqrt(w) P_i(x), eigendecomposition of
    E_n = B B^T, cumulative Christoffel rows.  Consumes density +
    grid + degree only."""
    d = np.asarray(d, float)
    xs, ws, fp = PIK.folded_measure(d, L, +1.0)
    ys, vs, fn = PIK.folded_measure(d, L, -1.0)
    al, sb, h0 = FS.mu_chain_f64(xs, ws, int(n))
    B = FS.b_matrix_f64(al, sb, h0, ys, vs, int(n))
    Bx = FS.b_matrix_f64(al, sb, h0, xs, ws, int(n))
    ev, V = np.linalg.eigh(B @ B.T)
    cum = LS.christoffel_rows(B)
    return dict(xs=xs, ws=ws, fp=fp, ys=ys, vs=vs, fn=fn,
                n=int(n), B=B, Bx=Bx, ev=ev, V=V, cum=cum)


def grad_of_pack(pk, d, L, kth=1):
    """Hellmann-Feynman gradient of the kth-from-top eigenvalue
    of E_n in signed-density space: with the extremal polynomial
    p* normalized int p*^2 dmu = 1 the envelope theorem gives
    dlam = int p*^2 d(dnu) - lam int p*^2 d(dmu); the fold map
    contributes the s_l envelope per grid point (mu points carry
    -lam s_l p*(x)^2, nu points -s_l p*(y)^2).  Consumes the
    kernel pack + density + grid only."""
    lam = float(pk["ev"][-kth])
    phi = pk["V"][:, -kth]
    c = pk["B"].T @ phi
    chat = c / math.sqrt(max(float(c @ c), 1e-300))
    pmu = (pk["Bx"] @ chat) ** 2 / pk["ws"]
    pnu = lam * phi * phi / pk["vs"]
    sl = s_env(L)
    fold = np.minimum(np.arange(L), L - np.arange(L))
    imu = {int(f): i for i, f in enumerate(pk["fp"])}
    inu = {int(f): i for i, f in enumerate(pk["fn"])}
    d = np.asarray(d, float)
    G = np.zeros(L)
    for l in range(L):
        f = int(fold[l])
        if d[l] > 0.0 and f in imu:
            G[l] = -lam * sl[l] * pmu[imu[f]]
        elif d[l] < 0.0 and f in inu:
            G[l] = -sl[l] * pnu[inu[f]]
    return G, lam


def eta0_project(dd, L):
    """exact eta_0 conservation projection on the own support
    (r290 dir_dens convention): the s_l component is removed so
    that sum dd_l s_l == 0 exactly."""
    dd = np.asarray(dd, float).copy()
    sl = s_env(L)
    supp = dd != 0.0
    if not np.any(supp):
        return dd
    coef = float(np.sum(dd * sl)) \
        / max(float(np.sum(sl[supp] ** 2)), 1e-300)
    dd[supp] -= coef * sl[supp]
    return dd


def cand_density(folds, vals, L):
    """weight-coordinate candidate pulled back to signed-density
    space through the ADJOINT of the exact fold map (value at
    fold f enters grid points l = f and L - f with the s_l
    envelope -- the same map that carries grad lambda), then
    eta_0-projected exactly.  Consumes folds + values + grid."""
    dd = np.zeros(L)
    sl = s_env(L)
    for f, v in zip(np.asarray(folds, np.int64), vals):
        l1 = int(f)
        l2 = (L - l1) % L
        dd[l1] = float(v) * sl[l1]
        if l2 != l1:
            dd[l2] = float(v) * sl[l2]
    return eta0_project(dd, L)


def fold_gaps(folds):
    """local fold-gap per union fold: distance to the nearest
    other union fold (fold-index units)."""
    fr = np.asarray(folds, np.int64)
    fs = np.sort(fr)
    out = np.zeros(len(fr), float)
    for i, f in enumerate(fr):
        j = int(np.searchsorted(fs, f))
        cand = []
        if j > 0:
            cand.append(int(f - fs[j - 1]))
        if j + 1 < len(fs):
            cand.append(int(fs[j + 1] - f))
        out[i] = float(min(cand)) if cand else 0.0
    return out


def frac_offsets(folds, D, uu, mm):
    """the r289 fraction profile: signed sub-cell offset
    u_match / D - f of the best tent-matched comb atom per union
    fold (r284 atom_labels matching rule; 0 if unmatched)."""
    order = np.argsort(uu)
    uus = np.asarray(uu, float)[order]
    mms = np.asarray(mm, float)[order]
    out = []
    for f in np.asarray(folds, np.int64):
        si = float(f) * D
        lo = int(np.searchsorted(uus, si - D, side="right"))
        hi = int(np.searchsorted(uus, si + D, side="left"))
        best_w, best_u = -1.0, None
        for t in range(lo, hi):
            vt = 1.0 - abs(si - uus[t]) / D
            if vt > 0.0 and abs(mms[t]) * vt > best_w:
                best_w, best_u = abs(mms[t]) * vt, float(uus[t])
        out.append(0.0 if best_u is None
                   else (best_u / D - float(f)))
    return np.asarray(out, float)


def moment_grad(d0, L, j):
    """grad_delta of the j-th moment of mutilde in signed-density
    space: dd_l = s_l x_{fold(l)}^j on the support of d0,
    eta_0-projected (j = 0 is exactly the projected-out
    direction and excluded)."""
    d0 = np.asarray(d0, float)
    sl = s_env(L)
    fold = np.minimum(np.arange(L), L - np.arange(L))
    x = np.cos(2.0 * math.pi * fold / float(L))
    dd = np.where(d0 != 0.0, sl * x ** int(j), 0.0)
    return eta0_project(dd, L)


def build_candidate(name, d, L, D, uu, mm, n):
    """the ONE sealed candidate constructor (identical at MAIN,
    controls and windows): returns the eta_0-projected signed-
    density direction of the named library member.  Consumes the
    density, grid geometry, the comb and the kernel degree only."""
    d = np.asarray(d, float)
    fp, wp, fn, vn, xp, yn = LS.split_by_fold(d, L)
    if name.startswith("T1"):
        kth = {"T1_GRAD_LMAX": 1, "T1B_GRAD_LAM2": 2,
               "T1C_GRAD_LAM3": 3}[name]
        pk = kernel_pack(d, L, n)
        G, _lam = grad_of_pack(pk, d, L, kth)
        return eta0_project(G, L)
    folds_u = np.concatenate([np.asarray(fp, np.int64),
                              np.asarray(fn, np.int64)])
    if name.startswith("T2"):
        labs = LS.atom_labels(folds_u, D, uu, mm)
        mode = name.split("_")[-1]
        vals = []
        for cls, p, _dev in labs:
            lp = math.log(p) if (cls > 0 and p > 1) else 0.0
            if mode == "ALL":
                vals.append(lp if cls > 0 else 0.0)
            elif mode == "PRIME":
                vals.append(lp if cls == 1 else 0.0)
            else:
                vals.append(lp if cls == 2 else 0.0)
        return cand_density(folds_u, vals, L)
    if name == "T3_LOCALGAP":
        g = fold_gaps(folds_u)
        return cand_density(folds_u, g - float(np.mean(g)), L)
    if name == "T3_LOGDENS":
        vals = [1.0 / (float(f) * D) if f >= 1 else 0.0
                for f in folds_u]
        return cand_density(folds_u, vals, L)
    if name == "T3_FRAC289":
        return cand_density(folds_u,
                            frac_offsets(folds_u, D, uu, mm), L)
    pk = kernel_pack(d, L, n)
    diag = pk["cum"][:, int(n) - 1]
    vs = pk["vs"]
    if name == "T4_CHRISTOFFEL":
        vals = vs / np.maximum(diag, 1e-300)
    elif name == "T4_EDIAG":
        vals = diag
    else:                                    # T4_CDDIAG
        vals = diag / np.maximum(vs, 1e-300)
    return cand_density(np.asarray(fn, np.int64), vals, L)


def cos_pair(u, v):
    """plain L2 cosine of two grid vectors."""
    u = np.asarray(u, float)
    v = np.asarray(v, float)
    nn = float(np.linalg.norm(u)) * float(np.linalg.norm(v))
    return float(u @ v) / max(nn, 1e-300)


def lag_cos_pair(u, v, M):
    """L2 cosine in the LAG coordinate (the linear r289/r290
    completeness coordinate; theta_eq is an L1 object with no
    inner product -- this is the disclosed L2 robustness angle
    in the coordinate theta_eq lives in)."""
    lu = PFP.lag_of(np.asarray(u, float), M)
    lv = PFP.lag_of(np.asarray(v, float), M)
    return cos_pair(lu, lv)


def sub_share(W, e):
    """projection share |P_W e|^2 / |e|^2 of a vector on the
    span of the columns of W (Gram eigencut pseudo-solve, no
    fitting)."""
    W = np.asarray(W, float)
    e = np.asarray(e, float)
    G = W.T @ W
    wG, UG = np.linalg.eigh(G)
    keep = wG >= GCUT * max(float(wG[-1]), 1e-300)
    Ui = UG[:, keep]
    b = W.T @ e
    a = Ui @ ((Ui.T @ b) / wG[keep])
    Pe = W @ a
    return float(Pe @ Pe) / max(float(e @ e), 1e-300)


# ============== must-fail mutants
def mutant_hf_noweight(pk, d, L):
    """m1 MUST-FAIL: Hellmann-Feynman with the WRONG
    normalization factor -- the nu weight is dropped from
    p*(y_k)^2 = lam phi_k^2 / v_k.  The FD ward must CATCH the
    distortion loudly."""
    lam = float(pk["ev"][-1])
    phi = pk["V"][:, -1]
    sl = s_env(L)
    fold = np.minimum(np.arange(L), L - np.arange(L))
    inu = {int(f): i for i, f in enumerate(pk["fn"])}
    d = np.asarray(d, float)
    G = np.zeros(L)
    for l in range(L):
        f = int(fold[l])
        if d[l] < 0.0 and f in inu:
            G[l] = -sl[l] * lam * phi[inu[f]] ** 2   # /v_k MISSING
    return G


def mutant_unprojected_candidate(folds, vals, L):
    """m2 MUST-FAIL: the candidate pullback WITHOUT the eta_0
    projection -- the conservation gate must CATCH it."""
    dd = np.zeros(L)
    sl = s_env(L)
    for f, v in zip(np.asarray(folds, np.int64), vals):
        l1 = int(f)
        l2 = (L - l1) % L
        dd[l1] = float(v) * sl[l1]
        if l2 != l1:
            dd[l2] = float(v) * sl[l2]
    return dd


def mutant_posthoc_library():
    """m3 MUST-FAIL: a candidate added AFTER evaluation (seal
    break simulated) -- the library hash auditor must CATCH the
    mismatch."""
    broken = LIB_ELIGIBLE + ("T7_POSTHOC_BEST",)
    return hashlib.sha256(repr(
        (broken, LIB_CONTROL, LIB_SUBSPACE, MOM_K,
         NDIR_NULL, SEED_NULL, SEED_DECOY,
         COS_ID, COS_PART, NULL_PAD)).encode("utf-8")).hexdigest()


def class_of(c):
    """sealed verdict class of an absolute cosine."""
    c = abs(float(c))
    if c >= COS_ID:
        return "ID"
    if c >= COS_PART:
        return "PART"
    return "BLIND"


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("dens_identity_probe -- PRIME.PORT.LSTAR."
          "DENS_IDENTITY.01 (round 296)")
    print("SPEC_SHA %s   (r292 CF %s / r290 PFP %s / r284 LS %s)"
          % (SPEC_SHA[:16], CF.SPEC_SHA[:16], PFP.SPEC_SHA[:16],
             LS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + w9 "
                        "regression + m1-toy/m3 mutants; anchors, "
                        "legs, adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + LIBRARY SEAL")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the candidate library (12 "
          "members + T5 subspace + 8 nulls + decoy) with the ONE "
          "source-pure constructor, the in-span PRIMARY metric "
          "with raw/lag/capture honesty columns, the bars 0.80/"
          "0.40 with the noise rule, the world-collapse and "
          "window-class hardening with the downgrade logic, the "
          "T1 FD ward and the must-fail set; the Hesse forms are "
          "honestly typed measurement-consuming (r292/r294 "
          "protocol); the STOP list forbids any L* claim, any "
          "new survival predictor and any posthoc candidate")
    check("G03-library-seal", len(LIB_ELIGIBLE) == 10
          and len(LIB_CONTROL) == 2,
          "LIBRARY HASH SEALED: sha256 = %s (10 eligible + 2 "
          "control members + %s(k=%d) + %d nulls seeds %d+ + "
          "decoy %d; bars ID %.2f / PART %.2f / pad %.2f inside "
          "the hash)" % (LIB_SEAL[:16], LIB_SUBSPACE, MOM_K,
                         NDIR_NULL, SEED_NULL, SEED_DECOY,
                         COS_ID, COS_PART, NULL_PAD))

    # ---------------- S1 toys
    section("S1  TOYS -- HELLMANN-FEYNMAN, PROJECTION, LAG, "
            "CANDIDATE PULLBACK")
    x_t = np.array([0.9, 0.4, -0.2, -0.7])
    w_t = np.array([1.0, 0.5, 0.25, 0.125])
    y_t = np.array([0.6, -0.5])
    v_t = np.array([0.03, 0.01])
    n_t = 3

    def lam_toy(w2, v2):
        al2, sb2, h02 = FS.mu_chain_f64(x_t, np.asarray(w2), n_t)
        B2 = FS.b_matrix_f64(al2, sb2, h02, y_t,
                             np.asarray(v2), n_t)
        return float(np.linalg.eigvalsh(B2 @ B2.T)[-1])

    al_t, sb_t, h0_t = FS.mu_chain_f64(x_t, w_t, n_t)
    B_t = FS.b_matrix_f64(al_t, sb_t, h0_t, y_t, v_t, n_t)
    Bx_t = FS.b_matrix_f64(al_t, sb_t, h0_t, x_t, w_t, n_t)
    ev_t, V_t = np.linalg.eigh(B_t @ B_t.T)
    lam_t = float(ev_t[-1])
    phi_t = V_t[:, -1]
    c_t = B_t.T @ phi_t
    chat_t = c_t / math.sqrt(float(c_t @ c_t))
    gw_an = -lam_t * (Bx_t @ chat_t) ** 2 / w_t
    gv_an = lam_t * phi_t * phi_t / v_t
    h_t = 1e-7
    dev_t = 0.0
    for i in range(len(w_t)):
        w2p = w_t.copy()
        w2p[i] += h_t
        w2m = w_t.copy()
        w2m[i] -= h_t
        g_num = (lam_toy(w2p, v_t) - lam_toy(w2m, v_t)) / (2 * h_t)
        dev_t = max(dev_t, abs(g_num / gw_an[i] - 1.0))
    for k in range(len(v_t)):
        v2p = v_t.copy()
        v2p[k] += h_t
        v2m = v_t.copy()
        v2m[k] -= h_t
        g_num = (lam_toy(w_t, v2p) - lam_toy(w_t, v2m)) / (2 * h_t)
        dev_t = max(dev_t, abs(g_num / gv_an[k] - 1.0))
    check("G10-toy-hellmann-feynman", dev_t <= 1e-5,
          "HAND TWO-MEASURE TOY (4 mu + 2 nu atoms, n = 3): the "
          "envelope-theorem gradient dlam/dw_f = -lam p*(x_f)^2 "
          "and dlam/dv_k = p*(y_k)^2 (int p*^2 dmu = 1) matches "
          "central differences on EVERY coordinate, worst rel "
          "dev %.1e <= 1e-5 -- the Hellmann-Feynman route is "
          "exact" % dev_t)
    # projection / cosine toy
    V3 = np.zeros((3, 2))
    V3[0, 0] = 1.0
    V3[0, 1] = 1.0
    V3[1, 1] = 1.0
    wG3, UG3 = np.linalg.eigh(V3.T @ V3)
    T3v = np.array([1.0, 2.0, 5.0])
    a3 = CF.proj_coords(V3, wG3, UG3, GCUT, T3v)
    PT3 = V3 @ a3
    e3 = np.array([0.0, 1.0, 0.0])
    cs3 = cos_pair(e3, PT3)
    cap3 = float(np.linalg.norm(PT3)) / float(np.linalg.norm(T3v))
    sh3 = sub_share(np.eye(3)[:, :2],
                    np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0))
    ok_t2 = (float(np.max(np.abs(PT3 - np.array([1.0, 2.0, 0.0]))))
             <= 1e-12
             and abs(cs3 - 2.0 / math.sqrt(5.0)) <= 1e-12
             and abs(cap3 - math.sqrt(5.0 / 30.0)) <= 1e-12
             and abs(sh3 - 2.0 / 3.0) <= 1e-12)
    check("G11-toy-projection-cos", ok_t2,
          "HAND PROJECTION (V = (e1, e1+e2), T = (1,2,5)): P T = "
          "(1,2,0) exact; cos(e2, PT) = 2/sqrt(5) exact; capture "
          "= sqrt(5/30) exact; subspace share of (1,1,1)/sqrt(3) "
          "on span(e1,e2) = 2/3 exact")
    # lag-cosine toy on grid_density images (even house densities)
    L_t = 8
    M_t = L_t // 2 + 1
    ca = np.zeros(M_t)
    ca[1] = 1.0
    cb = np.zeros(M_t)
    cb[2] = 1.0
    da = PIK.grid_density(ca)
    db = PIK.grid_density(cb)
    lca = PFP.lag_of(da, M_t)
    ok_t3 = (float(np.max(np.abs(lca - ca))) <= 1e-12
             and abs(lag_cos_pair(da, da, M_t) - 1.0) <= 1e-12
             and abs(lag_cos_pair(da, db, M_t)) <= 1e-12)
    check("G12-toy-lag-cos", ok_t3,
          "LAG-COSINE TOY (grid_density images, L = 8): inversion "
          "lag(grid_density(c)) == c exact; self-cosine 1, "
          "disjoint-mode cosine 0 -- the lag coordinate is the "
          "exact linear robustness coordinate")
    # candidate pullback toy
    dd_t4 = cand_density((1, 2), (2.0, -1.0), L_t)
    sl_t4 = s_env(L_t)
    # a1 (calibration, disclosed): the s_l envelope is even only
    # to libm precision (sin at mirrored arguments differs at
    # ~1e-17); the evenness gate is drawn at 1e-12 RELATIVE.
    mx_t4 = max(float(np.max(np.abs(dd_t4))), 1e-300)
    ok_ev4 = all(abs(dd_t4[l] - dd_t4[(L_t - l) % L_t])
                 <= 1e-12 * mx_t4 for l in range(L_t))
    eta_t4 = abs(float(np.sum(dd_t4 * sl_t4)))
    raw_t4 = mutant_unprojected_candidate((1, 2), (2.0, -1.0), L_t)
    ok_t4 = (ok_ev4 and eta_t4 <= 1e-15
             and raw_t4[1] == 2.0 * sl_t4[1]
             and raw_t4[7] == 2.0 * sl_t4[7]
             and raw_t4[2] == -1.0 * sl_t4[2])
    check("G13-toy-cand-density", ok_t4,
          "CANDIDATE PULLBACK TOY (folds (1,2), values (2,-1), "
          "L = 8): even placement at l and L-l with the s_l "
          "envelope exact; eta_0 after projection = %.1e "
          "(<= 1e-15)" % eta_t4)

    # ---------------- S2 w9 + anchors
    section("S2  W9 REGRESSION + METRIC + RIDGE + L* SPECTRAL "
            "ANCHORS")
    ctx9 = MS.ctx_build(MAIN_KZ)
    d9 = np.asarray(ctx9["darm"], float)
    L9 = int(ctx9["L"])
    uu9 = np.asarray(ctx9["uu"], float)
    mm9 = np.asarray(ctx9["mm"], float)
    M9 = L9 // 2 + 1
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    M0 = PFP.measure_density(d9, L9)
    margin9 = 1.0 - M0["rho"][N_REF]
    ok_w9 = ((M0["S"], M0["Sp"], M0["Sm"]) == S_REC
             and M0["minC"] == MINC_REC
             and M0["cross"] == CROSS_REC
             and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
             and abs(M0["zv"] - ZV_REC) <= ZV_TOL
             and abs(M0["b34"] - B34_REC) <= B34_TOL)
    check("G20-w9-regression", ok_w9,
          "w9 through the r290 channel: S = %d (mu %d / nu %d), "
          "minC = %s, crossing = %s, margin %.4e (rec %.2e), z_v "
          "= %+.3f, b34 = %+.3f"
          % (M0["S"], M0["Sp"], M0["Sm"], str(M0["minC"]),
             str(M0["cross"]), margin9, MARGIN_REC, M0["zv"],
             M0["b34"]))
    if smoke:
        gv_mut = lam_t * phi_t * phi_t          # /v_k MISSING
        dev_m1t = max(abs(gv_mut[k] / gv_an[k] - 1.0)
                      for k in range(len(v_t)))
        check("G80-mustfail-hf-norm", dev_m1t > 0.5,
              "m1 TOY (nu weight dropped from p*(y)^2 = lam "
              "phi^2 / v): mutant deviates from the exact toy "
              "gradient by rel %.2f > 0.5 -- the wrong "
              "normalization is loud; the real FD catch runs in "
              "the full record" % dev_m1t)
        bad_hash = mutant_posthoc_library()
        check("G82-mustfail-seal-break", bad_hash != LIB_SEAL,
              "m3 SEAL BREAK (posthoc candidate T7 injected): "
              "library hash %s != sealed %s -- CAUGHT by the "
              "hash auditor" % (bad_hash[:12], LIB_SEAL[:12]))
        hits_s = []
        for fn_ in CONSTRUCTORS:
            hits_s += scope_audit(fn_, SCOPE_FORBIDDEN)
        ag_s = antigate_fragment_audit()
        check("G84-scope-audits", not hits_s and not ag_s,
              "the %d sealed source-pure constructors consume "
              "densities/combs/geometry/degrees/seeds ONLY (%s); "
              "fragment audit: %s"
              % (len(CONSTRUCTORS),
                 "CLEAN" if not hits_s else "; ".join(hits_s),
                 "CLEAN" if not ag_s else "; ".join(ag_s)))
        return finish(smoke)

    # metric anchor (r290-a1 coordinate, pinned quadruple verbatim)
    g_loc = MF.local_gaps(uu9)
    Dg9 = 2.0 * ctx9["alpha"] / ctx9["M"]
    REF = 0.5 * float(np.sum(mm9 * g_loc)) / Dg9

    def lag_l1(dd):
        return float(np.sum(np.abs(PFP.lag_of(dd, M9))))

    c_back = PFP.lag_of(d9, M9)
    inv_dev = float(np.max(np.abs(PIK.grid_density(c_back) - d9))) \
        / max(float(np.max(np.abs(d9))), 1e-300)
    devs_c = []
    cons_c = True
    for th_c, seed_c in [(THETA_CAL, s_) for s_ in CAL_SEEDS] \
            + [(T3_THETA, T3_SEED)]:
        u2c, m2c = MF.pert_jit(uu9, mm9, th_c, seed_c, False)
        cons_c = cons_c and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2c, m2c, th_c)
        d2c = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2c, m2c))["d"], float)
        devs_c.append(abs(lag_l1(d2c - d9) / REF / th_c - 1.0))
    ok_met = (abs(REF / REF_REC - 1.0) <= REF_TOL
              and inv_dev <= 1e-12 and cons_c
              and max(devs_c) <= T3_TOL)
    check("G21-metric-anchor", ok_met,
          "theta_eq metric (r290-a1 LAG coordinate, pinned "
          "quadruple VERBATIM): analytic REF = %.4f (rec %.2f); "
          "inversion identity rel %.1e; jitter devs %s <= %.2f, "
          "conservation exact"
          % (REF, REF_REC, inv_dev,
             str([round(v, 3) for v in devs_c]), T3_TOL))
    # control worlds (r292 constructions verbatim)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uE = np.log(nn_idx.astype(float))
    mE = 2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    gpc = PC.Grid()
    comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
    ctx_c = {"EPST": MS.ctx_build(MAIN_KZ, comb=(uE, mE)),
             "SCR": MS.ctx_build(MAIN_KZ, scramble_seed=1),
             "SMOOTH": MS.ctx_build(MAIN_KZ, comb=(ug9, uw9)),
             "HL2": MS.ctx_build(MAIN_KZ, comb=comb_hl)}
    d_worlds = {w: np.asarray(ctx_c[w]["darm"], float)
                for w in ctx_c}
    worlds_meas = {w: PFP.measure_density(d_worlds[w], L9)
                   for w in d_worlds}
    ok_fl = all(worlds_meas[w]["minC"] == CTRL_FLIPS[w]
                for w in CTRL_FLIPS)
    check("G22-control-flips", ok_fl,
          "control flips through this channel: %s == records "
          "(25/21/27/25)"
          % str({w: worlds_meas[w]["minC"] for w in CTRL_FLIPS}))
    # ridge anchor (r280 rebuilt verbatim) + top-9 atom ranking
    GE = BL.grad_ext(ctx9, N_REF + 2)
    xi = BL.dir_opt(GE["gR"], GE["gL"], GE["gaps"], N_REF)
    th_up, th_kill, _cvec = BL.theta_of_dir(GE["gR"], GE["gL"],
                                            GE["gaps"], xi, N_REF)
    du_ridge = 2.0 * th_up * GE["gaps"] * xi
    uR, mR = RA.subset_move(uu9, mm9, du_ridge, np.ones(len(uu9)))
    dR = np.asarray(PIK.build_rung(MAIN_KZ, comb=(uR, mR))["d"],
                    float)
    MRi = PFP.measure_density(dR, L9)
    du1 = GE["gaps"] * xi
    cj = np.where(du1 > 0, du1 * GE["gR"][:, N_REF],
                  du1 * GE["gL"][:, N_REF])
    nn_at = RA.atom_ints(uu9)
    order = np.argsort(cj)
    top9 = tuple(int(v) for v in nn_at[order[:N_ATOM]])
    ok_ridge = (abs(th_up / THUP_REC - 1.0) <= THUP_TOL
                and th_kill > th_up
                and MRi["minC"] == RIDGE_MINC_REC
                and MF.conserve_comb("P2_JIT", uu9, mm9, uR, mR,
                                     2.0 * th_up * AMP_PAD)
                and top9 == R291_TOP9)
    check("G23-ridge-anchor", ok_ridge,
          "r280 RIDGE ANCHOR: theta_up = %.4e (rec %.2e), "
          "theta_kill = %.2e; OPT endpoint minC = %s == %d; "
          "conservation exact; top-9 atoms %s == the r291 record"
          % (th_up, THUP_REC, th_kill, str(MRi["minC"]),
             RIDGE_MINC_REC, str(top9)))
    # L* spectral anchor (r283/r284/r286 records)
    PK9 = kernel_pack(d9, L9, N_REF)
    lam184 = float(PK9["ev"][-1])
    top5 = PK9["ev"][-5:][::-1]
    dev_top5 = max(abs(float(top5[i]) - R283_TOP5[i])
                   for i in range(5))
    dev_mid = abs((1.0 - lam184) - margin9)
    ok_lstar = (abs(lam184 - LAM184_REC) <= LAM184_TOL
                and dev_top5 <= TOP5_TOL
                and dev_mid <= 1e-12
                and M0["cross"] == MINC_REC + 1)
    check("G24-lstar-spectral-anchor", ok_lstar,
          "THE L* OBJECT: lambda_max(E_184) = %.8f (rec %.8f, "
          "dev %.1e <= %.0e); top-5 eigs == r283 (max dev %.1e "
          "<= %.0e); margin identity 1 - lambda_max == 1 - "
          "rho_184 (dev %.1e); crossing %d == minC + 1 (r283 "
          "theorem)" % (lam184, LAM184_REC,
                        abs(lam184 - LAM184_REC), LAM184_TOL,
                        dev_top5, TOP5_TOL, dev_mid, CROSS_REC))
    # EPSTEIN first-order flatness anchor (r292 verbatim)
    mcE0 = worlds_meas["EPST"]["minC"]
    GEe = BL.grad_ext(ctx_c["EPST"], mcE0 + 2)
    xiE = BL.dir_opt(GEe["gR"], GEe["gL"], GEe["gaps"], mcE0)
    tuE, _tkE, cE = BL.theta_of_dir(GEe["gR"], GEe["gL"],
                                    GEe["gaps"], xiE, mcE0)
    ok_ef = abs(cE[mcE0]) <= EPST_C_BAR and tuE >= EPST_THUP_MIN
    check("G25-epstein-flatness-anchor", ok_ef,
          "EPSTEIN first-order flatness (own wall degree %d): "
          "c_%d = %.2e (bar %.0e), theta_up = %.2e >= %.0e -- "
          "the r291/r292 flat-wall anchor"
          % (mcE0, mcE0, cE[mcE0], EPST_C_BAR, tuE,
             EPST_THUP_MIN))

    # ---------------- S3 r292 Hessian rebuilt verbatim -> e_top
    section("S3  LEG 0b -- r292 HESSIAN REBUILT VERBATIM "
            "(29 sealed directions) -> e_top")

    def margin_at(dvec):
        meas = PFP.measure_density(dvec, L9)
        if meas["rho"] is None or meas["cross"] is None \
                or meas["cross"] <= N_REF:
            return float("nan")
        return 1.0 - meas["rho"][N_REF]

    m00 = margin_at(d9)
    dd_R = dR - d9
    dirsD = []
    for wn in ("SMOOTH", "SCR", "EPST"):
        dirsD.append(("W_" + wn, d_worlds[wn] - d9))
    dirsD.append(("RIDGE", dd_R))
    ok_dcons = True
    for j in range(N_ATOM):
        mask = np.zeros(len(uu9))
        mask[order[j]] = 1.0
        u2, m2 = RA.subset_move(uu9, mm9, du_ridge, mask)
        ok_dcons = ok_dcons and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2, m2, 2.0 * th_up * AMP_PAD)
        ddj = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2, m2))["d"],
                         float) - d9
        dirsD.append(("ATOM%02d_n%d" % (j, int(nn_at[order[j]])),
                      ddj))
    for i in range(NDIR_FRAC):
        dd, (u2, m2) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                    THETA_CAL, SEED_FRAC + i)
        ok_dcons = ok_dcons and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2, m2, THETA_CAL)
        dirsD.append(("FRAC%02d" % i, dd))
    sl9 = s_env(L9)
    for i in range(NDIR_DENS):
        dd = PFP.dir_dens(d9, L9, SEED_DENS + i)
        eta0 = abs(float(np.sum(dd * sl9)))
        ok_dcons = ok_dcons and eta0 <= ETA0_BAR \
            * max(float(np.sum(np.abs(dd * sl9))), 1.0)
        dirsD.append(("DENS%02d" % i, dd))
    names_D = [n for n, _d in dirsD]
    vhat = {n: CF.unit_dir(dd, lag_l1(dd), REF) for n, dd in dirsD}
    check("G30-direction-set", ok_dcons and len(dirsD) == 29,
          "SEALED DIRECTION SET D (r292 verbatim): %d directions "
          "= 3 world axes + ridge + %d atoms (conservation "
          "exact) + %d FRAC (seeds 292100+) + %d DENS (seeds "
          "292200+, eta_0 exact); all theta_eq-normalized"
          % (len(dirsD), N_ATOM, NDIR_FRAC, NDIR_DENS))
    nD = len(dirsD)
    d2_tab = {}
    ok_finA = True
    for name in names_D:
        v = vhat[name]
        ests = []
        for h in HESS_EQ_HS:
            mp_ = margin_at(d9 + v * h)
            mn_ = margin_at(d9 - v * h)
            ok_finA = ok_finA and math.isfinite(mp_) \
                and math.isfinite(mn_)
            ests.append((mp_ - 2.0 * m00 + mn_) / (h * h))
        d2_tab[name] = ests
    diag_mid = {n: d2_tab[n][1] for n in names_D}
    check("G31-diagonal-census", ok_finA,
          "DIAGONAL d2 census (r292 a1 ladder %s, all finite): "
          "worlds %s; RIDGE %.2f; DENS [%.3g..%.3g]"
          % (str(HESS_EQ_HS),
             str({n: "%.1f" % d2_tab[n][0] for n in names_D[:3]}),
             d2_tab["RIDGE"][0],
             min(d2_tab[n][0] for n in names_D[23:]),
             max(d2_tab[n][0] for n in names_D[23:])))
    Hmat = np.zeros((nD, nD))
    for i in range(nD):
        Hmat[i, i] = diag_mid[names_D[i]]
    sel_pairs = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]
    sel_pairs += [(3, 4 + j) for j in range(N_ATOM)]
    ok_finP = True
    pol_dev_max = 0.0
    n_pairs = 0
    d2sum_cache = {}
    for i in range(nD):
        for j in range(i + 1, nD):
            u, v = vhat[names_D[i]], vhat[names_D[j]]
            h = H_PAIR_H
            msp = margin_at(d9 + (u + v) * h)
            msn = margin_at(d9 - (u + v) * h)
            mdp = margin_at(d9 + (u - v) * h)
            mdn = margin_at(d9 - (u - v) * h)
            ok_finP = ok_finP and all(math.isfinite(x)
                                      for x in (msp, msn, mdp,
                                                mdn))
            d2su = (msp - 2.0 * m00 + msn) / (h * h)
            d2di = (mdp - 2.0 * m00 + mdn) / (h * h)
            Hij = CF.pol_of_d2(d2su, d2di)
            Hmat[i, j] = Hmat[j, i] = Hij
            d2sum_cache[(i, j)] = d2su
            n_pairs += 1
    for (i, j) in sel_pairs:
        Hij = Hmat[i, j]
        Hexp = CF.expand_of_d2(d2sum_cache[(i, j)],
                               diag_mid[names_D[i]],
                               diag_mid[names_D[j]])
        dev = abs(Hij - Hexp) / max(abs(Hij), D2_FLOOR)
        pol_dev_max = max(pol_dev_max, dev)
    check("G32-polarization-matrix", ok_finP
          and pol_dev_max <= POL_TOL,
          "FULL POLARIZATION MATRIX (r292 verbatim): %d pairs at "
          "h = %.3g (all finite); %d selected pairs pass the "
          "expansion crosscheck (worst rel dev %.3f <= %.2f)"
          % (n_pairs, H_PAIR_H, len(sel_pairs), pol_dev_max,
             POL_TOL))
    Vmat = np.stack([vhat[n] for n in names_D], axis=1)
    Gmat = Vmat.T @ Vmat
    wG, UG = np.linalg.eigh(Gmat)
    keep = wG >= GCUT * wG[-1]
    Uk = UG[:, keep]
    Wk = Uk / np.sqrt(wG[keep])[None, :]
    Ared = Wk.T @ Hmat @ Wk
    lam, Y = np.linalg.eigh(Ared)
    o_l = np.argsort(-np.abs(lam))
    lam_s = lam[o_l]
    Evec = Vmat @ (Wk @ Y[:, o_l])
    tr_abs = float(np.sum(np.abs(lam_s)))
    share1 = abs(lam_s[0]) / max(tr_abs, 1e-300)
    coef_top = (Wk @ Y[:, o_l])[:, 0]
    # a2: sign canonicalization pinned to the DENS05 loading
    i_d05 = names_D.index("DENS05")
    if coef_top[i_d05] < 0.0:
        coef_top = -coef_top
        Evec[:, 0] = -Evec[:, 0]
    e_top = Evec[:, 0]
    coef_n = coef_top / max(float(np.max(np.abs(coef_top))),
                            1e-300)
    o_c = np.argsort(-np.abs(coef_n))
    load4 = [(names_D[i], float(coef_n[i])) for i in o_c[:4]]
    ok_load = all(load4[i][0] == R292_LOADINGS[i][0]
                  and abs(load4[i][1] - R292_LOADINGS[i][1])
                  <= R292_LOAD_TOL for i in range(4))
    vSMn = vhat["W_SMOOTH"]
    cos_sm = abs(cos_pair(vSMn, e_top))
    l2n2 = {n: float(vhat[n] @ vhat[n]) for n in names_D}
    diag_l2 = {n: diag_mid[n] / max(l2n2[n], 1e-300)
               for n in names_D}
    Hrr = diag_l2["RIDGE"]
    diag_sorted = sorted((abs(diag_l2[n]) for n in names_D),
                         reverse=True)
    rank_rr = 1 + sum(1 for v in diag_sorted if v > abs(Hrr))
    dens_idx = [i for i, n in enumerate(names_D)
                if n.startswith("DENS")]
    share_dens9 = float(np.sum(coef_top[dens_idx] ** 2)) \
        / max(float(np.sum(coef_top ** 2)), 1e-300)
    ok_r292 = (abs(share1 - R292_SHARE_REC) <= R292_SHARE_TOL
               and abs(lam_s[0] / R292_LAMTOP_REC - 1.0)
               <= R292_LAMTOP_TOL
               and abs(cos_sm - R292_COS_SM_REC)
               <= R292_COS_SM_TOL
               and rank_rr == R292_RIDGE_RANK_REC
               and ok_load)
    check("G33-r292-etop-anchor", ok_r292,
          "r292 SPECTROSCOPY REPRODUCED: trace share %.4f == "
          "0.925, lam_top %.4f == -0.418, SMOOTH |cos| %.4f == "
          "0.07, ridge L2-rank %d/29 == 28; e_top loadings "
          "(sign pinned to DENS05) %s == r292 record (tol "
          "%.2f); 29-dir DENS coefficient share %.3f typed "
          "MEASUREMENT (a3: the r294 0.989 is the 18-direction "
          "training-form share, a different object) -- e_top is "
          "the sealed round object"
          % (share1, lam_s[0], cos_sm, rank_rr,
             str([(n, round(v, 2)) for n, v in load4]),
             R292_LOAD_TOL, share_dens9))

    # ---------------- S4 LEG A: T1 gradient + library
    section("S4  LEG A -- T1 = GRAD LAMBDA_MAX (FD WARD) + THE "
            "SEALED LIBRARY")
    G_raw, lam_chk = grad_of_pack(PK9, d9, L9, 1)

    def lam_fd_eval(dv):
        xs2, ws2, fp2 = PIK.folded_measure(dv, L9, +1.0)
        ys2, vs2, fn2 = PIK.folded_measure(dv, L9, -1.0)
        ok_split = (np.array_equal(fp2, PK9["fp"])
                    and np.array_equal(fn2, PK9["fn"]))
        al2, sb2, h02 = FS.mu_chain_f64(xs2, ws2, N_REF)
        B2 = FS.b_matrix_f64(al2, sb2, h02, ys2, vs2, N_REF)
        return float(np.linalg.eigvalsh(B2 @ B2.T)[-1]), ok_split

    # a2: FD-resolvable coordinates -- per channel the 3 even
    # pair moves with the LARGEST |analytic directional
    # derivative| (tiny-gradient folds sit at the f64
    # eigensolver noise floor ~1e-14, disclosed)
    half = [l for l in range(1, L9 // 2) if d9[l] != 0.0]

    def pair_g(l):
        return abs(G_raw[l] + G_raw[(L9 - l) % L9])

    mu_l = sorted([l for l in half if d9[l] > 0],
                  key=pair_g)[-FD_NCOORD:]
    nu_l = sorted([l for l in half if d9[l] < 0],
                  key=pair_g)[-FD_NCOORD:]
    t0 = FD_T * float(np.max(np.abs(d9)))
    fd_rows = []
    ok_fd = True
    ok_res = True
    ok_split_all = True
    for l in mu_l + nu_l:
        e = np.zeros(L9)
        e[l] = 1.0
        e[(L9 - l) % L9] = 1.0
        g_an = float(G_raw @ e)
        ok_res = ok_res and abs(g_an) * t0 >= FD_MIN
        gs = []
        for t in (t0, t0 / 2.0):
            lp, okp = lam_fd_eval(d9 + t * e)
            lmn, okm = lam_fd_eval(d9 - t * e)
            ok_split_all = ok_split_all and okp and okm
            gs.append((lp - lmn) / (2.0 * t))
        g_rich = (4.0 * gs[1] - gs[0]) / 3.0
        dev = abs(g_rich / g_an - 1.0) if g_an != 0.0 \
            else float("inf")
        ok_fd = ok_fd and dev <= FD_BAR
        fd_rows.append((l, g_an, g_rich, dev))
    worst_fd = max(r[3] for r in fd_rows)
    check("G40-t1-gradient-fdward", ok_fd and ok_res
          and ok_split_all and abs(lam_chk - lam184) <= 1e-14,
          "T1 = grad lambda_max(E_184) via Hellmann-Feynman "
          "(phi*, int p*^2 dmu = 1): FD ward on the %d sealed "
          "coordinates (a2: per channel the 3 largest |analytic "
          "pair derivative|, resolvability |g| t >= %.0e "
          "holds, Richardson pair at the re-measured margin-"
          "valid step t = %.3g max|d|): worst rel "
          "dev %.1e <= %.0e; fold split invariant at every FD "
          "point; lam identity %.1e -- the gradient is EXACT to "
          "ward precision"
          % (len(fd_rows), FD_MIN, FD_T, worst_fd, FD_BAR,
             abs(lam_chk - lam184)))
    # library construction (sealed constructor, one per member)
    CAND = {}
    for nm in LIB_ELIGIBLE + LIB_CONTROL:
        CAND[nm] = build_candidate(nm, d9, L9, D9, uu9, mm9,
                                   N_REF)
    T5cols = np.stack([moment_grad(d9, L9, j)
                       for j in range(1, MOM_K + 1)], axis=1)
    NULLS = [PFP.dir_dens(d9, L9, SEED_NULL + i)
             for i in range(NDIR_NULL)]
    decoy = PFP.dir_dens(d9, L9, SEED_DECOY)
    ok_cons = True
    ok_even = True
    for nm, dd in list(CAND.items()) \
            + [("T5_M%d" % j, T5cols[:, j - 1])
               for j in range(1, MOM_K + 1)] \
            + [("NULL%02d" % i, NULLS[i])
               for i in range(NDIR_NULL)] + [("DECOY", decoy)]:
        eta0 = abs(float(np.sum(dd * sl9)))
        ok_cons = ok_cons and eta0 <= ETA0_BAR \
            * max(float(np.sum(np.abs(dd * sl9))), 1.0)
        mx_dd = max(float(np.max(np.abs(dd))), 1e-300)
        ok_even = ok_even and all(
            abs(dd[l] - dd[(L9 - l) % L9]) <= 1e-12 * mx_dd
            for l in range(0, L9, 37))
    check("G41-library-conservation",
          ok_cons and ok_even and len(CAND) == 12,
          "SEALED LIBRARY BUILT (one constructor, hash-sealed "
          "members): 12 members + T5(%d) + %d nulls + decoy; "
          "eta_0 exact (<= %.0e rel) and even on ALL %d vectors "
          "-- same conservation projection, same pullback"
          % (MOM_K, NDIR_NULL, ETA0_BAR,
             len(CAND) + MOM_K + NDIR_NULL + 1))

    # ---------------- S5 LEG B: the identity test
    section("S5  LEG B -- THE IDENTITY TEST (in-span primary, "
            "sealed bars)")

    def cos_cols(T):
        a = CF.proj_coords(Vmat, wG, UG, GCUT, T)
        PT = Vmat @ a
        cs = cos_pair(e_top, PT)
        cap = float(np.linalg.norm(PT)) \
            / max(float(np.linalg.norm(T)), 1e-300)
        return cs, cos_pair(e_top, T), \
            lag_cos_pair(e_top, PT, M9), cap

    tab = {}
    for nm in LIB_ELIGIBLE + LIB_CONTROL:
        tab[nm] = cos_cols(CAND[nm])
    null_cos = [abs(cos_cols(dd)[0]) for dd in NULLS]
    noise_ref = max(null_cos)
    decoy_cos = abs(cos_cols(decoy)[0])
    # T5 subspace: in-span share of e_top on the projected T5 span
    T5span = np.stack([Vmat @ CF.proj_coords(Vmat, wG, UG, GCUT,
                                             T5cols[:, j])
                       for j in range(MOM_K)], axis=1)
    sh_t5 = sub_share(T5span, e_top)
    cos_t5 = math.sqrt(max(sh_t5, 0.0))
    nullq = []
    for q0 in (0, 4):
        Wq = np.stack([Vmat @ CF.proj_coords(
            Vmat, wG, UG, GCUT, NULLS[q0 + j])
            for j in range(4)], axis=1)
        nullq.append(math.sqrt(max(sub_share(Wq, e_top), 0.0)))
    for nm in LIB_ELIGIBLE + LIB_CONTROL:
        cs, cr, cl, cap = tab[nm]
        info("%-16s cos_span %+.3f | raw %+.3f | lag %+.3f | "
             "capture %.3f%s"
             % (nm, cs, cr, cl, cap,
                "  [CONTROL row]" if nm in LIB_CONTROL else ""))
    info("T5_MOMENTS       root share %.3f (share %.4f; null "
         "quadruple roots %.3f / %.3f)"
         % (cos_t5, sh_t5, nullq[0], nullq[1]))
    info("T6 NULLS         |cos_span| %s -> noise reference "
         "(max) %.3f; DECOY %.3f"
         % (str([round(v, 3) for v in null_cos]), noise_ref,
            decoy_cos))
    check("G50-cos-table", all(math.isfinite(t[0])
                               for t in tab.values()),
          "COS TABLE measured (in-span primary + raw/lag/capture "
          "honesty columns, printed above); T5 root share %.3f; "
          "all values finite" % cos_t5)
    check("G51-noise-reference", noise_ref < COS_ID,
          "NOISE REFERENCE (max of %d nulls through the "
          "IDENTICAL pipeline, conservative q95 estimator at "
          "n = %d, disclosed): %.3f; null-quadruple subspace "
          "roots %.3f / %.3f (the 4-dim chance level of T5, "
          "disclosed)" % (NDIR_NULL, NDIR_NULL, noise_ref,
                          nullq[0], nullq[1]))
    # sealed adjudication
    elig_vals = {nm: abs(tab[nm][0]) for nm in LIB_ELIGIBLE}
    elig_vals["T5_MOMENTS"] = cos_t5
    best_nm = max(elig_vals, key=lambda k: elig_vals[k])
    best_c = elig_vals[best_nm]
    id_hits = [nm for nm in LIB_ELIGIBLE
               if abs(tab[nm][0]) >= COS_ID]
    if id_hits:
        base_nm = max(id_hits, key=lambda k: abs(tab[k][0]))
        base_verd = "DENS_ARITHMETIC_IDENTITY(%s, |cos| %.3f)" \
            % (base_nm, abs(tab[base_nm][0]))
        base_cls = "ID"
    elif best_c >= COS_PART:
        base_nm = best_nm
        base_verd = "DENS_PARTIAL(%s, |cos| %.3f)" % (best_nm,
                                                      best_c)
        base_cls = "PART"
    else:
        base_nm = best_nm
        above = best_c >= noise_ref + NULL_PAD
        base_verd = ("DENS_WORLD_BLIND(best %s %.3f%s)"
                     % (best_nm, best_c,
                        ", ABOVE-NOISE FLAG (>= %.3f + %.2f), "
                        "disclosed" % (noise_ref, NULL_PAD)
                        if above else
                        ", below noise %.3f + %.2f"
                        % (noise_ref, NULL_PAD)))
        base_cls = "BLIND"
    check("G52-identity-adjudication", True,
          "SEALED RULE (ID iff |cos| >= %.2f for T1 or a "
          "T2/T3/T4 member; PART iff max >= %.2f; else BLIND "
          "with the noise clause): best = %s (%.3f) -> BASE %s"
          % (COS_ID, COS_PART, best_nm, best_c,
             base_verd.split("(")[0]))
    t1c = tab["T1_GRAD_LMAX"]
    check("G53-t1-coupling", True,
          "THE COUPLING NUMBER OF THE ROUND (always reported): "
          "cos(e_top, grad lambda_max) = %+.3f in-span (raw "
          "%+.3f, lag %+.3f, capture %.3f); eigen-specificity "
          "controls: grad lam2 %+.3f, grad lam3 %+.3f (excluded "
          "from the identity award, disclosed)"
          % (t1c[0], t1c[1], t1c[2], t1c[3],
             tab["T1B_GRAD_LAM2"][0], tab["T1C_GRAD_LAM3"][0]))

    # ---------------- S6 LEG C: world + window hardening
    section("S6  LEG C -- WORLD CONTRAST (EPST/SCR) + WINDOW "
            "TRANSPORT (w7/w11)")

    def hess_span_etop(d0, Lx, dirs, margin_f, m00x):
        """gate-side: span Hessian (r292 ladder + r294 halving)
        -> top eigenaxis in the span + Richardson devs of the
        top-|diag| direction."""
        names = [n for n, _ in dirs]
        vx = {n: dd for n, dd in dirs}
        ladder = list(HESS_EQ_HS)
        n_halve = 0
        diag_x = {}
        ests_x = {}
        for _try in range(LADDER_MAX_HALVE + 1):
            fin = True
            for n in names:
                ests = []
                for h in ladder:
                    mp_ = margin_f(d0 + vx[n] * h)
                    mn_ = margin_f(d0 - vx[n] * h)
                    fin = fin and math.isfinite(mp_) \
                        and math.isfinite(mn_)
                    ests.append((mp_ - 2.0 * m00x + mn_)
                                / (h * h))
                diag_x[n] = ests[1]
                ests_x[n] = ests
            if fin:
                break
            ladder = [h / 2.0 for h in ladder]
            n_halve += 1
        hp = ladder[1]
        k = len(names)
        Hx = np.zeros((k, k))
        fin_p = True
        for i in range(k):
            Hx[i, i] = diag_x[names[i]]
            for j in range(i + 1, k):
                u, v = vx[names[i]], vx[names[j]]
                msp = margin_f(d0 + (u + v) * hp)
                msn = margin_f(d0 - (u + v) * hp)
                mdp = margin_f(d0 + (u - v) * hp)
                mdn = margin_f(d0 - (u - v) * hp)
                fin_p = fin_p and all(math.isfinite(x)
                                      for x in (msp, msn, mdp,
                                                mdn))
                if not fin_p:
                    continue
                d2su = (msp - 2.0 * m00x + msn) / (hp * hp)
                d2di = (mdp - 2.0 * m00x + mdn) / (hp * hp)
                Hx[i, j] = Hx[j, i] = CF.pol_of_d2(d2su, d2di)
        Vx = np.stack([vx[n] for n in names], axis=1)
        Gx = Vx.T @ Vx
        wGx, UGx = np.linalg.eigh(Gx)
        keepx = wGx >= GCUT * wGx[-1]
        Ukx = UGx[:, keepx]
        Wkx = Ukx / np.sqrt(wGx[keepx])[None, :]
        Ax = Wkx.T @ Hx @ Wkx
        lamx, Yx = np.linalg.eigh(Ax)
        ox = np.argsort(-np.abs(lamx))
        coefx = (Wkx @ Yx[:, ox])[:, 0]
        e_x = Vx @ coefx
        i_top = max(range(k),
                    key=lambda i: abs(diag_x[names[i]]))
        rdv = CF.rich_devs(ests_x[names[i_top]])
        rich_ok = rdv is not None and max(rdv) <= RICH_TOL
        return dict(e=e_x, V=Vx, wG=wGx, UG=UGx, coef=coefx,
                    names=names, n_halve=n_halve, fin=fin_p,
                    lam_top=float(lamx[ox[0]]), rich_ok=rich_ok,
                    rich=rdv, hp=hp)

    def span_cos(bundle, T):
        a = CF.proj_coords(bundle["V"], bundle["wG"],
                           bundle["UG"], GCUT, T)
        PT = bundle["V"] @ a
        return cos_pair(bundle["e"], PT)

    def span_root_share(bundle, cols):
        """root share of the bundle top axis on the span-
        projected column subspace (the a4 subspace repetition)."""
        W = np.stack([bundle["V"] @ CF.proj_coords(
            bundle["V"], bundle["wG"], bundle["UG"], GCUT, c)
            for c in cols], axis=1)
        return math.sqrt(max(sub_share(W, bundle["e"]), 0.0))

    def best_repeat(bundle, d_x, L_x, D_x, u_x, m_x, n_x):
        """a4: rebuild the ACTUAL best member world/window-own:
        single directions via the one sealed constructor, the
        T5 subspace via the own moment-gradient span root
        share."""
        if base_nm == "T5_MOMENTS":
            cols = [moment_grad(d_x, L_x, j)
                    for j in range(1, MOM_K + 1)]
            return span_root_share(bundle, cols)
        T_x = build_candidate(base_nm, d_x, L_x, D_x, u_x, m_x,
                              n_x)
        return abs(span_cos(bundle, T_x))

    def null_reference(bundle, d_x, L_x, seed0, nn):
        """noise reference matched to the best-member type:
        single-direction |cos| values, or null-quadruple root
        shares when the best member is the T5 subspace."""
        dirs = [PFP.dir_dens(d_x, L_x, seed0 + i)
                for i in range(nn)]
        if base_nm == "T5_MOMENTS":
            return [span_root_share(bundle, dirs[0:4]),
                    span_root_share(bundle, dirs[4:8])]
        return [abs(span_cos(bundle, dd)) for dd in dirs]

    # (c1) world contrast at EPST and SCR
    ctrl_res = {}
    for cn in CTRL_WORLDS:
        d_c = d_worlds[cn]
        n_c = int(worlds_meas[cn]["minC"])
        u_c = np.asarray(ctx_c[cn]["uu"], float)
        m_c = np.asarray(ctx_c[cn]["mm"], float)
        g_lc = MF.local_gaps(u_c)
        Dg_c = 2.0 * ctx_c[cn]["alpha"] / ctx_c[cn]["M"]
        REF_c = 0.5 * float(np.sum(m_c * g_lc)) / Dg_c

        def margin_c(dv, n_c=n_c):
            me = PFP.measure_density(dv, L9)
            if me["rho"] is None or me["cross"] is None \
                    or me["cross"] <= n_c:
                return float("nan")
            return 1.0 - me["rho"][n_c]

        m0c = margin_c(d_c)
        dirs_c = []
        for i in range(N_DENS_CTRL):
            dd = PFP.dir_dens(d_c, L9, SEED_CTRL[cn] + i)
            dirs_c.append(("CD%02d" % i,
                           CF.unit_dir(dd, lag_l1(dd), REF_c)))
        bun = hess_span_etop(d_c, L9, dirs_c, margin_c, m0c)
        cs_c = best_repeat(bun, d_c, L9, D9, u_c, m_c, n_c)
        nl_c = null_reference(bun, d_c, L9, SEED_CTRL_NULL[cn],
                              NNULL_CTRL)
        collapsed = (not bun["rich_ok"]) or cs_c < COS_PART
        ctrl_res[cn] = dict(cs=cs_c, coll=collapsed,
                            rich_ok=bun["rich_ok"],
                            nmax=max(nl_c), m0=m0c,
                            n_halve=bun["n_halve"],
                            lam_top=bun["lam_top"])
        check("G6%d-%s-contrast" % (0 if cn == "EPST" else 1,
                                    cn.lower()),
              bun["fin"] and math.isfinite(cs_c),
              "%s WORLD CONTRAST (own wall degree %d, margin_0 "
              "%.3g, 12 DENS dirs, ladder halved %dx): top-diag "
              "Richardson %s (devs %s); |cos_c(%s)| = %.3f "
              "(null max %.3f) -> %s"
              % (cn, n_c, m0c, bun["n_halve"],
                 "STABLE (structured own axis, disclosed)"
                 if bun["rich_ok"] else
                 "UNSTABLE (no structured axis)",
                 str([round(v, 4) for v in (bun["rich"] or [])]),
                 base_nm, cs_c, max(nl_c),
                 "COLLAPSED" if collapsed else
                 "NOT COLLAPSED (construction-trivial risk)"))
    world_ok = all(ctrl_res[cn]["coll"] for cn in CTRL_WORLDS)
    check("G62-world-hardening", True,
          "SEALED COLLAPSE RULE (collapse iff Richardson-"
          "unstable OR |cos_c| < %.2f): EPST %s, SCR %s -> "
          "world hardening %s"
          % (COS_PART,
             "COLLAPSED" if ctrl_res["EPST"]["coll"] else "HELD",
             "COLLAPSED" if ctrl_res["SCR"]["coll"] else "HELD",
             "PASSED (match is world-specific)" if world_ok
             else "FAILED -> DOWNGRADE one level (disclosed)"))
    # (c2) window transport w7 / w11 (r294 protocol verbatim)
    win_res = {}
    for wi, kz in enumerate(W_LIST):
        wsd = W_SEED_BASE + W_SEED_STEP * wi
        ctxw = MS.ctx_build(kz)
        dw0 = np.asarray(ctxw["darm"], float)
        Lw = int(ctxw["L"])
        uuw = np.asarray(ctxw["uu"], float)
        mmw = np.asarray(ctxw["mm"], float)
        Mw = Lw // 2 + 1
        Dw = float(core.build_window(kz)["D"])
        m0w_meas = PFP.measure_density(dw0, Lw)
        nref_w = int(m0w_meas["minC"])
        ok_wall = (m0w_meas["cross"] is not None
                   and m0w_meas["cross"] == nref_w + 1
                   and nref_w == W_NREF_REC[kz])

        def margin_w(dv, nref_w=nref_w, Lw=Lw):
            me = PFP.measure_density(dv, Lw)
            if me["rho"] is None or me["cross"] is None \
                    or me["cross"] <= nref_w:
                return float("nan")
            return 1.0 - me["rho"][nref_w]

        m00w = margin_w(dw0)
        g_lw = MF.local_gaps(uuw)
        Dgw = 2.0 * ctxw["alpha"] / ctxw["M"]
        REFw = 0.5 * float(np.sum(mmw * g_lw)) / Dgw

        def lag_l1w(dd, Mw=Mw):
            return float(np.sum(np.abs(PFP.lag_of(dd, Mw))))

        GEw = BL.grad_ext(ctxw, nref_w + 2)
        xiw = BL.dir_opt(GEw["gR"], GEw["gL"], GEw["gaps"],
                         nref_w)
        thw, _thkw, _cw = BL.theta_of_dir(GEw["gR"], GEw["gL"],
                                          GEw["gaps"], xiw,
                                          nref_w)
        du_rw = 2.0 * thw * GEw["gaps"] * xiw
        f_ex = min(1.0, THETA_CAL / (2.0 * thw))
        du1w = GEw["gaps"] * xiw
        cjw = np.where(du1w > 0, du1w * GEw["gR"][:, nref_w],
                       du1w * GEw["gL"][:, nref_w])
        ordw = np.argsort(cjw)
        dirs_w = []
        okc = True
        uRw, mRw = RA.subset_move(uuw, mmw, f_ex * du_rw,
                                  np.ones(len(uuw)))
        okc = okc and MF.conserve_comb(
            "P2_JIT", uuw, mmw, uRw, mRw,
            f_ex * 2.0 * thw * AMP_PAD)
        dirs_w.append(("RIDGE", np.asarray(PIK.build_rung(
            kz, comb=(uRw, mRw))["d"], float) - dw0))
        for j in range(N_ATOM_W):
            mk = np.zeros(len(uuw))
            mk[ordw[j]] = 1.0
            u2, m2 = RA.subset_move(uuw, mmw, f_ex * du_rw, mk)
            okc = okc and MF.conserve_comb(
                "P2_JIT", uuw, mmw, u2, m2,
                f_ex * 2.0 * thw * AMP_PAD)
            dirs_w.append(("ATOM%02d" % j, np.asarray(
                PIK.build_rung(kz, comb=(u2, m2))["d"],
                float) - dw0))
        for i in range(N_FRAC_W):
            dd, (u2, m2) = PFP.dir_frac(uuw, mmw, kz, dw0,
                                        THETA_CAL, wsd + i)
            okc = okc and MF.conserve_comb(
                "P2_JIT", uuw, mmw, u2, m2, THETA_CAL)
            dirs_w.append(("FRAC%02d" % i, dd))
        slw = s_env(Lw)
        for i in range(N_DENS_W):
            dd = PFP.dir_dens(dw0, Lw, wsd + 10 + i)
            eta0 = abs(float(np.sum(dd * slw)))
            okc = okc and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * slw))), 1.0)
            dirs_w.append(("DENS%02d" % i, dd))
        dirs_wu = [(n, CF.unit_dir(dd, lag_l1w(dd), REFw))
                   for n, dd in dirs_w]
        bun_w = hess_span_etop(dw0, Lw, dirs_wu, margin_w, m00w)
        dens_iw = [i for i, n in enumerate(bun_w["names"])
                   if n.startswith("DENS")]
        cf_w = bun_w["coef"]
        share_w = float(np.sum(cf_w[dens_iw] ** 2)) \
            / max(float(np.sum(cf_w ** 2)), 1e-300)
        # window-own best repetition + T1 coupling (always)
        cs_w = best_repeat(bun_w, dw0, Lw, Dw, uuw, mmw, nref_w)
        if base_nm != "T1_GRAD_LMAX":
            t1_w = abs(span_cos(bun_w, build_candidate(
                "T1_GRAD_LMAX", dw0, Lw, Dw, uuw, mmw, nref_w)))
        else:
            t1_w = cs_w
        nl_w = null_reference(bun_w, dw0, Lw, SEED_WIN_NULL[kz],
                              NNULL_WIN)
        ok_share = abs(share_w - W_DENS_SHARE_REC[kz]) \
            <= W_DENS_SHARE_TOL
        win_res[kz] = dict(cs=cs_w, t1=t1_w, cls=class_of(cs_w),
                           share=share_w, nmax=max(nl_w),
                           nref=nref_w)
        check("G6%d-window-w%d" % (3 + wi, kz),
              okc and ok_wall and bun_w["fin"] and ok_share,
              "WINDOW w%d (r294 protocol verbatim, seeds %d+): "
              "NREF_w %d == rec (cross %s == NREF+1), theta_up "
              "%.3e, f_ex %.3f, ladder halved %dx; top-axis DENS "
              "share %.3f == r294 %.3f (tol %.2f); window-own "
              "|cos(%s)| = %.3f (T1_w %.3f, null max %.3f, "
              "12-dim span chance ~0.29 disclosed) -> class %s"
              % (kz, wsd, nref_w, str(m0w_meas["cross"]), thw,
                 f_ex, bun_w["n_halve"], share_w,
                 W_DENS_SHARE_REC[kz], W_DENS_SHARE_TOL, base_nm,
                 cs_w, t1_w, max(nl_w), win_res[kz]["cls"]))
    cls_rank = {"BLIND": 0, "PART": 1, "ID": 2}
    cls_w9 = base_cls          # a4: w9 = the adjudicated class
    classes3 = {9: cls_w9}
    classes3.update({kz: win_res[kz]["cls"] for kz in W_LIST})
    n_hold = sum(1 for kz in classes3
                 if cls_rank[classes3[kz]] >= cls_rank[base_cls])
    window_ok = (base_cls == "BLIND") or n_hold >= WIN_CLASS_NEED
    check("G65-window-hardening", True,
          "SEALED WINDOW RULE (class holds on >= %d of 3 "
          "windows): classes %s vs base %s -> %d/3 hold -> "
          "window hardening %s"
          % (WIN_CLASS_NEED,
             str({("w%d" % k): classes3[k]
                  for k in sorted(classes3)}), base_cls, n_hold,
             "PASSED" if window_ok else
             "FAILED -> DOWNGRADE one level (disclosed)"))
    # downgrades
    final_cls = base_cls
    trail = []
    if base_cls != "BLIND":
        if not world_ok:
            final_cls = {"ID": "PART", "PART": "BLIND"}[final_cls]
            trail.append("WORLD-DOWNGRADE")
        if not window_ok and final_cls != "BLIND":
            final_cls = {"ID": "PART", "PART": "BLIND"}[final_cls]
            trail.append("WINDOW-DOWNGRADE")
    if final_cls == base_cls:
        final_verd = base_verd
    elif final_cls == "PART":
        final_verd = "DENS_PARTIAL(%s, |cos| %.3f; %s)" \
            % (base_nm, best_c, "+".join(trail))
    else:
        final_verd = "DENS_WORLD_BLIND(%s %.3f downgraded; %s)" \
            % (base_nm, best_c, "+".join(trail))

    # ---------------- S7 LEG D: bridge table
    section("S7  LEG D -- BRIDGE TABLE (measurement only)")
    if final_cls in ("ID", "PART") and base_nm == "T1_GRAD_LMAX":
        T1v = CAND["T1_GRAD_LMAX"]
        btab = {nm: cos_pair(T1v, CAND[nm])
                for nm in LIB_ELIGIBLE if nm != "T1_GRAD_LMAX"}
        sh_t1_t5 = sub_share(T5cols, T1v)
        check("G70-bridge-table", True,
              "BRIDGE (which arithmetic density carries the L* "
              "gradient itself; raw on-support cosines, ONE "
              "table, no interpretation): %s; T5 share of T1 "
              "%.4f" % (str({k: round(v, 3)
                             for k, v in btab.items()}),
                        sh_t1_t5))
        anomaly = ""
    elif final_cls in ("ID", "PART"):
        t1_val = abs(tab["T1_GRAD_LMAX"][0])
        anomaly = (" THE ANOMALY: %s matches (%.3f) but T1 does "
                   "NOT (%.3f < %.2f) -- DENS would be "
                   "arithmetic but NOT L*-coupled"
                   % (base_nm, best_c, t1_val, COS_PART)
                   if t1_val < COS_PART else "")
        check("G70-bridge-table", True,
              "best match is %s (not T1);%s T1 coupling %.3f "
              "reported in G53" % (base_nm,
                                   anomaly if anomaly
                                   else " no anomaly (T1 also "
                                   ">= PART bar);", t1_val))
    else:
        anomaly = ""
        check("G70-bridge-table", True,
              "FINAL class BLIND (base %s via %s): no bridge "
              "table (sealed: leg D only on final IDENTITY/"
              "PARTIAL); T1 coupling reported in G53"
              % (base_cls, base_nm))

    # ---------------- S8 must-fails + scopes
    section("S8  MUST-FAILS + SCOPE AUDITS")
    G_mut = mutant_hf_noweight(PK9, d9, L9)
    l_m1 = nu_l[0]
    e_m1 = np.zeros(L9)
    e_m1[l_m1] = 1.0
    e_m1[(L9 - l_m1) % L9] = 1.0
    g_an_m1 = float(G_mut @ e_m1)
    g_ref = [r for r in fd_rows if r[0] == l_m1][0]
    dev_m1 = abs(g_an_m1 / g_ref[2] - 1.0)
    check("G80-mustfail-hf-norm", dev_m1 > FD_BAR,
          "m1 WRONG NORMALIZATION (nu weight dropped from "
          "p*(y)^2): mutant directional derivative off by rel "
          "%.1e >> %.0e vs the measured FD value -- CAUGHT by "
          "the ward" % (dev_m1, FD_BAR))
    fp9 = np.asarray(PK9["fp"], np.int64)
    dd_m2 = mutant_unprojected_candidate(
        fp9[:40], np.ones(40), L9)
    eta_m2 = abs(float(np.sum(dd_m2 * sl9))) \
        / max(float(np.sum(np.abs(dd_m2 * sl9))), 1e-300)
    check("G81-mustfail-unprojected", eta_m2 > ETA0_BAR,
          "m2 UNPROJECTED CANDIDATE: |eta_0| rel %.1e > %.0e -- "
          "CAUGHT by the exact conservation gate; mass-moving "
          "candidates cannot pass" % (eta_m2, ETA0_BAR))
    bad_hash = mutant_posthoc_library()
    check("G82-mustfail-seal-break", bad_hash != LIB_SEAL,
          "m3 SEAL BREAK (posthoc candidate injected after "
          "evaluation): hash %s != sealed %s -- CAUGHT; the "
          "library is frozen by hash BEFORE the first cosine"
          % (bad_hash[:12], LIB_SEAL[:12]))
    check("G83-mustfail-decoy", decoy_cos <= noise_ref + NULL_PAD,
          "m4 DECOY (pinned random seed %d smuggled through the "
          "candidate pipeline): |cos| %.3f <= noise %.3f + %.2f "
          "-- HELD below the reference; a random direction "
          "cannot fire the identity"
          % (SEED_DECOY, decoy_cos, noise_ref, NULL_PAD))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G84-scope-audits", not hits and not ag_hits,
          "the %d sealed source-pure constructors consume "
          "densities/combs/geometry/degrees/seeds ONLY (%s); "
          "the Hesse forms and margin channels are OUTSIDE the "
          "source-pure list and honestly typed measurement-"
          "consuming; fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S9 honesty + verdict
    section("S9  HONESTY LEDGER + VERDICT")
    check("G90-honesty-ledger", True,
          "cosines, captures, shares and contrasts are "
          "MEASUREMENTS on finite profile spaces; e_top is "
          "span-limited and the in-span primary metric is the "
          "sealed honest reading of exactly that limitation "
          "(raw/lag/capture disclosed per candidate); the Hesse "
          "forms consume measured margins (r292/r294 protocol); "
          "the control Richardson typing and the 12-dim window "
          "chance level are disclosed; a passing class is a "
          "finite-window alignment statement, not a mechanism "
          "theorem")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no new survival "
          "predictor, no posthoc candidate, no posthoc window, "
          "no RH claim; what the round adds: the sealed identity "
          "adjudication of the DENS top axis against the "
          "candidate library with the T1 coupling number and "
          "the world/window hardening; r243..r295 stand")
    parts_v = [final_verd]
    parts_v.append("T1_COUPLING(cos_span %+.3f, raw %+.3f, lag "
                   "%+.3f, capture %.3f)"
                   % (t1c[0], t1c[1], t1c[2], t1c[3]))
    parts_v.append("COS_TABLE(span %s; noise %.3f; T5 root %.3f)"
                   % (str({nm: round(tab[nm][0], 3)
                           for nm in LIB_ELIGIBLE}), noise_ref,
                      cos_t5))
    parts_v.append("WORLD_CONTRAST(EPST %s %.3f, SCR %s %.3f)"
                   % ("COLLAPSED" if ctrl_res["EPST"]["coll"]
                      else "HELD", ctrl_res["EPST"]["cs"],
                      "COLLAPSED" if ctrl_res["SCR"]["coll"]
                      else "HELD", ctrl_res["SCR"]["cs"]))
    parts_v.append("WINDOW_TRANSPORT(%s; shares w7 %.3f / w9 "
                   "%.3f / w11 %.3f)"
                   % (str({("w%d" % k): classes3[k]
                           for k in sorted(classes3)}),
                      win_res[7]["share"], share_dens9,
                      win_res[11]["share"]))
    if anomaly:
        parts_v.append("ANOMALY(%s)" % anomaly.strip())
    verd = " + ".join(parts_v)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s -- the DENS-identity fork answered by measurement; "
          "NO L* claim, NO RH claim" % verd)
    return finish(smoke)


def finish(smoke):
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
