#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sigma_stress_battery_probe -- PRIME.ONEBADMODE.KS.SIGMA.STRESS.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE ADVERSARIAL FRONT ON THE 0.665.  CCLXI (zolotarev_ks_dual_probe)
measured that the truth envelope of the Schur quotient

    sigma = a_1^2 [J_B^-1]_11 / b_1

in the Lanczos coordinates of the normalized wall (M~, e_0) is <= 0.605
on the 68-step deployed ladder, and that the reported-only cap
sigma <= 0.665 (= 0.6046 * 1.1, arithmetic margin, MECHANISM-IMPORTING
flagged) closes the KS.DUAL extremal class numerically (best 0.7264 < 1
with the cap, sup 2.2578 without).  Before anyone invests months
deriving sigma <= 0.665 source-only, this probe tries HARD to break it
everywhere the DEPLOYED CONSTRUCTION is legal:

 (a) THE FULL-LADDER MEASUREMENT: sigma on every registered step
     (40 surface + 1 bridge + 27 deep to the table limit h = 2854);
     envelope statistics min/med/max per segment, the h-trend with
     2SE, and the anatomy of the maximum (which step, which geometry).
 (b) THE ADVERSARIAL SWEEP: sigma across WALL-LEGAL geometries the
     registered ladder does not use (families F0-F5 below), plus the
     closing threshold t* measured from the CCLXI machinery itself
     (the cap-curve: sup tr R over the frozen class C_KS as a function
     of the sigma-cap), and the distance of the adversarial maximum
     to t*.
 (c) THE REGISTRATION (HALFGAP pattern): SIGMA_ENV frozen from a
     DECLARED choice subset with a declared safety factor and the
     verbatim no-tuning clause; blind test on the held-out rungs
     (the registered deep block + the F5 depth extension).
 (d) THE SCREENS: tau / c_h relocation screens on sigma AND on the
     margins (0.665 - sigma) and (t* - sigma); the world census
     (sigma in the falsifying worlds).
 (e) GATES: Lanczos wards (CCLXI B2-B5 verbatim + sigma-envelope
     reproduction), controls-must-fire, anti-circularity (sigma is
     computed from the construction FORWARD -- assembled wall matrix
     -> Lanczos -> Schur quotient; no read, reserve or margin
     identifier in the sigma/builder functions).

WALL-LEGALITY (frozen definition).  A geometry is wall-legal iff the
deployed pipeline itself admits it: the rung builds (Lanczos chain of
the folded positive measure completes, be > 0), core_ok (the eight
CORE_J folds present), negA = 0 (the wall target holds), lamS > 0 and
tau > 0 (the deployed step admission ob.make_steps applies verbatim),
and zol.assemble_step returns status OK.  Steps are formed in TWO
wall-legal ways: (i) consecutive pairs in (h, kz) order WITHIN a
family (the deployed chain construction), and (ii) one bridge step
per family rung from its nearest registered truth predecessor
(largest registered h <= rung h, else the smallest) -- the deployed
bridge pattern generalized; refusals are censused.  Every family
below only moves knobs the deployed family exposes:

 F0 SURFACE-OFFLADDER: frame-A zones (core.frame_a_zones, verbatim)
    with h in (H_LADDER_MAX, HCAP] = (900, 1450] -- constructible by
    core.build_window, excluded from the registered ladder only by
    the H_LADDER_MAX cut.  Declared pick: sorted by h descending,
    first F0_CAP = 12, then re-sorted ascending for steps.
 F1 DEEP-OFFLADDER-KZ: the deep-frame enumeration kz in [2, 400) on
    the DEPLOYED 4e6 table (ob.ext_frame / ob.build_rung("deep", kz)
    verbatim) with hz in F1_BAND = [64, 2900], EXCLUDING the
    registered deep census and the registered surface zones.
    Declared pick: qualifying kz sorted ascending, uniform stride to
    at most F1_CAP = 14.
 F2 DENSITY (fold count): nu in F2_NU = (5, 6, 8) -- NU_MAIN = 4 is
    the cited T105 admissibility FLOOR, so denser grids nu > 4 are
    legal; D_k = 0.5 G[kz] / nu, M = ceil(alpha/D_k - 1e-9) + 1
    rounded even (deployed formula).  Declared kz: the F2_NKZ = 4
    registered deep-census zones with the smallest h.
 F4 OFF-ANCHOR ALPHA (boundary window shape): alpha_mid =
    (U[kz] + U[kz+1]) / 2 -- the window boundary 2 alpha falls
    BETWEEN atom positions, changing the boundary tent truncation;
    D from the anchor gap G[kz] at nu = 4 (deployed formula).
    Declared kz: the F4_NKZ = 6 registered census zones with the
    smallest h.
 F5 DEPTH EXTENSION: the deployed table generator at TAB2 = 1.6e7
    (prefix warded bitwise against the 4e6 EXT arrays, the
    deep_blind_holdout W1/W2 pattern); newly reachable frames = NOT
    in the registered census AND (hz in (2900, H5_CAP] with X <= TAB2,
    or X in (4e6, TAB2] with hz in [128, H5_CAP]), H5_CAP = 4200
    (declared cost cap; the census also prints the maximum reachable
    hz WITHOUT the cost cap and the h^3 flops / h^2 memory cost law).
    Declared pick: the N5 = 4 newly reachable frames with the largest
    hz <= H5_CAP; chain steps among them plus their anchor bridges
    (for hz > 2854 the anchor is the deepest registered deep rung).
 (F3, fold count by direct M scaling, is the SAME knob as F2 --
  D = 2 alpha / M -- and is not duplicated; disclosed.)

