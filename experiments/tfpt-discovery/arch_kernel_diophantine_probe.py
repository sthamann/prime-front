#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arch_kernel_diophantine_probe -- PRIME.PORT.LSTAR.
ARCH_KERNEL_DIOPHANTINE_ANATOMY.01 (round 289): the four reviewer
questions on the r288 finding that the destructive ARCH coherence
sits in HYPER-FINE alignments ~200x below the phase resolution
(z_v flips at dose 0.005 while the phase field turns 0.24/dose).
STRICT RELEVANCE TEST ONLY: no proof attack, NO Baker/Matveev
APPLICATION (documentation of the needed strength only); the round
ends in EXACTLY ONE of three sealed verdicts: METRIC_ONLY /
DIOPHANTINE_SIGNAL / NEITHER.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

CONSTRUCTION CLARIFICATION (from rh/problem/lstar_problem.tex,
settled FIRST): every atom of (mu, nu) sits ON the fold grid
x_j = cos(2 pi j / L) -- the POSITION is grid-quantized; the
arithmetic lives in the WEIGHT profile w_j ~ (1-x_j) f(theta_j).
The lag vector c_i is assembled from tents t_Delta(i Delta - u)
at the comb centers u = log n: each center splits its mass onto
the TWO neighboring lag nodes i0 = floor(u/Delta), i0+1 with
weights (1 - frac) and frac, frac = {u/Delta} -- the TENT-SPLIT
FRACTIONS are the ONLY place where sub-grid information of the
source enters the weights (identity-gated below).  On w9 the
grid is COMMENSURATE with log 2 (Delta = log 2 / 46, r278): the
fractions are frac_j = {46 log2 n_j}; the whole 2-power family
sits exactly ON nodes (frac 0), and fraction DIFFERENCES are the
linear forms {46 log2(n/m)}.

INDEX FIREWALL (binding, r238-r288 discipline): w = window (kz),
S = #union entries, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2, n =
chain degree, k = kernel degree index, j = comb atom index, f =
fold index; ground truth (minC, crossings, z_v records) enters
GATES and record tables only; the sealed twin constructors
consume comb positions + weights + grid geometry + seed ONLY
(AST scope audit); no zero/prime oracles anywhere (AST firewall;
atom identities n_j = round(exp(u_j)) via the r254 world-blind
integer-root extraction ODG.base_exp).  MACHINERY IMPORTED
VERBATIM: r288 DC.{zv_block, balance_terms, balance_by_class,
band_split, pair_label_classes, jitter_folds, jacobi_zeros,
phase_field, phase_stats, circ_dist, local_gaps}, r284 LS.{
world_pack, spectral_block, atom_labels, dist_rule}, r283 FS.{
mu_chain_f64, b_matrix_f64, mu_chain_mp, b_matrix_mp}, r278 MS.{
ctx_build, grad_pack, pert_rows, pred_dlg, dlg_measured}, r276
MF.{window_ctx, pert_jit, conserve_comb, nf_from_comb}, r280
BL.sign_chain_f64, v881 PIK.{build_rung, grid_density,
folded_measure, lambda_eps}, r243 PB.smooth_comb, r254
ODG.base_exp, paircorr PC.{Grid, gen_model}, v563 core.{
build_window, atom_lags_at, arch_lags} READ-ONLY.

Q1 -- WHICH EXACT KERNEL TERM CARRIES THE FLIP: the source-frame
interference X_v = sum_{a<b} 2 u_a u_b E_ab (u = sqrt(v)/||.||)
decomposes EXACTLY over kernel degrees k (the CD sum: E_ab =
sum_k B_ak B_bk = sum_k v-dressed pihat_k(y_a) pihat_k(y_b)/h_k):
X_v(k) = (u^T B_k)^2 - sum_a u_a^2 B_ak^2, sum_k X_v(k) == X_v
(identity gate).  BASE MAP (w9, crossing 185 + fixed degree
N_w = 184): degree-band shares of X_v over the sealed bands
(fractions of the degree window: 0-25 / 25-50 / 50-75 / 75-95 /
95-100 pct) for ALL pairs and for the frozen r288 CARRIER SET
(fold band 3-4, ARCH-ARCH, T < 0 at the crossing) -- do the
terminal degrees carry?  DOSE 0.005 (r288 union machinery
VERBATIM, seeds 288000/288001, weights bitwise, order preserved;
regression: depth 0.71, z_v +0.17, dphi 0.001): at the FIXED
degree 184 (source frame identical -- weights bitwise) the
per-band changes |dX_b|/G_0 and the scale term |X_d/G_d -
X_d/G_0| are measured; SENSITIVE FACTOR (sealed naming rule) =
the largest of these six terms (med over reps); O(1) criterion:
max term >= 0.5 z-units while med |dphi| <= 0.01.

Q2 -- THE SUB-GAP ATTRIBUTION (three sealed candidates):
(i) TENT-SPLIT FRACTIONS frac_j = {u_j/Delta}: COMPLETENESS
  identity (the lag vector depends on the source exactly through
  (cell, frac, mass): two-node reconstruction c[i0] -=
  m/2 (1-frac), c[i0+1] -= m/2 frac equals core.atom_lags_at to
  1e-12, reflection branch gated inactive, on-node census
  disclosed); ANALYTIC CHAIN frac -> weights -> kernel terms:
  d(anything)/d frac_j = Delta * d/du_j with the exact r278
  Hellmann-Feynman gradients d log h_n/du_j (grad_pack imported
  verbatim; one FD re-gate at the hottest off-node atom,
  Richardson steps 1e-5/1e-6, bar 2e-3); 0.005-SENSITIVITY
  (comb channel, MF.pert_jit theta = 0.005 x 3 pinned reps,
  seeds 289000+): measured d log h_n vs first-order prediction
  (band 1e-3..0.5), terminal |dlg|, wall depth, z_v at own
  crossing, and the phase side med |dphi| (positions are
  GRID-FROZEN in this channel -- the dose acts through the
  weights alone); the 200x ACCOUNT: dose_flip = 1/max_n L1_n
  (linear flip criterion) vs dose_quarter = 0.25/(med dphi /
  theta); candidate explains the discrepancy iff
  dose_quarter/dose_flip >= 100.
(ii) FRACTION DIFFERENCES between slots: INCOMPLETENESS gate --
  a global fraction shift +1/4 mod 1 (cells kept, ALL pairwise
  differences preserved) must change the lag vector by >= 0.1
  rel: differences alone underdetermine the weights (LOUD).
(iii) EXACT WEIGHT DIFFERENCES of the ARCH slots: typed
  DOWNSTREAM_COMPLETE -- the folded weight vector carries the
  chain exactly (r278 eta ward <= 1e-9 re-gated) but lives
  POST-fold; the source-side sub-gap coordinate remains (i).
SEALED ADJUDICATION: SUBGAP_CARRIER = TENT_SPLIT_FRACTIONS iff
(i) completeness + FD gates pass AND the 200x account reaches
ratio >= 100; else SUBGAP_CARRIER_NOT_SEALED(values).

Q3 -- THE LINEAR FORMS (documentation, no proof attack):
commensurability gate |46 Delta / log 2 - 1| <= 1e-12; fraction
census (on-node = 2-power family, exact zero differences =
resonant pairs, counted); ATTRIBUTION: one-sided FD (e = 1e-6,
kink-guarded) of the carrier interference X_carrier at fixed
degree 184 through the full pipeline -> per-atom sensitivity
A_j = g_j |dX/du_j| -> top-6 atoms; the linear forms {46
log2(n/m)} of the top pairs DOCUMENTED with their distances to
the nearest integer; smallest nonzero circular fraction-
difference distance over ALL comb pairs (MEASUREMENT_ONLY).
NEED CALCULATION (DOCUMENTATION_ONLY): the measured flip dose
0.005 needs fraction structure resolved at c_need = 0.005 x
med(gap)/Delta; a family-uniform proof would need |{2 alpha/
(Delta log 2) * log2(n/m)}| >= c_need ~ 1/poly(M) while
Baker/Matveev-class two-log bounds deliver exp(-C (log H)^2
(log A)^2) with C >= 24 -- the needed vs delivered exponents are
computed and documented; NO bound is applied.  PAIRCORR HONESTY
(binding): every fraction statistic is typed MEASUREMENT_ONLY
and FORBIDDEN AS A PROOF PREMISE; the sealed r281 distance rule
types the fraction detectors K_F1 (min nonzero circular pair
distance) and K_F2 (circular resultant) over MAIN + EPST/SCR/
SMOOTH/HL2.

Q4 -- THE ARITHMETIC TWIN (the executioner; sealed family):
(a) RATIONAL TWIN (1 world, deterministic): every u_j/Delta is
  replaced by its first continued-fraction convergent p/q with
  |u_j/Delta - p/q| <= 1e-8 g_j / Delta (position change <
  1e-8 x local gap -- coarser than NOTHING for any continuous
  statistic at the measured dose scales, but every exact
  log-linear-form relation is replaced by a small-denominator
  rational relation: diophantine input TRIVIALIZED).  GATES:
  weights bitwise, |du| <= 1e-8 g, cells preserved, on-node
  atoms preserved, max denominator <= 1e6 (census).  MP WARD
  (dps 60, the boundary case): rho_184 < 1 < rho_185 and
  sign X_v(crossing) == f64 on the rational twin.
(b) JITTER LADDER (reference, comb channel MF.pert_jit,
  conservation exact): doses (1e-4, 3e-4, 1e-3, 3e-3, 5e-3,
  1e-2) x 2 pinned reps (seeds 289300+), log-staggered around
  the 0.005 threshold; r276 DOSE ANCHOR: theta = 0.02 with the
  EXACT r276 seeds must reproduce the record depth med 0.250.
(c) SHUFFLE TWIN (3 reps, seeds 289200+): the tent-split
  fractions PERMUTED among the atoms (cells bitwise, fraction
  multiset bitwise <= 1e-9, weights bitwise -- the fraction
  DISTRIBUTION preserved exactly, the assignment/relations
  destroyed); effective metric dose theta_eff = med |du|/g
  disclosed and referenced against the ladder.
MEASURED per twin world: depth s = minC/N_w, crossing, z_v,
C_off, fold-band 3-4 signed share, ARCH-ARCH share, terminal
degree-band share (95-100 pct) of X_v, K_F2 of its fractions.
SEALED THREE-WAY VERDICT (exactly one):
  METRIC_ONLY iff RATIONAL_KEEPS := (minC == 184 AND crossing
    == 185 AND z_v < 0 AND |z_v - z_v_MAIN| <= 0.05 AND band
    3-4 share < 0 AND AA share < 0) -- the exact log relations
    are irrelevant on every tested scale >= 1e-8 gap; Baker
    unnecessary; the shuffle outcome is reported as
    metric-dosed context.
  DIOPHANTINE_SIGNAL iff NOT RATIONAL_KEEPS AND SHUFFLE_LOSES
    := (med z_v > 0 OR med s < 0.90) AND the ladder KEEPS at
    the largest ladder dose <= theta_eff (med z_v < 0 AND med
    s >= 0.90) -- loss only when relations break, not
    explainable by matched metric dose; then the Q3
    documentation is the handover.
  NEITHER otherwise (honest, with anatomy).

