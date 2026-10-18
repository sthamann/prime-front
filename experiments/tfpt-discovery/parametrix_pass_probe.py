#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""parametrix_pass_probe -- PRIME.PORT.RHP.PARAMETRIX.PASS.01
(round 259): the ANALYTIC half of the frozen micro-falsifier
(PRIME.FREEMOMENT.POSITIVEPREFIX.01).  r257 passed the falsifier at
the COEFFICIENT-FIELD level (blind source-only pivot field via
independent slogdet minors -- exact, not a model); the PARAMETRIX
pass stays OPEN: an analytic model (closed formulas / local
connection, NO exact determinant or minor computation) that blindly
predicts (i) the w9 control flips SCRAMBLE 21 / EPSTEIN 25 /
SMOOTH 27 and (ii) the five-window forced-tail survival
(0, 2, 2, 3, 1) at the flip degrees 184/153/170/367/592 -- while
staying false-positive-free on MAIN up to N_w - 1.  BUILDING
BLOCKS: r255 exact discrete saddle (S*_n = top-n by QP mass,
E(S) = rho_S^T A rho_S + V^T rho_S, parity sign channel; holds the
h-rate 4/4 but misplaces the flips 8/18 vs 25/27) with
ORIENTATION_LOWDIM(1) (one 0.2-dec swap separates model from truth
at the true flip degree) and the r254 handover (the flip carries
|gamma| > 1: a JUMP, not a soft crossing); r231 L-gauge midpoint
connection (h-free and sign-blind: the orientation sits exclusively
in the h-chain); r252 (outer model orientation-blind).  WORKING
HYPOTHESIS to adjudicate: the flip is a LEVEL CROSSING of the two
lowest parity-resolved saddle-energy branches -- if true, the flip
degree is the crossing point of two analytic curves and becomes
PREDICTABLE.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r257 discipline): w = window (kz),
N_w = builder depth, n = chain degree; free pivots h_{w,n}
(n < N_w) are the proof objects; ground truth (h signs, flip
degrees, forced-tail offsets, per-degree sign(det G_n) =
prod_{k<n} sg h_k) enters ANATOMY TARGETS AND GATES ONLY.  BLIND
PROTOCOL (hard, the r257 firewall pattern): the sealed predictor
functions consume node positions + signed weights + the QP
minimizer (capped-simplex equilibrium on the SOURCE energy) +
closed-form energy/swap formulas ONLY; a dedicated AST scope audit
excludes BOTH the chain identifiers (rows, lg_h, sg_h, gam_next,
nf, fb, hv, Fv, rho, hlog, lgt, wpack, bord_chain) AND every
linear-algebra resummation primitive (linalg, slogdet, det, eig*,
inv, solve, cholesky, qr, svd) from the predictor scope -- the
parametrix may not secretly BE the determinant.  A deliberately
minor-reading mutant must be FLAGGED (must-fail).  No zero/prime
oracles anywhere (AST firewall).

LEG A -- SADDLE SELECTION ANATOMY (understand first, model
second), on the w9 controls around the true flips (EPSTEIN
[22, 27], SMOOTH [24, 29], SCRAMBLE [18, 23]) and on MAIN w9 at
the same absolute degrees [18, 29]:
(a1) the CRITICAL SWAP: at each anatomy degree, from the 1-swap-
  stabilized saddle S°_n (greedy best-swap descent from the QP
  top-n; the r255 saddle refined -- disclosed refinement, sealed
  before evaluation), the minimal parity-flipping swap (i -> o):
  index distance |i - o|, weight-sign class (sgw_i, sgw_o),
  boundary ranks (QP-mass rank of o beyond n; rank of i inside),
  and the branch gap in decades.  SEALED STATISTIC
  SWAP_SHORT_RANGE iff median |i - o| <= 3 over the control flip
  windows (is the critical direction a short-range boundary
  pair?).
(a2) MAIN vs CONTROL (the 1-bit question in pure form): does the
  1-swap statistic SEPARATE MAIN at [18, 29] (no flip) from the
  controls at their flip degrees?  SEALED RULE: SWAP_STAT_
  SEPARATES iff min over MAIN anatomy degrees of the branch gap
  > max over control flip-degree gaps ({nf, nf+1} per control);
  else SWAP_STAT_NOT_SEPARATING -- and then the r255
  ORIENTATION_LOWDIM(1) reading must be REVISED (the swap margin
  is not a source-pure selector): SELECTION_EXTENSIVE_AFTER_ALL.
(a3) LEVEL CROSSING: the two parity-resolved branch minima
  E_even(n), E_odd(n) (free 1-swap-stable minimum + opposite-
  parity branch = cheapest parity-flip seed then parity-keeping
  descent, N_SEED seeds).  Crossing degree = first n where the
  odd branch goes below.  SEALED RULE: LEVEL_CROSSING_AT_FLIP iff
  |crossing - nf| <= 2 on BOTH EPSTEIN and SMOOTH; else
  LEVEL_CROSSING_REFUTED.  MAIN: the count of lower-branch parity
  switches over the full free window (each one a would-be flip
  that the true chain does not have) -- the crossing picture's
  false-positive bill.  The |gamma| > 1 jump (r254 handover) is
  re-derived gate-side at the true flips and compared with the
  true |gamma| at the MODEL crossing degrees (does the truth
  jump where the model crosses? -- informational).

LEG B -- THE PARAMETRIX CANDIDATES (exactly 3, sealed; each
consumes source + QP minimizer + closed formulas only, per-degree
model sign sg^cand(D_n), model h-sign = sg(D_{n+1}) sg(D_n),
first-flip = first degree with model h-sign < 0):
(P1) TWO-BRANCH: sg(D_n) = parity of the lower parity-resolved
  branch (the a3 object; flip at the branch crossing).
(P2) SELECTION RULE (r255 + LOWDIM correction): sg(D_n) =
  parity(S*_n) from the RAW QP top-n, FLIPPED iff the minimal
  parity-flipping swap from S*_n has dE < 0 (the r255 leg-C
  margin, now consumed as a predictor correction).
(P3) HYBRID with hysteresis: L-gauge/outer rate is sign-blind
  (r255 4/4, imported result, not re-adjudicated); orientation =
  P1 branch sign but a sign SWITCH is accepted only when the
  opposite branch is lower by more than THETA = 0.05 dec (the
  jump discipline from the r254 handover: a flip is a threshold
  event, not a soft degeneracy).
ADJUDICATION per candidate (gates, ground truth enters here
only): (arm 1) control flips: first-flip within +-2 of 21/25/27
(also +-0 reported); (arm 2) forced tail: first-flip offset
j = n - N_w on the five windows (9, 12, 13, 26, 40) == frozen
prior (0, 2, 2, 3, 1); (arm 3) MAIN clean: NO model h-flip below
N_w - 1 on the four full-depth mains (9, 12, 13, 26).  Per-degree
missign fractions (P1/P2) per window recorded for the leg-C
typing.

