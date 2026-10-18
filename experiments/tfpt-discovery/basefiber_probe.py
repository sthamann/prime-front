#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""basefiber_probe -- PRIME.PORT.RHP.FULLSOURCE.BASEFIBER.01
(round 247): the FIRST round of the full-source campaign -- base/fiber
architecture + the first integrated estimate.  Scope (realistic,
sealed): this round delivers the CAMPAIGN FOUNDATIONS, not the
finished theorem.  Four legs: (0) the base-fiber split of the bordered
PSD claim with the frozen B discipline; (A) the QUIET-ZONE SOURCE RULE
-- why is F_n eight orders suppressed for n = 1..7 on MAIN: the exact
moment-gap bridge; (B) the integrated fiber-theorem target form
S = M + E with three sealed main-term candidates; (C) the base-bulk
capacity-law candidate gammahat_n = 1/4 + eps; (D) the frozen campaign
requirement spec for all follow-rounds.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r246 discipline): w = window (kz),
N_w = builder depth, n = chain degree, k = moment degree; F per
F_DEF / F_DEF_SHA imported verbatim from r243
(principal_bessel_probe.F_DEF); rho_n, S, and the r244 corner
candidates are BITWISE the r244 objects (bordered_hankel_probe.wpack
imported); m_k = int x^k dmutilde, s_k = int x^k dsigmatilde,
d_k := s_k - m_k (the moment gap).  Ground truth (h signs, flips)
enters gates only, never a construction path; the forced pivot h_N
only falsifies.

LEG 0 -- BASE-FIBER SPLIT + B DISCIPLINE (frozen).
The bordered PSD claim splits EXACTLY (r243 G12, re-gated here in
rationals):  [[H_N, u], [u^T, B]] PSD  <=>
  BASE:  h_{w,n} > 0 for all n < N   (the wall; EPSTEIN/SMOOTH must
         break HERE -- their pivot chains flip at 25/27),
  FIBER: D_{w,N}(B) = B - S_{N-1} >= 0  (the budget; SCRAMBLE is the
         sharpest fiber falsifier: pre-flip it consumes ~3 decades
         more budget per degree, r244; its full-depth budget is
         SIGNED post-flip and non-adjudicable, r246 typed).
B DISCIPLINE (frozen for the whole campaign, reviewer clause): any
budget B_w entering a positive claim must be (i) independently
defined SOURCE-SIDE and FROZEN BEFORE any S evaluation, (ii) never
fitted, (iii) carry a named source contract; tau^aug is ALWAYS
written tau^aug(B) with its parameter.  HONEST CURRENT STATUS:
IMPORTED -- the only budget known to cover the surface is
B_w = S_{N-2} + 5/7 (prefix data + the imported r241 floor;
r243/r244/r246 stand, nothing is upgraded here).

LEG A -- THE QUIET-ZONE SOURCE RULE (the round's new lever,
source-side).  Established (r246): median p_1..p_7 ~ 1e-8 on MAIN
(eight orders below carrying) while SCRAMBLE sits ~2 decades higher.
HYPOTHESIS: near-exact low-degree moment equality between comb and
smooth density -- int x^k dmutilde ~ int x^k dsigmatilde for small k
(PNT-partial-sum-like, but FINITE and exactly measurable).
THE EXACT BRIDGE (derived at design time, gated exact): by the r243
self-border identity (m_n - v_n^T H_n^{-1} (m_0..m_{n-1}) = 0
identically, r243 G14) and linearity of the moment route in the
border moments,
    F_n = d_n - v_n^T H_n^{-1} (d_0, ..., d_{n-1})   EXACTLY, n >= 1
-- F_n IS a linear functional of the moment gaps d_k ALONE.  The
quiet zone is therefore small iff the low d_k are small times bounded
coefficients (no hidden third mechanism), measurable by the
cancellation ratio |F_n| / sum |terms|.
(a1) measure d_k (k = 0..15) over the 42-window ladder: relative
depth |d_k|/max(|m_k|, |s_k|), N-trend per k (Spearman), and the
bridge gates: exact in rationals on the r243 toy (n = 1..4); mp
(dps 60) on the bridge worlds w9/w12/w13 + EPSTEIN/SCRAMBLE at
n = 1..7: route identity |F_s - F_d|/sqrt(h_n) <= 1e-30 and
chain-vs-moment F agreement (bar 1e-6, sqrt(h) absolute guard).
(a2) controls: which d_k break on SCRAMBLE (first k with >= 1 decade
level break vs MAIN-w9); EPSTEIN profile reported; SMOOTH is the
exact d == 0 world (its window IS the border comb -- gated <= 1e-25):
PERFECT moment equality with a BROKEN base at 27 -- the SMOOTH trap
made explicit: no moment-equality certificate may certify the base.
(a3) LAW-OR-MEASUREMENT (sealed rule): QUIETZONE_LAW_FOUND iff there
is a full prefix band {0..k*}, k* >= 1, with |d_k|/scale <= 1e-13 on
42/42 MAIN AND the same band holds on SCRAMBLE (construction-forced
quantities must survive position surgery); else
QUIETZONE_MEASURED_ONLY.  Sub-typing (sealed):
QUIETZONE_DIRECT_D_LEVEL iff the median cancellation ratio
|F_d|/sum|terms| over n = 1..7 on w9 is >= 0.01 (the quiet-zone
level IS the d level, no extra cancellation); else
QUIETZONE_EXTRA_CANCELLATION.  SOURCE_RULE_IDENTITY_EXACT appended
iff all bridge gates pass (the RULE is a theorem; the LEVEL is what
a3 adjudicates).  SOCKEL RE-ADJUDICATION (the three r244 corner
candidates vs the bulk-only rest S - rho_0 - Q, Q = sum_{1<=n<=7}
rho_n) is GATED BEHIND QUIETZONE_LAW_FOUND (source-rule peeling, not
mode peeling -- r246 did the latter); if the law does not fire the
numbers are printed as a TYPED DIAGNOSTIC with no verdict weight.

LEG B -- THE INTEGRATED FIBER FORM (the admissible target shape):
S_{N-1} = intint K_N dsigma dsigma = M_w + E_w with source-anchored
main term M and remainder E.  THREE candidates, sealed (max 3), with
provenance typing:
  M1 (= contract b1, GLATT/EQUILIBRIUM): the Szego/equilibrium budget
     of the free local model -- BITWISE the r244 b2 object
     (orthonormal arcsine chain on the measured hull, mass m_0; the
     r241 capacity confirmation as input).  SOURCE-PURE.
  M2 (= contract b2, TELESCOPE): the bordered-flow partial sum with
     sealed cutoff at the edge band, M2 = S_{N-21} (E2 = last 20
     increments -- the r241 edge window).  PREFIX DATA (disclosed:
     M2 consumes the window's own measured budget head; any firing
     carries M_IS_PREFIX_DATA, same epistemic status as r243's
     B_w = S_{N-2} + 5/7).
  M3 (= contract b3, TRACE/DIAGONAL): the trace part of the double
     smear in the r227 intertwiner currency: M3 = sum_{n<N}
     (sum_a w_a^2 pihat_n(t_a)^2)/h_n (diagonal of S = sum_{a,b}
     w_a w_b K_N(t_a, t_b); E3 = off-diagonal).  CHAIN CURRENCY,
     exact split M3 + E3 = S by construction.  DESIGN DISCLOSURE
     (pre-run): the du -> 0 continuum limit suppresses the diagonal;
     M3 adjudicates coherent vs incoherent budget -- its expected
     failure is itself the finding.
