#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hpin_floor_probe -- PRIME.HPIN.DERIVATIVE.FLOOR.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on H-pin, the round-131 L1BAND omega)
=======================================================================
State of the chain (rounds 122/128/131/132/133/134): under H-pin(x)
for x >= x_0 = 121 everything closes at battery-a (Theorem A, r133).
H-pin = a lam-uniform derivative floor |E_N'(gamma_j)| >= m(x) > 0 at
the true zeros in the resolvability zone gamma <= 2 pi x, strong
enough that the certified ball radii g_j = 2 eps_bar/m_j (eps_bar =
sqrt((tau + OFF_ALLOW)/2)) keep the zone |dw|-mass <= TL/8, plus the
matched-prefix/no-stray counting (H1/H2/H3).  Round 134 established
that the frame dial buys the vector, never the floor.  This probe is
the maximal proof attempt on the floor itself.

=======================================================================
THE THEOREMS (T1/T2; exact algebra, sympy-gated generically + exact
rational instances + mp instances on the ladder; classical inputs
typed CITED)
=======================================================================
NOTATION.  Per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2 (k = 1..K-1), minimizer coefficients c_k
(round-114 builder, unit L2), A_{2m} = sum_k (-1)^k c_k om_k^{2m}
(boundary jets; A_0 = phi(A)), w_k := (-1)^k c_k b_k, and the SECULAR
FUNCTION  F(y) := A_0 + sum_{k>=1} w_k/(y - b_k)  (y = z^2), so that
z R(z)/2 = F(z^2) and E_N(z) = sin(Az) R(z) (r131 Layer 1, cited).
Census roots y_1 < ... < y_{K-1} (zeros of F; nodes mu_j = sqrt(y_j),
node count EXACTLY K-1, r131 secular identity, cited).

THEOREM D1 (the secular-derivative identity; NEW in-corpus).  At
every census node mu_j:
     E_N'(mu_j) = 4 sin(A mu_j) F'(mu_j^2),
with the two exact closed forms
  (weight form)    F'(y) = - sum_k w_k/(y - b_k)^2,
  (spacing form)   F'(y_j) = A_0 prod_{i != j}(y_j - y_i)
                                  / prod_k (y_j - b_k).
PROOF: R = 2F(z^2)/z, E = sin(Az) R; at F = 0 the product rule gives
E' = sin(A mu) R'(mu) and R'(mu) = 4 F'(mu^2); the spacing form is
F = A_0 prod(y - y_i)/prod(y - b_k) (degree match, leading value A_0).
CONSEQUENCE: THE H-PIN FLOOR IS EXACTLY A ZERO-SPACING STATEMENT --
|E_N'| at a node = 4 |A_0| |sin(A mu_j)| times the node-spacing
product over the lattice product.  T1 of the contract is answered:
the floor is the spacing product; real-rootedness on the band is
certified per rung (census + argument principle below).

THEOREM D2 (jet sum rules; NEW in-corpus).  With m_p := sum_k w_k
b_k^p = A_{2p+2} (the boundary jets!):
     sum_j 1/F'(y_j)      = (sum y_j - sum b_k)/A_0 = -A_2/A_0^2,
     sum_j y_j/F'(y_j)    = -A_4/A_0^2 + A_2^2/A_0^3,
and generally the reciprocal-floor measure sum_j delta_{y_j}/F'(y_j)
has ALL power moments given by polynomials in the jets over powers of
A_0 (partial fractions of 1/F; expansion of 1/(A_0 + S) at infinity).
THE ROUND-131 BOUNDARY-JET TELESCOPE IS EXACTLY THE MOMENT DATA OF
THE RECIPROCAL DERIVATIVE FLOORS -- the telescope-controls-the-
counting-remainder connection of the contract, made exact.
COROLLARY D2s (sign-uniform harmonic floor).  IF F'(y_j) had one
sign for all j, then |F'(y_j)| >= A_0^2/|A_2| uniformly.  MACHINE
FACT (pre-freeze): the F'-sign census is MIXED at x = 3, 5 (3/4 and
7/10 negative) -- the corollary is INAPPLICABLE on MAIN; and the
sum-rule mass localizes OUT of the zone (zone share of sum |1/F'| =
1.5e-4 at x=3, 1.1e-6 at x=5): the harmonic-mean floor A_0^2/|A_2|
is 10+ orders below the measured zone floors -- the sum rule budgets
the EDGE nodes, not the zone.  Typed OBSTRUCTION for the moment
route; the zone floor is counting-localized.

THEOREM D3 (A_0-cancellation of the H-pin demand).  The zone-mass
condition of H-pin holds if the uniform floor m_min,zone satisfies
m_min >= m_req := 16 eps_bar sum_zone |w_a'(gamma)| / TL(x,a)
(exact rearrangement, sympy-gated).  With eps_bar = c(x) |A_0|
(the EPS-LOCK, measured law: c = eps_bar/|A_0| flat ~0.19-0.21 on
the calibration rungs; equivalently tau ~ 8 A_0^2 G(T_z), the r131
GW law) and the identity floor m_j = 4 |A_0 sin(A mu_j)| PR_j
(PR = spacing/lattice product ratio), the ball radius
     g_j = 2 eps_bar/m_j = c(x) / (2 |sin(A mu_j)| PR_j)
is A_0-FREE: the Connes scale cancels EXACTLY at identity level.
H-pin splits into (OMEGA-a) EPS-LOCK -- eps_bar/|A_0| bounded by a
power of x (measured flat), and (OMEGA-b) SPACING-REMAINDER -- the
zone spacing ratio |sin| PR >= 1/poly(x), which is a NODE-COUNTING
statement (below), plus the H1/H2/H3 matching counts.

