#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""source_sch_sign_probe -- PRIME.RDAGGER.SOURCE_SCH_SIGN.01
(round 417): the source-pure sign of the edge Schur scalar.
P1 rests (window-emergent defect, ~20 languages dead).  The
edge half is qualitatively different: O(1) K2-margin, exact
3x3 Sylvester chart (r401), three equivalent death/life
coordinates (q_N, |Z_loc|, sch, and on nneg-1 the r377
pivot product).  sch<0 was never attacked SOURCE-PURE --
every previous form (gamma>lam_-, alternation, Z_loc) was a
readout.  Since r401/r415, sch is an explicit scalar in the
Sylvester chart with compact (a,b).  This round writes that
scalar from the source, maps the sign region, measures the
tau trend, and tests whether the rate is source-pure
(Uvarov / fold telescopy, PNT-free preferred).

THE OBJECT.  Phi = [[K2, c0], [c0^T, phibb]] with
K2 = I + Ucd^T A0^{-1} Ucd, c0 = Ucd^T A0^{-1} s,
phibb = den-2+s^T A0^{-1}s, s the SM-border vector.
sch = phibb - c0^T K2^{-1} c0.  Haynsworth: the +1 shift
ind_-(Phi)=1+ind_-(A0) iff sch<0 (r401).

CALIBRATION DISCLOSURE.  Closed formula over Q, w9
Woodbury/chart residuals, unnormalized (a,b), phibb, Q vs
2-den, core-42 + EXT-6 + selected 2^k (k=5,9) trend,
sign-map grids, dead-chi geometry, pivot cross, scramble /
two-period / drop-border / false-chart first measured in
/tmp (r417_cal.py, r417_cal2.py) on the r401 constructors,
2026-08-29.  Frozen floors below are that measurement,
sealed as gates.  Pins disclosed.  Builder fallback NOT
taken: full wall ~25 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: sch = den-2 + s^T(A0+Ucd Ucd^T)^{-1}s
    (Woodbury) equals the Sylvester chart
    P1: sch = phibb + a_un^2 - b_un^2,
    VAC: sch = phibb - (a_un^2 + b_un^2),
    with (a_un,b_un)=D2^T c0.  P1 toy sch=-2/3; VAC
    toy sch=-7/6; identity exact.
  * w9: sch=-0.06696, (a,b)=(-0.53249,-0.06903),
    (a_un,b_un)=(-0.13779,-0.01786), phibb=-0.08562,
    Q=0.33193, den=1.60111, dist=0.241, dsch_w=3e-17.
    False-chart (VAC formula on P1) residual = 2 a_un^2
    = 0.03797.  h_N h_{N+1} < 0 and det K2 < 0.
  * SIGN MAP: on VAC with phibb<0 the whole unnormalized
    disk has sch<0 (couplings cannot kill).  On P1 with
    phibb=-0.05, R=0.4, only 989/1257 points (hyperbola;
    large |a_un| is the danger axis).  The w9-un disk
    R=0.14 is entirely sch<0 (min |sch|=0.066).
  * CORE-42: 42/42 sch<0 (P1 28 + vac 14); formula
    residual <= 2e-14; Q in [0.283,0.502] all >0;
    den in [1.460,1.652]; sch in [-0.0919,-0.00151]
    (min at kz16); |t_un| max 0.399.  Living MAIN P1:
    sch<0 AND detK<0 28/28; vac: sch<0 AND detK>0
    14/14 -- sch and the r377 product are NOT globally
    equivalent (dead P1 keeps detK<0 at sch>0).
  * TREND: log|t|~log N slope -0.41 (falling; combined
    with EXT -0.47); log|sch|~log N slope +0.09
    (FLAT, halves ratio 1.00); |t|->0, sch stays
    O(0.04) negative.  EXT-119 N=1119 |t|=0.075,
    sch=-0.045; EXT-6 all sch<0.  Selected a_k=2^k:
    k=5 kz17 sch=-0.109 |t|=0.204; k=9 kz116 N=1433
    sch=-0.038 |t|=0.125.  tau_inf = 0 (census);
    sch(tau_inf) is NOT a function of normalized tau
    (the scale is quotiented by d3); unnormalized
    tau_un->0 implies sch->phibb, and phibb<0 at
    large N (census).
  * RATE: the observed |t|~N^{-0.47} is CENSUS, not
    derived from Uvarov quotients or fold telescopy.
    Gate RATE_OPEN (PNT-free in form -- finite window
    sums -- but no proof).  No legitimate k0.
  * DEAD CHI: 5/5 chi3 + chi4-20 have sch>0.  Dead
    dist to sch=0 median 0.011 vs live 0.180 -- death
    sits on/across the curve.  Three dead P1 have
    |t|~4.6..6.7 (disk escape, R=3.2); two stay inside
    and still cross.  Live chi3 37/37 and chi4 41/41
    sch<0.
  * KILLS: scramble nnegA0=21; two-period nneg=4;
    drop-border shift by 0 (no sch scalar);
    false-chart residual 0.038 at w9.

