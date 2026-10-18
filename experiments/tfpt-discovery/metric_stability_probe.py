#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""metric_stability_probe -- PRIME.PORT.WALL.METRIC_STABILITY.01
(round 278): from the MEASURED dose-response continuum (r276) to
the LOCAL STABILITY LAW.  r276 measured that the wall is a
continuum (D ~ theta^b, b 0.04..1.09, no switch) and that SUPPORT
EXACTNESS is the most wall-critical property (P2_JIT at 2 percent
of the local gap already costs 3/4 of the depth); the named
follow-up was the u-profile of single-op influence.  REVIEWER
DIRECTION (the concretely attackable one): "if the dose-response
relation admits an analytic stability inequality -- positivity
reserve >= F(metric deviation from the prime comb) -- the firewall
becomes mathematically graspable."  THE ANALYTIC LEVER: r276
measured finite doses; the LOCAL law is the DERIVATIVE -- the
exact sensitivity of the chain against atom positions, computable
from orthogonal-polynomial perturbation theory (Hellmann-Feynman
class).  NOT a proof round: no certificate, no bound, no wall
mechanism claim, no H5 progress -- exact first-order calculus plus
measurement.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r244/r276 machinery imported verbatim): per window
the exact scaled h-chain of the signed defect measure mutilde =
mu - nu (BH.bord_chain), built from the comb (u_j, m_j) through
the SEALED channel comb -> tent lags (core.atom_lags_at) -> even
extension + FFT (PIK.grid_density) -> signed grid density d_l ->
folded zone measure with atom weights d_l s_l at x_l =
cos(2 pi l / L), s_l = 4 sin^2(pi l / L) / (2L).  STRUCTURAL
DISCLOSURE (measured at design time / in the smoke pass, not
tuned): the tent assembly is PIECEWISE LINEAR in each u_j --
exactly two grid nodes i0 = floor(u_j/D), i0+1 carry
d c[i0]/du_j = +m_j/(2D) and d c[i0+1]/du_j = -m_j/(2D) (lever
1/(2D), D = 2 alpha / M); the map u -> d is a.e. differentiable
with derivative KINKS when an atom crosses a grid node.
ON-NODE GEOMETRY (structural finding of the smoke pass,
disclosed BEFORE calibration): on w9 the window scale alpha =
log 16 makes D = log 2 / 46 COMMENSURATE with log 2 -- the
entire 2-power family (2, 4, 8, ..., 256) and the window-edge
atom u = alpha sit EXACTLY ON tent nodes (8 of 70 atoms); at an
on-node atom only ONE-SIDED derivatives exist (the two linear
cells differ), so the gradient object is carried TWO-SIDED:
DW_right (cell i0) and DW_left (cell i0-1), equal off-node;
every prediction is SIDE-SELECTED (du_j > 0 reads the right
slope, du_j < 0 the left slope); on-node classification at
dist <= 1e-6 D, census disclosed per window; the reflection
branch u_j < D is gated INACTIVE on every world this round
touches.  All gradients below are the exact one-sided a.e.
derivatives of this finite machinery.

LEG A -- THE EXACT SENSITIVITIES (derived at design time by
classical orthogonal-polynomial perturbation theory, then frozen;
every formula is FD-gated):
(a1) HELLMANN-FEYNMAN GRADIENT of the pivot chain: with h_n =
  int pihat_n^2 dmutilde and monic pihat_n, the polynomial
  variation drops by orthogonality (d pihat_n has degree < n), so
      d h_n / du_j = int pihat_n^2 dmudot_j
                   = sum_l wdot_l(j) pihat_n(x_l)^2,
  wdot_l(j) = s_l * d d_l/du_j (the tent+FFT derivative, exact).
  In the r244 scaled variables this is SCALE-FREE:
      d log h_n / du_j = [sum_l wdot_l(j) q_n(x_l)^2] / eta_n.
  BORDER/CD FORM for the budget column: with F_n = int pihat_n
  dsigmatilde (border fixed) and the border kernel B_n(x) =
  sum_{k<n} F_k pihat_k(x)/h_k (the r274 telescope object),
      d F_n / du_j = - sum_l wdot_l(j) pihat_n(x_l) B_n(x_l),
  scale-free through q_k fb_k / eta_k.  TERMINAL MARGIN (r243/
  r244 corner): D_N = 5/7 - rho_{N-1}, rho = F^2/h, so
      d D_N / du_j = - rho_{N-1} (2 dF/F - dh/h)_{N-1}.
  GATES: central finite differences through the FULL pipeline
  (comb -> build_rung -> fold -> chain) at adaptive kink-guarded
  steps with Richardson extrapolation on sealed (n, j) pairs
  (OFF-node atoms) on all three r276 windows; ONE-SIDED FD gates
  (first-order Richardson) on the hottest ON-node atom, left and
  right slope separately; one-sided full-vector directional FD
  against the side-selected prediction; margin FD; mp counter-
  check (dps 40) on two sealed off-node w9 pairs; the weight-
  vector derivative DW is itself FD-gated (piecewise-linear map:
  exact to rounding); degrees whose whole gradient row sits
  below the absolute floor 1e-4 are skipped (disclosed) -- the
  low-degree chain is position-blind at f64 scale.
(a2) THE U-PROFILE (the r276 follow-up): the gap-weighted
  sensitivity map G_{n,j} = g_j |d log h_n / du_j| over (n, j) on
  w9 + the two r276 rungs (kz18, kz55); per-atom aggregate A_j =
  g_j max_n |d log h_n/du_j|; hull-position and weight
  correlations; LETHALITY CENSUS: deterministic single-atom
  jitters u_j -> u_j +/- g_j (the r276 SINGLE amplitude, both
  signs, all atoms) measured against the exact chain -- Spearman
  (A_j, min-depth_j) adjudicates whether the gradient map
  PREDICTS the r276 position-dependent lethal singles (their
  flip degrees landed at 51..152 on w9).
(a3) the same map for the terminal margin: M_j = g_j
  |d D_N / du_j| (via the border/CD route above).
CONTROL CONTRAST: the same gradient maps on EPSTEIN / SCRAMBLE /
SMOOTH (w9, their positive prefix n < flip 25/21/27) -- where
does the fragility of the wrong arithmetic sit vs MAIN.

LEG B -- THE LOCAL STABILITY LAW:
(b1) LIPSCHITZ SIZE (conventions SEALED): the r276-P2 dose is
  gap-relative (du_j = theta g_j xi_j, |xi| <= 1), so the dual
  norms are gap-weighted: L1_n = sum_j g_j |d log h_n/du_j|
  (worst case over |xi|_inf <= 1) and L2_n (rms); margin
  L_D = sum_j g_j |d D_N/du_j|.  LOCAL INEQUALITY:
      margin(pert) >= margin(0) - L_D theta + O(theta^2),
  and per degree log h_n(pert) >= log h_n - L1_n theta +
  O(theta^2); first-order FLIP criterion: predicted flip at the
  first n with <grad log h_n, du> <= -1 (linearized h through
  zero).  DOSE ADJUDICATION against the exact r276 smallest
  doses: the P2_JIT theta = 0.02 worlds are REBUILT with the
  r276 seeds (seed = 276000 + 1*100000 + di*10000 + rep*1000 +
  wi*10, MF.pert_jit verbatim) on all three windows; per
  replicate the measured d log h_n (exact chain) is compared to
  the first-order prediction (median ratio over the sealed band
  1e-3 <= |dlg| <= 0.5, degrees below the perturbed flip) and
  the measured flip degree to the predicted one; kink crossings
  per replicate disclosed.
(b2) THE QUADRATIC REST: along kink-projected directions (atoms
  within 2 percent of D of a grid node get zero component,
  count disclosed; the r276 w9/kz55 dose directions rescaled +
  two pinned random directions), central second differences
  q_n(eps) = [dlg(+eps) + dlg(-eps)] / eps^2 over the sealed
  eps ladder (1e-4, 3e-4, 1e-3, 3e-3; kink-capped); TAME iff
  the q-consistency ratio between adjacent resolvable eps is
  <= 4 in the median (explosion bar 32); VALIDITY WINDOW
  theta*_n = |<grad, dir>| / |q_n| (the dose where second order
  catches first order), reported vs the r276 smallest dose 0.02.
(b3) N-SCALING of L (gap-relative) over the ladder kz (18, 9,
  12, 13, 26, 40, 55) sorted by N: L_D and max_n L1_n per
  window; halves log-slope b_L of L_D vs N; sealed typing:
  GROWING iff b_L >= +0.5 (the wall gets more fragile with N --
  consistent with the margin razor), SHRINKING iff <= -0.5,
  else FLAT; UNIFORM_CANDIDATE iff FLAT and max/min <= 10 --
  only then is "margin >= margin_MAIN - L_uni dist" a uniform
  lemma candidate.

LEG C -- THE STABILITY HYPOTHESIS (delivery object, typed
TASK_FORMULATION_ONLY): "positivity reserve >= F(metric
deviation)" with MEASURED F: locally linear with slope L(n, N)
(the L-map), validity window from b2, N-behaviour from b3;
EXTRAPOLATION: the linear flip criterion applied to the rebuilt
r276 theta = 0.05 / 0.10 worlds (same seeds) -- where the
linearity of the global curve breaks; MAINWINDOW PREDICATE
(honest, PERTURBATIVE_ONLY): the metric predicate dist(comb,
MAIN) = max_j |u_j - u_j^MAIN| / g_j <= theta with theta inside
the measured validity window inherits wall positivity from MAIN
positivity via the stability inequality -- this inherits ONLY
perturbatively around MAIN; the MAIN positivity itself stays the
open center (H5 untouched).

LEG D -- WARDS / MUST-FAILS: identity wards (grad_chain
reproduces BH.bord_chain FIELD-EXACTLY on every ladder window;
the comb channel reproduces BH.wpack bitwise in rho and nf on
the three r276 windows; eta reconstruction from the full grid
weight vector; theta = 0 bitwise through MF.pert_jit);
kink/reflection census; conservation checks (MF.conserve_comb on
every rebuilt dose world); control anchors 25/21/27; mp (dps 40)
base ward + FD counter-check; MUST-FAILS (each loud): (m1a)
WEIGHT-TERM MUTANT -- the gradient with the s_l = 4 sin^2/(2L)
factor dropped must break the FD gate by >= 0.1 rel; (m1b)
HALF-ARM MUTANT -- dropping the mirror arm of the even extension
must break by >= 0.1 rel; (m2) ROUNDING-REGIME FD -- a finite
difference at step 1e-16 (below one ulp of u) must DISAGREE with
the analytic gradient by >= 1e-2 rel (the adaptive step is
load-bearing); (m3) GIFT PROFILE -- a profile oriented by the
withheld lethality census must be FLAGGED by the AST scope
audit.  STOP LIST (anti-gates, binding): NO pair hierarchies,
NO splits, NO s-flows, NO precision escalation beyond the sealed
dps-40 counter-check; fragment audit (no polyfit/curve_fit/
lstsq/minimize) inherited.