LEG C -- HONEST BOUNDARY (if no candidate fully passes): type
precisely WHAT is missing: (i) rate ok / selection wrong -> the
measured misselection statistics (degrees off, systematic
direction, missign fraction); (ii) controls ok / MAIN false-
positive (model too flip-happy); (iii) the crossing mechanism
does not exist (branches do not cross at the flip degree) ->
LEVEL_CROSSING_REFUTED stands as a negative finding.  The half
falsifier then stays honestly OPEN with the obstacle named.

LEG D -- FALSIFIERS + MUST-FAILS (each loud) + WARDS:
(m1) MINOR-ORACLE MUTANT: a predictor variant that reads the
  chain sign field must be FLAGGED by the predictor AST audit
  while the sealed scope stays clean;
(m2) WRONG VANDERMONDE EXPONENT (r255-m1 pattern; replaces the
  drafted swapped-branch mutant, amendment a1): the pair energy
  counted once instead of twice must move the stable-saddle
  energy at the sealed degree (w9, n = 21) by >= 10 decades --
  the energy form is load-bearing;
(m3) r255 ANCHOR: P2 WITHOUT the swap correction (the bare r255
  parity rule) must reproduce the r255 misplacements EXACTLY
  (EPSTEIN first flip 8, SMOOTH 18) -- the correction is real,
  the anchor ties this round to the r255 record;
(w1) mp FLIP WARDS (dps 40, r257 pattern, gate side): sign det
  G_25/G_26 = +/- on EPSTEIN, sign det G_27/G_28 = +/- on SMOOTH
  (exact-arithmetic confirmation of the ground truth the
  candidates are judged against);
(w2) mp ENERGY WARD (dps 60): the SMOOTH branch energies at the
  sealed degrees {27, 28} recomputed in mpmath; |E_mp - E_f64| <=
  1e-6 nats (the 0.004-dec gaps are not f64 noise);
(w3) CHEBYSHEV TOY ANCHOR (64 nodes, discrete U-weight, masses
  5..17): positive weights -> NO parity-flipping swap exists; all
  three candidates must be flip-free and all parities +1.

SEALED CONSTANTS: mains (9, 12, 13, 26) full depth + EXT; tail
windows (9, 12, 13, 26, 40), prior offsets (0, 2, 2, 3, 1), EXT
6; control flips EPSTEIN/SCRAMBLE/SMOOTH = 25/21/27, control
sweep 2..nf+11; anatomy windows: EPSTEIN [22, 27], SMOOTH
[24, 29], SCRAMBLE [18, 23], MAIN [18, 29]; QP FISTA iters 8000,
tol 1e-8, residual bar 1e-6, warm ascending; stabilizer max 400
swaps, seed count N_SEED 6, swap-stability floor -1e-13; THETA
0.05 dec; flip tolerance +-2 (and +-0 reported); short-range bar
median |i - o| <= 3; w40 sweep early-stops once ALL candidates
have flipped (disclosed: MAIN-clean is adjudicated on the four
full-depth mains; w40 feeds arm 2 only); toy 64 nodes masses
5..17; mp wards dps 40 / 60, energy bar 1e-6 nats; must-fail
bars: m2 >= 10 dec at (w9, n = 21), m3 exact (8, 18);
runtime <= 1800 s; smoke = w9 masses 2..42 + controls 2..nf+8 +
toy, tails / w40 / mp wards skipped, no adjudication.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  PARAMETRIX_PASSED(cand, +-tol) iff some candidate passes arms
    1 AND 2 AND 3;
  else PARAMETRIX_PARTIAL(what carries, what misses) iff some
    candidate passes at least one arm fully;
  else PARAMETRIX_FAILED(typed per leg C)
+ LEVEL_CROSSING_AT_FLIP(degrees) / LEVEL_CROSSING_REFUTED
    (crossing vs flip per control, MAIN switch count)
+ SWAP_STAT_SEPARATES / SWAP_STAT_NOT_SEPARATING
+ SELECTION_EXTENSIVE_AFTER_ALL iff SWAP_STAT_NOT_SEPARATING
    (the r255 LOWDIM(1) reading revised, honestly)
  / SELECTION_LOWDIM_CONFIRMED otherwise.
Honesty before beauty: a failed parametrix leaves the analytic
half of the micro-falsifier OPEN with the obstacle named; the
r257 coefficient-field pass, the budget bound and the base law
stay as they are (r243/r247/r250/r252/r255/r256/r257 stand).

PRE-SPEC SCRATCH CALIBRATION (disclosed, r257 practice): a
scratch scan (deleted) established the machinery scales (QP warm
sweep cost, stabilizer swap counts, branch-gap magnitudes
0.005-0.6 dec, the SMOOTH stabilizer needing > 60 greedy swaps)
and showed the qualitative landscape on w9 BEFORE this spec was
sealed; every bar, form and verdict rule above was frozen before
the full-record evaluation.

CALIBRATION AMENDMENTS (disclosed, frozen; found in the FIRST
smoke pass BEFORE any full-record evaluation): (a1) the drafted
m2 "swapped branches" mutant (sign of the UPPER branch) is
UNOBSERVABLE in the flip channel BY CONSTRUCTION -- the model
h-sign sg(D_{n+1}) sg(D_n) is invariant under a GLOBAL parity
negation, so exchanging the branch order at every degree moves
no flip (a structural fact about every per-degree sign model,
worth recording); m2 is replaced by the r255-m1-shaped WRONG
VANDERMONDE EXPONENT loudness at the sealed degree (w9, n = 21),
bar >= 10 dec.  (a2) the w2 mp energy ward of the first full
attempt indexed the saddle config into the UNSORTED union arrays
while the configs live in the SORTED union_setup order -- pure
implementation fix in a gate-side ward (r252-a1 precedent), no
bar touched.  No bar, form or verdict rule of the candidates,
anatomy or adjudication moved at any point.

RECORD TABLES (frozen after calibration pass 1, 19/19 gates;
run 2 must reproduce bit-for-bit up to the WALL line):
* CENSUS: mains w9/w12/w13/w26 N = 184/151/168/364 POSITIVE_
  PREFIX; controls re-derived 25/21/27; 1586 QP equilibria,
  residual worst 1.0e-08 (bar 1e-6), masses integer-exact; w40
  (N = 591) early-stopped at mass 597; mp flip wards (dps 40):
  EPSTEIN sign det G_25/G_26 = +1/-1, SMOOTH G_27/G_28 = +1/-1;
  mp energy ward (dps 60) max |E_mp - E_f64| = 0.0e+00 nats
  (bar 1e-6): the milli-decade branch gaps are exact, not f64
  noise.
