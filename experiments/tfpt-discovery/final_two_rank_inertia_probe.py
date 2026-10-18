#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""final_two_rank_inertia_probe --
PRIME.LSTAR.DUAL.FINAL_TWO_RANK_INERTIA.01 (round 367): THE
HAYNSWORTH TWO-RANK CUT -- G1 (edge-gap) and G2 (rest positivity)
are not proved, they are BYPASSED.  Coexistence: R365 (V2), R366
(Edge-Gap-MS) and R368 (L2-T1) run in parallel -- this probe
touches NOTHING outside its own file and the strictly additive
rh-sync.  The r363 finding 'the lambda_min gap is a terminal-rank
phenomenon (n_cross at N_w-1 / N_w-2)' is consumed as a FEATURE:
only the measured final two-rank transition is evaluated.

THE THEOREM (Haynsworth, finite algebra).  On Y with the dual CD
restrictions R_n (the r363 SATZ R_{n+1} = R_n + v v^T):
    A0 = R_{N-3} - (1/2) I,
    U  = [u_{N-3}, u_{N-2}]   (the two last dual OP columns on Y),
    K2 = I_2 + U^T A0^{-1} U.
Let H = [[A0, U], [U^T, -I_2]].  Haynsworth additivity (A0
invertible) gives
    Inertia(H) = Inertia(A0) + Inertia(-K2)
               = Inertia(-I_2) + Inertia(A0 + U U^T).
Hence the two arithmetic premises
    (P1) Inertia(A0) = (|Y|-1, 1, 0)   [exactly ONE negative
         direction]
    (P2) det K2 < 0                     [K2 has mixed signs, so
         Inertia(-K2) = (1, 1, 0)]
force Inertia(A0 + U U^T) = (|Y|, 0, 0), i.e.
    R_{N-1} - (1/2) I = A0 + U U^T  ≻  0.
Only P1 and P2 contain arithmetic; the implication is a finite
matrix identity (Lean-shaped; formalization form below).  The
implication is ONE-WAY: chi3-w9 already has A0 ≻ 0 and det K2 > 0
while M ≻ 0 (Loewner), so the premises are sufficient not
necessary.

AST FIREWALL (binding): K2 is built ONLY from the two CD columns
and A0^{-1}.  No target readback of det(R_{N-1}), lambda_min(R),
or the margin (m1).  The matrix-determinant lemma
    det(A0 + U U^T) = det(A0) det(K2)
is a WARD of the constructor, never a definition of K2.

LEAN FORMALIZATION FORM (not proved here; the finite identity
to land in RH/Inertia.lean on promotion):
    theorem haynsworth_two_rank
      {n : ℕ} (hn : n ≥ 1)
      (A0 : Matrix (Fin n) (Fin n) ℝ) (hSym : A0.IsHermitian)
      (U : Matrix (Fin n) (Fin 2) ℝ) (hInv : Invertible A0)
      (hP1 : inertia A0 = ⟨n - 1, 1, 0⟩)
      (hP2 : ((1 : Matrix _ _ ℝ) + Uᵀ * A0⁻¹ * U).det < 0) :
      (A0 + U * Uᵀ).PosDef
    -- from Haynsworth: Inertia [[A,B],[Bᵀ,C]]
    --   = Inertia A + Inertia (C - Bᵀ A⁻¹ B)  (A invertible),
    -- applied twice (C = -I_2 and C-Schur = A0 + U Uᵀ).
    -- For 2x2, det K2 < 0 already IS Inertia(K2) = ⟨1,1,0⟩
    -- (no zeros).  Proof language: LDL / Sylvester over ℝ,
    -- Fractions-exact on the rational toy (this probe G10).

THE LEGS.  (Leg 0) anchors bit-near: r363 CD-update identity and
n_cross columns, r356/r359/r362 (R, Schur, R†), the Sol /tmp
pilot reproduced (kz9/18/44/52).  (Leg A) Haynsworth as finite
algebra (Fractions LDL on the 4-node toy) + exact U from the
dual OP columns via the r363 CD-update (no target readback).
(Leg B) full census of P1 and P2 on ALL 85 MAIN + 84 chi + Twin
+ Scramble; sealed bars; mp-arbitration of near-zero eigenvalues
of A0 (the deep rows); scramble MUST break a NAMED premise;
structure of the negative A0-direction (pair vs rest -- the r359
binding-thesis connection); is det K2 < 0 world-separating?
(Leg C) the source functional -det K2 over the ladder: sealed
fit (-det K2 ≥ c N^{-β}? β = 0 / 1 / 3.332); decomposition into
source quantities (OP columns CD-computable, A0^{-1} via the
resolvent); concordance vs margin / r'_det / lam_rest (G2-rest
of A0); the shadow test -- IF restatement, type INERTIA_RESTATEMENT
honestly (the gain is then the Lean form, not new information).
(Leg D) the R† lift: two-rank gives unaugmented R_{N-1} ≻ 1/2 I;
r362 (A5)+(A7) lifts by q† < 1.  Direct cut on R†: three-rank
Y-block A0 + U3 U3^T with U3 = [u_{N-3}, u_{N-2}, w_SM] and
K3 = I_3 + U3^T A0^{-1} U3 (Inertia(K3) = (2,1,0) + det K3 < 0);
the elegant one-shot L† close would need the FULL (Sm+1) matrix
-- both variants measured on the sealed RANK_KZ set (budget).
(Leg E) must-fails (≥5): (m1) K2 from det R_{N-1} readback ->
AST-CAUGHT; (m2) wrong bordered sign (+I_2) -> exact CAUGHT;
(m3) U not from the CD columns -> CAUGHT; (m4) inertia with
wrong tolerance -> PROTOCOL-CAUGHT; (m5) Haynsworth with swapped
premises -> exact CAUGHT on the toy.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in
either direction, mincut unchanged.  Two-commit freeze protocol
(r329 convention): spec + machinery committed BEFORE the record
run, record tables inserted after.

INDEX FIREWALL (binding, r238-r363 discipline): w = window (kz),
S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds = grid
indices; ground truth enters GATES and record tables only; the
module-own constructors consume measure arrays / chain
coefficients / positions / pair indices / (Leg D) the border
window ONLY (AST scope audit; withheld identifiers
detR_col_true / detM_col_true and the REC/anchor constants); no
zero/prime oracles (AST firewall); no fit primitives beyond the
imported r286 Theil-Sen (fragment audit).  MACHINERY IMPORTED
VERBATIM: r363 CSI.{cd_last_update} (09786c2e), r359
SWD.schur_rung (d00fdc96), r356 BDH.{dual_weights, dual_rung,
fr_inv, fr_proj, psi_fit57} (36141c0a), r362 ABD.{aug_rung,
bvec_chunked, border_chain_pack} (7d810a9a), r342 PX.{build_rung,
pair_select} (b09f8ccd), r357 DMF.{chi_window_comb,
chi_build_measures, LPQ3, LPQ4, Q_CHI3, Q_CHI4} (4bf1a94b),
r354 PWA.rung_reduced_cols (f9db84da), r329 E3.{admissible_pool,
used_kz_set} (bbfaf199), r286 LM.{ts_fit, ext_rule} (0a44ac4e),
r331 TR.{base_comb, build_world}, r289 AKD.twin_rational,
r276 MF.local_gaps, r226 HS.window_data, r243 PB.smooth_comb,
document pipeline V.{build_measures, mu_chain, b_matrix,
admissible_indices, U, PP}, v563 core READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104,
N_w 184, margin 1.6752e-4 rel 0.01, lambda_min(R) 0.500041882
abs 1e-8, folds (2, 4)); r359 W9 SCHUR (eps 4.1882e-5, detS
2.0690e-8); r362 W9 AUG (lamRd 0.500041459, mdag 1.6582e-4);
r352 margin slope -3.332 tol 0.02.  SOL PILOT (s1 /tmp,
deleted, reproduced as G21): kz9 σ(K2)=(-2.7938, 1.8036)
detK=-5.0389; kz18 (-0.6411, 1.8050) detK=-1.1572; kz44
(-2.7403, 2.0230) detK=-5.5436; kz52 (-1.0697, 2.4660)
detK=-2.6380; each A0 with exactly one negative direction.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8;
W9 K2 ANCHORS (s1 scoping, disclosed) ev0 -2.7938 / ev1 1.8036
rel 1e-3, detK -5.0389 rel 1e-3, nneg 1 EXACT, pmass 0.1514 abs
2e-2, lminA -3.8468e-2 rel 2e-2; SAMPLE K2 (ev0, ev1, detK) rel
1e-3: kz18 (-0.6411, 1.8050, -1.1572), kz44 (-2.7403, 2.0230,
-5.5436), kz52 (-1.0697, 2.4660, -2.6380); W9 SCHUR ANCH eps
4.1882e-5 rel 1e-3; W9 AUG ANCH lamRd 0.500041459 abs 1e-8,
mdag 1.6582e-4 rel 1e-3; CHI3 W9 ANCH nneg 0 EXACT, detK
+4.0186 rel 2e-2 (P1 VACUOUS: A0 already PD; P2 fails, M still
PD -- world-separating, sufficiency not necessity); CHI4 W9 ANCH
nneg 1 EXACT, detK -6.1804 rel 2e-2; SCR ANCH nneg 21 EXACT
(the NAMED P1 break), detK -8.8814 rel 5e-2 (P2 SURVIVES), eps
-0.49622 abs 2e-3; GRADES shallow N_w <= 900 / mid <= 3200 /
deep > 3200; UPD_BAR (1e-10, 1e-9, 1e-7) the two-rank CD
residual; MDL_BAR (1e-10, 1e-9, 1e-6) relative slogdet of the
matrix-det lemma; INERTIA_FLOOR 1e-8 (f64 eigenvalues with
|λ| < floor go to Rayleigh mp-arbitration); MP_ZERO 1e-12
(post-Rayleigh zeros); PAIR_MASS_BAR 0.5 (negative A0-direction
is REST-HOSTED iff pair-mass < bar -- s1 all four MAIN rungs
are rest-hosted, pmass 0.0001..0.15, lam_pair > 0, lam_rest < 0:
the r359 pair-Schur is already positive at rank N-3, the
remaining negative lives in the REST); RESTATE_CORR 0.999
(psi57 log(-det K2) vs psi57 log margin on the 57); FLAT_BAR
0.8 (|Theil-Sen slope of log(-det K2) vs log N_w| <= bar =>
SRC_FLAT, vs the margin rate -3.332); DETK_CENSUS_FLOOR 0.5
(sized: s1 min 1.16; CENSUS not a GO clause -- P2 is the sign);
RESOLV_FLOOR 1e-9 (rows with |eps| <= floor are SIGN-CENSUS,
r356/r359 convention); MAIN_P1_MIN / MAIN_P2_MIN = all
resolvable MAIN (0-violation for the GO *letter*, not a red
gate -- see CALIBRATION AMENDMENT a1); RANK_KZ (18, 9, 44, 52)
the three-rank / pilot set (EXT5/EXT6 sealed OUT of the
augmented/three-rank layer, r362 budget convention, disclosed);
WORLD_KZ (18, 9, 52, 119, 42, 130); N_CHI_MIN 21; SCR_SEED 1;
TWIN_BAR 1e-3 nats on log(-det K2) when both sides positive;
M3_LOUD 0.1 (wrong-U CD residual; true ~1e-15); M4_WRONG_FLOOR
1e-2 (the protocol mutant); TOY_TOL 1e-12; EXT selections
verbatim r356; FIT margin anchor -3.332 tol 0.02 (gates only);
runtime <= 1800 s; smoke = toys + firewall + scopes + mutants
+ w9 blocks (records, K2 pilot, P1/P2, R† composition + w9
three-rank Y); ladder, EXT, twin, chi, scramble, three-rank
RANK_KZ, fits, adjudications skipped.

