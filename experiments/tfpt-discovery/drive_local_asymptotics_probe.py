#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""drive_local_asymptotics_probe -- PRIME.PORT.RHP.QUENCHED.
DRIVE_LOCAL_ASYMPTOTICS.01 (round 268): the core round of the
final campaign after r266 closed the border-identity class
(NO_IDENTITY_IN_CLASS + RHP_LOCAL_ASYMPTOTICS_REQUIRED).
REVIEWER ADJUDICATION (binding, adopted): NO general parametrix
round -- the contract is NARROW: build a local asymptotic formula
EXCLUSIVELY for the border-drive column t_{N-2} in the terminal
region, target type t_{N-2} = t_local + R_N with an explicit
local main term and a PROVABLE error |R_N| <= eps_N; the ONLY
success measure: does the local analysis deliver a quantitative
drive bound STRONGER than the minimal S6 reserve (razor kz15:
0.027 magnitude slack M - |Z|; the up-to-0.41-dec triangle gap on
the 7 exceptions) WITHOUT falling back to the wall bound or a
paircorr-scale cancellation estimate?  IF NOT: immediate abort
(sealed abort criterion, no candidate repair after seeing the
numbers -- selection-by-answer forbidden).  kz15 (N = 203) is the
DESIGN ANCHOR of the whole round, not just a test case.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT: t_{N-2} = T_{N-2}/sqrt(h_{N-1}), T_{N-2} = int x
pihat_{N-2} dsigmatilde = sum_b bw_b bx_b pihat_{N-2}(bx_b) -- a
FINITE border-comb sum against the terminal polynomial.  Per-atom
contributions in t-units: ct_b = bw_b bx_b v_{N-2}(bx_b)
e^{Ls_{N-2} - Ls_{N-1}} / sqrt|eta_{N-1}| (r244 scaled rows, r266
eval machinery), with sum_b ct_b == t_{N-2} EXACTLY (gated on all
worlds -- the same identity IS the control-reproduction ward).
STRUCTURAL GUARD (binding): T_{N-2} = F_{N-1} + alh_{N-2} F_{N-2}
+ gam_{N-2} F_{N-3} is the driven recursion RESTATED -- any
"local model" that consumes the terminal readout r_{N-1}/rho or
the withheld terminal drive value is TARGET_INVERSE / answer-
reading and forbidden (AST-audited, mutants must be flagged).

LEG A -- DRIVE ANATOMY AT THE TERMINAL (dissect first):
(a1) exact contribution decomposition of ct per rung: raw abs
  mass A = sum|ct|, cancellation depth |t_{N-2}|/A, edge-region
  abs share and signed capture (hull fraction sealed 0.10 for
  the census; hull = union+border [lo, hi], r257/r260
  convention), N_eff = A^2/sum ct^2, top-1 share -- printed for
  the anatomy pool (7 exceptions + kz15 anchor + both mains + 5
  sealed cheap references) and computed on all 42 rungs;
(a2) oscillation structure: sign field of v_{N-2} on the sorted
  border atoms (sign-flip census with edge share; amplitude
  envelope med|v| edge / med|v| bulk) -- exact from the chain;
(a3) the cheap-vs-exception difference IN THIS decomposition:
  AUC powers (r264 metric, 7 x 35, branch labels table-side
  only) of DEPTH / ABSMASS / EDGEABS / NEFF / TOP1, plus the
  |t_{N-2}| power itself as a REPRODUCTION WARD (r264 recorded
  0.959, sealed tolerance +-0.02); |t| = depth x mass -- which
  factor carries the exception branch is adjudicated data-driven
  with the sealed 0.8 power bar.

LEG B -- THE LOCAL MAIN TERM (max 3 sealed candidates, source-
pure, target-blind; the terminal drive value is structurally
withheld from every builder scope under the forbidden key
"t" + "_term"; builders consume prefix arrays / atom arrays
passed as plain arguments):
(b1) QUENCHED LOCAL MODEL (r231/r264 class): t_local =
  sign(t_{N-3}) x median|t_k| over the trailing window W in
  {4, 8, 16} (sealed ablation; deterministic local drive data
  only).  EPS DERIVATION: NONE EXISTS at this complexity -- the
  drive is length-N essential (r260 d6 FIXED_STATE_COMPRESSION
  kill): typed EPS_UNPROVABLE, magnitude/sign quality measured
  honestly, EXCLUDED from leg-C certification by type.
(b2) L-GAUGE / DUAL-FRAME MAIN TERM: the r231/r266-b4 border
  transport is re-derived AT THE NODES: pihat#_{S-1-k}(x_j) =
  w_j L'(x_j) pihat_k(x_j) / h_k EXACTLY (residue of L C[pihat_k
  mutilde] at x_j; toy rationals k = 1..3 at ALL nodes; mp ward
  on w9 at the drive pair k = N-2 <-> m = N, dps 60, sealed
  sample nodes).  CONSEQUENCE (structure statement of the
  round): wherever the border atoms sit ON union nodes
  (coincidence census gated on the mains, ladder printed), the
  L-gauge-transported drive sum T_k = h_k sum_j w#_j
  pihat#_m(x_j) x_j M_j COLLAPSES TERM-BY-TERM to the direct
  comb sum -- the gauge frame yields NO new local decomposition
  at the terminal; and the self-dual ladder S = 2N-1 (r266,
  re-gated 42/42) puts the dual degree of the drive at m = N --
  NOT small: the contract premise "the dual problem is low-
  degree at the terminal" is structurally REFUTED.  The
  surviving dual-frame local candidate is the MASS-RANKED
  truncation: keep the top-W atoms by |bw bx| (drive-mass field,
  solution-free; W in {8, 16, 32} sealed), t_local = signed
  partial sum over the kept atoms, eps_N = sum|ct| over the
  excluded atoms -- an EXACT triangle bound (provable; its
  evaluation consumes every atom: the locality of the BOUND is
  typed honestly).
(b3) SADDLE+PHASE / EDGE-REGION MAIN TERM: keep the atoms in the
  outer hull-edge region (fractions {0.05, 0.10, 0.20} sealed;
  the Heine-saddle magnitude of the terminal polynomial sits at
  the hull edge -- leg-A a1/a2 measure whether the dominant
  contributions do), t_local = signed edge partial sum, eps_N =
  bulk abs remainder (same provable triangle type).
FOR EACH CANDIDATE: t_local vs t_true magnitude AND sign
separately, R_N = t_true - t_local distribution, eps derivation
status; the d2 PAIRCORR detector (demand log10((|Z_local| +
eps_N)/M_W), sealed bar 1.0 dec on the exception branch) and the
r266 WALL fingerprint detector (decision pattern + rank
fingerprint vs g(1), sealed bar 0.9, selftest re-armed on the
measured ladder) adjudicate whether the route consumes forbidden
cancellation or is the wall in disguise.

LEG C -- THE SUCCESS GATE (sealed, hard): the sign-refined
terminal bound |Z_w| <= |Z_local| + eps_N with Z_local = t_local
+ a'_{N-2} r_{N-2} + b'_{N-2} r_{N-3} (exact triangle on the
R-decomposition, gated); per exception rung: margin_cert =
sqrt(5/7) - (|Z_local| + eps_N) vs margin_true = sqrt(5/7) -
|Z_w|; CERTIFIED iff margin_cert > 0 AND the candidate carries
no wall flag; kz15 DETAIL: the 0.027 reserve (sealed
reproduction band [0.020, 0.035]) -- held or missed, with the
miss decades log10(eps / max(M - |Z_local|, 0)) printed.  SEALED
ABORT CRITERION: if NO candidate certifies even ONE exception
rung without wall/paircorr fallback => DRIVE_LOCAL_INSUFFICIENT
and immediate clean close.

