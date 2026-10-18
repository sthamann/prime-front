#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""delta_deformation_probe -- LEMMA.DELTA_DEFORMATION.01 (round 388):
THE Delta-DEFORMATION, the C_eps closing attempt after r381/r385.

Coexistence: r381 reduced G_eps to G_eps^mu ^ C_eps ^ R2, with
C_eps: |FO_k[-nu]| <= 1/32 on the last twelve, and R2 the
Taylor remainder of mu -> mu-nu (Fejer-ref |quad|/|lin|=1.013
at n=40, not dominated).  r385 proved FO_k[-nu]=gamma_k
(Q_k-Q_{k-1}) and split Q = Q^T + Delta, with Delta the
mu-OP deformation off Chebyshev (max 0.335 at w9).  This
round asks whether a Szego/Geronimus bound on consecutive
Delta, plus R2 on the mu-reference, closes C_eps.

THE FROZEN QUESTION.  |Delta_k - Delta_{k-1}| small enough
that |FO_k|=gamma_k |Q_k-Q_{k-1}| <= 1/32 on the last twelve,
from a proved bound on the mu-deformation of Chebyshev?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Deformation machinery: mu = Fejer x (1+eps) on a fixed
     cosine grid; candidate |dDelta| <= C * osc(eps on nu).
     Does consecutive Q see local osc rather than ||eps||_inf?
  B  The right R2 reference: mu-chain as base, -nu as the
     step (the r381 split).  |quad|/|lin| < 1/4 would make
     R2 a Neumann SATZ and collapse the reduction to
     G_eps^mu ^ C_eps.
  C  Combine A+B: explicit Delta-diff bound + dominated R2
     => C_eps?  Name what of G_eps^mu remains.
  D  Kills: scramble must break the osc bound; mutants
     (C x 2, wrong reference); two-period as control
     deformation (eps=0).

CALIBRATION DISCLOSURE.  Identities, w9 Delta/FO/eps, R2
midpoint ratios on the mu-path and the Fejer-path, scramble
osc vs dDelta, two-period eps=0, and the core-42 / MAIN-85 /
chi3-42 tallies were first measured in /tmp (r388_cal.py,
r388_cal2.py) on the same constructors, 2026-08-28.  Frozen
floors/ceilings below are that measurement, sealed as gates.
No two-commit pre-blind freeze: pins disclosed.  Builder
fallback: MAIN-85 + chi3-42 (no 181-pack).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Split FO = gamma (dQ^T + dDelta) exact (w9 last-12 residual
    2e-15).  w9: |FO|12=0.00978, dQ12=0.03868, dQT12=0.01969,
    dDelta12=0.04946, Dmax=0.3347, g12=0.2761.
  * Fejer-stripped ||eps_mu||_inf=5.166, osc(eps on nu)=8.764,
    C_emp=dDelta/osc=0.0056.  Core-42: corr(dQ, einf)=0.025,
    corr(dD, osc_nu)=-0.287 -- consecutive Q is NOT controlled
    by amplitude or by range-osc (both grow 5->120 with N).
  * osc-majorant g (dQT + C* osc) with C*=0.0056 reaches 0.191
    > 1/32 on core-42 (closes on 5/42).  C x 2 on w9 already
    exceeds 1/32 (maj=0.0328).
  * R2 mu-path n=40: |quad|/|lin|_12=0.8615 (Fejer-path 1.0127
    reproduced).  Full n=182: 0.6403.  Small-N n=40 range
    0.559..1.126, all > 1/4.  Exact |R2|/|FO| last-12 full
    = 4.19 -- Neumann domination REFUTED.
  * Small-N last-12 |FO| MAIN 0.01182, chi3 0.01541, both
    < 1/32 (11 windows N<=220).
  * SCRAMBLE seed=1: osc_nu=3.54 < MAIN 8.76 but dDelta12=2.16e6
    (C_emp=6.1e5).  Named kill of any C that works on MAIN.
  * Two-period S=81 c=2/3: eps=0, FO=0, dDelta=0 (control:
    Fejer-pure => consecutive Delta vanishes).

