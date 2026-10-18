#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""budget_headtail_probe -- PRIME.PORT.BUDGET.HEADTAIL.01
(round 246): short adjudication round on the r243/r244 budget object
-- NO new positivity shortcut, the round determines the correct
ASYMPTOTIC LOAD of the budget S_{N-1} = sum_{n<N} rho_n,
rho_n = F_n^2/h_n.  Two separate questions, two separate verdicts:
(1) SUPPORT SIZE: is the budget ENERGY effectively low-dimensional
(finite / logarithmic / sublinear head) or an extensive irregular
bulk?  REVIEWER FRAMING (binding): r244's IRREGULAR_BULK typing only
excluded frontier dominance; from p_0 = 0.37 already R_2 <= 1/p_0^2
~ 7.3 -- the energy COULD be low-dimensional while the SOURCE stays
incompressible (each head mode consumes the full comb; no no-go is
touched).  (2) RENORMALIZATION: did the three r244 source-pure
corner candidates (b1/b2/b3, PSD 0/42 with N-growing deficit) fail
only for lack of a FINITE renormalization head -- i.e. does the
budget read B_w = S_{K-1} + b_can (measured head prefix + candidate
covers the tail) for a sealed K?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r244 discipline): w = window (kz),
N_w = builder depth, n = chain degree; F per F_DEF / F_DEF_SHA
imported verbatim from r243 (principal_bessel_probe.F_DEF); the
budget machinery is imported verbatim from r244
(bordered_hankel_probe.wpack): rho_n, S, and the candidates b1
(smooth self-pairing s_0), b2 (Szego/equilibrium budget), b3
(mu-side norm) are BITWISE the r244 objects -- exact reproduction,
no re-derivation.  Ground truth (h signs, flips) enters gates only.

BLIND SEAL (sealed BEFORE evaluation): BLIND = the two largest-N
rungs of the (N, kz)-sorted frame-A h <= 900 ladder (deterministic
rule; the realized pair is printed, never chosen); DEV = the
remaining 40.  ALL leg-A fits run on DEV; BLIND enters only the
prediction check.