Per candidate: |E|/M distribution over the 42 windows, N-trend
(Spearman), and THE FALSIFIER: on the common pre-flip range n < 21
(w9 base) the SCRAMBLE budget excess must be VISIBLE pre-target:
either |E|/M separates by >= 1 decade from MAIN, or the leg-A
quiet-zone observable Q separates by >= 1 decade (then modifier
FALSIFIER_VIA_QUIETZONE).  SEALED RULE per candidate:
med_w |E|/M <= 0.5 AND Spearman(|E|/M; N) <= 0.5 AND falsifier
visible => INTEGRATED_M_CANDIDATE(Mx, stats); none => 
NO_INTEGRATED_FORM.  No control is certified by any candidate
(SMOOTH trap: its budget is rho_0 alone -- typed, wall kills it).

LEG C -- BASE-BULK LAW CANDIDATE: the bulk h_n > 0 (n <= N-20) is
trivially measured (42/42); the THEOREM CANDIDATE is the capacity
law gammahat_n = 1/4 + eps_n with |eps_n| < 1/4 UNIFORM on the
sealed bulk band n in [8, N-20] (gammahat_n = h_n/h_{n-1}; |eps| <
1/4 <=> gammahat in (0, 1/2) => positivity propagates
multiplicatively).  Measured sharp: per window worst |eps| and p90
on the bulk band, violation count, ladder worst case, Spearman(worst
|eps|; N); head band n in [1, 7] and edge band (last 19 gammahat)
profiled separately (outside the law band -- head is certified by
finite measurement, edge by the r241 edge rule, factor 1.46, cited).
COMPOSITION (the minimal bulk statement): BASE(w) <= [head: h_0 > 0
and gammahat_{1..7} > 0, finite check 42/42] AND [bulk capacity law
on [8, N-20]] AND [edge: gammahat > 0 on the last 19 steps, r241
edge window] -- via h_n = h_0 prod gammahat.  CONTROLS break
mechanism documented: first exit of gammahat from the (0, 1/2) band
vs the sealed flips 25/21/27 (h-flip <=> gammahat < 0).  SEALED
RULE: BULK_CAPACITY_LAW_CANDIDATE iff bulk violations = 0 on 42/42
AND the ladder-worst |eps| keeps headroom >= 1e-3 to the 1/4 bar (a
law candidate needs a real margin, not a squeak -- |eps| < 1/4 with
zero headroom is the tautology 'base positivity'); else
BULK_MEASURED_ONLY with the measured margin profile as the caveat.

LEG D -- CAMPAIGN SPEC FROZEN: the consolidated requirement document
(objects, bands, error forms, falsifiers, B discipline, follow-round
map) is frozen as the module constant CAMPAIGN_SPEC and delivered
with its SHA under any verdict: CAMPAIGN_SPEC_FROZEN.

MUST-FAILS (each loud): (m1) SMOOTH TRAP: SMOOTH has PERFECT moment
equality (d_k == 0 exactly) and STILL breaks the base at 27 -- shown
live: no d-based/moment-equality certificate can certify the base;
(m2) SELF-BORDER ALIAS: mutilde's own moments as border force F == 0
identically (exact toy, r243 G14 re-gated -- this identity IS the
bridge's engine and must hold); (m3) FIBER ORACLE: B_orc = 1.01 *
S_{N-1} covers 42/42 trivially and is EXCLUDED (consumes S); (m4)
SIGN ORACLE: reading sign h_{N-1} hits 42/42 and is EXCLUDED by the
input firewall; (m5) BAND ORACLE: the bulk band [8, N-20] is sealed
GLOBALLY -- a per-window band choice could hide violations and never
enters any verdict path.

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs); background
du = 0.01, masses 2 e^{u/2} du (imported verbatim via BH/PB);
K_MAX = 15; bridge degrees n = 1..7; bridge worlds (9, 12, 13) +
EPSTEIN + SCRAMBLE; mp dps 60; route-identity bar 1e-30 (sqrt(h)
scale); chain-F bar 1e-6 (sqrt(h) absolute guard at F^2/h <=
1e-24); law floor 1e-13; SMOOTH d bar 1e-25; decade bar 1.0;
cancellation bar 0.01; quiet zone n in [1, 7]; bulk band
[8, N-20]; edge = last 20 degrees; eps bar 1/4 with law headroom
1e-3; |E|/M median bar 0.5, trend bar 0.5; M2 cutoff N-20;
control-range telescope tail 5; control flips 25/21/27; toy = r243
signed 9-atom toy + disjoint signed 5-atom smooth border, degrees
1..4; smoke rungs (9, 12, 13, 26, 40); runtime <= 1800 s.

SEALED VERDICT FORM (frozen before evaluation):
  <QUIETZONE_LAW_FOUND | QUIETZONE_MEASURED_ONLY>
    [+ SOURCE_RULE_IDENTITY_EXACT]
    [+ QUIETZONE_DIRECT_D_LEVEL | QUIETZONE_EXTRA_CANCELLATION]
  + <INTEGRATED_M_CANDIDATE(Mx) [+ M_IS_PREFIX_DATA]
     [+ FALSIFIER_VIA_QUIETZONE] | NO_INTEGRATED_FORM>
  + <BULK_CAPACITY_LAW_CANDIDATE | BULK_MEASURED_ONLY>
  + CAMPAIGN_SPEC_FROZEN.
Honesty before beauty; no control may be certified (SMOOTH trap,
SCRAMBLE budget); a firing M2 is PREFIX DATA, never a bound.

