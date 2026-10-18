#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sigma_edge_growth_probe -- PRIME.ONEBADMODE.KS.SIGMA.EDGE.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE ONE OPEN MEASUREMENT QUESTION OF CCLXIX.  The sigma stress battery
(sigma_stress_battery_probe, note CCLXIX) measured the adversarial
maximum of the Schur quotient

    sigma = a_1^2 [J_B^-1]_11 / b_1      (Lanczos of the normalized
                                          wall, CCLXI verbatim)

at 0.709925 on an F0 SURFACE-OFFLADDER bridge step (kz 45, h 1359) --
directly at the registration edge of the frame-A scan, whose census
stops at HCAP = 1450 (v563_paper2_readouts, the T170 window range).
The registered envelope SIGMA_ENV = 0.780917 and the measured closing
threshold t* (t*_lo 0.85 / t*_num 0.9188 / t*_hi 0.92) are FROZEN
CCLXIX references; the frozen kill criterion is ONE wall-legal step
with sigma >= t*_hi = 0.92.  The open question, verbatim from the
CCLXIX seam: does sigma keep GROWING along the surface registration
edge beyond the scan cap (h > 1450 does not exist in the frame-A
census), or is ~0.71 the PLATEAU?  This probe builds the edge.

THE EDGE CENSUS (the deployed construction, one registration gate
removed).  A frame-A EDGE zone is every prime-power zone kz in
[2, NZ_DEEP - 2) whose deployed frame formula (D_k = G[kz]/(2 nu),
nu = 4, M = ceil(alpha/D_k - 1e-9) + 1 rounded even, h = M/2, alpha =
U[kz] -- v563 frame_a_zones verbatim) gives h in (HCAP, H_EDGE_MAX],
which passes the deployed atom floor (atoms_in >= N_ATOM_MIN = 40),
and which is ATOM-COMPLETE: X = exp(2 alpha) <= ATOM_MAX = 4e5 (the
deployed atom table covers the whole window -- the same gate the
deployed level machinery euler_phase_identity_probe.level_rung
applies; zones with X > ATOM_MAX would be built on a TRUNCATED atom
table, a construction the deployed surface family never uses, and are
censused as ATOM-INCOMPLETE, not built).  MEASURED CENSUS FACT
(reconnaissance, disclosed): the atom-complete edge is FINITE -- 58
zones in h in (1450, 8000] and NONE above -- so this probe builds THE
ENTIRE REMAINING FRAME-A EDGE (subject only to the wall-clock guard),
a 3.9x-5.5x extension of HCAP; there is no further frame-A surface
beyond it.  Wall-legality per cell is the CCLXIX definition verbatim:
the rung builds, core_ok, negA = 0, lamS > 0, tau > 0, the deployed
step admission ob.make_steps applies, zol.assemble_step returns OK.

STEPS (CCLXIX sweep_steps verbatim, both wall-legal formations):
within-family chain pairs in (h, kz) order among the built edge cells
PLUS one bridge step per cell from its nearest registered truth
predecessor (largest registered h <= cell h, else the smallest) --
anchors are the 42 + 28 registered combined rungs.  sigma per cell =
max over the wall-legal steps LANDING on the cell (r2 = cell), with
the winning mode reported.  The trace/reserve/filter machinery is
never entered (sigma is filter-independent); no artifact is read for
sigma; no optimizer runs (t* is a FROZEN reference, not re-measured).

THE VERDICT LAW (frozen, dominance order):
 EDGE-KILL: any wall-legal edge step with sigma >= KILL_REF = 0.92 --
   the CCLXIX kill criterion fires for real (the route dies).
 EDGE-GROWING: both law fits (per-cell sigma vs log h, and the
   NBIN = 6 log-h bin-envelope maxima vs log h) have slope - 2SE > 0;
   the extrapolated h* where the ENVELOPE fit reaches 0.92 is
   reported (the honest risk number); since the probe builds the
   whole finite census, a crossing inside the census IS the direct
   kill test -- the crossing cell is built and measured.
 EDGE-FALLING: both fits have slope + 2SE < 0.
 EDGE-NONMONOTONE: an interior bin envelope exceeds BOTH end-bin
   envelopes by NM_DELTA = 0.05 (anatomy reported).
 EDGE-PLATEAU: everything else -- the plateau level = max edge sigma,
   with its distances to 0.665 / SIGMA_ENV 0.780917 / 0.92.
Plus typed tags ENV-STATUS (does any edge cell break the FROZEN
registered envelope 0.780917?  A miss is a first-class FAIL of the
CCLXIX registration, never repaired here -- the constants do not
move), BAND (the breach band kz in [35, 60] profile), MECHANISM,
SCREENS, CONTROLS, CENSUS, AMENDMENTS.  Every enum is a finite
float64 statement about the deployed construction family; NEVER an
all-h statement, NEVER an RH claim.

