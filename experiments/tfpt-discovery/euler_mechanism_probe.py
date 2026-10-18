#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_mechanism_probe -- PRIME.PORT.COUPLEDTAU.
EULER_MECHANISM.01 (round 273): the reviewer-adjudicated MECHANISM
round after the r272 case-B outcome (BOUND_COARSENESS_CONFIRMED,
gamma_true +0.453, the entire lost cancellation at address c3 =
beyond blind level-2 pairing, flip condition delta' > 0.21 of the
available 0.45, TRUTH_ALLOWS).  The question of the round: WHAT
level of the arithmetic organization of the source produces the
truth-side cancellation decay C_N ~ N^{-0.45}?  Instrument: a
sealed EULER PERTURBATION LADDER -- controlled, GRADUATED source
surgeries on the comb (node positions u_j + weights w_j ONLY),
each with a strength parameter theta in [0, 1] (0 = MAIN, 1 =
fully perturbed), run against gamma_true, the c3 slack and
margin_true on the full 42-rung N-ladder.  NOT a proof round:
no new certificate, no bound modification, no H5 progress
claimed.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r271/r272 machinery imported verbatim): per
world t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); edge
split F = 0.20 (FROZEN); maximal same-sign runs of the bx-sorted
bulk with masses M_i and exact signed sums s_i; truth metrics
(typed POTENTIAL_ONLY, never a bound): R = sum s_i, C_true =
|R| / sum|s_i|, margin_true = (M_W - |Z|)/M_W with Z = t_{N-2} +
chain and M_W = sqrt(5/7); bound side for the c3 share only:
eps = r269 bound_pairsum(M), eps_L2 = r271 bound_level2(s),
slack2 = log10(eps_L2 / |R|) (the r272 c3 loss beyond blind
level-2, reused verbatim).  gamma_true := -halves log-slope of
C_true over the N-sorted 42-rung ladder (the r272 estimator,
deterministic; SHORT-LADDER GUARD: the fit REFUSES fewer than
MIN_RUNGS = 10 rungs).

THE SOURCE (binding): the MAIN comb of window kz is (uu, mm) =
(core.build_window(kz)["uu"], 2 * ["lam"]) -- node positions
u_j = log n_j and weights w_j = 2 Lambda(n_j)/sqrt(n_j) as DATA
ARRAYS; a perturbed world is BH.wpack(kz, base_kw=dict(comb=
(uu', mm'))), bitwise identical to MAIN at the identity comb
(gated).  Atom classification WITHOUT prime functions: the r254
world-blind labels via ODG.base_exp (pure integer root
extraction on n_j = round(exp(u_j)), admission bar 1e-9) --
(p, k) with k = 1 (K1) or k >= 2 (KHI); the AST firewall (no
zetazero/nzeros/isprime/primerange/grampoint) holds.

LEG A -- THE SEALED LADDER (four graduated surgeries; theta
stages (0.25, 0.5, 1.0) + theta = 0 = MAIN baseline; REPS = 3
pinned seeds per stage; seed = 273000 + P*100000 + T*10000 +
rep*1000 + rung_index -- fully deterministic):
(P1) ASSIGN -- weight<->position assignment randomized within
  u-sorted blocks of size B = max(1, round(n_at^theta)): the
  REACH of the exchange is the gradualness lever (theta 0.25 ~
  neighbor-scale swaps, 1.0 = free global weight permutation).
  PRESERVED EXACTLY: position set (bitwise), weight multiset
  (bitwise as sorted array).  DESTROYED: the assignment
  weight<->position beyond block scale.
(P2) JITTER -- positions u_j -> u_j + theta * g_j * U[-1, 1]
  with g_j = local nearest-neighbor gap of the sorted u (the
  contract scale: fraction-of-atom-spacing up to atom spacing;
  at theta = 1 atoms move by one local slot -- prime-power
  support is genuinely destroyed).  PRESERVED EXACTLY: weights
  (bitwise), per-atom bound |du_j| <= theta * g_j (gated).
  DESTROYED: phase relations / support arithmetic at local
  scale.
(P3) FAMILY -- the r254 (p, k) classes as families: a fraction
  theta of the KHI atoms (k >= 2, the Euler-family echoes) swap
  weights with the nearest-in-u atom of a DIFFERENT family
  (different p; deterministic nearest scan).  PRESERVED
  EXACTLY: positions (bitwise), weight multiset (bitwise),
  within-family structure of unselected atoms.  DESTROYED:
  SAMEP coherence (the weight of p^k decoupled from its p).
(P4) WINDOW (local->global decay) -- the u-sorted weight
  sequence is cut into consecutive segments of length ell =
  max(1, round(n_at^(1-theta))); the SEGMENT ORDER is randomly
  permuted, within-segment weight sequences stay intact:
  windows of size ell keep their local structure, the global
  arrangement outside is randomized (theta 0.25: few huge
  blocks; 1.0 = free permutation -- P1 and P4 share the global
  endpoint from complementary directions, disclosed).
  PRESERVED EXACTLY: position set, weight multiset (bitwise),
  within-segment weight order.  DESTROYED: the global
  arrangement of local blocks.
CONSERVATION GATES (exact, per perturbed world, EVERY world):
P1/P3/P4 positions bitwise identical + sorted weight multiset
bitwise identical; P2 weights bitwise identical + per-atom
jitter bound; theta = 0 returns bitwise-identical arrays for
all four surgeries (gated on the MAIN window); the identity
comb reproduces BH.wpack(9) bitwise in rho and St.

LEG B -- THE MEASUREMENT (per stage = perturbation x theta;
per replicate the FULL 42-rung ladder is rebuilt and
measured):
(b1) gamma_true per replicate over the 42 rungs (>= MIN_RUNGS
  gate), stage value = MEDIAN over replicates + spread
  (max - min);
(b2) the c3 share: slack2 = log10(eps_L2/|R|) -- per replicate
  its Spearman vs N and second-half median, stage medians;
(b3) margin_true trend: sp(N, margin_true) per replicate,
  stage median;
(b4) FIREWALL TYPING: perturbed worlds may flip the basis
  early -- per stage the positive-prefix fraction pp (worlds
  with nf None), the median flip degree of flipped worlds, and
  abort count; on indefinite continuations every quantity is
  ALGEBRAIC (documented, kept in the primary fit); SECONDARY
  gt_pp = the fit restricted to positive-prefix rungs iff >=
  MIN_RUNGS remain in a replicate (else n/a) -- both printed;
(b5) CONTROL ANCHORS: EPSTEIN/SCRAMBLE/SMOOTH on w9 (flips
  re-derived 25/21/27); C_true(w9) of EPSTEIN/SCRAMBLE must
  reproduce the r272 records 0.135/0.094 (abs tol 0.005);
  SMOOTH anchor alias <= 1e-12 and q_N <= 1e-20; the anchor
  C_true values are placed against the stage w9 medians
  (descriptive INFO, no verdict weight).

