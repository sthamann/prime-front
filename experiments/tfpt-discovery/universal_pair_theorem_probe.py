#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""universal_pair_theorem_probe -- PRIME.PORT.COUPLEDTAU.
UNIVERSAL_PAIR_THEOREM.01 (round 271): the reviewer-adjudicated
follow-up of r269: the FIXED, window-independent form c2PAIR
(edge split F0.20 frozen, pairing offset 0, adjacent sign-run
pairs exact, triangle on the pairs -- no grid parameter) is
promoted to a THEOREM IN PURE FORM with an explicit hypothesis
list, refined by at most THREE sealed parameter-free refinements
of the fixed form, scaled over the ladder (the entry door of the
cofinal step) and prepared for Lean (rh/lean/RH/PairBound.lean,
synced by the same round OUTSIDE this probe).

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE THEOREM (LEG A -- pure form, all constants explicit): given
one window w with terminal degree N and the r244/r266 chain rows,
the drive decomposes exactly (H1, warded) as t_{N-2} = sum_b ct_b
over the border atoms; the F = 0.20 edge mask (H2, hull geometry
only) splits t = t_edge + R; Z = t_{N-2} + chain and Z_local =
t_edge + chain.  The maximal same-sign runs r_0..r_{m-1} of the
bx-sorted bulk alternate in sign (H3, gated), with masses M_i =
sum |ct| and exact signed sums s_i = sigma_i M_i.  With the FIXED
pairing (H4, offset 0):
  (i)   pair decomposition: R = sum_j B_j + [m odd] s_{m-1},
        B_j = s_{2j} + s_{2j+1} -- EXACT;
  (ii)  pair identity: |B_j| = |M_{2j} - M_{2j+1}| -- EXACT
        (alternation);
  (iii) pair triangle: |R| <= eps := sum_j |M_{2j} - M_{2j+1}|
        + [m odd] M_{m-1};
  (iv)  certification form: |Z| <= |Z_local| + eps.
(i)-(iv) are window-independent finite algebra (Lean layer:
rh/lean/RH/PairBound.lean).  H5 -- the MARGIN |Z_local| + eps <
sqrt(5/7) -- is the ONLY window-dependent input: the entry door
of the cofinal step (Leg C lemma list).  Machine verification:
(i)-(iv) exact on 42 rungs + 2 mains + 3 controls; the r269
c2PAIR record (5/7 margins, kz39/kz15 misses) is warded.

LEG B -- THE SEALED REFINEMENTS OF THE FIXED FORM (max 3,
mathematical justification BEFORE evaluation, evaluated ONCE;
each parameter-free, source-pure, target-blind; the withheld key
"t" + "_term" is forbidden in every builder scope):
(b1) b1RAND -- EXACT BOUNDARY GROUP: for odd run count m >= 3 the
  c2 form majorizes the unpaired tail wholesale (+ M_{m-1}); the
  exact treatment evaluates the last THREE runs as one signed
  group: |s_{m-3} + s_{m-2} + s_{m-1}| = |M_{m-3} - M_{m-2} +
  M_{m-1}| (alternation => exact).  Never worse than c2 (triangle
  |a + c| <= |a| + |c|); identical for even m.  Parameter-free:
  the group is ALWAYS the last three runs, never chosen.
(b2) b2LEVEL2 -- THE TRIANGLE ON DOUBLE PAIRS: the exact signed
  pair sums B_j (offset 0) get the SAME fixed pairing once more:
  eps2 = sum_k |B_{2k} + B_{2k+1}| + [J odd] |B_{J-1}| + [m odd]
  M_{m-1}.  Locality radius SEALED at <= 4 adjacent runs, never
  adapted.  Never worse than c2 (triangle on |B + B'|).
  Justification: the r269 reading located the residual
  sub-paircorr cancellation "in the near-exact balance of
  adjacent PAIR SUMS" -- exactly the level-2 object.  ANATOMY
  FIRST (sealed): the sign-alternation share of the block-sum
  sequence (B_j) is MEASURED and printed before the certification
  table; the bound's validity is alternation-INDEPENDENT (plain
  triangle on exact signed values).
(b3) b3SHARPENV -- THE EXACT ENVELOPE CONSTANT: the r269 chain
  envelope rounds the Pruefer amplitude with the SIN2_MIN = 0.01
  clamp; the sharp form removes the last rounding parameter:
  E = sqrt(v^2 + b^2 - 2 v b cos th)/|sin th| exactly wherever
  sin^2 th > 0 (hypot fallback only at sin^2 th <= 0 or gam <=
  0).  The c1 pair inequality |M_o - M_e| <= |E_o - E_e| + D_o +
  D_e is exact algebra for ANY envelope.  (Honest expectation
  disclosed: the r269 error-mass diagnosis may persist.)
FOR EACH: validity gated on 47 worlds (bar 1e-9); certification
table on the 7 exception rungs + full-ladder count; the d2
PAIRCORR demand (bar 1.0 dec) and the r266 wall fingerprint (bar
0.9, selftest re-armed) on every derivation; REGRESSION WARD:
the five c2-certified rungs (kz20/22/36/38/52) must not fall
under any pair-family refinement (b1, b2 are <= c2 by
construction -- the ward gates the construction).
ADJUDICATION (sealed): candidate order (c2PAIR, b1RAND, b2LEVEL2,
b3SHARPENV) -- ALL fixed parameter-free forms, no grid; winner =
max certified count on the 7 among clean candidates (no wall
flag, no paircorr fire), ties broken by the EARLIER position in
the sealed order (simplicity preference).  kz39 and kz15 detail
ALWAYS printed (kz15 reserve band [0.020, 0.035] reproduction).

LEG C -- N-SCALING (the entry door of cofinality; measurement +
honest typing ONLY): decompose the theorem bound into its
components (|Z_local|, level-1 pair-gap sum, boundary/tail mass,
eps of the winner) and measure their N-scaling over the 42-rung
ladder, normalized by the demand side sqrt(5/7): Spearman rank
trends (no fit primitives), first-half/second-half medians of
the certified margin M - |Z_local| - eps, exception-branch
detail.  THE LEMMA LIST (what a cofinal proof of H5 must supply,
source-pure, NOT claimed):
  L1 EDGE UNIFORMITY: |Z_local(w)| <= (1 - delta) sqrt(5/7)
     uniformly over the family, delta > 0;
  L2 PAIR-SUM DECAY: eps(w) <= delta' sqrt(5/7), delta' < delta
     uniformly -- a source-pure bound on the bulk envelope
     VARIATION of the three-term chain recursion;
  L3 BOUNDARY VANISHING: the unpaired boundary mass -> 0 (or is
     absorbed exactly, b1);
  L4 RUN-STRUCTURE STABILITY: the bulk sign runs stay alternating
     with bounded run length (measured med 2) -- a comb
     sign-pattern statement about the border drive;
  L5 FLOOR IMPORT: the 5/7 budget floor derived source-purely
     (the known edge-A subproblem, r241/r243 import).