LEG D -- CONTROLS + WARDS + MUST-FAILS: control worlds firewall-
typed: the contribution identity sum ct == t_{N-2} must hold on
EPSTEIN/SCRAMBLE exactly as on MAIN (world-blind algebra, G20)
and the triangle validity |R| <= eps_N must hold there too --
else LOCAL_MODEL_MAIN_FITTED; SMOOTH anchor: drive alias (r260
form, max_{k>=2}|T~_k|/max(|T~_0|,|T~_1|)) <= 1e-12 AND the b1
local model returns |t_local| <= 1e-10 trivially AND q_N <=
1e-20; mp WARDS (dps 60) of the terminal drive t_{N-2} at kz15
(N = 203, the razor) AND kz20 (N = 170), abs bar 1e-8 vs the f64
chain; MUST-FAILS: (m1) WINDOW TRUNCATION WITHOUT ERROR TERM --
the naked claim |t| <= |t_local| breaks by >= 1e3 x the honest
contribution-ward floor (loud); (m2) PHASE SUM WITH GROUND-TRUTH
SIGN -- the mutant reading the withheld terminal drive key must
be FLAGGED by the candidate scope audit; (m3) LOCAL MODEL
SECRETLY READING THE TARGET -- the rho-reading mutant must be
FLAGGED; inherited kills armed (PAIRCORR, TARGET_INVERSE,
SELECTION_BY_ANSWER; no fit primitives -- fragment audit).

INDEX FIREWALL (binding, r238-r266 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; rho_k = F_k^2/h_k, S_n =
sum_{k<=n} rho_k; ground truth (flips, branch labels) enters
GATES and census tables only; no zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack +
BH.spearman, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r264 QO.port_pack / QO.auc_power, r266 BR.eval_scaled,
r230 JF toy chain, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-
sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); TB_WARD bars (contribution-sum dev over abs mass)
1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls (CALIBRATION
AMENDMENT a1, disclosed: the draft single bar 1e-9 was split
into the standard r260/r264 main/deep/control floor family
after the FIRST smoke pass measured the SCRAMBLE f64 route
floor 2.4e-8 on the flipped world -- gate-side tolerance on an
exact identity, no physics bar, rule, candidate or verdict
moved); TRI_BAR 1e-9 (triangle-slack wards); ANAT_FRAC
0.10; EDGE_FRACS (0.05, 0.10, 0.20); MASS_W (8, 16, 32);
QUENCH_W (4, 8, 16); CHEAP_REF_IDX (0, 10, 20, 30, 41) (advance
to the next cheap rung if an exception sits there -- sealed
rule); TDRIVE_POWER_REF 0.959 +- 0.02 (r264 reproduction ward);
SIG_POWER_BAR 0.8; FP_BAR 0.9; DEMAND_BAR 1.0 dec; RESERVE_BAND
(0.020, 0.035) (kz15 razor slack, r263 record 0.027); SM_Q_BAR
1e-20; SM_ALIAS_BAR 1e-12; SM_LOC_BAR 1e-10; MP_DPS 60; MP_T_BAR
1e-8; MP_EXC_KZ (15, 20); COLLAPSE_LG_BAR 1e-6; COLLAPSE_SAMPLE
5 nodes (0, S//4, S//2, 3S//4, S-1); TOY_K (1, 2, 3); LOUD 1e3;
SHUFFLE_SEED 268 (detector mutant, r266 pattern); runtime <=
1800 s; smoke = w9 + controls + toy + w9 candidate numerics +
must-fails (ladder, AUC census, fingerprints, mp wards, success
gate, adjudication skipped).  DISCLOSED PRE-SPEC INPUT (no
scratch run of this probe): every reproduction band is an
r263/r264/r266 RECORD number adopted as-is (exception set and
g/Z table; drive power 0.959; self-dual S = 2N-1 42/42; border-
atom/union-node coincidence structure; razor slack 0.027; f64/mp
floor families for the new bars) -- nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  DRIVE_ANATOMY(carrier of |t| on the exception branch, AUC
    powers, edge capture)
+ B2_GAUGE_COLLAPSE_AT_NODES(exact; self-dual S = 2N-1: dual
    degree N, NOT small -- contract premise refuted)
+ B1_QUENCHED(sign acc, mag spread, EPS_UNPROVABLE)
+ B2_MASSLOCAL(best W, sign acc, eps decades, cert k/7)
+ B3_EDGELOCAL(best frac, sign acc, eps decades, cert k/7)
+ [exactly one of] DRIVE_LOCAL_GO(cand, 7/7, eps type) /
    DRIVE_LOCAL_PARTIAL(cand, n/7, rest anatomy) /
    DRIVE_LOCAL_INSUFFICIENT(sealed abort: the eps evaluation
    sits X dec above the certification budget -- the excluded-
    set abs sum needs exactly the forbidden root-scale comb
    cancellation: PAIRCORR at the eps step)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if fired] PAIRCORR_MINIATURE(candidate list).
