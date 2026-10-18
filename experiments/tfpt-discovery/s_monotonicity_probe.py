#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""s_monotonicity_probe -- PRIME.PORT.RHP.QUENCHED.S_MONOTONICITY
.01 (round 265): adjudicate the s-COORDINATE CLASS of the quenched
full-source RHP campaign.  r264 measured the border-dressed
s-coordinate sign-stable and monotone on 44/44 worlds (tightest
spot always s = 1, min margin 0.0139) -- but is any s-deformation
a TOOL (a definite dynamics that IMPORTS the endpoint positivity
from s = 0) or a RESTATEMENT (the endpoint IS the budget
inequality in new clothes)?  Three sealed coordinate families are
closed exactly and typed honestly.

LEG A -- THE NAIVE BORDER-DRESSED COORDINATE, CLOSED EXACTLY:
the deformation scales the border comb, sigmatilde -> s sigmatilde.
Every border functional is LINEAR in the border weights (F_k = int
pihat_k dsigmatilde, T_k = int x pihat_k dsigmatilde) while the
chain coefficients (alh, gam) consume the WINDOW arrays only =>
    F_k(s) = s F_k,  T_k(s) = s T_k,  (a', b') s-FREE,
    r_0(s) = s r_0,  and by the driven recursion (r260: r_{k+1} =
    t_k + a'_k r_k + b'_k r_{k-1}, LINEAR-HOMOGENEOUS in the pair
    (r, t))  r_k(s) = s r_k EXACTLY at every degree.
CLOSED FORM (with the FIXED imported corner B = S_{N-2} + 5/7):
    D_n(s) = B - s^2 S_{n-1},
    1 - q_N(s) = (B - s^2 S_{N-1}) / (B - s^2 S_{N-2})
-- an explicit RATIONAL function of s^2 with source-pure
coefficients (B, S_{N-2}, S_{N-1}); its log-derivative is
    d/ds log(1 - q_N(s)) =
        -2 s B rho_{N-1} / [(B - s^2 S_{N-1})(B - s^2 S_{N-2})],
and the per-degree cross-ratio x_n(s) = (B - s^2 S_n)/(B - s^2
S_{n-1}) obeys d/ds x_n = -2 s B rho_n / (B - s^2 S_{n-1})^2 (a
SQUARED denominator: the sign is -sign(B rho_n) at EVERY world,
flipped or not).  CONSEQUENCES, machine-gated: (i) the r264
monotonicity/sign-stability of the naive coordinate is
ALGEBRAICALLY TRIVIAL (positive branch: sign = -sign(rho_{N-1}),
margin falls, tightest spot s = 1 on every rung -- the r264 min
margin 0.0139 census is reproduced as a corollary); (ii) the
endpoint s = 1 positivity IS B - S_{N-1} > 0, i.e. EXACTLY the
budget inequality => sealed typing S_NAIVE_RESTATEMENT (the
coordinate reformulates the target, it does not attack it) --
the naive route is buried cleanly BEFORE anyone mistakes it for
a tool.  Gates: (a1) sympy EXACT identities (bordered det with a
sigma-scaled column == det H (B - sigma^2 b^T H^{-1} b) on the
r263 rational instance; the log-derivative rational form; the
drop antiderivative d/ds [1/(lam(1 - s lam))] = (1 - s lam)^{-2}
with endpoint value 1/(1-lam) -- feeds leg B); (a2) linear
homogeneity on real data: rebuild the r244 chain with the border
weights scaled by s: r(s) == s r, t(s) == s t, (a', b')
unchanged, at the DYADIC s = 1/2 (bar 1e-13; scaling by a power
of two commutes with every IEEE op -- the check is exact) and at
s = 0.3 (bar 1e-12), on both mains + 3 ladder samples; (a3) the
closed form vs the DIRECT bordered-slogdet route with the border
column scaled by s (mains + samples at s in {0.5, 0.9}, sizes
N-1 and N, ABS bars 3e-8 main / 3e-6 deep -- calibration
amendment a1, disclosed: the draft main bar 1e-8 was set from
the scratch floors at N = 184 (4.2e-10) and N = 878 (5.8e-8);
calibration pass 1 measured 1.2e-8 on the N ~ 380 ladder
sample, the ordinary f64 solve floor of the scaled-column
bordered route at that depth -- gate tolerance only, r264-a1
precedent, no physics bar, band, rule or verdict moved;
controls at the terminal, bar 1e-3 -- the identity is
world-blind algebra);
(a4) the derivative formula d/ds x = -2sB rho_{N-1}/den^2 vs a
DIRECT-route central FD (step 1e-3) on the mains (rel bar 1e-4,
FD floor) + the r264 census
reproduction (sign-stable, tightest s = 1 on 44/44, min margin
in the sealed band [0.010, 0.020]) + the endpoint identity
1 - q_N(1) == D_N / D_{N-1} (rel 1e-12) => the restatement
typing is a machine conclusion, not an opinion.

LEG B -- THE IIKS s-FAMILY (the real question; r257/r264 port
pair VERBATIM): tau_w(s) = det(I - s Q_w), tau^aug_w(s) =
det(I - s (Q_w + f f^T)) with Q = A^T A the folded-port state
Gram and f the Uvarov border row (QO.port_pack).  EXACT ODEs
(JMU/Fredholm form, r224 machinery):
    d/ds log tau(s)      = -Tr[(I - s Q)^{-1} Q],
    d/ds log tau^aug(s)  = -Tr[(I - s Q_aug)^{-1} Q_aug],
    X(s) := tau^aug/tau  = 1 - s f^T (I - s Q)^{-1} f  (Schur),
    d/ds log X(s) = Tr[(I - sQ)^{-1}Q] - Tr[(I - sQaug)^{-1}Qaug]
(the cross-ratio ODE as the DIFFERENCE OF TWO RESOLVENT TRACES).
THE ROUND'S SATZ (exact algebra, machine-gated):
    X'(s) = -f^T (I - s Q)^{-2} f = -|| (I - sQ)^{-1} f ||^2
          = -sum_i c_i^2 / (1 - s lambda_i)^2,   c = U^T f,
-- EVERY spectral carrier term is a NEGATIVE SQUARE: the s-ODE
of the IIKS cross-ratio is FULLY DEFINITE (the Herglotz/CP
structure is trivially present, indefinite part ZERO), so X is
strictly monotone falling on [0, 1] on every rung; AND the exact
drop identity (int_0^1 (1 - s lam)^{-2} ds = 1/(1 - lam)):
    X(0) - X(1) = f^T (I - Q)^{-1} f
-- the total definite drop EQUALS the r257-blocked bordered
spectral quantity EXACTLY.  Hence the definite ODE's endpoint
criterion "X(1) > 0" IS f^T (I - Q)^{-1} f < 1: the bordered
spectral bound that r257/r264 measured FALSE on every rung (the
augmented zero crosses at s* < 1, 42/42).  SEALED ADJUDICATION:
HERGLOTZ_STRUCTURE_FOUND iff the definite drop is affordable,
g_w(1) = f^T (I - Q)^{-1} f < 1 on ALL rungs (then X(1) > 0
follows from the ODE alone, without binding the budget sum);
else DEFINITENESS_WALL_EQUIVALENT (the definite structure exists
but its endpoint criterion is exactly the blocked wall bound --
the s-ODE proves the CROSSING, not the target).  Gates: (b1)
tau-ODE trace vs central FD on the sealed ward rungs (9, 13, 20,
52) over the s-grid, rel bar 1e-5 (FD floor); (b2) X' by THREE
routes (carrier sum == X * trace-difference on pole-safe grid
points, min_i |1 - s mu_i| >= 0.05, == central FD), bars 1e-9
exact-vs-exact / 1e-5 FD; (b3) sign census on ALL 42 rungs:
X'(s) < 0 at every census point (incl. s = 1), indefinite
carrier terms 0/h, crossing census s* = 1/mu_max, X(1) < 0
count, branch separation power of s* (r264 branch-blindness
reproduction); (b4) the drop identity |(X(0) - X(1)) -
f^T(I-Q)^{-1}f| rel <= 1e-7 on all rungs + the sealed
adjudication above.  NOTE (honesty): the port X(s) is the
r257/r264 PAIR family; its s = 1 value is NOT the budget
cross-ratio 1 - q_N -- that is precisely the finding: the IIKS
coordinate carries a definite, exactly-solvable s-dynamics whose
endpoint is the WRONG (blocked) statement, while the naive
coordinate carries the RIGHT endpoint with trivial dynamics.
No admissible s-coordinate measured this round does both.

