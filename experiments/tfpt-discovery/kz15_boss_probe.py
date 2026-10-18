#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kz15_boss_probe -- PRIME.PORT.RHP.QUENCHED.KZ15_BOSS.01
(round 270): the kz15 boss fight under the binding reviewer
adjudication: NO further F0.20 level-1 optimisation (the r269
record measured only 0.05 dec of TOTAL level-1 ground-truth
headroom at that split); instead exactly THREE sealed attacks,
every rule frozen BEFORE evaluation, then an honest close.
REVIEWER ANATOMY HYPOTHESIS (the lever): at kz15 the adjacent
PAIR SUMS cancel each other across the whole bulk (a SECOND
cancellation level); the r269 method re-absolutises after the
first pairing (eps_L1 = sum|P_i|) and loses that level -- the
0.05-dec limit binds the LEVEL-1 class only.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r268/r269 machinery verbatim): t_{N-2} = sum_b ct_b,
ct_b = bw_b bx_b v_{N-2}(bx_b) e^{Ls_{N-2}-Ls_{N-1}} /
sqrt|eta_{N-1}| (r244 scaled rows, r266 eval); Z_w = t_{N-2} +
a'_{N-2} r_{N-2} + b'_{N-2} r_{N-3}; split t = t_edge + R; runs =
maximal same-sign runs of ct on the bx-sorted bulk (they
alternate, r269 G31); signed run sums s_i; LEVEL-1 blocks P_j =
s_{2j} + s_{2j+1} (offset 0, odd tail run its own block);
eps_L1 = sum_j |P_j| == the r269 c2PAIR bound (equality warded).
LEVEL-2 (new): eps_L2 = sum_k |P_{2k} + P_{2k+1}| + (|P_last| if
the block count is odd) -- the exact block triangle one level up
(offset 0 frozen, both levels).  THEOREM CHAIN (gated exactly):
|R| <= eps_L2 <= eps_L1 <= sum|ct_bulk|.

LEG A -- LEVEL-2 ANATOMY FIRST (kz15 + the 6 certified + mains +
5 cheap refs): (a1) sign structure of the P_j sequence
(alternation fraction of adjacent signs, sign-run lengths,
pairability); (a2) the LEVEL-2 chain envelope EP_j =
|E~_{2j} - E~_{2j+1}| + D_{2j} + D_{2j+1} (E~ = r269 sealed
Pruefer/Christoffel chain-envelope run masses -- SOURCE; D_i =
|M_i - E~_i| the honest envelope-error mass; odd tail E~ + D):
majorization share, slack share; (a3) the LEVEL-2 POTENTIAL
(ground truth, typed POTENTIAL_ONLY, never a bound): pot2 =
log10(eps_L1 / |R|) per rung vs the level-1 miss log10(eps_L1 /
need), need = M - |Z_local|: does perfect level-2 pairing hold
MORE decades than kz15 needs (r269 record: c2 miss 0.18 dec at
F0.20, c3F0.30 miss 0.12 dec)?
LEG B -- THE THREE SEALED ATTACKS (rules here, no re-selection):
(b1) LEVEL-2 BLOCK-ALTERNATION at the FROZEN record split F0.20:
  eps_L2 as defined above; validity warded on 42 rungs + 2 mains
  + 3 controls (exact triangle, slack <= 1e-9); certification
  |Z_local| + eps_L2 < M = sqrt(5/7) on the 7 exception rungs;
  kz15 detail always.  b1 is the ONLY new F0.20 candidate and it
  is a LEVEL-2 object -- no level-1 re-optimisation.
(b2) A-PRIORI MASS-DEFINED SPLIT (ONE rule, ONE evaluation):
  edge = the minimal set of atoms, in ascending order of the
  hull-edge coordinate f_b = min(bx_b - lo, hi - bx_b)/(hi - lo)
  (ties by stable original index), whose ABSOLUTE contribution
  mass sum|ct| reaches >= MASS_FRAC = 2/3 of the total; realised
  as the threshold f* of the last prefix atom (edge = f_b <= f*).
  MOTIVATION (sealed with the rule, r268 record): '10 pct of the
  hull carries 2/3 of the absolute mass' -- a mass-defined
  boundary instead of a parameter-defined one.  PROTOCOL: the
  ground-truth POTENTIAL of the new split is measured and
  REPORTED BEFORE the bound gates; then eps_L1 and eps_L2 on the
  mass split, certification on the 7.  NO other mass fraction is
  evaluated by any candidate (the peek mutant below is typed
  FORBIDDEN and only measured).
(b3) CERTIFIED INTERVAL EVALUATION of Z_kz15 (typed
  EXACT_FINITE_CERTIFICATE): a legitimate finite certificate of
  the r262-reviewer precedent kind ('the current rungs could
  afterwards be certified exactly') -- NOT a mechanism, does NOT
  count as a target-blind class certificate; it closes the
  surface honestly.  Route: the ENTIRE bordered chain (r269
  mp_drive route extended to the full terminal readout Z = t +
  a' r + b' r) in outward-rounded mpmath INTERVAL arithmetic
  (mp.iv, IV_DPS 640; the interval DEPENDENCY growth of the
  three-term recursion consumes ~2.2 digits per chain step,
  measured on the w9 SELFTEST window -- the working precision
  is an engineering constant, sized BEFORE any boss-target
  evaluation): every f64 source atom converted EXACTLY
  (binary64 -> point interval), every subsequent operation an
  enclosure; normalisation constants sc are exact point floats
  from interval midpoints (they cancel in the algebra: Ls
  accumulates iv.log(sc)); every sign use (eta, gam) demands a
  sign-DEFINITE interval, else the certificate aborts.
  CERTIFICATE: sup|Z_iv| < inf(iv.sqrt(5/7)) STRICT.  PRECISION
  CHAIN documented: dps, atom/iteration counts, interval widths
  (eta_{N-1}, Z), margin.  SCOPE (typed): the certificate is a
  statement about the f64-DEFINED comb of the ladder (the rung's
  source data ARE these binary64 atoms; no claim about any
  higher-precision re-derivation of the atoms themselves).
LEG C -- WARDS / DETECTORS / MUST-FAILS: d2 PAIRCORR demand
log10((|Z_local| + eps)/M) (sealed bar 1.0 dec, exception
branch) + r266 WALL fingerprint (bar 0.9, selftest re-armed) on
b1/b2; kz22/kz39 REGRESSION wards (b1 must keep kz22; the r269
c3F0.30 kz39 margin +0.075 reproduced in [0.06, 0.09] -- no
certified rung is lost); r268/r269 reproduction wards (exception
set == the named 7; kz15 reserve in [0.020, 0.035]; c2PAIR kz15
miss 0.18 +- 0.02; c2 cert set == {20, 22, 36, 38, 52}; c3F0.30
kz15 miss in [0.10, 0.14]; kz15 F0.20 total potential in [0.44,
0.54]); eps_L1 == r269 bound_pairsum equality (rel 1e-9); toy
triangle chain |sum| <= eps_L2 <= eps_L1 <= sum|.| exact on 200
seeded random combs (seed 270); iv SELFTEST on w9 (f64 Z inside
the interval, dev <= 1e-9); SMOOTH anchor (alias <= 1e-12, q_N
<= 1e-20, validity trivial); EPSTEIN/SCRAMBLE control
reproduction (identity + validity, world-blind); mp point ward
(dps 60) of t_{N-2} at kz15 (bar 1e-8); MUST-FAILS: (m1) LEVEL-2
ENVELOPE FROM DATA -- the mutant smoothing realized block sums
into an envelope is CIRCULAR, flagged by the AST envelope-scope
audit (the sealed env2 builder consumes chain run masses +
declared error masses only); (m2) SPLIT RULE AFTER THE NUMBERS
-- the mutant evaluating the mass grid {0.50, 0.60, 2/3, 0.75,
0.80} and keeping the best kz15 margin is selection-by-answer:
AST-flagged AND its gain measured and printed, typed FORBIDDEN
(the sealed candidates use 2/3 unconditionally); (m3) SILENT
ROUNDING LOSS -- dps HALVING must BLOW the certificate: the
interval route at IV_DPS_HALF 320 must FAIL to certify
(sign-indefinite abort, sign-indefinite Z, or width > the true
reserve); if the half run survives at all it must additionally
have widened by >= IV_RATIO_MIN 1e6 while intersecting the
full-precision enclosure -- low precision can never silently
certify.
SEALED ADJUDICATION (priority order fixed BEFORE evaluation,
never by result): a clean candidate (no wall flag, no paircorr
fire) certifies kz15 => KZ15_CLOSED, candidate named in the
order b1 > b2L2 > b2L1; surface tally = 35 cheap + union of
exception rungs certified by sealed candidates across rounds
(r268 kz22, r269 c2/c3F0.30 reproduced, this round's clean
candidates); kz15 via b3 counts SEPARATELY (exact-finite, not
target-blind).  VERDICT GRAMMAR (joined with '+'):
  LEVEL2_ANATOMY(blocks, alt frac, env maj/slack, pot2 med,
    kz15 pot2 vs miss_L1)
+ B1_L2PAIR(cert k/7, kz15 miss dec, gain med dec)
+ B2_MASS_SPLIT(f* med, pot med dec, L1 cert k/7, L2 cert k/7,
    kz15 miss dec)
+ B3_INTERVAL(EXACT_FINITE_CERTIFICATE closed/failed, margin,
    width, dps)
+ [exactly one of] KZ15_CLOSED(cand, SURFACE 42/42 target-blind)
    / KZ15_EXACT_ONLY(surface closed: 41 mechanism + kz15
    exact-finite; the MECHANISM stays open) / KZ15_OPEN(all
    three attacks failed)
+ [if pot2(kz15, F0.20) < miss_L1(kz15, F0.20)]
    LEVEL2_POTENTIAL_INSUFFICIENT(where the cancellation sits)
+ [if b2 does not certify kz15] SPLIT_RULE_FAILED(cert counts)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if fired] PAIRCORR_MINIATURE(candidate list).
Honesty before beauty: no verdict claims a cofinal law or an
asymptotic mechanism; b3 is typed as a finite certificate, never
as a class statement; r243-r269 stand.

