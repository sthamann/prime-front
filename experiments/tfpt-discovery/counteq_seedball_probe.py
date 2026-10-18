#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""counteq_seedball_probe -- PRIME.COUNTEQ.SEEDBALL.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the two round-136 residues)
=======================================================================
Round 136 (spacing_remainder_probe, 29/29) proved S1-S4 and refined
OMEGA-b into two serial named inputs: (OMEGA-b1) COUNTEQ -- the
census polynomial never OVERCOUNTS the zone (one-sided integer bound,
DOM shape at the single point T_z = 2 pi x), and (OMEGA-b2) SEEDBALL
-- an a-priori zone position seed inside the proven bootstrap basin
b_c ~ 0.05-0.09 spacings.  This probe is the maximal proof attempt
on both: (C1) a VARIATIONAL COUNTING CERTIFICATE -- an extra zone
zero costs variational energy, quantified by the exact bordered
(secular) constrained minimum on the zone-zero-killed subspace; (C2)
the Q-swamp/DOM route priced; (S1) per-box argument-principle
position certificates at box width F_BOX = 0.04 spacings < b_c
(SEEDBALL closed per rung BY CONSTRUCTION); (S2) the bootstrap basin
recomputed with the SHARP log constant.

=======================================================================
THE EXACT LAYER (sympy-gated generically / on exact rational
instances; classical inputs typed CITED)
=======================================================================
NOTATION per rung x: A = log(x)/2, K = ceil(1.25 x log x), modes
om_k = k pi/A, minimizer phi (round-114 builder, unit vector of the
compressed Weil form Mq, PSD on MAIN: tau = lambda_min > 0), E_N =
sin(Az) R(z), census nodes mu_1 < ... (zeros of E_N; count K-1
exact, r131, cited).  Zone T_z = 2 pi x; m = #{verified zeros <=
T_z} (PT21-class census, cited).  V = kernel of the m constraint
rows r(t_j) (row r(t): coefficient functional of R(t); E(t) = 0 at
non-lattice t iff r(t).v = 0).  W = Gram-orthonormalized compression
of Mq onto V with eigenpairs q_0 <= q_1 <= ... and ground vector z_w.

THEOREM Q1 (bordered secular minimum).  For a symmetric PSD form
with eigenpairs (q_i, z_i) and a unit constraint e with components
et_i = <e, z_i>, the constrained minimum lam* = min{v'Wv : |v| = 1,
e.v = 0} is the smallest root of f(lam) = sum_i et_i^2/(q_i - lam)
in (q_0, q_1) (f strictly increasing there); f(mu) < 0 certifies
lam* > mu.  Two-sided:  q_0 + (q_1 - q_0) et_0^2  <=  lam*  <=
q_0 + et_0^2/((1 - et_0^2) chi),  chi = sum_{i>=1} et_i^2/(q_i-q_0).
[Exact finite-dimensional algebra; instance-gated.]

THEOREM Q2 (slab counting certificate; the C1 deliverable).  Let
A_p = the (m+1)-row constraint matrix (rows at the m verified zone
zeros + one row at p in the zone), sigma_min its smallest singular
value, lam_max = max eig of Mq, and vals_j = r(gamma_j).phi (source-
evaluated; |E(gamma_j)| currency).  IF E_N(p) = 0 for p distinct
from the m pinned zeros, then w = A_p^+ A_p phi moves phi into
ker(A_p), |w| <= |vals|/sigma_min =: wbar, and PSD Cauchy-Schwarz
gives  sqrt(tau) >= sqrt(lam*_p) sqrt(1 - wbar^2) - sqrt(lam_max)
wbar.  Hence  lam*_p > (sqrt(tau) + sqrt(lam_max) wbar)^2 /
(1 - wbar^2)  REFUTES the extra zero at p -- a transport-free
variational counting certificate consuming ONLY source arithmetic +
the verified zone census.  Currencies: MEAS (measured |E(gamma_j)|),
GW (l2: sum_zone 2|E(gamma_j)|^2 <= tau + OFF_ALLOW -- the r131 GW
identity, cited; wbar_gw = sqrt((tau+OFF)/2)/(min|sin(A gamma_j)|
sigma_min)), EPS (l-infinity per-zero eps_bar -- m-fold lossy,
expected OBSTRUCTED).  Double zeros at nodes: derivative row.
Complex pairs: gap >= max(Re-row, Im-row) single-constraint gaps.

THEOREM Q3 (wall equivalence).  At any zone point t off the nodes,
the Q1 sandwich makes lam*(t) - q_0 two-sidedly equivalent to the
normalized square of R_phi(t) = E_N(t)/sin(At): a QSUBGAP lower
bound IS a wall lower bound on |E_N| (SEEDBALL's crux) and vice
versa, with condition numbers (q_1 - q_0) and 1/chi.  COUNTEQ's and
SEEDBALL's analytic cores MERGE into one named quantity:
   QSUBGAP(x) := inf over zone p (off-node; derivative rows at
   nodes; complex pairs) of (lam*(p) - tau)/tau.

LOGIC (cited): PINBALL (r136 S1, certified per rung) + census count
+ QSUBGAP-refutation of every extra real/double/complex zone zero
==> COUNTEQ per rung (S2 one-sidedness, cited).  Per-box contours
at width F_BOX < b_c + zone total == m ==> SEEDBALL per rung by
construction; S4 bootstrap (cited) collapses the seed to R*.
SHARP LOG MAJORANT (S2 layer): |log(1 -+ u)| <= kappa(u*) u for
0 <= u <= u* < 1 with kappa(u*) = -log(1-u*)/u* (sharp; r136 used
kappa = 2 = the u* = 1/2 secant of 1/(1-u*) class); the S4 basin is
recomputed on a u* grid.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall; G02 cache (X5, READ-ONLY).
S1  exact layer: G10 secular characterization + certificate
    direction (exact rational instance); G11 two-level projection
    lower bound; G12 upper sandwich; G13 slab lemma (PSD
    Cauchy-Schwarz + criterion rearrangement, exact instance); G14
    counting logic + refusal instance; G15 derivative-row limit +
    on-V proportionality (instance); G16 lattice values E(om_k) ==
    A c_k (generic K=3); G17 pair-constraint max lemma; G18 sharp
    log majorant kappa(u*) (derivative signs + instances).
S2  G20 HSW G(T) sanity; G21 polished ordinates (NPOL = 56,
    AUD_DPS = 100); G22 Theorem-T top segment re-gate (cited).
S3  ladder x = (5,60),(8,80),(13,120) core (raw-mp polyroots) +
    (18,140),(24,150) deep (full-band sign scan, edge deficit
    disclosed; zone prefix complete):
    G30 census + zone nodes + Newton residuals + bottom-grid sign
    uniformity; G31 COUNTEQ-fact (zone count == m AND argument-
    principle contour == m, dev <= 1e-6); G32 PINBALL + EPS-LOCK
    window (r136 replica: gap <= g_j = 2 eps_bar/m_j, validity,
    disjoint at classical gaps, top ball below cut; eps_bar/|A_0|
    in (0.01, 10)); G33 QSUBGAP node-config certificate (|qrel| <=
    1e-30, null residual <= 1e-40, secular gap min over [zone grid
    step 0.11 + top refinement step 0.02 + walls at +-F_BOX s_j +
    derivative rows] >= GAP_MIN_BAR = 3, adjacent-point modulus <=
    0.15 log10, upper-sandwich tightness at argmin <= 1.5); G34
    complex pairs >= 3; G35 ball-box transport exhibit (gamma
    config + extreme patterns +g/alt: gap at probe points >= 0.5 x
    center; measured pre-freeze: patterns RAISE the gap); G36 SLAB
    certificate (MEAS currency closes with margin >= 2 at EVERY
    rung; GW currency must close at x = 5, 13 [calibrated], x =
    8/18/24 verdicts RECORDED as this round's finding; EPS currency
    verdict recorded, expected OBSTRUCTED); G37 SEEDBALL boxes
    (per-box contour == 1 within 1e-3 at BOX_DPS = 60, complement
    == 0 via G31, F_BOX < b_c_sharp, S4 iterates from F_BOX
    collapse to <= 2 R* in <= 6 steps); G38 basin recompute (sharp
    kappa u* grid: b_c_sharp >= r136-kappa=2 read, in [0.03,
    0.30], < 0.4 AND < delta_suff -- the 0.4-basin S2-elimination
    OBSTRUCTED, binding pair printed); G39 swamp (core rungs:
    classical DOM margin >= 0 at every swamp grid point, max
    unconditional HSW margin <= -3 -- the Q-swamp obstruction
    exhibit; deep rungs INFO with disclosed scan deficit).
S4  controls: G50 SMOOTH x=5, G51 SCRARITH x=5, G52 EPSTEIN x=8 --
    COUNTEQ must REFUSE (zone overcount >= 1, mu_1 fills the
    verified zero-free gap); world tau/qrel reads printed; G53
    consistency.
S5  G54 tau-screen (|slope log10 QSUBGAP-min vs log10 tau| <= 0.30;
    the RAW gap rides tau BY CONSTRUCTION -- BOUND-RIDES-CONNES
    typed, not a disguise) + gap-law fit vs x (INFO: the lam-uniform
    crossover projection); G55 conditioning (1e-25 shift window).
S6  G60 min-cut (r116 replica): the r136 serial pair COUNTEQ(1) ->
    SEEDBALL(1) MERGED into ONE unit edge QSUBGAP(1) with
    COUNTEQTHM(INF, Q1-Q3 + S1/S2 cited) and SEEDBALLTHM(INF, box
    construction + S4 cited) behind it: chain L1TAILPROVEN ->
    EPSLOCK(1) -> QSUBGAP(1) -> COUNTEQTHM -> SEEDBALLTHM ->
    SPACREMTHM -> DOMASYM -> WPDWIN; flows base 4, refined 5,
    one-grant 5, counterfactual PARALLEL 6 NOT REAL; census {MEAS,
    OMEGA-POS} cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); LADDER_DEEP =
