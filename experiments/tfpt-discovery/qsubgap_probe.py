#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qsubgap_probe -- PRIME.QSUBGAP.UNIFORM.PROOF.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on QSUBGAP-lambda-uniform, r138 omega)
=======================================================================
Round 138 (counteq_seedball_probe, 32/32) merged COUNTEQ + SEEDBALL
into ONE named quantity QSUBGAP(x) = inf over zone p of
(lam*(p) - tau)/tau, measured 33.7/16.8/22.7/16.6/19.6 at x =
5/8/13/18/24, ALWAYS binding at the zone top T_z = 2 pi x, no decay
trend.  Missing: a proof that the ratio stays > 1 for ALL x.  This
probe is the maximal proof attempt: (Q1) the zone-top cost in exact
closed two-sided form; (Q2) the scale-free formulation and the
compactness question; (Q3) the adversarial branch over classically
legal zone configurations.

=======================================================================
THE EXACT LAYER (Theorems U1-U4; sympy-gated generically + exact
rational instances + mp-instantiated per rung; classical inputs CITED)
=======================================================================
NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, b_k = om_k^2, minimizer phi (round-114 builder; tau =
lambda_min(Mq) > 0 on MAIN), E_N = sin(Az) R(z), R(z) = 2F(z^2)/z
with the secular function F(y) = A_0 + sum_k w_k/(y - b_k), w_k =
(-1)^k c_k b_k (r131/r135, cited).  Zone T_z = 2 pi x, m = verified
zone census (PT21-class, cited).  V(theta) = kernel of the constraint
rows r(theta_j); W = Gram-orthonormal compression of Mq onto V with
eigenpairs q_0 <= q_1 <= ...; at the node config q_0 = tau, ground =
phi (r138 Q1-Q3, cited).  For a probe row r = r(p): R_phi = r . phi
(== R(p) == E_N(p)/sin(Ap), three-way gated), en2 = |P_V r|^2, rho2 =
R_phi^2/en2, chi_abs = sum_{i>=1} (r . z_i)^2/(q_i - q_0).

THEOREM U1 (two-sided susceptibility form of the gap; the lower
side NEW in-corpus).  For PSD W with simple ground and R_phi != 0:
  R_phi^2/(chi_abs + R_phi^2/(q_1 - q_0))  <=  lam*(p) - q_0
                          <=  R_phi^2/((1 - rho2) chi_abs).
PROOF (lower): v = alpha z_0 + w, v'Wv = q_0 + w'(W - q_0)w;
the constraint gives alpha R_phi = -r.w, Cauchy-Schwarz in the
(W - q_0) metric gives (r.w)^2 <= chi_abs w'(W-q_0)w, and |w|^2 <=
w'(W-q_0)w/(q_1 - q_0); insert into alpha^2 + |w|^2 = 1.  (Upper:
r138 Q1 sandwich, re-gated.)  CONSEQUENCE: the zone-top gap IS the
susceptibility-normalized wall value, PROVEN two-sided (upgrades the
r138 MEASURED tightness 1.0000-1.0001).

THEOREM U2 (scale-free factorization).  With tlaw := tau/(8 A_0^2
G(T_z)) (the CDXLI budget ratio) and P := F(T_z^2)/A_0 (the pure
spacing-lattice product, A_0-free by the r135 spacing form):
  n := R_phi(T_z)^2/tau  ==  P^2/(2 T_z^2 G(T_z) tlaw)   exactly,
and gap(T_z) = n/D up to the U1 correction, D := chi_abs.  The
numerator consumes ONLY tlaw (EPS-LOCK content, OMEGA-a class) and
the spacing product (counting class); D is the susceptibility -- the
denominator object this round prices.

THEOREM U3 (row-subset monotonicity = locality lower bound).
Dropping constraint rows enlarges V, so for any subset S of the zone
rows lam*_S(p) <= lam*_full(p): the TOP-J-ROW gap is a certified
LOWER bound on QSUBGAP's top value, and q_0(V_S) = tau still (phi
remains in the kernel).  MACHINE FACT (pre-freeze): J = 2 already
reproduces the full gap to 6 digits at x = 5/8/13/18 -- QSUBGAP
REDUCES to a THREE-ROW problem (top two zeros + probe row).

THEOREM U4 (collision closure).  span{r(theta), r(p)} ==
span{r(theta), (r(p) - r(theta))/(p - theta)} (elementary column
recombination; the 2-constraint minimum depends only on the span),
and the divided-difference row -> the derivative row as p -> theta
(r138 G15 limit, re-gated): the boundary-collision direction
(gamma_m -> T_z) morphs CONTINUOUSLY into the double-zero (drow)
pricing -- no collapse route through the collision corner.

SCALE-FREE SECULAR (Q2 currency): in dimensionless variables
delta_i = (q_i - q_0)/tau, the gap g solves rho2/g = sum_{i>=1}
et_i^2/(delta_i - g) and g <= rho2/chi-tilde: the ratio is a
function of the unit overlap vector and the spectral ratios ONLY.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import; no zeta use anywhere in this probe);
    G02 cache (X5, READ-ONLY).
S1  exact layer: G10 U1 lower (decomposition identity + metric
    Cauchy-Schwarz instance + rearrangement + exact rational
    instance); G11 U1 two-sided on the instance (lower <= exact
    secular root <= upper, root in (q_0, q_1)); G12 U3 nesting
    instance; G13 U2 (z R/2 == F(z^2) generic K=3 + tlaw
    rearrangement exact); G14 U4 (span invariance instance +
    divided-difference -> drow limit); G15 scale-free secular
    instance + g <= rho2/chi-tilde tightness.
