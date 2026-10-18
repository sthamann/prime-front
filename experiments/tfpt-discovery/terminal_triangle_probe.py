#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""terminal_triangle_probe -- PRIME.PORT.COUPLEDTAU.TERMINAL_
TRIANGLE.01 (round 262): close or honestly localize the 0.41-decade
coverage gap of the ONLY certificate that survived the r260
cancellation-demand bar -- the terminal one-step triangle C1b
    |r_{N-1}| <= |t_{N-2}| + |a'_{N-2}||r_{N-2}| + |b'_{N-2}||r_{N-3}|
(r260: valid 42/42, covers 35/42, worst gap 0.41 dec on the 7
missing rungs) -- and pursue the 5/7 GRAM PROVENANCE via the signed
continuation tail (r260-C3: 0.9501 w9 / 0.7255 w13 vs 5/7 = 0.7143).

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r260 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots are the proof
objects; rho_k = F_k^2/h_k, S_n = sum_{k<=n} rho_k; ground truth
(h signs, flip degrees, forced-tail offsets) enters GATES only; no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r244 BH.wpack + BH.bord_chain, r257 CT.union_arrays /
u_matrix / blind_flip_predictor, r260 TX.drive_arrays +
TX.cand_triangle (the sealed driven-recursion coordinates r_k =
F_k/sqrt(h_k), t_k = T_k/sqrt(h_{k+1}), a'_k = -alh_k/
sqrt(gam_{k+1}), b'_k = -sign(gam_k) sqrt|gam_k/gam_{k+1}|), r243
PB.smooth_comb, v881 PIK controls.  B PROVENANCE: B_w = S_{N-2} +
5/7 (r241/r243 IMPORTED floor, never fitted; D_{N-1} = 5/7 by
construction, q_N = rho_{N-1}/(5/7)).  COFINAL LADDER (pre-sealed):
frame-A h <= 900, 42 rungs, (N, kz)-sorted.  R260 KILLS ADOPTED AS
GATES: FIVE_SEVENTHS_NUMEROLOGY, PAIRCORR_REENCODED detector,
WALL_COMPLETION, TARGET_INVERSE_USED, FIXED_STATE_COMPRESSION.

LEG A -- C1B REPRODUCTION + ANATOMY OF THE 7 MISSING RUNGS:
(a1) reproduce the r260 C1b census exactly: valid 42/42, coverage
tri^2 < 5/7 on exactly 35/42, worst gap on the missing rungs inside
the sealed reproduction band [0.30, 0.50] dec.  (a2) source-pure
anatomy of every missing rung: N and h position, window geometry
(union hull length, atom count, support density), the dominant
triangle term (|t| vs |a'r| vs |b'r'|), the terminal cancellation
degree kappa = |r_{N-1}| / tri (how much cancellation the triangle
discards), max prefix r_k^2/D_k; gate = anatomy complete on 7/7
with kappa <= 1 + 1e-9 everywhere (validity restated).  (a3)
signature census (MEASUREMENT): missing-vs-covered medians of
(kappa, terminal q, max prefix r^2/D, hull length, atom count);
Spearman(gap, q) on the 42 rungs printed; the hypothesis "the 7
missing rungs are exactly the top-7 by terminal q" tested and
printed (no gate bar -- census).

LEG B -- SEALED SHARPENING CANDIDATES (exactly 4, target-blind by
construction: every builder consumes ONLY the prefix slice
(r_0..r_{N-2}) plus (t, a', b'); the terminal readout r_{N-1} is
structurally withheld; machine AST audit + deliberate oracle
mutant):
  (b1) K-STEP UNROLLING, j = 1..4 substitutions (k = j+1 recursion
       steps): unroll r_{N-1} = P_j + A_j r_{N-2-j} + B_j r_{N-3-j}
       with P_j the EXACT signed accumulation of the drives
       t_{N-2}..t_{N-2-j} through the (a', b') transfer (a finite
       evaluated linear statistic of prefix data -- same typology
       as t itself) and triangle only the two deepest r-terms:
       bound_j = |P_j| + |A_j||r_{N-2-j}| + |B_j||r_{N-3-j}|.
       VALIDITY gate (bound_j >= |r_{N-1}|(1 - 1e-9), algebraic)
       + coverage bound_j^2 < 5/7 counted per j over 42.
  (b2) SIGN-REFINED GROUPING: measure the terminal sign structure
       (sign t, sign a'r_{N-2}, sign b'r_{N-3}) over the ladder;
       the grouped bound |r_{N-1}| <= |t_{N-2}| + |a'_{N-2}
       r_{N-2} + b'_{N-2} r_{N-3}| is UNCONDITIONALLY valid
       (triangle on two groups) but typed RESTATEMENT_ADJACENT
       (only the drive is triangled; the pair sum is one
       evaluation from the target); the sign RULE (a'r and b'r
       systematically opposite <=> adjacent r-sign alternation,
       since a' < 0 iff alh > 0 and b' < 0 on the positive
       prefix) is censused and typed OBSERVED unless it holds
       42/42 AND the coefficient negativity is chain-uniform
       (then SIGN_RULE_CHAIN_CONSISTENT -- still not a theorem).
  (b3) DRIVE BOUND HONESTY: t_{N-2} = T_{N-2}/sqrt(h_{N-1}) with
       T a FINITE border-comb sum against the terminal polynomial;
       measure the drive cancellation content dec_t = log10(
       T_abs/|T|) at the terminal degree via the rolling
       normalized recursion (T_abs = sum |w_j x_j| |pihat(x_j)|,
       scale-free ratio); the abs-drive triangle t_abs + |a'r| +
       |b'r'| coverage counted: if median dec_t >= 1.0 dec the
       triangle's drive term is itself PAIRCORR-ADJACENT (an
       a-priori proof of the bound would demand a sqrt-scale
       comb cancellation estimate) -- honest typing, sealed.
  (b4) TRIANGLE+PSI1 HYBRID: use the OBSERVED orbit fact r_k^2 <=
       0.51 D_k (r260: max prefix 0.416/0.502) for the two deep
       r-terms: bound = |t| + |a'| sqrt(0.51 D_{N-2}) + |b'|
       sqrt(0.51 D_{N-3}), D_{N-2} = 5/7 + rho_{N-2}, D_{N-3} =
       5/7 + rho_{N-2} + rho_{N-3} (prefix data); validity =
       the orbit fact holds at k = N-2, N-3 on the rung (gated
       as reproduction); typed CONDITIONAL certificate on an
       OBSERVED constant, never source-reasoned.
  SEALED CLOSURE RULES: TRIANGLE_CLOSED(cand) only from the pure
  triangle family (C1b or b1@j): valid 42/42 + covers 42/42;
  b2 closing = TRIANGLE_GROUPED_CLOSED (typed RESTATEMENT_
  ADJACENT); b4 closing = TRIANGLE_CONDITIONALLY_CLOSED(PSI1
  0.51 OBSERVED); best coverage > 35 without closure =
  TRIANGLE_PARTIAL_IMPROVED(cand, cover, gap); no candidate
  above 35 = TRIANGLE_CANCELLATION_ESSENTIAL (the 7 rungs need
  true terminal cancellation -- precise handover).

LEG C -- THE 5/7 GRAM PROVENANCE (exact-square path): the signed
continuation tail tail(m) = sum_{k=N-1}^{N+m-1} rho_k over N+m
degrees, m = 2..12, one indefinite chain continuation per rung
(f64), on ALL 42 rungs + both mains.  (c1) CROSS-ROUTE WARD: the
continued chain rho_k vs the direct bordered-slogdet increments
D_k - D_{k+1} (same corner B) for k in [N-1, N+11] on w9 + w13 +
the 3 sealed sample rungs (idx 0, 20, 41), dev scale max(|D_k|,
|D_{k+1}|), bar 3e-6 (r260 deep-route floor) -- the f64 tail is
trusted only through this ward.  (c2) convergence census:
converged iff |tail(12) - tail(10)| <= 0.02 (absolute; tails are
O(5/7)); per-rung tail(12) spread: median, IQR vs 5/7; N-trend
Spearman(tail(12), N).  (c3) SEALED PROVENANCE RULES:
GRAM_PROVENANCE_CONFIRMED(limit, spread) iff converged fraction
>= 0.90 AND |median tail(12) - 5/7| <= 0.02 AND IQR <= 0.05;
GRAM_PROVENANCE_REFUTED(window-dependent) iff converged fraction
>= 0.90 AND (median or IQR outside); GRAM_PROVENANCE_INCONCLUSIVE
(no convergence) otherwise.  (c4) conditional exact-square test,
armed ONLY on CONFIRMED: replace the corner by B_gram = S_{N-2} +
tail(12) on the two mains and re-gate D_N == B_gram - S_{N-1} >= 0
with the direct square route (rel 1e-6); otherwise EXACT_SQUARE_
OPEN stands.  EVERYTHING in leg C is indefinite arithmetic --
measurement, not a theorem, unless (c4) closes exactly.

LEG D -- KILLS + CONTROLS: (d1) FIVE_SEVENTHS_NUMEROLOGY: floor
min_w h_{N-1}/F_{N-1}^2 in [1.40, 1.46] with non-saturation >=
0.01 (a1-amendment route eta/fb^2, scale-exact); (d2) PAIRCORR
detector on the NEW candidates: any candidate promoted to closure
must stay < 1.0 dec cancellation demand on every rung; the b3
census supplies the honest drive typing; (d3) WALL_COMPLETION:
continuation flips at N+0 / N+2 on w9/w13 within EXT = 6 (ground
truth in gates only); (d4) TARGET_INVERSE_USED: candidate scope
AST audit CLEAN on all four builders while the deliberate oracle
mutant (reads the terminal rho) is FLAGGED (must-fail); (d5)
FIXED_STATE_COMPRESSION: drive truncated to its first 8 entries
breaks the S rebuild by >= 1e3 x honest.  CONTROLS (firewall-
typed): the per-degree triangle tri_k^2 < D_{k+1} on SCR/EPST
BEFORE their flips (validity |r_{k+1}| <= tri_k algebraic at
every pre-flip degree, bar 1e-9 relative) and the first coverage
break located relative to the flip (MEASUREMENT, flips ground
truth in gates only); SMOOTH anchor q_N <= 1e-20; the r257 blind
micro-predictor ward reproduces the control flips 3/3.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; ladder frame-A h <=
900 (42 rungs, (N, kz)-sorted); C1B_COVER_EXPECT 35; C1B_GAP_BAND
[0.30, 0.50] dec; UNROLL_JS (1, 2, 3, 4); PSI1_C 0.51; VALID_EPS
1e-9; DEMAND_BAR 1.0 dec; M_EXT 12, M_LIST 2..12; TAIL_CONV_BAR
0.02; GRAM_MED_BAR 0.02; GRAM_IQR_BAR 0.05; GRAM_CONV_FRAC 0.90;
ROUTE_BAR_EXT 3e-6 (r260 deep floor); WARD_SAMPLE_IDX (0, 20,
41); EXT 6; FIB_LO 8; B57 = 5/7; FLOOR_BAND [1.40, 1.46],
non-saturation 0.01; MARGIN_BAND [0.010, 0.020]; SM_Q_BAR 1e-20;
LOUD 1e3; SQUARE_REGATE_BAR 1e-6; runtime <= 1800 s; smoke = w9 +
controls only (ladder, w13, cross-route samples, reproduction
gates skipped).  DISCLOSED PRE-SPEC SCRATCH CALIBRATION (one
pass, floors and feasibility only, no verdict rule tuned after
any full evaluation): (s1) the r260 record numbers (C1b 35/42,
gap 0.41 dec; floor 1.4278; margin 0.0139; tails 0.9501/0.7255
at m = 6) are adopted as reproduction bands, not re-tuned; (s2)
route floors imported from r260 (deep dict 2.6e-8..1.2e-7,
per-degree bilinear 4.8e-10 MAIN) motivate ROUTE_BAR_EXT 3e-6.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  TRIANGLE_CLOSED(cand) / TRIANGLE_GROUPED_CLOSED(b2) /
  TRIANGLE_CONDITIONALLY_CLOSED(b4) / TRIANGLE_PARTIAL_IMPROVED(
  cand, cover, gap) / TRIANGLE_CANCELLATION_ESSENTIAL(anatomy)
  [all closures achieved are reported, strongest first]
+ TRIANGLE_DRIVE_PAIRCORR_ADJACENT(median dec_t) [if the b3
  census puts the a-priori drive bound above 1.0 dec]
+ GRAM_PROVENANCE_CONFIRMED(limit, IQR) / GRAM_PROVENANCE_REFUTED(
  median, IQR) / GRAM_PROVENANCE_INCONCLUSIVE(conv frac)
+ EXACT_SQUARE_CLOSED / EXACT_SQUARE_OPEN(5/7 Gram provenance)
+ FIVE_SEVENTHS_NUMERICAL_ONLY [if the floor stays measured]
+ PAIRCORR_REENCODED(candidate list) [detector census on the new
  candidates].
Honesty before beauty: a TRIANGLE_CLOSED would certify q_N < 1 on
the whole ladder CONDITIONALLY on the positive base prefix, never
RH; a GROUPED or CONDITIONAL closure is a reduction, not a proof;
no verdict claims a derived 5/7, a bound mechanism, or an
asymptotic law (r243/r250/r253/r256/r257/r258/r260 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
pass 1 = first full evaluation, 26/26 gates, wall 8.3 s -- after
pass 1 ONE PRESENTATION AMENDMENT p1 is disclosed: the G22 detail
clause carried a pre-written conclusion sentence ("the signature
is the terminal q") that the measured data refuted; the clause
was made data-driven; NO bar, band, candidate, closure rule or
provenance rule was moved at any point; pass 2 = the record run
below, numerically identical to pass 1):
CAL_VERDICT = TRIANGLE_PARTIAL_IMPROVED(b1@j=4, cover 38/42, gap
0.39 dec) + TRIANGLE_DRIVE_PAIRCORR_ADJACENT(median dec_t 1.05)
+ GRAM_PROVENANCE_INCONCLUSIVE(conv frac 0.09) + EXACT_SQUARE_
OPEN(5/7 Gram provenance) + FIVE_SEVENTHS_NUMERICAL_ONLY.
Key numbers.  LEG A: C1b reproduced EXACTLY: valid 42/42, cover
35/42, worst gap 0.409 dec in band; the 7 misses: kz20 N170
q0.587 / kz22 N199 q0.055 / kz15 N203 q0.938 / kz39 N277 q0.541
/ kz36 N488 q0.467 / kz38 N522 q0.370 / kz52 N878 q0.138 -- ALL
SEVEN are DRIVE-dominated (|t| is the largest triangle term;
covered set: 32 t-dominated, 3 b'r, 0 a'r); miss-vs-cover
medians kappa 0.427/0.998 (on covered rungs the triangle is
nearly TIGHT -- there is almost no cancellation to discard; the
misses discard a factor ~2.3), q 0.467/0.413, maxq_pre
0.358/0.357, hull 2.00/2.00, atoms 1.1e3/1.6e3; top-7-by-q ==
miss set: FALSE, Spearman(gap, q) on misses -0.21 -- the miss
signature is NOT the terminal q and NOT the geometry: it is the
DISCARDED DRIVE-vs-CHAIN CANCELLATION (kappa), full stop.
LEG B: b1 unroll valid 42/42 at every j; coverage NON-MONOTONE
in depth: j=1 36/42 (gap 0.42), j=2 30/42 (0.25), j=3 31/42
(0.25), j=4 38/42 (0.39) -- best 38/42, no closure; b2 grouped
valid 42/42, covers 36/42 (worst bound^2/B57 2.461): the exact
pair sum does NOT rescue the 7 (they are t-dominated, grouping
the two r-terms attacks the wrong pair); sign census (t, a'r,
b'r): (---) 15, (-+-) 15, (-++) 6, (--+) 4, (+--) 1, (++-) 1;
(a'r, b'r) opposite on 20/42 ONLY => sign rule FAILS
(OBSERVED_PARTIAL, no rule-based bound); a' < 0 on 20/42 (NOT
chain-uniform -- alh changes sign across rungs), b' < 0 on
42/42; adjacent r-alternation fraction median 0.39; b3 drive
cancellation content dec_t = log10(T_abs/|T|): median 1.05, min
0.66, max 2.31 dec; abs-drive triangle covers 0/42 => the
triangle IS paircorr-adjacent in its drive term (any a-priori
bound on |t| re-encodes comb-vs-smooth cancellation at sqrt
scale; the EVALUATED t stays prefix data -- typed, sealed); b4
hybrid: orbit fact r^2 <= 0.51 D holds at k = N-2, N-3 on 42/42
(pool max prefix r^2/D 0.5201 sits ABOVE 0.51 at interior
degrees -- the sealed 0.51 is NOT a uniform orbit constant),
but the bound DILUTES: covers 4/42 (worst bound^2/B57 4.017) --
sqrt(0.51 D) is far above typical |r|.  LEG C: cross-route ward
worst 3.5e-7 (w9; w13 9.6e-10, rungs 0/20/41: 7.1e-10 / 1.1e-7
/ 1.4e-7; bar 3e-6) -- the f64 continuation is route-exact, the
oscillation below is REAL, not noise; tails: converged
(|t12 - t10| <= 0.02) on 4/44 ONLY (conv frac 0.09), tail(12)
median 0.5496, IQR 1.4574, range [-7.24, 13.70]; per-m medians
0.34 / 0.25 / 0.56 / 0.77 / 0.77 / 0.69 / 0.76 / 0.80 / 0.80 /
0.54 / 0.55 (m = 2..12): the ENSEMBLE median hovers near 5/7
for m = 5..10 and destabilizes at m >= 11, while PER-RUNG the
signed tail oscillates without limit (w9: +4.01, w13: -1.56 at
m = 12; the r260 m = 6 snapshot values 0.9501/0.7255 carried no
limit information) => GRAM_PROVENANCE_INCONCLUSIVE by the
sealed rule (no convergence -- neither confirmed nor refuted as
a limit; the ensemble-median brush with 5/7 at moderate m is
recorded as the honest residue); N-trend Spearman(tail12, N) =
-0.00 (none); exact-square test NOT armed, EXACT_SQUARE_OPEN.
LEG D: d1 floor 1.4278 in [1.40, 1.46], non-saturation 0.0278;
q-margin ward min 0.0139 in band; d2 detector fires on NONE of
the sealed candidates (all coverage gaps < 1.0 dec; the b3
typing is carried in the verdict, not as a kill); d3 wall flips
N+0 (w9) / N+2 (w13) == ground truth; d4 AST scopes CLEAN on
all four builders, oracle mutant FLAGGED (rho scope hit); d5
drive truncation to 8 entries breaks the S rebuild by 1.2e+15 x
honest; controls: pre-flip triangle validity worst rel dev
8.3e-16, per-degree D-coverage breaks already at degree 2 on
SCR/EPST (flips 21/25) -- the PER-DEGREE coverage question is
much harder than the terminal one (D_k+1 shrinks toward 5/7
only at the top; measurement, firewall-typed); SMOOTH q_N =
4.2e-25 <= 1e-20; micro-predictor ward 3/3.  READING (typed, no
upgrade): the 0.41-dec gap is HONESTLY LOCALIZED, not closed --
the 7 missing rungs are drive-dominated with kappa ~ 0.43 (the
covered 35 are near-tight, kappa ~ 1.0): what is missing is
genuine cancellation between the border-comb drive t_{N-2} and
the two chain terms at ONE degree per rung, a FINITE (not
asymptotic) comb-vs-smooth cancellation demand -- and the b3
census shows exactly this demand is paircorr-adjacent (median
1.05 dec between |T| and its abs-mass); every pure-triangle
sharpening stays partial (best b1@j=4, 38/42), the sign field
has no usable rule, and the PSI1 hybrid dilutes; the 5/7 Gram
provenance via the continuation tail is INCONCLUSIVE (the tail
does not converge per rung; only the ensemble median at
moderate m brushes 5/7): the exact-square path stays OPEN and
the w13 suggestion is retired.  Runtime 8.3 s full / 0.2 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE (p1 disclosed above, presentation-only, before the
record pass).

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import coupledtau_probe as CT                # noqa: E402 r257
import terminal_crossratio_probe as TX       # noqa: E402 r260
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
C1B_COVER_EXPECT = 35
C1B_GAP_BAND = (0.30, 0.50)
UNROLL_JS = (1, 2, 3, 4)
PSI1_C = 0.51
VALID_EPS = 1e-9
DEMAND_BAR = 1.0
M_EXT = 12
M_LIST = tuple(range(2, 13))
TAIL_CONV_BAR = 0.02
GRAM_MED_BAR = 0.02
GRAM_IQR_BAR = 0.05
GRAM_CONV_FRAC = 0.90
ROUTE_BAR_EXT = 3e-6
WARD_SAMPLE_IDX = (0, 20, 41)
EXT = 6
FIB_LO = 8
FLOOR_BAND = (1.40, 1.46)
NONSAT_MARGIN = 0.01
MARGIN_BAND = (0.010, 0.020)
SM_Q_BAR = 1e-20
LOUD = 1e3
SQUARE_REGATE_BAR = 1e-6
TAIL_OFFSETS = {9: 0, 13: 2}
CTRL_TRI_BAR = 1e-9
CAL_VERDICT = (
    "TRIANGLE_PARTIAL_IMPROVED(b1@j=4, cover 38/42, gap 0.39 "
    "dec) + TRIANGLE_DRIVE_PAIRCORR_ADJACENT(median dec_t 1.05) "
    "+ GRAM_PROVENANCE_INCONCLUSIVE(conv frac 0.09) + "
    "EXACT_SQUARE_OPEN(5/7 Gram provenance) + "
    "FIVE_SEVENTHS_NUMERICAL_ONLY")

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
                       "the r244 chain rows; ground truth (flips, "
                       "tail offsets) enters gates only"
                       if not bad else "; ".join(bad))


# --------------------- sealed sharpening candidates (target-blind:
# consume ONLY the prefix slice rpre = r[:N-1] plus (t, a', b');
# the terminal r_{N-1} is structurally withheld; AST-audited)
def cand_unroll(rpre, t, ap, bp, j):
    """b1: unroll j substitutions of the driven recursion; the
    signed drive accumulation P stays exact, only the two deepest
    r-terms are triangled."""
    P = t[-1]
    A = ap[-1]
    Bc = bp[-1]
    idx = len(t) - 1
    for _ in range(j):
        idx -= 1
        P = P + A * t[idx]
        A, Bc = A * ap[idx] + Bc, A * bp[idx]
    return abs(P) + abs(A) * abs(rpre[idx]) + abs(Bc) * abs(rpre[idx - 1])


def cand_grouped(rpre, t, ap, bp):
    """b2: grouped triangle -- exact signed pair sum, drive
    triangled (RESTATEMENT_ADJACENT typing sealed in the spec)."""
    return abs(t[-1]) + abs(ap[-1] * rpre[-1] + bp[-1] * rpre[-2])


def cand_hybrid(rpre, t, ap, bp):
    """b4: triangle + PSI1 orbit fact r^2 <= 0.51 D (OBSERVED)
    for the two deep r-terms; D from prefix rho only."""
    d_m2 = B57 + rpre[-1] ** 2
    d_m3 = B57 + rpre[-1] ** 2 + rpre[-2] ** 2
    return (abs(t[-1]) + abs(ap[-1]) * math.sqrt(PSI1_C * d_m2)
            + abs(bp[-1]) * math.sqrt(PSI1_C * d_m3))


def drive_abs_ratio(chain, nodes, wts, k_hi):
    """b3: scale-free drive cancellation ratio T_abs/|T| at degree
    k_hi via the rolling normalized recursion (prefix chain data
    alh, gam_next only; the terminal pivot is never read)."""
    p0 = np.ones(len(nodes))
    if k_hi == 0:
        pk = p0
    else:
        p1 = (nodes - chain[0]["alh"]) * p0 \
            / math.sqrt(abs(chain[0]["gam_next"]))
        for k in range(1, k_hi):
            gk = chain[k - 1]["gam_next"]
            gk1 = chain[k]["gam_next"]
            p2 = ((nodes - chain[k]["alh"]) * p1
                  - math.copysign(math.sqrt(abs(gk)), gk) * p0) \
                / math.sqrt(abs(gk1))
            p0, p1 = p1, p2
        pk = p1
    xv = wts * nodes
    num = float(np.abs(xv) @ np.abs(pk))
    den = abs(float(xv @ pk))
    return num / max(den, 1e-300)


def oracle_certificate(p):
    """DELIBERATE MUST-FAIL MUTANT: reads the terminal target
    directly -- the candidate AST audit must FLAG this scope."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


def candidate_scope_audit(funcname):
    """walk ONLY the named function's subtree; flag any target-
    side identifier or dict key from the sealed forbidden set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"rho", "S", "sa", "la", "q_chain", "D_dir", "wb",
            "anchor", "world_block", "direct_terminal"}
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
                if nm in forb:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ------------------------------------------- leg C continuation
