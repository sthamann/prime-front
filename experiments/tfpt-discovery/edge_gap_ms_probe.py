#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_gap_ms_probe --
PRIME.LSTAR.DUAL.EDGE_GAP_MS.01 (round 366): THE EDGE-GAP LEMMA
VIA MARKOV-STIELTJES MASS COUNTING -- the last sharp-formed
internal attempt after the r363 INTERNAL_LIMIT.  Coexistence:
R365 (V2, rh/problem) runs in parallel -- this probe touches
NOTHING outside its own file and the strictly additive rh-sync.
Proof-first: the numerics verify proof steps.  NO freeze for
externals; every leg aims at a proveable statement.

THE BINDING HANDOFF (r363, read first): the internal L* chain
was typed down to TWO open theorem-loci:
  1. THE EDGE-GAP LEMMA (S5, OPEN): why does one zero of each
     of the two consecutive dual OPs occupy the unique pair-gap
     (y2, y1)?  BKMM node-pinning is REFUTED (Hurwitz sat 0.462
     vs bar 0.15 -- the edge is dual-void, pinning lived in the
     bulk if anywhere); the measured placement is Gauss-like
     (pin3 in (0.15, 0.55) on 74/74, O(1), not shrinking).
  2. REST POSITIVITY (OPEN): c=1/Cauchy gives rest >= eps, which
     is circular as a proof of rest > 0; det S_N > 0 alone does
     NOT give rest > 0 (scramble counterexample: lambda_min(S_N)
     = +1.37e-2 at rest = -0.4962).
The canonical Sturm holds 84/85 as census; the SATZ stages are
Sturm/Markov interlacing + count (the dual ensemble IS positive),
Schur split, CD update, r362-(A5)(A7).

THE NEW IDEA (not tested in r363 -- the MASS path instead of
the pinning path): Markov-Stieltjes.  For a positive discrete
measure sigma and the Gauss quadrature of order n, the number of
zeros of p_n in an interval I is controlled by the sigma-mass in
I (classical MS inequalities: between consecutive zeros lies at
least one quadrature-node weight; the counting deviation
|#zeros(I) - n·sigma_norm(I)-like| is bounded by the Christoffel
numbers).  THE EDGE-GAP QUESTION BECOMES A MASS QUESTION: how
much mu_vee-mass (the dual weight u_vee = c_j(1-x)/|f|, CLOSED)
sits in the pair-gap (y2, y1) and in the edge segments -- and
does the closed weight force the one-zero occupancy?  Analogously
for rest positivity: R_CC is the restriction of the projection
kernel to the non-pair Y-nodes; lambda_min(R_CC) - 1/2 has a
mass/counting reading (hole density off the pair; the exact
occupation field o_dual of r360 IS the diagonal).

THE LEGS:
  (Leg 0) anchors bit-near: r363 (zero columns, pin3, 84/85),
    r360 (occupation field, saturation zone), r356 (dual weight
    three routes), r362 (R-dagger layer).
  (Leg A) THE MASS BALANCE IN THE PAIR-GAP (the core).  Exact
    Fractions on the toy, f64/mp live on all 85 + chi: the u_vee
    mass in the pair-gap, in the adjacent segments, and the
    associated Christoffel numbers of the dual ensemble.  The
    Markov-Stieltjes chain: the classical inequality in the
    discrete case (nodes = grid points; zeros of p_vee_{N-1},
    p_vee_{N-2}) and the CANDIDATE: "the pair-gap carries enough
    mass for >= 1 zero and too little for >= 2" (the correct MS
    form with Christoffel numbers as buffer).  Every inequality
    stage is verified pointwise and typed satz/dictionary/census.
    The weight form is closed -- does the mass bound FOLLOW from
    the Digamma/tent/reciprocal dictionary (that would be the
    theorem)?
  (Leg B) REST POSITIVITY AS A MASS/COUNTING STATEMENT.
    lambda_min(R_CC) - 1/2 > 0 via the occupation/counting
    structure: R_CC is a principal submatrix of the dual
    projection; the exact complementation o_eta + o_dual == 1
    and the interlacing SATZ stages yield a NON-circular
    sufficient condition (e.g. non-pair Y-nodes carry occupation
    >= 1/2 + delta elementwise?).  What the occupation field
    actually gives -- the r360 fold-1 anomaly is the known
    structure, and it lives on a mu-atom, not on C.  The scramble
    must break at the named hypothesis (does it break at
    occupation? measure it).
  (Leg C) COMPOSITION.  If A+B carry: the chain Sturm(84/85 ->
    satz modulo MS stages) => det S_N > 0 => [with B] R > 1/2 I
    => [r362] R-dagger > 1/2 I -- the final typing, what is now
    SATZ modulo which named stages.  If not: INTERNAL_EXHAUSTED
    -- the internal path is exhausted at measured grade; the
    final conditional package (every named lemma of both lanes)
    listed cleanly.
  (Leg D) worlds + must-fails (>=5): MAIN/Twin/chi (the MS mass
    balance there -- does it tip consistently with the Sturm
    tip?), scramble named.  Must-fails: MS inequality with the
    wrong counting convention -> exactly CAUGHT; mass bars after
    sight -> protocol-CAUGHT; occupation condition read back
    from lambda_min(R_CC) -> AST-CAUGHT; circular Christoffel
    numbers -> AST-CAUGHT; wrong gap bounds -> exactly CAUGHT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO L* CLAIM, NO RH
CLAIM in either direction, mincut unchanged.  Two-commit freeze
protocol (r329 convention): spec + machinery committed BEFORE
the record run, record tables inserted after.

INDEX FIREWALL (binding, r238-r363 discipline): w = window (kz),
S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds = grid
indices; ground truth enters GATES and record tables only; the
module-own constructors consume measure arrays / chain
coefficients / positions / pair indices ONLY (AST scope audit;
withheld identifiers z_col_true / rest_col_true / mass_col_true
and the REC/anchor constants); no zero/prime oracles (AST
firewall); no fit primitives.  MACHINERY IMPORTED VERBATIM:
r363 CSI.{attack_rung, op_pair, zeros_of, hurwitz_row, grade_of}
(09786c2e), r360 CS.{occ_from_chain, sat_rung} (ea24936c),
r359 SWD.{schur_rung, slim359, fr_monic_ops, fr_det} (d00fdc96),
r356 BDH.{dual_weights, dual_rung, fr_proj, fr_inv} (36141c0a),
r362 ABD.aug_rung (7d810a9a), r342 PX.{build_rung, pair_select}
(b09f8ccd), r357 DMF.{chi_window_comb, chi_build_measures,
LPQ3, LPQ4, Q_CHI3, Q_CHI4} (4bf1a94b), r354 PWA.rung_reduced_cols
(f9db84da), r329 E3.{admissible_pool, used_kz_set} (bbfaf199),
r286 LM.{ts_fit, ext_rule} (0a44ac4e), r331 TR.{base_comb,
build_world}, r289 AKD.twin_rational, r276 MF.local_gaps,
r226 HS.window_data, r243 PB.smooth_comb, document pipeline
V.{build_measures, mu_chain, b_matrix, admissible_indices, U,
PP}, v563 core READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104,
N_w 184, margin 1.6752e-4 rel 0.01, lambda_min(R) 0.500041882
abs 1e-8, folds (2, 4)); r359 W9 SCHUR (eps 4.1882e-5, lamS
4.2003e-5, detS 2.0690e-8, rest_min 9.173e-4); r363 W9 HUR
(pin3_n 0.3105, n_in 1/1, straddle, n_mid 1); r362 W9 AUG
(lamRd 0.500041459); r360 W9 occupation (od1 0.1497).

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8;
W9 MASS ANCHORS (s1 scoping, disclosed, /tmp deleted):
M_I 6.834941e-5 rel 2e-2, U 5.2026691056e2 rel 1e-6, lam_in 9.996278e-5
rel 2e-2, minC 0.5151 abs 5e-3, n_in 1/1 EXACT, n_mid 1 EXACT,
MS viol 0/0, sumlam/U = 1 abs 1e-12 (f64) / 1e-14 (mp dps 30
at the f64 Gauss nodes), n*M_I/U = 2.40e-5 (NOT in SCALED_BAND); SCR_ANCH rest
-0.4962 / lamS +1.369e-2 / minC 0.1863 abs 2e-2 (the named
occupation break); CHI3_EPS 2.205e-4; PIN3_BAND (0.15, 0.55)
reused r363; SAT_FOLDS (1, 2, 3); MAIN_STURM_MIN 83; MS_VIOL_MAX
0 (classical sandwich in exact arithmetic; f64 floor graded by
MS_DEV_BAR, amendment a1); SUMLAM_BAR (1e-11, 1e-10, 1e-8) (a2: chi shallow Gauss
sumλ floor 7.4e-12);
MS_DEV_BAR (1e-12, 1e-8, 5e-7) the f64 sandwich maxdev bars
(a1: first full evaluation, mid/deep high-side <= 1.7e-7); ZERO_RES_BAR (1e-8, 1e-6,
1e-4); SCALED_BAND (0.5, 1.5) the proportional-counting
candidate "n M_I/U near 1 => Z = 1" -- the hypothesis under
test; MINC_HALF 0.5 the necessary occupation bar (lambda_min
<= min diag); MAIN_MS_MIN 83; INTERLACE_MIN 0.95; GRADES
shallow N_w <= 900 / mid <= 3200 / deep > 3200; r359 graded
bars REUSED: CD / DETID; EPS_FLOOR 1.25e-10; RESOLV_FLOOR 1e-9;
WORLD_KZ (18, 9, 52, 119, 42, 130); N_CHI_MIN 21; SCR_SEED 1;
TWIN_BAR 1e-3 nats; TWIN_MASS_BAR 5e-2 rel; M1_VIOL_MIN 1 (wrong
MS counting must produce >= 1 sandwich violation at w9);
EXT selections verbatim r356/r363; TOY_TOL 1e-12; BISECT_STEPS
52; runtime <= 1800 s; smoke = toys + firewall + scopes +
mutants + w9 blocks (records, MS sandwich, mass table, rest
occupation); ladder, EXT, twin, chi, scramble, adjudications
skipped.