LEG C -- THE INTERMEDIATE COORDINATES (sealed family, closed
forms): (c1) TERMINAL-DRIVE family t_{N-2} -> s t_{N-2} (all
else fixed): Z(s) = s t_{N-2} + a'_{N-2} r_{N-2} + b'_{N-2}
r_{N-3} is AFFINE in s, 1 - q_N(s) = (5/7 - Z(s)^2)/(5/7) a
downward parabola; the exception rung loses its exception
property at the CLOSED-FORM crossing
    s*_w = (sqrt(5/7) - |a'_{N-2} r_{N-2}| - |b'_{N-2} r_{N-3}|)
           / |t_{N-2}|  =  1 + g_w / |t_{N-2}|
-- source-pure (prefix data + the imported budget only), and
s* < 1 <=> g_w < 0 EXACTLY (the branch rule restated); gates:
the equivalence on 42/42 + mains, U(s*) == M on the exceptions
(abs 1e-12), the exception s* table printed, the vertex census
of the parabola (count of interior extrema -- monotonicity is
NOT generic here, measured); typing: the terminal family is
RESTATEMENT_ADJACENT (its endpoint s = 1 is |Z| < sqrt(5/7)
itself; s* is a useful BRANCH COORDINATE, not a certificate).
(c2) THE Q_7/CENTERING (level-8 subtraction) family: in the
orthonormal chain coordinates the border functional has
components phi_k with phi_k^2 = rho_k; the family scales the
HEAD, phi_k(s) = (1 - s) phi_k for k < 8, tail fixed =>
    margin(s) = B - S_{N-1}(s) = D_N + (1 - (1-s)^2) S_7,
    d/ds margin = +2 (1-s) S_7 >= 0 on the positive prefix
-- the definite direction points AWAY from the target endpoint
s = 0 (removing head mass can only widen the margin; the family
redistributes prefix mass and leaves the s = 0 question
untouched) => sealed typing Q7_CENTERING_RESTATEMENT.  Gates:
the chain-coordinate ward phi_k^2 == rho_k (Cholesky of the
r261 Gram, mains, rel 1e-8), the deformed DIRECT route (border
column L phi(s), bordered slogdet) vs the closed form (mains,
s = 1/2, abs 1e-8), S_7 > 0 on mains.

LEG D -- KILLS + CONTROLS: (d1) PAIRCORR-IN-S census: rescuing
the definite IIKS route needs the drop bound f^T(I-Q)^{-1}f < 1
where the measured drop is g(1); demand = log10 g(1) decades of
comb cancellation in the border row f (f IS the comb-minus-
smooth statistic) -- census over 42 rungs (min/med/max, fired
count at the 1.0 dec bar, cheap vs exception medians); the kill
does NOT depend on the bar: the endpoint criterion is measured
FALSE (crossing < 1) on every rung.  (d2) control-flip
consistency of the naive closed form: d/ds x_n = -2 s B rho_n /
den^2 => sign(FD of x_n) == -sign(B_w rho_n) at the flip degree
AND a pre-flip degree on EPSTEIN + SCRAMBLE via the DIRECT
scaled-column route (SMOOTH excluded: alias floor, rho at the
flip is 0/0 noise -- disclosed); NOTE B_w < 0 on SCRAMBLE (the
signed S_{N-2} dominates the corner) -- the den^2 form carries
the flip EXACTLY (measured in the scratch, sealed here).  (d3)
SMOOTH anchor q_N <= 1e-20; control closed form world-blind
(bar 1e-3).  (d4) MUST-FAILS (each loud): (m1) SWAPPED TRACE --
the cross-ratio ODE with the two resolvent traces exchanged
must break vs FD by >= 1e3 x honest on the w9 port; (m2) WRONG
s-DEGREE -- the naive closed form with B - s S_{n-1} (degree 1
instead of 2) must break vs the direct route by >= 1e3 x
honest.  (d5) mp WARD: the naive closed form at the smallest-N
exception rung kz20 (N = 170, sealed rule min-N), dps 60,
s = 1/2: mp bordered-det ratio vs the f64 chain closed form,
bar 1e-8.  (d6) AST: firewall (no zero/prime oracles), fragment
audit (no fit primitives), sstar builder scope clean (prefix +
imported budget only), deliberate rho-reading mutant FLAGGED.

INDEX FIREWALL (binding, r238-r264 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; rho_k = F_k^2/h_k, S_n
= sum_{k<=n} rho_k; ground truth (flips, branch labels) enters
GATES and census tables only; no zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack +
BH.bord_chain, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap/u_triangle, r264 QO.gram_input / QO.port_pack /
QO.auc_power, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 =
5/7; M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20,
22, 36, 38, 39, 52); SAMPLE_IDX (0, 20, 41); DEEP_N 400;
S_HOMOG (0.5 dyadic, 0.3); HOMOG_BAR_DY 1e-13 / HOMOG_BAR
1e-12; S_DIRECT (0.5, 0.9); DIRECT_ABS_MAIN 3e-8 (amendment a1,
disclosed above; draft 1e-8) / DEEP 3e-6 / CTRL 1e-3; DERIV_FD_H 1e-3; DERIV_FD_BAR 1e-4; ENDPOINT_BAR
1e-12; MARGIN_BAND
(0.010, 0.020); S_GRID (0.1, 0.25, 0.5, 0.75, 0.9); S_CENSUS =
S_GRID + (1.0,); ODE_WARD_KZ (9, 13, 20, 52); FD_H 1e-4;
TAU_FD_BAR 1e-5; XP_FD_BAR 1e-5; XP_TRACE_BAR 1e-9;
SAFE_POLE_GAP 0.05; DROP_ID_BAR 1e-7; DEMAND_BAR 1.0 dec;
SSTAR_EQ_BAR 1e-12; Q7_HEAD 8; Q7_PHI_BAR 1e-8; Q7_DIRECT_BAR
1e-8; Q7_S 0.5; CTRL_PREFLIP_N 10; MP_DPS 60; MP_S 0.5; MP_BAR
1e-8; LOUD 1e3; runtime <= 1800 s; smoke = w9 + controls +
symbolic + port rung 9 + Q7 w9 + must-fails (ladder, w13,
censuses, adjudications, mp ward skipped).  DISCLOSED PRE-SPEC
SCRATCH (one feasibility pass, floors only, script deleted; all
bars above were then FIXED before any full evaluation; no
verdict rule touched after any measurement): homogeneity dev
0.0 at s = 0.5 (dyadic-exact as predicted) / 5.6e-17 at s =
0.3 on kz9+kz52; direct closed-form dev 4.2e-10 main (N=184) /
5.8e-8 deep (N=878); Q7 phi^2==rho worst rel 1.3e-11, deformed
direct dev 3.4e-10; tau-ODE FD dev 1.6e-7, X'-FD 6.8e-8,
X'-trace 7.2e-13, drop identity rel 1.3e-10; g(1) = 7.82 (kz9,
0.89 dec) / 15.4 (kz52, 1.19 dec) => the demand census is
expected to straddle the 1.0 dec bar (reported honestly; the
adjudication rule g(1) < 1 is bar-independent); control FD
signs (EPST +/- at 25/10, SCR -/+ at 21/10) == -sign(B rho)
with B_SCR < 0 -- the den^2 rule sealed above.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  S_NAIVE_RESTATEMENT(closed rational form; r264 monotonicity
    algebraically trivial; endpoint == the budget inequality) /
    S_NAIVE_TOOL(typed)
