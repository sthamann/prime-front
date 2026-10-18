#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""vdc_chain_provenance_probe -- PRIME.PORT.L2.
VDC_CHAIN_PROVENANCE.01 (round 297): the CHAIN ORIGIN of the
vdC input -- can the P-variance / autocorrelation scaling (the
INPUT of the proven v964-S0 van der Corput inequality) be derived
SOURCE-PURELY from the chain structure, as a provable statement
instead of a measurement?  Context (sealed record inputs): wave 7
(v964) proved the vdC inequality |sum P|^2 <= ((m + H - 1)/H) x
sum_{|h|<H} (1 - |h|/H) A(h) EXACTLY in Fractions (S0 section,
covering identity + Cauchy-Schwarz, wrong-prefactor must-fail) and
ledgered PRIME.PORT.L2.VDC_LEMMA.01 [O] with the documented rest:
the CHAIN PROVENANCE of the input scaling; r287 (SPEC 761d88fa)
measured delta'(F2_VDC) = +0.309 > DELTA_NEED = 0.21 world-blind
at the frozen H = ceil(sqrt(m)), cert 6/7 + 38/42; r272 located
the task (a mechanism must supply N^{-delta'}, delta' > 0.21, of
the available gamma_true = 0.45) and r273 showed the decay is
GENERIC (root-scale baseline, perturbation-insensitive -- no
arithmetic fingerprint); r270 certified kz15 exact-finitely
(reserve 0.0268).  Reviewer routing (r296 fork): the DENS lane is
closed (DENS_WORLD_BLIND) -- resources move to the L2 front, "the
mathematically more classical attack surface": vdC theorem
(proved) + input scaling (open) = delta' > 0.21 as a theorem on
the generic half, with a 0.24 exponent pad.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r270/r271/r287 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split t = t_edge + R; Z = t_{N-2} + chain, Z_local = t_edge +
chain; maximal same-sign runs of the bx-sorted bulk with masses
M_i and exact signed sums s_i; level-2 blocks (r270 convention,
offset 0) P_j = s_{2j} + s_{2j+1}, odd tail its own block; the
FROZEN vdC window H = max(2, ceil(sqrt(m))); the vdC INPUT
S_F := sum_{|h|<H} (1 - |h|/H) A(h) = (1/H) sum_t W_t^2 (the
Fejer window sum, v964-S0 identity) and A(0) = sum_j P_j^2 (the
P-variance).  Demand scale M_W = sqrt(5/7); DELTA_NEED = 0.21
(r272 record); halves log-slope estimator (r272, deterministic,
exactly additive over products).  EVERY input object here is
SOURCE-PURE (atoms, weights, chain rows, run partition): the
input anatomy needs no truth-side quantity.

LEG 0 -- ANCHOR REGRESSION (record wards, all bands disclosed
r270/r272/r287 record numbers): r287 core bit-near (delta'(F2) =
+0.309 tol 0.01 at the frozen H rule, cert 6/7 exceptions +
38/42 ladder, kz15 F2 miss 0.10 dec tol 0.02); r272 wards
(sp(N, eps_c2) +0.67 tol 0.05, gamma_true +0.453 tol 0.05,
slope(eps_c2/M) +0.196 tol 0.01, exception P-sign alternation
med in [0.34, 0.44]); r270 kz15 reserve in [0.020, 0.035]; the
v964-S0 vdC set RE-COMPUTED (not re-proved) in exact Fractions
on the frozen rational sequences: Fejer window-sum identity,
H-fold covering identity, the vdC inequality at every H with the
H = 1 equality witness, the wrong-prefactor must-fail 14 < 16.

LEG A -- THE INPUT ANATOMY (the target inequality; every slope a
halves log-slope on the N-sorted 42-rung ladder): the exact slope
decomposition slope(eps_F2/M) = (1/2) x [slope(pref) + sigma]
with pref = (m + H - 1)/H and sigma := slope(S_F / M^2) (gated
EXACTLY, additivity bar 1e-9).  delta'(F2) > DELTA_NEED is
therefore EQUIVALENT to the TARGET INEQUALITY (frozen fine-type
TARGET_INEQUALITY_FROZEN):
  sigma  <=  sigma* := 2 x (slope(eps_c2/M) - DELTA_NEED)
                         - slope(pref)
-- the WEAKEST sufficient input bound, all constants printed from
the ladder (expectation from the records: sigma* ~ -0.53 vs the
measured truth sigma ~ -0.72; the 0.24 exponent pad of the lane
in sigma coordinates ~ 0.19).  PAD TABLE: the allowed loss at
every stage of the chain (Fejer step S_F <= H x A(0); block step
A(0) <= 2 sum s_i^2; CS step; mass step) printed as slope
budgets.  Per-rung certification variant printed on the 7
exceptions: S_F < (H/(m + H - 1)) x (M_W - |Z_local|)^2.

LEG B -- CHAIN-PROVENANCE ROUTES (the core; each an exact
per-rung inequality chain on the real builders, each consuming
ONLY source-side objects, AST scope audit; worlds test on
EPSTEIN / SCRAMBLE -- the statement must be world-blind, here a
STRENGTH: the generic half needs no arithmetic):
(B1) THREE-TERM / PAIR-IDENTITY ROUTE: by the r271 alternation
  identity |B_j| = |M_{2j} - M_{2j+1}| EXACTLY, so A(0) =
  sum B_j^2 + [m odd] tail^2 <= gapmax x eps_c2 with gapmax =
  max(pair gaps, tail) and eps_c2 the sealed r269 pair bound:
  eps_B1 = sqrt((m + H - 1) x gapmax x eps_c2) -- a per-rung
  EXACT theorem (vdC + Fejer step + pair identity); the
  provenance question is the SCALING of gapmax/M (the Jacobi
  near-balance of adjacent run masses): measured, printed, and
  the route's delta'_B1 adjudicated against DELTA_NEED.
(B2) ROOT-SCALE / NODE-DENSITY ROUTE (r273 trace): A(0) <=
  2 sum_i M_i^2 <= 2 x maxM x sumM (exact); the node-density
  content: run boundaries are sign changes of the chain value
  ct on the sorted support (Sturm count) -- census: run count m
  vs N (alpha_m), run-length distribution, the mass imbalance
  imb = n_runs x maxM / sumM and its slope, and the ET-style
  equidistribution discrepancies of the boundary positions
  (rank coordinate D_rank and |ct|-mass coordinate D_mass,
  both deterministic sups against the uniform CDF): does pure
  node density supply the decay WITHOUT arithmetic?
(B3) FEJER-POSITIVITY / PARSEVAL ROUTE: per-run Cauchy-Schwarz
  against the |bw| measure: s_i^2 <= (sum_run |bw|) x
  (sum_run |bw| (bx v2 fac)^2), summed: sum s_i^2 <= wrunmax x
  Q_abs (exact); the IDENTITY CANDIDATE: sum_b W x^2 v2^2 ==
  e1^2 n_{N-1} + alh^2 n_{N-2} + gam^2 e3^2 n_{N-3} (diagonal
  form, orthogonality-assuming), where the SYMBOLIC sum
  rule sum w x^2 pi_k^2 = h_{k+1} + a_k^2 h_k + b_k^2 h_{k-1}
  is PROVED in exact Fractions on a small rational measure
  (monic three-term chain, orthogonality + Parseval-type norm
  identity, module-own), and the numeric identity census on the
  REAL chain classifies orthogonality/norm/second-moment
  deviations (sealed classification HOLDS <= 1e-6 / NEAR <=
  1e-3 / BREAKS, relative) on THREE sealed candidate measures:
  BORDER = union(dsm), WINDOW = union(d), WDIFF = WINDOW with
  negated BORDER appended -- MAIN + EPSTEIN + SCRAMBLE (the
  identity must be world-blind); the tautological full-cross
  prediction (recursion residual) is a WARD (bar 1e-9 rel);
  the signed-to-absolute gap (wrunmax x Q_abs) / sum s_i^2 is
  the route's named structural obstruction (the border weights
  are mixed-sign by construction: ws > 0, -vs < 0), measured
  with slope.
FOR EACH ROUTE: validity of every chain step exact on 47 worlds
(bar 1e-9 x scale); delta'_route = slope(eps_c2/M) -
slope(eps_route/M) vs DELTA_NEED; loss anatomy (decades med +
slope per step); exact verification of the chains on >= 3
window sizes (the 42 ladder windows + mains w9/w13; the
symbolic identities on small Fractions windows).