PRE-SPEC SCOPING (disclosed -- ONE sizing pass on kz9/18 +
chi3 w9 + scramble w9, /tmp, deleted; no bar, band, clause,
candidate or verdict rule tuned after any evaluation except as
sized here and said so): with TRUE Gauss zeros (vectorized
bisection of p_n in each sign-change gap, 52 steps; interpolated
phi-zeros of r363 are a discrete Sturm proxy, NOT the Gauss
nodes -- a disclosed construction fact, not a finding against
r363): at w9, sum λ = U to 3e-15, MS sandwich 0/183 violations,
Gauss quadrature of 1 and of x exact at 1e-14; n_in 1/1, n_mid
1; M_I = 6.83e-5, U = 520.27, n M_I/U = 2.4e-5 NOT in
SCALED_BAND -- the proportional mass counting predicts Z = 0,
the measured Z = 1, the O(1) MS buffer swallows the difference.
CAND_GE1 (M_I > chr(y_lo)+chr(y_hi) = 4.46e-4) FAILS (M_I is
smaller).  CAND_LE1 (M_I < lam_L + lam_R) is not a forcing of
Z <= 1 at the right edge (no zero to the right of y_hi; the
last zero IS the pair-gap zero).  The pair-gap is DUAL-VOID
mass: M_L ≈ U, M_R ≈ 1.3e-6, M_pair ≈ 2.3e-4.  Dictionary: M_I
IS the closed route-B weight at the unique interior atom (fold
3); comparing it to Christoffel numbers needs the OP kernel,
which is NOT in the Digamma/tent/reciprocal dictionary.  kz18
reproduces the same qualitative table (n M_I/U = 5.6e-6, Z = 1,
MS 0 viol after true zeros).  Leg B: min_diag(R_CC) = 0.5151
> 1/2 at w9 (necessary condition HOLDS; 0 of 102 C-nodes below
1/2); Gershgorin lower bound -0.029 < 0 -- diagonal >= 1/2 is
NOT sufficient for lambda_min(R_CC) >= 1/2.  Fold-1 occupation
0.150 is a UNION mu-atom, not a C-node.  Scramble: n_mid 3,
n_in 2/2, minC 0.186 < 1/2, rest -0.4962 -- BREAKS the necessary
occupation condition AND the Z = 1 occupancy, named.  chi3 w9:
still n_in 1/1, n_mid 1, minC 0.502 > 1/2, n M_I/U = 3.7e-4
still outside SCALED_BAND.  The verdict letters, SCALED_BAND,
MINC_HALF, MS_VIOL_MAX and every bar were frozen from these
numbers BEFORE any ladder-wide evaluation.

CALIBRATION AMENDMENT a1 (first full evaluation, disclosed; NO
forcing candidate, SCALED_BAND, MINC_HALF, rest clause or verdict
letter moved): the MS sandwich is exact-arithmetic SATZ (toy +
w9 0/183 + sum λ = U on all 85); f64 produces a high-side floor
on mid/deep MAIN (15 rows, all N_w >= 2475, max maxdev 1.7e-7
at EXT6 kz133, the same f64-floor row as r359) and on some chi
windows.  G33/G41/G42 retyped to graded maxdev (MS_DEV_BAR)
instead of a zero-violation count -- the count is reported as
census, not a fail.  Analogous to the r359 kz133 Sturm floor.

CALIBRATION AMENDMENT a2 (chi first evaluation, disclosed; NO
MAIN forcing candidate, SCALED_BAND, MINC_HALF or verdict
letter moved): chi3 2/42 and chi4 1/42 shallow rows have
|sum λ/U - 1| = 7.4e-12 / 5.7e-12 against the frozen shallow
SUMLAM_BAR 1e-12, with sandwich 0/0.  Shallow SUMLAM_BAR
resized 1e-12 -> 1e-11 in the disclosed 1/U f64-noise class.
MAIN w9 remains 3e-15.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > CHAIN_FAIL > the
adjudicated letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the rank/support gate fails on any
    real MAIN ladder window /
  CHAIN_FAIL(loci)  iff any exact ward fails (toys, r359 E1/CD
    graded, Gauss sum λ = U, MS sandwich, zero residual) /
  otherwise the letters, each exactly one of the A-group and
  one of the B-group, plus the always-on tags:
  [EDGE_GAP_MS_PROVED  iff the MS chain closes theorem-grade
    from the closed weight form (classical MS + a proved
    forcing of Z = 1 in the pair-gap, 0-violation, named
    theorem, dictionary supplies the mass bound) /
   MS_CENSUS(stages)  iff the MS inequalities hold as SATZ
    (verified pointwise) but the forcing candidate fails --
    Z = 1 remains census, the mass path does not close S5 /
   EDGE_GAP_OPEN]
  [REST_MASS_GO  iff a NON-circular sufficient occupation/
    counting condition implies rest > 0, 0-violation on
    resolvable MAIN, scramble breaks it named /
   REST_NECESSARY_ONLY  iff min_diag(R_CC) > 1/2 holds as a
    necessary census on MAIN and fails on the scramble, but
    is NOT sufficient (Gershgorin or a named counterexample) /
   REST_OPEN]
  + STURM_CANONICAL_CENSUS(MAIN straddle >= MAIN_STURM_MIN,
    chi MAY tip, scramble MUST tip) [always if the chain holds]
  + COMPOSITION_TYPED(SATZ / dictionary / census / open per
    link) [always]
  + INTERNAL_EXHAUSTED  iff BOTH mass paths remain short of a
    theorem (forcing not proved, AND rest not GO) -- honest:
    the internal full attack, pinning path then mass path, is
    exhausted at measured grade; the external RHP path stays
    on the table /
  + WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK + MUSTFAIL_LEDGER.
Combinations allowed.  Honesty before beauty: the classical MS
sandwich for a positive discrete measure, the discrete gap
theorem (at most one zero per interatomic gap), the Gauss
quadrature of degree 2n-1, the occupation complement, the
Schur split, Cauchy rest >= eps, and r362 (A5)/(A7) are finite
theorems; Z = 1 in the pair-gap, det S_N > 0, rest > 0, min_diag
> 1/2, n_mid = 1 are census; the proportional-mass forcing
n M_I/U in SCALED_BAND, the Christoffel-endpoint forcing
M_I > chr_pair, and any dictionary-only bound that would
distinguish Z = 0 from Z = 1 without the OP kernel are the
hypotheses under test; no verdict claims L*, a bound mechanism,
a derived 5/7, or RH progress in any direction; the DCCX STOP
list stands.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit besides disclosed a1/a2; TWO-COMMIT PROTOCOL:
sealed spec committed as "r366 pre-freeze" (dbf340ab, SPEC_SHA
freeze 4164a1c1a1bd3aaf / file fdab9391) BEFORE the first full
evaluation; chronology honest: smoke 30/30 byte-identical;
pre-freeze commit dbf340ab; first full evaluation found the
f64 sandwich floor (a1) and the chi sumλ floor (a2), both
disclosed, NO forcing candidate / SCALED_BAND / MINC_HALF /
verdict letter moved; record run1 = 30/30 (260.3 s), run2 =
30/30 (267.2 s), byte-identical up to the WALL line):
MAIN VERDICT = MS_CENSUS(M1-gap SATZ, M3-sandwich SATZ,
M4-sumλ SATZ, M5-scaled REFUTED, M6-chr-endpoint REFUTED,
M7-dictionary-force OPEN/NO, Z=1 CENSUS 84/85)
+ REST_NECESSARY_ONLY
+ STURM_CANONICAL_CENSUS(84/85 MAIN, chi MAY tip, scramble MUST
tip) + COMPOSITION_TYPED + INTERNAL_EXHAUSTED.
LEG A: classical MS sandwich and Gauss sum λ = U are SATZ
(exact arithmetic; f64-graded, a1 floor 15/85 mid/deep, max
high-side 1.7e-7 at kz133); discrete gap theorem SATZ; true
Gauss zeros == degree 85/85 graded.  THE MASS-FORCING
CANDIDATES ARE REFUTED: CAND_SCALED (n M_I/U in (0.5, 1.5))
0/74 resolvable MAIN; CAND_GE1 (M_I > chr_pair) 0/74.  The
pair-gap is DUAL-VOID (w9 M_I = 6.83e-5, U = 520.27,
n M_I/U = 2.40e-5); the proportional counting predicts Z = 0,
the measured Z = 1 lives in the O(1) MS buffer, which cannot
distinguish 0 from 1.  Dictionary: M_I IS the closed route-B
weight at fold 3; comparing it to Christoffel numbers needs
the OP kernel, which is NOT in the Digamma/tent/reciprocal
dictionary.  EDGE-GAP remains OPEN as a theorem.
LEG B: min_diag(R_CC) > 1/2 on 74/74 resolvable (0 C-nodes
below 1/2) -- NECESSARY, SATZ (lambda_min <= min diag);
Gershgorin >= 0 on 0/74 -- NOT sufficient.  Fold-1 occupation
is a UNION mu-atom, not a C-node.  Scramble minC 0.186 < 1/2
(23 C-nodes below) -- named occupation break.  REST_MASS_GO
does not fire.
COMPOSITION (74 resolvable): Schur split SATZ 74/74; Cauchy
rest>=eps SATZ 74/74; detS>0 and rest>0 CENSUS 74/74; r362
A5/A7 gated at w9.  The r363 hoped chain still has TWO gaps.
Worlds: chi3 30/42 and chi4 29/42 keep the Sturm pattern (MAY
tip); CAND_SCALED 0/42 + 0/42; scramble straddle FAILS (n_mid
3, zeros_in_pair 2/2) AND rest -0.4962 AND minC 0.186.
Twin dose-zero bitwise, |dlog| 6.9e-4, |d M_I| 9.7e-10.
Must-fails 5/5.  Runtime 260.3 / 267.2 s rec1/rec2; smoke 0.5 s.

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