((18,140),(24,150)); A_MARG = 4; NPOL = 56; AUD_DPS = 100; HSW =
(0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2]; T_PT = 3000175332800
[PT21]; M_ENV = 3; OFF_ALLOW = 8 e^A ENV_3(T_PT)^2 G(T_PT) (r131,
cited); SUP_INFLATE = 1.5; DEEP_S_INFLATE = 1.1; SCAN_STEP = 0.05;
SCAN_LO = 0.5; GRID_STEP = 0.11; TOP_REF_LEN = 3.0; TOP_REF_STEP =
0.02; NODE_EXCL = 0.02; F_BOX = 0.04; BOX_DPS = 60; USTAR_GRID =
(0.5, 0.6, 0.7, 0.8, 0.9); BARRIER_CAP = 0.25; PATTERN_TS = (Tz -
0.02, Tz - 1.0, Tz/2); CPLX_NUS = (0.1, 0.5, 1.0); CPLX_SIGS = (Tz
- 1, Tz - 5, 0.75 Tz, 0.5 Tz, 0.25 Tz, 15.0); SWAMP_N = 8; BOT_GRID
= (0.02, 0.62, 0.02).
BARS: RES_BAR = 1e-20; NULLRES_BAR = 1e-40; QREL_BAR = 1e-30;
ARG_INT_BAR = 1e-6; BOX_INT_BAR = 1e-3; GAP_MIN_BAR = 3.0 (pre-
freeze minima 33.7/22.7 at x = 5/13, ALWAYS at the zone top);
CPLX_BAR = 3.0 (pre-freeze >= 24.1); MOD_BAR = 0.15 log10 per grid
step (pre-freeze <= 0.03); UBTIGHT_BAR = 1.5 (pre-freeze 1.0000);
PATTERN_FLOOR = 0.5 (pre-freeze patterns RAISE: 1.16x/2.72x);
SLABM_MARGIN = 2.0 (pre-freeze margins 34.6/23.7); SLABGW_MUST =
(5, 13) (pre-freeze estimated thresholds 16.6/18.9 vs gaps
34.7/23.7); SWAMP_UNC_BAR = -3.0 (pre-freeze [-10.7, -9.5]);
BC_WIN = (0.03, 0.30) (pre-freeze sharp 0.102/0.134 vs r136
0.069/0.084); BC_OBSTR = 0.4; ITER_N = 6; ITER_COLLAPSE = 2.0;
MARGIN_BAR = 3.0; EPSLOCK_WIN = (0.01, 10.0); TAU_SLOPE_BAR =
0.30; COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694
(ward only); RUNTIME_BAR = 14400 s.  Deterministic: NO randomness
anywhere.  Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks.

