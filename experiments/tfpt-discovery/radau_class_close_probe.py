#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""radau_class_close_probe -- PRIME.ONEBADMODE.RADAU.CLASS.02
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE THREE-LEVER CLOSURE TEST FOR THE JOINT RADAU CLASS.  CCLXXXI
(radau_class_assembly_probe) built the non-circular source-only class

  C_RADAU = C_KS AND n > 0 AND MOM
            AND RADAU_K(nu_0..nu_{2K-2}; c) <= t_R n,

with t_R = 0.7809 and c a certified lower floor of the co-block B.
It proved class-level definiteness numerically but left a reserve leak
at K=5: sup tr R = 1.041073, at the scale corner.  This probe applies
all three named levers, without touching the verification compiler.

 (i) SHARP PIVOT THEOREM.  For the positive B-spectral measure
     dmu = sum_i w_i delta_{x_i}, x_i > 0,
       nu_0 = int 1 dmu,  nu_1 = int x dmu,
       q = int x^{-1} dmu,
     Cauchy-Schwarz gives nu_0^2 <= nu_1 q.  Equivalently,
       nu_1 q - nu_0^2
         = 1/2 sum_ij w_i w_j (x_i-x_j)^2/(x_i x_j) >= 0.
     RAD and t_R>0 therefore imply the SOURCE-ONLY theorem
       n >= RADAU_K/t_R >= q/t_R
         >= nu_0^2/(nu_1 t_R)
         = nu_0 / ((nu_1/nu_0) t_R).
     This replaces CCLXXXI's lossy lambda_max(B)=L step.  The algebra
     is warded in sympy; the inequality is warded on all 85 cells and
     on the adversarial scale corner.  The measured ratio eta =
     nu_1/nu_0 is itself frozen as a log-widened source-only class
     datum; its range and provenance are printed before optimization.

 (ii) PER-MEMBER FLOOR GEOMETRY.  The scalar Radau node c and the
     seven ordered co-block spectral floors f_1..f_7 are carried as
     per-member certified data, not collapsed across members before
     composition.  For each assembled Jacobi co-block, an exact
     rational Sturm recurrence certifies f_j < lambda_j(B), j=1..7.
     The continuous extremal class carries c as a sixteenth variable,
     constrained to the certified range and by B-cI >= 0; RAD is
     evaluated at that datum.  Separately, the sum-rule class is the
     finite union of the certified floor-vector branches.  This
     distinction is explicit: continuous-range sups test robustness;
     catalog-branch geometry is what may sharpen the class-uniform F.

 (iii) TWO-TIER ASSEMBLY.  The K=4 joint class is measured together
     with K=5.  CCLXXIX's complete wall-legal census is consumed as a
     frozen cited premise: 150/151 built cells satisfy K=4 at their
     own floor; the sole exception is F0 kz=45,h=1359, individually
     certified at K=5 with sigma <= 0.726909.  This run rebuilds and
     wards the CCLXXXI 85-cell core, including that exception.  It
     states either a single K=5 tier if the levers close it, or the
     honest two-tier finite assembly.

THE COMPOSED STATEMENT printed by this probe is conditional and fully
typed.  The exact inequalities are the Schur theorem, Gauss-Radau,
interlacing, the sharp pivot Cauchy inequality and exact Sturm floor
certificates.  The filter envelope and optimizer extrema remain
FROZEN-NUMERIC.  The all-h membership question remains open, and the
truth floor caps every reserve margin at 1-0.9727 = 0.0273.  No
all-h statement and NO RH claim is made.

FROZEN PROTOCOL.
 S0 firewall and source-locality AST scans; predecessors read-only.
 R  reproduce CCLXXXI in full: no-go lemma; 42 -> 68 ladder; 17 F0;
    exact floors/Radau wards; class SHA; anti-circularity; membership;
    E0..E5 sups; D2/D3/D4 infima; sum-rule; 11-world controls; screens.
 P  derive and ward the sharp pivot theorem, including scale corner.
 G  certify seven ordered floors per member by exact Sturm recurrence.
 E  rerun K=4/K=5 with eta and with the constrained floor datum.
 F  compare the old uniform sum-rule, sharp-pivot uniform form and
    per-member-floor catalog form.
 T  assemble the single- or two-tier certificate with typed premises.
 X  controls: ratio excluder, overclaimed floor refusal, scale
    invariance, plus every inherited CCLXXXI control.
 S  tau/c_h screens on the new margins.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 required control
silent -> CONTROL-SILENT.

FROZEN BARS.  All CCLXXXI bars are inherited verbatim.  ETA_MARGIN =
0.10 in log width; FLOOR_MARGIN = 0.10 in log width; STURM_ITERS = 48;
RATIO_TIE = 1e-10; FLOOR_TIE = 1e-9; CATALOG_TIE = 1e-8;
FLOOR_CERT_RTOL = 1e-6 (the inherited round-62 quality bar);
CCLXXXI refs E3=0.982778, E4=1.041073, D3=8.325984e-3,
D4=3.792671e-4, D2=-5.740475e2, F_uniform=-0.233276;
CCLXXIX cited census 150/151 at K=4 and kz-45 K=5 bound 0.726909.
Optimizer seed and budgets are inherited; this probe uses 32
multi-starts and 220 DE generations per new full extremum (8/30 in
smoke).  Runtime cap 25 min.