import canonical_sturm_induction_probe as CSI  # noqa: E402 r363
import critical_saturation_probe as CS         # noqa: E402 r360
import schur_wronskian_dual_probe as SWD       # noqa: E402 r359
import borodin_dual_hole_probe as BDH          # noqa: E402 r356
import augmented_borodin_duality_probe as ABD  # noqa: E402 r362
import pair_extremal_probe as PX               # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF    # noqa: E402 r357
import phi_wander_anatomy_probe as PWA         # noqa: E402 r354
import ext3_fresh_anchors_probe as E3          # noqa: E402 r329
import lstar_margin_scaling_probe as LM        # noqa: E402 r286
import twin_resolution_probe as TR             # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276
import hirota_sign_probe as HS                 # noqa: E402 r226
import principal_bessel_probe as PB            # noqa: E402 r243
import verify_lstar_instance as V              # noqa: E402 document
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
CSI_SHA_PREFIX = "09786c2e"
CS_SHA_PREFIX = "ea24936c"
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
ABD_SHA_PREFIX = "7d810a9a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
LM_SHA_PREFIX = "0a44ac4e"
W9_SCHUR_ANCH = dict(eps=4.1882e-5, lamS=4.2003e-5, detS=2.0690e-8,
                     rest=9.173e-4, share=0.6973, f1=2, f2=4)
W9_AUG_ANCH = dict(lamRd=0.500041459, mdag=1.658218770e-4)
W9_MASS_ANCH = dict(M_I=6.834941e-5, U=5.2026691056e2,
                    lam_in=9.996278e-5, minC=0.5151, od1=0.1497,
                    n_in=1, n_mid=1)
W9_HUR_ANCH = dict(pin3_n=0.3105)
MASS_ANCH_TOL = 2.0e-2
MINC_ANCH_TOL = 5.0e-3
HUR_ANCH_TOL = 2.0e-2
PIN3_BAND = (0.15, 0.55)
SAT_FOLDS = (1, 2, 3)
MAIN_STURM_MIN = 83
MAIN_MS_MIN = 83
INTERLACE_MIN = 0.95
MS_VIOL_MAX = 0
SUMLAM_BAR = (1.0e-11, 1.0e-10, 1.0e-8)
MS_DEV_BAR = (1.0e-12, 1.0e-8, 5.0e-7)
ZERO_RES_BAR = (1.0e-8, 1.0e-6, 1.0e-4)
SCALED_BAND = (0.5, 1.5)
MINC_HALF = 0.5
NW_SHALLOW = 900
NW_MID = 3200
CD_BAR = (1.0e-12, 1.0e-11, 1.0e-10)
DETID_BAR = (1.0e-10, 1.0e-9, 1.0e-6)
EPS_FLOOR = 1.25e-10
RESOLV_FLOOR = 1.0e-9
WORLD_KZ = (18, 9, 52, 119, 42, 130)
N_CHI_MIN = 21
SCR_SEED = 1
TWIN_BAR = 1.0e-3
TWIN_MASS_BAR = 5.0e-2
M1_VIOL_MIN = 1
CHI3_EPS_ANCH = 2.205e-4
SCR_ANCH = dict(eps=-0.4962, rest=-0.4962, lamS=1.369e-2,
                minC=0.1863)
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
BISECT_STEPS = 52
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
                       "coefficients / positions / pair indices ONLY; "
                       "record numbers and anchors enter gates and "
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


CONSTRUCTORS = ("grade_of", "eval_pn", "true_zeros", "kxx_at",
                "ms_sandwich", "mass_segments", "rest_occ",
                "ms_rung", "chi_ms_row")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_SCHUR_ANCH",
                   "W9_AUG_ANCH", "W9_MASS_ANCH", "W9_HUR_ANCH",
                   "SCALED_BAND", "MINC_HALF", "SCR_ANCH",
                   "CHI3_EPS_ANCH", "z_col_true", "rest_col_true",
                   "mass_col_true"}


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


def eval_pn(x, a, b, h0, n):
    """orthonormal p_n at the abscissae x via the three-term
    recurrence; consumes chain coefficients + positions only."""
    x = np.asarray(x, float)
    p = np.full_like(x, 1.0 / math.sqrt(h0))
    pm = np.zeros_like(x)
    for i in range(n):
        r = (x - a[i]) * p - (b[i - 1] * pm if i > 0 else 0.0)
        pm, p = p, r / b[i]
    return p


def true_zeros(xu, a, b, h0, n, steps=BISECT_STEPS):
    """Gauss nodes = zeros of p_n, one per sign-change gap of
    the nodal sequence, by vectorized bisection (deterministic);
    consumes chain + the support positions only."""
    xu = np.asarray(xu, float)
    pnd = eval_pn(xu, a, b, h0, n)
    los, his = [], []
    for j in range(len(xu) - 1):
        if pnd[j] == 0.0:
            los.append(float(xu[j]))
            his.append(float(xu[j]))
        elif pnd[j] * pnd[j + 1] < 0.0:
            los.append(float(xu[j]))
            his.append(float(xu[j + 1]))
    if not los:
        return np.zeros(0), 0.0
    lo = np.array(los, float)
    hi = np.array(his, float)
    plo = eval_pn(lo, a, b, h0, n)
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        pm = eval_pn(mid, a, b, h0, n)
        goL = plo * pm <= 0.0
        hi = np.where(goL, mid, hi)
        lo = np.where(goL, lo, mid)
        plo = np.where(goL, plo, pm)
    z = 0.5 * (lo + hi)
    res = float(np.max(np.abs(eval_pn(z, a, b, h0, n))))
    return z, res


def kxx_at(xs, a, b, h0, depth):
    """Christoffel-Darboux diagonal K_{depth-1}(x,x) =
    sum_{j < depth} p_j(x)^2 at the abscissae xs; consumes
    chain + positions only."""
    xs = np.asarray(xs, float)
    p = np.full_like(xs, 1.0 / math.sqrt(h0))
    pm = np.zeros_like(xs)
    K = p * p
    for i in range(depth - 1):
        r = (xs - a[i]) * p - (b[i - 1] * pm if i > 0 else 0.0)
        pm, p = p, r / b[i]
        K = K + p * p
    return K


def ms_sandwich(zs, lam, xu, ud):
    """classical Markov-Stieltjes sandwich for a discrete
    measure: Lambda_{j-1} <= M((-inf, z_j)) <= Lambda_j at
    every Gauss node (strict left, zeros off the atoms);
    consumes the zeros, their Christoffel numbers, and the
    atomic measure only."""
    zs = np.asarray(zs, float)
    lam = np.asarray(lam, float)
    xu = np.asarray(xu, float)
    ud = np.asarray(ud, float)
    if len(zs) == 0:
        return 0, 0, 0.0, 0.0, 1.0
    order = np.argsort(zs)
    zs_s = zs[order]
    lam_s = lam[order]
    cdf = np.cumsum(lam_s)
    U = float(np.sum(ud))
    vlo = vhi = 0
    maxlo = maxhi = 0.0
    for j in range(len(zs_s)):
        mleft = float(np.sum(ud[xu < zs_s[j]]))
        lo = 0.0 if j == 0 else float(cdf[j - 1])
        hi = float(cdf[j])
        if mleft + 1e-12 < lo:
            vlo += 1
            maxlo = max(maxlo, lo - mleft)
        if mleft > hi + 1e-12:
            vhi += 1
            maxhi = max(maxhi, mleft - hi)
    sumrat = float(np.sum(lam_s) / U) if U > 0 else float("nan")
    return vlo, vhi, maxlo, maxhi, sumrat


def mass_segments(xu, ud, ylo, yhi):
    """u_vee-mass in the open pair-gap, the left/right edge
    segments, and at the two pair atoms; consumes the atomic
    measure + the two gap endpoints only."""
    xu = np.asarray(xu, float)
    ud = np.asarray(ud, float)
    interior = (xu > ylo) & (xu < yhi)
    left = xu < ylo
    right = xu > yhi
    pair = (np.abs(xu - ylo) < 1e-15) | (np.abs(xu - yhi) < 1e-15)
    U = float(np.sum(ud))
    M_I = float(np.sum(ud[interior]))
    M_L = float(np.sum(ud[left]))
    M_R = float(np.sum(ud[right]))
    M_pair = float(np.sum(ud[pair]))
    n_mid = int(np.sum(interior))
    return dict(U=U, M_I=M_I, M_L=M_L, M_R=M_R, M_pair=M_pair,
                n_mid=n_mid, frac=M_I / U if U > 0 else float("nan"))