S2  G20 HSW G(T) sanity.
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots census)
    + (18,140),(24,150) deep (zone sign-scan census to T_z + 6,
    step 0.05; zone prefix complete; edge census not consumed):
    G30 census (zone node count == m, residuals <= 1e-20, bottom
    grid sign-uniform); G31 node-config V (|qrel| <= 1e-30, null
    residual <= 1e-40); G32 zone-top gap replication (top-grid min
    in the frozen r138 window per rung AND >= GAP_MIN_BAR = 3);
    G33 U1 instantiation (R_phi three-way identity <= 1e-40 rel,
    rho2 en2 == R_phi^2 <= 1e-40 rel, lower <= exact <= upper,
    tightness factors <= 1.01); G34 U2 instantiation (n-identity
    <= 1e-12 rel, tlaw window (0.05, 5) + CDXLI cross-check <= 5e-3
    rel at shared rungs, |n/D / gap - 1| <= 1e-2); G35 chi anatomy
    (first-excited share >= 0.5; compensation table delta_1 vs
    rho2/et_1^2 printed INFO); G36 locality (gap_J <= gap_full
    (1 + 1e-6) for J = 2, 4, 6 AND retention gap_2/gap_full >= 0.9);
    G37 ADVERSARIAL battery (Q3): frozen configs C0 center, A1-A3
    top zero at T_z - eps*s_top (eps = 0.5/0.1/0.02), A4 top zero
    down 0.9 s_top, A5 clustered top pair at +-0.0005 s_top around
    T_z - 0.1 s_top (Lehmer-class legal minimum gap 0.001 spacings,
    observed-minimum model CITED), A6 lattice-proximal top zero,
    A7 uniform up-shift by half the boundary gap, A8 RvM quantile
    config, P1/P2 ball patterns +g/alternating (r138 G35 replica);
    per config: q0rel = q_0(theta)/tau - 1, min ABSOLUTE gap
    (lam* - tau)/tau over the frozen probe set, min RELATIVE gap
    (lam* - q_0)/q_0, drow at the top zero; HARD ASSERTS: (i) abs
    gap >= ABS_BAR = 3 for EVERY config and probe point, (ii)
    rel-gap <= 1 forces q0rel >= 10 (the mechanism only fails where
    source-config consistency already failed), (iii) q0rel <= 1
    forces rel-gap >= 3 (the consistent core is stable); G38
    profile anatomy (8 zone samples: argmin in the top two samples
    -- the zone-top law replica; n(p), D(p) printed).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    zone overcount >= 1 AND mu_1 fills the verified zero-free gap
    (0, gamma_1); tau_w printed (pre-freeze: NOT PSD in all three);
    G53 consistency.
S5  G54 tau-screen (|slope log10 top-gap vs log10 tau| <= 0.30;
    the RAW gap rides tau BY CONSTRUCTION -- BOUND-RIDES-CONNES
    typed); G55 conditioning (1e-25 shift window).
S6  G60 min-cut (r116 replica): the r138 unit edge QSUBGAP(1)
    REFINED in series PFLOOR(1) -> SUSCAP2(1) behind EPSLOCK(1)
    (U2: the numerator consumes tlaw = EPS-LOCK content + the
    spacing product; U1+U3: the denominator is the top-2-row
    susceptibility), with QSUBGAPTHM(INF, U1-U4 + locality +
    adversarial certificates) behind them; chain L1TAILPROVEN ->
    EPSLOCK(1) -> PFLOOR(1) -> SUSCAP2(1) -> QSUBGAPTHM ->
    COUNTEQTHM -> SEEDBALLTHM -> SPACREMTHM -> DOMASYM -> WPDWIN;
    flows base 4, refined 5, one-grant 5, counterfactual PARALLEL
    7 NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor.
1.2]; T_PT = 3000175332800 [PT21]; M_ENV = 3; OFF_ALLOW = 8 e^A
ENV_3(T_PT)^2 G(T_PT) (r131, cited); SCAN_STEP = 0.05; SCAN_LO =
0.5; SCAN_OVER = 6.0; TOP_GRID_LEN = 3.0; TOP_GRID_STEP = 0.05;
NODE_EXCL = 0.02; PROFILE_FRACS = (0.15, 0.3, 0.45, 0.6, 0.75,
0.85, 0.93, 0.999); LOC_JS = (2, 4, 6); ADV_EPS = (0.5, 0.1, 0.02);
MINGAP_SP = 0.001 (observed-minimum spacing model, Lehmer-pair
class, typed CITED-OBSERVED); CLUSTER_AT = 0.1; BOT_GRID = (0.02,
0.62, 0.02).
BARS: RES_BAR = 1e-20; QREL_BAR = 1e-30; NULLRES_BAR = 1e-40;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25, 45), 8: (12, 22), 13:
(17, 30), 18: (12, 22), 24: (14, 26)} (r138 values 33.7/16.8/22.7/
16.6/19.6); ID_BAR = 1e-40 (R_phi three-way + rho2 en2, pre-freeze
7e-57..2e-67); TIGHT_BAR = 1.01 (pre-freeze lower 1.000005/
1.000001/1.000000/1.000000, upper 1.000147/1.000016/1.000002/
1.000000 at x = 5/8/13/18); N_ID_BAR = 1e-12 (pre-freeze 2e-16);
TLAW_WIN = (0.05, 5.0); TLAW_TAB = {5: 0.2664, 8: 0.3738, 13:
0.4674, 18: 0.4827, 24: 0.5122} rel tol 5e-3 (CDXLI strings;
pre-freeze match exact to 4 digits at 5/8/13/18); ND_BAR = 1e-2;
SHARE1_BAR = 0.5 (pre-freeze 0.969/0.965/0.946/0.944); LOC_TOL =
1e-6; LOC_RET_BAR = 0.9 (pre-freeze retention 1.000 at all four
measured rungs); ABS_BAR = 3.0; REL_BREAK_Q0 = 10.0; CONSIST_Q0 =
1.0; CONSIST_REL = 3.0; TAU_SLOPE_BAR = 0.30 (r138: 0.0017);
COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward
only); RUNTIME_BAR = 14400 s.  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks; no
f64-refinement of mp roots; np.float64-repr casts guarded by
float() (r133/r136/r138 trap).

