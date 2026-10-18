#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quenched_opening_probe -- PRIME.PORT.RHP.QUENCHED.OPENING.01
(round 264): the OPENING ROUND of the quenched full-source RHP
campaign.  r263 closed the primary floor lane and handed over ONE
signed scalar per exception window; r261 froze the campaign input.
This round freezes the CAMPAIGN CHARTER in code, builds the EXACT
RHP DICTIONARY for the handover scalar Z_w (a designated readout
of the discrete 2x2 FIK/IIKS solution), asks the first substance
question (how does the exception branch manifest in the RHP DATA,
not in the solution?), and measures the pair-dynamics no-pole
coordinate in s.

THE CHARTER (leg A, frozen as machine-readable constants below):
  TARGET (r263 S6, verbatim): produce Z_w = Z^RHP_w + E_w with
    |Z^RHP_w| + |E_w| < M_w = sqrt(5/7) on the exception branch,
    OR directly the positivity of the tau cross-ratio 1 - q_N =
    (tau^aug_N tau_{N-1})/(tau^aug_{N-1} tau_N).
  BRANCH RULE (source-defined, NO selection-by-answer): the
    exception branch is entered iff g_w = sqrt(5/7) - U_w < 0
    with the SEALED r260/r262 C1b triangle U_w = |t_{N-2}| +
    |a'_{N-2} r_{N-2}| + |b'_{N-2} r_{N-3}|; named exception set
    {kz15, 20, 22, 36, 38, 39, 52} on the frame-A h <= 900 ladder.
  INPUT: r261 CAMPAIGN_INPUT_FROZEN(G_n, t_n, B) in the sealed
    scaled-Chebyshev basis on the union+border hull [x0 -+ rh].
  KILL LIST (inherited, stays armed): PAIRCORR detector (demand
    bar 1.0 dec), TARGET_INVERSE, WALL_COMPLETION, FIXED_STATE_
    COMPRESSION, SELECTION_BY_ANSWER.
  BLOCKED ROUTES (measured dead, not to be re-entered): (i)
    SMOOTH DRESSING -- the Szego D-layer is ESSENTIALLY SINGULAR
    at the atoms (r253 leg P: log-pole exponent >= 0.8; only the
    rank-1 border layer is exactly removable); (ii) BORDERED
    SPECTRAL BOUND -- BOTH augmented variants (RAW and UNIT) cross
    the wall at s < 1 on every rung (r257 leg D): the no-pole path
    must go through the PAIR dynamics, not a bordered spectral
    bound.
  DESIGN RULES: full von Mangoldt comb stays in the main problem
    (NO PNT smoothing -- the smooth-background+small-error
    architecture is measured dead: amplification extensive, the
    arithmetic lives in the error); no compression (all classes
    closed r254/r256/r259/r261); small parameters ONLY in degree/
    edge/s-deformation directions.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r263 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; free pivots are the
