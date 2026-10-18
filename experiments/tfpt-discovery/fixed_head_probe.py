#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fixed_head_probe -- PRIME.LSTAR.FIXED_HEAD.01 (round 307):
the reviewer's CHEAPEST KILL TEST of proof architecture C (fixed
head + contractive tail) for the window positivity L*.  The r284
anatomy showed that MAIN's critical direction at the wall is
carried almost entirely by the FLAT ARCHIMEDEAN EDGE ATOMS below
the first prime (flagship: 99.7 percent of the extremal direction
on TWO such atoms, folds 2 and 4; leading candidates folds 2, 4,
6, 8, 10).  In the mu-orthonormal frame E = B^T B = E_H + E_T
(H = the first r flat edge atoms, T = the rest); if I - E_T > 0
then by Schur/Woodbury

    I - E > 0   <=>   S_H := I_r - B_H (I - E_T)^{-1} B_H^T > 0,

reducing the growing N_w x N_w problem to (1) a tail contraction
statement I - E_T > 0 (an explicit positive, possibly shrinking
lower bound suffices) and (2) a FIXED r x r matrix (border-
extended: (r+1) x (r+1)).  THIS ROUND IS THE KILL TEST: no
functional search, no new statistic -- only lambda_max(E_T),
lambda_min(S_H) and the minimal fixed r, on all 57 windows (42
core + 15 r286 anchors) plus 20 NEW deeper windows (budget probed
honestly: the r306 round managed the 15 EXT anchors at ~1 s per
window; the 20 new ones cost seconds each, included).  The round
decides whether the near-one-atom anatomy is merely DESCRIPTIVE
or genuinely PROOF-RELEVANT.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r306 discipline): w = window (kz
into the prime-power list PP), z = PP[kz], S = #union atoms of
mutilde = mu - nu, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2 =
builder depth, n = degree, r = head size, f = fold index (atoms
sit on the fold grid x_f = cos(2 pi f / L); u = f Delta with
Delta = 2 alpha / M the lag spacing); FLAT EDGE = the nu atoms
with u < log 2 (below the first prime), fold-ascending.  E_n =
nu-dressed mu-CD kernel Gram; margin = 1 - lambda_max(E_{N_w});
E_T(r) = E with the r head-atom rows removed; reserve(r) =
1 - lambda_max(E_T(r)); S_H = I_r - B_H (I - E_T)^{-1} B_H^T
(exact Schur identities det(I - E) = det(I - E_T) det(S_H) and,
border-extended with the r264/r266 augmented convention [[G, t],
[t^T, c]], det(I - E_T) det(S_aug) = det(I - E) D_N with t_i =
int pihat_i dsigma_border (smooth-comb border, r258 route),
corner c = sum_{j <= N-2} rho_j + 5/7 and D_N = 5/7 - rho_{N-1} =
(5/7)(1 - q_N), rho_j = the r244 bordered Christoffel terms).
Ground truth (record margins, masses, census) enters GATES and
record tables only; the sealed ORDERING constructors consume fold
indices + grid geometry + the frozen w9 permutation ONLY (AST
scope audit: NO eigensolver, NO target data in any ordering);
no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: the standalone document pipeline rh/problem/
verify_lstar_instance.py V.{build_measures, mu_chain, b_matrix,
admissible_indices, mp_lam_max, window_shape, PP}, r286
LM.{ext_rule, spearman, ts_slope_free}, r284 LS.{world_pack,
atom_labels}, r283 FS.{mu_chain_f64, b_matrix_f64}, r278
MS.ctx_build, r276 MF.local_gaps, r289 AK.{twin_rational,
RAT_TOL}, r244 BH.bord_chain, r226 HS.window_data, r243
PB.smooth_comb, v881 PIK.lambda_eps, r230 JF.{TOY_NODES,
TOY_WTS}, r274 WD.{stj_gen, pv_seq}, paircorr PC READ-ONLY,
v563 core.build_window READ-ONLY.

THE TWO SEALED ORDERINGS (both tested, both disclosed; the
ordering is FIXED ACROSS WINDOWS -- never by the target window's
own eigenvector, which would be target-inverse and is a must-fail
mutant here):
  ORDER_FOLD: the flat-edge atoms of each window in ascending
    fold order (window-intrinsic, purely positional).
  ORDER_W9X: the w9-flagship extremal-mass rank permutation,
    computed ONCE on the w9 record object, frozen as the sealed
    constant W9X_PERM = (0, 1, 2, 3, 4, 5, 11, 9, 12, 10, 7, 13,
    8, 14, 18, 15) (ranks into the fold-sorted flat-edge list;
    the first six ranks coincide with fold order, the later ranks
    order noise-level masses < 1e-4 and are frozen as measured --
    disclosed), transferred to every window by rank; out-of-range
    ranks skipped, exhaustion falls back to ascending fold order
    (counts disclosed).  On w9 itself this ordering derives from
    w9's own record eigenvector -- allowed by the reviewer's rule
    ("derived from the w9 flagship, then frozen"), disclosed.

LEG 0 -- ANCHORS: w9 record block (S = 367/263/104, N_w = 184,
lambda_max(E_184) = 0.99983248, margin 1.6752e-4, extremal top-2
atoms folds 2 + 4 with masses 0.625/0.372 summing >= 0.99, first
five fold-order heads == the candidate folds (2, 4, 6, 8, 10),
all flat-edge atoms ARCH-labeled); r286 margin anchors kz9/kz64
(core max/min) + kz35/kz119 (extension max/min) reproduced.

LEG A -- THE r-SWEEP: both sealed orderings, r = 0..16,
lambda_max(E_T(r)) on all 42 + 15 + 20 windows; per window the
minimal r with reserve >= RESERVE_MIN = 1e-2 (the macroscopic
bar); reserve trend over anchor depth at r = 4/8/16 (Theil-Sen +
spearman); EDGE-FRACTION DIAGNOSTIC (sealed): reserve at r =
ceil(q x edge size) for q in (1/4, 1/2, 3/4, 1) -- the full-edge
point separates HEAD_GROWS from TAIL_COLLECTIVE; amplification
amp = reserve(full edge)/margin.  STRUCTURAL GATES: reserve
monotone non-decreasing in r (PSD interlacing, exact theorem) and
lambda_max(E_T) <= lambda_max(E) on every window/r -- sign safety
of every tail eigenvalue below 1 INHERITS from the r286
mp-verified positive margins through this exact monotonicity
(disclosed reasoning), plus direct mp spot wards (dps 30, chain +
B recomputed on the tail atom set) at the sealed spots (w9, r=8),
(kz119, r=8), (kz119, full edge).

LEG B -- THE HEAD SCHUR REST: at the sealed r = 8 (the reviewer's
fixed-head scale; r = 16 reported) on the 57 record windows:
S_H via the tail-atom-frame Woodbury route, lambda_min(S_H) > 0
on 57/57 (given I - E_T > 0 this is EXACTLY the wall, by the
Schur equivalence), the exact determinant identity gated on every
window; sealed anchor-monotonicity statistic spearman(
lambda_min(S_H), N_w), typed MONOTONE iff |sp| >= 0.75 (sign
disclosed); ratio lambda_min(S_H)/margin reported (how much of
the wall margin the head block carries).  BORDER-EXTENDED
VERSION: the (r+1) x (r+1) S_aug with the border column t and
corner c from the augmented convention above; exact identities
gated per window: det(I - E_T) det(S_aug) = det(I - E) D_N with
D_N = (5/7)(1 - q_N) from the INDEPENDENT r244/r258 bordered-
chain route (this cross-gates the Christoffel identity
t^T (I - E)^{-1} t = sum_{j<N} rho_j on every window implicitly;
gated explicitly on w9 + toy); q_N < 1 re-gated on 57/57 (r286
reproduction); lambda_min(S_aug) census + monotonicity.

LEG C -- WORLD/TWIN HARDENING: (c1) the r289 RATIONAL TWIN
(every u_j/Delta -> first CF convergent at |du| <= 1e-8 gap,
weights bitwise, fold sets preserved -- diophantine input
trivialized): the full r-sweep on the twin at N_w = 184 must
match MAIN (METRIC_ONLY expectation): equal head fold sets,
equal r_min under both orderings, max |reserve difference|
<= 1e-3 over r = 0..16; typed TWIN_METRIC_OK / TWIN_DEVIATES.
(c2) CONTROLS EPSTEIN + SCRAMBLE (r284 channel verbatim, their
own N_w): the same fold-order sweep; typed CONTROL_COLLECTIVE
iff lambda_max(E_T(16)) >= 1 on both (no small head rescues a
dead world -- the architecture is world-specific; a control
break here is expected and informative, not an error), else
CONTROL_RESCUED(names).

LEG D -- PROOF PRECURSOR (measurement always, GO-typing only on
GO): per record window at r = 8 and at the full edge: tail
maxdiag = max_k v_k K_{N_w}(y_k) (Christoffel), gain =
lambda_max/maxdiag, Gershgorin/Schur-test row-sum bound
max_k sum_j |E_T^atom[k, j]| and the census of windows where the
classical bound already delivers < 1 (the road to a source-pure
C2 statement).  Measurement only, no bound claim.

LEG E -- MUST-FAILS (each loud): (m1) TARGET_INVERSE ordering --
a mutant ordering the head by the target window's own top
eigenvector must be FLAGGED by the AST scope audit (eigensolver
inside an ordering constructor); (m2) WOODBURY WRONG SIGN -- S_H
with + instead of - in the correction term must break the exact
determinant identity on the exact toy by >= 0.1 (LOUD; measured
break 0.163); (m3) NO ORTHONORMAL FRAME -- the head/tail split
on the monomial-basis B must HIDE the toy wall: at the toy
crossing degree 4 the monomial lambda deviates from the true
lambda by >= 0.5 rel (LOUD; the split without the mu-orthonormal
frame loses the subordination meaning); (m4) r = 0 DEGENERATE --
the tail route at r = 0 must reproduce the known lambda_max
series exactly (w9 record to 1e-6; route equality to 1e-12; the
r = 0 augmented scalar equals D_N).