WARDS / MUST-FAILS (each loud): w9 regression gated against the
r283/r284/r285/r288 records (S = 367/263/104, N_w = 184, minC
184, crossing 185, margin 1.68e-4 rel 0.01, z_v -3.149 tol
0.02, C_off -0.1046 tol 0.005, band 3-4 share -0.105 tol 0.01,
AA -0.056 tol 0.01); helper consistency (the twin measurement
helper reproduces the base records exactly); r288 dose anchor
(dose 0.005, seeds 288000+: depth med 0.71 tol 0.02, z_v med
+0.17 tol 0.05, dphi <= 0.003); r276 dose anchor (theta 0.02,
seeds exact: depth med 0.250 tol 0.005); channel identity (the
attribution fold channel reproduces ctx darm BITWISE at dose
zero); degree-band sum identities (rel 1e-10); mp (dps 60) on
the rational twin; exact toys (t1 hand tent split c[1] = -0.5 =
c[2] at frac 1/2 and the frac-linearity hand values; t2
continued fractions: 1/2, pi -> 333/106 at tol 1e-4, 46 -> 46/1;
t3 hand 2x3 degree decomposition sums exactly; t4 hand shuffle
conservation).  MUST-FAILS: (m1) MASS TWIN -- a twin scaling one
weight by 1.15 must be CAUGHT by the bitwise weight gate; (m2)
WRONG-DELTA FRACTIONS -- tent splits computed with Delta/2 must
break the reconstruction identity by >= 0.1 rel (LOUD); (m3)
DROPPED-BAND DECOMPOSITION -- dropping the largest |share|
degree band must break the sum identity by >= 0.01 of sum|T|
(LOUD); (m4) a twin oriented by the withheld crossing is
FLAGGED by the AST scope audit.  STOP LIST (anti-gates,
binding): NO L* claim, NO bound mechanism, NO Baker/Matveev
APPLICATION (need documentation only), NO asymptotic law, NO
derived 5/7, NO equidistribution premise, NO posthoc window,
NO RH claim; r243..r288 stand.

SEALED CONSTANTS: MAIN window 9; DEPTH_PAD 6; EXT 8 / EXT2 32;
CROSS_REC 185; MINC_REC 184; S_REC (367, 263, 104); MARGIN_REC
1.68e-4 rel 0.01; ZV_REC -3.149 tol 0.02; COFF_REC -0.1046 tol
0.005; B34_REC -0.105 tol 0.01; AA_REC -0.056 tol 0.01;
DEG_BANDS ((0, .25), (.25, .5), (.5, .75), (.75, .95),
(.95, 1.0001)); FIXED_DEG = N_w; DOSE_CRIT 0.005; SEED_R288
288000; UREPS 2; ZV_DOSE_REC +0.17 tol 0.05; S_DOSE_REC 0.71
tol 0.02; DPHI_DOSE_BAR 0.003; O1_BAR 0.5; PHASE_STILL 0.01;
RECON_TOL 1e-12; SUM_TOL 1e-10; FD_STEPS (1e-5, 1e-6) bar 2e-3;
SEED_C2 289000 / C2_REPS 3; DLG_BAND (1e-3, 0.5); RATIO_BAR
100; QUARTER 0.25; COMM_BAR 1e-12; ONNODE_EPS 1e-6; ATT_E 1e-6;
TOPK 6; RAT_TOL 1e-8; QMAX 1e6; RAT_DZV 0.05; SEED_SH 289200 /
SH_REPS 3; LADDER (1e-4, 3e-4, 1e-3, 3e-3, 5e-3, 1e-2) x
LAD_REPS 2, SEED_JL 289300; R276_SEEDS (386000, 387000, 388000)
theta 0.02 depth REC 0.250 tol 0.005; NEAR 0.90; FRAC_MULTISET
TOL 1e-9; WARD_DPS 60; M1_BAR bitwise; M2_BAR 0.1; M3_BAR 0.01;
runtime <= 1800 s; smoke = toys + firewall + scopes + mutants +
w9 f64 regression + base degree map + Q2 completeness identity
(doses, twins, ladder, gradients, attribution, detectors, mp,
adjudication skipped).  PRE-SPEC SCOPING (disclosed): every
record number above is a published r276/r278/r283/r284/r285/
r288 record adopted as-is; the degree bands, the twin
constructions, the three candidates, the need-calculation
convention and the three-way verdict rule were fixed at design
time from the r288 carrier map and the lstar_problem
construction; no machinery pass preceded this spec except
record reading; no bar, band or rule was tuned after any
evaluation of this probe.

DISCLOSED CALIBRATION AMENDMENTS (found in calibration pass 1,
BEFORE the record freeze; no physics bar, band, twin
construction, decomposition or verdict rule moved):
(a1) SHUFFLE GATE NODE SNAP: when the permutation assigns an
  exact on-node fraction (0.0), the gate-side RE-split
  floor(u'/Delta) can round the cell down by one (frac
  1 - 5.7e-14) -- an f64 floor artifact at exact nodes; the
  constructed world is exact (u' = (cell + frac) Delta
  bitwise).  The conservation gate now canonicalizes the
  re-split (frac > 1 - 1e-9 -> (cell+1, frac-1)).  A
  measurement-domain fix on a ward; the twin construction,
  every bar and the verdict rule never moved.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] METRIC_ONLY(rational twin values, shuffle
    context) / DIOPHANTINE_SIGNAL(twin table, ladder reference,
    Q3 handover) / NEITHER(anatomy)
  + SENSITIVE_FACTOR(name, delta in z-units, dphi) [always]
  + SUBGAP_CARRIER(TENT_SPLIT_FRACTIONS / NOT_SEALED; gates;
    200x account) [always]
  + LINEAR_FORMS(top pairs, min distance, resonance census,
    need vs Baker documentation) [always]
  + TWIN_TABLE(per-twin measures + conservation) [always]
  + DETECTOR_LEDGER [always].