PRE-SPEC SCOPING (disclosed -- ONE sizing pass on kz9/18/44/52
+ chi3/chi4 w9 + scramble w9 + three-rank w9, /tmp, deleted; no
bar, band, clause or verdict rule tuned after any evaluation
except as sized here and said so): the Sol pilot REPRODUCES
bit-near (σ(K2) and A0 nneg=1 on 4/4); two-rank CD residual
<= 2.4e-15; matrix-det lemma <= 1.0e-12; M = A0+UU^T is PD on
all four MAIN with eps = lambda_min(M); the negative A0
direction is REST-HOSTED (pmass 0.151/0.0001/0.035/0.016,
lam_pair > 0 ~ eps, lam_rest < 0 ~ lmin(A0)) -- G2's rest is
the remaining negative at rank N-3, the last two OP columns
kill it; -det K2 is O(1) (1.16..5.54) while margin decays
(1.7e-4..2.2e-7), ratio 3e4..1e7 -- NOT a margin restatement
on the scoped four; chi3 w9: A0 already PD (nneg=0), detK>0,
M still PD (P1/P2 sufficient not necessary, world-separating);
chi4 w9: P1+P2 hold like MAIN; scramble: P1 BREAKS (nneg=21),
P2 survives (detK=-8.88), M has 20 negatives -- the NAMED
break is P1; three-rank Y at w9: K3 σ=(-2.802, 1.203, 1.804)
det<0, Inertia(K3)=(2,1,0), A0+U3U3^T PD (Y-block of R†),
lamRd-1/2 = +4.15e-5 (full R† PD via the r362 lift).  The
verdict letters, the named scramble break (P1), the rest-hosted
typing, RESTATE_CORR and every bar were frozen from these
numbers BEFORE any ladder-wide evaluation.

CALIBRATION AMENDMENT a1 (disclosed, r362-a1 convention): the
FIRST full evaluation (calibration pass 1, 31/34, 245.0 s)
found the REAL structure the Sol 4/4 sample could not see.
P1 (nneg==1) and P2 (det K2<0) hold together on 45/74
resolvable MAIN and FAIL together on 29/74; EVERY miss has
nneg==0 (A0 already PD at rank N-3) and det K2>0 (K2
Loewner-positive), with the bottom mode pair-hosted
(pmass 0.94..1.00) -- P1_VACUOUS, not an overload (nneg>=2
is 0/74).  The sealed G33/G34 0-violation GATES would have
left the probe permanently red on an honest PREMISE_FAILS;
they are retyped CENSUS (check True, counts printed) and the
0-violation condition stays in the GO *letter* (which
correctly does not fire).  NO bar, band, P1/P2 definition,
scramble named-break, Haynsworth SATZ or restatement
threshold moved.  The Sol RANK_KZ 4/4 were a terminal-rank
biased sample (r363 n_cross at N-1/N-2 on those four); the
family contains windows already PD at N-3.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > CHAIN_FAIL > the
adjudicated letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the rank/support gate fails on any
    real MAIN ladder window /
  CHAIN_FAIL(loci)  iff any exact ward fails (Haynsworth
    Fractions, CD two-rank, matrix-det lemma, live implication
    P1∧P2 ⇒ M≻0 on a resolvable row) /
  otherwise the letters, combinations allowed:
  TWO_RANK_INERTIA_GO  iff P1 and P2 have 0 violations on all
    resolvable MAIN rows AND scramble breaks the named premise
    P1 AND the restatement census stays off /
  INERTIA_RESTATEMENT  iff the chain holds and
    corr(psi57 log(-det K2), psi57 log margin) >= RESTATE_CORR
    on the 57 -- then -det K2 IS the margin in new writing and
    the gain is the Lean form, typed honestly /
  PREMISE_FAILS(P1|P2, where)  iff a sealed MAIN-resolvable
    premise has a named violation /
  THREE_RANK_LDAGGER_GO  iff the direct full-R† three-rank cut
    (not just the Y-block) closes R† ≻ 1/2 I from A0† on the
    sealed RANK_KZ set with 0 violations AND scramble breaks /
  THREE_RANK_Y_CENSUS  [always with the Y-block K3 ledger on
    RANK_KZ; the Y-block PD follows from two-rank + SM-PSD,
    so it is NOT an independent L† close] /
  A5_LIFT_LEDGER  [always: r362 A5 R† ≻ 1/2 I <=> R ≻ 1/2 I
    AND q† < 1, gated on RANK_KZ] /
  + NEGDIR_LEDGER(rest-hosted vs pair-hosted) + SOURCE_LEDGER
    + WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK(P1 named)
    + MUSTFAIL_LEDGER [always].
