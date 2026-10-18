#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""minimal_firewall_probe -- PRIME.PORT.WALL.MINIMAL_FIREWALL.01
(round 276): the DOSE-RESPONSE CURVE OF THE ARITHMETIC -- from
binary to graduated to minimal.  The r273 mechanism round measured
that gamma_true is PERTURBATION-INSENSITIVE (generic root-scale
cancellation) while EVERY tested surgery kills the free-prefix
positivity (flip degrees 33-43 for P1/P2/P4, 66-101 for the
mildest family surgery P3; MAIN holds ALL windows); the v956 scale
fixes the control level: EPSTEIN/SCRAMBLE/SMOOTH die at 25/21/27
= 0.11..0.15 of the w9 free window N_w = 184 while MAIN exhausts
the ENTIRE free moment window.  REVIEWER ADJUDICATION (the new
firewall lane): the prime structure does NOT produce the
cancellation -- it keeps the small remainder ON THE RIGHT SIDE;
the question of the lane: WHICH MINIMAL EULER STRUCTURE PRESERVES
THE PREFIX POSITIVITY?  This round measures the WALL SURVIVAL
DEPTH as a function of surgery DOSE, from the r273 binary regime
(theta 0.25..1.0, wall always dead) down to the MINIMAL surgery
(ONE neighbor swap / ONE atom jitter / ONE sign-pair exchange).
NOT a proof round: no certificate, no bound, no H5 progress, no
mechanism claim -- MEASUREMENT ONLY.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r244/r273 machinery imported verbatim): per world the
exact h-chain of the signed defect measure mutilde = mu - nu
(BH.bord_chain, the r244 scaled recursion; sign chain sg_h) --
the WALL SURVIVAL DEPTH is nf = first degree n with sg_h < 0
(None = the world survives its ENTIRE free window), normalized
s = nf / N_w in [0, 1] (s = 1 for survivors; N_w = builder
depth = the free-moment-window cap of v956).  TWO exact world
channels, both gated bitwise against BH.wpack at the identity:
(ch-1) COMB channel: (uu, mm) -> PIK.build_rung(kz, comb) ->
  grid density -> folded +/- zones -> BH.bord_chain (for the
  comb surgeries P1/P2/P3);
(ch-2) DENSITY channel: the signed grid density d_arm of the
  UNPERTURBED window, surgered directly, then folded ->
  BH.bord_chain (for the sign/magnitude surgeries B1/B2 -- the
  signature and magnitude fields of the world live on the grid,
  not on the comb, whose weights are one-signed).
Atom classification WITHOUT prime functions: r254 world-blind
labels via ODG.base_exp (pure integer root extraction, admission
bar 1e-9); AST firewall (no zetazero/nzeros/isprime/primerange/
grampoint) holds.

LEG A -- THE DOSE LADDERS (sealed; five surgeries x six doses x
three windows; seeds pinned, fully deterministic; seed = 276000
+ P*100000 + dose*10000 + rep*1000 + win*10):
DOSES: SINGLE (the minimal operation, 9 pinned replicates --
  disclosed: single-op outcomes are position-dependent, the
  extra replicates map the spread) + theta in (0.02, 0.05, 0.10,
  0.15, 0.25) (3 pinned replicates each -- the r273 regime
  starts at 0.25; this ladder refines toward zero).
SURGERIES (dose semantics per surgery, conservation EXACT):
(P1_SWAP) minimal-reach assignment surgery: n_pair = max(1,
  round(theta n/2)) DISJOINT u-adjacent weight transpositions
  (greedy disjoint selection over a seeded permutation of the
  n-1 adjacencies); SINGLE = ONE neighbor swap.  DISCLOSED
  reparametrization of r273-P1: the exchange REACH is pinned at
  the minimum (adjacent), the dose is the COUNT -- the r273
  block law B = n^theta is degenerate below theta 0.1 (B = 1 =
  identity).  PRESERVED: positions bitwise, weight multiset
  bitwise.  DESTROYED: weight<->position assignment at neighbor
  scale, dose-many places.
(P2_JIT) support jitter: u_j -> u_j + amp * g_j * U[-1, 1] on
  ALL atoms with amp = theta (fraction of the local nn gap g_j
  -- the r273-P2 amplitude lever refined toward zero); SINGLE =
  ONE seed-chosen atom jittered at amp = 1.0 (one atom, one
  slot).  PRESERVED: weights bitwise, |du_j| <= amp g_j (gated).
  DESTROYED: support arithmetic at amplitude amp.
(P3_FAM) Euler-family decoupling (r273-P3 verbatim logic):
  nsel = round(theta n_KHI) of the KHI atoms (k >= 2) swap
  weights with the nearest-in-u atom of a DIFFERENT family;
  SINGLE = exactly ONE such swap; nsel = 0 stages are typed
  IDENTITY_DOSE (eff = 0).  PRESERVED: positions bitwise,
  weight multiset bitwise, unselected within-family structure.
  DESTROYED: SAMEP coherence, dose-many echoes.
(B1_SIGN) NEW -- signature surgery on the grid density: nsel =
  max(2, round(theta n_nz)) nonzero grid entries selected, their
  SIGNS permuted among the selection (magnitude field |d| stays
  AT POSITION); SINGLE = ONE +/- pair sign exchange.  PRESERVED:
  |d| array bitwise, sign multiset (p/q census) exact.
  DESTROYED: the signature-position pattern -- signature
  separated from magnitude.
(B2_MAG) NEW -- magnitude surgery on the grid density: nsel =
  max(2, round(theta n_nz)) nonzero entries selected, their
  MAGNITUDES permuted among the selection (sign field stays AT
  POSITION); SINGLE = ONE grid-adjacent magnitude exchange.
  PRESERVED: sign array bitwise, |d| multiset bitwise.
  DESTROYED: the magnitude-position pattern -- magnitude
  separated from signature.
WINDOWS (sealed selection rule, structural census disclosed as
the only pre-spec input): w9 (the v956 anchor window, N_w = 184,
comb 70 atoms / 16 KHI, grid 734 signed entries 526+/208-) + the
min-N frame-A rung (kz18, N_w = 142) + the frame-A rung with N_w
closest to 400 (kz55, N_w = 388).  CONSERVATION GATES exact per
perturbed world (EVERY world); DOSE ACCOUNTING gate: the number
of changed entries never exceeds the nominal dose cap (2 n_pair
/ n_at resp. 1 / 2 nsel / nsel / nsel); theta = 0 returns
bitwise-identical arrays for all five surgeries (gated).

LEG B -- THE MEASUREMENT + PROPERTY RANKING: per stage (surgery
x dose x window) the replicate depths s_r; stage stats = median
/ min / max depth + survivor count.  WALL TOLERANCE per surgery
(w9 map): tol_P = mean of the stage median depths over the six
doses; PROPERTY_RANKING = ascending tol (the property whose
destruction costs the most depth per dose ranks FIRST as
wall-carrier).  The two new surgeries separate SIGNATURE (B1)
from MAGNITUDE (B2); P1/P2/P3 carry the r273 assignment /
support / family axes into the small-dose regime.

LEG C -- THE MINIMALITY MAP (delivery object; sealed rules
frozen BEFORE evaluation, w9 primary):
STAGE CLASS: a stage is MIDDLE iff CTRL_HI < s_med < NEAR_FULL
  (CTRL_HI = 0.20 = the v956 control band 0.11..0.15 plus
  slack; NEAR_FULL = 0.90).
SURGERY CLASS (per surgery on w9): P_THRESHOLD iff s_med(SINGLE)
  <= CTRL_HI (one op collapses to control level); P_TOLERANT
  iff min over all doses s_med >= NEAR_FULL; P_GRADED iff
  s_med(SINGLE) >= NEAR_FULL and min s_med < NEAR_FULL;
  P_INTERMEDIATE otherwise.
