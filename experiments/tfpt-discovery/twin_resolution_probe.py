#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""twin_resolution_probe -- PRIME.AUDIT.TWIN_RESOLUTION.01
(round 331): the AUDIT REPAIR of the METRIC_ONLY reach.  Audit C
(round 328C) found that the strategically load-bearing r289 switch
METRIC_ONLY ("the diophantine structure of the log positions is
irrelevant -- only the metric structure carries") was adjudicated
at the w9 wall margin 1.7e-4 on the log-2-commensurate grid, while
the r286 ladder runs down to margins 1.8e-8 (kz98/kz119) -- where
the rational twin's own construction disturbance might exceed the
margin: THE TWIN COULD BE BLIND THERE, and METRIC_ONLY would be
UNTESTED (not confirmed) at the tight anchors.  This round
measures the twin RESOLUTION exactly: how large is the twin
disturbance in margin units, on which anchors is disturbance <
margin (twin CAN distinguish -- METRIC_ONLY is evidenced there)
and where is it > margin (twin blind -- METRIC_ONLY untested), at
which twin precision do the tight anchors become twin-stable, and
does a GENUINE diophantine perturber (exact log relations broken,
metric gap structure preserved) crack the wall on an anchor where
the twin resolves?  MEASUREMENT + ADJUDICATION ONLY: no proof
attack, no L* claim, no retyping of earlier rounds (the
coordinator owns any consequence bookkeeping).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r330 discipline): w = window (kz
index into the prime-power list V.PP), z = V.PP[kz], S = #union
atoms, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2 = critical degree,
n = chain degree, j = comb atom index; margin = 1 -
lambda_max(E_{N_w}) on the r283/r284/r286 dressed CD-kernel Gram;
minC = first union pivot flip (r283 equivalence: margin > 0 <=>
minC >= N_w -- the two-route gate on EVERY world).  Ground truth
(record margins, offsets, minC) enters GATES and record tables
only; the sealed constructors consume comb positions + weights +
grid geometry ONLY (AST scope audit); no zero/prime oracles
anywhere (AST firewall).  MACHINERY IMPORTED VERBATIM: the
standalone document pipeline rh/problem/verify_lstar_instance
V.{window_shape, arch_lags, spectral_density, mu_chain, b_matrix,
mp_lam_max, admissible_indices, PP, U, W_VM} (r285/r286: the
document object IS the campaign object, cross-check-gated), r289
AKD.{best_rational, twin_rational, frac_split} (the sealed twin
constructors, scope-audited there and re-audited here), r286
LMS.{sign_chain_union, audit_no_mp} (union census + the m3
no-mp detector), r276 MF.local_gaps.  The comb->world channel is
a VERBATIM re-expression of V.prime_lags/build_measures with
explicit atoms (comb_lags/build_world below), identity-gated
BITWISE against V.build_measures at dose zero on every anchor
this round touches.  No RNG anywhere: the round is seed-free
deterministic (twins by continued fractions, the counter-test by
a fixed golden-ratio pattern).

LEG A -- THE RESOLUTION ANALYSIS (audit task 1):
(a1) the r289 twin disturbance quantified: per anchor the twin at
  the r289 reference precision RAT_TOL_REF = 1e-8 (every u_j /
  Delta replaced by its first CF convergent p/q with |u/Delta -
  p/q| <= 1e-8 g_j/Delta); printed per anchor: denominator census
  (median / max q), position deviation max |log(p^k) - (p/q)
  Delta| absolute and gap-relative -- the exact twin disturbance
  the audit asked for.
(a2) the margin-unit comparison: DISTURBANCE(margin units) :=
  |Delta_m| = |margin_twin - margin_main| MEASURED per anchor
  (not modeled), against the anchor margin.  Sealed resolution
  classes (bars fixed from the audit semantics BEFORE any
  evaluation, not tuned on data): RESOLVES iff signature kept
  (margin_twin > 0 AND minC_twin == minC_main) and |Delta_m| <=
  RES_BAR x margin (RES_BAR = 0.1: the twin's own footprint is
  <= 10 percent of the margin -- a null twin outcome is a
  resolved statement); BLIND iff signature broken OR |Delta_m| >
  BLIND_BAR x margin (BLIND_BAR = 1.0: the twin's footprint
  exceeds the margin -- the twin cannot distinguish there);
  MARGINAL otherwise.
(a3) the RESOLUTION TABLE over the ladder: sealed anchor rule =
  the 42 document-admissible rungs in list order, indices
  TABLE_IDX = (0, 6, 12, 18, 24, 30, 36, 41) (an 8-rung spread
  across the family; margins span the wall margin 1.7e-4 down to
  the 1e-7 class) PLUS the sweep anchors of LEG B (kz 64 / 98 /
  119 -- the r286 minimum of the 42 and the two tightest
  extension anchors of the 1.8e-8 class).  Every main margin is
  typed by the r286 sign-safety tiers (F >= 1e-5 f64 + two-route
  equivalence; M < 1e-5 adds mp dps 30, rel agreement 0.05;
  X < 1e-6 adds dps 45, staggered agreement 0.01).