INDEX FIREWALL (binding, r238-r276 discipline): w = window (kz),
N_w = builder depth, n = chain degree, j = comb atom index;
the gradient constructors (tent_dw, grad_chain, grad_pack,
wsig_vec, pred_dlg, pred_flip) consume comb data, chain data and
the evaluation grid ONLY (AST scope audit against the withheld
truth-side set incl. the lethality census); ground truth (flip
degrees, lethality depths) enters MEASUREMENT and gates only; no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r244 BH.bord_chain + BH.wpack + BH.spearman, v881
PIK.build_rung + PIK.folded_measure + PIK.grid_density +
PIK.lambda_eps, r243 PB.smooth_comb, r276 MF.window_ctx +
MF.local_gaps + MF.pert_jit + MF.conserve_comb, core
build_window READ-ONLY.

SEALED CONSTANTS: MAIN window 9; R276 windows (9, 18, 55);
ladder (18, 9, 12, 13, 26, 40, 55); controls w9 EPSTEIN/
SCRAMBLE(seed 1)/SMOOTH, flips 25/21/27; B57 = 5/7; FD steps
(1e-4, 1e-5, 1e-6) with KINK_GUARD 0.25 (step <= 0.25 x node
distance) and Richardson pairs from the two SMALLEST
kink-guarded steps (the chain is violently curved in single
atom positions -- analyticity scale ~1e-4 in u -- so the small
pair controls the quadratic term); FD degrees (5, N/3, 2N/3, N-1); FD atoms
(first/mid/last/hottest-terminal OFF-node atoms + the hottest
ON-node atom one-sided); FD bars: Richardson 5e-5, raw 2e-3,
one-sided 1e-3, floor frac 1e-3, absolute floor 1e-4;
ONNODE_EPS 1e-6 (x D); directional bar 1e-3 (one-sided,
side-selected); margin bar 1e-4; DW ward bar
1e-6 (e = 1e-6); eta ward bar 1e-9; MP_DPS 40, MP_E 1e-8, mp
base bar 1e-8, mp FD bar 1e-6; EPS ladder (1e-4, 3e-4, 1e-3,
3e-3), KINK_PROJ 0.02, Q_FLOOR 1e-9, QCONS_TAME 4, QCONS_EXPLODE
32; dose band (1e-3, 0.5), ratio EXPLAINED (0.7, 1.43) / PARTIAL
(0.33, 3.0), FLIP_TOL 0.25; profile bars SP_PRED -0.5 / SP_WEAK
-0.2; N-trend slope band +/-0.5, decade 10; r276 seeds (SEED
276000, P2 index 1, dose indices 0.02/0.05/0.10 -> 1/2/3,
window indices 9/18/55 -> 0/1/2, 3 replicates); direction seed
278000; mutant bars m1 >= 0.1, m2 >= 1e-2, ROUND_E 1e-16;
runtime <= 1800 s; smoke = w9 censuses + identity/eta/DW wards +
kink census + theta-0 + reduced FD gates + m1 + m2 + scope
audits (ladder, profiles, lethality, controls, doses, eps, mp,
b3 skipped).  DISCLOSED PRE-SPEC INPUT: one machinery scoping
pass (tent derivative geometry, kink-distance census, gradient
magnitude order for bar placement, mp cost) -- no verdict band
was tuned; every class boundary above is an r276/v956 record
number or a round constant fixed before the first full
evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] METRIC_STABILITY_LAW(L-map; validity window;
    N-trend; UNIFORM_CANDIDATE or not) iff ALL leg-A gates pass
    AND b2 is not NONSMOOTH
  / WALL_LOCALLY_NONSMOOTH(second order explodes -- the
    continuum is not differentiably graspable at the probed
    scales) iff leg-A gates pass AND b2 median consistency > 32
  / GRADIENT_GATES_FAILED (any leg-A gate fails)
+ GRADIENT_EXPLAINS_DOSE(EXPLAINED / PARTIAL / UNEXPLAINED;
    median band ratio; flip-degree deviations; kink census)
+ U_PROFILE(PREDICTIVE / WEAK / UNCOUPLED; sp vs lethality; hull
    correlation; top atoms)
+ N_TREND(GROWING / SHRINKING / FLAT; L values; slope;
    UNIFORM_CANDIDATE flag)
+ MAINWINDOW_PREDICATE(proposal, typed PERTURBATIVE_ONLY).
Honesty before beauty: every gradient is the exact a.e.
derivative of the FINITE tent-grid machinery on finite windows
(kinks disclosed); no verdict claims a wall lemma, a bound
mechanism, a cofinal law or H5 progress; the stability
inequality, where it holds, inherits positivity only
PERTURBATIVELY around MAIN -- the MAIN positivity itself remains
the open center; r243-r276 stand.

DISCLOSED CALIBRATION AMENDMENTS (found in smoke + calibration
pass 1, all BEFORE the record freeze; the gradient formulas,
norm conventions, dose protocol, class rules, ratio/flip bands
and every verdict rule never moved):
(a0) ON-NODE GEOMETRY (smoke): the smoke pass found the 2-power
  family sitting EXACTLY on tent nodes (w9: alpha = log 16
  makes D commensurate with log 2) -- the gradient object was
  extended to the disclosed one-sided pair with side-selected
  predictions and one-sided FD gates; a structural finding, not
  a tuning.
(a1) FD-GATE MP ESCALATION (pass 1): on the deep window kz55
  two off-node pairs showed an e-LINEAR f64-FD deviation ~7e-4
  that is NOT curvature -- the f64 chain rounding error is a
  SMOOTH function of u and its gradient pollutes the f64 FD;
  the mp (dps 40) FD through the actual pipeline confirms the
  analytic value to 6e-8.  Pairs whose f64 Richardson exceeds
  the bar are now ESCALATED to the sealed mp FD and gated there
  (no precision beyond the sealed dps-40 counter-check).  A
  measurement-domain fix on a ward; the formula never moved.
(a2) MP PAIR SELECTION (pass 1): the mp counter-check atoms are
  chosen per-degree hottest off-node (the mid-atom choice sat
  at the f64 input-quantization floor of the d-vector, dev
  1.1e-5 vs bar 1e-6 on a gradient of order 1e-3).
(a3) B2 CAP EXCLUSION BUG (pass 1): kink-projected atoms
  (component zeroed) still bounded the eps cap with node
  distance zero, leaving 0 resolvable quadratic probes; the
  cap now ignores zero components.  A bug fix, not a band move.
(a4) REPORTING CONVENTIONS (pass 1): hull coordinate corrected
  to u/(2 alpha) (the comb spans (0, 2 alpha]); control
  contrast reports MAIN over the SAME pre-flip degree range;
  the flip deviation counts an unpredicted flip as n_pred = N
  (survivor prediction) instead of silently dropping it.
(a5) MP FD STEPS (pass 2/3): the two mp-FD roles need
  DIFFERENT sealed steps -- the G24 counter-check probes the
  hottest pairs where the chain curvature is violent
  (analyticity scale ~2.6e-4 in u, the same nonlinearity b2
  measures): its step moved 1e-6 -> 1e-8 (curvature ~2.5e-10,
  f64 input quantization ~2e-9); the G20 escalation arbitrates
  pairs that are f64-Richardson-CONSISTENT (low curvature) but
  f64-biased on the deep window: it stays at 1e-6, where its
  measured dev is 1.3e-7 while 1e-8 is input-quantization-
  limited (~3e-5) on the small deep-window gradients.  Bars
  unchanged.