LAW FIT (per surgery, deterministic, no fit primitives): deficit
  D(theta) = 1 - s_med over the five theta stages with eff > 0
  and D > DEF_MIN = 0.005; iff >= LAW_MIN = 4 such stages the
  exponent b = halves log-slope of D vs theta (D ~ theta^b);
  else typed NO_LAW(sparse).  Monotonicity sp(theta, s_med)
  reported.
CONTINUUM vs JUMP (sealed): JUMP iff NO w9 stage is MIDDLE;
  CONTINUUM iff >= K_CONT = 3 w9 stages are MIDDLE;
  SPARSE_MIDDLE otherwise.
V956 PLACEMENT: the minimal w9 stage depth vs the control band;
  CONTROL_TOUCHED iff any w9 stage s_med <= CTRL_HI.
N-TRANSPORT (typed classification, not a gate): Spearman between
  the 30 w9 stage medians and the same stages on kz18 / kz55;
  MAP_TRANSPORTS iff sp >= 0.5 on both rungs, else
  WINDOW_SPECIFIC.
FIREWALL HYPOTHESIS (typed TASK_FORMULATION_ONLY): "the wall is
  carried by [the top-ranked property combination]; loss of it
  at dose theta costs survival depth by law f" -- quantified
  from the measured map, falsifiable, NO mechanism claim.

LEG D -- WARDS / MUST-FAILS: identity wards (comb channel
reproduces BH.wpack bitwise in rho and nf on ALL three windows;
theta = 0 bitwise for all five surgeries); control anchors
EPSTEIN/SCRAMBLE/SMOOTH flips re-derived 25/21/27 (w9) -- the
"wrong arithmetic" anchor points of the map; MAIN survives all
three windows (baseline s = 1); label admission <= 1e-9 on all
windows; conservation + dose accounting on EVERY perturbed
world; mp COUNTER-CHECK (dps 40, the sealed anti-noise ward):
the f64 flip degree of the EARLIEST-flipping w9 SINGLE world of
every surgery is re-derived by an mp signed-Stieltjes sign chain
(exact agreement demanded), one surviving w9 SINGLE world and
MAIN w9 are mp-confirmed over the full f64 chain domain (degrees
<= N_w - 1; amendment a1 below), the boundary degree N_w on MAIN
is a sealed BOUNDARY ward (the v956 record n_flip = N_w + 0 must
reproduce at dps 40), EPSTEIN to its flip; run1/run2 determinism
(pinned seeds).  MUST-FAILS (each
loud): (m1) MASS SURGERY -- a mutant scaling a theta-fraction of
comb weights by 1.15 AND a density mutant scaling |d| by 1.02
must be CAUGHT by the conservation gates; (m2) DOSE MUTANT -- a
mutant applying 2x the claimed P1 dose must be CAUGHT by the
dose-accounting cap; (m3) FLIP-NOISE MUTANT -- a mutant flip
report (EPSTEIN nf - 3) must be REJECTED by the mp counter-check
(the detector is not trusted on f64 alone at the borderline);
(m4) GIFT SURGERY -- a mutant orienting itself by the withheld
wall outcome (nf) must be FLAGGED by the AST scope audit (the
five sealed surgeries audit clean).  STOP LIST (anti-gates,
binding): NO pair hierarchies, NO splits, NO s-flows, NO
precision escalation beyond the sealed dps-40 counter-check;
fragment audit (no polyfit/curve_fit/lstsq/minimize) inherited.

INDEX FIREWALL (binding, r238-r273 discipline): w = window (kz),
N_w = builder depth, n = chain degree; the surgery functions
consume (uu, mm / d_arm, theta, seed, labels) ONLY (AST scope
audit against the withheld truth-side set incl. the wall outcome
nf); ground truth (nf, sg_h chains) enters MEASUREMENT and gates
only; no zero/prime oracles anywhere (AST firewall); labels via
ODG.base_exp = r254 integer root extraction, world-blind.
MACHINERY IMPORTED VERBATIM: r244 BH.wpack + BH.bord_chain +
BH.spearman, v881 PIK.build_rung + PIK.folded_measure +
PIK.lambda_eps, r243 PB.smooth_comb, r254 ODG.base_exp, core
build_window/frame_a_zones READ-ONLY.

SEALED CONSTANTS: MAIN window 9; RUNG windows (18, 55); controls
w9 EPSTEIN/SCRAMBLE(seed 1)/SMOOTH, flips 25/21/27; THETAS
(0.02, 0.05, 0.10, 0.15, 0.25); REPS 3; REPS_SINGLE 9; SEED_BASE
276000; CTRL_HI 0.20; NEAR_FULL 0.90; K_CONT 3; DEF_MIN 0.005;
LAW_MIN 4; SP_TRANSPORT 0.5; NINT_BAR 1e-9; JIT_TOL 1e-12;
MASS_MUT_MIN 1e-3; MP_DPS 40; SHUFFLE n/a (no trend axis this
round); runtime <= 1800 s; smoke = censuses + identity wards +
theta-0 gates + conservation battery + dose accounting + label
census + base_exp toy + scope audits + m1 + m2 (ladders, map,
anchors, mp, m3 skipped).  DISCLOSED PRE-SPEC INPUT: the window
selection censuses (N_w, comb size, KHI count, grid census) and
ONE machinery scoping pass (identity bitwise, controls 25/21/27,
single-op feasibility, mp cost) -- no verdict-relevant band was
tuned; every class boundary above is a v956/r273 record number
or a round constant fixed before the first full evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] FIREWALL_THRESHOLD(all surgeries collapse to
    control level at SINGLE dose -- the wall is a discrete
    arithmetic all-or-nothing phenomenon) / FIREWALL_GRADED(
    every surgery graded or tolerant -- the wall is
    perturbation-tolerant up to measured dose) / FIREWALL_LAW(
    mixed classes; per-surgery laws)
+ PROPERTY_RANKING(surgeries ascending by wall tolerance)
+ CONTINUUM_VS_JUMP(JUMP / CONTINUUM / SPARSE_MIDDLE, middle
    census)
+ V956_PLACEMENT(min stage depth vs the 0.11..0.15 control band)
+ N_TRANSPORT(MAP_TRANSPORTS / WINDOW_SPECIFIC, sp per rung)
+ FIREWALL_HYPOTHESIS(quantified, TASK_FORMULATION_ONLY).
Honesty before beauty: every depth is MEASURED on three finite
windows; no verdict claims a cofinal law, a mechanism theorem or
H5 progress; survival-depth loss under surgery is an
EXPERIMENTAL localization of the wall-carrying properties, not a
proof that any property suffices; r243-r273 stand.

DISCLOSED CALIBRATION AMENDMENTS (before freeze; the surgery
definitions, conservation gates, class rules, verdict rules and
every physics band never moved):
(a1) MP WARD DOMAIN: calibration pass 1 ran the survivor/MAIN
  mp chains to N_w -- ONE degree past the f64 chain domain
  (rows 0..N_w-1) -- and the mp chain correctly reported the
  v956 BOUNDARY flip AT N_w = 184 (n_flip = N_w + 0, the r228
  record, reproduced at dps 40); the ward now compares
  like-for-like (upto N_w - 1) and the boundary degree is kept
  as its own sealed BOUNDARY ward (MAIN mp flip == N_w).  A
  measurement-domain fix on a ward, not a physics band; every
  interior flip check of pass 1 already agreed EXACTLY.

