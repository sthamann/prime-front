#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""budget_localization_probe -- PRIME.PORT.WALL.
BUDGET_LOCALIZATION.01 (round 280): the LOCALIZATION ANATOMY of
the fixed crossing budget and the EXTREMALITY question.  r279
proved the crossing-budget theorem #(h_n < 0) = S_- world-blindly
(Jacobi/Sylvester) and left the precise sorry: min C := min{n :
h_n < 0} >= N_w = ceil(S/2) -- the localization of the fixed
budget into the upper half of the continuation (measured offsets
min C - N_w: +0 on w9/kz52 EXTREMAL, +1 on kz15, +2 on w13).
v956 fixed the frame: N_w is the free-moment-window maximum
(half-filling law), the r228 offsets 0/2/2/3/1 are forced-coupling
survival counts, and the complement duality h_{S-m}(mutilde)
h_{m-1}(mutilde#) = 1 with dual weights w#_j = 1/(w_j L'(x_j)^2)
is exact.  r276 measured the dose-response continuum of the
survival depth, r278 the exact gradients d log h_n / du_j
(bottom-loaded u-profile).  REVIEWER FRAME (the dam): the budget
S_- is FIXED; the prime geometry does not PREVENT the negativity
-- it HOLDS IT BACK until beyond half-filling.  This round: the
full localization census, the extremality/variational question,
the duality lens, and the moment-perturbation range.  NOT a proof
round: no certificate, no bound mechanism, no localization claim
from any census.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r279 discipline): w = window (kz),
N_w = builder depth = ceil(S/2), S = #union support atoms of
mutilde = mu - nu, n = chain degree, j = atom index, min C =
first n with h_n < 0 (the budget's first spend), offset =
min C - N_w; ground truth (v956/r279 record offsets, control
flips, r276 depth records) enters GATES and census tables only;
no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r278 MS.{ctx_build, grad_chain, tent_dw,
pred_dlg, pert_rows}, r276 MF.{local_gaps, pert_jit}, r274
WD.stj_gen, r279 OT.{p_eval, chain_coef_polys} + r279 toy
conventions, r230 JF toy nodes, v881 PIK, r243 PB.smooth_comb,
r244 BH.{wpack, bord_chain, spearman}, paircorr PC.{Grid,
gen_model} (HL2 surrogate), v563 core (READ-ONLY).

LEG A -- THE FULL LOCALIZATION CENSUS (a1/a2): min C - N_w on
ALL 42 rungs of the frame-A cofinal ladder (h <= 900; the mains
w9/w13 are ladder members, flagged): per rung the sealed source
channel (MS.ctx_build -> folded union arrays) and the scaled f64
union sign chain to N_w + 8 (escalation to N_w + 32 if no
crossing found, disclosed); HALF-FILLING GATE N_w == (S+1)//2 on
every rung; IDENTITY WARD: the union chain reproduces the
BH.bord_chain sign rows and nf on w9 bitwise at sign level; MP
ARBITRATION (dps 40, recount at dps 80 if the mp margin guard
fires): the sealed ward set {w9, w13, kz15, kz52} plus the
census argmax-offset rung plus the census min-margin rung plus
every rung whose f64 relative margin at any degree <= min C + 2
falls below 1e-6 -- exact sign agreement demanded at all degrees
N_w - 2 .. min C + 2.  SEALED ANCHORS (hard): offsets 0/2/2/3/1
on kz 9/12/13/26/40 (v956), +1 on kz15, +0 on kz52 (r279).
STATISTICS: offset distribution, max, spearman(offset, N) (the
"does the offset grow with N" question), MAIN O(1) census.
CONTROLS (a2): EPSTEIN/SCRAMBLE(seed 1)/SMOOTH on w9 -- min C =
flips 25/21/27, min C / N_w = the v956 control scale 0.11..0.15.
DOSE LINK (a2): min C == nf is DEFINITIONAL (gated); the r276
dose curve in budget language is therefore min C(theta)/N_w =
the r276 survival depth s: the P2_JIT w9 stages theta = 0.02 /
0.10 are REBUILT with the exact r276 seeds (MF.pert_jit, seed =
276000 + 1*100000 + di*10000 + rep*1000 + 0, 3 replicates) and
the medians must reproduce the r276 records 0.250 / 0.207
(tolerance 6e-3, printed rounding).

LEG B -- THE EXTREMALITY / VARIATIONAL QUESTION (the core): on
w9 min C = N_w exactly (budget localization at the theoretical
free-window maximum).  Worlds w9 / kz15 / w13 (offsets +0/+1/+2):
(b0) EXTENDED GRADIENT PACK: MS.grad_chain run to N_w + 8 gives
  the exact one-sided a.e. gradients d log|h_n| / du_j PAST the
  wall (Hellmann-Feynman is sign-blind: d log|h_n|/du_j =
  [sum_l wdot_l(j) q_n(x_l)^2]/eta_n holds for eta_n < 0 too);
  FD GATES: central kink-guarded finite differences through the
  FULL pipeline at the hottest and the median off-node atom,
  degrees min C - 1 and min C (sign-equal branches), raw bar
  2e-3 (r278 raw bar; no mp escalation ladder this round,
  disclosed).
(b1) FIRST-ORDER DIRECTION CENSUS (w9): directions xi
  (|xi|_inf <= 1, du = theta g xi, g = r276 local gaps): 200
  pinned random (seed 280001), all +-140 atom singles, and the
  sealed structured directions OPT (per-atom side-selected
  steepest raise of h_{min C}), OPT_SAFE (OPT restricted to
  atoms that do NOT lower h_{min C - 1}), SMALLPRIME (OPT
  restricted to hull position u/(2 alpha) <= 0.3, the r278
  bottom-loading).  Per direction the exact first-order zero
  doses: theta_up = -1/c_{min C} (c_n = <grad log h_n, du>,
  side-selected; h_{min C} < 0 reaches 0 iff c < 0) and
  theta_kill = min over n < min C with c_n < 0 of -1/c_n.  A
  direction RAISES min C at first order iff theta_up <
  theta_kill.  CRITICALITY STATISTICS: rho_crit = L1(min C) /
  median L1(min C - 10 .. min C - 1) (gap-weighted gradient
  norms) and the gap-weighted cosine cos_w(grad h_{min C},
  grad h_{min C - 1}).
(b2) EXACT VERIFICATION: the structured directions + the top-3
  random candidates (ranked by theta_kill - theta_up among
  raisers, else by theta_up ascending) are REBUILT nonlinearly
  (comb -> build_rung -> fold -> union chain to N_w + 8) at
  doses (0.5, 1, 2) x min(theta_up, 0.05) plus the fixed dose
  0.005; measured min C per world; ANY rebuilt world with
  min C > min C(base) is mp-verified (dps 40) before it counts.
  kz15/w13: the same census + verification (are the offset
  windows below a nearby maximum?), plus the forced-tail
  margins (relative h margins at degrees N_w .. min C - 1).
(b3) VARIATIONAL HYPOTHESIS (typed TASK_FORMULATION_ONLY): if
  no direction raises: "the exact comb is a local maximum of
  the localization functional min C under gap-scaled position
  deformations (|du_j| <= theta g_j, theta <= 0.05)" --
  falsifiable; if raisers verify: the hypothesis is REFUTED and
  the raising directions are the finding.
SEALED TYPING: MAIN_NOT_MAXIMAL iff >= 1 mp-confirmed rebuilt
w9 world has min C > 184; MAIN_LOCALLY_MAXIMAL iff ZERO
first-order raisers exist in the full census AND no rebuilt
world raises; MAIN_MAXIMALITY_UNRESOLVED otherwise (first-order
candidates exist but none verifies).  CRITICALITY_STRUCTURED
iff rho_crit <= 0.1 OR cos_w <= -0.5; else
CRITICALITY_UNSTRUCTURED.

LEG C -- THE DUALITY LENS (v956 complement duality): dual
weights w#_j = 1/(w_j L'(x_j)^2), L'(x_j) = prod_{k != j}
(x_j - x_k).
(c1) EXACT TRANSLATION (toys, rationals): h_{S-m}(mutilde)
  h#_{m-1} == 1 for m = 1..S-1 AND the sign mirror
  sign h#_k == sign h_{S-1-k} for k = 0..S-2 on JF9 + MAINLIKE
  + FLIPLIKE; hence EXACTLY: min C >= N_w  <=>  max{k : h#_k <
  0} <= S - 1 - N_w (= N_w - 2 on the real windows) -- the
  localization statement IS the confinement of ALL S_- dual
  negative pivots to the LOWER half of the dual chain.  REAL
  GATE (w9, mp dps 40 full chain to S-1): the dual sign chain
  derived from the mirrored beta reversal equals the mirrored
  primal sign chain at every degree; budget == S_-; sign
  (sum w#) == sign h_{S-1} (the m = 1 instance, measured
  cross-check); translation booleans equal.
(c2) DUAL MAGNITUDE LANDSCAPE (w9, f64 logs): log10|w#_j| vs
  log10|w_j| and hull position; dual negative-mass fraction
  |w#-|/(|w#+| + |w#-|); concentration (gini, top-5 percent
  mass); position shift of the dual top-5 percent vs the primal
  top-5 percent.  SEALED TYPING: DUAL_MECHANISM_HINT iff the
  dual negative-mass fraction <= 1e-3 OR (top-5 percent |w#|
  mass >= 0.99 AND |median hull position shift| >= 0.3); else
  DUAL_RESTATEMENT (the translation is exact sign bookkeeping;
  same atom signature, different magnitudes -- honest).