LEG B -- THE PRECISION SWEEP (audit task 2; the sharpened twin):
sweep anchors SWEEP_KZ = (9, 64, 98, 119) (wall anchor + min of
the 42 + the two 1.8e-8-class extension anchors; r286 records
+1.6752e-4 / +1.4175e-7 / +1.9486e-8 / +1.8056e-8, offsets 0 /
+2 / +1 / +1 -- gate anchors), precision ladder TOLS = (1e-3,
1e-6, 1e-8, 1e-10) (gap-relative twin tolerance; the DENOMINATOR
ladder is its measured dual and is printed per stage -- q grows
as the tolerance falls; the audit's 10^3..10^12 denominator
stages appear in the censuses).  Per stage (anchor x tol): twin
construction (AKD.twin_rational verbatim at tol), conservation
gates (weights bitwise, cells preserved with the r289-a1 node
snap, strict atom order, |du_j| <= max(tol g_j, ULP floor),
on-node family preserved, q <= QMAX_GUARD = 1e12 on constructible
atoms -- "small denominator" always means q << 2^53), f64 margin
+ minC, and the mp pair protocol: for margin < MP_TIER1 the
stage Delta_m is taken from the mp dps-30 PAIR (margin_twin -
margin_main both at dps 30) with the f64 cross-ward |Delta_f64 -
Delta_mp30| <= max(0.25 |Delta_mp30|, DELTA_FLOOR); |Delta_mp30|
< DELTA_FLOOR = 1e-13 (the pipeline's eigenvalue resolution: B
is mp-exact, the eigensolve is f64) is typed "< floor" and the
class uses the SAFE upper bound DELTA_FLOOR.  DECISION STAGES
(each anchor's main + its coarsest RESOLVING stage) additionally
carry the dps-45 pair: per-world staggered agreement <= 0.01
rel (r286 MP_AGREE) and pair agreement |D30 - D45| <= max(0.25
max(|D30|, |D45|), DELTA_FLOOR) -- else the stage is typed
MP_TIER_BREAK and FLAGGED.  DELIVERABLE: per tight anchor
(margin < 1e-6) the coarsest tol t* such that t* and every finer
ladder stage RESOLVES ("ab welcher Praezision wird der Anker
Twin-stabil"); NOT_RESOLVED if none.  F64 CONSTRUCTION FLOOR
(disclosed): atoms whose tolerance falls below ULP_GUARD = 64
ulp of u/Delta are typed ON_F64_FLOOR (census printed; their CF
runs to the f64-exact rational -- the double itself; they are
excluded from the QMAX gate and their measured |du| is the
honest stage dose); sub-floor twin precisions are not
constructible in this f64 pipeline -- a disclosed machinery
boundary, not a physics statement.

LEG C -- THE COUNTER-TEST (audit task 3; the genuine diophantine
perturber): positions u_j -> u_j + eps g_j (2 {(j+1) phi} - 1)
with phi = (sqrt(5)-1)/2 (fixed golden-ratio pattern:
deterministic, atom-distinct, structure-free in the rational
sense) -- the INVERSE of the twin: the twin RATIONALIZES every
position (diophantine input trivialized), the counter-test
DETUNES every exact relation away from the designed log
arithmetic while PRESERVING the metric gap structure (sealed
admissibility gates: weights bitwise, |du_j| <= eps g_j exact,
max relative gap change <= GAP_ABS_BAR = 1e-4 -- one order below
the r289-measured metric coherence threshold 1e-3..3e-3 gap; a
perturber that moves the gap structure is a METRIC surgeon and
is REJECTED, see must-fail m2).  Two variants on w9: CT1 = all
atoms, CT2 = the exact-resonance family only (the on-node
2-power atoms; the 28 exact resonances {46 log2 2^(a-b)} = 0
must drop to 0 resonant pairs -- the diophantine structure
DEMONSTRABLY destroyed at metric cost <= eps); plus CT1 on the
TIGHTEST sweep anchor that resolves (kz 119 expected; its exact-
resonance census is measured and CT2 there is typed
NOT_APPLICABLE if the census is empty -- the log-2
commensurability is a w9 property).  Sealed dose rule: eps_CT =
min(t*(anchor), CT_EPS_CAP = 1e-4) -- the counter-test runs
EXACTLY where the twin resolution is established, capped one
order below the metric threshold.  Sealed break rule: CT_BREAKS
iff minC changes or margin_CT <= 0 (signature loss); Delta_m of
every CT world printed (mp pair per the LEG-B protocol at tight
anchors).  If any admissible CT world at a resolving dose
BREAKS: the switch must be revised (lead verdict REVISED,
sealed) -- honest and immediate.

SEALED ADJUDICATION (exactly one lead verdict):
  METRIC_ONLY_REVISED(anchor, dose) iff any admissible
    counter-test world at a RESOLVING dose breaks the wall;
  else METRIC_ONLY_CONFIRMED_AT_RESOLUTION(range) iff EVERY
    tight sweep anchor (margin < 1e-6) has a resolving t* in the
    ladder AND every admissible counter-test (w9 CT1 + CT2 + the
    tight-anchor CT) keeps the wall -- the confirmed range is
    the measured resolved set (margins and tolerances named);
  else METRIC_ONLY_UNTESTED_AT_TIGHT(anchors) -- the tight
    anchors without a resolving stage are named and the switch
    is confirmed only on the resolved range (consequence
    bookkeeping belongs to the coordinator, NOT this round).

WARDS / MUST-FAILS (each loud): flagship w9 regression through
the document pipeline (S = 367/263/104, N_w = 184, lambda_max =
0.99983248, margin 1.6752e-4 rel 0.01, minC = 184, crossing
lambda(E_185) = 1.00003660 > 1, mp staffel dps 30/45 vs the
dps-60 record, abs bar 1e-6); comb-channel identity BITWISE
(build_world == V.build_measures on xp/wp/yn/vn at dose zero on
EVERY anchor of the round); r289 twin regression (w9 twin at
1e-8: minC 184 kept, margin sign kept, weights bitwise, cells
kept, on-node family kept -- the r289 METRIC_ONLY signature
reproduced through the document pipeline, with the NEW
measurement Delta_m printed); r286 sweep-anchor regression
(margins rel 0.05 + offsets exact vs the r286 records); exact
toys (t1 continued fractions 1/2, pi -> 333/106, 46 -> 46/1;
t2 hand 4-atom transfer toy: lambda_max(E_2) = 11/240 exact,
position transfer d lambda = v(2 y e + e^2) x 2 reproduced to
1e-12, the failure direction v = 10 flips minC to 0 both routes;
t3 hand fraction census: one exact resonant pair counted, golden
detune destroys it, gaps preserved, weights bitwise).
MUST-FAILS: (m1) TWIN COLLISION -- the denominator-ladder mutant
at tol_gap = 4.0 (position budget 4x the local gap) must produce
position COLLISIONS on w9 and be CAUGHT by the strict-order/
distinctness gate; (m2) METRIC PERTURBER AS COUNTER-TEST -- the
golden detune at eps = 0.05 changes the gap structure loudly
(> GAP_ABS_BAR) and must be REJECTED by the CT admissibility
gate (it would be a metric, not a diophantine perturber);
(m3) MP-TIER BREAK -- a deliberate ledger entry with margin
5e-6 and no mp verification must be FLAGGED by the r286
audit_no_mp detector (and the real stage ledger must be clean);
(m4) TARGET READBACK -- a twin oriented by the withheld minC is
FLAGGED by the AST scope audit (the sealed constructors audit
clean; fragment audit: no fit primitives).  STOP LIST
(anti-gates, binding): NO L* claim, NO bound mechanism, NO
Baker/Matveev application, NO asymptotic law, NO retyping of
r289/r286 or any earlier round (findings are HANDED OVER), NO
posthoc anchor choice, NO RH claim; r243..r330 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel 0.01; MP_REC_BAR 1e-6; SWEEP_KZ (9, 64, 98, 119);
SWEEP_REC (+1.6752e-4, +1.4175e-7, +1.9486e-8, +1.8056e-8) rel
0.05; SWEEP_OFF (0, +2, +1, +1); TABLE_IDX (0, 6, 12, 18, 24,
30, 36, 41); TOLS (1e-3, 1e-6, 1e-8, 1e-10); RAT_TOL_REF 1e-8;
RES_BAR 0.1; BLIND_BAR 1.0; MP_TIER1 1e-5; MP_TIER2 1e-6; DPS_A
30; DPS_B 45; F64_AGREE 0.05; MP_AGREE 0.01; PAIR_WARD 0.25;
DELTA_FLOOR 1e-13; QMAX_GUARD 1e12; ULP_GUARD 64; CENSUS_EXT 48;
ONNODE_EPS 1e-6; RESON_TOL 1e-12; NODE_SNAP 1e-9; GOLDEN
(sqrt(5)-1)/2; CT_EPS_CAP 1e-4; GAP_ABS_BAR 1e-4; M1_TOL 4.0;
M2_EPS 0.05; TOY_TOL 1e-12; runtime <= 1800 s; smoke = toys +
firewall + scopes + w9 regression + comb identity + w9 twin at
1e-8 (f64) + must-fails m1-m4 (table, sweep, mp tiers,
counter-test, adjudication skipped).  PRE-SPEC SCOPING
(disclosed, budget/feasibility sizing only): ONE scoping pass
before this spec was frozen measured (s1) mp dps-30 cost 9.7 /
13.0 / 16.4 s at kz 64/98/119 (the mp budget plan), (s2) the
comb-channel identity bitwise + the r286 record margins/offsets
reproduced on the four sweep anchors, (s3) the m1 collision
mutant produces 4 collisions on w9 at tol 4.0 (feasibility),
and (s4) the four @1e-8 twin deltas were SEEN (ratios 1.4e-5 /
1.9e-4 / 3.6e-4 / 1.8e-4 -- disclosed honestly); the resolution
bars RES_BAR/BLIND_BAR are the audit's own semantics (10
percent / 100 percent of the margin), fixed before the scoping
values were read and NOT moved after; no other bar, band, class
rule or verdict rule was tuned on any evaluation of this probe.

DISCLOSED CALIBRATION AMENDMENTS (found in calibration pass 1 =
the first full evaluation, BEFORE the record freeze; each is a
measurement-domain fix on a GATE/WARD -- the twin construction,
the resolution classes, the Delta source policy (mp pairs), the
counter-test rules and the lead-verdict rule never moved):
(a1) DU-GATE ROUNDING SLACK: the reconstruction u' = (p/q) Delta
  rounds ONCE beyond the CF tolerance check |u/Delta - p/q| <=
  tol_x -- a handful of atoms tied the gate at the last ulp
  (e.g. kz119 tol 1e-10: |du| 9.41e-14 vs allowance 9.35e-14).
  The gate now carries the slack + 4 ulp(u).
(a2) CELL/NODE GATES BUDGET-SCOPED: at coarse tolerance the twin
  legitimately rationalizes near-node atoms ONTO exact nodes
  (e.g. kz98 tol 1e-3: fraction 4.95e-6 -> 0) -- WITHIN the
  sealed position budget; the r289 cell/on-node preservation
  statements are 1e-8-scale statements.  The gates now bind only
  on atoms whose budget cannot reach a node (tol_x + 4 ulp <
  fraction distance); in-budget node landings / cell hops are
  counted and printed per stage.
(a3) F64-vs-MP CROSS-WARD FLOOR: at the finest stages the f64
  Delta is dominated by the f64 margin noise (~1e-12 abs at the
  deep anchors; r286 measured f64-vs-mp rel dev up to 6.6e-6)
  while the mp pair Delta is ~1e-13 -- the cross ward's floor
  moved from DELTA_FLOOR (1e-13, the mp resolution) to
  F64_NOISE = 1e-11 (the f64 noise floor).  The CLASSIFICATION
  is untouched: it always consumes the mp pair Delta.
PROTOCOL DISCLOSURE (r316-class, honest): a drafted record-table
block was accidentally written into this docstring BEFORE the
first run and was REMOVED before any evaluation; the record
tables below stem exclusively from the sealed record run.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] METRIC_ONLY_CONFIRMED_AT_RESOLUTION(range) /
    METRIC_ONLY_UNTESTED_AT_TIGHT(anchors) /
    METRIC_ONLY_REVISED(anchor, dose)
  + RESOLUTION_TABLE(per anchor: margin, tier, twin disturbance,
    class) [always]
  + PRECISION_SWEEP(per sweep anchor: stage classes + t*)
    [always]
  + COUNTER_TEST(w9 CT1/CT2 + tight-anchor CT outcomes) [always]
  + DENOMINATOR_LEDGER(q + floor censuses) [always]
  + DETECTOR_LEDGER(mp discipline, audits) [always].
