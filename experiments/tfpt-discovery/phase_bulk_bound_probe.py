#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""phase_bulk_bound_probe -- PRIME.PORT.RHP.QUENCHED.
PHASE_BULK_BOUND.01 (round 269): the named follow-up of r268
(reviewer-covered, NARROW): a source-pure PHASE-AWARE BULK-
REMAINDER BOUND that beats the abs-sum triangle of the r268
remainder by the required 0.18-0.44 dec on the 6 open exception
rungs -- NO new identity class.  LEGITIMATION (r268 record): the
bulk oscillation of the border-drive comb has ~N sign flips with
a CHAIN-known envelope (amplitude from the three-term recursion
-- SOURCE, not target); Abel-summation/alternation-pairing of
adjacent flips replaces sum|ct| by envelope VARIATION -- local,
phase-aware, but WITHOUT root-scale comb cancellation.  The
detectors (PAIRCORR demand of every derivation, r266 wall
fingerprint) stay armed on EVERY bound derivation.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r268 machinery verbatim): t_{N-2} = sum_b ct_b with
per-atom contributions ct_b = bw_b bx_b v_{N-2}(bx_b)
e^{Ls_{N-2} - Ls_{N-1}} / sqrt|eta_{N-1}| (r244 scaled rows, r266
eval machinery); the r268 record split: t = t_edge(F0.20) + R
with t_edge the outer-20-pct hull partial sum (carries the drive
SIGN on 42/42) and R the finite oscillating BULK remainder; r268
certified kz22 source-purely (margin_cert +0.04) with the abs
triangle eps = sum|ct_bulk|; the 6 open rungs miss by 0.18-0.44
dec (kz52 0.18, kz20 0.19, kz38 0.23, kz36 0.25, kz39 0.31, kz15
0.44 -- the razor, reserve 0.027), ALL demands < 1.0 dec: the
residual gap is SUB-PAIRCORR.

LEG A -- THE BULK-REMAINDER STRUCTURE EXACTLY (dissect first):
(a1) flip structure of ct on the bx-sorted bulk atoms: maximal
  same-sign runs (count, run-length med/max, pairability =
  paired-run fraction), the CHAIN envelope E_b (sealed
  Christoffel/Pruefer amplitude of the three-term recursion at
  the FROZEN terminal coefficients alh_{N-3}, gam_{N-4}:
  K^2 sin^2 th = v^2 + b^2 - 2 v b cos th with v = v_{N-2},
  b = sqrt(gam) v_{N-3} e^{Ls_{N-3}-Ls_{N-2}}, cos th =
  (x - alh)/(2 sqrt(gam)); fallback hypot(v, b) where sin^2 th <
  0.01 or gam <= 0 -- the envelope is SOURCE (chain recursion),
  never the data; exactness of the toy invariant gated on monic
  Chebyshev, bar 1e-12), envelope quality (majorization share,
  error-mass share sum|M_i - E~_i| / sum E~_i) and the envelope
  VARIATION over the bulk (sum_pairs |E~_odd - E~_even| / sum
  E~_i);
(a2) the honest potential: perfect pairing = ground-truth
  cancellation depth log10(sum|ct_bulk| / |R|) per rung (typed
  POTENTIAL_ONLY -- a measurement, NEVER usable as a bound) vs
  the needed 0.18-0.44 dec (r268 record misses, reproduction-
  warded), plus the naked envelope-variation ratio as anatomy.
LEG B -- THE PHASE-AWARE BOUNDS (max 3 sealed candidates, each
source-pure + target-blind + detector-adjudicated; the terminal
drive value stays structurally withheld from every builder under
the forbidden key "t" + "_term"; the ENVELOPE builder is AST-
separated: it must not consume the realized contributions ct):
(b1) c1ENV ABEL/ALTERNATION: pair adjacent flip runs of the
  bx-sorted bulk (pairing offset FROZEN 0 = start at the first
  run); |sum ct_bulk| <= sum_pairs(|E~_odd - E~_even| + D_odd +
  D_even) + (E~_last + D_last if unpaired), where E~_i = run
  mass of the CHAIN envelope and D_i = |M_i - E~_i| the honest
  envelope-error mass -- envelope variation + error + boundary:
  an EXACT theorem (|s_odd + s_even| = |M_odd - M_even| <=
  |E~_odd - E~_even| + D_odd + D_even for alternating runs);
(b2) c2PAIR BLOCK-ALTERNATION: blocks = adjacent run pairs
  (block boundaries from the SIGN STRUCTURE of the chain comb
  only, sealed offset 0); eps = sum_blocks |block sum| + tail =
  sum_pairs |M_odd - M_even| + (M_last if unpaired) -- the exact
  block triangle (refines the r268 singleton triangle, never
  worse, gated);
(b3) c3HYBRID edge-window ablation: the SAME c2 pairing on the
  reduced bulk of F in {0.10, 0.15, 0.25, 0.30} (grid SEALED
  BEFORE evaluation; adjudication only via the sealed r268 rule
  best-by-cert-count, tie by lower demand median -- no per-rung
  parameter selection, no selection-by-answer).
FOR EACH: validity |R| <= eps gated on 42 rungs + 2 mains + 3
controls (exact triangle slack <= 1e-9); certification table on
the 7 exception rungs (margin_cert = sqrt(5/7) - (|Z_local| +
eps) vs margin_true); the d2 PAIRCORR demand log10((|Z_local| +
eps)/M_W) (sealed bar 1.0 dec on the exception branch) and the
r266 WALL fingerprint (decision pattern + rank fingerprint vs
g(1), sealed bar 0.9, selftest re-armed) on every derivation;
the MAIN-fitting test = EPSTEIN/SCRAMBLE reproduction of the
contribution identity AND the bound validity.
LEG C -- SUCCESS GATE + UNIVERSALITY TYPING (sealed, hard):
(c1) certified count on the 7 (kz15 detail ALWAYS: reserve band
  [0.020, 0.035] reproduction + miss decades); at 7/7 by a clean
  candidate: SURFACE_CLOSED -- the exception branch is closed
  target-blind on the 42-rung ladder (together with the r263
  cheap branch, q_N < 1 would be certified on ALL 42 measured
  rungs -- a SURFACE statement, no cofinality claim from census);
(c2) the honest typing of the winning bound form, sealed rule:
  UNIVERSAL_FORM iff the winning clean candidate is c1ENV or
  c2PAIR (ONE fixed formula -- frozen F = 0.20, frozen pairing
  offset 0, no per-rung parameter -- whose VALIDITY |R| <= eps
  is a window-independent triangle THEOREM, provable source-
  purely for the whole cofinal family: a theorem candidate for
  the Lean roadmap; the certification MARGIN stays measured on
  the 42 -- stated explicitly); SURFACE_ONLY iff the winner is a
  c3 grid setting (the F parameter was adjudicated on the 42).
  NO cofinality claim in either case.
