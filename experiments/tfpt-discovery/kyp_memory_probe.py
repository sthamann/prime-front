#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kyp_memory_probe -- PRIME.PORT.COUPLEDTAU.KYP_MEMORY.01
(round 275): the l^1 -> l^2 CURRENCY-REFORM TEST in state-space
form.  After r272 (the lost cancellation sits at address c3 =
beyond blind level-2 pairing; flip condition delta' > 0.21 of the
available gamma_true 0.45; TRUTH_ALLOWS) and r273 (the N^{-0.45}
truth decay is GENERIC -- root-scale baseline of signed sums,
coin-like P signs, no local rule), the reviewer-authorized track
2 question: can a source-pure QUADRATIC ENERGY -- a storage
operator P >= 0 with the discrete KYP inequality
    T_j^T P_{j+1} T_j - P_j + C_j^T C_j <= 0
over the exact block dynamics -- certify that cancellation
WITHOUT any sign law?  Cauchy-Schwarz target: a positive G_w with
x^T G_w x < M^2 AND e^T G_w^{-1} e <= 1 for x = (Z_loc,
b_0..b_{J-1}), Z = e^T x, gives |Z|^2 <= (e^T G^{-1} e)
(x^T G x) < M^2.  G_w's PROVENANCE must be the exact rank-1 block
dynamics (KYP memory, telescope), NOT a per-window SDP ("kz15
with a tie" -- typed FORBIDDEN); the memory must not consume q_N,
Z_N or the true margin (source atoms + exact transfer + fixed
boundary conditions only) and it MUST fail on the control worlds
exactly where their wall kips.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r272 machinery verbatim): t_{N-2} = sum_b ct_b
(r244 chain rows, r266 eval); F = 0.20 edge split (FROZEN),
Z_loc = t_edge + chain, Z = t_{N-2} + chain; maximal same-sign
runs of the bx-sorted bulk with exact signed sums s_i.  SEALED
BLOCK CONVENTION (r270/r272, offset 0 FROZEN): level-2 blocks
b_j = s_{2j} + s_{2j+1}, the odd tail run its own final block;
Z = Z_loc + sum_j b_j (exact bookkeeping).  Demand scale
M_W = sqrt(5/7), M_W^2 = 5/7 exactly (rational).

LEG A -- THE BLOCK STATE SYSTEM (sealed realization): state
x_j = (acc_j, 1) -- the block analogue of the driven-recursion
state (r, r_-, accumulator): the block chain is FIRST-ORDER
(each block enters Z once), so the memory question lives on
(accumulator, homogenization) alone, dimension 2; transfer
T_j = [[1, b_j], [0, 1]] EXACT (unitriangular, the block drive
rides in the transfer -- exact from chain coefficients + block
atoms); readout C_j = (0, b_j), so C_j x_j = b_j = the block's
contribution to Z; x_0 = (Z_loc, 1) the fixed boundary
condition; acc_J = Z.  Gates: (a1) float bookkeeping
|acc_J - Z| within the r272 contribution-ward floors (1e-9 main
N <= 400 / 3e-6 deep / 1e-6 controls, vs abs mass); (a2) exact
rational identity acc_J == Z_loc + sum b_j (dev 0 -- floats are
dyadic, Fraction() is exact).