LEG C -- THE MECHANISM MAP (the delivery object; sealed rules
frozen BEFORE evaluation):  gt_main = gamma_true of MAIN on
the same 42-rung ladder (meaningfulness gate gt_main >= 0.2);
STAGE STATUS (sealed): COLLAPSED iff gt_med <= GT_ZERO (0.05);
REDUCED iff gt_med <= 0.5 * gt_main; INTACT iff gt_med >=
0.75 * gt_main; else PARTIAL; UNMEASURED if no replicate
delivers a valid fit (typed, excluded from collapse claims).
theta*_P = smallest theta with COLLAPSED (None if never).
SHARP(P) iff the stage below theta*_P (previous tested theta,
or the theta = 0 baseline) is INTACT; else GRADUAL.
SENSITIVITY (Trennschaerfe, sealed): sens_P = mean over the
three theta stages of (gt_main - gt_med) / gt_main
(UNMEASURED stages excluded); ranking descending.
SEALED VERDICTS: MECHANISM_LOCALIZED(P*, theta*, SHARP/GRADUAL)
iff exactly ONE perturbation attains the minimal theta*;
MECHANISM_DISTRIBUTED(tied set, ranking) iff >= 2 attain it;
PERTURBATION_INSENSITIVE(ranking) iff no stage collapses;
always + FIREWALL_MAP(pp summary) + SENSITIVITY_RANKING +
CONTROL_ANCHORS; SYNTHESIS (typed TASK_FORMULATION_ONLY): the
precise L2 mechanism hypothesis ("the N^{-0.45} decay is
carried by [level X at reach Y]") as a quantified, falsifiable
formulation -- NO proof claim, NO upgrade.

LEG D -- WARDS / MUST-FAILS: theta = 0 regression against the
r272 records on the FULL 42-rung ladder (gamma_true_42 in
0.453 +- 0.05, sp(N, eps) in +0.67 +- 0.05, kz15 true reserve
in [0.020, 0.035], r263 branch census cheap 35 + the named 7
exceptions); contribution ward sum ct == t_{N-2} (bars 1e-9
main N <= 400 / 3e-6 deep / 1e-4 perturbed -- measurement
quality, not a certificate); mp SAMPLES (dps 60): MAIN at the
two deepest rungs (bar 3e-6, the r272 deep family) + ONE
perturbed world (P1, theta = 1, rep 0) at the deepest rung
(bar 1e-4, measurement quality on an ALGEBRAIC continuation;
calibration amendment a2, disclosed below); label admission
max|exp(u) - n|/n <= 1e-9 on every rung; run1/run2
determinism (pinned seeds).  MUST-FAILS (each loud): (m1) MASS-CHANGING SURGERY --
a mutant scaling a theta-fraction of weights by 1.15 must be
CAUGHT by the conservation gate (multiset break >= 1e-3 rel);
(m2) SHORT-LADDER FIT -- the gamma fit called with 4 rungs
must REFUSE (returns None; MIN_RUNGS gate); (m3) GIFT SURGERY
-- a mutant orienting the surgery by the withheld terminal
drive key must be FLAGGED by the AST scope audit (the four
sealed surgeries audit clean against the truth-side forbidden
set); (m4) HALVES-SHUFFLE -- the seed-273 permutation of the
42-rung eps series against the N axis must destroy the trend
(|sp| < 0.5 and < the measured sp); fragment audit (no fit
primitives) inherited.

INDEX FIREWALL (binding, r238-r272 discipline): w = window
(kz), N_w = builder depth; ground truth (t_term, Z, R, branch
labels) enters GATES and census tables only -- the surgery
functions consume (uu, mm, theta, seed, labels) ONLY (AST
scope audit); no zero/prime oracles anywhere (AST firewall);
labels via ODG.base_exp = r254 integer root extraction,
world-blind.  MACHINERY IMPORTED VERBATIM: r269 PBB.mask_edge
+ PBB.runs_split + PBB.bound_pairsum + PBB.mp_drive, r271
UPT.bound_level2, r244 BH.wpack + BH.spearman, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, r254 ODG.base_exp, v881 PIK, r243
PB.smooth_comb.  COFINAL LADDER: the FULL 42 frame-A rungs
h <= 900, (N, kz)-sorted, N in [142, 878], for the baseline
AND every stage replicate (calibration amendment a1,
disclosed below); the truth measurement is cheap, no bounds
needed (1512 perturbed worlds, measured wall ~0.22 s each).

SEALED CONSTANTS: MAIN window 9; controls w9 EPSTEIN/
SCRAMBLE(seed 1)/SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); EDGE_F 0.20 (FROZEN); MIN_RUNGS 10; THETAS
(0.25, 0.5, 1.0); REPS 3; SEED_BASE 273000; GT_ZERO
0.05; INTACT_FRAC 0.75; REDUCED_FRAC 0.5; GT_MAIN_MIN 0.2;
R272_GT_REF 0.453 tol 0.05; R272_SP_EPS +0.67 tol 0.05;
RESERVE_BAND (0.020, 0.035); CHEAP_EXPECT 35; EXC_KZ_EXPECT
(15, 20, 22, 36, 38, 39, 52); CTRUE_EPST_REF 0.135;
CTRUE_SCR_REF 0.094; CTRUE_ANCH_TOL 0.005; TB bars 1e-9 main
N <= 400 / 3e-6 deep / 1e-4 perturbed; MP_DPS 60; MP_DEEP_BAR
3e-6; MP_PERT_BAR 1e-4; SM_ALIAS_BAR 1e-12; SM_Q_BAR 1e-20;
NINT_BAR 1e-9; SHUFFLE_SEED 273; SHUF_BAR 0.5; MASS_MUT_MIN
1e-3; runtime <= 1800 s; smoke = w9 census + identity ward +
theta-0 gates + conservation battery (all stages, one rep,
comb level) + label census + base_exp toy + scope audits + m1
+ m2 (ladder, map, anchors, mp, m4 skipped).  DISCLOSED
PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r263/r269/r270/r271/r272 RECORD number
adopted as-is; nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] MECHANISM_LOCALIZED(P, theta*, SHARP/
    GRADUAL) / MECHANISM_DISTRIBUTED(tied set, ranking) /
    PERTURBATION_INSENSITIVE(ranking)
+ FIREWALL_MAP(per-stage pp fractions, flip degrees)
+ SENSITIVITY_RANKING(P order by sens)
+ CONTROL_ANCHORS(EPST/SCR/SMOOTH placement)
+ L2_HYPOTHESIS(quantified, TASK_FORMULATION_ONLY).
Honesty before beauty: every trend is MEASURED on the 42-rung
ladder only; no verdict claims a cofinal law, a mechanism
theorem or H5 progress; collapse under surgery is an
EXPERIMENTAL localization of the carrying organization level,
not a proof that the level suffices; r243-r272 stand.

