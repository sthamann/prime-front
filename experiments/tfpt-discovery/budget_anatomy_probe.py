#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""budget_anatomy_probe -- PRIME.PORT.RHP.BUDGET.ANATOMY.01
(round 258): the anatomy of the r257 drain and the TERMINAL
REDUCTION.  After r257 (COUPLED_RECURSION_EXACT: the pair (tau,
tau^aug) closes under tau_{n+1} = a_n tau_n, tau^aug_{n+1} = a_n
tau^aug_n + b_n tau_n, equivalently D_{n+1} = D_n - rho_n with
rho_n = F_n^2/h_n >= 0 on MAIN; anchor D_N = 5/7 - rho_{N-1}) the
fiber positivity is the BUDGET INEQUALITY of a monotone drain.
THIS round clarifies the suspected COLLAPSE STRUCTURE: with
B_w = S_{N-2} + 5/7 the budget question telescopes COMPLETELY
onto the single terminal inequality rho_{N-1} < 5/7, i.e.
F_{N-1}^2 < (5/7) h_{N-1} -- and that terminal statement is a
t*-COORDINATE in exact normal form (the return of the r238/r239
coordinate).

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r257 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots h_{w,k}
(k < N_w) are the proof objects; rho_k = F_k^2/h_k, S_n =
sum_{k<=n} rho_k; ground truth (h signs, flip degrees) enters
GATES only; no zero/prime oracles anywhere (AST firewall).
MACHINERY IMPORTED VERBATIM: r244 BH.wpack (chain, rho, S, b1),
r257 CT.u_matrix/union_arrays/mp_trunc_ward/spearman, r254
OG.phat_matrix, r243 PB.smooth_comb, v881 PIK controls.  B
PROVENANCE: B_w = S_{N-2} + 5/7 (r243 amendment a4, IMPORTED,
never fitted).  POSITIVITY TYPING (r256): POSITIVE_PREFIX vs
INDEFINITE_CONTINUATION; controls SCR/EPST/SMOOTH flip 21/25/27.

LEG A -- THE EXACT TELESCOPE IDENTITY (the foundation): (a1) in
what sense does B = S_{N-2} + 5/7 hold?  ANSWER SEALED AS THE
CLAIM UNDER TEST: it is EXACT BY CONSTRUCTION -- B is DEFINED as
prefix data + the imported terminal constant (r243 a4); the
nontrivial exact content is the SCHUR TELESCOPE D_N = B - S_{N-1}
(det factorization), whose combination gives D_N = 5/7 - rho_{N-1}
as an ALGEBRAIC IDENTITY.  Gates: direct bordered slogdet (sealed
scaled-Chebyshev hull basis, r257 route) at FULL depth vs
5/7 - rho_{N-1} on the four main windows w9/w12/w13/w26 AND the
sealed 9-rung ladder sample (indices (0, 5, 10, 15, 20, 25, 30,
35, 41) of the (N, kz)-sorted 42-rung frame-A h <= 900 ladder,
including the largest N = 878); bars 1e-8 mains / 3e-6 deep (f64
route floors from the two disclosed pre-spec scratch
calibrations: worst 1.3e-9 / 9.5e-8; the EXACTNESS claim is
carried by the mp wards, the f64 deviation is CONDITIONING, its
N-slope is printed as the honest error law of the ROUTE, not of
the identity); mp truncation wards (dps 220, r257 pattern,
corner 5/7) at sealed n_t in {12, 24} on w9 AND n_t = 12 on the
largest rung, bar 1e-12.  (a2) WHERE DOES THE 5/7 COME FROM
(source-pure audit): the import chain r243 <- r241 defines 5/7 =
1/(7/5) with 7/5 the FROZEN r241 FLOOR of the measured terminal
ratio h_{N-1}/F_{N-1}^2; gate: reproduce min_w h_{N-1}/F_{N-1}^2
on all 42 in the sealed band [1.40, 1.46] AND >= 7/5 with
NON-SATURATION margin >= 0.01 (the measured floor 1.4278 is NOT
7/5: the constant is a chosen round rational BELOW the measured
surface saturation).  SEALED ADJUDICATION of the two named origin
hypotheses: Q7_SHARE and LEVEL8_SUBTRACTION are NOT_SUPPORTED
unless the floor saturates 7/5 to 1e-6 (it does not) or a
source-pure compile path exists in the import chain (it does
not; the only occurrences are the r241/r243 floor literals) =>
5/7 stays FLOOR_IMPORTED(r241), source derivation OPEN.  (a3)
margin equivalence: sign(D_N) == sign(5/7 - rho_{N-1}) on the
full sample AND on the w9 controls (there ALGEBRAIC, typed
INDEFINITE_CONTINUATION); on MAIN both sides positive.  If any
telescope gate fails: TELESCOPE_APPROX with the measured error
law -- the budget question is then typed TWO-TERM (terminal +
residual).

LEG B -- THE TERMINAL INEQUALITY OVER THE LADDER: q_N :=
rho_{N-1}/(5/7) on ALL 42 rungs (N = 142..878).  (b1) census:
q < 1 on 42/42 (reproduces the r243 razor, min margin band
[0.010, 0.020] on 5/7 - rho_{N-1}); distribution (min/med/max);
wall margin gap = 1 - q_N vs N: LS slope + Spearman, sealed
trend rule (bar 0.5): APPROACHING iff Spearman <= -0.5, RECEDING
iff >= +0.5, else FLAT.  (b2) the driver decomposition log10 q =
2 log10 |F_{N-1}| - log10 h_{N-1} - log10(5/7): Spearman of
log q vs 2 log|F| and vs log h, plus the CROSS correlation
Spearman(2 log|F|, log h) over the ladder; SEALED DRIVER RULE:
COVARIANT_RATIO iff the cross Spearman >= 0.7 (the two terminal
components track each other and q is the residual of the
covariation); the residual side is F/H if the respective
|Spearman(log q, .)| exceeds the other by >= 0.2, else BALANCED.
(b3) THE t*-CONNECTION (exact): (i) the CORNER RAY B(t) =
S_{N-2} + t (5/7) makes the terminal bordered pivot AFFINE with
slope 5/7 in t (Schur, slope-1 in B); its zero crossing is
t*_bud = rho_{N-1}/(5/7) = q_N EXACTLY -- gated by direct
bordered slogdets at t in {0, 1/2, 1}: collinearity <= 1e-9 rel,
slope == 5/7 and root == q_N (bars 1e-8 mains / 3e-6 deep; the
slope bar was split main/deep at calibration, amendment a1
below); this is the SAME sealed normal form as the r238 t* =
gbar/(gbar - gammahat_N) (terminal pivot affine slope-1 in its
one forced parameter, coordinate = ray crossing, wall = pivot
positive at physical parameter 1) -- the budget question IS a
t*-statement: q_N < 1.  (ii) HONEST TYPING of the r238/r239
INSTANCE: it consumes the forced moment m_{2N} (pivot h_N),
q_N consumes the border readout F_{N-1} -- SAME normal form,
DIFFERENT terminal data; re-derive the r238 census on all 42
(sealed priors: 29 down-crossing windows, 18 with t* < 1 = the
delta = 0 set) and print Spearman(q_N, t*_r238) on the crossing
windows (measurement, no bar).  TSTAR_IDENTIFIED fires iff (i)
passes and (ii) reproduces the census -- worded as: one
COORDINATE NORMAL FORM, two data instances; NEVER as numeric
equality of the two instances (that would be the must-fail
direction).  (b4) worlds: controls' q before their base flip
(q_pre = rho_{pmax-1}/(5/7), pmax = 21/25/27) and the signed
full-depth value typed INDEFINITE_CONTINUATION; SMOOTH is the
alias world: q_N(SMOOTH) <= 1e-20 (F_{N-1} = 0 structurally).

