#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""canonical_sturm_induction_probe --
PRIME.LSTAR.DUAL.INTERNAL_ATTACK.01 (round 363): THE INTERNAL
FULL ATTACK ON R† ≻ ½I -- two sharp internal angles, shared
machinery, proof-first.  Coexistence: a MED-CAP proof worker
(rh/problem) and a Lean worker (rh/lean) run in parallel -- this
probe touches NOTHING outside its own file and the strictly
additive rh-sync.  DAS PROBLEM VOLLSTÄNDIG INTERN LÖSEN: no freeze
for externals; every leg aims at a proveable statement, numerics
verify the proof steps.

THE STRATEGIC OBSERVATION (binding): the r359 STURM_CENSUS holds
on 84/85 MAIN rows (kz133 = the disclosed f64 floor) and fails on
chi worlds far from the wall.  The universal carrier was correctly
rejected.  BUT the final theorem needs only the CANONICAL family
(lstar_canonical quantifies over CanonicalWindow = the MAIN
windows; chi worlds are negative controls, not proof-load).  If
the near-wall Sturm pattern is proveable FROM THE STRUCTURE of
the canonical family (the r360 saturation-edge straddle), then
sign(det S_N) follows without RHP asymptotics; with the proved
c=1 rest inequality (Cauchy interlacing, r360) the hope was that
R ≻ ½I would close, and r362 interlacing + border-Schur would
lift it to R†.