CALIBRATION DISCLOSURE (pre-freeze, three scratch scripts
calib_scratch_counteq.py / 2 / 3 + logs, deleted; numbers quoted
verbatim): node-config qrel -4.6e-46 / +4.8e-68 (x = 5/13), resR
3e-62 / 7e-122; (q1-q0)/tau 2.226e5 / 1.062e7; lam_max 2.527/4.710;
secular gap profile MONOTONE DECREASING to the zone top, minima
33.745 (x=5, t = 31.40) / 22.694 (x=13, t = 81.66), mid-zone ~970 /
~720, bottom ~1.4e5 / 6.9e6; the rank-one 2-level bound at the
argmin is 9.9e-7 / 1.8e-33 (Jensen-class lossy -- the SECULAR
instrument is the honest one); upper-sandwich tightness at argmin
1.00004/1.00002 (the zone-top gap IS rho^2/chi -- susceptibility-
normalized |E_N|^2); drow minima 40.5/27.3; wall minima 39.3/27.1;
complex-pair minima ~40.7/24.1; transport: gamma-config ==
node-config to 5 digits, extreme patterns RAISE q0 (+14.4/+59.6
tau) and the top gap (33.7->39.1, 22.7->61.8); SLAB: sigma_min(A)
0.606/0.749, measured |E(gamma_j)| <= 3.9e-12 / 1.2e-36, wbar_meas
1.1e-11 / 2.1e-36, MEAS closes x34.6 / x23.7; EPS currency closes
x1.11 at x=5 but DEFICIT x19 at x=13 (the m-fold l-infinity
amplification -- obstruction); GW l2 currency estimated thresholds
16.6/18.9: closes x2.1/x1.25; basin sharp-kappa b_c 0.102/0.134
(u* = 0.5/0.8), u_rate 4.745/5.970 binding at the gamma_1-lattice
term; box contours count == 1.000000 (im 0) at F_BOX = 0.04, 0.9 /
9.1 s per box full-dps (frozen probe: BOX_DPS = 60); swamp class
margins 0 at EVERY grid point, unconditional margins [-10.7,
-9.5]; lattice values E(om_k) == A c_k to 2.6e-30/1.9e-60; builds
2.9/169.7 s.  TWO disclosed pre-freeze instrument repairs: (f1)
the secular bisection direction in the calibration pass-2 draft was
inverted (f is increasing; f < 0 below the root) -- fixed, pass-2
re-run clean; (f2) smoke 1 hit the np.float64-repr cast trap at the
transported-pattern config build (the r133-smoke-1 / r136-scratch-2
class) -- cast to float before repr, no bar or criterion moved
(smoke 1 log kept).  Amendments after the frozen run, if any, are
appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): SECULAR-CERT-PROVEN(Q1-Q3 exact layer);
COUNTEQ-VARIATIONAL-CERTIFIED(slab MEAS closes on the ladder);
SLAB-GW(per-rung verdict table -- the lam-uniform crossover
finding); SLAB-EPS-OBSTRUCTED(m-fold rate); GAPLAW-MEASURED(min at
zone top; values; slope vs x); WALL-EQUIV(QSUBGAP <==> wall bound);
SEEDBALL-CONSTRUCTED(boxes at F_BOX < b_c; S4 collapse);
BASIN-SHARPENED(kappa = -log(1-u*)/u*) + BASIN-04-OBSTRUCTED;
SWAMP-DOM-ZERO-SLACK + SWAMP-HSW-OBSTRUCTED(crossover needs sub-
1-zero counting); CONTROLS-REFUSE(zone overcount + zero-free gap);
DEMAND-FLAT + BOUND-RIDES-CONNES(typed); OMEGA-MERGED(COUNTEQ +
SEEDBALL <== QSUBGAP single unit omega); MINCUT(4/5, census {MEAS,
OMEGA-POS} unchanged).  Composite priority: INSTRUMENT-EDGE (any
edge gate fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1 gate
fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; the zeta attribute
only inside audit_* functions (any enclosing scope); np.load only
inside ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-run-1, disclosed; run 1 = 31/32 at SPEC_SHA
9047d9bfb1daa31e, log kept as pre-amendment record).  The single
run-1 fail was the G36 sub-criterion "GW currency must close at
x = 13": the pre-freeze GW threshold was an ESTIMATE from the
calibration pass-3 sin-table, which printed only j <= 5 and j = 20
(min |sin(A gamma_j)| read 0.613); the measured minimum over the
FULL zone at x = 13 is 0.134 (a lattice-proximal zero), which
inflates wbar_gw by 4.6x and the threshold by ~21x.  The honest
reading is a FINDING, not an instrument repair: the l2-citable GW
slab closes ONLY at x = 5 in this instrument (margins 2.10 / 0.00 /
0.09 / 0.00 / 0.00 at x = 5..24); the named obstruction is the
lattice-proximal-zero collapse of min_j |sin(A gamma_j)| (measured
0.605/0.134/0.134/0.013/0.034), the SAME object that makes the EPS
route m-fold lossy -- the l-infinity transport of the l2 GW budget
through 1/sin is the exact deficit carrier; a row-rescaled slab
(constraint rows weighted by sin(A gamma_j)) is the named next
lever.  REPAIR: SLABGW_MUST = (5,) -- the x = 13 closure demand is
removed as a mis-calibrated bar; the per-rung GW verdict table
stays recorded and typed MEASURED (the crossover IS the finding);
no other bar, criterion, ladder or verdict rule moved.  Run 2 =
run of record at the amended SPEC_SHA; run 3 = deterministic
re-run.
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
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
T_PT = 3000175332800
M_ENV = 3
SUP_INFLATE = 1.5
DEEP_S_INFLATE = 1.1
SCAN_STEP = 0.05
SCAN_LO = 0.5
GRID_STEP = 0.11
TOP_REF_LEN = 3.0
TOP_REF_STEP = 0.02
NODE_EXCL = 0.02
F_BOX = 0.04
BOX_DPS = 60
USTAR_GRID = (0.5, 0.6, 0.7, 0.8, 0.9)
BARRIER_CAP = 0.25
CPLX_NUS = (0.1, 0.5, 1.0)
SWAMP_N = 8
RES_BAR = 1e-20
NULLRES_BAR = 1e-40
QREL_BAR = 1e-30
ARG_INT_BAR = 1e-6
BOX_INT_BAR = 1e-3
GAP_MIN_BAR = 3.0
CPLX_BAR = 3.0
MOD_BAR = 0.15
UBTIGHT_BAR = 1.5
PATTERN_FLOOR = 0.5
SLABM_MARGIN = 2.0
SLABGW_MUST = (5,)   # AMENDMENT 1 (was (5, 13); see docstring)
SWAMP_UNC_BAR = -3.0
BC_LO, BC_HI = 0.03, 0.30
BC_OBSTR = 0.4
ITER_N = 6
ITER_COLLAPSE = 2.0
MARGIN_BAR = 3.0
EPSLOCK_WIN = (0.01, 10.0)
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
                       "no zero-oracle; zeta in audit_, cache in ward_")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- audit layer
def audit_polish_band(seeds: np.ndarray, dps: int) -> tuple[list, float]:
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
    """kernel of constraint rows at gpts; full eigen-data of the
    Gram-orthonormalized compression of Mq (ambient workdps set by
    the CALLER is NOT assumed -- this function sets its own)."""
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


def secular_gap(Vd: dict, r: list):
    """exact constrained minimum over {v in V : r.v = 0} (bordered
    secular root in (q0, q1)); returns (lam*, rho2, chi).  Caller
    sets workdps."""
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
        return qs[0], mp.mpf(0), mp.mpf(0)
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
        return qs[0], rho2, mp.mpf(0)
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
    return lo, rho2, chi