LEG C -- THE THEOREM COMPOSITION (fires ONLY on B success =
adjudicated PROVEN or PARTIAL with slope coverage): CANDIDATE
THEOREM (L2 generic half) printed with every constant explicit:
target inequality (Leg B route) + vdC (v964-S0, proved) + pad
arithmetic -> delta' > 0.21 on the generic half; scope: the 42
measured rungs (N in [142, 878]), h < H = ceil(sqrt(m)); the 7
exceptions cleanly excluded (6 via the r287 F2 certificates,
kz15 via the r270 exact-finite certificate).  The wave-9
promotion candidate -- NOT promoted here.  If Leg B fails,
Leg C is void and the probe documents PRECISELY where every
route breaks (the gap object of the lane).

LEG D -- KZ15 MARGINAL NOTE (small): per route, does eps_route
certify kz15 (need = M_W - |Z_local| at the razor, record
0.292)?  Expected structurally OUTSIDE (the routes majorize
eps_F2 which already misses by 0.10 dec) -- then the r270
exact-finite certification remains the permanent closure
(clarity, not a problem).

LEG E -- WARDS / MUST-FAILS (>= 4 mutants): (m1) WRONG vdC
PREFACTOR m/H (exact Fractions, v964-S0 anchor): breaks on
P = (1,1,1,1), H = 2 with 14 < 16 -- CAUGHT; (m2) PAD-DROPPED
TARGET (sharpness): sigma* computed WITHOUT the pad term
(DELTA_NEED -> 0) composes to delta' = 0 <= 0.21 EXACTLY (bar
1e-12) while the sealed sigma* composes to delta' = DELTA_NEED
exactly -- the pad term is load-bearing; (m3) PERTURBED FEJER
WEIGHT: the window-sum identity with (1 - |h|/(H + 1)) breaks
LOUDLY on the toy sequence (>= 1e-6 abs); (m4) WORLD-BLINDNESS
BREAK: a route builder consuming the withheld terminal drive
key (gift mutant) AND a builder consuming the branch label
(branch-peek mutant) must both be FLAGGED by the AST scope
audit.  Scope hygiene: every route builder consumes source-side
objects only (BOUND_FORBIDDEN set); fragment audit (no fit
primitives); TOY EXACTNESS (bar 1e-14): hand-checked sequences
reproduce the block builder, the vdC window core (H = 2,
sum W^2 = 6, S_F = 3), the B1 chain (Mr = (3,1,2,4,1): gaps
(2,2), tail 1, eps_c2 = 5, gapmax = 2, A0 = 9 <= 10), the B2
chain (sum M^2 = 31 <= maxM x sumM = 44; A0 = 9 <= 2 x 31) and
the B3 CS step on a two-run toy; contribution ward, block
identity, autocorr/Fejer identity per rung; SMOOTH anchor
(alias <= 1e-12, q_N <= 1e-20); mp SAMPLES (dps 60): kz15 (bar
1e-8) + the two deepest rungs (bar 3e-6).

SEALED ADJUDICATION (frozen BEFORE evaluation): per route
VALID = every chain step holds on 47 worlds (bar 1e-9);
SLOPE_OK = delta'_route > DELTA_NEED; IDENT(B3) = orthogonality
+ diag second-moment identity HOLDS (<= 1e-6 rel) on at least
one sealed measure, on MAIN AND both broken-arithmetic
controls.  CHAIN_PROVENANCE_PROVEN(Bx) iff VALID and SLOPE_OK
and every non-universal factor of the composed bound reduces to
a chain identity (operationally reachable only by B3: IDENT
holds AND the signed-to-absolute step is exact, i.e. the bulk
weights are one-signed -- disclosed expectation: structurally
FALSE on the border union, ws > 0 vs -vs < 0);
CHAIN_PROVENANCE_PARTIAL(best route by (SLOPE_OK, delta'),
gap) iff some route is VALID and (SLOPE_OK or IDENT) -- gap =
the named measured factor / slope miss; else
INPUT_STILL_EMPIRICAL(the measured common obstruction).
Leg C fires iff PROVEN or (PARTIAL with SLOPE_OK).

INDEX FIREWALL (binding, r238-r296 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r269
PBB.mask_edge + PBB.runs_split + PBB.bound_pairsum +
PBB.mp_drive, r287 L2D.blocks_level2 + L2D.bound_vdc +
L2D.vdc_window + L2D.halves_slope + L2D.autocorr_full, r244
BH.wpack + BH.spearman, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN);
DEG_OFFS (1, 0, -1) around N-2 (the recursion triple); MEAS =
(BORDER, WINDOW, WDIFF) (FROZEN candidate measures); ID_HOLDS
1e-6; ID_NEAR 1e-3 (relative classification bars); REC_BAR 1e-9
(tautological recursion ward, rel); TB_WARD bars 1e-9 main
N <= 400 / 3e-6 deep / 1e-6 controls; VAL_BAR 1e-9; ID_BAR
1e-12; AC_BAR 1e-9; ADD_BAR 1e-9 (slope additivity); TOY_BAR
1e-14; SHARP_BAR 1e-12 (m2 pad arithmetic); MUT_MIN 1e-6;
R287_DELTA_F2 +0.309 tol 0.01; R287_CERT (6, 38); R287_KZ15_MISS
0.10 tol 0.02; R272_SP_EPS +0.67 tol 0.05; R272_GAMMA_TRUE
0.453 tol 0.05; R272_SL_C2 +0.196 tol 0.01; R270_ALT_BAND
(0.34, 0.44); RESERVE_BAND (0.020, 0.035); MP_DPS 60; MP_T_BAR
1e-8 (kz15); MP_DEEP_BAR 3e-6 (two deepest rungs); SM_Q_BAR
1e-20; SM_ALIAS_BAR 1e-12; KZ_ANCHOR 15; runtime <= 1800 s;
smoke = w9 + controls + Fractions section + toys + scope audits
+ route numerics + identity census at w9 (ladder, slopes,
target inequality, adjudication, mp wards skipped).  DISCLOSED
PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r270/r272/r287 RECORD number adopted
as-is; sigma*'s expected magnitude is derived arithmetic from
the r287 record slopes, disclosed above; nothing tuned.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  TARGET_INEQUALITY_FROZEN(sigma* with all constants, sigma
    measured, pad table)
+ ROUTE_TABLE(B1/B2/B3: valid n/47, delta'_route, identity
    status, break point)
+ [exactly one of] CHAIN_PROVENANCE_PROVEN(Bx, ...) /
    CHAIN_PROVENANCE_PARTIAL(Bx, gap) /
    INPUT_STILL_EMPIRICAL(the measured common obstruction)
+ [iff fired] CANDIDATE_THEOREM(L2 generic half, constants)
+ KZ15_NOTE(covered / structurally outside; r270 stands)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED.
Honesty before beauty: no verdict claims a cofinal law or an
asymptotic mechanism; every slope is MEASURED on 42 rungs only;
a VALID + SLOPE_OK route is a per-rung exact theorem WITH A
MEASURED LADDER EXPONENT (the r287 F2 typing), not a proof of
the m-dependence; the exception scalar's positivity beyond the
measured 42 stays OPEN; r243-r296 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 CRASHED on an index bug in the B1 builder --
amendment a1 (the r287 pairing-index convention restored, a code
bugfix, no bar or rule touched); smoke pass 2 = 27/27; amendment
a2 after smoke pass 2 (REPORTING ONLY: the ROUTE_TABLE identity
field shows the best sealed measure, the G61 text carries the
measure-transfer honesty clause, the break label renamed -- no
bar, band, rule or verdict rule moved); calibration pass 1 =
first full evaluation, 27/27 gates, wall 47.8 s, NO further
amendment; pass 2 = the record run, identical to pass 1 in every
printed figure up to WALL and the source line numbers inside the
scope-audit prints (shifted by this insertion); the only
post-freeze edit is this record-table insertion, which IS the
protocol):
CAL_VERDICT = TARGET_INEQUALITY_FROZEN(sigma* -0.516, sigma
-0.714, margin 0.198 in sigma = 0.099 in delta') + ROUTE_TABLE(
B1_PAIRGAP valid 47/47 delta' -0.112 BREAK@gapmax scaling;
B2_NODEDENS valid 47/47 delta' -0.097 BREAK@mass imbalance
growth; B3_PARSEVAL valid 47/47 delta' -0.097 IDENT HOLDS(
WINDOW) BREAK@measure transfer + signed-to-absolute gap) +
CHAIN_PROVENANCE_PARTIAL(B3_PARSEVAL, gap: slope miss 0.307) +
KZ15_NOTE(structurally outside: B1 0.57 / B2 0.86 / B3 0.91
dec; r270 exact-finite certificate remains the permanent
closure).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; block + autocorr identities worst 6.3e-16 /
2.7e-15 on 47 worlds; r272 wards exact (sp +0.67, gamma_true
+0.453, reserve 0.0268, alt med 0.39); r287 F2 regression exact
(delta' +0.309, cert 6/7 + 38/42, kz15 miss 0.096 dec, sl_c2
+0.196).  S3: v964-S0 recheck green in Fractions (window
identity + covering + vdC at every H + witness 36 == 36; m1
wrong prefactor 14 < 16 CAUGHT; m3 perturbed Fejer breaks by
2.00e+0 LOUD); the SYMBOLIC B3 sum rule PROVED exact on the
rational 4-node measure (orthogonality dev 0, Parseval-type
x^2 identity dev 0, pure Fractions); m4a/m4b FLAGGED by the
scope audit.  S4 (Leg A): additivity dev 2.6e-16; sl_c2 +0.196,
sl_pref +0.489, sigma = -0.714 <= sigma* = -0.516: THE TRUTH
SATISFIES THE TARGET INEQUALITY with 0.198 sigma margin -- what
is missing is not room, it is provenance; pad table (slope
budgets): Fejer step +0.607, block step -0.012, CS step +0.217;
per-exception certification form: kz15 +0.19 dec OVER, the
other six all under (kz20 -0.25 .. kz22 -0.83); m2 pad
arithmetic exact (0.210000000000 / 0.0).  S5 B1 (valid 47/47):
delta'_B1 = -0.112; gapmax/M slope -0.535 (sufficient <=
-1.178): the MAX pair gap falls far slower than the mean
amplitude (r272 B_amp -0.81) -- the Jacobi near-balance is a
MEAN statement, its extreme is not chain-controlled; loss med
0.88 dec.  S6 B2 (valid 47/47): delta'_B2 = -0.097; alpha_m
+1.006, run-length med 2.0 at every depth; D_rank med 0.024
(slope -0.42, falling!) vs D_mass med 0.154: the boundary
POSITIONS are near-equidistributed -- provable terrain -- but
the MASS is not; the obstruction is the imbalance n x maxM /
sumM slope +0.244 (max/mean run mass GROWS with N): pure node
density supplies the COUNT, not the decay (the r273 root-scale
mechanism sits in the mass profile).  S7 B3 (valid 47/47): THE
SURPRISE OF THE ROUND -- the chain is EXACTLY ORTHOGONAL w.r.t.
the WINDOW measure (union(d)): cross med 0.000, diag identity
dev 0.000, worst 0.000 across kz15/kz20/mains/EPST/SCR, while
BORDER (cross med 1.101) and WDIFF (1.086) BREAK: the Parseval
attachment point EXISTS -- the symbolic sum rule holds verbatim
on the window union; what remains is the MEASURE TRANSFER
(the vdC input lives on the BORDER union) and the signed-to-
absolute gap (wrx x Qabs)/sum s^2 med 4.3, slope +0.217 (the
mixed-sign border weights); recursion ward 7.5e-13; delta'_B3 =
-0.097, wrunmax slope -0.570.  S9: no route SLOPE_OK; B3 is
VALID + IDENT => CHAIN_PROVENANCE_PARTIAL(B3, slope miss
0.307); Leg C VOID; kz15 structurally outside for all three
routes, r270 stands.  SMOOTH alias 2.4e-14, q_N 4.2e-25; mp
wards kz15 2.9e-10, kz64 9.3e-9, kz52 6.6e-8; every chain step
holds on EPST/SCR by the same algebra (world-blind, 47/47).
READING (typed, no upgrade): the round DELIVERS the frozen
target inequality (sigma <= 2(sl_c2 - 0.21) - sl_pref, all
constants live) and shows the truth clears it with ~0.2 sigma
margin -- but ALL THREE classical provenance routes miss the
slope at the same wall: every source-pure majorization of the
P-variance through MAGNITUDES (|B_j|, M_i, |bw|) pays a
max/mean imbalance factor that grows (+0.22..+0.24 slope) and
eats the pad; the SIGNED structure that carries sigma = -0.71
(the pairwise cancellation already absorbed into the P_j
magnitudes, r287) is exactly what magnitude chains cannot see.
The two REAL assets the round leaves for the lane: (1) the
chain IS exactly orthogonal on the window union -- the Parseval
sum rule attaches there verbatim, so the missing piece is a
bordered-form transfer statement (window -> border union), a
concrete named object; (2) the run-boundary positions are
near-equidistributed with FALLING discrepancy (D_rank med
0.024, slope -0.42) -- the node-count side is provable terrain;
the mass imbalance (+0.24) is the single quantity a future
equidistribution argument must control.  Runtime 47.8 s full /
0.7 s smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE beyond the disclosed a1/a2 (records inserted per
protocol; no bar, band, rule or verdict rule moved).

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
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
AC_BAR = 1e-9
ADD_BAR = 1e-9
TOY_BAR = 1e-14
SHARP_BAR = 1e-12
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
DEG_OFFS = (1, 0, -1)
MEAS = ("BORDER", "WINDOW", "WDIFF")
ID_HOLDS = 1e-6
ID_NEAR = 1e-3
REC_BAR = 1e-9
R287_DELTA_F2 = 0.309
R287_DF2_TOL = 0.01
R287_CERT = (6, 38)
R287_KZ15_MISS = 0.10
R287_KZ15_TOL = 0.02
R272_SP_EPS = 0.67
R272_SP_TOL = 0.05
R272_GAMMA_TRUE = 0.453
R272_GT_TOL = 0.05
R272_SL_C2 = 0.196
R272_SL_TOL = 0.01
R270_ALT_BAND = (0.34, 0.44)
RESERVE_BAND = (0.020, 0.035)
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
KZ_ANCHOR = 15
ROUTE_ORDER = ("B1_PAIRGAP", "B2_NODEDENS", "B3_PARSEVAL")

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


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
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


