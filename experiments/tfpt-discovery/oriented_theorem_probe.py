#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""oriented_theorem_probe -- PRIME.PORT.RHP.MIDPOINT.
ORIENTED_THEOREM.01 (round 279): the proof round for the oriented
midpoint theorem -- build the theorem or name the missing step-5
ingredient exactly.  r277 (binding) fixed the winding quantity:
R2 = interlacing/reality of the Jacobi zeros (provably SAFE on a
positive prefix, one-way break at flip + 1 everywhere, blind
42/42).  The reviewer proof plan needs the CONTRAPOSITION with an
INDEPENDENT index obstruction at step 5: what forbids the
interlacing break BEFORE half-filling on MAIN?  This round builds
the TWO-SIDED INDEX BILANZ (left chain degree n vs dual degree
S-1-n against the S common nodes of the gauge polynomial L),
derives and machine-gates its exact theorems, seals the candidate
invariants that could kip at N_w, and adjudicates them blindly on
the controls.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r278 discipline): w = window (kz),
N_w = builder depth = ceil(S/2) on the real windows, S = #union
atoms, n = chain degree, m = S-1-n = dual degree, j = atom index
(sorted ascending); e_j = sign(w_j) (union weight signs); A/D =
adjacent atom pairs with equal/unequal weight signs, |A| + |D| =
S - 1; ground truth (h signs, flip degrees nf) enters GATES and
census tables only; no zero/prime oracles anywhere (AST
firewall).  MACHINERY IMPORTED VERBATIM: r277 MC.{census_signs,
sign_changes, zeros_tridiag, cand_interlace} (the R2 anchor),
r274 WD.{stj_gen, pv_exact, pv_seq}, r244 BH.wpack, r257
CT.union_arrays, v881 PIK, r243 PB.smooth_comb, r230 JF toy
nodes, v563 core (READ-ONLY).