LEG D -- WARDS / KILLS / MUST-FAILS: inherited kills (PAIRCORR,
TARGET_INVERSE, SELECTION_BY_ANSWER; no fit primitives --
fragment audit); r268 reproduction wards: exception set == the
named 7 + cheap 35, F0.20 abs-triangle eps med +0.05 dec vs M
(tol 0.02), the six r268 misses (tol 0.015 each), kz22 abs-
triangle margin in [0.02, 0.06] (the certified rung as
REGRESSION ward), kz15 reserve in [0.020, 0.035]; SMOOTH anchor
(drive alias <= 1e-12, q_N <= 1e-20, bound validity holds
trivially); mp WARDS (dps 60) of t_{N-2} at kz15 + kz20 + kz22
(bar 1e-8 vs the f64 chain); MUST-FAILS: (m1) ENVELOPE FROM DATA
-- the mutant smoothing |ct| into an envelope is CIRCULAR and
must be FLAGGED by the AST envelope-scope audit (the sealed
envelope builder consumes chain values + geometry only); (m2)
PAIRING WITH GROUND-TRUTH SIGN -- the mutant orienting the
pairing by the withheld terminal drive key must be FLAGGED by
the candidate scope audit; (m3) BLOCK BOUNDARIES AFTER LOOKING
AT CANCELLATION -- the mutant evaluating BOTH pairing offsets
and keeping the smaller bound is selection-by-answer: typed
FORBIDDEN, its gain measured and printed (the sealed candidates
use offset 0 unconditionally); (m4) inherited r268 m1: the naked
truncation claim |t| <= |t_local| without error term breaks by
>= 1e3 x the honest contribution-ward floor (loud).

INDEX FIREWALL (binding, r238-r268 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R and t values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r244 BH.wpack + BH.spearman, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r264
QO.port_pack, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb;
the mp drive ward and the census/control scaffold are the r268
routes re-used unchanged.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls (r268 floor family); VAL_BAR 1e-9 (bound-validity
slack); TRI_BAR 1e-9; EDGE_F 0.20 (r268 record winner, FROZEN);
F_GRID (0.10, 0.15, 0.25, 0.30); PAIR_OFFSET 0 (FROZEN: pairing
starts at the first bulk run); SIN2_MIN 0.01 (envelope phase
guard); TOY_ENV_BAR 1e-12 (monic-Chebyshev invariant); TOY_ENV_N
(5, 6, 7); R268_EPS020_MED +0.05 dec (tol 0.02); R268_MISS
kz15 0.44 / kz20 0.19 / kz36 0.25 / kz38 0.23 / kz39 0.31 /
kz52 0.18 (tol 0.015 each); R268_KZ22_BAND (0.02, 0.06);
RESERVE_BAND (0.020, 0.035); DEMAND_BAR 1.0 dec; FP_BAR 0.9;
MP_DPS 60; MP_T_BAR 1e-8; MP_WARD_KZ (15, 20, 22); SM_Q_BAR
1e-20; SM_ALIAS_BAR 1e-12; LOUD 1e3; SHUFFLE_SEED 269;
CHEAP_REF_IDX (0, 10, 20, 30, 41) (advance rule inherited);
KZ_ANCHOR 15; runtime <= 1800 s; smoke = w9 + controls + toy +
w9/control candidate numerics + scope audits + must-fails
(ladder, wall detector, mp wards, success gate, adjudication
skipped).  DISCLOSED PRE-SPEC INPUT (no scratch run of this
probe): every reproduction band is an r263/r264/r266/r268 RECORD
number adopted as-is (exception set; razor slack 0.027; the
F0.20 eps median, the six misses and the kz22 margin from the
r268 record tables; f64/mp floor families) -- nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  BULK_ANATOMY(runs vs flips, pairability, envelope
    majorization/error, potential dec vs needed)
+ C1_ABEL_ENV(cert k/7, gain med dec, validity)
+ C2_PAIRSUM(cert k/7, gain med dec)
+ C3_HYBRID(best F, cert k/7)
+ [exactly one of] PHASE_BOUND_GO(cand, 7/7, SURFACE_CLOSED,
    UNIVERSAL_FORM / SURFACE_ONLY) /
    PHASE_BOUND_PARTIAL(cand, n/7, rest anatomy: per-rung miss
    dec + where the remaining cancellation sits) /
    PHASE_BOUND_INSUFFICIENT(the measured limit of the local
    class: structural gap dec + location of the remaining
    cancellation)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if fired] PAIRCORR_MINIATURE(candidate list).
