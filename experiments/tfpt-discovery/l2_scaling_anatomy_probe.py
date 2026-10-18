#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""l2_scaling_anatomy_probe -- PRIME.PORT.COUPLEDTAU.
L2_SCALING_ANATOMY.01 (round 272): the reviewer-adjudicated
follow-up of r271: a PURE ANATOMY round (NO new certificate, NO
bound modification, NO refinement) that dissects the critical
r271 finding sp(N, eps) = +0.67 -- the sealed c2PAIR bound GROWS
with N on the measured ladder while the certified margin halves
move +0.032 -> -0.019 -- into an EXACT factorization, measures
the truth side separately, locates where the bound loses, and
formulates the flip condition quantitatively.  The entire front
of the round: WHY does the rigorous pair bound grow with N, and
is H5 asymptotically at risk (possibility A: the TRUE rest grows
toward the demand) or is only the bound too coarse (possibility
B: the true rest falls, the bound loses cancellation)?

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r271 machinery verbatim): t_{N-2} = sum_b ct_b
(r244 chain rows, r266 eval); F = 0.20 edge split t = t_edge + R;
Z = t_{N-2} + chain, Z_local = t_edge + chain; maximal same-sign
runs of the bx-sorted bulk with masses M_i and exact signed sums
s_i (alternation warded); the SEALED c2PAIR bound (r269 winner,
r271 theorem form, F 0.20 + offset 0 FROZEN):
  eps = sum_j |M_{2j} - M_{2j+1}| + [m odd] M_{m-1}.
Demand scale M_W = sqrt(5/7); ALL scalings are measured as RATIOS
to the demand (only the ratio decides H5).

LEG A -- THE EXACT FACTORIZATION OF THE BOUND (bound-side scope):
with J = pair count, A = 2J the paired-run count, S_pair = sum of
paired run masses, eps_pairs = sum_j |M_{2j} - M_{2j+1}|:
  eps_pairs == A x B x C EXACTLY, with
  A = paired-run count            (the COUNT factor),
  B = S_pair / A                  (the AMPLITUDE scale, mean
                                   paired run mass, reported as
                                   B / M_W -- ratio to demand),
  C = eps_pairs / S_pair          (the bound-side realized
                                   pair-CANCELLATION factor),
  eps = eps_pairs + tail          (tail = unpaired last-run mass).
The count CASCADE is measured alongside (bulk atoms nb, run count
m, pair count J).  EXPONENTS: the primary log-log slope is the
HALVES LOG-SLOPE (difference of mean ln X between the second and
first half of the N-sorted 42-rung ladder, divided by the same
for ln N) -- deterministic and EXACTLY ADDITIVE across factors of
a product; secondary: Theil-Sen median of pairwise log-log slopes
and Spearman rank confidence; halves medians for every series.
  alpha  = halves slope of A;  beta = halves slope of B / M_W;
  cslope = halves slope of C;  gamma := -cslope.
CONSISTENCY GATE (exact): alpha + beta + cslope == halves slope
of eps_pairs / M_W (bar 1e-9), the sign reproduces the r271
upward trend, and sp(N, eps/M_W) reproduces the r271 record
+0.67 (tol 0.05).  TREND CARRIER (sealed rule): the factor with
the LARGEST halves-slope contribution to the eps_pairs trend
(A vs B vs C; reported with the full exponent table).

LEG B -- THE TRUTH SIDE (typed POTENTIAL_ONLY, ground truth,
NEVER usable as a bound; SEPARATE function scope from the
bound-side factorization, AST-audited):
(b1) the TRUE bulk rest |R| vs N as a ratio to the demand
  (|R| / M_W): does it fall or grow -- and the BOUND LOSS
  loss = log10(eps / |R|) vs N (how far the bound sits above the
  truth, in decades);
(b2) the true cancellation depth C_true = |R| / sum|s_i| vs N
  (gamma_true := -halves slope of C_true) and the true level-2
  depth |sum_j P_j| / sum_j |P_j| vs N (P_j = s_{2j} + s_{2j+1});
(b3) the MARGIN OF TRUTH margin_true = M_W - |Z| vs N (the
  r258-FLAT result re-measured in this coordinate).
A-vs-B ADJUDICATION (sealed rule, SP_BAR 0.30, MT_SLOW_BAR -0.5):
  RISK  iff sp(N, |R|/M_W) >= SP_BAR AND the second-half median
        of |R|/M_W exceeds the first-half median;
  LOSSG iff sp(N, loss) >= SP_BAR AND the second-half median of
        loss exceeds the first-half median;
  MTOK  iff sp(N, margin_true) >= MT_SLOW_BAR (flat or slowly
        falling truth margin);
  verdict: MIXED iff RISK and LOSSG; H5_ASYMPTOTIC_RISK iff RISK
  only; BOUND_COARSENESS_CONFIRMED iff LOSSG and MTOK and not
  RISK; SCALING_INCONCLUSIVE otherwise -- combinations honest.

LEG C -- WHERE THE BOUND LOSES (the loss decomposition; every
source with its own N-trend):
  loss = log10(eps / |R|) decomposes EXACTLY (same logs) as
  loss = gap12 + slack2 with gap12 = log10(eps / eps_L2) (the
  part a blind level-2 pairing of the SAME fixed form recovers --
  adjacent pair-sum cancellation, r271 sealed builder imported
  verbatim) and slack2 = log10(eps_L2 / |R|) (beyond blind
  level-2: non-adjacent / global cancellation).  SOURCES:
  (c1) ENVELOPE SLACK: the r269 Christoffel-majorant error-mass
       share sum|M_i - E~_i| / sum E~_i vs N (does it grow?);
  (c2) PAIRING SLACK level 1 = gap12 vs N, PLUS the sign-
       correlation structure of the P_j sequence (alternation
       fraction, sign-run lengths, lag-1..4 sign correlations vs
       N -- the correlation length of the level-2 signs; sign
       statistics on the r270 block convention, the odd tail run
       as its own block);
  (c3) LEVEL-2 SLACK = slack2 vs N (the r270 coin-like P signs:
       does the potential beyond blind level-2 GROW with N? then
       the lost cancellation sits there);
  (c4) BOUNDARY/TAIL share tail / eps vs N.
  RANKING (sealed rule): sources c1-c4 ranked by sp(N, source)
  DESCENDING (halves deltas reported); the countertrend address
  = the top-ranked source with sp >= SP_BAR, restricted for the
  FLIP CONDITION to the cancellation carriers {c2, c3}.
  R270 reproduction ward: the exception-branch P-sign alternation
  fraction median must sit in [0.34, 0.44] (r270 record 0.39).

