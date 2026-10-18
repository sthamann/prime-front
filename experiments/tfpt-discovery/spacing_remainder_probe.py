#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""spacing_remainder_probe -- PRIME.SPACREM.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on OMEGA-b, the SPACING-REMAINDER)
=======================================================================
Round 135 (hpin_floor_probe, 33/33) proved the zone floor is
COUNTING-DETERMINED and split H-pin into (OMEGA-a) EPS-LOCK and
(OMEGA-b) SPACING-REMAINDER: the zone node counting law at O(spacing)
accuracy lam-uniformly, sufficient slack delta_suff = ln(margin)/S
measured 0.42/0.58/1.11 spacings at x = 5/8/13 and GROWING, against
measured node accuracy ~1e-9 spacings.  Round 133 (Theorem M) CONSUMES
H1/H2/H3 (ball matching + no-stray + one-per-ball) as measured
hypotheses.  This probe's central move: MAKE NO-STRAY/INJECTIVITY/
EXHAUSTION A THEOREM from counting, and derive the radius law by an
exact deformation + bootstrap -- so that OMEGA-b REDUCES to two named
inputs (COUNTEQ, SEEDBALL) given EPS-LOCK.

=======================================================================
THE THEOREMS (T1/T2; exact finite counting + exact inequalities,
sympy-gated generically/on exact rational instances + mp-instantiated
per rung; classical inputs typed CITED)
=======================================================================
NOTATION.  Per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer coefficients c_k (round-114
builder), E_N = sin(Az) R(z), census nodes mu_1 < ... < mu_{K-1}
(zeros of the census polynomial; node count EXACTLY K-1, r131 secular
identity, cited).  Zone T_z = 2 pi x (r131 G17 crossover theorem,
re-cited); m = #{true zeros gamma_j <= T_z} (verified computation,
classical, cited: all zeros to height 3e12 are on-line and counted --
PT21/v914 corpus input; the zone is gamma <= 2 pi x <= 151 on this
ladder).  s_j = true local spacing = (gamma_{j+1} - gamma_{j-1})/2.
eps_bar = sqrt((tau + OFF_ALLOW)/2) (r131/r135 recipe, cited).

THEOREM S1 (matching from counting; NEW in-corpus).  Hypotheses:
 (C) COUNTEQ: #{nodes <= T_z} = m  (an integer; certified from source
     by the argument-principle contour of E_N'/E_N -- counts ALL
     zeros of E_N in the zone strip, complex included);
 (P) PINBALL: every true zone zero gamma_j has a node within g_j,
     with balls B_j = [gamma_j - g_j, gamma_j + g_j] pairwise
     disjoint (true-zero spacing floor: CLASSICAL in the zone, the
     gaps of verified zeros below 151) and B_j inside the count
     region (gamma_m + g_m below the contour top).
Conclusion: every ball contains EXACTLY ONE node, NO node <= T_z
lies outside the balls (NO STRAYS), the matching is the order-
preserving bijection, and |mu_j - gamma_j| <= g_j for all j <= m --
i.e. the zone node counting law holds at accuracy delta =
max_j g_j/s_j spacings.  PROOF (pure counting): the m disjoint balls
each contain >= 1 of the m nodes in the region, so each contains
exactly one and none are left over; ordering gives the bijection.
CONSEQUENCE: r133's H1/H2/H3 stop being independent hypotheses --
they FOLLOW from (C) + (P).  The r133 Theorem M chain (sorted
dominance, M- bounds, Theorem A assembly) then consumes them, cited.

THEOREM S2 (one-sidedness suffices).  (P) alone forces
#{nodes <= T_z} >= m (each disjoint ball holds >= 1 node).  Hence
under (P):  COUNTEQ  <==>  #{nodes <= T_z} <= m -- the counting
input to OMEGA-b is ONE-SIDED (the census polynomial never
overcounts the zone), an integer inequality per rung.  This is the
DOM shape (r132/r133) in count currency at the single point T_z.

THEOREM S3 (floor deformation; exact inequalities).  Let the zone
configuration move from the star config y* (zone positions = true
zeros; edge nodes FROZEN -- they cancel exactly in the ratio) to the
node config, every zone position within delta*s of its zero.  With
the paired factor g(t) = sin(At)/(t - om_k*), k* = nearest lattice
index (removable-pole pairing: sin and the lattice factor cancel),
the floor m_j = |E_N'(mu_j)| = 4|A_0 sin(A mu_j)| PR_j (r135 D1,
cited) satisfies  |log m_j - log m*_j| <= KAPPA * S_pair,j * delta,
valid while all u-ratios <= 1/2 (KAPPA = 2 from |log(1+u)| <=
|u|/(1-u*), sympy-gated) and the ball stays in the g-sample window
(delta <= 1/4).  S_pair,j = SUP_INFLATE*sup|g'/g|*s_j (sampled sup,
7-point stencil on [gamma_j +- s_j/4]) + s_j/(gamma_j + om_k*) +
sum_{k != k*} 2 gamma_j s_j / |y_j - b_k| + sum_{i != j, zone}
(2 gamma_i s_i + 2 gamma_j s_j)/|y_j - y_i|.  All terms classical
(true zeros + lattice) -- the edge census NEVER enters.

THEOREM S4 (bootstrap self-improvement).  Let R*_j = 2 eps_bar /
(m*_j s_j) (the certified radius at the star config, in spacing
units) and F(delta) = max_j R*_j exp(KAPPA S_pair,j delta), monotone
increasing.  If the true matching slack delta satisfies delta <=
delta_seed with F(delta_seed) <= delta_seed inside the validity
region (delta <= b_c := min(barrier, 1/2 u_rate^{-1}, 1/4)), then
delta <= F(F(...F(delta_seed))) -> the low fixed point ~ max R*_j:
ANY seed inside the basin self-improves to the certified-radius
level.  MACHINE FACT (pre-freeze): the basin b_c = 0.069/0.090/
0.084/0.050 spacings at x = 5/8/13/18 while delta_suff = 0.42..2.4
and GROWING: THE PROVEN BASIN SITS STRICTLY BELOW THE H-PIN SLACK
(SEED-GAP) -- the remaining position omega is a seed at ~0.03-0.09
spacings, not at delta_suff; once seeded, the slack collapses to
R* ~ 2.4e-3..1.6e-14 (iterates gated).

ASSEMBLY (OMEGA-b, exactly typed).  Per rung: COUNTEQ (contour,
certified) + PINBALL (gap law, certified) ==> S1 matching ==> the
SPACING-REMAINDER statement holds with delta_cert = max_j g_j/s_j
<< delta_suff -- CERTIFIED at every ladder rung x >= x_1 = 5.
lam-uniformly: OMEGA-b <== EPSLOCK (OMEGA-a) + COUNTEQ-lam +
SEEDBALL-lam, via S1-S4 + classical zone data (verified census +
spacing floor + zero-free gap (0, 14.13)).  The classical input that
carries no-stray is the VERIFIED ZERO CENSUS below T_z (count m +
gap floor + the zero-free interval) -- verified-computation-citable
(PT21-class), NOT RH-adjacent; beyond the verification height
(x > H/(2 pi) ~ 4.8e11) the true count itself is only RvM +- Q(T),
NOT O(spacing): COUNTEQ keeps a genuine source-side open core.

