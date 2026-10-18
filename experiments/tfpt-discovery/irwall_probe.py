#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""irwall_probe -- PRIME.STAGE1.IRWALL.01: the IR wall of the
adele-class cokernel coupling attacked on an explicit coupled ladder
omega -> 1, T -> infinity.

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  NO RH CLAIM.  Round 119
(coupling_ansatz_probe.py, COUPLING-STRUCTURAL(C1)) established: the
quotient Gram of the corpus nodes v_j = 1/(sigma_j + i tau) against
coker(E), E = sum_n n^{-1/2} U_n (Mellin multiplier
m(tau) = zeta(1/2 - i tau)), in the omega-weighted H^1_ell completion
(global hats + source-only dip refinement; zeros never input),
reproduces the truncated zero-side Pick block T_omega at defect 0.0033
(ell = 0.8, Omega = 25, T ~ 63), RK normalization 2*ell*omega fitted
1.0033, PSD exact -- and the round-119 Omega ladder already measured
the wall: Omega = 40 at FIXED T = 63 degrades the defect to 0.0087.
The four open data of round 119 are attacked here: (ii) the IR limit
(T1), (i) the completion/isometry datum (T2), (iv) the oscillation
coupling (T3), plus the min-cut price (T4) and controls incl. the
round-117 Epstein witness (T5).

===========================================================================
T1 -- THE IR LADDER (the priority)
===========================================================================
Coupled schedule, frozen: rung heights T_r chosen SOURCE-ONLY as
argmax |zeta(1/2 + i tau)| on the declared scan windows
(58,64), (88,94), (123,129), (168,174), (228,234); weight scale
Omega_r = 25 * T_r / T_0 (the round-119 ratio Omega/T ~ 0.3965 held
fixed -- omega -> 1 pointwise on every compact); RK scale
ell_r = 0.8 * log(T_0/2pi) / log(T_r/2pi) (the mean zero gap
2pi/log(T/2pi) shrinks like 1/log T; this schedule keeps gap/ell
CONSTANT, i.e. constant RK cross-talk -- the candidate IR schedule,
in the round-118 delta(L) tradition); grid step dtau_r = 0.01875 *
ell_r (the round-119 best ratio dtau/ell held fixed: constant
discretization level).  Per rung: quotient-Gram defect vs the
source-only box target T_omega (own EM zeta/zeta' + own digamma,
c = 0.45, dt = 0.004, integer zero-count gates), RK normalization
s_fit, lambda_min, completion/range/quotient traces, basis census,
ridge-conditioning audit; smooth control (multiplier 1/(s-1):
cokernel must empty) and golden-scramble control (must die) THROUGH
THE SAME LIFT AT EVERY RUNG.  Counterfactuals: (a) the round-119
Omega = 40 at T_0 reproduced (frozen 0.0087), and the same
Omega-ratio 0.634 re-measured at rung 2 -- is the ratio penalty
stationary in T (edge law) or growing (divergence)?  (b) fixed
ell = 0.8 (schedule off) at rung 2.  Outcome adjudication (frozen):
CARRIES if every rung defect <= 3e-2 AND top-rung defect <= 3 * rung-0
defect AND s_fit within 15 percent everywhere AND PSD exact AND
controls die everywhere; DIVERGES if the defect grows monotonically
past 3x with the diagnostics naming the diverging object (completion
norms / range trace / target degeneration / conditioning);
DEGENERATES if the identity holds but the target or quotient block
collapses toward rank deficiency (lambda_min/trace collapse > 100x
vs rung 0).  The IR convergence of the TARGET itself is priced
against the certified floors' object: |T_omega(rung) - Pick_4| must
match the declared mean-density deficit model (arch density
(Re psi(1/4 + i tau/2)/2 - log(pi)/2)/pi, welded to RvM in round 119
at 7.4e-6; (1-omega) weight deficit on [0,T] plus the |tau| > T
tail, log-grid to 1e5) at 35 percent Frobenius -- and must shrink
monotonically along the ladder.