HONEST AMENDMENTS (declared before the frozen run).
 A1 eta=nu_1/nu_0 is added as an explicit measured, log-widened,
    SOURCE-ONLY class datum.  The pointwise sharp pivot inequality is
    a theorem without this envelope; only its class-uniform constant
    uses eta_hi.
 A2 the seven Sturm floors certify the dyadic Jacobi matrix assembled
    from the Lanczos coordinates.  CCLXXVII's scalar c_cert of the
    original assembled wall B is retained for Radau and cross-warded
    against the first Sturm floor; float64-vs-ideal enclosure remains
    the known pg_chain scope edge.
 A3 the continuous floor-variable class is deliberately larger than
    the finite catalog union.  A leak there refutes that robust class;
    closure there is numeric.  The catalog sum-rule never silently
    upgrades to an all-matrix statement outside its declared branch
    premises.
 A4 the 151-cell wall-legal census is cited from CCLXXIX rather than
    rebuilt: rebuilding its TAB2=1.6e7 F5 lane adds no new class
    geometry and would spend the frozen budget twice.  The 85-cell
    CCLXXXI core and kz-45 are rebuilt here.
 A5 every optimizer closure is NUMERIC-GLOBAL only: a found maximum
    is a lower bound on the true supremum.  Analytic-looking reserve
    bounds still consume Rdec, a declared numeric envelope of the
    frozen filter.
 A6 POST-FREEZE AMENDMENT (disclosed).  Frozen-run-1 (SPEC_SHA
    ef9288fc, 511.0 s, 83/83 checks, no kills) printed F3=1.016906
    but F4=0.972698, violating the theorem that the K=4 tier is
    contained in K=5.  The missing gate exposed an optimizer miss,
    not closure.  It also exposed two specification defects: the
    continuous floor datum allowed arbitrary underclaims rather than
    the tight largest certified floor produced by the declared
    round-62 machine, and the composed narrative conflated the open
    analytic sum-rule bound 1.233279 with a numeric optimizer delta.
    Run 2 therefore (only) (1) enforces the inherited 1e-6 certified-
    floor quality bar, (2) seeds every weaker tier with the stronger
    tier's witness and requires nesting, and (3) prints analytic and
    numeric reserve pedigrees separately.  No source range, frozen
    bar, optimizer budget, membership rule or positive threshold is
    relaxed.  The changes make a positive result harder and prevent
    a search miss from being called closure.