LEG C -- DRAIN PROFILE ANATOMY: (c1) zones (r246 conventions
HEAD n < 8 / BULK / TAIL last 5) on all 42: share medians; the
head is ONE MODE: rho_0 == b1^2/h_0 EXACTLY (rel 1e-12) with
b1 = total signed BORDER mass (zeroth border readout F_0) and
h_0 = total signed window mass -- source-pure WHY of the r246
~44 percent head: the head mode is the raw mass pairing
(border mass)^2/(window mass), no orthogonal-polynomial
oscillation enters; sealed reproduction band median p_0 in
[0.25, 0.55]; ladder spread of rho_0 printed (r246: ~0.2
decades).  (c2) tail decay law: per rung LS fits of log10
rho_n over the sealed bulk window n in [8, N-6]: EXP (vs n)
against POWER (vs log10 n), winner needs rms <= 0.8 x other,
else IRREGULAR; majority token over the 42 rungs + w9/w13
detail, min rho + terminal rebound printed.  (c3) MAJORANTS
(sealed BEFORE evaluation, max 3, all TRUE pointwise bounds by
construction -- ward m_n >= rho_n (1 - 1e-6) on every MAIN rung,
n in [8, N-2], POSITIVE_PREFIX-typed): with phat_n = pihat_n /
sqrt(h_n) at the border atoms and |sigma| the border total
variation:
  M1_SUP: m_n = ||sigma||_TV^2 max_atom phat_n^2   (sup bound),
  M2_CS : m_n = ||sigma||_TV int phat_n^2 d|sigma| (Cauchy-
          Schwarz in |sigma|),
  M3_ABS: m_n = (int |phat_n| d|sigma|)^2          (triangle
          bound; analytically the tightest of the three).
BUDGET TEST per rung and candidate: head as prefix data, does
sum_{n=8}^{N-2} m_n <= (S_{N-2} - S_7) + 5/7 hold?  Coverage
over 42, overshoot factor sum m / budget, break locus argmax_n
m_n (fraction of N).  MAJORANT_FOUND(cand) iff some candidate
covers 42/42; else MAJORANT_OPEN(best candidate, median
overshoot, locus) -- the honest break anatomy is the deliverable
(controls excluded: their budget side is algebraic beyond the
flip, r246 typing).  (c4) PREFIX-BORDER DOMINANCE (the r256
side-finding as its own object): on the sealed 10-rung ladder
kz = (17, 10, 18, 12, 13, 9, 15, 19, 26, 40), per rung the
MAIN x SCRAMBLE(seed 1) cleaned raster at the pair's OWN common
positive prefix n* = min(pmax_M, pmax_C) (re-derived per rung;
r254-a1 sorted-union embedding re-gated; cells by the separable
route T = sum_k sg_k (phat_k . s)^2, r256-identical algebra);
prior re-gate on w9: Dbo* = -0.175897, Gap* = -0.216051, ratio
0.814 (rel 2e-3); rungs with |Gap*| <= 1e-9 x gross typed NULL;
SEALED RULE: PREFIX_DOMINANCE_STABLE iff >= 0.8 of non-null
rungs have sign(Dbo*) == sign(Gap*) AND |Dbo*|/|Gap*| in the
r256 band [0.3, 3.0]; else PREFIX_DOMINANCE_ARTIFACT (the sign
census and the ratio range are printed separately -- a stable
sign with unstable magnitude is typed as such, never upgraded).

LEG D -- FALSIFIERS + MUST-FAILS (each loud, >= 1e3 x honest):
(d1) SHIFTED TELESCOPE INDEX: D_N vs 5/7 - rho_{N-2} must break
the w9 anchor loudly; (d2) SWAPPED F/h: the terminal increment
read as h_{N-1}/F_{N-1}^2 must break loudly; (d3) WRONG t*
NORMALIZATION: t* claimed as rho_{N-1}/(7/5) must miss the
machine root loudly (the 5/7 ray normalization is content);
(d4) SMOOTH ANCHOR: max_{n>=1} |rho_n|/rho_0 <= 1e-18 AND
D_N(SMOOTH) == 5/7 rel 1e-9 AND q_N(SMOOTH) <= 1e-20 -- the
terminal question trivializes exactly when the source aliases.

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs, (N, kz)
sorted); main windows (9, 12, 13, 26); ladder sample indices
(0, 5, 10, 15, 20, 25, 30, 35, 41); controls on w9: EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; FIB_LO 8; direct
bars 1e-8 main / 3e-6 deep / 1e-3 controls; lin bar 1e-9;
slope + root bars 1e-8 main / 3e-6 deep; mp n_t {12, 24} (w9) +
12 (largest), dps 220, bar 1e-12; floor band [1.40, 1.46],
non-saturation 0.01, saturation probe 1e-6; margin band [0.010,
0.020]; trend/driver bars: Spearman 0.5, covariance 0.7, driver
delta 0.2; r238 census priors 29 crossing / 18 below 1; zones
HEAD_K 8 / TAIL_K 5; p0 band [0.25, 0.55]; rho0 identity bar
1e-12; phat-vs-chain rho bar 1e-6; majorant ward tol 1e-6; tail
rms ratio 0.8; c4 ladder (17, 10, 18, 12, 13, 9, 15, 19, 26,
40), prior tol 2e-3, LB band [0.3, 3.0], stability fraction
0.8, null floor 1e-9 x gross; SMOOTH alias 1e-18 / q 1e-20 /
D_N 1e-9; loudness 1e3; runtime <= 1800 s; smoke = w9 (+ w9
controls): telescope w9, corner ray w9, zones w9, majorant w9,
c4 w9 pair, must-fails; ladder legs + mp wards + r238 census
skipped.  DISCLOSED PRE-SPEC SCRATCH CALIBRATIONS (both before
this spec was frozen, informing floors/bands only, no verdict
rule tuned after any full evaluation): (s1) route floors (direct
devs, corner-ray root devs, mp cost, q/t* census scales,
majorant overshoot scale, tail rms scale); (s2) c4 feasibility
(embedding + prefix depths + cell values on the 10-rung
ladder).

SEALED VERDICT FORM (frozen BEFORE the record run, joined '+'):
  TELESCOPE_EXACT(BY_CONSTRUCTION; 5/7 = r241 IMPORTED floor,
    source derivation OPEN) / TELESCOPE_APPROX(error law)
+ TERMINAL_Q_LAW(trend, driver)
+ TSTAR_IDENTIFIED(one normal form, two data instances)
    / TSTAR_OPEN
+ MAJORANT_FOUND(cand) / MAJORANT_OPEN(best, overshoot, locus)
+ PREFIX_DOMINANCE_STABLE(median ratio)
    / PREFIX_DOMINANCE_ARTIFACT(sign census, ratio range).
Honesty before beauty: no verdict claims a derived 5/7, a bound
mechanism, or numeric equality of the two t* instances; the
budget bound and the base law stay OPEN (r243/r246/r247/r256/
r257 stand).

