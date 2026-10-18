#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""compound_cd_wedge_probe --
PRIME.LSTAR.DUAL.COMPOUND_CD.01 (round 371): THE EXTERIOR-SQUARE
KILL TEST -- the canonical two-form of the last two dual CD
columns, ONE run, no nachbessern.  Reviewer solution 3.
Coexistence: R369 / R372 / R373 run in parallel -- this probe
touches NOTHING outside its own file and the strictly additive
rh-sync.  The r367 Haynsworth cut is consumed as ANCHOR: A0,
U, K2, the 45-row P1 set, the nneg-1 / vacuous dichotomy.  The
r363 CD update is the column constructor.  NO L* CLAIM, NO RH
CLAIM, mincut unchanged.

THE EXACT IDENTITY (12).  With u, v the two last dual CD columns
on Y and A0 = R_{N-3} - (1/2) I invertible,
    det K2 = 1 + <u, A0^{-1} u> + <v, A0^{-1} v>
             + <u∧v, (∧² A0^{-1})(u∧v)>,
the last term EXACTLY <u,A0^{-1}u><v,A0^{-1}v> - <u,A0^{-1}v>²
(the Gram determinant of the A0^{-1}-inner product).  K2 is the
r367 matrix I_2 + U^T A0^{-1} U; this identity is finite
algebra (Cauchy-Binet / compound), not a new constructor.

THE CD-STRUCTURE (13).  The canonical wedge ω_N = u_{N-3} ∧
u_{N-2} is ONE two-form, not the bag of all minors (that was
the r318 SR-death, coin-flip on MAIN, ORIGINAL-matrix minors --
it does NOT refute a sign structure of the SECOND compound
matrix on the one-dimensional CD-wedge; the search space is
now tiny).  On Y,
    (u∧v)_ij = c_N · √(υ_i υ_j) · (y_j - y_i) · K_{N-3}(y_i, y_j)
with c_N = 1/b_{N-3} > 0 the dual Jacobi subdiagonal coupling
P_{N-3} → P_{N-2} (three-term recurrence of the dual ensemble).

THE COMPOUND-EDGE-CAPTURE CANDIDATE (14).  On the nneg-1 branch
    <ω, (∧² A0^{-1}) ω> < -1 - <u,A0^{-1}u> - <v,A0^{-1}v>
implies det K2 < 0.  Via (12) this is EQUIVALENT to P2, not an
independent arithmetic; the live question is the SOURCE
SIGNATURE of ω in the second compound resolvent.

AND² INERTIA (the r367 dichotomy, exterior).  ∧² of a matrix
with inertia (p, 1, 0) has inertia (C(p,2), p, 0): the negative
∧²-directions are exactly the products of the one negative
direction of A0 with each positive direction.  On the nneg-1
branch this is nneg(∧² A0) = |Y|-1.  The source-signature
question: does the CD-wedge sit predominantly in that negative
subspace?

THE OVERLOAD THEOREM (parallel).  ind_-(A0) ≤ 1 via a
Stieltjes-contour count (1/2πi) ∮_{Γ_-} tr(A0 - z I)^{-1} dz
< 2 -- the left side is INTEGER, the contour may be coarse.
Sealed construction (source-pure, NOT from the eigenvalues of
A0): the Gershgorin-Stieltjes majorant MAJ = #{i : A_ii - r_i
≤ 0} (disks meeting (-∞, 0]), plus the isolation lemma (a
disjoint cluster of k disks contains exactly k eigenvalues),
plus the occupation-diagonal ledger n_diagneg = #{A_ii < 0}
(r360/r366: min diag(R_CC) > 1/2 is SATZ on the rest block of
the full R; here we measure min diag(A0) = min diag(R_{N-3})
- 1/2).  OVERLOAD_MAJORANT_GO fires only if isolation certifies
a cluster of size < 2 on the nneg-1 branch AND MAJ > 2 on the
scramble (else the construction is vacuous).  Pre-spec scoping
already saw isolation FAIL and MAJ ≫ 2 on BOTH MAIN and
scramble -- the GO letter is not expected to fire; the scramble
vacuity test (MAJ > 2) still binds.

THE LEGS.  (Leg 0) anchors bit-near: r367 columns (A0, U, K2,
the 45-row P1 set, the dichotomy), r363 CD-updates.  (Leg A)
identities exact: (12) Fractions on the 4-node Haynsworth toy
+ f64 ≤ 1e-10 live on resolvable rows; (13) CD-wedge structure
with explicit c_N (Fractions CD-telescope + live dressing).
(Leg B) the compound census / kill test: on the nneg-1 branch
(45 MAIN resolvable + the χ analogs) the sign of the wedge
term, the capture inequality (14), and the ∧²-subspace share
-- bars sealed BEFORE freeze.  Binary question: does the
canonical wedge have a STABLE source signature in the second
compound resolvent (0 violations on the branch) or not?
(Leg C) the overload candidate: the sealed Gershgorin-Stieltjes
construction; honest type if only the nneg≤1 census remains.
(Leg D) worlds + must-fails (≥5): twin bitwise; scramble
(nneg = 21 -- the majorant MUST be > 2, else vacuous; the
wedge term is measured); χ including the terminal-dead
sprouts.  Must-fails: wedge from det K2 readback → AST-CAUGHT;
wrong ∧² convention → exact CAUGHT; bars after sight →
protocol-CAUGHT (ONE run); contour majorant from the
eigenvalues → AST-CAUGHT; c_N sign flipped → exact CAUGHT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO L* CLAIM, NO RH
CLAIM in either direction, mincut unchanged.  Two-commit freeze
protocol (r329 convention): spec + machinery committed BEFORE
the record run, record tables inserted after.  EIN RUN -- bars
are not moved after the freeze; census gates print counts and
do not fail the probe; 0-violation lives in the GO *letter*.