SMOKE DISCLOSURE (2026-08-12; ONE declared smoke run before this
freeze).  SMOKE-1 (SPEC_SHA a68b5f2d, 10 contiguous surface rungs +
3 lowest deep rungs -> 11 ladder cells, F0 cap 2 -> 1 substitute
cell, 68.3 s) ran 76 checks: 75 passed and one K3 gate failed only
because the smoke F0 cap does not include the named kz=45,h=1359
cell.  Every symbolic, exact-Sturm, Radau, anti-circularity,
inherited control and new control passed.  The known fake smoke
bridge (kz=177,h=1219; not a frozen 68-step cell) dominated every
reserve sup at tr R=4.850599, so no smoke closure number was consumed.
The sharp pivot ward held on 12/12 cells; eta gave a 3.8x improvement
over the old smoke pivot constant, while the independent MOM-box
edges were (honestly) looser.  THE ONLY post-smoke changes are this
disclosure and a smoke bypass on T1/T2, exactly like the inherited
depth-curve gate: frozen mode still requires kz=45 and its cited
bound.  No bar, optimizer budget, class constraint, control, verdict
or frozen gate changed; the bypass cannot make a frozen positive
result easier.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched.  The only later edit outside this file
is the German CCLXXXV line prepended to experiments/next.txt AFTER the
frozen summary.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/radau_class_close_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/radau_class_close_probe.py
"""
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
from scipy import optimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import radau_class_assembly_probe as rc       # noqa: E402 (READ-ONLY)
import bfloor_perstep_certification_probe as bf  # noqa: E402 (RO)

ETA_MARGIN = 0.10
FLOOR_MARGIN = 0.10
STURM_ITERS = 48
RATIO_TIE = 1.0e-10
FLOOR_TIE = 1.0e-9
CATALOG_TIE = 1.0e-8
FLOOR_CERT_RTOL = 1.0e-6
E3_REF = 0.982778
E4_REF = 1.041073
D3_REF = 8.325984e-3
D4_REF = 3.792671e-4
D2_REF = -5.740475e2
FCLASS_REF = -0.233276
CCLXXIX_TOTAL = 151
CCLXXIX_K4 = 150
KZ45_BOUND5 = 0.726909
NEW_MS = 8 if "--smoke" in sys.argv[1:] else 32
NEW_DE = 30 if "--smoke" in sys.argv[1:] else 220
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()

SOURCE_FUNCS = ("eta_value", "sharp_pivot_lower", "source_slacks")
SOURCE_BANNED = set(rc.CLASS_BANNED) | {
    "coblock_floor", "cert_slack", "sturm_count", "spectral_floors",
}


def configure_predecessor():
    """Route inherited checks into this run and select its smoke mode."""
    rc.CHECKS = []
    rc.KILLS = []
    rc.SMOKE = SMOKE
    rc.T0 = T0


def check(name, ok, detail="", kill=None):
    return rc.check(name, ok, detail, kill)


def section(title):
    rc.section(title)


def source_ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or \
                node.name not in SOURCE_FUNCS:
            continue
        for sub in ast.walk(node):
            name = None
            if isinstance(sub, ast.Name):
                name = sub.id
            elif isinstance(sub, ast.Attribute):
                name = sub.attr
            elif isinstance(sub, ast.arg):
                name = sub.arg
            if name in SOURCE_BANNED:
                bad.append("%s:%s" % (node.name, name))
    return bad


def eta_value(theta):
    """eta=nu_1/nu_0 from moment-local source entries only."""
    mom = rc.moment_vector(theta, 2)
    if len(mom) < 2 or not (mom[0] > 0.0 and mom[1] > 0.0):
        return float("nan")
    return float(mom[1] / mom[0])


def sharp_pivot_lower(nu0, nu1, t_cap):
    """n >= nu0^2/(nu1*t_cap), the source-only Cauchy lower bound."""
    if not (nu0 > 0.0 and nu1 > 0.0 and t_cap > 0.0):
        return float("nan")
    return float(nu0 * nu0 / (nu1 * t_cap))


def ratio_slacks(theta, cls):
    eta = eta_value(theta)
    if not (eta > 0.0) or not math.isfinite(eta):
        return np.asarray([-1.0, -1.0])
    wid = max(math.log(cls["eta_hi"]) - math.log(cls["eta_lo"]),
              1.0e-12)
    return np.asarray([
        (math.log(eta) - math.log(cls["eta_lo"])) / wid,
        (math.log(cls["eta_hi"]) - math.log(eta)) / wid,
    ])


def source_slacks(theta, floor_c, kdeg, cls):
    """Source-only additions: MOM, eta, sharp pivot and RAD."""
    mom = rc.moment_vector(theta, rc.KDEG5)
    piv_lo = sharp_pivot_lower(mom[0], mom[1], cls["t_r"])
    piv = float(theta[0])
    pslack = ((piv - piv_lo) / max(abs(piv), 1.0e-12)
              if math.isfinite(piv_lo) else -1.0)
    return np.concatenate([
        rc.moment_box_con(theta, rc.KDEG5, cls["mlo"], cls["mhi"]),
        ratio_slacks(theta, cls),
        np.asarray([pslack,
                    rc.radau_con(theta, kdeg, floor_c, cls["t_r"])]),
    ])


def cert_slack(theta, floor_c):
    """The tight round-62-style floor premise: c<=lambda_min(B) and
    c is within the inherited certificate-quality bar."""
    _jm, jb = rc.theta_matrices(theta)
    try:
        lam = float(np.linalg.eigvalsh(jb)[0])
    except np.linalg.LinAlgError:
        return np.asarray([-1.0, -1.0])
    scale = max(abs(lam), 1.0)
    return np.asarray([
        (lam - floor_c) / scale,
        (floor_c - (1.0 - FLOOR_CERT_RTOL) * lam) / scale,
    ])


def full_slacks(xvec, kdeg, cls):
    theta = np.asarray(xvec[:-1], float)
    floor_c = float(xvec[-1])
    base, _names = rc.class_slack_vector(theta, cls)
    return np.concatenate([
        base,
        source_slacks(theta, floor_c, kdeg, cls),
        cert_slack(theta, floor_c),
    ])


def exact_sturm_count(diag, off, shift):
    """Exact Jacobi Sturm count: number of eigenvalues below shift."""
    seq = [Fraction(1), diag[0] - shift]
    for k in range(1, len(diag)):
        seq.append((diag[k] - shift) * seq[-1]
                   - off[k - 1] * off[k - 1] * seq[-2])
    signs = []
    for value in seq:
        if value > 0:
            signs.append(1)
        elif value < 0:
            signs.append(-1)
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def spectral_floors(theta):
    """Certified dyadic lower floors for all ordered eigenvalues of B."""
    theta = np.asarray(theta, float)
    diag = [Fraction(float(v)) for v in theta[1:rc.NDIM]]
    off = [Fraction(float(v))
           for v in theta[rc.NDIM + 1:]]
    _jm, jb = rc.theta_matrices(theta)
    truth = np.linalg.eigvalsh(jb)
    floors = []
    for j, eig in enumerate(truth):
        lo = Fraction(0)
        hi = Fraction(float(max(eig * (1.0 + 1.0e-7), 1.0e-14)))
        while exact_sturm_count(diag, off, hi) <= j:
            hi *= 2
        for _ in range(STURM_ITERS):
            mid = (lo + hi) / 2
            if exact_sturm_count(diag, off, mid) <= j:
                lo = mid
            else:
                hi = mid
        floors.append(lo)
    return floors


def freeze_new_data(rows, cls):
    section("P0 -- freeze eta and per-member floor geometry")
    ladder = [r for r in rows if r["seg"] != "F0"]
    etas = np.asarray([eta_value(r["theta"]) for r in ladder], float)
    certs = np.asarray([r["c_cert"] for r in ladder], float)

    def log_widen(values, margin):
        lo = float(np.min(values))
        hi = float(np.max(values))
        width = max(math.log(hi) - math.log(lo), 1.0e-12)
        return (math.exp(math.log(lo) - margin * width),
                math.exp(math.log(hi) + margin * width))

    cls["eta_lo"], cls["eta_hi"] = log_widen(etas, ETA_MARGIN)
    cls["floor_lo"], cls["floor_hi"] = log_widen(certs, FLOOR_MARGIN)
    print("    eta=nu_1/nu_0 truth min/med/max %s; log-widened class "
          "range [%.6e, %.6e]" % (rc.e3(etas), cls["eta_lo"],
                                  cls["eta_hi"]))
    print("    c_cert truth min/med/max %s; log-widened datum range "
          "[%.6e, %.6e]" % (rc.e3(certs), cls["floor_lo"],
                             cls["floor_hi"]))
    frozen = np.asarray([cls["eta_lo"], cls["eta_hi"],
                         cls["floor_lo"], cls["floor_hi"]], float)
    cls["close_sha"] = hashlib.sha256(
        cls["box_sha"].encode("ascii") + frozen.tobytes()).hexdigest()
    check("P0.1 closure class frozen before new optimization "
          "(SHA-256 %s)" % cls["close_sha"][:16], True)


def certify_geometry(rows):
    section("G -- exact-rational per-member seven-floor geometry")
    max_gap = 0.0
    min_gap = float("inf")
    first_tie = 0.0
    n_ok = 0
    for row in rows:
        floors_fr = spectral_floors(row["theta"])
        floors = np.asarray([float(v) for v in floors_fr], float)
        row["spec_floor_fr"] = floors_fr
        row["spec_floor"] = floors
        truth = np.asarray(row["lam_jb"], float)
        gaps = truth - floors
        min_gap = min(min_gap, float(np.min(gaps)))
        max_gap = max(max_gap, float(np.max(
            gaps / np.maximum(1.0, np.abs(truth)))))
        first_tie = max(first_tie, abs(floors[0] - row["c_cert"])
                        / max(1.0, abs(row["c_cert"])))
        if np.all(gaps >= -FLOOR_TIE * np.maximum(1.0,
                                                  np.abs(truth))):
            n_ok += 1
    check("G1 exact Sturm floors f_j <= lambda_j(B) for all seven "
          "ordered modes on %d/%d cells; min slack %.3e"
          % (n_ok, len(rows), min_gap), n_ok == len(rows), kill="K2")
    check("G2 48-step dyadic Sturm floors sit within max rel %.3e "
          "of float truth" % max_gap, max_gap <= 1.0e-6, kill="K2")
    print("    first Sturm floor vs CCLXXVII scalar c_cert: max rel "
          "%.3e (independent exact machines on Jacobi/original B)"
          % first_tie)
    for j in range(rc.NDIM - 1):
        print("    f_%d certified min/med/max %s"
              % (j + 1, rc.e3([r["spec_floor"][j] for r in rows])))


def pivot_theorem(rows, cls, base_tiers):
    section("P -- lever (i): the sharp source-only pivot theorem")
    import sympy as sp
    x, y = sp.symbols("x y", positive=True)
    pair = sp.simplify(
        sp.Rational(1, 2) * (x / y + y / x - 2)
        - (x - y) ** 2 / (2 * x * y))
    check("P1 EXACT sympy pair identity: 1/2(x/y+y/x-2) = "
          "(x-y)^2/(2xy) >= 0", pair == 0, kill="K2")
    defects = []
    chain_defects4 = []
    chain_defects5 = []
    for row in rows:
        nu0, nu1 = float(row["nu"][0]), float(row["nu"][1])
        defects.append(row["q_wall"] * nu1 - nu0 * nu0)
        lo = sharp_pivot_lower(nu0, nu1, cls["t_r"])
        if row["bound4"] <= cls["t_r"] + RATIO_TIE:
            chain_defects4.append(row["n_piv"] - lo)
        if row["bound5"] <= cls["t_r"] + RATIO_TIE:
            chain_defects5.append(row["n_piv"] - lo)
        row["sharp_piv_lo"] = lo
        row["sharp_piv_margin"] = row["n_piv"] - lo
    scale = max(1.0, max(abs(r["q_wall"] * r["nu"][1])
                         for r in rows))
    check("P2 Cauchy moment ward q*nu_1-nu_0^2 >= 0 on all %d "
          "cells: min %.3e (scaled %.3e)"
          % (len(rows), min(defects), min(defects) / scale),
          min(defects) >= -RATIO_TIE * scale, kill="K2")
    check("P3 composed sharp pivot bound holds on every admitted "
          "cell: K=4 %d cells min slack %.3e; K=5 %d cells min "
          "slack %.3e" % (len(chain_defects4), min(chain_defects4),
                          len(chain_defects5), min(chain_defects5)),
          min(chain_defects4) >= -RATIO_TIE
          and min(chain_defects5) >= -RATIO_TIE, kill="K2")
    old = cls["piv_lo"]
    box_new = cls["mlo"][0] ** 2 / (
        cls["mhi"][1] * cls["t_r"])
    ratio_new = cls["mlo"][0] / (cls["eta_hi"] * cls["t_r"])
    cls["piv_lo_box2"] = box_new
    cls["piv_lo_eta"] = ratio_new
    print("    class-uniform pivot floors:")
    print("      old  nu_0_lo/(L*t_R)                 %.9e" % old)
    print("      MOM  nu_0_lo^2/(nu_1_hi*t_R)         %.9e  x%.1f"
          % (box_new, box_new / old))
    print("      ETA  nu_0_lo/(eta_hi*t_R)            %.9e  x%.1f"
          % (ratio_new, ratio_new / old))

    corner = base_tiers["E4"]["theta"]
    ratios = []
    if corner is not None:
        for fac in (1.0, 0.5, 0.2):
            th = np.asarray(corner, float).copy()
            th[0] *= fac * fac
            th[rc.NDIM] *= fac
            mom = rc.moment_vector(th, rc.KDEG5)
            rad = rc.radau_from_entries(
                th, rc.KDEG5, rc.coblock_floor(th))
            ratios.append((eta_value(th), rad / th[0],
                           sharp_pivot_lower(mom[0], mom[1],
                                             cls["t_r"]) / th[0]))
        spread = float(np.max(np.ptp(np.asarray(ratios), axis=0)))
    else:
        spread = float("inf")
    check("P4 adversarial SCALE-CORNER ward: scaling "
          "(n,a1)->(s^2 n,s a1) leaves eta, RADAU_5/n and "
          "n_sharp/n invariant for s=1,.5,.2 (max spread %.3e)"
          % spread, spread <= 1.0e-8, kill="K2")
    print("    EFFECT READING: the theorem sharpens the uniform pivot "
          "constant but is scale-covariant; whether the eta/floor "
          "class closes K=5 is decided by the extremal rerun below.")


def maximize_floor_class(rows, cls, fdata, kdeg, label,
                         inherited_seeds=()):
    lo_t = np.asarray(cls["lo"], float).copy()
    hi_t = np.asarray(cls["hi"], float).copy()
    lo_t[0] = max(0.0, lo_t[0])
    lo = np.concatenate([lo_t, [cls["floor_lo"]]])
    hi = np.concatenate([hi_t, [cls["floor_hi"]]])
    bounds = list(zip(lo, hi))

    def objective(xvec):
        val = rc.tr_r_of_theta(xvec[:-1], fdata)
        return -val if math.isfinite(val) else 1.0e12

    def slacks(xvec):
        return full_slacks(xvec, kdeg, cls)

    def penalized(xvec):
        val = rc.tr_r_of_theta(xvec[:-1], fdata)
        if not math.isfinite(val):
            return 1.0e12
        ss = slacks(xvec)
        viol = float(np.sum(np.clip(-ss, 0.0, None)))
        return -val + rc.PEN_W * viol * viol

    seeds = []
    pick = np.linspace(0, len(rows) - 1,
                       max(2, NEW_MS // 2)).astype(int)
    for idx in sorted(set(pick.tolist())):
        row = rows[idx]
        seeds.append(np.concatenate([
            np.clip(row["theta"], lo_t, hi_t),
            [np.clip(row["c_cert"], cls["floor_lo"],
                     cls["floor_hi"])]])
        )
    for theta in rc.opt_seeds(rows, lo_t, hi_t, NEW_MS):
        cval = np.clip(rc.coblock_floor(theta), cls["floor_lo"],
                       cls["floor_hi"])
        seeds.append(np.concatenate([theta, [cval]]))
    for inherited in inherited_seeds:
        if inherited is not None:
            seeds.insert(0, np.clip(np.asarray(inherited, float),
                                    lo, hi))
    best_v, best_x, n_conv = -float("inf"), None, 0
    cons = [dict(type="ineq", fun=slacks)]
    for seed in seeds[:NEW_MS]:
        try:
            res = optimize.minimize(
                objective, seed, method="SLSQP", bounds=bounds,
                constraints=cons,
                options=dict(maxiter=rc.SLSQP_MAXIT, ftol=1.0e-12))
        except (ValueError, OverflowError):
            continue
        xx = np.clip(res.x, lo, hi)
        if float(np.min(slacks(xx))) >= -rc.FEAS_TOL:
            n_conv += 1
            value = rc.tr_r_of_theta(xx[:-1], fdata)
            if value > best_v:
                best_v, best_x = value, xx
    de = optimize.differential_evolution(
        penalized, bounds=bounds, seed=rc.OPT_SEED, maxiter=NEW_DE,
        popsize=rc.DE_POP, polish=False, tol=1.0e-10, init="sobol")
    for candidate in (np.clip(de.x, lo, hi),):
        try:
            polished = optimize.minimize(
                objective, candidate, method="SLSQP", bounds=bounds,
                constraints=cons,
                options=dict(maxiter=rc.SLSQP_MAXIT, ftol=1.0e-12))
            candidates = (candidate, np.clip(polished.x, lo, hi))
        except (ValueError, OverflowError):
            candidates = (candidate,)
        for xx in candidates:
            if float(np.min(slacks(xx))) >= -rc.FEAS_TOL:
                value = rc.tr_r_of_theta(xx[:-1], fdata)
                if value > best_v:
                    best_v, best_x = value, xx
    truth_best = -float("inf")
    truth_x = None
    for row in rows:
        xx = np.concatenate([row["theta"], [row["c_cert"]]])
        if cls["floor_lo"] <= xx[-1] <= cls["floor_hi"] \
                and float(np.min(slacks(xx))) >= -rc.FEAS_TOL \
                and row["trace_r"] > truth_best:
            truth_best, truth_x = row["trace_r"], xx
    sup = max(best_v, truth_best)
    out = dict(label=label, sup=sup, opt=best_v, truth=truth_best,
               x=best_x if best_v >= truth_best else truth_x,
               src="optimizer" if best_v >= truth_best
               else "truth-in-class")
    print("    %-48s sup tr R = %.6f (%s; optimizer %.6f, "
          "%d/%d feasible starts, truth %.6f) [%.1f s]"
          % (label, sup, out["src"], best_v, n_conv, NEW_MS,
             truth_best, time.time() - T0), flush=True)
    if out["x"] is not None:
        th, floor_c = out["x"][:-1], out["x"][-1]
        rad = rc.radau_from_entries(th, kdeg, floor_c)
        print("      anatomy: n %.6g a1 %.6g eta %.6g c_datum %.6g "
              "lambda_min(B) %.6g RADAU_%d/n %.6f sigma %.6f"
              % (th[0], th[rc.NDIM], eta_value(th), floor_c,
                 rc.coblock_floor(th), kdeg, rad / th[0],
                 rc.sigma_quotient(th)))
    return out


def rerun_extrema(rows, cls, fdata, base):
    section("E+ -- levers (i)/(ii): eta and constrained-floor reruns")
    lo_p = np.asarray(cls["lo"], float).copy()
    hi_p = np.asarray(cls["hi"], float).copy()
    lo_p[0] = 0.0
    pbox = (lo_p, hi_p)

    def mom(theta):
        return rc.moment_box_con(theta, rc.KDEG5, cls["mlo"],
                                 cls["mhi"])

    def eta(theta):
        return ratio_slacks(theta, cls)

    def rad4(theta):
        return rc.radau_self_con(theta, rc.KDEG, cls["t_r"])

    def rad5(theta):
        return rc.radau_self_con(theta, rc.KDEG5, cls["t_r"])

    map_ms = 6 if SMOKE else 24
    map_de = 20 if SMOKE else 180
    out = {}
    out["R3"] = rc.maximize(
        rows, cls, fdata, "R3  E3 + measured eta range (lever i)",
        [mom, eta, rad4], pbox, map_ms, map_de)
    out["R4"] = rc.maximize(
        rows, cls, fdata, "R4  E4 + measured eta range (lever i)",
        [mom, eta, rad5], pbox, map_ms, map_de)

    def inherit_known_witness(result, known):
        theta = known.get("theta")
        if theta is None:
            return
        if float(np.min(result["slacks"](theta))) >= -rc.FEAS_TOL:
            value = rc.tr_r_of_theta(theta, fdata)
            if value > result["sup"]:
                print("      inherited nested-tier witness raises "
                      "%s from %.6f to %.6f"
                      % (result["label"], result["sup"], value))
                result["sup"] = value
                result["theta"] = theta
                result["src"] = "inherited-witness"

    inherit_known_witness(out["R3"], base["E3"])
    inherit_known_witness(out["R4"], base["E4"])
    out["F3"] = maximize_floor_class(
        rows, cls, fdata, rc.KDEG,
        "F3  K=4 + eta + certified floor datum")
    out["F4"] = maximize_floor_class(
        rows, cls, fdata, rc.KDEG5,
        "F4  K=5 + eta + certified floor datum",
        inherited_seeds=(out["F3"]["x"],))
    check("E+.1 TIER NESTING: tight-floor K=4 class is contained in "
          "K=5, hence sup F3 %.6f <= sup F4 %.6f"
          % (out["F3"]["sup"], out["F4"]["sup"]),
          out["F3"]["sup"] <= out["F4"]["sup"] + 1.0e-6,
          kill="K2")
    print("\n    SUP TABLE (NUMERIC-GLOBAL; <1 closes numerically):")
    for key, value in (
            ("CCLXXXI E2 separate envelopes", base["E2"]["sup"]),
            ("CCLXXXI E3 K=4 own spectral floor", base["E3"]["sup"]),
            ("CCLXXXI E4 K=5 own spectral floor", base["E4"]["sup"]),
            ("lever-i R3 K=4 + eta", out["R3"]["sup"]),
            ("lever-i R4 K=5 + eta", out["R4"]["sup"]),
            ("lever-ii F3 K=4 floor datum", out["F3"]["sup"]),
            ("lever-ii F4 K=5 floor datum", out["F4"]["sup"])):
        print("      %-44s %.6f  %s" % (
            key, value, "CLOSES" if value < 1.0 else "LEAKS"))
    print("    lever (i) K=5 effect: %.6f -> %.6f (%+.6f); "
          "lever (ii) final K=5 %.6f"
          % (base["E4"]["sup"], out["R4"]["sup"],
             out["R4"]["sup"] - base["E4"]["sup"], out["F4"]["sup"]))
    return out


def sumrule_close(rows, cls, fdata, base_fclass):
    section("F -- sharpened class-uniform and per-member-floor sum rule")
    rdec, _grid, _vals = rc.r_envelope_builder(fdata, cls)
    good_uniform = math.fsum(rdec(float(v)) for v in cls["jb_floor"])

    def uniform_at(piv_lo):
        lam = rc.lambda_closed(piv_lo, cls["cb"], cls["t_r"])
        return rdec(lam) + good_uniform, lam

    u_old, lam_old = uniform_at(cls["piv_lo"])
    u_box, lam_box = uniform_at(cls["piv_lo_box2"])
    u_eta, lam_eta = uniform_at(cls["piv_lo_eta"])
    check("F1 reproduce CCLXXXI class-uniform F %.6f vs %.6f"
          % (1.0 - u_old, FCLASS_REF),
          SMOKE or abs((1.0 - u_old) - FCLASS_REF) <= 5.0e-3,
          kill="K3")
    print("    uniform good-block term sum_j Rdec(f_j^uniform) = %.6f"
          % good_uniform)
    print("    pivot rung          n_lo          Lambda        sup bound "
          "  F=1-sup")
    for name, piv, lam, upper in (
            ("old-L", cls["piv_lo"], lam_old, u_old),
            ("MOM-CS", cls["piv_lo_box2"], lam_box, u_box),
            ("ETA-CS", cls["piv_lo_eta"], lam_eta, u_eta)):
        print("    %-10s %12.4e %12.4e %12.6f %+12.6f"
              % (name, piv, lam, upper, 1.0 - upper))

    catalog = {}
    for depth, tag in ((rc.KDEG, "4"), (rc.KDEG5, "5")):
        admitted = [r for r in rows
                    if r["bound%d" % depth] <= cls["t_r"]
                    + RATIO_TIE]
        uniform_uppers = []
        point_uppers = []
        validity_uniform = 0
        validity_point = 0
        for row in admitted:
            lam = rc.lambda_closed(cls["piv_lo_eta"],
                                   row["spec_floor"][0], cls["t_r"])
            good = math.fsum(rdec(float(v))
                             for v in row["spec_floor"])
            upper_uniform = rdec(lam) + good
            lam_point = rc.lambda_closed(row["sharp_piv_lo"],
                                         row["spec_floor"][0],
                                         cls["t_r"])
            upper_point = rdec(lam_point) + good
            row["catalog_upper_%s" % tag] = upper_point
            row["catalog_F_%s" % tag] = 1.0 - upper_point
            uniform_uppers.append(upper_uniform)
            point_uppers.append(upper_point)
            if upper_uniform + CATALOG_TIE >= row["trace_r"]:
                validity_uniform += 1
            if upper_point + CATALOG_TIE >= row["trace_r"]:
                validity_point += 1
        worst_uniform = (max(uniform_uppers) if uniform_uppers
                         else float("inf"))
        worst_point = max(point_uppers) if point_uppers else float("inf")
        catalog[tag] = dict(
            depth=depth, admitted=admitted, sup=worst_point,
            sup_uniform=worst_uniform, delta=1.0 - worst_point)
        check("F2.%s catalog composition dominates truth tr R: "
              "uniform %d/%d, pointwise-moment %d/%d"
              % (tag, validity_uniform, len(admitted),
                 validity_point, len(admitted)),
              validity_uniform == len(admitted)
              and validity_point == len(admitted), kill="K2")
        print("    per-member certified-floor catalog K=%d: admitted "
              "%d/%d; global-pivot sup <= %.6f; pointwise-moment "
              "sup <= %.6f, delta = %+.6f"
              % (depth, len(admitted), len(rows), worst_uniform,
                 worst_point, 1.0 - worst_point))
    print("    EFFECT: sharp pivot alone changes the uniform form "
          "%.6f -> %.6f; per-member floor geometry gives K=4 %.6f "
          "and K=5 %.6f."
          % (u_old, u_eta, catalog["4"]["sup"],
             catalog["5"]["sup"]))
    return dict(old=u_old, box=u_box, eta=u_eta, catalog=catalog,
                base_fclass=base_fclass)


def new_controls(rows, cls, base):
    section("X+ -- new controls-must-fire")
    row = rows[len(rows) // 2]
    over = rc.coblock_floor(row["theta"]) * 1.01
    floor_fire = float(np.min(cert_slack(row["theta"], over))) < 0.0
    check("X+.1 overclaimed per-member floor 1.01*lambda_min(B) is "
          "REFUSED by the co-block premise", floor_fire, kill="K4")

    theta = np.asarray(row["theta"], float).copy()
    theta[1] = cls["eta_hi"] * 1.20
    eta_fire = float(np.min(ratio_slacks(theta, cls))) < 0.0
    check("X+.2 measured moment-ratio envelope excludes a synthetic "
          "eta=1.2*eta_hi world", eta_fire, kill="K4")

    corner = base["E4"]["theta"]
    if corner is not None:
        mom = rc.moment_vector(corner, rc.KDEG5)
        theorem_slack = (corner[0]
                         - sharp_pivot_lower(mom[0], mom[1],
                                             cls["t_r"]))
        rad_inside = rc.radau_self_con(
            corner, rc.KDEG5, cls["t_r"]) >= -rc.FEAS_TOL
    else:
        theorem_slack, rad_inside = float("nan"), False
    check("X+.3 sharp pivot theorem is active on the inherited K=5 "
          "scale corner (RAD inside %s, pivot slack %.3e)"
          % (rad_inside, theorem_slack),
          rad_inside and theorem_slack >= -RATIO_TIE, kill="K4")


def new_screens(rows, cls):
    section("S+ -- tau/c_h screens on the new margins")
    ch_map = rc.ch_surface_map(rows)
    taus = np.asarray([r["tau_scale"] for r in rows], float)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in rows], float)
    sharp = np.asarray([r["sharp_piv_margin"] for r in rows], float)
    fcat = np.asarray([r.get("catalog_F_5", float("nan"))
                       for r in rows], float)
    reloc = []
    for label, arr in (("sharp pivot margin", sharp),
                       ("catalog K=5 reserve margin", fcat)):
        t1, v1 = rc.screen(arr, taus, "%s vs tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = rc.screen(arr[mask], chs[mask],
                           "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S+.1 new tau/c_h screens completed; relocation seats %s"
          % (",".join(reloc) or "none"), not reloc)


def assembly(rows, cls, rerun, sumdata):
    section("T -- lever (iii): the typed tier assembly")
    kz45 = sorted((r for r in rows
                   if r["seg"] == "F0" and r["kz"] == 45),
                  key=lambda r: -r["sigma"])[:1]
    target = kz45[0] if kz45 else None
    check("T1 rebuilt CCLXXIX exception is the F0 kz=45 h=1359 "
          "cell", SMOKE or (target is not None
                            and int(target["h"]) == 1359),
          kill="K3")
    if target is not None:
        check("T2 kz-45 certified K=5 bound %.6f reproduces cited "
              "%.6f" % (target["bound5"], KZ45_BOUND5),
              SMOKE or abs(target["bound5"] / KZ45_BOUND5 - 1.0)
              <= 2.0e-3,
              kill="K3")
    k4_core = sum(1 for r in rows
                  if r["bound4"] <= cls["t_r"] + RATIO_TIE)
    check("T3 core membership reproduces 84/85 at K=4 and 85/85 at "
          "K=5: %d/%d and %d/%d"
          % (k4_core, len(rows),
             sum(1 for r in rows
                 if r["bound5"] <= cls["t_r"] + RATIO_TIE),
             len(rows)),
          SMOKE or (k4_core == 84 and len(rows) == 85), kill="K3")

    single_numeric = rerun["F4"]["sup"] < 1.0
    single_sumrule = sumdata["catalog"]["5"]["sup"] < 1.0
    k4_numeric = rerun["R3"]["sup"] < 1.0
    kz_reserve = (1.0 - target["trace_r"] if target is not None
                  else float("nan"))
    two_delta = min(1.0 - rerun["R3"]["sup"], kz_reserve)
    print("    COMPLETE WALL-LEGAL CENSUS (CITED CCLXXIX premise): "
          "K=4 own-floor relation %d/%d; exception kz-45 has "
          "individual exact-rational K=5 sigma bound %.6f."
          % (CCLXXIX_K4, CCLXXIX_TOTAL, KZ45_BOUND5))
    if target is not None:
        print("    rebuilt kz-45 frozen-filter trace tr R = %.6f, "
              "individual reserve %.6f" % (target["trace_r"],
                                           kz_reserve))
    if single_numeric:
        tier = ("SINGLE-TIER K=5 numeric class closure: sup %.6f, "
                "delta %.6f" % (rerun["F4"]["sup"],
                                1.0 - rerun["F4"]["sup"]))
    elif single_sumrule:
        tier = ("SINGLE-TIER K=5 catalog sum-rule closure: sup %.6f, "
                "delta %.6f" % (sumdata["catalog"]["5"]["sup"],
                                sumdata["catalog"]["5"]["delta"]))
    elif k4_numeric and target is not None:
        tier = ("TWO-TIER: K=4 class covers cited 150/151 with "
                "numeric sup %.6f; kz-45 is individually K=5 "
                "certified at %.6f; finite assembled reserve delta "
                "%.6f" % (rerun["R3"]["sup"], target["bound5"],
                          two_delta))
    else:
        tier = "RESIDUAL-OPEN: neither declared tier closes"
    print("\n    TIER ASSEMBLY VERDICT: %s" % tier)

    delta = (1.0 - rerun["F4"]["sup"] if single_numeric
             else sumdata["catalog"]["5"]["delta"]
             if single_sumrule else two_delta)
    if single_sumrule:
        reserve_text = (
            "The frozen Rdec composition on the declared catalog "
            "gives tr R(J) <= %.9f = 1-delta."
            % sumdata["catalog"]["5"]["sup"])
        reserve_pedigree = (
            "This reserve inequality consumes the declared numeric "
            "Rdec envelope; it is not an interval-certified global "
            "optimizer theorem.")
    else:
        reserve_text = (
            "The analytic Rdec composition remains OPEN: its "
            "pointwise catalog upper bound is %.9f (global-pivot "
            "form %.9f), not <1.  Separately, the frozen extremal "
            "search reports the tier statement above with delta "
            "%.9f."
            % (sumdata["catalog"]["5"]["sup"],
               sumdata["catalog"]["5"]["sup_uniform"], delta))
        reserve_pedigree = (
            "That reserve delta is NUMERIC-GLOBAL evidence only, "
            "not a theorem: a found optimizer maximum is a lower "
            "bound on the true supremum.")
    print("""