AUSGANG CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN.
SATZ: Woodbury and the two Sylvester-chart formulae.
REDUZIERT: on VAC, phibb<0 => sch<0 for every coupling;
on P1, sch<0 <=> a_un^2 - b_un^2 < -phibb, and tau_un->0
would reduce this to phibb<0 cofinally.  CENSUS supports
tau->0, sch flat O(0.04), phibb<0 at large N, two-sided
dead-chi geometry.  COFINAL sch<0 NOT PROVED (rate not
source-pure; no k0).  Does not move the mincut.
No RH claim.

MACHINERY: r401 ES.phi_block / main_row / chi_row /
Phi_edge, r375 P2.six_from_AU, r377 PC.row_from_mz
(pivot product at w9 / dead-15), r392 Uvarov cited as
the exact kernel-update identity (rate NOT derived),
r415 chart rewrite -sch=beta-alpha (readout, not source).

NO RH CLAIM.  Finite identities, a named reduction, a
named census, a named open rate.  Research documentation,
not a theorem of RH.  No L* claim.  No R-dagger claim.
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

import edge_signature_probe as ES  # noqa: E402
import postcap_pivots_probe as PC  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402

ES_SHA_PREFIX = "395673f2"
PC_SHA_PREFIX = "b7167c37"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
CORE_N, P1_N, VAC_N = 42, 28, 14
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
CHI4_LIVE_N, CHI4_DEAD_N = 41, 1
K_RADIUS = ES.K_RADIUS
REL = 5.0e-3

W9_SCH = ES.W9_SCH
W9_A, W9_B = ES.W9_A, ES.W9_B
W9_A_UN, W9_B_UN = -0.137787, -0.017863
W9_PHIBB = -0.085622
W9_DIST = 0.2410
W9_Q = 0.33193
W9_FALSE = 0.03797
W9_DEN = ES.W9_DEN

