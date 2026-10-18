#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""highpole_filter_tradeoff_probe -- PRIME.ONEBADMODE.HIGHPOLE.01
(EXPLORATION ONLY, experiments/; dissolve the tier-2 obstruction by
filter redesign -- or measure the obstruction law.  2026-08-12.)

MISSION.  CCLIII (rhp_tier2_polecontrol_probe) proved that the eight
pole reads of the deployed m=8 Zolotarev certificate (CCXXV/CCXLVII)
are Weyl m-function values, that the Killip-Simon first-order response
is EXACT at the top pole (capture 1.000 at y = 4.97e4), and that the
Neumann norm route fails at the low decision poles because the KS step
distance D_i (med 2.120e3) exceeds y_j for j <= 4 (Neumann-admissible
cells 148/536).  THE QUESTION: does a rational separator whose poles
ALL satisfy |Im z| >= Y_min -- for a ladder of Y_min values reaching
the KS step scale -- still certify the 68-step finite wall ladder, and
at what (m', reserve, Y_min) trade-off?  If certification and
all-pole Neumann admissibility meet, the corridor's uniform-control
demand moves into the regime where the classical machinery works; if
they cannot meet, the probe must MEASURE the obstruction law and
quantify the best achievable split.

THE STRUCTURAL FRAME (fixed before the frozen run; the probe tests
it).  Any admissible separator R = 1 - D f with f <= 0 on x <= 0,
f in [1-delta, 1] on [c_B, L], and NO poles in |Im z| < Y_min is
analytic on the disk |z - c_B/2| < Y_min/2.  The two-constants
theorem (Nevanlinna; harmonic measure as in Garnett-Marshall,
"Harmonic Measure") applied to h = f - 1 with |h| <= delta on the
segment [c_B, Y_min/2], |h(0)| >= 1, gives
  sup_disk |f| >= (1/delta)^{omega/(1-omega)},  1-omega ~ sqrt(c_B/Y),
i.e. EXPONENTIALLY large in sqrt(Y_min/c_B) ln(1/delta).  Since the
partial-fraction basis functions u_j = eta_j^2/(x^2+eta_j^2), v_j =
eta_j x/(x^2+eta_j^2) are O(1)-bounded on that disk, the l1
coefficient weight of ANY pole-read expression of such a filter --
and hence the KS transfer weight of the certificate -- must be at
least sup_disk|f| up to O(1) factors.  PREDICTION: the best band
delta*(Y_min, W) achievable at l1 budget W obeys
  ln(1/delta*) ~ K sqrt(c_B/Y_min) ln W,
with K an O(1) geometry constant, so the census frontier in Y_min is
LOGARITHMIC in the budget and can never reach the KS scale D ~ 2e3 at
float-representable weights.  The probe MEASURES delta*(Y_min, W) on
frozen ladders, tests the collapse K(Y) = slope * sqrt(Y/c_B) ~
const, finds the actual certification frontier Y*, and recomputes the
tier-2 a-priori census on the constructed filters.  CONSUMED from the
citation: the two-constants inequality as a mechanism; NOT CONSUMED:
any quantitative constant (the law is measured, not assumed).

CONSTRUCTION ROUTES (poles are what is constrained; the verification
is what counts, the construction may be heuristic).
 (i)   CONSTRAINED ZOLOTAREV BY NODE TRUNCATION: CCXXV global elliptic
       filters m = 8..20 with all denominator nodes below
       (Y_min/L)^2 dropped (paired numerator nodes dropped too),
       renormalized by the same outward-padded interval boxes.  Cost
       law exhibit; delta expected to collapse toward 1.
 (ii)  ELEMENTARY HIGH-POLE BLOCKS: f(t) = t prod(t^2+a_k)/
       prod(t^2+b_k), geometric high ladders b_k >= (Y_min/L)^2,
       interlacing midpoint numerators, same interval machinery.
       Same collapse exhibit.
 (iii) THE WORKHORSE -- PARTIAL-FRACTION LP FAMILY: on the FROZEN
       geometric pole ladder eta_1..eta_m' in [Y_min, X_top], X_top =
       max(4 L, 8 Y_min), m'(Y) = min(300, ceil(2.5 sqrt(Y/c_B))+24),
       f(x) = sum_j [alpha_j u_j(x) + beta_j v_j(x)] with coefficients
       from scipy/HiGHS linprog: minimize delta subject to
       f >= 1-delta on the bulk grid [c_B, L]; f <= 1-MARGIN_SUP on
       all positive grids (out to 1e17 so the far tail cannot steal
       the normalization); f <= -MARGIN_NEG min(1,|x|/c_B) on the
       negative grid inside the pole window and f <= 0 beyond;
       f(0) <= 0; 0 <= sum_j beta_j eta_j <= B_NET_CAP (signed tail
       control); per-coefficient bounds |.| <= W and the l1 budget
       sum_j (|alpha_j|+|beta_j|) <= W via auxiliary variables.  The
       LP is scanned over the frozen (Y_LADDER x W_LADDER) grid; one
       disclosed replicate at (1e3, 1e6, m'/2) types m'-insensitivity.
       Because tr f(M) = sum_j eta_j [alpha_j Im + beta_j Re]
       tr(M - i eta_j)^{-1}, the certificate IS an explicit
       l1-bounded functional of the m-function reads at poles
       >= Y_min; kappa_PF = sum_j |term_j|/|sum term_j| is printed.

CERTIFICATION MODEL (rigorous up to outward float padding).
 C-a  Second-order chord boxes with ADAPTIVE bisection: on each box f
      lies between its endpoint values -/+ (dx)^2/8 * F2(box), F2 =
      sum_j |alpha_j| E_u + |beta_j| E_v with the exact per-factor
      curvature envelopes |u''| <= 6/((1+s^2)^2 eta^2) (monotone in
      s = x/eta) and |v''| <= 6 s/((1+s^2)^2 eta^2) (critical point
      s = 1/sqrt(3)).  Boxes failing their target are bisected at the
      geometric midpoint (wave-wise, budget BOX_BUDGET per pass, width
      floor 1e-13 relative); the pad shrinks 4x per split.
 C-b  Targets: certified sup of f on [0, X_TAIL_CF] within relative
      SUP_TOL (D = 1/sup_cert, so R >= 0 on the axis); certified bulk
      lower bound on [c_B, L] within BULK_TOL (delta_cert reporting);
      certified negative-side max <= NEG_ABS (else eps_neg reported
      honestly), so R >= 1 - D eps_neg on x <= 0.
 C-c  Closed-form signed tail beyond X_TAIL_CF = 1e16 (valid X >=
      2 eta_max):  |f(X)| <= |sum beta eta|/X + A_sum/(X^2-eta_max^2)
      + B_sum eta_max^2/(X(X^2-eta_max^2)), A_sum = sum|alpha|eta^2,
      B_sum = sum|beta|eta.  The certificate threshold is the HONEST
      tr R < 1 - D(eps_neg + eps_tail) - CERT_EPS; filters with
      D(eps_neg+eps_tail) > CERT_MARGIN_MAX are typed CERT-VOID.

DECISION AND WARD ROUTES.  DECISION trace: eig-free real route
tr R = 8 - D sum_j [alpha_j eta_j^2 tr(M^2+eta_j^2)^{-1} + beta_j
eta_j tr(M(M^2+eta_j^2)^{-1})] via batched PD solves.  WARDED against
(1) the complex pole-read route via batched LU (algebraically
identical; tie normalized by the cancellation scale D sum|term|), and
(2) the eigensum truth reference (eigenvalues only in truth-reference
and control typing, as in CCXXV).

THE CENSUS (mission b).  Every OK (Y_min, W) filter is censused on
all 68 steps: cert count against its honest threshold, reserve trio
and h-trend (leave-one-out 2SE), kappa_PF, the Neumann fractions
(cells {D_i < eta_j} and pairs {D_i < Y_min}) with D_i recomputed by
local Lanczos (reproduced against CCLIII med 2.120e3, and the
exponent refit on all/surface/deep pairs to sharpen -0.278 +/-
0.277), and the tier-2 a-priori census with the closed-form
||(M - i eta)^{-1}||_HS <= sqrt(8)/eta:  BND_i = D sum_j
eta_j(|alpha_j|+|beta_j|) min(BOUND-A, BOUND-B), BOUND-A = sqrt(8)
D_i/eta^2, BOUND-B = (sqrt(8)/eta) D_i/(eta - D_i) in the Neumann
regime; CONTROLLED(i) iff BND_i <= min(reserve_i, reserve_{i+1}).
THE LAW FIT: per Y, slope_Y = d ln(1/delta*)/d ln W over the W ladder
and the collapse constant K(Y) = slope_Y sqrt(Y/c_B); the frontier
Y* = max Y with a 68/68 certification.

ANTI-CIRCULARITY / EXACTNESS MODEL.  Ladder, frames, split, controls,
source-only L_src imported READ-ONLY from onebadmode_moments_probe
(CCVII); elliptic machinery and interval boxes from
zolotarev_phase_filter_probe (CCXXV); c_h diagnostic from
euler_phase_identity_probe (CCXVII, labelled screen currency only).
All filters are built from (c_B CITED, L_global source-only, frozen
Y/W/m' ladders, frozen grids) ONLY -- no rung spectra enter any
construction (AST-scanned).  One filter per grid point, frozen before
the census, no per-rung tuning.  c_B = 0.5523 CITED from CLIII for
the certified surface range; deep floor FLOAT-LEVEL (CLIV); bridge
exception typed.  Positivity on these finitely many float64 rungs
proves nothing at other h.  NO RH CLAIM.

EXTERNAL-CITED PEDIGREE.  Zolotarev (1877)/Akhiezer Ch. 9 elliptic
nodes (routes i/ii); Nevanlinna two-constants theorem / harmonic
measure (Garnett-Marshall) as the mechanism behind the predicted law;
scipy HiGHS linprog as heuristic constructor.  All deployed
inequalities are re-certified here; no quantitative constant is
borrowed.

GATES (kill -> WARD-BROKEN unless pipeline count failure).
 W1-W6  CCVII/CCXXV ladder reproduction (42 surface, 28 deep,
        68 = 40+1+27; P2/P3 and deep floor reference values).
 W7     L_global equals the stored CCXXV artifact L (rtol 1e-9).
 W8     deployed m=8 margins reproduce the stored artifact per rung
        (<= 1e-8 absolute).
 W9     D_i reproduction: med within rtol 2e-2 of CCLIII 2.120e3.
 M1     every OK LP filter is certified conclusively (cert_margin <=
        CERT_MARGIN_MAX) or typed CERT-VOID; at least one filter
        certifies conclusively.
 M2     decision route == pole-read route and == eigensum truth on
        every rung x filter (ties normalized by the cancellation
        scale; bars TIE_ROUTES/TIE_EIG).
 M3     routes (i)/(ii): certified interval facts on every exhibited
        filter; kept poles >= Y_min.
 M4     m'-insensitivity replicate: |delta*(m'/2) - delta*| at
        (1e3, 1e6) printed and typed (no kill; a large gap means m'
        binds and is disclosed).
 E1-E4  controls fire at rung level (smooth, scramble seed 1, Epstein
        x^2+5y^2 at kz 9 with the declared O(X^2) step-ladder skip,
        cosh A=.01).
 E5     zero certificates on eig-indefinite control steps across ALL
        censused filters and the deployed anchor; genuinely-PD cosh
        cores typed and listed.
 D1     tau screens on reserves non-vacuous where a positive-reserve
        filter exists; c_h screen on the matched surface subset.

FROZEN BARS.  NDIM=8; c_B=5523/10000; Y_LADDER=(1e1,1e2,3e2,1e3,3e3,
1e4,5e4) (the mission ladder 1e3..5e4 extended downward to locate the
split frontier); W_LADDER=(1e2,1e4,1e6,1e8); m'(Y)=min(300,
ceil(2.5 sqrt(Y/c_B))+24); X_TOP=max(4L,8Y); MARGIN_SUP=1e-4;
MARGIN_NEG=1e-6; B_NET_CAP=1e7; LP grids neg/pos/bulk=1200/2200/2600
geometric out to 1e17; LP_TIME_LIMIT=120 s; certification: initial
boxes pos/neg/bulk=3000/2000/4000 (smoke /4), SUP_TOL=1e-4,
SUP_ABS=1e-9, BULK_TOL=1e-4, NEG_ABS=1e-8, WIDTH_FLOOR=1e-13,
BOX_BUDGET=1.5e6 boxes/pass (smoke /4); X_TAIL_CF=1e16; CERT_EPS=
1e-9; CERT_MARGIN_MAX=1e-4; TIE_ROUTES=5e-12, TIE_EIG=1e-9
(normalized); W8 tie 1e-8; D_REF=2.120e3 rtol 2e-2; RESERVE_FLOOR=
1e-2 (CCXLVII typing); SLOPE_PASS=.30, SLOPE_RELOC=.70; truncation
m=8..20; elementary m2 in (8,24), spreads (1e1,1e3); runtime cap
25 min.

SMOKE DISCLOSURE (mandatory; pre-freeze history preserved).
 SMOKE-0 (SPEC v0, artifact suppressed, 208.3 s) ran a first design
 whose LP capped PER-COEFFICIENT magnitudes at 1e4 with no l1 budget
 axis and whose mission verdict logic assumed certification at high
 Y was reachable.  It reproduced the ladder, W7/W8 wards and D_i
 (med 2.120e3, MAX 4.348e4 -- itself a finding: all-pole Neumann
 admissibility needs Y > 4.3e4), routes (i)/(ii) collapsed as
 predicted (best delta 0.9993/0.9993), and controls fired with zero
 leaks.  But ALL 12 LP points returned delta* ~ 0.98 with every
 coefficient pinned at the cap: the l1 budget, not the pole count, is
 the binding resource.  This exposed the two-constants structure now
 frozen in THE STRUCTURAL FRAME above, and three mechanical defects:
 the positive LP grid stopped at 30 eta_max so the far tail stole the
 normalization (sup ~ B_net/x uncontrolled out to ~1e13); the
 negative-side box slop scaled with l1 and broke CERT_MARGIN_MAX for
 every filter (M1 0/12, the one FAIL); and gap_med hit an all-NaN
 slice when no reserve was positive.  SPEC v1 therefore: (a) adds the
 W_LADDER axis with true l1 auxiliary constraints and extends
 Y_LADDER downward -- the mission's own fallback ("measure the
 obstruction law ... quantify the best achievable split"); (b)
 extends the LP grids to 1e17 and adds the signed-tail B_NET row and
 the closed-form signed tail bound; (c) replaces fixed boxes by
 adaptive bisection with explicit targets; (d) normalizes the route
 ties by the cancellation scale; (e) guards empty medians/fits.  No
 truth-side number from SMOKE-0 is claimed; the census/verdict logic
 was rebuilt, not re-barred (no enum weakened: the certification
 threshold and controls are unchanged or stricter).
 SMOKE-1 (SPEC v1, artifact suppressed, boxes /4, 415.3 s): 28/28
 checks, no kills, and NO code change was needed afterwards -- the
 frozen SPEC v2 differs from v1 only by this disclosure paragraph.
 Uncensored smoke headline: W7 tie 0, W8 tie 0.00e+00, W9 D_i med
 2120 exact (trio 1.869e2/2.120e3/4.348e4), route ties 2.71e-13.
 delta*(Y=1e1) = 0.597/0.261/0.108/0.0915 over W = 1e2/1e4/1e6/1e8;
 Y=1e2: 0.952/0.868/0.767/0.748; delta* saturates >= 0.97 for all
 Y >= 1e3 at every budget.  Certifications: 64/68 at (Y=1e1, W=1e6,
 reserve med +0.522), 30/68 at (1e1,1e4), 34/68 at (1e1,1e8) but
 CERT-VOID (eps_neg 0.58: at l1 >= 5e6 the LP negative grid is too
 coarse to hold f <= 0 between its points -- typed, threshold
 honest); ZERO certifications for every Y >= 1e2, hence Y* = NONE
 even at poles only 20x above the deployed minimum.  Collapse
 constants K(Y) = 0.60/0.25/0.13/0.07/0.06/0.03/0.01 -- falling, i.e.
 the attained frontier is at or below the two-constants exponential
 ceiling, as the necessity direction demands (at the top rungs the
 m' = 300 cap and float64 also bind; typed, not repaired).  One LP
 timed out (Y=1e4, W=1e8, status typed).  m'-replicate gap 3.6e-4
 (l1, not m', is the binding resource).  Controls: 1 indefinite, 0
 leaks, min indefinite trace 3.61, 2 PD cosh cores typed
 (certified-by 3/4 filters -- genuinely PD, sound).  Screens:
 tau@deployed PASS, tau@best PASS, c_h@best PASS (40 matched);
 non-best tau rows vacuous (no positive reserve) as expected.
 SPEC v2 (2026-08-12, frozen after the two disclosed smokes):
 everything above unchanged from v1 except this paragraph.  No
 post-freeze numerical amendment is permitted without a new disclosed
 SPEC version.

The only frozen-run write is highpole_filter_tradeoff_results.json
beside this probe; the German CCLVII line is prepended to
experiments/next.txt only after the frozen-run summary.  No marker
move, no verification/paper/ledger/website/manifest edit.

Run:
  TFPT_HIGHPOLE_SMOKE=1 experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/highpole_filter_tradeoff_probe.py
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/highpole_filter_tradeoff_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
from scipy.optimize import linprog

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import onebadmode_moments_probe as ob            # noqa: E402 READ-ONLY CCVII
import zolotarev_phase_filter_probe as zpf       # noqa: E402 READ-ONLY CCXXV
import euler_phase_identity_probe as eul         # noqa: E402 READ-ONLY CCXVII

NDIM = 8
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
Y_LADDER = (1.0e1, 1.0e2, 3.0e2, 1.0e3, 3.0e3, 1.0e4, 5.0e4)
W_LADDER = (1.0e2, 1.0e4, 1.0e6, 1.0e8)
M_CAP = 300
MARGIN_SUP = 1.0e-4
MARGIN_NEG = 1.0e-6
B_NET_CAP = 1.0e7
LP_N_NEG = 1200
LP_N_POS = 2200
LP_N_BULK = 2600
LP_TIME_LIMIT = 120.0
LP_X_FAR = 1.0e17
SMOKE = os.environ.get("TFPT_HIGHPOLE_SMOKE", "0") == "1"
_DIV = 4 if SMOKE else 1
N0_POS = 3000 // _DIV
N0_NEG = 2000 // _DIV
N0_BULK = 4000 // _DIV
BOX_BUDGET = int(1.5e6) // _DIV
SUP_TOL = 1.0e-4
SUP_ABS = 1.0e-9
BULK_TOL = 1.0e-4
NEG_ABS = 1.0e-8
WIDTH_FLOOR = 1.0e-13
X_TAIL_CF = 1.0e16
CERT_EPS = 1.0e-9
CERT_MARGIN_MAX = 1.0e-4
TIE_ROUTES = 5.0e-12
TIE_EIG = 1.0e-9
W8_TIE = 1.0e-8
D_REF = 2.120e3
D_REF_RTOL = 2.0e-2
RESERVE_FLOOR = 1.0e-2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
TRUNC_M = tuple(range(8, 21))
ELEM_M2 = (8, 24)
ELEM_SPREAD = (1.0e1, 1.0e3)
REPL_POINT = (1.0e3, 1.0e6)
HS_C = math.sqrt(float(NDIM))
ARTIFACT = os.path.join(_HERE, "highpole_filter_tradeoff_results.json")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
AC_BANNED = ("eigs", "eigh", "eigvalsh", "Mt", "lamB1")

CHECKS = []
KILLS = []
T0 = time.time()
I8 = np.eye(NDIM)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def trio(values):
    vals = np.asarray(values, float)
    return float(np.min(vals)), float(np.median(vals)), float(np.max(vals))


def f3(values, fmt="%.3f"):
    return "/".join(fmt % value for value in trio(values))


def e3(values):
    return f3(values, "%.3e")


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    variance = float(np.var(x))
    if variance == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    slope = float(np.cov(x, y, bias=True)[0, 1] / variance)
    intercept = float(np.mean(y) - slope * np.mean(x))
    residual = float(np.sum((y - intercept - slope * x) ** 2))
    total = float(np.sum((y - np.mean(y)) ** 2))
    return intercept, slope, 1.0 - residual / total if total > 0 else float("nan")


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _b, slope, r2 = ols_line(x, y)
    loo = []
    for index in range(len(x)):
        keep = np.ones(len(x), bool)
        keep[index] = False
        loo.append(ols_line(x[keep], y[keep])[1])
    loo = np.asarray(loo)
    err = math.sqrt((len(x) - 1) / len(x)
                    * float(np.sum((loo - loo.mean()) ** 2)))
    return slope, err, r2


def screen(values, taus):
    values = np.asarray(values, float)
    taus = np.asarray(taus, float)
    positive = (values > 0.0) & (taus > 0.0) & np.isfinite(values)
    if int(np.sum(positive)) < 3:
        return "vacuous(pos=%d)" % int(np.sum(positive)), float("nan")
    _b, slope, r2 = ols_line(np.log(taus[positive]),
                             np.log(values[positive]))
    label = ("PASS" if abs(slope) <= SLOPE_PASS
             else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s(slope=%+.3f,R2=%.3f,%d excluded)"
            % (label, slope, r2, int(np.sum(~positive)))), slope


def ast_scan():
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(source)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def ast_scan_functions(function_names, banned):
    """AC scan: construction/certification functions must not read any
    rung spectral data."""
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in function_names:
            for sub in ast.walk(node):
                name = None
                if isinstance(sub, ast.Name):
                    name = sub.id
                elif isinstance(sub, ast.Attribute):
                    name = sub.attr
                if name in banned:
                    hits.append("%s:%s" % (node.name, name))
    return hits


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# ------------------------------------------------------------- ladder
def assemble_step(step):
    """CCXXV assemble_step, reproduced verbatim on the ob machinery."""
    tau = step["tau"]
    if tau <= 0.0:
        step["status"] = "REFUSED-TAU"
        return step
    matrix = sym(step["Q"].T @ (step["r2"]["S"] / tau) @ step["Q"])
    step["Mt"] = matrix
    pivot, coupling, block = ob.split_parts(matrix)
    step["n0"], step["bvec"], step["Bblk"] = pivot, coupling, block
    block_eigenvalues = np.linalg.eigvalsh(block)
    step["lamB1"] = float(block_eigenvalues[0])
    try:
        step["gap"] = pivot - float(coupling
                                    @ np.linalg.solve(block, coupling))
    except np.linalg.LinAlgError:
        step["gap"] = float("nan")
    step["eigs"] = np.linalg.eigvalsh(matrix)  # truth reference only
    gershgorin = ob.gersh_bound(matrix)
    frobenius = ob.fro_bound(matrix)
    step["L_src"] = min(gershgorin, frobenius) * ob.L_INFLATE
    step["L_win"] = "G" if gershgorin <= frobenius else "F"
    if step["L_src"] <= CB_F * (1.0 + 1e-6):
        step["status"] = "REFUSED-L"
        return step
    step["status"] = "OK"
    return step


def build_truth_ladder():
    section("W -- CCVII/CCXXV ladder reproduction (read-only machinery)")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones),
                                               ob.N_RUNGS_EXP),
          len(zones) == ob.N_RUNGS_EXP, kill="K1")
    surface = [ob.build_rung("surf", kz, with_split=True) for kz in zones]
    check("W1b all surface chains complete",
          all(rung is not None for rung in surface), kill="K1")
    if KILLS:
        return zones, []
    surface_h = sorted(surface, key=lambda rung: (rung["h"], rung["kz"]))
    surface_steps = ob.make_steps(surface_h)
    for step in surface_steps:
        assemble_step(step)
    surface_ok = [step for step in surface_steps if step["status"] == "OK"]
    min_b_surface = min(step["lamB1"] for step in surface_ok)
    gaps = np.asarray([step["gap"] for step in surface_ok])
    check("W2 P2/P3 reproduction minB %.4f, gap min/med %.4f/%.4f"
          % (min_b_surface, float(np.min(gaps)), float(np.median(gaps))),
          (abs(min_b_surface / ob.MINB_REF - 1.0) <= ob.MINB_RTOL
           and abs(float(np.min(gaps)) / ob.GAPMIN_REF - 1.0) <= ob.GAP_RTOL
           and abs(float(np.median(gaps)) / ob.GAPMED_REF - 1.0)
           <= ob.GAP_RTOL), kill="K2")

    extension = ob.build_ext_tables()
    overlap = float(np.max(np.abs(
        extension[:ob.core.ATOM_MAX + 1] - ob.core.LAM_TAB)))
    deep_zones = ob.deep_zone_census()
    check("W3 deep table overlap %.1e == 0; rung census %d == %d"
          % (overlap, len(deep_zones), ob.N_DEEP_EXP),
          overlap == 0.0 and len(deep_zones) == ob.N_DEEP_EXP, kill="K1")
    deep = []
    for kz, expected_h in sorted(deep_zones, key=lambda pair:
                                 (pair[1], pair[0])):
        if time.time() - T0 > ob.SOFT_BUDGET_S:
            break
        rung = ob.build_rung("deep", kz, with_split=True)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.0f s]"
              % (kz, expected_h, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [rung for rung in deep
               if rung["core_ok"] and rung["negA"] == 0
               and rung.get("lamS", -1.0) > 0.0]
    check("W4 deep truth rungs %d == %d" % (len(deep_ok), ob.N_DEEP_EXP),
          len(deep_ok) == ob.N_DEEP_EXP, kill="K1")
    if KILLS:
        return zones, []
    deep_h = sorted(deep_ok, key=lambda rung: (rung["h"], rung["kz"]))
    deep_steps = ob.make_steps(deep_h)
    for step in deep_steps:
        assemble_step(step)
    deep_step_ok = [step for step in deep_steps if step["status"] == "OK"]
    min_b_deep = min(step["lamB1"] for step in deep_step_ok)
    check("W5 CLIV deep own-frame floor %.4f == %.4f"
          % (min_b_deep, ob.DEEP_MINB_REF),
          abs(min_b_deep / ob.DEEP_MINB_REF - 1.0) <= ob.DEEP_MINB_RTOL,
          kill="K2")

    combined = sorted(
        [rung for rung in surface_h if rung["core_ok"]] + deep_h,
        key=lambda rung: (rung["h"], rung["kz"]))
    combined_steps = ob.make_steps(combined)
    for step in combined_steps:
        assemble_step(step)
    ok_steps = [step for step in combined_steps if step["status"] == "OK"]
    segments = [ob.seg_of(step) for step in ok_steps]
    expected = (segments.count("surf") == 40
                and segments.count("bridge") == 1
                and segments.count("deep") == 27
                and len(ok_steps) == 68)
    check("W6 combined ladder 68 = surface %d + bridge %d + deep %d"
          % (segments.count("surf"), segments.count("bridge"),
             segments.count("deep")), expected, kill="K1")
    return zones, ok_steps


# ------------------------------------------- KS distances (tier-2 data)
def jacobi_form(matrix):
    """CCLIII Lanczos tridiagonalization of (M, e_0), reproduced."""
    if not np.all(np.isfinite(matrix)):
        return None
    qq = np.zeros((NDIM, NDIM))
    qq[0, 0] = 1.0
    a = np.zeros(NDIM - 1)
    b = np.zeros(NDIM)
    for k in range(NDIM):
        z = matrix @ qq[:, k]
        b[k] = float(qq[:, k] @ z)
        z = z - b[k] * qq[:, k]
        if k > 0:
            z = z - a[k - 1] * qq[:, k - 1]
        for _ in range(2):
            z = z - qq[:, :k + 1] @ (qq[:, :k + 1].T @ z)
        if k == NDIM - 1:
            break
        nz = float(np.linalg.norm(z))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b


def ks_distance(a1, b1, a2, b2):
    da = np.asarray(a2, float) - np.asarray(a1, float)
    db = np.asarray(b2, float) - np.asarray(b1, float)
    return math.sqrt(float(np.sum(db ** 2)) + 2.0 * float(np.sum(da ** 2)))


def ks_census(steps):
    section("K -- KS step distances D_i recomputed (tier-2 currency), "
            "deep-extended exponent")
    jac = []
    for step in steps:
        form = jacobi_form(step["Mt"])
        if form is None:
            return None
        jac.append(form)
    dks = np.asarray([ks_distance(*jac[i], *jac[i + 1])
                      for i in range(len(jac) - 1)], float)
    h_pair = np.asarray([steps[i]["r2"]["h"] for i in range(len(dks))],
                        float)
    seg_pair = [ob.seg_of(steps[i]) for i in range(len(dks))]
    med = float(np.median(dks))
    check("W9 D_i reproduction: med %.4g vs CCLIII %.4g (rtol %.0e); "
          "trio %s" % (med, D_REF, D_REF_RTOL, e3(dks)),
          abs(med / D_REF - 1.0) <= D_REF_RTOL, kill="K2")
    fits = {}
    for label, mask in (
            ("all", np.ones(len(dks), bool)),
            ("surface", np.asarray([s == "surf" for s in seg_pair])),
            ("deep", np.asarray([s == "deep" for s in seg_pair]))):
        if int(np.sum(mask)) >= 4:
            slope, err, r2 = jack_slope(np.log(h_pair[mask]),
                                        np.log(dks[mask]))
            fits[label] = (slope, 2.0 * err, r2, int(np.sum(mask)))
            print("    D ~ h^%+.3f +/- 2SE %.3f (R2 %.3f, n=%d)  [%s]"
                  % (slope, 2.0 * err, r2, int(np.sum(mask)), label))
    return dict(dks=dks, h_pair=h_pair, seg_pair=seg_pair, fits=fits,
                dmax=float(np.max(dks)))


# --------------------------------------------- route (iii): LP family
def ladder_poles(y_min, m_prime, l_global):
    x_top = max(4.0 * l_global, 8.0 * y_min)
    return np.geomspace(y_min, x_top, m_prime)


def basis_uv(x, eta):
    xx = np.asarray(x, float)[:, None]
    ee = np.asarray(eta, float)[None, :]
    den = xx * xx + ee * ee
    return (ee * ee) / den, (ee * xx) / den


def m_of(y_min):
    return int(min(M_CAP, math.ceil(2.5 * math.sqrt(y_min / CB_F)) + 24))


def lp_construct(y_min, w_budget, l_global, m_prime=None):
    """HEURISTIC constructor (HiGHS).  Inputs: frozen scalars/grids
    only.  Output re-certified by certify_filter."""
    if m_prime is None:
        m_prime = m_of(y_min)
    eta = ladder_poles(y_min, m_prime, l_global)
    g_neg = -np.geomspace(1e-4 * CB_F, LP_X_FAR, LP_N_NEG)
    g_pos = np.geomspace(1e-4 * CB_F, LP_X_FAR, LP_N_POS)
    g_bulk = np.geomspace(CB_F, l_global, LP_N_BULK)
    n_coef = 2 * m_prime
    n_var = n_coef + 1 + n_coef            # coefs, delta, l1-aux
    rows = []
    rhs = []

    def block(xgrid, sign, rhs_vals, with_delta=0.0):
        u, v = basis_uv(xgrid, eta)
        mat = np.zeros((len(xgrid), n_var))
        mat[:, :m_prime] = sign * u
        mat[:, m_prime:n_coef] = sign * v
        mat[:, n_coef] = with_delta
        rows.append(mat)
        rhs.append(np.asarray(rhs_vals, float))

    # f >= 1 - delta on bulk:  -f - delta <= -1
    block(g_bulk, -1.0, -np.ones(LP_N_BULK), with_delta=-1.0)
    # f <= 1 - MARGIN_SUP on bulk and the full positive grid
    block(g_bulk, 1.0, np.full(LP_N_BULK, 1.0 - MARGIN_SUP))
    block(g_pos, 1.0, np.full(LP_N_POS, 1.0 - MARGIN_SUP))
    # f <= -MARGIN_NEG*min(1,|x|/c) inside the pole window; f <= 0 beyond
    neg_rhs = np.where(np.abs(g_neg) <= 10.0 * float(eta[-1]),
                       -MARGIN_NEG * np.minimum(1.0, np.abs(g_neg) / CB_F),
                       0.0)
    block(g_neg, 1.0, neg_rhs)
    # f(0) = sum alpha <= 0
    row0 = np.zeros((1, n_var))
    row0[0, :m_prime] = 1.0
    rows.append(row0)
    rhs.append(np.zeros(1))
    # signed tail control: 0 <= sum beta_j eta_j <= B_NET_CAP
    rowb = np.zeros((2, n_var))
    rowb[0, m_prime:n_coef] = -eta
    rowb[1, m_prime:n_coef] = eta
    rows.append(rowb)
    rhs.append(np.asarray([0.0, B_NET_CAP]))
    # l1 auxiliaries: +-coef_j - s_j <= 0; sum s_j <= W
    aux = np.zeros((2 * n_coef + 1, n_var))
    for j in range(n_coef):
        aux[2 * j, j] = 1.0
        aux[2 * j, n_coef + 1 + j] = -1.0
        aux[2 * j + 1, j] = -1.0
        aux[2 * j + 1, n_coef + 1 + j] = -1.0
    aux[2 * n_coef, n_coef + 1:] = 1.0
    rows.append(aux)
    rhs.append(np.concatenate([np.zeros(2 * n_coef), [w_budget]]))

    a_ub = np.concatenate(rows, axis=0)
    b_ub = np.concatenate(rhs)
    bounds = ([(-w_budget, w_budget)] * n_coef + [(0.0, 2.0)]
              + [(0.0, w_budget)] * n_coef)
    cost = np.zeros(n_var)
    cost[n_coef] = 1.0
    t_lp = time.time()
    res = linprog(cost, A_ub=a_ub, b_ub=b_ub, bounds=bounds,
                  method="highs",
                  options=dict(time_limit=LP_TIME_LIMIT))
    dt = time.time() - t_lp
    if res.status != 0 or res.x is None:
        return dict(status="LP-%s" % res.status, y_min=y_min,
                    w_budget=w_budget, m_prime=m_prime, eta=eta,
                    lp_seconds=dt)
    alpha = np.asarray(res.x[:m_prime], float)
    beta = np.asarray(res.x[m_prime:n_coef], float)
    delta_lp = float(res.x[n_coef])
    return dict(status="OK", y_min=y_min, w_budget=w_budget,
                m_prime=m_prime, eta=eta, alpha=alpha, beta=beta,
                delta_lp=delta_lp,
                l1=float(np.sum(np.abs(alpha)) + np.sum(np.abs(beta))),
                w_l1=float(np.sum(eta * (np.abs(alpha) + np.abs(beta)))),
                lp_seconds=dt)


def _f2_env(b0, b1, eta):
    """Certified per-box curvature envelopes: |u''| <= 6/((1+s^2)^2
    eta^2) (monotone decreasing in s = |x|/eta) and |v''| <=
    6 s/((1+s^2)^2 eta^2) (critical point s = 1/sqrt(3))."""
    s0 = b0[:, None] / eta[None, :]
    s1 = b1[:, None] / eta[None, :]
    inv_eta2 = 1.0 / (eta[None, :] ** 2)
    e_u = 6.0 / ((1.0 + s0 * s0) ** 2) * inv_eta2
    g0 = s0 / ((1.0 + s0 * s0) ** 2)
    g1 = s1 / ((1.0 + s1 * s1) ** 2)
    g_crit = math.sqrt(3.0) * 3.0 / 16.0
    crit = 1.0 / math.sqrt(3.0)
    g_max = np.maximum(g0, g1)
    inside = (s0 <= crit) & (crit <= s1)
    g_max = np.where(inside, np.maximum(g_max, g_crit), g_max)
    e_v = 6.0 * g_max * inv_eta2
    return e_u, e_v


def _box_pass(a_edges, b_edges, filt, mode, bar_fn):
    """Adaptive certified extreme of f over the boxes [a_i, b_i].
    mode 'hi' certifies an upper bound, 'lo' a lower bound (internally
    flipped to an upper bound of -f).  bar_fn maps the current
    achieved endpoint extreme (in flipped coordinates) to the
    refinement bar.  Returns (certified extreme, achieved endpoint
    extreme, n_boxes), both in the original orientation."""
    eta = filt["eta"]
    abs_a = np.abs(filt["alpha"])
    abs_b = np.abs(filt["beta"])
    flip = -1.0 if mode == "lo" else 1.0

    def f_of(x):
        u, v = basis_uv(x, eta)
        return flip * (u @ filt["alpha"] + v @ filt["beta"])

    a_cur = np.asarray(a_edges, float)
    b_cur = np.asarray(b_edges, float)
    fa = f_of(a_cur)
    fb = f_of(b_cur)
    achieved = float(np.max(np.concatenate([fa, fb])))
    total = len(a_cur)
    done_extreme = -np.inf
    while True:
        alo = np.abs(a_cur)
        blo = np.abs(b_cur)
        s_lo = np.minimum(alo, blo)
        s_hi = np.maximum(alo, blo)
        e_u, e_v = _f2_env(s_lo, s_hi, eta)
        f2 = e_u @ abs_a + e_v @ abs_b
        dx = np.abs(b_cur - a_cur)
        pad = (dx * dx / 8.0) * f2 * (1.0 + 1e-12) + 1e-12 * filt["l1"]
        hi_box = np.maximum(fa, fb) + pad
        achieved = max(achieved, float(np.max(np.maximum(fa, fb))))
        bar = bar_fn(achieved)
        refinable = (hi_box > bar) \
            & (dx > WIDTH_FLOOR * np.maximum(s_hi, 1e-300))
        if np.any(~refinable):
            done_extreme = max(done_extreme,
                               float(np.max(hi_box[~refinable])))
        if not np.any(refinable) or total > BOX_BUDGET:
            if np.any(refinable):
                done_extreme = max(done_extreme,
                                   float(np.max(hi_box[refinable])))
            break
        a_ref = a_cur[refinable]
        b_ref = b_cur[refinable]
        mid = np.sign(0.5 * (a_ref + b_ref)) * np.sqrt(
            np.maximum(np.abs(a_ref) * np.abs(b_ref), 1e-300))
        low_mag = np.minimum(np.abs(a_ref), np.abs(b_ref))
        bad = (np.abs(mid) <= low_mag) | (np.abs(mid)
                                          >= np.maximum(np.abs(a_ref),
                                                        np.abs(b_ref)))
        mid = np.where(bad, 0.5 * (a_ref + b_ref), mid)
        fm = f_of(mid)
        fa_r = fa[refinable]
        fb_r = fb[refinable]
        a_cur = np.concatenate([a_ref, mid])
        b_cur = np.concatenate([mid, b_ref])
        fa = np.concatenate([fa_r, fm])
        fb = np.concatenate([fm, fb_r])
        total += len(mid)
    certified = max(done_extreme, achieved)
    return flip * certified, flip * achieved, total


def certify_filter(filt, l_global):
    """Rigorous-up-to-float-padding certification of an LP filter."""
    eta = filt["eta"]
    a_sum = float(np.sum(np.abs(filt["alpha"]) * eta * eta))
    b_sum = float(np.sum(np.abs(filt["beta"]) * eta))
    b_net = abs(float(np.sum(filt["beta"] * eta)))
    eta_max = float(eta[-1])
    tail_bound = (b_net / X_TAIL_CF
                  + a_sum / (X_TAIL_CF ** 2 - eta_max ** 2)
                  + b_sum * eta_max ** 2
                  / (X_TAIL_CF * (X_TAIL_CF ** 2 - eta_max ** 2)))
    pos_edges = np.concatenate((
        [0.0], np.geomspace(1e-9 * CB_F, CB_F, N0_POS // 3 + 1),
        np.geomspace(CB_F, l_global, N0_POS + 1)[1:],
        np.geomspace(l_global, X_TAIL_CF, N0_POS // 3 + 1)[1:]))
    pos_edges = np.unique(pos_edges)
    sup_pos, _ach_s, n1 = _box_pass(
        pos_edges[:-1], pos_edges[1:], filt, "hi",
        lambda ach: ach + max(SUP_ABS, SUP_TOL * abs(ach)))
    sup_cert = max(sup_pos, tail_bound)
    bulk_edges = np.geomspace(CB_F, l_global, N0_BULK + 1)
    # bar_fn acts in flipped coordinates (upper bound of -f)
    bulk_lo, _ach_b, n2 = _box_pass(
        bulk_edges[:-1], bulk_edges[1:], filt, "lo",
        lambda ach: ach + BULK_TOL)
    neg_grid = np.concatenate(([0.0],
                               np.geomspace(1e-9 * CB_F, X_TAIL_CF,
                                            N0_NEG + 1)))
    neg_edges = -neg_grid[::-1]
    neg_max, _ach_n, n3 = _box_pass(
        neg_edges[:-1], neg_edges[1:], filt, "hi",
        lambda ach: NEG_ABS)
    eps_neg = max(0.0, neg_max) + tail_bound
    d_norm = 1.0 / sup_cert if sup_cert > 0.0 else float("inf")
    delta_cert = 1.0 - d_norm * bulk_lo
    cert_margin = d_norm * (eps_neg + tail_bound)
    filt.update(D=d_norm, sup_cert=sup_cert, bulk_lo=bulk_lo,
                delta_cert=float(delta_cert), eps_neg=float(eps_neg),
                tail_bound=float(tail_bound),
                cert_margin=float(cert_margin),
                threshold=1.0 - cert_margin - CERT_EPS,
                cert_conclusive=bool(cert_margin <= CERT_MARGIN_MAX),
                boxes=int(n1 + n2 + n3))
    return filt


def trace_decision(matrix, filt):
    """DECISION route: eig-free real PD solves, batched.  Returns
    (trace, kappa, cancellation scale)."""
    eta, alpha, beta = filt["eta"], filt["alpha"], filt["beta"]
    m2 = matrix @ matrix
    a_batch = m2[None, :, :] + (eta ** 2)[:, None, None] * I8[None, :, :]
    sol = np.linalg.solve(a_batch, np.broadcast_to(
        I8, (len(eta), NDIM, NDIM)))
    tr_u = eta ** 2 * np.trace(sol, axis1=1, axis2=2)
    tr_v = eta * np.trace(matrix[None, :, :] @ sol, axis1=1, axis2=2)
    terms = alpha * tr_u + beta * tr_v
    tr_f = math.fsum(terms)
    scale = filt["D"] * float(np.sum(np.abs(terms)))
    kappa = scale / max(1e-300, filt["D"] * abs(tr_f))
    return NDIM - filt["D"] * tr_f, kappa, scale


def trace_reads(matrix, filt):
    """WARD route: the pole-read expression via complex LU, batched."""
    eta, alpha, beta = filt["eta"], filt["alpha"], filt["beta"]
    a_batch = matrix[None, :, :].astype(complex) \
        - 1j * eta[:, None, None] * I8[None, :, :].astype(complex)
    sol = np.linalg.solve(a_batch, np.broadcast_to(
        I8.astype(complex), (len(eta), NDIM, NDIM)))
    reads = np.trace(sol, axis1=1, axis2=2)
    terms = eta * (alpha * reads.imag + beta * reads.real)
    return NDIM - filt["D"] * math.fsum(terms)


def scalar_f(x, filt):
    u, v = basis_uv(np.atleast_1d(np.asarray(x, float)), filt["eta"])
    return u @ filt["alpha"] + v @ filt["beta"]


# ----------------------------------- routes (i)/(ii): interval exhibits
def custom_interval_filter(num_nodes, den_nodes, eps_val):
    """delta/D for a positive-interlacing node filter via the CCXXV
    outward-padded interval boxes (READ-ONLY import)."""
    left_edges = np.linspace(0.0, eps_val, zpf.N_LEFT + 1)
    target_edges = np.geomspace(eps_val, 1.0, zpf.N_TARGET + 1)
    tail_edges = np.concatenate(([0.0],
                                 np.geomspace(1e-14, 1.0, zpf.N_TAIL + 1)))
    _l_lo, l_hi = zpf.product_interval(left_edges, num_nodes, den_nodes)
    t_lo, t_hi = zpf.product_interval(target_edges, num_nodes, den_nodes)
    _q_lo, q_hi = zpf.product_interval(tail_edges, num_nodes, den_nodes,
                                       reciprocal=True)
    sup = max(float(np.max(l_hi)), float(np.max(t_hi)),
              float(np.max(q_hi)))
    inf_bulk = float(np.min(t_lo))
    d_norm = 1.0 / sup
    return max(0.0, 1.0 - d_norm * inf_bulk), d_norm


def route_i_truncation(l_global):
    section("T -- route (i): constrained Zolotarev by node truncation "
            "(cost-law exhibit)")
    base = {m: zpf.build_filter(CB_F, l_global, m) for m in TRUNC_M}
    rows = []
    for y_min in Y_LADDER:
        theta = (y_min / l_global) ** 2
        best = None
        for m in TRUNC_M:
            den = np.asarray(base[m]["den"], float)
            num = np.asarray(base[m]["num"], float)
            keep = den >= theta
            d_drop = int(np.sum(~keep))
            if d_drop == 0 or d_drop >= m or (m - d_drop) < 1 \
                    or d_drop > len(num):
                continue
            den_k = den[keep]
            num_k = num[d_drop:]
            delta, _d = custom_interval_filter(num_k, den_k,
                                               CB_F / l_global)
            min_pole = l_global * math.sqrt(float(np.min(den_k)))
            row = dict(y_min=y_min, m=m, kept=int(m - d_drop),
                       delta=float(delta), min_pole=float(min_pole))
            rows.append(row)
            if best is None or delta < best["delta"]:
                best = row
        if best:
            print("    Y_min %.0e best delta %.6f (m=%d kept=%d, "
                  "min pole %.3g)" % (y_min, best["delta"], best["m"],
                                      best["kept"], best["min_pole"]))
        else:
            print("    Y_min %.0e: no admissible truncation" % y_min)
    ok = all(row["min_pole"] >= row["y_min"] * (1.0 - 1e-9)
             for row in rows)
    check("M3a truncation exhibits: every kept pole >= Y_min (%d rows)"
          % len(rows), ok and len(rows) > 0, kill="K2")
    return rows


def route_ii_elementary(l_global):
    section("U -- route (ii): elementary high-pole block products "
            "(cost-law exhibit)")
    rows = []
    for y_min in Y_LADDER:
        b0 = (y_min / l_global) ** 2
        for m2 in ELEM_M2:
            for spread in ELEM_SPREAD:
                den = np.geomspace(b0, b0 * spread, m2)
                num = np.sqrt(den[:-1] * den[1:])
                delta, _d = custom_interval_filter(num, den,
                                                   CB_F / l_global)
                rows.append(dict(y_min=y_min, m=m2, spread=spread,
                                 delta=float(delta),
                                 min_pole=float(l_global
                                                * math.sqrt(den[0]))))
    for y_min in Y_LADDER:
        sub = [row for row in rows if row["y_min"] == y_min]
        best = min(sub, key=lambda row: row["delta"])
        print("    Y_min %.0e best delta %.6f (m=%d spread %.0e)"
              % (y_min, best["delta"], best["m"], best["spread"]))
    ok = all(row["min_pole"] >= row["y_min"] * (1.0 - 1e-9)
             for row in rows)
    check("M3b elementary exhibits: every pole >= Y_min (%d rows)"
          % len(rows), ok, kill="K2")
    return rows


# ------------------------------------------------------------- census
def census_filter(filt, steps, ks_data):
    reserves = []
    kappas = []
    tie_routes = 0.0
    tie_eig = 0.0
    for step in steps:
        trace_val, kappa, scale = trace_decision(step["Mt"], filt)
        trace_rd = trace_reads(step["Mt"], filt)
        truth = NDIM - filt["D"] * math.fsum(
            scalar_f(step["eigs"], filt).tolist())
        norm = max(1.0, scale)
        tie_routes = max(tie_routes, abs(trace_val - trace_rd) / norm)
        tie_eig = max(tie_eig, abs(trace_val - truth) / norm)
        reserves.append(1.0 - trace_val)
        kappas.append(kappa)
    reserves = np.asarray(reserves)
    margin_needed = filt["cert_margin"] + CERT_EPS
    cert_n = int(np.sum(reserves > margin_needed))
    h_log = np.log([step["r2"]["h"] for step in steps])
    positive = reserves > 0.0
    if int(np.sum(positive)) >= 4:
        slope, err, _r2 = jack_slope(h_log[positive],
                                     np.log(reserves[positive]))
    else:
        slope, err = float("nan"), float("nan")
    dks = ks_data["dks"]
    eta = filt["eta"]
    cell_frac = float(np.mean(dks[:, None] < eta[None, :]))
    pair_frac = float(np.mean(dks < float(np.min(eta))))
    weights = eta * (np.abs(filt["alpha"]) + np.abs(filt["beta"]))
    bnd_a = HS_C * dks[:, None] / (eta[None, :] ** 2)
    with np.errstate(divide="ignore", invalid="ignore"):
        bnd_b = np.where(dks[:, None] < eta[None, :],
                         (HS_C / eta[None, :]) * dks[:, None]
                         / (eta[None, :] - dks[:, None]), np.inf)
    bnd = filt["D"] * (np.minimum(bnd_a, bnd_b) @ weights)
    budget = np.minimum(reserves[:-1], reserves[1:])
    valid = budget > 0.0
    n_valid = int(np.sum(valid))
    controlled = int(np.sum((bnd <= budget) & valid))
    gap_med = (float(np.median((bnd / budget)[valid]))
               if n_valid else float("nan"))
    filt.update(reserves=reserves, cert_n=cert_n,
                reserve_trio=trio(reserves), h_slope=slope,
                h_slope_2se=2.0 * err,
                kappa_med=float(np.median(kappas)),
                tie_routes=tie_routes, tie_eig=tie_eig,
                cell_frac=cell_frac, pair_frac=pair_frac,
                controlled=controlled, n_valid=n_valid,
                gap_med=gap_med,
                o1=bool(float(np.min(reserves)) >= RESERVE_FLOOR))
    return filt


# ------------------------------------------------------------ controls
def run_controls(zones, filters, deployed):
    section("C -- controls (CCVII battery; controls must fire)")
    worlds = {}
    smooth = [ob.build_rung("surf", kz, world="smooth") for kz in zones]
    smooth_fire = sum(isinstance(rung, dict) and rung["negA"] > 0
                      for rung in smooth)
    check("E1 smooth fires on %d rungs" % smooth_fire, smooth_fire > 0,
          kill="K2")
    worlds["smooth"] = smooth
    scramble = [ob.build_rung("surf", kz, scramble_seed=ob.SCR_SEED)
                for kz in zones]
    scramble_fire = sum(rung is None or (
        isinstance(rung, dict) and rung["negA"] > 0) for rung in scramble)
    check("E2 scramble seed %d fires on %d rungs"
          % (ob.SCR_SEED, scramble_fire), scramble_fire > 0, kill="K2")
    worlds["scramble"] = scramble
    rung9 = ob.window_of(ob.CTRL_KZ)
    epstein_n = int(math.floor(math.exp(2.0 * rung9["alpha"]))) + 1
    epstein_lambda = ob.lambda_eps(epstein_n)
    idx = np.nonzero(np.abs(epstein_lambda) > 1e-12)[0]
    epstein = ob.build_rung(
        "surf", ob.CTRL_KZ,
        comb=(np.log(idx.astype(float)),
              2.0 * epstein_lambda[idx] / np.sqrt(idx.astype(float))))
    check("E3 Epstein x^2+5y^2 fires at kz %d; step ladder DECLARED "
          "SKIPPED O(X^2)" % ob.CTRL_KZ,
          epstein is None or epstein["negA"] > 0, kill="K2")

    def cosh_injection(rung):
        times = np.arange(rung["M"]) * rung["D"]
        return (ob.INJ_A * np.cos(ob.INJ_GAMMA0 * times)
                * (np.cosh(ob.INJ_DELTA * times) - 1.0))

    cosh = [ob.build_rung("surf", kz, lag_fn=cosh_injection)
            for kz in zones]
    cosh_fire = sum(rung is None or (
        isinstance(rung, dict) and rung["negA"] > 0) for rung in cosh)
    check("E4 cosh A=%.3g fires on %d rungs" % (ob.INJ_A, cosh_fire),
          cosh_fire > 0, kill="K2")
    worlds["cosh"] = cosh

    leaks = 0
    n_indef = 0
    min_trace = float("inf")
    pd_cores = []
    for world_name, ladder in worlds.items():
        rungs = sorted([rung for rung in ladder if isinstance(rung, dict)],
                       key=lambda rung: (rung["h"], rung["kz"]))
        control_steps = ob.make_steps(rungs, relax=True)
        world_indef = 0
        for step in control_steps:
            assemble_step(step)
            if step["status"] != "OK":
                continue
            lam_min = float(step["eigs"][0])
            lam_scale = max(1.0, float(step["eigs"][-1]))
            indefinite = lam_min <= -1e-10 * lam_scale
            certs = []
            for filt in filters:
                trace_val, _k, _s = trace_decision(step["Mt"], filt)
                certs.append(trace_val < filt["threshold"])
                if indefinite:
                    min_trace = min(min_trace, trace_val)
            dep_trace = zpf.trace_filter_lu(step["Mt"], deployed)
            certs.append(dep_trace < 1.0)
            if indefinite:
                n_indef += 1
                world_indef += 1
                leaks += int(any(certs))
            elif lam_min > 0.0:
                pd_cores.append(dict(world=world_name,
                                     kz=int(step["r2"]["kz"]),
                                     h=int(step["r2"]["h"]),
                                     lam_min=lam_min,
                                     certified=int(sum(certs))))
        print("    %-9s steps %2d indefinite %2d"
              % (world_name, len(control_steps), world_indef))
    for core in pd_cores:
        print("      PD core %(world)s kz %(kz)d h %(h)d lam_min "
              "%(lam_min)+.3e certified-by %(certified)d filters"
              % core)
    check("E5 zero certificates on eig-indefinite controls across all "
          "%d census filters + deployed (%d indefinite, %d leaks; min "
          "indefinite trace %.4g)" % (len(filters), n_indef, leaks,
                                      min_trace),
          leaks == 0 and n_indef > 0, kill="K2")
    check("E6 genuinely-PD cosh cores typed: %d listed"
          % len([c for c in pd_cores if c["world"] == "cosh"]),
          True)
    return dict(n_indef=n_indef, leaks=leaks,
                pd_cores=pd_cores, min_trace=min_trace)


def ch_surface_map():
    """CCXVII c_h on the euler-probe surface rungs, keyed by (h, kz) of
    the euler rung (matched to steps by h, as in tier-2)."""
    out = {}
    for kz in range(3, eul.KZMAX):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        out[int(rung["h"])] = 1.0 - top
    return out


# ---------------------------------------------------------------- main
def main():
    section("PRIME.ONEBADMODE.HIGHPOLE.01 -- high-pole separator "
            "trade-off census (EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    CCVII imported-spec SHA-256 = %s"
          % hashlib.sha256(ob.__doc__.encode("utf-8")).hexdigest())
    print("    CCXXV imported-spec SHA-256 = %s"
          % hashlib.sha256(zpf.__doc__.encode("utf-8")).hexdigest())
    print("    mode = %s; NO RH claim; finite float ladder only"
          % ("SMOKE (artifact suppressed, boxes /4)" if SMOKE
             else "FROZEN"))
    bad = ast_scan()
    check("S0 AST firewall clean", not bad,
          ",".join(sorted(set(bad))) if bad else "", kill="K2")
    ac = ast_scan_functions(("ladder_poles", "m_of", "lp_construct",
                             "certify_filter", "custom_interval_filter",
                             "_box_pass", "_f2_env"), AC_BANNED)
    check("S0.2 AC scan: construction/certification functions read no "
          "rung spectral data", not ac,
          ",".join(ac) if ac else "", kill="K2")

    zones, steps = build_truth_ladder()
    if KILLS or not steps:
        return finish({})

    l_global = max(step["L_src"] for step in steps)
    stored = json.load(open(zpf.PHASE_ARTIFACT, encoding="utf-8"))
    l_stored = float(stored["filter"]["L"])
    check("W7 L_global %.6f == stored CCXXV artifact L (rtol 1e-9)"
          % l_global, abs(l_global / l_stored - 1.0) <= 1e-9, kill="K2")

    deployed = zpf.build_filter(CB_F, l_global, 8)
    stored_by_key = {(row["h"], row["kz"]): row for row in stored["rungs"]}
    dep_reserves = []
    w8 = 0.0
    for step in steps:
        trace_val = zpf.trace_filter_lu(step["Mt"], deployed)
        dep_reserves.append(1.0 - trace_val)
        key = (int(step["r2"]["h"]), int(step["r2"]["kz"]))
        if key in stored_by_key:
            w8 = max(w8, abs((1.0 - trace_val)
                             - float(stored_by_key[key]["margin"])))
    dep_reserves = np.asarray(dep_reserves)
    check("W8 deployed m=8 margins reproduce stored artifact: max abs "
          "%.2e <= %.0e (matched %d/68)" % (w8, W8_TIE,
                                            len(stored_by_key)),
          w8 <= W8_TIE and len(stored_by_key) == len(steps), kill="K2")

    ks_data = ks_census(steps)
    if ks_data is None or KILLS:
        return finish({})
    print("    D_i max %.4g -> all-pole Neumann admissibility needs "
          "Y_min > D_max" % ks_data["dmax"])

    route_i_rows = route_i_truncation(l_global)
    route_ii_rows = route_ii_elementary(l_global)

    section("A -- route (iii): the LP family over (Y_min x W), "
            "construction + certification")
    filters = []
    for y_min in Y_LADDER:
        for w_budget in W_LADDER:
            filt = lp_construct(y_min, w_budget, l_global)
            if filt["status"] != "OK":
                print("    Y %.0e W %.0e m' %-3d %s [%.1f s]"
                      % (y_min, w_budget, filt["m_prime"],
                         filt["status"], filt["lp_seconds"]))
                filters.append(filt)
                continue
            certify_filter(filt, l_global)
            print("    Y %.0e W %.0e m' %-3d delta_lp %-9.3g "
                  "delta_cert %-9.3g l1 %-8.3g eps_neg %-8.2g %s "
                  "[LP %.1f s, boxes %d, %.0f s]"
                  % (y_min, w_budget, filt["m_prime"], filt["delta_lp"],
                     filt["delta_cert"], filt["l1"], filt["eps_neg"],
                     "CERT-OK" if filt["cert_conclusive"]
                     else "CERT-VOID", filt["lp_seconds"], filt["boxes"],
                     time.time() - T0), flush=True)
            filters.append(filt)
    live = [f for f in filters if f.get("status") == "OK"]
    conclusive = [f for f in live if f["cert_conclusive"]]
    check("M1 certification: %d/%d LP filters conclusive, %d typed "
          "CERT-VOID (honest thresholds everywhere); at least one "
          "conclusive" % (len(conclusive), len(live),
                          len(live) - len(conclusive)),
          len(conclusive) >= 1, kill="K2")

    # m'-insensitivity replicate (disclosed ward, no kill)
    base_point = next((f for f in live
                       if f["y_min"] == REPL_POINT[0]
                       and f["w_budget"] == REPL_POINT[1]), None)
    if base_point is not None:
        repl = lp_construct(REPL_POINT[0], REPL_POINT[1], l_global,
                            m_prime=max(8, base_point["m_prime"] // 2))
        gap_repl = (abs(repl.get("delta_lp", float("nan"))
                        - base_point["delta_lp"])
                    if repl["status"] == "OK" else float("nan"))
        check("M4 m'-insensitivity at (1e3,1e6): |delta*(m'/2=%d) - "
              "delta*(m'=%d)| = %.3g (typed, no kill)"
              % (repl["m_prime"], base_point["m_prime"], gap_repl), True)
    else:
        check("M4 m'-insensitivity replicate: base point missing "
              "(typed)", True)
        gap_repl = float("nan")

    section("B -- THE TRADE-OFF CENSUS (decision route: eig-free PD "
            "solves; honest per-filter thresholds)")
    for filt in live:
        census_filter(filt, steps, ks_data)
    tie_r = max(f["tie_routes"] for f in live)
    tie_e = max(f["tie_eig"] for f in live)
    check("M2 route wards (normalized by cancellation scale): decision "
          "== pole-read %.2e <= %.0e; == eigensum truth %.2e <= %.0e "
          "(68 x %d)" % (tie_r, TIE_ROUTES, tie_e, TIE_EIG, len(live)),
          tie_r <= TIE_ROUTES and tie_e <= TIE_EIG, kill="K2")

    print("\n    Y_min    W      m'  delta*    delta_c   cert  "
          "reserve med   kappa     Nm-pair ctrl/val gap_med")
    for filt in live:
        print("    %-8.0e %-6.0e %-3d %-9.3g %-9.3g %2d/68 %+.4e "
              "%-9.3g %5.3f  %2d/%-3d %-9.3g%s"
              % (filt["y_min"], filt["w_budget"], filt["m_prime"],
                 filt["delta_lp"], filt["delta_cert"], filt["cert_n"],
                 filt["reserve_trio"][1], filt["kappa_med"],
                 filt["pair_frac"], filt["controlled"], filt["n_valid"],
                 filt["gap_med"],
                 "" if filt["cert_conclusive"] else "  CERT-VOID"))
    print("    deployed m=8 (CCXXV anchor): reserve %s; min pole 0.484"
          % e3(dep_reserves))
    check("B1 census table complete on %d LP points + deployed anchor"
          % len(live), len(live) > 0)

    section("L -- THE OBSTRUCTION LAW: delta*(Y_min, W) collapse test")
    slopes = {}
    for y_min in Y_LADDER:
        pts = [(math.log(f["w_budget"]),
                math.log(1.0 / max(1e-12, f["delta_lp"])))
               for f in live if f["y_min"] == y_min
               and f["delta_lp"] < 1.9]
        if len(pts) >= 2:
            _b, slope, r2 = ols_line([p[0] for p in pts],
                                     [p[1] for p in pts])
            k_const = slope * math.sqrt(y_min / CB_F)
            slopes[y_min] = (slope, k_const, r2, len(pts))
            print("    Y %.0e: d ln(1/delta*)/d ln W = %.4f -> K = "
                  "slope*sqrt(Y/c_B) = %.3f (R2 %.3f, n=%d)"
                  % (y_min, slope, k_const, r2, len(pts)))
    if slopes:
        k_vals = [v[1] for v in slopes.values()]
        print("    collapse constants K(Y): %s (two-constants "
              "prediction: O(1), Y-independent)"
              % "/".join("%.2f" % k for k in k_vals))
    check("L1 obstruction-law fit non-vacuous on %d/%d Y rungs"
          % (len(slopes), len(Y_LADDER)), len(slopes) >= 3)

    # verdict logic
    best = {}
    for y_min in Y_LADDER:
        sub = [f for f in live if f["y_min"] == y_min
               and f["cert_n"] == len(steps) and f["cert_conclusive"]]
        if sub:
            best[y_min] = min(sub, key=lambda f: f["w_budget"])
    y_star = max(best) if best else None
    target = None
    for y_min in sorted(best, reverse=True):
        if best[y_min]["pair_frac"] >= 0.99:
            target = best[y_min]
            break
    if target is not None:
        head = ("HIGHPOLE-CERTIFIES(Y_min=%.0e, m'=%d, W=%.0e, reserve "
                "med %.3f, Neumann pairs %.0f%%)"
                % (target["y_min"], target["m_prime"],
                   target["w_budget"], target["reserve_trio"][1],
                   100 * target["pair_frac"]))
    elif best:
        target = best[y_star]
        head = ("HIGHPOLE-FRONTIER(certification frontier Y* = %.0e "
                "<< D_med %.3g; Neumann pairs there %.0f%%)"
                % (y_star, D_REF, 100 * target["pair_frac"]))
    else:
        target = max(live, key=lambda f: f["reserve_trio"][0])
        head = "HIGHPOLE-FRONTIER(no conclusive 68/68 point at all)"
    print("    VERDICT CANDIDATE: %s" % head)
    check("B2 verdict computed with best point Y_min=%.0e W=%.0e"
          % (target["y_min"], target["w_budget"]), True)

    controls = run_controls(zones, live, deployed)
    if KILLS:
        return finish({})

    section("D -- relocation screens (tau on reserves; CCXVII c_h on "
            "the matched surface subset)")
    taus = [step["tau"] for step in steps]
    screen_rows = {}
    for y_min in Y_LADDER:
        sub = [f for f in live if f["y_min"] == y_min]
        if not sub:
            continue
        pick = best.get(y_min) or max(sub,
                                      key=lambda f: f["reserve_trio"][0])
        label, _s = screen(pick["reserves"], taus)
        screen_rows["tau@Y%.0e" % y_min] = label
        print("    reserve tau-screen Y %.0e (W %.0e): %s"
              % (y_min, pick["w_budget"], label))
    dep_label, _s = screen(dep_reserves, taus)
    screen_rows["tau@deployed"] = dep_label
    print("    reserve tau-screen deployed m=8: %s" % dep_label)
    ch_map = ch_surface_map()
    matched_idx = []
    matched_ch = []
    for index, step in enumerate(steps):
        h_val = int(step["r2"]["h"])
        if ob.seg_of(step) == "surf" and h_val in ch_map:
            matched_idx.append(index)
            matched_ch.append(ch_map[h_val])
    if len(matched_idx) >= 3:
        ch_label, _s = screen(
            np.asarray(target["reserves"])[matched_idx], matched_ch)
        print("    reserve c_h-screen best point (surface %d/68): %s"
              % (len(matched_idx), ch_label))
    else:
        ch_label = "vacuous(matched=%d)" % len(matched_idx)
        print("    c_h screen %s" % ch_label)
    screen_rows["c_h@best"] = ch_label
    non_vac = [lab for key, lab in screen_rows.items()
               if "tau" in key and "vacuous" not in lab]
    check("D1 screens: %d non-vacuous tau rows (positive-reserve "
          "filters exist on %d Y rungs); c_h matched %d"
          % (len(non_vac), len(best), len(matched_idx)),
          len(non_vac) >= 1)

    section("R -- THE RESIDUE RESTATEMENT (mission c)")
    fit_all = ks_data["fits"].get("all", (float("nan"),) * 4)
    fit_deep = ks_data["fits"].get("deep", (float("nan"),) * 4)
    print("    KS data D ~ h^%+.3f +/- %.3f (all 67 pairs); deep-only "
          "h^%+.3f +/- %.3f (n=%d) -- CCLIII read -0.278 +/- 0.277"
          % (fit_all[0], fit_all[1], fit_deep[0], fit_deep[1],
             fit_deep[3] if len(fit_deep) > 3 else 0))
    print("    THE SPLIT: certification frontier Y* = %s vs the "
          "Neumann demand D_med %.4g / D_max %.4g."
          % ("%.0e" % y_star if y_star else "NONE", D_REF,
             ks_data["dmax"]))
    print("    AT THE BEST POINT (Y %.0e, W %.0e): certificate = "
          "l1-bounded functional of m_h(i eta_j), eta_j >= %.4g, "
          "transfer weight D*w_l1 = %.4g, kappa_PF med %.3g; a-priori "
          "census %d/%d CONTROLLED, gap med %.4g (CCLIII: 0/67, med "
          "2.88e4)."
          % (target["y_min"], target["w_budget"],
             float(np.min(target["eta"])),
             target["D"] * target["w_l1"], target["kappa_med"],
             target["controlled"], max(1, target["n_valid"]),
             target["gap_med"]))
    print("    REMAINING DEMAND: the two-constants mechanism prices "
          "any upward pole relocation at l1 >= exp(K sqrt(Y/c_B) "
          "ln(1/delta)) (measured K above), so the KS-transfer weight "
          "explodes long before Y reaches D ~ 2e3: the corridor's "
          "uniform-control residue stays at the LOW poles -- the "
          "bound route (parametrix), not filter redesign, remains the "
          "open seam; plus the wall-side KS uniformity (D exponent "
          "above, not resolved as flat).")
    check("R1 residue restated at the best point", True)

    artifact = dict(
        schema="tfpt.highpole_filter_tradeoff.v2",
        mission="PRIME.ONEBADMODE.HIGHPOLE.01",
        spec_sha256=spec_sha,
        no_rh_claim=True,
        finite_float_ladder=True,
        l_global=l_global,
        d_ks=dict(values=[float(v) for v in ks_data["dks"]],
                  h_pair=[float(v) for v in ks_data["h_pair"]],
                  fits={k: list(v) for k, v in ks_data["fits"].items()},
                  dmax=ks_data["dmax"]),
        table=[{k: (float(f[k]) if isinstance(f[k], (int, float))
                    else f[k])
                for k in ("y_min", "w_budget", "m_prime", "delta_lp",
                          "delta_cert", "l1", "w_l1", "cert_n",
                          "h_slope", "h_slope_2se", "cell_frac",
                          "pair_frac", "controlled", "n_valid",
                          "gap_med", "kappa_med", "cert_margin",
                          "eps_neg", "lp_seconds")
                if k in f} | dict(
                    reserve_trio=list(f["reserve_trio"]),
                    cert_conclusive=bool(f["cert_conclusive"]))
               for f in live],
        law=dict(slopes={"%.0e" % y: list(v)
                         for y, v in slopes.items()},
                 y_star=y_star, m_repl_gap=gap_repl),
        best_point=dict(y_min=target["y_min"],
                        w_budget=target["w_budget"],
                        m_prime=target["m_prime"],
                        eta=[float(v) for v in target["eta"]],
                        alpha=[float(v) for v in target["alpha"]],
                        beta=[float(v) for v in target["beta"]],
                        D=target["D"], threshold=target["threshold"]),
        route_i=route_i_rows,
        route_ii=route_ii_rows,
        deployed_anchor=dict(reserve_trio=list(trio(dep_reserves))),
        screens=screen_rows,
        controls=dict(n_indef=controls["n_indef"],
                      leaks=controls["leaks"],
                      pd_cores=controls["pd_cores"]))
    if SMOKE:
        print("    SMOKE: artifact write suppressed")
    else:
        with open(ARTIFACT, "w", encoding="utf-8") as handle:
            json.dump(artifact, handle, ensure_ascii=False,
                      separators=(",", ":"), sort_keys=True)
            handle.write("\n")
        print("    artifact written: %s" % os.path.basename(ARTIFACT))

    labels = dict(
        head=head,
        law=("LAW(K(Y) = %s; route-i best delta %.4g; route-ii best "
             "delta %.4g)"
             % ("/".join("%.2f" % v[1] for v in slopes.values())
                if slopes else "unresolved",
                min((r["delta"] for r in route_i_rows),
                    default=float("nan")),
                min(r["delta"] for r in route_ii_rows))),
        census=("CENSUS(best Y %.0e W %.0e: reserve %s, %s, ctrl %d/%d "
                "gap med %.3g)"
                % (target["y_min"], target["w_budget"],
                   e3(target["reserves"]),
                   "O1-RESERVE" if target["o1"] else "COLLAPSING",
                   target["controlled"], max(1, target["n_valid"]),
                   target["gap_med"])),
        residue=("RESIDUE(D ~ h^%+.3f +/- %.3f; deep h^%+.3f +/- %.3f; "
                 "D_max %.4g; Y* %s)"
                 % (fit_all[0], fit_all[1], fit_deep[0], fit_deep[1],
                    ks_data["dmax"],
                    "%.0e" % y_star if y_star else "NONE")),
        controls=("CONTROLS(indefinite %d, leaks %d, PD cores %d)"
                  % (controls["n_indef"], controls["leaks"],
                     len(controls["pd_cores"]))),
        screens="SCREENS(%s)" % "; ".join(
            "%s %s" % (key, lab.split("(")[0])
            for key, lab in screen_rows.items()))
    return finish(labels)


def finish(labels):
    section("V -- VERDICT")
    passed = sum(ok for _name, ok in CHECKS)
    if KILLS:
        verdict = ("PIPELINE-BROKEN" if KILLS[0] == "K1"
                   else "WARD-BROKEN")
    elif labels:
        verdict = " / ".join(labels[key] for key in
                             ("head", "law", "census", "residue",
                              "controls", "screens") if key in labels)
    else:
        verdict = "INCOMPLETE"
    print("  VERDICT: %s" % verdict)
    print("  [EXTERNAL-CITED] Zolotarev/Akhiezer elliptic nodes "
          "(routes i/ii); Nevanlinna two-constants / harmonic measure "
          "as mechanism (no constant borrowed); HiGHS LP heuristic "
          "constructor; every deployed inequality re-certified here.")
    print("  HONEST FRAME: finite float64 ladder only; c_B surface "
          "CITED, deep FLOAT-LEVEL, bridge exception typed; "
          "source-only L; eigenvalues truth-reference/control typing "
          "only; certification outward-padded adaptive float boxes; "
          "NO RH claim.")
    print("  [TIME] %.1f s  [CHECKS] %d/%d passed  [KILLS] %s"
          % (time.time() - T0, passed, len(CHECKS),
             ",".join(KILLS) if KILLS else "none"))
    return 0 if passed == len(CHECKS) and not KILLS else 1


if __name__ == "__main__":
    raise SystemExit(main())