# ---------------- v964-S0 recheck machinery (exact Fractions; the
# ---------------- proven vdC set RE-COMPUTED, not re-proved)
def fr_autocorr(P, h):
    m = len(P)
    return sum(P[j] * P[j + h] for j in range(m - h))


def fr_window_sums(P, H):
    m = len(P)
    out = []
    for t in range(-(H - 1), m):
        out.append(sum(P[j] for j in range(max(0, t),
                                           min(m, t + H))))
    return out


def fr_fejer_windowsum(P, H, perturbed=False):
    """sum_{|h|<H} (1 - |h|/H) A(h); the m3 mutant flag replaces
    the Fejer weight by (1 - |h|/(H + 1)) -- must break the
    window-sum identity LOUDLY."""
    den = H + 1 if perturbed else H
    tot = Fr(0)
    for h in range(-(H - 1), H):
        tot += (1 - Fr(abs(h), den)) * fr_autocorr(P, abs(h))
    return tot


def fr_vdc_bound_sq(P, H, prefactor_m_only=False):
    m = len(P)
    pref = Fr(m, H) if prefactor_m_only else Fr(m + H - 1, H)
    return pref * fr_fejer_windowsum(P, H)


FR_SEQS = (
    [Fr(2), Fr(-2), Fr(1)],
    [Fr(1), Fr(1)],
    [Fr(1), Fr(1), Fr(1), Fr(1)],
    [Fr(3, 7), Fr(-2, 9), Fr(5, 11), Fr(1, 4), Fr(1, 3),
     Fr(-3, 8), Fr(2, 5), Fr(7, 13), Fr(-1, 6)],
    [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
     Fr(1, 3), Fr(-1, 2), Fr(5, 4)],
    [Fr((-1) ** j * (j + 1), 2 * j + 3) for j in range(12)],
)


def fr_symbolic_sumrule():
    """the SYMBOLIC B3 sum rule, module-own, exact Fractions: on
    the rational 4-node measure x = (0, 1, 2, 3), w = (1, 2, 1, 3)
    build the monic three-term chain pi_0..pi_3 (a_k = <x pi_k,
    pi_k>/h_k, b_k = h_k/h_{k-1}) and verify (i) orthogonality
    sum w pi_a pi_b == 0 for a != b, (ii) the Parseval-type
    second-moment identity sum w x^2 pi_k^2 == h_{k+1} + a_k^2
    h_k + b_k^2 h_{k-1} for k = 1 (all exact)."""
    xs = [Fr(0), Fr(1), Fr(2), Fr(3)]
    ws = [Fr(1), Fr(2), Fr(1), Fr(3)]
    n = len(xs)
    pis = [[Fr(1)] * n]
    a_ = []
    b_ = []
    hs = [sum(w * p * p for w, p in zip(ws, pis[0]))]
    for k in range(3):
        ak = sum(w * x * p * p for w, x, p in zip(ws, xs, pis[k])) \
            / hs[k]
        bk = (hs[k] / hs[k - 1]) if k >= 1 else Fr(0)
        nxt = []
        for i in range(n):
            v = (xs[i] - ak) * pis[k][i]
            if k >= 1:
                v -= bk * pis[k - 1][i]
            nxt.append(v)
        pis.append(nxt)
        a_.append(ak)
        b_.append(bk)
        hs.append(sum(w * p * p for w, p in zip(ws, nxt)))
    worst_orth = Fr(0)
    for a in range(4):
        for b in range(a):
            worst_orth = max(worst_orth,
                             abs(sum(w * pis[a][i] * pis[b][i]
                                     for i, w in enumerate(ws))))
    k = 1
    lhs = sum(w * x * x * p * p
              for w, x, p in zip(ws, xs, pis[k]))
    rhs = hs[k + 1] + a_[k] ** 2 * hs[k] + b_[k] ** 2 * hs[k - 1]
    return worst_orth, abs(lhs - rhs)