===========================================================================
T2 -- THE ISOMETRY / COMPLETION DATUM
===========================================================================
(a) SYMBOLIC (sympy, exact): the H^1_ell reproducing kernel on the
line is K(tau,tau') = e^{-|tau-tau'|/ell}/(2 ell) -- the ODE
(1 - ell^2 d^2) K = 0 off-diagonal plus the derivative jump
-ell^2 [K']_{-}^{+} = 1 verified exactly; for the exactly solvable
exponential weight omega = e^{2 alpha tau} the diagonal is
K(g,g) = 1/(2 ell omega(g) sqrt(1 + alpha^2 ell^2)) -- the WKB
correction to the RK normalization is (1 + alpha^2 ell^2)^{-1/2},
i.e. for our omega (|alpha| <= 1/Omega) at most ell^2/(2 Omega^2)
per rung: printed ladder, all << the 15 percent bar and SHRINKING
along the schedule (ell down, Omega up).
(b) MEASURED (the keystone): the DISCRETE reproducing kernel of the
very completion used by the lift (tridiagonal H^1_{ell,omega}
operator on the tau grid, Thomas solve) is evaluated at the emergent
dip centers: 2*ell*omega(g)*K_disc(g,g) must equal 1 up to
discretization; measured on the dtau ladder (0.0375, 0.01875,
0.009375) * ell and Richardson-extrapolated: the gate demands the
extrapolated normalization equal 1 within 5e-3 -- the RK
normalization of the completion itself is EXACT in the continuum.
Cross-talk: measured K_disc off-diagonals vs the exact e^{-gap/ell}
law (factor-2 gate); the cross-talk-corrected zero-side prediction
T_pred = V_Z (2 ell K_Z)^{-1} V_Z^H (K_Z = measured discrete RK
matrix at the dips) is compared to T_omega (same class as the
measured ell-floor below).
(b') THE COMPLETION FLOOR (the discovery of the smoke ladder, frozen
as the round's central T2 measurement): the JOINT refinement table
at the baseline rung -- dtau/ell in (0.0375, 0.01875, 0.009375) x
hat-spacing/ell in (0.5, 0.25, 0.125), both ell = 0.8 and ell = 0.4
-- shows the identity defect does NOT collapse to 0 with the grid at
fixed ell: at ell = 0.8 the fully refined defect CONVERGES UPWARD to
delta*(0.8) ~ 0.0056 (under-refined configs undershoot through an
accidental crossing -- the round-119 operating point sat near it),
while at ell = 0.4 the fully refined defect falls to delta*(0.4) ~
0.0010 and the RK fit brackets 1 from the other side (1.0057 above
vs 0.9990 below).  AMENDMENT to the round-119 C1d interpretation
(their gates stand, the reading sharpens): the residual defect is
grid PLUS a finite ell-window floor delta*(ell), and the floor
shrinks by the measured factor >= ~5 per ell-halving -- the exact
identity needs the joint limit ell -> 0 on top of Omega, T ->
infinity.  Gates: refinement increments shrink at ell = 0.8
(saturation exists); delta*(0.4) <= 0.35 delta*(0.8) (the ell law);
|s*(0.4) - 1| <= 0.35 |s*(0.8) - 1| with opposite signs (the
normalization brackets the theory value and tightens).
(c) THE CANONICAL NORM (typed, cited; NOT proven here): the norm in
which the zero evaluations are EXACTLY orthonormal is the de Branges
norm of a structure function built from xi(1/2 - i z); the existence
of that norm as a Hilbert-space completion is the Hermite--Biehler
property of xi, which is EQUIVALENT to RH (Lagarias, Hilbert spaces
of entire functions / dB theory: "assuming RH, E~0(z) is a structure
function"; orthonormal RK bases sit exactly at the phase points --
Antezana--Marzo--Olsen IMRN 2016 Thm 1.1).  The honest T2 endpoint:
H^1_{ell,omega} is a mollified proxy whose RK normalization
converges to the theory value (measured here); DERIVING the exact
canonical completion unconditionally IS RH -- a structural
obstruction of proven class, cited, not a probe theorem.  DISGUISE
screen: the finite object never touches this equivalence.

===========================================================================
T3 -- THE OSCILLATION DEBT (open datum iv)
===========================================================================
Channel split of the truncated zero-side block, frozen: mean channel
M_mean[j,k] = int_0^T dbar(tau) omega(tau) 2 Re[1/((sigma_j - i tau)
(sigma_k + i tau))] d tau with dbar = the arch density above (the
degenerate orbit's density, round-119 E7); oscillation channel
O = T_omega - M_mean.  Measured per rung: how much of O the quotient
Gram reproduces beyond its own error (digits_matrix = log10(|O|_F /
|Re Ghat - T_omega|_F)); at the c* packet (ground eigenvector of
Pick_4, warded to the round-115/119 lambda_4 = 1.106e-14): q_mean =
2 int dbar omega |g_c*|^2, q_T = the omega-weighted box band mass of
the packet (precise, contour currency), q_G = c*^T Re(Ghat) c*
(defect-limited, Richardson over the R0 dtau ladder), digits_packet
= log10(|q_mean| / max(|q_G - q_T|, bar)).  HONESTY TYPING (the
tau-screen): the PSD sign of the quotient Gram bounds the TOTAL
packet value one-sidedly; it is NOT an independent sign source for
the oscillation channel alone -- printed and typed, no upgrade.  Z1:
the cache-transcribable integrand (Lambda partial sum, pole-free in
the box) reads ~0 both at the block and at the packet: the
oscillation channel lives on the poles of xi'/xi, resummed currency
only; no zero-cache is read anywhere (AST firewall).

===========================================================================
T5 -- THE EPSTEIN WITNESS (off-line control through the same lift)
===========================================================================
The round-117 witness: Q = x^2 + 5 y^2 (disc -20, h = 2), off-line
zero at rho ~ 0.6969270453 + 36.3740636864 i.  NEW INSTRUMENT
(frozen): the genus decomposition Z_Q(s) = zeta(s) L(s,chi_-20) +
L(s,chi_-4) L(s,chi_5) (one class per genus at disc -20) makes Z_Q
computable ON THE LINE by own Euler--Maclaurin Hurwitz machinery (no
exponential cancellation) -- welded (i) against the literal lattice
sum at s = 3, 2.5, (ii) against own mp Hurwitz EM at complex spots
(1e-9), (iii) against the round-117 incomplete-gamma xi_Q at
s = 0.5 + 3 i (1e-8), (iv) functional-equation residual (1e-8), (v)
witness re-refined by mp Newton from the frozen seed 0.7 + 36.4 i
and matched to the round-117 record at 1e-6.  GLOBAL MEASUREMENT:
the quotient-Gram defect of the Epstein world on a source-only box
(window (37.4, 39.2), witness inside) at ell = 0.8 vs ell = 0.4:
the target is DOMINATED by the low on-line zeros (first at gamma ~
1.45) where the (ell/|sigma + i gamma|)^2 evaluation-smoothing
class is largest; gates: monotone on ell, plus a dedicated LOW-ZERO
window (count-gated) whose response ratio must sit in (0.6, 1.4) --
the identity carries at the boundary zero.  THE WINDOWED DETECTOR
(the off-line test): the box target counts the off-line quadruple;
the line multiplier does NOT vanish near gamma_w (soft dip only),
so the continuum cokernel carries no state there.  Localized
statistic, frozen: cos^2-tapered window w (flat |d| <= 0.5, zero at
|d| = 1.0) at +-gamma_w and at a control on-line dip (frozen rule:
the ISOLATION-MAXIMIZING dip center with distance >= 2.5 from
gamma_w, 3.0 <= c <= T_E - 1.2 -- an isolated zero, so the window
holds its full response energy; the zeta world calibrates the
statistic at 0.97); windowed quotient response G_win = resid^H w
resid / (2 ell) (explicit-residual coker at ell = 0.4, dtau =
0.0075, recipe untouched); windowed target T_win = sum over the
Newton-refined zeros inside the +-0.7 small boxes of w(gamma_z)
omega(z) kernel; small-box zero counts by contour integral must be
INTEGER and equal the number of refined zeros (witness upper box:
EXACTLY 2, the off-line pair rho, 1 - conj(rho), both |Re s - 1/2|
> 0.15; control: on-line to 1e-8).  Gates: witness response ratio
tr(G_win)/tr(T_win) <= 0.2 (the cokernel is EMPTY where the
multiplier does not vanish -- the identity SEES the off-line zero
as missing response mass); control ratio in (0.8, 1.2); witness
soft-dip floor min|m_Q| >= 25x the sharpest on-line dip on the same
grid (the currency of the detection).  The zeta world pushed
through the SAME windows is the placebo (no zeros in the witness
window: count 0, response at noise, printed).  A quotient-Gram
identity that sees an off-line zero as a localized response deficit
is the tau-screen answer: the channel distinguishes worlds, no
disguise.

===========================================================================
T4 -- THE MIN-CUT PRICE
===========================================================================
The round-116 graph (idgraph_search_probe.py NODES/EDGES, copied
verbatim as frozen data and warded against the owner file) is
re-adjudicated: base flows reproduced (conservative 2, full 4, BFS
unreachability, transfer-null); the remodel replaces the single edge
PICK-FLOORS-FIN -> SV-HYP by the explicit omega gate node
SV-OMEGA-GATE (flow-equivalent, gated); the extension adds
IRQG-MEAS (this round's IR-stable quotient-Gram identity, MEAS
grade, fed from PICK-FLOORS-FIN by the measured dictionary) routed
through the SAME omega gate: extended flow must stay 4 -- the
identity SHARES the existing capacity-1 Pick-floors omega edge (same
evidence source: own EM zeta data; same quantifier class: infinitary
positivity/limit introduction).  The counterfactual wiring
(independent omega edge IRQG-MEAS -> SV-HYP) flows 5 and is printed
as INFO, not gated true-of-the-world.  THE EXACT REMAINING OMEGA
(printed, typed): "the quotient-Gram identity holds at omega == 1,
T = infinity, for every N and every node family, with the zero
evaluations exactly orthonormal in the completion" -- by T2(c) this
contains the Hermite--Biehler/RH equivalence: same wall, sharper
coordinates.  No new unconditional statement beyond the round-116
A2 cap is claimed.

===========================================================================
DECLARED NUMERICS (frozen before the adjudication run)
===========================================================================
mp: DPS = 100 pins/floors/c*; EM 96/28 vs 128/32 stability gate
1e-70; high-T welds vs mp EM (cutoff 400, terms 20, workdps 50) at
box-corner spots, bar 1e-9.  numpy: own EM zeta/zeta' (M = 250,
K = 12), own complex digamma (shift 32), own EM Hurwitz (M = 120,
K = 12) for the four Dirichlet factors (chi_-20 on
{1,3,7,9,11,13,17,19} = {+,+,+,+,-,-,-,-}; chi_-4; chi_5).  Boxes:
c = 0.45, dt = 0.004, dual-step gate at rungs 0-1 (bar 1e-6), zero
counts integer to 2e-4, T_omega PSD to -1e-6 * max entry.  Coker
recipe = round 119 VERBATIM (hats spacing 0.5 ell + 24 Cauchy atoms
+ source-only dips: minima of |m| below 0.35 median, merge 0.25,
half-width min(3 ell, 1.0), fine spacing 2 dtau; ridge 1e-11 on
normalized normal equations), implemented chunk-accumulated
(chunk 4000, quotient = V^H V - C^H (Ghat + ridge)^{-1} C,
algebraically identical); ridge-audit 10x at every rung (bar 20
percent); deterministic multiplier perturbation (1 + 1e-9
cos(0.7 tau)) at rungs 0 and 2: response must be NONZERO (the
round-118 ambient-dps trap: an exactly-zero response is the red
flag) and <= 1e-4.  Golden scramble (sqrt(5)-1)/2 on 250 dilation
lengths, weights kept.  Smooth trace-ratio bar 1e-2; scramble defect
bar > 0.5.  Joint-refinement floor table at rung 0: ell = 0.8 at
(dtau/ell, spacing/ell) in {(0.0375,0.5), (0.01875,0.5),
(0.009375,0.5), (0.01875,0.25), (0.01875,0.125), (0.009375,0.25),
(0.009375,0.125)}; ell = 0.4 at {(0.01875,0.5), (0.01875,0.25),
(0.01875,0.125), (0.009375,0.5), (0.009375,0.25), (0.009375,0.125)};
delta*(ell) = the (0.009375, 0.125) corner.  Density/deficit
integrals: trapezoid dtau = 0.01 on [0, T], log-grid 4000 points to
1e5 for the tail.  Packet band bar = 5 * max(box dual-res dev, 1e-9)
* packet scale (conservative; the measured dual-res level is also
printed).  Epstein: lattice weld qmax 2e5; witness Newton dps 50
(mp Hurwitz M = 200, K = 24); grids ell = 0.8 and 0.4 at dtau =
0.0075, Omega = 25; window half-width 1.0 (flat to 0.5), small-box
half-height 0.7 with dt = 0.002, control rule: isolation-maximizing
dip >= 2.5 from gamma_w in [3.0, T_E - 1.2]; low-zero window at the
smallest dip center; response-ratio bars 0.2 / (0.8, 1.2) /
(0.6, 1.4); soft-dip currency bar 25x.  Frozen round-119 reads:
defect 0.0033 (bar 15
percent), s_fit 1.0033 (bar 0.005 absolute), Omega-40-at-T0 defect
0.0087 (bar 20 percent), heights T* = 63.06, T2 = 126.00 (bar 0.05).
Frozen round-117 read: witness 0.6969270453 + 36.3740636864 i (bar
1e-6).  Frozen floors/debt: v915/sieve4 intervals warded verbatim;
lambda_4 = 1.106e-14; debt digits (1.07, 5.23, 9.61, 14.60).  Pin
nodes sigma_j = 1 + 1/j, N = 4.  No randomness anywhere.  Runtime
bar 7200 s.  Smoke mode (env IRWALL_SMOKE=1) truncates the ladder
for development only and is NOT the run of record; the record runs
the full frozen spec twice (deterministic re-run gate, diff modulo
runtime lines).

===========================================================================
VERDICT ENUM (frozen, exactly one composite line)
===========================================================================
  IRWALL-CARRIES(schedule)      outcome (a): the identity survives
      the coupled schedule Omega = 0.3965 T, ell = 1.844/log(T/2pi),
      dtau = 0.01875 ell with defect <= bar at every rung, top rung
      <= 3x baseline, PSD exact, controls dying, target converging
      to Pick_4 at the modeled mean-density rate -- PRICED with the
      T2(b') completion floor: the carried defect is the ell-window
      floor delta*(ell), constant along the schedule (gap/ell
      fixed), vanishing only on the additional ell -> 0 axis
      (measured law, one halving).
  IRWALL-DIVERGES(object)       outcome (b): monotone defect growth
      past 3x -- the named diverging object from the trace/
      conditioning diagnostics.
  IRWALL-DEGENERATES            outcome (c): identity survives but a
      block collapses toward rank deficiency (>100x lambda_min/trace
      collapse vs baseline).
  IRWALL-INSTRUMENT-EDGE        an instrument/ward gate fails
      (exit 1, no mathematical verdict).
Composite suffixes: COMPLETION-FLOOR(delta* law measured),
ISO-CANONICAL-RH-EQUIV(cited)+RK-DIAG-TO-1(measured),
OSC-DIGITS(matrix m / packet p), EPSTEIN-OFFLINE-SEEN(windowed) or
-BLIND, MINCUT-UNCHANGED(4) or -CHANGED(n).

Writes stdout only.  No verification/, no ledger, no manifest, no
website, no commit.  Reads only the declared ARTIFACTS allowlist
(read-only).  NO RH CLAIM.  EXPLORATION ONLY.  A structural identity
for a TRUNCATED block, however IR-stable, is not RH; the all-h/all-N
positivity of the canonical ladder remains THE RH-hard quantifier.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np
import sympy as sp

T0_WALL = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SMOKE = os.environ.get("IRWALL_SMOKE", "") == "1"

ARTIFACTS = {
    "ep_log": "experiments/tfpt-discovery/eulerpick_ladder_frozen.log",
    "s4_log": "experiments/tfpt-discovery/sieve4_run1.log",
    "r119": "experiments/tfpt-discovery/coupling_ansatz_probe.run1.log",
    "r119src": "experiments/tfpt-discovery/coupling_ansatz_probe.py",
    "r117src": "experiments/tfpt-discovery/radius4_reduction_probe.py",
    "r116src": "experiments/tfpt-discovery/idgraph_search_probe.py",
    "stage1": "experiments/tfpt-discovery/stage1_construction_probe.py",
}

# ---------------------------------------------------------------- frozen
PIN_COUNT = 4
CERTIFIED = {
    1: (4.5917135e-2, 4.5917136e-2),
    2: (9.0288701e-6, 9.0289075e-6),
    3: (2.3643695e-10, 1.1497752e-9),
    4: (8.278338e-15, 1.3840906e-14),
}
FROZEN_LAM4 = 1.106e-14
FROZEN_DEBT_DIGITS = (1.07, 5.23, 9.61, 14.60)
BASE_DEFECT = 0.0033
BASE_SFIT = 1.0033
BASE_OM40 = 0.0087
BASE_TSTAR = 63.06
BASE_T2 = 126.00
WITNESS_R117 = complex(0.6969270453, 36.3740636864)
WITNESS_SEED = complex(0.7, 36.4)

DPS = 100
BOX_C = 0.45
BOX_DT = 0.004
OMEGA0 = 25.0
ELL0 = 0.8
DTAU_RATIO = 0.01875
RUNG_WINDOWS = ((58.0, 64.0), (88.0, 94.0), (123.0, 129.0),
                (168.0, 174.0), (228.0, 234.0))
RICH_RATIOS = (0.0375, 0.01875, 0.009375)
CHUNK = 4000
RIDGE = 1e-11
DEFECT_BAR = 3e-2
CARRY_FACTOR = 3.0
NORM_BAR = 0.15
P4_MODEL_BAR = 0.35
EPS_WINDOW = (37.4, 39.2)
EPS_ELL = 0.8
EPS_DTAU = 0.0075
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
X_SCR = 250
RUNTIME_BAR = 7200.0
N_CHECKS_EXPECTED = 49

CHECKS: list[tuple[str, bool, str]] = []
ARTIFACT_TEXT: dict[str, str] = {}


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-46s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print("%s   [t=%.1f s]" % (title, time.time() - T0_WALL))
    print("=" * 78)


def fmt(x, digits: int = 8) -> str:
    return mp.nstr(x if isinstance(x, mp.mpf) else mp.mpf(x), digits,
                   min_fixed=0, max_fixed=0)


def read_artifact(key: str) -> str:
    """The ONLY repository read path.  Allowlist enforced."""
    if key not in ARTIFACTS:
        raise RuntimeError("artifact not in allowlist: %s" % key)
    if key in ARTIFACT_TEXT:
        return ARTIFACT_TEXT[key]
    path = os.path.join(ROOT, ARTIFACTS[key])
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        ARTIFACT_TEXT[key] = fh.read()
    return ARTIFACT_TEXT[key]


def ward(key: str, tokens: list[str]) -> tuple[bool, list[str]]:
    text = read_artifact(key)
    missing = [token for token in tokens if token not in text]
    return not missing, missing


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {"__future__", "ast", "hashlib", "math", "os", "time",
                     "mpmath", "numpy", "sympy"}
    forbidden_calls = {"load", "loadtxt", "genfromtxt", "fromfile",
                       "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    forbidden_attrs = {"zeta", "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    open_scopes: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    for fn in ast.walk(tree):
        if isinstance(fn, ast.FunctionDef):
            for node in ast.walk(fn):
                if (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Name)
                        and node.func.id == "open"):
                    open_scopes.append(fn.name)
    stray = [name for name in open_scopes
             if name not in ("read_artifact", "firewall_audit")]
    if stray:
        bad.append("open-outside-allowlist:%s" % stray)
    return not bad, "violations=%s" % (bad or "none")


# ------------------------------------------- Euler--Maclaurin source (mp)
def dirichlet_logderivative(s, cutoff: int, terms: int):
    total = mp.mpf(0)
    derivative = mp.mpf(0)
    for n in range(1, cutoff):
        power = mp.power(n, -s)
        total += power
        derivative -= mp.log(n) * power
    M = mp.mpf(cutoff)
    logM = mp.log(M)
    lead = M ** (1 - s) / (s - 1)
    total += lead
    derivative += lead * (-logM - 1 / (s - 1))
    half = mp.mpf("0.5") * M ** (-s)
    total += half
    derivative -= logM * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        rising = mp.rf(s, order)
        coefficient = mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
        correction = coefficient * rising * M ** (-s - order)
        harmonic = mp.fsum(1 / (s + j) for j in range(order))
        total += correction
        derivative += correction * (harmonic - logM)
    return total, derivative


def zeta_logderiv(s, cutoff: int = 96, terms: int = 28):
    value, derivative = dirichlet_logderivative(s, cutoff, terms)
    return derivative / value


def mp_hurwitz_pair(s, a, cutoff: int = 200, terms: int = 24):
    """(zeta_H(s, a), d/ds zeta_H(s, a)) by Euler--Maclaurin in mp."""
    total = mp.mpc(0)
    derivative = mp.mpc(0)
    for n in range(cutoff):
        base = mp.mpf(n) + a
        power = base ** (-s)
        total += power
        derivative -= mp.log(base) * power
    M = mp.mpf(cutoff) + a
    logM = mp.log(M)
    lead = M ** (1 - s) / (s - 1)
    total += lead
    derivative += lead * (-logM - 1 / (s - 1))
    half = mp.mpf("0.5") * M ** (-s)
    total += half
    derivative -= logM * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        rising = mp.rf(s, order)
        coefficient = mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
        correction = coefficient * rising * M ** (-s - order)
        harmonic = mp.fsum(1 / (s + j) for j in range(order))
        total += correction
        derivative += correction * (harmonic - logM)
    return total, derivative


def h_pole(sigma):
    s = mp.mpf("0.5") + sigma
    return 1 / s + 1 / (s - 1)


def h_gamma(sigma):
    s = mp.mpf("0.5") + sigma
    return mp.digamma(s / 2) / 2 - mp.log(mp.pi) / 2


def pin_reference(sigma):
    return h_pole(sigma) + h_gamma(sigma) + zeta_logderiv(mp.mpf("0.5")
                                                          + sigma)


def pick_matrix(values, sigmas):
    n = len(values)
    matrix = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            matrix[j, k] = (values[j] + values[k]) / (sigmas[j] + sigmas[k])
    return matrix


# ------------------------------------------- numpy Euler--Maclaurin zeta
BERN2K = (1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66,
          -691.0 / 2730, 7.0 / 6, -3617.0 / 510, 43867.0 / 798,
          -174611.0 / 330, 854513.0 / 138, -236364091.0 / 2730)


def np_hurwitz_pair(s: np.ndarray, a: float, cutoff: int = 120,
                    terms: int = 12) -> tuple[np.ndarray, np.ndarray]:
    """Own vectorized EM Hurwitz zeta: (zeta_H(s,a), d/ds zeta_H(s,a))."""
    s = np.asarray(s, dtype=complex)
    flat = s.ravel()
    z = np.zeros(flat.shape, dtype=complex)
    dz = np.zeros(flat.shape, dtype=complex)
    base = np.arange(0, cutoff, dtype=float) + a
    lg = np.log(base)
    chunk = 4000
    for lo in range(0, flat.size, chunk):
        sc = flat[lo:lo + chunk, None]
        P = np.exp(-sc * lg[None, :])
        z[lo:lo + chunk] = P.sum(axis=1)
        dz[lo:lo + chunk] = -(P * lg[None, :]).sum(axis=1)
    M = cutoff + a
    logM = math.log(M)
    lead = np.exp((1.0 - flat) * logM) / (flat - 1.0)
    z += lead
    dz += lead * (-logM - 1.0 / (flat - 1.0))
    half = 0.5 * np.exp(-flat * logM)
    z += half
    dz += -logM * half
    rising = flat.copy()
    harm = 1.0 / flat
    for k in range(1, terms + 1):
        order = 2 * k - 1
        coeff = BERN2K[k - 1] / math.factorial(2 * k)
        term = coeff * rising * np.exp(-(flat + order) * logM)
        z += term
        dz += term * (harm - logM)
        rising = rising * (flat + order) * (flat + order + 1)
        harm = harm + 1.0 / (flat + order) + 1.0 / (flat + order + 1)
    return z.reshape(s.shape), dz.reshape(s.shape)


def np_zeta_pair(s: np.ndarray, cutoff: int = 250,
                 terms: int = 12) -> tuple[np.ndarray, np.ndarray]:
    """Own vectorized EM continuation: returns (zeta(s), zeta'(s))."""
    s = np.asarray(s, dtype=complex)
    flat = s.ravel()
    z = np.zeros(flat.shape, dtype=complex)
    dz = np.zeros(flat.shape, dtype=complex)
    n = np.arange(1, cutoff, dtype=float)
    lg = np.log(n)
    chunk = 4000
    for lo in range(0, flat.size, chunk):
        sc = flat[lo:lo + chunk, None]
        P = np.exp(-sc * lg[None, :])
        z[lo:lo + chunk] = P.sum(axis=1)
        dz[lo:lo + chunk] = -(P * lg[None, :]).sum(axis=1)
    logM = math.log(cutoff)
    lead = np.exp((1.0 - flat) * logM) / (flat - 1.0)
    z += lead
    dz += lead * (-logM - 1.0 / (flat - 1.0))
    half = 0.5 * np.exp(-flat * logM)
    z += half
    dz += -logM * half
    rising = flat.copy()
    harm = 1.0 / flat
    for k in range(1, terms + 1):
        order = 2 * k - 1
        coeff = BERN2K[k - 1] / math.factorial(2 * k)
        term = coeff * rising * np.exp(-(flat + order) * logM)
        z += term
        dz += term * (harm - logM)
        rising = rising * (flat + order) * (flat + order + 1)
        harm = harm + 1.0 / (flat + order) + 1.0 / (flat + order + 1)
    return z.reshape(s.shape), dz.reshape(s.shape)


def np_digamma(z: np.ndarray) -> np.ndarray:
    """Own complex digamma: 32-step recurrence + asymptotic series."""
    z = np.asarray(z, dtype=complex)
    res = np.zeros_like(z)
    zz = z.copy()
    for _ in range(32):
        res -= 1.0 / zz
        zz = zz + 1.0
    inv = 1.0 / zz
    inv2 = inv * inv
    res += np.log(zz) - 0.5 * inv
    coeffs = (1.0 / 12, -1.0 / 120, 1.0 / 252, -1.0 / 240, 1.0 / 132,
              -691.0 / 32760, 1.0 / 12)
    p = inv2.copy()
    for c in coeffs:
        res -= c * p
        p = p * inv2
    return res


def np_xi_logderiv(z: np.ndarray, cutoff: int = 250) -> np.ndarray:
    """(xi'/xi)(1/2+z), own EM + own digamma, vectorized."""
    s = 0.5 + np.asarray(z, dtype=complex)
    zeta_v, dzeta_v = np_zeta_pair(s, cutoff=cutoff)
    return (1.0 / s + 1.0 / (s - 1.0) - 0.5 * math.log(math.pi)
            + 0.5 * np_digamma(s / 2.0) + dzeta_v / zeta_v)


# ------------------------------------------------------- Dirichlet L, Epstein
CHI20 = {1: 1, 3: 1, 7: 1, 9: 1, 11: -1, 13: -1, 17: -1, 19: -1}
CHI4 = {1: 1, 3: -1}
CHI5 = {1: 1, 2: -1, 3: -1, 4: 1}
SQRT20 = math.sqrt(20.0)
C20 = math.log(SQRT20 / (2.0 * math.pi))


def np_L_pair(s: np.ndarray, chi: dict[int, int],
              q: int) -> tuple[np.ndarray, np.ndarray]:
    s = np.asarray(s, dtype=complex)
    lq = math.log(q)
    qs = np.exp(-s * lq)
    L = np.zeros(s.shape, dtype=complex)
    dL = np.zeros(s.shape, dtype=complex)
    for a, cv in chi.items():
        hz, dhz = np_hurwitz_pair(s, a / q)
        L += cv * hz
        dL += cv * dhz
    return qs * L, qs * (dL - lq * L)


def np_epstein_pair(s: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Z_Q(s), Z_Q'(s) for Q = x^2 + 5y^2 via the genus decomposition
    Z_Q = zeta * L(chi_-20) + L(chi_-4) * L(chi_5) (disc -20, one
    class per genus)."""
    z, dz = np_zeta_pair(np.asarray(s, dtype=complex))
    L20, dL20 = np_L_pair(s, CHI20, 20)
    L4, dL4 = np_L_pair(s, CHI4, 4)
    L5, dL5 = np_L_pair(s, CHI5, 5)
    Z = z * L20 + L4 * L5
    dZ = dz * L20 + z * dL20 + dL4 * L5 + L4 * dL5
    return Z, dZ


def np_epstein_xilogderiv(z: np.ndarray) -> np.ndarray:
    """xi_Q'/xi_Q(1/2+z), xi_Q = s(s-1)(sqrt20/2pi)^s Gamma(s) Z_Q(s)."""
    s = 0.5 + np.asarray(z, dtype=complex)
    Z, dZ = np_epstein_pair(s)
    return (1.0 / s + 1.0 / (s - 1.0) + C20 + np_digamma(s) + dZ / Z)


def mp_epstein_pair(s, cutoff: int = 200, terms: int = 24):
    """mp-grade Z_Q, Z_Q' via the same genus decomposition (own EM)."""
    z, dz = dirichlet_logderivative(s, 250, 20)
    def mp_L(chi, q):
        lq = mp.log(q)
        qs = mp.e ** (-s * lq)
        L = mp.mpc(0)
        dL = mp.mpc(0)
        for a, cv in chi.items():
            hz, dhz = mp_hurwitz_pair(s, mp.mpf(a) / q, cutoff, terms)
            L += cv * hz
            dL += cv * dhz
        return qs * L, qs * (dL - lq * L)
    L20, dL20 = mp_L(CHI20, 20)
    L4, dL4 = mp_L(CHI4, 4)
    L5, dL5 = mp_L(CHI5, 5)
    Z = z * L20 + L4 * L5
    dZ = dz * L20 + z * dL20 + dL4 * L5 + L4 * dL5
    return Z, dZ


def epstein_lattice(qmax: int) -> list[tuple[int, int]]:
    cnt: dict[int, int] = {}
    b = 0
    while 5 * b * b <= qmax:
        aa = 0
        while aa * aa + 5 * b * b <= qmax:
            q = aa * aa + 5 * b * b
            if q >= 1:
                cnt[q] = cnt.get(q, 0) + (2 if aa else 1) * (2 if b else 1)
            aa += 1
        b += 1
    return sorted(cnt.items())


def epstein_xi_incgamma(s, qcap: int = 3000, dps: int = 50):
    """Round-117 audit representation of xi_Q (incomplete gamma)."""
    lat = epstein_lattice(qcap)
    with mp.workdps(dps):
        sv = mp.mpc(s)
        c = 2 * mp.pi / mp.sqrt(20)
        tot = -1 / sv - 1 / (1 - sv)
        for qv, cnt in lat:
            x = c * qv
            tot += cnt * (x ** (-sv) * mp.gammainc(sv, x, mp.inf)
                          + x ** (-(1 - sv)) * mp.gammainc(1 - sv, x,
                                                           mp.inf))
        return sv * (sv - 1) * tot


# ------------------------------------------------------- box contours
def scan_height(lo: float, hi: float, epstein: bool = False) -> float:
    """SOURCE-ONLY height: argmax |m(1/2 + i tau)| on [lo, hi]."""
    taus = np.arange(lo, hi, 0.02)
    if epstein:
        vals, _ = np_epstein_pair(0.5 + 1j * taus)
    else:
        vals, _ = np_zeta_pair(0.5 + 1j * taus, cutoff=250)
    return float(taus[int(np.argmax(np.abs(vals)))])


def box_nodes(T: float, c: float, dt: float,
              dx: float = 0.005) -> tuple[np.ndarray, np.ndarray]:
    tv = np.arange(-T, T + dt / 2, dt)
    wt = np.full(tv.shape, dt)
    wt[0] = wt[-1] = dt / 2
    xv = np.arange(-c, c + dx / 2, dx)
    wx = np.full(xv.shape, dx)
    wx[0] = wx[-1] = dx / 2
    nodes = np.concatenate([
        c + 1j * tv,
        xv[::-1] + 1j * T,
        -c + 1j * tv[::-1],
        xv - 1j * T,
    ])
    weights = np.concatenate([1j * wt, -wx, -1j * wt, wx])
    return nodes, weights


class BoxData:
    def __init__(self, T: float, dt: float, epstein: bool = False):
        self.T = T
        self.nodes, self.weights = box_nodes(T, BOX_C, dt)
        if epstein:
            self.F = np_epstein_xilogderiv(self.nodes)
        else:
            self.F = np_xi_logderiv(self.nodes, cutoff=250)

    def integrate(self, kernel_vals: np.ndarray) -> complex:
        return complex(np.sum(self.weights * self.F * kernel_vals)
                       / (2j * math.pi))

    def integrate_plain(self, kernel_vals: np.ndarray,
                        Fvals: np.ndarray) -> complex:
        return complex(np.sum(self.weights * Fvals * kernel_vals)
                       / (2j * math.pi))

    def zero_count(self) -> float:
        return float(np.real(np.sum(self.weights * self.F)
                             / (2j * math.pi)))


def omega_line(tau: np.ndarray, om: float) -> np.ndarray:
    return (om * om / (om * om + tau * tau)) ** 2


def omega_analytic(z: np.ndarray, om: float) -> np.ndarray:
    return (om * om / (om * om - z * z)) ** 2


def target_block(box: BoxData, sig: list[float], om: float) -> np.ndarray:
    n = len(sig)
    z = box.nodes
    w = omega_analytic(z, om)
    out = np.zeros((n, n))
    for j in range(n):
        for k in range(j, n):
            ker = w / ((sig[j] - z) * (sig[k] + z))
            val = box.integrate(ker)
            out[j, k] = out[k, j] = val.real
            if abs(val.imag) > 1e-6:
                out[j, k] = out[k, j] = float("nan")
    return out


# ------------------------------------------------------- coker machinery
ATOM_BETAS = (0.6, 0.8, 1.0, 13.0 / 12, 9.0 / 8, 1.2, 1.25, 4.0 / 3,
              1.5, 2.0, 2.5, 3.0)


def dip_windows(m_vals: np.ndarray, tau: np.ndarray, ell: float,
                mask: list[float] | None = None,
                mask_half: float = 0.0) -> list[tuple[float, float]]:
    """SOURCE-ONLY refinement windows: local minima of |m| below
    0.35 median, merged at 0.25, half-width min(3 ell, 1.0) --
    round-119 recipe verbatim.  Optional declared mask (Epstein
    variant B)."""
    a = np.abs(m_vals)
    med = float(np.median(a))
    idx = np.where((a[1:-1] < a[:-2]) & (a[1:-1] <= a[2:])
                   & (a[1:-1] < 0.35 * med))[0] + 1
    centers: list[float] = []
    for i in idx:
        t = float(tau[i])
        if mask and any(abs(t - mc) <= mask_half for mc in mask):
            continue
        if not centers or t - centers[-1] > 0.25:
            centers.append(t)
    half = min(3.0 * ell, 1.0)
    return [(c - half, c + half) for c in centers]


def coker_gram_big(m_vals: np.ndarray, node_vecs: np.ndarray,
                   tau: np.ndarray, dtau: float, ell: float,
                   spacing: float, om: float, refine: bool = True,
                   mask: list[float] | None = None,
                   mask_half: float = 0.0,
                   ridge: float = RIDGE) -> dict:
    """Chunk-accumulated round-119 coker quotient Gram:
    Ghat = (V^H V - C^H y) / (2 ell) with y from the ridge-normalized
    normal equations -- algebraically identical to the round-119
    explicit-residual path."""
    n_tau = len(tau)
    T = float(tau[-1])
    omega = omega_line(tau, om)
    om_mid = 0.5 * (omega[:-1] + omega[1:])
    hat_c = np.arange(-T + spacing, T - spacing / 2, spacing)
    cw = [hat_c]
    ww = [np.full(hat_c.shape, spacing)]
    windows: list[tuple[float, float]] = []
    if refine:
        windows = dip_windows(m_vals, tau, ell, mask, mask_half)
        sp = 2.0 * dtau
        for lo, hi in windows:
            cc = np.arange(lo, hi + sp / 2, sp)
            cw.append(cc)
            ww.append(np.full(cc.shape, sp))
    centers = np.concatenate(cw)
    widths = np.concatenate(ww)
    n_hat = len(centers)
    n_atom = 2 * len(ATOM_BETAS)
    ncol = n_hat + n_atom
    nv = node_vecs.shape[1]
    G = np.zeros((ncol, ncol), dtype=complex)
    C = np.zeros((ncol, nv), dtype=complex)
    VV = np.zeros((nv, nv), dtype=complex)
    sq_val = np.sqrt(omega * dtau)
    sq_der = ell * np.sqrt(om_mid * dtau) / dtau
    for i0 in range(0, n_tau - 1, CHUNK):
        i1 = min(i0 + CHUNK, n_tau - 1)
        hi = i1 + 1
        tt = tau[i0:hi]
        B = 1.0 - np.abs(tt[:, None] - centers[None, :]) / widths[None, :]
        np.clip(B, 0.0, None, out=B)
        A = np.empty((hi - i0, ncol), dtype=complex)
        A[:, :n_hat] = B
        col = n_hat
        for beta in ATOM_BETAS:
            A[:, col] = 1.0 / (beta + 1j * tt)
            A[:, col + 1] = 1.0 / (beta - 1j * tt)
            col += 2
        A *= m_vals[i0:hi, None]
        V = node_vecs[i0:hi]
        n_val = i1 - i0 if i1 < n_tau - 1 else hi - i0
        Ev = A[:n_val] * sq_val[i0:i0 + n_val, None]
        Ed = (A[1:] - A[:-1]) * sq_der[i0:i1, None]
        Vv = V[:n_val] * sq_val[i0:i0 + n_val, None]
        Vd = (V[1:] - V[:-1]) * sq_der[i0:i1, None]
        Eall = np.concatenate([Ev, Ed], axis=0)
        Vall = np.concatenate([Vv, Vd], axis=0)
        G += Eall.conj().T @ Eall
        C += Eall.conj().T @ Vall
        VV += Vall.conj().T @ Vall
        del A, B, Eall, Vall, Ev, Ed
    diag = np.real(np.diag(G)).copy()
    diag[diag <= 0] = 1.0
    D = np.sqrt(diag)
    G /= D[:, None]
    G /= D[None, :]
    Ch = C / D[:, None]
    idx = np.diag_indices(ncol)
    G[idx] += ridge
    y = np.linalg.solve(G, Ch)
    quot = VV - Ch.conj().T @ y
    range_tr = float(np.real(np.trace(Ch.conj().T @ y)))
    G[idx] += 9.0 * ridge
    y10 = np.linalg.solve(G, Ch)
    quot10 = VV - Ch.conj().T @ y10
    return {
        "Ghat": np.asarray(quot) / (2.0 * ell),
        "Ghat10": np.asarray(quot10) / (2.0 * ell),
        "VV": np.asarray(VV),
        "range_tr": range_tr,
        "ncol": ncol,
        "n_windows": len(windows),
        "windows": windows,
        "cond_span": float(D.max() / D.min()),
    }


def coker_resid(m_vals: np.ndarray, node_vecs: np.ndarray,
                tau: np.ndarray, dtau: float, ell: float,
                spacing: float, om: float,
                ridge: float = RIDGE) -> dict:
    """Explicit-residual coker (small problems): same recipe as
    coker_gram_big, returning the embedded residual rows for
    windowed inner products."""
    n_tau = len(tau)
    T = float(tau[-1])
    omega = omega_line(tau, om)
    om_mid = 0.5 * (omega[:-1] + omega[1:])
    hat_c = np.arange(-T + spacing, T - spacing / 2, spacing)
    cw = [hat_c]
    ww = [np.full(hat_c.shape, spacing)]
    windows = dip_windows(m_vals, tau, ell)
    sp = 2.0 * dtau
    for lo, hi in windows:
        cc = np.arange(lo, hi + sp / 2, sp)
        cw.append(cc)
        ww.append(np.full(cc.shape, sp))
    centers = np.concatenate(cw)
    widths = np.concatenate(ww)
    n_hat = len(centers)
    ncol = n_hat + 2 * len(ATOM_BETAS)
    A = np.empty((n_tau, ncol), dtype=complex)
    B = 1.0 - np.abs(tau[:, None] - centers[None, :]) / widths[None, :]
    np.clip(B, 0.0, None, out=B)
    A[:, :n_hat] = B
    del B
    col = n_hat
    for beta in ATOM_BETAS:
        A[:, col] = 1.0 / (beta + 1j * tau)
        A[:, col + 1] = 1.0 / (beta - 1j * tau)
        col += 2
    A *= m_vals[:, None]
    sq_val = np.sqrt(omega * dtau)
    sq_der = ell * np.sqrt(om_mid * dtau) / dtau
    E = np.concatenate([A * sq_val[:, None],
                        (A[1:] - A[:-1]) * sq_der[:, None]], axis=0)
    del A
    Vemb = np.concatenate([node_vecs * sq_val[:, None],
                           (node_vecs[1:] - node_vecs[:-1])
                           * sq_der[:, None]], axis=0)
    norms = np.sqrt(np.sum(np.abs(E) ** 2, axis=0))
    norms[norms == 0] = 1.0
    E /= norms[None, :]
    G = E.conj().T @ E
    G[np.diag_indices(ncol)] += ridge
    coef = np.linalg.solve(G, E.conj().T @ Vemb)
    resid = Vemb - E @ coef
    return {
        "Ghat": (resid.conj().T @ resid) / (2.0 * ell),
        "resid": resid,
        "n_tau": n_tau,
        "windows": windows,
    }


def window_weight(d: np.ndarray) -> np.ndarray:
    """cos^2 taper: 1 for d <= 0.5, 0 beyond 1.0."""
    d = np.asarray(d, dtype=float)
    out = np.where(d <= 0.5, 1.0,
                   np.where(d < 1.0, np.cos(np.pi * (d - 0.5)) ** 2, 0.0))
    return out


def windowed_gram(res: dict, tau: np.ndarray, ell: float,
                  g_center: float) -> np.ndarray:
    """Windowed H^1 Gram of the residuals at +-g_center / (2 ell)."""
    w_val = (window_weight(np.abs(tau - g_center))
             + window_weight(np.abs(tau + g_center)))
    mid = 0.5 * (tau[:-1] + tau[1:])
    w_der = (window_weight(np.abs(mid - g_center))
             + window_weight(np.abs(mid + g_center)))
    w_rows = np.sqrt(np.concatenate([w_val, w_der]))
    R = res["resid"] * w_rows[:, None]
    return (R.conj().T @ R) / (2.0 * ell)


def windowed_target(sig: list[float], zeros_upper: list[complex],
                    g_center: float, om: float) -> np.ndarray:
    """T_win from the refined zeros s in the upper small box (their
    conjugates added automatically)."""
    zs = []
    for s0 in zeros_upper:
        zs.append(complex(s0) - 0.5)
        zs.append(np.conj(complex(s0) - 0.5))
    zs = np.array(zs)
    wz = window_weight(np.abs(np.abs(np.imag(zs)) - g_center))
    n = len(sig)
    out = np.zeros((n, n))
    for j in range(n):
        for k in range(n):
            out[j, k] = float(np.real(np.sum(
                wz * omega_analytic(zs, om)
                / ((sig[j] - zs) * (sig[k] + zs)))))
    return out


def small_box_count(g: float, hw: float = 0.7, dt: float = 0.002,
                    epstein: bool = True) -> float:
    tv = np.arange(g - hw, g + hw + dt / 2, dt)
    wt = np.full(tv.shape, dt)
    wt[0] = wt[-1] = dt / 2
    dx = 0.005
    xv = np.arange(-BOX_C, BOX_C + dx / 2, dx)
    wx = np.full(xv.shape, dx)
    wx[0] = wx[-1] = dx / 2
    nodes = np.concatenate([
        BOX_C + 1j * tv,
        xv[::-1] + 1j * (g + hw),
        -BOX_C + 1j * tv[::-1],
        xv + 1j * (g - hw),
    ])
    wts = np.concatenate([1j * wt, -wx, -1j * wt, wx])
    if epstein:
        F = np_epstein_xilogderiv(nodes)
    else:
        F = np_xi_logderiv(nodes, cutoff=250)
    return float(np.real(np.sum(wts * F) / (2j * math.pi)))


def rel_defect(G: np.ndarray, Ttarget: np.ndarray) -> float:
    return float(np.linalg.norm(np.real(G) - Ttarget)
                 / np.linalg.norm(Ttarget))


def fit_scale(G: np.ndarray, Ttarget: np.ndarray) -> float:
    RG = np.real(G)
    return float(np.sum(RG * Ttarget) / np.sum(RG * RG))


# ------------------------------------------------------- discrete RK
def thomas_columns(dl: np.ndarray, dm: np.ndarray, du: np.ndarray,
                   idxs: list[int]) -> np.ndarray:
    """Tridiagonal solve for unit-vector RHS at idxs (Thomas)."""
    n = len(dm)
    k = len(idxs)
    B = np.zeros((n, k))
    for j, ix in enumerate(idxs):
        B[ix, j] = 1.0
    cp = np.zeros(n)
    dmw = dm.copy()
    X = B.copy()
    cp[0] = du[0] / dmw[0]
    X[0] /= dmw[0]
    for i in range(1, n):
        m_fac = dmw[i] - dl[i - 1] * cp[i - 1]
        if i < n - 1:
            cp[i] = du[i] / m_fac
        X[i] = (X[i] - dl[i - 1] * X[i - 1]) / m_fac
    for i in range(n - 2, -1, -1):
        X[i] -= cp[i] * X[i + 1]
    return X


def discrete_rk(tau: np.ndarray, dtau: float, ell: float, om: float,
                gam: list[float]) -> np.ndarray:
    """Discrete H^1_{ell,omega} reproducing kernel at points gam:
    K = M^{-1} restricted, M = the tridiagonal grid operator of
    int omega(|u|^2 + ell^2 |u'|^2)."""
    n = len(tau)
    omega = omega_line(tau, om)
    om_mid = 0.5 * (omega[:-1] + omega[1:])
    c_der = ell * ell / dtau
    dm = omega * dtau
    dm[:-1] += c_der * om_mid
    dm[1:] += c_der * om_mid
    off = -c_der * om_mid
    idxs = [int(round((g - tau[0]) / dtau)) for g in gam]
    X = thomas_columns(off, dm, off, idxs)
    return X[np.array(idxs)][:, :]


# ------------------------------------------------------- small sieve
def sieve_small(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def mangoldt_array(limit: int) -> np.ndarray:
    lam = np.zeros(limit + 1)
    for p in sieve_small(limit):
        q = p
        while q <= limit:
            lam[q] = math.log(p)
            q *= p
    return lam


def scramble_multiplier(tau: np.ndarray) -> np.ndarray:
    order = np.argsort([(n * GOLDEN) % 1.0 for n in range(1, X_SCR + 1)])
    log_perm = np.log(np.arange(1, X_SCR + 1, dtype=float)[order])
    wgt = np.arange(1, X_SCR + 1, dtype=float) ** (-0.5)
    out = np.zeros(tau.shape, dtype=complex)
    chunk = 8000
    for lo in range(0, len(tau), chunk):
        out[lo:lo + chunk] = (wgt[None, :] * np.exp(
            1j * np.outer(tau[lo:lo + chunk], log_perm))).sum(axis=1)
    return out


# ------------------------------------------------------- density model
def arch_density(tau: np.ndarray) -> np.ndarray:
    """(Re psi(1/4 + i tau/2)/2 - log(pi)/2)/pi -- the degenerate-orbit
    (mean) zero density, round-119 E7 welded to RvM at 7.4e-6."""
    return (np.real(np_digamma(0.25 + 0.5j * tau)) * 0.5
            - 0.5 * math.log(math.pi)) / math.pi


def mean_channel_matrix(sig: list[float], T: float,
                        om: float) -> np.ndarray:
    tt = np.arange(0.0, T, 0.01)
    db = arch_density(tt)
    w = omega_line(tt, om)
    n = len(sig)
    M = np.zeros((n, n))
    for j in range(n):
        for k in range(j, n):
            ker = 2.0 * np.real(1.0 / ((sig[j] - 1j * tt)
                                       * (sig[k] + 1j * tt)))
            M[j, k] = M[k, j] = float(np.trapezoid(db * w * ker, tt))
    return M


def deficit_model_matrix(sig: list[float], T: float,
                         om: float) -> np.ndarray:
    """Model of Pick_4 - T_omega: (1-omega) weight deficit on [0,T]
    plus the full |tau| > T tail, at the mean density."""
    tt = np.arange(0.0, T, 0.01)
    db = arch_density(tt)
    w = omega_line(tt, om)
    tl = np.exp(np.linspace(math.log(T), math.log(1e5), 4000))
    db_t = arch_density(tl)
    n = len(sig)
    M = np.zeros((n, n))
    for j in range(n):
        for k in range(j, n):
            ker = 2.0 * np.real(1.0 / ((sig[j] - 1j * tt)
                                       * (sig[k] + 1j * tt)))
            kert = 2.0 * np.real(1.0 / ((sig[j] - 1j * tl)
                                        * (sig[k] + 1j * tl)))
            v = float(np.trapezoid(db * (1.0 - w) * ker, tt))
            v += float(np.trapezoid(db_t * kert * tl, np.log(tl)))
            M[j, k] = M[k, j] = v
    return M


# ------------------------------------------------------- min-cut graph
INF = 10 ** 9

R116_NODES = {
    "UNCOND": "SOURCE",
    "STRIP": "UNC-CITED", "PT21": "UNC-CITED", "HSW22": "UNC-CITED",
    "GAMMA1": "UNC-CITED",
    "PASCAL": "UNC-ID", "FLOW": "UNC-ID", "GF2": "UNC-ID",
    "SOS": "UNC-ID", "LI": "UNC-ID", "EPIN": "UNC-ID",
    "SPLIT": "UNC-ID", "LAMBDA": "UNC-ID", "KICK": "UNC-ID",
    "FRED": "UNC-ID", "EXTDET": "UNC-ID", "TRACE-OP": "UNC-ID",
    "HFLOW": "UNC-ID", "JETREP": "UNC-ID", "WSUM": "UNC-ID",
    "WINDOW": "UNC-ID", "DIAGDET-ALG": "UNC-ID",
    "K74-THM": "UNC-THM", "FIXEDN-EVENTUAL": "UNC-THM",
    "A1-BOUND": "UNC-NEW", "A2-AMAX": "UNC-NEW",
    "A3-DIAG-ALLM": "UNC-NEW", "CONE": "UNC-NEW",
    "HAUS-CELLS-FIN": "UNC-THM",
    "PICK-FLOORS-FIN": "UNC-THM",
    "DIAG-BOUNDS-FIN": "UNC-NEW",
    "WEYL-PINS-MEAS": "MEAS",
    "SIGNPOS-MEAS": "MEAS",
    "FORMA-HYP": "HYP", "SV-HYP": "HYP", "R4-HYP": "HYP",
    "WEYL-HYP": "HYP",
    "RH": "TARGET", "Y01": "COND-RH", "W14": "COND-RH",
    "SIGNREG-ALL": "COND-RH",
}

R116_EDGES = [
    ("UNCOND", "STRIP", "DEF", INF), ("UNCOND", "PT21", "DEF", INF),
    ("UNCOND", "HSW22", "DEF", INF), ("UNCOND", "GAMMA1", "DEF", INF),
    ("UNCOND", "PASCAL", "DEF", INF), ("UNCOND", "FLOW", "DEF", INF),
    ("UNCOND", "GF2", "DEF", INF), ("UNCOND", "SOS", "DEF", INF),
    ("UNCOND", "LI", "DEF", INF), ("UNCOND", "EPIN", "DEF", INF),
    ("UNCOND", "SPLIT", "DEF", INF), ("UNCOND", "LAMBDA", "DEF", INF),
    ("UNCOND", "KICK", "DEF", INF), ("UNCOND", "FRED", "DEF", INF),
    ("UNCOND", "EXTDET", "DEF", INF),
    ("UNCOND", "TRACE-OP", "DEF", INF),
    ("UNCOND", "HFLOW", "DEF", INF), ("UNCOND", "JETREP", "DEF", INF),
    ("UNCOND", "WSUM", "DEF", INF), ("UNCOND", "WINDOW", "DEF", INF),
    ("UNCOND", "DIAGDET-ALG", "DEF", INF),
    ("UNCOND", "WEYL-PINS-MEAS", "MEAS", 1),
    ("UNCOND", "SIGNPOS-MEAS", "MEAS", 1),
    ("PT21", "K74-THM", "UNC", INF), ("HSW22", "K74-THM", "UNC", INF),
    ("STRIP", "A1-BOUND", "UNC", INF),
    ("GAMMA1", "A1-BOUND", "UNC", INF),
    ("WINDOW", "A2-AMAX", "UNC", INF),
    ("PT21", "A2-AMAX", "UNC", INF),
    ("A1-BOUND", "A2-AMAX", "UNC", INF),
    ("PT21", "A3-DIAG-ALLM", "UNC", INF),
    ("HSW22", "A3-DIAG-ALLM", "UNC", INF),
    ("K74-THM", "A3-DIAG-ALLM", "UNC", INF),
    ("A3-DIAG-ALLM", "CONE", "UNC", INF),
    ("K74-THM", "HAUS-CELLS-FIN", "UNC", INF),
    ("UNCOND", "HAUS-CELLS-FIN", "UNC", INF),
    ("UNCOND", "PICK-FLOORS-FIN", "UNC", INF),
    ("A2-AMAX", "DIAG-BOUNDS-FIN", "UNC", INF),
    ("HAUS-CELLS-FIN", "FORMA-HYP", "OMEGA-POS", 1),
    ("PICK-FLOORS-FIN", "SV-HYP", "OMEGA-POS", 1),
    ("DIAG-BOUNDS-FIN", "R4-HYP", "OMEGA-POS", 1),
    ("WEYL-PINS-MEAS", "WEYL-HYP", "OMEGA-POS-MEAS", 1),
    ("FORMA-HYP", "RH", "PROVEN-EQUIV", INF),
    ("SV-HYP", "RH", "KERNEL-CHECKED", INF),
    ("WEYL-HYP", "RH", "PROVEN-SUFF", INF),
    ("R4-HYP", "RH", "CANDIDATE", 1),
    ("RH", "Y01", "COND-RH", INF), ("Y01", "W14", "COND-RH", INF),
    ("Y01", "SIGNREG-ALL", "COND-RH", INF),
]


def max_flow(edges, source: str, sink: str):
    cap: dict[tuple[str, str], int] = {}
    adj: dict[str, set[str]] = {}
    for src, dst, _cls, capacity in edges:
        cap[(src, dst)] = cap.get((src, dst), 0) + capacity
        cap.setdefault((dst, src), 0)
        adj.setdefault(src, set()).add(dst)
        adj.setdefault(dst, set()).add(src)
    flow = 0
    while True:
        parent = {source: None}
        queue = [source]
        while queue and sink not in parent:
            node = queue.pop(0)
            for nxt in sorted(adj.get(node, ())):
                if nxt not in parent and cap.get((node, nxt), 0) > 0:
                    parent[nxt] = node
                    queue.append(nxt)
        if sink not in parent:
            break
        path = []
        cur = sink
        while parent[cur] is not None:
            path.append((parent[cur], cur))
            cur = parent[cur]
        bottleneck = min(cap[(u, v)] for u, v in path)
        for u, v in path:
            cap[(u, v)] -= bottleneck
            cap[(v, u)] += bottleneck
        flow += bottleneck
    reachable = {source}
    queue = [source]
    while queue:
        node = queue.pop(0)
        for nxt in sorted(adj.get(node, ())):
            if nxt not in reachable and cap.get((node, nxt), 0) > 0:
                reachable.add(nxt)
                queue.append(nxt)
    cut = [(src, dst, cls) for src, dst, cls, capacity in edges
           if src in reachable and dst not in reachable and capacity > 0]
    return flow, cut


def remodel_edges(edges, extended: bool, counterfactual: bool):
    """Replace PICK-FLOORS-FIN -> SV-HYP by the explicit omega gate;
    optionally add IRQG-MEAS through the same gate (extended) or as an
    independent omega edge (counterfactual)."""
    out = []
    for e in edges:
        if e[0] == "PICK-FLOORS-FIN" and e[1] == "SV-HYP":
            out.append(("PICK-FLOORS-FIN", "SV-OMEGA-GATE", "UNC", INF))
            out.append(("SV-OMEGA-GATE", "SV-HYP", "OMEGA-POS", 1))
        else:
            out.append(e)
    if extended:
        out.append(("PICK-FLOORS-FIN", "IRQG-MEAS", "MEAS-DICT", INF))
        if counterfactual:
            out.append(("IRQG-MEAS", "SV-HYP", "OMEGA-POS-MEAS", 1))
        else:
            out.append(("IRQG-MEAS", "SV-OMEGA-GATE", "MEAS-DICT", INF))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("irwall_probe  PRIME.STAGE1.IRWALL.01%s"
          % ("  [SMOKE -- not the run of record]" if SMOKE else ""))
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM. EXPLORATION ONLY. An IR-stable identity for a")
    print("truncated block is not RH; the all-h/all-N quantifier stays open.")
    print("=" * 78)

    # ============================================================ A
    section("A. INSTRUMENTS: firewall, wards, pins, floors, c* packet")

    fw_ok, fw_detail = firewall_audit()
    check("A1 source-only AST firewall", fw_ok, fw_detail)

    ok_ep, miss_ep = ward("ep_log", [
        "N=1  lo=4.5917135e-2", "N=2  lo=9.0288701e-6",
        "N=3  lo=2.3643695e-10", "CERTIFIED POSITIVE"])
    ok_s4, miss_s4 = ward("s4_log", [
        "N=4  lo=8.278338e-15", "hi=1.3840906e-14", "CERTIFIED POSITIVE"])
    ok_r119, miss_r119 = ward("r119", [
        "defect vs T_omega = 0.0033",
        "fitted scale vs 2*ell theory: 1.0033",
        "Omega=25 defect 0.0033 | Omega=40 defect 0.0087",
        "heights: T*=63.06  T2=126.00",
        "lambda_min(Ghat_4)=8.702e-14"])
    ok_r117, miss_r117 = ward("r117src", [
        "WITNESS_R102 = complex(0.69692705, 36.37406369)",
        "def epstein_lattice(qmax: int)"])
    ok_r116, miss_r116 = ward("r116src", [
        '("PICK-FLOORS-FIN", "SV-HYP", "OMEGA-POS", 1)',
        '("WEYL-PINS-MEAS", "WEYL-HYP", "OMEGA-POS-MEAS", 1)'])
    ok_s1, miss_s1 = ward("stage1", [
        "BRK-A1-CROSSTERMS      direct-sum glue supplies ZERO"])
    check("A2 wards (floors / r119 baseline / r117 / r116 / r115)",
          ok_ep and ok_s4 and ok_r119 and ok_r117 and ok_r116 and ok_s1,
          "ep=%s s4=%s r119=%s r117=%s r116=%s stage1=%s"
          % (miss_ep or "ok", miss_s4 or "ok", miss_r119 or "ok",
             miss_r117 or "ok", miss_r116 or "ok", miss_s1 or "ok"))

    mp.mp.dps = DPS
    pin_sigmas = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, PIN_COUNT + 1)]
    p_pins = [pin_reference(sig) for sig in pin_sigmas]
    p_ref = [h_pole(sig) + h_gamma(sig)
             + zeta_logderiv(mp.mpf("0.5") + sig, 128, 32)
             for sig in pin_sigmas]
    em_dev = max(abs(a - b) for a, b in zip(p_pins, p_ref))
    floors = []
    for n in range(1, PIN_COUNT + 1):
        E = mp.eigsy(pick_matrix(p_pins[:n], pin_sigmas[:n]),
                     eigvals_only=True)
        floors.append(E[0])
    in_iv = all(CERTIFIED[n][0] <= float(floors[n - 1]) <= CERTIFIED[n][1]
                for n in range(1, 5))
    check("A3 EM stability + certified floors N<=4",
          em_dev < mp.mpf("1e-70") and in_iv,
          "EM dev=%s; lambda_min(4)=%s in [%.3e, %.3e]"
          % (fmt(em_dev, 4), fmt(floors[3], 6), *CERTIFIED[4]))

    E4, Q4 = mp.eigsy(pick_matrix(p_pins[:4], pin_sigmas[:4]))
    cstar = np.array([float(Q4[i, 0]) for i in range(4)])
    lam4 = float(E4[0])
    P4_mp = pick_matrix(p_pins[:4], pin_sigmas[:4])
    P4 = np.array([[float(P4_mp[j, k]) for k in range(4)]
                   for j in range(4)])
    check("A4 c* packet warded (lambda_4)",
          abs(lam4 / FROZEN_LAM4 - 1) < 0.01,
          "lambda_4 = %.4e vs frozen %.3e; c* = (%s)"
          % (lam4, FROZEN_LAM4,
             ", ".join("%+.4f" % c for c in cstar)))
    sig4 = [float(s) for s in pin_sigmas]

    # ============================================================ B
    section("B. THE ISOMETRY DATUM (T2): sympy exact + discrete RK")

    tau_s, tp_s, ell_s, alpha_s = sp.symbols(
        "tau tau_p ell alpha", positive=True)
    K_expr = sp.exp(-(tau_s - tp_s) / ell_s) / (2 * ell_s)
    ode_res = sp.simplify(K_expr - ell_s ** 2 * sp.diff(K_expr, tau_s, 2))
    jump = sp.simplify(
        -ell_s ** 2 * (sp.diff(K_expr, tau_s).subs(tau_s, tp_s)
                       - sp.diff(sp.exp((tau_s - tp_s) / ell_s)
                                 / (2 * ell_s), tau_s).subs(tau_s, tp_s)))
    check("B1 sympy: H^1_ell RK = e^{-|d|/ell}/(2 ell) exact",
          ode_res == 0 and sp.simplify(jump - 1) == 0,
          "(1 - ell^2 d^2)K = %s off-diagonal; derivative jump = %s"
          % (ode_res, jump))

    lam_p = -alpha_s + sp.sqrt(alpha_s ** 2 + 1 / ell_s ** 2)
    lam_m = -alpha_s - sp.sqrt(alpha_s ** 2 + 1 / ell_s ** 2)
    omega_w = sp.exp(2 * alpha_s * tau_s)
    up = sp.exp(lam_m * tau_s)      # decays as tau -> +inf (with weight)
    um = sp.exp(lam_p * tau_s)      # decays as tau -> -inf
    wron = sp.simplify(-ell_s ** 2 * omega_w
                       * (sp.diff(up, tau_s) * um - up * sp.diff(um, tau_s)))
    K_diag = sp.simplify(up * um / wron)
    K_pred = 1 / (2 * ell_s * omega_w * sp.sqrt(1 + alpha_s ** 2
                                                * ell_s ** 2))
    check("B2 sympy: exp-weight RK diagonal (WKB law exact)",
          sp.simplify(K_diag - K_pred) == 0,
          "K(g,g) = 1/(2 ell omega(g) sqrt(1 + alpha^2 ell^2)): the "
          "normalization correction is <= ell^2/(2 Omega^2) per rung")

    # heights (source-only) for all rungs
    rungs = []
    for wlo, whi in RUNG_WINDOWS:
        rungs.append(scan_height(wlo, whi))
    T0 = rungs[0]
    check("B3 rung heights source-only (baseline reproduces r119)",
          abs(T0 - BASE_TSTAR) <= 0.05 and abs(rungs[2] - BASE_T2) <= 0.05,
          "T = %s (T0 vs frozen %.2f; rung2 vs frozen %.2f)"
          % (["%.2f" % t for t in rungs], BASE_TSTAR, BASE_T2))
    log0 = math.log(T0 / (2 * math.pi))
    sched = []
    for Tr in rungs:
        ellr = ELL0 * log0 / math.log(Tr / (2 * math.pi))
        sched.append((Tr, OMEGA0 * Tr / T0, ellr, DTAU_RATIO * ellr))
    if SMOKE:
        sched = sched[:2]
        rungs = rungs[:2]

    # discrete RK at R0: the keystone normalization measurement
    Tr0, Om0, ell_r0, _ = sched[0]
    rk_tab = []
    dip_cs_fine: list[float] = []
    for ratio in RICH_RATIOS:
        dt_r = ratio * ell_r0
        tau_g = np.arange(-Tr0, Tr0 + dt_r / 2, dt_r)
        m_g = np_zeta_pair(0.5 - 1j * tau_g, cutoff=250)[0]
        wins = dip_windows(m_g, tau_g, ell_r0)
        cs = [0.5 * (lo + hi) for lo, hi in wins
              if abs(0.5 * (lo + hi)) < Tr0 - 3.0]
        K = discrete_rk(tau_g, dt_r, ell_r0, Om0, cs)
        vals = 2.0 * ell_r0 * omega_line(np.array(cs), Om0) * np.diag(K)
        rk_tab.append((ratio, float(np.mean(vals)), float(np.max(
            np.abs(vals - 1.0))), cs, K))
        if ratio == RICH_RATIOS[-1]:
            dip_cs_fine = cs
        print("    dtau/ell=%.5f  <2 ell omega K_ii> = %.6f  "
              "max|.-1| = %.4f  (%d dips)"
              % (ratio, rk_tab[-1][1], rk_tab[-1][2], len(cs)))
    m1, m2, m3 = rk_tab[0][1], rk_tab[1][1], rk_tab[2][1]
    denom = (m1 - m2) - (m2 - m3)
    rk_extrap = m3 - (m2 - m3) ** 2 / denom if abs(denom) > 1e-15 else m3
    check("B4 RK normalization -> 1 on the grid ladder (Richardson)",
          abs(rk_extrap - 1.0) <= 5e-3,
          "2 ell omega K_ii: %.5f / %.5f / %.5f -> extrapolated %.5f "
          "(gate |.-1| <= 5e-3): the fitted r119 1.0033 is grid, the "
          "continuum normalization is the theory value" % (m1, m2, m3,
                                                           rk_extrap))

    ratio_f, _, _, cs_f, K_f = rk_tab[-1]
    off_ok = True
    off_detail = "no adjacent pair below gap 3"
    wkb0 = ell_r0 ** 2 / (2.0 * Om0 ** 2)
    pairs_checked = 0
    for i in range(len(cs_f) - 1):
        gap = cs_f[i + 1] - cs_f[i]
        if gap <= 3.0:
            meas = abs(K_f[i, i + 1]) / math.sqrt(abs(K_f[i, i])
                                                  * abs(K_f[i + 1, i + 1]))
            pred = math.exp(-gap / ell_r0)
            pairs_checked += 1
            if not (0.5 <= meas / pred <= 2.0):
                off_ok = False
                off_detail = ("gap %.2f: measured %.4f vs e^{-gap/ell} "
                              "%.4f" % (gap, meas, pred))
    if off_ok and pairs_checked:
        off_detail = ("%d adjacent pairs within factor 2 of the "
                      "e^{-gap/ell} law" % pairs_checked)
    check("B5 RK cross-talk follows the exponential law", off_ok,
          off_detail + "; WKB weight correction this rung <= %.1e" % wkb0)
    print("    T2(c) typed CITED: exact orthonormal zero evaluations = "
          "de Branges")
    print("    sampling at phase points (Antezana--Marzo--Olsen 2016 "
          "Thm 1.1);")
    print("    xi(1/2 - i z) a structure function <=> RH (Lagarias, dB "
          "theory):")
    print("    the canonical completion datum IS RH -- obstruction of "
          "proven class,")
    print("    cited, not a probe theorem.  H^1_{ell,omega} is its "
          "mollified proxy.")

    # ============================================================ C
    section("C. T1 -- THE IR LADDER (coupled schedule)")

    boxes = []
    weld_hi = 0.0
    for r, (Tr, Omr, ellr, dtr) in enumerate(sched):
        box = BoxData(Tr, BOX_DT)
        boxes.append(box)
        spots = [BOX_C + 1j * (0.98 * Tr), -BOX_C - 1j * (0.61 * Tr)]
        Fnp = np_xi_logderiv(np.array(spots), cutoff=250)
        with mp.workdps(50):
            for i, spz in enumerate(spots):
                sv = mp.mpc(0.5 + spz.real, spz.imag)
                val, dval = dirichlet_logderivative(sv, 400, 20)
                ref = (1 / sv + 1 / (sv - 1) - mp.log(mp.pi) / 2
                       + mp.digamma(sv / 2) / 2 + dval / val)
                weld_hi = max(weld_hi, float(abs(complex(Fnp[i])
                                                 - complex(ref))
                                             / abs(complex(ref))))
    check("C1 high-T EM welds at every rung box", weld_hi < 1e-9,
          "max rel dev np(M=250) vs mp(M=400, dps 50) = %.2e" % weld_hi)

    counts = [b.zero_count() for b in boxes]
    int_dev = max(abs(cv - round(cv)) for cv in counts)
    check("C2 zero-count integrals integer at every rung",
          int_dev < 2e-4,
          "counts=%s max dist=%.1e"
          % (["%.4f" % cv for cv in counts], int_dev))

    dual_dev = 0.0
    for r in range(min(2, len(sched))):
        Tb = sched[r][0]
        bh = BoxData(Tb, 2 * BOX_DT)
        Tg = target_block(boxes[r], sig4, sched[r][1])
        Th = target_block(bh, sig4, sched[r][1])
        dual_dev = max(dual_dev, float(np.max(np.abs(Tg - Th))))
    box_bar = max(dual_dev, 1e-9)
    check("C3 box dual-resolution stability (rungs 0-1)",
          dual_dev < 1e-6, "max entry dev %.2e (declared box bar)" %
          dual_dev)

    targets = [target_block(boxes[r], sig4, sched[r][1])
               for r in range(len(sched))]
    tpsd_ok = True
    for r, Tg in enumerate(targets):
        evl = np.linalg.eigvalsh(Tg)[0]
        if evl < -1e-6 * np.max(np.abs(Tg)):
            tpsd_ok = False
    check("C4 T_omega PSD at every rung", tpsd_ok,
          "lambda_min(T)/max|T| >= -1e-6 at all rungs "
          "(truncated zero Grams)")

    # the ladder
    ladder = []
    lam_arr = mangoldt_array(3000)
    for r, (Tr, Omr, ellr, dtr) in enumerate(sched):
        t_r0 = time.time()
        tau_r = np.arange(-Tr, Tr + dtr / 2, dtr)
        s_line = 0.5 - 1j * tau_r
        m_r = np_zeta_pair(s_line, cutoff=250)[0]
        nodes_r = np.stack([1.0 / (s + 1j * tau_r) for s in sig4], axis=1)
        res = coker_gram_big(m_r, nodes_r, tau_r, dtr, ellr, 0.5 * ellr,
                             Omr)
        d_r = rel_defect(res["Ghat"], targets[r])
        d_r10 = rel_defect(res["Ghat10"], targets[r])
        sfit_r = fit_scale(res["Ghat"], targets[r])
        evG = np.linalg.eigvalsh(np.real(res["Ghat"]))
        trG = float(np.trace(np.real(res["Ghat"])))
        # controls through the same lift, every rung
        m_sm = 1.0 / (s_line - 1.0)
        res_sm = coker_gram_big(m_sm, nodes_r, tau_r, dtr, ellr,
                                0.5 * ellr, Omr)
        tr_sm = float(np.trace(np.real(res_sm["Ghat"]))
                      / np.trace(targets[r]))
        m_sc = scramble_multiplier(tau_r)
        res_sc = coker_gram_big(m_sc, nodes_r, tau_r, dtr, ellr,
                                0.5 * ellr, Omr)
        d_sc = rel_defect(res_sc["Ghat"], targets[r])
        ladder.append({
            "T": Tr, "Om": Omr, "ell": ellr, "dt": dtr,
            "defect": d_r, "defect10": d_r10, "sfit": sfit_r,
            "lam_min": float(evG[0]), "trG": trG,
            "trT": float(np.trace(targets[r])),
            "trVV": float(np.real(np.trace(res["VV"]))),
            "range_tr": res["range_tr"], "ncol": res["ncol"],
            "nwin": res["n_windows"], "cond": res["cond_span"],
            "tr_sm": tr_sm, "d_sc": d_sc,
            "Ghat": res["Ghat"], "m": m_r, "tau": tau_r,
            "nodes": nodes_r,
        })
        print("    rung %d: T=%7.2f Om=%6.2f ell=%.3f dtau=%.4f | "
              "defect %.4f  sfit %.4f  lam_min %+.2e" %
              (r, Tr, Omr, ellr, dtr, d_r, sfit_r, float(evG[0])))
        print("            trV=%.4f range=%.4f quot=%.4f trT=%.4f "
              "cols=%d win=%d ridge10x-dev %.1f%% | smooth %.1e "
              "scram %.1f  [%.0f s]"
              % (ladder[-1]["trVV"], ladder[-1]["range_tr"],
                 2 * ellr * ladder[-1]["trG"] / (2 * ellr),
                 ladder[-1]["trT"], res["ncol"], res["n_windows"],
                 100 * abs(d_r10 - d_r) / d_r, tr_sm, d_sc,
                 time.time() - t_r0))

    d0 = ladder[0]["defect"]
    check("C5 baseline rung reproduces round 119 (frozen)",
          abs(d0 / BASE_DEFECT - 1) <= 0.15
          and abs(ladder[0]["sfit"] - BASE_SFIT) <= 0.005,
          "defect %.4f vs frozen %.4f; sfit %.4f vs frozen %.4f"
          % (d0, BASE_DEFECT, ladder[0]["sfit"], BASE_SFIT))

    dmax = max(l["defect"] for l in ladder)
    check("C6 defect <= bar at every rung", dmax <= DEFECT_BAR,
          "max defect on ladder = %.4f <= %.2f" % (dmax, DEFECT_BAR))
    dtop = ladder[-1]["defect"]
    carries = dtop <= CARRY_FACTOR * d0
    check("C7 IR carry gate: top rung <= 3x baseline", carries,
          "defect ladder %s (top/base = %.2f)"
          % ("/".join("%.4f" % l["defect"] for l in ladder), dtop / d0))
    check("C8 RK normalization within bar at every rung",
          all(abs(l["sfit"] - 1) <= NORM_BAR for l in ladder),
          "sfit ladder %s"
          % "/".join("%.4f" % l["sfit"] for l in ladder))
    check("C9 quotient PSD exact at every rung",
          all(l["lam_min"] > -1e-12 * max(l["trG"], 1e-30)
              for l in ladder),
          "lam_min ladder %s"
          % "/".join("%+.1e" % l["lam_min"] for l in ladder))
    check("C10 smooth control empties at every rung",
          all(l["tr_sm"] < 1e-2 for l in ladder),
          "coker trace ratios %s"
          % "/".join("%.1e" % l["tr_sm"] for l in ladder))
    check("C11 scramble control dies at every rung",
          all(l["d_sc"] > 0.5 for l in ladder),
          "scramble defects %s"
          % "/".join("%.1f" % l["d_sc"] for l in ladder))
    check("C12 ridge-conditioning audit at every rung",
          all(abs(l["defect10"] - l["defect"]) <= 0.2 * l["defect"]
              for l in ladder),
          "10x-ridge defect shifts %s (bar 20%%)"
          % "/".join("%.1f%%" % (100 * abs(l["defect10"] - l["defect"])
                                 / l["defect"]) for l in ladder))
    degen = (ladder[-1]["trT"] / max(np.linalg.eigvalsh(
        targets[len(ladder) - 1])[0], 1e-30)
        > 100 * ladder[0]["trT"] / max(np.linalg.eigvalsh(
            targets[0])[0], 1e-30))

    # ============================================================ D
    section("D. IR DIAGNOSTICS: the completion floor, counterfactuals, "
            "P4 convergence")

    floor_configs = (
        (ELL0, 0.0375, 0.5), (ELL0, 0.01875, 0.5), (ELL0, 0.009375, 0.5),
        (ELL0, 0.01875, 0.25), (ELL0, 0.01875, 0.125),
        (ELL0, 0.009375, 0.25), (ELL0, 0.009375, 0.125),
        (0.4, 0.01875, 0.5), (0.4, 0.01875, 0.25), (0.4, 0.01875, 0.125),
        (0.4, 0.009375, 0.5), (0.4, 0.009375, 0.25),
        (0.4, 0.009375, 0.125),
    )
    floor = {}
    for ellf, ratio, spf in floor_configs:
        if (abs(ellf - sched[0][2]) < 1e-12
                and abs(ratio - DTAU_RATIO) < 1e-12 and spf == 0.5):
            l0 = ladder[0]
            qg = float(cstar @ np.real(l0["Ghat"]) @ cstar)
            floor[(ellf, ratio, spf)] = (l0["defect"], l0["sfit"], qg)
        else:
            dt_r = ratio * ellf
            tau_g = np.arange(-sched[0][0], sched[0][0] + dt_r / 2, dt_r)
            m_g = np_zeta_pair(0.5 - 1j * tau_g, cutoff=250)[0]
            nodes_g = np.stack([1.0 / (s + 1j * tau_g) for s in sig4],
                               axis=1)
            rr = coker_gram_big(m_g, nodes_g, tau_g, dt_r, ellf,
                                spf * ellf, sched[0][1])
            qg = float(cstar @ np.real(rr["Ghat"]) @ cstar)
            floor[(ellf, ratio, spf)] = (
                rel_defect(rr["Ghat"], targets[0]),
                fit_scale(rr["Ghat"], targets[0]), qg)
        dd, ss, qg = floor[(ellf, ratio, spf)]
        print("    R0 ell=%.2f dtau/ell=%.5f sp/ell=%.3f: defect %.5f "
              "sfit %.5f q_G(c*) %+.3e" % (ellf, ratio, spf, dd, ss, qg))
    d_c5 = floor[(ELL0, 0.009375, 0.5)][0]
    d_c25 = floor[(ELL0, 0.009375, 0.25)][0]
    d_c125 = floor[(ELL0, 0.009375, 0.125)][0]
    dstar08, sstar08 = d_c125, floor[(ELL0, 0.009375, 0.125)][1]
    dstar04, sstar04 = floor[(0.4, 0.009375, 0.125)][:2]
    check("D1 completion floor: joint refinement saturates (ell=0.8)",
          abs(d_c125 - d_c25) <= 0.6 * abs(d_c25 - d_c5),
          "fully-refined defect converges: %.5f -> %.5f -> %.5f "
          "(increment ratio %.2f): delta*(0.8) = %.5f is a FINITE "
          "ell-window floor -- the r119 'pure grid' reading is "
          "AMENDED (their gates stand; the operating point sat near "
          "an under-refinement crossing)"
          % (d_c5, d_c25, d_c125,
             abs(d_c125 - d_c25) / max(abs(d_c25 - d_c5), 1e-12),
             dstar08))
    check("D2 the floor collapses on the ell axis",
          dstar04 <= 0.35 * dstar08,
          "delta*(0.4) = %.5f <= 0.35 x delta*(0.8) = 0.35 x %.5f: "
          "the exact identity needs the joint limit ell -> 0 -- the "
          "measured law is >= ~5x per halving (one halving certified "
          "here; extrapolation typed MEASURED, not proven)"
          % (dstar04, dstar08))
    check("D3 RK fit brackets 1 and tightens on the ell axis",
          (sstar08 - 1.0) * (sstar04 - 1.0) < 0
          and abs(sstar04 - 1.0) <= 0.35 * abs(sstar08 - 1.0),
          "s*(0.8) = %.5f (above), s*(0.4) = %.5f (below): the "
          "normalization brackets the theory value 1 and tightens "
          "with ell; WKB weight bound this rung %.1e" %
          (sstar08, sstar04, wkb0))

    # cross-talk-corrected prediction from the measured discrete RK
    Vz = np.stack([1.0 / (np.array(dip_cs_fine) * 1j + s)
                   for s in sig4], axis=0)
    Kz = 2.0 * sched[0][2] * K_f
    T_pred = np.real(Vz @ np.linalg.solve(Kz, Vz.conj().T))
    d_pred_vs_T = rel_defect(T_pred, targets[0])
    print("    T_pred(discrete-RK dips) vs T_omega: defect %.4f "
          "(same class as delta*(0.8) = %.4f)" % (d_pred_vs_T, dstar08))
    check("D4 RK-geometry prediction reproduces the target",
          d_pred_vs_T <= 0.02,
          "the measured discrete-RK zero-evaluation block reproduces "
          "T_omega at %.4f: dip-emergent evaluations near-orthonormal "
          "(diag law B4, off-diag law B5); the residual is the same "
          "ell-window class as the D1 floor" % d_pred_vs_T)

    # counterfactual 1: the r119 Omega=40 wall entry, reproduced + rescaled
    l0 = ladder[0]
    T40 = target_block(boxes[0], sig4, 40.0)
    r40 = coker_gram_big(l0["m"], l0["nodes"], l0["tau"], sched[0][3],
                         sched[0][2], 0.5 * sched[0][2], 40.0)
    d40 = rel_defect(r40["Ghat"], T40)
    check("D5 r119 Omega-40-at-T0 wall entry reproduced",
          abs(d40 / BASE_OM40 - 1) <= 0.2,
          "defect %.4f vs frozen %.4f: the round-119 'IR wall' entry"
          % (d40, BASE_OM40))
    ir2 = min(2, len(ladder) - 1)
    l2 = ladder[ir2]
    Om_hi = sched[ir2][1] * (40.0 / OMEGA0)
    Thi = target_block(boxes[ir2], sig4, Om_hi)
    rhi = coker_gram_big(l2["m"], l2["nodes"], l2["tau"], sched[ir2][3],
                         sched[ir2][2], 0.5 * sched[ir2][2], Om_hi)
    dhi = rel_defect(rhi["Ghat"], Thi)
    ratio0 = d40 / d0
    ratio2 = dhi / l2["defect"]
    check("D6 the Omega/T ratio penalty is stationary in T (edge law)",
          ratio2 <= 1.6 * ratio0 and dhi <= DEFECT_BAR,
          "Omega-ratio 0.634 penalty: x%.2f at T0 -> x%.2f at rung %d "
          "(both defects %.4f/%.4f <= bar): the r119 Omega-40 "
          "degradation is the Omega/T EDGE law, not a divergence -- "
          "the wall entry closes under the coupled schedule"
          % (ratio0, ratio2, ir2, d40, dhi))

    # counterfactual 2: schedule off (fixed ell) at rung ir2
    tau_c2 = np.arange(-sched[ir2][0], sched[ir2][0] + 0.015 / 2, 0.015)
    m_c2 = np_zeta_pair(0.5 - 1j * tau_c2, cutoff=250)[0]
    nodes_c2 = np.stack([1.0 / (s + 1j * tau_c2) for s in sig4], axis=1)
    rc2 = coker_gram_big(m_c2, nodes_c2, tau_c2, 0.015, ELL0,
                         0.5 * ELL0, sched[ir2][1])
    d_c2 = rel_defect(rc2["Ghat"], targets[ir2])
    print("    schedule-off counterfactual at rung %d: fixed ell=%.1f "
          "defect %.4f vs scheduled %.4f (INFO: measures the ell "
          "schedule's necessity)" % (ir2, ELL0, d_c2, l2["defect"]))

    # P4 convergence of the target (the certified-floor object)
    p4_ok = True
    prev = None
    for r in range(len(ladder)):
        diff = P4 - targets[r]
        model = deficit_model_matrix(sig4, sched[r][0], sched[r][1])
        rel = float(np.linalg.norm(diff - model) / np.linalg.norm(model))
        dist = float(np.linalg.norm(diff) / np.linalg.norm(P4))
        print("    rung %d: |P4 - T_omega|/|P4| = %.4f  deficit-model "
              "rel dev = %.3f" % (r, dist, rel))
        if rel > P4_MODEL_BAR or (prev is not None and dist >= prev):
            p4_ok = False
        prev = dist
    check("C13 target converges to Pick_4 at the modeled mean-density "
          "rate", p4_ok,
          "deficit == (1-omega) weight + tail at the arch density "
          "(<= %.0f%% Frobenius), distance monotone down the ladder: "
          "the IR path ends at the certified floors' object"
          % (100 * P4_MODEL_BAR))

    # perturbation-response trap gate (round-118 amendment 1)
    pert_ok = True
    pert_detail = []
    for rr_ in {0, ir2}:
        lr = ladder[rr_]
        m_p = lr["m"] * (1.0 + 1e-9 * np.cos(0.7 * lr["tau"]))
        rp = coker_gram_big(m_p, lr["nodes"], lr["tau"], sched[rr_][3],
                            sched[rr_][2], 0.5 * sched[rr_][2],
                            sched[rr_][1])
        dp = rel_defect(rp["Ghat"], targets[rr_])
        shift = abs(dp - lr["defect"])
        pert_detail.append("rung %d: %.2e" % (rr_, shift))
        if not (1e-15 < shift < 1e-4):
            pert_ok = False
    check("D7 perturbation response nonzero and bounded (dps trap)",
          pert_ok,
          "defect shifts under 1e-9 multiplier perturbation: %s "
          "(an exactly-zero response is the round-118 red flag)"
          % "; ".join(pert_detail))

    # ============================================================ E
    section("E. T3 -- THE OSCILLATION CHANNEL")

    osc_rows = []
    for r in range(len(ladder)):
        Mm = mean_channel_matrix(sig4, sched[r][0], sched[r][1])
        Osc = targets[r] - Mm
        err = float(np.linalg.norm(np.real(ladder[r]["Ghat"])
                                   - targets[r]))
        dig_m = math.log10(float(np.linalg.norm(Osc)) / err)
        # packet channels
        zb = boxes[r].nodes
        wb = omega_analytic(zb, sched[r][1])
        fj = sum(cstar[j] / (sig4[j] - zb) for j in range(4))
        fk = sum(cstar[k] / (sig4[k] + zb) for k in range(4))
        q_T = boxes[r].integrate(wb * fj * fk).real
        tt = np.arange(0.0, sched[r][0], 0.01)
        g_c = np.zeros(tt.shape, dtype=complex)
        for j in range(4):
            g_c += cstar[j] / (sig4[j] - 1j * tt)
        q_mean = 2.0 * float(np.trapezoid(
            arch_density(tt) * omega_line(tt, sched[r][1])
            * np.abs(g_c) ** 2, tt))
        q_G = float(cstar @ np.real(ladder[r]["Ghat"]) @ cstar)
        osc_rows.append((r, float(np.linalg.norm(Osc)), dig_m, q_T,
                         q_mean, q_G))
        print("    rung %d: |Osc|_F=%.4f  digits_matrix=%.2f | packet: "
              "q_T=%+.2e q_mean=%+.4e q_G=%+.2e"
              % (r, float(np.linalg.norm(Osc)), dig_m, q_T, q_mean, q_G))
    check("E1 oscillation channel carried at matrix level (all rungs)",
          all(row[2] >= 1.0 for row in osc_rows),
          "digits_matrix = log10(|T_omega - M_mean|_F / |Ghat - "
          "T_omega|_F) = %s: the quotient Gram reproduces the "
          "oscillation structure beyond mean density at every rung"
          % "/".join("%.2f" % row[2] for row in osc_rows))

    qg1 = floor[(ELL0, 0.0375, 0.5)][2]
    qg2 = floor[(ELL0, 0.01875, 0.5)][2]
    qg3 = floor[(ELL0, 0.009375, 0.5)][2]
    den_q = (qg1 - qg2) - (qg2 - qg3)
    qg_inf = qg3 - (qg2 - qg3) ** 2 / den_q if abs(den_q) > 1e-18 else qg3
    q_T0 = osc_rows[0][3]
    q_mean0 = osc_rows[0][4]
    pkt_bar = 5.0 * box_bar * float(np.sum(np.abs(np.outer(cstar,
                                                           cstar))))
    dig_pkt = math.log10(abs(q_mean0)
                         / max(abs(qg_inf - q_T0), pkt_bar))
    dig_pkt_meas = math.log10(abs(q_mean0)
                              / max(abs(qg_inf - q_T0), 1e-12))
    check("E2 packet: quotient supplies oscillation digits "
          "(Richardson)",
          qg_inf >= -pkt_bar and dig_pkt >= 1.0,
          "q_G ladder %+.3e/%+.3e/%+.3e -> extrap %+.3e vs q_T %+.2e; "
          "q_mean %+.3e: digits_packet = %.2f at the declared 1e-9 "
          "bar (%.2f at the measured dual-res level: the defect "
          "matrix inherits the packet's own zero-frame cancellation); "
          "PSD gives the one-sided sign of the TOTAL; NOT typed as an "
          "independent sign source for the oscillation channel alone"
          % (qg1, qg2, qg3, qg_inf, q_T0, q_mean0, dig_pkt,
             dig_pkt_meas))

    ns = np.arange(2, 251, dtype=float)
    lam_s = lam_arr[2:251]
    sbox = 0.5 + boxes[0].nodes
    cache_F = (1.0 / sbox + 1.0 / (sbox - 1.0)
               - 0.5 * math.log(math.pi) + 0.5 * np_digamma(sbox / 2.0)
               - (lam_s[None, :]
                  * np.exp(-sbox[:, None] * np.log(ns)[None, :])).sum(1))
    wb0 = omega_analytic(boxes[0].nodes, sched[0][1])
    ker11 = wb0 / ((sig4[0] - boxes[0].nodes) * (sig4[0]
                                                 + boxes[0].nodes))
    t_cache = boxes[0].integrate_plain(ker11, cache_F)
    fj0 = sum(cstar[j] / (sig4[j] - boxes[0].nodes) for j in range(4))
    fk0 = sum(cstar[k] / (sig4[k] + boxes[0].nodes) for k in range(4))
    q_cache = boxes[0].integrate_plain(wb0 * fj0 * fk0, cache_F)
    check("E3 Z1 screen: oscillation channel not transcribable",
          abs(t_cache) < 1e-5 and abs(q_cache) < 1e-5,
          "Lambda-partial-sum integrand (pole-free) box readouts: "
          "block %.1e (vs T[0,0]=%.3e), packet %.1e (vs q_mean "
          "%.2e): the channel lives on the poles of xi'/xi -- "
          "resummed currency only, no cache anywhere (A1 firewall)"
          % (abs(t_cache), targets[0][0, 0], abs(q_cache), q_mean0))

    # ============================================================ F
    section("F. T5 -- THE EPSTEIN WITNESS (off-line control)")

    lat = epstein_lattice(200000)
    relws = []
    for s_test in (3.0, 2.5):
        Zd = sum(cnt * qv ** (-s_test) for qv, cnt in lat)
        Zn = complex(np_epstein_pair(np.array([s_test]))[0][0])
        relws.append(abs(Zn - Zd) / abs(Zd))
    check("F1 genus decomposition == lattice sum",
          relws[0] < 1e-8 and relws[1] < 1e-6,
          "Z_Q = zeta L_-20 + L_-4 L_5 vs literal sum(x^2+5y^2 <= "
          "2e5): rel %.1e at s=3, %.1e at s=2.5 (tail-limited)"
          % (relws[0], relws[1]))

    spots_e = [complex(0.6, 30.0), complex(0.95, 38.0)]
    dev_e = 0.0
    with mp.workdps(50):
        for spz in spots_e:
            Zn = complex(np_epstein_pair(np.array([spz]))[0][0])
            Zm, _ = mp_epstein_pair(mp.mpc(spz.real, spz.imag))
            dev_e = max(dev_e, abs(Zn - complex(Zm)) / abs(complex(Zm)))
    check("F2 np vs mp Epstein weld at complex spots", dev_e < 1e-9,
          "max rel dev %.1e at Re s in {0.6, 0.95}, Im s up to 38"
          % dev_e)

    with mp.workdps(50):
        s_spot = mp.mpc("0.5", "3.0")
        Zm, _ = mp_epstein_pair(s_spot)
        xi_me = (s_spot * (s_spot - 1)
                 * (mp.sqrt(20) / (2 * mp.pi)) ** s_spot
                 * mp.gamma(s_spot) * Zm)
        xi_ig = epstein_xi_incgamma(complex(0.5, 3.0))
        dev_ig = float(abs(xi_me - xi_ig) / abs(xi_ig))
        s_fe = mp.mpc("0.3", "7.0")
        Zf1, _ = mp_epstein_pair(s_fe)
        Zf2, _ = mp_epstein_pair(1 - s_fe)
        lam1 = (mp.sqrt(20) / (2 * mp.pi)) ** s_fe * mp.gamma(s_fe) * Zf1
        lam2 = ((mp.sqrt(20) / (2 * mp.pi)) ** (1 - s_fe)
                * mp.gamma(1 - s_fe) * Zf2)
        dev_fe = float(abs(lam1 - lam2) / abs(lam1))
    check("F3 xi_Q identity weld + functional equation",
          dev_ig < 1e-8 and dev_fe < 1e-8,
          "vs r117 incomplete-gamma rep at 1/2+3i: %.1e; FE residual "
          "at 0.3+7i: %.1e" % (dev_ig, dev_fe))

    with mp.workdps(50):
        rho_w = mp.mpc(WITNESS_SEED.real, WITNESS_SEED.imag)
        for _ in range(30):
            Zv, dZv = mp_epstein_pair(rho_w)
            step = Zv / dZv
            rho_w = rho_w - step
            if abs(step) < mp.mpf("1e-30"):
                break
        Zres = abs(mp_epstein_pair(rho_w)[0])
        rho_wc = complex(rho_w)
    check("F4 witness re-refined from the frozen seed",
          abs(rho_wc - WITNESS_R117) < 1e-6 and float(Zres) < 1e-25,
          "rho = %.10f + %.10fi vs r117 %.10f + %.10fi; |Z_Q(rho)| = "
          "%.1e" % (rho_wc.real, rho_wc.imag, WITNESS_R117.real,
                    WITNESS_R117.imag, float(Zres)))

    T_E = scan_height(*EPS_WINDOW, epstein=True)
    box_E = BoxData(T_E, BOX_DT, epstein=True)
    cnt_E = box_E.zero_count()
    check("F5 Epstein box: integer count, witness inside",
          abs(cnt_E - round(cnt_E)) < 2e-4 and rho_wc.imag < T_E
          and round(cnt_E) >= 4,
          "T_E=%.2f count=%.5f (contains the off-line quadruple "
          "z = +-%.4f +- %.4f i)" % (T_E, cnt_E, rho_wc.real - 0.5,
                                     rho_wc.imag))

    TE_full = target_block(box_E, sig4, OMEGA0)
    tau_E = np.arange(-T_E, T_E + EPS_DTAU / 2, EPS_DTAU)
    mE = np_epstein_pair(0.5 - 1j * tau_E)[0]
    nodes_E = np.stack([1.0 / (s + 1j * tau_E) for s in sig4], axis=1)
    gam_w = rho_wc.imag

    # global ell law (the conductor-20 density price collapses on ell)
    resE8 = coker_gram_big(mE, nodes_E, tau_E, EPS_DTAU, EPS_ELL,
                           0.5 * EPS_ELL, OMEGA0)
    dE8 = rel_defect(resE8["Ghat"], TE_full)
    resE4 = coker_resid(mE, nodes_E, tau_E, EPS_DTAU, 0.4, 0.2, OMEGA0)
    dE4 = rel_defect(resE4["Ghat"], TE_full)
    zq = np.array([complex(rho_wc.real - 0.5, gam_w),
                   complex(rho_wc.real - 0.5, -gam_w),
                   complex(0.5 - rho_wc.real, gam_w),
                   complex(0.5 - rho_wc.real, -gam_w)])
    D_off = np.zeros((4, 4))
    for j in range(4):
        for k in range(4):
            D_off[j, k] = float(np.real(np.sum(
                omega_analytic(zq, OMEGA0)
                / ((sig4[j] - zq) * (sig4[k] + zq)))))
    diff4 = np.real(resE4["Ghat"]) - TE_full
    corr4 = float(np.sum(diff4 * (-D_off))
                  / (np.linalg.norm(diff4) * np.linalg.norm(D_off)))
    print("    global defects: ell=0.8: %.4f -> ell=0.4: %.4f "
          "(target dominated by the LOW on-line zeros, first at "
          "gamma ~ 1.45, where the (ell/|sigma + i gamma|)^2 "
          "evaluation-smoothing class is largest); INFO corr(diff, "
          "-D_off) = %.2f, |D_off|_F/|T|_F = %.5f (global Frobenius "
          "cannot resolve the witness -- the windowed detector below "
          "can)" % (dE8, dE4, corr4,
                    float(np.linalg.norm(D_off)
                          / np.linalg.norm(TE_full))))

    # windowed detector
    wins_E = resE4["windows"]
    cs_E = sorted(0.5 * (a + b) for a, b in wins_E if 0.5 * (a + b) > 0)

    def isolation(c: float) -> float:
        return min(abs(c - c2) for c2 in cs_E if abs(c - c2) > 1e-9)

    ctr = max((c for c in cs_E
               if abs(c - gam_w) >= 2.5 and 3.0 <= c <= T_E - 1.2),
              key=isolation)
    gam_low = min(cs_E)

    # the low-zero window: identity at the lowest Epstein zero
    seeds_low = [c for c in cs_E if abs(c - gam_low) <= 0.7]
    zeros_low = []
    with mp.workdps(50):
        for sd in seeds_low:
            rr = mp.mpc(0.5, sd)
            for _ in range(30):
                Zv, dZv = mp_epstein_pair(rr)
                st = Zv / dZv
                rr = rr - st
                if abs(st) < mp.mpf("1e-25"):
                    break
            rc = complex(rr)
            if not any(abs(rc - zc) < 1e-6 for zc in zeros_low):
                zeros_low.append(rc)
    cnt_low = small_box_count(gam_low)
    Gw_low = windowed_gram(resE4, tau_E, 0.4, gam_low)
    Tw_low = windowed_target(sig4, zeros_low, gam_low, OMEGA0)
    ratio_low = float(np.trace(np.real(Gw_low)) / np.trace(Tw_low))
    check("F6 the ell law and the low-zero window (independent world)",
          dE4 < dE8 and abs(cnt_low - len(zeros_low)) < 2e-3
          and 0.6 <= ratio_low <= 1.4,
          "global defect monotone on ell (%.4f -> %.4f); lowest zero "
          "gamma = %.3f (count %.3f): windowed response ratio %.3f "
          "-- the identity carries at the low boundary zero where "
          "the smoothing class is largest" % (dE8, dE4, gam_low,
                                              cnt_low, ratio_low))
    cnt_w = small_box_count(gam_w)
    cnt_c = small_box_count(ctr)
    seeds_c = [c for c in cs_E if abs(c - ctr) <= 0.7]
    zeros_c = []
    with mp.workdps(50):
        for sd in seeds_c:
            rr = mp.mpc(0.5, sd)
            for _ in range(30):
                Zv, dZv = mp_epstein_pair(rr)
                st = Zv / dZv
                rr = rr - st
                if abs(st) < mp.mpf("1e-25"):
                    break
            rc = complex(rr)
            if not any(abs(rc - zc) < 1e-6 for zc in zeros_c):
                zeros_c.append(rc)
    online_pure = all(abs(z.real - 0.5) < 1e-8 for z in zeros_c)
    zeros_w = [rho_wc, complex(1.0 - rho_wc.real, gam_w)]
    check("F7 windowed counts: off-line pair vs on-line control",
          abs(cnt_w - 2.0) < 2e-3 and abs(cnt_c - len(zeros_c)) < 2e-3
          and online_pure
          and all(abs(z.real - 0.5) > 0.15 for z in zeros_w),
          "witness box count %.4f == 2 (pair rho, 1-conj(rho), "
          "|Re - 1/2| = %.3f); control at %.2f: count %.4f == %d "
          "Newton-refined on-line zeros (|Re - 1/2| < 1e-8)"
          % (cnt_w, abs(rho_wc.real - 0.5), ctr, cnt_c, len(zeros_c)))

    Gw_w = windowed_gram(resE4, tau_E, 0.4, gam_w)
    Gw_c = windowed_gram(resE4, tau_E, 0.4, ctr)
    Tw_w = windowed_target(sig4, zeros_w, gam_w, OMEGA0)
    Tw_c = windowed_target(sig4, zeros_c, ctr, OMEGA0)
    ratio_w = float(np.trace(np.real(Gw_w)) / np.trace(Tw_w))
    ratio_c = float(np.trace(np.real(Gw_c)) / np.trace(Tw_c))
    # dip currency: the witness dip never vanishes; on-line dips do
    min_m_w = min(float(np.min(np.abs(mE)[np.abs(tau_E - c) <= 1.0]))
                  for c in cs_E if abs(c - gam_w) <= 1.0)
    sharpest = min(float(np.min(np.abs(mE)[np.abs(tau_E - c) <= 1.0]))
                   for c in cs_E if abs(c - gam_w) > 1.0)
    # zeta placebo through the same windows
    m_z = np_zeta_pair(0.5 - 1j * tau_E, cutoff=250)[0]
    resZ4 = coker_resid(m_z, nodes_E, tau_E, EPS_DTAU, 0.4, 0.2,
                        OMEGA0)
    Gw_z = windowed_gram(resZ4, tau_E, 0.4, gam_w)
    cnt_z = small_box_count(gam_w, epstein=False)
    print("    windowed responses: witness tr(G_win)=%.3e vs "
          "tr(T_win)=%.3e (ratio %.4f) | control tr=%.3e vs %.3e "
          "(ratio %.3f)" % (float(np.trace(np.real(Gw_w))),
                            float(np.trace(Tw_w)), ratio_w,
                            float(np.trace(np.real(Gw_c))),
                            float(np.trace(Tw_c)), ratio_c))
    print("    zeta placebo at the witness window: count %.5f, "
          "tr(G_win) = %.2e (noise floor)"
          % (cnt_z, float(np.trace(np.real(Gw_z)))))
    check("F8 THE OFF-LINE DETECTION: witness response deficit",
          ratio_w <= 0.2,
          "tr(G_win)/tr(T_win) = %.4f at the witness: the target "
          "counts the off-line pair (count 2) but the cokernel "
          "carries (almost) NO state there -- |m_Q| never vanishes "
          "on the line; the identity SEES the off-line zero as "
          "missing response mass" % ratio_w)
    check("F9 control window responds at the RK weight",
          0.8 <= ratio_c <= 1.2,
          "tr(G_win)/tr(T_win) = %.3f at the isolated on-line "
          "control %.2f (frozen rule: max isolation, distance >= 2.5 "
          "from the witness; the zeta world calibrates the same "
          "statistic at 0.97)" % (ratio_c, ctr))
    check("F10 detection currency: soft dip vs true dips",
          min_m_w >= 25.0 * sharpest,
          "min|m_Q| at the witness dip %.3f >= 25 x sharpest on-line "
          "dip %.4f on the same grid: the multiplier itself "
          "separates off-line from on-line -- resummed currency only "
          "(Euler truncation min|m_P| = 0.11 could NEVER see this, "
          "r119 C1j)" % (min_m_w, sharpest))

    # ============================================================ G
    section("G. T4 -- MIN-CUT PLACEMENT (round-116 graph)")

    flow_base, cut_base = max_flow(R116_EDGES, "UNCOND", "RH")
    conservative = [e for e in R116_EDGES
                    if e[2] not in ("CANDIDATE", "MEAS",
                                    "OMEGA-POS-MEAS")]
    flow_c, cut_c = max_flow(conservative, "UNCOND", "RH")
    check("G1 round-116 base flows reproduced",
          flow_base == 4 and flow_c == 2
          and sorted({c for _s, _d, c in cut_c}) == ["OMEGA-POS"],
          "full=4, conservative=2, conservative cut all OMEGA-POS "
          "(census {MEAS, OMEGA-POS}, cardinality 4)")

    remod = remodel_edges(R116_EDGES, extended=False,
                          counterfactual=False)
    flow_rm, _ = max_flow(remod, "UNCOND", "RH")
    ext = remodel_edges(R116_EDGES, extended=True, counterfactual=False)
    flow_ext, cut_ext = max_flow(ext, "UNCOND", "RH")
    cf = remodel_edges(R116_EDGES, extended=True, counterfactual=True)
    flow_cf, _ = max_flow(cf, "UNCOND", "RH")
    check("G2 omega-gate remodel is flow-equivalent", flow_rm == 4,
          "PICK-FLOORS-FIN -> SV via explicit SV-OMEGA-GATE: flow 4")
    check("G3 IRQG-MEAS shares the Pick-floors omega edge",
          flow_ext == 4,
          "extended flow = 4: the IR-stable quotient-Gram identity "
          "adds NO new cut capacity -- same evidence source (own EM "
          "zeta), same quantifier class (infinitary positivity/limit "
          "introduction); cardinality 4 unchanged")
    print("    counterfactual (independent omega edge): flow = %d "
          "(INFO -- would require the completion to be an evidence "
          "source independent of the Pick floors; it is not: same EM "
          "zeta data)" % flow_cf)
    check("G4 counterfactual arithmetic", flow_cf == 5,
          "independent-omega wiring flows 5, printed as INFO only")
    print("    THE EXACT REMAINING OMEGA (typed): the quotient-Gram")
    print("    identity at omega == 1, T = infinity, for EVERY N and")
    print("    node family, with the zero evaluations EXACTLY")
    print("    orthonormal -- by T2(c) this is the Hermite--Biehler")
    print("    property of xi, i.e. RH itself: same wall, sharper")
    print("    coordinates.  No new unconditional statement beyond")
    print("    the round-116 A2 cap.")

    # ============================================================ H
    section("H. FITNESS TABLE AND VERDICT")

    print("  IR-LADDER TABLE (schedule Om=%.4f T, ell=%.3f/log(T/2pi), "
          "dtau=%.5f ell):" % (OMEGA0 / T0, ELL0 * log0, DTAU_RATIO))
    print("    rung    T      Omega   ell    defect   sfit     "
          "lam_min    |P4-T|/|P4|")
    for r, l in enumerate(ladder):
        print("    %d    %7.2f  %6.2f  %.3f   %.4f   %.4f   %+.2e"
              "   %.4f"
              % (r, l["T"], l["Om"], l["ell"], l["defect"], l["sfit"],
                 l["lam_min"],
                 float(np.linalg.norm(P4 - targets[r])
                       / np.linalg.norm(P4))))

    structural = (dmax <= DEFECT_BAR and carries
                  and all(abs(l["sfit"] - 1) <= NORM_BAR for l in ladder)
                  and all(l["lam_min"] > -1e-12 * max(l["trG"], 1e-30)
                          for l in ladder)
                  and all(l["tr_sm"] < 1e-2 and l["d_sc"] > 0.5
                          for l in ladder)
                  and dstar04 <= 0.35 * dstar08
                  and abs(rk_extrap - 1.0) <= 5e-3)
    diverges = (not carries) and all(
        ladder[i]["defect"] < ladder[i + 1]["defect"]
        for i in range(len(ladder) - 1))

    check("H1 composite typing consistent",
          structural and not degen and not diverges,
          "carry + completion-floor law + RK-diag-to-1 + controls + "
          "no degeneration: outcome (a) of the contract, priced by "
          "the T2(b') floor")
    wall = time.time() - T0_WALL
    check("H2 runtime", wall <= RUNTIME_BAR,
          "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))
    prior = len(CHECKS)
    prior_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("H3 pattern gate",
          prior == N_CHECKS_EXPECTED - 1 and prior_pass == prior,
          "expected %d prior checks, zero fails (got %d, %d fails)"
          % (N_CHECKS_EXPECTED - 1, prior, prior - prior_pass))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    if n_pass != len(CHECKS):
        print("VERDICT: IRWALL-INSTRUMENT-EDGE (failed gate; no "
              "mathematical verdict)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    if structural:
        print("VERDICT: IRWALL-CARRIES(schedule Omega = %.4f T, "
              "ell = %.3f/log(T/2pi)," % (OMEGA0 / T0, ELL0 * log0))
        print("  dtau = %.5f ell: defect ladder %s at constant"
              % (DTAU_RATIO,
                 "/".join("%.4f" % l["defect"] for l in ladder)))
        print("  discretization level, PSD exact, controls die at "
              "every rung, target")
        print("  -> Pick_4 at the modeled mean-density rate)")
        print("  + COMPLETION-FLOOR(delta*(0.8) = %.5f, delta*(0.4) = "
              "%.5f: the exact" % (dstar08, dstar04))
        print("    identity needs the joint limit ell -> 0; r119 "
              "'pure grid' AMENDED)")
        print("  + ISO-CANONICAL-RH-EQUIV(cited: de Branges/HB; the "
              "exact completion")
        print("    datum IS RH) + RK-DIAG-TO-1(measured %.5f)"
              % rk_extrap)
        print("  + OSC-DIGITS(matrix %.1f min over rungs; packet %.1f "
              "at the declared bar,"
              % (min(row[2] for row in osc_rows), dig_pkt))
        print("    %.1f at the measured level)" % dig_pkt_meas)
        print("  + EPSTEIN-OFFLINE-SEEN(windowed: witness response "
              "ratio %.3f vs" % ratio_w)
        print("    control %.2f; counts 2/%d integer; global ell-law "
              "%.4f -> %.4f)" % (ratio_c, len(zeros_c), dE8, dE4))
        print("  + MINCUT-UNCHANGED(4; IRQG shares the Pick-floors "
              "omega edge)")
    elif diverges:
        print("VERDICT: IRWALL-DIVERGES(see the trace/conditioning "
              "diagnostics above)")
    else:
        print("VERDICT: IRWALL-DEGENERATES(identity holds, block "
              "collapse measured)")
    print()
    print("NO RH CLAIM. EXPLORATION ONLY. An IR-stable identity for a")
    print("truncated block is not RH: the omega == 1 / T = infinity /")
    print("all-N completion datum is Hermite--Biehler for xi, i.e. RH")
    print("itself.  Stage 1 remains OPEN.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
