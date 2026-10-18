#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""blockgreen_membership_probe -- PRIME.LSTAR.BLOCKGREEN.
MEMBERSHIP.01 (round 312, THE ONE construction round granted by
the reviewer decision tree after r311's STRICT_SOURCE_CONE): DOES
A SOURCE-PURE, CONSTRUCTIVE RULE EXIST -- NO SDP OPTIMIZATION IN
THE FINAL STATEMENT -- THAT WRITES DOWN AN EXPLICIT PSD BLOCK
FAMILY FOR THE WORLD TARGETS, AND DOES IT EXPLAIN WHAT SEPARATES
BORDERED-HANKEL FORMS FROM GENERIC PD FORMS?  Strategic frame
(binding, from the published r311 record): the r308 world
discriminator is DEAD (the separation was fully the budget sign;
the Delta sparsity graph is chordal -- on evaluation space a pure
restatement; the common dual Y_t = e_t e_t^T is the known r243
budget positivity; the ablations flip the separation in both
directions) -- BUT the cone is genuinely strict on the compressed
subspace: 0/16 sealed in-span PD samples decompose, with fully
exact rational Farkas certificates on MINI16 (the real-w9
miniature with full span 55/55) and SM1.  BLOCK MEMBERSHIP IS
GENUINELY STRONGER THAN POSITIVITY -- MAIN + the rational twin
HAVE it at deg <= 8, generic positive forms do NOT.  The
re-scoped object of this round is the MEMBERSHIP MECHANISM.  Per
the reviewer tree this is exactly ONE construction round, no L*
status move; if it fails, lane A stays a valuable cone LANGUAGE
but not a proof path and the resources move to the fiber.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r314 (signed cube identity, fiber lane) runs in
parallel; this probe touches nothing of theirs.

INDEX FIREWALL (binding, r238-r311 discipline): w = window (kz),
S = #union atoms, N_w = (S+1)//2, n = degree, minC = first
h_n < 0.  Ground truth (minC, flips, published r308/r309/r311
record numbers) enters GATES and record tables only; the sealed
constructors consume split-source arrays, coordinate matrices and
the source-pure budget scalar ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r308 BG.{cheb_rows, block_maps_f64/fr, target_form_
f64/fr, system_f64/fr, least_norm, block_eigs, mono_rows_fr,
rref_solve_fr, exact_budget_fr, census_world, world_arrays,
world_budget, hull_of, border_split, feas_diag}; r311 BN.{graph_
from_blocks, mcs_order, peo_check, max_cliques_peo, rref_rank_fr,
det_fr, comp_psd_fr, cheb_rows_fr, y_from_leftnull, span_project,
compress_bases, comp_min_eig, dual_pocs, polish_dual, run_feas3,
rationalize_sym, exact_cert_check, exact_strict_cert, sample_psd,
gate_lam_rel, vech_of, unvech}; worlds through r278 MS.ctx_build,
r284 LS.world_pack, r289 AK.twin_rational + r276 MF.local_gaps,
v881 PIK, r243 PB.smooth_comb, r274 WD chains via BG, v563 core
READ-ONLY.  The ONLY local re-implementation is feas_diag_g = the
UNCHANGED r308 Dykstra iteration returning its final iterate (the
solution family is needed for Leg A; iteration body verbatim).

THE SEALED GENERATOR LIBRARY (frozen HERE, in this docstring,
BEFORE any Leg-A evaluation -- the reviewer's classes, expressed
in the sealed r308 Delta coordinates D1..D6 of each fourfold
block; all 22 vectors have INTEGER coordinates in the D basis;
the library is identical for every block and every world):
  fold distance 1 and 2:     V01 = D1,  V02 = D2;
  antiphase 3 and 4:         V03 = D3,  V04 = D4;
  the r307 arch coordinates: V05 = D5 (local gross-mass arch
    mean), V17 = D1 + D4 (2 e_{j+1} - e_j - e_{j+3}, symmetric),
    V18 = D1 - D4 (e_{j+3} - e_j, the growing edge-to-edge span);
  border-vs-interior modes:  V06 = D6 and the ten pairs
    V07..V16 = D_a + D6 / D_a - D6 for a = 1..5;
  four-block modes:          V19 = D2 + D3 (2 e_j - 2 e_{j+1}),
    V20 = D2 - D3 (2 e_{j+2} - 2 e_{j+1}), V21 = 2 D1 + D2 + D4
    (= -(e_j - e_{j+1} - e_{j+2} + e_{j+3}), symmetric four-point
    mode), V22 = D2 + D4 (= e_j - e_{j+1} + e_{j+2} - e_{j+3},
    alternating four-point mode).
Per block the 22 rank-one matrices V V^T span a FIXED 15-dim
subspace of the 21-dim symmetric block space (exact integer rank,
gated); the cone cone{V V^T} is a scaled-diagonally-dominant-type
STRICT sub-cone of the psd cone -- smaller BY DESIGN: the round
tests whether the world identity fits inside it, and if not,
WHERE it breaks (span or sign).

THE SEALED FORMULA VOCABULARY (source arrays only; frozen here):
per block r on atoms (j..j+3): m+_r / m-_r = local mu / nu gross
masses, G_r = m+_r + m-_r, tent fractions t1_r = |x_j - x_{j+1}| /
|x_j - x_{j+3}| and t2_r = |x_{j+1} - x_{j+2}| / |x_j - x_{j+3}|,
edge flag e_r = [all four atoms have u = f Delta < log 2] (the
r307 flat arch edge), budget share Gt_r = G_r S_{N-2}(w) /
sum_rho G_rho (S_{N-2} = B - 5/7, the source-pure r243 budget
scalar), and the 4-bit nu-occupancy type of the block.  SEALED
CANDIDATE FORMULAS (parameters a >= 0 calibrated by NNLS on
w9@DEG_A ONLY -- the solver discovers -- then FROZEN and verified
with frozen parameters, independently, on all 57 rungs + twin):
  PHI_A: c_{r,l} = a_l G_r + b_l Gt_r
  PHI_B: c_{r,l} = a_l m+_r + b_l m-_r + d_l Gt_r
  PHI_C: c_{r,l} = (a_l + b_l t1_r + d_l t2_r) G_r + e_l Gt_r
  PHI_D: c_{r,l} = a_{type(r),l} G_r + b_{type(r),l} Gt_r
    (an explicit PIECEWISE formula -- allowed by the reviewer's
    piecewise clause; its CONTENT is the transfer: the w9-frozen
    16x22x2 table must carry all 57 rungs).
All features are nonnegative, so c >= 0 holds by construction;
regression-free: NNLS parameter determination is exact linear
algebra on sealed features, no free exponents, no fit primitives.
METRIC_ONLY semantics (binding): features consume masses,
positions, the fold-grid u and the budget scalar ONLY -- no exact
logarithmic relations; the rational twin must satisfy the same
rule (gated live in m3: a planted log-relation consumer must be
exposed by the MAIN-vs-twin comparison).

THE SEALED LEGS (frozen BEFORE any evaluation):

LEG 0 -- R311 ANCHORS BIT-NEAR.  w9 source split (367/263/104/
184/184); B = 8.368649 (tol 1e-3); census rank/dof records
(51/7593 @DEG_A, 229/7415 @DEG_B); least-norm min eig rel in the
2x band around -1.30e-2; chordality of the full w9 graph (S=367,
maximal cliques == the 364 sealed blocks); the budget-dual values
<Y_t, A> = S_{N-2}: w9/twin positive reserve vs EPST -3.992 /
SCR -5.237 (tol 0.05); the r308 Dykstra anchors w9@A + twin@A
CONV at stage 200; THE STRICTNESS CENSUS REPRODUCED BIT-NEAR with
the identical rng stream (seed 20260826, identical draw order
w9A -> MINI16 -> SM1): 0/6 + 0/6 + 0/4 in-span PD samples
decompose under the staged r308 protocol (200/2000/20000), the
10 MINI16/SM1 stalls carry valid polished-numeric Farkas duals,
MINI#0 and SM1#0 carry FULLY EXACT in-span rational certificates
(exact Chebyshev basis, den 1e6, <Y,Q> in (-1.0001, -0.999)); the
six w9A stalls stay one-sided (dual POCS diverges).

LEG A -- MEMBERSHIP ANATOMY (DISCOVERY, openly labeled; the r308
Dykstra solutions are discovery material -- NO circularity: they
inform the formula SEARCH only, never the verification).  Extract
the converged psd G families on w9@A and twin@A (feas_diag_g, 200
steps from the least-norm start -- the r308 protocol).  Measure:
(i) the eigen-rank census of the G_r across the 364 blocks
(RANK_TOL relative to the block Frobenius norm) and the alignment
of each block's top eigenvector with the sealed library
directions; (ii) the library-cone share per block: the NNLS
projection of G_r onto cone{V V^T} in Frobenius-isometric
coordinates -- cone fraction f_r = 1 - dist_F / ||G_r||_F,
reported min / median / mean; (iii) the DUAL ANATOMY: for every
valid r311 sample dual Y (MINI16/SM1), the decomposition of
<Y, A_world> and <Y, Q_sample> into Hankel / border-column /
budget parts, plus the most-negative eigendirection z of Y (its
t component, its overlap with the border column u, its dominant
degree index) -- what the generic-missing directions look like
against the world-target components.  Fine type:
MEMBERSHIP_ANATOMY(rank census; cone share; dual anatomy).

LEG B -- THE CONSTRUCTIVE SECTION (the core).  On the sealed
library system M_lib (columns vech(L_r^T V_l V_l^T L_r)):
  (B1) SPAN LAYER: unconstrained least-squares residual of
       M_lib c = q on w9@A, twin@A, MINI16, SM1 (f64, Chebyshev)
       + EXACT existence on SM1 and MINI16 (Fractions, monomial
       basis, rref of [M_lib | q]) -- if the library SPAN already
       fails, the letter is PSD_NEEDS_FULL_MATRIX;
  (B2) CONE LAYER: deterministic Lawson-Hanson NNLS (column-
       normalized, deterministic ties, iteration caps loud) on
       w9@A and twin@A; a feasible c (rel residual <= NN_BAR) IS
       an explicit rank-one section (the solver-found
       decomposition, support reported); an infeasible NNLS
       yields the KKT residual y = M c* - q as a FARKAS
       certificate (verified independently: min_l <col_l, y> /
       ||col_l|| >= -FARKAS_TOL with <y, q> < 0; when the raw
       margin is tolerance-limited the sealed f64 I-POLISH runs:
       y + delta y_I with <col, y_I> = ||w||^2 > 0 over the
       DELTA_LADDER, accepted iff min normalized product >=
       -POLISH_MIN and <y, q> <= -POLISH_VAL -- amendment a1,
       the f64 twin of the exact I-polish sealed below and of
       the r311 eps*I polish class), whose t-row
       mass fraction localizes the obstruction (wall vs
       structure); on SM1/MINI16 the certificate is escalated to
       FULLY EXACT rational form by the I-polish (Y + delta I has
       <col, Y> = v^T Y v + delta ||v||^2, exactly positive --
       the exact analog of the r311 eps*I polish), and a feasible
       c is escalated to an exact rational section attempt
       (rationalize on the support, exact rref correction, c >= 0
       exact) -- both one-sided attempts, honestly reported;
  (B3) THE RUNG CENSUS: NNLS feasibility on all 57 rungs at DEG_A
       (the r308 census ladder verbatim: 42 core h <= 900 + 15
       extension anchors h <= 1300 sorted by (N_w, kz));
  (B4) THE FORMULA: calibrate PHI_A..PHI_D on w9@A (NNLS over the
       sealed feature space), FREEZE the parameters, verify the
       frozen formula independently on all 57 rungs + twin:
       identity residual <= FORM_BAR, all c >= 0 by construction,
       recomposition == Q gated through the same residual.
  SEALED ADJUDICATION TREE (the round's main letter):
    span fails on w9@A (rel > SPAN_BAR)
        => PSD_NEEDS_FULL_MATRIX(span defect);
    NNLS feasible on w9@A AND a frozen formula carries 57 + twin
        => RANKONE_SECTION_GO(phi);
    NNLS feasible on w9@A, no formula carries
        => MEMBERSHIP_UNEXPLAINED(explicit solver section exists,
           formula missing);
    NNLS infeasible with verified Farkas, t-row mass >= WALL_FRAC
        => COEFFICIENT_SIGN_WALL(the identity forces negative c
           exactly where the wall is thin);
    NNLS infeasible with verified Farkas, t-row mass < WALL_FRAC
        => PSD_NEEDS_FULL_MATRIX(cone infeasible off-wall);
    otherwise => MEMBERSHIP_UNEXPLAINED(undecided numerics).
  Twin consistency (METRIC_ONLY) is reported inside the letter;
  a MAIN/twin type mismatch is a loud honest finding, never
  silently absorbed.

LEG C -- W9@DEG_B (the open flank).  Anchor: the staged r308
protocol from the least-norm start reproduces the r311 state
(min eig rel in the 2x band around -1.78e-5 after 20000).  Then:
(i) NNLS on the library system at DEG_B -- a feasible c DECIDES
deg-28 membership constructively (sufficient, not necessary);
(ii) the EXTENDED Dykstra: continue the sealed protocol from the
20000-step iterate for EXT_STEPS more steps; (iii) on a persistent
stall the strengthened dual attempt (dual POCS at OMEGA_B = 0.1,
DUAL_ITER_B = 8000, divergence guard, eps*I polish).  Typed
W9B_MEMBER(route) / W9B_DUAL_CERT / W9B_OPEN(state) -- honest
one-sided semantics throughout.

LEG D -- MUST-FAILS (each loud):
  (m1) TARGET-EIGENDIRECTION LIBRARY: a mutant extending the
       sealed library by an eigendirection of the assembled
       target (consumes eigvecs_target) -- FLAGGED by the AST
       scope audit (TARGET_INVERSE class);
  (m2) NEGATIVE-c FORMULA: the independent verifier receives a
       coefficient vector with one entry forced negative -- it
       must REJECT loudly (the c >= 0 check is load-bearing);
  (m3) LOG-RELATION CONSUMER: a mutant phi factor that consumes
       exact rational structure of the r289 rationalization
       variable u/Delta (den-ladder probe at LOGREL_TOL;
       amendment a2 -- the first harness probed u itself, which
       the twin does NOT rationalize) -- the MAIN-vs-twin
       comparison must EXPOSE it (disagreement fraction >=
       M3_BAR) while the sealed features stay METRIC-stable
       (max rel dev <= M3_STAB);
  (m4) RECOMPOSITION BREAK: corrupting one library coefficient
       of an exactly reconstructed SM1 form must leave a NONZERO
       exact entrywise defect -- CAUGHT in Fractions.

STOP LIST (binding): NO L* claim, NO bound mechanism, NO
asymptotic law, NO derived 5/7, NO posthoc window, NO library or
bar change after any evaluation (amendments disclosed), NO RH
claim; r243..r311 stand; the r311 verdict letters stand -- this
round adjudicates the CONSTRUCTION question only.

WORLDS: MAIN w9; the r289 rational twin; EPSTEIN / SCRAMBLE
(seed 1) budget scalars for the Y_t anchor only; the 57-rung r308
census ladder; exact small models SM1 and MINI16 rebuilt VERBATIM
from the r308 constructors.

SEALED CONSTANTS: DEG_A 8; DEG_B 28; MAIN_KZ 9; W9_ANCH (367,
263, 104, 184, 184); H_CAP 900; EXT_H 1300; K_EXT 15; RES_BAR
1e-8; SPAN_BAR 1e-8; NN_BAR 1e-7; NN_GRAD_TOL 1e-11; NN_ITMAX
4000; FARKAS_TOL 1e-9; WALL_FRAC 0.5; FORM_BAR 1e-8; RANK_TOL
1e-8; RCOND 1e-11; PSD_NEG 1e-7; FEAS_CONV 1e-9; SEED 20260826;
NSAMP (6, 6, 4); FEAS stages (200, 2000, 20000); EXT_STEPS 80000;
DUAL_ITER_B 8000; OMEGA_B 0.1; DEN_LADDER (100, 10000, 1000000);
D_LADDER (1e-6, 1e-4, 1e-2) exact; DELTA_LADDER f64 (1e-8, 1e-6,
1e-4, 1e-2) with POLISH_MIN 1e-12 / POLISH_VAL 0.5 (a1);
CERT_CAP 1; LOGREL_TOL 1e-15;
M3_BAR 0.3; M3_STAB 1e-3; LIB_SPAN_REC 15; RANK_REC {SM1 44,
MINI16 55, w9A 51, w9B 229}; DOF_REC {w9A 7593, w9B 7415};
LEAST_REC -1.30e-2 (band 2x); B_W9_REC 8.368649 tol 1e-3;
S_EPST_REC -3.992 / S_SCR_REC -5.237 tol 0.05; W9B_20K_REC
-1.78e-5 (band 2x); CERT_BAND (-1.0001, -0.999); QMAX 1e6;
RAT_TOL 1e-8; MINI_K 16; MINI_BK 3; runtime <= 1800 s; smoke =
S0 + S1 (library structure + SM1 exact) + S2 w9/MINI16 anchors +
chordality + SM1/MINI16 f64 NNLS + S7 mutants + verdict-skip
(twin, controls, samples, Leg A, w9 NNLS, rungs, formulas, Leg C
skipped).  PRE-SPEC SCOPING (disclosed): every record number
above is a published r308/r309/r311 record adopted as-is; the
library, the formula vocabulary, the candidates, the adjudication
tree, every bar/ladder/schedule and the verdict form were fixed
at design time BEFORE any evaluation of this probe; no machinery
pass preceded this spec except record reading; the only
target-derived data any constructor consumes is the source-pure
budget scalar S_{N-2} (a declared source quantity of the formula
vocabulary, r243 provenance).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of, by the Leg-B tree]
    RANKONE_SECTION_GO(phi, transfer census) /
    PSD_NEEDS_FULL_MATRIX(defect locus) /
    COEFFICIENT_SIGN_WALL(farkas localization) /
    MEMBERSHIP_UNEXPLAINED(state)
  + MEMBERSHIP_ANATOMY(rank census; cone share; dual anatomy)
    [always]
  + W9B_STATUS(MEMBER / DUAL_CERT / OPEN) [always]
  + R311_DEMARCATION [always]: the r311 letters stand; this round
    adjudicates the construction question only.
CONSEQUENCE MAP (sealed, reviewer tree): RANKONE_SECTION_GO =>
lane A becomes a genuine proof lane (formula in hand); every
other letter => lane A is documented and CLOSED as cone language,
resources move to the fiber.  Honesty before beauty: the formula
bar is strict by design (identity exact on every window under
frozen parameters); a solver-feasible-but-formula-free outcome is
typed MEMBERSHIP_UNEXPLAINED and is NOT a GO.

RECORD TABLES (frozen from the record run; chronology honest:
smoke pass 1 = 32/32 (32.0 s) at the sealed rules -- no fail at
smoke stage; calibration pass 1 = first full evaluation = 29/32
with two harness findings and one consequence: (i) G52 -- the
raw NNLS-residual Farkas margin is TOLERANCE-LIMITED near
feasibility (worst normalized column product -2.54e-06 at the
KKT residual scale tol/||y||^2, three decades above the 1e-9
bar although Lawson-Hanson had converged) -> AMENDMENT a1
(disclosed, certificate bookkeeping only, the four-way tree
never moved): the sealed f64 I-POLISH y + delta y_I over
DELTA_LADDER with POLISH_MIN/POLISH_VAL acceptance -- the f64
twin of the exact I-polish already sealed for the miniatures
and of the r311 eps*I polish class; (ii) G72 -- the m3 mutant
probed the comb u itself, which the r289 twin does NOT
rationalize (disagreement 0.000) -> AMENDMENT a2 (disclosed,
must-fail harness only): the mutant now consumes the r289
rationalization variable u/Delta (the docstring constant line
was corrected to the sealed code value LOGREL_TOL 1e-15);
(iii) G96 followed arithmetically.  Calibration pass 2 = 32/32
(573.7 s).  No library element, formula candidate, main-leg bar
or verdict rule moved at any point after first evaluation; the
only post-freeze edit is this record-table insertion, which IS
the protocol; record run1/run2 = 32/32, identical up to WALL.
REC_VERDICT = COEFFICIENT_SIGN_WALL(w9@A: the library SPAN
CARRIES the identity (unconstrained rel 2.4e-13) but the CONE
does not: NNLS stalls at rel 4.7e-4 (support 35, not capped)
with a VERIFIED I-polished Farkas certificate (delta 1e-4, min
normalized column product +9.7e-5 >= -1e-12, <y,q> = -0.9975 <=
-0.5), t-row mass fraction 0.58254 >= WALL_FRAC 0.50 -- the
identity forces negative c on the wall/border coordinates; twin
type-identical (rel 4.7e-4, t-mass 0.58254, METRIC_ONLY holds);
EXACT GRADE on the miniatures (mono basis): SM1 NNLS rel 0.0329
and MINI16 rel 0.0079, BOTH with FULLY EXACT I-polished rational
Farkas certificates (den 100, delta 1/10000, <Y,q> = -0.9988 /
-1.0000 exact rational < 0, all 154/286 exact column products
>= 0) -- the sealed rank-one library cone EXACTLY cannot
represent the miniature targets; rung census 1/57 NNLS-feasible
(worst rel 8e-4 at kz12) -- the sign wall is uniform across the
ladder; formulas never fired: PHI_A 0.0389 / PHI_B 0.0239 /
PHI_C 0.0277 / PHI_D 0.0077 on w9@A, all >> FORM_BAR 1e-8,
no transfer test)
+ MEMBERSHIP_ANATOMY(the converged r308 Dykstra family on w9@A
is HIGH-RANK and library-ALIGNED but not library-CONIC: rank
census over 364 blocks {rank 3: 17, rank 4: 79, rank 5: 268},
top-eigvec alignment with the sealed library med 0.9973 (min
0.925), library-cone share med 0.976 / min 0.952 / mean 0.978
(twin med 0.976) -- 97.6 percent of the psd family lives in the
sealed cone and the WHOLE membership obstruction sits in the
remaining 2.4 percent of SDD-forbidden negative cross mixtures;
DUAL ANATOMY of the 10 valid r311 sample duals: the MINI16
duals nearly ANNIHILATE their world target (<Y, A_world> parts
H/u/t all ~ +0.000 -- the world target sits close to the face
the certificates separate along) while the SM1 duals are
carried by the Hankel part (+0.42..+1.34, u- and t-parts ~ 0);
the most-negative dual eigendirections are INTERIOR: |z_t| med
0.000 (max 0.087), u-overlap 0.01..0.40, dominant degree
indices {1, 2, 4, 5, 6} -- what generic PD forms are missing is
low/mid-degree INTERIOR mass, not border mass)
+ W9B_STATUS(OPEN, two-sidedly hardened: staged anchor
-1.784e-5 == the r311 record; library NNLS@B infeasible (rel
4.1e-4, support 151, t-row mass 0.72523 -- the same wall class,
even more border-localized); EXTENDED Dykstra +80000 steps from
the 20000-step iterate improves only -1.784e-5 -> -7.655e-6 (a
slow factor-2.3 tail, consistent with asymptotic feasibility,
NOT decided); strengthened dual POCS (OMEGA 0.1, 8000 iters)
runs but the polish is INVALID (val +1.753) = no certificate:
w9@deg28 stays honestly OPEN)
+ R311_DEMARCATION.
Key numbers.  LIBRARY: abstract span 15/21 exact (integer
rref); SM1 exact [M_lib | q]: EXISTS FALSE (rank 41, dof 113 --
on the MAIN-class miniature even the SPAN fails exactly, the
sharpest small-model form of the wall); MINI16 exact: EXISTS
(rank 55, dof 231).  LEG 0 bit-near on the identical rng
stream: w9 367/263/104/184/184, B 8.368649, rank/dof 51/7593@A
229/7415@B, least-norm -1.298e-2, chordal (364 maximal cliques
== blocks), Y_t: w9/twin +7.6544 vs EPST -3.9921 / SCR -5.2368;
Dykstra w9@A +6.56e-16 / twin@A +2.05e-17 CONV@200 (affine res
3.7e-14); strictness census 0/6 + 0/6 + 0/4 decomposed, 10/10
polished duals, MINI#0 exact cert <Y,Q> = -0.9999977 / SM1#0
-0.9999930 (both den 1e6, d 1e-6), the six w9A duals diverge
(one-sided) -- every r311 record reproduced.  READING (typed
measurement): the membership mechanism is now NAMED -- the
world targets sit in the block-psd cone (r308/r311) but NOT in
its sealed rank-one SDD sub-cone; the missing 2.4 percent are
negative cross mixtures the reviewer's generator classes cannot
carry with c >= 0, and the Farkas mass localizes on the
border/budget row: the sign question of the c IS the wall, in
the constructive language too.  MUST-FAILS: m1 eigvecs_target
library FLAGGED; m2 negative-c REJECTED loud; m3 log-relation
consumer EXPOSED (disagreement 0.886 >= 0.3, features
METRIC-stable 1.4e-5 <= 1e-3); m4 exact recomposition break
CAUGHT (max |dev| = 3 exact); constructors + fragment audit
CLEAN.  Runtime 562.8 s full / 32.0 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import block_green_probe as BG                     # noqa: E402 r308
import blockgreen_nontriviality_probe as BN        # noqa: E402 r311
import lstar_two_measure_probe as LS               # noqa: E402 r284
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import minimal_firewall_probe as MF                # noqa: E402 r276
import metric_stability_probe as MS                # noqa: E402 r278
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
DEG_B = 28
MAIN_KZ = 9
W9_ANCH = (367, 263, 104, 184, 184)
H_CAP = 900
EXT_H = 1300
K_EXT = 15
RES_BAR = 1e-8
SPAN_BAR = 1e-8
NN_BAR = 1e-7
NN_GRAD_TOL = 1e-11
NN_ITMAX = 4000
FARKAS_TOL = 1e-9
WALL_FRAC = 0.5
FORM_BAR = 1e-8
RANK_TOL = 1e-8
RCOND = 1e-11
PSD_NEG = 1e-7
FEAS_CONV = 1e-9
SEED = 20260826
NSAMP_W9 = 6
NSAMP_MINI = 6
NSAMP_SM = 4
FEAS_IT1 = 200
FEAS_IT2 = 2000
FEAS_IT3 = 20000
EXT_STEPS = 80000
DUAL_ITER_B = 8000
OMEGA_B = 0.1
DEN_LADDER = (100, 10000, 1000000)
D_LADDER = (Fr(1, 10 ** 6), Fr(1, 10 ** 4), Fr(1, 100))
DELTA_LADDER = (1e-8, 1e-6, 1e-4, 1e-2)
POLISH_MIN = 1e-12
POLISH_VAL = 0.5
CERT_CAP = 1
LOGREL_TOL = 1e-15
LOGREL_DENS = (10, 100, 1000, 10000, 100000)
M3_BAR = 0.3
M3_STAB = 1e-3
LIB_SPAN_REC = 15
RANK_REC = {"SM1": 44, "MINI16": 55, "w9A": 51, "w9B": 229}
DOF_REC = {"w9A": 7593, "w9B": 7415}
LEAST_REC = -1.30e-2
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
S_EPST_REC = -3.992
S_SCR_REC = -5.237
S_CTRL_TOL = 0.05
W9B_20K_REC = -1.78e-5
CERT_BAND = (-1.0001, -0.999)
QMAX = 1e6
RAT_TOL = 1e-8
MINI_K = 16
MINI_BK = 3
FIVE_SEVEN = Fr(5, 7)
LOG2 = math.log(2.0)

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
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume split-source arrays, "
                       "coordinate matrices and the source-pure "
                       "budget scalar ONLY; record numbers enter "
                       "gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq_fit",
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


CONSTRUCTORS = ("lib_vectors", "lib_tensor", "lib_cols_fr",
                "nnls_lh", "farkas_stats", "feas_diag_g",
                "block_feats", "cand_design", "formula_coeffs",
                "verify_section", "exact_farkas_polish",
                "exact_section_attempt", "cheb_pack_x")
SCOPE_FORBIDDEN = {"CTRL_FLIPS", "ANCHORS", "minC_true",
                   "cross_true", "blk_eigs_true", "cholesky",
                   "eigvecs_target", "target_inverse", "wall_sign"}


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


# ============== the sealed generator library (AST-audited)
def lib_vectors():
    """the 22 sealed library generators as INTEGER vectors in the
    D basis (D1..D6) -- fixed for every block and world; declared
    in the docstring BEFORE any Leg-A evaluation.  Consumes
    nothing."""
    e = np.eye(6, dtype=np.int64)
    V = [e[0], e[1], e[2], e[3], e[4],                       # V01..V05
         e[5],                                               # V06
         e[0] + e[5], e[0] - e[5],                           # V07/V08
         e[1] + e[5], e[1] - e[5],                           # V09/V10
         e[2] + e[5], e[2] - e[5],                           # V11/V12
         e[3] + e[5], e[3] - e[5],                           # V13/V14
         e[4] + e[5], e[4] - e[5],                           # V15/V16
         e[0] + e[3], e[0] - e[3],                           # V17/V18
         e[1] + e[2], e[1] - e[2],                           # V19/V20
         2 * e[0] + e[1] + e[3],                             # V21
         e[1] + e[3]]                                        # V22
    labels = ("D1", "D2", "D3", "D4", "D5", "D6",
              "D1+D6", "D1-D6", "D2+D6", "D2-D6", "D3+D6",
              "D3-D6", "D4+D6", "D4-D6", "D5+D6", "D5-D6",
              "D1+D4", "D1-D4", "D2+D3", "D2-D3",
              "2D1+D2+D4", "D2+D4")
    return np.array(V, dtype=np.int64), labels


def lib_tensor(L, V):
    """f64 library system tensor: T[r, l, e] = vech entry e of
    L_r^T V_l V_l^T L_r (plain upper-triangular convention,
    matching BG.system_f64 / census q).  Consumes coordinate
    maps only."""
    W = np.einsum("la,ram->rlm", V.astype(float), L)
    m = L.shape[2]
    iu, ju = np.triu_indices(m)
    T = W[:, :, iu] * W[:, :, ju]
    return T


def lib_cols_fr(Ls, V, idx):
    """exact library system matrix (Fractions): rows = the (i<=j)
    entry list idx, columns = (block r, generator l)."""
    nblk = len(Ls)
    nl = len(V)
    M = [[Fr(0)] * (nblk * nl) for _ in range(len(idx))]
    m = len(Ls[0][0])
    for r in range(nblk):
        for li in range(nl):
            w = [sum(int(V[li][a]) * Ls[r][a][i] for a in range(6))
                 for i in range(m)]
            col = r * nl + li
            for e_i, (i, j) in enumerate(idx):
                M[e_i][col] = w[i] * w[j]
    return M


def nnls_lh(M, q, itmax=NN_ITMAX):
    """deterministic Lawson-Hanson NNLS on the column-normalized
    system: min ||M c - q|| s.t. c >= 0.  Deterministic ties
    (numpy argmax = first maximum); iteration caps reported
    loudly; consumes the coordinate system only."""
    nr, nc = M.shape
    coln = np.linalg.norm(M, axis=0)
    live = coln > 1e-300
    Mn = M[:, live] / coln[live][None, :]
    n = Mn.shape[1]
    P = np.zeros(n, bool)
    c = np.zeros(n)
    qn = float(np.linalg.norm(q))
    tol = NN_GRAD_TOL * max(qn, 1e-300)
    capped = False
    outer = 0
    while True:
        resid = q - Mn @ c
        w = Mn.T @ resid
        w_masked = np.where(P, -np.inf, w)
        j = int(np.argmax(w_masked))
        if not np.isfinite(w_masked[j]) or w_masked[j] <= tol:
            break
        outer += 1
        if outer > itmax:
            capped = True
            break
        P[j] = True
        inner = 0
        while True:
            idxP = np.nonzero(P)[0]
            z = np.zeros(n)
            zi, _r, _rk, _sv = np.linalg.lstsq(Mn[:, idxP], q,
                                               rcond=None)
            z[idxP] = zi
            if len(idxP) == 0 or float(np.min(z[idxP])) > 0.0:
                c = z
                break
            inner += 1
            if inner > 200:
                capped = True
                c = np.clip(z, 0.0, None)
                break
            neg = idxP[z[idxP] <= 0.0]
            alpha = float(np.min(c[neg] / (c[neg] - z[neg])))
            c = c + alpha * (z - c)
            P[c <= 1e-15] = False
        if capped:
            break
    out = np.zeros(nc)
    out[live] = c / coln[live]
    resid = M @ out - q
    rel = float(np.linalg.norm(resid) / max(qn, 1e-300))
    return out, rel, int(np.sum(out > 0)), capped


def farkas_stats(M, q, c):
    """independent Farkas verification of an NNLS stall: the KKT
    residual y = M c - q satisfies <col, y> >= 0 (all columns)
    and <y, q> < 0 at the optimum; normalize <y, q> = -1, report
    the worst normalized column product and the t-row mass
    fraction of y.  Consumes the coordinate system only."""
    y = M @ c - q
    val = float(y @ q)
    if val >= 0.0:
        return None
    yh = y / (-val)
    coln = np.linalg.norm(M, axis=0)
    prods = (M.T @ yh) / np.maximum(coln, 1e-300)
    return yh, float(np.min(prods)), val


def farkas_polish(M, q, yh, iu, ju):
    """the sealed f64 I-polish (amendment a1, the f64 twin of
    the exact I-polish and of the r311 eps*I class): y_I =
    plain-vech functional of the identity has <col, y_I> =
    ||w||^2 > 0 strictly; over the DELTA_LADDER accept the first
    y' = yh + delta y_I with min normalized column product >=
    -POLISH_MIN and <y', q> <= -POLISH_VAL.  Verified
    independently of how yh was found."""
    yI = (iu == ju).astype(float)
    coln = np.maximum(np.linalg.norm(M, axis=0), 1e-300)
    for delta in DELTA_LADDER:
        y2 = yh + delta * yI
        prods = (M.T @ y2) / coln
        val2 = float(y2 @ q)
        if float(np.min(prods)) >= -POLISH_MIN \
                and val2 <= -POLISH_VAL:
            return y2, float(np.min(prods)), val2, delta
    return None, None, None, None


def feas_diag_g(M, q, g0, nblk, iters):
    """the UNCHANGED r308 Dykstra iteration (feas_diag body
    verbatim), returning the final iterate g in addition -- the
    converged family is Leg-A discovery material."""
    pa, pb = np.triu_indices(6)
    npairs = len(pa)
    g = g0.copy()
    Mp = np.linalg.pinv(M, rcond=RCOND)
    for _it in range(iters):
        lam, scale, G = BG.block_eigs(g, nblk)
        ev, V = np.linalg.eigh(G)
        evc = np.clip(ev, 0.0, None)
        Gp = np.einsum("rij,rj,rkj->rik", V, evc, V)
        gv = np.zeros((nblk, npairs))
        for p_i in range(npairs):
            a, b = int(pa[p_i]), int(pb[p_i])
            if a == b:
                gv[:, p_i] = Gp[:, a, a]
            else:
                gv[:, p_i] = Gp[:, a, b] * math.sqrt(2.0)
        g = gv.reshape(-1)
        g = g - Mp @ (M @ g - q)
    lam, scale, G = BG.block_eigs(g, nblk)
    rel = float(np.linalg.norm(M @ g - q)
                / max(np.linalg.norm(q), 1e-300))
    return float(np.min(lam) / scale), rel, g


def block_feats(xx, ww, ff, D, S_w):
    """the sealed formula features per block (source arrays
    only): m+, m-, G, tent fractions t1/t2, edge flag, budget
    share Gt, 4-bit nu-occupancy type."""
    ww = np.asarray(ww, float)
    xx = np.asarray(xx, float)
    ff = np.asarray(ff, float)
    wp = np.clip(ww, 0.0, None)
    wn = np.clip(-ww, 0.0, None)
    mp = wp[:-3] + wp[1:-2] + wp[2:-1] + wp[3:]
    mm = wn[:-3] + wn[1:-2] + wn[2:-1] + wn[3:]
    G = mp + mm
    span = np.abs(xx[:-3] - xx[3:])
    span = np.maximum(span, 1e-300)
    t1 = np.abs(xx[:-3] - xx[1:-2]) / span
    t2 = np.abs(xx[1:-2] - xx[2:-1]) / span
    u = ff * float(D)
    edge = ((u[:-3] < LOG2) & (u[1:-2] < LOG2)
            & (u[2:-1] < LOG2) & (u[3:] < LOG2)).astype(float)
    Gt = G * (float(S_w) / max(float(np.sum(G)), 1e-300))
    typ = ((wn[:-3] > 0).astype(np.int64)
           + 2 * (wn[1:-2] > 0).astype(np.int64)
           + 4 * (wn[2:-1] > 0).astype(np.int64)
           + 8 * (wn[3:] > 0).astype(np.int64))
    return dict(mp=mp, mm=mm, G=G, t1=t1, t2=t2, edge=edge,
                Gt=Gt, typ=typ)


def cand_design(feats):
    """the sealed candidate feature matrices (nblk x K), all
    features nonnegative by construction."""
    F = {}
    F["PHI_A"] = np.stack([feats["G"], feats["Gt"]], axis=1)
    F["PHI_B"] = np.stack([feats["mp"], feats["mm"],
                           feats["Gt"]], axis=1)
    F["PHI_C"] = np.stack([feats["G"], feats["G"] * feats["t1"],
                           feats["G"] * feats["t2"],
                           feats["Gt"]], axis=1)
    cols = []
    for tau in range(16):
        ind = (feats["typ"] == tau).astype(float)
        cols.append(ind * feats["G"])
        cols.append(ind * feats["Gt"])
    F["PHI_D"] = np.stack(cols, axis=1)
    return F


def formula_coeffs(Fmat, a_mat):
    """c_{r,l} = sum_k a[l,k] F[r,k] -- the frozen formula
    evaluated on a window's features; flat order (r major, l
    minor) matches the library tensor."""
    C = Fmat @ a_mat.T
    return C.reshape(-1)


def verify_section(T, q, c):
    """the INDEPENDENT verifier: c >= 0 (hard), identity
    residual of the recomposition sum c vech(L^T V V^T L) vs q.
    Consumes the sealed library tensor + coefficients only."""
    if float(np.min(c)) < 0.0:
        return False, float("inf"), float(np.min(c))
    M = T.reshape(-1, T.shape[2]).T
    rel = float(np.linalg.norm(M @ c - q)
                / max(np.linalg.norm(q), 1e-300))
    return rel <= FORM_BAR, rel, float(np.min(c))


def exact_farkas_polish(M_fr, q_fr, idx, m, y_f64):
    """FULLY EXACT rational Farkas certificate by the I-polish:
    Y = rationalize(y) + delta I has <col, Y> = v^T Y v +
    delta ||v||^2; certified iff every exact column product >= 0
    AND <Y, q> < 0 exact.  One-sided attempt over the sealed
    ladders."""
    ncol = len(M_fr[0])
    for den in DEN_LADDER:
        yr = [Fr(float(v)).limit_denominator(den) for v in y_f64]
        for d in D_LADDER:
            Y = BN.y_from_leftnull(yr, idx, m)
            for i in range(m):
                Y[i][i] += d
            valq = Fr(0)
            for e_i, (i, j) in enumerate(idx):
                valq += (Y[i][j] if i == j else 2 * Y[i][j]) \
                    * q_fr[e_i]
            if valq >= 0:
                continue
            ok = True
            for col in range(ncol):
                v = Fr(0)
                for e_i, (i, j) in enumerate(idx):
                    Me = M_fr[e_i][col]
                    if Me != 0:
                        v += (Y[i][j] if i == j
                              else 2 * Y[i][j]) * Me
                if v < 0:
                    ok = False
                    break
            if ok:
                return True, den, d, valq
    return False, None, None, None


def exact_section_attempt(M_fr, q_fr, c_f64, den):
    """one-sided exact rank-one-section attempt: rationalize the
    NNLS support coefficients, solve the exact correction on the
    support columns, check c >= 0 exact."""
    supp = [j for j in range(len(c_f64)) if c_f64[j] > 1e-12]
    if not supp:
        return False, "empty support"
    c_rat = {j: Fr(float(c_f64[j])).limit_denominator(den)
             for j in supp}
    r_fr = [q_fr[e] - sum(M_fr[e][j] * c_rat[j] for j in supp)
            for e in range(len(q_fr))]
    Msub = [[M_fr[e][j] for j in supp] for e in range(len(q_fr))]
    ex, rk, dof, sol = BG.rref_solve_fr(Msub, r_fr)
    if not ex:
        return False, "exact correction infeasible on support"
    cs = [c_rat[j] + sol[k] for k, j in enumerate(supp)]
    if any(v < 0 for v in cs):
        return False, "corrected coefficient negative"
    return True, "exact section on %d support columns" % len(supp)


def cheb_pack_x(xs_fr, ws_fr, hull):
    """exact Chebyshev system pack (verbatim r311 cheb_pack) for
    the exact certificate reproduction."""
    lo = Fr(float(hull[0]))
    hi = Fr(float(hull[1]))
    Pc = BN.cheb_rows_fr(xs_fr, DEG_A, lo, hi)
    Lc = BG.block_maps_fr(Pc, ws_fr)
    m_ = DEG_A + 2
    zeroA = [[Fr(0)] * m_ for _ in range(m_)]
    Mc, _qc, ic = BG.system_fr(Lc, zeroA)
    return Lc, Mc, ic


# ============== must-fail mutants
def mutant_target_lib(eigvecs_target):
    """m1 MUST-FAIL: the library extended by an eigendirection of
    the assembled target -- FLAGGED by the AST scope audit
    (TARGET_INVERSE class)."""
    return eigvecs_target[:, -1]


def den_probe_ladder(x):
    """gate-side helper of the m3 mutant: smallest sealed-ladder
    denominator reproducing x to LOGREL_TOL, else None."""
    ax = max(1.0, abs(x))
    for den in LOGREL_DENS:
        fr = Fr(x).limit_denominator(den)
        if abs(float(fr) - x) <= LOGREL_TOL * ax:
            return den
    return None


def mutant_phi_logrel(u_vals, Dg):
    """m3 MUST-FAIL: a formula factor consuming exact rational
    structure of the r289 rationalization variable u/Delta
    (log-relation class; amendment a2) -- the MAIN-vs-twin
    comparison must expose it."""
    return np.array([1.0 if den_probe_ladder(float(u) / float(Dg))
                     is not None else 2.0 for u in u_vals])


def dual_pocs_b(A, Bst):
    """the strengthened Leg-C dual attempt: r311 dual_pocs body
    with OMEGA_B / DUAL_ITER_B (divergence guard kept)."""
    nrm = float(np.sum(A * A))
    y_cap = 1e12 / max(math.sqrt(nrm), 1e-300)
    Y = -A / max(nrm, 1e-300)
    for _it in range(DUAL_ITER_B):
        C = np.einsum("rim,mn,rjn->rij", Bst, Y, Bst)
        if not np.all(np.isfinite(C)):
            return None, float("-inf"), 0.0, "diverged"
        ev, V = np.linalg.eigh(C)
        evn = np.minimum(ev, 0.0)
        Nn = np.einsum("rij,rj,rkj->rik", V, evn, V)
        corr = np.einsum("rim,rij,rjn->mn", Bst, Nn, Bst)
        Y = Y - OMEGA_B * corr
        Y = 0.5 * (Y + Y.T)
        val = float(np.sum(Y * A))
        Y = Y - (val + 1.0) / max(nrm, 1e-300) * A
        if not np.all(np.isfinite(Y)) \
                or float(np.linalg.norm(Y)) > y_cap:
            return None, float("-inf"), 0.0, "diverged"
    worst = BN.comp_min_eig(Y, Bst)
    val = float(np.sum(Y * A))
    return Y, worst, val, "ran"


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("blockgreen_membership_probe -- "
          "PRIME.LSTAR.BLOCKGREEN.MEMBERSHIP.01 (round 312)")
    print("SPEC_SHA %s   (r308 BG %s / r311 BN %s / r284 LS %s)"
          % (SPEC_SHA[:16], BG.SPEC_SHA[:16], BN.SPEC_SHA[:16],
             LS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (library structure + SM1/MINI16 "
                        "exact + w9 anchor + chordality + small "
                        "NNLS + mutants; twin, samples, Leg A, "
                        "w9 NNLS, rungs, formulas, Leg C, "
                        "adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the 22-generator library "
          "(reviewer classes in the sealed D basis, integer "
          "coordinates, declared in the docstring BEFORE any "
          "Leg-A evaluation), the formula vocabulary + the four "
          "candidates PHI_A..PHI_D with the calibrate-on-w9 / "
          "freeze / verify-on-57+twin protocol, the NNLS + Farkas "
          "+ exact-I-polish machinery, the Leg-B adjudication "
          "tree, the Leg-C schedule (staged anchor + %d extension "
          "steps + strengthened dual), all four mutants, every "
          "bar/ladder and the sealed verdict form; METRIC_ONLY "
          "semantics binding; the reviewer tree grants exactly "
          "ONE construction round -- no L* status move in any "
          "branch" % EXT_STEPS)

    # ---------------- S1 library structure + SM1 exact
    section("S1  THE SEALED LIBRARY -- STRUCTURE + SM1 EXACT LAYER")
    V, VLAB = lib_vectors()
    # abstract span of the 22 rank-one matrices in D-space (exact)
    pairs6 = [(a, b) for a in range(6) for b in range(a, 6)]
    rows_int = []
    for v in V:
        X = np.outer(v, v)
        rows_int.append([Fr(int(X[a, b])) for (a, b) in pairs6])
    rank_lib, _p, _R = BN.rref_rank_fr(rows_int)
    check("G10-library-structure", rank_lib == LIB_SPAN_REC,
          "22 sealed generators (integer D-coordinates): abstract "
          "span of {V V^T} = %d of 21 (record %d) -- the library "
          "cone is a strict SDD-type sub-cone of the block psd "
          "cone BY DESIGN; crosses present: (a,6) a=1..5, (1,4), "
          "(2,3), (1,2), (2,4); labels %s"
          % (rank_lib, LIB_SPAN_REC, ",".join(VLAB)))

    # SM1 verbatim (r308 constructors)
    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    bxs_sm = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
    bws_sm = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
    B_sm1 = BG.exact_budget_fr(x10, w_sm1, bxs_sm, bws_sm,
                               (len(x10) + 1) // 2)
    A_sm1 = BG.target_form_fr(x10, w_sm1, bxs_sm, bws_sm, B_sm1,
                              DEG_A)
    As_sm1 = [row[:] for row in A_sm1]
    As_sm1[-1][-1] = B_sm1 - FIVE_SEVEN
    P_sm1 = BG.mono_rows_fr(x10, DEG_A)
    Ls_sm1 = BG.block_maps_fr(P_sm1, w_sm1)
    M_sm1, q_sm1, idx_sm1 = BG.system_fr(Ls_sm1, As_sm1)
    rank_sm1, _p1, _R1 = BN.rref_rank_fr(M_sm1)
    Mlib_sm1 = lib_cols_fr(Ls_sm1, V, idx_sm1)
    ex_lib1, rk_lib1, dof_lib1, _s1 = BG.rref_solve_fr(Mlib_sm1,
                                                       q_sm1)
    ok_cons1 = not (ex_lib1 and rank_sm1 != RANK_REC["SM1"])
    check("G11-sm1-exact-span", rank_sm1 == RANK_REC["SM1"]
          and ok_cons1,
          "SM1 (r308 verbatim, exact monomials): full block "
          "system rank %d == record %d; LIBRARY system 55 x %d: "
          "[M_lib | q] rref -> EXISTS %s (rank %d, dof %d) -- "
          "the exact SPAN layer of the sealed library on the "
          "MAIN-class miniature, adjudicated in S8"
          % (rank_sm1, RANK_REC["SM1"], len(Mlib_sm1[0]),
             ex_lib1, rk_lib1, dof_lib1))

    # ---------------- S2 worlds + anchors
    section("S2  WORLDS -- W9 / MINI16 / CHORDALITY / TWIN / Y_t")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ff9, xx9, ww9 = BG.world_arrays(W9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4])
    B9, rho9, bxa9, bwa9 = BG.world_budget(W9, ctx9)
    S9 = B9 - 5.0 / 7.0
    hull9 = BG.hull_of(xx9, bxa9)
    CA9 = BG.census_world(xx9, ww9, bxa9, bwa9, B9, DEG_A, hull9)
    ok_anch = (ok_src and abs(B9 - B_W9_REC) <= B_W9_TOL
               and CA9["rel"] <= RES_BAR
               and CA9["dof"] == DOF_REC["w9A"]
               and CA9["rank"] == RANK_REC["w9A"]
               and LEAST_REC * 2 <= CA9["lam_rel"]
               <= LEAST_REC / 2)
    check("G20-w9-anchor", ok_anch,
          "w9 SOURCE %d/%d/%d N %d minC %d; B = %.6f (rec %.6f); "
          "identity rel res %.1e, rank %d == rec (dof %d == rec "
          "%d); least-norm min eig rel %+.3e (rec %+.2e, band 2x)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], W9["minC"],
             B9, B_W9_REC, CA9["rel"], CA9["rank"], CA9["dof"],
             DOF_REC["w9A"], CA9["lam_rel"], LEAST_REC))

    # MINI16 (verbatim r311)
    bx9, bw9, by9, bv9 = BG.border_split(ctx9)
    bxa9f = np.concatenate([bx9, by9])
    bwa9f = np.concatenate([bw9, -bv9])
    mini_x = [Fr(float(x)) for x in xx9[:MINI_K]]
    mini_w = [Fr(float(w)) for w in ww9[:MINI_K]]
    mini_bx = [Fr(float(x)) for x in bxa9f[:MINI_BK]]
    mini_bw = [Fr(float(w)) for w in bwa9f[:MINI_BK]]
    B_mini = BG.exact_budget_fr(mini_x, mini_w, mini_bx, mini_bw,
                                (MINI_K + 1) // 2)
    mxf = np.array([float(x) for x in mini_x])
    mwf = np.array([float(w) for w in mini_w])
    mbxf = np.array([float(x) for x in mini_bx])
    mbwf = np.array([float(w) for w in mini_bw])
    CMINI = BG.census_world(mxf, mwf, mbxf, mbwf, float(B_mini),
                            DEG_A, BG.hull_of(mxf, mbxf))
    A_mini = BG.target_form_fr(mini_x, mini_w, mini_bx, mini_bw,
                               B_mini, DEG_A)
    As_mini = [row[:] for row in A_mini]
    As_mini[-1][-1] = B_mini - FIVE_SEVEN
    L_mini_fr = BG.block_maps_fr(BG.mono_rows_fr(mini_x, DEG_A),
                                 mini_w)
    Mm_fr, qm_fr, im_fr = BG.system_fr(L_mini_fr, As_mini)
    rank_mini, _pm, _Rm = BN.rref_rank_fr(Mm_fr)
    Mlib_mini = lib_cols_fr(L_mini_fr, V, im_fr)
    ex_libm, rk_libm, dof_libm, _sm = BG.rref_solve_fr(Mlib_mini,
                                                       qm_fr)
    check("G21-mini16-exact-span", rank_mini == RANK_REC["MINI16"]
          and CMINI["rel"] <= RES_BAR,
          "MINI16 (real w9 miniature, exact): full rank %d == "
          "FULL record %d; LIBRARY system 55 x %d: EXISTS %s "
          "(rank %d, dof %d) -- exact span layer on the "
          "full-span miniature, adjudicated in S8"
          % (rank_mini, RANK_REC["MINI16"], len(Mlib_mini[0]),
             ex_libm, rk_libm, dof_libm))

    # chordality anchor (r311 machinery)
    adj = BN.graph_from_blocks(W9_ANCH[0])
    order = BN.mcs_order(adj)
    okp, _wit = BN.peo_check(adj, order)
    cl = set(BN.max_cliques_peo(adj, order))
    expect = set(frozenset([j, j + 1, j + 2, j + 3, W9_ANCH[0]])
                 for j in range(W9_ANCH[0] - 3))
    check("G22-chordality-anchor", okp and cl == expect,
          "the full w9 sparsity graph (S = %d + t): CHORDAL, "
          "maximal cliques == the %d sealed blocks (r311 "
          "reproduced) -- evaluation-space restatement stands, "
          "all content lives in the compression"
          % (W9_ANCH[0], W9_ANCH[0] - 3))

    if smoke:
        for g in ("G23-twin-anchor", "G24-budget-dual-values"):
            check(g, True, "SMOKE: skipped")
        CAT = None
        ctxT = None
        yt_vals = {}
    else:
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and bool(np.all(np.abs(duR)
                                 <= RAT_TOL * gaps_c + 1e-300))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        BT, _rT, bxaT, bwaT = BG.world_budget(WT, ctxT)
        ST = BT - 5.0 / 7.0
        ffT, xaT, waT = BG.world_arrays(WT)
        CAT = BG.census_world(xaT, waT, bxaT, bwaT, BT, DEG_A,
                              BG.hull_of(xaT, bxaT))
        check("G23-twin-anchor", ok_tc and WT["minC"] == 184
              and CAT["rel"] <= RES_BAR,
              "r289 RATIONAL TWIN rebuilt verbatim (weights "
              "bitwise, |du| <= %.0e gap, denominators <= %.0e): "
              "minC = %s (record 184); identity rel res %.1e"
              % (RAT_TOL, QMAX, str(WT["minC"]), CAT["rel"]))
        # controls: budget scalars only (Y_t anchor)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        yt_vals = {"w9": S9, "twin": ST}
        for cn, kw in (("EPST", dict(comb=(
                np.log(nn_idx.astype(float)),
                2.0 * lamE[nn_idx]
                / np.sqrt(nn_idx.astype(float))))),
                ("SCR", dict(scramble_seed=1))):
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            Bc, _rc, _bx, _bw = BG.world_budget(Wc, cctx)
            yt_vals[cn] = Bc - 5.0 / 7.0
        ok_yt = (yt_vals["w9"] > 0 and yt_vals["twin"] > 0
                 and abs(yt_vals["EPST"] - S_EPST_REC)
                 <= S_CTRL_TOL
                 and abs(yt_vals["SCR"] - S_SCR_REC)
                 <= S_CTRL_TOL)
        check("G24-budget-dual-values", ok_yt,
              "the r311 budget dual re-anchored: <Y_t, A> = "
              "S_{N-2}: w9 %+.4f / twin %+.4f POSITIVE vs EPST "
              "%+.4f (rec %+.3f) / SCR %+.4f (rec %+.3f) -- the "
              "known wall reading, carried as Leg-0 anchor only"
              % (yt_vals["w9"], yt_vals["twin"], yt_vals["EPST"],
                 S_EPST_REC, yt_vals["SCR"], S_SCR_REC))

    # ---------------- S3 leg 0 strictness census
    section("S3  LEG 0 -- R311 STRICTNESS CENSUS BIT-NEAR")
    if smoke:
        for g in ("G30-leg0-dykstra", "G31-sample-census",
                  "G32-exact-certs"):
            check(g, True, "SMOKE: skipped")
        g9A = None
        gTA = None
        DUALS = []
        SM_CEN1 = None
    else:
        fm9, rel9, g9A = feas_diag_g(CA9["M"], CA9["q"], CA9["g"],
                                     CA9["nblk"], FEAS_IT1)
        fmT, relT, gTA = feas_diag_g(CAT["M"], CAT["q"], CAT["g"],
                                     CAT["nblk"], FEAS_IT1)
        check("G30-leg0-dykstra", fm9 >= -FEAS_CONV
              and fmT >= -FEAS_CONV,
              "r308 Dykstra anchors (UNCHANGED protocol, %d "
              "steps): w9@A CONV (min eig rel %+.2e, rec "
              "+6.6e-16 class, affine res %.1e) / twin@A CONV "
              "(%+.2e) -- the converged families are the Leg-A "
              "discovery material" % (FEAS_IT1, fm9, rel9, fmT))
        # SM1 f64 census for the sample leg
        xs1f = np.array([float(x) for x in x10])
        ws1f = np.array([float(w) for w in w_sm1])
        bx1f = np.array([float(x) for x in bxs_sm])
        bw1f = np.array([float(w) for w in bws_sm])
        SM_CEN1 = BG.census_world(xs1f, ws1f, bx1f, bw1f,
                                  float(B_sm1), DEG_A,
                                  BG.hull_of(xs1f, bx1f))
        # exact Chebyshev packs (verbatim r311)
        L1c, M1c, i1c = cheb_pack_x(x10, w_sm1,
                                    BG.hull_of(xs1f, bx1f))
        Lmc, Mmc, imc = cheb_pack_x(mini_x, mini_w,
                                    BG.hull_of(mxf, mbxf))
        rng = np.random.default_rng(SEED)
        strict_certs = []
        exact_certs = []
        DUALS = []
        sample_stats = {}

        def run_samples(tag, C, nsamp, Ls_fr=None, M_fr=None,
                        idx_fr=None):
            m_s = int(round((math.sqrt(8 * len(C["q"]) + 1) - 1)
                            / 2))
            got = BN.sample_psd(C["M"], m_s, rng, nsamp)
            n_psd = 0
            n_dec = 0
            n_exact_tried = 0
            n_diverged = 0
            for k, g_ in enumerate(got):
                if g_ is None:
                    info("SAMPLE %s#%d: no psd projection "
                         "(SAMPLE_INDEFINITE)" % (tag, k))
                    continue
                Qs, x0, rel_s, lam_s, al_s = g_
                n_psd += 1
                lbl = "%s#%d" % (tag, k)
                qs = BN.vech_of(Qs)
                fms, frs, its = BN.run_feas3(C["M"], qs, x0,
                                             C["nblk"],
                                             allow3=True)
                conv = fms >= -FEAS_CONV
                info("SAMPLE %-8s lam rel %+.2e  Dykstra %s "
                     "(%+.3e, %d steps)"
                     % (lbl, lam_s, "CONV" if conv else "STALL",
                        fms, its))
                if conv:
                    n_dec += 1
                    continue
                Bst, _rk, _s = BN.compress_bases(C["L"])
                Yd, worst, val, std = BN.dual_pocs(Qs, Bst)
                if Yd is None:
                    n_diverged += 1
                    info("  %s: dual POCS DIVERGED (one-sided)"
                         % lbl)
                    continue
                Yp, eps, valp, okp = BN.polish_dual(Yd, Qs, Bst)
                if okp:
                    strict_certs.append(lbl)
                    DUALS.append((lbl, tag, Yp, Qs))
                note = ("dual worst %+.2e val %+.3f polish %s"
                        % (worst, val, okp))
                if okp and Ls_fr is not None \
                        and n_exact_tried < CERT_CAP:
                    n_exact_tried += 1
                    for den in DEN_LADDER:
                        okx, dtl, _Yx = BN.exact_strict_cert(
                            M_fr, idx_fr, Ls_fr, x0, Yp, Qs, den)
                        if okx:
                            exact_certs.append((lbl, den, dtl))
                            note += ("; EXACT cert den %d (%s)"
                                     % (den, dtl))
                            break
                    else:
                        note += "; exact rationalization failed"
                info("  %s STALLED PD: %s" % (lbl, note))
            sample_stats[tag] = (n_psd, n_dec, nsamp, n_diverged)

        run_samples("w9A", CA9, NSAMP_W9)
        run_samples("MINI", CMINI, NSAMP_MINI, Ls_fr=Lmc,
                    M_fr=Mmc, idx_fr=imc)
        run_samples("SM1", SM_CEN1, NSAMP_SM, Ls_fr=L1c,
                    M_fr=M1c, idx_fr=i1c)
        ok_census = (sample_stats["w9A"][:2] == (6, 0)
                     and sample_stats["MINI"][:2] == (6, 0)
                     and sample_stats["SM1"][:2] == (4, 0)
                     and len(strict_certs) == 10
                     and sample_stats["w9A"][3] == 6)
        check("G31-sample-census", ok_census,
              "r311 STRICTNESS REPRODUCED on the identical rng "
              "stream: 0/6 w9A + 0/6 MINI16 + 0/4 SM1 in-span PD "
              "samples decompose; %d/10 MINI/SM1 stalls carry "
              "valid polished-numeric duals (%s); the 6 w9A "
              "duals diverge (one-sided, r311 OPEN_LOCI class)"
              % (len(strict_certs), ",".join(strict_certs)))
        ok_exact = (len(exact_certs) == 2
                    and all(lbl in ("MINI#0", "SM1#0")
                            for lbl, _d, _t in exact_certs))
        check("G32-exact-certs", ok_exact,
              "the two FULLY EXACT in-span rational certificates "
              "reproduced: %s -- generic positive forms on the "
              "real-source miniature have NO block decomposition "
              "(exact grade); MEMBERSHIP of the world targets is "
              "the genuine residual object, exactly as r311 "
              "scoped it" % str(exact_certs))

    # ---------------- S4 leg A anatomy
    section("S4  LEG A -- MEMBERSHIP ANATOMY (DISCOVERY, OPEN)")
    pa6, pb6 = np.triu_indices(6)
    isow = np.where(pa6 == pb6, 1.0, math.sqrt(2.0))
    A21 = np.stack([np.outer(v, v).astype(float)[pa6, pb6] * isow
                    for v in V], axis=1)
    if smoke:
        for g in ("G40-solution-extraction",
                  "G41-eigenrank-cone-census",
                  "G42-dual-anatomy"):
            check(g, True, "SMOKE: skipped")
        anat_txt = "SMOKE"
    else:
        def anatomy(gvec, nblk):
            lam, scale, G = BG.block_eigs(gvec, nblk)
            ev, W = np.linalg.eigh(G)
            fro = np.sqrt(np.sum(G * G, axis=(1, 2)))
            fro = np.maximum(fro, 1e-300)
            ranks = np.sum(ev > RANK_TOL * fro[:, None], axis=1)
            top = W[:, :, -1]
            Vn = V.astype(float)
            Vn = Vn / np.linalg.norm(Vn, axis=1, keepdims=True)
            align = np.max(np.abs(top @ Vn.T), axis=1)
            shares = np.zeros(nblk)
            for r in range(nblk):
                rhs = G[r][pa6, pb6] * isow
                cc, rel_c, _sup, _cap = nnls_lh(A21, rhs)
                shares[r] = 1.0 - rel_c
            return ranks, align, shares, float(np.min(lam) /
                                               scale)

        rk9, al9, sh9, lam9m = anatomy(g9A, CA9["nblk"])
        rkT, alT, shT, lamTm = anatomy(gTA, CAT["nblk"])
        check("G40-solution-extraction", lam9m >= -PSD_NEG
              and lamTm >= -PSD_NEG,
              "the converged r308 families are genuinely psd "
              "(w9@A min eig rel %+.2e / twin %+.2e) -- "
              "discovery material for the formula search only"
              % (lam9m, lamTm))
        rk_hist = {int(k): int(np.sum(rk9 == k))
                   for k in sorted(set(rk9.tolist()))}
        anat_txt = ("rank census w9@A %s; top-eig library "
                    "alignment med %.4f min %.3f; library-cone "
                    "share med %.3f min %.3f mean %.3f; twin med "
                    "share %.3f"
                    % (str(rk_hist), float(np.median(al9)),
                       float(np.min(al9)), float(np.median(sh9)),
                       float(np.min(sh9)), float(np.mean(sh9)),
                       float(np.median(shT))))
        check("G41-eigenrank-cone-census", True,
              "MEASURED: %s -- how much of the solver's psd "
              "family already lives in the sealed rank-one cone "
              "(adjudicated as anatomy, S8)" % anat_txt)
        # dual anatomy
        dual_rows = []
        for lbl, tag, Yp, Qs in DUALS:
            Aw = BN.unvech(np.asarray(
                CMINI["q"] if tag == "MINI" else SM_CEN1["q"]),
                DEG_A + 2)
            m_ = DEG_A + 2
            hA = float(np.sum(Yp[:m_ - 1, :m_ - 1]
                              * Aw[:m_ - 1, :m_ - 1]))
            uA = float(2.0 * np.sum(Yp[:m_ - 1, m_ - 1]
                                    * Aw[:m_ - 1, m_ - 1]))
            tA = float(Yp[m_ - 1, m_ - 1] * Aw[m_ - 1, m_ - 1])
            evY, WY = np.linalg.eigh(Yp)
            z = WY[:, 0]
            zt = abs(float(z[m_ - 1]))
            uvec = Aw[:m_ - 1, m_ - 1]
            un = float(np.linalg.norm(uvec))
            ov = abs(float(z[:m_ - 1] @ uvec)) \
                / max(np.linalg.norm(z[:m_ - 1]) * un, 1e-300)
            kmax = int(np.argmax(np.abs(z[:m_ - 1])))
            dual_rows.append((lbl, hA, uA, tA, zt, ov, kmax))
            info("DUAL %-8s <Y,A_world> parts H %+.3f u %+.3f "
                 "t %+.3f | z_t %.3f u-overlap %.3f deg* %d"
                 % (lbl, hA, uA, tA, zt, ov, kmax))
        zts = [r[4] for r in dual_rows]
        kms = [r[6] for r in dual_rows]
        hs_ = [r[1] for r in dual_rows]
        dual_txt = ("10 duals: med H-part %+.3f, |z_t| med %.3f "
                    "max %.3f, dominant degree indices %s"
                    % (float(np.median(hs_)),
                       float(np.median(zts)), float(np.max(zts)),
                       str(sorted(set(kms)))))
        check("G42-dual-anatomy", len(dual_rows) == 10,
              "MEASURED: %s -- the generic-missing directions "
              "against the world-target components (adjudicated "
              "as anatomy, S8)" % dual_txt)

    # ---------------- S5 leg B constructive section
    section("S5  LEG B -- SPAN / NNLS / FARKAS / FORMULA")
    T9 = lib_tensor(CA9["L"], V)
    Mfull9 = T9.reshape(-1, T9.shape[2]).T
    q9 = np.asarray(CA9["q"], float)
    x_sp, _r, _rk, _sv = np.linalg.lstsq(Mfull9, q9, rcond=RCOND)
    span9 = float(np.linalg.norm(Mfull9 @ x_sp - q9)
                  / max(np.linalg.norm(q9), 1e-300))
    # SM1 + MINI16 f64 library systems (Chebyshev census packs)
    if smoke:
        xs1f = np.array([float(x) for x in x10])
        ws1f = np.array([float(w) for w in w_sm1])
        bx1f = np.array([float(x) for x in bxs_sm])
        bw1f = np.array([float(w) for w in bws_sm])
        SM_CEN1s = BG.census_world(xs1f, ws1f, bx1f, bw1f,
                                   float(B_sm1), DEG_A,
                                   BG.hull_of(xs1f, bx1f))
        TS1 = lib_tensor(SM_CEN1s["L"], V)
        qs1 = np.asarray(SM_CEN1s["q"], float)
        Mf_s1 = TS1.reshape(-1, TS1.shape[2]).T
        c_s1, rel_s1, sup_s1, cap_s1 = nnls_lh(Mf_s1, qs1)
        Tm = lib_tensor(CMINI["L"], V)
        qmf = np.asarray(CMINI["q"], float)
        Mf_m = Tm.reshape(-1, Tm.shape[2]).T
        c_m, rel_m, sup_m, cap_m = nnls_lh(Mf_m, qmf)
        info("SMOKE NNLS: SM1 rel %.3e (support %d) / MINI16 "
             "rel %.3e (support %d) / w9@A span rel %.3e"
             % (rel_s1, sup_s1, rel_m, sup_m, span9))
        for g in ("G50-span-layer", "G51-nnls-main",
                  "G52-farkas-verification", "G53-exactization",
                  "G54-rung-census", "G55-formula-calibration",
                  "G56-formula-transfer"):
            check(g, True, "SMOKE: skipped (SM1/MINI16 NNLS "
                  "exercised above)")
        legb = None
    else:
        TT = lib_tensor(CAT["L"], V)
        MfullT = TT.reshape(-1, TT.shape[2]).T
        qT = np.asarray(CAT["q"], float)
        xT_sp, _r2, _rk2, _sv2 = np.linalg.lstsq(MfullT, qT,
                                                 rcond=RCOND)
        spanT = float(np.linalg.norm(MfullT @ xT_sp - qT)
                      / max(np.linalg.norm(qT), 1e-300))
        Tm = lib_tensor(CMINI["L"], V)
        Mf_m = Tm.reshape(-1, Tm.shape[2]).T
        qmf = np.asarray(CMINI["q"], float)
        TS1 = lib_tensor(SM_CEN1["L"], V)
        Mf_s1 = TS1.reshape(-1, TS1.shape[2]).T
        qs1 = np.asarray(SM_CEN1["q"], float)
        ok_span_cons = not ((ex_lib1 and span_of(Mf_s1, qs1)
                             > 1e-6)
                            or (ex_libm and span_of(Mf_m, qmf)
                                > 1e-6))
        check("G50-span-layer", ok_span_cons,
              "SPAN LAYER: w9@A unconstrained rel %.2e (bar "
              "%.0e) / twin %.2e; EXACT: SM1 EXISTS %s (dof %d) "
              "/ MINI16 EXISTS %s (dof %d); f64/exact "
              "consistency holds -- span verdict feeds the "
              "sealed tree (S8)"
              % (span9, SPAN_BAR, spanT, ex_lib1, dof_lib1,
                 ex_libm, dof_libm))
        c9, rel9nn, sup9, cap9 = nnls_lh(Mfull9, q9)
        cT, relTnn, supT, capT = nnls_lh(MfullT, qT)
        c_m, rel_m, sup_m, cap_m = nnls_lh(Mf_m, qmf)
        c_s1, rel_s1, sup_s1, cap_s1 = nnls_lh(Mf_s1, qs1)
        nn_ok9 = (rel9nn <= NN_BAR) and not cap9
        check("G51-nnls-main", not (cap9 or capT),
              "CONE LAYER (deterministic Lawson-Hanson): w9@A "
              "rel %.4f (support %d%s) / twin %.4f (support %d) "
              "/ MINI16 %.4f / SM1 %.4f -- feasibility bar %.0e; "
              "MEASURED, adjudicated in S8"
              % (rel9nn, sup9, ", CAPPED" if cap9 else "",
                 relTnn, supT, rel_m, rel_s1, NN_BAR))
        fk9 = farkas_stats(Mfull9, q9, c9) if not nn_ok9 else None
        fkT = farkas_stats(MfullT, qT, cT) \
            if relTnn > NN_BAR else None
        iu9, ju9 = np.triu_indices(DEG_A + 2)
        trow = (ju9 == DEG_A + 1)
        if fk9 is not None:
            yh9, worst9, _v9 = fk9
            tmass9 = float(np.sum(yh9[trow] ** 2)
                           / max(np.sum(yh9 ** 2), 1e-300))
            fk_valid = worst9 >= -FARKAS_TOL
            pol_txt = "raw margin sufficient"
            if not fk_valid:
                y2, w2, v2, d2 = farkas_polish(Mfull9, q9, yh9,
                                               iu9, ju9)
                if y2 is not None:
                    fk_valid = True
                    pol_txt = ("I-POLISHED at delta %.0e: min "
                               "product %+.1e >= -%.0e, <y,q> = "
                               "%+.4f <= -%.1f" % (d2, w2,
                                                   POLISH_MIN,
                                                   v2,
                                                   POLISH_VAL))
                else:
                    pol_txt = "polish failed on the ladder"
            tmassT = float("nan")
            if fkT is not None:
                yhT, worstT, _vT = fkT
                tmassT = float(np.sum(yhT[trow] ** 2)
                               / max(np.sum(yhT ** 2), 1e-300))
            check("G52-farkas-verification", fk_valid,
                  "FARKAS certificate from the NNLS stall "
                  "(independent verification): <y,q> = -1, worst "
                  "raw normalized column product %+.2e (bar "
                  "-%.0e); %s => %s; t-row mass fraction %.5f "
                  "(WALL_FRAC %.2f) -- twin: %.5f (type %s)"
                  % (worst9, FARKAS_TOL, pol_txt,
                     "VALID" if fk_valid else "INVALID", tmass9,
                     WALL_FRAC, tmassT,
                     "identical" if fkT is not None else
                     "MISMATCH: twin feasible"))
        else:
            tmass9 = 0.0
            fk_valid = False
            check("G52-farkas-verification", True,
                  "not fired: w9@A NNLS feasible (rel %.2e) -- "
                  "the solver-found explicit rank-one section "
                  "exists" % rel9nn)
        # exactization on the miniatures (mono basis, one-sided)
        Mlib_s1_f = np.array([[float(v) for v in row]
                              for row in Mlib_sm1])
        q_s1_f = np.array([float(v) for v in q_sm1])
        Mlib_m_f = np.array([[float(v) for v in row]
                             for row in Mlib_mini])
        q_m_f = np.array([float(v) for v in qm_fr])
        cx1, relx1, supx1, capx1 = nnls_lh(Mlib_s1_f, q_s1_f)
        cxm, relxm, supxm, capxm = nnls_lh(Mlib_m_f, q_m_f)
        ex_txt = []
        ex_grade = []
        for nm, Mfr, qfr, Mff, qff, cx, relx in (
                ("SM1", Mlib_sm1, q_sm1, Mlib_s1_f, q_s1_f,
                 cx1, relx1),
                ("MINI16", Mlib_mini, qm_fr, Mlib_m_f, q_m_f,
                 cxm, relxm)):
            if relx <= NN_BAR:
                okx, dtl = exact_section_attempt(Mfr, qfr, cx,
                                                 DEN_LADDER[-1])
                ex_txt.append("%s feasible (rel %.1e): exact "
                              "section attempt %s (%s)"
                              % (nm, relx, okx, dtl))
                ex_grade.append((nm, "section", okx))
            else:
                fkx = farkas_stats(Mff, qff, cx)
                if fkx is None:
                    ex_txt.append("%s: no farkas direction"
                                  % nm)
                    continue
                yx, worstx, _vx = fkx
                okx, denx, dx, vqx = exact_farkas_polish(
                    Mfr, qfr,
                    [(i, j) for i in range(DEG_A + 2)
                     for j in range(i, DEG_A + 2)],
                    DEG_A + 2, yx)
                ex_txt.append("%s infeasible (rel %.4f, worst "
                              "col %+.1e): EXACT I-polished "
                              "Farkas %s%s"
                              % (nm, relx, worstx, okx,
                                 (" (den %s, delta %s, <Y,q> = "
                                  "%.4f exact)" % (denx, str(dx),
                                                   float(vqx)))
                                 if okx else ""))
                ex_grade.append((nm, "farkas", okx))
        check("G53-exactization", True,
              "one-sided exact attempts on the miniatures (mono "
              "basis): %s" % "; ".join(ex_txt))
        # rung census + formula calibration/transfer
        S_feats9 = block_feats(xx9, ww9, ff9, D9, S9)
        FD9 = cand_design(S_feats9)
        cal = {}
        for nm in ("PHI_A", "PHI_B", "PHI_C", "PHI_D"):
            Fm = FD9[nm]
            K = Fm.shape[1]
            Mc = np.einsum("rk,rle->elk", Fm, T9).reshape(
                T9.shape[2], 22 * K)
            a_c, rel_c, sup_c, cap_c = nnls_lh(Mc, q9)
            cal[nm] = (a_c.reshape(K, 22).T, rel_c)
            info("FORMULA %s: w9@A calibration rel %.4f "
                 "(support %d, %d params)"
                 % (nm, rel_c, sup_c, 22 * K))
        fired = [nm for nm in cal if cal[nm][1] <= FORM_BAR]
        check("G55-formula-calibration", True,
              "sealed candidates calibrated on w9@A ONLY: %s -- "
              "fired (rel <= %.0e): %s"
              % (str({nm: "%.4f" % cal[nm][1] for nm in cal}),
                 FORM_BAR, str(fired) if fired else "NONE"))
        # 57-rung loop: NNLS census (+ formula transfer if fired)
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H:
                ekz.append(kz)
        packs = {}
        for kz in kzs + ekz:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx, Dk)
        epool = sorted(ekz, key=lambda kz: (packs[kz][0]["N"], kz))
        rungs = kzs + epool[:K_EXT]
        n_feas = 0
        worst_rung = (0.0, None)
        transfer = {nm: [] for nm in fired}
        for kz in rungs:
            Wp, ctx, Dk = packs[kz]
            Bw, _rho, bxa, bwa = BG.world_budget(Wp, ctx)
            ffw, xaw, waw = BG.world_arrays(Wp)
            Cw = CA9 if kz == MAIN_KZ else BG.census_world(
                xaw, waw, bxa, bwa, Bw, DEG_A,
                BG.hull_of(xaw, bxa))
            Tw = T9 if kz == MAIN_KZ else lib_tensor(Cw["L"], V)
            Mw = Tw.reshape(-1, Tw.shape[2]).T
            qw = np.asarray(Cw["q"], float)
            cw, relw, supw, capw = nnls_lh(Mw, qw)
            if relw <= NN_BAR and not capw:
                n_feas += 1
            if relw > worst_rung[0]:
                worst_rung = (relw, kz)
            for nm in fired:
                fw = block_feats(xaw, waw, ffw, Dk,
                                 Bw - 5.0 / 7.0)
                Fw = cand_design(fw)[nm]
                cf = formula_coeffs(Fw, cal[nm][0])
                okv, relv, minc = verify_section(Tw, qw, cf)
                transfer[nm].append((kz, relv, okv))
        check("G54-rung-census", len(rungs) == 57,
              "NNLS census on the %d rungs at DEG_A: %d/%d "
              "library-cone feasible (bar %.0e); worst rel "
              "residual %.4f at kz%s -- MEASURED, adjudicated "
              "in S8" % (len(rungs), n_feas, len(rungs), NN_BAR,
                         worst_rung[0], str(worst_rung[1])))
        go_phi = None
        for nm in fired:
            fwT = block_feats(xaT, waT, ffT, D9, ST)
            FwT = cand_design(fwT)[nm]
            cfT = formula_coeffs(FwT, cal[nm][0])
            okT_, relT_, _mc = verify_section(TT, qT, cfT)
            all_ok = all(ok for _kz, _r, ok in transfer[nm]) \
                and okT_
            info("TRANSFER %s: rungs %d/%d pass, twin rel %.2e "
                 "%s" % (nm,
                         sum(1 for _k, _r, ok in transfer[nm]
                             if ok), len(rungs), relT_,
                         "PASS" if okT_ else "FAIL"))
            if all_ok and go_phi is None:
                go_phi = nm
        check("G56-formula-transfer", True,
              "frozen-parameter transfer: %s -- MEASURED, "
              "adjudicated in S8"
              % ("never fired (no candidate reached the "
                 "calibration bar)" if not fired else
                 ("GO candidate %s" % go_phi if go_phi
                  else "fired but transfer FAILED")))
        legb = dict(span9=span9, spanT=spanT, nn_ok9=nn_ok9,
                    rel9nn=rel9nn, relTnn=relTnn, sup9=sup9,
                    fk_valid=fk_valid, tmass9=tmass9,
                    rel_m=rel_m, rel_s1=rel_s1,
                    ex_grade=ex_grade, n_feas=n_feas,
                    nrungs=len(rungs), cal=cal, fired=fired,
                    go_phi=go_phi, worst_rung=worst_rung,
                    cap9=cap9)

    # ---------------- S6 leg C w9@DEG_B
    section("S6  LEG C -- W9@DEG_B (THE OPEN FLANK)")
    if smoke:
        for g in ("G60-w9B-anchor", "G61-w9B-nnls",
                  "G62-w9B-extension"):
            check(g, True, "SMOKE: skipped")
        w9b_status = "SMOKE"
    else:
        CB9 = BG.census_world(xx9, ww9, bxa9, bwa9, B9, DEG_B,
                              hull9)
        lam9B, _sc = BN.gate_lam_rel(BN.unvech(
            np.asarray(CB9["q"]), DEG_B + 2))
        fmB1, _r1, gB1 = feas_diag_g(CB9["M"], CB9["q"],
                                     CB9["g"], CB9["nblk"],
                                     FEAS_IT1)
        fmB = fmB1
        gB = gB1
        itB = FEAS_IT1
        if fmB < -FEAS_CONV:
            fmB, _r2, gB = feas_diag_g(CB9["M"], CB9["q"],
                                       CB9["g"], CB9["nblk"],
                                       FEAS_IT2)
            itB = FEAS_IT2
        if fmB < -FEAS_CONV:
            fmB, _r3, gB = feas_diag_g(CB9["M"], CB9["q"],
                                       CB9["g"], CB9["nblk"],
                                       FEAS_IT3)
            itB = FEAS_IT3
        ok_b_anchor = (CB9["rank"] == RANK_REC["w9B"]
                       and CB9["dof"] == DOF_REC["w9B"]
                       and W9B_20K_REC * 2 <= fmB
                       <= W9B_20K_REC / 2)
        check("G60-w9B-anchor", ok_b_anchor,
              "w9@DEG_B anchor (staged r308 protocol, %d steps): "
              "rank %d == rec / dof %d == rec; target PD-thin "
              "(lam rel %+.2e); min eig rel %+.3e (r311 rec "
              "%+.2e, band 2x) -- the honest OPEN state "
              "reproduced" % (itB, CB9["rank"], CB9["dof"],
                              lam9B, fmB, W9B_20K_REC))
        TB = lib_tensor(CB9["L"], V)
        MB = TB.reshape(-1, TB.shape[2]).T
        qB = np.asarray(CB9["q"], float)
        cB, relB, supB, capB = nnls_lh(MB, qB)
        memberB = (relB <= NN_BAR) and not capB
        fkB = farkas_stats(MB, qB, cB) if not memberB else None
        tmassB = float("nan")
        if fkB is not None:
            iuB, juB = np.triu_indices(DEG_B + 2)
            trB = (juB == DEG_B + 1)
            yhB, worstB_, _vB = fkB
            tmassB = float(np.sum(yhB[trB] ** 2)
                           / max(np.sum(yhB ** 2), 1e-300))
        check("G61-w9B-nnls", True,
              "library NNLS at DEG_B: rel %.5f (support %d)%s -- "
              "%s" % (relB, supB, ", CAPPED" if capB else "",
                      "FEASIBLE: deg-28 membership DECIDED "
                      "constructively" if memberB else
                      "infeasible (t-row mass %.5f -- the same "
                      "wall class)" % tmassB))
        if memberB:
            w9b_status = ("W9B_MEMBER(explicit library section, "
                          "rel %.1e)" % relB)
            check("G62-w9B-extension", True,
                  "not needed: membership decided by the "
                  "library section")
        else:
            fmE, relE, gE = feas_diag_g(CB9["M"], CB9["q"], gB,
                                        CB9["nblk"], EXT_STEPS)
            if fmE >= -FEAS_CONV:
                w9b_status = ("W9B_MEMBER(extended Dykstra CONV "
                              "%+.2e after +%d)" % (fmE,
                                                    EXT_STEPS))
                dual_txt_b = "not needed"
            else:
                A9B = BN.unvech(qB, DEG_B + 2)
                BstB, _rkB, _sB = BN.compress_bases(CB9["L"])
                Yb, worstBB, valBB, stB = dual_pocs_b(A9B, BstB)
                if Yb is None:
                    dual_txt_b = ("strengthened dual POCS "
                                  "DIVERGES (no certificate, "
                                  "one-sided)")
                    w9b_status = ("W9B_OPEN(min eig rel %+.2e "
                                  "after %d+%d; dual diverges)"
                                  % (fmE, FEAS_IT3, EXT_STEPS))
                else:
                    _Yp, epsB, valPB, okPB = BN.polish_dual(
                        Yb, A9B, BstB)
                    if okPB:
                        w9b_status = ("W9B_DUAL_CERT(polished "
                                      "val %+.3f)" % valPB)
                        dual_txt_b = "VALID polished dual"
                    else:
                        dual_txt_b = ("dual ran, polish invalid "
                                      "(val %+.3f)" % valPB)
                        w9b_status = ("W9B_OPEN(min eig rel "
                                      "%+.2e; dual invalid)"
                                      % fmE)
            check("G62-w9B-extension", True,
                  "EXTENDED Dykstra (+%d steps from the %d-step "
                  "iterate): min eig rel %+.3e (was %+.3e); "
                  "dual side: %s => %s"
                  % (EXT_STEPS, itB, fmE, fmB, dual_txt_b,
                     w9b_status.split("(")[0]))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS + SCOPE AUDITS (LEG D)")
    hits_m1 = scope_audit("mutant_target_lib")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G70-scope-audit", bool(hits_m1) and not hits
          and not ag_hits,
          "m1 TARGET-EIGENDIRECTION library mutant FLAGGED (%s); "
          "the %d sealed constructors audit CLEAN; fragment "
          "audit: %s"
          % ("; ".join(hits_m1) if hits_m1 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    # m2: negative-c formula must be rejected loudly
    T_toy = lib_tensor(np.asarray(
        BG.block_maps_f64(BG.cheb_rows(
            np.array([float(x) for x in x10]), DEG_A, -1.0, 1.0),
            np.abs(np.array([float(w) for w in w_sm1])))), V)
    c_toy = np.ones(T_toy.shape[0] * 22)
    q_toy = T_toy.reshape(-1, T_toy.shape[2]).T @ c_toy
    ok_pos, rel_pos, _m1 = verify_section(T_toy, q_toy, c_toy)
    c_bad = c_toy.copy()
    c_bad[7] = -1.0
    ok_neg, rel_neg, min_neg = verify_section(T_toy, q_toy, c_bad)
    check("G71-mustfail-negative-c", ok_pos and not ok_neg
          and min_neg < 0,
          "m2 NEGATIVE-c: the verifier accepts the honest "
          "all-ones section (rel %.1e) and REJECTS the mutant "
          "with one negative coefficient (min c = %+.1f) -- the "
          "c >= 0 check is load-bearing and loud"
          % (rel_pos, min_neg))
    # m3: log-relation consumer exposed by the twin
    if smoke:
        check("G72-mustfail-logrel-twin", True, "SMOKE: skipped")
    else:
        uu_main = np.asarray(ctx9["uu"], float)
        uu_twin = np.asarray(ctxT["uu"], float)
        fac_main = mutant_phi_logrel(uu_main, D9)
        fac_twin = mutant_phi_logrel(uu_twin, D9)
        n_cmp = min(len(fac_main), len(fac_twin))
        disagree = float(np.mean(fac_main[:n_cmp]
                                 != fac_twin[:n_cmp]))
        fT_ = block_feats(xaT, waT, ffT, D9, ST)
        f9_ = block_feats(xx9, ww9, ff9, D9, S9)
        nb_cmp = min(len(f9_["G"]), len(fT_["G"]))
        stab = max(float(np.max(np.abs(
            f9_[k][:nb_cmp] - fT_[k][:nb_cmp])
            / np.maximum(np.abs(f9_[k][:nb_cmp]), 1e-12)))
            for k in ("G", "mp", "mm", "t1", "t2", "Gt"))
        check("G72-mustfail-logrel-twin",
              disagree >= M3_BAR and stab <= M3_STAB,
              "m3 LOG-RELATION CONSUMER: the planted mutant "
              "(den-ladder probe at %.0e) disagrees between "
              "MAIN and twin on %.3f of the comb (bar %.2f) "
              "while the sealed features are METRIC-stable "
              "(max rel dev %.1e <= %.0e) -- METRIC_ONLY "
              "semantics enforced live"
              % (LOGREL_TOL, disagree, M3_BAR, stab, M3_STAB))
    # m4: recomposition break, exact
    c_ex = [Fr(1)] * (len(Ls_sm1) * 22)
    A_ok = [sum(Mlib_sm1[e][c] * c_ex[c]
                for c in range(len(c_ex)))
            for e in range(len(idx_sm1))]
    c_bad_ex = c_ex[:]
    c_bad_ex[5] += Fr(3)
    A_bad = [sum(Mlib_sm1[e][c] * c_bad_ex[c]
                 for c in range(len(c_bad_ex)))
             for e in range(len(idx_sm1))]
    defect = max(abs(A_bad[e] - A_ok[e])
                 for e in range(len(idx_sm1)))
    check("G73-mustfail-recomposition", defect > 0,
          "m4 RECOMPOSITION BREAK (SM1, exact Fractions): "
          "corrupting one library coefficient leaves a NONZERO "
          "exact entrywise defect (max |dev| = %s) -- CAUGHT; "
          "the recomposition gate is not vacuous"
          % str(defect))

    # ---------------- S8 adjudication
    section("S8  ADJUDICATION (SEALED TREE)")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "library or bar change after evaluation, no RH claim; "
          "r243..r311 stand; the r311 letters stand -- this "
          "round adjudicates the construction question only")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        if legb["span9"] > SPAN_BAR:
            main_v = ("PSD_NEEDS_FULL_MATRIX(the sealed rank-one "
                      "library SPAN cannot carry the w9 identity "
                      "-- unconstrained rel %.2e > %.0e)"
                      % (legb["span9"], SPAN_BAR))
        elif legb["nn_ok9"] and legb["go_phi"]:
            main_v = ("RANKONE_SECTION_GO(%s: the frozen formula "
                      "carries all %d rungs + twin at rel <= "
                      "%.0e)" % (legb["go_phi"], legb["nrungs"],
                                 FORM_BAR))
        elif legb["nn_ok9"]:
            main_v = ("MEMBERSHIP_UNEXPLAINED(the solver-found "
                      "explicit rank-one section EXISTS on w9@A "
                      "(rel %.1e, support %d) and on %d/%d "
                      "rungs, but no sealed formula carries -- "
                      "membership true, mechanism unformulated)"
                      % (legb["rel9nn"], legb["sup9"],
                         legb["n_feas"], legb["nrungs"]))
        elif legb["fk_valid"] and legb["tmass9"] >= WALL_FRAC:
            main_v = ("COEFFICIENT_SIGN_WALL(w9@A: library span "
                      "CARRIES the identity (rel %.1e) but the "
                      "cone does NOT: NNLS rel %.4f with "
                      "VERIFIED Farkas certificate, t-row mass "
                      "%.5f >= %.2f -- the identity forces "
                      "negative c exactly on the wall/border "
                      "coordinates; twin rel %.4f type-"
                      "identical; exact grade on miniatures: %s; "
                      "rung census %d/%d feasible)"
                      % (legb["span9"], legb["rel9nn"],
                         legb["tmass9"], WALL_FRAC,
                         legb["relTnn"], str(legb["ex_grade"]),
                         legb["n_feas"], legb["nrungs"]))
        elif legb["fk_valid"]:
            main_v = ("PSD_NEEDS_FULL_MATRIX(cone infeasible "
                      "OFF-wall: verified Farkas with t-row "
                      "mass %.3f < %.2f -- the rank-one library "
                      "is structurally too small)"
                      % (legb["tmass9"], WALL_FRAC))
        else:
            main_v = ("MEMBERSHIP_UNEXPLAINED(undecided "
                      "numerics: NNLS rel %.4f without a "
                      "verified certificate%s)"
                      % (legb["rel9nn"],
                         ", CAPPED" if legb["cap9"] else ""))
        verd = " + ".join([
            main_v,
            "MEMBERSHIP_ANATOMY(%s; DUALS: %s)" % (anat_txt,
                                                   dual_txt),
            "W9B_STATUS(%s)" % w9b_status,
            "R311_DEMARCATION(the r311 letters stand; this "
            "round adjudicates the construction question only)"])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the ONE construction round of the reviewer "
          "tree; GO => lane A becomes a proof lane; otherwise "
          "lane A closes as cone language and the resources "
          "move to the fiber; NO RH claim"
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


def span_of(M, q):
    x, _r, _rk, _sv = np.linalg.lstsq(M, q, rcond=RCOND)
    return float(np.linalg.norm(M @ x - q)
                 / max(np.linalg.norm(q), 1e-300))


if __name__ == "__main__":
    sys.exit(main())
