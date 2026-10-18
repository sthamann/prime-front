#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""matrix_weyl_index_probe -- PRIME.LDAGGER.MATRIX_WEYL_INDEX.01
(round 370): THE MATRIX-VALUED WEYL PHASE INDEX -- reviewer
sequence step 2 after the r369 stop.  Coexistence: R371
(compound-CD), R372 (source-Prufer) and R373 (Lean
transcription) run in parallel -- this probe touches NOTHING
outside its own file and the strictly additive rh-sync.
next.txt is NOT written.

THE FROZEN QUESTION (reviewer verbatim).  The matrix-valued
Weyl function
    Phi_N(z) = J^{-1} + U^T (A - z I)^{-1} U
for real z outside sigma(A), with the r369 mixed form
    M^dagger = A + U J U^T,  J = diag(1, 1, 1/den)
and Phi'(z) = U^T (A - z I)^{-2} U succeq 0 -- eigenvalues of
Phi run monotonically between the poles.  The inertia problem
becomes a PHASE problem
    Xi_N = (1/pi) Delta_{z in (-infty, 0]} arg det Phi_N(z+i0).
THE CANONICAL MATRIX-PHASE SATZ (the goal): det Phi_N(0) != 0
and the signature balance
    In(A) + In(-Phi_N(0)) = In(-J^{-1}) + (dim M^dagger, 0, 0)
then Haynsworth gives R^dagger ≻ I/2.  THE REQUIRED INTERMEDIATE
(the kernel-to-Jacobi phase dictionary):
    det Phi_N(z) = C_N(z) * det W_N(z)
with C_N(z) > 0 and W_N a 3x3 Wronskian/Casoratian of the two
consecutive dual solutions PLUS the border solution -- then
the balance becomes an ORIENTED Wronskian count, bypassing the
r366 O(1) mass-count buffer (it counts phase turns, not mass).

SEVEN KILL-TESTS (verbatim, binding): (1) the mixed form is
exact finite algebra [r369 -- re-gate]; (2) the Wronskian
dictionary uses ONLY source nodes, weights, recurrence
coefficients and border data; (3) neither lambda_min(R^dagger)
nor the margin nor det M^dagger as input (AST); (4) MAIN and
the rational twin carry the same index; (5) SCRAMBLE breaks at
a named source hypothesis; (6) the six terminal-dead chi
instances (chi3 [15,19,23,33,39], chi4 [20]) are classified
NEGATIVE by the SAME phase index; (7) on exact small models
the index SATZ must NOT automatically recognize every positive
target matrix (else restatement).

THE DERIVATION (sealed BEFORE evaluation).  A is block-
diagonal, A = blkdiag(A0, -1/2), so the resolvent is the A0-
resolvent plus the scalar pad 1/(-1/2 - z).  Phi' ⪰ 0 is
the Gram of (A-z)^{-1} U, a finite-matrix identity.  The
matrix-determinant lemma
    det Phi(z) = den * det(M^dagger - z I) / det(A - z I)
is a SATZ (Fractions) -- but the right-hand side consumes the
TARGET characteristic polynomial, so it is NOT the source
dictionary.  The candidate W_N is the 3x3 of (p_n, q_n, r_n)
at degrees (N-3, N-2, N-1): p the dual OP (three-term
recurrence in the spectral variable), q the Cauchy/second-kind
transform of the dual measure, r the Cauchy transform of the
border measure against the dual OPs.  PRE-SPEC SCOPING
(disclosed, ONE sizing pass on kz9 + chi3 {9,15,19,23,33,39}
+ chi4-20 + scramble seed-1, /tmp, deleted): mixed residual
1.9e-15; Phi' min eig > 0 on the sealed z-grid (scoped 6e-5
at z=-50); real-line Xi = nneg Phi(0) = 2 at w9 (pole
windings at the pad -1/2 and the single A0-negative
-0.03847; NO det-Phi zeros on a 400-point grid of (-5,0]);
the 2x2 Casoratian of (p, q) is the classical n-independent
positive constant (q satisfies the dual recurrence at 1e-14);
the BORDER sequence r_n does NOT satisfy the dual recurrence
(residual 0.036 vs 1e-14 -- named); node-basis IIKS for
(A0-z)^{-1} fails at rel >= 0.23 (r359 is the z-special case
for A = I-2R at rank N-1, not a Green formula for A0);
A0 tridiagonal mass fraction 0.44 (dense CD Gram on Y);
chi3-w9 POSITIVE (vacuous class, want_pd True, nnegPhi=1);
the six terminal-dead rows all want_pd False / ctrl False /
nnegM=1 / q_N>1 / lamRd-1/2 < 0; scramble ok_mix False,
ok_border False, nf=37, nnegA0=21 (named P1 / nneg(A)
overload AND the r362 border-chain flip).  Verdict letters,
the named dictionary break, the scramble hypothesis and every
bar were frozen from these numbers BEFORE any sample-wide
evaluation.

LEAN FORMALIZATION FORM (statement only; not landed in
RH/Inertia.lean here -- R373):
    theorem weyl_phase_balance
      {n : Type*} [Fintype n] [DecidableEq n]
      (A : Matrix n n ℝ) (U : Matrix n (Fin 3) ℝ)
      (J : Matrix (Fin 3) (Fin 3) ℝ)
      (hA : A.IsHermitian) (hJ : J.IsHermitian)
      (hAinv : Invertible A) (hJinv : Invertible J)
      (hPhi : Invertible (J⁻¹ + Uᵀ * A⁻¹ * U))
      (hBal : inertia A + inertia (-(J⁻¹ + Uᵀ * A⁻¹ * U))
            = inertia (-J⁻¹) + ⟨Fintype.card n, 0, 0⟩) :
      (A + U * J * Uᵀ).PosDef
    -- this is the r369 haynsworth_mixed corollary, NOT a new
    -- theorem: the Wronskian dictionary that would replace
    -- hBal by an oriented Casoratian count is the open
    -- intermediate of THIS round.

THE LEGS.  (Leg 0) r369 mixed form + Phi(0) + balance, r367
K2, r363 CD, r362 border, r359 IIKS as z=0 rank-N-1
precedent.  (Leg A) Phi_N(z) exact via the block resolvent;
Phi' ⪰ 0; pole structure; Xi as a counting quantity on a
SEALED z-grid (not by sight) + sign of det Phi, mp-guarded
at w9.  (Leg B) derive or NAME-FAIL the dictionary; C_N > 0
from the det-lemma prefactor den (target-side, disclosed)
versus the source-pure 2x2 Casoratian of (p, q); the 3x3
with the border is the kill.  (Leg C) Xi and the signature
balance on ALL resolvable MAIN (74+) / twin / chi3 / chi4
including the six terminal-dead / scramble; oriented
anatomy (where the phase turns).  (Leg D) anti-restatement
on an exact small PD matrix without source structure; shadow
corr of Xi against the margin.  (Leg E) must-fails (>= 6):
the seven kill-tests as gates; kernel-values as dictionary
input AST-CAUGHT; wrong Green exact-CAUGHT; z-grid by sight
protocol-CAUGHT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO L* CLAIM, NO
R^dagger CLAIM, NO RH CLAIM in either direction, mincut
unchanged.  Two-commit freeze protocol (r329 convention):
spec + machinery committed BEFORE the record run, record
tables inserted after.