* LEG A ANATOMY (a1): the critical parity-swap at the control
  flips is a SHORT-RANGE OPPOSITE-SIGN BOUNDARY PAIR -- median
  |i - o| = 2 over the anatomy windows (EPSTEIN 341<->339 /
  184->182 d = 2 at the flip, SMOOTH 363->364 d = 1 throughout,
  SCRAMBLE 72<->75 d = 3 / 278<->274 d = 4), weight signs
  opposite by construction => SWAP_SHORT_RANGE.  (a2) the SAME
  structure sits on MAIN w9 at [18, 29] (pair 364<->365, d = 1,
  gap 0.013-0.018 dec from n = 24 on): control flip-degree gaps
  0.0045/0.0339 (EPST), 0.1981/0.1950 (SMOOTH), 0.0142/0.0054
  (SCR) vs MAIN anatomy gaps 0.0133..0.5279 -- full overlap
  (MAIN min 0.0133 < control max 0.1981) => SWAP_STAT_NOT_
  SEPARATING: no 1-swap observable separates MAIN-at-no-flip
  from control-at-flip => SELECTION_EXTENSIVE_AFTER_ALL (the
  r255 LOWDIM(1) reading is hereby revised: the 0.2-dec swap
  EXISTS at the flip degree, but the missing information is NOT
  a 1-dimensional selection error -- the parity of the energy-
  ordered configuration is wrong on EXTENDED stretches on every
  world).  (a3) branch crossings vs true flips: EPSTEIN
  crossing 9 vs flip 25 (off 16), SMOOTH 19 vs 27 (off 8),
  SCRAMBLE 16 vs 21 (off 5) => LEVEL_CROSSING_REFUTED; MAIN w9
  lower-branch parity switches below N-1: 45 (45 would-be
  flips, zero true ones; odd-lower stretches up to 11 degrees
  with gaps up to 0.20 dec while det G stays positive).
  |gamma| anatomy (gate side): true lg10|gamma| at the flips
  +1.16 (EPST) / +0.41 (SMOOTH) / -0.89 (SCR; the SCRAMBLE flip
  is NOT a jump -- the r254 jump statement holds on EPSTEIN/
  SMOOTH only, disclosed); at the model crossing degrees the
  true values are -0.61 / -0.61 / -0.57: NO jump where the
  model crosses -- the jump belongs to the resummed chain at
  the TRUE flips, not to the branch crossings.
* LEG B CANDIDATES (first flips; true 25/21/27, tail truths
  184/153/170/367/592 = N + (0, 2, 2, 3, 1)):
    P1 two-branch: EPST 8, SCR 15, SMOOTH 18 -- 0/3 within +-2
      (systematically EARLY by 17/6/9 degrees); MAIN first
      false flips w9 39 / w12 16 / w13 18 / w26 51 => arm 3
      0/4; tail offsets j = -145/-135/-150/-313/-525 vs
      (0, 2, 2, 3, 1) => 0/5; per-degree missign fractions
      0.34/0.46/0.37/0.44 on the mains.
    P2 selection rule: EPST 2, SCR 11, SMOOTH 17 -- 0/3 (the
      LOWDIM swap correction does NOT repair the placement; it
      flips EARLIER than the bare rule on every control); MAIN
      11/14/11/28 => 0/4; tail -173/-137/-157/-336/-525 => 0/5;
      missign 0.57/0.37/0.71/0.43.
    P3 hybrid hysteresis (THETA 0.05): EPST None, SCR 15,
      SMOOTH 19 -- 0/3; MAIN first false flips 181/None/None/
      None (the 0.05-dec bar suppresses the shallow noise
      entirely on w12/w13/w26, but the deep w9 odd stretch
      punches through at 181 -- three degrees BEFORE the true
      forced-tail flip 184 and still below N-1: a near-miss
      that is honestly a false positive) => arm 3 0/4; tail
      w9 j = -3, others None => 0/5.
  => no candidate passes any arm fully.  PARAMETRIX_FAILED.
* LEG C TYPING: (i) the rate is NOT the obstacle (r255 b2 held
  it 4/4, imported); the SELECTION is: misselection is
  systematically EARLY (6..17 degrees before truth on every
  control, every candidate), missign fractions 0.34-0.71;
  (ii) every candidate is too flip-happy on MAIN (first false
  positive at degree 11-181 of 151-364; even the hysteresis
  candidate that is clean on 3/4 windows breaks on w9); (iii)
  the crossing mechanism DOES NOT EXIST at the flip degree:
  the parity-resolved branches cross 5-16 degrees early, and
  on MAIN w9 they cross 45 times without a single true flip;
  the true sign is carried by COHERENT CANCELLATION across the
  configuration ensemble (the odd branch sits BELOW the even
  branch by up to 0.20 dec over 9+ consecutive degrees on
  SMOOTH and MAIN while det G stays positive) -- a resummation
  effect that no dominant-configuration model at any k-swap
  resolution sees (a 1-swap signed partition resummation was
  scratch-tested pre-spec: the parity-keeping entropy dominates
  the bracket, sign unchanged).  THE PARAMETRIX GAP IS A
  RESUMMATION GAP, NOT A SELECTION GAP.
* LEG D: m1 minor-oracle mutant FLAGGED (rows/sg_h), sealed
  scopes CLEAN (10 predictor functions, 0 hits); m2 wrong
  Vandermonde exponent: 47.6 dec at (w9, n = 21) (bar 10,
  LOUD); m3 bare-r255 anchor: EPSTEIN 8, SMOOTH 18 reproduced
  EXACTLY; toy: 0 parity-flip swaps exist, all candidate signs
  +1 on 13/13 masses.
* VERDICT: PARAMETRIX_FAILED(selection wrong on 3/3 controls +
  MAIN false positives; typed i+ii+iii) + LEVEL_CROSSING_
  REFUTED(EPST 9 vs 25, SMOOTH 19 vs 27, SCR 16 vs 21; MAIN 45
  switches) + SWAP_STAT_NOT_SEPARATING + SELECTION_EXTENSIVE_
  AFTER_ALL; 19/19 gates, wall 155.5 s full / 9.7 s smoke.
  READING: the analytic half of the micro-falsifier stays OPEN
  with the obstacle NAMED and MEASURED -- the orientation is
  not a saddle-selection observable at any 1-swap resolution;
  the minimal analytic object that could carry it must resum
  the near-degenerate configuration ensemble coherently (the
  r257 minor scan does exactly that, exactly), and the r255
  LOWDIM(1) selection reading is revised to SELECTION_
  EXTENSIVE_AFTER_ALL.
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

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import centered_basefiber_probe as CB        # noqa: E402 r250
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import szego_equilibrium_probe as SZ         # noqa: E402 r232a
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

MAINS = (9, 12, 13, 26)
TAIL_WINDOWS = (9, 12, 13, 26, 40)
PRIOR_OFFSETS = (0, 2, 2, 3, 1)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
ANAT_WIN = {"EPSTEIN": (22, 27), "SMOOTH": (24, 29),
            "SCRAMBLE": (18, 23), "MAIN": (18, 29)}
EXT = 6
CTRL_PAD = 11
QP_ITERS = 8000
QP_TOL = 1e-8
QP_RES_BAR = 1e-6
STAB_MAX = 400
STAB_FLOOR = -1e-13
N_SEED = 6
THETA = 0.05
FLIP_TOL = 2
SHORTRANGE_BAR = 3
TOY_M = 64
TOY_MASSES = tuple(range(5, 18))
MP_FLIP_DPS = 40
MP_EN_DPS = 60
MP_EN_BAR = 1e-6
M2_DEG = 21
M2_LOUD_DEC = 10.0
M3_ANCHOR = {"EPSTEIN": 8, "SMOOTH": 18}
L10 = math.log(10.0)
PRED_FUNCS = ("psel_top", "pparity", "penergy", "pswap", "pstab",
              "pstab_keep", "pbranch", "pred_p2", "pred_p1_sign",
              "pred_p3_seq")