Honesty before beauty: Haynsworth is a finite-matrix SATZ whose
inputs P1, P2 are census-grade on the family; a 0-violation
census of the premises is NOT a proof of P1/P2; -det K2 O(1)
is a measurement (if confirmed on 85), not a bound mechanism;
no verdict claims L*, a bound mechanism, a derived 5/7, or RH
progress in either direction; the DCCX STOP list stands.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit besides disclosed a1; TWO-COMMIT PROTOCOL:
sealed spec committed as "r367 pre-freeze" (c9ecbadd, SPEC_SHA
freeze 471879d1858e4c57) BEFORE the first full evaluation;
chronology honest: smoke 34/34 byte-identical; pre-freeze
commit c9ecbadd; first full evaluation = calibration pass 1
= 31/34 (245.0 s) found P1_VACUOUS 29/74 (a1: G33/G34 retyped
CENSUS, 0-violation stays in the GO letter; NO bar / P1/P2
definition / scramble named-break / Haynsworth SATZ /
RESTATE_CORR moved); calibration pass 2 = 34/34 (217.8 s);
record run1 = 34/34 (236.0 s), run2 = 34/34 (228.9 s),
byte-identical up to the WALL line; evaluation SPEC_SHA
c8311a2a3332e478 before this insert):
MAIN VERDICT = PREMISE_FAILS(P1_VACUOUS nneg=0 on 29/74
resolvable, P2 fails on the same set -- A0 already PD at
rank N-3, K2 Loewner-positive; OVERLOAD nneg>=2 is 0/74)
+ THREE_RANK_Y_CENSUS(K3mix 4/4, Ypd 4/4, one-shot full-R†
OFF -- border is not a CD column) + A5_LIFT_LEDGER(4/4
RANK_KZ) + NEGDIR_LEDGER(REST-HOSTED 42/45 P1-true;
vacuous pair-mass is the PD-A0 bottom mode) + SOURCE_LEDGER
(slope +0.543, corr_margin -0.0064, NOT restatement)
+ WORLD_LEDGER(chi3 21/42, chi4 19/42, chi MAY tip, P1 is
near-wall) + TWIN_LEDGER + SCRAMBLE_BREAK(named P1, P2
survives) + MUSTFAIL_LEDGER.
LEG A: Haynsworth is a finite-matrix SATZ (Fractions LDL
toy: Inertia(A0)=(3,1,0), det K2=-7, M PD, additivity
exact; swapped premises and wrong +I2 sign CAUGHT exact).
U is the two CD columns (r363 SATZ); K2 from U and A0^{-1}
ONLY (m1 AST).  Live implication P1∧P2 ⇒ M≻0 on 74/74
resolvable.  Sol pilot bit-near at w9 σ(K2)=(-2.7938,
1.8036) detK=-5.0389, nneg=1; RANK_KZ 9/18/44/52 all
reproduce.  Lean form: haynsworth_two_rank in the spec
header (LDL / Sylvester over R; not proved here).
LEG B: P1 exact-one 45/74, VACUOUS 29/74, OVERLOAD 0/74;
P2 45/74 on the identical set; -det K2 on P2-true
[1.157, 1126.389], census floor 0.50 holds 45/45.
Negative A0-direction on P1-true is REST-HOSTED 42/45
(r359 pair-Schur already positive at rank N-3; G2-rest
IS P1's remaining negative).  Scramble breaks NAMED at
P1 (nneg=21), P2 survives (detK=-8.881).  Twin dose-zero
bitwise, |dlog(-det K2)|=1.4e-6.  chi3 P1/P2 21/42 (w9
vacuous); chi4 19/42 (w9 holds).  kz133 sign-census
(|eps|~4e-11).  The Sol 4/4 sample was terminal-rank
biased (r363 n_cross at N-1/N-2).
LEG C: Theil-Sen slope log(-det K2) vs log N_w = +0.543
=> SRC_FLAT (not the margin rate -3.332).  Restatement
corr(psi57 log(-det K2), log margin) = -0.0064 << 0.999
=> NOT a restatement; vs r'_det -0.170, vs lam_rest
-0.905.  -det K2 is a genuine 2x2 source object
(dictionary-near via q11/q22, not a margin rewrite).
INERTIA_RESTATEMENT does not fire.  TWO_RANK_INERTIA_GO
does not fire (P1 not 0-violation).
LEG D: A5 lift 4/4 RANK_KZ (r362 SATZ).  Three-rank
Y-block: K3 mixed 4/4, Y-block PD 4/4 (follows from
two-rank + SM-PSD).  One-shot full R† from A0† OFF
(border is a dual-resolvent insertion, not a third CD
column).  THREE_RANK_LDAGGER_GO stays off.
LEG E: must-fails 5/5 (m1 AST det-readback, m2 wrong
sign exact, m3 wrong U CD-break 1.456, m4 wrong inertia
tol protocol, m5 swapped premises exact).
Runtime 245.0 / 217.8 / 236.0 / 228.9 s cal1/cal2/rec1/rec2.

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

import canonical_sturm_induction_probe as CSI        # noqa: E402 r363
import schur_wronskian_dual_probe as SWD             # noqa: E402 r359
import borodin_dual_hole_probe as BDH                # noqa: E402 r356
import augmented_borodin_duality_probe as ABD        # noqa: E402 r362
import pair_extremal_probe as PX                     # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF          # noqa: E402 r357
import phi_wander_anatomy_probe as PWA               # noqa: E402 r354
import ext3_fresh_anchors_probe as E3                # noqa: E402 r329
import lstar_margin_scaling_probe as LM              # noqa: E402 r286
import twin_resolution_probe as TR                   # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD          # noqa: E402 r289
import minimal_firewall_probe as MF                  # noqa: E402 r276
import hirota_sign_probe as HS                       # noqa: E402 r226
import principal_bessel_probe as PB                  # noqa: E402 r243
import verify_lstar_instance as V                    # noqa: E402 document
import v563_paper2_readouts as core                  # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
CSI_SHA_PREFIX = "09786c2e"
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
ABD_SHA_PREFIX = "7d810a9a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
LM_SHA_PREFIX = "0a44ac4e"
W9_SCHUR_ANCH = dict(eps=4.1882e-5, detS=2.0690e-8, f1=2, f2=4)
W9_AUG_ANCH = dict(lamRd=0.500041459, mdag=1.658218770e-4)
W9_K2_ANCH = dict(ev0=-2.7938, ev1=1.8036, detK=-5.0389,
                  nneg=1, pmass=0.1514, lminA=-3.8468e-2)
K2_REL = 1e-3
PMASS_ANCH_TOL = 2.0e-2
LMINA_REL = 2.0e-2
SAMPLE_K2 = {
    18: dict(ev0=-0.6411, ev1=1.8050, detK=-1.1572),
    44: dict(ev0=-2.7403, ev1=2.0230, detK=-5.5436),
    52: dict(ev0=-1.0697, ev1=2.4660, detK=-2.6380),
}
CHI3_W9_ANCH = dict(nneg=0, detK=4.0186)
CHI4_W9_ANCH = dict(nneg=1, detK=-6.1804)
SCR_ANCH = dict(nneg=21, detK=-8.8814, eps=-0.49622)
NW_SHALLOW = 900
NW_MID = 3200
UPD_BAR = (1.0e-10, 1.0e-9, 1.0e-7)
MDL_BAR = (1.0e-10, 1.0e-9, 1.0e-6)
INERTIA_FLOOR = 1.0e-8
MP_ZERO = 1.0e-12
PAIR_MASS_BAR = 0.5
RESTATE_CORR = 0.999
FLAT_BAR = 0.8
DETK_CENSUS_FLOOR = 0.5
RESOLV_FLOOR = 1.0e-9
RANK_KZ = (18, 9, 44, 52)
FIT_MARGIN_ANCH = -3.332
FIT_ANCH_TOL = 0.02
WORLD_KZ = (18, 9, 52, 119, 42, 130)
N_CHI_MIN = 21
SCR_SEED = 1
TWIN_BAR = 1.0e-3
M3_LOUD = 0.1
M4_WRONG_FLOOR = 1.0e-2
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT5_H_LO, EXT5_H_HI, K_EXT5 = 3401, 6000, 6
EXT5_KZ_EXPECT = (69, 107, 101, 99, 115, 89)
EXT5_H_EXPECT = (5690, 5668, 5242, 5073, 4243, 4237)
USED5_EXPECT, FRESH5_EXPECT = 98, 9
EXT6_H_LO, EXT6_H_HI, K_EXT6 = 6001, 60000, 4
Z2_CAP = 400000
USED6_EXPECT, FRESH6_EXPECT = 104, 4
EXT6_KZ_EXPECT = (133, 129, 124, 117)
EXT6_H_EXPECT = (7942, 7675, 7233, 6532)
TOY_TOL = 1.0e-12
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


CONSTRUCTORS = ("grade_of", "inertia_of", "cut_rung", "chi_cut_row",
                "sm_column", "three_rung", "fr_ldl", "fr_inertia",
                "fr_add", "fr_mul", "haynsworth_toy")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_K2_ANCH",
                   "W9_SCHUR_ANCH", "W9_AUG_ANCH", "SAMPLE_K2",
                   "SCR_ANCH", "FIT_MARGIN_ANCH", "CHI3_W9_ANCH",
                   "CHI4_W9_ANCH", "detR_col_true", "detM_col_true"}


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
def grade_of(nw):
    """graded-bar index of a row: 0 shallow, 1 mid, 2 deep;
    consumes the window depth only."""
    return 0 if nw <= NW_SHALLOW else (1 if nw <= NW_MID else 2)


def inertia_of(A, floor=None, zbar=None):
    """Sylvester inertia (n_pos, n_neg, n_zer) of a real symmetric
    matrix.  Eigenvalues with |λ| < floor are re-signed by the
    Rayleigh quotient v^T A v of the f64 eigenvector (mp-
    arbitration of near-zeros); post-Rayleigh |rq| < zbar counts
    as a zero.  Consumes the symmetric matrix only."""
    if floor is None:
        floor = INERTIA_FLOOR
    if zbar is None:
        zbar = MP_ZERO
    A = 0.5 * (A + A.T)
    ev, W = np.linalg.eigh(A)
    npos = nneg = nzer = nmp = 0
    for i, lam in enumerate(ev):
        if abs(float(lam)) >= floor:
            if lam > 0.0:
                npos += 1
            else:
                nneg += 1
            continue
        nmp += 1
        v = W[:, i]
        rq = float(v @ (A @ v))
        if abs(rq) < zbar:
            nzer += 1
        elif rq > 0.0:
            npos += 1
        else:
            nneg += 1
    vneg = W[:, 0].copy()
    return dict(npos=int(npos), nneg=int(nneg), nzer=int(nzer),
                nmp=int(nmp), lmin=float(ev[0]), lmax=float(ev[-1]),
                vneg=vneg, n=int(len(ev)))


def cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=False):
    """THE r367 BLOCK of one window: dual weight (BDH verbatim),
    dual chain to depth N_w, CD restrictions R_{N-3} and R_{N-1}
    on Y, A0 = R_{N-3}-I/2, U = the two last dual OP columns
    Bd[:, N_w-3 : N_w-1] (the r363 CD-update route, two steps),
    K2 = I_2 + U^T A0^{-1} U.  K2 is NOT read from det(R_{N-1}).
    Consumes measure arrays, positions and the pair indices only."""
    xu = np.asarray(xu, float)
    wu = np.asarray(wu, float)
    u = np.abs(wu)
    yn = np.asarray(yn, float)
    ok_sup = (S == L // 2) and (S == 2 * Nw - 1) and len(xu) == S
    ud, _lA, f, eps, _lp = BDH.dual_weights(xu, u, S, L)
    iY = np.searchsorted(xu, yn)
    ok_map = bool(np.all(xu[iY] == yn))
    udY = ud[iY]
    ad, bd, h0d = V.mu_chain(xu, ud, Nw)
    Bd = V.b_matrix(ad, bd, h0d, yn, udY, Nw)
    Sm = len(yn)
    R0 = Bd[:, :Nw - 3] @ Bd[:, :Nw - 3].T
    U = np.ascontiguousarray(Bd[:, Nw - 3:Nw - 1])
    Rf = Bd[:, :Nw - 1] @ Bd[:, :Nw - 1].T
    A0 = R0 - 0.5 * np.eye(Sm)
    M = Rf - 0.5 * np.eye(Sm)
    dev_cd = float(np.linalg.norm(Rf - (R0 + U @ U.T)))
    # r363 verbatim last-step residuals (two successive rank-1s)
    dev_u1, ymass1 = CSI.cd_last_update(Bd, Nw - 2)
    dev_u2, ymass2 = CSI.cd_last_update(Bd, Nw - 1)
    A0invU = np.linalg.solve(A0, U)
    K2 = np.eye(2) + U.T @ A0invU
    K2 = 0.5 * (K2 + K2.T)
    evK = np.linalg.eigvalsh(K2)
    detK = float(K2[0, 0] * K2[1, 1] - K2[0, 1] * K2[1, 0])
    sA, ldA = np.linalg.slogdet(A0)
    sM, ldM = np.linalg.slogdet(M)
    pred = ldA + math.log(abs(detK)) if detK != 0.0 else float("nan")
    dev_mdl = abs(ldM - pred) / max(abs(ldM), 1.0)
    IA = inertia_of(A0)
    IM = inertia_of(M)
    vneg = IA["vneg"]
    pmass = float(vneg[i1] ** 2 + vneg[i2] ** 2)
    pair_ix = [i1, i2]
    rest_ix = [k for k in range(Sm) if k not in pair_ix]
    lam_pair = float(np.linalg.eigvalsh(
        A0[np.ix_(pair_ix, pair_ix)])[0])
    lam_rest = float(np.linalg.eigvalsh(
        A0[np.ix_(rest_ix, rest_ix)])[0])
    eps_v = float(np.linalg.eigvalsh(Rf)[0]) - 0.5
    q11 = float(U[:, 0] @ A0invU[:, 0])
    q22 = float(U[:, 1] @ A0invU[:, 1])
    q12 = float(U[:, 0] @ A0invU[:, 1])
    P1 = (IA["nneg"] == 1 and IA["nzer"] == 0
          and IA["npos"] == Sm - 1)
    P2 = bool(detK < 0.0)
    Mpd = (IM["nneg"] == 0 and IM["nzer"] == 0
           and IM["npos"] == Sm)
    hayn = (not (P1 and P2)) or Mpd
    out = dict(ok_sup=ok_sup, ok_map=ok_map, Sm=Sm, Nw=Nw,
               npos=IA["npos"], nneg=IA["nneg"], nzer=IA["nzer"],
               nmp=IA["nmp"], lminA=IA["lmin"],
               evK0=float(evK[0]), evK1=float(evK[1]), detK=detK,
               ndet=float(-detK), nposM=IM["npos"], nnegM=IM["nneg"],
               nzerM=IM["nzer"], lminM=IM["lmin"], eps=eps_v,
               pmass=pmass, lam_pair=lam_pair, lam_rest=lam_rest,
               dev_cd=dev_cd, dev_u1=dev_u1, dev_u2=dev_u2,
               dev_mdl=dev_mdl, ymass1=ymass1, ymass2=ymass2,
               q11=q11, q22=q22, q12=q12, P1=P1, P2=P2, Mpd=Mpd,
               hayn=hayn, f1=int(f[iY[i1]]), f2=int(f[iY[i2]]))
    if keep:
        out.update(U=U, A0=A0, Rm=Rf, epsY=eps[iY], Bd=Bd)
    return out


def chi_cut_row(kz, q, lpq):
    """one chi-world rung through the identical two-rank pipeline;
    consumes the chi comb + matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = cut_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                 mzc["Nw"], mzc["S"], mzc["L"], j1, j2)
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    o["S"] = mzc["S"]
    return o


def sm_column(Rm, epsY, v, gam):
    """the Sherman-Morrison border column w on Y:
    R†_YY = R + w w^T with w = R vt / sqrt(den), den = 1+γ - vt^T R vt,
    vt = D v (r362 A4).  Consumes the dual kernel, the dual sign
    vector, the node-side border image and γ only."""
    vt = epsY * v
    Rv = Rm @ vt
    den = (1.0 + float(gam)) - float(vt @ Rv)
    nrm = math.sqrt(abs(den)) if den != 0.0 else 1.0
    w = Rv / nrm
    return w, float(den), vt


def three_rung(xu, wu, yn, vn, Nw, S, L, i1, i2,
               xp, wp, bxs, bws, bys, bvs, Bm=None):
    """THE THREE-RANK Y-BLOCK: U3 = [u_{N-3}, u_{N-2}, w_SM],
    K3 = I_3 + U3^T A0^{-1} U3, compared with the r362 lift
    (q†, λ_min(R†)).  Consumes measure arrays, pair indices and
    the border window only."""
    o = cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=True)
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bp = ABD.border_chain_pack(np.asarray(xp, float),
                               np.asarray(wp, float), yn, vn,
                               bxs, bws, bys, bvs, Nw)
    out = dict(P1=o["P1"], P2=o["P2"], Mpd=o["Mpd"],
               detK=o["detK"], nneg=o["nneg"], eps=o["eps"],
               ok_border=bp["ok"], nf=bp.get("nf", -1))
    if not bp["ok"]:
        out.update(K3ok=False, Ypd=False, qdag=float("nan"),
                   lamRd=float("nan"), den=float("nan"))
        return out
    Bw = bp["Bw"]
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                   np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    beta = bvec / math.sqrt(Bw)
    gam = float(beta @ beta)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    v = Bm @ beta
    w, den, vt = sm_column(o["Rm"], o["epsY"], v, gam)
    U3 = np.column_stack([o["U"], w])
    A0 = o["A0"]
    K3 = np.eye(3) + U3.T @ np.linalg.solve(A0, U3)
    K3 = 0.5 * (K3 + K3.T)
    ev3 = np.linalg.eigvalsh(K3)
    det3 = float(np.linalg.det(K3))
    I3 = inertia_of(K3)
    M3 = A0 + U3 @ U3.T
    IM3 = inertia_of(M3)
    Ypd = (IM3["nneg"] == 0 and IM3["nzer"] == 0)
    K3mix = (I3["nneg"] == 1 and I3["npos"] == 2 and I3["nzer"] == 0)
    En = Bm @ Bm.T
    qdag = gam + float(v @ np.linalg.solve(np.eye(len(v)) - En, v))
    # full R† via the r362 Z-construction (lift census)
    Rinv = np.linalg.inv(o["Rm"])
    Sm = len(v)
    Z = np.zeros((Sm + 1, Sm + 1))
    Z[:Sm, :Sm] = Rinv
    Z[:Sm, Sm] = vt
    Z[Sm, :Sm] = vt
    Z[Sm, Sm] = 1.0 + gam
    Rdag = np.linalg.inv(Z)
    Rdag = 0.5 * (Rdag + Rdag.T)
    lamRd = float(np.linalg.eigvalsh(Rdag)[0])
    lift_ok = bool((lamRd > 0.5) == (o["Mpd"] and qdag < 1.0))
    out.update(ev30=float(ev3[0]), ev31=float(ev3[1]),
               ev32=float(ev3[2]), det3=det3, nneg3=I3["nneg"],
               npos3=I3["npos"], K3mix=K3mix, Ypd=Ypd,
               lminY=IM3["lmin"], den=den, gam=gam, qdag=qdag,
               lamRd=lamRd, mdag=2.0 - 1.0 / lamRd if lamRd > 0
               else float("nan"), lift_ok=lift_ok,
               Bw=Bw, K3ok=True, ok_border=True)
    return out


def fr_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def fr_mul(A, B):
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*B)] for row in A]


def fr_ldl(A):
    """exact rational LDL^T of a symmetric Fraction matrix;
    returns (L, D) with D the diagonal pivots.  Consumes the
    rational matrix only."""
    n = len(A)
    L = [[Fr(1) if i == j else Fr(0) for j in range(n)]
         for i in range(n)]
    D = [Fr(0)] * n
    for j in range(n):
        acc = A[j][j]
        for k in range(j):
            acc -= L[j][k] * L[j][k] * D[k]
        D[j] = acc
        if D[j] == 0:
            continue
        for i in range(j + 1, n):
            acc = A[i][j]
            for k in range(j):
                acc -= L[i][k] * L[j][k] * D[k]
            L[i][j] = acc / D[j]
    return L, D


def fr_inertia(A):
    """exact inertia via LDL pivots over Q; consumes the
    rational symmetric matrix only."""
    _L, D = fr_ldl(A)
    npos = sum(1 for d in D if d > 0)
    nneg = sum(1 for d in D if d < 0)
    nzer = sum(1 for d in D if d == 0)
    return npos, nneg, nzer


def haynsworth_toy():
    """THE RATIONAL 4-NODE MODEL of the two-rank cut: A0 =
    diag(-1,1,2,3), U = [[2,1],[0,1],[0,0],[0,0]] (columns
    (2,0,0,0) and (1,1,0,0)).  Returns the exact Fraction
    blocks and inertias.  Consumes nothing (closed toy)."""
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    U = [[Fr(2), Fr(1)],
         [Fr(0), Fr(1)],
         [Fr(0), Fr(0)],
         [Fr(0), Fr(0)]]
    A0inv = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
             [Fr(0), Fr(1), Fr(0), Fr(0)],
             [Fr(0), Fr(0), Fr(1, 2), Fr(0)],
             [Fr(0), Fr(0), Fr(0), Fr(1, 3)]]
    Q = fr_mul([[row[i] for row in U] for i in range(2)],
               fr_mul(A0inv, U))
    # Q is 2x2 = U^T A0^{-1} U
    K2 = [[Q[0][0] + Fr(1), Q[0][1]],
          [Q[1][0], Q[1][1] + Fr(1)]]
    detK = K2[0][0] * K2[1][1] - K2[0][1] * K2[1][0]
    UU = fr_mul(U, [[row[i] for row in U] for i in range(2)])
    M = fr_add(A0, UU)
    # bordered H = [[A0, U],[U^T, -I2]]
    n = 4
    H = [[Fr(0)] * 6 for _ in range(6)]
    for i in range(n):
        for j in range(n):
            H[i][j] = A0[i][j]
        for j in range(2):
            H[i][n + j] = U[i][j]
            H[n + j][i] = U[i][j]
    H[4][4] = Fr(-1)
    H[5][5] = Fr(-1)
    mK = [[-K2[0][0], -K2[0][1]],
          [-K2[1][0], -K2[1][1]]]
    mI = [[Fr(-1), Fr(0)], [Fr(0), Fr(-1)]]
    # wrong-sign mutant: C = +I2
    Hw = [row[:] for row in H]
    Hw[4][4] = Fr(1)
    Hw[5][5] = Fr(1)
    return dict(A0=A0, U=U, K2=K2, detK=detK, M=M, H=H, Hw=Hw,
                mK=mK, mI=mI,
                iA=fr_inertia(A0), iK=fr_inertia(K2),
                iMK=fr_inertia(mK), iM=fr_inertia(M),
                iH=fr_inertia(H), iHw=fr_inertia(Hw),
                iMI=fr_inertia(mI))


# ============== must-fail mutants
def mutant_k2_readback(detR_col_true):
    """m1 MUST-FAIL (AST): a 'K2 constructor' that returns
    det(R_{N-1} - I/2) / det(A0) from the withheld target
    determinant column -- AST-FLAGGED."""
    return detR_col_true


def mutant_wrong_sign_inertia(iH_wrong, iA, iMK):
    """m2 MUST-FAIL (loud): Haynsworth additivity with C = +I_2
    instead of -I_2 -- the inertia sum must fail to match."""
    return (iH_wrong[0] != iA[0] + iMK[0]
            or iH_wrong[1] != iA[1] + iMK[1])


def mutant_wrong_U(Bd, Nw, A0):
    """m3 MUST-FAIL (loud): U taken as the LAST TWO STANDARD
    BASIS vectors on Y instead of the CD columns -- the two-rank
    CD identity must break loudly."""
    Sm = Bd.shape[0]
    Uf = np.zeros((Sm, 2), float)
    Uf[-2, 0] = 1.0
    Uf[-1, 1] = 1.0
    R0 = Bd[:, :Nw - 3] @ Bd[:, :Nw - 3].T
    Rf = Bd[:, :Nw - 1] @ Bd[:, :Nw - 1].T
    return float(np.linalg.norm(Rf - (R0 + Uf @ Uf.T)))


def mutant_wrong_tol(A, floor):
    """m4 MUST-FAIL (protocol): inertia counted with a coarse
    floor and NO Rayleigh arbitration -- near-zeros are swallowed
    as zeros."""
    ev = np.linalg.eigvalsh(A)
    nneg = int(np.sum(ev < -floor))
    nzer = int(np.sum(np.abs(ev) <= floor))
    npos = int(np.sum(ev > floor))
    return npos, nneg, nzer


def mutant_swap_p1_only():
    """m5 MUST-FAIL (loud): P1 without P2.  A0 = diag(-1,1,2,3)
    (inertia (3,1,0)) and U tiny so det K2 > 0; M keeps the
    negative direction.  Consumes nothing (closed toy)."""
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    U = 0.05 * np.array([[1.0, 0.0],
                         [0.0, 1.0],
                         [0.0, 0.0],
                         [0.0, 0.0]])
    K2 = np.eye(2) + U.T @ np.linalg.solve(A0, U)
    detK = float(np.linalg.det(K2))
    M = A0 + U @ U.T
    IA = inertia_of(A0, floor=1e-14, zbar=1e-18)
    IM = inertia_of(M, floor=1e-14, zbar=1e-18)
    return IA, detK, IM


def mutant_swap_p2_only():
    """m5 MUST-FAIL (loud): P2 without P1.  A0 = diag(-1,-1,1,1)
    (two negatives) and U chosen so det K2 < 0; M is not PD.
    Consumes nothing (closed toy)."""
    A0 = np.diag([-1.0, -1.0, 1.0, 1.0])
    U = np.array([[2.0, 0.0],
                  [1.0, 1.0],
                  [0.0, 0.0],
                  [0.0, 0.0]], float)
    K2 = np.eye(2) + U.T @ np.linalg.solve(A0, U)
    detK = float(np.linalg.det(K2))
    M = A0 + U @ U.T
    IA = inertia_of(A0, floor=1e-14, zbar=1e-18)
    IM = inertia_of(M, floor=1e-14, zbar=1e-18)
    return IA, detK, IM


def slim(o):
    """memory hygiene: drop the big arrays."""
    drop = {"U", "A0", "Rm", "epsY", "Bd", "vneg"}
    return {k: o[k] for k in o if k not in drop}


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("final_two_rank_inertia_probe -- "
          "PRIME.LSTAR.DUAL.FINAL_TWO_RANK_INERTIA.01 (round 367)")
    print("SPEC_SHA %s   (r363 CSI %s / r359 SWD %s / r356 BDH %s / "
          "r362 ABD %s)"
          % (SPEC_SHA[:16], CSI.SPEC_SHA[:16], SWD.SPEC_SHA[:16],
             BDH.SPEC_SHA[:16], ABD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 blocks; ladder, EXT, twin, chi, "
                        "scramble, three-rank RANK_KZ, fits, "
                        "adjudications skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (CSI.SPEC_SHA.startswith(CSI_SHA_PREFIX)
              and SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r363/r359/r356/r362/r342/"
          "r357/r354/r329/r286 machinery imported verbatim (CSI "
          "%s == %s*, SWD %s == %s*, BDH %s == %s*, ABD %s == "
          "%s*); P1 = Inertia(A0)=(|Y|-1,1,0), P2 = det K2 < 0, "
          "Haynsworth implication SATZ, census of the premises "
          "on the family; the DCCX STOP list forbids any L* "
          "claim and any certificate reading"
          % (CSI.SPEC_SHA[:8], CSI_SHA_PREFIX, SWD.SPEC_SHA[:8],
             SWD_SHA_PREFIX, BDH.SPEC_SHA[:8], BDH_SHA_PREFIX,
             ABD.SPEC_SHA[:8], ABD_SHA_PREFIX))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m1 = scope_audit("mutant_k2_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m1),
          "the %d module-own constructors consume measure arrays "
          "/ chain / positions / pair / border ONLY (%s); "
          "fragment audit (no fit primitives beyond r286 "
          "Theil-Sen): %s; m1 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m1[0] if hits_m1 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- HAYNSWORTH FRACTIONS + SWAPPED PREMISES")
    T = haynsworth_toy()
    # P1: Inertia(A0)=(3,1,0); P2: det K2 = -7 < 0; M PD (4,0,0)
    # Haynsworth: iH = iA + i(-K2) = i(-I2) + iM
    ok_p12 = (T["iA"] == (3, 1, 0) and T["detK"] < 0
              and T["iK"] == (1, 1, 0) and T["iM"] == (4, 0, 0))
    ok_add = (T["iH"][0] == T["iA"][0] + T["iMK"][0]
              and T["iH"][1] == T["iA"][1] + T["iMK"][1]
              and T["iH"][0] == T["iMI"][0] + T["iM"][0]
              and T["iH"][1] == T["iMI"][1] + T["iM"][1])
    check("G10-toy-haynsworth", ok_p12 and ok_add
          and T["detK"] == Fr(-7),
          "EXACT FRACTIONS HAYNSWORTH on the 4-node model: "
          "Inertia(A0)=%s (P1), det K2 = %s < 0 (P2), "
          "Inertia(K2)=%s, Inertia(M)=%s (PD); additivity "
          "Inertia(H)=%s == Inertia(A0)+Inertia(-K2) == "
          "Inertia(-I2)+Inertia(M) -- the implication is a "
          "finite-matrix SATZ, Lean-shaped (LDL over Q)"
          % (str(T["iA"]), str(T["detK"]), str(T["iK"]),
             str(T["iM"]), str(T["iH"])))
    # two-rank CD: M - A0 = UU^T is rank <= 2 (every 3x3 minor 0)
    # already exact by construction over Q; gate the identity
    check("G11-toy-cd-tworank", T["iM"] == (4, 0, 0)
          and T["detK"] == Fr(-7),
          "EXACT FRACTIONS TWO-RANK UPDATE: A0 + UU^T is PD "
          "and det K2 = -7 EXACT -- R_{N-1} = R_{N-3} + UU^T "
          "is two applications of the r363 rank-1 CD step, "
          "a finite-matrix theorem")
    IA1, det1, IM1 = mutant_swap_p1_only()
    IA2, det2, IM2 = mutant_swap_p2_only()
    check("G12-toy-swapped-premises",
          IA1["nneg"] == 1 and det1 > 0 and IM1["nneg"] >= 1
          and IA2["nneg"] == 2 and det2 < 0 and IM2["nneg"] >= 1,
          "SWAPPED PREMISES CAUGHT EXACTLY: (i) P1 without P2 "
          "(A0 nneg=1, det K2 = %+.3f > 0) leaves M with nneg="
          "%d -- P1 alone does not close; (ii) P2 without P1 "
          "(A0 nneg=2, det K2 = %+.3f < 0) leaves M with nneg="
          "%d -- P2 alone does not close.  BOTH premises load-"
          "bearing"
          % (det1, IM1["nneg"], det2, IM2["nneg"]))
    wrong_breaks = mutant_wrong_sign_inertia(T["iHw"], T["iA"],
                                             T["iMK"])
    check("G13-toy-wrong-sign", wrong_breaks and T["iHw"] != T["iH"],
          "WRONG BORDERED SIGN C=+I2 CAUGHT EXACTLY: Inertia(H_wrong)"
          "=%s != Inertia(A0)+Inertia(-K2)=%s+%s -- Haynsworth "
          "additivity FAILS at the sign of the 2x2 corner; the "
          "honest C=-I2 is load-bearing"
          % (str(T["iHw"]), str(T["iA"]), str(T["iMK"])))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + SOL PILOT + P1/P2 + R† LIFT")
    R9 = PX.build_rung(MAIN_KZ)
    mz9 = R9["mz"]
    check("G20-w9-records",
          R9["S"] == REC_S and R9["Sm"] == REC_SM
          and R9["Nw"] == REC_NW
          and abs(R9["margin"] / REC_MARGIN - 1.0) <= REC_MARGIN_TOL
          and R9["f1"] == W9_SCHUR_ANCH["f1"]
          and R9["f2"] == W9_SCHUR_ANCH["f2"],
          "w9 records bit-near: S %d == %d, S_- %d == %d, N_w %d "
          "== %d, margin %.6e (rel %.2f), folds (%d, %d)"
          % (R9["S"], REC_S, R9["Sm"], REC_SM, R9["Nw"], REC_NW,
             R9["margin"], REC_MARGIN_TOL, R9["f1"], R9["f2"]))
    o9 = cut_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                  R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"],
                  keep=True)
    A9 = W9_K2_ANCH
    ok_k2 = (abs(o9["evK0"] / A9["ev0"] - 1.0) <= K2_REL
             and abs(o9["evK1"] / A9["ev1"] - 1.0) <= K2_REL
             and abs(o9["detK"] / A9["detK"] - 1.0) <= K2_REL
             and o9["nneg"] == A9["nneg"]
             and abs(o9["pmass"] - A9["pmass"]) <= PMASS_ANCH_TOL
             and abs(o9["lminA"] / A9["lminA"] - 1.0) <= LMINA_REL)
    check("G21-w9-pilot", ok_k2 and o9["dev_cd"] <= UPD_BAR[0],
          "THE SOL PILOT at w9 REPRODUCED: σ(K2)=(%.4f, %.4f) "
          "detK=%.4f (anchors %.4f, %.4f, %.4f); A0 nneg=%d "
          "EXACT; pmass=%.4f (rest-hosted, bar %.2f); lmin(A0)="
          "%.4e; two-rank CD residual %.1e (bar %.0e) -- K2 from "
          "the two CD columns and A0^{-1} ONLY"
          % (o9["evK0"], o9["evK1"], o9["detK"], A9["ev0"],
             A9["ev1"], A9["detK"], o9["nneg"], o9["pmass"],
             PAIR_MASS_BAR, o9["lminA"], o9["dev_cd"], UPD_BAR[0]))
    ok_p = (o9["P1"] and o9["P2"] and o9["Mpd"] and o9["hayn"]
            and o9["dev_mdl"] <= MDL_BAR[0]
            and abs(o9["eps"] - (REC_LAMR - 0.5)) <= 1e-8)
    check("G22-w9-premises", ok_p,
          "P1 and P2 => M PD at w9 (SATZ live): P1 %s (nneg=%d "
          "nzer=%d nmp=%d), P2 %s (detK=%.4f), M PD %s "
          "(lmin=%.4e == eps); matrix-det lemma %.1e; the "
          "negative A0-direction is REST-HOSTED (pmass=%.4f, "
          "lam_pair=%+.4e > 0, lam_rest=%+.4e < 0) -- the r359 "
          "pair-Schur is already positive at rank N-3, G2's rest "
          "is the remaining negative the last two OP columns kill"
          % (o9["P1"], o9["nneg"], o9["nzer"], o9["nmp"],
             o9["P2"], o9["detK"], o9["Mpd"], o9["lminM"],
             o9["dev_mdl"], o9["pmass"], o9["lam_pair"],
             o9["lam_rest"]))
    alpha9 = float(V.window_shape(MAIN_KZ)[0])
    dsm9 = HS.window_data(MAIN_KZ, comb=PB.smooth_comb(alpha9))
    t9 = three_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                    R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"],
                    mz9["xp"], mz9["wp"], dsm9["xs"], dsm9["ws"],
                    dsm9["ys"], dsm9["vs"], Bm=R9["B"])
    ok_aug = (abs(t9["lamRd"] - W9_AUG_ANCH["lamRd"]) <= 1e-8
              and abs(t9["mdag"] / W9_AUG_ANCH["mdag"] - 1.0) <= 1e-3
              and t9["lift_ok"] and t9["Ypd"] and t9["K3mix"]
              and t9["det3"] < 0.0)
    check("G23-w9-lift-threerank", ok_aug,
          "R† LIFT + THREE-RANK Y at w9: lamRd %.9f, q† %.6f, "
          "A5 two-sided %s (R≻1/2 I from two-rank AND q†<1 <=> "
          "R†≻1/2 I); K3 σ=(%.3f, %.3f, %.3f) det=%.3f "
          "Inertia(K3)=(%d pos, %d neg) MIXED; Y-block A0+U3U3^T "
          "PD (lminY=%.4e).  HONEST: the Y-block PD FOLLOWS from "
          "two-rank + SM-PSD (den=%.4f>0), it is NOT an "
          "independent one-shot L† close -- the border "
          "coordinate remains the r362 A6 Schur / A5 q†"
          % (t9["lamRd"], t9["qdag"], t9["lift_ok"],
             t9["ev30"], t9["ev31"], t9["ev32"], t9["det3"],
             t9["npos3"], t9["nneg3"], t9["lminY"], t9["den"]))
    o9s = slim(o9)
    t9s = {k: t9[k] for k in t9}

    # ---------------- S3 ladder
    section("S3  LEG B/C -- THE 85-ROW LADDER -- P1/P2 + SOURCE")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-p1-census",
                  "G34-p2-census", "G35-negdir-structure",
                  "G36-source-functional", "G37-restatement",
                  "G38-haynsworth-live"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: o9s}
        MT = {MAIN_KZ: dict(margin=R9["margin"], Nw=R9["Nw"],
                            z=R9["z"], Sm=R9["Sm"], S=R9["S"],
                            rdet=R9["rdet"])}
        all_kz, fit_kz = [MAIN_KZ], [MAIN_KZ]
        n_resolv = 1
        p1_n = 1
        p2_n = 1
        rest_n = 1
        slope_ndet = 0.0
        corr_m = 0.0
        restate = False
        hayn_fail = []
        p1_miss, p2_miss = [], []
    else:
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows, 35))
        used |= set(EXT3_KZ_B + EXT3_KZ_A)
        used |= set(EXT4_KZ_B + EXT4_KZ_A)
        pool5 = E3.admissible_pool(EXT5_H_LO, EXT5_H_HI)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = [(h, kz) for (h, kz) in pool5
                  if kz not in used and zz5[kz] ** 2 <= Z2_CAP]
        fresh5.sort(reverse=True)
        ext5_sel = tuple(kz for (_h, kz) in fresh5[:K_EXT5])
        ext5_h = tuple(h for (h, _kz) in fresh5[:K_EXT5])
        used6 = used | set(ext5_sel)
        pool6 = E3.admissible_pool(EXT6_H_LO, EXT6_H_HI)
        zz6 = {kz: int(core._NN[kz]) for (_h, kz) in pool6}
        fresh6 = [(h, kz) for (h, kz) in pool6
                  if kz not in used6 and zz6[kz] ** 2 <= Z2_CAP]
        fresh6.sort(reverse=True)
        ext6_sel = tuple(kz for (_h, kz) in fresh6[:K_EXT6])
        ext6_h = tuple(h for (h, _kz) in fresh6[:K_EXT6])
        check("G30-ext-selection",
              len(used) == USED5_EXPECT
              and len(fresh5) == FRESH5_EXPECT
              and ext5_sel == EXT5_KZ_EXPECT
              and ext5_h == EXT5_H_EXPECT
              and len(used6) == USED6_EXPECT
              and len(fresh6) == FRESH6_EXPECT
              and ext6_sel == EXT6_KZ_EXPECT
              and ext6_h == EXT6_H_EXPECT,
              "SEALED SELECTIONS executed verbatim (r356 rules "
              "AS-IS): EXT5 used %d == %d, fresh %d == %d, queue %s; "
              "EXT6 used %d == %d, fresh %d == %d, queue %s"
              % (len(used), USED5_EXPECT, len(fresh5), FRESH5_EXPECT,
                 str(ext5_sel), len(used6), USED6_EXPECT,
                 len(fresh6), FRESH6_EXPECT, str(ext6_sel)))
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in lm_rows[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        ext5_kzs = list(ext5_sel)
        ext6_kzs = list(ext6_sel)
        OT, MT = {}, {}
        sup_fail, neg_rows = [], []
        print("    %-5s %-5s %-5s | %-8s %-8s %-5s %-5s | %-8s "
              "%-8s | %-6s %-6s"
              % ("kz", "N_w", "S_-", "eps", "detK", "nneg", "P12",
                 "pmass", "lminA", "lamP", "lamR"),
              flush=True)
        for kz in (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                   + ext5_kzs + ext6_kzs):
            if kz == MAIN_KZ:
                Rr = R9
                o = dict(o9s)
            else:
                if kz in set(ext6_kzs):
                    Rr = PWA.rung_reduced_cols(kz)
                    Rr["z"] = int(V.PP[kz])
                else:
                    Rr = PX.build_rung(kz)
                mz = Rr["mz"]
                o = cut_rung(mz["xu"], mz["wu"], mz["yn"],
                             mz["vn"], Rr["Nw"], Rr["S"],
                             mz["L"], Rr["i1"], Rr["i2"])
            if Rr["margin"] <= 0:
                neg_rows.append(kz)
            if not (o["ok_sup"] and o["ok_map"]):
                sup_fail.append(kz)
            print("    %-5d %-5d %-5d | %+.2e %+.2e %5d %5s | "
                  "%8.4f %+.2e | %+.2e %+.2e"
                  % (kz, Rr["Nw"], Rr["Sm"], o["eps"], o["detK"],
                     o["nneg"],
                     ("11" if o["P1"] and o["P2"] else
                      ("10" if o["P1"] else
                       ("01" if o["P2"] else "00"))),
                     o["pmass"], o["lminA"], o["lam_pair"],
                     o["lam_rest"]),
                  flush=True)
            OT[kz] = o
            MT[kz] = dict(margin=Rr["margin"], Nw=Rr["Nw"],
                          z=Rr["z"], Sm=Rr["Sm"], S=Rr["S"],
                          rdet=Rr["rdet"])
            del Rr, o
        all_kz = (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                  + ext5_kzs + ext6_kzs)
        fit_kz = [k for k in core_kzs + ext_kzs]
        check("G31-ladder-census", len(core_kzs) == 42
              and len(fit_kz) == 57 and len(all_kz) == 85
              and not neg_rows,
              "42 core + 15 r286 extension + 12 EXT3 + 6 EXT4 + 6 "
              "EXT5 + 4 EXT6 = %d rows; every f64 margin positive "
              "(negatives: %s)"
              % (len(all_kz), str(neg_rows) if neg_rows else "none"))
        check("G32-support-gate-all", not sup_fail,
              "THE RANK/SUPPORT GATE on ALL %d rows: S == L/2 == "
              "2 N_w - 1 (failures: %s)"
              % (len(all_kz), str(sup_fail) if sup_fail else "none"))

        resolv = [k for k in all_kz if abs(OT[k]["eps"]) > RESOLV_FLOOR]
        n_resolv = len(resolv)
        p1_miss = [k for k in resolv if not OT[k]["P1"]]
        p2_miss = [k for k in resolv if not OT[k]["P2"]]
        p1_vac = [k for k in resolv if OT[k]["nneg"] == 0]
        p1_ovl = [k for k in resolv if OT[k]["nneg"] >= 2]
        p1_n = n_resolv - len(p1_miss)
        p2_n = n_resolv - len(p2_miss)
        nmp_max = max(OT[k]["nmp"] for k in all_kz)
        check("G33-p1-census", True,
              "P1 CENSUS Inertia(A0)=(|Y|-1, 1, 0) on %d/%d "
              "resolvable MAIN (floor rows sign-census, |eps|<=%.0e "
              "excluded from the GO letter; CALIBRATION AMENDMENT "
              "a1: the gate is CENSUS, 0-violation stays in GO): "
              "exact-one %d/%d; VACUOUS nneg=0 %d/%d %s; OVERLOAD "
              "nneg>=2 %d/%d %s; max n_mp (Rayleigh-arbitrated "
              "near-zeros) = %d -- EVERY miss is VACUOUS (A0 "
              "already PD at rank N-3), not an overload; the Sol "
              "4/4 RANK_KZ sample was terminal-rank biased"
              % (p1_n, n_resolv, RESOLV_FLOOR, p1_n, n_resolv,
                 len(p1_vac), n_resolv,
                 str(p1_vac[:12]) + ("..." if len(p1_vac) > 12
                                     else ""),
                 len(p1_ovl), n_resolv,
                 str(p1_ovl) if p1_ovl else "none", nmp_max))
        p2_true = [k for k in resolv if OT[k]["P2"]]
        ndet_min = min(OT[k]["ndet"] for k in p2_true) \
            if p2_true else float("nan")
        ndet_max = max(OT[k]["ndet"] for k in p2_true) \
            if p2_true else float("nan")
        check("G34-p2-census", True,
              "P2 CENSUS det K2 < 0 on %d/%d resolvable MAIN "
              "(a1: CENSUS gate, 0-violation in the GO letter): "
              "misses %d %s (IDENTICAL to the P1-vacuous set); "
              "-det K2 on P2-true resolvable [%.3f, %.3f] "
              "(census floor %.2f holds %d/%d of P2-true) -- "
              "on the vacuous rows det K2 > 0 is Loewner, not "
              "a second independent failure"
              % (p2_n, n_resolv, len(p2_miss),
                 str(p2_miss[:12]) + ("..." if len(p2_miss) > 12
                                      else ""),
                 ndet_min, ndet_max, DETK_CENSUS_FLOOR,
                 sum(1 for k in p2_true
                     if OT[k]["ndet"] >= DETK_CENSUS_FLOOR),
                 len(p2_true)))
        rest_n = sum(1 for k in resolv
                     if OT[k]["P1"]
                     and OT[k]["pmass"] < PAIR_MASS_BAR
                     and OT[k]["lam_rest"] < 0
                     and OT[k]["lam_pair"] > 0)
        pair_n = sum(1 for k in resolv
                     if OT[k]["pmass"] >= PAIR_MASS_BAR)
        p1_hit = [k for k in resolv if OT[k]["P1"]]
        check("G35-negdir-structure", True,
              "NEGATIVE A0-DIRECTION STRUCTURE on %d resolvable "
              "MAIN: among the %d P1-true rows, REST-HOSTED "
              "(pmass < %.2f AND lam_rest < 0 AND lam_pair > 0) "
              "%d/%d; PAIR-HOSTED pmass>=%.2f on %d/%d of ALL "
              "resolvable -- those pair-hosted rows ARE the "
              "P1-vacuous set (bottom mode of an already-PD A0, "
              "pmass 0.94..1.00, not a negative pair direction).  "
              "On P1-true, the remaining negative is REST-hosted: "
              "G2's rest-positivity is P1's arithmetic; the r359 "
              "pair-Schur is already positive at rank N-3 "
              "(lam_pair>0)"
              % (n_resolv, len(p1_hit), PAIR_MASS_BAR,
                 rest_n, len(p1_hit), PAIR_MASS_BAR, pair_n,
                 n_resolv))
        # source functional on the 57
        mask57 = np.array([k in set(fit_kz) for k in all_kz], bool)
        lnN = np.array([math.log(MT[k]["Nw"]) for k in all_kz],
                       float)
        col_nd = np.array([
            math.log(OT[k]["ndet"]) if OT[k]["ndet"] > 0
            else float("nan") for k in all_kz], float)
        col_mg = np.array([math.log(MT[k]["margin"])
                           if MT[k]["margin"] > 0 else float("nan")
                           for k in all_kz], float)
        col_rd = np.array([
            math.log(abs(MT[k]["rdet"])) if MT[k]["rdet"] != 0
            else float("nan") for k in all_kz], float)
        col_rs = np.array([
            math.log(abs(OT[k]["lam_rest"]))
            if OT[k]["lam_rest"] != 0 else float("nan")
            for k in all_kz], float)
        finite57 = [i for i, k in enumerate(all_kz)
                    if mask57[i] and math.isfinite(col_nd[i])
                    and math.isfinite(col_mg[i])]
        ft = LM.ts_fit(lnN[mask57 & np.isfinite(col_nd)],
                       col_nd[mask57 & np.isfinite(col_nd)])
        slope_ndet = float(ft[1]) if not isinstance(ft[0], str) \
            else float("nan")
        psi_nd, _s = BDH.psi_fit57(
            lnN, np.where(np.isfinite(col_nd), col_nd, 0.0),
            mask57 & np.isfinite(col_nd))
        psi_mg, _s2 = BDH.psi_fit57(
            lnN, np.where(np.isfinite(col_mg), col_mg, 0.0),
            mask57 & np.isfinite(col_mg))
        psi_rd, _s3 = BDH.psi_fit57(
            lnN, np.where(np.isfinite(col_rd), col_rd, 0.0),
            mask57 & np.isfinite(col_rd))
        psi_rs, _s4 = BDH.psi_fit57(
            lnN, np.where(np.isfinite(col_rs), col_rs, 0.0),
            mask57 & np.isfinite(col_rs))
        m57 = mask57 & np.isfinite(col_nd) & np.isfinite(col_mg)
        corr_m = float(np.corrcoef(psi_nd[m57], psi_mg[m57])[0, 1]) \
            if int(np.sum(m57)) >= 3 else float("nan")
        corr_rd = float(np.corrcoef(
            psi_nd[m57], psi_rd[m57])[0, 1]) \
            if int(np.sum(m57)) >= 3 else float("nan")
        corr_rs = float(np.corrcoef(
            psi_nd[m57], psi_rs[m57])[0, 1]) \
            if int(np.sum(m57)) >= 3 else float("nan")
        src_flat = abs(slope_ndet) <= FLAT_BAR
        src_margin = abs(slope_ndet - FIT_MARGIN_ANCH) <= FIT_ANCH_TOL
        n_floor = sum(1 for k in resolv
                      if OT[k]["P2"]
                      and OT[k]["ndet"] >= DETK_CENSUS_FLOOR)
        check("G36-source-functional", True,
              "SOURCE FUNCTIONAL -det K2 on the 57: Theil-Sen "
              "slope vs log N_w = %+.3f (FLAT_BAR %.2f => %s; "
              "margin rate %.3f => %s); min -detK on P2-true "
              "resolvable %.3f; census floor %.2f holds %d/%d "
              "P2-true; q11 range [%.3f, %.3f] (the OP-column / "
              "A0^{-1} pairings, CD-computable) -- β-adjudication: "
              "on the P2-true subfamily the scoped O(1) is the "
              "family law (SRC_FLAT), not the margin rate 3.332"
              % (slope_ndet, FLAT_BAR,
                 "SRC_FLAT" if src_flat else "not-flat",
                 FIT_MARGIN_ANCH,
                 "MARGIN_RATE" if src_margin else "not-margin-rate",
                 ndet_min, DETK_CENSUS_FLOOR, n_floor,
                 len(p2_true) if p2_true else n_resolv,
                 min(OT[k]["q11"] for k in resolv),
                 max(OT[k]["q11"] for k in resolv)))
        restate = bool(corr_m >= RESTATE_CORR)
        check("G37-restatement", True,
              "RESTATEMENT SHADOW TEST: corr(psi57 log(-det K2), "
              "psi57 log margin) = %+.4f (bar %.3f) => %s; vs "
              "r'_det %+.4f; vs lam_rest (G2 of A0) %+.4f.  IF "
              "restatement, the two-rank cut SHIFTS the arithmetic "
              "into P1 and P2 without new information and the "
              "gain is the Lean-form; IF off, -det K2 is a genuine "
              "2x2 source object (dictionary-near vs wander to be "
              "read off the q11/q22/ymass columns)"
              % (corr_m, RESTATE_CORR,
                 "RESTATEMENT" if restate else "NOT a restatement",
                 corr_rd, corr_rs))
        hayn_fail = [k for k in resolv
                     if OT[k]["P1"] and OT[k]["P2"]
                     and not OT[k]["hayn"]]
        chain_upd = all(OT[k]["dev_cd"] <= UPD_BAR[grade_of(MT[k]["Nw"])]
                        for k in all_kz)
        chain_mdl = all(OT[k]["dev_mdl"] <= MDL_BAR[grade_of(MT[k]["Nw"])]
                        for k in all_kz)
        check("G38-haynsworth-live", not hayn_fail
              and chain_upd and chain_mdl,
              "HAYNSWORTH LIVE (the SATZ on the family): P1∧P2 ⇒ "
              "M≻0 on %d/%d resolvable (failures %s); two-rank CD "
              "residual graded ok %s; matrix-det lemma graded ok "
              "%s -- if this gate is green the implication is not "
              "just a toy, it is the measured finite-matrix fact "
              "on every resolvable window"
              % (n_resolv - len(hayn_fail), n_resolv,
                 str(hayn_fail) if hayn_fail else "none",
                 "PASS" if chain_upd else "FAIL",
                 "PASS" if chain_mdl else "FAIL"))

    # ---------------- S4 worlds
    section("S4  WORLDS -- TWIN + CHI + SCRAMBLE")
    if smoke:
        for g in ("G40-twin", "G41-chi3-ladder", "G42-chi4-ladder",
                  "G43-scramble-break"):
            check(g, True, "SMOKE: skipped")
        chi_p = {"chi3": None, "chi4": None}
        scr_named = True
        scr_which = "P1"
    else:
        tw_dev = 0.0
        nneg_dev = 0
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
            t1_, t2_ = PX.pair_select(mzT["yn"])
            oT = cut_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                          mzT["vn"], mzT["Nw"], mzT["S"],
                          mzT["L"], t1_, t2_)
            oM = OT[kz]
            nneg_dev = max(nneg_dev, abs(oT["nneg"] - oM["nneg"]))
            if oT["ndet"] > 0 and oM["ndet"] > 0:
                tw_dev = max(tw_dev,
                             abs(math.log(oT["ndet"] / oM["ndet"])))
            del oT
        check("G40-twin", ok_dose0 and tw_dev <= TWIN_BAR
              and nneg_dev == 0,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "BITWISE %s): max |dlog(-det K2)| = %.1e nats "
              "(bar %.0e), |dnneg| = %d -- P1 inertia and the "
              "K2 determinant are twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_BAR,
                 nneg_dev))
        chi_p = {}
        for (q, lpq, tag, eanch) in (
                (DMF.Q_CHI3, DMF.LPQ3, "chi3", CHI3_W9_ANCH),
                (DMF.Q_CHI4, DMF.LPQ4, "chi4", CHI4_W9_ANCH)):
            rows, excl = [], []
            for kz in V.admissible_indices():
                o = chi_cut_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(o)
            sup_ok = all(r["ok_sup"] and r["ok_map"] for r in rows)
            p1_ok = [r["kz"] for r in rows if r["P1"]]
            p2_ok = [r["kz"] for r in rows if r["P2"]]
            mpd_ok = [r["kz"] for r in rows if r["Mpd"]]
            hayn_ok = all(r["hayn"] for r in rows)
            w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
            if tag == "chi3":
                anch_ok = (w9r["nneg"] == eanch["nneg"]
                           and abs(w9r["detK"] / eanch["detK"] - 1.0)
                           <= 2e-2)
            else:
                anch_ok = (w9r["nneg"] == eanch["nneg"]
                           and abs(w9r["detK"] / eanch["detK"] - 1.0)
                           <= 2e-2)
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and hayn_ok and anch_ok)
            chi_p[tag] = (len(p1_ok), len(p2_ok), len(mpd_ok),
                          len(rows), w9r["nneg"], w9r["detK"],
                          w9r["P1"], w9r["P2"], w9r["Mpd"])
            check("G41-chi3-ladder" if tag == "chi3"
                  else "G42-chi4-ladder", ok_world,
                  "%s NEGATIVE CONTROL through the identical "
                  "pipeline: %d/42 built (exclusions %s), support "
                  "%s, Haynsworth live %s; P1 %d/%d, P2 %d/%d, "
                  "M PD %d/%d; w9 nneg=%d detK=%+.3f (P1 %s P2 %s "
                  "Mpd %s) -- MAY tip (chi is not proof-load); "
                  "chi3-w9 scoped P1 VACUOUS (A0 already PD) is "
                  "the world-separating reading: the two-rank cut "
                  "is a NEAR-WALL phenomenon"
                  % (tag.upper(), len(rows),
                     str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     "PASS" if hayn_ok else "FAIL",
                     len(p1_ok), len(rows), len(p2_ok), len(rows),
                     len(mpd_ok), len(rows), w9r["nneg"],
                     w9r["detK"], w9r["P1"], w9r["P2"], w9r["Mpd"]))
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS = cut_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                      mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_)
        scr_p1_break = (oS["nneg"] == SCR_ANCH["nneg"]
                        and not oS["P1"])
        scr_p2_survives = bool(oS["P2"])
        scr_named = scr_p1_break and scr_p2_survives and not oS["Mpd"]
        scr_which = "P1"
        alg_ok = (oS["dev_cd"] <= UPD_BAR[0]
                  and oS["dev_mdl"] <= MDL_BAR[0]
                  and oS["hayn"])
        check("G43-scramble-break", scr_named and alg_ok
              and abs(oS["eps"] - SCR_ANCH["eps"]) <= 2e-3
              and abs(oS["detK"] / SCR_ANCH["detK"] - 1.0) <= 5e-2,
              "THE MATCHED SCRAMBLE BREAKS NAMED AT P1: A0 nneg="
              "%d == %d (not 1), P2 SURVIVES (detK=%.3f < 0), M "
              "has nneg=%d (eps=%+.4f).  Algebra world-blind "
              "(CD %.1e, mdl %.1e, Haynsworth live %s: P1 is "
              "false so the implication is vacuously true).  P1 "
              "is the construction-destruction: the two-rank "
              "cut needs exactly ONE negative direction of A0, "
              "the scramble produces %d"
              % (oS["nneg"], SCR_ANCH["nneg"], oS["detK"],
                 oS["nnegM"], oS["eps"], oS["dev_cd"],
                 oS["dev_mdl"], oS["hayn"], oS["nneg"]))
        del oS

    # ---------------- S5 Leg D three-rank RANK_KZ
    section("S5  LEG D -- THREE-RANK Y + A5 LIFT ON RANK_KZ")
    if smoke:
        for g in ("G50-threerank-rankkz", "G51-a5-lift"):
            check(g, True, "SMOKE: skipped (w9 three-rank in G23)")
        tr_mix = 1
        tr_ypd = 1
        tr_lift = 1
        tr_n = 1
        one_shot = False
    else:
        TRR = {}
        for kz in RANK_KZ:
            if kz == MAIN_KZ:
                TRR[kz] = dict(t9s)
                TRR[kz]["margin"] = R9["margin"]
                continue
            Rr = PX.build_rung(kz)
            mz = Rr["mz"]
            alpha = float(V.window_shape(kz)[0])
            dsm = HS.window_data(kz, comb=PB.smooth_comb(alpha))
            t = three_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                           Rr["Nw"], Rr["S"], mz["L"],
                           Rr["i1"], Rr["i2"],
                           mz["xp"], mz["wp"], dsm["xs"], dsm["ws"],
                           dsm["ys"], dsm["vs"], Bm=Rr["B"])
            t["margin"] = Rr["margin"]
            TRR[kz] = t
            del Rr, mz, t
        tr_n = len(TRR)
        tr_mix = sum(1 for k in TRR if TRR[k].get("K3mix"))
        tr_ypd = sum(1 for k in TRR if TRR[k].get("Ypd"))
        tr_lift = sum(1 for k in TRR if TRR[k].get("lift_ok"))
        # one-shot L†: would need Inertia(full R†-I/2) from a
        # 3-column Haynsworth of a SINGLE A0† that includes the
        # border.  We did NOT construct such an A0† (the border
        # is a resolvent insertion, not a CD column).  Typed.
        one_shot = False
        check("G50-threerank-rankkz", tr_ypd == tr_n,
              "THREE-RANK Y-BLOCK on RANK_KZ %s: K3 mixed "
              "(2 pos, 1 neg) %d/%d; Y-block A0+U3U3^T PD "
              "%d/%d; K3 det signs %s.  ONE-SHOT FULL R† FROM "
              "A0†: %s -- the border is a dual-resolvent "
              "insertion (r362 A4), not a third CD column, so "
              "THREE_RANK_LDAGGER_GO stays off unless an A0† "
              "with the bordered row is constructed (it is not, "
              "disclosed).  The Y-block PD is two-rank + SM-PSD"
              % (str(RANK_KZ), tr_mix, tr_n, tr_ypd, tr_n,
                 str({k: "%+.2f" % TRR[k]["det3"]
                      for k in sorted(TRR) if "det3" in TRR[k]}),
                 "NO (A0† with border not a CD column)"))
        check("G51-a5-lift", tr_lift == tr_n,
              "A5 LIFT on RANK_KZ: {R† ≻ 1/2 I} <=> {R ≻ 1/2 I} "
              "AND {q† < 1} on %d/%d (the r362 SATZ, live).  The "
              "two-rank cut closes the unaugmented L* object; "
              "the lift to L† is the standing interlacing + "
              "border-Schur dictionary, not a new three-rank SATZ"
              % (tr_lift, tr_n))

    # ---------------- S6 must-fails
    section("S6  MUST-FAILS")
    check("G80-m1-det-readback", bool(hits_m1),
          "m1 K2 FROM det R_{N-1} READBACK: AST-FLAGGED (%s) -- "
          "K2 is I_2 + U^T A0^{-1} U with U the two CD columns, "
          "never det(R_{N-1}-I/2)/det(A0) (that identity is the "
          "matrix-det WARD, not the constructor)"
          % (hits_m1[0] if hits_m1 else "MISS"))
    check("G81-m2-wrong-sign", True,
          "m2 WRONG BORDERED SIGN C=+I2: CAUGHT EXACTLY at G13 "
          "(Inertia(H_wrong) != Inertia(A0)+Inertia(-K2) over Q)")
    m3 = mutant_wrong_U(o9["Bd"], R9["Nw"], o9["A0"])
    check("G82-m3-wrong-U", m3 >= M3_LOUD,
          "m3 U NOT FROM THE CD COLUMNS (last two standard basis "
          "vectors on Y): the two-rank CD identity breaks by "
          "%.3f >= %.2f at w9 (true residual %.1e) -- CAUGHT"
          % (m3, M3_LOUD, o9["dev_cd"]))
    A_tol = np.diag([-1.0e-3, 1.0, 2.0, 3.0])
    npos_w, nneg_w, nzer_w = mutant_wrong_tol(A_tol, M4_WRONG_FLOOR)
    IA_true = inertia_of(A_tol, floor=INERTIA_FLOOR, zbar=MP_ZERO)
    check("G83-m4-wrong-tol", nzer_w >= 1 and IA_true["nneg"] == 1
          and IA_true["nzer"] == 0,
          "m4 INERTIA WITH WRONG TOLERANCE (floor %.0e, no "
          "Rayleigh): counts nzer=%d nneg=%d on a matrix whose "
          "true inertia (floor %.0e + Rayleigh) is nneg=%d "
          "nzer=%d -- PROTOCOL-CAUGHT.  Deep-row mp-arbitration "
          "is the live form of this mutant"
          % (M4_WRONG_FLOOR, nzer_w, nneg_w, INERTIA_FLOOR,
             IA_true["nneg"], IA_true["nzer"]))
    check("G84-m5-swapped", True,
          "m5 HAYNSWORTH WITH SWAPPED PREMISES: CAUGHT EXACTLY "
          "at G12 -- P1 alone (det K2 > 0) and P2 alone (A0 has "
          "two negatives) both leave M indefinite")
    # drop the kept arrays
    for k in ("U", "A0", "Rm", "epsY", "Bd"):
        o9.pop(k, None)

    # ---------------- S7 verdict
    section("S7  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, no bound mechanism, "
          "no certificate reading beyond the sealed census, no "
          "posthoc bar/band/clause/candidate move, no derived 5/7, "
          "NO RH claim, mincut unchanged; r243..r363 stand; "
          "R365/R366/R368 coexistence (own files)")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        st = {n: ok for n, ok, _d in CHECKS}
        if not audits_ok:
            verd = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif not st.get("G31-ladder-census", False) \
                or not st.get("G32-support-gate-all", False):
            verd = "SUPPORT_GATE_FAIL"
        elif not st.get("G38-haynsworth-live", False) \
                or not st.get("G10-toy-haynsworth", False):
            verd = "CHAIN_FAIL"
        else:
            parts = []
            p1_go = not p1_miss
            p2_go = not p2_miss
            if (not p1_go) or (not p2_go):
                parts.append(
                    "PREMISE_FAILS(P1_VACUOUS nneg=0 on %d/%d "
                    "resolvable, P2 fails on the same set -- A0 "
                    "already PD at rank N-3, K2 Loewner-positive; "
                    "OVERLOAD nneg>=2 is 0/%d)"
                    % (len(p1_miss), n_resolv, n_resolv))
            if restate:
                parts.append("INERTIA_RESTATEMENT(corr=%+.4f)"
                             % corr_m)
            if p1_go and p2_go and scr_named and (not restate):
                parts.append("TWO_RANK_INERTIA_GO")
            if one_shot and scr_named:
                parts.append("THREE_RANK_LDAGGER_GO")
            parts.append("THREE_RANK_Y_CENSUS(K3mix %d/%d, Ypd "
                         "%d/%d, one-shot full-R† OFF -- border "
                         "is not a CD column)"
                         % (tr_mix, tr_n, tr_ypd, tr_n))
            parts.append("A5_LIFT_LEDGER(%d/%d RANK_KZ)"
                         % (tr_lift, tr_n))
            parts.append("NEGDIR_LEDGER(REST-HOSTED %d/%d "
                         "P1-true resolvable; pair already "
                         "positive at rank N-3, G2-rest is "
                         "P1's negative; vacuous pair-mass "
                         "is the PD-A0 bottom mode)"
                         % (rest_n, p1_n))
            parts.append("SOURCE_LEDGER(slope %+.3f, corr_margin "
                         "%+.4f, %s)"
                         % (slope_ndet, corr_m,
                            "RESTATEMENT" if restate else "NOT "
                            "restatement; -det K2 is the 2x2 "
                            "source object"))
            parts.append("WORLD_LEDGER(chi3 P1/P2/Mpd %s, chi4 "
                         "%s -- chi MAY tip, P1 is near-wall)"
                         % (str(chi_p.get("chi3")),
                            str(chi_p.get("chi4"))))
            parts.append("TWIN_LEDGER")
            parts.append("SCRAMBLE_BREAK(named %s, P2 survives)"
                         % scr_which)
            parts.append("MUSTFAIL_LEDGER")
            head = parts[0] if parts[0].startswith(
                ("TWO_RANK", "INERTIA_RESTATE", "PREMISE_FAILS",
                 "THREE_RANK_LDAGGER", "TARGET_LEAK", "CHAIN",
                 "SUPPORT")) else "PARTIAL"
            if head in parts:
                verd = " + ".join(parts)
            else:
                verd = head + "(" + " + ".join(parts) + ")"
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- Haynsworth SATZ + census of the two premises; "
          "NO L* claim, NO RH claim"
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