INDEX FIREWALL (binding, r238-r367 discipline): w = window
(kz), S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2, folds
= grid indices; ground truth enters GATES and record tables
only; the module-own constructors consume measure arrays /
chain coefficients / positions / pair indices ONLY (AST scope
audit; withheld identifiers detK_col_true / nneg_col_true /
share_col_true and the REC/anchor constants); no zero/prime
oracles (AST firewall); no fit primitives.  MACHINERY IMPORTED
VERBATIM: r367 FTRI.{cut_rung, haynsworth_toy, grade_of,
inertia_of} (e0d79840), r363 CSI.cd_last_update (09786c2e),
r359 SWD (d00fdc96), r356 BDH.{dual_weights, dual_rung} (36141c0a),
r362 ABD (7d810a9a), r342 PX.{build_rung, pair_select}
(b09f8ccd), r357 DMF.{chi_window_comb, chi_build_measures,
LPQ3, LPQ4, Q_CHI3, Q_CHI4} (4bf1a94b), r354 PWA.rung_reduced_cols
(f9db84da), r329 E3.{admissible_pool, used_kz_set} (bbfaf199),
r286 LM.ext_rule (0a44ac4e), r331 TR.{base_comb, build_world},
r289 AKD.twin_rational, r276 MF.local_gaps, r226 HS.window_data,
r243 PB.smooth_comb, document pipeline V.{build_measures,
mu_chain, b_matrix, admissible_indices, U, PP}, v563 core
READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104,
N_w 184, margin 1.6752e-4 rel 0.01, folds (2, 4)); r367 W9 K2
σ=(-2.7938, 1.8036) detK=-5.0389 nneg=1 EXACT; SAMPLE K2
kz18/44/52 detK -1.1572/-5.5436/-2.6380 rel 1e-3; r367 P1
exact-one 45 / vacuous 29 / overload 0 on 74 resolvable MAIN
(reproduction ward of the nneg-1 branch, not a target
readback); CHI3 W9 nneg=0 detK=+4.0186; CHI4 W9 nneg=1
detK=-6.1804; SCR nneg=21 detK=-8.8814.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; W9_K2_ANCH as r367; W9_WEDGE_ANCH
(s1 scoping, disclosed) wterm -3.0487 rel 1e-3, share 0.6836
abs 5e-2, c_N 1.953 abs 5e-2, nneg2 103 EXACT (= |Y|-1),
n_diagneg 0 EXACT, mind(A0) +3.94e-3 rel 5e-2; SAMPLE_WTERM
rel 1e-3 kz18/44/52 -1.3211/-3.8263/-3.0343; SAMPLE_SHARE abs
5e-2 0.7830/0.7478/0.6748; CHI3_W9 wterm +0.9830 rel 2e-2
share 0 EXACT (no negative ∧² direction); CHI4_W9 wterm
-3.0148 rel 2e-2 share 0.5352 abs 5e-2; SCR_ANCH nneg 21
EXACT, n_hit 49 (vacuity: > 2), n_diagneg 24 (> 2), wterm
-3.0224 rel 5e-2; SHARE_BAR 0.50 (majority in the negative
∧²-subspace; sized from Sol min 0.675 and the χ analog 0.535,
NOT dominant-0.90 -- Sol share is 0.67..0.78, disclosed);
ID_LIVE 1e-10; ID_BAR (1e-10, 1e-9, 1e-7) graded instrument
floor; CN_MIN 0.5 (c_N > 0 with room; Sol ~1.92..2.06);
RESOLV_FLOOR 1e-9; MAJ_SCR_MIN 3 (scramble MAJ > 2);
P1_BRANCH_N 45 / VACUOUS_N 29 / RESOLV_N 74 the r367 census
as a reproduction ward; GRADES shallow N_w <= 900 / mid <=
3200 / deep > 3200; RANK_KZ (18, 9, 44, 52); WORLD_KZ (18, 9,
52, 119, 42, 130); N_CHI_MIN 21; SCR_SEED 1; TWIN_BAR 1e-3
nats on |d wterm|; M5_RATIO 1e6 (flipped-c_N residual over
true residual; smoke-sized -- w9 max|ω_ij| is O(1e-2) so an
absolute 0.1 bar is instrument-dead; disclosed before freeze);
TOY_TOL 1e-12; EXT selections verbatim r356/r367; runtime
<= 1800 s; smoke = toys + firewall + scopes + mutants + w9
blocks (records, identities, wedge, majorant); ladder, EXT,
twin, chi, scramble skipped.

CALIBRATION AMENDMENT a1 (disclosed, first full evaluation
28/30 at 266.4 s, SPEC_SHA 85b31ee99180bf64): G35 used a
SECOND raw 1e-8 floor for nneg(∧² A0) that disagreed with the
r367 Rayleigh-arbitrated inertia on 10/45 P1 rows (deep
near-zeros).  The SATZ is the product formula nneg(∧²) =
nneg(A0)*npos(A0) from the SAME inertia -- tautological on
P1 and now the constructor.  SHARE_BAR, sign definition,
MAJ construction, scramble named-break, identity bars and
the GO letters are NOT moved.  The SHARE finding of the
first evaluation stands: majority 27/45, min 0.001 (the Sol
4/4 sample was terminal-rank biased, same lesson as r367 a1
on P1_VACUOUS).  EIN RUN on the science: no bar nachbessern.

PRE-SPEC SCOPING (disclosed -- ONE sizing pass on kz9/18/44/52
+ chi3/chi4 w9 + scramble w9, /tmp, deleted; no bar, band,
clause or verdict rule tuned after any evaluation except as
sized here and said so): identity (12) residual 0..4e-15;
identity (13) residual ~4e-17 with c_N in (1.92, 2.06) all
positive; on the four MAIN nneg-1 rungs the wedge term is
NEGATIVE (-1.32..-3.83) and capture holds (identity with
det K2 < 0); ∧²-share 0.675..0.783 (majority, NOT dominant);
nneg(∧² A0) = |Y|-1 exact; min diag(A0) > 0 and n_diagneg = 0
on MAIN, scramble n_diagneg = 24; Gershgorin n_hit = 67..483
on MAIN and 49 on scramble, isolation FALSE everywhere -- the
Gershgorin-Stieltjes majorant does NOT certify < 2 on MAIN
(and is > 2 on scramble, so the scramble vacuity test holds
and the construction is not empty).  chi3 w9: nneg=0, wterm
> 0, share = 0 (PD Gram determinant -- world-separating);
chi4 w9: nneg-1 like MAIN, wterm < 0, share 0.535.  The
verdict letters, SHARE_BAR, MAJ construction, scramble named
break (nneg=21 AND MAJ>2) and every bar were frozen from
these numbers BEFORE any ladder-wide evaluation.  EIN RUN:
no calibration amendment path; census gates print and pass;
0-violation is the GO letter only.

VERDICT (frozen enum):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL  iff the rank/support gate fails on any
    real MAIN ladder window /
  CHAIN_FAIL  iff any exact ward fails (Fractions (12)/(13),
    live identity floor graded, ∧² inertia on the toy) /
  otherwise the letters, combinations allowed:
  COMPOUND_SIGNATURE_STABLE  iff 0 violations of (wterm < 0
    AND share >= SHARE_BAR) on the resolvable MAIN nneg-1
    branch AND scramble breaks named /
  CAPTURE_HOLDS_CENSUS  [always with the (14) ledger: capture
    ≡ det K2 < 0 via (12); 0-violation of that identity on
    resolvable MAIN is a ward, the P2 count is census] /
  WEDGE_COIN_FLIP  iff the sign of wterm is mixed on the
    nneg-1 MAIN branch (the r318 death repeating on the
    compound -- honest, route-to) /
  OVERLOAD_MAJORANT_GO  iff the sealed Gershgorin-isolation
    construction certifies cluster size < 2 on every
    resolvable MAIN nneg-1 row AND MAJ > 2 on scramble /
  OVERLOAD_CENSUS_ONLY  iff nneg ≤ 1 remains a census (r367
    overload 0/74 reproduced) and the majorant does not
    certify /
  + AND2_LEDGER + WORLD_LEDGER + TWIN_LEDGER +
    SCRAMBLE_BREAK(nneg=21 named, MAJ>2) + MUSTFAIL_LEDGER
    [always].