LEG B -- THE KYP CLASS LADDER (test sequence binding: constant
-> even/odd -> period 4 -> recursive Riccati).  The KYP
telescope plus the terminal-usefulness condition P_J >= E11
(== e^T G_w^{-1} e <= 1 in the pulled-back G geometry) give
Z^2 + sum_j (C_j x_j)^2 <= x_0^T P_0 x_0 =: E_w; certification
would be E_w < 5/7 (EXACT rational compare).  The search may be
numeric, but the found P is rationalized and the KYP inequality
verified EXACTLY (2x2 LMI: m11 <= 0, m22 <= 0, m11 m22 - m12^2
>= 0 in exact integer-rational arithmetic) -- that is the gate.
(b1) EXISTENCE per class:
  UNIFORM CLASSES (period m = 1, 2, 4): the two-part EXACT
  OBSTRUCTION (paper algebra derived BEFORE any run, machine-
  verified per world):
  (o1) FIBER FORCING: the LMI (1,1) entries telescope to zero
    around every period => all p11 equal; TWO DISTINCT drive
    values in one transition class force p11 = 0 and p12
    constant via the off-diagonal p11 b_j + (p12' - p12) = 0;
    PSD then forces p12 = 0; terminal usefulness (p11 >= 1) is
    dead.
  (o2) DESCENT: with p11 = p12 = 0 the (2,2) entry demands
    p22_next <= p22_cur - b_j^2; any m consecutive blocks return
    to the same class => sum b^2 <= 0 over EVERY m-window; ONE
    nonzero block in a window kills the LMI chain even without
    the terminal condition.
  Machine preconditions checked EXACTLY per world: every
  transition class carries >= 2 distinct b values AND some
  m-window has sum b^2 > 0 => INFEASIBLE stamped with the
  loudest window as witness (the blocks that blow the LMI).
  Belt + braces: a sealed deterministic PSD grid (const class,
  5 x 7 x 6 points) finds 0 LMI-feasible points on w9 (+ kz15
  in full mode).  Scope: 42 rungs + 2 mains + EPSTEIN +
  SCRAMBLE; SMOOTH census-only (self-aliased anchor, near-zero
  blocks, printed).
  RICCATI CLASS (source-dependent memory): backward equality
  chain P_J = E11, P_j = T_j^T P_{j+1} T_j + C_j^T C_j; closed
  form verified EXACTLY: P_j = v_j v_j^T + diag(0, d_j) with
  v_j = (1, c_j), c_j = sum_{i>=j} b_i the EXACT SIGNED TAIL
  SUM, d_j = sum_{i>=j} b_i^2; budget E_w = Z^2 + sum b_j^2
  EXACTLY (identity gated).  The rank-1 forcing (a rank-1
  difference with equal (1,1) corners admits NO slack: any
  admissible memory must carry the exact tail sums) is
  DEMONSTRATED by must-fail m1.
(b2) CERTIFICATION TABLE (typed by the LEG C detectors -- a
  flagged memory certifies NOTHING): budget vs 5/7 on all 42
  rungs + the 7 exceptions + kz15 detail; consistency
  margin_book <= margin_true (+ ward floor) gated.
(b3) N-SCALING: sp(N, sqrt(E_w)/M) + halves log-slope (r272
  estimator); the block-energy trend sp(N, sqrt(sum b^2)/M)
  alongside.
(b4) CONTROL FAILURE: EPSTEIN/SCRAMBLE/SMOOTH budgets; sealed
  rule: KYP_TOO_FRIENDLY iff an admitted memory certifies the
  EPSTEIN terminal budget (the world whose wall kips AT THE
  TERMINAL, |q| ~ 1.51 > 1, r260 record); the SCRAMBLE budget
  outcome is recorded as the friendliness-signature census (its
  wall kips in the chain INTERIOR at degree 21 -- structurally
  invisible to a terminal block system, reported honestly);
  SMOOTH anchor (alias <= 1e-12, q_N <= 1e-20).

LEG C -- DETECTORS + HONESTY:
(c1) TARGET-INVERSE FINGERPRINT (r266 style): sp of the budget
  margin against the true margin over the 42 rungs (bar 0.9)
  PLUS the identity c_0 == sum b_j == R exact; sealed rule:
  KYP_IS_TARGET_INVERSE iff both hold -- the memory's second
  coordinate IS the inverted terminal readout (the Schur-
  complement value the reviewer no-go names).
(c2) WALL CONSUMPTION: the Riccati memory exists PSD on every
  world INCLUDING the flipped controls -- existence is world-
  blind, no wall positivity consumed (reported; a memory whose
  existence needed the wall would be flagged).
(c3) CURRENCY TYPING (r273 tie-in): the generic root-scale l^2
  repackaging bound_gen = |Z_loc| + sqrt(J sum b^2) obeys
  bound_gen >= |Z_loc| + sum|b_j| (QM-AM) -- the naive l^2
  currency can NEVER beat the sealed l^1 pairing on the same
  decomposition data (overhead log10(sqrt(J sum b^2) /
  sum|b_j|) >= 0 gated + measured in decades; generic-baseline
  certification census printed).  What a quadratic energy would
  have to catch is the COVARIANCE (off-diagonal G) -- and the
  KYP route to it is adjudicated by (c1).

MUST-FAILS (each loud): (m1) TAIL-SUM PERTURBATION: c_{j0} ->
c_{j0} + 1/1000 at j0 = J//2 breaks the exact KYP LMI loudly
(det = -eps^2 = -1e-6 < 0; the honest floor is exact 0) -- the
memory coordinate is FORCED, no slack; (m2) GIFT MEMORY: a
builder oriented by the withheld terminal drive key must be
FLAGGED by the AST scope audit (the sealed builders audit
clean); (m3) HALVES-SHUFFLE (seed 275): the permuted eps series
loses the r272 +0.67 trend (|sp| < 0.5 and < the true sp).

STOP LIST (respected): no new pair hierarchies, no splits, no
s-flows, no packet invariants, no precision escalation (no mp
wards this round -- measurement quality is carried by the
contribution ward + the r272 reproduction wards, disclosed).

INDEX FIREWALL (binding, r238-r273 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree, j = block index; ground
truth (branch labels, the true R/t/Z values, margins) enters
GATES and census tables only; the sealed memory builders consume
(blocks, boundary condition) ONLY (AST scope audit); no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r269 PBB.mask_edge + PBB.runs_split + PBB.bound_
pairsum, r271 UPT.bound_level2, r272 L2A.halves_slope +
L2A.halves_med, r244 BH.wpack + BH.spearman, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN); TB
bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls; DEEP_N 400;
EXACT_BAR 0 (rational identities); CLASSES (1, 2, 4) + RICCATI;
E11 = diag(1, 0) terminal; PERT_EPS = 1/1000; PERT_MIN 1e-9;
FP_BAR 0.9; QM_BAR -1e-12; CONS_BAR 1e-6 (margin consistency
float slack); GRID_P11 (0, 1e-4, 1e-2, 1, 100); GRID_P12 (-10,
-1, -1/10, 0, 1/10, 1, 10); GRID_P22 (0, 1/100, 5/7, 1, 10,
100); R272_SP_EPS +0.67 tol 0.05; RESERVE_BAND (0.020, 0.035);
KZ_ANCHOR 15; SHUFFLE_SEED 275; SHUF_BAR 0.5; LOUD 1e3; runtime
<= 1800 s; smoke = w9 + controls + toy + scope audits +
bookkeeping + obstruction (w9/EPST/SCR) + grid (w9) + Riccati
exact (w9 + controls) + m1 + m2 (ladder, r272 wards,
certification, trends, fingerprint, m3 skipped).  DISCLOSED
PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r260/r263/r269/r271/r272 RECORD number
adopted as-is; the o1/o2 obstruction lemma and the Riccati
closed form are pre-run paper algebra (structural, no data);
scipy 1.17.1 is PRESENT in the venv but UNUSED -- the sealed
method is exact rational obstruction + deterministic grid +
closed-form Riccati (the LMI dimension is 2, no SDP needed).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  BLOCK_STATE_EXACT(dim 2, drive-in-transfer, level-2 blocks
    offset 0 + odd tail)
+ KYP_CONST + KYP_EVENODD + KYP_PERIOD4 (each: INFEASIBLE(o1 +
    o2, witness window) / EXISTS(cert k/42))
+ KYP_RICCATI(EXISTS_EXACT, budget = Z^2 + sum b^2,
    FORCED_TAILSUM)
+ [exactly one head] KYP_MEMORY_GO(class, cert 42/42 + 7/7,
    N-trend, control failure at the flips) / KYP_PARTIAL(class,
    n/42, break anatomy) / KYP_INFEASIBLE(uniform classes,
    o1 + o2 anatomy) / KYP_TOO_FRIENDLY(EPST certified)
+ [if fired] KYP_IS_TARGET_INVERSE(fingerprint sp, c_0 == R)
+ N_TREND(sp(N, bound/M), halves; block energy trend)
+ CONTROL_CENSUS(EPST / SCR / SMOOTH budget outcomes)
+ CURRENCY_READING(QM-AM overhead med dec, generic-baseline
    census).
Honesty before beauty: no verdict claims a cofinal law, an
asymptotic mechanism or H5 progress; every trend and census is
MEASURED on the 42 rungs only; a detector-flagged memory
certifies NOTHING; the exception scalar's positivity beyond the
measured 42 stays OPEN; r243-r273 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 was 22/24 -- the TOY guard demanded J >= 2m + 1
where the obstruction needs only two occurrences per class
(J >= 2m); disclosed CALIBRATION AMENDMENT a1: guard J < 2m + 1
-> J < 2m (implementation only, real worlds have J >= 28, no
bar, band, rule or verdict rule moved); smoke then 24/24;
calibration pass 1 = first full evaluation, 24/24 gates, wall
7.6 s; pass 2 = the record run, identical to pass 1 in every
printed FIGURE up to WALL (one prose correction between the
passes: the G61 detail text had hardcoded a wrong decade range,
replaced by the measured-value phrasing -- no figure, bar or
rule involved); the only post-freeze edit is this record-table
insertion, which IS the protocol):
CAL_VERDICT = BLOCK_STATE_EXACT(dim 2, drive-in-transfer,
level-2 blocks offset 0 + odd tail) + KYP_CONST:INFEASIBLE(o1 +
o2) + KYP_EVENODD:INFEASIBLE(o1 + o2) + KYP_PERIOD4:INFEASIBLE(
o1 + o2) + KYP_RICCATI(EXISTS_EXACT, budget = Z^2 + sum b^2,
FORCED_TAILSUM) + KYP_INFEASIBLE(uniform classes, o1 fiber
forcing + o2 descent on 46/46 worlds) + KYP_IS_TARGET_INVERSE(
fingerprint sp +1.00, c_0 == R exact) + N_TREND(sp(N, bound/M)
-0.36, halves -0.235; energy sp -0.69) + CONTROL_CENSUS(EPST
FAIL 1.291 >= 5/7; SCR CERTIFIED 0.221 < 5/7 -- friendliness
signature; SMOOTH trivial 6.1e-5) + CURRENCY_READING(QM-AM
overhead med +0.15 dec, generic census 8/42).
Key numbers.  LEG A: 42 rungs N in [142, 878] POSITIVE_PREFIX
42/42, controls flip 25/21/27 re-derived; branch census cheap 35
+ the named 7 EXACT; bookkeeping ward acc_J vs Z worst
dev/absmass 2.1e-13 main / 3.9e-13 deep / 2.4e-8 controls (bars
1e-9/3e-6/1e-6); exact rational identity acc_J == Z_loc + sum b
dev 0 on 47/47 worlds; block counts J med 71 (min 28, max 169);
r272 wards sp(N, eps) +0.67 (record +0.67 tol 0.05), kz15
reserve 0.0268 in [0.020, 0.035].  LEG B (b1): o1 + o2 verified
EXACTLY on 46/46 worlds x 3 classes (every transition class >= 2
distinct b at m = 1, 2, 4; every world's loudest m-window sum
b^2 > 0; loudest witnesses kz9 j=4: 5.5e-2 / 8.6e-2 / 1.2e-1 at
m = 1/2/4) => CONST / EVENODD / PERIOD4 all INFEASIBLE (double
kill: p11 = 0 vs terminal usefulness AND descent windows); grid
refutation 84 PSD points each on w9 + kz15, 0 LMI-feasible;
SMOOTH census: J = 37, max |b| 7.5e-3, worst 1-window 5.7e-5 > 0
=> o2 holds even on the trivial anchor (the obstruction is
scale-free, structural).  RICCATI: KYP equality + PSD + terminal
E11 + budget identity E == Z_book^2 + sum b^2 EXACT (dev 0) on
47/47 worlds incl flipped controls (existence world-blind, c2
wall detector SILENT).  (b2) certification (typed TARGET_
INVERSE-FLAGGED, no certificate): budget < 5/7 exact on 42/42
rungs and 7/7 exceptions (exception sum b^2 4.1e-3..1.1e-2);
kz15 detail: |Z| 0.8184, margin_true 0.0268, sum b^2 9.34e-3 =
0.2094 of the M^2 slack 0.0446, bound 0.8240, margin_book
+0.0211; consistency margin_book <= margin_true on 42/42.  (b3)
sp(N, bound/M) -0.36, halves slope -0.235 (the budget scales
the 'right' way -- but it is the target inverse: bound/M tracks
|Z|/M, sp(N, |Z|/M) -0.36); energy trend sp(N, sqrt(sum b^2)/M)
-0.69, halves med 0.0936 -> 0.0784 (the block energy deepens
with N, consistent with the r272 truth decay).  (b4) EPST
budget 1.291 >= 5/7 FAIL exactly at the world whose wall kips
at the terminal (|q| = 1.51 > 1; Z^2 1.078 + energy 0.213); SCR
budget 0.221 < 5/7 CERTIFIED (Z^2 0.193 + 0.028) -- the
friendliness signature: the inverse memory 'certifies' a
broken-arithmetic world because it reads the answer (SCR's wall
kips at interior degree 21, invisible to the terminal block
system); SMOOTH alias 2.4e-14, q_N 4.2e-25, budget 6.1e-5
trivial.  LEG C: (c1) fingerprint sp(margin_book, margin_true)
= +1.00 >= 0.9 AND c_0 == R exact on 47/47 =>
KYP_IS_TARGET_INVERSE stamped (the sealed reviewer no-go: the
memory IS the inverted terminal readout); (c3) QM-AM overhead
med +0.15 dec (min +0.11, max +0.26, all >= 0): the generic
root-scale l^2 repackaging is 0.11-0.26 decades COARSER than
the sealed l^1 pairing on every world; generic-baseline census
8/42 certified (bound_gen = |Z_loc| + sqrt(J sum b^2) -- the
root-scale l^2 without covariance certifies only a fifth of
what the l^1 pairing reaches).  MUST-FAILS: m1 tail
perturbation at j0 = 17 on w9 breaks the LMI det by -1.0e-6
(floor exact 0, loud); m2 gift builder FLAGGED (withheld key in
scope), sealed builders CLEAN, fragment audit CLEAN; m3
seed-275 shuffle |sp| 0.196 < 0.5 < +0.67.  READING (typed, no
upgrade): the l^1 -> l^2 currency reform DOES NOT CARRY in
state-space/KYP form -- the round closes the reviewer's track 2
with a two-sided no-go: (i) every uniform quadratic memory
(constant, even/odd, period 4) over the exact block bookkeeping
is INFEASIBLE by structural algebra (the homogenization fiber
forces p11 = 0, killing terminal usefulness; the descent
windows kill the LMI chain outright -- machine-verified exactly
on every world including the trivial SMOOTH anchor: this is not
a cancellation issue but a structure theorem about additive
accumulation of sign-free drives); (ii) the unique admissible
source-dependent memory (the backward Riccati) is FORCED to
carry the exact signed tail sums c_j -- its budget is Z^2 +
sum b^2, the inverted terminal readout itself (fingerprint
+1.00; it 'certifies' SCRAMBLE); and (iii) the naive generic
l^2 energy is QM-AM-coarser than the sealed l^1 pairing on
every world (med +0.15 dec) and certifies only 8/42.  The
covariance that a quadratic form would need is exactly what
r273 typed GENERIC -- per-window data, not source law:
quadratic storage without a sign/covariance law either dies
(uniform) or reads the answer (Riccati).  The open edges after
this round are unchanged: the kz15 razor at 0.12 dec (r269) and
the cofinal step; the L2 task keeps its r272 address
(non-adjacent/global mechanism, delta' > 0.21) -- with the
state-space vehicle now excluded alongside l^1 refinement.
Runtime 7.6 s full / 0.2 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (a1 and the G61 prose
correction predate the record run, disclosed above; records
inserted per protocol; no bar, band, rule or verdict rule
moved).

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
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import universal_pair_theorem_probe as UPT     # noqa: E402 r271
import l2_scaling_anatomy_probe as L2A         # noqa: E402 r272
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
B57_FR = Fraction(5, 7)
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
EDGE_F = 0.20
PAIR_OFFSET = 0
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
CLASSES = (1, 2, 4)
CLASS_NAMES = {1: "KYP_CONST", 2: "KYP_EVENODD", 4: "KYP_PERIOD4"}
PERT_EPS = Fraction(1, 1000)
PERT_MIN = 1e-9
FP_BAR = 0.9
QM_BAR = -1e-12
CONS_BAR = 1e-6
GRID_P11 = (Fraction(0), Fraction(1, 10000), Fraction(1, 100),
            Fraction(1), Fraction(100))
GRID_P12 = (Fraction(-10), Fraction(-1), Fraction(-1, 10),
            Fraction(0), Fraction(1, 10), Fraction(1), Fraction(10))
GRID_P22 = (Fraction(0), Fraction(1, 100), Fraction(5, 7),
            Fraction(1), Fraction(10), Fraction(100))
R272_SP_EPS = 0.67
R272_SP_TOL = 0.05
RESERVE_BAND = (0.020, 0.035)
KZ_ANCHOR = 15
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
SHUFFLE_SEED = 275
SHUF_BAR = 0.5
LOUD = 1e3

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
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z, margins) enters gates "
                       "and census tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
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


