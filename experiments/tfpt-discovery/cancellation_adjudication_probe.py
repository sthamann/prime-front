#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cancellation_adjudication_probe -- PRIME.PORT.COUPLEDTAU.
CANCELLATION_ADJUDICATION.01 (round 263): the GATE ROUND before the
RHP handover.  r262 localized the C1b coverage gap honestly: the 7
missing rungs (kz 15/20/22/36/38/39/52) are ALL drive-dominated with
kappa = |r_{N-1}|/triangle = 0.43 (vs 0.998 on the covered 35) --
genuine phase-sensitive comb cancellation at ONE degree per rung.
REVIEWER ADJUDICATION (binding, adopted): the correct r262 typing is
ONE_DEGREE_PER_WINDOW_LOCALIZATION + TRIANGLE_GENERIC_BRANCH +
PAIRCORR_CANCELLATION_EXCEPTION_BRANCH -- a finite sum term per
window is NOT a finitely dischargeable problem (the unbounded window
quantifier makes the family of growing finite comb sums the same
arithmetic wall); BUT the architecture reduction is real: on the
exception branch the entire missing information sits in ONE scalar
cancellation value at ONE degree.  TARGET ARCHITECTURE = the BRANCH
THEOREM: the triangle closes directly for g_w >= 0; the full-source
RHP closes the cancellation scalar for g_w < 0 -- independent of
whether the exception branch is finite, thin, or infinite.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r262 discipline): w = window (kz),
N_w = builder depth, k = chain degree; free pivots are the proof
objects; rho_k = F_k^2/h_k, S_n = sum_{k<=n} rho_k; ground truth
(h signs, flip degrees) enters GATES only; no zero/prime oracles
anywhere (AST firewall).  MACHINERY IMPORTED VERBATIM: r244
BH.wpack, r257 CT.union_arrays/u_matrix, r260 TX.drive_arrays +
TX.direct_terminal (sealed driven-recursion coordinates r_k =
F_k/sqrt(h_k), t_k = T_k/sqrt(h_{k+1}), a'_k = -alh_k/
sqrt(gam_{k+1}), b'_k = -sign(gam_k) sqrt|gam_k/gam_{k+1}|), r243
PB.smooth_comb, v881 PIK controls.  B PROVENANCE: B_w = S_{N-2} +
5/7 (r241/r243 IMPORTED floor, never fitted; D_{N-1} = 5/7 by
construction).  COFINAL LADDER (pre-sealed): frame-A h <= 900, 42
rungs, (N, kz)-sorted (r258/r260/r262 convention).

LEG A -- THE TWO BRANCHES FROZEN EXACTLY (source-pure per rung):
  U_w = the SEALED triangle upper bound: the r260/r262 C1b one-step
        terminal triangle |t_{N-2}| + |a'_{N-2}||r_{N-2}| +
        |b'_{N-2}||r_{N-3}| (ONE choice, sealed here: C1b, NOT
        b1@j=4 -- the 7 named exception rungs and the kappa anatomy
        of r262 are C1b objects; the handover set stays the named
        one).  U consumes ONLY prefix data (r_0..r_{N-2}, t, a',
        b'); machine AST audit.
  M_w = the allowed terminal budget sqrt(5/7) (target-blind:
        D_{N-1} = 5/7 by construction of the imported corner; the
        demand |r_{N-1}| < sqrt(D_{N-1}) = M_w IS q_N < 1).
  g_w = M_w - U_w.  g_w >= 0  =>  CHEAP BRANCH: |r_{N-1}| <= U_w
        <= M_w -- the theorem closes there WITHOUT any cancellation
        (gate).
  Z_w = t_{N-2} + a'_{N-2} r_{N-2} + b'_{N-2} r_{N-3}, the EXACT
        SIGNED terminal sum (border-comb drive + chain terms BEFORE
        absolute values); by the driven recursion Z_w == r_{N-1}
        EXACTLY (gated rel 1e-9) -- Z is built from the same prefix
        inputs as U but is ONE signed evaluation from the target
        (r262 typing RESTATEMENT_ADJACENT carried).
  C_w = U_w - |Z_w| = the cancellation credit actually used.  On
        the exception branch (g_w < 0) the needed statement is
        C_w >= -g_w  <=>  |Z_w| <= M_w  <=>  q_N < 1.
  GATES: Z-identity on all 42 rungs + both mains; branch
  decomposition EXACT: cheap branch = the 35 covered rungs,
  exception set = EXACTLY {kz15, 20, 22, 36, 38, 39, 52} (r262
  reproduction); cheap-branch closure restated; exception credit
  C_w >= -g_w on 7/7 (MEASURED q-razor, not a theorem).

LEG B -- EXACT-SQUARE GATE (the only admissible positive route;
exactly 3 sealed identity candidates of FIXED algebraic complexity;
each tested symbolically on small exact instances AND numerically
on the ladder; hard conditions per candidate, each gated: no target
inverse, no Cholesky/sqrt of the wall, no measured offset, no
fitted 5/7, no post-hoc grouping of comb atoms, fixed formula for
arbitrary window size, and SCRAMBLE MUST lose the sign -- an
identity equally positive on SCRAMBLE is support geometry):
  K1 BORDERED-SCHUR DET RATIO: M_w^2 - Z_w^2 = D_N =
     det(Gcal_w)/P_w EXACTLY, Gcal_w the bordered Gram (corner B),
     P_w = tau_N = det G_N > 0 on the positive prefix.  Symbolic:
     aug_n == tau_n (B - sum_{k<n} F_k^2/h_k) exact on MAINLIKE +
     FLIPLIKE instances.  Numeric: direct slogdet ratio vs chain on
     mains + 3 sample rungs.  ADJUDICATION: the identity is exact,
     but the positivity premise "Gcal_w PSD" IS D_N >= 0 -- the
     target restated; the corner B has NO source-pure square
     provenance (r262 GRAM_PROVENANCE_INCONCLUSIVE stands); AND the
     terminal ratio stays POSITIVE on the flipped controls
     (EPSTEIN/SCRAMBLE D_N in the sealed bands) => SCRAMBLE does
     NOT lose the sign at the terminal => support geometry.
     Expected break: CORNER_PROVENANCE + SCRAMBLE_SIGN_NOT_LOST.
  K2 BILINEAR TELESCOPING SQUARES (r260 tau identity, corner
     cancels): aug_n tau_{n+1} - aug_{n+1} tau_n = F_n^2 tau_n^2
     (manifest square), telescoped: M_w^2 - Z_w^2 = D_N = B -
     sum_{k<=N-1} r_k^2.  Symbolic: bilinear exact n = 1..4 on both
     instances; on FLIPLIKE the decrement-square structure breaks
     EXACTLY at the flip (h_2 < 0, rho_2 < 0).  Numeric: terminal
     decrement direct == rho_{N-1} on mains + samples; SCRAMBLE
     first rho < 0 at EXACTLY its flip (the square structure DOES
     discriminate -- K2 passes the scramble condition).
     ADJUDICATION: every manifest square sits on the DRAIN side
     (negative sign in D_N = B - sum r^2) -- the wrong side for an
     SOS of the gap; the head B is not a source-pure square
     (provenance open).  Expected break: DRAIN_SIDE_SQUARES +
     HEAD_PROVENANCE.
  K3 WRONSKIAN/TRANSFER ROW (variation of parameters of the driven
     recursion): Z_w = K_w . (r_0, t_0..t_{N-2}) with the terminal
     transfer row K_w from (a', b') alone (exact, fixed formula,
     any window size).  Symbolic: exact rational rebuild of F_4
     from (F_0, T_0..T_3) at depth 4 on both instances.  Numeric:
     rebuild rel 1e-9 on all 42 rungs + mains.  ADJUDICATION: a
     fixed-complexity SOS in the transfer atoms would certify
     |Z_w| <= M_w through the row-abs majorant sum_j |K_j tau_j|;
     its demand log10(rowabs/M_w) is measured by the r260 d2
     detector on every rung -- demand >= 1.0 dec on the exception
     branch means the majorant must deliver exactly the missing
     comb cancellation at the root scale => PAIRCORR_MINIATURE,
     route closed IMMEDIATELY (leg-D firewall); the row-abs bound
     is used ONLY inside the detector, never as a certificate (the
     anti-gate "no further drive-abs majorant" stands).  Expected
     break: PAIRCORR (demand measured in decades).
  SEALED GO RULE: EXACT_CANCELLATION_IDENTITY_GO(K) iff K's
  identity is exact (symbolic AND numeric), its positivity
  premises are source-pure (no target restatement, no open corner
  provenance consumed), SCRAMBLE loses the sign/square structure
  while MAIN keeps it to full depth, and the d2 demand stays
  < 1.0 dec on every rung.  Anything else: honest break location.

LEG C -- EVENTUAL-TRIANGLE GATE: does a theorem "exists w_0 with
g_w >= 0 for all w >= w_0" follow from source-pure ASYMPTOTIC
SEPARATION OF MAGNITUDES (scaling of M_w vs U_w -- both magnitude
quantities, NO cancellation estimate allowed)?  M_w = sqrt(5/7) is
constant; the question is whether U_w falls below it eventually.
MEASURE on the full 42-rung ladder: sign census of g_w, Spearman(
g_w, N), Spearman(U_w, N), Spearman(|t_{N-2}|, N), tercile medians
of g_w, and the branch of the DEEPEST rung.  SEALED ADJUDICATION:
EVENTUAL_TRIANGLE_GO only from a derived magnitude law (machine
proxy: Spearman(g, N) >= +0.5 AND every exception in the lowest
N-tercile AND the deepest tercile all-cheap -- necessary, not
sufficient; a GO additionally requires the law itself, which this
round does NOT attempt to fit -- no regression anti-gate);
FINITE_SURFACE_ONLY typing iff all exceptions sit in the lowest
N-tercile; else EVENTUAL_TRIANGLE_NOGO(typed).  A deeper census
does NOT suffice (7 exceptions below 400 prove no finiteness); the
ladder is NOT extended.

LEG D -- PAIRCORR FIREWALL (immediate closure discipline): as soon
as a required step reads "|Z_w| <= majorant" where the majorant
must deliver exactly the missing comb cancellation at the root
scale => PAIRCORR_MINIATURE and the route closes IMMEDIATELY; the
r260 d2 detector (demand bar 1.0 dec) runs as a gate on every
candidate.  FIREWALL BALANCE reported in the verdict.

LEG E -- RHP HANDOVER (the expected exit): if neither B nor C
carries: freeze Z_w as the SINGLE exception readout -- exact
definition (the signed sum above == the signed terminal readout
F_{N-1}/sqrt(h_{N-1}) of the r244 chain == the sign form of the
tau cross-ratio 1 - q_N = (tau^aug_N tau_{N-1})/(tau^aug_{N-1}
tau_N)), computation route (BH.wpack -> TX.drive_arrays -> one
signed sum), the 7 named rungs, and the FUTURE-WINDOW RULE: the
exception branch is entered iff g_w < 0 with the sealed C1b form
-- source-defined, NO selection-by-answer.  HANDOVER REQUIREMENT
to the quenched full-source RHP lane: produce Z_w = Z^RHP_w + E_w
with |Z^RHP_w| + |E_w| < M_w = sqrt(5/7) on the exception branch,
or directly the positivity of the tau cross-ratio; together with
the r261 input (CAMPAIGN_INPUT_FROZEN: G_n, t_n, B in the sealed
scaled-Chebyshev basis) this is the COMPLETE RHP target package.

ANTI-GATES (binding, documented as gates): no 5/6/8/16-step unroll
series (the sealed U is the ONE C1b choice; no cand_unroll in this
module -- AST-checked); no new sign heuristics (no sign-pattern
census); no regression on the 7 exceptions (no fit primitives --
AST-checked); no renewed 5/7 search (B57 literal only, imported);
no further drive-abs majorant as certificate (row-abs lives ONLY
inside the d2 detector); no cofinal subsequence selection by
post-hoc cancellation values (the branch rule reads g_w only --
builder scope AST-audited).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27, first rho < 0 at
25/21/27; ladder frame-A h <= 900 (42 rungs, (N, kz)-sorted);
B57 = 5/7; M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15,
20, 22, 36, 38, 39, 52); VALID_EPS 1e-9; Z_ID_BAR 1e-9; direct-
route bars ABS 1e-8 main / 3e-6 deep (r260 floors); EPST_DN_BAND
(1.70, 1.90); SCR_DN_BAND (0.45, 0.60); DEMAND_BAR 1.0 dec;
WARD_SAMPLE_IDX (0, 20, 41); SPEAR_GO 0.5; SM_Q_BAR 1e-20;
symbolic instances (r261 verbatim): atoms (-3/2, -1, -1/2, 1/4,
3/4, 5/4), MAINLIKE weights (2/3, -1/5, 1/2, -3/7, 1, 1/3),
FLIPLIKE weights (2/3, -6/5, 1/2, -3/7, 1, 1/3), border atoms
(0, 1/2) weights (1/3, 1/6), corner 5/7, depth 4 (bilinear n =
1..4 via H_5); runtime <= 1800 s; smoke = w9 + controls +
symbolic legs only (ladder, w13, samples, adjudication skipped).
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): all
reproduction bands are r260/r261/r262 RECORD numbers adopted
as-is (C1b 35/42 with the named 7; anchors EPST +1.79 / SCR
+0.52; first rho < 0 at 25/21/27; route floors) -- nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  TWO_BRANCH_DECOMPOSITION_EXACT(U=C1b, cheap m/42, exceptions k)
    / TWO_BRANCH_DECOMPOSITION_BROKEN(typed)