THE MECHANISM PEEK (cheap, one paragraph): on the TOP_N = 6 legal
edge cells by sigma, the ingredient decomposition (b_1, a_1,
[J_B^-1]_11, lamB1, gap, winning mode, anchor) plus the ingredient
trend fits d log(a_1^2)/d log h, d log(1/b_1)/d log h,
d log([J_B^-1]_11)/d log h against d log sigma/d log h (the exact
decomposition d log sigma = 2 d log a_1 + d log m_B - d log b_1), and
the bridge-vs-chain anatomy (per-mode sigma stats + the Q-frame
diagnostic: sigma of the UNROTATED cell matrix S_2 -- sigma is scale
invariant, so this isolates the Householder bridge frame; diagnostic
only, not a wall-legal step).

GATES / WARDS (kill -> typed verdicts):
 S0 AST firewall (no prime/zero oracle) + anti-circularity: the
    sigma/builder/census functions carry no read identifier (reserve,
    margin, trace_r, lu_read, scalar_r, trace_filter_lu); sigma is
    computed from the construction FORWARD (assembled wall matrix ->
    jacobi_form -> Schur quotient); 0.665 / 0.780917 / 0.92 / 0.9188
    enter ONLY as frozen comparison references, never as inputs.
 EC the edge-census formula, run on (H_LADDER_MAX, HCAP] WITHOUT the
    atom-complete gate, reproduces the CCLXIX F0 zone set exactly
    (frame_a_zones minus ladder_zones) -- the census is the deployed
    scan with one bound moved.
 W  ladder rebuilt read-only (42 surface rungs, 68 = 40 + 1 + 27
    steps, deployed admission verbatim).
 B  CCLXI B1-B5 verbatim on all 68 ladder steps AND on every edge /
    breach / control step (Lanczos exists; b_1 == M[0,0]; a_1 ==
    ||M[1:,0]||; lambda_min(J_B) == lamB1; m(0) gap == 1; the sigma
    identity b_1 (1 - sigma) == gap).
 SR SIGMA-REPRO: the truth-ladder sigma envelope reproduces CCLXI/
    CCLXIX (max 0.6046, rtol 2e-3).
 BR BREACH-REPRO: the CCLXIX adversarial maximum reproduces -- the
    F0 kz 45 (h 1359) bridge step from its nearest registered truth
    predecessor gives sigma = 0.709925 (rtol 1e-5).
 C  controls-must-fire on the declared control cell CTRL_KZ = 47
    (the smallest-h edge cell in the breach band): C1 the smooth
    world violates the wall target or leaves legality; C2 the
    scramble world (deployed seed) leaves legality or moves sigma by
    >= CTRL_DELTA = 0.05.  Silent -> CONTROL-SILENT.
 SCREENS: tau relocation screens (CCXLVII bars verbatim, slopes
    0.30 / 0.70) on edge sigma and on both frozen margins
    (0.92 - sigma), (0.780917 - sigma); c_h relocation screen on the
    CH_N = 6 top legal edge cells with h <= CH_HMAX = 2900 (the c_h
    surface is computed with the deployed level formulas -- window
    lag arm -> grid density -> gram pencil top eigenvalue -- applied
    past the HCAP registration gate, DISCLOSED: the gate is a
    registration bound, not a construction bound; cells above
    CH_HMAX are typed OUT-OF-SURFACE for c_h, cost cap declared).

BUDGET (declared, the CCLXIX cost question answered by
reconnaissance): the surface pipeline folds to n ~ 0.54 h points, so
a cell costs ~COST_C * h^3 with COST_C = 8.3 s / 2854^3 (machine
calibration, disclosed) -- h 2472 measured 5.7 s, h 2854 (deep) 8.3
s.  Cells are built in ascending h; before each build the projected
finish elapsed + 2 * COST_C * h^3 must stay <= HARD_CAP_S = 1350 s,
else the cell and all remaining cells are censused UNBUILT-GUARD
(honest, machine-dependent, disclosed).  Total runtime target < 25
min including the ladder (~105 s) and the c_h screen (~60 s).

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward -> WARD-BROKEN;
K3 reproduction -> REPRO-BROKEN; K4 control silent -> CONTROL-SILENT.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; TRANSLATE_TIE
= 1e-8; MZERO_TIE = 1e-7; SIGMA_MAX_REF = 0.6046; SIGMA_RTOL = 2e-3;
BREACH_KZ = 45; BREACH_H = 1359; BREACH_REF = 0.709925; BREACH_RTOL =
1e-5; ENV_REF = 0.665; SIGMA_ENV_REF = 0.780917; KILL_REF = 0.92;
TSTAR_NUM_REF = 0.9188 (report-only); H_EDGE_MAX = 8000; NBIN = 6;
NM_DELTA = 0.05; TOP_N = 6; CH_N = 6; CH_HMAX = 2900; CTRL_KZ = 47;
CTRL_DELTA = 0.05; KZ_BAND = (35, 60); SLOPE_PASS = 0.30; SLOPE_RELOC
= 0.70; COST_C = 8.3 / 2854^3 s; HARD_CAP_S = 1350; GUARD_FAC = 2.0;
runtime cap 25 min.  Smoke: ladder 10 contiguous surface rungs + 3
lowest deep; edge build = the 3 lowest-h census cells only, the rest
censused SMOKE-SKIPPED (typed); CH_N = 2; SR / BR / W3-counts / EC
bypassed by design (the smoke ladder is not the 68-step artifact
ladder and the smoke anchors are not the deployed anchors -- the
CCLXI/CCLXIX identical smoke phenomenon, disclosed).