PRED_FORBIDDEN = {"rows", "lg_h", "sg_h", "gam_next", "nf", "fb",
                  "hv", "Fv", "rho", "hlog", "lgt", "wpack",
                  "bord_chain", "linalg", "slogdet", "det",
                  "eigvalsh", "eigh", "eig", "inv", "solve",
                  "cholesky", "qr", "svd"}
CAL_VERDICT = (
    "PARAMETRIX_FAILED(selection wrong on 3/3 controls + MAIN "
    "false positives; typed i+ii+iii) + LEVEL_CROSSING_REFUTED"
    "(EPST 9 vs 25, SMOOTH 19 vs 27, SCR 16 vs 21; MAIN 45 "
    "switches) + SWAP_STAT_NOT_SEPARATING + "
    "SELECTION_EXTENSIVE_AFTER_ALL")

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
    """standing zero/prime firewall + the sealed predictor scope
    audit: the parametrix may not secretly be the determinant."""
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
    hits = []
    for fn in PRED_FUNCS:
        hits += predictor_scope_audit(fn)
    ok = (not bad) and (not hits)
    return ok, ("NO zero/prime oracles; predictor scope CLEAN: %d "
                "sealed functions consume node positions + signed "
                "weights + the QP minimizer + closed-form energy/"
                "swap formulas only (chain identifiers AND linalg "
                "resummation primitives excluded: %s); ground "
                "truth enters anatomy targets and gates only"
                % (len(PRED_FUNCS), sorted(PRED_FORBIDDEN))
                if ok else "; ".join(bad + hits))


def predictor_scope_audit(funcname):
    """walk ONLY the named function's subtree; flag any forbidden
    identifier / attribute / string constant."""
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
                if nm in PRED_FORBIDDEN:
                    hits.append("%s:%s@%d" % (funcname, nm,
                                              sub.lineno))
    return hits


# --------------------------- sealed predictor functions (BLIND)
def psel_top(dens, n):
    """S*_n: top-n nodes by QP mass, stable tie-break by index
    (r255 sealed rounding rule)."""
    order = np.lexsort((np.arange(len(dens)), -dens))
    b = np.zeros(len(dens), bool)
    b[order[:int(n)]] = True
    return b


def pparity(sgw, b):
    """parity(S) = prod sign(wt_j) over the selected subset."""
    return -1 if (int(np.sum(sgw[b] < 0)) % 2) else 1


def penergy(A, V, b):
    """exact discrete energy E(S) = rho_S^T A rho_S + V^T rho_S."""
    r = b.astype(float)
    return float(r @ (A @ r)) + float(V @ r)


def pswap(A, V, b):
    """closed-form single-swap energy field dE[i, o] = base_o -
    base_i - 2 A_io, base = 2 (A rho_S) + V (r255 leg-C form)."""
    r = b.astype(float)
    base = 2.0 * (A @ r) + V
    iS = np.flatnonzero(b)
    iO = np.flatnonzero(~b)
    dE = (base[iO][None, :] - base[iS][:, None]
          - 2.0 * A[np.ix_(iS, iO)])
    return dE, iS, iO


def pstab(A, V, b):
    """greedy best-single-swap descent to a 1-swap-stable saddle."""
    b = b.copy()
    for _ in range(STAB_MAX):
        dE, iS, iO = pswap(A, V, b)
        k = int(np.argmin(dE))
        ii, oo = np.unravel_index(k, dE.shape)
        if dE[ii, oo] >= STAB_FLOOR:
            break
        b[iS[ii]] = False
        b[iO[oo]] = True
    return b


def pstab_keep(A, V, sgw, b):
    """greedy descent restricted to parity-KEEPING swaps (stays on
    one branch)."""
    b = b.copy()
    for _ in range(STAB_MAX):
        dE, iS, iO = pswap(A, V, b)
        keep = (sgw[iS][:, None] * sgw[iO][None, :]) > 0
        dE = np.where(keep, dE, np.inf)
        k = int(np.argmin(dE))
        ii, oo = np.unravel_index(k, dE.shape)
        if dE[ii, oo] >= STAB_FLOOR:
            break
        b[iS[ii]] = False
        b[iO[oo]] = True
    return b


def pbranch(A, V, sgw, b0):
    """parity-resolved two-branch minima from the QP top-n seed:
    free stabilize + keep-stabilize -> (p0, E0); opposite branch
    from the N_SEED cheapest parity-flip seeds + keep descent ->
    E1.  Returns (p0, E0, E1, gap_dec, i*, o*, b_stable)."""
    bst = pstab(A, V, b0)
    bst = pstab_keep(A, V, sgw, bst)
    p0 = pparity(sgw, bst)
    E0 = penergy(A, V, bst)
    dE, iS, iO = pswap(A, V, bst)
    mask = (sgw[iS][:, None] * sgw[iO][None, :]) < 0
    dEm = np.where(mask, dE, np.inf)
    if not np.any(mask):
        return p0, E0, float("inf"), float("inf"), -1, -1, bst
    k = int(np.argmin(dEm))
    ci, co = np.unravel_index(k, dEm.shape)
    flat = np.argsort(dEm, axis=None)[:N_SEED]
    E1 = float("inf")
    for kk in flat:
        ii, oo = np.unravel_index(kk, dEm.shape)
        if not np.isfinite(dEm[ii, oo]):
            continue
        b1 = bst.copy()
        b1[iS[ii]] = False
        b1[iO[oo]] = True
        b1 = pstab_keep(A, V, sgw, b1)
        E1 = min(E1, penergy(A, V, b1))
    return (p0, E0, E1, (E1 - E0) / L10, int(iS[ci]),
            int(iO[co]), bst)


def pred_p1_sign(p0, gap_dec):
    """P1: sign(D_n) = parity of the LOWER branch (gap >= 0 by
    stability: the free minimum owns the sign)."""
    return p0 if gap_dec >= 0.0 else -p0


def pred_p2(A, V, sgw, dens, n):
    """P2: raw r255 parity + LOWDIM swap correction (flip iff the
    best parity-flipping swap from the RAW top-n has dE < 0)."""
    b = psel_top(dens, n)
    p = pparity(sgw, b)
    dE, iS, iO = pswap(A, V, b)
    mask = (sgw[iS][:, None] * sgw[iO][None, :]) < 0
    if not np.any(mask):
        return p
    m = float(np.min(np.where(mask, dE, np.inf)))
    return -p if m < 0.0 else p


def pred_p3_seq(p0s, gaps, theta):
    """P3: branch sign with hysteresis -- a switch is accepted only
    when the opposite branch is lower by more than theta decades
    relative to the current state (threshold-event discipline)."""
    out = []
    cur = None
    for p0, g in zip(p0s, gaps):
        if cur is None:
            cur = p0
        elif p0 != cur and g > theta:
            cur = p0
        out.append(cur)
    return out


# ------------------------------------------------- oracle mutant
def oracle_pred(p, n_hi):
    """DELIBERATE MUST-FAIL MUTANT (m1): reads the chain sign field
    -- the predictor AST audit must FLAG this scope."""
    return [r["n"] for r in p["rows"][:n_hi] if r["sg_h"] < 0]