THE COMPOSED CLASS STATEMENT (verbatim; conditional premises).
Let J=[[n,b^T],[b,B]] be a real symmetric Jacobi matrix in the frozen
C_KS entry/radius/wall class (CCLXXXI box SHA prefix %s).  Give the
member the SOURCE data
  (P1) n>0 and moments nu_k=b^T B^k b, k=0..2K-2;
  (P2) certified ordered co-block floors
       0<f_j<=lambda_j(B), j=1..7, from the exact Sturm/LDL tier;
  (P3) eta=nu_1/nu_0 in [%.9e, %.9e] and the frozen MOM ranges;
  (P4) RADAU_K(nu;f_1)<=t_R n, t_R=%.4f.
Then the theorem inequalities give
  q=b^T B^{-1}b <= RADAU_K < n,
  n >= nu_0^2/(nu_1 t_R),
  lambda_1(J) >= Lambda(n,f_1,t_R)>0,
so J is positive definite.  %s
%s
Typing: Schur, Cauchy interlacing, Gauss-Radau, the Cauchy moment
inequality and exact Sturm decisions are THEOREM/exact tiers; the
class ranges, floor catalog and Rdec are FROZEN constants with the
printed SHAs/provenance; optimizer sups are NUMERIC-GLOBAL only.
Tier scope: %s
Honest residue: membership for all h is NOT proved; the thin-rung
truth member tr R=0.9727 caps any reserve statement at delta<=0.0273;
the finite catalog is not silently enlarged; NO RH claim.
""" % (cls["box_sha"][:16], cls["eta_lo"], cls["eta_hi"],
       cls["t_r"], reserve_text, reserve_pedigree, tier))
    return tier, delta


def reproduce_baseline(rows, cls, fdata):
    tiers = rc.extremal(rows, cls, fdata)
    sub, seat, fclass = rc.sum_rule(rows, cls, fdata, tiers)
    rc.controls(rows, cls, fdata, tiers)
    rc.screens(rows, cls)
    if not SMOKE:
        checks = (
            ("R0.1 CCLXXXI E3 sup", tiers["E3"]["sup"], E3_REF,
             5.0e-3),
            ("R0.2 CCLXXXI E4 sup", tiers["E4"]["sup"], E4_REF,
             5.0e-3),
            ("R0.3 CCLXXXI D3 inf", tiers["D3"]["inf"], D3_REF,
             8.0e-2),
            ("R0.4 CCLXXXI D4 inf", tiers["D4"]["inf"], D4_REF,
             1.5e-1),
            ("R0.5 CCLXXXI D2 inf", tiers["D2"]["inf"], D2_REF,
             8.0e-2),
            ("R0.6 CCLXXXI F_class", fclass, FCLASS_REF, 5.0e-3),
        )
        for name, got, ref, rtol in checks:
            check("%s %.6e vs %.6e" % (name, got, ref),
                  abs(got / ref - 1.0) <= rtol, kill="K3")
    return tiers, sub, seat, fclass


def finish(tier, delta):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _name, ok in rc.CHECKS if ok)
    total = len(rc.CHECKS)
    if rc.KILLS:
        verdict = {
            "K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
            "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT",
        }[rc.KILLS[0]]
    else:
        verdict = "RADAU-CLASS-CLOSE-02(%s; delta %.6f)" % (
            tier, delta)
    print("\n  VERDICT: %s" % verdict)
    print("  HONEST FRAME: experiments-only finite/frozen class result; "
          "all-h membership open; thin-rung cap 0.0273; NO RH claim.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, total, total - passed,
             ",".join(rc.KILLS) if rc.KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if passed == total and not rc.KILLS else 1


def main():
    configure_predecessor()
    section("PRIME.ONEBADMODE.RADAU.CLASS.02 -- residual reserve "
            "closure (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode=%s; experiments-only; NO RH claim"
          % ("SMOKE" if SMOKE else "FROZEN"))
    bad = source_ast_scan()
    check("S0.1 new SOURCE path AST-clean: no sigma/Schur/reserve/"
          "trace/eigensolver/read/identifier", not bad,
          ",".join(sorted(set(bad))), kill="K2")

    rc.no_go_lemma()
    steps, combined = rc.build_ladder()
    if rc.KILLS:
        return finish("not reached", float("nan"))
    artifact = rc.artifact_key_ward(steps)
    f0_cells = rc.build_f0(combined)
    fdata = rc.get_filter(steps, artifact)
    rows = rc.make_rows(steps, f0_cells, artifact, fdata)
    rows = rc.jacobi_identity_wards(rows)
    rc.repro_anchors(rows)
    rc.certify_cells(rows)
    if rc.KILLS:
        return finish("not reached", float("nan"))
    cls = rc.freeze_class(rows, fdata)
    rc.ac_typing(rows, cls)
    rc.membership(rows, cls)

    base, _sub, _seat, base_fclass = reproduce_baseline(
        rows, cls, fdata)
    if rc.KILLS:
        return finish("baseline failed", float("nan"))
    freeze_new_data(rows, cls)
    certify_geometry(rows)
    pivot_theorem(rows, cls, base)
    rerun = rerun_extrema(rows, cls, fdata, base)
    sumdata = sumrule_close(rows, cls, fdata, base_fclass)
    new_controls(rows, cls, base)
    new_screens(rows, cls)
    tier, delta = assembly(rows, cls, rerun, sumdata)
    return finish(tier, delta)


if __name__ == "__main__":
    sys.exit(main())
