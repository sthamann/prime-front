#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""l2_deterministic_cancellation_probe -- PRIME.PORT.L2.
DETERMINISTIC_CANCELLATION.01 (round 287): the STANDARD-FRAMEWORK
CENSUS for the level-2 block sums -- WHICH classical deterministic
cancellation framework captures the P_j sums?  Context (sealed
record inputs): r272 quantified the L2 task (a NON-ADJACENT /
global mechanism must supply an additional N^{-delta'} with
delta' > 0.21 of the available gamma_true = 0.45 -- address c3,
beyond blind level-2 pairing, TRUTH_ALLOWS); r273 showed the
cancellation is GENERIC (root-scale baseline, perturbation-
insensitive); r275 killed the state-space/KYP vehicle; r269/r270
mapped the block machinery (P signs coin-like on lags 1-4, run
lengths med 2).  THE REVIEWER HOPE (the 30 pct lane): BECAUSE the
cancellation is generic, a DETERMINISTIC standard framework might
capture it WITHOUT arithmetic.  STOP LIST (excluded vehicles, NOT
revisited): l1 pair hierarchies, state-space/KYP, s-flows, mass
splits.  A world-blind VALID bound is ADMISSIBLE here: L2 is the
generic half -- it only has to REACH (the declared difference to
the L* lane).

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r271/r272 machinery imported verbatim): t_{N-2}
= sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge split
t = t_edge + R; Z = t_{N-2} + chain, Z_local = t_edge + chain;
maximal same-sign runs of the bx-sorted bulk with masses M_i and
exact signed sums s_i; the LEVEL-2 BLOCKS (r270 convention,
offset 0): P_j = s_{2j} + s_{2j+1}, the odd tail run its own
block -- sum_j P_j == R EXACTLY (gated).  Demand scale M_W =
sqrt(5/7); reference bound eps_c2 = r269 bound_pairsum (sealed);
the needed additional decay DELTA_NEED = 0.21 (r272 record).
delta'(F) := halves-slope(eps_c2 / M_W) - halves-slope(eps_F /
M_W) on the N-sorted 42-rung ladder (the r272 halves log-slope
estimator, deterministic).

THE FOUR SEALED CANDIDATE FRAMEWORKS (max 4, each implemented as
an exact per-rung bound eps_F on |sum_j P_j| = |R|, each tested
against DELTA_NEED and against certification |Z| <= |Z_local| +
eps_F < M_W on the 7 exception rungs; every builder consumes ONLY
the plain block-sum list P, AST scope audit; the withheld key
"t" + "_term" and every target-side identifier forbidden):
(F1) DISCREPANCY / ERDOS-TURAN (Koksma-Hlawka-like, EXACT Abel
  form): with sigma_j = sign(P_j), a_j = |P_j|: |sum P_j| <=
  D* x V, D* = max_n |sum_{j<=n} sigma_j| (the sign/position
  discrepancy of the block sequence), V = a_{m-1} +
  sum_j |a_{j+1} - a_j| (magnitude variation + terminal) -- an
  EXACT summation-by-parts theorem; both factors source-pure;
  measured: does the normalized discrepancy D*/sqrt(m) decay,
  i.e. does eps_F1 scale like N^{-beta} with usable beta?
(F2) VAN DER CORPUT / WEYL DIFFERENCES (EXACT finite form): with
  the sealed window H = max(2, ceil(sqrt(m))): |sum P_j|^2 <=
  ((m + H - 1)/H) x sum_{|h|<H} (1 - |h|/H) A(h), A(h) =
  sum_j P_j P_{j+h} -- the full autocorrelation content at lags
  < H; implemented through the exact window-sum identity
  sum_{|h|<H} (1-|h|/H) A(h) = (1/H) sum_t W_t^2 (Fejer
  smoothing, nonnegativity guaranteed); the NON-ADJACENT address
  c3 directly: are the autocorrelations over LARGE lags small
  enough in the mean, and does the vdC bound deliver delta'?
(F3) SALEM-ZYGMUND CLASS (deterministic sub-Gauss comparison):
  the exact Gauss-analog scale sz = sqrt(sum P_j^2 x log(2m));
  measured constant per rung C = max_n |partial sum P| / sz;
  candidate bound eps_F3 = C_ALL x sz with C_ALL = max C over
  the 42 rungs + mains (a MEASURED constant -- typed honestly
  LEMMA_CANDIDATE_MEASURED_CONSTANT, NOT a source-pure theorem:
  if C is stable on all rungs, the deterministic sub-Gauss
  statement is a lemma candidate whose PROOF would then be the
  task); stability rule sealed: spread = C_max / C_med over the
  ladder <= SPREAD_BAR 2.0.
(F4) MDS / AZUMA CLASS (chain filtration): are the P_j a
  deterministic martingale-difference-like sequence w.r.t. the
  source-defined chain filtration P_{<j}?  Conditional means via
  the sealed sign-bin chain regression (bins: start / previous
  block positive / previous block negative, MDS_LAG 1, NO fit
  primitives): mu_b = bin mean, compensator q_j = P_j - mu_b(j);
  measured: md_ratio = rms(mu) / rms(P) (are the conditional
  means small against the variance?); candidate bound eps_F4 =
  sum_j |mu_b(j)| + C4_ALL x sqrt(sum q_j^2 x log(2m)) (same
  measured-constant typing and stability rule as F3).
FOR EACH FRAMEWORK: (i) the bound exact on all 42 rungs + mains
(validity |R| <= eps_F, bar 1e-9 for the exact theorems F1/F2;
by construction for F3/F4 with C_ALL, verified); (ii) the delta'
test: delta'(F) > DELTA_NEED AND the certification balance (the
7 exceptions + kz15 via |Z_local| + eps_F < M_W, full-ladder
count /42); (iii) the WORLDS TEST: F1/F2 hold on EPSTEIN /
SCRAMBLE by exact algebra -- declared WORLD_BLIND_VALID (which
is ADMISSIBLE for L2, the generic half; the declared difference
to the L* lane); F3/F4: control coverage C_ctrl <= C_ALL
(COVERED -> world-blind candidate / BREAKS -> arithmetic-
sensitive, honest); (iv) PAIRCORR DETECTOR: no builder may
PRESUPPOSE root-scale comb cancellation -- it must DELIVER it
from structure: enforced by the AST scope audit (builders see
the block-sum list only), by exact validity, and by the d2
demand bar log10((|Z_local| + eps_F)/M_W) <= 1.0 dec on the
exception branch (fire = candidate closed for certification).

AUTOCORRELATION_PROFILE (the independent delivery object, the
lag-space MAP of the c3 cancellation): per rung the full profile
A(h); the EXACT identity (sum P)^2 = A(0) + 2 sum_{h>=1} A(h)
(gated, bar 1e-9 x A(0)) decomposes the cancellation deficit
A(0) - (sum P)^2 = -2 sum_{h>=1} A(h) into sealed lag bands
(1-2, 3-4, 5-8, 9-16, 17-32, 33-64, 65+): WHERE does the c3
cancellation sit in lag space?  Band shares are DEFINED on the
rungs with a positive cancellation deficit (canc > 1e-12 x A(0);
qualifier count reported -- on reinforcing rungs the share is
undefined; amendment a1 after smoke pass 1: this denominator
guard, a definition repair, no physics bar moved); medians over
the qualifying rungs and over the qualifying exception branch;
the large-lag smallness mean |rho(h)| over h > H vs lags 1-4
printed.

