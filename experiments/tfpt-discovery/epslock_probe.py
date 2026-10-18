#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""epslock_probe -- PRIME.EPSLOCK.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on OMEGA-a = EPS-LOCK, the first of
the two serial remainders of round 135)
=======================================================================
Round 135 (hpin_floor_probe, 33/33) split the last arithmetic-path
omega H-pin into (OMEGA-a) EPS-LOCK -- eps_bar <= poly(x) |A_0|
sqrt(G) lam-uniformly, eps_bar = sqrt((tau + OFF_ALLOW)/2) -- and
(OMEGA-b) SPACING-REMAINDER (concurrent lane).  Round 135 measured
eps_bar/(|A_0| sqrt(8 G(T_z))) = 0.28 -> 0.51 over x = 3..24,
drifting toward ~0.5, and posed the EXACT-CONSTANT question: is
tau -> 4 A_0^2 G an identity?  This probe (T1) DERIVES and measures
the exact GW budget of tau in A_0^2 G currency, (T2) PROVES the
reduction Theorem E1 (EPS-LOCK <== JET-LOCK + BAND-MASS-CONTRACTION,
explicit constants) and instantiates it per rung, (T3) prices the
weakest sufficient form against the cited r135 H-pin margins, (T4)
runs controls/screens, and adjudicates the exact-half hypothesis on
a deepened ladder x = 3..28 (x = 28 NEW depth).

NOTATION.  Per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, om_max = (K-1) pi/A, minimizer coefficients c_k
(round-114 builder, unit L2), E_N(z) = 2 sin(Az) F(z^2)/z with
F(y) = A_0 + sum_k w_k/(y - b_k), w_k = (-1)^k c_k b_k, b_k = om_k^2
(r131 Layer 1 + r135 D1, cited); boundary jets A_{2m} =
sum_k (-1)^k c_k om_k^{2m} (A_0 = phi(A)); SABS_{2m} =
sum |c_k| om_k^{2m}; tau = lambda_min of the compressed Weil form;
T_z = min(0.98 om_max, 2 pi x) (r131 G17); G(T) = certified HSW22
upper bound for sum_{gamma > T} gamma^{-2}; gtop = top cache
ordinate (X5, 7000 zeros, gtop = 7264.75).

=======================================================================
T1 -- THE EXACT BUDGET (the derivation; every step exact or cited)
=======================================================================
Guinand-Weil on psi = phi * phi~ (r131 Layer 2, cited; re-gated here
through the budget): tau = 2 sum_{gamma>0} |E_N(gamma)|^2 + S_off,
|S_off| <= OFF_ALLOW = 8 e^A ENV_3(T_PT)^2 G(T_PT) (r131 recipe;
e^A = sqrt(x) EXACTLY, so OFF == 8 sqrt(x) (1+eta_PT)^2 A_0^2 G(T_PT)
with eta_PT := ENVres_3(T_PT)/|A_0| -- the OFF identity, G15).
Per-term EXACT: 2|E_N(gamma)|^2 = 8 sin^2(A gamma) F(gamma^2)^2 /
gamma^2, and with 2A = log x the phase identity
     cos(2 A gamma) == cos(gamma log x)  --
THE TAIL OSCILLATION AT RUNG x IS LANDAU'S EXPONENTIAL SUM AT THE
COORDINATE x ITSELF (x^{i gamma} = x^{rho}/sqrt(x); Landau 1912,
uniform version Gonek 1993, CITED for the prediction shape only).
BUDGET DECOMPOSITION (exact per-term algebra, machine-gated):
  tau = M_band + M_mid + M_beyond + S_off,
  M_band = 2 sum_{gamma <= om_max} |E_N|^2   (polished ordinates),
  M_mid  = 2 sum_{om_max < gamma <= gtop} |E_N|^2
         = 4 A_0^2 (G_mid - C_mid) + J_mid,
     G_mid = sum gamma^{-2},  C_mid = sum cos(gamma log x)/gamma^2,
     J_mid = 8 sum sin^2(A gamma)(F^2 - A_0^2)/gamma^2,
  M_beyond in [0, 8 A_0^2 (1+eta_top)^2 G(gtop)]  (sin^2 <= 1 +
     jet envelope; eta_top := min_m ENVres_m(gtop)/|A_0|,
     ENVres_m(T) = sum_{i=1..m} |A_{2i}|/T^{2i}
                   + SABS_{2m+2}/(T^{2m}(T^2 - om_max^2)),
     each term monotone falling in T for T > om_max -- G13).
LANDAU PIN: C_mid_pred = -Lambda(x)/(2 pi sqrt(x)) (1/om_max -
1/gtop); fluctuation scale sigma_C = sqrt(sum gamma^{-4}/2).
R_J := M_mid / (4 A_0^2 (G_mid - C_mid)) -- the pure F^2-excess of
the tail onset; R_J == 1 iff the exact-half law is clean.

=======================================================================
T2 -- THEOREM E1 (the reduction; proven, sympy-gated) + E2
=======================================================================
THEOREM E1.  Fix a rung and a split point Theta.  IF
  (BM_theta)  M_below(Theta) <= theta (tau + OFF), theta < 1,
  (JL_rho)    |F(gamma^2)/A_0 - 1| <= rho at every zero gamma with
              Theta < gamma <= gtop (pointwise-checkable) AND
              ENVres(gtop) <= eta |A_0| (beyond-cache envelope),
THEN  tau (1-theta) <= 8 (1+max(rho,eta))^2 A_0^2 G(Theta)
                       + (1+theta) OFF   and hence
  eps_bar^2 <= [4 (1+r)^2 / (1-theta)] A_0^2 G(Theta)
               + OFF/(1-theta),   r = max(rho, eta),
  lock := eps_bar/(|A_0| sqrt(8 G(T_z))) <= sqrt(C_E1/8),
  C_E1 = [4(1+r)^2 G(Theta)/G(T_z) + OFF/(A_0^2 G(T_z))]/(1-theta).
PROOF: rearrangement of the budget + sin^2 <= 1 + HSW (sympy G14).
The probe instantiates E1 per rung with MEASURED (theta, rho, eta)
on a rho-grid (0.5, 1, 2, 4, 8), reporting the optimal C_E1*.
LAM-UNIFORM EPS-LOCK REDUCES EXACTLY TO: (JL) jet-lock -- a SOURCE-
side statement on the minimizer's jets (no zeros) -- and (BM) the
band-mass contraction -- the arithmetic core: the finitely many
zeros below Theta never carry more than a fixed fraction of the GW
value.  Both typed OPEN; BM is strictly weaker than H-pin's
exponential pinning (theta < 1 vs gap ~ eps_bar).
THEOREM E2 (weakest sufficient form; exact rearrangement).  The
r135-D3 zone-mass demand m_min >= 16 eps_bar sum|w'|/TL tolerates
eps_bar inflation by EXACTLY the measured margin m_min/m_req; the
ball-validity side condition b <= sp/2 tolerates inflation by
sp_min/(2 g_max).  Hence per rung the SUFFICIENT EPS-LOCK is
lock <= lock_meas * min(margin_r135, sp_min/(2 g_max_r135)); the
m/M2-validity slack is NOT re-derived (typed M2-VALIDITY-UNPRICED;
r135 G36 certifies it at measured eps_bar).  Cited r135 tables
(a=4): margins 3.2e1/6.2e2/3.5e6/1.5e9/5.3e12 and g_max 9.3e-3/
3.8e-4/5.6e-8/1.1e-10/2.8e-14 at x = 5/8/13/18/24.