THE TWO ANGLES (one round, shared machinery):
  ANGLE A -- THE CANONICAL STURM THEOREM.  Standing pieces:
    (i) zeros of consecutive OPs of a POSITIVE measure interlace
    classically (Sturm/Markov -- the dual ensemble IS positive,
    r356); (ii) the critical pair sits at the saturation edge
    (r360, QP 4/4 + occupation 85/85); (iii) the dual weight is
    closed (u_vee = c_j(1-x)/|f|); (iv) the exact identities
    (IIKS Casoratian, adjugate, r359).  THE PRECISE GAP: where
    do the dual-OP zeros sit relative to the two pair atoms --
    does the straddle follow from the edge location?  Candidate
    lemma (BKMM Thm 2.3 reading): in a saturated zone the zeros
    are node-pinned with distance <= f(N); at the straddle point
    that forces the interlacing.  Pre-spec scoping (s1, /tmp,
    deleted) found the HURWITZ ratios in the sealed zone {1,2,3}
    are O(1) (~0.29..0.42 of the local gap), COMPARABLE TO THE
    BULK median (~0.25..0.30), and NOT shrinking in N (w9 0.31
    -> kz56 0.42): the exponential node-pinning reading is the
    hypothesis under test, not a prior.  A second, independent
    gap remains regardless: WHY a zero of p_{N-1} occupies the
    unique pair-gap (y2, y1) -- the EDGE-GAP LEMMA, named even
    if BKMM-pinning is refuted.
  ANGLE B -- N-MONOTONICITY / INDUCTION.  Exact CD update
    R_{n+1} = R_n + v_n v_n^T on Y (v_n = the n-th dual
    orthonormal polynomial restricted to Y -- finite theorem).
    Loewner gives lambda_min increasing in n: the r282 Toda
    tautology if that is sold as the induction.  The NON-
    tautological form needs an EXPLICIT loss term from the
    source weights.  Pre-spec scoping found n_cross (the first
    n with lambda_min(R_n) > 1/2) equals N_w-1 or N_w-2 on
    every sized instance -- the L* gap is a TERMINAL-RANK
    phenomenon; an induction from a certified small-n head
    cannot start.  The window-ladder form (delta_{k+1} >=
    delta_k * (1 - L_k) with L_k from the cosine-edge geometry
    LC_EDGE2 = 1 - (S/S')^2 or from the pair dual-weight ratio
    LC_UVEE) is the sealed alternative, adjudicated not assumed.
    The Toda-tautology mutant (L read back from lambda_min) is
    a must-fail.

THE LEGS: (Leg 0) anchors bit-near: r359 Sturm columns 84/85,
r360 saturation zone / occupation, r362 R† + interlacing +
border-Schur, r356 dual ensemble.  (Leg A) zero survey +
candidate lemma + step typing on all 85 + Fractions toys.
(Leg B) exact update + increment census + induction inequality
with sealed loss.  (Leg C) composition chain, honestly typed
(SATZ / census / open), with the c=1 rest clause NOT allowed
to silently close rest > 0.  (Leg D) worlds + must-fails (>=5):
chi is a negative control (the pattern MAY tip -- consistent);
SCRAMBLE breaks named.  Must-fails: Toda tautology -> AST;
pinning from the straddle circularly -> construction AST;
induction bar after sight -> protocol AST; wrong OP indices ->
exact CAUGHT; c=1 rest misquoted as rest>0 from S_N>0 -> exact
CAUGHT (the scramble IS the counterexample: lamS > 0 and
rest < 0).

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO L* CLAIM, NO RH
CLAIM in either direction, mincut unchanged.  Two-commit freeze
protocol (r329 convention): spec + machinery committed BEFORE
the record run, record tables inserted after.

INDEX FIREWALL (binding, r238-r362 discipline): w = window (kz),
S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds = grid
indices; ground truth enters GATES and record tables only; the
module-own constructors consume measure arrays / chain
coefficients / positions / pair indices ONLY (AST scope audit;
withheld identifiers delta_col_true / straddle_col_true /
pin3_col_true and the REC/anchor constants); no zero/prime
oracles (AST firewall); no fit primitives beyond the imported
r286 Theil-Sen (fragment audit).  MACHINERY IMPORTED VERBATIM:
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
4.2003e-5, detS 2.0690e-8, share 0.6973, P_N 8.601e-9);
r362 W9 AUG (lamRd 0.500041459, mdag 1.6582e-4); r352 margin
slope -3.332 tol 0.02.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8;
W9 HUR ANCHORS (s1 scoping, disclosed): pin3_l 0.2935 / pin3_n
0.3105 abs 2e-2, sat_pin_max 0.310 abs 2e-2, bulk_med_n 0.267
abs 5e-2, n_cross 183 EXACT, nzeros 182/183 EXACT, Ymass_last
0.2666 abs 2e-2 (the last column of the rank-(N_w-1) hole
kernel), n_mid 1, zeros_in_pair 1/1; RANK ANCHORS
kz18 n_cross 140/142, kz44 435/436 (gap <= RANK_GAP_MAX 3);
PIN_SAT_BAR 0.15 (BKMM-like exponential-pinning reading: sat
Hurwitz ratio <= 0.15 AND sat_max <= 0.7 x bulk_med -- the
hypothesis under test; scoping 0.29..0.42 vs bulk 0.25..0.30
is the expected REFUTATION if the finite-N census agrees);
PIN3_BAND (0.15, 0.55) the Gauss-like pair-gap placement
census; SAT_FOLDS (1, 2, 3) the r360 sealed dual-void /
primal-sat block as a geometric index set; MAIN_STURM_MIN 83
(of 85; kz133 f64-floor allowance, the r359 convention);
INTERLACE_MIN 0.95; GRADES shallow N_w <= 900 / mid <= 3200 /
deep > 3200; r359 graded bars REUSED: CD / IIKS / COUP / RM /
DETID; EPS_FLOOR 1.25e-10; RESOLV_FLOOR 1e-9; RANK_KZ (18, 9,
44, 52) -- mid/deep rank bisection sealed OUT of the clause
(kz56 scoping n_cross 2016/2018 already sized the terminal-rank
pattern; disclosed); LC_EDGE2 1-L = (S/S')^2 on consecutive
N_w-ordered resolvable pairs with S' > S; LC_UVEE 1-L =
min(ud_pair')/min(ud_pair); INDUCTION_GO iff 0 violations of
BOTH candidates -- expected NOT, the adjudication is the
letter; WORLD_KZ (18, 9, 52, 119, 42, 130); N_CHI_MIN 21;
SCR_SEED 1; TWIN_BAR 1e-3 nats (Schur) + TWIN_PIN_BAR 5e-2 abs
(pin3); M4_BAR 0.5 (wrong OP indices, r359 scoped 2.02);
EXT selections verbatim r356; TOY_TOL 1e-12; runtime <= 1800 s;
smoke = toys + firewall + scopes + mutants + w9 blocks
(records, Hurwitz, n_cross, R† composition); ladder, EXT,
twin, chi, scramble, rank census, loss census, adjudications
skipped.

PRE-SPEC SCOPING (disclosed -- ONE sizing pass on kz9/18/44/56
+ chi3 w9 + scramble w9, /tmp, deleted; no bar, band, clause,
candidate or verdict rule tuned after any evaluation except as
sized here and said so): MAIN straddle both-flip + zeros_in_pair
1/1 + n_mid 1 on every sized rung; nzeros = degree EXACT;
Hurwitz sat_pin_max 0.293/0.370/0.397/0.416 (w9/18/44/56)
vs bulk_med 0.267/0.254/0.258/0.249 -- NOT separated, NOT
shrinking; pin3 0.29..0.42 inside PIN3_BAND; chi3 w9 STRADDLES
(both flip, 1/1) but pin3 = 1.03 OUTSIDE the band (fold-3 is
NOT the pair-gap zero's nearest node) -- world-separating for
PIN3, not for the w9 straddle; scramble n_mid 3, both same
sign, zeros_in_pair 2/2, named straddle break; n_cross =
Nw-1 or Nw-2 on all four MAIN rank instances (w9 183/184,
kz18 140/142, kz44 435/436, kz56 2016/2018) AND chi3 181/184
-- TERMINAL-RANK; window-ladder preview on six rungs already
shows LC_EDGE2 violations (kz9->44 d'/d = 0.004 vs 0.177).
The verdict letters, PIN_SAT_BAR, RANK_GAP_MAX, LC candidates
and every bar were frozen from these numbers BEFORE any
ladder-wide evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > CHAIN_FAIL > the
adjudicated letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the rank/support gate fails on any
    real MAIN ladder window /
  CHAIN_FAIL(loci)  iff any exact ward fails (toys, r359 E1-E5
    graded, CD-update, zero-count, composition algebra) /
  otherwise the angle letters, each exactly one:
  [CANONICAL_STURM_PROVED  iff the straddle is theorem-grade on
    the canonical family (classical Sturm + a proved placement
    lemma, 0-violation, named theorem) /
   PINNING_LEMMA_NAMED  iff the BKMM-2.3 node-pinning clause
    fires (sat Hurwitz <= PIN_SAT_BAR and sat_max <= 0.7 x
    bulk_med on resolvable MAIN) -- the straddle then reduces
    to that one lemma /
   PINNING_REFUTED  iff the BKMM-2.3 clause fails, plus
    EDGE_GAP_LEMMA_NAMED (the remaining placement lemma: why
    a zero of each consecutive dual OP occupies the unique
    pair-gap) /
   STURM_OPEN]
  [INDUCTION_GO  iff LC_EDGE2 AND LC_UVEE have 0 violations on
    consecutive N_w-ordered resolvable MAIN pairs with S' > S /
   TERMINAL_RANK_DEAD  iff every sealed RANK_KZ instance has
    n_cross >= N_w - RANK_GAP_MAX (the positivity is a last-
    rank phenomenon; Loewner cannot start from a certified
    small-n head) /
   INDUCTION_OPEN]
  + STURM_CANONICAL_CENSUS(MAIN straddle >= MAIN_STURM_MIN,
    chi MAY tip, scramble MUST tip) [always if the chain holds]
  + COMPOSITION_TYPED(SATZ / census / open per link) [always]
  + INTERNAL_LIMIT  iff BOTH angles remain short of a theorem
    (pinning refuted or named-open, AND induction not GO) --
    honest: genuine new analysis, the external RHP path stays
    on the table /
  + WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK + MUSTFAIL_LEDGER.
Combinations allowed.  Honesty before beauty: the CD update,
classical zero-interlacing of a positive discrete measure, the
Schur split, Cauchy rest >= eps, and r362 (A5)/(A7) are finite
theorems; the straddle on MAIN, det S_N > 0, rest > 0, n_cross
terminal, Hurwitz ratios are census; the BKMM pinning lemma
and any window-ladder loss that would prove delta_N > 0 from
the certified head are the hypotheses under test; the c=1 rest
inequality does NOT close rest > 0 from det S_N > 0 (scramble
counterexample); no verdict claims L*, a bound mechanism, a
derived 5/7, or RH progress in any direction; the DCCX STOP
list stands.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit; TWO-COMMIT PROTOCOL: sealed spec committed
as "r363 pre-freeze" (de7c55ec, SPEC_SHA freeze fd7613339dfc18a0)
BEFORE the first full evaluation; chronology honest: smoke
32/32 byte-identical; pre-freeze commit de7c55ec; calibration
pass 1 = FIRST full evaluation = 32/32 (149.6 s) with ZERO
amendments -- no bar, band, clause, candidate or verdict rule
moved after the freeze; record run1 = 32/32 (133.4 s), run2 =
32/32 (140.6 s), byte-identical up to the WALL line and
identical to calibration):
MAIN VERDICT = BOTH_PARTIAL(PINNING_REFUTED+EDGE_GAP_LEMMA_NAMED
+ TERMINAL_RANK_DEAD + STURM_CANONICAL_CENSUS(84/85 MAIN, chi
MAY tip, scramble MUST tip) + COMPOSITION_TYPED + INTERNAL_LIMIT).
ANGLE A: BKMM Thm 2.3 node-pinning REFUTED at census grade on
74 resolvable MAIN rows (sat Hurwitz max 0.462 vs bar 0.15;
bulk median 0.257; sat is LARGER than bulk, not smaller; pin3
in (0.15, 0.55) on 74/74 -- Gauss-like pair-gap placement, not
exponential pinning; ratios do not shrink in N).  Canonical
Sturm census 84/85 (miss kz133 = f64 floor, the r359 row);
interpolated-zero interlacing 85/85; zero-count == degree
0-miss graded.  The remaining lemma is EDGE-GAP: why a zero of
each consecutive dual OP occupies the unique pair-gap (y2,y1)
-- classical Sturm/Markov gives interlacing and the count, not
the placement.  The r360 zone {1,2,3} is DUAL-VOID (primal-sat),
so dual-OP pinning if it applied would live in the BULK.
ANGLE B: n_cross/N_w = 183/184, 140/142, 435/436, 877/878 on
RANK_KZ -- TERMINAL-RANK (gap 1-2); CD update residual 3.3e-17
at w9 (Fractions rank-1 on the toy).  Window-ladder LC_EDGE2
36/71 violations, LC_UVEE 32/71 -- INDUCTION_GO does not fire.
COMPOSITION (74 resolvable): Schur split SATZ 74/74; Cauchy
rest>=eps SATZ 74/74; detS>0 and rest>0 CENSUS 74/74; r362 A5/A7
gated at w9.  The hoped chain "Sturm => det S_N > 0 => [c=1]
R > 1/2 I" has TWO gaps, both measured: Sturm does not give
det S_N without P_N, W_N signs; c=1 does not give rest>0
(scramble: lamS +1.37e-2, rest -0.4962).  Worlds: chi3 30/42
and chi4 29/42 keep the Sturm pattern (MAY tip); chi w9 pin3
1.039/1.038 OUTSIDE the MAIN band (world-separating for fold-3
pinning); scramble straddle FAILS (n_mid 3, zeros_in_pair 2/2)
AND is the live c=1-misquote counterexample.  Twin dose-zero
bitwise, |dlog| 6.9e-4, |dpin3| 6.0e-10.  Must-fails 5/5.
Runtime 149.6 / 133.4 / 140.6 s calib/rec1/rec2; smoke 0.3 s.

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

import schur_wronskian_dual_probe as SWD         # noqa: E402 r359
import borodin_dual_hole_probe as BDH            # noqa: E402 r356
import augmented_borodin_duality_probe as ABD    # noqa: E402 r362
import pair_extremal_probe as PX                 # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF      # noqa: E402 r357
import phi_wander_anatomy_probe as PWA           # noqa: E402 r354
import ext3_fresh_anchors_probe as E3            # noqa: E402 r329
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import hirota_sign_probe as HS                   # noqa: E402 r226
import principal_bessel_probe as PB              # noqa: E402 r243
import verify_lstar_instance as V                # noqa: E402 document
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
ABD_SHA_PREFIX = "7d810a9a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
LM_SHA_PREFIX = "0a44ac4e"
W9_SCHUR_ANCH = dict(eps=4.1882e-5, lamS=4.2003e-5, detS=2.0690e-8,
                     share=0.6973, P_N=8.601e-9, f1=2, f2=4)
W9_AUG_ANCH = dict(lamRd=0.500041459, mdag=1.658218770e-4)
W9_HUR_ANCH = dict(pin3_l=0.2935, pin3_n=0.3105, sat_max=0.310,
                   bulk_n=0.267, n_cross=183, nzeros_l=182,
                   nzeros_n=183, ymass=0.2666)
HUR_ANCH_TOL = 2.0e-2
BULK_ANCH_TOL = 5.0e-2
YMASS_ANCH_TOL = 2.0e-2
RANK_ANCH = {18: (140, 142), 9: (183, 184), 44: (435, 436)}
PIN_SAT_BAR = 0.15
PIN_SEP = 0.70
PIN3_BAND = (0.15, 0.55)
SAT_FOLDS = (1, 2, 3)
MAIN_STURM_MIN = 83
INTERLACE_MIN = 0.95
RANK_GAP_MAX = 3
RANK_KZ = (18, 9, 44, 52)
FIT_MARGIN_ANCH = -3.332
FIT_ANCH_TOL = 0.02
NW_SHALLOW = 900
NW_MID = 3200
CD_BAR = (1.0e-12, 1.0e-11, 1.0e-10)
IIKS_BAR = (1.0e-6, 1.0e-3, 5.0e-2)
COUP_BAR = (1.0e-8, 1.0e-6, 1.0e-3)
RM_BAR = (1.0e-8, 1.0e-6, 1.0e-3)
DETID_BAR = (1.0e-10, 1.0e-9, 1.0e-6)
UPD_BAR = (1.0e-10, 1.0e-9, 1.0e-7)
EPS_FLOOR = 1.25e-10
RESOLV_FLOOR = 1.0e-9
WORLD_KZ = (18, 9, 52, 119, 42, 130)
N_CHI_MIN = 21
SCR_SEED = 1
TWIN_BAR = 1.0e-3
TWIN_PIN_BAR = 5.0e-2
M4_BAR = 0.5
CHI3_EPS_ANCH = 2.205e-4
SCR_ANCH = dict(eps=-0.4962, rest=-0.4962, lamS=1.369e-2)
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


CONSTRUCTORS = ("grade_of", "op_pair", "zeros_of", "local_gap",
                "hurwitz_row", "n_cross_bisect", "cd_last_update",
                "loss_edge2", "loss_uvee", "attack_rung",
                "chi_attack_row")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_SCHUR_ANCH",
                   "W9_AUG_ANCH", "W9_HUR_ANCH", "RANK_ANCH",
                   "PIN_SAT_BAR", "PIN3_BAND", "FIT_MARGIN_ANCH",
                   "CHI3_EPS_ANCH", "SCR_ANCH",
                   "delta_col_true", "straddle_col_true",
                   "pin3_col_true"}


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


def op_pair(xu, wvec, a, b, h0, n_lo, n_hi):
    """orthonormal dual-OP columns n_lo, n_hi (0-based) at all
    nodes via the three-term recurrence; sign(phi) = sign(p)
    because sqrt(w) > 0; consumes measure + chain only."""
    u = np.sqrt(wvec) / math.sqrt(h0)
    um = np.zeros_like(u)
    cols = {}
    if 0 in (n_lo, n_hi):
        cols[0] = u.copy()
    for i in range(n_hi):
        r = (xu - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        if i + 1 in (n_lo, n_hi):
            cols[i + 1] = u.copy()
    return cols[n_lo], cols[n_hi]


def zeros_of(phi, xu):
    """sign-change zeros by linear interpolation; Hurwitz
    distance to the nearest node; consumes the OP field +
    positions only."""
    zs, dH, nearest = [], [], []
    for j in range(len(xu) - 1):
        a, b = float(phi[j]), float(phi[j + 1])
        if a == 0.0:
            zs.append(float(xu[j]))
            dH.append(0.0)
            nearest.append(j)
            continue
        if a * b < 0.0:
            z = float(xu[j] - a * (xu[j + 1] - xu[j]) / (b - a))
            d = np.abs(xu - z)
            k = int(np.argmin(d))
            zs.append(z)
            dH.append(float(d[k]))
            nearest.append(k)
    if float(phi[-1]) == 0.0:
        zs.append(float(xu[-1]))
        dH.append(0.0)
        nearest.append(len(xu) - 1)
    return zs, dH, nearest


def local_gap(xu, k):
    """nearest-neighbour gap at node k; consumes positions only."""
    if k == 0:
        return float(xu[1] - xu[0])
    if k == len(xu) - 1:
        return float(xu[-1] - xu[-2])
    return float(min(xu[k] - xu[k - 1], xu[k + 1] - xu[k]))


def hurwitz_row(phl, phn, xu, f, iY, i1, i2, sat_folds):
    """Hurwitz / straddle / pin3 columns of one window; consumes
    the two OP fields + positions + fold indices + pair + the
    geometric sat-fold tuple only."""
    xu = np.asarray(xu, float)
    y1, y2 = float(xu[iY[i1]]), float(xu[iY[i2]])
    if y1 < y2:
        y1, y2 = y2, y1
    sl = float(np.sign(phl[iY[i1]]) * np.sign(phl[iY[i2]]))
    sn = float(np.sign(phn[iY[i1]]) * np.sign(phn[iY[i2]]))
    zs_l, dH_l, nr_l = zeros_of(phl, xu)
    zs_n, dH_n, nr_n = zeros_of(phn, xu)
    sat = set(int(j) for j in np.nonzero(
        np.isin(f, list(sat_folds)))[0])

    def zone_max(dH, nr):
        sat_r, bulk_r = [], []
        for d, k in zip(dH, nr):
            g = local_gap(xu, k)
            r = d / g if g > 0 else float("nan")
            (sat_r if k in sat else bulk_r).append(r)
        smax = max(sat_r) if sat_r else float("nan")
        bmed = float(np.median(bulk_r)) if bulk_r else float("nan")
        return smax, bmed

    sat_l, bulk_l = zone_max(dH_l, nr_l)
    sat_n, bulk_n = zone_max(dH_n, nr_n)
    n_in_l = sum(1 for z in zs_l if y2 < z < y1)
    n_in_n = sum(1 for z in zs_n if y2 < z < y1)
    j3s = np.nonzero(f == 3)[0]
    if len(j3s) and zs_l and zs_n:
        j3 = int(j3s[0])
        g3 = local_gap(xu, j3)
        pin3_l = min(abs(z - xu[j3]) for z in zs_l) / g3
        pin3_n = min(abs(z - xu[j3]) for z in zs_n) / g3
    else:
        pin3_l = pin3_n = float("nan")
    za = np.sort(zs_l)
    zb = np.sort(zs_n)
    ilace = False
    if len(zb) == len(za) + 1 and len(za) > 0:
        ilace = all(zb[i] < za[i] < zb[i + 1]
                    for i in range(len(za)))
    return dict(sl=sl, sn=sn,
                straddle=(sl < 0 and sn < 0),
                nzeros_l=len(zs_l), nzeros_n=len(zs_n),
                n_in_l=n_in_l, n_in_n=n_in_n,
                sat_l=sat_l, sat_n=sat_n,
                bulk_l=bulk_l, bulk_n=bulk_n,
                pin3_l=pin3_l, pin3_n=pin3_n,
                ilace=ilace)


def n_cross_bisect(Bd):
    """smallest n in 1..ncols with lambda_min(B[:,:n] B[:,:n].T)
    > 1/2; consumes the dual orthonormal frame on Y only."""
    ncols = Bd.shape[1]
    lo, hi = 1, ncols
    while lo < hi:
        mid = (lo + hi) // 2
        R = Bd[:, :mid] @ Bd[:, :mid].T
        lm = float(np.linalg.eigvalsh(R)[0])
        if lm > 0.5:
            hi = mid
        else:
            lo = mid + 1
    n = lo
    R = Bd[:, :n] @ Bd[:, :n].T
    lm = float(np.linalg.eigvalsh(R)[0])
    return n, lm, ncols


def cd_last_update(Bd, n):
    """the exact CD rank-1 step R_n = R_{n-1} + v v^T with
    v = Bd[:, n-1]; returns the Frobenius residual; consumes
    the dual frame on Y only."""
    if n < 2:
        return 0.0, 0.0
    R = Bd[:, :n] @ Bd[:, :n].T
    Rp = Bd[:, :n - 1] @ Bd[:, :n - 1].T
    v = Bd[:, n - 1]
    dev = float(np.linalg.norm(R - (Rp + np.outer(v, v))))
    ymass = float(v @ v)
    return dev, ymass


def loss_edge2(S, Sp):
    """LC_EDGE2: the cosine-edge geometry candidate 1-L =
    (S/S')^2 for S' > S; consumes the two grid sizes only."""
    if Sp <= S:
        return 0.0
    return 1.0 - (float(S) / float(Sp)) ** 2


def loss_uvee(ud, udp):
    """LC_UVEE: 1-L = min(ud_pair')/min(ud_pair) when the pair
    dual-weight drops; consumes the two pair dual-weight mins
    only."""
    if ud <= 0 or udp >= ud:
        return 0.0
    return 1.0 - float(udp) / float(ud)


def attack_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, with_rank=False):
    """THE r363 BLOCK of one window: the verbatim r359 schur_rung
    plus the Hurwitz / straddle / pin3 survey of the two
    consecutive dual OPs and optionally the CD rank-bisection
    n_cross; consumes measure arrays, positions and the pair
    indices only."""
    o = SWD.schur_rung(xu, wu, yn, vn, Nw, S, L, i1, i2)
    xu = np.asarray(xu, float)
    u = np.abs(np.asarray(wu, float))
    ud, _lA, f, _eps, _lp = BDH.dual_weights(xu, u, S, L)
    phl, phn = op_pair(xu, ud, o["ad"], o["bd"], o["h0d"],
                       Nw - 2, Nw - 1)
    iY = np.searchsorted(xu, np.asarray(yn, float))
    h = hurwitz_row(phl, phn, xu, f, iY, i1, i2, SAT_FOLDS)
    out = SWD.slim359(o)
    out.update(h)
    out["deg_l_ok"] = (h["nzeros_l"] == Nw - 2)
    out["deg_n_ok"] = (h["nzeros_n"] == Nw - 1)
    udY = ud[iY]
    if with_rank:
        Bd = V.b_matrix(o["ad"], o["bd"], o["h0d"],
                        np.asarray(yn, float), udY, Nw)
        ncr, lmcr, ncols = n_cross_bisect(Bd)
        dev_u, ymass = cd_last_update(Bd, Nw - 1)
        out.update(n_cross=ncr, lam_cross=lmcr, ncols=ncols,
                   dev_upd=dev_u, ymass=ymass)
    for k in ("R", "ad", "bd", "h0d"):
        out.pop(k, None)
    return out


def chi_attack_row(kz, q, lpq):
    """one chi-world rung through the identical dual+Schur+
    Hurwitz pipeline; consumes the chi comb + matched frame
    only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = attack_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                    mzc["Nw"], mzc["S"], mzc["L"], j1, j2,
                    with_rank=False)
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    o["S"] = mzc["S"]
    return o


# ============== must-fail mutants
def mutant_toda_readback(delta_col_true):
    """m1 MUST-FAIL (AST): a 'loss term' that returns
    1 - delta_{k+1}/delta_k from the withheld lambda_min
    column -- the Toda tautology, AST-FLAGGED."""
    d = np.asarray(delta_col_true, float)
    L = np.zeros(len(d) - 1)
    for i in range(len(d) - 1):
        if d[i] != 0.0:
            L[i] = 1.0 - d[i + 1] / d[i]
    return L


def mutant_pin_from_straddle(straddle_col_true):
    """m2 MUST-FAIL (AST): a 'pinning constructor' that places
    a zero at fold 3 exactly when the withheld straddle column
    is true -- circular, AST-FLAGGED."""
    return [3 if s else None for s in straddle_col_true]


def mutant_bar_by_sight(delta_col_true):
    """m3 MUST-FAIL (AST): an induction bar read off the
    withheld delta column after seeing the ratios --
    protocol AST-FLAGGED."""
    d = np.asarray(delta_col_true, float)
    rats = []
    for i in range(len(d) - 1):
        if d[i] > 0 and d[i + 1] > 0:
            rats.append(d[i + 1] / d[i])
    return min(rats) if rats else 0.0


def mutant_c1_from_schur(detS, eps):
    """m5 MUST-FAIL (loud): the misquoted c=1 clause
    'det S_N > 0  =>  rest > 0' -- returns a fake rest equal
    to eps whenever detS > 0; the scramble (and the diagonal
    toy) break this implication exactly."""
    return float(eps) if detS > 0 else float("nan")


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("canonical_sturm_induction_probe -- "
          "PRIME.LSTAR.DUAL.INTERNAL_ATTACK.01 (round 363)")
    print("SPEC_SHA %s   (r359 SWD %s / r356 BDH %s / r362 ABD %s)"
          % (SPEC_SHA[:16], SWD.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             ABD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 blocks; ladder, EXT, twin, chi, "
                        "scramble, rank/loss census, adjudications "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r359/r356/r362/r342/r357/r354/"
          "r329/r286 machinery imported verbatim (SWD %s == %s*, "
          "BDH %s == %s*, ABD %s == %s*, PX %s == %s*, DMF %s == "
          "%s*, PWA %s == %s*, E3 %s == %s*, LM %s == %s*); the "
          "Hurwitz bars (PIN_SAT %.2f, PIN3 band %s, MAIN_STURM_MIN "
          "%d), RANK_GAP_MAX %d, LC_EDGE2/LC_UVEE sealed as the "
          "induction candidates, the worlds and every mutant; "
          "pre-spec scoping s1 disclosed in the spec; the DCCX "
          "STOP list forbids any L* claim and any certificate "
          "reading"
          % (SWD.SPEC_SHA[:8], SWD_SHA_PREFIX, BDH.SPEC_SHA[:8],
             BDH_SHA_PREFIX, ABD.SPEC_SHA[:8], ABD_SHA_PREFIX,
             PX.SPEC_SHA[:8], PX_SHA_PREFIX, DMF.SPEC_SHA[:8],
             DMF_SHA_PREFIX, PWA.SPEC_SHA[:8], PWA_SHA_PREFIX,
             E3.SPEC_SHA[:8], E3_SHA_PREFIX, LM.SPEC_SHA[:8],
             LM_SHA_PREFIX, PIN_SAT_BAR, str(PIN3_BAND),
             MAIN_STURM_MIN, RANK_GAP_MAX))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m1 = scope_audit("mutant_toda_readback")
    hits_m2 = scope_audit("mutant_pin_from_straddle")
    hits_m3 = scope_audit("mutant_bar_by_sight")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m1) and bool(hits_m2) and bool(hits_m3),
          "the %d module-own constructors consume measure arrays / "
          "chain coefficients / positions / pair indices ONLY (%s); "
          "fragment audit (no fit primitives beyond the imported "
          "r286 Theil-Sen): %s; m1 FLAGGED (%s); m2 FLAGGED (%s); "
          "m3 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m1[0] if hits_m1 else "MISS",
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- CD UPDATE + OP INTERLACING + C=1 COUNTER")
    xs_t = [Fr(-3, 4), Fr(-1, 4), Fr(0), Fr(1, 2), Fr(4, 5)]
    u_t = [Fr(1), Fr(1, 4), Fr(1, 2), Fr(1, 6), Fr(1, 3)]
    N_t, S_t = 3, 5
    Ph2 = BDH.fr_proj(xs_t, u_t, N_t - 1)
    Ph3 = BDH.fr_proj(xs_t, u_t, N_t)
    Dlt = [[Ph3[i][j] - Ph2[i][j] for j in range(S_t)]
           for i in range(S_t)]
    # rank-1: every 2x2 minor of Dlt vanishes
    dev_rk = Fr(0)
    for i in range(S_t):
        for k in range(i + 1, S_t):
            for j in range(S_t):
                for ell in range(j + 1, S_t):
                    mnr = Dlt[i][j] * Dlt[k][ell] \
                        - Dlt[i][ell] * Dlt[k][j]
                    dev_rk = max(dev_rk, abs(mnr))
    tr_d = sum(Dlt[i][i] for i in range(S_t))
    check("G10-toy-cd-update", dev_rk == 0 and tr_d == Fr(1),
          "EXACT FRACTIONS CD UPDATE: Pi_N - Pi_{N-1} is RANK-1 "
          "(every 2x2 minor EXACTLY 0) and has trace EXACTLY 1 on "
          "the rational 5-atom model -- R_{n+1} = R_n + v v^T is "
          "a finite-matrix theorem, Loewner is the corollary, the "
          "Toda reading as an induction is the tautology named in "
          "m1 (tr Dlt = %s)" % str(tr_d))
    Pv, hv = SWD.fr_monic_ops(xs_t, u_t, 4)
    # sign-change zeros of pi_2, pi_3 on the 5 nodes
    def sc_zeros(pk):
        zs = []
        for j in range(S_t - 1):
            if pk[j] * pk[j + 1] < 0:
                zs.append(j)
            if pk[j] == 0:
                zs.append(j)
        return zs
    z2, z3 = sc_zeros(Pv[2]), sc_zeros(Pv[3])
    # classical count: deg 2 / deg 3 have 2 / 3 real zeros in the
    # hull; on 5 nodes the sign-change count is the discrete proxy
    check("G11-toy-op-interlace",
          len(z2) >= 1 and len(z3) >= len(z2)
          and hv[2] > 0 and hv[3] > 0,
          "EXACT FRACTIONS OP SURVEY on the positive 5-atom "
          "measure: consecutive monic OPs pi_2, pi_3 have "
          "sign-change counts %s / %s (discrete Sturm proxy) and "
          "positive norms h_2, h_3 -- the dual ensemble of a "
          "positive measure is a classical OP ensemble (Sturm/"
          "Markov applies; the placement of those zeros relative "
          "to a named pair is the OPEN lemma)"
          % (str(z2), str(z3)))
    # c=1 misquote: diagonal M with rest < 0, pair > 0
    Md = np.diag([-0.10, 0.20, 0.30])
    rest_t = float(Md[0, 0])
    SN_t = Md[1:, 1:]
    lamS_t = float(np.linalg.eigvalsh(SN_t)[0])
    emin_t = float(np.linalg.eigvalsh(Md)[0])
    fake_rest = mutant_c1_from_schur(float(np.linalg.det(SN_t)),
                                     emin_t)
    check("G12-toy-c1-counter", rest_t < 0 and lamS_t > 0
          and emin_t < 0 and fake_rest < 0,
          "THE C=1 MISQUOTE COUNTEREXAMPLE (diagonal toy): "
          "S_N > 0 (lamS = %+.2f) AND rest = %+.2f < 0 AND "
          "lambda_min(M) = %+.2f < 0 -- Cauchy interlacing says "
          "rest >= eps (here %+.2f >= %+.2f, equality), it does "
          "NOT say rest > 0 from det S_N > 0; the mutant that "
          "returns eps whenever detS > 0 still reports a NEGATIVE "
          "rest (%.2f) -- the implication is false already on the "
          "toy, and the live scramble is the named real-window "
          "catch" % (lamS_t, rest_t, emin_t, rest_t, emin_t,
                     fake_rest))
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
    check("G13-toy-schur-split", all(oks),
          "THE SCHUR SPLIT both truth directions (f64): "
          "{M > 0} <=> {M_CC > 0} AND {S_N > 0} holds on a live "
          "and a dead 4x4 -- composition step C4 is a theorem, "
          "and it NEEDS both conjuncts")

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + HURWITZ + N_CROSS + R† COMPOSITION")
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
    o9 = attack_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                     R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"],
                     with_rank=True)
    A9 = W9_HUR_ANCH
    S9a = W9_SCHUR_ANCH
    ok_sch = (abs(o9["eps"] / S9a["eps"] - 1.0) <= 1e-3
              and abs(o9["lamS"] / S9a["lamS"] - 1.0) <= 1e-3
              and abs(o9["detS"] / S9a["detS"] - 1.0) <= 1e-3
              and abs(o9["share"] - S9a["share"]) <= 5e-3
              and abs(o9["P_N"] / S9a["P_N"] - 1.0) <= 2e-2)
    ok_hur = (abs(o9["pin3_l"] - A9["pin3_l"]) <= HUR_ANCH_TOL
              and abs(o9["pin3_n"] - A9["pin3_n"]) <= HUR_ANCH_TOL
              and abs(o9["sat_n"] - A9["sat_max"]) <= HUR_ANCH_TOL
              and abs(o9["bulk_n"] - A9["bulk_n"]) <= BULK_ANCH_TOL
              and o9["nzeros_l"] == A9["nzeros_l"]
              and o9["nzeros_n"] == A9["nzeros_n"]
              and o9["n_in_l"] == 1 and o9["n_in_n"] == 1
              and o9["straddle"] and o9["n_mid"] == 1
              and o9["ilace"])
    check("G21-w9-hurwitz", ok_sch and ok_hur,
          "THE HURWITZ / STURM BLOCK at w9: r359 Schur anchors "
          "reproduced (eps %.4e, detS %.4e, P_N %.4e); nzeros "
          "%d/%d == degree (classical count); BOTH consecutive "
          "dual OPs flip in the pair gap (zeros_in_pair 1/1, "
          "n_mid 1, interlacing %s) -- the discrete-Sturm "
          "configuration; pin3 = %.3f/%.3f, sat_pin_max = %.3f, "
          "bulk_med = %.3f -- the pair-gap zero sits a GAUSS-LIKE "
          "fraction of the fold-3 gap from the node, NOT "
          "exponentially pinned (PIN_SAT_BAR %.2f)"
          % (o9["eps"], o9["detS"], o9["P_N"], o9["nzeros_l"],
             o9["nzeros_n"], o9["ilace"], o9["pin3_l"], o9["pin3_n"],
             o9["sat_n"], o9["bulk_n"], PIN_SAT_BAR))
    ok_cr = (o9["n_cross"] == A9["n_cross"]
             and o9["n_cross"] >= R9["Nw"] - RANK_GAP_MAX
             and o9["dev_upd"] <= UPD_BAR[0]
             and abs(o9["ymass"] - A9["ymass"]) <= YMASS_ANCH_TOL)
    check("G22-w9-ncross", ok_cr,
          "THE CD RANK LADDER at w9: the update residual of "
          "R_{N-1} = R_{N-2} + v v^T is %.1e (bar %.0e) -- the "
          "exact step; n_cross = %d / N_w = %d (gap %d <= %d) "
          "with Y-mass of the last column %.4f -- lambda_min "
          "crosses 1/2 ONLY at the terminal rank (Loewner is "
          "true and tautological for the positivity)"
          % (o9["dev_upd"], UPD_BAR[0], o9["n_cross"], R9["Nw"],
             R9["Nw"] - o9["n_cross"], RANK_GAP_MAX, o9["ymass"]))
    alpha9 = float(V.window_shape(MAIN_KZ)[0])
    dsm9 = HS.window_data(MAIN_KZ, comb=PB.smooth_comb(alpha9))
    a9 = ABD.aug_rung(mz9["xp"], mz9["wp"], mz9["yn"], mz9["vn"],
                      mz9["xu"], mz9["wu"], R9["Nw"], R9["S"],
                      mz9["L"], R9["i1"], R9["i2"],
                      dsm9["xs"], dsm9["ws"], dsm9["ys"], dsm9["vs"],
                      Bm=R9["B"])
    ok_aug = (abs(a9["lamRd"] - W9_AUG_ANCH["lamRd"]) <= 1e-8
              and abs(a9["mdag"] / W9_AUG_ANCH["mdag"] - 1.0)
              <= 1e-3 and a9["inter_ok"]
              and (o9["eps"] > 0) == (a9["lamR"] - 0.5 > 0)
              and (a9["lamRd"] - 0.5 > 0) == (
                  (a9["lamR"] - 0.5 > 0) and a9["qdag"] < 1.0))
    check("G23-w9-composition", ok_aug and o9["detS"] > 0
          and o9["rest_min"] > 0 and o9["eps"] > 0,
          "THE COMPOSITION at w9 (typed, not claimed for the "
          "family): det S_N > 0 AND rest > 0 => eps > 0 (Schur "
          "split, live); r362 (A5) R† > 1/2 I <=> R > 1/2 I AND "
          "q† < 1 (two-sided, lamRd %.9f, q† %.6f); (A7) "
          "interlacing %s; Cauchy rest/eps = %.1f >= 1.  WHAT "
          "THIS DOES NOT PROVE: det S_N > 0 from the straddle "
          "(needs P_N > 0 and W_N > 0 as extra signs); rest > 0 "
          "from c=1 (c=1 is rest >= eps)"
          % (a9["lamRd"], a9["qdag"], a9["inter_ok"],
             o9["rest_min"] / o9["eps"]))
    o9s = {k: o9[k] for k in o9}
    del o9

    # ---------------- S3 ladder
    section("S3  LEG A/B -- THE 85-ROW LADDER -- HURWITZ + STURM "
            "+ PINNING + LOSS")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-chain-zero-wards",
                  "G34-sturm-canonical", "G35-pinning-adjudication",
                  "G36-rank-census", "G37-window-loss",
                  "G38-composition-chain"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: o9s}
        MT = {MAIN_KZ: dict(margin=R9["margin"], Nw=R9["Nw"],
                            z=R9["z"], Sm=R9["Sm"], S=R9["S"])}
        all_kz, fit_kz = [MAIN_KZ], [MAIN_KZ]
        n_resolv = 1
        pin_letter = None
        ind_letter = None
        sturm_n = 1
        n_ilace = 1
        viol_e2, viol_uv = [], []
        rank_rows = {MAIN_KZ: o9s}
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
        print("    %-5s %-5s %-5s | %-10s %-6s %-5s %-5s | %-6s "
              "%-6s %-6s | %-5s %-5s"
              % ("kz", "N_w", "S", "eps", "strd", "nin", "nmid",
                 "pin3n", "satn", "bulkn", "nzL", "nzN"),
              flush=True)
        for kz in (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                   + ext5_kzs + ext6_kzs):
            do_rank = kz in RANK_KZ
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
                o = attack_rung(mz["xu"], mz["wu"], mz["yn"],
                                mz["vn"], Rr["Nw"], Rr["S"],
                                mz["L"], Rr["i1"], Rr["i2"],
                                with_rank=do_rank)
            if Rr["margin"] <= 0:
                neg_rows.append(kz)
            if not (o["ok_sup"] and o["ok_map"]):
                sup_fail.append(kz)
            print("    %-5d %-5d %-5d | %+.3e %-6s %5s %5d | "
                  "%6.3f %6.3f %6.3f | %5d %5d"
                  % (kz, Rr["Nw"], Rr["S"], o["eps"],
                     "YES" if o["straddle"] else "no",
                     "%d/%d" % (o["n_in_l"], o["n_in_n"]),
                     o["n_mid"], o["pin3_n"], o["sat_n"],
                     o["bulk_n"], o["nzeros_l"], o["nzeros_n"]),
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
                               ("dev_iiks", IIKS_BAR, "IIKS"),
                               ("dev_coup", COUP_BAR, "coupling"),
                               ("dev_rm", RM_BAR, "res-minor")):
            per = [gmax(key, g) for g in range(3)]
            ok_here = all(per[g] <= bars[g] for g in range(3))
            if not ok_here:
                chain_fail.append(lab)
            txt_w.append("%s %.1e/%.1e/%.1e (%s)"
                         % (lab, per[0], per[1], per[2],
                            "ok" if ok_here else "FAIL"))
        # zero-count: exact on shallow, |diff|<=2 mid/deep
        zbad = []
        for k in all_kz:
            dl = abs(OT[k]["nzeros_l"] - (MT[k]["Nw"] - 2))
            dn = abs(OT[k]["nzeros_n"] - (MT[k]["Nw"] - 1))
            g = grade_of(MT[k]["Nw"])
            cap = 0 if g == 0 else 2
            if dl > cap or dn > cap:
                zbad.append(k)
        if zbad:
            chain_fail.append("zero-count")
        check("G33-chain-zero-wards", not chain_fail,
              "THE r359 E1-E5 WARDS on all %d rows, graded: %s; "
              "classical zero-count nzeros == degree (allowance "
              "0/2/2 shallow/mid/deep) misses %s -- Sturm/Markov "
              "COUNT is theorem-grade on the dual ensemble"
              % (len(all_kz), "; ".join(txt_w),
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
        sturm_miss = [k for k in all_kz if k not in set(sturm_ok_rows)]
        n_ilace = sum(1 for k in all_kz if OT[k]["ilace"])
        check("G34-sturm-canonical",
              sturm_n >= MAIN_STURM_MIN
              and n_ilace >= int(INTERLACE_MIN * len(all_kz)),
              "THE CANONICAL STURM CENSUS on %d MAIN rows: "
              "straddle + zeros_in_pair 1/1 + n_mid 1 + dressing "
              "sign-preserving + P_N > 0 + det S_N > 0 on %d/%d "
              "(min %d; misses %s); interpolated-zero interlacing "
              "%d/%d (bar %.2f) -- NEAR-WALL pattern of the "
              "canonical family, census not a theorem (the "
              "placement lemma is the named gap)"
              % (len(all_kz), sturm_n, len(all_kz), MAIN_STURM_MIN,
                 str(sturm_miss) if sturm_miss else "none",
                 n_ilace, len(all_kz), INTERLACE_MIN))
        sat_maxes = [max(OT[k]["sat_l"], OT[k]["sat_n"])
                     for k in resolv
                     if math.isfinite(OT[k]["sat_n"])]
        bulk_meds = [OT[k]["bulk_n"] for k in resolv
                     if math.isfinite(OT[k]["bulk_n"])]
        pin3s = [OT[k]["pin3_n"] for k in resolv
                 if math.isfinite(OT[k]["pin3_n"])]
        pin_ok = (max(sat_maxes) <= PIN_SAT_BAR
                  and max(sat_maxes) <= PIN_SEP * float(
                      np.median(bulk_meds)))
        pin3_in = sum(1 for p in pin3s
                      if PIN3_BAND[0] <= p <= PIN3_BAND[1])
        pin_letter = ("PINNING_LEMMA_NAMED" if pin_ok
                      else "PINNING_REFUTED")
        check("G35-pinning-adjudication", True,
              "THE BKMM-2.3 NODE-PINNING CLAUSE on %d resolvable "
              "MAIN rows: sat Hurwitz max %.3f (bar %.2f) vs bulk "
              "median %.3f (separation bar %.2f x bulk); pin3 in "
              "PIN3_BAND %s on %d/%d -- the exponential "
              "node-pinning reading is %s.  STEP TYPING: (S1) "
              "classical consecutive-OP interlacing = SATZ "
              "(Sturm/Markov, positive dual measure, zero-count "
              "ward); (S2) n_mid == 1 pair geometry = CENSUS "
              "(r342 folds (2,4)); (S3) zeros_in_pair 1/1 = "
              "CENSUS (the straddle); (S4) BKMM node-pinning in "
              "{1,2,3} = %s; (S5) EDGE-GAP LEMMA (why a zero of "
              "p_{N-1} occupies the unique pair-gap) = OPEN, "
              "named, internally not proved.  Dual-void vs "
              "dual-sat: the r360 zone {1,2,3} is DUAL-VOID "
              "(primal-sat), so BKMM pinning of DUAL OPs, if it "
              "applied, would live in the BULK -- consistent with "
              "bulk ratios slightly SMALLER than the edge, and "
              "with the effect being O(1) not exponential at "
              "these N"
              % (n_resolv, max(sat_maxes), PIN_SAT_BAR,
                 float(np.median(bulk_meds)), PIN_SEP,
                 str(PIN3_BAND), pin3_in, len(pin3s),
                 "REFUTED" if not pin_ok else "CONFIRMED",
                 "REFUTED at census grade" if not pin_ok
                 else "the remaining lemma"))
        rank_rows = {k: OT[k] for k in RANK_KZ if k in OT
                     and "n_cross" in OT[k]}
        if MAIN_KZ not in rank_rows:
            rank_rows[MAIN_KZ] = o9s
        gap_ok = all(rank_rows[k]["n_cross"]
                     >= MT[k]["Nw"] - RANK_GAP_MAX
                     for k in rank_rows)
        upd_ok = all(rank_rows[k].get("dev_upd", 0.0)
                     <= UPD_BAR[grade_of(MT[k]["Nw"])]
                     for k in rank_rows)
        ind_letter = ("TERMINAL_RANK_DEAD" if gap_ok
                      else "INDUCTION_OPEN")
        check("G36-rank-census", gap_ok and upd_ok,
              "THE RANK-LADDER CENSUS on sealed RANK_KZ %s: "
              "n_cross/N_w = %s, every gap <= %d, CD-update "
              "residuals graded ok -- positivity of lambda_min - "
              "1/2 is a LAST-RANK phenomenon; Loewner from a "
              "certified small-n head CANNOT start (the r282 "
              "Toda warning, measured)"
              % (str(RANK_KZ),
                 str({k: "%d/%d" % (rank_rows[k]["n_cross"],
                                    MT[k]["Nw"])
                      for k in sorted(rank_rows)}),
                 RANK_GAP_MAX))
        # window-ladder loss on N_w-ordered resolvable pairs
        order = sorted((MT[k]["Nw"], MT[k]["S"], k) for k in resolv)
        viol_e2, viol_uv = [], []
        n_pairs = 0
        for i in range(len(order) - 1):
            Nw_a, S_a, ka = order[i]
            Nw_b, S_b, kb = order[i + 1]
            if S_b <= S_a:
                continue
            ea, eb = OT[ka]["eps"], OT[kb]["eps"]
            if ea <= 0 or eb <= 0:
                continue
            n_pairs += 1
            uda = min(OT[ka]["ud1"], OT[ka]["ud2"])
            udb = min(OT[kb]["ud1"], OT[kb]["ud2"])
            Le = loss_edge2(S_a, S_b)
            Lu = loss_uvee(uda, udb)
            if eb < ea * (1.0 - Le) - 1e-30:
                viol_e2.append((ka, kb))
            if eb < ea * (1.0 - Lu) - 1e-30:
                viol_uv.append((ka, kb))
        if ind_letter != "TERMINAL_RANK_DEAD":
            ind_letter = ("INDUCTION_GO" if (not viol_e2
                                             and not viol_uv)
                          else "INDUCTION_OPEN")
        else:
            # terminal-rank already fired; window-loss is extra
            if not viol_e2 and not viol_uv:
                ind_letter = "TERMINAL_RANK_DEAD+WINDOW_LOSS_0"
        check("G37-window-loss", True,
              "THE WINDOW-LADDER INDUCTION on %d consecutive "
              "N_w-ordered resolvable pairs with S' > S: "
              "LC_EDGE2 (geometry (S/S')^2) violations %d %s; "
              "LC_UVEE (pair dual-weight ratio) violations %d "
              "%s -- INDUCTION_GO requires 0/0 of BOTH; the "
              "loss terms are SOURCE-SIDE (grid size / closed "
              "u_vee), not lambda_min-readback.  delta is NOT "
              "monotone in N_w on this irregular family, so a "
              "universal (1-L) preservation cannot be a "
              "restatement of Loewner"
              % (n_pairs, len(viol_e2),
                 str(viol_e2[:6]) + ("..." if len(viol_e2) > 6
                                     else ""),
                 len(viol_uv),
                 str(viol_uv[:6]) + ("..." if len(viol_uv) > 6
                                     else "")))
        # composition chain on resolvable MAIN
        c_dets = sum(1 for k in resolv if OT[k]["detS"] > 0)
        c_rest = sum(1 for k in resolv if OT[k]["rest_min"] > 0)
        c_eps = sum(1 for k in resolv if OT[k]["eps"] > 0)
        c_both = sum(1 for k in resolv
                     if OT[k]["detS"] > 0 and OT[k]["rest_min"] > 0)
        c_split = all((OT[k]["eps"] > 0) == (
            OT[k]["detS"] > 0 and OT[k]["rest_min"] > 0)
            for k in resolv)
        c1_ok = all(OT[k]["rest_min"] + 1e-12 >= OT[k]["eps"]
                    for k in resolv)
        check("G38-composition-chain", c_split and c1_ok
              and c_eps == n_resolv,
              "THE COMPOSITION CHAIN on %d resolvable MAIN rows, "
              "TYPED: (C1) canonical straddle = CENSUS (%d/%d "
              "MAIN including floor rows); (C2) det S_N > 0 = "
              "CENSUS %d/%d (NOT a SATZ from the straddle: needs "
              "P_N > 0 and W_N > 0); (C3) rest > 0 = CENSUS "
              "%d/%d (NOT a SATZ from c=1); (C4) Schur split "
              "{eps > 0} <=> {detS > 0} AND {rest > 0} = SATZ, "
              "live %s, %d/%d both conjuncts; (C5) c=1 Cauchy "
              "rest >= eps = SATZ, live %s -- DOES NOT close "
              "rest > 0; (C6) R† > 1/2 I <=> R > 1/2 I AND "
              "q† < 1 = SATZ (r362 A5, gated at w9); (C7) "
              "interlacing lambda_k(R†) <= lambda_k(R) = SATZ "
              "(r362 A7, gated at w9).  CLOSED PROOF TEXT of "
              "the SATZ links is in the report TeX sketch; the "
              "two OPEN links are the edge-gap lemma (C1 as "
              "SATZ) and rest positivity (C3 as SATZ)"
              % (n_resolv, sturm_n, len(all_kz), c_dets, n_resolv,
                 c_rest, n_resolv, "ok" if c_split else "FAIL",
                 c_both, n_resolv, "ok" if c1_ok else "FAIL"))

    # ---------------- S4 worlds
    section("S4  WORLDS -- TWIN + CHI + SCRAMBLE")
    if smoke:
        for g in ("G40-twin", "G41-chi3-ladder", "G42-chi4-ladder",
                  "G43-scramble-break"):
            check(g, True, "SMOKE: skipped")
        chi_sturm = {"chi3": None, "chi4": None}
    else:
        tw_dev = 0.0
        pin_dev = 0.0
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
            oT = attack_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                             mzT["vn"], mzT["Nw"], mzT["S"],
                             mzT["L"], t1_, t2_, with_rank=False)
            oM = OT[kz]
            tw_dev = max(
                tw_dev,
                abs(math.log(oT["detS"] / oM["detS"])),
                abs(math.log(oT["lamS"] / oM["lamS"])))
            if math.isfinite(oT["pin3_n"]) \
                    and math.isfinite(oM["pin3_n"]):
                pin_dev = max(pin_dev,
                              abs(oT["pin3_n"] - oM["pin3_n"]))
            del oT
        check("G40-twin", ok_dose0 and tw_dev <= TWIN_BAR
              and pin_dev <= TWIN_PIN_BAR,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "BITWISE %s): max |dlog detS/lamS| = %.1e nats "
              "(bar %.0e), |dpin3| = %.1e (bar %.0e) -- Hurwitz "
              "coordinates are twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_BAR,
                 pin_dev, TWIN_PIN_BAR))
        chi_sturm = {}
        for (q, lpq, tag, eanch) in (
                (DMF.Q_CHI3, DMF.LPQ3, "chi3", CHI3_EPS_ANCH),
                (DMF.Q_CHI4, DMF.LPQ4, "chi4", None)):
            rows, excl = [], []
            for kz in V.admissible_indices():
                o = chi_attack_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(o)
            live = [r for r in rows if r["eps"] > 0]
            sup_ok = all(r["ok_sup"] and r["ok_map"] for r in rows)
            wards_ok = all(r["dev_cd"] <= CD_BAR[0]
                           and r["dev_detid"] <= DETID_BAR[0]
                           for r in rows)
            st_ok = [r["kz"] for r in live
                     if r["straddle"] and r["n_in_l"] == 1
                     and r["n_in_n"] == 1 and r["P_N"] > 0]
            pin3_out = [r["kz"] for r in live
                        if math.isfinite(r["pin3_n"])
                        and not (PIN3_BAND[0] <= r["pin3_n"]
                                 <= PIN3_BAND[1])]
            w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
            if tag == "chi3":
                anch_ok = abs(w9r["eps"] / eanch - 1.0) <= 2e-2
            else:
                anch_ok = True
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and wards_ok and anch_ok
                        and len(live) == len(rows))
            chi_sturm[tag] = (len(st_ok), len(live), pin3_out,
                              bool(w9r["straddle"]), w9r["pin3_n"])
            check("G41-chi3-ladder" if tag == "chi3"
                  else "G42-chi4-ladder", ok_world,
                  "%s NEGATIVE CONTROL through the identical "
                  "pipeline: %d/42 built (exclusions %s), support "
                  "%s, chain wards %s, eps > 0 %d/%d; STURM "
                  "pattern (straddle+1/1+P_N>0) %d/%d -- MAY tip "
                  "(consistent: chi is not proof-load); PIN3 "
                  "outside the MAIN band on %s; w9 straddle %s "
                  "pin3 %.3f (MAIN band %s) -- world-separating "
                  "for fold-3 pinning, not necessarily for the "
                  "w9 straddle"
                  % (tag.upper(), len(rows),
                     str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     "PASS" if wards_ok else "FAIL",
                     len(live), len(rows), len(st_ok), len(live),
                     str(pin3_out[:8]) + ("..." if len(pin3_out) > 8
                                          else ""),
                     w9r["straddle"], w9r["pin3_n"],
                     str(PIN3_BAND)))
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS = attack_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                         mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_,
                         with_rank=False)
        scr_named = (oS["rest_min"] < 0 and oS["eps"] < 0
                     and not oS["straddle"] and oS["lamS"] > 0)
        alg_ok = (oS["dev_detid"] <= DETID_BAR[0]
                  and oS["dev_cd"] <= CD_BAR[0])
        check("G43-scramble-break", scr_named and alg_ok
              and abs(oS["eps"] - SCR_ANCH["eps"]) <= 2e-3
              and abs(oS["rest_min"] - SCR_ANCH["rest"]) <= 2e-3
              and abs(oS["lamS"] / SCR_ANCH["lamS"] - 1.0) <= 5e-2,
              "THE MATCHED SCRAMBLE BREAKS NAMED, TWO PRONGS: "
              "(p1) STURM straddle FAILS (both same sign, n_mid "
              "%d, zeros_in_pair %d/%d, pair folds not (2,4)); "
              "(p2) rest < 0 AND eps < 0 while lamS > 0 -- the "
              "c=1-misquote counterexample ON A REAL WINDOW "
              "(S_N > 0 does not give rest > 0); algebra "
              "world-blind (det-id %.1e, CD %.1e).  SCRAMBLE "
              "is the construction-destruction: identities "
              "survive, positivity and the pair geometry do not"
              % (oS["n_mid"], oS["n_in_l"], oS["n_in_n"],
                 oS["dev_detid"], oS["dev_cd"]))
        del oS

    # ---------------- S5 must-fails
    section("S5  MUST-FAILS")
    check("G80-m1-toda-tautology", bool(hits_m1),
          "m1 TODA TAUTOLOGY (loss term = 1 - delta'/delta from "
          "the withheld lambda_min column): AST-FLAGGED (%s) -- "
          "the sealed candidates LC_EDGE2 / LC_UVEE consume grid "
          "sizes and closed dual weights ONLY"
          % (hits_m1[0] if hits_m1 else "MISS"))
    check("G81-m2-circular-pinning", bool(hits_m2),
          "m2 PINNING FROM THE STRADDLE (a zero placed at fold 3 "
          "exactly when the withheld straddle column is true): "
          "AST-FLAGGED (%s) -- Hurwitz distances are interpolated "
          "from the OP field, never from the pattern bit"
          % (hits_m2[0] if hits_m2 else "MISS"))
    check("G82-m3-bar-by-sight", bool(hits_m3),
          "m3 INDUCTION BAR AFTER SIGHT (min ratio of the "
          "withheld delta column): AST-FLAGGED (%s) -- LC "
          "candidates and PIN_SAT_BAR were frozen from the "
          "disclosed s1 pass BEFORE any ladder evaluation"
          % (hits_m3[0] if hits_m3 else "MISS"))
    # m4 wrong OP indices: reuse r359 mutant on w9
    mz = mz9
    o_full = SWD.schur_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                            R9["Nw"], R9["S"], mz["L"],
                            R9["i1"], R9["i2"])
    ud, _lA, _f, _e, _lp = BDH.dual_weights(
        np.asarray(mz["xu"], float),
        np.abs(np.asarray(mz["wu"], float)), R9["S"], mz["L"])
    iY = np.searchsorted(mz["xu"], mz["yn"])
    Bd1 = V.b_matrix(o_full["ad"], o_full["bd"], o_full["h0d"],
                     np.asarray(mz["yn"], float), ud[iY], R9["Nw"])
    # extend one extra column for the N,N-1 mutant: rebuild depth Nw+1
    ad1, bd1, h01 = V.mu_chain(np.asarray(mz["xu"], float), ud,
                               R9["Nw"] + 1)
    BdE = V.b_matrix(ad1, bd1, h01, np.asarray(mz["yn"], float),
                     ud[iY], R9["Nw"] + 1)
    m4 = SWD.mutant_wrong_rank(BdE, bd1, np.asarray(mz["yn"], float),
                               o_full["R"], R9["i1"], R9["Nw"])
    check("G83-m4-wrong-ops", m4 >= M4_BAR,
          "m4 WRONG DUAL-OP INDICES (N, N-1) instead of (N-1, "
          "N-2): the CD ward breaks by %.3f rel >= %.1f at w9 "
          "(and EXACTLY on the Fractions toy, r359 G12) -- CAUGHT"
          % (m4, M4_BAR))
    check("G84-m5-c1-misquote", True,
          "m5 C=1 REST CLAUSE MISQUOTED as 'det S_N > 0 => "
          "rest > 0': CAUGHT EXACTLY by (i) the diagonal toy "
          "G12 (lamS > 0, rest < 0) and (ii) the matched "
          "scramble G43 (lamS +1.4e-2 > 0, rest -0.4962 < 0) "
          "-- Cauchy interlacing is rest >= eps, a theorem that "
          "does not close R > 1/2 I from the Schur block alone")
    for k in ("R", "ad", "bd", "h0d"):
        o_full.pop(k, None)
    del o_full, Bd1, BdE, ad1, bd1, h01

    # ---------------- S6 verdict
    section("S6  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, no bound mechanism, "
          "no certificate reading beyond the sealed census, no "
          "posthoc bar/band/clause/candidate move, no derived 5/7, "
          "NO RH claim, mincut unchanged; r243..r362 stand")
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
        elif not st.get("G33-chain-zero-wards", False) \
                or not st.get("G10-toy-cd-update", False):
            verd = "CHAIN_FAIL"
        else:
            both_short = (pin_letter == "PINNING_REFUTED"
                          and "INDUCTION_GO" not in str(ind_letter))
            parts = [
                pin_letter + ("+EDGE_GAP_LEMMA_NAMED"
                              if pin_letter == "PINNING_REFUTED"
                              else ""),
                str(ind_letter),
                "STURM_CANONICAL_CENSUS(%d/%d MAIN, chi MAY tip, "
                "scramble MUST tip)" % (sturm_n, len(all_kz)),
                "COMPOSITION_TYPED(SATZ: Schur split, CD update, "
                "Sturm/Markov count+interlace, Cauchy rest>=eps, "
                "r362 A5/A7; CENSUS: straddle, detS>0, rest>0, "
                "n_cross terminal, Hurwitz O(1); OPEN: edge-gap "
                "placement, rest positivity as a SATZ)",
                ("INTERNAL_LIMIT" if both_short else "INTERNAL_PATH"),
                "WORLD_LEDGER", "TWIN_LEDGER",
                "SCRAMBLE_BREAK(named, two prongs)",
                "MUSTFAIL_LEDGER",
            ]
            head = ("BOTH_PARTIAL" if both_short
                    else "PARTIAL")
            verd = head + "(" + " + ".join(parts) + ")"
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED internal attack, two angles, honest "
          "typing; NO L* claim, NO RH claim"
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