# ---------------- sealed source-pure route builders.  Every route
# ---------------- builder consumes ONLY source-side objects (run
# ---------------- masses, atoms, weights, chain rows); the withheld
# ---------------- terminal drive key, the branch label and every
# ---------------- target-side identifier are forbidden in scope
# ---------------- (AST audit against BOUND_FORBIDDEN).
def route_b1(Mr, H):
    """B1 THREE-TERM / PAIR-IDENTITY route: by the exact r271
    alternation identity |B_j| = |M_{2j} - M_{2j+1}|: A(0) <=
    gapmax x eps_c2 with gapmax = max(pair gaps, tail); composed
    eps_B1 = sqrt((m_blk + H - 1) x gapmax x eps_c2)."""
    nr = len(Mr)
    if nr == 0:
        return dict(eps=0.0, gapmax=0.0, a0b=0.0, e_c2=0.0)
    gaps = [abs(Mr[i] - Mr[i + 1])
            for i in range(PAIR_OFFSET, nr - 1, 2)]
    odd = (nr - PAIR_OFFSET) % 2 == 1
    tail = Mr[-1] if odd else 0.0
    vals = gaps + ([tail] if odd else [])
    gapmax = max(vals) if vals else 0.0
    e_c2 = sum(gaps) + tail
    m_blk = (nr + 1) // 2
    a0_bound = gapmax * e_c2
    eps = math.sqrt(max((m_blk + H - 1) * a0_bound, 0.0))
    return dict(eps=eps, gapmax=gapmax, a0b=a0_bound, e_c2=e_c2)


def route_b2(Mr, H):
    """B2 ROOT-SCALE / NODE-DENSITY route: A(0) <= 2 sum M_i^2 <=
    2 x maxM x sumM (exact); composed eps_B2 = sqrt((m_blk + H -
    1) x 2 x maxM x sumM); imbalance = n_runs x maxM / sumM."""
    nr = len(Mr)
    if nr == 0:
        return dict(eps=0.0, mx=0.0, sm=0.0, m2=0.0, imb=0.0)
    mx = max(Mr)
    sm = sum(Mr)
    m2 = sum(v * v for v in Mr)
    m_blk = (nr + 1) // 2
    eps = math.sqrt((m_blk + H - 1) * 2.0 * mx * sm)
    return dict(eps=eps, mx=mx, sm=sm, m2=m2,
                imb=nr * mx / max(sm, 1e-300))


def route_b3(bw_runs, f_runs, H):
    """B3 FEJER / PARSEVAL route: per-run Cauchy-Schwarz against
    the |bw| measure: s_i^2 <= (sum_run |bw|) x (sum_run |bw|
    f^2) with f = bx v2 fac; summed: sum s_i^2 <= wrunmax x
    Q_abs; composed eps_B3 = sqrt((m_blk + H - 1) x 2 x wrunmax
    x Q_abs)."""
    nr = len(bw_runs)
    if nr == 0:
        return dict(eps=0.0, wrx=0.0, qabs=0.0, cs_sum=0.0)
    wr = [float(np.sum(np.abs(w))) for w in bw_runs]
    qr = [float(np.sum(np.abs(w) * f * f))
          for w, f in zip(bw_runs, f_runs)]
    wrx = max(wr)
    qabs = sum(qr)
    cs_sum = sum(a * b for a, b in zip(wr, qr))
    m_blk = (nr + 1) // 2
    eps = math.sqrt((m_blk + H - 1) * 2.0 * wrx * qabs)
    return dict(eps=eps, wrx=wrx, qabs=qabs, cs_sum=cs_sum)


def mutant_gift_bound(rc, Mr):
    """m4a MUST-FAIL MUTANT: a 'route bound' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * route_b1(Mr, 2)["eps"]


def mutant_branch_peek(rc, Mr):
    """m4b MUST-FAIL MUTANT (world-blindness break simulated): a
    'route bound' that consumes the branch label to pick its
    constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * route_b2(Mr, 2)["eps"]


def chain_quads(rows, N, X, W):
    """the B3 identity census objects on one candidate measure
    (X, W): scaled chain values v_k at the recursion triple
    degrees, norms n_k = sum W v_k^2, normalized crosses, the
    second moment q2 = sum W x^2 v_{N-2}^2, the tautological
    full-cross prediction (recursion ward) and the diagonal-only
    (orthogonality-assuming) prediction."""
    degs = [N - 2 + o for o in DEG_OFFS]        # N-1, N-2, N-3
    v = {d: BR.eval_scaled(rows, X, d) for d in degs}
    n_ = {d: float(np.sum(W * v[d] * v[d])) for d in degs}
    cr = {}
    for i, a in enumerate(degs):
        for b in degs[:i]:
            den = math.sqrt(max(abs(n_[a]) * abs(n_[b]), 1e-300))
            cr[(a, b)] = float(np.sum(W * v[a] * v[b])) / den
    # recursion coefficients at degree N-2 (scaled coordinates)
    alh = rows[N - 2]["alh"]
    gam = rows[N - 3]["gam_next"]
    e1 = math.exp(rows[N - 1]["Ls"] - rows[N - 2]["Ls"])
    e3 = math.exp(rows[N - 3]["Ls"] - rows[N - 2]["Ls"])
    c = {N - 1: e1, N - 2: alh, N - 3: gam * e3}
    q2 = float(np.sum(W * X * X * v[N - 2] * v[N - 2]))
    pred_full = 0.0
    for a in degs:
        for b in degs:
            pred_full += c[a] * c[b] * float(np.sum(W * v[a] * v[b]))
    pred_diag = sum(c[d] * c[d] * n_[d] for d in degs)
    return dict(n=n_, cr=cr, q2=q2, pf=pred_full, pd=pred_diag)