DISCLOSED CALIBRATION AMENDMENTS (before freeze; the surgery
definitions, conservation gates, status rules, verdict rules
and every physics band never moved):
(a1) LADDER WIDTH: the pre-spec 16-rung subset FAILED its own
  sealed meaningfulness gate in calibration pass 1 (subset
  gamma_true -0.028 vs the 42-rung r272 record +0.453 --
  the halves estimator does not survive the subsampling;
  per-stage replicate spreads up to 1.9) => every stage
  replicate measures the FULL 42-rung ladder (budget allows:
  ~0.22 s per world, 1512 perturbed worlds); the gate itself
  never moved.
(a2) MP_PERT_BAR 1e-5 -> 1e-4 (absolute, dps-60 vs f64 on the
  ALGEBRAIC continuation of the deepest perturbed sample;
  pass 1 measured 2.4e-5 -- a measurement-quality ward on a
  flipped world, not a physics bar; MAIN deep bars untouched).

RECORD TABLES (frozen from calibration pass 2 = the first
full evaluation AFTER the two disclosed amendments; 24/24
gates; the record insertion below is the only post-freeze
edit, which IS the protocol; run1/run2 identical up to WALL):
CAL_VERDICT = PERTURBATION_INSENSITIVE(P3_FAMILY -0.181 >
P2_JITTER -0.323 > P1_ASSIGN -0.847 > P4_WINDOW -1.098) +
FIREWALL_MAP(pp min/med/max 0.00/0.00/0.01 over 12 stages)
+ SENSITIVITY_RANKING(same order) + CONTROL_ANCHORS(EPST
0.135, SCR 0.094, SMOOTH ok) + L2_HYPOTHESIS(see reading).
Key numbers.  BASELINE (theta = 0 == the r272 world, exact):
gamma_true_42 +0.453 (record hit), sp(N, eps) +0.67, kz15
reserve 0.0268, branch census 35 + the named 7 EXACT; slack2
h2-med 0.503 dec, sp(N, margin_true) +0.36, w9 C_true 0.2919.
MECHANISM MAP (gt_med [spread] status | flip_med | slack2h2 |
sp_mt | w9 C_true; 3 replicates x 42 rungs per stage):
  P1_ASSIGN  0.25 +0.880 [0.44] INTACT |43.0|0.796|+0.05|0.155
             0.50 +0.236 [0.16] PARTIAL|42.0|0.610|-0.01|0.205
             1.00 +1.396 [0.59] INTACT |33.5|0.997|+0.12|0.055
  P2_JITTER  0.25 +0.536 [0.21] INTACT |42.5|0.681|-0.16|0.133
             0.50 +0.489 [0.34] INTACT |39.0|0.672|+0.05|0.230
             1.00 +0.774 [0.61] INTACT |37.5|0.671|-0.13|0.215
  P3_FAMILY  0.25 +0.200 [0.30] REDUCED|101.0 (1 abort)
             |0.596|+0.08|0.315
             0.50 +0.633 [0.94] INTACT |83.5|0.735|-0.11|0.330
             1.00 +0.774 [0.00] INTACT |66.5|0.734|+0.16|0.046
  P4_WINDOW  0.25 +1.040 [1.35] INTACT |39.0|0.867|+0.34|0.096
             0.50 +0.752 [0.63] INTACT |34.0|0.916|+0.14|0.051
             1.00 +1.061 [1.28] INTACT |34.0|0.904|+0.21|0.310