SMOKE DISCLOSURE (2026-08-12, one smoke pass + one pre-freeze
reconnaissance before the freeze; no bar, control, screen, enum or
success rule was changed after the smoke; SPEC SHA moves with this
text, disclosed).
 SMOKE-1 (12.1 s) ran 31/31 GREEN, no kills: the 3 lowest-h census
 cells built (kz 91 h 1458, kz 126 h 1481, kz 92 h 1485), 5
 wall-legal edge steps, edge sigma 0.0932/0.1861/0.2854, B-wards on
 ladder and edge clean, both controls fired (C1 smooth negA = 220;
 C2 scramble left legality, NEGA), tau screens PASS, SR / BR / W3 /
 EC smoke-bypassed as declared.  ONE post-smoke change (cosmetic,
 disclosed, no bar or rule touched): the c_h print format %.6f ->
 %.4e (the values are ~1e-7 and displayed as 0.000000).
 PRE-FREEZE RECONNAISSANCE (disclosed): the EC and BR gates were
 validated standalone with the full deployed anchors BEFORE the
 freeze -- EC zone set 28 == 28 exact, and the breach bridge
 (anchor deep kz 243 h 1292) gave sigma 0.709924975 against the
 CCLXIX reference 0.709925 (rel 3.5e-8) -- no constant, bar or rule
 was adjusted in response; the references were already frozen.
 The frozen run below is the run of record.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXXIII line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder + rung
builder), zolotarev_phase_filter_probe (step assembly, verbatim),
v563_paper2_readouts (deployed frame-A generators, READ-ONLY),
euler_phase_identity_probe (c_h level machinery, cited),
sigma_stress_battery_probe / note CCLXIX (breach anatomy, frozen
references, sweep-step pattern, cited),
zolotarev_ks_dual_probe / note CCLXI (sigma definition, cited).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_edge_growth_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sigma_edge_growth_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

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
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
SIGMA_MAX_REF = 0.6046
SIGMA_RTOL = 2.0e-3
BREACH_KZ = 45
BREACH_H = 1359
BREACH_REF = 0.709925
BREACH_RTOL = 1.0e-5
ENV_REF = 0.665
SIGMA_ENV_REF = 0.780917
KILL_REF = 0.92
TSTAR_NUM_REF = 0.9188
H_EDGE_MAX = 8000
NBIN = 6
NM_DELTA = 0.05
TOP_N = 6
CH_N = 6
CH_HMAX = 2900
CTRL_KZ = 47
CTRL_DELTA = 0.05
KZ_BAND = (35, 60)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
COST_C = 8.3 / 2854.0 ** 3
HARD_CAP_S = 1350.0
GUARD_FAC = 2.0
SCRAMBLE_SEED = ob.SCR_SEED

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
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


def theta_matrices(theta):
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


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


def sigma_of_matrix(matrix):
    """sigma from the construction FORWARD: wall matrix -> Lanczos ->
    Schur quotient.  Returns (sigma, theta) or (nan, None)."""
    jf = jacobi_form(matrix)
    if jf is None:
        return float("nan"), None
    theta = np.concatenate([jf[1], jf[0]])
    return sigma_quotient(theta), theta


# ================================ B: Jacobi translation + sigma wards
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


# ====================================================== wall ladder
def build_ladder():
    section("W -- the CCVII/CCXXV wall ladder, rebuilt read-only "
            "(anchors + truth envelope)")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          SMOKE or len(zones) == SURF_EXP, kill="K1")
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
    rows = [dict(step=st, seg=ob.seg_of(st),
                 h=float(st["r2"]["h"]), kz=int(st["r2"]["kz"]),
                 tau_scale=float(st["tau"]), gap=float(st["gap"]))
            for st in steps]
    return zones, rows, combined