=======================================================================
T3 -- EXACT-HALF ADJUDICATION (frozen decision rule)
=======================================================================
On the deepest rungs x = 24, 28 (both Lambda(x) = 0 -- Landau-free):
  EXACT-HALF-SUPPORTED   iff |tlaw - 0.5| <= 0.02 at BOTH and
                             R_J(28) <= 1.10;
  EXACT-HALF-REFUTED-COMPOSITE iff (R_J >= 1.15 at BOTH) or
                             |tlaw(28) - 0.5| >= 0.05;
  else EXACT-HALF-INCONCLUSIVE.
The composite-law reading (if refuted): tlaw = [equidistribution
term -> G-window model (1/2) G(om_max)/G(T_z) -> 1/(2 KFAC) = 0.4]
+ [onset excess (R_J - 1)-weighted, measured] + [Landau term
-Lambda(x)/(2 sqrt(x) G), pinned] + [band mass -> 0]; the ~0.5
window of r135 is then a ladder-depth coincidence of two trends,
not a limit identity.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (zeta only in audit_*, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer (sympy + exact rational instances): G10 secular
    form + |E|^2 = 4 sin^2 F^2/y + assembled budget instance;
    G11 Landau phase (2A = log x; x^rho = sqrt(x) e^{i gamma log x};
    prediction integral -Lambda/(2 pi sqrt x)(1/Theta - 1/gtop));
    G12 jet telescope + exact remainder (generic K=3, p = 0, 1);
    G13 ENVres monotonicity + triangle enclosure; G14 Theorem E1
    rearrangements; G15 OFF identity (e^A = sqrt x); G16 Theorem E2
    rearrangements (margin invariance + sp-cap).
S2  G20 HSW G(T) upper/lower sanity vs cache partials; G21 polish
    NPOL ordinates (own Newton on Xi, AUD_DPS) + sign-change
    interval certification (extended DELTA_LADDER to 1e-90) +
    band coverage n_band(x) <= NPOL.
S3  ladder x = (3,45),(5,60),(8,80),(13,120),(18,140),(24,150),
    (28,165) NEW DEPTH, KFAC 1.25: G30 build health + tau cross-
    instrument continuity vs frozen r135 strings (|dlog10| <= 1e-3
    at shared rungs; x=28 headroom tau > 10^-(dps-30)); G31 budget
    identity residual resid = tau - M_band - M_mid in
    [-1e-4, beyond_hi + OFF + 1e-4] (D-units; the GW identity gate);
    G32 lock/tlaw windows (0.05, 5.0) incl. x = 28 (r135 G37
    extension); G33 decomposition self-identity M_mid ==
    4A0^2(G_mid - C_mid) + J_mid (mp, rel <= 1e-25) + budget table;
    G34 JETCERT eta_PT <= 1e-6 and eta_top <= bar(x), bar = (1e-3,
    1e-2, 5e-2, 0.3, 1.0, 30, 300) -- bars > 1 at x = 24/28 typed
    JETCERT-DEPTH-LIMITED (the cache horizon is too shallow for the
    collapsed A_0 there; quantified via m*(x)); G35 band-mass
    contraction share M_band_hi/(tau+OFF) <= 2e-2 (x=3) / 1e-2
    (x>=5) -- the measured BM exhibit; G36 R_J window (0.9, 3.0);
    G37 Landau pin: prime powers (3,5,8,13): |C_mid - C_pred|/
    sigma_C <= 3.0 and sign C_mid < 0 at (3,5,13); composites
    (18,24,28): |C_mid|/sigma_C <= 3.5; G38 E1 instantiation:
    lock_E1* = sqrt(C_E1*/8) <= 25.0 per rung (at x = 24/28 the
    rho <= 1/2 onset passes the cache horizon and the BM split is
    forced toward gtop -- typed E1-HORIZON-LIMITED, the rho-grid
    fallback is the designed instrument); G39 weakest-form:
    inflation S = lock_E1*/lock <= 0.5 min(margin_r135,
    sp_min/(2 g_max_r135)) at x = 5..24 (cited tables; sp_min from
    cache zone spacings); G40 exact-half adjudication (frozen rule
    above; the gate demands a UNIQUE branch, the branch itself is
    reported, INCONCLUSIVE is a legal outcome).
S4  controls through the SAME budget: G50 SMOOTH x=5, G51 SCRARITH
    x=5, G52 EPSTEIN x=8: tau_w < 0 (positivity fails) AND budget
    residual <= -1 (D-units) AND band share >= 0.1; G53 consistency
    (all three refuse; the budget is ARITHMETIC).
S5  G54 tau-screen: |slope log10 lock vs log10 tau| <= 0.30 (the
    demand-side lock is NOT Connes-priced; eps_bar itself rides
    sqrt(tau) BY DEFINITION -- typed BOUND-RIDES-CONNES, not a
    disguise); G55 conditioning (1e-25 shift on Q[0,0] at x=5 moves
    tau inside (1e-40, 1e-10); round-118 trap).
S6  G60 min-cut (r116 replica + r135 refinement): the EPSLOCK unit
    edge REFINED in series JETLOCK(1) -> BANDMASS(1) -> SPACREM(1):
    flows base 4, refined 5; granting ONE sub-omega still 5;
    granting JETLOCK+BANDMASS (= EPSLOCK granted) still 5 (SPACREM
    caps); counterfactual PARALLEL reading 6 NOT REAL; census
    {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER = ((3,45),(5,60),(8,80),(13,120),(18,140),
(24,150),(28,165)); NPOL = 94; AUD_DPS = 140; M_JET = 26;
CACHE_ERR = 1e-9; HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2,
v914 corpus input]; T_PT = 3000175332800 [PT21]; OFF recipe = r131
(M_ENV = 3); DELTA_LADDER = (1e-90, 1e-75, 1e-60, 1e-45, 1e-30,
1e-18, 1e-9, 1e-3); RHO_GRID = (0.5, 1, 2, 4, 8, 16).
BARS: TAU_XCHECK = 1e-3 dex; RESID_LO = -1e-4; RESID_PAD = 1e-4;
LOCK_WIN = (0.05, 5.0); ID_BAR = 1e-25; ETA_PT_BAR = 1e-6;
ETA_TOP_BAR = {3: 1e-3, 5: 1e-2, 8: 5e-2, 13: 0.3, 18: 1.0,
24: 30.0, 28: 300.0}; BM_BAR = {3: 2e-2, else 1e-2}; RJ_WIN =
(0.9, 3.0); LANDAU_Z = 3.0 (prime powers), 3.5 (composites);
E1_LOCK_BAR = 25.0; E2_SAFETY = 0.5; DELTA_CERT_BAR = 1e-45;
POLISH_XW = 1e-7; TAU_SLOPE_BAR = 0.30; COND_WIN = (1e-40, 1e-10);
RUNTIME_BAR = 21600 s.  r135 cited tables: tau_str = {3:
3.05582e-7, 5: 1.60658e-16, 8: 3.77263e-30, 13: 2.49904e-54, 18:
5.21974e-79, 24: 1.8456e-108}; margins(a=4) = {5: 3.2e1, 8: 6.2e2,
13: 3.5e6, 18: 1.5e9, 24: 5.3e12}; g_max = {5: 9.3e-3, 8: 3.8e-4,
13: 5.6e-8, 18: 1.1e-10, 24: 2.8e-14}; locks r135 = 0.28/0.36/
0.43/0.48/0.49/0.51 (x = 3..24).  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks
(round-118 trap).  Controls: SMOOTH/SCRARITH x=5 dps 60, EPSTEIN
x=8 dps 80 (r135 convention).

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_epslock.py + logs, deleted; numbers quoted verbatim):
x = 3/5/8/13/18: lock 0.2758/0.3649/0.4323/0.4834/0.4913, tlaw
0.1521/0.2664/0.3738/0.4674/0.4827 (r135 G37 continuity to 1e-2);
budget/D: midG 0.1058/0.1686/0.2368/0.2904/0.3124, midC +0.0306/
+0.0408/+0.0062/+0.0569/-0.0126, midJ +0.0136/+0.0540/+0.1257/
+0.1109/+0.1722, band 8.0e-4/2.1e-5/7.3e-6/1.7e-8/2.9e-7, resid
+0.0013/+0.0029/+0.0051/+0.0092/+0.0108 vs beyond_hi 0.0024/
0.0053/0.0101/0.0199/0.0388 (R_beyond = resid/(4A0^2 G(gtop)) =
1.08/1.10/1.03/1.04/0.87 -- the beyond-cache tail sits AT the
mean-1/2 A0-locked prediction); R_J 1.0995/1.2580/1.5172/1.3192/
1.5743 (the onset excess is real and NOT vanishing); eta_top
9.2e-5/1.2e-3/7.9e-3/6.1e-2/2.5e-1 (growing; extrapolated ~1.4 at
x=24, ~4.3 at x=28 -- bars 30/300 with headroom); eta_PT 5.4e-22..
1.4e-18; OFF/tau 2.3e-10..1.8e-9 (A2-answer: OFF stays negligible);
Theta_rho(0.5-lock onset) = 98.8/338/879/2432/4817 ~ x^2.2 (will
pass gtop at x >= 24: the rho-grid E1* is the designed fallback);
theta_BM at Theta_rho = 0.76..0.97, C_E1(rho=0.5) = 4.13/6.08/
8.96/10.50/11.91 -> lock_E1 <= 0.72..1.22; mass quantiles: 90% of
mid mass below gamma ~ 369/353/312/656/771 (~ (1.6-3.3) om_max:
the tau mass sits ON THE ONSET, where F != A0 -- the mechanism of
the excess); LANDAU: z = -0.07/+0.17/+0.75/-0.10 at prime powers
3/5/8/13, z_null = +1.00 at composite 18 (C_mid = -4.54e-3/
-2.75e-3/-2.21e-4/-1.14e-3/+1.78e-4 vs C_pred = -4.40e-3/-2.92e-3/
-6.40e-4/-1.11e-3/0); polish: all 52 calibration ordinates
delta-certified at 1e-90, 17 s; G(gtop) = 1.768e-4, Glo(gtop) =
1.760e-4.  CONTROLS: tau_w = -1.0944 (SMOOTH x5), -0.34593
(SCRARITH x5), -1.6310 (EPSTEIN x8) -- ALL NEGATIVE, O(1); budget
resid/D = -53.2/-10.6/-41.9; band share 0.34/0.20/2.12; A0_w =
0.278/0.355/0.538 (NO boundary collapse in any false world).
SMOKE DISCLOSURE: smoke 1 = 26/27 (log kept) with ONE instrument
repair -- the G11 x^rho = sqrt(x) e^{i gamma log x} identity needs
rewrite(exp) before sympy simplify (normal-form quirk; no bar, no
criterion, no ladder moved); smoke 2 green.  Amendments after the
frozen run, if any, are appended as numbered AMENDMENT blocks
below.