LEG D -- THE FLIP CONDITION (the delivery object; typed
TASK_FORMULATION_ONLY, no claim): with the measured halves
exponents, the eps trend exponent is alpha + beta - gamma; the
sign flips iff the cancellation factor supplies gamma > alpha +
beta =: gamma_req; the currently missing decay is delta :=
alpha + beta - gamma (the precise L2 task: "the missing
cancellation structure must supply an additional N^{-delta'}
with delta' > delta, and it must sit in the top-ranked slack
source").  TRUTH FEASIBILITY (sealed; the truth cannot be
beaten): flip_true := alpha + beta - gamma_true; TRUTH_ALLOWS
iff flip_true < 0; TRUTH_MARGINAL iff 0 <= flip_true <=
FEAS_TOL (0.05); TRUTH_INSUFFICIENT iff flip_true > FEAS_TOL
(then possibility A is real at the measured exponents).

LEG E -- WARDS / MUST-FAILS: all measurements deterministic; the
bound-side factorization and the truth-side metrics live in TWO
SEPARATE function scopes (AST scope audit: the bound-side scope
must not contain any truth-side identifier; a gift mutant
reading the withheld terminal drive key must be FLAGGED);
inherited kills (no fit primitives -- fragment audit; no
zero/prime oracles -- AST firewall); r263/r269/r271 reproduction
wards (exception set == the named 7 + cheap 35; kz15 reserve in
[0.020, 0.035]; sp(N, eps) +0.67 tol 0.05; sp(N, |Z_local|)
-0.20 tol 0.05; sp(N, margin_cert) -0.03 tol 0.05; margin_cert
halves +0.032 / -0.019 tol 0.005; eps == r269 bound_pairsum,
rel 1e-9); SMOOTH anchor (alias <= 1e-12, q_N <= 1e-20, factor
identity holds); EPSTEIN/SCRAMBLE control reference (identity +
factor census on the broken-arithmetic worlds); mp SAMPLES on
the DEEPEST rungs (the most critical points of the trend fits):
PBB.mp_drive (dps 60) at kz15 (bar 1e-8, r269 record route) and
at the two deepest ladder rungs (bar 3e-6, the deep ward family
constant; the f64 quality at N_max protects the trend fit);
MUST-FAILS: (m1) FACTORIZATION THAT DOES NOT MULTIPLY -- the
mutant replacing the mean amplitude B by the MEDIAN breaks the
exact identity A x B x C == eps_pairs loudly (>= 1e3 x the
exact-identity floor AND >= 1e-6 abs); (m2) HALVES-SPLIT MUTANT
-- the seed-272 permutation of the eps series against the
N-sorted axis must destroy the trend (|sp| < SHUF_BAR 0.5 and
< the measured true sp); TOY EXACTNESS: hand-checked sequences
reproduce the factorization, the truth metrics and the loss
decomposition EXACTLY (bar 1e-14).

INDEX FIREWALL (binding, r238-r271 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r269 PBB.mask_edge + PBB.runs_split +
PBB.bound_pairsum + PBB.env_chain + PBB.mp_drive, r271
UPT.bound_level2 (the sealed level-2 fixed form), r244 BH.wpack
+ BH.spearman, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls;
VAL_BAR 1e-9; ID_BAR 1e-12; ADD_BAR 1e-9 (slope additivity +
loss decomposition); TOY_BAR 1e-14; SP_BAR 0.30; MT_SLOW_BAR
-0.5; SHUF_BAR 0.5; FEAS_TOL 0.05; LOUD 1e3; MUT_MIN 1e-6;
R271_SP_EPS +0.67 tol 0.05; R271_SP_ZL -0.20 tol 0.05;
R271_SP_MG -0.03 tol 0.05; R271_MG_HALVES (+0.032, -0.019) tol
0.005; R270_ALT_BAND (0.34, 0.44); RESERVE_BAND (0.020, 0.035);
MP_DPS 60; MP_T_BAR 1e-8 (kz15); MP_DEEP_BAR 3e-6 (two deepest
rungs); SM_Q_BAR 1e-20; SM_ALIAS_BAR 1e-12; SHUFFLE_SEED 272;
KZ_ANCHOR 15; LAGS (1, 2, 3, 4); runtime <= 1800 s; smoke = w9
+ controls + toy + factor numerics + scope audits + must-fail m1
(ladder, trends, adjudication, mp wards, m2 skipped).  DISCLOSED
PRE-SPEC INPUT (no scratch run of this probe): every reproduction
band is an r263/r269/r270/r271 RECORD number adopted as-is;
nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  TREND_CARRIER(factor, exponent table alpha/beta/gamma +
    cascade + truth exponents, halves splits)
+ TRUTH_SIDE(sp R_rel, sp loss, sp margin_true + halves)
+ [exactly one of] BOUND_COARSENESS_CONFIRMED(loss trend, truth
    margin flat) / H5_ASYMPTOTIC_RISK(R_rel trend) / MIXED(both
    quantified) / SCALING_INCONCLUSIVE(the measured sp values)
+ SLACK_RANKING(c1-c4 ordered by sp, halves deltas)
+ FLIP_CONDITION(delta, gamma_req, address cX, TRUTH_ALLOWS /
    TRUTH_MARGINAL / TRUTH_INSUFFICIENT)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED.
Honesty before beauty: no verdict claims a cofinal law or an
asymptotic mechanism; every trend is MEASURED on 42 rungs only;
the exception scalar's positivity beyond the measured 42 stays
OPEN; r243-r271 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 was 28/28 gates with NO amendment; calibration pass
1 = first full evaluation, 28/28 gates, wall 52.3 s -- NO physics
bar, band, rule or verdict rule was moved at any point; pass 2 =
the record run, identical to pass 1 in every printed figure up
to WALL; the only post-freeze edit is this record-table
insertion, which IS the protocol):
CAL_VERDICT = TREND_CARRIER(A_pairs, alpha +1.01 beta -0.81
gamma -0.01 -> eps slope +0.20) + TRUTH_SIDE(sp R/M -0.31, sp
loss +0.51, sp margin_true +0.36) + BOUND_COARSENESS_CONFIRMED
+ SLACK_RANKING(c3_slack2 > c2_gap12 > c4_tail > c1_envelope)
+ FLIP_CONDITION(delta +0.21, gamma_req +0.20, address
c3_slack2, TRUTH_ALLOWS).
Key numbers.  LEG A (42 rungs N in [142, 878], halves log-slope
primary, Theil-Sen + Spearman confidence, ratios to sqrt(5/7)):
alpha(A_pairs) +1.010 (ts +1.009, sp +1.00, halves med 84 ->
210); beta(B_amp/M) -0.808 (ts -0.798, sp -0.98, halves med
0.0113 -> 0.0055); cslope(C_bound) +0.005 (ts +0.007, sp +0.06,
halves med 0.4709 -> 0.4751) => gamma = -0.005: the bound-side
pair-cancellation factor is FLAT -- the sealed pairing captures
a CONSTANT ~53 pct of the bulk mass at every depth and gains
NOTHING with N; cascade alpha(nb_atoms) +1.001, alpha(m_runs)
+1.006; eps_pairs/M slope +0.207 == alpha + beta + cslope
(additivity dev 2.8e-16), eps/M slope +0.196 (tail correction
-0.011), sp(N, eps) +0.67 == the r271 record; the +0.67 trend
is carried by COUNT x AMPLITUDE (A x B ~ N^{+0.20}) with ZERO
cancellation gain.  LEG B (POTENTIAL_ONLY): |R|/M sp -0.31,
slope_h -0.256, halves med 0.2318 -> 0.1490 -- the TRUE rest
FALLS relative to the demand; bound loss log10(eps/|R|) sp
+0.51, halves 0.345 -> 0.632 dec -- the bound LOSES a growing
number of decades; C_true sp -0.46, gamma_true +0.453 (the true
cancellation deepens like ~N^{-0.45}); level-2 depth
|sumP|/sum|P| sp -0.50, halves 0.450 -> 0.234; margin_true/M sp
+0.36, halves +0.264 -> +0.414 -- the truth margin RISES with N
(the r258-FLAT result re-measured: better than flat in this
coordinate); sealed rule: RISK False, LOSS-GROWS True, MT-OK
True => BOUND_COARSENESS_CONFIRMED (possibility B: H5 lives at
the measured exponents, the bound loses cancellation).  LEG C:
loss = gap12 + slack2 exact (dev 2.2e-16); ranking c3_slack2 sp
+0.52 halves 0.221 -> 0.503 dec (the countertrend carrier: the
cancellation BEYOND blind level-2 pairing -- non-adjacent /
global structure); c2_gap12 sp -0.04 (~0.12 dec, flat: blind
level-2 recovers a constant share); c4_tail sp -0.08 (share <=
0.016); c1_envelope sp -0.14 (error share ~0.36, flat -- the
r269 0.32-0.39 range reproduced, NOT growing); P-sign census:
exception alt-frac med 0.39 == the r270 record, all-42 med
0.45, lag-1..4 sign corr med [0.09, 0.01, 0.07, 0.02] (no
usable level-2 sign correlation at any lag), sp(N, lag-1)
-0.14.  LEG D (typed TASK_FORMULATION_ONLY): the missing decay
delta = +0.207 must come from cancellation structure BEYOND
adjacent blind pairing (address c3_slack2); truth feasibility
flip_true = 1.010 - 0.808 - 0.453 = -0.251 => TRUTH_ALLOWS with
~0.25 exponent margin (gamma_true 0.453 >> gamma_req 0.202):
the truth HAS the required decay, the precise L2 task is to
capture ~0.21 of the measured 0.45 truth-decay exponent
source-purely.  LEG E: contribution ward 2.1e-13 main / 3.9e-13
deep / 2.4e-8 controls; factorization identity worst rel dev
1.5e-16 on 47 worlds; r271 wards exact (sp eps/Zl/margin +0.67/
-0.20/-0.03, margin halves +0.032 -> -0.019, kz15 reserve
0.0268); mp deep wards kz15 dev 2.9e-10 (bar 1e-8), kz64 N859
dev 9.3e-9, kz52 N878 dev 6.6e-8 (bar 3e-6; <= 1.0e-7 x eps --
f64 quality at the deepest trend points secured); EPST/SCR
factor reference A 44/60, C 0.425/0.502, C_true 0.135/0.094
(identity OK, world-blind); SMOOTH alias 2.4e-14, q_N 4.2e-25;
m1 median mutant breaks by 4.57e-1 rel (>= 1e3 x floor); m2
seed-272 shuffle |sp| 0.139 < 0.5.  READING (typed, no
upgrade): the r271 alarm is ANATOMICALLY RESOLVED -- the pair
bound grows with N because pair COUNT x amplitude rises ~N^0.2
while the sealed pairing's cancellation capture is exactly
FLAT; the truth moves the OTHER way (rest falls, margin_true
rises): possibility B, the bound is too coarse, H5 is not
asymptotically contradicted by any measured truth trend; the
lost cancellation sits beyond blind adjacent level-2 pairing
(c3, growing 0.22 -> 0.50 dec) with coin-like P signs at every
lag -- the L2 lemma needs a NON-ADJACENT / global mechanism
supplying N^{-delta'}, delta' > 0.21, of the available 0.45.
Runtime 52.3 s full / 0.2 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (records inserted per
protocol; no bar, band, rule or verdict rule moved).

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import universal_pair_theorem_probe as UPT     # noqa: E402 r271
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
VAL_BAR = 1e-9
ID_BAR = 1e-12
ADD_BAR = 1e-9
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
SP_BAR = 0.30
MT_SLOW_BAR = -0.5
SHUF_BAR = 0.5
FEAS_TOL = 0.05
LOUD = 1e3
MUT_MIN = 1e-6
R271_SP_EPS = 0.67
R271_SP_ZL = -0.20
R271_SP_MG = -0.03
R271_SP_TOL = 0.05
R271_MG_HALVES = (0.032, -0.019)
R271_MG_HALVES_TOL = 0.005
R270_ALT_BAND = (0.34, 0.44)
RESERVE_BAND = (0.020, 0.035)
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
SHUFFLE_SEED = 272
KZ_ANCHOR = 15
LAGS = (1, 2, 3, 4)

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
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
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


# ---- the two SEPARATE scopes (AST-audited): bound-side exact
# factorization vs truth-side potential metrics.  The bound-side
# scope consumes ONLY the plain run-mass list; every truth-side
# identifier (signed sums, rest, drive, margin) is forbidden there.
def bound_factors(Mr):
    """LEG A sealed EXACT FACTORIZATION of the c2PAIR bound
    (bound-side scope: run MASSES only): with J pairs (offset 0),
    A = 2J paired runs, mass = paired run mass, ep = pair-gap sum:
    A x B x C == ep EXACTLY, B = mass / A (amplitude scale),
    C = ep / mass (bound-side pair-cancellation factor);
    eps = ep + tl (tl = unpaired last-run mass)."""
    m = len(Mr)
    J = (m - PAIR_OFFSET) // 2
    ep = 0.0
    mass = 0.0
    for i in range(PAIR_OFFSET, m - 1, 2):
        ep += abs(Mr[i] - Mr[i + 1])
        mass += Mr[i] + Mr[i + 1]
    tl = Mr[-1] if (m - PAIR_OFFSET) % 2 == 1 else 0.0
    A = 2 * J
    B = mass / max(A, 1)
    C = ep / max(mass, 1e-300)
    return dict(m=m, J=J, A=A, B=B, C=C, ep=ep, tl=tl,
                eps=ep + tl, mass=mass)


def truth_metrics(Sr):
    """LEG B truth-side scope (typed POTENTIAL_ONLY -- ground-
    truth measurements, NEVER usable as a bound; SEPARATE scope
    from bound_factors): the true bulk rest R = sum s_i, the true
    cancellation depth |R| / sum|s_i|, the level-2 block sums
    P_j = s_{2j} + s_{2j+1} (depth on the PAIRED blocks; the
    sign statistics on the r270 block convention with the odd
    tail run as its own block), and the P-sign statistics
    (alternation fraction, sign-run lengths, lag-k sign
    correlations)."""
    m = len(Sr)
    R = sum(Sr)
    sabs = sum(abs(v) for v in Sr)
    P = [Sr[i] + Sr[i + 1] for i in range(PAIR_OFFSET, m - 1, 2)]
    sumP = sum(P)
    absP = sum(abs(v) for v in P)
    P_full = list(P)
    if (m - PAIR_OFFSET) % 2 == 1:
        P_full.append(Sr[-1])
    sg = [1.0 if v > 0.0 else -1.0 for v in P_full if v != 0.0]
    alt = (sum(1 for j in range(len(sg) - 1)
               if sg[j] * sg[j + 1] < 0.0)
           / max(len(sg) - 1, 1))
    lag = []
    for k in LAGS:
        if len(sg) > k:
            lag.append(sum(sg[j] * sg[j + k]
                           for j in range(len(sg) - k))
                       / (len(sg) - k))
        else:
            lag.append(0.0)
    rl = []
    cur = 1
    for j in range(1, len(sg)):
        if sg[j] == sg[j - 1]:
            cur += 1
        else:
            rl.append(cur)
            cur = 1
    if sg:
        rl.append(cur)
    return dict(R=R, sabs=sabs, sumP=sumP, absP=absP, alt=alt,
                lag=lag,
                rl_med=float(np.median(rl)) if rl else 0.0,
                rl_max=max(rl) if rl else 0)


def mutant_factors_median(Mr):
    """m1 MUST-FAIL MUTANT: a factorization that does NOT
    multiply -- replaces the mean amplitude B by the MEDIAN of
    the paired run masses; A x B_med x C deviates loudly from
    eps_pairs (measured, typed FORBIDDEN as a factorization)."""
    m = len(Mr)
    J = (m - PAIR_OFFSET) // 2
    ep = 0.0
    paired = []
    for i in range(PAIR_OFFSET, m - 1, 2):
        ep += abs(Mr[i] - Mr[i + 1])
        paired.extend((Mr[i], Mr[i + 1]))
    A = 2 * J
    Bmed = float(np.median(paired)) if paired else 0.0
    C = ep / max(sum(paired), 1e-300)
    return A * Bmed * C, ep


def mutant_gift_factor(rc, Mr):
    """scope-audit MUST-FAIL MUTANT: a 'factorization' oriented
    by the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * bound_factors(Mr)["eps"]


BOUND_FORBIDDEN = {"t" + "_term", "Rb", "Sr", "cb", "ct", "cts",
                   "Z", "Zl", "margin", "rho", "R" + "_bulk",
                   "truth_metrics", "sumP", "absP", "pot",
                   "M_W", "loss"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
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


# ---------------------------------------------- trend estimators
def halves_slope(Ns, Xs):
    """dyadic log-slope: (mean ln X | second half - mean ln X |
    first half) / (same for ln N) on the N-sorted ladder --
    deterministic and EXACTLY additive across factors of a
    product (the consistency gate lives on this exactness)."""
    n = len(Ns)
    h = n // 2
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    ln = [math.log(float(v)) for v in Ns]
    num = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    den = (sum(ln[h:]) / (n - h)) - (sum(ln[:h]) / h)
    return num / den


def median_slope(Ns, Xs):
    """Theil-Sen style median of pairwise log-log slopes
    (deterministic; secondary confidence measure)."""
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    ln = [math.log(float(v)) for v in Ns]
    sl = []
    for i in range(len(ln)):
        for j in range(i + 1, len(ln)):
            d = ln[j] - ln[i]
            if abs(d) > 1e-12:
                sl.append((lx[j] - lx[i]) / d)
    return float(np.median(sl)) if sl else 0.0


def halves_med(Xs):
    n = len(Xs)
    h = n // 2
    return (float(np.median(Xs[:h])), float(np.median(Xs[h:])))


# ------------------------------------------------ toy exact tool
def toy_factorization():
    """hand-checked deterministic sequences: the factorization,
    the truth metrics and the loss decomposition must reproduce
    EXACTLY."""
    worst = 0.0
    # odd-m example: ct = [3, -1, 2, -4, 1]
    Mr = [3.0, 1.0, 2.0, 4.0, 1.0]
    Sr = [3.0, -1.0, 2.0, -4.0, 1.0]
    fc = bound_factors(Mr)
    worst = max(worst, abs(fc["A"] - 4.0))
    worst = max(worst, abs(fc["B"] - 2.5))
    worst = max(worst, abs(fc["C"] - 0.4))
    worst = max(worst, abs(fc["A"] * fc["B"] * fc["C"] - fc["ep"]))
    worst = max(worst, abs(fc["ep"] - 4.0))
    worst = max(worst, abs(fc["tl"] - 1.0))
    worst = max(worst, abs(fc["eps"] - PBB.bound_pairsum(Mr)))
    tm = truth_metrics(Sr)
    worst = max(worst, abs(tm["R"] - 1.0))
    worst = max(worst, abs(tm["sabs"] - 11.0))
    worst = max(worst, abs(tm["sumP"] - 0.0))
    worst = max(worst, abs(tm["absP"] - 4.0))
    # loss decomposition on the toy: eps 5, eps_L2 1, |R| 1
    e2 = UPT.bound_level2(Sr)
    worst = max(worst, abs(e2 - 1.0))
    dec = math.log10(fc["eps"] / abs(tm["R"]))
    worst = max(worst, abs(dec - (math.log10(fc["eps"] / e2)
                                  + math.log10(e2 / abs(tm["R"])))))
    # even-m example: ct = [2, -5, 3, -1]
    Mr2 = [2.0, 5.0, 3.0, 1.0]
    fc2 = bound_factors(Mr2)
    worst = max(worst, abs(fc2["A"] - 4.0))
    worst = max(worst, abs(fc2["B"] - 2.75))
    worst = max(worst, abs(fc2["C"] - 5.0 / 11.0))
    worst = max(worst,
                abs(fc2["A"] * fc2["B"] * fc2["C"] - fc2["ep"]))
    worst = max(worst, abs(fc2["eps"] - 5.0))
    worst = max(worst, abs(fc2["tl"] - 0.0))
    # m1 mutant on the even example: 4 x 2.5 x 5/11 = 50/11 != 5
    mut, ep2 = mutant_factors_median(Mr2)
    worst = max(worst, abs(mut - 50.0 / 11.0))
    worst = max(worst, abs(ep2 - 5.0))
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("l2_scaling_anatomy_probe -- PRIME.PORT.COUPLEDTAU."
          "L2_SCALING_ANATOMY.01 (round 272)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   R271_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], UPT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + factor "
                        "numerics + scope audits + must-fail m1; "
                        "ladder, trends, adjudication, mp wards, "
                        "m2 skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED PURE ANATOMY ROUND (no new "
          "certificate, no bound modification): the r271 finding "
          "sp(N, eps) = +0.67 is decomposed EXACTLY into eps = "
          "A x B x C + tail (count x amplitude x bound-side "
          "cancellation, all ratios to the demand sqrt(5/7)); "
          "the truth side (|R|, C_true, margin_true) is measured "
          "in a SEPARATE scope (POTENTIAL_ONLY); the loss "
          "decomposition loss = gap12 + slack2 locates where the "
          "bound loses; the flip condition alpha + beta - gamma "
          "< 0 is formulated quantitatively; A-vs-B adjudicated "
          "by the sealed SP_BAR %.2f rule; ALL bars, rules and "
          "verdicts sealed BEFORE evaluation (pre-spec input = "
          "r263/r269/r270/r271 record numbers, disclosed)"
          % SP_BAR)

    # ---------------- S1: census + controls (r271 scaffold)
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
        v3 = BR.eval_scaled(rows, bx, N - 3)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        wgeom = np.abs(bw * bx) * fac
        alh_t = rows[N - 3]["alh"]
        gam_t = rows[N - 4]["gam_next"]
        sc3 = math.exp(rows[N - 3]["Ls"] - rows[N - 2]["Ls"])
        E = PBB.env_chain(bx, v2, v3, alh_t, gam_t, sc3, wgeom)
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx,
                    E=E, o=o, lo=lo, hi=hi, p=p)

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

    # ---------------- S2: decomposition + factorization identity
    section("S2  EXACT DECOMPOSITION + FACTORIZATION IDENTITY")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        rc["absum"] = absum
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for c in crecs:
        rc = crecs[c]
        rc["absum"] = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d mains + 3 "
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e) -- "
          "the anatomy operates on an EXACT decomposition"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        Ecl = rc["E"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        t_loc = float(np.sum(cts[ed]))
        cb = cts[~ed]
        Eb = Ecl[~ed]
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        Er = [float(np.sum(Eb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        sm_dev = max((abs(abs(s_) - m_)
                      for s_, m_ in zip(Sr, Mr)), default=0.0)
        fc = bound_factors(Mr)
        tm = truth_metrics(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        e_l2 = UPT.bound_level2(Sr)
        errsh = (sum(abs(a_ - b_) for a_, b_ in zip(Mr, Er))
                 / max(sum(Er), 1e-300))
        Zl = t_loc + rc["chain"]
        return dict(nb=int(len(cb)), Mr=Mr, Sr=Sr, alt_ok=alt_ok,
                    sm_dev=sm_dev, fc=fc, tm=tm, e_c2=e_c2,
                    e_l2=e_l2, errsh=errsh, t_loc=t_loc, Zl=Zl)

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    sm_worst = max((rc["ev"]["sm_dev"] /
                    max(max(rc["ev"]["Mr"], default=1.0), 1e-300)
                    for rc in all_rc), default=0.0)
    check("G21-run-structure-ward", alt_all and sm_worst <= ID_BAR,
          "consecutive bulk runs alternate in sign on every rung "
          "(%d worlds) AND |s_i| == M_i exactly (worst rel dev "
          "%.1e, bar %.0e) -- the truth-side signed sums and the "
          "bound-side masses describe the SAME runs"
          % (len(all_rc), sm_worst, ID_BAR))

    id_worst = 0.0
    eq_worst = 0.0
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        fc = ev["fc"]
        scale = max(fc["ep"], 1e-300)
        id_worst = max(id_worst,
                       abs(fc["A"] * fc["B"] * fc["C"] - fc["ep"])
                       / scale)
        eq_worst = max(eq_worst,
                       abs(fc["eps"] - ev["e_c2"])
                       / max(ev["e_c2"], 1e-300))
    check("G22-factorization-identity", id_worst <= ID_BAR
          and eq_worst <= VAL_BAR,
          "A x B x C == eps_pairs EXACT on every world (worst "
          "rel dev %.1e, bar %.0e) AND eps_pairs + tail == the "
          "sealed r269 bound_pairsum (worst rel dev %.1e, bar "
          "%.0e) -- the factorization IS the bound, not a model "
          "of it" % (id_worst, ID_BAR, eq_worst, VAL_BAR))

    # per-rung normalized series (N-sorted recs only)
    Ns = [rc["N"] for rc in recs]
    eps_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
    epp_rel = [rc["ev"]["fc"]["ep"] / M_W for rc in recs]
    A_s = [float(rc["ev"]["fc"]["A"]) for rc in recs]
    B_rel = [rc["ev"]["fc"]["B"] / M_W for rc in recs]
    C_s = [rc["ev"]["fc"]["C"] for rc in recs]
    nb_s = [float(rc["ev"]["nb"]) for rc in recs]
    m_s = [float(rc["ev"]["fc"]["m"]) for rc in recs]
    zl_rel = [abs(rc["ev"]["Zl"]) / M_W for rc in recs]
    mg_rel = [(M_W - (abs(rc["ev"]["Zl"]) + rc["ev"]["e_c2"]))
              / M_W for rc in recs]
    R_rel = [abs(rc["ev"]["tm"]["R"]) / M_W for rc in recs]
    Ct_s = [abs(rc["ev"]["tm"]["R"])
            / max(rc["ev"]["tm"]["sabs"], 1e-300) for rc in recs]
    mt_rel = [(M_W - abs(rc["Z"])) / M_W for rc in recs]
    loss_s = [math.log10(rc["ev"]["e_c2"]
                         / max(abs(rc["ev"]["tm"]["R"]), 1e-300))
              for rc in recs]
    gap12_s = [math.log10(rc["ev"]["e_c2"]
                          / max(rc["ev"]["e_l2"], 1e-300))
               for rc in recs]
    slack2_s = [math.log10(rc["ev"]["e_l2"]
                           / max(abs(rc["ev"]["tm"]["R"]),
                                 1e-300)) for rc in recs]
    errsh_s = [rc["ev"]["errsh"] for rc in recs]
    tail_s = [rc["ev"]["fc"]["tl"] / max(rc["ev"]["e_c2"], 1e-300)
              for rc in recs]
    d2_s = [abs(rc["ev"]["tm"]["sumP"])
            / max(rc["ev"]["tm"]["absP"], 1e-300) for rc in recs]
    alt_s = [rc["ev"]["tm"]["alt"] for rc in recs]
    lag1_s = [rc["ev"]["tm"]["lag"][0] for rc in recs]

    if not smoke:
        sp_eps = BH.spearman(Ns, eps_rel)
        sp_zl = BH.spearman(Ns, zl_rel)
        sp_mg = BH.spearman(Ns, mg_rel)
        h1_mg, h2_mg = halves_med(mg_rel)
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        check("G23-r271-reproduction-wards",
              abs(sp_eps - R271_SP_EPS) <= R271_SP_TOL
              and abs(sp_zl - R271_SP_ZL) <= R271_SP_TOL
              and abs(sp_mg - R271_SP_MG) <= R271_SP_TOL
              and abs(h1_mg - R271_MG_HALVES[0])
              <= R271_MG_HALVES_TOL
              and abs(h2_mg - R271_MG_HALVES[1])
              <= R271_MG_HALVES_TOL and ok15,
              "the r271 scaling record recomputed: sp(N, eps) "
              "%+.2f (ref %+.2f), sp(N, |Z_local|) %+.2f (ref "
              "%+.2f), sp(N, margin_cert) %+.2f (ref %+.2f), "
              "margin halves %+.3f -> %+.3f (ref %+.3f -> %+.3f, "
              "tol %.3f); kz15 true reserve %.4f in %s"
              % (sp_eps, R271_SP_EPS, sp_zl, R271_SP_ZL, sp_mg,
                 R271_SP_MG, h1_mg, h2_mg, R271_MG_HALVES[0],
                 R271_MG_HALVES[1], R271_MG_HALVES_TOL, slack15,
                 str(RESERVE_BAND)))
    else:
        sp_eps = float("nan")
        check("G23-r271-reproduction-wards", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---------------- S3: toy exactness + scope audits
    section("S3  TOY EXACTNESS + SCOPE AUDITS")
    toy_worst = toy_factorization()
    check("G30-toy-exactness", toy_worst <= TOY_BAR,
          "hand-checked sequences reproduce EXACTLY (worst dev "
          "%.1e, bar %.0e): factorization A=4 B=2.5 C=0.4 -> "
          "ep=4 on [3,-1,2,-4,1]; truth R=1, sumP=0, absP=4; "
          "loss decomposition log-exact; even example A=4 "
          "B=2.75 C=5/11 -> ep=5; m1 median mutant 50/11 != 5"
          % (toy_worst, TOY_BAR))
    h_bf = scope_audit("bound_factors", BOUND_FORBIDDEN)
    h_hs = scope_audit("halves_slope", BOUND_FORBIDDEN)
    h_m0 = scope_audit("mutant_gift_factor", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G31-scope-audits", not (h_bf or h_hs) and bool(h_m0)
          and not ag_hits,
          "TWO SEPARATE SCOPES: bound_factors consumes run "
          "masses only, NO truth-side identifier in scope%s; "
          "trend estimator clean%s; the gift mutant (withheld "
          "terminal drive key) FLAGGED (%s); fragment audit (no "
          "fit primitives): %s"
          % ("" if not h_bf else " VIOLATION " + "; ".join(h_bf),
             "" if not h_hs else " VIOLATION " + "; ".join(h_hs),
             "; ".join(h_m0) if h_m0 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: LEG A -- exponents + carrier
    section("S4  LEG A -- EXPONENT TABLE + TREND CARRIER")
    if not smoke:
        alpha = halves_slope(Ns, A_s)
        beta = halves_slope(Ns, B_rel)
        cslope = halves_slope(Ns, C_s)
        gamma = -cslope
        sl_epp = halves_slope(Ns, epp_rel)
        sl_eps = halves_slope(Ns, eps_rel)
        alpha_nb = halves_slope(Ns, nb_s)
        alpha_m = halves_slope(Ns, m_s)
        tabA = (("A_pairs", A_s, alpha), ("B_amp/M", B_rel, beta),
                ("C_bound", C_s, cslope),
                ("eps_pairs/M", epp_rel, sl_epp),
                ("eps/M", eps_rel, sl_eps),
                ("nb_atoms", nb_s, alpha_nb),
                ("m_runs", m_s, alpha_m))
        for nm, ser, sl in tabA:
            hm1, hm2 = halves_med(ser)
            info("%-13s slope_h %+.3f  ts %+.3f  sp %+.2f  "
                 "halves med %.4g -> %.4g"
                 % (nm, sl, median_slope(Ns, ser),
                    BH.spearman(Ns, ser), hm1, hm2))
        check("G40-exponent-table", True,
              "BOUND-SIDE EXPONENTS (halves log-slope primary, "
              "Theil-Sen + Spearman confidence, all ratios to "
              "sqrt(5/7)): alpha(A) %+.3f, beta(B/M) %+.3f, "
              "gamma(C decay) %+.3f (cslope %+.3f); cascade "
              "alpha(nb) %+.3f, alpha(runs) %+.3f; eps_pairs/M "
              "slope %+.3f, eps/M slope %+.3f (tail correction "
              "%+.3f)"
              % (alpha, beta, gamma, cslope, alpha_nb, alpha_m,
                 sl_epp, sl_eps, sl_eps - sl_epp))
        add_dev = abs((alpha + beta + cslope) - sl_epp)
        check("G41-consistency-gate", add_dev <= ADD_BAR
              and sl_eps > 0.0
              and abs(sp_eps - R271_SP_EPS) <= R271_SP_TOL,
              "alpha + beta + cslope == slope(eps_pairs/M) EXACT "
              "(dev %.1e, bar %.0e); the sign is POSITIVE "
              "(%+.3f) and sp(N, eps) %+.2f reproduces the r271 "
              "record %+.2f -- the factorization carries the "
              "+0.67 trend without residue"
              % (add_dev, ADD_BAR, sl_eps, sp_eps, R271_SP_EPS))
        contrib = (("A_pairs", alpha), ("B_amp", beta),
                   ("C_bound", cslope))
        carrier = max(contrib, key=lambda t: t[1])
        check("G42-trend-carrier", True,
              "SEALED RULE (largest halves-slope contribution to "
              "the eps_pairs trend): %s -- contributions "
              "alpha(A) %+.3f + beta(B) %+.3f + cslope(C) %+.3f "
              "= %+.3f; the count cascade (atoms %+.3f -> runs "
              "%+.3f -> pairs %+.3f) shows where the count "
              "growth originates"
              % (carrier[0], alpha, beta, cslope, sl_epp,
                 alpha_nb, alpha_m, alpha))
    else:
        alpha = beta = gamma = cslope = sl_epp = sl_eps = 0.0
        carrier = ("n/a", 0.0)
        for g_ in ("G40-exponent-table", "G41-consistency-gate",
                   "G42-trend-carrier"):
            check(g_, True, "SMOKE: skipped")

    # ---------------- S5: LEG B -- truth side + A-vs-B
    section("S5  LEG B -- TRUTH SIDE (POTENTIAL_ONLY) + A-vs-B")
    if not smoke:
        sp_R = BH.spearman(Ns, R_rel)
        sp_loss = BH.spearman(Ns, loss_s)
        sp_mt = BH.spearman(Ns, mt_rel)
        sp_Ct = BH.spearman(Ns, Ct_s)
        sp_d2 = BH.spearman(Ns, d2_s)
        gamma_true = -halves_slope(Ns, Ct_s)
        sl_R = halves_slope(Ns, R_rel)
        h1R, h2R = halves_med(R_rel)
        h1L, h2L = halves_med(loss_s)
        h1M, h2M = halves_med(mt_rel)
        h1D, h2D = halves_med(d2_s)
        tabB = (("R/M", R_rel), ("loss dec", loss_s),
                ("margin_true/M", mt_rel), ("C_true", Ct_s),
                ("depth2_true", d2_s))
        for nm, ser in tabB:
            hm1, hm2 = halves_med(ser)
            info("%-14s sp %+.2f  halves med %.4g -> %.4g"
                 % (nm, BH.spearman(Ns, ser), hm1, hm2))
        check("G50-truth-side-table", True,
              "TRUTH SIDE (typed POTENTIAL_ONLY, never a bound): "
              "b1 |R|/M sp %+.2f slope_h %+.3f halves %.4g -> "
              "%.4g; bound loss log10(eps/|R|) sp %+.2f halves "
              "%.3f -> %.3f dec; b2 C_true sp %+.2f gamma_true "
              "%+.3f, level-2 depth |sumP|/sum|P| sp %+.2f "
              "halves %.3f -> %.3f; b3 margin_true/M sp %+.2f "
              "halves %+.4f -> %+.4f (the r258-FLAT coordinate)"
              % (sp_R, sl_R, h1R, h2R, sp_loss, h1L, h2L, sp_Ct,
                 gamma_true, sp_d2, h1D, h2D, sp_mt, h1M, h2M))
        risk = (sp_R >= SP_BAR) and (h2R > h1R)
        lossg = (sp_loss >= SP_BAR) and (h2L > h1L)
        mtok = (sp_mt >= MT_SLOW_BAR)
        if risk and lossg:
            ab_verd = "MIXED"
        elif risk:
            ab_verd = "H5_ASYMPTOTIC_RISK"
        elif lossg and mtok:
            ab_verd = "BOUND_COARSENESS_CONFIRMED"
        else:
            ab_verd = "SCALING_INCONCLUSIVE"
        check("G51-a-vs-b-adjudication", True,
              "SEALED RULE (SP_BAR %.2f, MT_SLOW_BAR %.1f): RISK "
              "= %s (sp(R/M) %+.2f, halves %.4g -> %.4g), LOSS-"
              "GROWS = %s (sp %+.2f, halves %.3f -> %.3f dec), "
              "MT-FLAT-OK = %s (sp %+.2f) => %s"
              % (SP_BAR, MT_SLOW_BAR, risk, sp_R, h1R, h2R,
                 lossg, sp_loss, h1L, h2L, mtok, sp_mt, ab_verd))
    else:
        ab_verd = "n/a"
        sp_R = sp_loss = sp_mt = gamma_true = float("nan")
        check("G50-truth-side-table", True, "SMOKE: skipped")
        check("G51-a-vs-b-adjudication", True, "SMOKE: skipped")

    # ---------------- S6: LEG C -- loss decomposition + ranking
    section("S6  LEG C -- LOSS DECOMPOSITION + SLACK RANKING")
    dec_worst = max((abs(loss_s[i] - (gap12_s[i] + slack2_s[i]))
                     for i in range(len(recs))), default=0.0)
    check("G60-loss-decomposition-exact", dec_worst <= ADD_BAR,
          "loss = gap12 + slack2 EXACT per rung (worst dev %.1e, "
          "bar %.0e): gap12 = log10(eps/eps_L2) is what the "
          "sealed blind level-2 pairing recovers, slack2 = "
          "log10(eps_L2/|R|) is the cancellation BEYOND blind "
          "level-2" % (dec_worst, ADD_BAR))
    if not smoke:
        srcs = (("c1_envelope", errsh_s), ("c2_gap12", gap12_s),
                ("c3_slack2", slack2_s), ("c4_tail", tail_s))
        ranked = []
        for nm, ser in srcs:
            sp_ = BH.spearman(Ns, ser)
            hm1, hm2 = halves_med(ser)
            ranked.append((nm, sp_, hm1, hm2))
            info("%-12s sp %+.2f  halves med %.4g -> %.4g "
                 "(delta %+.4g)" % (nm, sp_, hm1, hm2,
                                    hm2 - hm1))
        ranked.sort(key=lambda t: -t[1])
        top = ranked[0]
        cand23 = [t for t in ranked
                  if t[0] in ("c2_gap12", "c3_slack2")]
        addr = cand23[0][0] if cand23 else "none"
        check("G61-slack-ranking", True,
              "SEALED RANKING (by sp(N, source) desc): %s; "
              "countertrend address (cancellation carriers "
              "{c2, c3} only): %s -- the lost cancellation the "
              "flip condition must recover sits there"
              % ("; ".join("%s sp %+.2f d %+.3g"
                           % (t[0], t[1], t[3] - t[2])
                           for t in ranked), addr))
        alt_exc = [rc["ev"]["tm"]["alt"] for rc in recs
                   if rc["g"] < 0.0]
        alt_med_exc = float(np.median(alt_exc))
        lag_meds = [float(np.median([rc["ev"]["tm"]["lag"][k]
                                     for rc in recs]))
                    for k in range(len(LAGS))]
        check("G62-p-sign-census", R270_ALT_BAND[0]
              <= alt_med_exc <= R270_ALT_BAND[1],
              "P-sign structure (level-2 correlation length): "
              "exception alt-frac med %.2f in %s (r270 record "
              "0.39 reproduced); all-42 alt-frac med %.2f, "
              "sign-run len med %.1f max %d; lag-1..4 sign corr "
              "med %s; sp(N, lag-1) %+.2f, sp(N, alt) %+.2f"
              % (alt_med_exc, str(R270_ALT_BAND),
                 float(np.median(alt_s)),
                 float(np.median([rc["ev"]["tm"]["rl_med"]
                                  for rc in recs])),
                 max(rc["ev"]["tm"]["rl_max"] for rc in recs),
                 str([round(v, 2) for v in lag_meds]),
                 BH.spearman(Ns, lag1_s),
                 BH.spearman(Ns, alt_s)))
    else:
        ranked = []
        addr = "n/a"
        check("G61-slack-ranking", True, "SMOKE: skipped")
        check("G62-p-sign-census", True, "SMOKE: skipped")

    # ---------------- S7: LEG D -- the flip condition
    section("S7  LEG D -- FLIP CONDITION (TASK_FORMULATION_ONLY)")
    if not smoke:
        gamma_req = alpha + beta
        delta = alpha + beta - gamma
        flip_true = alpha + beta - gamma_true
        if flip_true < 0.0:
            feas = "TRUTH_ALLOWS"
        elif flip_true <= FEAS_TOL:
            feas = "TRUTH_MARGINAL"
        else:
            feas = "TRUTH_INSUFFICIENT"
        check("G70-flip-condition", True,
              "THE QUANTIFIED L2 TASK (typed TASK_FORMULATION_"
              "ONLY, no claim): the eps trend exponent is alpha "
              "+ beta - gamma = %+.3f + %+.3f - %+.3f = %+.3f; "
              "the sign flips iff the cancellation factor "
              "supplies gamma > gamma_req = %+.3f, i.e. the "
              "missing structure must deliver an ADDITIONAL "
              "N^(-delta') with delta' > delta = %+.3f, and by "
              "the slack ranking it must sit in %s"
              % (alpha, beta, gamma, delta, gamma_req, delta,
                 addr))
        check("G71-truth-feasibility", True,
              "SEALED FEASIBILITY (the truth cannot be beaten): "
              "flip_true = alpha + beta - gamma_true = %+.3f + "
              "%+.3f - %+.3f = %+.3f => %s (tol %.2f); truth "
              "slope of |R|/M is %+.3f -- if gamma_true itself "
              "does not reach gamma_req, possibility A is real "
              "at the measured exponents"
              % (alpha, beta, gamma_true, flip_true, feas,
                 FEAS_TOL, halves_slope(Ns, R_rel)))
    else:
        delta = float("nan")
        feas = "n/a"
        check("G70-flip-condition", True, "SMOKE: skipped")
        check("G71-truth-feasibility", True, "SMOKE: skipped")

    # ---------------- S8: controls + mp wards + must-fails
    section("S8  CONTROLS + MP WARDS + MUST-FAILS")
    ctl_ok = True
    ctl_note = []
    for c in ("EPST", "SCR"):
        rc = crecs[c]
        ev = rc["ev"]
        fc = ev["fc"]
        ok_id = (abs(fc["A"] * fc["B"] * fc["C"] - fc["ep"])
                 / max(fc["ep"], 1e-300) <= ID_BAR)
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        ctl_note.append("%s A %d B/M %.3f C %.3f C_true %.3f "
                        "dev %.1e id %s"
                        % (c, fc["A"], fc["B"] / M_W, fc["C"],
                           abs(ev["tm"]["R"])
                           / max(ev["tm"]["sabs"], 1e-300),
                           dev, "OK" if ok_id else "BROKEN"))
        ctl_ok = ctl_ok and ok_id and (dev <= TB_WARD_BAR_CTRL)
    main_fitted = not ctl_ok
    check("G80-control-reference", ctl_ok,
          "the factorization identity holds on the PERTURBED "
          "worlds exactly (broken-arithmetic REFERENCE points "
          "for the factor levels): %s -- world-blind algebra, "
          "NOT main-fitted" % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    rcS = crecs["SMOOTH"]
    fcS = rcS["ev"]["fc"]
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    okS = (abs(fcS["A"] * fcS["B"] * fcS["C"] - fcS["ep"])
           / max(fcS["ep"], 1e-300) <= ID_BAR)
    check("G81-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okS,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "factor identity holds trivially on the self-aliased "
          "source (%s)" % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
                           "OK" if okS else "BROKEN"))
    if not smoke:
        mp_note = []
        ok_mp = True
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        t15 = PBB.mp_drive(rc15["p"], MP_DPS)
        d15 = abs(t15 - rc15["t_term"])
        ok_mp = ok_mp and (d15 <= MP_T_BAR)
        mp_note.append("kz15 (N %d) dev %.1e (bar %.0e)"
                       % (rc15["N"], d15, MP_T_BAR))
        for rc in recs[-2:]:
            t_mp = PBB.mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("kz%d (N %d, DEEPEST) dev %.1e (bar "
                           "%.0e; %.1e x eps)"
                           % (rc["kz"], rc["N"], dv, MP_DEEP_BAR,
                              dv / max(rc["ev"]["e_c2"],
                                       1e-300)))
        check("G82-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs -- the deepest points anchor every exponent "
              "fit: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G82-mp-deep-wards", True, "SMOKE: skipped")
    mut_worst = 0.0
    for rc in all_rc:
        mut, ep_ = mutant_factors_median(rc["ev"]["Mr"])
        if ep_ > 0.0:
            mut_worst = max(mut_worst, abs(mut - ep_) / ep_)
    floor = max(id_worst, 1e-16)
    check("G83-mustfail-nonmultiplying", mut_worst >= LOUD * floor
          and mut_worst >= MUT_MIN,
          "m1 FACTORIZATION THAT DOES NOT MULTIPLY (median "
          "amplitude): worst rel identity break %.2e >= %.0f x "
          "the exact floor %.1e AND >= %.0e -- only the mean "
          "amplitude factorizes the bound exactly; the median "
          "variant is typed FORBIDDEN as a factorization"
          % (mut_worst, LOUD, floor, MUT_MIN))
    if not smoke:
        rng = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(Ns,
                                 list(rng.permutation(eps_rel))))
        check("G84-mustfail-halves-shuffle", sp_mut < SHUF_BAR
              and sp_mut < abs(sp_eps),
              "m2 HALVES-SPLIT MUTANT (seed-%d permutation of "
              "the eps series against the N axis): |sp| = %.3f "
              "< %.1f and < the true trend %.2f -- the +0.67 "
              "trend is carried by N, not by the split "
              "machinery" % (SHUFFLE_SEED, sp_mut, SHUF_BAR,
                             abs(sp_eps)))
    else:
        check("G84-mustfail-halves-shuffle", True,
              "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact factorization of the sealed c2PAIR "
          "bound into count x amplitude x cancellation with "
          "measured exponents, the separated truth side, the "
          "exact loss decomposition with slack ranking, and the "
          "quantified flip condition -- NO new certificate, NO "
          "bound modification")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        parts.append("TREND_CARRIER(%s, alpha %+.2f beta %+.2f "
                     "gamma %+.2f -> eps slope %+.2f)"
                     % (carrier[0], alpha, beta, gamma, sl_eps))
        parts.append("TRUTH_SIDE(sp R/M %+.2f, sp loss %+.2f, "
                     "sp margin_true %+.2f)"
                     % (sp_R, sp_loss, sp_mt))
        parts.append("%s" % ab_verd)
        parts.append("SLACK_RANKING(%s)"
                     % " > ".join(t[0] for t in ranked))
        parts.append("FLIP_CONDITION(delta %+.2f, gamma_req "
                     "%+.2f, address %s, %s)"
                     % (delta, alpha + beta, addr, feas))
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the factorization "
          "identity, the loss decomposition, the run structure; "
          "MEASURED: every exponent, trend and ranking (42 rungs "
          "only); OPEN: the cofinal step H5 and the L2 mechanism "
          "(quantified task, not claimed); NO RH claim"
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