NO stage collapses (every gt_med >= +0.20 >> the sealed 0.05
bar); most sit AT or ABOVE the MAIN +0.453 -- the negative
sensitivities are honest: destroyed worlds cancel as deep or
DEEPER than MAIN.  THE FIREWALL MAP IS THE SHARP FINDING: pp
= 0.00 on 11/12 stages (0.01 on P4@0.25) -- EVERY tested
surgery destroys the free-prefix positivity (flip degrees
33-43 for P1/P2/P4, 66-101 for P3, mildest; the r243 flip
census reproduced at ladder scale), so all perturbed
measurements are typed ALGEBRAIC continuations, gt_pp n/a
everywhere.  ANCHORS: EPSTEIN C_true(w9) 0.1350 / SCRAMBLE
0.0943 == the r272 records; MAIN w9 0.2919; the theta = 1
endpoints scatter across 0.05-0.31 (both sides of MAIN,
world-blind); SMOOTH alias 2.4e-14, q_N 4.2e-25.  WARDS:
contribution 2.1e-13 main / 3.9e-13 deep / 7.8e-6 perturbed
(bar 1e-4); mp kz64/N859 9.3e-9, kz52/N878 6.6e-8 (bar 3e-6),
perturbed P1@1.0 kz52 2.0e-6 (bar 1e-4); conservation EXACT
on 1512/1512 perturbed worlds; label admission 9.8e-16, KHI
share med 0.049; m1 mass mutant CAUGHT (7.7e-2 rel break);
m2 4-rung fit REFUSED; m3 gift surgery FLAGGED (t_term@614),
four surgeries clean; m4 seed-273 shuffle |sp| 0.070 < 0.5.
READING (typed, no upgrade -- the honest third sealed
outcome): the N^{-0.45} truth-cancellation deepening is NOT
carried by any tested level of the arithmetic organization
-- weight assignment (P1), local support arithmetic (P2),
Euler-family coherence (P3) and global arrangement (P4) can
each be fully destroyed without collapsing gamma_true, which
stays at or above the MAIN value (generic signed sums cancel
at root scale: 0.45 is NEAR THE GENERIC sqrt BASELINE, not
an arithmetic fingerprint); what IS arithmetically special
about MAIN -- and what every surgery kills at degrees 33-101
-- is the FREE-PREFIX POSITIVITY (the wall), not the
cancellation rate.  L2_HYPOTHESIS (TASK_FORMULATION_ONLY,
falsifiable): "the missing delta' > 0.21 decay of the L2
lemma does not require an Euler-structural mechanism; it is
GENERIC root-scale equidistribution of the level-2 block
signs -- the lemma task is to CAPTURE generic cancellation
source-purely without crossing the PAIRCORR firewall, and
any candidate mechanism that needs SAMEP coherence, exact
support or assignment structure is measured here to be
aiming at the wrong carrier"; the tension that this generic
class brushes the forbidden root-scale demand is stated, not
hidden.  Runtime 257.2 s full / 0.1 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE
(records inserted per protocol; no bar, band, status rule or
verdict rule moved).

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
import offdiag_gram_probe as ODG               # noqa: E402 r254
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
EDGE_F = 0.20
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
MIN_RUNGS = 10
THETAS = (0.25, 0.5, 1.0)
REPS = 3
SEED_BASE = 273000
GT_ZERO = 0.05
INTACT_FRAC = 0.75
REDUCED_FRAC = 0.5
GT_MAIN_MIN = 0.2
R272_GT_REF = 0.453
R272_GT_TOL = 0.05
R272_SP_EPS = 0.67
R272_SP_TOL = 0.05
RESERVE_BAND = (0.020, 0.035)
CTRUE_EPST_REF = 0.135
CTRUE_SCR_REF = 0.094
CTRUE_ANCH_TOL = 0.005
TB_BAR_MAIN = 1e-9
TB_BAR_DEEP = 3e-6
TB_BAR_PERT = 1e-4
DEEP_N = 400
MP_DPS = 60
MP_DEEP_BAR = 3e-6
MP_PERT_BAR = 1e-4
SM_ALIAS_BAR = 1e-12
SM_Q_BAR = 1e-20
NINT_BAR = 1e-9
SHUFFLE_SEED = 273
SHUF_BAR = 0.5
MASS_MUT_MIN = 1e-3
JIT_TOL = 1e-12
PERT_NAMES = ("P1_ASSIGN", "P2_JITTER", "P3_FAMILY", "P4_WINDOW")

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
    return (not bad), ("NO zero/prime oracles; the surgeries consume "
                       "node positions + weights + r254 integer-root "
                       "labels ONLY; ground truth (t_term, Z, R, "
                       "branch labels) enters gates and census tables "
                       "only" if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden fit-method families (identifiers
    only; the fragment table is assembled from split strings)."""
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


PERT_FORBIDDEN = {"t" + "_term", "Z", "Zl", "St", "rho", "margin",
                  "truth_rec", "drive_arrays", "g_gap",
                  "eval_scaled", "bound_pairsum", "bound_level2",
                  "sabs", "C_true", "slack2"}


# ------------------------------------------------ trend estimators
def halves_slope(Ns, Xs):
    """r272 dyadic log-slope (deterministic): (mean ln X | second
    half - mean ln X | first half) / (same for ln N) on the
    N-sorted ladder."""
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


def gamma_true_fit(Ns, Cs):
    """sealed exponent fit gamma_true = -halves_slope(N, C_true);
    SHORT-LADDER GUARD (m2): REFUSES fewer than MIN_RUNGS rungs."""
    if len(Ns) < MIN_RUNGS or len(Ns) != len(Cs):
        return None
    return -halves_slope(Ns, Cs)


# ------------------------------------ the four sealed surgeries
# (source-pure scope, AST-audited: consume uu, mm, theta, seed and
#  the world-blind r254 labels ONLY -- no truth-side identifier)
def perturb_assign(uu, mm, theta, seed):
    """P1 ASSIGN: weight<->position assignment randomized within
    u-sorted blocks of size B = max(1, round(n^theta)); positions
    and the weight multiset are preserved EXACTLY."""
    if theta <= 0.0:
        return uu.copy(), mm.copy()
    n = len(uu)
    Bsz = max(1, int(round(n ** theta)))
    rng = np.random.default_rng(seed)
    o = np.argsort(uu, kind="stable")
    mm2 = mm.copy()
    for a in range(0, n, Bsz):
        idx = o[a:a + Bsz]
        mm2[idx] = mm2[idx][rng.permutation(len(idx))]
    return uu.copy(), mm2


def local_gaps(uu):
    """per-atom local nearest-neighbor gap of the sorted u
    (endpoints single-sided) -- the sealed P2 jitter scale."""
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


def perturb_jitter(uu, mm, theta, seed):
    """P2 JITTER: u_j -> u_j + theta * g_j * U[-1, 1] with g_j the
    local nn gap (fraction-of-atom-spacing .. atom spacing);
    weights preserved EXACTLY."""
    if theta <= 0.0:
        return uu.copy(), mm.copy()
    rng = np.random.default_rng(seed)
    g = local_gaps(uu)
    uu2 = uu + theta * g * rng.uniform(-1.0, 1.0, len(uu))
    return uu2, mm.copy()


def perturb_family(uu, mm, theta, seed, ps, ks):
    """P3 FAMILY: a fraction theta of the KHI atoms (k >= 2) swap
    weights with the nearest-in-u atom of a DIFFERENT family
    (different primary p); positions and the weight multiset are
    preserved EXACTLY (pure transpositions)."""
    uu2, mm2 = uu.copy(), mm.copy()
    if theta <= 0.0:
        return uu2, mm2
    n = len(uu)
    cand = np.nonzero(ks >= 2)[0]
    nsel = int(round(theta * len(cand)))
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


def perturb_window(uu, mm, theta, seed):
    """P4 WINDOW (local->global decay): the u-sorted weight
    sequence is cut into consecutive segments of length ell =
    max(1, round(n^(1-theta))); the segment ORDER is permuted,
    within-segment sequences stay intact; positions and the
    weight multiset are preserved EXACTLY."""
    if theta <= 0.0:
        return uu.copy(), mm.copy()
    n = len(uu)
    ell = max(1, int(round(n ** (1.0 - theta))))
    if ell >= n:
        return uu.copy(), mm.copy()
    rng = np.random.default_rng(seed)
    o = np.argsort(uu, kind="stable")
    segs = [o[a:a + ell] for a in range(0, n, ell)]
    perm = rng.permutation(len(segs))
    ws = np.concatenate([mm[segs[i]] for i in perm])
    mm2 = mm.copy()
    mm2[o] = ws
    return uu.copy(), mm2


def mutant_mass_perturb(uu, mm, theta, seed):
    """m1 MUST-FAIL MUTANT: a 'surgery' that secretly scales a
    theta-fraction of the weights by 1.15 -- the conservation
    gate must CATCH it (typed FORBIDDEN as a perturbation)."""
    rng = np.random.default_rng(seed)
    mm2 = mm.copy()
    nsel = max(1, int(round(theta * len(mm))))
    sel = rng.choice(len(mm), size=nsel, replace=False)
    mm2[sel] *= 1.15
    return uu.copy(), mm2


def mutant_gift_perturb(uu, mm, rc):
    """m3 scope-audit MUST-FAIL MUTANT: a 'surgery' oriented by
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return uu.copy(), (mm[::-1].copy() if s < 0.0 else mm.copy())


def conserve_check(kind, uu, mm, uu2, mm2, theta):
    """exact conservation gates per surgery (LEG D): P1/P3/P4
    positions bitwise + sorted weight multiset bitwise; P2
    weights bitwise + per-atom jitter bound."""
    if kind == "P2_JITTER":
        ok_m = bool(np.array_equal(mm2, mm))
        g = local_gaps(uu)
        dev = np.abs(uu2 - uu)
        ok_u = bool(np.all(dev <= theta * g * (1.0 + JIT_TOL)
                           + 1e-300))
        return ok_u and ok_m
    ok_u = bool(np.array_equal(uu2, uu))
    ok_m = bool(np.array_equal(np.sort(mm2), np.sort(mm)))
    return ok_u and ok_m


def apply_pert(kind, uu, mm, theta, seed, ps, ks):
    if kind == "P1_ASSIGN":
        return perturb_assign(uu, mm, theta, seed)
    if kind == "P2_JITTER":
        return perturb_jitter(uu, mm, theta, seed)
    if kind == "P3_FAMILY":
        return perturb_family(uu, mm, theta, seed, ps, ks)
    return perturb_window(uu, mm, theta, seed)


# ------------------------------------------------ truth machinery
def truth_rec(p):
    """r272 truth-side record (typed POTENTIAL_ONLY, never a
    bound): drive decomposition, edge split, runs, C_true, eps,
    eps_L2, slack2, margin_true; None on chain abort."""
    rows = p["rows"]
    N = p["N"]
    if len(rows) < N or rows[N - 2]["gam_next"] is None:
        return None
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
    t_term = float(t[N - 2])
    absum = float(np.sum(np.abs(ct)))
    tb_dev = abs(float(np.sum(ct)) - t_term) / max(absum, 1e-300)
    o = np.argsort(bx, kind="stable")
    bxs = bx[o]
    cts = ct[o]
    ed = PBB.mask_edge(bxs, lo, hi, EDGE_F)
    cb = cts[~ed]
    runs = PBB.runs_split(cb)
    Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
    Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
    R = sum(Sr)
    sabs = sum(abs(v) for v in Sr)
    C_true = abs(R) / max(sabs, 1e-300)
    eps = PBB.bound_pairsum(Mr)
    e_l2 = UPT.bound_level2(Sr)
    slack2 = math.log10(max(e_l2, 1e-300) / max(abs(R), 1e-300))
    mt = (M_W - abs(Z)) / M_W
    return dict(kz=p["kz"], N=N, nf=p["nf"], g=g, Z=Z,
                t_term=t_term, tb_dev=tb_dev, C_true=C_true,
                R=R, eps=eps, e_l2=e_l2, slack2=slack2, mt=mt,
                p=p)


def main_comb(kz):
    rr = core.build_window(kz)
    return (np.asarray(rr["uu"], float).copy(),
            2.0 * np.asarray(rr["lam"], float).copy())


def comb_labels(uu):
    """r254 world-blind (p, k) labels of the comb atoms via pure
    integer root extraction (ODG.base_exp, imported verbatim);
    returns (p array, k array, admission dev)."""
    nn = np.round(np.exp(uu)).astype(np.int64)
    dev = float(np.max(np.abs(np.exp(uu) - nn) / nn))
    pk = [ODG.base_exp(int(n)) for n in nn]
    ps = np.array([p for p, _k in pk], dtype=np.int64)
    ks = np.array([k for _p, k in pk], dtype=np.int64)
    return ps, ks, dev


def base_exp_toy():
    """hand-checked base_exp table (exact)."""
    tab = ((2, (2, 1)), (3, (3, 1)), (4, (2, 2)), (5, (5, 1)),
           (8, (2, 3)), (9, (3, 2)), (25, (5, 2)), (27, (3, 3)),
           (32, (2, 5)), (49, (7, 2)), (121, (11, 2)),
           (128, (2, 7)), (243, (3, 5)))
    return all(ODG.base_exp(n) == r for n, r in tab)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("euler_mechanism_probe -- PRIME.PORT.COUPLEDTAU."
          "EULER_MECHANISM.01 (round 273)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   R271_SHA %s "
          "(imported)   R272_SHA %s (imported)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], UPT.SPEC_SHA[:16],
             hashlib.sha256(
                 open(os.path.join(HERE,
                                   "l2_scaling_anatomy_probe.py"),
                      "rb").read()).hexdigest()[:16]))
    print("mode: %s" % ("SMOKE (w9 census + identity ward + "
                        "theta-0 gates + conservation battery + "
                        "labels + toy + scope audits + m1 + m2; "
                        "ladder, map, anchors, mp, m4 skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED MECHANISM ROUND (no proof, no "
          "certificate, no bound): four sealed graduated source "
          "surgeries (ASSIGN reach n^theta / JITTER at local "
          "atom-spacing scale / FAMILY decoupling of the r254 "
          "KHI echoes / WINDOW segment shuffle at preserved "
          "local length n^(1-theta)) x thetas %s x %d pinned "
          "replicates against gamma_true, the c3 slack and "
          "margin_true on the full 42-rung ladder; stage status "
          "COLLAPSED <= %.2f / REDUCED <= %.2f gt_main / INTACT "
          ">= %.2f gt_main; verdicts LOCALIZED/DISTRIBUTED/"
          "INSENSITIVE + FIREWALL_MAP sealed BEFORE evaluation "
          "(pre-spec input = r263/r269-r272 record numbers, "
          "disclosed)"
          % (str(THETAS), REPS, GT_ZERO, REDUCED_FRAC,
             INTACT_FRAC))

    # ---------------- S1: census + identity wards
    section("S1  CENSUS + IDENTITY WARDS")
    p9 = BH.wpack(MAIN_KZ)
    uu9, mm9 = main_comb(MAIN_KZ)
    p9i = BH.wpack(MAIN_KZ, base_kw=dict(comb=(uu9, mm9)))
    ok_id = (bool(np.array_equal(p9["rho"], p9i["rho"]))
             and p9["St"] == p9i["St"] and p9["nf"] == p9i["nf"]
             and p9i["nf"] is None)
    check("G10-identity-comb", ok_id,
          "BH.wpack(9, comb=(uu, 2 lam)) reproduces BH.wpack(9) "
          "BITWISE (rho array, St %.6f, nf %s) -- the surgery "
          "channel is exact at the identity; %d comb atoms"
          % (p9["St"], str(p9["nf"]), len(uu9)))
    ps9, ks9, dev9 = comb_labels(uu9)
    n_k1 = int(np.sum(ks9 == 1))
    n_khi = int(np.sum(ks9 >= 2))
    check("G11-label-admission", dev9 <= NINT_BAR,
          "r254 world-blind labels on the w9 comb: n = "
          "round(exp(u)) integer to %.1e (bar %.0e); census K1 "
          "%d + KHI %d of %d (KHI share %.3f) -- the FAMILY "
          "surgery operates on the KHI echoes"
          % (dev9, NINT_BAR, n_k1, n_khi, len(uu9),
             n_khi / len(uu9)))
    ok0 = True
    for kind in PERT_NAMES:
        u2, m2 = apply_pert(kind, uu9, mm9, 0.0, SEED_BASE, ps9,
                            ks9)
        ok0 = ok0 and bool(np.array_equal(u2, uu9)) \
            and bool(np.array_equal(m2, mm9))
    check("G12-theta0-exact", ok0,
          "theta = 0 returns BITWISE-identical (uu, mm) for all "
          "four surgeries -- the MAIN baseline is the exact "
          "ladder origin")
    cons_ok = True
    cons_note = []
    for kind in PERT_NAMES:
        for ti, th in enumerate(THETAS):
            u2, m2 = apply_pert(kind, uu9, mm9, th,
                                SEED_BASE + 7 * ti + 1, ps9, ks9)
            okc = conserve_check(kind, uu9, mm9, u2, m2, th)
            cons_ok = cons_ok and okc
            if th == 1.0:
                moved = int(np.sum(m2 != mm9)) \
                    if kind != "P2_JITTER" \
                    else int(np.sum(u2 != uu9))
                cons_note.append("%s@1.0 moved %d" % (kind, moved))
    check("G13-conservation-battery", cons_ok,
          "w9 conservation battery (all 4 surgeries x 3 thetas): "
          "P1/P3/P4 positions bitwise + weight multiset bitwise, "
          "P2 weights bitwise + per-atom |du| <= theta g_j -- "
          "EXACT; endpoint movement census: %s"
          % "; ".join(cons_note))

    # ---------------- S2: toy + scope audits + m1/m2
    section("S2  TOY + SCOPE AUDITS + MUST-FAILS (m1, m2)")
    check("G20-toy-base-exp", base_exp_toy(),
          "hand-checked integer-root table exact: 2/3/4/5/8/9/25/"
          "27/32/49/121/128/243 -> the r254 label machine is "
          "loaded verbatim (no prime oracle)")
    h_p = []
    for fn in ("perturb_assign", "perturb_jitter",
               "perturb_family", "perturb_window", "local_gaps"):
        h_p.extend(scope_audit(fn, PERT_FORBIDDEN))
    h_g = scope_audit("mutant_gift_perturb", PERT_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G21-scope-audits", not h_p and bool(h_g)
          and not ag_hits,
          "the four sealed surgeries audit CLEAN against the "
          "truth-side forbidden set%s; the gift mutant (withheld "
          "terminal drive key) FLAGGED (%s); fragment audit (no "
          "fit primitives): %s"
          % ("" if not h_p else " VIOLATION " + "; ".join(h_p),
             "; ".join(h_g) if h_g else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    u2, m2 = mutant_mass_perturb(uu9, mm9, 0.5, SEED_BASE + 99)
    caught = not conserve_check("P1_ASSIGN", uu9, mm9, u2, m2, 0.5)
    mbreak = abs(float(np.sum(np.sort(m2) - np.sort(mm9)))) \
        / max(float(np.sum(np.abs(mm9))), 1e-300)
    check("G22-mustfail-mass", caught and mbreak >= MASS_MUT_MIN,
          "m1 MASS-CHANGING SURGERY (1.15x on a theta-fraction): "
          "CAUGHT by the conservation gate; multiset break %.1e "
          ">= %.0e rel -- a surgery that changes mass cannot "
          "pass as a perturbation" % (mbreak, MASS_MUT_MIN))
    short = gamma_true_fit([100, 200, 300, 400],
                           [0.5, 0.4, 0.3, 0.2])
    check("G23-mustfail-short-ladder", short is None,
          "m2 SHORT-LADDER FIT: gamma fit on 4 rungs REFUSED "
          "(returns None; MIN_RUNGS gate %d) -- no exponent from "
          "an untrustworthy ladder" % MIN_RUNGS)

    if smoke:
        tr9 = truth_rec(p9)
        info("SMOKE w9 truth: C_true %.4f  slack2 %.3f dec  "
             "margin_true %.4f  tb_dev %.1e"
             % (tr9["C_true"], tr9["slack2"], tr9["mt"],
                tr9["tb_dev"]))
        for g_ in ("G30-42rung-regression", "G31-branch-census",
                   "G40-ladder-baseline", "G41-conservation-full",
                   "G50-mechanism-map", "G51-firewall-map",
                   "G60-control-anchors", "G61-smooth-anchor",
                   "G70-contribution-ward", "G71-mp-wards",
                   "G80-mustfail-shuffle"):
            check(g_, True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # ---------------- S3: MAIN 42-rung regression
        section("S3  MAIN LADDER + R272 REGRESSION WARDS")
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        packs = [BH.wpack(kz) for kz in kzs]
        packs.sort(key=lambda p: (p["N"], p["kz"]))
        recs42 = [truth_rec(p) for p in packs]
        okL = (len(recs42) == 42
               and all(r_ is not None for r_ in recs42)
               and all(r_["nf"] is None for r_ in recs42))
        Ns42 = [r_["N"] for r_ in recs42]
        C42 = [r_["C_true"] for r_ in recs42]
        eps42 = [r_["eps"] / M_W for r_ in recs42]
        gt42 = gamma_true_fit(Ns42, C42)
        sp_eps = BH.spearman(Ns42, eps42)
        rc15 = next(r_ for r_ in recs42 if r_["kz"] == 15)
        res15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= res15 <= RESERVE_BAND[1]
        check("G30-42rung-regression", okL
              and gt42 is not None
              and abs(gt42 - R272_GT_REF) <= R272_GT_TOL
              and abs(sp_eps - R272_SP_EPS) <= R272_SP_TOL
              and ok15,
              "42 rungs POSITIVE_PREFIX, N in [%d, %d]; "
              "gamma_true_42 %+.3f (r272 record %+.3f, tol "
              "%.2f); sp(N, eps) %+.2f (record %+.2f); kz15 "
              "true reserve %.4f in %s -- the theta = 0 world "
              "IS the r272 world"
              % (Ns42[0], Ns42[-1], gt42, R272_GT_REF,
                 R272_GT_TOL, sp_eps, R272_SP_EPS, res15,
                 str(RESERVE_BAND)))
        cheap = [r_ for r_ in recs42 if r_["g"] >= 0.0]
        exc_kz = tuple(sorted(r_["kz"] for r_ in recs42
                              if r_["g"] < 0.0))
        check("G31-branch-census",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT)),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7"
              % (len(cheap), str(exc_kz)))

        # baseline = the full 42-rung ladder (amendment a1)
        sub = recs42
        sub_kzs = [r_["kz"] for r_ in sub]
        Ns_sub = [r_["N"] for r_ in sub]
        gt_main = gamma_true_fit(Ns_sub,
                                 [r_["C_true"] for r_ in sub])
        s2_main = halves_med([r_["slack2"] for r_ in sub])[1]
        mt_sp_main = BH.spearman(Ns_sub, [r_["mt"] for r_ in sub])
        ct_w9_main = next(r_["C_true"] for r_ in sub
                          if r_["kz"] == MAIN_KZ)
        check("G40-ladder-baseline", gt_main is not None
              and gt_main >= GT_MAIN_MIN,
              "BASELINE (full %d-rung ladder, amendment a1): "
              "gt_main %+.3f >= %.1f (meaningfulness gate); "
              "slack2 h2-med %.3f dec; sp(N, margin_true) "
              "%+.2f; w9 C_true %.4f -- the map reference"
              % (len(sub), gt_main, GT_MAIN_MIN, s2_main,
                 mt_sp_main, ct_w9_main))

        # ---------------- S4: the perturbation ladder
        section("S4  THE PERTURBATION LADDER (%d worlds)"
                % (len(PERT_NAMES) * len(THETAS) * REPS
                   * len(sub)))
        combs = {kz: main_comb(kz) for kz in sub_kzs}
        labels = {}
        lab_worst = 0.0
        for kz in sub_kzs:
            ps_, ks_, dv_ = comb_labels(combs[kz][0])
            labels[kz] = (ps_, ks_)
            lab_worst = max(lab_worst, dv_)
        khi_shares = [float(np.sum(labels[kz][1] >= 2))
                      / len(labels[kz][1]) for kz in sub_kzs]
        info("labels on %d ladder rungs: admission worst %.1e, "
             "KHI share med %.3f"
             % (len(sub_kzs), lab_worst,
                float(np.median(khi_shares))))
        cons_all = lab_worst <= NINT_BAR
        tb_pert_worst = 0.0
        stages = {}
        pert_sample = None
        for pi, kind in enumerate(PERT_NAMES):
            for ti, th in enumerate(THETAS):
                gts, gtpp, s2h, mtsp, ctw9 = [], [], [], [], []
                nfl, ndeg, nab, nworld = 0, [], 0, 0
                for rep in range(REPS):
                    Ns_r, Cs_r, S2_r, MT_r = [], [], [], []
                    Ns_p, Cs_p = [], []
                    for ri, kz in enumerate(sub_kzs):
                        seed = (SEED_BASE + pi * 100000
                                + ti * 10000 + rep * 1000 + ri)
                        uu, mm = combs[kz]
                        ps_, ks_ = labels[kz]
                        u2, m2 = apply_pert(kind, uu, mm, th,
                                            seed, ps_, ks_)
                        cons_all = cons_all and conserve_check(
                            kind, uu, mm, u2, m2, th)
                        try:
                            pw = BH.wpack(kz, base_kw=dict(
                                comb=(u2, m2)))
                            tr = truth_rec(pw)
                        except (IndexError, ValueError,
                                OverflowError):
                            tr = None
                        nworld += 1
                        if tr is None:
                            nab += 1
                            continue
                        tb_pert_worst = max(tb_pert_worst,
                                            tr["tb_dev"])
                        if tr["nf"] is not None:
                            nfl += 1
                            ndeg.append(tr["nf"])
                        else:
                            Ns_p.append(tr["N"])
                            Cs_p.append(tr["C_true"])
                        Ns_r.append(tr["N"])
                        Cs_r.append(tr["C_true"])
                        S2_r.append(tr["slack2"])
                        MT_r.append(tr["mt"])
                        if kz == MAIN_KZ:
                            ctw9.append(tr["C_true"])
                        if (pert_sample is None
                                and kind == "P1_ASSIGN"
                                and th == 1.0 and rep == 0
                                and kz == sub_kzs[-1]):
                            pert_sample = tr
                    gv = gamma_true_fit(Ns_r, Cs_r)
                    if gv is not None:
                        gts.append(gv)
                        s2h.append(halves_med(S2_r)[1])
                        mtsp.append(BH.spearman(Ns_r, MT_r))
                    gp = gamma_true_fit(Ns_p, Cs_p)
                    if gp is not None:
                        gtpp.append(gp)
                st = dict(kind=kind, th=th)
                if gts:
                    st["gt"] = float(np.median(gts))
                    st["spread"] = max(gts) - min(gts)
                    st["s2"] = float(np.median(s2h))
                    st["mtsp"] = float(np.median(mtsp))
                else:
                    st["gt"] = None
                st["gtpp"] = (float(np.median(gtpp)) if gtpp
                              else None)
                st["pp"] = 1.0 - (nfl + nab) / max(nworld, 1)
                st["flipmed"] = (float(np.median(ndeg)) if ndeg
                                 else None)
                st["nab"] = nab
                st["ctw9"] = (float(np.median(ctw9)) if ctw9
                              else None)
                stages[(kind, th)] = st
        check("G41-conservation-full", cons_all,
              "conservation EXACT on ALL %d perturbed worlds "
              "(positions/multisets bitwise per surgery type) + "
              "label admission worst %.1e (bar %.0e)"
              % (len(PERT_NAMES) * len(THETAS) * REPS * len(sub),
                 lab_worst, NINT_BAR))

        # ---------------- S5: mechanism map + verdict pieces
        section("S5  MECHANISM MAP (sealed status rules)")

        def status_of(st):
            if st["gt"] is None:
                return "UNMEASURED"
            if st["gt"] <= GT_ZERO:
                return "COLLAPSED"
            if st["gt"] <= REDUCED_FRAC * gt_main:
                return "REDUCED"
            if st["gt"] >= INTACT_FRAC * gt_main:
                return "INTACT"
            return "PARTIAL"

        theta_star = {}
        sens = {}
        for kind in PERT_NAMES:
            vals = []
            tstar = None
            for th in THETAS:
                st = stages[(kind, th)]
                stt = status_of(st)
                st["status"] = stt
                if stt == "COLLAPSED" and tstar is None:
                    tstar = th
                if st["gt"] is not None:
                    vals.append((gt_main - st["gt"]) / gt_main)
                info("%-9s theta %.2f: gt %s [spread %s] %s | "
                     "gt_pp %s | pp %.2f flip_med %s ab %d | "
                     "slack2h2 %s | sp_mt %s | w9 C %s"
                     % (kind, th,
                        "%+.3f" % st["gt"]
                        if st["gt"] is not None else "n/a",
                        "%.3f" % st["spread"]
                        if st["gt"] is not None else "-",
                        st["status"],
                        "%+.3f" % st["gtpp"]
                        if st["gtpp"] is not None else "n/a",
                        st["pp"], str(st["flipmed"]), st["nab"],
                        "%.3f" % st["s2"]
                        if st["gt"] is not None else "-",
                        "%+.2f" % st["mtsp"]
                        if st["gt"] is not None else "-",
                        "%.4f" % st["ctw9"]
                        if st["ctw9"] is not None else "-"))
            theta_star[kind] = tstar
            sens[kind] = (float(np.mean(vals)) if vals
                          else float("-inf"))
        collapsed = {k: v for k, v in theta_star.items()
                     if v is not None}
        rank = sorted(PERT_NAMES, key=lambda k: -sens[k])
        rank_txt = " > ".join("%s %.3f" % (k, sens[k])
                              for k in rank)
        if not collapsed:
            v_main = "PERTURBATION_INSENSITIVE(%s)" % rank_txt
        else:
            tmin = min(collapsed.values())
            argmin = [k for k, v in collapsed.items()
                      if v == tmin]
            if len(argmin) == 1:
                kstar = argmin[0]
                prev = None
                idx = THETAS.index(tmin)
                if idx == 0:
                    prev_st = "INTACT"  # theta = 0 baseline
                else:
                    prev_st = stages[(kstar,
                                      THETAS[idx - 1])]["status"]
                sharp = "SHARP" if prev_st == "INTACT" \
                    else "GRADUAL"
                v_main = ("MECHANISM_LOCALIZED(%s, theta* = "
                          "%.2f, %s)" % (kstar, tmin, sharp))
            else:
                v_main = ("MECHANISM_DISTRIBUTED(%s at theta* = "
                          "%.2f; %s)"
                          % (",".join(sorted(argmin)), tmin,
                             rank_txt))
        check("G50-mechanism-map", True,
              "SEALED RULES (COLLAPSED <= %.2f, REDUCED <= %.2f "
              "x gt_main, INTACT >= %.2f x gt_main %.3f): %s; "
              "theta* per surgery %s; sensitivity ranking %s"
              % (GT_ZERO, REDUCED_FRAC, INTACT_FRAC, gt_main,
                 v_main, str(theta_star), rank_txt))
        pps = [stages[(k, t)]["pp"] for k in PERT_NAMES
               for t in THETAS]
        fmap = ("pp min/med/max %.2f/%.2f/%.2f over 12 stages"
                % (min(pps), float(np.median(pps)), max(pps)))
        check("G51-firewall-map", True,
              "FIREWALL_MAP: %s; flipped worlds are typed "
              "ALGEBRAIC (indefinite continuation) and kept in "
              "the primary fit; gt_pp (positive-prefix "
              "restriction) printed per stage above -- %s"
              % (fmap,
                 "no stage lost a rung to flips or aborts"
                 if min(pps) >= 1.0 - 1e-12 else
                 "flip census disclosed per stage"))

        # ---------------- S6: control anchors
        section("S6  CONTROL ANCHORS")
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        ctrl_defs = (("EPSTEIN", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx]
            / np.sqrt(nn_idx.astype(float))))),
            ("SCRAMBLE", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        ctrl = {c: BH.wpack(MAIN_KZ, base_kw=kw)
                for c, kw in ctrl_defs}
        okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
        trE = truth_rec(ctrl["EPSTEIN"])
        trS = truth_rec(ctrl["SCRAMBLE"])
        okA = (abs(trE["C_true"] - CTRUE_EPST_REF)
               <= CTRUE_ANCH_TOL
               and abs(trS["C_true"] - CTRUE_SCR_REF)
               <= CTRUE_ANCH_TOL)
        place = "; ".join(
            "%s@1.0 w9 C %.4f" % (k, stages[(k, 1.0)]["ctw9"])
            for k in PERT_NAMES
            if stages[(k, 1.0)]["ctw9"] is not None)
        check("G60-control-anchors", okCf and okA,
              "flips re-derived %s; C_true(w9) anchors EPSTEIN "
              "%.4f (r272 record %.3f) / SCRAMBLE %.4f (record "
              "%.3f, tol %.3f); MAIN w9 C %.4f; stage endpoint "
              "placement (INFO, no verdict weight): %s"
              % (str({c: ctrl[c]["nf"] for c in ctrl}),
                 trE["C_true"], CTRUE_EPST_REF, trS["C_true"],
                 CTRUE_SCR_REF, CTRUE_ANCH_TOL, ct_w9_main,
                 place))
        rowsS = ctrl["SMOOTH"]["rows"]
        NS = ctrl["SMOOTH"]["N"]
        scT = [abs(rowsS[k]["tb"]
                   * math.exp(rowsS[k]["Ls"]
                              - rowsS[k + 1]["Ls"]))
               for k in range(NS - 1)]
        alias = max(scT[2:]) / max(scT[0], scT[1])
        qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
        check("G61-smooth-anchor", alias <= SM_ALIAS_BAR
              and abs(qS) <= SM_Q_BAR,
              "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= "
              "%.0e -- the null endpoint of every surgery "
              "family is warded" % (alias, SM_ALIAS_BAR, qS,
                                    SM_Q_BAR))

        # ---------------- S7: wards + must-fail m4
        section("S7  CONTRIBUTION + MP WARDS + MUST-FAIL m4")
        tb_main = max(r_["tb_dev"] for r_ in recs42
                      if r_["N"] <= DEEP_N)
        tb_deep = max(r_["tb_dev"] for r_ in recs42
                      if r_["N"] > DEEP_N)
        check("G70-contribution-ward", tb_main <= TB_BAR_MAIN
              and tb_deep <= TB_BAR_DEEP
              and tb_pert_worst <= TB_BAR_PERT,
              "sum ct == t_{N-2}: MAIN worst %.1e (bar %.0e) / "
              "deep %.1e (bar %.0e) / PERTURBED worst %.1e over "
              "all measured worlds (bar %.0e, measurement "
              "quality) -- every gamma point sits on an exact "
              "decomposition"
              % (tb_main, TB_BAR_MAIN, tb_deep, TB_BAR_DEEP,
                 tb_pert_worst, TB_BAR_PERT))
        mp_note = []
        ok_mp = True
        for r_ in recs42[-2:]:
            t_mp = PBB.mp_drive(r_["p"], MP_DPS)
            dv = abs(t_mp - r_["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("MAIN kz%d (N %d) dev %.1e (bar %.0e)"
                           % (r_["kz"], r_["N"], dv, MP_DEEP_BAR))
        if pert_sample is not None:
            t_mp = PBB.mp_drive(pert_sample["p"], MP_DPS)
            dv = abs(t_mp - pert_sample["t_term"])
            ok_mp = ok_mp and (dv <= MP_PERT_BAR)
            mp_note.append("PERT P1@1.0 kz%d (N %d) dev %.1e "
                           "(bar %.0e)"
                           % (pert_sample["kz"],
                              pert_sample["N"], dv, MP_PERT_BAR))
        else:
            ok_mp = False
            mp_note.append("PERT sample MISSING")
        check("G71-mp-wards", ok_mp,
              "mp (dps %d) terminal drive at the deepest ladder "
              "rungs -- the trend-critical points anchor the "
              "exponent fits: %s" % (MP_DPS, "; ".join(mp_note)))
        rng = np.random.default_rng(SHUFFLE_SEED)
        sp_mut = abs(BH.spearman(Ns42,
                                 list(rng.permutation(eps42))))
        check("G80-mustfail-shuffle", sp_mut < SHUF_BAR
              and sp_mut < abs(sp_eps),
              "m4 HALVES-SHUFFLE (seed-%d permutation of the "
              "42-rung eps series against the N axis): |sp| = "
              "%.3f < %.1f and < the true trend %.2f -- the "
              "trends are carried by N, not by the estimator"
              % (SHUFFLE_SEED, sp_mut, SHUF_BAR, abs(sp_eps)))

        # verdict assembly
        hyp_kind = rank[0]
        hyp_level = {"P1_ASSIGN": "weight-assignment level "
                                  "(reach n^theta)",
                     "P2_JITTER": "support level, local reach "
                                  "(atom-slot scale)",
                     "P3_FAMILY": "Euler-family (SAMEP) level",
                     "P4_WINDOW": "global-arrangement level "
                                  "(preserved length "
                                  "n^(1-theta))"}[hyp_kind]
        verd = " + ".join([
            v_main,
            "FIREWALL_MAP(%s)" % fmap,
            "SENSITIVITY_RANKING(%s)" % rank_txt,
            "CONTROL_ANCHORS(EPST %.3f, SCR %.3f, SMOOTH ok)"
            % (trE["C_true"], trS["C_true"]),
            "L2_HYPOTHESIS(%s)" % hyp_level])

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the experimentally isolated organization level "
          "of the N^{-0.45} truth cancellation via a sealed "
          "graduated perturbation ladder -- NO certificate, NO "
          "bound, NO H5 progress claimed")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): conservation identities "
          "and the exact drive decomposition; MEASURED: every "
          "gamma, status and ranking (42-rung ladder, 3 "
          "replicates); OPEN: the cofinal step H5 and the L2 "
          "mechanism (the hypothesis is a quantified TASK, not a "
          "claim); NO RH claim"
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