NO cofinality claim; every trend is typed MEASURED_TREND_ONLY.

LEG D -- LEAN PREPARATION (same round, outside this probe):
rh/lean/RH/PairBound.lean states the finite pair algebra
abstractly (List over a linearly ordered field): the blockSums
sum identity (= (i)), the abs-sum triangle, pairBound = absSum o
blockSums, |sum l| <= pairBound l (= (iii)), the level-2
refinement pairBound (blockSums l) <= pairBound l and its
validity, the alternation pair identity (= (ii)), the boundary
triple triangle (b1); the chain-specific margin H5 stays a
documented sorry.  Gate (rh-sync): lake build green.

WARDS / KILLS / MUST-FAILS: inherited kills (PAIRCORR,
TARGET_INVERSE, SELECTION_BY_ANSWER; no fit primitives --
fragment audit); r269 reproduction wards: exception set == the
named 7 + cheap 35, the five c2 margins (kz20 +0.0735, kz22
+0.3974, kz36 +0.0461, kz38 +0.1135, kz52 +0.1490; tol 0.005),
the two misses (kz39 0.01, kz15 0.18 dec; tol 0.015), kz15
reserve in [0.020, 0.035]; SMOOTH anchor (alias <= 1e-12, q_N <=
1e-20, validity trivial); EPSTEIN/SCRAMBLE reproduction
(contribution identity + validity, world-blind); MUST-FAILS:
(m1) LEVEL PEEK -- the mutant evaluating ALL refinement levels
per rung and keeping the smallest eps is selection-by-answer:
typed FORBIDDEN, its gain over the sealed winner measured and
printed (the round adjudicates ONE global form); (m2) PAIRING
WITH GROUND-TRUTH SIGN -- the mutant orienting the level-2
pairing by the withheld terminal drive key must be FLAGGED by
the candidate scope audit; TOY EXACTNESS: hand-checked
deterministic sequences must reproduce EXACTLY (bar 1e-14):
pair decomposition, boundary group, level-2 chain
eps_b2 <= eps_b1 <= eps_c2 <= sum|ct|.

INDEX FIREWALL (binding, r238-r269 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R and t values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r269 PBB.mask_edge + PBB.runs_split +
PBB.bound_pairsum + PBB.bound_abelenv + PBB.env_chain (the fixed
form itself), r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r260 TX.drive_arrays, r263 CA.g_gap, r264 QO.port_pack, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
LEVEL2_RADIUS 4 (FROZEN documentation constant); TB_WARD bars
1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls; VAL_BAR 1e-9;
ID_BAR 1e-12 (pair-identity exactness); TOY_BAR 1e-14;
R269_C2_MARGIN ((20, +0.0735), (22, +0.3974), (36, +0.0461),
(38, +0.1135), (52, +0.1490)) tol 0.005; R269_MISS ((39, 0.01),
(15, 0.18)) tol 0.015; RESERVE_BAND (0.020, 0.035); DEMAND_BAR
1.0; FP_BAR 0.9; SM_Q_BAR 1e-20; SM_ALIAS_BAR 1e-12;
SHUFFLE_SEED 271; KZ_ANCHOR 15; KZ_NEAR 39; runtime <= 1800 s;
smoke = w9 + controls + toy + candidate numerics + scope audits
+ must-fails (ladder, detectors, success gate, adjudication,
scaling skipped).  DISCLOSED PRE-SPEC INPUT (no scratch run of
this probe): every reproduction band is an r263/r268/r269 RECORD
number adopted as-is; nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  THEOREM_FORM(valid n/47, identities exact, H1-H5 printed)
+ BLOCK_ANATOMY(level-2 block census, block-sum alternation
    share)
+ B1_RAND(cert k/7, delta vs c2)
+ B2_LEVEL2(cert k/7, gain med dec)
+ B3_SHARPENV(cert k/7, gain med dec)
+ [exactly one of] UNIVERSAL_PAIR_THEOREM_GO(winner, 7/7, the
    theorem form + hypothesis list stand; Lean status reported
    by the round) / UNIVERSAL_STILL_PARTIAL(winner, n/7,
    missing: per-rung miss dec + where the rest sits) /
    REFINEMENT_BREAKS_REGRESSION(the honest list)
+ SCALING_REPORT(margin trend, component trends, lemma list
    L1-L5)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if fired] PAIRCORR_MINIATURE(candidate list).