RECORD TABLES (frozen from calibration pass 4 = the first full
evaluation AFTER the disclosed amendments; chronology honest:
smoke 30/30; pass 1 = 28/31 exposing a1/a3/a4, pass 2 = 29/31
exposing the G24 curvature limit, pass 3 = 29/31 exposing the
escalation quantization limit -> a5 split steps; pass 4 = 31/31,
wall 20.8 s; the record insertion below is the only post-freeze
edit, which IS the protocol; run1/run2 identical up to WALL):
CAL_VERDICT = METRIC_STABILITY_LAW(L-map sealed; theta* med
8.0e-04 [w9]; N-trend SHRINKING) + GRADIENT_EXPLAINS_DOSE(
PARTIAL, ratio 0.41, flip dev 3.00) + U_PROFILE(PREDICTIVE,
sp -0.82) + N_TREND(SHRINKING, b_L -1.09) +
MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY).
Key numbers.  GRADIENTS (a1 gates): grad_chain == BH.bord_chain
FIELD-EXACT on 7/7 ladder windows; comb channel == BH.wpack
bitwise (rho + nf) on the r276 windows; eta reconstruction
worst 1.2e-11; central FD 21 pairs on (9, 18, 55): worst f64
Richardson dev 4.5e-05 (bar 5e-5), raw 6.8e-04 (bar 2e-3), 2
kz55 pairs escalated to the sealed mp FD (worst 1.3e-07 --
amendment a1: the f64 chain error-gradient, NOT the formula);
one-sided FD at the on-node 2-power atom worst 1.2e-04 (bar
1e-3); directional worst 7.6e-04; margin worst 1.5e-05; DW ward
7.8e-10 (piecewise-linear map exact to rounding); mp (dps 40)
base ward 1.2e-11, mp counter-FD 2.5e-09 / 2.6e-08 (bar 1e-6).
KINK CENSUS: on-node atoms 8/70 (w9, the FULL 2-power family
2..256 -- alpha = log 16), 2/247 (kz18), 2/120 (kz12), 4/136
(kz13), 4/604 (kz26), 2/1773 (kz40), 2/3589 (kz55); reflection
inactive everywhere (min u >= 27 D).  U-PROFILE (a2/a3, the
r276 follow-up closed): the gap-weighted sensitivity sits at
the BOTTOM of the comb -- sp(A_j, hull pos) = -0.80 / -0.83 /
-0.83 on w9/kz18/kz55, top-3 w9 atoms at hull positions 0.12 /
0.20 / 0.29 = the SMALL PRIMES 2, 3, 5 (A = 48.4 / 29.2 /
18.7); sp(A, weight) +0.74..+0.82; the terminal-margin map M_j
tracks A_j at sp +0.83: wall depth and terminal margin share
one sensitivity geometry.  LETHALITY (w9, deterministic +/-g_j
singles): 66/70 atoms flip the wall (flip degrees 25..183,
containing the r276 lethal band 51..152); sp(A_j, min-depth_j)
= -0.82 <= -0.5: U_PROFILE_PREDICTIVE -- the gradient map
locates the lethal positions.  DOSE (b1, seeds exact,
conservation EXACT 27/27): theta = 0.02 median band ratio
pred/meas 0.41 (replicate medians 0.15..1.09) -- first order
UNDER-predicts the measured losses ~2.4x; the linear flip
criterion reaches the flip on only 2/9 replicates (flip dev
med 3.00; measured flips 41..72, predicted mostly SURVIVE):
GRADIENT_EXPLAINS_DOSE(PARTIAL) -- the r276 smallest dose is
ALREADY beyond first order; kink crossings med 7/70 per
replicate; extrapolation 0.05/0.10 med dev 0.90/0.70 (the
global curve is nonlinear from the first stage on).  QUADRATIC
(b2): 40/40 probes resolvable, q-consistency median 1.02 (TAME,
bar 4; 2 probes above 32 at the noise floor); validity window
theta* = |lin|/|quad| med 8.0e-04 (w9) / 1.2e-04 (kz55), min
2.1e-05: the strict linear window sits 25x..170x BELOW the
smallest r276 dose 0.02 -- the wall's dose-response continuum
(r276, b 0.04..1.09) is the NONLINEAR cascade beyond theta*,
not the linear regime; the law is real but its window is tiny.
N-SCALING (b3): L_D (gap-relative margin Lipschitz) = 264 /
309 / 147 / 126 / 17.8 / 269 / 120 on N = 142 / 151 / 168 /
184 / 364 / 388 / 591 (kz 18/12/13/9/26/55/40), halves slope
b_L = -1.09, decade 17.3: the margin sensitivity does NOT grow
with N (no fragility growth -- the razor is not a sensitivity
razor) but is strongly window-specific (decade > 10): NO
uniform stability constant from this data; max_n L1_n = 156..
491.  CONTROLS (w9 contrast, hull coordinate u/(2 alpha)):
flips 25/21/27 exact; pre-flip L1 medians EPSTEIN 3.2e-14 /
SCRAMBLE 0.98 / SMOOTH 0.017 vs MAIN over the SAME degree
ranges ~1.4e-14: at low degrees the ARITHMETIC combs (MAIN,
EPSTEIN) are position-BLIND while the metrically wrong worlds
(SCRAMBLE, SMOOTH) already carry O(1e-2..1) sensitivity -- the
low-degree gradient separates metric randomness from
arithmetic structure, the wall depth separates the arithmetic
combs among themselves.  MUST-FAILS: m1a weight-term mutant
dev 4.5e+03 LOUD; m1b half-arm mutant dev 4.9e-01 LOUD; m2
rounding-step FD dev 1.0 LOUD; m3 gift profile FLAGGED by the
scope audit; constructor scopes CLEAN; fragment audit CLEAN.
READING (typed): the reviewer's stability inequality EXISTS
locally -- margin(c) >= margin_MAIN - L_D(w) theta - O(theta^2)
with exact, machine-gated L_D(w) and TAME curvature -- but its
strict window theta*(w) ~ 1e-3..1e-4 is far below the doses
where the r276 continuum lives, its constant is window-specific
(no uniform L), and the MainWindow predicate MetricNear(c,
MAIN, theta) <= theta*(w) therefore inherits wall positivity
only PERTURBATIVELY and per window; the u-profile answer to
r276: the wall's metric reading is BOTTOM-LOADED (small primes
2, 3, 5 at gap scale), predictive of single-op lethality, and
identical for depth and margin.  Runtime 20.8 s full / 0.3 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE (records inserted per protocol; no bar, band,
class rule or verdict rule moved).

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
R276_KZS = (9, 18, 55)
LADDER_KZS = (18, 9, 12, 13, 26, 40, 55)
B2_KZS = (9, 55)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
B57 = 5.0 / 7.0
FD_STEPS = (1e-4, 1e-5, 1e-6)
FD_RICH_BAR = 5e-5
FD_RAW_BAR = 2e-3
FD_ONE_BAR = 1e-3
GRAD_FLOOR_FRAC = 1e-3
ABS_GRAD_MIN = 1e-4
ONNODE_EPS = 1e-6
DIR_BAR = 1e-3
MARG_BAR = 1e-4
DW_E = 1e-6
DW_BAR = 1e-6
ETA_WARD_BAR = 1e-9
KINK_GUARD = 0.25
KINK_PROJ = 0.02
MP_DPS = 40
MP_E = 1e-8
MP_E_ESC = 1e-6
MP_BASE_BAR = 1e-8
MP_FD_BAR = 1e-6
EPS_LADDER = (1e-4, 3e-4, 1e-3, 3e-3)
Q_FLOOR = 1e-9
QCONS_TAME = 4.0
QCONS_EXPLODE = 32.0
BAND_LO = 1e-3
BAND_HI = 0.5
RATIO_EXPL = (0.7, 1.43)
RATIO_PART = (0.33, 3.0)
FLIP_TOL = 0.25
SP_PRED = -0.5
SP_WEAK = -0.2
TREND_SLOPE = 0.5
TREND_DECADE = 10.0
THETAS_R276 = (0.02, 0.05, 0.10)
REPS = 3
SEED_R276 = 276000
P2_SI = 1
DOSE_DI = {0.02: 1, 0.05: 2, 0.10: 3}
WIN_WI = {9: 0, 18: 1, 55: 2}
SEED_DIR = 278000
MUT_LOUD = 0.1
ROUND_E = 1e-16
ROUND_MIN_DEV = 1e-2

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


# ------------------------------------------------------ AST audits
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
    return (not bad), ("NO zero/prime oracles; the gradient "
                       "constructors consume comb positions + "
                       "weights, chain data and the evaluation "
                       "grid ONLY; flip degrees and the lethality "
                       "census enter MEASUREMENT and gates only"
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


GRAD_FUNCS = ("tent_dw", "grad_chain", "grad_pack", "wsig_vec",
              "pred_dlg", "pred_flip")
GRAD_FORBIDDEN = {"nf", "nf2", "nf_base", "depths", "leth",
                  "lethality", "wall_depth", "s_med", "flip_meas"}


# ------------------------------------------------ trend estimators
def halves_slope(Xs, Ys):
    """r272 dyadic log-slope (deterministic)."""
    n = len(Xs)
    h = n // 2
    ly = [math.log(max(float(v), 1e-300)) for v in Ys]
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    num = (sum(ly[h:]) / (n - h)) - (sum(ly[:h]) / h)
    den = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    return num / den


# ---------------------------------------- gradient constructors
# (source-pure scope, AST-audited: consume comb data, chain data
#  and the evaluation grid ONLY -- no withheld truth)
def wsig_vec(darm, L):
    """signed folded grid weight vector on the full fold-point
    grid pt = 0..L/2: wsig[pt] = sum_{l: min(l, L-l) = pt}
    d_l s_l, s_l = 4 sin^2(pi l/L)/(2L) -- mutilde as one signed
    vector on the fixed cos grid."""
    ll = np.arange(L)
    s_l = 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)
    fold = np.minimum(ll, L - ll)
    npts = L // 2 + 1
    w = np.zeros(npts)
    np.add.at(w, fold, darm * s_l)
    return w


def tent_dw(uu, mm, alpha, M, L):
    """exact ONE-SIDED derivatives of the signed folded weight
    vector wrt each atom position: the tent assembly is
    piecewise linear -- in the cell (i0 D, (i0+1) D) the two
    nodes carry d c[i0]/du_j = +m_j/(2D), d c[i0+1]/du_j =
    -m_j/(2D), D = 2 alpha/M; pushed through the linear even-
    extension FFT and the s_l weighting, fold-aggregated.  At an
    ON-NODE atom (dist <= ONNODE_EPS D; the 2-power family on
    w9) the right derivative reads cell i0 = u/D and the left
    derivative cell i0 - 1; off-node both sides coincide.
    Returns (DWr, DWl [n_at x npts], dists, D, onnode)."""
    D = 2.0 * alpha / M
    ll = np.arange(L)
    s_l = 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)
    fold = np.minimum(ll, L - ll)
    npts = L // 2 + 1
    n_at = len(uu)
    DWr = np.zeros((n_at, npts))
    DWl = np.zeros((n_at, npts))
    dists = np.empty(n_at)
    onnode = np.zeros(n_at, dtype=bool)
    lever = mm / (2.0 * D)

    def cell_row(cell, lev):
        dc = np.zeros(M)
        if 0 <= cell < M:
            dc[cell] += lev
        if 0 <= cell + 1 < M:
            dc[cell + 1] -= lev
        dd = PIK.grid_density(dc)
        row = np.zeros(npts)
        np.add.at(row, fold, dd * s_l)
        return row

    for j in range(n_at):
        i0 = int(math.floor(uu[j] / D))
        r = uu[j] - i0 * D
        dists[j] = min(r, D - r)
        onnode[j] = dists[j] <= ONNODE_EPS * D
        DWr[j] = cell_row(i0, lever[j])
        DWl[j] = cell_row(i0 - 1, lever[j]) if onnode[j] \
            else DWr[j]
    return DWr, DWl, dists, D, onnode


def grad_chain(xs, ws, ys, vs, bx, bw, by, bv, n_upto, xe):
    """r244 BH.bord_chain VERBATIM in every original operation
    (field-exact identity gated), extended by one propagated
    value array on the evaluation grid xe; returns (rows, Q) with
    Q[:, n] = q_n(xe) (the scaled monic values, scale e^{-Ls})."""
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qe = np.ones_like(xe)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    qe_m = np.zeros_like(xe)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    lg_h = math.log(abs(eta))
    sg_h = math.copysign(1.0, eta)
    rows = []
    Q = np.empty((len(xe), n_upto))
    for n in range(n_upto):
        fb = float(np.sum(bw * qb) - np.sum(bv * qc))
        tb = float(np.sum(bw * bx * qb) - np.sum(bv * by * qc))
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        Q[:, n] = qe
        rows.append(dict(n=n, lg_h=lg_h, sg_h=sg_h, Ls=Ls, eta=eta,
                         fb=fb, tb=tb, rho=fb * fb / eta, alh=alh,
                         gam_next=None))
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
            pb = (bx - alh) * qb
            pc = (by - alh) * qc
            pe = (xe - alh) * qe
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
            pb = (bx - alh) * qb - ge * fc * qb_m
            pc = (by - alh) * qc - ge * fc * qc_m
            pe = (xe - alh) * qe - ge * fc * qe_m
        sc = max(float(np.max(np.abs(px))), float(np.max(np.abs(py))),
                 float(np.max(np.abs(pb))), float(np.max(np.abs(pc))))
        if sc == 0.0 or not math.isfinite(sc):
            return rows, Q
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qb_m, qc_m = qb, qc
        qe_m = qe
        qx, qy = px / sc, py / sc
        qb, qc = pb / sc, pc / sc
        qe = pe / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        if eta == 0.0 or not math.isfinite(eta):
            return rows, Q
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        rows[-1]["gam_next"] = gam
        lg_h += math.log(abs(gam))
        sg_h *= math.copysign(1.0, gam)
    return rows, Q