RECORD TABLES (frozen from calibration pass 1, 25/27 gates with
EXACTLY ONE bar amendment, then 27/27; wall 8.5 s full; ALL
verdict rules, candidates, bands and every other bar untouched;
the two pre-spec scratch calibrations are disclosed above.
CALIBRATION AMENDMENT a1 (disclosed, BEFORE the record run):
the corner-ray SLOPE bar was drafted as a single 1e-9 while the
measured slope deviation on the deep rungs is 1.1e-7 -- the SAME
f64 route conditioning already sealed main/deep for the direct
and root gates; the slope bar was split to the identical
main/deep pair 1e-8 / 3e-6; no other change):
CAL_VERDICT = TELESCOPE_EXACT(BY_CONSTRUCTION; 5/7 = r241
IMPORTED floor, source derivation OPEN) +
TERMINAL_Q_LAW(FLAT, COVARIANT_RATIO(residual BALANCED)) +
TSTAR_IDENTIFIED(one normal form, two data instances) +
MAJORANT_OPEN(M3_ABS, overshoot x4.9e+02 med, locus 0.97 N) +
PREFIX_DOMINANCE_ARTIFACT(sign 10/10, ratio 0.006..4.11).
Key numbers.  CENSUS: 42 rungs N in [142, 878], POSITIVE_PREFIX
42/42; controls flip 25/21/27 re-derived.  LEG A: direct
telescope on the 12-window sample worst rel 1.7e-9 (N <= 400) /
9.5e-8 (deep, N = 878), signs exact 12/12; f64 route error law
slope +4.16 dec/dec vs N (CONDITIONING of the route, disclosed
-- the identity itself is definitional + mp-warded); mp
truncation wards (dps 220): w9 2.8e-17 / 1.0e-16, largest rung
(kz 52, N = 878) 2.4e-16 -- the Schur telescope is exact in
exact arithmetic; 5/7 provenance: min_w h_{N-1}/F_{N-1}^2 =
1.4278 in [1.40, 1.46], >= 7/5 with non-saturation margin
0.0278 >= 0.01 => Q7_SHARE and LEVEL8_SUBTRACTION
NOT_SUPPORTED, the constant is the r241 IMPORTED floor (a round
rational BELOW the measured saturation 1.4278; source
derivation OPEN); margin equivalence sign(D_N) == sign(5/7 -
rho_{N-1}) on 12/12 + w9 controls (EPST +1.7922 / SCR +0.5219 /
SMOOTH +0.7143, algebraic, typed).  LEG B: q_N < 1 on 42/42,
min/med/max 0.0015/0.4188/0.9805, min margin 0.0139 (band hit,
r243 razor reproduced); gap = 1 - q_N vs N: slope +0.41,
Spearman +0.357 => FLAT (the wall margin does NOT shrink with N
on this surface); DRIVER: Spearman(2lgF, lgh) = +1.000
(RANK-PERFECT covariation of F_{N-1}^2 and h_{N-1} over the
ladder -- the round's sharpest single finding), residuals
Spearman(lgq, 2lgF) +0.361 vs (lgq, lgh) +0.357 => COVARIANT_
RATIO(residual BALANCED): neither component drives q, the
terminal coordinate is the residual of an exact covariation --
any terminal proof must bound the RATIO, not either side;
corner ray: collinearity worst 3.4e-13, slope vs 5/7 worst
1.1e-7 (deep, = the route floor), root == q_N worst 3.2e-9
main / 5.2e-8 deep on 12/12; r238 census reproduced: 29
down-crossing, 18 below 1 (= the delta = 0 set), 13
no-crossing; Spearman(q_N, t*_r238) on the 29 crossing windows
= +0.027 -- the two instances are STATISTICALLY UNRELATED (one
normal form, two data: the r238 instance reads the forced
moment m_{2N}, q_N reads the border readout F_{N-1}; the
predicates differ on exactly the 18 t* < 1 windows where q_N
< 1 throughout); worlds: q_pre(EPST@25/SCR@21/SMOOTH@27) =
9.6e-5/1.3e-2/2.6e-31, full-depth signed q EPST -1.51 / SCR
+0.27 typed INDEFINITE_CONTINUATION, SMOOTH q_N = 4.2e-25.
LEG C: zones med H/B/T = 0.366/0.604/0.035, median p_0 0.366
in [0.25, 0.55] range [0.278, 0.523] (r246 reproduced); rho_0
== b1^2/h_0 worst rel 6.7e-16 (the head mode IS the raw mass
pairing (border mass)^2/(window mass) -- source-pure WHY of
the one-mode head); rho_0 ladder spread 0.18 decades; tail
law: EXP/POW/IRREGULAR = 0/2/40 of 42 (w9: EXP rms 1.25 vs POW
rms 1.11, min rho 8.9e-10 at n = 180 = 0.978 N, terminal
rebound +8.2 dec; w13: min rho 1.6e-08 at n = 26 = 0.155 N,
rebound +7.4 dec) => majority IRREGULAR, no clean decay law;
MAJORANTS: ward m_n >= rho_n holds at every degree on 42/42
(worst phat-vs-chain rho rel 4.0e-8); coverage M1_SUP 0/42
(overshoot med x1.5e+11), M2_CS 0/42 (x7.3e+05), M3_ABS 0/42
(x4.9e+02) => MAJORANT_OPEN(best M3_ABS, median overshoot
x4.9e+02, break locus argmax at 0.97 N median) -- the sealed
mass bounds break in the NEAR-TERMINAL zone where h_n
collapses: no |sigma|-mass bound can see the F^2/h
cancellation (consistent with the b2 covariation finding; the
budget proof needs a ratio object, not a mass object).  LEG
C4: w9 prior re-gate hit (Dbo* -0.175897, Gap* -0.216051,
ratio 0.8141, rel <= 2e-3); 10-rung ladder (n* = 9..21, 0
NULL, embeddings all gated): sign(Dbo*) == sign(Gap*) on 10/10
(SCRAMBLE's border carries MORE prefix mass than MAIN's on
EVERY rung -- the sign is universal), but |Dbo*|/|Gap*| =
0.006..4.11 with only 3/10 in [0.3, 3.0] =>
PREFIX_DOMINANCE_ARTIFACT(sign 10/10 stable, ratio n*-
artifact): the r256 '81 percent' magnitude was a w9/n* = 21
coincidence, the SIGN of the border excess is the stable
object (candidate for a future contract, typed, not
upgraded).  LEG D: d1 shifted telescope breaks by 6.5e+8 x
honest; d2 swapped F/h (6.534 vs 0.153) breaks by 3.6e+9 x;
d3 wrong t* normalization misses the machine root by 3.2e+9
x; d4 SMOOTH alias 7.6e-23 (bar 1e-18), q_N = 4.2e-25 <=
1e-20, D_N == 5/7 rel 1.1e-11.  READING (typed, no upgrade):
the budget question IS the single terminal inequality --
exactly, by construction of B, with the Schur telescope
machine-exact and mp-warded; its coordinate q_N is a
t*-coordinate in the same exact normal form as r238 (two
instances, different terminal data, statistically unrelated);
on the measured surface q < 1 with a FLAT N-trend and a
rank-perfect F^2-vs-h covariation whose residual no sealed
mass majorant can bound; the r256 border dominance survives
only as a universal SIGN.  Runtime 8.5 s full / 0.1 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE:
NONE (a1 predates the record run, disclosed above).

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import coupledtau_probe as CT                # noqa: E402 r257
import offdiag_gram_probe as OG              # noqa: E402 r254
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
MAIN_TELE = (9, 12, 13, 26)
LADDER_SAMPLE_IDX = (0, 5, 10, 15, 20, 25, 30, 35, 41)
DEEP_N = 400
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
FIB_LO = 8
B57 = 5.0 / 7.0
DIRECT_BAR_MAIN = 1e-8
DIRECT_BAR_DEEP = 3e-6
DIRECT_BAR_CTRL = 1e-3
LIN_BAR = 1e-9
SLOPE_BAR_MAIN = 1e-8
SLOPE_BAR_DEEP = 3e-6
ROOT_BAR_MAIN = 1e-8
ROOT_BAR_DEEP = 3e-6
MP_TRUNCS_W9 = (12, 24)
MP_TRUNC_DEEP = 12
MP_TRUNC_DPS = 220
MP_TRUNC_BAR = 1e-12
FLOOR_BAND = (1.40, 1.46)
NONSAT_MARGIN = 0.01
SAT_PROBE = 1e-6
MARGIN_BAND = (0.010, 0.020)
SPEAR_BAR = 0.5
COVAR_BAR = 0.7
DRIVER_DELTA = 0.2
R238_CROSS = 29
R238_LT1 = 18
HEAD_K = 8
TAIL_K = 5
P0_BAND = (0.25, 0.55)
RHO0_ID_BAR = 1e-12
PHAT_RHO_BAR = 1e-6
MAJ_WARD_TOL = 1e-6
TAIL_RMS_RATIO = 0.8
C4_LADDER = (17, 10, 18, 12, 13, 9, 15, 19, 26, 40)
C4_PRIOR = {"Dbo": -0.175897, "Gap": -0.216051}
C4_PRIOR_TOL = 2e-3
LB_LO, LB_HI = 0.3, 3.0
STAB_FRAC = 0.8
GAP_NULL = 1e-9
SM_ALIAS_BAR = 1e-18
SM_Q_BAR = 1e-20
SM_DN_BAR = 1e-9
LOUD = 1e3
CAL_VERDICT = (
    "TELESCOPE_EXACT(BY_CONSTRUCTION; 5/7 = r241 IMPORTED floor, "
    "source derivation OPEN) + TERMINAL_Q_LAW(FLAT, "
    "COVARIANT_RATIO(residual BALANCED)) + TSTAR_IDENTIFIED(one "
    "normal form, two data instances) + MAJORANT_OPEN(M3_ABS, "
    "overshoot x4.9e+02 med, locus 0.97 N) + "
    "PREFIX_DOMINANCE_ARTIFACT(sign 10/10, ratio 0.006..4.11)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []
LN10 = math.log(10.0)


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
                       "the r244 chain; ground truth (flips) enters "
                       "gates only" if not bad else "; ".join(bad))


# ------------------------------------------------ direct route
def direct_DN(p, t_corners):
    """full-depth bordered slogdet route (r257 basis: scaled
    Chebyshev-U on the union+border hull) with the corner along
    the sealed ray B(t) = S_{N-2} + t (5/7); returns D_N(t) list."""
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
    sg, lg = np.linalg.slogdet(G)
    out = []
    for t in t_corners:
        B = float(p["S"][N - 2]) + t * B57
        A = np.zeros((N + 1, N + 1))
        A[:N, :N] = G
        A[:N, N] = tv
        A[N, :N] = tv
        A[N, N] = B
        sa, la = np.linalg.slogdet(A)
        out.append(sa * sg * math.exp(la - lg))
    return out


def terminal_logs(p):
    """(2 log10 |F_{N-1}|, log10 h_{N-1}, q_N) from the chain."""
    N = p["N"]
    r = p["rows"][N - 1]
    lF2 = 2.0 * (math.log10(max(abs(r["fb"]), 1e-300))
                 + r["Ls"] / LN10)
    lh = r["lg_h"] / LN10
    return lF2, lh, float(p["rho"][N - 1]) / B57


def tstar_r238(p):
    """the r238 coordinate with the sealed m_free convention
    gammahat_{N,free} = gammahat_{N-1}; returns (t*, crossing)."""
    N = p["N"]
    gN = p["rows"][N - 1]["gam_next"]
    gb = p["rows"][N - 2]["gam_next"]
    if gN >= gb:
        return float("inf"), False
    return gb / (gb - gN), True


def pmax_of(p):
    """maximal positive prefix degree (r256 leg-0 coordinate)."""
    for k in range(FIB_LO, p["N"]):
        if p["rows"][k]["sg_h"] < 0.0:
            return k
    return p["N"]


def wfields(p):
    d, dsm = p["d"], p["dsm"]
    return dict(
        bx=np.concatenate([dsm["xs"], dsm["ys"]]),
        bw=np.concatenate([dsm["ws"], -dsm["vs"]]),
        wx=np.concatenate([d["xs"], d["ys"]]),
        wu=np.concatenate([d["ws"], -d["vs"]]),
        c0=p["Fv"][0] / p["hv"][0],
        sg=np.array([r["sg_h"] for r in p["rows"]]), p=p)


def c4_raster(pM, pC):
    """MAIN x SCRAMBLE cleaned raster at the pair's own common
    positive prefix (r256 algebra via the separable cell route
    T = sum_k sg_k (phat_k . s)^2); returns the effect dict."""
    WM, WC = wfields(pM), wfields(pC)
    ns = min(pmax_of(pM), pmax_of(pC))
    U = np.unique(np.concatenate([WM["wx"], WC["wx"]]))
    im = np.searchsorted(U, WM["wx"])
    ic = np.searchsorted(U, WC["wx"])
    ok_pos = (np.array_equal(WM["bx"], WC["bx"])
              and bool(np.all(U[im] == WM["wx"]))
              and bool(np.all(U[ic] == WC["wx"])))
    posU = np.concatenate([WM["bx"], U])
    nb = len(WM["bx"])

    def s_emb(W, idx):
        sv = np.zeros(len(posU))
        sv[:nb] = W["bw"]
        np.add.at(sv, nb + idx, -W["c0"] * W["wu"])
        return sv

    sM, sC = s_emb(WM, im), s_emb(WC, ic)
    if ns <= FIB_LO:
        return dict(ok_pos=ok_pos, nstar=ns, null=True)
    PM = OG.phat_matrix(pM["rows"], posU, ns)
    PC = OG.phat_matrix(pC["rows"], posU, ns)

    def cell(P, sg, s):
        v = P[FIB_LO:] @ s
        return float(np.sum(sg[FIB_LO:len(P)] * v * v))

    MM = cell(PM, WM["sg"], sM)
    MC = cell(PM, WM["sg"], sC)
    CC = cell(PC, WC["sg"], sC)
    vg = np.abs(PM[FIB_LO:]) @ np.abs(sM)
    gross = float(np.sum(vg * vg))
    Dbo, Gap = MM - MC, MM - CC
    return dict(ok_pos=ok_pos, nstar=ns, null=abs(Gap)
                <= GAP_NULL * max(gross, 1e-300),
                Dbo=Dbo, Gap=Gap, gross=gross,
                ratio=abs(Dbo) / max(abs(Gap), 1e-300),
                sgn_ok=(Dbo * Gap > 0.0))


def tail_fit(rho, N):
    """sealed bulk-window fits: EXP log10 rho ~ a + b n vs POWER
    log10 rho ~ a + b log10 n on n in [HEAD_K, N-TAIL_K-1]."""
    nn = np.arange(HEAD_K, N - TAIL_K)
    y = np.log10(np.maximum(np.abs(rho[HEAD_K:N - TAIL_K]), 1e-300))
    ce = np.polyfit(nn, y, 1)
    rmse = float(np.sqrt(np.mean((np.polyval(ce, nn) - y) ** 2)))
    lx = np.log10(nn)
    cp = np.polyfit(lx, y, 1)
    rmsp = float(np.sqrt(np.mean((np.polyval(cp, lx) - y) ** 2)))
    if rmse <= TAIL_RMS_RATIO * rmsp:
        tok = "EXP"
    elif rmsp <= TAIL_RMS_RATIO * rmse:
        tok = "POW"
    else:
        tok = "IRREGULAR"
    return tok, float(ce[0]), rmse, float(cp[0]), rmsp


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("budget_anatomy_probe -- PRIME.PORT.RHP.BUDGET."
          "ANATOMY.01 (round 258)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + w9 controls only; ladder legs, "
                        "mp wards, r238 census skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN OBJECT: the terminal reduction of the r257 drain -- "
          "B_w = S_{N-2} + 5/7 (IMPORTED, by construction) makes "
          "D_N = 5/7 - rho_{N-1} an algebraic identity; gates: "
          "direct bordered slogdet on the 12-window sample + mp "
          "truncation wards dps %d; q_N = rho_{N-1}/(5/7) census + "
          "driver decomposition on the 42-rung ladder; corner ray "
          "B(t) = S_{N-2} + t(5/7) as the sealed t* normal form; "
          "majorant candidates M1_SUP/M2_CS/M3_ABS sealed; c4 "
          "dominance ladder %s with per-pair prefix depth; ALL "
          "bars, bands, rules and verdicts sealed in the frozen "
          "spec BEFORE the record run (two pre-spec scratch "
          "calibrations disclosed)"
          % (MP_TRUNC_DPS, str(C4_LADDER)))

    # ---------------- S1: census
    section("S1  CENSUS + CONTROLS + POSITIVITY TYPING")
    if smoke:
        packs = [BH.wpack(9)]
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        packs = [BH.wpack(kz) for kz in kzs]
        packs.sort(key=lambda p: (p["N"], p["kz"]))
    by_kz = {p["kz"]: p for p in packs}
    okC = all(p["nf"] is None for p in packs)
    check("G10-census-ladder", okC,
          "%d rungs, N in [%d, %d]: free prefix positive at full "
          "depth on ALL (typed POSITIVE_PREFIX)%s"
          % (len(packs), packs[0]["N"], packs[-1]["N"],
             " (smoke: w9 only)" if smoke else ""))
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
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    check("G11-census-controls", okCf,
          "w9 control flips re-derived %s (typed INDEFINITE_"
          "CONTINUATION beyond pmax, r256 firewall adopted)"
          % str({c: ctrl[c]["nf"] for c in ctrl}))

    # sample for the telescope/ray gates
    if smoke:
        sample = [by_kz[9]]
    else:
        skz = list(MAIN_TELE) + [packs[i]["kz"]
                                 for i in LADDER_SAMPLE_IDX]
        seen: list = []
        sample = []
        for kz in skz:
            if kz not in seen:
                seen.append(kz)
                sample.append(by_kz[kz])

    # ---------------- S2: LEG A -- the exact telescope identity
    section("S2  LEG A -- THE EXACT TELESCOPE IDENTITY")
    dev_main = dev_deep = 0.0
    sgn_ok = True
    ray = {}
    devs, Ns_s = [], []
    a_note = []
    for p in sample:
        D0, Dh, D1 = direct_DN(p, (0.0, 0.5, 1.0))
        ray[p["kz"]] = (D0, Dh, D1)
        ref = B57 - float(p["rho"][p["N"] - 1])
        dv = abs(D1 / ref - 1.0)
        sgn_ok = sgn_ok and (math.copysign(1.0, D1)
                             == math.copysign(1.0, ref)) \
            and (ref > 0.0)
        if p["N"] <= DEEP_N:
            dev_main = max(dev_main, dv)
        else:
            dev_deep = max(dev_deep, dv)
        devs.append(max(dv, 1e-16))
        Ns_s.append(p["N"])
        a_note.append("kz%d(N=%d) %.1e" % (p["kz"], p["N"], dv))
    err_slope = (float(np.polyfit(np.log10(Ns_s),
                                  np.log10(devs), 1)[0])
                 if len(devs) >= 3 else float("nan"))
    check("G20-telescope-direct",
          dev_main <= DIRECT_BAR_MAIN and dev_deep <= DIRECT_BAR_DEEP
          and sgn_ok,
          "direct bordered slogdet D_N == 5/7 - rho_{N-1} on the "
          "%d-window sample: %s -- worst rel %.1e (N <= %d, bar "
          "%.0e) / %.1e (deep, bar %.0e), all signs positive and "
          "exact; f64 route error law slope %+.2f dec/dec vs N "
          "(CONDITIONING of the route, disclosed -- the identity "
          "is BY CONSTRUCTION, exactness carried by the mp wards)"
          % (len(sample), "; ".join(a_note), dev_main, DEEP_N,
             DIRECT_BAR_MAIN, dev_deep, DIRECT_BAR_DEEP, err_slope))
    if not smoke:
        tr_note = []
        tr_w = 0.0
        for n_t in MP_TRUNCS_W9:
            dv = CT.mp_trunc_ward(by_kz[9], n_t, MP_TRUNC_DPS, B57)
            tr_w = max(tr_w, dv)
            tr_note.append("w9 n_t=%d %.1e" % (n_t, dv))
        dv = CT.mp_trunc_ward(packs[-1], MP_TRUNC_DEEP,
                              MP_TRUNC_DPS, B57)
        tr_w = max(tr_w, dv)
        tr_note.append("kz%d(N=%d) n_t=%d %.1e"
                       % (packs[-1]["kz"], packs[-1]["N"],
                          MP_TRUNC_DEEP, dv))
        check("G21-mp-truncation-wards", tr_w <= MP_TRUNC_BAR,
              "monomial mp Hankel truncations (dps %d, corner "
              "5/7): %s (bar %.0e) -- the Schur telescope D_n = "
              "B_t - S_{n-1} is exact in exact arithmetic"
              % (MP_TRUNC_DPS, "; ".join(tr_note), MP_TRUNC_BAR))
    else:
        check("G21-mp-truncation-wards", True, "SMOKE: skipped")
    # (a3) margin equivalence incl. controls (algebraic side)
    eq_ok = True
    c_note = []
    for c in ctrl:
        Dc = direct_DN(ctrl[c], (1.0,))[0]
        refc = B57 - float(ctrl[c]["rho"][ctrl[c]["N"] - 1])
        dvc = abs(Dc / refc - 1.0)
        eq_ok = eq_ok and dvc <= DIRECT_BAR_CTRL \
            and (math.copysign(1.0, Dc) == math.copysign(1.0, refc))
        c_note.append("%s D_N %+.4f rel %.1e" % (c, Dc, dvc))
    check("G22-margin-equivalence", sgn_ok and eq_ok,
          "sign(D_N) == sign(5/7 - rho_{N-1}) on the full sample "
          "(MAIN: both sides positive) AND on the w9 controls "
          "(%s -- there ALGEBRAIC tau-quotient statements, typed "
          "INDEFINITE_CONTINUATION, ctrl bar %.0e): margin > 0 "
          "<=> rho_{N-1} < 5/7 EXACTLY"
          % ("; ".join(c_note), DIRECT_BAR_CTRL))
    # (a2) 5/7 provenance
    ratios = [1.0 / (B57 * terminal_logs(p)[2]) for p in packs]
    rmin = min(ratios)
    ok_fl = (FLOOR_BAND[0] <= rmin <= FLOOR_BAND[1]
             and rmin >= 1.4 + NONSAT_MARGIN) or smoke
    saturated = abs(rmin - 1.4) <= SAT_PROBE
    check("G23-five-sevenths-provenance", ok_fl and not saturated,
          "min_w h_{N-1}/F_{N-1}^2 = %.4f in [%.2f, %.2f], >= 7/5 "
          "with non-saturation margin %.4f >= %.2f: the constant "
          "does NOT saturate (probe %.0e) and has no source-pure "
          "compile path in the import chain (r243 <- r241 floor "
          "literals only) => Q7_SHARE and LEVEL8_SUBTRACTION "
          "NOT_SUPPORTED; 5/7 stays FLOOR_IMPORTED(r241), source "
          "derivation OPEN%s"
          % (rmin, FLOOR_BAND[0], FLOOR_BAND[1], rmin - 1.4,
             NONSAT_MARGIN, SAT_PROBE,
             " (smoke: w9 only, band not binding)" if smoke else ""))
    vA = ("TELESCOPE_EXACT(BY_CONSTRUCTION; 5/7 = r241 IMPORTED "
          "floor, source derivation OPEN)"
          if (dev_main <= DIRECT_BAR_MAIN
              and dev_deep <= DIRECT_BAR_DEEP and sgn_ok and eq_ok)
          else "TELESCOPE_APPROX(err main %.1e deep %.1e)"
          % (dev_main, dev_deep))

    # ---------------- S3: LEG B -- the terminal inequality
    section("S3  LEG B -- THE TERMINAL INEQUALITY q_N OVER THE "
            "LADDER")
    lF2s, lhs, qs = [], [], []
    for p in packs:
        lF2, lh, q = terminal_logs(p)
        lF2s.append(lF2)
        lhs.append(lh)
        qs.append(q)
    qmax, qmed, qmin = (max(qs), float(np.median(qs)), min(qs))
    marg_min = B57 * (1.0 - qmax)
    ok_q = all(q < 1.0 for q in qs) and \
        (smoke or MARGIN_BAND[0] <= marg_min <= MARGIN_BAND[1])
    check("G30-q-census", ok_q,
          "q_N = rho_{N-1}/(5/7) < 1 on %d/%d rungs; min/med/max "
          "= %.4f/%.4f/%.4f; min terminal margin 5/7 - rho_{N-1} "
          "= %.4f (band [%.3f, %.3f], the r243 razor reproduced)%s"
          % (len(qs), len(qs), qmin, qmed, qmax, marg_min,
             MARGIN_BAND[0], MARGIN_BAND[1],
             " (smoke: band not binding)" if smoke else ""))
    if not smoke:
        Ns = [p["N"] for p in packs]
        gaps = [1.0 - q for q in qs]
        g_slope = float(np.polyfit(np.log10(Ns),
                                   np.log10(gaps), 1)[0])
        g_sp = CT.spearman(Ns, gaps)
        trend = ("APPROACHING" if g_sp <= -SPEAR_BAR else
                 ("RECEDING" if g_sp >= SPEAR_BAR else "FLAT"))
        check("G31-q-trend", True,
              "wall margin gap = 1 - q_N vs N: LS slope %+.2f "
              "dec/dec, Spearman %+.3f (sealed bar %.1f) => "
              "TREND %s -- the terminal margin does NOT shrink "
              "with N on this surface (measurement)"
              % (g_slope, g_sp, SPEAR_BAR, trend))
        lgq = [math.log10(q) for q in qs]
        sp_F = CT.spearman(lgq, lF2s)
        sp_h = CT.spearman(lgq, lhs)
        sp_x = CT.spearman(lF2s, lhs)
        if sp_x >= COVAR_BAR:
            if abs(sp_F) >= abs(sp_h) + DRIVER_DELTA:
                res = "residual F"
            elif abs(sp_h) >= abs(sp_F) + DRIVER_DELTA:
                res = "residual H"
            else:
                res = "residual BALANCED"
            driver = "COVARIANT_RATIO(%s)" % res
        elif abs(sp_F) >= abs(sp_h) + DRIVER_DELTA:
            driver = "F_DRIVEN"
        elif abs(sp_h) >= abs(sp_F) + DRIVER_DELTA:
            driver = "H_DRIVEN"
        else:
            driver = "BALANCED"
        check("G32-driver-decomposition", True,
              "log10 q = 2 log10|F_{N-1}| - log10 h_{N-1} - "
              "log10(5/7): Spearman(2lgF, lgh) = %+.3f (covariance "
              "bar %.1f) -- the two terminal components track each "
              "other; residual correlations Spearman(lgq, 2lgF) "
              "%+.3f vs (lgq, lgh) %+.3f (delta %.1f) => DRIVER "
              "%s: q is the residual of the F^2-vs-h covariation, "
              "any terminal proof must bound the RATIO, not "
              "either side" % (sp_x, COVAR_BAR, sp_F, sp_h,
                               DRIVER_DELTA, driver))
    else:
        trend, driver = "SMOKE_NA", "SMOKE_NA"
        check("G31-q-trend", True, "SMOKE: skipped")
        check("G32-driver-decomposition", True, "SMOKE: skipped")
    # (b3-i) the corner ray = the t* normal form
    lin_w = 0.0
    slope_main = slope_deep = 0.0
    root_main = root_deep = 0.0
    for p in sample:
        D0, Dh, D1 = ray[p["kz"]]
        lin_w = max(lin_w, abs(Dh - 0.5 * (D0 + D1))
                    / max(abs(D1), 1e-300))
        slope = D1 - D0
        troot = -D0 / slope
        q = float(p["rho"][p["N"] - 1]) / B57
        dq = abs(troot - q)
        ds = abs(slope / B57 - 1.0)
        if p["N"] <= DEEP_N:
            root_main = max(root_main, dq)
            slope_main = max(slope_main, ds)
        else:
            root_deep = max(root_deep, dq)
            slope_deep = max(slope_deep, ds)
    check("G33-tstar-corner-ray",
          lin_w <= LIN_BAR and slope_main <= SLOPE_BAR_MAIN
          and slope_deep <= SLOPE_BAR_DEEP
          and root_main <= ROOT_BAR_MAIN
          and root_deep <= ROOT_BAR_DEEP,
          "corner ray B(t) = S_{N-2} + t(5/7): D_N(t) AFFINE "
          "(collinearity worst %.1e, bar %.0e), slope == 5/7 "
          "(rel %.1e main / %.1e deep, bars %.0e/%.0e, amendment "
          "a1), machine root == q_N (worst %.1e main / %.1e "
          "deep, bars %.0e/%.0e) on %d/%d windows: the terminal "
          "budget question IS a t*-coordinate in the sealed r238 "
          "normal form (pivot affine slope-1 in its one forced "
          "parameter, coordinate = ray crossing, wall = q_N < 1)"
          % (lin_w, LIN_BAR, slope_main, slope_deep,
             SLOPE_BAR_MAIN, SLOPE_BAR_DEEP, root_main, root_deep,
             ROOT_BAR_MAIN, ROOT_BAR_DEEP, len(sample),
             len(sample)))
    if not smoke:
        n_cross = n_lt1 = 0
        tq, tt_ = [], []
        for p, q in zip(packs, qs):
            ts, crossing = tstar_r238(p)
            if crossing:
                n_cross += 1
                tq.append(q)
                tt_.append(ts)
                if ts < 1.0:
                    n_lt1 += 1
        sp_qt = CT.spearman(tq, tt_) if len(tq) >= 3 else float("nan")
        ok_cens = (n_cross == R238_CROSS and n_lt1 == R238_LT1)
        check("G34-tstar-r238-census", ok_cens,
              "r238 instance re-derived on all 42 (m_free "
              "convention gammahat_{N,free} = gammahat_{N-1}): %d "
              "down-crossing (prior %d), %d below 1 (prior %d, = "
              "the delta = 0 set); Spearman(q_N, t*_r238) on the "
              "crossing windows = %+.3f -- SAME sealed normal "
              "form, DIFFERENT terminal data (m_{2N} vs F_{N-1}); "
              "the predicates differ on exactly the t* < 1 "
              "windows where q_N < 1 throughout: one COORDINATE, "
              "two instances, never claimed numerically equal"
              % (n_cross, R238_CROSS, n_lt1, R238_LT1, sp_qt))
        vT = ("TSTAR_IDENTIFIED(one normal form, two data "
              "instances)"
              if (ok_cens and lin_w <= LIN_BAR
                  and slope_main <= SLOPE_BAR_MAIN
                  and slope_deep <= SLOPE_BAR_DEEP
                  and root_main <= ROOT_BAR_MAIN
                  and root_deep <= ROOT_BAR_DEEP)
              else "TSTAR_OPEN")
    else:
        check("G34-tstar-r238-census", True, "SMOKE: skipped")
        vT = "TSTAR_SMOKE_NA"
    w_note = []
    for c in ctrl:
        pc = ctrl[c]
        pm = pmax_of(pc)
        q_pre = float(pc["rho"][pm - 1]) / B57
        q_full = float(pc["rho"][pc["N"] - 1]) / B57
        w_note.append("%s q_pre@%d %.1e / q_full %+.2f [INDEF]"
                      % (c, pm, q_pre, q_full))
    check("G35-world-q", True,
          "controls before their base flip: %s -- the pre-flip "
          "terminal increments are STRUCTURALLY TINY (the quiet "
          "zone, r246), the control q-question only becomes "
          "nontrivial in the indefinite continuation where it is "
          "algebraic (typed, not a Hilbert-space statement); the "
          "controls are discriminated by the WALL, not by q"
          % "; ".join(w_note))

    # ---------------- S4: LEG C -- drain profile anatomy
    section("S4  LEG C -- DRAIN PROFILE ANATOMY")
    p0s, sh_h, sh_b, sh_t, r0dev, r0log = [], [], [], [], [], []
    for p in packs:
        N = p["N"]
        S = p["S"]
        St = float(S[N - 1])
        zh = float(S[HEAD_K - 1]) / St
        zt = (St - float(S[N - TAIL_K - 1])) / St
        sh_h.append(zh)
        sh_b.append(1.0 - zh - zt)
        sh_t.append(zt)
        p0s.append(float(p["rho"][0]) / St)
        r0 = float(p["rho"][0])
        r0dev.append(abs(r0 / (p["b1"] ** 2 / p["hv"][0]) - 1.0))
        r0log.append(math.log10(r0))
    p0_med = float(np.median(p0s))
    ok_z = max(r0dev) <= RHO0_ID_BAR and \
        (smoke or P0_BAND[0] <= p0_med <= P0_BAND[1])
    check("G40-zone-profile", ok_z,
          "zones (HEAD < %d / BULK / TAIL last %d) medians H/B/T "
          "= %.3f/%.3f/%.3f; median p_0 = %.3f in [%.2f, %.2f] "
          "range [%.3f, %.3f] (r246 one-mode head reproduced); "
          "SOURCE-PURE WHY: rho_0 == b1^2/h_0 EXACTLY (worst rel "
          "%.1e, bar %.0e) -- the head mode is the raw mass "
          "pairing (border mass)^2/(window mass), no orthogonal-"
          "polynomial oscillation enters; rho_0 ladder spread "
          "%.2f decades%s"
          % (HEAD_K, TAIL_K, float(np.median(sh_h)),
             float(np.median(sh_b)), float(np.median(sh_t)),
             p0_med, P0_BAND[0], P0_BAND[1], min(p0s), max(p0s),
             max(r0dev), RHO0_ID_BAR, max(r0log) - min(r0log),
             " (smoke: band not binding)" if smoke else ""))
    toks = {"EXP": 0, "POW": 0, "IRREGULAR": 0}
    det_note = []
    for p in packs:
        tok, se, re_, sp_, rp = tail_fit(np.asarray(p["rho"],
                                                    float), p["N"])
        toks[tok] += 1
        if p["kz"] in (9, 13):
            rho = np.asarray(p["rho"][:p["N"]], float)
            i0 = int(np.argmin(np.abs(rho[HEAD_K:p["N"]]))) + HEAD_K
            det_note.append(
                "w%d %s (EXP slope %+.4f rms %.2f | POW slope "
                "%+.2f rms %.2f; min rho %.1e at n=%d = %.3f N, "
                "terminal rebound %+.1f dec)"
                % (p["kz"], tok, se, re_, sp_, rp,
                   float(np.abs(rho[i0])), i0, i0 / p["N"],
                   math.log10(float(rho[p["N"] - 1])
                              / float(np.abs(rho[i0])))))
    tmaj = max(toks, key=lambda k: toks[k])
    check("G41-tail-law", True,
          "sealed bulk-window fits (n in [%d, N-%d), winner needs "
          "rms <= %.1f x other): EXP/POW/IRREGULAR = %d/%d/%d of "
          "%d => majority %s; %s -- NO clean decay law: the drain "
          "profile is head-loaded + irregular bulk (r244/r246 "
          "consistent), the near-terminal zone collapses and "
          "rebounds at the razor (measurement)"
          % (HEAD_K, TAIL_K + 1, TAIL_RMS_RATIO, toks["EXP"],
             toks["POW"], toks["IRREGULAR"], len(packs), tmaj,
             "; ".join(det_note)))
    # (c3) majorants
    ward_ok = True
    phat_dev = 0.0
    cov = {"M1_SUP": 0, "M2_CS": 0, "M3_ABS": 0}
    ovs = {k: [] for k in cov}
    loci = []
    for p in packs:
        N = p["N"]
        bxa = np.concatenate([p["dsm"]["xs"], p["dsm"]["ys"]])
        bwa = np.concatenate([p["dsm"]["ws"], -p["dsm"]["vs"]])
        aw = np.abs(bwa)
        tv = float(np.sum(aw))
        Pb = OG.phat_matrix(p["rows"], bxa, N)
        Fhat = Pb @ bwa
        rho_pf = Fhat * Fhat
        rr = np.asarray(p["rho"][:N], float)
        phat_dev = max(phat_dev,
                       float(np.max(np.abs(
                           rho_pf[HEAD_K:N - 1]
                           / rr[HEAD_K:N - 1] - 1.0))))
        m1 = tv * tv * np.max(Pb * Pb, axis=1)
        m2 = tv * ((Pb * Pb) @ aw)
        m3 = (np.abs(Pb) @ aw) ** 2
        budget = (float(p["S"][N - 2]) - float(p["S"][HEAD_K - 1])
                  + B57)
        for nm, m in (("M1_SUP", m1), ("M2_CS", m2),
                      ("M3_ABS", m3)):
            ward_ok = ward_ok and bool(np.all(
                m[HEAD_K:N - 1] >= rr[HEAD_K:N - 1]
                * (1.0 - MAJ_WARD_TOL)))
            sm = float(np.sum(m[HEAD_K:N - 1]))
            if sm <= budget:
                cov[nm] += 1
            ovs[nm].append(sm / budget)
        loci.append((int(np.argmax(m3[HEAD_K:N - 1])) + HEAD_K)
                    / N)
    check("G42-majorant-ward", ward_ok and phat_dev <= PHAT_RHO_BAR,
          "all three sealed candidates are TRUE pointwise bounds "
          "m_n >= rho_n at every degree n in [%d, N-2] on %d/%d "
          "rungs (tol %.0e); phat-route rho vs chain rho worst "
          "rel %.1e (bar %.0e)"
          % (HEAD_K, len(packs), len(packs), MAJ_WARD_TOL,
             phat_dev, PHAT_RHO_BAR))
    best = max(cov, key=lambda k: (cov[k], -float(np.median(ovs[k]))))
    found = cov[best] == len(packs) and not smoke
    ov_med = {k: float(np.median(ovs[k])) for k in ovs}
    vM = ("MAJORANT_FOUND(%s)" % best if found
          else "MAJORANT_OPEN(%s, overshoot x%.1e med, locus "
          "%.2f N)" % (best, ov_med[best],
                       float(np.median(loci))))
    check("G43-majorant-budget", True,
          "budget test sum_{n=8}^{N-2} m_n <= (S_{N-2} - S_7) + "
          "5/7 (head as prefix data): coverage M1_SUP %d/%d "
          "(overshoot med x%.1e) / M2_CS %d/%d (x%.1e) / M3_ABS "
          "%d/%d (x%.1e); break locus argmax_n m_n at median "
          "%.2f N => %s -- the sealed |sigma|-mass bounds break "
          "in the NEAR-TERMINAL zone where h_n collapses: no "
          "mass bound sees the F^2/h cancellation (consistent "
          "with the G32 covariation finding: the budget proof "
          "needs a RATIO object); controls excluded (algebraic "
          "beyond their flip, r246 typing)"
          % (cov["M1_SUP"], len(packs), ov_med["M1_SUP"],
             cov["M2_CS"], len(packs), ov_med["M2_CS"],
             cov["M3_ABS"], len(packs), ov_med["M3_ABS"],
             float(np.median(loci)), vM))

    # ---------------- S5: LEG C4 -- prefix-border dominance
    section("S5  LEG C4 -- PREFIX-BORDER DOMINANCE OVER THE "
            "LADDER")
    e9 = c4_raster(by_kz[9] if 9 in by_kz else BH.wpack(9),
                   ctrl["SCRAMBLE"])
    ok_prior = (e9["ok_pos"] and not e9["null"]
                and abs(e9["Dbo"] / C4_PRIOR["Dbo"] - 1.0)
                <= C4_PRIOR_TOL
                and abs(e9["Gap"] / C4_PRIOR["Gap"] - 1.0)
                <= C4_PRIOR_TOL)
    check("G50-prefix-prior-regate", ok_prior,
          "w9 x SCRAMBLE cleaned raster at n* = %d (separable "
          "cell route, r256 algebra): Dbo* %+.6f (prior %+.6f), "
          "Gap* %+.6f (prior %+.6f), ratio %.4f (r256: 0.814), "
          "rel tol %.0e; r254-a1 sorted-union embedding re-gated"
          % (e9["nstar"], e9["Dbo"], C4_PRIOR["Dbo"], e9["Gap"],
             C4_PRIOR["Gap"], e9["ratio"], C4_PRIOR_TOL))
    if not smoke:
        rows_c4 = []
        for kz in C4_LADDER:
            pM = by_kz[kz] if kz in by_kz else BH.wpack(kz)
            pC = ctrl["SCRAMBLE"] if kz == 9 \
                else BH.wpack(kz, base_kw=dict(scramble_seed=1))
            e = c4_raster(pM, pC)
            rows_c4.append((kz, pM["N"], e))
            if e.get("null", True):
                info("kz%-3d N=%-3d n*=%-3d NULL/empty (emb %s)"
                     % (kz, pM["N"], e["nstar"], e["ok_pos"]))
            else:
                info("kz%-3d N=%-3d n*=%-3d Dbo* %+.4e Gap* "
                     "%+.4e ratio %.3f sign %s"
                     % (kz, pM["N"], e["nstar"], e["Dbo"],
                        e["Gap"], e["ratio"],
                        "OK" if e["sgn_ok"] else "FLIP"))
        live = [(kz, N, e) for kz, N, e in rows_c4
                if not e.get("null", True)]
        emb_ok = all(e["ok_pos"] for _, _, e in rows_c4)
        n_sgn = sum(1 for _, _, e in live if e["sgn_ok"])
        n_band = sum(1 for _, _, e in live
                     if e["sgn_ok"] and LB_LO <= e["ratio"] <= LB_HI)
        ratios_ = [e["ratio"] for _, _, e in live]
        stable = (len(live) > 0
                  and n_band >= STAB_FRAC * len(live) and emb_ok)
        vP = ("PREFIX_DOMINANCE_STABLE(median ratio %.2f)"
              % float(np.median(ratios_)) if stable else
              "PREFIX_DOMINANCE_ARTIFACT(sign %d/%d, ratio "
              "%.3f..%.2f)" % (n_sgn, len(live),
                               min(ratios_), max(ratios_)))
        check("G51-prefix-dominance-ladder", emb_ok,
              "10-rung ladder, per-pair prefix depth n* re-derived "
              "(all embeddings gated): sign(Dbo*) == sign(Gap*) "
              "on %d/%d non-null rungs, ratio in [%.1f, %.1f] on "
              "%d/%d (sealed stability fraction %.1f) => %s -- "
              "honest split: the SIGN of the border excess "
              "(SCRAMBLE border carries more prefix mass) is "
              "universal, the r256 magnitude 0.81 is an n* "
              "coincidence" % (n_sgn, len(live), LB_LO, LB_HI,
                               n_band, len(live), STAB_FRAC, vP))
    else:
        vP = "PREFIX_SMOKE_NA"
        check("G51-prefix-dominance-ladder", True, "SMOKE: skipped")

    # ---------------- S6: LEG D -- must-fails + anchors
    section("S6  LEG D -- FALSIFIERS + MUST-FAILS")
    p9 = by_kz[9] if 9 in by_kz else packs[0]
    N9 = p9["N"]
    D1 = ray[9][2] if 9 in ray else direct_DN(p9, (1.0,))[0]
    ref = B57 - float(p9["rho"][N9 - 1])
    honest = abs(D1 / ref - 1.0)
    ref_shift = B57 - float(p9["rho"][N9 - 2])
    dev1 = abs(D1 / ref_shift - 1.0)
    ok_d1 = dev1 >= LOUD * max(honest, 1e-300)
    check("G60-shifted-telescope-mustfail", ok_d1,
          "telescope with shifted index (rho_{N-2} in place of "
          "rho_{N-1}): dev %.1e = %.1e x honest %.1e (bar %.0f x) "
          "-- the terminal reduction consumes the terminal index "
          "exactly" % (dev1, dev1 / max(honest, 1e-300), honest,
                       LOUD))
    r9 = p9["rows"][N9 - 1]
    F2 = (r9["fb"] * math.exp(r9["Ls"])) ** 2
    h9 = r9["sg_h"] * math.exp(r9["lg_h"])
    rho_swap = h9 / F2
    dev2 = abs(D1 / (B57 - rho_swap) - 1.0)
    ok_d2 = dev2 >= LOUD * max(honest, 1e-300)
    check("G61-swapped-Fh-mustfail", ok_d2,
          "terminal increment read as h_{N-1}/F_{N-1}^2 = %.3f "
          "instead of F^2/h = %.3f: anchor dev %.1e = %.1e x "
          "honest (bar %.0f x) -- rho is F^2/h, not its "
          "reciprocal" % (rho_swap, float(p9["rho"][N9 - 1]),
                          dev2, dev2 / max(honest, 1e-300), LOUD))
    D0_, _, D1_ = ray[9] if 9 in ray else direct_DN(p9,
                                                    (0.0, 0.5, 1.0))
    troot = -D0_ / (D1_ - D0_)
    q9 = float(p9["rho"][N9 - 1]) / B57
    t_wrong = float(p9["rho"][N9 - 1]) / (7.0 / 5.0)
    hon_r = max(abs(troot - q9), 1e-12)
    dev3 = abs(t_wrong - troot)
    ok_d3 = dev3 >= LOUD * hon_r
    check("G62-tstar-wrong-normalization-mustfail", ok_d3,
          "t* claimed with the wrong normalization rho/(7/5) = "
          "%.6f vs machine root %.6f: miss %.1e = %.1e x honest "
          "%.1e (bar %.0f x) -- the 5/7 ray normalization is "
          "content, not a label" % (t_wrong, troot, dev3,
                                    dev3 / hon_r, hon_r, LOUD))
    pS = ctrl["SMOOTH"]
    r0S = float(pS["rho"][0])
    r1S = max(abs(float(x)) for x in pS["rho"][1:pS["N"]])
    qS = float(pS["rho"][pS["N"] - 1]) / B57
    DS = direct_DN(pS, (1.0,))[0]
    ok_d4 = (r1S / r0S <= SM_ALIAS_BAR and qS <= SM_Q_BAR
             and abs(DS / B57 - 1.0) <= SM_DN_BAR)
    check("G63-smooth-anchor", ok_d4,
          "SMOOTH self-alias: max|rho_{n>=1}|/rho_0 = %.1e (bar "
          "%.0e), q_N = %.1e (bar %.0e), D_N == 5/7 rel %.1e "
          "(bar %.0e) -- the terminal question trivializes "
          "EXACTLY when the source aliases: q is source-driven"
          % (r1S / r0S, SM_ALIAS_BAR, qS, SM_Q_BAR,
             abs(DS / B57 - 1.0), SM_DN_BAR))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the terminal reduction typed EXACT-BY-"
          "CONSTRUCTION with mp-warded Schur telescope, the 5/7 "
          "provenance audit, the q_N census with the covariation "
          "driver law, the corner-ray t* normal form, the sealed "
          "majorant break anatomy, and the dominance-ladder "
          "adjudication of the r256 side-finding")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        verd = " + ".join([
            vA,
            "TERMINAL_Q_LAW(%s, %s)" % (trend, driver),
            vT, vM, vP])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ-LEVEL (machine-gated): the telescope "
          "collapse and the corner-ray normal form; MEASURED: "
          "q census, trend, covariation, tail law, majorant "
          "break, dominance ladder; OPEN: a source-pure 5/7, any "
          "a-priori terminal bound, the budget bound and the "
          "base law (r243/r246/r247/r256/r257 stand); NO RH claim"
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