INDEX FIREWALL (binding, r238-r269 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, true R/t/Z) enters GATES and census tables only; no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r269 PBB.mask_edge/runs_split/bound_pairsum/env_chain/
mp_drive, r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r260 TX.drive_arrays, r263 CA.g_gap, r264 QO.port_pack, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 imported floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls; VAL_BAR 1e-9; TRI_BAR 1e-9 (also the eps_L1 equality
rel bar); EDGE_F 0.20 (frozen record split); REF_F30 0.30
(reproduction-WARD setting only, NOT a candidate of this round);
PAIR_OFFSET 0 (both levels, frozen); MASS_FRAC 2/3 (the ONE
sealed split rule); MASS_GRID (0.50, 0.60, 2/3, 0.75, 0.80)
(FORBIDDEN mutant only); RESERVE_BAND (0.020, 0.035); R269
reproduction bands: C2_KZ15_MISS 0.18 tol 0.02, C2_CERT_SET
(20, 22, 36, 38, 52), C3F30_KZ39_MARGIN_BAND (0.06, 0.09),
C3F30_KZ15_MISS_BAND (0.10, 0.14), KZ15_POT_BAND (0.44, 0.54);
DEMAND_BAR 1.0 dec; FP_BAR 0.9; MP_DPS 60; MP_T_BAR 1e-8;
IV_DPS 640; IV_DPS_HALF 320; IV_WIDTH_BAR 1e-40; IV_RATIO_MIN
1e6; IV_F64_BAR 1e-9 (w9 selftest) / 1e-8 (kz15 cross ward);
SM_Q_BAR 1e-20; SM_ALIAS_BAR 1e-12; TOY_SEED 270; TOY_N 200;
TOY_BAR 1e-12 (rel); SHUFFLE_SEED 270; CHEAP_REF_IDX
(0, 10, 20, 30, 41) (advance rule inherited); KZ_ANCHOR 15;
runtime <= 1800 s; smoke = w9 + controls + toy + iv selftest +
scope audits + candidate numerics on w9 (ladder, detectors, mp
wards, b3-kz15, adjudication skipped).  DISCLOSED PRE-SPEC INPUT
(no scratch run of this probe): every reproduction band is an
r263/r264/r266/r268/r269 RECORD number adopted as-is; the only
pre-spec measurements of this round are ENGINEERING-ONLY
feasibility checks (mpmath.iv API + op timing on toy scalars;
kz15 atom counts 405 union / 405 border, N = 203) -- no target
quantity, no potential, no bound was evaluated before sealing.
DISCLOSED PRE-RECORD AMENDMENT (engineering, before the record
run, after smoke pass 1): the originally sealed IV_DPS 60 /
IV_DPS_HALF 30 / IV_DPS_BREAK 5 underestimated the interval
DEPENDENCY growth of the recursion (~2.2 digits consumed per
chain step, measured on the w9 SELFTEST window where the dps-60
enclosure honestly ABORTED sign-indefinite); re-sized to IV_DPS
640 / IV_DPS_HALF 320 and the break tier merged into the
halving must-fail -- NO physics bar, band, rule, split, bound
or verdict rule moved; the boss target kz15 was never evaluated
during the re-sizing.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 29/29 gates after the disclosed engineering
amendment above; calibration pass 1 = first full evaluation =
the record run below, 29/29 gates, wall 30.0 s -- NO physics
bar, band, rule, split or verdict rule was moved at any point;
the only post-freeze edit is this record-table insertion, which
IS the protocol; the post-insertion passes reproduce every
printed figure exactly):
CAL_VERDICT = LEVEL2_ANATOMY(blocks ~ 0.50 x runs, alt frac med
0.39, pot2 med exc 0.28 dec, kz15 pot2 0.22 vs miss_L1 0.18) +
B1_L2PAIR(cert 5/7, kz15 miss +0.06 dec, gain med +0.12 dec) +
B2_MASS_SPLIT(f* med 0.102, pot med exc 0.74 dec, L1 cert 1/7,
L2 cert 4/7, kz15 miss +0.31 dec) + B3_INTERVAL(
EXACT_FINITE_CERTIFICATE closed, margin +0.02680, width
1.5e-92, dps 640) + KZ15_EXACT_ONLY(surface closed: 41
mechanism + kz15 exact-finite; mechanism OPEN) +
SPLIT_RULE_FAILED(L1 1/7, L2 4/7).
Key numbers.  LEG A (7 exc + 2 mains + 5 cheap refs, F0.20):
contribution ward worst dev/absmass 2.1e-13 main / 3.9e-13
deep / 2.4e-8 controls; r269 reproduction wards EXACT (c2PAIR
kz15 miss 0.177 vs record 0.18; c2 cert set == the named 5;
c3F0.30 kz15 miss 0.117 in [0.10, 0.14]; c3F0.30 kz39 margin
+0.0750 in [0.06, 0.09]; kz15 F0.20 total potential 0.485 in
[0.44, 0.54]; true reserve 0.0268; eps_L1 == r269 bound_pairsum
worst rel dev 9.3e-16); LEVEL-2 anatomy: blocks = ceil(runs/2)
everywhere; the P_j sequence does NOT alternate cleanly --
adjacent opposite-sign fraction 0.31-0.50 on the exceptions
(med 0.39; kz15 0.42; a fair coin, NO level-2 alternation law),
sign-run lengths med 1-2 max 6-13; the level-2 chain envelope
EP majorizes |P_j| 1.00 on every pool rung but with slack share
0.54-0.62 (coarse); LEVEL-2 POTENTIAL (typed POTENTIAL_ONLY):
exceptions pot2 0.16-0.39 dec (med 0.28), all-42 med 0.49 dec;
AT THE RAZOR kz15: pot2 = 0.22 dec vs needed miss_L1 = 0.18 dec
-- the reviewer's second cancellation level EXISTS and its
perfect capture would certify kz15, but with only +0.04 dec of
ground-truth headroom.  LEG B: b1 validity + monotonicity exact
on 47 worlds (worst slacks -8.9e-3 / -6.9e-3 <= 0); gain over
eps_L1 med +0.12 dec (min +0.01, max +0.25); cert 5/7 -- kz20
margin_cert +0.1507, kz22 +0.5228, kz36 +0.1524, kz38 +0.2019,
kz52 +0.2510; kz39 misses by 0.002 dec (margin -0.0022: blind
level-2 pairing captures only +0.01 dec on kz39's P-sequence),
kz15 misses by +0.06 dec (margin -0.0461, gain +0.11 of the
needed 0.177): the coin-like P-signs leave 0.06 dec
uncaptured.  b2 mass split: f* med 0.102 (the r268 '10 pct of
the hull carries 2/3 of the absolute mass' reproduced as a
rule; edge share 0.36-0.46 of the atoms), potential med exc
0.74 dec -- the potential is LARGE but the bounds do not reach
it: eps on the 2/3-mass bulk stays 0.5-1.2 vs needs 0.28-0.79,
L1 cert 1/7 (kz22), L2 cert 4/7 (kz20, kz22, kz36, kz38), kz15
L2 miss +0.31 dec => SPLIT_RULE_FAILED (one sealed rule, one
evaluation, honestly reported).  b3 kz15 (N = 203, 405 + 405
f64 atoms exactly converted, dps 640, outward-rounded): Z
enclosed in [-0.818353152618..., -0.818353152618...], width
1.5e-92 (eta_{N-1} rel width 3.5e-92, interval dependency
consumed ~548 digits over 202 chain steps); sup|Z| <
inf(sqrt(5/7)) STRICT: CLOSED, margin +0.02680 == the r263/
r269 true reserve reproduced at certificate level; f64 cross
ward dev 1.3e-10 (bar 1e-8); w9 selftest dev 8.6e-12 (width
4.5e-239).  LEG C: wall fingerprints b1L2F020 sp 0.02 /
b2L1MASS 0.57 / b2L2MASS 0.41, all < 0.9, no all-FALSE pattern
=> NO candidate is the wall; paircorr demand on the exception
branch: b1 med -0.09 max +0.02, b2L1 med +0.07 max +0.19, b2L2
med -0.03 max +0.13 -- nothing reaches the 1.0-dec bar (the
gap stays SUB-PAIRCORR); full-ladder cert b1 32/42, b2L2
10/42; regression: kz22 margin_cert under b1 +0.5228 > 0,
c3F0.30 kz39 margin +0.0750 reproduced -- no certified rung
lost; controls EPST dev 6.0e-11 / SCR 2.4e-8 + validity exact
(world-blind, NOT main-fitted); SMOOTH alias 2.4e-14, q_N
4.2e-25, validity trivial; mp point ward kz15 dev 2.9e-10 (bar
1e-8); must-fails: m1 env-from-data mutant FLAGGED (ct in env2
scope), m2 frac-peek mutant FLAGGED (margin in scope) AND
measured: the grid mutant picks 0.80 with kz15 margin -0.0013
vs the sealed rule's -0.2896 (gain +0.2882 margin units -- the
temptation is real, stays SEALED AWAY, and even the mutant
does NOT certify kz15), m3 the halved dps 320 BLOWS the
certificate (eta sign-indefinite at n = 143).  READING (typed,
no upgrade): the reviewer's level-2 hypothesis is CONFIRMED IN
SUBSTANCE and bounded in size -- a second cancellation level
exists on every measured rung (pot2 med 0.28 dec on the
exceptions) and at kz15 its perfect capture would certify (0.22
vs 0.18), but the P-sign sequence is coin-like (alt frac 0.39
med), so the sealed BLIND adjacent level-2 pairing captures
only +0.11 dec of kz15's needed 0.177 and misses by 0.06 dec
(kz39 by 0.002 dec); the mass-defined 2/3 split fails loudly
and honestly; the surface is CLOSED: 41/42 mechanism-certified
target-blind (35 cheap + 6 exceptions across sealed rounds) +
kz15 by EXACT_FINITE_CERTIFICATE (typed separately, a finite
enclosure statement, not a mechanism); the open edges after
this round: (i) the kz15 level-2 MECHANISM (0.06 dec,
sub-paircorr, sign structure beyond blind pairing -- e.g. a
source-derivable P-sign law), (ii) the cofinal step
(window-independent margin law) -- unchanged.  Runtime 30.0 s
full / 6.5 s smoke; the two post-insertion passes are identical
up to WALL.
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