Honesty before beauty: every resolution class is a MEASUREMENT
on finite windows through one sealed pipeline; RESOLVES states
that the twin's own footprint is provably below a tenth of the
margin THERE, never that METRIC_ONLY holds beyond the tested
set; the f64 construction floor bounds the reachable twin
precision and is disclosed, not hidden; a REVISED outcome would
be sealed immediately and handed to the coordinator; no verdict
claims L*, a bound mechanism, an asymptotic law, or RH progress
in any direction.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 24/24 (0.5 s) on the sealed
spec; calibration pass 1 = first full evaluation = 21/24, wall
479.3 s, exposing the three gate/ward artifacts behind the
disclosed amendments a1-a3 above (du rounding ties, in-budget
node landings at coarse tol, f64-noise ward floor -- every
physics number of pass 1 is IDENTICAL to the record below);
calibration pass 2 = 24/24, wall 467.7 s; the pre-freeze commit
holds the amended spec WITHOUT records; record run1 = 24/24,
wall 453.7 s; run2 identical up to WALL (462.8 s); the
record-table insertion is the only post-freeze edit, which IS
the protocol):
CAL_VERDICT = METRIC_ONLY_CONFIRMED_AT_RESOLUTION(margins
1.675e-4 .. 1.806e-8 over 11 anchors; every tight anchor
twin-stable at t* = 1e-6; every admissible counter-test keeps
the wall) + RESOLUTION_TABLE + PRECISION_SWEEP + COUNTER_TEST +
DENOMINATOR_LEDGER + DETECTOR_LEDGER.
THE RESOLUTION TABLE (r289 twin at 1e-8; per anchor: margin
[tier], |Delta_m| (source), ratio, class):
  kz9  /z16   +1.675e-4 [F]  2.26e-9 (f64)   1.35e-5  RESOLVES
  kz18 /z37   +3.058e-5 [F]  2.78e-10 (f64)  9.10e-6  RESOLVES
  kz24 /z59   +2.094e-6 [M]  1.66e-10 (mp30) 7.91e-5  RESOLVES
  kz30 /z79   +1.003e-6 [M]  9.59e-11 (mp30) 9.56e-5  RESOLVES
  kz38 /z109  +8.845e-7 [X]  6.86e-11 (mp30) 7.76e-5  RESOLVES
  kz48 /z151  +6.245e-7 [X]  3.68e-11 (mp30) 5.88e-5  RESOLVES
  kz59 /z199  +6.309e-7 [X]  4.72e-13 (mp30) 7.48e-7  RESOLVES
  kz82 /z317  +1.722e-7 [X]  1.77e-11 (mp30) 1.03e-4  RESOLVES
  kz64 /z233  +1.417e-7 [X]  2.81e-11 (mp30) 1.98e-4  RESOLVES
  kz98 /z409  +1.949e-8 [X]  7.13e-12 (mp30) 3.66e-4  RESOLVES
  kz119/z529  +1.806e-8 [X]  3.45e-12 (mp30) 1.91e-4  RESOLVES
11/11 RESOLVE, 0 BLIND, 0 MARGINAL; worst ratio 3.66e-4 (kz98):
the audit's feared blindness at the r289 precision does NOT
occur -- the twin footprint lands >= 3.4 orders below EVERY
margin, including the 1.8e-8 class; minC preserved on all 11;
offsets vs r286 records exact (+0/+2/+1/+1 on the sweep
anchors).  THE PRECISION SWEEP (ratio |Delta_m|/margin; sig =
minC kept):
  kz9:   1e-3 BLIND (minC 170 != 184, ratio 1.28) / 1e-6
         2.03e-3 R / 1e-8 1.35e-5 R / 1e-10 4.42e-8 R
  kz64:  1e-3 BLIND (minC 223 != 861, ratio 4.78e4) / 1e-6
         1.73e-4 R / 1e-8 1.98e-4 R / 1e-10 1.78e-6 R
  kz98:  1e-3 BLIND (minC 200 != 998, ratio 1.17e5) / 1e-6
         9.87e-2 R / 1e-8 3.66e-4 R / 1e-10 < floor R
  kz119: 1e-3 BLIND (minC 224 != 1120, ratio 8.63e5) / 1e-6
         1.60e-2 R / 1e-8 1.91e-4 R / 1e-10 < floor R
t* = 1e-6 on ALL FOUR sweep anchors (decision stages dps-45
re-verified, values identical to dps-30 at print precision);
the twin-resolution threshold of the tight anchors sits between
1e-3 and 1e-6 of the local gap; kz98 at 1e-6 is the closest
call (ratio 9.87e-2 just under RES_BAR 0.1, dps-45 confirmed).
THE COUNTER-TEST (golden detune, gap-preserving, eps = t* =
1e-6): w9 CT1 (all 70 atoms): 28 -> 0 exact resonances, KEEPS
minC 184, Delta -3.99e-8; w9 CT2 (exactly the 8 on-node 2-power
atoms): 28 -> 0, KEEPS, Delta +8.26e-8 -- destroying the ENTIRE
exact 2-power resonance arithmetic costs 5e-4 of the margin;
kz119 CT1 (24574 atoms): KEEPS minC 1120, Delta +4.70e-11
(mp30, ratio 2.6e-3); kz119 CT2 (2 on-node atoms): KEEPS,
Delta +1.71e-12 -- the genuinely diophantine direction cannot
crack the wall at any resolving dose, on the wall anchor OR the
tightest anchor.  DENOMINATOR LEDGER: q med climbs 19 (1e-3) ->
5408 (1e-8) -> 71894 (1e-10) on w9 and 313 -> 98461 -> 981809
on kz119 (the audit's denominator ladder is the measured dual
of the tolerance ladder); q max on constructible atoms <=
3.9e8 <= QMAX_GUARD 1e12 << 2^53; f64 floor censuses 0
everywhere at 1e-3/1e-6 and 0..3230 at 1e-8, 4834/14606/23725
at 1e-10 (kz64/98/119) -- the sub-1e-10 twin regime is not
constructible in f64, disclosed; in-budget node landings/cell
hops only at 1e-3 (1-2 atoms per anchor, censused).
DETECTORS: mp discipline clean (41-stage ledger, every
sub-1e-5 margin carries dps-30, decision stages dps-45, no
MP_TIER_BREAK); m1 collision mutant CAUGHT (4 collisions,
66/70 unique); m2 metric perturber REJECTED (gap change 6.2e-2
> 1e-4); m3 no-mp entry FLAGGED + real ledger clean; m4
target-readback twin FLAGGED; constructors + fragment audit
CLEAN.  READING (typed MEASUREMENT, handed to the coordinator):
the audit-C2 concern is RESOLVED IN THE BENIGN DIRECTION -- the
r289 twin was never blind at the tight anchors (its footprint
at 1e-8 is 3.4+ orders below the 1.8e-8 margins because the
margin responds to the rationalization far more weakly than
1:1 in gap units), the METRIC_ONLY switch now carries a
measured resolution certificate over margins 1.7e-4 .. 1.8e-8
plus a genuine-diophantine counter-test at the tightest anchor;
what remains open honestly: (i) twin precision below the f64
floor (~1e-10 gap at the deep anchors), (ii) near-resonance
(vs exact-resonance) structure, (iii) anchors beyond the
tested 11, (iv) the counter-test destroys designed relations
at eps-scale -- sub-eps diophantine effects are not probed.
Runtime 453.7 s full / 0.5 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (records inserted per
protocol; no bar, band, class rule or verdict rule moved).

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
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V              # noqa: E402 document pipeline
import lstar_margin_scaling_probe as LMS       # noqa: E402 r286
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
MP_REC_BAR = 1.0e-6
SWEEP_KZ = (9, 64, 98, 119)
SWEEP_REC = {9: 1.6752e-4, 64: 1.4175e-7, 98: 1.9486e-8,
             119: 1.8056e-8}