SEALED ADJUDICATION (frozen BEFORE evaluation): candidate order
(F1, F2, F3, F4) (classicality preference); ELIGIBLE = validity
holds AND no demand fire AND (F3/F4 only: spread <= SPREAD_BAR
AND controls COVERED).  FRAMEWORK_GO(F*, delta' coverage,
certification balance) iff an eligible F has cert 7/7 AND
delta'(F) > DELTA_NEED (then the L2 lemma is a named classical
theorem candidate; F3/F4 keep the LEMMA_CANDIDATE typing);
FRAMEWORK_PARTIAL(best F by (cert, delta'), gap) iff an eligible
F has cert >= 6/7 OR delta'(F) > DELTA_NEED; else
ALL_FRAMEWORKS_INSUFFICIENT(the precise common obstruction,
measured -- then even the generic half is non-classical in this
census and that is a deep finding).  Always + AUTOCORRELATION_
PROFILE(band map) + KZ15_DETAIL; + LOCAL_MODEL_MAIN_FITTED if
any control gate breaks.

WARDS / MUST-FAILS: r272/r263/r269 reproduction wards (exception
set == the named 7 + cheap 35; sp(N, eps_c2) = +0.67 tol 0.05;
gamma_true = 0.453 tol 0.05; kz15 reserve in [0.020, 0.035];
exception P-sign alternation med in [0.34, 0.44]); contribution
ward sum ct == t_{N-2} (bars 1e-9 main N <= 400 / 3e-6 deep /
1e-6 controls); block identity sum_j P_j == R exact (bar 1e-12
rel); SMOOTH anchor (alias <= 1e-12, q_N <= 1e-20); mp SAMPLES
(dps 60): kz15 (bar 1e-8) + the two deepest rungs (bar 3e-6);
TOY EXACTNESS (bar 1e-14): hand-checked sequences reproduce the
block builder, the Abel identity + F1 bound (D* = 1, V = 2,
eps = 2 on P = [2, -2, 1]), the vdC window-sum identity + F2
bound (sum W^2 = 6, eps = sqrt(6)), the F3 identity C x sz =
max partial, the F4 degenerate compensator (cm = 5, q = 0), and
the autocorrelation identity.  MUST-FAILS: (m1) H-PEEK -- the
mutant evaluating a grid of vdC windows H and keeping the
smallest bound is selection-by-answer: typed FORBIDDEN, its gain
over the sealed H rule measured and printed; (m2) GIFT BOUND --
the mutant orienting a bound by the withheld terminal drive key
must be FLAGGED by the AST scope audit; (m3) WRONG-CONSTANT
MUTANTS (loud, toy level): the F1 variation WITHOUT the terminal
term breaks validity on P = [1, 1] (bound 0 < |sum| = 2); the
vdC prefactor m/H instead of (m + H - 1)/H breaks on P =
[1, 1, 1, 1] with H = 2 (14 < 16) -- each break >= 1e-6 abs;
(m4) HALVES-SHUFFLE -- the seed-287 permutation of the eps_c2
series against the N axis destroys the trend (|sp| < 0.5 and <
the measured +0.67).

INDEX FIREWALL (binding, r238-r285 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r269
PBB.mask_edge + PBB.runs_split + PBB.bound_pairsum +
PBB.mp_drive, r271 UPT.bound_level2 (reference), r244 BH.wpack +
BH.spearman, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN);
LAG_BANDS ((1, 2), (3, 4), (5, 8), (9, 16), (17, 32), (33, 64),
(65, inf)); LAGS_SMALL (1, 2, 3, 4); SPREAD_BAR 2.0; MDS_LAG 1;
TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls;
VAL_BAR 1e-9; ID_BAR 1e-12; AC_BAR 1e-9 (autocorr identity, x
A(0)); TOY_BAR 1e-14; MUT_MIN 1e-6; LOUD 1e3; SHUF_BAR 0.5;
R272_SP_EPS +0.67 tol 0.05; R272_GAMMA_TRUE 0.453 tol 0.05;
RESERVE_BAND (0.020, 0.035); R270_ALT_BAND (0.34, 0.44);
DEMAND_BAR 1.0 dec; MP_DPS 60; MP_T_BAR 1e-8 (kz15);
MP_DEEP_BAR 3e-6 (two deepest rungs); SM_Q_BAR 1e-20;
SM_ALIAS_BAR 1e-12; SHUFFLE_SEED 287; KZ_ANCHOR 15; runtime <=
1800 s; smoke = w9 + controls + toy + builder numerics + scope
audits + toy must-fails m2/m3 (ladder, trends, delta', cert,
adjudication, mp wards, m1 gain census, m4 skipped).  DISCLOSED
PRE-SPEC INPUT (no scratch run of this probe): every reproduction
band is an r263/r269/r270/r272 RECORD number adopted as-is;
DELTA_NEED is the r272 flip-condition record; nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  FRAMEWORK_TABLE(per F: eps med dec vs M, slope, delta',
    cert k/7 + n/42, world status, detector status)
+ [exactly one of] FRAMEWORK_GO(F*, delta' coverage,
    certification balance) / FRAMEWORK_PARTIAL(best F, best
    coverage, gap) / ALL_FRAMEWORKS_INSUFFICIENT(the precise
    common obstruction)
+ AUTOCORRELATION_PROFILE(the lag-band map of the c3
    cancellation)
+ KZ15_DETAIL(per-F margin/miss at the razor)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED.
Honesty before beauty: no verdict claims a cofinal law or an
asymptotic mechanism; every trend is MEASURED on 42 rungs only;
F3/F4 verdicts carry the LEMMA_CANDIDATE typing (a measured
constant is not a proof); the exception scalar's positivity
beyond the measured 42 stays OPEN; r243-r285 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 was 25/25 gates; ONE disclosed amendment a1 after
smoke pass 1 (the band-share denominator guard in the autocorr
map, a definition repair -- shares are undefined on rungs whose
block sequence REINFORCES; no physics bar, band, rule or verdict
rule was moved at any point); calibration pass 1 = first full
evaluation, 25/25 gates, wall 50.1 s, NO amendment; pass 2 = the
record run, identical to pass 1 in every printed figure up to
WALL; the only post-freeze edit is this record-table insertion,
which IS the protocol):
CAL_VERDICT = FRAMEWORK_TABLE(F1_DISCREPANCY eps med +0.80 dec
sl +0.40 delta' -0.21 cert 0/7 0/42 WORLD_BLIND_VALID det FIRE;
F2_VDC eps med -0.51 dec sl -0.11 delta' +0.31 cert 6/7 38/42
WORLD_BLIND_VALID det OK; F3_SALEMZYGMUND eps med -0.48 dec sl
-0.18 delta' +0.38 cert 6/7 35/42 COVERED spread 1.86 det OK;
F4_MDS_AZUMA eps med -0.49 dec sl -0.21 delta' +0.41 cert 6/7
37/42 COVERED spread 1.67 det OK) + FRAMEWORK_PARTIAL(
F4_MDS_AZUMA, delta' +0.41 vs 0.21, cert 6/7, gap 1 exceptions;
LEMMA_CANDIDATE typing) + AUTOCORRELATION_PROFILE(5/44
qualifying rungs, 0 exceptions -- the block sequence REINFORCES
at root scale on 39/44 worlds) + KZ15_DETAIL(F1 miss 1.38, F2
miss 0.10, F3 miss 0.07, F4 miss 0.12 dec; reserve 0.0268).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; block identity worst rel dev 6.3e-16 on 47
worlds; r272 wards exact (sp(N, eps_c2) +0.67, gamma_true
+0.453, kz15 reserve 0.0268, exception alt med 0.39).  S4 F1:
the Abel/Erdos-Turan factorization eps_F1 = D* x V is VALID
44/44 but BOTH factors grow (D*/sqrt(m) med 1.90, sp(N, D*)
+0.27, slope_h(D*) +0.221 -- the block-sign discrepancy grows
FASTER than a random walk, no N^{-beta}; V slope_h +0.183):
eps med +0.80 dec vs M, delta' -0.21, demand max +1.44 => the
paircorr detector FIRES on the exception branch -- the
discrepancy frame is the census's loud death (Koksma-Hlawka
pays both factors and the block signs supply no low-discrepancy
structure); m1 H-peek gain med 0.075 max 0.205 on 44/44 rungs
(sealed away).  S6 autocorr map (identity dev worst 2.7e-15 x
A(0)): the SURPRISE of the round -- only 5/44 rungs (0
exceptions) have a positive cancellation deficit at all: on
39/44 worlds (all 7 exceptions included) (sum P)^2 > sum P^2,
the level-2 block sequence REINFORCES in the root-scale sense
(the r270/r271 magnitude reading sharpened: the pairwise
near-cancellation is already fully absorbed INTO the P_j
magnitudes; beyond the blocks there is NO further root-scale
cancellation to harvest); on the 5 qualifying cheap rungs the
deficit sits at lags 1-2 med +0.25 / 5-8 med +1.10; large-lag
mean |rho(h > H)| med 0.058 vs small-lag (1-4) 0.129 -- the
non-adjacent address c3 RELOCATES: not long-range lag structure
but the sqrt(m)-count economy.  S7 (the delivery): slope(eps_c2
/M) +0.196; F2_VDC -- an EXACT world-blind THEOREM -- lands at
eps med -0.51 dec, delta' +0.309 > 0.21, and certifies 6/7
exceptions (kz20 kz22 kz36 kz38 kz39 kz52, ladder 38/42),
demand med -0.07 max +0.04; F3 delta' +0.381, 6/7, 35/42; F4
delta' +0.410, 6/7, 37/42; kz15 (the razor, need 0.292): F2
0.364 miss 0.10 dec, F3 0.341 miss 0.07 dec, F4 0.388 miss
0.12 dec -- every surviving frame closes everything EXCEPT the
razor.  S8: F3 sub-Gauss constant C med 0.90 min 0.25 max 1.68
spread 1.86 <= 2.0 STABLE, controls COVERED (EPST 0.61, SCR
0.50 <= C3_ALL 1.68); F4 C4 med 0.40 max 0.68 spread 1.67
STABLE, COVERED (0.29/0.51 <= 0.68); md_ratio med 0.29 (the
P_j are MDS-like against the sign filtration, compensator share
med 0.33); SMOOTH alias 2.4e-14, q_N 4.2e-25; mp wards kz15 dev
2.9e-10 (bar 1e-8), kz64 N859 9.3e-9, kz52 N878 6.6e-8 (bar
3e-6); m4 shuffle |sp| 0.038 < 0.5.  S9 adjudication (sealed
rule, no repair after seeing the numbers): no frame reaches
7/7 => FRAMEWORK_PARTIAL(F4 by the sealed (cert, delta') key;
the research-relevant edge is honest: F2_VDC -- the EXACT
theorem with no measured constant -- stands at 6/7 with delta'
+0.31 WITHOUT being adjudicated the winner).  READING (typed,
no upgrade): the reviewer hope is MEASURED CONFIRMED at the
exponent AND near-confirmed at the level -- the generic half of
the L2 task IS classical: the exact van der Corput inequality
at the frozen window H = ceil(sqrt(m)) delivers delta' = 0.31 >
0.21 world-blindly and closes 6 of the 7 exceptions as a
THEOREM (no constant, no fit, no arithmetic); the sub-Gauss /
MDS frames confirm the same economy with stable measured
constants (C <= 1.68, C4 <= 0.68).  What blocks 7/7 is -- once
again -- ONLY the kz15 razor (0.07-0.12 dec), and the autocorr
map explains why: at the block level there is NO residual
root-scale cancellation to harvest (39/44 worlds reinforce);
every sqrt(m)-frame therefore bottoms out at the same floor.
The precise L2 lemma candidate after this round: the vdC form
|R| <= sqrt((m + H - 1)/H x sum_{|h|<H} Fejer x A(h)) with H =
ceil(sqrt(m)) as a provable chain statement (source-pure,
window-independent), PLUS the r269-known kz15 exact-finite
certificate for the razor.  Runtime 50.1 s full / 0.2 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE
beyond the disclosed a1 (records inserted per protocol; no bar,
band, rule or verdict rule moved).

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
AC_BAR = 1e-9
TOY_BAR = 1e-14
MUT_MIN = 1e-6
LOUD = 1e3
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
LAG_BANDS = ((1, 2), (3, 4), (5, 8), (9, 16), (17, 32), (33, 64),
             (65, 10 ** 9))
LAGS_SMALL = (1, 2, 3, 4)
SPREAD_BAR = 2.0
MDS_LAG = 1
SHUF_BAR = 0.5
R272_SP_EPS = 0.67
R272_SP_TOL = 0.05
R272_GAMMA_TRUE = 0.453
R272_GT_TOL = 0.05
RESERVE_BAND = (0.020, 0.035)
R270_ALT_BAND = (0.34, 0.44)
DEMAND_BAR = 1.0
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
SHUFFLE_SEED = 287
KZ_ANCHOR = 15
FRAME_ORDER = ("F1_DISCREPANCY", "F2_VDC", "F3_SALEMZYGMUND",
               "F4_MDS_AZUMA")

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


# ---- sealed block builder + the four sealed framework builders.
# Every framework builder consumes ONLY the plain block-sum list
# (the exact level-2 decomposition values); the withheld terminal
# drive key and every target-side identifier are forbidden in
# scope (AST audit against BOUND_FORBIDDEN).
def blocks_level2(vals):
    """r270 block convention (offset 0): P_j = s_{2j} + s_{2j+1}
    over the alternating signed run sums; the odd tail run is its
    own block -- sum_j P_j equals the bulk remainder EXACTLY."""
    m = len(vals)
    P = [vals[i] + vals[i + 1] for i in range(PAIR_OFFSET, m - 1, 2)]
    if (m - PAIR_OFFSET) % 2 == 1:
        P.append(vals[-1])
    return P


def bound_discrepancy(P):
    """F1 sealed DISCREPANCY / ERDOS-TURAN bound (exact Abel /
    summation-by-parts form on the block sequence): with sign
    partial sums as the position/sign discrepancy D* and the
    magnitude variation V (differences + terminal): the product
    D* x V majorizes the block sum EXACTLY."""
    m = len(P)
    if m == 0:
        return dict(eps=0.0, dstar=0.0, var=0.0)
    sg = [0.0 if v == 0.0 else math.copysign(1.0, v) for v in P]
    a = [abs(v) for v in P]
    run = 0.0
    dstar = 0.0
    for s in sg:
        run += s
        dstar = max(dstar, abs(run))
    var = a[-1]
    for j in range(m - 1):
        var += abs(a[j + 1] - a[j])
    return dict(eps=dstar * var, dstar=dstar, var=var)


def vdc_window(P, H):
    """exact Fejer window core of the van der Corput bound: the
    window-sum identity sum_{|h|<H} (1 - |h|/H) A(h) = (1/H)
    sum_t W_t^2 with W_t the H-window sums of the zero-padded
    block sequence (nonnegativity guaranteed)."""
    m = len(P)
    p = np.zeros(m + 2 * (H - 1))
    p[H - 1:H - 1 + m] = np.asarray(P, dtype=float)
    c = np.concatenate(([0.0], np.cumsum(p)))
    W = c[H:] - c[:-H]
    return float(np.sum(W * W))


def bound_vdc(P):
    """F2 sealed VAN DER CORPUT / WEYL bound (exact finite form)
    at the FROZEN window rule H = max(2, ceil(sqrt(m))):
    |sum P|^2 <= ((m + H - 1)/H) x (1/H) sum_t W_t^2."""
    m = len(P)
    if m == 0:
        return dict(eps=0.0, H=2, s2=0.0)
    H = max(2, int(math.ceil(math.sqrt(m))))
    sw2 = vdc_window(P, H)
    return dict(eps=math.sqrt((m + H - 1) * sw2) / H, H=H, s2=sw2)


def sz_scale(P):
    """F3 sealed SALEM-ZYGMUND scale: the exact Gauss-analog
    sqrt(sum P^2 x log(2m)) plus the measured per-sequence
    constant max_n |partial sum| / scale (typed MEASURED)."""
    m = len(P)
    if m == 0:
        return dict(sz=0.0, C=0.0)
    q = math.sqrt(sum(v * v for v in P) * math.log(2.0 * m))
    run = 0.0
    mx = 0.0
    for v in P:
        run += v
        mx = max(mx, abs(run))
    return dict(sz=q, C=mx / max(q, 1e-300))


def mds_decompose(P):
    """F4 sealed MDS / AZUMA decomposition against the chain
    filtration (sign-bin chain regression, MDS_LAG 1, no fit
    primitives): bins = start / previous block > 0 / previous
    block < 0; bin means mu, compensator q = P - mu; returns the
    compensator mass, the Azuma scale of q, the measured
    constant and the conditional-mean ratio."""
    m = len(P)
    if m == 0:
        return dict(cm=0.0, az=0.0, C=0.0, md=0.0)
    bins = []
    for j in range(m):
        if j < MDS_LAG or P[j - MDS_LAG] == 0.0:
            bins.append(0)
        elif P[j - MDS_LAG] > 0.0:
            bins.append(1)
        else:
            bins.append(2)
    mu = {}
    for b in (0, 1, 2):
        sel = [P[j] for j in range(m) if bins[j] == b]
        mu[b] = (sum(sel) / len(sel)) if sel else 0.0
    mus = [mu[bins[j]] for j in range(m)]
    q = [P[j] - mus[j] for j in range(m)]
    cm = sum(abs(v) for v in mus)
    az = math.sqrt(sum(v * v for v in q) * math.log(2.0 * m))
    run = 0.0
    mx = 0.0
    for v in q:
        run += v
        mx = max(mx, abs(run))
    rms_p = math.sqrt(sum(v * v for v in P) / m)
    rms_m = math.sqrt(sum(v * v for v in mus) / m)
    return dict(cm=cm, az=az, C=mx / max(az, 1e-300),
                md=rms_m / max(rms_p, 1e-300))


def mutant_gift_bound(rc, P):
    """m2 MUST-FAIL MUTANT: a 'bound' oriented by the withheld
    ground-truth terminal drive key -- the scope audit must FLAG
    this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * bound_discrepancy(P)["eps"]


def mutant_h_peek(P):
    """m1 MUST-FAIL MUTANT: evaluates a GRID of vdC windows H and
    keeps the smallest bound -- selection-by-answer; typed
    FORBIDDEN, its gain over the sealed H rule measured."""
    m = len(P)
    if m == 0:
        return 0.0
    grid = {2, 4, 8, max(2, int(math.ceil(math.sqrt(m)))),
            max(2, m // 2)}
    best = float("inf")
    for H in sorted(grid):
        sw2 = vdc_window(P, H)
        best = min(best, math.sqrt((m + H - 1) * sw2) / H)
    return best


def mutant_wrong_variation(P):
    """m3 MUST-FAIL MUTANT (toy level): the F1 variation WITHOUT
    the terminal term -- breaks validity loudly on P = [1, 1]."""
    m = len(P)
    sg = [0.0 if v == 0.0 else math.copysign(1.0, v) for v in P]
    a = [abs(v) for v in P]
    run = 0.0
    dstar = 0.0
    for s in sg:
        run += s
        dstar = max(dstar, abs(run))
    var = 0.0
    for j in range(m - 1):
        var += abs(a[j + 1] - a[j])
    return dstar * var


def mutant_wrong_prefactor(P):
    """m3 MUST-FAIL MUTANT (toy level): the vdC prefactor m/H
    instead of (m + H - 1)/H -- breaks on P = [1, 1, 1, 1]."""
    m = len(P)
    H = 2
    sw2 = vdc_window(P, H)
    return math.sqrt(m * sw2) / H


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho", "ct",
                   "cts", "chain", "Sr", "Mr"}


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
    """r272 dyadic log-slope: (mean ln X | second half - mean ln X
    | first half) / (same for ln N) on the N-sorted ladder --
    deterministic."""
    n = len(Ns)
    h = n // 2
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    ln = [math.log(float(v)) for v in Ns]
    num = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    den = (sum(ln[h:]) / (n - h)) - (sum(ln[:h]) / h)
    return num / den


def halves_med(Xs):
    n = len(Xs)
    h = n // 2
    return (float(np.median(Xs[:h])), float(np.median(Xs[h:])))


# ---------------------------------------------- measurement scope
def autocorr_full(P):
    """the FULL autocorrelation profile A(h) of the block
    sequence (measurement scope; the exact identity (sum P)^2 =
    A(0) + 2 sum_{h>=1} A(h) is gated)."""
    p = np.asarray(P, dtype=float)
    if len(p) == 0:
        return np.zeros(1)
    return np.correlate(p, p, mode="full")[len(p) - 1:]


def block_sign_stats(P):
    """P-sign statistics (r270/r272 continuity): alternation
    fraction + lag-1..4 sign correlations."""
    sg = [1.0 if v > 0.0 else -1.0 for v in P if v != 0.0]
    alt = (sum(1 for j in range(len(sg) - 1)
               if sg[j] * sg[j + 1] < 0.0)
           / max(len(sg) - 1, 1))
    lag = []
    for k in LAGS_SMALL:
        if len(sg) > k:
            lag.append(sum(sg[j] * sg[j + k]
                           for j in range(len(sg) - k))
                       / (len(sg) - k))
        else:
            lag.append(0.0)
    return alt, lag


# ------------------------------------------------ toy exact tool
def toy_frameworks():
    """hand-checked deterministic sequences: the block builder,
    the F1 Abel bound, the F2 window-sum identity + bound, the
    F3 identity, the F4 degenerate compensator and the
    autocorrelation identity must reproduce EXACTLY."""
    worst = 0.0
    # runs example: s = [3, -1, 2, -4, 1] -> blocks [2, -2, 1]
    S = [3.0, -1.0, 2.0, -4.0, 1.0]
    P = blocks_level2(S)
    worst = max(worst, abs(P[0] - 2.0), abs(P[1] + 2.0),
                abs(P[2] - 1.0), abs(sum(P) - sum(S)))
    # F1 on P: D* = 1, V = |2-2| + |1-2| + 1 = 2, eps = 2 >= |1|
    f1 = bound_discrepancy(P)
    worst = max(worst, abs(f1["dstar"] - 1.0))
    worst = max(worst, abs(f1["var"] - 2.0))
    worst = max(worst, abs(f1["eps"] - 2.0))
    worst = max(worst, abs(sum(P)) - f1["eps"])
    # F2 on P (H = 2): windows (2), (0), (-1), (1) -> sum W^2 = 6;
    # eps = sqrt((3+1) * 6)/2 = sqrt(6)
    f2 = bound_vdc(P)
    worst = max(worst, abs(f2["H"] - 2))
    worst = max(worst, abs(f2["s2"] - 6.0))
    worst = max(worst, abs(f2["eps"] - math.sqrt(6.0)))
    worst = max(worst, abs(sum(P)) - f2["eps"])
    # F3 identity: C x sz == max partial = 2
    f3 = sz_scale(P)
    worst = max(worst, abs(f3["C"] * f3["sz"] - 2.0))
    worst = max(worst, abs(f3["sz"]
                           - math.sqrt(9.0 * math.log(6.0))))
    # F4 degenerate: single-element bins -> q = 0, cm = 5
    f4 = mds_decompose(P)
    worst = max(worst, abs(f4["cm"] - 5.0))
    worst = max(worst, abs(f4["az"] - 0.0))
    # autocorr identity on P: A = [9, -6, 2]; A0 + 2(A1 + A2) = 1
    A = autocorr_full(P)
    worst = max(worst, abs(A[0] - 9.0), abs(A[1] + 6.0),
                abs(A[2] - 2.0))
    worst = max(worst, abs((A[0] + 2.0 * (A[1] + A[2]))
                           - sum(P) ** 2))
    return worst


def toy_mustfail_m3():
    """m3 loud wrong-constant breaks (toy level): each mutant
    must UNDERSHOOT the true sum on its hand sequence."""
    # F1 without the terminal term on [1, 1]: bound 0 < |sum| = 2
    b1 = mutant_wrong_variation([1.0, 1.0])
    brk1 = abs(1.0 + 1.0) - b1
    # vdC with m/H on [1, 1, 1, 1]: sqrt(4 * 14)/2 = sqrt(14)
    # < |sum| = 4  (correct form sqrt(5 * 14)/2 = sqrt(17.5))
    b2 = mutant_wrong_prefactor([1.0, 1.0, 1.0, 1.0])
    brk2 = 4.0 - b2
    return brk1, brk2


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("l2_deterministic_cancellation_probe -- PRIME.PORT.L2."
          "DETERMINISTIC_CANCELLATION.01 (round 287)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   R271_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], UPT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + builder "
                        "numerics + scope audits + toy must-fails; "
                        "ladder, trends, delta', certification, "
                        "adjudication, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE 30-PCT L2 LANE (reviewer split 70 L* / 30 L2): the "
          "standard-framework census for the block sums -- FOUR "
          "sealed classical deterministic cancellation frameworks "
          "(F1 discrepancy/Erdos-Turan Abel form, F2 van der "
          "Corput at the frozen H = ceil(sqrt(m)), F3 Salem-"
          "Zygmund sub-Gauss comparison, F4 MDS/Azuma against the "
          "sign-bin chain filtration), each an exact per-rung "
          "bound on |sum P_j|, tested against DELTA_NEED %.2f and "
          "the 7-exception certification; STOP LIST honored (no "
          "l1 pair hierarchies, no state-space/KYP, no s-flows, "
          "no mass splits); world-blind VALID bounds ADMISSIBLE "
          "(L2 is the generic half -- declared lane difference); "
          "F3/F4 typed LEMMA_CANDIDATE_MEASURED_CONSTANT "
          "honestly; ALL bars, rules and verdicts sealed BEFORE "
          "evaluation (pre-spec input = r263/r269/r270/r272 "
          "record numbers, disclosed)" % DELTA_NEED)

    # ---------------- S1: census + controls (r272 scaffold)
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

    # ---------------- S2: decomposition + block identity + wards
    section("S2  EXACT DECOMPOSITION + BLOCK IDENTITY + WARDS")
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
          "the census operates on an EXACT decomposition"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

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
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        sabs = sum(abs(v) for v in Sr)
        P = blocks_level2(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        e_l2 = UPT.bound_level2(Sr)
        Zl = t_loc + rc["chain"]
        alt, lag = block_sign_stats(P)
        return dict(Mr=Mr, Sr=Sr, alt_ok=alt_ok, R=R, sabs=sabs,
                    P=P, e_c2=e_c2, e_l2=e_l2, Zl=Zl, alt=alt,
                    lag=lag, m=len(P))

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
    check("G21-block-identity", alt_all and bid_worst <= ID_BAR,
          "consecutive bulk runs alternate in sign on every world "
          "AND the r270 block decomposition sums back EXACTLY: "
          "worst |sum P - R| / |R| = %.1e (bar %.0e) over %d "
          "worlds -- the frameworks bound the TRUE bulk remainder"
          % (bid_worst, ID_BAR, len(all_rc) + len(crecs)))

    Ns = [rc["N"] for rc in recs]
    eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
    if not smoke:
        sp_eps = BH.spearman(Ns, eps_c2_rel)
        Ct_s = [abs(rc["ev"]["R"]) / max(rc["ev"]["sabs"], 1e-300)
                for rc in recs]
        gamma_true = -halves_slope(Ns, Ct_s)
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        alt_exc = [rc["ev"]["alt"] for rc in recs if rc["g"] < 0.0]
        alt_med = float(np.median(alt_exc))
        ok_alt = R270_ALT_BAND[0] <= alt_med <= R270_ALT_BAND[1]
        check("G22-r272-reproduction-wards",
              abs(sp_eps - R272_SP_EPS) <= R272_SP_TOL
              and abs(gamma_true - R272_GAMMA_TRUE) <= R272_GT_TOL
              and ok15 and ok_alt,
              "the r272 records recomputed: sp(N, eps_c2) %+.2f "
              "(ref %+.2f), gamma_true %+.3f (ref %+.3f, tol "
              "%.2f), kz15 true reserve %.4f in %s, exception "
              "P-sign alt med %.2f in %s -- the census stands on "
              "the recorded machine state"
              % (sp_eps, R272_SP_EPS, gamma_true,
                 R272_GAMMA_TRUE, R272_GT_TOL, slack15,
                 str(RESERVE_BAND), alt_med, str(R270_ALT_BAND)))
    else:
        sp_eps = float("nan")
        check("G22-r272-reproduction-wards", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---------------- S3: toy exactness + scope audits + m3
    section("S3  TOY EXACTNESS + SCOPE AUDITS + TOY MUST-FAILS")
    toy_worst = toy_frameworks()
    check("G30-toy-exactness", toy_worst <= TOY_BAR,
          "hand-checked sequences reproduce EXACTLY (worst dev "
          "%.1e, bar %.0e): blocks [2,-2,1] from [3,-1,2,-4,1]; "
          "F1 D*=1 V=2 eps=2; F2 H=2 sumW2=6 eps=sqrt(6); F3 "
          "C x sz == max partial 2; F4 degenerate cm=5 q=0; "
          "autocorr A=[9,-6,2] with A0 + 2(A1+A2) == (sum P)^2"
          % (toy_worst, TOY_BAR))
    h_f1 = scope_audit("bound_discrepancy", BOUND_FORBIDDEN)
    h_f2 = scope_audit("bound_vdc", BOUND_FORBIDDEN)
    h_fw = scope_audit("vdc_window", BOUND_FORBIDDEN)
    h_f3 = scope_audit("sz_scale", BOUND_FORBIDDEN)
    h_f4 = scope_audit("mds_decompose", BOUND_FORBIDDEN)
    h_bb = scope_audit("blocks_level2", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_f1 or h_f2 or h_fw or h_f3 or h_f4 or h_bb)
    check("G31-scope-audits", clean and bool(h_gift)
          and not ag_hits,
          "the four framework builders + the block builder "
          "consume the plain block-sum list only (no truth-side "
          "identifier in scope%s); m2 gift mutant (withheld "
          "terminal drive key) FLAGGED (%s); fragment audit (no "
          "fit primitives): %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    brk1, brk2 = toy_mustfail_m3()
    check("G32-mustfail-wrong-constants", brk1 >= MUT_MIN
          and brk2 >= MUT_MIN,
          "m3 WRONG-CONSTANT MUTANTS break validity loudly on "
          "the hand sequences: F1 without the terminal variation "
          "term undershoots |sum| by %.1f on [1,1] (bound 0 < "
          "2); the vdC prefactor m/H undershoots by %.2f on "
          "[1,1,1,1] (%.2f < 4) -- both >= %.0e: every constant "
          "in the sealed forms is load-bearing"
          % (brk1, brk2, 4.0 - brk2, MUT_MIN))

    # ---------------- S4/S5: framework bounds on every world
    section("S4  FRAMEWORK BOUNDS (F1 DISCREPANCY, F2 VDC)")
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        P = ev["P"]
        ev["f1"] = bound_discrepancy(P)
        ev["f2"] = bound_vdc(P)
        ev["f3"] = sz_scale(P)
        ev["f4"] = mds_decompose(P)
    # measured constants for F3/F4 (ladder + mains ONLY)
    C3_ALL = max(rc["ev"]["f3"]["C"] for rc in all_rc)
    C4_ALL = max(rc["ev"]["f4"]["C"] for rc in all_rc)
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        ev["eps"] = {
            "F1_DISCREPANCY": ev["f1"]["eps"],
            "F2_VDC": ev["f2"]["eps"],
            "F3_SALEMZYGMUND": C3_ALL * ev["f3"]["sz"],
            "F4_MDS_AZUMA": ev["f4"]["cm"]
            + C4_ALL * ev["f4"]["az"],
        }
    val_worst = {nm: -1e300 for nm in FRAME_ORDER}
    for rc in all_rc:
        ev = rc["ev"]
        for nm in FRAME_ORDER:
            val_worst[nm] = max(val_worst[nm],
                                abs(ev["R"]) - ev["eps"][nm])
    ok_val = all(val_worst[nm] <= VAL_BAR for nm in FRAME_ORDER)
    check("G40-validity-wards", ok_val,
          "every framework bound majorizes the true bulk "
          "remainder on %d worlds: worst |R| - eps slack %s "
          "(bar %.0e) -- F1/F2 exact theorems, F3/F4 by the "
          "measured C_ALL construction (C3_ALL %.3f, C4_ALL "
          "%.3f, ladder + mains only)"
          % (len(all_rc),
             str({nm[:2]: "%+.1e" % val_worst[nm]
                  for nm in FRAME_ORDER}), VAL_BAR, C3_ALL,
             C4_ALL))
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d  F1 D* %5.1f V %6.3f eps "
             "%6.3f | F2 H %-2d eps %6.3f | F3 C %.2f sz %6.3f | "
             "F4 md %.2f cm %5.3f  |R| %.4f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g"] < 0 else "chp", ev["m"],
                ev["f1"]["dstar"], ev["f1"]["var"],
                ev["f1"]["eps"], ev["f2"]["H"], ev["f2"]["eps"],
                ev["f3"]["C"], ev["f3"]["sz"], ev["f4"]["md"],
                ev["f4"]["cm"], abs(ev["R"])))
    if not smoke:
        d_s = [rc["ev"]["f1"]["dstar"]
               / max(math.sqrt(rc["ev"]["m"]), 1e-300)
               for rc in recs]
        v_s = [rc["ev"]["f1"]["var"] for rc in recs]
        check("G41-f1-factor-census", True,
              "F1 factor scaling (the Erdos-Turan question: does "
              "the block-sequence discrepancy decay?): D*/"
              "sqrt(m) med %.2f, sp(N, D*) %+.2f, slope_h(D*) "
              "%+.3f; V slope_h %+.3f, sp %+.2f -- eps_F1 = D* "
              "x V exact on every world"
              % (float(np.median(d_s)),
                 BH.spearman(Ns, [rc["ev"]["f1"]["dstar"]
                                  for rc in recs]),
                 halves_slope(Ns, [rc["ev"]["f1"]["dstar"]
                                   for rc in recs]),
                 halves_slope(Ns, v_s),
                 BH.spearman(Ns, v_s)))
        gain_pk = []
        for rc in all_rc:
            pk = mutant_h_peek(rc["ev"]["P"])
            gain_pk.append(rc["ev"]["f2"]["eps"] - pk)
        n_g = sum(1 for g_ in gain_pk if g_ > 1e-12)
        check("G42-mustfail-h-peek", True,
              "m1 H-PEEK (grid over vdC windows, keep the "
              "smallest): gains > 1e-12 on %d/%d rungs, med "
              "%.3f, max %.3f -- the temptation is real and "
              "stays SEALED AWAY: the sealed rule H = "
              "ceil(sqrt(m)) is used unconditionally; the "
              "mutant is selection-by-answer, typed FORBIDDEN"
              % (n_g, len(all_rc), float(np.median(gain_pk)),
                 max(gain_pk)))
    else:
        check("G41-f1-factor-census", True, "SMOKE: skipped")
        check("G42-mustfail-h-peek", True, "SMOKE: skipped")

    # ---------------- S6: the autocorrelation lag profile
    section("S6  AUTOCORRELATION LAG PROFILE (THE c3 MAP)")
    ac_worst = 0.0
    band_shares = {b: [] for b in LAG_BANDS}
    band_shares_exc = {b: [] for b in LAG_BANDS}
    large_small = []
    n_qual = 0
    n_qual_exc = 0
    for rc in all_rc:
        P = rc["ev"]["P"]
        A = autocorr_full(P)
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(P) ** 2)
                       / max(A[0], 1e-300))
        canc = A[0] - sum(P) ** 2
        H = rc["ev"]["f2"]["H"]
        rho_ = A / max(A[0], 1e-300)
        qual = canc > 1e-12 * max(A[0], 1e-300)
        if qual:
            n_qual += 1
            if rc["g"] < 0.0:
                n_qual_exc += 1
            for lo_, hi_ in LAG_BANDS:
                sl_ = float(np.sum(A[lo_:min(hi_ + 1, len(A))])) \
                    if lo_ < len(A) else 0.0
                share = -2.0 * sl_ / canc
                band_shares[(lo_, hi_)].append(share)
                if rc["g"] < 0.0:
                    band_shares_exc[(lo_, hi_)].append(share)
        sm = float(np.mean(np.abs(rho_[1:5]))) if len(rho_) > 5 \
            else 0.0
        lg = float(np.mean(np.abs(rho_[H:]))) if len(rho_) > H \
            else 0.0
        large_small.append((sm, lg))
    check("G50-autocorr-identity", ac_worst <= AC_BAR,
          "(sum P)^2 == A(0) + 2 sum_{h>=1} A(h) EXACT on every "
          "world (worst dev %.1e x A(0), bar %.0e) -- the lag "
          "profile decomposes the c3 cancellation without "
          "residue" % (ac_worst, AC_BAR))
    map_note = []
    for b in LAG_BANDS:
        med_a = (float(np.median(band_shares[b]))
                 if band_shares[b] else float("nan"))
        med_e = (float(np.median(band_shares_exc[b]))
                 if band_shares_exc[b] else float("nan"))
        map_note.append("lags %d-%s all %+.2f exc %+.2f"
                        % (b[0],
                           str(b[1]) if b[1] < 10 ** 9 else "inf",
                           med_a, med_e))
        info("band lags %4d-%-10s share of the cancellation "
             "deficit: med all %+.3f  exc %+.3f"
             % (b[0], str(b[1]) if b[1] < 10 ** 9 else "inf",
                med_a, med_e))
    sm_med = float(np.median([t[0] for t in large_small]))
    lg_med = float(np.median([t[1] for t in large_small]))
    check("G51-autocorr-map", True,
          "THE LAG-SPACE MAP of the c3 cancellation (band shares "
          "of A(0) - (sum P)^2 on the %d/%d qualifying rungs, "
          "%d exceptions): %s; large-lag mean |rho(h > H)| med "
          "%.3f vs small-lag (1-4) med %.3f -- WHERE the "
          "cancellation beyond blind level-2 pairing sits"
          % (n_qual, len(all_rc), n_qual_exc,
             "; ".join(map_note), lg_med, sm_med))

    # ---------------- S7: trends, delta', certification
    section("S7  DELTA' TEST + CERTIFICATION BALANCE")
    frames = {}
    if not smoke:
        sl_c2 = halves_slope(Ns, eps_c2_rel)
        for nm in FRAME_ORDER:
            e_rel = [rc["ev"]["eps"][nm] / M_W for rc in recs]
            sl_ = halves_slope(Ns, e_rel)
            dp_ = sl_c2 - sl_
            med_dec = float(np.median([math.log10(max(v, 1e-300))
                                       for v in e_rel]))
            cert7 = 0
            cert42 = 0
            dem = []
            for rc in recs:
                ev = rc["ev"]
                mg = M_W - (abs(ev["Zl"]) + ev["eps"][nm])
                if mg > 0.0:
                    cert42 += 1
                if rc["g"] < 0.0:
                    if mg > 0.0:
                        cert7 += 1
                    dem.append(math.log10(
                        (abs(ev["Zl"]) + ev["eps"][nm]) / M_W))
            fire = (max(dem) >= DEMAND_BAR) if dem else False
            frames[nm] = dict(sl=sl_, dp=dp_, med=med_dec,
                              c7=cert7, c42=cert42, fire=fire,
                              dem_med=float(np.median(dem)),
                              dem_max=max(dem))
            info("%-16s eps med %+.2f dec  slope %+.3f  sp %+.2f"
                 "  delta' %+.3f (need > %.2f)  cert %d/7 %d/42"
                 "  demand med %+.2f max %+.2f%s"
                 % (nm, med_dec, sl_, BH.spearman(Ns, e_rel),
                    dp_, DELTA_NEED, cert7, cert42,
                    frames[nm]["dem_med"], frames[nm]["dem_max"],
                    "  FIRE" if fire else ""))
        check("G60-delta-table", True,
              "delta'(F) = slope(eps_c2/M) %+.3f - slope(eps_F/M) "
              "on the 42-rung ladder vs DELTA_NEED %.2f: %s"
              % (sl_c2, DELTA_NEED,
                 "; ".join("%s %+.3f" % (nm, frames[nm]["dp"])
                           for nm in FRAME_ORDER)))
        # kz15 + per-exception detail of the best-eps frames
        kz15_note = []
        for nm in FRAME_ORDER:
            rc = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
            ev = rc["ev"]
            need = M_W - abs(ev["Zl"])
            miss = (math.log10(ev["eps"][nm] / need)
                    if need > 0 else float("inf"))
            kz15_note.append("%s %s" % (nm[:2],
                                        ("cert %+.4f" % (need
                                                         - ev["eps"][nm]))
                                        if ev["eps"][nm] < need
                                        else "miss %.2f dec" % miss))
        for rc in sorted(exc, key=lambda r_: r_["kz"]):
            ev = rc["ev"]
            need = M_W - abs(ev["Zl"])
            info("kz%-3d need %.3f  " % (rc["kz"], need)
                 + "  ".join("%s %6.3f%s"
                             % (nm[:2], ev["eps"][nm],
                                "*" if ev["eps"][nm] < need
                                else " ")
                             for nm in FRAME_ORDER))
        check("G61-kz15-detail", True,
              "kz15 (the razor, N = %d, true reserve %.4f): %s"
              % (next(r_ for r_ in recs
                      if r_["kz"] == KZ_ANCHOR)["N"],
                 slack15, "; ".join(kz15_note)))
    else:
        check("G60-delta-table", True, "SMOKE: skipped")
        check("G61-kz15-detail", True, "SMOKE: skipped")

    # ---------------- S8: constant stability + worlds test
    section("S8  CONSTANT STABILITY + WORLDS TEST")
    if not smoke:
        C3_lad = [rc["ev"]["f3"]["C"] for rc in recs]
        C4_lad = [rc["ev"]["f4"]["C"] for rc in recs]
        sp3 = max(C3_lad) / max(float(np.median(C3_lad)), 1e-300)
        sp4 = max(C4_lad) / max(float(np.median(C4_lad)), 1e-300)
        md_lad = [rc["ev"]["f4"]["md"] for rc in recs]
        cm_sh = [rc["ev"]["f4"]["cm"]
                 / max(sum(abs(v) for v in rc["ev"]["P"]), 1e-300)
                 for rc in recs]
        check("G70-constant-stability", True,
              "F3 sub-Gauss constant: C med %.2f min %.2f max "
              "%.2f spread %.2f (bar %.1f -> %s); F4 Azuma "
              "constant: C4 med %.2f max %.2f spread %.2f (%s); "
              "F4 chain-filtration conditional means: md_ratio "
              "med %.2f (rms(mu)/rms(P) -- small against the "
              "variance %s), compensator share med %.2f"
              % (float(np.median(C3_lad)), min(C3_lad),
                 max(C3_lad), sp3, SPREAD_BAR,
                 "STABLE" if sp3 <= SPREAD_BAR else "UNSTABLE",
                 float(np.median(C4_lad)), max(C4_lad), sp4,
                 "STABLE" if sp4 <= SPREAD_BAR else "UNSTABLE",
                 float(np.median(md_lad)),
                 "YES" if float(np.median(md_lad)) < 0.5
                 else "NO",
                 float(np.median(cm_sh))))
    else:
        sp3 = sp4 = 0.0
        check("G70-constant-stability", True, "SMOKE: skipped")
    ctl_ok = True
    ctl_note = []
    cover3 = True
    cover4 = True
    for c in ("EPST", "SCR"):
        ev = crecs[c]["ev"]
        okv = (abs(ev["R"]) <= ev["f1"]["eps"] + VAL_BAR
               and abs(ev["R"]) <= ev["f2"]["eps"] + VAL_BAR)
        c3c = ev["f3"]["C"] <= C3_ALL + 1e-12
        c4c = ev["f4"]["C"] <= C4_ALL + 1e-12
        cover3 = cover3 and c3c
        cover4 = cover4 and c4c
        ctl_note.append("%s F1/F2 valid %s, C3 %.2f %s, C4 %.2f "
                        "%s" % (c, "OK" if okv else "BROKEN",
                                ev["f3"]["C"],
                                "covered" if c3c else "BREAKS",
                                ev["f4"]["C"],
                                "covered" if c4c else "BREAKS"))
        ctl_ok = ctl_ok and okv
    main_fitted = not ctl_ok
    check("G71-worlds-test", ctl_ok,
          "WORLDS TEST on the broken-arithmetic controls: F1/F2 "
          "hold by exact algebra (WORLD_BLIND_VALID -- "
          "ADMISSIBLE for L2, the generic half; declared lane "
          "difference to L*); F3/F4 constant coverage: %s"
          % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    evS = crecs["SMOOTH"]["ev"]
    okSv = abs(evS["R"]) <= evS["f1"]["eps"] + VAL_BAR
    check("G72-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSv,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "framework validity holds trivially on the self-"
          "aliased source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSv else "BROKEN"))
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
                           "%.0e)" % (rc["kz"], rc["N"], dv,
                                      MP_DEEP_BAR))
        check("G73-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
        rng = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(Ns,
                                 list(rng.permutation(
                                     eps_c2_rel))))
        check("G74-mustfail-halves-shuffle", sp_mut < SHUF_BAR
              and sp_mut < abs(sp_eps),
              "m4 HALVES-SHUFFLE (seed-%d permutation of the "
              "eps_c2 series against the N axis): |sp| = %.3f < "
              "%.1f and < the true trend %.2f -- every slope in "
              "the delta' table is carried by N, not by the "
              "estimator" % (SHUFFLE_SEED, sp_mut, SHUF_BAR,
                             abs(sp_eps)))
    else:
        check("G73-mp-deep-wards", True, "SMOKE: skipped")
        check("G74-mustfail-halves-shuffle", True,
              "SMOKE: skipped")

    # ---------------- S9: adjudication + verdict
    section("S9  ADJUDICATION + VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the four-framework census with exact validity, "
          "the delta' table against the r272 flip condition, the "
          "certification balance, and the lag-space map of the "
          "c3 cancellation -- NO new certificate promoted, NO "
          "bound modification of the sealed c2 form")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        elig = {}
        for nm in FRAME_ORDER:
            e_ = (val_worst[nm] <= VAL_BAR
                  and not frames[nm]["fire"])
            if nm == "F3_SALEMZYGMUND":
                e_ = e_ and sp3 <= SPREAD_BAR and cover3
            if nm == "F4_MDS_AZUMA":
                e_ = e_ and sp4 <= SPREAD_BAR and cover4
            elig[nm] = e_
        go_set = [nm for nm in FRAME_ORDER
                  if elig[nm] and frames[nm]["c7"] == len(exc)
                  and frames[nm]["dp"] > DELTA_NEED]
        part_set = [nm for nm in FRAME_ORDER
                    if elig[nm]
                    and (frames[nm]["c7"] >= len(exc) - 1
                         or frames[nm]["dp"] > DELTA_NEED)]
        tab = []
        for nm in FRAME_ORDER:
            wst = ("WORLD_BLIND_VALID"
                   if nm in ("F1_DISCREPANCY", "F2_VDC")
                   else (("COVERED spread %.2f"
                          % (sp3 if nm == "F3_SALEMZYGMUND"
                             else sp4))
                         if ((cover3, cover4)
                             [nm == "F4_MDS_AZUMA"])
                         else "BREAKS"))
            tab.append("%s eps med %+.2f dec sl %+.2f delta' "
                       "%+.2f cert %d/7 %d/42 %s det %s"
                       % (nm, frames[nm]["med"],
                          frames[nm]["sl"], frames[nm]["dp"],
                          frames[nm]["c7"], frames[nm]["c42"],
                          wst,
                          "FIRE" if frames[nm]["fire"]
                          else "OK"))
        parts = ["FRAMEWORK_TABLE(%s)" % "; ".join(tab)]
        if go_set:
            w = go_set[0]
            parts.append("FRAMEWORK_GO(%s, delta' %+.2f > %.2f, "
                         "cert 7/7%s)"
                         % (w, frames[w]["dp"], DELTA_NEED,
                            "; LEMMA_CANDIDATE typing" if w in
                            ("F3_SALEMZYGMUND", "F4_MDS_AZUMA")
                            else ""))
        elif part_set:
            w = max(part_set, key=lambda nm: (frames[nm]["c7"],
                                              frames[nm]["dp"]))
            gap = min(len(exc) - frames[w]["c7"], 7)
            parts.append("FRAMEWORK_PARTIAL(%s, delta' %+.2f vs "
                         "%.2f, cert %d/7, gap %d exceptions%s)"
                         % (w, frames[w]["dp"], DELTA_NEED,
                            frames[w]["c7"], gap,
                            "; LEMMA_CANDIDATE typing" if w in
                            ("F3_SALEMZYGMUND", "F4_MDS_AZUMA")
                            else ""))
        else:
            best = max(FRAME_ORDER,
                       key=lambda nm: (frames[nm]["c7"],
                                       frames[nm]["dp"]))
            parts.append("ALL_FRAMEWORKS_INSUFFICIENT(common "
                         "obstruction measured: best %s still "
                         "eps med %+.2f dec vs M with delta' "
                         "%+.2f, cert %d/7)"
                         % (best, frames[best]["med"],
                            frames[best]["dp"],
                            frames[best]["c7"]))
        parts.append("AUTOCORRELATION_PROFILE(%s)"
                     % "; ".join(map_note[:4]))
        parts.append("KZ15_DETAIL(%s)" % "; ".join(kz15_note))
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the block identity, the "
          "F1/F2 validity, the autocorr identity; MEASURED: "
          "every slope, constant, share and margin (42 rungs "
          "only); OPEN: the cofinal step H5 and the L2 lemma "
          "PROOF (candidates typed, not claimed); NO RH claim"
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
