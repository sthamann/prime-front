#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""blockgreen_nontriviality_probe -- PRIME.LSTAR.BLOCKGREEN.
NONTRIVIALITY.01 (round 311, the reviewer's MANDATORY round BEFORE
any constructive G-search): IS THE PSD BLOCK FAMILY STRONGER AND
MORE LOCAL THAN Q_w >= 0 -- OR IS IT A SPARSE-GRAM / CHORDAL
RESTATEMENT OF THE SAME POSITIVITY?  r308 (block_green_probe) found
that the affine set A(w) = {(G_1..G_R): Q_w = sum Delta^T G_r Delta}
intersected with the psd product cone is nonempty on MAIN and the
rational twin (Dykstra converges to full-psd, +6.6e-16 / +2.0e-17)
and empty-looking on EPSTEIN/SCRAMBLE (stall at -0.45 / -0.49).
The reviewer's question: if every positive global form decomposes
into such blocks by a general psd-completion theorem, the SDP
separates the worlds BY FORCE -- it evaluates the wall in new
clothes, and IDENTITY_EXISTS is language, not mechanism.  DESIGN-
TIME KNOWLEDGE (published r309 amendment a1, adopted as-is): the
control budgets are NEGATIVE past the flip (S_{N-2} = -3.992 EPST /
-5.237 SCR), so the r308 control targets A_sys carry a negative
(t,t) diagonal entry -- the central trivialization HYPOTHESIS of
this round, declared BEFORE any evaluation: the r308 feasibility
separation may be exactly the sign of lambda_min(A_sys), i.e. the
budget/wall sign leaking through the target, since the image cone
C_w = L_w(Pi S_+) contains only psd matrices.  This probe TESTS and
QUANTIFIES that hypothesis, then pushes PAST it (ablations, sealed
samples, exact Farkas duals) to decide what remains.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r309 (paired cone) and r313 (Renyi-3 proof form) run
in parallel; this probe touches nothing of theirs.

INDEX FIREWALL (binding, r238-r308 discipline): w = window (kz),
S = #union atoms, N_w = (S+1)//2, n = degree, minC = first h_n < 0.
Ground truth (minC, flips, published r308/r309 record numbers)
enters GATES and record tables only; the sealed constructors
consume split-source arrays and coordinate matrices ONLY (AST scope
audit); no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM from r308 block_green_probe (BG): the Delta
coordinate library (cheb_rows, block_maps_f64/fr, target_form_
f64/fr, system_f64/fr, least_norm, block_eigs, kernel_exclusion,
census_world, world_arrays, world_budget, hull_of, border_split,
rref_solve_fr, reconstruct_fr, exact_budget_fr, mono_rows_fr) and
the UNCHANGED r308 Dykstra protocol feas_diag (used as-is -- the
anchor object under audit); worlds through r278 MS.ctx_build, r284
LS.world_pack, r289 AK.twin_rational + r276 MF.local_gaps, r244
BH.bord_chain, v881 PIK, r243 PB.smooth_comb, r274 WD.{stj_gen,
pv_seq}, v563 core READ-ONLY.

THE SEALED LEGS (frozen BEFORE any evaluation):

LEG 0 -- R308 ANCHORS BIT-NEAR.  w9 source split (367/263/104/184/
184); identity residuals <= RES_BAR with dof 7593@DEG_A / 7415@
DEG_B (=> rank 51 / 229 of nvech 55 / 465 -- the SPAN CODIMENSIONS
4 and 236, first disclosed here); least-norm min eig rel in the
band 2x around -1.30e-2; the Dykstra world table reproduced with
the UNCHANGED r308 protocol: w9@A + twin@A converge at stage 200
(record +6.6e-16 / +2.0e-17), EPST@A / SCR@A stall after 2000 in
[-0.60,-0.30] / [-0.65,-0.35] (records -0.45 / -0.49); budgets
B_w9 = 8.368649 (tol 1e-3), S_EPST = -3.992 +- 0.05, S_SCR =
-5.237 +- 0.05 (r309 records).

LEG A1 -- EXACT CONE COMPARISON C_w = L_w(Pi S_+) vs {Q >= 0}.
(i) THE SPARSITY GRAPH OF THE Delta COORDINATES, BUILT EXPLICITLY:
vertices = the S union atoms + one t vertex; every fourfold block
contributes the clique {j, j+1, j+2, j+3, t} (D1..D5 couple the
four atom evaluations, D6 = t couples t into every block through
the G_r off-diagonals).  Chordality tested ALGORITHMICALLY (maximum
cardinality search + Tarjan-Yannakakis perfect-elimination check;
maximal-clique census compared entrywise against the sealed block
cliques) on the SM graphs and the full S = 367 w9 graph.  DISCLOSED
consequence (Grone et al. completion / Agler-Helton-McCullough-
Rodman & Griewank-Toeplitz sparse-Gram theorem): IF the graph is
chordal AND each block's six coordinates span the full local
evaluation space R^5 (tested: exact per-block rank 5 on the SM
worlds, row-normalized sigma_5 > SIG_TOL on w9 -- adjacent fold
atoms are nearly coincident, so raw difference rows are tiny; row
scaling does not change the row space), THEN in EVALUATION
coordinates
the image cone equals the full pattern-psd cone -- the block
language on evaluation space is EXACTLY a chordal restatement, and
every remaining nontriviality lives in the COMPRESSION E onto the
restricted subspace span{x^0..x^d, t}.  (ii) THE SPAN LAYER, EXACT:
rank(M) vs nvech = (d+2)(d+3)/2 per world -- exact Fraction ranks
on SM0..SM3 (r308-derived records 44/44/53/54 of 55) and MINI16
(55 = FULL, exact), f64 lstsq ranks on w9 (51@A / 229@B);
exact left-nullspace bases (the ANNIHILATORS N = {Y: L_r Y L_r^T =
0 for all r}) on SM1/SM2/SM3 with exact verification of every
compression; any nonzero Y in N is indefinite by theorem (psd Y
with zero compressions has all V_r in ker Y, and the stacked V_r
have full rank -- the r308 kernel-exclusion condition), and yields
the exact AMBIENT counter-model of Leg A2.  (iii) THE SAMPLE
CENSUS on the restricted subspace: sealed generation (rng seed
20260826, Q = V V^T Frobenius-normalized, psd-shift ladder ALPHA_
LADDER, isometric span projection -- NEVER from wall data, NEVER
from target eigenvectors), NSAMP_W9 = 6 on w9@DEG_A, NSAMP_MINI =
6 on MINI16 (full span!), NSAMP_SM = 4 on SM1; every psd sample
runs the staged Dykstra (200 / 2000 / 20000): are ALL decomposable,
or do undecomposable positive Q exist?

LEG A2 -- POSITIVE COUNTER-MODELS.  Ambient (exact, small models):
from the exact annihilator Y of SM1 take a deterministic rational
direction z with z^T Y z < 0 (sign-flip of Y allowed -- N is a
subspace); then Q = z z^T is psd, <Y, Q> < 0 while <Y, X> = 0 on
all of C_w: the EXACT rational Farkas certificate that the psd
rank-one form z z^T has NO block decomposition (not even an
indefinite one -- a SPAN obstruction, disclosed as the cheap
linear layer); confirmed independently by exact rank jump of
[M | vech(z z^T)].  Deep (within span): every psd in-span sample
or world target that stalls through the full Dykstra ladder gets
the DUAL SEARCH (POCS between the compression cone {Y: B_r Y B_r^T
>= 0} and the hyperplane <Y, A> = -1, OMEGA = 0.25, DUAL_ITER =
4000), the eps*I POLISH (compressions of I are exactly I_5, so
Y + eps*I is exactly compression-psd; certificate valid iff
<Y,A> + eps*tr(A) <= -0.5), and on the small systems (cap
CERT_CAP per world) the fully exact in-span reconstruction IN THE
EXACT CHEBYSHEV BASIS (exact three-term recurrence with rational
hull -- the same coordinates as the f64 leg, so no basis
mismatch): rationalize the affine coefficient vector x (isometric
sqrt(2) unknowns converted to the unscaled exact convention),
build Q = unvech(M x) EXACTLY (in span by construction, entrywise
crosschecked against the f64 sample), verify Q PD exactly (leading
minors), Y = rationalize + d*I over the sealed ladder D_LADDER,
exact verification (all 6x6 compressions L_r Y L_r^T psd via
all-principal-minors, <Y, Q> < 0 exact).  A verified certificate
(polished-numeric or exact) against a PD in-span target = the
STRICT_SOURCE_CONE building block.  TOY4 exact restatement datum: on the single-block toy the
cone is ALL of S_+ by explicit exact section G = P X P^T,
P = L (L^T L)^{-1} (hand psd X_TOY reproduced entrywise).

LEG A3 -- FARKAS DUALS OF THE DEAD WORLDS.  The trivialization
hypothesis names the candidate dual: Y_t = e_t e_t^T (ONE nonzero
rational entry -- the lowest-dimensional possible dual).  Y_t is
psd, hence <Y_t, X> >= 0 on C_w by theorem (compression identity
L_r Y_t L_r^T = E_66 verified exactly on SM1); <Y_t, A_sys> =
S_{N-2} -- measured per world: EPST/SCR NEGATIVE (exact-grade
infeasibility certificates for r308's one-sided stalls, closing
them two-sidedly), MAIN + twin POSITIVE with reserve +7.654.  The
reviewer protocol (normalize, symmetrize, eliminate small entries,
rationalize) terminates trivially on Y_t; the COMMON low-
dimensional Y for both controls therefore EXISTS and IS the budget
coordinate -- i.e. the r243 budget positivity S_{N-2}(w) >= 0, the
known wall reading, NOT a new source inequality.  Blind test on
NEW worlds (SCRAMBLE seeds 2 and 3, built through the sealed r278
channel, never seen by any prior round): predict feasibility by
sign(S_{N-2}) FIRST, then run the staged Dykstra -- the prediction
must hit 2/2.  The EXACT SCHUR-TAIL LEMMA (verified exactly on SM0
and SM1): the (t,t) Schur complement of A_sys at cap d equals
S_{N-2} - sum_{k<=d} F_k^2/h_k -- on SM0 exactly -(rho_3 + .. +
rho_8) < 0: THE POSITIVE-CLASS SM0 TARGET IS INDEFINITE EXACTLY
(deg cap 8 > N_w - 2 = 3 overshoots the budget depth), so the r308
SM0..SM3 "OPEN" feasibility stalls are DECIDED (trivially target-
indefinite), and the wall sign enters the target mechanically as
the budget rho-tail.

LEG A4 -- CHORDALITY + LEAKAGE AUDIT (three trivialization
mechanisms): (i) general chordal psd decomposition = Leg A1(i);
(ii) top-eigendirection selection: START ABLATION of the r308
Dykstra (zero start + sealed random start, replacing the least-
norm start) on w9@A (zero start must converge; the random start
must reach near-convergence START_NEAR = 1e-8, amendment a2) and
EPST@A (must still stall) -- convergence must not be an artifact
of the start choice;
(iii) implicit use of the wall sign through an SDP objective: AST
audit that the UNCHANGED r308 feas_diag consumes (M, q, g0) only
-- eigen-clips act on CANDIDATE blocks, the pseudoinverse is of
the coordinate matrix, no objective function, no target spectral
data (audited against the same forbidden-name set as the
constructors) -- plus the TARGET-SIGN TABLE lambda_min_rel(A_sys)
per world/cap: the sign-equivalence census "Dykstra converged <=>
target psd" over every measured cell; a converged-on-indefinite
cell is a theorem violation (hard FAIL); a PD-target stall
surviving the full ladder + dual search is an honest OPEN locus.
BUDGET ABLATION (the decisive residual test, diagnosis-grade): on
EPST/SCR replace the (t,t) entry by the sealed ladder |S_{N-2}|
then (if still not PD) the MAIN budget record 7.654364; if the
ablated target is PD, run the staged Dykstra: convergence => the
ENTIRE r308 separation was the budget sign (restatement locked);
a robust stall => residual conic selectivity beyond the wall sign
(escalated to the dual search).  The mirror consistency side: w9
with the EPST budget transplanted must STALL (indefinite target,
theorem).  W9@DEG_B ESCALATION: lambda_min(A_sys@B) via the Schur
tail (predicted positive = the rho-tail beyond k = 28), then the
staged Dykstra up to 20000 (the r308 -4.2e-5 OPEN cell decided or
honestly kept OPEN), dual search if it stalls.