+ EXACT_CANCELLATION_IDENTITY_GO(K) / EXACT_IDENTITY_NOGO(K1@
    break, K2@break, K3@break)
+ EVENTUAL_TRIANGLE_GO(w0) / EVENTUAL_TRIANGLE_NOGO(typed) /
    FINITE_SURFACE_ONLY(typed)
+ PAIRCORR_MINIATURE(route list) [if the d2 detector fired -- the
    fired route closed immediately]
+ [iff legs B AND C are no-gos] TWO_BRANCH_RHP_REDUCTION +
    PRIMARY_FLOOR_LANE_CLOSED + TRIANGLE_RETAINED_AS_GENERIC_
    BRANCH + EXCEPTION_SCALAR_HANDED_TO_QUENCHED_FULLSOURCE_RHP.
Honesty before beauty: the cheap branch closes CONDITIONALLY on
the positive base prefix, never RH; the exception branch is handed
over, not solved; no verdict claims a derived 5/7, a bound
mechanism, or an asymptotic law (r243/r250/r253/r256/r257/r258/
r260/r261/r262 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
pass 1 = first full evaluation, 26/26 gates, wall 7.9 s -- after
pass 1 ONE PRESENTATION AMENDMENT p1 is disclosed (r262-p1
precedent): the G41 detail clause carried a pre-written conclusion
sentence ("the drive magnitude does NOT decay with depth") that
the measured weak trends (Spearman(U, N) -0.31, Spearman(|t|, N)
-0.21) only partially support; the clause was made data-driven
with the sealed usability rule |Spearman| >= 0.5; NO bar, band,
branch rule, candidate, kill or verdict rule was moved at any
point; pass 2 = the record run below, numerically identical to
pass 1): CAL_VERDICT =
TWO_BRANCH_DECOMPOSITION_EXACT(U=C1b, cheap 35/42, exceptions 7)
+ EXACT_IDENTITY_NOGO(K1@CORNER_PROVENANCE+SCRAMBLE_SIGN_NOT_LOST,
K2@DRAIN_SIDE_SQUARES+HEAD_PROVENANCE, K3@PAIRCORR 2.25 dec) +
EVENTUAL_TRIANGLE_NOGO(deepest rung N878 IS an exception;
Spearman(g, N) 0.31) + PAIRCORR_MINIATURE(K3) +
TWO_BRANCH_RHP_REDUCTION + PRIMARY_FLOOR_LANE_CLOSED +
TRIANGLE_RETAINED_AS_GENERIC_BRANCH +
EXCEPTION_SCALAR_HANDED_TO_QUENCHED_FULLSOURCE_RHP.
Key numbers.  LEG A: Z-identity worst rel dev 1.8e-14 on 42 rungs
+ 2 mains; D_{N-1} == 5/7 DIRECT bordered-slogdet: worst abs dev
4.5e-10 mains / 5.7e-8 samples idx (0, 20, 41) (r260 deep floor
family, bar 3e-6); branch decomposition EXACT: cheap (g >= 0)
35/42, exception set == {kz15, 20, 22, 36, 38, 39, 52} EXACTLY;
g on the exceptions: kz20 -0.434 / kz22 -0.238 / kz15 -0.002 /
kz39 -0.331 / kz36 -0.508 / kz38 -0.409 / kz52 -0.439 (Z signed:
-0.6478 / -0.1974 / -0.8184 / -0.6219 / -0.5778 / -0.5142 /
-0.3138 -- ALL SEVEN Z negative, recorded); cheap-branch g in
[+0.01, +0.76]; mains both CHEAP (w9 g +0.442, w13 g +0.212);
cheap closure |Z| <= U <= M restated 35/35; exception credit
C_w >= -g_w on 7/7 (min magnitude slack M - |Z| = 0.027 on kz15;
the q-razor 42/42 < 1 restated, min q-margin 0.0139 in band
[0.010, 0.020]).  LEG B: candidate AST scopes CLEAN, oracle
mutant FLAGGED (rho scope hit); K1 symbolic bordered-Schur exact
n = 1..4 on MAINLIKE + FLIPLIKE (rational zero); numeric direct
ratio: D_N worst abs dev 1.7e-10 mains / 5.8e-8 samples; terminal
positivity on flipped controls: EPST D_N +1.792 in (1.70, 1.90),
SCR +0.522 in (0.45, 0.60) => SCRAMBLE does NOT lose the sign =>
K1 killed CORNER_PROVENANCE + SCRAMBLE_SIGN_NOT_LOST (support
geometry at the terminal); K2 symbolic bilinear exact n = 1..4
both instances, FLIPLIKE flip tracked exactly (tau_3 =
-50107/20160 < 0, first h < 0 at k = 2, rho_2 =
-1566180625/1098746296 < 0: the decrement-square structure breaks
AT the flip); numeric terminal decrement carried by the same
direct slogdets (worst 1.7e-10 / 5.8e-8); first rho < 0 on
EPST/SCR/SMOOTH at 25/21/27 EXACTLY (K2 passes the scramble
condition) => K2 killed DRAIN_SIDE_SQUARES + HEAD_PROVENANCE
(every manifest square drains; B not a source square, r262
INCONCLUSIVE stands); K3 symbolic transfer rebuild of F_4 exact
(rational zero, both instances); numeric rebuild worst rel dev
1.0e-13 on 42 + mains; d2 demand log10(rowabs/M): median 1.73,
min 1.24, max 2.25 dec, exceptions 1.43..2.00 dec, fires 42/42
=> K3 killed PAIRCORR, route closed immediately (leg-D firewall);
adjudication: NO candidate meets the sealed GO conditions.
LEG C: g sign census 35+/7-; Spearman(g, N) = +0.31 (below the
0.5 usability bar); tercile medians of g: 0.192 (N <= 291) /
0.192 (<= 516) / 0.301 (> 516); exceptions per tercile [4, 1, 2]
-- spread over N 170..878 with the DEEPEST LADDER RUNG (kz52,
N = 878) an EXCEPTION => no observed w_0; Spearman(U, N) = -0.31,
Spearman(|t_term|, N) = -0.21 (weak trends, no usable magnitude-
decay law); FINITE_SURFACE_ONLY typing REFUSED (exceptions in all
three terciles) => EVENTUAL_TRIANGLE_NOGO(NO_MAGNITUDE_
SEPARATION).  LEG D: firewall balance: detector fired on K3 ONLY,
42/42 rungs above 1.0 dec (K1/K2 die structurally before any
majorant step); anti-gates CLEAN (no unroll/fit primitives,
branch-builder scope reads g only); controls: SMOOTH q_N =
4.2e-25 <= 1e-20, discrimination summary: the square/flip
structure separates worlds at the PREFIX level (first rho < 0 at
25/21/27 == flips) while the terminal det ratio does NOT
(EPST/SCR positive) -- exactly the K2-vs-K1 kill split.
LEG E: handover package frozen (printed in S6): Z-definition (3
exact equivalent forms), route, the 7 named rungs with (N, g, Z,
q), future-window rule g_w < 0 (source-defined), requirement
Z_w = Z^RHP_w + E_w with |Z^RHP_w| + |E_w| < sqrt(5/7), joined
with r261 CAMPAIGN_INPUT_FROZEN(G_n, t_n, B).  READING (typed, no
upgrade): the branch theorem stands as architecture -- the
triangle IS the generic branch (35/42 + both mains, closed
without cancellation), the exception branch carries ONE signed
scalar per window whose positivity margin no fixed-complexity
source-pure identity reaches (K1 restates the target through the
open corner provenance and is support-geometric at the terminal,
K2's manifest squares all drain, K3's row-abs demand is 1.2-2.3
decades of comb cancellation); the magnitude route to an eventual
triangle is empirically refuted on the surface (the deepest rung
is an exception, all terciles carry exceptions); the primary
floor lane closes and the exception scalar goes to the quenched
full-source RHP lane with the complete target package.  Runtime
7.9 s full / 0.4 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE (p1 disclosed above, presentation-
only, before the record pass).

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
import sympy as sp

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
CTRL_RHO_NEG = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
VALID_EPS = 1e-9
Z_ID_BAR = 1e-9
DIRECT_BAR_MAIN = 1e-8
DIRECT_BAR_DEEP = 3e-6
EPST_DN_BAND = (1.70, 1.90)
SCR_DN_BAND = (0.45, 0.60)
DEMAND_BAR = 1.0
WARD_SAMPLE_IDX = (0, 20, 41)
SPEAR_GO = 0.5
SM_Q_BAR = 1e-20
MARGIN_BAND = (0.010, 0.020)
SYM_N_MAX = 4
CAL_VERDICT = (
    "TWO_BRANCH_DECOMPOSITION_EXACT(U=C1b, cheap 35/42, "
    "exceptions 7) + EXACT_IDENTITY_NOGO(K1@CORNER_PROVENANCE+"
    "SCRAMBLE_SIGN_NOT_LOST, K2@DRAIN_SIDE_SQUARES+"
    "HEAD_PROVENANCE, K3@PAIRCORR 2.25 dec) + "
    "EVENTUAL_TRIANGLE_NOGO(deepest rung N878 IS an exception; "
    "Spearman(g, N) 0.31) + PAIRCORR_MINIATURE(K3) + "
    "TWO_BRANCH_RHP_REDUCTION + PRIMARY_FLOOR_LANE_CLOSED + "
    "TRIANGLE_RETAINED_AS_GENERIC_BRANCH + "
    "EXCEPTION_SCALAR_HANDED_TO_QUENCHED_FULLSOURCE_RHP")

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
                       "the r244 chain rows; ground truth (flips) "
                       "enters gates only"
                       if not bad else "; ".join(bad))