RECORD TABLES (frozen from calibration pass 2 = the first full
evaluation AFTER the disclosed amendment; 25/25 gates; the
record insertion below is the only post-freeze edit, which IS
the protocol; run1/run2 identical up to WALL):
CAL_VERDICT = FIREWALL_LAW(P1_SWAP GRADED b +0.59 / P2_JIT
GRADED b +0.04 / P3_FAM INTERMEDIATE b +1.09 / B1_SIGN GRADED
b +0.26 / B2_MAG GRADED b +0.38) + PROPERTY_RANKING(P2_JIT
0.343 < B2_MAG 0.389 < B1_SIGN 0.536 < P1_SWAP 0.621 < P3_FAM
0.700 ascending tolerance) + CONTINUUM_VS_JUMP(CONTINUUM, 48/90
MIDDLE stages, w9 19/30) + V956_PLACEMENT(min stage depth 0.109
at B2_MAG theta 0.15, CONTROL_TOUCHED) + N_TRANSPORT(
MAP_TRANSPORTS, sp +0.84 kz18 / +0.86 kz55) +
FIREWALL_HYPOTHESIS(see reading).
Key numbers (w9 primary map; stage = median depth s_med over
replicates [min..max], surv = survivors/reps):
  P1_SWAP  SINGLE 1.000 [0.75..1.00] surv 5/9 | 0.02 0.886 |
           0.05 0.565 | 0.10 0.359 | 0.15 0.560 | 0.25 0.359
  P2_JIT   SINGLE 0.957 [0.83..1.00] surv 2/9 | 0.02 0.250 |
           0.05 0.255 | 0.10 0.207 | 0.15 0.196 | 0.25 0.196
  P3_FAM   SINGLE 0.875 [0.28..0.93] surv 0/9 | 0.02 IDENTITY |
           0.05 0.935 | 0.10 0.511 | 0.15 0.603 | 0.25 0.277
  B1_SIGN  SINGLE 0.973 [0.48..1.00] surv 4/9 | 0.02 0.755 |
           0.05 0.337 | 0.10 0.375 | 0.15 0.505 | 0.25 0.272
  B2_MAG   SINGLE 1.000 [0.61..1.00] surv 5/9 | 0.02 0.647 |
           0.05 0.342 | 0.10 0.125 | 0.15 0.109 | 0.25 0.109