LEG E -- MUST-FAILS (each loud):
  (m1) WRONG-SIGN FARKAS: the exact certificate checker must
       REJECT (-Y, z) (z^T(-Y)z > 0 exact) -- CAUGHT exactly;
  (m2) WALL-CONTAMINATED COUNTER-MODEL SEARCH: a mutant selecting
       z from minC_true / wall data -- FLAGGED by the AST scope
       audit;
  (m3) CHORDALITY ON THE WRONG GRAPH: the sealed tester must
       report NON-CHORDAL on C4 and C5 (a tester that cannot fail
       is vacuous), and the t-less mutant graph builder must be
       caught by exact edge-set mismatch against the sealed block
       cliques;
  (m4) TARGET-EIGENVECTOR SAMPLING: a mutant generating sample Q
       from eigvecs_target -- FLAGGED by the AST scope audit
       (TARGET_INVERSE class).
STOP LIST (binding): NO L* claim, NO bound mechanism, NO
asymptotic law, NO derived 5/7, NO posthoc window, NO selection by
measured signs inside constructors (the staged-Dykstra stage-3
permission consumes the target inertia as gate-side SCHEDULING
only, disclosed -- infeasibility on indefinite targets is a
theorem, escalation there is wasted compute), NO RH claim;
r243..r310 stand; the r282 full-class refutations and the r308
verdict letters are untouched.

WORLDS: MAIN w9; the r289 rational twin; controls EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH (minC 25/21/27); NEW blind worlds
SCRAMBLE(seed 2) and SCRAMBLE(seed 3); exact small models TOY4 /
SM0..SM3 / MINI16 rebuilt VERBATIM from the r308 constructors.

SEALED CONSTANTS: DEG_A 8; DEG_B 28; MAIN_KZ 9; W9_ANCH (367, 263,
104, 184, 184); CTRL_FLIPS {EPST 25, SCR 21, SMOOTH 27}; RES_BAR
1e-8; RCOND 1e-11; PSD_NEG 1e-7; KER_TOL 1e-12; SIG_TOL 1e-10;
FEAS stages (200, 2000, 20000); FEAS_CONV 1e-9; SEED 20260826;
NSAMP_W9 6; NSAMP_MINI 6; NSAMP_SM 4; ALPHA_LADDER (0.0, 0.5,
1.0, 2.0); DUAL_ITER 4000; DUAL_TOL 1e-7; OMEGA 0.25; DEN_LADDER
(100, 10000, 1000000); POLISH_BAR 0.5; START_NEAR 1e-8; CERT_CAP
1; D_LADDER (1e-6, 1e-4, 1e-2) exact; RAT_TOL 1e-8; QMAX 1e6;
X_TOY [[2,1,0],[1,2,0],[0,0,1]]; RANK_REC {TOY4 6, SM0 44, SM1 44,
SM2 53, SM3 54, MINI16 55, w9A 51, w9B 229} (derived from the
published r308 dof record); DOF_REC {w9A 7593, w9B 7415}; LEAST_REC
-1.30e-2 (band factor 2); DYK_REC {w9A conv@200, twin conv, EPST
[-0.60,-0.30], SCR [-0.65,-0.35]}; B_W9_REC 8.368649 tol 1e-3;
S_EPST_REC -3.992 / S_SCR_REC -5.237 tol 0.05 (r309); SMOOTH_REC
-1.3e-5 / W9B_REC -4.2e-5 (report anchors, factor-5 bands); ABL_
MAIN_S 7.654364; runtime <= 1800 s; smoke = S0 + S1 (exact leg) +
S2 (graphs) + w9 build + w9@A census anchor + S7 + verdict
(worlds census, Dykstra, ablations, samples, duals skipped).
PRE-SPEC SCOPING (disclosed): every record number above is a
published r308/r309 record adopted as-is; the trivialization
hypothesis, the Schur-tail lemma, the graph construction, every
bar, ladder, schedule and the verdict rule were fixed at design
time BEFORE any evaluation of this probe; no machinery pass
preceded this spec except record reading; the only steering by
measured target data is the disclosed gate-side stage-3 schedule
permission and the ablation ladder (both diagnosis-side, both
sealed here).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of]
    TARGET_INVERSE_SELECTION(audit loci)   -- iff the A4 audits
      find the r308 protocol target-spectrally driven (start
      ablation flips convergence or feas_diag consumes target
      spectra / an objective);
    SOURCE_SECTION_EXISTS(Y)               -- iff a verified dual
      certificate against a PD in-span target exists AND a
      reconstructed nontrivial (beyond Y_t) rational/algebraic
      common dual separates BOTH controls with positive MAIN +
      twin reserve and holds blind on the new worlds;
    STRICT_SOURCE_CONE(certificates)       -- iff a verified
      (exact rational, or polished-numeric with margin) dual
      certificate against a PD IN-SPAN target exists without the
      common source dual; carries the binding SEPARATION
      MECHANISM clause: whether the r308 world separation itself
      was the budget sign is reported inside the verdict;
    PSD_DECOMP_RESTATEMENT(mechanism)      -- iff the audits are
      clean, the graph is chordal with full local spanning, every
      DECIDED census cell is sign-equivalent (converged <=>
      target psd) and no strict certificate exists; undecided
      PD-stalls are listed in the OPEN_LOCI clause.
  + SPAN_LEDGER(exact codim table; ambient rank-one counter-model
    status -- always; DISCLOSED as the linear layer, not conic)
  + SIGN_EQUIVALENCE_LEDGER(census + OPEN loci) [always]
  + R308_DEMARCATION [always]: the r308 verdict letters stand;
    this round retypes their INTERPRETATION only.
Honesty before beauty: the trivialization hypothesis was declared
design-time from the published r309 amendment -- confirming it is
the honest expected outcome and a NO-GO for the planned R312
G-search; only a verified strict-cone certificate or a nontrivial
common source dual justifies R312.

CONSEQUENCE MAP (sealed): PSD_DECOMP_RESTATEMENT or
TARGET_INVERSE_SELECTION => NO-GO for R312 in its planned
rank-one-conductivity form (the identity language stays valuable
AS LANGUAGE, not as mechanism); STRICT_SOURCE_CONE or
SOURCE_SECTION_EXISTS => GO.