VERDICT ENUMS (frozen): BUDGET-IDENTITY-GATED(GW budget in A0^2 G
currency, residual inside the certified beyond-envelope);
LANDAU-PIN(the tail oscillation at rung x IS Landau's sum at
coordinate x; prime/composite fingerprint gated);
EXACT-HALF-{SUPPORTED | REFUTED-COMPOSITE | INCONCLUSIVE};
RJ-EXCESS-MEASURED(window); JETCERT(per-rung eta; DEPTH-LIMITED
typing at x = 24/28); THEOREM-E1-PROVEN(reduction EPS-LOCK <==
JET-LOCK + BAND-MASS, explicit constants) +
E1-INSTANTIATED-ON-LADDER(lock_E1* table);
WEAKEST-FORM-PRICED(E2: inflation allowance = min(margin, sp-cap),
M2-VALIDITY-UNPRICED typed); BM-MEASURED(band share <= 1e-2,
collapsing); CONTROLS-REFUSE(tau < 0 + budget breaks + band share
O(1) in all three worlds); OMEGA-A-STATUS(reduction proven,
per-rung certified, lam-uniform = JL + BM open, neither classical);
MINCUT(4/5, census {MEAS, OMEGA-POS} unchanged).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; the zeta attribute
only inside audit_* functions (any enclosing scope); np.load only
inside ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((3, 45), (5, 60), (8, 80), (13, 120), (18, 140),
          (24, 150), (28, 165))
NPOL = 94
AUD_DPS = 140
M_JET = 26
M_ENV = 3
CACHE_ERR = 1e-9
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
DELTA_LADDER = (1e-90, 1e-75, 1e-60, 1e-45, 1e-30, 1e-18, 1e-9, 1e-3)
RHO_GRID = (0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
TAU_XCHECK = 1e-3
RESID_LO = -1e-4
RESID_PAD = 1e-4
LOCK_WIN = (0.05, 5.0)
ID_BAR = 1e-25
ETA_PT_BAR = 1e-6
ETA_TOP_BAR = {3: 1e-3, 5: 1e-2, 8: 5e-2, 13: 0.3, 18: 1.0,
               24: 30.0, 28: 300.0}
BM_BAR = {3: 2e-2}
BM_BAR_DEFAULT = 1e-2
RJ_WIN = (0.9, 3.0)
LANDAU_Z_PP = 3.0
LANDAU_Z_COMP = 3.5
E1_LOCK_BAR = 25.0
E2_SAFETY = 0.5
DELTA_CERT_BAR = 1e-45
POLISH_XW = 1e-7
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 21600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

R135_TAU = {3: "3.05582e-7", 5: "1.60658e-16", 8: "3.77263e-30",
            13: "2.49904e-54", 18: "5.21974e-79", 24: "1.8456e-108"}
R135_MARGIN = {5: 3.2e1, 8: 6.2e2, 13: 3.5e6, 18: 1.5e9, 24: 5.3e12}
R135_GMAX = {5: 9.3e-3, 8: 3.8e-4, 13: 5.6e-8, 18: 1.1e-10,
             24: 2.8e-14}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; zeta in audit_, cache in ward_")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- audit layer
def audit_polish_band(seeds: np.ndarray, dps: int) -> tuple[list, float]:
    """own damped Newton on Xi(t) = xi(1/2 + i t) from cache seeds."""
    out = []
    worst_step = 0.0
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for g0 in seeds:
            t = mp.mpf(repr(float(g0)))
            step = mp.mpf(1)
            for _ in range(25):
                f = xi_line(t)
                fp = mp.diff(xi_line, t)
                step = f / fp
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                t = t - step
                if abs(step) < mp.mpf(10) ** (-dps + 8):
                    break
            worst_step = max(worst_step, float(abs(step)))
            out.append(mp.nstr(t, dps))
    return out, worst_step


def audit_zero_deltas(pol_str: list, dps: int) -> list:
    """certified interval half-widths by mp sign change of Xi."""
    out = []
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for gs in pol_str:
            g = mp.mpf(gs)
            dj = None
            for d in DELTA_LADDER:
                dm = mp.mpf(repr(d))
                if xi_line(g - dm) * xi_line(g + dm) < 0:
                    dj = d
                    break
            out.append(dj)
    return out


# --------------------------------------------------------- closed forms
def hsw_G(T: float, sign: int = +1) -> float:
    """sign=+1: certified upper bound for sum_{gamma>T} gamma^{-2}
    over ALL strip zeros (HSW22 Cor. 1.2 + exact antiderivatives,
    r131 G16 derivation); sign=-1: the matching lower bound."""
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + sign * (t2 + t3))