# =============================== edge census + steps (AC-scanned)
def edge_census(h_lo, h_hi, atom_complete=True):
    """The deployed frame-A candidate scan (v563 frame_a_zones
    formula VERBATIM) with the h-window moved to (h_lo, h_hi] and the
    deployed level-machinery atom-complete gate X <= ATOM_MAX
    (optional, disclosed)."""
    out = []
    for kz in range(2, core.NZ_DEEP - 2):
        d_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        mz = int(math.ceil(float(core.U_ALL[kz]) / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        hz = mz // 2
        if hz <= h_lo or hz > h_hi:
            continue
        if core.atoms_in(float(core.U_ALL[kz])) < core.N_ATOM_MIN:
            continue
        if atom_complete and math.exp(
                2.0 * float(core.U_ALL[kz])) > core.ATOM_MAX:
            continue
        out.append((hz, kz))
    return sorted(out)


def sweep_steps(rungs, family, anchors):
    """CCLXIX sweep_steps verbatim (fdata argument dropped -- it was
    unused there; no trace machinery is entered): deployed step
    admission (ob.make_steps + zol.assemble_step) on TWO wall-legal
    step formations: (i) the within-family chain sorted by (h, kz),
    and (ii) one bridge step per family rung from its nearest
    registered truth predecessor (largest anchor h <= rung h, else
    the smallest anchor)."""
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
                        kz=int(st["r2"]["kz"]),
                        tau_scale=float(st["tau"]),
                        gap=float(st["gap"]),
                        anchor="%s:%d:h%d" % (r1["kind"], r1["kz"],
                                              int(r1["h"])),
                        mode=kind))
    return out, n_refused


def cell_legal(rung):
    """CCLXIX wall-legality of a single cell, verbatim fields."""
    if rung is None:
        return False, "CHAIN-SHORT"
    if not rung.get("core_ok"):
        return False, "CORE-SHORT"
    if rung["negA"] > 0:
        return False, "NEGA"
    if rung.get("lamS", -1.0) <= 0.0:
        return False, "LAMS"
    if rung["tau"] <= 0.0:
        return False, "TAU"
    return True, "OK"