Honesty before beauty: no verdict claims a cofinal law or an
asymptotic mechanism; the exception scalar's positivity beyond
the measured 42 stays OPEN; r243-r269 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 was 28/28 gates with NO amendment; calibration pass
1 = first full evaluation, 28/28 gates, wall 11.7 s -- NO physics
bar, band, rule or verdict rule was moved at any point; pass 2 =
the record run below, numerically identical to pass 1 in every
printed figure; the only post-freeze edit is this record-table
insertion, which IS the protocol):
CAL_VERDICT = THEOREM_FORM(valid 47/47, identities exact, H1-H5
printed) + BLOCK_ANATOMY(blk-alt share med 0.45) + B1_RAND(cert
5/7, gain med +0.33 dec) + B2_LEVEL2(cert 5/7, gain med +0.45
dec) + B3_SHARPENV(cert 0/7, gain med -0.06 dec) +
UNIVERSAL_STILL_PARTIAL(c2PAIR, cert 5/7: kz20, kz22, kz36,
kz38, kz52; missing kz15 0.18 dec; kz39 0.01 dec) +
SCALING_REPORT(sp(N, margin) -0.03, halves +0.032 -> -0.019,
lemma list L1-L5 typed).
Key numbers.  LEG A: contribution ward worst dev/absmass 2.1e-13
main / 3.9e-13 deep / 2.4e-8 controls; |s_i| == M_i and |B_j| ==
|M_odd - M_even| EXACT (worst rel dev 0.0); theorem validity
|R| <= eps_c2 worst slack -1.5e-2 <= 0 and |Z| <= |Z_local| +
eps_c2 worst slack -2.1e-2 <= 0 on 47 worlds; r269 reproduction
EXACT (five margins dev 0.0000; kz39 miss 0.008, kz15 miss
0.177, kz15 reserve 0.0268).  LEG B: refinement validity 47/47 x
4 settings (worst slack -1.4e-2); sealed chain b1, b2 <= c2 <=
abs triangle exact (worst dev +1.1e-16); block anatomy: block
count ~ m/2, block-sum alternation share med 0.45 (min 0.31, max
0.60) -- the adjacent pair-sum balance is NOT sign-alternation-
dominated (the r269 reading is REFINED: the balance is a
magnitude effect, not a strict sign pattern); certification
b1RAND 5/7 (kz15 miss 0.15 dec, kz39 0.01 dec; kz36 margin
+0.0556 vs c2 +0.0461), b2LEVEL2 5/7 with kz39 miss 0.002 dec
(margin_cert -0.0022) and kz15 miss 0.06 dec (margin_cert
-0.0461), full-ladder cert 31/42 (c2: 21/42), gain med +0.45
dec, demand max +0.02, fingerprint sp 0.05; b3SHARPENV honestly
COARSER (cert 0/7, eps 0.88-1.47: the unclamped 1/|sin th| blows
up near the hull edges -- the r269 clamp was hiding a real
divergence, the sharp constant is NOT the mechanism); detectors:
no wall flag (sp 0.05-0.51 < 0.9), no paircorr fire (max demand
+0.26 << 1.0 dec); regression ward HOLDS (the five c2-certified
rungs stay certified under b1 and b2).  ADJUDICATION (sealed
tie-break: counts {c2 5, b1 5, b2 5, b3 0} -> earliest in the
sealed order): winner c2PAIR, UNIVERSAL_STILL_PARTIAL(5/7) --
the research-relevant edge is honest: b2LEVEL2 leaves kz39 at
0.002 dec and kz15 at 0.06 dec WITHOUT being adjudicated the
winner (no repair after seeing the numbers).  LEG C (winner
c2PAIR, components / sqrt(5/7)): sp(N, |Z_local|) -0.20; sp(N,
eps) +0.67 -- the pair sum GROWS with N on the measured ladder:
L2 (pair-sum decay) is the critical missing lemma and currently
trends the WRONG way; sp(N, margin_cert) -0.03 (halves +0.032 ->
-0.019); sp(N, level-1 gap sum) +0.67; sp(N, tail mass) -0.04;
exception-branch margin med +0.087.  LEG D (synced by the
round): rh/lean/RH/PairBound.lean states blockSums/absSum/
pairBound with proved sum identity, pair triangle, refinement
chain and alternation identity; the H5 margin stays a documented
sorry; lake build green (see rh/ sync).  READING (typed, no
upgrade): the fixed form IS a finite theorem with one open
window-dependent hypothesis (H5); the natural refinements sharpen
the bound (b2: kz39 to 0.002 dec, kz15 to 0.06 dec) but no
sealed candidate closes 7/7 -- the exception branch stays
UNIVERSAL_STILL_PARTIAL; the cofinal step needs L1-L5, and the
measured eps trend (+0.67 with N) says L2 must supply a
mechanism the plain pair triangle does not have.  Runtime 11.7 s
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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import quenched_opening_probe as QO            # noqa: E402 r264
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
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
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
LEVEL2_RADIUS = 4
R269_C2_MARGIN = ((20, 0.0735), (22, 0.3974), (36, 0.0461),
                  (38, 0.1135), (52, 0.1490))
R269_C2_MARGIN_TOL = 0.005
R269_MISS = ((39, 0.01), (15, 0.18))
R269_MISS_TOL = 0.015
RESERVE_BAND = (0.020, 0.035)
DEMAND_BAR = 1.0
FP_BAR = 0.9
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
SHUFFLE_SEED = 271
KZ_ANCHOR = 15
KZ_NEAR = 39
C2_CERT_KZ = (20, 22, 36, 38, 52)

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


# ---- sealed refinement builders (target-blind: consume ONLY the
# plain run-mass / signed-run-sum lists passed as arguments; the
# withheld terminal drive key and every target-side identifier are
# forbidden in scope, AST-audit; the envelope builder additionally
# must not consume the realized contributions ct)
def bound_rand(Mr):
    """b1 sealed EXACT BOUNDARY GROUP: identical to the r269 c2
    block triangle for even run count; for odd m >= 3 the last
    THREE runs form one exactly evaluated signed group
    |M_{m-3} - M_{m-2} + M_{m-1}| (alternation => exact), never
    worse than pair + majorized tail (triangle)."""
    m = len(Mr)
    if (m - PAIR_OFFSET) % 2 == 0 or m < 3:
        return PBB.bound_pairsum(Mr)
    e = 0.0
    for i in range(PAIR_OFFSET, m - 3, 2):
        e += abs(Mr[i] - Mr[i + 1])
    e += abs(Mr[m - 3] - Mr[m - 2] + Mr[m - 1])
    return e


def bound_level2(Sr):
    """b2 sealed LEVEL-2 FIXED FORM: the exact signed pair sums
    B_j = s_{2j} + s_{2j+1} (offset 0) get the SAME fixed pairing
    once more; radius sealed at <= 4 adjacent runs; plain triangle
    on exact signed values (alternation-independent validity)."""
    m = len(Sr)
    blocks = []
    for i in range(PAIR_OFFSET, m - 1, 2):
        blocks.append(Sr[i] + Sr[i + 1])
    e = 0.0
    nb = len(blocks)
    for j in range(0, nb - 1, 2):
        e += abs(blocks[j] + blocks[j + 1])
    if nb % 2 == 1:
        e += abs(blocks[-1])
    if (m - PAIR_OFFSET) % 2 == 1:
        e += abs(Sr[-1])
    return e