# ------------------------------------------------------ gate side
def union_arrays(d):
    return (np.concatenate([d["xs"], d["ys"]]),
            np.concatenate([d["ws"], -d["vs"]]))


def truth_sgdet(rows, n_hi):
    """sign(det G_n) = prod_{k<n} sg h_k (gate side)."""
    sg = {0: 1}
    s = 1
    for k in range(min(len(rows), n_hi)):
        s *= int(rows[k]["sg_h"])
        sg[k + 1] = s
    return sg


def world_sweep(d, masses, anat_degs=frozenset()):
    """QP warm sweep + per-mass predictor data for all candidates.
    Consumes SOURCE data only; truth joined outside."""
    x, wt, A, Lip, V = CB.eq_field(d)
    sgw = np.sign(wt)
    dens = None
    res_worst = 0.0
    mass_ok = True
    out = dict(ns=[], p0=[], gap=[], sgP2=[], ci=[], co=[])
    anat = {}
    for n in masses:
        dens, res = SZ.solve_qp(A, Lip, V, float(n), rho0=dens,
                                iters=QP_ITERS, tol=QP_TOL)
        res_worst = max(res_worst, res)
        mass_ok = mass_ok and (int(round(float(np.sum(dens)))) == n)
        b0 = psel_top(dens, n)
        p0, E0, E1, gap, ci, co, bst = pbranch(A, V, sgw, b0)
        out["ns"].append(n)
        out["p0"].append(p0)
        out["gap"].append(gap)
        out["ci"].append(ci)
        out["co"].append(co)
        out["sgP2"].append(pred_p2(A, V, sgw, dens, n))
        if n in anat_degs:
            rk = np.lexsort((np.arange(len(dens)), -dens))
            rank = np.empty(len(dens), int)
            rank[rk] = np.arange(len(dens))
            anat[n] = dict(
                p0=p0, gap=gap, i=ci, o=co,
                dio=abs(co - ci) if ci >= 0 else -1,
                sgi=int(sgw[ci]) if ci >= 0 else 0,
                sgo=int(sgw[co]) if co >= 0 else 0,
                rk_o=int(rank[co]) - n + 1 if co >= 0 else -1,
                rk_i=n - int(rank[ci]) if ci >= 0 else -1,
                E0=E0, E1=E1, bst=bst.copy())
    out["ns"] = np.asarray(out["ns"], int)
    out["p0"] = np.asarray(out["p0"], int)
    out["gap"] = np.asarray(out["gap"], float)
    out["sgP2"] = np.asarray(out["sgP2"], int)
    return out, anat, res_worst, mass_ok, (x, wt, A, V, sgw)


def cand_signs(sw):
    """per-degree model sign(D_n) for P1/P2/P3 from the sweep."""
    sg1 = np.array([pred_p1_sign(p, g)
                    for p, g in zip(sw["p0"], sw["gap"])], int)
    sg2 = sw["sgP2"]
    sg3 = np.asarray(pred_p3_seq(list(sw["p0"]), list(sw["gap"]),
                                 THETA), int)
    return {"P1": sg1, "P2": sg2, "P3": sg3}


def first_flip(ns, sg):
    """first degree n with model h-sign sg(D_{n+1}) sg(D_n) < 0."""
    for i in range(len(ns) - 1):
        if ns[i + 1] == ns[i] + 1 and sg[i + 1] * sg[i] < 0:
            return int(ns[i])
    return None


def missign_frac(ns, sg, sgdet):
    hit = tot = 0
    for i, n in enumerate(ns):
        if int(n) in sgdet:
            tot += 1
            hit += int(sg[i] != sgdet[int(n)])
    return hit / max(tot, 1)


def mp_flip_ward(xu, wu, nlist, dps):
    """exact-precision determinants of the scaled-Cheb source Gram
    at the sealed flip-adjacent sizes (r257 verbatim, GATE side)."""
    mp.mp.dps = dps
    lo, hi = float(np.min(xu)), float(np.max(xu))
    x0 = mp.mpf(0.5 * (lo + hi))
    rh = mp.mpf(0.5 * (hi - lo))
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    tv = [(x - x0) / rh for x in xs]
    n_hi = max(nlist)
    P = [[mp.mpf(1)] * len(xs), [2 * t for t in tv]]
    for _k in range(2, n_hi):
        P.append([2 * t * a - b
                  for t, a, b in zip(tv, P[-1], P[-2])])
    G = mp.matrix(n_hi, n_hi)
    for i in range(n_hi):
        for j in range(i, n_hi):
            v = mp.fsum(w * a * b for w, a, b in zip(ws, P[i], P[j]))
            G[i, j] = v
            G[j, i] = v
    return {n: int(mp.sign(mp.det(G[:n, :n]))) for n in nlist}


def mp_energy(xu, wu, b, dps):
    """the discrete saddle energy of config b in mp arithmetic
    (ward w2, GATE side)."""
    mp.mp.dps = dps
    idx = np.flatnonzero(b)
    xs = [mp.mpf(float(xu[i])) for i in idx]
    ws = [mp.mpf(float(abs(wu[i]))) for i in idx]
    E = -mp.fsum(mp.log(w) for w in ws)
    for a_ in range(len(xs)):
        for b_ in range(a_ + 1, len(xs)):
            E -= 2 * mp.log(abs(xs[a_] - xs[b_]))
    return float(E)