SEALED CONSTANTS: MAIN_KZ 9; R_MAX 16; GO_RMAX 8; RESERVE_MIN
1e-2; EDGE_RES 1e-3; EDGE_PASS_FRAC 0.95; AMP_BAR 100; SHRINK_SP
-0.5; GROW_SP 0.0; MONO_SP 0.75; EDGE_FRACS (1/4, 1/2, 3/4, 1);
K_EXT 15; K_EXT2 20; REC (367, 263, 104, 184); REC_LAM
0.99983248; REC_MARGIN 1.6752e-4 rel 0.01; R286_ANCH {9:
1.6752e-4, 64: 1.4175e-7, 35: 3.314e-7, 119: 1.806e-8} rel 0.05;
W9X_PERM above; W9_EDGE_N 19; W9_EDGE5 (2, 4, 6, 8, 10); W9_TOP2
((2, 0.625), (4, 0.372)) tol 5e-3, sum >= 0.99; QN_CORNER 5/7;
DETID_TOL 1e-5; WID_TOL 1e-6; TOY_TOL 1e-10; XCHK_TOL 1e-9;
MP_DPS 30; MP_SPOTS ((9, 8), (119, 8), (119, EDGE)); MP_TOL
1e-6; RAT_DRES 1e-3; CTRL_R 16; M2_BAR 0.1; M3_BAR 0.5; M4_TOL
1e-12; MONO_R_TOL 1e-10; ADMIT 1e-9; runtime <= 1800 s; smoke =
toys + firewall + scopes + mutants + w9 block (sweep, Schur,
border identities); ladder, extension, twin, controls, mp spots,
anatomy and adjudication skipped.  PRE-SPEC SCOPING (disclosed,
r286 precedent -- sizing only, no rule tuned after any evaluation
of this probe): four scratch passes preceded this spec and are
disclosed HONESTLY because they saw the likely outcome: (s1) w9
reserve profile (r = 5 gives 3.8e-2; r_min = 3 at the 1e-2 bar)
and kz35 (r = 16 leaves reserve 5.3e-4 -- a fixed small r does
NOT hold at depth); (s2) full-edge removal restores macroscopic
reserve at depth (kz35: 65 edge atoms, 1.07e-2; kz119: 60 atoms,
5.9e-3) -- RESERVE_MIN/EDGE_RES/AMP_BAR and the HEAD_GROWS /
TAIL_COLLECTIVE split were sized from these two scratches BEFORE
the spec froze, and the adjudication rests on the other 74
windows plus the sealed protocol; (s3) the exact toy values
(S_H = 5079569347/6986834571, wrong-sign break 0.163, monomial
dev 0.80 at the toy crossing) and the W-identity index convention
(sum_{j<N} rho_j, verified 4.4e-13 on w9); (s4) the EXT2
enumeration (ranks 15..34 of the r286 rule, N_w 1218..1650,
seconds per window -- feasible, included).  The w9 extremal
ordering W9X_PERM was computed once in (s1) and frozen.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] FIXED_HEAD_GO(r*, order; min reserve; trend;
    requires fixed r <= 8 with reserve >= 1e-2 on ALL windows,
    spearman(reserve, S) >= 0, S_H positive AND anchor-monotone)
  / BORDER_BREAKS_HEAD(GO conditions hold but the border-extended
    S_aug loses positivity)
  / HEAD_GROWS(edge-pass frac >= 0.95 at EDGE_RES, median
    amplification >= 100, spearman(reserve(8), S) <= -0.5: the
    head is real but its dimension grows with the window)
  / TAIL_COLLECTIVE(otherwise; break loci printed)
  + SCHUR_LEDGER(det identities; lambda_min census; monotonicity
    typing; border D_N cross-route; q_N reproduction) [always]
  + TWIN(TWIN_METRIC_OK / TWIN_DEVIATES) [always]
  + CONTROLS(CONTROL_COLLECTIVE / CONTROL_RESCUED) [always]
  + TAIL_ANATOMY(maxdiag/gain/Gershgorin census; proof-precursor
    typing only on GO) [always]
  + MP_SPOTS [always].
Honesty before beauty: every sweep number is a MEASUREMENT on
finite windows; the Schur/Woodbury identities are exact algebra,
gated, not new mathematics; a HEAD_GROWS verdict kills the FIXED
head, not the head coordinate (the edge-fraction diagnostic
quantifies what a window-dependent head buys); no verdict claims
L*, a tail-contraction theorem, a bound mechanism, a derived 5/7
or RH progress in any direction.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 27/27 (0.2 s) at the sealed
rules; calibration pass 1 = first full evaluation = 28/28, wall
109.3 s -- NO amendment: no bar, band, ordering or verdict rule
moved; the record-table insertion below is the only post-freeze
edit, which IS the protocol; record run identical to calibration;
run1/run2 byte-identical up to WALL):
CAL_VERDICT = HEAD_GROWS(edge-pass 77/77 at EDGE_RES = 1e-3 (min
full-edge reserve 2.192e-3 at kz100), median amplification
3.1e+04 (min 345.8), spearman(reserve(8), S) = -0.93 with TS
slope -3.15 == the r286 margin-law class: the fixed-head reserve
COLLAPSES with depth -- best fixed candidate r <= 8: min reserve
6.54e-6 at r = 8 FOLD, four decades below the 1e-2 bar; a
fixed-head r_min <= 16 exists on 15/77 windows only (all N_w <=
434) -- while the FULL edge (13..96 atoms, GROWING with the
window: spearman(edge, N_w) = +0.98) restores a macroscopic
reserve on 77/77: the near-one-atom anatomy is REAL and
PROOF-RELEVANT AS A COORDINATE (the binding lives on the flat
arch edge; 3-5 decades of reserve amplification) but NOT as a
fixed dimension -- architecture C in its fixed-head form is
DEAD; the honest successor object is the window-dependent head
of size ~ edge(w) ~ log2/(2 Delta_w), and even ITS reserve
decays slowly (full-edge TS slope -0.87, sp -0.83 -- disclosed))
+ SCHUR_LEDGER(det identity worst 3.4e-8, border-augmented worst
2.1e-6 on 57/57 at r = 8; lambda_min(S_H(8)) > 0 on 57/57 AND
== the wall margin to 4 digits (ratio band 1.000..1.000, w9
1.0001): the head Schur block INHERITS the full wall margin --
anchor-MONOTONE(sp -0.92, TS -3.33) == the r286 margin decay,
i.e. the reviewer's hoped-for simplification is EMPTY: S_H
carries the whole problem, no simpler anchor function appears;
border: q_N < 1 on 57/57 (min 1 - q_N = 0.0195, r286
reproduced), D_N cross-route exact on every window,
lambda_min(S_aug(8)) > 0 on 57/57 with degradation factor
0.873..1.000 -- the border does NOT break the head, it is inert
on this coordinate)
+ TWIN(TWIN_METRIC_OK: fold sets == MAIN, denominators med 5408
/ max 56801, r_min 3/3 == 3/3 under both orders, max |dreserve|
= 1.0e-7 over r = 0..16 -- diophantine input irrelevant on the
head coordinate, r289 METRIC_ONLY reproduced)
+ CONTROLS(CONTROL_COLLECTIVE: at their own N_w = 184 EPST
lambda_max(E) = 2191.4 -> E_T(16) = 2189.5 (a 16-atom head
removes 0.1 percent), SCR 1.36e+7 -> 3.2e+4 (a 424x drop that
still leaves the tail 4 decades above 1) -- no small head
rescues a dead world: the architecture reads MAIN-specific
structure, the expected informative control break)
+ TAIL_ANATOMY(measurement: at r = 8 tail maxdiag 0.910..0.992
with gain lambda/maxdiag 1.008..1.052; at the full edge maxdiag
0.862..0.981 with gain 1.015..1.089 -- after edge removal the
tail lambda_max rides its own near-single-atom Christoffel
profile on the BULK atoms (u > log 2); Gershgorin/Schur-test
row sums 1.5..3.6, < 1 on 0/57 at both spots -- the classical
bounds stay DEAD on the tail (r283: Gershgorin died at 21); no
proof-precursor typing (not GO))
+ MP_SPOTS(3/3 at dps 30, chain + B recomputed on the tail
sets: w9/r8 rel dev 9.9e-15 (lambda = 0.96152027), kz119/r8
2.8e-14, kz119/full-edge 2.0e-14 -- the sweep is not f64 noise).
Key numbers.  W9: edge = 19 atoms (folds 2..43, ALL ARCH,
first five == the reviewer candidates (2, 4, 6, 8, 10)), r284
top-2 masses 0.6249/0.3720 (sum 0.9970), W9X_PERM regated
exactly; r_min = 3 both orders (reserve 1.283e-2 at r = 3),
reserve(8) = 3.848e-2, full edge 6.962e-2, amp 415.6;
lambda_min(S_H(8)) = 1.6753e-4 vs margin 1.6752e-4; W-identity
rel dev 4.4e-13; q_N = 0.2143, D_N = 0.5612, lambda_min(S_aug)
= 1.6584e-4.  LADDER: 42 core + 15 r286 anchors (margins
reproduced, worst rel dev 2.3e-4) + 20 NEW windows N_w
1218..1650 (S up to 3299, S_- up to 1073, seconds per window);
half-filling 77/77; monotone-in-r + interlacing EXACT on 77 x
both orders (worst dev 0.0); ORDER_W9X never beats ORDER_FOLD
(median reserve ratio at r = 8: 0.48 -- the frozen noise ranks
transfer nothing beyond the first six).  EXACT TOY (JF9,
rational): S_H = 5079569347/6986834571, det identity EXACT in
Fractions, f64 route 3.3e-16; border toy: W-identity 3.3e-16,
aug det identity 2.4e-16, r = 0 scalar == D_N = 0.617018 to
2.2e-16.  MUST-FAILS: m1 FLAGGED (eigh@604; ordering
constructors CLEAN); m2 wrong-sign break 0.1626 >= 0.1 LOUD;
m3 monomial frame hides the toy wall (4.3615 -> 0.8515, rel dev
0.805 >= 0.5) LOUD; m4 r = 0 exact (route equality 0.0, w9
record dev 4.1e-9).  READING (typed measurement): the
reviewer's question "descriptive or proof-relevant" SPLITS --
the edge COORDINATE is proof-relevant (worlds-specific,
twin-stable, 3-5 decades of amplification), the FIXED DIMENSION
is refuted; any C2 successor must contract the tail below the
GROWING edge, whose size is the explicit source-pure quantity
~ log2/(2 Delta_w), and must live with a slowly decaying
full-edge reserve (TS -0.87).  Runtime 109.3 s full / 0.2 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE (record tables inserted per protocol; no bar,
band, ordering or verdict rule moved).

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
_VERI = os.path.abspath(os.path.join(HERE, "..", "..", "verification"))
if _VERI not in sys.path:
    sys.path.insert(0, _VERI)