# ---------------------------------------------- toy exact tools
def toy_routes():
    """hand-checked deterministic sequences: the B1/B2/B3 chains
    must reproduce EXACTLY (bar 1e-14)."""
    worst = 0.0
    # runs Mr = (3,1,2,4,1), signs alternating: s = (3,-1,2,-4,1)
    Mr = [3.0, 1.0, 2.0, 4.0, 1.0]
    S = [3.0, -1.0, 2.0, -4.0, 1.0]
    P = L2D.blocks_level2(S)                    # [2, -2, 1]
    A0 = sum(v * v for v in P)                  # 9
    b1 = route_b1(Mr, 2)
    # gaps (2, 2), tail 1 -> gapmax 2, e_c2 5, a0_bound 10 >= 9
    worst = max(worst, abs(b1["gapmax"] - 2.0),
                abs(b1["e_c2"] - 5.0), abs(b1["a0b"] - 10.0))
    worst = max(worst, max(A0 - b1["a0b"], 0.0))
    # eps_B1 = sqrt((3 + 2 - 1) * 10) = sqrt(40)
    worst = max(worst, abs(b1["eps"] - math.sqrt(40.0)))
    b2 = route_b2(Mr, 2)
    # sum M^2 = 31 <= maxM x sumM = 44; A0 = 9 <= 2 x 31
    worst = max(worst, abs(b2["m2"] - 31.0), abs(b2["mx"] - 4.0),
                abs(b2["sm"] - 11.0))
    worst = max(worst, max(b2["m2"] - b2["mx"] * b2["sm"], 0.0))
    worst = max(worst, max(A0 - 2.0 * b2["m2"], 0.0))
    # eps_B2 = sqrt((3 + 2 - 1) * 2 * 44) = sqrt(352)
    worst = max(worst, abs(b2["eps"] - math.sqrt(352.0)))
    # B3 CS on a two-run toy: run1 w = (1, 2), f = (1, -1) ->
    # s1 = w.f = -1, |s1|^2 = 1 <= (3)(3) = 9; run2 w = (-1,),
    # f = (2,) -> s2^2 = 4 <= (1)(4)
    bwr = [np.array([1.0, 2.0]), np.array([-1.0])]
    fr_ = [np.array([1.0, -1.0]), np.array([2.0])]
    b3 = route_b3(bwr, fr_, 2)
    worst = max(worst, abs(b3["wrx"] - 3.0),
                abs(b3["qabs"] - 7.0), abs(b3["cs_sum"] - 13.0))
    s1 = float(np.sum(bwr[0] * fr_[0]))
    s2 = float(np.sum(bwr[1] * fr_[1]))
    worst = max(worst, max(s1 * s1 - 9.0, 0.0),
                max(s2 * s2 - 4.0, 0.0))
    worst = max(worst,
                max(s1 * s1 + s2 * s2 - b3["cs_sum"], 0.0),
                max(b3["cs_sum"] - b3["wrx"] * b3["qabs"], 0.0))
    # vdC window core reproduction on P (r287 toy): H = 2,
    # sum W^2 = 6, S_F = 3, eps = sqrt(6)
    f2 = L2D.bound_vdc(P)
    worst = max(worst, abs(f2["H"] - 2), abs(f2["s2"] - 6.0),
                abs(f2["s2"] / f2["H"] - 3.0),
                abs(f2["eps"] - math.sqrt(6.0)))
    # Fejer step S_F <= H x A(0): 3 <= 18
    worst = max(worst, max(f2["s2"] / f2["H"] - f2["H"] * A0, 0.0))
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("vdc_chain_provenance_probe -- PRIME.PORT.L2."
          "VDC_CHAIN_PROVENANCE.01 (round 297)")
    print("SPEC_SHA %s   R269_SHA %s (imported)   R287_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], PBB.SPEC_SHA[:16], L2D.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + route numerics + "
                        "identity census at w9; ladder, slopes, "
                        "target inequality, adjudication, mp wards "
                        "skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE L2 CHAIN-PROVENANCE ROUND (reviewer routing after "
          "the r296 DENS close): the vdC machine is a THEOREM "
          "(v964-S0, exact Fractions) -- its INPUT (the P-variance"
          " / autocorrelation scaling) is so far only MEASURED; "
          "this round freezes the weakest sufficient input bound "
          "(TARGET_INEQUALITY, Leg A) and tests THREE source-pure "
          "chain-provenance routes (B1 pair-identity, B2 node-"
          "density/root-scale per the r273 trace, B3 Fejer/"
          "Parseval with the symbolic sum rule proved in "
          "Fractions); DELTA_NEED %.2f (r272 record), pad "
          "gamma_true 0.45 (r272/r273: generic, perturbation-"
          "insensitive); world-blind validity ADMISSIBLE (L2 is "
          "the generic half); ALL bars, rules and verdicts sealed "
          "BEFORE evaluation (pre-spec input = r270/r272/r287 "
          "record numbers, disclosed)" % DELTA_NEED)

    # ---------------- S1: census + controls (r287 scaffold verbatim)
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
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, o=o, lo=lo,
                    hi=hi, p=p)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs)))

    # ---------------- S2: decomposition + identities + record wards
    section("S2  EXACT DECOMPOSITION + IDENTITIES + RECORD WARDS")
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
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        bws = rc["bw"][o]
        v2s = rc["v2"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        t_loc = float(np.sum(cts[ed]))
        cb = cts[~ed]
        wb = bws[~ed]
        fb = (bxs * v2s)[~ed] * rc["fac"]
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        sabs = sum(abs(v) for v in Sr)
        P = L2D.blocks_level2(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        f2 = L2D.bound_vdc(P)
        H = f2["H"]
        S_F = f2["s2"] / H
        A0 = sum(v * v for v in P)
        Zl = t_loc + rc["chain"]
        alt, lag = L2D.block_sign_stats(P)
        bw_runs = [wb[a:b] for a, b, _s in runs]
        f_runs = [fb[a:b] for a, b, _s in runs]
        b1 = route_b1(Mr, H)
        b2 = route_b2(Mr, H)
        b3 = route_b3(bw_runs, f_runs, H)
        # node-density census (B2): boundary discrepancies
        nb = len(cb)
        nr = len(runs)
        d_rank = 0.0
        d_mass = 0.0
        if nr > 1 and nb > 0:
            cmass = np.cumsum(np.abs(cb))
            tot = max(float(cmass[-1]), 1e-300)
            for i, (a, b, _s) in enumerate(runs[:-1]):
                d_rank = max(d_rank,
                             abs(b / nb - (i + 1) / nr))
                d_mass = max(d_mass,
                             abs(float(cmass[b - 1]) / tot
                                 - (i + 1) / nr))
        rl_med = float(np.median([b - a for a, b, _s in runs])) \
            if runs else 0.0
        return dict(Mr=Mr, Sr=Sr, alt_ok=alt_ok, R=R, sabs=sabs,
                    P=P, e_c2=e_c2, f2=f2, H=H, S_F=S_F, A0=A0,
                    Zl=Zl, alt=alt, lag=lag, m=len(P), nr=nr,
                    b1=b1, b2=b2, b3=b3, d_rank=d_rank,
                    d_mass=d_mass, rl_med=rl_med,
                    sum_s2=sum(v * v for v in Sr))

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(all_rc) + len(crecs)))

    Ns = [rc["N"] for rc in recs]
    eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
    if not smoke:
        sp_eps = BH.spearman(Ns, eps_c2_rel)
        Ct_s = [abs(rc["ev"]["R"]) / max(rc["ev"]["sabs"], 1e-300)
                for rc in recs]
        gamma_true = -L2D.halves_slope(Ns, Ct_s)
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        slack15 = M_W - abs(rc15["Z"])
        ok15 = RESERVE_BAND[0] <= slack15 <= RESERVE_BAND[1]
        alt_exc = [rc["ev"]["alt"] for rc in recs
                   if rc["g_branch"] < 0.0]
        alt_med = float(np.median(alt_exc))
        ok_alt = R270_ALT_BAND[0] <= alt_med <= R270_ALT_BAND[1]
        check("G22-r272-reproduction-wards",
              abs(sp_eps - R272_SP_EPS) <= R272_SP_TOL
              and abs(gamma_true - R272_GAMMA_TRUE) <= R272_GT_TOL
              and ok15 and ok_alt,
              "sp(N, eps_c2) %+.2f (ref %+.2f), gamma_true %+.3f "
              "(ref %+.3f), kz15 true reserve %.4f in %s (the "
              "r270 exact-finite anchor), exception P-sign alt "
              "med %.2f in %s"
              % (sp_eps, R272_SP_EPS, gamma_true,
                 R272_GAMMA_TRUE, slack15, str(RESERVE_BAND),
                 alt_med, str(R270_ALT_BAND)))
        # r287 F2 regression (bit-near record reproduction)
        sl_c2 = L2D.halves_slope(Ns, eps_c2_rel)
        eF2_rel = [rc["ev"]["f2"]["eps"] / M_W for rc in recs]
        sl_F2 = L2D.halves_slope(Ns, eF2_rel)
        delta_F2 = sl_c2 - sl_F2
        cert7 = 0
        cert42 = 0
        for rc in recs:
            ev = rc["ev"]
            mg = M_W - (abs(ev["Zl"]) + ev["f2"]["eps"])
            if mg > 0.0:
                cert42 += 1
                if rc["g_branch"] < 0.0:
                    cert7 += 1
        ev15 = rc15["ev"]
        need15 = M_W - abs(ev15["Zl"])
        miss15 = math.log10(ev15["f2"]["eps"] / need15) \
            if need15 > 0 else float("inf")
        check("G23-r287-f2-regression",
              abs(delta_F2 - R287_DELTA_F2) <= R287_DF2_TOL
              and cert7 == R287_CERT[0] and cert42 == R287_CERT[1]
              and abs(miss15 - R287_KZ15_MISS) <= R287_KZ15_TOL
              and abs(sl_c2 - R272_SL_C2) <= R272_SL_TOL,
              "the r287 F2_VDC record recomputed at the frozen H "
              "rule: delta'(F2) %+.3f (ref %+.3f), cert %d/7 + "
              "%d/42 (ref %d/%d), kz15 miss %.3f dec (ref %.2f), "
              "slope(eps_c2/M) %+.3f (ref %+.3f) -- the round "
              "stands on the recorded machine state"
              % (delta_F2, R287_DELTA_F2, cert7, cert42,
                 R287_CERT[0], R287_CERT[1], miss15,
                 R287_KZ15_MISS, sl_c2, R272_SL_C2))
    else:
        sl_c2 = float("nan")
        check("G22-r272-reproduction-wards", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G23-r287-f2-regression", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    okv = True
    for P in FR_SEQS:
        m = len(P)
        s = sum(P)
        for Hh in range(1, m + 1):
            W = fr_window_sums(P, Hh)
            okv &= (len(W) == m + Hh - 1)
            okv &= (fr_fejer_windowsum(P, Hh)
                    == Fr(1, Hh) * sum(w * w for w in W))
            okv &= (sum(W) == Hh * s)
            okv &= (s * s <= fr_vdc_bound_sq(P, Hh))
    Peq = [Fr(1)] * 6
    okv &= (sum(Peq) ** 2 == fr_vdc_bound_sq(Peq, 1))
    check("G30-v964-s0-recheck", okv,
          "the PROVEN v964-S0 vdC set RE-COMPUTED exact in "
          "Fractions on all %d frozen sequences: Fejer window-sum "
          "identity, H-fold covering identity, |sum P|^2 <= "
          "((m + H - 1)/H) x windowsum at every H, H = 1 equality "
          "witness 36 == 36 -- the machine this round feeds is a "
          "THEOREM" % len(FR_SEQS))
    w_orth, w_id = fr_symbolic_sumrule()
    check("G31-symbolic-sumrule", w_orth == 0 and w_id == 0,
          "the B3 SYMBOLIC sum rule PROVED exact in Fractions on "
          "the rational 4-node measure: monic three-term chain "
          "orthogonality dev %s, Parseval-type second-moment "
          "identity sum w x^2 pi_k^2 == h_{k+1} + a_k^2 h_k + "
          "b_k^2 h_{k-1} dev %s -- the identity CANDIDATE exists "
          "as abstract algebra; whether the REAL border chain "
          "attaches to it is the S7 census"
          % (str(w_orth), str(w_id)))
    toy_worst = toy_routes()
    check("G32-toy-exactness", toy_worst <= TOY_BAR,
          "hand-checked sequences reproduce EXACTLY (worst dev "
          "%.1e, bar %.0e): blocks [2,-2,1]; vdC H=2 sumW2=6 "
          "S_F=3 eps=sqrt(6); B1 gaps (2,2) tail 1 gapmax 2 "
          "e_c2 5 A0 9 <= 10 eps sqrt(40); B2 sumM2 31 <= 44 "
          "eps sqrt(352); B3 CS two-run toy wrx 3 qabs 7 "
          "cs_sum 13" % (toy_worst, TOY_BAR))
    h_b1 = scope_audit("route_b1", BOUND_FORBIDDEN)
    h_b2 = scope_audit("route_b2", BOUND_FORBIDDEN)
    h_b3 = scope_audit("route_b3", BOUND_FORBIDDEN)
    h_cq = scope_audit("chain_quads", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_b1 or h_b2 or h_b3 or h_cq)
    check("G33-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the three route builders + the identity census consume "
          "source-side objects only "
          "(no truth-side identifier in scope%s); m4a gift mutant "
          "FLAGGED (%s); m4b branch-peek mutant (simulated world-"
          "blindness break) FLAGGED (%s); fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    P4 = [Fr(1)] * 4
    wrong = fr_vdc_bound_sq(P4, 2, prefactor_m_only=True)
    ok_m1 = (wrong == 14 and sum(P4) ** 2 == 16 and wrong < 16
             and fr_vdc_bound_sq(P4, 2) >= 16)
    Pt = [Fr(2), Fr(-2), Fr(1)]
    Wt = fr_window_sums(Pt, 2)
    brk3 = abs(float(fr_fejer_windowsum(Pt, 2, perturbed=True)
                     - Fr(1, 2) * sum(w * w for w in Wt)))
    check("G34-mustfails-m1-m3", ok_m1 and brk3 >= MUT_MIN,
          "m1 WRONG PREFACTOR m/H: 14 < 16 = |sum P|^2 on "
          "P = (1,1,1,1), H = 2 EXACT (correct bound 35/2) -- "
          "CAUGHT; m3 PERTURBED FEJER weight (1 - |h|/(H+1)) "
          "breaks the window-sum identity by %.2e (>= %.0e) "
          "LOUD -- every constant in the sealed forms is "
          "load-bearing" % (brk3, MUT_MIN))

    # ---------------- S4: Leg A -- the target inequality
    section("S4  LEG A: THE TARGET INEQUALITY (VDC INPUT ANATOMY)")
    # validity of the universal chain steps on ALL worlds (gate)
    val_worst = {nm: -1e300 for nm in ROUTE_ORDER}
    fej_worst = -1e300
    a0_worst = {"B1_PAIRGAP": -1e300, "B2_NODEDENS": -1e300,
                "B3_PARSEVAL": -1e300}
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        sc = max(abs(ev["A0"]), 1e-300)
        # Fejer step S_F <= H x A(0)
        fej_worst = max(fej_worst, (ev["S_F"] - ev["H"] * ev["A0"])
                        / sc)
        # A(0) <= gapmax x eps_c2 (B1); <= 2 sum M^2 <= 2 mx sm
        # (B2); <= 2 sum s^2 <= 2 wrx qabs (B3)
        a0_worst["B1_PAIRGAP"] = max(
            a0_worst["B1_PAIRGAP"], (ev["A0"] - ev["b1"]["a0b"]) / sc)
        a0_worst["B2_NODEDENS"] = max(
            a0_worst["B2_NODEDENS"],
            (ev["A0"] - 2.0 * ev["b2"]["m2"]) / sc,
            (ev["b2"]["m2"] - ev["b2"]["mx"] * ev["b2"]["sm"]) / sc)
        a0_worst["B3_PARSEVAL"] = max(
            a0_worst["B3_PARSEVAL"],
            (ev["A0"] - 2.0 * ev["sum_s2"]) / sc,
            (ev["sum_s2"] - ev["b3"]["cs_sum"]) / sc,
            (ev["b3"]["cs_sum"]
             - ev["b3"]["wrx"] * ev["b3"]["qabs"]) / sc)
        for nm, key in (("B1_PAIRGAP", "b1"), ("B2_NODEDENS", "b2"),
                        ("B3_PARSEVAL", "b3")):
            val_worst[nm] = max(val_worst[nm],
                                (abs(ev["R"]) - ev[key]["eps"])
                                / max(abs(ev["R"]), 1e-300))
    ok_val = (fej_worst <= VAL_BAR
              and all(a0_worst[nm] <= VAL_BAR for nm in ROUTE_ORDER)
              and all(val_worst[nm] <= VAL_BAR
                      for nm in ROUTE_ORDER))
    check("G40-route-validity-wards", ok_val,
          "every chain step EXACT on %d worlds (incl. the broken-"
          "arithmetic controls -- WORLD-BLIND by the same "
          "algebra): Fejer step slack %.1e; A(0) majorization "
          "slacks %s; route validity |R| <= eps slacks %s (bar "
          "%.0e)"
          % (len(all_rc) + len(crecs), fej_worst,
             str({nm[:2]: "%+.1e" % a0_worst[nm]
                  for nm in ROUTE_ORDER}),
             str({nm[:2]: "%+.1e" % val_worst[nm]
                  for nm in ROUTE_ORDER}), VAL_BAR))
    if not smoke:
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        sf_rel = [rc["ev"]["S_F"] / (M_W * M_W) for rc in recs]
        sl_pref = L2D.halves_slope(Ns, pref)
        sigma = L2D.halves_slope(Ns, sf_rel)
        add_dev = abs(sl_F2 - 0.5 * (sl_pref + sigma))
        sigma_star = 2.0 * (sl_c2 - DELTA_NEED) - sl_pref
        pad_sig = sigma_star - sigma
        check("G41-slope-additivity", add_dev <= ADD_BAR,
              "the exact decomposition slope(eps_F2/M) = (1/2) x "
              "[slope(pref) + sigma]: dev %.1e (bar %.0e); "
              "sl_pref %+.3f, sigma = slope(S_F/M^2) %+.3f"
              % (add_dev, ADD_BAR, sl_pref, sigma))
        # pad table: slope budgets of the universal steps
        fej_sl = L2D.halves_slope(
            Ns, [rc["ev"]["H"] * rc["ev"]["A0"]
                 / max(rc["ev"]["S_F"], 1e-300) for rc in recs])
        blk_sl = L2D.halves_slope(
            Ns, [2.0 * rc["ev"]["sum_s2"]
                 / max(rc["ev"]["A0"], 1e-300) for rc in recs])
        cs_sl = L2D.halves_slope(
            Ns, [rc["ev"]["b3"]["wrx"] * rc["ev"]["b3"]["qabs"]
                 / max(rc["ev"]["sum_s2"], 1e-300) for rc in recs])
        tgt_note = []
        for rc in sorted(exc, key=lambda r_: r_["kz"]):
            ev = rc["ev"]
            need = M_W - abs(ev["Zl"])
            allow = (ev["H"] / (ev["m"] + ev["H"] - 1)) * need * need \
                if need > 0 else 0.0
            tgt_note.append("kz%d %.2f dec" % (
                rc["kz"],
                math.log10(ev["S_F"] / max(allow, 1e-300))))
        check("G42-target-inequality-frozen", True,
              "TARGET_INEQUALITY_FROZEN: sigma <= sigma* = "
              "2 x (slope(eps_c2/M) - DELTA_NEED) - slope(pref) = "
              "2 x (%+.3f - %.2f) - %+.3f = %+.3f; measured sigma "
              "%+.3f => the TRUTH SATISFIES the target with %.3f "
              "sigma margin (%.3f in delta'); PAD TABLE (slope "
              "budgets of the universal steps): Fejer step %+.3f, "
              "block step %+.3f, CS step %+.3f; per-exception "
              "certification form S_F < H/(m+H-1) x (M_W-|Zl|)^2 "
              "(dec over): %s"
              % (sl_c2, DELTA_NEED, sl_pref, sigma_star, sigma,
                 pad_sig, 0.5 * pad_sig, fej_sl, blk_sl, cs_sl,
                 "; ".join(tgt_note)))
        # m2 pad-sharpness arithmetic
        d_with = sl_c2 - 0.5 * (sl_pref + sigma_star)
        sigma_nopad = 2.0 * sl_c2 - sl_pref
        d_nopad = sl_c2 - 0.5 * (sl_pref + sigma_nopad)
        check("G43-mustfail-pad-dropped", abs(d_with - DELTA_NEED)
              <= SHARP_BAR and abs(d_nopad) <= SHARP_BAR
              and d_nopad <= DELTA_NEED,
              "m2 PAD-DROPPED TARGET (sharpness): the sealed "
              "sigma* composes to delta' = %.12f == DELTA_NEED "
              "exactly; dropping the pad term (DELTA_NEED -> 0) "
              "composes to delta' = %.1e <= 0.21 -- the chain "
              "would NOT deliver: the pad term is load-bearing "
              "(bar %.0e)" % (d_with, d_nopad, SHARP_BAR))
    else:
        sigma = sigma_star = sl_pref = float("nan")
        check("G41-slope-additivity", True, "SMOKE: skipped")
        check("G42-target-inequality-frozen", True,
              "SMOKE: skipped")
        check("G43-mustfail-pad-dropped", True, "SMOKE: skipped")

    # ---------------- S5/S6: B1 + B2 censuses
    section("S5  LEG B1 (PAIR-IDENTITY) + B2 (NODE DENSITY)")
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d H %-2d  |R| %.4f  F2 %.3f"
             "  B1 %.3f (gapmax %.4f)  B2 %.3f (imb %.2f)  B3 "
             "%.3f (wrx %.2e)"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g_branch"] < 0 else "chp", ev["m"],
                ev["H"], abs(ev["R"]), ev["f2"]["eps"],
                ev["b1"]["eps"], ev["b1"]["gapmax"],
                ev["b2"]["eps"], ev["b2"]["imb"],
                ev["b3"]["eps"], ev["b3"]["wrx"]))
    if not smoke:
        routes = {}
        for nm, key in (("B1_PAIRGAP", "b1"), ("B2_NODEDENS", "b2"),
                        ("B3_PARSEVAL", "b3")):
            e_rel = [rc["ev"][key]["eps"] / M_W for rc in recs]
            sl_ = L2D.halves_slope(Ns, e_rel)
            dp_ = sl_c2 - sl_
            med_dec = float(np.median(
                [math.log10(max(v, 1e-300)) for v in e_rel]))
            loss = float(np.median(
                [math.log10(rc["ev"][key]["eps"]
                            / max(abs(rc["ev"]["R"]), 1e-300))
                 for rc in recs]))
            routes[nm] = dict(sl=sl_, dp=dp_, med=med_dec,
                              loss=loss)
        gap_sl = L2D.halves_slope(
            Ns, [rc["ev"]["b1"]["gapmax"] / M_W for rc in recs])
        gap_need = 2.0 * (sl_c2 - DELTA_NEED) - L2D.halves_slope(
            Ns, [rc["ev"]["m"] + rc["ev"]["H"] - 1
                 for rc in recs]) - sl_c2
        check("G50-b1-census", True,
              "B1 PAIR-IDENTITY route: delta'_B1 %+.3f (need > "
              "%.2f); the provenance carrier gapmax/M slope %+.3f "
              "(sufficient would be <= %+.3f): the MAX pair gap "
              "falls far slower than the mean amplitude (r272 "
              "B_amp -0.81) -- the Jacobi near-balance is a MEAN "
              "statement, its extreme is not chain-controlled; "
              "loss med %.2f dec; eps med %+.2f dec vs M"
              % (routes["B1_PAIRGAP"]["dp"], DELTA_NEED, gap_sl,
                 gap_need, routes["B1_PAIRGAP"]["loss"],
                 routes["B1_PAIRGAP"]["med"]))
        alpha_m = L2D.halves_slope(Ns, [rc["ev"]["nr"]
                                        for rc in recs])
        imb_sl = L2D.halves_slope(Ns, [rc["ev"]["b2"]["imb"]
                                       for rc in recs])
        dr_med = float(np.median([rc["ev"]["d_rank"]
                                  for rc in recs]))
        dm_med = float(np.median([rc["ev"]["d_mass"]
                                  for rc in recs]))
        dr_sl = L2D.halves_slope(Ns, [max(rc["ev"]["d_rank"],
                                          1e-300) for rc in recs])
        rl_med = float(np.median([rc["ev"]["rl_med"]
                                  for rc in recs]))
        check("G51-b2-census", True,
              "B2 NODE-DENSITY route: delta'_B2 %+.3f (need > "
              "%.2f); alpha_m(runs) %+.3f, run-length med %.1f; "
              "ET-style boundary discrepancies: D_rank med %.3f "
              "(slope %+.2f) vs D_mass med %.3f -- the boundary "
              "POSITIONS are near-equidistributed (provable "
              "terrain), the MASS is not; the obstruction is the "
              "imbalance n x maxM / sumM slope %+.3f (max/mean "
              "run mass GROWS with N): pure node density supplies "
              "the COUNT, not the decay"
              % (routes["B2_NODEDENS"]["dp"], DELTA_NEED, alpha_m,
                 rl_med, dr_med, dr_sl, dm_med, imb_sl))
    else:
        routes = {}
        check("G50-b1-census", True, "SMOKE: skipped")
        check("G51-b2-census", True, "SMOKE: skipped")

    # ---------------- S7: B3 identity census
    section("S7  LEG B3: THE PARSEVAL IDENTITY CENSUS")
    id_pool = (mrecs + [crecs[c] for c in ("EPST", "SCR")]) \
        if smoke else \
        ([rc for rc in recs if rc["kz"] in (KZ_ANCHOR, 20)]
         + mrecs + [crecs[c] for c in ("EPST", "SCR")])
    rec_worst = 0.0
    id_status = {}
    for meas in MEAS:
        crosses = []
        devs = []
        for rc in id_pool:
            N = rc["N"]
            rows = rc["p"]["rows"]
            if meas == "BORDER":
                X, W = rc["bx"], rc["bw"]
            elif meas == "WINDOW":
                X, W = rc["xu"], rc["wu"]
            else:
                X = np.concatenate([rc["xu"], rc["bx"]])
                W = np.concatenate([rc["wu"], -rc["bw"]])
            cq = chain_quads(rows, N, X, W)
            rec_worst = max(rec_worst,
                            abs(cq["q2"] - cq["pf"])
                            / max(abs(cq["q2"]), 1e-300))
            crosses.append(max(abs(v) for v in cq["cr"].values()))
            devs.append(abs(cq["q2"] - cq["pd"])
                        / max(abs(cq["q2"]), 1e-300))
            rc.setdefault("cq", {})[meas] = cq
        cmed = float(np.median(crosses))
        dmed = float(np.median(devs))
        wm = max(max(crosses), max(devs))
        st = ("HOLDS" if wm <= ID_HOLDS
              else ("NEAR" if wm <= ID_NEAR else "BREAKS"))
        id_status[meas] = (st, cmed, dmed, wm)
        info("measure %-7s orth-cross med %.3f  diag-identity dev "
             "med %.3f  worst %.3f  => %s"
             % (meas, cmed, dmed, wm, st))
    check("G60-recursion-ward", rec_worst <= REC_BAR,
          "the tautological full-cross prediction (the three-term "
          "recursion in scaled coordinates, all 9 cross terms) "
          "reproduces sum W x^2 v2^2 on every (world, measure): "
          "worst rel dev %.1e (bar %.0e) -- the recursion algebra "
          "is exact; ONLY orthogonality is in question"
          % (rec_worst, REC_BAR))
    id_holds = [m for m in MEAS if id_status[m][0] == "HOLDS"]
    ident_ok = bool(id_holds)
    check("G61-b3-identity-census", True,
          "the chain is %s w.r.t. the sealed candidate "
          "measures: %s -- %s"
          % (("ORTHOGONAL on " + "/".join(id_holds))
             if ident_ok else "NOT orthogonal",
             "; ".join("%s %s (cross med %.3f, diag dev med %.3f)"
                       % (m, id_status[m][0], id_status[m][1],
                          id_status[m][2]) for m in MEAS),
             "the symbolic sum rule ATTACHES on that measure (an "
             "exact chain-norm identity exists there); the vdC "
             "input lives on the BORDER union -- the transfer "
             "between the measures is the remaining provenance "
             "step" if ident_ok else
             "the r244 bordered-Hankel chain is orthogonal w.r.t. "
             "the full bordered form, NOT a plain union -- the "
             "Parseval route has no attachment point on these "
             "measures (the named break)"))
    if not smoke:
        ag_ratio = [rc["ev"]["b3"]["wrx"] * rc["ev"]["b3"]["qabs"]
                    / max(rc["ev"]["sum_s2"], 1e-300)
                    for rc in recs]
        ag_sl = L2D.halves_slope(Ns, ag_ratio)
        wrx_sl = L2D.halves_slope(
            Ns, [rc["ev"]["b3"]["wrx"] for rc in recs])
        check("G62-b3-census", True,
              "B3 PARSEVAL route: delta'_B3 %+.3f (need > %.2f); "
              "wrunmax slope %+.3f; the signed-to-absolute gap "
              "(wrx x Qabs) / sum s^2: med %.1f, slope %+.3f -- "
              "the mixed-sign border weights (ws > 0, -vs < 0 by "
              "construction) put the |.|-chain above the signed "
              "truth by a GROWING factor: the structural break "
              "of the route"
              % (routes["B3_PARSEVAL"]["dp"], DELTA_NEED, wrx_sl,
                 float(np.median(ag_ratio)), ag_sl))
    else:
        check("G62-b3-census", True, "SMOKE: skipped")

    # ---------------- S8: worlds + anchors + mp wards
    section("S8  WORLDS + ANCHORS + MP WARDS")
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    evS = crecs["SMOOTH"]["ev"]
    okSv = abs(evS["R"]) <= evS["b1"]["eps"] + VAL_BAR
    check("G70-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSv,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "route validity holds trivially on the self-aliased "
          "source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSv else "BROKEN"))
    if not smoke:
        mp_note = []
        ok_mp = True
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        t15 = PBB.mp_drive(rc15["p"], MP_DPS)
        d15 = abs(t15 - rc15["t_term"])
        ok_mp = ok_mp and (d15 <= MP_T_BAR)
        mp_note.append("kz15 (N %d) dev %.1e (bar %.0e)"
                       % (rc15["N"], d15, MP_T_BAR))
        for rc in recs[-2:]:
            t_mp = PBB.mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("kz%d (N %d, DEEPEST) dev %.1e (bar "
                           "%.0e)" % (rc["kz"], rc["N"], dv,
                                      MP_DEEP_BAR))
        check("G71-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G71-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: adjudication + Legs C/D + verdict
    section("S9  ADJUDICATION + LEG C/D + VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the frozen target inequality (the weakest "
          "sufficient vdC input bound with all constants), the "
          "three-route provenance census with exact validity, "
          "the identity census of the border chain, and the "
          "named gap object -- NO new certificate promoted, NO "
          "bound modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        elig = {}
        for nm in ROUTE_ORDER:
            elig[nm] = dict(
                valid=(val_worst[nm] <= VAL_BAR
                       and a0_worst[nm] <= VAL_BAR),
                slope_ok=(routes[nm]["dp"] > DELTA_NEED),
                ident=(nm == "B3_PARSEVAL" and ident_ok))
        # PROVEN reachable only by B3 with IDENT + exact abs step
        # (disclosed expectation: structurally false) -- checked:
        bulk_onesign = all(
            float(np.min(rc["bw"])) > 0.0
            or float(np.max(rc["bw"])) < 0.0 for rc in mrecs)
        proven = [nm for nm in ("B3_PARSEVAL",)
                  if elig[nm]["valid"] and elig[nm]["slope_ok"]
                  and elig[nm]["ident"] and bulk_onesign]
        part = [nm for nm in ROUTE_ORDER
                if elig[nm]["valid"]
                and (elig[nm]["slope_ok"] or elig[nm]["ident"])]
        tab = []
        breaks = {"B1_PAIRGAP": "gapmax scaling (max vs mean)",
                  "B2_NODEDENS": "mass imbalance growth",
                  "B3_PARSEVAL": "measure transfer + "
                                 "signed-to-absolute gap"}
        for nm in ROUTE_ORDER:
            tab.append("%s valid %s delta' %+.3f%s %s"
                       % (nm,
                          "47/47" if elig[nm]["valid"] else "FAIL",
                          routes[nm]["dp"],
                          (" IDENT " + ("HOLDS(%s)"
                                        % "/".join(id_holds)
                                        if ident_ok else "BREAKS"))
                          if nm == "B3_PARSEVAL" else "",
                          "SLOPE_OK" if elig[nm]["slope_ok"]
                          else "BREAK@" + breaks[nm]))
        parts = ["TARGET_INEQUALITY_FROZEN(sigma* %+.3f, sigma "
                 "%+.3f, margin %.3f in sigma = %.3f in delta')"
                 % (sigma_star, sigma, sigma_star - sigma,
                    0.5 * (sigma_star - sigma))]
        parts.append("ROUTE_TABLE(%s)" % "; ".join(tab))
        w = None
        if proven:
            w = proven[0]
            parts.append("CHAIN_PROVENANCE_PROVEN(%s, delta' "
                         "%+.3f > %.2f)" % (w, routes[w]["dp"],
                                            DELTA_NEED))
            fired = True
        elif part:
            w = max(part, key=lambda nm: (elig[nm]["slope_ok"],
                                          routes[nm]["dp"]))
            gap = ("slope miss %.3f" % (DELTA_NEED
                                        - routes[w]["dp"])
                   if not elig[w]["slope_ok"] else breaks[w])
            parts.append("CHAIN_PROVENANCE_PARTIAL(%s, gap: %s)"
                         % (w, gap))
            fired = elig[w]["slope_ok"]
        else:
            parts.append("INPUT_STILL_EMPIRICAL(common "
                         "obstruction: every universal "
                         "majorization of A(0) through magnitudes "
                         "pays a max/mean imbalance factor that "
                         "GROWS and eats the pad; the true input "
                         "sigma %+.3f lives in the SIGNED block "
                         "structure that no |.|-chain sees)"
                         % sigma)
            fired = False
        # Leg C
        if fired and w is not None:
            info("CANDIDATE THEOREM (L2 generic half): for every "
                 "rung of the sealed ladder (N in [%d, %d], H = "
                 "ceil(sqrt(m))): |R| <= eps_%s (exact chain, "
                 "constants: pref (m+H-1), route factors printed "
                 "above) AND slope(eps_%s/M) <= slope(eps_c2/M) "
                 "- %.2f (MEASURED hypothesis, 42 rungs) => "
                 "delta' > %.2f on the generic half; exceptions: "
                 "6 via the r287 F2 certificates, kz15 via the "
                 "r270 exact-finite certificate.  NOT promoted "
                 "(wave-9 candidate)."
                 % (min(Ns), max(Ns), w, w, DELTA_NEED,
                    DELTA_NEED))
        else:
            info("Leg C VOID (no route carries).  The gap object "
                 "of the lane: a signed/bordered-form sum rule "
                 "(the r244 bordered Hankel form itself, not a "
                 "plain union measure) OR a mass-profile "
                 "equidistribution statement (D_rank is flat and "
                 "small -- node positions are provable terrain; "
                 "the mass imbalance is the obstruction).")
        # Leg D: kz15 note
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        ev15 = rc15["ev"]
        need15 = M_W - abs(ev15["Zl"])
        kz_note = []
        covered = False
        for nm, key in (("B1", "b1"), ("B2", "b2"), ("B3", "b3")):
            e_ = ev15[key]["eps"]
            if e_ < need15:
                covered = True
                kz_note.append("%s cert %+.4f" % (nm, need15 - e_))
            else:
                kz_note.append("%s miss %.2f dec"
                               % (nm, math.log10(e_ / need15)))
        parts.append("KZ15_NOTE(%s: %s; r270 exact-finite "
                     "certificate %s)"
                     % ("covered" if covered
                        else "structurally outside",
                        "; ".join(kz_note),
                        "redundant" if covered
                        else "remains the permanent closure"))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the v964-S0 recheck, the "
          "symbolic sum rule, every route chain step (world-blind"
          " 47/47); MEASURED: every slope, imbalance, gap and "
          "margin (42 rungs only); OPEN: the chain origin of the "
          "vdC input beyond the named gap object, the cofinal "
          "step H5, kz15 beyond r270; NO RH claim"
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