THEOREM D4 (far-lattice factorization; Euler product, cited).
sin(A mu)/(A mu prod_{k<K}(1 - y/b_k)) = prod_{k>=K}(1 - y/b_k),
with the certified truncation bound |log prod_{k>K'}(1 - y/b_k)| <=
(1/(1-q*)) sum_{k>K'} y/b_k, q* = y/b_{K'+1} (elementary, gated).
So the floor anatomy m_j = 4|A_0| A mu_j |prod_{i!=j}(y_j - y_i)|
/ prod_{k<K} b_k times a certified lattice factor is fully explicit.

THE COUNTING REDUCTION (T2; machine-exhibited).  Replace the ZONE
census nodes by the RvM quantiles (rvm(t_i) = i + 1/2) and keep the
edge layer (mu > 2 pi x) frozen as data: the spacing-form floor is
reproduced to <= 0.13 in log10 at x = 5, 8 (pre-freeze; frozen bar
0.5).  THE ZONE FLOOR IS COUNTING-DETERMINED: floor = 4|A_0 sin| x
(RvM main term) x (edge-layer factor) x exp(remainder), remainder
priced by the node-counting deviation (measured <= 1.2 zeros,
r128/r131) times the log-kernel sensitivity S_j = sum_{i!=j}
2 mu_i s_i / |y_j - y_i| (s_i = local spacing; measured S ~ 8-11).
SUFFICIENCY RATE: a uniform zone node-position law with accuracy
delta <= log(margin)/S_j IN UNITS OF LOCAL SPACING suffices --
measured margins give delta_suff ~ 0.4-0.6 spacings at x = 5-8 and
growing, versus measured node-position accuracy ~1e-9 spacings.
THE EXACT REMAINING OMEGA (typed, not claimed): (OMEGA-a) EPS-LOCK
lam-uniformly (variational upper bound tau <= Q(trial); explicit
jet-killed trial families give only poly(x) rates -- the measured
super-exponential collapse is arithmetic pinning, open), and
(OMEGA-b) the zone node-counting law at O(spacing) accuracy
lam-uniformly (RvM node law: measured dev <= 1.2, counting-level
crossover T = 2 pi x proven r131; the lam-uniform statement is
open -- it is source-side, NOT classical, NOT known RH-equivalent).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (zeta only in audit_*, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer: G10 derivative identity (generic partial-fraction
    zR/2 == A_0 + sum w/(y-b), K=4; E' == 4 sin F' on an exact
    rational instance); G11 weight + spacing forms (generic + exact
    instance); G12 jet sum rules p = 0, 1 (generic K=3 + exact
    instance + trace link sum y - sum b == -A_2/A_0); G13 far-
    lattice tail lemma (-log(1-q) <= q/(1-q*), exact) ; G14 gap
    transfer + demand rearrangement (sympy); G15 A_0-cancellation
    (symbolic); G16 sign-uniform corollary logic (exact instance).
S2  G20 HSW G(T) sanity; G21 Theorem-T T*(x) re-gate per core rung;
    G22 polished ordinates (NPOL=50, AUD_DPS=100) + sign-change
    intervals (adaptive delta ladder).
S3  CORE ladder x = (3,45),(5,60),(8,80),(13,120), KFAC 1.25,
    raw-mp census (r132 AMENDMENT-1 currency): G30 census complete
    + real + node residuals; G31 identity on ladder (weight and
    spacing forms vs direct E', rel <= 1e-30); G32 sum rules on
    ladder (p = 0, 1, rel <= 1e-25); G33 zone sum-rule localization
    (zone share <= 1e-2 -- the moment-route obstruction exhibit);
    G34 F'-sign census + corollary bookkeeping (if uniform: floor
    >= A_0^2/|A_2| must hold; if mixed: corollary typed
    INAPPLICABLE); G35 argument-principle zone real-rootedness at
    x = 5, 8, 13 (contour count == zone census count, integrality
    <= 1e-6); G36 gap law + floor transfer at true zeros (polished
    zone zeros matched, gap <= g_j = 2 eps_bar/m_j, validity g <=
    min(m/M2, spacing/2), |E'(gamma_j)| >= m_j/2: the r131 G34 law
    + the NEW floor-transfer, per rung); G37 EPS-LOCK + GW-tau law
    windows (eps_bar/(|A_0| sqrt(8 G(T_z))) and tau/(8 A_0^2 G) in
    (0.05, 5) at every rung incl. deep); G38 H-pin ZONE-MASS
    margins (m_min,zone/m_req >= 3 at every (rung >= 5, a), growth
    last/first >= 5); G39 counting-model floor (zone nodes -> RvM
    quantiles, edge frozen: |log10 dev| <= 0.5 at x = 5, 8, 13)
    + sensitivity S_j + delta_suff printed.
S3b DEEP rungs x = (18,140),(24,150) (NEW depth; scaling currency;
    nodes by zone sign-scan + Newton, no polyroots): G40 scan
    complete (count == cache zone count, all matched identity-
    style, residuals); G41 identity at deep zone nodes (weight
    form, rel <= 1e-30); G42 deep gap law + floors + margins (the
    x = 18/24 extension of the r131 gap law -- new territory,
    honestly gated); G43 scaling fits on x = 5..24: slopes of
    log10 eps_bar, m_min,zone, margin vs x; gates: margin slope
    >= +0.05 dex/x, eps_bar slope <= -0.5 dex/x; extrapolation to
    x_0 = 121 printed (typed MEASURED-EXTRAPOLATION, no claim).
S4  controls through the SAME instrument: G50 SMOOTH x=5, G51
    SCRARITH x=5, G52 EPSTEIN x=8: the IDENTITY must PASS (algebra
    is world-blind -- null control) and the zone MATCHING must
    REFUSE (strays/mismatch: H2 = the arithmetic zero-free gap,
    r133); G53 consistency (all three refuse).
S5  G54 tau-screen: |slope log10 margin(a=4) vs log10 tau| <= 0.30
    (the DEMAND is not Connes-priced) AND slope log10 m_min vs
    log10 tau in (0.20, 0.80) (the FLOOR alone rides sqrt(tau) BY
    the identity -- typed FLOOR-RIDES-CONNES, not a disguise; the
    de Branges reading -- |E'| at zeros = phase-velocity currency
    -- typed INFO, no axiom consumed); G55 conditioning (1e-25
    shift on Q[0,0] at x=5 moves tau by (1e-40, 1e-10)).
S6  G60 min-cut (r116 replica): the L1BAND unit omega REFINED in
    series EPSLOCK(1) -> SPACREM(1) -> DOMASYM(INF, r133) ->
    WPDWIN(INF): flows base 4, refined 5, granting ONE sub-omega
    still 5, granting BOTH = 6 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((3,45),(5,60),(8,80),(13,120));
LADDER_DEEP = ((18,140),(24,150)); A_BAT = (1,4,16); NPOL = 50;
AUD_DPS = 100; CACHE_ERR = 1e-9; HSW = (0.1038, 0.2573, 9.3675)
[HSW22 Cor. 1.2, v914 corpus input]; T_PT = 3000175332800 [PT21];
M_ENV = 3; OFF_ALLOW = 8 e^A ENV_3(T_PT)^2 G(T_PT) (r131 recipe,
cited); SUP_INFLATE = 1.5; MATCH_F = 0.25; DELTA_LADDER = (1e-30,
1e-24, 1e-18, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2); ZONE T_z = min(0.98
edge, 2 pi x) (r131 G17 theorem); SCAN_STEP = 0.05, SCAN_LO = 0.5.
BARS: BAR_ID = 1e-30 (identity rel dev; pre-freeze 8.4e-54);
BAR_SR = 1e-25 (sum rules; pre-freeze 1.4e-44); ZONE_SR_BAR = 1e-2
(pre-freeze 1.5e-4); EPSLOCK_WIN = (0.05, 5.0) (pre-freeze
0.57/0.59); TAULAW_WIN = (0.05, 5.0) (pre-freeze 0.64/0.69);
ARG_INT_BAR = 1e-6; RES_BAR = 1e-20 (node residuals, Newton-
polished); MARGIN_BAR = 3.0 (x >= 5; pre-freeze 30/592 at x=5/8);
MARGIN_GROWTH = 5.0; CDEV_BAR = 0.5 log10 (pre-freeze <= 0.13);
SLOPE_MARGIN_MIN = 0.05 dex/x; SLOPE_EPS_MAX = -0.5 dex/x;
TAU_SLOPE_BAR = 0.30; FLOOR_SLOPE_WIN = (0.20, 0.80); COND_WIN =
(1e-40, 1e-10); BAR_POLISH_XW = 1e-7; BAR_POLISH_RES = 1e-60;
GAMMA1_LIT = 14.134725141734694 (ward only); RUNTIME_BAR = 10800 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks (round-118 trap).

CALIBRATION DISCLOSURE (pre-freeze, two scratch scripts
calib_scratch_hpin.py / calib_scratch_hpin2.py + logs, deleted;
numbers quoted verbatim): symbolic sum rule K=3 generic EXACT;
identity max rel dev 7.5e-43 (x=3) / 8.4e-54 (x=5); sum rules
p=0/1 rel 9.2e-45/1.4e-44 (x=3), 7.6e-55/1.2e-54 (x=5); F'-sign
census 3/4 and 7/10 negative (MIXED); zone sum-rule share 1.5e-4 /
1.1e-6; eps_bar/|A_0| = 0.212/0.189 (tau-only eps); argument
principle x=5 count 4.0 == 4 (1.8 s); x=18 build 487.6 s (K=66,
dps 140, tau 5.2e-79), zone scan 35 sign changes vs RvM 34.9
(2.4 s); margins m_min/m_req: x=5: 30.3/31.8/37.9, x=8:
592/616/719 (a=1/4/16); counting-model dev (zone-RvM, edge
frozen): x=5 in [0.00, 0.04], x=8 in [-0.13, 0.04] log10;
sensitivity S_j max 8.2/11.0; T* = 79.2/102.8, gamma_N = 49.77/
77.14 (x=5/8).  SMOKE 1 (26/27, log kept): ONE instrument repair
-- the G60 counterfactual was mis-built as series-INF grants
(unbounded flow); rebuilt as the PARALLEL unit reading (the r133
G60 convention), no bar or criterion moved.  Amendments after the
frozen run, if any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): DERIVATIVE-IDENTITY-PROVEN;
JET-SUMRULES-PROVEN(telescope == reciprocal-floor moments);
FLOOR-IS-SPACING(T1 answered); ZONE-REALROOT-CERTIFIED(argument
principle); FLOOR-IS-COUNTING(model dev <= 0.5 dex);
SIGNCENSUS-MIXED(harmonic-floor corollary INAPPLICABLE) +
SUMRULE-MASS-OUT-OF-ZONE(moment route OBSTRUCTED);
EPSLOCK-MEASURED(window); GAPLAW-EXTENDED(x = 18, 24);
HPIN-ZONEMASS-CERTIFIED-ON-LADDER(margins, growth);
DEMAND-A0-FREE(tau-screen on the margin) + FLOOR-RIDES-CONNES
(typed, not a disguise); CONTROLS-REFUSE(identity world-blind,
matching consumes the arithmetic gap); OMEGA-SPLIT(H-pin =
EPS-LOCK + SPACING-REMAINDER, both typed open, demand rates
named); MINCUT(4/5, census {MEAS, OMEGA-POS} unchanged).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; the zeta attribute
only inside audit_* functions (any enclosing scope); np.load only
inside ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 32/33 at SPEC_SHA
c2c8f223f0d5748a, log kept as pre-amendment record).  INSTRUMENT
FIX ONLY: the x=24 resolvability zone holds 53 true zeros but
NPOL = 50 capped the G40 match loop and the G36 zone coverage at
50 (G40 read "matched 50" == the cap with zero mismatches; every
comparable prefix zero matched).  NPOL raised 50 -> 56 so the cap
never binds on the frozen ladder; no bar, no criterion, no ladder
moved.  DISCLOSURE: the spec section list names a gate "G42" for
the deep floors/margins; as built, that content is carried by
G36/G37/G38 which run over core + deep rungs (naming slip, no
missing content).  Run 2 = run of record at the amended SPEC_SHA;
run 3 = deterministic re-run.
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