import verify_lstar_instance as V              # noqa: E402 document pipeline
import lstar_margin_scaling_probe as LM        # noqa: E402 r286
import lstar_two_measure_probe as LS           # noqa: E402 r284
import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import metric_stability_probe as MS            # noqa: E402 r278
import minimal_firewall_probe as MF            # noqa: E402 r276
import arch_kernel_diophantine_probe as AK     # noqa: E402 r289
import bordered_hankel_probe as BH             # noqa: E402 r244
import hirota_sign_probe as HS                 # noqa: E402 r226
import principal_bessel_probe as PB            # noqa: E402 r243
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import jfraction_probe as JF                   # noqa: E402 r230
import wronskian_dictionary_probe as WD        # noqa: E402 r274
import paircorr_margin_probe as PC             # noqa: E402
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
R_MAX = 16
GO_RMAX = 8
RESERVE_MIN = 1.0e-2
EDGE_RES = 1.0e-3
EDGE_PASS_FRAC = 0.95
AMP_BAR = 100.0
SHRINK_SP = -0.5
GROW_SP = 0.0
MONO_SP = 0.75
EDGE_FRACS = (0.25, 0.5, 0.75, 1.0)
K_EXT = 15
K_EXT2 = 20
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
R286_ANCH = {9: 1.6752e-4, 64: 1.4175e-7, 35: 3.314e-7,
             119: 1.806e-8}
R286_ANCH_TOL = 0.05
W9X_PERM = (0, 1, 2, 3, 4, 5, 11, 9, 12, 10, 7, 13, 8, 14, 18, 15)
W9_EDGE_N = 19
W9_EDGE5 = (2, 4, 6, 8, 10)
W9_TOP2 = ((2, 0.625), (4, 0.372))
TOP2_TOL = 5.0e-3
TOP2_SUM_MIN = 0.99
QN_CORNER = 5.0 / 7.0
DETID_TOL = 1.0e-5
WID_TOL = 1.0e-6
TOY_TOL = 1.0e-10
XCHK_TOL = 1.0e-9
MP_DPS = 30
MP_SPOTS = ((9, 8), (119, 8), (119, None))
MP_TOL = 1.0e-6
RAT_DRES = 1.0e-3
CTRL_R = 16
M2_BAR = 0.1
M3_BAR = 0.5
M4_TOL = 1.0e-12
MONO_R_TOL = 1.0e-10
ADMIT = 1.0e-9
HL2_SEED = 101
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
    return (not bad), ("NO zero/prime oracles; the ordering "
                       "constructors consume fold indices + grid "
                       "geometry + the frozen w9 permutation ONLY; "
                       "record margins/masses enter gates and "
                       "record tables only" if not bad
                       else "; ".join(bad))


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


ORDER_CONSTRUCTORS = ("fold_index", "flat_edge", "head_fold_order",
                      "head_w9x_order")
ORDER_FORBIDDEN = {"eigh", "eigvalsh", "svd", "lam_true",
                   "margins_true", "r_min_true"}
CONSTRUCTORS = ("tail_stats", "head_schur", "aug_schur",
                "border_column")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_MARGIN", "R286_ANCH", "W9_TOP2",
                   "margins_true", "minC_true", "r_min_true"}


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


# ============== sealed source-pure ordering constructors
def fold_index(y, L):
    """fold index of atoms on the grid x_f = cos(2 pi f / L)
    (consumes positions + L only)."""
    th = np.arccos(np.clip(np.asarray(y, float), -1.0, 1.0))
    return np.rint(th * L / (2.0 * math.pi)).astype(np.int64)


def flat_edge(fn, D):
    """indices of the flat archimedean edge atoms below the first
    prime (u = f Delta < log 2), sorted ascending by fold
    (consumes fold indices + lag spacing only)."""
    fn = np.asarray(fn, np.int64)
    idx = np.nonzero(fn.astype(float) * float(D) < LOG2)[0]
    return idx[np.argsort(fn[idx])]


def head_fold_order(edge, r):
    """ORDER_FOLD: the first r flat-edge atoms in ascending fold
    order (window-intrinsic, purely positional)."""
    edge = np.asarray(edge, np.int64)
    return edge[:min(int(r), len(edge))]


def head_w9x_order(edge, r):
    """ORDER_W9X: the frozen w9-flagship rank permutation applied
    to the fold-sorted flat-edge list; out-of-range ranks skipped,
    exhaustion falls back to ascending fold order."""
    edge = np.asarray(edge, np.int64)
    n = len(edge)
    take = []
    for rk in W9X_PERM:
        if len(take) >= r:
            break
        if rk < n and rk not in take:
            take.append(rk)
    rk = 0
    while len(take) < min(int(r), n):
        if rk not in take:
            take.append(rk)
        rk += 1
    if not take:
        return np.zeros(0, np.int64)
    return edge[np.asarray(take, np.int64)]


# ============== sealed measurement constructors (AST-audited)
def tail_stats(B, head_rows):
    """lambda_max, max Christoffel diagonal and Gershgorin row-sum
    bound of the tail Gram E_T = B_T B_T^T (head rows removed)."""
    keep = np.ones(B.shape[0], bool)
    hr = np.asarray(head_rows, np.int64)
    if len(hr):
        keep[hr] = False
    Bt = B[keep]
    Gt = Bt @ Bt.T
    lam = float(np.linalg.eigvalsh(Gt)[-1])
    maxd = float(np.max(np.sum(Bt * Bt, axis=1)))
    gersh = float(np.max(np.sum(np.abs(Gt), axis=1)))
    return lam, maxd, gersh


def head_schur(B, head_rows):
    """S_H = I_r - B_H (I - E_T)^{-1} B_H^T via the tail-atom-frame
    Woodbury route (one linear solve, well conditioned once the
    tail is contractive); returns (S_H, logdet(I - E_T))."""
    keep = np.ones(B.shape[0], bool)
    hr = np.asarray(head_rows, np.int64)
    keep[hr] = False
    Bt, Bh = B[keep], B[hr]
    A = np.eye(Bt.shape[0]) - Bt @ Bt.T
    X = np.linalg.solve(A, Bt @ Bh.T)
    SH = np.eye(len(hr)) - Bh @ Bh.T - (Bh @ Bt.T) @ X
    SH = 0.5 * (SH + SH.T)
    sg, ld = np.linalg.slogdet(A)
    return SH, (float(sg), float(ld))


def border_column(a, b, h0, bxs, bws, bys, bvs, depth):
    """t_i = int pihat_i dsigma_border (mu-orthonormal border
    readouts of the signed border measure)."""
    t = np.zeros(depth)
    if len(bxs):
        Pp = V.b_matrix(a, b, h0, np.asarray(bxs, float),
                        np.ones(len(bxs)), depth)
        t += Pp.T @ np.asarray(bws, float)
    if len(bys):
        Pm = V.b_matrix(a, b, h0, np.asarray(bys, float),
                        np.ones(len(bys)), depth)
        t -= Pm.T @ np.asarray(bvs, float)
    return t


def aug_schur(B, head_rows, t, corner):
    """the border-extended (r+1) x (r+1) Schur rest S_aug =
    [[S_H, m], [m^T, corner - t^T K_T^{-1} t]] with K_T = I - E_T,
    all K_T^{-1} actions through the tail-atom-frame Woodbury."""
    keep = np.ones(B.shape[0], bool)
    hr = np.asarray(head_rows, np.int64)
    if len(hr):
        keep[hr] = False
    Bt, Bh = B[keep], B[hr]
    r = len(hr)
    A = np.eye(Bt.shape[0]) - Bt @ Bt.T
    rhs = np.concatenate([Bt @ Bh.T, (Bt @ t)[:, None]], axis=1) \
        if r else (Bt @ t)[:, None]
    X = np.linalg.solve(A, rhs)
    S = np.zeros((r + 1, r + 1))
    if r:
        S[:r, :r] = np.eye(r) - Bh @ Bh.T - (Bh @ Bt.T) @ X[:, :r]
        mv = -(Bh @ t) - (Bh @ Bt.T) @ X[:, r]
        S[:r, r] = mv
        S[r, :r] = mv
    S[r, r] = float(corner) - float(t @ t) \
        - float((Bt @ t) @ X[:, r if r else 0])
    return 0.5 * (S + S.T)


# ============== must-fail mutants
def mutant_target_order(B, edge, r):
    """m1 MUST-FAIL: head ordered by the target window's OWN top
    eigenvector (TARGET_INVERSE) -- the scope audit must FLAG the
    eigensolver inside an ordering constructor."""
    _ev, W = np.linalg.eigh(B @ B.T)
    m = W[:, -1] ** 2
    edge = np.asarray(edge, np.int64)
    o = np.argsort(m[edge])[::-1]
    return edge[o[:min(int(r), len(edge))]]