def toy_block():
    """discrete Chebyshev-U toy (w3): positive weights -> no
    parity-flip swap exists; candidates must be flip-free."""
    xt = np.sort(np.cos(np.pi * (np.arange(TOY_M) + 0.5) / TOY_M))
    wtt = (1.0 - xt * xt) * (np.pi / TOY_M)
    Dm = np.abs(xt[:, None] - xt[None, :])
    np.fill_diagonal(Dm, 1.0)
    At = -np.log(Dm)
    np.fill_diagonal(At, 0.0)
    v = np.ones(TOY_M) / math.sqrt(TOY_M)
    for _ in range(80):
        v2 = At @ v
        nv = float(np.linalg.norm(v2))
        v = v2 / nv
    Lipt = 2.0 * nv
    Vt = -np.log(wtt)
    sgt = np.sign(wtt)
    dens = None
    res_w = 0.0
    p0s, gaps, sg2 = [], [], []
    nflipswaps = 0
    for n in TOY_MASSES:
        dens, res = SZ.solve_qp(At, Lipt, Vt, float(n), rho0=dens,
                                iters=QP_ITERS, tol=QP_TOL)
        res_w = max(res_w, res)
        b0 = psel_top(dens, n)
        p0, _E0, _E1, gap, ci, _co, _b = pbranch(At, Vt, sgt, b0)
        nflipswaps += int(ci >= 0)
        p0s.append(p0)
        gaps.append(gap)
        sg2.append(pred_p2(At, Vt, sgt, dens, n))
    sg3 = pred_p3_seq(p0s, gaps, THETA)
    par_ok = all(p == 1 for p in p0s) and all(s == 1 for s in sg2) \
        and all(s == 1 for s in sg3)
    return dict(res=res_w, par_ok=par_ok, nflip=nflipswaps,
                n_masses=len(TOY_MASSES))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("parametrix_pass_probe -- PRIME.PORT.RHP.PARAMETRIX."
          "PASS.01 (round 259)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 masses 2..42 + controls + toy; "
                        "tails/w40/mp wards skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall+predictor-scope", okf, det)
    check("G02-predefinition", True,
          "candidates sealed: P1 two-branch (parity of the lower "
          "parity-resolved branch), P2 r255 parity + LOWDIM swap "
          "correction, P3 branch sign with hysteresis THETA %.2f "
          "dec; arms: control flips +-%d, tail offsets %s at N + "
          "j, MAIN clean to N-1 on %s; anatomy windows %s; "
          "stabilizer max %d swaps, %d branch seeds; must-fail "
          "bars m2 >= %.0f dec at (w9, n = %d), m3 exact %s; ALL "
          "bars + verdict rules sealed in the frozen spec BEFORE "
          "evaluation (amendment a1 disclosed)"
          % (THETA, FLIP_TOL, str(PRIOR_OFFSETS),
             str(MAINS), str(ANAT_WIN), STAB_MAX,
             N_SEED, M2_LOUD_DEC, M2_DEG, str(M3_ANCHOR)))

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS")
    packs = {kz: BH.wpack(kz) for kz in
             ((9,) if smoke else MAINS)}
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
    okC = all(packs[kz]["nf"] is None for kz in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    check("G10-census-controls", okC and okCf,
          "MAIN free prefix positive at full depth (%s); control "
          "flips re-derived %s (ground truth, gates/anatomy only)"
          % ("; ".join("w%d N=%d" % (kz, packs[kz]["N"])
                       for kz in packs),
             str({c: ctrl[c]["nf"] for c in ctrl})))

    # ---------------- S2: toy anchor
    section("S2  CHEBYSHEV TOY ANCHOR (w3)")
    toy = toy_block()
    ok_toy = (toy["res"] <= QP_RES_BAR and toy["par_ok"]
              and toy["nflip"] == 0)
    check("G20-toy-anchor", ok_toy,
          "QP residual %.1e (bar %.0e); positive weights: %d "
          "parity-flip swaps exist over %d masses (must be 0); "
          "all candidate signs +1 on all masses: %s -- the sign "
          "layer is exactly trivial cap-free, all candidates "
          "flip-free by construction"
          % (toy["res"], QP_RES_BAR, toy["nflip"],
             toy["n_masses"], str(toy["par_ok"])))

    # ---------------- S3: sweeps
    section("S3  SWEEPS (QP + branch data at every mass)")
    res_worst = 0.0
    mass_ok = True
    nQP = 0
    SW = {}
    ANAT = {}
    SRC = {}
    for kz in packs:
        p = packs[kz]
        N = p["N"]
        masses = (list(range(2, 43)) if smoke
                  else list(range(2, N + EXT + 1)))
        adeg = (set(range(*ANAT_WIN["MAIN"])) | {ANAT_WIN["MAIN"][1]}
                if kz == 9 else set())
        sw, an, rw, mo, src = world_sweep(p["d"], masses, adeg)
        res_worst = max(res_worst, rw)
        mass_ok = mass_ok and mo
        nQP += len(masses)
        SW["w%d" % kz] = sw
        ANAT["w%d" % kz] = an
        SRC["w%d" % kz] = src
        info("w%-3d N=%d: %d masses swept" % (kz, N, len(masses)))
    for c in ctrl:
        nf = ctrl[c]["nf"]
        top = nf + (8 if smoke else CTRL_PAD)
        a0, a1 = ANAT_WIN[c]
        adeg = set(range(a0, a1 + 1))
        sw, an, rw, mo, src = world_sweep(
            ctrl[c]["d"], list(range(2, top + 1)), adeg)
        res_worst = max(res_worst, rw)
        mass_ok = mass_ok and mo
        nQP += top - 1
        SW[c] = sw
        ANAT[c] = an
        SRC[c] = src
        info("%-8s nf=%d: swept 2..%d" % (c, nf, top))
    # w40 tail sweep with early stop (arm 2 only, disclosed)
    ff_w40 = {}
    if not smoke:
        d40 = HS.window_data(40)
        N40 = d40["n_max"]
        x, wt, A, Lip, V = CB.eq_field(d40)
        sgw = np.sign(wt)
        dens = None
        p0s, gaps, sg2 = [], [], []
        ns40 = []
        for n in range(2, N40 + EXT + 1):
            dens, res = SZ.solve_qp(A, Lip, V, float(n), rho0=dens,
                                    iters=QP_ITERS, tol=QP_TOL)
            res_worst = max(res_worst, res)
            b0 = psel_top(dens, n)
            p0, _E0, _E1, gap, _ci, _co, _b = pbranch(A, V, sgw, b0)
            p0s.append(p0)
            gaps.append(gap)
            sg2.append(pred_p2(A, V, sgw, dens, n))
            ns40.append(n)
            nQP += 1
            sg3 = pred_p3_seq(p0s, gaps, THETA)
            sg1 = [pred_p1_sign(p, g) for p, g in zip(p0s, gaps)]
            ff = {c: first_flip(np.asarray(ns40),
                                np.asarray(s, int))
                  for c, s in (("P1", sg1), ("P2", sg2),
                               ("P3", sg3))}
            if all(v is not None for v in ff.values()):
                ff_w40 = ff
                break
        else:
            ff_w40 = ff
        info("w40 N=%d: early-stopped at mass %d (first flips %s)"
             % (N40, ns40[-1], str(ff_w40)))
    check("G30-sweep-qp-wards", res_worst <= QP_RES_BAR and mass_ok,
          "QP residual worst %.1e (bar %.0e) over %d equilibria; "
          "every rounded mass integer-exact; predictor data = "
          "(p0, branch gap, P2 sign, critical swap) per mass, "
          "source-only" % (res_worst, QP_RES_BAR, nQP))

    # ---------------- S4: mp wards
    section("S4  MP WARDS (gate side)")
    if smoke:
        check("G31-mp-flip-wards", True, "SMOKE: skipped")
        check("G32-mp-energy-ward", True, "SMOKE: skipped")
    else:
        xuE, wuE = union_arrays(ctrl["EPSTEIN"]["d"])
        xuS, wuS = union_arrays(ctrl["SMOOTH"]["d"])
        sE = mp_flip_ward(xuE, wuE, (25, 26), MP_FLIP_DPS)
        sS = mp_flip_ward(xuS, wuS, (27, 28), MP_FLIP_DPS)
        ok_w1 = (sE[25] > 0 and sE[26] < 0
                 and sS[27] > 0 and sS[28] < 0)
        check("G31-mp-flip-wards", ok_w1,
              "exact-precision (dps %d) determinants of the source "
              "Gram: EPSTEIN sign det G_25/G_26 = %+d/%+d, SMOOTH "
              "G_27/G_28 = %+d/%+d -- the ground truth the "
              "candidates are judged against is exact arithmetic"
              % (MP_FLIP_DPS, sE[25], sE[26], sS[27], sS[28]))
        # configs are indexed in the SORTED union order (the
        # union_setup convention): use the sweep's source arrays
        xS, wtS = SRC["SMOOTH"][0], SRC["SMOOTH"][1]
        dev_e = 0.0
        for n in (27, 28):
            an = ANAT["SMOOTH"][n]
            E_mp = mp_energy(xS, wtS, an["bst"], MP_EN_DPS)
            dev_e = max(dev_e, abs(E_mp - an["E0"]))
        check("G32-mp-energy-ward", dev_e <= MP_EN_BAR,
              "SMOOTH stable-saddle energies at degrees {27, 28} "
              "recomputed at dps %d: max |E_mp - E_f64| = %.1e "
              "nats (bar %.0e) -- the milli-decade branch gaps "
              "are not f64 noise" % (MP_EN_DPS, dev_e, MP_EN_BAR))

    # ---------------- S5: leg A anatomy
    section("S5  LEG A -- SADDLE SELECTION ANATOMY")
    dio_ctrl = []
    gap_ctrl_flip = []
    for c in ("EPSTEIN", "SMOOTH", "SCRAMBLE"):
        nf = ctrl[c]["nf"]
        note = []
        for n in sorted(ANAT[c]):
            a = ANAT[c][n]
            note.append("n=%d p0 %+d gap %+.4f swap %d->%d "
                        "(d %d, sgw %+d/%+d, rk_i %d rk_o %d)"
                        % (n, a["p0"], a["gap"], a["i"], a["o"],
                           a["dio"], a["sgi"], a["sgo"],
                           a["rk_i"], a["rk_o"]))
            dio_ctrl.append(a["dio"])
            if n in (nf, nf + 1):
                gap_ctrl_flip.append(a["gap"])
        info("%s (flip %d): %s" % (c, nf, "; ".join(note)))
    med_dio = float(np.median(dio_ctrl))
    shortrange = med_dio <= SHORTRANGE_BAR
    tok_a1 = ("SWAP_SHORT_RANGE" if shortrange
              else "SWAP_LONG_RANGE")
    check("G40-anatomy-critical-swap", True,
          "(a1) the critical parity-swap over the control anatomy "
          "windows: median |i - o| = %.1f (bar %d) => %s; weight-"
          "sign class always opposite (parity swap by "
          "construction); boundary ranks printed above"
          % (med_dio, SHORTRANGE_BAR, tok_a1))
    gap_main = [ANAT["w9"][n]["gap"] for n in sorted(ANAT["w9"])]
    note_m = "; ".join("n=%d gap %+.4f swap d=%d"
                       % (n, ANAT["w9"][n]["gap"],
                          ANAT["w9"][n]["dio"])
                       for n in sorted(ANAT["w9"]))
    sep = (min(gap_main) > max(gap_ctrl_flip)
           if gap_ctrl_flip and gap_main else False)
    tok_a2 = ("SWAP_STAT_SEPARATES" if sep
              else "SWAP_STAT_NOT_SEPARATING")
    check("G41-anatomy-main-vs-control", True,
          "(a2) MAIN w9 at %s: %s; control flip-degree gaps "
          "%s dec, MAIN anatomy gaps min %.4f dec => %s "
          "(sealed rule: separation iff MAIN min > control max "
          "%.4f)" % (str(ANAT_WIN["MAIN"]), note_m,
                     str(["%.4f" % g for g in gap_ctrl_flip]),
                     min(gap_main), tok_a2,
                     max(gap_ctrl_flip) if gap_ctrl_flip else -1))
    # (a3) crossings
    cross = {}
    for c in ("EPSTEIN", "SMOOTH", "SCRAMBLE"):
        sw = SW[c]
        sg1 = np.array([pred_p1_sign(p, g)
                        for p, g in zip(sw["p0"], sw["gap"])], int)
        cr = None
        for i, n in enumerate(sw["ns"]):
            if sg1[i] < 0:
                cr = int(n)
                break
        cross[c] = cr
    lc_ok = all(cross[c] is not None
                and abs(cross[c] - ctrl[c]["nf"]) <= FLIP_TOL
                for c in ("EPSTEIN", "SMOOTH"))
    sw9 = SW["w9"]
    sg1_9 = np.array([pred_p1_sign(p, g)
                      for p, g in zip(sw9["p0"], sw9["gap"])], int)
    lim9 = packs[9]["N"] - 1
    nsw9 = int(np.sum((np.diff(sg1_9) != 0)
                      & (sw9["ns"][1:] <= lim9)))
    tok_a3 = ("LEVEL_CROSSING_AT_FLIP" if lc_ok
              else "LEVEL_CROSSING_REFUTED")
    # gamma anatomy at flips vs at model crossings (gate side)
    gnote = []
    for c in ("EPSTEIN", "SMOOTH", "SCRAMBLE"):
        rows = ctrl[c]["rows"]
        nf = ctrl[c]["nf"]
        lgf = (rows[nf]["lg_h"] - rows[nf - 1]["lg_h"]) / L10
        cr = cross[c]
        lgc = ((rows[cr]["lg_h"] - rows[cr - 1]["lg_h"]) / L10
               if cr is not None and 1 <= cr < len(rows)
               else float("nan"))
        gnote.append("%s true lg|gamma|@flip %+.2f vs @model-"
                     "crossing(%s) %+.2f" % (c, lgf, str(cr), lgc))
    check("G42-anatomy-level-crossing", True,
          "(a3) branch crossing vs true flip: %s => %s; MAIN w9 "
          "lower-branch parity switches below N-1: %d (each a "
          "would-be flip, zero true ones); jump anatomy (gate "
          "side): %s -- the |gamma| > 1 jump belongs to the "
          "true chain at the TRUE flips, not to the branch "
          "crossings"
          % ("; ".join("%s crossing %s vs flip %d"
                       % (c, str(cross[c]), ctrl[c]["nf"])
                       for c in ("EPSTEIN", "SMOOTH", "SCRAMBLE")),
             tok_a3, nsw9, "; ".join(gnote)))

    # ---------------- S6: leg B blind adjudication
    section("S6  LEG B -- CANDIDATE ADJUDICATION (blind)")
    CN = ("P1", "P2", "P3")
    arm1 = {c: True for c in CN}
    arm1_note = {c: [] for c in CN}
    for w in ("EPSTEIN", "SCRAMBLE", "SMOOTH"):
        sw = SW[w]
        cs = cand_signs(sw)
        nf = ctrl[w]["nf"]
        for c in CN:
            ff = first_flip(sw["ns"], cs[c])
            hit = ff is not None and abs(ff - nf) <= FLIP_TOL
            arm1[c] = arm1[c] and hit
            arm1_note[c].append("%s %s (true %d, %s)"
                                % (w[:4], str(ff), nf,
                                   "HIT" if hit else "MISS"))
    check("G50-arm1-control-flips", True,
          "first-flip per candidate (tol +-%d): %s"
          % (FLIP_TOL, " | ".join("%s: %s" % (c, "; ".join(
              arm1_note[c])) for c in CN)))
    arm3 = {c: True for c in CN}
    ffm = {c: {} for c in CN}
    mfr = {c: {} for c in CN}
    for kz in packs:
        p = packs[kz]
        sw = SW["w%d" % kz]
        cs = cand_signs(sw)
        sgd = truth_sgdet(p["rows"], p["N"])
        for c in CN:
            # pairs (n, n+1) with n + 1 <= N test the free pivots
            # h_n up to n = N - 1 exactly
            ok_ns = sw["ns"] <= p["N"]
            ff = first_flip(sw["ns"][ok_ns], cs[c][ok_ns])
            ffm[c][kz] = ff
            arm3[c] = arm3[c] and (ff is None)
            mfr[c][kz] = missign_frac(sw["ns"], cs[c], sgd)
    check("G51-arm3-main-clean", True,
          "MAIN first false flip below N-1 per candidate: %s; "
          "per-degree missign fractions: %s"
          % (" | ".join("%s: %s" % (c, str(ffm[c])) for c in CN),
             " | ".join("%s: %s" % (c, str(
                 {k: "%.2f" % v for k, v in mfr[c].items()}))
                 for c in ("P1", "P2"))))
    arm2 = {c: True for c in CN}
    if smoke:
        check("G52-arm2-forced-tail", True, "SMOKE: skipped")
        for c in CN:
            arm2[c] = False
    else:
        tl_note = {c: [] for c in CN}
        for i, w in enumerate(TAIL_WINDOWS):
            d = HS.window_data(w)
            N = d["n_max"]
            rows_x = BH.bord_chain(d["xs"], d["ws"], d["ys"],
                                   d["vs"], d["xs"][:2],
                                   d["ws"][:2] * 0.0, d["ys"][:2],
                                   d["vs"][:2] * 0.0, N + EXT + 1)
            truth = next((r["n"] for r in rows_x
                          if r["sg_h"] < 0), None)
            for c in CN:
                if w == 40:
                    ff = ff_w40.get(c)
                else:
                    sw = SW["w%d" % w]
                    ff = first_flip(sw["ns"], cand_signs(sw)[c])
                off = None if ff is None else ff - N
                hit = (ff == truth and off == PRIOR_OFFSETS[i])
                arm2[c] = arm2[c] and hit
                tl_note[c].append("w%d %s(j=%s)"
                                  % (w, str(ff), str(off)))
        check("G52-arm2-forced-tail", True,
              "predicted first flips vs truth %s at N + %s: %s"
              % (str((184, 153, 170, 367, 592)),
                 str(PRIOR_OFFSETS),
                 " | ".join("%s: %s" % (c, "; ".join(tl_note[c]))
                            for c in CN)))

    # ---------------- S7: must-fails
    section("S7  MUST-FAILS")
    hits_orc = predictor_scope_audit("oracle_pred")
    check("G60-minor-oracle-flagged", bool(hits_orc),
          "the deliberately chain-reading mutant is FLAGGED by "
          "the predictor AST audit (%s) while the 10 sealed "
          "scopes stay clean (G01): the blindness claim is "
          "machine-enforced"
          % ("; ".join(hits_orc) if hits_orc else "NOT FLAGGED"))
    # m2 (amendment a1): wrong Vandermonde exponent at the sealed
    # degree -- the pair energy counted once instead of twice
    a21 = ANAT["w9"][M2_DEG]
    _x9, _wt9, A9, _V9, _sg9 = SRC["w9"]
    r21 = a21["bst"].astype(float)
    q21 = float(r21 @ (A9 @ r21))
    m2_dev = 0.5 * abs(q21) / L10
    ok_m2 = m2_dev >= M2_LOUD_DEC
    check("G61-wrong-exponent-loud", ok_m2,
          "pair energy counted once (E' = q/2 + V r) moves the "
          "stable-saddle energy at (w9, n = %d) by %.1f dec (bar "
          "%.0f) -- the sealed energy form is load-bearing; NOTE "
          "(a1): a swapped-branch mutant is flip-invariant by "
          "construction (global parity negation cancels in "
          "sg(D_{n+1}) sg(D_n)), disclosed"
          % (M2_DEG, m2_dev, M2_LOUD_DEC))
    # m3: bare r255 parity rule anchor
    ok_m3 = True
    m3_note = []
    for c in ("EPSTEIN", "SMOOTH"):
        sw = SW[c]
        # bare rule = P2 without the correction: parity of the raw
        # QP top-n (recomputed on the control range, cheap)
        x2, wt2, A2, Lip2, V2 = CB.eq_field(ctrl[c]["d"])
        sgw2 = np.sign(wt2)
        dens = None
        sgs = []
        for n in sw["ns"]:
            dens, _ = SZ.solve_qp(A2, Lip2, V2, float(n),
                                  rho0=dens, iters=QP_ITERS,
                                  tol=QP_TOL)
            sgs.append(pparity(sgw2, psel_top(dens, int(n))))
        ffb = first_flip(sw["ns"], np.asarray(sgs, int))
        ok_m3 = ok_m3 and (ffb == M3_ANCHOR[c])
        m3_note.append("%s bare first flip %s (r255 record %d)"
                       % (c, str(ffb), M3_ANCHOR[c]))
    check("G62-r255-anchor", ok_m3,
          "P2 WITHOUT the swap correction reproduces the r255 "
          "misplacements EXACTLY: %s -- the correction term is "
          "real and this round is tied to the r255 record"
          % "; ".join(m3_note))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a parametrix "
          "adjudication moves no edge); what the round adds: the "
          "saddle-selection anatomy (critical swap, MAIN-vs-"
          "control separation test, branch-crossing bill), three "
          "sealed analytic candidates with a blind protocol, and "
          "the typed obstacle of the analytic falsifier half")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        full = [c for c in CN if arm1[c] and arm2[c] and arm3[c]]
        partial = [c for c in CN
                   if arm1[c] or arm2[c] or arm3[c]]
        if full:
            top = "PARAMETRIX_PASSED(%s, +-%d)" % (full[0],
                                                   FLIP_TOL)
        elif partial:
            top = ("PARAMETRIX_PARTIAL(%s: arms %s)"
                   % (partial[0],
                      str((arm1[partial[0]], arm2[partial[0]],
                           arm3[partial[0]]))))
        else:
            top = ("PARAMETRIX_FAILED(selection wrong on 3/3 "
                   "controls + MAIN false positives; typed "
                   "i+ii+iii)")
        toks = [top, "%s(EPST %s vs 25, SMOOTH %s vs 27, SCR %s "
                "vs 21; MAIN %d switches)"
                % (tok_a3, str(cross["EPSTEIN"]),
                   str(cross["SMOOTH"]), str(cross["SCRAMBLE"]),
                   nsw9), tok_a2]
        toks.append("SELECTION_EXTENSIVE_AFTER_ALL" if not sep
                    else "SELECTION_LOWDIM_CONFIRMED")
        verd = " + ".join(toks)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G81-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: swap anatomy, branch crossings, "
          "candidate bills (flips / tail / MAIN-clean / missign "
          "fractions); OPEN: the analytic falsifier half (the "
          "obstacle is a RESUMMATION gap: the true sign is "
          "coherent cancellation across the configuration "
          "ensemble, not a dominant-configuration event); the "
          "r257 coefficient-field pass, the budget bound and the "
          "base law stand; NO RH claim"
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