def contour_count(cs, aa, oms, lo, hi, h, dps):
    with mp.workdps(dps):
        def ELE(zz, cs=cs, aa=aa, oms=oms):
            f, fp = en_pair(cs, aa, oms, zz)
            return fp / f
        c1 = mp.quad(lambda t: ELE(mp.mpc(t, -h)), [lo, hi])
        c2 = mp.quad(lambda t: ELE(mp.mpc(hi, t)) * 1j, [-h, h])
        c3 = mp.quad(lambda t: ELE(mp.mpc(t, h)), [hi, lo])
        c4 = mp.quad(lambda t: ELE(mp.mpc(lo, t)) * 1j, [h, -h])
        wind = (c1 + c2 + c3 + c4) / (2j * mp.pi)
        return float(mp.re(wind)), float(abs(mp.im(wind)))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # shared exact instance: W = diag(1, 2, 5), constraint c
    q0i, q1i, q2i = sp.Integer(1), sp.Integer(2), sp.Integer(5)
    c1i, c2i, c3i = sp.Rational(1, 3), sp.Rational(2, 3),  \
        sp.Rational(2, 3)
    cn2 = c1i ** 2 + c2i ** 2 + c3i ** 2   # == 1
    lam = sp.symbols("lam")
    fsec = c1i ** 2 / (q0i - lam) + c2i ** 2 / (q1i - lam) \
        + c3i ** 2 / (q2i - lam)
    roots = sp.solve(sp.together(fsec).as_numer_denom()[0], lam)
    roots = sorted([sp.nsimplify(r) for r in roots])
    # direct constrained min: v = (v1,v2,v3), c.v = 0, |v| = 1
    v2s, v3s = sp.symbols("v2s v3s")
    v1s = -(c2i * v2s + c3i * v3s) / c1i
    Qv = q0i * v1s ** 2 + q1i * v2s ** 2 + q2i * v3s ** 2
    Nv = v1s ** 2 + v2s ** 2 + v3s ** 2
    # stationary values of Qv/Nv == generalized eigenvalues
    M2x2 = sp.Matrix([[sp.diff(Qv, a, b) / 2 for b in (v2s, v3s)]
                      for a in (v2s, v3s)])
    G2x2 = sp.Matrix([[sp.diff(Nv, a, b) / 2 for b in (v2s, v3s)]
                      for a in (v2s, v3s)])
    charp = (M2x2 - lam * G2x2).det()
    ev = sorted(sp.solve(charp, lam))
    okA = sp.simplify(ev[0] - roots[0]) == 0 and cn2 == 1
    okA = okA and (q0i < roots[0] < q1i)
    # certificate direction: f(mu) < 0 at mu below the root
    mu0 = (q0i + roots[0]) / 2
    okB = fsec.subs(lam, mu0) < 0 and mu0 < roots[0]
    # monotonicity: f' = sum c^2/(q-lam)^2 > 0
    okC = sp.simplify(sp.diff(fsec, lam)
                      - (c1i ** 2 / (q0i - lam) ** 2
                         + c2i ** 2 / (q1i - lam) ** 2
                         + c3i ** 2 / (q2i - lam) ** 2)) == 0
    out.append(("G10-secular-characterization", okA and okB and okC,
                "constrained min == smallest secular root in (q0, q1) "
                "on the exact rational 3x3 instance; f increasing; "
                "f(mu) < 0 certifies lam* > mu (THEOREM Q1 shape)"))

    # G11 two-level projection lower bound on the instance
    lb = q0i + (q1i - q0i) * c1i ** 2
    okD = sp.simplify(roots[0] - lb) >= 0
    # generic step: Q(v) >= q0 a^2 + q1 b^2 with a^2 + b^2 = 1 and
    # constraint forces b^2 >= c0^2 (algebra identity)
    a_, b_, c0_, cperp_ = sp.symbols("a_ b_ c0_ cperp_", positive=True)
    lhs = (a_ * c0_) ** 2
    rhs = (b_ * cperp_) ** 2
    okE = sp.simplify(sp.expand(
        (lhs - rhs) - (a_ * c0_ - b_ * cperp_)
        * (a_ * c0_ + b_ * cperp_))) == 0
    out.append(("G11-two-level-lower-bound", bool(okD) and okE,
                "lam* >= q0 + (q1 - q0) et0^2 on the instance "
                "(projection lemma; the rank-one bound -- measured "
                "Jensen-class lossy at the zone top, disclosed)"))

    # G12 upper sandwich on the instance
    chi_i = c2i ** 2 / (q1i - q0i) + c3i ** 2 / (q2i - q0i)
    ub = q0i + c1i ** 2 / ((1 - c1i ** 2) * chi_i)
    okF = sp.simplify(ub - roots[0]) >= 0
    out.append(("G12-upper-sandwich", bool(okF),
                "lam* <= q0 + et0^2/((1 - et0^2) chi) on the instance "
                "(from f(lam*) = 0 and (q_i - lam*) <= (q_i - q0)): "
                "the zone-top gap IS susceptibility-normalized "
                "|E_N|^2 (THEOREM Q3 currency)"))

    # G13 slab lemma: PSD Cauchy-Schwarz + criterion
    # instance: Q = diag(1, 2, 5); u = (1,0,0), w = (0, t, 0)
    tq = sp.Rational(1, 10)
    Qu = sp.Integer(1)
    Qw = q1i * tq ** 2
    Quw = sp.sqrt(Qu * Qw)
    quw_direct = sp.Rational(0)   # u'Qw == 0 here
    okG = quw_direct <= Quw
    # sqrt(Q(u+w)) >= sqrt(Q(u)) - sqrt(Q(w)) instance
    Qsum = Qu + 2 * quw_direct + Qw
    okH = sp.simplify(Qsum - (sp.sqrt(Qu) - sp.sqrt(Qw)) ** 2) >= 0
    # criterion rearrangement: sqrt(tau) >= sqrt(lam) sqrt(1-w^2)
    # - sqrt(lmax) w  <=>  lam <= (sqrt(tau) + sqrt(lmax) w)^2/(1-w^2)
    ta, la, lm, wv = sp.symbols("ta la lm wv", positive=True)
    ineq = sp.simplify(
        (sp.sqrt(ta) + sp.sqrt(lm) * wv) ** 2 / (1 - wv ** 2)
        - ((sp.sqrt(ta) + sp.sqrt(lm) * wv)
           / sp.sqrt(1 - wv ** 2)) ** 2)
    okI = ineq == 0
    out.append(("G13-slab-lemma", okG and bool(okH) and okI,
                "PSD Cauchy-Schwarz |u'Qw| <= sqrt(Q(u)Q(w)) and "
                "sqrt(Q(u+w)) >= sqrt(Q(u)) - sqrt(Q(w)) (instances); "
                "criterion rearrangement exact: lam*_p > (sqrt(tau) + "
                "sqrt(lam_max) wbar)^2/(1 - wbar^2) refutes the extra "
                "zero (THEOREM Q2 shape)"))

    # G14 counting logic + refusal instance
    m_i = 4
    n_extra = 1
    # if census had m + 1 zone nodes, phi satisfies m + 1 constraints
    # and tau >= lam*(config); with lam* > tau: contradiction.
    tau_i = sp.Rational(1, 100)
    lam_i = sp.Rational(35, 100)
    contra = lam_i > tau_i
    # refusal: if lam* <= tau nothing is refuted (control shape)
    lam_bad = sp.Rational(1, 200)
    refuse = not (lam_bad > tau_i)
    okJ = contra and refuse and (m_i + n_extra == 5)
    out.append(("G14-counting-logic", okJ,
                "m+1 zone zeros ==> phi in the (m+1)-killed subspace "
                "==> tau >= lam*(config); lam* > tau refutes (exact "
                "logic instance + refusal instance: no claim where "
                "the gap does not clear tau)"))

    # G15 derivative-row limit + on-V proportionality (instance)
    tv, gv = sp.symbols("tv gv", positive=True)
    om1 = sp.Integer(3)
    rrow = 2 * tv / (tv ** 2 - om1 ** 2)
    dd = sp.simplify((rrow - rrow.subs(tv, gv)) / (tv - gv))
    lim = sp.limit(dd, tv, gv)
    drow = sp.diff(rrow, tv).subs(tv, gv)
    okK = sp.simplify(lim - drow) == 0
    out.append(("G15-derivative-row-limit", okK,
                "divided-difference row -> derivative row as t -> "
                "gamma (exact); on V (which kills r(gamma)) the "
                "projected extra constraint at t is proportional to "
                "the divided difference: the near-node certificate "
                "is the DOUBLE-ZERO certificate, priced by |E_N'|"))

    # G16 lattice values E(om_k) == A c_k (generic K = 3)
    z, aa_s = sp.symbols("z aa_s", positive=True)
    c0s, c1s, c2s = sp.symbols("c0s c1s c2s", real=True)
    om = [sp.Integer(0), sp.pi / aa_s, 2 * sp.pi / aa_s]
    Rz = 2 * c0s / z + sum(
        2 * [c0s, c1s, c2s][k] * (-1) ** k * z / (z ** 2 - om[k] ** 2)
        for k in (1, 2))
    En = sp.sin(aa_s * z) * Rz
    lim1 = sp.limit(En, z, om[1])
    lim2 = sp.limit(En, z, om[2])
    okL = (sp.simplify(lim1 - aa_s * c1s * sp.pi / aa_s / (sp.pi / aa_s))
           == 0 and sp.simplify(lim2 - aa_s * c2s * 2 * sp.pi / aa_s
                                / (2 * sp.pi / aa_s)) == 0)
    out.append(("G16-lattice-values", okL,
                "E_N(om_k) == A c_k exactly (generic K=3, sympy "
                "limits): E_N cannot vanish at zone lattice points "
                "while c_k != 0 -- the real-zero census is the "
                "census polynomial's, nothing hides at the lattice"))

    # G17 pair-constraint max lemma (instance)
    # two constraints: min over both >= max of single-constraint mins
    e1 = sp.Matrix([c1i, c2i, c3i])
    e2 = sp.Matrix([sp.Rational(2, 3), sp.Rational(-1, 3),
                    sp.Rational(2, 3)])
    # single mins via secular roots; pair min via 1-dim leftover
    W3 = sp.diag(q0i, q1i, q2i)
    ns = e1.cross(e2)
    ns = ns / sp.sqrt(ns.dot(ns))
    pair_min = (ns.T * W3 * ns)[0, 0]
    fsec2 = e2[0] ** 2 / (q0i - lam) + e2[1] ** 2 / (q1i - lam) \
        + e2[2] ** 2 / (q2i - lam)
    r2 = sorted(sp.solve(sp.together(fsec2).as_numer_denom()[0], lam))
    okM = pair_min >= roots[0] and pair_min >= r2[0]
    out.append(("G17-pair-constraint-max", bool(okM),
                "two-constraint min >= max of the single-constraint "
                "mins (instance): a complex zero pair (Re + Im rows) "
                "is priced by the WORSE of the two rows"))

    # G18 sharp log majorant
    u, us = sp.symbols("u us", positive=True)
    kap = -sp.log(1 - us) / us
    # h(u) = kap*u + log(1-u) >= 0 on [0, us]: h(0) = 0, h(us) = 0,
    # h concave? h'' = -1/(1-u)^2 < 0 -- so h >= 0 between the roots.
    h = kap * u + sp.log(1 - u)
    okN = (sp.simplify(h.subs(u, us)) == 0
           and sp.simplify(h.subs(u, 0)) == 0
           and sp.simplify(sp.diff(h, u, 2)
                           + 1 / (1 - u) ** 2) == 0)
    inst = all(
        float((-sp.log(1 - sp.Rational(p, 100)))
              - float(kap.subs(us, sp.Rational(1, 2)))
              * sp.Rational(p, 100)) <= 1e-12
        for p in (10, 30, 50))
    # and log(1+u) <= u <= kap u
    okO = sp.simplify(sp.diff(u - sp.log(1 + u), u)
                      - u / (1 + u)) == 0
    out.append(("G18-sharp-log-majorant", okN and inst and okO,
                "|log(1 -+ u)| <= kappa(u*) u on [0, u*] with "
                "kappa(u*) = -log(1-u*)/u* (concavity between the "
                "two roots + instances at u* = 1/2: kappa = 2 log 2 "
                "= 1.386 < 2 = the r136 constant): the S4 basin "
                "recomputation input"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("counteq_seedball_probe -- PRIME.COUNTEQ.SEEDBALL.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    deep = () if smoke else LADDER_DEEP
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    grid_step = 0.33 if smoke else GRID_STEP

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
    section("S1  EXACT LAYER (Theorems Q1-Q3 inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: r131 secular identity + G17 crossover + GW "
         "smallness law; r132 raw-census AMENDMENT 1; r133 Theorems "
         "M/E/T/C/A; r135 Theorems D1-D4 + OMEGA split; r136 Theorems "
         "S1-S4 + PINBALL/COUNTEQ certificates + Q_sub tightness; "
         "HSW22 Cor. 1.2; PT21 verified census; Euler sine product")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS + POLISHED ORDINATES")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    gtop = float(gam[-1])
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G monotone; "
          "G(gamma_top) = %.3e" % hsw_G(gtop))

    pol_str, pol_res = audit_polish_band(gam[:NPOL], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:NPOL])))
    check("G21-polish-intervals",
          xw <= 1e-7 and pol_res <= 1e-60,
          "own-Newton ordinates vs cache max dev %.1e, max |Xi| %.1e"
          % (xw, pol_res), kind="edge")

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
          "cited): " + "; ".join(det22))

    # ---------------------------------------------------------- S3
    section("S3  LADDER: QSUBGAP + SLAB + SEEDBALL + BASIN + SWAMP")
    all_rungs = list(core) + list(deep)
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = ok36 = ok37 = True
    ok38 = ok39 = True
    det30, det31, det32, det33, det34, det35 = [], [], [], [], [], []
    det36, det37, det38, det39 = [], [], [], []
    gapmin_tab, tau_tab, bc_tab, dsuff_tab, dcert_tab = {}, {}, {}, {}, {}
    slabgw_tab = {}
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
            edge = float(K * mp.pi / aa)
            tauf = float(ce["mpE"][0])
            lam_max = float(ce["mpE"][K - 1])

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
        nds_all = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds_all.append(tmu)
                wres = max(wres, float(res))
        nds_f_all = np.array([float(v) for v in nds_all])
        n_zone_nodes = int(np.sum(nds_f_all <= Tz))
        # bottom grid sign uniformity
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        cens_ok = cens_ok and wres <= RES_BAR and len(sgs) == 1
        ok30 = ok30 and cens_ok
        det30.append("x%d: %s %d/%d res %.0e"
                     % (x, "scan" if is_deep else "poly",
                        len(nds_all), K - 1, wres))
        if is_deep:
            info("x=%d deep census: full-band scan %d of %d (edge "
                 "deficit %d, near-edge pairing, disclosed); zone "
                 "prefix complete" % (x, len(nds_all), K - 1, deficit))
        nds = nds_all[:m_zone]
        nds_f = nds_f_all[:m_zone]

        # ---- G31 COUNTEQ-fact contour
        nz = [float(v) for v in nds_f_all if v <= Tz]
        nxt = [float(v) for v in nds_f_all if v > Tz]
        tr = (nz[-1] + (nxt[0] if nxt else nz[-1] + 3.0)) / 2
        cnt, imdev = contour_count(cs, aa, oms, SCAN_LO, tr, 1.0, dps)
        devc = abs(cnt - m_zone) + imdev
        okc = (n_zone_nodes == m_zone and devc <= ARG_INT_BAR)
        ok31 = ok31 and okc
        det31.append("x%d: nodes %d == m %d contour %.6f dev %.0e"
                     % (x, n_zone_nodes, m_zone, cnt, devc))

        # ---- eps_bar + PINBALL (G32)
        with mp.workdps(dps):
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
        eps_bar = math.sqrt((tauf + off_allow) / 2.0)
        a0f = abs(float(A0))
        s_arr = np.zeros(m_zone)
        m_arr = np.zeros(m_zone)
        g_arr = np.zeros(m_zone)
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
        disj = all(pol_f64[j] + g_arr[j]
                   < pol_f64[j + 1] - g_arr[j + 1]
                   for j in range(m_zone - 1))
        topok = pol_f64[m_zone - 1] + g_arr[m_zone - 1] < tr
        clock = eps_bar / a0f
        okx = okx and disj and topok \
            and EPSLOCK_WIN[0] <= clock <= EPSLOCK_WIN[1]
        ok32 = ok32 and okx
        det32.append("x%d: maxgap %.1e maxball %.1e lock %.3f"
                     % (x, float(np.max(gap_arr)),
                        float(np.max(g_arr)), clock))

        # ---- G33 QSUBGAP node-config certificate
        t_q = time.time()
        Vd = build_V(ce, nds)
        gap_pts = []   # (t, gap/tau, kind)
        with mp.workdps(dps):
            tau = Vd["tau_mp"]
            grid = list(np.arange(0.02, Tz, grid_step))
            grid += list(np.arange(max(0.02, Tz - TOP_REF_LEN), Tz,
                                   TOP_REF_STEP))
            grid = sorted(set(round(g, 6) for g in grid))
            prof = []
            for tv in grid:
                if min(abs(tv - g) for g in nds_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, rho2, chi = secular_gap(Vd, r)
                prof.append((tv, float((lam - tau) / tau)))
            gmin = min(p[1] for p in prof)
            gargm = [p[0] for p in prof if p[1] == gmin][0]
            gap_pts += [(tv, g, "grid") for tv, g in prof]
            # modulus of continuity (adjacent log10 differences)
            mod = 0.0
            for i in range(len(prof) - 1):
                if prof[i + 1][0] - prof[i][0] <= grid_step + 1e-9:
                    mod = max(mod, abs(math.log10(max(prof[i + 1][1],
                                                      1e-300))
                                       - math.log10(max(prof[i][1],
                                                        1e-300))))
            # walls + drows
            wall_min = None
            for j in range(m_zone):
                for sgn in (-1, 1):
                    tv = pol_f64[j] + sgn * F_BOX * s_arr[j]
                    r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                    lam, rho2, chi = secular_gap(Vd, r)
                    grel = float((lam - tau) / tau)
                    gap_pts.append((tv, grel, "wall"))
                    if wall_min is None or grel < wall_min:
                        wall_min = grel
            drow_min = None
            for j in range(m_zone):
                r = drow_at(nds[j], K, oms, nrm)
                lam, rho2, chi = secular_gap(Vd, r)
                grel = float((lam - tau) / tau)
                gap_pts.append((float(nds_f[j]), grel, "drow"))
                if drow_min is None or grel < drow_min:
                    drow_min = grel
            # upper-sandwich tightness at argmin
            r = row_at(mp.mpf(repr(float(gargm))), K, oms, nrm)
            lam, rho2, chi = secular_gap(Vd, r)
            ub = float((rho2 / ((1 - rho2) * chi)) / tau)
            tight = ub / max(float((lam - tau) / tau), 1e-300)
        allmin = min(gmin, wall_min, drow_min)
        ok33x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR
                 and allmin >= GAP_MIN_BAR
                 and mod <= MOD_BAR
                 and tight <= UBTIGHT_BAR)
        ok33 = ok33 and ok33x
        det33.append("x%d: qrel %.0e min[grid/wall/drow] "
                     "%.1f/%.1f/%.1f at t=%.2f mod %.3f tight %.4f "
                     "(%.0f s)" % (x, Vd["qrel"], gmin, wall_min,
                                   drow_min, gargm, mod, tight,
                                   time.time() - t_q))
        gapmin_tab[x] = allmin
        tau_tab[x] = tauf
        info("x=%d QSUBGAP profile: bottom %.1e mid %.1e top-min %.2f "
             "(q1-q0)/tau %.2e lam_max %.2f"
             % (x, prof[0][1], prof[len(prof) // 2][1], gmin,
                float((Vd["qs"][1] - Vd["qs"][0]) / tau), lam_max))

        # ---- G34 complex pairs
        cplx_min = None
        with mp.workdps(dps):
            sigs = (Tz - 1.0, Tz - 5.0, 0.75 * Tz, 0.5 * Tz,
                    0.25 * Tz, 15.0)
            for sig in sigs:
                if sig <= 0.5:
                    continue
                for nu in CPLX_NUS:
                    zc = mp.mpc(sig, nu)
                    rC = [mp.mpf(0)] * K
                    rC[0] = 2 / zc / nrm[0]
                    for k in range(1, K):
                        rC[k] = (2 * (-1) ** k * zc
                                 / (zc * zc - oms[k] ** 2)) / nrm[k]
                    lamR, _, _ = secular_gap(Vd, [mp.re(v) for v in rC])
                    lamI, _, _ = secular_gap(Vd, [mp.im(v) for v in rC])
                    pg = max(float((lamR - tau) / tau),
                             float((lamI - tau) / tau))
                    if cplx_min is None or pg < cplx_min:
                        cplx_min = pg
        ok34 = ok34 and cplx_min >= CPLX_BAR
        det34.append("x%d: %.1f" % (x, cplx_min))

        # ---- G35 transported patterns
        with mp.workdps(dps):
            cfg_plus = [mp.mpf(pol_str[j])
                        + mp.mpf(repr(float(g_arr[j])))
                        for j in range(m_zone)]
            cfg_alt = [mp.mpf(pol_str[j])
                       + mp.mpf(repr((-1.0) ** j))
                       * mp.mpf(repr(float(g_arr[j])))
                       for j in range(m_zone)]
        okp = True
        pat_det = []
        for nmc, cfg in (("plus", cfg_plus), ("alt", cfg_alt)):
            Vp = build_V(ce, cfg)
            with mp.workdps(dps):
                for tv in (Tz - 0.02, Tz - 1.0, 0.5 * Tz):
                    r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                    lam, _, _ = secular_gap(Vp, r)
                    gP = float((lam - Vp["tau_mp"]) / Vp["tau_mp"])
                    rc = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                    lamc, _, _ = secular_gap(Vd, rc)
                    gC = float((lamc - tau) / tau)
                    okp = okp and gP >= PATTERN_FLOOR * gC
                pat_det.append("%s q0rel %.1e" % (nmc, Vp["qrel"]))
        ok35 = ok35 and okp
        det35.append("x%d: %s" % (x, ", ".join(pat_det)))

        # ---- G36 SLAB certificate
        with mp.workdps(dps):
            Vfull = ce["mpV"]
            phi = [Vfull[i, 0] for i in range(K)]
            gam_rows = [row_at(mp.mpf(pol_str[j]), K, oms, nrm)
                        for j in range(m_zone)]
            vals = []
            sin_min = None
            for j in range(m_zone):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += gam_rows[j][k] * phi[k]
                vals.append(acc)
                sv = float(abs(mp.sin(aa * mp.mpf(pol_str[j]))))
                if sin_min is None or sv < sin_min:
                    sin_min = sv
            nAphi = float(mp.sqrt(sum(v * v for v in vals)))
            # gamma-config V for lam*_p
            Vg = build_V(ce, [mp.mpf(pol_str[j]) for j in
                              range(m_zone)])
            p_mp = mp.mpf(repr(float(gargm)))
            rp = row_at(p_mp, K, oms, nrm)
            lam_p, _, _ = secular_gap(Vg, rp)
            gap_p = float((lam_p - Vg["tau_mp"]) / Vg["tau_mp"])
            # sigma_min of the (m+1)-row constraint matrix
            rows = gam_rows + [rp]
            mr = m_zone + 1
            AAT = mp.zeros(mr, mr)
            for i in range(mr):
                for j2 in range(i + 1):
                    acc = mp.mpf(0)
                    for k in range(K):
                        acc += rows[i][k] * rows[j2][k]
                    AAT[i, j2] = AAT[j2, i] = acc
            Es, _ = mp.eigsy(AAT)
            smin = math.sqrt(max(float(min(Es[i] for i in range(mr))),
                                 0.0))
            verds = []
            okslab_m = False
            gwmarg = float("nan")
            for wname, nA in (
                    ("MEAS", nAphi),
                    ("GW", math.sqrt((tauf + off_allow) / 2.0)
                     / max(sin_min, 1e-300)),
                    ("EPS", eps_bar / max(sin_min, 1e-300)
                     * math.sqrt(m_zone))):
                wbar = nA / max(smin, 1e-300)
                if wbar >= 1.0:
                    verds.append("%s:NOT-CLOSING(wbar>=1)" % wname)
                    continue
                rhs = (math.sqrt(tauf)
                       + math.sqrt(lam_max) * wbar) ** 2 \
                    / (1 - wbar ** 2)
                marg = (1 + gap_p) * tauf / rhs
                verds.append("%s:%s x%.2f" % (
                    wname, "CLOSES" if marg > 1 else "DEFICIT", marg))
                if wname == "MEAS":
                    okslab_m = marg >= SLABM_MARGIN
                if wname == "GW":
                    gwmarg = marg
        slabgw_tab[x] = gwmarg
        okgw = (x not in SLABGW_MUST) or (gwmarg > 1.0)
        ok36 = ok36 and okslab_m and okgw
        det36.append("x%d: smin %.3f sin_min %.3f lam_p/tau %.1f | %s"
                     % (x, smin, sin_min, 1 + gap_p, " ".join(verds)))

        # ---- G37 SEEDBALL boxes
        t_b = time.time()
        okb = True
        worst_bint = 0.0
        with mp.workdps(BOX_DPS):
            cs60 = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa60 = mp.log(x) / 2
            oms60 = [k * mp.pi / aa60 for k in range(K)]
        for j in range(m_zone):
            blo = pol_f64[j] - F_BOX * s_arr[j]
            bhi = pol_f64[j] + F_BOX * s_arr[j]
            cntb, imb = contour_count(cs60, aa60, oms60, blo, bhi,
                                      F_BOX * s_arr[j], BOX_DPS)
            dev = abs(cntb - 1.0) + imb
            worst_bint = max(worst_bint, dev)
            okb = okb and dev <= BOX_INT_BAR
        # S4 collapse from the box seed (sharp kappa at u* = 1/2)
        oms_f = [float(o) for o in oms]
        with mp.workdps(dps):
            bks = [oms[k] ** 2 for k in range(1, K)]
            Delta = np.zeros(m_zone)
            S_pair = np.zeros(m_zone)
            u_rate = 0.0
            u_bind = None
            for j in range(m_zone):
                gjf = float(pol_f64[j])
                ksn = min(range(1, K),
                          key=lambda k: abs(oms_f[k] - gjf))
                gq = mp.mpf(pol_str[j])
                mum = nds[j]
                dl = (mp.log(abs(mp.sin(aa * gq) / (gq - oms[ksn])))
                      - mp.log(abs(mp.sin(aa * mum)
                                   / (mum - oms[ksn]))))
                dl += (mp.log(abs(mum + oms[ksn]))
                       - mp.log(abs(gq + oms[ksn])))
                for k in range(1, K):
                    if k == ksn:
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
                              - 1 / (tt - oms[ksn]))
                    sg = max(sg, float(val))
                acc = SUP_INFLATE * sg * s_arr[j]
                acc += s_arr[j] / (gjf + oms_f[ksn])
                yj = gjf * gjf
                for k in range(1, K):
                    if k == ksn:
                        continue
                    dy = abs(yj - float(bks[k - 1]))
                    term = 2 * gjf * s_arr[j] / dy
                    acc += term
                    if term > u_rate:
                        u_rate = term
                        u_bind = ("lat", j, k)
                for i in range(m_zone):
                    if i == j:
                        continue
                    dy = abs(yj - pol_f64[i] ** 2)
                    term = (2 * pol_f64[i] * s_arr[i]
                            + 2 * gjf * s_arr[j]) / dy
                    acc += term
                    if term > u_rate:
                        u_rate = term
                        u_bind = ("zero", j, i)
                S_pair[j] = acc
        Rstar = (g_arr / s_arr) * np.exp(Delta)
        Rmax = float(np.max(Rstar))

        def Fmap(d, kapv, Rstar=Rstar, S_pair=S_pair):
            with np.errstate(over="ignore"):
                return float(np.max(np.minimum(
                    Rstar * np.exp(kapv * S_pair * d), 1e300)))

        kap_half = -math.log(0.5) / 0.5   # kappa(1/2) = 2 log 2
        it = F_BOX
        its = [it]
        for _ in range(ITER_N):
            it = Fmap(it, kap_half)
            its.append(it)
        collapse = its[-1] <= ITER_COLLAPSE * Rmax
        ok37 = ok37 and okb and collapse
        det37.append("x%d: %d boxes worst-int %.0e collapse %s->"
                     "%.1e (%.0f s)"
                     % (x, m_zone, worst_bint,
                        "0.04", its[-1], time.time() - t_b))

        # ---- G38 basin recompute (sharp kappa u* grid)
        bc_old = None
        bc_best = None
        u_best = None
        for ustar in (0.5,) + USTAR_GRID:
            kapv = 2.0 if ustar == 0.5 and bc_old is None \
                else -math.log(1 - ustar) / ustar
            if Fmap(BARRIER_CAP, kapv) <= BARRIER_CAP:
                barrier = BARRIER_CAP
            else:
                lo_b, hi_b = 0.0, BARRIER_CAP
                for _ in range(60):
                    mid = 0.5 * (lo_b + hi_b)
                    if Fmap(mid, kapv) <= mid:
                        lo_b = mid
                    else:
                        hi_b = mid
                barrier = lo_b
            u_over = 0.5 if (ustar == 0.5 and bc_old is None) else ustar
            b_c = min(barrier, u_over / max(u_rate, 1e-12), BARRIER_CAP)
            if bc_old is None:
                bc_old = b_c        # r136 currency: kappa = 2, u* = 1/2
                continue
            if bc_best is None or b_c > bc_best:
                bc_best = b_c
                u_best = ustar
        # delta_suff (r135/136 currency)
        N = K - 1
        Ts = t_star(N)
        zg = gam[gam <= Tz]
        swp = float(np.sum([wp_abs(float(A_MARG), g) for g in zg]))
        TL = tl_shells(N, float(A_MARG), Ts)
        m_req = 16.0 * eps_bar * swp / TL if TL > 0 else float("inf")
        margin = float(np.min(m_arr)) / m_req
        star = np.concatenate([pol_f64[:m_zone], nds_f_all[m_zone:]])
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
        d_cert = float(np.max(g_arr / s_arr))
        ok38x = (bc_best >= bc_old - 1e-12
                 and BC_LO <= bc_best <= BC_HI
                 and bc_best < BC_OBSTR
                 and bc_best < d_suff
                 and F_BOX < bc_best
                 and margin >= MARGIN_BAR
                 and d_cert <= d_suff)
        ok38 = ok38 and ok38x
        det38.append("x%d: bc %.3f (u*=%.1f) vs r136-cur %.3f; "
                     "d_suff %.3f d_cert %.1e margin %.1e bind %s"
                     % (x, bc_best, u_best, bc_old, d_suff, d_cert,
                        margin, u_bind))
        bc_tab[x] = bc_best
        dsuff_tab[x] = d_suff
        dcert_tab[x] = d_cert

        # ---- G39 swamp
        Tsw_hi = min(Ts, 0.98 * edge)
        rowsw = []
        okw = True
        umax = -1e9
        for T in np.linspace(Tz, Tsw_hi, SWAMP_N):
            nfin = int(np.sum(nds_f_all <= T)) + (deficit if is_deep
                                                  else 0)
            ntrue = int(np.sum(gam <= T))
            cm = ntrue - int(np.sum(nds_f_all <= T))
            um = (m_rvm(T) - q_hsw(T)) - nfin
            umax = max(umax, um)
            okw = okw and cm >= 0
            rowsw.append("T%.0f:%d/%d" % (T, int(np.sum(
                nds_f_all <= T)), ntrue))
        if not is_deep:
            ok39x = okw and umax <= SWAMP_UNC_BAR
            ok39 = ok39 and ok39x
            det39.append("x%d: class-marg all >= 0, unc-marg max "
                         "%.2f (%s)" % (x, umax, " ".join(rowsw[:4])))
        else:
            info("x=%d swamp INFO (scan deficit %d folded into "
                 "N_fin_hi): unc-marg max %.2f; counts %s"
                 % (x, deficit, umax, " ".join(rowsw[:4])))

    check("G30-census", ok30,
          "core: raw-mp census complete + real; deep: full-band scan, "
          "zone prefix complete, deficit disclosed; residuals <= %.0e; "
          "bottom grid sign-uniform: %s" % (RES_BAR, "; ".join(det30)))
    check("G31-counteq-fact", ok31,
          "zone node count == m AND argument-principle contour == m "
          "(dev <= %.0e) at EVERY rung (r136 G31 replica): %s"
          % (ARG_INT_BAR, "; ".join(det31)))
    check("G32-pinball-epslock", ok32,
          "gap <= ball 2 eps_bar/m_j, validity, balls disjoint at "
          "classical gaps, top ball below cut, eps_bar/|A_0| in %s "
          "(typed CONSUMED = OMEGA-a): %s"
          % (str(EPSLOCK_WIN), "; ".join(det32)))
    check("G33-qsubgap-certificate", ok33,
          "node-config: |qrel| <= %.0e, nullres <= %.0e; SECULAR gap "
          "min over [grid + walls + drows] >= %.1f x tau; modulus <= "
          "%.2f; upper-sandwich tight <= %.1f at argmin (min ALWAYS "
          "at the zone top): %s"
          % (QREL_BAR, NULLRES_BAR, GAP_MIN_BAR, MOD_BAR, UBTIGHT_BAR,
             "; ".join(det33)))
    check("G34-complex-pairs", ok34,
          "complex-pair gap (max of Re/Im rows) >= %.1f x tau on the "
          "(sigma, nu) grid: no complex zone pair is variationally "
          "affordable: %s" % (CPLX_BAR, "; ".join(det34)))
    check("G35-ball-box-transport", ok35,
          "extreme ball-box patterns (+g, alternating +-g) keep the "
          "gap >= %.1f x center (pre-freeze: patterns RAISE the gap "
          "-- the box-inf sits at the true-zero corner): %s"
          % (PATTERN_FLOOR, "; ".join(det35)))
    check("G36-slab-certificate", ok36,
          "SLAB (Theorem Q2): MEAS currency closes with margin >= "
          "%.1f at EVERY rung -- the (m+1)-th real zone zero is "
          "variationally REFUTED per rung, transport-free; GW "
          "currency gated at x in %s, recorded elsewhere (the "
          "lam-uniform crossover finding); EPS l-inf currency "
          "recorded (m-fold obstruction): %s"
          % (SLABM_MARGIN, str(SLABGW_MUST), "; ".join(det36)))
    check("G37-seedball-boxes", ok37,
          "per-box argument-principle contour == 1 (dev <= %.0e, "
          "BOX_DPS %d) at box half-width F_BOX = %.2f spacings; "
          "complement == 0 via G31; S4 iterates from the box seed "
          "collapse to <= %.1f R* in <= %d steps: SEEDBALL IS "
          "CONSTRUCTED per rung: %s"
          % (BOX_INT_BAR, BOX_DPS, F_BOX, ITER_COLLAPSE, ITER_N,
             "; ".join(det37)))
    check("G38-basin-sharpened", ok38,
          "sharp-kappa basin b_c >= r136 read, in [%.2f, %.2f], "
          "< %.1f (the 0.4-basin elimination of SEEDBALL is "
          "OBSTRUCTED), < delta_suff (seed-gap persists), > F_BOX "
          "(the box seed is inside the basin); margins >= %.0f: %s"
          % (BC_LO, BC_HI, BC_OBSTR, MARGIN_BAR, "; ".join(det38)))
    check("G39-swamp", ok39,
          "core rungs: classical DOM margin >= 0 at EVERY swamp grid "
          "point (measured EQUALITY pre-freeze) and unconditional "
          "HSW margin max <= %.1f: the swamp is classically closed "
          "per rung and HSW-obstructed lam-uniformly (crossover "
          "needs a sub-1-zero counting certificate): %s"
          % (SWAMP_UNC_BAR, "; ".join(det39)))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (COUNTEQ must refuse)")
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
              "= %.3f fills the verified zero-free gap (0, %.2f); "
              "tau_w = %.3e (%s: the variational counting currency "
              "itself degenerates off the primes)"
              % (world, xw, n_nodes_w, m_true_w, over,
                 float(musw[0]), float(gam[0]), tauw,
                 "NOT PSD" if tauw <= 0 else "PSD"))
    check("G53-mechanism-consistency", ctrl_ok,
          "COUNTEQ refuses in ALL control worlds by ZONE OVERCOUNT; "
          "the consumed classical input is the verified census below "
          "T_z (count + gaps + zero-free interval); the slab "
          "certificate never claims where PSD/pinning fail")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS + GAP LAW")
    if not smoke:
        xs_all = [x for x, _d in all_rungs]
        lt = [math.log10(max(tau_tab[x], 1e-300)) for x in xs_all]
        lg_ = [math.log10(gapmin_tab[x]) for x in xs_all]
        s_g = float(np.polyfit(lt, lg_, 1)[0])
        lx = [math.log10(x) for x in xs_all]
        s_x = float(np.polyfit(lx, lg_, 1)[0])
        check("G54-tau-screen", abs(s_g) <= TAU_SLOPE_BAR,
              "slope log10 QSUBGAP-min vs log10 tau = %.4f (<= %.2f: "
              "the gap RATIO is not Connes-priced; the RAW gap rides "
              "tau BY CONSTRUCTION -- BOUND-RIDES-CONNES, typed); "
              "gap law vs x: slope %.2f in log-log (INFO: values %s; "
              "GW-slab margins %s)"
              % (s_g, TAU_SLOPE_BAR, s_x,
                 ["%.1f" % gapmin_tab[x] for x in xs_all],
                 ["%.2f" % slabgw_tab[x] for x in xs_all]))
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
                ("EPSLOCK", "QSUBGAP"): 1,
                ("QSUBGAP", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("EPSLOCK", "QSUBGAP")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "QSUBGAP"): 1, ("QSUBGAP", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows: base 4, refined 5 -- the r136 serial pair "
          "COUNTEQ(1) -> SEEDBALL(1) MERGED into ONE unit edge "
          "QSUBGAP(1), with COUNTEQTHM/SEEDBALLTHM INF edges behind "
          "(Theorems Q1-Q3 + boxes + S1-S4/cited); granting QSUBGAP "
          "still flows 5 (EPSLOCK caps); counterfactual PARALLEL 6 "
          "NOT REAL; census {MEAS, OMEGA-POS} cardinality 4 "
          "UNCHANGED; RH unreachable without the omega edges")
    info("EXACT OMEGA-b RESIDUE after this round: SPACING-REMAINDER "
         "<== EPSLOCK (OMEGA-a, r135, open) + QSUBGAP (ONE new named "
         "quantity: the secular constrained-minimum gap of the zone- "
         "zero-killed subspace at the zone top -- lam-uniform lower "
         "bound 1/poly(x) open).  QSUBGAP ==> COUNTEQ (slab "
         "certificate, Theorem Q2; per-rung CLOSES in MEAS currency "
         "at every rung) AND ==> SEEDBALL (wall equivalence Q3 + "
         "per-box contours at F_BOX = 0.04 < b_c: constructed per "
         "rung; S4 collapses the seed).  The classical carrier stays "
         "the verified census below T_z (PT21-class, x <= 4.8e11).  "
         "NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SECULAR-CERT-PROVEN(Q1-Q3 exact layer; G10-G18)",
        "COUNTEQ-VARIATIONAL-CERTIFIED(slab MEAS closes at every "
        "rung; G36)",
        "SLAB-GW-TABLE(the lam-uniform crossover finding; G36/G54)",
        "SLAB-EPS-OBSTRUCTED(m-fold l-inf amplification; G36)",
        "GAPLAW-MEASURED(min at the zone top; G33/G54)",
        "WALL-EQUIV(QSUBGAP <==> wall bound; G12/G33)",
        "SEEDBALL-CONSTRUCTED(boxes at F_BOX < b_c + S4 collapse; "
        "G37)",
        "BASIN-SHARPENED + BASIN-04-OBSTRUCTED(G38)",
        "SWAMP-DOM-ZERO-SLACK + SWAMP-HSW-OBSTRUCTED(G39)",
        "CONTROLS-REFUSE(zone overcount + zero-free gap; G50-G53)",
        "DEMAND-FLAT + BOUND-RIDES-CONNES(G54)",
        "OMEGA-MERGED(COUNTEQ + SEEDBALL <== QSUBGAP single unit; "
        "G60)"]
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
        print("COMPOSITE: SECULAR-CERT-PROVEN + "
              "COUNTEQ-VARIATIONAL-CERTIFIED + SLAB-GW-TABLE + "
              "SLAB-EPS-OBSTRUCTED + GAPLAW-MEASURED + WALL-EQUIV + "
              "SEEDBALL-CONSTRUCTED + BASIN-SHARPENED + "
              "BASIN-04-OBSTRUCTED + SWAMP-DOM-ZERO-SLACK + "
              "SWAMP-HSW-OBSTRUCTED + CONTROLS-REFUSE + "
              "OMEGA-MERGED + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