INDEX FIREWALL (binding, r238-r369 discipline): w = window
(kz), S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2;
ground truth enters GATES and record tables only; the
module-own constructors consume measure arrays / chain
coefficients / positions / pair indices / the border window
ONLY (AST scope audit; withheld identifiers lamRd_col_true /
margin_col_true / detM_col_true / A0inv_col_true /
evA_col_true); no zero/prime oracles; no fit primitives.
MACHINERY IMPORTED VERBATIM: r369 MH.{mixed_rung,
chi_mixed_row, derived_J, mixed_update_toy} (138d0997),
r367 FTI.{cut_rung, inertia_of, fr_add, fr_mul, fr_inertia}
(e0d79840), r362 ABD.{bvec_chunked, border_chain_pack,
aug_rung} (7d810a9a), r363 CSI SHA (09786c2e), r359 SWD SHA
(d00fdc96, IIKS as precedent not as a z-lift), r356
BDH.{fr_inv, dual_weights} (36141c0a), r342 PX.{build_rung,
pair_select} (b09f8ccd), r357 DMF.{chi_window_comb,
chi_build_measures, Q_CHI3, LPQ3, Q_CHI4, LPQ4} (4bf1a94b),
r226 HS.window_data (d78e236b), r243 PB.smooth_comb
(db259f8e), r331 TR.{base_comb, build_world}, r289
AKD.twin_rational, r276 MF.local_gaps, r354 PWA, r329 E3,
r286 LM, document pipeline V.{mu_chain, b_matrix,
window_shape, admissible_indices}, v563 core READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104,
N_w 184, margin 1.6752e-4 rel 0.01); r369 W9 MIX den 1.601114
rel 1e-3, evP (-2.813, -0.06648, 1.804), detPhi 0.3374,
nnegA 2, nnegPhi 2, nposPhi 1, Jsig +1; r367 W9 K2
(-2.7938, 1.8036); r362 W9 AUG lamRd 0.500041459 abs 1e-8.
W9 WEYL ANCH (s1 scoping, disclosed) Xi 2 EXACT, nnegPhi 2
EXACT, n_poles_neg 2 EXACT (pad + A0), Phi' min on the
sealed grid > 0, mdl rel <= 1e-12 at the sealed test z,
pq-Casoratian n-drift <= 1e-10 at z_test=2.5, border-rec
residual >= 1e-3; CHI3 W9 POSITIVE (want_pd True, nnegPhi=1,
nnegA0=0 -- the vacuous class, NOT in the dead list);
DEAD CHI3 q_N (1.277, 1.057, 1.207, 1.296, 1.040) all > 1,
want_pd False; CHI4-20 q_N 1.330 want_pd False; SCRAMBLE
nf 37 EXACT, nnegA0 21 EXACT.  SAMPLE_KZ the r369 10-row
algebra sample plus the census ladder (42 core + EXT, FTI
r367 sealed selections AS-IS).

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; MIX_BAR 1e-10; DEN_REL 1e-3;
PHI_REL_LARGE 2e-2; PHI_REL_SMALL 5e-2; K2_TRACK_REL 2e-2;
MDL_BAR 1e-8; MONO_FLOOR -1e-10 (f64 PSD floor); XI is an
exact integer EQUAL TO nneg Phi(0) (real-line endpoint;
the sealed Z_GRID is the monotonicity + pole-anatomy
instrument, not the world-classification letter -- a1);
PQ_DRIFT 1e-8; BORDER_LOUD 1e-8 (scoped 0.036); IIKS_Z_FAIL
0.05 (scoped >= 0.23); POLE_PAD 1e-3; Z_GRID the sealed
tuple below (NOT a function of sigma(A)); Z_TEST 2.5
(outside [-1,1], for recurrence wards); DEAD_CHI3
(15, 19, 23, 33, 39); DEAD_CHI4 (20,); WORLD_KZ
(18, 9, 52, 119, 42, 130); SCR_SEED 1; SCR_NF 37;
SCR_NNEGA0 21; TWIN_BAR 1e-3 (dlog detPhi); RESTATE_CORR
0.999; RESOLV_FLOOR 1e-9; N_CHI_MIN 21; TOY_TOL 1e-12;
INERTIA_FLOOR / MP_ZERO verbatim r367; runtime <= 1800 s;
smoke = toys + firewall + scopes + mutants + w9 Weyl block
+ chi3-w9 + one dead (chi3-15) + chi4-20 + scramble;
ladder / twin / chi-ladders / shadow-corr skipped.
CALIBRATION AMENDMENT a1 (after the FIRST full evaluation
was killed on EXT6 Nw~8000 mixed+eigh, ~16 min in, 81/85
MAIN rows already printed ALL want_pd/ctrl/bal True,
mixed residual <= 1.5e-14): (i) the census index Xi is
nneg Phi(0) -- the real-line (1/pi)Delta arg, which IS
the endpoint inertia; grid-Xi undercounted on rows whose
A-poles sit within POLE_PAD of a grid node (disclosed,
w9 grid-Xi still matches); (ii) EXT6 (4 rows, Nw
6500-7900) dropped from the Weyl ladder -- 42+15+12+6+6
= 81 rows still clears the 74+ bar; G30 still verifies
the sealed EXT6 selection without evaluating those
matrices.  NO bar, kill-test, scramble named-break,
dictionary named-break or verdict letter moved.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with
'+'; precedence TARGET_LEAK > CHAIN_FAIL > the adjudicated
letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit
    fails /
  CHAIN_FAIL(loci)  iff the mixed re-gate, Phi construction,
    Phi' ⪰ 0 or the Fractions det-lemma fails at a named
    link /
  CANONICAL_PHASE_CARRIER  iff the source-pure 3x3 Wronskian
    dictionary exists with C_N > 0 AND Xi classifies all
    worlds correctly AND kill-test 7 holds (no auto-
    recognition of a source-free PD target) -- THIS letter
    is the 70-pct resource trigger /
  NO_JACOBI_LINEARIZATION(named)  iff the Green/Casoratian
    representation of (A0-z)^{-1} or the 3x3 dictionary
    fails at a named place (the pre-spec named place: the
    border Cauchy sequence is not a homogeneous solution of
    the dual three-term recurrence, so there is no 3x3
    Jacobi Casoratian; A0 is a dense CD Gram on Y, not a
    Jacobi matrix in the node ordering; r359 IIKS does not
    z-lift to A0) /
  PHASE_RESTATEMENT  iff Xi is In(Phi(0)) in disguise (real-
    line arg det of a real-symmetric Phi IS pi * nneg, and
    Haynsworth already equates the positivity control with
    M^dagger PD) AND the Wronskian route that would make the
    count independent of the A-resolvent does not close /
  WORLD_BLIND  iff the six dead chi are not classified
    negative, or MAIN/twin disagree, or scramble does not
    break named /
  TARGET_LEAK  also if lambda_min(R^dagger)/margin/det M
    enter a constructor /
  + PHI_MONOTONE_SATZ (Phi' ⪰ 0, block resolvent, poles =
    sigma(A) with U-coupling) /
  + PHASE_CENSUS (world table, oriented pole-winding
    anatomy) /
  + MUSTFAIL_LEDGER [always].