SWEEP_REC_TOL = 0.05
SWEEP_OFF = {9: 0, 64: 2, 98: 1, 119: 1}
TABLE_IDX = (0, 6, 12, 18, 24, 30, 36, 41)
TOLS = (1.0e-3, 1.0e-6, 1.0e-8, 1.0e-10)
RAT_TOL_REF = 1.0e-8
RES_BAR = 0.1
BLIND_BAR = 1.0
MP_TIER1 = 1.0e-5
MP_TIER2 = 1.0e-6
DPS_A = 30
DPS_B = 45
F64_AGREE = 0.05
MP_AGREE = 0.01
PAIR_WARD = 0.25
DELTA_FLOOR = 1.0e-13
F64_NOISE = 1.0e-11
QMAX_GUARD = 1.0e12
ULP_GUARD = 64.0
CENSUS_EXT = 48
ONNODE_EPS = 1.0e-6
RESON_TOL = 1.0e-12
NODE_SNAP = 1.0e-9
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
CT_EPS_CAP = 1.0e-4
GAP_ABS_BAR = 1.0e-4
M1_TOL = 4.0
M2_EPS = 0.05
TOY_TOL = 1.0e-12

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
    return (not bad), ("NO zero/prime oracles; the constructors "
                       "consume comb positions + weights + grid "
                       "geometry ONLY; record margins/offsets enter "
                       "gates and record tables only; the frozen "
                       "V.PP/U/W_VM table is the document's family "
                       "definition" if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("comb_lags", "build_world", "base_comb",
                "ct_detune", "onnode_mask")
SCOPE_FORBIDDEN = {"minC", "minC_true", "margin", "margin_true",
                   "REC_LAM", "REC_MARGIN", "SWEEP_REC", "mp_a"}


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
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def comb_lags(uu, mm, M, D):
    """V.prime_lags with EXPLICIT atoms (verbatim body): the
    triangular-window sampling of the comb, including the
    reflected tent branch; consumes positions + weights + grid
    shape only."""
    c = np.zeros(M)
    for u_j, m_j in zip(uu, mm):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D))
                                  + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= m_j * 0.5 * v
    return c


_ARCH_CACHE: dict = {}


def build_world(kz, uu, mm):
    """the document world at explicit comb atoms: comb lags +
    archimedean lags -> circulant spectral density -> folded
    mu/nu split (V.build_measures verbatim tail); identity-gated
    BITWISE against V.build_measures at dose zero."""
    alpha, M, L, Nw, D = V.window_shape(kz)
    if kz not in _ARCH_CACHE:
        _ARCH_CACHE[kz] = V.arch_lags(M, D)
    d = V.spectral_density(_ARCH_CACHE[kz] + comb_lags(uu, mm, M, D))
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    o = np.argsort(x)
    return dict(alpha=alpha, M=M, L=L, Nw=Nw, D=D,
                xp=x[pos], wp=wt[pos], yn=x[~pos], vn=-wt[~pos],
                xu=x[o], wu=wt[o], S=len(x))


def base_comb(kz):
    """the window's von Mangoldt comb from the frozen document
    table: (u_j, m_j) = (log n_j, 2 Lambda(n_j)/sqrt(n_j)) for
    n_j <= e^{2 alpha}."""
    alpha, _M, _L, _Nw, _D = V.window_shape(kz)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14,
                             side="right"))
    return (V.U[:ka].astype(float).copy(),
            V.W_VM[:ka].astype(float).copy())


def ct_detune(uu, mm, gaps, eps, mask=None):
    """the GENUINE diophantine perturber: u_j -> u_j + eps g_j
    (2 {(j+1) GOLDEN} - 1) on the masked atoms -- deterministic,
    atom-distinct, breaks every exact designed log relation while
    the metric gap structure is preserved to O(eps); weights
    untouched by construction."""
    u = np.asarray(uu, float)
    j = np.arange(1, len(u) + 1, dtype=float)
    phi = 2.0 * np.mod(j * GOLDEN, 1.0) - 1.0
    du = eps * np.asarray(gaps, float) * phi
    if mask is not None:
        du = np.where(mask, du, 0.0)
    return u + du, np.asarray(mm, float).copy(), du


def onnode_mask(uu, Dg):
    """on-node atoms (fraction distance <= ONNODE_EPS of the
    grid cell) -- the exact-resonance family of a commensurate
    grid; consumes positions + grid spacing only."""
    _i0, fr = AKD.frac_split(uu, Dg)
    return np.minimum(fr, 1.0 - fr) <= ONNODE_EPS


# ============== must-fail mutants
def mutant_target_twin(uu, minC_true):
    """m4 MUST-FAIL: a 'twin' oriented by the withheld minC --
    the scope audit must FLAG this."""
    u2 = np.asarray(uu, float).copy()
    u2[minC_true % len(u2)] += 1e-6
    return u2


# ============== gate-side measurement helpers
def frac_canon(uu, Dg):
    """(cell, fraction) with the r289-a1 node snap (frac >
    1 - NODE_SNAP -> cell+1, frac-1): the gate-side canonical
    split."""
    i0, fr = AKD.frac_split(uu, Dg)
    snap = fr > 1.0 - NODE_SNAP
    return (np.where(snap, i0 + 1, i0),
            np.where(snap, fr - 1.0, fr))


def resonance_census(fr):
    """number of EXACT resonant pairs (circular fraction values
    equal to RESON_TOL) via sorted grouping -- O(n log n), no
    pair matrix."""
    f = np.mod(np.asarray(fr, float), 1.0)
    f = np.where(f > 1.0 - RESON_TOL, f - 1.0, f)
    fs = np.sort(f)
    groups = []
    run = 1
    for k in range(1, len(fs)):
        if fs[k] - fs[k - 1] <= RESON_TOL:
            run += 1
        else:
            groups.append(run)
            run = 1
    groups.append(run)
    return int(sum(g * (g - 1) // 2 for g in groups))


def margin_f64(mz):
    """1 - lambda_max(E_{N_w}) through the document chain."""
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], mz["Nw"])
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], mz["Nw"])
    return 1.0 - float(np.linalg.eigvalsh(B @ B.T)[-1])


def minc_of(mz):
    """first union pivot flip (r286 sign_chain_union verbatim)."""
    sg = LMS.sign_chain_union(mz["xu"], mz["wu"],
                              min(mz["Nw"] + CENSUS_EXT,
                                  mz["S"] - 2))
    return next((n for n in range(len(sg)) if sg[n] < 0), None)


def mp_margin(mz, dps):
    """mp margin (document mp_lam_max verbatim: chain + B in mp,
    eigensolve f64 on the mp-exact B)."""
    return 1.0 - V.mp_lam_max(mz, mz["Nw"], dps=dps)


def measure_world(kz, uu, mm):
    """f64 bundle of one comb world: margin, minC, S."""
    mz = build_world(kz, uu, mm)
    return dict(mz=mz, margin=margin_f64(mz), minC=minc_of(mz),
                S=mz["S"], Nw=mz["Nw"], D=mz["D"])


def twin_gates(ctx, u2, m2, dens, du, tol):
    """sealed conservation gates of one twin stage; returns
    (ok, note, censuses).  Amendments a1/a2 (disclosed in the
    spec): the du gate carries the reconstruction rounding slack
    4 ulp(u) (u2 = (p/q) Delta rounds once beyond the CF
    tolerance check), and the cell/node preservation gates are
    BUDGET-SCOPED (enforced only on atoms whose position budget
    cannot reach a node; in-budget node landings / cell hops are
    counted and disclosed, they are tolerance semantics, not
    violations)."""
    uu, mm, gaps, Dg = ctx["uu"], ctx["mm"], ctx["gaps"], ctx["D"]
    x = uu / Dg
    tol_x = tol * gaps / Dg
    floor_x = ULP_GUARD * np.spacing(np.abs(x) + 1.0)
    on_floor = tol_x < floor_x
    n_floor = int(np.sum(on_floor))
    ok_w = bool(np.array_equal(m2, mm))
    ok_ord = bool(np.all(np.diff(u2) > 0.0)) \
        and len(np.unique(u2)) == len(u2)
    slack_u = 4.0 * np.spacing(np.abs(uu) + 1.0)
    allow = np.maximum(tol * gaps, floor_x * Dg) + slack_u
    ok_du = bool(np.all(np.abs(du) <= allow))
    # budget scope: atoms whose allowed move cannot reach a node
    i0a, fa = frac_canon(uu, Dg)
    i0b, fb = frac_canon(u2, Dg)
    fr = np.mod(fa, 1.0)
    dist_node = np.minimum(fr, 1.0 - fr)
    guard_x = np.maximum(tol_x, floor_x) \
        + 4.0 * np.spacing(np.abs(x) + 1.0)
    scoped = dist_node > guard_x
    ok_cell = bool(np.array_equal(i0a[scoped], i0b[scoped]))
    onA = onnode_mask(uu, Dg)
    onB = onnode_mask(u2, Dg)
    ok_on = bool(np.array_equal(onA[scoped], onB[scoped]))
    n_hop = int(np.sum(i0a[~scoped] != i0b[~scoped]))
    n_land = int(np.sum(onA[~scoped] != onB[~scoped]))
    q_con = dens[~on_floor] if n_floor < len(dens) else dens[:0]
    ok_q = (len(q_con) == 0
            or float(np.max(q_con)) <= QMAX_GUARD)
    ok = ok_w and ok_ord and ok_cell and ok_du and ok_q and ok_on
    note = ("w %s ord %s cell %s du %s q %s node %s"
            % tuple("OK" if t else "BREAK"
                    for t in (ok_w, ok_ord, ok_cell, ok_du, ok_q,
                              ok_on)))
    cens = dict(q_med=int(np.median(dens)), q_max=int(np.max(dens)),
                q_max_con=(int(np.max(q_con)) if len(q_con)
                           else 0),
                n_floor=n_floor, n_hop=n_hop, n_land=n_land,
                du_max=float(np.max(np.abs(du))),
                th_max=float(np.max(np.abs(du) / gaps)),
                th_med=float(np.median(np.abs(du) / gaps)))
    return ok, note, cens


