#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""border_centering_probe -- PRIME.PORT.BORDER.CENTERING.01
(round 248): exact NORMAL FORM of the r243/r244/r246 bordered budget
object and typing of its tail.  r246 left three zones: a rank-1 head
rho_0 ~ 37 percent (geometry -- EPSTEIN head-identical), a quiet zone
p_1..p_7 ~ 1e-8 (MAIN silent, SCRAMBLE +2.1 decades), and an
extensive tail K_0.9 ~ 0.9 N.  This round proves the theorem-grade
statements the consolidation and the coming CENTERED_BASEFIBER
campaign need: the head is ALGEBRAICALLY ELIMINABLE (centering
congruence), the quiet zone is an exact moment-annihilation statement
of a CENTERED border functional sigma0 (the dictionary), and the
extensive tail compresses into ONE terminal CD-kernel-difference
readout -- then the tail PROFILE is typed under DEV/BLIND discipline.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r246 discipline): w = window (kz),
N_w = builder depth, n = chain degree; free pivots h_{w,n} (n < N_w)
are the proof objects; sigma = the sealed r239/r243 smooth PNT-shape
border (F_DEF / F_DEF_SHA imported verbatim from r243); F_n =
int pihat_n dsigmatilde, rho_n = F_n^2/h_n, S = cumsum rho; the
machinery is imported verbatim from r244 (bordered_hankel_probe.
wpack -- rho/S/chain bitwise the r244 objects).  pihat_N (the
degree-N polynomial) consumes recursion data of the FREE prefix
only (m_0..m_{2N-1}); the forced pivot h_N is never consumed.
Ground truth (h signs, flips) enters gates only.

LEG A -- THE CENTERING CONGRUENCE (theorem grade): with
  c  = u_0 / (H_N)_{00} = F_0 / h_0   (= s_0 / m_0),
  u0 = u - c H_N e_0        (entries s_i - c m_i),
  B0 = B - F_0^2/h_0 = B - rho_0,
the elementary congruence
  [[I, -c e_0],[0, 1]]^T [[H_N, u],[u^T, B]] [[I, -c e_0],[0, 1]]
      = [[H_N, u0],[u0^T, B0]]
holds EXACTLY -- det E = 1, so the bordered matrix is congruent
(hence PSD- and inertia-equivalent) to its CENTERED form: the
geometric rank-1 head rho_0 is ALGEBRAICALLY FULLY ELIMINABLE and
does not belong in the large analysis.  GATES: exact in rationals
on the r243 signed toy + signed smooth border (n = 2..4, budgets
B in {22/7, 5/3}; congruence entrywise, det equality, and the
centered moment route F0_0 = 0, F0_n = F_n for n >= 1); f64 on ALL
ladder windows AND all three controls (world-blind -- the
congruence is algebra, it holds on every world, n = 8, B in
{2, 20}); mp ward (dps 60) on the real w9 at n = 8/12, both
budgets, entrywise + det route.

LEG B -- THE sigma0 DICTIONARY OF THE QUIET ZONE (theorem grade):
define the CENTERED border functional sigma0 = sigma -
(F_0/h_0) mutilde (an explicit signed measure on the union of the
border and window atom sets).  EXACT statements, each gated:
  (b1) int pihat_0 dsigma0 = 0 and int pihat_n dsigma0 = F_n for
       n >= 1 (because int pihat_n dmutilde = 0);
  (b2) THE DICTIONARY THEOREM: F_1 = ... = F_m = 0  <=>
       int p dsigma0 = 0 for ALL polynomials p of degree <= m
       (sigma0 annihilates the low-degree polynomial space);
       gated constructively in rationals: subtracting the
       projections sum_{k<=m} (F_k/h_k) pihat_k dmutilde kills
       moments 0..m exactly and leaves F_k (k > m) untouched, and
       the converse follows from the triangular (monic) transform
       t_j = sum_{1<=k<=j} b_{jk} F_k with b_{jj} = 1 (forward
       substitution reconstructs F from t exactly);
  (b3) DUAL-NORM IDENTITY: Q_m = sum_{n=1}^m F_n^2/h_n is EXACTLY
       the squared dual norm of sigma0 restricted to P_m in the
       mutilde form on the positive prefix: Q_m = t^T H_{m+1}^{-1}
       t with t = (t_0..t_m), t_j = s_j - c m_j (the centered
       partial Parseval); rationals + mp (dps 60) on real w9.
THE MEASUREMENT (the new arithmetic observable): how close to
exact-zero are the sigma0 moments on MAIN?  Per window k = 0..12:
raw centered moments t_k normalized on the absolute pre-
cancellation scale (|s_k| + |c| |m_k| mass norms), and the scale-
free orthogonal projections g_k = |F_k|/sqrt(h_k); ladder medians,
DEV N-trends; on SCRAMBLE the per-degree decade excess
log10(rho^SCR_k / rho^MAIN_k) locates WHERE the annihilation
breaks (sealed breakpoint rule: first k in 1..12 with excess
>= 1 decade).  SOURCE-IDENTITY CHECK (the builder question): does
sigma share low u-moments with the comb BY CONSTRUCTION?  Compare
sum_a MU_ALL_a U_ALL_a^k vs sum_j (2 e^{u_j/2} du) u_j^k for
k = 0..7 on every DEV window (rel dev on the joint abs scale).
SEALED TYPING (mutually exclusive, priority order):
  QUIETZONE_EXACT_MOMENTS iff the u-moment source identity holds
    to <= 1e-10 on all DEV windows (an exact construction
    identity explains the silence);
  QUIETZONE_ASYMPTOTIC_MOMENTS iff DEV median of G_q :=
    sqrt(Q_7 / S_{N-1}) <= 1e-2 AND the DEV log-log slope of G_q
    vs N is <= -0.10 (PNT-like small and N-falling);
  QUIETZONE_FINITE_NUMERICAL_ONLY otherwise.
NO eight-bit/E8 narrative anywhere: the number 7 is a finding of
the sealed head cut HEAD_K = 8 (r246), not an oracle.

LEG C -- TAIL-KERNEL COMPRESSION (theorem grade): with the
Christoffel-Darboux kernel K_m(x, y) = sum_{k<m} pihat_k(x)
pihat_k(y)/h_k = [pihat_m(x) pihat_{m-1}(y) - pihat_{m-1}(x)
pihat_m(y)] / (h_{m-1}(x - y)) (confluent diagonal via the
derivative form), the extensive tail is ONE terminal readout:
  T = sum_{n>=8} rho_n
    = intint [K_N(x,y) - K_8(x,y)] dsigma0(x) dsigma0(y),
and the readout is CENTERING-INVARIANT (the difference kernel
only sees modes >= 8 > 0, so sigma and sigma0 give the same
value) -- extensive information in the SOURCE, not extensive
dimension of the analytic STATE.  GATES: exact in rationals on
the toy (K_4 - K_2 double pairing over the sigma0 atom union,
confluent diagonal, spectral == CD form, sigma == sigma0
invariance); f64 at (m_hi, m_lo) = (12, 8) on ALL ladder windows
+ all three controls (world-blind; SMOOTH is the sigma0 == 0
self-alias -- absolute guard on the CD mass-norm scale, r243
amendment-a1 pattern, sealed here pre-run); sigma0-invariance
f64 on w9 + the three controls; mp (dps 160) on w9 through the
FULL depth: T = intint [K_{N} - K_8] dsigma dsigma vs the mp
tail sum, N = 184 (the terminal readout is not an f64 artifact).