LEG D -- THE MOMENT VIEW: min C >= N_w <=> D_1..D_{N_w} > 0
(Hankel principal minors; D_n = prod_{k<n} h_k gated exactly on
the toys, n <= 5, Fraction determinants).
(d1) WEYL PERTURBATION RANGE (w9, mp): the natural centered
  split is mutilde = mu - nu with BOTH parts positive; Weyl's
  bound guarantees D_n > 0 while lam_max(H_n(nu)) <
  lam_min(H_n(mu)).  Measured on the sealed degree grid (1..8,
  10, 12, 16, 20, 24, 32; dps = 60 + 8 n) with exact scan
  refinement at the first failing bracket: X_weyl = last n with
  the bound holding; the bound must genuinely FAIL at X_weyl+1
  while the chain shows D_n > 0 far beyond (the rest is the
  actual core -- honest).  CANCELLATION-DEPTH CENSUS (mp dps
  60): r_k = |m_k(mutilde)| / (|m_k(mu)| + |m_k(nu)|), k =
  0..40 -- the moment-coordinate rest zone of the r248 kind, on
  MAIN vs the controls.
(d2) THE PAIRCORR DETECTOR on every candidate argument: the
  battery = EPSTEIN / SCRAMBLE / SMOOTH + one HL2
  pair-correlation-faithful surrogate comb (PC.gen_model, seed
  101, its flip measured); a candidate argument is typed
  MAIN_SEPARATING iff its statistic separates MAIN from ALL
  dead worlds by the sealed factor 2 (Weyl: X_MAIN >= 2 max
  X_dead; rest zone: MAIN median r_{k<=12} <= 0.5 x min dead
  median), else WORLD_BLIND -- a WORLD_BLIND argument cannot
  carry the localization.

WARDS / MUST-FAILS (each loud): identity ward (union chain ==
BH.wpack sign rows + nf on w9); half-filling gate all rungs;
anchors; determinism run1/run2; (m1) DUAL WEIGHTS WITHOUT L'^2
(w#_j := 1/w_j) break the complement product exactly (toy,
rationals); (m2) OFF-BY-ONE TRANSLATION (max neg dual pivot <=
S - N_w instead of S - 1 - N_w) misadjudicates on a constructed
toy with min C == N_w - 1 (sealed deterministic search over the
disclosed weight list); (m3) WEYL OVERREACH (asserting the bound
at X_weyl + 1) must FAIL; (m4) GIFT DIRECTION (a direction
oriented by the withheld census offsets) must be FLAGGED by the
AST scope audit; scope audits (the constructors consume comb/
chain/grid data ONLY); fragment audit (no fit primitives).
STOP LIST (anti-gates, binding): no derived 5/7, no bound
mechanism claim, no asymptotic law, no localization claim from
the census, NO RH claim; r243..r279 stand.

SEALED CONSTANTS: LADDER frame-A h <= 900 (42 rungs); MAINS
(9, 13); EXT 8 / EXT2 32; MARGIN_GUARD 1e-6; MP_DPS 40 /
MP_RECOUNT 80 / MP_GUARD 1e-30; WARD_SET {9, 13, 15, 52};
ANCHORS {9:+0, 12:+2, 13:+2, 26:+3, 40:+1, 15:+1, 52:+0};
CTRL_FLIPS 25/21/27; DOSE_THETAS (0.02, 0.10), REPS 3, r276
seed formula verbatim, R276_MED {0.02: 0.250, 0.10: 0.207},
DOSE_TOL 6e-3; LEGB worlds (9, 15, 13); NDIR 200, DIR_SEED
280001; DOSE_CAP 0.05, VER_FACTORS (0.5, 1, 2), FIXED_DOSE
0.005, NVER_RANDOM 3; SMALLPRIME hull cut 0.3; CRIT_RHO 0.1,
COS_OPP -0.5, CRIT_BAND 10; FD: 2 atoms x 2 degrees per world,
steps (1e-5, 1e-6) kink-guarded 0.25, raw bar 2e-3, floor 1e-4;
DUAL_NEGMASS 1e-3, DUAL_CONC 0.99, TOP_FRAC 0.05, POS_SHIFT
0.3; WEYL_GRID (1,2,3,4,5,6,7,8,10,12,16,20,24,32), WEYL_DPS
60 + 8 n, CTRL_WEYL_MAX 12; K_CANC 40, CANC_DPS 60, REST_K 12;
DETECTOR factor 2.0; HL2 seed 101; TOY M2 weight list = the 15
disclosed variants (6 MAINLIKE sign flips + 6 MAINLIKE x5
scalings + 3 FLIPLIKE w_i := -1 at i in {2, 4, 5}); LOUD
1e3; runtime <= 1800 s; smoke = toys + m1/m2/m4 + scopes + w9
f64 census sanity (ladder, mp, legs B/C-real/D, controls,
verdict adjudication skipped).  PRE-SPEC SCOPING (disclosed):
one machinery pass on w9 + the toys only (chain cost, gradient
extension past the wall runs, mp cost estimate); no bar, band
or verdict rule was tuned after it; the ladder, kz15/w13/kz52,
controls and all doses were UNTOUCHED pre-spec.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  LOCALIZATION_CENSUS(offset stats; anchors; sp(offset, N);
    dose link) [always, measurement]
  + [exactly one of] MAIN_NOT_MAXIMAL(mp-confirmed raising
    worlds) / MAIN_LOCALLY_MAXIMAL(zero first-order raisers AND
    zero verified raisers; within the tested direction classes)
    / MAIN_MAXIMALITY_UNRESOLVED(first-order candidates exist,
    none verified)
  + CRITICALITY_STRUCTURED(rho_crit or cosine) /
    CRITICALITY_UNSTRUCTURED
  + DUAL_TRANSLATION_EXACT + DUAL_MECHANISM_HINT /
    DUAL_RESTATEMENT
  + MOMENT_PERTURBATION_RANGE(X_weyl; rest-zone census;
    detector typing per argument).
Honesty before beauty: the census is measurement, never a
localization proof; local maximality is only ever asserted
WITHIN the tested direction classes and doses; the Weyl range
is expected to die far before N_w -- the remainder is the open
core; no verdict claims a derived 5/7, a bound mechanism or an
asymptotic law; the MAIN positivity (H5) stays the open center.

RECORD TABLES (frozen from the record run; calibration
protocol, chronology honest: smoke pass 1 = 29/29 at first
evaluation (0.2 s); calibration pass 1 = first full evaluation
= 27/29, wall 84.6 s -- TWO disclosed amendments, no bar, band,
class or verdict rule moved: (a1) the FD gate was extended from
the single-step raw difference to the sealed two-step
Richardson with an mp (dps 40) escalation path (the r278-a1
protocol; the pass-1 single-step dev 4.2e-3 is the f64
curvature/rounding pollution r278 measured; Richardson dev
2.9e-5, 0 escalations needed); (a2) the w9 dual mirror slice
had an off-by-one bug (sgm[S-2::-1] reads h_{S-2-k}; the
toy-exact convention is sign h#_k = sign h_{S-1-k}) -- a bug
fix against the exact toy gate, no rule moved; (a3, wording
only) the G32/G34 detail strings were aligned with the measured
typing (anti-alignment reading; offset-window maximality typed
UNRESOLVED at the tested doses).  Pass 2 with a1-a3 = 29/29,
wall 88.4 s = the record run; run1/run2 identical up to WALL):
CAL_VERDICT = LOCALIZATION_CENSUS + MAIN_NOT_MAXIMAL +
CRITICALITY_STRUCTURED + DUAL_TRANSLATION_EXACT +
DUAL_RESTATEMENT + MOMENT_PERTURBATION_RANGE(X_weyl = 2;
detector WORLD_BLIND x2).
Key numbers.  TOYS (exact rationals): complement product
h_{S-m} h#_{m-1} == 1 at ALL m on JF9/MAINLIKE/FLIPLIKE; sign
mirror sign h#_k == sign h_{S-1-k} exact; translation exact
(minC/N_w/maxNegDual: JF9 3/5/5, MAINLIKE 4/3/1, FLIPLIKE
2/3/3); D_n == prod h_k exact (n <= 5).  CENSUS (42 rungs, f64
union chains to N_w + 8, 0 escalations to +32): HALF-FILLING
N_w == (S+1)//2 on 42/42; ANCHORS EXACT (kz 9/12/13/26/40 =
+0/+2/+2/+3/+1, kz15 +1, kz52 +0); OFFSET DISTRIBUTION
{+0: 18, +1: 10, +2: 6, +3: 6, +4: 1, +5: 1}, max +5 (kz43,
N_w = 839; +4 kz50), sp(offset, N) = +0.096 over N in
[142, 878] -- the offset stays O(1) with NO N-growth trend in
this census; mp arbitration dps 40: ward set {9, 13, 15, 52} +
argmax kz43 + min-margin kz48 + 7 margin-guard escalations
(kz 43/44/46/48/64/67/78, worst f64 margin 1.1e-7) -- EXACT
sign agreement everywhere, 0 dps-80 recounts; identity ward w9
bitwise (nf None, min C 184 = N_w + 0, S = 367); CONTROLS
min C = 25/21/27 == flips (0.11..0.15 N_w); DOSE LINK min C ==
nf definitional, r276 P2_JIT medians reproduced EXACTLY (0.250
/ 0.207 at theta 0.02/0.10, exact r276 seeds).  LEG B: FD
worst Richardson dev 2.9e-5 (bar 2e-3, 0 mp escalations);
census w9: 116/200 random + 71/140 single directions raise at
first order; OPT/OPT_SAFE/SMALLPRIME theta_up = 3.87e-5 /
3.91e-5 / 8.18e-5 vs theta_kill 3.2e-2..4.8e-2 (|h_184|
relmarg 1.9e-3 -- the crossing is SHALLOW, the raise dose is
tiny); VERIFICATION (nonlinear rebuilds): OPT at theta 7.75e-5
-> min C 185, OPT_SAFE at 7.81e-5 -> 185, SMALLPRIME at
1.64e-4 -> 185, ALL mp (dps 40) confirmed => the w9 extremal
localization min C = N_w is NOT a local maximum -- position
deformation pushes the first crossing PAST half-filling by one
degree (MAIN_NOT_MAXIMAL; the variational hypothesis b3 is
REFUTED in its local-maximum form); kz15/w13: first-order
raisers exist (53/103 of 200 random) but NONE verifies at the
tested doses (theta_up 5.1e-3 / 1.5e-3 at O(1) crossing
margins, beyond the linear window) -- offset-window maximality
UNRESOLVED; criticality rho_crit = 244.98 (the 1/|h_minC|
inflation), cos_w = -0.971 / -0.956 / -0.978 on w9/kz15/w13 --
the crossing log-gradient is ANTI-ALIGNED with the last free
pivot on all three worlds (the h-sign flip of a raw-gradient
lockstep): CRITICALITY_STRUCTURED by the sealed cosine rule.
LEG C (w9, mp dps 40 full chain to S-1 = 366): budget 104 ==
S_-; sign(sum w#) == sign h_{S-1}; beta-reversal dual sign
chain == mirrored primal at ALL degrees; TRANSLATION EXACT:
max neg dual pivot 182 == S - 1 - min C == the bound S - 1 -
N_w -- w9 SATURATES the dual confinement bound exactly;
landscape: log10|w#| in [211.9, 219.6] vs primal [-7.2, -1.3],
dual negative-mass fraction 0.424, gini 0.79, top-18 mass 0.60,
hull shift 0.198 < 0.3 => DUAL_RESTATEMENT (same signature,
radically different magnitudes, no isolated carrier).  LEG D:
X_weyl = 2 of N_w = 184 (bound fails at n = 3: 1.37e-1 <=
2.77e-1) while D_n > 0 holds through N_w -- the natural mu/nu
Weyl perturbation argument carries 1.1 percent of the way, the
remainder IS the open core; REST ZONE: median r_k (k <= 12)
MAIN 0.94, EPST 0.51, SCR 0.91, SMOOTH 1.00, HL2 0.80 -- NO
deep cancellation in the raw mutilde moments on ANY world (the
r248 quiet zone is a CENTERED BORDER-functional statement, not
a mutilde-moment statement -- honest negative); DETECTOR: Weyl
X = 1/2/6/2 on EPST/SCR/SMOOTH/HL2 (SMOOTH exceeds MAIN!) =>
WORLD_BLIND; rest zone => WORLD_BLIND; HL2 flip 25 (= the
paircorr record).  MUST-FAILS: m1 w# := 1/w breaks the
complement product LOUDLY (exact); m2 variant ML-neg2 (min C =
2 = N_w - 1): the off-by-one mutant MISADJUDICATES loudly; m3
Weyl overreach at n = 3 FAILS as demanded; m4 gift direction
FLAGGED (offs_true); scope audits CLEAN (8 constructors);
fragment audit CLEAN.  Runtime 88.4 s full / 0.2 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

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
import minimal_firewall_probe as MF           # noqa: E402 r276
import metric_stability_probe as MS           # noqa: E402 r278
import oriented_theorem_probe as OT           # noqa: E402 r279
import wronskian_dictionary_probe as WD       # noqa: E402 r274
import jfraction_probe as JF                  # noqa: E402 r230
import paircorr_margin_probe as PC            # noqa: E402 relocation
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

H_CAP = 900
MAINS = (9, 13)
EXT = 8
EXT2 = 32
MARGIN_GUARD = 1e-6
MP_DPS = 40
MP_RECOUNT = 80
MP_GUARD = 1e-30
WARD_SET = (9, 13, 15, 52)
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
DOSE_THETAS = (0.02, 0.10)
REPS = 3
R276_MED = {0.02: 0.250, 0.10: 0.207}
DOSE_TOL = 6e-3
LEGB_KZS = (9, 15, 13)
NDIR = 200
DIR_SEED = 280001
DOSE_CAP = 0.05
VER_FACTORS = (0.5, 1.0, 2.0)
FIXED_DOSE = 0.005
NVER_RANDOM = 3
SP_HULL_CUT = 0.3
CRIT_RHO = 0.1
COS_OPP = -0.5
CRIT_BAND = 10
FD_STEPS = (1e-5, 1e-6)
FD_KINK_GUARD = 0.25
FD_RAW_BAR = 2e-3
FD_FLOOR = 1e-4
DUAL_NEGMASS = 1e-3
DUAL_CONC = 0.99
TOP_FRAC = 0.05
POS_SHIFT = 0.3
WEYL_GRID = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 24, 32)
CTRL_WEYL_MAX = 12
K_CANC = 40
CANC_DPS = 60
REST_K = 12
DET_FACTOR = 2.0
HL2_SEED = 101
LOUD = 1e3