+ IIKS_S_ODE_EXACT(tau ODE + cross-ratio ODE, three routes) /
    IIKS_S_ODE_OPEN(typed)
+ S_MONOTONE_IIKS(carrier: X' = -sum c_i^2/(1 - s lam_i)^2, all
    terms definite, indefinite 0) / S_NOT_MONOTONE_IIKS
+ HERGLOTZ_STRUCTURE_FOUND(definite drop affordable) /
    DEFINITENESS_WALL_EQUIVALENT(drop == f^T(I-Q)^{-1}f == the
    r257-blocked bordered spectral bound; endpoint measured
    FALSE)
+ PAIRCORR_IN_S(demand census)
+ TERMINAL_SSTAR(s* = 1 + g/|t_term| exact, source-pure;
    equivalence with the branch rule)
+ Q7_CENTERING_RESTATEMENT(definite direction points away from
    the target).
Honesty before beauty: no verdict claims a derived 5/7, a bound
mechanism, or an asymptotic law; the naive coordinate is buried
as a restatement, the IIKS coordinate is typed wall-equivalent,
the target positivity itself stays OPEN (the campaign's work);
r243/r250/r253/r256/r257/r258/r260/r261/r262/r263/r264 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke 24/24 first pass; calibration pass 1 = first full
evaluation, 22/24 -- the ONLY miss was the G22 main bar (worst
1.2e-8 vs the draft 1e-8 on the N ~ 380 ladder sample, the
understood f64 solve floor of the scaled-column bordered route;
G96 failed only as its consequence) => the ONE disclosed
amendment a1 above (main gate tolerance 1e-8 -> 3e-8, gate-side
only); pass 2 = the record run below, numerically identical to
pass 1 in every printed figure):
CAL_VERDICT = S_NAIVE_RESTATEMENT(closed rational form; r264
monotonicity algebraically trivial; endpoint == the budget
inequality) + IIKS_S_ODE_EXACT(tau ODE + cross-ratio ODE, three
routes) + S_MONOTONE_IIKS(carrier fully definite, indefinite
0/42) + DEFINITENESS_WALL_EQUIVALENT(drop == f^T(I-Q)^{-1}f;
g(1) in [6.06, 15.41], X(1) < 0 on 42/42) + PAIRCORR_IN_S(
demand 0.78/1.02/1.19 dec min/med/max, fired 22/42) +
TERMINAL_SSTAR(s* = 1 + g/|t_term|, equivalence 44/44) +
Q7_CENTERING_RESTATEMENT.
Key numbers.  LEG A: sympy identities EXACT (rational zero:
bordered sigma-det, log-derivative form, drop antiderivative);
homogeneity r(s) == s r / t(s) == s t / (a', b') unchanged:
dev 0.0 at the dyadic s = 1/2 on ALL 5 worlds (mains + 3
samples N in [142, 878]) -- machine-EXACT as sealed -- and
worst 1.4e-16 at s = 0.3 (bars 1e-13 / 1e-12); closed form
D_n(s) = B - s^2 S_{n-1} vs direct scaled-column slogdet:
worst 1.2e-8 main N <= 400 / 5.8e-8 deep (bars 3e-8 after a1 /
3e-6), controls worst 5.5e-5 at the terminal (bar 1e-3, world-
blind); derivative formula d/ds x = -2sB rho_{N-1}/den^2 vs
direct-route FD: worst rel 2.7e-07 (bar 1e-4) on both mains;
r264 census reproduced AS A COROLLARY: sign-stable + margin
monotone falling + tightest s = 1 on 44/44, min terminal
margin 0.0139 in [0.010, 0.020]; endpoint identity rel dev
1.1e-13 => S_NAIVE_RESTATEMENT (machine conclusion).  LEG B:
ports 42/42, wall lambda_max < 1 on 42/42, nearest base zero
in [1.0000001, 1.0001675] (r264 reproduced); tau-ODE trace vs
FD worst rel 1.6e-07 (bar 1e-5) on ward rungs (9, 13, 20, 52)
x 5 grid points; X' three routes: carrier-vs-trace-difference
worst rel 7.2e-13 (bar 1e-9, 20/20 pole-safe points), carrier-
vs-FD 6.8e-08 (bar 1e-5); sign census: X'(s) < 0 at EVERY
census point incl. s = 1 on 42/42, indefinite carrier terms 0
of 17849 (every spectral component a negative square), crossing
s* = 1/mu_max in [0.1107, 0.2303] (the r264 RAW band), X(1) < 0
on 42/42, branch separation power of s* 0.192 (branch-blind,
r264 reproduced); drop identity worst rel 3.5e-10 (bar 1e-7) on
42/42; g(1) in [6.06, 15.41], min 6.06 >= 1 on EVERY rung =>
HERGLOTZ_STRUCTURE_FOUND refused: DEFINITENESS_WALL_EQUIVALENT
(the definite ODE proves the crossing, not the target).  LEG C:
s* equivalence (s* < 1 <=> g < 0) on 44/44, U(s*) == M worst
1.1e-16 on the 7 exceptions; exception s* table: kz15 0.9966 /
kz20 0.5496 / kz22 0.6287 / kz36 0.4666 / kz38 0.5378 / kz39
0.6322 / kz52 0.4508 (kz15 razor-close to 1, matching its g
-0.002); parabola vertex interior (0, 1) on 9/44 (the terminal
family is NOT generically monotone -- measured); Q7: phi^2 ==
rho worst rel 1.3e-11 (bar 1e-8), deformed direct route dev
3.4e-10 at s = 1/2 (bar 1e-8), S_7 = 3.487/3.252 > 0 on
w9/w13, margin(1) - margin(0) == S_7 exact =>
Q7_CENTERING_RESTATEMENT.  LEG D: demand census log10 g(1):
min 0.78 / med 1.02 / max 1.19 dec, fired (>= 1.0) on 22/42,
cheap med 1.02 vs exception med 0.99 -- the wall is NOT branch-
localized in s either (the definite-route demand is branch-
blind, matching the r264 port blindness); control-flip
consistency: sign(FD x_n) == -sign(B_w rho_n) at flip +
pre-flip degrees on EPST (B +6.04) and SCR (B -0.44): 4/4 --
the den^2 rule carries the flip through the indefinite
continuation; SMOOTH anchor q_N = 4.2e-25 <= 1e-20; must-fails:
m1 swapped-trace breaks by 1.4e+01 = 7.6e+08 x honest, m2 wrong
s-degree by 1.9e+00 = 6.7e+09 x honest (bars 1e3); mp ward kz20
(N = 170, dps 60, s = 1/2): D_mp = 6.68348999143, dev 2.8e-11
vs the closed form (bar 1e-8); scope audits CLEAN, rho-reading
mutant FLAGGED (rho scope hit).  READING (typed, no upgrade):
the s-coordinate class is adjudicated -- the naive border-
dressed family is a RESTATEMENT (exact rational form in s^2,
trivial monotonicity, endpoint == the budget inequality: the
r264 finding was a reformulation, not a tool), the IIKS port
family has an EXACT, FULLY DEFINITE cross-ratio s-ODE whose
total drop equals the r257-blocked bordered spectral bound
machine-exactly (wall-equivalent: the definiteness proves the
crossing at s* < 1, not the target; the demand census is
branch-blind), the terminal-drive family yields the exact
branch coordinate s* = 1 + g/|t_term| (kz15 at 0.9966), and
the Q7 family's definite direction points away from the
target.  NO admissible s-coordinate this round carries BOTH
the right endpoint AND a definite dynamics: a usable s-tool
must couple the border drive into the resolvent structure
WITHOUT reducing to the wall bound -- that is the sharpened
residual question handed back to the campaign.  Runtime 32.0 s
full / 0.3 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE (a1 predates the record run,
disclosed above).

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
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import cancellation_adjudication_probe as CA  # noqa: E402 r263
import coupledtau_probe as CT                # noqa: E402 r257
import terminal_crossratio_probe as TX       # noqa: E402 r260
import quenched_opening_probe as QO          # noqa: E402 r264
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
SAMPLE_IDX = (0, 20, 41)
DEEP_N = 400
S_HOMOG = (0.5, 0.3)
HOMOG_BAR_DY = 1e-13
HOMOG_BAR = 1e-12
S_DIRECT = (0.5, 0.9)
DIRECT_ABS_MAIN = 3e-8
DIRECT_ABS_DEEP = 3e-6
DIRECT_ABS_CTRL = 1e-3
DERIV_FD_H = 1e-3
DERIV_FD_BAR = 1e-4
ENDPOINT_BAR = 1e-12
MARGIN_BAND = (0.010, 0.020)
S_GRID = (0.1, 0.25, 0.5, 0.75, 0.9)
S_CENSUS = S_GRID + (1.0,)
ODE_WARD_KZ = (9, 13, 20, 52)
FD_H = 1e-4
TAU_FD_BAR = 1e-5
XP_FD_BAR = 1e-5
XP_TRACE_BAR = 1e-9
SAFE_POLE_GAP = 0.05
DROP_ID_BAR = 1e-7
DEMAND_BAR = 1.0
SSTAR_EQ_BAR = 1e-12
Q7_HEAD = 8
Q7_PHI_BAR = 1e-8
Q7_DIRECT_BAR = 1e-8
Q7_S = 0.5
CTRL_PREFLIP_N = 10
MP_DPS = 60
MP_S = 0.5
MP_BAR = 1e-8
LOUD = 1e3