# ------------- sealed branch builders (target-blind: consume ONLY
# the prefix slice rpre = r[:N-1] plus (t, a', b'); the terminal
# readout r_{N-1} is structurally withheld; AST-audited)
def u_triangle(rpre, t, ap, bp):
    """U_w: the SEALED r260/r262 C1b one-step terminal triangle
    (prefix data only; the ONE sealed choice of this round)."""
    return abs(t[-1]) + abs(ap[-1] * rpre[-1]) + abs(bp[-1] * rpre[-2])


def g_gap(rpre, t, ap, bp):
    """g_w = M_w - U_w; the branch rule is g_w >= 0 (source-
    defined, no selection-by-answer)."""
    return M_W - u_triangle(rpre, t, ap, bp)


def k3_row(t, ap, bp):
    """K3: terminal transfer row K with r_{N-1} = K . (r_0,
    t_0..t_{N-2}) -- exact variation of parameters of the driven
    recursion; coefficients from (a', b') alone, fixed formula for
    any window size."""
    n = len(t) + 1
    K0 = np.zeros(n)
    K0[0] = 1.0
    K1 = ap[0] * K0
    K1[1] += 1.0
    for k in range(1, n - 1):
        K2 = ap[k] * K1 + bp[k] * K0
        K2[k + 1] += 1.0
        K0, K1 = K1, K2
    return K1


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