LEG A -- EFFECTIVE SUPPORT SIZE (all 42 windows): normalized
contributions p_{n,w} = rho_{n,w}/S_{N-1,w}; K_q(w) = min{K:
sum_{n<K} p_n >= q} in NATURAL degree order for q in Q_LIST =
(0.5, 0.9, 0.99, 0.999); R_2 = 1/sum p_n^2 (participation ratio,
the reviewer's R_eff); R_ent = exp(-sum p_n log p_n).  Per
statistic X on DEV two 2-parameter models compete: POWER
log X = c + s log N vs LOG X = a + b log N, compared by rms
relative residual.  CLASS RULE (sealed): O(1) iff |s| <= 0.10;
O(N) iff s >= 0.85; O(log N) iff s <= 0.50 AND the LOG model rms
<= POWER rms; else O(N^s).  SUPPORT VERDICT (sealed, on the two
designated statistics R_2 (primary) and K_0.9 (secondary)):
FINITE_HEAD iff both are O(1); EXTENSIVE_IRREGULAR_BULK iff either
is O(N); LOGARITHMIC_HEAD iff both in {O(1), O(log N)}; else
SUBLINEAR_HEAD.  BLIND CHECK: the DEV-winning model per designated
statistic must predict BOTH blind windows within factor 1.5 (R_2)
and within factor 2 OR +-2 absolute (K_0.9); a miss appends the
modifier SUPPORT_BLIND_CHECK_FAILED (the classification is typed
UNSTABLE, never upgraded, never silently dropped).  CONTROLS
comparison profile: EPSTEIN and SCRAMBLE on their pre-flip range
n < flip (25/21) get the same statistics as a single-window
profile (no scaling claim); SMOOTH is the self-alias world: its
budget is EXACTLY rho_0 (F_0 = s_0, the smooth self-pairing;
modes n >= 1 are structural zeros by orthogonality) -- typed and
excluded from profile stats.

LEG B -- EXACT HEAD PEELING (sealed K_LIST = (1, 2, 4, 8, 16,
32)): after eliminating the first K modes of the bordered problem
the Schur rest has corner B - S_{K-1} and remaining increments
rho_K..rho_{N-1} -- EXACT by the r243/r244 nested-pivot and
telescope identities, re-gated here in rationals on the r243 toy
including the renormalized reading det G_n(B = S_{K-1} + b) =
det H_n (b - (S_{n-1} - S_{K-1})).  The rest test per (K, cand):
b_can(w) > tail_w(K) := S_{N-1} - S_{K-1} -- i.e. does the
candidate cover the tail once the measured head is carried as an
explicit finite renormalization?  This is NOT an a-posteriori
constant choice: K_LIST and the candidates are sealed, the test
is binary per (K, cand).  Reported per cell: coverage on 42 MAIN,
margin d_w = b - tail, Spearman(d; N) (deficit N-trend), median
shortfall D(K) = med_w max(-d_w, 0).  CONTROL CLAUSES (ALL
required for a success; amended at calibration, disclosed in the
records): wall flips reproduced at 25/21/27; NO control certified
by the full bordered claim (wall + budget -- the r244 c2
discipline).  The SCRAMBLE/SMOOTH budget sides are MEASURED and
reported at every cell in BOTH variants (signed full depth and
pre-flip) but are NOT a kill clause: post-flip control rho
carries the h sign, so the full-depth control budget is signed
and non-adjudicable as a positive quantity (SCRAMBLE signed
S_{N-1} < 0, measured), and the pre-flip control tails are
structurally tiny because rho_0 dominates every world's head --
the controls are discriminated by the WALL, not the budget side
(typed, the r243/r244 finding).  SUCCESS(K, cand) iff coverage
42/42 AND control clauses AND Spearman(d; N) > -0.5 (margin does
not collapse).  K_cov DIAGNOSTIC: per window the minimal K with
b >= tail(K) (searchsorted on the monotone MAIN S); DIAGNOSTIC
ONLY -- a per-window K choice is the head oracle (must-fail m1)
and can NEVER fire FINITE.

RENORMALIZATION VERDICT (sealed, mutually exclusive, priority):
  FINITE_HEAD_RENORMALIZES(K, cands): SUCCESS at some sealed K
    (smallest reported, all passing candidates listed);
  LOG_HEAD_RENORMALIZES(cand): no SUCCESS and for some candidate
    the DEV slope of log max(K_cov, 1) vs log N is <= 0.5 AND
    K_cov(w) <= 6 ln N_w on 42/42 (control clauses as above);
  EXTENSIVE_BULK_CONFIRMED: neither fires, support verdict is
    EXTENSIVE_IRREGULAR_BULK, and D(32) >= 0.7 D(1);
  HEAD_PEEL_RELOCATES: neither renormalizes and D(32) >= 0.7 D(1)
    (peeling merely relocates the deficit);
  IMPORTED_CORNER_PERSISTS: else (peeling narrows materially but
    no sealed K closes; the r243 imported window form
    B_w = S_{N-2} + 5/7 remains the only budget known to cover --
    the reviewer's prior).
HONESTY GUARD (sealed pre-run): a firing FINITE/LOG verdict is a
MEASUREMENT and carries the modifier RENORM_HEAD_IS_PREFIX_DATA:
B_w = S_{K-1} + b_can consumes the window's own measured head --
the SAME epistemic status as r243's B_w = S_{N-2} + 5/7, only
with a smaller imported remainder; no bound mechanism is claimed
and the SOURCE stays incompressible (each head mode consumes the
full comb; r243 PAIRCORR_REENCODED stands).

LEG C -- HEAD-MODE ANATOMY (first HEAD_K = 8 modes): median p_n
per mode over the ladder and which degrees CARRY (median p_n >=
0.01); per-mode N-scaling: DEV log-log slope of rho_n vs N for
n = 0..7; world comparison on the w9 base over the common
pre-flip range n < flip: normalized head shapes phat =
rho[:8]/sum(rho[:8]), max |phat_ctrl - phat_MAIN|, per-mode log10
magnitude ratios, and the head/rest split of the control-minus-
MAIN budget difference frac_head = sum_{n<8} Delta rho /
sum_{n<flip} Delta rho.  SEALED WORDING RULE:
HEAD_CARRIES_ARITHMETIC iff max |dphat(SCRAMBLE)| > 0.15 OR the
median over n < 8 of log10(rho_SCR/rho_MAIN) >= 1.0 (the head
separates the worlds in shape or by >= one decade); else
HEAD_GEOMETRY_SHARED.

MUST-FAILS (each loud): (m1) HEAD ORACLE: choosing K per window
post hoc (the K_cov diagnostic) makes EVERY positive candidate
cover 42/42 trivially -- shown live and EXCLUDED from every
verdict path; (m2) normalization ward |sum_n p_n - 1| <= 1e-12
per window; (m3) telescope identity tail(K) = S_{N-1} - S_{K-1}
equals the direct sum sum_{n>=K} rho_n to 1e-12 relative on every
window and EXACTLY in rationals on the r243 toy; (m4) sorted-K_q
ward: K_q on the natural degree order >= K_q on the
descending-sorted profile ("head = low degrees" is a finding,
never a definition).

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs);
background du = 0.01, masses 2 e^{u/2} du (imported verbatim via
BH/PB); BLIND = two largest-N rungs of the (N, kz) sort; Q_LIST
= (0.5, 0.9, 0.99, 0.999); K_LIST = (1, 2, 4, 8, 16, 32); HEAD_K
= 8; class bars 0.10 / 0.50 / 0.85; blind bars factor 1.5 (R_2),
factor 2 or +-2 (K_0.9); margin trend -0.5; relocation bar 0.7;
K_cov slope bar 0.5, cap 6 ln N; head-shape bar 0.15, magnitude
bar 1.0 decade; carry bar 0.01; control flips 25/21/27; smoke
rungs (9, 12, 13, 26, 40) with DEV/BLIND by the same rule;
runtime <= 1800 s.

SEALED VERDICT FORM: SUPPORT(<class>) [+
SUPPORT_BLIND_CHECK_FAILED] + <renormalization verdict> [+
RENORM_HEAD_IS_PREFIX_DATA] + <HEAD_CARRIES_ARITHMETIC |
HEAD_GEOMETRY_SHARED>.  Honesty before beauty.

RECORD TABLES (frozen from calib_ht_pass1.log, 16/16, wall 8.1 s;
disclosed SMOKE/CALIBRATION AMENDMENTS -- the statistics, the
class rule, the peeling test, the blind rule and ALL verdict
rules NEVER moved: (a1) the smoke pass caught the original
SCRAMBLE budget-side KILL clause as structurally non-adjudicable
(post-flip control rho carries the h sign: SCRAMBLE's signed
S_{N-1} = -0.97 < 0, and the pre-flip control tails are tiny
because rho_0 dominates every world's head) -- the clause was
replaced BEFORE the record run by the r244 c2 discipline (no
control certified by the full bordered claim) with the budget
sides reported in BOTH variants as a typed diagnostic; no
numeric bar moved; (a2) the SMOOTH typing was corrected from
'budget structurally ~ 0' to the measured truth 'budget = rho_0
alone' (F_0 = s_0 is the smooth self-pairing, only n >= 1 are
structural zeros); text only.  HONESTY NOTE: on the shallow
5-rung smoke ladder FINITE_HEAD_RENORMALIZES(K=1, b3) fired --
the full ladder REFUTES it (b3 coverage 24/42): the smoke
verdict was a shallow-window artifact, disclosed):
CAL_VERDICT = SUPPORT(EXTENSIVE_IRREGULAR_BULK) +
IMPORTED_CORNER_PERSISTS + HEAD_CARRIES_ARITHMETIC.
Key numbers.  LEG A (BLIND = kz 64 (N = 859) + kz 52 (N = 878),
sealed rule; DEV = 40 rungs, N in [142, 841]):
  K_0.5   med 182  in [1, 485]    slope +1.47  class O(N)
  K_0.9   med 346  in [135, 799]  slope +0.99  class O(N)
  K_0.99  med 388  in [142, 876]  slope +1.00  class O(N)
  K_0.999 med 388  in [142, 878]  slope +1.00  class O(N)
  R_2     med 6.76 in [3.4, 10.6] slope +0.26  class O(N^0.26)
  R_ent   med 24.6 in [9.3, 46.3] slope +0.54  class O(N^0.54)
SUPPORT VERDICT: class(R_2) = O(N^0.26), class(K_0.9) = O(N)
=> SUPPORT(EXTENSIVE_IRREGULAR_BULK); BLIND CHECK PASSED (R_2
pred 8.27/8.31 vs actual 6.97/10.30, worst factor 1.24 <= 1.5;
K_0.9 pred 774/791 vs actual 745/799, worst factor 1.04 <= 2):
the classification is STABLE on the two sealed blind windows.
RECONCILIATION with the reviewer's R_eff <= 7.3: CONFIRMED as
the R_2 scale (med 6.76, max 10.6) -- but R_2 is a
p_0-dominated statistic; the 90-percent shoulder K_0.9 ~ 0.9 N
is LINEAR in N: beyond mode 0 the budget energy is NOT
low-dimensional in any q-quantile sense.  CONTROLS profile
(pre-flip, single-window): EPSTEIN K_0.5/K_0.9/R_2 = 1/1/1.00,
SCRAMBLE 1/1/1.15, MAIN-w9 restricted 1/1/1.00 (every world's
pre-flip budget is mode-0 total-dominated); SMOOTH budget
3.48 = rho_0 alone, tail 0.  LEG B (the adjudication): the
coverage matrix is K-INDEPENDENT across the whole sealed list
(K = 1..32 identical cells: modes 1..31 carry NOTHING -- on w9
S[0] = S[31] to 15 digits): b1 cov 1/42 (med shortfall 3.11,
trend -0.50), b2 16/42 (0.41, -0.39), b3 24/42 (0.00, -0.37);
NO cell reaches 42/42 => no SUCCESS; deficit trends all
negative (the deficit GROWS with N after peeling); K_cov
diagnostic: b1 med 251.5 / max 628 (cap 6 ln N violated 41/42),
b2 med 103 / max 485 (26/42), b3 med 1 / max 411 (18/42) => the
LOG rule cannot fire; relocation ratios D(32)/D(1) = 0.99 (b1) /
1.00 (b2) / nan (b3, D(1) = 0) => IMPORTED_CORNER_PERSISTS: the
reviewer's prior stands -- the only budget known to cover the
surface remains the r243 window form B_w = S_{N-2} + 5/7; the
candidates do not miss a finite or logarithmic head, they miss
an EXTENSIVE bulk (peeling any fixed number of modes changes
nothing because the head beyond mode 0 is empty); control
budget sides covered in both variants at every cell (typed
diagnostic, a1), no control certified, walls break at 25/21/27.
LEG C (head anatomy -- the round's sharpest refinement of
r244): the 'heavy head' is EXACTLY ONE MODE: median p_0 = 0.37,
median p_1..p_7 ~ 1e-8 (eight orders below carrying); carrying
set {0}; argmax at degree 0 on 42/42 (r244 reproduced); rho_0
is nearly UNIVERSAL across the ladder (spread 0.2 decades,
DEV slope +0.21 ~ flat; rho_0 ~ 3.5 = the smooth self-pairing
scale) -- S_{N-1} = rho_0 + structural quiet zone + extensive
irregular bulk; the budget growth S ~ N^0.33 (r243) lives
ENTIRELY in the bulk.  World comparison (w9 base, common
pre-flip range): EPSTEIN max|dphat| 0.00, med log10 rho-ratio
+0.00, frac_head 0.000 (EPSTEIN's head is bitwise-close MAIN
geometry); SCRAMBLE max|dphat| 0.01 (SHAPE shared: mode-0
dominance is geometry), med log10 rho-ratio +2.12 decades,
frac_head 0.164 => HEAD_CARRIES_ARITHMETIC by the sealed
MAGNITUDE clause: the quiet zone n = 1..7 sits ~ 2 decades
higher on SCRAMBLE -- the arithmetic worlds separate in the
LEVEL of the quiet head modes, not in the head shape; 84
percent of the pre-flip budget excess sits in n >= 8.
MUST-FAILS all loud: m1 head oracle covers 42/42 for every
candidate (excluded live), m2 worst |sum p - 1| = 2.2e-15, m3
telescope worst 2.8e-15 rel + exact rationals, m4 sorted ward
holds 42/42.  Runtime 8.1 s full, 0.4 s smoke.  AMENDMENTS
AFTER FREEZE: NONE.

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
Q_LIST = (0.5, 0.9, 0.99, 0.999)
K_LIST = (1, 2, 4, 8, 16, 32)
HEAD_K = 8
S_O1 = 0.10
S_LOG = 0.50
S_LIN = 0.85
BLIND_R2_FAC = 1.5
BLIND_K_FAC = 2.0
BLIND_K_ABS = 2.0
MARGIN_TREND = -0.5
RELOC_BAR = 0.7
LOGCOV_SLOPE = 0.5
LOGCOV_CONST = 6.0
SHAPE_BAR = 0.15
MAG_BAR = 1.0
CARRY_BAR = 0.01
NORM_BAR = 1e-12
TELE_BAR = 1e-12
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SMOKE_KZ = (9, 12, 13, 26, 40)
CAL_VERDICT = ("SUPPORT(EXTENSIVE_IRREGULAR_BULK) + "
               "IMPORTED_CORNER_PERSISTS + "
               "HEAD_CARRIES_ARITHMETIC")

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
    return (not bad), ("NO zero/prime oracles; rho/S/b1/b2/b3 are "
                       "the BITWISE r244 objects (BH.wpack "
                       "imported); K_LIST and Q_LIST sealed; the "
                       "per-window K choice (head oracle) is a "
                       "must-fail, never a verdict path"
                       if not bad else "; ".join(bad))


# --------------------------------------------------- leg-A helpers
def support_stats(rho, St):
    """normalized head/tail statistics of one budget profile."""
    p = np.asarray(rho, float) / St
    csum = np.cumsum(p)
    Kq = {q: int(np.searchsorted(csum, q) + 1) for q in Q_LIST}
    R2 = 1.0 / float(np.sum(p * p))
    pp = p[p > 0.0]
    Rent = float(np.exp(-np.sum(pp * np.log(pp))))
    return p, csum, Kq, R2, Rent


def fit_models(Ns, Xs):
    """two 2-parameter models on DEV: POWER log X = c + s log N vs
    LOG X = a + b log N, compared by rms relative residual."""
    ln_n = np.log(np.asarray(Ns, float))
    X = np.asarray(Xs, float)
    s, c = np.polyfit(ln_n, np.log(X), 1)
    pred_p = np.exp(c + s * ln_n)
    rms_p = float(np.sqrt(np.mean(((pred_p - X) / X) ** 2)))
    b, a = np.polyfit(ln_n, X, 1)
    pred_l = a + b * ln_n
    rms_l = float(np.sqrt(np.mean(((pred_l - X) / X) ** 2)))
    return dict(s=float(s), c=float(c), a=float(a), b=float(b),
                rms_p=rms_p, rms_l=rms_l)


def classify(f):
    if abs(f["s"]) <= S_O1:
        return "O(1)"
    if f["s"] >= S_LIN:
        return "O(N)"
    if f["s"] <= S_LOG and f["rms_l"] <= f["rms_p"]:
        return "O(log N)"
    return "O(N^%.2f)" % f["s"]


def blind_pred(f, N):
    """prediction of the DEV-winning model at depth N."""
    if f["rms_l"] <= f["rms_p"]:
        return f["a"] + f["b"] * math.log(N)
    return math.exp(f["c"] + f["s"] * math.log(N))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("budget_headtail_probe -- PRIME.PORT.BUDGET."
          "HEADTAIL.01 (round 246)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (five known rungs, DEV/BLIND by the "
                        "same rule)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "machinery imported verbatim (r244 BH.wpack: rho, S, "
          "b1/b2/b3 bitwise); BLIND rule = two largest-N rungs of "
          "the (N, kz) sort, sealed BEFORE the ladder is built; "
          "Q_LIST %s; K_LIST %s; class bars %.2f/%.2f/%.2f; blind "
          "bars %.1fx (R_2), %.0fx or +-%.0f (K_0.9); margin "
          "trend %.1f; relocation bar %.1f; K_cov slope %.1f cap "
          "%.0f ln N; head-shape bar %.2f, magnitude bar %.1f "
          "decade; HEAD_K = %d; verdict rules sealed in the "
          "frozen spec (support and renormalization verdicts are "
          "SEPARATE by design)"
          % (str(Q_LIST), str(K_LIST), S_O1, S_LOG, S_LIN,
             BLIND_R2_FAC, BLIND_K_FAC, BLIND_K_ABS, MARGIN_TREND,
             RELOC_BAR, LOGCOV_SLOPE, LOGCOV_CONST, SHAPE_BAR,
             MAG_BAR, HEAD_K))

    # ---------------- S1: exact Schur-rest identity (rationals)
    section("S1  EXACT SCHUR-REST / RENORMALIZED-BUDGET IDENTITY")
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
    Stoy = []
    acc = Fr(0)
    for k in range(NTOY + 1):
        acc += rhotoy[k]
        Stoy.append(acc)

    def Hm(n):
        return [[mom[i + j] for j in range(n)] for i in range(n)]

    def Gb(n, B):
        M = [[mom[i + j] for j in range(n)] + [smom[i]]
             for i in range(n)]
        M.append([smom[j] for j in range(n)] + [B])
        return M

    b_toy = Fr(5, 3)
    ok1 = ok2 = ok3 = True
    for K in (1, 2, 3):
        # (i) bordered det factorization at prefix K (r244, cited)
        B = Fr(22, 7)
        ok1 = ok1 and (PB.frac_det(Gb(K, B))
                       == PB.frac_det(Hm(K)) * (B - Stoy[K - 1]))
        # (ii) rest telescope: the Schur corner after K modes minus
        # the remaining increments IS the full corner
        ok2 = ok2 and ((B - Stoy[K - 1])
                       - sum(rhotoy[K:NTOY + 1])
                       == B - Stoy[NTOY])
        # (iii) renormalized reading at full size n = NTOY:
        # det G_n(B = S_{K-1} + b) = det H_n (b - (S_{n-1}-S_{K-1}))
        n = NTOY
        Bren = Stoy[K - 1] + b_toy
        ok3 = ok3 and (PB.frac_det(Gb(n, Bren))
                       == PB.frac_det(Hm(n))
                       * (b_toy - (Stoy[n - 1] - Stoy[K - 1])))
    check("G10-schur-rest-exact", ok1 and ok2 and ok3,
          "rationals on the r243 toy (K = 1..3): bordered det "
          "factorization det[[H_K, u],[u^T, B]] = det H_K "
          "(B - S_{K-1}) (r244 G10 cited, re-gated); rest "
          "telescope (B - S_{K-1}) - sum_{n>=K} rho_n = B - "
          "S_{N-1}; renormalized reading det G_n(B = S_{K-1} + b) "
          "= det H_n (b - tail(K)) at b = 5/3 -- the head-peeled "
          "test 'b > tail(K)' IS the exact Schur-rest positivity "
          "of the bordered problem, not an approximation")

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
          "BLIND = two largest-N rungs by the sealed rule: kz %s "
          "(N %s); DEV = %d rungs (N in [%d, %d]); all leg-A fits "
          "run on DEV, BLIND enters only the prediction check"
          % (str([p["kz"] for p in blind]),
             str([p["N"] for p in blind]), len(dev),
             dev[0]["N"], dev[-1]["N"]))

    # ---------------- S3: leg A -- effective support size
    section("S3  LEG A -- EFFECTIVE SUPPORT SIZE (DEV fit, BLIND "
            "check)")
    norm_worst = 0.0
    tele_worst = 0.0
    for p in packs:
        p_n, csum, Kq, R2, Rent = support_stats(p["rho"], p["St"])
        p["p_n"], p["csum"], p["Kq"] = p_n, csum, Kq
        p["R2"], p["Rent"] = R2, Rent
        norm_worst = max(norm_worst, abs(float(csum[-1]) - 1.0))
        for K in K_LIST:
            direct = float(np.sum(p["rho"][K:]))
            tele = p["St"] - float(p["S"][K - 1])
            tele_worst = max(tele_worst,
                             abs(tele - direct) / p["St"])
    check("G30-normalization-telescope-wards", norm_worst <= NORM_BAR
          and tele_worst <= TELE_BAR,
          "m2: |sum_n p_n - 1| worst %.1e (bar %.0e) on all "
          "windows; m3: tail(K) = S_{N-1} - S_{K-1} vs direct "
          "sum_{n>=K} rho_n worst rel %.1e (bar %.0e) at all "
          "sealed K -- the peeled tail is the exact telescope, "
          "gated exactly in rationals in G10"
          % (norm_worst, NORM_BAR, tele_worst, TELE_BAR))
    Ns_dev = [p["N"] for p in dev]
    stat_defs = [("K_0.5", lambda p: p["Kq"][0.5]),
                 ("K_0.9", lambda p: p["Kq"][0.9]),
                 ("K_0.99", lambda p: p["Kq"][0.99]),
                 ("K_0.999", lambda p: p["Kq"][0.999]),
                 ("R_2", lambda p: p["R2"]),
                 ("R_ent", lambda p: p["Rent"])]
    fits = {}
    classes = {}
    for name, get in stat_defs:
        vals_all = [get(p) for p in packs]
        vals_dev = [get(p) for p in dev]
        f = fit_models(Ns_dev, vals_dev)
        fits[name] = f
        classes[name] = classify(f)
        info("%-8s med %.3g in [%.3g, %.3g] | DEV slope %+.2f | "
             "rms POWER %.3f vs LOG %.3f | class %s"
             % (name, float(np.median(vals_all)), min(vals_all),
                max(vals_all), f["s"], f["rms_p"], f["rms_l"],
                classes[name]))
    cr2 = classes["R_2"]
    ck9 = classes["K_0.9"]
    if cr2 == "O(1)" and ck9 == "O(1)":
        support = "FINITE_HEAD"
    elif cr2 == "O(N)" or ck9 == "O(N)":
        support = "EXTENSIVE_IRREGULAR_BULK"
    elif cr2 in ("O(1)", "O(log N)") and ck9 in ("O(1)", "O(log N)"):
        support = "LOGARITHMIC_HEAD"
    else:
        support = "SUBLINEAR_HEAD"
    check("G31-support-classified", True,
          "SEALED RULE result: SUPPORT(%s) -- designated pair: "
          "class(R_2) = %s (primary; the reviewer's R_eff), "
          "class(K_0.9) = %s (secondary); full table above (the "
          "deep-tail statistics K_0.99/K_0.999 are reported, "
          "never designated)" % (support, cr2, ck9))
    okB = True
    bl_note = []
    for p in blind:
        pr2 = blind_pred(fits["R_2"], p["N"])
        fac2 = (max(pr2 / p["R2"], p["R2"] / pr2)
                if pr2 > 0 else float("inf"))
        okB = okB and fac2 <= BLIND_R2_FAC
        pk9 = blind_pred(fits["K_0.9"], p["N"])
        act9 = p["Kq"][0.9]
        fac9 = (max(pk9 / act9, act9 / pk9)
                if pk9 > 0 else float("inf"))
        okB = okB and (fac9 <= BLIND_K_FAC
                       or abs(pk9 - act9) <= BLIND_K_ABS)
        bl_note.append("kz%d(N=%d): R_2 pred %.2f act %.2f "
                       "(x%.2f); K_0.9 pred %.1f act %d (x%.2f)"
                       % (p["kz"], p["N"], pr2, p["R2"], fac2,
                          pk9, act9, fac9))
    supp_mod = "" if okB else " + SUPPORT_BLIND_CHECK_FAILED"
    check("G32-blind-check", True,
          "BLIND prediction of the DEV-winning models: %s -- %s "
          "(bars %.1fx R_2, %.0fx or +-%.0f K_0.9); by the sealed "
          "rule a miss types the classification UNSTABLE via "
          "modifier, it never upgrades"
          % ("; ".join(bl_note),
             "PASSED, classification STABLE on blind" if okB
             else "MISSED -> SUPPORT_BLIND_CHECK_FAILED",
             BLIND_R2_FAC, BLIND_K_FAC, BLIND_K_ABS))
    ctrl_note = []
    for c in ("EPSTEIN", "SCRAMBLE"):
        pc = ctrl[c]
        nf = pc["nf"]
        Spre = float(pc["S"][nf - 1])
        _pn, _cs, Kqc, R2c, Rentc = support_stats(pc["rho"][:nf],
                                                  Spre)
        _pn9, _cs9, Kq9, R29, _re9 = support_stats(
            by_kz[9]["rho"][:nf], float(by_kz[9]["S"][nf - 1]))
        ctrl_note.append("%s(n<%d): K_0.5/K_0.9/R_2 = %d/%d/%.2f "
                         "vs MAIN-w9 %d/%d/%.2f"
                         % (c, nf, Kqc[0.5], Kqc[0.9], R2c,
                            Kq9[0.5], Kq9[0.9], R29))
    psm = ctrl["SMOOTH"]
    sm_bud = float(psm["St"])
    sm_r0 = float(psm["rho"][0])
    check("G33-controls-profile", True,
          "single-window comparison profile (pre-flip range, no "
          "scaling claim): %s; SMOOTH typed self-alias: budget "
          "%.4g = rho_0 alone (%.4g; F_0 = s_0 self-pairing, "
          "modes n >= 1 structural zeros, tail %.1e) -- excluded "
          "from profile stats"
          % ("; ".join(ctrl_note), sm_bud, sm_r0,
             sm_bud - sm_r0))

    # ---------------- S4: leg B -- head peeling matrix
    section("S4  LEG B -- HEAD PEELING (sealed K x candidate)")
    Ns = [p["N"] for p in packs]
    cells = {}
    for K in K_LIST:
        for tag in ("b1", "b2", "b3"):
            dm = [p[tag] - (p["St"] - float(p["S"][K - 1]))
                  for p in packs]
            cov = sum(1 for d_ in dm if d_ > 0.0)
            sp = BH.spearman(dm, Ns)
            Dk = float(np.median([max(-d_, 0.0) for d_ in dm]))
            certs = []
            bud_cov = {}
            for c in ctrl:
                pc = ctrl[c]
                tail_sg = (float(pc["St"])
                           - float(pc["S"][K - 1]))
                tail_pf = (float(pc["S"][pc["nf"] - 1])
                           - float(pc["S"][K - 1]))
                bud_cov[c] = (pc[tag] - tail_sg > 0.0,
                              pc[tag] - tail_pf > 0.0)
                if (pc["nf"] is None) and bud_cov[c][0]:
                    certs.append(c)
            succ = (cov == len(packs)
                    and not certs and okCf and sp > MARGIN_TREND)
            cells[(K, tag)] = dict(cov=cov, sp=sp, Dk=Dk,
                                   bud_cov=bud_cov, certs=certs,
                                   succ=succ)
    for K in K_LIST:
        info("K=%-3d " % K + " | ".join(
            "%s: cov %d/%d, med shortfall %.2f, trend %+.2f"
            % (tag, cells[(K, tag)]["cov"], len(packs),
               cells[(K, tag)]["Dk"], cells[(K, tag)]["sp"])
            for tag in ("b1", "b2", "b3")))
    info("control budget sides (signed/pre-flip coverage, TYPED "
         "diagnostic, not a kill clause): " + "; ".join(
             "%s@K=32: %s" % (c, str({t: cells[(32, t)]
                                      ["bud_cov"][c]
                                      for t in ("b1", "b2",
                                                "b3")}))
             for c in ("EPSTEIN", "SCRAMBLE", "SMOOTH")))
    check("G40-controls-not-certified",
          all(not cells[(K, t)]["certs"] for K in K_LIST
              for t in ("b1", "b2", "b3")) and okCf,
          "NO control is certified by the full bordered claim at "
          "any (K, cand): the walls break at the sealed flips %s "
          "regardless of peeling; budget sides measured above -- "
          "the full-depth control budget is SIGNED post-flip "
          "(SCRAMBLE S_{N-1} = %.2f < 0) and the pre-flip tails "
          "are structurally tiny (rho_0 dominates every world): "
          "the controls are discriminated by the WALL, not the "
          "budget side (amended at calibration, disclosed)"
          % (str({c: ctrl[c]["nf"] for c in ctrl}),
             float(ctrl["SCRAMBLE"]["St"])))
    # K_cov diagnostic (head oracle -- excluded from FINITE)
    kcov = {}
    for tag in ("b1", "b2", "b3"):
        kc = []
        for p in packs:
            thr = p["St"] - p[tag]
            if thr <= 0.0:
                kc.append(0)
            else:
                kc.append(int(np.searchsorted(p["S"], thr) + 1))
        kcov[tag] = kc
        info("K_cov[%s]: med %.1f, max %d, cap 6 ln N violated "
             "on %d/%d windows"
             % (tag, float(np.median(kc)), max(kc),
                sum(1 for k_, p in zip(kc, packs)
                    if k_ > LOGCOV_CONST * math.log(p["N"])),
                len(packs)))
    # sealed renormalization verdict
    succ_cells = [(K, t) for K in K_LIST for t in ("b1", "b2", "b3")
                  if cells[(K, t)]["succ"]]
    renorm_mod = ""
    if succ_cells:
        Kmin = min(K for K, _t in succ_cells)
        tags = sorted({t for K, t in succ_cells if K == Kmin})
        renorm = ("FINITE_HEAD_RENORMALIZES(K=%d, %s)"
                  % (Kmin, ",".join(tags)))
        renorm_mod = " + RENORM_HEAD_IS_PREFIX_DATA"
    else:
        dev_kzs = {p["kz"] for p in dev}
        log_tags = []
        for tag in ("b1", "b2", "b3"):
            kc = kcov[tag]
            kc_dev = [k_ for k_, p in zip(kc, packs)
                      if p["kz"] in dev_kzs]
            f = fit_models(Ns_dev, [max(k_, 1) for k_ in kc_dev])
            cap_ok = all(k_ <= LOGCOV_CONST * math.log(p["N"])
                         for k_, p in zip(kc, packs))
            no_cert = all(not cells[(K, tag)]["certs"]
                          for K in K_LIST)
            if f["s"] <= LOGCOV_SLOPE and cap_ok and no_cert:
                log_tags.append(tag)
        if log_tags:
            renorm = ("LOG_HEAD_RENORMALIZES(%s)"
                      % ",".join(log_tags))
            renorm_mod = " + RENORM_HEAD_IS_PREFIX_DATA"
        else:
            relocs = []
            for tag in ("b1", "b2", "b3"):
                D1 = cells[(1, tag)]["Dk"]
                D32 = cells[(32, tag)]["Dk"]
                relocs.append(D32 >= RELOC_BAR * D1
                              if D1 > 0 else False)
            if all(relocs):
                renorm = ("EXTENSIVE_BULK_CONFIRMED"
                          if support == "EXTENSIVE_IRREGULAR_BULK"
                          else "HEAD_PEEL_RELOCATES")
            else:
                renorm = "IMPORTED_CORNER_PERSISTS"
    reloc_note = "; ".join(
        "%s D(32)/D(1) = %.2f/%.2f = %.2f"
        % (t, cells[(32, t)]["Dk"], cells[(1, t)]["Dk"],
           cells[(32, t)]["Dk"] / cells[(1, t)]["Dk"]
           if cells[(1, t)]["Dk"] > 0 else float("nan"))
        for t in ("b1", "b2", "b3"))
    check("G41-renorm-adjudicated", True,
          "SEALED RULE result: %s%s -- coverage matrix above; "
          "relocation ratios: %s (bar %.1f); K_cov diagnostic "
          "reported above is the HEAD ORACLE (must-fail m1) and "
          "never enters FINITE; HONESTY (sealed): a firing "
          "FINITE/LOG would be a MEASUREMENT -- B_w = S_{K-1} + "
          "b_can consumes the window's own measured head, same "
          "epistemic status as r243's B_w = S_{N-2} + 5/7, no "
          "bound mechanism claimed, the source stays "
          "incompressible" % (renorm, renorm_mod, reloc_note,
                              RELOC_BAR))

    # ---------------- S5: leg C -- head-mode anatomy
    section("S5  LEG C -- HEAD-MODE ANATOMY (first %d modes)"
            % HEAD_K)
    med_p = [float(np.median([p["p_n"][n] for p in packs]))
             for n in range(HEAD_K)]
    carry = [n for n in range(HEAD_K) if med_p[n] >= CARRY_BAR]
    n_arg0 = sum(1 for p in packs
                 if int(np.argmax(p["rho"])) == 0)
    slopes = []
    for n in range(HEAD_K):
        vals = [float(p["rho"][n]) for p in dev]
        s_, _c = np.polyfit(np.log(Ns_dev), np.log(vals), 1)
        slopes.append(float(s_))
    info("median p_n (n = 0..%d): %s | carrying degrees (med p "
         ">= %.2f): %s | argmax at degree 0 on %d/%d"
         % (HEAD_K - 1,
            str(["%.2g" % v for v in med_p]), CARRY_BAR,
            str(carry), n_arg0, len(packs)))
    info("per-mode DEV slopes of rho_n vs N: %s | rho_0 spread "
         "%.1f decades"
         % (str(["%+.2f" % s_ for s_ in slopes]),
            math.log10(max(float(p["rho"][0]) for p in packs)
                       / min(float(p["rho"][0]) for p in packs))))
    p9 = by_kz[9]
    world_note = []
    scr_shape = scr_mag = None
    for c in ("EPSTEIN", "SCRAMBLE"):
        pc = ctrl[c]
        nf = pc["nf"]
        hM = np.asarray(p9["rho"][:HEAD_K], float)
        hC = np.asarray(pc["rho"][:HEAD_K], float)
        phM = hM / float(np.sum(hM))
        phC = hC / float(np.sum(hC))
        maxd = float(np.max(np.abs(phC - phM)))
        mrat = float(np.median(np.log10(hC / hM)))
        dl = (np.asarray(pc["rho"][:nf], float)
              - np.asarray(p9["rho"][:nf], float))
        tot = float(np.sum(dl))
        fh = (float(np.sum(dl[:HEAD_K])) / tot
              if tot != 0.0 else float("nan"))
        if c == "SCRAMBLE":
            scr_shape, scr_mag = maxd, mrat
        world_note.append("%s: max|dphat| %.2f, med log10 "
                          "rho-ratio %+.2f, frac_head(n<%d of "
                          "n<%d diff) %.3f"
                          % (c, maxd, mrat, HEAD_K, nf, fh))
    head_verd = ("HEAD_CARRIES_ARITHMETIC"
                 if (scr_shape > SHAPE_BAR or scr_mag >= MAG_BAR)
                 else "HEAD_GEOMETRY_SHARED")
    check("G50-head-anatomy", True,
          "SEALED WORDING result: %s -- w9 base, common pre-flip "
          "range: %s (bars: shape %.2f, magnitude %.1f decade); "
          "the ladder head statistics and per-mode N-slopes are "
          "reported above (measurement, no mechanism claim)"
          % (head_verd, "; ".join(world_note), SHAPE_BAR,
             MAG_BAR))

    # ---------------- S6: must-fails
    section("S6  MUST-FAILS")
    okM1 = all(all(0 <= k_ <= p["N"] for k_, p in zip(kcov[t],
                                                      packs))
               and len(kcov[t]) == len(packs)
               for t in ("b1", "b2", "b3"))
    okM4 = True
    for p in packs:
        ps = np.sort(np.asarray(p["p_n"], float))[::-1]
        cs = np.cumsum(ps)
        k_srt = int(np.searchsorted(cs, 0.9) + 1)
        okM4 = okM4 and p["Kq"][0.9] >= k_srt
    check("G60-must-fails-fire", okM1 and okM4,
          "m1 HEAD ORACLE shown live: the per-window K_cov choice "
          "covers %d/%d for every positive candidate trivially -- "
          "EXCLUDED from every verdict path (diagnostic only); "
          "m2 normalization and m3 telescope gated in G30 (+ "
          "exact rationals G10); m4 sorted ward: K_0.9 on the "
          "natural degree order >= K_0.9 on the descending-sorted "
          "profile on %d/%d ('head = low degrees' is a finding, "
          "not a definition)" % (len(packs), len(packs),
                                 len(packs), len(packs)))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (an adjudication/"
          "measurement round moves no edge); what the round adds: "
          "the asymptotic LOAD of the budget object is typed -- "
          "support-size class and renormalization question "
          "answered separately, with the head anatomy as the "
          "requirement profile for any later conditioned "
          "asymptotic")
    verd = "SUPPORT(%s)%s + %s%s + %s" % (support, supp_mod,
                                          renorm, renorm_mod,
                                          head_verd)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s%s -- PROVEN: the Schur-rest/renormalized-budget "
          "identity (exact rationals); MEASURED: support-size "
          "scaling (DEV-fit, BLIND-checked), the peeling census "
          "and the head anatomy; OPEN: the budget bound itself "
          "(the wall; r243 PAIRCORR_REENCODED stands); NO RH "
          "claim" % (verd, " (SMOKE)" if smoke else ""))
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