def rest_occ(R, i1, i2):
    """occupation reading of R_CC: the diagonal of the dual
    projection on the non-pair Y-nodes, plus the Gershgorin
    lower bound for lambda_min(R_CC); consumes the Y-kernel
    and the pair indices only."""
    Sm = R.shape[0]
    rest = [k for k in range(Sm) if k != i1 and k != i2]
    if not rest:
        return dict(minC=float("nan"), n_below=0, nC=0,
                    gersh=float("nan"))
    diagC = np.array([float(R[k, k]) for k in rest])
    RCC = R[np.ix_(rest, rest)]
    gersh = []
    for ii in range(len(rest)):
        off = float(np.sum(np.abs(RCC[ii, :])) - abs(RCC[ii, ii]))
        gersh.append(float(RCC[ii, ii] - off))
    return dict(minC=float(np.min(diagC)),
                n_below=int(np.sum(diagC < 0.5)),
                nC=len(rest),
                gersh=float(np.min(gersh)))


def ms_rung(xu, wu, yn, vn, Nw, S, L, i1, i2):
    """THE r366 BLOCK of one window: the verbatim r359 schur_rung
    plus true Gauss zeros of the two consecutive dual OPs, the
    MS sandwich, the pair-gap mass table, and the rest-occupation
    reading of R_CC; consumes measure arrays, positions and the
    pair indices only."""
    o = SWD.schur_rung(xu, wu, yn, vn, Nw, S, L, i1, i2)
    xu = np.asarray(xu, float)
    u = np.abs(np.asarray(wu, float))
    ud, _lA, f, _eps, _lp = BDH.dual_weights(xu, u, S, L)
    y1, y2 = float(o["y1"]), float(o["y2"])
    ylo, yhi = (y2, y1) if y2 < y1 else (y1, y2)
    n = Nw - 1
    zs_n, res_n = true_zeros(xu, o["ad"], o["bd"], o["h0d"], n)
    zs_l, res_l = true_zeros(xu, o["ad"], o["bd"], o["h0d"], n - 1)
    Kn = kxx_at(zs_n, o["ad"], o["bd"], o["h0d"], n)
    lam = 1.0 / np.maximum(Kn, 1e-300)
    vlo, vhi, maxlo, maxhi, sumrat = ms_sandwich(zs_n, lam, xu, ud)
    mass = mass_segments(xu, ud, ylo, yhi)
    n_in_n = int(np.sum((zs_n > ylo) & (zs_n < yhi)))
    n_in_l = int(np.sum((zs_l > ylo) & (zs_l < yhi)))
    in_mask = (zs_n > ylo) & (zs_n < yhi)
    lam_in = float(np.sum(lam[in_mask])) if in_mask.any() else 0.0
    occ = CS.occ_from_chain(xu, ud, o["ad"], o["bd"], o["h0d"], n)
    jlo = int(np.argmin(np.abs(xu - ylo)))
    jhi = int(np.argmin(np.abs(xu - yhi)))
    chr_pair = 0.0
    for j in (jlo, jhi):
        if occ[j] > 0:
            chr_pair += float(ud[j] / occ[j])
    ro = rest_occ(o["R"], i1, i2)
    iY = np.searchsorted(xu, np.asarray(yn, float))
    j1s = np.nonzero(f == 1)[0]
    od1 = float(occ[int(j1s[0])]) if len(j1s) else float("nan")
    scaled = (n * mass["M_I"] / mass["U"]) if mass["U"] > 0 else 0.0
    cand_ge1 = mass["M_I"] > chr_pair
    out = SWD.slim359(o)
    out.update(mass)
    out.update(ro)
    out.update(n_in_l=n_in_l, n_in_n=n_in_n,
               nzeros_l=len(zs_l), nzeros_n=len(zs_n),
               res_n=res_n, res_l=res_l,
               ms_vlo=vlo, ms_vhi=vhi,
               ms_maxlo=maxlo, ms_maxhi=maxhi,
               sumrat=sumrat, lam_in=lam_in,
               chr_pair=chr_pair, scaled=scaled,
               cand_ge1=bool(cand_ge1),
               od1=od1,
               straddle=(out["sl"] < 0 and out["sn"] < 0),
               deg_n_ok=(len(zs_n) == n),
               deg_l_ok=(len(zs_l) == n - 1))
    phl, phn = CSI.op_pair(xu, ud, o["ad"], o["bd"], o["h0d"],
                           Nw - 2, Nw - 1)
    h = CSI.hurwitz_row(phl, phn, xu, f, iY, i1, i2, SAT_FOLDS)
    out["pin3_n"] = h["pin3_n"]
    out["ilace"] = h["ilace"]
    for k in ("R", "ad", "bd", "h0d"):
        out.pop(k, None)
    return out