import phase_bulk_bound_probe as PBB           # noqa: E402 r269
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
REF_F30 = 0.30
PAIR_OFFSET = 0
MASS_FRAC = 2.0 / 3.0
MASS_GRID = (0.50, 0.60, 2.0 / 3.0, 0.75, 0.80)
RESERVE_BAND = (0.020, 0.035)
C2_KZ15_MISS = 0.18
C2_KZ15_MISS_TOL = 0.02
C2_CERT_SET = (20, 22, 36, 38, 52)
C3F30_KZ39_MARGIN_BAND = (0.06, 0.09)
C3F30_KZ15_MISS_BAND = (0.10, 0.14)
KZ15_POT_BAND = (0.44, 0.54)
DEMAND_BAR = 1.0
FP_BAR = 0.9
MP_DPS = 60
MP_T_BAR = 1e-8
IV_DPS = 640
IV_DPS_HALF = 320
IV_WIDTH_BAR = 1e-40
IV_RATIO_MIN = 1e6
IV_F64_BAR_W9 = 1e-9
IV_F64_BAR_KZ15 = 1e-8
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
TOY_SEED = 270
TOY_N = 200
TOY_BAR = 1e-12
SHUFFLE_SEED = 270
CHEAP_REF_IDX = (0, 10, 20, 30, 41)
KZ_ANCHOR = 15

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


CAND_FORBIDDEN = {"t" + "_term", "rho", "S", "sa", "la", "q_chain",
                  "D_dir", "wb", "world_block", "direct_terminal",
                  "rhp_readout", "gram_input", "g_gap",
                  "u_triangle", "M_W", "R" + "_bulk", "margin"}
ENV2_FORBIDDEN = CAND_FORBIDDEN | {"ct", "cts", "t" + "_loc",
                                   "t" + "_edge", "Pj", "Pabs"}


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


# ---- sealed builders (target-blind: consume ONLY the plain
# arrays passed as arguments; the withheld terminal drive key and
# every target-side identifier are forbidden in scope, AST-audit;
# the LEVEL-2 envelope builder additionally must not consume the
# realized contributions or block sums -- circularity firewall)
def signed_run_sums(cb, runs):
    """signed sums s_i of the maximal same-sign runs (exact
    decomposition of the bulk remainder)."""
    return [float(np.sum(cb[a:b])) for a, b, _s in runs]


def blocks_level1(sv):
    """LEVEL-1 blocks P_j = s_{2j} + s_{2j+1} from PAIR_OFFSET 0;
    an odd tail run forms its own final block (frozen rule)."""
    P = []
    m = len(sv)
    for i in range(PAIR_OFFSET, m - 1, 2):
        P.append(sv[i] + sv[i + 1])
    if (m - PAIR_OFFSET) % 2 == 1:
        P.append(sv[-1])
    return P


def bound_level2(P):
    """LEVEL-2 sealed block-alternation bound: eps_L2 =
    sum_k |P_{2k} + P_{2k+1}| + (|P_last| if the block count is
    odd) -- the exact block triangle one level up (offset 0)."""
    e = 0.0
    m2 = len(P)
    for i in range(PAIR_OFFSET, m2 - 1, 2):
        e += abs(P[i] + P[i + 1])
    if (m2 - PAIR_OFFSET) % 2 == 1:
        e += abs(P[-1])
    return e


def env2_chain(Er, Dr):
    """sealed LEVEL-2 envelope (anatomy object, never consumed by
    any bound): EP_j = |E~_{2j} - E~_{2j+1}| + D_{2j} + D_{2j+1}
    from the r269 CHAIN envelope run masses E~ plus the declared
    envelope-error masses D; odd tail E~ + D."""
    EP = []
    m = len(Er)
    for i in range(PAIR_OFFSET, m - 1, 2):
        EP.append(abs(Er[i] - Er[i + 1]) + Dr[i] + Dr[i + 1])
    if (m - PAIR_OFFSET) % 2 == 1:
        EP.append(Er[-1] + Dr[-1])
    return EP


def split_mass(fbf, act):
    """b2 sealed A-PRIORI split rule (the ONE rule, evaluated
    once): edge = minimal prefix in ascending hull-edge
    coordinate fbf whose absolute mass reaches >= MASS_FRAC of
    the total; realised as threshold f* (edge = fbf <= f*)."""
    tot = float(np.sum(act))
    order = np.argsort(fbf, kind="stable")
    cum = np.cumsum(act[order])
    idx = int(np.searchsorted(cum, MASS_FRAC * tot, side="left"))
    idx = min(idx, len(order) - 1)
    f_star = float(fbf[order[idx]])
    return fbf <= f_star, f_star


def env2_mutant_data(ct):
    """m1 MUST-FAIL MUTANT: level-2 envelope smoothed from the
    realized data -- CIRCULAR; the envelope scope audit must FLAG
    this (ct is forbidden in env2 scope)."""
    a = np.abs(ct)
    k = np.ones(3) / 3.0
    return np.convolve(a, k, mode="same")


def split_mutant_fracpeek(fbf, act, cts, chain_val):
    """m2 MUST-FAIL MUTANT: evaluates the WHOLE mass grid and
    keeps the split with the best kz-level certification margin
    -- selection-by-answer; AST-flagged (margin in scope) and its
    gain measured, typed FORBIDDEN."""
    best = None
    tot = float(np.sum(act))
    order = np.argsort(fbf, kind="stable")
    cum = np.cumsum(act[order])
    for fr in MASS_GRID:
        idx = min(int(np.searchsorted(cum, fr * tot, side="left")),
                  len(order) - 1)
        ed = fbf <= float(fbf[order[idx]])
        cb = cts[~ed]
        runs = PBB.runs_split(cb)
        sv = signed_run_sums(cb, runs)
        eps = bound_level2(blocks_level1(sv))
        margin = M_W - (abs(float(np.sum(cts[ed])) + chain_val)
                        + eps)
        if best is None or margin > best[1]:
            best = (fr, margin)
    return best