AUSGANG REDUZIERT.  SATZ: the split FO=gamma(dQ^T+dDelta);
monic gamma homogeneous in total mass; Fejer-pure (eps=0)
implies FO=0.  The osc-Geronimus candidate does not close
C_eps (true-but-useless majorant, scramble kill).  R2 on
the mu-reference is not dominated.  Remaining, strictly
the r381 triple: C_eps as cancelled last-12 pairing (not
an eps-size bound); R2 of the finite mu->mu-nu step;
G_eps^mu as the Jacobi box of Fejer x d_arm (r342 dictionary
v_pred < 1e-4 is the right language for the sibling).

MACHINERY: r226 hirota_sign.window_data, r283
verify_lstar_instance.build_measures / mu_chain, r330
chi_build_measures, r381 FO dictionary, r385 Q/Q^T/Delta.

NO RH CLAIM.  Finite identities, a named reduction, named
kills.  Research documentation, not a theorem of RH.
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

import hirota_sign_probe as HS  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import lstar_margin_scaling_probe as LM  # noqa: E402

SCR_SEED = 1
CEPS = 1.0 / 32.0
NEUMANN = 0.25
MAIN_KZ = 9
C_FLANK = 2.0 / 3.0
CORE_N = 42
MAIN_N = 85
CHI3_N = 42
SMALLN_FO_N = 11
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT5_KZ = (69, 107, 101, 99, 115, 89)
EXT6_KZ = (133, 129, 124, 117)

# disclosed /tmp pins
W9_FO12_BAR = 0.012
W9_DQ_LO, W9_DQ_HI = 0.030, 0.050
W9_DQT_LO, W9_DQT_HI = 0.015, 0.025
W9_DD_LO, W9_DD_HI = 0.040, 0.060
W9_EINF_LO, W9_EINF_HI = 5.0, 5.4
W9_OSC_LO, W9_OSC_HI = 8.0, 9.5
W9_CEMP_BAR = 0.007
W9_G12_LO, W9_G12_HI = 0.26, 0.29
R2_MU40_LO, R2_MU40_HI = 0.80, 0.95
R2_FJ40_LO, R2_FJ40_HI = 0.95, 1.10
R2_MU_FULL_LO, R2_MU_FULL_HI = 0.55, 0.75
R2_OVER_FO_FLOOR = 2.0
SCR_OSC_HI = 4.5
SCR_DD_FLOOR = 1.0e5
CORE_CORR_EINF_BAR = 0.15
CORE_CORR_OSC_BAR = 0.40
CSTAR_HALF_FAIL_MIN = 4
OSC_MAJ_CLOSE_MAX = 10
SMALLN_FO_BAR = CEPS
CHI3_SMALL_FO_BAR = CEPS
SPLIT_BAR = 1.0e-12
FO_ID_BAR = 1.0e-12

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
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "build_measures / chi_build_measures only"
                       if not bad else "; ".join(bad))