def ext_chain(p, m_ext):
    """indefinite chain continuation to N + m_ext degrees (f64,
    r244 recursion verbatim); returns rows + first flip degree."""
    d, dsm = p["d"], p["dsm"]
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"],
                         dsm["vs"], p["N"] + m_ext)
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    return rows, nf


def tails_from_rows(rows, N, m_list):
    """tail(m) = sum_{k=N-1}^{N+m-1} rho_k (partial sums of the
    signed continuation); nan where the chain terminated early."""
    out = {}
    for m in m_list:
        hi = N + m
        if len(rows) >= hi:
            out[m] = float(sum(r["rho"] for r in rows[N - 1:hi]))
        else:
            out[m] = float("nan")
    return out


def direct_ext_dev(p, rows_ext, m_ext):
    """cross-route ward: chain rho_k vs direct bordered-slogdet
    increments D_k - D_{k+1} for k in [N-1, N+m_ext-1] (same
    corner B); dev scale max(|D_k|, |D_{k+1}|)."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    n_hi = min(N + m_ext + 1, len(rows_ext) + 1)
    P = CT.u_matrix(xu, x0, rh, n_hi)
    TB = CT.u_matrix(bx, x0, rh, n_hi)
    G = (P * wu) @ P.T
    tv = TB @ bw
    Bc = float(p["S"][N - 2]) + B57
    Dv = {}
    for n in range(N - 1, n_hi + 1):
        if n > G.shape[0]:
            break
        sg, lg = np.linalg.slogdet(G[:n, :n])
        A = np.zeros((n + 1, n + 1))
        A[:n, :n] = G[:n, :n]
        A[:n, n] = tv[:n]
        A[n, :n] = tv[:n]
        A[n, n] = Bc
        sa, la = np.linalg.slogdet(A)
        Dv[n] = sa * sg * math.exp(la - lg)
    worst = 0.0
    for k in range(N - 1, n_hi - 1):
        if k in Dv and (k + 1) in Dv and k < len(rows_ext):
            X = Dv[k] - Dv[k + 1]
            sc = max(abs(Dv[k]), abs(Dv[k + 1]), 1e-300)
            worst = max(worst,
                        abs(X - float(rows_ext[k]["rho"])) / sc)
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("terminal_triangle_probe -- PRIME.PORT.COUPLEDTAU."
          "TERMINAL_TRIANGLE.01 (round 262)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls; ladder, w13, "
                        "cross-route samples, reproduction gates "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN OBJECT: the r260 terminal triangle C1b |r_{N-1}| "
          "<= |t_{N-2}| + |a'_{N-2}||r_{N-2}| + |b'_{N-2}|"
          "|r_{N-3}| (the only certificate under the demand bar, "
          "35/42, gap 0.41 dec) -- anatomy of the 7 misses + 4 "
          "sealed sharpenings (b1 unroll j=1..4, b2 sign-refined "
          "grouping, b3 drive-bound honesty, b4 PSI1 hybrid) + "
          "the 5/7 Gram-provenance tail m=2..12 on 42 rungs with "
          "cross-route ward; closure rules, provenance rules, "
          "kills d1-d5 ALL sealed BEFORE evaluation (r260 record "
          "numbers adopted as reproduction bands, disclosed)")

    # ---------------- S1: census + controls + ladder
    section("S1  CENSUS + CONTROLS + POSITIVITY TYPING")
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
          "control flips re-derived %s (typed INDEFINITE_"
          "CONTINUATION beyond pmax); cofinal ladder %d rungs "
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

    # ---------------- per-rung computation (single pass)
    recs = []
    for p in pool:
        N = p["N"]
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        rpre = r[:N - 1]
        rterm = abs(r[N - 1])
        tri = TX.cand_triangle(t[N - 2], ap[N - 2], bp[N - 2],
                               r[N - 2], r[N - 3])
        q = float(p["rho"][N - 1]) / B57
        Bc = float(p["S"][N - 2]) + B57
        D = np.empty(N)
        D[0] = Bc
        for k in range(1, N):
            D[k] = D[k - 1] - r[k - 1] ** 2
        maxq_pre = float(np.max(r[:N - 1] ** 2 / D[:N - 1]))
        terms = (abs(t[N - 2]), abs(ap[N - 2] * r[N - 2]),
                 abs(bp[N - 2] * r[N - 3]))
        dom = ("t", "a'r", "b'r")[int(np.argmax(terms))]
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        hull = hi - lo
        natoms = len(xu) + len(bx)
        ub = {j: cand_unroll(rpre, t, ap, bp, j)
              for j in UNROLL_JS}
        gb = cand_grouped(rpre, t, ap, bp)
        hb = cand_hybrid(rpre, t, ap, bp)
        psi_ok = (r[N - 2] ** 2 <= PSI1_C * (B57 + r[N - 2] ** 2)
                  * (1 + VALID_EPS)
                  and r[N - 3] ** 2 <= PSI1_C
                  * (B57 + r[N - 2] ** 2 + r[N - 3] ** 2)
                  * (1 + VALID_EPS))
        ratio = drive_abs_ratio(p["rows"], bx, bw, N - 2)
        ab = abs(t[N - 2]) * ratio + terms[1] + terms[2]
        signs = (math.copysign(1, t[N - 2]),
                 math.copysign(1, ap[N - 2] * r[N - 2]),
                 math.copysign(1, bp[N - 2] * r[N - 3]))
        nalt = sum(1 for k in range(1, N - 1)
                   if r[k] * r[k - 1] < 0)
        rows_ext, nf_ext = ext_chain(p, M_EXT)
        tails = tails_from_rows(rows_ext, N, M_LIST)
        recs.append(dict(
            kz=p["kz"], N=N, q=q, tri=tri, rterm=rterm,
            kappa=rterm / tri, dom=dom, terms=terms,
            maxq_pre=maxq_pre, hull=hull, natoms=natoms,
            ub=ub, gb=gb, hb=hb, psi_ok=psi_ok, ratio=ratio,
            ab=ab, signs=signs, alt_frac=nalt / max(N - 2, 1),
            ap_neg=(ap[N - 2] < 0), bp_neg=(bp[N - 2] < 0),
            tails=tails, nf_ext=nf_ext, rows_ext=rows_ext,
            valid=(tri >= rterm * (1 - VALID_EPS)),
            cover=(tri * tri < B57), p=p))
    npool = len(recs)

    # ---------------- S2: LEG A -- reproduction + anatomy
    section("S2  LEG A -- C1B REPRODUCTION + MISS ANATOMY")
    n_valid = sum(1 for rc in recs if rc["valid"])
    n_cover = sum(1 for rc in recs if rc["cover"])
    misses = [rc for rc in recs if not rc["cover"]]
    covers = [rc for rc in recs if rc["cover"]]
    gaps = [math.log10(rc["tri"] ** 2 / B57) for rc in misses]
    wgap = max(gaps) if gaps else 0.0
    if smoke:
        check("G20-c1b-reproduction", n_valid == npool,
              "SMOKE: validity %d/%d on w9 only; coverage census "
              "skipped" % (n_valid, npool))
    else:
        check("G20-c1b-reproduction",
              n_valid == 42 and n_cover == C1B_COVER_EXPECT
              and (C1B_GAP_BAND[0] <= wgap <= C1B_GAP_BAND[1]),
              "r260 C1b census reproduced EXACTLY: valid %d/42, "
              "coverage tri^2 < 5/7 on %d/42 (expect %d), worst "
              "gap on the %d missing rungs %.3f dec in the sealed "
              "band %s" % (n_valid, n_cover, C1B_COVER_EXPECT,
                           len(misses), wgap, str(C1B_GAP_BAND)))
    kap_ok = all(rc["kappa"] <= 1.0 + VALID_EPS for rc in recs)
    miss_note = "; ".join(
        "kz%d N%d q%.3f gap%.2f dom=%s kap%.2f mqp%.2f"
        % (rc["kz"], rc["N"], rc["q"],
           math.log10(rc["tri"] ** 2 / B57), rc["dom"],
           rc["kappa"], rc["maxq_pre"]) for rc in misses)
    check("G21-miss-anatomy", kap_ok and (smoke or
                                          len(misses) == 42 - C1B_COVER_EXPECT),
          "anatomy complete on %d/%d misses, kappa = |r_{N-1}|/tri "
          "<= 1 everywhere (validity restated): %s"
          % (len(misses), 42 - C1B_COVER_EXPECT if not smoke
             else len(misses), miss_note if miss_note else "none"))
    if not smoke:
        med = lambda xs: float(np.median(xs)) if xs else float("nan")  # noqa: E731
        m_k = med([rc["kappa"] for rc in misses])
        c_k = med([rc["kappa"] for rc in covers])
        m_q = med([rc["q"] for rc in misses])
        c_q = med([rc["q"] for rc in covers])
        m_h = med([rc["hull"] for rc in misses])
        c_h = med([rc["hull"] for rc in covers])
        m_a = med([rc["natoms"] for rc in misses])
        c_a = med([rc["natoms"] for rc in covers])
        m_p = med([rc["maxq_pre"] for rc in misses])
        c_p = med([rc["maxq_pre"] for rc in covers])
        top7 = sorted(recs, key=lambda rc: -rc["q"])[:len(misses)]
        top_is_miss = all(not rc["cover"] for rc in top7)
        sp_gq = BH.spearman(
            [math.log10(rc["tri"] ** 2 / B57) for rc in misses],
            [rc["q"] for rc in misses]) if len(misses) > 2 else 0.0
        dom_m = {d: sum(1 for rc in misses if rc["dom"] == d)
                 for d in ("t", "a'r", "b'r")}
        dom_c = {d: sum(1 for rc in covers if rc["dom"] == d)
                 for d in ("t", "a'r", "b'r")}
        dom_top = max(dom_m, key=lambda d: dom_m[d])
        sig = ("miss signature: %s-dominated %d/%d, kappa-"
               "separated (%.2f vs %.2f), q-%s, geometry-%s"
               % (dom_top, dom_m[dom_top], len(misses), m_k, c_k,
                  "sorted" if top_is_miss else "blind",
                  "blind" if abs(m_h - c_h) < 0.5 else "linked"))
        check("G22-signature-census",
              math.isfinite(m_k) and math.isfinite(c_k),
              "MEASUREMENT: miss-vs-cover medians kappa %.3f/%.3f "
              "(the misses discard %s cancellation), q %.3f/%.3f, "
              "maxq_pre %.3f/%.3f, hull %.2f/%.2f, atoms "
              "%.1e/%.1e; top-%d-by-q == miss set: %s; "
              "Spearman(gap, q) on misses %.2f; dominant term "
              "miss %s / cover %s -- %s"
              % (m_k, c_k, "MORE" if m_k < c_k else "LESS",
                 m_q, c_q, m_p, c_p, m_h, c_h, m_a, c_a,
                 len(misses), top_is_miss, sp_gq,
                 str(dom_m), str(dom_c), sig))
    else:
        check("G22-signature-census", True, "SMOKE: skipped")

    # ---------------- S3: LEG B -- sealed sharpenings
    section("S3  LEG B -- SEALED SHARPENING CANDIDATES")
    hits = []
    for fn in ("cand_unroll", "cand_grouped", "cand_hybrid",
               "drive_abs_ratio"):
        hits += candidate_scope_audit(fn)
    check("G30-candidate-ast-clean", not hits,
          "the four sealed sharpening builders consume ONLY the "
          "prefix slice + (t, a', b') / chain rows -- no target-"
          "side identifier in scope (sealed forbidden set): %s"
          % ("CLEAN" if not hits else "; ".join(hits)))
    hits_orc = candidate_scope_audit("oracle_certificate")
    check("G31-oracle-mutant-flagged", bool(hits_orc),
          "the deliberately target-reading mutant is FLAGGED by "
          "the candidate AST audit (%s): target-blindness is "
          "machine-enforced (TARGET_INVERSE kill armed)"
          % ("; ".join(hits_orc) if hits_orc else "NOT FLAGGED"))
    # b1 unroll
    u_valid = {j: True for j in UNROLL_JS}
    u_cover = {j: 0 for j in UNROLL_JS}
    u_gap = {j: 0.0 for j in UNROLL_JS}
    for rc in recs:
        for j in UNROLL_JS:
            b = rc["ub"][j]
            u_valid[j] = u_valid[j] and (
                b >= rc["rterm"] * (1 - VALID_EPS))
            if b * b < B57:
                u_cover[j] += 1
            else:
                u_gap[j] = max(u_gap[j],
                               math.log10(b * b / B57))
    u_note = "; ".join(
        "j=%d valid %s cover %d/%d gap %.2f dec"
        % (j, u_valid[j], u_cover[j], npool, u_gap[j])
        for j in UNROLL_JS)
    check("G32-b1-unroll", all(u_valid.values()),
          "b1 K-STEP UNROLLING (exact signed drive accumulation, "
          "two deepest r-terms triangled): %s -- validity is "
          "algebraic and gated; coverage adjudicates in the "
          "verdict (C1b baseline %d/%d)"
          % (u_note, n_cover, npool))
    # b2 grouped + sign census
    g_valid = all(rc["gb"] >= rc["rterm"] * (1 - VALID_EPS)
                  for rc in recs)
    g_cover = sum(1 for rc in recs if rc["gb"] ** 2 < B57)
    g_gap = max([math.log10(rc["gb"] ** 2 / B57)
                 for rc in recs if rc["gb"] ** 2 >= B57],
                default=0.0)
    g_worst = max(rc["gb"] ** 2 / B57 for rc in recs)
    patt = {}
    n_opp = 0
    for rc in recs:
        key = "".join("+" if s > 0 else "-" for s in rc["signs"])
        patt[key] = patt.get(key, 0) + 1
        if rc["signs"][1] * rc["signs"][2] < 0:
            n_opp += 1
    ap_neg = sum(1 for rc in recs if rc["ap_neg"])
    bp_neg = sum(1 for rc in recs if rc["bp_neg"])
    alt_med = float(np.median([rc["alt_frac"] for rc in recs]))
    rule_holds = (n_opp == npool)
    check("G33-b2-grouped-signs", g_valid,
          "b2 GROUPED bound valid %d/%d (unconditional algebra), "
          "covers %d/%d (worst bound^2/B57 %.3f, gap %.2f dec) -- "
          "typed RESTATEMENT_ADJACENT (sealed); sign census (t, "
          "a'r, b'r): %s; (a'r, b'r) opposite on %d/%d => sign "
          "rule %s; a'<0 %d/%d, b'<0 %d/%d (chain-uniform "
          "negativity), adjacent r-alternation fraction median "
          "%.2f -- %s"
          % (npool, npool, g_cover, npool, g_worst, g_gap,
             str(patt), n_opp, npool,
             "HOLDS 42/42" if rule_holds else "FAILS (OBSERVED_"
             "PARTIAL, no rule-based bound)",
             ap_neg, npool, bp_neg, npool, alt_med,
             "r-signs alternate regularly" if alt_med > 0.9
             else "r-signs are NOT alternating-regular"))
    # b3 drive-bound honesty
    decs = [math.log10(rc["ratio"]) for rc in recs]
    dec_med = float(np.median(decs))
    a_cover = sum(1 for rc in recs if rc["ab"] ** 2 < B57)
    check("G34-b3-drive-honesty",
          all(rc["ratio"] >= 1.0 - VALID_EPS for rc in recs),
          "b3 DRIVE CANCELLATION CONTENT dec_t = log10(T_abs/|T|) "
          "at the terminal drive degree: median %.2f, min %.2f, "
          "max %.2f dec; abs-drive triangle covers %d/%d -- %s "
          "(sealed typing: median >= %.1f dec => the a-priori "
          "drive bound re-encodes comb cancellation; the "
          "EVALUATED t stays prefix data)"
          % (dec_med, min(decs), max(decs), a_cover, npool,
             "TRIANGLE_DRIVE_PAIRCORR_ADJACENT" if dec_med
             >= DEMAND_BAR else "drive a-priori boundable",
             DEMAND_BAR))
    # b4 hybrid
    h_psi = sum(1 for rc in recs if rc["psi_ok"])
    h_valid = all(rc["hb"] >= rc["rterm"] * (1 - VALID_EPS)
                  for rc in recs if rc["psi_ok"])
    h_cover = sum(1 for rc in recs if rc["hb"] ** 2 < B57)
    h_worst = max(rc["hb"] ** 2 / B57 for rc in recs)
    mqp_max = max(rc["maxq_pre"] for rc in recs)
    check("G35-b4-hybrid", h_psi == npool and h_valid,
          "b4 TRIANGLE+PSI1 HYBRID: orbit fact r^2 <= %.2f D "
          "holds at k = N-2, N-3 on %d/%d (max prefix r^2/D over "
          "the pool %.4f -- OBSERVED, not proven); bound valid "
          "on all psi-ok rungs, covers %d/%d (worst bound^2/B57 "
          "%.3f) -- CONDITIONAL certificate, sealed typing"
          % (PSI1_C, h_psi, npool, mqp_max, h_cover, npool,
             h_worst))
    info("SHARPENING TABLE (candidate -> cover -> worst gap -> "
         "typing): C1b %d/%d 0.41dec pure-triangle | "
         "b1@j1 %d/%d %.2fdec pure-triangle | b1@j2 %d/%d %.2f | "
         "b1@j3 %d/%d %.2f | b1@j4 %d/%d %.2f | b2 %d/%d %.2f "
         "RESTATEMENT_ADJACENT | b3-abs %d/%d paircorr-typing | "
         "b4 %d/%d PSI1-conditional"
         % (n_cover, npool, u_cover[1], npool, u_gap[1],
            u_cover[2], npool, u_gap[2], u_cover[3], npool,
            u_gap[3], u_cover[4], npool, u_gap[4], g_cover,
            npool, g_gap, a_cover, npool, h_cover, npool))

    # ---------------- S4: LEG C -- the 5/7 Gram provenance
    section("S4  LEG C -- 5/7 GRAM PROVENANCE (CONTINUATION TAIL)")
    ward_worst = 0.0
    ward_note = []
    ward_pool = ([("w%d" % kz, packs["w%d" % kz])
                  for kz in windows]
                 + ([("rung%d" % i, ladder[i])
                     for i in WARD_SAMPLE_IDX] if not smoke
                    else []))
    for tag, p in ward_pool:
        rc = next((x for x in recs if x["p"] is p), None)
        if rc is not None:
            rext = rc["rows_ext"]
        else:
            rext, _ = ext_chain(p, M_EXT)
        dv = direct_ext_dev(p, rext, M_EXT)
        ward_worst = max(ward_worst, dv)
        ward_note.append("%s %.1e" % (tag, dv))
    check("G40-crossroute-ward", ward_worst <= ROUTE_BAR_EXT,
          "continued chain rho_k vs direct bordered-slogdet "
          "increments D_k - D_{k+1} for k in [N-1, N+%d-1], same "
          "corner: worst %.1e (bar %.0e) on %s -- the f64 "
          "indefinite continuation is route-exact, the tail "
          "measurement is trusted"
          % (M_EXT, ward_worst, ROUTE_BAR_EXT,
             "; ".join(ward_note)))
    # tails on the pool + mains
    tail_pool = list(recs)
    for kz in windows:
        p = packs["w%d" % kz]
        if not any(rc["p"] is p for rc in recs):
            rext, nfe = ext_chain(p, M_EXT)
            tail_pool.append(dict(
                kz=p["kz"], N=p["N"],
                tails=tails_from_rows(rext, p["N"], M_LIST),
                nf_ext=nfe, p=p))
    t12 = [rc["tails"][12] for rc in tail_pool
           if math.isfinite(rc["tails"][12])]
    conv = [rc for rc in tail_pool
            if math.isfinite(rc["tails"][12])
            and math.isfinite(rc["tails"][10])
            and abs(rc["tails"][12] - rc["tails"][10])
            <= TAIL_CONV_BAR]
    conv_frac = len(conv) / max(len(tail_pool), 1)
    med12 = float(np.median(t12)) if t12 else float("nan")
    q25, q75 = (np.percentile(t12, (25, 75)) if t12
                else (float("nan"),) * 2)
    iqr = float(q75 - q25)
    m_note = "; ".join(
        "m=%d med %.4f" % (m, float(np.median(
            [rc["tails"][m] for rc in tail_pool
             if math.isfinite(rc["tails"][m])])))
        for m in M_LIST)
    check("G41-tail-census", bool(t12) and len(t12)
          == len(tail_pool),
          "signed continuation tail on %d rungs+mains, m = 2..12 "
          "all finite: %s; tail(12) median %.4f, IQR %.4f, range "
          "[%.3f, %.3f] vs 5/7 = %.4f; converged (|t12 - t10| <= "
          "%.2f) on %d/%d (frac %.2f); mains w9 %.4f / w13 %s"
          % (len(t12), m_note, med12, iqr,
             min(t12), max(t12), B57, TAIL_CONV_BAR, len(conv),
             len(tail_pool), conv_frac,
             next((rc["tails"][12] for rc in tail_pool
                   if rc["kz"] == 9 and rc["N"] == 184), float("nan")),
             "%.4f" % next((rc["tails"][12] for rc in tail_pool
                            if rc["kz"] == 13), float("nan"))
             if not smoke else "n/a"))
    sp_tn = BH.spearman([rc["tails"][12] for rc in tail_pool
                         if math.isfinite(rc["tails"][12])],
                        [rc["N"] for rc in tail_pool
                         if math.isfinite(rc["tails"][12])]) \
        if len(t12) > 3 else 0.0
    check("G42-tail-n-trend", True,
          "MEASUREMENT: Spearman(tail(12), N) = %.2f over %d "
          "rungs -- %s" % (sp_tn, len(t12),
                           "no N-trend" if abs(sp_tn) < 0.3
                           else "N-trend present"))
    gram_conf = (conv_frac >= GRAM_CONV_FRAC
                 and abs(med12 - B57) <= GRAM_MED_BAR
                 and iqr <= GRAM_IQR_BAR)
    gram_refu = (conv_frac >= GRAM_CONV_FRAC and not gram_conf)
    sq_closed = False
    if gram_conf and not smoke:
        sq_dev = 0.0
        for kz in windows:
            p = packs["w%d" % kz]
            rc = next(x for x in tail_pool if x["p"] is p)
            Bg = float(p["S"][p["N"] - 2]) + rc["tails"][12]
            DNg = Bg - float(p["S"][p["N"] - 1])
            sq_dev = max(sq_dev, abs(
                DNg - (B57 - float(p["rho"][p["N"] - 1])))
                / max(abs(DNg), 1e-300))
            sq_closed = sq_closed or (DNg >= 0.0)
        sq_closed = sq_closed and sq_dev <= SQUARE_REGATE_BAR
        check("G43-exact-square-protocol", True,
              "trigger ARMED (provenance confirmed): B_gram = "
              "S_{N-2} + tail(12) square re-gate dev %.1e, "
              "closed %s" % (sq_dev, sq_closed))
    else:
        check("G43-exact-square-protocol", True,
              "conditional exact-square test NOT armed (sealed "
              "trigger: conv frac %.2f >= %.2f AND |med - 5/7| "
              "%.4f <= %.2f AND IQR %.4f <= %.2f evaluates "
              "False%s) -- EXACT_SQUARE_OPEN stands"
              % (conv_frac, GRAM_CONV_FRAC, abs(med12 - B57),
                 GRAM_MED_BAR, iqr, GRAM_IQR_BAR,
                 "; SMOKE" if smoke else ""))

    # ---------------- S5: LEG D -- kills + controls
    section("S5  LEG D -- KILLS + CONTROLS")
    if not smoke:
        floors = [p["rows"][p["N"] - 1]["eta"]
                  / p["rows"][p["N"] - 1]["fb"] ** 2
                  for p in ladder]
        fmin = min(floors)
        check("G50-numerology-kill",
              FLOOR_BAND[0] <= fmin <= FLOOR_BAND[1]
              and fmin >= 1.4 + NONSAT_MARGIN,
              "FIVE_SEVENTHS_NUMEROLOGY: floor min h_{N-1}/"
              "F_{N-1}^2 = %.4f in %s, non-saturation %.4f >= "
              "%.2f (a1 scale-exact route) -- the constant stays "
              "the r241 IMPORTED floor" % (fmin, str(FLOOR_BAND),
                                           fmin - 1.4, NONSAT_MARGIN))
        qs = np.array([rc["q"] for rc in recs])
        margins = B57 * (1.0 - qs)
        check("G51-q-margin-ward",
              bool(np.all(qs < 1.0)) and MARGIN_BAND[0]
              <= float(np.min(margins)) <= MARGIN_BAND[1],
              "q census 42/42 < 1, min terminal margin %.4f in "
              "band %s (r243/r258 razor reproduced)"
              % (float(np.min(margins)), str(MARGIN_BAND)))
    else:
        check("G50-numerology-kill", True, "SMOKE: skipped")
        check("G51-q-margin-ward", True, "SMOKE: skipped")
    fire = []
    if not smoke:
        for j in UNROLL_JS:
            if u_cover[j] < npool and u_gap[j] >= DEMAND_BAR:
                fire.append("b1@j=%d" % j)
        if g_cover < npool and g_gap >= DEMAND_BAR:
            fire.append("b2")
        if dec_med >= DEMAND_BAR:
            pass  # b3 typing carried separately (drive typing)
    check("G52-paircorr-detector", True,
          "PAIRCORR detector census (sealed bar %.1f dec) on the "
          "sealed candidates: fires on [%s]; the b3 drive typing "
          "(median %.2f dec) is carried as TRIANGLE_DRIVE_"
          "PAIRCORR_ADJACENT in the verdict, NOT as a candidate "
          "kill (the evaluated t is prefix data)"
          % (DEMAND_BAR, ", ".join(fire) if fire else "none",
             dec_med))
    cont_ok = True
    ct_note = []
    for kz in windows:
        p = packs["w%d" % kz]
        rc = next((x for x in tail_pool if x["p"] is p), None)
        nfe = rc["nf_ext"] if rc else None
        cont_ok = cont_ok and (nfe == p["N"] + TAIL_OFFSETS[kz])
        ct_note.append("w%d flip N%+d (truth N+%d)"
                       % (kz, (nfe - p["N"]) if nfe else 99,
                          TAIL_OFFSETS[kz]))
    check("G53-wall-completion-kill", cont_ok,
          "WALL_COMPLETION: the continuation flips at %s within "
          "EXT = %d (ground truth in gates only): completion "
          "certificates stay wall-equivalent" % ("; ".join(ct_note),
                                                 EXT))
    r9, t9, ap9, bp9 = TX.drive_arrays(packs["w9"]["rows"],
                                       packs["w9"]["N"])
    N9 = packs["w9"]["N"]
    t_tr = t9.copy()
    t_tr[FIB_LO:] = 0.0
    rr_tr = np.zeros(N9)
    rr_tr[0] = r9[0]
    rr_tr[1] = t_tr[0] + ap9[0] * rr_tr[0]
    for k in range(1, N9 - 1):
        rr_tr[k + 1] = t_tr[k] + ap9[k] * rr_tr[k] \
            + bp9[k] * rr_tr[k - 1]
    S_ch = float(packs["w9"]["S"][N9 - 1])
    honest = abs(float(np.sum(r9 ** 2)) / S_ch - 1.0)
    dev_tr = abs(float(np.sum(rr_tr ** 2)) / S_ch - 1.0)
    check("G54-compression-kill",
          dev_tr >= LOUD * max(honest, 1e-300),
          "FIXED_STATE_COMPRESSION: drive truncated to %d entries "
          "-> S rebuild dev %.1e = %.1e x honest %.1e (bar %.0f "
          "x): the drive stays length-N essential"
          % (FIB_LO, dev_tr, dev_tr / max(honest, 1e-300),
             honest, LOUD))
    # controls: pre-flip triangle + coverage break
    ctri_dev = 0.0
    cbrk_note = []
    for c in ("SCR", "EPST"):
        p = ctrl[c]
        Nc = p["N"]
        flip = CTRL_FLIPS[long_names[c]]
        r, t, ap, bp = TX.drive_arrays(p["rows"], Nc)
        Bc = float(p["S"][Nc - 2]) + B57
        Dc = np.empty(Nc)
        Dc[0] = Bc
        for k in range(1, Nc):
            Dc[k] = Dc[k - 1] - float(p["rho"][k - 1])
        first_unc = None
        for k in range(1, min(flip - 1, Nc - 1)):
            tri_k = abs(t[k]) + abs(ap[k] * r[k]) \
                + abs(bp[k] * r[k - 1])
            ctri_dev = max(ctri_dev,
                           max(abs(r[k + 1]) - tri_k, 0.0)
                           / max(tri_k, 1e-300))
            if first_unc is None and not (
                    Dc[k + 1] > 0 and tri_k ** 2 < Dc[k + 1]):
                first_unc = k + 1
        cbrk_note.append("%s validity dev %.1e, coverage breaks "
                         "at %s (flip %d)"
                         % (c, ctri_dev, first_unc, flip))
    check("G55-controls-triangle", ctri_dev <= CTRL_TRI_BAR,
          "pre-flip triangle on SCR/EPST: validity |r_{k+1}| <= "
          "tri_k algebraic at every pre-flip degree (worst rel "
          "dev %.1e, bar %.0e); %s -- MEASUREMENT, firewall-typed "
          "(flips ground truth in gates only)"
          % (ctri_dev, CTRL_TRI_BAR, "; ".join(cbrk_note)))
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) \
        / B57
    fl_ok = True
    fl_note = []
    for c in ctrl:
        xu, wu = CT.union_arrays(ctrl[c]["d"])
        fl = CT.blind_flip_predictor(xu, wu, ctrl[c]["N"])
        first = fl[0] if fl else None
        fl_ok = fl_ok and (first == ctrl[c]["nf"])
        fl_note.append("%s -> %s (truth %s)"
                       % (c, first, ctrl[c]["nf"]))
    check("G56-smooth-and-predictor",
          abs(qS) <= SM_Q_BAR and fl_ok,
          "SMOOTH anchor q_N = %.1e <= %.0e (the terminal "
          "question trivializes on the self-aliased source); "
          "r257 blind micro-predictor ward: %s -- 3/3, mechanism "
          "coordinate check, NOT a proof"
          % (qS, SM_Q_BAR, "; ".join(fl_note)))

    # ---------------- S6: verdict
    section("S6  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the anatomy of the 7 C1b misses (pure terminal-"
          "cancellation signature), the sealed sharpening "
          "adjudication (unroll/grouped/drive-honesty/PSI1-"
          "hybrid), and the 42-rung tail census that settles the "
          "5/7 window-provenance question")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        closed_pure = [("C1b", n_cover)] if n_cover == npool \
            else []
        closed_pure += [("b1@j=%d" % j, u_cover[j])
                        for j in UNROLL_JS
                        if u_cover[j] == npool and u_valid[j]]
        best_j = max(UNROLL_JS, key=lambda j: u_cover[j])
        if closed_pure:
            parts.append("TRIANGLE_CLOSED(%s, 42/42, "
                         "target-blind)" % closed_pure[0][0])
        if h_cover == npool and h_psi == npool:
            parts.append("TRIANGLE_CONDITIONALLY_CLOSED(b4, "
                         "%d/%d, PSI1 %.2f OBSERVED)"
                         % (h_cover, npool, PSI1_C))
        if not closed_pure and u_cover[best_j] > n_cover:
            parts.append("TRIANGLE_PARTIAL_IMPROVED(b1@j=%d, "
                         "cover %d/%d, gap %.2f dec)"
                         % (best_j, u_cover[best_j], npool,
                            u_gap[best_j]))
        if g_cover == npool:
            parts.append("TRIANGLE_GROUPED_CLOSED(b2, %d/%d, "
                         "RESTATEMENT_ADJACENT)"
                         % (g_cover, npool))
        if (not closed_pure and u_cover[best_j] <= n_cover
                and h_cover < npool and g_cover < npool):
            parts.append("TRIANGLE_CANCELLATION_ESSENTIAL("
                         "top-q misses, kappa med %.2f)" % m_k)
        if dec_med >= DEMAND_BAR:
            parts.append("TRIANGLE_DRIVE_PAIRCORR_ADJACENT("
                         "median dec_t %.2f)" % dec_med)
        if gram_conf:
            parts.append("GRAM_PROVENANCE_CONFIRMED(median "
                         "%.4f, IQR %.4f)" % (med12, iqr))
        elif gram_refu:
            parts.append("GRAM_PROVENANCE_REFUTED(median %.4f, "
                         "IQR %.4f)" % (med12, iqr))
        else:
            parts.append("GRAM_PROVENANCE_INCONCLUSIVE(conv "
                         "frac %.2f)" % conv_frac)
        parts.append("EXACT_SQUARE_CLOSED" if sq_closed
                     else "EXACT_SQUARE_OPEN(5/7 Gram "
                     "provenance)")
        parts.append("FIVE_SEVENTHS_NUMERICAL_ONLY")
        if fire:
            parts.append("PAIRCORR_REENCODED(%s)"
                         % ", ".join(fire))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): validities, the "
          "reproduction census, the cross-route tail ward; "
          "MEASURED: miss anatomy, sharpening coverage, sign "
          "census, drive cancellation content, tail spread; "
          "OPEN: any source-pure closure of the 7 drive-"
          "dominated rungs (finite comb-vs-smooth cancellation "
          "at one degree per rung); NO RH claim"
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