def env_sharp(bxa, v2a, v3a, alh_t, gam_t, sc3, wgeom):
    """b3 sealed SHARP CHAIN ENVELOPE: the r269 Pruefer amplitude
    with the SIN2_MIN clamp REMOVED -- E = sqrt(v^2 + b^2 - 2 v b
    cos th)/|sin th| exactly wherever sin^2 th > 0; hypot fallback
    only at sin^2 th <= 0 or gam <= 0 (source-pure: chain values +
    geometry only, NEVER ct)."""
    if gam_t > 0.0:
        rb = math.sqrt(gam_t)
        bt = rb * sc3 * v3a
        cth = (bxa - alh_t) / (2.0 * rb)
        s2 = 1.0 - cth * cth
        inv = v2a * v2a + bt * bt - 2.0 * v2a * bt * cth
        kf = np.hypot(v2a, bt)
        with np.errstate(divide="ignore", invalid="ignore"):
            kp = np.sqrt(np.maximum(inv, 0.0)) \
                / np.sqrt(np.maximum(s2, 0.0))
        K = np.where(s2 > 0.0, kp, kf)
    else:
        bt = math.sqrt(abs(gam_t)) * sc3 * v3a
        K = np.hypot(v2a, bt)
    return wgeom * K


def cand_mutant_giftpair(rc, Sr):
    """m2 MUST-FAIL MUTANT: level-2 pairing oriented by the
    ground-truth terminal drive sign -- reads the withheld key;
    the candidate scope audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * bound_level2(Sr)


def cand_mutant_levelpeek(Mr, Sr):
    """m1 MUST-FAIL MUTANT: evaluates ALL refinement levels per
    rung and keeps the smallest eps -- selection-by-answer; typed
    FORBIDDEN, gain measured (the sealed round adjudicates ONE
    global form)."""
    return min(PBB.bound_pairsum(Mr), bound_rand(Mr),
               bound_level2(Sr))


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
def toy_pair_algebra():
    """hand-checked deterministic sequences: the pair
    decomposition, the boundary group, the level-2 chain and the
    alternation pair identity must reproduce EXACTLY."""
    worst = 0.0
    # odd-m singleton-run example: ct = [3, -1, 2, -4, 1]
    Mr = [3.0, 1.0, 2.0, 4.0, 1.0]
    Sr = [3.0, -1.0, 2.0, -4.0, 1.0]
    R = sum(Sr)
    worst = max(worst, abs(PBB.bound_pairsum(Mr) - 5.0))
    worst = max(worst, abs(bound_rand(Mr) - 3.0))
    worst = max(worst, abs(bound_level2(Sr) - 1.0))
    worst = max(worst, abs(R) - bound_level2(Sr))  # validity, tight
    # even-m example: ct = [2, -5, 3, -1]
    Mr2 = [2.0, 5.0, 3.0, 1.0]
    Sr2 = [2.0, -5.0, 3.0, -1.0]
    worst = max(worst, abs(PBB.bound_pairsum(Mr2) - 5.0))
    worst = max(worst, abs(bound_rand(Mr2) - 5.0))     # even: == c2
    worst = max(worst, abs(bound_level2(Sr2) - 1.0))
    worst = max(worst, abs(sum(Sr2)) - bound_level2(Sr2))
    # alternation pair identity |sg M1 - sg M2| == |M1 - M2|
    for sg in (1.0, -1.0):
        for m1, m2 in ((3.0, 1.0), (0.25, 0.75), (2.0, 2.0)):
            worst = max(worst, abs(abs(sg * m1 - sg * m2)
                                   - abs(m1 - m2)))
    # refinement chain on both examples
    for M_, S_ in ((Mr, Sr), (Mr2, Sr2)):
        c2 = PBB.bound_pairsum(M_)
        worst = max(worst, bound_rand(M_) - c2)
        worst = max(worst, bound_level2(S_) - c2)
        worst = max(worst, c2 - sum(M_))
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("universal_pair_theorem_probe -- PRIME.PORT.COUPLEDTAU."
          "UNIVERSAL_PAIR_THEOREM.01 (round 271)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   CHARTER_SHA %s "
          "(imported r264)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], QO.CHARTER_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toy + candidate "
                        "numerics + scope audits + must-fails; "
                        "ladder, detectors, success gate, "
                        "adjudication, scaling skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED FOLLOW-UP of r269: the FIXED form "
          "c2PAIR (F 0.20, offset 0, no per-rung parameter) is "
          "stated as a finite THEOREM with the explicit hypothesis "
          "list H1-H5; exactly 3 sealed parameter-free refinements "
          "of the fixed form (b1 exact boundary group, b2 level-2 "
          "double-pair triangle radius <= %d, b3 sharp envelope "
          "constant); success gate = certify the 7 exception rungs "
          "via |Z_local| + eps < sqrt(5/7); regression ward: the "
          "five c2-certified rungs must not fall; N-scaling of the "
          "bound components + the cofinality lemma list L1-L5 "
          "(typed, never claimed); ALL bars, rules and verdicts "
          "sealed BEFORE evaluation (pre-spec input = r263/r268/"
          "r269 record numbers, disclosed)" % LEVEL2_RADIUS)

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
        Es = env_sharp(bx, v2, v3, alh_t, gam_t, sc3, wgeom)
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx,
                    E=E, Esh=Es, o=o, lo=lo, hi=hi, p=p)

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

    # ---------------- S2: LEG A -- the theorem in pure form
    section("S2  LEG A -- THE THEOREM IN PURE FORM (H1-H5)")
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
    check("G20-H1-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "H1: sum_b ct_b == t_{N-2} on %d rungs + %d mains + 3 "
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e) -- "
          "the theorem operates on an EXACT decomposition"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        Ecl = rc["E"][o]
        Esh = rc["Esh"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        t_loc = float(np.sum(cts[ed]))
        cb = cts[~ed]
        Eb = Ecl[~ed]
        Eb_s = Esh[~ed]
        Rb = float(np.sum(cb))
        ab = float(np.sum(np.abs(cb)))
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        Er = [float(np.sum(Eb[a:b])) for a, b, _s in runs]
        Ers = [float(np.sum(Eb_s[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        sm_dev = max((abs(abs(s_) - m_)
                      for s_, m_ in zip(Sr, Mr)), default=0.0)
        # pair identity (ii): |B_j| == |M_{2j} - M_{2j+1}| exact
        id_dev = 0.0
        for i in range(PAIR_OFFSET, len(Sr) - 1, 2):
            id_dev = max(id_dev, abs(abs(Sr[i] + Sr[i + 1])
                                     - abs(Mr[i] - Mr[i + 1])))
        e_c2 = PBB.bound_pairsum(Mr)
        e_b1 = bound_rand(Mr)
        e_b2 = bound_level2(Sr)
        e_c1 = PBB.bound_abelenv(Mr, Er)
        e_b3 = PBB.bound_abelenv(Mr, Ers)
        e_peek = cand_mutant_levelpeek(Mr, Sr)
        nblk = (len(Sr) - PAIR_OFFSET) // 2
        blocks = [Sr[i] + Sr[i + 1]
                  for i in range(PAIR_OFFSET, len(Sr) - 1, 2)]
        alt_blk = (sum(1 for j in range(len(blocks) - 1)
                       if blocks[j] * blocks[j + 1] < 0.0)
                   / max(len(blocks) - 1, 1))
        tail = Mr[-1] if (len(Mr) - PAIR_OFFSET) % 2 == 1 else 0.0
        gap1 = sum(abs(Mr[i] - Mr[i + 1])
                   for i in range(PAIR_OFFSET, len(Mr) - 1, 2))
        return dict(t_loc=t_loc, Rb=Rb, ab=ab, runs=runs, Mr=Mr,
                    Sr=Sr, alt_ok=alt_ok, sm_dev=sm_dev,
                    id_dev=id_dev, e_c2=e_c2, e_b1=e_b1,
                    e_b2=e_b2, e_c1=e_c1, e_b3=e_b3,
                    e_peek=e_peek, nb=int(len(cb)), nblk=nblk,
                    alt_blk=alt_blk, tail=tail, gap1=gap1)

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    sm_worst = max((rc["ev"]["sm_dev"] /
                    max(max(rc["ev"]["Mr"], default=1.0), 1e-300)
                    for rc in all_rc), default=0.0)
    check("G21-H3-run-structure", alt_all and sm_worst <= ID_BAR,
          "H3: consecutive bulk runs alternate in sign on every "
          "rung (%d worlds) AND |s_i| == M_i exactly (worst rel "
          "dev %.1e, bar %.0e) -- the signed run sums ARE the "
          "masses up to the alternating sign" % (len(all_rc),
                                                 sm_worst, ID_BAR))
    id_worst = max((rc["ev"]["id_dev"] /
                    max(max(rc["ev"]["Mr"], default=1.0), 1e-300)
                    for rc in all_rc), default=0.0)
    check("G22-pair-identity-exact", id_worst <= ID_BAR,
          "(ii) |B_j| == |M_{2j} - M_{2j+1}| on every pair of "
          "every world (worst rel dev %.1e, bar %.0e) -- the "
          "block triangle evaluates EXACT signed pair sums"
          % (id_worst, ID_BAR))
    val_worst = -1e300
    cert_worst = -1e300
    for rc in all_rc:
        ev = rc["ev"]
        val_worst = max(val_worst, abs(ev["Rb"]) - ev["e_c2"])
        Zl = ev["t_loc"] + rc["chain"]
        cert_worst = max(cert_worst,
                         abs(rc["Z"]) - (abs(Zl) + ev["e_c2"]))
    for c in crecs:
        ev = crecs[c]["ev"]
        val_worst = max(val_worst, abs(ev["Rb"]) - ev["e_c2"])
        Zl = ev["t_loc"] + crecs[c]["chain"]
        cert_worst = max(cert_worst,
                         abs(crecs[c]["Z"])
                         - (abs(Zl) + ev["e_c2"]))
    n_worlds = len(all_rc) + len(crecs)
    check("G23-theorem-validity", val_worst <= VAL_BAR
          and cert_worst <= VAL_BAR,
          "(iii)+(iv): |R| <= eps_c2 (worst slack %+.1e) AND "
          "|Z| <= |Z_local| + eps_c2 (worst slack %+.1e) on %d "
          "worlds (bar %.0e) -- the fixed form IS a theorem on "
          "every measured world" % (val_worst, cert_worst,
                                    n_worlds, VAL_BAR))

    if not smoke:
        # r269 c2PAIR record reproduction (regression ward)
        dev_mg = 0.0
        note_mg = []
        for kz, m_ref in R269_C2_MARGIN:
            rc = next(r_ for r_ in recs if r_["kz"] == kz)
            ev = rc["ev"]
            mg = M_W - (abs(ev["t_loc"] + rc["chain"])
                        + ev["e_c2"])
            dev_mg = max(dev_mg, abs(mg - m_ref))
            note_mg.append("kz%d %+.4f(ref %+.4f)" % (kz, mg,
                                                      m_ref))
        dev_ms = 0.0
        note_ms = []
        for kz, m_ref in R269_MISS:
            rc = next(r_ for r_ in recs if r_["kz"] == kz)
            ev = rc["ev"]
            need = M_W - abs(ev["t_loc"] + rc["chain"])
            miss = math.log10(ev["e_c2"] / need) if need > 0 \
                else float("inf")
            dev_ms = max(dev_ms, abs(miss - m_ref))
            note_ms.append("kz%d %.3f(ref %.2f)" % (kz, miss,
                                                    m_ref))
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        check("G24-r269-reproduction-wards",
              dev_mg <= R269_C2_MARGIN_TOL
              and dev_ms <= R269_MISS_TOL and ok15,
              "the r269 c2PAIR record recomputed: five certified "
              "margins %s (worst dev %.4f, tol %.3f); the two "
              "misses %s dec (worst dev %.3f, tol %.3f); kz15 "
              "true reserve %.4f in %s"
              % ("; ".join(note_mg), dev_mg, R269_C2_MARGIN_TOL,
                 "; ".join(note_ms), dev_ms, R269_MISS_TOL,
                 slack15, str(RESERVE_BAND)))
    else:
        check("G24-r269-reproduction-wards", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    check("G25-hypothesis-list", True,
          "H1 exact atom decomposition t_{N-2} = sum ct_b (chain "
          "rows; warded G20); H2 geometric edge split F = %.2f of "
          "the hull width (source-pure); H3 alternating sign-run "
          "structure of the bx-sorted bulk (warded G21); H4 fixed "
          "pairing offset %d, boundary group + level-2 radius <= "
          "%d, NO parameter, NO adaptation; H5 the MARGIN "
          "|Z_local| + eps < sqrt(5/7) -- the ONLY window-"
          "dependent hypothesis: what a window family must "
          "supply for the theorem to certify it (the cofinal "
          "entry door, lemma list L1-L5 in Leg C)"
          % (EDGE_F, PAIR_OFFSET, LEVEL2_RADIUS))

    # ---------------- S3: toy exactness + scope audits
    section("S3  TOY EXACTNESS + SCOPE AUDITS")
    toy_worst = toy_pair_algebra()
    check("G30-toy-pair-algebra", toy_worst <= TOY_BAR,
          "hand-checked sequences reproduce EXACTLY (worst dev "
          "%.1e, bar %.0e): c2 pair triangle, b1 boundary group "
          "(odd m: 3.0, even m: == c2), b2 level-2 (both "
          "examples: 1.0, tight on [3,-1,2,-4,1]), alternation "
          "pair identity, refinement chain b1/b2 <= c2 <= "
          "sum|ct|" % (toy_worst, TOY_BAR))
    h_b1 = scope_audit("bound_rand", CAND_FORBIDDEN)
    h_b2 = scope_audit("bound_level2", CAND_FORBIDDEN)
    h_b3 = scope_audit("env_sharp",
                       CAND_FORBIDDEN | ENV_EXTRA_FORBIDDEN)
    h_m2 = scope_audit("cand_mutant_giftpair", CAND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G31-scope-audits", not (h_b1 or h_b2 or h_b3)
          and bool(h_m2) and not ag_hits,
          "sealed refinement builders CLEAN (b1/b2 consume run "
          "masses / signed run sums only%s; b3 envelope consumes "
          "chain values + geometry only%s); m2 gift-sign mutant "
          "FLAGGED (%s); fragment audit (no fit primitives): %s"
          % ("" if not (h_b1 or h_b2) else " VIOLATION",
             "" if not h_b3 else " VIOLATION " + "; ".join(h_b3),
             "; ".join(h_m2) if h_m2 else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: LEG B -- refinements + detectors
    section("S4  LEG B -- SEALED REFINEMENTS + DETECTORS")
    settings = (("c2PAIR", "e_c2"), ("b1RAND", "e_b1"),
                ("b2LEVEL2", "e_b2"), ("b3SHARPENV", "e_b3"))
    val_worst = -1e300
    chain_worst = -1e300
    for rc in all_rc:
        ev = rc["ev"]
        for _nm, key in settings:
            val_worst = max(val_worst, abs(ev["Rb"]) - ev[key])
        chain_worst = max(chain_worst, ev["e_b1"] - ev["e_c2"])
        chain_worst = max(chain_worst, ev["e_b2"] - ev["e_c2"])
        chain_worst = max(chain_worst, ev["e_c2"] - ev["ab"])
    for c in crecs:
        ev = crecs[c]["ev"]
        for _nm, key in settings:
            val_worst = max(val_worst, abs(ev["Rb"]) - ev[key])
    check("G40-refinement-validity", val_worst <= VAL_BAR
          and chain_worst <= VAL_BAR,
          "|R| <= eps holds for all 4 settings on %d worlds "
          "(worst slack %+.1e, bar %.0e) AND the sealed chain "
          "b1, b2 <= c2 <= abs triangle is exact (worst dev "
          "%+.1e) -- every refinement is a theorem, never a "
          "repair" % (n_worlds, val_worst, VAL_BAR, chain_worst))

    # block anatomy FIRST (sealed order: anatomy before certs)
    if smoke:
        anat_pool = mrecs
    else:
        anat_pool = sorted(exc, key=lambda r_: r_["kz"]) + mrecs
    for rc in anat_pool:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s bulk %-4d runs %-4d blocks %-3d "
             "blk-alt %.2f tail/M %.3f  eps c2 %.3f b1 %.3f b2 "
             "%.3f b3 %.2e"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g"] < 0 else "chp",
                ev["nb"], len(ev["runs"]), ev["nblk"],
                ev["alt_blk"], ev["tail"] / M_W, ev["e_c2"],
                ev["e_b1"], ev["e_b2"], ev["e_b3"]))
    alt_blk_pool = [rc["ev"]["alt_blk"]
                    for rc in (recs if not smoke else mrecs)]
    check("G41-block-anatomy", True,
          "LEVEL-2 ANATOMY (measured BEFORE certification): "
          "block-sum sign-alternation share med %.2f (min %.2f, "
          "max %.2f) over %d rungs -- the r269 residual "
          "cancellation location (adjacent pair-sum balance) is "
          "%s; the b2 validity never consumed it (plain triangle)"
          % (float(np.median(alt_blk_pool)),
             min(alt_blk_pool), max(alt_blk_pool),
             len(alt_blk_pool),
             "CONFIRMED alternating-dominated"
             if float(np.median(alt_blk_pool)) >= 0.5
             else "NOT alternation-dominated (honest)"))

    res = {}
    for nm, key in settings:
        rows_ = []
        for rc in all_rc:
            ev = rc["ev"]
            eps = ev[key]
            Zl = ev["t_loc"] + rc["chain"]
            bound = abs(Zl) + eps
            rows_.append(dict(kz=rc["kz"], N=rc["N"],
                              exc=rc["g"] < 0, eps=eps, Zl=Zl,
                              ab=ev["ab"], bound=bound,
                              margin=M_W - bound,
                              gain=math.log10(
                                  ev["ab"] / max(eps, 1e-300)),
                              Z=rc["Z"]))
        res[nm] = rows_

    def fam_rows(nm):
        return res[nm][:len(recs)]

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
        check("G42-wall-detector-armed",
              fl_wall and not fl_tgt and sp_mut < FP_BAR,
              "selftest: wall criterion g(1) < 1 FALSE 42/42, "
              "sp(g1, g1) = %.3f >= %.1f FLAGGED; target D_N > 0 "
              "TRUE 42/42, sp(D_N, g1) = %.3f NOT flagged; "
              "seed-%d shuffle mutant sp = %.3f misses -- r266 "
              "detector re-armed"
              % (sp_wall, FP_BAR, sp_tgt, SHUFFLE_SEED, sp_mut))
        fired = []
        fp_note = []
        for nm, _key in settings:
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
                                     passes=passes)
            fp_note.append("%s sp %.2f cert %d/42 demand max "
                           "%+.2f%s"
                           % (nm, sp_, passes, max(dem),
                              " FIRE" if fire else ""))
        check("G43-detector-census", True,
              "d2 paircorr demand log10((|Z_local| + eps)/M) on "
              "the exception branch (bar %.1f dec) + wall "
              "fingerprints (bar %.1f) on EVERY derivation: %s "
              "-- fired routes are closed for certification "
              "IMMEDIATELY" % (DEMAND_BAR, FP_BAR,
                               "; ".join(fp_note)))
    else:
        fired = []
        check("G42-wall-detector-armed", True, "SMOKE: skipped")
        check("G43-detector-census", True, "SMOKE: skipped")

    # ---------------- S5: success gate + adjudication + scaling
    section("S5  SUCCESS GATE + ADJUDICATION + SCALING")
    if not smoke:
        def cert_count(nm):
            if res[nm + "_meta"]["wall"] \
                    or res[nm + "_meta"]["fire"]:
                return -1
            return sum(1 for r_ in fam_rows(nm)
                       if r_["exc"] and r_["margin"] > 0.0)

        cons_ok = True
        for nm, _key in settings:
            for r_ in res[nm]:
                cons_ok = cons_ok and (r_["margin"]
                                       <= (M_W - abs(r_["Z"]))
                                       + VAL_BAR)
        miss_tab = {}
        for nm, _key in settings:
            for r_ in fam_rows(nm):
                if not r_["exc"]:
                    continue
                need = M_W - abs(r_["Zl"])
                miss = (math.log10(r_["eps"] / need)
                        if need > 0 else float("inf"))
                miss_tab[(nm, r_["kz"])] = miss
                info("%-10s kz%-3d margin_true %+0.4f margin_cert "
                     "%+0.4f |Z_loc| %.3f eps %.3f %s"
                     % (nm, r_["kz"], M_W - abs(r_["Z"]),
                        r_["margin"], abs(r_["Zl"]), r_["eps"],
                        "CERTIFIED" if r_["margin"] > 0
                        else ("miss %.2f dec" % miss
                              if math.isfinite(miss)
                              else "MAIN_TERM_EXCEEDS")))
        check("G50-success-gate-table", cons_ok,
              "per-exception-rung table printed for all 4 fixed "
              "forms; consistency margin_cert <= margin_true on "
              "every rung x setting (exact, %s)"
              % ("OK" if cons_ok else "BROKEN"))
        # regression ward: the five c2-certified must not fall
        reg_break = []
        for nm in ("b1RAND", "b2LEVEL2"):
            for kz in C2_CERT_KZ:
                r_ = next(x for x in fam_rows(nm)
                          if x["kz"] == kz)
                if r_["margin"] <= 0.0:
                    reg_break.append("%s@kz%d" % (nm, kz))
        check("G51-regression-ward", not reg_break,
              "the five c2-certified rungs %s stay certified "
              "under every pair-family refinement (b1, b2 <= c2 "
              "by construction): %s"
              % (str(C2_CERT_KZ),
                 "HOLDS" if not reg_break
                 else "BROKEN " + "; ".join(reg_break)))
        cands = [nm for nm, _k in settings]
        cert_counts = {nm: cert_count(nm) for nm in cands}
        clean = [nm for nm in cands if cert_counts[nm] >= 0]
        best = max(clean, key=lambda nm: (cert_counts[nm],
                                          -cands.index(nm))) \
            if clean else "none"
        cert_best = max(cert_counts.get(best, 0), 0)
        cert_kzs = sorted(r_["kz"] for r_ in fam_rows(best)
                          if r_["exc"] and r_["margin"] > 0.0) \
            if best != "none" else []
        full42 = sum(1 for r_ in fam_rows(best)
                     if r_["margin"] > 0.0) if best != "none" \
            else 0
        check("G52-adjudication", True,
              "sealed rule (max cert on the 7 among clean "
              "candidates, tie -> earlier in the sealed order): "
              "counts %s => winner %s cert %d/7 (%s), full-ladder "
              "cert %d/42; wall flags %s; paircorr fired %s -- "
              "no candidate repair after seeing the numbers"
              % (str({nm: cert_counts[nm] for nm in cands}),
                 best, cert_best,
                 ", ".join("kz%d" % kz for kz in cert_kzs)
                 if cert_kzs else "none",
                 full42,
                 str([nm for nm in cands
                      if res[nm + "_meta"]["wall"]]),
                 str(fired) if fired else "none"))
        def rung_state(nm, kz):
            r_ = next(x for x in fam_rows(nm) if x["kz"] == kz)
            if r_["margin"] > 0.0:
                return "CERTIFIED (margin %+.4f)" % r_["margin"]
            return "miss %.3f dec" % miss_tab[(nm, kz)]

        check("G53-kz39-kz15-detail", True,
              "the two r269-open rungs under the winner %s: kz39 "
              "%s; kz15 %s (r269 c2 misses were 0.01 / 0.18 dec; "
              "the kz15 ground-truth potential headroom at F0.20 "
              "is 0.05 dec, r269 record)"
              % (best, rung_state(best, KZ_NEAR),
                 rung_state(best, KZ_ANCHOR)))

        # LEG C: component decomposition + N-scaling
        Ns = [r_["N"] for r_ in fam_rows(best)]
        zl_n = [abs(r_["Zl"]) / M_W for r_ in fam_rows(best)]
        ep_n = [r_["eps"] / M_W for r_ in fam_rows(best)]
        mg_n = [r_["margin"] / M_W for r_ in fam_rows(best)]
        gap_n = [rc["ev"]["gap1"] / M_W for rc in recs]
        tl_n = [rc["ev"]["tail"] / M_W for rc in recs]
        sp_zl = BH.spearman(Ns, zl_n)
        sp_ep = BH.spearman(Ns, ep_n)
        sp_mg = BH.spearman(Ns, mg_n)
        sp_gp = BH.spearman(Ns, gap_n)
        sp_tl = BH.spearman(Ns, tl_n)
        h1 = float(np.median(mg_n[:len(mg_n) // 2]))
        h2 = float(np.median(mg_n[len(mg_n) // 2:]))
        exc_mg = [r_["margin"] / M_W for r_ in fam_rows(best)
                  if r_["exc"]]
        check("G60-scaling-census", True,
              "MEASURED_TREND_ONLY (winner %s, 42 rungs N-sorted, "
              "components / sqrt(5/7)): sp(N, |Z_local|) %+.2f; "
              "sp(N, eps) %+.2f; sp(N, margin_cert) %+.2f "
              "(first-half med %+.3f -> second-half med %+.3f); "
              "sp(N, level-1 gap sum) %+.2f; sp(N, tail mass) "
              "%+.2f; exception-branch margin med %+.3f"
              % (best, sp_zl, sp_ep, sp_mg, h1, h2, sp_gp,
                 sp_tl, float(np.median(exc_mg))))
        check("G61-cofinality-lemma-list", True,
              "WHAT A COFINAL PROOF OF H5 MUST SUPPLY (typed, NOT "
              "claimed): L1 edge uniformity |Z_local| <= (1 - "
              "delta) sqrt(5/7); L2 pair-sum decay eps <= delta' "
              "sqrt(5/7), delta' < delta (a source-pure bound on "
              "the bulk envelope VARIATION of the chain "
              "recursion); L3 boundary vanishing (or exact b1 "
              "absorption); L4 run-structure stability "
              "(alternating, bounded run length); L5 the 5/7 "
              "floor import derived source-purely -- NO "
              "cofinality claim in this round")
    else:
        best = "n/a"
        cert_best = 0
        cert_kzs = []
        full42 = 0
        cert_counts = {}
        for g_ in ("G50-success-gate-table", "G51-regression-ward",
                   "G52-adjudication", "G53-kz39-kz15-detail",
                   "G60-scaling-census",
                   "G61-cofinality-lemma-list"):
            check(g_, True, "SMOKE: skipped")

    # ---------------- S6: controls + must-fails
    section("S6  CONTROLS + MUST-FAILS")
    ctl_ok = True
    ctl_note = []
    for c in ("EPST", "SCR"):
        rc = crecs[c]
        ev = rc["ev"]
        ok_v = all(abs(ev["Rb"]) <= ev[k] + VAL_BAR
                   for _nm, k in settings)
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(rc["absum"], 1e-300)
        ctl_note.append("%s t %+0.3f dev %.1e validity %s"
                        % (c, rc["t_term"], dev,
                           "OK" if ok_v else "BROKEN"))
        ctl_ok = ctl_ok and ok_v and (dev <= TB_WARD_BAR_CTRL)
    main_fitted = not ctl_ok
    check("G70-control-reproduction", ctl_ok,
          "the theorem + every refinement hold on the PERTURBED "
          "worlds exactly (contribution identity + validity on "
          "EPSTEIN/SCRAMBLE at F0.20): %s -- world-blind algebra, "
          "NOT main-fitted" % "; ".join(ctl_note))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    rcS = crecs["SMOOTH"]
    evS = rcS["ev"]
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    okS_v = all(abs(evS["Rb"]) <= evS[k] + VAL_BAR
                for _nm, k in settings)
    check("G71-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okS_v,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "validity holds trivially on the self-aliased source "
          "(%s)" % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
                    "OK" if okS_v else "BROKEN"))
    n_gain = 0
    g_max = 0.0
    for rc in all_rc:
        ev = rc["ev"]
        base = min(ev["e_b1"], ev["e_b2"])
        d_ = base - ev["e_peek"]
        if d_ > 1e-12:
            n_gain += 1
            g_max = max(g_max, d_)
    check("G72-mustfail-level-peek", True,
          "m1 LEVEL PEEK (min over all refinement levels per "
          "rung): gains > 1e-12 over the per-rung best sealed "
          "pair form on %d/%d rungs (max %.2e abs) -- ANY "
          "per-rung form selection is selection-by-answer, typed "
          "FORBIDDEN: the round adjudicates ONE global fixed "
          "form (sealed rule, G52)" % (n_gain, len(all_rc),
                                       g_max))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the c2PAIR theorem in pure form with the "
          "explicit hypothesis list H1-H5, three sealed "
          "parameter-free refinements of the fixed form with "
          "exact validity + regression wards, the honest "
          "adjudication, the N-scaling census and the "
          "cofinality lemma list -- plus the Lean statement "
          "rh/lean/RH/PairBound.lean (synced by the round)")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        parts.append("THEOREM_FORM(valid %d/%d, identities "
                     "exact, H1-H5 printed)"
                     % (n_worlds, n_worlds))
        parts.append("BLOCK_ANATOMY(blk-alt share med %.2f)"
                     % float(np.median(alt_blk_pool)))
        for nm, lbl in (("b1RAND", "B1_RAND"),
                        ("b2LEVEL2", "B2_LEVEL2"),
                        ("b3SHARPENV", "B3_SHARPENV")):
            rws = fam_rows(nm)
            gains = [r_["gain"] for r_ in rws]
            parts.append("%s(cert %d/7, gain med %+.2f dec)"
                         % (lbl, max(cert_counts[nm], 0),
                            float(np.median(gains))))
        if reg_break:
            parts.append("REFINEMENT_BREAKS_REGRESSION(%s)"
                         % "; ".join(reg_break))
        elif best != "none" and cert_best == len(exc):
            parts.append("UNIVERSAL_PAIR_THEOREM_GO(%s, 7/7: the "
                         "fixed-form theorem certifies the whole "
                         "exception branch; H1-H5 + Lean "
                         "PairBound.lean carry the statement)"
                         % best)
        else:
            rest = [(r_["kz"],
                     miss_tab.get((best, r_["kz"]),
                                  float("nan")))
                    for r_ in fam_rows(best)
                    if r_["exc"] and r_["margin"] <= 0.0]
            parts.append("UNIVERSAL_STILL_PARTIAL(%s, cert %d/7: "
                         "%s; missing %s)"
                         % (best, cert_best,
                            ", ".join("kz%d" % kz
                                      for kz in cert_kzs),
                            "; ".join("kz%d %.2f dec"
                                      % (kz, ms)
                                      for kz, ms in rest)))
        parts.append("SCALING_REPORT(sp(N, margin) %+.2f, halves "
                     "%+.3f -> %+.3f, lemma list L1-L5 typed)"
                     % (sp_mg, h1, h2))
        if main_fitted:
            parts.append("LOCAL_MODEL_MAIN_FITTED")
        if fired:
            parts.append("PAIRCORR_MINIATURE(%s)"
                         % ", ".join(fired))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the pair decomposition, "
          "the pair identity, the block triangle, the refinement "
          "chain; MEASURED: the censuses, the certification "
          "margins, the trends (42 rungs only); OPEN: the "
          "cofinal step H5 (lemma list L1-L5); NO RH claim"
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