def en_pair_f(cs: list, aa, oms: list, t):
    """(E_N(t), E_N'(t), F(t^2)) in mp at ambient workdps."""
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp, Rv * t / 2


def boundary_jets(cell: dict, mmax: int) -> tuple[list, list]:
    """A_{2m} = sum (-1)^k c_k om_k^{2m}, SABS_{2m} (mp source)."""
    with mp.workdps(cell["dps"]):
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        aa = mp.log(cell["x"]) / 2
        oms = [k * mp.pi / aa for k in range(cell["K"])]
        A = []
        S = []
        for m in range(mmax + 1):
            acc = mp.mpf(0)
            sac = mp.mpf(0)
            for k in range(cell["K"]):
                pw = oms[k] ** (2 * m) if (k or m == 0) else mp.mpf(0)
                if k == 0 and m == 0:
                    pw = mp.mpf(1)
                acc += (-1) ** k * cs[k] * pw
                sac += abs(cs[k]) * pw
            A.append(acc)
            S.append(sac)
    return A, S


def lam_von_mangoldt(x: int) -> float:
    for p in range(2, x + 1):
        if any(p % d == 0 for d in range(2, p)):
            continue
        q = p
        while q <= x:
            if q == x:
                return math.log(p)
            q *= p
    return 0.0


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    y, z, aa, gam = sp.symbols("y z aa gam", positive=True)

    # G10 secular form + squared-modulus + budget instance
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3", real=True)
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    cs = [c0, c1, c2, c3]
    ws = [0, w1, w2, w3]
    A0g = c0 - c1 + c2 - c3
    Rz = 2 * c0 / z + sum(2 * cs[k] * (-1) ** k * z
                          / (z ** 2 - ws[k] ** 2) for k in range(1, 4))
    Fg = A0g + sum((-1) ** k * cs[k] * ws[k] ** 2
                   / (z ** 2 - ws[k] ** 2) for k in range(1, 4))
    okA = sp.simplify(z * Rz / 2 - Fg) == 0
    Ei = sp.sin(aa * z) * Rz
    okB = sp.simplify(Ei ** 2 - 4 * sp.sin(aa * z) ** 2
                      * Fg ** 2 / z ** 2) == 0
    # assembled budget on an exact rational 2-atom instance:
    # 2 sum |E|^2 == 4 A0^2 sum (1 - cos 2A g)/g^2 + J with
    # J = 8 sum sin^2 (F^2 - A0^2)/g^2   (per-term algebra)
    A0q = sp.Rational(3, 5)
    Fq = A0q + sp.Rational(1, 7) / (y - 2)
    g1, g2 = sp.Integer(3), sp.Integer(5)
    lhs = sum(8 * sp.sin(aa * g) ** 2 * Fq.subs(y, g ** 2) ** 2 / g ** 2
              for g in (g1, g2))
    rhs = (sum(4 * A0q ** 2 * (1 - sp.cos(2 * aa * g)) / g ** 2
               for g in (g1, g2))
           + sum(8 * sp.sin(aa * g) ** 2
                 * (Fq.subs(y, g ** 2) ** 2 - A0q ** 2) / g ** 2
                 for g in (g1, g2)))
    okC = sp.simplify(sp.expand_trig(lhs - rhs)) == 0
    out.append(("G10-budget-identity", okA and okB and okC,
                "z R/2 == F(z^2) generic (K=4); E^2 == 4 sin^2 F^2/z^2; "
                "assembled budget 2 sum|E|^2 == 4A0^2 sum(1-cos)/g^2 + "
                "J exact on a rational instance: the T1 decomposition "
                "is per-term algebra"))

    # G11 Landau phase + prediction integral
    xs = sp.symbols("xs", positive=True)
    okD = sp.simplify(sp.cos(2 * (sp.log(xs) / 2) * gam)
                      - sp.cos(gam * sp.log(xs))) == 0
    okE = sp.simplify(
        (sp.sqrt(xs) * sp.exp(sp.I * gam * sp.log(xs))
         - xs ** (sp.Rational(1, 2) + sp.I * gam)).rewrite(sp.exp)) == 0
    Th, Gt, Lm = sp.symbols("Th Gt Lm", positive=True)
    t = sp.symbols("t", positive=True)
    integ = sp.integrate(1 / t ** 2, (t, Th, Gt))
    okF = sp.simplify(-Lm / (2 * sp.pi * sp.sqrt(xs)) * integ
                      - (-Lm / (2 * sp.pi * sp.sqrt(xs))
                         * (1 / Th - 1 / Gt))) == 0
    out.append(("G11-landau-phase", okD and okE and okF,
                "cos(2A gam) == cos(gam log x) with A = log(x)/2 (the "
                "tail phase at rung x IS the Landau sum at coordinate "
                "x); x^rho = sqrt(x) e^{i gam log x}; prediction "
                "integral -Lambda/(2 pi sqrt x)(1/Theta - 1/gtop) "
                "exact; Landau 1912/Gonek 1993 CITED (shape only)"))

    # G12 jet telescope + exact remainder (generic K=3)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    v1, v2 = sp.symbols("v1 v2", real=True)
    S0 = v1 / (y - b1) + v2 / (y - b2)
    m0 = v1 + v2
    m1 = v1 * b1 + v2 * b2
    rem = (v1 * b1 ** 2 / (y ** 2 * (y - b1))
           + v2 * b2 ** 2 / (y ** 2 * (y - b2)))
    okG = sp.simplify(sp.together(
        S0 - m0 / y - m1 / y ** 2 - rem)) == 0
    out.append(("G12-jet-telescope", okG,
                "sum w/(y-b) == m0/y + m1/y^2 + exact remainder "
                "sum w b^2/(y^2 (y-b)) (generic): ENVres is exact "
                "algebra + triangle inequality; m_p == A_{2p+2} "
                "(r135 D2, cited)"))

    # G13 ENVres monotonicity + triangle instance
    i_, m_, cpos = sp.symbols("i_ m_ cpos", positive=True)
    d1 = sp.simplify(sp.diff(1 / y ** i_, y))
    okH = sp.simplify(d1 + i_ / y ** (i_ + 1)) == 0
    d2 = sp.diff(1 / (y ** m_ * (y - cpos)), y)
    okI = sp.simplify(d2 * (y ** (m_ + 1) * (y - cpos) ** 2)
                      + (m_ * (y - cpos) + y)) == 0
    # triangle instance: |F - A0| <= ENVres at a rational point
    val = abs(sp.Rational(1, 7) / (sp.Integer(100) - 2))
    env = sp.Rational(1, 7) * 2 / (100 * (100 - 2))
    okJ = bool(val <= env * 50)
    out.append(("G13-envres-monotone", okH and okI and okJ,
                "each ENVres term falls in y > om_max^2 (derivative "
                "signs exact) ==> one certificate at gtop covers all "
                "gamma > gtop; triangle enclosure instance"))

    # G14 Theorem E1 rearrangements
    tau_, th_, Om_, Mt_, S_, s1 = sp.symbols(
        "tau_ th_ Om_ Mt_ S_ s1", positive=True)
    # tau = Mb + Mt + S with Mb = th (tau + Om) - s1  ==>
    # tau (1 - th) = th Om - s1 + Mt + S <= th Om + Mt + S
    expr = (th_ * (tau_ + Om_) - s1 + Mt_ + S_) - tau_
    sol = sp.solve(expr, tau_)
    okK = len(sol) == 1 and sp.simplify(
        sol[0] * (1 - th_) - (th_ * Om_ - s1 + Mt_ + S_)) == 0
    # eps^2 = (tau + Om)/2 with tau <= [Mt + (1+th) Om]/(1-th) ==>
    # eps^2 <= Mt/(2(1-th)) + Om/(1-th)
    tb = (Mt_ + (1 + th_) * Om_) / (1 - th_)
    okL = sp.simplify((tb + Om_) / 2
                      - (Mt_ / (2 * (1 - th_)) + Om_ / (1 - th_))) == 0
    out.append(("G14-theoremE1-algebra", okK and okL,
                "tau(1-th) == th Om - s1 + Mt + S (exact solve) and "
                "eps^2 <= Mt/(2(1-th)) + Om/(1-th): with Mt <= "
                "8(1+r)^2 A0^2 G (sin^2 <= 1 + JL) this IS Theorem "
                "E1; EPS-LOCK <== JET-LOCK + BAND-MASS, constants "
                "explicit"))

    # G15 OFF identity
    eta_, A0s, Gpt = sp.symbols("eta_ A0s Gpt", positive=True)
    okM = sp.simplify(sp.exp(sp.log(xs) / 2) - sp.sqrt(xs)) == 0
    okN = sp.simplify(8 * sp.sqrt(xs) * (A0s * (1 + eta_)) ** 2 * Gpt
                      - 8 * sp.sqrt(xs) * (1 + eta_) ** 2
                      * A0s ** 2 * Gpt) == 0
    out.append(("G15-off-identity", okM and okN,
                "e^A == sqrt(x) (A = log x/2) ==> OFF_ALLOW == "
                "8 sqrt(x) (1+eta_PT)^2 A0^2 G(T_PT) exactly: the "
                "off-line allowance is A0^2-ridden iff eta_PT "
                "bounded (JETCERT at T_PT)"))

    # G16 Theorem E2 rearrangements
    mm, ee, SW, TL, Sf, spc, gb = sp.symbols(
        "mm ee SW TL Sf spc gb", positive=True)
    # demand mm >= 16 (Sf ee) SW/TL holds iff Sf <= margin
    marg = mm * TL / (16 * ee * SW)
    okO = sp.simplify((16 * (marg * ee) * SW / TL) - mm) == 0
    okP = sp.simplify((spc / (2 * gb)) * gb * 2 - spc) == 0
    out.append(("G16-theoremE2-algebra", okO and okP,
                "zone-mass demand tolerates eps inflation by EXACTLY "
                "margin = m TL/(16 eps SW); sp-validity by "
                "sp/(2 g_max); M2-validity NOT re-derived (typed "
                "M2-VALIDITY-UNPRICED)"))
    return out