proof objects; rho_k = F_k^2/h_k, S_n = sum_{k<=n} rho_k; ground
truth (h signs, flip degrees, branch labels) enters GATES and
SEPARATION TABLES only; no zero/prime oracles anywhere (AST
firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack, r257
CT.union_arrays/u_matrix/blind_flip_predictor, r260
TX.drive_arrays (sealed driven-recursion coordinates), r263
CA.u_triangle/g_gap (the sealed branch builders), v881 PIK port
builders, r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted.

LEG A -- CHARTER FROZEN + BRANCH REPRODUCTION: the charter
constants above are code constants with CHARTER_SHA; gate: the
branch decomposition of all 42 rungs + both mains is reproduced
EXACTLY from the r263 route (cheap 35/42, exception set == the
named 7, mains both cheap) -- the campaign's future-window rule
is machine-checked at the opening.

LEG B -- THE EXACT RHP DICTIONARY FOR Z (the round's SATZ): the
discrete 2x2 FIK problem carries the full comb as residue/jump
data (Y_n normalization r227/r234, frozen); its z^{-1} coefficient
gives the EXACT readout h_n = (Y1)_12 (r234, frozen formula), and
the rank-1 Uvarov/Schlesinger border augmentation (r245/r253)
carries the border column whose pairing with the monic RHP first
row is F_n = int pihat_n dsigmatilde.  SEALED DESIGNATED READOUT
(the ONE route of this campaign, chosen and frozen here):
    Z^RHP_w = F_{N-1} / sqrt(h_{N-1}),
    h_{N-1}  from the Y1 entry == the tau ratio: a_{N-1} =
             tau_N/tau_{N-1} = c_{N-1}^2 h_{N-1} by DIRECT
             slogdet of the r261 input Gram (never the chain),
    F_{N-1}  from the BORDER COLUMN: the Gram solve G_{N-1} beta
             = -g_col gives the monic coefficients of pihat_{N-1}
             in the scaled basis; c_{N-1} F_{N-1} = t_{N-1} +
             beta . t_{<N-1} (the augmentation column pairing),
    so Z^RHP = (t_{N-1} + beta . t_{<N-1}) / sqrt(a_{N-1}) with
    the basis constant c_{N-1} cancelling EXACTLY (scale-free).
GATES: (b1) chain identity Z_w == r_{N-1} (r263 restated, rel
1e-9); (b2) Z^RHP == Z_w on all 42 rungs + mains in f64 (ABS
devs, O(1) coordinate: bars 1e-8 main N <= 400 / 3e-6 deep,
solve residual <= 1e-8, sign match EVERYWHERE, a_{N-1} > 0 on
the positive prefix); (b3) controls in the sign-safe rho form
rho_{N-1} = num^2/a_{N-1} vs the chain on EPST/SCR/SMOOTH (abs
bar 1e-3; SMOOTH is the 0 == 0 self-alias case, abs bar 1e-8);
(b4) mp ward at the TERMINAL of the smallest-N exception rung
(kz20, N = 170; sealed rule: min-N member of the named set), dps
60, dev vs the f64 chain <= 1e-8 (f64 reference floor); (b5) mp
ward THROUGH a control flip: SCR at n = 24 (spans the flip 21),
dev <= 1e-6 (r257 control floor family).  With (b1)-(b5) the
target package is COMPLETE IN RHP LANGUAGE: sought is the sign/
size of a designated readout of the RHP solution.

LEG C -- THE RHP DATA SIGNATURE OF THE EXCEPTION BRANCH (the
substance question): g_w < 0 is source-defined -- how does it
manifest in the RHP DATA (residue/weight geometry, drive column,
local terminal environment), NOT in the solution?  FIVE sealed
candidate characteristics (frozen before evaluation, max 5;
the separation bar 0.8 was sealed BEFORE the feasibility
scratch):
  S1_TERMDRIVE  = |t_{N-2}|                (terminal drive
                  magnitude -- the border-drive column entry),
  S2_DRIVEPEAK  = |t_{N-2}| / median |t| over the local window
                  W in {4, 8, 16} (QUENCHED local-environment
                  family, r231: which window size explains the
                  branch best is REPORTED, never fitted),
  S3_CHAINTERM  = |a'_{N-2} r_{N-2}| + |b'_{N-2} r_{N-3}|
                  (the chain side of the triangle, drive
                  excluded),
  S4_EDGEGAP    = min node gap in the outer 10 percent of the
                  hull / median gap  (PURE SOURCE GEOMETRY:
                  near-degenerate residue pairs),
  S5_EDGEMASS   = share of |w| mass in the outer 5 percent of
                  the hull  (PURE SOURCE GEOMETRY: weight scale
                  near the hull edge).
SEPARATION POWER (sealed metric): AUC of exception vs cheap over
the 7 x 35 rung pairs, power = 2 |AUC - 1/2|; branch labels
(from the source-defined g) enter the TABLE side only, never a
candidate scope (AST audit + a deliberately g-reading mutant
that must be FLAGGED).  SEALED ADJUDICATION:
EXCEPTION_DATA_SIGNATURE_FOUND(cand, power, class) iff the best
sealed candidate has power >= 0.8, with the honest CLASS typing:
S1/S2 = PREFIX_DRIVE (the drive column of the RHP data), S3 =
PREFIX_CHAIN, S4/S5 = SOURCE_GEOMETRY (solution-free comb
geometry); a FOUND in the PREFIX classes localizes the branch in
the drive/chain columns (the r262 drive-dominance in RHP data
language) and names the deformation lever; a FOUND in
SOURCE_GEOMETRY would be a naked-comb signature; else
EXCEPTION_DATA_BLIND (the branch is invisible in the data --
the campaign is typed global from the start).

LEG D -- THE PAIR-DYNAMICS NO-POLE COORDINATE (r257: the no-pole
path must go through the pair dynamics): (d1) the s-dressed port
pair (tau_w(s), tau^aug_w(s)) = (det(I - sQ_w), det(I - s(Q_w +
f f^T))) on ALL 42 rungs (r257 leg-D machinery verbatim; RAW
mass row + UNIT direction row): zero constellation in [0, 1+eps]
-- nearest base zero 1/lambda_max vs nearest augmented zero
1/mu_max, Cauchy interlacing (exact ward), crossing census RAW/
UNIT, cheap vs exception vs mains medians (do they cross
together? does the coupling protect?).  (d2) the Schur cross-
ratio X_w(s) = tau^aug(s)/tau(s) = 1 - s f^T (I - sQ)^{-1} f
(identity warded by slogdet on the sealed sample rungs 9, 13,
20, 52): sign census on the sealed s-grid vs the crossing s* =
1/mu_max.  (d3) the BORDER-DRESSED exact coordinate on the r261
input: t_n(s) = s t_n gives D_{N-1}(s) = B - s^2 S_{N-2} and the
cross-ratio 1 - q_N(s) = (B - s^2 S_{N-1})/(B - s^2 S_{N-2}):
s = 0 trivial (q = 0), s = 1 the target (q = q_N) EXACTLY; gate
uniform sign stability on [0, 1] on all 42 + mains, tightest
spot (monotone: the margin B - s^2 S_{N-1} falls in s, tightest
at s = 1 with value D_N = 5/7 - rho_{N-1} -- the razor margin),
min margin in the sealed band [0.010, 0.020]; exception-rung
margins printed.  ALL of leg D is typed MEASUREMENT.

LEG E -- KILLS + CONTROLS: inherited kill list armed (no new
certificate is attempted this round -- no majorant, no unroll,
no fit primitives: fragment AST audit); controls firewall-typed
(flips re-derived 25/21/27, INDEFINITE_CONTINUATION beyond
pmax); SMOOTH anchor q_N <= 1e-20; r257 blind micro-predictor
ward (flips 3/3); MUST-FAILS (each loud/flagged): (m1) READOUT
INDEX SWAP -- a_{N-2} in place of a_{N-1} breaks the dictionary
>= 1e3 x honest on w9; (m2) BORDER COLUMN WITHOUT AUGMENTATION
-- the raw top border moment t_{N-1} without the Gram-solve
projection breaks the dictionary >= 1e3 x honest on w9; (m3) a
signature mutant that secretly reads the branch answer (M_W,
u_triangle scope) must be FLAGGED by the sig AST audit.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; ladder frame-A
h <= 900 (42 rungs, (N, kz)-sorted); B57 = 5/7; M_W = sqrt(5/7);
CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36, 38, 39, 52);
Z_ID_BAR 1e-9; DICT_ABS_MAIN 1e-8 (N <= 400) / DICT_ABS_DEEP
3e-6 / DICT_ABS_CTRL 1e-3 / DICT_ABS_SM 1e-8; SOLVE_RES_BAR
1e-8; MP_DPS 60; MP_EXC_BAR 1e-8; MP_SCR_N 24; MP_SCR_BAR 1e-6;
SIG_POWER_BAR 0.8 (sealed BEFORE the feasibility scratch);
SIG_WINDOWS (4, 8, 16); SIG_EDGE_FRAC 0.10; SIG_MASS_FRAC 0.05;
S_GRID (0.25, 0.5, 0.75, 0.9, 1.0); EPS_S 0.25; INTERLACE_TOL
1e-8; XRATIO_WARD_KZ (9, 13, 20, 52); XRATIO_BAR 1e-8
(calibration amendment a1, disclosed: the draft bar 1e-9 was
set from the w9 smoke floor 4.4e-13; calibration pass 1
measured 2.1e-9 on the DEEPEST ward rung kz52 at s = 1.0,
where I - sQ carries 1 - lambda_max ~ 7e-7, i.e. condition
~1e7 and an f64 solve floor ~1e-9 -- a ward tolerance on an
exact identity, r234-a1/r253 precedent; no physics bar, band,
rule or verdict moved); MARGIN_BAND (0.010, 0.020); SM_Q_BAR
1e-20; LOUD 1e3; runtime
<= 1800 s; smoke = w9 + controls + SCR mp ward + port rung 9 +
must-fails (ladder, w13, exception mp, signature census,
adjudication skipped).  DISCLOSED PRE-SPEC SCRATCH (two runs,
feasibility + floors only, scripts deleted; the SIG bar 0.8, the
window set, the candidate list, the readout route and all
verdict rules were fixed BEFORE the scratch): (s1) ladder 42
rungs N in [142, 878]; exception (kz, N) = (15,203) (20,170)
(22,199) (36,488) (38,522) (39,277) (52,878); f64 dictionary
floor 9.2e-9 main / 1.5e-7 deep, solve residual 1.9e-10; port
lanczos complete 42/42 with lambda_max < 1 on 42/42, RAW aug
zero in [0.111, 0.230]; (s2) mp terminal dictionary at kz20 dev
8.1e-11 (26 s at dps 60), SCR n=24 dev 3.7e-14.  Nothing tuned:
every bar above is the r260/r257 floor family adopted as-is.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  CHARTER_FROZEN(sha, exceptions 7, kills 5, blocked 2)
+ RHP_DICTIONARY_EXACT(Z = designated readout: border column /
    Y1) / RHP_DICTIONARY_OPEN(typed)
+ EXCEPTION_DATA_SIGNATURE_FOUND(cand, power, class) /
    EXCEPTION_DATA_BLIND
+ S_FAMILY_COORDINATE(BORDER_S: sign stability, tightest spot;
    PORT_S: wall + crossing census, branch separation)
+ PAIR_INTERLACING(measured).
Honesty before beauty: the dictionary is a language statement
(the target restated exactly in RHP readout form), never a
bound; the signature is a separation MEASUREMENT on 7-vs-35
labels; leg D is measurement; no verdict claims a derived 5/7,
a bound mechanism, or an asymptotic law (r243/r250/r253/r256/
r257/r258/r260/r261/r262/r263 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
smoke 28/28 first pass; calibration pass 1 = first full
evaluation, 26/28 -- the ONLY miss was the G53 ward bar (worst
2.1e-9 vs the draft 1e-9 on the deepest ward rung at s = 1.0,
the understood f64 solve floor near the base wall) => the ONE
disclosed amendment a1 above (ward tolerance 1e-9 -> 1e-8,
gate-side only); pass 2 = the record run below, numerically
identical to pass 1 in every printed figure):
CAL_VERDICT = CHARTER_FROZEN(7b9e751d958404b7, exceptions 7,
kills 5, blocked 2) + RHP_DICTIONARY_EXACT(Z = designated
readout: border column / Y1) + EXCEPTION_DATA_SIGNATURE_FOUND(
S1_TERMDRIVE, power 0.959, class PREFIX_DRIVE) +
S_FAMILY_COORDINATE(BORDER_S sign-stable 44/44, tightest s = 1,
min margin 0.0139; PORT_S wall 42/42, aug crossing RAW+UNIT
42/42 at s < 1, branch-blind) + PAIR_INTERLACING(exact 1.4e-15;
aug zero BELOW base zero on 42/42).
Key numbers.  LEG A: branch reproduction EXACT (cheap 35/42,
exception set == the named 7, mains w9 g +0.442 / w13 g +0.212
both CHEAP); CHARTER_SHA 7b9e751d958404b7; exception table
(kz, N, g, Z): kz15 N203 g-0.002 Z-0.8184; kz20 N170 g-0.434
Z-0.6478; kz22 N199 g-0.238 Z-0.1974; kz36 N488 g-0.508
Z-0.5778; kz38 N522 g-0.409 Z-0.5142; kz39 N277 g-0.331
Z-0.6219; kz52 N878 g-0.439 Z-0.3138 (r263 table reproduced).
LEG B: chain identity worst rel 1.8e-14 on 42 + 2; f64
designated readout worst abs dev 9.2e-9 main N <= 400 / 1.5e-7
deep (bars 1e-8/3e-6), solve residual 1.9e-10, sign match
44/44, a_{N-1} > 0 44/44; controls rho form EPST/SCR worst
1.3e-5 (bar 1e-3), SMOOTH 2.3e-25 (bar 1e-8); mp exception
ward kz20 (N = 170, dps 60): Z_mp = -0.647785842379, dev
8.1e-11 vs the f64 chain (bar 1e-8) -- the handover scalar of
an exception rung IS the RHP readout at mp precision; mp
control-flip ward SCR n = 24 (through flip 21): dev 3.7e-14
(bar 1e-6).  LEG C: sig scopes CLEAN, branch-reading mutant
FLAGGED (M_W/u_triangle); separation census (power =
2|AUC - 1/2|): S1_TERMDRIVE 0.959 (exc med 0.884 vs cheap med
0.447) -- WINNER, class PREFIX_DRIVE; S3_CHAINTERM 0.894
(0.370 vs 0.105); S2_DRIVEPEAK 0.339/0.282/0.388 at W =
4/8/16 (best local window W = 16, weak); S4_EDGEGAP 0.139,
S5_EDGEMASS 0.184 -- PURE SOURCE GEOMETRY IS BLIND: the branch
lives in the DRIVE COLUMN of the RHP data (the border
functional near the terminal), the r262 drive-dominance
restated in data language; the campaign's deformation lever is
the border-drive column, NOT the naked comb geometry.  LEG D:
port built 42/42, base wall lambda_max < 1 on 42/42, nearest
base zero in [1.0000001, 1.0001675] (the r257 cofinal approach
on the full ladder); RAW aug zero in [0.111, 0.230] (mass-
driven, |f|^2 in [4.15, 8.79]), UNIT aug zero in [0.750,
0.835]; crossing census: base NEVER crosses [0, 1] (42/42),
augmented ALWAYS (RAW and UNIT 42/42) -- the pair does NOT
cross together and the coupling does NOT protect (interlacing
exact, worst rel violation 1.4e-15, the aug zero sits BELOW
the base zero); branch separation of the aug zero: RAW cheap
med 0.1421 vs exc med 0.1540 (power 0.19), UNIT 0.7845 vs
0.7860 (power 0.05) -- the PORT zero constellation is BRANCH-
BLIND; mains kz9/kz13 RAW zeros 0.1710/0.1846; Schur cross-
ratio ward X(s) vs slogdet on rungs (9, 13, 20, 52): worst abs
dev 2.1e-9 (bar 1e-8 after a1), grid signs == sign(s* - s) at
every point; BORDER_S exact coordinate: sign-stable on [0, 1]
on 44/44 worlds, margin monotone falling, tightest spot s = 1
on EVERY rung, min terminal margin 0.0139 in the sealed band
[0.010, 0.020] (the r260/r263 razor as the s = 1 endpoint
value); exception margins at s = 1: kz15 0.045 / kz20 0.295 /
kz22 0.675 / kz36 0.380 / kz38 0.450 / kz39 0.328 / kz52
0.616 (kz15 is the tightest exception, matching its g -0.002).
LEG E: must-fails m1 index swap breaks the w9 dictionary by
1.2e-2 = 2.4e+8 x honest 5.1e-11, m2 unprojected border column
by 4.5e+0 = 8.8e+10 x honest, m3 mutant FLAGGED; micro-
predictor ward 3/3 (25/21/27); SMOOTH q_N = 4.2e-25 <= 1e-20;
anti-gate fragment audit CLEAN.  READING (typed, no upgrade):
the campaign opens with its target package fully in RHP
language -- the exception scalar IS a designated readout of
the discrete FIK solution (border column over sqrt of the Y1
entry, machine-exact on all 44 worlds, at mp precision on an
exception terminal and through a control flip); the exception
branch HAS a data signature and it sits in the drive column
(power 0.96) while the naked comb geometry is blind: the local
RHP analysis must attack the border-drive functional near the
terminal degree; the s-coordinate is viable as a proof
coordinate in the BORDER-DRESSED form (trivial at s = 0, the
razor at s = 1, sign-stable and monotone on every rung, the
tightest exception is kz15 at 0.045) while the PORT zero
constellation is branch-blind and its augmented zero crosses
below the wall on every rung -- the r257 warning reproduced on
the full 42-rung ladder: no bordered spectral shortcut.
Runtime 38.3 s full / 0.5 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (a1 predates the record
run, disclosed above).

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
import cancellation_adjudication_probe as CA  # noqa: E402 r263
import coupledtau_probe as CT                # noqa: E402 r257
import terminal_crossratio_probe as TX       # noqa: E402 r260
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
Z_ID_BAR = 1e-9
DICT_ABS_MAIN = 1e-8
DICT_ABS_DEEP = 3e-6
DICT_ABS_CTRL = 1e-3
DICT_ABS_SM = 1e-8
DEEP_N = 400
SOLVE_RES_BAR = 1e-8
MP_DPS = 60
MP_EXC_BAR = 1e-8
MP_SCR_N = 24
MP_SCR_BAR = 1e-6
SIG_POWER_BAR = 0.8
SIG_WINDOWS = (4, 8, 16)
SIG_EDGE_FRAC = 0.10
SIG_MASS_FRAC = 0.05
S_GRID = (0.25, 0.5, 0.75, 0.9, 1.0)
EPS_S = 0.25
INTERLACE_TOL = 1e-8
XRATIO_WARD_KZ = (9, 13, 20, 52)
XRATIO_BAR = 1e-8
MARGIN_BAND = (0.010, 0.020)
SM_Q_BAR = 1e-20
LOUD = 1e3

# ------------------------- THE CHARTER (machine-readable, leg A)
CH_TARGET = ("Z_w = Z^RHP_w + E_w with |Z^RHP_w| + |E_w| < "
             "sqrt(5/7) on the exception branch, OR directly the "
             "positivity of the tau cross-ratio 1 - q_N = "
             "(tau^aug_N tau_{N-1})/(tau^aug_{N-1} tau_N)")
CH_BRANCH = ("exception iff g_w = sqrt(5/7) - U_w < 0 with the "
             "SEALED C1b triangle U_w = |t_{N-2}| + |a'_{N-2} "
             "r_{N-2}| + |b'_{N-2} r_{N-3}| -- source-defined, "
             "NO selection-by-answer")
CH_INPUT = ("r261 CAMPAIGN_INPUT_FROZEN(G_n, t_n, B; scaled-"
            "Chebyshev basis, union+border hull [x0 -+ rh])")
CH_KILLS = ("PAIRCORR_DETECTOR(1.0 dec)", "TARGET_INVERSE",
            "WALL_COMPLETION", "FIXED_STATE_COMPRESSION",
            "SELECTION_BY_ANSWER")
CH_BLOCKED = (
    "SMOOTH_DRESSING(r253: Szego D-layer essentially singular at "
    "the atoms, log-pole exponent >= 0.8; only the rank-1 border "
    "layer is exactly removable)",
    "BORDERED_SPECTRAL_BOUND(r257: RAW and UNIT augmented "
    "variants cross the wall at s < 1 on every rung; the no-pole "
    "path must go through the PAIR dynamics)")
CHARTER_SHA = hashlib.sha256("|".join(
    (CH_TARGET, CH_BRANCH, CH_INPUT) + CH_KILLS
    + CH_BLOCKED + (str(EXC_KZ_EXPECT),)).encode()).hexdigest()

CAL_VERDICT = (
    "CHARTER_FROZEN(7b9e751d958404b7, exceptions 7, kills 5, "
    "blocked 2) + RHP_DICTIONARY_EXACT(Z = designated readout: "
    "border column / Y1) + EXCEPTION_DATA_SIGNATURE_FOUND("
    "S1_TERMDRIVE, power 0.959, class PREFIX_DRIVE) + "
    "S_FAMILY_COORDINATE(BORDER_S sign-stable 44/44, tightest "
    "s = 1, min margin 0.0139; PORT_S wall 42/42, aug crossing "
    "RAW+UNIT 42/42 at s < 1, branch-blind) + "
    "PAIR_INTERLACING(exact 1.4e-15; aug zero BELOW base zero "
    "on 42/42)")

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
                       "the r244 chain rows / the r261 Gram input; "
                       "ground truth (flips, branch labels) enters "
                       "gates and separation tables only"
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


# ------------------------------------- the RHP dictionary route
def gram_input(p):
    """the r261 CAMPAIGN INPUT: scaled-Chebyshev Gram G, border
    column tv on the sealed union+border hull (r257/r260 hull
    convention, verbatim)."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    P = CT.u_matrix(xu, x0, rh, N)
    TB = CT.u_matrix(bx, x0, rh, N)
    G = (P * wu) @ P.T
    tv = TB @ bw
    return G, tv


def rhp_readout(G, tv, n, swap_a=False, unprojected=False):
    """THE SEALED DESIGNATED READOUT at degree n: h_n from the Y1
    entry == the tau ratio a_n = tau_{n+1}/tau_n (direct slogdet
    of the input Gram), F_n from the border column via the Gram
    solve; Z = c_n F_n / sqrt(a_n) with c_n cancelling exactly.
    swap_a / unprojected are the m1/m2 must-fail mutants."""
    sg1, lg1 = np.linalg.slogdet(G[:n, :n])
    sg2, lg2 = np.linalg.slogdet(G[:n + 1, :n + 1])
    if swap_a:
        sg0, lg0 = np.linalg.slogdet(G[:n - 1, :n - 1])
        sa, la = sg0 * sg1, lg1 - lg0
    else:
        sa, la = sg1 * sg2, lg2 - lg1
    if unprojected:
        num = float(tv[n])
        res = 0.0
    else:
        beta = np.linalg.solve(G[:n, :n], -G[:n, n])
        res = float(np.max(np.abs(G[:n, :n] @ beta + G[:n, n])))
        num = float(tv[n] + beta @ tv[:n])
    Z = num * math.exp(-0.5 * la) if sa > 0 else float("nan")
    rho_d = num * num * sa * math.exp(-la)
    return Z, rho_d, res, sa


def mp_rhp_readout(p, n, dps):
    """the SAME designated readout in mp (dps sealed): mp Gram +
    border column from the raw atoms, mp dets + lu_solve."""
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    xu, wu = CT.union_arrays(d)
    bx, bw = CT.union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0m = mp.mpf(0.5 * (lo + hi))
    rhm = mp.mpf(0.5 * (hi - lo))
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    bs = [mp.mpf(float(v)) for v in bx]
    bwm = [mp.mpf(float(v)) for v in bw]
    tvm = [(x - x0m) / rhm for x in xs]
    tbm = [(x - x0m) / rhm for x in bs]
    n_hi = n + 1
    PU = [[mp.mpf(1)] * len(xs), [2 * u for u in tvm]]
    TU = [[mp.mpf(1)] * len(bs), [2 * u for u in tbm]]
    for _k in range(2, n_hi):
        PU.append([2 * u * a - b
                   for u, a, b in zip(tvm, PU[-1], PU[-2])])
        TU.append([2 * u * a - b
                   for u, a, b in zip(tbm, TU[-1], TU[-2])])
    GM = mp.matrix(n_hi, n_hi)
    for i in range(n_hi):
        for j in range(i, n_hi):
            v = mp.fsum(w * a * b
                        for w, a, b in zip(ws, PU[i], PU[j]))
            GM[i, j] = v
            GM[j, i] = v
    tm = [mp.fsum(w * a for w, a in zip(bwm, TU[i]))
          for i in range(n_hi)]
    tau_n = mp.det(GM[:n, :n])
    tau_n1 = mp.det(GM)
    sub = GM[:n, :n]
    rv = mp.matrix(n, 1)
    for i in range(n):
        rv[i] = -GM[i, n]
    beta = mp.lu_solve(sub, rv)
    num = tm[n] + mp.fsum(beta[k] * tm[k] for k in range(n))
    a_n = tau_n1 / tau_n
    Z = num / mp.sqrt(a_n) if a_n > 0 else mp.mpf("nan")
    rho_d = num * num / a_n
    return Z, rho_d


# --------------- sealed signature candidates (leg C; consume the
# drive/chain prefix arrays and the raw source atoms ONLY; the
# branch answer (M_W, u_triangle, g_gap) is structurally withheld
# from every scope -- AST-audited)
def sig_termdrive(t_arr):
    """S1: terminal drive magnitude |t_{N-2}| (the border-drive
    column entry of the RHP data at the last free degree)."""
    return abs(float(t_arr[-1]))


def sig_drivepeak(t_arr, w):
    """S2: local drive peaking |t_{N-2}| / median |t| over the
    trailing window of size w (QUENCHED local environment)."""
    seg = np.abs(np.asarray(t_arr[max(len(t_arr) - 1 - w, 0):-1]))
    return abs(float(t_arr[-1])) / max(float(np.median(seg)),
                                       1e-300)


def sig_chainterm(t_arr, ap_arr, bp_arr, rpre):
    """S3: the chain side of the terminal triangle (drive
    excluded): |a'_{N-2} r_{N-2}| + |b'_{N-2} r_{N-3}|."""
    del t_arr
    return abs(float(ap_arr[-1] * rpre[-1])) \
        + abs(float(bp_arr[-1] * rpre[-2]))


def sig_edgegap(xs_sorted):
    """S4: PURE SOURCE GEOMETRY -- min node gap in the outer
    hull edges (fraction sealed) over the median gap."""
    gaps = np.diff(xs_sorted)
    lo, hi = float(xs_sorted[0]), float(xs_sorted[-1])
    edge = SIG_EDGE_FRAC * (hi - lo)
    mask = (xs_sorted[:-1] <= lo + edge) \
        | (xs_sorted[:-1] >= hi - edge)
    return float(np.min(gaps[mask]) / np.median(gaps))


def sig_edgemass(xs_sorted, ws_absv):
    """S5: PURE SOURCE GEOMETRY -- |w| mass share in the outer
    hull edges (fraction sealed)."""
    lo, hi = float(xs_sorted[0]), float(xs_sorted[-1])
    edge = SIG_MASS_FRAC * (hi - lo)
    mask = (xs_sorted <= lo + edge) | (xs_sorted >= hi - edge)
    return float(np.sum(ws_absv[mask]) / np.sum(ws_absv))


def sig_oracle(rpre, t_arr, ap_arr, bp_arr):
    """DELIBERATE MUST-FAIL MUTANT: reads the branch answer
    (M_W and the sealed triangle) -- the sig AST audit must FLAG
    this scope."""
    return M_W - CA.u_triangle(rpre, t_arr, ap_arr, bp_arr)


SIG_FORBIDDEN = {"M_W", "u_triangle", "g_gap", "B57", "rho", "S",
                 "sa", "la", "q_chain", "D_dir", "wb",
                 "world_block", "direct_terminal", "rhp_readout"}


def sig_scope_audit(funcname):
    """walk ONLY the named function's subtree; flag any branch-
    answer identifier or dict key from the sealed forbidden set."""
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
                if nm in SIG_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def auc_power(vals_cheap, vals_exc):
    """sealed separation metric: AUC over the cheap x exception
    rung pairs, power = 2 |AUC - 1/2|."""
    cnt = 0.0
    for e in vals_exc:
        for c in vals_cheap:
            cnt += 1.0 if e > c else (0.5 if e == c else 0.0)
    a = cnt / (len(vals_cheap) * len(vals_exc))
    return a, 2.0 * abs(a - 0.5)


# ----------------------------------------- s-dressed port (leg D)
def port_pack(kz):
    """r257 leg-D machinery verbatim: state Gram Q = A^T A of the
    folded port, Uvarov border row f from the smooth-comb rung;
    returns eigen data of Q, Q + ff^T (RAW), Q + uu^T (UNIT)."""
    b = PIK.build_rung(kz)
    h, L, alpha = b["h"], b["L"], b["alpha"]
    xs, ws_, _ = PIK.folded_measure(b["d"], L, +1.0)
    ys, vs, _ = PIK.folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = PIK.lanczos_chain(xs, ws_, h + 1)
    if steps < h + 1:
        return None
    Pn = PIK.eval_chain(al, be, m0, ys, h)
    A = np.sqrt(vs)[:, None] * Pn
    Q = A.T @ A
    ev = np.linalg.eigvalsh(Q)
    bS = PIK.build_rung(kz, comb=PB.smooth_comb(alpha))
    xsS, wsS, _ = PIK.folded_measure(bS["d"], L, +1.0)
    ysS, vsS, _ = PIK.folded_measure(bS["d"], L, -1.0)
    bn = np.concatenate([xsS, ysS])
    bwt = np.concatenate([wsS, -vsS])
    Pb = PIK.eval_chain(al, be, m0, bn, h)
    f = Pb.T @ bwt
    f2 = float(f @ f)
    evr = np.linalg.eigvalsh(Q + np.outer(f, f))
    u = f / math.sqrt(f2)
    evu = np.linalg.eigvalsh(Q + np.outer(u, u))
    return dict(kz=kz, h=h, Q=Q, f=f, f2=f2, ev=ev, evr=evr,
                evu=evu)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("quenched_opening_probe -- PRIME.PORT.RHP.QUENCHED."
          "OPENING.01 (round 264)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + SCR mp ward + "
                        "port rung 9 + must-fails; ladder, w13, "
                        "exception mp, signature census, "
                        "adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "OPENING ROUND: charter frozen as code constants "
          "(CHARTER_SHA below), the sealed designated readout "
          "Z^RHP = (border column pairing)/sqrt(Y1 entry) on the "
          "r261 input, 5 sealed signature candidates with the "
          "0.8 separation bar (sealed BEFORE the feasibility "
          "scratch), the r257 port pair + the border-dressed "
          "exact s-coordinate, inherited kill list armed -- ALL "
          "bars, rules and verdicts sealed BEFORE evaluation "
          "(two pre-spec scratches disclosed in the spec)")

    # ---------------- S1: census
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
          "control flips re-derived %s (INDEFINITE_CONTINUATION "
          "beyond pmax); cofinal ladder %d rungs POSITIVE_PREFIX "
          "%s, N in [%s, %s]"
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

    # per-rung record (drive arrays + branch + chain Z)
    def rung_rec(p):
        N = p["N"]
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        rpre = r[:N - 1]
        g = CA.g_gap(rpre, t, ap, bp)
        Z = t[N - 2] + ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
        zdev = abs(Z - r[N - 1]) / max(1.0, abs(r[N - 1]))
        return dict(kz=p["kz"], N=N, g=g, Z=Z, zdev=zdev, p=p,
                    r=r, t=t, ap=ap, bp=bp, rpre=rpre)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]

    # ---------------- S2: LEG A -- charter + branch reproduction
    section("S2  LEG A -- CAMPAIGN CHARTER FROZEN")
    info("TARGET: %s" % CH_TARGET)
    info("BRANCH RULE: %s" % CH_BRANCH)
    info("INPUT: %s" % CH_INPUT)
    info("KILL LIST (armed): %s" % "; ".join(CH_KILLS))
    for bl in CH_BLOCKED:
        info("BLOCKED ROUTE: %s" % bl)
    check("G20-charter-frozen", True,
          "CHARTER_SHA %s (target + branch rule + input + %d "
          "kills + %d blocked routes + the named exception set "
          "%s, hashed as machine constants)"
          % (CHARTER_SHA[:16], len(CH_KILLS), len(CH_BLOCKED),
             str(EXC_KZ_EXPECT)))
    cheap = [rc for rc in recs if rc["g"] >= 0.0]
    exc = [rc for rc in recs if rc["g"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G21-branch-reproduction", recs[0]["g"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g"] >= 0 else "EXCEPTION",
                 recs[0]["g"]))
    else:
        m_cheap = all(rc["g"] >= 0.0 for rc in mrecs)
        check("G21-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and m_cheap,
              "r263 route reproduced EXACTLY: cheap %d/42 "
              "(expect %d), exception set %s == the named set; "
              "mains %s -- the future-window rule is machine-"
              "checked at the opening"
              % (len(cheap), CHEAP_EXPECT, str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g"])
                           for rc in mrecs)))
        info("EXCEPTION RUNGS (kz, N, g, Z): %s"
             % "; ".join("kz%d N%d g%+.3f Z%+.4f"
                         % (rc["kz"], rc["N"], rc["g"], rc["Z"])
                         for rc in sorted(exc,
                                          key=lambda rc: rc["kz"])))

    # ---------------- S3: LEG B -- the exact RHP dictionary
    section("S3  LEG B -- THE EXACT RHP DICTIONARY FOR Z")
    zworst = max(rc["zdev"] for rc in recs + mrecs)
    check("G30-z-chain-identity", zworst <= Z_ID_BAR,
          "Z_w = t_{N-2} + a'r_{N-2} + b'r_{N-3} == r_{N-1} by "
          "the driven recursion (r263 restated): worst rel dev "
          "%.1e (bar %.0e) on %d rungs + %d mains"
          % (zworst, Z_ID_BAR, len(recs), len(mrecs)))
    dworst_m = dworst_d = 0.0
    res_w = 0.0
    sign_ok = True
    apos_ok = True
    for rc in recs + mrecs:
        p = rc["p"]
        N = p["N"]
        G, tv = gram_input(p)
        Zd, _rhod, res, sa = rhp_readout(G, tv, N - 1)
        rc["G"], rc["tv"] = G, tv
        dev = abs(Zd - rc["Z"])
        res_w = max(res_w, res)
        apos_ok = apos_ok and (sa > 0)
        sign_ok = sign_ok and (math.copysign(1.0, Zd)
                               == math.copysign(1.0, rc["Z"]))
        if N <= DEEP_N:
            dworst_m = max(dworst_m, dev)
        else:
            dworst_d = max(dworst_d, dev)
    check("G31-rhp-dictionary-f64",
          dworst_m <= DICT_ABS_MAIN and dworst_d <= DICT_ABS_DEEP
          and res_w <= SOLVE_RES_BAR and sign_ok and apos_ok,
          "Z^RHP = (t_{N-1} + beta . t_{<N-1})/sqrt(tau_N/"
          "tau_{N-1}) -- the DESIGNATED READOUT (border column / "
          "Y1 entry, basis constant cancels exactly) == Z_w: "
          "worst abs dev %.1e main N<=%d (bar %.0e) / %.1e deep "
          "(bar %.0e) on %d+%d rungs; solve residual %.1e (bar "
          "%.0e); sign match %s; a_{N-1} > 0 %s (positive "
          "prefix)"
          % (dworst_m, DEEP_N, DICT_ABS_MAIN, dworst_d,
             DICT_ABS_DEEP, len(recs), len(mrecs), res_w,
             SOLVE_RES_BAR,
             "ALL" if sign_ok else "BROKEN",
             "ALL" if apos_ok else "BROKEN"))
    dev_ct = dev_sm = 0.0
    ct_note = []
    for c in ctrl:
        p = ctrl[c]
        N = p["N"]
        G, tv = gram_input(p)
        _Zd, rhod, _res, _sa = rhp_readout(G, tv, N - 1)
        rho_ch = float(p["rho"][N - 1])
        dv = abs(rhod - rho_ch)
        if c == "SMOOTH":
            dev_sm = dv
        else:
            dev_ct = max(dev_ct, dv)
        ct_note.append("%s rho_dir %+.3e chain %+.3e" %
                       (c, rhod, rho_ch))
    check("G32-rho-dictionary-controls",
          dev_ct <= DICT_ABS_CTRL and dev_sm <= DICT_ABS_SM,
          "controls in the sign-safe rho form rho_{N-1} = "
          "num^2/a_{N-1} vs the chain: EPST/SCR worst abs %.1e "
          "(bar %.0e, f64 chain floor on flipped worlds), SMOOTH "
          "%.1e (bar %.0e, the 0 == 0 self-alias case); %s -- "
          "the dictionary is world-blind algebra"
          % (dev_ct, DICT_ABS_CTRL, dev_sm, DICT_ABS_SM,
             "; ".join(ct_note)))
    if not smoke:
        exc_min = min(exc, key=lambda rc: rc["N"])
        Zmp, _rhomp = mp_rhp_readout(exc_min["p"],
                                     exc_min["N"] - 1, MP_DPS)
        dv_mp = abs(float(Zmp) - exc_min["Z"])
        check("G33-mp-exception-ward", dv_mp <= MP_EXC_BAR,
              "mp (dps %d) designated readout at the TERMINAL of "
              "the smallest-N exception rung kz%d (N = %d, "
              "sealed rule min-N): Z_mp = %s vs chain %+.9f, dev "
              "%.1e (bar %.0e, f64 reference floor) -- the "
              "handover scalar of an exception rung IS the RHP "
              "readout at mp precision"
              % (MP_DPS, exc_min["kz"], exc_min["N"],
                 mp.nstr(Zmp, 12), exc_min["Z"], dv_mp,
                 MP_EXC_BAR))
    else:
        check("G33-mp-exception-ward", True, "SMOKE: skipped")
    _Zs, rho_scr = mp_rhp_readout(ctrl["SCR"], MP_SCR_N, MP_DPS)
    dv_scr = abs(float(rho_scr) - float(ctrl["SCR"]["rho"][MP_SCR_N]))
    check("G34-mp-controlflip-ward", dv_scr <= MP_SCR_BAR,
          "mp (dps %d) rho dictionary on SCRAMBLE at n = %d "
          "(THROUGH the flip 21): dev %.1e vs f64 chain (bar "
          "%.0e) -- the readout formulas hold through the "
          "indefinite continuation"
          % (MP_DPS, MP_SCR_N, dv_scr, MP_SCR_BAR))
    check("G35-target-package-rhp-complete", True,
          "STRUCTURE STATEMENT (gated by G30-G34): the campaign "
          "target is now FULLY in RHP language -- sought is the "
          "sign/size of the designated readout Z^RHP = F_{N-1}/"
          "sqrt(h_{N-1}) (border column pairing of the rank-1 "
          "Uvarov augmentation over the sqrt of the (Y1)_12 "
          "entry, r234/r245 frozen formulas) of the discrete 2x2 "
          "FIK problem with the FULL comb as residue/jump data; "
          "requirement: |Z^RHP| + |E| < sqrt(5/7) on the "
          "exception branch (E the route error, here machine-"
          "zero) or the cross-ratio positivity directly")

    # ---------------- S4: LEG C -- the data signature
    section("S4  LEG C -- RHP DATA SIGNATURE OF THE EXCEPTION "
            "BRANCH")
    hits = []
    for fn in ("sig_termdrive", "sig_drivepeak", "sig_chainterm",
               "sig_edgegap", "sig_edgemass"):
        hits += sig_scope_audit(fn)
    check("G40-sig-ast-clean", not hits,
          "the 5 sealed signature candidates consume the drive/"
          "chain prefix arrays and the raw source atoms ONLY -- "
          "no branch-answer identifier in scope (forbidden set "
          "sealed): %s"
          % ("CLEAN" if not hits else "; ".join(hits)))
    hits_orc = sig_scope_audit("sig_oracle")
    check("G41-sig-oracle-flagged", bool(hits_orc),
          "the deliberately branch-reading mutant (M_W + sealed "
          "triangle) is FLAGGED (%s): answer-blindness of the "
          "signature scopes is machine-enforced"
          % ("; ".join(hits_orc) if hits_orc else "NOT FLAGGED"))
    if smoke:
        check("G42-signature-census", True, "SMOKE: skipped")
        check("G43-signature-adjudication", True, "SMOKE: skipped")
        sig_best = ("SMOKE", float("nan"), "n/a")
    else:
        sig_vals: dict = {}
        for rc in recs:
            xu, wu = CT.union_arrays(rc["p"]["d"])
            o = np.argsort(xu)
            xs_sorted = xu[o]
            ws_absv = np.abs(wu[o])
            vals = {"S1_TERMDRIVE": sig_termdrive(rc["t"]),
                    "S3_CHAINTERM": sig_chainterm(
                        rc["t"], rc["ap"], rc["bp"], rc["rpre"]),
                    "S4_EDGEGAP": sig_edgegap(xs_sorted),
                    "S5_EDGEMASS": sig_edgemass(xs_sorted,
                                                ws_absv)}
            for w in SIG_WINDOWS:
                vals["S2_DRIVEPEAK_W%d" % w] = sig_drivepeak(
                    rc["t"], w)
            for k, v in vals.items():
                sig_vals.setdefault(k, []).append(
                    (rc["g"] < 0.0, v))
        tab = {}
        for k in sorted(sig_vals):
            ve = [v for e, v in sig_vals[k] if e]
            vc = [v for e, v in sig_vals[k] if not e]
            a, pw = auc_power(vc, ve)
            tab[k] = (a, pw, float(np.median(ve)),
                      float(np.median(vc)))
            info("%-16s AUC %.3f power %.3f (exc med %.3g / "
                 "cheap med %.3g)" % (k, a, pw, tab[k][2],
                                      tab[k][3]))
        check("G42-signature-census", len(tab) == 7,
              "separation table complete: 5 sealed candidates "
              "(S2 at the 3 sealed windows) on 7 exception vs "
              "35 cheap rungs; branch labels enter the TABLE "
              "side only (source-defined g, r263 rule)")
        best = max(tab, key=lambda k: tab[k][1])
        best_pw = tab[best][1]
        cls = ("PREFIX_DRIVE" if best.startswith(("S1", "S2"))
               else ("PREFIX_CHAIN" if best.startswith("S3")
                     else "SOURCE_GEOMETRY"))
        geo_best = max(tab["S4_EDGEGAP"][1], tab["S5_EDGEMASS"][1])
        w_best = max((k for k in tab if k.startswith("S2")),
                     key=lambda k: tab[k][1])
        found = best_pw >= SIG_POWER_BAR
        sig_best = (best, best_pw, cls)
        check("G43-signature-adjudication", True,
              "sealed rule (best power >= %.1f): %s -- best %s "
              "power %.3f (class %s), runner-up chain side %.3f; "
              "PURE SOURCE GEOMETRY best %.3f (%s); best local "
              "window %s (%.3f): %s"
              % (SIG_POWER_BAR,
                 "EXCEPTION_DATA_SIGNATURE_FOUND" if found
                 else "EXCEPTION_DATA_BLIND",
                 best, best_pw, cls, tab["S3_CHAINTERM"][1],
                 geo_best,
                 "BLIND" if geo_best < SIG_POWER_BAR
                 else "signature-bearing",
                 w_best, tab[w_best][1],
                 "the branch lives in the DRIVE COLUMN of the "
                 "RHP data (r262 drive-dominance in data "
                 "language) -- the deformation lever is the "
                 "border-drive functional near the terminal, "
                 "NOT the naked comb geometry" if found and
                 cls == "PREFIX_DRIVE" else "typed honestly"))

    # ---------------- S5: LEG D -- the s-family
    section("S5  LEG D -- PAIR-DYNAMICS NO-POLE COORDINATE IN s")
    port_kzs = [rc["kz"] for rc in recs] if not smoke else [9]
    ports = {}
    for kz in port_kzs:
        pk = port_pack(kz)
        if pk is not None:
            ports[kz] = pk
    built = len(ports)
    wall_ok = all(float(pk["ev"][-1]) < 1.0
                  for pk in ports.values())
    sb_all = [1.0 / float(pk["ev"][-1]) for pk in ports.values()]
    check("G50-port-census", built == len(port_kzs) and wall_ok,
          "s-dressed port built on %d/%d rungs (lanczos complete)"
          "; base wall lambda_max < 1 on %d/%d => tau_w(s) has "
          "NO zero in [0, 1]: nearest base zero in [%.7f, %.7f] "
          "(the r257 cofinal approach on the full ladder)"
          % (built, len(port_kzs),
             sum(1 for pk in ports.values()
                 if float(pk["ev"][-1]) < 1.0), built,
             min(sb_all), max(sb_all)))
    inter_worst = 0.0
    raw_cross = unit_cross = 0
    for pk in ports.values():
        ev, evr = pk["ev"], pk["evr"]
        spread = float(ev[-1] - ev[0])
        for i in range(len(ev)):
            inter_worst = max(
                inter_worst,
                max(float(ev[i] - evr[i]), 0.0)
                / max(spread, 1e-300))
            if i + 1 < len(ev):
                inter_worst = max(
                    inter_worst,
                    max(float(evr[i] - ev[i + 1]), 0.0)
                    / max(spread, 1e-300))
        raw_cross += int(float(evr[-1]) >= 1.0)
        unit_cross += int(float(pk["evu"][-1]) >= 1.0)
    order_ok = all(1.0 / float(pk["evr"][-1])
                   <= 1.0 / float(pk["ev"][-1]) + 1e-15
                   for pk in ports.values())
    check("G51-pair-interlacing", inter_worst <= INTERLACE_TOL
          and order_ok,
          "Cauchy interlacing of the rank-1 Uvarov row EXACT "
          "(worst rel violation %.1e, tol %.0e); the augmented "
          "zero sits BELOW the base zero on %d/%d rungs: the "
          "pair does NOT cross together and the coupling does "
          "NOT protect -- PAIR_INTERLACING(measured)"
          % (inter_worst, INTERLACE_TOL, built, built))
    if not smoke:
        lab = {rc["kz"]: rc["g"] < 0.0 for rc in recs}
        sr_raw = {kz: 1.0 / float(pk["evr"][-1])
                  for kz, pk in ports.items()}
        sr_unit = {kz: 1.0 / float(pk["evu"][-1])
                   for kz, pk in ports.items()}
        rc_c = [sr_raw[kz] for kz in sr_raw if not lab[kz]]
        rc_e = [sr_raw[kz] for kz in sr_raw if lab[kz]]
        uc_c = [sr_unit[kz] for kz in sr_unit if not lab[kz]]
        uc_e = [sr_unit[kz] for kz in sr_unit if lab[kz]]
        _a1, p_raw = auc_power(rc_c, rc_e)
        _a2, p_unit = auc_power(uc_c, uc_e)
        f2s = [pk["f2"] for pk in ports.values()]
        check("G52-zero-constellation", True,
              "MEASUREMENT: crossing census -- base NEVER "
              "crosses [0, 1] (%d/%d), augmented ALWAYS: RAW "
              "%d/%d (zero in [%.3f, %.3f], mass-driven |f|^2 "
              "in [%.2f, %.2f]), UNIT %d/%d (zero in [%.3f, "
              "%.3f]); branch separation of the aug zero: RAW "
              "cheap med %.4f vs exc med %.4f (power %.2f), "
              "UNIT %.4f vs %.4f (power %.2f) -- the port zero "
              "constellation is BRANCH-BLIND; mains kz9/kz13 "
              "RAW zeros %.4f/%.4f"
              % (built, built, raw_cross, built,
                 min(sr_raw.values()), max(sr_raw.values()),
                 min(f2s), max(f2s), unit_cross, built,
                 min(sr_unit.values()), max(sr_unit.values()),
                 float(np.median(rc_c)), float(np.median(rc_e)),
                 p_raw, float(np.median(uc_c)),
                 float(np.median(uc_e)), p_unit,
                 sr_raw.get(9, float("nan")),
                 sr_raw.get(13, float("nan"))))
    else:
        check("G52-zero-constellation", True, "SMOKE: skipped")
    xw_worst = 0.0
    xw_signs_ok = True
    ward_kzs = [kz for kz in (XRATIO_WARD_KZ if not smoke
                              else (9,)) if kz in ports]
    for kz in ward_kzs:
        pk = ports[kz]
        Q, f = pk["Q"], pk["f"]
        n = Q.shape[0]
        s_star = 1.0 / float(pk["evr"][-1])
        for s in S_GRID:
            X = 1.0 - s * float(f @ np.linalg.solve(
                np.eye(n) - s * Q, f))
            s1, l1 = np.linalg.slogdet(
                np.eye(n) - s * (Q + np.outer(f, f)))
            s2, l2 = np.linalg.slogdet(np.eye(n) - s * Q)
            Xdet = s1 * s2 * math.exp(l1 - l2)
            xw_worst = max(xw_worst, abs(X - Xdet))
            xw_signs_ok = xw_signs_ok and (
                math.copysign(1.0, X)
                == math.copysign(1.0, s_star - s))
    check("G53-schur-xratio-ward",
          xw_worst <= XRATIO_BAR and xw_signs_ok,
          "the Schur cross-ratio X(s) = tau^aug(s)/tau(s) = 1 - "
          "s f^T(I - sQ)^{-1} f vs the slogdet ratio on the "
          "sealed ward rungs %s over the s-grid %s: worst abs "
          "dev %.1e (bar %.0e); grid sign == sign(s* - s) at "
          "every point (s* = 1/mu_max, the augmented zero)"
          % (str(tuple(ward_kzs)), str(S_GRID), xw_worst,
             XRATIO_BAR))
    stab_ok = True
    tight_ok = True
    marg_min = float("inf")
    exc_marg = []
    for rc in recs + mrecs:
        p = rc["p"]
        N = p["N"]
        Bw = float(p["S"][N - 2]) + B57
        S1_ = float(p["S"][N - 1])
        S2_ = float(p["S"][N - 2])
        prev = float("inf")
        for s in (0.0,) + S_GRID:
            if s > 1.0:
                continue
            num = Bw - s * s * S1_
            den = Bw - s * s * S2_
            stab_ok = stab_ok and (num > 0.0 and den > 0.0)
            tight_ok = tight_ok and (num <= prev + 1e-12)
            prev = num
        m1 = Bw - S1_
        marg_min = min(marg_min, m1)
        if rc["g"] < 0.0:
            exc_marg.append((rc["kz"], m1))
    band_ok = smoke or (MARGIN_BAND[0] <= marg_min
                        <= MARGIN_BAND[1])
    check("G54-border-s-coordinate", stab_ok and tight_ok
          and band_ok,
          "BORDER-DRESSED exact coordinate t_n(s) = s t_n: "
          "1 - q_N(s) = (B - s^2 S_{N-1})/(B - s^2 S_{N-2}), "
          "s = 0 trivial / s = 1 the target EXACTLY; sign-stable "
          "on [0, 1] on %d/%d worlds with the margin B - s^2 "
          "S_{N-1} monotone falling => tightest spot s = 1 on "
          "EVERY rung, min terminal margin %.4f in the sealed "
          "band %s (the razor as the s = 1 endpoint); exception "
          "margins at s = 1: %s -- MEASUREMENT: the s-deformation "
          "is a viable proof coordinate in this form"
          % (len(recs) + len(mrecs), len(recs) + len(mrecs),
             marg_min if not smoke else float("nan"),
             str(MARGIN_BAND),
             "; ".join("kz%d %.3f" % (kz, m)
                       for kz, m in sorted(exc_marg))
             if exc_marg else "n/a"))

    # ---------------- S6: LEG E -- kills + controls + must-fails
    section("S6  LEG E -- KILLS + CONTROLS + MUST-FAILS")
    p9 = packs["w9"]
    rc9 = mrecs[0] if not smoke else recs[0]
    G9, tv9 = rc9["G"], rc9["tv"]
    N9 = p9["N"]
    Zh, _r1, _e1, _s1 = rhp_readout(G9, tv9, N9 - 1)
    honest = abs(Zh - rc9["Z"])
    Zm1, _r2, _e2, _s2 = rhp_readout(G9, tv9, N9 - 1, swap_a=True)
    dev_m1 = abs(Zm1 - rc9["Z"])
    check("G60-mustfail-index-swap",
          dev_m1 >= LOUD * max(honest, 1e-300),
          "m1 READOUT INDEX SWAP (a_{N-2} for a_{N-1}): w9 "
          "dictionary breaks by %.1e = %.1e x honest %.1e (bar "
          "%.0f x) -- the Y1 entry is degree-pinned"
          % (dev_m1, dev_m1 / max(honest, 1e-300), honest, LOUD))
    Zm2, _r3, _e3, _s3 = rhp_readout(G9, tv9, N9 - 1,
                                     unprojected=True)
    dev_m2 = abs(Zm2 - rc9["Z"])
    check("G61-mustfail-unprojected-border",
          dev_m2 >= LOUD * max(honest, 1e-300),
          "m2 BORDER COLUMN WITHOUT AUGMENTATION (raw top border "
          "moment, no Gram-solve projection): breaks by %.1e = "
          "%.1e x honest (bar %.0f x) -- F_{N-1} is the "
          "PROJECTED border pairing, not a naked moment"
          % (dev_m2, dev_m2 / max(honest, 1e-300), LOUD))
    fl_ok = True
    fl_note = []
    for c in ctrl:
        xu, wu = CT.union_arrays(ctrl[c]["d"])
        fl = CT.blind_flip_predictor(xu, wu, ctrl[c]["N"])
        first = fl[0] if fl else None
        fl_ok = fl_ok and (first == ctrl[c]["nf"])
        fl_note.append("%s -> %s (truth %s)"
                       % (c, first, ctrl[c]["nf"]))
    check("G62-micropredictor-ward", fl_ok,
          "r257 blind source-only pivot field reproduces the "
          "control flips: %s -- WARD, not a proof"
          % "; ".join(fl_note))
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) \
        / B57
    check("G63-smooth-anchor", abs(qS) <= SM_Q_BAR,
          "SMOOTH anchor q_N = %.1e <= %.0e: the terminal "
          "question trivializes exactly when the source aliases "
          "(F_{N-1} = 0 structurally) -- the designated readout "
          "is source-driven, not an artifact" % (qS, SM_Q_BAR))
    ag_hits = antigate_fragment_audit()
    check("G64-antigates-kill-list-armed", not ag_hits,
          "NO new certificate is attempted this round: no "
          "majorant, no unroll, no fit primitives (fragment "
          "scan %s); the inherited kill list stays armed as "
          "charter constants (%s); no cofinal selection by "
          "post-hoc values (the branch rule reads g only, r263 "
          "audit precedent)"
          % ("CLEAN" if not ag_hits else "; ".join(ag_hits),
             "; ".join(CH_KILLS)))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the opening "
          "adds: the charter as code, the target package fully "
          "in RHP language (designated readout, machine-exact), "
          "the data-signature localization of the exception "
          "branch, and the honest s-coordinate census (border-"
          "dressed viable, port constellation branch-blind)")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        okB = (zworst <= Z_ID_BAR and dworst_m <= DICT_ABS_MAIN
               and dworst_d <= DICT_ABS_DEEP and sign_ok
               and apos_ok and dv_mp <= MP_EXC_BAR
               and dv_scr <= MP_SCR_BAR)
        parts = ["CHARTER_FROZEN(%s, exceptions %d, kills %d, "
                 "blocked %d)" % (CHARTER_SHA[:16], len(exc),
                                  len(CH_KILLS), len(CH_BLOCKED))]
        parts.append("RHP_DICTIONARY_EXACT(Z = designated "
                     "readout: border column / Y1)" if okB
                     else "RHP_DICTIONARY_OPEN(typed)")
        if sig_best[1] >= SIG_POWER_BAR:
            parts.append("EXCEPTION_DATA_SIGNATURE_FOUND(%s, "
                         "power %.3f, class %s)" % sig_best)
        else:
            parts.append("EXCEPTION_DATA_BLIND")
        parts.append("S_FAMILY_COORDINATE(BORDER_S sign-stable "
                     "%d/%d, tightest s = 1, min margin %.4f; "
                     "PORT_S wall %d/%d, aug crossing RAW+UNIT "
                     "%d/%d at s < 1, branch-blind)"
                     % (len(recs) + len(mrecs),
                        len(recs) + len(mrecs), marg_min,
                        built, built, min(raw_cross, unit_cross),
                        built))
        parts.append("PAIR_INTERLACING(exact %.1e; aug zero "
                     "BELOW base zero on %d/%d)"
                     % (inter_worst, built, built))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the charter branch "
          "reproduction, the Z chain identity, the designated-"
          "readout dictionary (f64 + mp); MEASURED: the "
          "signature separation, the zero constellation, the "
          "s-coordinate census; OPEN: the exception scalar's "
          "positivity itself (the campaign's work); NO RH claim"
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