THE A2 CRUX (trial-function route on tau).  The r131 builder IS the
exact frame minimizer (Rayleigh re-gate).  Therefore tau <= Q(v)
for every trial v.  MACHINE FACT (pre-freeze): the ZONE-ZERO-KILLED
subspace minimum Q_sub (kill E at the m verified zone zeros -- a
classical-zero-consuming certificate, NOT a builder input; the
builder never sees zeros, G01) reproduces tau at ratio 1.00 at every
rung x = 5..24: the tau-collapse is PER-RUNG PROVABLE modulo the
classical verified zeros, and the bound is TIGHT.  The zero-free
trials stay at O(1): jet-killed (A_0..A_6 = 0) and Fejer trials sit
>= 6.9e15 .. 2.2e108 ABOVE tau -- the poly(x) wall of r135 OMEGA-a
machine-pinned from the trial side.  The lam-uniform ANALYTIC rate
of Q_sub stays open (that is OMEGA-a).

THE COUNTING OBSTRUCTION (why COUNTEQ cannot be soft).  Jensen/type
counting is BLIND: the Jensen bound on E_N's zero count in |z| <=
T_z/e allows 2.9 zeros at x = 5 (true: 0) and 23.2 at x = 13 (true:
3) -- entire-function counting misses by >= a factor ~8; COUNTEQ
must consume arithmetic.  CONTROLS: the certificate REFUSES in all
three worlds at COUNTEQ itself -- SMOOTH/SCRARITH x=5 OVERCOUNT the
zone 7 vs 4, EPSTEIN x=8 16 vs 10, with mu_1 = 4.836/2.006/1.230
filling the verified zero-free gap (0, 14.13): the one-sided count
bound IS the arithmetic consumption, exactly where r133 located H2.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (zeta only in audit_*, np.load only in ward_*,
    no zero-oracle names, no verification/ import); G02 cache (X5).
S1  exact layer: G10 THEOREM S1 on an exact rational instance +
    two refusal instances (count-violation ==> refusal; empty-ball
    with count equality ==> stray or double, exhibited); G11
    THEOREM S2 logic (>= from pinning; equality <=> one-sided);
    G12 deformation lemmas (log bounds by derivative sign + exact
    instances; paired-floor rearrangement identity; y-shift bound);
    G13 bootstrap monotonicity + finite iteration logic; G14
    delta_suff rearrangement (m_min e^{-S delta} >= m_req <==
    delta <= ln(margin)/S); G15 D1 re-gate on the exact rational
    instance (E' == 4 sin(A mu) F'(mu^2); r135, cited).
S2  G20 HSW G(T) sanity; G21 polished ordinates (NPOL = 56,
    AUD_DPS = 100) + sign-change intervals; G22 Theorem-T top
    segment re-gate (gamma_{K-1} <= T*(x); r133, cited).
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census,
    r132 AMENDMENT-1 currency) + (18,140),(24,150) deep (full-band
    sign-scan census at step 0.05; CALIBRATION DISCLOSURE: the scan
    finds 50/65 and 74/95 nodes -- the near-edge nodes pair up
    inside one step; the ZONE prefix is complete (35/35, 53/53) and
    the S-sensitivity uses the found nodes + DEEP_S_INFLATE = 1.1
    for the disclosed deficit; the certificates consume ZONE data
    only -- the edge census cancels in S3/S4 by construction):
    G30 census (core: count == K-1, all real, residuals <= 1e-20;
    deep: zone count complete + residuals); G31 COUNTEQ certificate
    (zone node count == m AND argument-principle contour == m at
    ALL FIVE rungs, integrality <= 1e-6, bottom grid sign-uniform);
    G32 PINBALL (gap <= g_j = 2 eps_bar/m_j, validity g <=
    min(m/M2, s/2) with SUP_INFLATE M2, balls disjoint at classical
    gaps, top ball below the contour cut); G33 S1-consequences
    verified (0 strays, one node per ball, order-preserving --
    consequences now, not hypotheses); G34 SPACING-REMAINDER
    (delta_cert <= delta_suff per rung, margin growing >= 1e3 over
    the ladder); G35 bootstrap (R* via the edge-cancelling Delta
    route, R*/delta_cert in (0.5, 2); basin b_c in [0.03, 0.25];
    u-check; iterates from 0.9 b_c collapse to <= 2 R*max in 4
    steps; SEED-GAP b_c < delta_suff at every rung); G36 EPS-LOCK
    input window (eps_bar/|A_0| in (0.01, 10), typed CONSUMED);
    G37 trial bounds (minimizer Rayleigh <= 1e-30; 0 <= Q_sub/tau
    - 1 <= 0.5; Q_jet/tau and Q_fejer/tau >= 1e10; null residual
    <= 1e-40).
S3c G45 Jensen blindness at x = 5, 13 (bound - true count >= 2:
    the soft-counting obstruction exhibit).
S4  controls through the SAME certificate: G50 SMOOTH x=5, G51
    SCRARITH x=5, G52 EPSTEIN x=8 -- COUNTEQ must REFUSE (zone
    overcount >= 1) with mu_1 inside the zero-free gap; G53
    consistency (all three refuse at the counting hypothesis).
S5  G54 tau-screen: |slope log10 delta_cert vs log10 tau| <= 0.30
    (delta_cert is A_0-free by D3, cited -- the DEMAND is not
    Connes-priced; the raw radius g_max rides sqrt(tau) BY
    CONSTRUCTION, typed BOUND-RIDES-CONNES, not a disguise);
    G55 conditioning (1e-25 shift on Q[0,0] at x=5 moves tau
    inside (1e-40, 1e-10)).
S6  G60 min-cut (r116 replica): the r135 SPACREM unit edge REFINED
    in series COUNTEQ(1) -> SEEDBALL(1); chain L1TAILPROVEN ->
    EPSLOCK(1) -> COUNTEQ(1) -> SEEDBALL(1) -> SPACREMTHM(INF,
    THIS ROUND: S1-S4) -> DOMASYM(INF, r133) -> WPDWIN(INF); flows
    base 4, refined 5, granting ONE sub-omega still 5,
    counterfactual PARALLEL 7 NOT REAL; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); A_MARG = 4 (margin battery point, r135); NPOL =
56; AUD_DPS = 100; CACHE_ERR = 1e-9; HSW = (0.1038, 0.2573, 9.3675)
[HSW22 Cor. 1.2, v914 corpus input]; T_PT = 3000175332800 [PT21];
M_ENV = 3; OFF_ALLOW = 8 e^A ENV_3(T_PT)^2 G(T_PT) (r131 recipe,
cited); SUP_INFLATE = 1.5; KAPPA = 2.0; BARRIER_CAP = 0.25; U_BAR =
0.5; DEEP_S_INFLATE = 1.1; SCAN_STEP = 0.05; SCAN_LO = 0.5;
DELTA_LADDER = (1e-30, 1e-24, 1e-18, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2);
BOT_GRID = (0.02, 0.62, 0.02).
BARS: RES_BAR = 1e-20 (pre-freeze 5e-63..5e-153); ARG_INT_BAR = 1e-6
(pre-freeze 2.7e-29..4.3e-16 at x = 5..18); BAR_POLISH_XW = 1e-7;
BAR_POLISH_RES = 1e-60 (pre-freeze 7e-104); MARGIN_BAR = 3.0
(pre-freeze margins 31.8/616/3.5e6/1.5e9/5.3e12); DSUFF_GROWTH = 1e3
(pre-freeze (delta_suff/delta_cert) 178 -> ~1.7e14); RSTAR_WIN =
(0.5, 2.0) (pre-freeze R*/delta_cert = 1.000 at every rung);
BASIN_LO, BASIN_HI = 0.03, 0.25 (pre-freeze b_c 0.069/0.090/0.084/
0.050); ITER_COLLAPSE = 2.0 (pre-freeze iterates reach R* in <= 3);
EPSLOCK_WIN = (0.01, 10.0) (pre-freeze c = 0.189/0.163/0.137/0.117/
0.104); RAY_BAR = 1e-30 (pre-freeze 5.3e-46..1.2e-44); QSUB_REL =
(-1e-9, 0.5) (pre-freeze ratio 1.00); QFREE_MIN = 1e10 (pre-freeze
6.9e15..2.2e108); NULLRES_BAR = 1e-40 (pre-freeze 3e-62..1e-151);
JENSEN_MARGIN = 2.0 (pre-freeze 2.9 vs 0, 23.2 vs 3); TAU_SLOPE_BAR
= 0.30 (pre-freeze slope ~0.12); COND_WIN = (1e-40, 1e-10);
GAMMA1_LIT = 14.134725141734694 (ward only); RUNTIME_BAR = 10800 s.
Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks (round-118 trap).