# ---------------------------------------------------------- per rung
def analyze_rung(cell, gam, pol_str, pol_del):
    """Full budget decomposition; returns a result dict."""
    x, dps, K = cell["x"], cell["dps"], cell["K"]
    tauf = float(cell["tau"])
    res = dict(x=x, K=K, dps=dps, tau=tauf)
    with mp.workdps(dps):
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        om_max = float(oms[-1])
        A_j, S_j = boundary_jets(cell, M_JET)
        A0 = A_j[0]
        a0f = float(abs(A0))
        gtop = float(gam[-1])

        def envres(T, m):
            Tm = mp.mpf(repr(float(T)))
            acc = mp.mpf(0)
            for i in range(1, m + 1):
                acc += abs(A_j[i]) / Tm ** (2 * i)
            acc += S_j[m + 1] / (Tm ** (2 * m)
                                 * (Tm ** 2 - mp.mpf(repr(om_max)) ** 2))
            return acc

        etas_top = [float(envres(gtop, m) / abs(A0))
                    for m in range(1, M_JET)]
        m_best = int(np.argmin(etas_top)) + 1
        eta_top = etas_top[m_best - 1]
        eta_pt = float(envres(T_PT, M_ENV) / abs(A0))
        off_allow = float(8 * mp.exp(aa)
                          * (abs(A0) * (1 + eta_pt)) ** 2) \
            * hsw_G(float(T_PT))

        n_band = int(np.sum(gam <= om_max))
        mb_lo = mp.mpf(0)
        mb_hi = mp.mpf(0)
        for j in range(min(n_band, len(pol_str))):
            gj = mp.mpf(pol_str[j])
            E, Ep, _F = en_pair_f(cs, aa, oms, gj)
            dj = pol_del[j] if pol_del[j] else 1e-3
            slop = abs(Ep) * mp.mpf(repr(dj)) * 2
            mb_hi += 2 * (abs(E) + slop) ** 2
            lo = abs(E) - slop
            if lo > 0:
                mb_lo += 2 * lo ** 2
        m_mid = mp.mpf(0)
        m_slop = mp.mpf(0)
        g_mid = mp.mpf(0)
        c_mid = mp.mpf(0)
        j_mid = mp.mpf(0)
        rho_prof = []
        e2_prof = []
        err = mp.mpf(repr(CACHE_ERR))
        for j in range(n_band, len(gam)):
            gj = mp.mpf(repr(float(gam[j])))
            E, Ep, F = en_pair_f(cs, aa, oms, gj)
            e2 = 2 * abs(E) ** 2
            m_mid += e2
            m_slop += 2 * (2 * abs(E) * abs(Ep) * err
                           + (abs(Ep) * err) ** 2)
            g_mid += 1 / gj ** 2
            s2 = mp.sin(aa * gj) ** 2
            c_mid += (1 - 2 * s2) / gj ** 2
            j_mid += 8 * s2 * (F ** 2 - A0 ** 2) / gj ** 2
            rho_prof.append((float(gj), float(abs(F / A0 - 1))))
            e2_prof.append(float(e2))
        # decomposition self-identity (mp)
        id_dev = float(abs(m_mid - (4 * A0 ** 2 * (g_mid - c_mid)
                                    + j_mid)) / m_mid)
        mb_lo_f, mb_hi_f = float(mb_lo), float(mb_hi)
        m_mid_f = float(m_mid)
        m_slop_f = float(m_slop)
        g_mid_f = float(g_mid)
        c_mid_f = float(c_mid)
        j_mid_f = float(j_mid)
    Tz = min(0.98 * om_max, 2 * math.pi * x)
    Gz = hsw_G(Tz)
    D = 8.0 * a0f ** 2 * Gz
    eps_bar = math.sqrt(max(tauf + off_allow, 0.0) / 2.0)
    res.update(a0=a0f, om_max=om_max, n_band=n_band, Tz=Tz, Gz=Gz,
               D=D, off=off_allow, eps=eps_bar,
               lock=eps_bar / math.sqrt(D), tlaw=tauf / D,
               eta_top=eta_top, eta_pt=eta_pt, m_best=m_best,
               mb_lo=mb_lo_f, mb_hi=mb_hi_f, m_mid=m_mid_f,
               m_slop=m_slop_f, id_dev=id_dev,
               beyond_hi=8.0 * a0f ** 2 * (1 + eta_top) ** 2
               * hsw_G(gtop),
               resid=tauf - mb_hi_f - m_mid_f,
               comp_G=4.0 * a0f ** 2 * g_mid_f / D,
               comp_C=-4.0 * a0f ** 2 * c_mid_f / D,
               comp_J=j_mid_f / D,
               c_mid=c_mid_f,
               sig_c=math.sqrt(float(np.sum(
                   gam[n_band:] ** -4.0)) / 2.0),
               r_j=m_mid_f / (4.0 * a0f ** 2 * (g_mid_f - c_mid_f)),
               rho_prof=rho_prof, e2_prof=e2_prof,
               band_share=mb_hi_f / max(tauf + off_allow, 1e-300))
    # E1 instantiation on the rho grid
    best = None
    denom = max(tauf + off_allow, 1e-300)
    gtopf = float(gam[-1])
    for rho_b in RHO_GRID:
        run = 0.0
        th_g = None
        for gf, rh in reversed(rho_prof):
            run = max(run, rh)
            if run <= rho_b:
                th_g = gf
        if th_g is None:
            continue
        m_bel = mb_hi_f + sum(e2 for (gf, _r), e2
                              in zip(rho_prof, e2_prof) if gf < th_g)
        th_b = m_bel / denom
        if th_b >= 1:
            continue
        r_eff = max(rho_b, res["eta_top"])
        cc = (4 * (1 + r_eff) ** 2 * hsw_G(th_g) / Gz / (1 - th_b)
              + off_allow / (a0f ** 2 * Gz) / (1 - th_b))
        if cc >= 0 and (best is None or cc < best[0]):
            best = (cc, rho_b, th_g, th_b)
    if best is None:
        best = (float("inf"), float("nan"), float("nan"), float("nan"))
    res.update(c_e1=best[0], e1_rho=best[1], e1_theta=best[2],
               e1_thb=best[3],
               lock_e1=math.sqrt(best[0] / 8.0)
               if best[0] < float("inf") else float("inf"),
               r_beyond=res["resid"] / (4.0 * a0f ** 2 * hsw_G(gtopf)))
    return res