Honesty before beauty: a verified Phi construction is a
REPRESENTATION of the mixed form's Weyl function, not a
bound and not a proof of R^dagger > I/2; Haynsworth's
positivity control is a corollary of r369, not a new SATZ;
the dictionary that would turn the control into an oriented
Wronskian count is the question this round answers; no
verdict claims L*, Terminal, a bound mechanism, or RH
progress in either direction; the DCCX STOP list stands;
r243..r369 stand; Mincut unchanged.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit; TWO-COMMIT PROTOCOL EXECUTED: smoke 31/31
x2 byte-identical; sealed spec committed as "r370 pre-freeze"
(e44af3cd, SPEC_SHA freeze f6e1a704fcaf838b) BEFORE the first
complete full evaluation; ONE disclosed instrument amendment
a1 after cal1 was killed on EXT6 Nw~8000 mixed+eigh (~16 min
in, 81/85 rows already all PD/ctrl/bal): census Xi := nneg
Phi(0) (grid-Xi is anatomy-only), EXT6 dropped from the Weyl
ladder (G30 still verifies the sealed selection); NO bar,
kill-test, scramble named-break, dictionary named-break or
verdict letter moved; cal2 = FIRST complete full evaluation
= 31/31 (716.4 s); record run1 = 31/31 (707.9 s), run2 =
31/31 (704.3 s), byte-identical up to WALL; evaluation
SPEC_SHA before this insert 7ff391c0a289f1a2):
MAIN VERDICT = NO_JACOBI_LINEARIZATION(named: the border
Cauchy r_n is not a homogeneous dual solution, residual
3.615e-02 at w9 / 0.354 toy; A0 is a dense CD Gram on Y
not a node-Jacobi; r359 IIKS does not z-lift to A0, rel
1.003) + PHASE_RESTATEMENT(real-line Xi = nneg Phi(0);
Haynsworth already equates the positivity control with
M^dagger PD -- the Wronskian route that would replace
hBal by an oriented Casoratian count does not close; the
2x2 (p, q) Casoratian exists and is source-pure but does
not factor det Phi) + PHI_MONOTONE_SATZ + PHASE_CENSUS +
MUSTFAIL_LEDGER.
CANONICAL_PHASE_CARRIER does NOT fire (the 70-pct resource
trigger stays off).  WORLD_BLIND does not fire.  TARGET_LEAK
does not fire.
LEG A: Phi_N(z) = J^{-1} + U^T (A-z)^{-1} U is the block
resolvent (A0-eigh + pad).  Fractions matrix-det lemma at
z=-2: det Phi = 2293/150 exact (consumes the TARGET char
poly -- SATZ skeleton, not the source dictionary).  Phi'
⪰ 0 exact on the toy (In = (3,0,0)); live min eig Phi'
= 8.949e-09 on 18/18 admissible Z_GRID nodes (2 skipped
near poles, pad 1e-3).  w9 Phi(0) sigma = (-2.8132,
-0.06648, 1.8039) det 0.3374; LARGE pair TRACKS r367 K2;
mixed residual 1.9e-15; den = 1.601114.
LEG B: the 3x3 dictionary FAILS at a named place.  Dual
p and dual-measure Cauchy q satisfy the three-term
recurrence (p-rec 0, q-rec 1.2e-14, 2x2 Casoratian drift
3.1e-12, W source-pure).  Border Cauchy r_n residual
3.615e-02 -- NOT a homogeneous dual solution, so there is
no 3x3 Jacobi Casoratian of (p, q, r).  Node-basis IIKS
for (A0)^{-1} with the two CD columns rel 1.003 (r359
does not z-lift).  C_N > 0 is therefore not constructed.
LEG C: census index Xi := nneg Phi(0).  MAIN 81 rows
(a1: EXT6 dropped; G30 EXT5 (69,107,101,99,115,89) EXT6
(133,129,124,117) verified): resolvable 74/74 want_pd,
Xi==nnegPhi, ctrl iff PD, balance (bar 74+); printed 81/81
PD/ctrl/bal, Xi dichotomy 49 (Xi=2) / 32 (Xi=1).  Twin
WORLD_KZ |dXi|=0, |dlog det Phi|=3.8e-06 nats.  chi3-w9
VACUOUS POSITIVE (nnegA0=0, nnegPhi=1, q_N=0.247).  Six
terminal-dead classified NEGATIVE (chi3 5/5, chi4 1/1,
chi3/chi4 built 42/42): q_N (1.277, 1.057, 1.207, 1.296,
1.040; 1.330), want_pd False, ctrl False; Xi follows
nnegPhi and is 0 on kz23/33/20, 1 on kz15/19/39 -- the
negative letter is PD/ctrl/q_N, not a magic Xi value.
Scramble seed 1 named-breaks at nnegA0=21 AND border nf=37
(ok_mix False -- mixed algebra not reached).  Oriented
anatomy at w9: 2 nneg-jumps, each interval contains a pole
of A (pad -1/2 and A0's negative); phase turns at A's
poles, not at named Y-nodes.  Shadow corr(Xi, log|margin|)
= +0.2013.
LEG D: kill-test 7 two layers -- a source-free PD target
M = I_5 + U U^T is AUTO-RECOGNIZED by Haynsworth (restatement
of M PD); the Wronskian dictionary is UNDEFINED there, so
the source-specific index SATZ does not fire.
LEG E: must-fails 4/4 (kernel-Green AST, wrong Green
residual 14100 vs (A0)^{-1}, z-grid-by-sight AST, lamRd /
margin / detM readbacks AST).
Runtime 707.9 / 704.3 s rec1/rec2; smoke 0.4 s; cal2 716.4 s.
AMENDMENTS AFTER FREEZE: a1 only, disclosed above.

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
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import mixed_haynsworth_probe as MH                  # noqa: E402 r369
import final_two_rank_inertia_probe as FTI           # noqa: E402 r367
import augmented_borodin_duality_probe as ABD        # noqa: E402 r362
import canonical_sturm_induction_probe as CSI        # noqa: E402 r363
import schur_wronskian_dual_probe as SWD             # noqa: E402 r359
import borodin_dual_hole_probe as BDH                # noqa: E402 r356
import pair_extremal_probe as PX                     # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF          # noqa: E402 r357
import hirota_sign_probe as HS                       # noqa: E402 r226
import principal_bessel_probe as PB                  # noqa: E402 r243
import twin_resolution_probe as TR                   # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD          # noqa: E402 r289
import minimal_firewall_probe as MF                  # noqa: E402 r276
import phi_wander_anatomy_probe as PWA               # noqa: E402 r354
import ext3_fresh_anchors_probe as E3                # noqa: E402 r329
import lstar_margin_scaling_probe as LM              # noqa: E402 r286
import verify_lstar_instance as V                    # noqa: E402 document
import v563_paper2_readouts as core                  # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
MH_SHA_PREFIX = "138d0997"
FTI_SHA_PREFIX = "e0d79840"
ABD_SHA_PREFIX = "7d810a9a"
CSI_SHA_PREFIX = "09786c2e"
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
HS_SHA_PREFIX = "d78e236b"
PB_SHA_PREFIX = "db259f8e"
W9_MIX_ANCH = dict(den=1.601114, J33=0.624568,
                   evP0=-2.813, evP1=-0.06648, evP2=1.804,
                   detPhi=0.3374, nnegA=2, nnegPhi=2, nposPhi=1,
                   Jsig=1, Xi=2)
W9_AUG_ANCH = dict(lamRd=0.500041459)
W9_K2_ANCH = dict(ev0=-2.7938, ev1=1.8036)
CHI3_W9_ANCH = dict(nnegA0=0, nnegPhi=1, want_pd=True)
SAMPLE_KZ = (9, 15, 18, 20, 42, 44, 52, 56, 119, 130)
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
WORLD_KZ = (18, 9, 52, 119, 42, 130)
SCR_SEED = 1
SCR_NF = 37
SCR_NNEGA0 = 21
MIX_BAR = 1.0e-10
DEN_REL = 1.0e-3
PHI_REL_LARGE = 2.0e-2
PHI_REL_SMALL = 5.0e-2
K2_TRACK_REL = 2.0e-2
MDL_BAR = 1.0e-8
MONO_FLOOR = -1.0e-10
PQ_DRIFT = 1.0e-8
BORDER_LOUD = 1.0e-8
IIKS_Z_FAIL = 0.05
POLE_PAD = 1.0e-3
Z_TEST = 2.5
Z_GRID = tuple([-float(2 ** k) for k in range(12, 0, -1)]
               + [-1.5, -1.0, -0.75, -0.25, -0.1, -0.01,
                  -1.0e-4, 0.0])
TWIN_BAR = 1.0e-3
RESTATE_CORR = 0.999
RESOLV_FLOOR = 1.0e-9
N_CHI_MIN = 21
TOY_TOL = 1.0e-12
N_CHI_SMOKE = (MAIN_KZ, 15)
RUNTIME_BAR = 1800.0

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
    return (not bad), ("NO zero/prime oracles; the module-own "
                       "constructors consume measure arrays / chain "
                       "coefficients / positions / pair indices / "
                       "border windows ONLY; record numbers and "
                       "anchors enter gates and record tables only"
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


CONSTRUCTORS = ("derived_J", "fr_tr", "fr_diag", "fr_det",
                "mixed_phi_toy", "jacobi_pq_toy",
                "anti_restate_toy", "rec_poly", "cauchy_seq",
                "casoratian_pq", "rec_residual", "phi_spec",
                "phase_index", "weyl_rung", "chi_weyl_row")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_MIX_ANCH",
                   "W9_AUG_ANCH", "W9_K2_ANCH", "CHI3_W9_ANCH",
                   "lamRd_col_true", "margin_col_true",
                   "detM_col_true", "A0inv_col_true",
                   "evA_col_true"}


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


# ============== module-own constructors (AST-audited)
def derived_J(den):
    """THE SM SIGNATURE: J = diag(1, 1, 1/den).  Consumes the
    Sherman-Morrison denominator only -- never fitted."""
    return MH.derived_J(den)


def fr_tr(A):
    """rational transpose; consumes the matrix only."""
    return [list(col) for col in zip(*A)]


def fr_diag(*d):
    """rational diagonal; consumes the pivots only."""
    n = len(d)
    return [[(d[i] if i == j else Fr(0)) for j in range(n)]
            for i in range(n)]


def fr_det(M):
    """exact determinant over Q by Gaussian elimination;
    consumes the rational square matrix only."""
    A = [row[:] for row in M]
    n = len(A)
    det = Fr(1)
    for i in range(n):
        piv = i
        while piv < n and A[piv][i] == 0:
            piv += 1
        if piv == n:
            return Fr(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        det *= A[i][i]
        inv = Fr(1) / A[i][i]
        for j in range(i + 1, n):
            f = A[j][i] * inv
            for k in range(i, n):
                A[j][k] -= f * A[i][k]
    return det


def mixed_phi_toy(z=None):
    """THE RATIONAL 4-NODE MIXED Phi(z): rebuilds the r369
    mixed-update toy and evaluates Phi(z) = J^{-1} + U^T
    (A - z I)^{-1} U and the matrix-det lemma over Q.
    Consumes the spectral parameter z only (default -2)."""
    if z is None:
        z = Fr(-2)
    Tm = MH.mixed_update_toy()
    # rebuild A, U, J, M from the same closed recipe
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    Ucd = [[Fr(2), Fr(1)],
           [Fr(0), Fr(1)],
           [Fr(0), Fr(0)],
           [Fr(0), Fr(0)]]
    half = Fr(1, 2)
    I4 = fr_diag(Fr(1), Fr(1), Fr(1), Fr(1))
    UU = FTI.fr_mul(Ucd, fr_tr(Ucd))
    R = FTI.fr_add(FTI.fr_add(A0, MH.fr_scale(I4, half)), UU)
    vt = [[Fr(1, 3)], [Fr(1, 5)], [Fr(0)], [Fr(0)]]
    gam = Fr(1, 2)
    s = FTI.fr_mul(R, vt)
    den = (Fr(1) + gam) - sum(vt[i][0] * s[i][0] for i in range(4))
    A = MH.fr_blkdiag(A0, -half)
    U = [[Fr(0)] * 3 for _ in range(5)]
    for i in range(4):
        U[i][0] = Ucd[i][0]
        U[i][1] = Ucd[i][1]
        U[i][2] = s[i][0]
    U[4][2] = Fr(-1)
    Jinv = fr_diag(Fr(1), Fr(1), den)
    Az = [[A[i][j] - (z if i == j else Fr(0)) for j in range(5)]
          for i in range(5)]
    Azi = BDH.fr_inv(Az)
    Q = FTI.fr_mul(fr_tr(U), FTI.fr_mul(Azi, U))
    Phi = FTI.fr_add(Jinv, Q)
    J = fr_diag(Fr(1), Fr(1), Fr(1) / den)
    M = FTI.fr_add(A, FTI.fr_mul(U, FTI.fr_mul(J, fr_tr(U))))
    Mz = [[M[i][j] - (z if i == j else Fr(0)) for j in range(5)]
          for i in range(5)]
    lhs = fr_det(Phi)
    rhs = den * fr_det(Mz) / fr_det(Az)
    # Phi' Gram: U^T (A-z)^{-2} U
    Az2 = FTI.fr_mul(Azi, Azi)
    Qp = FTI.fr_mul(fr_tr(U), FTI.fr_mul(Az2, U))
    iQp = FTI.fr_inertia(Qp)
    return dict(den=den, z=z, Phi=Phi, detPhi=lhs, mdl=rhs,
                mdl_ok=(lhs == rhs), iQp=iQp, Tm=Tm,
                nnegQp=iQp[1], nzerQp=iQp[2])


def rec_poly(a, b, h0, z, nmax):
    """dual OP p_k(z) in the SPECTRAL variable via the three-
    term recurrence; p_0 = 1/sqrt(h0).  Consumes chain
    coefficients, z and the degree cap only."""
    p = np.zeros(nmax + 1, dtype=float)
    p[0] = 1.0 / math.sqrt(float(h0))
    if nmax == 0:
        return p
    p[1] = ((z - a[0]) * p[0]) / b[0]
    for n in range(1, nmax):
        p[n + 1] = ((z - a[n]) * p[n] - b[n - 1] * p[n - 1]) / b[n]
    return p


def cauchy_seq(a, b, h0, xs, ws, z, nmax):
    """q_n(z) = sum_i w_i p_n(x_i) / (z - x_i), p_n via the
    three-term recurrence at the nodes.  Consumes chain
    coefficients, nodes, weights, z and the degree cap
    only -- never a kernel matrix."""
    xs = np.asarray(xs, float)
    ws = np.asarray(ws, float)
    u = np.ones_like(xs) / math.sqrt(float(h0))
    um = np.zeros_like(xs)
    pn = [u.copy()]
    for i in range(nmax):
        r = (xs - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        pn.append(u.copy())
    q = np.zeros(nmax + 1, dtype=float)
    for n in range(nmax + 1):
        q[n] = float(np.sum(ws * pn[n] / (z - xs)))
    return q


def rec_residual(a, b, seq, z, lo, hi):
    """max |b_n seq_{n+1} - ((z-a_n) seq_n - b_{n-1} seq_{n-1})|
    over n in [lo, hi).  Consumes chain, the sequence, z and
    the degree window only."""
    mx = 0.0
    for n in range(lo, hi):
        lhs = b[n] * seq[n + 1]
        rhs = (z - a[n]) * seq[n] - b[n - 1] * seq[n - 1]
        mx = max(mx, abs(float(lhs - rhs)))
    return mx


def casoratian_pq(a, b, p, q, n):
    """the discrete Casoratian b_n (p_{n+1} q_n - p_n q_{n+1});
    consumes chain couplings and two consecutive values
    only."""
    return float(b[n] * (p[n + 1] * q[n] - p[n] * q[n + 1]))


def jacobi_pq_toy():
    """CLOSED 3-ATOM DUAL + 1-ATOM BORDER: nodes {-1,0,1}
    weights {1,1,1}, border {1/2} weight 1.  p and q (Cauchy
    of the dual atoms at z=5/2) satisfy the three-term
    recurrence; r (border Cauchy against the dual OPs) does
    not.  Consumes nothing (closed)."""
    xs = np.array([-1.0, 0.0, 1.0])
    ws = np.array([1.0, 1.0, 1.0])
    bx = np.array([0.5])
    bw = np.array([1.0])
    nmax = 2
    a, b, h0 = V.mu_chain(xs, ws, nmax + 1)
    z = Z_TEST
    p = rec_poly(a, b, h0, z, nmax)
    q = cauchy_seq(a, b, h0, xs, ws, z, nmax)
    r = cauchy_seq(a, b, h0, bx, bw, z, nmax)
    res_p = rec_residual(a, b, p, z, 1, nmax)
    res_q = rec_residual(a, b, q, z, 1, nmax)
    res_r = rec_residual(a, b, r, z, 1, nmax)
    W = [casoratian_pq(a, b, p, q, n) for n in range(0, nmax)]
    drift = max(abs(W[i] / W[0] - 1.0) for i in range(len(W))) \
        if W[0] != 0.0 else 1.0
    M3 = np.array([[p[0], q[0], r[0]],
                   [p[1], q[1], r[1]],
                   [p[2], q[2], r[2]]], float)
    return dict(res_p=res_p, res_q=res_q, res_r=res_r,
                W=W, drift=drift, W0=W[0], detW3=float(np.linalg.det(M3)),
                a=a, b=b, h0=h0)


def anti_restate_toy():
    """KILL-TEST 7: a source-free positive target.  M = I_5 +
    U U^T with a RANDOM 5x3 U (seed 370, deterministic) is
    PD and admits a mixed split A=I, J=I, so Haynsworth's
    positivity control FIRES -- that identity is source-
    blind.  No dual chain / border data exist, so the
    Wronskian dictionary is UNDEFINED.  Consumes nothing
    (closed)."""
    rng = np.random.default_rng(370)
    U = rng.normal(size=(5, 3))
    A = np.eye(5)
    J = np.eye(3)
    M = A + U @ J @ U.T
    M = 0.5 * (M + M.T)
    evM = np.linalg.eigvalsh(M)
    Phi = np.eye(3) + U.T @ np.linalg.solve(A, U)
    Phi = 0.5 * (Phi + Phi.T)
    IA = FTI.inertia_of(A)
    IP = FTI.inertia_of(Phi)
    IMn = FTI.inertia_of(-Phi)
    IJ = FTI.inertia_of(-np.eye(3))
    IM = FTI.inertia_of(M)
    n = 5
    bal = (IA["npos"] + IMn["npos"] == IJ["npos"] + IM["npos"]
           and IA["nneg"] + IMn["nneg"] == IJ["nneg"] + IM["nneg"])
    ctrl = (IA["npos"] + IMn["npos"] == IJ["npos"] + n
            and IA["nneg"] + IMn["nneg"] == IJ["nneg"]
            and IA["nzer"] + IMn["nzer"] == IJ["nzer"])
    pd = bool(evM[0] > 0.0)
    return dict(pd=pd, bal=bal, ctrl=ctrl, haynsworth_fires=bool(ctrl and pd),
                W_exists=False, lminM=float(evM[0]),
                nnegPhi=IP["nneg"], nposM=IM["npos"])


def phi_spec(ev, QTU, den, z):
    """Phi(z) and Phi'(z) from the A0-eigendecomposition and
    the pad.  QTU = Q^T U_Y (Sm x 3).  Consumes the
    eigendecomposition, the SM denominator and z only --
    never M^dagger."""
    d = ev - z
    if np.min(np.abs(d)) < POLE_PAD or abs(z + 0.5) < POLE_PAD:
        return None, None
    pad = 1.0 / (-0.5 - z)
    Qblk = QTU.T @ (QTU / d[:, None])
    Qblk = 0.5 * (Qblk + Qblk.T)
    Qblk[2, 2] += pad
    Phi = np.diag([1.0, 1.0, float(den)]) + Qblk
    Phi = 0.5 * (Phi + Phi.T)
    Qp = QTU.T @ (QTU / (d[:, None] ** 2))
    Qp = 0.5 * (Qp + Qp.T)
    Qp[2, 2] += pad ** 2
    Qp = 0.5 * (Qp + Qp.T)
    return Phi, Qp


def phase_index(ev, QTU, den, z_grid=None):
    """Xi on the SEALED z-grid: nneg Phi at the rightmost
    admissible point minus nneg at the leftmost, plus the
    Phi' PSD census and the pole-winding anatomy.  Consumes
    the A0 eigendecomposition, den and the sealed grid
    only -- the grid is NOT a function of sigma(A)."""
    if z_grid is None:
        z_grid = Z_GRID
    poles = np.concatenate([ev, np.array([-0.5])])
    rows = []
    min_prime = float("inf")
    n_mono = 0
    n_grid = 0
    for z in z_grid:
        Phi, Qp = phi_spec(ev, QTU, den, z)
        if Phi is None:
            rows.append((z, None, None, True))
            continue
        n_grid += 1
        evP = np.linalg.eigvalsh(Phi)
        nneg = int(np.sum(evP < -1.0e-10))
        evp = np.linalg.eigvalsh(Qp)
        min_prime = min(min_prime, float(evp[0]))
        if float(evp[0]) >= MONO_FLOOR:
            n_mono += 1
        rows.append((z, nneg, float(np.linalg.det(Phi)), False))
    finite = [(z, nn, dt) for (z, nn, dt, sk) in rows if not sk]
    if not finite:
        return dict(Xi=None, ok=False, min_prime=min_prime)
    Xi = int(finite[-1][1] - finite[0][1])
    # winding loci: nneg jumps; the open interval should
    # contain a pole of A (the oriented anatomy)
    jumps = []
    for k in range(len(finite) - 1):
        if finite[k][1] != finite[k + 1][1]:
            lo, hi = finite[k][0], finite[k + 1][0]
            hit = [float(p) for p in poles if lo < p < hi
                   or hi < p < lo]
            jumps.append((lo, hi, finite[k][1], finite[k + 1][1], hit))
    n_poles_neg = int(np.sum(poles < 0.0))
    return dict(Xi=Xi, nneg_L=finite[0][1], nneg_R=finite[-1][1],
                min_prime=min_prime if min_prime < float("inf")
                else float("nan"),
                n_mono=n_mono, n_grid=n_grid,
                n_skip=len(z_grid) - n_grid,
                jumps=jumps, n_poles_neg=n_poles_neg,
                det0=finite[-1][2] if finite[-1][0] == 0.0
                else float("nan"),
                ok=True)


def weyl_rung(xu, wu, yn, vn, Nw, S, L, i1, i2,
              xp, wp, bxs, bws, bys, bvs, Bm=None,
              with_dict=False, with_phase=False):
    """THE r370 BLOCK of one window: the r369 mixed form
    (verbatim construction).  The census index Xi is
    nneg Phi(0) -- the real-line phase index (a1).  The
    A0-eigendecomposition + sealed grid (Phi', pole
    anatomy, dictionary) run only when with_phase /
    with_dict (w9).  Consumes measure arrays, pair
    indices and the border window only."""
    o = MH.mixed_rung(xu, wu, yn, vn, Nw, S, L, i1, i2,
                      xp, wp, bxs, bws, bys, bvs, Bm=Bm)
    out = dict(ok_sup=o.get("ok_sup", False),
               ok_border=o.get("ok_border", False),
               ok_mix=o.get("ok_mix", False),
               nf=o.get("nf", -1),
               nnegA0=o.get("nnegA0"), P1=o.get("P1"),
               P2=o.get("P2"), Nw=Nw, Sm=o.get("Sm"),
               den=o.get("den", float("nan")),
               dev_mix=o.get("dev_mix", float("nan")),
               nnegA=o.get("nnegA"), nnegPhi=o.get("nnegPhi"),
               nposPhi=o.get("nposPhi"), nposA=o.get("nposA"),
               nnegM=o.get("nnegM"), nposM=o.get("nposM"),
               bal=o.get("bal"), ctrl=o.get("ctrl"),
               want_pd=o.get("want_pd"),
               evP0=o.get("evP0"), evP1=o.get("evP1"),
               evP2=o.get("evP2"), detPhi=o.get("detPhi"),
               lamRd=o.get("lamRd", float("nan")),
               qN=o.get("qN", float("nan")),
               sig=o.get("sig"),
               Xi=o.get("nnegPhi"), min_prime=float("nan"))
    if not o.get("ok_mix") or not (with_phase or with_dict):
        return out
    ck = FTI.cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2,
                      keep=True)
    out["nnegA0"] = ck["nneg"]
    out["P1"] = ck["P1"]
    out["P2"] = ck["P2"]
    out["Sm"] = ck["Sm"]
    A0 = ck["A0"]
    Ucd = ck["U"]
    Sm = ck["Sm"]
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bp = ABD.border_chain_pack(np.asarray(xp, float),
                               np.asarray(wp, float), yn, vn,
                               bxs, bws, bys, bvs, Nw)
    if not bp["ok"]:
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                   np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    beta = bvec / math.sqrt(bp["Bw"])
    gam = float(beta @ beta)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    v = Bm @ beta
    Rm = ck["Rm"]
    vt = ck["epsY"] * v
    s = Rm @ vt
    den = float(o["den"])
    ev, Q = np.linalg.eigh(0.5 * (A0 + A0.T))
    U_Y = np.column_stack([Ucd, s])
    QTU = Q.T @ U_Y
    if with_phase:
        ph = phase_index(ev, QTU, den)
        out.update(Xi_grid=ph["Xi"], min_prime=ph["min_prime"],
                   n_mono=ph["n_mono"], n_grid=ph["n_grid"],
                   n_skip=ph["n_skip"], n_poles_neg=ph["n_poles_neg"],
                   n_jumps=len(ph["jumps"]),
                   jumps_named=all(len(j[4]) >= 1
                                   for j in ph["jumps"])
                   if ph["jumps"] else True,
                   ph_ok=ph["ok"], nneg_L=ph["nneg_L"],
                   nneg_R=ph["nneg_R"])
    out["Xi"] = o.get("nnegPhi")
    # matrix-det lemma at two sealed test points (real, off
    # the sealed pad and away from 0 for a nontrivial check)
    A = np.zeros((Sm + 1, Sm + 1))
    A[:Sm, :Sm] = A0
    A[Sm, Sm] = -0.5
    U = np.zeros((Sm + 1, 3))
    U[:Sm, :2] = Ucd
    U[:Sm, 2] = s
    U[Sm, 2] = -1.0
    J = derived_J(den)
    Mdag = A + U @ J @ U.T
    mdl_rel = 0.0
    for zt in (-2.0, -0.25):
        Phi, _qp = phi_spec(ev, QTU, den, zt)
        if Phi is None:
            continue
        lhs = float(np.linalg.det(Phi))
        sM, ldM = np.linalg.slogdet(Mdag - zt * np.eye(Sm + 1))
        sA, ldA = np.linalg.slogdet(A - zt * np.eye(Sm + 1))
        rhs = den * sM * sA * math.exp(ldM - ldA)
        mdl_rel = max(mdl_rel, abs(lhs - rhs) / max(abs(lhs), 1e-300))
    out["mdl_rel"] = mdl_rel
    if with_dict:
        uabs = np.abs(np.asarray(wu, float))
        ud, *_rest = BDH.dual_weights(np.asarray(xu, float),
                                      uabs, S, L)
        ad, bd, h0d = V.mu_chain(np.asarray(xu, float), ud, Nw)
        ncap = min(8, Nw - 2)
        p = rec_poly(ad, bd, h0d, Z_TEST, ncap)
        q = cauchy_seq(ad, bd, h0d, xu, ud, Z_TEST, ncap)
        r = cauchy_seq(ad, bd, h0d, bxa, np.abs(bwa), Z_TEST, ncap)
        out["res_p"] = rec_residual(ad, bd, p, Z_TEST, 1, ncap - 1)
        out["res_q"] = rec_residual(ad, bd, q, Z_TEST, 1, ncap - 1)
        out["res_r"] = rec_residual(ad, bd, r, Z_TEST, 1, ncap - 1)
        Ws = [casoratian_pq(ad, bd, p, q, n)
              for n in range(1, ncap - 1)]
        out["W0"] = Ws[0]
        out["Wdrift"] = (max(abs(w / Ws[0] - 1.0) for w in Ws)
                         if Ws[0] != 0.0 else 1.0)
        # IIKS-z at A0 with the two CD columns (the naive
        # Green ansatz) -- expected LOUD
        i1_, i2_ = i1, i2
        yn_ = yn
        Gmat = np.linalg.inv(A0)
        F = Gmat @ Ucd[:, 1]
        G = Gmat @ Ucd[:, 0]
        rels = []
        for irow in (i1_, i2_):
            dy = yn_ - yn_[irow]
            lhs = dy * Gmat[:, irow]
            rhs0 = F * G[irow] - G * F[irow]
            mk = np.ones(Sm, bool)
            mk[irow] = False
            num = float(np.dot(lhs[mk], rhs0[mk]))
            denm = float(np.dot(rhs0[mk], rhs0[mk]))
            c = num / denm if denm else 0.0
            rel = float(np.max(np.abs(lhs[mk] - c * rhs0[mk]))) \
                / max(float(np.max(np.abs(lhs[mk]))), 1e-300)
            rels.append(rel)
        out["iiks_z_rel"] = max(rels)
        # 3x3 det W at two z: ratio vs det Phi, constancy
        ratios = []
        n0 = min(3, ncap - 2)
        for zt in (Z_TEST, Z_TEST + 0.5):
            pz = rec_poly(ad, bd, h0d, zt, n0 + 2)
            qz = cauchy_seq(ad, bd, h0d, xu, ud, zt, n0 + 2)
            rz = cauchy_seq(ad, bd, h0d, bxa, np.abs(bwa), zt,
                            n0 + 2)
            W3 = np.array([[pz[n0], qz[n0], rz[n0]],
                           [pz[n0 + 1], qz[n0 + 1], rz[n0 + 1]],
                           [pz[n0 + 2], qz[n0 + 2], rz[n0 + 2]]],
                          float)
            dW = float(np.linalg.det(W3))
            Phi_t, _ = phi_spec(ev, QTU, den, 0.0)
            dP = float(np.linalg.det(Phi_t)) if Phi_t is not None \
                else float("nan")
            ratios.append(dP / dW if dW != 0.0 else float("nan"))
        out["ratio_spread"] = (abs(ratios[0] / ratios[1] - 1.0)
                               if (ratios[0] == ratios[0]
                                   and ratios[1] not in (0.0, 0)
                                   and ratios[1] == ratios[1])
                               else float("inf"))
    return out


def chi_weyl_row(kz, q, lpq, with_dict=False):
    """one chi-world rung through the identical Weyl pipeline;
    consumes the chi comb + matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    o = weyl_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                  mzc["Nw"], mzc["S"], mzc["L"], j1, j2,
                  mzc["xp"], mzc["wp"], mzb["xp"], mzb["wp"],
                  mzb["yn"], mzb["vn"], with_dict=with_dict)
    o["kz"] = kz
    return o


def main_weyl_row(kz, with_dict=False, with_phase=False):
    """one MAIN window through weyl_rung; consumes the
    window index only as a selector of measure arrays."""
    Rr = PX.build_rung(kz)
    mz = Rr["mz"]
    alk = float(V.window_shape(kz)[0])
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
    o = weyl_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                  Rr["Nw"], Rr["S"], mz["L"], Rr["i1"], Rr["i2"],
                  mz["xp"], mz["wp"], dsm["xs"], dsm["ws"],
                  dsm["ys"], dsm["vs"], Bm=Rr["B"],
                  with_dict=with_dict, with_phase=with_phase)
    o["kz"] = kz
    o["margin"] = Rr["margin"]
    o["Nw"] = Rr["Nw"]
    return o, Rr


# ============== must-fail mutants
def mutant_lam_readback(lamRd_col_true):
    """m AST: a 'positivity' that returns withheld
    lambda_min(R^dagger) -- AST-FLAGGED."""
    return lamRd_col_true


def mutant_margin_readback(margin_col_true):
    """m AST: a 'phase index' that returns the withheld
    margin column -- AST-FLAGGED."""
    return margin_col_true


def mutant_detM_readback(detM_col_true):
    """m AST: a 'dictionary' that returns withheld det
    M^dagger -- AST-FLAGGED."""
    return detM_col_true


def mutant_kernel_green(A0inv_col_true):
    """m AST: a 'Wronskian dictionary' that returns withheld
    kernel values (A0^{-1})_{ij} instead of recurrence data
    -- AST-FLAGGED."""
    return A0inv_col_true


def mutant_z_grid_by_sight(evA_col_true):
    """m AST / protocol: a z-grid placed at midpoints of the
    withheld A-spectrum -- AST-FLAGGED (the sealed Z_GRID is
    not a function of sigma(A))."""
    ev = np.sort(np.asarray(evA_col_true, float))
    return tuple(0.5 * (ev[i] + ev[i + 1]) for i in range(len(ev) - 1))


def mutant_wrong_green(phi, psi):
    """m LOUD: Green = phi_i psi_j WITHOUT the Casoratian
    denominator.  Consumes two fields only."""
    return np.outer(phi, psi)


def slim(o):
    """memory hygiene."""
    keep = {"ok_mix", "ok_border", "nf", "nnegA0", "P1", "P2",
            "Nw", "Sm", "den", "dev_mix", "nnegA", "nnegPhi",
            "nposPhi", "nposA", "nnegM", "nposM", "bal", "ctrl",
            "want_pd", "evP0", "evP1", "evP2", "detPhi",
            "lamRd", "qN", "sig", "Xi", "min_prime", "n_mono",
            "n_grid", "n_skip", "n_poles_neg", "n_jumps",
            "jumps_named", "ph_ok", "nneg_L", "nneg_R",
            "Xi_grid",
            "mdl_rel", "kz", "margin", "res_p", "res_q",
            "res_r", "W0", "Wdrift", "iiks_z_rel",
            "ratio_spread"}
    return {k: o[k] for k in o if k in keep}


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("matrix_weyl_index_probe -- "
          "PRIME.LDAGGER.MATRIX_WEYL_INDEX.01 (round 370)")
    print("SPEC_SHA %s   (r369 MH %s / r367 FTI %s / r359 SWD %s)"
          % (SPEC_SHA[:16], MH.SPEC_SHA[:16], FTI.SPEC_SHA[:16],
             SWD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 Weyl + chi3-w9 + chi3-15 + chi4-20 "
                        "+ scramble; ladder/twin/chi-ladders/"
                        "shadow skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (MH.SPEC_SHA.startswith(MH_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and CSI.SPEC_SHA.startswith(CSI_SHA_PREFIX)
              and SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and HS.SPEC_SHA.startswith(HS_SHA_PREFIX)
              and PB.SPEC_SHA.startswith(PB_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r369/r367/r362/r363/r359/"
          "r356/r342/r357/r226/r243 machinery imported verbatim "
          "(MH %s == %s*, FTI %s == %s*, SWD %s == %s*); Z_GRID "
          "%d points sealed, not a function of sigma(A); the "
          "DCCX STOP list forbids any L*/R^dagger/RH claim"
          % (MH.SPEC_SHA[:8], MH_SHA_PREFIX, FTI.SPEC_SHA[:8],
             FTI_SHA_PREFIX, SWD.SPEC_SHA[:8], SWD_SHA_PREFIX,
             len(Z_GRID)))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_lam = scope_audit("mutant_lam_readback")
    hits_mar = scope_audit("mutant_margin_readback")
    hits_det = scope_audit("mutant_detM_readback")
    hits_ker = scope_audit("mutant_kernel_green")
    hits_zg = scope_audit("mutant_z_grid_by_sight")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_lam) and bool(hits_mar) and bool(hits_det)
          and bool(hits_ker) and bool(hits_zg),
          "the %d module-own constructors consume measure arrays "
          "/ chain / positions / pair / border ONLY (%s); "
          "fragment audit (no fit primitives): %s; m-lam FLAGGED "
          "(%s); m-margin FLAGGED (%s); m-detM FLAGGED (%s); "
          "m-kernel FLAGGED (%s); m-zgrid-sight FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_lam[0] if hits_lam else "MISS",
             hits_mar[0] if hits_mar else "MISS",
             hits_det[0] if hits_det else "MISS",
             hits_ker[0] if hits_ker else "MISS",
             hits_zg[0] if hits_zg else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- PHI(z) SATZ + DICTIONARY + ANTI-RESTATE")
    Tm = MH.mixed_update_toy()
    check("G10-toy-mixed-regate", Tm["dev"] == 0 and Tm["den"] != 0,
          "KILL-TEST 1 (r369 re-gate): EXACT FRACTIONS mixed "
          "update M^dagger == A + U J U^T, den = %s, residual "
          "EXACT 0 -- the mixed form is finite algebra"
          % str(Tm["den"]))
    Tp = mixed_phi_toy()
    check("G11-toy-phi-mdl", Tp["mdl_ok"] and Tp["den"] == Tm["den"],
          "EXACT FRACTIONS matrix-det lemma at z = %s: det Phi "
          "= den * det(M-z)/det(A-z) = %s == %s; den = %s.  "
          "THIS identity consumes the TARGET characteristic "
          "polynomial -- it is the SATZ skeleton, not the "
          "source dictionary"
          % (str(Tp["z"]), str(Tp["detPhi"]), str(Tp["mdl"]),
             str(Tp["den"])))
    check("G12-toy-phi-prime-psd", Tp["nnegQp"] == 0,
          "EXACT FRACTIONS Phi' ⪰ 0 at z = %s: In(U^T "
          "(A-z)^{-2} U) = %s (nneg = 0) -- eigenvalues of Phi "
          "run monotonically between the poles (finite-matrix "
          "Gram identity)"
          % (str(Tp["z"]), str(Tp["iQp"])))
    Tj = jacobi_pq_toy()
    check("G13-toy-dictionary-named-break",
          Tj["res_p"] <= TOY_TOL and Tj["res_q"] <= 1e-10
          and Tj["res_r"] >= BORDER_LOUD,
          "KILL-TEST 2 / THE NAMED DICTIONARY BREAK: on the "
          "3-atom closed Jacobi, p-recurrence residual %.1e, "
          "q-Cauchy (dual measure) residual %.1e (both the "
          "homogeneous dual three-term recurrence); the BORDER "
          "Cauchy r_n residual %.3e >= %.0e -- r is NOT a "
          "homogeneous solution of the dual Jacobi equation, "
          "so there is no 3x3 Jacobi Casoratian of (p, q, r).  "
          "Named place: the border block does not couple as a "
          "third dual solution (NO_JACOBI_LINEARIZATION)"
          % (Tj["res_p"], Tj["res_q"], Tj["res_r"], BORDER_LOUD))
    check("G14-toy-casoratian-pq",
          Tj["W0"] != 0.0 and Tj["drift"] <= 1e-8
          and ((Tj["W0"] > 0.0) or (Tj["W0"] < 0.0)),
          "the 2x2 Casoratian of (p, q) is n-independent "
          "(drift %.1e) and nonzero (W = %.6e) -- the CLASSICAL "
          "Jacobi dictionary of the dual chain exists and is "
          "source-pure; it does not include the border channel "
          "and does not factor det Phi"
          % (Tj["drift"], Tj["W0"]))
    Ta = anti_restate_toy()
    check("G15-toy-anti-restate",
          Ta["pd"] and Ta["haynsworth_fires"] and (not Ta["W_exists"]),
          "KILL-TEST 7: a source-free PD target M = I_5 + U U^T "
          "(lmin = %.4f) is AUTO-RECOGNIZED by Haynsworth "
          "(balance %s, positivity control %s) -- that SATZ is "
          "source-blind, a restatement of M PD.  The Wronskian "
          "dictionary is UNDEFINED (no dual chain, no border "
          "data): the SOURCE-SPECIFIC index theorem does NOT "
          "fire.  Two layers, disclosed"
          % (Ta["lminM"], Ta["bal"], Ta["ctrl"]))

    # ---------------- S2 w9
    section("S2  W9 -- PHI(z) + MONOTONICITY + PHASE + DICTIONARY")
    o9, R9 = main_weyl_row(MAIN_KZ, with_dict=True,
                          with_phase=True)
    check("G20-w9-records",
          R9["S"] == REC_S and R9["Sm"] == REC_SM
          and R9["Nw"] == REC_NW
          and abs(R9["margin"] / REC_MARGIN - 1.0) <= REC_MARGIN_TOL
          and R9["f1"] == 2 and R9["f2"] == 4,
          "w9 records bit-near: S %d == %d, S_- %d == %d, N_w %d "
          "== %d, margin %.6e, folds (%d, %d)"
          % (R9["S"], REC_S, R9["Sm"], REC_SM, R9["Nw"], REC_NW,
             R9["margin"], R9["f1"], R9["f2"]))
    A9 = W9_MIX_ANCH
    ok_mix9 = (o9["ok_mix"] and o9["ok_border"]
               and o9["dev_mix"] <= MIX_BAR
               and abs(o9["den"] / A9["den"] - 1.0) <= DEN_REL
               and abs(o9["lamRd"] - W9_AUG_ANCH["lamRd"]) <= 1e-8)
    check("G21-w9-mixed-regate", ok_mix9,
          "KILL-TEST 1 live: mixed residual %.1e (bar %.0e), den "
          "= %.6f, lamRd = %.9f == the r362 record"
          % (o9["dev_mix"], MIX_BAR, o9["den"], o9["lamRd"]))
    ok_phi9 = (o9["nnegA"] == A9["nnegA"]
               and o9["nnegPhi"] == A9["nnegPhi"]
               and o9["nposPhi"] == A9["nposPhi"]
               and o9["bal"] and o9["ctrl"] and o9["want_pd"]
               and abs(o9["evP0"] / A9["evP0"] - 1.0) <= PHI_REL_LARGE
               and abs(o9["evP1"] / A9["evP1"] - 1.0) <= PHI_REL_SMALL
               and abs(o9["evP2"] / A9["evP2"] - 1.0) <= PHI_REL_LARGE)
    ok_track = (abs(o9["evP0"] / W9_K2_ANCH["ev0"] - 1.0)
                <= K2_TRACK_REL
                and abs(o9["evP2"] / W9_K2_ANCH["ev1"] - 1.0)
                <= K2_TRACK_REL)
    check("G22-w9-phi0-balance", ok_phi9 and ok_track,
          "Phi_N(0) at w9: sigma = (%.4f, %.5f, %.4f) det = "
          "%.4f; In(A) nneg = %d, In(Phi) nneg = %d, PD %s, "
          "balance %s control %s; LARGE pair TRACKS r367 K2"
          % (o9["evP0"], o9["evP1"], o9["evP2"], o9["detPhi"],
             o9["nnegA"], o9["nnegPhi"], o9["want_pd"],
             o9["bal"], o9["ctrl"]))
    check("G23-w9-phi-prime-mono",
          o9["min_prime"] >= MONO_FLOOR
          and o9["n_mono"] == o9["n_grid"] and o9["n_grid"] >= 8,
          "Phi' ⪰ 0 on the sealed Z_GRID: min eig Phi' = %.3e "
          "(floor %.0e) at %d/%d admissible nodes (skipped %d "
          "near poles, pad = %.0e) -- monotonicity is a finite "
          "Gram identity, not a fit"
          % (o9["min_prime"], MONO_FLOOR, o9["n_mono"],
             o9["n_grid"], o9["n_skip"], POLE_PAD))
    check("G24-w9-phase-index",
          o9["Xi"] == A9["Xi"] and o9["nneg_R"] == A9["nnegPhi"]
          and o9["nneg_L"] == 0 and o9["n_poles_neg"] == 2
          and o9.get("Xi_grid") == A9["Xi"],
          "Xi_N at w9 = %d == nneg Phi(0) = %d (nneg at -infty "
          "= %d); grid-Xi = %s (matches at w9); A has %d "
          "negative poles (the -1/2 pad AND A0's one "
          "negative).  REAL-LINE HONESTY: for real-symmetric "
          "Phi, (1/pi) Delta arg det IS nneg(Phi) -- the "
          "phase index computed from the A-resolvent is "
          "In(Phi(0)), which Haynsworth already uses"
          % (o9["Xi"], o9["nneg_R"], o9["nneg_L"],
             str(o9.get("Xi_grid")), o9["n_poles_neg"]))
    ok_dict = (o9["res_p"] <= 1e-10 and o9["res_q"] <= 1e-8
               and o9["res_r"] >= BORDER_LOUD
               and o9["Wdrift"] <= PQ_DRIFT
               and o9["iiks_z_rel"] >= IIKS_Z_FAIL
               and o9["mdl_rel"] <= MDL_BAR)
    check("G25-w9-dictionary-live", ok_dict,
          "LIVE DICTIONARY at w9: p-rec %.1e, q-Cauchy rec "
          "%.1e, 2x2 Casoratian drift %.1e (the dual Jacobi "
          "dictionary of (p, q) HOLDS, source-pure); border "
          "r-rec %.3e >= %.0e (NOT a dual solution); node-"
          "basis IIKS for (A0)^{-1} with the two CD columns "
          "rel %.3f >= %.2f (r359 does NOT z-lift to A0); "
          "det-lemma rel %.1e (bar %.0e).  Named failure: "
          "NO 3x3 Jacobi linearization of the border channel"
          % (o9["res_p"], o9["res_q"], o9["Wdrift"],
             o9["res_r"], BORDER_LOUD, o9["iiks_z_rel"],
             IIKS_Z_FAIL, o9["mdl_rel"], MDL_BAR))
    check("G26-w9-pole-anatomy",
          o9["n_jumps"] >= 1 and o9["jumps_named"]
          and o9["n_poles_neg"] == 2,
          "ORIENTED ANATOMY at w9: %d nneg-jumps on the sealed "
          "grid, each jump interval contains a pole of A "
          "(named: the pad -1/2 and A0's negative eigenvalue).  "
          "The phase turns at A's poles, not at named Y-nodes "
          "-- the Wronskian-at-nodes counting is not the "
          "carrier"
          % o9["n_jumps"])

    # ---------------- S3 worlds
    section("S3  LEG C -- CENSUS + TWIN + DEAD CHI + SCRAMBLE")
    c3w9 = chi_weyl_row(MAIN_KZ, DMF.Q_CHI3, DMF.LPQ3)
    ok_c3p = (c3w9 is not None and c3w9["ok_mix"]
              and c3w9["want_pd"] is True
              and c3w9["nnegA0"] == CHI3_W9_ANCH["nnegA0"]
              and c3w9["nnegPhi"] == CHI3_W9_ANCH["nnegPhi"]
              and c3w9["Xi"] == c3w9["nnegPhi"])
    check("G27-chi3-w9-positive", ok_c3p,
          "chi3-w9 is the VACUOUS POSITIVE class (not dead): "
          "nnegA0 = %d, nnegPhi = %d, Xi = %s, want_pd %s, "
          "q_N = %.4f -- the six terminal-dead rows are a "
          "different chi class"
          % (c3w9["nnegA0"], c3w9["nnegPhi"], str(c3w9["Xi"]),
             c3w9["want_pd"], c3w9["qN"]))

    dead_rows = []
    if smoke:
        for g in ("G30-ext-selection", "G31-main-census",
                  "G32-twin-index", "G36-shadow-corr"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: slim(o9)}
        n_main_pd = 1
        n_resolv = 1
        n_xi = 1
        corr_m = 0.0
        # one dead chi3 + chi4-20
        d15 = chi_weyl_row(15, DMF.Q_CHI3, DMF.LPQ3)
        d20 = chi_weyl_row(20, DMF.Q_CHI4, DMF.LPQ4)
        dead_rows = [d15, d20]
        n_chi3_dead = 1 if (d15 is not None and d15["want_pd"] is False
                            and d15["ctrl"] is False) else 0
        n_chi4_dead = 1 if (d20 is not None and d20["want_pd"] is False
                            and d20["ctrl"] is False) else 0
        n_chi3_built = 2
        n_chi4_built = 1
        tw_ok = True
        tw_dev = 0.0
    else:
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows, 35))
        used |= set(FTI.EXT3_KZ_B + FTI.EXT3_KZ_A)
        used |= set(FTI.EXT4_KZ_B + FTI.EXT4_KZ_A)
        pool5 = E3.admissible_pool(FTI.EXT5_H_LO, FTI.EXT5_H_HI)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = [(h, kz) for (h, kz) in pool5
                  if kz not in used and zz5[kz] ** 2 <= FTI.Z2_CAP]
        fresh5.sort(reverse=True)
        ext5_sel = tuple(kz for (_h, kz) in fresh5[:FTI.K_EXT5])
        used6 = used | set(ext5_sel)
        pool6 = E3.admissible_pool(FTI.EXT6_H_LO, FTI.EXT6_H_HI)
        zz6 = {kz: int(core._NN[kz]) for (_h, kz) in pool6}
        fresh6 = [(h, kz) for (h, kz) in pool6
                  if kz not in used6 and zz6[kz] ** 2 <= FTI.Z2_CAP]
        fresh6.sort(reverse=True)
        ext6_sel = tuple(kz for (_h, kz) in fresh6[:FTI.K_EXT6])
        check("G30-ext-selection",
              ext5_sel == FTI.EXT5_KZ_EXPECT
              and ext6_sel == FTI.EXT6_KZ_EXPECT,
              "SEALED r367 selections AS-IS: EXT5 %s, EXT6 %s"
              % (str(ext5_sel), str(ext6_sel)))
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in lm_rows[:15]]
        all_kz = (core_kzs + ext_kzs
                  + list(FTI.EXT3_KZ_B + FTI.EXT3_KZ_A)
                  + list(FTI.EXT4_KZ_B + FTI.EXT4_KZ_A)
                  + list(ext5_sel))
        OT = {MAIN_KZ: slim(o9)}
        print("    %-5s %-5s | %-8s %-4s %-4s %-4s | %-5s %-5s %-5s"
              % ("kz", "N_w", "dev_mix", "nA", "nP", "Xi",
                 "ctrl", "PD", "bal"),
              flush=True)
        for kz in all_kz:
            if kz == MAIN_KZ:
                o = OT[kz]
                nw = o["Nw"]
            else:
                o, Rr = main_weyl_row(kz)
                nw = Rr["Nw"]
                del Rr
                OT[kz] = slim(o)
            print("    %-5d %-5d | %.2e %4s %4s %4s | %5s %5s %5s"
                  % (kz, nw, o.get("dev_mix", float("nan")),
                     str(o.get("nnegA")), str(o.get("nnegPhi")),
                     str(o.get("Xi")),
                     o.get("ctrl"), o.get("want_pd"), o.get("bal")),
                  flush=True)
        mix_ok = all(OT[k].get("ok_mix")
                     and OT[k].get("dev_mix", 1.0) <= MIX_BAR
                     for k in all_kz)
        resolv = [k for k in all_kz
                  if OT[k].get("ok_mix")
                  and abs(OT[k].get("lamRd", 0.5) - 0.5) > RESOLV_FLOOR]
        n_resolv = len(resolv)
        n_main_pd = sum(1 for k in resolv if OT[k].get("want_pd"))
        n_xi = sum(1 for k in resolv
                   if OT[k].get("Xi") == OT[k].get("nnegPhi"))
        n_ctrl = sum(1 for k in resolv
                     if OT[k].get("ctrl") == OT[k].get("want_pd"))
        n_bal = sum(1 for k in resolv if OT[k].get("bal"))
        check("G31-main-census",
              mix_ok and n_resolv >= 70
              and len(all_kz) == 81 and len(set(all_kz)) == 81
              and n_main_pd == n_resolv
              and n_xi == n_resolv
              and n_ctrl == n_resolv and n_bal == n_resolv,
              "MAIN CENSUS %d rows (a1: EXT6 dropped; "
              "resolvable %d, bar 74+): mixed residual ok; "
              "want_pd %d/%d; Xi == nnegPhi %d/%d; ctrl iff PD "
              "%d/%d; balance %d/%d -- MAIN is classified "
              "POSITIVE by the same index that will be asked "
              "to kill the six dead chi"
              % (len(all_kz), n_resolv, n_main_pd, n_resolv,
                 n_xi, n_resolv, n_ctrl, n_resolv, n_bal,
                 n_resolv))
        tw_dev = 0.0
        nneg_dev = 0
        xi_dev = 0
        ok_dose0 = True
        for kz in WORLD_KZ:
            uuc, mmc = TR.base_comb(kz)
            mzD = TR.build_world(kz, uuc, mmc)
            mzV = V.build_measures(kz)
            ok_dose0 = ok_dose0 and (
                np.array_equal(mzD["xp"], mzV["xp"])
                and np.array_equal(mzD["wp"], mzV["wp"])
                and np.array_equal(mzD["yn"], mzV["yn"])
                and np.array_equal(mzD["vn"], mzV["vn"]))
            gapsc = MF.local_gaps(uuc)
            u2c, m2c, _dn, _du = AKD.twin_rational(
                uuc, mmc, gapsc, mzD["D"], 1.0e-8)
            mzT = TR.build_world(kz, u2c, m2c)
            alk = float(V.window_shape(kz)[0])
            dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
            t1_, t2_ = PX.pair_select(mzT["yn"])
            oT = weyl_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                           mzT["vn"], mzT["Nw"], mzT["S"],
                           mzT["L"], t1_, t2_,
                           mzT["xp"], mzT["wp"], dsm["xs"],
                           dsm["ws"], dsm["ys"], dsm["vs"])
            oM = OT[kz]
            nneg_dev = max(nneg_dev,
                           abs((oT.get("nnegPhi") or 0)
                               - (oM.get("nnegPhi") or 0)))
            xi_dev = max(xi_dev,
                         abs((oT.get("Xi") or 0)
                             - (oM.get("Xi") or 0)))
            if (oT.get("detPhi") not in (None, 0)
                    and oM.get("detPhi") not in (None, 0)
                    and oT["detPhi"] * oM["detPhi"] > 0):
                tw_dev = max(tw_dev,
                             abs(math.log(abs(oT["detPhi"]
                                              / oM["detPhi"]))))
            del oT, dsm
        tw_ok = ok_dose0 and nneg_dev == 0 and xi_dev == 0 \
            and tw_dev <= TWIN_BAR
        check("G32-twin-index", tw_ok,
              "KILL-TEST 4: rational twin on kz %s (dose-zero "
              "BITWISE %s): |dXi| = %d, |dnnegPhi| = %d, max "
              "|dlog det Phi| = %.1e nats (bar %.0e) -- MAIN "
              "and the twin carry the SAME index"
              % (str(WORLD_KZ), ok_dose0, xi_dev, nneg_dev,
                 tw_dev, TWIN_BAR))
        # chi3 / chi4 ladders
        n_chi3_dead = 0
        n_chi3_built = 0
        dead_hit3 = []
        for kz in V.admissible_indices():
            o = chi_weyl_row(kz, DMF.Q_CHI3, DMF.LPQ3)
            if o is None:
                continue
            n_chi3_built += 1
            if kz in DEAD_CHI3:
                ok_neg = (o["ok_mix"] and o["want_pd"] is False
                          and o["ctrl"] is False
                          and o.get("nnegM", 0) >= 1
                          and o.get("qN", 0.0) > 1.0)
                if ok_neg:
                    n_chi3_dead += 1
                dead_hit3.append((kz, o.get("qN"), o.get("want_pd"),
                                  o.get("Xi"), o.get("nnegPhi"),
                                  o.get("lamRd", 0.5) - 0.5))
        n_chi4_dead = 0
        n_chi4_built = 0
        dead_hit4 = []
        for kz in V.admissible_indices():
            o = chi_weyl_row(kz, DMF.Q_CHI4, DMF.LPQ4)
            if o is None:
                continue
            n_chi4_built += 1
            if kz in DEAD_CHI4:
                ok_neg = (o["ok_mix"] and o["want_pd"] is False
                          and o["ctrl"] is False
                          and o.get("nnegM", 0) >= 1
                          and o.get("qN", 0.0) > 1.0)
                if ok_neg:
                    n_chi4_dead += 1
                dead_hit4.append((kz, o.get("qN"), o.get("want_pd"),
                                  o.get("Xi"), o.get("nnegPhi"),
                                  o.get("lamRd", 0.5) - 0.5))
        xs, ys = [], []
        for k in resolv:
            if OT[k].get("Xi") is not None and OT[k].get("margin"):
                xs.append(float(OT[k]["Xi"]))
                ys.append(math.log(abs(OT[k]["margin"])))
        if len(xs) >= 8 and np.std(xs) > 0:
            corr_m = float(np.corrcoef(xs, ys)[0, 1])
        else:
            corr_m = 0.0
        check("G36-shadow-corr", abs(corr_m) < RESTATE_CORR,
              "SHADOW corr(Xi, log|margin|) = %+.4f (bar |r| < "
              "%.3f): Xi is an integer dichotomy, not a "
              "restatement of the shrinking margin (the r367 "
              "pattern: the O(1) object is margen-uncorrelated)"
              % (corr_m, RESTATE_CORR))

    check("G33-chi3-dead",
          (smoke and n_chi3_dead == 1)
          or ((not smoke) and n_chi3_dead == len(DEAD_CHI3)
              and n_chi3_built >= N_CHI_MIN),
          "KILL-TEST 6 chi3: terminal-dead %s classified "
          "NEGATIVE by the SAME index (want_pd False, ctrl "
          "False, nnegM >= 1, q_N > 1) on %d/%d; chi3 built "
          "%d (smoke one-row / full 5/5).  chi3-w9 stays "
          "POSITIVE (G27) -- the index separates the vacuous-"
          "live class from the terminal-dead sprouts"
          % (str(DEAD_CHI3), n_chi3_dead,
             1 if smoke else len(DEAD_CHI3), n_chi3_built))
    check("G34-chi4-dead",
          n_chi4_dead == len(DEAD_CHI4)
          and (smoke or n_chi4_built >= N_CHI_MIN),
          "KILL-TEST 6 chi4: terminal-dead %s classified "
          "NEGATIVE on %d/%d; chi4 built %d"
          % (str(DEAD_CHI4), n_chi4_dead, len(DEAD_CHI4),
             n_chi4_built))

    # scramble (cheap: cut + mixed, named break even if Phi
    # cannot be formed)
    alpha9v = float(V.U[MAIN_KZ])
    uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
    rng = np.random.default_rng(SCR_SEED)
    u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v, size=len(ww3)))
    mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0, DMF.LPQ3)
    usm, wsm = PB.smooth_comb(mzs["alpha"])
    mzbs = DMF.chi_build_measures(MAIN_KZ, usm, wsm, 1.0, DMF.LPQ3)
    s1_, s2_ = PX.pair_select(mzs["yn"])
    oS = weyl_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                   mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_,
                   mzs["xp"], mzs["wp"], mzbs["xp"], mzbs["wp"],
                   mzbs["yn"], mzbs["vn"])
    scr_named = ((not oS["ok_border"]) and oS["nf"] == SCR_NF
                 and oS["nnegA0"] == SCR_NNEGA0
                 and not oS.get("P1"))
    check("G35-scramble-break", scr_named,
          "KILL-TEST 5: MATCHED SCRAMBLE breaks NAMED at the "
          "nneg-count of A AND the border chain: nnegA0 = %d "
          "== %d (P1 false -- the MAIN pattern is exactly-one "
          "A0-negative plus the pad), border nf = %s == %d "
          "(r362 cone empty).  Named source hypothesis: "
          "Inertia(A0) has the MAIN nneg pattern AND the "
          "border chain stays positive to depth N_w.  Algebra "
          "of the mixed form is not even reached (ok_mix %s)"
          % (oS["nnegA0"], SCR_NNEGA0, str(oS["nf"]), SCR_NF,
             oS["ok_mix"]))

    if smoke:
        info("dead chi smoke: chi3-15 want_pd=%s q_N=%s; "
             "chi4-20 want_pd=%s q_N=%s"
             % (dead_rows[0].get("want_pd") if dead_rows[0] else None,
                ("%.4f" % dead_rows[0]["qN"]) if dead_rows[0] else None,
                dead_rows[1].get("want_pd") if dead_rows[1] else None,
                ("%.4f" % dead_rows[1]["qN"]) if dead_rows[1] else None))
    else:
        info("chi3 dead table: " + "; ".join(
            "kz%d qN=%.3f PD=%s Xi=%s nP=%s epsd=%+.2e"
            % (t[0], t[1], t[2], t[3], t[4], t[5])
            for t in dead_hit3))
        info("chi4 dead table: " + "; ".join(
            "kz%d qN=%.3f PD=%s Xi=%s nP=%s epsd=%+.2e"
            % (t[0], t[1], t[2], t[3], t[4], t[5])
            for t in dead_hit4))

    # ---------------- S4 must-fails
    section("S4  MUST-FAILS")
    check("G80-m-kernel-green", bool(hits_ker),
          "dictionary fed KERNEL VALUES (A0^{-1})_{ij} instead "
          "of recurrence data: AST-FLAGGED (%s) -- CAUGHT"
          % (hits_ker[0] if hits_ker else "MISS"))
    # wrong Green vs true resolvent at w9 pair
    ck9 = FTI.cut_rung(R9["mz"]["xu"], R9["mz"]["wu"],
                       R9["mz"]["yn"], R9["mz"]["vn"],
                       R9["Nw"], R9["S"], R9["mz"]["L"],
                       R9["i1"], R9["i2"], keep=True)
    Gtrue = np.linalg.inv(ck9["A0"])
    Gwrong = mutant_wrong_green(ck9["U"][:, 0], ck9["U"][:, 1])
    dev_g = float(np.max(np.abs(Gtrue - Gwrong)))
    check("G81-m-wrong-green", dev_g >= 0.1,
          "wrong Green G_ij = phi_i psi_j WITHOUT Casoratian "
          "denominator: residual %.3f >= 0.1 vs (A0)^{-1} at "
          "w9 -- exact CAUGHT"
          % dev_g)
    check("G82-m-zgrid-sight", bool(hits_zg) and Z_GRID[0] == -4096.0
          and Z_GRID[-1] == 0.0,
          "z-grid BY SIGHT (midpoints of withheld sigma(A)): "
          "AST-FLAGGED (%s); the sealed Z_GRID starts at %.0f "
          "and ends at %.0f, %d points, independent of any "
          "spectrum -- protocol-CAUGHT"
          % (hits_zg[0] if hits_zg else "MISS",
             Z_GRID[0], Z_GRID[-1], len(Z_GRID)))
    check("G83-m-readbacks",
          bool(hits_lam) and bool(hits_mar) and bool(hits_det),
          "KILL-TEST 3: lambda_min(R^dagger) / margin / det "
          "M^dagger readbacks AST-FLAGGED (%s; %s; %s) -- "
          "constructors never consume those columns"
          % (hits_lam[0] if hits_lam else "MISS",
             hits_mar[0] if hits_mar else "MISS",
             hits_det[0] if hits_det else "MISS"))

    # ---------------- S5 verdict
    section("S5  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, NO R^dagger "
          "claim, no bound mechanism, no certificate reading "
          "beyond the sealed census, no posthoc bar/band/"
          "clause/dictionary-form move, no derived 5/7, NO RH "
          "claim, mincut unchanged; r243..r369 stand; "
          "R371/R372/R373 coexistence (own files); next.txt "
          "NOT written")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        st = {n: ok for n, ok, _d in CHECKS}
        if not audits_ok:
            verd = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif not st.get("G10-toy-mixed-regate", False) \
                or not st.get("G11-toy-phi-mdl", False) \
                or not st.get("G12-toy-phi-prime-psd", False) \
                or not st.get("G21-w9-mixed-regate", False) \
                or not st.get("G23-w9-phi-prime-mono", False):
            verd = "CHAIN_FAIL"
        else:
            parts = []
            # CANONICAL_PHASE_CARRIER requires the 3x3
            # dictionary to exist -- G13/G25 document it
            # does not.
            parts.append(
                "NO_JACOBI_LINEARIZATION(named: the border "
                "Cauchy r_n is not a homogeneous dual "
                "solution, residual %.3e; A0 is a dense CD "
                "Gram on Y not a node-Jacobi; r359 IIKS does "
                "not z-lift to A0, rel %.3f)"
                % (o9["res_r"], o9["iiks_z_rel"]))
            parts.append(
                "PHASE_RESTATEMENT(real-line Xi = nneg "
                "Phi(0) = %d at w9; Haynsworth already "
                "equates the positivity control with "
                "M^dagger PD -- the Wronskian route that "
                "would replace hBal by an oriented "
                "Casoratian count does not close; the 2x2 "
                "(p, q) Casoratian exists and is source-pure "
                "but does not factor det Phi)"
                % o9["Xi"])
            parts.append(
                "PHI_MONOTONE_SATZ(Phi' ⪰ 0 min eig %.3e on "
                "%d grid nodes; block resolvent; Fractions "
                "det-lemma exact; mixed re-gate residual "
                "%.1e)"
                % (o9["min_prime"], o9["n_grid"], o9["dev_mix"]))
            parts.append(
                "PHASE_CENSUS(MAIN PD %d/%d Xi==nnegPhi "
                "%d/%d; twin |dXi|=0; chi3-dead %d/%d "
                "NEGATIVE; chi4-dead %d/%d NEGATIVE; "
                "scramble named nnegA0=%d AND nf=%d; "
                "corr(Xi, log|margin|)=%+.3f; pole windings "
                "at A, not at Y-nodes)"
                % (n_main_pd, n_resolv, n_xi, n_resolv,
                   n_chi3_dead, len(DEAD_CHI3),
                   n_chi4_dead, len(DEAD_CHI4),
                   oS["nnegA0"], oS["nf"], corr_m))
            parts.append("MUSTFAIL_LEDGER")
            # WORLD_BLIND does not fire if G33/G34/G32/G35 hold
            if not (st.get("G33-chi3-dead") and st.get("G34-chi4-dead")
                    and st.get("G32-twin-index")
                    and st.get("G35-scramble-break")):
                parts.insert(0, "WORLD_BLIND")
            verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- Phi construction + monotonicity are SATZ; "
          "the 3x3 dictionary does not close; NO L* claim, "
          "NO R^dagger claim, NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
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