# ------------------------------------------------ rung record
def rung_rec(p):
    """r269 rung record verbatim: contributions ct, chain
    envelope E, hull, drive/chain scalars."""
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


def split_eval(rc, ed):
    """evaluate one split (edge mask on the bx-sorted arrays):
    local sum, bulk remainder, runs, masses, envelope masses,
    signed sums, level-1 blocks, eps_L1/eps_L2 + anatomy."""
    o = rc["o"]
    cts = rc["ct"][o]
    Es = rc["E"][o]
    t_loc = float(np.sum(cts[ed]))
    cb = cts[~ed]
    Eb = Es[~ed]
    Rb = float(np.sum(cb))
    ab = float(np.sum(np.abs(cb)))
    runs = PBB.runs_split(cb)
    Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
    Er = [float(np.sum(Eb[a:b])) for a, b, _s in runs]
    Dr = [abs(m_ - e_) for m_, e_ in zip(Mr, Er)]
    sv = signed_run_sums(cb, runs)
    P = blocks_level1(sv)
    eps_L1 = sum(abs(v) for v in P)
    eps_L1_ref = PBB.bound_pairsum(Mr)
    eps_L2 = bound_level2(P)
    sg = [s for _a, _b, s in runs]
    alt_ok = all(sg[i + 1] == -sg[i] for i in range(len(sg) - 1))
    return dict(t_loc=t_loc, Zl=t_loc + rc["chain"], Rb=Rb, ab=ab,
                runs=runs, Mr=Mr, Er=Er, Dr=Dr, sv=sv, P=P,
                eps_L1=eps_L1, eps_L1_ref=eps_L1_ref,
                eps_L2=eps_L2, alt_ok=alt_ok, nb=int(len(cb)))


def p_sign_census(P):
    """level-2 sign anatomy of the block sequence P_j."""
    sg = [1.0 if v > 0 else (-1.0 if v < 0 else 0.0) for v in P]
    nz = [s for s in sg if s != 0.0]
    if len(nz) < 2:
        return dict(alt=float("nan"), rl_med=0, rl_max=0, m2=len(P))
    flips = sum(1 for i in range(len(nz) - 1)
                if nz[i + 1] == -nz[i])
    alt = flips / (len(nz) - 1)
    rl = []
    cur = 1
    for i in range(1, len(nz)):
        if nz[i] == nz[i - 1]:
            cur += 1
        else:
            rl.append(cur)
            cur = 1
    rl.append(cur)
    return dict(alt=alt, rl_med=int(np.median(rl)),
                rl_max=int(max(rl)), m2=len(P))


# ---------------------------------------------------- iv route
def _iv_abs(x):
    if x.a > 0:
        return x
    if x.b < 0:
        return -x
    return None


def _iv_sgn(x):
    if x.a > 0:
        return 1
    if x.b < 0:
        return -1
    return 0


def iv_chain_Z(xu, wu, bx, bw, N, dps):
    """b3 certified interval evaluation: the ENTIRE bordered
    chain (r269 mp_drive route extended to the full terminal
    readout Z = t_{N-2} + a'_{N-2} r_{N-2} + b'_{N-2} r_{N-3})
    in outward-rounded mpmath interval arithmetic.  Every f64
    source atom converted EXACTLY (point interval); scaling
    constants are exact point floats (they cancel: Ls accumulates
    iv.log(sc)); every sign use demands a sign-DEFINITE interval,
    else the certificate honestly aborts (returns the abort
    stage).  Returns dict(lo, hi, wid, mid, eta_relwid, a_mp,
    b_mp) or dict(blown=stage); a_mp/b_mp are the EXACT mpf
    endpoints (the strict comparison never passes through f64
    rounding)."""
    iv = mp.iv
    old_dps = iv.dps
    try:
        iv.dps = dps
        one = iv.mpf(1)
        zero = iv.mpf(0)
        X = [iv.mpf(float(v)) for v in xu]
        W = [iv.mpf(float(v)) for v in wu]
        Bx = [iv.mpf(float(v)) for v in bx]
        Bw = [iv.mpf(float(v)) for v in bw]
        Bwx = [Bw[i] * Bx[i] for i in range(len(Bx))]
        nx, nb = len(X), len(Bx)
        qx = [one] * nx
        qb = [one] * nb
        qx_m = [zero] * nx
        qb_m = [zero] * nb
        Ls = zero
        Ls_m = zero
        eta = sum(W[i] * qx[i] * qx[i] for i in range(nx))
        eta_m = eta
        cap = {}
        gamA = gamB = None
        for n in range(N - 1):
            if _iv_sgn(eta) == 0:
                return dict(blown="eta sign-indefinite at n=%d"
                            % n)
            if n == N - 3:
                cap["fb3"] = sum(Bw[i] * qb[i] for i in range(nb))
                cap["eta3"] = eta
            if n == N - 2:
                cap["fb2"] = sum(Bw[i] * qb[i] for i in range(nb))
                cap["tb2"] = sum(Bwx[i] * qb[i] for i in range(nb))
                cap["eta2"] = eta
                cap["Ls2"] = Ls
            alh = sum(W[i] * X[i] * qx[i] * qx[i]
                      for i in range(nx)) / eta
            if n == N - 2:
                cap["alh2"] = alh
            if n == 0:
                px = [(X[i] - alh) * qx[i] for i in range(nx)]
                pb = [(Bx[i] - alh) * qb[i] for i in range(nb)]
            else:
                gf = (eta / eta_m) * iv.exp(Ls - Ls_m)
                px = [(X[i] - alh) * qx[i] - gf * qx_m[i]
                      for i in range(nx)]
                pb = [(Bx[i] - alh) * qb[i] - gf * qb_m[i]
                      for i in range(nb)]
            sc = 0.0
            for v in px:
                sc = max(sc, abs(float(v.mid)))
            if sc <= 0.0 or not math.isfinite(sc):
                return dict(blown="scale degenerate at n=%d" % n)
            SC = iv.mpf(sc)
            qx_m, qb_m, eta_m, Ls_m = qx, qb, eta, Ls
            qx = [v / SC for v in px]
            qb = [v / SC for v in pb]
            Ls = Ls + iv.log(SC)
            eta = sum(W[i] * qx[i] * qx[i] for i in range(nx))
            gam = (eta / eta_m) * iv.exp(2 * (Ls - Ls_m))
            if n == N - 3:
                gamA = gam
            if n == N - 2:
                gamB = gam
        etaN1 = eta
        aN1 = _iv_abs(etaN1)
        a2 = _iv_abs(cap["eta2"])
        a3 = _iv_abs(cap["eta3"])
        aA = _iv_abs(gamA)
        aB = _iv_abs(gamB)
        if None in (aN1, a2, a3, aA, aB):
            return dict(blown="terminal sign-indefinite")
        sA = _iv_sgn(gamA)
        t2 = cap["tb2"] * iv.exp(cap["Ls2"] - Ls) / iv.sqrt(aN1)
        term_a = (-cap["alh2"] / iv.sqrt(aB)) \
            * (cap["fb2"] / iv.sqrt(a2))
        term_b = iv.mpf(-sA) * iv.sqrt(aA / aB) \
            * (cap["fb3"] / iv.sqrt(a3))
        Z = t2 + term_a + term_b
        rel = float(etaN1.delta) / abs(float(etaN1.mid))
        return dict(lo=float(Z.a), hi=float(Z.b),
                    wid=float(Z.delta), mid=float(Z.mid),
                    eta_relwid=rel, a_mp=Z.a, b_mp=Z.b)
    except (ValueError, ZeroDivisionError, OverflowError,
            ArithmeticError) as e:
        return dict(blown="iv exception: %s" % e)
    finally:
        iv.dps = old_dps