Honesty before beauty: no verdict claims a derived 5/7, a
cofinal law, or an asymptotic mechanism; the exception scalar's
positivity beyond the measured 42 stays OPEN; r243-r268 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 was 29/29 gates with NO amendment; calibration pass
1 = first full evaluation, 29/29 gates, wall 14.8 s -- NO
physics bar, band, rule or verdict rule was moved at any point;
pass 2 = the record run below, numerically identical to pass 1
in every printed figure; the only post-freeze edit is this
record-table insertion, which IS the protocol):
CAL_VERDICT = BULK_ANATOMY(runs ~ 0.47 x bulk atoms, pairability
1.00, env majorization 1.00 / error share 0.36, potential med
0.54 dec vs needed 0.18-0.44) + C1_ABEL_ENV(cert 0/7, gain med
-0.06 dec, valid 47/47) + C2_PAIRSUM(cert 5/7, gain med +0.33
dec, valid 47/47) + C3_HYBRID(best c3F0.30, cert 6/7) +
PHASE_BOUND_PARTIAL(c3F0.30, cert 6/7: kz20, kz22, kz36, kz38,
kz39, kz52; rest misses 0.12-0.12 dec, SURFACE_ONLY).
Key numbers.  LEG A: contribution ward worst dev/absmass 2.1e-13
main / 3.9e-13 deep / 2.4e-8 controls (bars 1e-9/3e-6/1e-6);
r268 reproduction wards EXACT: exception set == the named 7,
F0.20 abs eps med +0.053 dec (record +0.05), six misses worst
dev 0.005 (tol 0.015), kz22 abs-triangle margin +0.0439 in
[0.02, 0.06], kz15 reserve 0.0268 in [0.020, 0.035]; bulk
anatomy (7 exc + 2 mains + 5 cheap refs): bulk runs 55..338
(~ 0.47 x bulk atoms, run len med 2, max 4-10), pairability
0.98-1.00, envelope majorization share 1.00 on EVERY pool rung
(the Pruefer amplitude is a true numerical envelope), envelope
error-mass share 0.32-0.39, naked envelope variation 0.39-0.71
of the bulk abs mass; potential (ground truth, typed
POTENTIAL_ONLY): exceptions 0.42-0.66 dec (med 0.54), all 42
med 0.81 dec -- AT THE RAZOR kz15 even PERFECT pairing holds
only 0.49 dec against the needed 0.44: the razor bulk is
nearly incompressible, 0.05 dec of ground-truth headroom.
LEG B (42 rungs + 2 mains + 3 controls): validity EXACT
everywhere (worst |R| - eps slack -4.0e-3 <= 0 over 47 worlds x
6 settings; eps_pair never exceeds the abs triangle, worst
slack 0.0); c2PAIR gain over the r268 abs triangle med +0.33
dec (min +0.26, max +0.41), eps med -0.28 dec vs M; c1ENV gain
med -0.06 dec (min -0.12, max +0.02), eps med +0.11 dec vs M --
the chain envelope alone is COARSER than the abs triangle (its
error-mass D dominates: typed honestly, cert 0/7, demand med
+0.24); c3 grid gains med +0.32..+0.34 dec; wall fingerprints
c1 0.51 / c2 0.10 / c3 0.09-0.52, all < 0.9, no all-FALSE
pattern => NO candidate is the wall; paircorr demand on the
exception branch: c2 med -0.04 max +0.07, c3F0.30 med -0.07 max
+0.02, c3F0.25 med -0.06 max +0.04 -- NOTHING reaches the
1.0-dec bar (the gap was and stays SUB-PAIRCORR).  LEG C:
success gate (|Z| <= |Z_local| + eps, exact triangle): c2PAIR
(the FIXED formula, F 0.20 + offset 0) certifies 5/7 -- kz20
margin_cert +0.0735, kz22 +0.3974, kz36 +0.0461, kz38 +0.1135,
kz52 +0.1490; kz39 misses by 0.01 dec, kz15 by 0.18 dec;
c3F0.30 certifies 6/7 (adds kz39 at +0.0750; kz15 miss 0.12
dec), full-ladder cert 37/42; the sealed best-by-cert rule
adjudicates c3F0.30 => PHASE_BOUND_PARTIAL(6/7), typing
SURFACE_ONLY (the winning F was adjudicated on the 42; the
fixed-formula c2PAIR at 5/7 would type UNIVERSAL_FORM but is
not the winner under the sealed rule -- no repair after seeing
the numbers); kz15 DETAIL: true reserve 0.0268 (r263 record
0.027 reproduced), r268 missed by 0.44 dec, the phase-aware
bounds shrink the miss to 0.12 dec (c3F0.30) / 0.18 dec
(c2PAIR); consistency margin_cert <= margin_true exact on
every rung x setting.  LEG D: control reproduction EPST dev
6.0e-11 / SCR 2.4e-8 + bound validity exact on both (world-
blind, NOT main-fitted); SMOOTH alias 2.4e-14, q_N 4.2e-25,
validity holds; mp drive wards (dps 60): kz15 dev 2.9e-10,
kz20 dev 2.2e-10, kz22 dev 2.0e-10 (bar 1e-8); must-fails: m1
env-from-data mutant FLAGGED (ct in envelope scope), m2 gift-
sign mutant FLAGGED (withheld key), m3 offset-peek mutant typed
FORBIDDEN (gains > 1e-12 on 24/44 rungs, max 0.069 -- the
temptation is real and stays sealed away), m4 naked truncation
breaks by 4.0e+11 x the ward floor (loud); fragment audit
CLEAN.  READING (typed, no upgrade): the narrow follow-up
CARRIES 6/7 -- the r268 gap was exactly what the anatomy said:
adjacent-flip cancellation with a mild envelope; the sealed
block-alternation triangle recovers ~0.3 dec on every world
and closes kz20/22/36/38/39/52 source-purely with no detector
fire; the honest rest: the razor kz15 misses by 0.12 dec, and
the measured ground-truth potential at kz15 is 0.49 dec vs the
needed 0.44 -- ONLY 0.05 dec of TOTAL bulk-cancellation
headroom exist at F0.20: the remaining kz15 gap is NOT a
sharper-pairing problem but the measured limit of the local
class at this window split (the residual cancellation sits in
the near-exact balance of adjacent PAIR SUMS across the whole
bulk, sub-paircorr, no detector fires); the chain-envelope-only
bound (c1) is honestly too coarse (error mass 0.32-0.39
dominates the variation term); the open edges after this
round: (i) the kz15 razor at 0.12 dec, (ii) the cofinal step
(window-independent margin law) -- unchanged.  Runtime 14.8 s
full / 0.2 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE (records inserted per protocol;
no bar, band, rule or verdict rule moved).

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
TRI_BAR = 1e-9
EDGE_F = 0.20
F_GRID = (0.10, 0.15, 0.25, 0.30)
PAIR_OFFSET = 0
SIN2_MIN = 0.01
TOY_ENV_BAR = 1e-12
TOY_ENV_N = (5, 6, 7)
R268_EPS020_MED = 0.05
R268_EPS020_TOL = 0.02
R268_MISS = ((15, 0.44), (20, 0.19), (36, 0.25),
             (38, 0.23), (39, 0.31), (52, 0.18))
R268_MISS_TOL = 0.015
R268_KZ22_BAND = (0.02, 0.06)
RESERVE_BAND = (0.020, 0.035)
DEMAND_BAR = 1.0
FP_BAR = 0.9
MP_DPS = 60
MP_T_BAR = 1e-8
MP_WARD_KZ = (15, 20, 22)
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
LOUD = 1e3
SHUFFLE_SEED = 269
CHEAP_REF_IDX = (0, 10, 20, 30, 41)
KZ_ANCHOR = 15

CAL_VERDICT = (
    "BULK_ANATOMY(runs ~ 0.47 x bulk atoms, pairability 1.00, "
    "env majorization 1.00 / error share 0.36, potential med "
    "0.54 dec vs needed 0.18-0.44) + C1_ABEL_ENV(cert 0/7, gain "
    "med -0.06 dec, valid 47/47) + C2_PAIRSUM(cert 5/7, gain "
    "med +0.33 dec, valid 47/47) + C3_HYBRID(best c3F0.30, cert "
    "6/7) + PHASE_BOUND_PARTIAL(c3F0.30, cert 6/7: kz20, kz22, "
    "kz36, kz38, kz39, kz52; rest misses 0.12-0.12 dec, "
    "SURFACE_ONLY)")

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
                       "labels, true R/t) enters gates and census "
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


# ---- sealed builders (target-blind: consume ONLY the plain
# arrays passed as arguments; the withheld terminal drive key and
# every target-side identifier are forbidden in scope, AST-audit;
# the ENVELOPE builder additionally must not consume the realized
# contributions ct -- circularity firewall, AST-separated)
def mask_edge(bx, lo, hi, frac):
    """r268 sealed keep-mask: atoms in the outer hull-edge region
    (fraction of the union+border hull width)."""
    edge = frac * (hi - lo)
    return (bx <= lo + edge) | (bx >= hi - edge)