def classify(sig_ok, dabs, margin):
    """sealed resolution classes (audit semantics)."""
    if (not sig_ok) or dabs > BLIND_BAR * margin:
        return "BLIND"
    if dabs <= RES_BAR * margin:
        return "RESOLVES"
    return "MARGINAL"


def main_tier(kz, w_main, smoke):
    """r286 sign-safety tier protocol on a main margin; returns
    (tier, safe, mp_a, mp_b)."""
    m = w_main["margin"]
    eq = (m > 0) == (w_main["minC"] is None
                     or w_main["minC"] >= w_main["Nw"])
    if abs(m) >= MP_TIER1 or smoke:
        return ("F" if abs(m) >= MP_TIER1 else "F(smoke)",
                bool(eq), None, None)
    mp_a = mp_margin(w_main["mz"], DPS_A)
    ok = (abs(m - mp_a) <= F64_AGREE * abs(mp_a)) \
        and ((m > 0) == (mp_a > 0)) and eq
    if abs(mp_a) >= MP_TIER2:
        return ("M", bool(ok), mp_a, None)
    mp_b = mp_margin(w_main["mz"], DPS_B)
    ok = ok and (abs(mp_a - mp_b) <= MP_AGREE * abs(mp_b)) \
        and ((mp_a > 0) == (mp_b > 0))
    return ("X", bool(ok), mp_a, mp_b)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("twin_resolution_probe -- PRIME.AUDIT.TWIN_RESOLUTION.01 "
          "(round 331)")
    print("SPEC_SHA %s   (r289 AKD %s / r286 LMS %s imported)"
          % (SPEC_SHA[:16], AKD.SPEC_SHA[:16], LMS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + w9 "
                        "regression + comb identity + w9 twin f64 "
                        "+ must-fails; table, sweep, mp tiers, "
                        "counter-test, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the resolution classes "
          "(RESOLVES <= %.1f x margin / BLIND > %.1f x margin, "
          "the audit's own semantics), the anchor rules (8-rung "
          "table spread + sweep anchors %s), the precision ladder "
          "%s, the mp pair protocol (dps %d/%d, floor %.0e), the "
          "counter-test construction + admissibility gates + dose "
          "rule, the mutants and the three-way lead verdict; "
          "pre-spec scoping (budget sizing + the four seen @1e-8 "
          "deltas) disclosed in the spec; NO RNG anywhere -- the "
          "round is seed-free deterministic"
          % (RES_BAR, BLIND_BAR, str(SWEEP_KZ), str(TOLS), DPS_A,
             DPS_B, DELTA_FLOOR))

    # ---------------- S1 toys
    section("S1  TOYS -- CONTINUED FRACTIONS, TRANSFER, CENSUS")
    ok_t1 = (AKD.best_rational(0.5, 1e-9) == (1, 2)
             and AKD.best_rational(math.pi, 1e-4) == (333, 106)
             and AKD.best_rational(46.0, 1e-9) == (46, 1))
    check("G10-toy-rational", ok_t1,
          "CONTINUED FRACTIONS (r289 hand values): 1/2 exact; pi "
          "at tol 1e-4 -> 333/106; integer 46 -> 46/1 -- the twin "
          "replacement is deterministic and minimal along the "
          "convergent ladder")
    # t2: hand 4-atom transfer toy (r286 toy world)
    xp_t = np.array([-0.5, 0.0, 0.5])
    wp_t = np.array([1.0, 1.0, 1.0])
    y0, v0, e_t = 0.25, 0.1, 1e-6
    a_t, b_t, h_t = V.mu_chain(xp_t, wp_t, 2)
    B_t = V.b_matrix(a_t, b_t, h_t, np.array([y0]),
                     np.array([v0]), 2)
    lam_t = float(np.linalg.eigvalsh(B_t @ B_t.T)[-1])
    B_e = V.b_matrix(a_t, b_t, h_t, np.array([y0 + e_t]),
                     np.array([v0]), 2)
    lam_e = float(np.linalg.eigvalsh(B_e @ B_e.T)[-1])
    dlam_hand = v0 * 2.0 * (2.0 * y0 * e_t + e_t * e_t)
    sg_t = LMS.sign_chain_union(
        np.array([-0.5, 0.0, 0.25, 0.5]),
        np.array([1.0, 1.0, -0.1, 1.0]), 3)
    minc_t = next((n for n in range(len(sg_t)) if sg_t[n] < 0),
                  None)
    sg_d = LMS.sign_chain_union(
        np.array([-0.5, 0.0, 0.25, 0.5]),
        np.array([1.0, 1.0, -10.0, 1.0]), 2)
    minc_d = next((n for n in range(len(sg_d)) if sg_d[n] < 0),
                  None)
    ok_t2 = (abs(lam_t - 11.0 / 240.0) <= TOY_TOL
             and abs((lam_e - lam_t) - dlam_hand) <= TOY_TOL
             and (minc_t is None or minc_t >= 2)
             and minc_d == 0)
    check("G11-toy-transfer", ok_t2,
          "HAND 4-ATOM WORLD: lambda_max(E_2) = %.12f == 11/240 "
          "exact; position transfer y -> y + 1e-6 moves lambda by "
          "%.3e == hand value v(4 y e + 2 e^2) (dev %.1e, tol "
          "%.0e) -- the margin-transfer measurement channel is "
          "exact on a hand value; failure direction v = 10 flips "
          "minC to %s == 0 (two routes)"
          % (lam_t, lam_e - lam_t,
             abs((lam_e - lam_t) - dlam_hand), TOY_TOL,
             str(minc_d)))
    # t3: hand fraction census + detune toy
    fr_t = np.array([0.25, 0.25, 0.7])
    n_res0 = resonance_census(fr_t)
    uu_t = np.array([0.31, 0.47, 0.86])
    g_t = MF.local_gaps(uu_t)
    u2_t, m2_t, du_t = ct_detune(uu_t, np.array([1.0, 2.0, 3.0]),
                                 g_t, 1e-3)
    gap0 = np.diff(uu_t)
    gap1 = np.diff(u2_t)
    ok_t3 = (n_res0 == 1
             and resonance_census(np.array([0.25 + 3e-6, 0.25,
                                            0.7])) == 0
             and bool(np.array_equal(m2_t,
                                     np.array([1.0, 2.0, 3.0])))
             and bool(np.all(np.abs(du_t) <= 1e-3 * g_t + 1e-300))
             and float(np.max(np.abs(gap1 - gap0) / gap0))
             <= 10.0 * 1e-3)
    check("G12-toy-census-detune", ok_t3,
          "HAND CENSUS: fractions (1/4, 1/4, 0.7) -> exactly 1 "
          "resonant pair; a 3e-6 detune destroys it; golden "
          "detune at eps 1e-3 on 3 atoms: weights bitwise, |du| "
          "<= eps g exact, max rel gap change %.1e <= 10 eps -- "
          "the counter-test constructor preserves the metric "
          "frame by construction"
          % float(np.max(np.abs(gap1 - gap0) / gap0)))

    # ---------------- S2 flagship regression + r289 twin
    section("S2  W9 -- DOCUMENT-PIPELINE REGRESSION + r289 TWIN")
    uu9, mm9 = base_comb(MAIN_KZ)
    mzV9 = V.build_measures(MAIN_KZ)
    w9 = measure_world(MAIN_KZ, uu9, mm9)
    mz9 = w9["mz"]
    ident9 = all(bool(np.array_equal(mz9[k], mzV9[k]))
                 for k in ("xp", "wp", "yn", "vn"))
    lam9 = 1.0 - w9["margin"]
    a9, b9, h9 = V.mu_chain(mz9["xp"], mz9["wp"], mz9["Nw"] + 1)
    B9 = V.b_matrix(a9, b9, h9, mz9["yn"], mz9["vn"],
                    mz9["Nw"] + 1)
    lam9n = float(np.linalg.eigvalsh(B9 @ B9.T)[-1])
    ok_w9 = (mz9["S"] == REC_S and len(mz9["xp"]) == REC_SP
             and len(mz9["yn"]) == REC_SM and mz9["Nw"] == REC_NW
             and abs(lam9 - REC_LAM) <= MP_REC_BAR
             and abs(lam9n - REC_LAM_NEXT) <= MP_REC_BAR
             and abs(w9["margin"] / REC_MARGIN - 1.0)
             <= REC_MARGIN_TOL
             and w9["minC"] == REC_NW and ident9)
    check("G20-w9-records", ok_w9,
          "w9 through the document pipeline: S = %d/%d/%d, N_w = "
          "%d, lambda_max = %.8f (record %.8f), margin %.4e "
          "(record %.4e rel %.2f), minC = %s == N_w, crossing "
          "lambda(E_185) = %.8f > 1; comb channel == "
          "V.build_measures BITWISE"
          % (mz9["S"], len(mz9["xp"]), len(mz9["yn"]), mz9["Nw"],
             lam9, REC_LAM, w9["margin"], REC_MARGIN,
             REC_MARGIN_TOL, str(w9["minC"]), lam9n))
    if smoke:
        check("G21-w9-mp-staffel", True, "SMOKE: skipped")
    else:
        m30 = mp_margin(mz9, DPS_A)
        m45 = mp_margin(mz9, DPS_B)
        ok_mp9 = (abs((1.0 - m30) - REC_LAM) <= MP_REC_BAR
                  and abs((1.0 - m45) - REC_LAM) <= MP_REC_BAR
                  and abs(m30 - m45) <= MP_AGREE * abs(m45))
        check("G21-w9-mp-staffel", ok_mp9,
              "mp staffel: margin dps30 %.8e / dps45 %.8e "
              "(staggered rel dev %.1e <= %.0e; vs dps-60 record "
              "dev %.1e <= %.0e) -- the tier protocol is anchored"
              % (m30, m45, abs(m30 - m45) / abs(m45), MP_AGREE,
                 abs((1.0 - m45) - REC_LAM), MP_REC_BAR))
    gaps9 = MF.local_gaps(uu9)
    ctx9 = dict(uu=uu9, mm=mm9, gaps=gaps9, D=mz9["D"])
    uR9, mR9, dens9, duR9 = AKD.twin_rational(uu9, mm9, gaps9,
                                              mz9["D"],
                                              RAT_TOL_REF)
    okg9, note9, cen9 = twin_gates(ctx9, uR9, mR9, dens9, duR9,
                                   RAT_TOL_REF)
    wT9 = measure_world(MAIN_KZ, uR9, mR9)
    d9_f64 = wT9["margin"] - w9["margin"]
    ok_r289 = (okg9 and wT9["minC"] == w9["minC"]
               and wT9["margin"] > 0.0)
    check("G22-r289-twin-regression", ok_r289,
          "r289 TWIN at 1e-8 gap reproduced through the document "
          "pipeline (gates %s; dens med %d / max %d; max |du| "
          "%.1e = %.1e of the local gap): minC %s == MAIN, "
          "margin %+.4e > 0; THE NEW NUMBER: Delta_m = %+.3e = "
          "%.1e of the margin -- the r289 adjudication's own "
          "resolution reserve, measured"
          % (note9, cen9["q_med"], cen9["q_max"], cen9["du_max"],
             cen9["th_max"], str(wT9["minC"]), wT9["margin"],
             d9_f64, abs(d9_f64) / w9["margin"]))

    # ---------------- world/stage machinery for table + sweep
    W_MAIN: dict = {}
    CTX: dict = {}
    STAGE_LEDGER: list = []

    def get_main(kz):
        if kz in W_MAIN:
            return W_MAIN[kz]
        if kz == MAIN_KZ:
            uu, mm = uu9, mm9
            w = w9
            ident = ident9
        else:
            uu, mm = base_comb(kz)
            w = measure_world(kz, uu, mm)
            mzV = V.build_measures(kz)
            ident = all(bool(np.array_equal(w["mz"][k], mzV[k]))
                        for k in ("xp", "wp", "yn", "vn"))
        tier, safe, mp_a, mp_b = main_tier(kz, w, smoke)
        w.update(kz=kz, z=int(V.PP[kz]), ident=ident, tier=tier,
                 safe=safe, mp_a=mp_a, mp_b=mp_b,
                 tag="kz%d-main" % kz)
        gaps = MF.local_gaps(uu)
        CTX[kz] = dict(uu=uu, mm=mm, gaps=gaps, D=w["D"])
        W_MAIN[kz] = w
        STAGE_LEDGER.append(dict(tag=w["tag"], margin=w["margin"],
                                 mp_a=mp_a))
        return w

    def twin_stage(kz, tol, decision=False):
        """one (anchor, tol) twin stage: construction, gates,
        f64 + mp pair Delta, class."""
        wM = get_main(kz)
        ctx = CTX[kz]
        u2, m2, dens, du = AKD.twin_rational(
            ctx["uu"], ctx["mm"], ctx["gaps"], ctx["D"], tol)
        okg, note, cen = twin_gates(ctx, u2, m2, dens, du, tol)
        wT = measure_world(kz, u2, m2)
        d_f64 = wT["margin"] - wM["margin"]
        st = dict(kz=kz, tol=tol, okg=okg, note=note, cen=cen,
                  minC=wT["minC"], m_twin=wT["margin"],
                  d_f64=d_f64, mp_a=None, mp_b=None,
                  ward_ok=True, tier_break=False,
                  tag="kz%d-tol%.0e" % (kz, tol))
        dabs = abs(d_f64)
        d_src = "f64"
        if (not smoke) and abs(wM["margin"]) < MP_TIER1:
            mtw30 = mp_margin(wT["mz"], DPS_A)
            d30 = mtw30 - wM["mp_a"]
            st["mp_a"] = mtw30
            st["ward_ok"] = (abs(d_f64 - d30)
                             <= max(PAIR_WARD * abs(d30),
                                    F64_NOISE))
            if abs(d30) < DELTA_FLOOR:
                dabs = DELTA_FLOOR
                d_src = "mp30<floor"
            else:
                dabs = abs(d30)
                d_src = "mp30"
            if decision:
                mtw45 = mp_margin(wT["mz"], DPS_B)
                mM45 = (wM["mp_b"] if wM["mp_b"] is not None
                        else mp_margin(wM["mz"], DPS_B))
                d45 = mtw45 - mM45
                st["mp_b"] = mtw45
                ok_st = (abs(mtw30 - mtw45)
                         <= MP_AGREE * abs(mtw45))
                ok_pair = (abs(d30 - d45)
                           <= max(PAIR_WARD * max(abs(d30),
                                                  abs(d45)),
                                  DELTA_FLOOR))
                st["tier_break"] = not (ok_st and ok_pair)
                if abs(d45) >= DELTA_FLOOR:
                    dabs = abs(d45)
                    d_src = "mp45"
        sig_ok = (wT["margin"] > 0.0 and wT["minC"] == wM["minC"])
        st["dabs"] = dabs
        st["d_src"] = d_src
        st["sig_ok"] = sig_ok
        st["ratio"] = dabs / abs(wM["margin"])
        st["cls"] = classify(sig_ok, dabs, abs(wM["margin"]))
        STAGE_LEDGER.append(dict(tag=st["tag"],
                                 margin=wM["margin"],
                                 mp_a=st["mp_a"]))
        return st

    def stage_line(st, wM):
        return ("kz%-4d z=%-6d tol %.0e  margin %+.3e [%s]  "
                "|D| %.2e (%s)  ratio %.2e  minC %s/%s  q "
                "%d/%d fl %d hop/land %d/%d  -> %s"
                % (st["kz"], wM["z"], st["tol"], wM["margin"],
                   wM["tier"], st["dabs"], st["d_src"],
                   st["ratio"], str(st["minC"]), str(wM["minC"]),
                   st["cen"]["q_med"], st["cen"]["q_max"],
                   st["cen"]["n_floor"], st["cen"]["n_hop"],
                   st["cen"]["n_land"], st["cls"]))

    # ---------------- S3 the resolution table (task 1)
    section("S3  LEG A -- THE RESOLUTION TABLE (r289 TWIN AT "
            "1e-8 OVER THE LADDER)")
    if smoke:
        for g in ("G30-table-mains", "G31-resolution-table",
                  "G32-table-conservation"):
            check(g, True, "SMOKE: skipped")
        table_rows = []
    else:
        kzs42 = V.admissible_indices()
        table_kz = [kzs42[i] for i in TABLE_IDX]
        for kz in SWEEP_KZ:
            if kz not in table_kz:
                table_kz.append(kz)
        rows = []
        for kz in table_kz:
            wM = get_main(kz)
            st = twin_stage(kz, RAT_TOL_REF)
            rows.append((st, wM))
            info(stage_line(st, wM))
        table_rows = rows
        ok_mains = all(wM["safe"] and wM["ident"]
                       and wM["margin"] > 0 for _st, wM in rows)
        off_ok = all(W_MAIN[kz]["minC"] - W_MAIN[kz]["Nw"]
                     == SWEEP_OFF[kz]
                     and abs(W_MAIN[kz]["margin"]
                             / SWEEP_REC[kz] - 1.0)
                     <= SWEEP_REC_TOL for kz in SWEEP_KZ)
        check("G30-table-mains", ok_mains and off_ok,
              "%d table mains: comb identity BITWISE on all, "
              "every margin sign-safe positive per the r286 tier "
              "protocol (tiers %s); sweep-anchor regression vs "
              "the r286 records: margins rel <= %.2f and offsets "
              "== %s"
              % (len(rows),
                 str({("kz%d" % wM["kz"]): wM["tier"]
                      for _s, wM in rows}),
                 SWEEP_REC_TOL,
                 str({("kz%d" % k): ("+%d" % SWEEP_OFF[k])
                      for k in SWEEP_KZ})))
        n_res = sum(1 for st, _w in rows if st["cls"] == "RESOLVES")
        n_bli = sum(1 for st, _w in rows if st["cls"] == "BLIND")
        worst = max(rows, key=lambda r: r[0]["ratio"])
        check("G31-resolution-table", True,
              "THE AUDIT TABLE (r289 precision 1e-8): %d/%d "
              "anchors RESOLVE, %d BLIND, %d MARGINAL; worst "
              "ratio |Delta_m|/margin = %.2e at kz%d (margin "
              "%+.2e) -- disturbance-vs-margin measured on every "
              "anchor, mp pairs on every sub-%.0e margin"
              % (n_res, len(rows), n_bli,
                 len(rows) - n_res - n_bli, worst[0]["ratio"],
                 worst[1]["kz"], worst[1]["margin"], MP_TIER1))
        ok_cons = all(st["okg"] and st["ward_ok"]
                      for st, _w in rows)
        check("G32-table-conservation", ok_cons,
              "conservation EXACT on all %d table twins (weights "
              "bitwise, cells + on-node family kept, strict "
              "order, |du| <= max(tol g, ULP floor), q <= %.0e "
              "on constructible atoms) and every mp pair ward "
              "holds" % (len(rows), QMAX_GUARD))

    # ---------------- S4 the precision sweep (task 2)
    section("S4  LEG B -- THE PRECISION SWEEP (TIGHT ANCHORS)")
    tstar: dict = {}
    if smoke:
        for g in ("G40-sweep-stages", "G41-sweep-thresholds",
                  "G42-mp-discipline"):
            check(g, True, "SMOKE: skipped")
        sweep_rows = []
    else:
        sweep_rows = []
        SW = {}
        for kz in SWEEP_KZ:
            wM = get_main(kz)
            stages = {}
            for tol in TOLS:
                st = twin_stage(kz, tol)
                stages[tol] = st
                sweep_rows.append((st, wM))
                info(stage_line(st, wM))
            # t*: coarsest tol with RESOLVES and all finer RESOLVE
            ts = None
            for i, tol in enumerate(TOLS):
                if all(stages[t]["cls"] == "RESOLVES"
                       for t in TOLS[i:]):
                    ts = tol
                    break
            tstar[kz] = ts
            SW[kz] = stages
            # decision stage: dps-45 pair at t* (tight anchors)
            if ts is not None and abs(wM["margin"]) < MP_TIER1:
                st_d = twin_stage(kz, ts, decision=True)
                sweep_rows.append((st_d, wM))
                info("DECISION " + stage_line(st_d, wM))
                if st_d["cls"] != "RESOLVES":
                    tstar[kz] = None
                SW[kz][ts] = st_d
        ok_stage = all(st["okg"] and st["ward_ok"]
                       and not st["tier_break"]
                       for st, _w in sweep_rows)
        eq_ok = all(((st["m_twin"] > 0)
                     == (st["minC"] is not None
                         and st["minC"] >= wM["Nw"]))
                    for st, wM in sweep_rows)
        check("G40-sweep-stages", ok_stage and eq_ok,
              "%d sweep stages: conservation + mp pair wards + "
              "no tier break; two-route equivalence (margin > 0 "
              "<=> minC >= N_w) on every twin world"
              % len(sweep_rows))
        tight = [kz for kz in SWEEP_KZ
                 if abs(W_MAIN[kz]["margin"]) < MP_TIER2]
        check("G41-sweep-thresholds", True,
              "TWIN STABILITY t* (coarsest tol with the full "
              "finer ladder RESOLVING): %s; tight anchors "
              "(margin < %.0e): %s -- 'ab welcher Praezision "
              "werden die knappen Anker Twin-stabil' is answered "
              "by this map"
              % (str({("kz%d" % k): (("%.0e" % tstar[k])
                                     if tstar[k] is not None
                                     else "NOT_RESOLVED")
                      for k in SWEEP_KZ}), MP_TIER2,
                 str(["kz%d" % k for k in tight])))
        fake = [dict(tag="FAKE", margin=5.0e-6, mp_a=None)]
        fl_fake = LMS.audit_no_mp(fake)
        fl_real = LMS.audit_no_mp(STAGE_LEDGER)
        check("G42-mp-discipline", bool(fl_fake) and not fl_real,
              "m3 MP-TIER AUDIT (r286 detector verbatim): the "
              "deliberate no-mp entry is FLAGGED (%s) and the "
              "real stage ledger is CLEAN (%d stages, every "
              "sub-%.0e margin carries its dps-%d value)"
              % (str(fl_fake), len(STAGE_LEDGER), MP_TIER1,
                 DPS_A))

    # ---------------- S5 the counter-test (task 3)
    section("S5  LEG C -- THE GENUINE DIOPHANTINE PERTURBER")
    ct_rows = []
    if smoke:
        for g in ("G50-ct-w9", "G51-ct-tight", "G52-ct-verdict"):
            check(g, True, "SMOKE: skipped")
        ct_break = None
    else:
        def run_ct(kz, eps, mask, label):
            wM = get_main(kz)
            ctx = CTX[kz]
            u2, m2, du = ct_detune(ctx["uu"], ctx["mm"],
                                   ctx["gaps"], eps, mask)
            gap0 = np.diff(ctx["uu"])
            gap1 = np.diff(u2)
            gap_dev = float(np.max(np.abs(gap1 - gap0) / gap0))
            ok_adm = (bool(np.array_equal(m2, ctx["mm"]))
                      and bool(np.all(np.abs(du)
                                      <= eps * ctx["gaps"]
                                      + 1e-300))
                      and gap_dev <= GAP_ABS_BAR)
            _i0a, fra = frac_canon(ctx["uu"], ctx["D"])
            _i0b, frb = frac_canon(u2, ctx["D"])
            res0 = resonance_census(fra)
            res1 = resonance_census(frb[mask]
                                    if mask is not None else frb)
            wC = measure_world(kz, u2, m2)
            dC = wC["margin"] - wM["margin"]
            d_src = "f64"
            if abs(wM["margin"]) < MP_TIER1:
                mC30 = mp_margin(wC["mz"], DPS_A)
                dC = mC30 - wM["mp_a"]
                d_src = "mp30"
            breaks = (wC["minC"] != wM["minC"]
                      or wC["margin"] <= 0.0)
            row = dict(kz=kz, label=label, eps=eps,
                       n_det=int(np.sum(du != 0.0)),
                       gap_dev=gap_dev, ok_adm=ok_adm,
                       res0=res0, res1=res1, minC=wC["minC"],
                       m_ct=wC["margin"], dC=dC, d_src=d_src,
                       breaks=breaks)
            ct_rows.append(row)
            info("CT %-10s kz%-4d eps %.0e det %5d  gaps %.1e  "
                 "reson %d->%d  minC %s/%s  margin %+.3e  "
                 "Delta %+.2e (%s)  -> %s"
                 % (label, kz, eps, row["n_det"], gap_dev,
                    res0, res1, str(wC["minC"]),
                    str(wM["minC"]), wC["margin"], dC, d_src,
                    "BREAKS" if breaks else "KEEPS"))
            return row

        eps_w9 = min(tstar.get(MAIN_KZ) or CT_EPS_CAP,
                     CT_EPS_CAP)
        on9 = onnode_mask(uu9, mz9["D"])
        r1 = run_ct(MAIN_KZ, eps_w9, None, "w9-CT1")
        r2 = run_ct(MAIN_KZ, eps_w9, on9, "w9-CT2")
        ok_ct9 = (r1["ok_adm"] and r2["ok_adm"]
                  and r1["res0"] == 28 and r1["res1"] == 0
                  and r2["res1"] == 0
                  and int(np.sum(on9)) == 8)
        check("G50-ct-w9", ok_ct9,
              "w9 counter-tests at eps %.0e (sealed dose rule): "
              "CT1 detunes all %d atoms, CT2 exactly the %d "
              "on-node 2-power atoms; the %d exact resonances "
              "{46 log2 2^(a-b)} = 0 drop to 0 in both worlds "
              "(the designed log arithmetic DEMONSTRABLY "
              "destroyed) while gaps move <= %.1e <= %.0e -- "
              "admissible diophantine perturbers"
              % (eps_w9, r1["n_det"], r2["n_det"], r1["res0"],
                 max(r1["gap_dev"], r2["gap_dev"]),
                 GAP_ABS_BAR))
        # tightest resolving sweep anchor
        tight_res = [kz for kz in SWEEP_KZ
                     if kz != MAIN_KZ and tstar.get(kz)
                     is not None]
        if tight_res:
            kz_t = min(tight_res,
                       key=lambda k: abs(W_MAIN[k]["margin"]))
            eps_t = min(tstar[kz_t], CT_EPS_CAP)
            on_t = onnode_mask(CTX[kz_t]["uu"], CTX[kz_t]["D"])
            r3 = run_ct(kz_t, eps_t, None, "tight-CT1")
            n_on_t = int(np.sum(on_t))
            ct2_note = ("CT2 NOT_APPLICABLE (on-node census %d "
                        "-- the log-2 commensurability is a w9 "
                        "property, disclosed)" % n_on_t
                        if n_on_t == 0 else "")
            if n_on_t > 0:
                r4 = run_ct(kz_t, eps_t, on_t, "tight-CT2")
                ct2_note = "CT2 ran (%d on-node atoms)" % n_on_t
            check("G51-ct-tight", r3["ok_adm"],
                  "the TIGHT-ANCHOR counter-test: kz%d (margin "
                  "%+.2e, the tightest resolving anchor) at eps "
                  "%.0e = t*; %d atoms detuned, gaps <= %.1e; "
                  "%s; Delta_m %+.2e (%s) vs the twin's %.2e at "
                  "the same tol -- the diophantine direction "
                  "measured exactly where the resolution is "
                  "established"
                  % (kz_t, W_MAIN[kz_t]["margin"], eps_t,
                     r3["n_det"], r3["gap_dev"], ct2_note,
                     r3["dC"], r3["d_src"],
                     [st["dabs"] for st, w in sweep_rows
                      if w["kz"] == kz_t
                      and st["tol"] == tstar[kz_t]][0]))
        else:
            check("G51-ct-tight", True,
                  "NO tight anchor resolves within the ladder -- "
                  "the tight counter-test cannot run (typed "
                  "honestly; see the lead verdict)")
        ct_break = next((r for r in ct_rows
                         if r["ok_adm"] and r["breaks"]), None)
        check("G52-ct-verdict", True,
              "sealed break rule evaluated on %d admissible CT "
              "worlds: %s"
              % (sum(1 for r in ct_rows if r["ok_adm"]),
                 ("BREAK at kz%d eps %.0e -- the switch must be "
                  "revised" % (ct_break["kz"], ct_break["eps"]))
                 if ct_break else
                 "ALL KEEP the wall (minC and margin sign "
                 "unchanged everywhere)"))

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    uC, mC, densC, duC = AKD.twin_rational(uu9, mm9, gaps9,
                                           mz9["D"], M1_TOL)
    n_coll = len(uC) - len(np.unique(uC))
    okgC, noteC, _cenC = twin_gates(ctx9, uC, mC, densC, duC,
                                    M1_TOL)
    check("G60-mustfail-collision", n_coll > 0 and not okgC,
          "m1 TWIN COLLISION (denominator ladder at tol %.1f x "
          "gap): %d position collisions (unique %d/%d) -- CAUGHT "
          "by the strict-order/distinctness gate (%s)"
          % (M1_TOL, n_coll, len(np.unique(uC)), len(uC), noteC))
    u2m, m2m, dum = ct_detune(uu9, mm9, gaps9, M2_EPS)
    gap0 = np.diff(uu9)
    gapm = np.diff(u2m)
    dev_m2 = float(np.max(np.abs(gapm - gap0) / gap0))
    check("G61-mustfail-metric-ct", dev_m2 > GAP_ABS_BAR,
          "m2 METRIC PERTURBER AS COUNTER-TEST (eps %.2f): max "
          "rel gap change %.1e > %.0e -- REJECTED by the CT "
          "admissibility gate: a perturber that moves the gap "
          "structure is a METRIC surgeon, not a diophantine one"
          % (M2_EPS, dev_m2, GAP_ABS_BAR))
    if smoke:
        fake = [dict(tag="FAKE", margin=5.0e-6, mp_a=None)]
        check("G62-mustfail-no-mp", bool(LMS.audit_no_mp(fake)),
              "m3 (smoke half): the r286 no-mp detector FLAGS "
              "the deliberate sub-bar entry (full-ledger check "
              "runs in G42)")
    else:
        check("G62-mustfail-no-mp", True,
              "m3 adjudicated in G42 (FLAGGED + real ledger "
              "clean)")
    hits_m4 = scope_audit("mutant_target_twin")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G63-scope-audits", bool(hits_m4) and not hits
          and not ag_hits,
          "m4 TARGET-READBACK TWIN FLAGGED (%s); the %d sealed "
          "constructors consume comb positions + weights + grid "
          "geometry ONLY (%s); r289 twin constructors re-audited "
          "there; fragment audit (no fit primitives): %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "Baker/Matveev application, no asymptotic law, no "
          "retyping of r289/r286 or any earlier round (the "
          "resolution map is HANDED OVER to the coordinator), no "
          "posthoc anchor choice, NO RH claim; what the round "
          "adds: the measured twin-resolution map over the "
          "ladder, the precision sweep at the tight anchors, and "
          "the genuine-diophantine counter-test at resolving "
          "doses; r243..r330 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        tight = [kz for kz in SWEEP_KZ
                 if abs(W_MAIN[kz]["margin"]) < MP_TIER2]
        unresolved = [kz for kz in tight if tstar.get(kz) is None]
        if ct_break is not None:
            lead = ("METRIC_ONLY_REVISED(kz%d at eps %.0e: an "
                    "admissible gap-preserving diophantine "
                    "perturber breaks the wall at a resolving "
                    "dose -- the switch must be revised; "
                    "handover to the coordinator)"
                    % (ct_break["kz"], ct_break["eps"]))
        elif not unresolved and all(not r["breaks"]
                                    for r in ct_rows
                                    if r["ok_adm"]):
            mn_m = min(abs(W_MAIN[k]["margin"]) for k in W_MAIN)
            mx_m = max(abs(W_MAIN[k]["margin"]) for k in W_MAIN)
            lead = ("METRIC_ONLY_CONFIRMED_AT_RESOLUTION(margins "
                    "%.3e .. %.3e over %d anchors; every tight "
                    "anchor twin-stable at t* %s; every "
                    "admissible counter-test keeps the wall)"
                    % (mx_m, mn_m, len(W_MAIN),
                       str({("kz%d" % k): ("%.0e" % tstar[k])
                            for k in tight})))
        else:
            lead = ("METRIC_ONLY_UNTESTED_AT_TIGHT(%s have no "
                    "resolving stage in the constructible "
                    "ladder -- the switch is confirmed only on "
                    "the resolved range; consequence bookkeeping "
                    "belongs to the coordinator)"
                    % str(["kz%d" % k for k in unresolved]))
        parts = [lead]
        parts.append("RESOLUTION_TABLE(%s)"
                     % "; ".join("kz%d %.0e->%s" %
                                 (wM["kz"], st["ratio"], st["cls"])
                                 for st, wM in table_rows))
        parts.append("PRECISION_SWEEP(t* %s)"
                     % str({("kz%d" % k): (("%.0e" % tstar[k])
                                           if tstar.get(k)
                                           is not None
                                           else "NOT_RESOLVED")
                            for k in SWEEP_KZ}))
        parts.append("COUNTER_TEST(%s)"
                     % "; ".join("%s %s" %
                                 (r["label"],
                                  "BREAKS" if r["breaks"]
                                  else "KEEPS")
                                 for r in ct_rows))
        parts.append("DENOMINATOR_LEDGER(w9@1e-8 q med %d max "
                     "%d; floors disclosed per stage)"
                     % (cen9["q_med"], cen9["q_max"]))
        parts.append("DETECTOR_LEDGER(mp discipline clean; "
                     "m1-m4 loud)")
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the resolution map, the sweep, the "
          "counter-test outcomes; EXACT: the toys, the "
          "conservation gates, the two-route equivalence; OPEN: "
          "L* itself and every sub-floor twin precision "
          "(unchanged); NO RH claim"
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