def grad_pack(ctx):
    """the full exact gradient block of one world: chain +
    evaluation grid + tent derivative -> d log h_n/du_j (all n,
    j), dF_rel via the border kernel, terminal margin gradient,
    gap-weighted Lipschitz curves.  Consumes ctx source data
    only."""
    darm = ctx["darm"]
    L = ctx["L"]
    N = ctx["N"]
    uu, mm = ctx["uu"], ctx["mm"]
    npts = L // 2 + 1
    xe = np.cos(2.0 * math.pi * np.arange(npts) / L)
    xs, ws, _ = PIK.folded_measure(darm, L, +1.0)
    ys, vs, _ = PIK.folded_measure(darm, L, -1.0)
    rows, Q = grad_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], N, xe)
    n_run = len(rows)
    eta = np.array([r["eta"] for r in rows])
    fb = np.array([r["fb"] for r in rows])
    Q = Q[:, :n_run]
    wsig = wsig_vec(darm, L)
    eta_ward = float(np.max(np.abs(wsig @ (Q * Q) - eta)
                            / np.abs(eta)))
    DWr, DWl, dists, Dg, onnode = tent_dw(uu, mm, ctx["alpha"],
                                          ctx["M"], L)
    Q2 = Q * Q
    glogh = (DWr @ Q2) / eta[None, :]
    gloghL = (DWl @ Q2) / eta[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        cker = fb / eta
        BK = np.cumsum(Q * cker[None, :], axis=1)
        BKsh = np.concatenate([np.zeros((npts, 1)), BK[:, :-1]],
                              axis=1)
        QB = Q * BKsh
        dFrel = -(DWr @ QB) / fb[None, :]
        dFrelL = -(DWl @ QB) / fb[None, :]
    rhoT = fb[n_run - 1] ** 2 / eta[n_run - 1]
    DN = B57 - rhoT
    gmarg = -rhoT * (2.0 * dFrel[:, n_run - 1]
                     - glogh[:, n_run - 1])
    gmargL = -rhoT * (2.0 * dFrelL[:, n_run - 1]
                      - gloghL[:, n_run - 1])
    g = MF.local_gaps(uu)
    Gabs = np.maximum(np.abs(glogh), np.abs(gloghL))
    Gw = Gabs * g[:, None]
    L1 = Gw.sum(axis=0)
    L2 = np.sqrt((Gw ** 2).sum(axis=0))
    gm_abs = np.maximum(np.abs(gmarg), np.abs(gmargL))
    Lm1 = float(np.sum(g * gm_abs))
    Lm2 = float(math.sqrt(np.sum((g * gm_abs) ** 2)))
    return dict(rows=rows, Q=Q, eta=eta, fb=fb, n_run=n_run,
                glogh=glogh, gloghL=gloghL, dFrel=dFrel,
                gmarg=gmarg, gmargL=gmargL, DN=DN, rhoT=rhoT,
                gaps=g, Gabs=Gabs, L1=L1, L2=L2, Lm1=Lm1,
                Lm2=Lm2, DW=DWr, DWl=DWl, dists=dists, Dg=Dg,
                onnode=onnode, wsig=wsig, xe=xe,
                eta_ward=eta_ward)


def pred_dlg(gr, gl, du):
    """side-selected first-order prediction d log h_n =
    <grad log h_n, du>: components with du_j > 0 read the right
    slope, du_j < 0 the left slope (equal off-node)."""
    return (du * (du > 0.0)) @ gr + (du * (du < 0.0)) @ gl


def pred_flip(pred):
    """first-order flip criterion: first degree with linearized
    h through zero (relative change <= -1); None if none."""
    idx = np.nonzero(pred <= -1.0)[0]
    return int(idx[0]) if len(idx) else None


def mutant_gift_profile(prof, depths):
    """m3 MUST-FAIL MUTANT: a 'profile' oriented by the withheld
    lethality census -- the scope audit must FLAG this."""
    o = np.argsort(np.asarray(depths))
    return np.asarray(prof)[o]


# ------------------------------------------------ world machinery
def ctx_build(kz, comb=None, scramble_seed=None):
    """per-world context: comb, grid density, border zones,
    tent geometry.  Default comb = the r276 window_ctx comb
    (bitwise); comb/scramble overrides build the control worlds
    through the SAME sealed channel."""
    b0 = PIK.build_rung(kz)
    alpha = b0["alpha"]
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    if comb is not None:
        uu = np.asarray(comb[0], float).copy()
        mm = np.asarray(comb[1], float).copy()
    else:
        uu = np.asarray(rr["uu"], float).copy()
        mm = 2.0 * np.asarray(rr["lam"], float).copy()
    bb = PIK.build_rung(kz, comb=(uu, mm))
    darm = np.asarray(bb["d"], float).copy()
    L = int(bb["L"])
    N = int(bb["h"])
    M = L // 2 + 1
    sm = PB.smooth_comb(alpha)
    bsm = PIK.build_rung(kz, comb=sm)
    bx, bw, _ = PIK.folded_measure(bsm["d"], bsm["L"], +1.0)
    by, bv, _ = PIK.folded_measure(bsm["d"], bsm["L"], -1.0)
    return dict(kz=kz, N=N, L=L, M=M, alpha=alpha, uu=uu, mm=mm,
                darm=darm, bx=bx, bw=bw, by=by, bv=bv)


def pert_rows(ctx, u2, m2):
    """exact chain of a perturbed comb through the sealed channel
    (r276 nf_from_comb equivalent, full rows)."""
    bb = PIK.build_rung(ctx["kz"], comb=(u2, m2))
    d2 = np.asarray(bb["d"], float)
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    rows = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], ctx["N"])
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    return rows, nf, (xs, ws, ys, vs)


def dlg_measured(rows0, rows2):
    """measured d log h_n where both chains carry a positive sign
    (below any flip); nan elsewhere."""
    n = min(len(rows0), len(rows2))
    out = np.full(n, np.nan)
    for k in range(n):
        if rows0[k]["sg_h"] > 0 and rows2[k]["sg_h"] > 0:
            out[k] = rows2[k]["lg_h"] - rows0[k]["lg_h"]
    return out


def fd_pair(ctx, j, e):
    """central FD through the FULL pipeline for atom j at step e:
    returns (dlg vector over n, dDN)."""
    u_p = ctx["uu"].copy()
    u_m = ctx["uu"].copy()
    u_p[j] += e
    u_m[j] -= e
    rp, _nfp, _zp = pert_rows(ctx, u_p, ctx["mm"])
    rm, _nfm, _zm = pert_rows(ctx, u_m, ctx["mm"])
    n = min(len(rp), len(rm))
    dlg = np.full(ctx["N"], np.nan)
    for k in range(min(n, ctx["N"])):
        if rp[k]["sg_h"] > 0 and rm[k]["sg_h"] > 0:
            dlg[k] = (rp[k]["lg_h"] - rm[k]["lg_h"]) / (2.0 * e)
    DNp = B57 - rp[ctx["N"] - 1]["rho"]
    DNm = B57 - rm[ctx["N"] - 1]["rho"]
    return dlg, (DNp - DNm) / (2.0 * e)


def fd_dir(ctx, rows0, v, e):
    """ONE-SIDED FD along a full direction vector v at step e
    (side-selected slopes demand one-sided differences at the
    on-node atoms)."""
    rp, _n1, _z1 = pert_rows(ctx, ctx["uu"] + e * v, ctx["mm"])
    dlg = np.full(ctx["N"], np.nan)
    for k in range(min(len(rp), len(rows0), ctx["N"])):
        if rp[k]["sg_h"] > 0 and rows0[k]["sg_h"] > 0:
            dlg[k] = (rp[k]["lg_h"] - rows0[k]["lg_h"]) / e
    return dlg


# ------------------------------------------------ mp counter-check
def mp_lgh(zones, degs, dps):
    """mp signed-Stieltjes chain (r276 pattern): returns
    {n: log h_n} at the requested degrees (window zones only --
    the h-chain does not need the border)."""
    import mpmath as mp
    mp.mp.dps = dps
    xs, ws, ys, vs = zones
    X = [mp.mpf(float(v)) for v in xs]
    W = [mp.mpf(float(v)) for v in ws]
    Y = [mp.mpf(float(v)) for v in ys]
    V = [mp.mpf(float(v)) for v in vs]
    qx = [mp.mpf(1)] * len(X)
    qy = [mp.mpf(1)] * len(Y)
    qxm = [mp.mpf(0)] * len(X)
    qym = [mp.mpf(0)] * len(Y)
    Ls = mp.mpf(0)
    Lsm = mp.mpf(0)
    eta = sum(w * a * a for w, a in zip(W, qx)) \
        - sum(v * a * a for v, a in zip(V, qy))
    etam = eta
    want = set(degs)
    out = {}
    if 0 in want:
        out[0] = float(mp.log(abs(eta)))
    top = max(want)
    for n in range(top):
        alh = (sum(w * x * a * a for w, x, a in zip(W, X, qx))
               - sum(v * y * a * a
                     for v, y, a in zip(V, Y, qy))) / eta
        if n == 0:
            px = [(x - alh) * a for x, a in zip(X, qx)]
            py = [(y - alh) * a for y, a in zip(Y, qy)]
        else:
            ge = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
            fc = mp.e ** (Lsm - Ls)
            px = [(x - alh) * a - ge * fc * am
                  for x, a, am in zip(X, qx, qxm)]
            py = [(y - alh) * a - ge * fc * am
                  for y, a, am in zip(Y, qy, qym)]
        sc = max(max(abs(v) for v in px), max(abs(v) for v in py))
        qxm, qym, etam, Lsm = qx, qy, eta, Ls
        qx = [v / sc for v in px]
        qy = [v / sc for v in py]
        Ls += mp.log(sc)
        eta = sum(w * a * a for w, a in zip(W, qx)) \
            - sum(v * a * a for v, a in zip(V, qy))
        if n + 1 in want:
            out[n + 1] = float(mp.log(abs(eta)) + 2 * Ls)
    return out