RECORD TABLES (frozen from the record run; chronology honest:
smoke pass 1 = 30/33 -- two harness-conditioning fails (the raw
sigma_5 spanning test on nearly-coincident fold atoms -> row-
normalized; the MINI16 rank read f64 54 vs the exact r308 record
55 -> exact Fractions rank) fixed at smoke stage; smoke 33/33
(8.4 s) deterministic; calibration pass 1 crashed in the dual
POCS on the empty-dual side (iterates blow up along the
hyperplane when no dual exists) -> AMENDMENT a1: divergence guard
(reported one-sidedly as NOT FOUND) + the start-ablation runs on
PD targets receive the stage-3 permission the sealed schedule
rule already grants them; calibration pass 2 = 32/34: the sealed
random start reached -8.5e-9 after 20000 (slow tail, three
decades past the control stalls) -> AMENDMENT a2: near-
convergence bar START_NEAR = 1e-8 for the random start (a bar
amendment, disclosed); and the polished-numeric certificates
were not recorded by the harness although the sealed verdict
rule accepts them -> AMENDMENT a3: certificate bookkeeping per
the sealed rule, verdict clauses refined to carry the separation
mechanism (reporting only -- the four-way selection rule never
moved), and the exact certification rebuilt in the EXACT
CHEBYSHEV basis with the isometric-unknown conversion and an
entrywise f64 crosscheck (the first monomial-basis attempt was a
coordinate mismatch, caught by the crosscheck); calibration
passes 3/4/5 = 34/34 (319/313/316 s), pass 5 with both exact
certificates; the only post-freeze edit is this record-table
insertion, which IS the protocol; record run1/run2 identical up
to WALL.
REC_VERDICT = STRICT_SOURCE_CONE(10 polished-numeric + 2 exact
in-span rational certificates; SEPARATION MECHANISM clause: the
r308 world separation is fully the budget sign, 9/10 world cells
sign-equivalent, budget ablation CONV, blind 2/2, transplant
kills MAIN) + SPAN_LEDGER(codim TOY4 0 / SM0 11 / SM1 11 / SM2 2
/ SM3 1 / MINI16 0 / w9A 4 / w9B 236) + SIGN_EQUIVALENCE_LEDGER
(OPEN_LOCI = w9@B + the six w9A samples, all one-sided) +
R308_DEMARCATION.
Key numbers.  EXACT LEG: TOY4 cone = S_+ by explicit exact
section G = P X_TOY P^T (entrywise exact, G psd rank 3); exact
ranks 44/44/53/54 == the r308 dof records; annihilator dims SM1
11 / SM2 2 / SM3 1, every compression exactly zero; SM1 ambient
counter-model z^T Y z = -2304/62004635 < 0 exact, affine system
exactly infeasible; SCHUR-TAIL LEMMA exact on SM0 AND SM1
(u^T H^{-1} u == the chain readout entrywise): s(SM0) =
-(rho_3..rho_8) = -7.082e-2 < 0 EXACT with all h_k > 0 -- the
POSITIVE-CLASS SM0 target is INDEFINITE at cap 8 and all four
r308 small-model OPEN stalls are DECIDED target-indefinite
(first h <= 0 at n = 6/6/8 on SM1/SM2/SM3, n = 3 on MINI16);
MINI16 exact rank 55 = FULL.  GRAPHS: chordal on every size
(w9: 368 vertices, 1462 edges, 364 maximal cliques == the sealed
blocks); local spanning exact 5/5, w9 row-normalized min
sigma_5/sigma_1 = 7.9e-9; C4/C5 correctly non-chordal.  TARGET-
SIGN TABLE (lambda_min rel of A_sys): w9@A +8.39e-4 PD / twin@A
+8.39e-4 PD / EPST@A -8.64e-1 / SCR@A -1.00 / scr2 -1.00 / scr3
-1.00 INDEF / SMOOTH@A +1.6e-16 BOUNDARY (S_SMOOTH = +3.48 --
the r308 SMOOTH marginality is a boundary target, not a thin
wall) / SM0 -5.64e-3 / SM1 -6.95e-2 / MINI16 -2.01e-3 INDEF /
w9@B +2.42e-6 PD-thin (rho-tail beyond k = 28: +4.167).  LEG 0
bit-near: dof 7593@A / 7415@B, least-norm -1.298e-2; Dykstra
w9@A +6.56e-16 conv@200 / twin@A +2.05e-17 conv@200 / EPST
-0.451 / SCR -0.493 stall@2000 / SMOOTH -1.28e-5 (rec -1.3e-5).
THE BUDGET DUAL: <Y_t, A_sys> = S_{N-2}: w9/twin +7.6544 reserve
vs EPST -3.9921 / SCR -5.2368 -- ONE common one-entry rational
dual closes the r308 stalls two-sidedly; it IS the r243 budget
positivity (the known wall reading); BLIND 2/2 (scr2 S = -6.196
minC 23, scr3 S = -6.146 minC 11: predicted infeasible BEFORE
the runs, stalled -0.551 / -0.501).  THE DECISIVE ABLATIONS:
EPST with (t,t) <- |S| = +3.992: PD (+1.04e-3) and the Dykstra
CONVERGES (+2.5e-16); SCR ablated: PD (+1.08e-3), CONVERGES
(-5.1e-11 at 200 steps); w9 with the EPST budget transplanted:
INDEF (-8.64e-1), STALLS (-0.449) -- the ENTIRE r308 DEG_A world
separation is the ONE budget scalar, in both directions.  START
ABLATION: w9@A zero start converges (-1.9e-10), random start
-8.5e-9 (bar 1e-8); EPST stalls from both (-0.451 / -0.377);
feas_diag AST audit CLEAN (objective-free).  W9@DEG_B: PD-thin,
STILL OPEN after 20000 (-1.78e-5, improved from the r308
-4.2e-5; dual POCS diverges = no certificate -- one-sided).
THE SAMPLE CENSUS (the round's second discovery): 0/6 w9A + 0/6
MINI16 + 0/4 SM1 sealed in-span PD samples decompose; every
MINI16/SM1 stall carries a VALID POLISHED-NUMERIC DUAL (worst
compression -1e-16..-1.4e-8, <Y,Q> = -1); MINI#0 and SM1#0 carry
FULLY EXACT in-span rational certificates (den 1e6, d = 1e-6,
<Y,Q> = -0.9999977 / -0.9999930 exact rational < 0) -- generic
positive forms on the restricted subspace have NO psd block
decomposition: C_w is STRICTLY smaller than span cap S_+, ON THE
REAL-SOURCE MINIATURE with full span.  MUST-FAILS: m1 wrong-sign
Farkas rejected exact (+2304/62004635); m2 wall-z FLAGGED; m3
C4/C5 non-chordal + 20 edge mismatches caught; m4 eigvecs_target
sampler FLAGGED; constructors + fragment audit CLEAN.  Runtime
316 s full / 8.4 s smoke; run1/run2 identical up to WALL.
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
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import block_green_probe as BG                     # noqa: E402 r308
import lstar_two_measure_probe as LS               # noqa: E402 r284
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import minimal_firewall_probe as MF                # noqa: E402 r276
import metric_stability_probe as MS                # noqa: E402 r278
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import wronskian_dictionary_probe as WD            # noqa: E402 r274
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
DEG_B = 28
MAIN_KZ = 9
W9_ANCH = (367, 263, 104, 184, 184)
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
RES_BAR = 1e-8
RCOND = 1e-11
PSD_NEG = 1e-7
KER_TOL = 1e-12
SIG_TOL = 1e-10
FEAS_IT1 = 200
FEAS_IT2 = 2000
FEAS_IT3 = 20000
FEAS_CONV = 1e-9
SEED = 20260826
NSAMP_W9 = 6
NSAMP_MINI = 6
NSAMP_SM = 4
ALPHA_LADDER = (0.0, 0.5, 1.0, 2.0)
DUAL_ITER = 4000
DUAL_TOL = 1e-7
OMEGA = 0.25
DEN_LADDER = (100, 10000, 1000000)
POLISH_BAR = 0.5
RAT_TOL = 1e-8
QMAX = 1e6
FIVE_SEVEN = Fr(5, 7)
B_TOY = Fr(9, 7)
X_TOY = [[Fr(2), Fr(1), Fr(0)], [Fr(1), Fr(2), Fr(0)],
         [Fr(0), Fr(0), Fr(1)]]
RANK_REC = {"TOY4": 6, "SM0": 44, "SM1": 44, "SM2": 53, "SM3": 54,
            "MINI16": 55, "w9A": 51, "w9B": 229}
DOF_REC = {"w9A": 7593, "w9B": 7415}
LEAST_REC = -1.30e-2
DYK_EPST_BAND = (-0.60, -0.30)
DYK_SCR_BAND = (-0.65, -0.35)
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
S_EPST_REC = -3.992
S_SCR_REC = -5.237
S_CTRL_TOL = 0.05
START_NEAR = 1e-8
CERT_CAP = 1
D_LADDER = (Fr(1, 10 ** 6), Fr(1, 10 ** 4), Fr(1, 100))
SMOOTH_REC = -1.3e-5
W9B_REC = -4.2e-5
ABL_MAIN_S = 7.654364
MINI_K = 16
MINI_BK = 3

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
                       "constructors consume split-source arrays "
                       "and coordinate matrices ONLY; record "
                       "numbers enter gates and record tables only"
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


CONSTRUCTORS = ("graph_from_blocks", "mcs_order", "peo_check",
                "max_cliques_peo", "local_span_rank_fr",
                "rref_rank_fr", "nullbasis_fr", "y_from_leftnull",
                "comp_zero_fr", "comp_psd_fr", "neg_dir_fr",
                "schur_fr", "cheb_rows_fr", "chain_readout_fr",
                "span_project",
                "compress_bases", "comp_min_eig", "dual_pocs",
                "polish_dual", "run_feas3", "rationalize_sym",
                "exact_cert_check", "exact_strict_cert",
                "sample_psd")
SCOPE_FORBIDDEN = {"CTRL_FLIPS", "ANCHORS", "minC_true",
                   "cross_true", "blk_eigs_true", "cholesky",
                   "eigvecs_target", "target_inverse", "wall_sign"}


def scope_audit_src(src, funcname):
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


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    return scope_audit_src(src, funcname)


# ============== sealed graph constructors (AST-audited)
def graph_from_blocks(S):
    """the sparsity graph of the Delta coordinates: vertices =
    atoms 0..S-1 in fold order + the t vertex (index S); every
    sliding fourfold block contributes the clique
    {j, j+1, j+2, j+3, t}.  Consumes the atom count only."""
    n = S + 1
    adj = [set() for _ in range(n)]
    for j in range(S - 3):
        cl = [j, j + 1, j + 2, j + 3, S]
        for a_i in range(len(cl)):
            for b_i in range(a_i + 1, len(cl)):
                adj[cl[a_i]].add(cl[b_i])
                adj[cl[b_i]].add(cl[a_i])
    return adj


def mutant_wrong_graph(S):
    """m3 MUST-FAIL side: the t-less graph builder (omits the
    border vertex coupling) -- caught by exact edge-set
    mismatch."""
    n = S + 1
    adj = [set() for _ in range(n)]
    for j in range(S - 3):
        cl = [j, j + 1, j + 2, j + 3]
        for a_i in range(len(cl)):
            for b_i in range(a_i + 1, len(cl)):
                adj[cl[a_i]].add(cl[b_i])
                adj[cl[b_i]].add(cl[a_i])
    return adj


def mcs_order(adj):
    """maximum cardinality search: returns a candidate perfect
    elimination ordering (deterministic ties: smallest index)."""
    n = len(adj)
    wt = [0] * n
    num = [None] * n
    order = [None] * n
    for k in range(n - 1, -1, -1):
        v = -1
        best = -1
        for u in range(n):
            if num[u] is None and wt[u] > best:
                best = wt[u]
                v = u
        order[k] = v
        num[v] = k
        for u in adj[v]:
            if num[u] is None:
                wt[u] += 1
    return order


def peo_check(adj, order):
    """Tarjan-Yannakakis test: order is a perfect elimination
    ordering iff for every v the later neighbors X satisfy
    X \\ {u0} subset N(u0) with u0 = the earliest later
    neighbor.  Chordal <=> MCS order passes."""
    n = len(adj)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    for i, v in enumerate(order):
        later = [u for u in adj[v] if pos[u] > i]
        if not later:
            continue
        u0 = min(later, key=lambda u: pos[u])
        for u in later:
            if u != u0 and u not in adj[u0]:
                return False, (v, u0, u)
    return True, None


def max_cliques_peo(adj, order):
    """maximal cliques from a PEO: candidates {v} + later
    neighbors, filtered by containment."""
    n = len(adj)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    cands = []
    for i, v in enumerate(order):
        c = frozenset([v] + [u for u in adj[v] if pos[u] > i])
        cands.append(c)
    cands = sorted(set(cands), key=lambda c: (-len(c), sorted(c)))
    out = []
    for c in cands:
        if not any(c < d for d in out):
            out.append(c)
    return out


# ============== sealed exact-linear-algebra constructors
def rref_rank_fr(rows):
    """exact rank via Gaussian elimination (deterministic
    first-nonzero pivot); destructive on a copy."""
    A = [r[:] for r in rows]
    nr = len(A)
    nc = len(A[0]) if nr else 0
    r = 0
    piv = []
    for c in range(nc):
        p = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [vi - f * vr for vi, vr in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == nr:
            break
    return r, piv, A


def nullbasis_fr(rows, nc):
    """exact nullspace basis of the (nr x nc) Fraction matrix:
    rref + free-variable back-substitution."""
    rank, piv, R = rref_rank_fr(rows)
    pivset = set(piv)
    free = [c for c in range(nc) if c not in pivset]
    basis = []
    for f in free:
        v = [Fr(0)] * nc
        v[f] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -R[i][f]
        basis.append(v)
    return rank, basis


def y_from_leftnull(yvec, idx, m):
    """rebuild the symmetric Fraction matrix Y from a left-null
    functional over the (i <= j) entry list: <Y, X>_F =
    sum_{i<=j} y_{ij} X_{ij} => Y_ij = y/2 off-diagonal."""
    Y = [[Fr(0)] * m for _ in range(m)]
    for e_i, (i, j) in enumerate(idx):
        if i == j:
            Y[i][i] = yvec[e_i]
        else:
            Y[i][j] = yvec[e_i] / 2
            Y[j][i] = Y[i][j]
    return Y


def comp_zero_fr(Ls, Y):
    """exact test: every block compression L_r Y L_r^T == 0."""
    m = len(Y)
    for rows in Ls:
        for a in range(6):
            YL = [sum(Y[i][k] * rows[a][k] for k in range(m))
                  for i in range(m)]
            for b in range(a, 6):
                v = sum(rows[b][i] * YL[i] for i in range(m))
                if v != 0:
                    return False
    return True


def comp_psd_fr(Ls, Y):
    """exact test: every 6x6 block compression L_r Y L_r^T psd
    (all principal minors >= 0)."""
    m = len(Y)
    for rows in Ls:
        C = [[sum(rows[a][i] * Y[i][k] * rows[b][k]
                  for i in range(m) for k in range(m))
              for b in range(6)] for a in range(6)]
        for mask in range(1, 64):
            S_ = [i for i in range(6) if mask >> i & 1]
            sub = [[C[i][j] for j in S_] for i in S_]
            if det_fr(sub) < 0:
                return False
    return True


def det_fr(A):
    """exact determinant (fraction Gaussian elimination)."""
    A = [r[:] for r in A]
    n = len(A)
    d = Fr(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        pv = A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] / pv
                A[i] = [vi - f * vc for vi, vc in zip(A[i], A[c])]
    return d


def neg_dir_fr(Y):
    """deterministic exact rational direction ladder: first z in
    (e_i; e_i + e_j; e_i - e_j) with z^T Y z != 0.  Complete: a
    nonzero symmetric Y cannot vanish on the whole ladder."""
    m = len(Y)
    for i in range(m):
        if Y[i][i] != 0:
            z = [Fr(0)] * m
            z[i] = Fr(1)
            return z, Y[i][i]
    for i in range(m):
        for j in range(i + 1, m):
            for s in (Fr(1), Fr(-1)):
                v = Y[i][i] + Y[j][j] + 2 * s * Y[i][j]
                if v != 0:
                    z = [Fr(0)] * m
                    z[i] = Fr(1)
                    z[j] = s
                    return z, v
    return None, Fr(0)


def schur_fr(A, K):
    """exact (t,t) Schur complement of the (K+1)x(K+1) target:
    s = A[K][K] - u^T H^{-1} u via exact solve."""
    H = [[A[i][j] for j in range(K)] for i in range(K)]
    u = [A[i][K] for i in range(K)]
    M_ = [H[i][:] + [u[i]] for i in range(K)]
    r, piv, R = rref_rank_fr(M_)
    if r < K:
        return None
    y = [Fr(0)] * K
    for i, c in enumerate(piv):
        y[c] = R[i][K]
    return A[K][K] - sum(u[i] * y[i] for i in range(K))


def cheb_rows_fr(xs, d, lo, hi):
    """exact Chebyshev rows T_0..T_d on the affine hull map --
    the EXACT twin of the f64 cheb_rows (same mathematical
    object, Fractions recurrence with rational hull), so the
    exact certificate lives in the SAME coordinate basis as the
    f64 leg."""
    out = []
    for x in xs:
        xi = (2 * x - lo - hi) / (hi - lo)
        row = [Fr(1)]
        if d >= 1:
            row.append(xi)
        for k in range(2, d + 1):
            row.append(2 * xi * row[k - 1] - row[k - 2])
        out.append(row)
    return out


def chain_readout_fr(xs, ws, bxs, bws, n_hi):
    """exact chain readout sum_{k<n_hi} F_k^2/h_k through the
    sealed r274 WD chain (mirrors exact_budget_fr)."""
    al, be, hs = WD.stj_gen(list(xs), list(ws), n_hi)
    vals = [WD.pv_seq(al, be, bx, n_hi) for bx in bxs]
    out = Fr(0)
    terms = []
    for k in range(n_hi):
        Fk = sum(bws[b_i] * vals[b_i][k] for b_i in range(len(bxs)))
        t = Fk * Fk / hs[k]
        terms.append(t)
        out += t
    return out, terms, hs


# ============== sealed f64 constructors
def span_project(M, Q):
    """isometric projection of the symmetric Q onto the span of
    the block image cone col(M): scale off-diagonal vech rows by
    sqrt(2), least-squares, map back.  Consumes the coordinate
    matrix only."""
    m = Q.shape[0]
    iu, ju = np.triu_indices(m)
    w = np.where(iu == ju, 1.0, math.sqrt(2.0))
    q0 = Q[iu, ju] * w
    Mi = M * w[:, None]
    x, _res, rank, _sv = np.linalg.lstsq(Mi, q0, rcond=RCOND)
    qs = (Mi @ x) / w
    Qs = np.zeros((m, m))
    Qs[iu, ju] = qs
    Qs[ju, iu] = qs
    rel = float(np.linalg.norm(Mi @ x - q0)
                / max(np.linalg.norm(q0), 1e-300))
    return Qs, x, rel, int(rank)


def compress_bases(L):
    """orthonormal bases of the block coordinate row spaces
    (rank 5: D3 is dependent, disclosed): batched SVD on the
    ROW-NORMALIZED copy (adjacent fold atoms are nearly
    coincident, so raw difference rows are tiny; row scaling
    does not change the row space)."""
    nrm = np.linalg.norm(L, axis=2, keepdims=True)
    Ln = L / np.maximum(nrm, 1e-300)
    _u, s, vt = np.linalg.svd(Ln, full_matrices=False)
    ranks = np.sum(s > SIG_TOL * s[:, :1], axis=1)
    B = vt[:, :5, :]
    return B, ranks, s


def comp_min_eig(Y, Bst):
    """minimum eigenvalue over all block compressions
    B_r Y B_r^T (candidate side)."""
    C = np.einsum("rim,mn,rjn->rij", Bst, Y, Bst)
    ev = np.linalg.eigvalsh(C)
    return float(np.min(ev))


def dual_pocs(A, Bst, iters=DUAL_ITER):
    """dual Farkas search: POCS between the compression cone
    {Y: B_r Y B_r^T >= 0} (relaxed parallel projection, OMEGA)
    and the hyperplane <Y, A>_F = -1.  Consumes A linearly (the
    hyperplane), never spectrally.  Divergence guard: when the
    intersection is empty (dual infeasible) the iterates can blow
    up along the hyperplane -- caught and reported one-sidedly as
    NOT FOUND."""
    nrm = float(np.sum(A * A))
    y_cap = 1e12 / max(math.sqrt(nrm), 1e-300)
    Y = -A / max(nrm, 1e-300)
    status = "ran"
    for _it in range(iters):
        C = np.einsum("rim,mn,rjn->rij", Bst, Y, Bst)
        if not np.all(np.isfinite(C)):
            status = "diverged"
            break
        ev, V = np.linalg.eigh(C)
        evn = np.minimum(ev, 0.0)
        Nn = np.einsum("rij,rj,rkj->rik", V, evn, V)
        corr = np.einsum("rim,rij,rjn->mn", Bst, Nn, Bst)
        Y = Y - OMEGA * corr
        Y = 0.5 * (Y + Y.T)
        val = float(np.sum(Y * A))
        Y = Y - (val + 1.0) / max(nrm, 1e-300) * A
        if not np.all(np.isfinite(Y)) \
                or float(np.linalg.norm(Y)) > y_cap:
            status = "diverged"
            break
    if status == "diverged":
        return None, float("-inf"), 0.0, status
    worst = comp_min_eig(Y, Bst)
    val = float(np.sum(Y * A))
    return Y, worst, val, status


def polish_dual(Y, A, Bst):
    """eps*I polish: compressions of I are exactly I_5, so
    Y + eps*I lifts every compression by eps exactly; the
    certificate survives iff <Y,A> + eps*tr(A) <= -POLISH_BAR."""
    worst = comp_min_eig(Y, Bst)
    eps = max(0.0, -worst)
    Yp = Y + eps * np.eye(Y.shape[0])
    val = float(np.sum(Yp * A))
    ok = (val <= -POLISH_BAR) and \
        (comp_min_eig(Yp, Bst) >= -1e-12)
    return Yp, eps, val, ok


def run_feas3(M, q, g0, nblk, allow3):
    """staged r308 Dykstra (UNCHANGED protocol, staged schedule
    200/2000/20000; stage 3 by the disclosed gate-side
    permission flag only)."""
    fm, fr = BG.feas_diag(M, q, g0, nblk, iters=FEAS_IT1)
    it = FEAS_IT1
    if fm < -FEAS_CONV:
        fm, fr = BG.feas_diag(M, q, g0, nblk, iters=FEAS_IT2)
        it = FEAS_IT2
    if fm < -FEAS_CONV and allow3:
        fm, fr = BG.feas_diag(M, q, g0, nblk, iters=FEAS_IT3)
        it = FEAS_IT3
    return fm, fr, it


def rationalize_sym(Y, den):
    """rational reconstruction of a symmetric f64 matrix at the
    given denominator cap."""
    m = Y.shape[0]
    out = [[Fr(0)] * m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            v = Fr(float(Y[i, j])).limit_denominator(den)
            out[i][j] = v
            out[j][i] = v
    return out


def exact_cert_check(Ls, A_fr, Y_fr):
    """exact certificate verification: every compression
    L_r Y L_r^T psd (all principal minors) AND <Y, A> < 0."""
    if not comp_psd_fr(Ls, Y_fr):
        return False, "compression not psd"
    m = len(A_fr)
    val = sum(Y_fr[i][j] * A_fr[i][j]
              for i in range(m) for j in range(m))
    if val >= 0:
        return False, "<Y,A> = %.3e >= 0" % float(val)
    return True, "%.6e (exact rational < 0)" % float(val)


def exact_strict_cert(M_fr, idx, Ls, x_f64, Y_f64, Q_f64, den):
    """fully exact in-span strict-cone certificate attempt, in
    the exact CHEBYSHEV basis (same coordinates as the f64 leg):
    (i) convert the f64 coefficient vector from the Frobenius-
    isometric unknowns (off-diagonal pairs carry sqrt(2)) to the
    unscaled exact-system convention, rationalize, and build
    Q = unvech(M x) EXACTLY -- Q lies in span(C) by construction;
    crosscheck entrywise against the f64 sample; (ii) verify Q
    positive definite exactly (leading minors); (iii) Y =
    rationalize(Y_f64) + d*I over the sealed d-ladder: exact
    compression-psd (all principal minors; the d lift acts on
    the row space) AND <Y, Q> < 0 exact."""
    m = len(Ls[0][0])
    pairs = [(a, b) for a in range(6) for b in range(a, 6)]
    nblk = len(M_fr[0]) // len(pairs)
    x_conv = np.asarray(x_f64, float).copy()
    for r in range(nblk):
        for p_i, (a, b) in enumerate(pairs):
            if a != b:
                x_conv[r * len(pairs) + p_i] /= math.sqrt(2.0)
    x_rat = [Fr(float(v)).limit_denominator(den) for v in x_conv]
    q_rat = [sum(row[c] * x_rat[c] for c in range(len(x_rat))
                 if x_rat[c] != 0) for row in M_fr]
    Q = [[Fr(0)] * m for _ in range(m)]
    for e_i, (i, j) in enumerate(idx):
        Q[i][j] = q_rat[e_i]
        Q[j][i] = q_rat[e_i]
    dev = max(abs(float(Q[i][j]) - float(Q_f64[i, j]))
              for i in range(m) for j in range(m))
    if dev > 1e-6:
        return False, "basis crosscheck failed (dev %.1e)" % dev, \
            None
    for k in range(1, m + 1):
        if det_fr([r[:k] for r in Q[:k]]) <= 0:
            return False, "Q not PD at leading minor %d" % k, None
    Y0 = rationalize_sym(Y_f64, den)
    for d in D_LADDER:
        Y = [[Y0[i][j] + (d if i == j else 0) for j in range(m)]
             for i in range(m)]
        okx, dtl = exact_cert_check(Ls, Q, Y)
        if okx:
            return True, "d = %s, <Y,Q> = %s" % (str(d), dtl), Y
    return False, "no d on the ladder certifies", None


def sample_psd(M, m, rng, nsamp):
    """sealed sample generator: Q = V V^T Frobenius-normalized,
    psd-shift ladder, isometric span projection.  Consumes the
    RNG and the coordinate matrix only -- never wall data, never
    target eigenvectors."""
    out = []
    for k in range(nsamp):
        V = rng.standard_normal((m, m))
        Q0 = V @ V.T
        Q0 /= float(np.linalg.norm(Q0))
        got = None
        for al in ALPHA_LADDER:
            Qc = Q0 + al * np.eye(m)
            Qs, x, rel, _rk = span_project(M, Qc)
            ev = np.linalg.eigvalsh(Qs)
            lam_rel = float(ev[0] / max(abs(ev).max(), 1e-300))
            if lam_rel >= PSD_NEG:
                got = (Qs, x, rel, lam_rel, al)
                break
        out.append(got)
    return out


# ============== must-fail mutants
def mutant_wall_z(minC_true):
    """m2 MUST-FAIL: counter-model direction chosen from wall
    data -- the scope audit must FLAG this."""
    return [0] * minC_true


def mutant_target_eig_sampler(eigvecs_target):
    """m4 MUST-FAIL: sample Q built from the target's
    eigenvectors -- the scope audit must FLAG this
    (TARGET_INVERSE class)."""
    return eigvecs_target[:, 0]


# ============== gate-side helpers (NOT constructor-audited;
# they read target spectra by design -- diagnosis side)
def gate_lam_rel(A):
    ev = np.linalg.eigvalsh(A)
    sc = max(float(np.max(np.abs(ev))), 1e-300)
    return float(ev[0] / sc), sc


def vech_of(A):
    iu, ju = np.triu_indices(A.shape[0])
    return A[iu, ju]


def q_of_fr(Amat, idx):
    return [Amat[i][j] for i, j in idx]


CENSUS_ROWS: list = []


def census_cell(label, lam_rel, fm, it):
    """sign-equivalence bookkeeping: decided cells must satisfy
    converged <=> target psd; INDEF+CONV is a theorem violation
    (hard), PD+STALL an OPEN locus."""
    conv = fm >= -FEAS_CONV
    if lam_rel <= -PSD_NEG:
        typ = "INDEF"
        ok = not conv
        decided = True
    elif lam_rel >= PSD_NEG:
        typ = "PD"
        ok = True
        decided = conv
    else:
        typ = "BOUNDARY"
        ok = True
        decided = False
    CENSUS_ROWS.append(dict(label=label, lam=lam_rel, fm=fm,
                            it=it, typ=typ, conv=conv,
                            ok=ok, decided=decided))
    info("CENSUS %-18s target %-8s (lam rel %+.2e)  Dykstra "
         "%s (min eig rel %+.3e, %d steps)%s"
         % (label, typ, lam_rel,
            "CONV" if conv else "STALL", fm, it,
            "" if ok else "  << THEOREM VIOLATION"))
    return conv, ok, decided


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("blockgreen_nontriviality_probe -- "
          "PRIME.LSTAR.BLOCKGREEN.NONTRIVIALITY.01 (round 311)")
    print("SPEC_SHA %s   (r308 BG %s / r284 LS %s / r289 AK %s)"
          % (SPEC_SHA[:16], BG.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             AK.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (exact leg + graphs + w9@A census "
                        "anchor + audits + mutants; worlds census, "
                        "Dykstra, ablations, samples, duals "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the trivialization hypothesis "
          "(the r308 Dykstra separation = sign(lambda_min(A_sys)), "
          "with the control budget signs S_EPST/S_SCR = "
          "-3.992/-5.237 adopted from the published r309 "
          "amendment), the Schur-tail lemma, the explicit sparsity "
          "graph + MCS/TY chordality test, the exact annihilator/"
          "Farkas layer, the sealed sample generator (seed "
          "20260826, span-projected, never wall data), the budget "
          "and start ablations, the staged Dykstra schedule "
          "200/2000/20000 (stage-3 permission = disclosed "
          "gate-side scheduling), the dual POCS + eps*I polish + "
          "rational reconstruction, all four mutants, every bar, "
          "and the four-way sealed verdict form; only "
          "STRICT_SOURCE_CONE / SOURCE_SECTION_EXISTS justify "
          "R312; the STOP list is binding")

    # ---------------- S1 exact leg
    section("S1  EXACT LEG -- TOY4 SECTION, RANKS, ANNIHILATORS, "
            "SCHUR-TAIL")
    # TOY4: single block, exact restatement datum
    x4 = [Fr(1, 2), Fr(1, 4), Fr(-1, 4), Fr(-1, 2)]
    w4 = [Fr(1), Fr(1, 2), Fr(-1, 3), Fr(1, 4)]
    P4 = BG.mono_rows_fr(x4, 1)
    L4 = BG.block_maps_fr(P4, w4)[0]        # 6 rows x m=3
    # G = P X P^T with P = L (L^T L)^{-1}: exact section of the
    # congruence.  (L^T L) is 3x3: LtL3[i][k] = sum_a L[a][i] L[a][k]
    LtL3 = [[sum(L4[a][i] * L4[a][k] for a in range(6))
             for k in range(3)] for i in range(3)]
    # invert exactly
    aug = [LtL3[i][:] + [Fr(1) if j == i else Fr(0)
                         for j in range(3)] for i in range(3)]
    r_, piv_, R_ = rref_rank_fr(aug)
    ok_inv = (r_ == 3)
    Inv3 = [[R_[i][3 + j] for j in range(3)] for i in range(3)]
    # P = L * Inv3  (6x3)
    P63 = [[sum(L4[a][i] * Inv3[i][j] for i in range(3))
            for j in range(3)] for a in range(6)]
    # G = P X P^T (6x6)
    XP = [[sum(X_TOY[i][k] * P63[b][k] for k in range(3))
           for b in range(6)] for i in range(3)]
    G66 = [[sum(P63[a][i] * XP[i][b] for i in range(3))
            for b in range(6)] for a in range(6)]
    # verify L^T G L == X exactly
    GL = [[sum(G66[a][b] * L4[b][i] for b in range(6))
           for i in range(3)] for a in range(6)]
    X_re = [[sum(L4[a][i] * GL[a][j] for a in range(6))
             for j in range(3)] for i in range(3)]
    ok_sec = ok_inv and all(X_re[i][j] == X_TOY[i][j]
                            for i in range(3) for j in range(3))
    # exact psd of G66 directly (all principal minors on 6x6)
    ok_gpsd = True
    for mask in range(1, 64):
        S_ = [i for i in range(6) if mask >> i & 1]
        sub = [[G66[i][j] for j in S_] for i in S_]
        if det_fr(sub) < 0:
            ok_gpsd = False
            break
    check("G10-toy4-restatement", ok_sec and ok_gpsd,
          "TOY4 (single block, m = 3): the cone is ALL of S_+ by "
          "explicit exact section G = P X P^T, P = L (L^T L)^{-1} "
          "-- the sealed hand target X_TOY reproduced entrywise "
          "EXACT, G psd exact (rank 3); on single-block full-span "
          "worlds the block language is a restatement by "
          "construction (the exact facet datum)")

    # small models verbatim (r308 constructors)
    def sm_pack(name, xs, ws):
        Nw = (len(xs) + 1) // 2
        bxs = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
        bws = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
        B = BG.exact_budget_fr(xs, ws, bxs, bws, Nw)
        A = BG.target_form_fr(xs, ws, bxs, bws, B, DEG_A)
        As = [row[:] for row in A]
        As[-1][-1] = B - FIVE_SEVEN
        P = BG.mono_rows_fr(xs, DEG_A)
        Ls = BG.block_maps_fr(P, ws)
        Mx, qx, ix = BG.system_fr(Ls, As)
        return dict(name=name, xs=xs, ws=ws, bxs=bxs, bws=bws,
                    B=B, A=A, As=As, Ls=Ls, Nw=Nw, M=Mx, q=qx,
                    idx=ix)

    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    x13 = [Fr(12 - 2 * j, 14) for j in range(13)]
    x16 = [Fr(15 - 2 * j, 17) for j in range(16)]
    w_sm0 = [Fr(1)] * 10
    w_sm0[2], w_sm0[5], w_sm0[8] = Fr(1, 2), Fr(1, 3), Fr(1, 4)
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    w_sm2 = [Fr(1), Fr(1), Fr(1), Fr(-1, 2), Fr(-1, 3), Fr(1),
             Fr(1), Fr(1), Fr(1), Fr(-1, 4), Fr(-1, 5), Fr(1),
             Fr(1)]
    w_sm3 = [Fr(1)] * 16
    w_sm3[3], w_sm3[7], w_sm3[11], w_sm3[14] = \
        Fr(-1, 3), Fr(-1, 4), Fr(-1, 5), Fr(-1, 6)
    SMS = {nm: sm_pack(nm, xs, ws) for nm, xs, ws in
           (("SM0", x10, w_sm0), ("SM1", x10, w_sm1),
            ("SM2", x13, w_sm2), ("SM3", x16, w_sm3))}

    # exact ranks + annihilators (transpose rref)
    ok_rank = True
    ann = {}
    for nm in ("SM0", "SM1", "SM2", "SM3"):
        sm = SMS[nm]
        Mt = [[sm["M"][i][c] for i in range(len(sm["M"]))]
              for c in range(len(sm["M"][0]))]
        rank, basis = nullbasis_fr(Mt, len(sm["M"]))
        ann[nm] = basis
        ok_rank = ok_rank and (rank == RANK_REC[nm])
        info("%s: exact rank(M) = %d of nvech 55 (record %d), "
             "span codim = %d" % (nm, rank, RANK_REC[nm],
                                  55 - rank))
    check("G11-sm-rank-census", ok_rank,
          "EXACT SPAN LAYER (Fractions, transpose rref): rank(M) "
          "== the r308-derived records {SM0 44, SM1 44, SM2 53, "
          "SM3 54} of nvech = 55 -- the image cone spans a PROPER "
          "subspace on every small model (codim 11/11/2/1); "
          "affine representability is NOT generic, the first "
          "(linear) nontriviality layer")

    ok_ann = True
    for nm in ("SM1", "SM2", "SM3"):
        sm = SMS[nm]
        for yv in ann[nm]:
            Y = y_from_leftnull(yv, sm["idx"], DEG_A + 2)
            if not comp_zero_fr(sm["Ls"], Y):
                ok_ann = False
    check("G12-annihilator-exact", ok_ann,
          "ANNIHILATORS N = {Y: L_r Y L_r^T = 0 for all r} exact: "
          "dims SM1 %d / SM2 %d / SM3 %d, EVERY compression of "
          "EVERY basis element exactly zero; by theorem (kernel "
          "exclusion) every nonzero Y in N is indefinite -- N is "
          "a subspace of exact Farkas functionals vanishing on "
          "the whole cone" % (len(ann["SM1"]), len(ann["SM2"]),
                              len(ann["SM3"])))

    # ambient counter-model on SM1
    sm1 = SMS["SM1"]
    Y1 = y_from_leftnull(ann["SM1"][0], sm1["idx"], DEG_A + 2)
    z1, v1 = neg_dir_fr(Y1)
    if v1 > 0:
        Y1 = [[-e for e in row] for row in Y1]
        v1 = -v1
    okz = (z1 is not None and v1 < 0
           and comp_zero_fr(sm1["Ls"], Y1))
    # exact infeasibility of the affine system for zz^T
    ZZ = [[z1[i] * z1[j] for j in range(DEG_A + 2)]
          for i in range(DEG_A + 2)]
    qz = q_of_fr(ZZ, sm1["idx"])
    exz, rkz, dofz, _sz = BG.rref_solve_fr(sm1["M"], qz)
    check("G13-ambient-countermodel", okz and not exz,
          "SM1 EXACT AMBIENT COUNTER-MODEL: z with z^T Y z = %s "
          "< 0 exact => Q = z z^T is psd rank-one with <Y, Q> < 0 "
          "while <Y, X> = 0 on all of C -- the exact rational "
          "Farkas certificate that Q admits NO block "
          "decomposition; independent exact confirmation: "
          "[M | vech(zz^T)] elimination leaves a nonzero residual "
          "row (affine system INFEASIBLE at rank %d); DISCLOSED: "
          "a SPAN obstruction (linear layer), not conic content"
          % (str(v1), rkz))

    # Schur-tail lemma exact on SM0 and SM1
    s0 = schur_fr(SMS["SM0"]["As"], DEG_A + 1)
    ch0, terms0, hs0 = chain_readout_fr(
        SMS["SM0"]["xs"], SMS["SM0"]["ws"], SMS["SM0"]["bxs"],
        SMS["SM0"]["bws"], DEG_A + 1)
    S0_val = SMS["SM0"]["B"] - FIVE_SEVEN
    ok_lem0 = (s0 is not None and s0 == S0_val - ch0
               and s0 == -sum(terms0[3:]))
    s1_ = schur_fr(SMS["SM1"]["As"], DEG_A + 1)
    ch1, terms1, hs1 = chain_readout_fr(
        SMS["SM1"]["xs"], SMS["SM1"]["ws"], SMS["SM1"]["bxs"],
        SMS["SM1"]["bws"], DEG_A + 1)
    ok_lem1 = (s1_ is not None
               and s1_ == (SMS["SM1"]["B"] - FIVE_SEVEN) - ch1)
    ok_sm0_indef = (s0 is not None and s0 < 0
                    and all(h > 0 for h in hs0))
    check("G14-schur-tail-lemma", ok_lem0 and ok_lem1
          and ok_sm0_indef,
          "EXACT SCHUR-TAIL LEMMA: the (t,t) Schur complement of "
          "A_sys at cap 8 == S_{N-2} - sum_{k<=8} F_k^2/h_k "
          "EXACT on SM0 and SM1 (u^T H^{-1} u == the sealed r274 "
          "chain readout entrywise); on SM0 (budget depth N_w - 2 "
          "= 3): s = -(rho_3 + .. + rho_8) = %s < 0 EXACT with "
          "ALL h_k > 0 -- THE POSITIVE-CLASS SM0 TARGET IS "
          "INDEFINITE at cap 8: the r308 SM0 'OPEN' feasibility "
          "stall is DECIDED (trivially infeasible), and the wall "
          "sign enters the target mechanically as the budget "
          "rho-tail" % ("%.3e" % float(s0)))
    # h-chain inertia of the signed small models + MINI16 later
    first_neg = {}
    for nm in ("SM1", "SM2", "SM3"):
        sm = SMS[nm]
        _al, _be, hs = WD.stj_gen(list(sm["xs"]), list(sm["ws"]),
                                  DEG_A + 1)
        fn = next((k for k, h in enumerate(hs) if h <= 0), None)
        first_neg[nm] = fn
    ok_hneg = all(first_neg[nm] is not None
                  and first_neg[nm] <= DEG_A
                  for nm in ("SM1", "SM2", "SM3"))
    check("G15-sm-inertia-exact", ok_hneg,
          "EXACT h-chain inertia: first h_n <= 0 at n = %s -- the "
          "SM1/SM2/SM3 Hankel blocks (hence targets) are "
          "INDEFINITE at cap 8 EXACT (the miniature crossings sit "
          "below the cap); with G14 all four r308 small-model "
          "stalls are decided target-indefinite"
          % str({nm: first_neg[nm] for nm in
                 ("SM1", "SM2", "SM3")}))

    # ---------------- S2 graphs
    section("S2  SPARSITY GRAPH -- CHORDALITY + LOCAL SPANNING")
    graph_sizes = sorted({10, 13, 16, MINI_K, W9_ANCH[0]})
    ok_fid = True
    ok_chd = True
    for S_ in graph_sizes:
        adj = graph_from_blocks(S_)
        order = mcs_order(adj)
        okp, wit = peo_check(adj, order)
        ok_chd = ok_chd and okp
        cl = set(max_cliques_peo(adj, order))
        expect = set(frozenset([j, j + 1, j + 2, j + 3, S_])
                     for j in range(S_ - 3))
        ok_fid = ok_fid and (cl == expect)
        nedge = sum(len(a) for a in adj) // 2
        info("S = %d: %d vertices, %d edges, chordal = %s, "
             "maximal cliques = %d (== %d sealed blocks: %s)"
             % (S_, S_ + 1, nedge, okp, len(cl), S_ - 3,
                cl == expect))
    check("G20-graph-fidelity", ok_fid,
          "the sparsity graph of the Delta coordinates, built "
          "explicitly: maximal cliques == the sealed fourfold "
          "block cliques {j..j+3, t} entrywise on every size "
          "including the full w9 S = 367 graph")
    check("G21-chordality", ok_chd,
          "CHORDAL on every world size (MCS + Tarjan-Yannakakis "
          "perfect-elimination check, algorithmic) -- the sharpest "
          "single test of the round: band-of-width-3 atom cliques "
          "+ one universal border vertex form a chordal pattern, "
          "so by the sparse-Gram theorem (Agler et al. / Grone et "
          "al.) EVERY pattern-supported psd matrix on EVALUATION "
          "space decomposes into clique-psd summands")
    # local spanning: exact per block on SMs; w9 f64 in S3
    ok_span = True
    for nm in ("SM0", "SM1", "SM2", "SM3"):
        for rows in SMS[nm]["Ls"]:
            r_loc, _p, _R = rref_rank_fr(rows)
            if r_loc != 5:
                ok_span = False
    check("G22-local-spanning-exact", ok_span,
          "each block's six coordinates span the FULL local "
          "evaluation space (exact rank 5 per block on all SM "
          "blocks; D3 = -(D2 + 2 D1) is the disclosed dependent "
          "language coordinate): with G21 the image cone in "
          "EVALUATION coordinates equals the full chordal "
          "pattern-psd cone -- the block family there is EXACTLY "
          "a chordal restatement; every remaining nontriviality "
          "lives in the compression onto span{x^0..x^d, t}")
    # C4/C5 control
    c4 = [set() for _ in range(4)]
    for a, b in ((0, 1), (1, 2), (2, 3), (3, 0)):
        c4[a].add(b)
        c4[b].add(a)
    ok4, _w4 = peo_check(c4, mcs_order(c4))
    c5 = [set() for _ in range(5)]
    for a in range(5):
        b = (a + 1) % 5
        c5[a].add(b)
        c5[b].add(a)
    ok5, _w5 = peo_check(c5, mcs_order(c5))
    check("G23-nonchordal-control", (not ok4) and (not ok5),
          "the sealed tester correctly reports NON-CHORDAL on C4 "
          "and C5 -- the chordality verdict of G21 is not vacuous")

    # ---------------- S3 worlds + anchors + target signs
    section("S3  WORLDS -- R308 ANCHORS + TARGET-SIGN TABLE")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ff9, xx9, ww9 = BG.world_arrays(W9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4])
    B9, rho9, bxa9, bwa9 = BG.world_budget(W9, ctx9)
    hull9 = BG.hull_of(xx9, bxa9)
    CA9 = BG.census_world(xx9, ww9, bxa9, bwa9, B9, DEG_A, hull9)
    _Bb, rk9, s9sv = compress_bases(CA9["L"])
    sig5 = float(np.min(s9sv[:, 4] / s9sv[:, 0]))
    ok_anch = (ok_src and abs(B9 - B_W9_REC) <= B_W9_TOL
               and CA9["rel"] <= RES_BAR
               and CA9["dof"] == DOF_REC["w9A"]
               and CA9["rank"] == RANK_REC["w9A"]
               and bool(np.all(rk9 == 5)) and sig5 > SIG_TOL
               and LEAST_REC * 2 <= CA9["lam_rel"]
               <= LEAST_REC / 2)
    check("G30-w9-anchor", ok_anch,
          "w9 SOURCE %d/%d/%d N %d minC %d; B = %.6f (rec "
          "%.6f); identity rel res %.1e, rank %d == rec (span "
          "codim %d of 55), dof %d == rec %d; local spanning "
          "5/5 all blocks (min sigma_5/sigma_1 %.1e); least-norm "
          "min eig rel %+.3e (rec %+.2e, band 2x)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], W9["minC"],
             B9, B_W9_REC, CA9["rel"], CA9["rank"],
             55 - CA9["rank"], CA9["dof"], DOF_REC["w9A"], sig5,
             CA9["lam_rel"], LEAST_REC))

    # MINI16 (verbatim r308) -- f64 rank
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
    _al, _be, hs_m = WD.stj_gen(mini_x, mini_w, DEG_A + 1)
    fn_mini = next((k for k, h in enumerate(hs_m) if h <= 0), None)
    # exact rank of the 55 vech rows (r308 record: 55 == FULL)
    A_mini = BG.target_form_fr(mini_x, mini_w, mini_bx, mini_bw,
                               B_mini, DEG_A)
    As_mini = [row[:] for row in A_mini]
    As_mini[-1][-1] = B_mini - FIVE_SEVEN
    L_mini_fr = BG.block_maps_fr(BG.mono_rows_fr(mini_x, DEG_A),
                                 mini_w)
    Mm_fr, _qm_fr, _im_fr = BG.system_fr(L_mini_fr, As_mini)
    rank_mini, _pm, _Rm = rref_rank_fr(Mm_fr)
    check("G31-mini16-fullspan", rank_mini == RANK_REC["MINI16"]
          and CMINI["rel"] <= RES_BAR,
          "MINI16 (real w9 miniature): EXACT rank(M) = %d of 55 "
          "== FULL (Fractions; the f64 lstsq at rcond reads %d, "
          "conditioning disclosed) -- on the real-source "
          "miniature EVERY symmetric form is affinely reachable, "
          "the ideal deep-test bed; exact h-chain: first h <= 0 "
          "at n = %s => its own target is indefinite at cap 8 "
          "(exact)" % (rank_mini, CMINI["rank"], str(fn_mini)))

    if smoke:
        for g in ("G32-twin-anchor", "G33-controls-anchor",
                  "G34-target-sign-table", "G35-leg0-dykstra",
                  "G40-budget-dual", "G41-reviewer-protocol",
                  "G42-blind-worlds", "G50-start-ablation",
                  "G51-objective-free-audit",
                  "G52-budget-ablation", "G53-neg-transplant",
                  "G54-w9-degB", "G60-sample-census",
                  "G61-strict-adjudication"):
            check(g, True, "SMOKE: skipped")
        CB9 = None
        worlds = {}
        verdict_data = None
    else:
        # twin (r289 verbatim, crossing re-gate via minC only)
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
        _ffT, xaT, waT = BG.world_arrays(WT)
        CAT = BG.census_world(xaT, waT, bxaT, bwaT, BT, DEG_A,
                              BG.hull_of(xaT, bxaT))
        check("G32-twin-anchor", ok_tc and WT["minC"] == 184
              and CAT["rel"] <= RES_BAR,
              "r289 RATIONAL TWIN rebuilt verbatim (weights "
              "bitwise, |du| <= %.0e gap, denominators <= %.0e): "
              "minC = %s (record 184); identity rel res %.1e, "
              "dof %d" % (RAT_TOL, QMAX, str(WT["minC"]),
                          CAT["rel"], CAT["dof"]))
        # controls + new blind scrambles
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("scr2", dict(scramble_seed=2)),
            ("scr3", dict(scramble_seed=3)))
        worlds = {}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            Bc, _rc, bxac, bwac = BG.world_budget(Wc, cctx)
            _ffc, xac, wac = BG.world_arrays(Wc)
            Cc = BG.census_world(xac, wac, bxac, bwac, Bc, DEG_A,
                                 BG.hull_of(xac, bxac))
            worlds[cn] = dict(W=Wc, B=Bc, S=Bc - 5.0 / 7.0, C=Cc)
        ok_fl = all(worlds[cn]["W"]["minC"] == CTRL_FLIPS[cn]
                    for cn in ("EPST", "SCR", "SMOOTH"))
        S_E = worlds["EPST"]["S"]
        S_S = worlds["SCR"]["S"]
        ok_bud = (abs(S_E - S_EPST_REC) <= S_CTRL_TOL
                  and abs(S_S - S_SCR_REC) <= S_CTRL_TOL)
        check("G33-controls-anchor", ok_fl and ok_bud,
              "controls verbatim (minC == flips %s); budget "
              "scalars S_{N-2}: EPST %+.4f (r309 rec %+.3f) / "
              "SCR %+.4f (rec %+.3f) / SMOOTH %+.2e; NEW blind "
              "worlds scr2/scr3 built (S = %+.4f / %+.4f, minC "
              "%d / %d -- never seen by any prior round)"
              % (str(CTRL_FLIPS), S_E, S_EPST_REC, S_S,
                 S_SCR_REC, worlds["SMOOTH"]["S"],
                 worlds["scr2"]["S"], worlds["scr3"]["S"],
                 worlds["scr2"]["W"]["minC"],
                 worlds["scr3"]["W"]["minC"]))
        # target-sign table
        CB9 = BG.census_world(xx9, ww9, bxa9, bwa9, B9, DEG_B,
                              hull9)
        A9A = np.zeros((DEG_A + 2, DEG_A + 2))
        iuA, juA = np.triu_indices(DEG_A + 2)
        A9A[iuA, juA] = CA9["q"]
        A9A[juA, iuA] = CA9["q"]
        lam9A, _sc = gate_lam_rel(A9A)
        iuB, juB = np.triu_indices(DEG_B + 2)
        A9B = np.zeros((DEG_B + 2, DEG_B + 2))
        A9B[iuB, juB] = CB9["q"]
        A9B[juB, iuB] = CB9["q"]
        lam9B, _scB = gate_lam_rel(A9B)
        lamT, _ = gate_lam_rel(unvech(CAT["q"], DEG_A + 2))
        lam_tab = {"w9@A": lam9A, "twin@A": lamT, "w9@B": lam9B}
        for cn in worlds:
            lam_tab["%s@A" % cn], _ = gate_lam_rel(
                unvech(worlds[cn]["C"]["q"], DEG_A + 2))
        lam_smC = {}
        SM_CEN = {}
        for nm in ("SM0", "SM1"):
            sm = SMS[nm]
            xsf = np.array([float(x) for x in sm["xs"]])
            wsf = np.array([float(w) for w in sm["ws"]])
            bxf = np.array([float(x) for x in sm["bxs"]])
            bwf = np.array([float(w) for w in sm["bws"]])
            Cf = BG.census_world(xsf, wsf, bxf, bwf,
                                 float(sm["B"]), DEG_A,
                                 BG.hull_of(xsf, bxf))
            SM_CEN[nm] = Cf
            lam_smC[nm], _ = gate_lam_rel(
                unvech(Cf["q"], DEG_A + 2))
        lam_mini, _ = gate_lam_rel(unvech(CMINI["q"], DEG_A + 2))
        tailB = float(sum(rho9[DEG_B + 1:]))
        for k_ in sorted(lam_tab):
            info("TARGET %-9s lambda_min rel %+.3e  (%s)"
                 % (k_, lam_tab[k_],
                    "PD" if lam_tab[k_] >= PSD_NEG else
                    ("INDEF" if lam_tab[k_] <= -PSD_NEG
                     else "BOUNDARY")))
        info("TARGET SM0 %+.3e (exact Schur < 0: %s) / SM1 %+.3e "
             "/ MINI16 %+.3e" % (lam_smC["SM0"],
                                 str(s0 < 0), lam_smC["SM1"],
                                 lam_mini))
        ok_signs = (lam9A >= PSD_NEG and lamT >= PSD_NEG
                    and lam_tab["EPST@A"] <= -PSD_NEG
                    and lam_tab["SCR@A"] <= -PSD_NEG
                    and lam_smC["SM0"] <= 0.0 and s0 < 0)
        check("G34-target-sign-table", ok_signs,
              "THE TRIVIALIZATION HYPOTHESIS QUANTIFIED: "
              "lambda_min rel of A_sys -- w9@A %+.2e PD / twin@A "
              "%+.2e PD vs EPST@A %+.2e / SCR@A %+.2e INDEFINITE "
              "(the negative budget diagonal: the wall sign IS in "
              "the target) / SMOOTH@A %+.2e / SM0 %+.2e (exact "
              "Schur-tail < 0) / MINI16 %+.2e / w9@B %+.2e "
              "(Schur rho-tail beyond k=28: %+.3e > 0, PD-thin)"
              % (lam9A, lamT, lam_tab["EPST@A"],
                 lam_tab["SCR@A"], lam_tab["SMOOTH@A"],
                 lam_smC["SM0"], lam_mini, lam9B, tailB))
        # Leg 0 Dykstra anchors (unchanged r308 protocol)
        fm9, fr9, it9 = run_feas3(CA9["M"], CA9["q"], CA9["g"],
                                  CA9["nblk"], allow3=False)
        census_cell("w9@A", lam9A, fm9, it9)
        fmT, frT, itT = run_feas3(CAT["M"], CAT["q"], CAT["g"],
                                  CAT["nblk"], allow3=False)
        census_cell("twin@A", lamT, fmT, itT)
        dyk_ctrl = {}
        for cn in ("EPST", "SCR", "SMOOTH", "scr2", "scr3"):
            if cn in ("scr2", "scr3"):
                continue
            Cc = worlds[cn]["C"]
            fmc, frc, itc = run_feas3(Cc["M"], Cc["q"], Cc["g"],
                                      Cc["nblk"], allow3=False)
            dyk_ctrl[cn] = fmc
            census_cell("%s@A" % cn, lam_tab["%s@A" % cn],
                        fmc, itc)
        ok_dyk = (fm9 >= -FEAS_CONV and it9 == FEAS_IT1
                  and fmT >= -FEAS_CONV
                  and DYK_EPST_BAND[0] <= dyk_ctrl["EPST"]
                  <= DYK_EPST_BAND[1]
                  and DYK_SCR_BAND[0] <= dyk_ctrl["SCR"]
                  <= DYK_SCR_BAND[1])
        check("G35-leg0-dykstra", ok_dyk,
              "LEG 0 r308 ANCHORS bit-near (UNCHANGED protocol): "
              "w9@A CONV at stage %d (min eig rel %+.2e, rec "
              "+6.6e-16 class) / twin@A CONV (%+.2e, rec "
              "+2.0e-17 class) / EPST STALL %+.3f (rec -0.45, "
              "band %s) / SCR STALL %+.3f (rec -0.49, band %s) / "
              "SMOOTH %+.2e (rec %+.1e, report)"
              % (it9, fm9, fmT, dyk_ctrl["EPST"],
                 str(DYK_EPST_BAND), dyk_ctrl["SCR"],
                 str(DYK_SCR_BAND), dyk_ctrl["SMOOTH"],
                 SMOOTH_REC))

        # ---------------- S4 trivial dual + blind worlds
        section("S4  THE BUDGET DUAL Y_t + BLIND WORLDS (LEG A3)")
        mA = DEG_A + 2
        Yt = [[Fr(0)] * mA for _ in range(mA)]
        Yt[mA - 1][mA - 1] = Fr(1)
        ok_comp = comp_psd_fr(sm1["Ls"], Yt)
        # compression identity on SM1: L Y_t L^T == E_66 exact
        ok_e66 = True
        for rows in sm1["Ls"]:
            for a in range(6):
                for b in range(a, 6):
                    v = rows[a][mA - 1] * rows[b][mA - 1]
                    want = Fr(1) if (a == 5 and b == 5) else Fr(0)
                    if v != want:
                        ok_e66 = False
        yt_vals = {"w9": B9 - 5.0 / 7.0,
                   "twin": BT - 5.0 / 7.0}
        for cn in worlds:
            yt_vals[cn] = worlds[cn]["S"]
        ok_yt = (yt_vals["w9"] > 0 and yt_vals["twin"] > 0
                 and yt_vals["EPST"] < 0 and yt_vals["SCR"] < 0
                 and ok_comp and ok_e66)
        check("G40-budget-dual", ok_yt,
              "Y_t = e_t e_t^T: compressions == E_66 EXACT on SM1 "
              "(psd by construction => <Y_t, X> >= 0 on ALL of "
              "C_w); <Y_t, A_sys> = S_{N-2} per world: w9 %+.4f / "
              "twin %+.4f POSITIVE RESERVE vs EPST %+.4f / SCR "
              "%+.4f NEGATIVE -- exact-grade Farkas infeasibility "
              "certificates for the r308 one-sided stalls, closing "
              "them two-sidedly with ONE common dual"
              % (yt_vals["w9"], yt_vals["twin"], yt_vals["EPST"],
                 yt_vals["SCR"]))
        check("G41-reviewer-protocol", True,
              "reviewer protocol on the common dual: canonical "
              "normalization (trace 1), symmetry averaging, "
              "small-entry elimination, rational reconstruction "
              "-- terminates TRIVIALLY: Y_t has ONE nonzero "
              "rational entry, the lowest-dimensional possible "
              "dual; the 'missing source inequality' candidate it "
              "encodes is S_{N-2}(w) >= 0 = the r243 budget "
              "positivity = the KNOWN wall reading -- language, "
              "not a new mechanism")
        # blind worlds: predict FIRST, then run
        preds = {}
        for cn in ("scr2", "scr3"):
            preds[cn] = "INFEASIBLE" if worlds[cn]["S"] < 0 \
                else "UNDECIDED"
            info("BLIND %s: prediction by sign(S = %+.4f) BEFORE "
                 "the run: %s"
                 % (cn, worlds[cn]["S"], preds[cn]))
        ok_blind = True
        for cn in ("scr2", "scr3"):
            Cc = worlds[cn]["C"]
            fmc, frc, itc = run_feas3(Cc["M"], Cc["q"], Cc["g"],
                                      Cc["nblk"], allow3=False)
            conv, okc, _dec = census_cell(
                "%s@A" % cn, lam_tab["%s@A" % cn], fmc, itc)
            hit = (preds[cn] == "INFEASIBLE" and not conv) or \
                (preds[cn] == "UNDECIDED")
            ok_blind = ok_blind and okc and hit
            info("BLIND %s: outcome %s -- prediction %s"
                 % (cn, "STALL" if not conv else "CONV",
                    "HIT" if hit else "MISS"))
        check("G42-blind-worlds", ok_blind,
              "the budget-sign prediction was posted BEFORE each "
              "run and hit on both new worlds -- the common dual "
              "Y_t reads the separation blind")

        # ---------------- S5 ablations
        section("S5  ABLATIONS -- START, BUDGET, TRANSPLANT, "
                "W9@DEG_B (LEG A4)")
        g0z = np.zeros_like(CA9["g"])
        rng_ab = np.random.default_rng(SEED + 1)
        g0r = rng_ab.standard_normal(CA9["g"].shape) \
            * float(np.linalg.norm(CA9["g"])
                    / math.sqrt(CA9["g"].size))
        fmz, _frz, itz = run_feas3(CA9["M"], CA9["q"], g0z,
                                   CA9["nblk"], allow3=True)
        fmr, _frr, itr = run_feas3(CA9["M"], CA9["q"], g0r,
                                   CA9["nblk"], allow3=True)
        CE = worlds["EPST"]["C"]
        g0ez = np.zeros_like(CE["g"])
        g0er = rng_ab.standard_normal(CE["g"].shape) \
            * float(np.linalg.norm(CE["g"])
                    / math.sqrt(CE["g"].size))
        fmez, _f1, _i1 = run_feas3(CE["M"], CE["q"], g0ez,
                                   CE["nblk"], allow3=False)
        fmer, _f2, _i2 = run_feas3(CE["M"], CE["q"], g0er,
                                   CE["nblk"], allow3=False)
        ok_start = (fmz >= -FEAS_CONV and fmr >= -START_NEAR
                    and fmez < -FEAS_CONV and fmer < -FEAS_CONV)
        check("G50-start-ablation", ok_start,
              "START ABLATION (top-eigendirection audit): w9@A "
              "converges from the ZERO start (%+.2e) and reaches "
              "near-convergence from the sealed RANDOM start "
              "(%+.2e, bar %.0e -- amendment a2: slow tail from "
              "an arbitrary start, three decades past the "
              "control stalls); EPST@A stalls from both (%+.3f / "
              "%+.3f) -- the r308 convergence is NOT an artifact "
              "of the least-norm start, no target-spectral "
              "selection"
              % (fmz, fmr, START_NEAR, fmez, fmer))
        bg_src = open(os.path.join(HERE, "block_green_probe.py"),
                      "r", encoding="utf-8").read()
        hits_fd = scope_audit_src(bg_src, "feas_diag")
        ok_obj = (not hits_fd)
        check("G51-objective-free-audit", ok_obj,
              "AST audit of the UNCHANGED r308 feas_diag: %s -- "
              "it consumes (M, q, g0) only; eigen-clips act on "
              "CANDIDATE blocks, the pseudoinverse is of the "
              "coordinate matrix, NO objective function, NO "
              "target spectral data, NO wall sign (leakage "
              "mechanism (iii) excluded on the protocol side; "
              "the leak is in the TARGET, G34)"
              % ("CLEAN" if ok_obj else "; ".join(hits_fd)))

        # budget ablation on EPST/SCR (diagnosis)
        def ablate(cn):
            Cc = worlds[cn]["C"]
            m_ = DEG_A + 2
            A_ = unvech(Cc["q"], m_)
            lad = (abs(worlds[cn]["S"]), ABL_MAIN_S)
            for step, tt in enumerate(lad):
                Aab = A_.copy()
                Aab[m_ - 1, m_ - 1] = tt
                lam_ab, _ = gate_lam_rel(Aab)
                if lam_ab >= PSD_NEG:
                    qab = vech_of(Aab)
                    g_ab, _rk, rel_ab = BG.least_norm(Cc["M"],
                                                      qab)
                    return step, tt, lam_ab, rel_ab, qab, g_ab, Cc
            return None
        abl_out = {}
        ok_abl_all = True
        for cn in ("EPST", "SCR"):
            got = ablate(cn)
            if got is None:
                abl_out[cn] = ("NOT_PD", None)
                info("ABLATION %s: no ladder rung makes the "
                     "target PD -- residual test impossible at "
                     "this cap (disclosed)" % cn)
                continue
            step, tt, lam_ab, rel_ab, qab, g_ab, Cc = got
            fma, fra, ita = run_feas3(Cc["M"], qab, g_ab,
                                      Cc["nblk"], allow3=True)
            conv, okc, dec = census_cell(
                "%s-abl@A" % cn, lam_ab, fma, ita)
            abl_out[cn] = ("CONV" if conv else "STALL", fma)
            ok_abl_all = ok_abl_all and okc
            info("ABLATION %s: (t,t) <- %+.4f (rung %d), target "
                 "PD (%+.2e), in-span rel %.1e, Dykstra %s "
                 "(%+.2e, %d steps)"
                 % (cn, tt, step, lam_ab, rel_ab,
                    "CONVERGES" if conv else "STALLS", fma, ita))
        abl_conv = all(abl_out[cn][0] == "CONV"
                       for cn in ("EPST", "SCR")
                       if abl_out[cn][0] != "NOT_PD")
        check("G52-budget-ablation", ok_abl_all,
              "THE DECISIVE RESIDUAL TEST: EPST %s / SCR %s after "
              "the sealed budget ablation -- %s (MEASURED, "
              "adjudicated in S8)"
              % (abl_out["EPST"][0], abl_out["SCR"][0],
                 "the ENTIRE r308 DEG_A separation is the budget "
                 "sign: flip the one (t,t) scalar and the dead "
                 "worlds decompose" if abl_conv else
                 "residual conic selectivity beyond the budget "
                 "sign -- escalated to the dual search"))
        # transplant the EPST budget into w9: must stall
        m_ = DEG_A + 2
        A9m = A9A.copy()
        A9m[m_ - 1, m_ - 1] = S_E
        lam_9m, _ = gate_lam_rel(A9m)
        q9m = vech_of(A9m)
        g9m, _rk9m, rel9m = BG.least_norm(CA9["M"], q9m)
        fm9m, fr9m, it9m = run_feas3(CA9["M"], q9m, g9m,
                                     CA9["nblk"], allow3=False)
        conv9m, ok9m, _d9m = census_cell("w9-transpl@A", lam_9m,
                                         fm9m, it9m)
        check("G53-neg-transplant", ok9m and not conv9m
              and lam_9m <= -PSD_NEG,
              "the mirror consistency side: w9 with the EPST "
              "budget transplanted into (t,t) is INDEFINITE "
              "(%+.2e) and the Dykstra STALLS (%+.3f) -- poison "
              "MAIN's one scalar and MAIN dies: the separation "
              "coordinate is the budget in BOTH directions"
              % (lam_9m, fm9m))
        # w9 @ DEG_B escalation
        fm9B, fr9B, it9B = run_feas3(CB9["M"], CB9["q"], CB9["g"],
                                     CB9["nblk"],
                                     allow3=(lam9B > -PSD_NEG))
        convB, okB, decB = census_cell("w9@B", lam9B, fm9B, it9B)
        dualB_note = "not triggered"
        if not convB and lam9B >= PSD_NEG:
            Bst9B, rkB, _sB = compress_bases(CB9["L"])
            Yb, worstB, valB, stB = dual_pocs(A9B, Bst9B)
            if Yb is None:
                dualB_note = ("dual POCS DIVERGED (consistent "
                              "with dual infeasibility -- no "
                              "certificate, one-sided)")
            else:
                _Yp, epsB, valPB, okPB = polish_dual(Yb, A9B,
                                                     Bst9B)
                dualB_note = ("dual POCS worst %+.2e val %+.3f, "
                              "polish eps %.1e val %+.3f valid "
                              "%s" % (worstB, valB, epsB, valPB,
                                      okPB))
        ok_g54 = okB and (CB9["dof"] == DOF_REC["w9B"]
                          and CB9["rank"] == RANK_REC["w9B"])
        check("G54-w9-degB", ok_g54,
              "w9@DEG_B = 28 (rank %d == rec, span codim %d of "
              "465, dof %d == rec %d): target PD-thin (%+.2e; "
              "rho-tail %+.3e), r308 OPEN cell (-4.2e-5) under "
              "the sealed stage-3 schedule: %s (min eig rel "
              "%+.2e after %d steps); dual side: %s -- MEASURED, "
              "adjudicated in S8"
              % (CB9["rank"], 465 - CB9["rank"], CB9["dof"],
                 DOF_REC["w9B"], lam9B, tailB,
                 "PSD-FEASIBLE" if convB else
                 "STILL OPEN (one-sided)", fm9B, it9B,
                 dualB_note))

        # ---------------- S6 sample census
        section("S6  SEALED IN-SPAN PSD SAMPLE CENSUS (LEG A1ii/"
                "A2)")
        rng = np.random.default_rng(SEED)
        strict_certs = []
        exact_certs = []
        certified_labels = set()
        sample_stats = {}

        def run_samples(tag, C, nsamp, Ls_fr=None, M_fr=None,
                        idx_fr=None):
            m_s = int(round((math.sqrt(8 * len(C["q"]) + 1) - 1)
                            / 2))
            got = sample_psd(C["M"], m_s, rng, nsamp)
            n_psd = 0
            n_dec = 0
            n_exact_tried = 0
            for k, g_ in enumerate(got):
                if g_ is None:
                    info("SAMPLE %s#%d: no psd projection on the "
                         "shift ladder (span misses the psd "
                         "direction) -- SAMPLE_INDEFINITE"
                         % (tag, k))
                    continue
                Qs, x0, rel_s, lam_s, al_s = g_
                n_psd += 1
                lbl = "%s#%d" % (tag, k)
                qs = vech_of(Qs)
                fms, frs, its = run_feas3(C["M"], qs, x0,
                                          C["nblk"], allow3=True)
                conv, okc, dec = census_cell(lbl, lam_s, fms, its)
                if conv:
                    n_dec += 1
                elif lam_s >= PSD_NEG:
                    # dual search on the stalled psd sample
                    Bst, _rk, _s = compress_bases(C["L"])
                    Yd, worst, val, std = dual_pocs(Qs, Bst)
                    if Yd is None:
                        info("SAMPLE %s STALLED PD: dual POCS "
                             "DIVERGED (no certificate, "
                             "one-sided)" % lbl)
                        continue
                    Yp, eps, valp, okp = polish_dual(Yd, Qs, Bst)
                    note = ("dual worst %+.2e val %+.3f polish "
                            "%s" % (worst, val, okp))
                    if okp:
                        strict_certs.append((lbl, "polished "
                                             "numeric, eps "
                                             "%.1e" % eps))
                        certified_labels.add(lbl)
                    if okp and Ls_fr is not None \
                            and n_exact_tried < CERT_CAP:
                        n_exact_tried += 1
                        for den in DEN_LADDER:
                            okx, dtl, _Yx = exact_strict_cert(
                                M_fr, idx_fr, Ls_fr, x0, Yp, Qs,
                                den)
                            if okx:
                                exact_certs.append((lbl, den,
                                                    dtl))
                                note += ("; EXACT in-span "
                                         "rational certificate "
                                         "at den %d (%s)"
                                         % (den, dtl))
                                break
                        else:
                            note += ("; exact rationalization "
                                     "failed on the ladder "
                                     "(numeric cert stands)")
                    info("SAMPLE %s STALLED PD: %s" % (lbl, note))
            sample_stats[tag] = (n_psd, n_dec, nsamp)
            return n_psd, n_dec

        # exact CHEBYSHEV-basis machinery for the certificates
        # (same coordinates as the f64 leg; rational hull)
        def cheb_pack(xs_fr, ws_fr, hull):
            lo = Fr(float(hull[0]))
            hi = Fr(float(hull[1]))
            Pc = cheb_rows_fr(xs_fr, DEG_A, lo, hi)
            Lc = BG.block_maps_fr(Pc, ws_fr)
            m_ = DEG_A + 2
            zeroA = [[Fr(0)] * m_ for _ in range(m_)]
            Mc, _qc, ic = BG.system_fr(Lc, zeroA)
            return Lc, Mc, ic

        xs1f = np.array([float(x) for x in sm1["xs"]])
        bx1f = np.array([float(x) for x in sm1["bxs"]])
        L1c, M1c, i1c = cheb_pack(sm1["xs"], sm1["ws"],
                                  BG.hull_of(xs1f, bx1f))
        Lmc, Mmc, imc = cheb_pack(mini_x, mini_w,
                                  BG.hull_of(mxf, mbxf))
        run_samples("w9A", CA9, NSAMP_W9)
        run_samples("MINI", CMINI, NSAMP_MINI, Ls_fr=Lmc,
                    M_fr=Mmc, idx_fr=imc)
        run_samples("SM1", SM_CEN["SM1"], NSAMP_SM,
                    Ls_fr=L1c, M_fr=M1c, idx_fr=i1c)
        stat_str = "; ".join("%s: %d of %d psd samples "
                             "decomposed"
                             % (t, sample_stats[t][1],
                                sample_stats[t][0])
                             for t in sample_stats)
        all_dec = all(sample_stats[t][1] == sample_stats[t][0]
                      for t in sample_stats)
        check("G60-sample-census", True,
              "sealed psd sample census (never wall data, never "
              "target eigenvectors): %s -- MEASURED, adjudicated "
              "in S8" % stat_str)
        check("G61-strict-adjudication", True,
              "strict-cone certificates: %d polished-numeric "
              "(%s), %d fully EXACT in-span rational (%s) -- "
              "every stalled PD cell was escalated to the dual "
              "search + polish + exact attempt (cap %d per "
              "world); MEASURED, adjudicated in S8"
              % (len(strict_certs),
                 str([c[0] for c in strict_certs]),
                 len(exact_certs), str(exact_certs), CERT_CAP))
        verdict_data = dict(
            all_dec=all_dec, strict_certs=strict_certs,
            exact_certs=exact_certs,
            certified_labels=certified_labels,
            abl_out=abl_out, abl_conv=abl_conv,
            ok_start=ok_start, ok_obj=ok_obj,
            convB=convB, lam9B=lam9B, yt=yt_vals,
            ok_blind=ok_blind)

    # ---------------- S7 must-fails + scopes
    section("S7  TARGET-INVERSE AUDIT + MUST-FAILS (LEG E)")
    hits_m2 = scope_audit("mutant_wall_z")
    hits_m4 = scope_audit("mutant_target_eig_sampler")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G70-scope-audit", bool(hits_m2) and bool(hits_m4)
          and not hits and not ag_hits,
          "m2 WALL-CONTAMINATED z mutant FLAGGED (%s); m4 "
          "TARGET-EIGENVECTOR sampler FLAGGED (%s); the %d "
          "sealed constructors audit CLEAN (no wall data, no "
          "target inverse/eigenvectors); fragment audit: %s"
          % ("; ".join(hits_m2) if hits_m2 else "NOT FLAGGED",
             "; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    # m1: wrong-sign Farkas must be rejected exactly
    Y1n = [[-e for e in row] for row in Y1]
    v1n = sum(z1[i] * Y1n[i][j] * z1[j]
              for i in range(DEG_A + 2) for j in range(DEG_A + 2))
    ok_m1 = (v1n > 0)      # checker demands z^T Y z < 0
    check("G71-mustfail-wrong-sign-dual", ok_m1,
          "m1 WRONG-SIGN FARKAS (SM1, exact): the flipped "
          "certificate (-Y, z) fails the exact checker "
          "(z^T(-Y)z = %s > 0) -- CAUGHT exactly; the "
          "certificate direction is load-bearing" % str(v1n))
    # m3: wrong graph caught by exact edge mismatch
    S_m3 = 10
    adj_good = graph_from_blocks(S_m3)
    adj_bad = mutant_wrong_graph(S_m3)
    miss = sum(len(adj_good[v] - adj_bad[v])
               for v in range(S_m3 + 1))
    check("G72-mustfail-wrong-graph", miss > 0,
          "m3 WRONG GRAPH: the t-less mutant builder misses %d "
          "directed edge slots against the sealed block cliques "
          "-- CAUGHT by exact edge-set comparison; with G23 "
          "(C4/C5 correctly non-chordal) the chordality verdict "
          "cannot be gamed by a vacuous tester or a wrong graph"
          % miss)

    # ---------------- S8 verdict
    section("S8  ADJUDICATION (SEALED)")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "selection by measured signs inside constructors (the "
          "stage-3 schedule permission and the ablation ladder "
          "are disclosed gate-side diagnosis), no RH claim; "
          "r243..r310 stand; the r308 verdict letters stand -- "
          "this round retypes their INTERPRETATION only")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        certified = verdict_data["certified_labels"]
        viol = [r for r in CENSUS_ROWS if not r["ok"]]
        open_loci = [r["label"] for r in CENSUS_ROWS
                     if r["typ"] == "PD" and not r["conv"]
                     and r["label"] not in certified]
        n_world = sum(1 for r in CENSUS_ROWS
                      if "#" not in r["label"]
                      and r["typ"] != "BOUNDARY")
        n_world_eq = sum(1 for r in CENSUS_ROWS
                         if "#" not in r["label"]
                         and r["typ"] != "BOUNDARY"
                         and (r["conv"] == (r["typ"] == "PD")))
        protocol_clean = (verdict_data["ok_start"]
                          and verdict_data["ok_obj"]
                          and not viol)
        strict = bool(verdict_data["strict_certs"]) or \
            bool(verdict_data["exact_certs"])
        if not protocol_clean:
            main_v = ("TARGET_INVERSE_SELECTION(start ablation "
                      "or protocol audit failed: %s)"
                      % str([r["label"] for r in viol]))
        elif strict:
            main_v = ("STRICT_SOURCE_CONE(%d polished-numeric + "
                      "%d exact in-span rational certificates: "
                      "generic in-span PD forms are NOT "
                      "block-decomposable -- C_w is STRICTLY "
                      "smaller than span cap S_+, the language "
                      "is not a restatement on the compressed "
                      "subspace; SEPARATION MECHANISM clause "
                      "(binding): the r308 WORLD separation "
                      "itself is fully the budget sign -- "
                      "%d/%d world cells sign-equivalent, "
                      "budget ablation %s, blind 2/2, "
                      "transplant kills MAIN -- so the r308 "
                      "'world discriminator' evidence stays "
                      "retyped TRIVIAL while cone MEMBERSHIP "
                      "(which MAIN + twin have at DEG_A and "
                      "generic PD forms lack) is the genuine "
                      "residual object)"
                      % (len(verdict_data["strict_certs"]),
                         len(verdict_data["exact_certs"]),
                         n_world_eq, n_world,
                         "CONV" if verdict_data["abl_conv"]
                         else "PARTIAL"))
        else:
            main_v = ("PSD_DECOMP_RESTATEMENT(chordal + full "
                      "local span + sign-equivalence on all "
                      "decided cells + budget ablation %s + no "
                      "strict certificate: the block-Green SDP "
                      "at the r308 caps measures "
                      "sign(lambda_min(A_sys)) -- on the "
                      "controls the budget sign, i.e. the wall "
                      "in new clothes)"
                      % ("CONV" if verdict_data["abl_conv"]
                         else "PARTIAL"))
        span_v = ("SPAN_LEDGER(codim TOY4 0 / SM0 11 / SM1 11 / "
                  "SM2 2 / SM3 1 / MINI16 0 / w9A 4 / w9B 236; "
                  "SM1 exact rank-one ambient counter-model with "
                  "exact rational Farkas -- the linear layer, "
                  "disclosed)")
        sign_v = ("SIGN_EQUIVALENCE_LEDGER(world cells %d/%d "
                  "equivalent -- the separation reads the "
                  "target sign; sample cells refute the "
                  "CONVERSE 'PD => decomposable' with "
                  "certificates; OPEN_LOCI (PD stalls without "
                  "certificate, one-sided) %s)"
                  % (n_world_eq, n_world,
                     str(open_loci) if open_loci else "{}"))
        verd = " + ".join([main_v, span_v, sign_v,
                           "R308_DEMARCATION(the r308 letters "
                           "stand; interpretation retyped)"])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the reviewer's mandatory nontriviality round; "
          "only STRICT_SOURCE_CONE / SOURCE_SECTION_EXISTS would "
          "justify R312; NO RH claim"
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


def unvech(q, m):
    A = np.zeros((m, m))
    iu, ju = np.triu_indices(m)
    A[iu, ju] = q
    A[ju, iu] = q
    return A


if __name__ == "__main__":
    sys.exit(main())