Honesty before beauty: (12) and (13) are finite-matrix SATZ;
capture (14) is equivalent to P2 via (12), not independent
arithmetic; a 0-violation census of the wedge sign is NOT a
proof of the sign law; the ∧²-share on the Sol 4/4 is
majority not dominant (disclosed); no verdict claims L*, a
bound mechanism, or RH progress in either direction; the
DCCX STOP list stands.  EIN RUN -- the verdict is accepted
as it falls.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit besides disclosed a1; TWO-COMMIT PROTOCOL:
sealed spec committed as "r371 pre-freeze" (ac7c0b0b, SPEC_SHA
freeze 85b31ee99180bf64, file SHA c7860a863ef19983) BEFORE
the first full evaluation; chronology honest: smoke 30/30
byte-identical; pre-freeze commit ac7c0b0b; first full
evaluation = 28/30 (266.4 s) found a1 (G35 second raw floor
vs Rayleigh inertia, 10/45 P1 near-zeros -- INSTRUMENT, not
a bar move) plus the SHARE finding 27/45; a1 product formula;
record run1 = 30/30 (283.3 s), run2 = 30/30 (239.3 s),
byte-identical up to the WALL line; evaluation SPEC_SHA
179cd387155299dc before this insert):
MAIN VERDICT = SIGNATURE_PARTIAL(wterm<0 45/45, share>=0.50
27/45) + CAPTURE_HOLDS_CENSUS(nneg-1 45/45 via (12) ≡ P2)
+ OVERLOAD_CENSUS_ONLY(cert_lt2 0/45, scramble MAJ>2)
+ AND2_LEDGER(nneg(∧² A0)=|Y|-1 on 45/45 of the branch, share
min/med/max 0.001/0.601/0.905) + WORLD_LEDGER(chi3 nneg-1
21/42 all sign-stable, chi4 19/42 all sign-stable, chi MAY
tip, terminal-dead eps<=0 is 0/42 on the unaugmented A0)
+ TWIN_LEDGER + SCRAMBLE_BREAK(named P1 nneg=21, MAJ=49>2,
wterm=-3.022 measured) + MUSTFAIL_LEDGER.
LEG A: identities are finite-matrix SATZ.  (12) Fractions
toy det K2 = -7 = 1+q11+q22+wterm exact (wterm=-4);
f64 graded 74/74 (maxerr 5.7e-10), live 1e-10 on 72/74
(the two misses kz37/kz95 at 5.7e-10/5.0e-10 sit in the
mid grade 1e-9).  (13) Fractions CD-telescope exact;
live dressing 74/74 at 1e-10 (maxerr 9.1e-17), c_N =
1/b_{N-3} in (1.92, 2.06) all positive.  RANK_KZ
wterm/share anchors PASS.  Wrong ∧² convention λ_i+λ_j
CAUGHT exact (nneg_sum=0 != nneg_prod=3).
LEG B: the kill test.  Wedge SIGN is STABLE on the nneg-1
branch (wterm<0 45/45, range [-637.7, -1.32], 0 flips) --
NOT the r318 coin-flip.  Capture (14) holds 45/45 by
identity (12) ≡ P2 (not independent arithmetic).  The
∧²-subspace share is NOT stable: majority (>=0.50) only
27/45, min 0.001 (kz37/kz95/kz129-class deep rows), max
0.905; the Sol 4/4 sample (0.67..0.78) was terminal-rank
biased.  COMPOUND_SIGNATURE_STABLE does not fire.
nneg(∧² A0)=|Y|-1 on 45/45 (product formula from the r367
inertia, a1).  r367 dichotomy reproduced P1 45 / vacuous 29
/ overload 0 on 74 resolvable.
LEG C: Gershgorin-Stieltjes MAJ = n_hit on the branch
[67, 1425] ≫ 2, isolation 0/45, cert_lt2 0/45 -- the
construction does NOT certify ind_- < 2.  Occupation
diagonal of A0: n_diagneg = 0 on the whole nneg-1 branch
(min diag > 0, the remaining negative is off-diagonal).
Scramble MAJ=49>2 (vacuity test holds, construction not
empty) and n_diagneg=24.  OVERLOAD_MAJORANT_GO stays off;
nneg≤1 remains the r367 census (overload 0/74).
LEG D: twin dose-zero bitwise, |d wterm|=6.2e-5.  chi3
21/42 nneg-1 all wterm<0 (w9 PD, wterm>0, share=0 --
world-separating); chi4 19/42 nneg-1 all wterm<0 (w9
share 0.535).  Scramble named P1 nneg=21, P2 survives,
wterm=-3.022 measured.  Must-fails 5/5 (m1 AST detK
readback, m2 wrong ∧² convention exact, m3 bars-after-
sight AST, m4 majorant-from-eigs AST, m5 c_N sign ratio
3.2e14).
Honesty: the canonical two-form has a STABLE SOURCE SIGN
and an UNSTABLE ∧²-subspace share; capture is algebra;
the overload theorem stays census.  No L* claim, no RH
claim.
"""

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

import final_two_rank_inertia_probe as FTRI          # noqa: E402 r367
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
import verify_lstar_instance as V                    # noqa: E402 document
import v563_paper2_readouts as core                  # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
FTRI_SHA_PREFIX = "e0d79840"
CSI_SHA_PREFIX = "09786c2e"
SWD_SHA_PREFIX = "d00fdc96"
BDH_SHA_PREFIX = "36141c0a"
ABD_SHA_PREFIX = "7d810a9a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
LM_SHA_PREFIX = "0a44ac4e"
W9_SCHUR_ANCH = dict(f1=2, f2=4)
W9_K2_ANCH = dict(ev0=-2.7938, ev1=1.8036, detK=-5.0389, nneg=1)
K2_REL = 1e-3
W9_WEDGE_ANCH = dict(wterm=-3.0487, share=0.6836, cN=1.953,
                     nneg2=103, n_diagneg=0, mind=3.9388e-3)
WTERM_REL = 1e-3
SHARE_ANCH_TOL = 5.0e-2
CN_ANCH_TOL = 5.0e-2
MIND_REL = 5.0e-2
SAMPLE_K2 = {
    18: dict(detK=-1.1572, wterm=-1.3211, share=0.7830),
    44: dict(detK=-5.5436, wterm=-3.8263, share=0.7478),
    52: dict(detK=-2.6380, wterm=-3.0343, share=0.6748),
}
CHI3_W9_ANCH = dict(nneg=0, detK=4.0186, wterm=0.9830, share=0.0)
CHI4_W9_ANCH = dict(nneg=1, detK=-6.1804, wterm=-3.0148,
                    share=0.5352)
SCR_ANCH = dict(nneg=21, detK=-8.8814, n_hit=49, n_diagneg=24,
                wterm=-3.0224)
NW_SHALLOW = 900
NW_MID = 3200
ID_LIVE = 1.0e-10
ID_BAR = (1.0e-10, 1.0e-9, 1.0e-7)
SHARE_BAR = 0.50
CN_MIN = 0.5
RESOLV_FLOOR = 1.0e-9
MAJ_SCR_MIN = 3
P1_BRANCH_N = 45
VACUOUS_N = 29
RESOLV_N = 74
RANK_KZ = (18, 9, 44, 52)
WORLD_KZ = (18, 9, 52, 119, 42, 130)
N_CHI_MIN = 21
SCR_SEED = 1
TWIN_BAR = 1.0e-3
M5_RATIO = 1.0e6              # flipped-c_N residual / true residual
                              # (w9 max|ω_ij| is O(1e-2); an absolute
                              # 0.1 bar is instrument-dead -- sized in
                              # smoke, disclosed, before freeze)
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


CONSTRUCTORS = ("compound_rung", "chi_compound_row", "ident12_from_q",
                "ident13_cd", "wedge_share", "overload_majorant",
                "and2_inertia_from_ev", "fr_cd_telescope",
                "fr_ident12_from_toy")
SCOPE_FORBIDDEN = {"REC_MARGIN", "W9_K2_ANCH", "W9_WEDGE_ANCH",
                   "SAMPLE_K2", "SCR_ANCH", "CHI3_W9_ANCH",
                   "CHI4_W9_ANCH", "SHARE_BAR", "detK_col_true",
                   "nneg_col_true", "share_col_true"}


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
def ident12_from_q(q11, q22, q12, detK):
    """identity (12): det K2 = 1 + q11 + q22 + (q11 q22 - q12^2).
    Consumes the three quadratic forms and det K2 only."""
    wterm = float(q11) * float(q22) - float(q12) * float(q12)
    det_id = 1.0 + float(q11) + float(q22) + wterm
    err = abs(det_id - float(detK))
    capture = wterm < -1.0 - float(q11) - float(q22)
    return dict(wterm=wterm, det_id=det_id, err=err,
                capture=bool(capture))


def ident13_cd(Bd, yn, bd, Nw):
    """identity (13): (u∧v)_ij = c_N (y_j - y_i) R_{N-2,ij}
    with c_N = 1/b_{N-3} > 0 and R_{N-2} = Bd[:, :Nw-2]
    Bd[:, :Nw-2]^T (the √υ-dressed K_{N-3}).  Consumes the
    dual frame on Y, the nodes and the Jacobi b only."""
    u = Bd[:, Nw - 3]
    v = Bd[:, Nw - 2]
    cn = 1.0 / float(bd[Nw - 3])
    Rnm2 = Bd[:, :Nw - 2] @ Bd[:, :Nw - 2].T
    Wedge = np.outer(u, v) - np.outer(v, u)
    dy = yn[np.newaxis, :] - yn[:, np.newaxis]
    pred = cn * dy * Rnm2
    err = float(np.max(np.abs(Wedge - pred)))
    nrm = float(np.max(np.abs(Wedge)))
    rel = err / max(nrm, 1.0)
    return dict(cN=cn, err=err, rel=rel, nrm=nrm,
                bN=float(bd[Nw - 3]))


def wedge_share(u, v, A0):
    """fraction of |ω|^2 in the negative ∧²-subspace of A0
    (products of each negative evec with each positive evec).
    Consumes the two columns and A0 only."""
    A0 = 0.5 * (A0 + A0.T)
    ev, W = np.linalg.eigh(A0)
    uc = W.T @ u
    vc = W.T @ v
    n2 = float(u @ u) * float(v @ v) - float(u @ v) ** 2
    neg_ix = np.where(ev < -1.0e-8)[0]
    pos_ix = np.where(ev > 1.0e-8)[0]
    neg_e = 0.0
    for i in neg_ix:
        for j in pos_ix:
            cij = float(uc[i] * vc[j] - uc[j] * vc[i])
            neg_e += cij * cij
    share = neg_e / n2 if n2 > 1.0e-30 else float("nan")
    nneg = int(np.sum(ev < -1.0e-8))
    npos = int(np.sum(ev > 1.0e-8))
    nzer = int(len(ev) - nneg - npos)
    return dict(share=share, n2=n2, nneg=nneg, npos=npos,
                nzer=nzer, nneg2=int(nneg * npos),
                npos2=int(npos * (npos - 1) // 2
                          + nneg * (nneg - 1) // 2))


def and2_inertia_from_ev(ev, floor=1.0e-8):
    """inertia of ∧² A from the eigenvalues of A: products
    λ_i λ_j for i<j.  Consumes the eigenvalue vector only."""
    ev = np.asarray(ev, float)
    pos = ev[ev > floor]
    neg = ev[ev < -floor]
    npos2 = int(len(pos) * (len(pos) - 1) // 2
                + len(neg) * (len(neg) - 1) // 2)
    nneg2 = int(len(pos) * len(neg))
    nzer2 = int(len(ev) * (len(ev) - 1) // 2 - npos2 - nneg2)
    return npos2, nneg2, nzer2


def overload_majorant(A0):
    """Gershgorin-Stieltjes + occupation-diagonal construction.
    MAJ = n_hit = #{disks meeting (-∞,0]}; isolation = the
    hitting cluster is disjoint from the complement; cert_lt2
    iff isolation holds AND n_hit < 2.  Consumes the symmetric
    matrix only -- never its eigenvalues."""
    A = 0.5 * (A0 + A0.T)
    d = np.diag(A).real.copy()
    r = np.sum(np.abs(A), axis=1) - np.abs(d)
    lo = d - r
    hi = d + r
    hit = lo <= 0.0
    n_hit = int(np.sum(hit))
    n_diagneg = int(np.sum(d < 0.0))
    mind = float(np.min(d))
    iso = False
    if 0 < n_hit < len(d):
        hhi = float(np.max(hi[hit]))
        clo = float(np.min(lo[~hit]))
        hlo = float(np.min(lo[hit]))
        chi = float(np.max(hi[~hit]))
        iso = (hhi < clo) or (chi < hlo)
    cert = bool(iso and n_hit < 2)
    return dict(n_hit=n_hit, n_diagneg=n_diagneg, mind=mind,
                iso=iso, cert_lt2=cert, maj=n_hit)


def compound_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=False):
    """THE r371 BLOCK of one window: r367 two-rank cut plus the
    compound identities (12)(13), the ∧²-share and the sealed
    overload majorant.  Consumes measure arrays, positions and
    the pair indices only."""
    o = FTRI.cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=True)
    xu = np.asarray(xu, float)
    uabs = np.abs(np.asarray(wu, float))
    yn = np.asarray(yn, float)
    ud, _lA, _f, _eps, _lp = BDH.dual_weights(xu, uabs, S, L)
    ad, bd, h0d = V.mu_chain(xu, ud, Nw)
    Bd = o["Bd"]
    U = o["U"]
    A0 = o["A0"]
    id12 = ident12_from_q(o["q11"], o["q22"], o["q12"], o["detK"])
    id13 = ident13_cd(Bd, yn, bd, Nw)
    ws = wedge_share(U[:, 0], U[:, 1], A0)
    gs = overload_majorant(A0)
    g = FTRI.grade_of(Nw)
    # ∧² inertia from the SAME Rayleigh-arbitrated (npos, nneg,
    # nzer) as r367 P1 -- a second raw 1e-8 floor disagrees on
    # deep near-zeros (a1, first evaluation 35/45).  Product
    # formula: nneg(∧²) = nneg * npos.
    nneg2 = int(o["nneg"] * o["npos"])
    npos2 = int(o["npos"] * (o["npos"] - 1) // 2
                + o["nneg"] * (o["nneg"] - 1) // 2)
    out = dict(ok_sup=o["ok_sup"], ok_map=o["ok_map"], Sm=o["Sm"],
               Nw=Nw, nneg=o["nneg"], npos=o["npos"], nzer=o["nzer"],
               detK=o["detK"], P1=o["P1"], P2=o["P2"], Mpd=o["Mpd"],
               hayn=o["hayn"], eps=o["eps"], lminA=o["lminA"],
               q11=o["q11"], q22=o["q22"], q12=o["q12"],
               wterm=id12["wterm"], cap=id12["capture"],
               id12_err=id12["err"], cN=id13["cN"],
               id13_err=id13["err"], id13_rel=id13["rel"],
               bN=id13["bN"], share=ws["share"], n2=ws["n2"],
               nneg2=nneg2, npos2=npos2,
               n_hit=gs["n_hit"], n_diagneg=gs["n_diagneg"],
               mind=gs["mind"], iso=gs["iso"],
               cert_lt2=gs["cert_lt2"], maj=gs["maj"],
               grade=g, sign_neg=bool(id12["wterm"] < 0.0),
               maj_share=bool(ws["share"] >= 0.5)
               if math.isfinite(ws["share"]) else False)
    if keep:
        out.update(U=U, A0=A0, Bd=Bd, bd=bd, yn=yn)
    return out


def chi_compound_row(kz, q, lpq):
    """one chi-world rung through the identical compound
    pipeline; consumes the chi comb + matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    o = compound_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                      mzc["Nw"], mzc["S"], mzc["L"], j1, j2)
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    o["S"] = mzc["S"]
    return o