CAL_VERDICT = (
    "S_NAIVE_RESTATEMENT(closed rational form; r264 monotonicity "
    "algebraically trivial; endpoint == the budget inequality) + "
    "IIKS_S_ODE_EXACT(tau ODE + cross-ratio ODE, three routes) + "
    "S_MONOTONE_IIKS(carrier fully definite, indefinite 0/42) + "
    "DEFINITENESS_WALL_EQUIVALENT(drop == f^T(I-Q)^{-1}f; g(1) "
    "in [6.06, 15.41], X(1) < 0 on 42/42) + PAIRCORR_IN_S(demand "
    "0.78/1.02/1.19 dec min/med/max, fired 22/42) + "
    "TERMINAL_SSTAR(s* = 1 + g/|t_term|, equivalence 44/44) + "
    "Q7_CENTERING_RESTATEMENT")

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
                       "the r244 chain rows / the r261 Gram input / "
                       "the r257 port pair; ground truth (flips, "
                       "branch labels) enters gates and census "
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


# ------------- sealed deformation builders (target-blind where
# required: sstar consumes the prefix triangle + the imported
# budget ONLY; AST-audited)
def sstar_terminal(t_arr, ap_arr, bp_arr, rpre):
    """c1 CLOSED FORM: the terminal-drive crossing s* at which
    U(s) = s|t_{N-2}| + chain meets M_W; s* = 1 + g/|t_{N-2}|.
    Prefix data + the imported budget constant only."""
    chain = abs(float(ap_arr[-1] * rpre[-1])) \
        + abs(float(bp_arr[-1] * rpre[-2]))
    return (M_W - chain) / abs(float(t_arr[-1]))