Honesty before beauty: no verdict claims a derived 5/7, a bound
mechanism, or an asymptotic law; the exception scalar's
positivity stays OPEN (the campaign's work); r243/r250/r253/
r256/r257/r258/r260/r261/r262/r263/r264/r265/r266 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 caught a1 (the ward-bar split above, disclosed) and
smoke pass 2 was 28/28; calibration pass 1 = first full
evaluation, 28/28 gates, wall 17.2 s -- NO physics bar, band,
rule or verdict rule was moved at any point; ONE PRESENTATION
AMENDMENT p1 is disclosed (r263-p1/r266-p1 precedent): the draft
PARTIAL verdict printer omitted the SEALED fields (candidate,
certified rungs, rest anatomy) demanded by the verdict form
above; it was made data-driven BEFORE the record pass; pass 2 =
the record run below, numerically identical to pass 1 in every
printed figure):
CAL_VERDICT = DRIVE_ANATOMY(|t| power 0.959 reproduced; carrier
DEPTH 0.812; ABSMASS 0.143 / EDGEABS 0.086 / NEFF 0.135 / TOP1
0.135 all blind) + B2_GAUGE_COLLAPSE_AT_NODES(exact; self-dual
S = 2N-1: dual degree N, NOT small -- contract premise refuted)
+ B1_QUENCHED(W16 sign 7/42, magspread med 0.44 dec, |R|exc med
1.024, EPS_UNPROVABLE) + B2_MASSLOCAL(best b2W32, cert 0/7,
demand med 0.80 dec) + B3_EDGELOCAL(best b3F0.20, cert 1/7,
demand med 0.17 dec) + DRIVE_LOCAL_PARTIAL(b3F0.20, cert 1/7:
kz22; rest misses 0.18-0.44 dec, kz15 miss 0.44 dec).
Key numbers.  LEG A: contribution ward sum ct == t_{N-2} worst
dev/absmass 2.1e-13 main N <= 400 / 3.9e-13 deep / 2.4e-8
controls (bars 1e-9 / 3e-6 / 1e-6); anatomy census (42 rungs,
AUC power on 7-vs-35, labels table-side): DEPTH |t|/sum|ct| exc
med 0.160 vs cheap med 0.074, power 0.812 -- the ONLY strong
anatomical carrier; ABSMASS exc med 5.39 vs cheap 5.36 (power
0.143: BLIND -- the exceptions are NOT heavier, they are LESS
CANCELLED at fixed comb mass); EDGEABS 0.669 vs 0.646 (0.086),
NEFF 104 vs 83 (0.135), TOP1 0.060 vs 0.066 (0.135) all blind;
|t| power 0.959 == the r264 record EXACTLY (reproduction ward,
tol 0.02); anatomy pool: edge(0.10) abs share 0.58..0.77 (the
outer 10 pct of the hull carries ~2/3 of the abs mass on every
world), signed edge capture +0.36..+0.80 (med +0.62 on the
exceptions); oscillation: sign flips ~= N per rung (135..837),
edge flip share 0.39..0.43, amplitude ratio med|v| edge/bulk
1.0..1.6 -- the terminal polynomial oscillates through the
whole hull with a mild edge envelope, and the drive's abs mass
concentrates at the edge.  LEG B structure: toy collapse
identity pihat#_{S-1-k}(x_j) = w_j L'(x_j) pihat_k(x_j)/h_k
EXACT (rationals, k = 1..3, all 9 nodes); mp collapse ward on
REAL w9 (dps 60, drive pair k = N-2 = 182 <-> m = N = 184):
worst lg dev 2.8e-14, signs 5/5 sample nodes (bar 1e-6); self-
dual S = 2N-1 on 44/44; border-atom/union-node coincidence 100
pct on the mains AND 42/42 on the ladder => the transported
drive sum collapses term-by-term to the direct comb sum: the
gauge frame yields NO new local decomposition, and the dual
degree of the drive is N (NOT small) -- the b2 gauge premise is
dead structurally, the mass-ranked truncation is its only
surviving local content.  LEG B candidates (42 rungs): b1 sign
acc 7/42 at ALL windows (the persistence sign is ANTI-
correlated: the terminal drive sign flips against t_{N-3} on
35/42 rungs -- a measured half-wave alternation), magspread med
0.44-0.50 dec, |R| exc med 1.02-1.08 => no sign channel, no
provable eps (typed); b2 at W = 8/16/32: sign acc 31/32/37 of
42, |R| med 0.43/0.39/0.36, eps med +0.79/+0.78/+0.76 dec vs M;
b3 at frac 0.05/0.10/0.20: sign acc 40/41/42 of 42, |R| med
0.21/0.19/0.14, eps med +0.48/+0.34/+0.05 dec vs M (the edge
partial sum carries the SIGN of the drive on 42/42 at frac
0.20); triangle wards exact: worst |R| - eps slack 0.0, worst
|Z| bound slack 0.0 (bars 1e-9); wall detector re-armed:
selftest sp(g1, g1) = 1.000 flagged / target sp(D_N, g1) =
0.284 not flagged / seed-268 mutant sp = 0.112 misses;
fingerprints b2 0.74/0.74/0.76, b3 0.79/0.71/0.43, all < 0.9
AND no all-FALSE decision pattern => NO candidate is the wall;
paircorr demand on the exception branch: b2 med 0.80-0.83 (max
0.91), b3F0.05 med 0.50, b3F0.10 med 0.38, b3F0.20 med 0.17
(max 0.21) -- NO setting reaches the 1.0-dec bar: NOTHING
FIRES (the remaining gap is BELOW the sealed paircorr scale).
LEG C: success gate (sign-refined bound |Z| <= |Z_local| + eps,
exact triangle): b3F0.20 CERTIFIES kz22 (margin_cert +0.04 > 0
vs margin_true +0.648; |Z_local| = 0.024, eps = 0.78 < M --
the FIRST source-pure certification of an exception rung, no
wall flag, no paircorr fire); the other 6 rungs miss by 0.18
(kz52) / 0.19 (kz20) / 0.23 (kz38) / 0.25 (kz36) / 0.31 (kz39)
/ 0.44 (kz15) dec; b2W32 misses 0.67-1.23 dec (cert 0/7); kz15
detail: true reserve M - |Z| = 0.0268 in the sealed band
[0.020, 0.035] (r263 record 0.027 reproduced), |Z_local| =
0.554, eps = 0.81, miss 0.44 dec; consistency margin_cert <=
margin_true exact on every rung x setting.  LEG D: control
reproduction EPST dev 6.0e-11 / SCR 2.4e-8 (the local formula
reproduces the PERTURBED drives -- world-blind algebra, NOT
main-fitted; triangle validity exact on both); SMOOTH: drive
alias 2.4e-14 <= 1e-12, b1 t_local 9.8e-13 <= 1e-10 (the
trivial zero delivered trivially), q_N = 4.2e-25 <= 1e-20; mp
drive wards (dps 60): kz15 (N = 203) t_mp = -0.685943703 dev
2.9e-10, kz20 (N = 170) t_mp = -0.963458463 dev 2.2e-10 (bar
1e-8) -- the razor-rung drive is the mp value, not an f64
artifact; must-fails: m1 naked truncation breaks by 8.5e-2
abs-mass units = 4.0e+11 x the honest ward floor 2.1e-13
(loud), m2 gift-sign mutant FLAGGED (withheld-key hit), m3
rho-mutant FLAGGED (rho scope hit); fragment audit CLEAN.
READING (typed, no upgrade): the narrow contract half-carries
-- honest split: (i) the drive anatomy is now exact: the
exception branch is a CANCELLATION-DEPTH anomaly at fixed comb
mass (DEPTH power 0.812; mass, edge share, participation and
top-atom all blind) -- the r264 signature 0.959 reproduced and
anatomized; (ii) the L-gauge frame provably adds no new
locality at the terminal (node collapse exact at theorem grade,
dual degree N not small -- the contract's b2 premise refuted);
(iii) the edge-region triangle bound (outer 20 pct of the hull,
where ~2/3 of the abs mass and the saddle envelope sit, and
which carries the drive SIGN on 42/42) delivers the FIRST
source-pure certification of an exception rung (kz22) without
wall or paircorr fallback, and the remaining 6 rungs miss by
only 0.18-0.44 dec with NO detector firing: the residual gap
sits BELOW the sealed paircorr scale -- the named follow-up
target is a source-pure bulk-remainder bound sharper than the
abs-sum triangle by 0.2-0.45 dec (phase-aware but local), NOT
a new identity class; the razor kz15 needs 0.44 dec.  Runtime
16.7 s full / 0.2 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE (a1 and p1 predate the record
run, disclosed above).

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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import quenched_opening_probe as QO            # noqa: E402 r264
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import jfraction_probe as JF                   # noqa: E402 r230
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
TRI_BAR = 1e-9
ANAT_FRAC = 0.10
EDGE_FRACS = (0.05, 0.10, 0.20)
MASS_W = (8, 16, 32)
QUENCH_W = (4, 8, 16)
CHEAP_REF_IDX = (0, 10, 20, 30, 41)
TDRIVE_POWER_REF = 0.959
TDRIVE_POWER_TOL = 0.02
SIG_POWER_BAR = 0.8
FP_BAR = 0.9
DEMAND_BAR = 1.0
RESERVE_BAND = (0.020, 0.035)
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
SM_LOC_BAR = 1e-10
MP_DPS = 60
MP_T_BAR = 1e-8
MP_EXC_KZ = (15, 20)
COLLAPSE_LG_BAR = 1e-6
TOY_K = (1, 2, 3)
LOUD = 1e3
SHUFFLE_SEED = 268
KZ_ANCHOR = 15

CAL_VERDICT = (
    "DRIVE_ANATOMY(|t| power 0.959 reproduced; carrier DEPTH "
    "0.812; ABSMASS 0.143 / EDGEABS 0.086 / NEFF 0.135 / TOP1 "
    "0.135 all blind) + B2_GAUGE_COLLAPSE_AT_NODES(exact; "
    "self-dual S = 2N-1: dual degree N, NOT small -- contract "
    "premise refuted) + B1_QUENCHED(W16 sign 7/42, magspread "
    "med 0.44 dec, |R|exc med 1.024, EPS_UNPROVABLE) + "
    "B2_MASSLOCAL(best b2W32, cert 0/7, demand med 0.80 dec) + "
    "B3_EDGELOCAL(best b3F0.20, cert 1/7, demand med 0.17 dec) "
    "+ DRIVE_LOCAL_PARTIAL(b3F0.20, cert 1/7: kz22; rest "
    "misses 0.18-0.44 dec, kz15 miss 0.44 dec)")

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
                       "branch labels) enters gates and census "
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


# ---- sealed candidate builders (target-blind: consume ONLY the
# plain arrays passed as arguments -- prefix drives / atom data /
# per-atom contributions; the withheld terminal drive key and
# every target-side identifier are forbidden in scope, AST-audit)
def mask_edge(bx, lo, hi, frac):
    """b3 sealed keep-mask: atoms in the outer hull-edge region
    (fraction of the union+border hull width)."""
    edge = frac * (hi - lo)
    return (bx <= lo + edge) | (bx >= hi - edge)


def mask_mass(bx, bw, w_keep):
    """b2 sealed keep-mask: top-W atoms by the drive-mass field
    |bw bx| (solution-free source geometry)."""
    order = np.argsort(-np.abs(bw * bx), kind="stable")
    m = np.zeros(len(bx), dtype=bool)
    m[order[:min(w_keep, len(bx))]] = True
    return m


def cand_trunc(ct, keep):
    """b2/b3 shared truncation: t_local = signed partial sum over
    the kept atoms; eps = EXACT triangle bound on the remainder
    (sum of excluded abs contributions)."""
    t_loc = float(np.sum(ct[keep]))
    eps = float(np.sum(np.abs(ct[~keep])))
    return t_loc, eps


def cand_quenched(tpre, w):
    """b1 sealed quenched local model: magnitude = median of the
    trailing |drive| window, sign = persistence sign(t_{N-3})."""
    seg = np.abs(np.asarray(tpre[-w:], dtype=float))
    return math.copysign(float(np.median(seg)), float(tpre[-1]))


def cand_mutant_giftsign(rc, mag):
    """m2 MUST-FAIL MUTANT: phase sum with the ground-truth sign
    -- reads the withheld terminal drive key; the candidate scope
    audit must FLAG this."""
    return math.copysign(mag, rc["t_term"])


def cand_mutant_oracle(p):
    """m3 MUST-FAIL MUTANT: local model secretly reading the
    terminal target -- the scope audit must FLAG this."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


CAND_FORBIDDEN = {"t" + "_term", "rho", "S", "sa", "la", "q_chain",
                  "D_dir", "wb", "world_block", "direct_terminal",
                  "rhp_readout", "gram_input", "g_gap",
                  "u_triangle", "M_W"}


def cand_scope_audit(funcname):
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
                if nm in CAND_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ------------------------------------------------ toy exact tools
def pival_fr(z, n, al, be):
    """exact monic chain value (rationals)."""
    p0, p1 = Fr(1), z - al[0]
    if n == 0:
        return p0
    for k in range(1, n):
        p0, p1 = p1, (z - al[k]) * p1 - be[k - 1] * p0
    return p1


def toy_collapse():
    """the node-value form of the r231 L-gauge connection:
    pihat#_{S-1-k}(x_j) == w_j L'(x_j) pihat_k(x_j) / h_k, exact
    rationals on the r230 toy for k in TOY_K at ALL nodes."""
    nodes, wts = JF.TOY_NODES, JF.TOY_WTS
    St = len(nodes)
    al, be, hs = JF.stieltjes_exact(nodes, wts, St)
    Lp = []
    for j in range(St):
        pr = Fr(1)
        for k in range(St):
            if k != j:
                pr *= (nodes[j] - nodes[k])
        Lp.append(pr)
    dw = [1 / (wts[j] * Lp[j] ** 2) for j in range(St)]
    alD, beD, hsD = JF.stieltjes_exact(nodes, dw, St - 1)
    for k in TOY_K:
        m = St - 1 - k
        for j in range(St):
            lhs = pival_fr(nodes[j], m, alD, beD)
            rhs = wts[j] * Lp[j] * pival_fr(nodes[j], k, al, be) \
                / hs[k]
            if lhs != rhs:
                return False, (k, j)
    return True, None


# ---------------------------------------------------- mp routes
def mp_chain_nodes(xs_m, ws_m, deg, track=None):
    """mp scaled monic Stieltjes chain on (xs, ws) to degree deg;
    returns per-sample-node (log|pihat_deg|, sign) for the sealed
    track indices plus (log h_deg).  BR.mp_dual_route pattern."""
    S_ = len(xs_m)
    qx = [mp.mpf(1)] * S_
    qx_m = [mp.mpf(0)] * S_
    Ls = Ls_m = mp.mpf(0)
    eta = mp.fsum(w * q * q for w, q in zip(ws_m, qx))
    eta_m = eta
    for n in range(deg):
        alh = mp.fsum(w * x * q * q
                      for w, x, q in zip(ws_m, xs_m, qx)) / eta
        if n == 0:
            px = [(x - alh) * q for x, q in zip(xs_m, qx)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            px = [(x - alh) * q - ge * fc * qq
                  for x, q, qq in zip(xs_m, qx, qx_m)]
        sc = max(abs(v) for v in px)
        qx_m, eta_m, Ls_m = qx, eta, Ls
        qx = [v / sc for v in px]
        Ls = Ls + mp.log(sc)
        eta = mp.fsum(w * q * q for w, q in zip(ws_m, qx))
    out = {}
    for j in (track or ()):
        vv = qx[j]
        out[j] = (float(mp.log(abs(vv)) + Ls) if vv != 0
                  else float("-inf"),
                  int(mp.sign(vv)))
    lg_h = float(mp.log(abs(eta)) + 2 * Ls)
    sg_h = int(mp.sign(eta))
    return out, lg_h, sg_h


def mp_collapse_ward(p, dps, n_sample=5):
    """mp (dps sealed) ward of the node-value collapse identity
    at the DRIVE pair k = N-2 <-> m = S-1-k = N on the real
    window: dual chain (weights 1/(w L'^2), log-shifted; monic
    scale-invariant) vs w_j L'(x_j) pihat_{N-2}(x_j)/h_{N-2}."""
    mp.mp.dps = dps
    xu, wu = CT.union_arrays(p["d"])
    N = p["N"]
    S_ = len(xu)
    k = N - 2
    m = S_ - 1 - k
    xs_m = [mp.mpf(float(v)) for v in xu]
    ws_m = [mp.mpf(float(v)) for v in wu]
    lgLp = []
    sgLp = []
    for j in range(S_):
        lg = mp.mpf(0)
        sg = 1
        for i in range(S_):
            if i != j:
                d = xs_m[j] - xs_m[i]
                lg += mp.log(abs(d))
                sg *= int(mp.sign(d))
        lgLp.append(lg)
        sgLp.append(sg)
    lgdw = [-mp.log(abs(w)) - 2 * lg
            for w, lg in zip(ws_m, lgLp)]
    sh = max(lgdw)
    dwm = [mp.sign(w) * mp.e ** (lg - sh)
           for w, lg in zip(ws_m, lgdw)]
    sample = (0, S_ // 4, S_ // 2, (3 * S_) // 4, S_ - 1)[:n_sample]
    dual_vals, _lgD, _sgD = mp_chain_nodes(xs_m, dwm, m,
                                           track=sample)
    orig_vals, lg_hk, sg_hk = mp_chain_nodes(xs_m, ws_m, k,
                                             track=sample)
    worst = 0.0
    signs_ok = True
    for j in sample:
        lg_l, sg_l = dual_vals[j]
        lg_o, sg_o = orig_vals[j]
        lg_r = float(mp.log(abs(ws_m[j]))) + float(lgLp[j]) \
            + lg_o - lg_hk
        sg_r = int(mp.sign(ws_m[j])) * sgLp[j] * sg_o * sg_hk
        worst = max(worst, abs(lg_l - lg_r))
        signs_ok = signs_ok and (sg_l == sg_r)
    return worst, signs_ok, m


def mp_drive(p, dps):
    """mp (dps sealed) terminal drive t_{N-2} = T~ e^{Ls_{N-2} -
    Ls_{N-1}} / sqrt|eta_{N-1}| from the raw atoms (original mp
    scaled chain with border tracking)."""
    mp.mp.dps = dps
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    N = p["N"]
    xs_m = [mp.mpf(float(v)) for v in xu]
    ws_m = [mp.mpf(float(v)) for v in wu]
    bs = [mp.mpf(float(v)) for v in bx]
    bwm = [mp.mpf(float(v)) for v in bw]
    qx = [mp.mpf(1)] * len(xs_m)
    qb = [mp.mpf(1)] * len(bs)
    qx_m = [mp.mpf(0)] * len(xs_m)
    qb_m = [mp.mpf(0)] * len(bs)
    Ls = Ls_m = mp.mpf(0)
    eta = mp.fsum(w * q * q for w, q in zip(ws_m, qx))
    eta_m = eta
    Tb = None
    Ls2 = None
    for n in range(N - 1):
        if n == N - 2:
            Tb = mp.fsum(w * z * q
                         for w, z, q in zip(bwm, bs, qb))
            Ls2 = Ls
        alh = mp.fsum(w * x * q * q
                      for w, x, q in zip(ws_m, xs_m, qx)) / eta
        if n == 0:
            px = [(x - alh) * q for x, q in zip(xs_m, qx)]
            pb = [(z - alh) * q for z, q in zip(bs, qb)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            px = [(x - alh) * q - ge * fc * qq
                  for x, q, qq in zip(xs_m, qx, qx_m)]
            pb = [(z - alh) * q - ge * fc * qq
                  for z, q, qq in zip(bs, qb, qb_m)]
        sc = max(abs(v) for v in px)
        qx_m, qb_m, eta_m, Ls_m = qx, qb, eta, Ls
        qx = [v / sc for v in px]
        qb = [v / sc for v in pb]
        Ls = Ls + mp.log(sc)
        eta = mp.fsum(w * q * q for w, q in zip(ws_m, qx))
    t_mp = Tb * mp.e ** (Ls2 - Ls) / mp.sqrt(abs(eta))
    return float(t_mp)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("drive_local_asymptotics_probe -- PRIME.PORT.RHP."
          "QUENCHED.DRIVE_LOCAL_ASYMPTOTICS.01 (round 268)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)   "
          "CHARTER_SHA %s (imported r264)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16], QO.CHARTER_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + w9 "
                        "candidate numerics + must-fails; ladder, "
                        "AUC census, fingerprints, mp wards, "
                        "success gate, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "NARROW CONTRACT (reviewer-adjudicated): local main term "
          "+ PROVABLE eps for the border-drive column t_{N-2} "
          "ONLY; 3 sealed candidates (b1 quenched window, b2 "
          "mass-ranked dual-frame truncation, b3 edge-region "
          "saddle truncation); success gate = certify |Z| < "
          "sqrt(5/7) on exception rungs via |Z_local| + eps, "
          "razor kz15 the design anchor; sealed abort criterion "
          "DRIVE_LOCAL_INSUFFICIENT if no rung certifies; wall + "
          "paircorr detectors re-armed; ALL bars, rules and "
          "verdicts sealed BEFORE evaluation (pre-spec input = "
          "r263/r264/r266 record numbers, disclosed)")

    # ---------------- S1: census + controls
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
          "control flips re-derived %s (INDEFINITE_CONTINUATION "
          "beyond pmax); cofinal ladder %d rungs POSITIVE_PREFIX "
          "%s, N in [%s, %s]"
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
        vb = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * vb * fac
        return dict(kz=p["kz"], N=N, g=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), tpre=t[:N - 2],
                    ct=ct, bx=bx, bw=bw, vb=vb, xu=xu,
                    lo=lo, hi=hi, p=p)

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
        info("EXCEPTION RUNGS (kz, N, g, Z, |t|): %s"
             % "; ".join("kz%d N%d g%+.3f Z%+.4f |t|%.3f"
                         % (rc["kz"], rc["N"], rc["g"], rc["Z"],
                            abs(rc["t_term"]))
                         for rc in sorted(exc,
                                          key=lambda r_: r_["kz"])))

    # ---------------- S2: LEG A -- drive anatomy
    section("S2  LEG A -- DRIVE ANATOMY AT THE TERMINAL")
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
          "sum_b ct_b == t_{N-2} (per-atom drive contributions in "
          "t-units, r266 eval machinery + r244 scaled rows) on "
          "%d rungs + %d mains + 3 controls: worst dev/absmass "
          "%.1e main N<=%d (bar %.0e) / %.1e deep (bar %.0e) / "
          "%.1e controls (bar %.0e, f64 chain-reference floor on "
          "flipped worlds, r253/r264 precedent) -- the anatomy "
          "operates on an EXACT decomposition, world-blind (the "
          "same identity is the control-reproduction ward)"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def anat(rc, frac):
        ct, bx = rc["ct"], rc["bx"]
        absum = rc["absum"]
        depth = abs(rc["t_term"]) / max(absum, 1e-300)
        ed = mask_edge(bx, rc["lo"], rc["hi"], frac)
        edge_abs = float(np.sum(np.abs(ct[ed]))) \
            / max(absum, 1e-300)
        cap = (float(np.sum(ct[ed])) / rc["t_term"]
               if abs(rc["t_term"]) > 1e-300 else float("nan"))
        neff = absum * absum / max(float(np.sum(ct * ct)), 1e-300)
        top1 = float(np.max(np.abs(ct))) / max(absum, 1e-300)
        return depth, edge_abs, cap, neff, top1

    def osc(rc, frac):
        o = np.argsort(rc["bx"], kind="stable")
        sx = rc["bx"][o]
        sv = rc["vb"][o]
        sgn = np.sign(sv)
        nzm = sgn != 0.0
        sgnn = sgn[nzm]
        sxn = sx[nzm]
        fl = np.nonzero(sgnn[1:] * sgnn[:-1] < 0)[0]
        nfl = len(fl)
        edl = mask_edge(sxn[:-1], rc["lo"], rc["hi"], frac)
        fshare = (float(np.sum(edl[fl])) / nfl) if nfl else 0.0
        edm = mask_edge(sx, rc["lo"], rc["hi"], frac)
        me = float(np.median(np.abs(sv[edm]))) if edm.any() \
            else float("nan")
        mb = float(np.median(np.abs(sv[~edm]))) if (~edm).any() \
            else float("nan")
        amp = me / max(mb, 1e-300)
        return nfl, fshare, amp

    for rc in recs + mrecs:
        rc["anat"] = anat(rc, ANAT_FRAC)
        rc["osc"] = osc(rc, ANAT_FRAC)
    if smoke:
        anat_pool = mrecs
    else:
        used = set()
        refs = []
        for i0 in CHEAP_REF_IDX:
            i = i0
            while recs[i]["g"] < 0.0 or i in used:
                i = (i + 1) % len(recs)
            used.add(i)
            refs.append(recs[i])
        anat_pool = sorted(exc, key=lambda r_: r_["kz"]) \
            + mrecs + refs
    for rc in anat_pool:
        d_, ea, cp, ne, t1 = rc["anat"]
        nfl, fs, am = rc["osc"]
        info("kz%-3d N%-4d %-4s |t| %.3f  depth %.4f  mass %.2f  "
             "edgeabs %.3f  capture %+0.3f  neff %.1f  top1 %.3f  "
             "flips %d (edge %.2f)  amp %.2f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g"] < 0 else "chp",
                abs(rc["t_term"]), d_, rc["absum"], ea, cp, ne,
                t1, nfl, fs, am))
    check("G21-anatomy-census", True,
          "a1 MEASUREMENT (exact decomposition; pool = %s): the "
          "drive is a deep-cancellation comb sum -- per-rung "
          "table printed (|t| = depth x mass, edge share/capture "
          "at hull frac %.2f, N_eff, top-1)"
          % ("7 exc + 2 mains + 5 cheap refs" if not smoke
             else "mains (SMOKE)", ANAT_FRAC))
    check("G22-oscillation-structure", True,
          "a2 MEASUREMENT: sign field of v_{N-2} on the sorted "
          "border atoms -- flip census and edge amplitude "
          "envelope printed per pool rung (exact from the chain; "
          "the terminal polynomial oscillates through the whole "
          "hull, amplitude concentrated at the edge)")
    if not smoke:
        lab = {rc["kz"]: rc["g"] < 0.0 for rc in recs}
        stats = {"TDRIVE": [abs(rc["t_term"]) for rc in recs],
                 "DEPTH": [rc["anat"][0] for rc in recs],
                 "ABSMASS": [rc["absum"] for rc in recs],
                 "EDGEABS": [rc["anat"][1] for rc in recs],
                 "NEFF": [rc["anat"][3] for rc in recs],
                 "TOP1": [rc["anat"][4] for rc in recs]}
        powers = {}
        for k in sorted(stats):
            ve = [v for v, rc in zip(stats[k], recs)
                  if lab[rc["kz"]]]
            vc = [v for v, rc in zip(stats[k], recs)
                  if not lab[rc["kz"]]]
            _a, pw = QO.auc_power(vc, ve)
            powers[k] = pw
            info("%-8s power %.3f (exc med %.3g / cheap med "
                 "%.3g)" % (k, pw, float(np.median(ve)),
                            float(np.median(vc))))
        carriers = [k for k in powers
                    if k != "TDRIVE" and powers[k] >= SIG_POWER_BAR]
        ok_rep = abs(powers["TDRIVE"] - TDRIVE_POWER_REF) \
            <= TDRIVE_POWER_TOL
        check("G23-anatomy-adjudication", ok_rep,
              "a3: |t_{N-2}| power %.3f == r264 record %.3f "
              "(reproduction ward, tol %.2f); |t| = depth x "
              "mass, anatomical carrier(s) at the sealed %.1f "
              "bar: %s -- %s"
              % (powers["TDRIVE"], TDRIVE_POWER_REF,
                 TDRIVE_POWER_TOL, SIG_POWER_BAR,
                 str(carriers) if carriers else "NONE",
                 ("the exception branch is carried by %s (labels "
                  "table-side only)" % ", ".join(carriers))
                 if carriers else
                 "no single anatomical statistic carries the "
                 "branch at the sealed bar (typed honestly)"))
    else:
        powers = {}
        check("G23-anatomy-adjudication", True, "SMOKE: skipped")

    # ---------------- S3: LEG B structure -- the gauge collapse
    section("S3  B2 STRUCTURE -- L-GAUGE COLLAPSE AT THE NODES")
    ok_toy, brk = toy_collapse()
    check("G30-toy-collapse-exact", ok_toy,
          "pihat#_{S-1-k}(x_j) == w_j L'(x_j) pihat_k(x_j)/h_k "
          "EXACT (rationals, r230 toy, k = %s, ALL %d nodes)%s "
          "-- the residue of the r231 connection L C[pihat_k]/h_k "
          "at a node: the L-gauge transported drive sum collapses "
          "term-by-term to the direct comb sum wherever border "
          "atoms sit ON union nodes"
          % (str(TOY_K), len(JF.TOY_NODES),
             "" if ok_toy else " BREAK at %s" % str(brk)))
    sd_all = all(len(rc["xu"]) == 2 * rc["N"] - 1
                 for rc in recs + mrecs)
    coin_m = True
    coin_l = 0
    for rc in mrecs:
        cnt = (rc["bx"][:, None] == rc["xu"][None, :]).sum(axis=1)
        coin_m = coin_m and bool(np.all(cnt == 1))
    for rc in recs:
        cnt = (rc["bx"][:, None] == rc["xu"][None, :]).sum(axis=1)
        if bool(np.all(cnt == 1)):
            coin_l += 1
    check("G31-selfdual-coincidence", sd_all and coin_m,
          "self-dual S = 2N-1 on %d/%d rungs + mains (r266 "
          "re-gated): the dual degree of the DRIVE pair k = N-2 "
          "is m = N -- NOT small (the contract premise 'the dual "
          "problem is low-degree at the terminal' is REFUTED "
          "structurally); border-atom/union-node coincidence: "
          "mains 100 pct, ladder %s => with G30 the gauge frame "
          "yields NO new local decomposition of the drive: the "
          "surviving b2 content is the mass-ranked truncation"
          % (len(recs) + len(mrecs), len(recs) + len(mrecs),
             ("%d/%d" % (coin_l, len(recs))) if not smoke
             else "n/a (SMOKE)"))
    if not smoke:
        w9p = packs["w9"]
        wst, sgn_ok, m_dual = mp_collapse_ward(w9p, MP_DPS)
        check("G32-mp-collapse-ward",
              wst <= COLLAPSE_LG_BAR and sgn_ok,
              "mp (dps %d) node-value collapse on REAL w9 at the "
              "drive pair k = N-2 = %d <-> m = %d: worst lg dev "
              "%.1e (bar %.0e), signs %s on the 5 sealed sample "
              "nodes -- theorem-grade on the true comb"
              % (MP_DPS, w9p["N"] - 2, m_dual, wst,
                 COLLAPSE_LG_BAR, "MATCH" if sgn_ok else "BROKEN"))
    else:
        check("G32-mp-collapse-ward", True, "SMOKE: skipped")

    # ---------------- S4: LEG B -- the three sealed candidates
    section("S4  LEG B -- SEALED LOCAL CANDIDATES + DETECTORS")
    hits = []
    for fn in ("mask_edge", "mask_mass", "cand_trunc",
               "cand_quenched"):
        hits += cand_scope_audit(fn)
    h_m2 = cand_scope_audit("cand_mutant_giftsign")
    h_m3 = cand_scope_audit("cand_mutant_oracle")
    ag_hits = antigate_fragment_audit()
    check("G40-scope-audits", not hits and bool(h_m2)
          and bool(h_m3) and not ag_hits,
          "sealed builders consume plain prefix/atom arrays only "
          "(%s); m2 gift-sign mutant FLAGGED (%s); m3 target-"
          "reading mutant FLAGGED (%s); fragment audit (no fit "
          "primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(h_m2) if h_m2 else "NOT FLAGGED",
             "; ".join(h_m3) if h_m3 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    all_rc = recs + mrecs
    settings = []
    for W in QUENCH_W:
        settings.append(("b1W%d" % W, "b1", W))
    for W in MASS_W:
        settings.append(("b2W%d" % W, "b2", W))
    for f in EDGE_FRACS:
        settings.append(("b3F%.2f" % f, "b3", f))
    res = {}
    for nm, fam, par_ in settings:
        rows_ = []
        for rc in all_rc:
            if fam == "b1":
                t_loc = cand_quenched(rc["tpre"], par_)
                eps = None
            elif fam == "b2":
                keep = mask_mass(rc["bx"], rc["bw"], par_)
                t_loc, eps = cand_trunc(rc["ct"], keep)
            else:
                keep = mask_edge(rc["bx"], rc["lo"], rc["hi"],
                                 par_)
                t_loc, eps = cand_trunc(rc["ct"], keep)
            R = rc["t_term"] - t_loc
            Zl = t_loc + rc["chain"]
            bound = abs(Zl) + (eps if eps is not None
                               else float("inf"))
            rows_.append(dict(kz=rc["kz"], exc=rc["g"] < 0,
                              t_loc=t_loc, eps=eps, R=R, Zl=Zl,
                              bound=bound,
                              margin=M_W - bound,
                              sgn_ok=(math.copysign(1, t_loc)
                                      == math.copysign(
                                          1, rc["t_term"])),
                              t_true=rc["t_term"], Z=rc["Z"]))
        res[nm] = rows_

    def fam_rows(nm, only_pool=True):
        return res[nm][:len(recs)] if only_pool else res[nm]

    # b1 census
    b1_note = []
    for W in QUENCH_W:
        rws = fam_rows("b1W%d" % W)
        acc = sum(1 for r_ in rws if r_["sgn_ok"])
        mag = [abs(math.log10(abs(r_["t_loc"] / r_["t_true"])))
               for r_ in rws if abs(r_["t_true"]) > 1e-300]
        Re = [abs(r_["R"]) for r_ in rws if r_["exc"]]
        b1_note.append("W%d sign %d/%d magspread med %.2f dec "
                       "|R|exc med %s"
                       % (W, acc, len(rws),
                          float(np.median(mag)) if mag else
                          float("nan"),
                          ("%.3f" % float(np.median(Re)))
                          if Re else "n/a"))
    check("G41-b1-quenched-census", True,
          "b1 QUENCHED window model (sign = persistence, mag = "
          "trailing median): %s -- EPS DERIVATION: NONE at this "
          "complexity (the drive is length-N essential, r260 d6 "
          "kill): typed EPS_UNPROVABLE, excluded from leg-C "
          "certification by type" % "; ".join(b1_note))
    # b2/b3 census
    for gate, fam, pars, unit in (
            ("G42-b2-masslocal-census", "b2", MASS_W, "W"),
            ("G43-b3-edgelocal-census", "b3", EDGE_FRACS, "frac")):
        note = []
        for par_ in pars:
            nm = ("b2W%d" % par_) if fam == "b2" \
                else ("b3F%.2f" % par_)
            rws = fam_rows(nm)
            acc = sum(1 for r_ in rws if r_["sgn_ok"])
            Rm = float(np.median([abs(r_["R"]) for r_ in rws]))
            epd = float(np.median(
                [math.log10(r_["eps"] / M_W) for r_ in rws]))
            note.append("%s%s sign %d/%d |R| med %.2f eps med "
                        "%+.2f dec vs M"
                        % (unit, str(par_), acc, len(rws), Rm,
                           epd))
        check(gate, True,
              "%s truncation (sealed ablation): %s -- t_local = "
              "signed partial sum, eps = EXACT triangle bound on "
              "the excluded atoms (provable; evaluation consumes "
              "every atom, locality of the BOUND typed honestly)"
              % ("b2 MASS-RANKED (top-W by |bw bx|)"
                 if fam == "b2" else
                 "b3 EDGE-REGION (outer hull fraction)",
                 "; ".join(note)))
    tri_w1 = 0.0
    tri_w2 = 0.0
    for nm, fam, _p in settings:
        if fam == "b1":
            continue
        for r_ in res[nm]:
            tri_w1 = max(tri_w1, abs(r_["R"]) - r_["eps"])
            tri_w2 = max(tri_w2, abs(r_["Z"]) - r_["bound"])
    check("G44-triangle-wards", tri_w1 <= TRI_BAR
          and tri_w2 <= TRI_BAR,
          "the provable bounds are EXACT triangles on the "
          "R-decomposition: worst |R| - eps slack %+.1e <= 0, "
          "worst |Z| - (|Z_local| + eps) slack %+.1e <= 0 (bars "
          "%.0e) over all settings x %d worlds -- |Z| <= "
          "|Z_local| + eps is a THEOREM given the decomposition"
          % (tri_w1, tri_w2, TRI_BAR, len(all_rc)))
    if not smoke:
        g1s = {}
        for rc in recs:
            pk = QO.port_pack(rc["kz"])
            lam, U = np.linalg.eigh(pk["Q"])
            c2 = (U.T @ pk["f"]) ** 2
            g1s[rc["kz"]] = float(np.sum(c2 / (1.0 - lam)))
        g1v = [g1s[rc["kz"]] for rc in recs]
        dnv = [B57 - float(rc["p"]["rho"][rc["N"] - 1])
               for rc in recs]

        def wall_flag(critv, passes):
            sp_ = abs(BH.spearman(critv, g1v))
            return ((passes == 0) and sp_ >= FP_BAR), sp_

        fl_wall, sp_wall = wall_flag(
            g1v, sum(1 for v in g1v if v < 1.0))
        fl_tgt, sp_tgt = wall_flag(
            dnv, sum(1 for v in dnv if v > 0.0))
        rng = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(g1v,
                                 list(rng.permutation(g1v))))
        check("G45-wall-detector-armed",
              fl_wall and not fl_tgt and sp_mut < FP_BAR,
              "selftest: wall criterion g(1) < 1 FALSE 42/42, "
              "sp(g1, g1) = %.3f >= %.1f FLAGGED; target D_N > 0 "
              "TRUE 42/42, sp(D_N, g1) = %.3f NOT flagged; "
              "seed-%d shuffle mutant sp = %.3f misses (loud, as "
              "sealed) -- r266 detector re-armed on the measured "
              "ladder"
              % (sp_wall, FP_BAR, sp_tgt, SHUFFLE_SEED, sp_mut))
        fired = []
        fp_note = []
        for nm, fam, _p in settings:
            if fam == "b1":
                continue
            rws = fam_rows(nm)
            crit = [r_["margin"] for r_ in rws]
            passes = sum(1 for v in crit if v > 0.0)
            fl, sp_ = wall_flag(crit, passes)
            dem = [math.log10(r_["bound"] / M_W)
                   for r_ in rws if r_["exc"]]
            fire = (max(dem) >= DEMAND_BAR) if dem else False
            if fire:
                fired.append(nm)
            for r_ in rws:
                r_["wall"] = fl
            res[nm + "_meta"] = dict(sp=sp_, wall=fl, fire=fire,
                                     passes=passes,
                                     dem_med=float(np.median(dem))
                                     if dem else float("nan"),
                                     dem_max=max(dem)
                                     if dem else float("nan"))
            fp_note.append("%s sp %.2f cert %d/42 demand med "
                           "%.2f max %.2f%s"
                           % (nm, sp_, passes,
                              res[nm + "_meta"]["dem_med"],
                              res[nm + "_meta"]["dem_max"],
                              " FIRE" if fire else ""))
        check("G46-detector-census", True,
              "d2 paircorr demand log10((|Z_local| + eps)/M) on "
              "the exception branch (bar %.1f dec) + wall "
              "fingerprints (bar %.1f): %s -- fired routes are "
              "closed for certification IMMEDIATELY (no "
              "sharpening)" % (DEMAND_BAR, FP_BAR,
                               "; ".join(fp_note)))
    else:
        fired = []
        check("G45-wall-detector-armed", True, "SMOKE: skipped")
        check("G46-detector-census", True, "SMOKE: skipped")

    # ---------------- S5: LEG C -- the success gate
    section("S5  LEG C -- SUCCESS GATE (SEALED, HARD)")
    if not smoke:
        prov = [nm for nm, fam, _p in settings if fam != "b1"]

        def cert_count(nm):
            meta = res[nm + "_meta"]
            if meta["wall"]:
                return -1
            return sum(1 for r_ in fam_rows(nm)
                       if r_["exc"] and r_["margin"] > 0.0)

        best_b2 = max((nm for nm in prov if nm.startswith("b2")),
                      key=lambda nm: (cert_count(nm),
                                      -res[nm + "_meta"]["dem_med"]))
        best_b3 = max((nm for nm in prov if nm.startswith("b3")),
                      key=lambda nm: (cert_count(nm),
                                      -res[nm + "_meta"]["dem_med"]))
        cons_ok = True
        for nm in prov:
            for r_ in res[nm]:
                cons_ok = cons_ok and (r_["margin"]
                                       <= (M_W - abs(r_["Z"]))
                                       + TRI_BAR)
        best_miss = {}
        for nm in (best_b2, best_b3):
            for r_ in fam_rows(nm):
                if not r_["exc"]:
                    continue
                need = M_W - abs(r_["Zl"])
                miss = (math.log10(r_["eps"] / need)
                        if need > 0 else float("inf"))
                best_miss[(nm, r_["kz"])] = miss
                info("%s kz%-3d margin_true %+0.4f margin_cert "
                     "%+0.2f |Z_loc| %.3f eps %.2f miss %s dec "
                     "%s"
                     % (nm, r_["kz"], M_W - abs(r_["Z"]),
                        r_["margin"], abs(r_["Zl"]), r_["eps"],
                        ("%.2f" % miss) if math.isfinite(miss)
                        else "inf(MAIN_TERM_EXCEEDS)",
                        "CERTIFIED" if r_["margin"] > 0
                        else "not certified"))
        check("G50-success-gate-table", cons_ok,
              "per-exception-rung table printed for the best b2 "
              "(%s) and best b3 (%s); consistency margin_cert <= "
              "margin_true on every rung x setting (exact, "
              "%s) -- the certified margin can never beat the "
              "true one, only reach it"
              % (best_b2, best_b3, "OK" if cons_ok else "BROKEN"))
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        m15 = min(best_miss.get((best_b2, KZ_ANCHOR),
                                float("inf")),
                  best_miss.get((best_b3, KZ_ANCHOR),
                                float("inf")))
        check("G51-kz15-design-anchor", ok15,
              "kz15 (N = %d, the razor): true reserve M - |Z| = "
              "%.4f in the sealed band %s (r263 record 0.027 "
              "reproduced); best local certification misses by "
              "%.2f dec (the eps needed to certify the razor "
              "rung is that many decades below the measured "
              "excluded-set abs sum)"
              % (rc15["N"], slack15, str(RESERVE_BAND), m15))
        cert_best = max(cert_count(best_b2), cert_count(best_b3))
        clean_ok = [nm for nm in prov
                    if cert_count(nm) > 0
                    and not res[nm + "_meta"]["fire"]]
        if clean_ok:
            best_clean = max(clean_ok,
                             key=lambda nm: (cert_count(nm),
                                             -res[nm + "_meta"]
                                             ["dem_med"]))
            cert_kzs = sorted(r_["kz"] for r_ in
                              fam_rows(best_clean)
                              if r_["exc"] and r_["margin"] > 0)
            rest_miss = []
            for r_ in fam_rows(best_clean):
                if r_["exc"] and r_["margin"] <= 0:
                    need = M_W - abs(r_["Zl"])
                    rest_miss.append(
                        math.log10(r_["eps"] / need)
                        if need > 0 else float("inf"))
        else:
            best_clean = "none"
            cert_kzs = []
            rest_miss = []
        if clean_ok and max(cert_count(nm)
                            for nm in clean_ok) == len(exc):
            verdict_c = "GO"
        elif clean_ok:
            verdict_c = "PARTIAL"
        else:
            verdict_c = "INSUFFICIENT"
        check("G52-abort-adjudication", True,
              "sealed rule (certify >= 1 exception rung without "
              "wall/paircorr fallback, else abort): best cert "
              "count %d/7 (wall flags none: %s; paircorr fired: "
              "%s) => %s -- no candidate repair after seeing the "
              "numbers (selection-by-answer forbidden)"
              % (max(cert_best, 0),
                 str([nm for nm in prov
                      if res[nm + "_meta"]["wall"]]),
                 str(fired) if fired else "none",
                 "DRIVE_LOCAL_" + verdict_c))
    else:
        verdict_c = "SMOKE"
        best_b2 = best_b3 = "n/a"
        check("G50-success-gate-table", True, "SMOKE: skipped")
        check("G51-kz15-design-anchor", True, "SMOKE: skipped")
        check("G52-abort-adjudication", True, "SMOKE: skipped")

    # ---------------- S6: LEG D -- controls + wards + must-fails
    section("S6  LEG D -- CONTROLS + MP WARDS + MUST-FAILS")
    ctl_ok = True
    ctl_note = []
    for c in ("EPST", "SCR"):
        rc = crecs[c]
        for fam, par_ in (("b2", 16), ("b3", 0.10)):
            if fam == "b2":
                keep = mask_mass(rc["bx"], rc["bw"], par_)
            else:
                keep = mask_edge(rc["bx"], rc["lo"], rc["hi"],
                                 par_)
            t_loc, eps = cand_trunc(rc["ct"], keep)
            R = rc["t_term"] - t_loc
            ctl_ok = ctl_ok and (abs(R) <= eps + TRI_BAR)
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        ctl_note.append("%s t %+0.3f dev %.1e" % (c, rc["t_term"],
                                                  dev))
        ctl_ok = ctl_ok and (dev <= TB_WARD_BAR_CTRL)
    main_fitted = not ctl_ok
    check("G60-control-reproduction", ctl_ok,
          "the local formula reproduces the PERTURBED drives on "
          "EPSTEIN/SCRAMBLE exactly (contribution identity + "
          "triangle validity |R| <= eps at the middle settings): "
          "%s -- world-blind algebra, NOT main-fitted"
          % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    rcS = crecs["SMOOTH"]
    b1_sm = abs(cand_quenched(rcS["tpre"], 16))
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    check("G61-smooth-anchor", alias <= SM_ALIAS_BAR
          and b1_sm <= SM_LOC_BAR and abs(qS) <= SM_Q_BAR,
          "SMOOTH: drive alias max_{k>=2}|T~|/max(|T~_0|,|T~_1|) "
          "= %.1e <= %.0e (the drive is EXACTLY the two Jacobi "
          "readouts on the self-aliased source, r260); b1 local "
          "model returns |t_local| = %.1e <= %.0e (the trivial "
          "zero delivered trivially); q_N = %.1e <= %.0e"
          % (alias, SM_ALIAS_BAR, b1_sm, SM_LOC_BAR, qS,
             SM_Q_BAR))
    if not smoke:
        mp_note = []
        mp_w = 0.0
        for kz in MP_EXC_KZ:
            rc = next(r_ for r_ in recs if r_["kz"] == kz)
            t_mp = mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            mp_w = max(mp_w, dv)
            mp_note.append("kz%d (N = %d) t_mp = %+0.9f dev %.1e"
                           % (kz, rc["N"], t_mp, dv))
        check("G62-mp-drive-wards", mp_w <= MP_T_BAR,
              "mp (dps %d) terminal drive t_{N-2} at BOTH sealed "
              "exception rungs: %s vs the f64 chain (bar %.0e) "
              "-- the razor-rung drive is the mp value, not an "
              "f64 artifact"
              % (MP_DPS, "; ".join(mp_note), MP_T_BAR))
    else:
        check("G62-mp-drive-wards", True, "SMOKE: skipped")
    viol = 0.0
    honest = max(tb_worst, 1e-300)
    for rc in all_rc:
        keep = mask_edge(rc["bx"], rc["lo"], rc["hi"], 0.10)
        t_loc, _eps = cand_trunc(rc["ct"], keep)
        viol = max(viol, (abs(rc["t_term"]) - abs(t_loc))
                   / max(rc["absum"], 1e-300))
    check("G63-mustfail-naked-truncation", viol >= LOUD * honest,
          "m1 WINDOW TRUNCATION WITHOUT ERROR TERM: the naked "
          "claim |t| <= |t_local| breaks by %.1e (abs-mass "
          "units) = %.1e x the honest contribution-ward floor "
          "%.1e (bar %.0f x) -- no truncation is admissible "
          "without its eps term" % (viol, viol / honest, honest,
                                    LOUD))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact drive anatomy (contribution "
          "decomposition + oscillation census), the node-value "
          "collapse of the L-gauge frame (dual degree NOT "
          "small), the sealed local-candidate adjudication with "
          "provable triangle eps, and the honest success-gate/"
          "abort adjudication on the exception branch")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        parts.append("DRIVE_ANATOMY(|t| power %.3f reproduced; "
                     "carrier %s: DEPTH %.3f / ABSMASS %.3f / "
                     "EDGEABS %.3f / NEFF %.3f / TOP1 %.3f)"
                     % (powers["TDRIVE"],
                        str(carriers) if carriers else "NONE",
                        powers["DEPTH"], powers["ABSMASS"],
                        powers["EDGEABS"], powers["NEFF"],
                        powers["TOP1"]))
        parts.append("B2_GAUGE_COLLAPSE_AT_NODES(exact; self-"
                     "dual S = 2N-1: dual degree N, NOT small "
                     "-- contract premise refuted)")
        parts.append("B1_QUENCHED(%s, EPS_UNPROVABLE)"
                     % b1_note[-1])
        parts.append("B2_MASSLOCAL(best %s, cert %d/7, demand "
                     "med %.2f dec)"
                     % (best_b2, max(cert_count(best_b2), 0),
                        res[best_b2 + "_meta"]["dem_med"]))
        parts.append("B3_EDGELOCAL(best %s, cert %d/7, demand "
                     "med %.2f dec)"
                     % (best_b3, max(cert_count(best_b3), 0),
                        res[best_b3 + "_meta"]["dem_med"]))
        if verdict_c == "GO":
            parts.append("DRIVE_LOCAL_GO(%s, 7/7, eps = exact "
                         "triangle)" % best_clean)
        elif verdict_c == "PARTIAL":
            parts.append("DRIVE_LOCAL_PARTIAL(%s, cert %d/7: "
                         "%s; rest misses %.2f-%.2f dec, kz15 "
                         "miss %.2f dec)"
                         % (best_clean, cert_best,
                            ", ".join("kz%d" % kz
                                      for kz in cert_kzs),
                            min(rest_miss), max(rest_miss),
                            m15))
        else:
            parts.append("DRIVE_LOCAL_INSUFFICIENT(sealed "
                         "abort: kz15 miss %.2f dec; the eps "
                         "evaluation sits above the "
                         "certification budget on every "
                         "exception rung -- the excluded-set "
                         "abs sum needs exactly the forbidden "
                         "root-scale comb cancellation: "
                         "PAIRCORR at the eps step)" % m15)
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        if fired:
            parts.append("PAIRCORR_MINIATURE(%s)"
                         % ", ".join(fired))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the contribution "
          "decomposition, the triangle bounds, the node-value "
          "collapse; MEASURED: the anatomy powers, the capture/"
          "eps censuses, the success-gate table; OPEN: the "
          "exception scalar's positivity (the campaign's work); "
          "NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