SCH_LO, SCH_HI = -0.095, -0.0012
AB_UN_MAX = 0.42
Q_LO, Q_HI = 0.25, 0.55
DEN_LO, DEN_HI = 1.45, 1.66
SLOPE_AB_LO, SLOPE_AB_HI = -0.70, -0.20
SLOPE_SCH_LO, SLOPE_SCH_HI = -0.20, 0.30
HALVES_SCH_BOX = (0.80, 1.30)
EXT119_AB, EXT119_N = 0.0748, 1119
SEL5_SCH, SEL5_KZ = -0.10864, 17
SEL9_AB, SEL9_KZ, SEL9_N = 0.1251, 116, 1433
DIST_DEAD_MED_HI = 0.05
DIST_LIVE_MED_LO = 0.10
P1_GRID_LO, P1_GRID_HI = 0.70, 0.90
SCR_NNEG, TP21_NNEG = ES.SCR_NNEG, ES.TP21_NNEG

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
    return (not bad), ("NO zero/prime oracles; Woodbury / "
                       "Sylvester chart / r401 Phi / SM border only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


# ---- Leg A: closed formulae over Q ----

def sch_woodbury_Q_p1():
    """P1 toy: A0=diag(-1/2,2,3), Ucd=(e0,e1), s=e1, den=1."""
    A0d = [Fr(-1, 2), Fr(2), Fr(3)]
    A0inv = [Fr(1) / x for x in A0d]
    K2d = [Fr(1) + A0inv[0], Fr(1) + A0inv[1]]
    s = [Fr(0), Fr(1), Fr(0)]
    c0 = [A0inv[0] * s[0], A0inv[1] * s[1]]
    qbb = sum(s[i] * A0inv[i] * s[i] for i in range(3))
    den = Fr(1)
    phibb = den - Fr(2) + qbb
    K2inv = [Fr(1) / K2d[0], Fr(1) / K2d[1]]
    cKc = c0[0] * K2inv[0] * c0[0] + c0[1] * K2inv[1] * c0[1]
    sch = phibb - cKc
    Apd = [A0d[0] + Fr(1), A0d[1] + Fr(1), A0d[2]]
    sWs = s[1] * (Fr(1) / Apd[1]) * s[1]
    sch_w = den - Fr(2) + sWs
    b_un_sq = (c0[1] * c0[1]) / K2d[1]
    sch_ch = phibb - b_un_sq  # a_un = 0
    return dict(sch=sch, sch_w=sch_w, sch_ch=sch_ch, phibb=phibb,
                b_un_sq=b_un_sq, K2=K2d)


def sch_woodbury_Q_vac():
    """VAC toy: A0=diag(2,3,-1,4), Ucd=(e0,e1), s=e0, den=1/2."""
    A0d = [Fr(2), Fr(3), Fr(-1), Fr(4)]
    A0inv = [Fr(1) / x for x in A0d]
    K2d = [Fr(1) + A0inv[0], Fr(1) + A0inv[1]]
    s = [Fr(1), Fr(0), Fr(0), Fr(0)]
    c0 = [A0inv[0] * s[0], Fr(0)]
    qbb = s[0] * A0inv[0] * s[0]
    den = Fr(1, 2)
    phibb = den - Fr(2) + qbb
    K2inv = [Fr(1) / K2d[0], Fr(1) / K2d[1]]
    cKc = c0[0] * K2inv[0] * c0[0]
    sch = phibb - cKc
    Apd = [A0d[0] + Fr(1), A0d[1] + Fr(1), A0d[2], A0d[3]]
    sWs = s[0] * (Fr(1) / Apd[0]) * s[0]
    sch_w = den - Fr(2) + sWs
    a_un_sq = (c0[0] * c0[0]) / K2d[0]
    sch_ch = phibb - a_un_sq
    return dict(sch=sch, sch_w=sch_w, sch_ch=sch_ch, phibb=phibb)


def sch_p1(au, bu, phibb):
    return phibb + au * au - bu * bu


def sch_vac(au, bu, phibb):
    return phibb - (au * au + bu * bu)


def grid_sign(phibb, R, chart, n=40):
    nneg, ntot = 0, 0
    gmin = 1e9
    for i in range(n + 1):
        for j in range(n + 1):
            x = -R + 2 * R * i / n
            y = -R + 2 * R * j / n
            if x * x + y * y > R * R + 1e-15:
                continue
            ntot += 1
            s = (sch_p1(x, y, phibb) if chart == "P1"
                 else sch_vac(x, y, phibb))
            if s < 0:
                nneg += 1
                gmin = min(gmin, -s)
    return nneg, ntot, (gmin if gmin < 1e8 else 0.0)


def chart_from_row(p):
    """Unnormalized chart scalars from an r401 row (no rebuild)."""
    sch = float(p["sch"])
    a, b = float(p["a"]), float(p["b"])
    den = float(p["den"])
    scale = math.sqrt(abs(sch)) if abs(sch) > FLOOR else 0.0
    au = a * scale
    bu = b * scale
    ab_un = math.hypot(au, bu)
    signs = p.get("signs", (0.0, 0.0))
    p1 = (abs(signs[0] + 1.0) < 0.5 and abs(signs[1] - 1.0) < 0.5)
    if p1:
        phibb = sch - au * au + bu * bu
        kchart = "P1"
    else:
        phibb = sch + au * au + bu * bu
        kchart = "VAC"
    dist = (abs(sch) / (2.0 * ab_un) if ab_un > 1e-14 else abs(sch))
    Q = sch - (den - 2.0)
    return dict(a_un=au, b_un=bu, ab_un=ab_un, phibb=phibb,
                dist=dist, Q=Q, kchart=kchart, scale=scale)


def woodbury_w9():
    """One-window reconstruction: Woodbury vs chart vs r401 sch."""
    R = PX.build_rung(9)
    mz = R["mz"]
    alk = float(V.window_shape(9)[0])
    dsm = HS.window_data(9, comb=PB.smooth_comb(alk))
    p = ES.phi_block(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                     R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                     mz["xp"], mz["wp"], dsm["xs"], dsm["ws"],
                     dsm["ys"], dsm["vs"], Bm=R["B"])
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                        R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                        keep=True)
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    bp = ABD.border_chain_pack(np.asarray(mz["xp"], float),
                               np.asarray(mz["wp"], float),
                               yn, vn, dsm["xs"], dsm["ws"],
                               dsm["ys"], dsm["vs"], R["Nw"])
    A0 = np.asarray(cut["A0"], float)
    Ucd = np.asarray(cut["U"], float)
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(mz["xp"], float),
                                  np.asarray(mz["wp"], float), R["Nw"])
    bxa = np.concatenate([np.asarray(dsm["xs"], float),
                          np.asarray(dsm["ys"], float)])
    bwa = np.concatenate([np.asarray(dsm["ws"], float),
                          -np.asarray(dsm["vs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, R["Nw"])
    vt = cut["epsY"] * (R["B"] @ (bvec / math.sqrt(bp["Bw"])))
    s = cut["Rm"] @ vt
    den = (1.0 + float(bvec @ bvec) / float(bp["Bw"])) - float(vt @ s)
    Ap = A0 + Ucd @ Ucd.T
    sch_w = den - 2.0 + float(s @ np.linalg.solve(Ap, s))
    ch = chart_from_row(p)
    sch_ch = (sch_p1(ch["a_un"], ch["b_un"], ch["phibb"])
              if ch["kchart"] == "P1"
              else sch_vac(ch["a_un"], ch["b_un"], ch["phibb"]))
    return p, ch, sch_w, sch_ch, den


def loglog_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    m = (xs > 0) & (ys > 0) & np.isfinite(xs) & np.isfinite(ys)
    if int(m.sum()) < 3:
        return float("nan")
    X = np.log(xs[m])
    Y = np.log(ys[m])
    Xc = X - X.mean()
    den = float(Xc @ Xc)
    if den < 1e-18:
        return float("nan")
    return float((Xc @ (Y - Y.mean())) / den)


# ---- legs ----

def part_satz():
    section("S1  LEG A -- CLOSED sch FORMULA OVER Q + SIGN MAP")
    t1 = sch_woodbury_Q_p1()
    check("G01-P1-toy-Q",
          t1["sch"] == t1["sch_w"] == t1["sch_ch"] == Fr(-2, 3)
          and t1["phibb"] == Fr(-1, 2) and t1["b_un_sq"] == Fr(1, 6)
          and t1["K2"] == [Fr(-1), Fr(3, 2)],
          "P1: sch=Woodbury=chart=-2/3, phibb=-1/2, "
          "K2=diag(-1,3/2), b_un^2=1/6")
    t0 = sch_woodbury_Q_vac()
    check("G02-VAC-toy-Q",
          t0["sch"] == t0["sch_w"] == t0["sch_ch"] == Fr(-7, 6)
          and t0["phibb"] == Fr(-1),
          "VAC: sch=Woodbury=chart=-7/6, phibb=-1")
    n1, t1n, gmin = grid_sign(-0.05, 0.40, "VAC")
    check("G03-VAC-phibb-neg-whole-disk",
          n1 == t1n and t1n >= 1000,
          "phibb=-0.05 R=0.4 VAC: sch<0 on %d/%d (couplings "
          "cannot kill)" % (n1, t1n))
    n2, t2n, _g = grid_sign(-0.05, 0.40, "P1")
    frac = n2 / float(t2n)
    check("G04-P1-hyperbola-not-whole",
          P1_GRID_LO <= frac <= P1_GRID_HI,
          "phibb=-0.05 R=0.4 P1: sch<0 %d/%d = %.3f "
          "(danger = large |a_un|)" % (n2, t2n, frac))
    n3, t3n, gmin3 = grid_sign(W9_PHIBB, 0.14, "P1")
    check("G05-w9-un-disk-inside",
          n3 == t3n and gmin3 >= 0.06,
          "w9-un R=0.14: %d/%d sch<0, min|sch|=%.4f "
          "(source inside the living region)" % (n3, t3n, gmin3))


def part_w9():
    section("S2  LEG A -- w9 SOURCE PACK + FALSE CHART")
    p, ch, sch_w, sch_ch, den = woodbury_w9()
    check("G10-w9-woodbury-chart",
          abs(sch_w - p["sch"]) <= 1e-12
          and abs(sch_ch - p["sch"]) <= 1e-12
          and ch["kchart"] == "P1",
          "dsch_w=%.2e dsch_ch=%.2e chart=%s"
          % (abs(sch_w - p["sch"]), abs(sch_ch - p["sch"]),
             ch["kchart"]))
    check("G11-w9-pins",
          abs(p["sch"] / W9_SCH - 1.0) <= 0.02
          and abs(p["a"] - W9_A) <= 0.01
          and abs(p["b"] - W9_B) <= 0.01
          and abs(ch["a_un"] - W9_A_UN) <= 0.001
          and abs(ch["phibb"] - W9_PHIBB) <= 0.001
          and abs(ch["dist"] - W9_DIST) <= 0.01
          and abs(ch["Q"] - W9_Q) <= 0.01
          and abs(p["den"] / W9_DEN - 1.0) <= REL,
          "sch=%.5f (a_un,b_un)=(%.5f,%.5f) phibb=%.5f "
          "Q=%.5f dist=%.3f" % (
              p["sch"], ch["a_un"], ch["b_un"], ch["phibb"],
              ch["Q"], ch["dist"]))
    mz = V.build_measures(9)
    piv = PC.row_from_mz("w9", 9, mz)
    check("G12-w9-pivot-cross",
          piv["sN"] * piv["sNp1"] < 0 and p["detK"] < 0
          and p["sch"] < 0 and p["nnegA0"] == 1,
          "prod h_N h_{N+1}=%d detK=%+.3f sch<0 nnegA0=1 "
          "(nneg-1 branch: both coordinates negative)"
          % (piv["sN"] * piv["sNp1"], p["detK"]))
    false = sch_vac(ch["a_un"], ch["b_un"], ch["phibb"])
    check("G13-false-chart",
          abs(abs(p["sch"] - false) - W9_FALSE) <= 0.002
          and abs(p["sch"] - false - 2.0 * ch["a_un"] ** 2) <= 1e-12,
          "VAC formula on P1 residual=%.5f = 2 a_un^2 (chart "
          "load-bearing)" % abs(p["sch"] - false))
    return p, ch


def part_kills(ch_w9):
    section("S3  LEG D -- DEAD CHI / SCRAMBLE / MUTANTS")
    p15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    c15 = chart_from_row(p15)
    uu, ww, _nn, _ch = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(15, uu, ww, 1.0, DMF.LPQ3)
    piv15 = PC.row_from_mz("D15", 15, mzc)
    check("G20-dead-chi3-15",
          p15["ok"] and p15["sch"] > 0 and (not p15["shift"])
          and c15["dist"] <= DIST_DEAD_MED_HI
          and p15["ab"] > K_RADIUS
          and p15["detK"] < 0
          and piv15["sN"] * piv15["sNp1"] < 0,
          "DEAD: sch=%+.4f dist=%.3f |t|=%.2f > R=%.1f; "
          "detK<0 and prod<0 STILL (sch is the separator)"
          % (p15["sch"], c15["dist"], p15["ab"], K_RADIUS))
    p3 = ES.chi_row(9, DMF.Q_CHI3, DMF.LPQ3, "L9")
    check("G21-live-chi3-9",
          p3["ok"] and p3["shift"] and p3["sch"] < 0,
          "LIVE vacuous sch=%.4f SHIFT" % p3["sch"])
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d (J / A0 chart dies)" % oS["nneg"])
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G23-two-period",
          oT["nneg"] >= TP21_NNEG,
          "nnegA0=%d >= 4" % oT["nneg"])
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G24-drop-border",
          nK == nA0 == 1,
          "K2 nneg=%d == nnegA0 (shift by 0; no sch scalar)"
          % nK)
    p4d = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    check("G25-dead-chi4-20",
          p4d["ok"] and p4d["sch"] > 0 and (not p4d["shift"]),
          "chi4-20 sch=%+.4f nnegPhi=%d" % (
              p4d["sch"], p4d["nnegPhi"]))
    return p15, c15


def part_census(smoke):
    section("S4  LEG B/C -- TREND / SELECTED / CHI / RATE")
    if smoke:
        section("S4b  core/EXT/chi skipped (--smoke)")
        return None
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        p = ES.main_row(kz)
        p.update(chart_from_row(p))
        p["kz"] = kz
        rows.append(p)
    ok = [r for r in rows if r.get("ok")]
    p1 = [r for r in ok if r["nnegA0"] == 1]
    vac = [r for r in ok if r["nnegA0"] == 0]
    dsch = [abs(sch_p1(r["a_un"], r["b_un"], r["phibb"]) - r["sch"])
            if r["kchart"] == "P1"
            else abs(sch_vac(r["a_un"], r["b_un"], r["phibb"]) - r["sch"])
            for r in ok]
    check("G30-core42-sch-neg",
          len(ok) == CORE_N and len(p1) == P1_N and len(vac) == VAC_N
          and all(r["sch"] < 0 for r in ok)
          and max(dsch) <= 1e-12
          and all(r["Q"] > 0 for r in ok),
          "42/42 sch<0; P1 %d vac %d; max chart residual %.1e; Q>0"
          % (len(p1), len(vac), max(dsch)))
    check("G31-P1-detK-and-sch",
          all(r["sch"] < 0 and r["detK"] < 0 for r in p1)
          and SCH_LO <= min(r["sch"] for r in ok) <= -0.05
          and -0.005 <= max(r["sch"] for r in ok) <= SCH_HI
          and max(r["ab_un"] for r in ok) <= AB_UN_MAX,
          "P1 28/28 sch<0 AND detK<0; sch in [%.4f, %.4f]; "
          "|t_un| max=%.3f" % (min(r["sch"] for r in ok),
                               max(r["sch"] for r in ok),
                               max(r["ab_un"] for r in ok)))
    check("G32-vac-sch-not-detK",
          all(r["sch"] < 0 and r["detK"] > 0 for r in vac),
          "vac 14/14 sch<0 AND detK>0 -- sch and r377 product "
          "are independent coordinates")
    dens = [r["den"] for r in ok]
    Qs = [r["Q"] for r in ok]
    check("G33-Q-den-boxes",
          DEN_LO <= min(dens) and max(dens) <= DEN_HI
          and Q_LO <= min(Qs) and max(Qs) <= Q_HI,
          "den [%.3f, %.3f] Q [%.3f, %.3f] -- two O(1) terms, "
          "sch is their difference" % (
              min(dens), max(dens), min(Qs), max(Qs)))
    p1s = sorted(ok, key=lambda r: r["Nw"])
    mid = len(p1s) // 2
    lo, hi = p1s[:mid], p1s[mid:]
    rat_sch = (float(np.median([abs(r["sch"]) for r in hi]))
               / float(np.median([abs(r["sch"]) for r in lo])))
    sl_ab = loglog_slope([r["Nw"] for r in ok], [r["ab"] for r in ok])
    sl_sch = loglog_slope([r["Nw"] for r in ok],
                          [abs(r["sch"]) for r in ok])
    check("G34-sch-trend-free",
          HALVES_SCH_BOX[0] <= rat_sch <= HALVES_SCH_BOX[1]
          and SLOPE_SCH_LO <= sl_sch <= SLOPE_SCH_HI,
          "halves |sch| rat=%.3f; slope log|sch|~log N = %.3f "
          "(FLAT O(0.04))" % (rat_sch, sl_sch))
    check("G35-tau-falling",
          SLOPE_AB_LO <= sl_ab <= SLOPE_AB_HI,
          "slope log|t|~log N = %.3f (falling toward 0)"
          % sl_ab)

    ext = []
    for kz in ES.SAMPLE_EXT:
        p = ES.main_row(kz)
        p.update(chart_from_row(p))
        p["kz"] = kz
        ext.append(p)
        print("    EXT-%d N=%d sch=%+.4f |t|=%.4f |t_un|=%.4f "
              "phibb=%.4f" % (kz, p["Nw"], p["sch"], p["ab"],
                              p["ab_un"], p["phibb"]), flush=True)
    p119 = next(r for r in ext if r["kz"] == 119)
    check("G36-EXT",
          all(r.get("ok") and r["sch"] < 0 for r in ext)
          and abs(p119["ab"] - EXT119_AB) <= 0.01
          and p119["Nw"] == EXT119_N
          and all(r["phibb"] < 0 for r in ext),
          "%d EXT sch<0; kz119 N=%d |t|=%.4f; all phibb<0"
          % (len(ext), p119["Nw"], p119["ab"]))

    live3, dead3, live4, dead4 = [], [], [], []
    for kz in core:
        p = ES.chi_row(kz, DMF.Q_CHI3, DMF.LPQ3, "C3-%d" % kz)
        if p is not None and p.get("ok"):
            p.update(chart_from_row(p))
            (dead3 if kz in ES.DEAD_CHI3 else live3).append(p)
        p4 = ES.chi_row(kz, DMF.Q_CHI4, DMF.LPQ4, "C4-%d" % kz)
        if p4 is not None and p4.get("ok"):
            p4.update(chart_from_row(p4))
            (dead4 if kz in ES.DEAD_CHI4 else live4).append(p4)
    check("G37-chi3",
          len(live3) == CHI3_LIVE_N
          and all(r["sch"] < 0 for r in live3)
          and len(dead3) == CHI3_DEAD_N
          and all(r["sch"] > 0 for r in dead3),
          "live chi3 %d/%d sch<0; dead %d/%d sch>0"
          % (len(live3), CHI3_LIVE_N, len(dead3), CHI3_DEAD_N))
    check("G38-chi4",
          len(live4) == CHI4_LIVE_N
          and all(r["sch"] < 0 for r in live4)
          and len(dead4) == CHI4_DEAD_N
          and all(r["sch"] > 0 for r in dead4),
          "live chi4 %d/%d sch<0; dead %d sch>0"
          % (len(live4), CHI4_LIVE_N, len(dead4)))
    d_live = float(np.median([r["dist"] for r in live3]))
    d_dead = float(np.median([r["dist"] for r in dead3]))
    n_escape = sum(1 for r in dead3 if r["ab"] > K_RADIUS)
    check("G39-dead-geometry",
          d_dead <= DIST_DEAD_MED_HI and d_live >= DIST_LIVE_MED_LO
          and n_escape >= 2
          and all(r["detK"] < 0 for r in dead3 if r["nnegA0"] == 1),
          "dead dist med=%.3f vs live %.3f; %d/%d disk-escape; "
          "dead P1 keeps detK<0" % (d_dead, d_live, n_escape,
                                    len(dead3)))

    p5 = ES.main_row(SEL5_KZ)
    p9s = ES.main_row(SEL9_KZ)
    check("G40-selected-2k",
          p5["ok"] and p5["sch"] < 0
          and abs(p5["sch"] / SEL5_SCH - 1.0) <= 0.05
          and p9s["ok"] and p9s["sch"] < 0
          and abs(p9s["ab"] - SEL9_AB) <= 0.02
          and p9s["Nw"] == SEL9_N,
          "k=5 kz17 sch=%.4f; k=9 kz116 N=%d |t|=%.4f sch=%.4f"
          % (p5["sch"], p9s["Nw"], p9s["ab"], p9s["sch"]))
    both = ok + ext
    sl_both = loglog_slope([r["Nw"] for r in both],
                           [r["ab"] for r in both])
    check("G41-rate-open",
          SLOPE_AB_LO <= sl_both <= SLOPE_AB_HI
          and SLOPE_SCH_LO <= sl_sch <= SLOPE_SCH_HI,
          "combined |t| slope=%.3f (CENSUS, not Uvarov/fold "
          "derived; RATE_OPEN, PNT-free form, no k0)" % sl_both)
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("source_sch_sign_probe -- "
          "PRIME.RDAGGER.SOURCE_SCH_SIGN.01 (round 417)")
    print("SPEC_SHA %s   (ES %s / PC %s / HM %s)"
          % (SPEC_SHA[:16], ES.SPEC_SHA[:16], PC.SPEC_SHA[:16],
             HM.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi + EXT-6 + selected 2^k)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and PC.SPEC_SHA.startswith(PC_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / PC %s / HM %s / FTI %s / DMF %s"
          % (ES.SPEC_SHA[:8], PC.SPEC_SHA[:8], HM.SPEC_SHA[:8],
             FTI.SPEC_SHA[:8], DMF.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    _p, ch = part_w9()
    part_kills(ch)
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN: "
          "Woodbury+chart SATZ; tau->0 census; sch flat "
          "O(0.04); cofinal sch<0 NOT proved.  no RH / L* / "
          "R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("SOURCE SCH SIGN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("SOURCE SCH SIGN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