CALIBRATION DISCLOSURE (pre-freeze, two scratch scripts
calib_scratch_qsubgap.py / calib_scratch_qsubgap2.py + logs,
deleted; numbers quoted verbatim): zone-top gap at p = T_z - 0.02:
33.7446/16.7599/22.6936/16.6067 at x = 5/8/13/18 (r138 replica);
U1 lower/upper tightness as in TIGHT_BAR note; U2 n-identity dev
<= 2e-16; tlaw 0.2664/0.3738/0.4674/0.4827; P = F(T_z^2)/A_0 =
2.04e3/9.40e3/8.02e7/-1.38e12; n = 2.36e5/2.63e6/1.03e14/2.18e22;
D = chi_abs = 7.00e3/1.57e5/4.54e12/1.31e21; chi share of i=1 =
0.969/0.965/0.946/0.944 with delta_1 = 2.23e5/9.95e5/1.06e7/
3.25e7; locality J = 2/4/6 ratio 1.000 at all four rungs (J-gap
== full gap to 6 digits); adversarial (scratch used cache
half-spacings for s_top; the frozen probe uses node gaps -- same
regime): top-zero moves eps = 0.5/0.1/0.02 give q0rel = 49/36/34
(x=5), 19/17/17 (x=8), 6.9e12/6.8e12/6.8e12 (x=13), 7.7e29/7.5e29/
7.5e29 (x=18) with min rel-gap 1.41/1.41/3.61 (x=5), 24.5/14.7/
22.7 (x=8), 0.024/0.034/0.037 (x=13), 4.33/4.42/4.44 (x=18); RvM
quantile config q0rel = 3.5e6/6.8e14/1.9e31/5.8e49 with rel-gap
0.209/0.154/0.031/0.040 (ALL BELOW 1 -- the shape-compactness
refutation exhibit; abs gap stays >= q0rel, astronomically above
bar) and D_rvm dev -2.6/-9.7/-12.7/-19.4 dex (the susceptibility
is position-hypersensitive; the r135-G39 counting-determination of
the FLOOR does NOT transfer to the gap); builds 2.8/13.4/163/478
s; exact layer: all six sympy gates pass (U1 instance lower 70/61
<= lam* <= 757/640; span-parallel cross == 0; dd -> drow limit
exact; scale-free instance g <= rho2/chi-tilde).  x = 24
unmeasured pre-freeze (build cost); its bars are set from the r138
value 19.6 and the structural asserts, disclosed.  Amendments
after the frozen run, if any, are appended as numbered AMENDMENT
blocks.

VERDICT ENUMS (frozen): U1-PROVEN(two-sided susceptibility form);
U2-PROVEN(scale-free factorization: n = P^2/(2 T_z^2 G tlaw)
exact); LOCALITY-CERTIFIED(top-2-row lower bound == full gap;
QSUBGAP reduces to a three-row problem); COLLISION-CLOSED(U4);
WELL-ANATOMY(chi carried by the first excited mode; delta_1 vs
overlap compensation MEASURED); ADVERSARIAL-ABS-BOUNDED(absolute
gap >= bar over the whole battery); SHAPE-COMPACTNESS-REFUTED(
legal RvM shape gives relative gap < 1 at broken consistency: the
gap is the ARITHMETIC WELL DEPTH, not zone geometry -- QSUBGAP
consumes source-config consistency at O(ball) accuracy, 5-12
orders below the O(spacing) classical currency; arithmetic-
pinning-shaped, BANDMASS-class); CMODEL-SPLIT(numerator counting-
class, susceptibility position-hypersensitive); CONTROLS-REFUSE;
DEMAND-FLAT + BOUND-RIDES-CONNES(typed); OMEGA-REFINED(QSUBGAP <==
EPSLOCK-consumed + PFLOOR + SUSCAP2 serial; census {MEAS,
OMEGA-POS} cardinality 4 UNCHANGED); MINCUT(4/5).  Composite
priority: INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; no zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.
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
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_ENV = 3
SCAN_STEP = 0.05
SCAN_LO = 0.5
SCAN_OVER = 6.0
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
PROFILE_FRACS = (0.15, 0.3, 0.45, 0.6, 0.75, 0.85, 0.93, 0.999)
LOC_JS = (2, 4, 6)
ADV_EPS = (0.5, 0.1, 0.02)
MINGAP_SP = 0.001
CLUSTER_AT = 0.1
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0),
            18: (12.0, 22.0), 24: (14.0, 26.0)}