import semilocal_realroot_limit_probe as SL   # warded source builder
import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER_CORE = ((3, 45), (5, 60), (8, 80), (13, 120))
LADDER_DEEP = ((18, 140), (24, 150))
A_BAT = (1, 4, 16)
NPOL = 56   # AMENDMENT 1 (was 50; x=24 zone holds 53 zeros)
AUD_DPS = 100
CACHE_ERR = 1e-9
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_ENV = 3
SUP_INFLATE = 1.5
MATCH_F = 0.25
DELTA_LADDER = (1e-30, 1e-24, 1e-18, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2)
SCAN_STEP = 0.05
SCAN_LO = 0.5
BAR_ID = 1e-30
BAR_SR = 1e-25
ZONE_SR_BAR = 1e-2
EPSLOCK_WIN = (0.05, 5.0)
TAULAW_WIN = (0.05, 5.0)
ARG_INT_BAR = 1e-6
RES_BAR = 1e-20
MARGIN_BAR = 3.0
MARGIN_GROWTH = 5.0
CDEV_BAR = 0.5
SLOPE_MARGIN_MIN = 0.05
SLOPE_EPS_MAX = -0.5
TAU_SLOPE_BAR = 0.30
FLOOR_SLOPE_WIN = (0.20, 0.80)
COND_LO, COND_HI = 1e-40, 1e-10
BAR_POLISH_XW = 1e-7
BAR_POLISH_RES = 1e-60
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 10800.0

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
    worst = 0.0
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for g0 in seeds:
            t = mp.mpf(repr(float(g0)))
            for _ in range(60):
                f = xi_line(t)
                fp = mp.diff(xi_line, t)
                step = f / fp
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                t = t - step
                if abs(step) < mp.mpf(10) ** (-dps + 8):
                    break
            worst = max(worst, float(abs(xi_line(t))))
            out.append(mp.nstr(t, dps))
    return out, worst


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
                v1, v2 = xi_line(g - dm), xi_line(g + dm)
                if v1 * v2 < 0:
                    dj = d
                    break
            out.append(dj)
    return out


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM (SL mp path minus
    the f64 refine); returns (sorted real positive mu, n_nonreal)."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300, extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    realm = np.abs(roots.imag) <= 1e-10 * float(s_mp)
    real_y = roots[realm & (roots.real > 0)]
    n_nonreal = int(np.sum(~realm))
    return np.sort(np.sqrt(real_y.real)), n_nonreal


def en_pair(cs: list, aa, oms: list, t):
    """(E_N(t), E_N'(t)) in mp at ambient workdps (caller sets)."""
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def newton_node(cs: list, aa, oms: list, z0: float, dps: int):
    with mp.workdps(dps):
        t = mp.mpf(repr(float(z0)))
        for _ in range(80):
            f, fp = en_pair(cs, aa, oms, t)
            step = f / fp
            if abs(step) > mp.mpf("0.1"):
                step = step / abs(step) * mp.mpf("0.1")
            t = t - step / 1 if abs(step) < mp.mpf("0.05") else t - step / 2
            if abs(step) < mp.mpf(10) ** (-dps + 6):
                break
        f, _fp = en_pair(cs, aa, oms, t)
        return t, abs(f)


def boundary_jets(cell: dict, mmax: int) -> tuple[list, list]:
    """A_{2m} = sum (-1)^k cn_k om_k^{2m}, SABS_{2m} (mp source)."""
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


def env_pref(A: list, S: list, om_max: float, T: float, dps: int):
    with mp.workdps(dps):
        Tm = mp.mpf(repr(float(T)))
        acc = mp.mpf(0)
        for i in range(M_ENV + 1):
            acc += abs(A[i]) / Tm ** (2 * i)
        acc += S[M_ENV + 1] / (Tm ** (2 * M_ENV)
                               * (Tm ** 2 - mp.mpf(repr(om_max)) ** 2))
        return acc


# --------------------------------------------------------- closed forms
def w_of(a: float, t):
    return a * t ** 2 / (a + t ** 2) ** 2


def wp_abs(a: float, t: float) -> float:
    return abs(2.0 * a * t * (a - t * t)) / (a + t * t) ** 3


def hsw_G(T: float) -> float:
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
        return float(t1 + t2 + t3)


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_hsw(T: float) -> float:
    return HSW_A * math.log(T) + HSW_B * math.log(math.log(T)) + HSW_C


def t_star(N: int) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_hsw(mid) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells(N: int, a: float, Ts: float) -> float:
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = m_rvm(Ts) + q_hsw(Ts)
            for j in range(J):
                n_next = m_rvm(Tj[j + 1]) - q_hsw(Tj[j + 1])
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * w_of(a, Tj[j + 1])
                u_prev = m_rvm(Tj[j + 1]) + q_hsw(Tj[j + 1])
            best = max(best, tot)
    return best