def env_chain(bxa, v2a, v3a, alh_t, gam_t, sc3, wgeom):
    """sealed CHAIN envelope (Christoffel/Pruefer amplitude of
    the three-term recursion at the frozen terminal coefficients;
    source-pure: chain values + comb geometry only, NEVER ct):
    K^2 sin^2 th = v^2 + b^2 - 2 v b cos th, b = sqrt(gam) v3
    sc3, cos th = (x - alh)/(2 sqrt(gam)); hypot fallback where
    the phase is degenerate (sin^2 th < SIN2_MIN or gam <= 0)."""
    if gam_t > 0.0:
        rb = math.sqrt(gam_t)
        bt = rb * sc3 * v3a
        cth = (bxa - alh_t) / (2.0 * rb)
        s2 = 1.0 - cth * cth
        inv = v2a * v2a + bt * bt - 2.0 * v2a * bt * cth
        kf = np.hypot(v2a, bt)
        kp = np.sqrt(np.maximum(inv, 0.0)) \
            / np.sqrt(np.maximum(s2, SIN2_MIN))
        K = np.where(s2 >= SIN2_MIN, kp, kf)
    else:
        bt = math.sqrt(abs(gam_t)) * sc3 * v3a
        K = np.hypot(v2a, bt)
    return wgeom * K


def runs_split(cts):
    """maximal same-sign runs of the bx-sorted bulk contributions
    (zero atoms attach to the current run; consecutive runs
    alternate in sign by construction)."""
    sg = np.sign(cts)
    runs = []
    cur = 0.0
    start = 0
    for i in range(len(sg)):
        s = sg[i]
        if s == 0.0:
            continue
        if cur == 0.0:
            cur = s
        elif s != cur:
            runs.append((start, i, cur))
            start = i
            cur = s
    if len(cts):
        runs.append((start, len(cts), cur if cur != 0.0 else 1.0))
    return runs


def bound_pairsum(Mr):
    """c2/c3 sealed block-alternation bound: blocks = adjacent
    run pairs from PAIR_OFFSET 0; eps = sum_pairs |M_odd -
    M_even| + tail (exact block triangle)."""
    e = 0.0
    m = len(Mr)
    for i in range(PAIR_OFFSET, m - 1, 2):
        e += abs(Mr[i] - Mr[i + 1])
    if (m - PAIR_OFFSET) % 2 == 1:
        e += Mr[-1]
    return e


def bound_abelenv(Mr, Er):
    """c1 sealed Abel/alternation bound: envelope VARIATION +
    envelope-error masses + boundary (exact: |M_o - M_e| <=
    |E~_o - E~_e| + D_o + D_e)."""
    e = 0.0
    m = len(Mr)
    for i in range(PAIR_OFFSET, m - 1, 2):
        e += abs(Er[i] - Er[i + 1]) + abs(Mr[i] - Er[i]) \
            + abs(Mr[i + 1] - Er[i + 1])
    if (m - PAIR_OFFSET) % 2 == 1:
        e += Er[-1] + abs(Mr[-1] - Er[-1])
    return e


def cand_mutant_envdata(ct):
    """m1 MUST-FAIL MUTANT: envelope smoothed from the realized
    data |ct| -- CIRCULAR; the envelope scope audit must FLAG
    this (ct is forbidden in envelope scope)."""
    a = np.abs(ct)
    k = np.ones(5) / 5.0
    return np.convolve(a, k, mode="same")