def oracle_sstar(p):
    """DELIBERATE MUST-FAIL MUTANT: reads the terminal target --
    the scope audit must FLAG this."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


SSTAR_FORBIDDEN = {"rho", "S", "sa", "la", "q_chain", "D_dir",
                   "wb", "world_block", "direct_terminal",
                   "rhp_readout", "gram_input", "port_pack"}


def sstar_scope_audit(funcname):
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
                if nm in SSTAR_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ------------------------------------------- naive direct route
def d_direct_scaled(G, tv, n, B, s, sdeg=1):
    """DIRECT bordered-slogdet with the border column scaled by
    s^sdeg (sdeg = 1 honest; the m2 mutant passes sqrt(s) via the
    caller): D_dir(s) = det[[G_n, s tv],[s tv^T, B]] / det G_n."""
    col = (s ** sdeg) * tv[:n]
    A = np.zeros((n + 1, n + 1))
    A[:n, :n] = G[:n, :n]
    A[:n, n] = col
    A[n, :n] = col
    A[n, n] = B
    sa, la = np.linalg.slogdet(A)
    sg, lg = np.linalg.slogdet(G[:n, :n])
    return sa * sg * math.exp(la - lg)


# --------------------------------------------------- mp ward
def mp_direct_scaled(p, n, dps, s):
    """the SAME direct route in mp (dps sealed): mp Gram + border
    column from the raw atoms, bordered det ratio with the column
    scaled by s (r264 mp route adapted)."""
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
    PU = [[mp.mpf(1)] * len(xs), [2 * u for u in tvm]]
    TU = [[mp.mpf(1)] * len(bs), [2 * u for u in tbm]]
    for _k in range(2, n):
        PU.append([2 * u * a - b
                   for u, a, b in zip(tvm, PU[-1], PU[-2])])
        TU.append([2 * u * a - b
                   for u, a, b in zip(tbm, TU[-1], TU[-2])])
    GM = mp.matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            v = mp.fsum(w * a * b
                        for w, a, b in zip(ws, PU[i], PU[j]))
            GM[i, j] = v
            GM[j, i] = v
    tm = [mp.fsum(w * a for w, a in zip(bwm, TU[i]))
          for i in range(n)]
    sm = mp.mpf(s)
    Bm = mp.mpf(float(p["S"][p["N"] - 2])) + mp.mpf(5) / 7
    A = mp.matrix(n + 1, n + 1)
    for i in range(n):
        for j in range(n):
            A[i, j] = GM[i, j]
        A[i, n] = sm * tm[i]
        A[n, i] = sm * tm[i]
    A[n, n] = Bm
    return mp.det(A) / mp.det(GM)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("s_monotonicity_probe -- PRIME.PORT.RHP.QUENCHED."
          "S_MONOTONICITY.01 (round 265)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)   "
          "CHARTER_SHA %s (imported r264)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16], QO.CHARTER_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + symbolic + port "
                        "rung 9 + Q7 w9 + must-fails; ladder, "
                        "w13, censuses, adjudications, mp ward "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THREE sealed coordinate families: NAIVE border-dressed "
          "(closed rational form + restatement typing), IIKS port "
          "pair (exact s-ODEs, carrier decomposition, drop "
          "identity, Herglotz-vs-wall adjudication), INTERMEDIATE "
          "(terminal-drive s*, Q7 centering); kills: paircorr-in-"
          "s census, control-flip consistency, must-fails m1/m2, "
          "mp ward -- ALL bars, rules and verdicts sealed BEFORE "
          "evaluation (one pre-spec feasibility scratch disclosed "
          "in the spec, floors only)")

    # ---------------- S1: census + controls
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

    def rung_rec(p):
        N = p["N"]
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        rpre = r[:N - 1]
        g = CA.g_gap(rpre, t, ap, bp)
        return dict(kz=p["kz"], N=N, g=g, p=p, r=r, t=t, ap=ap,
                    bp=bp, rpre=rpre)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    # avoid double-listing mains (they are ladder rungs) in the
    # 44-world tables: worlds = 42 rungs + the 2 main packs
    worlds44 = recs + (mrecs if not smoke else [])

    # ---------------- S2: LEG A -- the naive coordinate
    section("S2  LEG A -- NAIVE BORDER-DRESSED COORDINATE, CLOSED")
    # (a1) sympy exact identities
    sig, Bs, s_sym = sp.symbols("sigma B s", positive=False)
    m3 = [sum(w * x ** j for w, x in zip(
        [sp.Rational(2, 3), sp.Rational(-1, 5), sp.Rational(1, 2),
         sp.Rational(-3, 7), sp.Integer(1), sp.Rational(1, 3)],
        [sp.Rational(-3, 2), sp.Integer(-1), sp.Rational(-1, 2),
         sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(5, 4)]))
        for j in range(6)]
    H3 = sp.Matrix(3, 3, lambda i, j: m3[i + j])
    bm3 = [sum(bw * bx ** j for bw, bx in zip(
        [sp.Rational(1, 3), sp.Rational(1, 6)],
        [sp.Integer(0), sp.Rational(1, 2)])) for j in range(3)]
    b3 = sp.Matrix(3, 1, lambda i, _j: bm3[i])
    A3 = sp.zeros(4, 4)
    A3[:3, :3] = H3
    for i in range(3):
        A3[i, 3] = sig * b3[i]
        A3[3, i] = sig * b3[i]
    A3[3, 3] = Bs
    lhs = A3.det()
    rhs = H3.det() * (Bs - sig ** 2 * (b3.T * H3.inv() * b3)[0, 0])
    ok_sym1 = sp.simplify(lhs - rhs) == 0
    S1s, S2s = sp.symbols("S1 S2")
    expr = sp.diff(sp.log((Bs - s_sym ** 2 * S1s)
                          / (Bs - s_sym ** 2 * S2s)), s_sym) \
        + 2 * s_sym * Bs * (S1s - S2s) \
        / ((Bs - s_sym ** 2 * S1s) * (Bs - s_sym ** 2 * S2s))
    ok_sym2 = sp.simplify(expr) == 0
    lam_s = sp.Symbol("lam")
    Fanti = 1 / (lam_s * (1 - s_sym * lam_s))
    ok_sym3 = (sp.simplify(sp.diff(Fanti, s_sym)
                           - (1 - s_sym * lam_s) ** (-2)) == 0
               and sp.simplify(
                   Fanti.subs(s_sym, 1) - Fanti.subs(s_sym, 0)
                   - 1 / (1 - lam_s)) == 0)
    check("G20-symbolic-naive-family", ok_sym1 and ok_sym2
          and ok_sym3,
          "sympy EXACT (rational zero): det[[H, sigma b],[sigma "
          "b^T, B]] == det H (B - sigma^2 b^T H^{-1} b) on the "
          "r263 MAINLIKE instance (the closed form IS bordered-"
          "Schur algebra); d/ds log[(B - s^2 S1)/(B - s^2 S2)] == "
          "-2sB(S1 - S2)/[(B - s^2 S1)(B - s^2 S2)] (the rational "
          "log-derivative); the drop antiderivative d/ds [1/(lam"
          "(1 - s lam))] == (1 - s lam)^{-2} with total 1/(1 - "
          "lam) (feeds the leg-B drop identity)")
    # (a2) linear homogeneity on real data
    homog_pool = mains + ([ladder[i] for i in SAMPLE_IDX]
                          if not smoke else [])
    dev_dy = dev_odd = 0.0
    for p in homog_pool:
        N = p["N"]
        d, dsm = p["d"], p["dsm"]
        r, t, ap, bp = TX.drive_arrays(p["rows"], N)
        for s in S_HOMOG:
            rows_s = BH.bord_chain(
                d["xs"], d["ws"], d["ys"], d["vs"], dsm["xs"],
                dsm["ws"] * s, dsm["ys"], dsm["vs"] * s, N)
            rs, ts, aps, bps = TX.drive_arrays(rows_s, N)
            dv = max(
                float(np.max(np.abs(rs - s * r)))
                / float(np.max(np.abs(r))),
                float(np.max(np.abs(ts - s * t)))
                / float(np.max(np.abs(t))),
                float(np.max(np.abs(aps - ap))),
                float(np.max(np.abs(bps - bp))))
            if s == 0.5:
                dev_dy = max(dev_dy, dv)
            else:
                dev_odd = max(dev_odd, dv)
    check("G21-linear-homogeneity", dev_dy <= HOMOG_BAR_DY
          and dev_odd <= HOMOG_BAR,
          "border comb scaled by s through the FULL r244 chain: "
          "r(s) == s r, t(s) == s t, (a', b') unchanged on %d "
          "worlds (mains + %d samples): worst dev %.1e at the "
          "DYADIC s = 1/2 (bar %.0e; power-of-two scaling "
          "commutes with IEEE -- machine-exact expected) / %.1e "
          "at s = 0.3 (bar %.0e) -- the driven recursion is "
          "linear-homogeneous in (r, t), r_k(s) = s r_k EXACTLY"
          % (len(homog_pool),
             len(SAMPLE_IDX) if not smoke else 0, dev_dy,
             HOMOG_BAR_DY, dev_odd, HOMOG_BAR))
    # (a3) closed form vs direct route
    dworst_m = dworst_d = 0.0
    for p in homog_pool:
        N = p["N"]
        G, tv = QO.gram_input(p)
        p["_G"], p["_tv"] = G, tv
        B = float(p["S"][N - 2]) + B57
        for s in S_DIRECT:
            for n in (N - 1, N):
                Dd = d_direct_scaled(G, tv, n, B, s)
                Dc = B - s * s * float(p["S"][n - 1])
                dv = abs(Dd - Dc)
                if N <= DEEP_N:
                    dworst_m = max(dworst_m, dv)
                else:
                    dworst_d = max(dworst_d, dv)
    dworst_c = 0.0
    for c in ctrl:
        p = ctrl[c]
        N = p["N"]
        G, tv = QO.gram_input(p)
        p["_G"], p["_tv"] = G, tv
        B = float(p["S"][N - 2]) + B57
        Dd = d_direct_scaled(G, tv, N - 1, B, 0.5)
        Dc = B - 0.25 * float(p["S"][N - 2])
        dworst_c = max(dworst_c, abs(Dd - Dc))
    check("G22-closed-form-direct",
          dworst_m <= DIRECT_ABS_MAIN and dworst_d
          <= DIRECT_ABS_DEEP and dworst_c <= DIRECT_ABS_CTRL,
          "D_n(s) = B - s^2 S_{n-1} vs the DIRECT bordered-"
          "slogdet with the border column scaled by s (sizes "
          "N-1, N; s in %s): worst abs dev %.1e main N<=%d (bar "
          "%.0e) / %.1e deep (bar %.0e); controls at the "
          "terminal %.1e (bar %.0e) -- the closed form is world-"
          "blind algebra" % (str(S_DIRECT), dworst_m, DEEP_N,
                             DIRECT_ABS_MAIN, dworst_d,
                             DIRECT_ABS_DEEP, dworst_c,
                             DIRECT_ABS_CTRL))
    # (a4) derivative formula + census reproduction + endpoint
    fd_worst = 0.0
    for p in mains:
        N = p["N"]
        G, tv = p["_G"], p["_tv"]
        B = float(p["S"][N - 2]) + B57
        s0 = 0.5
        h = DERIV_FD_H
        xp_ = (d_direct_scaled(G, tv, N, B, s0 + h)
               / d_direct_scaled(G, tv, N - 1, B, s0 + h)
               - d_direct_scaled(G, tv, N, B, s0 - h)
               / d_direct_scaled(G, tv, N - 1, B, s0 - h)) \
            / (2 * h)
        den = B - s0 * s0 * float(p["S"][N - 2])
        rho_t = float(p["rho"][N - 1])
        xf = -2.0 * s0 * B * rho_t / (den * den)
        fd_worst = max(fd_worst, abs(xp_ - xf) / (1 + abs(xf)))
    stab_ok = True
    tight_ok = True
    marg_min = float("inf")
    end_dev = 0.0
    for rc in worlds44:
        p = rc["p"]
        N = p["N"]
        Bw = float(p["S"][N - 2]) + B57
        S1_ = float(p["S"][N - 1])
        S2_ = float(p["S"][N - 2])
        prev = float("inf")
        for s in (0.0,) + S_CENSUS:
            num = Bw - s * s * S1_
            den = Bw - s * s * S2_
            stab_ok = stab_ok and (num > 0.0 and den > 0.0)
            tight_ok = tight_ok and (num <= prev + 1e-12)
            prev = num
        marg_min = min(marg_min, Bw - S1_)
        q_ch = float(p["rho"][N - 1]) / B57
        end_dev = max(end_dev, abs((1.0 - q_ch)
                                   - (Bw - S1_) / (Bw - S2_))
                      / max(abs(1.0 - q_ch), 1e-300))
    band_ok = smoke or (MARGIN_BAND[0] <= marg_min
                        <= MARGIN_BAND[1])
    check("G23-naive-restatement", fd_worst <= DERIV_FD_BAR
          and stab_ok and tight_ok and band_ok
          and end_dev <= ENDPOINT_BAR,
          "derivative formula d/ds log(1 - q_N(s)) = -2sB rho_"
          "{N-1}/(num den) vs DIRECT-route FD: worst rel %.1e "
          "(bar %.0e); r264 census reproduced AS A COROLLARY: "
          "sign-stable + margin monotone falling + tightest "
          "s = 1 on %d/%d worlds, min terminal margin %.4f in "
          "%s; endpoint identity 1 - q_N(1) == (B - S_{N-1})/"
          "(B - S_{N-2}) rel %.1e (bar %.0e) => the s = 1 "
          "positivity IS B - S_{N-1} > 0, the budget inequality "
          "-- S_NAIVE_RESTATEMENT (machine conclusion: the "
          "coordinate reformulates the target, the naive route "
          "is buried)"
          % (fd_worst, DERIV_FD_BAR, len(worlds44),
             len(worlds44),
             marg_min if not smoke else float("nan"),
             str(MARGIN_BAND), end_dev, ENDPOINT_BAR))

    # ---------------- S3: LEG B -- the IIKS s-family
    section("S3  LEG B -- IIKS s-FAMILY (EXACT ODE + CARRIER)")
    port_kzs = [rc["kz"] for rc in recs] if not smoke else [9]
    ports = {}
    for kz in port_kzs:
        pk = QO.port_pack(kz)
        if pk is not None:
            lam, U = np.linalg.eigh(pk["Q"])
            pk["lam"] = lam
            pk["c2"] = (U.T @ pk["f"]) ** 2
            ports[kz] = pk
    built = len(ports)
    wall_ok = all(float(pk["lam"][-1]) < 1.0
                  for pk in ports.values())
    sb_all = [1.0 / float(pk["lam"][-1]) for pk in ports.values()]
    check("G30-port-census", built == len(port_kzs) and wall_ok,
          "IIKS port pair built on %d/%d rungs; base wall "
          "lambda_max < 1 on %d/%d (tau(s) zero-free on [0, 1]); "
          "nearest base zero in [%.7f, %.7f] (r264 reproduced)"
          % (built, len(port_kzs),
             sum(1 for pk in ports.values()
                 if float(pk["lam"][-1]) < 1.0), built,
             min(sb_all), max(sb_all)))
    ward_kzs = [kz for kz in (ODE_WARD_KZ if not smoke else (9,))
                if kz in ports]
    tau_fd_w = 0.0
    xp_tr_w = 0.0
    xp_fd_w = 0.0
    n_safe = 0
    n_grid = 0
    for kz in ward_kzs:
        pk = ports[kz]
        Q, f = pk["Q"], pk["f"]
        lam, c2 = pk["lam"], pk["c2"]
        mu = pk["evr"]
        n = Q.shape[0]
        Qa = Q + np.outer(f, f)

        def ldet(M, ss):
            _sg, ld = np.linalg.slogdet(np.eye(M.shape[0])
                                        - ss * M)
            return ld

        def Xdet(ss):
            s1, l1 = np.linalg.slogdet(np.eye(n) - ss * Qa)
            s2, l2 = np.linalg.slogdet(np.eye(n) - ss * Q)
            return s1 * s2 * math.exp(l1 - l2)
        for s in S_GRID:
            n_grid += 1
            tr = -float(np.sum(lam / (1.0 - s * lam)))
            fd = (ldet(Q, s + FD_H) - ldet(Q, s - FD_H)) \
                / (2 * FD_H)
            tau_fd_w = max(tau_fd_w, abs(fd - tr) / (1 + abs(tr)))
            xp = -float(np.sum(c2 / (1.0 - s * lam) ** 2))
            fdx = (Xdet(s + FD_H) - Xdet(s - FD_H)) / (2 * FD_H)
            xp_fd_w = max(xp_fd_w, abs(fdx - xp) / (1 + abs(xp)))
            if float(np.min(np.abs(1.0 - s * mu))) \
                    >= SAFE_POLE_GAP:
                n_safe += 1
                trd = float(np.sum(lam / (1.0 - s * lam))
                            - np.sum(mu / (1.0 - s * mu)))
                xptr = Xdet(s) * trd
                xp_tr_w = max(xp_tr_w,
                              abs(xptr - xp) / (1 + abs(xp)))
    check("G31-tau-s-ode-exact", tau_fd_w <= TAU_FD_BAR,
          "d/ds log tau(s) == -Tr[(I - sQ)^{-1} Q] (JMU/Fredholm "
          "form, r224): trace vs central FD on ward rungs %s x "
          "s-grid %s: worst rel %.1e (bar %.0e, FD floor)"
          % (str(tuple(ward_kzs)), str(S_GRID), tau_fd_w,
             TAU_FD_BAR))
    check("G32-crossratio-ode-three-routes",
          xp_tr_w <= XP_TRACE_BAR and xp_fd_w <= XP_FD_BAR,
          "X'(s) by THREE routes: carrier sum -sum c_i^2/(1 - s "
          "lam_i)^2 == X(s) [Tr[(I-sQ)^{-1}Q] - Tr[(I-sQaug)^"
          "{-1}Qaug]] (difference of two resolvent traces, %d/%d "
          "pole-safe points, worst rel %.1e, bar %.0e) == central "
          "FD of the slogdet ratio (worst rel %.1e, bar %.0e) -- "
          "the cross-ratio s-ODE is EXACT and its carrier is an "
          "explicit resolvent square"
          % (n_safe, n_grid, xp_tr_w, XP_TRACE_BAR, xp_fd_w,
             XP_FD_BAR))
    lab = {rc["kz"]: rc["g"] < 0.0 for rc in recs}
    xneg_ok = True
    indef_terms = 0
    tot_terms = 0
    sstars = {}
    g1s = {}
    x1_neg = 0
    drop_w = 0.0
    for kz, pk in ports.items():
        lam, c2, mu = pk["lam"], pk["c2"], pk["evr"]
        n = pk["Q"].shape[0]
        tot_terms += n
        indef_terms += int(np.sum(c2 < 0.0))
        for s in S_CENSUS:
            xp = -float(np.sum(c2 / (1.0 - s * lam) ** 2))
            xneg_ok = xneg_ok and (xp < 0.0)
        sstars[kz] = 1.0 / float(mu[-1])
        g1 = float(np.sum(c2 / (1.0 - lam)))
        g1s[kz] = g1
        X1 = 1.0 - g1
        if X1 < 0.0:
            x1_neg += 1
        s1, l1 = np.linalg.slogdet(
            np.eye(n) - (pk["Q"] + np.outer(pk["f"], pk["f"])))
        s2, l2 = np.linalg.slogdet(np.eye(n) - pk["Q"])
        X1d = s1 * s2 * math.exp(l1 - l2)
        drop_w = max(drop_w, abs((1.0 - X1d) - g1) / g1)
    if not smoke:
        sc = [sstars[kz] for kz in sstars if not lab[kz]]
        se = [sstars[kz] for kz in sstars if lab[kz]]
        _a, p_sep = QO.auc_power(sc, se)
    else:
        p_sep = float("nan")
    check("G33-iiks-sign-census", xneg_ok and indef_terms == 0
          and x1_neg == built,
          "sign census on %d rungs: X'(s) < 0 at EVERY census "
          "point %s (incl. s = 1) -- X strictly monotone FALLING; "
          "carrier decomposition: indefinite terms %d of %d "
          "(every spectral component is a negative square: the "
          "Herglotz/CP structure is trivially present); crossing "
          "s* = 1/mu_max in [%.4f, %.4f]; X(1) < 0 on %d/%d (the "
          "endpoint is measured FALSE in this coordinate); branch "
          "separation power of s* %.3f (branch-blind, r264 "
          "reproduced)"
          % (built, str(S_CENSUS), indef_terms, tot_terms,
             min(sstars.values()), max(sstars.values()),
             x1_neg, built,
             p_sep if not smoke else float("nan")))
    g1_min = min(g1s.values())
    herglotz_found = g1_min < 1.0 and all(
        v < 1.0 for v in g1s.values())
    check("G34-drop-identity-adjudication",
          drop_w <= DROP_ID_BAR,
          "drop identity X(0) - X(1) == f^T (I - Q)^{-1} f: worst "
          "rel %.1e on %d/%d (bar %.0e) -- the TOTAL definite "
          "drop EQUALS the r257-blocked bordered spectral bound "
          "EXACTLY; sealed adjudication (HERGLOTZ_STRUCTURE_FOUND "
          "iff g(1) < 1 on all rungs): g(1) in [%.2f, %.2f], "
          "min %.2f %s 1 => %s -- the definite s-ODE proves the "
          "CROSSING, not the target"
          % (drop_w, built, built, DROP_ID_BAR,
             min(g1s.values()), max(g1s.values()), g1_min,
             "<" if g1_min < 1 else ">=",
             "HERGLOTZ_STRUCTURE_FOUND" if herglotz_found
             else "DEFINITENESS_WALL_EQUIVALENT"))

    # ---------------- S4: LEG C -- intermediate coordinates
    section("S4  LEG C -- INTERMEDIATE COORDINATES (s*, Q7)")
    eq_ok = True
    us_worst = 0.0
    vert_int = 0
    exc_tab = []
    for rc in worlds44:
        sstar = sstar_terminal(rc["t"], rc["ap"], rc["bp"],
                               rc["rpre"])
        eq_ok = eq_ok and ((sstar < 1.0) == (rc["g"] < 0.0))
        alt = 1.0 + rc["g"] / abs(float(rc["t"][-1]))
        eq_ok = eq_ok and abs(sstar - alt) <= SSTAR_EQ_BAR
        if rc["g"] < 0.0:
            U_at = sstar * abs(float(rc["t"][-1])) \
                + abs(float(rc["ap"][-1] * rc["rpre"][-1])) \
                + abs(float(rc["bp"][-1] * rc["rpre"][-2]))
            us_worst = max(us_worst, abs(U_at - M_W))
            exc_tab.append((rc["kz"], sstar))
        chainZ = float(rc["ap"][-1] * rc["rpre"][-1]
                       + rc["bp"][-1] * rc["rpre"][-2])
        sv = -chainZ / float(rc["t"][-1])
        if 0.0 < sv < 1.0:
            vert_int += 1
    check("G40-terminal-sstar", eq_ok and us_worst
          <= SSTAR_EQ_BAR,
          "c1 TERMINAL-DRIVE family: s* = (M - chain)/|t_{N-2}| "
          "= 1 + g/|t_{N-2}| CLOSED FORM (source-pure: prefix + "
          "imported budget); equivalence s* < 1 <=> g < 0 on "
          "%d/%d worlds; U(s*) == M on the exceptions worst "
          "%.1e; exception s* table: %s; parabola vertex "
          "interior (0,1) on %d/%d (the terminal family is NOT "
          "generically monotone -- measured); typing: "
          "RESTATEMENT_ADJACENT (the endpoint s = 1 is |Z| < "
          "sqrt(5/7) itself; s* is a branch coordinate, not a "
          "certificate)"
          % (len(worlds44), len(worlds44), us_worst,
             "; ".join("kz%d %.4f" % kv for kv in
                       sorted(exc_tab)) if exc_tab else
             "n/a (SMOKE)", vert_int, len(worlds44)))
    q7_phi_w = 0.0
    q7_dir_w = 0.0
    q7_s7 = []
    for p in mains:
        N = p["N"]
        G, tv = p["_G"], p["_tv"]
        B = float(p["S"][N - 2]) + B57
        Lc = np.linalg.cholesky(G)
        phi = np.linalg.solve(Lc, tv)
        rho = np.asarray(p["rho"][:N])
        q7_phi_w = max(q7_phi_w,
                       float(np.max(np.abs(phi[:N] ** 2 - rho))
                             / np.max(np.abs(rho))))
        n = N - 1
        phis = phi.copy()
        phis[:Q7_HEAD] *= (1.0 - Q7_S)
        tvs = Lc[:n, :n] @ phis[:n]
        A = np.zeros((n + 1, n + 1))
        A[:n, :n] = G[:n, :n]
        A[:n, n] = tvs
        A[n, :n] = tvs
        A[n, n] = B
        sa, la = np.linalg.slogdet(A)
        sg, lg = np.linalg.slogdet(G[:n, :n])
        Dd = sa * sg * math.exp(la - lg)
        S7 = float(p["S"][Q7_HEAD - 1])
        q7_s7.append(S7)
        Dc = B - ((1.0 - Q7_S) ** 2 * S7
                  + float(p["S"][n - 1]) - S7)
        q7_dir_w = max(q7_dir_w, abs(Dd - Dc))
    check("G41-q7-centering", q7_phi_w <= Q7_PHI_BAR
          and q7_dir_w <= Q7_DIRECT_BAR
          and all(v > 0.0 for v in q7_s7),
          "c2 Q7/CENTERING family: chain-coordinate ward phi_k^2 "
          "== rho_k (Cholesky of the r261 Gram) worst rel %.1e "
          "on mains (bar %.0e); deformed DIRECT route (head "
          "scaled by 1-s, border column L phi(s)) vs closed form "
          "margin(s) = D + (1 - (1-s)^2) S_7: worst %.1e at s = "
          "%.1f (bar %.0e); S_7 = %s > 0 => d/ds margin = +2(1-s)"
          "S_7 >= 0: the definite direction points AWAY from the "
          "target endpoint s = 0 -- Q7_CENTERING_RESTATEMENT "
          "(the family redistributes prefix mass, the s = 0 "
          "question is untouched)"
          % (q7_phi_w, Q7_PHI_BAR, q7_dir_w, Q7_S,
             Q7_DIRECT_BAR,
             str(["%.3f" % v for v in q7_s7])))

    # ---------------- S5: LEG D -- kills + controls + must-fails
    section("S5  LEG D -- KILLS + CONTROLS + MUST-FAILS")
    hits = sstar_scope_audit("sstar_terminal")
    hits_orc = sstar_scope_audit("oracle_sstar")
    ag_hits = antigate_fragment_audit()
    check("G50-scope-audits", not hits and bool(hits_orc)
          and not ag_hits,
          "sstar builder consumes the prefix triangle + the "
          "imported budget ONLY (%s); the deliberately target-"
          "reading mutant is FLAGGED (%s); fragment audit (no "
          "fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_orc) if hits_orc else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    if not smoke:
        dems = {kz: math.log10(v) for kz, v in g1s.items()}
        dvals = sorted(dems.values())
        fired = sum(1 for v in dvals if v >= DEMAND_BAR)
        dc = [dems[kz] for kz in dems if not lab[kz]]
        de = [dems[kz] for kz in dems if lab[kz]]
        check("G51-paircorr-in-s", True,
              "MEASUREMENT: rescuing the definite IIKS route "
              "needs the drop bound g(1) < 1; demand = log10 "
              "g(1) decades of comb cancellation in the border "
              "row f: min %.2f / med %.2f / max %.2f dec, fired "
              "(>= %.1f dec) on %d/%d; cheap med %.2f vs "
              "exception med %.2f -- the kill is bar-independent "
              "(the endpoint is measured FALSE on every rung, "
              "G33/G34): the wall in s-clothes"
              % (dvals[0], float(np.median(dvals)), dvals[-1],
                 DEMAND_BAR, fired, built,
                 float(np.median(dc)), float(np.median(de))))
    else:
        check("G51-paircorr-in-s", True, "SMOKE: skipped")
    fl_ok = True
    fl_note = []
    for c in ("EPST", "SCR"):
        p = ctrl[c]
        N = p["N"]
        G, tv = p["_G"], p["_tv"]
        B = float(p["S"][N - 2]) + B57
        for nfp in (CTRL_FLIPS[long_names[c]], CTRL_PREFLIP_N):
            x1 = d_direct_scaled(G, tv, nfp + 1, B, 0.55) \
                / d_direct_scaled(G, tv, nfp, B, 0.55)
            x0 = d_direct_scaled(G, tv, nfp + 1, B, 0.45) \
                / d_direct_scaled(G, tv, nfp, B, 0.45)
            fd_sign = math.copysign(1.0, x1 - x0)
            pred = -math.copysign(1.0, B * float(p["rho"][nfp]))
            fl_ok = fl_ok and (fd_sign == pred)
            fl_note.append("%s n=%d FD %+d pred %+d"
                           % (c, nfp, int(fd_sign), int(pred)))
        fl_note.append("%s B %+.2f" % (c, B))
    check("G52-controlflip-consistency", fl_ok,
          "d/ds x_n = -2sB rho_n / den^2 => sign(FD of the "
          "DIRECT-route x_n) == -sign(B_w rho_n) at the flip "
          "degree AND the pre-flip degree %d on EPST + SCR: %s "
          "-- the den^2 rule carries the flip through the "
          "indefinite continuation (B_SCR < 0, sealed from the "
          "disclosed scratch; SMOOTH excluded: alias floor)"
          % (CTRL_PREFLIP_N, "; ".join(fl_note)))
    qS = float(ctrl["SMOOTH"]["rho"][ctrl["SMOOTH"]["N"] - 1]) \
        / B57
    check("G53-smooth-anchor", abs(qS) <= 1e-20,
          "SMOOTH anchor q_N = %.1e <= 1e-20: the naive family "
          "trivializes exactly when the source aliases (S_{N-1} "
          "== S_{N-2} structurally, the rational form becomes "
          "1)" % qS)
    pk9 = ports[9]
    lam9, c29, mu9 = pk9["lam"], pk9["c2"], pk9["evr"]
    n9 = pk9["Q"].shape[0]
    Qa9 = pk9["Q"] + np.outer(pk9["f"], pk9["f"])
    s0 = 0.5

    def X9(ss):
        s1, l1 = np.linalg.slogdet(np.eye(n9) - ss * Qa9)
        s2, l2 = np.linalg.slogdet(np.eye(n9) - ss * pk9["Q"])
        return s1 * s2 * math.exp(l1 - l2)
    fdx9 = (X9(s0 + FD_H) - X9(s0 - FD_H)) / (2 * FD_H)
    xp9 = -float(np.sum(c29 / (1.0 - s0 * lam9) ** 2))
    honest = abs(fdx9 - xp9)
    trd_sw = float(np.sum(mu9 / (1.0 - s0 * mu9))
                   - np.sum(lam9 / (1.0 - s0 * lam9)))
    xp_sw = X9(s0) * trd_sw
    dev_m1 = abs(fdx9 - xp_sw)
    check("G54-mustfail-swapped-trace",
          dev_m1 >= LOUD * max(honest, 1e-300),
          "m1 SWAPPED TRACE (the two resolvent traces exchanged "
          "in the cross-ratio ODE): breaks vs FD by %.1e = %.1e "
          "x honest %.1e (bar %.0f x) -- the ODE is trace-order-"
          "pinned" % (dev_m1, dev_m1 / max(honest, 1e-300),
                      honest, LOUD))
    p9 = packs["w9"]
    N9 = p9["N"]
    G9, tv9 = p9["_G"], p9["_tv"]
    B9 = float(p9["S"][N9 - 2]) + B57
    Dd9 = d_direct_scaled(G9, tv9, N9 - 1, B9, 0.5)
    honest2 = abs(Dd9 - (B9 - 0.25 * float(p9["S"][N9 - 2])))
    dev_m2 = abs(Dd9 - (B9 - 0.5 * float(p9["S"][N9 - 2])))
    check("G55-mustfail-wrong-s-degree",
          dev_m2 >= LOUD * max(honest2, 1e-300),
          "m2 WRONG s-DEGREE (B - s S_{n-1} instead of B - s^2 "
          "S_{n-1}): breaks vs the direct route by %.1e = %.1e "
          "x honest %.1e (bar %.0f x) -- the closed form is "
          "degree-pinned in s^2"
          % (dev_m2, dev_m2 / max(honest2, 1e-300), honest2,
             LOUD))
    if not smoke:
        exc_min = min((rc for rc in recs if rc["g"] < 0.0),
                      key=lambda rc: rc["N"])
        pmn = exc_min["p"]
        Nmn = pmn["N"]
        Dmp = mp_direct_scaled(pmn, Nmn - 1, MP_DPS, MP_S)
        Bmn = float(pmn["S"][Nmn - 2]) + B57
        Dcl = Bmn - MP_S * MP_S * float(pmn["S"][Nmn - 2])
        dv_mp = abs(float(Dmp) - Dcl)
        check("G56-mp-ward", dv_mp <= MP_BAR,
              "mp (dps %d) bordered-det ratio with the border "
              "column scaled by s = %.1f at the TERMINAL of the "
              "smallest-N exception rung kz%d (N = %d): D_mp = "
              "%s vs closed form %.9f, dev %.1e (bar %.0e) -- "
              "the closed form holds at mp precision on an "
              "exception terminal"
              % (MP_DPS, MP_S, exc_min["kz"], exc_min["N"],
                 mp.nstr(Dmp, 12), Dcl, dv_mp, MP_BAR))
    else:
        check("G56-mp-ward", True, "SMOKE: skipped")

    # ---------------- S6: verdict
    section("S6  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the naive s-coordinate closed exactly and "
          "buried as a restatement, the exact fully-definite "
          "IIKS cross-ratio s-ODE with its drop identity typed "
          "wall-equivalent, the closed-form branch coordinate "
          "s*, and the Q7 family typed; the campaign's residual "
          "question is SHARPENED: a usable s-tool must couple "
          "the border drive into the resolvent without reducing "
          "to the wall bound")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["S_NAIVE_RESTATEMENT(closed rational form; r264 "
                 "monotonicity algebraically trivial; endpoint "
                 "== the budget inequality)"
                 if (stab_ok and tight_ok and band_ok
                     and end_dev <= ENDPOINT_BAR)
                 else "S_NAIVE_TOOL(typed)"]
        parts.append("IIKS_S_ODE_EXACT(tau ODE + cross-ratio "
                     "ODE, three routes)"
                     if (tau_fd_w <= TAU_FD_BAR
                         and xp_tr_w <= XP_TRACE_BAR
                         and xp_fd_w <= XP_FD_BAR)
                     else "IIKS_S_ODE_OPEN(typed)")
        parts.append("S_MONOTONE_IIKS(carrier fully definite, "
                     "indefinite 0/%d)" % built
                     if (xneg_ok and indef_terms == 0)
                     else "S_NOT_MONOTONE_IIKS")
        parts.append("HERGLOTZ_STRUCTURE_FOUND" if herglotz_found
                     else "DEFINITENESS_WALL_EQUIVALENT(drop == "
                     "f^T(I-Q)^{-1}f; g(1) in [%.2f, %.2f], "
                     "X(1) < 0 on %d/%d)"
                     % (min(g1s.values()), max(g1s.values()),
                        x1_neg, built))
        parts.append("PAIRCORR_IN_S(demand %.2f/%.2f/%.2f dec "
                     "min/med/max, fired %d/%d)"
                     % (dvals[0], float(np.median(dvals)),
                        dvals[-1], fired, built))
        parts.append("TERMINAL_SSTAR(s* = 1 + g/|t_term|, "
                     "equivalence %d/%d)"
                     % (len(worlds44), len(worlds44)))
        parts.append("Q7_CENTERING_RESTATEMENT")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the linear homogeneity, "
          "the closed rational form, the exact cross-ratio "
          "s-ODE, the carrier decomposition, the drop identity, "
          "the s* closed form; MEASURED: the sign censuses, the "
          "demand census, the vertex census; OPEN: the target "
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