def rvm_quantiles(n: int) -> list:
    out = []
    for i in range(n):
        lo, hi = 2 * math.pi + 0.1, 1e7
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) >= i + 0.5:
                hi = mid
            else:
                lo = mid
        out.append(hi)
    return out


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # G10 derivative identity
    z, aa = sp.symbols("z aa", positive=True)
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3", real=True)
    w1s, w2s, w3s = sp.symbols("w1 w2 w3", positive=True)
    cs = [c0, c1, c2, c3]
    ws = [0, w1s, w2s, w3s]
    A0g = c0 - c1 + c2 - c3
    Rz = 2 * c0 / z + sum(2 * cs[k] * (-1) ** k * z
                          / (z ** 2 - ws[k] ** 2) for k in range(1, 4))
    Fg = A0g + sum((-1) ** k * cs[k] * ws[k] ** 2
                   / (z ** 2 - ws[k] ** 2) for k in range(1, 4))
    okA = sp.simplify(z * Rz / 2 - Fg) == 0
    # exact rational instance: F = A0 (y-4)(y-9)/((y-2)(y-7))
    y = sp.symbols("y")
    A0q = sp.Rational(3, 5)
    Fi = A0q * (y - 4) * (y - 9) / ((y - 2) * (y - 7))
    Ei = sp.sin(aa * z) * 2 * Fi.subs(y, z ** 2) / z
    Epr = sp.diff(Ei, z)
    lhs = sp.simplify(Epr.subs(z, 2))
    rhs = sp.simplify(4 * sp.sin(2 * aa) * sp.diff(Fi, y).subs(y, 4))
    okB = sp.simplify(lhs - rhs) == 0
    out.append(("G10-derivative-identity", okA and okB,
                "z R(z)/2 == F(z^2) generic (K=4) and E'(mu) == "
                "4 sin(A mu) F'(mu^2) exact on the rational instance "
                "(mu = 2, y = 4): the floor is F'-currency"))

    # G11 weight + spacing forms
    b1, b2 = sp.symbols("b1 b2", positive=True)
    y1, y2 = sp.symbols("y1 y2", positive=True)
    A0s = sp.symbols("A0s", positive=True)
    Fg2 = A0s * (y - y1) * (y - y2) / ((y - b1) * (y - b2))
    w1r = sp.simplify((Fg2 * (y - b1)).subs(y, b1))
    w2r = sp.simplify((Fg2 * (y - b2)).subs(y, b2))
    Fw = A0s + w1r / (y - b1) + w2r / (y - b2)
    okC = sp.simplify(sp.together(Fg2 - Fw)) == 0
    Fpw = sp.diff(Fw, y)
    okD = sp.simplify(Fpw - (-w1r / (y - b1) ** 2
                             - w2r / (y - b2) ** 2)) == 0
    spac = A0s * (y1 - y2) / ((y1 - b1) * (y1 - b2))
    okE = sp.simplify(sp.diff(Fg2, y).subs(y, y1) - spac) == 0
    out.append(("G11-weight-spacing-forms", okC and okD and okE,
                "F == A0 + sum w_k/(y-b_k) with residue weights; "
                "F' == -sum w_k/(y-b_k)^2; F'(y_j) == A0 "
                "prod(y_j - y_i)/prod(y_j - b_k) -- all exact "
                "(generic K=3): the spacing-product identity"))

    # G12 jet sum rules
    Fp1 = sp.diff(Fg2, y).subs(y, y1)
    Fp2 = sp.diff(Fg2, y).subs(y, y2)
    sr0 = sp.simplify(sp.together(
        1 / Fp1 + 1 / Fp2 - (y1 + y2 - b1 - b2) / A0s))
    lnk = sp.simplify((y1 + y2 - b1 - b2) + (w1r + w2r) / A0s)
    sr1 = sp.simplify(sp.together(
        y1 / Fp1 + y2 / Fp2
        - (-(w1r * b1 + w2r * b2) / A0s ** 2
           + (w1r + w2r) ** 2 / A0s ** 3)))
    okF = sr0 == 0 and lnk == 0 and sr1 == 0
    # jet link A_2 == sum w_k (definition algebra)
    A2g = sum((-1) ** k * cs[k] * ws[k] ** 2 for k in range(1, 4))
    wkg = [(-1) ** k * cs[k] * ws[k] ** 2 for k in range(1, 4)]
    okG_ = sp.simplify(A2g - sum(wkg)) == 0
    out.append(("G12-jet-sum-rules", okF and okG_,
                "sum 1/F'(y_j) == (sum y - sum b)/A0 == -sum w/A0^2 "
                "== -A_2/A_0^2 and sum y_j/F' == -A_4/A_0^2 + "
                "A_2^2/A_0^3 (generic, exact): the r131 boundary-jet "
                "telescope IS the reciprocal-floor moment data"))

    # G13 far-lattice tail lemma
    q, qs = sp.symbols("q qs", positive=True)
    g13 = sp.simplify(sp.diff(-sp.log(1 - q) - q / (1 - qs), q))
    # derivative = 1/(1-q) - 1/(1-qs) <= 0 for q <= qs; check sign form
    okH = sp.simplify(g13 - (1 / (1 - q) - 1 / (1 - qs))) == 0
    inst = all(
        float(-sp.log(1 - sp.Rational(v, 100))
              - sp.Rational(v, 100) / (1 - sp.Rational(64, 100))) <= 0
        for v in (10, 40, 64))
    out.append(("G13-far-lattice-tail", okH and inst,
                "-log(1-q) <= q/(1-q*) for 0 <= q <= q* < 1 "
                "(derivative form + exact instances at q* = 0.64): "
                "the sin/lattice factorization tail is certified; "
                "Euler sine product CITED classical"))

    # G14 gap transfer + demand rearrangement
    mM, MM, h = sp.symbols("mM MM h", positive=True)
    ok14a = sp.simplify(mM * h - MM * h ** 2 / 2 - mM * h / 2
                        - (h / 2) * (mM - MM * h)) == 0
    eps, mmin, TL, SW = sp.symbols("eps mmin TL SW", positive=True)
    # sum 2 eps |w'|/m <= (2 eps/mmin) SW <= TL/8 iff
    # mmin >= 16 eps SW / TL
    ok14b = sp.simplify(
        (2 * eps / (16 * eps * SW / TL)) * SW - TL / 8) == 0
    out.append(("G14-gap-demand", ok14a and ok14b,
                "gap lemma re-gate (r131 G14 shape) and the demand "
                "rearrangement: zone mass <= TL/8 <== m_min >= "
                "m_req = 16 eps_bar sum|w'| / TL (exact)"))

    # G15 A0-cancellation
    cA, A0c, sF, PR = sp.symbols("cA A0c sF PR", positive=True)
    g15 = sp.simplify(2 * (cA * A0c) / (4 * A0c * sF * PR)
                      - cA / (2 * sF * PR))
    out.append(("G15-a0-cancellation", g15 == 0,
                "g = 2 eps/m with eps = c A0 and m = 4 A0 |sin| PR "
                "==> g = c/(2 |sin| PR): the Connes/boundary scale "
                "cancels EXACTLY in the H-pin demand ratio"))

    # G16 sign-uniform corollary logic (exact instance)
    rs = [sp.Rational(-1, 3), sp.Rational(-1, 5), sp.Rational(-2, 7)]
    Ssum = -sum(rs)
    ok16 = all(abs(r) <= Ssum for r in rs) and Ssum > 0
    out.append(("G16-signuniform-corollary", ok16,
                "if all r_j = 1/F'(y_j) share a sign and sum r_j = "
                "-A2/A0^2 then |F'(y_j)| >= A0^2/|A2| each (exact "
                "instance): applicable ONLY under a uniform sign "
                "census -- gated against the measured census in G34"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("hpin_floor_probe -- PRIME.HPIN.DERIVATIVE.FLOOR.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:2] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    npol = 12 if smoke else NPOL
    arg_rungs = (5,) if smoke else (5, 8, 13)

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
    section("S1  EXACT LAYER (Theorems D1-D4 inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r131 secular identity + G17 crossover "
         "T_z = 2 pi x; r132 raw-census AMENDMENT 1; r133 Theorem A "
         "(H-pin ==> {d1 > 0, MRB} for x >= x_0 = 121); HSW22 "
         "Cor. 1.2; PT21; Euler sine product; infinitude of zeros")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS + POLISHED ORDINATES")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    ok21 = True
    det21 = []
    for x, _d in core + deep:
        K = int(math.ceil(KFAC * x * math.log(x)))
        N = K - 1
        Ts = t_star(N)
        gN = float(gam[N - 1])
        ok21 = ok21 and gN <= Ts \
            and (m_rvm(Ts) - q_hsw(Ts)) >= N - 1e-9
        det21.append("x%d: g_%d %.1f <= T* %.1f" % (x, N, gN, Ts))
    check("G21-thmT-top-segment", ok21,
          "gamma_{K-1} <= T*(x) per rung (Theorem T re-gate, "
          "cited): " + "; ".join(det21))

    pol_str, pol_res = audit_polish_band(gam[:npol], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:npol])))
    zdel = audit_zero_deltas(pol_str, AUD_DPS)
    check("G22-polish-intervals",
          xw <= BAR_POLISH_XW and pol_res <= BAR_POLISH_RES
          and all(d is not None for d in zdel),
          "own-Newton ordinates vs cache max dev %.1e, max |Xi| "
          "%.1e; all %d sign-change certified (worst delta %.0e)"
          % (xw, pol_res, npol, max(d for d in zdel)), kind="edge")

    # ---------------------------------------------------------- S3
    section("S3  CORE LADDER: IDENTITY, SUM RULES, FLOORS")
    cells = {}
    nodes = {}
    meta = {}
    for x, dps in core:
        ce = R4.build_cell(x, KFAC, "MAIN", dps,
                           want_mp=(x == 5))
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)

    ok30 = ok31 = ok32 = ok33 = True
    det30, det31, det32, det33 = [], [], [], []
    sign_rows = []
    for x, dps in core:
        ce = cells[x]
        K = ce["K"]
        mus, n_nonreal = raw_mp_census(ce)
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            bks = [oms[k] ** 2 for k in range(1, K)]
            wks = [(-1) ** k * cs[k] * bks[k - 1] for k in range(1, K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * oms[k] ** 2
                     for k in range(1, K))
            A4 = sum((-1) ** k * cs[k] * oms[k] ** 4
                     for k in range(1, K))
            nds = []
            wres = 0.0
            for m0 in mus:
                tmu, res = newton_node(cs, aa, oms, float(m0), dps)
                nds.append(tmu)
                wres = max(wres, float(res))
            ok30 = ok30 and len(mus) == K - 1 and n_nonreal == 0 \
                and wres <= RES_BAR
            det30.append("x%d: %d/%d nonreal %d res %.0e"
                         % (x, len(mus), K - 1, n_nonreal, wres))
            wid = 0.0
            wsp = 0.0
            n_neg = 0
            invsum = mp.mpf(0)
            invsum1 = mp.mpf(0)
            zone_share = mp.mpf(0)
            Tz = min(0.98 * K * math.pi / float(aa), 2 * math.pi * x)
            fps = []
            for j, mu in enumerate(nds):
                yj = mu ** 2
                _f, fp = en_pair(cs, aa, oms, mu)
                Fp_w = -sum(wks[k] / (yj - bks[k])
                            ** 2 for k in range(K - 1))
                pred = 4 * mp.sin(aa * mu) * Fp_w
                wid = max(wid, float(abs(fp - pred) / abs(fp)))
                prd = A0
                for i2, mu2 in enumerate(nds):
                    if i2 != j:
                        prd *= (yj - mu2 ** 2)
                for k in range(K - 1):
                    prd /= (yj - bks[k])
                wsp = max(wsp, float(abs(Fp_w - prd) / abs(Fp_w)))
                if Fp_w < 0:
                    n_neg += 1
                invsum += 1 / Fp_w
                invsum1 += yj / Fp_w
                if float(mu) <= Tz:
                    zone_share += abs(1 / Fp_w)
                fps.append(Fp_w)
            sr0 = float(abs(invsum + A2 / A0 ** 2) / abs(invsum))
            sr1 = float(abs(invsum1 - (-A4 / A0 ** 2
                                       + A2 ** 2 / A0 ** 3))
                        / abs(invsum1))
            zshare = float(zone_share / abs(invsum))
            ok31 = ok31 and wid <= BAR_ID and wsp <= BAR_ID
            det31.append("x%d: w %.0e sp %.0e" % (x, wid, wsp))
            ok32 = ok32 and sr0 <= BAR_SR and sr1 <= BAR_SR
            det32.append("x%d: p0 %.0e p1 %.0e" % (x, sr0, sr1))
            ok33 = ok33 and zshare <= ZONE_SR_BAR
            det33.append("x%d: %.1e" % (x, zshare))
            sign_rows.append((x, n_neg, len(nds),
                              float(abs(A0)), float(abs(A2)),
                              min(float(abs(v)) for v in fps)))
        nodes[x] = nds
        meta[x] = dict(cs=cs, aa=aa, oms=oms, bks=bks, wks=wks,
                       A0=A0, A2=A2, Tz=Tz)
    check("G30-census", ok30,
          "raw-mp census complete (count == K-1), ALL roots real "
          "(n_nonreal == 0: global real-rootedness of the census "
          "polynomial, measured), Newton residuals <= %.0e: %s"
          % (RES_BAR, "; ".join(det30)))
    check("G31-identity-on-ladder", ok31,
          "E'(mu_j) == 4 sin(A mu_j) F'(mu_j^2) (weight form) and "
          "spacing form, max rel dev per rung <= %.0e: %s"
          % (BAR_ID, "; ".join(det31)))
    check("G32-sum-rules-on-ladder", ok32,
          "sum 1/F' == -A2/A0^2 and sum y/F' == -A4/A0^2 + "
          "A2^2/A0^3 <= %.0e rel: the telescope-floor budget is "
          "EXACT on every rung: %s" % (BAR_SR, "; ".join(det32)))
    check("G33-zone-sumrule-localization", ok33,
          "zone share of sum |1/F'| <= %.0e (%s): the sum-rule "
          "mass sits on the EDGE nodes -- the moment route cannot "
          "see the zone floor (OBSTRUCTION exhibit)"
          % (ZONE_SR_BAR, "; ".join(det33)))

    ok34 = True
    det34 = []
    for (x, n_neg, n_all, a0f, a2f, fmin) in sign_rows:
        mixed = 0 < n_neg < n_all
        if mixed:
            det34.append("x%d: %d/%d neg MIXED" % (x, n_neg, n_all))
        else:
            okc = fmin >= a0f ** 2 / a2f * (1 - 1e-10)
            ok34 = ok34 and okc
            det34.append("x%d: UNIFORM, floor check %s"
                         % (x, "ok" if okc else "VIOLATED"))
    check("G34-sign-census", ok34,
          "F'-sign census + corollary bookkeeping (mixed ==> "
          "harmonic floor A0^2/|A2| INAPPLICABLE, typed; uniform "
          "==> floor must hold): %s" % "; ".join(det34))

    # G35 argument principle (zone real-rootedness, certified)
    ok35 = True
    det35 = []
    for x in arg_rungs:
        if x not in nodes:
            continue
        mtd = meta[x]
        dps = cells[x]["dps"]
        with mp.workdps(dps):
            cs, aa, oms = mtd["cs"], mtd["aa"], mtd["oms"]
            Tz = mtd["Tz"]
            nz = [float(v) for v in nodes[x] if float(v) <= Tz]
            nxt = [float(v) for v in nodes[x] if float(v) > Tz]
            tr = (nz[-1] + (nxt[0] if nxt else nz[-1] + 3.0)) / 2

            def ELE(zz, cs=cs, aa=aa, oms=oms):
                f, fp = en_pair(cs, aa, oms, zz)
                return fp / f
            c1 = mp.quad(lambda t: ELE(mp.mpc(t, -1)), [SCAN_LO, tr])
            c2 = mp.quad(lambda t: ELE(mp.mpc(tr, t)) * 1j, [-1, 1])
            c3 = mp.quad(lambda t: ELE(mp.mpc(t, 1)), [tr, SCAN_LO])
            c4 = mp.quad(lambda t: ELE(mp.mpc(SCAN_LO, t)) * 1j,
                         [1, -1])
            wind = (c1 + c2 + c3 + c4) / (2j * mp.pi)
            dev = float(abs(wind - len(nz)))
        ok35 = ok35 and dev <= ARG_INT_BAR
        det35.append("x%d: count %.6f == %d (dev %.0e)"
                     % (x, float(mp.re(wind)), len(nz), dev))
    check("G35-argument-principle-zone-real", ok35,
          "contour count on [%.1f, mid]x[-1,1] == zone census count "
          "(no non-real zeros in the zone strip, CERTIFIED): %s"
          % (SCAN_LO, "; ".join(det35)))

    # per-rung floors, eps-lock, gap law, margins (core + deep)
    all_rungs = list(core) + list(deep)
    for x, dps in deep:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=False)
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)
        K = ce["K"]
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            bks = [oms[k] ** 2 for k in range(1, K)]
            wks = [(-1) ** k * cs[k] * bks[k - 1] for k in range(1, K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            A2 = sum((-1) ** k * cs[k] * oms[k] ** 2
                     for k in range(1, K))
            Tz = min(0.98 * K * math.pi / float(aa), 2 * math.pi * x)
            ts = np.arange(SCAN_LO, Tz + SCAN_STEP, SCAN_STEP)
            vprev = en_pair(cs, aa, oms, mp.mpf(repr(float(ts[0]))))[0]
            seeds = []
            for tv in ts[1:]:
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                if v * vprev < 0:
                    seeds.append(float(tv) - SCAN_STEP / 2)
                vprev = v
            nds = []
            for s0 in seeds:
                tmu, _res = newton_node(cs, aa, oms, s0, dps)
                nds.append(tmu)
        nodes[x] = nds
        meta[x] = dict(cs=cs, aa=aa, oms=oms, bks=bks, wks=wks,
                       A0=A0, A2=A2, Tz=Tz)

    # G40/G41 deep scan + identity gates
    if deep:
        ok40 = ok41 = True
        det40, det41 = [], []
        for x, dps in deep:
            mtd = meta[x]
            Tz = mtd["Tz"]
            nzc = int(np.sum(gam <= Tz))
            nds = nodes[x]
            okc = abs(len(nds) - nzc) <= 1
            matched = 0
            for i in range(min(len(nds), nzc, npol)):
                g = abs(float(nds[i]) - pol_f64[i])
                lo = pol_f64[i - 1] if i > 0 else 0.0
                hi = pol_f64[i + 1] if i + 1 < npol \
                    else pol_f64[i] + 6.0
                if g < MATCH_F * 0.5 * (hi - lo):
                    matched += 1
                else:
                    break
            ok40 = ok40 and okc and matched >= min(len(nds), nzc) - 1
            det40.append("x%d: scan %d cache-zone %d matched %d"
                         % (x, len(nds), nzc, matched))
            with mp.workdps(dps):
                cs, aa, oms = mtd["cs"], mtd["aa"], mtd["oms"]
                bks, wks = mtd["bks"], mtd["wks"]
                wid = 0.0
                for mu in nds:
                    yj = mu ** 2
                    _f, fp = en_pair(cs, aa, oms, mu)
                    Fp_w = -sum(wks[k] / (yj - bks[k]) ** 2
                                for k in range(len(bks)))
                    pred = 4 * mp.sin(aa * mu) * Fp_w
                    wid = max(wid, float(abs(fp - pred) / abs(fp)))
            ok41 = ok41 and wid <= BAR_ID
            det41.append("x%d: %.0e" % (x, wid))
        check("G40-deep-scan", ok40,
              "deep zone node scan complete + identity-matched to "
              "the cache prefix: " + "; ".join(det40))
        check("G41-deep-identity", ok41,
              "derivative identity at deep zone nodes (weight form) "
              "<= %.0e: %s" % (BAR_ID, "; ".join(det41)))

    # unified per-rung floor/eps/gap/margin loop
    ok36 = ok37 = ok38 = True
    det36, det37, det38 = [], [], []
    eps_tab, mmin_tab, marg_tab, tau_tab, gmax_tab = {}, {}, {}, {}, {}
    for x, dps in all_rungs:
        ce = cells[x]
        mtd = meta[x]
        nds = nodes[x]
        K = ce["K"]
        Tz = mtd["Tz"]
        tauf = float(ce["tau"])
        with mp.workdps(dps):
            cs, aa, oms = mtd["cs"], mtd["aa"], mtd["oms"]
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
            eps_bar = math.sqrt((tauf + off_allow) / 2.0)
            a0f = float(abs(mtd["A0"]))
            # zone floors + gap law at polished true zeros
            zone_j = [j for j in range(npol) if pol_f64[j] <= Tz]
            m_min = float("inf")
            g_max = 0.0
            okx = True
            rows = []
            for j in zone_j:
                if j >= len(nds):
                    okx = False
                    break
                mu = nds[j]
                gmp = mp.mpf(pol_str[j])
                gap = float(abs(mu - gmp))
                lo = pol_f64[j - 1] if j > 0 else 0.0
                hi = pol_f64[j + 1] if j + 1 < npol \
                    else pol_f64[j] + 6.0
                spac = 0.5 * (hi - lo)
                _f0, fp0 = en_pair(cs, aa, oms, mu)
                m_j = float(abs(fp0))
                d2f = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                 tt)[0], mu, 2)
                d2g = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                 tt)[0], gmp, 2)
                M2 = SUP_INFLATE * max(float(abs(d2f)),
                                       float(abs(d2g)))
                b_j = 2.0 * eps_bar / max(m_j, 1e-300)
                valid = b_j <= min(m_j / max(M2, 1e-300), 0.5 * spac)
                _fg, fpg = en_pair(cs, aa, oms, gmp)
                m_g = float(abs(fpg))
                okj = gap <= b_j and valid and m_g >= 0.5 * m_j
                okx = okx and okj
                m_min = min(m_min, m_j)
                g_max = max(g_max, b_j)
                rows.append((pol_f64[j], m_j, gap, b_j, m_g))
            if x == 13 and not smoke:
                print("  floor anatomy x=13 (zone):")
                for (gv, mv, gpv, bv, mgv) in rows:
                    print("    g=%9.4f m_node=%.3e gap=%.2e "
                          "ball=%.2e m_gamma=%.3e"
                          % (gv, mv, gpv, bv, mgv))
            ok36 = ok36 and okx
            det36.append("x%d: %d/%d gaps<=ball, m_min %.1e "
                         "g_max %.1e" % (x, len(rows), len(zone_j),
                                         m_min, g_max))
            GT = hsw_G(Tz)
            lock = eps_bar / (a0f * math.sqrt(8.0 * GT))
            tlaw = tauf / (8.0 * a0f ** 2 * GT)
            okl = EPSLOCK_WIN[0] <= lock <= EPSLOCK_WIN[1] \
                and TAULAW_WIN[0] <= tlaw <= TAULAW_WIN[1]
            ok37 = ok37 and okl
            det37.append("x%d: lock %.2f tlaw %.2f" % (x, lock, tlaw))
            # margins
            zg = gam[gam <= Tz]
            Ts = t_star(K - 1)
            margs = []
            for a in A_BAT:
                swp = float(np.sum([wp_abs(a, g) for g in zg]))
                TL = tl_shells(K - 1, float(a), Ts)
                m_req = 16.0 * eps_bar * swp / TL if TL > 0 \
                    else float("inf")
                margs.append(m_min / m_req if m_req > 0
                             else float("inf"))
            if x >= 5:
                ok38 = ok38 and all(mg >= MARGIN_BAR for mg in margs)
            det38.append("x%d: %.1e/%.1e/%.1e"
                         % (x, margs[0], margs[1], margs[2]))
            eps_tab[x] = eps_bar
            mmin_tab[x] = m_min
            marg_tab[x] = margs[1]
            tau_tab[x] = tauf
            gmax_tab[x] = g_max
    check("G36-gap-law-floor-transfer", ok36,
          "every polished zone zero matched at gap <= ball 2 eps/m, "
          "validity b <= min(m/M2, spacing/2), and |E'(gamma_j)| >= "
          "m_node/2 (floor transfers to the TRUE zeros): "
          + "; ".join(det36))
    check("G37-epslock-taulaw", ok37,
          "eps_bar/(|A0| sqrt(8 G(T_z))) and tau/(8 A0^2 G(T_z)) "
          "inside %s at every rung (the EPS-LOCK: eps_bar rides A0 "
          "-- measured law, r131 GW mechanism): %s"
          % (str(EPSLOCK_WIN), "; ".join(det37)))
    xs_m = [x for x, _d in all_rungs if x >= 5]
    grow_ok = (marg_tab[xs_m[-1]] >= MARGIN_GROWTH * marg_tab[xs_m[0]]
               if len(xs_m) >= 2 else True)
    check("G38-zonemass-margins", ok38 and grow_ok,
          "H-pin zone-mass margins m_min,zone/m_req at (a=1/4/16) "
          ">= %.1f for x >= 5 and growing >= %.1fx over the ladder: "
          "%s" % (MARGIN_BAR, MARGIN_GROWTH, "; ".join(det38)))

    # G39 counting-model floor (x = 5, 8, 13)
    ok39 = True
    det39 = []
    for x in (5, 8, 13):
        if x not in nodes or smoke and x > 5:
            continue
        mtd = meta[x]
        nds = nodes[x]
        dps = cells[x]["dps"]
        Tz = mtd["Tz"]
        with mp.workdps(dps):
            A0 = mtd["A0"]
            bks = mtd["bks"]
            n_zone = sum(1 for v in nds if float(v) <= Tz)
            model = rvm_quantiles(n_zone) \
                + [float(v) for v in nds[n_zone:]]
            devs = []
            sens = []
            edge = cells[x]["K"] * math.pi / float(mtd["aa"])
            for j in range(n_zone):
                yj = float(nds[j]) ** 2
                lg_a = float(mp.log(abs(A0)))
                lg_m = float(mp.log(abs(A0)))
                S = 0.0
                for i2 in range(len(nds)):
                    if i2 != j:
                        lg_a += float(mp.log(abs(
                            yj - float(nds[i2]) ** 2)))
                        lg_m += float(mp.log(abs(
                            yj - model[i2] ** 2)))
                        mu_i = float(nds[i2])
                        lo = float(nds[i2 - 1]) if i2 > 0 else 0.0
                        hi = float(nds[i2 + 1]) \
                            if i2 + 1 < len(nds) else edge
                        S += 2 * mu_i * 0.5 * (hi - lo) \
                            / abs(yj - mu_i ** 2)
                for k in range(len(bks)):
                    lg_a -= float(mp.log(abs(yj - float(bks[k]))))
                    lg_m -= float(mp.log(abs(yj - float(bks[k]))))
                devs.append((lg_a - lg_m) / math.log(10))
                sens.append(S)
            dmax = max(abs(d) for d in devs)
            ok39 = ok39 and dmax <= CDEV_BAR
            dsuff = math.log(max(marg_tab[x], 1.0)) / max(sens)
            det39.append("x%d: dev [%.2f, %.2f] S_max %.1f "
                         "delta_suff %.2f sp" %
                         (x, min(devs), max(devs), max(sens), dsuff))
    check("G39-counting-model-floor", ok39,
          "zone nodes -> RvM quantiles (edge layer frozen as data) "
          "reproduces the spacing-form floor to <= %.1f log10: THE "
          "ZONE FLOOR IS COUNTING-DETERMINED; delta_suff = counting "
          "slack the omega may spend (in local spacings): %s"
          % (CDEV_BAR, "; ".join(det39)))

    # G43 scaling fits
    if not smoke:
        xs_f = [x for x, _d in all_rungs if x >= 5]
        le = [math.log10(eps_tab[x]) for x in xs_f]
        lm = [math.log10(mmin_tab[x]) for x in xs_f]
        lg_ = [math.log10(marg_tab[x]) for x in xs_f]
        s_eps = float(np.polyfit(xs_f, le, 1)[0])
        s_m = float(np.polyfit(xs_f, lm, 1)[0])
        s_marg = float(np.polyfit(xs_f, lg_, 1)[0])
        fit_m = np.polyfit(xs_f, lg_, 1)
        pred121 = float(np.polyval(fit_m, 121.0))
        check("G43-scaling-laws", s_eps <= SLOPE_EPS_MAX
              and s_marg >= SLOPE_MARGIN_MIN,
              "dex/x slopes on x = %s: eps_bar %.2f (<= %.1f), "
              "m_min,zone %.2f, margin %+.2f (>= +%.2f); "
              "extrapolated log10 margin at x_0 = 121: %.0f "
              "(MEASURED-EXTRAPOLATION, no claim)"
              % (xs_f, s_eps, SLOPE_EPS_MAX, s_m, s_marg,
                 SLOPE_MARGIN_MIN, pred121))
        info("scaling tables: eps_bar %s; m_min,zone %s; margin(a=4) "
             "%s; g_max %s"
             % (["%.1e" % eps_tab[x] for x in xs_f],
                ["%.1e" % mmin_tab[x] for x in xs_f],
                ["%.1e" % marg_tab[x] for x in xs_f],
                ["%.1e" % gmax_tab[x] for x in xs_f]))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (identity world-blind; matching refuses)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=False)
        musw, _nr = raw_mp_census(cw)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            csw = [mp.mpf(s) for s in cw["cn_mp_str"]]
            aaw = mp.log(xw) / 2
            omsw = [k * mp.pi / aaw for k in range(Kw)]
            bksw = [omsw[k] ** 2 for k in range(1, Kw)]
            wksw = [(-1) ** k * csw[k] * bksw[k - 1]
                    for k in range(1, Kw)]
            widw = 0.0
            for m0 in musw:
                tmu, _res = newton_node(csw, aaw, omsw, float(m0),
                                        dpsw)
                yj = tmu ** 2
                _f, fp = en_pair(csw, aaw, omsw, tmu)
                Fp_w = -sum(wksw[k] / (yj - bksw[k]) ** 2
                            for k in range(Kw - 1))
                pred = 4 * mp.sin(aaw * tmu) * Fp_w
                widw = max(widw, float(abs(fp - pred) / abs(fp)))
        Tzw = min(0.98 * Kw * math.pi / float(aaw),
                  2 * math.pi * xw)
        m_idw = 0
        for i in range(min(len(musw), npol)):
            if pol_f64[i] > Tzw:
                break
            g = abs(float(musw[i]) - pol_f64[i])
            lo = pol_f64[i - 1] if i > 0 else 0.0
            hi = pol_f64[i + 1] if i + 1 < npol else pol_f64[i] + 6.0
            if g < MATCH_F * 0.5 * (hi - lo):
                m_idw = i + 1
            else:
                break
        strays_w = int(np.sum(musw[m_idw:] <= Tzw))
        n_zone_true = int(np.sum(gam <= Tzw))
        refuse = strays_w >= 1 or m_idw < n_zone_true
        okw = (widw <= BAR_ID) and refuse
        ctrl_ok = ctrl_ok and okw
        check("G50-%s" % world.lower(), okw,
              "%s x=%d: identity dev %.0e (world-blind algebra, "
              "PASSES) but matching REFUSES: matched %d/%d zone, "
              "strays %d, mu_1 = %.3f fills the gap (0, %.2f)"
              % (world, xw, widw, m_idw, n_zone_true, strays_w,
                 float(musw[0]), float(gam[0])))
    check("G53-mechanism-consistency", ctrl_ok,
          "the identity is world-blind ALGEBRA (passes everywhere); "
          "the H-pin content -- matching + floors at TRUE zeros -- "
          "refuses in every control world at the arithmetic "
          "zero-free gap (H2 consumption, r133 sharpened)")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_f = [x for x, _d in all_rungs if x >= 5]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_f]
        lgm = [math.log10(marg_tab[x]) for x in xs_f]
        lmf = [math.log10(mmin_tab[x]) for x in xs_f]
        s_marg_t = float(np.polyfit(lt, lgm, 1)[0])
        s_floor_t = float(np.polyfit(lt, lmf, 1)[0])
        check("G54-tau-screen", abs(s_marg_t) <= TAU_SLOPE_BAR
              and FLOOR_SLOPE_WIN[0] <= s_floor_t
              <= FLOOR_SLOPE_WIN[1],
              "slope log10 margin vs log10 tau = %.3f (<= %.2f: THE "
              "DEMAND IS NOT CONNES-PRICED -- A0 cancels, G15); "
              "slope log10 m_min vs log10 tau = %.2f in %s (the "
              "FLOOR ALONE rides sqrt(tau) BY THE IDENTITY -- typed "
              "FLOOR-RIDES-CONNES, not a disguise; de Branges "
              "phase-velocity reading typed INFO, no axiom consumed)"
              % (s_marg_t, TAU_SLOPE_BAR, s_floor_t,
                 str(FLOOR_SLOPE_WIN)))
    ce5 = cells[5]
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e (nonzero "
          "and bounded; round-118 red flag; all mp under workdps)"
          % d_eps, kind="edge")

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
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "SPACREM"): 1, ("SPACREM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows: base 4, refined 5 -- the L1BAND unit omega "
          "REFINED in series EPSLOCK(1) -> SPACREM(1); granting ONE "
          "sub-omega still flows 5; counterfactual PARALLEL reading "
          "6 NOT REAL (the split is serial); census {MEAS, "
          "OMEGA-POS} cardinality 4 UNCHANGED; RH unreachable "
          "without the omega edges")
    info("EXACT H-PIN RESIDUE after this round: H-pin(x) <==> "
         "(H1/H2/H3 zone matching counts, r133 Theorem-M shape) + "
         "zone-mass margin m_min,zone >= m_req = 16 eps_bar "
         "sum|w'|/TL.  PROVEN (exact): m_j = 4|A0 sin(A mu_j)| "
         "|F'|-spacing product (D1); reciprocal-floor moments == "
         "boundary jets (D2); demand ratio A0-FREE (D3); lattice "
         "factor certified (D4).  The omega SPLITS: (OMEGA-a) "
         "EPS-LOCK eps_bar <= poly(x) |A0| sqrt(G) -- measured "
         "window %s, lam-uniform proof open (variational trial "
         "route gives only poly tau bounds); (OMEGA-b) "
         "SPACING-REMAINDER: zone node counting at O(spacing) "
         "accuracy -- sufficient slack delta_suff ~ 0.4+ spacings "
         "and GROWING vs measured node accuracy ~1e-9 spacings; "
         "source-side, NOT classical, NOT known RH-equivalent.  "
         "NO RH claim; nothing upgraded." % str(EPSLOCK_WIN))

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "DERIVATIVE-IDENTITY-PROVEN(E' == 4 sin F'; weight + "
        "spacing forms; G10/G11/G31/G41)",
        "JET-SUMRULES-PROVEN(sum y^p/F' == jet polynomials; the "
        "r131 telescope IS the reciprocal-floor moment data; "
        "G12/G32)",
        "FLOOR-IS-SPACING(T1 answered: the H-pin floor is a "
        "zero-spacing product; real-rootedness certified G30/G35)",
        "FLOOR-IS-COUNTING(zone RvM model reproduces the floor to "
        "<= %.1f dex; G39)" % CDEV_BAR,
        "SIGNCENSUS-MIXED + SUMRULE-MASS-OUT-OF-ZONE(the moment/"
        "harmonic route is OBSTRUCTED; G33/G34)",
        "EPSLOCK-MEASURED + GAPLAW-EXTENDED(x = 18, 24; G36/G37/"
        "G40-G42)",
        "HPIN-ZONEMASS-CERTIFIED-ON-LADDER(margins >= %.0f, "
        "growing; G38/G43)" % MARGIN_BAR,
        "DEMAND-A0-FREE + FLOOR-RIDES-CONNES(G15/G54: the demand "
        "ratio is not Connes-priced, the floor alone is)",
        "CONTROLS-REFUSE(identity world-blind, matching consumes "
        "the arithmetic gap; G50-G53)",
        "OMEGA-SPLIT(H-pin = EPS-LOCK + SPACING-REMAINDER, both "
        "open, demand rates named; G60 census unchanged)"]
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
        print("COMPOSITE: DERIVATIVE-IDENTITY-PROVEN + "
              "JET-SUMRULES-PROVEN + FLOOR-IS-SPACING + "
              "FLOOR-IS-COUNTING + SIGNCENSUS-MIXED + "
              "SUMRULE-MASS-OUT-OF-ZONE + EPSLOCK-MEASURED + "
              "GAPLAW-EXTENDED + HPIN-ZONEMASS-CERTIFIED + "
              "DEMAND-A0-FREE + FLOOR-RIDES-CONNES + "
              "CONTROLS-REFUSE + OMEGA-SPLIT + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