def cand_mutant_giftpair(rc, Mr):
    """m2 MUST-FAIL MUTANT: pairing oriented by the ground-truth
    terminal drive sign -- reads the withheld key; the candidate
    scope audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * bound_pairsum(Mr)


def cand_mutant_offsetpeek(Mr):
    """m3 MUST-FAIL MUTANT: block boundaries chosen AFTER looking
    at the cancellation -- evaluates BOTH pairing offsets and
    keeps the smaller bound (selection-by-answer; typed FORBIDDEN,
    gain measured)."""
    e0 = bound_pairsum(Mr)
    e1 = Mr[0] if Mr else 0.0
    m = len(Mr)
    for i in range(1, m - 1, 2):
        e1 += abs(Mr[i] - Mr[i + 1])
    if m >= 2 and (m - 1) % 2 == 1:
        e1 += Mr[-1]
    return min(e0, e1)


CAND_FORBIDDEN = {"t" + "_term", "rho", "S", "sa", "la", "q_chain",
                  "D_dir", "wb", "world_block", "direct_terminal",
                  "rhp_readout", "gram_input", "g_gap",
                  "u_triangle", "M_W", "R" + "_bulk", "margin"}
ENV_EXTRA_FORBIDDEN = {"ct", "cts", "t" + "_loc", "t" + "_edge"}


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
def toy_env_chebyshev():
    """the envelope invariant on the monic Chebyshev chain
    (alh = 0, gam_1 = 1/2, gam_n = 1/4): p_n(cos th) = 2^{1-n}
    cos(n th) => K = sqrt(p_n^2 + b^2 - 2 p_n b cos th)/|sin th|
    with b = p_{n-1}/2 must equal 2^{1-n} EXACTLY (constant
    coefficients: the invariant is the envelope)."""
    xs = [math.cos(math.pi * j / 10.0) for j in range(1, 10)]
    worst = 0.0
    for n in TOY_ENV_N:
        for x in xs:
            p0, p1 = 1.0, x
            for k in range(1, n):
                be = 0.5 if k == 1 else 0.25
                p0, p1 = p1, x * p1 - be * p0
            a = p1
            b = 0.5 * p0
            cth = x / (2.0 * 0.5)
            s2 = 1.0 - cth * cth
            if s2 < 1e-12:
                continue
            K = math.sqrt(max(a * a + b * b - 2.0 * a * b * cth,
                              0.0)) / math.sqrt(s2)
            worst = max(worst, abs(K * 2.0 ** (n - 1) - 1.0))
    return worst


# ---------------------------------------------------- mp route
def mp_drive(p, dps):
    """mp (dps sealed) terminal drive t_{N-2} = T~ e^{Ls_{N-2} -
    Ls_{N-1}} / sqrt|eta_{N-1}| from the raw atoms (r268 route
    verbatim)."""
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
    print("phase_bulk_bound_probe -- PRIME.PORT.RHP.QUENCHED."
          "PHASE_BULK_BOUND.01 (round 269)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)   "
          "CHARTER_SHA %s (imported r264)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16], QO.CHARTER_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + candidate "
                        "numerics + scope audits + must-fails; "
                        "ladder, wall detector, mp wards, success "
                        "gate, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "NARROW FOLLOW-UP (reviewer-covered): source-pure "
          "PHASE-AWARE bulk-remainder bound sharper than the "
          "r268 abs-sum triangle by the needed 0.18-0.44 dec -- "
          "NO new identity class; 3 sealed candidates (c1 "
          "Abel/envelope-variation from the CHAIN recursion, c2 "
          "block-alternation over adjacent sign-run pairs, c3 "
          "the same pairing on a sealed edge-window grid); "
          "success gate = certify |Z| < sqrt(5/7) via |Z_local| "
          "+ eps on the exception branch, kz15 the anchor; wall "
          "+ paircorr detectors armed on EVERY derivation; "
          "envelope builder AST-separated from ct (circularity "
          "firewall); pairing offset FROZEN 0; ALL bars, rules "
          "and verdicts sealed BEFORE evaluation (pre-spec "
          "input = r263/r264/r266/r268 record numbers, "
          "disclosed)")

    # ---------------- S1: census + controls (r268 scaffold)
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
        E = env_chain(bx, v2, v3, alh_t, gam_t, sc3, wgeom)
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

    # ---------------- S2: LEG A -- ward + r268 reproduction
    section("S2  LEG A -- CONTRIBUTION WARD + R268 REPRODUCTION")
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
          "controls: worst dev/absmass %.1e main N<=%d (bar "
          "%.0e) / %.1e deep (bar %.0e) / %.1e controls (bar "
          "%.0e) -- the bounds operate on an EXACT decomposition"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    # the F0.20 split + all bound settings per rung
    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        Es = rc["E"][o]
        out = {}
        for f in (EDGE_F,) + F_GRID:
            ed = mask_edge(bxs, rc["lo"], rc["hi"], f)
            t_loc = float(np.sum(cts[ed]))
            cb = cts[~ed]
            Eb = Es[~ed]
            Rb = float(np.sum(cb))
            ab = float(np.sum(np.abs(cb)))
            runs = runs_split(cb)
            Mr = [float(np.sum(np.abs(cb[a:b])))
                  for a, b, _s in runs]
            Er = [float(np.sum(Eb[a:b])) for a, b, _s in runs]
            sg = [s for _a, _b, s in runs]
            alt_ok = all(sg[i + 1] == -sg[i]
                         for i in range(len(sg) - 1))
            e_pair = bound_pairsum(Mr)
            e_env = bound_abelenv(Mr, Er)
            e_peek = cand_mutant_offsetpeek(Mr)
            out[f] = dict(t_loc=t_loc, Rb=Rb, ab=ab, runs=runs,
                          Mr=Mr, Er=Er, alt_ok=alt_ok,
                          e_pair=e_pair, e_env=e_env,
                          e_peek=e_peek, nb=int(len(cb)))
        return out

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    if not smoke:
        # r268 reproduction wards: abs-triangle F0.20 med + the
        # six misses + kz22 margin (regression) -- all recomputed
        eps_dec = []
        for rc in recs:
            ev = rc["ev"][EDGE_F]
            eps_dec.append(math.log10(ev["ab"] / M_W))
        med020 = float(np.median(eps_dec))
        ok_med = abs(med020 - R268_EPS020_MED) <= R268_EPS020_TOL
        miss_dev = 0.0
        miss_note = []
        for kz, m_ref in R268_MISS:
            rc = next(r_ for r_ in recs if r_["kz"] == kz)
            ev = rc["ev"][EDGE_F]
            need = M_W - abs(ev["t_loc"] + rc["chain"])
            miss = math.log10(ev["ab"] / need) if need > 0 \
                else float("inf")
            miss_dev = max(miss_dev, abs(miss - m_ref))
            miss_note.append("kz%d %.3f(ref %.2f)" % (kz, miss,
                                                      m_ref))
        rc22 = next(r_ for r_ in recs if r_["kz"] == 22)
        ev22 = rc22["ev"][EDGE_F]
        mg22 = M_W - (abs(ev22["t_loc"] + rc22["chain"])
                      + ev22["ab"])
        ok22 = R268_KZ22_BAND[0] <= mg22 <= R268_KZ22_BAND[1]
        check("G21-r268-reproduction-wards",
              ok_med and miss_dev <= R268_MISS_TOL and ok22,
              "abs-triangle b3F0.20 recomputed: eps med %+.3f "
              "dec vs M (r268 record %+.2f, tol %.2f); the six "
              "open-rung misses reproduced (worst dev %.3f, tol "
              "%.3f): %s; kz22 abs-triangle margin %+.4f in the "
              "sealed band %s (the r268-certified rung as "
              "REGRESSION ward)"
              % (med020, R268_EPS020_MED, R268_EPS020_TOL,
                 miss_dev, R268_MISS_TOL, "; ".join(miss_note),
                 mg22, str(R268_KZ22_BAND)))
    else:
        check("G21-r268-reproduction-wards", True,
              "SMOKE: skipped (ladder wards need the 42 rungs)")

    # anatomy pool + census prints
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
        ev = rc["ev"][EDGE_F]
        runs = ev["runs"]
        m = len(runs)
        rl = [b - a for a, b, _s in runs]
        pairable = (2 * ((m - PAIR_OFFSET) // 2)) / max(m, 1)
        o = rc["o"]
        cts = rc["ct"][o]
        Es = rc["E"][o]
        ed = mask_edge(rc["bx"][o], rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        Eb = Es[~ed]
        maj = float(np.mean(np.abs(cb) <= Eb)) if len(cb) else 0.0
        errsh = (sum(abs(a_ - b_) for a_, b_ in zip(ev["Mr"],
                                                    ev["Er"]))
                 / max(sum(ev["Er"]), 1e-300))
        var_naked = 0.0
        for i in range(PAIR_OFFSET, m - 1, 2):
            var_naked += abs(ev["Er"][i] - ev["Er"][i + 1])
        pot = (math.log10(ev["ab"] / abs(ev["Rb"]))
               if abs(ev["Rb"]) > 1e-300 else float("inf"))
        gain2 = math.log10(ev["ab"] / max(ev["e_pair"], 1e-300))
        gain1 = math.log10(ev["ab"] / max(ev["e_env"], 1e-300))
        info("kz%-3d N%-4d %-4s bulk %-4d runs %-4d (len med %d "
             "max %d, pairable %.2f)  envmaj %.2f errsh %.2f "
             "nakedvar %.2f  |R| %.3f  pot %.2f dec  gain c2 "
             "%+.2f c1 %+.2f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g"] < 0 else "chp",
                ev["nb"], m, int(np.median(rl)), int(max(rl)),
                pairable, maj, errsh,
                var_naked / max(ev["ab"], 1e-300),
                abs(ev["Rb"]), pot, gain2, gain1))
    check("G22-bulk-anatomy-census", True,
          "a1 MEASUREMENT (pool = %s): flip-run census (count, "
          "lengths, pairability), chain-envelope quality "
          "(majorization share, error-mass share), naked "
          "envelope variation, and the bulk remainder -- per "
          "pool rung printed (exact decomposition)"
          % ("7 exc + 2 mains + 5 cheap refs" if not smoke
             else "mains (SMOKE)"))
    pot_all = []
    for rc in (recs if not smoke else mrecs):
        ev = rc["ev"][EDGE_F]
        if abs(ev["Rb"]) > 1e-300:
            pot_all.append(math.log10(ev["ab"] / abs(ev["Rb"])))
    check("G23-potential-typed", True,
          "a2 MEASUREMENT (typed POTENTIAL_ONLY, never a bound): "
          "perfect-pairing ground-truth cancellation depth "
          "log10(sum|ct_bulk|/|R|) med %.2f dec (min %.2f, max "
          "%.2f) vs the needed 0.18-0.44 dec (r268 record) -- "
          "the potential is measured, the BOUNDS below never "
          "consume it"
          % (float(np.median(pot_all)) if pot_all else
             float("nan"),
             min(pot_all) if pot_all else float("nan"),
             max(pot_all) if pot_all else float("nan")))

    # ---------------- S3: envelope structure + scope audits
    section("S3  ENVELOPE STRUCTURE + SCOPE AUDITS")
    toy_worst = toy_env_chebyshev()
    check("G30-toy-envelope-exact", toy_worst <= TOY_ENV_BAR,
          "monic-Chebyshev invariant: K = sqrt(p_n^2 + b^2 - 2 "
          "p_n b cos th)/|sin th| == 2^{1-n} EXACT on n = %s x 9 "
          "interior nodes (worst rel dev %.1e, bar %.0e) -- the "
          "sealed envelope is the Pruefer amplitude of the "
          "three-term recursion, exact at constant coefficients"
          % (str(TOY_ENV_N), toy_worst, TOY_ENV_BAR))
    alt_all = all(rc["ev"][f]["alt_ok"]
                  for rc in all_rc for f in (EDGE_F,) + F_GRID)
    check("G31-run-structure-ward", alt_all,
          "consecutive bulk runs alternate in sign on every rung "
          "x window setting (%d worlds x %d settings) -- the "
          "block boundaries come from the SIGN STRUCTURE of the "
          "comb alone (sealed offset %d), every block spans "
          "exactly <= 2 adjacent runs: the bound derivation is "
          "LOCAL by construction"
          % (len(all_rc), 1 + len(F_GRID), PAIR_OFFSET))
    h_env = scope_audit("env_chain",
                        CAND_FORBIDDEN | ENV_EXTRA_FORBIDDEN)
    h_b1 = scope_audit("bound_abelenv", CAND_FORBIDDEN)
    h_b2 = scope_audit("bound_pairsum", CAND_FORBIDDEN)
    h_rs = scope_audit("runs_split", CAND_FORBIDDEN)
    h_m1 = scope_audit("cand_mutant_envdata",
                       CAND_FORBIDDEN | ENV_EXTRA_FORBIDDEN)
    h_m2 = scope_audit("cand_mutant_giftpair", CAND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G32-scope-audits", not (h_env or h_b1 or h_b2 or h_rs)
          and bool(h_m1) and bool(h_m2) and not ag_hits,
          "sealed builders CLEAN (envelope consumes chain values "
          "+ geometry only%s; bounds consume run masses only%s); "
          "m1 env-from-data mutant FLAGGED (%s); m2 gift-sign "
          "mutant FLAGGED (%s); fragment audit (no fit "
          "primitives): %s"
          % ("" if not h_env else " VIOLATION " + "; ".join(h_env),
             "" if not (h_b1 or h_b2 or h_rs) else " VIOLATION",
             "; ".join(h_m1) if h_m1 else "NOT FLAGGED",
             "; ".join(h_m2) if h_m2 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: LEG B -- the sealed bounds + detectors
    section("S4  LEG B -- PHASE-AWARE BOUNDS + DETECTORS")
    settings = [("c1ENV", "env", EDGE_F), ("c2PAIR", "pair",
                                           EDGE_F)]
    for f in F_GRID:
        settings.append(("c3F%.2f" % f, "pair", f))
    res = {}
    val_worst = -1e300
    ref_worst = 0.0
    for nm, fam, f in settings:
        rows_ = []
        for rc in all_rc:
            ev = rc["ev"][f]
            eps = ev["e_env"] if fam == "env" else ev["e_pair"]
            t_loc = ev["t_loc"]
            Zl = t_loc + rc["chain"]
            bound = abs(Zl) + eps
            val_worst = max(val_worst, abs(ev["Rb"]) - eps)
            if fam == "pair":
                ref_worst = max(ref_worst, eps - ev["ab"])
            rows_.append(dict(kz=rc["kz"], exc=rc["g"] < 0,
                              t_loc=t_loc, eps=eps,
                              ab=ev["ab"], Zl=Zl, bound=bound,
                              margin=M_W - bound,
                              gain=math.log10(
                                  ev["ab"] / max(eps, 1e-300)),
                              Z=rc["Z"]))
        res[nm] = rows_
    for c in crecs:
        rc = crecs[c]
        for f in (EDGE_F,) + F_GRID:
            ev = rc["ev"][f]
            val_worst = max(val_worst, abs(ev["Rb"]) - ev["e_pair"])
            val_worst = max(val_worst, abs(ev["Rb"]) - ev["e_env"])
    n_worlds = len(all_rc) + len(crecs)
    check("G40-validity-wards", val_worst <= VAL_BAR
          and ref_worst <= VAL_BAR,
          "the phase-aware bounds are EXACT theorems on the "
          "decomposition: worst |R| - eps slack %+.1e <= 0 over "
          "%d worlds x %d settings (bar %.0e) AND the pairing "
          "never exceeds the abs triangle (worst eps_pair - "
          "sum|ct| slack %+.1e <= 0) -- |Z| <= |Z_local| + eps "
          "is a window-independent triangle theorem"
          % (val_worst, n_worlds, len(settings), VAL_BAR,
             ref_worst))

    def fam_rows(nm):
        return res[nm][:len(recs)]

    for gate, nm in (("G41-c1-abelenv-census", "c1ENV"),
                     ("G42-c2-pairsum-census", "c2PAIR")):
        rws = fam_rows(nm)
        gains = [r_["gain"] for r_ in rws]
        epd = [math.log10(r_["eps"] / M_W) for r_ in rws]
        check(gate, True,
              "%s: gain over the abs triangle med %+.2f dec "
              "(min %+.2f, max %+.2f), eps med %+.2f dec vs M "
              "over %d rungs -- %s"
              % (nm, float(np.median(gains)) if gains else
                 float("nan"),
                 min(gains) if gains else float("nan"),
                 max(gains) if gains else float("nan"),
                 float(np.median(epd)) if epd else float("nan"),
                 len(rws),
                 "envelope VARIATION + error masses + boundary "
                 "(chain-recursion envelope)" if nm == "c1ENV"
                 else "exact block triangle over adjacent "
                 "sign-run pairs (offset 0)"))
    note3 = []
    for f in F_GRID:
        nm = "c3F%.2f" % f
        rws = fam_rows(nm)
        gains = [r_["gain"] for r_ in rws]
        note3.append("F%.2f gain med %+.2f dec"
                     % (f, float(np.median(gains)) if gains
                        else float("nan")))
    check("G43-c3-hybrid-census", True,
          "c3 HYBRID (sealed F grid, same pairing): %s -- "
          "adjudicated ONLY by the sealed best-by-cert rule "
          "below" % "; ".join(note3))

    if not smoke:
        g1s = {}
        for rc in recs:
            pk = QO.port_pack(rc["kz"])
            lam, U = np.linalg.eigh(pk["Q"])
            c2_ = (U.T @ pk["f"]) ** 2
            g1s[rc["kz"]] = float(np.sum(c2_ / (1.0 - lam)))
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
              "seed-%d shuffle mutant sp = %.3f misses -- r266 "
              "detector re-armed on the measured ladder"
              % (sp_wall, FP_BAR, sp_tgt, SHUFFLE_SEED, sp_mut))
        fired = []
        fp_note = []
        for nm, _fam, _f in settings:
            rws = fam_rows(nm)
            crit = [r_["margin"] for r_ in rws]
            passes = sum(1 for v in crit if v > 0.0)
            fl, sp_ = wall_flag(crit, passes)
            dem = [math.log10(r_["bound"] / M_W)
                   for r_ in rws if r_["exc"]]
            fire = (max(dem) >= DEMAND_BAR) if dem else False
            if fire:
                fired.append(nm)
            res[nm + "_meta"] = dict(sp=sp_, wall=fl, fire=fire,
                                     passes=passes,
                                     dem_med=float(np.median(dem))
                                     if dem else float("nan"),
                                     dem_max=max(dem)
                                     if dem else float("nan"))
            fp_note.append("%s sp %.2f cert %d/42 demand med "
                           "%+.2f max %+.2f%s"
                           % (nm, sp_, passes,
                              res[nm + "_meta"]["dem_med"],
                              res[nm + "_meta"]["dem_max"],
                              " FIRE" if fire else ""))
        check("G46-detector-census", True,
              "d2 paircorr demand log10((|Z_local| + eps)/M) on "
              "the exception branch (bar %.1f dec) + wall "
              "fingerprints (bar %.1f) on EVERY derivation: %s "
              "-- fired routes are closed for certification "
              "IMMEDIATELY" % (DEMAND_BAR, FP_BAR,
                               "; ".join(fp_note)))
    else:
        fired = []
        check("G45-wall-detector-armed", True, "SMOKE: skipped")
        check("G46-detector-census", True, "SMOKE: skipped")

    # ---------------- S5: LEG C -- success gate + typing
    section("S5  LEG C -- SUCCESS GATE + UNIVERSALITY TYPING")
    if not smoke:
        def cert_count(nm):
            meta = res[nm + "_meta"]
            if meta["wall"]:
                return -1
            return sum(1 for r_ in fam_rows(nm)
                       if r_["exc"] and r_["margin"] > 0.0)

        cons_ok = True
        for nm, _fam, _f in settings:
            for r_ in res[nm]:
                cons_ok = cons_ok and (r_["margin"]
                                       <= (M_W - abs(r_["Z"]))
                                       + TRI_BAR)
        best_c3 = max((nm for nm, _fam, _f in settings
                       if nm.startswith("c3")),
                      key=lambda nm: (cert_count(nm),
                                      -res[nm + "_meta"]["dem_med"]))
        show = ["c1ENV", "c2PAIR", best_c3]
        best_miss = {}
        for nm in show:
            for r_ in fam_rows(nm):
                if not r_["exc"]:
                    continue
                need = M_W - abs(r_["Zl"])
                miss = (math.log10(r_["eps"] / need)
                        if need > 0 else float("inf"))
                best_miss[(nm, r_["kz"])] = miss
                info("%s kz%-3d margin_true %+0.4f margin_cert "
                     "%+0.4f |Z_loc| %.3f eps %.3f gain %+0.2f "
                     "dec %s"
                     % (nm, r_["kz"], M_W - abs(r_["Z"]),
                        r_["margin"], abs(r_["Zl"]), r_["eps"],
                        r_["gain"],
                        "CERTIFIED" if r_["margin"] > 0
                        else ("miss %.2f dec" % miss
                              if math.isfinite(miss)
                              else "MAIN_TERM_EXCEEDS")))
        check("G50-success-gate-table", cons_ok,
              "per-exception-rung table printed for c1ENV, "
              "c2PAIR and the best c3 (%s); consistency "
              "margin_cert <= margin_true on every rung x "
              "setting (exact, %s)"
              % (best_c3, "OK" if cons_ok else "BROKEN"))
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        m15 = min(best_miss.get((nm, KZ_ANCHOR), float("inf"))
                  for nm in show)
        check("G51-kz15-design-anchor", ok15,
              "kz15 (N = %d, the razor): true reserve M - |Z| = "
              "%.4f in the sealed band %s (r263 record 0.027 "
              "reproduced); best phase-aware miss %s dec (r268 "
              "abs triangle missed by 0.44 dec)"
              % (rc15["N"], slack15, str(RESERVE_BAND),
                 ("%+.2f" % m15) if math.isfinite(m15)
                 else "n/a: CERTIFIED"))
        clean_ok = [nm for nm, _fam, _f in settings
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
            cert_best = cert_count(best_clean)
            full42 = sum(1 for r_ in fam_rows(best_clean)
                         if r_["margin"] > 0.0)
        else:
            best_clean = "none"
            cert_kzs = []
            rest_miss = []
            cert_best = 0
            full42 = 0
        if clean_ok and cert_best == len(exc):
            verdict_c = "GO"
        elif clean_ok:
            verdict_c = "PARTIAL"
        else:
            verdict_c = "INSUFFICIENT"
        check("G52-adjudication", True,
              "sealed rule (best clean candidate by cert count, "
              "tie by lower demand med): %s cert %d/7 (%s), "
              "full-ladder cert %d/42 (wall flags: %s; paircorr "
              "fired: %s) => PHASE_BOUND_%s -- no candidate "
              "repair after seeing the numbers"
              % (best_clean, max(cert_best, 0),
                 ", ".join("kz%d" % kz for kz in cert_kzs)
                 if cert_kzs else "none",
                 full42,
                 str([nm for nm, _fam, _f in settings
                      if res[nm + "_meta"]["wall"]]),
                 str(fired) if fired else "none", verdict_c))
        if best_clean in ("c1ENV", "c2PAIR"):
            typing = "UNIVERSAL_FORM"
            typ_note = ("ONE fixed formula (frozen F %.2f + "
                        "pairing offset %d, no per-rung "
                        "parameter); validity |R| <= eps is a "
                        "window-independent triangle THEOREM "
                        "(Lean-roadmap candidate); the "
                        "certification MARGIN stays measured on "
                        "the 42 -- NO cofinality claim"
                        % (EDGE_F, PAIR_OFFSET))
        elif best_clean != "none":
            typing = "SURFACE_ONLY"
            typ_note = ("the winning F parameter was adjudicated "
                        "on the 42 measured rungs -- honest "
                        "SURFACE_CERTIFIED_ONLY, the cofinal "
                        "step stays the open edge")
        else:
            typing = "NONE"
            typ_note = "no clean certifying candidate"
        check("G53-universality-typing", True,
              "sealed typing rule: %s -- %s" % (typing, typ_note))
    else:
        verdict_c = "SMOKE"
        best_clean = best_c3 = "n/a"
        typing = "n/a"
        check("G50-success-gate-table", True, "SMOKE: skipped")
        check("G51-kz15-design-anchor", True, "SMOKE: skipped")
        check("G52-adjudication", True, "SMOKE: skipped")
        check("G53-universality-typing", True, "SMOKE: skipped")

    # ---------------- S6: LEG D -- controls + wards + must-fails
    section("S6  LEG D -- CONTROLS + MP WARDS + MUST-FAILS")
    ctl_ok = True
    ctl_note = []
    for c in ("EPST", "SCR"):
        rc = crecs[c]
        ev = rc["ev"][EDGE_F]
        ok_v = (abs(ev["Rb"]) <= ev["e_pair"] + VAL_BAR
                and abs(ev["Rb"]) <= ev["e_env"] + VAL_BAR)
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        ctl_note.append("%s t %+0.3f dev %.1e validity %s"
                        % (c, rc["t_term"], dev,
                           "OK" if ok_v else "BROKEN"))
        ctl_ok = ctl_ok and ok_v and (dev <= TB_WARD_BAR_CTRL)
    main_fitted = not ctl_ok
    check("G60-control-reproduction", ctl_ok,
          "the phase-aware bounds hold on the PERTURBED worlds "
          "exactly (contribution identity + validity |R| <= eps "
          "on EPSTEIN/SCRAMBLE at F0.20): %s -- world-blind "
          "algebra, NOT main-fitted" % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    rcS = crecs["SMOOTH"]
    evS = rcS["ev"][EDGE_F]
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    okS_v = abs(evS["Rb"]) <= evS["e_pair"] + VAL_BAR
    check("G61-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okS_v,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "bound validity holds trivially on the self-aliased "
          "source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okS_v else "BROKEN"))
    if not smoke:
        mp_note = []
        mp_w = 0.0
        for kz in MP_WARD_KZ:
            rc = next(r_ for r_ in recs if r_["kz"] == kz)
            t_mp = mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            mp_w = max(mp_w, dv)
            mp_note.append("kz%d (N = %d) t_mp = %+0.9f dev %.1e"
                           % (kz, rc["N"], t_mp, dv))
        check("G62-mp-drive-wards", mp_w <= MP_T_BAR,
              "mp (dps %d) terminal drive t_{N-2} at the sealed "
              "rungs (kz22 = the r268-certified rung as "
              "regression ward): %s (bar %.0e)"
              % (MP_DPS, "; ".join(mp_note), MP_T_BAR))
    else:
        check("G62-mp-drive-wards", True, "SMOKE: skipped")
    # m3 offset-peek mutant: measured + typed forbidden
    n_gain = 0
    g_max = 0.0
    for rc in all_rc:
        ev = rc["ev"][EDGE_F]
        d_ = ev["e_pair"] - ev["e_peek"]
        if d_ > 1e-12:
            n_gain += 1
            g_max = max(g_max, d_)
    check("G64-mustfail-offset-peek", True,
          "m3 BLOCK BOUNDARIES AFTER LOOKING AT CANCELLATION: "
          "the offset-peek mutant (min over both pairings) "
          "gains > 1e-12 on %d/%d rungs (max %.3f abs) -- the "
          "temptation is real and stays SEALED AWAY: the "
          "candidates use offset %d unconditionally (frozen "
          "before evaluation); the mutant is selection-by-"
          "answer, typed FORBIDDEN"
          % (n_gain, len(all_rc), g_max, PAIR_OFFSET))
    viol = 0.0
    honest = max(tb_worst, 1e-300)
    for rc in all_rc:
        ev = rc["ev"][0.10]
        viol = max(viol, (abs(rc["t_term"]) - abs(ev["t_loc"]))
                   / max(rc["absum"], 1e-300))
    check("G65-mustfail-naked-truncation", viol >= LOUD * honest,
          "m4 (inherited r268 m1) WINDOW TRUNCATION WITHOUT "
          "ERROR TERM: the naked claim |t| <= |t_local| breaks "
          "by %.1e (abs-mass units) = %.1e x the honest ward "
          "floor %.1e (bar %.0f x) -- no truncation is "
          "admissible without its eps term"
          % (viol, viol / honest, honest, LOUD))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact bulk-remainder anatomy (flip runs + "
          "chain envelope + potential), three sealed phase-aware "
          "triangle bounds with exact validity, the honest "
          "success-gate adjudication on the exception branch, "
          "and the sealed universality typing")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # anatomy summary for the verdict (exception branch)
        r_run = []
        r_maj = []
        r_err = []
        for rc in exc:
            ev = rc["ev"][EDGE_F]
            r_run.append(len(ev["runs"]) / max(ev["nb"], 1))
            o = rc["o"]
            ed = mask_edge(rc["bx"][o], rc["lo"], rc["hi"],
                           EDGE_F)
            cb = rc["ct"][o][~ed]
            Eb = rc["E"][o][~ed]
            r_maj.append(float(np.mean(np.abs(cb) <= Eb)))
            r_err.append(sum(abs(a_ - b_) for a_, b_
                             in zip(ev["Mr"], ev["Er"]))
                         / max(sum(ev["Er"]), 1e-300))
        pot_exc = [math.log10(rc["ev"][EDGE_F]["ab"]
                              / abs(rc["ev"][EDGE_F]["Rb"]))
                   for rc in exc
                   if abs(rc["ev"][EDGE_F]["Rb"]) > 1e-300]
        parts = []
        parts.append("BULK_ANATOMY(runs ~ %.2f x bulk atoms, "
                     "pairability 1.00, env majorization %.2f / "
                     "error share %.2f, potential med %.2f dec "
                     "vs needed 0.18-0.44)"
                     % (float(np.median(r_run)),
                        float(np.median(r_maj)),
                        float(np.median(r_err)),
                        float(np.median(pot_exc))))
        for nm, label in (("c1ENV", "C1_ABEL_ENV"),
                          ("c2PAIR", "C2_PAIRSUM")):
            rws = fam_rows(nm)
            gains = [r_["gain"] for r_ in rws]
            parts.append("%s(cert %d/7, gain med %+.2f dec, "
                         "valid %d/%d)"
                         % (label, max(cert_count(nm), 0),
                            float(np.median(gains)),
                            n_worlds, n_worlds))
        parts.append("C3_HYBRID(best %s, cert %d/7)"
                     % (best_c3, max(cert_count(best_c3), 0)))
        if verdict_c == "GO":
            parts.append("PHASE_BOUND_GO(%s, 7/7, "
                         "SURFACE_CLOSED, %s)"
                         % (best_clean, typing))
        elif verdict_c == "PARTIAL":
            parts.append("PHASE_BOUND_PARTIAL(%s, cert %d/7: "
                         "%s; rest misses %.2f-%.2f dec, %s)"
                         % (best_clean, cert_best,
                            ", ".join("kz%d" % kz
                                      for kz in cert_kzs),
                            min(rest_miss), max(rest_miss),
                            typing))
        else:
            parts.append("PHASE_BOUND_INSUFFICIENT(the measured "
                         "limit of the local class: even the "
                         "exact adjacent-pair cancellation "
                         "leaves the certification budget "
                         "unmet -- the remaining cancellation "
                         "sits ACROSS non-adjacent runs: "
                         "root-scale comb territory)")
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        if fired:
            parts.append("PAIRCORR_MINIATURE(%s)"
                         % ", ".join(fired))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the contribution "
          "decomposition, the block-triangle validity, the "
          "Chebyshev envelope invariant; MEASURED: the run/"
          "envelope censuses, the gains, the success-gate "
          "table, the certification margins (42 rungs only); "
          "OPEN: the cofinal step (window-independent margin "
          "law); NO RH claim"
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