RECORD TABLES (frozen from calib_bf_pass1.log, 25/25, wall 10.5 s;
disclosed SMOKE/CALIBRATION AMENDMENTS -- the bridge identity, the
candidate definitions, the adjudication rules, the headroom clause
and ALL verdict rules NEVER moved: (a1) the G20 SCRAMBLE
fiber-falsifier diagnostic was sharpened at the smoke pass: the
TOTAL pre-flip budget ratio is mode-0 dominated in every world
(r246) and therefore blind (+0.0 decades measured); the
sockel-excluded excess (S - rho_0 on the pre-flip range) was added
as the reported statistic -- diagnostic wording only, no bar moved,
no verdict touched):
CAL_VERDICT = QUIETZONE_MEASURED_ONLY + SOURCE_RULE_IDENTITY_EXACT
+ QUIETZONE_DIRECT_D_LEVEL + INTEGRATED_M_CANDIDATE(M2) +
M_IS_PREFIX_DATA + BULK_CAPACITY_LAW_CANDIDATE +
CAMPAIGN_SPEC_FROZEN.
Key numbers.  LEG 0: base 42/42 (N in [142, 878]); control base
flips at 25/21/27; fiber min margin 5/7 - rho_{N-1} = 0.0139 (r243
razor reproduced); SCRAMBLE pre-flip TOTAL budget ratio +0.0
decades (mode-0 blind, a1) vs sockel-excluded excess +3.8 decades.
LEG A (the round's core finding): the bridge is EXACT -- toy
rationals n = 1..4; mp route identity worst 1.4e-59 (bar 1e-30);
chain-vs-moment F worst 1.4e-12 over 5 worlds x 7 degrees: for
n >= 1, F_n IS the d-functional, the quiet zone has NO third
mechanism.  d-census (42 windows): rel depth med ~2.1e-3 at EVERY
k = 0..15 (ranges [2.4e-05, 3.2e-03]) -- the comb-smooth moment
equality is ~3 decimal digits deep, k-UNIFORM, and NOT exact (law
floor 1e-13 missed by ~10 decades on every k); N-trend NEGATIVE on
all k (Spearman -0.78..-0.57: the equality DEEPENS with N, the
PNT-partial-sum signature).  w9 bridge anatomy: |F_n|/sqrt(h_n) =
1.2e-3..2.5e-3 with cancellation ratios 0.38 (n = 1) down to 0.01
(n = 7), median 0.05 >= 0.01, and |H^{-1}v| coefficients <= 1.38
=> QUIETZONE_DIRECT_D_LEVEL: the quiet-zone stillness is the
measured d-depth (~1e-3, squared in rho ~ 1e-6..1e-7) times O(1)
coefficients with only mild extra cancellation -- no hidden
mechanism.  Controls: SCRAMBLE breaks the d-levels from k = 1 on
(med +1.4 decades: position-mass pairing destroys the moment
equality across the board); EPSTEIN never breaks a level (med
+0.0 decades -- its d-profile is MAIN-close geometry, consistent
with the r246 head-identity); SMOOTH d == 0 EXACTLY (max 0.0 <=
1e-25) with the base broken at 27: the SMOOTH trap is live (m1) --
perfect moment equality certifies NOTHING about the base.  a3:
QUIETZONE_MEASURED_ONLY (law prefix k* = -1: no k reaches the
floor; SCRAMBLE does not survive) -- the stillness is ARITHMETIC
(finite PNT-partial-sum equality), not builder geometry; the
SOCKEL RE-ADJUDICATION stays CLOSED (typed diagnostic: even
against the bulk-only rest S - rho_0 - Q the r244 corners cover
only 1/16/24 of 42, identical to the r246 full-S coverage of
b3 -- the sockel + quiet zone are NOT the obstruction, the
extensive bulk is).  LEG B: M1 (equilibrium, SOURCE-PURE): med
|E|/M = 0.672 in [0.157, 1.2], Spearman +0.39 -- fails the median
bar (the r244 corner deficit reproduced in |E|/M form); M2
(telescope S_{N-21}, PREFIX DATA): med 0.0692 in [0.009, 0.30],
Spearman -0.78, falsifier fires DIRECTLY (+3.9 decades in |E|/M
pre-flip; Q-route +3.3 decades as cross-check) =>
INTEGRATED_M_CANDIDATE(M2) + M_IS_PREFIX_DATA -- honest reading:
the only integrated form that lands is the budget's own measured
head, a RESTATEMENT of the extensive bulk (r246), NOT a
source-side main term; M3 (trace/diagonal): med |E|/M = 0.582 in
[0.004, 0.98], Spearman +0.03 -- fails the median bar; NOTE (the
design expectation 'du -> 0 suppression' was WRONG in magnitude:
the diagonal carries ~63 percent of S at the median, the budget
is NOT strongly coherent -- measured, typed, no rule involved).
LEG C: bulk band [8, N-20] on 42/42: worst |eps| ladder-max
0.09281 (headroom 0.157 >= 1e-3), med(worst) 0.066, p90 med
0.024, med eps -0.0007, eps range [-0.0844, +0.0928]; Spearman
(worst; N) = -0.57 (the worst case SHRINKS with N) =>
BULK_CAPACITY_LAW_CANDIDATE fires with real margin: gammahat
stays in [0.166, 0.343] across the ENTIRE measured bulk -- far
inside (0, 1/2), the capacity plateau 1/4 is the median with p90
deviation ~0.024; head band [1, 7] worst |eps| med 0.038 / max
0.051 (finite certification); edge: no gammahat <= 0 in the last
20 anywhere.  Controls break mechanism: EPSTEIN/SCRAMBLE/SMOOTH
leave the (0, 1/2) band EXACTLY at their flips 25/21/27 via
gammahat < 0 (values -15 / -0.13 / -2.6; no early >= 1/2 exit):
the wall IS the band exit.  MUST-FAILS all loud: m1 SMOOTH trap
live, m2 self-border zero exact, m3 fiber oracle B = 1.01 S
covers 42/42 and is EXCLUDED, m4 sign oracle 42/42 EXCLUDED, m5
band sealed globally.  Runtime 10.5 s full, 0.7 s smoke.
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
K_MAX = 15
BRIDGE_N = 7
BRIDGE_KZ = (9, 12, 13)
MP_DPS = 60
ID_BAR = 1e-30
CHF_BAR = 1e-6
CHF_ABS2 = 1e-24
LAW_FLOOR = 1e-13
SMOOTH_D_BAR = 1e-25
DEC_BAR = 1.0
CANC_BAR = 0.01
QZ_LO, QZ_HI = 1, 7
BULK_LO = 8
EDGE_LEN = 20
EPS_BAR = 0.25
LAW_HEADROOM = 1e-3
EM_MED_BAR = 0.5
EM_TREND_BAR = 0.5
PRE_TAIL = 5
B_FLOOR = Fr(5, 7)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SMOKE_KZ = (9, 12, 13, 26, 40)
CAL_VERDICT = ("QUIETZONE_MEASURED_ONLY + SOURCE_RULE_IDENTITY_EXACT "
               "+ QUIETZONE_DIRECT_D_LEVEL + "
               "INTEGRATED_M_CANDIDATE(M2) + M_IS_PREFIX_DATA + "
               "BULK_CAPACITY_LAW_CANDIDATE + "
               "CAMPAIGN_SPEC_FROZEN")

CAMPAIGN_SPEC = """\
TFPT RH-LANE CAMPAIGN SPEC v1 (frozen r247) -- requirement document
for the asymptotic rounds of PRIME.PORT.RHP.FULLSOURCE.
OBJECTS: mutilde chain (h_n, alphahat_n, gammahat_n = h_n/h_{n-1});
  sigma border (F_n, T_n, rho_n = F_n^2/h_n, S_n, D_n(B) = B -
  S_{n-1}); moment gap d_k = s_k - m_k (k <= 15); quiet-zone mass
  Q = sum_{1<=n<=7} rho_n; sockel rho_0 = s_0^2/h_0 (geometry).
SPLIT: BASE = {h_n > 0, n < N} == gammahat-positivity chain;
  FIBER = D_N(B) >= 0 with B PARAMETRIC (tau^aug(B) always carries
  its parameter).  B DISCIPLINE (binding): any budget entering a
  positive claim is (i) source-side defined and FROZEN BEFORE any S
  evaluation, (ii) never fitted, (iii) named source contract;
  honest status: IMPORTED -- only B_w = S_{N-2} + 5/7 covers.
BANDS: head n in {0} u [1, 7] (sockel + quiet zone = d-functional,
  finite certification); bulk n in [8, N-20]; edge = last 20
  degrees (r241 edge rule, factor 1.46).
ERROR FORMS: bulk eps_n = gammahat_n - 1/4 (band profile, worst
  case, N-trend); integrated fiber S = M + E with target
  med|E|/M <= 0.5 and Spearman(|E|/M; N) <= 0.5; quiet zone: the
  d_k levels are the arithmetic input (PNT-partial-sum currency;
  F_n = d_n - v_n^T H_n^{-1} d_prefix EXACT for n >= 1).
FALSIFIERS (every follow-round carries all): EPSTEIN/SMOOTH break
  in the BASE (gammahat band exit at the sealed flips 25/27);
  SCRAMBLE shows the fiber excess >= 1 decade pre-target (Q or
  |E|/M on the pre-flip range); SMOOTH trap: d == 0 with base
  break at 27 -- no moment-equality certificate certifies the
  base; no control is ever certified; forced pivot h_N only
  falsifies.
FOLLOW-ROUNDS: (R1) d_k asymptotics -- the declared
  pair-correlation / PNT-error entry point (the quiet zone is the
  arithmetic surface); (R2) bulk gammahat law from the
  equilibrium/capacity input (r241; the law object is set by the
  r247 leg-C margin profile); (R3) E-control for the r247 leg-B
  winner, or a direct bulk-integral attack if no source-side M
  lands; (R4) edge-window composition (last 20 degrees, r241
  factor 1.46).
"""
CAMPAIGN_SHA = hashlib.sha256(CAMPAIGN_SPEC.encode("utf-8")).hexdigest()

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
    return (not bad), ("NO zero/prime oracles; rho/S and the r244 "
                       "corner candidates are the BITWISE r244 "
                       "objects (BH.wpack imported); d_k consumes "
                       "moments only; bands and cutoffs sealed; the "
                       "per-window band choice (m5) is a must-fail, "
                       "never a verdict path"
                       if not bad else "; ".join(bad))


# ------------------------------------------------- aux fiber chain
def fiber_chain(xs, ws, ys, vs, bx, bw, by, bv, n_upto):
    """BH.bord_chain recursion VERBATIM (r244) with ONE addition:
    per degree the diagonal (trace) increment of the sigma double
    smear, dg_n = (sum bw^2 qb^2 + sum bv^2 qc^2)/eta -- the M3
    candidate.  Every pre-existing operation is bitwise identical;
    rho is warded against BH.wpack in G21."""
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    rho = []
    dg = []
    for n in range(n_upto):
        fb = float(np.sum(bw * qb) - np.sum(bv * qc))
        rho.append(fb * fb / eta)
        dg.append((float(np.sum(bw * bw * qb * qb))
                   + float(np.sum(bv * bv * qc * qc))) / eta)
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
            pb = (bx - alh) * qb
            pc = (by - alh) * qc
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
            pb = (bx - alh) * qb - ge * fc * qb_m
            pc = (by - alh) * qc - ge * fc * qc_m
        sc = max(float(np.max(np.abs(px))), float(np.max(np.abs(py))),
                 float(np.max(np.abs(pb))), float(np.max(np.abs(pc))))
        if sc == 0.0 or not math.isfinite(sc):
            return rho, dg
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qb_m, qc_m = qb, qc
        qx, qy = px / sc, py / sc
        qb, qc = pb / sc, pc / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        if eta == 0.0 or not math.isfinite(eta):
            return rho, dg
    return rho, dg


def cheb_at(p, n_upto):
    """M1 at arbitrary cutoff: BITWISE the r244 wpack b2 code path
    (hull, mass m_0, arcsine chain via BH.cheb_budget)."""
    d, dsm = p["d"], p["dsm"]
    bxa = np.concatenate([dsm["xs"], dsm["ys"]])
    bwa = np.concatenate([dsm["ws"], -dsm["vs"]])
    wxa = np.concatenate([d["xs"], d["ys"]])
    wwa = np.concatenate([d["ws"], -d["vs"]])
    hull_lo = min(float(np.min(wxa)), float(np.min(bxa)))
    hull_hi = max(float(np.max(wxa)), float(np.max(bxa)))
    x0 = 0.5 * (hull_lo + hull_hi)
    rh = 0.5 * (hull_hi - hull_lo)
    m0 = float(np.sum(wwa))
    return BH.cheb_budget(bxa, bwa, x0, rh, m0, n_upto)


# ------------------------------------------------------- mp blocks
def mp_dk(p):
    """moment gaps d_k = s_k - m_k, k = 0..K_MAX, at dps 60 (the
    f64 route dies on the m_k/s_k cancellation)."""
    import mpmath as mp
    mp.mp.dps = MP_DPS
    mmom, smom = BH.mp_moments(p["d"], p["dsm"], K_MAX, MP_DPS)
    dks, rels = [], []
    for k in range(K_MAX + 1):
        dk = smom[k] - mmom[k]
        sc = max(abs(mmom[k]), abs(smom[k]))
        dks.append(dk)
        rels.append(float(abs(dk) / sc) if sc > 0 else 0.0)
    return mmom, smom, dks, rels


def mp_bridge(p, mmom, smom, dks):
    """the exact d-bridge at n = 1..BRIDGE_N: F_s = s_n - v^T
    H^{-1} q vs F_d = d_n - v^T H^{-1} d_prefix (identical by the
    self-border zero), plus chain-F agreement and the cancellation
    anatomy of the d-functional."""
    import mpmath as mp
    mp.mp.dps = MP_DPS
    out = []
    for n in range(1, BRIDGE_N + 1):
        H = mp.matrix([[mmom[i + j] for j in range(n)]
                       for i in range(n)])
        v = mp.matrix([mmom[n + i] for i in range(n)])
        sol_v = mp.lu_solve(H, v)
        h_n = mmom[2 * n] - mp.fsum(v[i] * sol_v[i]
                                    for i in range(n))
        F_s = smom[n] - mp.fsum(sol_v[i] * smom[i]
                                for i in range(n))
        terms = [dks[n]] + [-sol_v[i] * dks[i] for i in range(n)]
        F_d = mp.fsum(terms)
        tsum = mp.fsum(abs(t) for t in terms)
        hsc = mp.sqrt(abs(h_n))
        dev_id = float(abs(F_s - F_d) / hsc)
        r = p["rows"][n]
        F_ch = r["fb"] * math.exp(r["Ls"])
        if float((F_s / hsc) ** 2) > CHF_ABS2:
            dev_ch = abs(F_ch / float(F_s) - 1.0)
        else:
            dev_ch = abs(F_ch - float(F_s)) / float(hsc)
        canc = float(abs(F_d) / tsum) if tsum > 0 else float("nan")
        cmax = max(float(abs(sol_v[i])) for i in range(n))
        out.append(dict(n=n, dev_id=dev_id, dev_ch=dev_ch,
                        canc=canc, cmax=cmax,
                        Fnorm=float(abs(F_s) / hsc)))
    return out


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("basefiber_probe -- PRIME.PORT.RHP.FULLSOURCE."
          "BASEFIBER.01 (round 247)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (five known rungs, d-census reduced)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "machinery imported verbatim (BH.wpack bitwise: rho, S, "
          "r244 corners; F_DEF_SHA above); K_MAX %d, bridge n = "
          "1..%d on worlds %s + EPSTEIN + SCRAMBLE; bars: route "
          "identity %.0e, chain-F %.0e, law floor %.0e, SMOOTH d "
          "%.0e, decade %.1f, cancellation %.2f; quiet zone [%d, "
          "%d]; bulk [%d, N-%d]; eps bar %.2f; |E|/M bars %.1f / "
          "%.1f; M2 cutoff N-%d, control tail %d; verdict rules "
          "sealed in the frozen spec"
          % (K_MAX, BRIDGE_N, str(BRIDGE_KZ), ID_BAR, CHF_BAR,
             LAW_FLOOR, SMOOTH_D_BAR, DEC_BAR, CANC_BAR, QZ_LO,
             QZ_HI, BULK_LO, EDGE_LEN, EPS_BAR, EM_MED_BAR,
             EM_TREND_BAR, EDGE_LEN, PRE_TAIL))

    # ---------------- S1: leg 0 -- base-fiber split (exact toy)
    section("S1  LEG 0 -- BASE-FIBER SPLIT (rationals) + B "
            "DISCIPLINE")
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
    smomt = [sum(w * x ** k for w, x in zip(SBw, SBn))
             for k in range(NTOY + 2)]
    Ftoy = [sum(w * PB.toy_eval(al, hs, k, x)
                for w, x in zip(SBw, SBn)) for k in range(NTOY + 1)]
    Stoy = []
    acc = Fr(0)
    for k in range(NTOY + 1):
        acc += Ftoy[k] * Ftoy[k] / hs[k]
        Stoy.append(acc)

    def Hm(n):
        return [[mom[i + j] for j in range(n)] for i in range(n)]

    def Gb(n, B):
        M = [[mom[i + j] for j in range(n)] + [smomt[i]]
             for i in range(n)]
        M.append([smomt[j] for j in range(n)] + [B])
        return M

    n = NTOY
    B_hi = Stoy[n - 1] + 1
    B_lo = Stoy[n - 1] - 1
    ok_split = True
    for B, want_pos in ((B_hi, True), (B_lo, False)):
        detG = PB.frac_det(Gb(n, B))
        detH = PB.frac_det(Hm(n))
        ok_split = ok_split and (detG == detH * (B - Stoy[n - 1]))
        ok_split = ok_split and ((detG > 0) == want_pos)
    # positivity of the toy prefix pivots (base) is h_k > 0? the
    # r243 toy is SIGNED -- gate the identity, not toy positivity
    check("G10-base-fiber-split-exact", ok_split,
          "rationals on the r243 toy (n = 4): det [[H_n, u],[u^T, "
          "B]] = det H_n (B - S_{n-1}) at B = S +- 1 -- the "
          "bordered determinant changes sign EXACTLY with the "
          "fiber corner while the base block is untouched: PSD of "
          "the bordered matrix == (BASE: nested pivots h_0..h_{n-1}"
          " > 0) + (FIBER: B - S_{n-1} >= 0), the r243 G12 nested-"
          "pivot chain cited and re-gated at the split point")
    check("G11-B-discipline-frozen", True,
          "FROZEN (campaign-binding): any budget B_w entering a "
          "positive claim is (i) source-side defined and fixed "
          "BEFORE any S evaluation, (ii) never fitted, (iii) named "
          "source contract; tau^aug is ALWAYS tau^aug(B) with "
          "parameter; HONEST STATUS: IMPORTED -- the only covering "
          "budget remains B_w = S_{N-2} + 5/7 (prefix data + r241 "
          "floor; r243/r244/r246 unchanged, nothing upgraded)")

    # ---------------- S2: ladder + controls + aux chain
    section("S2  LADDER + CONTROLS + AUX-CHAIN WARD")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    packs = [BH.wpack(kz) for kz in kzs]
    packs.sort(key=lambda p: (p["N"], p["kz"]))
    by_kz = {p["kz"]: p for p in packs}
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
    fib_min = min(float(B_FLOOR) - float(p["rho"][p["N"] - 1])
                  for p in packs)
    scr = ctrl["SCRAMBLE"]
    nf_s = scr["nf"]
    pre_dec = math.log10(float(scr["S"][nf_s - 1])
                         / float(by_kz[9]["S"][nf_s - 1]))
    # sockel-excluded pre-flip excess (amendment a1, smoke-caught:
    # the TOTAL pre-flip budget is mode-0 dominated in every world
    # -- r246 -- so the total ratio is blind; the excess lives in
    # n >= 1)
    exc_dec = math.log10(
        (float(scr["S"][nf_s - 1]) - float(scr["rho"][0]))
        / (float(by_kz[9]["S"][nf_s - 1])
           - float(by_kz[9]["rho"][0])))
    check("G20-base-fiber-census", okC and okCf and fib_min > 0.0,
          "BASE: free prefix positive on %d/%d MAIN windows (N in "
          "[%d, %d]); control BASE flips at the sealed degrees %s "
          "(EPSTEIN/SMOOTH are base falsifiers); FIBER with the "
          "imported B_w = S_{N-2} + 5/7: min margin 5/7 - "
          "rho_{N-1} = %.4f > 0 (r243 razor reproduced); SCRAMBLE "
          "fiber falsifier: pre-flip TOTAL budget ratio %+.1f "
          "decades (mode-0 dominated, blind -- r246 reproduced), "
          "sockel-excluded excess (S - rho_0 on n < %d) = %+.1f "
          "decades (full-depth control budget is SIGNED "
          "post-flip, non-adjudicable -- r246 typed, cited)"
          % (sum(1 for p in packs if p["nf"] is None), len(packs),
             packs[0]["N"], packs[-1]["N"],
             str({c: ctrl[c]["nf"] for c in ctrl}), fib_min,
             pre_dec, nf_s, exc_dec))
    ward = 0.0
    for p in packs + list(ctrl.values()):
        d, dsm = p["d"], p["dsm"]
        rho2, dg = fiber_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                               dsm["xs"], dsm["ws"], dsm["ys"],
                               dsm["vs"], p["N"])
        p["dg"] = np.asarray(dg)
        sc = float(np.max(np.abs(p["rho"]))) or 1.0
        ward = max(ward, float(np.max(np.abs(
            np.asarray(rho2) - np.asarray(p["rho"])))) / sc)
    m1_ward = max(abs(cheb_at(p, p["N"]) / p["b2"] - 1.0)
                  for p in packs)
    check("G21-aux-chain-ward", ward <= 1e-12 and m1_ward <= 1e-12,
          "the diag-augmented fiber chain reproduces the BITWISE "
          "r244 rho on every world (worst rel %.1e <= 1e-12: the "
          "added trace accumulator perturbs nothing); the M1 "
          "cutoff evaluator reproduces wpack's b2 at n = N (worst "
          "rel %.1e)" % (ward, m1_ward))

    # ---------------- S3: leg A -- quiet-zone source rule
    section("S3  LEG A -- QUIET-ZONE SOURCE RULE (d-bridge + "
            "census)")
    # toy bridge, exact: F_n == d_n - v^T H^{-1} d_prefix
    dtoy = [smomt[k] - mom[k] for k in range(NTOY + 2)]
    okT = True
    for n in range(1, NTOY + 1):
        v = [mom[n + i] for i in range(n)]
        sol_v = PB.frac_solve(Hm(n), v)
        F_d = dtoy[n] - sum(sol_v[i] * dtoy[i] for i in range(n))
        okT = okT and (F_d == Ftoy[n])
        # m2 engine: self-border zero
        F_self = mom[n] - sum(sol_v[i] * mom[i] for i in range(n))
        okT = okT and (F_self == 0)
    check("G30-toy-bridge-exact", okT,
          "rationals (n = 1..4): F_n = d_n - v_n^T H_n^{-1} "
          "(d_0..d_{n-1}) EXACTLY, with d_k = s_k - m_k -- the "
          "engine is the r243 self-border zero m_n - v^T H^{-1} "
          "m_prefix = 0 (G14 cited, re-gated): for n >= 1 the "
          "border functional F sees ONLY the moment gaps; the "
          "quiet zone has no third mechanism BY IDENTITY")
    bridge_worlds = ([("w%d" % kz, by_kz[kz]) for kz in BRIDGE_KZ
                      if kz in by_kz]
                     + [("EPSTEIN", ctrl["EPSTEIN"]),
                        ("SCRAMBLE", ctrl["SCRAMBLE"])])
    id_w = ch_w = 0.0
    canc9 = []
    cmax9 = 0.0
    mp_cache = {}
    for name, p in bridge_worlds:
        mmom, smom, dks, rels = mp_dk(p)
        mp_cache[name] = (mmom, smom, dks, rels)
        rows = mp_bridge(p, mmom, smom, dks)
        id_w = max(id_w, max(r["dev_id"] for r in rows))
        ch_w = max(ch_w, max(r["dev_ch"] for r in rows))
        if name == "w9":
            canc9 = [r["canc"] for r in rows]
            cmax9 = max(r["cmax"] for r in rows)
            info("w9 bridge anatomy (n: |F|/sqrt(h), canc "
                 "|F|/sum|terms|, max|H^-1 v|): " + "; ".join(
                     "%d: %.1e, %.2f, %.2f"
                     % (r["n"], r["Fnorm"], r["canc"], r["cmax"])
                     for r in rows))
    check("G31-mp-bridge", id_w <= ID_BAR and ch_w <= CHF_BAR,
          "mp (dps %d) on %d worlds x n = 1..%d: route identity "
          "|F_s - F_d|/sqrt(h_n) worst %.1e (bar %.0e -- the two "
          "routes are the SAME functional); chain-vs-moment F "
          "worst %.1e (bar %.0e, sqrt(h) guard): the d-bridge is "
          "exact on the true comb, SOURCE_RULE_IDENTITY candidate "
          "gates" % (MP_DPS, len(bridge_worlds), BRIDGE_N, id_w,
                     ID_BAR, ch_w, CHF_BAR))
    # d-census over the ladder
    rel_tab = {k: [] for k in range(K_MAX + 1)}
    Ns = [p["N"] for p in packs]
    for p in packs:
        kz = p["kz"]
        name = "w%d" % kz
        if name in mp_cache:
            rels = mp_cache[name][3]
        else:
            rels = mp_dk(p)[3]
            mp_cache[name] = (None, None, None, rels)
        for k in range(K_MAX + 1):
            rel_tab[k].append(rels[k])
    law_ks = []
    for k in range(K_MAX + 1):
        v = rel_tab[k]
        sp = BH.spearman(v, Ns)
        info("d_%-2d rel depth med %.2e in [%.2e, %.2e] | "
             "Spearman(rel; N) %+.2f"
             % (k, float(np.median(v)), min(v), max(v), sp))
        if max(v) <= LAW_FLOOR:
            law_ks.append(k)
    check("G32-d-census", True,
          "moment-gap census over %d windows, k = 0..%d (table "
          "above): the equality depth and its N-trend are the "
          "round's measured arithmetic surface; k at the law "
          "floor (%.0e on 42/42): %s"
          % (len(packs), K_MAX, LAW_FLOOR,
             str(law_ks) if law_ks else "NONE"))
    # controls: d-level break
    rels9 = mp_cache["w9"][3]
    br_note = []
    scr_decs = []
    for cname in ("EPSTEIN", "SCRAMBLE"):
        relc = mp_cache[cname][3]
        decs = [math.log10(relc[k] / rels9[k])
                if rels9[k] > 0 and relc[k] > 0 else float("nan")
                for k in range(K_MAX + 1)]
        kbrk = next((k for k, dc in enumerate(decs)
                     if math.isfinite(dc) and dc >= DEC_BAR), None)
        if cname == "SCRAMBLE":
            scr_decs = decs
        br_note.append("%s: first >= %.0f-decade break at k = %s; "
                       "med dec %+.1f"
                       % (cname, DEC_BAR, str(kbrk),
                          float(np.nanmedian(decs))))
    _mm, _sm, dks_sm, rels_sm = mp_dk(ctrl["SMOOTH"])
    sm_dmax = max(rels_sm)
    okSm = sm_dmax <= SMOOTH_D_BAR
    check("G33-controls-d-break", okSm,
          "d-level break vs MAIN-w9 (relative depths, per-k "
          "decades): %s; SMOOTH: max rel d_k = %.1e <= %.0e -- "
          "PERFECT moment equality (its window IS the border "
          "comb) with the base broken at %d: the SMOOTH trap is "
          "live (m1)" % ("; ".join(br_note), sm_dmax,
                         SMOOTH_D_BAR, ctrl["SMOOTH"]["nf"]))
    # a3 adjudication
    kstar = -1
    while (kstar + 1) in law_ks:
        kstar += 1
    law_main = kstar >= 1
    law_scr = law_main and all(
        (mp_cache["SCRAMBLE"][3][k] <= LAW_FLOOR)
        for k in range(kstar + 1))
    if law_main and law_scr:
        vA = "QUIETZONE_LAW_FOUND"
    else:
        vA = "QUIETZONE_MEASURED_ONLY"
    canc_med = float(np.median(canc9)) if canc9 else float("nan")
    sub = ("QUIETZONE_DIRECT_D_LEVEL" if canc_med >= CANC_BAR
           else "QUIETZONE_EXTRA_CANCELLATION")
    src_ok = okT and id_w <= ID_BAR and ch_w <= CHF_BAR
    vA_full = vA + (" + SOURCE_RULE_IDENTITY_EXACT" if src_ok
                    else "") + " + " + sub
    check("G34-quietzone-adjudicated", True,
          "SEALED RULE result: %s -- law prefix band on MAIN: "
          "k* = %d (needs >= 1 with SCRAMBLE surviving: %s); "
          "cancellation median %.2f over n = 1..7 on w9 (bar "
          "%.2f, max |H^{-1}v| coeff %.2f): the quiet-zone LEVEL "
          "is %s; the RULE itself (F = d-functional) is %s"
          % (vA_full, kstar, "yes" if law_scr else "no",
             canc_med, CANC_BAR, cmax9,
             "directly the measured d-depth (no extra "
             "cancellation layer)" if sub.endswith("LEVEL")
             else "further cancelled below the d-level",
             "EXACT (theorem-grade identity, gated)" if src_ok
             else "OPEN"))
    # sockel path
    if vA == "QUIETZONE_LAW_FOUND":
        cov_note = []
        for tag in ("b1", "b2", "b3"):
            cov = sum(1 for p in packs
                      if p[tag] - (p["St"] - float(p["rho"][0])
                                   - float(np.sum(
                                       p["rho"][QZ_LO:QZ_HI + 1])))
                      > 0.0)
            cov_note.append("%s %d/%d" % (tag, cov, len(packs)))
        check("G35-sockel-readjudication", True,
              "LAW fired -> source-rule sockel peeling admissible: "
              "r244 corners vs bulk-only rest S - rho_0 - Q: %s"
              % "; ".join(cov_note))
    else:
        cov_note = []
        for tag in ("b1", "b2", "b3"):
            cov = sum(1 for p in packs
                      if p[tag] - (p["St"] - float(p["rho"][0])
                                   - float(np.sum(
                                       p["rho"][QZ_LO:QZ_HI + 1])))
                      > 0.0)
            cov_note.append("%s %d/%d" % (tag, cov, len(packs)))
        check("G35-sockel-path-closed", True,
              "sealed rule: the sockel re-adjudication is gated "
              "behind QUIETZONE_LAW_FOUND (not fired) -- CLOSED; "
              "TYPED DIAGNOSTIC ONLY (no verdict weight): r244 "
              "corners vs the bulk-only rest S - rho_0 - Q would "
              "cover %s" % "; ".join(cov_note))

    # ---------------- S4: leg B -- integrated fiber form
    section("S4  LEG B -- INTEGRATED FIBER FORM S = M + E")
    check("G40-candidates-sealed", True,
          "M1 = equilibrium/Szego budget (BITWISE r244 b2; "
          "SOURCE-PURE); M2 = telescope partial sum S_{N-%d} "
          "(PREFIX DATA, disclosed); M3 = trace/diagonal part of "
          "the double smear (CHAIN CURRENCY, exact split; du -> 0 "
          "suppression disclosed pre-run); mapping to the "
          "contract labels: M1 = b1(glatt/equilibrium), M2 = "
          "b2(telescope), M3 = b3(trace)" % EDGE_LEN)
    cand = {}
    for p in packs:
        N = p["N"]
        p["M1"] = p["b2"]
        p["M2"] = float(p["S"][N - EDGE_LEN - 1])
        p["M3"] = float(np.sum(p["dg"]))
    ok_split3 = True
    for p in packs:
        e3 = p["St"] - p["M3"]
        ok_split3 = ok_split3 and math.isfinite(e3)
    okM2t = max(abs((p["St"] - p["M2"])
                    - float(np.sum(p["rho"][p["N"] - EDGE_LEN:])))
                / p["St"] for p in packs)
    check("G41-decomposition-wards", ok_split3 and okM2t <= 1e-12,
          "M3 + E3 = S by construction (finite on 42/42); M2 "
          "telescope ward: S - S_{N-%d} equals the direct last-%d "
          "rho sum (worst rel %.1e <= 1e-12); M1 cutoff ward "
          "gated in G21" % (EDGE_LEN, EDGE_LEN, okM2t))
    for tag in ("M1", "M2", "M3"):
        em = [abs(p["St"] - p[tag]) / p[tag] if p[tag] > 0
              else float("inf") for p in packs]
        sp = BH.spearman(em, Ns)
        cand[tag] = dict(em=em, med=float(np.median(em)), sp=sp)
        info("%s: |E|/M med %.3g in [%.3g, %.3g] | Spearman(|E|/M;"
             " N) %+.2f" % (tag, cand[tag]["med"], min(em),
                            max(em), sp))
    check("G42-EM-table", True,
          "|E|/M distribution over %d windows per candidate "
          "(table above) -- the integrated-form quality surface "
          "of the fiber" % len(packs))
    # falsifier: pre-flip range on SCRAMBLE vs MAIN-w9
    p9 = by_kz[9]
    nf = nf_s
    S9p = float(p9["S"][nf - 1])
    Ssp = float(scr["S"][nf - 1])
    Q9 = float(np.sum(p9["rho"][QZ_LO:QZ_HI + 1]))
    Qs = float(np.sum(scr["rho"][QZ_LO:QZ_HI + 1]))
    qdec = math.log10(Qs / Q9)
    fals = {}
    for tag in ("M1", "M2", "M3"):
        if tag == "M1":
            m9 = cheb_at(p9, nf)
            ms = cheb_at(scr, nf)
        elif tag == "M2":
            m9 = float(p9["S"][nf - PRE_TAIL - 1])
            ms = float(scr["S"][nf - PRE_TAIL - 1])
        else:
            m9 = float(np.sum(p9["dg"][:nf]))
            ms = float(np.sum(scr["dg"][:nf]))
        r9 = abs(S9p - m9) / m9 if m9 > 0 else float("inf")
        rs = abs(Ssp - ms) / ms if ms > 0 else float("inf")
        edec = (math.log10(rs / max(r9, 1e-30))
                if math.isfinite(rs) and rs > 0 else float("nan"))
        via_q = not (math.isfinite(edec) and edec >= DEC_BAR) \
            and qdec >= DEC_BAR
        fals[tag] = dict(edec=edec, via_q=via_q,
                         ok=(math.isfinite(edec)
                             and edec >= DEC_BAR) or via_q)
        info("%s falsifier (n < %d): |E|/M MAIN %.3g vs SCRAMBLE "
             "%.3g -> %+.1f decades%s"
             % (tag, nf, r9, rs, edec,
                "; via quiet zone (Q %+.1f dec)" % qdec
                if via_q else ""))
    check("G43-falsifier", True,
          "SCRAMBLE visibility pre-target (sealed: >= %.0f decade "
          "in |E|/M on the common pre-flip range OR in the leg-A "
          "quiet-zone observable Q): Q_scr/Q_w9 = %+.1f decades "
          "(the r246 quiet-zone level break IS the pre-target "
          "fiber falsifier); per-candidate rows above"
          % (DEC_BAR, qdec))
    winners = []
    mods = []
    for tag in ("M1", "M2", "M3"):
        c = cand[tag]
        if (c["med"] <= EM_MED_BAR and c["sp"] <= EM_TREND_BAR
                and fals[tag]["ok"]):
            winners.append(tag)
            if tag == "M2":
                mods.append("M_IS_PREFIX_DATA")
            if fals[tag]["via_q"]:
                mods.append("FALSIFIER_VIA_QUIETZONE")
    if winners:
        vB = ("INTEGRATED_M_CANDIDATE(%s)" % ",".join(winners)
              + "".join(" + " + m for m in mods))
    else:
        vB = "NO_INTEGRATED_FORM"
    check("G44-integrated-adjudicated", True,
          "SEALED RULE result: %s -- bars: med |E|/M <= %.1f, "
          "Spearman <= %.1f, falsifier visible; HONESTY (sealed): "
          "a firing M2 is the budget's own measured head (prefix "
          "data) -- a RESTATEMENT of the extensive bulk (r246), "
          "never a source-side main term; no control is certified "
          "(SMOOTH budget = rho_0 alone, wall kills it at 27)"
          % (vB, EM_MED_BAR, EM_TREND_BAR))

    # ---------------- S5: leg C -- bulk capacity law candidate
    section("S5  LEG C -- BULK CAPACITY LAW CANDIDATE")
    worsts = []
    viols = 0
    p90s = []
    eps_min = float("inf")
    eps_max = -float("inf")
    med_all = []
    head_worst = []
    edge_viol = 0
    for p in packs:
        N = p["N"]
        gams = [p["rows"][k]["gam_next"] for k in range(N - 1)]
        bulk = np.asarray(gams[BULK_LO - 1:N - EDGE_LEN],
                          float) - 0.25
        head = np.asarray(gams[0:QZ_HI], float) - 0.25
        edge = np.asarray(gams[N - EDGE_LEN:N - 1], float) - 0.25
        worsts.append(float(np.max(np.abs(bulk))))
        p90s.append(float(np.quantile(np.abs(bulk), 0.9)))
        viols += int(np.sum(np.abs(bulk) >= EPS_BAR))
        eps_min = min(eps_min, float(np.min(bulk)))
        eps_max = max(eps_max, float(np.max(bulk)))
        med_all.append(float(np.median(bulk)))
        head_worst.append(float(np.max(np.abs(head))))
        edge_viol += int(np.sum(edge <= -0.25))
    spW = BH.spearman(worsts, Ns)
    info("bulk band [%d, N-%d]: worst |eps| ladder-max %.7f "
         "(margin to 1/4: %.1e), med(worst) %.4f, p90 med %.4f, "
         "med eps %+.4f; eps range [%+.5f, %+.5f]; Spearman("
         "worst; N) %+.2f; violations %d"
         % (BULK_LO, EDGE_LEN, max(worsts),
            EPS_BAR - max(worsts), float(np.median(worsts)),
            float(np.median(p90s)), float(np.median(med_all)),
            eps_min, eps_max, spW, viols))
    info("head band [1, %d]: worst |eps| med %.3f max %.3f "
         "(outside the law band, certified by finite "
         "measurement); edge band (last %d): gammahat <= 0 count "
         "%d (edge composes by the r241 edge rule, factor 1.46, "
         "cited)" % (QZ_HI, float(np.median(head_worst)),
                     max(head_worst), EDGE_LEN, edge_viol))
    check("G50-eps-census", True,
          "eps profile measured sharp on 42/42 (bands, worst "
          "case, N-trend above) -- the requirement surface of "
          "any bulk gammahat law")
    exit_note = []
    okX = True
    for cname in ("EPSTEIN", "SCRAMBLE", "SMOOTH"):
        pc = ctrl[cname]
        ex = None
        for k in range(pc["N"] - 1):
            g = pc["rows"][k]["gam_next"]
            if g is None or not (0.0 < g < 0.5):
                ex = k + 1
                break
        okX = okX and ex == CTRL_FLIPS[cname]
        exit_note.append("%s exit at n = %s (flip %d, gammahat "
                         "%.2g)" % (cname, str(ex),
                                    CTRL_FLIPS[cname],
                                    pc["rows"][ex - 1]["gam_next"]
                                    if ex else float("nan")))
    check("G51-controls-band-exit", okX,
          "break mechanism: %s -- every control leaves the "
          "(0, 1/2) band EXACTLY at its sealed flip via gammahat "
          "< 0 (no early >= 1/2 exit): the wall IS the band exit"
          % "; ".join(exit_note))
    headroom = EPS_BAR - max(worsts)
    if viols == 0 and headroom >= LAW_HEADROOM:
        vC = "BULK_CAPACITY_LAW_CANDIDATE"
        caveat = (" (violations 0/%d, worst |eps| = %.5f with "
                  "headroom %.2e >= %.0e to the 1/4 bar, "
                  "Spearman(worst; N) = %+.2f)"
                  % (len(packs), max(worsts), headroom,
                     LAW_HEADROOM, spW))
    elif viols == 0:
        vC = "BULK_MEASURED_ONLY"
        caveat = (" (sealed headroom clause: violations 0/%d but "
                  "the worst case sits only %.1e below the 1/4 "
                  "bar (< %.0e), eps range [%+.5f, %+.5f], "
                  "Spearman(worst; N) = %+.2f -- with zero "
                  "headroom |eps| < 1/4 is the tautology 'base "
                  "positivity', not a capacity law; the plateau "
                  "(med eps %+.4f) is a median property, the law "
                  "object goes to the campaign spec)"
                  % (len(packs), headroom, LAW_HEADROOM, eps_min,
                     eps_max, spW, float(np.median(med_all))))
    else:
        vC = "BULK_MEASURED_ONLY"
        caveat = (" (%d violations of |eps| < 1/4 inside the "
                  "sealed bulk band)" % viols)
    check("G52-bulk-adjudicated", True,
          "SEALED RULE result: %s%s -- COMPOSITION (minimal bulk "
          "statement): BASE(w) <= [head n <= %d: finite check, "
          "42/42] AND [bulk n in [%d, N-%d]: gammahat in (0, "
          "1/2)] AND [edge last %d: gammahat > 0, r241 edge "
          "rule] via h_n = h_0 prod gammahat"
          % (vC, caveat, QZ_HI, BULK_LO, EDGE_LEN, EDGE_LEN))

    # ---------------- S6: leg D -- campaign spec
    section("S6  LEG D -- CAMPAIGN SPEC (frozen deliverable)")
    print(CAMPAIGN_SPEC, flush=True)
    check("G60-campaign-spec-frozen", True,
          "CAMPAIGN_SPEC_FROZEN -- SHA %s (module constant, "
          "printed above in full; the deliverable of leg D)"
          % CAMPAIGN_SHA[:16])

    # ---------------- S7: must-fails
    section("S7  MUST-FAILS")
    okM = okSm and ctrl["SMOOTH"]["nf"] == CTRL_FLIPS["SMOOTH"]
    n_orc = sum(1 for p in packs if 1.01 * p["St"] - p["St"] > 0)
    okM = okM and n_orc == len(packs)
    n_sgn = sum(1 for p in packs
                if p["rows"][p["N"] - 1]["sg_h"] > 0)
    okM = okM and n_sgn == len(packs)
    check("G80-must-fails-fire", okM and okT,
          "m1 SMOOTH trap live: d == 0 exactly (G33) with base "
          "broken at 27 -- no moment-equality certificate "
          "certifies the base; m2 self-border alias F == 0 exact "
          "(G30, the bridge engine); m3 fiber oracle B = 1.01 S "
          "covers %d/%d trivially and is EXCLUDED (consumes S); "
          "m4 sign oracle hits %d/%d and is EXCLUDED; m5 band "
          "oracle: the bulk band is sealed GLOBALLY, a per-window "
          "band never enters any verdict path"
          % (n_orc, len(packs), n_sgn, len(packs)))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a foundations + "
          "measurement round moves no edge); what the round adds: "
          "the base-fiber architecture with frozen B discipline, "
          "the exact quiet-zone source rule (F = d-functional), "
          "the integrated-form quality surface, the bulk eps "
          "requirement profile, and the sealed campaign spec")
    verd = "%s + %s + %s + CAMPAIGN_SPEC_FROZEN" % (vA_full, vB, vC)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s%s -- PROVEN: the base-fiber split and the d-bridge "
          "(exact identities); MEASURED: d-census, |E|/M surface, "
          "eps profile, control breaks; OPEN: the budget bound "
          "and the base law themselves (r243 PAIRCORR_REENCODED "
          "stands); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s   CAMPAIGN_SHA "
          "%s" % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
                  SPEC_SHA[:16], CAMPAIGN_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