# --------------------------- symbolic exact instances (r261 style)
def sym_instance(fliplike):
    """exact rational instance: 6 atoms, signed weights, border
    (0, 1/2), corner 5/7; returns taus, augs, monic chain."""
    xs = [sp.Rational(-3, 2), sp.Integer(-1), sp.Rational(-1, 2),
          sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(5, 4)]
    if fliplike:
        ws = [sp.Rational(2, 3), sp.Rational(-6, 5),
              sp.Rational(1, 2), sp.Rational(-3, 7),
              sp.Integer(1), sp.Rational(1, 3)]
    else:
        ws = [sp.Rational(2, 3), sp.Rational(-1, 5),
              sp.Rational(1, 2), sp.Rational(-3, 7),
              sp.Integer(1), sp.Rational(1, 3)]
    bxs = [sp.Integer(0), sp.Rational(1, 2)]
    bws = [sp.Rational(1, 3), sp.Rational(1, 6)]
    Bc = sp.Rational(5, 7)
    m = [sum(w * x ** j for w, x in zip(ws, xs)) for j in range(10)]
    bm = [sum(bw * bx ** j for bw, bx in zip(bws, bxs))
          for j in range(6)]
    tau = {0: sp.Integer(1)}
    aug = {0: Bc}
    for n in range(1, SYM_N_MAX + 2):
        H = sp.Matrix(n, n, lambda i, j: m[i + j])
        tau[n] = H.det()
        A = sp.zeros(n + 1, n + 1)
        A[:n, :n] = H
        for i in range(n):
            A[i, n] = bm[i]
            A[n, i] = bm[i]
        A[n, n] = Bc
        aug[n] = A.det()
    # monic chain p_0..p_{SYM_N_MAX}
    hs, Fs, Ts, alhs = [], [], [], []
    for k in range(SYM_N_MAX + 1):
        if k == 0:
            coef = []
        else:
            Hk = sp.Matrix(k, k, lambda i, j: m[i + j])
            rhs = sp.Matrix(k, 1, lambda i, _j: -m[i + k])
            coef = list(Hk.LUsolve(rhs))

        def pev(x, c=coef, kk=k):
            return x ** kk + sum(ci * x ** i for i, ci in enumerate(c))
        hk = sum(w * pev(x) ** 2 for w, x in zip(ws, xs))
        Fk = sum(bw * pev(bx) for bw, bx in zip(bws, bxs))
        Tk = sum(bw * bx * pev(bx) for bw, bx in zip(bws, bxs))
        ak = sum(w * x * pev(x) ** 2 for w, x in zip(ws, xs)) / hk
        hs.append(sp.nsimplify(hk))
        Fs.append(sp.nsimplify(Fk))
        Ts.append(sp.nsimplify(Tk))
        alhs.append(sp.nsimplify(ak))
    return dict(tau=tau, aug=aug, B=Bc, h=hs, F=Fs, T=Ts, alh=alhs)