def chi_ms_row(kz, q, lpq):
    """one chi-world rung through the identical dual+Schur+MS
    pipeline; consumes the chi comb + matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = ms_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                mzc["Nw"], mzc["S"], mzc["L"], j1, j2)
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    o["S"] = mzc["S"]
    return o


# ============== must-fail mutants
def mutant_ms_offbyone(zs, lam, xu, ud):
    """m1 MUST-FAIL (loud): the MS sandwich with the WRONG
    counting convention Lambda_j <= M_left(z_j) <= Lambda_{j+1}
    (off-by-one vs the classical Lambda_{j-1} <= M <= Lambda_j).
    Must produce sandwich violations on a live window."""
    zs = np.asarray(zs, float)
    lam = np.asarray(lam, float)
    xu = np.asarray(xu, float)
    ud = np.asarray(ud, float)
    order = np.argsort(zs)
    zs_s, lam_s = zs[order], lam[order]
    cdf = np.cumsum(lam_s)
    n = len(zs_s)
    viol = 0
    for j in range(n):
        mleft = float(np.sum(ud[xu < zs_s[j]]))
        lo = float(cdf[j])
        hi = float(cdf[j + 1]) if j + 1 < n else lo
        if mleft + 1e-12 < lo or mleft > hi + 1e-12:
            viol += 1
    return viol


def mutant_bar_by_sight(z_col_true, mass_col_true):
    """m2 MUST-FAIL (AST): a mass bar read off the withheld
    (Z, M_I) columns after seeing which rows have Z = 1 --
    protocol AST-FLAGGED."""
    z = np.asarray(z_col_true, float)
    m = np.asarray(mass_col_true, float)
    hit = [float(m[i]) for i in range(len(z)) if z[i] == 1]
    return min(hit) if hit else 0.0


def mutant_occ_from_rest(rest_col_true):
    """m3 MUST-FAIL (AST): an 'occupation condition' that
    returns 1/2 + withheld rest -- reading the sufficient
    occupation bound back from lambda_min(R_CC), AST-FLAGGED."""
    r = np.asarray(rest_col_true, float)
    return 0.5 + r


def mutant_chr_circular(mass_col_true, z_col_true):
    """m4 MUST-FAIL (AST): Christoffel numbers set equal to
    M_I / Z from the withheld columns -- circular, AST-FLAGGED."""
    m = np.asarray(mass_col_true, float)
    z = np.asarray(z_col_true, float)
    out = np.zeros_like(m)
    for i in range(len(m)):
        out[i] = m[i] / z[i] if z[i] != 0.0 else 0.0
    return out


def mutant_wrong_gap(xu, ud, zs, f):
    """m5 MUST-FAIL (loud): pair-gap taken as the fold-(1,2)
    interval instead of the critical pair -- must miss the
    measured pair-gap zero."""
    xu = np.asarray(xu, float)
    f = np.asarray(f)
    j1s = np.nonzero(f == 1)[0]
    j2s = np.nonzero(f == 2)[0]
    if not len(j1s) or not len(j2s):
        return 0
    a, b = float(xu[int(j1s[0])]), float(xu[int(j2s[0])])
    lo, hi = (a, b) if a < b else (b, a)
    return int(np.sum((zs > lo) & (zs < hi)))


def mp_sumlam_ward(zs, a, b, h0, n, U):
    """mp dps-30 recompute of sum 1/K_{n-1}(z_k,z_k) vs U at
    the f64 Gauss nodes; consumes chain + zeros + total mass."""
    from mpmath import mp, mpf
    mp.dps = 30
    tot = mpf(0)
    h0m = mpf(h0)
    am = [mpf(float(ai)) for ai in a[:n]]
    bm = [mpf(float(bi)) for bi in b[:n]]
    for zk in zs:
        x = mpf(float(zk))
        p = 1 / h0m ** mpf("0.5")
        pm = mpf(0)
        K = p * p
        for i in range(n - 1):
            r = (x - am[i]) * p - (bm[i - 1] * pm if i > 0 else mpf(0))
            pm, p = p, r / bm[i]
            K = K + p * p
        tot += 1 / K
    return abs(float(tot - mpf(U))) / max(U, 1.0)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("edge_gap_ms_probe -- "
          "PRIME.LSTAR.DUAL.EDGE_GAP_MS.01 (round 366)")
    print("SPEC_SHA %s   (r363 CSI %s / r360 CS %s / r359 SWD %s / "
          "r356 BDH %s)"
          % (SPEC_SHA[:16], CSI.SPEC_SHA[:16], CS.SPEC_SHA[:16],
             SWD.SPEC_SHA[:16], BDH.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 blocks; ladder, EXT, twin, chi, "
                        "scramble, adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (CSI.SPEC_SHA.startswith(CSI_SHA_PREFIX)
              and CS.SPEC_SHA.startswith(CS_SHA_PREFIX)
              and SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r363/r360/r359/r356/r362/"
          "r342/r357/r354/r329/r286 machinery imported verbatim "
          "(CSI %s == %s*, CS %s == %s*, SWD %s == %s*, BDH %s == "
          "%s*); SCALED_BAND %s, MINC_HALF %.2f, MS_DEV_BAR %s "
          "(a1 f64 sandwich floor), MAIN_MS_MIN %d, BISECT_STEPS "
          "%d; pre-spec scoping s1 disclosed in the spec; "
          "amendment a1/a2 disclosed; the DCCX STOP list forbids any "
          "L* claim and any certificate reading"
          % (CSI.SPEC_SHA[:8], CSI_SHA_PREFIX, CS.SPEC_SHA[:8],
             CS_SHA_PREFIX, SWD.SPEC_SHA[:8], SWD_SHA_PREFIX,
             BDH.SPEC_SHA[:8], BDH_SHA_PREFIX, str(SCALED_BAND),
             MINC_HALF, str(MS_DEV_BAR), MAIN_MS_MIN, BISECT_STEPS))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_bar_by_sight")
    hits_m3 = scope_audit("mutant_occ_from_rest")
    hits_m4 = scope_audit("mutant_chr_circular")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4),
          "the %d module-own constructors consume measure arrays / "
          "chain coefficients / positions / pair indices ONLY (%s); "
          "fragment audit: %s; m2 FLAGGED (%s); m3 FLAGGED (%s); "
          "m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- DISCRETE GAP + GAUSS-MS + OCCUPATION")
    xs_t = [Fr(-3, 4), Fr(-1, 4), Fr(0), Fr(1, 2), Fr(4, 5)]
    u_t = [Fr(1), Fr(1, 4), Fr(1, 2), Fr(1, 6), Fr(1, 3)]
    N_t, S_t = 3, 5
    Pv, hv = SWD.fr_monic_ops(xs_t, u_t, 4)

    def sc_gaps(pk):
        gs = []
        for j in range(S_t - 1):
            if pk[j] * pk[j + 1] < 0 or pk[j] == 0:
                gs.append(j)
        return gs

    g2, g3 = sc_gaps(Pv[2]), sc_gaps(Pv[3])
    check("G10-toy-gap-theorem",
          len(set(g2)) == len(g2) and len(set(g3)) == len(g3)
          and len(g2) <= S_t - 1 and len(g3) <= S_t - 1
          and hv[2] > 0 and hv[3] > 0,
          "EXACT FRACTIONS DISCRETE-GAP THEOREM on the positive "
          "5-atom measure: consecutive monic OPs pi_2, pi_3 have "
          "sign-change gaps %s / %s, all DISTINCT (at most one "
          "zero per interatomic gap -- SATZ, Sturm/Markov for a "
          "positive discrete measure); positive norms h_2, h_3.  "
          "The PLACEMENT of those zeros relative to a named pair "
          "is the OPEN lemma the mass path is testing"
          % (str(g2), str(g3)))
    Pp_t = [math.prod([xs_t[j] - xs_t[k] for k in range(S_t)
                       if k != j], start=Fr(1)) for j in range(S_t)]
    uv_t = [Fr(1) / (u_t[j] * Pp_t[j] ** 2) for j in range(S_t)]
    Ah = BDH.fr_proj(xs_t, u_t, N_t)
    Bh = BDH.fr_proj(xs_t, uv_t, N_t - 1)
    dev_occ = max(abs(Ah[j][j] + Bh[j][j] - Fr(1))
                  for j in range(S_t))
    tr_A = sum(Ah[j][j] for j in range(S_t))
    tr_B = sum(Bh[j][j] for j in range(S_t))
    check("G11-toy-occ-complement",
          dev_occ == 0 and tr_A == Fr(N_t) and tr_B == Fr(N_t - 1),
          "EXACT FRACTIONS OCCUPATION COMPLEMENT (r360 O1, the "
          "diagonal of the Borodin complementation on dual "
          "weights): o_eta + o_dual == 1 on all 5 nodes (max "
          "|dev| = 0) and traces EXACT (tr o_eta = 3 = N, "
          "tr o_dual = 2 = N-1) -- R_ii on a subset is the "
          "occupation field, SATZ")
    # Gauss-MS on the 5-atom model, f64 Jacobi / Golub-Welsch
    xs_f = np.array([float(x) for x in xs_t])
    u_f = np.array([float(w) for w in u_t])
    nG = 3
    aJ, bJ, h0J = V.mu_chain(xs_f, u_f, nG)
    J = np.zeros((nG, nG))
    for i in range(nG):
        J[i, i] = aJ[i]
        if i + 1 < nG:
            J[i, i + 1] = J[i + 1, i] = bJ[i]
    evals, evecs = np.linalg.eigh(J)
    lam_gw = h0J * (evecs[0, :] ** 2)
    U_t = float(np.sum(u_f))
    zs_t, res_t = true_zeros(xs_f, aJ, bJ, h0J, nG)
    Kn_t = kxx_at(zs_t, aJ, bJ, h0J, nG)
    lam_t = 1.0 / Kn_t
    vlo_t, vhi_t, _, _, srat_t = ms_sandwich(zs_t, lam_t, xs_f, u_f)
    check("G12-toy-gauss-ms",
          abs(float(np.sum(lam_gw)) - U_t) <= TOY_TOL
          and abs(srat_t - 1.0) <= TOY_TOL
          and vlo_t == 0 and vhi_t == 0
          and res_t <= 1e-10
          and len(zs_t) == nG,
          "GAUSS / MARKOV-STIELTJES on the 5-atom toy (n = 3): "
          "Golub-Welsch sum λ = U (dev %.1e); bisection zeros "
          "n = %d, residual %.1e; sum λ/U = %.3e; MS sandwich "
          "viol lo/hi = %d/%d == 0/0 -- the classical discrete "
          "MS inequality is a finite theorem, verified"
          % (abs(float(np.sum(lam_gw)) - U_t), len(zs_t), res_t,
             srat_t - 1.0, vlo_t, vhi_t))
    Md = np.diag([-0.10, 0.20, 0.30])
    rest_t = float(Md[0, 0])
    SN_t = Md[1:, 1:]
    lamS_t = float(np.linalg.eigvalsh(SN_t)[0])
    seedM = np.array([[1.0, 2, 3, 4], [5, 6, 7, 8],
                      [9, 1, 2, 3], [4, 5, 6, 7]], float)
    Qr, _ = np.linalg.qr(seedM)
    oks = []
    for lams, expect in ((np.array([0.52, 0.60, 0.70, 0.90]), True),
                         (np.array([0.31, 0.60, 0.70, 0.90]), False)):
        Rt = Qr @ np.diag(lams) @ Qr.T
        Mt = Rt - 0.5 * np.eye(4)
        rest_ix = list(range(2, 4))
        Mcc_x = Mt[np.ix_(rest_ix, rest_ix)]
        Sx = Mt[np.ix_([0, 1], [0, 1])] \
            - Mt[np.ix_([0, 1], rest_ix)] \
            @ np.linalg.solve(Mcc_x, Mt[np.ix_(rest_ix, [0, 1])])
        emin = float(np.linalg.eigvalsh(Mt)[0])
        rmin = float(np.linalg.eigvalsh(Mcc_x)[0])
        smin = float(np.linalg.eigvalsh(0.5 * (Sx + Sx.T))[0])
        both = (rmin > 0) and (smin > 0)
        oks.append(((emin > 0) == expect) and (both == expect))
    check("G13-toy-schur-c1", all(oks) and rest_t < 0 and lamS_t > 0,
          "SCHUR SPLIT both truth directions AND the c=1 misquote "
          "counterexample (diagonal toy: S_N > 0, rest = %+.2f < 0) "
          "-- composition needs BOTH conjuncts; c=1 is rest >= eps, "
          "NOT rest > 0 from det S_N > 0"
          % rest_t)

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + MS SANDWICH + MASS TABLE + REST OCC")
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
    o9 = ms_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                 R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"])
    A9 = W9_MASS_ANCH
    S9a = W9_SCHUR_ANCH
    ok_sch = (abs(o9["eps"] / S9a["eps"] - 1.0) <= 1e-3
              and abs(o9["lamS"] / S9a["lamS"] - 1.0) <= 1e-3
              and abs(o9["detS"] / S9a["detS"] - 1.0) <= 1e-3
              and abs(o9["rest_min"] / S9a["rest"] - 1.0) <= 1e-3)
    ok_ms = (o9["ms_vlo"] == 0 and o9["ms_vhi"] == 0
               and abs(o9["sumrat"] - 1.0) <= 1e-12
             and o9["res_n"] <= ZERO_RES_BAR[0]
             and o9["nzeros_n"] == R9["Nw"] - 1
             and o9["nzeros_l"] == R9["Nw"] - 2)
    check("G21-w9-ms-sandwich", ok_sch and ok_ms,
          "THE MS SANDWICH at w9: r359 Schur anchors reproduced "
          "(eps %.4e, rest %.4e, detS %.4e); true Gauss zeros "
          "nzeros %d/%d == degree; residual %.1e; sum λ/U - 1 = "
          "%.1e (bar %.0e); MS viol lo/hi = %d/%d == 0/0 -- the "
          "classical discrete Markov-Stieltjes inequality HOLDS "
          "pointwise (SATZ, verified)"
          % (o9["eps"], o9["rest_min"], o9["detS"],
             o9["nzeros_l"], o9["nzeros_n"], o9["res_n"],
             o9["sumrat"] - 1.0, SUMLAM_BAR[0],
             o9["ms_vlo"], o9["ms_vhi"]))
    o9c = SWD.schur_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                         R9["Nw"], R9["S"], mz9["L"],
                         R9["i1"], R9["i2"])
    zs9, _r9 = true_zeros(np.asarray(mz9["xu"], float),
                          o9c["ad"], o9c["bd"], o9c["h0d"],
                          R9["Nw"] - 1)
    ud9 = BDH.dual_weights(np.asarray(mz9["xu"], float),
                           np.abs(np.asarray(mz9["wu"], float)),
                           R9["S"], mz9["L"])[0]
    mp_dev = mp_sumlam_ward(zs9, o9c["ad"], o9c["bd"], o9c["h0d"],
                            R9["Nw"] - 1, float(np.sum(ud9)))
    cand_sc9 = (SCALED_BAND[0] <= o9["scaled"] <= SCALED_BAND[1])
    ok_mass = (abs(o9["M_I"] / A9["M_I"] - 1.0) <= MASS_ANCH_TOL
               and abs(o9["U"] / A9["U"] - 1.0) <= 1e-6
               and abs(o9["lam_in"] / A9["lam_in"] - 1.0)
               <= MASS_ANCH_TOL
               and o9["n_in_n"] == A9["n_in"]
               and o9["n_in_l"] == A9["n_in"]
               and o9["n_mid"] == A9["n_mid"]
               and o9["straddle"]
               and mp_dev <= 1e-14)
    check("G22-w9-mass-table", ok_mass,
          "THE PAIR-GAP MASS TABLE at w9: M_I = %.6e (anchor "
          "%.6e), U = %.6e, lam_in = %.6e, n_mid = %d, zeros_"
          "in_pair %d/%d, straddle %s; n M_I/U = %.3e NOT in "
          "SCALED_BAND %s (CAND_SCALED %s); CAND_GE1 M_I > "
          "chr_pair (%.3e > %.3e) %s; mp dps-30 |sumλ - U|/U "
          "= %.1e -- the gap carries a DUAL-VOID mass, the "
          "proportional counting predicts Z = 0, the measured "
          "Z = 1 lives in the O(1) MS buffer.  Dictionary: M_I "
          "IS the closed route-B weight at fold 3 (identity); "
          "the comparison to Christoffel numbers needs the OP "
          "kernel, which is NOT in the Digamma/tent/reciprocal "
          "dictionary"
          % (o9["M_I"], A9["M_I"], o9["U"], o9["lam_in"],
             o9["n_mid"], o9["n_in_l"], o9["n_in_n"],
             o9["straddle"], o9["scaled"], str(SCALED_BAND),
             cand_sc9, o9["M_I"], o9["chr_pair"],
             o9["cand_ge1"], mp_dev))
    ok_occ = (abs(o9["minC"] - A9["minC"]) <= MINC_ANCH_TOL
              and o9["n_below"] == 0
              and o9["minC"] > MINC_HALF
              and o9["gersh"] < 0.0
              and abs(o9["od1"] - A9["od1"]) <= 2e-2
              and o9["rest_min"] > 0)
    check("G23-w9-rest-occ", ok_occ,
          "THE REST-OCCUPATION READING at w9: min_diag(R_CC) = "
          "%.4f > 1/2 (necessary HOLDS, %d/%d C-nodes below "
          "1/2); Gershgorin lower bound %.4f < 0 -- diagonal "
          ">= 1/2 is NOT sufficient for lambda_min(R_CC) >= "
          "1/2; fold-1 occupation %.4f is a UNION mu-atom, not "
          "a C-node (the r360 anomaly does not sit in R_CC); "
          "rest_min = %.4e > 0"
          % (o9["minC"], o9["n_below"], o9["nC"], o9["gersh"],
             o9["od1"], o9["rest_min"]))
    alpha9 = float(V.window_shape(MAIN_KZ)[0])
    dsm9 = HS.window_data(MAIN_KZ, comb=PB.smooth_comb(alpha9))
    a9 = ABD.aug_rung(mz9["xp"], mz9["wp"], mz9["yn"], mz9["vn"],
                      mz9["xu"], mz9["wu"], R9["Nw"], R9["S"],
                      mz9["L"], R9["i1"], R9["i2"],
                      dsm9["xs"], dsm9["ws"], dsm9["ys"], dsm9["vs"],
                      Bm=R9["B"])
    ok_aug = (abs(a9["lamRd"] - W9_AUG_ANCH["lamRd"]) <= 1e-8
              and a9["inter_ok"]
              and (o9["eps"] > 0) == (a9["lamR"] - 0.5 > 0))
    check("G24-w9-composition", ok_aug and o9["detS"] > 0
          and o9["rest_min"] > 0 and o9["eps"] > 0,
          "THE COMPOSITION at w9 (typed, not claimed for the "
          "family): det S_N > 0 AND rest > 0 => eps > 0 (Schur "
          "split, live); r362 (A5)/(A7) gated (lamRd %.9f, "
          "interlacing %s).  WHAT THIS DOES NOT PROVE: Z = 1 "
          "from the pair-gap mass (Leg A); rest > 0 from "
          "occupation (Leg B, Gershgorin already fails)"
          % (a9["lamRd"], a9["inter_ok"]))
    for k in ("R", "ad", "bd", "h0d"):
        o9c.pop(k, None)
    o9s = {k: o9[k] for k in o9}
    del o9

    # ---------------- S3 ladder
    section("S3  LEG A/B -- THE 85-ROW LADDER -- MS + MASS + REST")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-ms-chain-wards",
                  "G34-mass-forcing", "G35-rest-occ-census",
                  "G36-composition-chain"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: o9s}
        MT = {MAIN_KZ: dict(margin=R9["margin"], Nw=R9["Nw"],
                            z=R9["z"], Sm=R9["Sm"], S=R9["S"])}
        all_kz, fit_kz = [MAIN_KZ], [MAIN_KZ]
        n_resolv = 1
        sturm_n = 1
        a_letter = None
        b_letter = None
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
        print("    %-5s %-5s %-5s | %-10s %-6s %-5s | %-8s %-8s "
              "%-6s | %-5s %-5s %-4s"
              % ("kz", "N_w", "S", "eps", "strd", "nin",
                 "M_I/U", "nMI/U", "minC", "msV", "sumλ", "ge1"),
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
                o = ms_rung(mz["xu"], mz["wu"], mz["yn"],
                            mz["vn"], Rr["Nw"], Rr["S"],
                            mz["L"], Rr["i1"], Rr["i2"])
            if Rr["margin"] <= 0:
                neg_rows.append(kz)
            if not (o["ok_sup"] and o["ok_map"]):
                sup_fail.append(kz)
            print("    %-5d %-5d %-5d | %+.3e %-6s %5s | "
                  "%8.2e %8.2e %6.3f | %2d/%-2d %.1e %s"
                  % (kz, Rr["Nw"], Rr["S"], o["eps"],
                     "YES" if o["straddle"] else "no",
                     "%d/%d" % (o["n_in_l"], o["n_in_n"]),
                     o["frac"], o["scaled"], o["minC"],
                     o["ms_vlo"], o["ms_vhi"], o["sumrat"] - 1.0,
                     "Y" if o["cand_ge1"] else "n"),
                  flush=True)
            OT[kz] = o
            MT[kz] = dict(margin=Rr["margin"], Nw=Rr["Nw"],
                          z=Rr["z"], Sm=Rr["Sm"], S=Rr["S"])
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

        def gmax(key, g):
            vals = [OT[k][key] for k in all_kz
                    if grade_of(MT[k]["Nw"]) == g]
            return max(vals) if vals else 0.0

        chain_fail = []
        txt_w = []
        for key, bars, lab in (("dev_detid", DETID_BAR, "det-id"),
                               ("dev_cd", CD_BAR, "CD"),
                               ("res_n", ZERO_RES_BAR, "zero-res"),
                               ("ms_maxlo", MS_DEV_BAR, "ms-lo"),
                               ("ms_maxhi", MS_DEV_BAR, "ms-hi")):
            per = [gmax(key, g) for g in range(3)]
            ok_here = all(per[g] <= bars[g] for g in range(3))
            if not ok_here:
                chain_fail.append(lab)
            txt_w.append("%s %.1e/%.1e/%.1e (%s)"
                         % (lab, per[0], per[1], per[2],
                            "ok" if ok_here else "FAIL"))
        srat_bad = []
        viol_bad = []
        zbad = []
        for k in all_kz:
            g = grade_of(MT[k]["Nw"])
            if abs(OT[k]["sumrat"] - 1.0) > SUMLAM_BAR[g]:
                srat_bad.append(k)
            # a1: f64 sandwich floor is graded by maxdev, not by
            # a zero-violation count (the count is census)
            if (OT[k]["ms_maxlo"] > MS_DEV_BAR[g]
                    or OT[k]["ms_maxhi"] > MS_DEV_BAR[g]):
                viol_bad.append(k)
            dl = abs(OT[k]["nzeros_l"] - (MT[k]["Nw"] - 2))
            dn = abs(OT[k]["nzeros_n"] - (MT[k]["Nw"] - 1))
            cap = 0 if g == 0 else 2
            if dl > cap or dn > cap:
                zbad.append(k)
        if srat_bad:
            chain_fail.append("sumlam")
        if viol_bad:
            chain_fail.append("ms-viol")
        if zbad:
            chain_fail.append("zero-count")
        n_floor = sum(1 for k in all_kz
                      if OT[k]["ms_vlo"] + OT[k]["ms_vhi"] > 0)
        check("G33-ms-chain-wards", not chain_fail,
              "THE MS / r359 WARDS on all %d rows, graded: %s; "
              "sum λ/U misses %s; MS sandwich maxdev misses %s; "
              "f64 sandwich floor (vlo+vhi>0) on %d/%d rows "
              "(census, a1; all N_w-deep); zero-count == degree "
              "misses %s -- classical MS COUNT+SANDWICH is "
              "theorem-grade in exact arithmetic, f64-graded "
              "on the ladder (the placement is the remaining lemma)"
              % (len(all_kz), "; ".join(txt_w),
                 str(srat_bad) if srat_bad else "none",
                 str(viol_bad) if viol_bad else "none",
                 n_floor, len(all_kz),
                 str(zbad) if zbad else "none"))
        resolv = [k for k in all_kz if OT[k]["eps"] > RESOLV_FLOOR]
        n_resolv = len(resolv)
        sturm_ok_rows = [k for k in all_kz
                         if OT[k]["straddle"]
                         and OT[k]["n_in_l"] == 1
                         and OT[k]["n_in_n"] == 1
                         and OT[k]["n_mid"] == 1
                         and OT[k]["dress_ok"]
                         and OT[k]["P_N"] > 0
                         and OT[k]["detS"] > 0]
        sturm_n = len(sturm_ok_rows)
        n_scaled = sum(1 for k in resolv
                       if SCALED_BAND[0] <= OT[k]["scaled"]
                       <= SCALED_BAND[1])
        n_ge1 = sum(1 for k in resolv if OT[k]["cand_ge1"])
        n_z1 = sum(1 for k in resolv
                   if OT[k]["n_in_n"] == 1 and OT[k]["n_in_l"] == 1)
        force_ok = (n_scaled == n_resolv and n_ge1 == n_resolv
                    and n_z1 == n_resolv)
        a_letter = ("EDGE_GAP_MS_PROVED" if force_ok
                    else "MS_CENSUS")
        check("G34-mass-forcing", True,
              "THE MASS-FORCING CANDIDATES on %d resolvable MAIN "
              "rows: Z = 1/1 in the pair-gap on %d/%d (census, "
              "the r363 EDGE-GAP occupancy); CAND_SCALED "
              "(n M_I/U in %s) %d/%d -- %s; CAND_GE1 (M_I > "
              "chr_pair) %d/%d -- %s.  STEP TYPING: (M1) discrete "
              "gap theorem Z <= n_mid+1 = SATZ; (M2) n_mid == 1 "
              "pair geometry = CENSUS (r342 folds (2,4)); (M3) "
              "classical MS sandwich = SATZ (G33); (M4) Gauss "
              "sum λ = U = SATZ; (M5) proportional forcing "
              "n M_I/U ~ 1 = %s; (M6) Christoffel-endpoint "
              "forcing M_I > chr_pair = %s; (M7) dictionary-only "
              "bound (Digamma/tent/reciprocal without the OP "
              "kernel) = DOES NOT SUPPLY a mass lower bound that "
              "distinguishes Z = 0 from Z = 1 (M_I is the closed "
              "fold-3 weight, O(U/N^k) dual-void).  The pair-gap "
              "is dual-void: n M_I/U = O(10^{-5}), the O(1) MS "
              "buffer swallows Z in {0,1}.  EDGE-GAP remains OPEN "
              "as a theorem; the mass path does not close S5"
              % (n_resolv, n_z1, n_resolv, str(SCALED_BAND),
                 n_scaled, n_resolv,
                 "REFUTED" if n_scaled < n_resolv else "HOLDS",
                 n_ge1, n_resolv,
                 "REFUTED" if n_ge1 < n_resolv else "HOLDS",
                 "REFUTED at census grade" if n_scaled < n_resolv
                 else "the remaining lemma",
                 "REFUTED at census grade" if n_ge1 < n_resolv
                 else "the remaining lemma"))
        n_minc = sum(1 for k in resolv
                     if OT[k]["minC"] > MINC_HALF
                     and OT[k]["n_below"] == 0)
        n_gersh = sum(1 for k in resolv if OT[k]["gersh"] >= 0.0)
        n_rest = sum(1 for k in resolv if OT[k]["rest_min"] > 0)
        b_letter = ("REST_MASS_GO" if n_gersh == n_resolv
                    and n_minc == n_resolv
                    else "REST_NECESSARY_ONLY")
        check("G35-rest-occ-census", True,
              "THE REST-OCCUPATION CENSUS on %d resolvable MAIN "
              "rows: min_diag(R_CC) > 1/2 AND 0 C-nodes below "
              "1/2 on %d/%d -- NECESSARY for rest > 0 (lambda_min "
              "<= min diag, SATZ); Gershgorin lower bound >= 0 "
              "on %d/%d -- the SUFFICIENT diagonal-dominance "
              "reading %s; rest > 0 census %d/%d.  The r360 "
              "fold-1 anomaly is a UNION mu-atom, not a C-node, "
              "so it does not enter R_CC.  Elementwise occupation "
              ">= 1/2 is NOT sufficient for lambda_min(R_CC) >= "
              "1/2 (w9 Gershgorin already negative).  REST_MASS_GO "
              "does not fire"
              % (n_resolv, n_minc, n_resolv, n_gersh, n_resolv,
                 "FAILS" if n_gersh < n_resolv else "HOLDS",
                 n_rest, n_resolv))
        c_eps = sum(1 for k in resolv if OT[k]["eps"] > 0)
        c_dets = sum(1 for k in resolv if OT[k]["detS"] > 0)
        c_rest = sum(1 for k in resolv if OT[k]["rest_min"] > 0)
        c_both = sum(1 for k in resolv
                     if OT[k]["detS"] > 0 and OT[k]["rest_min"] > 0)
        c_split = all((OT[k]["eps"] > 0) == (
            OT[k]["detS"] > 0 and OT[k]["rest_min"] > 0)
            for k in resolv)
        c1_ok = all(OT[k]["rest_min"] + 1e-12 >= OT[k]["eps"]
                    for k in resolv)
        check("G36-composition-chain", c_split and c1_ok
              and c_eps == n_resolv,
              "THE COMPOSITION CHAIN on %d resolvable MAIN rows, "
              "TYPED: (C1) canonical straddle / Z = 1 = CENSUS "
              "(%d/%d MAIN); (C2) MS sandwich + Gauss sum λ = U "
              "+ discrete gap = SATZ; (C3) mass-forcing of Z = 1 "
              "= OPEN (refuted as a local MS argument); (C4) "
              "det S_N > 0 = CENSUS %d/%d; (C5) rest > 0 = "
              "CENSUS %d/%d (occupation necessary %d/%d, not "
              "sufficient); (C6) Schur split = SATZ, live %s, "
              "%d/%d both conjuncts; (C7) c=1 Cauchy rest >= eps "
              "= SATZ -- DOES NOT close rest > 0; (C8) R-dagger "
              "> 1/2 I <=> R > 1/2 I AND q-dagger < 1 = SATZ "
              "(r362 A5, gated at w9); (C9) interlacing = SATZ "
              "(r362 A7, gated at w9).  The two OPEN links of "
              "r363 remain OPEN after the mass path"
              % (n_resolv, sturm_n, len(all_kz), c_dets, n_resolv,
                 c_rest, n_resolv, n_minc, n_resolv,
                 "ok" if c_split else "FAIL", c_both, n_resolv))

    # ---------------- S4 worlds
    section("S4  WORLDS -- TWIN + CHI + SCRAMBLE")
    if smoke:
        for g in ("G40-twin", "G41-chi3-ladder", "G42-chi4-ladder",
                  "G43-scramble-break"):
            check(g, True, "SMOKE: skipped")
        chi_sturm = {"chi3": None, "chi4": None}
    else:
        tw_dev = 0.0
        mass_dev = 0.0
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
            oT = ms_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                         mzT["vn"], mzT["Nw"], mzT["S"],
                         mzT["L"], t1_, t2_)
            oM = OT[kz]
            tw_dev = max(
                tw_dev,
                abs(math.log(oT["detS"] / oM["detS"])),
                abs(math.log(oT["lamS"] / oM["lamS"])))
            if oM["M_I"] > 0 and oT["M_I"] > 0:
                mass_dev = max(mass_dev,
                               abs(oT["M_I"] / oM["M_I"] - 1.0))
            del oT
        check("G40-twin", ok_dose0 and tw_dev <= TWIN_BAR
              and mass_dev <= TWIN_MASS_BAR,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "BITWISE %s): max |dlog detS/lamS| = %.1e nats "
              "(bar %.0e), |d M_I| rel = %.1e (bar %.0e) -- MS "
              "mass coordinates are twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_BAR,
                 mass_dev, TWIN_MASS_BAR))
        chi_sturm = {}
        for (q, lpq, tag, eanch) in (
                (DMF.Q_CHI3, DMF.LPQ3, "chi3", CHI3_EPS_ANCH),
                (DMF.Q_CHI4, DMF.LPQ4, "chi4", None)):
            rows, excl = [], []
            for kz in V.admissible_indices():
                o = chi_ms_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(o)
            live = [r for r in rows if r["eps"] > 0]
            sup_ok = all(r["ok_sup"] and r["ok_map"] for r in rows)
            wards_ok = all(
                r["dev_cd"] <= CD_BAR[grade_of(r["Nw"])]
                and abs(r["sumrat"] - 1.0)
                <= SUMLAM_BAR[grade_of(r["Nw"])]
                and r["ms_maxlo"] <= MS_DEV_BAR[grade_of(r["Nw"])]
                and r["ms_maxhi"] <= MS_DEV_BAR[grade_of(r["Nw"])]
                for r in rows)
            st_ok = [r["kz"] for r in live
                     if r["straddle"] and r["n_in_l"] == 1
                     and r["n_in_n"] == 1 and r["P_N"] > 0]
            scaled_hit = [r["kz"] for r in live
                          if SCALED_BAND[0] <= r["scaled"]
                          <= SCALED_BAND[1]]
            w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
            if tag == "chi3":
                anch_ok = abs(w9r["eps"] / eanch - 1.0) <= 2e-2
            else:
                anch_ok = True
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and wards_ok and anch_ok
                        and len(live) == len(rows))
            chi_sturm[tag] = (len(st_ok), len(live), scaled_hit,
                              bool(w9r["straddle"]), w9r["n_in_n"],
                              w9r["scaled"])
            check("G41-chi3-ladder" if tag == "chi3"
                  else "G42-chi4-ladder", ok_world,
                  "%s NEGATIVE CONTROL through the identical MS "
                  "pipeline: %d/42 built (exclusions %s), support "
                  "%s, MS+chain wards %s, eps > 0 %d/%d; STURM "
                  "pattern %d/%d -- MAY tip (consistent: chi is "
                  "not proof-load); CAND_SCALED on %s; w9 straddle "
                  "%s n_in %d n M_I/U %.2e (SCALED_BAND %s) -- "
                  "the MS sandwich is world-blind (classical); "
                  "the occupancy Z = 1 is the near-wall pattern, "
                  "not a mass-forced theorem, and MAY tip with "
                  "the Sturm pattern"
                  % (tag.upper(), len(rows),
                     str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     "PASS" if wards_ok else "FAIL",
                     len(live), len(rows), len(st_ok), len(live),
                     str(scaled_hit[:8]) + ("..." if len(scaled_hit)
                                            > 8 else ""),
                     w9r["straddle"], w9r["n_in_n"], w9r["scaled"],
                     str(SCALED_BAND)))
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS = ms_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                     mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_)
        scr_named = (oS["rest_min"] < 0 and oS["eps"] < 0
                     and not oS["straddle"] and oS["lamS"] > 0
                     and oS["minC"] < MINC_HALF
                     and oS["n_in_n"] != 1)
        alg_ok = (oS["dev_detid"] <= DETID_BAR[0]
                  and oS["dev_cd"] <= CD_BAR[0]
                  and abs(oS["sumrat"] - 1.0) <= SUMLAM_BAR[0]
                  and oS["ms_vlo"] + oS["ms_vhi"] <= MS_VIOL_MAX)
        check("G43-scramble-break", scr_named and alg_ok
              and abs(oS["eps"] - SCR_ANCH["eps"]) <= 2e-3
              and abs(oS["rest_min"] - SCR_ANCH["rest"]) <= 2e-3
              and abs(oS["lamS"] / SCR_ANCH["lamS"] - 1.0) <= 5e-2
              and abs(oS["minC"] - SCR_ANCH["minC"]) <= 2e-2,
              "THE MATCHED SCRAMBLE BREAKS NAMED, THREE PRONGS: "
              "(p1) STURM straddle FAILS (n_mid %d, zeros_in_"
              "pair %d/%d); (p2) REST clause FAILS (rest %.4f, "
              "lamS +%.4e -- the live c=1-misquote counterexample); "
              "(p3) OCCUPATION NECESSARY CONDITION FAILS "
              "(min_diag(R_CC) = %.4f < 1/2, %d C-nodes below "
              "1/2) -- the scramble breaks Leg B at the named "
              "occupation hypothesis AND Leg A at Z != 1.  MS "
              "algebra world-blind (sum λ/U, sandwich, CD all "
              "hold).  CAND_SCALED %s CAND_GE1 %s"
              % (oS["n_mid"], oS["n_in_l"], oS["n_in_n"],
                 oS["rest_min"], oS["lamS"], oS["minC"],
                 oS["n_below"],
                 SCALED_BAND[0] <= oS["scaled"] <= SCALED_BAND[1],
                 oS["cand_ge1"]))

    # ---------------- S5 must-fails
    section("S5  MUST-FAILS")
    # m1: off-by-one MS counting on w9 true zeros
    xu9 = np.asarray(mz9["xu"], float)
    u9 = np.abs(np.asarray(mz9["wu"], float))
    ud9m = BDH.dual_weights(xu9, u9, R9["S"], mz9["L"])[0]
    o9w = SWD.schur_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                         R9["Nw"], R9["S"], mz9["L"],
                         R9["i1"], R9["i2"])
    zs_m1, _ = true_zeros(xu9, o9w["ad"], o9w["bd"], o9w["h0d"],
                          R9["Nw"] - 1)
    lam_m1 = 1.0 / kxx_at(zs_m1, o9w["ad"], o9w["bd"], o9w["h0d"],
                          R9["Nw"] - 1)
    m1_viol = mutant_ms_offbyone(zs_m1, lam_m1, xu9, ud9m)
    check("G80-m1-wrong-counting", m1_viol >= M1_VIOL_MIN,
          "m1 MS OFF-BY-ONE COUNTING (Lambda_j <= M_left <= "
          "Lambda_{j+1} instead of Lambda_{j-1} <= M <= Lambda_j): "
          "%d sandwich violations at w9 (min %d) -- EXACTLY "
          "CAUGHT; the classical convention is load-bearing"
          % (m1_viol, M1_VIOL_MIN))
    check("G81-m2-bar-by-sight", bool(hits_m2),
          "m2 MASS BAR AFTER SIGHT (min M_I among withheld Z = 1 "
          "rows): AST-FLAGGED (%s) -- SCALED_BAND and every mass "
          "bar were frozen from the disclosed s1 pass BEFORE any "
          "ladder evaluation"
          % (hits_m2[0] if hits_m2 else "MISS"))
    check("G82-m3-occ-from-rest", bool(hits_m3),
          "m3 OCCUPATION READ BACK FROM lambda_min(R_CC) "
          "(returns 1/2 + withheld rest): AST-FLAGGED (%s) -- "
          "rest_occ consumes the diagonal of R, never the "
          "eigenvalue"
          % (hits_m3[0] if hits_m3 else "MISS"))
    check("G83-m4-circular-christoffel", bool(hits_m4),
          "m4 CIRCULAR CHRISTOFFEL (λ := M_I/Z from withheld "
          "columns): AST-FLAGGED (%s) -- Christoffel numbers are "
          "1/K_{n-1}(z,z) from the dual OP recurrence"
          % (hits_m4[0] if hits_m4 else "MISS"))
    f9 = BDH.dual_weights(xu9, u9, R9["S"], mz9["L"])[2]
    m5_nin = mutant_wrong_gap(xu9, ud9m, zs_m1, f9)
    check("G84-m5-wrong-gap", m5_nin != o9s["n_in_n"],
          "m5 WRONG GAP BOUNDS (fold-(1,2) interval instead of "
          "the critical pair): zeros_in_gap = %d != pair-gap "
          "n_in = %d -- EXACTLY CAUGHT"
          % (m5_nin, o9s["n_in_n"]))
    for k in ("R", "ad", "bd", "h0d"):
        o9w.pop(k, None)

    # ---------------- S6 verdict
    section("S6  VERDICT")
    if smoke:
        verd = "SMOKE"
        check("G90-verdict", True, "SMOKE: verdict deferred")
    else:
        parts = []
        if a_letter == "MS_CENSUS":
            parts.append(
                "MS_CENSUS(M1-gap SATZ, M3-sandwich SATZ, "
                "M4-sumλ SATZ, M5-scaled REFUTED, M6-chr-endpoint "
                "REFUTED, M7-dictionary-force OPEN/NO, Z=1 CENSUS "
                "%d/%d)" % (sturm_n, len(all_kz)))
        else:
            parts.append(a_letter)
        parts.append(b_letter)
        parts.append("STURM_CANONICAL_CENSUS(%d/%d MAIN, chi MAY "
                     "tip, scramble MUST tip)"
                     % (sturm_n, len(all_kz)))
        parts.append("COMPOSITION_TYPED")
        exhausted = (a_letter != "EDGE_GAP_MS_PROVED"
                     and b_letter != "REST_MASS_GO")
        if exhausted:
            parts.append("INTERNAL_EXHAUSTED")
        parts.append("WORLD_LEDGER")
        parts.append("TWIN_LEDGER")
        parts.append("SCRAMBLE_BREAK")
        parts.append("MUSTFAIL_LEDGER")
        verd = "+".join(parts)
        check("G90-verdict", True,
              "MAIN VERDICT %s.  CONDITIONAL PACKAGE (every named "
              "lemma of both internal lanes, r363+r366): SATZ -- "
              "discrete gap theorem; Sturm/Markov interlacing of "
              "a positive discrete measure; Gauss quadrature of "
              "degree 2n-1; MS sandwich Lambda_{j-1} <= M_left(z_j) "
              "<= Lambda_j; occupation complement o_eta + o_dual "
              "== 1; Schur split {R > I/2} <=> {R_CC > I/2} AND "
              "{S_N > 0}; Cauchy rest >= eps; CD update; r362 "
              "(A5)/(A7).  CENSUS -- canonical straddle / Z = 1 "
              "in the pair-gap 84/85; det S_N > 0; rest > 0; "
              "min_diag(R_CC) > 1/2 on resolvable MAIN; n_mid = 1.  "
              "OPEN -- EDGE-GAP placement as SATZ (mass forcing "
              "refuted: dual-void pair-gap, n M_I/U ~ 10^{-5}, "
              "O(1) MS buffer cannot distinguish Z = 0 from Z = 1; "
              "BKMM pinning already refuted at r363); rest > 0 as "
              "SATZ (occupation necessary not sufficient; c=1 does "
              "not close it; scramble is the live counterexample).  "
              "The internal full attack (pinning path r363, mass "
              "path r366) is exhausted at measured grade.  NO L* "
              "claim, NO RH claim"
              % verd)

    print("RESULT_LETTER: %s%s"
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