def mu_Qk(xp, wp, yn, vn, depth):
    a, b, h0 = V.mu_chain(xp, wp, depth)
    u = np.ones_like(yn) / math.sqrt(h0)
    um = np.zeros_like(yn)
    Q = np.empty(depth)
    Q[0] = float(np.dot(vn, u * u))
    for i in range(depth - 1):
        r = (yn - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        Q[i + 1] = float(np.dot(vn, u * u))
    return Q, b, h0


def qcheb_all(xp, wp, yn, vn, depth):
    thy = np.arccos(np.clip(yn, -1.0, 1.0))
    thx = np.arccos(np.clip(xp, -1.0, 1.0))
    ks = np.arange(depth)[:, None]
    num = (vn[None, :] * (1.0 + np.cos(2.0 * ks * thy[None, :]))).sum(1)
    den = (wp[None, :] * (1.0 + np.cos(2.0 * ks * thx[None, :]))).sum(1)
    return num / np.maximum(den, 1e-30)


def eps_fejer(x, w):
    fe = np.maximum(1.0 - np.asarray(x, float), 1e-15)
    d = np.asarray(w, float) / fe
    d = d / float(np.mean(d))
    return d - 1.0


def signed_chain(xs, ws, ys, vs, n_upto):
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    gams = []
    for _n in range(n_upto):
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if _n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
        sc = max(float(np.max(np.abs(px))),
                 float(np.max(np.abs(py))), 1e-300)
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qx, qy = px / sc, py / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        gams.append((eta / eta_m) * math.exp(2.0 * (Ls - Ls_m)))
    return np.array(gams)


def mu_gams(x, w, n_upto):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    h = float(np.sum(w * q * q))
    hs = [h]
    gams = []
    for k in range(n_upto):
        alh = float(np.sum(w * x * q * q)) / h
        px = ((x - alh) * q if k == 0
              else (x - alh) * q - (h / hs[-2]) * qm)
        qm, q = q, px
        hs.append(float(np.sum(w * q * q)))
        gams.append(hs[-1] / hs[-2])
        h = hs[-1]
    return np.array(gams)


def last12_ratio(g0, g1, gh):
    lin = g1 - g0
    quad = g1 - 2.0 * gh + g0
    lin_m = float(np.max(np.abs(lin[-12:])))
    quad_m = float(np.max(np.abs(quad[-12:])))
    return quad_m / max(lin_m, 1e-12), lin_m, quad_m


def midpoint_mu_nu(xp, wp, yn, vn, n):
    g0 = signed_chain(xp, wp, yn, 0.0 * vn, n)
    g1 = signed_chain(xp, wp, yn, vn, n)
    gh = signed_chain(xp, wp, yn, 0.5 * vn, n)
    return last12_ratio(g0, g1, gh) + (g0, g1)


def midpoint_fejer(xs, ws, ys, vs, n):
    fejer_x = np.maximum(1.0 - xs, 1e-15)
    fejer_y = np.maximum(1.0 - ys, 1e-15)
    wx = fejer_x * (float(ws.sum()) / float(np.sum(fejer_x)))
    wy = fejer_y * (float(vs.sum()) / float(np.sum(fejer_y)))

    def g_of(t):
        wxt = (1.0 - t) * wx + t * ws
        wyt = (1.0 - t) * wy + t * vs
        return signed_chain(xs, wxt, ys, wyt, n)

    return last12_ratio(g_of(0.0), g_of(1.0), g_of(0.5))


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S)