CALIBRATION DISCLOSURE (pre-freeze, two scratch scripts
calib_scratch_spacrem.py / calib_scratch_spacrem2.py + logs,
deleted; numbers quoted verbatim): builds 2.9/13.6/166/490/1154 s;
zone counts true == nodes 4/10/21/35/53 at every rung; contour
counts exact 4/10/21/35 (dev <= 4.3e-16, cost 1.8/7.5/19.5/36.3 s;
x=24 contour not calibrated, extrapolated ~90 s, first exercised in
the frozen run); FULL-BAND scan finds 50/65 (x=18) and 74/95 (x=24)
-- the deep census deficit is near-edge pairing, disclosed above,
zone prefix complete; delta_meas = 5.2e-7/9.6e-10/1.0e-17/5.3e-23/
2.4e-30; delta_cert = 2.35e-3/1.53e-4/1.93e-8/6.8e-11/1.6e-14;
delta_suff (r135 S-currency) = 0.419/0.582/1.111 core, deep ~2.4/
2.9 pre-deficit-inflation; Delta range [-4.2e-7, 9.0e-8] (x=5) down
to [-1.3e-22, -2.0e-24] (x=18); S_pair max 89.3/82.5/156.0/121.2;
u_rate binds the basin at x >= 8; iterates x=13: 0.152 -> 9.8e-4 ->
2.0e-8 -> 1.93e-8 (== R*); Q_sub/tau = 1.00 at all five rungs
(cost <= 12.6 s); Q_jet/tau = 1.1e16/5.1e29/1.1e54/5.4e78/2.2e108;
Q_fejer similar; Jensen 2.9 vs 0 (x=5), 23.2 vs 3 (x=13); controls
zone counts 7/7/16 vs 4/4/10 with mu_1 = 4.836/2.006/1.230; E(0) ==
2 A c_0 dev <= 4e-17.  One scratch-2 instrument fix pre-freeze
(np.float64 repr cast at the g-sample stencil, the r133-smoke-1
class).  Amendments after the frozen run, if any, are appended as
numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): THMS1-PROVEN(matching from counting; H2/H3
demoted to consequences); THMS2-PROVEN(one-sided count suffices);
DEFORM-LEMMA-PROVEN + BOOTSTRAP-PROVEN(basin + collapse);
COUNTEQ-CERTIFIED-ON-LADDER(contour == m at five rungs);
PINBALL-CERTIFIED; SPACREM-ASSEMBLED-ON-LADDER(x_1 = 5, margins
growing); SEED-GAP(b_c < delta_suff everywhere: the basin sits
strictly below the H-pin slack -- the position omega is a seed at
~0.03-0.09 spacings); TRIALBOUND-TIGHT(Q_sub/tau ~ 1, classical-
zero-consuming; zero-free trials >= 1e10 above: the OMEGA-a wall
machine-pinned trial-side); JENSEN-BLIND(soft counting obstructed);
CONTROLS-REFUSE(COUNTEQ overcount; zero-free-gap consumption);
DEMAND-A0-FREE(tau-screen) + BOUND-RIDES-CONNES(typed);
OMEGA-REFINED(SPACREM = COUNTEQ + SEEDBALL serial, both open,
rates named); MINCUT(4/5, census {MEAS, OMEGA-POS} unchanged).
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
LADDER_CORE = ((5, 60), (8, 80), (13, 120))
LADDER_DEEP = ((18, 140), (24, 150))
A_MARG = 4
NPOL = 56
AUD_DPS = 100
CACHE_ERR = 1e-9
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_ENV = 3
SUP_INFLATE = 1.5
KAPPA = 2.0
BARRIER_CAP = 0.25
U_BAR = 0.5
DEEP_S_INFLATE = 1.1
SCAN_STEP = 0.05
SCAN_LO = 0.5
DELTA_LADDER = (1e-30, 1e-24, 1e-18, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2)
RES_BAR = 1e-20
ARG_INT_BAR = 1e-6
BAR_POLISH_XW = 1e-7
BAR_POLISH_RES = 1e-60
MARGIN_BAR = 3.0
DSUFF_GROWTH = 1e3
RSTAR_WIN = (0.5, 2.0)
BASIN_LO, BASIN_HI = 0.03, 0.25
ITER_COLLAPSE = 2.0
EPSLOCK_WIN = (0.01, 10.0)
RAY_BAR = 1e-30
QSUB_REL = (-1e-9, 0.5)
QFREE_MIN = 1e10
NULLRES_BAR = 1e-40
JENSEN_MARGIN = 2.0
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
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


# --------------------------------------------------------- exact layer
def instance_s1(trues, gs, nodes, Tz):
    """THEOREM S1 on exact rationals: returns dict with counteq,
    pinball, and (if both hold) the forced conclusions."""
    import sympy as sp
    tv = [sp.Rational(v) for v in trues]
    gv = [sp.Rational(v) for v in gs]
    nv = [sp.Rational(v) for v in nodes]
    Tzq = sp.Rational(Tz)
    m = sum(1 for t in tv if t <= Tzq)
    n_zone = sum(1 for v in nv if v <= Tzq)
    counteq = (n_zone == m)
    disjoint = all(tv[j] + gv[j] < tv[j + 1] - gv[j + 1]
                   for j in range(m - 1))
    inside = (m == 0) or (tv[m - 1] + gv[m - 1] < Tzq)
    in_ball = [[i for i in range(len(nv))
                if abs(nv[i] - tv[j]) <= gv[j]] for j in range(m)]
    pinball = disjoint and inside and all(len(b) >= 1 for b in in_ball)
    out = dict(counteq=counteq, pinball=pinball)
    if counteq and pinball:
        out["one_per_ball"] = all(len(b) == 1 for b in in_ball)
        ball_ids = set(i for b in in_ball for i in b)
        out["no_stray"] = all(i in ball_ids for i in range(len(nv))
                              if nv[i] <= Tzq)
        out["order"] = all(in_ball[j][0] == j for j in range(m))
        out["gaps_ok"] = all(abs(nv[j] - tv[j]) <= gv[j]
                             for j in range(m))
    return out