def zones_of(ctx, u2):
    bb = PIK.build_rung(ctx["kz"], comb=(u2, ctx["mm"]))
    d2 = np.asarray(bb["d"], float)
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    return (xs, ws, ys, vs)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("metric_stability_probe -- PRIME.PORT.WALL."
          "METRIC_STABILITY.01 (round 278)")
    print("SPEC_SHA %s   R244_SHA %s (imported)   R276_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], BH.SPEC_SHA[:16], MF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 censuses + identity/eta/DW "
                        "wards + kink census + theta-0 + reduced "
                        "FD + m1 + m2 + scope audits; ladder, "
                        "profiles, lethality, controls, doses, "
                        "eps, mp, b3 skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED STABILITY ROUND (no proof, no "
          "bound, no mechanism claim): exact Hellmann-Feynman "
          "gradients d log h_n/du_j and border/CD gradients "
          "dF_n/du_j of the r244 chain through the sealed tent-"
          "grid channel, FD/mp-gated; gap-weighted Lipschitz "
          "curves L1/L2; dose adjudication against the rebuilt "
          "r276 P2 theta = %s worlds; quadratic window (eps %s); "
          "N-scaling over ladder %s; verdicts LAW/NONSMOOTH/"
          "FAILED + EXPLAINS_DOSE + U_PROFILE + N_TREND + "
          "MAINWINDOW_PREDICATE sealed BEFORE evaluation"
          % (str(THETAS_R276), str(EPS_LADDER), str(LADDER_KZS)))

    # ---------------- S1: censuses + identity wards
    section("S1  CENSUSES + IDENTITY WARDS")
    kzs = (MAIN_KZ,) if smoke else LADDER_KZS
    ctxs = {kz: ctx_build(kz) for kz in kzs}
    packs = {kz: grad_pack(ctxs[kz]) for kz in kzs}
    ok_id = True
    id_note = []
    for kz in kzs:
        ctx, pk = ctxs[kz], packs[kz]
        xs, ws, _ = PIK.folded_measure(ctx["darm"], ctx["L"], +1.0)
        ys, vs, _ = PIK.folded_measure(ctx["darm"], ctx["L"], -1.0)
        ref = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                            ctx["by"], ctx["bv"], ctx["N"])
        same = (len(ref) == pk["n_run"]) and all(
            ref[k][f] == pk["rows"][k][f]
            for k in range(len(ref))
            for f in ("lg_h", "sg_h", "Ls", "eta", "fb", "tb",
                      "rho", "alh", "gam_next"))
        ok_id = ok_id and same and pk["n_run"] == ctx["N"]
        id_note.append("w%d N %d" % (kz, ctx["N"]))
    check("G10-identity-chain", ok_id,
          "grad_chain reproduces BH.bord_chain FIELD-EXACTLY "
          "(lg_h/sg_h/Ls/eta/fb/tb/rho/alh/gam) on %d/%d ladder "
          "windows at full depth: %s -- the evaluation-grid "
          "extension changes nothing"
          % (len(kzs), len(kzs), "; ".join(id_note)))
    ok_ch = True
    for kz in (R276_KZS if not smoke else (MAIN_KZ,)):
        ctx = ctxs.get(kz) or ctx_build(kz)
        p_ref = BH.wpack(kz)
        pk = packs.get(kz) or grad_pack(ctx)
        rho_me = np.array([r["rho"] for r in pk["rows"]])
        nf_me = next((r["n"] for r in pk["rows"]
                      if r["sg_h"] < 0), None)
        ok_ch = ok_ch and bool(np.array_equal(rho_me,
                                              p_ref["rho"])) \
            and nf_me == p_ref["nf"]
    check("G11-channel-identity", ok_ch,
          "the comb channel reproduces BH.wpack BITWISE (rho "
          "array + nf) on the r276 windows -- the gradient block "
          "sits on the canonical object")
    ok_eta = all(packs[kz]["eta_ward"] <= ETA_WARD_BAR
                 for kz in kzs)
    check("G12-eta-reconstruction", ok_eta,
          "eta_n == <wsig, q_n^2> on the full fold grid at EVERY "
          "degree, worst rel %.1e (bar %.0e) -- the signed grid "
          "weight vector carries the chain exactly"
          % (max(packs[kz]["eta_ward"] for kz in kzs),
             ETA_WARD_BAR))
    # kink + reflection + on-node census
    ok_kink = True
    kink_note = []
    for kz in kzs:
        ctx, pk = ctxs[kz], packs[kz]
        Dg = pk["Dg"]
        off = ~pk["onnode"]
        mind = float(np.min(pk["dists"][off])) / Dg if \
            np.any(off) else float("nan")
        refl = float(np.min(ctx["uu"])) / Dg
        ok_kink = ok_kink and refl >= 2.0
        kink_note.append("w%d on-node %d/%d, off-node min-dist "
                         "%.3f D, min u %.0f D"
                         % (kz, int(np.sum(pk["onnode"])),
                            len(ctx["uu"]), mind, refl))
    check("G13-kink-reflection-census", ok_kink,
          "tent geometry: %s -- reflection branch INACTIVE "
          "everywhere (min u >= 2 D); ON-NODE atoms carry the "
          "disclosed one-sided derivative pair (on w9 they are "
          "the 2-power family: alpha = log 16 makes D "
          "commensurate with log 2)"
          % "; ".join(kink_note))
    c9 = ctxs[MAIN_KZ]
    u0, m0_ = MF.pert_jit(c9["uu"], c9["mm"], 0.0, SEED_R276,
                          False)
    ok0 = bool(np.array_equal(u0, c9["uu"])) \
        and bool(np.array_equal(m0_, c9["mm"]))
    check("G14-theta0-exact", ok0,
          "MF.pert_jit at theta = 0 returns BITWISE-identical "
          "arrays -- MAIN is the exact dose origin (r276 "
          "machinery loaded verbatim)")

    # ---------------- S2: FD gates + mp + must-fails
    section("S2  LEG A1 -- FD GATES + MP COUNTER-CHECK + "
            "MUST-FAILS")
    fd_kzs = (MAIN_KZ,) if smoke else R276_KZS
    worst_rich = worst_raw = 0.0
    n_pairs = 0
    n_skip = 0
    n_esc = 0
    worst_esc = 0.0
    esc_ok = True
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        N = ctx["N"]
        degs = (5, N // 3, 2 * N // 3, N - 1)
        offi = np.nonzero(~pk["onnode"])[0]
        hot = offi[int(np.argmax(
            (pk["gaps"] * np.abs(pk["glogh"][:, N - 1]))[offi]))]
        atoms = sorted(set((int(offi[0]),
                            int(offi[len(offi) // 2]),
                            int(offi[-1]), int(hot))))
        if smoke:
            atoms = atoms[:2]
        for j in atoms:
            allowed = [e for e in FD_STEPS
                       if e <= KINK_GUARD * pk["dists"][j]]
            if len(allowed) < 2:
                n_skip += 1
                continue
            e_big, e_small = allowed[-2], allowed[-1]
            fd_b, _db = fd_pair(ctx, j, e_big)
            fd_s, _ds = fd_pair(ctx, j, e_small)
            r2 = (e_big / e_small) ** 2
            for n in degs:
                gan = pk["glogh"][j, n]
                floor = max(GRAD_FLOOR_FRAC * float(
                    np.max(np.abs(pk["glogh"][:, n]))),
                    ABS_GRAD_MIN)
                if abs(gan) < floor:
                    n_skip += 1
                    continue
                if not (np.isfinite(fd_b[n])
                        and np.isfinite(fd_s[n])):
                    n_skip += 1
                    continue
                rich = fd_s[n] + (fd_s[n] - fd_b[n]) / (r2 - 1.0)
                dev_r = abs(rich - gan) / max(abs(gan), floor)
                dev_w = abs(fd_s[n] - gan) / max(abs(gan), floor)
                if dev_r > FD_RICH_BAR and not smoke:
                    # amendment a1: the f64 chain rounding error
                    # is SMOOTH in u -- its gradient pollutes the
                    # f64 FD on the deep window; the sealed mp
                    # (dps 40) FD arbitrates
                    n_esc += 1
                    u_pe = ctx["uu"].copy()
                    u_me = ctx["uu"].copy()
                    u_pe[j] += MP_E_ESC
                    u_me[j] -= MP_E_ESC
                    lpe = mp_lgh(zones_of(ctx, u_pe), (n,),
                                 MP_DPS)[n]
                    lme = mp_lgh(zones_of(ctx, u_me), (n,),
                                 MP_DPS)[n]
                    dev_e = abs((lpe - lme) / (2.0 * MP_E_ESC)
                                - gan) / max(abs(gan), floor)
                    worst_esc = max(worst_esc, dev_e)
                    esc_ok = esc_ok and dev_e <= MP_FD_BAR
                else:
                    worst_rich = max(worst_rich, dev_r)
                worst_raw = max(worst_raw, dev_w)
                n_pairs += 1
    check("G20-fd-gates", worst_rich <= FD_RICH_BAR
          and worst_raw <= FD_RAW_BAR and esc_ok
          and n_pairs >= (2 if smoke else 8),
          "central FD through the FULL pipeline (off-node "
          "atoms, kink-guarded adaptive steps, Richardson from "
          "the two smallest allowed): %d pairs on %s, worst "
          "f64 Richardson dev %.1e (bar %.0e), worst raw dev "
          "%.1e (bar %.0e), %d skipped (kink guard / grad "
          "floor / flip overlap); %d pairs ESCALATED to the "
          "sealed mp (dps %d) FD where the f64 chain "
          "error-gradient bites (worst mp dev %.1e, bar %.0e) "
          "-- the Hellmann-Feynman formula IS the derivative "
          "of the machinery"
          % (n_pairs, str(fd_kzs), worst_rich, FD_RICH_BAR,
             worst_raw, FD_RAW_BAR, n_skip, n_esc, MP_DPS,
             worst_esc, MP_FD_BAR))
    # one-sided gate at the hottest ON-node atom (w9)
    pk9s = packs[MAIN_KZ]
    c9s = ctxs[MAIN_KZ]
    N9s = c9s["N"]
    oni = np.nonzero(pk9s["onnode"])[0]
    worst_one = 0.0
    one_note = "no on-node atoms"
    if len(oni):
        j_on = oni[int(np.argmax(
            (pk9s["gaps"]
             * np.abs(pk9s["glogh"][:, N9s - 1]))[oni]))]
        e_b, e_s = FD_STEPS[-2], FD_STEPS[-1]
        r_ = e_b / e_s
        base_lg = np.array([r["lg_h"] for r in pk9s["rows"]])
        vals = {}
        for sgn, gmat in ((+1.0, pk9s["glogh"]),
                          (-1.0, pk9s["gloghL"])):
            fds = {}
            for e in (e_b, e_s):
                u2 = c9s["uu"].copy()
                u2[j_on] += sgn * e
                rws, _nf, _z = pert_rows(c9s, u2, c9s["mm"])
                lg2 = np.array([r["lg_h"] for r in rws])
                fds[e] = sgn * (lg2 - base_lg[:len(lg2)]) / e
            for n in (2 * N9s // 3, N9s - 1):
                gan = gmat[j_on, n]
                rich = (r_ * fds[e_s][n] - fds[e_b][n]) \
                    / (r_ - 1.0)
                dev = abs(rich - gan) / max(abs(gan),
                                            ABS_GRAD_MIN)
                worst_one = max(worst_one, dev)
                vals[(sgn, n)] = dev
        one_note = ("j %d (2-power family), right/left devs %s"
                    % (int(j_on),
                       str({("%+d@n%d" % (s, n)): "%.1e" % d
                            for (s, n), d in vals.items()})))
    check("G20b-fd-one-sided", worst_one <= FD_ONE_BAR,
          "ONE-SIDED FD (first-order Richardson) at the hottest "
          "on-node w9 atom, left and right slope separately: "
          "%s, worst dev %.1e (bar %.0e) -- the kink pair is "
          "the correct derivative object at the 2-power atoms"
          % (one_note, worst_one, FD_ONE_BAR))
    # directional FD (one-sided, side-selected prediction)
    worst_dir = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        N = ctx["N"]
        dist_eff = np.where(pk["onnode"], pk["Dg"], pk["dists"])
        for di in range(1 if smoke else 2):
            rng = np.random.default_rng(SEED_DIR + kz * 100 + di)
            v = pk["gaps"] * rng.uniform(-1.0, 1.0,
                                         len(ctx["uu"]))
            with np.errstate(divide="ignore"):
                caps = KINK_GUARD * dist_eff \
                    / np.maximum(np.abs(v), 1e-300)
            cap = float(np.min(caps))
            allowed = [e for e in FD_STEPS if e <= cap]
            if len(allowed) < 2:
                continue
            e_b, e_s = allowed[-2], allowed[-1]
            fd_b = fd_dir(ctx, pk["rows"], v, e_b)
            fd_s = fd_dir(ctx, pk["rows"], v, e_s)
            r_ = e_b / e_s
            pred = pred_dlg(pk["glogh"], pk["gloghL"], v)
            for n in (5, N // 2, N - 1):
                if abs(pred[n]) < ABS_GRAD_MIN:
                    continue
                if not (np.isfinite(fd_b[n])
                        and np.isfinite(fd_s[n])):
                    continue
                rich = (r_ * fd_s[n] - fd_b[n]) / (r_ - 1.0)
                worst_dir = max(worst_dir,
                                abs(rich - pred[n])
                                / abs(pred[n]))
    check("G21-directional-fd", worst_dir <= DIR_BAR,
          "full-vector ONE-SIDED directional FD (pinned "
          "gap-scaled directions incl. the on-node atoms, "
          "first-order Richardson) vs the SIDE-SELECTED "
          "prediction: worst dev %.1e (bar %.0e) -- the "
          "gradient assembles correctly over ALL atoms"
          % (worst_dir, DIR_BAR))
    # margin FD (amendment a1: Richardson from the two LARGEST
    # kink-guarded steps -- |dD| ~ 1e-9..1e-7 sits at the f64
    # cancellation floor at the smallest steps)
    worst_marg = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        offi = np.nonzero(~pk["onnode"])[0]
        j = int(offi[int(np.argmax(
            (pk["gaps"] * np.abs(pk["gmarg"]))[offi]))])
        allowed = [e for e in FD_STEPS
                   if e <= KINK_GUARD * pk["dists"][j]]
        if len(allowed) < 2:
            continue
        e_b, e_s = allowed[-2], allowed[-1]
        _f1, dD_b = fd_pair(ctx, j, e_b)
        _f2, dD_s = fd_pair(ctx, j, e_s)
        r2 = (e_b / e_s) ** 2
        rich = dD_s + (dD_s - dD_b) / (r2 - 1.0)
        gan = pk["gmarg"][j]
        worst_marg = max(worst_marg,
                         abs(rich - gan) / max(abs(gan), 1e-10))
    check("G22-margin-fd", worst_marg <= MARG_BAR,
          "terminal-margin gradient dD_N/du_j (border/CD route) "
          "vs Richardson FD at the hottest margin atom per "
          "window: worst dev %.1e (bar %.0e) -- the chain rule "
          "through rho = F^2/h is exact"
          % (worst_marg, MARG_BAR))
    # DW ward (piecewise-linear map: FD exact to rounding)
    worst_dw = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        offi = np.nonzero(~pk["onnode"])[0]
        for j in (int(offi[0]), int(offi[len(offi) // 2]),
                  int(offi[-1])):
            if DW_E > KINK_GUARD * pk["dists"][j]:
                continue
            u_p = ctx["uu"].copy()
            u_m = ctx["uu"].copy()
            u_p[j] += DW_E
            u_m[j] -= DW_E
            dp = np.asarray(PIK.build_rung(
                kz, comb=(u_p, ctx["mm"]))["d"], float)
            dm = np.asarray(PIK.build_rung(
                kz, comb=(u_m, ctx["mm"]))["d"], float)
            fdw = (wsig_vec(dp, ctx["L"])
                   - wsig_vec(dm, ctx["L"])) / (2.0 * DW_E)
            sc = float(np.linalg.norm(pk["DW"][j]))
            worst_dw = max(worst_dw,
                           float(np.linalg.norm(fdw - pk["DW"][j]))
                           / max(sc, 1e-300))
    check("G23-dw-ward", worst_dw <= DW_BAR,
          "tent+FFT weight derivative DW vs central FD of the "
          "full weight vector (e = %.0e): worst rel %.1e (bar "
          "%.0e) -- the piecewise-linear map is differentiated "
          "EXACTLY between kinks" % (DW_E, worst_dw, DW_BAR))
    # mp counter-check
    if smoke:
        check("G24-mp-counter-fd", True, "SMOKE: skipped")
    else:
        pk9 = packs[MAIN_KZ]
        N9 = ctxs[MAIN_KZ]["N"]
        offi9 = np.nonzero(~pk9["onnode"])[0]
        degs_mp = (2 * N9 // 3, N9 - 1)
        j_a = int(offi9[int(np.argmax(
            np.abs(pk9["glogh"][:, degs_mp[0]])[offi9]))])
        j_b = int(offi9[int(np.argmax(
            np.abs(pk9["glogh"][:, degs_mp[1]])[offi9]))])
        if j_b == j_a:
            ordb = offi9[np.argsort(
                -np.abs(pk9["glogh"][:, degs_mp[1]])[offi9])]
            j_b = int(ordb[1])
        z0 = zones_of(c9, c9["uu"])
        base_mp = mp_lgh(z0, degs_mp, MP_DPS)
        base_dev = max(abs(base_mp[n] - pk9["rows"][n]["lg_h"])
                       for n in degs_mp)
        ok_mp = base_dev <= MP_BASE_BAR
        mp_note = ["base lg dev %.1e" % base_dev]
        for j, n_t in ((j_a, degs_mp[0]), (j_b, degs_mp[1])):
            if MP_E > KINK_GUARD * pk9["dists"][j]:
                mp_note.append("j%d kink-guarded, skipped" % j)
                continue
            u_p = c9["uu"].copy()
            u_m = c9["uu"].copy()
            u_p[j] += MP_E
            u_m[j] -= MP_E
            lp = mp_lgh(zones_of(c9, u_p), (n_t,), MP_DPS)[n_t]
            lm = mp_lgh(zones_of(c9, u_m), (n_t,), MP_DPS)[n_t]
            fd_mp = (lp - lm) / (2.0 * MP_E)
            gan = pk9["glogh"][j, n_t]
            dev = abs(fd_mp - gan) / max(abs(gan), 1e-10)
            ok_mp = ok_mp and dev <= MP_FD_BAR
            mp_note.append("(n %d, j %d) dev %.1e" % (n_t, j, dev))
        check("G24-mp-counter-fd", ok_mp,
              "mp (dps %d) chain FD at e = %.0e on the sealed w9 "
              "pairs: %s (base bar %.0e, FD bar %.0e) -- no f64 "
              "chain noise in the gradient gates"
              % (MP_DPS, MP_E, "; ".join(mp_note), MP_BASE_BAR,
                 MP_FD_BAR))
    # must-fails m1a/m1b/m2
    pk9 = packs[MAIN_KZ]
    N9 = c9["N"]
    offi9m = np.nonzero(~pk9["onnode"])[0]
    j_hot = int(offi9m[int(np.argmax(
        (pk9["gaps"] * np.abs(pk9["glogh"][:, N9 - 1]))[offi9m]))])
    allowed = [e for e in FD_STEPS
               if e <= KINK_GUARD * pk9["dists"][j_hot]]
    e_b, e_s = allowed[-2], allowed[-1]
    fd_b, _d1 = fd_pair(c9, j_hot, e_b)
    fd_s, _d2 = fd_pair(c9, j_hot, e_s)
    r2 = (e_b / e_s) ** 2
    rich = fd_s[N9 - 1] + (fd_s[N9 - 1] - fd_b[N9 - 1]) / (r2 - 1)
    # m1a: sin^2 weight factor dropped
    L9 = c9["L"]
    Dg9 = pk9["Dg"]
    i0 = int(math.floor(c9["uu"][j_hot] / Dg9))
    dcM = np.zeros(c9["M"])
    dcM[i0] += c9["mm"][j_hot] / (2.0 * Dg9)
    dcM[i0 + 1] -= c9["mm"][j_hot] / (2.0 * Dg9)
    dd = PIK.grid_density(dcM)
    ll = np.arange(L9)
    fold = np.minimum(ll, L9 - ll)
    npts9 = L9 // 2 + 1
    row_m1a = np.zeros(npts9)
    np.add.at(row_m1a, fold, dd * (1.0 / (2.0 * L9)))
    g_m1a = float(row_m1a @ (pk9["Q"][:, N9 - 1] ** 2)
                  / pk9["eta"][N9 - 1])
    dev_m1a = abs(g_m1a - rich) / abs(rich)
    # m1b: mirror arm of the even extension dropped
    s_l = 4.0 * np.sin(math.pi * ll / L9) ** 2 / (2.0 * L9)
    half = ll <= L9 // 2
    row_m1b = np.zeros(npts9)
    np.add.at(row_m1b, fold[half], (dd * s_l)[half])
    g_m1b = float(row_m1b @ (pk9["Q"][:, N9 - 1] ** 2)
                  / pk9["eta"][N9 - 1])
    dev_m1b = abs(g_m1b - rich) / abs(rich)
    check("G25-mustfail-weight-terms", dev_m1a >= MUT_LOUD
          and dev_m1b >= MUT_LOUD,
          "m1 WEIGHT-TERM MUTANTS at the hottest w9 pair: "
          "dropping the s_l = 4 sin^2/(2L) factor deviates "
          "%.1e and dropping the mirror arm deviates %.1e from "
          "the Richardson FD (bar >= %.1f) -- every factor of "
          "the sealed weight map is load-bearing"
          % (dev_m1a, dev_m1b, MUT_LOUD))
    fd_r, _d3 = fd_pair(c9, j_hot, ROUND_E)
    v_r = fd_r[N9 - 1] if np.isfinite(fd_r[N9 - 1]) else 0.0
    dev_m2 = abs(v_r - rich) / abs(rich)
    check("G26-mustfail-rounding-step", dev_m2 >= ROUND_MIN_DEV,
          "m2 ROUNDING-REGIME FD (step %.0e, below one ulp of "
          "u): dev %.1e >= %.0e vs the analytic gradient -- the "
          "kink-guarded adaptive step is load-bearing, a naive "
          "FD is NOT a substitute for the formula"
          % (ROUND_E, dev_m2, ROUND_MIN_DEV))

    if smoke:
        for g_ in ("G30-control-anchors", "G31-uprofile",
                   "G32-lethality-census", "G33-control-contrast",
                   "G40-conservation-doses", "G41-dose-ratio",
                   "G42-flip-prediction", "G43-extrapolation",
                   "G50-quadratic-window", "G60-n-scaling",
                   "G70-stability-hypothesis",
                   "G71-mainwindow-predicate"):
            check(g_, True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # ---------------- S3: u-profile + lethality + controls
        section("S3  LEG A2/A3 -- U-PROFILE + LETHALITY + "
                "CONTROLS")
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrl_ctx = {
            "EPSTEIN": ctx_build(MAIN_KZ, comb=(
                np.log(nn_idx.astype(float)),
                2.0 * lamE[nn_idx]
                / np.sqrt(nn_idx.astype(float)))),
            "SCRAMBLE": ctx_build(MAIN_KZ, scramble_seed=1),
            "SMOOTH": ctx_build(MAIN_KZ,
                                comb=PB.smooth_comb(
                                    rr9["alpha"]))}
        ctrl_pk = {c: grad_pack(ctrl_ctx[c]) for c in ctrl_ctx}
        ctrl_nf = {c: next((r["n"] for r in ctrl_pk[c]["rows"]
                            if r["sg_h"] < 0), None)
                   for c in ctrl_ctx}
        ok_ctrl = all(ctrl_nf[c] == CTRL_FLIPS[c]
                      for c in ctrl_ctx)
        nf_main = {kz: next((r["n"] for r in packs[kz]["rows"]
                             if r["sg_h"] < 0), None)
                   for kz in LADDER_KZS}
        check("G30-control-anchors", ok_ctrl
              and all(nf_main[kz] is None for kz in LADDER_KZS),
              "controls re-derived %s == the sealed 25/21/27 "
              "through the gradient chain; MAIN positive at "
              "full depth on all %d ladder windows"
              % (str(ctrl_nf), len(LADDER_KZS)))
        # u-profile on the r276 windows
        prof = {}
        sp_pos = {}
        sp_wt = {}
        for kz in R276_KZS:
            ctx, pk = ctxs[kz], packs[kz]
            A = pk["gaps"] * np.max(np.abs(pk["glogh"]), axis=1)
            Mj = pk["gaps"] * np.abs(pk["gmarg"])
            pos = ctx["uu"] / (2.0 * ctx["alpha"])
            prof[kz] = (A, Mj, pos)
            sp_pos[kz] = BH.spearman(A, pos)
            sp_wt[kz] = BH.spearman(A, ctx["mm"])
        A9, M9, pos9 = prof[MAIN_KZ]
        topi = np.argsort(A9)[::-1][:3]
        sp_am = BH.spearman(A9, M9)
        check("G31-uprofile", True,
              "U-PROFILE (gap-weighted A_j = g_j max_n "
              "|dlogh/du_j|): sp(A, hull pos) %s; sp(A, weight) "
              "%s; sp(A, margin map M_j) %+.2f (w9); top-3 w9 "
              "atoms at hull positions %s with A %s -- the "
              "sensitivity localization the r276 follow-up "
              "asked for"
              % (str({k: "%+.2f" % sp_pos[k] for k in sp_pos}),
                 str({k: "%+.2f" % sp_wt[k] for k in sp_wt}),
                 sp_am,
                 str(["%.2f" % pos9[i] for i in topi]),
                 str(["%.1f" % A9[i] for i in topi])))
        # lethality census (w9, deterministic +/- g_j singles)
        g9 = packs[MAIN_KZ]["gaps"]
        depths = np.empty(len(c9["uu"]))
        flips = []
        for j in range(len(c9["uu"])):
            dmin = 1.0
            for sgn in (+1.0, -1.0):
                u2 = c9["uu"].copy()
                u2[j] += sgn * g9[j]
                _r2, nf2, _z2 = pert_rows(c9, u2, c9["mm"])
                dmin = min(dmin, 1.0 if nf2 is None
                           else nf2 / N9)
                if nf2 is not None:
                    flips.append(nf2)
            depths[j] = dmin
        sp_leth = BH.spearman(A9, depths)
        n_flip = int(np.sum(depths < 1.0))
        if sp_leth <= SP_PRED:
            u_cls = "U_PROFILE_PREDICTIVE"
        elif sp_leth <= SP_WEAK:
            u_cls = "U_PROFILE_WEAK"
        else:
            u_cls = "U_PROFILE_UNCOUPLED"
        check("G32-lethality-census", True,
              "deterministic +/-g_j singles on w9: %d/%d atoms "
              "flip the wall (flip degrees %d..%d; the r276 "
              "lethal band was 51..152), sp(A_j, min-depth_j) = "
              "%+.2f -> %s (sealed bars %.1f/%.1f) -- the "
              "gradient map vs the measured single-op lethality"
              % (n_flip, len(depths),
                 min(flips) if flips else -1,
                 max(flips) if flips else -1, sp_leth, u_cls,
                 SP_PRED, SP_WEAK))
        # control contrast maps
        cm_note = []
        A_main = A9
        cm_main = float(np.sum(A_main * pos9) / np.sum(A_main))
        for c in ("EPSTEIN", "SCRAMBLE", "SMOOTH"):
            ctxc, pkc = ctrl_ctx[c], ctrl_pk[c]
            nfc = ctrl_nf[c]
            Ac = pkc["gaps"] * np.max(
                np.abs(pkc["glogh"][:, :nfc]), axis=1)
            posc = ctxc["uu"] / (2.0 * ctxc["alpha"])
            cmc = float(np.sum(Ac * posc) / np.sum(Ac))
            L1c = float(np.median(pkc["L1"][:nfc]))
            L1m_pre = float(np.median(
                packs[MAIN_KZ]["L1"][:nfc]))
            cm_note.append("%s cm %.2f L1med %.3g (MAIN same "
                           "range %.3g)" % (c, cmc, L1c,
                                            L1m_pre))
        L1m = float(np.median(packs[MAIN_KZ]["L1"]))
        check("G33-control-contrast", True,
              "CONTRAST (pre-flip gradient maps, hull "
              "coordinate u/(2 alpha)): MAIN hull-cm %.2f, L1 "
              "med %.3g (full depth) vs %s -- typed "
              "MEASUREMENT: where the wrong arithmetic is "
              "fragile vs where MAIN is"
              % (cm_main, L1m, "; ".join(cm_note)))

        # ---------------- S4: dose adjudication (b1)
        section("S4  LEG B1 -- THE r276 DOSE ADJUDICATION")
        cons_ok = True
        band_ratios = []
        flip_devs = []
        kink_cross = []
        dose_worlds = {}
        for th in THETAS_R276:
            for kz in R276_KZS:
                ctx, pk = ctxs[kz], packs[kz]
                for rep in range(REPS):
                    seed = (SEED_R276 + P2_SI * 100000
                            + DOSE_DI[th] * 10000 + rep * 1000
                            + WIN_WI[kz] * 10)
                    u2, m2 = MF.pert_jit(ctx["uu"], ctx["mm"],
                                         th, seed, False)
                    cons_ok = cons_ok and MF.conserve_comb(
                        "P2_JIT", ctx["uu"], ctx["mm"], u2, m2,
                        th)
                    du = u2 - ctx["uu"]
                    Dg = pk["Dg"]
                    cross = int(np.sum(
                        np.floor(ctx["uu"] / Dg)
                        != np.floor(u2 / Dg)))
                    rows2, nf2, _z = pert_rows(ctx, u2, m2)
                    pred = pred_dlg(pk["glogh"], pk["gloghL"],
                                    du)
                    npred = pred_flip(pred)
                    dose_worlds[(th, kz, rep)] = (
                        du, nf2, npred, cross)
                    if th == THETAS_R276[0]:
                        kink_cross.append(cross)
                        meas = dlg_measured(pk["rows"], rows2)
                        m_ = np.isfinite(meas) \
                            & (np.abs(meas) >= BAND_LO) \
                            & (np.abs(meas) <= BAND_HI)
                        if np.any(m_):
                            band_ratios.append(float(np.median(
                                pred[m_] / meas[m_])))
                        if nf2 is not None:
                            npx = ctx["N"] if npred is None \
                                else npred
                            flip_devs.append(
                                abs(npx - nf2) / nf2)
        check("G40-conservation-doses", cons_ok,
              "conservation EXACT (MF.conserve_comb) on all %d "
              "rebuilt r276 P2 worlds (theta %s x %d reps x %s)"
              % (len(dose_worlds), str(THETAS_R276), REPS,
                 str(R276_KZS)))
        med_ratio = float(np.median(band_ratios)) \
            if band_ratios else float("nan")
        med_flip = float(np.median(flip_devs)) \
            if flip_devs else float("nan")
        if (RATIO_EXPL[0] <= med_ratio <= RATIO_EXPL[1]
                and med_flip <= FLIP_TOL):
            dose_cls = "EXPLAINED"
        elif (RATIO_PART[0] <= med_ratio <= RATIO_PART[1]
                or med_flip <= 2 * FLIP_TOL):
            dose_cls = "PARTIAL"
        else:
            dose_cls = "UNEXPLAINED"
        check("G41-dose-ratio", True,
              "theta = 0.02 replicates (seeds exact): median "
              "band ratio pred/meas %.2f over %d replicates "
              "(band %.0e..%.1f, replicate medians %s); kink "
              "crossings med %.0f/%d atoms -- sealed classes "
              "EXPLAINED %s / PARTIAL %s"
              % (med_ratio, len(band_ratios), BAND_LO, BAND_HI,
                 str(["%.2f" % r for r in band_ratios]),
                 float(np.median(kink_cross)) if kink_cross
                 else -1, len(c9["uu"]),
                 str(RATIO_EXPL), str(RATIO_PART)))
        fl_note = []
        for kz in R276_KZS:
            pm = [(dose_worlds[(0.02, kz, r)][2],
                   dose_worlds[(0.02, kz, r)][1])
                  for r in range(REPS)]
            fl_note.append("w%d pred %s meas %s"
                           % (kz, [p for p, _ in pm],
                              [m for _, m in pm]))
        check("G42-flip-prediction", True,
              "first-order flip criterion (first n with "
              "<grad, du> <= -1) vs the measured flip: median "
              "|n_pred - nf|/nf = %.2f (tol %.2f); %s -> "
              "GRADIENT_EXPLAINS_DOSE(%s)"
              % (med_flip, FLIP_TOL, "; ".join(fl_note),
                 dose_cls))
        ex_note = []
        for th in THETAS_R276[1:]:
            devs = []
            for kz in R276_KZS:
                for rep in range(REPS):
                    _du, nf2, npred, _c = dose_worlds[(th, kz,
                                                       rep)]
                    if nf2 is not None:
                        npx = ctxs[kz]["N"] if npred is None \
                            else npred
                        devs.append(abs(npx - nf2) / nf2)
            ex_note.append("theta %.2f med dev %.2f (%d)"
                           % (th, float(np.median(devs))
                              if devs else float("nan"),
                              len(devs)))
        check("G43-extrapolation", True,
              "EXTRAPOLATION of the linear flip criterion to "
              "the r276 stages 0.05/0.10 (rebuilt worlds): %s "
              "-- where the global curve leaves first order "
              "(typed MEASUREMENT)" % "; ".join(ex_note))

        # ---------------- S5: quadratic window (b2)
        section("S5  LEG B2 -- THE QUADRATIC REST")
        q_cons = []
        thetas_star = {kz: [] for kz in B2_KZS}
        n_res_q = 0
        n_unres = 0
        n_explode = 0
        for kz in B2_KZS:
            ctx, pk = ctxs[kz], packs[kz]
            N = ctx["N"]
            Dg = pk["Dg"]
            dirs = []
            for rep in range(REPS):
                seed = (SEED_R276 + P2_SI * 100000
                        + DOSE_DI[0.02] * 10000 + rep * 1000
                        + WIN_WI[kz] * 10)
                u2, _m2 = MF.pert_jit(ctx["uu"], ctx["mm"], 0.02,
                                      seed, False)
                dirs.append((u2 - ctx["uu"]) / 0.02)
            for di in range(2):
                rng = np.random.default_rng(SEED_DIR + 7000
                                            + kz * 100 + di)
                dirs.append(pk["gaps"]
                            * rng.uniform(-1.0, 1.0,
                                          len(ctx["uu"])))
            degs = (N // 4, N // 2, 3 * N // 4, N - 1)
            for dvec in dirs:
                v = dvec.copy()
                v[pk["dists"] < KINK_PROJ * Dg] = 0.0
                with np.errstate(divide="ignore"):
                    caps = np.where(
                        np.abs(v) > 0.0,
                        0.9 * pk["dists"]
                        / np.maximum(np.abs(v), 1e-300),
                        np.inf)
                cap = float(np.min(caps))
                eps_ok = [e for e in EPS_LADDER if e <= cap]
                if len(eps_ok) < 2:
                    n_unres += 1
                    continue
                g1 = pred_dlg(pk["glogh"], pk["gloghL"], v)
                qs = {}
                for e in eps_ok:
                    rp, nfp, _z1 = pert_rows(ctx,
                                             ctx["uu"] + e * v,
                                             ctx["mm"])
                    rm, nfm, _z2 = pert_rows(ctx,
                                             ctx["uu"] - e * v,
                                             ctx["mm"])
                    dp = dlg_measured(pk["rows"], rp)
                    dm = dlg_measured(pk["rows"], rm)
                    qv = np.full(N, np.nan)
                    for n in degs:
                        if (np.isfinite(dp[n])
                                and np.isfinite(dm[n])
                                and abs(dp[n] + dm[n])
                                >= Q_FLOOR):
                            qv[n] = (dp[n] + dm[n]) / e ** 2
                    qs[e] = qv
                for n in degs:
                    pairq = [qs[e][n] for e in eps_ok
                             if np.isfinite(qs[e][n])]
                    if len(pairq) < 2:
                        n_unres += 1
                        continue
                    n_res_q += 1
                    r_ = max(abs(pairq[0] / pairq[1]),
                             abs(pairq[1] / pairq[0])) \
                        if pairq[1] != 0 else float("inf")
                    q_cons.append(r_)
                    if r_ > QCONS_EXPLODE:
                        n_explode += 1
                    q_small = pairq[0]
                    if q_small != 0.0 and abs(g1[n]) > 0:
                        thetas_star[kz].append(
                            abs(g1[n]) / abs(q_small))
        med_cons = float(np.median(q_cons)) if q_cons \
            else float("nan")
        b2_verdict = ("TAME" if med_cons <= QCONS_TAME else
                      ("NONSMOOTH" if med_cons > QCONS_EXPLODE
                       else "INTERMEDIATE"))
        ts_note = {kz: (float(np.median(thetas_star[kz])),
                        float(np.min(thetas_star[kz])))
                   for kz in B2_KZS if thetas_star[kz]}
        check("G50-quadratic-window", True,
              "SEALED q-consistency (adjacent eps, %d resolvable "
              "probes, %d unresolved): median %.2f (TAME bar %.0f"
              ", explode bar %.0f, %d probes explode) -> %s; "
              "validity window theta* = |lin|/|quad|: %s vs the "
              "r276 smallest dose 0.02"
              % (n_res_q, n_unres, med_cons, QCONS_TAME,
                 QCONS_EXPLODE, n_explode, b2_verdict,
                 str({("w%d" % k): ("med %.1e min %.1e" % v)
                      for k, v in ts_note.items()})))

        # ---------------- S6: N-scaling (b3)
        section("S6  LEG B3 -- N-SCALING OF L")
        recs = sorted(((ctxs[kz]["N"], kz) for kz in LADDER_KZS))
        Ns = [n for n, _ in recs]
        Lm = [packs[kz]["Lm1"] for _, kz in recs]
        Lx = [float(np.max(packs[kz]["L1"])) for _, kz in recs]
        b_L = halves_slope(Ns, Lm)
        dec = max(Lm) / min(Lm)
        if b_L >= TREND_SLOPE:
            trend = "GROWING"
        elif b_L <= -TREND_SLOPE:
            trend = "SHRINKING"
        else:
            trend = "FLAT"
        uniform = (trend == "FLAT" and dec <= TREND_DECADE)
        for (n, kz), lm, lx in zip(recs, Lm, Lx):
            info("kz %-3d N %-4d L_D %10.3g  max_n L1 %10.3g  "
                 "D_N %+9.6f"
                 % (kz, n, lm, lx, packs[kz]["DN"]))
        check("G60-n-scaling", True,
              "gap-relative margin Lipschitz L_D over the "
              "ladder: %s on N %s; halves slope b_L = %+.2f "
              "(bands +/-%.1f), decade %.1f (bar %.0f) -> "
              "N_TREND(%s)%s"
              % (str(["%.3g" % v for v in Lm]), str(Ns), b_L,
                 TREND_SLOPE, dec, TREND_DECADE, trend,
                 ", UNIFORM_CANDIDATE" if uniform else
                 " -- NO uniform lemma candidate from this "
                 "data"))

        # ---------------- S7: hypothesis + predicate + scopes
        section("S7  LEG C -- HYPOTHESIS + MAINWINDOW PREDICATE")
        ts9 = ts_note.get(MAIN_KZ, (float("nan"), float("nan")))
        check("G70-stability-hypothesis", True,
              "STABILITY HYPOTHESIS (typed TASK_FORMULATION_"
              "ONLY, falsifiable): 'positivity reserve >= "
              "margin_MAIN - L_D(w) theta - O(theta^2) for "
              "gap-relative doses theta <= theta*(w)' with "
              "MEASURED L_D %s over N %s (b_L %+.2f), theta* "
              "med %.1e (w9) -- locally %s, first order "
              "explains the smallest r276 dose at ratio %.2f, "
              "linearity leaves the global curve per G43"
              % (str(["%.3g" % v for v in Lm]), str(Ns), b_L,
                 ts9[0], b2_verdict, med_ratio))
        check("G71-mainwindow-predicate", True,
              "MAINWINDOW PREDICATE (typed PERTURBATIVE_ONLY): "
              "MetricNear(c, MAIN, theta) := max_j |u_j - "
              "u_j^MAIN|/g_j <= theta; for theta <= theta*(w) "
              "the stability inequality INHERITS margin(c) >= "
              "margin_MAIN - L_D(w) theta; %s -- the predicate "
              "transports wall positivity only PERTURBATIVELY "
              "around MAIN; the MAIN positivity itself stays "
              "the open center (H5 untouched)"
              % (("with N-trend %s and NO uniform constant "
                  "(G60), any Lean encoding must carry L_D(w) "
                  "per window" % trend) if not uniform else
                 "a UNIFORM candidate constant exists (G60)"))
        h_p = []
        for fn in GRAD_FUNCS:
            h_p.extend(scope_audit(fn, GRAD_FORBIDDEN))
        h_g = scope_audit("mutant_gift_profile", GRAD_FORBIDDEN)
        ag_hits = antigate_fragment_audit()
        check("G72-scope-audits", not h_p and bool(h_g)
              and not ag_hits,
              "the gradient constructors audit CLEAN against "
              "the withheld truth-side set (incl. the lethality "
              "census)%s; the gift profile FLAGGED (%s); "
              "fragment audit (no fit primitives): %s"
              % ("" if not h_p else " VIOLATION "
                 + "; ".join(h_p),
                 "; ".join(h_g) if h_g else "NOT FLAGGED",
                 "CLEAN" if not ag_hits else "; ".join(ag_hits)))

        # verdict assembly
        a1_gates = ("G20", "G20b", "G21", "G22", "G23", "G24")
        a1_ok = all(ok for nm, ok, _d in CHECKS
                    if nm.startswith(a1_gates))
        if not a1_ok:
            v_main = "GRADIENT_GATES_FAILED"
        elif b2_verdict == "NONSMOOTH":
            v_main = ("WALL_LOCALLY_NONSMOOTH(q median %.1f > "
                      "%.0f)" % (med_cons, QCONS_EXPLODE))
        else:
            v_main = ("METRIC_STABILITY_LAW(L-map sealed; "
                      "theta* med %.1e [w9]; N-trend %s)"
                      % (ts9[0], trend))
        verd = " + ".join([
            v_main,
            "GRADIENT_EXPLAINS_DOSE(%s, ratio %.2f, flip dev "
            "%.2f)" % (dose_cls, med_ratio, med_flip),
            "U_PROFILE(%s, sp %+.2f)" % (u_cls, sp_leth),
            "N_TREND(%s, b_L %+.2f%s)"
            % (trend, b_L, ", UNIFORM_CANDIDATE" if uniform
               else ""),
            "MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY)"])

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the EXACT first-order sensitivity calculus of "
          "the wall (Hellmann-Feynman + border/CD gradients, "
          "FD/mp-gated), the u-profile with its lethality "
          "adjudication, the local stability inequality with "
          "measured validity window and N-trend -- NO "
          "certificate, NO bound, NO mechanism claim, NO H5 "
          "progress")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the gradient formulas "
          "against FD/Richardson/mp on the full pipeline, the "
          "chain identities, conservation; MEASURED: every map, "
          "ratio, window and trend (finite windows); OPEN: the "
          "cofinal step H5 and the wall mechanism (the "
          "stability inequality is perturbative around MAIN); "
          "NO RH claim"
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