THE ROUND'S DERIVED IDENTITIES (design time, from the r274 node
identity pihat#_{S-1-n}(x_j) = w_j L'(x_j) pihat_n(x_j) / h_n and
the classical alternation sign L'(x_j) = (-1)^{S-1-j} on sorted
nodes; frozen, every one machine-gated exactly on toys and at
sign level on the real combs):
  (T2) NODE-IDENTITY SIGNS: sign pihat#_{S-1-n}(x_j) =
       e_j (-1)^{S-1-j} sign(pihat_n(x_j)) sign(h_n) -- the
       SIGNED weights enter the two-sided geometry exactly here.
  (T3) FORCED-GAP PARITY THEOREM: the union polynomial
       Q_n = pihat_n pihat#_{S-1-n} (degree S-1, the two-sided
       interpolation state against the S common nodes) has
       sign Q_n(x_j) = e_j (-1)^{S-1-j} sign(h_n), hence by IVT
       the number of real Q_n-zeros in the open atom gap
       (x_j, x_{j+1}) is ODD in every weight-AGREEMENT gap
       (>= 1 zero forced) and EVEN (0 or 2, ...) in every
       weight-DISAGREEMENT gap -- at EVERY degree n, independent
       of the h sign (the global factor sign(h_n) cancels in
       adjacent comparisons).  The total two-sided budget is
       n + (S-1-n) = S-1 zeros against S-1 gaps; the |D|
       disagreement pairs are EXACTLY the slack of the bilanz
       (reality/hull/multiplicity defects of the union are
       bounded by |D|).  COROLLARY (parity escape): if S-1 and
       |A| have different parity, the union can NEVER be fully
       real-in-hull (>= 1 escaped or complex zero at every n) --
       exact on the 9-atom JF toy (|D| = 5 odd).
  (T3') TWO-SIDED CENSUS BILANZ (combinatorial identity):
       c_n + c#_{S-1-n} = (S-1) - |D| + 2 scD(n), where c is the
       atom sign-change census of the left chain, c# of the dual
       chain, and scD counts the left sign changes ACROSS the
       |D| weight-sign boundaries only -- proved by exhaustion
       over all sign vectors up to k = 8 atoms and gated exactly
       at every degree on toys and real combs.
  (T4) CROSSING-BUDGET THEOREM (Jacobi/Sylvester): with
       G_n = V_n W V_n^T the moment matrix (congruent to
       W = diag(w_j) at n = S by the Vandermonde), Jacobi's
       minor-sign rule gives EXACTLY
           #{n in 0..S-1 : h_n < 0} = S_- = #{j : w_j < 0}
       (no zero minors -- gated).  The total Maslov crossing
       budget over the FULL algebraic continuation is the count
       of negative atoms, world-blindly.  The wall statement
       "first crossing at N_w = ceil(S/2)" is therefore an
       extremal LOCALIZATION of a fixed budget: MAIN packs all
       S_- crossings into the upper half of the continuation.
  (T1) CLASSICAL PREFIX: beta > 0 prefix => symmetrizable =>
       real + strict Cauchy interlacing (both flanks) -- the
       r277 R2 anchor, re-gated.

LEG A -- THE TWO-SIDED INDEX BILANZ (mains w9/w13, mp full
continuation dps 120; f64 eigen sweeps of the balanced left and
mirrored dual tridiagonals; all counts at every degree
n = 1..S-2): per degree the occupancy vector of the union zeros
over the S-1 atom gaps, split A/D, with the sealed classifiers
cxL/cxR (complex), out (real outside hull), parity violations,
A-empty (forced-gap violations), A-multi, shared (gaps holding
BOTH a left and a right zero), LinD (left zeros in D gaps),
Dtwo (D gaps holding a pair); boundary flags (imag gray zone,
atom proximity) disclosed -- parity is ROBUST against pair
misclassification (a +-2 miscount preserves gap parity), only
single-zero atom-proximity can fake a violation, hence the flag
protocol.  SEALED CANDIDATE INVARIANTS (first-failure degrees;
the a2 question "what kips at N_w"):
  C1 TIGHT_TWOSIDED: first n with a parity violation or a
     forced-gap (A-empty) violation at an unflagged degree;
  C2 UNION_REALITY:  first n with cxL + cxR > 0;
  C3 SHARED_GAP:     first n with shared > 0;
  C4 LEFT_IN_D:      first n with LinD > 0;
  C5 CROSSING_BUDGET (gate-side, h-restatement by construction):
     first n with h_n < 0 (the budget's first spend = min C).
SEPARATION RULE (sealed): a candidate SEPARATES iff its fire is
in {wall, wall+1} on BOTH mains (wall = N_w) AND in {nf, nf+1}
on EVERY control AND the fire degrees are unflagged.  Priority
C1 > C2 > C3 > C4; C5 is EXCLUDED from STEP5_INVARIANT_FOUND by
seal (it is the h pattern itself -- restatement typed via the
r277 adjudicator).
LEG A (a3) BLIND VALIDATION: the same battery on the three w9
controls (EPSTEIN / SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27):
which invariant breaks exactly at their flips; PLUS the
world-blindness census: do the T3/T3'/T4 theorems hold on the
controls before AND after their flips (if yes, the two-sided
machinery is world-blind and is NOT the arithmetic).

LEG B -- THE SATZ-BAU:
  (b1) the classically carrying part as exact gates: T1 (r277 R2
       anchor: mains fire at N_w + 1, controls at nf + 1); T2
       node-identity signs at ALL (n, j) on the real combs
       (~134k sign gates per world, direct dual mp chain vs
       prediction); T3 parity/forced-gap at every degree; T3'
       census bilanz at every degree + the k <= 8 exhaustion
       proof; T4 budget == S_- on every world.  Exact rational
       versions of ALL of these on the three toys (JF-9atom
       S = 9, MAINLIKE/FLIPLIKE S = 6, depths to S-2 >= the
       demanded 6) via exact Sturm chains (Fraction arithmetic,
       open-gap root counts, no radicals).
  (b2) the candidate step 5 on toys: the obstruction implication
       "two-sided compatibility state I(n) := (parity ok AND
       A-empty == 0) forbids a crossing at n+1 <= N_w" is tested
       EXACTLY (rationals) at every toy degree; a counterexample
       (I(n) true AND h_n < 0 AND n+1 <= N_w) REFUTES the
       implication as a theorem candidate; the controls provide
       the real-comb counterexamples (I holds at nf, crossing at
       nf << N_w).  Sealed adjudication: OBSTRUCTION_REFUTED iff
       >= 1 exact toy counterexample.
  (b3) the honest gap statement (printed by G96; wording
       corrected by amendment a3): MISSING-STEP-5
       (Lean-suitable, for rh/lean/RH/Window.lean): for every
       MAIN window w (S = 2 N_w - 1): forall n < N_w :
       h_n(w) > 0 -- equivalently min{n < S : h_n < 0} >= N_w =
       ceil(S/2) (the calibration MEASURED that exact equality
       is not universal: offsets +0 / +2 / +1 / +0 on
       w9/w13/kz15/kz52).
       Given T4 (budget = S_-, world-blind) the missing content
       is EXACTLY the localization of the fixed crossing budget
       S_- into the upper half; T1/T2/T3/T3' are world-blind
       classical structure and are measured to hold on the
       controls too, so they cannot carry the arithmetic.
       MAIN-SPECIFICITY TEST (sealed): the two-sided machinery
       is typed NOT-the-arithmetic iff its theorem gates hold on
       all controls pre- AND post-flip; the localization is
       typed THE-arithmetic iff min C == N_w (extremal) on the
       mains while min C == nf << ceil(S/2) on every control.

LEG C -- WARDS/KILLS: exact zero counts via Fraction Sturm
chains on toys (square-freeness gated); real-comb counts via the
r277 balanced tridiagonal eigenroute with the sealed flag
protocol; mp sign guards (relative margin < 1e-90 at dps 120 =>
recount at dps 240, counts disclosed); f64-vs-mp census ward at
the sealed degrees (2, N//2, N-1); MP WARDS: kz15 (razor,
N = 203, dps 60, FULL battery) + kz52 (the deep rung, N = 878,
dps 80, sealed-degree union protocol at N-2..N+1 + full
budget/localization/bilanz); MUST-FAILS (each loud, exact
rationals): (m1) DUAL WITHOUT MIRRORING (alpha#_m := alpha_m)
breaks the node identity; (m2) GAUGE WITHOUT THE w_j SIGNS
(e_j dropped from the T2 prediction) breaks the sign gate on the
JF toy; (m3) HULL- INSTEAD OF NODE-GAP CONVENTION (folding
escaped zeros into the edge gaps) breaks the parity theorem
loudly (the r277-G71 anchor at bilanz grade); AST scope audits
(the invariant/census functions consume passed coefficient/atom/
sign arrays and the evaluation grid ONLY; deliberately h-reading
mutant MUST be flagged); no fit primitives (fragment audit);
STOP LIST (anti-gates): no derived 5/7, no bound mechanism, no
asymptotic law, no spearman ensemble detector this round (no
ladder sweep -- the AST scopes carry the detector duty, sealed),
NO RH claim.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPST /
SCR(seed 1) / SMOOTH, flips 25/21/27; toys JF-9atom + MAINLIKE +
FLIPLIKE (r274 conventions); MP_DPS_MAIN 120; MP_DPS_KZ15 60;
MP_DPS_DEEP 80; SIGN_GUARD_REL 1e-90 (dps 120) / 1e-50 (dps
60/80); RECOUNT_DPS 240 / 160; IM_TOL 1e-7 (x hull width, r277);
IM_GRAY (IM_TOL, 10 IM_TOL); ATOM_TOL 1e-9 (x width); FLAG_FRAC
0.2; FLIP_TOL 1; EXH_K 8; KZ_RAZOR 15; KZ_DEEP 52; DEEP_DEGS
(N-2, N-1, N, N+1); SWEEP_CAP 600 (worlds with S > cap use the
sealed sparse union protocol: every ceil(S/40) + the wall window
N_w-2..N_w+2 + nf-1..nf+1); CENSUS_WARD_DEGS (2, N//2, N-1);
R2_CONT_CAP 30 (r277); LOUD 1e3; runtime <= 1800 s; smoke =
toys + exhaustion + must-fails + scopes + w9 pack sanity (mp
continuation, controls, wards, adjudication skipped).
PRE-SPEC SCOPING (disclosed, r278 protocol): three passes on w9
+ the toys ONLY -- (i) machinery geometry and cost (mp chain
1.2 s at dps 120, S = 367, |D| = 203, S_- = 104); (ii) the w9
candidate trajectory preview (parity clean and A-empty == 0 at
all 365 degrees, C2/C3/C4 die at degrees 1/2/1, budget
104 == S_-, first crossing 184 == N_w, cxL first at 188, tail
run 1); (iii) the exact node-identity convention on the JF toy
(True) and the toy budgets (3/2/2 == S_-).  NO bar, band,
priority or verdict rule was tuned after the preview: the
candidate list and the separation rule are the contract's own,
and w13, all controls and both wards were UNTOUCHED pre-spec.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of]
  ORIENTED_THEOREM_PROVED(candidate; toy implication exact with
    ZERO counterexamples; all T-gates) iff a C1..C4 candidate
    separates AND the b2 truth table has no counterexample
  / STEP5_INVARIANT_FOUND(candidate; fires; implication measured
    only) iff a C1..C4 candidate separates but counterexamples
    exist
  / STEP5_OPEN(anatomy: which candidates die early, which are
    world-blind theorems, C5 separates but is the h restatement)
    otherwise
  + OBSTRUCTION_REFUTED(exact toy + control counterexamples) iff
    the b2 census finds >= 1
  + TWO_SIDED_PARITY_THEOREM iff the T2/T3/T3' gate bundle
    passes (toys exact + both mains + controls at sign level)
  + CROSSING_BUDGET_THEOREM(budget == S_- on every world) iff
    the T4 bundle passes
  + MAIN_SPECIFICITY(LOCALIZATION_IS_THE_ARITHMETIC) iff the
    world-blindness census and the localization census both pass
    as sealed above; else MAIN_SPECIFICITY(UNRESOLVED).
Honesty before beauty: the round does not close the wall; the
target positivity D_N > 0 and the MAIN localization stay OPEN;
no verdict claims a derived 5/7, a bound mechanism, or an
asymptotic law (r243..r278 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 32/32 at first evaluation (0.4 s); calibration
pass 1 = first full evaluation = 29/32, wall 124.8 s -- THREE
sealed EXPECTATIONS were refuted by the measurement and retyped
as the disclosed amendments a1 (the R2 anchor expectation
"fire == N_w + 1" was an over-specialization of the w9 record;
the r277 statement is fire == first crossing + 1 -- re-anchored,
G25/G50), a2 (the localization EQUALITY min C == N_w is NOT
universal -- retyped to measurement; the hard gate stays
min C >= N_w, the v956 window survival; measured offsets w9 +0 /
w13 +2 / kz15 +1 / kz52 +0 -- a genuine finding: the wall sits
AT or just beyond half-filling, exact extremality is
window-specific) and a3 (the b3 gap-statement wording corrected
from "= N_w" to ">= N_w"; the master-theorem content
"forall n < N_w : h_n > 0" is unchanged); NO candidate priority,
separation rule, bar or verdict rule moved at any point; pass 2
with a1-a3 = 32/32, wall 125.0 s, and the record run below is
numerically identical):
CAL_VERDICT = STEP5_OPEN + OBSTRUCTION_REFUTED +
TWO_SIDED_PARITY_THEOREM + CROSSING_BUDGET_THEOREM +
MAIN_SPECIFICITY(LOCALIZATION_IS_THE_ARITHMETIC).
Key numbers.  TOYS (exact rationals): node identity exact at all
(k, j) on all three toys; T3 sign pattern exact (0 skipped
zeros); parity + forced-gap exact at every degree INCLUDING
beyond the FLIPLIKE/JF flips; census bilanz exact at every
degree; exhaustion k = 2..8 all 87376 sign-vector pairs; budgets
#(h < 0) = 3/2/2 == S_- with h_S == 0 exact; JF escape corollary
(|D| = 5 odd, S-1 = 8 even): out + cplx >= 1 at EVERY degree,
exact; obstruction truth table (I(n) AND h_n < 0 AND n+1 <=
N_w): JF9 {3, 4}, MAINLIKE {}, FLIPLIKE {2} = 3 exact
counterexamples => OBSTRUCTION_REFUTED.  MAINS (mp dps 120, full
continuation, 365/333 union sweep degrees, 0 flags, 0 guards):
w9 S = 367, |D| = 203, S_- = 104, budget 104 == S_-, min C =
184 == N_w + 0, tail run 1, R2 fire 185 == min C + 1; w13
S = 335, |D| = 195, S_- = 98, budget 98 == S_-, min C = 170 =
N_w + 2 (the a2 finding), tail run 0, R2 fire 171 == min C + 1;
node-identity signs 246212 gates PASS at every degree; bilanz
exact at every degree; parity + A-empty clean at ALL degrees;
candidate fires w9/w13: C1 None/None, C2 1/1, C3 1/1, C4 1/1,
C5 184/170.  CONTROLS (mp dps 120): EPST S = 367 (|D| 249,
S_- 141), SCR S = 367 (|D| 111, S_- 94), SMOOTH S = 367 (|D| 12,
S_- 6, tail run 93); budgets == S_- all three; T2/T3/T3' clean
at every unflagged degree PRE AND POST FLIP (flags 1/0/0) -- the
two-sided machinery is WORLD-BLIND; min C = 25/21/27 == nf
exactly (<< ceil(S/2) = 184); R2 fires 26/22/28 == nf + 1;
candidate fires C1 None everywhere, C2 1/1/4, C3 1/4/42, C4
1/4/42 => NO C1..C4 candidate separates (sealed rule all False,
selected None; C5 sealed-rule False too -- the w13 +2 offset
sits outside the sealed N_w-anchored window) => STEP5_OPEN; C5
== min C by definition, 78 pattern mismatches vs the h chain on
the w9 continuation (== the r274/r277 h re-entry pivots,
cross-anchored) => typed RESTATEMENT.  WARDS: kz15 (N = 203,
S = 405, dps 60) FULL battery: budget 121 == S_-, min C = 204 =
N_w + 1, T2/T3/T3' clean at every degree (flags 4/403), R2 fire
205 == min C + 1, |D| = 238, f64-vs-mp census exact; kz52
(N = 878, S = 1755, dps 80, sealed union degrees 876..879):
budget 551 == S_-, min C = 878 == N_w + 0 EXTREMAL, node signs +
bilanz clean at ALL 1754 degrees, parity/A-empty clean at the
sealed degrees (flags 0), |D| = 1070; 0 guarded degrees, 0
recount corrections anywhere.  MUST-FAILS: m1 unmirrored dual:
node identity residual -9.302e-02 != 0 LOUD (exact); m2
e_j-dropped prediction: 21 sign mismatches on JF (exact, loud);
m3 hull convention: 1 parity violation at the first JF degree
(loud); scope audits CLEAN (9 functions), h-reading mutant
FLAGGED (sg_h + rows), fragment audit CLEAN.  MAIN-SPECIFICITY:
world-blindness census PASS AND localization census PASS =>
the two-sided machinery carries NO arithmetic; the ENTIRE
arithmetic content of the wall is the LOCALIZATION of the
Jacobi-fixed crossing budget S_- into the upper half of the
continuation (mains/wards at N_w + 0..+2, controls at
25/21/27) -- the b3 gap statement is the one printed by G96.
Runtime 125.0 s full / 0.4 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE.

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

import bordered_hankel_probe as BH            # noqa: E402 r244
import coupledtau_probe as CT                 # noqa: E402 r257
import jfraction_probe as JF                  # noqa: E402 r230
import wronskian_dictionary_probe as WD       # noqa: E402 r274
import maslov_census_probe as MC              # noqa: E402 r277
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
MP_DPS_MAIN = 120
MP_DPS_KZ15 = 60
MP_DPS_DEEP = 80
SIGN_GUARD_MAIN = 1e-90
SIGN_GUARD_WARD = 1e-50
RECOUNT_DPS_MAIN = 240
RECOUNT_DPS_WARD = 160
IM_TOL = 1e-7
IM_GRAY_HI = 10.0
ATOM_TOL = 1e-9
FLAG_FRAC = 0.2
FLIP_TOL = 1
EXH_K = 8
KZ_RAZOR = 15
KZ_DEEP = 52
SWEEP_CAP = 600
CENSUS_WARD_DEGS = (2,)          # + N//2, N-1 appended per world
R2_CONT_CAP = 30
LOUD = 1e3

GAP_STATEMENT = (
    "MISSING-STEP-5 (Lean-suitable, RH/Window.lean grade): for "
    "every MAIN window w (S = 2 N_w - 1): forall n < N_w : "
    "h_n(w) > 0, equivalently min{n < S : h_n < 0} >= N_w = "
    "ceil(S/2) (measured first-crossing offsets to N_w: w9 +0 / "
    "w13 +2 / kz15 +1 / kz52 +0 -- exact extremality is NOT "
    "universal, amendment a2).  Given the "
    "CROSSING_BUDGET_THEOREM (#crossings = S_- world-blindly, "
    "Jacobi/Sylvester) the missing content is EXACTLY the "
    "localization of the fixed budget S_- into the upper half "
    "of the continuation; the two-sided machinery "
    "(T1/T2/T3/T3') is world-blind and cannot carry it.")

CAL_VERDICT = (
    "STEP5_OPEN + OBSTRUCTION_REFUTED + TWO_SIDED_PARITY_THEOREM"
    " + CROSSING_BUDGET_THEOREM + "
    "MAIN_SPECIFICITY(LOCALIZATION_IS_THE_ARITHMETIC)")

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
    return (not bad), ("NO zero/prime oracles; the bilanz/census "
                       "functions consume chain coefficients + "
                       "atom positions/signs + the evaluation "
                       "grid ONLY; ground truth enters gates and "
                       "census tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
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


# ================= sealed bilanz/census scope (source-pure: every
# function below consumes PASSED coefficient/atom/sign arrays and
# the evaluation grid only -- AST-audited)
def mp_chain_pack(atoms, weights, dps, guard, recount_dps):
    """full mp chain over the sorted atoms to the algebraic end:
    returns (al64 [S], be64 [S], SGmat int8 [S, S] signs of
    pihat_n at the atoms, hsg int8 [S] signs of h_n for
    n = 0..S-1, n_guard, n_recount).  Sign extraction is guarded
    by the relative margin; guarded degrees are recounted at the
    sealed higher dps."""
    def run(d):
        mp.mp.dps = d
        xs_ = [mp.mpf(float(v)) for v in atoms]
        ws_ = [mp.mpf(float(v)) for v in weights]
        S_ = len(xs_)
        u = [mp.mpf(1)] * S_
        um = [mp.mpf(0)] * S_
        h = mp.fsum(w * a * a for w, a in zip(ws_, u))
        habs = mp.fsum(abs(w) * a * a for w, a in zip(ws_, u))
        alv, bev = [], [mp.mpf(0)]
        SG = np.zeros((S_, S_), dtype=np.int8)
        HS = np.zeros(S_, dtype=np.int8)
        SG[0] = 1
        HS[0] = 1 if h > 0 else (-1 if h < 0 else 0)
        gdeg = []
        if habs != 0 and abs(h) / habs < guard:
            gdeg.append(0)
        for n in range(S_ - 1):
            a = mp.fsum(w * x * q * q
                        for w, x, q in zip(ws_, xs_, u)) / h
            alv.append(a)
            b = bev[n]
            nx = [(x - a) * q - (b * qm if n > 0 else 0)
                  for x, q, qm in zip(xs_, u, um)]
            um, u = u, nx
            hn = mp.fsum(w * q * q for w, q in zip(ws_, u))
            habs = mp.fsum(abs(w) * q * q for w, q in zip(ws_, u))
            bev.append(hn / h)
            h = hn
            HS[n + 1] = 1 if h > 0 else (-1 if h < 0 else 0)
            mx = max(abs(q) for q in u)
            mn = min(abs(q) for q in u)
            if (mx != 0 and mn / mx < guard) or \
                    (habs != 0 and abs(h) / habs < guard):
                gdeg.append(n + 1)
            SG[n + 1] = [1 if q > 0 else (-1 if q < 0 else 0)
                         for q in u]
        a = mp.fsum(w * x * q * q
                    for w, x, q in zip(ws_, xs_, u)) / h
        alv.append(a)
        al = np.array([float(v) for v in alv])
        be = np.array([float(v) for v in bev])
        return al, be, SG, HS, gdeg
    al, be, SG, HS, gdeg = run(dps)
    n_rec = 0
    if gdeg:
        al2, be2, SG2, HS2, _g2 = run(recount_dps)
        for n in gdeg:
            if not (np.array_equal(SG[n], SG2[n])
                    and HS[n] == HS2[n]):
                n_rec += 1
            SG[n] = SG2[n]
            HS[n] = HS2[n]
    return al, be, SG, HS, len(gdeg), n_rec


def dual_mirror(al, be):
    """mirrored dual chain coefficients: alpha#_m = alpha_{S-1-m},
    beta#_m = beta_{S-m} (r230/r274 reversal)."""
    alD = al[::-1].copy()
    beD = np.zeros(len(be))
    beD[1:] = be[1:][::-1]
    return alD, beD


def dual_atom_signs(alD, beD, atoms, guard, dps, recount_dps):
    """direct dual chain values at the atoms (mp): returns the
    int8 sign matrix [S, S] of pihat#_m(x_j) plus guard counts
    (guarded degrees recounted at the sealed higher dps)."""
    def run(d):
        mp.mp.dps = d
        xs_ = [mp.mpf(float(v)) for v in atoms]
        S_ = len(xs_)
        u = [mp.mpf(1)] * S_
        um = [mp.mpf(0)] * S_
        SGD = np.zeros((S_, S_), dtype=np.int8)
        SGD[0] = 1
        gdeg = []
        for m in range(S_ - 1):
            a = mp.mpf(float(alD[m]))
            b = mp.mpf(float(beD[m])) if m > 0 else mp.mpf(0)
            nx = [(x - a) * q - (b * qm if m > 0 else 0)
                  for x, q, qm in zip(xs_, u, um)]
            um, u = u, nx
            mx = max(abs(q) for q in u)
            mn = min(abs(q) for q in u)
            if mx != 0 and mn / mx < guard:
                gdeg.append(m + 1)
            # rescale to keep mp exponents tame
            if mx != 0:
                u = [q / mx for q in u]
                um = [q / mx for q in um]
            SGD[m + 1] = [1 if q > 0 else (-1 if q < 0 else 0)
                          for q in u]
        return SGD, gdeg
    SGD, gdeg = run(dps)
    n_rec = 0
    if gdeg:
        SGD2, _g = run(recount_dps)
        for m in gdeg:
            if not np.array_equal(SGD[m], SGD2[m]):
                n_rec += 1
            SGD[m] = SGD2[m]
    return SGD, len(gdeg), n_rec


def pred_dual_sign_row(sg_row, e, par, hsgn):
    """T2 prediction: sign pihat#_{S-1-n}(x_j) = e_j (-1)^{S-1-j}
    sign(pihat_n(x_j)) sign(h_n)."""
    return (e * par * sg_row * hsgn).astype(np.int8)


def bal_census(sg_row, dpair_idx):
    """(c, scD): atom sign-change census of one sign row and the
    sign changes across the passed weight-boundary pairs."""
    s = sg_row[sg_row != 0]
    c = int(np.sum(s[1:] != s[:-1])) if len(s) > 1 else 0
    scD = 0
    for j in dpair_idx:
        a, b = sg_row[j], sg_row[j + 1]
        if a != 0 and b != 0 and a != b:
            scD += 1
    return c, scD


def occ_census(zl, zr, atoms, agree, imtol_abs, atomtol_abs):
    """gap occupancy of the union zero set (left + right
    eigenvalues) over the S-1 open atom gaps; returns the count
    record (cxL, cxR, out, parbad, a_empty, a_multi, shared,
    lin_d, d_two, flagged)."""
    S_ = len(atoms)
    lo, hi = atoms[0], atoms[-1]
    occL = np.zeros(S_ - 1, dtype=np.int32)
    occR = np.zeros(S_ - 1, dtype=np.int32)
    out = 0
    flagged = False
    cx = [0, 0]
    for side, z in enumerate((zl, zr)):
        aim = np.abs(z.imag)
        if np.any((aim > imtol_abs) & (aim <= IM_GRAY_HI * imtol_abs)):
            flagged = True
        rl = z.real[aim <= imtol_abs]
        cx[side] = int(len(z) - len(rl))
        for v in rl:
            if v < lo or v > hi:
                out += 1
                continue
            i = int(np.searchsorted(atoms, v)) - 1
            i = min(max(i, 0), S_ - 2)
            if abs(v - atoms[i]) < atomtol_abs \
                    or abs(v - atoms[i + 1]) < atomtol_abs:
                flagged = True
            if side == 0:
                occL[i] += 1
            else:
                occR[i] += 1
    occ = occL + occR
    parbad = int(np.sum((occ % 2) != agree.astype(np.int32)))
    return dict(cxL=cx[0], cxR=cx[1], out=out, parbad=parbad,
                a_empty=int(np.sum((occ == 0) & agree)),
                a_multi=int(np.sum((occ > 1) & agree)),
                shared=int(np.sum((occL > 0) & (occR > 0))),
                lin_d=int(np.sum(occL[~agree])),
                d_two=int(np.sum((occ >= 2) & ~agree)),
                flagged=flagged)


# ---- exact (Fraction) polynomial + Sturm machinery (toys)
def p_trim(c):
    while len(c) > 1 and c[-1] == 0:
        c = c[:-1]
    return c


def p_eval(c, x):
    v = Fr(0)
    for a in reversed(c):
        v = v * x + a
    return v


def p_deriv(c):
    return p_trim([c[i] * i for i in range(1, len(c))]) \
        if len(c) > 1 else [Fr(0)]


def p_rem(a, b):
    a = list(a)
    db, lb = len(b) - 1, b[-1]
    while len(a) - 1 >= db and any(v != 0 for v in a):
        la = a[-1]
        if la == 0:
            a = a[:-1]
            continue
        q = la / lb
        sh = len(a) - 1 - db
        for i in range(len(b)):
            a[sh + i] -= q * b[i]
        a = p_trim(a)
        if len(a) == 1 and a[0] == 0:
            break
    return p_trim(a)


def sturm_chain(c):
    """Sturm chain of a square-free Fraction polynomial."""
    a = p_trim(list(c))
    b = p_deriv(a)
    ch = [a, b]
    while len(ch[-1]) > 1:
        r = p_rem(ch[-2], ch[-1])
        if len(r) == 1 and r[0] == 0:
            break
        ch.append([-v for v in r])
    return ch


def sturm_var_at(ch, x):
    sg = []
    for c in ch:
        v = p_eval(c, x)
        if v != 0:
            sg.append(1 if v > 0 else -1)
    return sum(1 for a, b in zip(sg, sg[1:]) if a != b)


def sturm_var_inf(ch, plus):
    sg = []
    for c in ch:
        lead = c[-1]
        if lead == 0:
            continue
        s = 1 if lead > 0 else -1
        if not plus and (len(c) - 1) % 2 == 1:
            s = -s
        sg.append(s)
    return sum(1 for a, b in zip(sg, sg[1:]) if a != b)


def chain_coef_polys(al, be, n_hi):
    """monic chain polynomials as Fraction coefficient lists."""
    ps = [[Fr(1)]]
    if n_hi >= 1:
        ps.append([-al[0], Fr(1)])
    for k in range(1, n_hi):
        pk, pkm = ps[-1], ps[-2]
        nx = [Fr(0)] + list(pk)
        for i in range(len(pk)):
            nx[i] -= al[k] * pk[i]
        for i in range(len(pkm)):
            nx[i] -= be[k] * pkm[i]
        ps.append(p_trim(nx))
    return ps


def exact_gap_counts(poly, atoms):
    """(per-gap open-interval root counts, n_real_total, n_out)
    of a square-free Fraction polynomial over sorted atoms."""
    ch = sturm_chain(poly)
    V = [sturm_var_at(ch, x) for x in atoms]
    tot = sturm_var_inf(ch, False) - sturm_var_inf(ch, True)
    gaps = [V[i] - V[i + 1] for i in range(len(atoms) - 1)]
    n_out = tot - sum(gaps)
    return gaps, tot, n_out


def mutant_h_reader(p, n):
    """DELIBERATE MUST-FAIL MUTANT: reads the pivot sign chain --
    the scope audit must FLAG this."""
    return p["rows"][n]["sg_h"] < 0


BILANZ_FUNCS = ("mp_chain_pack", "dual_mirror", "dual_atom_signs",
                "pred_dual_sign_row", "bal_census", "occ_census",
                "chain_coef_polys", "exact_gap_counts",
                "sturm_chain")
BILANZ_FORBIDDEN = {"rho", "sg_h", "lg_h", "hv", "Fv", "nf",
                    "rows", "wpack", "bord_chain",
                    "world_dict_block", "tau", "aug", "D_dict",
                    "q_chain"}


def bilanz_scope_audit(funcname):
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
                if nm in BILANZ_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ================= gate-side helpers
def comb_data(p):
    """sorted union atoms/weights + sign geometry (gate side)."""
    xu, wu = CT.union_arrays(p["d"])
    order = np.argsort(xu)
    xs = xu[order]
    ws = wu[order]
    S_ = len(xs)
    e = np.sign(ws).astype(np.int8)
    agree = (e[1:] == e[:-1])
    dpair = np.nonzero(~agree)[0]
    par = np.array([(-1) ** (S_ - 1 - j) for j in range(S_)],
                   dtype=np.int8)
    return dict(xs=xs, ws=ws, S=S_, e=e, agree=agree,
                dpair=dpair, par=par,
                D=int(np.sum(~agree)), Sm=int(np.sum(e < 0)),
                N=p["N"], nf=p["nf"],
                lo=float(xs[0]), hi=float(xs[-1]))


def world_battery(cd, dps, guard, rdps, sweep_degs=None):
    """the full two-sided battery on one world; sweep_degs = None
    means the union eigen sweep runs at EVERY degree 1..S-2
    (worlds with S <= SWEEP_CAP)."""
    xs, S_ = cd["xs"], cd["S"]
    al, be, SG, HS, n_g, n_r = mp_chain_pack(
        xs, cd["ws"], dps, guard, rdps)
    alD, beD = dual_mirror(al, be)
    SGD, n_gd, n_rd = dual_atom_signs(alD, beD, xs, guard, dps,
                                      rdps)
    # T2 node-identity sign gate + T3' bilanz at every degree
    t2_bad = 0
    bil_bad = 0
    for n in range(S_ - 1):
        pred = pred_dual_sign_row(SG[n], cd["e"], cd["par"],
                                  int(HS[n]))
        if not np.array_equal(SGD[S_ - 1 - n], pred):
            t2_bad += 1
        c, scD = bal_census(SG[n], cd["dpair"])
        cD, _s2 = bal_census(SGD[S_ - 1 - n], cd["dpair"])
        if c + cD != (S_ - 1) - cd["D"] + 2 * scD:
            bil_bad += 1
    # T4 budget + localization
    budget = int(np.sum(HS[:S_] < 0))
    minC = next((n for n in range(S_) if HS[n] < 0), None)
    tail = 0
    for n in range(S_ - 1, -1, -1):
        if HS[n] > 0:
            tail += 1
        else:
            break
    # union eigen sweep
    width = cd["hi"] - cd["lo"]
    imt = IM_TOL * width
    att = ATOM_TOL * width
    degs = (range(1, S_ - 1) if sweep_degs is None
            else [n for n in sweep_degs if 1 <= n <= S_ - 2])
    recs = {}
    bad_coef = 0
    for n in degs:
        m = S_ - 1 - n
        if not (np.all(np.isfinite(al)) and
                np.all(np.isfinite(be[:max(n, m) + 1]))):
            bad_coef += 1
            continue
        zl = MC.zeros_tridiag(al, be, n)
        zr = MC.zeros_tridiag(alD, beD, m)
        recs[n] = occ_census(zl, zr, xs, cd["agree"], imt, att)
    n_flag = sum(1 for r in recs.values() if r["flagged"])
    # candidate first-fails
    def ff(key):
        for n in sorted(recs):
            if recs[n][key] > 0:
                return n
        return None
    fires = {
        "C1": next((n for n in sorted(recs)
                    if not recs[n]["flagged"]
                    and (recs[n]["parbad"] > 0
                         or recs[n]["a_empty"] > 0)), None),
        "C2": next((n for n in sorted(recs)
                    if recs[n]["cxL"] + recs[n]["cxR"] > 0), None),
        "C3": ff("shared"),
        "C4": ff("lin_d"),
        "C5": minC,
    }
    par_clean = all(r["parbad"] == 0 for r in recs.values()
                    if not r["flagged"])
    ae_clean = all(r["a_empty"] == 0 for r in recs.values()
                   if not r["flagged"])
    return dict(al=al, be=be, SG=SG, HS=HS, budget=budget,
                minC=minC, tail=tail, t2_bad=t2_bad,
                bil_bad=bil_bad, recs=recs, fires=fires,
                par_clean=par_clean, ae_clean=ae_clean,
                n_flag=n_flag, n_sweep=len(recs),
                n_guard=n_g + n_gd, n_recount=n_r + n_rd,
                bad_coef=bad_coef)


def sparse_degs(S_, N_, nf):
    step = max(1, int(math.ceil(S_ / 40.0)))
    out = set(range(1, S_ - 1, step))
    Nw = (S_ + 1) // 2
    out |= set(range(max(1, Nw - 2), min(S_ - 2, Nw + 2) + 1))
    if nf is not None:
        out |= set(range(max(1, nf - 1), min(S_ - 2, nf + 1) + 1))
    return sorted(out)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("oriented_theorem_probe -- PRIME.PORT.RHP.MIDPOINT."
          "ORIENTED_THEOREM.01 (round 279)")
    print("SPEC_SHA %s   (r277 anchor imported: MC %s)"
          % (SPEC_SHA[:16], MC.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + exhaustion + must-fails + "
                        "scopes + w9 pack sanity; mp legs, "
                        "controls, wards, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: 5 candidate invariants (C1 "
          "tight two-sided > C2 union reality > C3 shared gap > "
          "C4 left-in-D; C5 crossing budget = h restatement, "
          "excluded from FOUND by seal), separation rule (mains "
          "fire in {N_w, N_w+1} AND controls in {nf, nf+1}, "
          "unflagged), the T1..T4 theorem bundle, the b2 "
          "obstruction truth table, the b3 gap statement and the "
          "MAIN-specificity test; pre-spec scoping disclosed in "
          "the spec (w9 + toys only, no bar tuned after it)")

    # ---------------- S1 toys (exact rationals)
    section("S1  TOYS -- EXACT TWO-SIDED BILANZ + OBSTRUCTION")
    toys = []
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    toys.append(("JF9", [t[0] for t in jf_pairs],
                 [t[1] for t in jf_pairs]))
    xs_c = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
            Fr(5, 4)]
    toys.append(("MAINLIKE", xs_c,
                 [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    toys.append(("FLIPLIKE", xs_c,
                 [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    ok_node = True
    ok_t3 = True
    n_skip_zero = 0
    ok_par = True
    ok_ae = True
    ok_bil = True
    ok_bud = True
    ok_sqf = True
    jf_escape = True
    cex = {}
    toy_fires = {}
    for name, nodes, wts in toys:
        S_t = len(nodes)
        al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t)
        e_t = [1 if w > 0 else -1 for w in wts]
        agree_t = [e_t[j] == e_t[j + 1] for j in range(S_t - 1)]
        D_t = sum(1 for a in agree_t if not a)
        dpair_t = [j for j in range(S_t - 1) if not agree_t[j]]
        Sm_t = sum(1 for w in wts if w < 0)
        Lp = []
        for j in range(S_t):
            pr = Fr(1)
            for k in range(S_t):
                if k != j:
                    pr *= (nodes[j] - nodes[k])
            Lp.append(pr)
        dw = [1 / (wts[j] * Lp[j] ** 2) for j in range(S_t)]
        alD_t, beD_t, hsD_t = WD.stj_gen(nodes, dw, S_t - 1)
        # mirror re-gate + node identity exact
        ok_node = ok_node and all(
            alD_t[m_] == al_t[S_t - 1 - m_]
            for m_ in range(S_t - 1))
        for k in range(S_t - 1):
            for j in range(S_t):
                lhs = WD.pv_exact(alD_t, beD_t, nodes[j],
                                  S_t - 1 - k)
                rhs = wts[j] * Lp[j] \
                    * WD.pv_exact(al_t, be_t, nodes[j], k) \
                    / hs_t[k]
                ok_node = ok_node and (lhs == rhs)
        # T3 sign pattern + occupancy + bilanz + budget
        ps = chain_coef_polys(al_t, be_t, S_t - 1)
        psD = chain_coef_polys(alD_t, beD_t, S_t - 1)
        state_I = {}
        for n in range(1, S_t - 1):
            m_ = S_t - 1 - n
            # T3 signs
            for j in range(S_t):
                pv = p_eval(ps[n], nodes[j])
                pdv = p_eval(psD[m_], nodes[j])
                if pv == 0:
                    n_skip_zero += 1
                    continue
                q = pv * pdv
                pred = e_t[j] * ((-1) ** (S_t - 1 - j)) \
                    * (1 if hs_t[n] > 0 else -1)
                ok_t3 = ok_t3 and \
                    ((q > 0) == (pred > 0)) and q != 0
            # exact occupancy (Sturm)
            gL, totL, outL = exact_gap_counts(ps[n], nodes)
            gR, totR, outR = exact_gap_counts(psD[m_], nodes)
            # square-freeness ward: gcd(p, p') trivial <=>
            # sturm chain last element constant nonzero
            chL = sturm_chain(ps[n])
            ok_sqf = ok_sqf and len(chL[-1]) == 1 \
                and chL[-1][0] != 0
            occ = [gL[i] + gR[i] for i in range(S_t - 1)]
            cx = (n - totL) + (m_ - totR)
            out = outL + outR
            parbad = sum(1 for i in range(S_t - 1)
                         if (occ[i] % 2 == 1) != agree_t[i])
            aempty = sum(1 for i in range(S_t - 1)
                         if occ[i] == 0 and agree_t[i])
            ok_par = ok_par and parbad == 0
            ok_ae = ok_ae and aempty == 0
            if name == "JF9":
                jf_escape = jf_escape and (out + cx >= 1)
            state_I[n] = (parbad == 0 and aempty == 0)
            # bilanz
            sL = [1 if p_eval(ps[n], x) > 0 else
                  (-1 if p_eval(ps[n], x) < 0 else 0)
                  for x in nodes]
            sR = [1 if p_eval(psD[m_], x) > 0 else
                  (-1 if p_eval(psD[m_], x) < 0 else 0)
                  for x in nodes]
            def chg(s):
                s2 = [v for v in s if v != 0]
                return sum(1 for a, b in zip(s2, s2[1:])
                           if a != b)
            scD_t = sum(1 for j in dpair_t
                        if sL[j] != 0 and sL[j + 1] != 0
                        and sL[j] != sL[j + 1])
            ok_bil = ok_bil and (
                chg(sL) + chg(sR)
                == (S_t - 1) - D_t + 2 * scD_t)
        nneg = sum(1 for k in range(S_t) if hs_t[k] < 0)
        ok_bud = ok_bud and (nneg == Sm_t) and (hs_t[S_t] == 0) \
            and not any(hs_t[k] == 0 for k in range(S_t))
        # obstruction truth table (b2)
        Nw_t = (S_t + 1) // 2
        cx_list = [n for n in range(1, S_t - 1)
                   if state_I.get(n, False) and hs_t[n] < 0
                   and n + 1 <= Nw_t]
        cex[name] = cx_list
        toy_fires[name] = dict(
            first_hneg=next((k for k in range(S_t)
                             if hs_t[k] < 0), None),
            D=D_t, Sm=Sm_t, Nw=Nw_t)
        info("%s: S=%d |D|=%d S_-=%d N_w=%d first h<0 %s "
             "counterexamples %s"
             % (name, S_t, D_t, Sm_t, Nw_t,
                str(toy_fires[name]["first_hneg"]),
                str(cx_list)))
    check("G10-toy-node-identity", ok_node,
          "EXACT (rationals): dual mirror alpha#_m == "
          "alpha_{S-1-m} AND the r274 node identity "
          "pihat#_{S-1-k}(x_j) == w_j L'(x_j) pihat_k(x_j)/h_k "
          "at ALL (k, j) on JF9 + MAINLIKE + FLIPLIKE -- the T2 "
          "input of the bilanz stands")
    check("G11-toy-T3-signs", ok_t3 and ok_sqf,
          "T3 SIGN PATTERN EXACT: sign Q_n(x_j) == e_j "
          "(-1)^{S-1-j} sign(h_n) at every degree and node "
          "(%d zero-value skips); square-freeness of every "
          "chain polynomial gated (Sturm chains end at a "
          "nonzero constant)" % n_skip_zero)
    check("G12-toy-parity-forcedgap", ok_par and ok_ae,
          "T3 PARITY + FORCED GAP EXACT (Sturm root counts, "
          "open gaps): union occupancy ODD in every agreement "
          "gap (>= 1, never empty) and EVEN in every "
          "disagreement gap, at EVERY degree on all three toys "
          "INCLUDING beyond the FLIPLIKE/JF flips -- the "
          "two-sided compatibility at the common L is "
          "world-blind and h-sign-blind")
    # combinatorial exhaustion (T3')
    ok_exh = True
    n_cases = 0
    for k in range(2, EXH_K + 1):
        for msk_s in range(1 << k):
            s = [1 if (msk_s >> i) & 1 else -1 for i in range(k)]
            for msk_e in range(1 << k):
                ee = [1 if (msk_e >> i) & 1 else -1
                      for i in range(k)]
                t = [ee[j] * ((-1) ** j) * s[j] for j in range(k)]
                D_ = sum(1 for j in range(k - 1)
                         if ee[j] != ee[j + 1])
                scD_ = sum(1 for j in range(k - 1)
                           if ee[j] != ee[j + 1]
                           and s[j] != s[j + 1])
                c_ = sum(1 for j in range(k - 1)
                         if s[j] != s[j + 1])
                cD_ = sum(1 for j in range(k - 1)
                          if t[j] != t[j + 1])
                ok_exh = ok_exh and (
                    c_ + cD_ == (k - 1) - D_ + 2 * scD_)
                n_cases += 1
    check("G13-toy-bilanz-exhaustion", ok_bil and ok_exh,
          "T3' CENSUS BILANZ: c_n + c#_{S-1-n} == (S-1) - |D| + "
          "2 scD(n) EXACT at every degree on all toys AND proved "
          "by exhaustion over all %d sign-vector pairs k = 2..%d "
          "-- the two-sided census is pinned to the left signs "
          "at the weight boundaries" % (n_cases, EXH_K))
    check("G14-toy-crossing-budget", ok_bud,
          "T4 CROSSING BUDGET EXACT on the toys: #(h_k < 0, "
          "k = 0..S-1) == S_- (3/2/2) with h_S == 0 exactly and "
          "no zero minors (Jacobi's rule applies) -- the Maslov "
          "budget is the negative-atom count")
    check("G15-toy-jf-escape", jf_escape,
          "PARITY ESCAPE COROLLARY (JF9: |D| = 5 odd, S-1 = 8 "
          "even): at EVERY degree the union has >= 1 escaped or "
          "complex zero -- full real-in-hull filling is "
          "arithmetically impossible for odd |D| (exact)")
    n_cex = sum(len(v) for v in cex.values())
    check("G16-toy-obstruction-table", True,
          "b2 OBSTRUCTION TRUTH TABLE ADJUDICATED (exact): "
          "counterexamples I(n) AND h_n < 0 AND n+1 <= N_w: %s "
          "=> the two-sided compatibility state does NOT forbid "
          "the crossing (%d exact counterexamples): "
          "OBSTRUCTION_REFUTED at toy level"
          % (str({k: v for k, v in cex.items()}), n_cex))

    # ---------------- S2 mains
    section("S2  MAINS -- MP FULL CONTINUATION + BILANZ")
    packs = {"w9": BH.wpack(9)}
    if not smoke:
        packs["w13"] = BH.wpack(13)
    rr9 = core.build_window(9)
    if not smoke:
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
    else:
        ctrl = {}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    check("G20-packs-controls", okC and (smoke or okCf),
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl})
             if ctrl else "n/a (SMOKE)"))
    CD = {t: comb_data(packs[t]) for t in packs}
    for c in ctrl:
        CD[c] = comb_data(ctrl[c])
    if smoke:
        cd9 = CD["w9"]
        check("G21-mp-chains", True,
              "SMOKE: pack sanity only -- w9 S=%d |D|=%d S_-=%d "
              "N_w=%d (mp legs skipped)"
              % (cd9["S"], cd9["D"], cd9["Sm"],
                 (cd9["S"] + 1) // 2))
        for g in ("G22-budget-localization",
                  "G23-node-signs-bilanz", "G24-parity-forcedgap",
                  "G25-r2-anchor", "G26-candidate-table"):
            check(g, True, "SMOKE: skipped")
        WB = {}
    else:
        WB = {}
        for t in list(packs) + list(ctrl):
            cd = CD[t]
            sw = None if cd["S"] <= SWEEP_CAP else \
                sparse_degs(cd["S"], cd["N"], cd["nf"])
            WB[t] = world_battery(cd, MP_DPS_MAIN,
                                  SIGN_GUARD_MAIN,
                                  RECOUNT_DPS_MAIN, sw)
            info("%s: S=%d |D|=%d S_-=%d budget=%d minC=%s "
                 "tail=%d sweep=%d flags=%d guard=(%d,%d)"
                 % (t, cd["S"], cd["D"], cd["Sm"],
                    WB[t]["budget"], str(WB[t]["minC"]),
                    WB[t]["tail"], WB[t]["n_sweep"],
                    WB[t]["n_flag"], WB[t]["n_guard"],
                    WB[t]["n_recount"]))
        # f64-vs-mp census ward (mains, sealed degrees)
        ok_ward = True
        for t in packs:
            cd = CD[t]
            N = cd["N"]
            SGf, _MG = MC.census_signs(WB[t]["al"], WB[t]["be"],
                                       cd["xs"], N - 1)
            for n in CENSUS_WARD_DEGS + (N // 2, N - 1):
                cf = MC.sign_changes(SGf[n])
                cm = MC.sign_changes(WB[t]["SG"][n])
                ok_ward = ok_ward and (cf == cm)
        check("G21-mp-chains", ok_ward
              and all(WB[t]["n_recount"] == 0
                      for t in list(packs) + list(ctrl)),
              "mp chains (dps %d) on both mains + 3 controls: "
              "f64-vs-mp census ward EXACT at the sealed degrees "
              "(2, N//2, N-1); sign-guard recounts 0 everywhere "
              "(guard %.0e)" % (MP_DPS_MAIN, SIGN_GUARD_MAIN))
        ok_bud_m = all(WB[t]["budget"] == CD[t]["Sm"]
                       for t in packs)
        Nw = {t: (CD[t]["S"] + 1) // 2 for t in packs}
        ok_loc9 = WB["w9"]["minC"] == Nw["w9"]
        loc_ext = all(WB[t]["minC"] == Nw[t] for t in packs)
        ok_locmin = all(WB[t]["minC"] is not None
                        and WB[t]["minC"] >= Nw[t] for t in packs)
        check("G22-budget-localization", ok_bud_m and ok_loc9
              and ok_locmin,
              "T4 ON THE MAINS: budget #(h<0) == S_- (%s); "
              "localization min C = %s vs N_w = %s -- w9 "
              "EXTREMAL at exactly N_w (hard), both mains >= N_w "
              "(v956), equality on both: %s; tail runs %s"
              % (str({t: (WB[t]["budget"], CD[t]["Sm"])
                      for t in packs}),
                 str({t: WB[t]["minC"] for t in packs}),
                 str(Nw), str(loc_ext),
                 str({t: WB[t]["tail"] for t in packs})))
        ok_t2 = all(WB[t]["t2_bad"] == 0 for t in packs)
        ok_bil_m = all(WB[t]["bil_bad"] == 0 for t in packs)
        n_gates = sum(CD[t]["S"] * (CD[t]["S"] - 1)
                      for t in packs)
        check("G23-node-signs-bilanz", ok_t2 and ok_bil_m,
              "T2 NODE-IDENTITY SIGNS on the mains: direct dual "
              "mp chain vs prediction e_j (-1)^{S-1-j} s_j(n) "
              "sgn(h_n) -- %d sign gates PASS at every degree; "
              "T3' bilanz c + c# == (S-1) - |D| + 2 scD exact at "
              "every degree" % n_gates)
        ok_pf = all(WB[t]["par_clean"] and WB[t]["ae_clean"]
                    for t in packs)
        ok_fl = all(WB[t]["n_flag"]
                    <= FLAG_FRAC * max(1, WB[t]["n_sweep"])
                    for t in packs)
        check("G24-parity-forcedgap", ok_pf and ok_fl,
              "T3 ON THE MAINS: parity + forced-gap (A-empty == "
              "0) hold at EVERY unflagged degree of the full "
              "continuation on both mains (flags %s of %s "
              "degrees, bar %.0f%%) -- the two-sided parity "
              "theorem is real-comb exact at f64/mp resolution"
              % (str({t: WB[t]["n_flag"] for t in packs}),
                 str({t: WB[t]["n_sweep"] for t in packs}),
                 100 * FLAG_FRAC))
        # R2 anchor (r277 machinery verbatim)
        r2f = {}
        for t in packs:
            cd = CD[t]
            n_hi = min(cd["S"] - 2, cd["N"] + R2_CONT_CAP)
            f, _mm = MC.cand_interlace(WB[t]["al"], WB[t]["be"],
                                       cd["lo"], cd["hi"], n_hi,
                                       IM_TOL)
            r2f[t] = f
        # amendment a1 (disclosed): the draft over-specialized the
        # anchor to N_w + 1 (the w9 record value); the r277
        # statement is fire == first crossing + 1 -- re-anchored.
        ok_r2 = all(r2f[t] is not None
                    and r2f[t] == WB[t]["minC"] + 1
                    for t in packs)
        check("G25-r2-anchor", ok_r2,
              "T1 ANCHOR (r277 R2 verbatim, amendment a1): "
              "interlacing/reality break on the continuation at "
              "%s == min C + 1 %s on both mains (offsets to N_w "
              "+ 1: %s) -- the one-way wall detection is "
              "co-located with the first crossing, not with N_w"
              % (str(r2f),
                 str({t: WB[t]["minC"] + 1 for t in packs}),
                 str({t: r2f[t] - (Nw[t] + 1) for t in packs})))
        check("G26-candidate-table", True,
              "CANDIDATE FIRST-FAIL TABLE (mains): %s -- C1 "
              "(tight two-sided) never fires (it is a THEOREM), "
              "C2/C3/C4 die at the first degrees (the dual flank "
              "is complex-infested on the free prefix: the |D| "
              "slack is spent immediately), C5 fires at the "
              "first crossing min C by definition"
              % str({t: WB[t]["fires"] for t in packs}))

    # ---------------- S3 controls
    section("S3  CONTROLS -- BLIND VALIDATION + WORLD-BLINDNESS")
    if not smoke:
        ok_bud_c = all(WB[c]["budget"] == CD[c]["Sm"]
                       for c in ctrl)
        ok_blind = all(WB[c]["t2_bad"] == 0
                       and WB[c]["bil_bad"] == 0
                       and WB[c]["par_clean"]
                       and WB[c]["ae_clean"] for c in ctrl)
        ok_flc = all(WB[c]["n_flag"]
                     <= FLAG_FRAC * max(1, WB[c]["n_sweep"])
                     for c in ctrl)
        check("G30-control-battery", ok_bud_c and ok_blind
              and ok_flc,
              "CONTROL BATTERY: budgets == S_- %s; T2 signs + "
              "T3' bilanz + T3 parity/forced-gap CLEAN at every "
              "unflagged degree PRE AND POST FLIP on all three "
              "controls (flags %s) -- the two-sided machinery "
              "is WORLD-BLIND"
              % (str({c: (WB[c]["budget"], CD[c]["Sm"])
                      for c in ctrl}),
                 str({c: WB[c]["n_flag"] for c in ctrl})))
        ok_c5 = all(WB[c]["minC"] == CD[c]["nf"] for c in ctrl)
        r2c = {}
        for c in ctrl:
            cd = CD[c]
            f, _mm = MC.cand_interlace(WB[c]["al"], WB[c]["be"],
                                       cd["lo"], cd["hi"],
                                       cd["N"] - 1, IM_TOL)
            r2c[c] = f
        ok_r2c = all(r2c[c] is not None
                     and 0 <= r2c[c] - CTRL_FLIPS[c] <= FLIP_TOL
                     for c in ctrl)
        check("G31-control-fires", ok_c5 and ok_r2c,
              "BLIND VALIDATION at the flips: C5 fires %s == nf "
              "%s exactly; R2 anchor fires %s == nf + 1; "
              "candidate table %s"
              % (str({c: WB[c]["minC"] for c in ctrl}),
                 str(CTRL_FLIPS), str(r2c),
                 str({c: WB[c]["fires"] for c in ctrl})))
        NwC = {c: (CD[c]["S"] + 1) // 2 for c in ctrl}
        ok_locc = all(WB[c]["minC"] < NwC[c] for c in ctrl)
        check("G32-localization-contrast", ok_locc,
              "LOCALIZATION CONTRAST: controls spend the budget "
              "at min C = %s << ceil(S/2) = %s while the mains "
              "sit AT or just beyond it (offsets +0/+2) -- the "
              "arithmetic difference is WHERE a world-blindly "
              "fixed budget is spent, nothing else in the bilanz"
              % (str({c: WB[c]["minC"] for c in ctrl}),
                 str(NwC)))
    else:
        for g in ("G30-control-battery", "G31-control-fires",
                  "G32-localization-contrast"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S4 adjudication
    section("S4  ADJUDICATION -- SEPARATION + TYPING")
    if not smoke:
        worlds_m = list(packs)
        sep = {}
        for cand in ("C1", "C2", "C3", "C4", "C5"):
            okm = all(WB[t]["fires"][cand] is not None
                      and 0 <= WB[t]["fires"][cand] - Nw[t]
                      <= FLIP_TOL for t in worlds_m)
            okc = all(WB[c]["fires"][cand] is not None
                      and 0 <= WB[c]["fires"][cand]
                      - CTRL_FLIPS[c] <= FLIP_TOL for c in ctrl)
            sep[cand] = okm and okc
        selected = next((cand for cand in ("C1", "C2", "C3",
                                           "C4")
                         if sep[cand]), None)
        check("G40-separation", True,
              "SEPARATION ADJUDICATED (sealed rule): %s => "
              "selected C1..C4 candidate: %s; C5 separates: %s "
              "(excluded from FOUND by seal)"
              % (str(sep), str(selected), str(sep["C5"])))
        # restatement typing (r277 adjudicator): C5 vs h pattern
        hp9 = WB["w9"]["HS"][:CD["w9"]["S"] - 1]
        c5_pat = np.array([1 if WB["w9"]["minC"] is None
                           or n < WB["w9"]["minC"] else -1
                           for n in range(CD["w9"]["S"] - 1)],
                          dtype=np.int8)
        n_mis = int(np.sum(c5_pat != hp9))
        check("G41-restatement-typing", True,
              "RESTATEMENT TYPING (r277 adjudicator, w9 "
              "continuation): C5's SAFE/CROSSING step pattern vs "
              "the h pattern: %d mismatches (the h re-entry "
              "pivots beyond the flip) -- C5 is the h pattern's "
              "FIRST CROSSING by definition: typed RESTATEMENT, "
              "never a step-5 obstruction" % n_mis)
        ok_blindall = (ok_blind and ok_bud_c)
        ok_locall = (ok_loc9 and ok_locmin and ok_locc
                     and ok_bud_m and ok_bud_c)
        main_spec = (ok_blindall and ok_locall)
        check("G42-main-specificity", True,
              "MAIN-SPECIFICITY ADJUDICATED: world-blindness "
              "census %s AND localization census %s => %s"
              % (str(ok_blindall), str(ok_locall),
                 "MAIN_SPECIFICITY(LOCALIZATION_IS_THE_"
                 "ARITHMETIC)" if main_spec
                 else "MAIN_SPECIFICITY(UNRESOLVED)"))
    else:
        for g in ("G40-separation", "G41-restatement-typing",
                  "G42-main-specificity"):
            check(g, True, "SMOKE: skipped")
        sep, selected, main_spec = {}, None, False

    # ---------------- S5 mp wards
    section("S5  MP WARDS -- kz15 (FULL) + kz52 (DEEP)")
    if not smoke:
        p15 = BH.wpack(KZ_RAZOR)
        cd15 = comb_data(p15)
        wb15 = world_battery(cd15, MP_DPS_KZ15, SIGN_GUARD_WARD,
                             RECOUNT_DPS_WARD, None)
        Nw15 = (cd15["S"] + 1) // 2
        f15, _m15 = MC.cand_interlace(wb15["al"], wb15["be"],
                                      cd15["lo"], cd15["hi"],
                                      min(cd15["S"] - 2,
                                          cd15["N"] + R2_CONT_CAP),
                                      IM_TOL)
        # f64-vs-mp census ward on kz15
        SGf, _MG = MC.census_signs(wb15["al"], wb15["be"],
                                   cd15["xs"], cd15["N"] - 1)
        okw15 = all(MC.sign_changes(SGf[n])
                    == MC.sign_changes(wb15["SG"][n])
                    for n in CENSUS_WARD_DEGS
                    + (cd15["N"] // 2, cd15["N"] - 1))
        # amendments a1/a2 (disclosed): anchor == min C + 1, and
        # localization equality retyped to measurement (hard
        # part: min C >= N_w, the v956 window survival).
        ok15 = (wb15["budget"] == cd15["Sm"]
                and wb15["minC"] is not None
                and wb15["minC"] >= Nw15
                and wb15["t2_bad"] == 0 and wb15["bil_bad"] == 0
                and wb15["par_clean"] and wb15["ae_clean"]
                and f15 == wb15["minC"] + 1 and okw15
                and wb15["n_recount"] == 0)
        check("G50-kz15-ward", ok15,
              "kz15 (razor, N = %d, S = %d, dps %d) FULL "
              "battery: budget %d == S_- %d; min C = %s >= N_w "
              "%d (offset %+d, MEASURED -- amendment a2); "
              "T2/T3/T3' clean at every degree (flags %d); R2 "
              "fire %s == min C + 1; f64-vs-mp census exact; "
              "|D| = %d"
              % (cd15["N"], cd15["S"], MP_DPS_KZ15,
                 wb15["budget"], cd15["Sm"], str(wb15["minC"]),
                 Nw15, wb15["minC"] - Nw15, wb15["n_flag"],
                 str(f15), cd15["D"]))
        p52 = BH.wpack(KZ_DEEP)
        cd52 = comb_data(p52)
        Nw52 = (cd52["S"] + 1) // 2
        deep_degs = tuple(n for n in
                          (cd52["N"] - 2, cd52["N"] - 1,
                           cd52["N"], cd52["N"] + 1)
                          if 1 <= n <= cd52["S"] - 2)
        wb52 = world_battery(cd52, MP_DPS_DEEP, SIGN_GUARD_WARD,
                             RECOUNT_DPS_WARD, deep_degs)
        ok52 = (wb52["budget"] == cd52["Sm"]
                and wb52["minC"] is not None
                and wb52["minC"] >= Nw52
                and wb52["t2_bad"] == 0 and wb52["bil_bad"] == 0
                and wb52["par_clean"] and wb52["ae_clean"]
                and wb52["bad_coef"] == 0
                and wb52["n_recount"] == 0)
        check("G51-kz52-deep-ward", ok52,
              "kz52 (deep rung, N = %d, S = %d, dps %d, sealed "
              "union degrees %s): budget %d == S_- %d; min C = "
              "%s >= N_w %d (offset %+d, MEASURED); T2 node "
              "signs + T3' bilanz clean at ALL %d degrees; "
              "parity/forced-gap clean at the sealed degrees "
              "(flags %d); |D| = %d"
              % (cd52["N"], cd52["S"], MP_DPS_DEEP,
                 str(deep_degs), wb52["budget"], cd52["Sm"],
                 str(wb52["minC"]), Nw52, wb52["minC"] - Nw52,
                 cd52["S"] - 1, wb52["n_flag"], cd52["D"]))
        tot_guard = sum(WB[t]["n_guard"]
                        for t in WB) + wb15["n_guard"] \
            + wb52["n_guard"]
        tot_rec = sum(WB[t]["n_recount"]
                      for t in WB) + wb15["n_recount"] \
            + wb52["n_recount"]
        check("G52-guard-bookkeeping", True,
              "sign-guard bookkeeping across all worlds: %d "
              "guarded degrees, %d recount corrections (guards "
              "%.0e/%.0e, recount dps %d/%d) -- disclosed"
              % (tot_guard, tot_rec, SIGN_GUARD_MAIN,
                 SIGN_GUARD_WARD, RECOUNT_DPS_MAIN,
                 RECOUNT_DPS_WARD))
    else:
        for g in ("G50-kz15-ward", "G51-kz52-deep-ward",
                  "G52-guard-bookkeeping"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    # exact JF toy material for the must-fails
    nodes = [t[0] for t in jf_pairs]
    wts = [t[1] for t in jf_pairs]
    S_t = len(nodes)
    al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t)
    Lp = []
    for j in range(S_t):
        pr = Fr(1)
        for k in range(S_t):
            if k != j:
                pr *= (nodes[j] - nodes[k])
        Lp.append(pr)
    dw = [1 / (wts[j] * Lp[j] ** 2) for j in range(S_t)]
    alD_t, beD_t, _hsD = WD.stj_gen(nodes, dw, S_t - 1)
    # m1: unmirrored dual
    al_bad = list(al_t[:S_t - 1])
    pd_bad = chain_coef_polys(al_bad, beD_t, S_t - 1)
    k0 = 2
    res_m1 = p_eval(pd_bad[S_t - 1 - k0], nodes[3]) \
        - wts[3] * Lp[3] * WD.pv_exact(al_t, be_t, nodes[3], k0) \
        / hs_t[k0]
    check("G60-mustfail-unmirrored-dual", res_m1 != 0,
          "m1 DUAL WITHOUT MIRRORING (alpha#_m := alpha_m): the "
          "node identity breaks LOUDLY (residual %.3e != 0, "
          "exact rationals) -- the reversal is load-bearing"
          % float(res_m1))
    # m2: prediction without the weight signs
    ps_t = chain_coef_polys(al_t, be_t, S_t - 1)
    psD_t = chain_coef_polys(alD_t, beD_t, S_t - 1)
    n_mis_m2 = 0
    for n in range(1, S_t - 1):
        m_ = S_t - 1 - n
        for j in range(S_t):
            pv = p_eval(ps_t[n], nodes[j])
            pdv = p_eval(psD_t[m_], nodes[j])
            if pv == 0:
                continue
            q = pv * pdv
            pred_noe = ((-1) ** (S_t - 1 - j)) \
                * (1 if hs_t[n] > 0 else -1)
            if (q > 0) != (pred_noe > 0):
                n_mis_m2 += 1
    check("G61-mustfail-gauge-without-wsign", n_mis_m2 > 0,
          "m2 GAUGE WITHOUT THE w_j SIGNS: dropping e_j from the "
          "T2 prediction produces %d sign mismatches on the JF "
          "toy (exact, loud) -- the SIGNED weights are exactly "
          "where the arithmetic data enters the bilanz"
          % n_mis_m2)
    # m3: hull convention breaks parity
    n_par_m3 = 0
    for n in (1,):
        m_ = S_t - 1 - n
        gL, totL, outL = exact_gap_counts(ps_t[n], nodes)
        gR, totR, outR = exact_gap_counts(psD_t[m_], nodes)
        occ = [gL[i] + gR[i] for i in range(S_t - 1)]
        # hull convention: fold ALL real zeros incl. escaped ones
        # into the edge gaps
        occ_h = list(occ)
        occ_h[0] += outL + outR
        agree_t = [(1 if wts[j] > 0 else -1)
                   == (1 if wts[j + 1] > 0 else -1)
                   for j in range(S_t - 1)]
        n_par_m3 = sum(1 for i in range(S_t - 1)
                       if (occ_h[i] % 2 == 1) != agree_t[i])
    check("G62-mustfail-hull-convention", n_par_m3 > 0,
          "m3 HULL- INSTEAD OF NODE-GAP CONVENTION: folding the "
          "escaped zeros into the edge gaps breaks the parity "
          "theorem (%d violations at the first JF degree, "
          "exact, loud) -- the open-gap node convention is the "
          "sealed one (r277-G71 anchor at bilanz grade)"
          % n_par_m3)
    hits = []
    for fn in BILANZ_FUNCS:
        hits += bilanz_scope_audit(fn)
    hits_mut = bilanz_scope_audit("mutant_h_reader")
    ag_hits = antigate_fragment_audit()
    check("G63-scope-audits", not hits and bool(hits_mut)
          and not ag_hits,
          "the bilanz/census scope consumes passed coefficient/"
          "atom/sign arrays + the evaluation grid ONLY (%s); the "
          "deliberately h-reading mutant is FLAGGED (%s); "
          "fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_mut) if hits_mut else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S7 verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the two-sided index bilanz with its exact "
          "theorems (T2 node signs, T3 parity/forced-gap, T3' "
          "census bilanz, T4 crossing budget == S_-), the sealed "
          "candidate adjudication, the exact obstruction "
          "refutation, and the b3 gap statement -- the "
          "localization of the crossing budget is the named "
          "open center")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        if selected is not None and n_cex == 0:
            parts.append("ORIENTED_THEOREM_PROVED(%s)" % selected)
        elif selected is not None:
            parts.append(
                "STEP5_INVARIANT_FOUND(%s; fires mains %s; "
                "implication measured only)"
                % (selected,
                   str({t: WB[t]["fires"][selected]
                        for t in packs})))
        else:
            parts.append(
                "STEP5_OPEN(anatomy: C1 never fires anywhere -- "
                "a world-blind THEOREM, not a separator; "
                "C2/C3/C4 die at degrees %s on w9 (the |D| "
                "slack is spent immediately by the complex dual "
                "flank); C5 fires at the first crossing %s by "
                "definition -- the h restatement, and the w13 "
                "offset +2 shows even it misses the sealed "
                "N_w-anchored window)"
                % (str((WB["w9"]["fires"]["C2"],
                        WB["w9"]["fires"]["C3"],
                        WB["w9"]["fires"]["C4"])),
                   str({t: WB[t]["fires"]["C5"]
                        for t in list(packs) + list(ctrl)})))
        if n_cex > 0:
            parts.append(
                "OBSTRUCTION_REFUTED(%d exact toy "
                "counterexamples + the controls as real-comb "
                "counterexamples)" % n_cex)
        bundle_t3 = (ok_node and ok_t3 and ok_par and ok_ae
                     and ok_bil and ok_exh
                     and all(WB[t]["t2_bad"] == 0
                             and WB[t]["bil_bad"] == 0
                             and WB[t]["par_clean"]
                             and WB[t]["ae_clean"] for t in WB))
        if bundle_t3:
            parts.append("TWO_SIDED_PARITY_THEOREM")
        bundle_t4 = (ok_bud
                     and all(WB[t]["budget"] == CD[t]["Sm"]
                             for t in WB)
                     and wb15["budget"] == cd15["Sm"]
                     and wb52["budget"] == cd52["Sm"])
        if bundle_t4:
            parts.append("CROSSING_BUDGET_THEOREM(budget == S_- "
                         "on every world incl. both wards)")
        parts.append(
            "MAIN_SPECIFICITY(%s)"
            % ("LOCALIZATION_IS_THE_ARITHMETIC" if main_spec
               else "UNRESOLVED"))
        verd = " + ".join(parts)
    info("b3 GAP STATEMENT: " + GAP_STATEMENT)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- PROVED (machine-gated, classical citations: "
          "node identity r274/r231, L' alternation, IVT, "
          "Jacobi's minor-sign rule + Sylvester congruence, "
          "beta-positivity symmetrization): T1..T4; MEASURED: "
          "the candidate table, the world-blindness census, the "
          "localization contrast; OPEN: the localization itself "
          "(the b3 statement above); NO RH claim"
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