CAL_VERDICT = (
    "LOCALIZATION_CENSUS + MAIN_NOT_MAXIMAL + "
    "CRITICALITY_STRUCTURED + DUAL_TRANSLATION_EXACT + "
    "DUAL_RESTATEMENT + MOMENT_PERTURBATION_RANGE(X_weyl = 2; "
    "detector WORLD_BLIND x2)")

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
    return (not bad), ("NO zero/prime oracles; the census/gradient/"
                       "dual/moment constructors consume comb data, "
                       "chain data and the evaluation grid ONLY; "
                       "record offsets and flips enter gates and "
                       "tables only"
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


BL_FUNCS = ("sign_chain_f64", "mp_sign_chain", "union_of_ctx",
            "grad_ext", "dir_opt", "theta_of_dir", "dual_logw",
            "moments_mp")
BL_FORBIDDEN = {"ANCHORS", "WARD_SET", "CTRL_FLIPS", "R276_MED",
                "offs_true", "minC_true", "leth"}


def scope_audit(funcname):
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
                if nm in BL_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited:
# consume comb/chain/grid data ONLY)
def union_of_ctx(ctx):
    """sorted union atoms/weights of mutilde from a world ctx."""
    xs, ws, _ = PIK.folded_measure(ctx["darm"], ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(ctx["darm"], ctx["L"], -1.0)
    xu = np.concatenate([xs, ys])
    wu = np.concatenate([ws, -vs])
    o = np.argsort(xu)
    return xu[o], wu[o], (xs, ws, ys, vs)


def sign_chain_f64(xu, wu, n_upto):
    """scaled monic Stieltjes chain of the signed union measure:
    (sg int8, lgh, relmarg) for h_0..h_{n_upto}; relmarg =
    |eta| / sum |w| q^2 (the cancellation margin)."""
    q = np.ones_like(xu)
    qm = np.zeros_like(xu)
    Ls = Lsm = 0.0
    aw = np.abs(wu)
    eta = float(np.sum(wu))
    etam = eta
    n_tot = n_upto + 1
    sg = np.zeros(n_tot, dtype=np.int8)
    lgh = np.full(n_tot, np.nan)
    rmg = np.full(n_tot, np.nan)
    habs = float(np.sum(aw))
    sg[0] = 1 if eta > 0 else (-1 if eta < 0 else 0)
    lgh[0] = math.log(abs(eta)) if eta != 0 else np.nan
    rmg[0] = abs(eta) / habs if habs > 0 else np.nan
    for n in range(n_upto):
        alh = float(np.sum(wu * xu * q * q)) / eta
        if n == 0:
            p = (xu - alh) * q
        else:
            ge = (eta / etam) * math.exp(2.0 * (Ls - Lsm))
            fc = math.exp(Lsm - Ls)
            p = (xu - alh) * q - ge * fc * qm
        sc = float(np.max(np.abs(p)))
        if sc == 0.0 or not math.isfinite(sc):
            break
        qm, etam, Lsm = q, eta, Ls
        q = p / sc
        Ls += math.log(sc)
        eta = float(np.sum(wu * q * q))
        habs = float(np.sum(aw * q * q))
        if eta == 0.0 or not math.isfinite(eta):
            break
        sg[n + 1] = 1 if eta > 0 else -1
        lgh[n + 1] = math.log(abs(eta)) + 2.0 * Ls
        rmg[n + 1] = abs(eta) / habs if habs > 0 else np.nan
    return sg, lgh, rmg


def mp_sign_chain(xu, wu, n_upto, dps, guard, recount_dps):
    """mp arbitration chain on the union arrays: int8 signs of
    h_0..h_{n_upto}; margin-guarded degrees recounted at the
    sealed higher dps.  Returns (sg, n_guard, n_recount)."""
    def run(d):
        mp.mp.dps = d
        X = [mp.mpf(float(v)) for v in xu]
        W = [mp.mpf(float(v)) for v in wu]
        A = [abs(w) for w in W]
        q = [mp.mpf(1)] * len(X)
        qm = [mp.mpf(0)] * len(X)
        Ls = Lsm = mp.mpf(0)
        eta = mp.fsum(W)
        etam = eta
        sgv = np.zeros(n_upto + 1, dtype=np.int8)
        sgv[0] = 1 if eta > 0 else (-1 if eta < 0 else 0)
        gd = []
        for n in range(n_upto):
            alh = mp.fsum(w * x * a * a
                          for w, x, a in zip(W, X, q)) / eta
            if n == 0:
                p = [(x - alh) * a for x, a in zip(X, q)]
            else:
                ge = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
                fc = mp.e ** (Lsm - Ls)
                p = [(x - alh) * a - ge * fc * am
                     for x, a, am in zip(X, q, qm)]
            sc = max(abs(v) for v in p)
            qm, etam, Lsm = q, eta, Ls
            q = [v / sc for v in p]
            Ls += mp.log(sc)
            eta = mp.fsum(w * a * a for w, a in zip(W, q))
            hab = mp.fsum(a2 * a * a for a2, a in zip(A, q))
            sgv[n + 1] = 1 if eta > 0 else -1
            if hab != 0 and abs(eta) / hab < guard:
                gd.append(n + 1)
        return sgv, gd
    sgv, gd = run(dps)
    n_rec = 0
    if gd:
        sg2, _g2 = run(recount_dps)
        for n in gd:
            if sgv[n] != sg2[n]:
                n_rec += 1
            sgv[n] = sg2[n]
    return sgv, len(gd), n_rec


def grad_ext(ctx, n_upto):
    """r278 gradient pack EXTENDED past the wall: MS.grad_chain to
    n_upto; d log|h_n|/du_j = [sum_l wdot_l(j) q_n(x_l)^2]/eta_n
    (Hellmann-Feynman, sign-blind).  Returns dict with side pair
    (gR, gL) [n_at x n_run], sg/lgh per degree, gaps."""
    darm = ctx["darm"]
    L = ctx["L"]
    npts = L // 2 + 1
    xe = np.cos(2.0 * math.pi * np.arange(npts) / L)
    xs, ws, _ = PIK.folded_measure(darm, L, +1.0)
    ys, vs, _ = PIK.folded_measure(darm, L, -1.0)
    rows, Q = MS.grad_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                            ctx["by"], ctx["bv"], n_upto, xe)
    n_run = len(rows)
    eta = np.array([r["eta"] for r in rows])
    sg = np.array([r["sg_h"] for r in rows])
    lgh = np.array([r["lg_h"] for r in rows])
    Q = Q[:, :n_run]
    DWr, DWl, dists, Dg, onnode = MS.tent_dw(
        ctx["uu"], ctx["mm"], ctx["alpha"], ctx["M"], L)
    Q2 = Q * Q
    gR = (DWr @ Q2) / eta[None, :]
    gL = (DWl @ Q2) / eta[None, :]
    g = MF.local_gaps(ctx["uu"])
    return dict(gR=gR, gL=gL, sg=sg, lgh=lgh, n_run=n_run,
                gaps=g, dists=dists, Dg=Dg, onnode=onnode)


def dir_opt(gR, gL, g, deg, protect=None, hull=None, hull_cut=None):
    """side-selected steepest-raise direction of |h_deg| -> 0:
    per atom the sign choice minimizing the c_deg contribution;
    protect = degree whose pivot must not be lowered (OPT_SAFE);
    hull/hull_cut restrict to bottom atoms (SMALLPRIME)."""
    n_at = gR.shape[0]
    xi = np.zeros(n_at)
    for j in range(n_at):
        cp = g[j] * gR[j, deg]
        cn = -g[j] * gL[j, deg]
        s = 1.0 if cp <= cn else -1.0
        c = min(cp, cn)
        if c >= 0.0:
            continue
        if protect is not None:
            cprot = g[j] * gR[j, protect] if s > 0 \
                else -g[j] * gL[j, protect]
            if cprot < 0.0:
                continue
        if hull is not None and hull[j] > hull_cut:
            continue
        xi[j] = s
    return xi


def theta_of_dir(gR, gL, g, xi, deg_flip):
    """first-order zero doses along du = theta g xi: theta_up for
    h_{deg_flip} (< 0) and theta_kill = min over the positive
    prefix; c_n = side-selected <grad log h_n, du>."""
    du = g * xi
    c = MS.pred_dlg(gR, gL, du)
    cf = float(c[deg_flip])
    th_up = (-1.0 / cf) if cf < 0.0 else math.inf
    cpre = c[:deg_flip]
    neg = cpre[cpre < 0.0]
    th_kill = float(np.min(-1.0 / neg)) if len(neg) else math.inf
    return th_up, th_kill, c


def dual_logw(xu, wu):
    """dual weights w#_j = 1/(w_j L'(x_j)^2) in log-magnitude +
    sign form (f64 log accumulation, O(S^2))."""
    S_ = len(xu)
    lgLp = np.zeros(S_)
    sgLp = np.ones(S_)
    for j in range(S_):
        d = xu[j] - xu
        d[j] = 1.0
        lgLp[j] = float(np.sum(np.log(np.abs(d))))
        sgLp[j] = 1.0 if int(np.sum(d < 0)) % 2 == 0 else -1.0
    lgw = -(np.log(np.abs(wu)) + 2.0 * lgLp)
    sgw = np.sign(wu)
    return lgw, sgw, lgLp, sgLp


def moments_mp(x, w, K, dps):
    """mp moments m_0..m_K of an atom measure."""
    mp.mp.dps = dps
    X = [mp.mpf(float(v)) for v in x]
    W = [mp.mpf(float(v)) for v in w]
    out = []
    P = [mp.mpf(1)] * len(X)
    for _k in range(K + 1):
        out.append(mp.fsum(w * p for w, p in zip(W, P)))
        P = [p * xx for p, xx in zip(P, X)]
    return out


def hankel_extremes(mvec, n, dps):
    """(lam_min, lam_max) of the n x n Hankel H[i,j] = m_{i+j}."""
    mp.mp.dps = dps
    H = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            H[i, j] = mvec[i + j]
    E, _Q = mp.eigsy(H)
    ev = [E[i] for i in range(n)]
    return min(ev), max(ev)


def mutant_gift_dir(offs_true, gaps):
    """m4 MUST-FAIL MUTANT: a direction oriented by the withheld
    census offsets -- the scope audit must FLAG this."""
    o = np.argsort(np.asarray(offs_true, float))
    return np.asarray(gaps)[o]


# ============== exact toy machinery (Fractions)
def stj_full(nodes, wts):
    S_ = len(nodes)
    al, be, hs = WD.stj_gen(nodes, wts, S_)
    return al, be, hs


def toy_dual_weights(nodes, wts):
    S_ = len(nodes)
    Lp = []
    for j in range(S_):
        pr = Fr(1)
        for k in range(S_):
            if k != j:
                pr *= (nodes[j] - nodes[k])
        Lp.append(pr)
    return [1 / (wts[j] * Lp[j] ** 2) for j in range(S_)], Lp


def frac_det(M):
    """exact determinant via fraction Gaussian elimination with
    row pivoting."""
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            for k in range(c, n):
                A[r][k] -= f * A[c][k]
    return det


def toy_moments(nodes, wts, K):
    out = []
    P = [Fr(1)] * len(nodes)
    for _k in range(K + 1):
        out.append(sum(w * p for w, p in zip(wts, P)))
        P = [p * x for p, x in zip(P, nodes)]
    return out


TOYS_XS = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
           Fr(5, 4)]