# ---- sealed builders (target-blind: consume blocks + the fixed
# boundary condition ONLY; the withheld terminal drive key and
# every target-side identifier are forbidden in scope, AST-audit)
def blocks_from_runs(sruns):
    """SEALED BLOCK CONVENTION (r270/r272, offset 0): level-2
    blocks b_j = s_{2j} + s_{2j+1} over the bx-sorted bulk sign
    runs; the odd tail run is its own final block."""
    m = len(sruns)
    bl = [sruns[i] + sruns[i + 1]
          for i in range(PAIR_OFFSET, m - 1, 2)]
    if (m - PAIR_OFFSET) % 2 == 1:
        bl.append(sruns[-1])
    return bl


def state_chain(zloc, bl):
    """LEG A sealed realization: x_j = (acc_j, 1), acc_0 = zloc;
    T_j = [[1, b_j], [0, 1]] exact; readout C_j = (0, b_j).
    Returns (acc_J float, acc_J exact Fraction)."""
    acc = zloc
    acc_fr = Fraction(zloc)
    for b in bl:
        acc = acc + b
        acc_fr = acc_fr + Fraction(b)
    return acc, acc_fr


def kyp_lmi(P, Pn, b):
    """exact entries of M = T^T Pn T - P + C^T C for the sealed
    realization (T = [[1, b], [0, 1]], C = (0, b)); Fractions."""
    p11, p12, p22 = P
    q11, q12, q22 = Pn
    bf = Fraction(b)
    m11 = q11 - p11
    m12 = q11 * bf + q12 - p12
    m22 = q11 * bf * bf + 2 * q12 * bf + q22 - p22 + bf * bf
    return m11, m12, m22