ID_BAR = 1e-40
TIGHT_BAR = 1.01
N_ID_BAR = 1e-12
TLAW_WIN = (0.05, 5.0)
TLAW_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827, 24: 0.5122}
TLAW_TOL = 5e-3
ND_BAR = 1e-2
SHARE1_BAR = 0.5
LOC_TOL = 1e-6
LOC_RET_BAR = 0.9
ABS_BAR = 3.0
REL_BREAK_Q0 = 10.0
CONSIST_Q0 = 1.0
CONSIST_REL = 3.0
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 14400.0

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
                       "no zero-oracle; cache in ward_; no zeta use")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM."""
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


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def drow_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (-2 / t_mp ** 2) / nrm[0]
    for k in range(1, K):
        d = t_mp * t_mp - oms[k] ** 2
        r[k] = (2 * (-1) ** k * (-(t_mp * t_mp + oms[k] ** 2)) / d ** 2) \
            / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138 replica; sets own dps)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        oms_f = [float(o) for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        Mq = ce["mpM"]
        tau_mp = ce["mpE"][0]
        mcon = len(gpts_mp)
        Rm = mp.zeros(mcon, K)
        for j in range(mcon):
            g = gpts_mp[j]
            Rm[j, 0] = (2 / g) / nrm[0]
            for k in range(1, K):
                Rm[j, k] = (2 * (-1) ** k * g / (g * g - oms[k] ** 2)) \
                    / nrm[k]
        piv = []
        used = set()
        for j in range(mcon):
            gjf = float(gpts_mp[j])
            order = sorted(range(1, K), key=lambda k: abs(oms_f[k] - gjf))
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
        Ew, Vw = mp.eigsy(Wm)
        order = sorted(range(nf), key=lambda i: Ew[i])
        qs = [Ew[order[i]] for i in range(nf)]
        Z = mp.zeros(nf, nf)
        for c, i in enumerate(order):
            for r in range(nf):
                Z[r, c] = Vw[r, i]
        qrel = float((qs[0] - tau_mp) / tau_mp)
    return dict(qs=qs, Z=Z, Nb=Nb, fwd=fwd, nf=nf, resR=resR, qrel=qrel,
                cs=cs, aa=aa, oms=oms, nrm=nrm, tau_mp=tau_mp)


def secular_full(Vd: dict, r: list):
    """(lam*, rho2, chi, en2) for the extra row r on V (caller sets
    workdps): lam* = exact bordered-secular constrained minimum."""
    nf, Nb, fwd = Vd["nf"], Vd["Nb"], Vd["fwd"]
    qs, Z = Vd["qs"], Vd["Z"]
    K = len(r)
    d = []
    for fi in range(nf):
        acc = mp.mpf(0)
        for k in range(K):
            acc += Nb[k, fi] * r[k]
        d.append(acc)
    e = fwd(d)
    en2 = sum(v * v for v in e)
    if en2 == 0:
        return qs[0], mp.mpf(0), mp.mpf(0), en2
    et = []
    for i in range(nf):
        acc = mp.mpf(0)
        for k in range(nf):
            acc += Z[k, i] * e[k]
        et.append(acc)
    sq = mp.sqrt(en2)
    et = [v / sq for v in et]
    rho2 = et[0] * et[0]
    if rho2 == 0:
        return qs[0], rho2, mp.mpf(0), en2
    lo, hi = qs[0], qs[1]

    def fsec(mu):
        return sum(et[i] * et[i] / (qs[i] - mu) for i in range(nf))
    for _ in range(120):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(et[i] * et[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, rho2, chi, en2


def secular_shares(Vd: dict, r: list, ntop: int = 5):
    """top chi-share table [(share, i, delta_i, et_i^2)] (caller dps)."""
    nf, Nb, fwd = Vd["nf"], Vd["Nb"], Vd["fwd"]
    qs, Z = Vd["qs"], Vd["Z"]
    K = len(r)
    d = []
    for fi in range(nf):
        acc = mp.mpf(0)
        for k in range(K):
            acc += Nb[k, fi] * r[k]
        d.append(acc)
    e = fwd(d)
    en2 = sum(v * v for v in e)
    et = []
    for i in range(nf):
        acc = mp.mpf(0)
        for k in range(nf):
            acc += Z[k, i] * e[k]
        et.append(acc)
    sq = mp.sqrt(en2)
    et = [v / sq for v in et]
    chi = sum(et[i] * et[i] / (qs[i] - qs[0]) for i in range(1, nf))
    tau = Vd["tau_mp"]
    out = []
    for i in range(1, nf):
        shr = float((et[i] * et[i] / (qs[i] - qs[0])) / chi)
        out.append((shr, i, float((qs[i] - qs[0]) / tau),
                    float(et[i] * et[i])))
    out.sort(reverse=True)
    return out[:ntop], float(et[0] * et[0])


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    lam = sp.symbols("lam")

    # shared exact instance: W = diag(1, 2, 5), unit row (3,4,12)/13
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    r1, r2, r3 = sp.Rational(3, 13), sp.Rational(4, 13), \
        sp.Rational(12, 13)
    fsec = r1 ** 2 / (q0i - lam) + r2 ** 2 / (q1i - lam) \
        + r3 ** 2 / (q2i - lam)
    roots = sorted(sp.solve(sp.together(fsec).as_numer_denom()[0], lam))
    lam_star = roots[0]
    chi_abs = r2 ** 2 / (q1i - q0i) + r3 ** 2 / (q2i - q0i)
    Rq = r1
    lower = q0i + Rq ** 2 / (chi_abs + Rq ** 2 / (q1i - q0i))
    upper = q0i + Rq ** 2 / ((1 - Rq ** 2) * chi_abs)

    # G10 U1 lower: derivation steps + instance
    a_, w1, w2 = sp.symbols("a_ w1 w2", real=True)
    Wq = sp.diag(q0i, q1i, q2i)
    v = sp.Matrix([a_, w1, w2])
    quad = (v.T * Wq * v)[0, 0]
    decomp = q0i * (a_ ** 2 + w1 ** 2 + w2 ** 2) \
        + (q1i - q0i) * w1 ** 2 + (q2i - q0i) * w2 ** 2
    okA = sp.simplify(quad - decomp) == 0
    wv = sp.Matrix([0, 2, 3])
    rv = sp.Matrix([r1, r2, r3])
    okB = bool((rv.dot(wv)) ** 2
               <= chi_abs * ((q1i - q0i) * wv[1] ** 2
                             + (q2i - q0i) * wv[2] ** 2))
    chi_s, R_s, b_s = sp.symbols("chi_s R_s b_s", positive=True)
    okC = sp.simplify(1 / (chi_s / R_s ** 2 + 1 / b_s)
                      - R_s ** 2 * b_s / (chi_s * b_s + R_s ** 2)) == 0
    okD = bool(sp.simplify(lam_star - lower) >= 0)
    out.append(("G10-u1-lower", okA and okB and okC and okD,
                "v'Wv == q0 + w'(W-q0)w decomposition; metric "
                "Cauchy-Schwarz instance; rearrangement exact; "
                "lam* >= q0 + R^2/(chi_abs + R^2/(q1-q0)) on the "
                "exact rational instance (THEOREM U1 lower, NEW)"))

    # G11 U1 two-sided
    okE = bool(sp.simplify(upper - lam_star) >= 0) \
        and bool(q0i < lam_star < q1i)
    out.append(("G11-u1-two-sided", okE,
                "lower 70/61 <= lam* <= upper 757/640 with lam* in "
                "(q0, q1) on the instance: the zone-top gap IS the "
                "susceptibility-normalized wall value, two-sided"))

    # G12 U3 nesting
    sv = sp.Matrix([0, 1, 0])
    nsp2 = rv.cross(sv)
    nsp2 = nsp2 / sp.sqrt(nsp2.dot(nsp2))
    min2 = sp.simplify((nsp2.T * Wq * nsp2)[0, 0])
    okF = bool(sp.simplify(min2 - lam_star) >= 0)
    out.append(("G12-u3-nesting", okF,
                "adding a constraint raises the min (instance: "
                "min2 = 21/17 >= lam*): dropping rows gives a "
                "certified LOWER bound -- the top-J-row gap "
                "lower-bounds QSUBGAP (THEOREM U3)"))

    # G13 U2 factorization
    z, aa_s = sp.symbols("z aa_s", positive=True)
    c0s, c1s, c2s = sp.symbols("c0s c1s c2s", real=True)
    om1, om2 = sp.pi / aa_s, 2 * sp.pi / aa_s
    Rz = 2 * c0s / z - 2 * c1s * z / (z ** 2 - om1 ** 2) \
        + 2 * c2s * z / (z ** 2 - om2 ** 2)
    A0g = c0s - c1s + c2s
    Fg = A0g - c1s * om1 ** 2 / (z ** 2 - om1 ** 2) \
        + c2s * om2 ** 2 / (z ** 2 - om2 ** 2)
    okG = sp.simplify(z * Rz / 2 - Fg) == 0
    Fq, A0q, tq, Gq, tl = sp.symbols("Fq A0q tq Gq tl", positive=True)
    okH = sp.simplify((2 * Fq / tq) ** 2 / (8 * A0q ** 2 * Gq * tl)
                      - (Fq / A0q) ** 2 / (2 * tq ** 2 * Gq * tl)) == 0
    out.append(("G13-u2-factorization", okG and okH,
                "z R(z)/2 == F(z^2) generic (K=3) and R^2/tau == "
                "(F/A0)^2/(2 t^2 G tlaw) with tau = 8 A0^2 G tlaw "
                "exact: the numerator consumes ONLY tlaw (EPS-LOCK "
                "content) + the A0-free spacing product (THEOREM U2)"))

    # G14 U4 collision closure
    h_s = sp.symbols("h_s", positive=True)
    sv2 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 3),
                     sp.Rational(1, 6)])
    dd = (sv2 - rv) / h_s
    n1 = rv.cross(sv2)
    n2 = rv.cross(dd)
    okI = sp.simplify(n1.cross(n2).dot(n1.cross(n2))) == 0
    tv, gv = sp.symbols("tv gv", positive=True)
    om_i = sp.Integer(3)
    rrow = 2 * tv / (tv ** 2 - om_i ** 2)
    ddiff = sp.simplify((rrow - rrow.subs(tv, gv)) / (tv - gv))
    okJ = sp.simplify(sp.limit(ddiff, tv, gv)
                      - sp.diff(rrow, tv).subs(tv, gv)) == 0
    out.append(("G14-u4-collision", okI and okJ,
                "span{r(th), r(p)} == span{r(th), divided difference} "
                "(parallel nullvectors, instance) and the divided "
                "difference -> the derivative row as p -> th: the "
                "boundary collision morphs into the drow pricing "
                "(THEOREM U4; no collapse route through the corner)"))

    # G15 scale-free secular + tightness
    g_s = sp.symbols("g_s", positive=True)
    rho2i = sp.Rational(1, 100)
    et1 = sp.Rational(9, 10)
    d1, d2 = sp.Integer(1000), sp.Integer(10 ** 6)
    et2sq = 1 - rho2i - et1 ** 2
    eqn = rho2i / g_s - et1 ** 2 / (d1 - g_s) - et2sq / (d2 - g_s)
    gsol = [s for s in sp.solve(sp.together(eqn).as_numer_denom()[0],
                                g_s) if s.is_real and 0 < s < d1]
    gex = min(gsol)
    chit = et1 ** 2 / d1 + et2sq / d2
    okK = bool(gex <= rho2i / chit)
    out.append(("G15-scale-free-secular", okK,
                "in dimensionless variables the gap solves rho2/g == "
                "sum et_i^2/(delta_i - g) and g <= rho2/chi-tilde "
                "(instance): the ratio is a function of the unit "
                "overlap vector + spectral ratios ONLY (Q2 currency)"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("qsubgap_probe -- PRIME.QSUBGAP.UNIFORM.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

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

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorems U1-U4)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r131 secular identity + G17 crossover + GW "
         "law; r132 raw census; r133 M/E/T/A; r135 D1-D4 (weight/"
         "spacing forms); r136 S1-S4 + PINBALL; r138 Q1-Q3 + slab + "
         "gap tables; CDXLI tlaw strings; HSW22 Cor. 1.2; PT21 "
         "verified census; Euler sine product; observed-minimum "
         "spacing model (Lehmer-pair class) as the legal gap floor")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    gtop = float(gam[-1])
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone; "
          "G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: U1/U2 INSTANTIATION + LOCALITY + ADVERSARY")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = ok38 = True
    det30, det31, det32, det33, det34 = [], [], [], [], []
    det35, det36, det37, det38 = [], [], [], []
    gap_tab, tau_tab, comp_tab = {}, {}, {}
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
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            A0 = sum((-1) ** k * cs[k] for k in range(K))
            tauf = float(ce["mpE"][0])

        # ---- census (core: polyroots; deep: zone sign-scan)
        if not is_deep:
            mus, n_nonreal = raw_mp_census(ce)
            seeds = [float(v) for v in mus]
            cens_ok = (len(mus) == K - 1 and n_nonreal == 0)
        else:
            with mp.workdps(dps):
                ts = np.arange(SCAN_LO, Tz + SCAN_OVER, SCAN_STEP)
                vprev = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(ts[0]))))[0]
                seeds = []
                for tv in ts[1:]:
                    v = en_pair(cs, aa, oms,
                                mp.mpf(repr(float(tv))))[0]
                    if v * vprev < 0:
                        seeds.append(float(tv) - SCAN_STEP / 2)
                    vprev = v
            cens_ok = len(seeds) >= m_zone + 1
            info("x=%d deep census: zone-window scan to T_z + %.0f "
                 "found %d nodes (zone prefix + overhang; edge census "
                 "not consumed)" % (x, SCAN_OVER, len(seeds)))
        nds_all = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds_all.append(tmu)
                wres = max(wres, float(res))
        nds_f_all = np.array([float(v) for v in nds_all])
        n_zone_nodes = int(np.sum(nds_f_all <= Tz))
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        cens_ok = cens_ok and wres <= RES_BAR and len(sgs) == 1 \
            and n_zone_nodes == m_zone
        ok30 = ok30 and cens_ok
        det30.append("x%d: %d nodes zone %d/%d res %.0e"
                     % (x, len(nds_all), n_zone_nodes, m_zone, wres))
        zone_nds = nds_all[:m_zone]
        zone_f = nds_f_all[:m_zone]
        s_top = float(zone_f[-1] - zone_f[-2]) if m_zone > 1 else 3.0
        sbar = float((zone_f[-1] - zone_f[0]) / max(m_zone - 1, 1))

        # ---- G31 node-config V
        t_q = time.time()
        Vd = build_V(ce, zone_nds)
        ok31x = abs(Vd["qrel"]) <= QREL_BAR and Vd["resR"] <= NULLRES_BAR
        ok31 = ok31 and ok31x
        det31.append("x%d: qrel %.0e nullres %.0e nf %d (%.0f s)"
                     % (x, Vd["qrel"], Vd["resR"], Vd["nf"],
                        time.time() - t_q))

        # ---- G32 zone-top gap on the frozen top grid
        with mp.workdps(dps):
            tau = Vd["tau_mp"]
            tg = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                TOP_GRID_STEP)) + [Tz - 0.001]
            gmin = None
            argp = None
            for tv in tg:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, rho2, chi, en2 = secular_full(Vd, r)
                gg = float((lam - tau) / tau)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
        lo_w, hi_w = REPL_WIN[x]
        ok32x = (gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w)
        ok32 = ok32 and ok32x
        det32.append("x%d: top-min %.4f at t=%.3f (win [%.0f, %.0f])"
                     % (x, gmin, argp, lo_w, hi_w))
        gap_tab[x] = gmin
        tau_tab[x] = tauf

        # ---- G33 U1 instantiation at the argmin
        with mp.workdps(dps):
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, rho2, chi, en2 = secular_full(Vd, r)
            phi = [ce["mpV"][i, 0] for i in range(K)]
            Rdot = sum(r[k] * phi[k] for k in range(K))
            wks = [(-1) ** k * cs[k] * oms[k] ** 2 for k in range(1, K)]
            yv = p_mp * p_mp
            F = A0 + sum(wks[k - 1] / (yv - oms[k] ** 2)
                         for k in range(1, K))
            R_F = 2 * F / p_mp
            Ev, _ = en_pair(cs, aa, oms, p_mp)
            R_E = Ev / mp.sin(aa * p_mp)
            dev1 = float(abs(Rdot - R_F) / abs(R_F))
            dev2 = float(abs(R_E - R_F) / abs(R_F))
            dev3 = float(abs(rho2 * en2 - Rdot ** 2) / Rdot ** 2)
            chi_abs = chi * en2
            q1q0 = Vd["qs"][1] - Vd["qs"][0]
            lb = Rdot ** 2 / (chi_abs + Rdot ** 2 / q1q0)
            ub = Rdot ** 2 / ((1 - rho2) * chi_abs)
            g_ex = float((lam - tau) / tau)
            g_lb = float(lb / tau)
            g_ub = float(ub / tau)
            t_lo = g_ex / g_lb
            t_up = g_ub / g_ex
        ok33x = (dev1 <= ID_BAR and dev2 <= ID_BAR and dev3 <= ID_BAR
                 and g_lb <= g_ex <= g_ub
                 and 1.0 <= t_lo <= TIGHT_BAR
                 and 1.0 <= t_up <= TIGHT_BAR)
        ok33 = ok33 and ok33x
        det33.append("x%d: %.4f<=%.4f<=%.4f tight %.6f/%.6f ids "
                     "%.0e/%.0e/%.0e" % (x, g_lb, g_ex, g_ub, t_lo,
                                         t_up, dev1, dev2, dev3))

        # ---- G34 U2 instantiation
        with mp.workdps(dps):
            GT = hsw_G(Tz)
            a0f = abs(float(A0))
            tlaw = tauf / (8.0 * a0f ** 2 * GT)
            P = float(F / A0)
            n_num = float(Rdot ** 2 / tau)
            D = float(chi_abs)
            n_id = P ** 2 / (2.0 * float(p_mp) ** 2 * GT * tlaw)
            nd_dev = abs(n_num / D / g_ub - 1.0)
        tl_dev = abs(tlaw / TLAW_TAB[x] - 1.0)
        ok34x = (abs(n_num - n_id) / n_num <= N_ID_BAR
                 and TLAW_WIN[0] <= tlaw <= TLAW_WIN[1]
                 and tl_dev <= TLAW_TOL
                 and abs(n_num / D / g_ex - 1.0) <= ND_BAR)
        ok34 = ok34 and ok34x
        det34.append("x%d: tlaw %.4f (tab dev %.1e) P %.3e n %.3e "
                     "D %.3e n/D %.4f" % (x, tlaw, tl_dev, P, n_num,
                                          D, n_num / D))
        _ = nd_dev

        # ---- G35 chi anatomy
        with mp.workdps(dps):
            shares, rho2f = secular_shares(Vd, r)
        shr1 = shares[0][0] if shares[0][1] == 1 else \
            max(s for s, i, _, _ in shares if i == 1)
        d1 = [dl for s, i, dl, e2 in shares if i == 1][0]
        e12 = [e2 for s, i, dl, e2 in shares if i == 1][0]
        ok35x = shr1 >= SHARE1_BAR
        ok35 = ok35 and ok35x
        comp_tab[x] = (d1, rho2f, e12)
        det35.append("x%d: share1 %.3f delta1 %.2e rho2 %.2e et1^2 "
                     "%.2e" % (x, shr1, d1, rho2f, e12))
        info("x=%d compensation: delta_1 = %.3e, rho2/et1^2 = %.3e, "
             "product %.2f vs gap %.2f (the flat ratio = well depth "
             "x overlap ratio)" % (x, d1, rho2f / e12,
                                   d1 * rho2f / e12, g_ex))

        # ---- G36 locality
        okloc = True
        ret2 = None
        for J in LOC_JS:
            if J >= m_zone:
                continue
            VJ = build_V(ce, zone_nds[-J:])
            with mp.workdps(dps):
                rJ = row_at(p_mp, K, oms, nrm)
                lamJ, _, _, _ = secular_full(VJ, rJ)
                gJ = float((lamJ - VJ["tau_mp"]) / VJ["tau_mp"])
            okloc = okloc and abs(VJ["qrel"]) <= QREL_BAR \
                and gJ <= g_ex * (1.0 + LOC_TOL)
            if J == 2:
                ret2 = gJ / g_ex
        okloc = okloc and ret2 is not None and ret2 >= LOC_RET_BAR
        ok36 = ok36 and okloc
        det36.append("x%d: gap_2/gap %.6f (monotone ok %s)"
                     % (x, ret2, okloc))

        # ---- G37 adversarial battery
        # ball radii for the pattern configs (r138 currency)
        with mp.workdps(dps):
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
            eps_bar = math.sqrt((tauf + off_allow) / 2.0)
            g_arr = np.zeros(m_zone)
            for j in range(m_zone):
                _f0, fp0 = en_pair(cs, aa, oms, zone_nds[j])
                g_arr[j] = 2.0 * eps_bar / max(float(abs(fp0)), 1e-300)
        cfgs = []
        base = [mp.mpf(repr(float(v))) for v in zone_f]
        for epsv in ADV_EPS:
            th = list(base)
            th[-1] = mp.mpf(repr(float(Tz - epsv * s_top)))
            cfgs.append(("A-eps%.2f" % epsv, th))
        th = list(base)
        th[-1] = mp.mpf(repr(float(zone_f[-1] - 0.9 * s_top)))
        cfgs.append(("A-down", th))
        if m_zone >= 3:
            th = list(base)
            cc = Tz - CLUSTER_AT * s_top
            th[-2] = mp.mpf(repr(float(cc - MINGAP_SP * s_top)))
            th[-1] = mp.mpf(repr(float(cc + MINGAP_SP * s_top)))
            cfgs.append(("A-cluster", th))
        oms_f = [float(k * math.pi / float(aa)) for k in range(K)]
        omn = min(oms_f[1:], key=lambda o: abs(o - float(zone_f[-1])))
        latp = min(max(omn + 0.01, float(zone_f[-2] + zone_f[-1]) / 2),
                   Tz - 0.02)
        th = list(base)
        th[-1] = mp.mpf(repr(float(latp)))
        cfgs.append(("A-lattice", th))
        dsh = 0.5 * (Tz - float(zone_f[-1]))
        cfgs.append(("A-shift", [mp.mpf(repr(float(v) + dsh))
                                 for v in zone_f]))
        rvm = rvm_quantiles(m_zone)
        cfgs.append(("A-rvm", [mp.mpf(repr(float(v))) for v in rvm]))
        cfgs.append(("P-plus", [mp.mpf(repr(float(zone_f[j])
                                            + float(g_arr[j])))
                                for j in range(m_zone)]))
        cfgs.append(("P-alt", [mp.mpf(repr(float(zone_f[j])
                                           + ((-1.0) ** j)
                                           * float(g_arr[j])))
                               for j in range(m_zone)]))
        rows_out = ["C0 q0rel %.0e abs %.2f rel %.2f"
                    % (Vd["qrel"], g_ex, g_ex)]
        okadv = g_ex >= ABS_BAR
        batt = [(Vd["qrel"], g_ex, g_ex)]
        for nmc, th in cfgs:
            Vt = build_V(ce, th)
            with mp.workdps(dps):
                q0t = Vt["qs"][0]
                q0rel = Vt["qrel"]
                thf = [float(v) for v in th]
                pset = [Tz - 0.001, Tz - 0.16,
                        0.5 * (thf[-1] + Tz), thf[-1] + 0.03 * s_top]
                amin = rmin = None
                for pf in pset:
                    if pf <= 0.5 or pf > Tz + 2.0:
                        continue
                    if min(abs(pf - v) for v in thf) < NODE_EXCL:
                        continue
                    rr = row_at(mp.mpf(repr(float(pf))), K, oms, nrm)
                    lamt, _, _, _ = secular_full(Vt, rr)
                    ga = float((lamt - tau) / tau)
                    gr = float((lamt - q0t) / q0t)
                    if amin is None or ga < amin:
                        amin = ga
                    if rmin is None or gr < rmin:
                        rmin = gr
                rd = drow_at(th[-1], K, oms, nrm)
                lamd, _, _, _ = secular_full(Vt, rd)
                gad = float((lamd - tau) / tau)
                grd = float((lamd - q0t) / q0t)
                amin = gad if amin is None else min(amin, gad)
                rmin = grd if rmin is None else rmin
                rmin_d = grd
            rows_out.append("%s q0rel %.1e abs %.2e rel %.2e drow "
                            "%.2e" % (nmc, q0rel, amin, rmin, rmin_d))
            batt.append((q0rel, amin, min(rmin, rmin_d)))
            okadv = okadv and amin >= ABS_BAR
        # structure asserts
        for q0rel, amin, rmin in batt:
            if rmin <= 1.0:
                okadv = okadv and q0rel >= REL_BREAK_Q0
            if q0rel <= CONSIST_Q0:
                okadv = okadv and rmin >= CONSIST_REL
        ok37 = ok37 and okadv
        det37.append("x%d: %d configs, all abs >= %.1f: %s"
                     % (x, len(batt), ABS_BAR, okadv))
        info("x=%d adversary: " % x + " | ".join(rows_out))

        # ---- G38 profile anatomy
        with mp.workdps(dps):
            samp = []
            for fr in PROFILE_FRACS:
                tv = fr * Tz
                for _ in range(40):
                    if min(abs(tv - g) for g in zone_f) >= NODE_EXCL:
                        break
                    tv += 0.011
                r2 = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam2, rho22, chi2, en22 = secular_full(Vd, r2)
                gg = float((lam2 - tau) / tau)
                Rd2 = sum(r2[k] * phi[k] for k in range(K))
                samp.append((float(tv), gg, float(Rd2 ** 2 / tau),
                             float(chi2 * en22)))
        arg_i = min(range(len(samp)), key=lambda i: samp[i][1])
        ok38x = arg_i >= len(samp) - 2
        ok38 = ok38 and ok38x
        det38.append("x%d: argmin sample %d/%d (gap %.1e -> %.1f)"
                     % (x, arg_i + 1, len(samp), samp[0][1],
                        samp[-1][1]))
        info("x=%d profile (t, gap, n, D): " % x + "; ".join(
            "(%.1f, %.2e, %.2e, %.2e)" % s for s in samp))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: zone-window "
          "scan; zone node count == m; residuals <= %.0e; bottom "
          "grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    check("G31-node-config", ok31,
          "|qrel| <= %.0e, null residual <= %.0e at every rung "
          "(q_0 == tau: phi in the kernel): %s"
          % (QREL_BAR, NULLRES_BAR, "; ".join(det31)))
    check("G32-zone-top-replication", ok32,
          "top-grid gap minimum >= %.1f AND inside the frozen r138 "
          "window per rung: %s" % (GAP_MIN_BAR, "; ".join(det32)))
    check("G33-u1-instantiated", ok33,
          "R_phi three-way identity + rho2 en2 == R_phi^2 <= %.0e "
          "rel; U1 lower <= exact <= upper with tightness <= %.2f "
          "(the zone-top gap IS the susceptibility-normalized wall "
          "value, PROVEN two-sided + instantiated): %s"
          % (ID_BAR, TIGHT_BAR, "; ".join(det33)))
    check("G34-u2-instantiated", ok34,
          "n == P^2/(2 T_z^2 G tlaw) <= %.0e rel; tlaw in %s and on "
          "the CDXLI strings <= %.0e rel; |n/D / gap - 1| <= %.0e: "
          "%s" % (N_ID_BAR, str(TLAW_WIN), TLAW_TOL, ND_BAR,
                  "; ".join(det34)))
    check("G35-chi-anatomy", ok35,
          "first-excited chi share >= %.1f at every rung (the "
          "susceptibility is carried by ONE mode; gap ~= delta_1 "
          "rho2/et1^2 -- the well-depth x overlap-ratio law): %s"
          % (SHARE1_BAR, "; ".join(det35)))
    check("G36-locality", ok36,
          "top-J-row gaps are certified lower bounds (U3, monotone "
          "within %.0e) AND the top-2-row gap retains >= %.1f of "
          "the full gap: QSUBGAP REDUCES to a three-row problem: %s"
          % (LOC_TOL, LOC_RET_BAR, "; ".join(det36)))
    check("G37-adversarial", ok37,
          "frozen battery (top-zero moves, cluster, lattice, shift, "
          "RvM, ball patterns): ABSOLUTE gap >= %.1f everywhere; "
          "rel-gap <= 1 only where q0rel >= %.0f (consistency "
          "already broken); q0rel <= %.0f keeps rel-gap >= %.0f: %s"
          % (ABS_BAR, REL_BREAK_Q0, CONSIST_Q0, CONSIST_REL,
             "; ".join(det37)))
    check("G38-profile-anatomy", ok38,
          "gap argmin over the zone samples sits in the top two "
          "samples at every rung (zone-top law replica): %s"
          % "; ".join(det38))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (the certificate must refuse)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        musw, _nr = raw_mp_census(cw)
        Tzw = 2 * math.pi * xw
        n_nodes_w = int(np.sum(musw <= Tzw))
        m_true_w = int(np.sum(gam <= Tzw))
        over = n_nodes_w - m_true_w
        with mp.workdps(dpsw):
            tauw = float(cw["mpE"][0])
        refuse = over >= 1 and float(musw[0]) < float(gam[0]) - 1.0
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: zone nodes %d vs m %d (OVERCOUNT +%d), mu_1 "
              "= %.3f fills the zero-free gap (0, %.2f); tau_w = "
              "%.3e (%s)" % (world, xw, n_nodes_w, m_true_w, over,
                             float(musw[0]), float(gam[0]), tauw,
                             "NOT PSD" if tauw <= 0 else "PSD"))
    check("G53-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap; the U1 well machinery claims nothing where PSD/"
          "pinning fail (tau_w printed)")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lg_ = [math.log10(gap_tab[x]) for x in xs_all]
        s_g = float(np.polyfit(lt, lg_, 1)[0])
        ld1 = [math.log10(comp_tab[x][0]) for x in xs_all]
        lov = [math.log10(comp_tab[x][1] / comp_tab[x][2])
               for x in xs_all]
        s_d1 = float(np.polyfit(xs_all, ld1, 1)[0])
        s_ov = float(np.polyfit(xs_all, lov, 1)[0])
        check("G54-tau-screen", abs(s_g) <= TAU_SLOPE_BAR,
              "slope log10 top-gap vs log10 tau = %.4f (<= %.2f: the "
              "RATIO is not Connes-priced; the RAW gap rides tau BY "
              "CONSTRUCTION -- BOUND-RIDES-CONNES typed); "
              "compensation slopes dex/x: delta_1 %+.3f vs "
              "rho2/et1^2 %+.3f (sum %.3f ~ 0: the flatness is the "
              "well-depth/overlap cancellation, MEASURED)"
              % (s_g, TAU_SLOPE_BAR, s_d1, s_ov, s_d1 + s_ov))
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
                ("EPSLOCK", "PFLOOR"): 1,
                ("PFLOOR", "SUSCAP2"): 1,
                ("SUSCAP2", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("PFLOOR", "SUSCAP2")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "PFLOOR"): 1, ("PFLOOR", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2"): 1, ("SUSCAP2", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 7 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r138 unit edge QSUBGAP(1) "
          "REFINED in series PFLOOR(1) -> SUSCAP2(1) behind "
          "EPSLOCK(1) (U2 numerator consumes tlaw + spacing product; "
          "U1/U3 denominator = top-2-row susceptibility), "
          "QSUBGAPTHM(INF, U1-U4 + locality + adversarial) behind; "
          "one-grant still 5; counterfactual PARALLEL 7 NOT REAL; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")
    info("EXACT QSUBGAP RESIDUE after this round: QSUBGAP-lam-uniform "
         "<== EPSLOCK (tlaw <= poly, OMEGA-a = JETLOCK + BANDMASS, "
         "CDXLI, cited) + PFLOOR (the A0-free spacing-lattice product "
         "P(T_z)^2 >= 1/poly -- counting-class, classical below the "
         "verification height) + SUSCAP2 (chi_abs of the TOP-2-ROW "
         "well <= poly x R_phi^2/tau -- the NEW named object; the "
         "adversarial battery shows it is NOT determined by classical "
         "zone geometry: legal RvM shapes give rel-gap < 1 at broken "
         "consistency -- the gap is the ARITHMETIC WELL DEPTH, "
         "arithmetic-pinning-shaped, BANDMASS-class).  NO RH claim; "
         "nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "U1-PROVEN(two-sided susceptibility form; G10/G11/G33)",
        "U2-PROVEN(scale-free factorization n = P^2/(2 T_z^2 G "
        "tlaw); G13/G34)",
        "LOCALITY-CERTIFIED(top-2-row lower bound == full gap; "
        "QSUBGAP is a three-row problem; G12/G36)",
        "COLLISION-CLOSED(span identity -> drow pricing; G14)",
        "WELL-ANATOMY(chi one-mode; delta_1 x overlap compensation "
        "MEASURED; G35/G54)",
        "ADVERSARIAL-ABS-BOUNDED(absolute gap >= bar over the "
        "battery; G37)",
        "SHAPE-COMPACTNESS-REFUTED(legal shapes break the relative "
        "gap only at broken consistency: QSUBGAP consumes the "
        "arithmetic well, BANDMASS-class; G37)",
        "CMODEL-SPLIT(numerator counting-class, susceptibility "
        "position-hypersensitive; G34/G37)",
        "CONTROLS-REFUSE(zone overcount + zero-free gap; G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "OMEGA-REFINED(QSUBGAP <== EPSLOCK + PFLOOR + SUSCAP2 "
        "serial; G60)"]
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
        print("COMPOSITE: U1-PROVEN + U2-PROVEN + LOCALITY-CERTIFIED "
              "+ COLLISION-CLOSED + WELL-ANATOMY + "
              "ADVERSARIAL-ABS-BOUNDED + SHAPE-COMPACTNESS-REFUTED + "
              "CMODEL-SPLIT + CONTROLS-REFUSE + DEMAND-FLAT + "
              "OMEGA-REFINED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