def fr_ident12_from_toy():
    """identity (12) over Q on the r367 4-node Haynsworth toy.
    Consumes nothing (closed toy)."""
    T = FTRI.haynsworth_toy()
    q11 = T["K2"][0][0] - Fr(1)
    q22 = T["K2"][1][1] - Fr(1)
    q12 = T["K2"][0][1]
    wterm = q11 * q22 - q12 * q12
    det_id = Fr(1) + q11 + q22 + wterm
    # ∧² inertia from the diagonal of A0
    ev = [T["A0"][i][i] for i in range(4)]
    nneg2 = npos2 = nzer2 = 0
    for i in range(4):
        for j in range(i + 1, 4):
            p = ev[i] * ev[j]
            if p > 0:
                npos2 += 1
            elif p < 0:
                nneg2 += 1
            else:
                nzer2 += 1
    # wrong convention λ_i + λ_j
    nneg_sum = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if ev[i] + ev[j] < 0:
                nneg_sum += 1
    return dict(q11=q11, q22=q22, q12=q12, wterm=wterm,
                det_id=det_id, detK=T["detK"],
                npos2=npos2, nneg2=nneg2, nzer2=nzer2,
                nneg_sum=nneg_sum, iA=T["iA"])


def fr_cd_telescope():
    """Christoffel-Darboux over Q: p0=1, a=(0,1), b=(1,1),
    p1=x, p2=x²-x-1.  At (0,2) both K_0 and K_1 match the CD
    ratio, and the undressed wedge equals K_n (y-x)/b_n.
    Consumes nothing (closed toy)."""
    def p0(x):
        return Fr(1)

    def p1(x):
        return Fr(x)

    def p2(x):
        return Fr(x) * Fr(x) - Fr(x) - Fr(1)

    b0, b1 = Fr(1), Fr(1)
    x, y = Fr(0), Fr(2)
    K0 = p0(x) * p0(y)
    cd0 = b0 * (p1(x) * p0(y) - p0(x) * p1(y)) / (x - y)
    K1 = K0 + p1(x) * p1(y)
    cd1 = b1 * (p2(x) * p1(y) - p1(x) * p2(y)) / (x - y)
    w0 = p0(x) * p1(y) - p1(x) * p0(y)
    rhs0 = K0 * (y - x) / b0
    w1 = p1(x) * p2(y) - p2(x) * p1(y)
    rhs1 = K1 * (y - x) / b1
    return dict(K0=K0, cd0=cd0, K1=K1, cd1=cd1,
                w0=w0, rhs0=rhs0, w1=w1, rhs1=rhs1)