def ch_of_cell(kz):
    """The deployed c_h level readout (euler_phase_identity level
    machinery: window lag arm -> grid density -> gram pencil top
    eigenvalue), applied past the HCAP registration gate (DISCLOSED;
    the atom-complete gate X <= ATOM_MAX is enforced by the census)."""
    rr = ob.window_of(kz)
    c_at = np.asarray(core.atom_lags_at(rr["alpha"], rr["M"],
                                        rr["uu"], 2.0 * rr["lam"])[0],
                      float)
    dens = eul.grid_density(rr["c_ar"] + c_at)
    pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                             rr["M"])
    neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                             rr["M"])
    last = pos.shape[0] - 1
    top = float(sla.eigh(neg, pos, eigvals_only=True,
                         subset_by_index=[last, last])[0])
    return 1.0 - top


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
  HONEST FRAME.  Finite float64 measurements on the deployed frame-A
  construction past its registration cap HCAP = 1450, on the frozen
  atom-complete census (X <= 4e5) -- the census is FINITE and this
  run builds it up to the declared wall-clock guard.  sigma is
  computed from the construction forward; SIGMA_ENV = 0.780917, the
  kill line 0.92 and t*_num = 0.9188 are FROZEN CCLXIX references,
  reported against and never moved; an edge cell above SIGMA_ENV is
  a first-class FAIL of the CCLXIX registration, not repaired here.
  No marker moves; no paper, ledger, website, manifest or
  verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.SIGMA.EDGE.01 -- growth or plateau "
            "along the surface registration edge (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(("sigma_of_matrix", "sigma_quotient",
                             "theta_matrices", "jacobi_form",
                             "edge_census", "cell_legal",
                             "ch_of_cell"), READ_BANNED)
    check("S0.2 AC sigma/builder/census functions carry no read "
          "identifier (sigma from the construction forward)", not ac,
          ",".join(sorted(set(ac))), kill="K2")

    # EC: the census formula reproduces the CCLXIX F0 zone set
    f0_ref = sorted(set(core.frame_a_zones())
                    - set(ob.ladder_zones()))
    f0_mine = sorted(kz for _h, kz in
                     edge_census(ob.H_LADDER_MAX, core.HCAP,
                                 atom_complete=False))
    check("EC census formula on (%d, %d] reproduces the CCLXIX F0 "
          "zone set: %d == %d zones, equal %s"
          % (ob.H_LADDER_MAX, core.HCAP, len(f0_mine), len(f0_ref),
             f0_mine == f0_ref),
          SMOKE or f0_mine == f0_ref, kill="K3")

    zones, rows, combined = build_ladder()
    if KILLS:
        return finish([])

    # ---- B + SR on the truth ladder
    section("B/SR -- sigma on the registered ladder (truth envelope)")
    rows = jacobi_wards(rows, "ladder")
    if KILLS:
        return finish([])
    sig_all = np.asarray([r["sigma"] for r in rows], float)
    truth_max = float(np.max(sig_all))
    print("    ladder sigma over %d steps: %s"
          % (len(rows), e3(sig_all)))
    check("SR SIGMA-REPRO truth envelope max %.6f reproduces CCLXI/"
          "CCLXIX %.4f (rtol %.0e)"
          % (truth_max, SIGMA_MAX_REF, SIGMA_RTOL),
          SMOKE or abs(truth_max / SIGMA_MAX_REF - 1.0) <= SIGMA_RTOL,
          kill="K3")

    # ---- BR: the CCLXIX breach reproduction
    section("BR -- the CCLXIX breach cell (kz %d, h %d), reproduced"
            % (BREACH_KZ, BREACH_H))
    r_breach = ob.build_rung("surf", BREACH_KZ, with_split=False)
    leg_b, why_b = cell_legal(r_breach)
    breach_rows = []
    if leg_b:
        breach_rows, _ref = sweep_steps([r_breach], "F0", combined)
        breach_rows = [r for r in breach_rows if r["mode"] == "bridge"]
        breach_rows = jacobi_wards(breach_rows, "breach", kill="K3")
    sig_breach = (breach_rows[0]["sigma"] if breach_rows
                  else float("nan"))
    if breach_rows:
        print("    breach bridge: anchor %s, sigma %.9f (CCLXIX "
              "%.6f)" % (breach_rows[0]["anchor"], sig_breach,
                         BREACH_REF))
    check("BR breach reproduces: h %s legal %s, |sigma/%.6f - 1| = "
          "%s <= %.0e"
          % (r_breach["h"] if r_breach else "n/a", why_b, BREACH_REF,
             ("%.2e" % abs(sig_breach / BREACH_REF - 1.0))
             if math.isfinite(sig_breach) else "n/a", BREACH_RTOL),
          SMOKE or (leg_b and r_breach["h"] == BREACH_H
                    and math.isfinite(sig_breach)
                    and abs(sig_breach / BREACH_REF - 1.0)
                    <= BREACH_RTOL),
          kill="K3")
    if KILLS:
        return finish([])

    # ================================ EDGE: the census and the scan
    section("EDGE -- the frame-A registration edge beyond HCAP = %d"
            % core.HCAP)
    cens = edge_census(core.HCAP, H_EDGE_MAX)
    n_incomplete = len(edge_census(core.HCAP, H_EDGE_MAX,
                                   atom_complete=False)) - len(cens)
    print("    census: %d atom-complete edge zones in h (%d, %d]; "
          "%d ATOM-INCOMPLETE zones (X > %g) censused, NOT built "
          "(the deployed surface family never uses truncated atom "
          "tables)" % (len(cens), core.HCAP, H_EDGE_MAX,
                       n_incomplete, float(core.ATOM_MAX)))
    beyond = edge_census(H_EDGE_MAX, 10 ** 9)
    print("    census beyond the cap: %d atom-complete zones with "
          "h > %d exist -- %s"
          % (len(beyond), H_EDGE_MAX,
             "the edge census above the cap" if beyond
             else "THE FRAME-A EDGE IS FINITE: this census is all "
             "of it"))
    build_list = cens[:3] if SMOKE else cens
    if SMOKE:
        print("    SMOKE: only the %d lowest-h cells built, the "
              "rest censused SMOKE-SKIPPED (typed)"
              % len(build_list))
    built = []
    cell_meta = {}
    n_guard = 0
    for hz, kz in build_list:
        est = GUARD_FAC * COST_C * float(hz) ** 3
        if time.time() - T0 + est > HARD_CAP_S:
            n_guard += 1
            print("    edge kz %-4d h %-5d UNBUILT-GUARD (projected "
                  "+%.0f s > cap %.0f s) [%.1f s]"
                  % (kz, hz, est, HARD_CAP_S, time.time() - T0),
                  flush=True)
            continue
        r = ob.build_rung("surf", kz, with_split=False)
        leg, why = cell_legal(r)
        band = "*" if KZ_BAND[0] <= kz <= KZ_BAND[1] else " "
        print("    edge kz %-4d h %-5d %-11s%s [%.1f s]"
              % (kz, hz, why, band, time.time() - T0), flush=True)
        cell_meta[(kz, hz)] = why
        if leg:
            built.append(r)
    check("E1 edge scan built %d/%d census cells (%d guard-skipped, "
          "%d illegal)"
          % (len(built), len(build_list), n_guard,
             len(build_list) - n_guard - len(built)),
          len(built) >= (2 if SMOKE else 8), kill="K1")
    edge_rows, n_ref = sweep_steps(built, "EDGE", combined)
    print("    steps: %d wall-legal (%d bridge, %d chain), %d "
          "refused" % (len(edge_rows),
                       sum(1 for r in edge_rows
                           if r["mode"] == "bridge"),
                       sum(1 for r in edge_rows
                           if r["mode"] == "chain"), n_ref))
    edge_rows = jacobi_wards(edge_rows, "edge")
    if KILLS:
        return finish([])

    # per-cell sigma = max over wall-legal steps landing on the cell
    cells = {}
    for r in edge_rows:
        key = (r["kz"], int(r["h"]))
        if key not in cells or r["sigma"] > cells[key]["sigma"]:
            cells[key] = r
    prof = sorted(cells.values(), key=lambda r: (r["h"], r["kz"]))
    check("E2 sigma measured on %d edge cells (all finite)"
          % len(prof),
          len(prof) >= (2 if SMOKE else 8)
          and all(math.isfinite(r["sigma"]) for r in prof),
          kill="K2")
    print("    EDGE PROFILE (h, kz, sigma, mode, anchor)  "
          "[* = breach band kz %d..%d]" % KZ_BAND)
    for r in prof:
        band = "*" if KZ_BAND[0] <= r["kz"] <= KZ_BAND[1] else " "
        print("      h %-5d kz %-4d sigma %.6f %-6s %s %s"
              % (int(r["h"]), r["kz"], r["sigma"], r["mode"],
                 r["anchor"], band))
    sig_e = np.asarray([r["sigma"] for r in prof], float)
    hs_e = np.asarray([r["h"] for r in prof], float)
    edge_max = float(np.max(sig_e))
    i_emax = int(np.argmax(sig_e))
    print("    edge sigma over %d cells: %s; MAX %.6f at kz %d "
          "h %d (%s)" % (len(prof), e3(sig_e), edge_max,
                         prof[i_emax]["kz"], int(prof[i_emax]["h"]),
                         prof[i_emax]["mode"]))
    band_rows = [r for r in prof
                 if KZ_BAND[0] <= r["kz"] <= KZ_BAND[1]]
    band_txt = ("%d cells, sigma %s" % (len(band_rows),
                                        e3([r["sigma"]
                                            for r in band_rows]))
                if band_rows else "no cells")

    # ================================ LAW: the verdict fits
    section("LAW -- the edge h-law (per-cell fit + bin envelope)")
    s1, se1, r21, a1fit = linfit(np.log(hs_e), sig_e)
    print("    per-cell fit: d sigma / d log h = %+.5f +/- %.5f "
          "(2SE), R2 %.3f" % (s1, se1, r21))
    lo, hi = math.log(float(np.min(hs_e))), \
        math.log(float(np.max(hs_e)) + 1.0)
    edges = np.linspace(lo, hi + 1e-9, NBIN + 1)
    binmax = []
    for i in range(NBIN):
        sel = [(math.log(r["h"]) >= edges[i])
               and (math.log(r["h"]) < edges[i + 1]) for r in prof]
        sub = [r for r, s in zip(prof, sel) if s]
        if sub:
            best = max(sub, key=lambda r: r["sigma"])
            binmax.append((i, len(sub), math.log(best["h"]),
                           best["sigma"], best))
    for i, n_in, lh, sv, best in binmax:
        print("      bin %d (n=%2d): envelope %.6f at h %d kz %d"
              % (i, n_in, sv, int(best["h"]), best["kz"]))
    env_x = np.asarray([b[2] for b in binmax], float)
    env_y = np.asarray([b[3] for b in binmax], float)
    s2, se2, r22, a2fit = linfit(env_x, env_y)
    print("    bin-envelope fit (%d bins; unequal bin counts, "
          "honest note: max of a fuller bin is upward-biased): "
          "d sigma_env / d log h = %+.5f +/- %.5f (2SE), R2 %.3f"
          % (len(binmax), s2, se2, r22))
    check("L1 verdict-law fits measured (per-cell + envelope)",
          math.isfinite(s1) and math.isfinite(s2))

    kill_rows = [r for r in edge_rows if r["sigma"] >= KILL_REF]
    growing = (s1 - se1 > 0.0) and (s2 - se2 > 0.0)
    falling = (s1 + se1 < 0.0) and (s2 + se2 < 0.0)
    nonmono = False
    if len(binmax) >= 3:
        inner = max(b[3] for b in binmax[1:-1])
        nonmono = (inner > binmax[0][3] + NM_DELTA
                   and inner > binmax[-1][3] + NM_DELTA)
    h_star = float("nan")
    if s2 > 0.0:
        h_star = math.exp((KILL_REF - a2fit) / s2)
    print("    extrapolation: envelope fit reaches %.2f at h* = %s "
          "(census max h built %d; the census IS finite)"
          % (KILL_REF,
             ("%.3g" % h_star) if math.isfinite(h_star) else "never "
             "(non-positive slope)", int(np.max(hs_e))))
    d_env = ENV_REF - edge_max
    d_reg = SIGMA_ENV_REF - edge_max
    d_kill = KILL_REF - edge_max
    print("    DISTANCES of the edge max %.6f: to 0.665 %+.6f; to "
          "SIGMA_ENV %.6f %+.6f; to the kill line %.2f %+.6f "
          "(t*_num %.4f, frozen report-only)"
          % (edge_max, d_env, SIGMA_ENV_REF, d_reg, KILL_REF,
             d_kill, TSTAR_NUM_REF))
    env_fails = [r for r in edge_rows if r["sigma"] > SIGMA_ENV_REF]
    for r in env_fails[:6]:
        print("      REGISTERED-ENV FAIL (first-class, CCLXIX "
              "no-adjustment clause): kz %d h %d sigma %.6f > "
              "%.6f" % (r["kz"], int(r["h"]), r["sigma"],
                        SIGMA_ENV_REF))
    check("L2 frozen-reference report: %d edge steps >= kill %.2f, "
          "%d > SIGMA_ENV %.6f, %d > 0.665 (references NEVER moved)"
          % (len(kill_rows), KILL_REF, len(env_fails),
             SIGMA_ENV_REF,
             int(np.sum(np.asarray([r["sigma"]
                                    for r in edge_rows]) > ENV_REF))),
          True)

    # ================================ MECH: the mechanism peek
    section("MECH -- the ingredient decomposition at the edge maxima")
    top = sorted(prof, key=lambda r: -r["sigma"])[:TOP_N]
    print("    top %d cells: (h, kz, mode, sigma | b1, a1, mB="
          "[J_B^-1]_11, lamB1, gap | sigma(S2 unrotated, Q-frame "
          "diagnostic))" % len(top))
    for r in top:
        th = r["theta"]
        b1v, a1v = float(th[0]), float(th[NDIM])
        mbv = r["sigma"] * b1v / (a1v * a1v)
        lamb = float(np.linalg.eigvalsh(theta_matrices(th)[1])[0])
        sig_raw, _t = sigma_of_matrix(sym(r["step"]["r2"]["S"]))
        print("      h %-5d kz %-4d %-6s %.6f | %9.4f %10.3f "
              "%.5e %9.4f %8.4f | raw %.6f"
              % (int(r["h"]), r["kz"], r["mode"], r["sigma"], b1v,
                 a1v, mbv, lamb, r["gap"], sig_raw))
    lg_h = np.log(hs_e)
    tha = [r["theta"] for r in prof]
    la1 = np.log([float(t[NDIM]) ** 2 for t in tha])
    lb1 = np.log(np.abs([float(t[0]) for t in tha]))
    lmb = np.log(np.abs([r["sigma"] * float(t[0])
                         / float(t[NDIM]) ** 2
                         for r, t in zip(prof, tha)]))
    lsg = np.log(np.abs(sig_e))
    ss, sse, _r, _a = linfit(lg_h, lsg)
    sa, sae, _r, _a = linfit(lg_h, la1)
    sb, sbe, _r, _a = linfit(lg_h, lb1)
    sm, sme, _r, _a = linfit(lg_h, lmb)
    print("    ingredient h-trends (d log . / d log h, +/- 2SE): "
          "sigma %+.3f+/-%.3f = a1^2 %+.3f+/-%.3f + mB %+.3f+/-%.3f "
          "- b1 %+.3f+/-%.3f (exact decomposition, fit residual "
          "%+.1e)" % (ss, sse, sa, sae, sm, sme, sb, sbe,
                      ss - (sa + sm - sb)))
    br_s = [r["sigma"] for r in edge_rows if r["mode"] == "bridge"]
    ch_s = [r["sigma"] for r in edge_rows if r["mode"] == "chain"]
    print("    mode anatomy: bridge (%d) sigma %s; chain (%d) "
          "sigma %s" % (len(br_s), e3(br_s), len(ch_s), e3(ch_s)))
    check("M1 mechanism decomposition measured on %d cells"
          % len(prof), True)

    # ================================ S: screens
    section("S -- tau / c_h relocation screens on the edge")
    taus = np.asarray([r["tau_scale"] for r in prof], float)
    reloc = []
    seat_txt = []
    ch_cells = [r for r in top if r["h"] <= CH_HMAX][:CH_N]
    ch_vals = {}
    for r in ch_cells:
        ch_vals[(r["kz"], int(r["h"]))] = ch_of_cell(r["kz"])
        print("    c_h(kz %d, h %d) = %.4e [%.1f s]"
              % (r["kz"], int(r["h"]),
                 ch_vals[(r["kz"], int(r["h"]))],
                 time.time() - T0), flush=True)
    n_oos = sum(1 for r in top if r["h"] > CH_HMAX)
    if n_oos:
        print("    %d top cells h > %d typed OUT-OF-SURFACE for c_h "
              "(declared cost cap)" % (n_oos, CH_HMAX))
    chs = np.asarray([ch_vals.get((r["kz"], int(r["h"])),
                                  float("nan")) for r in prof],
                     float)
    for label, arr in (
            ("sigma", sig_e),
            ("margin(0.92-sigma)", KILL_REF - sig_e),
            ("margin(0.7809-sigma)", SIGMA_ENV_REF - sig_e)):
        t1, v1 = screen(arr, taus, "%s vs tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask], "%s vs c_h" % label)
        print("      " + t1 + " | " + t2)
        seat_txt.append("%s:%s/%s" % (label, v1, v2))
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 relocation screens: seats %s (a margin RELOC would "
          "mean the edge constraint is the lock relabeled)"
          % (",".join(reloc) or "none"), not reloc)

    # ================================ C: controls-must-fire
    section("C -- controls on the declared cell kz %d" % CTRL_KZ)
    r_true = ob.build_rung("surf", CTRL_KZ, with_split=False)
    leg_t, _why = cell_legal(r_true)
    rows_t, _n = sweep_steps([r_true] if leg_t else [], "CTRL",
                             combined)
    rows_t = [r for r in rows_t if r["mode"] == "bridge"]
    sig_t = (sigma_of_matrix(rows_t[0]["step"]["Mt"])[0]
             if rows_t else float("nan"))
    r_sm = ob.build_rung("surf", CTRL_KZ, world="smooth")
    fire_sm = (r_sm is None or r_sm["negA"] > 0
               or not cell_legal(r_sm)[0])
    check("C1 SMOOTH violates the wall target on the control cell "
          "(negA %s)" % (r_sm["negA"] if r_sm else "n/a"),
          fire_sm, kill="K4")
    r_sc = ob.build_rung("surf", CTRL_KZ,
                         scramble_seed=SCRAMBLE_SEED)
    leg_sc, why_sc = cell_legal(r_sc)
    sig_sc = float("nan")
    if leg_sc:
        rows_sc, _n = sweep_steps([r_sc], "CTRL-SCR", combined)
        rows_sc = [r for r in rows_sc if r["mode"] == "bridge"]
        if rows_sc:
            sig_sc = sigma_of_matrix(rows_sc[0]["step"]["Mt"])[0]
    fire_sc = ((not leg_sc) or (not math.isfinite(sig_sc))
               or abs(sig_sc - sig_t) >= CTRL_DELTA)
    check("C2 SCRAMBLE breaks the sigma structure: legality %s, "
          "sigma %s vs truth %s (|move| >= %.2f)"
          % (why_sc,
             "%.4f" % sig_sc if math.isfinite(sig_sc) else "n/a",
             "%.4f" % sig_t if math.isfinite(sig_t) else "n/a",
             CTRL_DELTA), fire_sc, kill="K4")
    if KILLS:
        return finish([])

    # ---- verdict
    if kill_rows:
        kb = max(kill_rows, key=lambda r: r["sigma"])
        head = ("EDGE-KILL(sigma %.4f >= %.2f at kz %d h %d -- the "
                "CCLXIX kill criterion fires on a wall-legal edge "
                "step)" % (kb["sigma"], KILL_REF, kb["kz"],
                           int(kb["h"])))
    elif growing:
        head = ("EDGE-GROWING(per-cell %+.4f+/-%.4f, envelope "
                "%+.4f+/-%.4f, extrapolated h*(0.92) = %s; edge max "
                "%.4f at h %d)"
                % (s1, se1, s2, se2,
                   "%.3g" % h_star if math.isfinite(h_star)
                   else "n/a", edge_max, int(prof[i_emax]["h"])))
    elif falling:
        head = ("EDGE-FALLING(per-cell %+.4f+/-%.4f, envelope "
                "%+.4f+/-%.4f; edge max %.4f at h %d, margin to "
                "0.92 %+.4f)"
                % (s1, se1, s2, se2, edge_max,
                   int(prof[i_emax]["h"]), d_kill))
    elif nonmono:
        head = ("EDGE-NONMONOTONE(interior envelope %.4f exceeds "
                "both ends by > %.2f; edge max %.4f at h %d, margin "
                "to 0.92 %+.4f)"
                % (max(b[3] for b in binmax[1:-1]), NM_DELTA,
                   edge_max, int(prof[i_emax]["h"]), d_kill))
    else:
        head = ("EDGE-PLATEAU(level %.4f at h %d; per-cell slope "
                "%+.4f+/-%.4f, envelope %+.4f+/-%.4f both "
                "insignificant; margin to 0.92 %+.4f, to SIGMA_ENV "
                "%+.4f)" % (edge_max, int(prof[i_emax]["h"]), s1,
                            se1, s2, se2, d_kill, d_reg))
    labels = [
        head,
        "ENV-STATUS(%s)" % (
            "REGISTERED ENVELOPE FAILS on %d edge steps (max %.4f "
            "> %.6f, first-class, not repaired)"
            % (len(env_fails), edge_max, SIGMA_ENV_REF)
            if env_fails else
            "registered envelope %.6f HOLDS on all %d edge steps "
            "(max %.4f)" % (SIGMA_ENV_REF, len(edge_rows),
                            edge_max)),
        "BAND(kz %d..%d: %s)" % (KZ_BAND[0], KZ_BAND[1], band_txt),
        "CENSUS(%d cells, %d built, %d guard-skipped, %d "
        "atom-incomplete censused; %d beyond cap %d)"
        % (len(build_list), len(built), n_guard, n_incomplete,
           len(beyond), H_EDGE_MAX),
        "SCREENS(%s)" % "; ".join(seat_txt),
        "CONTROLS(C1 smooth fired, C2 scramble fired)",
        "AMENDMENTS(per smoke disclosure)",
    ]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