def is_nsd(m11, m12, m22):
    return m11 <= 0 and m22 <= 0 and m11 * m22 - m12 * m12 >= 0


def is_psd(P):
    p11, p12, p22 = P
    return p11 >= 0 and p22 >= 0 and p11 * p22 - p12 * p12 >= 0


def class_obstruction(bl, m):
    """EXACT INFEASIBILITY CERTIFICATE for the uniform memory
    class of period m (o1 fiber forcing + o2 descent windows);
    all comparisons in exact rational arithmetic on the dyadic
    float blocks.  Returns dict(proved, dis_ok, worst, wit)."""
    J = len(bl)
    if J < 2 * m:
        return dict(proved=False, dis_ok=False, worst=Fraction(0),
                    wit=-1, short=True)
    dis_ok = True
    for r_ in range(m):
        vals = {Fraction(bl[j]) for j in range(r_, J, m)}
        if len(vals) < 2:
            dis_ok = False
    worst = Fraction(0)
    wit = -1
    for i in range(0, J - m + 1):
        s = Fraction(0)
        for j in range(i, i + m):
            bf = Fraction(bl[j])
            s += bf * bf
        if s > worst:
            worst = s
            wit = i
    return dict(proved=bool(dis_ok and worst > 0), dis_ok=dis_ok,
                worst=worst, wit=wit, short=False)


def grid_refute_const(bl):
    """belt + braces: sealed deterministic PSD grid for the const
    class; counts LMI-feasible points (expected 0; exact)."""
    n_psd = 0
    n_feas = 0
    for p11 in GRID_P11:
        for p12 in GRID_P12:
            for p22 in GRID_P22:
                P = (p11, p12, p22)
                if not is_psd(P):
                    continue
                n_psd += 1
                ok = True
                for b in bl:
                    if not is_nsd(*kyp_lmi(P, P, b)):
                        ok = False
                        break
                if ok:
                    n_feas += 1
    return n_psd, n_feas


def riccati_memory(bl):
    """class-4 backward Riccati memory (EQUALITY KYP, the
    tightest admissible chain): P_J = E11 = diag(1, 0); P_j =
    T_j^T P_{j+1} T_j + C_j^T C_j.  Closed form P_j = v_j v_j^T
    + diag(0, d_j), v_j = (1, c_j), c_j = sum_{i>=j} b_i, d_j =
    sum_{i>=j} b_i^2 -- exact dyadic rationals."""
    c = Fraction(0)
    d = Fraction(0)
    cs = [c]
    ds = [d]
    for b in reversed(bl):
        bf = Fraction(b)
        c = bf + c
        d = bf * bf + d
        cs.append(c)
        ds.append(d)
    cs.reverse()
    ds.reverse()
    Ps = [(Fraction(1), cs[j], cs[j] * cs[j] + ds[j])
          for j in range(len(bl) + 1)]
    return Ps, cs, ds


def mutant_gift_memory(rc, bl):
    """m2 MUST-FAIL MUTANT: a memory builder oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    Ps, cs, ds = riccati_memory([s * b for b in bl])
    return Ps


MEM_FORBIDDEN = {"t" + "_term", "rho", "S", "sa", "la",
                 "q" + "_chain", "wb", "world" + "_block",
                 "direct" + "_terminal", "M" + "_W", "margin",
                 "Zl", "Z", "R" + "_bulk", "g" + "_gap", "q_N"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    target-side identifier or dict key from the sealed set."""
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