# ============== must-fail mutants
def mutant_wedge_readback(detK_col_true):
    """m1 MUST-FAIL (AST): a 'wedge term' that returns det K2 - 1
    from the withheld determinant column -- AST-FLAGGED."""
    return float(detK_col_true) - 1.0


def mutant_wrong_and2_convention(ev):
    """m2 MUST-FAIL (loud): ∧² eigenvalues taken as λ_i + λ_j
    instead of λ_i λ_j -- the inertia of the Haynsworth toy
    must disagree with the product convention."""
    ev = list(ev)
    nneg_sum = 0
    nneg_prod = 0
    for i in range(len(ev)):
        for j in range(i + 1, len(ev)):
            if ev[i] + ev[j] < 0:
                nneg_sum += 1
            if ev[i] * ev[j] < 0:
                nneg_prod += 1
    return nneg_sum, nneg_prod


def mutant_bar_after_sight(share_col_true):
    """m3 MUST-FAIL (AST / protocol): a bar read from the
    evaluated share column after sight -- AST-FLAGGED."""
    s = np.asarray(share_col_true, float)
    s = s[np.isfinite(s)]
    return float(np.min(s)) * 0.9 if len(s) else 0.0


def mutant_contour_from_eigs(nneg_col_true):
    """m4 MUST-FAIL (AST): a 'majorant' that returns the
    eigenvalue count of A0 -- AST-FLAGGED."""
    return int(nneg_col_true)


def mutant_cn_sign(Bd, yn, bd, Nw):
    """m5 MUST-FAIL (loud): c_N flipped.  The (13) residual
    must be loud against the true positive c_N."""
    u = Bd[:, Nw - 3]
    v = Bd[:, Nw - 2]
    cn = 1.0 / float(bd[Nw - 3])
    Rnm2 = Bd[:, :Nw - 2] @ Bd[:, :Nw - 2].T
    Wedge = np.outer(u, v) - np.outer(v, u)
    dy = yn[np.newaxis, :] - yn[:, np.newaxis]
    pred_w = (-cn) * dy * Rnm2
    err_w = float(np.max(np.abs(Wedge - pred_w)))
    err_t = float(np.max(np.abs(Wedge - cn * dy * Rnm2)))
    return err_w, err_t