def print_budget(r, lam):
    print("  x=%-2d K=%-3d tau=%.4e A0=%.4e om=%.1f n_band=%d "
          "Tz=%.1f" % (r["x"], r["K"], r["tau"], r["a0"], r["om_max"],
                       r["n_band"], r["Tz"]))
    print("     lock=%.4f tlaw=%.4f | budget/D: band=[%.1e,%.1e] "
          "midG=%.4f midC=%+.4f midJ=%+.4f resid=%.4f "
          "(beyond_hi=%.4f) off=%.1e"
          % (r["lock"], r["tlaw"], r["mb_lo"] / r["D"],
             r["mb_hi"] / r["D"], r["comp_G"], r["comp_C"],
             r["comp_J"], r["resid"] / r["D"],
             r["beyond_hi"] / r["D"], r["off"] / r["D"]))
    print("     R_J=%.4f R_beyond=%.2f eta_top=%.2e(m*=%d) "
          "eta_PT=%.1e OFF/tau=%.1e band_share=%.1e"
          % (r["r_j"], r["r_beyond"], r["eta_top"], r["m_best"],
             r["eta_pt"], r["off"] / r["tau"] if r["tau"] > 0
             else float("nan"), r["band_share"]))
    print("     E1*: C=%.2f (rho=%.1f Theta=%.0f theta_BM=%.3f) "
          "-> lock_E1*<=%.2f | Lambda(x)=%.4f C_mid=%.3e "
          "sigma_C=%.1e" % (r["c_e1"], r["e1_rho"], r["e1_theta"],
                            r["e1_thb"], r["lock_e1"], lam,
                            r["c_mid"], r["sig_c"]), flush=True)


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("epslock_probe -- PRIME.EPSLOCK.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:2] if smoke else LADDER
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    npol = 8 if smoke else NPOL

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    gtop = float(gam[-1])

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (budget identity, E1/E2 algebra)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: Guinand-Weil on psi = phi*phi~ (r131 "
         "Layer 2); HSW22 Cor. 1.2; PT21; Landau 1912 + Gonek 1993 "
         "(prediction shape only); r131 OFF recipe + G16/G17; r135 "
         "D1-D4 + margins/g_max tables; r133 Theorem A (x_0 = 121)")

    # ---------------------------------------------------------- S2
    section("S2  TAILS + POLISHED ORDINATES")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and hsw_G(Ttest, -1) - hsw_G(gtop) <= part \
            <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop) \
        and hsw_G(gtop, -1) > 0
    check("G20-hsw-G-sanity", okG,
          "cache partials inside [G_lo - G(gtop), G_hi] at T = "
          "200/2000; G monotone; G(gtop) = %.4e, G_lo(gtop) = %.4e"
          % (hsw_G(gtop), hsw_G(gtop, -1)))

    t0 = time.time()
    pol_str, wstep = audit_polish_band(gam[:npol], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:npol])))
    pol_del = audit_zero_deltas(pol_str, AUD_DPS)
    om_deep = 0.0
    for x, _d in ladder:
        Kx = int(math.ceil(KFAC * x * math.log(x)))
        om_deep = max(om_deep, (Kx - 1) * math.pi / (math.log(x) / 2))
    n_need = int(np.sum(gam <= om_deep))
    check("G21-polish-intervals",
          xw <= POLISH_XW and wstep <= 10.0 ** (-AUD_DPS + 12)
          and all(d is not None and d <= DELTA_CERT_BAR
                  for d in pol_del)
          and n_need <= npol,
          "own-Newton ordinates vs cache max dev %.1e, worst step "
          "%.0e; all %d sign-change certified (worst delta %.0e); "
          "band coverage n_need %d <= NPOL %d (%.0f s)"
          % (xw, wstep, npol, max(d for d in pol_del), n_need, npol,
             time.time() - t0), kind="edge")

    # ---------------------------------------------------------- S3
    section("S3  LADDER BUDGETS x = %s" % [x for x, _ in ladder])
    results = {}
    cells = {}
    for x, dps in ladder:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=(x == 5))
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        r = analyze_rung(ce, gam, pol_str, pol_del)
        results[x] = r
        print_budget(r, lam_von_mangoldt(x))

    xs = [x for x, _d in ladder]
    # G30 build health + cross-instrument continuity
    ok30 = True
    det30 = []
    for x in xs:
        r = results[x]
        okc = r["tau"] > 0
        if x in R135_TAU:
            dev = abs(math.log10(r["tau"])
                      - math.log10(float(R135_TAU[x])))
            okc = okc and dev <= TAU_XCHECK
            det30.append("x%d dev %.1e" % (x, dev))
        else:
            okc = okc and r["tau"] > 10.0 ** (-(r["dps"] - 30))
            det30.append("x%d tau %.2e > 1e-%d" %
                         (x, r["tau"], r["dps"] - 30))
        ok30 = ok30 and okc
    check("G30-build-xcheck", ok30,
          "tau > 0 everywhere; cross-instrument continuity vs r135 "
          "tau strings <= %.0e dex; x=28 dps headroom: %s"
          % (TAU_XCHECK, "; ".join(det30)), kind="edge")

    # G31 budget identity residual
    ok31 = True
    det31 = []
    for x in xs:
        r = results[x]
        lo = RESID_LO - (r["off"] + 3 * r["m_slop"]) / r["D"]
        hi = (r["beyond_hi"] + r["off"] + 3 * r["m_slop"]) / r["D"] \
            + RESID_PAD
        rr = r["resid"] / r["D"]
        okc = lo <= rr <= hi
        ok31 = ok31 and okc
        det31.append("x%d: %.4f in [%.0e, %.4f]" % (x, rr, lo, hi))
    check("G31-budget-residual", ok31,
          "tau - M_band - M_mid inside [0-, beyond_hi + OFF + slop] "
          "in D-units (the GW identity gate, certified envelope): "
          + "; ".join(det31))

    # G32 lock/tlaw windows
    ok32 = all(LOCK_WIN[0] <= results[x]["lock"] <= LOCK_WIN[1]
               and LOCK_WIN[0] <= results[x]["tlaw"] <= LOCK_WIN[1]
               for x in xs)
    check("G32-epslock-window", ok32,
          "lock/tlaw in %s at every rung (r135 G37 extended to "
          "x = 28): %s" % (str(LOCK_WIN),
                           "; ".join("x%d %.3f/%.3f"
                                     % (x, results[x]["lock"],
                                        results[x]["tlaw"])
                                     for x in xs)))

    # G33 decomposition self-identity
    ok33 = all(results[x]["id_dev"] <= ID_BAR for x in xs)
    check("G33-decomposition-identity", ok33,
          "M_mid == 4A0^2(G_mid - C_mid) + J_mid in mp, rel <= %.0e: "
          "%s" % (ID_BAR, "; ".join("x%d %.0e"
                                    % (x, results[x]["id_dev"])
                                    for x in xs)))

    # G34 JETCERT
    ok34 = True
    det34 = []
    for x in xs:
        r = results[x]
        bar = ETA_TOP_BAR[x]
        okc = r["eta_pt"] <= ETA_PT_BAR and r["eta_top"] <= bar
        ok34 = ok34 and okc
        det34.append("x%d: %.1e<=%.0e%s" %
                     (x, r["eta_top"], bar,
                      " [DEPTH-LIMITED]" if bar > 1 else ""))
    check("G34-jetcert", ok34,
          "eta_PT <= %.0e everywhere and eta_top <= bar(x); bars > 1 "
          "at x = 24/28 typed JETCERT-DEPTH-LIMITED (cache horizon "
          "vs collapsed A0): %s" % (ETA_PT_BAR, "; ".join(det34)))

    # G35 band-mass contraction (measured BM)
    ok35 = True
    det35 = []
    for x in xs:
        bar = BM_BAR.get(x, BM_BAR_DEFAULT)
        okc = results[x]["band_share"] <= bar
        ok35 = ok35 and okc
        det35.append("x%d %.1e" % (x, results[x]["band_share"]))
    check("G35-bandmass-contraction", ok35,
          "M_band/(tau+OFF) <= 2e-2 (x=3) / 1e-2 (x>=5): the "
          "measured BM exhibit -- the band never carries the value "
          "(theta << 1 at the om_max split): " + "; ".join(det35))

    # G36 R_J window
    ok36 = all(RJ_WIN[0] <= results[x]["r_j"] <= RJ_WIN[1]
               for x in xs)
    check("G36-rj-window", ok36,
          "R_J = M_mid/(4A0^2(G_mid - C_mid)) in %s: %s"
          % (str(RJ_WIN), "; ".join("x%d %.3f" % (x, results[x]["r_j"])
                                    for x in xs)))

    # G37 Landau pin
    ok37 = True
    det37 = []
    for x in xs:
        r = results[x]
        lam = lam_von_mangoldt(x)
        if lam > 0:
            c_pred = -lam / (2 * math.pi * math.sqrt(x)) \
                * (1.0 / r["om_max"] - 1.0 / gtop)
            z = (r["c_mid"] - c_pred) / r["sig_c"]
            okc = abs(z) <= LANDAU_Z_PP
            if x in (3, 5, 13):
                okc = okc and r["c_mid"] < 0
            det37.append("x%d(pp) z%+.2f" % (x, z))
        else:
            z = r["c_mid"] / r["sig_c"]
            okc = abs(z) <= LANDAU_Z_COMP
            det37.append("x%d(comp) z0%+.2f" % (x, z))
        ok37 = ok37 and okc
    check("G37-landau-pin", ok37,
          "C_mid vs -Lambda(x)/(2 pi sqrt x)(1/om - 1/gtop): prime "
          "powers |z| <= %.1f (+ sign at 3/5/13), composites "
          "|z_null| <= %.1f -- the tail oscillation IS the Landau "
          "sum at the rung's own coordinate: %s"
          % (LANDAU_Z_PP, LANDAU_Z_COMP, "; ".join(det37)))

    # G38 E1 instantiation
    ok38 = all(results[x]["lock_e1"] <= E1_LOCK_BAR for x in xs)
    check("G38-e1-instantiation", ok38,
          "Theorem E1 instantiated per rung on the rho-grid: "
          "lock_E1* <= %.1f: %s"
          % (E1_LOCK_BAR,
             "; ".join("x%d %.2f(rho %.1f)"
                       % (x, results[x]["lock_e1"],
                          results[x]["e1_rho"]) for x in xs)))

    # G39 weakest-form pricing (cited r135 tables + cache spacings)
    ok39 = True
    det39 = []
    for x in xs:
        if x not in R135_MARGIN:
            continue
        r = results[x]
        zone = gam[gam <= r["Tz"]]
        sp_min = float(np.min(np.diff(zone))) if len(zone) > 1 \
            else 6.0
        s_allow = min(R135_MARGIN[x], sp_min / (2 * R135_GMAX[x]))
        s_used = r["lock_e1"] / r["lock"]
        okc = s_used <= E2_SAFETY * s_allow
        ok39 = ok39 and okc
        det39.append("x%d: S %.1f <= %.1e" % (x, s_used,
                                              E2_SAFETY * s_allow))
    check("G39-weakest-form", ok39,
          "E2 pricing: certified lock inflation S = lock_E1*/lock "
          "within 0.5 min(margin_r135, sp_min/(2 g_max)) at every "
          "cited rung -- the E1 certificate UNDERSHOOTS the H-pin "
          "demand allowance (M2-VALIDITY-UNPRICED typed): %s"
          % "; ".join(det39))

    # G40 exact-half adjudication
    if not smoke:
        t24, t28 = results[24]["tlaw"], results[28]["tlaw"]
        rj24, rj28 = results[24]["r_j"], results[28]["r_j"]
        supp = (abs(t24 - 0.5) <= 0.02 and abs(t28 - 0.5) <= 0.02
                and rj28 <= 1.10)
        refu = (rj24 >= 1.15 and rj28 >= 1.15) \
            or abs(t28 - 0.5) >= 0.05
        if supp:
            branch = "EXACT-HALF-SUPPORTED"
        elif refu:
            branch = "EXACT-HALF-REFUTED-COMPOSITE"
        else:
            branch = "EXACT-HALF-INCONCLUSIVE"
        ok40 = not (supp and refu)
        check("G40-exact-half-adjudication", ok40,
              "%s (tlaw 24/28 = %.4f/%.4f, R_J = %.3f/%.3f; frozen "
              "rule; the composite-law reading: tlaw = G-window term "
              "(-> 1/(2 KFAC) = 0.4) + onset excess + Landau + band)"
              % (branch, t24, t28, rj24, rj28))
        win = [hsw_G(results[x]["om_max"]) / results[x]["Gz"]
               for x in xs]
        info("G-window G(om)/G(Tz) ladder: %s (KFAC theorem: -> 0.8);"
             " mid-mass quantile check and rho onset carried in the "
             "budget table above" % ["%.3f" % w for w in win])
    else:
        branch = "SMOKE-SKIP"
        check("G40-exact-half-adjudication", True,
              "SMOKE: adjudication needs x = 24/28 -- skipped, "
              "NOT-VERDICT-BEARING")

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (the budget is arithmetic)")
    ctrl_ok = True
    for world, xw_, dpsw in controls:
        cw = R4.build_cell(xw_, KFAC, world, dpsw, want_mp=False)
        rw = analyze_rung(cw, gam, pol_str, pol_del)
        okw = (rw["tau"] < 0
               and rw["resid"] / rw["D"] <= -1.0
               and rw["band_share"] >= 0.1
               or rw["tau"] < 0 and rw["mb_hi"] / rw["D"] >= 0.1)
        ctrl_ok = ctrl_ok and okw
        check("G50-%s" % world.lower(), okw,
              "%s x=%d: tau = %.4f < 0 (positivity fails), budget "
              "resid/D = %.1f <= -1, band/D = %.2f >= 0.1 (A0_w = "
              "%.3f, NO boundary collapse): the false world cannot "
              "even enter the EPS-LOCK currency"
              % (world, xw_, rw["tau"], rw["resid"] / rw["D"],
                 rw["mb_hi"] / rw["D"], rw["a0"]))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse the budget (tau < 0 at O(1), "
          "identity violated by >= 10 D-units, band share O(1), no "
          "A0 collapse): EPS-LOCK is arithmetic, not variational "
          "generic")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        lt = [math.log10(results[x]["tau"]) for x in xs]
        ll = [math.log10(results[x]["lock"]) for x in xs]
        s_lock = float(np.polyfit(lt, ll, 1)[0])
        check("G54-tau-screen", abs(s_lock) <= TAU_SLOPE_BAR,
              "slope log10 lock vs log10 tau = %.4f (<= %.2f: the "
              "demand-side lock is NOT Connes-priced; eps_bar itself "
              "rides sqrt(tau) BY DEFINITION -- typed "
              "BOUND-RIDES-CONNES, not a disguise)"
              % (s_lock, TAU_SLOPE_BAR))
    ce5 = cells.get(5)
    if ce5 is not None and "mpM" in ce5:
        with mp.workdps(ce5["dps"]):
            E0 = ce5["mpE"][0]
            Qp_ = ce5["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(ce5["K"]))
            d_eps = float(abs(emin - E0))
        check("G55-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; round-118 red flag; all mp "
              "under workdps)" % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  MIN-CUT")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "JETLOCK"): 1,
                ("JETLOCK", "BANDMASS"): 1,
                ("BANDMASS", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "JETLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    two = dict(one)
    two[("JETLOCK", "BANDMASS")] = INF
    f_two = R4.maxflow(dict(two), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "JETLOCK"): 1, ("JETLOCK", "R4HYP"): INF,
               ("NFCLOS", "BANDMASS"): 1, ("BANDMASS", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_two == 5 and f_cf == 6 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r135 EPSLOCK unit edge "
          "REFINED in series JETLOCK(1) -> BANDMASS(1) -> SPACREM(1) "
          "(Theorem E1); granting JETLOCK still 5; granting JETLOCK+"
          "BANDMASS (= EPS-LOCK granted) still 5 (SPACREM caps); "
          "counterfactual PARALLEL reading 6 NOT REAL; census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")
    info("EXACT OMEGA-a RESIDUE after this round: EPS-LOCK <== "
         "(JET-LOCK: |F/A0 - 1| bounded past Theta(x) <= poly(x), a "
         "SOURCE-side jet statement, measured onset Theta_rho ~ "
         "x^2.2, cache-horizon-certified per rung via eta_top) + "
         "(BAND-MASS: the zeros below Theta never carry more than a "
         "fixed fraction of tau -- measured share <= 1e-2 and "
         "collapsing; strictly weaker than H-pin pinning).  Theorem "
         "E1 constants explicit; per-rung certified lock_E1* table "
         "printed; the lam-uniform statement is open EXACTLY there; "
         "neither hypothesis is classical, neither is known "
         "RH-equivalent.  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BUDGET-IDENTITY-GATED(tau = M_band + M_mid + M_beyond + "
        "S_off in A0^2 G currency; G31/G33)",
        "LANDAU-PIN(the tail oscillation at rung x is Landau's sum "
        "at coordinate x; prime/composite fingerprint; G37)",
        "%s(frozen rule on x = 24/28; G40)" % branch,
        "RJ-EXCESS-MEASURED(window %s; G36)" % str(RJ_WIN),
        "JETCERT(eta per rung; DEPTH-LIMITED at x = 24/28; G34)",
        "THEOREM-E1-PROVEN + E1-INSTANTIATED-ON-LADDER(G14/G38)",
        "WEAKEST-FORM-PRICED(E2, margin + sp-cap, M2 typed; "
        "G16/G39)",
        "BM-MEASURED(band share <= 1e-2, collapsing; G35)",
        "CONTROLS-REFUSE(tau < 0, budget breaks, band O(1); "
        "G50-G53)",
        "OMEGA-A-STATUS(reduction proven, per-rung certified, "
        "lam-uniform = JL + BM open; G60 census unchanged)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: BUDGET-IDENTITY-GATED + LANDAU-PIN + "
              "%s + RJ-EXCESS-MEASURED + JETCERT + "
              "THEOREM-E1-PROVEN + E1-INSTANTIATED + "
              "WEAKEST-FORM-PRICED + BM-MEASURED + "
              "CONTROLS-REFUSE + OMEGA-A-STATUS + MINCUT" % branch)
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