Monotonicity sp(theta, s_med): P1 -0.82 / P2 -0.87 / P3 -0.80 /
B1 -0.60 / B2 -0.97 (all decreasing).  MIDDLE census 48/90
stages (w9 19/30) -- a genuine CONTINUUM of survival depths
between control level and full survival; the v956 control level
(0.11..0.15) is REACHED inside the theta <= 0.25 ladder: B2_MAG
0.109-0.125 at theta 0.10-0.25, P2_JIT 0.196 at theta 0.15-0.25
(w9); on the deep window kz55 P2/B2 sit at 0.04-0.14 across the
ladder.  Single ops land at 0.88-1.00 median (position-
dependent minima 0.28-0.83).  N-transport sp +0.84/+0.86 -- the
map is window-portable.  ANCHORS: EPSTEIN/SCRAMBLE/SMOOTH
25/21/27 exact; MAIN survives all three windows (depth 1.0).
WARDS: conservation + dose accounting EXACT on 360/360
perturbed worlds; label admission worst 9.8e-16; mp counter-
checks 9/9 exact (earliest-flip singles 138/152/51/89/113 ==
f64, survivor + MAIN clean over degrees <= N_w - 1, BOUNDARY
flip 184 == N_w, EPSTEIN 25); m1 comb mutant CAUGHT (7.7e-2
rel) + density mutant CAUGHT by both gates (2.0e-3 rel); m2
dose mutant CAUGHT (14 changed > cap 8); m3 flip-noise mutant
REJECTED by mp (25 != 22); m4 gift surgery FLAGGED (nf@once);
five surgeries audit clean; fragment audit clean.
READING (typed MEASUREMENT_ONLY, no mechanism claim): the wall
is NOT an all-or-nothing firewall -- the dose-response is a
measured CONTINUUM: single minimal operations (one neighbor
swap, one sign exchange, one atom jitter) typically leave the
wall at depth 0.88-1.00, far ABOVE the v956 control level, with
position-dependent lethal exceptions (earliest-flip singles at
51-152 of 184; the scoping earliest-atom swap at 34 = the r249
anchor); the collapse to control level happens WITHIN the
graduated ladder (theta 0.10-0.25) and the deficit laws are
SHALLOW and saturating (b +0.04..+1.09) -- no critical dose, an
immediate-onset graded degradation.  PROPERTY_RANKING (the
round's surprise, refining r273): SUPPORT EXACTNESS is the most
wall-critical property -- P2_JIT at amplitude 0.02 of the LOCAL
ATOM GAP already costs 3/4 of the depth (0.250), and MAGNITUDE
placement (B2, tol 0.389) ranks SECOND, while the r273-mildest
FAMILY coherence stays mildest per-op too (P3, tol 0.700) and
the sign pattern sits mid-field (B1, 0.536): the wall reads the
POSITIONS and the MAGNITUDE FIELD of the signed density more
exactly than the family bookkeeping.  FIREWALL_HYPOTHESIS
(TASK_FORMULATION_ONLY, falsifiable): "the wall is carried by
the exact METRIC placement of the source -- support positions
at sub-gap precision and magnitude-position pairing -- with
graded loss D ~ theta^b, b in 0.04..1.09 (immediate onset, fast
saturation), NOT by an all-or-nothing arithmetic switch; any
candidate wall lemma must be quantitatively stable under
family/assignment permutations at small dose but consumes the
metric data exactly"; the position-dependence of single-op
lethality names the follow-up: the u-profile of single-op
influence.  Runtime 9.5 s full / 0.7 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE (records
inserted per protocol; no bar, band, class rule or verdict rule
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

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import offdiag_gram_probe as ODG               # noqa: E402 r254
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
RUNG_KZS = (18, 55)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
THETAS = (0.02, 0.05, 0.10, 0.15, 0.25)
REPS = 3
REPS_SINGLE = 9
SEED_BASE = 276000
CTRL_HI = 0.20
NEAR_FULL = 0.90
K_CONT = 3
DEF_MIN = 0.005
LAW_MIN = 4
SP_TRANSPORT = 0.5
NINT_BAR = 1e-9
JIT_TOL = 1e-12
MASS_MUT_MIN = 1e-3
MP_DPS = 40
SURG_NAMES = ("P1_SWAP", "P2_JIT", "P3_FAM", "B1_SIGN", "B2_MAG")
COMB_SURG = ("P1_SWAP", "P2_JIT", "P3_FAM")
DOSE_LABELS = ("SINGLE",) + THETAS

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


# ------------------------------------------------------ AST audits
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
    return (not bad), ("NO zero/prime oracles; the surgeries consume "
                       "node positions + weights / the grid density + "
                       "r254 integer-root labels ONLY; the wall outcome "
                       "(nf, sg_h) enters MEASUREMENT and gates only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden fit-method families (identifiers only;
    the fragment table is assembled from split strings)."""
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


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld
    truth-side identifier or dict-key string from the sealed set."""
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


PERT_FORBIDDEN = {"t" + "_term", "Z", "St", "rho", "n" + "f",
                  "sg" + "_h", "lg" + "_h", "wp" + "ack",
                  "bord" + "_chain", "margin", "slack2", "C_true"}


# ------------------------------------------------ trend estimators
def halves_slope(Xs, Ys):
    """r272 dyadic log-slope (deterministic): (mean ln Y | second
    half - first half) / (same for ln X) on the X-sorted list."""
    n = len(Xs)
    h = n // 2
    ly = [math.log(max(float(v), 1e-300)) for v in Ys]
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    num = (sum(ly[h:]) / (n - h)) - (sum(ly[:h]) / h)
    den = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    return num / den


# ------------------------------------ the five sealed surgeries
# (source-pure scope, AST-audited: consume uu, mm / d_arm, theta,
#  seed and the world-blind r254 labels ONLY -- no wall outcome)
def local_gaps(uu):
    """per-atom local nearest-neighbor gap of the sorted u
    (endpoints single-sided) -- the sealed P2 jitter scale
    (r273 verbatim)."""
    o = np.argsort(uu, kind="stable")
    us = uu[o]
    d = np.diff(us)
    g = np.empty(len(uu))
    if len(uu) == 1:
        g[:] = 1.0
        return g
    gs = np.empty(len(uu))
    gs[0] = d[0]
    gs[-1] = d[-1]
    if len(uu) > 2:
        gs[1:-1] = np.minimum(d[:-1], d[1:])
    g[o] = gs
    return g


def pert_swap(uu, mm, theta, seed, single):
    """P1_SWAP: n_pair disjoint u-adjacent weight transpositions
    (greedy disjoint selection over a seeded permutation of the
    adjacencies); SINGLE = one neighbor swap; positions and the
    weight multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return uu.copy(), mm.copy()
    n = len(uu)
    npair = 1 if single else max(1, int(round(theta * n / 2.0)))
    rng = np.random.default_rng(seed)
    o = np.argsort(uu, kind="stable")
    used = np.zeros(n, dtype=bool)
    mm2 = mm.copy()
    got = 0
    for s_ in rng.permutation(n - 1):
        if got >= npair:
            break
        if used[s_] or used[s_ + 1]:
            continue
        a_, b_ = o[s_], o[s_ + 1]
        mm2[a_], mm2[b_] = mm2[b_], mm2[a_]
        used[s_] = used[s_ + 1] = True
        got += 1
    return uu.copy(), mm2


def pert_jit(uu, mm, theta, seed, single):
    """P2_JIT: u_j -> u_j + amp g_j U[-1, 1]; amp = theta on ALL
    atoms, SINGLE = one atom at amp = 1.0; weights preserved
    EXACTLY."""
    if theta <= 0.0 and not single:
        return uu.copy(), mm.copy()
    rng = np.random.default_rng(seed)
    g = local_gaps(uu)
    if single:
        j = int(rng.integers(len(uu)))
        du = np.zeros(len(uu))
        du[j] = 1.0 * g[j] * rng.uniform(-1.0, 1.0)
    else:
        du = theta * g * rng.uniform(-1.0, 1.0, len(uu))
    return uu + du, mm.copy()


def pert_fam(uu, mm, theta, seed, ps, ks, single):
    """P3_FAM (r273 verbatim logic): nsel KHI atoms (k >= 2) swap
    weights with the nearest-in-u atom of a DIFFERENT family
    (different primary p); SINGLE = one swap; positions and the
    weight multiset preserved EXACTLY (pure transpositions)."""
    uu2, mm2 = uu.copy(), mm.copy()
    if theta <= 0.0 and not single:
        return uu2, mm2
    n = len(uu)
    cand = np.nonzero(ks >= 2)[0]
    nsel = 1 if single else int(round(theta * len(cand)))
    if nsel == 0:
        return uu2, mm2
    rng = np.random.default_rng(seed)
    sel = np.sort(rng.choice(cand, size=nsel, replace=False))
    for j in sel:
        lo = j - 1
        while lo >= 0 and ps[lo] == ps[j]:
            lo -= 1
        hi = j + 1
        while hi < n and ps[hi] == ps[j]:
            hi += 1
        opts = []
        if lo >= 0:
            opts.append((uu[j] - uu[lo], int(lo)))
        if hi < n:
            opts.append((uu[hi] - uu[j], int(hi)))
        if not opts:
            continue
        part = min(opts)[1]
        mm2[j], mm2[part] = mm2[part], mm2[j]
    return uu2, mm2


def pert_sign(darm, theta, seed, single, nzi):
    """B1_SIGN: signs of nsel selected nonzero grid entries
    permuted among the selection (magnitude field |d| stays AT
    POSITION); SINGLE = one +/- pair sign exchange; |d| array
    bitwise and sign multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return darm.copy()
    sgn = np.sign(darm)
    mag = np.abs(darm)
    rng = np.random.default_rng(seed)
    if single:
        posi = nzi[darm[nzi] > 0]
        negi = nzi[darm[nzi] < 0]
        i = int(posi[rng.integers(len(posi))])
        j = int(negi[rng.integers(len(negi))])
        sgn[i], sgn[j] = sgn[j], sgn[i]
    else:
        nsel = max(2, int(round(theta * len(nzi))))
        sel = rng.choice(nzi, size=nsel, replace=False)
        sgn[sel] = sgn[sel][rng.permutation(nsel)]
    return mag * sgn


def pert_mag(darm, theta, seed, single, nzi):
    """B2_MAG: magnitudes of nsel selected nonzero grid entries
    permuted among the selection (sign field stays AT POSITION);
    SINGLE = one grid-adjacent magnitude exchange; sign array
    bitwise and |d| multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return darm.copy()
    sgn = np.sign(darm)
    mag = np.abs(darm)
    rng = np.random.default_rng(seed)
    if single:
        k = int(rng.integers(len(nzi) - 1))
        i, j = int(nzi[k]), int(nzi[k + 1])
        mag[i], mag[j] = mag[j], mag[i]
    else:
        nsel = max(2, int(round(theta * len(nzi))))
        sel = rng.choice(nzi, size=nsel, replace=False)
        mag[sel] = mag[sel][rng.permutation(nsel)]
    return mag * sgn


def mutant_mass_comb(uu, mm, theta, seed):
    """m1 MUST-FAIL MUTANT (comb): scales a theta-fraction of the
    weights by 1.15 -- the conservation gate must CATCH it."""
    rng = np.random.default_rng(seed)
    mm2 = mm.copy()
    nsel = max(1, int(round(theta * len(mm))))
    sel = rng.choice(len(mm), size=nsel, replace=False)
    mm2[sel] *= 1.15
    return uu.copy(), mm2


def mutant_mass_density(darm, seed):
    """m1 MUST-FAIL MUTANT (density): scales |d| of a random tenth
    of the entries by 1.02 -- the density conservation gates must
    CATCH it."""
    rng = np.random.default_rng(seed)
    d2 = darm.copy()
    sel = rng.choice(len(darm), size=max(1, len(darm) // 10),
                     replace=False)
    d2[sel] *= 1.02
    return d2


def mutant_gift_pert(uu, mm, pack):
    """m4 scope-audit MUST-FAIL MUTANT: a 'surgery' oriented by the
    withheld wall outcome -- the scope audit must FLAG this."""
    s = 1.0 if pack["nf"] is None else -1.0
    return uu.copy(), (mm[::-1].copy() if s < 0.0 else mm.copy())


def dose_cap(kind, theta, single, n_at, n_khi, n_nz):
    """sealed nominal dose caps (changed-entry counts) for the
    dose-accounting gate."""
    if kind == "P1_SWAP":
        return 2 * (1 if single else max(1, int(round(theta * n_at
                                                      / 2.0))))
    if kind == "P2_JIT":
        return 1 if single else n_at
    if kind == "P3_FAM":
        return 2 * (1 if single else int(round(theta * n_khi)))
    nsel = 2 if single else max(2, int(round(theta * n_nz)))
    return nsel


def conserve_comb(kind, uu, mm, uu2, mm2, amp):
    """exact conservation gates (comb channel): P1/P3 positions
    bitwise + sorted weight multiset bitwise; P2 weights bitwise
    + per-atom jitter bound."""
    if kind == "P2_JIT":
        ok_m = bool(np.array_equal(mm2, mm))
        g = local_gaps(uu)
        dev = np.abs(uu2 - uu)
        ok_u = bool(np.all(dev <= amp * g * (1.0 + JIT_TOL) + 1e-300))
        return ok_u and ok_m
    ok_u = bool(np.array_equal(uu2, uu))
    ok_m = bool(np.array_equal(np.sort(mm2), np.sort(mm)))
    return ok_u and ok_m


def conserve_density(kind, d, d2):
    """exact conservation gates (density channel): B1 |d| bitwise
    + sign multiset; B2 sign array bitwise + |d| multiset."""
    if kind == "B1_SIGN":
        ok_a = bool(np.array_equal(np.abs(d2), np.abs(d)))
        ok_s = bool(np.array_equal(np.sort(np.sign(d2)),
                                   np.sort(np.sign(d))))
        return ok_a and ok_s
    ok_s = bool(np.array_equal(np.sign(d2), np.sign(d)))
    ok_a = bool(np.array_equal(np.sort(np.abs(d2)),
                               np.sort(np.abs(d))))
    return ok_s and ok_a


# ------------------------------------------------ world machinery
def window_ctx(kz):
    """per-window context: comb, labels, grid density, folded
    border (smooth), builder depth."""
    b = PIK.build_rung(kz)
    rr = core.build_window(kz)
    uu = np.asarray(rr["uu"], float).copy()
    mm = 2.0 * np.asarray(rr["lam"], float).copy()
    nn = np.round(np.exp(uu)).astype(np.int64)
    dev = float(np.max(np.abs(np.exp(uu) - nn) / nn))
    pk = [ODG.base_exp(int(n)) for n in nn]
    ps = np.array([p for p, _k in pk], dtype=np.int64)
    ks = np.array([k for _p, k in pk], dtype=np.int64)
    sm = PB.smooth_comb(b["alpha"])
    bsm = PIK.build_rung(kz, comb=sm)
    bx, bw, _ = PIK.folded_measure(bsm["d"], bsm["L"], +1.0)
    by, bv, _ = PIK.folded_measure(bsm["d"], bsm["L"], -1.0)
    darm = np.asarray(b["d"], float).copy()
    nzi = np.nonzero(darm)[0]
    return dict(kz=kz, N=int(b["h"]), L=int(b["L"]), uu=uu, mm=mm,
                ps=ps, ks=ks, lab_dev=dev, darm=darm, nzi=nzi,
                bx=bx, bw=bw, by=by, bv=bv,
                n_khi=int(np.sum(ks >= 2)))


def nf_from_density(ctx, d2):
    """wall survival of a (surgered) grid density: fold +/- and run
    the exact r244 bordered h-chain; nf = first sg_h < 0."""
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    rows = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], ctx["N"])
    return next((r["n"] for r in rows if r["sg_h"] < 0), None), \
        (xs, ws, ys, vs)


def nf_from_comb(ctx, u2, m2):
    """wall survival of a (surgered) comb: rebuild the grid density
    via the sealed comb channel, then the density path."""
    bb = PIK.build_rung(ctx["kz"], comb=(u2, m2))
    return nf_from_density(ctx, np.asarray(bb["d"], float))


def apply_surgery(kind, ctx, theta, seed, single):
    """dispatch; returns (nf, changed_count, zones) with the exact
    conservation + dose-accounting results folded in."""
    if kind in COMB_SURG:
        uu, mm = ctx["uu"], ctx["mm"]
        if kind == "P1_SWAP":
            u2, m2 = pert_swap(uu, mm, theta, seed, single)
        elif kind == "P2_JIT":
            u2, m2 = pert_jit(uu, mm, theta, seed, single)
        else:
            u2, m2 = pert_fam(uu, mm, theta, seed, ctx["ps"],
                              ctx["ks"], single)
        amp = 1.0 if (single and kind == "P2_JIT") else theta
        ok = conserve_comb(kind, uu, mm, u2, m2, amp)
        changed = int(np.sum(m2 != mm)) if kind != "P2_JIT" \
            else int(np.sum(u2 != uu))
        nf, zones = nf_from_comb(ctx, u2, m2)
        return nf, ok, changed, zones
    d = ctx["darm"]
    if kind == "B1_SIGN":
        d2 = pert_sign(d, theta, seed, single, ctx["nzi"])
    else:
        d2 = pert_mag(d, theta, seed, single, ctx["nzi"])
    ok = conserve_density(kind, d, d2)
    changed = int(np.sum(d2 != d))
    nf, zones = nf_from_density(ctx, d2)
    return nf, ok, changed, zones


def base_exp_toy():
    """hand-checked base_exp table (exact)."""
    tab = ((2, (2, 1)), (3, (3, 1)), (4, (2, 2)), (5, (5, 1)),
           (8, (2, 3)), (9, (3, 2)), (25, (5, 2)), (27, (3, 3)),
           (32, (2, 5)), (49, (7, 2)), (121, (11, 2)),
           (128, (2, 7)), (243, (3, 5)))
    return all(ODG.base_exp(n) == r for n, r in tab)


# ------------------------------------------------ mp counter-check
def mp_first_flip(zones, upto, dps):
    """mp signed-Stieltjes sign chain (the sealed dps-40 anti-noise
    counter-check): returns the first degree with a negative
    cumulative h-sign, or None if none up to `upto`."""
    import mpmath as mp
    mp.mp.dps = dps
    xs, ws, ys, vs = zones
    X = [mp.mpf(float(v)) for v in xs]
    W = [mp.mpf(float(v)) for v in ws]
    Y = [mp.mpf(float(v)) for v in ys]
    V = [mp.mpf(float(v)) for v in vs]
    qx = [mp.mpf(1)] * len(X)
    qy = [mp.mpf(1)] * len(Y)
    qxm = [mp.mpf(0)] * len(X)
    qym = [mp.mpf(0)] * len(Y)
    Ls = mp.mpf(0)
    Lsm = mp.mpf(0)
    eta = sum(w * a * a for w, a in zip(W, qx)) \
        - sum(v * a * a for v, a in zip(V, qy))
    etam = eta
    sg = 1 if eta > 0 else -1
    if sg < 0:
        return 0
    for n in range(upto):
        alh = (sum(w * x * a * a for w, x, a in zip(W, X, qx))
               - sum(v * y * a * a
                     for v, y, a in zip(V, Y, qy))) / eta
        if n == 0:
            px = [(x - alh) * a for x, a in zip(X, qx)]
            py = [(y - alh) * a for y, a in zip(Y, qy)]
        else:
            ge = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
            fc = mp.e ** (Lsm - Ls)
            px = [(x - alh) * a - ge * fc * am
                  for x, a, am in zip(X, qx, qxm)]
            py = [(y - alh) * a - ge * fc * am
                  for y, a, am in zip(Y, qy, qym)]
        sc = max(max(abs(v) for v in px), max(abs(v) for v in py))
        qxm, qym, etam, Lsm = qx, qy, eta, Ls
        qx = [v / sc for v in px]
        qy = [v / sc for v in py]
        Ls += mp.log(sc)
        eta = sum(w * a * a for w, a in zip(W, qx)) \
            - sum(v * a * a for v, a in zip(V, qy))
        gam = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
        if gam < 0:
            sg = -sg
        if sg < 0:
            return n + 1
    return None


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("minimal_firewall_probe -- PRIME.PORT.WALL."
          "MINIMAL_FIREWALL.01 (round 276)")
    print("SPEC_SHA %s   R244_SHA %s (imported)   R273_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], BH.SPEC_SHA[:16],
             hashlib.sha256(
                 open(os.path.join(HERE, "euler_mechanism_probe.py"),
                      "rb").read()).hexdigest()[:16]))
    print("mode: %s" % ("SMOKE (censuses + identity wards + theta-0 "
                        "gates + conservation battery + dose "
                        "accounting + labels + toy + scope audits + "
                        "m1 + m2; ladders, map, anchors, mp, m3 "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED DOSE-RESPONSE ROUND (no proof, no "
          "certificate, no bound, no mechanism claim): five sealed "
          "surgeries (neighbor SWAP / support JIT / family FAM / "
          "grid SIGN / grid MAG) x doses SINGLE + %s x pinned "
          "replicates (%d ladder / %d single) on windows w%d + %s "
          "against the exact h-chain wall depth s = nf/N_w; classes "
          "THRESHOLD <= %.2f / TOLERANT >= %.2f / GRADED / "
          "INTERMEDIATE and verdicts THRESHOLD/GRADED/LAW + "
          "CONTINUUM-vs-JUMP sealed BEFORE evaluation"
          % (str(THETAS), REPS, REPS_SINGLE, MAIN_KZ, str(RUNG_KZS),
             CTRL_HI, NEAR_FULL))

    # ---------------- S1: censuses + identity wards
    section("S1  CENSUSES + IDENTITY WARDS")
    ctxs = {kz: window_ctx(kz) for kz in (MAIN_KZ,) + RUNG_KZS}
    p_main = {kz: BH.wpack(kz) for kz in ctxs}
    ok_id = True
    id_note = []
    for kz, ctx in ctxs.items():
        nf0, _ = nf_from_comb(ctx, ctx["uu"], ctx["mm"])
        p9i = BH.wpack(kz, base_kw=dict(comb=(ctx["uu"], ctx["mm"])))
        rows0 = BH.bord_chain(*(PIK.folded_measure(ctx["darm"],
                                                   ctx["L"], +1.0)[:2]
                                + PIK.folded_measure(ctx["darm"],
                                                     ctx["L"],
                                                     -1.0)[:2]),
                              ctx["bx"], ctx["bw"], ctx["by"],
                              ctx["bv"], ctx["N"])
        rho0 = np.array([r_["rho"] for r_ in rows0])
        ok_id = ok_id and bool(np.array_equal(rho0,
                                              p_main[kz]["rho"])) \
            and nf0 == p_main[kz]["nf"] \
            and bool(np.array_equal(p9i["rho"], p_main[kz]["rho"]))
        id_note.append("w%d N %d nf %s" % (kz, ctx["N"], str(nf0)))
    check("G10-identity-channels", ok_id,
          "BOTH world channels reproduce BH.wpack BITWISE (rho "
          "array + nf) at the identity on all three windows: %s "
          "-- the surgery channels are exact at dose zero"
          % "; ".join(id_note))
    ok_lab = all(ctx["lab_dev"] <= NINT_BAR for ctx in ctxs.values())
    check("G11-label-admission", ok_lab,
          "r254 world-blind labels: admission worst %.1e (bar "
          "%.0e); censuses: %s"
          % (max(ctx["lab_dev"] for ctx in ctxs.values()), NINT_BAR,
             "; ".join("w%d comb %d KHI %d grid-nz %d (%d+/%d-)"
                       % (kz, len(ctx["uu"]), ctx["n_khi"],
                          len(ctx["nzi"]),
                          int(np.sum(ctx["darm"] > 0)),
                          int(np.sum(ctx["darm"] < 0)))
                       for kz, ctx in ctxs.items())))
    c9 = ctxs[MAIN_KZ]
    ok0 = True
    for kind in COMB_SURG:
        if kind == "P1_SWAP":
            u2, m2 = pert_swap(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                               False)
        elif kind == "P2_JIT":
            u2, m2 = pert_jit(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                              False)
        else:
            u2, m2 = pert_fam(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                              c9["ps"], c9["ks"], False)
        ok0 = ok0 and bool(np.array_equal(u2, c9["uu"])) \
            and bool(np.array_equal(m2, c9["mm"]))
    for kind in ("B1_SIGN", "B2_MAG"):
        fn = pert_sign if kind == "B1_SIGN" else pert_mag
        d2 = fn(c9["darm"], 0.0, SEED_BASE, False, c9["nzi"])
        ok0 = ok0 and bool(np.array_equal(d2, c9["darm"]))
    check("G12-theta0-exact", ok0,
          "theta = 0 returns BITWISE-identical arrays for all five "
          "surgeries -- MAIN is the exact dose origin")
    cons_ok = True
    acc_ok = True
    note = []
    for kind in SURG_NAMES:
        for di, lab in enumerate(DOSE_LABELS):
            single = (lab == "SINGLE")
            th = 0.0 if single else float(lab)
            nf_, okc, chg, _z = apply_surgery(
                kind, c9, th, SEED_BASE + 555 + 17 * di, single)
            cons_ok = cons_ok and okc
            cap = dose_cap(kind, th, single, len(c9["uu"]),
                           c9["n_khi"], len(c9["nzi"]))
            acc_ok = acc_ok and (chg <= cap)
            if lab in ("SINGLE", 0.25):
                note.append("%s@%s chg %d cap %d"
                            % (kind, str(lab), chg, cap))
    check("G13-conservation-battery", cons_ok,
          "w9 conservation battery (5 surgeries x 6 doses): "
          "positions/multisets/sign fields bitwise per surgery "
          "type -- EXACT")
    check("G14-dose-accounting", acc_ok,
          "changed-entry counts <= nominal dose caps on the full "
          "battery; endpoint census: %s" % "; ".join(note))

    # ---------------- S2: toy + scope audits + m1/m2
    section("S2  TOY + SCOPE AUDITS + MUST-FAILS (m1, m2)")
    check("G20-toy-base-exp", base_exp_toy(),
          "hand-checked integer-root table exact: 2/3/4/5/8/9/25/"
          "27/32/49/121/128/243 -> the r254 label machine is "
          "loaded verbatim (no prime oracle)")
    h_p = []
    for fn in ("pert_swap", "pert_jit", "pert_fam", "pert_sign",
               "pert_mag", "local_gaps"):
        h_p.extend(scope_audit(fn, PERT_FORBIDDEN))
    h_g = scope_audit("mutant_gift_pert", PERT_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G21-scope-audits", not h_p and bool(h_g) and not ag_hits,
          "the five sealed surgeries audit CLEAN against the "
          "withheld truth-side set (incl. the wall outcome)%s; the "
          "gift mutant FLAGGED (%s); fragment audit (no fit "
          "primitives): %s"
          % ("" if not h_p else " VIOLATION " + "; ".join(h_p),
             "; ".join(h_g) if h_g else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    u2, m2 = mutant_mass_comb(c9["uu"], c9["mm"], 0.5,
                              SEED_BASE + 99)
    caught1 = not conserve_comb("P1_SWAP", c9["uu"], c9["mm"], u2,
                                m2, 0.5)
    mb1 = abs(float(np.sum(np.sort(m2) - np.sort(c9["mm"])))) \
        / max(float(np.sum(np.abs(c9["mm"]))), 1e-300)
    d2 = mutant_mass_density(c9["darm"], SEED_BASE + 98)
    caught2 = (not conserve_density("B1_SIGN", c9["darm"], d2)) \
        and (not conserve_density("B2_MAG", c9["darm"], d2))
    mb2 = abs(float(np.sum(np.sort(np.abs(d2))
                           - np.sort(np.abs(c9["darm"]))))) \
        / max(float(np.sum(np.abs(c9["darm"]))), 1e-300)
    check("G22-mustfail-mass", caught1 and mb1 >= MASS_MUT_MIN
          and caught2 and mb2 >= MASS_MUT_MIN,
          "m1 MASS SURGERY: comb mutant (1.15x) CAUGHT (multiset "
          "break %.1e) AND density mutant (1.02x on |d|) CAUGHT by "
          "BOTH density gates (break %.1e; bar %.0e rel) -- mass "
          "change cannot pass as a permutation surgery"
          % (mb1, mb2, MASS_MUT_MIN))
    th_m2 = 0.10
    _u3, m3_ = pert_swap(c9["uu"], c9["mm"], 2.0 * th_m2,
                         SEED_BASE + 97, False)
    chg_m2 = int(np.sum(m3_ != c9["mm"]))
    cap_m2 = dose_cap("P1_SWAP", th_m2, False, len(c9["uu"]),
                      c9["n_khi"], len(c9["nzi"]))
    check("G23-mustfail-dose", chg_m2 > cap_m2,
          "m2 DOSE MUTANT (claims theta %.2f, applies %.2f): %d "
          "changed entries > claimed cap %d -- CAUGHT by the "
          "dose-accounting gate" % (th_m2, 2.0 * th_m2, chg_m2,
                                    cap_m2))

    if smoke:
        for g_ in ("G30-control-anchors", "G31-main-baselines",
                   "G40-conservation-full", "G41-map-measured",
                   "G50-dose-map", "G51-law-fits",
                   "G52-continuum-vs-jump", "G53-v956-placement",
                   "G54-n-transport", "G60-mp-counter-checks",
                   "G61-mustfail-flip-noise"):
            check(g_, True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # ---------------- S3: anchors + baselines
        section("S3  CONTROL ANCHORS + MAIN BASELINES")
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrl_defs = (("EPSTEIN", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCRAMBLE", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=PB.smooth_comb(rr9["alpha"]))))
        ctrl = {c: BH.wpack(MAIN_KZ, base_kw=kw)
                for c, kw in ctrl_defs}
        okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
        check("G30-control-anchors", okCf,
              "flips re-derived %s == the sealed 25/21/27 -- the "
              "v956 control level (0.11..0.15 of N_w %d) anchors "
              "the map bottom"
              % (str({c: ctrl[c]["nf"] for c in ctrl}),
                 ctxs[MAIN_KZ]["N"]))
        ok_base = all(p_main[kz]["nf"] is None for kz in ctxs)
        check("G31-main-baselines", ok_base,
              "MAIN survives the FULL free window on all three "
              "windows (nf None; N_w %s) -- depth 1.0 is the map "
              "top" % str([ctxs[kz]["N"] for kz in ctxs]))

        # ---------------- S4: the dose ladders
        n_worlds = len(SURG_NAMES) * (len(THETAS) * REPS
                                      + REPS_SINGLE) * len(ctxs)
        section("S4  THE DOSE LADDERS (%d worlds)" % n_worlds)
        stages = {}
        cons_all = True
        acc_all = True
        borderline = {}
        survivor_sample = None
        for si, kind in enumerate(SURG_NAMES):
            for di, lab in enumerate(DOSE_LABELS):
                single = (lab == "SINGLE")
                th = 0.0 if single else float(lab)
                reps = REPS_SINGLE if single else REPS
                for wi, (kz, ctx) in enumerate(ctxs.items()):
                    nfs = []
                    effs = []
                    for rep in range(reps):
                        seed = (SEED_BASE + si * 100000
                                + di * 10000 + rep * 1000 + wi * 10)
                        nf_, okc, chg, zones = apply_surgery(
                            kind, ctx, th, seed, single)
                        cons_all = cons_all and okc
                        cap = dose_cap(kind, th, single,
                                       len(ctx["uu"]), ctx["n_khi"],
                                       len(ctx["nzi"]))
                        acc_all = acc_all and (chg <= cap)
                        nfs.append(nf_)
                        effs.append(chg)
                        if kz == MAIN_KZ and single:
                            if nf_ is not None:
                                key = kind
                                if (key not in borderline
                                        or nf_ <
                                        borderline[key][0]):
                                    borderline[key] = (nf_, zones)
                            elif survivor_sample is None:
                                survivor_sample = (kind, zones)
                    N = ctx["N"]
                    ss = sorted((nf_ / N if nf_ is not None
                                 else 1.0) for nf_ in nfs)
                    st = dict(kind=kind, lab=lab, kz=kz,
                              med=float(np.median(ss)),
                              lo=ss[0], hi=ss[-1],
                              surv=sum(1 for v in nfs
                                       if v is None),
                              reps=reps,
                              eff=float(np.median(effs)),
                              iden=(max(effs) == 0))
                    stages[(kind, lab, kz)] = st
        check("G40-conservation-full", cons_all,
              "conservation EXACT on ALL %d perturbed worlds "
              "(positions / multisets / sign and magnitude fields "
              "bitwise per surgery type)" % n_worlds)
        check("G41-map-measured", acc_all
              and all((k_, l_, kz_) in stages
                      for k_ in SURG_NAMES for l_ in DOSE_LABELS
                      for kz_ in ctxs),
              "dose accounting <= nominal caps on ALL worlds; all "
              "%d map cells measured" % (len(stages)))

        # ---------------- S5: the minimality map
        section("S5  THE MINIMALITY MAP (sealed class rules)")
        for kind in SURG_NAMES:
            for kz in ctxs:
                cells = []
                for lab in DOSE_LABELS:
                    st = stages[(kind, lab, kz)]
                    cells.append("%s %s"
                                 % (str(lab),
                                    "IDENT" if st["iden"] else
                                    "%.3f[%.2f..%.2f]s%d/%d"
                                    % (st["med"], st["lo"],
                                       st["hi"], st["surv"],
                                       st["reps"])))
                info("%-8s w%-3d %s" % (kind, kz, " | ".join(cells)))
        classes = {}
        tol = {}
        laws = {}
        mono = {}
        for kind in SURG_NAMES:
            meds = [stages[(kind, lab, MAIN_KZ)]["med"]
                    for lab in DOSE_LABELS]
            s_single = stages[(kind, "SINGLE", MAIN_KZ)]["med"]
            tol[kind] = float(np.mean(meds))
            if s_single <= CTRL_HI:
                classes[kind] = "THRESHOLD"
            elif min(meds) >= NEAR_FULL:
                classes[kind] = "TOLERANT"
            elif s_single >= NEAR_FULL:
                classes[kind] = "GRADED"
            else:
                classes[kind] = "INTERMEDIATE"
            xs_, ds_ = [], []
            for th in THETAS:
                st = stages[(kind, th, MAIN_KZ)]
                D = 1.0 - st["med"]
                if (not st["iden"]) and D > DEF_MIN:
                    xs_.append(th)
                    ds_.append(D)
            laws[kind] = (halves_slope(xs_, ds_)
                          if len(xs_) >= LAW_MIN else None)
            th_meds = [(th, stages[(kind, th, MAIN_KZ)]["med"])
                       for th in THETAS
                       if not stages[(kind, th, MAIN_KZ)]["iden"]]
            mono[kind] = (BH.spearman([t for t, _ in th_meds],
                                      [m_ for _, m_ in th_meds])
                          if len(th_meds) >= 3 else float("nan"))
        rank = sorted(SURG_NAMES, key=lambda k: tol[k])
        rank_txt = " < ".join("%s %.3f" % (k, tol[k]) for k in rank)
        cls_txt = " / ".join(
            "%s %s%s" % (k, classes[k],
                         (" b %+.2f" % laws[k])
                         if laws[k] is not None else " NO_LAW")
            for k in SURG_NAMES)
        if all(classes[k] == "THRESHOLD" for k in SURG_NAMES):
            v_main = "FIREWALL_THRESHOLD(%s)" % cls_txt
        elif all(classes[k] in ("GRADED", "TOLERANT")
                 for k in SURG_NAMES):
            v_main = "FIREWALL_GRADED(%s)" % cls_txt
        else:
            v_main = "FIREWALL_LAW(%s)" % cls_txt
        check("G50-dose-map", True,
              "SEALED CLASSES (THRESHOLD s_single <= %.2f / "
              "TOLERANT min >= %.2f / GRADED / INTERMEDIATE): %s; "
              "monotonicity sp(theta, s_med): %s"
              % (CTRL_HI, NEAR_FULL, v_main,
                 str({k: ("%.2f" % mono[k]) for k in SURG_NAMES})))
        check("G51-law-fits", True,
              "deficit laws D ~ theta^b (halves log-slope, >= %d "
              "usable stages): %s -- deterministic, no fit "
              "primitives"
              % (LAW_MIN, " / ".join(
                  "%s %s" % (k, ("b %+.2f" % laws[k])
                             if laws[k] is not None
                             else "NO_LAW")
                  for k in SURG_NAMES)))
        mids = {kz: sum(1 for kind in SURG_NAMES
                        for lab in DOSE_LABELS
                        if CTRL_HI
                        < stages[(kind, lab, kz)]["med"]
                        < NEAR_FULL) for kz in ctxs}
        n_mid_w9 = mids[MAIN_KZ]
        n_mid = sum(mids.values())
        if n_mid_w9 == 0:
            cvj = "JUMP"
        elif n_mid_w9 >= K_CONT:
            cvj = "CONTINUUM"
        else:
            cvj = "SPARSE_MIDDLE"
        check("G52-continuum-vs-jump", True,
              "MIDDLE census (%.2f < s_med < %.2f): w9 %d/30, all "
              "windows %d/%d -> %s (sealed: JUMP iff 0, CONTINUUM "
              "iff >= %d on w9)"
              % (CTRL_HI, NEAR_FULL, n_mid_w9, n_mid, len(stages),
                 cvj, K_CONT))
        min_stage = min(((stages[(k_, l_, MAIN_KZ)]["med"], k_, l_)
                         for k_ in SURG_NAMES for l_ in DOSE_LABELS
                         if not stages[(k_, l_, MAIN_KZ)]["iden"]))
        touched = min_stage[0] <= CTRL_HI
        check("G53-v956-placement", True,
              "min w9 stage depth %.3f at %s theta %s vs the v956 "
              "control band 0.11..0.15 (controls 25/21/27 of N_w "
              "%d) -- CONTROL_%s; single ops land at %s"
              % (min_stage[0], min_stage[1], str(min_stage[2]),
                 ctxs[MAIN_KZ]["N"],
                 "TOUCHED" if touched else "NOT_REACHED",
                 str(["%.2f" % stages[(k_, "SINGLE",
                                       MAIN_KZ)]["med"]
                      for k_ in SURG_NAMES])))
        w9v = [stages[(k_, l_, MAIN_KZ)]["med"]
               for k_ in SURG_NAMES for l_ in DOSE_LABELS]
        sp_tr = {}
        for kz in RUNG_KZS:
            rv = [stages[(k_, l_, kz)]["med"]
                  for k_ in SURG_NAMES for l_ in DOSE_LABELS]
            sp_tr[kz] = BH.spearman(w9v, rv)
        transports = all(sp_tr[kz] >= SP_TRANSPORT
                         for kz in RUNG_KZS)
        check("G54-n-transport", True,
              "N-transport of the 30-stage map: sp(w9, kz18) "
              "%+.2f, sp(w9, kz55) %+.2f (bar %.1f) -> %s (typed "
              "classification, not a pass bar)"
              % (sp_tr[18], sp_tr[55], SP_TRANSPORT,
                 "MAP_TRANSPORTS" if transports
                 else "WINDOW_SPECIFIC"))

        # ---------------- S6: mp counter-checks + m3
        section("S6  MP COUNTER-CHECKS + MUST-FAIL m3")
        ok_mp = True
        mp_note = []
        for kind in SURG_NAMES:
            if kind not in borderline:
                mp_note.append("%s: no flipped single" % kind)
                continue
            nf_, zones = borderline[kind]
            r_mp = mp_first_flip(zones, min(nf_ + 5,
                                            ctxs[MAIN_KZ]["N"]),
                                 MP_DPS)
            ok_mp = ok_mp and (r_mp == nf_)
            mp_note.append("%s single nf %d mp %s"
                           % (kind, nf_, str(r_mp)))
        # amendment a1 (disclosed): the f64 chain covers degrees
        # 0..N_w-1; survivor/MAIN mp chains compare like-for-like
        # (upto N_w - 1); the boundary degree N_w is a disclosed
        # INFO ward (the v956 boundary flip AT the cap).
        if survivor_sample is not None:
            kind, zones = survivor_sample
            r_mp = mp_first_flip(zones, ctxs[MAIN_KZ]["N"] - 1,
                                 MP_DPS)
            ok_mp = ok_mp and (r_mp is None)
            mp_note.append("%s survivor mp %s (degrees <= N_w-1)"
                           % (kind, str(r_mp)))
        z_main = (p_main[MAIN_KZ]["d"]["xs"],
                  p_main[MAIN_KZ]["d"]["ws"],
                  p_main[MAIN_KZ]["d"]["ys"],
                  p_main[MAIN_KZ]["d"]["vs"])
        r_mp = mp_first_flip(z_main, ctxs[MAIN_KZ]["N"] - 1, MP_DPS)
        ok_mp = ok_mp and (r_mp is None)
        mp_note.append("MAIN mp %s (degrees <= N_w-1)" % str(r_mp))
        r_bnd = mp_first_flip(z_main, ctxs[MAIN_KZ]["N"], MP_DPS)
        info("v956 BOUNDARY WARD (mp dps %d): extending MAIN w9 one "
             "degree past the cap flips at %s == N_w %d (the r228 "
             "record n_flip = N_w + 0, reproduced)"
             % (MP_DPS, str(r_bnd), ctxs[MAIN_KZ]["N"]))
        ok_mp = ok_mp and (r_bnd == ctxs[MAIN_KZ]["N"])
        z_ep = (ctrl["EPSTEIN"]["d"]["xs"],
                ctrl["EPSTEIN"]["d"]["ws"],
                ctrl["EPSTEIN"]["d"]["ys"],
                ctrl["EPSTEIN"]["d"]["vs"])
        r_ep = mp_first_flip(z_ep, CTRL_FLIPS["EPSTEIN"] + 5,
                             MP_DPS)
        ok_mp = ok_mp and (r_ep == CTRL_FLIPS["EPSTEIN"])
        mp_note.append("EPSTEIN mp %s" % str(r_ep))
        check("G60-mp-counter-checks", ok_mp,
              "mp (dps %d) signed-Stieltjes sign chain confirms "
              "the f64 flip degrees EXACTLY at the borderline "
              "worlds -- no flip is f64 noise: %s"
              % (MP_DPS, "; ".join(mp_note)))
        nf_mut = CTRL_FLIPS["EPSTEIN"] - 3
        check("G61-mustfail-flip-noise", r_ep != nf_mut,
              "m3 FLIP-NOISE MUTANT (reports EPSTEIN nf %d): "
              "REJECTED by the mp counter-check (mp flip %s != "
              "%d) -- the detector is never trusted on f64 alone "
              "at the borderline" % (nf_mut, str(r_ep), nf_mut))

        # verdict assembly
        hyp = ("the wall is carried foremost by the %s property "
               "(tol %.3f) with the ranking %s; deficit laws %s; "
               "%s between control level and full survival"
               % (rank[0], tol[rank[0]], rank_txt,
                  " / ".join("%s %s" % (k, ("b %+.2f" % laws[k])
                                        if laws[k] is not None
                                        else "NO_LAW")
                             for k in SURG_NAMES), cvj))
        verd = " + ".join([
            v_main,
            "PROPERTY_RANKING(%s)" % rank_txt,
            "CONTINUUM_VS_JUMP(%s, %d/%d MIDDLE, w9 %d/30)"
            % (cvj, n_mid, len(stages), n_mid_w9),
            "V956_PLACEMENT(min %.3f at %s@%s, CONTROL_%s)"
            % (min_stage[0], min_stage[1], str(min_stage[2]),
               "TOUCHED" if touched else "NOT_REACHED"),
            "N_TRANSPORT(%s, sp %.2f/%.2f)"
            % ("MAP_TRANSPORTS" if transports
               else "WINDOW_SPECIFIC", sp_tr[18], sp_tr[55]),
            "FIREWALL_HYPOTHESIS(%s)" % hyp])

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the measured dose-response curve of the wall "
          "survival depth under five minimal-to-graduated "
          "surgeries -- NO certificate, NO bound, NO mechanism "
          "claim, NO H5 progress")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): conservation identities, "
          "dose accounting and the exact h-chain flips (mp "
          "counter-checked); MEASURED: every depth, class, law and "
          "ranking (three finite windows); OPEN: the cofinal step "
          "H5 and the wall mechanism (the hypothesis is a "
          "quantified TASK, not a claim); NO RH claim"
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