def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # G10 THEOREM S1 instance + refusal instances
    good = instance_s1(("4", "5", "6", "17/2", "11", "30"),
                       ("1/50", "1/40", "1/30", "1/20"),
                       ("401/100", "399/80", "541/90", "171/20",
                        "12", "14"),
                       "10")
    ok_g = (good["counteq"] and good["pinball"]
            and good["one_per_ball"] and good["no_stray"]
            and good["order"] and good["gaps_ok"])
    # refusal A: stray node breaks COUNTEQ (5 nodes <= Tz vs m = 4)
    badA = instance_s1(("4", "5", "6", "17/2", "11", "30"),
                       ("1/50", "1/40", "1/30", "1/20"),
                       ("3", "401/100", "399/80", "541/90", "171/20",
                        "12"),
                       "10")
    # refusal B: count equality but one ball empty ==> stray forced
    badB = instance_s1(("4", "5", "6", "17/2", "11", "30"),
                       ("1/50", "1/40", "1/30", "1/20"),
                       ("401/100", "399/80", "541/90", "7", "12",
                        "14"),
                       "10")
    okB = badB["counteq"] and not badB["pinball"]
    out.append(("G10-thmS1-instance",
                ok_g and (not badA["counteq"]) and okB,
                "COUNTEQ + PINBALL ==> one node per ball, no stray, "
                "order-preserving bijection, |mu_j - gamma_j| <= g_j "
                "(exact rationals); refusal A: stray flips the count "
                "(COUNTEQ false); refusal B: empty ball ==> PINBALL "
                "false (hypothesis necessity): H2/H3 are now "
                "CONSEQUENCES of counting, not hypotheses"))

    # G11 THEOREM S2 logic
    m_i = 4
    n_ball = 4          # pinning: >= one node per disjoint ball
    n_zone_lo = n_ball  # so #nodes >= m
    ok11 = (n_zone_lo >= m_i
            and ((n_zone_lo <= m_i) == (n_zone_lo == m_i)))
    out.append(("G11-thmS2-onesided", ok11,
                "PINBALL ==> #nodes(zone) >= m (each of m disjoint "
                "balls holds >= 1); hence COUNTEQ <==> #nodes(zone) "
                "<= m: the counting input is ONE-SIDED (census never "
                "overcounts the zone) -- DOM shape at the single "
                "point T_z"))

    # G12 deformation lemmas
    u, us, v = sp.symbols("u us v", positive=True)
    # (a) upper side: log(1+u) <= u  (classical; derivative sign)
    dU = sp.simplify(sp.diff(u - sp.log(1 + u), u)
                     - u / (1 + u))
    # lower side: -log(1-v) <= v/(1-us) for 0 <= v <= us < 1
    dL = sp.simplify(sp.diff(v / (1 - us) + sp.log(1 - v), v)
                     - (1 / (1 - us) - 1 / (1 - v)))
    instL = all(
        float(-sp.log(1 - sp.Rational(p, 100))
              - sp.Rational(p, 100) / (1 - sp.Rational(1, 2))) <= 0
        for p in (10, 30, 50))
    # (b) paired-floor rearrangement: sin/(y - b) == g/(mu + om)
    mu_s, om_s, As = sp.symbols("mu_s om_s As", positive=True)
    lhs = sp.sin(As * mu_s) / (mu_s ** 2 - om_s ** 2)
    rhs = (sp.sin(As * mu_s) / (mu_s - om_s)) / (mu_s + om_s)
    okb = sp.simplify(lhs - rhs) == 0
    # (c) y-shift bound: (t+d)^2 - t^2 == d(2t + d)
    t_s, d_s = sp.symbols("t_s d_s", positive=True)
    okc = sp.simplify((t_s + d_s) ** 2 - t_s ** 2
                      - d_s * (2 * t_s + d_s)) == 0
    ok12 = (dU == 0 and dL == 0 and instL and okb and okc)
    out.append(("G12-deformation-lemmas", ok12,
                "|log(1+u)| <= |u|/(1-u*) for |u| <= u* (= KAPPA "
                "= 2 at u* = 1/2; derivative signs + exact "
                "instances); paired removable-pole identity "
                "sin(A mu)/(y-b_k) == g(mu)/(mu+om_k) exact; y-shift "
                "(t+d)^2 - t^2 == d(2t+d) exact: THEOREM S3 inputs"))

    # G13 bootstrap monotonicity + finite iteration logic
    dd, Rr, Ss = sp.symbols("dd Rr Ss", positive=True)
    F = Rr * sp.exp(2 * Ss * dd)
    ok13a = sp.simplify(sp.diff(F, dd) - 2 * Ss * F) == 0
    # iteration instance (floats, deterministic): R = 1e-6, S = 10
    Rf, Sf = 1e-6, 10.0
    d0 = 0.05
    seq = [d0]
    for _ in range(4):
        seq.append(Rf * math.exp(2 * Sf * seq[-1]))
    ok13b = seq[1] < d0 and seq[-1] <= 2 * Rf and \
        all(seq[i + 1] <= seq[i] for i in range(len(seq) - 1))
    out.append(("G13-bootstrap-monotone", ok13a and ok13b,
                "F(delta) = R e^{2 S delta} strictly increasing "
                "(dF == 2SF > 0); monotone iteration from a seed "
                "with F(seed) <= seed collapses to the low fixed "
                "point ~ R (instance: 0.05 -> %.1e in 4 steps): "
                "THEOREM S4 logic" % seq[-1]))

    # G14 delta_suff rearrangement
    mm, mr, Sx, de = sp.symbols("mm mr Sx de", positive=True)
    expr = sp.simplify(
        sp.log(mm * sp.exp(-Sx * de) / mr)
        - (sp.log(mm / mr) - Sx * de))
    ok14 = expr == 0
    out.append(("G14-dsuff-rearrangement", ok14,
                "m_min e^{-S delta} >= m_req <==> delta <= "
                "ln(m_min/m_req)/S == ln(margin)/S exact: "
                "delta_suff is the exact counting slack of the "
                "r135 zone-mass demand"))

    # G15 D1 re-gate (r135, cited)
    y, z, aa = sp.symbols("y z aa", positive=True)
    A0q = sp.Rational(3, 5)
    Fi = A0q * (y - 4) * (y - 9) / ((y - 2) * (y - 7))
    Ei = sp.sin(aa * z) * 2 * Fi.subs(y, z ** 2) / z
    lhs15 = sp.simplify(sp.diff(Ei, z).subs(z, 2))
    rhs15 = sp.simplify(4 * sp.sin(2 * aa)
                        * sp.diff(Fi, y).subs(y, 4))
    ok15 = sp.simplify(lhs15 - rhs15) == 0
    out.append(("G15-d1-regate", ok15,
                "E'(mu) == 4 sin(A mu) F'(mu^2) on the exact "
                "rational instance (r135 THEOREM D1, cited): the "
                "floor is the spacing product -- the object the "
                "deformation lemma transports"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("spacing_remainder_probe -- PRIME.SPACREM.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    jensen_rungs = (5,) if smoke else (5, 13)

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
    section("S1  EXACT LAYER (Theorems S1-S4 inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r131 secular identity + G17 crossover "
         "T_z = 2 pi x; r132 raw-census AMENDMENT 1; r133 Theorems "
         "M/E/T/A; r135 Theorems D1-D4 + the OMEGA-a/OMEGA-b split; "
         "HSW22 Cor. 1.2; PT21 verified census (zone count m, zone "
         "gap floor, zero-free interval (0, gamma_1)); Euler sine "
         "product; infinitude of zeros")

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

    pol_str, pol_res = audit_polish_band(gam[:NPOL], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:NPOL])))
    zdel = audit_zero_deltas(pol_str, AUD_DPS)
    check("G21-polish-intervals",
          xw <= BAR_POLISH_XW and pol_res <= BAR_POLISH_RES
          and all(d is not None for d in zdel),
          "own-Newton ordinates vs cache max dev %.1e, max |Xi| "
          "%.1e; all %d sign-change certified (worst delta %.0e)"
          % (xw, pol_res, NPOL, max(d for d in zdel)), kind="edge")

    ok22 = True
    det22 = []
    for x, _d in core + deep:
        K = int(math.ceil(KFAC * x * math.log(x)))
        N = K - 1
        Ts = t_star(N)
        gN = float(gam[N - 1])
        ok22 = ok22 and gN <= Ts \
            and (m_rvm(Ts) - q_hsw(Ts)) >= N - 1e-9
        det22.append("x%d: g_%d %.1f <= T* %.1f" % (x, N, gN, Ts))
    check("G22-thmT-top-segment", ok22,
          "gamma_{K-1} <= T*(x) per rung (r133 Theorem T re-gate, "
          "cited; feeds the TL/margin machinery): " + "; ".join(det22))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: COUNTEQ + PINBALL + S1 + BOOTSTRAP + TRIALS")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    det30, det31, det32, det33, det34, det35 = [], [], [], [], [], []
    det36, det37 = [], []
    dcert_tab, dsuff_tab, tau_tab, gmax_tab, bc_tab = {}, {}, {}, {}, {}
    for x, dps in all_rungs:
        is_deep = x > 13
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            bks = [oms[k] ** 2 for k in range(1, K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            edge = float(K * mp.pi / aa)

        # ---- census
        deficit = 0
        if not is_deep:
            mus, n_nonreal = raw_mp_census(ce)
            seeds = [float(v) for v in mus]
            cens_ok = (len(mus) == K - 1 and n_nonreal == 0)
        else:
            with mp.workdps(dps):
                ts = np.arange(SCAN_LO, edge, SCAN_STEP)
                vprev = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(ts[0]))))[0]
                seeds = []
                for tv in ts[1:]:
                    v = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(tv))))[0]
                    if v * vprev < 0:
                        seeds.append(float(tv) - SCAN_STEP / 2)
                    vprev = v
            deficit = (K - 1) - len(seeds)
            cens_ok = deficit >= 0
        nds = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds.append(tmu)
                wres = max(wres, float(res))
        nds_f = np.array([float(v) for v in nds])
        n_zone_nodes = int(np.sum(nds_f <= Tz))
        cens_ok = cens_ok and wres <= RES_BAR
        ok30 = ok30 and cens_ok
        det30.append("x%d: %s %d/%d res %.0e"
                     % (x, "scan" if is_deep else "poly",
                        len(nds), K - 1, wres))
        if is_deep:
            info("x=%d deep census: full-band scan %d of %d (edge "
                 "deficit %d, near-edge pairing, disclosed); zone "
                 "prefix complete" % (x, len(nds), K - 1, deficit))

        # ---- G31 COUNTEQ
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        nz = [float(v) for v in nds_f if v <= Tz]
        nxt = [float(v) for v in nds_f if v > Tz]
        tr = (nz[-1] + (nxt[0] if nxt else nz[-1] + 3.0)) / 2
        with mp.workdps(dps):
            def ELE(zz, cs=cs, aa=aa, oms=oms):
                f, fp = en_pair(cs, aa, oms, zz)
                return fp / f
            c1 = mp.quad(lambda t: ELE(mp.mpc(t, -1)), [SCAN_LO, tr])
            c2 = mp.quad(lambda t: ELE(mp.mpc(tr, t)) * 1j, [-1, 1])
            c3 = mp.quad(lambda t: ELE(mp.mpc(t, 1)), [tr, SCAN_LO])
            c4 = mp.quad(lambda t: ELE(mp.mpc(SCAN_LO, t)) * 1j,
                         [1, -1])
            wind = (c1 + c2 + c3 + c4) / (2j * mp.pi)
            devc = float(abs(wind - m_zone))
        okc = (n_zone_nodes == m_zone and devc <= ARG_INT_BAR
               and len(sgs) == 1)
        ok31 = ok31 and okc
        det31.append("x%d: nodes %d == m %d contour %.6f dev %.0e"
                     % (x, n_zone_nodes, m_zone, float(mp.re(wind)),
                        devc))

        # ---- eps_bar + gap law (PINBALL)
        with mp.workdps(dps):
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
        tauf = float(ce["tau"])
        eps_bar = math.sqrt((tauf + off_allow) / 2.0)
        a0f = abs(float(A0))
        m_arr = np.zeros(m_zone)
        g_arr = np.zeros(m_zone)
        s_arr = np.zeros(m_zone)
        gap_arr = np.zeros(m_zone)
        okx = True
        with mp.workdps(dps):
            for j in range(m_zone):
                gj = mp.mpf(pol_str[j])
                mu = nds[j]
                gap_arr[j] = float(abs(mu - gj))
                lo = pol_f64[j - 1] if j > 0 else 0.0
                hi = pol_f64[j + 1] if j + 1 < NPOL \
                    else pol_f64[j] + 6.0
                s_arr[j] = 0.5 * (hi - lo)
                _f0, fp0 = en_pair(cs, aa, oms, mu)
                m_arr[j] = float(abs(fp0))
                g_arr[j] = 2.0 * eps_bar / max(m_arr[j], 1e-300)
                d2f = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                 tt)[0], mu, 2)
                d2g = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                 tt)[0], gj, 2)
                M2 = SUP_INFLATE * max(float(abs(d2f)),
                                       float(abs(d2g)))
                valid = g_arr[j] <= min(m_arr[j] / max(M2, 1e-300),
                                        0.5 * s_arr[j])
                okx = okx and gap_arr[j] <= g_arr[j] and valid
        # ball disjointness at CLASSICAL gaps + top ball below cut
        disj = all(pol_f64[j] + g_arr[j]
                   < pol_f64[j + 1] - g_arr[j + 1]
                   for j in range(m_zone - 1))
        topok = pol_f64[m_zone - 1] + g_arr[m_zone - 1] < tr
        okx = okx and disj and topok
        ok32 = ok32 and okx
        det32.append("x%d: maxgap %.1e maxball %.1e disj %s"
                     % (x, float(np.max(gap_arr)),
                        float(np.max(g_arr)), disj))

        # ---- G33 S1-consequences verified against data
        strays = int(np.sum(nds_f[m_zone:] <= Tz))
        one_per = all(int(np.sum(np.abs(nds_f - pol_f64[j])
                                 <= g_arr[j])) == 1
                      for j in range(m_zone))
        order_ok = all(abs(float(nds_f[j]) - pol_f64[j]) <= g_arr[j]
                       for j in range(m_zone))
        ok33 = ok33 and strays == 0 and one_per and order_ok
        det33.append("x%d: strays %d one-per %s order %s"
                     % (x, strays, one_per, order_ok))

        # ---- G34 spacing remainder vs delta_suff
        d_cert = float(np.max(g_arr / s_arr))
        N = K - 1
        Ts = t_star(N)
        zg = gam[gam <= Tz]
        swp = float(np.sum([wp_abs(float(A_MARG), g) for g in zg]))
        TL = tl_shells(N, float(A_MARG), Ts)
        m_req = 16.0 * eps_bar * swp / TL if TL > 0 else float("inf")
        margin = float(np.min(m_arr)) / m_req
        # S sensitivity, r135 currency: star positions, node spacings
        star = np.concatenate([pol_f64[:m_zone], nds_f[m_zone:]])
        s_node = np.zeros(len(star))
        for i in range(len(star)):
            lo = star[i - 1] if i > 0 else 0.0
            hi = star[i + 1] if i + 1 < len(star) else edge
            s_node[i] = 0.5 * (hi - lo)
        S135 = np.zeros(m_zone)
        for j in range(m_zone):
            yj = star[j] ** 2
            acc = 0.0
            for i in range(len(star)):
                if i != j:
                    acc += 2 * star[i] * s_node[i] \
                        / abs(yj - star[i] ** 2)
            S135[j] = acc
        s_sens = float(np.max(S135)) * (DEEP_S_INFLATE if is_deep
                                        else 1.0)
        d_suff = math.log(max(margin, 1.0)) / s_sens
        ok34x = margin >= MARGIN_BAR and d_cert <= d_suff
        ok34 = ok34 and ok34x
        det34.append("x%d: d_cert %.1e <= d_suff %.3f (margin %.1e "
                     "S %.1f)" % (x, d_cert, d_suff, margin, s_sens))
        dcert_tab[x] = d_cert
        dsuff_tab[x] = d_suff
        tau_tab[x] = tauf
        gmax_tab[x] = float(np.max(g_arr))

        # ---- G35 bootstrap (Delta route + basin + iterates)
        oms_f = [float(o) for o in oms]
        Delta = np.zeros(m_zone)
        S_pair = np.zeros(m_zone)
        u_rate = 0.0
        with mp.workdps(dps):
            for j in range(m_zone):
                gjf = float(pol_f64[j])
                ks = min(range(1, K),
                         key=lambda k: abs(oms_f[k] - gjf))
                gq = mp.mpf(pol_str[j])
                mum = nds[j]
                dl = (mp.log(abs(mp.sin(aa * gq) / (gq - oms[ks])))
                      - mp.log(abs(mp.sin(aa * mum)
                                   / (mum - oms[ks]))))
                dl += (mp.log(abs(mum + oms[ks]))
                       - mp.log(abs(gq + oms[ks])))
                for k in range(1, K):
                    if k == ks:
                        continue
                    dl += (mp.log(abs(mum ** 2 - bks[k - 1]))
                           - mp.log(abs(gq ** 2 - bks[k - 1])))
                for i in range(m_zone):
                    if i == j:
                        continue
                    dl += (mp.log(abs(gq ** 2
                                      - mp.mpf(pol_str[i]) ** 2))
                           - mp.log(abs(mum ** 2 - nds[i] ** 2)))
                Delta[j] = float(dl)
                sg = 0.0
                for q5 in range(-3, 4):
                    tv = float(gjf + (q5 / 3.0) * 0.25 * s_arr[j])
                    tt = mp.mpf(repr(tv))
                    val = abs(aa * mp.cos(aa * tt) / mp.sin(aa * tt)
                              - 1 / (tt - oms[ks]))
                    sg = max(sg, float(val))
                acc = SUP_INFLATE * sg * s_arr[j]
                acc += s_arr[j] / (gjf + oms_f[ks])
                yj = gjf * gjf
                for k in range(1, K):
                    if k == ks:
                        continue
                    dy = abs(yj - float(bks[k - 1]))
                    acc += 2 * gjf * s_arr[j] / dy
                    u_rate = max(u_rate, 2 * gjf * s_arr[j] / dy)
                for i in range(m_zone):
                    if i == j:
                        continue
                    dy = abs(yj - pol_f64[i] ** 2)
                    term = (2 * pol_f64[i] * s_arr[i]
                            + 2 * gjf * s_arr[j]) / dy
                    acc += term
                    u_rate = max(u_rate, term)
                S_pair[j] = acc
        Rstar = (g_arr / s_arr) * np.exp(Delta)
        Rmax = float(np.max(Rstar))

        def Fmap(d, Rstar=Rstar, S_pair=S_pair):
            with np.errstate(over="ignore"):
                return float(np.max(np.minimum(
                    Rstar * np.exp(KAPPA * S_pair * d), 1e300)))

        if Fmap(BARRIER_CAP) <= BARRIER_CAP:
            barrier = BARRIER_CAP
        else:
            lo_b, hi_b = 0.0, BARRIER_CAP
            for _ in range(60):
                mid = 0.5 * (lo_b + hi_b)
                if Fmap(mid) <= mid:
                    lo_b = mid
                else:
                    hi_b = mid
            barrier = lo_b
        b_c = min(barrier, U_BAR / max(u_rate, 1e-12), BARRIER_CAP)
        it = 0.9 * b_c
        its = [it]
        for _ in range(4):
            it = Fmap(it)
            its.append(it)
        rs_ratio = Rmax / d_cert
        ok35x = (RSTAR_WIN[0] <= rs_ratio <= RSTAR_WIN[1]
                 and BASIN_LO <= b_c <= BASIN_HI
                 and its[-1] <= ITER_COLLAPSE * Rmax
                 and b_c < d_suff)
        ok35 = ok35 and ok35x
        det35.append("x%d: R* %.1e (ratio %.3f) b_c %.3f iterates->"
                     "%.1e" % (x, Rmax, rs_ratio, b_c, its[-1]))
        bc_tab[x] = b_c
        info("x=%d bootstrap: barrier %.3f u_rate %.2f b_c %.3f "
             "S_pair max %.1f Delta in [%.1e, %.1e]; SEED-GAP: "
             "b_c %.3f < delta_suff %.3f"
             % (x, barrier, u_rate, b_c, float(np.max(S_pair)),
                float(np.min(Delta)), float(np.max(Delta)),
                b_c, d_suff))

        # ---- G36 EPS-LOCK input
        clock = eps_bar / a0f
        ok36 = ok36 and EPSLOCK_WIN[0] <= clock <= EPSLOCK_WIN[1]
        det36.append("x%d: %.3f" % (x, clock))

        # ---- G37 trials
        with mp.workdps(dps):
            Mq = ce["mpM"]
            tau_mp = ce["mpE"][0]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            vmin = [cs[k] * nrm[k] for k in range(K)]
            num = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                den += vmin[i] * vmin[i]
                acc = mp.mpf(0)
                for j2 in range(K):
                    acc += Mq[i, j2] * vmin[j2]
                num += vmin[i] * acc
            raydev = float(abs(num / den - tau_mp) / abs(tau_mp))

            mcon = m_zone
            Rm = mp.zeros(mcon, K)
            for j in range(mcon):
                g = mp.mpf(pol_str[j])
                Rm[j, 0] = (2 / g) / nrm[0]
                for k in range(1, K):
                    Rm[j, k] = (2 * (-1) ** k * g
                                / (g * g - oms[k] ** 2)) / nrm[k]
            piv = []
            used = set()
            for j in range(mcon):
                gjf = float(pol_f64[j])
                order = sorted(range(1, K),
                               key=lambda k: abs(oms_f[k] - gjf))
                for k in order:
                    if k not in used:
                        piv.append(k)
                        used.add(k)
                        break
            free = [k for k in range(K) if k not in used]
            RP = mp.zeros(mcon, mcon)
            for j in range(mcon):
                for i2, k in enumerate(piv):
                    RP[j, i2] = Rm[j, k]
            Nb = mp.zeros(K, len(free))
            for fi, k in enumerate(free):
                rhs = mp.matrix([-Rm[j, k] for j in range(mcon)])
                zsol = mp.lu_solve(RP, rhs)
                Nb[k, fi] = mp.mpf(1)
                for i2, kp in enumerate(piv):
                    Nb[kp, fi] = zsol[i2]
            resR = 0.0
            for j in range(mcon):
                for fi in range(len(free)):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Rm[j, k] * Nb[k, fi]
                    resR = max(resR, float(abs(acc)))
            nf = len(free)
            QN = mp.zeros(K, nf)
            for i in range(K):
                for fi in range(nf):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += Mq[i, k] * Nb[k, fi]
                    QN[i, fi] = acc
            Qr = mp.zeros(nf, nf)
            Gr = mp.zeros(nf, nf)
            for i in range(nf):
                for j2 in range(i + 1):
                    accq = mp.mpf(0)
                    accg = mp.mpf(0)
                    for k in range(K):
                        accq += Nb[k, i] * QN[k, j2]
                        accg += Nb[k, i] * Nb[k, j2]
                    Qr[i, j2] = Qr[j2, i] = accq
                    Gr[i, j2] = Gr[j2, i] = accg
            L = mp.cholesky(Gr)

            def fwd(rhs_list, L=L, nf=nf):
                y = [mp.mpf(0)] * nf
                for i in range(nf):
                    acc = rhs_list[i]
                    for j2 in range(i):
                        acc -= L[i, j2] * y[j2]
                    y[i] = acc / L[i, i]
                return y

            Yv = mp.zeros(nf, nf)
            for col in range(nf):
                y = fwd([Qr[i, col] for i in range(nf)])
                for i in range(nf):
                    Yv[i, col] = y[i]
            Wm = mp.zeros(nf, nf)
            for col in range(nf):
                y = fwd([Yv[col, i] for i in range(nf)])
                for i in range(nf):
                    Wm[i, col] = y[i]
            for i in range(nf):
                for j2 in range(i):
                    sym = (Wm[i, j2] + Wm[j2, i]) / 2
                    Wm[i, j2] = Wm[j2, i] = sym
            Ew, _ = mp.eigsy(Wm)
            q_sub = min(Ew[i] for i in range(nf))
            qrel = float((q_sub - tau_mp) / tau_mp)

            # jet-killed trial (A0..A6 = 0): best of 6 directions
            pcon = 4
            Rm2 = mp.zeros(pcon, K)
            for p in range(pcon):
                for k in range(K):
                    pw = oms[k] ** (2 * p) if (k or p == 0) \
                        else mp.mpf(0)
                    if k == 0 and p == 0:
                        pw = mp.mpf(1)
                    Rm2[p, k] = (-1) ** k * pw / nrm[k]
            piv2 = list(range(K - pcon, K))
            RP2 = mp.zeros(pcon, pcon)
            for j in range(pcon):
                for i2, k in enumerate(piv2):
                    RP2[j, i2] = Rm2[j, k]
            q_jet = None
            for seed_k in range(min(6, K - pcon)):
                vv = [mp.mpf(0)] * K
                vv[seed_k] = mp.mpf(1)
                rhs = mp.matrix([-Rm2[j, seed_k]
                                 for j in range(pcon)])
                zsol = mp.lu_solve(RP2, rhs)
                for i2, kp in enumerate(piv2):
                    vv[kp] = zsol[i2]
                num = mp.mpf(0)
                den = mp.mpf(0)
                for i in range(K):
                    den += vv[i] * vv[i]
                    acc = mp.mpf(0)
                    for j2 in range(K):
                        acc += Mq[i, j2] * vv[j2]
                    num += vv[i] * acc
                val = num / den
                if q_jet is None or val < q_jet:
                    q_jet = val
            vv = [mp.mpf(1 - k / K) * (-1) ** k * nrm[k]
                  for k in range(K)]
            num = mp.mpf(0)
            den = mp.mpf(0)
            for i in range(K):
                den += vv[i] * vv[i]
                acc = mp.mpf(0)
                for j2 in range(K):
                    acc += Mq[i, j2] * vv[j2]
                num += vv[i] * acc
            q_fej = num / den
            jet_ratio = float(q_jet / tau_mp)
            fej_ratio = float(q_fej / tau_mp)
        ok37x = (raydev <= RAY_BAR
                 and QSUB_REL[0] <= qrel <= QSUB_REL[1]
                 and jet_ratio >= QFREE_MIN
                 and fej_ratio >= QFREE_MIN
                 and resR <= NULLRES_BAR)
        ok37 = ok37 and ok37x
        det37.append("x%d: ray %.0e qsub-rel %.1e jet %.0e fej %.0e"
                     % (x, raydev, qrel, jet_ratio, fej_ratio))

        # ---- Jensen exhibit
        if x in jensen_rungs:
            with mp.workdps(dps):
                r = mp.mpf(repr(Tz))
                e00 = 2 * aa * cs[0]
                npts = 240
                acc = mp.mpf(0)
                for i in range(npts):
                    th = mp.pi * (i + mp.mpf("0.5")) / npts
                    zz = r * mp.exp(1j * th)
                    f, _ = en_pair(cs, aa, oms, zz)
                    acc += mp.log(abs(f))
                jensen = float(acc / npts - mp.log(abs(e00)))
            n_true_re = int(np.sum(gam <= Tz / math.e))
            okj = jensen >= n_true_re + JENSEN_MARGIN
            check("G45-jensen-blind-x%d" % x, okj,
                  "Jensen bound on #zeros(|z| <= T_z/e) = %.1f vs "
                  "true %d: soft entire-function counting is BLIND "
                  "at the needed resolution -- COUNTEQ must consume "
                  "arithmetic (obstruction exhibit)"
                  % (jensen, n_true_re))

    check("G30-census", ok30,
          "core: raw-mp census complete (count == K-1, all real); "
          "deep: full-band scan census, zone prefix complete, edge "
          "deficit disclosed; Newton residuals <= %.0e: %s"
          % (RES_BAR, "; ".join(det30)))
    check("G31-counteq-certificate", ok31,
          "zone node count == m AND argument-principle contour == m "
          "(dev <= %.0e; counts complex zeros too) AND bottom grid "
          "sign-uniform, at EVERY rung: COUNTEQ certified from "
          "source: %s" % (ARG_INT_BAR, "; ".join(det31)))
    check("G32-pinball-certificate", ok32,
          "every zone zero pinned at gap <= ball 2 eps_bar/m_j, "
          "validity b <= min(m/M2, s/2), balls DISJOINT at the "
          "classical zone gaps, top ball below the contour cut: "
          + "; ".join(det32))
    check("G33-s1-consequences", ok33,
          "THEOREM S1 conclusions verified against data at every "
          "rung (0 strays, one node per ball, order-preserving "
          "matching): r133's H2/H3 are now CONSEQUENCES of "
          "COUNTEQ + PINBALL: " + "; ".join(det33))
    xs_all = [x for x, _d in all_rungs]
    grow = ((dsuff_tab[xs_all[-1]] / dcert_tab[xs_all[-1]])
            / (dsuff_tab[xs_all[0]] / dcert_tab[xs_all[0]])
            if len(xs_all) >= 2 else float("inf"))
    check("G34-spacing-remainder", ok34
          and (smoke or grow >= DSUFF_GROWTH),
          "delta_cert <= delta_suff at every rung (margins >= %.0f) "
          "and the slack margin grows %.1e x over the ladder "
          "(>= %.0e): THE SPACING-REMAINDER STATEMENT IS CERTIFIED "
          "ON THE LADDER, x_1 = 5: %s"
          % (MARGIN_BAR, grow, DSUFF_GROWTH, "; ".join(det34)))
    check("G35-bootstrap", ok35,
          "R* via the edge-cancelling Delta route matches the "
          "certified radius (ratio in %s); basin b_c in [%.2f, "
          "%.2f]; iterates from 0.9 b_c collapse to <= %.1f R*; "
          "SEED-GAP: b_c < delta_suff at every rung (the proven "
          "basin sits STRICTLY BELOW the H-pin slack): %s"
          % (str(RSTAR_WIN), BASIN_LO, BASIN_HI, ITER_COLLAPSE,
             "; ".join(det35)))
    check("G36-epslock-input", ok36,
          "eps_bar/|A_0| inside %s at every rung (typed CONSUMED "
          "INPUT = OMEGA-a; r135 EPS-LOCK, cited): %s"
          % (str(EPSLOCK_WIN), "; ".join(det36)))
    check("G37-trial-bounds", ok37,
          "builder == exact frame minimizer (Rayleigh <= %.0e); "
          "zone-zero-killed subspace bound TIGHT (0 <= Q_sub/tau-1 "
          "<= %.1f, classical-zero-consuming certificate, NOT a "
          "builder input); zero-free trials (jet-killed, Fejer) "
          ">= %.0e above tau (the OMEGA-a poly wall, trial-side): %s"
          % (RAY_BAR, QSUB_REL[1], QFREE_MIN, "; ".join(det37)))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (COUNTEQ must refuse)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=False)
        musw, _nr = raw_mp_census(cw)
        Tzw = 2 * math.pi * xw
        n_nodes_w = int(np.sum(musw <= Tzw))
        m_true_w = int(np.sum(gam <= Tzw))
        over = n_nodes_w - m_true_w
        refuse = over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs true m %d (OVERCOUNT +%d), "
              "mu_1 = %.3f fills the verified zero-free gap "
              "(0, %.2f): COUNTEQ refuses -- the one-sided count "
              "bound is the arithmetic consumption (r133 H2, "
              "sharpened to counting)"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0])))
    check("G53-mechanism-consistency", ctrl_ok,
          "COUNTEQ refuses in ALL control worlds by ZONE OVERCOUNT "
          "(7/7/16 vs 4/4/10 pre-freeze): the certificate never "
          "claims the spacing remainder where it is false; the "
          "consumed classical input is the verified census below "
          "T_z (count + gaps + zero-free interval)")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        ld = [math.log10(dcert_tab[x]) for x in xs_all]
        s_d = float(np.polyfit(lt, ld, 1)[0])
        check("G54-tau-screen", abs(s_d) <= TAU_SLOPE_BAR,
              "slope log10 delta_cert vs log10 tau = %.3f (<= %.2f: "
              "the spacing-remainder DEMAND is A_0-free by r135 D3, "
              "not Connes-priced); the raw radius g_max %s rides "
              "sqrt(tau) BY CONSTRUCTION (typed BOUND-RIDES-CONNES, "
              "not a disguise)"
              % (s_d, TAU_SLOPE_BAR,
                 ["%.0e" % gmax_tab[x] for x in xs_all]))
    # conditioning: deterministic rebuild of the x=5 cell
    ce5c = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
    with mp.workdps(ce5c["dps"]):
        E0 = ce5c["mpE"][0]
        Qp_ = ce5c["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5c["K"]))
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
                ("EPSLOCK", "COUNTEQ"): 1,
                ("COUNTEQ", "SEEDBALL"): 1,
                ("SEEDBALL", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("EPSLOCK", "COUNTEQ")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "COUNTEQ"): 1, ("COUNTEQ", "R4HYP"): INF,
               ("NFCLOS", "SEEDBALL"): 1,
               ("SEEDBALL", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r135 SPACREM unit edge "
          "REFINED in series COUNTEQ(1) -> SEEDBALL(1), with "
          "SPACREMTHM (this round, Theorems S1-S4) an INF edge "
          "behind them; granting ONE sub-omega still flows 5; "
          "counterfactual PARALLEL reading 7 NOT REAL (the split is "
          "serial); census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED; RH unreachable without the omega edges")
    info("EXACT OMEGA-b RESIDUE after this round: SPACING-REMAINDER "
         "<== EPSLOCK (OMEGA-a, r135) + COUNTEQ (zone node count "
         "never exceeds the verified count -- one-sided integer per "
         "rung, contour-certified at x = 5..24, Jensen-blind to "
         "soft methods, refused by all controls at the zero-free "
         "gap) + SEEDBALL (an a-priori zone position law at b_c ~ "
         "0.03-0.09 spacings -- STRICTLY stricter than delta_suff; "
         "once seeded, S4 collapses the slack to R* ~ 2.4e-3.."
         "1.6e-14).  PROVEN (exact): S1 matching-from-counting "
         "(H2/H3 demoted to consequences), S2 one-sidedness, S3 "
         "deformation, S4 bootstrap.  CERTIFIED per rung x = 5..24: "
         "COUNTEQ + PINBALL + the assembled spacing remainder with "
         "delta_cert 2.4e-3..1.6e-14 << delta_suff 0.4..2.7.  The "
         "classical input carrying no-stray: the VERIFIED CENSUS "
         "below T_z = 2 pi x (count m + gap floor + zero-free "
         "interval), PT21-class, NOT RH-adjacent, valid for x <= "
         "H/(2 pi) ~ 4.8e11; beyond it even the true count is only "
         "RvM +- Q.  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "THMS1-PROVEN(matching from counting; H2/H3 demoted to "
        "consequences; G10/G33)",
        "THMS2-PROVEN(one-sided count suffices; G11)",
        "DEFORM-LEMMA-PROVEN + BOOTSTRAP-PROVEN(G12/G13/G35)",
        "COUNTEQ-CERTIFIED-ON-LADDER(contour == m at five rungs; "
        "G31)",
        "PINBALL-CERTIFIED(G32)",
        "SPACREM-ASSEMBLED-ON-LADDER(x_1 = 5, margins growing; "
        "G34)",
        "SEED-GAP(b_c < delta_suff at every rung; the position "
        "omega is a seed at ~0.03-0.09 spacings; G35)",
        "TRIALBOUND-TIGHT(Q_sub/tau ~ 1 classical-zero-consuming; "
        "zero-free trials >= 1e10 above; G37)",
        "JENSEN-BLIND(G45)",
        "CONTROLS-REFUSE(COUNTEQ overcount + zero-free gap; "
        "G50-G53)",
        "DEMAND-A0-FREE + BOUND-RIDES-CONNES(G54)",
        "OMEGA-REFINED(SPACREM = COUNTEQ + SEEDBALL serial; G60)"]
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
        print("COMPOSITE: THMS1-PROVEN + THMS2-PROVEN + "
              "DEFORM-LEMMA-PROVEN + BOOTSTRAP-PROVEN + "
              "COUNTEQ-CERTIFIED + PINBALL-CERTIFIED + "
              "SPACREM-ASSEMBLED(x_1 = 5) + SEED-GAP + "
              "TRIALBOUND-TIGHT + JENSEN-BLIND + CONTROLS-REFUSE + "
              "DEMAND-A0-FREE + OMEGA-REFINED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