THE THRESHOLD t*.  No source artifact for t* exists (checked: the
concurrent probes C/D address the reserve sum rule and the res(h)
carriers, not sigma), so t* is MEASURED here with the CCLXI machinery
verbatim: the class C_KS is re-frozen from the 68 truth steps (box
SHA-256 must reproduce CCLXI's 224a2737..., ward), and for each cap in
CAPS = (0.665, 0.75, 0.85, 0.92, 0.96, 0.99) the capped optimization
(CCLXI O3 sig_con verbatim, reduced declared budget CAP_MS = 10 /
CAP_DE = 80) measures sup tr R (cap).  Every sup is a NUMERIC LOWER
BOUND of the true supremum, hence:
    t*_hi = smallest cap with measured sup >= 1  (the route PROVABLY
            fails to close at that cap and above),
    t*_lo = largest cap with measured sup < 1    (closing is only
            UNVERIFIED-TO-FAIL there, not certified),
    t*_num = linear interpolation of the crossing sup = 1 (reported).
An uncapped row (same budget) anchors the curve against CCLXI's 2.2578.

THE KILL CRITERION (stated up front, frozen): ONE wall-legal step with
sigma >= t*_hi KILLS the KS.DUAL closing route -- the class would need
a cap that provably does not close.  sigma >= 0.665 anywhere wall-legal
BREAKS the registered envelope (the derivation target moves) even if
the route survives with a wider cap; both distances are reported.

THE REGISTRATION (HALFGAP no-adjustment clause, verbatim pattern):
SIGMA_ENV := (max sigma over the DECLARED CHOICE SET) * (1 + SAFETY),
SAFETY = 0.10 (the CCLXI arithmetic-margin convention, declared).
CHOICE SET = the 40 surface steps + the bridge + families F0, F1, F2,
F4.  HOLDOUT (scored blind, no refits, no constant moves, no
exclusions) = the 27 registered deep steps + the F5 extension steps.
A later miss on any rung -- holdout or otherwise -- is a FAIL of the
registered envelope, full stop; it must NOT be repaired by adjusting
the constant, by reweighting, or by excluding rungs.  A failed
registration is a first-class result.  Registry hash: SHA-256 over the
lines "family:kz:h:sigma(%.12e)" of the choice set plus the ENV line.

MEMBERSHIP / CONTROLS (controls-must-fire).
 C1 the smooth world violates the wall target (negA > 0) on every
    surface rung (kill CONTROL-SILENT if silent).
 C2 class-exclusion census of both falsifying worlds (CCLXI X2
    verbatim, majority bar; kill CONTROL-SILENT if silent).
 O0 OPT-POWER: on the declared control box (b_1 extended to -1) the
    optimizer must reach tr R >= 1 (kill CONTROL-SILENT if silent) --
    otherwise the cap-curve cannot be trusted.
 WORLD SIGMA CENSUS (reported, never a kill): sigma of the aligned
    falsifying-world matrices (CCLXI alignment verbatim), with the
    honest note that those worlds leave the class anyway (CCLXI:
    excluders B_floor / KS_wall), so a sigma-cap is not what excludes
    them.

WARDS (kill -> WARD-BROKEN / REPRO-BROKEN unless noted).
 W  ladder rebuilt read-only (42 surface rungs, 68 = 40 + 1 + 27
    steps); CCXXV global m=8 filter rebuilt from source-only L and
    warded against the stored artifact; LU trace / margin vs the
    stored 68x8 artifact; eigen == LU; T5 REPRO reserve med 0.9195 /
    min 2.730e-2 (CCXLVII).
 B  CCLXI B1-B5 verbatim on all 68 steps AND on every sweep step:
    Lanczos exists; b_1 == M[0,0]; a_1 == ||M[1:,0]||;
    lambda_min(J_B) == lamB1; m(0) gap == 1; the sigma identity
    b_1 (1 - sigma) == gap.
 SR SIGMA-REPRO: the truth sigma envelope reproduces CCLXI
    (max 0.6046, rtol 2e-3) and 0.6046 * 1.1 = 0.665 is re-printed as
    the arithmetic it is.
 G  class re-freeze reproduces CCLXI's box SHA-256 prefix 224a2737
    (kill REPRO-BROKEN -- the t* machinery would not be CCLXI's).
 BW BUILDER ward: the parametric rung builder at the DEPLOYED
    parameters (alpha = U[kz], nu = 4, deployed table) reproduces
    ob.build_rung("deep", kz) on BW_N = 3 declared census zones
    (tau, lamS, h exact to 1e-12 rel).
 X5 TAB2 prefix ward: the 1.6e7 table arrays agree BITWISE with the
    deployed 4e6 EXT arrays on the overlap.

ANTI-CIRCULARITY.  sigma is computed from the construction forward:
assembled wall matrix -> jacobi_form -> sigma_quotient; AST scan
proves the sigma / builder functions contain no read identifier
(reserve, margin, trace_r, lu_read, scalar_r, trace_filter_lu); the
class functions carry the CCLXI ban list verbatim; the optimizer never
sees h; the prime/zero-oracle firewall scan applies to the whole file.
The number 0.665 enters ONLY as a comparison threshold and as the
first cap of the declared grid -- never as an input to any sigma.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward -> WARD-BROKEN;
K3 reproduction -> REPRO-BROKEN; K4 control silent -> CONTROL-SILENT.

VERDICT (frozen enum, dominance order):
 SIGMA-KILL(adversarial max >= t*_hi: a wall-legal configuration
   provably kills the KS.DUAL closing route)
 SIGMA-BREACH(max wall-legal sigma >= 0.665 but < t*_hi: the
   registered envelope breaks; distance to t* reported)
 SIGMA-SURVIVES(max wall-legal sigma < 0.665; distances to 0.665 and
   t* reported)
plus typed tags REGISTERED(SIGMA_ENV, blind k/N), SCREENS(relocation
seats or none), WORLDS(census), AMENDMENTS.  Every enum is a finite
float64 statement about the deployed construction family and the
frozen class; NEVER an all-h statement, NEVER an RH claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE = 2e-9;
PF_TIE = 2e-8; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7; REPRO_RTOL =
5e-2; RES_MED_REF = 0.9195; RES_MIN_REF = 2.730e-2; SIGMA_MAX_REF =
0.6046; SIGMA_RTOL = 2e-3; ENV_REF = 0.665; MARGIN_FRAC = 0.10;
FEAS_TOL = 1e-9; BOX_SHA_REF = "224a2737"; F0_CAP = 12; F1_BAND =
(64, 2900); F1_CAP = 14; F2_NU = (5, 6, 8); F2_NKZ = 4; F4_NKZ = 6;
TAB2 = 16_000_000; KZ2_MAX = 800; H5_CAP = 4200; N5 = 4; SAFETY =
0.10; CAPS = (0.665, 0.75, 0.85, 0.92, 0.96, 0.99); CAP_MS = 10;
CAP_DE = 80; O0_MS = 8; O0_DE = 40; OPT_SEED = 20260812 (inherited,
declared); PEN_W = 1e4; SLSQP_MAXIT = 150; DE_POP = 20; SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; CTRL_MAJORITY = 0.5; BW_N = 3; BW_TIE =
1e-12; runtime cap 25 min.  Smoke: 10 contiguous surface rungs + 3
lowest deep; F0_CAP 2, F1_CAP 3, F2_NU (6,) x 1 kz, F4 1 kz, F5
SKIPPED (typed), CAPS (0.665, 0.92), CAP_MS 4, CAP_DE 20.

SMOKE DISCLOSURE (2026-08-12, two smoke passes before the freeze; no
bar, control, screen, enum or success rule was changed after the
smokes; SPEC SHA moves with this text, disclosed).
DESIGN NOTES DECLARED PRE-SMOKE: (i) T5 REPRO, the SIGMA-REPRO max
and the G box-SHA ward decide only on the frozen ladder and are
smoke-bypassed by design (the smoke subset ladder is not the 68-step
artifact ladder -- CCLXI's identical smoke phenomenon).  (ii) the
world sigma census reports b_1 > 0 and b_1 <= 0 counts separately
(aligned world matrices can have nonpositive pivots).
 SMOKE-1 (12.3 s) FAILED honestly at ADV1 (K1): within-family
 consecutive-pair steps alone starve the small smoke families (one
 wall-legal step total; the F0 pair was step-refused, single-rung
 families cannot pair).  AMENDMENT-1 (the only post-smoke code
 change, structural, no bar/enum/screen touched): steps are formed
 in the TWO wall-legal ways now frozen above -- within-family chain
 pairs PLUS one bridge step per family rung from its nearest
 registered truth predecessor (the deployed bridge pattern
 generalized); refusals are censused per family.
 SMOKE-2 (33.0 s) ran 34/34 GREEN, no kills.  Honest readings (not
 bars): translation wards at machine precision (ladder B2
 2.1e-18, B3 9.0e-14, B4 2.0e-15, B5 2.0e-16; sweep B2 6.2e-18, B3
 3.2e-14, B4 2.8e-15, B5 2.2e-15); builder ward exact 0.0e0 on all
 three zones; smoke sweep 6 wall-legal steps (F0 1, F1 3, F2 1,
 F4 1), sigma max 0.4153 (F1 kz 105 bridge), all < 0.665; the smoke
 subset's fake bridge step carried sigma 0.5612 and reserve -3.85
 and drove the disclosed smoke B-floor widening to 0.0053 (bypassed
 wards as declared; smoke box SHA d88d7037 != 224a2737 exactly as
 CCLXI's smoke box); smoke cap-curve on the SMOKE class (not the
 frozen class): 0.665 -> 0.9687, 0.92 -> 1.1460, smoke t*_num 0.71;
 O0 control fired at 3.0569; C1 fired 10/10; X2 fired on both
 worlds (smooth 4/4 out, all b_1 <= 0; scramble 2/2 out, one
 aligned scramble rung showed sigma 1.007 > 0.665 -- reported,
 meaningless as constraint evidence since the worlds leave the
 class); all six screens PASS on the smoke subset.  No further code
 path, bar or rule was changed after SMOKE-2; the frozen run below
 is the run of record.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXIX line prepended to experiments/next.txt AFTER the frozen
summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder),
zolotarev_phase_filter_probe (CCXXV filter + artifact),
zolotarev_ks_dual_probe (CCLXI class + sigma machinery, reproduced
verbatim, cited), euler_phase_identity_probe (CCXVII c_h),
deep_blind_holdout_probe (holdout pattern + table-extension wards,
cited), halfgap_registration_probe (registration pattern, cited),
v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_stress_battery_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_stress_battery_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla
from scipy import optimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
PF_TIE = 2.0e-8
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
REPRO_RTOL = 5.0e-2
RES_MED_REF = 0.9195
RES_MIN_REF = 2.730e-2
SIGMA_MAX_REF = 0.6046
SIGMA_RTOL = 2.0e-3
ENV_REF = 0.665
MARGIN_FRAC = 0.10
FEAS_TOL = 1.0e-9
BOX_SHA_REF = "224a2737"
F0_CAP = 12
F1_BAND = (64, 2900)
F1_CAP = 14
F2_NU = (5, 6, 8)
F2_NKZ = 4
F4_NKZ = 6
TAB2 = 16_000_000
KZ2_MAX = 800
H5_CAP = 4200
N5 = 4
SAFETY = 0.10
CAPS = (0.665, 0.75, 0.85, 0.92, 0.96, 0.99)
CAP_MS = 10
CAP_DE = 80
O0_MS = 8
O0_DE = 40
OPT_SEED = 20260812
PEN_W = 1.0e4
SLSQP_MAXIT = 150
DE_POP = 20
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_MAJORITY = 0.5
BW_N = 3
BW_TIE = 1.0e-12
OPT_CTRL_B1 = -1.0
OPT_CTRL_BAR = 1.0
CB_F = float(ob.CB_CITED)
SCRAMBLE_SEED = ob.SCR_SEED
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
CLASS_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h")
READ_BANNED = ("reserve", "margin", "trace_r", "trace_R", "lu_read",
               "scalar_r", "trace_filter_lu")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(values):
    v = np.asarray(values, float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return (float("nan"),) * 3
    return (float(np.min(v)), float(np.median(v)), float(np.max(v)))


def e3(values):
    return "%.4g/%.4g/%.4g" % trio(values)


def linfit(x, y):
    """OLS y = a + s x (CCLIII verbatim); returns s, 2SE, R^2, a."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan"), float(ym)
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * xm
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, 2.0 * se, r2, a


def screen(values, scales, label):
    """CCXLVII relocation screen, bars inherited verbatim."""
    v = np.asarray(values, float)
    s = np.asarray(scales, float)
    pos = (v > 0.0) & (s > 0.0) & np.isfinite(v) & np.isfinite(s)
    if int(np.sum(pos)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(pos))),
                "VAC")
    slope, _2se, r2, _a = linfit(np.log(s[pos]), np.log(v[pos]))
    verd = ("PASS" if abs(slope) <= SLOPE_PASS
            else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope=%+.3f,R2=%.3f,%d excl)"
            % (label, verd, slope, r2, int(np.sum(~pos))), verd)


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# =========================================== Jacobi form (CCLXI/CCLIII)
def jacobi_form(matrix):
    if not np.all(np.isfinite(matrix)):
        return None
    n = NDIM
    qq = np.zeros((n, n))
    qq[0, 0] = 1.0
    a = np.zeros(n - 1)
    b = np.zeros(n)
    for k in range(n):
        z = matrix @ qq[:, k]
        b[k] = float(qq[:, k] @ z)
        z = z - b[k] * qq[:, k]
        if k > 0:
            z = z - a[k - 1] * qq[:, k - 1]
        for _ in range(2):
            z = z - qq[:, :k + 1] @ (qq[:, :k + 1].T @ z)
        if k == n - 1:
            break
        nz = float(np.linalg.norm(z))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b, qq


# ============================== class / sigma functions (AC-scanned)
def theta_matrices(theta):
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def ks_wall_functionals(theta, cls):
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    ll = cls["L"]
    aa = 4.0 * ad / ll
    bb = (4.0 * bd - 2.0 * ll) / ll
    ks = float(np.sum((aa - 1.0) ** 2) + np.sum(bb ** 2))
    if np.any(aa <= 0.0):
        coef = -float("inf")
    else:
        coef = float(np.sum(np.log(aa))) - 0.5 * math.log(2.0)
    jm, _jb = theta_matrices(theta)
    try:
        evals, evecs = np.linalg.eigh(jm)
    except np.linalg.LinAlgError:
        return ks, coef, float("inf")
    ww = np.maximum(evecs[0, :] ** 2, 1e-300)
    spread = -0.5 * float(np.mean(np.log(NDIM * ww)))
    return ks, coef, spread


def class_slack_vector(theta, cls):
    theta = np.asarray(theta, float)
    lo, hi, wd = cls["lo"], cls["hi"], cls["wd"]
    out = []
    names = []
    for i in range(len(theta)):
        out.append((theta[i] - lo[i]) / wd[i])
        names.append("box_lo[%s]" % cls["coord"][i])
        out.append((hi[i] - theta[i]) / wd[i])
        names.append("box_hi[%s]" % cls["coord"][i])
    ad = theta[NDIM:]
    for k in range(NDIM - 1):
        out.append(ad[k] / wd[NDIM + k])
        names.append("a_pos[a%d]" % (k + 1))
    jm, jb = theta_matrices(theta)
    if np.all(np.isfinite(jm)):
        evj = np.linalg.eigvalsh(jm)
        evb = np.linalg.eigvalsh(jb)
        out.append((float(evb[0]) - cls["cb"]) / cls["cb"])
        names.append("B_floor")
        out.append((cls["L"] - float(evj[-1])) / cls["L"])
        names.append("radius_hi")
        out.append((float(evj[0]) + cls["L"]) / cls["L"])
        names.append("radius_lo")
    else:
        out.extend([-1.0, -1.0, -1.0])
        names.extend(["B_floor", "radius_hi", "radius_lo"])
    ks, coef, spread = ks_wall_functionals(theta, cls)
    out.append((cls["ks_cap"] - ks) / max(cls["ks_cap"], 1.0))
    names.append("KS_wall")
    out.append((coef - cls["coef_lo"]) / cls["coef_w"])
    names.append("COEF_lo")
    out.append((cls["coef_hi"] - coef) / cls["coef_w"])
    names.append("COEF_hi")
    out.append((spread - cls["spr_lo"]) / cls["spr_w"])
    names.append("SPREAD_lo")
    out.append((cls["spr_hi"] - spread) / cls["spr_w"])
    names.append("SPREAD_hi")
    return np.asarray(out, float), names


def sigma_quotient(theta):
    jm, jb = theta_matrices(theta)
    b1 = float(theta[0])
    a1 = float(theta[NDIM])
    if b1 == 0.0:
        return float("inf")
    try:
        e1 = np.zeros(NDIM - 1)
        e1[0] = 1.0
        mb = float(np.linalg.solve(jb, e1)[0])
    except np.linalg.LinAlgError:
        return float("inf")
    return a1 * a1 * mb / b1


def tr_r_of_theta(theta, fdata):
    jm, _jb = theta_matrices(theta)
    if not np.all(np.isfinite(jm)):
        return float("nan")
    evals = np.linalg.eigvalsh(jm)
    return math.fsum(zol.scalar_r(fdata, float(v)) for v in evals)


def sigma_of_matrix(matrix):
    """sigma from the construction FORWARD: wall matrix -> Lanczos ->
    Schur quotient.  Returns (sigma, theta) or (nan, None)."""
    jf = jacobi_form(matrix)
    if jf is None:
        return float("nan"), None
    theta = np.concatenate([jf[1], jf[0]])
    return sigma_quotient(theta), theta


# ====================================================== wall ladder
def build_ladder():
    section("W -- the CCVII/CCXXV wall ladder, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
        print("    SMOKE: %d contiguous surface rungs" % len(zones))
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W2 all surface chains complete",
          all(r is not None for r in surface), kill="K1")
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    if SMOKE:
        census = census[:3]
    deep = []
    for kz, hz in census:
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep
               if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    combined = sorted([r for r in surface
                       if r is not None and r["core_ok"]] + deep_ok,
                      key=lambda r: (r["h"], r["kz"]))
    steps = ob.make_steps(combined)
    for st in steps:
        zol.assemble_step(st)
    steps = [st for st in steps if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in steps]
    ok = (SMOKE or (len(steps) == STEPS_EXP
                    and segs.count("surf") == 40
                    and segs.count("bridge") == 1
                    and segs.count("deep") == 27))
    check("W3 combined steps %d = surface %d + bridge %d + deep %d"
          % (len(steps), segs.count("surf"), segs.count("bridge"),
             segs.count("deep")), ok, kill="K1")
    return zones, steps, census, combined


def get_filter(steps, artifact):
    poles_art = np.asarray([complex(*p)
                            for p in artifact["filter"]["poles"]],
                           complex)
    res_art = np.asarray(artifact["filter"]["residues"], float)
    l_art = float(artifact["filter"]["L"])
    global_l = (l_art if SMOKE
                else max(st["L_src"] for st in steps))
    fdata = zol.build_filter(CB_F, global_l, NDIM)
    dev_l = abs(global_l - l_art) / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fdata["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fdata["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("T1 fixed CCXXV GLOBAL m=8 filter rebuilt: L rel %.2e, "
          "poles %.2e, residues %.2e <= %.0e"
          % (dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    return fdata


def translation(steps, artifact, fdata):
    section("T -- per-step reads vs artifact vs eigen route")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_tr = d_marg = d_eig = 0.0
    n_match = 0
    for idx, st in enumerate(steps):
        key = (int(st["r1"]["h"]), int(st["r1"]["kz"]),
               int(st["r2"]["h"]), int(st["r2"]["kz"]))
        src = stored.get(key)
        trace_lu = zol.trace_filter_lu(st["Mt"], fdata)
        trace_eig = math.fsum(zol.scalar_r(fdata, float(v))
                              for v in st["eigs"])
        d_eig = max(d_eig, abs(trace_lu - trace_eig))
        if src is not None:
            n_match += 1
            d_tr = max(d_tr, abs(trace_lu - float(src["trace_R"])))
            d_marg = max(d_marg, abs((1.0 - trace_lu)
                                     - float(src["margin"])))
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         gap=float(st["gap"]),
                         trace_r=trace_lu,
                         reserve=1.0 - trace_lu))
    check("T2 LU trace_R / margin reproduce the stored artifact on "
          "%d matched steps: %.2e / %.2e <= %.0e"
          % (n_match, d_tr, d_marg, LU_TIE),
          n_match >= 1 and d_tr <= LU_TIE and d_marg <= LU_TIE
          and (SMOKE or n_match == STEPS_EXP), kill="K2")
    check("T3 eigen-route trace == LU trace on all %d steps: max "
          "dev %.2e <= %.0e" % (len(rows), d_eig, PF_TIE),
          d_eig <= PF_TIE, kill="K2")
    reserves = np.asarray([r["reserve"] for r in rows], float)
    med, mn = float(np.median(reserves)), float(np.min(reserves))
    ok_rep = (abs(med / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(mn / RES_MIN_REF - 1.0) <= REPRO_RTOL)
    check("T5 REPRO CCXLVII: reserve med %.4f (ref %.4f), min %.4e "
          "(ref %.3e)" % (med, RES_MED_REF, mn, RES_MIN_REF),
          SMOKE or ok_rep, kill="K3")
    return rows


# ================================ B: Jacobi translation + sigma
def jacobi_wards(rows_like, label, kill="K2"):
    """CCLXI B1-B5 verbatim on a list of dicts with 'step'."""
    d_b1 = d_a1 = d_bfl = d_m0 = d_sig = 0.0
    n_bad = 0
    for row in rows_like:
        st = row["step"]
        sig, theta = sigma_of_matrix(st["Mt"])
        if theta is None:
            n_bad += 1
            row["theta"] = None
            row["sigma"] = float("nan")
            continue
        row["theta"] = theta
        row["sigma"] = sig
        jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(theta[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(theta[NDIM]
                             - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["gap"] - 1.0))
        d_sig = max(d_sig, abs(theta[0] * (1.0 - sig) - row["gap"])
                    / max(1.0, abs(row["gap"])))
    check("B1[%s] Lanczos form exists on all %d steps (breakdowns "
          "%d)" % (label, len(rows_like), n_bad), n_bad == 0,
          kill=kill)
    check("B2[%s] b_1 == M[0,0], a_1 == ||M[1:,0]||: %.2e / %.2e "
          "<= %.0e" % (label, d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill=kill)
    check("B3[%s] lambda_min(J_B) == lamB1: max rel %.2e <= %.0e"
          % (label, d_bfl, TRANSLATE_TIE), d_bfl <= TRANSLATE_TIE,
          kill=kill)
    check("B4[%s] m(0) * gap == 1: max %.2e <= %.0e"
          % (label, d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill=kill)
    check("B5[%s] sigma identity b_1 (1 - sigma) == gap: max rel "
          "%.2e <= %.0e" % (label, d_sig, MZERO_TIE),
          d_sig <= MZERO_TIE, kill=kill)
    return [r for r in rows_like if r["theta"] is not None]


# ================================== G: freeze the class C_KS (CCLXI)
COORD = tuple(["b%d" % (i + 1) for i in range(NDIM)]
              + ["a%d" % (i + 1) for i in range(NDIM - 1)])


def freeze_class(rows, fdata):
    thetas = np.asarray([r["theta"] for r in rows], float)
    t_lo = thetas.min(axis=0)
    t_hi = thetas.max(axis=0)
    width = np.maximum(t_hi - t_lo, 1e-12 * np.maximum(1.0,
                                                       np.abs(t_hi)))
    lo = t_lo - MARGIN_FRAC * width
    hi = t_hi + MARGIN_FRAC * width
    lo[NDIM:] = np.maximum(lo[NDIM:], 0.0)
    cb_use = CB_F
    lamb_min = min(float(np.linalg.eigvalsh(
        theta_matrices(r["theta"])[1])[0]) for r in rows)
    widened = False
    if lamb_min < CB_F:
        cb_use = lamb_min * (1.0 - MARGIN_FRAC)
        widened = True
        print("    WIDENED (disclosed, CCLXI verbatim): measured "
              "lambda_min(J_B) = %.6f < c_B = %.6f -> floor %.6f"
              % (lamb_min, CB_F, cb_use))
    cls = dict(lo=lo, hi=hi, wd=hi - lo, cb=cb_use, L=fdata["L"],
               coord=COORD)
    funcs = np.asarray([ks_wall_functionals(r["theta"], cls)
                        for r in rows], float)
    ks_max = float(np.max(funcs[:, 0]))
    coef_lo_t, coef_hi_t = float(np.min(funcs[:, 1])), \
        float(np.max(funcs[:, 1]))
    spr_lo_t, spr_hi_t = float(np.min(funcs[:, 2])), \
        float(np.max(funcs[:, 2]))
    coef_w = max(coef_hi_t - coef_lo_t, 1e-12)
    spr_w = max(spr_hi_t - spr_lo_t, 1e-12)
    cls.update(ks_cap=ks_max * (1.0 + MARGIN_FRAC),
               coef_lo=coef_lo_t - MARGIN_FRAC * coef_w,
               coef_hi=coef_hi_t + MARGIN_FRAC * coef_w,
               coef_w=coef_w,
               spr_lo=spr_lo_t - MARGIN_FRAC * spr_w,
               spr_hi=spr_hi_t + MARGIN_FRAC * spr_w,
               spr_w=spr_w)
    frozen = np.concatenate([lo, hi,
                             [cls["cb"], cls["L"], cls["ks_cap"],
                              cls["coef_lo"], cls["coef_hi"],
                              cls["spr_lo"], cls["spr_hi"]]])
    box_sha = hashlib.sha256(frozen.tobytes()).hexdigest()
    cls["box_sha"] = box_sha
    cls["widened"] = widened
    check("G1 class C_KS re-frozen; box SHA-256 %s reproduces "
          "CCLXI %s..." % (box_sha[:16], BOX_SHA_REF),
          SMOKE or box_sha.startswith(BOX_SHA_REF), kill="K3")
    return cls


# ============================== O: capped optimization (CCLXI O1/O3)
def make_objective(cls, fdata, extra_con=None):
    def neg_f(theta):
        v = tr_r_of_theta(theta, fdata)
        return -v if math.isfinite(v) else 1e12

    def slacks(theta):
        sl, _names = class_slack_vector(theta, cls)
        if extra_con is not None:
            sl = np.concatenate([sl, [extra_con(theta)]])
        return sl

    def penalized(theta):
        v = tr_r_of_theta(theta, fdata)
        if not math.isfinite(v):
            return 1e12
        sl = slacks(theta)
        viol = float(np.sum(np.clip(-sl, 0.0, None)))
        return -v + PEN_W * viol * viol
    return neg_f, slacks, penalized


def run_stage1(rows, cls, fdata, label, n_ms, de_maxiter,
               extra_con=None):
    lo, hi = cls["lo"], cls["hi"]
    bounds = list(zip(lo, hi))
    neg_f, slacks, penalized = make_objective(cls, fdata, extra_con)
    rng = np.random.default_rng(OPT_SEED)
    thetas = [r["theta"] for r in rows]
    seeds = []
    idx = np.linspace(0, len(thetas) - 1,
                      max(2, n_ms // 3)).astype(int)
    for i in sorted(set(idx.tolist())):
        seeds.append(np.clip(thetas[i], lo, hi))
    for i in sorted(set(idx.tolist())):
        cn = np.clip(thetas[i], lo, hi).copy()
        cn[0] = lo[0] + 1e-9 * (hi[0] - lo[0])
        cn[NDIM] = hi[NDIM] - 1e-9 * (hi[NDIM] - lo[NDIM])
        seeds.append(cn)
    while len(seeds) < n_ms:
        seeds.append(rng.uniform(lo, hi))
    cons = [dict(type="ineq", fun=slacks)]
    best_v, best_t = -float("inf"), None
    n_conv = 0
    for sd in seeds[:n_ms]:
        try:
            res = optimize.minimize(neg_f, sd, method="SLSQP",
                                    bounds=bounds, constraints=cons,
                                    options=dict(maxiter=SLSQP_MAXIT,
                                                 ftol=1e-12))
        except (ValueError, OverflowError):
            continue
        th = np.clip(res.x, lo, hi)
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            n_conv += 1
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    de = optimize.differential_evolution(
        penalized, bounds=bounds, seed=OPT_SEED, maxiter=de_maxiter,
        popsize=DE_POP, polish=False, tol=1e-10, init="sobol")
    th_de = np.clip(de.x, lo, hi)
    try:
        res = optimize.minimize(neg_f, th_de, method="SLSQP",
                                bounds=bounds, constraints=cons,
                                options=dict(maxiter=SLSQP_MAXIT,
                                             ftol=1e-12))
        th_pol = np.clip(res.x, lo, hi)
    except (ValueError, OverflowError):
        th_pol = th_de
    for th in (th_de, th_pol):
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    print("    %s: best feasible tr R = %.6f (feasible starts %d/%d) "
          "[%.1f s]" % (label, best_v, n_conv, n_ms,
                        time.time() - T0), flush=True)
    return best_v, best_t


# ============================ parametric rung builder (F2/F4/F5)
def build_rung_param(kz_label, alpha, mfold, uu, mm):
    """The ob.build_rung deep branch VERBATIM with (alpha, M, atoms)
    made explicit.  mfold = M (even).  Returns the rung dict or a
    censused failure dict."""
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    d = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _uf_p, _fdp = ob.folded_measure_full(d, lfold, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(d, lfold, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1 or np.any(be <= 0):
        return dict(kind="param", kz=kz_label, h=half, fail="CHAIN")
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = sym(gram)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    eva = np.linalg.eigvalsh(amat)
    out = dict(kind="param", kz=kz_label, h=half, n=n,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               tau=float(eva[0]), negA=int(np.sum(eva < 0.0)))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in ob.CORE_J)
    if not out["core_ok"]:
        out["fail"] = "CORE-SHORT"
        return out
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset], dtype=int)
    bblk = amat[np.ix_(ic, ic)]
    xc = amat[np.ix_(ic, ib)]
    rblk = amat[np.ix_(ib, ib)]
    try:
        zsol = np.linalg.solve(rblk, xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        out["fail"] = "R-SINGULAR"
        return out
    smat = sym(bblk - xc @ zsol)
    evs = np.linalg.eigvalsh(smat)
    out["S"] = smat
    out["lamS"] = float(evs[0])
    out["negS"] = int(np.sum(evs < 0.0))
    return out


def frame_of(u_arr, g_arr, mu_arr, kz, nu, alpha=None):
    """Deployed frame formulas with (nu, alpha) explicit."""
    if alpha is None:
        alpha = float(u_arr[kz])
    d_k = 0.5 * float(g_arr[kz]) / float(nu)
    mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
    if mz % 2:
        mz += 1
    ka = int(np.searchsorted(u_arr, 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, mz, mz // 2, u_arr[:ka].copy(), mu_arr[:ka].copy()


def sweep_steps(rungs, family, fdata, anchors):
    """Deployed step admission verbatim (ob.make_steps +
    zol.assemble_step) on TWO wall-legal step formations: (i) the
    within-family chain sorted by (h, kz), and (ii) one bridge step
    per family rung from its nearest registered truth predecessor
    (largest anchor h <= rung h, else the smallest anchor) -- the
    deployed bridge pattern generalized (AMENDMENT, smoke-driven,
    disclosed)."""
    fam = sorted([r for r in rungs if r.get("core_ok")],
                 key=lambda r: (r["h"], r["kz"]))
    pairs = list(zip(fam, fam[1:]))
    anc = sorted(anchors, key=lambda r: r["h"])
    for r2 in fam:
        below = [a for a in anc if a["h"] <= r2["h"]]
        r1 = below[-1] if below else anc[0]
        pairs.append((r1, r2))
    out = []
    n_refused = 0
    for r1, r2 in pairs:
        steps = ob.make_steps([r1, r2])
        if not steps:
            n_refused += 1
            continue
        st = steps[0]
        zol.assemble_step(st)
        if st["status"] != "OK":
            n_refused += 1
            continue
        kind = "chain" if r1.get("kind") == r2.get("kind") \
            and r1 in fam else "bridge"
        out.append(dict(step=st, seg=family,
                        h=float(st["r2"]["h"]),
                        kz=st["r2"]["kz"],
                        tau_scale=float(st["tau"]),
                        gap=float(st["gap"]),
                        nu=st["r2"].get("nu", 4),
                        mode="%s/%s" % (st["r2"].get("mode",
                                                     "anchor"),
                                        kind)))
    return out, n_refused


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements on the deployed
  construction family (the 68-step ladder plus wall-legal geometry
  variations the registered ladder does not use) and ONE re-frozen
  CCLXI truth-envelope class.  Every capped supremum is a NUMERIC
  LOWER bound of the true supremum; t*_hi is therefore an honest
  'provably fails to close' bar while t*_lo is only
  unverified-to-fail.  sigma is computed from the construction
  forward; the optimizer never sees h; the registration carries the
  HALFGAP no-adjustment clause verbatim.  No marker moves; no paper,
  ledger, website, manifest or verification file is touched; NO RH
  claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def ch_surface_map(rows):
    out = {}
    for kz in sorted({r["kz"] for r in rows if r["seg"] == "surf"}):
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
        out[int(kz)] = 1.0 - top
    return out


def main():
    section("PRIME.ONEBADMODE.KS.SIGMA.STRESS.01 -- the adversarial "
            "front on the 0.665 (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(("theta_matrices", "ks_wall_functionals",
                              "class_slack_vector", "sigma_quotient",
                              "tr_r_of_theta"), CLASS_BANNED)
    check("S0.2 AC class/objective functions carry no ladder or "
          "read identifier (CCLXI ban list verbatim)", not ac1,
          ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(("sigma_of_matrix", "jacobi_form",
                              "build_rung_param", "frame_of"),
                             READ_BANNED)
    check("S0.3 AC sigma/builder functions carry no read identifier "
          "(sigma from the construction forward)", not ac2,
          ",".join(sorted(set(ac2))), kill="K2")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0.4 CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")

    zones, steps, census, combined = build_ladder()
    if KILLS:
        return finish([])
    fdata = get_filter(steps, artifact)
    rows = translation(steps, artifact, fdata)
    if KILLS:
        return finish([])

    # ---- B + A: Jacobi translation and the full-ladder measurement
    section("B/A -- sigma on every registered step (the full-ladder "
            "measurement)")
    rows = jacobi_wards(rows, "ladder")
    if KILLS:
        return finish([])
    sig_all = np.asarray([r["sigma"] for r in rows], float)
    hs_all = np.asarray([r["h"] for r in rows], float)
    truth_max = float(np.max(sig_all))
    i_max = int(np.argmax(sig_all))
    check("SR SIGMA-REPRO truth envelope max %.6f reproduces CCLXI "
          "%.4f (rtol %.0e); arithmetic %.4f * 1.1 = %.6f (the "
          "0.665)" % (truth_max, SIGMA_MAX_REF, SIGMA_RTOL,
                      SIGMA_MAX_REF, SIGMA_MAX_REF * 1.1),
          SMOKE or abs(truth_max / SIGMA_MAX_REF - 1.0) <= SIGMA_RTOL,
          kill="K3")
    print("    sigma over %d steps: %s" % (len(rows), e3(sig_all)))
    for seg in ("surf", "bridge", "deep"):
        sub = [r["sigma"] for r in rows if r["seg"] == seg]
        if sub:
            print("      %-6s (%2d): %s" % (seg, len(sub), e3(sub)))
    sl, se2, r2, _ = linfit(np.log(hs_all), sig_all)
    print("    h-trend: d sigma / d log h = %+.5f +/- %.5f (2SE), "
          "R2 %.3f" % (sl, se2, r2))
    print("    MAX LOCATION: seg %s, kz %d, h %.0f, sigma %.6f "
          "(b1 %.5f, gap %.5f, tau %.4g)"
          % (rows[i_max]["seg"], rows[i_max]["kz"], rows[i_max]["h"],
             truth_max, rows[i_max]["theta"][0], rows[i_max]["gap"],
             rows[i_max]["tau_scale"]))
    check("A1 full-ladder sigma measured on %d/%d steps (all "
          "finite)" % (int(np.sum(np.isfinite(sig_all))), len(rows)),
          bool(np.all(np.isfinite(sig_all))), kill="K2")

    # ---- G: the class (for t* and the world census)
    section("G -- re-freeze the CCLXI class C_KS (t* machinery)")
    cls = freeze_class(rows, fdata)
    if KILLS:
        return finish([])

    # ================================ ADV: the adversarial sweep
    section("ADV -- the wall-legal adversarial sweep (F0/F1/F2/F4/"
            "F5)")
    # BW builder ward on declared census zones
    bw_kz = [kz for kz, _hz in census[:BW_N]]
    d_bw = 0.0
    for kz in bw_kz:
        ref = ob.build_rung("deep", kz, with_split=False)
        alpha, mz, _hz, uu, mm = frame_of(ob.EXT["U"], ob.EXT["G"],
                                          ob.EXT["MU"], kz, 4)
        par = build_rung_param(kz, alpha, mz, uu, mm)
        for key in ("tau", "lamS"):
            d_bw = max(d_bw, abs(par[key] - ref[key])
                       / max(1.0, abs(ref[key])))
        d_bw = max(d_bw, abs(par["h"] - ref["h"]))
    check("BW builder ward: parametric builder == ob.build_rung on "
          "%d census zones: max rel %.2e <= %.0e"
          % (len(bw_kz), d_bw, BW_TIE), d_bw <= BW_TIE, kill="K2")

    families = {}
    censuses = {}

    # F0 surface off-ladder (h in (900, 1450])
    f0_cap = 2 if SMOKE else F0_CAP
    f0_zones = [kz for kz in core.frame_a_zones()
                if kz not in set(ob.ladder_zones())]
    f0_pick = sorted(f0_zones,
                     key=lambda kz: -ob.window_of(kz)["h"])[:f0_cap]
    f0_rungs = []
    for kz in f0_pick:
        r = ob.build_rung("surf", kz, with_split=False)
        if r is not None:
            f0_rungs.append(r)
        print("    F0 surf kz %-4d h %-5s %s [%.1f s]"
              % (kz, ob.window_of(kz)["h"],
                 "OK" if r is not None else "SHORT",
                 time.time() - T0), flush=True)
    families["F0"], ref0 = sweep_steps(f0_rungs, "F0", fdata,
                                       combined)
    censuses["F0"] = ("%d zones off-ladder, %d picked, %d built, "
                      "%d step-refused"
                      % (len(f0_zones), len(f0_pick), len(f0_rungs),
                         ref0))

    # F1 deep off-ladder kz on the deployed table
    f1_cap = 3 if SMOKE else F1_CAP
    reg_deep = {kz for kz, _hz in ob.deep_zone_census()}
    reg_surf = set(ob.ladder_zones())
    f1_all = []
    for kz in range(2, ob.KZ_SCAN_MAX):
        alpha, _mz, hz, _ka = ob.ext_frame(kz)
        x_val = math.exp(2.0 * alpha)
        if (F1_BAND[0] <= hz <= F1_BAND[1] and x_val <= ob.TAB_EXT
                and kz not in reg_deep and kz not in reg_surf):
            f1_all.append(kz)
    stride = max(1, len(f1_all) // f1_cap)
    f1_pick = f1_all[::stride][:f1_cap]
    f1_rungs = []
    n_core_short = 0
    for kz in f1_pick:
        r = ob.build_rung("deep", kz, with_split=False)
        ok = r is not None and r.get("core_ok")
        if r is not None and not r.get("core_ok"):
            n_core_short += 1
        if ok:
            f1_rungs.append(r)
        print("    F1 deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, ob.ext_frame(kz)[2],
                 "OK" if ok else "CORE-SHORT/FAIL",
                 time.time() - T0), flush=True)
    families["F1"], ref1 = sweep_steps(f1_rungs, "F1", fdata,
                                       combined)
    censuses["F1"] = ("%d qualifying kz, stride %d -> %d picked, "
                      "%d built, %d CORE-SHORT (censused), %d "
                      "step-refused"
                      % (len(f1_all), stride, len(f1_pick),
                         len(f1_rungs), n_core_short, ref1))

    # F2 density nu > 4 (admissibility floor is nu = 4, cited)
    f2_nu = (6,) if SMOKE else F2_NU
    f2_nkz = 1 if SMOKE else F2_NKZ
    f2_kz = [kz for kz, _hz in census[:f2_nkz]]
    f2_rungs = []
    for nu in f2_nu:
        for kz in f2_kz:
            alpha, mz, hz, uu, mm = frame_of(
                ob.EXT["U"], ob.EXT["G"], ob.EXT["MU"], kz, nu)
            r = build_rung_param(kz, alpha, mz, uu, mm)
            r["nu"] = nu
            ok = r.get("core_ok") and "fail" not in r
            if ok:
                f2_rungs.append(r)
            print("    F2 nu %d kz %-4d h %-5d %s [%.1f s]"
                  % (nu, kz, hz, "OK" if ok
                     else r.get("fail", "FAIL"),
                     time.time() - T0), flush=True)
    families["F2"], ref2 = sweep_steps(f2_rungs, "F2", fdata,
                                       combined)
    censuses["F2"] = ("%d nu-variants attempted, %d built, %d "
                      "step-refused"
                      % (len(f2_nu) * len(f2_kz), len(f2_rungs),
                         ref2))

    # F4 off-anchor alpha (boundary window shape)
    f4_nkz = 1 if SMOKE else F4_NKZ
    f4_kz = [kz for kz, _hz in census[:f4_nkz]]
    f4_rungs = []
    for kz in f4_kz:
        alpha_mid = 0.5 * (float(ob.EXT["U"][kz])
                           + float(ob.EXT["U"][kz + 1]))
        alpha, mz, hz, uu, mm = frame_of(
            ob.EXT["U"], ob.EXT["G"], ob.EXT["MU"], kz, 4,
            alpha=alpha_mid)
        r = build_rung_param(kz, alpha, mz, uu, mm)
        r["mode"] = "mid-alpha"
        ok = r.get("core_ok") and "fail" not in r
        if ok:
            f4_rungs.append(r)
        print("    F4 mid-alpha kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if ok else r.get("fail", "FAIL"),
                 time.time() - T0), flush=True)
    families["F4"], ref4 = sweep_steps(f4_rungs, "F4", fdata,
                                       combined)
    censuses["F4"] = ("%d mid-alpha frames attempted, %d built, %d "
                      "step-refused"
                      % (len(f4_kz), len(f4_rungs), ref4))

    # F5 depth extension (TAB2 table)
    if SMOKE:
        censuses["F5"] = "SMOKE-SKIPPED (typed)"
        families["F5"] = []
        print("    F5 SMOKE-SKIPPED (typed)")
    else:
        lam2 = core.von_mangoldt_table(TAB2)
        nn2 = np.nonzero(lam2 > 0.0)[0]
        u2 = np.log(nn2.astype(float))
        mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
        g2 = np.diff(u2)
        n_pref = len(ob.EXT["NN"])
        check("X5 TAB2 prefix ward: 1.6e7 arrays agree bitwise with "
              "the deployed 4e6 EXT arrays",
              (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
               and np.array_equal(u2[:n_pref], ob.EXT["U"])
               and np.array_equal(mu2[:n_pref], ob.EXT["MU"])),
              kill="K2")
        f5_new = []
        hz_max_reach = 0
        for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
            alpha = float(u2[kz])
            d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
            mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
            if mz % 2:
                mz += 1
            hz = mz // 2
            x_val = math.exp(2.0 * alpha)
            if x_val > TAB2 or kz in reg_deep:
                continue
            newly = ((2900 < hz) or
                     (x_val > ob.TAB_EXT and 128 <= hz))
            if not newly:
                continue
            hz_max_reach = max(hz_max_reach, hz)
            if hz <= H5_CAP:
                f5_new.append((hz, kz, alpha, mz, x_val))
        f5_new.sort(reverse=True)
        f5_pick = f5_new[:N5]
        censuses["F5"] = ("%d newly reachable frames (TAB2 1.6e7, "
                          "kz < %d); max reachable hz %d (UNBUILT "
                          "above cost cap %d: lanczos ~2 h^3 flops, "
                          "gram h^2 * 8 B memory -- hz %d ~ %.0e "
                          "flops, %.1f GB); %d picked"
                          % (len(f5_new), KZ2_MAX, hz_max_reach,
                             H5_CAP, hz_max_reach,
                             2.0 * hz_max_reach ** 3,
                             hz_max_reach ** 2 * 8 / 1e9,
                             len(f5_pick)))
        print("    F5 census: %s" % censuses["F5"], flush=True)
        f5_rungs = []
        for hz, kz, alpha, mz, x_val in f5_pick:
            ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14,
                                     side="right"))
            r = build_rung_param(kz, alpha, mz, u2[:ka].copy(),
                                 mu2[:ka].copy())
            r["mode"] = "depth-ext"
            ok = r.get("core_ok") and "fail" not in r
            if ok:
                f5_rungs.append(r)
            print("    F5 deep-ext kz %-4d h %-5d X %.3g %s [%.1f s]"
                  % (kz, hz, x_val, "OK" if ok
                     else r.get("fail", "FAIL"),
                     time.time() - T0), flush=True)
        families["F5"], ref5 = sweep_steps(f5_rungs, "F5", fdata,
                                           combined)
        censuses["F5"] += "; %d built, %d step-refused" \
            % (len(f5_rungs), ref5)

    # sweep wards + statistics
    sweep_rows = [r for fam in families.values() for r in fam]
    check("ADV1 sweep produced %d wall-legal steps (%s)"
          % (len(sweep_rows),
             ", ".join("%s %d" % (k, len(v))
                       for k, v in sorted(families.items()))),
          len(sweep_rows) >= (2 if SMOKE else 8), kill="K1")
    for fam, cen in sorted(censuses.items()):
        print("    census %s: %s" % (fam, cen))
    sweep_rows = jacobi_wards(sweep_rows, "sweep")
    if KILLS:
        return finish([])
    adv_sig = np.asarray([r["sigma"] for r in sweep_rows], float)
    adv_max = float(np.max(adv_sig))
    j_max = int(np.argmax(adv_sig))
    print("    sweep sigma over %d steps: %s"
          % (len(sweep_rows), e3(adv_sig)))
    for fam in sorted(families):
        sub = [r["sigma"] for r in families[fam]
               if r.get("theta") is not None]
        if sub:
            print("      %-3s (%2d): %s" % (fam, len(sub), e3(sub)))
    amax = sweep_rows[j_max]
    print("    ADVERSARIAL MAX: family %s, kz %s, h %.0f, nu %s, "
          "mode %s, sigma %.6f (b1 %.5f, a1 %.5f, lamB1 %.5f, gap "
          "%.5f)" % (amax["seg"], amax["kz"], amax["h"], amax["nu"],
                     amax["mode"], adv_max, amax["theta"][0],
                     amax["theta"][NDIM],
                     float(np.linalg.eigvalsh(
                         theta_matrices(amax["theta"])[1])[0]),
                     amax["gap"]))
    overall_max = max(truth_max, adv_max)
    check("ADV2 adversarial + ladder sigma envelope measured: "
          "adversarial max %.6f, ladder max %.6f, overall %.6f"
          % (adv_max, truth_max, overall_max), True)

    # ================================ t*: the closing threshold
    section("TSTAR -- the closing threshold from the CCLXI cap-curve")
    n_ms = 4 if SMOKE else CAP_MS
    de_it = 20 if SMOKE else CAP_DE
    ctrl_lo = cls["lo"].copy()
    ctrl_lo[0] = min(ctrl_lo[0], OPT_CTRL_B1)
    ctrl_cls = dict(cls)
    ctrl_cls["lo"] = ctrl_lo
    ctrl_cls["wd"] = cls["hi"] - ctrl_lo
    v_ctrl, _t = run_stage1(rows, ctrl_cls, fdata,
                            "O0 OPT-POWER control", O0_MS, O0_DE)
    check("O0 CONTROL optimizer reaches tr R >= %.1f on the control "
          "box: best %.4f" % (OPT_CTRL_BAR, v_ctrl),
          v_ctrl >= OPT_CTRL_BAR, kill="K4")
    if KILLS:
        return finish([])
    v_open, _t = run_stage1(rows, cls, fdata,
                            "uncapped anchor (CCLXI 2.2578 is the "
                            "full-budget value)", n_ms, de_it)
    caps = (0.665, 0.92) if SMOKE else CAPS
    curve = []
    for cap in caps:
        def sig_con(theta, cap=cap):
            s = sigma_quotient(theta)
            if not math.isfinite(s) or theta[0] <= 0.0:
                return -1.0
            return (cap - s) / max(abs(cap), 1e-6)
        v_cap, _t = run_stage1(rows, cls, fdata,
                               "cap sigma <= %.3f" % cap, n_ms,
                               de_it, extra_con=sig_con)
        curve.append((cap, v_cap))
    t_lo = max([c for c, v in curve if v < 1.0], default=float("nan"))
    t_hi = min([c for c, v in curve if v >= 1.0],
               default=float("nan"))
    t_num = float("nan")
    for (c1, v1), (c2, v2) in zip(curve, curve[1:]):
        if v1 < 1.0 <= v2:
            t_num = c1 + (1.0 - v1) * (c2 - c1) / (v2 - v1)
            break
    crossed = math.isfinite(t_hi)
    print("    cap-curve: %s; uncapped anchor %.4f"
          % (", ".join("%.3f->%.4f" % cv for cv in curve), v_open))
    print("    t*_lo = %s (largest closing cap, unverified-to-fail "
          "above), t*_hi = %s (provably non-closing), t*_num = %s"
          % ("%.4f" % t_lo if math.isfinite(t_lo) else "NONE",
             "%.4f" % t_hi if crossed else "NOT-CROSSED(grid max)",
             "%.4f" % t_num if math.isfinite(t_num) else "n/a"))
    check("TS1 cap-curve measured on %d caps (every sup a NUMERIC "
          "lower bound; typed)" % len(curve), True)
    t_use = t_num if math.isfinite(t_num) else (
        t_hi if crossed else max(c for c, _v in curve))
    d_env = ENV_REF - overall_max
    d_t = t_use - overall_max
    print("    DISTANCE VERDICT: overall max sigma %.6f; to 0.665: "
          "%+.6f; to t*(%s): %+.6f"
          % (overall_max, d_env,
             "num" if math.isfinite(t_num) else "grid", d_t))

    # ================================ R: the registration + blind
    section("R -- the registration (HALFGAP pattern) + blind "
            "holdout")
    print("    THE FROZEN NO-ADJUSTMENT CLAUSE (verbatim pattern): "
          "the envelope is FROZEN now, before any future data.  A "
          "later miss on any rung -- holdout or otherwise -- is a "
          "FAIL of the registered envelope, full stop; it must NOT "
          "be repaired by adjusting the constant, by reweighting, "
          "or by excluding rungs.  A failed registration is a "
          "first-class result.")
    choice = ([r for r in rows if r["seg"] in ("surf", "bridge")]
              + [r for r in sweep_rows if r["seg"] != "F5"])
    holdout = ([r for r in rows if r["seg"] == "deep"]
               + [r for r in sweep_rows if r["seg"] == "F5"])
    env_choice = float(np.max([r["sigma"] for r in choice]))
    sigma_env = env_choice * (1.0 + SAFETY)
    reg_lines = ["%s:%s:%d:%.12e" % (r["seg"], r["kz"], int(r["h"]),
                                     r["sigma"]) for r in choice]
    reg_lines.append("ENV:%.12e" % sigma_env)
    reg_sha = hashlib.sha256(
        "\n".join(reg_lines).encode("utf-8")).hexdigest()
    print("    CHOICE SET: %d steps (40 surface + bridge + F0-F4); "
          "choice max %.6f -> SIGMA_ENV = %.6f (safety %.2f); "
          "registry SHA-256 %s" % (len(choice), env_choice,
                                   sigma_env, SAFETY, reg_sha[:16]))
    print("    KILL CRITERION (frozen): ONE wall-legal step with "
          "sigma >= t*_hi = %s kills the KS.DUAL closing route; "
          "sigma >= 0.665 anywhere wall-legal breaks the registered "
          "envelope." % ("%.4f" % t_hi if crossed
                         else "NOT-CROSSED on the declared grid"))
    fails = [r for r in holdout if r["sigma"] > sigma_env]
    n_pass_blind = len(holdout) - len(fails)
    for r in fails:
        print("      BLIND FAIL %s kz %s h %.0f sigma %.6f > ENV "
              "%.6f" % (r["seg"], r["kz"], r["h"], r["sigma"],
                        sigma_env))
    check("R1 blind holdout (deep block + F5): %d/%d pass sigma <= "
          "SIGMA_ENV %.6f (fails are first-class, never repaired)"
          % (n_pass_blind, len(holdout), sigma_env), True)
    blind_txt = ("%d/%d PASS" % (n_pass_blind, len(holdout))
                 if not fails else
                 "%d/%d FAIL(%s)" % (len(fails), len(holdout),
                                     ",".join("%s:%s" % (r["seg"],
                                                         r["kz"])
                                              for r in fails[:4])))

    # ================================ S: screens + worlds
    section("S -- tau / c_h relocation screens + world census")
    taus = np.asarray([r["tau_scale"] for r in rows], float)
    ch_map = ch_surface_map(rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in rows], float)
    reloc = []
    seat_txt = []
    for label, arr in (
            ("sigma", sig_all),
            ("margin(0.665-sigma)", ENV_REF - sig_all),
            ("margin(t*-sigma)", t_use - sig_all)):
        t1, v1 = screen(arr, taus, "%s vs tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask], "%s vs c_h" % label)
        print("      " + t1 + " | " + t2)
        seat_txt.append("%s:%s/%s" % (label, v1, v2))
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau/c_h relocation screens: relocation seats %s "
          "(margin RELOC would mean the constraint is the lock "
          "relabeled)" % (",".join(reloc) or "none"), not reloc)

    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    world_txt = []
    for world in ("smooth", "scramble"):
        ladder = []
        for kz in zones:
            if world == "smooth":
                ladder.append((kz, ob.build_rung("surf", kz,
                                                 world="smooth")))
            else:
                ladder.append((kz, ob.build_rung(
                    "surf", kz, scramble_seed=SCRAMBLE_SEED)))
        if world == "smooth":
            wall_fire = sum(1 for _kz, r in ladder
                            if r is None or r["negA"] > 0)
            check("C1 SMOOTH violates the wall target on %d/%d "
                  "surface rungs" % (wall_fire, len(ladder)),
                  wall_fire == len(ladder), kill="K4")
        n_align = n_out = 0
        sig_pos = []
        n_bneg = 0
        n_over = 0
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if tr is None or ctl is None or not ctl.get("core_ok"):
                continue
            n_align += 1
            with np.errstate(over="ignore", invalid="ignore"):
                mw = sym(tr["step"]["Q"].T
                         @ (ctl["S"] / tr["tau_scale"])
                         @ tr["step"]["Q"])
                sig_w, theta_w = sigma_of_matrix(mw)
            if theta_w is None:
                n_out += 1
                continue
            slv, _n = class_slack_vector(theta_w, cls)
            if float(np.min(slv)) < -FEAS_TOL:
                n_out += 1
            if theta_w[0] <= 0.0:
                n_bneg += 1
            else:
                sig_pos.append(sig_w)
                if sig_w > ENV_REF:
                    n_over += 1
        fire = n_out > CTRL_MAJORITY * max(n_align, 1)
        check("X2[%s] class-exclusion census: OUT+BREAK %d/%d "
              "aligned -> %s" % (world, n_out, n_align,
                                 "FIRE" if fire else "SILENT"),
              fire, kill="K4")
        print("      %s sigma census: b1>0 %d "
              "(sigma %s; %d over 0.665), b1<=0 %d -- the worlds "
              "leave the class anyway (CCLXI excluders)"
              % (world, len(sig_pos), e3(sig_pos), n_over, n_bneg))
        world_txt.append("%s:%d/%d out,%d over-env"
                         % (world, n_out, n_align, n_over))

    # ---- verdict
    if crossed and adv_max >= t_hi:
        head = ("SIGMA-KILL(adversarial max %.4f >= t*_hi %.4f at "
                "%s kz %s h %.0f -- a wall-legal configuration "
                "provably kills the KS.DUAL closing route)"
                % (adv_max, t_hi, amax["seg"], amax["kz"],
                   amax["h"]))
    elif overall_max >= ENV_REF:
        head = ("SIGMA-BREACH(max wall-legal sigma %.4f >= 0.665 "
                "(%s), distance to t*(%s) %+.4f -- the registered "
                "envelope breaks; the closing route %s)"
                % (overall_max,
                   "adversarial" if adv_max >= truth_max
                   else "ladder", "%.4f" % t_use, d_t,
                   "survives only with a wider cap"
                   if d_t > 0 else "is dead"))
    else:
        head = ("SIGMA-SURVIVES(max wall-legal sigma %.4f < 0.665; "
                "distance %+.4f to the envelope, %+.4f to t* %s; "
                "adversarial max %.4f at %s kz %s h %.0f)"
                % (overall_max, d_env, d_t,
                   "%.4f" % t_use, adv_max, amax["seg"],
                   amax["kz"], amax["h"]))
    labels = [
        head,
        "REGISTERED(SIGMA_ENV %.6f, registry %s, blind %s)"
        % (sigma_env, reg_sha[:8], blind_txt),
        "TSTAR(%s; curve %s; NUMERIC lower bounds)"
        % ("t*_hi %.4f" % t_hi if crossed
           else "NOT-CROSSED on grid <= %.2f" % max(caps),
           " ".join("%.3f:%.3f" % cv for cv in curve)),
        "SCREENS(%s)" % "; ".join(seat_txt),
        "WORLDS(%s)" % "; ".join(world_txt),
        "AMENDMENTS(per smoke disclosure)",
    ]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