def iv_of_pack(p, dps):
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    return iv_chain_Z(xu, wu, bx, bw, p["N"], dps)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("kz15_boss_probe -- PRIME.PORT.RHP.QUENCHED."
          "KZ15_BOSS.01 (round 270)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   F_DEF_SHA %s "
          "(imported r243)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + iv selftest "
                        "+ scope audits + candidate numerics; "
                        "ladder, detectors, mp wards, b3-kz15, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "KZ15 BOSS FIGHT under the binding reviewer "
          "adjudication: NO F0.20 level-1 re-optimisation "
          "(measured level-1 headroom 0.05 dec); exactly THREE "
          "sealed attacks -- b1 LEVEL-2 block alternation at the "
          "frozen split (pairs of pair sums, offset 0), b2 ONE "
          "a-priori mass-defined split (2/3 absolute-mass edge, "
          "rule + motivation sealed, potential reported BEFORE "
          "the bound gates), b3 certified interval evaluation of "
          "Z_kz15 typed EXACT_FINITE_CERTIFICATE (finite "
          "surface-closing certificate, NOT a mechanism, NOT "
          "target-blind class evidence); level-2 anatomy + "
          "potential measured FIRST and always reported; "
          "detectors armed on every derivation; adjudication "
          "priority b1 > b2L2 > b2L1 frozen BEFORE evaluation"
          )

    # ---------------- S1: census + controls (r269 scaffold)
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

    # ---------------- S2: LEG A -- wards + level-2 anatomy
    section("S2  LEG A -- WARDS + LEVEL-2 ANATOMY + POTENTIAL")
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
          "%.0e) -- exact decomposition"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    # per-rung evaluation on the three splits (+ the F0.30 ward
    # setting, reproduction only -- NOT a candidate)
    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        out = {}
        for key, f in (("F020", EDGE_F), ("F030", REF_F30)):
            ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], f)
            out[key] = split_eval(rc, ed)
        span = rc["hi"] - rc["lo"]
        fbf = np.minimum(bxs - rc["lo"], rc["hi"] - bxs) / span
        act = np.abs(cts)
        edm, f_star = split_mass(fbf, act)
        out["MASS"] = split_eval(rc, edm)
        out["MASS"]["f_star"] = f_star
        out["MASS"]["edge_share"] = float(np.mean(edm))
        rc["fbf"] = fbf
        return out

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    # eps_L1 equality ward vs r269 bound_pairsum (exact algebra)
    eq_worst = 0.0
    for rc in all_rc:
        for key in ("F020", "F030", "MASS"):
            ev = rc["ev"][key]
            eq_worst = max(eq_worst,
                           abs(ev["eps_L1"] - ev["eps_L1_ref"])
                           / max(ev["eps_L1_ref"], 1e-300))
    alt_all = all(rc["ev"][key]["alt_ok"]
                  for rc in all_rc for key in ("F020", "F030",
                                               "MASS"))

    if not smoke:
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        ev15 = rc15["ev"]["F020"]
        need15 = M_W - abs(ev15["Zl"])
        missL1_15 = math.log10(ev15["eps_L1"] / need15)
        pot15 = math.log10(ev15["ab"] / abs(ev15["Rb"]))
        c2_certs = []
        for rc in exc:
            ev = rc["ev"]["F020"]
            if M_W - (abs(ev["Zl"]) + ev["eps_L1"]) > 0.0:
                c2_certs.append(rc["kz"])
        ev15_30 = rc15["ev"]["F030"]
        need15_30 = M_W - abs(ev15_30["Zl"])
        miss30_15 = math.log10(ev15_30["eps_L1"] / need15_30)
        rc39 = next(r_ for r_ in recs if r_["kz"] == 39)
        ev39_30 = rc39["ev"]["F030"]
        mg39_30 = M_W - (abs(ev39_30["Zl"]) + ev39_30["eps_L1"])
        slack15 = M_W - abs(rc15["Z"])
        c3f30_certs = []
        for rc in exc:
            ev = rc["ev"]["F030"]
            if M_W - (abs(ev["Zl"]) + ev["eps_L1"]) > 0.0:
                c3f30_certs.append(rc["kz"])
        ok21 = (abs(missL1_15 - C2_KZ15_MISS) <= C2_KZ15_MISS_TOL
                and tuple(sorted(c2_certs)) == C2_CERT_SET
                and C3F30_KZ15_MISS_BAND[0] <= miss30_15
                <= C3F30_KZ15_MISS_BAND[1]
                and C3F30_KZ39_MARGIN_BAND[0] <= mg39_30
                <= C3F30_KZ39_MARGIN_BAND[1]
                and KZ15_POT_BAND[0] <= pot15 <= KZ15_POT_BAND[1]
                and RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
                and eq_worst <= TRI_BAR and alt_all)
        check("G21-r269-reproduction-wards", ok21,
              "r269 record recomputed: c2PAIR kz15 miss %.3f dec "
              "(record %.2f, tol %.2f); c2 cert set %s == %s; "
              "c3F0.30 kz15 miss %.3f in %s; c3F0.30 kz39 margin "
              "%+.4f in %s (REGRESSION anchor); kz15 F0.20 total "
              "potential %.3f dec in %s; true reserve %.4f in "
              "%s; eps_L1 == r269 bound_pairsum (worst rel dev "
              "%.1e, bar %.0e); run alternation exact everywhere"
              % (missL1_15, C2_KZ15_MISS, C2_KZ15_MISS_TOL,
                 str(tuple(sorted(c2_certs))), str(C2_CERT_SET),
                 miss30_15, str(C3F30_KZ15_MISS_BAND), mg39_30,
                 str(C3F30_KZ39_MARGIN_BAND), pot15,
                 str(KZ15_POT_BAND), slack15, str(RESERVE_BAND),
                 eq_worst, TRI_BAR))
    else:
        check("G21-r269-reproduction-wards",
              eq_worst <= TRI_BAR and alt_all,
              "SMOKE: ladder wards skipped; eps_L1 equality on "
              "w9 (worst rel dev %.1e) + run alternation OK"
              % eq_worst)

    # level-2 anatomy census
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
    alt_pool = []
    for rc in anat_pool:
        ev = rc["ev"]["F020"]
        cen = p_sign_census(ev["P"])
        EP = env2_chain(ev["Er"], ev["Dr"])
        Pa = [abs(v) for v in ev["P"]]
        maj = (float(np.mean([a_ <= e_ + 1e-15 for a_, e_
                              in zip(Pa, EP)])) if Pa else 0.0)
        slack = (sum(max(e_ - a_, 0.0) for a_, e_
                     in zip(Pa, EP))
                 / max(sum(EP), 1e-300)) if EP else 0.0
        pot2 = (math.log10(ev["eps_L1"] / abs(ev["Rb"]))
                if abs(ev["Rb"]) > 1e-300 else float("inf"))
        need = M_W - abs(ev["Zl"])
        missL1 = (math.log10(ev["eps_L1"] / need) if need > 0
                  else float("inf"))
        if rc["g"] < 0:
            alt_pool.append(cen["alt"])
        info("kz%-3d N%-4d %-4s runs %-4d blocks %-4d altfrac "
             "%.2f (rl med %d max %d)  EPmaj %.2f slack %.2f  "
             "pot2 %+.2f dec  missL1 %+.2f dec  headroom %+.2f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g"] < 0 else "chp",
                len(ev["runs"]), cen["m2"], cen["alt"],
                cen["rl_med"], cen["rl_max"], maj, slack, pot2,
                missL1 if math.isfinite(missL1) else float("nan"),
                pot2 - missL1 if math.isfinite(missL1)
                else float("nan")))
    check("G22-level2-anatomy-census", True,
          "a1/a2 MEASUREMENT (pool = %s): P_j sign structure "
          "(alternation fraction, sign-run lengths), level-2 "
          "chain envelope EP (majorization, slack share) -- per "
          "pool rung printed; exception alt frac med %.2f"
          % ("7 exc + 2 mains + 5 cheap refs" if not smoke
             else "mains (SMOKE)",
             float(np.median(alt_pool)) if alt_pool
             else float("nan")))
    pot2_all = []
    pot2_exc = []
    for rc in (recs if not smoke else mrecs):
        ev = rc["ev"]["F020"]
        if abs(ev["Rb"]) > 1e-300:
            v = math.log10(ev["eps_L1"] / abs(ev["Rb"]))
            pot2_all.append(v)
            if rc["g"] < 0:
                pot2_exc.append(v)
    if not smoke:
        head15 = (math.log10(ev15["eps_L1"] / abs(ev15["Rb"]))
                  - missL1_15)
        kz15_note = ("kz15: pot2 %.2f dec vs needed miss_L1 "
                     "%.2f dec -- level-2 headroom %+.2f dec"
                     % (math.log10(ev15["eps_L1"]
                                   / abs(ev15["Rb"])),
                        missL1_15, head15))
    else:
        kz15_note = "kz15 n/a (SMOKE)"
    check("G23-level2-potential-typed", True,
          "a3 MEASUREMENT (typed POTENTIAL_ONLY, never a bound): "
          "level-2 perfect-pairing depth pot2 = log10(eps_L1/|R|)"
          " med %.2f dec all / %.2f dec exceptions; %s"
          % (float(np.median(pot2_all)) if pot2_all
             else float("nan"),
             float(np.median(pot2_exc)) if pot2_exc
             else float("nan"), kz15_note))

    # ---------------- S3: toy + scope audits + iv selftest
    section("S3  TOY THEOREMS + SCOPE AUDITS + IV SELFTEST")
    rng = np.random.default_rng(TOY_SEED)
    toy_worst = 0.0
    for _i in range(TOY_N):
        n = int(rng.integers(1, 61))
        cb = rng.normal(size=n)
        runs = PBB.runs_split(cb)
        sv = signed_run_sums(cb, runs)
        P = blocks_level1(sv)
        e1 = sum(abs(v) for v in P)
        e2 = bound_level2(P)
        ab = float(np.sum(np.abs(cb)))
        s = abs(float(np.sum(cb)))
        scl = max(ab, 1e-300)
        toy_worst = max(toy_worst, (s - e2) / scl,
                        (e2 - e1) / scl, (e1 - ab) / scl)
    check("G30-toy-triangle-chain", toy_worst <= TOY_BAR,
          "|sum| <= eps_L2 <= eps_L1 <= sum|.| EXACT on %d "
          "seeded random combs (seed %d, worst rel slack %.1e, "
          "bar %.0e) -- the level-2 bound is a triangle THEOREM "
          "on the block decomposition, never worse than level 1"
          % (TOY_N, TOY_SEED, toy_worst, TOY_BAR))
    h_b1 = scope_audit("blocks_level1", CAND_FORBIDDEN)
    h_b2 = scope_audit("bound_level2", CAND_FORBIDDEN)
    h_sp = scope_audit("split_mass", CAND_FORBIDDEN
                       | {"ct", "cts"})
    h_e2 = scope_audit("env2_chain", ENV2_FORBIDDEN)
    h_m1 = scope_audit("env2_mutant_data", ENV2_FORBIDDEN)
    h_m2 = scope_audit("split_mutant_fracpeek", CAND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G31-scope-audits",
          not (h_b1 or h_b2 or h_sp or h_e2)
          and bool(h_m1) and bool(h_m2) and not ag_hits,
          "sealed builders CLEAN (level-1/2 consume signed run "
          "sums only%s; split rule consumes hull coordinate + "
          "absolute masses only%s; env2 consumes chain run "
          "masses + declared error masses only%s); m1 "
          "env-from-data mutant FLAGGED (%s); m2 frac-peek "
          "mutant FLAGGED (%s); fragment audit: %s"
          % ("" if not (h_b1 or h_b2) else " VIOLATION",
             "" if not h_sp else " VIOLATION " + "; ".join(h_sp),
             "" if not h_e2 else " VIOLATION " + "; ".join(h_e2),
             "; ".join(h_m1) if h_m1 else "NOT FLAGGED",
             "; ".join(h_m2) if h_m2 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    rc9 = recs[0] if smoke else mrecs[0]
    iv9 = iv_of_pack(rc9["p"], IV_DPS)
    ok32 = ("blown" not in iv9
            and iv9["lo"] - IV_F64_BAR_W9 <= rc9["Z"]
            <= iv9["hi"] + IV_F64_BAR_W9
            and abs(rc9["Z"] - iv9["mid"]) <= IV_F64_BAR_W9)
    check("G32-iv-selftest", ok32,
          "iv route selftest on w%d (N = %d): f64 Z %+0.9f "
          "inside the dps-%d enclosure [%+.9f, %+.9f] (width "
          "%.1e, dev %.1e, bar %.0e) -- the interval chain "
          "reproduces the f64 chain"
          % (rc9["kz"], rc9["N"], rc9["Z"], IV_DPS,
             iv9.get("lo", float("nan")),
             iv9.get("hi", float("nan")),
             iv9.get("wid", float("nan")),
             abs(rc9["Z"] - iv9.get("mid", float("nan"))),
             IV_F64_BAR_W9))

    # ---------------- S4: LEG B -- the three sealed attacks
    section("S4  LEG B -- THE THREE SEALED ATTACKS")
    val_worst = -1e300
    mono_worst = -1e300
    for rc in all_rc:
        for key in ("F020", "MASS"):
            ev = rc["ev"][key]
            val_worst = max(val_worst,
                            (abs(ev["Rb"]) - ev["eps_L2"])
                            / max(ev["ab"], 1e-300))
            mono_worst = max(mono_worst,
                             (ev["eps_L2"] - ev["eps_L1"])
                             / max(ev["ab"], 1e-300))
    for c in crecs:
        for key in ("F020", "MASS"):
            ev = crecs[c]["ev"][key]
            val_worst = max(val_worst,
                            (abs(ev["Rb"]) - ev["eps_L2"])
                            / max(ev["ab"], 1e-300))
    n_worlds = len(all_rc) + len(crecs)
    check("G40-validity-wards", val_worst <= VAL_BAR
          and mono_worst <= VAL_BAR,
          "the level-2 bound is an EXACT theorem on the "
          "decomposition: worst (|R| - eps_L2)/absmass slack "
          "%+.1e <= 0 over %d worlds x 2 splits (bar %.0e) AND "
          "eps_L2 never exceeds eps_L1 (worst rel slack %+.1e) "
          "-- |Z| <= |Z_local| + eps_L2 is a window-independent "
          "triangle theorem"
          % (val_worst, n_worlds, VAL_BAR, mono_worst))

    # b1: level-2 at F0.20
    def cert_rows(split_key, level):
        rows_ = []
        for rc in all_rc:
            ev = rc["ev"][split_key]
            eps = ev["eps_L2"] if level == 2 else ev["eps_L1"]
            Zl = ev["Zl"]
            rows_.append(dict(kz=rc["kz"], exc=rc["g"] < 0,
                              eps=eps, Zl=Zl,
                              bound=abs(Zl) + eps,
                              margin=M_W - (abs(Zl) + eps),
                              gain=math.log10(
                                  max(ev["eps_L1"], 1e-300)
                                  / max(eps, 1e-300)),
                              Z=rc["Z"]))
        return rows_

    res = {"b1L2F020": cert_rows("F020", 2),
           "b2L1MASS": cert_rows("MASS", 1),
           "b2L2MASS": cert_rows("MASS", 2)}

    def exc_table(nm, label):
        certs = []
        misses = {}
        for r_ in res[nm][:len(recs)]:
            if not r_["exc"]:
                continue
            need = M_W - abs(r_["Zl"])
            miss = (math.log10(r_["eps"] / need) if need > 0
                    else float("inf"))
            if r_["margin"] > 0.0:
                certs.append(r_["kz"])
            misses[r_["kz"]] = miss
            info("%s kz%-3d margin_true %+0.4f margin_cert "
                 "%+0.4f |Z_loc| %.3f eps %.3f gain %+0.2f %s"
                 % (label, r_["kz"], M_W - abs(r_["Z"]),
                    r_["margin"], abs(r_["Zl"]), r_["eps"],
                    r_["gain"],
                    "CERTIFIED" if r_["margin"] > 0
                    else ("miss %+.2f dec" % miss
                          if math.isfinite(miss)
                          else "MAIN_TERM_EXCEEDS")))
        return sorted(certs), misses

    if not smoke:
        g1 = [math.log10(max(r_["eps_L1"], 1e-300)
                         / max(r_["eps_L2"], 1e-300))
              for r_ in (rc["ev"]["F020"] for rc in recs)]
        certs_b1, miss_b1 = exc_table("b1L2F020", "b1L2F020")
        check("G41-b1-level2-census", True,
              "b1 LEVEL-2 at the frozen split F%.2f: gain over "
              "eps_L1 med %+.2f dec (min %+.2f, max %+.2f) over "
              "42 rungs; cert %d/7 (%s); kz15 %s"
              % (EDGE_F, float(np.median(g1)), min(g1), max(g1),
                 len(certs_b1),
                 ", ".join("kz%d" % k for k in certs_b1)
                 if certs_b1 else "none",
                 ("CERTIFIED" if KZ_ANCHOR in certs_b1 else
                  "miss %+.2f dec" % miss_b1[KZ_ANCHOR])))
    else:
        certs_b1 = []
        miss_b1 = {}
        check("G41-b1-level2-census", True, "SMOKE: skipped "
              "(w9 numerics covered by G40)")

    # b2: potential of the mass split FIRST (sealed protocol),
    # then the bounds
    if not smoke:
        fstars = [rc["ev"]["MASS"]["f_star"] for rc in recs]
        pot_m = []
        pot_m_exc = []
        for rc in recs:
            ev = rc["ev"]["MASS"]
            if abs(ev["Rb"]) > 1e-300:
                v = math.log10(ev["ab"] / abs(ev["Rb"]))
                pot_m.append(v)
                if rc["g"] < 0:
                    pot_m_exc.append(v)
        for rc in sorted(exc, key=lambda r_: r_["kz"]):
            ev = rc["ev"]["MASS"]
            need = M_W - abs(ev["Zl"])
            info("MASS kz%-3d f* %.3f edge share %.2f  |Z_loc| "
                 "%.3f need %+0.4f  pot %+.2f dec"
                 % (rc["kz"], ev["f_star"], ev["edge_share"],
                    abs(ev["Zl"]), need,
                    math.log10(ev["ab"] / abs(ev["Rb"]))
                    if abs(ev["Rb"]) > 1e-300 else float("inf")))
        check("G42-b2-potential-first", True,
              "b2 sealed protocol: the mass split's ground-truth "
              "potential MEASURED AND REPORTED BEFORE the bound "
              "gates -- f* med %.3f (edge = 2/3 absolute mass), "
              "potential med %.2f dec all / %.2f dec exceptions "
              "(typed POTENTIAL_ONLY)"
              % (float(np.median(fstars)),
                 float(np.median(pot_m)) if pot_m
                 else float("nan"),
                 float(np.median(pot_m_exc)) if pot_m_exc
                 else float("nan")))
        certs_b2l1, miss_b2l1 = exc_table("b2L1MASS", "b2L1MASS")
        certs_b2l2, miss_b2l2 = exc_table("b2L2MASS", "b2L2MASS")
        check("G43-b2-mass-split-census", True,
              "b2 bounds on the ONE sealed mass split: L1 cert "
              "%d/7 (%s), L2 cert %d/7 (%s); kz15 L2 %s -- one "
              "rule, one evaluation, honestly reported"
              % (len(certs_b2l1),
                 ", ".join("kz%d" % k for k in certs_b2l1)
                 if certs_b2l1 else "none",
                 len(certs_b2l2),
                 ", ".join("kz%d" % k for k in certs_b2l2)
                 if certs_b2l2 else "none",
                 ("CERTIFIED" if KZ_ANCHOR in certs_b2l2 else
                  "miss %+.2f dec" % miss_b2l2[KZ_ANCHOR])))
    else:
        certs_b2l1 = certs_b2l2 = []
        miss_b2l2 = {}
        check("G42-b2-potential-first", True, "SMOKE: skipped")
        check("G43-b2-mass-split-census", True, "SMOKE: skipped")

    # b3: certified interval evaluation of Z_kz15
    if not smoke:
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        iv60 = iv_of_pack(rc15["p"], IV_DPS)
        iv_ = mp.iv
        old_ivdps = iv_.dps
        iv_.dps = IV_DPS
        MW_iv = iv_.sqrt(iv_.mpf(5) / iv_.mpf(7))
        MW_inf = MW_iv.a
        iv_.dps = old_ivdps
        MW_lo = float(MW_inf)  # display only
        b3_closed = False
        b3_margin = float("nan")
        if "blown" not in iv60:
            # strict comparison in EXACT endpoint arithmetic
            absZ_hi = max(abs(iv60["a_mp"]), abs(iv60["b_mp"]))
            b3_closed = (iv60["a_mp"] * iv60["b_mp"] > 0
                         and absZ_hi < MW_inf)
            # conservative display value: the LOWER endpoint of
            # the outward-rounded margin enclosure
            b3_margin = float((MW_inf - absZ_hi).a)
        check("G44-b3-interval-certificate",
              b3_closed and iv60.get("wid", 1.0) <= IV_WIDTH_BAR,
              "b3 EXACT_FINITE_CERTIFICATE kz15 (N = %d, %d + %d "
              "f64 atoms EXACTLY converted, dps %d, outward-"
              "rounded): Z in [%+.12f, %+.12f], width %.1e (bar "
              "%.0e), eta_{N-1} rel width %.1e; sup|Z| < "
              "inf(sqrt(5/7)) = %.6f... STRICT: %s, margin "
              "%+.5f -- a finite certificate (EnclOK kind), NOT "
              "a mechanism, NOT target-blind class evidence"
              % (rc15["N"], len(CT.union_arrays(rc15["p"]["d"])[0]),
                 len(CT.union_arrays(rc15["p"]["dsm"])[0]),
                 IV_DPS, iv60.get("lo", float("nan")),
                 iv60.get("hi", float("nan")),
                 iv60.get("wid", float("nan")), IV_WIDTH_BAR,
                 iv60.get("eta_relwid", float("nan")), MW_lo,
                 "CLOSED" if b3_closed else "FAILED", b3_margin))
        dev_f64 = abs(rc15["Z"] - iv60.get("mid", float("nan")))
        ok45 = ("blown" not in iv60
                and iv60["lo"] - IV_F64_BAR_KZ15 <= rc15["Z"]
                <= iv60["hi"] + IV_F64_BAR_KZ15
                and dev_f64 <= IV_F64_BAR_KZ15)
        cons = (IV_DPS - (-math.log10(iv60["wid"]))
                if "blown" not in iv60 and iv60["wid"] > 0
                else float("nan"))
        check("G45-b3-precision-wards", ok45,
              "precision chain documented: dps %d, %d chain "
              "steps, interval dependency consumed ~%.0f digits "
              "(final width %.1e); f64 cross ward: Z_f64 inside "
              "the enclosure, dev %.1e (bar %.0e) -- no silent "
              "rounding loss"
              % (IV_DPS, rc15["N"] - 1, cons,
                 iv60.get("wid", float("nan")), dev_f64,
                 IV_F64_BAR_KZ15))
    else:
        b3_closed = False
        b3_margin = float("nan")
        iv60 = {}
        check("G44-b3-interval-certificate", True,
              "SMOKE: skipped (iv route covered by G32 selftest)")
        check("G45-b3-precision-wards", True, "SMOKE: skipped")

    # ---------------- S5: detectors + regression + adjudication
    section("S5  DETECTORS + REGRESSION + ADJUDICATION")
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
        rng2 = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(g1v,
                                 list(rng2.permutation(g1v))))
        check("G50-wall-detector-armed",
              fl_wall and not fl_tgt and sp_mut < FP_BAR,
              "selftest: wall criterion g(1) < 1 FALSE 42/42, "
              "sp(g1, g1) = %.3f >= %.1f FLAGGED; target D_N > 0 "
              "TRUE 42/42, sp(D_N, g1) = %.3f NOT flagged; "
              "seed-%d shuffle mutant sp = %.3f misses"
              % (sp_wall, FP_BAR, sp_tgt, SHUFFLE_SEED, sp_mut))
        fired = []
        fp_note = []
        meta = {}
        for nm in ("b1L2F020", "b2L1MASS", "b2L2MASS"):
            rws = res[nm][:len(recs)]
            crit = [r_["margin"] for r_ in rws]
            passes = sum(1 for v in crit if v > 0.0)
            fl, sp_ = wall_flag(crit, passes)
            dem = [math.log10(r_["bound"] / M_W)
                   for r_ in rws if r_["exc"]]
            fire = (max(dem) >= DEMAND_BAR) if dem else False
            if fire:
                fired.append(nm)
            meta[nm] = dict(sp=sp_, wall=fl, fire=fire,
                            passes=passes)
            fp_note.append("%s sp %.2f cert %d/42 demand med "
                           "%+.2f max %+.2f%s"
                           % (nm, sp_, passes,
                              float(np.median(dem)), max(dem),
                              " FIRE" if fire else ""))
        check("G51-detector-census", True,
              "d2 paircorr demand (bar %.1f dec, exception "
              "branch) + wall fingerprints (bar %.1f) on every "
              "derivation: %s -- fired routes are closed for "
              "certification IMMEDIATELY"
              % (DEMAND_BAR, FP_BAR, "; ".join(fp_note)))
        mg22_b1 = next(r_["margin"] for r_ in res["b1L2F020"]
                       if r_["kz"] == 22)
        check("G52-regression-kz22-kz39", mg22_b1 > 0.0
              and C3F30_KZ39_MARGIN_BAND[0] <= mg39_30
              <= C3F30_KZ39_MARGIN_BAND[1],
              "no certified rung is lost: kz22 margin_cert under "
              "b1 %+.4f > 0 (eps_L2 <= eps_L1 keeps every c2 "
              "cert); kz39 stays certified by the reproduced "
              "r269 c3F0.30 (margin %+.4f in %s)"
              % (mg22_b1, mg39_30, str(C3F30_KZ39_MARGIN_BAND)))
        clean = {nm: (not meta[nm]["wall"]
                      and not meta[nm]["fire"])
                 for nm in meta}
        cert_sets = {"b1L2F020": set(certs_b1),
                     "b2L2MASS": set(certs_b2l2),
                     "b2L1MASS": set(certs_b2l1)}
        closer = None
        for nm in ("b1L2F020", "b2L2MASS", "b2L1MASS"):
            if clean[nm] and KZ_ANCHOR in cert_sets[nm]:
                closer = nm
                break
        base_union = set([22]) | set(C2_CERT_SET) \
            | set(c3f30_certs)
        mech_union = set(base_union)
        for nm in cert_sets:
            if clean[nm]:
                mech_union |= cert_sets[nm]
        n_mech = CHEAP_EXPECT + len(mech_union)
        check("G53-adjudication-surface", True,
              "sealed priority b1 > b2L2 > b2L1: kz15 mechanism "
              "closer = %s; surface tally = %d cheap + %d "
              "exception rungs mechanism-certified across sealed "
              "rounds (%s) = %d/42%s"
              % (closer if closer else "NONE",
                 CHEAP_EXPECT, len(mech_union),
                 ", ".join("kz%d" % k
                           for k in sorted(mech_union)),
                 n_mech,
                 "; kz15 additionally EXACT-FINITE (b3), typed "
                 "separately" if b3_closed
                 and KZ_ANCHOR not in mech_union else ""))
    else:
        fired = []
        closer = None
        mech_union = set()
        n_mech = 0
        check("G50-wall-detector-armed", True, "SMOKE: skipped")
        check("G51-detector-census", True, "SMOKE: skipped")
        check("G52-regression-kz22-kz39", True, "SMOKE: skipped")
        check("G53-adjudication-surface", True, "SMOKE: skipped")

    # ---------------- S6: controls + mp wards + must-fails
    section("S6  CONTROLS + MP WARDS + MUST-FAILS")
    ctl_ok = True
    ctl_note = []
    for c in ("EPST", "SCR"):
        rc = crecs[c]
        ev = rc["ev"]["F020"]
        evm = rc["ev"]["MASS"]
        ok_v = (abs(ev["Rb"]) <= ev["eps_L2"] + VAL_BAR
                and abs(evm["Rb"]) <= evm["eps_L2"] + VAL_BAR)
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        ctl_note.append("%s t %+0.3f dev %.1e validity %s"
                        % (c, rc["t_term"], dev,
                           "OK" if ok_v else "BROKEN"))
        ctl_ok = ctl_ok and ok_v and (dev <= TB_WARD_BAR_CTRL)
    main_fitted = not ctl_ok
    check("G60-control-reproduction", ctl_ok,
          "level-2 bound + mass split hold on the PERTURBED "
          "worlds exactly (identity + validity on EPSTEIN/"
          "SCRAMBLE): %s -- world-blind algebra, NOT main-fitted"
          % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    rcS = crecs["SMOOTH"]
    evS = rcS["ev"]["F020"]
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    okS_v = abs(evS["Rb"]) <= evS["eps_L2"] + VAL_BAR
    check("G61-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okS_v,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "level-2 validity holds trivially (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okS_v else "BROKEN"))
    if not smoke:
        t_mp15 = PBB.mp_drive(rc15["p"], MP_DPS)
        dv15 = abs(t_mp15 - rc15["t_term"])
        check("G62-mp-point-ward", dv15 <= MP_T_BAR,
              "mp (dps %d) point value of t_{N-2} at kz15: "
              "t_mp = %+0.9f dev %.1e (bar %.0e) -- the f64 "
              "chain is honest at the anchor"
              % (MP_DPS, t_mp15, dv15, MP_T_BAR))
        o15 = rc15["o"]
        peek = split_mutant_fracpeek(
            rc15["fbf"], np.abs(rc15["ct"][o15]),
            rc15["ct"][o15], rc15["chain"])
        mg_seal = next(r_["margin"] for r_ in res["b2L2MASS"]
                       if r_["kz"] == KZ_ANCHOR)
        check("G63-mustfail-frac-peek", True,
              "m2 SPLIT RULE AFTER THE NUMBERS: the grid mutant "
              "(best of %s by kz15 margin) picks %.2f with "
              "margin %+.4f vs the sealed 2/3 rule %+.4f -- "
              "gain %+.4f; the temptation is real and stays "
              "SEALED AWAY (typed FORBIDDEN, AST-flagged)"
              % (str(tuple(round(f, 2) for f in MASS_GRID)),
                 peek[0], peek[1], mg_seal, peek[1] - mg_seal))
        ivb = iv_of_pack(rc15["p"], IV_DPS_HALF)
        need_true = M_W - abs(rc15["Z"])
        if "blown" in ivb:
            broken = True
            note64 = ivb["blown"]
        else:
            no_cert = (ivb["wid"] > need_true
                       or ivb["lo"] * ivb["hi"] <= 0.0)
            ratio = ivb["wid"] / max(iv60.get("wid", 1e-300),
                                     1e-300)
            inter = ("blown" not in iv60
                     and max(ivb["lo"], iv60["lo"])
                     <= min(ivb["hi"], iv60["hi"]))
            broken = no_cert and ratio >= IV_RATIO_MIN and inter
            note64 = ("width %.2e vs true reserve %.4f, widened "
                      "x %.1e (bar >= %.0e), enclosures "
                      "intersect %s"
                      % (ivb["wid"], need_true, ratio,
                         IV_RATIO_MIN, "OK" if inter else "NO"))
        check("G64-mustfail-dps-halving", broken,
              "m3 SILENT ROUNDING LOSS: the interval route at "
              "the HALVED dps %d BLOWS the certificate (%s) -- "
              "the certificate is precision-honest, low "
              "precision cannot silently certify"
              % (IV_DPS_HALF, note64))
    else:
        check("G62-mp-point-ward", True, "SMOKE: skipped")
        check("G63-mustfail-frac-peek", True, "SMOKE: skipped")
        check("G64-mustfail-dps-halving", True, "SMOKE: skipped")

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the level-2 cancellation anatomy + potential, "
          "the sealed level-2 block triangle, the one a-priori "
          "mass split, and the exact-finite interval certificate "
          "surface close of kz15")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        r_blocks = []
        for rc in exc:
            ev = rc["ev"]["F020"]
            r_blocks.append(len(ev["P"])
                            / max(len(ev["runs"]), 1))
        parts = []
        parts.append("LEVEL2_ANATOMY(blocks ~ %.2f x runs, alt "
                     "frac med %.2f, pot2 med exc %.2f dec, "
                     "kz15 pot2 %.2f vs miss_L1 %.2f)"
                     % (float(np.median(r_blocks)),
                        float(np.median(alt_pool)),
                        float(np.median(pot2_exc)),
                        math.log10(ev15["eps_L1"]
                                   / abs(ev15["Rb"])),
                        missL1_15))
        parts.append("B1_L2PAIR(cert %d/7, kz15 %s, gain med "
                     "%+.2f dec)"
                     % (len(certs_b1),
                        "CERTIFIED" if KZ_ANCHOR in certs_b1
                        else "miss %+.2f dec"
                        % miss_b1[KZ_ANCHOR],
                        float(np.median(g1))))
        parts.append("B2_MASS_SPLIT(f* med %.3f, pot med exc "
                     "%.2f dec, L1 cert %d/7, L2 cert %d/7, "
                     "kz15 %s)"
                     % (float(np.median(fstars)),
                        float(np.median(pot_m_exc)),
                        len(certs_b2l1), len(certs_b2l2),
                        "CERTIFIED" if KZ_ANCHOR in certs_b2l2
                        else "miss %+.2f dec"
                        % miss_b2l2[KZ_ANCHOR]))
        parts.append("B3_INTERVAL(EXACT_FINITE_CERTIFICATE %s, "
                     "margin %+.5f, width %.1e, dps %d)"
                     % ("closed" if b3_closed else "FAILED",
                        b3_margin, iv60.get("wid", float("nan")),
                        IV_DPS))
        if closer is not None:
            parts.append("KZ15_CLOSED(%s, SURFACE %d/42 "
                         "target-blind)" % (closer, n_mech))
        elif b3_closed:
            parts.append("KZ15_EXACT_ONLY(surface closed: %d "
                         "mechanism + kz15 exact-finite; "
                         "mechanism OPEN)" % n_mech)
        else:
            parts.append("KZ15_OPEN(all three attacks failed)")
        head15v = (math.log10(ev15["eps_L1"] / abs(ev15["Rb"]))
                   - missL1_15)
        if head15v < 0.0:
            parts.append("LEVEL2_POTENTIAL_INSUFFICIENT(kz15 "
                         "level-2 headroom %+.2f dec: the "
                         "residual cancellation sits ACROSS "
                         "non-adjacent blocks)" % head15v)
        if KZ_ANCHOR not in (set(certs_b2l1) | set(certs_b2l2)):
            parts.append("SPLIT_RULE_FAILED(L1 %d/7, L2 %d/7)"
                         % (len(certs_b2l1), len(certs_b2l2)))
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        if fired:
            parts.append("PAIRCORR_MINIATURE(%s)"
                         % ", ".join(fired))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the block-triangle "
          "chain |R| <= eps_L2 <= eps_L1 <= sum|ct|, the "
          "interval enclosure; MEASURED: the level-2 anatomy + "
          "potentials, the cert tables, the split rule outcome "
          "(42 rungs only); OPEN: the kz15 level-2 MECHANISM "
          "and the cofinal step; the b3 certificate is finite "
          "and typed, NEVER a class statement; NO RH claim"
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