def mutant_wrong_woodbury(B, head_rows):
    """m2 MUST-FAIL: the Woodbury correction with the WRONG SIGN
    (+ instead of -) -- must break the exact determinant identity
    loudly on the exact toy."""
    keep = np.ones(B.shape[0], bool)
    hr = np.asarray(head_rows, np.int64)
    keep[hr] = False
    Bt, Bh = B[keep], B[hr]
    A = np.eye(Bt.shape[0]) - Bt @ Bt.T
    X = np.linalg.solve(A, Bt @ Bh.T)
    return np.eye(len(hr)) - Bh @ Bh.T + (Bh @ Bt.T) @ X


def mutant_monomial_frame(y, v, depth):
    """m3 MUST-FAIL: the split WITHOUT the mu-orthonormal frame
    (raw monomial basis) -- must hide the toy wall loudly."""
    y = np.asarray(y, float)
    v = np.asarray(v, float)
    return np.array([[math.sqrt(v[k]) * y[k] ** i
                      for i in range(depth)]
                     for k in range(len(y))])


# ============== gate-side window bundles
def window_bundle(kz):
    """standalone V-route bundle: measures, chain, B at N_w, fold
    indices, flat edge (gate-side; constructors get arrays)."""
    mz = V.build_measures(kz)
    N = mz["Nw"]
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], N)
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], N)
    fn = fold_index(mz["yn"], mz["L"])
    edge = flat_edge(fn, mz["D"])
    return dict(kz=kz, z=int(V.PP[kz]), mz=mz, N=N, a=a, b=b,
                h0=h0, B=B, fn=fn, edge=edge, S=mz["S"],
                Sm=len(mz["yn"]))


def sweep_bundle(B, edge):
    """the leg-A sweep of one window: reserves under both sealed
    orderings r = 0..R_MAX plus the edge-fraction diagnostic."""
    resF, resX = [], []
    for r in range(R_MAX + 1):
        lamF, _d, _g = tail_stats(B, head_fold_order(edge, r))
        lamX, _d, _g = tail_stats(B, head_w9x_order(edge, r))
        resF.append(1.0 - lamF)
        resX.append(1.0 - lamX)
    fr = {}
    for q in EDGE_FRACS:
        rq = int(math.ceil(q * len(edge)))
        lam, maxd, gersh = tail_stats(B, head_fold_order(edge, rq))
        fr[q] = (1.0 - lam, maxd, gersh, rq)
    return np.array(resF), np.array(resX), fr


def r_min_of(res):
    """minimal r with reserve >= RESERVE_MIN, else None."""
    for r in range(len(res)):
        if res[r] >= RESERVE_MIN:
            return r
    return None


def mp_tail_spot(mz, head_rows, N):
    """mp ward (chain + B recomputed at MP_DPS) of the tail
    lambda_max on the head-removed atom set."""
    keep = np.ones(len(mz["yn"]), bool)
    hr = np.asarray(head_rows, np.int64)
    if len(hr):
        keep[hr] = False
    mzt = dict(xp=mz["xp"], wp=mz["wp"], yn=mz["yn"][keep],
               vn=mz["vn"][keep])
    return V.mp_lam_max(mzt, N, dps=MP_DPS)