def slim(o):
    drop = {"U", "A0", "Bd", "bd", "yn"}
    return {k: o[k] for k in o if k not in drop}


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("compound_cd_wedge_probe -- "
          "PRIME.LSTAR.DUAL.COMPOUND_CD.01 (round 371)")
    print("SPEC_SHA %s   (r367 FTRI %s / r363 CSI %s / r356 BDH %s)"
          % (SPEC_SHA[:16], FTRI.SPEC_SHA[:16], CSI.SPEC_SHA[:16],
             BDH.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 blocks; ladder, EXT, twin, chi, "
                        "scramble skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (FTRI.SPEC_SHA.startswith(FTRI_SHA_PREFIX)
              and CSI.SPEC_SHA.startswith(CSI_SHA_PREFIX)
              and SWD.SPEC_SHA.startswith(SWD_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and LM.SPEC_SHA.startswith(LM_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r367/r363/r359/r356/r362/"
          "r342/r357/r354/r329/r286 machinery imported verbatim "
          "(FTRI %s == %s*, CSI %s == %s*); bars SHARE_BAR=%.2f, "
          "ID_LIVE=%.0e, MAJ = Gershgorin n_hit, isolation "
          "cert_lt2, ONE run no nachbessern; DCCX STOP list "
          "forbids any L* claim"
          % (FTRI.SPEC_SHA[:8], FTRI_SHA_PREFIX,
             CSI.SPEC_SHA[:8], CSI_SHA_PREFIX, SHARE_BAR, ID_LIVE))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m1 = scope_audit("mutant_wedge_readback")
    hits_m3 = scope_audit("mutant_bar_after_sight")
    hits_m4 = scope_audit("mutant_contour_from_eigs")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m1) and bool(hits_m3) and bool(hits_m4),
          "the %d module-own constructors consume measure arrays "
          "/ chain / positions / pair ONLY (%s); fragment audit "
          "%s; m1/m3/m4 FLAGGED (%s, %s, %s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m1[0] if hits_m1 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- (12) FRACTIONS + (13) CD + ∧² CONVENTION")
    T12 = fr_ident12_from_toy()
    ok12 = (T12["det_id"] == T12["detK"] == Fr(-7)
            and T12["wterm"] == Fr(-4)
            and T12["iA"] == (3, 1, 0)
            and T12["nneg2"] == 3 and T12["npos2"] == 3
            and T12["nzer2"] == 0)
    check("G10-toy-ident12", ok12,
          "EXACT FRACTIONS IDENTITY (12) on the 4-node toy: "
          "q11=%s q22=%s q12=%s wterm=%s, det K2 = %s == 1+q11+"
          "q22+wterm; ∧² inertia from λ_i λ_j = (%d pos, %d neg, "
          "%d zer) == (C(3,2), 3, 0) -- the compound of inertia "
          "(3,1,0)"
          % (str(T12["q11"]), str(T12["q22"]), str(T12["q12"]),
             str(T12["wterm"]), str(T12["detK"]),
             T12["npos2"], T12["nneg2"], T12["nzer2"]))
    Tcd = fr_cd_telescope()
    ok13 = (Tcd["K0"] == Tcd["cd0"] == Fr(1)
            and Tcd["K1"] == Tcd["cd1"]
            and Tcd["w0"] == Tcd["rhs0"]
            and Tcd["w1"] == Tcd["rhs1"])
    check("G11-toy-ident13", ok13,
          "EXACT FRACTIONS CD-TELESCOPE (13 undressed): K0=cd0="
          "%s, K1=cd1=%s; wedge p_n p_{n+1} - p_{n+1} p_n = "
          "K_n (y-x)/b_n at n=0 (%s) and n=1 (%s) -- SATZ over "
          "Q; the √υ dressing is bilinear and live-gated"
          % (str(Tcd["K0"]), str(Tcd["K1"]),
             str(Tcd["w0"] == Tcd["rhs0"]),
             str(Tcd["w1"] == Tcd["rhs1"])))
    check("G12-toy-wrong-and2", T12["nneg_sum"] != T12["nneg2"],
          "WRONG ∧² CONVENTION λ_i+λ_j CAUGHT EXACTLY: nneg_sum="
          "%d != nneg_prod=%d on the toy (sums of (-1,1,2,3) "
          "are nonnegative; products give 3 negatives) -- the "
          "product convention is load-bearing"
          % (T12["nneg_sum"], T12["nneg2"]))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + IDENTITIES + WEDGE + MAJORANT")
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
    o9 = compound_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                       R9["Nw"], R9["S"], mz9["L"], R9["i1"],
                       R9["i2"], keep=True)
    A9 = W9_K2_ANCH
    W9 = W9_WEDGE_ANCH
    ok_k2 = (abs(o9["detK"] / A9["detK"] - 1.0) <= K2_REL
             and o9["nneg"] == A9["nneg"] and o9["P1"] and o9["P2"])
    ok_id = (o9["id12_err"] <= ID_LIVE and o9["id13_err"] <= ID_LIVE
             and o9["cN"] > CN_MIN)
    ok_w = (abs(o9["wterm"] / W9["wterm"] - 1.0) <= WTERM_REL
            and abs(o9["share"] - W9["share"]) <= SHARE_ANCH_TOL
            and abs(o9["cN"] - W9["cN"]) <= CN_ANCH_TOL
            and o9["nneg2"] == W9["nneg2"]
            and o9["n_diagneg"] == W9["n_diagneg"]
            and abs(o9["mind"] / W9["mind"] - 1.0) <= MIND_REL)
    check("G21-w9-identities", ok_k2 and ok_id,
          "W9 IDENTITIES: detK=%.4f nneg=%d (r367 pilot); (12) "
          "err %.1e (bar %.0e); (13) err %.1e c_N=%.4f > %.2f "
          "(positive Jacobi coupling) -- both identities live"
          % (o9["detK"], o9["nneg"], o9["id12_err"], ID_LIVE,
             o9["id13_err"], o9["cN"], CN_MIN))
    check("G22-w9-wedge", ok_w and o9["sign_neg"] and o9["cap"]
          and o9["nneg2"] == o9["Sm"] - 1,
          "W9 WEDGE SIGNATURE: wterm=%.4f < 0 (anchor %.4f); "
          "share=%.4f (anchor %.4f, majority bar %.2f); capture "
          "%s ≡ P2; ∧² nneg=%d == |Y|-1=%d EXACT; n_diagneg=%d "
          "min diag(A0)=%+.4e > 0 -- the negative of A0 is "
          "OFF-DIAGONAL, the occupation diagonal stays positive"
          % (o9["wterm"], W9["wterm"], o9["share"], W9["share"],
             SHARE_BAR, o9["cap"], o9["nneg2"], o9["Sm"] - 1,
             o9["n_diagneg"], o9["mind"]))
    check("G23-w9-majorant", (not o9["cert_lt2"])
          and o9["maj"] >= MAJ_SCR_MIN and (not o9["iso"]),
          "W9 OVERLOAD CONSTRUCTION (sealed, pre-typed): MAJ="
          "n_hit=%d ≫ 2, isolation %s, cert_lt2 %s -- the "
          "Gershgorin-Stieltjes majorant does NOT certify "
          "ind_- < 2 at w9 (disclosed at freeze); n_diagneg=%d "
          "is a distinguisher vs scramble, not a majorant of "
          "nneg (nneg=1 > n_diagneg)"
          % (o9["maj"], o9["iso"], o9["cert_lt2"],
             o9["n_diagneg"]))
    o9s = slim(o9)

    # ---------------- S3 ladder
    section("S3  LEG A/B/C -- THE 85-ROW LADDER -- IDENTITIES + "
            "WEDGE CENSUS + MAJORANT")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-ident-census",
                  "G34-wedge-sign-census", "G35-share-and2-census",
                  "G36-capture-census", "G37-overload-census"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: o9s}
        MT = {MAIN_KZ: dict(margin=R9["margin"], Nw=R9["Nw"],
                            z=R9["z"], Sm=R9["Sm"], S=R9["S"])}
        n_resolv = 1
        nneg1_n = 1
        vac_n = 0
        ovl_n = 0
        sign_ok_n = 1
        share_ok_n = 1
        cap_ok_n = 1
        id12_ok_n = 1
        id13_ok_n = 1
        cert_n = 0
        id12_max = o9s["id12_err"]
        id13_max = o9s["id13_err"]
        share_min = o9s["share"]
        wterm_max = o9s["wterm"]
        flip_n = 0
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
              "SEALED SELECTIONS executed verbatim (r356/r367 "
              "rules AS-IS): EXT5 used %d == %d, fresh %d == %d, "
              "queue %s; EXT6 used %d == %d, fresh %d == %d, "
              "queue %s"
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
        print("    %-5s %-5s %-5s | %-9s %-8s %-6s | %-8s %-8s | "
              "%-5s %-5s %-4s"
              % ("kz", "N_w", "S_-", "detK", "wterm", "share",
                 "id12", "id13", "nneg", "hit", "dneg"),
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
                o = compound_rung(mz["xu"], mz["wu"], mz["yn"],
                                  mz["vn"], Rr["Nw"], Rr["S"],
                                  mz["L"], Rr["i1"], Rr["i2"])
            if Rr["margin"] <= 0:
                neg_rows.append(kz)
            if not (o["ok_sup"] and o["ok_map"]):
                sup_fail.append(kz)
            print("    %-5d %-5d %-5d | %+.2e %+.2e %6.3f | "
                  "%8.1e %8.1e | %5d %5d %4d"
                  % (kz, Rr["Nw"], Rr["Sm"], o["detK"], o["wterm"],
                     o["share"], o["id12_err"], o["id13_err"],
                     o["nneg"], o["n_hit"], o["n_diagneg"]),
                  flush=True)
            OT[kz] = o
            MT[kz] = dict(margin=Rr["margin"], Nw=Rr["Nw"],
                          z=Rr.get("z", kz), Sm=Rr["Sm"], S=Rr["S"])
            if kz != MAIN_KZ:
                del Rr, mz, o
        all_kz = list(OT)
        resolv = [k for k in all_kz
                  if abs(OT[k]["eps"]) > RESOLV_FLOOR]
        n_resolv = len(resolv)
        check("G31-ladder-census", n_resolv >= 40 and len(OT) >= 80,
              "LADDER built %d windows, resolvable (|eps|>%.0e) "
              "%d; RANK_KZ identities on the four Sol rungs "
              "follow in G33"
              % (len(OT), RESOLV_FLOOR, n_resolv))
        check("G32-support-gate-all", not sup_fail and not neg_rows,
              "SUPPORT GATE all MAIN windows: support/map %s, "
              "margin>0 %s (neg rows %s)"
              % ("PASS" if not sup_fail else str(sup_fail),
                 "PASS" if not neg_rows else "FAIL",
                 str(neg_rows) if neg_rows else "none"))
        # identities live
        id12_ok = [k for k in resolv
                   if OT[k]["id12_err"] <= ID_BAR[OT[k]["grade"]]]
        id13_ok = [k for k in resolv
                   if OT[k]["id13_err"] <= ID_BAR[OT[k]["grade"]]
                   and OT[k]["cN"] > CN_MIN]
        id12_live = [k for k in resolv if OT[k]["id12_err"] <= ID_LIVE]
        id13_live = [k for k in resolv if OT[k]["id13_err"] <= ID_LIVE]
        id12_max = max(OT[k]["id12_err"] for k in resolv)
        id13_max = max(OT[k]["id13_err"] for k in resolv)
        id12_ok_n = len(id12_ok)
        id13_ok_n = len(id13_ok)
        rk_ok = True
        for kz, anc in SAMPLE_K2.items():
            if kz not in OT:
                rk_ok = False
                continue
            rk_ok = rk_ok and (
                abs(OT[kz]["detK"] / anc["detK"] - 1.0) <= K2_REL
                and abs(OT[kz]["wterm"] / anc["wterm"] - 1.0)
                <= WTERM_REL
                and abs(OT[kz]["share"] - anc["share"])
                <= SHARE_ANCH_TOL)
        check("G33-ident-census",
              len(id12_ok) == n_resolv and len(id13_ok) == n_resolv
              and rk_ok,
              "IDENTITIES CENSUS (KILL at graded floor, LIVE "
              "1e-10 reported): (12) graded %d/%d maxerr %.1e; "
              "(12) live 1e-10 %d/%d; (13) graded %d/%d maxerr "
              "%.1e c_N>%.2f; (13) live 1e-10 %d/%d; RANK_KZ "
              "wterm/share anchors %s -- (12)(13) are SATZ live"
              % (len(id12_ok), n_resolv, id12_max,
                 len(id12_live), n_resolv,
                 len(id13_ok), n_resolv, id13_max, CN_MIN,
                 len(id13_live), n_resolv,
                 "PASS" if rk_ok else "FAIL"))
        # nneg-1 branch = r367 P1
        nneg1 = [k for k in resolv if OT[k]["P1"]]
        vac = [k for k in resolv
               if OT[k]["nneg"] == 0 and OT[k]["nzer"] == 0]
        ovl = [k for k in resolv if OT[k]["nneg"] >= 2]
        nneg1_n = len(nneg1)
        vac_n = len(vac)
        ovl_n = len(ovl)
        sign_ok = [k for k in nneg1 if OT[k]["sign_neg"]]
        sign_ok_n = len(sign_ok)
        flip_n = nneg1_n - sign_ok_n
        wterm_nneg1 = [OT[k]["wterm"] for k in nneg1]
        wterm_max = max(wterm_nneg1) if wterm_nneg1 else float("nan")
        wterm_min = min(wterm_nneg1) if wterm_nneg1 else float("nan")
        check("G34-wedge-sign-census", True,
              "WEDGE-SIGN CENSUS on the nneg-1 branch (r367 P1 "
              "reproduced %d/%d, vacuous %d, overload %d): "
              "wterm<0 %d/%d (flips %d); wterm on branch "
              "[%+.3f, %+.3f] -- 0-violation is the GO letter "
              "COMPOUND_SIGNATURE_STABLE, not this gate"
              % (nneg1_n, n_resolv, vac_n, ovl_n,
                 sign_ok_n, nneg1_n, flip_n, wterm_min, wterm_max))
        share_ok = [k for k in nneg1
                    if math.isfinite(OT[k]["share"])
                    and OT[k]["share"] >= SHARE_BAR]
        share_ok_n = len(share_ok)
        and2_ok = [k for k in nneg1
                   if OT[k]["nneg2"] == OT[k]["Sm"] - 1]
        shares = [OT[k]["share"] for k in nneg1
                  if math.isfinite(OT[k]["share"])]
        share_min = min(shares) if shares else float("nan")
        share_med = float(np.median(shares)) if shares else float("nan")
        share_max = max(shares) if shares else float("nan")
        check("G35-share-and2-census",
              len(and2_ok) == nneg1_n
              and nneg1_n == P1_BRANCH_N
              and vac_n == VACUOUS_N and ovl_n == 0
              and n_resolv == RESOLV_N,
              "∧²-SUBSPACE CENSUS: r367 dichotomy reproduced "
              "P1=%d/%d vacuous=%d overload=%d (ward %d/%d/%d); "
              "nneg(∧² A0)=|Y|-1 on %d/%d of the branch (SATZ "
              "inertia of ∧² of (p,1,0)); share min/med/max "
              "%.3f/%.3f/%.3f, majority (>=%.2f) %d/%d -- "
              "dominant-0.90 is NOT claimed (Sol 0.67..0.78)"
              % (nneg1_n, n_resolv, vac_n, ovl_n,
                 P1_BRANCH_N, VACUOUS_N, RESOLV_N,
                 len(and2_ok), nneg1_n,
                 share_min, share_med, share_max, SHARE_BAR,
                 share_ok_n, nneg1_n))
        cap_ok = [k for k in nneg1 if OT[k]["cap"] == OT[k]["P2"]]
        cap_true = [k for k in nneg1 if OT[k]["cap"]]
        # identity: capture iff P2, and P2 holds on the P1 branch
        # (r367: P1 and P2 fail together)
        cap_ok_n = len(cap_true)
        id_cap = all(OT[k]["cap"] == (OT[k]["detK"] < 0.0)
                     for k in resolv)
        check("G36-capture-census", id_cap,
              "CAPTURE (14) CENSUS: capture ≡ det K2 < 0 via "
              "(12) on %s resolvable (identity ward); on the "
              "nneg-1 branch capture holds %d/%d (the r367 P2 "
              "set -- not independent arithmetic).  CAPTURE_"
              "HOLDS_CENSUS is the letter, not a new SATZ"
              % ("ALL" if id_cap else "NOT-ALL",
                 cap_ok_n, nneg1_n))
        cert_n = sum(1 for k in nneg1 if OT[k]["cert_lt2"])
        maj_min = min(OT[k]["maj"] for k in nneg1) if nneg1 else 0
        maj_max = max(OT[k]["maj"] for k in nneg1) if nneg1 else 0
        dneg_max = max(OT[k]["n_diagneg"] for k in nneg1) \
            if nneg1 else 0
        check("G37-overload-census", True,
              "OVERLOAD MAJORANT CENSUS (sealed Gershgorin-"
              "Stieltjes): cert_lt2 %d/%d of nneg-1 (isolation "
              "+ n_hit<2); MAJ=n_hit on branch [%d, %d]; "
              "n_diagneg max %d (occupation diagonal of A0).  "
              "OVERLOAD_MAJORANT_GO requires 0-miss cert_lt2 "
              "AND scramble MAJ>2; else OVERLOAD_CENSUS_ONLY "
              "(r367 overload 0/%d reproduced: ovl=%d)"
              % (cert_n, nneg1_n, maj_min, maj_max, dneg_max,
                 n_resolv, ovl_n))

    # ---------------- S4 worlds
    section("S4  WORLDS -- TWIN + CHI + SCRAMBLE")
    if smoke:
        for g in ("G40-twin", "G41-chi3-ladder", "G42-chi4-ladder",
                  "G43-scramble-break"):
            check(g, True, "SMOKE: skipped")
        chi_p = {"chi3": None, "chi4": None}
        scr_named = True
        scr_maj = True
        scr_wterm = SCR_ANCH["wterm"]
        scr_hit = SCR_ANCH["n_hit"]
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
            oT = compound_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                               mzT["vn"], mzT["Nw"], mzT["S"],
                               mzT["L"], t1_, t2_)
            oM = OT[kz]
            nneg_dev = max(nneg_dev, abs(oT["nneg"] - oM["nneg"]))
            tw_dev = max(tw_dev, abs(oT["wterm"] - oM["wterm"]))
            del oT
        check("G40-twin", ok_dose0 and tw_dev <= TWIN_BAR
              and nneg_dev == 0,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "BITWISE %s): max |d wterm| = %.1e (bar %.0e), "
              "|dnneg| = %d -- the wedge term is twin-stable"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_BAR,
                 nneg_dev))
        chi_p = {}
        for (q, lpq, tag, eanch) in (
                (DMF.Q_CHI3, DMF.LPQ3, "chi3", CHI3_W9_ANCH),
                (DMF.Q_CHI4, DMF.LPQ4, "chi4", CHI4_W9_ANCH)):
            rows, excl = [], []
            for kz in V.admissible_indices():
                o = chi_compound_row(kz, q, lpq)
                if o is None:
                    excl.append(kz)
                    continue
                rows.append(o)
            sup_ok = all(r["ok_sup"] and r["ok_map"] for r in rows)
            nneg1_c = [r["kz"] for r in rows if r["P1"]]
            sign_c = [r["kz"] for r in rows
                      if r["P1"] and r["sign_neg"]]
            dead = [r["kz"] for r in rows if r["eps"] <= 0.0]
            w9r = next(r for r in rows if r["kz"] == MAIN_KZ)
            anch_ok = (w9r["nneg"] == eanch["nneg"]
                       and abs(w9r["detK"] / eanch["detK"] - 1.0)
                       <= 2e-2
                       and abs(w9r["wterm"] / eanch["wterm"] - 1.0)
                       <= 2e-2
                       and abs(w9r["share"] - eanch["share"])
                       <= SHARE_ANCH_TOL)
            ok_world = (len(rows) >= N_CHI_MIN and sup_ok
                        and anch_ok)
            chi_p[tag] = dict(n=len(rows), p1=len(nneg1_c),
                              sign=len(sign_c), dead=len(dead),
                              w9_nneg=w9r["nneg"],
                              w9_wterm=w9r["wterm"],
                              w9_share=w9r["share"],
                              w9_eps=w9r["eps"])
            check("G41-chi3-ladder" if tag == "chi3"
                  else "G42-chi4-ladder", ok_world,
                  "%s NEGATIVE CONTROL (terminal-dead sprouts "
                  "INCLUDED, eps<=0 on %d/%d): %d/42 built "
                  "(exclusions %s), support %s; nneg-1 %d/%d "
                  "with wterm<0 %d/%d; w9 nneg=%d wterm=%+.3f "
                  "share=%.3f -- MAY tip; chi3-w9 scoped PD "
                  "(wterm>0, share=0) is world-separating"
                  % (tag.upper(), len(dead), len(rows),
                     len(rows), str(excl) if excl else "none",
                     "PASS" if sup_ok else "FAIL",
                     len(nneg1_c), len(rows),
                     len(sign_c), max(len(nneg1_c), 1),
                     w9r["nneg"], w9r["wterm"], w9r["share"]))
        alpha9v = float(V.U[MAIN_KZ])
        uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
        rng = np.random.default_rng(SCR_SEED)
        u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v,
                                    size=len(ww3)))
        mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0,
                                     DMF.LPQ3)
        s1_, s2_ = PX.pair_select(mzs["yn"])
        oS = compound_rung(mzs["xu"], mzs["wu"], mzs["yn"],
                           mzs["vn"], mzs["Nw"], mzs["S"],
                           mzs["L"], s1_, s2_)
        scr_named = (oS["nneg"] == SCR_ANCH["nneg"] and not oS["P1"])
        scr_maj = oS["maj"] >= MAJ_SCR_MIN
        scr_wterm = oS["wterm"]
        scr_hit = oS["n_hit"]
        alg_ok = (abs(oS["detK"] / SCR_ANCH["detK"] - 1.0) <= 5e-2
                  and oS["n_diagneg"] == SCR_ANCH["n_diagneg"]
                  and abs(oS["wterm"] / SCR_ANCH["wterm"] - 1.0)
                  <= 5e-2)
        check("G43-scramble-break", scr_named and scr_maj and alg_ok
              and oS["P2"] and (not oS["cert_lt2"]),
              "THE MATCHED SCRAMBLE BREAKS NAMED AT P1: A0 nneg="
              "%d == %d; MAJ=n_hit=%d >= %d (vacuity test: the "
              "majorant IS > 2 here, construction not empty); "
              "n_diagneg=%d; wterm=%.3f (measured, P2 survives "
              "detK=%.3f); cert_lt2 %s.  The wedge term on an "
              "overload world is NOT the MAIN source signature"
              % (oS["nneg"], SCR_ANCH["nneg"], oS["maj"],
                 MAJ_SCR_MIN, oS["n_diagneg"], oS["wterm"],
                 oS["detK"], oS["cert_lt2"]))
        del oS

    # ---------------- S5 must-fails
    section("S5  MUST-FAILS")
    check("G80-m1-wedge-readback", bool(hits_m1),
          "m1 WEDGE FROM det K2 READBACK: AST-FLAGGED (%s) -- "
          "the wedge term is q11 q22 - q12^2 from the two CD "
          "columns and A0^{-1}, never det K2 - 1 (that drops "
          "the linear terms of identity (12))"
          % (hits_m1[0] if hits_m1 else "MISS"))
    check("G81-m2-wrong-and2", True,
          "m2 WRONG ∧² CONVENTION λ_i+λ_j: CAUGHT EXACTLY at "
          "G12 (nneg_sum != nneg_prod over Q)")
    check("G82-m3-bar-after-sight", bool(hits_m3),
          "m3 BARS AFTER SIGHT: AST-FLAGGED (%s) -- SHARE_BAR "
          "and MAJ construction were sealed in the spec BEFORE "
          "the freeze; EIN RUN, no nachbessern"
          % (hits_m3[0] if hits_m3 else "MISS"))
    check("G83-m4-contour-from-eigs", bool(hits_m4),
          "m4 CONTOUR MAJORANT FROM EIGENVALUES: AST-FLAGGED "
          "(%s) -- MAJ is the Gershgorin n_hit of A0, never "
          "nneg(A0) itself"
          % (hits_m4[0] if hits_m4 else "MISS"))
    e_w, e_t = mutant_cn_sign(o9["Bd"], o9["yn"], o9["bd"], R9["Nw"])
    ratio = e_w / max(e_t, 1.0e-18)
    check("G84-m5-cn-sign", ratio >= M5_RATIO and e_t <= ID_LIVE,
          "m5 c_N SIGN FLIPPED: the (13) residual jumps to "
          "%.3e (true %.1e, ratio %.1e >= %.0e) -- CAUGHT EXACT; "
          "the Jacobi coupling b_{N-3} is positive, c_N = 1/b "
          "cannot flip"
          % (e_w, e_t, ratio, M5_RATIO))
    for k in ("U", "A0", "Bd", "bd", "yn"):
        o9.pop(k, None)

    # ---------------- S6 verdict
    section("S6  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, no bound "
          "mechanism, no certificate reading beyond the sealed "
          "census, no posthoc bar/band/clause move, no derived "
          "5/7, NO RH claim, mincut unchanged; r243..r367 stand; "
          "R369/R372/R373 coexistence (own files)")
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
        elif not st.get("G10-toy-ident12", False) \
                or not st.get("G11-toy-ident13", False) \
                or not st.get("G33-ident-census", False) \
                or not st.get("G36-capture-census", False):
            verd = "CHAIN_FAIL"
        else:
            parts = []
            sig_stable = (flip_n == 0 and share_ok_n == nneg1_n
                          and scr_named)
            if flip_n > 0:
                parts.append("WEDGE_COIN_FLIP(sign mixed %d/%d "
                             "on nneg-1)"
                             % (flip_n, nneg1_n))
            elif sig_stable:
                parts.append("COMPOUND_SIGNATURE_STABLE")
            else:
                parts.append("SIGNATURE_PARTIAL(wterm<0 %d/%d, "
                             "share>=%.2f %d/%d)"
                             % (sign_ok_n, nneg1_n, SHARE_BAR,
                                share_ok_n, nneg1_n))
            parts.append("CAPTURE_HOLDS_CENSUS(nneg-1 %d/%d via "
                         "(12) ≡ P2)"
                         % (cap_ok_n, nneg1_n))
            if cert_n == nneg1_n and scr_maj:
                parts.append("OVERLOAD_MAJORANT_GO")
            else:
                parts.append("OVERLOAD_CENSUS_ONLY(cert_lt2 "
                             "%d/%d, scramble MAJ>2 %s)"
                             % (cert_n, nneg1_n, scr_maj))
            parts.append("AND2_LEDGER(nneg(∧²A0)=|Y|-1 on the "
                         "branch, share min %.3f)"
                         % share_min)
            parts.append("WORLD_LEDGER(chi3 %s, chi4 %s -- chi "
                         "MAY tip, terminal-dead included)"
                         % (str(chi_p.get("chi3")),
                            str(chi_p.get("chi4"))))
            parts.append("TWIN_LEDGER")
            parts.append("SCRAMBLE_BREAK(named P1 nneg=21, "
                         "MAJ=%d>2, wterm=%.3f measured)"
                         % (scr_hit, scr_wterm))
            parts.append("MUSTFAIL_LEDGER")
            verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- identities SATZ + wedge census + overload "
          "construction; NO L* claim, NO RH claim"
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