Honesty before beauty: the degree map, the twin outcomes and
the fraction statistics are MEASUREMENTS on finite windows; the
need calculation is a documentation of proof requirements, not
a bound; no verdict claims L*, a bound mechanism, a derived 5/7
or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 41/41 (0.2 s); calibration
pass 1 = first full evaluation = 40/42 exposing amendment a1
(the shuffle-gate node snap -- an f64 floor artifact on a WARD,
no physics bar, twin construction, band or verdict rule moved);
pass 2 = 42/42, wall 2.1 s = the record run; the record-table
insertion below is the only post-freeze edit, which IS the
protocol; run1/run2 identical up to WALL):
CAL_VERDICT = METRIC_ONLY(the rational twin KEEPS the full
signature: minC 184, crossing 185, z_v -3.149 == MAIN, C_off
-0.1046, band 3-4 -0.105, AA -0.056, terminal share -0.99 --
every printed record IDENTICAL to MAIN while every exact
log-relation is replaced by a small-denominator rational;
shuffle context: theta_eff 0.12, depth 0.212, the ladder at
0.01 already loses) + SENSITIVE_FACTOR(sealed rule: band
50-75pct, 0.01 z-units -- O(1) criterion NOT MET at fixed
degree: see reading) + SUBGAP_CARRIER(NOT_SEALED: completeness
4.2e-14 PASS, gradient chain 3.1e-07 PASS, 200x account 29x <
bar 100) + LINEAR_FORMS(top pairs (3/7) 0.2301 / (3/25) 0.2909
/ (3/8) 0.0917 / (3/29) 0.4411 / (3/17) 0.1150 / (7/25) 0.4791;
min nonzero distance 1.339e-06 at (181, 241); 28 exact 2-power
resonances; need c 0.009) + TWIN_TABLE + DETECTOR_LEDGER(K_F1 /
K_F2 both WORLD_BLIND).
Key numbers.  Q1 BASE DEGREE MAP (crossing 185, z-units X_b/G):
all pairs +3.54 / -0.31 / -3.17 / -2.22 / -0.99 over the bands
0-25/25-50/50-75/75-95/95-100 pct; frozen carrier set (38 of
5356 pairs, X_carr -0.0242) 0.95 / -0.58 / -2.48 / +0.14 /
+0.50; last-2 degrees +0.17 -- the destructivity is carried by
the MID band 50-75 pct, NOT by the terminal degrees.  DOSE
0.005 (r288 seeds, anchor reproduced: depth 0.71, z_v +0.17,
dphi 0.0012): at FIXED degree 184 with the frame held, ALL six
sensitive-factor terms are <= 0.01 z-units -- no fixed-degree
kernel component moves O(1); the O(1) mover is the CROSSING
RELOCATION itself (185 -> ~131: the pivot cascade of the
chain), i.e. the flip is carried by WHERE the kernel crosses 1,
not by a static band reweighting (READING, typed MEASUREMENT).
Q2: candidate (i) tent-split fractions -- completeness 4.2e-14
(the lag vector factors EXACTLY through (cell, frac, mass); the
only sub-grid entry point), candidate (ii) differences
underdetermine (global shift changes lags by 0.80 rel LOUD),
candidate (iii) DOWNSTREAM_COMPLETE (eta ward 1.5e-13,
post-fold); gradient chain d/dfrac = Delta d/du exact (FD
re-gate 3.1e-07); COMB channel at 0.005 (positions GRID-FROZEN,
dose acts on the weights alone): depth 0.30, z_v +6.05,
terminal |dlg| 0.47 = O(1), pred/meas 0.31, dphi 0.0067 -- the
weight channel moves the terminal chain O(1) while the phase
barely responds; 200x ACCOUNT: flip dose 1/L1max = 0.0064 vs
quarter-turn 0.19 -> 29x < sealed bar 100 (the comb-channel
zeros co-move LESS than in the union channel: turn rate 1.34
vs 0.24/dose) -- carrier attribution honest NOT_SEALED at the
sealed bar; the fraction channel is real (29x) but the r288
200x was a union-channel statement.  Q3: Delta = log 2 / 46
EXACT (dev 0.0); fractions frac_j = {46 log2 n_j}; 8/70 atoms
on-node (the 2-power family) => 28 EXACT resonances {46 log2
2^(a-b)} = 0 INSIDE the window; smallest nonzero distance
1.339e-06 at (181, 241); attribution top atoms n = 3, 7, 25,
8, 29, 17 (the small primes carry, consistent with the r278
bottom-loaded u-profile); NEED (DOCUMENTATION_ONLY): flip dose
0.005 needs fraction structure at c_need = 0.009 (exponent
~8.9 in u-units) -- Baker/Matveev-class two-log bounds deliver
exponent ~7e4: ~7900x weaker; finite instances are decided by
direct evaluation, diophantine input only matters for the
UNBOUNDED family; detectors K_F1/K_F2 WORLD_BLIND (EPST shares
MAIN's positions by construction, disclosed).  Q4 TWIN TABLE
(w9): MAIN s 1.000 cross 185 z_v -3.149 b34 -0.105 AA -0.056;
RATIONAL (dens med 5408 / max 56801, max |du| 2.1e-09,
conservation exact, mp dps-60 ward: rho_184 = 0.99983248 < 1 <
1.00003660 = rho_185, sign X_v == f64) s 1.000 cross 185 z_v
-3.149 b34 -0.105 AA -0.056 K_F2 0.056 -- IDENTICAL records;
SHUFFLE r0/r1/r2 (cells + fraction multiset + weights exact,
theta_eff 0.18/0.12/0.12) s 0.201/0.212/0.239 cross 38/40/45
z_v +4.35/+6.98/+4.14 b34 +0.14/+0.18/+0.16 -- total loss, all
records control-like; LADDER (comb, conservation exact, r276
anchor 0.250 == record at theta 0.02): depth med 1.00 / 1.00 /
1.00 / 0.37 / 0.40 / 0.25 and z_v med -3.15 / -3.32 / -3.34 /
+5.26 / +4.72 / +6.81 at theta 1e-4 / 3e-4 / 1e-3 / 3e-3 /
5e-3 / 1e-2 -- the METRIC THRESHOLD of the coherence sits
between 1e-3 and 3e-3 of the local gap; the shuffle's
theta_eff 0.12 is ~50x beyond it: its loss is fully
metric-explained.  READING (typed): the r288 hyper-fine
alignment is a METRIC precision scale (~1e-3 of the local gap
in the tent-split fractions), not a number-theoretic
exactness: destroying every exact log-relation at position
cost 2e-9 changes NOTHING (mp-confirmed at the 1.7e-4 margin),
while metrically matched fraction randomization at 0.12 gap
kills the wall exactly as the plain jitter ladder predicts --
Baker-class nonresonance input is UNNECESSARY on all tested
scales; what a proof needs from the source is the fraction
PROFILE at ~1e-3-gap metric precision (the open center H5 /
L* stands untouched).  MUST-FAILS: m1 CAUGHT; m2 rel 0.60
LOUD; m3 0.118 LOUD; m4 FLAGGED; constructors + fragment audit
CLEAN.  Runtime 2.1 s full / 0.2 s smoke; run1/run2 identical
up to WALL.  AMENDMENTS AFTER FREEZE: NONE (records inserted
per protocol; no bar, band, class rule or verdict rule moved).

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

import destructive_coherence_probe as DC           # noqa: E402 r288
import lstar_two_measure_probe as LS               # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import budget_localization_probe as BL             # noqa: E402 r280
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import offdiag_gram_probe as ODG                   # noqa: E402 r254
import paircorr_margin_probe as PC                 # noqa: E402
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

MAIN_KZ = 9
DEPTH_PAD = 6
EXT = 8
EXT2 = 32
CROSS_REC = 185
MINC_REC = 184
S_REC = (367, 263, 104)
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
ZV_REC = -3.149
ZV_TOL = 0.02
COFF_REC = -0.1046
COFF_TOL = 0.005
B34_REC = -0.105
B34_TOL = 0.01
AA_REC = -0.056
AA_TOL = 0.01
DEG_BANDS = ((0.0, 0.25), (0.25, 0.5), (0.5, 0.75),
             (0.75, 0.95), (0.95, 1.0001))
DOSE_CRIT = 0.005
SEED_R288 = 288000
UREPS = 2
ZV_DOSE_REC = 0.17
ZV_DOSE_TOL = 0.05
S_DOSE_REC = 0.71
S_DOSE_TOL = 0.02
DPHI_DOSE_BAR = 0.003
O1_BAR = 0.5
PHASE_STILL = 0.01
RECON_TOL = 1e-12
SUM_TOL = 1e-10
FD_STEPS = (1e-5, 1e-6)
FD_BAR = 2e-3
SEED_C2 = 289000
C2_REPS = 3
DLG_BAND = (1e-3, 0.5)
RATIO_BAR = 100.0
QUARTER = 0.25
COMM_BAR = 1e-12
ONNODE_EPS = 1e-6
ATT_E = 1e-6
TOPK = 6
RAT_TOL = 1e-8
QMAX = 1e6
RAT_DZV = 0.05
SEED_SH = 289200
SH_REPS = 3
LADDER = (1e-4, 3e-4, 1e-3, 3e-3, 5e-3, 1e-2)
LAD_REPS = 2
SEED_JL = 289300
R276_SEEDS = (386000, 387000, 388000)
R276_THETA = 0.02
R276_DEPTH_REC = 0.250
R276_DEPTH_TOL = 0.005
NEAR = 0.90
FRAC_MS_TOL = 1e-9
WARD_DPS = 60
M2_BAR = 0.1
M3_BAR = 0.01
HL2_SEED = 101

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
    return (not bad), ("NO zero/prime oracles; atom identities via "
                       "round(exp(u)) + the r254 integer-root "
                       "extraction; the twin constructors consume "
                       "comb positions + weights + grid geometry + "
                       "seed ONLY; record numbers enter gates and "
                       "record tables only"
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


CONSTRUCTORS = ("frac_split", "best_rational", "twin_rational",
                "twin_shuffle", "fold_world")
SCOPE_FORBIDDEN = {"minC", "minC_true", "cross_true", "nf", "sg_h",
                   "ZV_REC", "CROSS_REC", "ZV_DOSE_REC", "zv"}


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
def frac_split(uu, Dg):
    """exact (cell, fraction) split of the tent centers on the
    lag grid: i0 = floor(u/Delta), frac = u/Delta - i0 -- the
    only sub-grid coordinate of the source (consumes positions
    + grid spacing ONLY)."""
    x = np.asarray(uu, float) / float(Dg)
    i0 = np.floor(x).astype(np.int64)
    return i0, x - i0


def best_rational(x, tol):
    """first continued-fraction convergent p/q of x >= 0 with
    |x - p/q| <= tol (deterministic; the small-denominator
    rational replacement of the RATIONAL twin)."""
    a0 = int(math.floor(x))
    p0, q0 = 1, 0
    p1, q1 = a0, 1
    if abs(x - p1) <= tol:
        return p1, 1
    y = x - a0
    for _ in range(64):
        if y <= 1e-15:
            break
        y = 1.0 / y
        a = int(math.floor(y))
        y -= a
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        if abs(x - p1 / q1) <= tol:
            break
    return p1, q1


def twin_rational(uu, mm, gaps, Dg, tol_gap):
    """RATIONAL TWIN: u_j -> (p_j/q_j) Delta with p/q the first
    CF convergent of u_j/Delta at |u/Delta - p/q| <= tol_gap
    g_j/Delta (position change < tol_gap x local gap; weights
    untouched by construction).  Returns (u', m', dens, du)."""
    u = np.asarray(uu, float)
    g = np.asarray(gaps, float)
    u2 = np.empty_like(u)
    dens = np.empty(len(u), np.int64)
    for j in range(len(u)):
        p, q = best_rational(u[j] / Dg, tol_gap * g[j] / Dg)
        u2[j] = (p / q) * Dg
        dens[j] = q
    return u2, np.asarray(mm, float).copy(), dens, u2 - u


def twin_shuffle(uu, mm, Dg, seed):
    """SHUFFLE TWIN: the tent-split fractions permuted among the
    atoms, cells fixed: u'_j = (i0_j + frac_{pi(j)}) Delta --
    fraction multiset and cells preserved exactly, the
    assignment (all log-relations) destroyed; weights untouched
    by construction."""
    i0, fr = frac_split(uu, Dg)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(len(fr))
    u2 = (i0.astype(float) + fr[perm]) * float(Dg)
    return u2, np.asarray(mm, float).copy(), perm


def fold_world(u2, m2, c_ar, alpha, M, L):
    """the sealed comb->lag->fold channel at explicit positions
    (identical to PIK.build_rung internals; identity-gated
    bitwise at dose zero): returns (d, xp, wp, fp, xn, vn, fn)."""
    c_at, _D = core.atom_lags_at(alpha, M, u2, m2)
    d = PIK.grid_density(c_ar + c_at)
    xp, wp, fp = PIK.folded_measure(d, L, +1.0)
    xn, vn, fn = PIK.folded_measure(d, L, -1.0)
    return d, xp, wp, fp, xn, vn, fn


# ============== must-fail mutants
def mutant_mass_twin(mm):
    """m1 MUST-FAIL: a 'twin' scaling the largest weight by 1.15
    -- the bitwise weight conservation gate must CATCH it."""
    m2 = np.asarray(mm, float).copy()
    m2[int(np.argmax(m2))] *= 1.15
    return m2


def mutant_wrong_delta(uu, mm, Dg, M):
    """m2 MUST-FAIL: tent splits computed with Delta/2 (fractions
    against the WRONG grid) placed on the true node pair -- must
    break the reconstruction identity loudly."""
    c = np.zeros(M)
    i0, _f = frac_split(uu, Dg)
    _i2, f2 = frac_split(uu, Dg / 2.0)
    for j in range(len(uu)):
        if 0 <= i0[j] < M:
            c[i0[j]] -= mm[j] * 0.5 * (1.0 - f2[j])
        if 0 <= i0[j] + 1 < M:
            c[i0[j] + 1] -= mm[j] * 0.5 * f2[j]
    return c


def mutant_drop_band(prof, n):
    """m3 MUST-FAIL: a degree decomposition DROPPING the largest
    |share| band -- must break the exact sum identity loudly."""
    aggs = degband_agg(prof)
    bi = int(np.argmax(np.abs(aggs)))
    t = (np.arange(n) + 0.5) / n
    lo, hi = DEG_BANDS[bi]
    keep = ~((t >= lo) & (t < hi))
    return float(np.sum(np.asarray(prof)[keep])), bi


def mutant_cross_twin(uu, cross_true):
    """m4 MUST-FAIL: a 'twin' oriented by the withheld crossing
    -- the scope audit must FLAG this."""
    u2 = np.asarray(uu, float).copy()
    u2[cross_true % len(u2)] += 1e-6
    return u2


# ============== gate-side decomposition + measurement helpers
def deg_profile(B, n, u):
    """exact per-degree decomposition of the source-frame
    interference: X(k) = (u^T B_k)^2 - sum_a u_a^2 B_ak^2,
    sum_k X(k) == X (the CD sum over pihat_k pihat_k / h_k)."""
    Bn = B[:, :n]
    return (u @ Bn) ** 2 - (u * u) @ (Bn * Bn)


def carrier_profile(B, n, u, pa, pb):
    """per-degree contribution of a frozen pair set:
    sum_pairs 2 u_a u_b B_ak B_bk."""
    Bn = B[:, :n]
    return np.sum(2.0 * (u[pa] * u[pb])[:, None]
                  * Bn[pa] * Bn[pb], axis=0)


def degband_agg(prof):
    """sealed degree-band aggregation (fractions of the degree
    window)."""
    n = len(prof)
    t = (np.arange(n) + 0.5) / n
    out = []
    for lo, hi in DEG_BANDS:
        sel = (t >= lo) & (t < hi)
        out.append(float(np.sum(np.asarray(prof)[sel])))
    return out


def band_label(bi):
    lo, hi = DEG_BANDS[bi]
    return "%d-%dpct" % (int(round(lo * 100)),
                         int(round(min(hi, 1.0) * 100)))


def pair_geom(W, D9):
    """fold-band index + label-pair classes of one world's nu
    pairs (r288 conventions verbatim)."""
    iu = np.triu_indices(W["Sm"], 1)
    dist = np.abs(np.asarray(W["fn"])[iu[0]]
                  - np.asarray(W["fn"])[iu[1]])
    bidx = DC.band_split(dist)
    lab = LS.atom_labels(W["fn"], D9, W["uu"], W["mm"])
    cls = DC.pair_label_classes(lab, iu)
    return iu, bidx, cls


def comb_world_measure(u2, m2, D9, base=None):
    """gate-side measurement bundle of one comb world: depth,
    crossing, z_v/C_off, fold-band 3-4 + AA signed shares,
    terminal degree-band share, fraction resultant."""
    ctx = MS.ctx_build(MAIN_KZ, comb=(np.asarray(u2, float),
                                      np.asarray(m2, float)))
    W = LS.world_pack("tw", ctx, D9)
    N = W["N"]
    mc = W["minC"]
    s = 1.0 if mc is None else mc / N
    dep = min(max(N + DEPTH_PAD, (mc or N) + 2), W["Sp"] - 1)
    SP = LS.spectral_block(W, dep)
    nc = SP["cross"]
    out = dict(W=W, SP=SP, s=s, minC=mc, cross=nc,
               zv=float("nan"), coff=float("nan"),
               b34=float("nan"), aa=float("nan"),
               term=float("nan"))
    if nc is not None and nc <= dep:
        zb = DC.zv_block(SP["B"], nc, W["vn"])
        iu, bidx, cls = pair_geom(W, D9)
        bands, classes = DC.balance_by_class(zb["T"], bidx, cls)
        prof = deg_profile(SP["B"], nc, zb["uv"])
        aggs = degband_agg(prof)
        out.update(zv=zb["zv"], coff=zb["coff"], X=zb["X"],
                   G=zb["G"], b34=bands[1], aa=classes["AA"],
                   term=aggs[-1] / max(zb["G"], 1e-300))
    return out


def nu_phase_map(W, n):
    """phases of the nu atoms (fixed fold-grid positions) between
    the zeros of the mu-orthonormal P_n, keyed by fold index."""
    al, sb, _h0 = FS.mu_chain_f64(np.asarray(W["xp"], float),
                                  np.asarray(W["wp"], float), n)
    z = DC.jacobi_zeros(al, sb, n)
    phi, _c, _i = DC.phase_field(z, np.asarray(W["xn"], float))
    return {int(f): float(p) for f, p in zip(W["fn"], phi)}


def dphi_between(pm0, pm1):
    ks = [k for k in pm0 if k in pm1
          and math.isfinite(pm0[k]) and math.isfinite(pm1[k])]
    if not ks:
        return float("nan")
    d = DC.circ_dist(np.array([pm1[k] for k in ks]),
                     np.array([pm0[k] for k in ks]))
    return float(np.median(d))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("arch_kernel_diophantine_probe -- PRIME.PORT.LSTAR."
          "ARCH_KERNEL_DIOPHANTINE_ANATOMY.01 (round 289)")
    print("SPEC_SHA %s   (r288 DC %s / r284 LS %s / r278 MS %s)"
          % (SPEC_SHA[:16], DC.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             MS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 regression + base degree map + Q2 "
                        "completeness; doses, twins, ladder, "
                        "gradients, attribution, detectors, mp, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the degree bands, the exact "
          "degree decomposition, the three sub-gap candidates with "
          "their completeness/incompleteness gates, the 200x "
          "account convention, the linear-form documentation and "
          "need calculation (DOCUMENTATION_ONLY -- no Baker/"
          "Matveev application), the three twin constructions with "
          "conservation gates, the ladder reference, the mutants "
          "and the THREE-WAY verdict rule; every fraction "
          "statistic is typed MEASUREMENT_ONLY and forbidden as a "
          "proof premise; the STOP list forbids any L* claim and "
          "any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- TENT SPLIT, CONTINUED FRACTIONS, "
            "DECOMPOSITION, SHUFFLE")
    # t1: hand tent split (alpha 1, M 10 -> Delta 0.2)
    c_t, D_t = core.atom_lags_at(1.0, 10, np.array([0.3]),
                                 np.array([2.0]))
    c_t2, _D2 = core.atom_lags_at(1.0, 10, np.array([0.25]),
                                  np.array([2.0]))
    i0t, frt = frac_split(np.array([0.3, 0.25]), D_t)
    ok_t1 = (abs(D_t - 0.2) <= 1e-15
             and abs(c_t[1] + 0.5) <= 1e-12
             and abs(c_t[2] + 0.5) <= 1e-12
             and abs(c_t2[1] + 0.75) <= 1e-12
             and abs(c_t2[2] + 0.25) <= 1e-12
             and i0t[0] == 1 and abs(frt[0] - 0.5) <= 1e-12
             and abs(frt[1] - 0.25) <= 1e-12)
    check("G10-toy-tent-split", ok_t1,
          "HAND TENT (Delta = 0.2, m = 2): u = 0.3 (frac 1/2) -> "
          "c[1] = c[2] = -0.5 exact; u = 0.25 (frac 1/4) -> c[1] "
          "= -0.75, c[2] = -0.25 exact -- the lag vector is "
          "LINEAR in the fraction at fixed cell (dc[i0]/dfrac = "
          "+m/2, dc[i0+1]/dfrac = -m/2)")
    # t2: continued fractions
    ok_t2 = (best_rational(0.5, 1e-9) == (1, 2)
             and best_rational(math.pi, 1e-4) == (333, 106)
             and best_rational(46.0, 1e-9) == (46, 1))
    check("G11-toy-rational", ok_t2,
          "CONTINUED FRACTIONS: 1/2 exact; pi at tol 1e-4 -> "
          "333/106 (the first convergent within tolerance, err "
          "8.3e-5); integer 46 -> 46/1 -- the RATIONAL twin "
          "replacement is deterministic and minimal along the "
          "convergent ladder")
    # t3: hand 2x3 degree decomposition
    B_t = np.array([[1.0, 0.5, 0.25], [0.5, -0.5, 1.0]])
    u_t = np.array([0.6, 0.8])
    prof_t = deg_profile(B_t, 3, u_t)
    X_t = 2.0 * u_t[0] * u_t[1] * float(B_t[0] @ B_t[1])
    hand_t = 0.96 * np.array([0.5, -0.25, 0.25])
    ok_t3 = (float(np.max(np.abs(prof_t - hand_t))) <= 1e-14
             and abs(float(np.sum(prof_t)) - X_t) <= 1e-14)
    cp_t = carrier_profile(B_t, 3, u_t, np.array([0]),
                           np.array([1]))
    ok_t3 = ok_t3 and float(np.max(np.abs(cp_t - hand_t))) <= 1e-14
    check("G12-toy-decomposition", ok_t3,
          "HAND 2x3: per-degree X(k) = 0.96 x (0.5, -0.25, 0.25) "
          "exact by both routes (rank-1 identity and pair sum); "
          "sum == X = %.4f exact -- the CD-degree decomposition "
          "is an identity" % X_t)
    # t4: hand shuffle conservation
    uu_t = np.array([0.31, 0.47, 0.86])
    u2_t, m2_t, perm_t = twin_shuffle(uu_t, np.array([1.0, 2.0, 3.0]),
                                      0.2, 7)
    i0a, fra = frac_split(uu_t, 0.2)
    i0b, frb = frac_split(u2_t, 0.2)
    ok_t4 = (bool(np.array_equal(i0a, i0b))
             and float(np.max(np.abs(np.sort(fra)
                                     - np.sort(frb)))) <= 1e-12
             and bool(np.array_equal(m2_t,
                                     np.array([1.0, 2.0, 3.0]))))
    check("G13-toy-shuffle", ok_t4,
          "HAND SHUFFLE (3 atoms, Delta 0.2): cells bitwise, "
          "fraction multiset exact, weights bitwise -- the twin "
          "destroys only the assignment")

    # ---------------- S2 w9 regression
    section("S2  W9 -- REGRESSION AGAINST r283/r284/r285/r288")
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    ctx9 = MS.ctx_build(MAIN_KZ)
    W9 = LS.world_pack("w9", ctx9, D9)
    Nw = W9["N"]
    ok_src = (W9["S"], W9["Sp"], W9["Sm"]) == S_REC \
        and Nw == (W9["S"] + 1) // 2 and W9["minC"] == MINC_REC
    check("G20-w9-source", ok_src,
          "w9: S = %d (mu %d / nu %d), N_w = %d, minC = %s == %d "
          "(record)" % (W9["S"], W9["Sp"], W9["Sm"], Nw,
                        str(W9["minC"]), MINC_REC))
    depth9 = min(Nw + DEPTH_PAD, W9["Sp"] - 1)
    SP9 = LS.spectral_block(W9, depth9)
    margin9 = 1.0 - SP9["rho"][Nw]
    ok_cross = SP9["cross"] == CROSS_REC \
        and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
    check("G21-w9-crossing", ok_cross,
          "crossing %s == %d, margin %.4e (rec %.2e rel %.2f)"
          % (str(SP9["cross"]), CROSS_REC, margin9, MARGIN_REC,
             MARGIN_TOL))
    ZB9 = DC.zv_block(SP9["B"], CROSS_REC, W9["vn"])
    iu9, bidx9, cls9 = pair_geom(W9, D9)
    bands9, classes9 = DC.balance_by_class(ZB9["T"], bidx9, cls9)
    ok_carr = (abs(ZB9["zv"] - ZV_REC) <= ZV_TOL
               and abs(ZB9["coff"] - COFF_REC) <= COFF_TOL
               and abs(bands9[1] - B34_REC) <= B34_TOL
               and abs(classes9["AA"] - AA_REC) <= AA_TOL)
    check("G22-w9-carrier-map", ok_carr,
          "r288 CARRIER MAP reproduced at the crossing: z_v = "
          "%+.3f (rec %+.3f), C_off = %+.4f (rec %+.4f), band 3-4 "
          "signed share %+.3f (rec %+.3f), ARCH-ARCH %+.3f (rec "
          "%+.3f) -- the round's address"
          % (ZB9["zv"], ZV_REC, ZB9["coff"], COFF_REC, bands9[1],
             B34_REC, classes9["AA"], AA_REC))
    # frozen r288 carrier set (fold band 3-4, AA, T < 0)
    carr_sel = (bidx9 == 1) & (cls9 == "AA") & (ZB9["T"] < 0.0)
    pa9, pb9 = iu9[0][carr_sel], iu9[1][carr_sel]
    X_carr = float(np.sum(ZB9["T"][carr_sel]))
    info("frozen CARRIER SET: %d of %d pairs (fold 3-4, AA, "
         "destructive), X_carrier = %+.4f (%.2f of sum|T|), fold "
         "slots identity-mapped"
         % (int(np.sum(carr_sel)), len(ZB9["T"]), X_carr,
            X_carr / max(ZB9["A"], 1e-300)))
    # channel identity for the attribution route
    c_ar9 = np.asarray(core.arch_lags(ctx9["M"], D9), float)
    d0, xp0, wp0, fp0, xn0, vn0, fn0 = fold_world(
        ctx9["uu"], ctx9["mm"], c_ar9, ctx9["alpha"], ctx9["M"],
        ctx9["L"])
    ok_chan = bool(np.array_equal(d0, ctx9["darm"])) \
        and bool(np.array_equal(fn0, np.asarray(W9["fn"])))
    check("G23-channel-identity", ok_chan,
          "the attribution fold channel reproduces ctx darm "
          "BITWISE at dose zero (and the nu fold set exactly) -- "
          "fold_world is the sealed channel")

    # ---------------- S3 Q1 base degree map + dose 0.005
    section("S3  Q1 -- KERNEL-DEGREE ANATOMY OF THE FLIP")
    prof_cross = deg_profile(SP9["B"], CROSS_REC, ZB9["uv"])
    dev_sum = abs(float(np.sum(prof_cross)) - ZB9["X"]) \
        / max(abs(ZB9["X"]), 1e-300)
    prof_carr = carrier_profile(SP9["B"], CROSS_REC, ZB9["uv"],
                                pa9, pb9)
    dev_sum_c = abs(float(np.sum(prof_carr)) - X_carr) \
        / max(abs(X_carr), 1e-300)
    check("G30-degree-sum-identity", dev_sum <= SUM_TOL
          and dev_sum_c <= SUM_TOL,
          "sum_k X(k) == X_v exact (rel dev %.1e) and the carrier "
          "restriction sums exactly (rel dev %.1e, bar %.0e) -- "
          "the decomposition is the CD sum, nothing dropped"
          % (dev_sum, dev_sum_c, SUM_TOL))
    aggX = degband_agg(prof_cross)
    aggC = degband_agg(prof_carr)
    G0c = max(ZB9["G"], 1e-300)
    info("BASE degree-band map at the crossing (z-units X_b/G): "
         "all pairs %s; carrier %s; last-2 degrees %+0.3f / "
         "carrier %+0.3f"
         % (str({band_label(b): round(aggX[b] / G0c, 3)
                 for b in range(len(DEG_BANDS))}),
            str({band_label(b): round(aggC[b] / G0c, 3)
                 for b in range(len(DEG_BANDS))}),
            float(np.sum(prof_cross[-2:])) / G0c,
            float(np.sum(prof_carr[-2:])) / G0c))
    check("G31-base-degree-map", True,
          "MEASURED: the destructive X_v at the crossing is "
          "carried by degree band %s (all pairs %+.2f z-units) "
          "and the carrier set by %s (%+.2f); terminal band "
          "(95-100 pct) share %+.2f -- the question 'do the "
          "terminal degrees carry' is answered by this map"
          % (band_label(int(np.argmin(aggX))),
             min(aggX) / G0c,
             band_label(int(np.argmin(aggC))),
             min(aggC) / G0c, aggX[-1] / G0c))
    # fixed-degree base frame (weights bitwise under union jitter)
    E184 = SP9["B"][:, :Nw] @ SP9["B"][:, :Nw].T
    _dg0, _T0, X0_184, _p0, _n0, _A0, G0_184 = DC.balance_terms(
        E184, ZB9["uv"])
    prof0_184 = deg_profile(SP9["B"], Nw, ZB9["uv"])
    agg0_184 = degband_agg(prof0_184)
    prof0c_184 = carrier_profile(SP9["B"], Nw, ZB9["uv"], pa9, pb9)

    if smoke:
        for g in ("G32-r288-dose-anchor", "G33-sensitive-factor"):
            check(g, True, "SMOKE: skipped")
        sens_name, sens_val, dphi_u = "SKIPPED", float("nan"), \
            float("nan")
    else:
        # r288 union dose machinery VERBATIM (seeds pinned)
        x_all = np.concatenate([np.asarray(W9["xp"]),
                                np.asarray(W9["xn"])])
        f_all = np.concatenate([np.asarray(W9["fp"], np.int64),
                                np.asarray(W9["fn"], np.int64)])
        m_all = np.concatenate([np.asarray(W9["wp"]),
                                np.asarray(W9["vn"])])
        o_f = np.argsort(f_all)
        f_all, x_all, m_all = f_all[o_f], x_all[o_f], m_all[o_f]
        fn_set = set(int(f) for f in W9["fn"])
        numask = np.array([int(f) in fn_set for f in f_all])
        gaps_u = DC.local_gaps(f_all.astype(float))
        al9, sb9, h09 = FS.mu_chain_f64(np.asarray(W9["xp"]),
                                        np.asarray(W9["wp"]), Nw)
        z9 = DC.jacobi_zeros(al9, sb9, Nw)
        phi0_u, _c0u, _i0u = DC.phase_field(z9, x_all[numask])
        # nu-atom order in the sorted union == fold order of fn
        fn_sorted = np.sort(np.asarray(W9["fn"], np.int64))
        row_of = {int(f): r for r, f in enumerate(
            np.asarray(W9["fn"], np.int64))}
        remap = np.array([row_of[int(f)] for f in fn_sorted])
        uv_s = ZB9["uv"][remap]
        pa_s = np.searchsorted(fn_sorted,
                               np.asarray(W9["fn"],
                                          np.int64)[pa9])
        pb_s = np.searchsorted(fn_sorted,
                               np.asarray(W9["fn"],
                                          np.int64)[pb9])
        prof0_s = deg_profile(SP9["B"][remap], Nw, uv_s)
        rows_u = []
        for rep in range(UREPS):
            fj, xj, df = DC.jitter_folds(f_all, gaps_u, DOSE_CRIT,
                                         SEED_R288 + rep, W9["L"])
            ok_j = bool(np.all(np.abs(df)
                               <= DOSE_CRIT * gaps_u + 1e-15)
                        and np.all(np.diff(fj) > 0))
            wu_j = m_all * np.where(numask, -1.0, 1.0)
            sg_j, _l, _r = BL.sign_chain_f64(xj, wu_j, Nw + EXT)
            mc = next((n for n in range(len(sg_j))
                       if sg_j[n] < 0), None)
            if mc is None:
                sg_j, _l, _r = BL.sign_chain_f64(xj, wu_j,
                                                 Nw + EXT2)
                mc = next((n for n in range(len(sg_j))
                           if sg_j[n] < 0), None)
            crj = (mc + 1) if mc is not None else None
            xpj, wpj = xj[~numask], m_all[~numask]
            ynj, vnj = xj[numask], m_all[numask]
            dep = min(max(Nw, (crj or 1) + 1), len(xpj) - 1)
            alj, sbj, h0j = FS.mu_chain_f64(xpj, wpj, dep)
            Bj = FS.b_matrix_f64(alj, sbj, h0j, ynj, vnj, dep)
            rowd = dict(ok=ok_j, s=(mc / Nw if mc is not None
                                    else 1.0), cross=crj)
            if crj is not None and crj <= dep:
                rowd["zv"] = DC.zv_block(Bj, crj, vnj)["zv"]
            # fixed-degree comparison (weights bitwise -> uv_s)
            profd = deg_profile(Bj, Nw, uv_s)
            dgd, Td, Xd, _pd, _nd, _Ad, Gd = DC.balance_terms(
                Bj[:, :Nw] @ Bj[:, :Nw].T, uv_s)
            rowd["dband"] = [(bd - b0) / G0_184 for bd, b0
                             in zip(degband_agg(profd), agg0_184)]
            rowd["dscale"] = Xd / max(Gd, 1e-300) \
                - Xd / max(G0_184, 1e-300)
            profcd = carrier_profile(Bj, Nw, uv_s, pa_s, pb_s)
            rowd["dcarr"] = [(bd - b0) / G0_184 for bd, b0
                             in zip(degband_agg(profcd),
                                    degband_agg(prof0c_184))]
            zjw = DC.jacobi_zeros(alj, sbj, Nw)
            phij, _cj, _ij = DC.phase_field(zjw, ynj)
            both = np.isfinite(phij) & np.isfinite(phi0_u)
            rowd["dphi"] = float(np.median(DC.circ_dist(
                phij[both], phi0_u[both])))
            rows_u.append(rowd)
        s_med = float(np.median([r["s"] for r in rows_u]))
        zv_med = float(np.median([r["zv"] for r in rows_u
                                  if "zv" in r]))
        dphi_u = float(np.median([r["dphi"] for r in rows_u]))
        ok_anchor = (all(r["ok"] for r in rows_u)
                     and abs(s_med - S_DOSE_REC) <= S_DOSE_TOL
                     and abs(zv_med - ZV_DOSE_REC) <= ZV_DOSE_TOL
                     and dphi_u <= DPHI_DOSE_BAR)
        check("G32-r288-dose-anchor", ok_anchor,
              "r288 DOSE ANCHOR reproduced (dose %.3f, seeds "
              "%d+, weights bitwise): depth med %.2f (rec %.2f), "
              "z_v med %+.2f (rec %+.2f), dphi med %.4f (bar "
              "%.3f) -- the flip lives 200x below the phase "
              "resolution, re-derived"
              % (DOSE_CRIT, SEED_R288, s_med, S_DOSE_REC, zv_med,
                 ZV_DOSE_REC, dphi_u, DPHI_DOSE_BAR))
        terms = {}
        for b in range(len(DEG_BANDS)):
            terms["band " + band_label(b)] = float(np.median(
                [abs(r["dband"][b]) for r in rows_u]))
        terms["SCALE_G"] = float(np.median(
            [abs(r["dscale"]) for r in rows_u]))
        sens_name = max(terms, key=lambda k: terms[k])
        sens_val = terms[sens_name]
        carr_terms = {band_label(b): float(np.median(
            [r["dcarr"][b] for r in rows_u]))
            for b in range(len(DEG_BANDS))}
        ok_sens = sens_val >= O1_BAR and dphi_u <= PHASE_STILL
        check("G33-sensitive-factor", True,
              "SENSITIVE FACTOR at fixed degree %d (source frame "
              "identical, weights bitwise): %s changes by %.2f "
              "z-units (terms %s) while the phase field stands "
              "still (med dphi %.4f); carrier-set band deltas %s "
              "-- O(1) criterion (>= %.1f while dphi <= %.2f): %s"
              % (Nw, sens_name, sens_val,
                 str({k: round(v, 2) for k, v in terms.items()}),
                 dphi_u, str({k: round(v, 2)
                              for k, v in carr_terms.items()}),
                 O1_BAR, PHASE_STILL,
                 "MET" if ok_sens else "NOT MET (reported)"))

    # ---------------- S4 Q2 sub-gap attribution
    section("S4  Q2 -- SUB-GAP ATTRIBUTION (THREE CANDIDATES)")
    i0_9, fr_9 = frac_split(ctx9["uu"], D9)
    recon = np.zeros(ctx9["M"])
    for j in range(len(ctx9["uu"])):
        if 0 <= i0_9[j] < ctx9["M"]:
            recon[i0_9[j]] -= ctx9["mm"][j] * 0.5 * (1.0 - fr_9[j])
        if 0 <= i0_9[j] + 1 < ctx9["M"]:
            recon[i0_9[j] + 1] -= ctx9["mm"][j] * 0.5 * fr_9[j]
    c_at9, _D9b = core.atom_lags_at(ctx9["alpha"], ctx9["M"],
                                    ctx9["uu"], ctx9["mm"])
    dev_rec = float(np.max(np.abs(recon - c_at9))) \
        / max(float(np.max(np.abs(c_at9))), 1e-300)
    dist_node = np.minimum(fr_9, 1.0 - fr_9) * D9
    onnode9 = dist_node <= ONNODE_EPS * D9
    refl_ok = float(np.min(ctx9["uu"])) >= 2.0 * D9
    check("G40-frac-completeness", dev_rec <= RECON_TOL
          and refl_ok,
          "CANDIDATE (i) COMPLETENESS: the two-node "
          "reconstruction from (cell, fraction, mass) reproduces "
          "core.atom_lags_at to rel %.1e (bar %.0e); reflection "
          "branch inactive (min u >= 2 Delta); on-node census "
          "%d/%d (the 2-power family) -- the tent-split "
          "fractions are the ONLY sub-grid entry point of the "
          "source into the weights"
          % (dev_rec, RECON_TOL, int(np.sum(onnode9)),
             len(fr_9)))
    # candidate (ii): global fraction shift, differences kept
    fr_sh = (fr_9 + 0.25) % 1.0
    rec_sh = np.zeros(ctx9["M"])
    for j in range(len(ctx9["uu"])):
        if 0 <= i0_9[j] < ctx9["M"]:
            rec_sh[i0_9[j]] -= ctx9["mm"][j] * 0.5 \
                * (1.0 - fr_sh[j])
        if 0 <= i0_9[j] + 1 < ctx9["M"]:
            rec_sh[i0_9[j] + 1] -= ctx9["mm"][j] * 0.5 * fr_sh[j]
    dev_sh = float(np.max(np.abs(rec_sh - c_at9))) \
        / max(float(np.max(np.abs(c_at9))), 1e-300)
    check("G41-frac-diff-incomplete", dev_sh >= M2_BAR,
          "CANDIDATE (ii) INCOMPLETENESS: a global fraction "
          "shift +1/4 mod 1 (cells kept, ALL pairwise "
          "differences preserved) changes the lag vector by rel "
          "%.2f >= %.1f -- LOUD: fraction DIFFERENCES alone "
          "underdetermine the weights; they are a derived "
          "statistic of candidate (i)" % (dev_sh, M2_BAR))

    if smoke:
        for g in ("G42-gradient-fd-regate", "G43-comb-dose",
                  "G44-200x-account", "G45-carrier-adjudication"):
            check(g, True, "SMOKE: skipped")
        carrier_sealed = None
        ratio_200 = float("nan")
    else:
        pk9 = MS.grad_pack(ctx9)
        check("G42a-eta-downstream", pk9["eta_ward"] <= 1e-9,
              "CANDIDATE (iii) typing: eta_n == <wsig, q_n^2> at "
              "every degree (worst rel %.1e) -- the folded ARCH-"
              "slot weight vector is DOWNSTREAM_COMPLETE (post-"
              "fold); the source-side sub-gap coordinate remains "
              "candidate (i)" % pk9["eta_ward"])
        # FD re-gate at the hottest off-node atom
        offi = np.nonzero(~pk9["onnode"])[0]
        j_hot = int(offi[int(np.argmax(
            (pk9["gaps"] * np.abs(pk9["glogh"][:, Nw - 1]))[offi]))])
        allowed = [e for e in FD_STEPS
                   if e <= 0.25 * pk9["dists"][j_hot]]
        worst_fd = 0.0
        if len(allowed) >= 2:
            e_b, e_s = allowed[-2], allowed[-1]
            fd_b, _db = MS.fd_pair(ctx9, j_hot, e_b)
            fd_s, _ds = MS.fd_pair(ctx9, j_hot, e_s)
            r2 = (e_b / e_s) ** 2
            for n in (2 * Nw // 3, Nw - 1):
                if np.isfinite(fd_b[n]) and np.isfinite(fd_s[n]):
                    rich = fd_s[n] + (fd_s[n] - fd_b[n]) / (r2 - 1)
                    gan = pk9["glogh"][j_hot, n]
                    worst_fd = max(worst_fd, abs(rich - gan)
                                   / max(abs(gan), 1e-10))
        check("G42-gradient-fd-regate", worst_fd <= FD_BAR
              and len(allowed) >= 2,
              "the r278 Hellmann-Feynman gradient re-gated at the "
              "hottest off-node atom j = %d (Richardson %s): "
              "worst dev %.1e (bar %.0e) -- d(kernel term)/d frac "
              "= Delta x d/du is exact machinery calculus"
              % (j_hot, str(allowed), worst_fd, FD_BAR))
        # comb dose 0.005: weights-only channel
        pm0 = nu_phase_map(W9, Nw)
        crows = []
        cons_ok = True
        for rep in range(C2_REPS):
            u2, m2 = MF.pert_jit(ctx9["uu"], ctx9["mm"], DOSE_CRIT,
                                 SEED_C2 + rep, False)
            cons_ok = cons_ok and MF.conserve_comb(
                "P2_JIT", ctx9["uu"], ctx9["mm"], u2, m2,
                DOSE_CRIT)
            du = u2 - ctx9["uu"]
            rows2, nf2, _z2 = MS.pert_rows(ctx9, u2, m2)
            meas = MS.dlg_measured(pk9["rows"], rows2)
            pred = MS.pred_dlg(pk9["glogh"], pk9["gloghL"], du)
            m_ = np.isfinite(meas) & (np.abs(meas) >= DLG_BAND[0]) \
                & (np.abs(meas) <= DLG_BAND[1])
            ratio = float(np.median(pred[m_] / meas[m_])) \
                if np.any(m_) else float("nan")
            term_dlg = abs(meas[Nw - 1]) \
                if np.isfinite(meas[Nw - 1]) else abs(pred[Nw - 1])
            wm = comb_world_measure(u2, m2, D9)
            pm1 = nu_phase_map(wm["W"], Nw)
            crows.append(dict(ratio=ratio, term=term_dlg,
                              s=wm["s"], zv=wm["zv"],
                              dphi=dphi_between(pm0, pm1)))
        s_c = float(np.median([r["s"] for r in crows]))
        zv_c = float(np.median([r["zv"] for r in crows
                                if math.isfinite(r["zv"])]))
        dphi_c = float(np.median([r["dphi"] for r in crows]))
        term_c = float(np.median([r["term"] for r in crows]))
        ratio_c = float(np.median([r["ratio"] for r in crows]))
        check("G43-comb-dose", cons_ok,
              "COMB CHANNEL at theta = %.3f (positions of the "
              "atoms GRID-FROZEN -- the dose acts on the tent "
              "fractions/weights alone; conservation exact, %d "
              "reps): depth med %.2f, z_v med %+.2f, terminal "
              "|dlg| med %.2f = O(1), first-order pred/meas med "
              "%.2f, med dphi %.4f -- the kernel term moves O(1) "
              "through the WEIGHTS while the phase geometry "
              "barely responds"
              % (DOSE_CRIT, C2_REPS, s_c, zv_c, term_c, ratio_c,
                 dphi_c))
        L1max = float(np.max(pk9["L1"]))
        turn_c = dphi_c / DOSE_CRIT
        dose_flip = 1.0 / max(L1max, 1e-300)
        dose_quarter = QUARTER / max(turn_c, 1e-300)
        ratio_200 = dose_quarter / max(dose_flip, 1e-300)
        check("G44-200x-account", True,
              "THE 200x ACCOUNT (measured): linear flip dose "
              "1/max_n L1_n = %.4f (L1max %.0f, gap-relative) vs "
              "quarter-turn dose %.1f (comb-channel turn rate "
              "%.3f/dose) -> sensitivity ratio %.0fx (bar %.0f): "
              "the kernel-term channel through the tent-split "
              "fractions is %s orders below the phase resolution "
              "-- the r288 discrepancy is the WEIGHT channel, "
              "measured" % (dose_flip, L1max, dose_quarter,
                            turn_c, ratio_200, RATIO_BAR,
                            "2-3" if ratio_200 >= RATIO_BAR
                            else "NOT"))
        carrier_sealed = (dev_rec <= RECON_TOL
                          and worst_fd <= FD_BAR
                          and ratio_200 >= RATIO_BAR)
        check("G45-carrier-adjudication", True,
              "SEALED ADJUDICATION: SUBGAP_CARRIER = %s "
              "(completeness %s, gradient chain %s, 200x account "
              "%s)" % ("TENT_SPLIT_FRACTIONS" if carrier_sealed
                       else "NOT_SEALED",
                       "PASS" if dev_rec <= RECON_TOL else "FAIL",
                       "PASS" if worst_fd <= FD_BAR else "FAIL",
                       "%.0fx >= %.0f" % (ratio_200, RATIO_BAR)
                       if ratio_200 >= RATIO_BAR else
                       "%.0fx < %.0f" % (ratio_200, RATIO_BAR)))

    # ---------------- S5 Q3 linear forms (documentation)
    section("S5  Q3 -- LINEAR FORMS IN THE PRIME LOGARITHMS")
    comm = abs(46.0 * D9 / math.log(2.0) - 1.0)
    check("G50-commensurability", comm <= COMM_BAR,
          "w9 grid: Delta = log 2 / 46 (|46 Delta/log2 - 1| = "
          "%.1e <= %.0e) -- the fractions are frac_j = {46 log2 "
          "n_j}; the 2-power family (%d atoms) sits EXACTLY on "
          "nodes: their pairwise fraction differences are EXACT "
          "RESONANCES {46 log2 2^(a-b)} = 0"
          % (comm, COMM_BAR, int(np.sum(onnode9))))
    nn9 = np.round(np.exp(np.asarray(ctx9["uu"]))).astype(np.int64)
    lab_dev = float(np.max(np.abs(np.exp(ctx9["uu"]) - nn9)
                           / np.maximum(nn9, 1)))
    # all pairwise fraction differences (MEASUREMENT_ONLY)
    n_at = len(fr_9)
    ia, ib = np.triu_indices(n_at, 1)
    dfr = np.abs(fr_9[ia] - fr_9[ib])
    dfr = np.minimum(dfr % 1.0, 1.0 - (dfr % 1.0))
    zero_res = dfr <= 1e-12
    min_nz = float(np.min(dfr[~zero_res]))
    amin = int(np.argmin(np.where(zero_res, np.inf, dfr)))
    check("G51-fraction-census", lab_dev <= 1e-9,
          "fraction census (n_j via round(exp(u)), admission "
          "%.1e): %d atoms, %d exact resonant pairs (the on-node "
          "2-power family), smallest NONZERO circular "
          "fraction-difference distance %.3e at the pair (n = "
          "%d, m = %d) [{46 log2(n/m)} nearest-integer distance] "
          "-- MEASUREMENT_ONLY, forbidden as a proof premise"
          % (lab_dev, n_at, int(np.sum(zero_res)), min_nz,
             int(nn9[ia[amin]]), int(nn9[ib[amin]])))

    if smoke:
        for g in ("G52-attribution", "G53-need-documentation",
                  "G54-detector-fractions"):
            check(g, True, "SMOKE: skipped")
        det_typ = {}
        top_pairs_doc = "SKIPPED"
        c_need = float("nan")
    else:
        # attribution: one-sided FD of X_carrier at fixed degree
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        fnpa = np.asarray(W9["fn"], np.int64)[pa9]
        fnpb = np.asarray(W9["fn"], np.int64)[pb9]

        def xcarr_of(u2):
            _d, xp, wp, _fp, xn, vn, fn = fold_world(
                u2, ctx9["mm"], c_ar9, ctx9["alpha"], ctx9["M"],
                ctx9["L"])
            if len(vn) != W9["Sm"] or not np.array_equal(
                    fn, np.asarray(W9["fn"])):
                return None
            al, sb, h0 = FS.mu_chain_f64(xp, wp, Nw)
            Bx = FS.b_matrix_f64(al, sb, h0, xn, vn, Nw)
            uvx = np.sqrt(vn)
            uvx = uvx / float(np.linalg.norm(uvx))
            ra = np.searchsorted(fn, fnpa)
            rb = np.searchsorted(fn, fnpb)
            return float(np.sum(carrier_profile(Bx, Nw, uvx,
                                                ra, rb)))
        X0c = xcarr_of(np.asarray(ctx9["uu"], float))
        att = np.zeros(n_at)
        n_skip_att = 0
        for j in range(n_at):
            e_j = ATT_E
            if dist_node[j] > 1e-9 * D9:
                e_j = min(ATT_E, 0.1 * dist_node[j])
            u2 = np.asarray(ctx9["uu"], float).copy()
            u2[j] += e_j
            Xj = xcarr_of(u2)
            if Xj is None:
                n_skip_att += 1
                continue
            att[j] = gaps_c[j] * abs(Xj - X0c) / e_j
        topi = np.argsort(att)[::-1][:TOPK]
        pairs_doc = []
        for a_ in range(len(topi)):
            for b_ in range(a_ + 1, len(topi)):
                ja, jb = int(topi[a_]), int(topi[b_])
                dv = abs(fr_9[ja] - fr_9[jb])
                dv = min(dv % 1.0, 1.0 - (dv % 1.0))
                pairs_doc.append((att[ja] * att[jb],
                                  int(nn9[ja]), int(nn9[jb]), dv))
        pairs_doc.sort(reverse=True)
        top_pairs_doc = "; ".join(
            "(%d/%d): |{46 log2}| = %.4f" % (na, nb, dv)
            for _s, na, nb, dv in pairs_doc[:TOPK])
        check("G52-attribution", X0c is not None
              and n_skip_att <= 5,
              "ATTRIBUTION (one-sided FD of X_carrier at fixed "
              "degree %d, e = %.0e kink-guarded, %d skipped): "
              "top-%d atoms n = %s (A = %s); the LINEAR FORMS of "
              "the top pairs: %s -- these are the {2 alpha/"
              "(Delta) log(n/m)/log 2 mod 1} forms the carrier "
              "reads" % (Nw, ATT_E, n_skip_att, TOPK,
                         str([int(nn9[i]) for i in topi]),
                         str(["%.1f" % att[i] for i in topi]),
                         top_pairs_doc))
        c_need = DOSE_CRIT * float(np.median(gaps_c)) / D9
        logH = math.log(46.0 * 2.0 * ctx9["alpha"] / D9)
        logA = math.log(math.exp(2.0 * ctx9["alpha"]))
        baker_exp = 24.0 * (logH ** 2) * (logA ** 2)
        need_exp = -math.log(max(c_need * D9, 1e-300))
        check("G53-need-documentation", True,
              "NEED CALCULATION (DOCUMENTATION_ONLY, no bound "
              "applied): the measured flip dose %.3f needs "
              "fraction structure at c_need = %.3f (= dose x "
              "med gap/Delta; in u-units e^-%.1f); a family-"
              "uniform proof route would need |{46 log2(n/m)}| "
              ">= c_need ~ 1/poly(M) -- exponent ~%.1f -- while "
              "Baker/Matveev-class two-log bounds deliver "
              "exp(-C (log H)^2 (log A)^2) with C >= 24: "
              "exponent ~%.0f -- the delivered nonresonance is "
              "~%.0fx WEAKER in the exponent; finite instances "
              "are decided by direct evaluation, the diophantine "
              "input is only needed for the UNBOUNDED family"
              % (DOSE_CRIT, c_need, need_exp, need_exp,
                 baker_exp, baker_exp / max(need_exp, 1e-300)))
        # fraction detectors over the five worlds
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        worlds_fr = {
            "MAIN": np.asarray(ctx9["uu"], float),
            "EPST": np.log(nn_idx.astype(float)),
            "SCR": np.asarray(core.build_window(
                MAIN_KZ, scramble_seed=1)["uu"], float),
            "SMOOTH": np.asarray(PB.smooth_comb(
                rr9["alpha"])[0], float),
            "HL2": np.asarray(comb_hl[0], float)}
        kf1 = {}
        kf2 = {}
        for wname, upos in worlds_fr.items():
            _i0w, frw = frac_split(upos, D9)
            iaw, ibw = np.triu_indices(len(frw), 1)
            dw = np.abs(frw[iaw] - frw[ibw])
            dw = np.minimum(dw % 1.0, 1.0 - (dw % 1.0))
            nzw = dw[dw > 1e-12]
            kf1[wname] = float(np.min(nzw)) if len(nzw) \
                else float("nan")
            kf2[wname] = float(np.abs(np.mean(
                np.exp(2j * np.pi * frw))))
        ctrls = ["EPST", "SCR", "SMOOTH", "HL2"]
        det_typ = {"K_F1_minfrac": LS.dist_rule(kf1, ctrls),
                   "K_F2_fracR": LS.dist_rule(kf2, ctrls)}
        check("G54-detector-fractions", True,
              "FRACTION DETECTORS (sealed r281 distance rule): "
              "%s (K_F1 %s; K_F2 %s) -- typed MEASUREMENT_ONLY; "
              "note EPST shares MAIN's log-n positions by "
              "construction (disclosed)"
              % (str(det_typ),
                 str({k: ("%.1e" % v) for k, v in kf1.items()}),
                 str({k: round(v, 3) for k, v in kf2.items()})))

    # ---------------- S6 Q4 the arithmetic twins
    section("S6  Q4 -- THE ARITHMETIC TWIN FAMILY")
    if smoke:
        for g in ("G60-base-helper", "G61-rational-twin",
                  "G62-rational-mp-ward", "G63-r276-anchor",
                  "G64-jitter-ladder", "G65-shuffle-twin",
                  "G66-twin-table", "G67-adjudication"):
            check(g, True, "SMOKE: skipped")
        verdict3 = "SMOKE_NO_ADJUDICATION"
        twin_note = "SKIPPED"
    else:
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        wm0 = comb_world_measure(ctx9["uu"], ctx9["mm"], D9)
        ok_h = (wm0["minC"] == MINC_REC
                and wm0["cross"] == CROSS_REC
                and abs(wm0["zv"] - ZB9["zv"]) <= 1e-9
                and abs(wm0["b34"] - bands9[1]) <= 1e-9)
        check("G60-base-helper", ok_h,
              "the twin measurement helper reproduces the base "
              "records exactly (minC %s, crossing %s, z_v %+.3f, "
              "band 3-4 %+.3f) -- one measurement channel for "
              "all twins"
              % (str(wm0["minC"]), str(wm0["cross"]), wm0["zv"],
                 wm0["b34"]))
        # (a) RATIONAL twin
        uR, mR, dens, duR = twin_rational(ctx9["uu"], ctx9["mm"],
                                          gaps_c, D9, RAT_TOL)
        i0R, frR = frac_split(uR, D9)
        ok_rc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and bool(np.all(np.abs(duR)
                                 <= RAT_TOL * gaps_c + 1e-300))
                 and bool(np.array_equal(i0R, i0_9))
                 and int(np.max(dens)) <= QMAX
                 and bool(np.all(onnode9 == (np.minimum(
                     frR, 1.0 - frR) * D9 <= ONNODE_EPS * D9))))
        wmR = comb_world_measure(uR, mR, D9)
        _i0f, frRf = frac_split(uR, D9)
        kf2R = float(np.abs(np.mean(np.exp(2j * np.pi * frRf))))
        check("G61-rational-twin", ok_rc,
              "RATIONAL TWIN (every u/Delta -> CF convergent p/q, "
              "|du| <= 1e-8 gap, weights bitwise, cells kept, "
              "on-node family kept; denominators med %d / max %d "
              "<= %.0e; max |du| %.1e): DIOPHANTINE INPUT "
              "TRIVIALIZED, metric change below every tested "
              "scale.  MEASURED: depth %.3f, crossing %s, z_v "
              "%+.3f (MAIN %+.3f), C_off %+.4f, band 3-4 %+.3f, "
              "AA %+.3f, terminal share %+.2f"
              % (int(np.median(dens)), int(np.max(dens)), QMAX,
                 float(np.max(np.abs(duR))), wmR["s"],
                 str(wmR["cross"]), wmR["zv"], ZB9["zv"],
                 wmR["coff"], wmR["b34"], wmR["aa"], wmR["term"]))
        # mp ward on the rational twin (the boundary case)
        WR = wmR["W"]
        almR, sbmR, h0mR = FS.mu_chain_mp(
            np.asarray(WR["xp"]), np.asarray(WR["wp"]), Nw + 1,
            WARD_DPS)
        BmR = FS.b_matrix_mp(almR, sbmR, h0mR,
                             np.asarray(WR["xn"]),
                             np.asarray(WR["vn"]), Nw + 1,
                             WARD_DPS)
        rmp_N = float(np.linalg.eigvalsh(
            BmR[:, :Nw] @ BmR[:, :Nw].T)[-1])
        rmp_N1 = float(np.linalg.eigvalsh(
            BmR[:, :Nw + 1] @ BmR[:, :Nw + 1].T)[-1])
        uvR = np.sqrt(np.asarray(WR["vn"], float))
        uvR = uvR / float(np.linalg.norm(uvR))
        _dgm, _Tm, XmR, _pm, _nm, _Am, _Gm = DC.balance_terms(
            BmR[:, :Nw + 1] @ BmR[:, :Nw + 1].T, uvR)
        Xf64R = wmR.get("X", float("nan"))
        ok_mp = (rmp_N < 1.0 < rmp_N1
                 and math.isfinite(Xf64R)
                 and (XmR < 0.0) == (Xf64R < 0.0))
        check("G62-rational-mp-ward", ok_mp,
              "MP WARD (dps %d) on the rational twin: rho_%d = "
              "%.8f < 1 < %.8f = rho_%d and sign X_v(crossing) "
              "== f64 (%+.4f) -- the 1e-10 perturbation verdict "
              "is not f64 noise at the 1.7e-4 margin"
              % (WARD_DPS, Nw, rmp_N, rmp_N1, Nw + 1, XmR))
        # (b) r276 anchor + jitter ladder
        ctx_mf = MF.window_ctx(MAIN_KZ)
        nfs76 = []
        for seed in R276_SEEDS:
            u2, m2 = MF.pert_jit(ctx_mf["uu"], ctx_mf["mm"],
                                 R276_THETA, seed, False)
            nf2, _z = MF.nf_from_comb(ctx_mf, u2, m2)
            nfs76.append(1.0 if nf2 is None else nf2 / ctx_mf["N"])
        med76 = float(np.median(nfs76))
        check("G63-r276-anchor", abs(med76 - R276_DEPTH_REC)
              <= R276_DEPTH_TOL,
              "r276 DOSE ANCHOR (theta %.2f, seeds %s, exact "
              "machinery): depth med %.3f == record %.3f (tol "
              "%.3f) -- the comb channel is the r276 channel"
              % (R276_THETA, str(R276_SEEDS), med76,
                 R276_DEPTH_REC, R276_DEPTH_TOL))
        lad = {}
        cons_l = True
        for di, th in enumerate(LADDER):
            reps = []
            for rep in range(LAD_REPS):
                u2, m2 = MF.pert_jit(ctx9["uu"], ctx9["mm"], th,
                                     SEED_JL + di * 10 + rep,
                                     False)
                cons_l = cons_l and MF.conserve_comb(
                    "P2_JIT", ctx9["uu"], ctx9["mm"], u2, m2, th)
                reps.append(comb_world_measure(u2, m2, D9))
            lad[th] = reps
        for th in LADDER:
            reps = lad[th]
            info("ladder theta %.4f: depth med %.2f, z_v med %s, "
                 "band 3-4 med %s"
                 % (th,
                    float(np.median([r["s"] for r in reps])),
                    "%+.2f" % float(np.median(
                        [r["zv"] for r in reps
                         if math.isfinite(r["zv"])]))
                    if any(math.isfinite(r["zv"]) for r in reps)
                    else "n/a",
                    "%+.3f" % float(np.median(
                        [r["b34"] for r in reps
                         if math.isfinite(r["b34"])]))
                    if any(math.isfinite(r["b34"]) for r in reps)
                    else "n/a"))
        check("G64-jitter-ladder", cons_l,
              "JITTER LADDER (comb channel, conservation exact, "
              "%d doses x %d reps, log-staggered around %.3f) -- "
              "the metric reference curve for the shuffle twin"
              % (len(LADDER), LAD_REPS, DOSE_CRIT))
        # (c) SHUFFLE twins
        srows = []
        ok_sc = True
        for rep in range(SH_REPS):
            uS, mS, _perm = twin_shuffle(ctx9["uu"], ctx9["mm"],
                                         D9, SEED_SH + rep)
            i0S, frS = frac_split(uS, D9)
            # amendment a1 (disclosed): node snap of the RE-split
            # -- when the permutation assigns an exact on-node
            # fraction (0.0), floor(u'/Delta) can round the cell
            # down by one (frac 1 - 5.7e-14); the constructed
            # world is exact, only the gate's re-split wobbles.
            snap = frS > 1.0 - 1e-9
            i0S = np.where(snap, i0S + 1, i0S)
            frS = np.where(snap, frS - 1.0, frS)
            ok_sc = ok_sc and bool(np.array_equal(i0S, i0_9)) \
                and float(np.max(np.abs(np.sort(frS)
                                        - np.sort(fr_9)))) \
                <= FRAC_MS_TOL \
                and bool(np.array_equal(mS,
                                        np.asarray(ctx9["mm"])))
            th_eff = float(np.median(np.abs(uS - ctx9["uu"])
                                     / gaps_c))
            wmS = comb_world_measure(uS, mS, D9)
            wmS["th_eff"] = th_eff
            srows.append(wmS)
        th_eff_med = float(np.median([r["th_eff"] for r in srows]))
        s_sh = float(np.median([r["s"] for r in srows]))
        zv_sh = float(np.median([r["zv"] for r in srows
                                 if math.isfinite(r["zv"])])) \
            if any(math.isfinite(r["zv"]) for r in srows) \
            else float("nan")
        check("G65-shuffle-twin", ok_sc,
              "SHUFFLE TWIN (%d reps: cells bitwise, fraction "
              "multiset <= %.0e, weights bitwise -- distribution "
              "preserved EXACTLY, assignment destroyed): "
              "effective metric dose theta_eff med %.2f "
              "(DISCLOSED: far above the %.3f threshold -- the "
              "ladder is the reference); depth med %.3f, z_v med "
              "%s" % (SH_REPS, FRAC_MS_TOL, th_eff_med, DOSE_CRIT,
                      s_sh, ("%+.2f" % zv_sh)
                      if math.isfinite(zv_sh) else "n/a"))
        # twin table
        def _fmt(name, wm, extra=""):
            return ("%-9s s %.3f cross %-4s z_v %s C_off %s "
                    "b34 %s AA %s term %s%s"
                    % (name, wm["s"], str(wm["cross"]),
                       ("%+.3f" % wm["zv"])
                       if math.isfinite(wm["zv"]) else "n/a",
                       ("%+.4f" % wm["coff"])
                       if math.isfinite(wm["coff"]) else "n/a",
                       ("%+.3f" % wm["b34"])
                       if math.isfinite(wm["b34"]) else "n/a",
                       ("%+.3f" % wm["aa"])
                       if math.isfinite(wm["aa"]) else "n/a",
                       ("%+.2f" % wm["term"])
                       if math.isfinite(wm["term"]) else "n/a",
                       extra))
        info("TWIN TABLE (w9):")
        info(_fmt("MAIN", wm0))
        info(_fmt("RATIONAL", wmR, "  K_F2 %.3f" % kf2R))
        for rep, wmS in enumerate(srows):
            info(_fmt("SHUF r%d" % rep, wmS,
                      "  th_eff %.2f" % wmS["th_eff"]))
        check("G66-twin-table", True,
              "conservation summary: RATIONAL (weights bitwise, "
              "|du| <= 1e-8 gap, cells + on-node family kept, "
              "denominators <= %.0e), SHUFFLE (cells + fraction "
              "multiset + weights exact), LADDER (r276 "
              "conservation gates) -- what should be preserved "
              "IS preserved, on distribution level" % QMAX)
        # sealed three-way adjudication
        rational_keeps = (wmR["minC"] == MINC_REC
                          and wmR["cross"] == CROSS_REC
                          and math.isfinite(wmR["zv"])
                          and wmR["zv"] < 0.0
                          and abs(wmR["zv"] - ZB9["zv"]) <= RAT_DZV
                          and wmR["b34"] < 0.0
                          and wmR["aa"] < 0.0)
        shuffle_loses = (not math.isfinite(zv_sh)) or zv_sh > 0.0 \
            or s_sh < NEAR
        th_ref = max([t for t in LADDER if t <= th_eff_med]
                     or [LADDER[-1]])
        reps_ref = lad[th_ref]
        zv_ref_l = [r["zv"] for r in reps_ref
                    if math.isfinite(r["zv"])]
        ladder_keeps = (len(zv_ref_l) > 0
                        and float(np.median(zv_ref_l)) < 0.0
                        and float(np.median(
                            [r["s"] for r in reps_ref])) >= NEAR)
        if rational_keeps:
            verdict3 = ("METRIC_ONLY(rational twin KEEPS the full "
                        "signature: minC %d, crossing %d, z_v "
                        "%+.3f vs MAIN %+.3f, band 3-4 %+.3f, AA "
                        "%+.3f -- exact log-relations replaced by "
                        "small-denominator rationals with ZERO "
                        "effect; shuffle context: theta_eff %.2f, "
                        "depth %.3f, ladder at %.4f already %s)"
                        % (wmR["minC"], wmR["cross"], wmR["zv"],
                           ZB9["zv"], wmR["b34"], wmR["aa"],
                           th_eff_med, s_sh, th_ref,
                           "keeps" if ladder_keeps else "loses"))
        elif shuffle_loses and ladder_keeps:
            verdict3 = ("DIOPHANTINE_SIGNAL(rational twin LOSES "
                        "(z_v %s, depth %.3f) and shuffle loses "
                        "(z_v %s, depth %.3f) while the matched "
                        "metric ladder at %.4f keeps -- the Q3 "
                        "linear-form documentation is the "
                        "handover)"
                        % (("%+.2f" % wmR["zv"])
                           if math.isfinite(wmR["zv"]) else "n/a",
                           wmR["s"],
                           ("%+.2f" % zv_sh)
                           if math.isfinite(zv_sh) else "n/a",
                           s_sh, th_ref))
        else:
            verdict3 = ("NEITHER(rational keeps %s, shuffle "
                        "loses %s, ladder-at-theta_eff keeps %s "
                        "-- the measures do not separate a "
                        "diophantine channel from the metric "
                        "dose)" % (str(rational_keeps),
                                   str(shuffle_loses),
                                   str(ladder_keeps)))
        check("G67-adjudication", True,
              "SEALED THREE-WAY RULE evaluated: rational_keeps = "
              "%s, shuffle_loses = %s, ladder_keeps(at %.4f <= "
              "theta_eff %.2f) = %s -> %s"
              % (str(rational_keeps), str(shuffle_loses), th_ref,
                 th_eff_med, str(ladder_keeps),
                 verdict3.split("(")[0]))
        twin_note = ("RATIONAL s %.3f z_v %s / SHUFFLE med s "
                     "%.3f z_v %s theta_eff %.2f / LADDER %s"
                     % (wmR["s"],
                        ("%+.2f" % wmR["zv"])
                        if math.isfinite(wmR["zv"]) else "n/a",
                        s_sh,
                        ("%+.2f" % zv_sh)
                        if math.isfinite(zv_sh) else "n/a",
                        th_eff_med,
                        str({t: round(float(np.median(
                            [r["s"] for r in lad[t]])), 2)
                            for t in LADDER})))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    m2_mut = mutant_mass_twin(ctx9["mm"])
    caught_m1 = not bool(np.array_equal(m2_mut,
                                        np.asarray(ctx9["mm"])))
    check("G70-mustfail-mass", caught_m1,
          "m1 MASS TWIN (x 1.15 on the largest weight): CAUGHT "
          "by the bitwise weight conservation gate -- mass "
          "change cannot pass as a twin")
    c_wrong = mutant_wrong_delta(ctx9["uu"], ctx9["mm"], D9,
                                 ctx9["M"])
    dev_m2 = float(np.max(np.abs(c_wrong - c_at9))) \
        / max(float(np.max(np.abs(c_at9))), 1e-300)
    check("G71-mustfail-wrong-delta", dev_m2 >= M2_BAR,
          "m2 WRONG-DELTA FRACTIONS (tent split against Delta/2): "
          "reconstruction breaks by rel %.2f >= %.1f -- LOUD: "
          "the fraction is only defined against the TRUE lag "
          "grid" % (dev_m2, M2_BAR))
    X_mut, bi_mut = mutant_drop_band(prof_cross, CROSS_REC)
    dev_m3 = abs(X_mut - ZB9["X"]) / max(ZB9["A"], 1e-300)
    check("G72-mustfail-drop-band", dev_m3 >= M3_BAR,
          "m3 DROPPED-BAND DECOMPOSITION (band %s removed): sum "
          "identity breaks by %.3f of sum|T| >= %.2f -- LOUD: "
          "the decomposition must sum"
          % (band_label(bi_mut), dev_m3, M3_BAR))
    hits_m4 = scope_audit("mutant_cross_twin", SCOPE_FORBIDDEN)
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m4) and not hits
          and not ag_hits,
          "m4 CROSS-ORACLE TWIN FLAGGED (%s); the %d sealed "
          "constructors consume comb positions + weights + grid "
          "geometry + seed ONLY (%s); fragment audit: %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 honesty ledger
    section("S8  DETECTOR + HONESTY LEDGER")
    check("G80-honesty-ledger", True,
          "PAIRCORR HONESTY (binding): every fraction statistic "
          "(census, min distance, resultant, detectors %s) is "
          "typed MEASUREMENT_ONLY and FORBIDDEN as a proof "
          "premise; the Q3 need calculation is typed "
          "DOCUMENTATION_ONLY -- no Baker/Matveev bound was "
          "applied anywhere in this round"
          % (str(det_typ) if not smoke else "SKIPPED"))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "Baker/Matveev application, no asymptotic law, no "
          "derived 5/7, no equidistribution premise, no posthoc "
          "window, no RH claim; what the round adds: the "
          "kernel-degree anatomy of the flip, the sealed sub-gap "
          "carrier attribution, the linear-form documentation "
          "with need calculation, and the arithmetic-twin "
          "adjudication; r243..r288 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = [verdict3]
        parts.append(
            "SENSITIVE_FACTOR(%s: %.2f z-units at dose %.3f "
            "while dphi %.4f)"
            % (sens_name, sens_val, DOSE_CRIT, dphi_u))
        parts.append(
            "SUBGAP_CARRIER(%s; completeness %.0e; 200x account "
            "ratio %.0fx)"
            % ("TENT_SPLIT_FRACTIONS" if carrier_sealed
               else "NOT_SEALED", dev_rec, ratio_200))
        parts.append(
            "LINEAR_FORMS(top pairs %s; min nonzero distance "
            "%.3e; %d exact 2-power resonances; need c %.3f vs "
            "Baker-class exponent gap DOCUMENTED)"
            % (top_pairs_doc, min_nz, int(np.sum(zero_res)),
               c_need))
        parts.append("TWIN_TABLE(%s)" % twin_note)
        parts.append("DETECTOR_LEDGER(%s)" % str(det_typ))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy + sealed twin adjudication "
          "of the open scalar L*'s coherence half; NO L* claim, "
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
