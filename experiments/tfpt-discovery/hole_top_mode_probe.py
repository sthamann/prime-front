#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hole_top_mode_probe --
PRIME.RDAGGER.HOLE_TOP_MODE.01 (round 413):
is the defect the top orthogonal polynomial of the hole
measure, and is T0 contractive on that mode's complement?

THE FORMULA (Leg 0, SATZ over Q).  On a positive discrete
measure (Y, ω) with q = |Y| atoms, the Lagrange identity
    Σ_i p(y_i)/P_Y'(y_i) = 0    for all deg p ≤ q-2
makes π_{q-1}^Y(y_i) = c / (ω_i P_Y'(y_i)) the unique
(up to scale) degree-(q-1) OP.  Three bases (mono /
Chebyshev / Newton) give identical samples.  The
√ω-coordinate sample is the source-pure vector
    v_top,i ∝ 1 / (√(ω_i) · P_Y'(y_i)),
built from Y, u^vee, P_Y' only (NO eig, SVD, target).

THE PRIMARY TEST (Leg 1, HTM).  Q = I − v_top v_top^T
(unit v_top).  HTM asks Q (I − T0* T0) Q ⪰ 0, i.e.
#{σ(T0) > 1 on v_top^⊥} = 0.  Min-max would then give
at most one σ(T0) > 1, hence λ_2(C) ≥ 1 (r407/r411
dictionary T*T = C^{-1}).

QD (Leg 2, stronger).  Σ_X u^vee p² ≤ Σ_Y u^vee p² for
all deg p ≤ q-2.  Already the constant p ≡ 1 is the mass
ratio Σ_X u^vee / Σ_Y u^vee.  QD ⇒ HTM via min-norm
(||T z|| ≤ ||p||_X); the converse can fail.

CALIBRATION DISCLOSURE.  Formula, corr(v_top, C-ev0),
projected λ_min, leftover σ, mass ratio, permute/scramble,
mutants, core-42 / χ / EXT first measured in /tmp
(r413_cal.py, r413_cal2.py, r413_cal3.py) on the r409
constructors, 2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall < 15 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: Lagrange 0 fails / 3 bases; π·ω·P' = 1;
    GS last ∝ formula in mono/cheb/newton.
  * w9: corr(v_top, C-ev0) = 0.6766 > Fourier 0.278
    (R410 face vs C-ev0 was 0.386; v_top is better and
    still not the excess).  ||T|| = 1.080138;
    leftover σ_max(v^⊥) = 1.02354; λ_min(proj) = −0.04763;
    n_over = 1.  PRIMARY TEST FAILS ON FLAGSHIP MAIN.
  * QD: mass_X/mass_Y = 1.35713; already p≡1 fails.
    Min-norm does not restore HTM (leftover σ > 1).
  * MAIN core-42: P1 hold 4/28, PD 14/14 (trivial),
    total 18/42.  EXT P1 (119,35,109,69) all break.
  * χ: live-P1 1/37, live-PD 41/41, dead 4/6
    (architecture "dead must hold" FAILS: dead-19/39
    break; death is not HTM-edge).
  * KILLS: PERM n_over=20 λ_min=−54; SCR n_over=20
    λ_min=−217; |P'|-unsigned and random leave σ_max ≈ ||T||;
    constructor audit: no eig/SVD/target.

AUSGANG TOP_MODE_REFUTED.
SATZ: the OP formula and Lagrange identity over Q;
v_top is source-pure; kills 4/5/6 fire.
REFUTED: HTM on MAIN (clean w9 violation, 24/28 P1
windows); QD even for constants; "dead χ hold".
The Nyquist face of v_top is real (corr 0.68) and
not the excess direction (R411: excess = C-ev0).
Reviewer order: one clean MAIN violation closes the
route.  Does not move the mincut.  No RH claim.
No L* claim.  No R-dagger claim.

MACHINERY: r409 B.pack_graph / source_T0_cls / toy;
r407 DI.pack_C; r403 P1.reweight; r226 V; r356 dual
weights.  v_top uses only Y and u^vee.

NO RH CLAIM.  Finite identities, one named refutation.
Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"

FORMULA_HI = 1.0e-10
W9_CORR_LO, W9_CORR_HI = 0.65, 0.72
W9_FOUR_HI = 0.40
W9_OP = 1.080138437
W9_LMIN_HI = -0.02
W9_SMAX_LO, W9_SMAX_HI = 1.020, 1.028
W9_MASS_LO, W9_MASS_HI = 1.35, 1.37
PERM_NOVER_LO = 15
SCR_NOVER_LO = 15
P1_HOLD_HI = 6
P1_BREAK_LO = 20
PD_N = 14
CORE_N = 42
CHI_LIVE = 78
CHI_P1_HOLD_HI = 3
CHI_DEAD_N = 6
HOLD_FLOOR = -1.0e-9
SAMPLE_EXT = HM.SAMPLE_EXT
DEAD_CHI3 = HM.DEAD_CHI3
DEAD_CHI4 = HM.DEAD_CHI4

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; v_top from Y, "
                       "u^vee, P_Y' only"
                       if not bad else "; ".join(bad))


def scope_audit(funcname):
    """v_top constructor: no eig/SVD/target/Cholesky."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"eigvalsh", "eigh", "svd", "cholesky", "lstsq",
              "pinv", "pack_C", "chain_C", "r_nm3", "aug_rung",
              "pack_graph"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def v_top_from_Y(yn, wY):
    """SOURCE-PURE.  v_i ∝ 1/(√ω_i P_Y'(y_i)).  Only Y, u^vee."""
    y = np.asarray(yn, float)
    w = np.asarray(wY, float)
    D = y[:, None] - y[None, :]
    np.fill_diagonal(D, 1.0)
    sgn = np.prod(np.sign(D), axis=1)
    logP = np.sum(np.log(np.maximum(np.abs(D), 1e-300)), axis=1)
    logw = 0.5 * np.log(np.maximum(w, 1e-300))
    logv = -logw - logP
    logv -= float(np.max(logv))
    v = sgn * np.exp(logv)
    nrm = float(np.linalg.norm(v))
    if nrm <= 0.0:
        raise RuntimeError("v_top vanished")
    return v / nrm


def perp_basis(v):
    n = len(v)
    A = np.eye(n)
    A[:, 0] = np.asarray(v, float)
    Q, _ = np.linalg.qr(A)
    return Q[:, 1:]


def htm_of(T, v):
    """Projected form on v^⊥: λ_min and #{σ(T)>1}."""
    v = np.asarray(v, float)
    v = v / (np.linalg.norm(v) + 1e-30)
    N = perp_basis(v)
    ITT = np.eye(len(v)) - (T.T @ T)
    M = N.T @ ITT @ N
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    s = np.linalg.svd(T @ N, compute_uv=False)
    n_over = int(np.sum(s > 1.0 + 1e-9))
    return dict(lmin=float(ev[0]), n_over=n_over,
                smax=float(s[0]) if len(s) else 0.0)


def corr_abs(a, b):
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    return abs(float(np.vdot(a, b))) / (na * nb + 1e-30)


def holds(h):
    return h["lmin"] >= HOLD_FLOOR and h["n_over"] == 0


def Pprime_Q(ys, i):
    pr = Fr(1)
    yi = ys[i]
    for k, yk in enumerate(ys):
        if k != i:
            pr *= (yi - yk)
    return pr


def ip_om(a, b, om):
    return sum(w * x * y for w, x, y in zip(om, a, b))


def gs_last(ys, om, rows):
    vecs = []
    for row in rows:
        v = list(row)
        for u in vecs:
            nu = ip_om(u, u, om)
            if nu == 0:
                continue
            c = ip_om(v, u, om) / nu
            v = [a - c * b for a, b in zip(v, u)]
        vecs.append(v)
    return vecs[-1]


def ratio_const(a, b):
    nz = [(x, y) for x, y in zip(a, b) if y != 0]
    if not nz:
        return False
    r0 = nz[0][0] / nz[0][1]
    return all(x / y == r0 for x, y in nz)


def pack_htm(mz):
    g = B.pack_graph(mz)
    v = v_top_from_Y(g["yn"], g["wY"])
    h = htm_of(g["T0"], v)
    mass = float(g["wX"].sum() / max(float(g["wY"].sum()), 1e-300))
    return dict(g=g, v=v, h=h, mass=mass)


def fourier_face(yn, v):
    th = np.arccos(np.clip(np.asarray(yn, float), -1.0, 1.0))
    o = np.argsort(th)
    n = len(yn)
    t = np.arange(n)
    vF = np.zeros(n)
    vF[o] = np.cos(2.0 * math.pi * (n // 2) * t / float(n))
    vF /= np.linalg.norm(vF) + 1e-30
    return vF


def part_satz():
    section("S1  LEG 0 -- LAGRANGE / OP FORMULA OVER Q")
    xs, _u, ud, iX, iY, d0 = B.toy_dual()
    ys = [xs[i] for i in range(4)]
    om = [ud[i] for i in range(4)]
    q = 4
    fails = 0
    for kind in ("mono", "cheb", "newton"):
        for k in range(q - 1):
            row = [B.basis_row_Q(y, q, kind, ys)[k] for y in ys]
            s = sum(row[i] / Pprime_Q(ys, i) for i in range(q))
            fails += int(s != 0)
    check("G01-lagrange-identity-three-bases",
          fails == 0,
          "Σ p/P' = 0 on deg ≤ q-2, mono/cheb/newton")
    want = [Fr(1) / (om[i] * Pprime_Q(ys, i)) for i in range(q)]
    ok_gs = True
    for kind in ("mono", "cheb", "newton"):
        rows = [[B.basis_row_Q(y, q, kind, ys)[k] for y in ys]
                for k in range(q)]
        got = gs_last(ys, om, rows)
        ok_gs = ok_gs and ratio_const(got, want)
    check("G02-GS-three-bases-match-formula",
          ok_gs,
          "π_{q-1}(y_i) ∝ 1/(ω_i P'(y_i)) in three bases")
    ones = [want[i] * om[i] * Pprime_Q(ys, i) for i in range(q)]
    check("G03-formula-pi-om-Pprime-is-one",
          all(x == Fr(1) for x in ones),
          "π·ω·P' = 1 identically on the 4-atom toy")
    xp = np.array([float(xs[i]) for i in iX])
    yn = np.array([float(xs[i]) for i in iY])
    wX = np.array([float(ud[i]) for i in iX])
    wY = np.array([float(ud[i]) for i in iY])
    T = B.source_T0_cls(xp, wX, yn, wY, d0)
    h = htm_of(T, v_top_from_Y(yn, wY))
    check("G04-toy-HTM-holds",
          holds(h) and float(np.linalg.norm(T, 2)) < 1.0,
          "toy |Y|=2 lmin=%.4f n_over=%d (positive control)"
          % (h["lmin"], h["n_over"]))


def part_w9():
    section("S2  LEG 1 -- PRIMARY TEST ON FLAGSHIP MAIN (w9)")
    mz = V.build_measures(9)
    d = pack_htm(mz)
    g, v, h = d["g"], d["v"], d["h"]
    pk = DI.pack_C(mz)
    evC = np.linalg.eigh(pk["C"])[1][:, 0]
    vF = fourier_face(g["yn"], v)
    cC = corr_abs(v, evC)
    cF = corr_abs(v, vF)
    check("G10-w9-corr-better-than-Fourier-not-excess",
          W9_CORR_LO <= cC <= W9_CORR_HI and cF <= W9_FOUR_HI
          and abs(g["opnorm"] - W9_OP) <= 1e-8,
          "corr(v_top,C-ev0)=%.4f corr(v_top,vF)=%.4f ||T||=%.12f "
          "(better than R410 0.386, not the excess)"
          % (cC, cF, g["opnorm"]))
    check("G11-w9-primary-FAILS",
          h["lmin"] <= W9_LMIN_HI and h["n_over"] >= 1
          and W9_SMAX_LO <= h["smax"] <= W9_SMAX_HI,
          "λ_min(proj)=%.6f n_over=%d σ_max(v^⊥)=%.6f  "
          "TOP_MODE_REFUTED on flagship MAIN"
          % (h["lmin"], h["n_over"], h["smax"]))
    check("G12-leftover-sigma-not-below-one",
          h["smax"] > 1.0 and h["smax"] < g["opnorm"] - 0.01,
          "projecting v_top cuts ||T|| %.6f → %.6f, still > 1"
          % (g["opnorm"], h["smax"]))
    return dict(mz=mz, d=d, pk=pk, cC=cC, cF=cF)


def part_qd(w9):
    section("S3  LEG 2 -- QD INDEPENDENT (stronger form)")
    d = w9["d"]
    check("G20-QD-constants-FAIL",
          W9_MASS_LO <= d["mass"] <= W9_MASS_HI,
          "Σ_X u^vee / Σ_Y u^vee = %.6f > 1  (p≡1 already "
          "breaks QD; LOWER_DEGREE_DOMINANCE dead)"
          % d["mass"])
    z = np.sqrt(np.maximum(d["g"]["wY"], 0.0))
    z = z / (np.linalg.norm(z) + 1e-30)
    nT = float(np.linalg.norm(d["g"]["T0"] @ z))
    check("G21-min-norm-saves-constants-not-excess",
          nT < 1.0 and d["h"]["smax"] > 1.0,
          "||T v_1||=%.6f < 1 (min-norm saves p≡1) but "
          "σ_max(v_top^⊥)=%.6f > 1 (does not save HTM)"
          % (nT, d["h"]["smax"]))


def part_kills(w9):
    section("S4  LEG 3 -- KILLS (gates 4/5/6)")
    mz = w9["mz"]
    g = w9["d"]["g"]
    vC = np.linalg.eigh(w9["pk"]["C"])[1][:, 0]
    mzP = P1.reweight(mz, "permute", 1000)
    dP = pack_htm(mzP)
    check("G30-permute-breaks-primary",
          dP["h"]["n_over"] >= PERM_NOVER_LO
          and dP["h"]["lmin"] < -1.0,
          "PERM n_over=%d λ_min=%.2f ||T||=%.3f"
          % (dP["h"]["n_over"], dP["h"]["lmin"], dP["g"]["opnorm"]))
    dS = pack_htm(HM.scramble_mz())
    check("G31-scramble-breaks-primary",
          dS["h"]["n_over"] >= SCR_NOVER_LO
          and dS["h"]["lmin"] < -1.0,
          "SCR n_over=%d λ_min=%.2f ||T||=%.2f"
          % (dS["h"]["n_over"], dS["h"]["lmin"], dS["g"]["opnorm"]))
    y = np.asarray(g["yn"], float)
    D = y[:, None] - y[None, :]
    np.fill_diagonal(D, 1.0)
    logP = np.sum(np.log(np.maximum(np.abs(D), 1e-300)), axis=1)
    logw = 0.5 * np.log(np.maximum(g["wY"], 1e-300))
    logv = -logw - logP
    logv -= float(np.max(logv))
    v_abs = np.exp(logv)
    v_abs /= np.linalg.norm(v_abs)
    h_abs = htm_of(g["T0"], v_abs)
    check("G32-mutant-unsigned-Pprime-useless",
          h_abs["smax"] >= g["opnorm"] - 0.01
          and corr_abs(v_abs, vC) < 0.10,
          "|P'| corr=%.4f σ_max=%.6f ≈ ||T|| (signs carry "
          "the Nyquist face; dropping them is a no-op)"
          % (corr_abs(v_abs, vC), h_abs["smax"]))
    rng = np.random.default_rng(413)
    v_r = rng.normal(size=len(g["yn"]))
    v_r /= np.linalg.norm(v_r)
    h_r = htm_of(g["T0"], v_r)
    check("G33-mutant-random-useless",
          h_r["smax"] >= g["opnorm"] - 0.01
          and h_r["n_over"] >= 1,
          "random σ_max=%.6f n_over=%d (projection of a "
          "non-mode is worthless)"
          % (h_r["smax"], h_r["n_over"]))
    xu = np.asarray(mz["xu"], float)
    wu = np.abs(np.asarray(mz["wu"], float))
    iY = np.searchsorted(xu, g["yn"])
    v_u = v_top_from_Y(g["yn"], wu[iY])
    h_u = htm_of(g["T0"], v_u)
    check("G34-mutant-raw-u-not-uvee",
          h_u["n_over"] >= 1 and corr_abs(v_u, vC) < 0.25,
          "ω=u (not u^vee) corr=%.4f n_over=%d σ_max=%.6f"
          % (corr_abs(v_u, vC), h_u["n_over"], h_u["smax"]))
    dL = pack_htm(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = pack_htm(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G35-chi9-trivial-dead15-razor",
          holds(dL["h"]) and dL["g"]["opnorm"] < 1.0
          and holds(dD["h"]) and dD["g"]["opnorm"] > 1.0,
          "chi9 ||T||=%.6f HOLD (PD-trivial); dead-15 "
          "||T||=%.6f HOLD razor (not the rule: dead-19 "
          "breaks in the census)"
          % (dL["g"]["opnorm"], dD["g"]["opnorm"]))


def part_census(smoke):
    section("S5  CENSUS -- MAIN 42 / χ 78+dead / EXT")
    if smoke:
        section("S5b  core/chi/EXT skipped (--smoke)")
        return
    core = list(V.admissible_indices())
    p1_hold = p1_n = pd_hold = pd_n = 0
    for kz in core:
        d = pack_htm(V.build_measures(kz))
        ok = holds(d["h"])
        if d["g"]["opnorm"] <= 1.0:
            pd_n += 1
            pd_hold += int(ok)
        else:
            p1_n += 1
            p1_hold += int(ok)
    check("G40-main-P1-refuted-PD-trivial",
          p1_n + pd_n == CORE_N
          and pd_n == PD_N and pd_hold == PD_N
          and p1_hold <= P1_HOLD_HI
          and (p1_n - p1_hold) >= P1_BREAK_LO,
          "core-%d: P1 hold %d/%d (≤%d); PD %d/%d trivial; "
          "MAIN HOLD is not a theorem"
          % (CORE_N, p1_hold, p1_n, P1_HOLD_HI, pd_hold, pd_n))
    live_p1_h = live_p1 = live_pd_h = live_pd = 0
    dead_h = dead_n = dead_p1_break = 0
    for q, lpq, dead in ((DMF.Q_CHI3, DMF.LPQ3, DEAD_CHI3),
                         (DMF.Q_CHI4, DMF.LPQ4, DEAD_CHI4)):
        for kz in core:
            mz = HM.chi_mz(kz, q, lpq)
            if mz is None:
                continue
            d = pack_htm(mz)
            ok = holds(d["h"])
            is_dead = kz in dead
            is_pd = d["g"]["opnorm"] <= 1.0
            if is_dead:
                dead_n += 1
                dead_h += int(ok)
                if (not is_pd) and not ok:
                    dead_p1_break += 1
            elif is_pd:
                live_pd += 1
                live_pd_h += int(ok)
            else:
                live_p1 += 1
                live_p1_h += int(ok)
    check("G41-chi-live-P1-refuted",
          live_p1 + live_pd == CHI_LIVE
          and live_p1_h <= CHI_P1_HOLD_HI
          and live_pd_h == live_pd,
          "χ live %d: P1 hold %d/%d; PD %d/%d trivial"
          % (live_p1 + live_pd, live_p1_h, live_p1,
             live_pd_h, live_pd))
    check("G42-chi-dead-not-all-hold",
          dead_n == CHI_DEAD_N and dead_h < dead_n
          and dead_p1_break >= 1,
          "dead χ hold %d/%d (architecture wanted all); "
          "dead-P1 breaks ≥1 (death is not HTM-edge)"
          % (dead_h, dead_n))
    ext_p1_break = ext_pd_hold = ext_n = 0
    for kz in SAMPLE_EXT:
        d = pack_htm(V.build_measures(kz))
        ok = holds(d["h"])
        ext_n += 1
        if d["g"]["opnorm"] <= 1.0:
            ext_pd_hold += int(ok)
        elif not ok:
            ext_p1_break += 1
    check("G43-EXT-P1-breaks",
          ext_n == len(SAMPLE_EXT) and ext_p1_break >= 3,
          "EXT %s: P1 breaks %d (119/35/109/69)"
          % (SAMPLE_EXT, ext_p1_break))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("hole_top_mode_probe -- "
          "PRIME.RDAGGER.HOLE_TOP_MODE.01 (round 413)")
    print("SPEC_SHA %s   (B %s / DI %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], DI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + χ 78+dead + EXT)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA + CONSTRUCTOR AUDIT")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / DI %s / HM %s / P1 %s"
          % (B.SPEC_SHA[:8], DI.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], P1.SPEC_SHA[:8]))
    leak = scope_audit("v_top_from_Y")
    check("G00c-constructor-no-eig-svd-target",
          leak == [],
          "v_top_from_Y clean" if not leak else "; ".join(leak))

    part_satz()
    w9 = part_w9()
    part_qd(w9)
    part_kills(w9)
    part_census(smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "TOP_MODE_REFUTED: formula SATZ; HTM fails on "
          "flagship MAIN (leftover σ=1.024); QD fails for "
          "p≡1; route closed.  No RH / L* / R-dagger claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "TOP_MODE_REFUTED"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("HOLE TOP MODE %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("HOLE TOP MODE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