LEG D -- TAIL-PROFILE TYPING (EXTENSIVE is proven r246, the
PROFILE is open): per window T_w = sum_{n=8}^{N-1} rho_n,
q_{n,w} = rho_{n,w}/T_w; does N_w q_{floor(x N_w), w} converge to
a profile phi(x)?  SEALED PROCEDURE: x_n = n/N_w on the tail
range; binned mean profile of N_w q_n in 18 bins on [0.05, 0.95]
(sealed bandwidth 0.05); metric = relative L1: ||pi - pi'||_1 /
(0.5 (||pi||_1 + ||pi'||_1)).  DEV/BLIND: BLIND = the two
largest-N rungs of the (N, kz) sort (r246 rule); classification
on DEV, confirmation on BLIND.  SEALED VERDICTS (priority):
  EXTENSIVE_REGULAR_TAIL (d1, universal phi) iff the DEV median
    pairwise rel-L1 <= 0.25; BLIND confirmation: both blind
    profiles within 0.35 of the DEV mean profile;
  EXTENSIVE_QUENCHED_TAIL (d2, window-specific phi_w of stable
    form) iff not d1 AND the within-window even/odd half-profile
    rel-L1 has DEV median <= 0.25 (a window whose two disjoint
    degree-parity halves agree HAS a well-defined profile; the
    windows just differ); BLIND confirmation: both blind
    windows' even/odd rel-L1 <= 0.35;
  EXTENSIVE_IRREGULAR_TAIL (d3) otherwise.
A failed BLIND confirmation appends TAILPROFILE_BLIND_CHECK_
FAILED (typed UNSTABLE, never upgraded, never dropped).
ANALYTIC CONSEQUENCE (documented under any verdict): regular ->
one integrated density formula covers the tail; quenched ->
window-specific phi_w with a single uniform proof rule; irregular
-> the full discrete source stands without a macroprofile.

LEG E -- NAMING-CORRECTION RECORD (sealed): the corrected
three-zone typing of the budget object is
  GEOMETRIC_RANK1_HEAD        (world-blind, eliminable by leg A)
  + LOWMODE_ARITHMETIC_SILENCE (the arithmetic: sigma0
    annihilation, SCRAMBLE breaks it by decades)
  + EXTENSIVE_PAIRING_SENSITIVE_TAIL (the budget excess of the
    arithmetic-destroying world sits in n >= 8).
The r246 label HEAD_CARRIES_ARITHMETIC was a MISNOMER: the head
is geometry (its magnitude clause fired on the QUIET modes, not
on the head mode); the arithmetic sits in the silence and in the
pairing sensitivity of the tail.  RE-MEASURED GATES (w9 base):
head level world-shared: |log10(rho_0 ctrl / rho_0 MAIN)| <= 0.5
for EPSTEIN and SCRAMBLE; silence arithmetic: median over
k = 1..7 of log10(rho^SCR/rho^MAIN) >= 1.0 while |median| <= 0.5
for EPSTEIN; tail pairing-sensitive: the fraction of the
SCRAMBLE pre-flip budget excess sitting in n >= 8 is >= 0.5.

MUST-FAILS (each loud): (m1) WRONG CENTERING: c' = 8c/7 breaks
the congruence border entry 0 by exactly -(c'-c) m_0 and the
corner by exactly +m_0 (c'-c)^2 (rationals); (m2) INDEX-SHIFTED
TAIL KERNEL: [K_4 - K_1] differs from [K_4 - K_2] by exactly
rho_1 != 0 (rationals; the K_7-for-K_8 shift in toy form); (m3)
UNCENTERED ALIAS: sigma itself does NOT annihilate P_0 (t_0 =
s_0 != 0 and q^T H^{-1} q = Q + rho_0 != Q, rationals) -- the
centering is NECESSARY for the dictionary; (m4) SIGN ORACLE:
reading sign h_{N-1} hits every window and is EXCLUDED by the
input firewall (standing r243 exclusion, re-asserted).

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs);
background du = 0.01, masses 2 e^{u/2} du (imported via PB/BH);
toy = r243 signed 9-atom toy + disjoint signed 5-atom smooth
border, congruence degrees 2..4, toy budgets {22/7, 5/3};
real budgets {2, 20}; congruence f64 bar 1e-10 (n = 8, all 42+3
worlds, per-entry pre-cancellation scale); congruence mp dps 60
bar 1e-30 (w9, n = 8/12); t_0 bars 1e-12 (f64) / 1e-50 (mp,
rel s_0); F0/dual-norm mp bars 1e-8 (n = 8) / 2e-6 (n = 12)
(r243 moment-route bars); quiet range k = 1..7; u-moment source
bar 1e-10 (k = 0..7, all DEV windows); quiet level bar 1e-2
(DEV median G_q); quiet trend bar -0.10 (DEV log-log slope);
SCRAMBLE breakpoint bar 1.0 decade (per-degree rho excess);
CD f64 (m_hi, m_lo) = (12, 8) bar 1e-6 rel with self-alias
absolute guard 1e-12 on the CD mass-norm scale; sigma0-
invariance worlds = w9 + 3 controls, bar 1e-6 (same guard);
mp deep dps 160, w9 full depth, bar 1e-6 rel; profile bins 18
on [0.05, 0.95], bandwidth 0.05, rel-L1 metric, DEV bar 0.25,
BLIND bar 0.35, BLIND = two largest-N rungs; naming bars 0.5
decades (head), 1.0 / 0.5 decades (silence SCR / EPSTEIN), 0.5
(tail excess fraction); control flips 25/21/27; smoke rungs
(9, 12, 13, 26, 40); runtime <= 1800 s.

SEALED VERDICT FORM (joined with '+'):
  CENTERING_CONGRUENCE_EXACT / _OPEN        (leg A gates)
  + SIGMA0_DICTIONARY_EXACT / _OPEN         (leg B identity gates)
  + QUIETZONE_<EXACT_MOMENTS | ASYMPTOTIC_MOMENTS |
      FINITE_NUMERICAL_ONLY>                (leg B typing)
  + TAIL_KERNEL_COMPRESSED / TAIL_KERNEL_OPEN   (leg C gates)
  + EXTENSIVE_<REGULAR | QUENCHED | IRREGULAR>_TAIL
      [+ TAILPROFILE_BLIND_CHECK_FAILED]    (leg D typing)
  + THREE_ZONE_NORMALFORM(GEOMETRIC_RANK1_HEAD +
      LOWMODE_ARITHMETIC_SILENCE + EXTENSIVE_PAIRING_SENSITIVE_
      TAIL) / THREE_ZONE_NORMALFORM_UNCONFIRMED   (leg E gates).
Honesty before beauty.  No verdict claims a bound mechanism; the
r243 budget bound stays OPEN (PAIRCORR_REENCODED stands).

RECORD TABLES (frozen from calib_bc_pass1.log, 24/24, wall
10.6 s; disclosed SMOKE/CALIBRATION AMENDMENTS -- the congruence,
the dictionary, the typing rules, the profile rules and ALL
verdict rules NEVER moved: (a1) the smoke pass caught ONE
printing bug (a missing format argument in the G82 detail
string); fixed before the record run, no rule and no bar
touched.  HONESTY NOTES (sealed post-measurement, disclosed):
(h1) the 5-rung smoke ladder shows a POSITIVE G_q slope (+4.70,
shallow-window artifact) and would have typed FINITE_NUMERICAL_
ONLY; the full 40-rung DEV fit gives -0.18 -- the smoke verdict
is refuted by the record run exactly as in r246; (h2) the
ASYMPTOTIC typing is NOT robust: the DEV slope -0.18 sits close
to the sealed trend bar -0.10 and the per-mode slopes are mixed
in sign (k = 4/5 rise at +0.18/+0.25) -- the aggregate G_q falls
with N, the mode-resolved picture does not uniformly; typed as
measured, no upgrade):
CAL_VERDICT = CENTERING_CONGRUENCE_EXACT +
SIGMA0_DICTIONARY_EXACT + QUIETZONE_ASYMPTOTIC_MOMENTS +
TAIL_KERNEL_COMPRESSED + EXTENSIVE_IRREGULAR_TAIL +
THREE_ZONE_NORMALFORM(GEOMETRIC_RANK1_HEAD +
LOWMODE_ARITHMETIC_SILENCE + EXTENSIVE_PAIRING_SENSITIVE_TAIL).
Key numbers.  LEG A: toy congruence EXACT in rationals (n = 2..4,
both budgets: entrywise, det equality, F0_0 = 0, F0_n = F_n);
must-fail m1 loud (border break -(c'-c) m_0, corner +m_0
(c'-c)^2, exact); f64 congruence world-blind on 42 MAIN + 3
controls, worst per-entry dev 1.2e-16 (bar 1e-10, B = 2 and 20);
mp ward w9 (dps 60) worst 2.6e-62 entrywise / 4.8e-55 det route
(bar 1e-30).  LEG B: dictionary + dual norm EXACT in rationals
(t_0 = 0; constructive annihilation m = 2, 3; triangular
converse; Q_m = t^T H_{m+1}^{-1} t at m = 2..4); m3 loud
(t_0(sigma) = s_0 != 0, uncentered Parseval = Q + rho_0); mp w9:
t_0/s_0 = 0.0 (dps-60 exact), F0_8 dev 6.4e-13 / F0_12 dev
8.1e-13, dual-norm Q_7 dev 3.3e-13 / Q_11 dev 1.2e-13.  THE
MEASUREMENT (the new arithmetic observable, ladder medians):
tnorm_k ~ 0.5..1.8e-4 and g_k ~ 3.8..7.6e-4 across k = 1..12
(vs g_0 ~ 1.94: the centered functional sits ~ 3.5 decades
below the head on EVERY low mode); designated statistic G_q =
sqrt(Q_7/S_{N-1}): DEV median 4.99e-4 (level bar 1e-2 PASSED),
DEV log-log slope -0.18 (trend bar -0.10 PASSED) =>
QUIETZONE_ASYMPTOTIC_MOMENTS by the sealed rule, with honesty
note h2 (near-bar, mode-mixed); NOT an exact construction
identity: the u-moment source check measures worst rel dev
1.4e-2 over k = 0..7 on all DEV windows (exact bar 1e-10
decisively missed) -- sigma does NOT share low u-moments with
the comb by construction, the silence is a PNT-level
cancellation, not a builder identity.  SCRAMBLE break table
(decades log10 rho_SCR/rho_MAIN, k = 1..12): +3.3 +3.7 +3.8
+2.2 +2.0 +1.2 +1.7 | +2.7 +4.7 +4.4 +2.4 +3.7 => breakpoint
k = 1 (sealed rule, bar 1.0 decade): the annihilation breaks
IMMEDIATELY at the first centered mode, median excess +2.21
decades on the quiet range -- the WHOLE quiet zone is
arithmetic, not just its deep end.  LEG C: toy CD compression
EXACT (K_4 - K_2 double pairing == rho_2 + rho_3, confluent
diagonal, spectral == CD, sigma == sigma0 invariance, m2 shift
loud by exactly rho_1); f64 (12, 8) worst rel dev 5.4e-07 on
42 + 3 worlds (SMOOTH sigma0 == 0 self-alias on the abs
mass-norm guard: 3.9e-15 <= 1e-12, typed pre-run);
sigma0-invariance worst 6.1e-10 (w9 + 3 controls); mp deep w9
(dps 160, N = 184, 367 border atoms, 2 s): T = intint [K_184 -
K_8] dsigma dsigma matches the mp tail sum 4.334319 to rel dev
3.3e-160 (f64 chain drift 9.7e-13) -- the extensive tail IS one
terminal CD-kernel-difference readout, through the FULL depth
including the razor.  LEG D: tail share T_w/S_{N-1} in [0.48,
0.72] med 0.63 (the tail carries ~ 2/3 of the budget); d1
universality: DEV median pairwise rel-L1 0.730 (q25/q75
0.624/0.854, max 1.279, 780 pairs) vs bar 0.25 -- FAILS by 3x,
no universal phi; d2 quenched: within-window even/odd rel-L1
DEV median 1.143 (blind 1.255/0.681) vs bar 0.25 -- even the
two degree-parity halves of ONE window disagree at ~ 114
percent: no stable per-window profile => EXTENSIVE_IRREGULAR_
TAIL (d3): N q_n has NO macroprofile phi(x), neither universal
nor quenched; analytic consequence: the full discrete source
must be carried -- no integrated density formula, no per-window
profile rule; consistent with r244 IRREGULAR_BULK (Gini 0.909)
and r246 K_0.9 ~ 0.9 N, now sharpened to the profile level.
LEG E: head world-shared: rho_0 decade offsets EPSTEIN +0.000 /
SCRAMBLE +0.000 (bar 0.5; SCRAMBLE's rho_0 is IDENTICAL --
mass-multiset-preserving surgery leaves F_0 = s_0 and h_0
nearly untouched): the r246 +2.12-decade magnitude clause lived
ENTIRELY on the quiet modes, mode 0 is world-blind; silence
arithmetic: SCR median +2.21 decades (>= 1.0), EPSTEIN +0.000
(<= 0.5); tail pairing-sensitive: SCRAMBLE pre-flip excess
fraction in n >= 8 = 0.836 (>= 0.5; r246's 84 percent
reproduced) => THREE_ZONE_NORMALFORM recorded, the r246 label
HEAD_CARRIES_ARITHMETIC retired as a misnomer.  Must-fails all
loud (m1/m2/m3 exact in rationals, m4 oracle excluded by the
firewall).  Runtime 10.6 s full, 0.7 s smoke.
AMENDMENTS AFTER FREEZE: NONE.

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
B_TOY = (Fr(22, 7), Fr(5, 3))
B_REAL = (2.0, 20.0)
CONG_F64_BAR = 1e-10
CONG_MP_BAR = 1e-30
MP_DPS_A = 60
T0_F64_BAR = 1e-12
T0_MP_BAR = 1e-50
F0_BAR_8 = 1e-8
F0_BAR_12 = 2e-6
QUIET_KS = (1, 2, 3, 4, 5, 6, 7)
UMOM_EXACT_BAR = 1e-10
UMOM_KMAX = 7
QUIET_LEVEL_BAR = 1e-2
QUIET_TREND_BAR = -0.10
BREAK_DECADE = 1.0
CD_HI, CD_LO = 12, 8
CD_BAR = 1e-6
CD_ABS_GUARD = 1e-12
MP_DPS_C = 160
CD_MP_BAR = 1e-6
PROF_BINS = 18
PROF_LO, PROF_HI = 0.05, 0.95
PROF_DEV_BAR = 0.25
PROF_BLIND_BAR = 0.35
HEAD_DEC_BAR = 0.5
SIL_SCR_BAR = 1.0
SIL_EPS_BAR = 0.5
TAILFRAC_BAR = 0.5
KTAB = 12
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SMOKE_KZ = (9, 12, 13, 26, 40)
CAL_VERDICT = ("CENTERING_CONGRUENCE_EXACT + "
               "SIGMA0_DICTIONARY_EXACT + "
               "QUIETZONE_ASYMPTOTIC_MOMENTS + "
               "TAIL_KERNEL_COMPRESSED + "
               "EXTENSIVE_IRREGULAR_TAIL + "
               "THREE_ZONE_NORMALFORM(GEOMETRIC_RANK1_HEAD + "
               "LOWMODE_ARITHMETIC_SILENCE + "
               "EXTENSIVE_PAIRING_SENSITIVE_TAIL)")

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
    return (not bad), ("NO zero/prime oracles; rho/S/chain are the "
                       "BITWISE r244 objects (BH.wpack imported); "
                       "pihat_N consumes free-prefix recursion data "
                       "only; sign h_{N-1} (m4 oracle) EXCLUDED"
                       if not bad else "; ".join(bad))


# ----------------------------------------------- rational helpers
def fr_matmul(A, B):
    n, m, p_ = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m))
             for j in range(p_)] for i in range(n)]


def fr_transpose(A):
    return [list(r) for r in zip(*A)]


def toy_pd(al, hs, nodes, m):
    """exact monic values AND derivatives at rational nodes."""
    P = [[Fr(1) for _ in nodes]]
    dP = [[Fr(0) for _ in nodes]]
    if m >= 1:
        P.append([x - al[0] for x in nodes])
        dP.append([Fr(1) for _ in nodes])
    for k in range(1, m):
        g = hs[k] / hs[k - 1]
        P.append([(x - al[k]) * P[k][i] - g * P[k - 1][i]
                  for i, x in enumerate(nodes)])
        dP.append([P[k][i] + (x - al[k]) * dP[k][i] - g * dP[k - 1][i]
                   for i, x in enumerate(nodes)])
    return P, dP


def toy_cd_double(P, dP, hs, m, nodes, wts):
    """exact double pairing intint K_m dnu dnu, confluent diagonal."""
    tot = Fr(0)
    A = len(nodes)
    for a in range(A):
        for b in range(A):
            if a == b:
                k = (dP[m][a] * P[m - 1][a]
                     - dP[m - 1][a] * P[m][a]) / hs[m - 1]
            else:
                k = ((P[m][a] * P[m - 1][b]
                      - P[m - 1][a] * P[m][b])
                     / (hs[m - 1] * (nodes[a] - nodes[b])))
            tot += wts[a] * wts[b] * k
    return tot


# --------------------------------------------------- f64 helpers
def world_arrays(p):
    d, dsm = p["d"], p["dsm"]
    wxa = np.concatenate([d["xs"], d["ys"]])
    wwa = np.concatenate([d["ws"], -d["vs"]])
    bxa = np.concatenate([dsm["xs"], dsm["ys"]])
    bwa = np.concatenate([dsm["ws"], -dsm["vs"]])
    return wxa, wwa, bxa, bwa


def f64_moments(x, w, kmax):
    mm, ma = [], []
    cw = w.copy()
    ca = np.abs(w).copy()
    ax = np.abs(x)
    for _k in range(kmax + 1):
        mm.append(float(np.sum(cw)))
        ma.append(float(np.sum(ca)))
        cw = cw * x
        ca = ca * ax
    return mm, ma


def cong_dev_f64(p, n, B):
    """entrywise congruence deviation at size n, budget B, on the
    per-entry pre-cancellation scale (world-blind algebra)."""
    wxa, wwa, bxa, bwa = world_arrays(p)
    mm, mabs = f64_moments(wxa, wwa, 2 * n - 2)
    sm, sabs = f64_moments(bxa, bwa, n)
    c = sm[0] / mm[0]
    G = np.zeros((n + 1, n + 1))
    for i in range(n):
        for j in range(n):
            G[i, j] = mm[i + j]
        G[i, n] = G[n, i] = sm[i]
    G[n, n] = B
    E = np.eye(n + 1)
    E[0, n] = -c
    L = E.T @ G @ E
    R = G.copy()
    for i in range(n):
        R[i, n] = R[n, i] = sm[i] - c * mm[i]
    R[n, n] = B - sm[0] * sm[0] / mm[0]
    Sc = np.zeros((n + 1, n + 1))
    for i in range(n):
        for j in range(n):
            Sc[i, j] = mabs[i + j] + 1e-300
        Sc[i, n] = Sc[n, i] = sabs[i] + abs(c) * mabs[i] + 1e-300
    Sc[n, n] = abs(B) + 2 * abs(c) * sabs[0] + c * c * mabs[0]
    return float(np.max(np.abs(L - R) / Sc)), c


def hv_at(p, k):
    r = p["rows"][k]
    return r["sg_h"] * math.exp(r["lg_h"])


def cd_tail_f64(p, m_hi, m_lo, sigma0=False):
    """f64 CD-difference readout intint [K_hi - K_lo] dnu dnu vs the
    direct tail sum; returns (T_cd, T_direct, kscale)."""
    rows = p["rows"]
    alh = [rows[k]["alh"] for k in range(m_hi)]
    gamv = [0.0] + [rows[k]["gam_next"] for k in range(m_hi - 1)]
    wxa, wwa, bxa, bwa = world_arrays(p)
    if sigma0:
        c = (float(np.sum(bwa)) / float(np.sum(wwa)))
        nodes = np.concatenate([bxa, wxa])
        wts = np.concatenate([bwa, -c * wwa])
    else:
        nodes, wts = bxa, bwa
    P, dP = BH.plain_vals(alh, gamv, nodes, m_hi)
    T_cd = 0.0
    kscale = 0.0
    D = nodes[:, None] - nodes[None, :]
    for m in (m_hi, m_lo):
        h = hv_at(p, m - 1)
        NUM = (P[m][:, None] * P[m - 1][None, :]
               - P[m - 1][:, None] * P[m][None, :])
        with np.errstate(divide="ignore", invalid="ignore"):
            K = NUM / (h * D)
        kd = (dP[m] * P[m - 1] - dP[m - 1] * P[m]) / h
        np.fill_diagonal(K, kd)
        bad = (np.abs(D) < 1e-12) & (~np.eye(len(nodes), dtype=bool))
        if np.any(bad):
            ii, jj = np.nonzero(bad)
            K[ii, jj] = kd[ii]
        val = float(wts @ K @ wts)
        T_cd += val if m == m_hi else -val
        kscale += (float(np.abs(wts) @ np.abs(P[m]))
                   * float(np.abs(wts) @ np.abs(P[m - 1]))
                   / abs(h))
    T_direct = float(np.sum(p["rho"][m_lo:m_hi]))
    return T_cd, T_direct, kscale


# ------------------------------------------------------ mp blocks
def mp_cong_block(p):
    """leg A mp ward on w9: entrywise congruence + det route at
    n = 8/12, both real budgets (dps 60)."""
    import mpmath as mp
    mp.mp.dps = MP_DPS_A
    mmom, smom = BH.mp_moments(p["d"], p["dsm"], 12, MP_DPS_A)
    wxa, wwa, bxa, bwa = world_arrays(p)
    mabs = [float(np.sum(np.abs(wwa) * np.abs(wxa) ** k))
            for k in range(25)]
    sabs = [float(np.sum(np.abs(bwa) * np.abs(bxa) ** k))
            for k in range(13)]
    c = smom[0] / mmom[0]
    worst_e = worst_d = 0.0
    for n in (8, 12):
        for B in B_REAL:
            G = mp.zeros(n + 1, n + 1)
            for i in range(n):
                for j in range(n):
                    G[i, j] = mmom[i + j]
                G[i, n] = G[n, i] = smom[i]
            G[n, n] = mp.mpf(B)
            E = mp.eye(n + 1)
            E[0, n] = -c
            L = E.T * G * E
            R = mp.matrix(G)
            for i in range(n):
                R[i, n] = R[n, i] = smom[i] - c * mmom[i]
            R[n, n] = mp.mpf(B) - smom[0] * smom[0] / mmom[0]
            for i in range(n + 1):
                for j in range(n + 1):
                    if i < n and j < n:
                        sc = mabs[i + j]
                    elif i == n and j == n:
                        sc = (abs(B) + 2 * abs(float(c)) * sabs[0]
                              + float(c) ** 2 * mabs[0])
                    else:
                        k = min(i, j)
                        sc = sabs[k] + abs(float(c)) * mabs[k]
                    worst_e = max(worst_e,
                                  float(abs(L[i, j] - R[i, j])) / sc)
            dd = float(abs(mp.det(G) - mp.det(R))
                       / max(abs(mp.det(G)), mp.mpf("1e-300")))
            worst_d = max(worst_d, dd)
    return worst_e, worst_d


def mp_dict_block(p):
    """leg B mp ward on w9: t_0 = 0, F0_n = F_n (n >= 1), dual-norm
    Q_{n-1} = t^T H_n^{-1} t (dps 60), n = 8/12."""
    import mpmath as mp
    mp.mp.dps = MP_DPS_A
    mmom, smom = BH.mp_moments(p["d"], p["dsm"], 12, MP_DPS_A)
    c = smom[0] / mmom[0]
    tmom = [smom[i] - c * mmom[i] for i in range(13)]
    t0rel = float(abs(tmom[0]) / abs(smom[0]))
    out = {}
    for n in (8, 12):
        H = mp.matrix([[mmom[i + j] for j in range(n)]
                       for i in range(n)])
        v = mp.matrix([mmom[n + i] for i in range(n)])
        tq = mp.matrix([tmom[i] for i in range(n)])
        sv = mp.lu_solve(H, v)
        st = mp.lu_solve(H, tq)
        F0n = tmom[n] - sum(v[i] * st[i] for i in range(n))
        Q = sum(tq[i] * st[i] for i in range(n))
        r = p["rows"][n]
        F_ch = r["fb"] * math.exp(r["Ls"])
        Q_ch = float(np.sum(p["rho"][1:n]))
        devF = abs(float(F0n) / F_ch - 1.0)
        devQ = abs(float(Q) / Q_ch - 1.0)
        out[n] = (devF, devQ)
    return t0rel, out


def mp_deep_cd(p, m_lo, dps):
    """leg C mp on w9 through the FULL depth: T = intint
    [K_N - K_lo] dsigma dsigma vs the mp tail sum (dps 160).
    pihat_N uses free-prefix recursion data only; h_N never
    computed."""
    import mpmath as mp
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wtm = ([mp.mpf(float(w)) for w in d["ws"]]
           + [-mp.mpf(float(v)) for v in d["vs"]])
    bns = ([mp.mpf(float(x)) for x in dsm["xs"]]
           + [mp.mpf(float(y)) for y in dsm["ys"]])
    bwm = ([mp.mpf(float(w)) for w in dsm["ws"]]
           + [-mp.mpf(float(v)) for v in dsm["vs"]])
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    bk = [mp.mpf(1)] * len(bns)
    bkm = [mp.mpf(0)] * len(bns)
    dbk = [mp.mpf(0)] * len(bns)
    dbkm = [mp.mpf(0)] * len(bns)
    hs = [mp.fsum(w * q * q for w, q in zip(wtm, pk))]
    S_tail = mp.mpf(0)
    snap = None
    for k in range(N):
        if k == m_lo:
            snap = (list(bk), list(bkm), list(dbk), list(dbkm),
                    hs[m_lo - 1])
        if k >= m_lo:
            Fk = mp.fsum(w * q for w, q in zip(bwm, bk))
            S_tail += Fk * Fk / hs[k]
        a = mp.fsum(w * x * q * q
                    for w, x, q in zip(wtm, nds, pk)) / hs[k]
        g = (hs[k] / hs[k - 1]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * q - g * r for x, q, r in zip(nds, pk, pkm)]
        nb = [(x - a) * q - g * r for x, q, r in zip(bns, bk, bkm)]
        ndb = [q + (x - a) * dq - g * dr
               for x, q, dq, dr in zip(bns, bk, dbk, dbkm)]
        pkm, pk = pk, nx
        bkm, bk = bk, nb
        dbkm, dbk = dbk, ndb
        if k + 1 <= N - 1:
            hs.append(mp.fsum(w * q * q for w, q in zip(wtm, pk)))

    def cd_double(Pv, Pm, dPv, dPm, h):
        A = len(bns)
        tot = mp.mpf(0)
        for a_ in range(A):
            wa = bwm[a_]
            xa = bns[a_]
            Pa, Pma = Pv[a_], Pm[a_]
            for b_ in range(a_ + 1, A):
                tot += (2 * wa * bwm[b_]
                        * (Pa * Pm[b_] - Pma * Pv[b_])
                        / (xa - bns[b_]))
            tot += wa * wa * (dPv[a_] * Pma - dPm[a_] * Pa)
        return tot / h

    T_hi = cd_double(bk, bkm, dbk, dbkm, hs[N - 1])
    lo_bk, lo_bkm, lo_dbk, lo_dbkm, h_lo = snap
    T_lo = cd_double(lo_bk, lo_bkm, lo_dbk, lo_dbkm, h_lo)
    T_cd = T_hi - T_lo
    dev = float(abs(T_cd - S_tail) / abs(S_tail))
    f64_tail = float(p["St"] - float(p["S"][m_lo - 1]))
    dev_f64 = abs(float(S_tail) / f64_tail - 1.0)
    return dev, dev_f64, float(S_tail), len(bns)


# ------------------------------------------------- profile helpers
def tail_profile(p, parity=None):
    N = p["N"]
    T = p["St"] - float(p["S"][CD_LO - 1])
    n_arr = np.arange(CD_LO, N)
    v = N * np.asarray(p["rho"][CD_LO:], float) / T
    x = n_arr / float(N)
    if parity is not None:
        m_ = (n_arr % 2) == parity
        x, v = x[m_], v[m_]
    edges = np.linspace(PROF_LO, PROF_HI, PROF_BINS + 1)
    idx = np.digitize(x, edges) - 1
    prof = np.zeros(PROF_BINS)
    for b in range(PROF_BINS):
        sel = idx == b
        if np.any(sel):
            prof[b] = float(np.mean(v[sel]))
    return prof


def rel_l1(a, b):
    den = 0.5 * (float(np.sum(np.abs(a))) + float(np.sum(np.abs(b))))
    return float(np.sum(np.abs(a - b))) / max(den, 1e-300)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("border_centering_probe -- PRIME.PORT.BORDER."
          "CENTERING.01 (round 248)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (five known rungs, mp deep CD "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "machinery imported verbatim (r244 BH.wpack: rho/S/chain "
          "bitwise); toy budgets %s, real budgets %s; congruence "
          "bars %.0e (f64, 42+3 worlds) / %.0e (mp dps %d, w9); "
          "dictionary bars t_0 %.0e/%.0e, F0/dual-norm %.0e/%.0e; "
          "quiet range k = 1..7, u-moment source bar %.0e, level "
          "bar %.0e, trend bar %.2f, breakpoint bar %.1f decade; "
          "CD (m_hi, m_lo) = (%d, %d) bar %.0e (+ self-alias abs "
          "guard %.0e), mp deep dps %d bar %.0e; profile: %d bins "
          "on [%.2f, %.2f], rel-L1, DEV bar %.2f, BLIND bar %.2f, "
          "BLIND = two largest-N; naming bars %.1f/%.1f/%.1f "
          "decades + tail frac %.1f; ALL verdict rules sealed in "
          "the frozen spec"
          % (str([str(b) for b in B_TOY]), str(B_REAL),
             CONG_F64_BAR, CONG_MP_BAR, MP_DPS_A, T0_F64_BAR,
             T0_MP_BAR, F0_BAR_8, F0_BAR_12, UMOM_EXACT_BAR,
             QUIET_LEVEL_BAR, QUIET_TREND_BAR, BREAK_DECADE,
             CD_HI, CD_LO, CD_BAR, CD_ABS_GUARD, MP_DPS_C,
             CD_MP_BAR, PROF_BINS, PROF_LO, PROF_HI, PROF_DEV_BAR,
             PROF_BLIND_BAR, HEAD_DEC_BAR, SIL_SCR_BAR,
             SIL_EPS_BAR, TAILFRAC_BAR))

    # ---------------- S1: leg A toy congruence (rationals)
    section("S1  LEG A -- CENTERING CONGRUENCE (rationals) + m1")
    JFn = [Fr(-7, 8), Fr(-5, 8), Fr(-3, 8), Fr(-1, 8), Fr(1, 8),
           Fr(3, 8), Fr(5, 8), Fr(7, 8), Fr(0, 1)]
    JFw = [Fr(3, 7), Fr(-2, 9), Fr(5, 11), Fr(1, 4), Fr(-3, 8),
           Fr(2, 5), Fr(-1, 6), Fr(4, 9), Fr(1, 3)]
    SBn = [Fr(-13, 16), Fr(-7, 16), Fr(-1, 16), Fr(5, 16),
           Fr(11, 16)]
    SBw = [Fr(2, 5), Fr(-1, 7), Fr(3, 8), Fr(-2, 11), Fr(1, 3)]
    NTOY = 4
    al, hs, _v = PB.toy_chain(JFn, JFw, NTOY + 1)
    mom = [sum(w * x ** k for w, x in zip(JFw, JFn))
           for k in range(2 * NTOY + 4)]
    smom = [sum(w * x ** k for w, x in zip(SBw, SBn))
            for k in range(NTOY + 2)]
    Ftoy = [sum(w * PB.toy_eval(al, hs, k, x)
                for w, x in zip(SBw, SBn)) for k in range(NTOY + 1)]
    rhotoy = [Ftoy[k] * Ftoy[k] / hs[k] for k in range(NTOY + 1)]
    ct = smom[0] / mom[0]
    tmom = [smom[i] - ct * mom[i] for i in range(NTOY + 2)]

    def Hm(n):
        return [[mom[i + j] for j in range(n)] for i in range(n)]

    def Gb(n, B, border):
        M = [[mom[i + j] for j in range(n)] + [border[i]]
             for i in range(n)]
        M.append([border[j] for j in range(n)] + [B])
        return M

    ok_e = ok_d = ok_f = True
    for n in range(2, NTOY + 1):
        for B in B_TOY:
            G = Gb(n, B, smom)
            E = [[Fr(1) if i == j else Fr(0)
                  for j in range(n + 1)] for i in range(n + 1)]
            E[0][n] = -ct
            L = fr_matmul(fr_transpose(E), fr_matmul(G, E))
            R = Gb(n, B - rhotoy[0], tmom)
            ok_e = ok_e and (L == R)
            ok_d = ok_d and (PB.frac_det(G) == PB.frac_det(R))
    # centered moment route: F0_0 = 0, F0_n = F_n for n >= 1
    ok_f = ok_f and (tmom[0] == 0)
    for n in range(1, NTOY + 1):
        v = [mom[n + i] for i in range(n)]
        tq = [tmom[i] for i in range(n)]
        st = PB.frac_solve(Hm(n), tq)
        F0n = tmom[n] - sum(vi * si for vi, si in zip(v, st))
        ok_f = ok_f and (F0n == Ftoy[n])
    check("G10-congruence-exact-toy", ok_e and ok_d and ok_f,
          "rationals (n = 2..4, both budgets): E^T [[H,u],[u^T,B]] "
          "E == [[H, u0],[u0^T, B - rho_0]] ENTRYWISE with E = "
          "[[I, -c e_0],[0, 1]], c = F_0/h_0; det equality (det E "
          "= 1 => congruence, PSD/inertia-equivalence); centered "
          "moment route: F0_0 = t_0 = 0 and F0_n = F_n for n >= 1 "
          "EXACT -- the geometric rank-1 head rho_0 is "
          "ALGEBRAICALLY FULLY ELIMINABLE")
    # m1: wrong centering coefficient
    cp = ct * Fr(8, 7)
    n = 3
    B = B_TOY[0]
    G = Gb(n, B, smom)
    E = [[Fr(1) if i == j else Fr(0)
          for j in range(n + 1)] for i in range(n + 1)]
    E[0][n] = -cp
    L = fr_matmul(fr_transpose(E), fr_matmul(G, E))
    R = Gb(n, B - rhotoy[0], tmom)
    gap_b = L[0][n] - R[0][n]
    gap_c = L[n][n] - R[n][n]
    okm1 = (gap_b == -(cp - ct) * mom[0]
            and gap_c == mom[0] * (cp - ct) ** 2
            and gap_b != 0 and gap_c != 0)
    check("G11-mustfail-m1-wrong-c", okm1,
          "c' = 8c/7 breaks the congruence LOUDLY and EXACTLY: "
          "border entry 0 off by -(c'-c) m_0 != 0, corner off by "
          "+m_0 (c'-c)^2 != 0 (rationals) -- the centering "
          "coefficient c = F_0/h_0 is the unique head eliminator")

    # ---------------- S2: ladder + controls + blind seal
    section("S2  LADDER + CONTROLS + BLIND SEAL")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    packs = [BH.wpack(kz) for kz in kzs]
    packs.sort(key=lambda p: (p["N"], p["kz"]))
    by_kz = {p["kz"]: p for p in packs}
    blind = packs[-2:]
    dev = packs[:-2]
    dev_kz = {p["kz"] for p in dev}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okC = all(p["nf"] is None for p in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    check("G20-census", okC and okCf,
          "free prefix positive on %d/%d MAIN windows (N in "
          "[%d, %d]); control flips re-derived AT the sealed "
          "degrees %s" % (
              sum(1 for p in packs if p["nf"] is None), len(packs),
              packs[0]["N"], packs[-1]["N"],
              str({c: ctrl[c]["nf"] for c in ctrl})))
    check("G21-blind-seal", len(blind) == 2 and len(dev) >= 3,
          "BLIND = two largest-N rungs by the sealed r246 rule: "
          "kz %s (N %s); DEV = %d rungs; leg-B trend fits and "
          "leg-D classification run on DEV, BLIND enters only "
          "confirmation" % (str([p["kz"] for p in blind]),
                            str([p["N"] for p in blind]),
                            len(dev)))

    # ---------------- S3: leg A on real windows
    section("S3  LEG A -- CONGRUENCE ON REAL WINDOWS (world-blind)")
    allw = packs + list(ctrl.values())
    worst = 0.0
    for p in allw:
        for B in B_REAL:
            d_, _c = cong_dev_f64(p, 8, B)
            worst = max(worst, d_)
    check("G30-congruence-f64-worldblind", worst <= CONG_F64_BAR,
          "E^T G E vs the centered form, n = 8, B in %s, on ALL "
          "%d MAIN + 3 control worlds: worst per-entry dev %.1e "
          "on the pre-cancellation scale (bar %.0e) -- the "
          "congruence is ALGEBRA, it holds on every world "
          "(world-blind by construction): eliminating the head "
          "consumes no arithmetic" % (str(B_REAL), len(packs),
                                      worst, CONG_F64_BAR))
    e9, d9 = mp_cong_block(by_kz[9])
    check("G31-congruence-mp-w9", e9 <= CONG_MP_BAR
          and d9 <= CONG_MP_BAR,
          "mp ward (dps %d) on the real w9, n = 8/12, both "
          "budgets: entrywise worst %.1e, det-route worst %.1e "
          "(bar %.0e) -- the head elimination is exact on the "
          "true comb, not an f64 artifact"
          % (MP_DPS_A, e9, d9, CONG_MP_BAR))

    # ---------------- S4: leg B dictionary (exact)
    section("S4  LEG B -- SIGMA0 DICTIONARY (rationals + mp) + m3")
    # b1/b2 constructive annihilation + triangular converse
    okb = True
    # pihat values at toy window atoms (for mutilde-projections)
    pw = [[PB.toy_eval(al, hs, k, x) for x in JFn]
          for k in range(NTOY + 1)]
    for m_ in (2, 3):
        # sigma2 = sigma0 - sum_{k<=m} (F_k/h_k) pihat_k dmutilde
        t2 = []
        for j in range(NTOY + 1):
            proj = sum((Ftoy[k] / hs[k])
                       * sum(w * (x ** j) * pw[k][i]
                             for i, (w, x) in enumerate(zip(JFw,
                                                            JFn)))
                       for k in range(1, m_ + 1))
            t2.append(tmom[j] - proj)
        okb = okb and all(t2[j] == 0 for j in range(m_ + 1))
        # F-values of sigma2: 0 for k <= m, F_k for k > m
        for k in range(NTOY + 1):
            v = [mom[k + i] for i in range(k)]
            tq = [t2[i] for i in range(k)]
            st = PB.frac_solve(Hm(k), tq) if k else []
            F2k = t2[k] - sum(vi * si for vi, si in zip(v, st))
            want = Fr(0) if k <= m_ else Ftoy[k]
            okb = okb and (F2k == want)
    # triangular converse: reconstruct F from t by forward subst
    okc = True
    Frec = [Fr(0)]
    for j in range(1, NTOY + 1):
        bjk = [sum(w * (x ** j) * pw[k][i]
                   for i, (w, x) in enumerate(zip(JFw, JFn)))
               / hs[k] for k in range(j + 1)]
        okc = okc and (bjk[j] == 1)  # monic: b_{jj} = 1
        Frec.append(tmom[j] - sum(bjk[k] * Frec[k]
                                  for k in range(1, j)))
    okc = okc and all(Frec[j] == Ftoy[j]
                      for j in range(1, NTOY + 1))
    # b3 dual norm
    okq = True
    for m_ in (2, 3, 4):
        tq = [tmom[i] for i in range(m_ + 1)]
        st = PB.frac_solve(Hm(m_ + 1), tq)
        Q = sum(ti * si for ti, si in zip(tq, st))
        okq = okq and (Q == sum(rhotoy[k] for k in range(1, m_ + 1)))
    check("G40-dictionary-exact-toy", okb and okc and okq,
          "rationals: t_0 = 0; CONSTRUCTIVE ANNIHILATION (m = 2, "
          "3): subtracting the projections (F_k/h_k) pihat_k "
          "dmutilde kills moments 0..m EXACTLY and leaves F_k "
          "(k > m) untouched; TRIANGULAR CONVERSE: forward "
          "substitution through t_j = sum b_{jk} F_k (b_{jj} = 1 "
          "monic) reconstructs F_1..F_4 exactly => F_1 = .. = F_m "
          "= 0 <=> sigma0 annihilates P_m; DUAL-NORM IDENTITY: "
          "Q_m = t^T H_{m+1}^{-1} t EXACT at m = 2..4 (centered "
          "partial Parseval): Q_m IS the squared dual norm of "
          "sigma0|P_m in the mutilde form")
    t0rel, dct = mp_dict_block(by_kz[9])
    okm = (t0rel <= T0_MP_BAR
           and dct[8][0] <= F0_BAR_8 and dct[8][1] <= F0_BAR_8
           and dct[12][0] <= F0_BAR_12 and dct[12][1] <= F0_BAR_12)
    check("G41-dictionary-mp-w9", okm,
          "mp (dps %d) on the real w9: t_0/s_0 = %.1e (bar %.0e); "
          "F0_n vs chain F_n dev %.1e (n = 8) / %.1e (n = 12) "
          "(bars %.0e/%.0e); dual-norm Q_7 dev %.1e / Q_11 dev "
          "%.1e -- the centered moment route and the dual-norm "
          "identity hold on the true comb"
          % (MP_DPS_A, t0rel, T0_MP_BAR, dct[8][0], dct[12][0],
             F0_BAR_8, F0_BAR_12, dct[8][1], dct[12][1]))
    # m3: uncentered alias
    q0 = [smom[i] for i in range(4)]
    st = PB.frac_solve(Hm(4), q0)
    Qun = sum(qi * si for qi, si in zip(q0, st))
    okm3 = (smom[0] != 0
            and Qun == sum(rhotoy[k] for k in range(4))
            and Qun != sum(rhotoy[k] for k in range(1, 4)))
    check("G42-mustfail-m3-uncentered", okm3,
          "the UNCENTERED sigma does NOT annihilate P_0: t_0("
          "sigma) = s_0 != 0 and the uncentered Parseval q^T "
          "H^{-1} q = Q + rho_0 != Q EXACTLY (rationals) -- the "
          "centering is NECESSARY for the dictionary; on w9 the "
          "uncentered functional carries the full geometric head "
          "(rho_0 share ~ 0.37, r246)")

    # ---------------- S5: leg B measurement -- the quiet zone
    section("S5  LEG B -- SIGMA0 MOMENT TABLES + QUIET TYPING")
    # per-window tables
    Ns_dev = [p["N"] for p in dev]
    for p in packs:
        wxa, wwa, bxa, bwa = world_arrays(p)
        mm, mabs = f64_moments(wxa, wwa, KTAB)
        sm, sabs = f64_moments(bxa, bwa, KTAB)
        c = sm[0] / mm[0]
        p["tn"] = [abs(sm[k] - c * mm[k])
                   / (sabs[k] + abs(c) * mabs[k])
                   for k in range(KTAB + 1)]
        p["gk"] = [abs(p["rows"][k]["fb"])
                   / math.sqrt(p["rows"][k]["eta"])
                   for k in range(KTAB + 1)]
        Q7 = float(p["S"][7]) - float(p["rho"][0])
        p["Gq"] = math.sqrt(max(Q7, 0.0) / p["St"])
    info("sigma0 moment table, MAIN ladder medians (k: |t_k| "
         "normalized on the pre-cancellation scale | g_k = "
         "|F_k|/sqrt(h_k) | DEV log-log slope of g_k vs N):")
    for k in range(KTAB + 1):
        med_t = float(np.median([p["tn"][k] for p in packs]))
        med_g = float(np.median([p["gk"][k] for p in packs]))
        if k >= 1:
            sl = float(np.polyfit(
                np.log(Ns_dev),
                np.log([max(p["gk"][k], 1e-300) for p in dev]),
                1)[0])
            info("  k=%-3d tnorm med %.2e | g med %.2e | "
                 "slope %+.2f" % (k, med_t, med_g, sl))
        else:
            info("  k=%-3d tnorm med %.2e (t_0 structural zero) | "
                 "g_0 med %.2e (head, eliminated)"
                 % (k, med_t, med_g))
    # u-moment source check (the builder question)
    um_worst = 0.0
    for p in dev:
        alpha = PIK.build_rung(p["kz"])["alpha"]
        ka = core.atoms_in(alpha)
        uu = np.asarray(core.U_ALL[:ka], float)
        mmw = np.asarray(core.MU_ALL[:ka], float)
        ug, uw = PB.smooth_comb(alpha)
        for k in range(UMOM_KMAX + 1):
            a_ = float(np.sum(mmw * uu ** k))
            b_ = float(np.sum(uw * ug ** k))
            um_worst = max(um_worst,
                           abs(a_ - b_) / (abs(a_) + abs(b_)))
    Gq_dev = [p["Gq"] for p in dev]
    med_Gq = float(np.median(Gq_dev))
    sl_Gq = float(np.polyfit(np.log(Ns_dev),
                             np.log(Gq_dev), 1)[0])
    if um_worst <= UMOM_EXACT_BAR:
        quiet_t = "QUIETZONE_EXACT_MOMENTS"
    elif med_Gq <= QUIET_LEVEL_BAR and sl_Gq <= QUIET_TREND_BAR:
        quiet_t = "QUIETZONE_ASYMPTOTIC_MOMENTS"
    else:
        quiet_t = "QUIETZONE_FINITE_NUMERICAL_ONLY"
    check("G50-quietzone-typed", True,
          "SEALED RULE result: %s -- u-moment source check "
          "(does sigma share low u-moments with the comb BY "
          "CONSTRUCTION?): worst rel dev %.1e over k = 0..%d on "
          "all DEV windows (exact bar %.0e) => %s; designated "
          "statistic G_q = sqrt(Q_7/S_{N-1}): DEV median %.2e "
          "(level bar %.0e), DEV log-log slope %+.2f vs N (trend "
          "bar %.2f); the number 7 is the sealed r246 head cut, "
          "not an oracle -- no eight-bit narrative"
          % (quiet_t, um_worst, UMOM_KMAX, UMOM_EXACT_BAR,
             "SHARED (exact identity)" if um_worst <= UMOM_EXACT_BAR
             else "NOT exact (PNT-model level, no construction "
             "identity)", med_Gq, QUIET_LEVEL_BAR, sl_Gq,
             QUIET_TREND_BAR))
    # SCRAMBLE break table (w9 base)
    p9 = by_kz[9]
    scr = ctrl["SCRAMBLE"]
    eps = ctrl["EPSTEIN"]
    decs = [math.log10(float(scr["rho"][k]) / float(p9["rho"][k]))
            for k in range(1, KTAB + 1)]
    bp = next((k for k, d_ in zip(range(1, KTAB + 1), decs)
               if d_ >= BREAK_DECADE), None)
    info("SCRAMBLE decade excess log10(rho_SCR/rho_MAIN), k = "
         "1..12: %s" % str(["%+.1f" % d_ for d_ in decs]))
    check("G51-scramble-breakpoint", bp is not None,
          "SEALED breakpoint rule (first k in 1..12 with excess "
          ">= %.1f decade): k = %s; median excess over the quiet "
          "range k = 1..7: %+.2f decades: the sigma0 silence is "
          "an ARITHMETIC observable (SCRAMBLE destroys it), not "
          "a builder artifact"
          % (BREAK_DECADE, str(bp),
             float(np.median(decs[:7]))))

    # ---------------- S6: leg C tail-kernel compression
    section("S6  LEG C -- TAIL-KERNEL COMPRESSION + m2")
    # toy exact
    nodes0 = SBn + JFn
    wts0 = SBw + [-ct * w for w in JFw]
    P0, dP0 = toy_pd(al, hs, nodes0, NTOY)
    T42 = (toy_cd_double(P0, dP0, hs, 4, nodes0, wts0)
           - toy_cd_double(P0, dP0, hs, 2, nodes0, wts0))
    okc1 = (T42 == rhotoy[2] + rhotoy[3])
    Pu, dPu = toy_pd(al, hs, SBn, NTOY)
    T42u = (toy_cd_double(Pu, dPu, hs, 4, SBn, SBw)
            - toy_cd_double(Pu, dPu, hs, 2, SBn, SBw))
    okc2 = (T42u == T42)
    # spectral == CD at sample points
    za, zb = Fr(1, 3), Fr(-2, 7)
    Pz, dPz = toy_pd(al, hs, [za, zb], NTOY)
    cd_ab = ((Pz[4][0] * Pz[3][1] - Pz[3][0] * Pz[4][1])
             / (hs[3] * (za - zb)))
    sp_ab = sum(Pz[k][0] * Pz[k][1] / hs[k] for k in range(4))
    cd_aa = (dPz[4][0] * Pz[3][0] - dPz[3][0] * Pz[4][0]) / hs[3]
    sp_aa = sum(Pz[k][0] * Pz[k][0] / hs[k] for k in range(4))
    okc3 = (cd_ab == sp_ab) and (cd_aa == sp_aa)
    # m2: index-shifted tail kernel
    T41 = (toy_cd_double(P0, dP0, hs, 4, nodes0, wts0)
           - toy_cd_double(P0, dP0, hs, 1, nodes0, wts0))
    okm2 = (T41 - T42 == rhotoy[1]) and rhotoy[1] != 0
    check("G60-tailkernel-exact-toy", okc1 and okc2 and okc3
          and okm2,
          "rationals: intint [K_4 - K_2] dsigma0 dsigma0 = rho_2 "
          "+ rho_3 EXACT (double pairing over the sigma0 atom "
          "union, confluent diagonal); CENTERING-INVARIANCE: the "
          "same readout over sigma equals the sigma0 readout "
          "EXACTLY (the difference kernel only sees modes >= 2); "
          "spectral == CD form at sample points incl. diagonal; "
          "must-fail m2: [K_4 - K_1] differs by exactly rho_1 != "
          "0, loud -- the K_7-for-K_8 index shift in toy form")
    # f64 ladder
    worst_rel = 0.0
    worst_abs = 0.0
    for p in allw:
        T_cd, T_dir, ksc = cd_tail_f64(p, CD_HI, CD_LO)
        if abs(T_dir) > 1e-12 * p["St"]:
            worst_rel = max(worst_rel,
                            abs(T_cd / T_dir - 1.0))
        else:
            worst_abs = max(worst_abs, abs(T_cd - T_dir)
                            / max(ksc, 1e-300))
    ok61 = worst_rel <= CD_BAR and worst_abs <= CD_ABS_GUARD
    inv_worst = 0.0
    for p in [p9] + list(ctrl.values()):
        Ta, Td, _k1 = cd_tail_f64(p, CD_HI, CD_LO, sigma0=False)
        Tb, _d2, ksc = cd_tail_f64(p, CD_HI, CD_LO, sigma0=True)
        if abs(Td) > 1e-12 * p["St"]:
            inv_worst = max(inv_worst, abs(Tb / Ta - 1.0))
        else:
            inv_worst = max(inv_worst,
                            abs(Tb - Ta) / max(ksc, 1e-300))
    ok62 = inv_worst <= CD_BAR
    check("G61-tailkernel-f64-ladder", ok61 and ok62,
          "f64 (m_hi, m_lo) = (%d, %d) on ALL %d MAIN + 3 control "
          "worlds: worst rel dev %.1e (bar %.0e; SMOOTH sigma0 == "
          "0 self-alias on the abs mass-norm guard: %.1e <= %.0e, "
          "typed pre-run); SIGMA0-INVARIANCE on w9 + 3 controls: "
          "worst %.1e -- the tail readout does not see the "
          "centering, world-blind as algebra"
          % (CD_HI, CD_LO, len(packs), worst_rel, CD_BAR,
             worst_abs, CD_ABS_GUARD, inv_worst))
    if smoke:
        check("G62-tailkernel-mp-deep", True,
              "SKIPPED in smoke mode (dps-%d full-depth block on "
              "w9)" % MP_DPS_C)
    else:
        t_mp0 = time.time()
        dev_mp, dev_f64, S_tail, natoms = mp_deep_cd(p9, CD_LO,
                                                     MP_DPS_C)
        check("G62-tailkernel-mp-deep", dev_mp <= CD_MP_BAR,
              "mp (dps %d) on w9 through the FULL depth N = %d "
              "(%d border atoms, %.0f s): T = intint [K_N - K_8] "
              "dsigma dsigma matches the mp tail sum sum_{n>=8} "
              "rho_n = %.6f to rel dev %.1e (bar %.0e; f64 chain "
              "drift %.1e) -- the extensive tail IS one terminal "
              "CD-kernel-difference readout: extensive "
              "information in the SOURCE, one object in the "
              "analytic STATE"
              % (MP_DPS_C, p9["N"], natoms, time.time() - t_mp0,
                 S_tail, dev_mp, CD_MP_BAR, dev_f64))

    # ---------------- S7: leg D tail-profile typing
    section("S7  LEG D -- TAIL-PROFILE TYPING (DEV/BLIND)")
    for p in packs:
        p["prof"] = tail_profile(p)
        p["prof_e"] = tail_profile(p, parity=0)
        p["prof_o"] = tail_profile(p, parity=1)
        p["eo"] = rel_l1(p["prof_e"], p["prof_o"])
    pair_l1 = []
    for i in range(len(dev)):
        for j in range(i + 1, len(dev)):
            pair_l1.append(rel_l1(dev[i]["prof"], dev[j]["prof"]))
    med_pair = float(np.median(pair_l1))
    devmean = np.mean([p["prof"] for p in dev], axis=0)
    blind_uni = [rel_l1(p["prof"], devmean) for p in blind]
    med_eo = float(np.median([p["eo"] for p in dev]))
    blind_eo = [p["eo"] for p in blind]
    tfrac = [(p["St"] - float(p["S"][CD_LO - 1])) / p["St"]
             for p in packs]
    info("tail share T_w/S_{N-1} in [%.2f, %.2f] med %.2f; DEV "
         "pairwise rel-L1: med %.3f, q25/q75 %.3f/%.3f, max %.3f "
         "(%d pairs); blind-vs-DEVmean %.3f/%.3f; within-window "
         "even/odd rel-L1: DEV med %.3f, blind %.3f/%.3f"
         % (min(tfrac), max(tfrac), float(np.median(tfrac)),
            med_pair, float(np.percentile(pair_l1, 25)),
            float(np.percentile(pair_l1, 75)), max(pair_l1),
            len(pair_l1), blind_uni[0], blind_uni[1], med_eo,
            blind_eo[0], blind_eo[1]))
    prof_mod = ""
    if med_pair <= PROF_DEV_BAR:
        tail_t = "EXTENSIVE_REGULAR_TAIL"
        if not all(b <= PROF_BLIND_BAR for b in blind_uni):
            prof_mod = " + TAILPROFILE_BLIND_CHECK_FAILED"
    elif med_eo <= PROF_DEV_BAR:
        tail_t = "EXTENSIVE_QUENCHED_TAIL"
        if not all(b <= PROF_BLIND_BAR for b in blind_eo):
            prof_mod = " + TAILPROFILE_BLIND_CHECK_FAILED"
    else:
        tail_t = "EXTENSIVE_IRREGULAR_TAIL"
    conseq = {"EXTENSIVE_REGULAR_TAIL":
              "one integrated density formula covers the tail",
              "EXTENSIVE_QUENCHED_TAIL":
              "window-specific phi_w with a single uniform proof "
              "rule",
              "EXTENSIVE_IRREGULAR_TAIL":
              "the full discrete source stands -- no macroprofile,"
              " no integrated density formula, no per-window "
              "profile rule"}[tail_t]
    check("G70-tail-profile-typed", True,
          "SEALED RULE result: %s%s -- d1 (universal phi): DEV "
          "median pairwise rel-L1 %.3f vs bar %.2f; d2 (quenched "
          "phi_w): within-window even/odd DEV median %.3f vs bar "
          "%.2f (blind %.3f/%.3f vs %.2f); collapse statistics "
          "above (18 bins on [%.2f, %.2f], sealed bandwidth 0.05)"
          % (tail_t, prof_mod, med_pair, PROF_DEV_BAR, med_eo,
             PROF_DEV_BAR, blind_eo[0], blind_eo[1],
             PROF_BLIND_BAR, PROF_LO, PROF_HI))
    check("G71-analytic-consequence", True,
          "documented under the sealed verdict: %s -- EXTENSIVE "
          "is the r246 finding (K_0.9 ~ 0.9 N, blind-checked "
          "there), THIS round types the PROFILE; the consequence "
          "for the RHP lane: %s" % (tail_t, conseq))

    # ---------------- S8: leg E naming-correction record
    section("S8  LEG E -- THREE-ZONE NAMING RECORD")
    dec0_eps = math.log10(float(eps["rho"][0]) / float(p9["rho"][0]))
    dec0_scr = math.log10(float(scr["rho"][0]) / float(p9["rho"][0]))
    ok80 = (abs(dec0_eps) <= HEAD_DEC_BAR
            and abs(dec0_scr) <= HEAD_DEC_BAR)
    check("G80-head-geometric", ok80,
          "rho_0 decade offsets vs MAIN w9: EPSTEIN %+.3f, "
          "SCRAMBLE %+.3f (bar %.1f): the head LEVEL is "
          "world-shared -- together with the leg-A congruence "
          "(world-blind elimination) the head is GEOMETRY: "
          "GEOMETRIC_RANK1_HEAD" % (dec0_eps, dec0_scr,
                                    HEAD_DEC_BAR))
    dec_eps = [math.log10(float(eps["rho"][k]) / float(p9["rho"][k]))
               for k in QUIET_KS]
    med_scr = float(np.median(decs[:7]))
    med_eps = float(np.median(dec_eps))
    ok81 = med_scr >= SIL_SCR_BAR and abs(med_eps) <= SIL_EPS_BAR
    check("G81-silence-arithmetic", ok81,
          "quiet-zone decade excess (k = 1..7): SCRAMBLE median "
          "%+.2f (bar >= %.1f), EPSTEIN median %+.3f (bar <= "
          "%.1f): the SILENCE separates the arithmetic worlds by "
          "decades while the lattice world sits on MAIN -- "
          "LOWMODE_ARITHMETIC_SILENCE" % (med_scr, SIL_SCR_BAR,
                                          med_eps, SIL_EPS_BAR))
    nf = scr["nf"]
    dl = (np.asarray(scr["rho"][:nf], float)
          - np.asarray(p9["rho"][:nf], float))
    tot = float(np.sum(dl))
    tail_fr = float(np.sum(dl[CD_LO:])) / tot if tot != 0 else 0.0
    ok82 = tail_fr >= TAILFRAC_BAR
    check("G82-tail-pairing-sensitive", ok82,
          "SCRAMBLE pre-flip (n < %d) budget excess: fraction in "
          "n >= %d is %.3f (bar %.1f; r246 measured 0.84) -- "
          "EXTENSIVE_PAIRING_SENSITIVE_TAIL; NAMING RECORD "
          "(sealed): the r246 label HEAD_CARRIES_ARITHMETIC was "
          "a MISNOMER -- its magnitude clause fired on the QUIET "
          "modes n = 1..7, not on the head mode 0 (G80: the head "
          "is world-shared geometry); the corrected three-zone "
          "typing is GEOMETRIC_RANK1_HEAD + LOWMODE_ARITHMETIC_"
          "SILENCE + EXTENSIVE_PAIRING_SENSITIVE_TAIL"
          % (nf, CD_LO, tail_fr, TAILFRAC_BAR))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a normal-form + "
          "typing round moves no edge); what the round adds: the "
          "bordered object in NORMAL FORM -- eliminable rank-1 "
          "head (congruence), the quiet zone as an exact sigma0 "
          "annihilation dictionary with dual-norm Q_m, the tail "
          "as ONE terminal CD readout, and the tail profile "
          "typed; the CENTERED_BASEFIBER campaign consumes "
          "sigma0, Q_m and the compressed tail as its objects")
    legA_ok = all(ok for nm, ok, _d in CHECKS
                  if nm.startswith(("G10", "G11", "G30", "G31")))
    legB_ok = all(ok for nm, ok, _d in CHECKS
                  if nm.startswith(("G40", "G41", "G42")))
    legC_ok = all(ok for nm, ok, _d in CHECKS
                  if nm.startswith(("G60", "G61", "G62")))
    legE_ok = ok80 and ok81 and ok82
    verd = " + ".join([
        "CENTERING_CONGRUENCE_EXACT" if legA_ok
        else "CENTERING_CONGRUENCE_OPEN",
        "SIGMA0_DICTIONARY_EXACT" if legB_ok
        else "SIGMA0_DICTIONARY_OPEN",
        quiet_t,
        "TAIL_KERNEL_COMPRESSED" if legC_ok
        else "TAIL_KERNEL_OPEN",
        tail_t + prof_mod,
        ("THREE_ZONE_NORMALFORM(GEOMETRIC_RANK1_HEAD + "
         "LOWMODE_ARITHMETIC_SILENCE + "
         "EXTENSIVE_PAIRING_SENSITIVE_TAIL)") if legE_ok
        else "THREE_ZONE_NORMALFORM_UNCONFIRMED"])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s%s -- PROVEN: the centering congruence, the sigma0 "
          "dictionary + dual norm, the tail-kernel compression "
          "(exact identities, world-blind); MEASURED: the quiet-"
          "zone typing, the SCRAMBLE breakpoint, the tail-profile "
          "class, the three-zone record; OPEN: the budget bound "
          "itself (the wall; r243 PAIRCORR_REENCODED stands); NO "
          "RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