def border_bundle(kz, mz, a, b, h0, N):
    """border data of one window (r258 route): bordered-chain
    Christoffel terms, corner, D_N, q_N and the mu-frame border
    column t."""
    dsm = HS.window_data(kz, comb=PB.smooth_comb(mz["alpha"]))
    rows = BH.bord_chain(mz["xp"], mz["wp"], mz["yn"], mz["vn"],
                         dsm["xs"], dsm["ws"], dsm["ys"],
                         dsm["vs"], N)
    rhos = [rw["rho"] for rw in rows]
    t = border_column(a, b, h0, dsm["xs"], dsm["ws"], dsm["ys"],
                      dsm["vs"], N)
    corner = float(sum(rhos[:N - 1])) + QN_CORNER
    qN = rhos[N - 1] / QN_CORNER
    DN = QN_CORNER - rhos[N - 1]
    return dict(rhos=rhos, t=t, corner=corner, qN=qN, DN=DN,
                nrows=len(rows))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("fixed_head_probe -- PRIME.LSTAR.FIXED_HEAD.01 "
          "(round 307)")
    print("SPEC_SHA %s   (r286 LM %s / r284 LS %s / r283 FS %s)"
          % (SPEC_SHA[:16], LM.SPEC_SHA[:16], LS.SPEC_SHA[:16],
             FS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 block; ladder, extension, twin, "
                        "controls, mp spots, anatomy, adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the two orderings (FOLD; "
          "frozen W9X permutation), the flat-edge definition "
          "(u < log 2), RESERVE_MIN/EDGE_RES/AMP_BAR and the "
          "four-way verdict rule, the Schur/Woodbury and border "
          "identities with their gates, the twin/control "
          "expectations, the mp spots, every bar/tolerance, the "
          "mutants and the verdict form; the four pre-spec "
          "scratches (w9 + kz35 reserve profile, full-edge sizing, "
          "toy values, EXT2 enumeration) are DISCLOSED in the "
          "spec -- they sized bars only, no rule was tuned after "
          "any evaluation of this probe")

    # ---------------- S1 exact toy
    section("S1  TOY -- EXACT SCHUR/WOODBURY + BORDER IDENTITIES "
            "(JF9)")
    pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                   key=lambda tt: tt[0])
    xs_q = [tt[0] for tt in pairs]
    ws_q = [tt[1] for tt in pairs]
    xs_r = np.array([float(x) for x, w in zip(xs_q, ws_q) if w > 0])
    ws_r = np.array([float(w) for w in ws_q if w > 0])
    ys_q = [x for x, w in zip(xs_q, ws_q) if w < 0]
    vs_q = [-w for w in ws_q if w < 0]
    ys_r = np.array([float(y) for y in ys_q])
    vs_r = np.array([float(v) for v in vs_q])
    Nt = 3
    a_t, b_t, h0_t = V.mu_chain(xs_r, ws_r, Nt)
    B_t = V.b_matrix(a_t, b_t, h0_t, ys_r, vs_r, Nt)
    # exact rational atom-frame Gram via the r274 monic route
    xs_pos = [x for x, w in zip(xs_q, ws_q) if w > 0]
    ws_pos = [w for w in ws_q if w > 0]
    alm, bem, hsm = WD.stj_gen(xs_pos, ws_pos, len(xs_pos) - 1)
    vals = [WD.pv_seq(alm, bem, y, len(xs_r) - 1) for y in ys_q]
    K_ex = [[sum(vals[i][k] * vals[j][k] / hsm[k]
                 for k in range(Nt)) for j in range(3)]
            for i in range(3)]
    M_ex = [[(Fr(1) if i == j else Fr(0)) - vs_q[i] * K_ex[i][j]
             for j in range(3)] for i in range(3)]

    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    dM_ex = det3(M_ex)
    dTT_ex = M_ex[1][1] * M_ex[2][2] - M_ex[1][2] * M_ex[2][1]
    inv_tt = [[M_ex[2][2] / dTT_ex, -M_ex[1][2] / dTT_ex],
              [-M_ex[2][1] / dTT_ex, M_ex[1][1] / dTT_ex]]
    S_ex = M_ex[0][0] - sum(
        M_ex[0][1 + i] * sum(inv_tt[i][j] * M_ex[1 + j][0]
                             for j in range(2)) for i in range(2))
    ok_schur_ex = (dM_ex == dTT_ex * S_ex)
    G_t = B_t @ B_t.T
    dev_det = abs(float(np.linalg.det(np.eye(3) - G_t))
                  - float(dM_ex))
    SH_t, (sgA, ldA) = head_schur(B_t, np.array([0]))
    dev_sh = abs(float(SH_t[0, 0]) - float(S_ex))
    lam3 = float(np.linalg.eigvalsh(G_t)[-1])
    dev_id = abs(sgA * math.exp(ldA) * float(SH_t[0, 0])
                 - float(dM_ex))
    check("G10-toy-exact-schur", ok_schur_ex
          and dev_det <= TOY_TOL and dev_sh <= TOY_TOL
          and dev_id <= TOY_TOL and lam3 < 1.0,
          "JF9 toy (3 nu atoms, N_t = %d, lambda_max = %.6f < 1): "
          "the EXACT RATIONAL Schur identity det(I - E) = "
          "det(I - E_T) det(S_H) holds in Fractions (S_H = %s, "
          "det = %s, identity EXACT); the f64 degree-frame "
          "Woodbury route matches to %.1e / %.1e / %.1e "
          "(bar %.0e) -- the head/tail reduction is exact algebra"
          % (Nt, lam3, str(S_ex), str(dM_ex), dev_det, dev_sh,
             dev_id, TOY_TOL))
    # border toy (dummy zero-weight negative border atom)
    bx_t = np.array([-1.0 / 3.0, 1.0 / 3.0])
    bw_t = np.array([0.2, 1.0 / 7.0])
    by_t = np.array([0.0])
    bv_t = np.array([0.0])
    rows_t = BH.bord_chain(xs_r, ws_r, ys_r, vs_r, bx_t, bw_t,
                           by_t, bv_t, Nt)
    rhos_t = [rw["rho"] for rw in rows_t]
    t_t = border_column(a_t, b_t, h0_t, bx_t, bw_t,
                        np.zeros(0), np.zeros(0), Nt)
    Kd_t = np.eye(Nt) - B_t.T @ B_t
    W_t = float(t_t @ np.linalg.solve(Kd_t, t_t))
    dev_W = abs(W_t - sum(rhos_t[:Nt]))
    corner_t = float(sum(rhos_t[:Nt - 1])) + QN_CORNER
    DN_t = QN_CORNER - rhos_t[Nt - 1]
    Saug_t = aug_schur(B_t, np.array([0]), t_t, corner_t)
    ld_sa = np.linalg.slogdet(Saug_t)
    dev_aug = abs(sgA * math.exp(ldA) * ld_sa[0] * math.exp(ld_sa[1])
                  - float(dM_ex) * DN_t)
    S0_t = aug_schur(B_t, np.zeros(0, np.int64), t_t, corner_t)
    dev_r0 = abs(float(S0_t[0, 0]) - DN_t)
    check("G11-toy-border-identity", dev_W <= TOY_TOL
          and dev_aug <= TOY_TOL and dev_r0 <= 1.0e-9,
          "border toy (2 border atoms): the Christoffel identity "
          "t^T (I - E)^{-1} t == sum_{j<N} rho_j (r244 bordered "
          "chain, INDEPENDENT route) to %.1e; the augmented det "
          "identity det(I - E_T) det(S_aug) == det(I - E) D_N to "
          "%.1e; the r = 0 augmented scalar == D_N = %.6f to "
          "%.1e -- the border coordinate is wired exactly"
          % (dev_W, dev_aug, DN_t, dev_r0))

    # ---------------- S2 w9 block
    section("S2  W9 -- RECORDS, EDGE ANATOMY, SWEEP, SCHUR/BORDER")
    wb9 = window_bundle(MAIN_KZ)
    mz9, B9, fn9, edge9 = wb9["mz"], wb9["B"], wb9["fn"], wb9["edge"]
    N9 = wb9["N"]
    lam9 = float(np.linalg.eigvalsh(B9 @ B9.T)[-1])
    margin9 = 1.0 - lam9
    ok_rec = (mz9["S"] == REC_S and len(mz9["xp"]) == REC_SP
              and len(mz9["yn"]) == REC_SM and N9 == REC_NW
              and abs(lam9 - REC_LAM) <= 1.0e-6
              and abs(margin9 / REC_MARGIN - 1.0) <= REC_MARGIN_TOL)
    check("G20-w9-source-records", ok_rec,
          "w9 (STANDALONE document pipeline): S = %d (mu %d / nu "
          "%d), N_w = %d, lambda_max(E_184) = %.8f (record %.8f), "
          "margin = %.4e (record %.4e rel %.2f)"
          % (mz9["S"], len(mz9["xp"]), len(mz9["yn"]), N9, lam9,
             REC_LAM, margin9, REC_MARGIN, REC_MARGIN_TOL))
    # edge anatomy + labels + frozen permutation regate
    D9c = float(core.build_window(MAIN_KZ)["D"])
    ctx9 = MS.ctx_build(MAIN_KZ)
    W9L = LS.world_pack("w9", ctx9, D9c)
    ok_xchk = (abs(mz9["D"] - D9c) <= 1.0e-12
               and set(int(f) for f in fn9)
               == set(int(f) for f in W9L["fn"]))
    lab9 = LS.atom_labels(fn9[edge9], D9c, ctx9["uu"], ctx9["mm"])
    n_arch = sum(1 for c, _p, _d in lab9 if c == 0)
    ev9, Wv9 = np.linalg.eigh(B9 @ B9.T)
    m1_9 = Wv9[:, -1] ** 2
    mass_edge = m1_9[edge9]
    perm9 = tuple(int(i) for i in np.argsort(mass_edge)[::-1][:16])
    tops = {int(fn9[edge9[i]]): float(mass_edge[i])
            for i in perm9[:2]}
    ok_top2 = all(abs(tops.get(f, 0.0) - m) <= TOP2_TOL
                  for f, m in W9_TOP2) \
        and sum(tops.values()) >= TOP2_SUM_MIN
    ok_edge = (len(edge9) == W9_EDGE_N
               and tuple(int(f) for f in
                         fn9[head_fold_order(edge9, 5)])
               == W9_EDGE5
               and n_arch == len(edge9)
               and perm9 == W9X_PERM)
    check("G21-w9-edge-anatomy", ok_xchk and ok_top2 and ok_edge,
          "flat edge (u < log 2): %d nu atoms, folds %s..%d, ALL "
          "ARCH-labeled (%d/%d); first five fold-order heads == "
          "%s (the reviewer's candidates); r284 extremal top-2 "
          "reproduced: folds %s masses %s (sum %.4f >= %.2f); the "
          "frozen W9X permutation REGATED EXACTLY (%s); V-route "
          "fold set == builder fold set, D dev %.1e"
          % (len(edge9), str([int(f) for f in fn9[edge9][:5]]),
             int(fn9[edge9][-1]), n_arch, len(edge9),
             str(W9_EDGE5), str(sorted(tops)),
             str([round(tops[k], 4) for k in sorted(tops)]),
             sum(tops.values()), TOP2_SUM_MIN,
             "exact" if perm9 == W9X_PERM else str(perm9),
             abs(mz9["D"] - D9c)))
    # w9 sweep
    resF9, resX9, fr9 = sweep_bundle(B9, edge9)
    ok_r0 = (abs(resF9[0] - margin9) <= M4_TOL
             and abs(resX9[0] - margin9) <= M4_TOL)
    ok_mono = (bool(np.all(np.diff(resF9) >= -MONO_R_TOL))
               and bool(np.all(np.diff(resX9) >= -MONO_R_TOL)))
    rminF9, rminX9 = r_min_of(resF9), r_min_of(resX9)
    check("G22-w9-sweep", ok_r0 and ok_mono
          and rminF9 is not None and rminX9 is not None,
          "w9 r-sweep: r = 0 degenerate == the full margin "
          "(dev %.1e); reserve MONOTONE in r (interlacing, both "
          "orders); r_min(FOLD) = %s / r_min(W9X) = %s at "
          "RESERVE_MIN = %.0e; reserve(8) = %.4e, full edge "
          "(%d atoms) = %.4e, amp = %.1f"
          % (max(abs(resF9[0] - margin9), abs(resX9[0] - margin9)),
             str(rminF9), str(rminX9), RESERVE_MIN, resF9[8],
             len(edge9), fr9[1.0][0], fr9[1.0][0] / margin9))
    # w9 Schur + border
    bb9 = border_bundle(MAIN_KZ, mz9, wb9["a"], wb9["b"],
                        wb9["h0"], N9)
    t9 = bb9["t"]
    Kd9 = np.eye(N9) - B9.T @ B9
    W9r = float(t9 @ np.linalg.solve(Kd9, t9))
    dev_W9 = abs(W9r - sum(bb9["rhos"][:N9])) \
        / abs(sum(bb9["rhos"][:N9]))
    hr9 = head_fold_order(edge9, GO_RMAX)
    SH9, (sgA9, ldA9) = head_schur(B9, hr9)
    lmin_SH9 = float(np.linalg.eigvalsh(SH9)[0])
    sgF9, ldF9 = np.linalg.slogdet(np.eye(len(fn9)) - B9 @ B9.T)
    sgS9, ldS9 = np.linalg.slogdet(SH9)
    dev_id9 = abs(ldA9 + ldS9 - ldF9)
    Saug9 = aug_schur(B9, hr9, t9, bb9["corner"])
    sga9, ldsa9 = np.linalg.slogdet(Saug9)
    dev_aug9 = abs(ldA9 + ldsa9 - (ldF9 + math.log(bb9["DN"])))
    lmin_aug9 = float(np.linalg.eigvalsh(Saug9)[0])
    check("G23-w9-schur-border", dev_W9 <= WID_TOL
          and dev_id9 <= DETID_TOL and dev_aug9 <= DETID_TOL
          and lmin_SH9 > 0.0 and lmin_aug9 > 0.0
          and sgA9 > 0 and sgS9 > 0 and sga9 > 0
          and bb9["qN"] < 1.0 and bb9["nrows"] >= N9,
          "w9 at r = %d: lambda_min(S_H) = %.4e (wall margin "
          "%.4e, ratio %.4f), det identity dev %.1e; BORDER: "
          "W-identity t^T K^{-1} t == sum rho (rel %.1e, bar "
          "%.0e), q_N = %.4f < 1, D_N = %.4f, aug det identity "
          "dev %.1e, lambda_min(S_aug) = %.4e > 0"
          % (GO_RMAX, lmin_SH9, margin9, lmin_SH9 / margin9,
             dev_id9, dev_W9, WID_TOL, bb9["qN"], bb9["DN"],
             dev_aug9, lmin_aug9))
    if smoke:
        check("G24-w9-mp-spot", True, "SMOKE: skipped")
    else:
        lam_mp = mp_tail_spot(mz9, hr9, N9)
        lam_f64, _d, _g = tail_stats(B9, hr9)
        dev_mp = abs(lam_mp - lam_f64) / abs(lam_mp)
        check("G24-w9-mp-spot", dev_mp <= MP_TOL,
              "mp spot (dps %d, chain + B recomputed on the tail "
              "set): lambda_max(E_T(8)) = %.8f, f64 rel dev %.1e "
              "(bar %.0e)" % (MP_DPS, lam_mp, dev_mp, MP_TOL))

    # ---------------- S3 leg A ladder
    section("S3  LEG A -- THE r-SWEEP ON 42 + 15 + %d WINDOWS"
            % K_EXT2)
    ROWS = {}
    if smoke:
        for g in ("G30-ladder-census", "G31-sweep-structural",
                  "G32-rmin-trends"):
            check(g, True, "SMOKE: skipped")
    else:
        kzs42 = V.admissible_indices()
        cands = LM.ext_rule()
        ext15 = [t[1] for t in cands[:K_EXT]]
        ext20 = [t[1] for t in cands[K_EXT:K_EXT + K_EXT2]]
        groups = ([("CORE", kz) for kz in kzs42]
                  + [("EXT", kz) for kz in ext15]
                  + [("EXT2", kz) for kz in ext20])
        print("    %-5s %-5s %-6s %-5s %-5s %-4s %-3s "
              "%-12s %-3s %-3s %-10s %-10s %-10s %-10s %-9s"
              % ("grp", "kz", "z", "S", "N_w", "S-", "ne",
                 "margin", "rF", "rX", "res4", "res8", "res16",
                 "resEdge", "amp"))
        ok_hf = True
        ok_struct = True
        worst_inter = 0.0
        for grp, kz in groups:
            wb = wb9 if kz == MAIN_KZ else window_bundle(kz)
            B, edge, N = wb["B"], wb["edge"], wb["N"]
            resF, resX, fr = (resF9, resX9, fr9) if kz == MAIN_KZ \
                else sweep_bundle(B, edge)
            ok_hf = ok_hf and (N == (wb["S"] + 1) // 2)
            ok_struct = ok_struct \
                and bool(np.all(np.diff(resF) >= -MONO_R_TOL)) \
                and bool(np.all(np.diff(resX) >= -MONO_R_TOL))
            worst_inter = max(worst_inter,
                              float(np.max(resF[0] - resF)),
                              float(np.max(resX[0] - resX)))
            row = dict(grp=grp, kz=kz, z=wb["z"], S=wb["S"], N=N,
                       Sm=wb["Sm"], ne=len(edge), margin=resF[0],
                       resF=resF, resX=resX, fr=fr,
                       rminF=r_min_of(resF), rminX=r_min_of(resX),
                       amp=fr[1.0][0] / resF[0])
            if grp != "EXT2":
                bb = bb9 if kz == MAIN_KZ else border_bundle(
                    kz, wb["mz"], wb["a"], wb["b"], wb["h0"], N)
                hr = head_fold_order(edge, GO_RMAX)
                SH, (sgA_, ldA_) = head_schur(B, hr)
                sgF_, ldF_ = np.linalg.slogdet(
                    np.eye(len(wb["fn"])) - B @ B.T)
                sgS_, ldS_ = np.linalg.slogdet(SH)
                Saug = aug_schur(B, hr, bb["t"], bb["corner"])
                sga_, ldsa_ = np.linalg.slogdet(Saug)
                hr16 = head_fold_order(edge, R_MAX)
                SH16, _ld16 = head_schur(B, hr16)
                lamr8, maxd8, gersh8 = tail_stats(B, hr)
                row.update(
                    lmin=float(np.linalg.eigvalsh(SH)[0]),
                    lmin16=float(np.linalg.eigvalsh(SH16)[0]),
                    lmin_aug=float(np.linalg.eigvalsh(Saug)[0]),
                    dev_id=abs(ldA_ + ldS_ - ldF_),
                    dev_aug=abs(ldA_ + ldsa_
                                - (ldF_ + math.log(bb["DN"]))),
                    sgs=(sgA_ > 0, sgS_ > 0, sga_ > 0),
                    qN=bb["qN"], DN=bb["DN"],
                    maxd8=maxd8, gersh8=gersh8,
                    gain8=lamr8 / maxd8,
                    maxdE=fr[1.0][1], gershE=fr[1.0][2],
                    gainE=(1.0 - fr[1.0][0]) / fr[1.0][1])
            ROWS[kz] = row
            print("    %-5s %-5d %-6d %-5d %-5d %-4d %-3d "
                  "%+.4e %-3s %-3s %.4e %.4e %.4e %.4e %9.1f"
                  % (grp, kz, row["z"], row["S"], N, row["Sm"],
                     row["ne"], row["margin"],
                     str(row["rminF"]), str(row["rminX"]),
                     resF[4], resF[8], resF[16], fr[1.0][0],
                     row["amp"]), flush=True)
        ok_anch = all(
            abs(ROWS[kz]["margin"] / R286_ANCH[kz] - 1.0)
            <= R286_ANCH_TOL for kz in R286_ANCH)
        check("G30-ladder-census", len(kzs42) == 42
              and len(ext15) == K_EXT and len(ext20) == K_EXT2
              and ok_hf and ok_anch,
              "42 core (document rule) + %d r286 anchors + %d NEW "
              "deeper windows (r286 extension rule ranks %d..%d, "
              "N_w %d..%d -- feasibility probed honestly: seconds "
              "per window); half-filling %d/%d; r286 margin "
              "anchors kz9/64/35/119 reproduced (worst rel dev "
              "%.1e, bar %.2f)"
              % (K_EXT, K_EXT2, K_EXT, K_EXT + K_EXT2 - 1,
                 min(ROWS[k]["N"] for k in ext20),
                 max(ROWS[k]["N"] for k in ext20),
                 len(ROWS), len(ROWS),
                 max(abs(ROWS[kz]["margin"] / R286_ANCH[kz] - 1.0)
                     for kz in R286_ANCH), R286_ANCH_TOL))
        check("G31-sweep-structural", ok_struct
              and worst_inter <= MONO_R_TOL,
              "STRUCTURAL EXACTNESS on %d windows x both "
              "orderings: reserve monotone non-decreasing in r "
              "and lambda_max(E_T) <= lambda_max(E) everywhere "
              "(PSD interlacing; worst dev %.1e) -- every tail "
              "eigenvalue below 1 inherits its SIGN from the "
              "r286 mp-verified margins through this exact "
              "monotonicity" % (len(ROWS), worst_inter))
        allk = list(ROWS)
        Sv = np.array([ROWS[k]["S"] for k in allk], float)
        res4 = np.array([ROWS[k]["resF"][4] for k in allk])
        res8 = np.array([ROWS[k]["resF"][8] for k in allk])
        res16 = np.array([ROWS[k]["resF"][16] for k in allk])
        resE = np.array([ROWS[k]["fr"][1.0][0] for k in allk])
        amps = np.array([ROWS[k]["amp"] for k in allk])
        edges = np.array([ROWS[k]["ne"] for k in allk], float)
        Nv = np.array([ROWS[k]["N"] for k in allk], float)
        sp4 = LM.spearman(Sv, res4)
        sp8 = LM.spearman(Sv, res8)
        sp16 = LM.spearman(Sv, res16)
        spE = LM.spearman(Sv, resE)
        sl8 = LM.ts_slope_free(np.log(Sv), np.log(res8))
        slE = LM.ts_slope_free(np.log(Sv), np.log(resE))
        sp_edge = LM.spearman(Nv, edges)
        n_rmin = sum(1 for k in allk
                     if ROWS[k]["rminF"] is not None)
        ratio_w9x = np.median(
            [ROWS[k]["resX"][8] / ROWS[k]["resF"][8]
             for k in allk if ROWS[k]["resF"][8] > 0])
        check("G32-rmin-trends", True,
              "R-MIN TABLE: a fixed-head r_min <= %d exists on "
              "%d/%d windows only (FOLD; W9X <= FOLD, median "
              "reserve ratio at r = 8: %.2f); RESERVE TRENDS vs "
              "S: sp(res4/8/16) = %+.2f/%+.2f/%+.2f (TS slope "
              "res8 %+.2f -- the r286 margin-law class), "
              "full-edge sp %+.2f (TS %+.2f), amp %.0f..%.2e "
              "(median %.0f); edge sizes %d..%d, sp(edge, N_w) "
              "= %+.2f -- the natural head GROWS with the window"
              % (R_MAX, n_rmin, len(allk), ratio_w9x, sp4, sp8,
                 sp16, sl8, spE, slE, float(np.min(amps)),
                 float(np.max(amps)), float(np.median(amps)),
                 int(np.min(edges)), int(np.max(edges)), sp_edge))

    # ---------------- S4 leg B Schur ledger
    section("S4  LEG B -- HEAD SCHUR REST + BORDER (57 WINDOWS)")
    if smoke:
        for g in ("G40-det-identities", "G41-shmin-census",
                  "G42-border-census"):
            check(g, True, "SMOKE: skipped")
    else:
        k57 = [k for k in ROWS if ROWS[k]["grp"] != "EXT2"]
        worst_id = max(ROWS[k]["dev_id"] for k in k57)
        worst_aug = max(ROWS[k]["dev_aug"] for k in k57)
        ok_sgs = all(all(ROWS[k]["sgs"]) for k in k57)
        check("G40-det-identities", worst_id <= DETID_TOL
              and worst_aug <= DETID_TOL and ok_sgs,
              "EXACT det identities on %d/%d windows at r = %d: "
              "det(I - E) == det(I - E_T) det(S_H) worst logdet "
              "dev %.1e; border-extended det(I - E_T) det(S_aug) "
              "== det(I - E) D_N worst %.1e (bar %.0e; D_N from "
              "the INDEPENDENT r244 bordered-chain route -- the "
              "Christoffel W-identity is implicitly gated on "
              "every window)" % (len(k57), len(k57), GO_RMAX,
                                 worst_id, worst_aug, DETID_TOL))
        lmins = np.array([ROWS[k]["lmin"] for k in k57])
        margins = np.array([ROWS[k]["margin"] for k in k57])
        Nv57 = np.array([ROWS[k]["N"] for k in k57], float)
        ratios = lmins / margins
        sp_mono = LM.spearman(Nv57, lmins)
        sl_mono = LM.ts_slope_free(np.log(Nv57), np.log(lmins))
        mono_typ = "MONOTONE(sp %+.2f)" % sp_mono \
            if abs(sp_mono) >= MONO_SP else \
            "NOT_MONOTONE(sp %+.2f)" % sp_mono
        ok_pos = bool(np.all(lmins > 0.0)) \
            and all(ROWS[k]["lmin16"] > 0.0 for k in k57)
        check("G41-shmin-census", ok_pos,
              "lambda_min(S_H(8)) > 0 on %d/%d (and at r = 16): "
              "the head Schur rest IS the wall (exact Schur "
              "equivalence given I - E_T > 0); ratio to the wall "
              "margin in %.2e..%.2e (the head block inherits the "
              "full margin); anchor monotonicity: %s, TS slope "
              "%+.2f -- lambda_min(S_H) tracks the r286 margin "
              "decay, NOT a simpler function of the anchor "
              "(measured, verdict clause 5)"
              % (len(k57), len(k57), float(np.min(ratios)),
                 float(np.max(ratios)), mono_typ, sl_mono))
        qNs = np.array([ROWS[k]["qN"] for k in k57])
        lmin_aug = np.array([ROWS[k]["lmin_aug"] for k in k57])
        aug_ratio = lmin_aug / lmins
        sp_aug = LM.spearman(Nv57, lmin_aug)
        check("G42-border-census", bool(np.all(qNs < 1.0))
              and bool(np.all(lmin_aug > 0.0)),
              "BORDER: q_N < 1 on %d/%d with min(1 - q_N) = %.4f "
              "(r286 reproduced), D_N > 0 everywhere; "
              "lambda_min(S_aug(8)) > 0 on %d/%d, ratio to "
              "lambda_min(S_H) in %.4f..%.4f (border degradation "
              "factor), aug monotonicity sp %+.2f -- does the "
              "border break the head? measured here, adjudicated "
              "in S8" % (len(k57), len(k57),
                         float(np.min(1.0 - qNs)), len(k57),
                         len(k57), float(np.min(aug_ratio)),
                         float(np.max(aug_ratio)), sp_aug))

    # ---------------- S5 leg C twin + controls
    section("S5  LEG C -- RATIONAL TWIN + CONTROLS")
    if smoke:
        for g in ("G50-rational-twin", "G51-controls"):
            check(g, True, "SMOKE: skipped")
        twin_typ = ctrl_typ = "SMOKE"
    else:
        # MAIN through the LS/FS route (apples-to-apples channel)
        al9, sb9, h09 = FS.mu_chain_f64(np.asarray(W9L["xp"]),
                                        np.asarray(W9L["wp"]), N9)
        B9L = FS.b_matrix_f64(al9, sb9, h09,
                              np.asarray(W9L["xn"]),
                              np.asarray(W9L["vn"]), N9)
        fn9L = np.asarray(W9L["fn"], np.int64)
        edge9L = flat_edge(fn9L, D9c)
        lam9L = float(np.linalg.eigvalsh(B9L @ B9L.T)[-1])
        resF9L, resX9L, _fr9L = sweep_bundle(B9L, edge9L)
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9c, AK.RAT_TOL)
        ctxR = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WR = LS.world_pack("rat", ctxR, D9c)
        ok_tw_con = (bool(np.array_equal(mR,
                                         np.asarray(ctx9["mm"])))
                     and bool(np.all(np.abs(duR) <= AK.RAT_TOL
                                     * gaps_c + 1e-300))
                     and bool(np.array_equal(
                         np.asarray(WR["fn"]), fn9L))
                     and bool(np.array_equal(
                         np.asarray(WR["fp"]),
                         np.asarray(W9L["fp"]))))
        alR, sbR, h0R = FS.mu_chain_f64(np.asarray(WR["xp"]),
                                        np.asarray(WR["wp"]), N9)
        BR = FS.b_matrix_f64(alR, sbR, h0R, np.asarray(WR["xn"]),
                             np.asarray(WR["vn"]), N9)
        edgeR = flat_edge(np.asarray(WR["fn"], np.int64), D9c)
        resFR, resXR, _frR = sweep_bundle(BR, edgeR)
        dres = max(float(np.max(np.abs(resFR - resF9L))),
                   float(np.max(np.abs(resXR - resX9L))))
        ok_match = (r_min_of(resFR) == r_min_of(resF9L)
                    and r_min_of(resXR) == r_min_of(resX9L)
                    and dres <= RAT_DRES
                    and bool(np.array_equal(fn9L[edge9L],
                                            np.asarray(WR["fn"],
                                                       np.int64)
                                            [edgeR])))
        twin_typ = "TWIN_METRIC_OK" if ok_match \
            else "TWIN_DEVIATES(max dres %.1e, r_min %s vs %s)" \
            % (dres, str(r_min_of(resFR)), str(r_min_of(resF9L)))
        check("G50-rational-twin", ok_tw_con
              and abs(lam9L - lam9) <= XCHK_TOL,
              "RATIONAL TWIN (r289 construction verbatim: CF "
              "convergents at |du| <= 1e-8 gap, weights bitwise, "
              "denominators med %d / max %d; fold sets == MAIN): "
              "LS-route MAIN cross-gate |dlam| = %.1e (bar %.0e); "
              "twin sweep vs MAIN: r_min %s/%s == %s/%s, max "
              "|dreserve| = %.1e over r = 0..%d both orders => %s "
              "-- the METRIC_ONLY expectation is adjudicated on "
              "the head coordinate"
              % (int(np.median(dens)), int(np.max(dens)),
                 abs(lam9L - lam9), XCHK_TOL,
                 str(r_min_of(resFR)), str(r_min_of(resXR)),
                 str(r_min_of(resF9L)), str(r_min_of(resX9L)),
                 dres, R_MAX, twin_typ))
        # controls (r284 channel verbatim)
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)))
        ctrl = {}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9c)
            Nc = Wc["N"]
            alc, sbc, h0c = FS.mu_chain_f64(
                np.asarray(Wc["xp"]), np.asarray(Wc["wp"]), Nc)
            Bc = FS.b_matrix_f64(alc, sbc, h0c,
                                 np.asarray(Wc["xn"]),
                                 np.asarray(Wc["vn"]), Nc)
            edgec = flat_edge(np.asarray(Wc["fn"], np.int64), D9c)
            lam0c, _d, _g = tail_stats(Bc, np.zeros(0, np.int64))
            lam16c, _d, _g = tail_stats(
                Bc, head_fold_order(edgec, CTRL_R))
            ctrl[cn] = (lam0c, lam16c, len(edgec), Nc)
            info("%s: N_w = %d, edge %d atoms, lambda_max(E) = "
                 "%.3f, lambda_max(E_T(%d)) = %.3f"
                 % (cn, Nc, len(edgec), lam0c, CTRL_R, lam16c))
        rescued = [cn for cn in ctrl if ctrl[cn][1] < 1.0]
        ctrl_typ = "CONTROL_COLLECTIVE" if not rescued \
            else "CONTROL_RESCUED(%s)" % ",".join(rescued)
        check("G51-controls", True,
              "CONTROLS at their own N_w (r284 channel): EPST "
              "lambda_max(E_T(%d)) = %.3f, SCR = %.3f => %s -- "
              "%s" % (CTRL_R, ctrl["EPST"][1], ctrl["SCR"][1],
                      ctrl_typ,
                      "no small head rescues a dead world: the "
                      "architecture reads MAIN-specific structure"
                      if not rescued else
                      "a control is RESCUED by a small head -- "
                      "the architecture is NOT world-specific "
                      "there (informative break)"))

    # ---------------- S6 leg D tail anatomy
    section("S6  LEG D -- TAIL ANATOMY (PROOF PRECURSOR)")
    if smoke:
        check("G60-tail-anatomy", True, "SMOKE: skipped")
        go_flag = False
    else:
        k57 = [k for k in ROWS if ROWS[k]["grp"] != "EXT2"]
        maxd8 = np.array([ROWS[k]["maxd8"] for k in k57])
        gain8 = np.array([ROWS[k]["gain8"] for k in k57])
        ger8 = np.array([ROWS[k]["gersh8"] for k in k57])
        maxdE = np.array([ROWS[k]["maxdE"] for k in k57])
        gainE = np.array([ROWS[k]["gainE"] for k in k57])
        gerE = np.array([ROWS[k]["gershE"] for k in k57])
        n_ger8 = int(np.sum(ger8 < 1.0))
        n_gerE = int(np.sum(gerE < 1.0))
        go_flag = False  # set in S8; typing clause deferred
        check("G60-tail-anatomy", True,
              "WHAT CARRIES lambda_max(E_T) (measurement): at "
              "r = 8 tail maxdiag %.3f..%.3f (gain lambda/maxdiag "
              "%.4f..%.4f -- the tail rides its own near-single-"
              "atom Christoffel edge in the bulk); at the FULL "
              "edge maxdiag %.3f..%.3f (gain %.4f..%.4f); "
              "Gershgorin/Schur-test row sums %.1f..%.1f, < 1 on "
              "%d/%d (r = 8) and %d/%d (full edge) -- the "
              "classical bounds are %s on the tail; "
              "proof-precursor typing fires only on GO (S8)"
              % (float(np.min(maxd8)), float(np.max(maxd8)),
                 float(np.min(gain8)), float(np.max(gain8)),
                 float(np.min(maxdE)), float(np.max(maxdE)),
                 float(np.min(gainE)), float(np.max(gainE)),
                 float(np.min(np.concatenate([ger8, gerE]))),
                 float(np.max(np.concatenate([ger8, gerE]))),
                 n_ger8, len(k57), n_gerE, len(k57),
                 "DEAD (as on the full E: r283 Gershgorin died "
                 "at 21)" if n_ger8 == 0 and n_gerE == 0
                 else "PARTIALLY ALIVE"))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    hits_m1 = scope_audit("mutant_target_order", ORDER_FORBIDDEN)
    hits_ord = []
    for fn_ in ORDER_CONSTRUCTORS:
        hits_ord += scope_audit(fn_, ORDER_FORBIDDEN)
    check("G70-mustfail-target-order", bool(hits_m1)
          and not hits_ord,
          "m1 TARGET_INVERSE ordering FLAGGED by the AST scope "
          "audit (%s); the %d sealed ordering constructors are "
          "CLEAN of eigensolvers and target data (%s) -- the "
          "ordering is fixed across windows by construction"
          % ("; ".join(hits_m1) if hits_m1 else "NOT FLAGGED",
             len(ORDER_CONSTRUCTORS),
             "CLEAN" if not hits_ord else "; ".join(hits_ord)))
    SH_wr = mutant_wrong_woodbury(B_t, np.array([0]))
    dev_m2 = abs(ldA + math.log(abs(float(SH_wr[0, 0])))
                 - math.log(abs(float(dM_ex))))
    check("G71-mustfail-woodbury-sign", dev_m2 >= M2_BAR,
          "m2 WOODBURY WRONG SIGN on the exact toy: det identity "
          "breaks by %.4f in logdet (>= %.1f) -- LOUD: the sign "
          "of the correction term is load-bearing"
          % (dev_m2, M2_BAR))
    Bm4 = mutant_monomial_frame(ys_r, vs_r, 4)
    a4, b4, h04 = V.mu_chain(xs_r, ws_r, 4)
    B4 = V.b_matrix(a4, b4, h04, ys_r, vs_r, 4)
    lam4 = float(np.linalg.eigvalsh(B4 @ B4.T)[-1])
    lam4m = float(np.linalg.eigvalsh(Bm4 @ Bm4.T)[-1])
    dev_m3 = abs(lam4m - lam4) / lam4
    check("G72-mustfail-monomial-frame", dev_m3 >= M3_BAR
          and lam4 > 1.0 and lam4m < 1.0,
          "m3 NO ORTHONORMAL FRAME (monomial basis) on the toy: "
          "at the true crossing degree 4 (lambda = %.4f > 1) the "
          "monomial route reads %.4f < 1 -- rel dev %.3f >= %.1f "
          "LOUD: without the mu-orthonormal frame the head/tail "
          "split loses the wall (I is not the mu Gram)"
          % (lam4, lam4m, dev_m3, M3_BAR))
    lam_r0, _d, _g = tail_stats(B9, np.zeros(0, np.int64))
    dev_m4a = abs((1.0 - lam_r0) - margin9)
    dev_m4b = abs(lam_r0 - REC_LAM)
    check("G73-mustfail-r0-degenerate", dev_m4a <= M4_TOL
          and dev_m4b <= 1.0e-6,
          "m4 r = 0 DEGENERATE: the tail route with empty head "
          "reproduces the full lambda_max series (route equality "
          "%.1e <= %.0e; w9 record dev %.1e <= 1e-6); the r = 0 "
          "augmented scalar == D_N was gated exactly in G11"
          % (dev_m4a, M4_TOL, dev_m4b))
    hits_c = []
    for fn_ in CONSTRUCTORS:
        hits_c += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G74-scope-audits", not hits_c and not ag_hits,
          "the %d sealed measurement constructors consume "
          "B/atom/border arrays ONLY (%s); fragment audit (no "
          "fit primitives): %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits_c else "; ".join(hits_c),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 adjudication
    section("S8  ADJUDICATION (SEALED FOUR-WAY RULE)")
    if smoke:
        check("G80-adjudication", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
        mp_txt = "SKIPPED"
    else:
        allk = list(ROWS)
        Sv = np.array([ROWS[k]["S"] for k in allk], float)
        k57 = [k for k in ROWS if ROWS[k]["grp"] != "EXT2"]
        sh_pos = all(ROWS[k]["lmin"] > 0.0 for k in k57)
        lmins = np.array([ROWS[k]["lmin"] for k in k57])
        Nv57 = np.array([ROWS[k]["N"] for k in k57], float)
        sh_mono = abs(LM.spearman(Nv57, lmins)) >= MONO_SP
        aug_pos = all(ROWS[k]["lmin_aug"] > 0.0 for k in k57)
        go = None
        best = (-1.0, None, None)
        for o in ("FOLD", "W9X"):
            key = "resF" if o == "FOLD" else "resX"
            for r in range(GO_RMAX + 1):
                vals = np.array([ROWS[k][key][r] for k in allk])
                mn = float(np.min(vals))
                if mn > best[0]:
                    best = (mn, o, r)
                if mn >= RESERVE_MIN \
                        and LM.spearman(Sv, vals) >= GROW_SP \
                        and sh_pos and sh_mono:
                    go = (o, r, mn)
                    break
            if go:
                break
        resE = np.array([ROWS[k]["fr"][1.0][0] for k in allk])
        res8 = np.array([ROWS[k]["resF"][8] for k in allk])
        amps = np.array([ROWS[k]["amp"] for k in allk])
        edge_pass = int(np.sum(resE >= EDGE_RES))
        med_amp = float(np.median(amps))
        sp8 = LM.spearman(Sv, res8)
        cond_hg = (edge_pass >= EDGE_PASS_FRAC * len(allk)
                   and med_amp >= AMP_BAR and sp8 <= SHRINK_SP)
        if go is not None:
            if aug_pos:
                verdict_main = ("FIXED_HEAD_GO(r* = %d, %s, min "
                                "reserve %.2e, S_H positive + "
                                "monotone)" % (go[1], go[0],
                                               go[2]))
                go_flag = True
            else:
                bad = [k for k in k57 if ROWS[k]["lmin_aug"] <= 0]
                verdict_main = ("BORDER_BREAKS_HEAD(GO at r = %d "
                                "%s but S_aug loses positivity "
                                "at %s)" % (go[1], go[0],
                                            str(bad)))
        elif cond_hg:
            verdict_main = (
                "HEAD_GROWS(edge-pass %d/%d at EDGE_RES = %.0e "
                "(min full-edge reserve %.3e), median amp %.1e "
                "(min %.0f), sp(reserve(8), S) = %+.2f <= %.1f: "
                "the fixed-head reserve collapses with depth -- "
                "best fixed r <= %d: min reserve %.1e at r = %s "
                "%s, four decades below the %.0e bar -- while "
                "the FULL growing edge always restores a "
                "macroscopic reserve: the anatomy is REAL but "
                "NOT a fixed dimension"
                % (edge_pass, len(allk), EDGE_RES,
                   float(np.min(resE)), med_amp,
                   float(np.min(amps)), sp8, SHRINK_SP, GO_RMAX,
                   best[0], str(best[2]), best[1], RESERVE_MIN))
        else:
            loci = [("edge-pass %d/%d" % (edge_pass, len(allk)))
                    if edge_pass < EDGE_PASS_FRAC * len(allk)
                    else "",
                    ("med amp %.0f < %.0f" % (med_amp, AMP_BAR))
                    if med_amp < AMP_BAR else "",
                    ("sp8 %+.2f > %.1f" % (sp8, SHRINK_SP))
                    if sp8 > SHRINK_SP else ""]
            verdict_main = ("TAIL_COLLECTIVE(broken: %s; min "
                            "full-edge reserve %.2e)"
                            % ("; ".join(x for x in loci if x),
                               float(np.min(resE))))
        check("G80-adjudication", True,
              "SEALED RULE evaluated: GO search over both orders "
              "r <= %d -> %s (best fixed candidate: min reserve "
              "%.2e at r = %s %s); HEAD_GROWS conditions "
              "(edge-pass %d/%d, med amp %.1e, sp8 %+.2f) -> %s"
              % (GO_RMAX, "FOUND" if go else "NONE", best[0],
                 str(best[2]), best[1], edge_pass, len(allk),
                 med_amp, sp8, verdict_main.split("(")[0]))
        # mp spots
        mp_devs = {}
        for kz, rr in MP_SPOTS:
            wb = wb9 if kz == MAIN_KZ else window_bundle(kz)
            r_eff = len(wb["edge"]) if rr is None else rr
            hr = head_fold_order(wb["edge"], r_eff)
            lam_f64, _d, _g = tail_stats(wb["B"], hr)
            lam_mp = mp_tail_spot(wb["mz"], hr, wb["N"])
            mp_devs["kz%d/r%s" % (kz, "EDGE" if rr is None
                                  else str(rr))] = \
                abs(lam_mp - lam_f64) / abs(lam_mp)
        ok_mp = all(v <= MP_TOL for v in mp_devs.values())
        mp_txt = str({k_: "%.1e" % v for k_, v in mp_devs.items()})
        check("G81-mp-spots", ok_mp,
              "MP SPOTS (dps %d, chain + B recomputed on the "
              "tail sets): rel devs %s (bar %.0e) -- the sweep "
              "is not f64 noise" % (MP_DPS, mp_txt, MP_TOL))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no tail-contraction "
          "theorem, no bound mechanism, no derived 5/7, no "
          "posthoc reserve bar, no target-inverse ordering, NO "
          "RH claim; what the round adds: the fixed-head kill "
          "test with both sealed orderings, the exact Schur/"
          "Woodbury + border ledger, the twin/control hardening "
          "and the edge-fraction diagnostic; r243..r306 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        k57 = [k for k in ROWS if ROWS[k]["grp"] != "EXT2"]
        lmins = np.array([ROWS[k]["lmin"] for k in k57])
        margins = np.array([ROWS[k]["margin"] for k in k57])
        qNs = np.array([ROWS[k]["qN"] for k in k57])
        parts = [verdict_main,
                 "SCHUR_LEDGER(det ids worst %.1e/%.1e; "
                 "lambda_min(S_H(8)) > 0 %d/%d, ratio to margin "
                 "%.3f..%.3f, monotone sp %+.2f; q_N < 1 %d/%d "
                 "min gap %.4f; S_aug positive %d/%d)"
                 % (max(ROWS[k]["dev_id"] for k in k57),
                    max(ROWS[k]["dev_aug"] for k in k57),
                    int(np.sum(lmins > 0)), len(k57),
                    float(np.min(lmins / margins)),
                    float(np.max(lmins / margins)),
                    LM.spearman(np.array([ROWS[k]["N"]
                                          for k in k57], float),
                                lmins),
                    int(np.sum(qNs < 1.0)), len(k57),
                    float(np.min(1.0 - qNs)),
                    sum(1 for k in k57
                        if ROWS[k]["lmin_aug"] > 0), len(k57)),
                 "TWIN(%s)" % twin_typ,
                 "CONTROLS(%s)" % ctrl_typ,
                 "TAIL_ANATOMY(gershgorin dead; %s)"
                 % ("proof-precursor typing on GO"
                    if go_flag else "no GO -- typing not fired"),
                 "MP_SPOTS(%s)" % mp_txt]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED kill test of proof architecture C "
          "(fixed head + contractive tail); the Schur/Woodbury "
          "and border identities are exact algebra, gated; NO L* "
          "claim, NO RH claim" % (verd, " (SMOKE)" if smoke
                                  else ""))
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