# ------------------------------------------------ toy exact tool
def toy_kyp_exact():
    """hand-checked block sequence bl = (3, -1, 2, -2, 1, -3, 4,
    1), zloc = 1/2: obstruction preconditions hold at m = 1, 2,
    4; Riccati gives c_0 = 5, sum b^2 = 45, Z = 11/2, E = 121/4
    + 45 = 301/4 -- all identities EXACT (Fraction ==)."""
    bl = [3.0, -1.0, 2.0, -2.0, 1.0, -3.0, 4.0, 1.0]
    zl = 0.5
    ok = True
    for m in CLASSES:
        ob = class_obstruction(bl, m)
        ok = ok and ob["proved"]
    ok = ok and class_obstruction(bl, 1)["worst"] == Fraction(16)
    acc, acc_fr = state_chain(zl, bl)
    ok = ok and acc_fr == Fraction(11, 2)
    Ps, cs, ds = riccati_memory(bl)
    ok = ok and cs[0] == Fraction(5) and ds[0] == Fraction(45)
    for j in range(len(bl)):
        m11, m12, m22 = kyp_lmi(Ps[j], Ps[j + 1], bl[j])
        ok = ok and m11 == 0 and m12 == 0 and m22 == 0
        ok = ok and is_psd(Ps[j])
    ok = ok and Ps[-1] == (Fraction(1), Fraction(0), Fraction(0))
    zf = Fraction(zl)
    E = Ps[0][0] * zf * zf + 2 * Ps[0][1] * zf + Ps[0][2]
    ok = ok and E == Fraction(301, 4)
    ok = ok and E == acc_fr * acc_fr + Fraction(45)
    # m1 on the toy: perturb c_3 -> LMI det goes negative exactly
    j0 = 3
    cp = cs[j0] + PERT_EPS
    Pp = (Fraction(1), cp, cp * cp + ds[j0])
    m11, m12, m22 = kyp_lmi(Pp, Ps[j0 + 1], bl[j0])
    det = m11 * m22 - m12 * m12
    ok = ok and det == -(PERT_EPS * PERT_EPS)
    return ok


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("kyp_memory_probe -- PRIME.PORT.COUPLEDTAU."
          "KYP_MEMORY.01 (round 275)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   R272_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], L2A.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + scope "
                        "audits + bookkeeping + obstruction + "
                        "grid + Riccati + m1/m2; ladder, r272 "
                        "wards, certification, trends, "
                        "fingerprint, m3 skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER TRACK 2 (pre-authorized): the l^1 -> l^2 "
          "currency reform as a KYP MEMORY over the exact block "
          "state system x_j = (acc, 1), T_j = [[1, b_j], [0, 1]], "
          "C_j = (0, b_j); test sequence BINDING: constant -> "
          "even/odd -> period 4 -> Riccati; existence gates are "
          "EXACT rational (obstruction lemma o1 + o2 pre-derived "
          "on paper, closed-form Riccati); certification would "
          "be E_w < 5/7 exact; anti-circularity: builders "
          "consume blocks + boundary condition only, controls "
          "must fail at their flips; detectors: target-inverse "
          "fingerprint (bar %.1f) + wall consumption + QM-AM "
          "currency typing; ALL bars, rules and verdicts sealed "
          "BEFORE evaluation (pre-spec input = r260/r263/r269/"
          "r271/r272 record numbers + pre-run paper algebra, "
          "disclosed; scipy present but UNUSED)" % FP_BAR)

    # ---------------- S1: census + controls (r269/r272 scaffold)
    section("S1  CENSUS + CONTROLS")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        chain = ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
        Z = t[N - 2] + chain
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx,
                    o=o, lo=lo, hi=hi, p=p)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g"] >= 0.0]
    exc = [rc for rc in recs if rc["g"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g"] >= 0 else "EXCEPTION",
                 recs[0]["g"]))
    else:
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g"])
                           for rc in mrecs)))

    # ---------------- S2: LEG A -- decomposition + bookkeeping
    section("S2  LEG A -- EXACT DECOMPOSITION + BLOCK BOOKKEEPING")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ctrl = 0.0

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        t_loc = float(np.sum(cts[ed]))
        cb = cts[~ed]
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        bl = blocks_from_runs(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        e_l2 = UPT.bound_level2(Sr)
        Zl = t_loc + rc["chain"]
        return dict(nb=int(len(cb)), Mr=Mr, Sr=Sr, bl=bl,
                    e_c2=e_c2, e_l2=e_l2, t_loc=t_loc, Zl=Zl)

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    book_exact_ok = True

    def book_dev(rc):
        """gate-side bookkeeping check: run the (T_j, C_j) chain
        and compare acc_J against Z (float, ward floors) and
        against the exact rational identity (dev 0)."""
        ev = rc["ev"]
        acc, acc_fr = state_chain(ev["Zl"], ev["bl"])
        rc["acc"] = acc
        rc["acc_fr"] = acc_fr
        rc["absum"] = float(np.sum(np.abs(rc["ct"])))
        ref = Fraction(ev["Zl"])
        for b in ev["bl"]:
            ref += Fraction(b)
        dev = abs(acc - rc["Z"]) / max(rc["absum"], 1e-300)
        return dev, (acc_fr == ref)

    for rc in all_rc:
        dev, ex_ok = book_dev(rc)
        book_exact_ok = book_exact_ok and ex_ok
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for c in crecs:
        dev, ex_ok = book_dev(crecs[c])
        book_exact_ok = book_exact_ok and ex_ok
        tb_ctrl = max(tb_ctrl, dev)
    Js = [len(rc["ev"]["bl"]) for rc in all_rc]
    check("G20-bookkeeping-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL and book_exact_ok,
          "the (T_j, C_j) chain reproduces Z on %d rungs + %d "
          "mains + 3 controls: acc_J vs Z worst dev/absmass "
          "%.1e main N<=%d (bar %.0e) / %.1e deep (bar %.0e) / "
          "%.1e controls (bar %.0e); EXACT rational identity "
          "acc_J == Z_loc + sum b_j dev 0 on every world (%s); "
          "block counts J med %d (min %d, max %d) -- the state "
          "system is pure exact bookkeeping"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL,
             "OK" if book_exact_ok else "BROKEN",
             int(np.median(Js)), min(Js), max(Js)))

    Ns = [rc["N"] for rc in recs]
    eps_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
    if not smoke:
        sp_eps = BH.spearman(Ns, eps_rel)
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        check("G21-r272-reproduction-wards",
              abs(sp_eps - R272_SP_EPS) <= R272_SP_TOL and ok15,
              "sp(N, eps) %+.2f (record %+.2f, tol %.2f); kz15 "
              "true reserve %.4f in %s -- the r272 scaffold is "
              "reproduced on this rebuild"
              % (sp_eps, R272_SP_EPS, R272_SP_TOL, slack15,
                 str(RESERVE_BAND)))
    else:
        sp_eps = float("nan")
        check("G21-r272-reproduction-wards", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---------------- S3: toy exactness + scope audits
    section("S3  TOY EXACTNESS + SCOPE AUDITS")
    check("G30-toy-exactness", toy_kyp_exact(),
          "hand-checked blocks (3, -1, 2, -2, 1, -3, 4, 1), "
          "zloc = 1/2: obstruction preconditions PROVED at m = "
          "1, 2, 4 (worst 1-window 16); acc_J == 11/2; Riccati "
          "c_0 = 5, sum b^2 = 45, KYP EQUALITY + PSD + terminal "
          "E11 exact, E == 301/4 == Z^2 + sum b^2; m1 toy "
          "perturbation det == -eps^2 exactly -- all Fraction ==")
    h_bl = scope_audit("blocks_from_runs", MEM_FORBIDDEN)
    h_sc = scope_audit("state_chain", MEM_FORBIDDEN)
    h_ky = scope_audit("kyp_lmi", MEM_FORBIDDEN)
    h_ob = scope_audit("class_obstruction", MEM_FORBIDDEN)
    h_ri = scope_audit("riccati_memory", MEM_FORBIDDEN)
    h_gr = scope_audit("grid_refute_const", MEM_FORBIDDEN)
    h_m2 = scope_audit("mutant_gift_memory", MEM_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_bl or h_sc or h_ky or h_ob or h_ri or h_gr)
    check("G31-scope-audits", clean and bool(h_m2)
          and not ag_hits,
          "sealed builders CLEAN (blocks/state/KYP/obstruction/"
          "Riccati/grid consume blocks + boundary condition "
          "only%s); m2 gift-memory mutant FLAGGED (%s); fragment "
          "audit (no fit primitives): %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_m2) if h_m2 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: LEG B -- the KYP class ladder
    section("S4  LEG B -- THE KYP CLASS LADDER (EXACT)")
    ob_pool = all_rc + [crecs[c] for c in ("EPST", "SCR")]
    ob_ok = {m: True for m in CLASSES}
    ob_note = {}
    for m in CLASSES:
        worst_w = None
        for rc in ob_pool:
            ob = class_obstruction(rc["ev"]["bl"], m)
            if not ob["proved"]:
                ob_ok[m] = False
            if worst_w is None or ob["worst"] > worst_w[1]:
                worst_w = (rc.get("kz", -1), ob["worst"],
                           ob["wit"])
        ob_note[m] = worst_w
    rc9 = mrecs[0] if smoke else next(
        r_ for r_ in recs + mrecs if r_["kz"] == 9)
    ob9 = class_obstruction(rc9["ev"]["bl"], 1)
    for m, gate in ((1, "G40-const-infeasible"),
                    (2, "G41-evenodd-infeasible"),
                    (4, "G42-period4-infeasible")):
        check(gate, ob_ok[m],
              "%s (period %d) INFEASIBLE on %d/%d worlds by the "
              "EXACT obstruction: o1 fiber forcing (every "
              "transition class >= 2 distinct b => p11 = 0, "
              "p12 = 0 -- terminal usefulness p11 >= 1 dead) + "
              "o2 descent (every world has an m-window with sum "
              "b^2 > 0; loudest witness kz%s j=%d sum b^2 "
              "%.1e) -- ONE nonzero block per window kills the "
              "LMI chain even without the terminal condition"
              % (CLASS_NAMES[m], m, len(ob_pool), len(ob_pool),
                 str(ob_note[m][0]), ob_note[m][2],
                 float(ob_note[m][1])))
    grid_pool = [rc9]
    if not smoke:
        grid_pool.append(next(r_ for r_ in recs
                              if r_["kz"] == KZ_ANCHOR))
    g_note = []
    g_ok = True
    for rc in grid_pool:
        n_psd, n_feas = grid_refute_const(rc["ev"]["bl"])
        g_ok = g_ok and (n_feas == 0)
        g_note.append("kz%d %d PSD pts, %d feasible"
                      % (rc["kz"], n_psd, n_feas))
    check("G43-grid-refutation", g_ok,
          "belt + braces (sealed deterministic grid, const "
          "class, exact rational LMI checks): %s -- the numeric "
          "search finds NO feasible point, consistent with the "
          "exact obstruction" % "; ".join(g_note))
    # SMOOTH census (anchor, census-only)
    blS = crecs["SMOOTH"]["ev"]["bl"]
    obS = class_obstruction(blS, 1)
    maxbS = max((abs(b) for b in blS), default=0.0)
    info("SMOOTH census: J = %d, max |b| = %.1e, o2 worst "
         "1-window %.1e (> 0: the obstruction is scale-free -- "
         "it holds even on the trivial anchor)"
         % (len(blS), maxbS, float(obS["worst"])))

    # Riccati class on every world (incl controls)
    ric_ok = True
    ric_world_note = []
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        Ps, cs, ds = riccati_memory(ev["bl"])
        okw = Ps[-1] == (Fraction(1), Fraction(0), Fraction(0))
        for j in range(len(ev["bl"])):
            m11, m12, m22 = kyp_lmi(Ps[j], Ps[j + 1],
                                    ev["bl"][j])
            okw = okw and m11 == 0 and m12 == 0 and m22 == 0
            okw = okw and is_psd(Ps[j])
        zf = Fraction(ev["Zl"])
        E = Ps[0][0] * zf * zf + 2 * Ps[0][1] * zf + Ps[0][2]
        okw = okw and (E == rc["acc_fr"] * rc["acc_fr"] + ds[0])
        okw = okw and (E >= rc["acc_fr"] * rc["acc_fr"])
        rc["E_fr"] = E
        rc["c0_fr"] = cs[0]
        rc["sumsq_fr"] = ds[0]
        ric_ok = ric_ok and okw
    for c in crecs:
        rc = crecs[c]
        ric_world_note.append("%s E %.4f (Z^2 %.4f + sumsq "
                              "%.1e)"
                              % (c, float(rc["E_fr"]),
                                 float(rc["acc_fr"]) ** 2,
                                 float(rc["sumsq_fr"])))
    check("G44-riccati-exact", ric_ok,
          "RICCATI memory on %d worlds (42 + mains + 3 controls "
          "in full mode): KYP EQUALITY exact (all LMI entries "
          "== 0), PSD at every j, terminal == E11, budget "
          "identity E == Z_book^2 + sum b^2 EXACT, telescope "
          "E >= Z_book^2 -- existence is WORLD-BLIND (holds on "
          "the flipped controls too: the c2 wall detector is "
          "SILENT, no wall positivity consumed); %s"
          % (len(all_rc) + len(crecs),
             "; ".join(ric_world_note)))

    # ---------------- S5: certification + trends + controls
    section("S5  CERTIFICATION (TYPED) + N-TREND + CONTROLS")
    if not smoke:
        cert42 = 0
        cons_ok = True
        bound_rel = []
        en_rel = []
        mt_rel = []
        mb_rel = []
        for rc in recs:
            E = rc["E_fr"]
            certw = E < B57_FR
            if certw:
                cert42 += 1
            bound = math.sqrt(float(E))
            bound_rel.append(bound / M_W)
            en_rel.append(math.sqrt(float(rc["sumsq_fr"])) / M_W)
            mtrue = M_W - abs(rc["Z"])
            mbook = M_W - bound
            mt_rel.append(mtrue)
            mb_rel.append(mbook)
            cons_ok = cons_ok and (mbook <= mtrue + CONS_BAR)
        cert_exc = 0
        for rc in sorted(exc, key=lambda r_: r_["kz"]):
            E = rc["E_fr"]
            certw = E < B57_FR
            if certw:
                cert_exc += 1
            bound = math.sqrt(float(E))
            info("kz%-3d N%-4d EXC |Z| %.4f margin_true %+.4f  "
                 "sum b^2 %.1e  bound %.4f margin_book %+.4f %s"
                 % (rc["kz"], rc["N"], abs(rc["Z"]),
                    M_W - abs(rc["Z"]), float(rc["sumsq_fr"]),
                    bound, M_W - bound,
                    "CERT*" if certw else "MISS"))
        check("G50-certification-table", cons_ok,
              "TYPED TABLE (the memory is detector-adjudicated "
              "below -- a flagged memory certifies NOTHING; the "
              "star on CERT* marks the flag): budget < 5/7 "
              "(exact rational) on %d/42 rungs, %d/7 exceptions; "
              "consistency margin_book <= margin_true (+ %.0e) "
              "on 42/42 (%s)"
              % (cert42, cert_exc, CONS_BAR,
                 "OK" if cons_ok else "BROKEN"))
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        sl15 = B57_FR - rc15["acc_fr"] * rc15["acc_fr"]
        check("G51-kz15-detail", True,
              "kz15 (N %d, the razor): |Z| %.4f, margin_true "
              "%.4f; block energy sum b^2 %.2e = %.4f of the "
              "M^2 slack %.4f; bound %.4f, margin_book %+.4f"
              % (rc15["N"], abs(rc15["Z"]),
                 M_W - abs(rc15["Z"]),
                 float(rc15["sumsq_fr"]),
                 float(rc15["sumsq_fr"]) / float(sl15),
                 float(sl15), math.sqrt(float(rc15["E_fr"])),
                 M_W - math.sqrt(float(rc15["E_fr"]))))
        sp_b = BH.spearman(Ns, bound_rel)
        sl_b = L2A.halves_slope(Ns, bound_rel)
        sp_e = BH.spearman(Ns, en_rel)
        z_rel = [abs(rc["Z"]) / M_W for rc in recs]
        sp_z = BH.spearman(Ns, z_rel)
        check("G52-n-scaling", True,
              "b3 MEASUREMENT: sp(N, bound/M) %+.2f, halves "
              "log-slope %+.3f (falls with N -- the 'right' "
              "direction, but see the LEG C typing: bound/M "
              "tracks |Z|/M, sp(N, |Z|/M) %+.2f); block energy "
              "trend sp(N, sqrt(sum b^2)/M) %+.2f, halves med "
              "%.4g -> %.4g"
              % (sp_b, sl_b, sp_z, sp_e,
                 L2A.halves_med(en_rel)[0],
                 L2A.halves_med(en_rel)[1]))
    else:
        sp_b = sl_b = sp_e = float("nan")
        cert42 = cert_exc = -1
        check("G50-certification-table", True, "SMOKE: skipped")
        check("G51-kz15-detail", True, "SMOKE: skipped")
        check("G52-n-scaling", True, "SMOKE: skipped")

    # m1: tail-sum perturbation must break the exact KYP
    rc = rc9
    ev = rc["ev"]
    Ps, cs, ds = riccati_memory(ev["bl"])
    j0 = len(ev["bl"]) // 2
    cp = cs[j0] + PERT_EPS
    Pp = (Fraction(1), cp, cp * cp + ds[j0])
    m11, m12, m22 = kyp_lmi(Pp, Ps[j0 + 1], ev["bl"][j0])
    det = m11 * m22 - m12 * m12
    broke = not is_nsd(m11, m12, m22)
    check("G53-mustfail-tail-perturbation", broke
          and abs(float(det)) >= PERT_MIN,
          "m1 FORCED MEMORY: c_{j0} + 1/1000 at j0 = %d on w9 "
          "breaks the exact KYP LMI (det = %.1e < 0; honest "
          "floor is EXACT 0, bar %.0e) -- a rank-1 difference "
          "with equal (1,1) corners admits NO slack: any "
          "admissible memory must carry the exact signed tail "
          "sums" % (j0, float(det), PERT_MIN))

    # control battery (sealed rule: TOO_FRIENDLY iff EPST cert)
    E_ep = crecs["EPST"]["E_fr"]
    E_sc = crecs["SCR"]["E_fr"]
    E_sm = crecs["SMOOTH"]["E_fr"]
    epst_fails = not (E_ep < B57_FR)
    scr_cert = E_sc < B57_FR
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    check("G54-control-battery", epst_fails
          and alias <= SM_ALIAS_BAR and abs(qS) <= SM_Q_BAR,
          "sealed rule: the memory MUST fail where the wall "
          "kips at the terminal -- EPST budget %.3f %s 5/7 "
          "(|q| = 1.51 > 1: FAILS exactly there, %s); SCR "
          "budget %.3f %s 5/7 (%s -- SCR's wall kips at "
          "INTERIOR degree 21, structurally invisible to a "
          "terminal block system: recorded as the friendliness "
          "signature for LEG C); SMOOTH anchor: alias %.1e <= "
          "%.0e, q_N %.1e <= %.0e, budget %.1e trivial"
          % (float(E_ep), ">=" if epst_fails else "<",
             "OK" if epst_fails else "TOO_FRIENDLY",
             float(E_sc), "<" if scr_cert else ">=",
             "CERTIFIED" if scr_cert else "fails",
             alias, SM_ALIAS_BAR, qS, SM_Q_BAR, float(E_sm)))

    # ---------------- S6: LEG C -- detectors + currency typing
    section("S6  LEG C -- DETECTORS + CURRENCY TYPING")
    c0_ok = True
    for rc in all_rc + [crecs[c] for c in crecs]:
        ref = Fraction(0)
        for b in rc["ev"]["bl"]:
            ref += Fraction(b)
        c0_ok = c0_ok and (rc["c0_fr"] == ref)
    if not smoke:
        sp_fp = BH.spearman(mt_rel, mb_rel)
        inverse = (sp_fp >= FP_BAR) and c0_ok
        check("G60-target-inverse-detector", c0_ok,
              "c1 FINGERPRINT: sp(margin_book, margin_true) = "
              "%+.2f (bar %.1f) over the 42 rungs AND c_0 == "
              "sum b_j == R exact on every world (%s) => %s -- "
              "the memory's second coordinate IS the inverted "
              "terminal readout (the reviewer no-go: an "
              "inverted terminal Schur-complement value); c2 "
              "wall consumption: existence world-blind (G44), "
              "detector SILENT"
              % (sp_fp, FP_BAR, "OK" if c0_ok else "BROKEN",
                 "KYP_IS_TARGET_INVERSE STAMPED" if inverse
                 else "not stamped"))
    else:
        sp_fp = float("nan")
        inverse = c0_ok
        check("G60-target-inverse-detector", c0_ok,
              "SMOKE: c_0 == R exact on w9 + controls (%s); "
              "fingerprint needs the 42-rung ladder, skipped"
              % ("OK" if c0_ok else "BROKEN"))
    qm_worst = 1e300
    qm_all = []
    for rc in all_rc:
        ev = rc["ev"]
        Jb = len(ev["bl"])
        l1 = sum(abs(b) for b in ev["bl"])
        l2r = math.sqrt(Jb * float(rc["sumsq_fr"]))
        ov = math.log10(l2r / max(l1, 1e-300))
        qm_all.append(ov)
        qm_worst = min(qm_worst, ov)
    check("G61-currency-typing", qm_worst >= QM_BAR,
          "c3 QM-AM: the generic root-scale l^2 repackaging "
          "sqrt(J sum b^2) >= sum|b_j| on EVERY world (worst "
          "overhead %+.3f dec >= %.0e): overhead med %+.2f dec "
          "(min %+.2f, max %+.2f) -- the naive l^2 currency is "
          "measurably COARSER than the sealed l^1 pairing on "
          "the same decomposition data; the quadratic gain must "
          "come from COVARIANCE (off-diagonal G), and the KYP "
          "route to it is adjudicated by the c1 detector"
          % (qm_worst, QM_BAR,
             float(np.median(qm_all)) if qm_all else float("nan"),
             min(qm_all) if qm_all else float("nan"),
             max(qm_all) if qm_all else float("nan")))
    if not smoke:
        gen_cert = 0
        for rc in recs:
            ev = rc["ev"]
            Jb = len(ev["bl"])
            bg = abs(ev["Zl"]) + math.sqrt(
                Jb * float(rc["sumsq_fr"]))
            if bg < M_W:
                gen_cert += 1
        info("generic-baseline census: bound_gen = |Z_loc| + "
             "sqrt(J sum b^2) certifies %d/42 (measured; the "
             "root-scale l^2 without covariance)" % gen_cert)
        rng = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(Ns,
                                 list(rng.permutation(eps_rel))))
        check("G62-mustfail-halves-shuffle", sp_mut < SHUF_BAR
              and sp_mut < abs(sp_eps),
              "m3 HALVES-SHUFFLE (seed-%d permutation of the "
              "eps series against the N axis): |sp| = %.3f < "
              "%.1f and < the true trend %+.2f -- the scaffold "
              "trend is carried by N, not by the machinery"
              % (SHUFFLE_SEED, sp_mut, SHUF_BAR, sp_eps))
    else:
        gen_cert = -1
        check("G62-mustfail-halves-shuffle", True,
              "SMOKE: skipped")

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact block state system with its KYP class "
          "ladder adjudicated EXACTLY (obstruction lemma + "
          "closed-form Riccati + detectors) -- NO new "
          "certificate, NO bound modification, the l^2 vehicle "
          "typed")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["BLOCK_STATE_EXACT(dim 2, drive-in-transfer, "
                 "level-2 blocks offset 0 + odd tail)"]
        uniform_dead = all(ob_ok[m] for m in CLASSES)
        for m in CLASSES:
            parts.append("%s:%s" % (CLASS_NAMES[m],
                                    "INFEASIBLE(o1 + o2)"
                                    if ob_ok[m] else "OPEN"))
        parts.append("KYP_RICCATI(EXISTS_EXACT, budget = Z^2 + "
                     "sum b^2, FORCED_TAILSUM)")
        if uniform_dead:
            parts.append("KYP_INFEASIBLE(uniform classes, o1 "
                         "fiber forcing + o2 descent on %d/%d "
                         "worlds)" % (len(ob_pool), len(ob_pool)))
        if not epst_fails:
            parts.append("KYP_TOO_FRIENDLY(EPST certified)")
        if inverse:
            parts.append("KYP_IS_TARGET_INVERSE(fingerprint sp "
                         "%+.2f, c_0 == R exact)" % sp_fp)
        parts.append("N_TREND(sp(N, bound/M) %+.2f, halves "
                     "%+.3f; energy sp %+.2f)"
                     % (sp_b, sl_b, sp_e))
        parts.append("CONTROL_CENSUS(EPST %s %.3f; SCR %s "
                     "%.3f -- friendliness signature; SMOOTH "
                     "trivial %.1e)"
                     % ("FAIL" if epst_fails else "CERT",
                        float(E_ep),
                        "CERTIFIED" if scr_cert else "fails",
                        float(E_sc), float(E_sm)))
        parts.append("CURRENCY_READING(QM-AM overhead med "
                     "%+.2f dec, generic census %d/42)"
                     % (float(np.median(qm_all)), gen_cert))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the block bookkeeping, "
          "the obstruction lemma o1 + o2, the Riccati closed "
          "form and its budget identity (all EXACT rational); "
          "MEASURED: certification census, trends, control and "
          "currency censuses (42 rungs only); OPEN: the kz15 "
          "razor, the cofinal step and the L2 mechanism "
          "(unchanged, with the state-space vehicle now "
          "excluded); NO RH claim"
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