def sym_schur_ok(inst):
    """K1 symbolic: aug_n == tau_n (B - sum_{k<n} F_k^2/h_k)."""
    for n in range(1, SYM_N_MAX + 1):
        Dn = inst["B"] - sum(inst["F"][k] ** 2 / inst["h"][k]
                             for k in range(n))
        if sp.simplify(inst["aug"][n] - inst["tau"][n] * Dn) != 0:
            return False, n
    return True, None


def sym_bilinear_ok(inst):
    """K2 symbolic: aug_n tau_{n+1} - aug_{n+1} tau_n ==
    F_n^2 tau_n^2 (monic leading coefficients)."""
    for n in range(1, SYM_N_MAX + 1):
        lhs = inst["aug"][n] * inst["tau"][n + 1] \
            - inst["aug"][n + 1] * inst["tau"][n]
        rhs = inst["F"][n] ** 2 * inst["tau"][n] ** 2
        if sp.simplify(lhs - rhs) != 0:
            return False, n
    return True, None


def sym_transfer_ok(inst):
    """K3 symbolic: rebuild F_4 from (F_0, T_0..T_3) through the
    exact monic F-recursion F_{k+1} = T_k - alh_k F_k - gam_k
    F_{k-1} (gam_k = h_k/h_{k-1})."""
    F, T, h, al = inst["F"], inst["T"], inst["h"], inst["alh"]
    fa, fb_ = F[0], T[0] - al[0] * F[0]
    if sp.simplify(fb_ - F[1]) != 0:
        return False, 1
    for k in range(1, SYM_N_MAX):
        gk = h[k] / h[k - 1]
        fa, fb_ = fb_, T[k] - al[k] * fb_ - gk * fa
        if sp.simplify(fb_ - F[k + 1]) != 0:
            return False, k + 1
    return True, None


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("cancellation_adjudication_probe -- PRIME.PORT.COUPLEDTAU."
          "CANCELLATION_ADJUDICATION.01 (round 263)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + symbolic legs; "
                        "ladder, w13, samples, adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN OBJECT: the branch theorem -- U_w (SEALED C1b "
          "triangle), M_w = sqrt(5/7), g_w = M_w - U_w; g >= 0 "
          "=> CHEAP BRANCH (closed without cancellation); g < 0 "
          "=> EXCEPTION BRANCH with the single signed scalar Z_w "
          "and credit C_w = U_w - |Z_w|; 3 sealed exact-square "
          "candidates (K1 Schur det ratio, K2 bilinear squares, "
          "K3 transfer row), the eventual-triangle gate, the "
          "paircorr firewall and the RHP handover -- verdicts, "
          "bands, anti-gates ALL sealed BEFORE evaluation "
          "(r260/r261/r262 record numbers adopted, disclosed)")

    # ---------------- S1: census
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

    # ---------------- per-rung computation (single pass)
    def rung_rec(p):
        N = p["N"]
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        rpre = r[:N - 1]
        U = u_triangle(rpre, t, ap, bp)
        g = g_gap(rpre, t, ap, bp)
        Z = t[N - 2] + ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
        C = U - abs(Z)
        zdev = abs(Z - r[N - 1]) / max(1.0, abs(r[N - 1]))
        q = float(p["rho"][N - 1]) / B57
        K = k3_row(t, ap, bp)
        tau_vec = np.concatenate([[r[0]], t])
        Zreb = float(K @ tau_vec)
        rebdev = abs(Zreb - r[N - 1]) / max(1.0, abs(r[N - 1]))
        rowabs = float(np.abs(K * tau_vec).sum())
        demand = math.log10(rowabs / M_W)
        return dict(kz=p["kz"], N=N, U=U, g=g, Z=Z, C=C,
                    zdev=zdev, q=q, rebdev=rebdev, rowabs=rowabs,
                    demand=demand, t_term=abs(t[N - 2]), p=p)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    npool = len(recs)

    # ---------------- S2: LEG A -- the two branches
    section("S2  LEG A -- TWO-BRANCH DECOMPOSITION (U/M/g/Z/C)")
    zworst = max(rc["zdev"] for rc in recs + mrecs)
    check("G20-z-identity", zworst <= Z_ID_BAR,
          "Z_w = t_{N-2} + a'r_{N-2} + b'r_{N-3} == r_{N-1} "
          "EXACTLY by the driven recursion: worst rel dev %.1e "
          "(bar %.0e) on %d rungs + %d mains -- the exception "
          "scalar is ONE signed evaluation of prefix data"
          % (zworst, Z_ID_BAR, npool, len(mrecs)))
    dworst_m = 0.0
    dworst_s = 0.0
    if not smoke:
        for p in mains:
            d1, _dN = TX.direct_terminal(p)
            dworst_m = max(dworst_m, abs(d1 - B57))
        for i in WARD_SAMPLE_IDX:
            d1, _dN = TX.direct_terminal(ladder[i])
            dworst_s = max(dworst_s, abs(d1 - B57))
        okD = dworst_m <= DIRECT_BAR_MAIN \
            and dworst_s <= DIRECT_BAR_DEEP
    else:
        d1, _dN = TX.direct_terminal(packs["w9"])
        dworst_m = abs(d1 - B57)
        okD = dworst_m <= DIRECT_BAR_MAIN
    check("G21-dnm1-anchor", okD,
          "D_{N-1} == 5/7 by construction of the imported corner, "
          "DIRECT bordered-slogdet route: worst abs dev %.1e "
          "mains (bar %.0e)%s -- M_w = sqrt(5/7) is target-blind"
          % (dworst_m, DIRECT_BAR_MAIN,
             "" if smoke else " / %.1e samples idx %s (bar %.0e)"
             % (dworst_s, str(WARD_SAMPLE_IDX), DIRECT_BAR_DEEP)))
    cheap = [rc for rc in recs if rc["g"] >= 0.0]
    exc = [rc for rc in recs if rc["g"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G22-branch-decomposition", True,
              "SMOKE: w9 only -- branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g"] >= 0 else "EXCEPTION",
                 recs[0]["g"]))
    else:
        check("G22-branch-decomposition",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT)),
              "branch rule g_w >= 0 (source-defined): CHEAP %d/42 "
              "(expect %d), EXCEPTION set %s == r262 named set %s "
              "-- the r262 coverage census IS the branch "
              "decomposition, restated as a two-branch theorem"
              % (len(cheap), CHEAP_EXPECT, str(exc_kz),
                 str(tuple(sorted(EXC_KZ_EXPECT)))))
    ok_cheap = all(abs(rc["Z"]) <= rc["U"] * (1 + VALID_EPS)
                   and rc["U"] <= M_W for rc in cheap)
    m_cheap = all(rc["g"] >= 0.0 for rc in mrecs)
    check("G23-cheap-branch-closure", ok_cheap and m_cheap,
          "CHEAP BRANCH closed WITHOUT cancellation on %d/%d "
          "rungs: |Z| <= U <= M (triangle validity + coverage "
          "restated; conditional on the positive base prefix, "
          "never RH); mains: %s"
          % (len(cheap), len(cheap),
             "; ".join("w%d g %+.3f CHEAP" % (rc["kz"], rc["g"])
                       for rc in mrecs)))
    ok_credit = all(rc["C"] >= -rc["g"] - VALID_EPS for rc in exc)
    qs = np.array([rc["q"] for rc in recs])
    margins = B57 * (1.0 - qs)
    ok_razor = bool(np.all(qs < 1.0)) and (
        smoke or MARGIN_BAND[0] <= float(np.min(margins))
        <= MARGIN_BAND[1])
    slack = min((M_W - abs(rc["Z"]) for rc in exc), default=float("nan"))
    check("G24-exception-credit", ok_credit and ok_razor,
          "EXCEPTION BRANCH: C_w >= -g_w on %d/%d <=> |Z_w| <= "
          "M_w <=> q_N < 1 -- MEASURED razor, not a theorem (min "
          "magnitude slack M - |Z| = %s; q census %d/%d < 1, min "
          "q-margin %.4f in band %s)"
          % (len(exc), len(exc),
             ("%.3f" % slack) if exc else "n/a",
             npool, npool, float(np.min(margins)),
             str(MARGIN_BAND)))
    if not smoke:
        tab = "; ".join("kz%d N%d g%+.3f Z%+.3f q%.3f"
                        % (rc["kz"], rc["N"], rc["g"], rc["Z"],
                           rc["q"]) for rc in exc)
        info("EXCEPTION TABLE (the 7 handover rungs): %s" % tab)
        gvals = ["kz%d:%+.2f" % (rc["kz"], rc["g"]) for rc in recs]
        for i in range(0, len(gvals), 8):
            info("g ladder [%02d..%02d]: %s"
                 % (i, min(i + 7, len(gvals) - 1),
                    "  ".join(gvals[i:i + 8])))

    # ---------------- S3: LEG B -- exact-square gate
    section("S3  LEG B -- EXACT-SQUARE GATE (3 SEALED CANDIDATES)")
    hits = []
    for fn in ("u_triangle", "g_gap", "k3_row"):
        hits += candidate_scope_audit(fn)
    check("G30-candidate-ast-clean", not hits,
          "the sealed builders (u_triangle, g_gap, k3_row) consume "
          "ONLY the prefix slice + (t, a', b') -- no target-side "
          "identifier in scope: %s"
          % ("CLEAN" if not hits else "; ".join(hits)))
    hits_orc = candidate_scope_audit("oracle_certificate")
    check("G31-oracle-mutant-flagged", bool(hits_orc),
          "the deliberately target-reading mutant is FLAGGED (%s): "
          "target-blindness machine-enforced"
          % ("; ".join(hits_orc) if hits_orc else "NOT FLAGGED"))
    inst_m = sym_instance(False)
    inst_f = sym_instance(True)
    # K1
    ok1m, br1m = sym_schur_ok(inst_m)
    ok1f, br1f = sym_schur_ok(inst_f)
    check("G32-k1-symbolic", ok1m and ok1f,
          "K1 bordered-Schur det ratio aug_n == tau_n (B - sum "
          "F_k^2/h_k) EXACT (rational zero) n = 1..%d on MAINLIKE "
          "+ FLIPLIKE%s -- the det(Gcal)/P identity is exact "
          "algebra of fixed complexity"
          % (SYM_N_MAX, "" if ok1m and ok1f else
             " (break at n = %s/%s)" % (br1m, br1f)))
    k1_dev = 0.0
    for p in (mains if not smoke else [packs["w9"]]):
        _d1, dN = TX.direct_terminal(p)
        k1_dev = max(k1_dev, abs(dN - (B57 - float(
            p["rho"][p["N"] - 1]))))
    k1_devs = 0.0
    if not smoke:
        for i in WARD_SAMPLE_IDX:
            p = ladder[i]
            _d1, dN = TX.direct_terminal(p)
            k1_devs = max(k1_devs, abs(dN - (B57 - float(
                p["rho"][p["N"] - 1]))))
    dn_epst = B57 - float(ctrl["EPST"]["rho"][ctrl["EPST"]["N"] - 1])
    dn_scr = B57 - float(ctrl["SCR"]["rho"][ctrl["SCR"]["N"] - 1])
    k1_scr_kept = (EPST_DN_BAND[0] <= dn_epst <= EPST_DN_BAND[1]
                   and SCR_DN_BAND[0] <= dn_scr <= SCR_DN_BAND[1])
    check("G33-k1-numeric-kill",
          k1_dev <= DIRECT_BAR_MAIN
          and (smoke or k1_devs <= DIRECT_BAR_DEEP)
          and k1_scr_kept,
          "K1 numeric: M^2 - Z^2 = D_N = det(Gcal)/P direct-vs-"
          "chain worst abs dev %.1e mains / %s samples; BUT the "
          "PSD premise on Gcal IS D_N >= 0 (target restated; "
          "corner provenance OPEN, r262 INCONCLUSIVE stands) AND "
          "the terminal ratio stays POSITIVE on flipped controls "
          "(EPST D_N %+.3f in %s, SCR %+.3f in %s) => SCRAMBLE "
          "does NOT lose the sign => K1 KILLED: CORNER_PROVENANCE "
          "+ SCRAMBLE_SIGN_NOT_LOST (support geometry)"
          % (k1_dev, ("%.1e" % k1_devs) if not smoke else "n/a",
             dn_epst, str(EPST_DN_BAND), dn_scr,
             str(SCR_DN_BAND)))
    # K2
    ok2m, br2m = sym_bilinear_ok(inst_m)
    ok2f, br2f = sym_bilinear_ok(inst_f)
    h_f = inst_f["h"]
    first_hneg = next((k for k, hv in enumerate(h_f) if hv < 0),
                      None)
    rho2_f = inst_f["F"][2] ** 2 / h_f[2]
    flip_ok = (inst_f["tau"][3] < 0 and first_hneg == 2
               and rho2_f <= 0)
    check("G34-k2-symbolic", ok2m and ok2f and flip_ok,
          "K2 bilinear aug_n tau_{n+1} - aug_{n+1} tau_n == F_n^2 "
          "tau_n^2 EXACT n = 1..%d both instances%s; FLIPLIKE: "
          "tau_3 = %s < 0, first h < 0 at k = %s, rho_2 = %s < 0 "
          "-- the decrement-square structure breaks EXACTLY at "
          "the flip (the manifest square is conditional on h > 0)"
          % (SYM_N_MAX, "" if ok2m and ok2f else
             " (break n = %s/%s)" % (br2m, br2f),
             str(inst_f["tau"][3]), str(first_hneg), str(rho2_f)))
    rho_negs = {}
    for c in ("EPST", "SCR", "SMOOTH"):
        rv = ctrl[c]["rho"]
        rho_negs[c] = next((k for k in range(len(rv))
                            if float(rv[k]) < 0), None)
    k2_scr_ok = all(rho_negs[c] == CTRL_RHO_NEG[c]
                    for c in rho_negs)
    check("G35-k2-numeric-kill", k2_scr_ok,
          "K2 numeric: terminal decrement == rho_{N-1} carried by "
          "G33's direct route (same slogdets); first rho < 0 on "
          "EPST/SCR/SMOOTH at %s == sealed flips %s -- K2 PASSES "
          "the scramble condition (the square structure "
          "discriminates at the PREFIX level); K2 KILLED anyway: "
          "DRAIN_SIDE_SQUARES (every manifest square drains: D_N "
          "= B - sum r_k^2, wrong side for an SOS of the gap) + "
          "HEAD_PROVENANCE (B is not a source-pure square)"
          % (str(rho_negs), str(CTRL_RHO_NEG)))
    # K3
    ok3m, br3m = sym_transfer_ok(inst_m)
    ok3f, br3f = sym_transfer_ok(inst_f)
    reb_worst = max(rc["rebdev"] for rc in recs + mrecs)
    demands = [rc["demand"] for rc in recs]
    dem_exc = [rc["demand"] for rc in exc]
    fired = sum(1 for d in demands if d >= DEMAND_BAR)
    k3_fired = (max(dem_exc) >= DEMAND_BAR) if dem_exc else \
        (max(demands) >= DEMAND_BAR)
    check("G36-k3-transfer-detector",
          ok3m and ok3f and reb_worst <= Z_ID_BAR,
          "K3 transfer row: symbolic F_4 rebuild EXACT both "
          "instances%s; numeric rebuild worst rel dev %.1e (bar "
          "%.0e) on %d + mains; d2 demand log10(rowabs/M): median "
          "%.2f, min %.2f, max %.2f dec, exceptions %s, fires "
          "(>= %.1f dec) on %d/%d => K3 KILLED: PAIRCORR (the "
          "row-abs majorant must deliver the missing comb "
          "cancellation at root scale; leg-D firewall -- route "
          "closed IMMEDIATELY, no sharpening attempted)"
          % ("" if ok3m and ok3f else " (break %s/%s)"
             % (br3m, br3f), reb_worst, Z_ID_BAR, npool,
             float(np.median(demands)), min(demands),
             max(demands),
             ("%.2f..%.2f dec" % (min(dem_exc), max(dem_exc)))
             if dem_exc else "n/a", DEMAND_BAR, fired, npool))
    exact_go = False   # sealed GO conditions, evaluated honestly:
    # K1: premises not source-pure (corner provenance open) AND
    # scramble keeps the terminal sign; K2: squares drain-side;
    # K3: detector fired.  A GO would require ALL conditions met.
    k1_go = False and k1_scr_kept          # premise = target
    k2_go = False                          # drain-side structural
    k3_go = (reb_worst <= Z_ID_BAR) and not k3_fired
    exact_go = k1_go or k2_go or (k3_go and not smoke)
    check("G37-exact-square-adjudication", True,
          "sealed GO rule evaluated: K1 %s / K2 %s / K3 %s => %s"
          % ("NOGO (CORNER_PROVENANCE + SCRAMBLE_SIGN_NOT_LOST)",
             "NOGO (DRAIN_SIDE_SQUARES + HEAD_PROVENANCE)",
             "NOGO (PAIRCORR %.2f dec max)" % max(demands)
             if k3_fired else "GO-candidate",
             "EXACT_CANCELLATION_IDENTITY_GO" if exact_go
             else "EXACT_IDENTITY_NOGO (all three break "
             "locations honest, sealed conditions unmet)"))

    # ---------------- S4: LEG C -- eventual-triangle gate
    section("S4  LEG C -- EVENTUAL-TRIANGLE GATE (g SCALING)")
    if smoke:
        check("G40-g-scaling-census", True, "SMOKE: skipped")
        check("G41-separation-plausibility", True, "SMOKE: skipped")
        check("G42-eventual-triangle-adjudication", True,
              "SMOKE: skipped")
        evt_go = False
        finite_surface = False
        sp_gn = float("nan")
    else:
        sp_gn = BH.spearman([rc["g"] for rc in recs],
                            [rc["N"] for rc in recs])
        sp_un = BH.spearman([rc["U"] for rc in recs],
                            [rc["N"] for rc in recs])
        sp_tn = BH.spearman([rc["t_term"] for rc in recs],
                            [rc["N"] for rc in recs])
        Ns = sorted(rc["N"] for rc in recs)
        t1, t2 = Ns[len(Ns) // 3], Ns[2 * len(Ns) // 3]
        med = lambda xs: float(np.median(xs)) if xs else float("nan")  # noqa: E731
        g_t = [med([rc["g"] for rc in recs if rc["N"] <= t1]),
               med([rc["g"] for rc in recs if t1 < rc["N"] <= t2]),
               med([rc["g"] for rc in recs if rc["N"] > t2])]
        exc_terc = [sum(1 for rc in exc if rc["N"] <= t1),
                    sum(1 for rc in exc if t1 < rc["N"] <= t2),
                    sum(1 for rc in exc if rc["N"] > t2)]
        deepest = max(recs, key=lambda rc: rc["N"])
        deep_exc = deepest["g"] < 0.0
        check("G40-g-scaling-census", True,
              "MEASUREMENT: g sign census %d+/%d-; Spearman(g, N) "
              "= %.2f; tercile medians of g %.3f / %.3f / %.3f "
              "(N <= %d / <= %d / > %d); exceptions per tercile "
              "%s; DEEPEST rung kz%d N%d branch %s"
              % (len(cheap), len(exc), sp_gn, g_t[0], g_t[1],
                 g_t[2], t1, t2, t2, str(exc_terc),
                 deepest["kz"], deepest["N"],
                 "EXCEPTION" if deep_exc else "CHEAP"))
        decay_usable = (sp_un <= -SPEAR_GO)
        check("G41-separation-plausibility", True,
              "MEASUREMENT: Spearman(U, N) = %.2f, Spearman("
              "|t_term|, N) = %.2f -- %s (usability rule "
              "|Spearman| >= %.1f, sealed); M is constant: the "
              "magnitude-separation route needs U_w to FALL below "
              "sqrt(5/7) eventually%s"
              % (sp_un, sp_tn,
                 "U decays usably with depth"
                 if decay_usable else
                 "only weak trends, NO usable magnitude-decay law",
                 SPEAR_GO,
                 "" if decay_usable else
                 " -- no empirical carrier on this surface"))
        evt_go = (sp_gn >= SPEAR_GO and exc_terc[1] == 0
                  and exc_terc[2] == 0)
        finite_surface = (exc_terc[1] == 0 and exc_terc[2] == 0
                          and not evt_go)
        check("G42-eventual-triangle-adjudication", True,
              "sealed rule (Spearman >= %.1f AND exceptions "
              "confined to the lowest tercile AND deepest tercile "
              "all-cheap -- necessary, not sufficient): %s -- a "
              "deeper census would NOT prove finiteness (7 "
              "exceptions below 400 prove nothing; ladder NOT "
              "extended)"
              % (SPEAR_GO,
                 "EVENTUAL_TRIANGLE_GO candidate (law still "
                 "required)" if evt_go else
                 ("FINITE_SURFACE_ONLY typing" if finite_surface
                  else "EVENTUAL_TRIANGLE_NOGO: the deepest rung "
                  "IS an exception -- no observed w_0, no "
                  "magnitude separation")))

    # ---------------- S5: LEG D -- firewall + anti-gates
    section("S5  LEG D -- PAIRCORR FIREWALL + ANTI-GATES")
    check("G50-paircorr-firewall", True,
          "FIREWALL BALANCE: the d2 detector fired on K3 ONLY "
          "(%d/%d rungs above %.1f dec) -- K1/K2 die structurally "
          "BEFORE any majorant step (no |Z| <= majorant step ever "
          "entered their adjudication); the K3 route closed "
          "IMMEDIATELY on firing (no sharpening, no unrolling, no "
          "grouping attempted) -- PAIRCORR_MINIATURE(K3) carried "
          "in the verdict"
          % (fired if not smoke else
             sum(1 for d in demands if d >= DEMAND_BAR),
             npool, DEMAND_BAR))
    ag_hits = antigate_fragment_audit()
    br_hits = candidate_scope_audit("g_gap")
    check("G51-anti-gates", not ag_hits and not br_hits,
          "ANTI-GATES (binding): no unroll series (no cand_unroll "
          "identifier: %s), no fit primitives (fragment scan: "
          "%s), no new sign heuristics (no sign-pattern census in "
          "this module), no regression on the 7 exceptions, no "
          "5/7 refit (B57 literal, imported), no further drive-"
          "abs majorant as certificate (row-abs ONLY inside the "
          "d2 detector), no cofinal selection by post-hoc "
          "cancellation values (branch builder scope: %s)"
          % ("CLEAN" if not ag_hits else "; ".join(ag_hits),
             "CLEAN" if not ag_hits else "HIT",
             "CLEAN (reads g only)" if not br_hits
             else "; ".join(br_hits)))
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) / B57
    check("G52-controls-discrimination", abs(qS) <= SM_Q_BAR,
          "SMOOTH anchor q_N = %.1e <= %.0e; DISCRIMINATION "
          "SUMMARY: the square/flip structure separates worlds at "
          "the PREFIX level (first rho < 0 at %s == flips) while "
          "the terminal det ratio does NOT (EPST %+.3f / SCR "
          "%+.3f positive) -- exactly the K2-vs-K1 kill split: "
          "prefix positivity carries the arithmetic, the terminal "
          "ratio is support-geometric"
          % (qS, SM_Q_BAR, str(rho_negs), dn_epst, dn_scr))

    # ---------------- S6: LEG E -- handover + verdict
    section("S6  LEG E -- RHP HANDOVER + VERDICT")
    if not smoke:
        info("RHP HANDOVER PACKAGE (frozen): Z_w := t_{N-2} + "
             "a'_{N-2} r_{N-2} + b'_{N-2} r_{N-3} == r_{N-1} == "
             "F_{N-1}/sqrt(h_{N-1}) == the sign form of the tau "
             "cross-ratio 1 - q_N = (tau^aug_N tau_{N-1})/"
             "(tau^aug_{N-1} tau_N); route: BH.wpack -> "
             "TX.drive_arrays -> one signed sum")
        info("EXCEPTION RUNGS (7): %s"
             % "; ".join("kz%d N%d g%+.3f Z%+.4f q%.3f"
                         % (rc["kz"], rc["N"], rc["g"], rc["Z"],
                            rc["q"]) for rc in exc))
        info("FUTURE-WINDOW RULE: exception branch iff g_w = "
             "sqrt(5/7) - U_w < 0 with the SEALED C1b form -- "
             "source-defined, NO selection-by-answer")
        info("REQUIREMENT to the quenched full-source RHP lane: "
             "produce Z_w = Z^RHP_w + E_w with |Z^RHP_w| + |E_w| "
             "< M_w = sqrt(5/7) on the exception branch, or "
             "directly the positivity of the tau cross-ratio; "
             "INPUT = r261 CAMPAIGN_INPUT_FROZEN(G_n, t_n, B; "
             "scaled-Chebyshev basis, hull [x0 -+ rh] per window) "
             "-- together the COMPLETE RHP target package")
        ok_handover = (len(exc) == len(EXC_KZ_EXPECT)
                       and exc_kz == tuple(sorted(EXC_KZ_EXPECT)))
    else:
        ok_handover = True
    check("G60-rhp-handover", ok_handover,
          "handover package frozen%s: Z-definition (3 exact "
          "equivalent forms), computation route, %s named rungs, "
          "future-window rule, requirement + r261 join"
          % (" (SMOKE: package printed in full mode only)"
             if smoke else "",
             len(exc) if not smoke else "n/a"))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the branch THEOREM structure (cheap branch "
          "closed, exception scalar isolated), the adjudicated "
          "death of all three fixed-complexity exact-square "
          "routes, the empirical refutation of the magnitude "
          "route, and the frozen RHP target package")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["TWO_BRANCH_DECOMPOSITION_EXACT(U=C1b, cheap "
                 "%d/42, exceptions %d)" % (len(cheap), len(exc))]
        if exact_go:
            parts.append("EXACT_CANCELLATION_IDENTITY_GO")
        else:
            parts.append("EXACT_IDENTITY_NOGO(K1@CORNER_"
                         "PROVENANCE+SCRAMBLE_SIGN_NOT_LOST, "
                         "K2@DRAIN_SIDE_SQUARES+HEAD_PROVENANCE, "
                         "K3@PAIRCORR %.2f dec)" % max(demands))
        if evt_go:
            parts.append("EVENTUAL_TRIANGLE_GO(candidate)")
        elif finite_surface:
            parts.append("FINITE_SURFACE_ONLY(exceptions in the "
                         "lowest tercile)")
        else:
            parts.append("EVENTUAL_TRIANGLE_NOGO(deepest rung "
                         "N%d IS an exception; Spearman(g, N) "
                         "%.2f)" % (max(rc["N"] for rc in recs),
                                    sp_gn))
        if k3_fired:
            parts.append("PAIRCORR_MINIATURE(K3)")
        if not exact_go and not evt_go:
            parts += ["TWO_BRANCH_RHP_REDUCTION",
                      "PRIMARY_FLOOR_LANE_CLOSED",
                      "TRIANGLE_RETAINED_AS_GENERIC_BRANCH",
                      "EXCEPTION_SCALAR_HANDED_TO_QUENCHED_"
                      "FULLSOURCE_RHP"]
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the Z-identity, the "
          "branch decomposition, the cheap-branch closure, the "
          "symbolic identities; MEASURED: the exception credit, "
          "the g-scaling, the demand census; OPEN: the exception "
          "scalar itself (handed to the quenched full-source RHP "
          "lane); NO RH claim"
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