def pearson(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.std() < 1e-18 or b.std() < 1e-18:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def stieltjes_exact(nodes, wts, n_upto):
    pk = [Fr(1)] * len(nodes)
    pkm = [Fr(0)] * len(nodes)
    hs = [sum(w * p * p for w, p in zip(wts, pk))]
    beta = []
    for _k in range(n_upto):
        a = sum(w * x * p * p
                for w, x, p in zip(wts, nodes, pk)) / hs[-1]
        b = hs[-1] / hs[-2] if len(hs) > 1 else Fr(0)
        nx = [(x - a) * p - b * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(sum(w * p * p for w, p in zip(wts, pk)))
        beta.append(hs[-1] / hs[-2])
    return beta


def deform_row(xp, wp, yn, vn, depth):
    depth = min(depth, len(xp) - 2)
    Q, b, _ = mu_Qk(xp, wp, yn, vn, depth)
    QT = qcheb_all(xp, wp, yn, vn, depth)
    Dlt = Q - QT
    g12 = float(np.max(b[-12:] ** 2))
    fo12 = float(np.max(np.abs((b[-12:] ** 2) * np.diff(Q[-13:]))))
    dQ12 = float(np.max(np.abs(np.diff(Q[-13:]))))
    dQT12 = float(np.max(np.abs(np.diff(QT[-13:]))))
    dD12 = float(np.max(np.abs(np.diff(Dlt[-13:]))))
    split = float(np.max(np.abs(
        np.diff(Q[-13:]) - np.diff(QT[-13:]) - np.diff(Dlt[-13:]))))
    eps_mu = eps_fejer(xp, wp)
    eps_nu = eps_fejer(yn, vn)
    einf = float(np.max(np.abs(eps_mu)))
    osc_nu = float(np.max(eps_nu) - np.min(eps_nu))
    return dict(
        Q=Q, b=b, QT=QT, Dlt=Dlt, fo12=fo12, dQ12=dQ12, dQT12=dQT12,
        dD12=dD12, g12=g12, split=split, einf=einf, osc_nu=osc_nu,
        C_emp=dD12 / max(osc_nu, 1e-12),
        Q12=float(np.max(Q[-12:])), depth=depth,
    )


def main_ladder():
    core_kzs = list(V.admissible_indices())
    lm_rows = LM.ext_rule()
    ext_kzs = [t[1] for t in lm_rows[:15]]
    all_main = (core_kzs + ext_kzs + list(EXT3_KZ_B + EXT3_KZ_A)
                + list(EXT4_KZ_B + EXT4_KZ_A) + list(EXT5_KZ)
                + list(EXT6_KZ))
    return core_kzs, all_main


def part_a_standalone():
    section("S1  LEG A -- HOMOGENEITY, SPLIT, FEJER-PURE, NEUMANN BAR")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1, 5)] * 5
    b1 = stieltjes_exact(nodes, wts, 3)
    wts3 = [Fr(3) * w for w in wts]
    b3 = stieltjes_exact(nodes, wts3, 3)
    check("G01-gamma-homogeneous-Q",
          b1 == b3,
          "monic gamma invariant under w -> 3w, n=3 exact over Q")

    # 3-atom (3,-2,3) at (-1,0,1): Q0=1/2, FO_1 = gamma_1 (Q1-Q0)
    # used as the split skeleton: dQ = dQT + dDelta is definitional
    h0 = Fr(4)
    q0 = Fr(2) / Fr(4)
    check("G02-one-Rayleigh-split-skeleton",
          h0 * (Fr(1) - q0) == Fr(2) and q0 == Fr(1, 2),
          "h0(1-Q0)=2; the FO split is FO=gamma(dQ^T+dDelta)")

    mz = two_period(21, C_FLANK)
    eps = eps_fejer(mz["xp"], mz["wp"])
    Q, b, _ = mu_Qk(mz["xp"], mz["wp"], mz["yn"], mz["vn"], 8)
    fo = float(np.max(np.abs((b[-4:] ** 2) * np.diff(Q[-5:]))))
    check("G03-Fejer-pure-eps0-FO0",
          float(np.max(np.abs(eps))) < 1e-12
          and float(np.max(Q) - np.min(Q)) < 1e-12
          and fo < 1e-12,
          "S=21 c=2/3 ||eps||=%.3e Qspan=%.3e FO=%.3e"
          % (float(np.max(np.abs(eps))),
             float(np.max(Q) - np.min(Q)), fo))

    check("G04-Neumann-bar-is-1/4",
          NEUMANN == 0.25 and NEUMANN < 0.5,
          "domination criterion |quad|/|lin| < 1/4 (not met below)")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 Delta, R2 mu-ref, kills")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    xp, wp, yn, vn = mz["xp"], mz["wp"], mz["yn"], mz["vn"]
    r9 = deform_row(xp, wp, yn, vn, N - 1)
    check("G10-w9-Delta-FO-eps",
          r9["fo12"] < W9_FO12_BAR and r9["fo12"] < CEPS
          and W9_DQ_LO < r9["dQ12"] < W9_DQ_HI
          and W9_DQT_LO < r9["dQT12"] < W9_DQT_HI
          and W9_DD_LO < r9["dD12"] < W9_DD_HI
          and W9_EINF_LO < r9["einf"] < W9_EINF_HI
          and W9_OSC_LO < r9["osc_nu"] < W9_OSC_HI
          and r9["C_emp"] < W9_CEMP_BAR
          and W9_G12_LO < r9["g12"] < W9_G12_HI,
          "FO=%.5f dQ=%.5f dQT=%.5f dD=%.5f einf=%.3f osc=%.3f "
          "Cemp=%.4f g=%.4f" % (
              r9["fo12"], r9["dQ12"], r9["dQT12"], r9["dD12"],
              r9["einf"], r9["osc_nu"], r9["C_emp"], r9["g12"]))

    check("G11-FO-split-identity",
          r9["split"] < SPLIT_BAR,
          "dQ - (dQT + dDelta) last-12 maxdev=%.3e" % r9["split"])

    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    rat_mu, lin_mu, qd_mu, g0_40, g1_40 = midpoint_mu_nu(
        xs, ws, ys, vs, 40)
    rat_fj, lin_fj, qd_fj = midpoint_fejer(xs, ws, ys, vs, 40)
    check("G12-R2-mu-path-n40-not-dominated",
          R2_MU40_LO < rat_mu < R2_MU40_HI and rat_mu > NEUMANN,
          "|quad|/|lin|=%.4f lin=%.5f quad=%.5f (> 1/4)"
          % (rat_mu, lin_mu, qd_mu))
    check("G13-R2-Fejer-path-n40-reproduced",
          R2_FJ40_LO < rat_fj < R2_FJ40_HI,
          "|quad|/|lin|=%.4f (r381 was 1.013) lin=%.5f quad=%.5f"
          % (rat_fj, lin_fj, qd_fj))

    maj_c2 = r9["g12"] * (r9["dQT12"] + 2.0 * r9["C_emp"] * r9["osc_nu"])
    check("G14-mutant-Cx2-misses-Ceps",
          maj_c2 > CEPS,
          "w9 majorant with 2 C_emp = %.4f > 1/32 (closes at C_emp, "
          "C x 2 already overshoots)" % maj_c2)

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    rs = deform_row(ds["xs"], ds["ws"], ds["ys"], ds["vs"], 183)
    check("G15-scramble-breaks-osc-bound",
          rs["osc_nu"] < SCR_OSC_HI
          and rs["osc_nu"] < r9["osc_nu"]
          and rs["dD12"] >= SCR_DD_FLOOR,
          "SCR osc=%.3f < MAIN %.3f but dDelta=%.3e (Cemp=%.3e)"
          % (rs["osc_nu"], r9["osc_nu"], rs["dD12"], rs["C_emp"]))

    mz23 = two_period(81, C_FLANK)
    rt = deform_row(mz23["xp"], mz23["wp"], mz23["yn"], mz23["vn"], 40)
    check("G16-two-period-control-eps0",
          rt["einf"] < 1e-12 and rt["osc_nu"] < 1e-12
          and rt["fo12"] < 1e-12 and rt["dD12"] < 1e-12,
          "S=81 c=2/3 eps=0 FO=%.3e dD=%.3e Q=%.4f"
          % (rt["fo12"], rt["dD12"], rt["Q12"]))

    if smoke:
        return

    section("S3  FULL CENSUS -- core corr, small-N C_eps, R2 full, chi3")
    core_kzs, all_main = main_ladder()
    check("G20-ladder-size",
          len(core_kzs) == CORE_N and len(all_main) == MAIN_N,
          "core %d MAIN %d" % (len(core_kzs), len(all_main)))

    rows = []
    small = []
    for kz in core_kzs:
        m = V.build_measures(kz)
        Nv = int(m["Nw"])
        dep = Nv - 1 if Nv <= 220 else min(80, Nv - 1)
        rr = deform_row(m["xp"], m["wp"], m["yn"], m["vn"], dep)
        rr["kz"] = kz
        rr["Nv"] = Nv
        rows.append(rr)
        if Nv <= 220:
            small.append(rr)

    einfs = [r["einf"] for r in rows]
    oscs = [r["osc_nu"] for r in rows]
    dQs = [r["dQ12"] for r in rows]
    dDs = [r["dD12"] for r in rows]
    c_einf = pearson(dQs, einfs)
    c_osc = pearson(dDs, oscs)
    check("G21-core42-amp-does-not-control",
          abs(c_einf) < CORE_CORR_EINF_BAR
          and abs(c_osc) < CORE_CORR_OSC_BAR
          and min(einfs) > 4.0 and max(einfs) > 80.0,
          "corr(dQ,einf)=%.3f corr(dD,osc)=%.3f einf[%.2f,%.2f] "
          "osc[%.2f,%.2f]" % (
              c_einf, c_osc, min(einfs), max(einfs),
              min(oscs), max(oscs)))

    fo_hi = max(r["fo12"] for r in small)
    check("G22-smallN-FO-Ceps",
          len(small) == SMALLN_FO_N and fo_hi < SMALLN_FO_BAR,
          "n=%d max|FO|_12=%.5f < 1/32" % (len(small), fo_hi))

    Cstar = max(r["C_emp"] for r in rows)
    n_half = sum(1 for r in rows
                 if r["dD12"] > 0.5 * Cstar * r["osc_nu"] + 1e-15)
    n_maj = 0
    maj_hi = 0.0
    for r in rows:
        maj = r["g12"] * (r["dQT12"] + Cstar * r["osc_nu"])
        maj_hi = max(maj_hi, maj)
        if maj <= CEPS:
            n_maj += 1
    check("G23-osc-majorant-does-not-close",
          n_maj <= OSC_MAJ_CLOSE_MAX and maj_hi > CEPS
          and n_half >= CSTAR_HALF_FAIL_MIN,
          "C*=%.4f maj_hi=%.4f close %d/%d; C*/2 fails %d/%d"
          % (Cstar, maj_hi, n_maj, len(rows), n_half, len(rows)))

    nfull = int(d["n_max"]) - 2
    print("    full mu-path R2 n=%d ..." % nfull, flush=True)
    rat_f, lin_f, qd_f, g0f, g1f = midpoint_mu_nu(xs, ws, ys, vs, nfull)
    g_mu = mu_gams(xs, ws, nfull)
    Qf, bf, _ = mu_Qk(xs, ws, ys, vs, nfull + 1)
    fo_f = g_mu * np.diff(Qf[:nfull + 1])
    r2_f = g1f - g_mu - fo_f
    r2_over = (float(np.max(np.abs(r2_f[-12:])))
               / max(float(np.max(np.abs(fo_f[-12:]))), 1e-12))
    check("G24-R2-mu-full-not-dominated",
          R2_MU_FULL_LO < rat_f < R2_MU_FULL_HI
          and rat_f > NEUMANN
          and r2_over >= R2_OVER_FO_FLOOR,
          "|quad|/|lin|=%.4f |R2|/|FO|=%.3f lin=%.5f quad=%.5f"
          % (rat_f, r2_over, lin_f, qd_f))

    cfo = []
    for kz in core_kzs:
        uu, ww, _, _ = DMF.chi_window_comb(kz, DMF.Q_CHI3)
        mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, DMF.LPQ3)
        Nv = int(mzc["Nw"])
        if Nv <= 220:
            rr = deform_row(mzc["xp"], mzc["wp"], mzc["yn"], mzc["vn"],
                            Nv - 1)
            cfo.append(rr["fo12"])
    check("G25-chi3-smallN-FO-Ceps",
          len(cfo) == SMALLN_FO_N and max(cfo) < CHI3_SMALL_FO_BAR,
          "n=%d max|FO|_12=%.5f < 1/32 (181-pack skipped, disclosed)"
          % (len(cfo), max(cfo)))

    # MAIN-85 at dep=min(N-1,80): fixed-depth smoothness, NOT last-12
    # of the v2-chain for large N (builder fallback).
    main_fo80 = []
    for kz in all_main:
        m = V.build_measures(kz)
        Nv = int(m["Nw"])
        dep = min(Nv - 1, 80)
        rr = deform_row(m["xp"], m["wp"], m["yn"], m["vn"], dep)
        main_fo80.append(rr["fo12"])
    check("G26-MAIN85-dep80-smoothness",
          len(main_fo80) == MAIN_N and max(main_fo80) < 0.04,
          "dep80 |FO|12 max=%.5f (NOT the C_eps last-12 for N>81; "
          "disclosed fallback)" % max(main_fo80))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("delta_deformation_probe -- LEMMA.DELTA_DEFORMATION.01 "
          "(round 388)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_construction(smoke)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = "DELTA DEFORMATION SMOKE" if smoke else "DELTA DEFORMATION"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