MAINLIKE_W = [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
              Fr(1, 3)]
FLIPLIKE_W = [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
              Fr(1, 3)]
# m2 search list: 12 sealed MAINLIKE sign/scale variants +
# (amendment a1, disclosed) 3 FLIPLIKE-scale variants
M2_VARIANTS = tuple(
    [("ML-neg%d" % j,
      [(-w if i == j else w) for i, w in enumerate(MAINLIKE_W)])
     for j in range(6)]
    + [("ML-x5@%d" % j,
        [(5 * w if i == j else w) for i, w in enumerate(MAINLIKE_W)])
       for j in range(6)]
    + [("FL-neg%d" % j,
        [(Fr(-1) if i == j else w)
         for i, w in enumerate(FLIPLIKE_W)])
       for j in (2, 4, 5)])


def toy_minC(hs, S_):
    return next((k for k in range(S_) if hs[k] < 0), None)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("budget_localization_probe -- PRIME.PORT.WALL."
          "BUDGET_LOCALIZATION.01 (round 280)")
    print("SPEC_SHA %s   (r278 MS %s / r279 OT %s)"
          % (SPEC_SHA[:16], MS.SPEC_SHA[:16], OT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + m1/m2/m4 + scopes + w9 f64 "
                        "census sanity; ladder, mp, legs B/C-real/D "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: census anchors (v956 offsets "
          "0/2/2/3/1 + kz15 +1 + kz52 +0), mp arbitration protocol, "
          "the direction classes + raising criterion theta_up < "
          "theta_kill, verification doses, the maximality/"
          "criticality/dual/detector typing rules and the verdict "
          "form; pre-spec scoping disclosed in the spec (w9 + toys "
          "machinery pass only)")

    # ---------------- S1 toys (exact rationals)
    section("S1  TOYS -- COMPLEMENT DUALITY + TRANSLATION + MINORS")
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    toys = [("JF9", [t[0] for t in jf_pairs],
             [t[1] for t in jf_pairs]),
            ("MAINLIKE", TOYS_XS, MAINLIKE_W),
            ("FLIPLIKE", TOYS_XS, FLIPLIKE_W)]
    ok_prod = True
    ok_mirror = True
    ok_trans = True
    ok_sgw = True
    ok_det = True
    toy_tab = {}
    for name, nodes, wts in toys:
        S_t = len(nodes)
        al_t, be_t, hs_t = stj_full(nodes, wts)
        dw, Lp = toy_dual_weights(nodes, wts)
        alD, beD, hsD = WD.stj_gen(nodes, dw, S_t - 1)
        # complement product h_{S-m} h#_{m-1} == 1
        for m_ in range(1, S_t):
            ok_prod = ok_prod and (hs_t[S_t - m_]
                                   * hsD[m_ - 1] == 1)
        # sign mirror
        for k in range(S_t - 1):
            ok_mirror = ok_mirror and (
                (hsD[k] > 0) == (hs_t[S_t - 1 - k] > 0))
        # dual weight signs
        ok_sgw = ok_sgw and all(
            (dw[j] > 0) == (wts[j] > 0) for j in range(S_t))
        # translation: minC >= Nw <=> max neg dual pivot <= S-1-Nw
        Nw_t = (S_t + 1) // 2
        mc = toy_minC(hs_t, S_t)
        negD = [k for k in range(S_t - 1) if hsD[k] < 0]
        maxKD = max(negD) if negD else -1
        lhs = (mc is None) or (mc >= Nw_t)
        rhs = maxKD <= S_t - 1 - Nw_t
        ok_trans = ok_trans and (lhs == rhs) and (
            (mc is None and maxKD == -1)
            or (mc is not None and maxKD == S_t - 1 - mc))
        # Hankel minors D_n == prod h_k (n <= 5)
        mom = toy_moments(nodes, wts, 2 * min(5, S_t - 1))
        for n in range(1, min(5, S_t - 1) + 1):
            H = [[mom[i + j] for j in range(n)] for i in range(n)]
            pr = Fr(1)
            for k in range(n):
                pr *= hs_t[k]
            ok_det = ok_det and (frac_det(H) == pr)
        toy_tab[name] = (mc, Nw_t, maxKD, S_t)
        info("%s: S=%d N_w=%d minC=%s maxNegDual=%d "
             "(S-1-minC=%s)"
             % (name, S_t, Nw_t, str(mc), maxKD,
                str(None if mc is None else S_t - 1 - mc)))
    check("G10-toy-complement-product", ok_prod and ok_sgw,
          "EXACT (rationals): h_{S-m}(mutilde) h#_{m-1}(mutilde#) "
          "== 1 for ALL m = 1..S-1 on JF9 + MAINLIKE + FLIPLIKE "
          "with dual weights w# = 1/(w L'^2); sign(w#) == sign(w) "
          "everywhere (L'^2 > 0) -- the v956 complement duality "
          "re-derived exactly")
    check("G11-toy-sign-mirror-translation", ok_mirror and ok_trans,
          "EXACT: sign h#_k == sign h_{S-1-k} at every k, hence "
          "max neg dual pivot == S - 1 - min C and the "
          "TRANSLATION min C >= N_w <=> all dual negative pivots "
          "confined to k <= S - 1 - N_w (the LOWER dual half) -- "
          "the localization statement translated exactly: %s"
          % str(toy_tab))
    check("G12-toy-minors", ok_det,
          "EXACT: D_n(mutilde) == prod_{k<n} h_k for n = 1..5 on "
          "all toys (Fraction Hankel determinants) -- min C >= "
          "N_w <=> D_1..D_{N_w} > 0 stands on the minor side")

    # ---------------- S2 census
    section("S2  LEG A -- LOCALIZATION CENSUS (42 RUNGS + CONTROLS)")
    ctx9 = MS.ctx_build(9)
    xu9, wu9, zones9 = union_of_ctx(ctx9)
    S9 = len(xu9)
    N9 = ctx9["N"]
    sg9, lgh9, rmg9 = sign_chain_f64(xu9, wu9, N9 + EXT)
    minC9 = next((n for n in range(len(sg9)) if sg9[n] < 0), None)
    # identity ward vs BH.wpack
    p9 = BH.wpack(9)
    rows9 = p9["nf"]
    ok_id = (rows9 is None
             and bool(np.all(sg9[:N9] > 0))
             and minC9 == N9 + ANCHORS[9])
    check("G20-identity-ward", ok_id,
          "IDENTITY WARD (w9): BH.wpack nf None reproduced; the "
          "union f64 sign chain is positive on rows 0..N-1 and "
          "min C = %s == N_w %d + %d (v956/r279 record); S = %d, "
          "N_w == (S+1)//2: %s"
          % (str(minC9), N9, ANCHORS[9], S9,
             str(N9 == (S9 + 1) // 2)))
    if smoke:
        for g in ("G21-ladder-census", "G22-anchors",
                  "G23-census-stats", "G24-mp-arbitration",
                  "G25-controls-doselink"):
            check(g, True, "SMOKE: skipped")
        cens = {}
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        cens = {}
        ok_hf = True
        for kz in kzs:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            xu, wu, _z = union_of_ctx(ctx)
            S_ = len(xu)
            N_ = ctx["N"]
            ok_hf = ok_hf and (N_ == (S_ + 1) // 2)
            sg, lgh, rmg = sign_chain_f64(xu, wu, N_ + EXT)
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            ext_used = EXT
            if mc is None:
                sg, lgh, rmg = sign_chain_f64(xu, wu, N_ + EXT2)
                mc = next((n for n in range(len(sg))
                           if sg[n] < 0), None)
                ext_used = EXT2
            wmg = float(np.nanmin(rmg[:min(len(rmg),
                                           (mc or N_) + 3)]))
            cens[kz] = dict(N=N_, S=S_, minC=mc,
                            off=None if mc is None else mc - N_,
                            wmarg=wmg, ext=ext_used, xu=xu, wu=wu)
            info("kz%d: N_w=%d S=%d minC=%s off=%s worst-marg="
                 "%.1e" % (kz, N_, S_, str(mc),
                           str(cens[kz]["off"]), wmg))
        ok_all = all(c["minC"] is not None for c in cens.values())
        check("G21-ladder-census", len(cens) == 42 and ok_hf
              and ok_all,
              "42-rung frame-A ladder (h <= %d): union chain to "
              "N_w + %d (escalations to +%d: %d rungs); "
              "HALF-FILLING N_w == (S+1)//2 on 42/42; a first "
              "crossing found on every rung"
              % (H_CAP, EXT, EXT2,
                 sum(1 for c in cens.values() if c["ext"] == EXT2)))
        ok_anch = all(kz in cens
                      and cens[kz]["off"] == ANCHORS[kz]
                      for kz in ANCHORS)
        check("G22-anchors", ok_anch,
              "SEALED ANCHORS EXACT: offsets %s (v956 kz "
              "9/12/13/26/40 = 0/2/2/3/1; r279 kz15 +1, kz52 +0)"
              % str({kz: cens[kz]["off"] for kz in sorted(ANCHORS)
                     if kz in cens}))
        offs_true = [cens[kz]["off"] for kz in sorted(cens)]
        Ns = [cens[kz]["N"] for kz in sorted(cens)]
        dist = {}
        for o in offs_true:
            dist[o] = dist.get(o, 0) + 1
        sp_oN = BH.spearman(offs_true, Ns)
        check("G23-census-stats", True,
              "OFFSET DISTRIBUTION over the 42 rungs: %s (max +%d); "
              "sp(offset, N) = %+.3f over N in [%d, %d] -- MAIN "
              "stays O(1) from the half-filling extremum on every "
              "rung; NO growth trend claimed beyond this census"
              % (str({("+%d" % k): dist[k] for k in sorted(dist)}),
                 max(offs_true), sp_oN, min(Ns), max(Ns)))
        # mp arbitration
        argmax_kz = max(sorted(cens),
                        key=lambda k: cens[k]["off"])
        argmin_kz = min(sorted(cens),
                        key=lambda k: cens[k]["wmarg"])
        esc = [kz for kz in sorted(cens)
               if cens[kz]["wmarg"] < MARGIN_GUARD]
        ward = sorted(set(WARD_SET) | {argmax_kz, argmin_kz}
                      | set(esc))
        ok_mp = True
        n_rec_tot = 0
        for kz in ward:
            c = cens[kz]
            sgm, n_g, n_r = mp_sign_chain(
                c["xu"], c["wu"], c["minC"] + 2, MP_DPS,
                MP_GUARD, MP_RECOUNT)
            n_rec_tot += n_r
            sgf, _l, _r = sign_chain_f64(c["xu"], c["wu"],
                                         c["minC"] + 2)
            lo = max(0, c["N"] - 2)
            ok_mp = ok_mp and bool(
                np.array_equal(sgm[lo:c["minC"] + 3],
                               sgf[lo:c["minC"] + 3]))
        check("G24-mp-arbitration", ok_mp and n_rec_tot == 0,
              "MP ARBITRATION (dps %d): ward set %s (sealed %s + "
              "argmax-offset kz%d + min-margin kz%d + %d margin-"
              "guard escalations) -- EXACT sign agreement at all "
              "degrees N_w-2..min C+2; dps-%d recounts %d"
              % (MP_DPS, str(ward), str(list(WARD_SET)),
                 argmax_kz, argmin_kz, len(esc), MP_RECOUNT,
                 n_rec_tot))
        # controls + dose link
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        cdefs = {"EPST": dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float)))),
            "SCR": dict(scramble_seed=1),
            "SMOOTH": dict(comb=(ug9, uw9))}
        ctl_mc = {}
        for cn, kw in cdefs.items():
            cctx = MS.ctx_build(9, **kw)
            cxu, cwu, _cz = union_of_ctx(cctx)
            csg, _cl, _cr = sign_chain_f64(cxu, cwu,
                                           cctx["N"] + EXT)
            ctl_mc[cn] = next((n for n in range(len(csg))
                               if csg[n] < 0), None)
        ok_ctl = all(ctl_mc[c] == CTRL_FLIPS[c] for c in ctl_mc)
        # r276 dose sample (P2_JIT w9)
        med = {}
        for th in DOSE_THETAS:
            depths = []
            for rep in range(REPS):
                seed = (MS.SEED_R276 + MS.P2_SI * 100000
                        + MS.DOSE_DI[th] * 10000 + rep * 1000
                        + MS.WIN_WI[9] * 10)
                u2, m2 = MF.pert_jit(ctx9["uu"], ctx9["mm"], th,
                                     seed, False)
                _rw, nf2, _z2 = MS.pert_rows(ctx9, u2, m2)
                depths.append((nf2 if nf2 is not None else N9)
                              / float(N9))
            med[th] = float(np.median(depths))
        ok_dose = all(abs(med[th] - R276_MED[th]) <= DOSE_TOL
                      for th in DOSE_THETAS)
        check("G25-controls-doselink", ok_ctl and ok_dose,
              "CONTROLS: min C = %s == flips %s (= 0.11..0.15 "
              "N_w); DOSE LINK: min C == nf DEFINITIONAL (same "
              "first-negative object), the r276 dose curve in "
              "budget language min C(theta)/N_w reproduced with "
              "the exact r276 seeds: medians %s vs records %s -- "
              "the two lanes are ONE coordinate"
              % (str(ctl_mc), str(CTRL_FLIPS),
                 str({t: round(med[t], 3) for t in med}),
                 str(R276_MED)))

    # ---------------- S3 leg B
    section("S3  LEG B -- EXTREMALITY / VARIATIONAL QUESTION")
    if smoke:
        for g in ("G30-grad-ext", "G31-fd-gates",
                  "G32-direction-census", "G33-verification",
                  "G34-offset-windows", "G35-typing"):
            check(g, True, "SMOKE: skipped")
        n_raise_ver = 0
        n_fo_raisers = 0
        crit_struct = False
        rho_crit = float("nan")
        cosw = float("nan")
    else:
        GB = {}
        ok_gext = True
        for kz in LEGB_KZS:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            gp = grad_ext(ctx, ctx["N"] + EXT)
            mc = next((n for n in range(gp["n_run"])
                       if gp["sg"][n] < 0), None)
            GB[kz] = dict(ctx=ctx, gp=gp, minC=mc)
            ok_gext = ok_gext and (mc is not None) and (
                mc == (cens[kz]["minC"] if kz in cens else mc))
            info("kz%d: grad chain n_run=%d minC=%d "
                 "|h_minC| relmarg %.1e"
                 % (kz, gp["n_run"], mc,
                    math.exp(gp["lgh"][mc]
                             - gp["lgh"][mc - 1])))
        check("G30-grad-ext", ok_gext,
              "EXTENDED GRADIENT PACKS (r278 machinery verbatim, "
              "n_upto = N_w + %d): chains run past the wall on "
              "w9/kz15/w13; min C = %s reproduces the census "
              "exactly (sign-blind Hellmann-Feynman columns "
              "available at min C +- 1)"
              % (EXT, str({k: GB[k]["minC"] for k in GB})))
        # FD gates (amendment a1, disclosed: the r278-a1 protocol
        # -- pairs whose f64 Richardson value exceeds the bar are
        # ESCALATED to an mp (dps 40) FD through the actual
        # pipeline and gated there; bar unchanged; the f64 chain
        # rounding error is a smooth function of u and pollutes
        # the f64 FD, exactly as measured in r278)
        def fd_branch(ctx, j, e, deg, use_mp):
            up = ctx["uu"].copy()
            um = ctx["uu"].copy()
            up[j] += e
            um[j] -= e
            out = []
            for u2 in (up, um):
                bb = PIK.build_rung(ctx["kz"],
                                    comb=(u2, ctx["mm"]))
                xu2, wu2, _ = union_of_ctx(
                    dict(darm=np.asarray(bb["d"], float),
                         L=ctx["L"]))
                if use_mp:
                    mp.mp.dps = MP_DPS
                    X = [mp.mpf(float(v)) for v in xu2]
                    W = [mp.mpf(float(v)) for v in wu2]
                    q = [mp.mpf(1)] * len(X)
                    qm = [mp.mpf(0)] * len(X)
                    Ls = Lsm = mp.mpf(0)
                    eta = mp.fsum(W)
                    etam = eta
                    lg = None
                    for n in range(deg):
                        alh = mp.fsum(
                            w * x * a * a
                            for w, x, a in zip(W, X, q)) / eta
                        if n == 0:
                            p = [(x - alh) * a
                                 for x, a in zip(X, q)]
                        else:
                            ge = (eta / etam) \
                                * mp.e ** (2 * (Ls - Lsm))
                            fc = mp.e ** (Lsm - Ls)
                            p = [(x - alh) * a - ge * fc * am
                                 for x, a, am in zip(X, q, qm)]
                        sc = max(abs(v) for v in p)
                        qm, etam, Lsm = q, eta, Ls
                        q = [v / sc for v in p]
                        Ls += mp.log(sc)
                        eta = mp.fsum(w * a * a
                                      for w, a in zip(W, q))
                    lg = float(mp.log(abs(eta)) + 2 * Ls)
                    sgv = 1 if eta > 0 else -1
                    out.append((sgv, lg))
                else:
                    sg_, lg_, _r = sign_chain_f64(xu2, wu2,
                                                  deg + 1)
                    out.append((int(sg_[deg]), float(lg_[deg])))
            (sp_, lp_), (sm_, lm_) = out
            if sp_ == sm_ and sp_ != 0:
                return (lp_ - lm_) / (2.0 * e)
            return None
        ok_fd = True
        worst_fd = 0.0
        worst_mp = 0.0
        n_esc = 0
        for kz in LEGB_KZS:
            ctx, gp, mc = GB[kz]["ctx"], GB[kz]["gp"], GB[kz]["minC"]
            g = gp["gaps"]
            hot = np.abs(gp["gR"][:, mc]) * g
            hot[gp["onnode"]] = -1.0
            j_hot = int(np.argmax(hot))
            offn = np.nonzero(~gp["onnode"])[0]
            j_mid = int(offn[len(offn) // 2])
            for j in (j_hot, j_mid):
                e0 = min(FD_STEPS[0],
                         FD_KINK_GUARD * gp["dists"][j])
                e1 = max(FD_STEPS[1],
                         e0 / 10.0)
                for deg in (mc - 1, mc):
                    pred = gp["gR"][j, deg]
                    f0 = fd_branch(ctx, j, e0, deg, False)
                    f1 = fd_branch(ctx, j, e1, deg, False)
                    if f0 is None or f1 is None:
                        continue
                    r0 = (e0 / e1) ** 2
                    rich = (r0 * f1 - f0) / (r0 - 1.0)
                    dev = abs(rich - pred) / max(abs(pred),
                                                 FD_FLOOR)
                    worst_fd = max(worst_fd, dev)
                    if dev > FD_RAW_BAR:
                        n_esc += 1
                        fmp = fd_branch(ctx, j, e0, deg, True)
                        if fmp is None:
                            ok_fd = False
                            continue
                        dmp = abs(fmp - pred) / max(abs(pred),
                                                    FD_FLOOR)
                        worst_mp = max(worst_mp, dmp)
                        ok_fd = ok_fd and dmp <= FD_RAW_BAR
        check("G31-fd-gates", ok_fd,
              "FD GATES (central, kink-guarded, Richardson from "
              "the two sealed steps, through the FULL pipeline, "
              "sign-equal branches): worst f64 Richardson dev "
              "%.1e; %d pairs escalated to the mp (dps %d) FD "
              "(amendment a1, r278-a1 protocol), worst mp dev "
              "%.1e (bar %.0e) over 2 atoms x degrees (min C - "
              "1, min C) x 3 worlds -- the past-wall gradient "
              "columns are exact a.e. derivatives"
              % (worst_fd, n_esc, MP_DPS, worst_mp, FD_RAW_BAR))
        # b1 direction census per world
        VER = {}
        for kz in LEGB_KZS:
            ctx, gp, mc = GB[kz]["ctx"], GB[kz]["gp"], GB[kz]["minC"]
            gR, gL, g = gp["gR"], gp["gL"], gp["gaps"]
            hull = ctx["uu"] / (2.0 * ctx["alpha"])
            xi_opt = dir_opt(gR, gL, g, mc)
            xi_safe = dir_opt(gR, gL, g, mc, protect=mc - 1)
            xi_sp = dir_opt(gR, gL, g, mc, hull=hull,
                            hull_cut=SP_HULL_CUT)
            rng = np.random.default_rng(DIR_SEED)
            n_at = len(g)
            rand_dirs = [rng.uniform(-1.0, 1.0, n_at)
                         for _ in range(NDIR)]
            cand = [("OPT", xi_opt), ("OPT_SAFE", xi_safe),
                    ("SMALLPRIME", xi_sp)]
            tab = {}
            n_raise_rand = 0
            rand_scored = []
            for name, xi in cand:
                tu, tk, _c = theta_of_dir(gR, gL, g, xi, mc)
                tab[name] = (tu, tk)
            for i, xi in enumerate(rand_dirs):
                tu, tk, _c = theta_of_dir(gR, gL, g, xi, mc)
                if tu < tk:
                    n_raise_rand += 1
                rand_scored.append((tk - tu if tu < tk else -tu,
                                    tu, i, xi))
            n_raise_sing = 0
            for j in range(n_at):
                for s in (1.0, -1.0):
                    xi = np.zeros(n_at)
                    xi[j] = s
                    tu, tk, _c = theta_of_dir(gR, gL, g, xi, mc)
                    if tu < tk:
                        n_raise_sing += 1
            rand_scored.sort(key=lambda t: -t[0])
            L1c = np.sum(np.maximum(np.abs(gR), np.abs(gL))
                         * g[:, None], axis=0)
            band = L1c[max(0, mc - CRIT_BAND):mc]
            rho_c = float(L1c[mc] / np.median(band))
            a = g * gR[:, mc]
            b = g * gR[:, mc - 1]
            cw = float(np.sum(a * b)
                       / (np.linalg.norm(a) * np.linalg.norm(b)))
            GB[kz].update(tab=tab, n_raise_rand=n_raise_rand,
                          n_raise_sing=n_raise_sing,
                          rho_crit=rho_c, cosw=cw)
            info("kz%d: OPT th_up %.2e / kill %.2e; SAFE %.2e/"
                 "%.2e; SP %.2e/%.2e; raisers rand %d/%d singles "
                 "%d/%d; rho_crit %.3f cos_w %+.4f"
                 % (kz, tab["OPT"][0], tab["OPT"][1],
                    tab["OPT_SAFE"][0], tab["OPT_SAFE"][1],
                    tab["SMALLPRIME"][0], tab["SMALLPRIME"][1],
                    n_raise_rand, NDIR, n_raise_sing, 2 * n_at,
                    rho_c, cw))
            # verification worlds
            ver = []
            top_rand = [(("RAND%d" % t[2]), t[3])
                        for t in rand_scored[:NVER_RANDOM]]
            for name, xi in cand + top_rand:
                tu = theta_of_dir(gR, gL, g, xi, mc)[0]
                th0 = min(tu, DOSE_CAP) if math.isfinite(tu) \
                    else DOSE_CAP
                doses = sorted(set(
                    [min(f * th0, DOSE_CAP) for f in VER_FACTORS]
                    + [FIXED_DOSE]))
                for th in doses:
                    u2 = ctx["uu"] + th * g * xi
                    bb = PIK.build_rung(ctx["kz"],
                                        comb=(u2, ctx["mm"]))
                    xu2, wu2, _z = union_of_ctx(
                        dict(darm=np.asarray(bb["d"], float),
                             L=ctx["L"]))
                    sg2, _l2, _r2 = sign_chain_f64(
                        xu2, wu2, ctx["N"] + EXT)
                    mc2 = next((n for n in range(len(sg2))
                                if sg2[n] < 0), None)
                    conf = False
                    if mc2 is not None and mc2 > mc:
                        sgm2, _g2, _r2b = mp_sign_chain(
                            xu2, wu2, mc2 + 2, MP_DPS, MP_GUARD,
                            MP_RECOUNT)
                        mcm = next((n for n in range(len(sgm2))
                                    if sgm2[n] < 0), None)
                        conf = (mcm == mc2)
                    ver.append((name, th, mc2, conf,
                                len(xu2)))
            GB[kz]["ver"] = ver
            VER[kz] = ver
        check("G32-direction-census", True,
              "b1 FIRST-ORDER CENSUS ADJUDICATED (w9): %d/%d "
              "random and %d/%d single directions RAISE at first "
              "order (theta_up < theta_kill); OPT theta_up = "
              "%.2e; criticality rho_crit = %.3f (bar %.1f), "
              "cos_w(grad h_minC, grad h_minC-1) = %+.4f -- the "
              "crossing log-gradient is INFLATED by the shallow "
              "crossing (1/|h_minC|) and ANTI-ALIGNED with the "
              "last free pivot (the h-sign flip of a raw-"
              "gradient lockstep), NOT vanishing"
              % (GB[9]["n_raise_rand"], NDIR,
                 GB[9]["n_raise_sing"], 2 * len(GB[9]["gp"]["gaps"]),
                 GB[9]["tab"]["OPT"][0], GB[9]["rho_crit"],
                 CRIT_RHO, GB[9]["cosw"]))
        raisers9 = [(n, t, m, c) for (n, t, m, c, _s) in VER[9]
                    if m is not None and m > GB[9]["minC"] and c]
        n_raise_ver = len(raisers9)
        n_fo_raisers = (GB[9]["n_raise_rand"]
                        + GB[9]["n_raise_sing"]
                        + sum(1 for nm in GB[9]["tab"]
                              if GB[9]["tab"][nm][0]
                              < GB[9]["tab"][nm][1]))
        check("G33-verification", True,
              "b2 EXACT VERIFICATION ADJUDICATED (w9, nonlinear "
              "rebuilds + mp confirmation of every raiser): "
              "raising worlds %s of %d rebuilt candidates -- %s"
              % (str(raisers9), len(VER[9]),
                 "MAIN localization is NOT a local maximum: "
                 "deformation pushes the first crossing PAST "
                 "half-filling" if raisers9 else
                 "no rebuilt world raised min C at the tested "
                 "doses"))
        off_tab = {}
        for kz in (15, 13):
            mc = GB[kz]["minC"]
            N_ = GB[kz]["ctx"]["N"]
            r_kz = [(n, t, m, c) for (n, t, m, c, _s) in VER[kz]
                    if m is not None and m > mc and c]
            tails = [math.exp(GB[kz]["gp"]["lgh"][n]
                              - GB[kz]["gp"]["lgh"][n - 1])
                     for n in range(N_, mc)]
            off_tab[kz] = (mc - N_, r_kz, tails)
        check("G34-offset-windows", True,
              "b2 OFFSET WINDOWS ADJUDICATED: kz15 (+1) verified "
              "raisers %s; w13 (+2) verified raisers %s (first-"
              "order candidates exist on both, but their theta_up "
              "sits at the O(1) crossing margins beyond the "
              "linear window -- whether the offset windows lie "
              "below a nearby maximum stays UNRESOLVED at the "
              "tested doses); forced-tail h ratios (degrees "
              "N_w..min C - 1): kz15 %s / w13 %s"
              % (str(off_tab[15][1]), str(off_tab[13][1]),
                 str(["%.2e" % v for v in off_tab[15][2]]),
                 str(["%.2e" % v for v in off_tab[13][2]])))
        rho_crit = GB[9]["rho_crit"]
        cosw = GB[9]["cosw"]
        crit_struct = (rho_crit <= CRIT_RHO) or (cosw <= COS_OPP)
        check("G35-typing", True,
              "SEALED TYPING: maximality = %s; criticality = %s "
              "(rho_crit %.3f vs %.1f, cos_w %+.3f vs %+.1f); "
              "variational hypothesis: %s"
              % ("MAIN_NOT_MAXIMAL" if n_raise_ver > 0 else
                 ("MAIN_LOCALLY_MAXIMAL" if n_fo_raisers == 0
                  else "MAIN_MAXIMALITY_UNRESOLVED"),
                 "STRUCTURED" if crit_struct else "UNSTRUCTURED",
                 rho_crit, CRIT_RHO, cosw, COS_OPP,
                 "REFUTED -- the exact comb is NOT a local "
                 "maximum of min C under gap-scaled position "
                 "deformations; the raising directions are the "
                 "finding" if n_raise_ver > 0 else
                 "TASK_FORMULATION_ONLY: the exact comb is a "
                 "local maximum of min C under gap-scaled "
                 "position deformations (theta <= 0.05) -- "
                 "falsifiable"))

    # ---------------- S4 leg C real
    section("S4  LEG C -- DUALITY LENS ON w9")
    if smoke:
        for g in ("G40-w9-translation", "G41-dual-landscape"):
            check(g, True, "SMOKE: skipped")
        dual_hint = False
    else:
        sgm9, n_g9, n_r9 = mp_sign_chain(xu9, wu9, S9 - 1, MP_DPS,
                                         MP_GUARD, MP_RECOUNT)
        Sm9 = int(np.sum(wu9 < 0))
        budget9 = int(np.sum(sgm9 < 0))
        minC9m = next((n for n in range(len(sgm9))
                       if sgm9[n] < 0), None)
        # dual sign chain: sign h#_k = sign h_{S-1-k} (mirror);
        # independent derivation via the beta reversal telescope:
        # sign h#_m = sign(h#_0) sign(h_{S-1}) sign(h_{S-1-m})
        lgw, sgw, lgLp, sgLp = dual_logw(xu9, wu9)
        sh = np.max(lgw)
        sum_wd = float(np.sum(sgw * np.exp(lgw - sh)))
        sg_sum = 1 if sum_wd > 0 else -1
        ok_h0 = (sg_sum == int(sgm9[S9 - 1]))
        # sign h#_k = sign h_{S-1-k}, k = 0..S-2 (amendment a2:
        # calibration pass 1 had an off-by-one slice here --
        # sgm9[S9-2::-1] reads h_{S-2-k}; the toy-exact mirror is
        # h_{S-1-k}; a bug fix, no rule moved)
        sgD_mirror = sgm9[S9 - 1:0:-1]
        sgD_tele = np.array(
            [sg_sum * int(sgm9[S9 - 1]) * int(sgm9[S9 - 1 - m])
             for m in range(S9 - 1)], dtype=np.int8)
        ok_dchain = bool(np.array_equal(sgD_mirror, sgD_tele))
        negD9 = [k for k in range(S9 - 1) if sgD_mirror[k] < 0]
        maxKD9 = max(negD9) if negD9 else -1
        lhs9 = minC9m >= N9
        rhs9 = maxKD9 <= S9 - 1 - N9
        ok_tr9 = (lhs9 == rhs9) and (maxKD9 == S9 - 1 - minC9m)
        check("G40-w9-translation", (budget9 == Sm9) and ok_h0
              and ok_dchain and ok_tr9 and n_r9 == 0,
              "w9 (mp dps %d full chain to S-1 = %d): budget "
              "#(h<0) = %d == S_- %d; sign(sum w#) == sign "
              "h_{S-1} (the m = 1 complement instance, measured); "
              "the beta-reversal dual sign chain == the mirrored "
              "primal chain at ALL degrees; TRANSLATION exact: "
              "max neg dual pivot %d == S - 1 - min C (min C "
              "%d), bound S - 1 - N_w = %d -- min C >= N_w IS "
              "the confinement of all %d dual negatives to the "
              "lower dual half"
              % (MP_DPS, S9 - 1, budget9, Sm9, maxKD9, minC9m,
                 S9 - 1 - N9, Sm9))
        # c2 landscape
        mgw = np.exp(lgw - sh)
        neg_frac = float(np.sum(mgw[sgw < 0])
                         / np.sum(mgw))
        o = np.argsort(-lgw)
        ntop = max(1, int(TOP_FRAC * S9))
        top_mass = float(np.sum(mgw[o[:ntop]]) / np.sum(mgw))
        gini_d = BH.gini(mgw)
        hull9 = (np.arccos(np.clip(xu9, -1, 1)) / math.pi)
        top_pos_dual = float(np.median(hull9[o[:ntop]]))
        op = np.argsort(-np.abs(wu9))
        top_pos_prim = float(np.median(hull9[op[:ntop]]))
        shift = abs(top_pos_dual - top_pos_prim)
        dual_hint = (neg_frac <= DUAL_NEGMASS) or (
            top_mass >= DUAL_CONC and shift >= POS_SHIFT)
        check("G41-dual-landscape", True,
              "c2 DUAL MAGNITUDES ADJUDICATED (w9): log10|w#| "
              "range [%.1f, %.1f] vs primal [%.1f, %.1f]; dual "
              "negative-mass fraction %.3f (hint bar %.0e); "
              "gini %.4f, top-%d mass %.4f, hull-position shift "
              "%.3f (bar %.1f) => %s"
              % (float(np.min(lgw)) / math.log(10),
                 float(np.max(lgw)) / math.log(10),
                 float(np.min(np.log(np.abs(wu9))))
                 / math.log(10),
                 float(np.max(np.log(np.abs(wu9))))
                 / math.log(10),
                 neg_frac, DUAL_NEGMASS, gini_d, ntop, top_mass,
                 shift, POS_SHIFT,
                 "DUAL_MECHANISM_HINT" if dual_hint
                 else "DUAL_RESTATEMENT (same atom signature, "
                 "radically different magnitudes, no isolated "
                 "carrier structure)"))

    # ---------------- S5 leg D
    section("S5  LEG D -- MOMENT VIEW (WEYL RANGE + REST ZONE)")
    if smoke:
        for g in ("G50-weyl-range", "G51-rest-zone",
                  "G52-detector"):
            check(g, True, "SMOKE: skipped")
        X_weyl = None
        det_typ = {}
    else:
        def weyl_X(zones, grid, tag):
            xs_, ws_, ys_, vs_ = zones
            Kmax = 2 * max(grid) - 1
            dpsm = 60 + 8 * max(grid)
            m_mu = moments_mp(xs_, ws_, Kmax, dpsm)
            m_nu = moments_mp(ys_, vs_, Kmax, dpsm)
            last_ok = 0
            first_bad = None
            curve = {}
            prev = 0
            for n in grid:
                dps_n = 60 + 8 * n
                lmn, _lx = hankel_extremes(m_mu, n, dps_n)
                _ln, lxn = hankel_extremes(m_nu, n, dps_n)
                curve[n] = (float(lmn), float(lxn))
                if lmn > lxn:
                    last_ok = n
                    prev = n
                else:
                    first_bad = n
                    break
            if first_bad is not None and first_bad - prev > 1:
                for n in range(prev + 1, first_bad):
                    dps_n = 60 + 8 * n
                    lmn, _lx = hankel_extremes(m_mu, n, dps_n)
                    _ln, lxn = hankel_extremes(m_nu, n, dps_n)
                    curve[n] = (float(lmn), float(lxn))
                    if lmn > lxn:
                        last_ok = n
                    else:
                        first_bad = n
                        break
            return last_ok, first_bad, curve
        X_weyl, xbad, curve9 = weyl_X(zones9, WEYL_GRID, "w9")
        ok_w = (X_weyl >= 1) and (xbad is not None) \
            and bool(np.all(sg9[:N9] > 0))
        check("G50-weyl-range", ok_w,
              "d1 WEYL RANGE (w9, mp): lam_min(H_n(mu)) > "
              "lam_max(H_n(nu)) holds up to X_weyl = %d and "
              "genuinely FAILS at n = %d (%.2e vs %.2e) while "
              "D_n > 0 holds through N_w = %d -- the natural "
              "perturbation argument carries %.1f%% of the way; "
              "the remainder IS the open core (honest)"
              % (X_weyl, xbad, curve9[xbad][0], curve9[xbad][1],
                 N9, 100.0 * X_weyl / N9))
        # rest zone census
        def canc(zones):
            xs_, ws_, ys_, vs_ = zones
            m_mu = moments_mp(xs_, ws_, K_CANC, CANC_DPS)
            m_nu = moments_mp(ys_, vs_, K_CANC, CANC_DPS)
            r = [float(abs(a - b) / (abs(a) + abs(b)))
                 for a, b in zip(m_mu, m_nu)]
            return r
        r9 = canc(zones9)
        worlds_d = {}
        for cn, kw in cdefs.items():
            cctx = MS.ctx_build(9, **kw)
            _x, _w, cz = union_of_ctx(cctx)
            worlds_d[cn] = (cctx, cz)
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        hctx = MS.ctx_build(9, comb=comb_hl)
        hxu, hwu, hz = union_of_ctx(hctx)
        hsg, _hl, _hr = sign_chain_f64(hxu, hwu, hctx["N"] + EXT)
        hl_mc = next((n for n in range(len(hsg)) if hsg[n] < 0),
                     None)
        worlds_d["HL2"] = (hctx, hz)
        rz = {"MAIN": float(np.median(r9[:REST_K + 1]))}
        wx = {}
        for cn, (cctx, cz) in worlds_d.items():
            rc = canc(cz)
            rz[cn] = float(np.median(rc[:REST_K + 1]))
            Xc, _b, _cv = weyl_X(
                cz, tuple(n for n in WEYL_GRID
                          if n <= CTRL_WEYL_MAX), cn)
            wx[cn] = Xc
        check("G51-rest-zone", True,
              "d1 REST ZONE ADJUDICATED (r248-type moment "
              "cancellation, mp dps %d): median r_k (k <= %d) "
              "MAIN %.2e vs %s; HL2 surrogate flip %s"
              % (CANC_DPS, REST_K, rz["MAIN"],
                 str({c: "%.1e" % rz[c] for c in worlds_d}),
                 str(hl_mc)))
        dead_rz = [rz[c] for c in worlds_d]
        det_typ = {
            "WEYL": ("MAIN_SEPARATING"
                     if X_weyl >= DET_FACTOR * max(wx.values())
                     else "WORLD_BLIND"),
            "RESTZONE": ("MAIN_SEPARATING"
                         if rz["MAIN"] * DET_FACTOR
                         <= min(dead_rz) else "WORLD_BLIND")}
        check("G52-detector", True,
              "d2 PAIRCORR DETECTOR ADJUDICATED (battery = 3 "
              "controls + HL2 seed %d): Weyl X per world %s => "
              "%s; rest-zone medians => %s -- a WORLD_BLIND "
              "argument cannot carry the localization"
              % (HL2_SEED, str(wx), det_typ["WEYL"],
                 det_typ["RESTZONE"]))

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    # m1: dual weights without L'^2
    nodes = [t[0] for t in jf_pairs]
    wts = [t[1] for t in jf_pairs]
    S_t = len(nodes)
    _al, _be, hs_t = stj_full(nodes, wts)
    dw_bad = [1 / w for w in wts]
    _aB, _bB, hsB = WD.stj_gen(nodes, dw_bad, 1)
    res_m1 = hs_t[S_t - 1] * hsB[0] - 1
    check("G60-mustfail-noLp", res_m1 != 0,
          "m1 DUAL WEIGHTS WITHOUT L'^2 (w# := 1/w): the "
          "complement product h_{S-1} h#_0 - 1 = %.3e != 0 LOUD "
          "(exact rationals) -- the Vandermonde gauge is "
          "load-bearing" % float(res_m1))
    # m2: off-by-one translation on a constructed minC == Nw-1 toy
    hit = None
    for vname, vw in M2_VARIANTS:
        _a2, _b2, hs2 = stj_full(TOYS_XS, vw)
        mc2 = toy_minC(hs2, 6)
        if mc2 == (6 + 1) // 2 - 1:
            hit = (vname, vw, hs2, mc2)
            break
    ok_m2 = False
    det_m2 = "no minC == N_w - 1 variant found"
    if hit is not None:
        vname, vw, hs2, mc2 = hit
        dw2, _lp2 = toy_dual_weights(TOYS_XS, vw)
        _aD, _bD, hsD2 = WD.stj_gen(TOYS_XS, dw2, 5)
        negD2 = [k for k in range(5) if hsD2[k] < 0]
        maxK2 = max(negD2) if negD2 else -1
        Nw2 = (6 + 1) // 2
        lhs2 = mc2 >= Nw2
        rhs_true = maxK2 <= 6 - 1 - Nw2
        rhs_mut = maxK2 <= 6 - Nw2
        ok_m2 = (lhs2 == rhs_true) and (lhs2 != rhs_mut)
        det_m2 = ("variant %s: min C = %d = N_w - 1; true "
                  "translation adjudicates EQUAL (%s == %s), the "
                  "off-by-one mutant (bound S - N_w) "
                  "MISADJUDICATES (%s != %s) -- loud"
                  % (vname, mc2, str(lhs2), str(rhs_true),
                     str(lhs2), str(rhs_mut)))
    check("G61-mustfail-offbyone", ok_m2, "m2 " + det_m2)
    # m3: Weyl overreach
    if smoke:
        check("G62-mustfail-weyl-overreach", True,
              "SMOKE: skipped (needs the leg-D curve)")
    else:
        lmn, lxn = curve9[xbad]
        check("G62-mustfail-weyl-overreach", not (lmn > lxn),
              "m3 WEYL OVERREACH: asserting the bound at n = "
              "X_weyl + 1 = %d FAILS as demanded (%.2e <= %.2e) "
              "-- the perturbation range is not extendable by "
              "assertion" % (xbad, lmn, lxn))
    # m4 + scopes
    hits = []
    for fn in BL_FUNCS:
        hits += scope_audit(fn)
    hits_mut = scope_audit("mutant_gift_dir")
    ag_hits = antigate_fragment_audit()
    check("G63-scope-audits", not hits and bool(hits_mut)
          and not ag_hits,
          "the census/gradient/dual/moment constructors consume "
          "comb/chain/grid data ONLY (%s); the deliberately "
          "offset-reading gift direction is FLAGGED (%s); "
          "fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_mut) if hits_mut else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S7 verdict
    section("S7  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: no derived 5/7, no bound mechanism "
          "claim, no asymptotic law, NO localization claim from "
          "the census (measurement only), mincut base 4 / "
          "refined 5 UNCHANGED; what the round adds: the full "
          "42-rung offset census with dose link, the extremality "
          "adjudication with exact rebuilt worlds, the exact "
          "dual translation, and the honest Weyl range")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["LOCALIZATION_CENSUS(offsets %s, max +%d, "
                 "sp(offset, N) %+.3f; anchors exact; dose link "
                 "min C == nf + r276 medians reproduced)"
                 % (str({("+%d" % k): dist[k]
                         for k in sorted(dist)}),
                    max(offs_true), sp_oN)]
        if n_raise_ver > 0:
            parts.append("MAIN_NOT_MAXIMAL(%d mp-confirmed "
                         "raising worlds on w9: %s)"
                         % (n_raise_ver, str(raisers9)))
        elif n_fo_raisers == 0:
            parts.append("MAIN_LOCALLY_MAXIMAL(within the tested "
                         "direction classes)")
        else:
            parts.append("MAIN_MAXIMALITY_UNRESOLVED(%d "
                         "first-order candidates, none verified)"
                         % n_fo_raisers)
        parts.append("CRITICALITY_%s(rho_crit %.3f, cos_w %+.3f)"
                     % ("STRUCTURED" if crit_struct
                        else "UNSTRUCTURED", rho_crit, cosw))
        parts.append("DUAL_TRANSLATION_EXACT")
        parts.append("DUAL_MECHANISM_HINT" if dual_hint
                     else "DUAL_RESTATEMENT")
        parts.append("MOMENT_PERTURBATION_RANGE(X_weyl = %s of "
                     "N_w %d; detector: WEYL %s, RESTZONE %s)"
                     % (str(X_weyl), N9, det_typ.get("WEYL"),
                        det_typ.get("RESTZONE")))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: census, directions, rebuilt worlds, "
          "dual landscape, Weyl range; PROVED (exact, toy grade): "
          "complement product, sign mirror, translation, minor "
          "factorization; OPEN: the localization itself (the "
          "r279-b3 statement stands); NO RH claim"
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
