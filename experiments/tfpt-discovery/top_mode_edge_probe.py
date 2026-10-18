#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""top_mode_edge_probe -- PRIME.RDAGGER.TOP_MODE_EDGE.01
(round 415, parallel to R413): if the hole-top-mode
architecture holds, the r401 3x3 is the edge of the
canonical top mode
    v_top,i  ~  1 / (sqrt(u^vee(y_i)) * P_Y'(y_i))
and sch need not be proved generally negative, but as a
balance  -sch_k = beta_k - alpha_k  with alpha the top-mode
defect energy after bulk continuation and beta the net CD
lift after border consumption.

R405 tested the CONSTANT (wrong vector).  Euler tail and
disk Parseval are kept as identities and re-read on v_top.

CALIBRATION DISCLOSURE.  v_top vs T0-SV / A0-vneg, Euler
projection, Woodbury (eta, r, Delta) vs sch, H=A0+vv^T
inertia, closed-kappa mismatch, geo-span relres, ones
control (r405 pins), MAIN-18 cosine, core-42 + chi3/chi4
sign census first measured in /tmp (r415_cal.py,
r415_cal2.py, r415_cal3.py, r415_cal4.py) on the same
constructors, 2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.  Builder
fallback NOT taken: full wall < 50 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: Euler tail 1-z^{K+1}=(1-z)Sum z^r (z=1/3 K=5,
    728/729); disk Parseval (q=1/2 K=6, reserve 1/128).
  * SATZ Q: with alpha=(eta-1)/kappa, beta=r^T K_W^{-1}r
    /kappa and kappa=Delta/(-sch) from r405 kappa_closed_Q,
    beta-alpha=-sch exactly (eta=13/12, Delta=7/36,
    sch=21/8, kappa=-2/27, alpha=-9/8, beta=-15/4).
  * w9: |Y|=104, sch=-0.06696, ||T0||=1.08014, nneg=1.
    cos(v_top, v_SV)=cos(v_top, vneg_A0)=0.6766 != 1;
    cos(v_top, 1)=0.0107.  alpha_T = v^T(TT-I)v = -0.07302
    (CONTRACTIVE -- v_top is not the excess direction;
    the true SV has alpha_SV=+0.16670).
  * Euler re-read: E_p+T_p=1 POINTWISE, so
    Sum nu_p |<E_p+T_p, v_top>|^2 = |<1, v_top>|^2
    = 0.01192 != |alpha_T|.  Geo-span relres=0.74.
  * Woodbury H=A0+v_top v_top^T, U=2 CD cols: eta=0.98781,
    r2=-0.00736, Delta=0.004830, nnegH=1 (H not PD),
    kappa_emp=0.07214.  Scaled beta-alpha=-sch at 1e-17.
    Closed formula kappa=-(1-eta)det K2/det K_W does NOT
    match kappa_emp (source U is not the 3x3 Phi U).
  * Ones control REPRODUCES r405: Delta=2.110e-3, c2=0.99789,
    kappa=0.03151.  The constant is the wrong vector.
  * MAIN-18 (true defect ||T||=1.25): cos(v_top, vneg)=0.058.
  * CENSUS (kappa-scaled beta>alpha iff sch<0, ANY ell):
    MAIN 42/42 beta>alpha; living chi 37+41=78 beta>alpha;
    dead chi 5+1=6 beta<alpha.  Identity residual <= 2e-17.
    H PD only 18/42 MAIN -- v_top is not a one-defect split.
    cos(v_top, vneg) in [0.006, 0.816].
  * KILLS: 1/P' (no sqrt u^vee) worse SV overlap; fake P'
    (y-mean) not the defect; permute nneg~20 / scramble 21
    (bulk already dead, edge of one mode irrelevant);
    2x2 K2 mixed on BOTH living w9 and dead chi15 (border
    omitted: no living/dead scalar).

AUSGANG CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT.
SATZ: Euler tail; disk Parseval; Woodbury-Schur rewrite
-sch=beta-alpha with the r405 kappa scaling (Q-exact and
f64 residual 0).  CENSUS: living beta>alpha / dead beta<alpha
is exactly sch<0 / sch>0 (r401), for v_top AND for ones.
REFUTED: v_top = T0 top SV (MAIN-18 cos=0.058; w9 cos=0.68);
alpha_T as Euler energy; H=A0+vv^T PD; closed kappa formula
on the 2-col source split; positive Euler-span source of
beta-alpha (relres 0.74).  The edge theorem does not become
easier by changing the test vector from 1 to v_top: the
sign of beta-alpha is the chart coordinate sch.  No RH claim.

MACHINERY: r401 ES.main_row / chi_row / Phi 3x3, r405
E.euler_tail_Q / disk_parseval_Q / kappa_closed_Q /
ones_woodbury_Y / cut_of, r409 B.pack_graph / source_T0_cls,
r407 DI.chain_C (u^vee on Y), r406 Woodbury Delta=1-eta+r^T
K^{-1}r (finite algebra, not Lean this round).

NO RH CLAIM.  Finite identities, named refutations, named
reduction to the r401 chart.  Research documentation, not
a theorem of RH.  No L* claim.  No R-dagger claim.
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
import edge_contractive_lift_probe as E405  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import mixed_haynsworth_probe as MH  # noqa: E402

ES_SHA_PREFIX = "395673f2"
E405_SHA_PREFIX = "b91e6629"
B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
MH_SHA_PREFIX = "138d0997"

FLOOR = 1.0e-8
ID_RES = 1.0e-12
CORE_N = 42
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
CHI4_LIVE_N, CHI4_DEAD_N = 41, 1
HPD_MAIN = 18
COS_LO, COS_HI = 0.005, 0.82
PERM_NNEG_LO = 15
SCR_NNEG = 21

W9_COS_SV = 0.6766
W9_COS_ONES = 0.0107
W9_ALPHA_T = -0.073023
W9_ALPHA_SV = 0.16670
W9_EUL = 0.01192
W9_ETA = 0.987808
W9_R2 = -0.007362
W9_DLT = 4.82991e-3
W9_KAPPA = 0.072136
W9_GEO_REL = 0.7396
MAIN18_COS_HI = 0.12

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
    return (not bad), ("NO zero/prime oracles; v_top / Euler / "
                       "Woodbury / r401 sch only"
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


def v_top_of(yn, wY):
    """Canonical hole-top mode in the sqrt(u^vee)-weighted
    sample coordinate: v_i ~ 1/(sqrt(w_i) P_Y'(y_i)).
    Log-sum P' (no overflow).  No fit."""
    yn = np.asarray(yn, float)
    wY = np.asarray(wY, float)
    n = len(yn)
    logabs = np.empty(n)
    sgn = np.ones(n)
    for i in range(n):
        acc = -0.5 * math.log(max(wY[i], 1e-300))
        s = 1.0
        for j in range(n):
            if j == i:
                continue
            d = yn[i] - yn[j]
            if d == 0.0:
                acc = -1e300
                break
            acc -= math.log(abs(d))
            if d < 0.0:
                s = -s
        logabs[i] = acc
        sgn[i] = s
    m = float(np.max(logabs))
    raw = sgn * np.exp(np.clip(logabs - m, -700.0, 700.0))
    nrm = float(np.linalg.norm(raw))
    if nrm < 1e-30:
        raw = np.ones(n)
        nrm = float(np.linalg.norm(raw))
    return raw / nrm


def v_wrong_omega(yn, wY):
    """Kill: drop sqrt(u^vee), v ~ 1/P_Y'."""
    yn = np.asarray(yn, float)
    n = len(yn)
    logabs = np.empty(n)
    sgn = np.ones(n)
    for i in range(n):
        acc = 0.0
        s = 1.0
        for j in range(n):
            if j == i:
                continue
            d = yn[i] - yn[j]
            acc -= math.log(max(abs(d), 1e-300))
            if d < 0.0:
                s = -s
        logabs[i] = acc
        sgn[i] = s
    m = float(np.max(logabs))
    raw = sgn * np.exp(np.clip(logabs - m, -700.0, 700.0))
    return raw / (np.linalg.norm(raw) + 1e-30)


def v_wrong_P(yn, wY):
    """Kill: fake P' = y_i - mean(Y) (degree 1)."""
    yn = np.asarray(yn, float)
    wY = np.asarray(wY, float)
    mu = float(np.mean(yn))
    d = yn - mu
    raw = np.sign(d + 1e-18) / (
        np.sqrt(np.maximum(wY, 1e-300)) * np.maximum(np.abs(d), 1e-12))
    return raw / (np.linalg.norm(raw) + 1e-30)


def euler_energy(yn, v):
    """Sum_p nu_p |<E_p+T_p, v>|^2.  Because E_p+T_p=1
    pointwise (Euler tail), this equals |<1,v>|^2."""
    yn = np.asarray(yn, float)
    v = np.asarray(v, float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    logs = np.array([math.log(p) for p in E405.PRIMES_GEO], float)
    nu = logs / float(np.sum(logs))
    energy = 0.0
    for p, w in zip(E405.PRIMES_GEO, nu):
        z = (p ** -0.5) * np.exp(1j * th * math.log(p))
        geom = sum(z ** r for r in range(E405.K_GEO + 1))
        et = (1.0 - z) * geom + z ** (E405.K_GEO + 1)
        energy += float(w) * abs(complex(np.vdot(v, et))) ** 2
    ip1 = float(np.vdot(v, np.ones(len(yn))))
    return energy, ip1 * ip1, ip1


def geo_relres(yn, v):
    g = E405.geometric_ones(yn)
    Vgeo = g["V"]
    Q, _R = np.linalg.qr(Vgeo, mode="reduced")
    return float(np.linalg.norm(v - Q @ (Q.T @ v))
                 / (np.linalg.norm(v) + 1e-30))


def woodbury_ell(A0, U, ell):
    A0 = 0.5 * (np.asarray(A0, float) + np.asarray(A0, float).T)
    U = np.asarray(U, float)
    ell = np.asarray(ell, float).ravel()
    ell = ell / (float(np.linalg.norm(ell)) + 1e-30)
    H = 0.5 * ((A0 + np.outer(ell, ell)) + (A0 + np.outer(ell, ell)).T)
    Hi_e = np.linalg.solve(H, ell)
    Hi_U = np.linalg.solve(H, U)
    eta = float(ell @ Hi_e)
    r = U.T @ Hi_e
    Kw = 0.5 * ((np.eye(U.shape[1]) + U.T @ Hi_U)
                + (np.eye(U.shape[1]) + U.T @ Hi_U).T)
    r2 = float(r @ np.linalg.solve(Kw, r))
    Delta = 1.0 - eta + r2
    evH = np.linalg.eigvalsh(H)
    nnegH = int(np.sum(evH < -FLOOR))
    K2 = 0.5 * ((np.eye(U.shape[1]) + U.T @ np.linalg.solve(A0, U))
                + (np.eye(U.shape[1]) + U.T @ np.linalg.solve(A0, U)).T)
    detK2 = float(np.linalg.det(K2))
    detKw = float(np.linalg.det(Kw))
    kap_f = (-(1.0 - eta) * detK2 / detKw
             if abs(detKw) > 1e-30 else float("nan"))
    nnegK2 = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    return dict(eta=eta, r2=r2, Delta=Delta, nnegH=nnegH,
                kap_f=kap_f, nnegK2=nnegK2, ell=ell,
                K2=K2, detK2=detK2)


def alpha_beta(w, sch):
    """Source-pure (Woodbury) then chart-scaled.
    alpha_raw = eta-1, beta_raw = r^T K^{-1} r,
    Delta = beta_raw - alpha_raw.
    kappa_emp = Delta/(-sch); alpha = alpha_raw/kappa,
    beta = beta_raw/kappa  =>  beta-alpha = -sch."""
    kap = w["Delta"] / (-sch) if abs(sch) > FLOOR else float("nan")
    a_raw = w["eta"] - 1.0
    b_raw = w["r2"]
    a = a_raw / kap if math.isfinite(kap) and abs(kap) > 1e-18 else float("nan")
    b = b_raw / kap if math.isfinite(kap) and abs(kap) > 1e-18 else float("nan")
    return dict(kappa=kap, alpha=a, beta=b, ba=b - a,
                alpha_raw=a_raw, beta_raw=b_raw)


def y_weights(mz):
    _C, meta = DI.chain_C(mz)
    yn = np.asarray(meta["yn"], float)
    wY = np.asarray(meta["ud"][meta["iY"]], float)
    return yn, wY


def edge_row(kz, chi=None):
    cut, row, mz = E405.cut_of(kz, chi=chi)
    yn, wY = y_weights(mz)
    vt = v_top_of(yn, wY)
    A0 = np.asarray(cut["A0"], float)
    U = np.asarray(cut["U"], float)
    w = woodbury_ell(A0, U, vt)
    sch = float(row["sch"])
    ab = alpha_beta(w, sch)
    ev, VA = np.linalg.eigh(A0)
    vneg = VA[:, 0]
    return dict(kz=kz, sch=sch, nnegA0=int(row["nnegA0"]),
                yn=yn, wY=wY, vt=vt, A0=A0, U=U, cut=cut,
                mz=mz, row=row, w=w, ab=ab,
                cos_neg=abs(float(np.vdot(vt, vneg))),
                nnegK2=w["nnegK2"])


def ab_identity_Q():
    """Label the r405 Q-toy as alpha/beta."""
    kq = E405.kappa_closed_Q()
    eta, D, sch, kap = kq["eta"], kq["Delta"], kq["sch"], kq["kappa"]
    a_raw = eta - Fr(1)
    r2 = D - (Fr(1) - eta)
    a = a_raw / kap
    b = r2 / kap
    return dict(eta=eta, Delta=D, sch=sch, kappa=kap,
                alpha=a, beta=b, ba=b - a, equal=(b - a == -sch),
                r2=r2)


def part_satz():
    section("S1  LEG 3 -- Q IDENTITIES (EULER / DISK / ALPHA-BETA)")
    et = E405.euler_tail_Q()
    check("G01-euler-tail-Q",
          et["ok"] and et["lhs"] == Fr(728, 729),
          "z=1/3 K=5 lhs=%s (R405, kept)" % et["lhs"])
    dp = E405.disk_parseval_Q()
    check("G02-disk-parseval-Q",
          dp["ok"] and (Fr(1) - dp["rhs"]) == Fr(1, 128),
          "reserve q^{K+1}=1/128 (R405, kept)")
    t = ab_identity_Q()
    check("G03-alpha-beta-Q",
          t["equal"] and t["alpha"] == Fr(-9, 8)
          and t["beta"] == Fr(-15, 4) and t["sch"] == Fr(21, 8),
          "beta-alpha=%s=-sch; alpha=%s beta=%s kappa=%s"
          % (t["ba"], t["alpha"], t["beta"], t["kappa"]))
    return t


def part_leg1():
    section("S2  LEG 1 -- EULER ON v_top AND T0 RAYLEIGH (w9, sample)")
    mz = V.build_measures(9)
    g = B.pack_graph(mz)
    yn, wY = g["yn"], g["wY"]
    vt = v_top_of(yn, wY)
    TT = g["TT"]
    I = np.eye(len(yn))
    alpha_T = float(vt @ (TT - I) @ vt)
    _U, _s, Vt = np.linalg.svd(g["T0"], full_matrices=False)
    vsv = Vt[0]
    if float(np.vdot(vt, vsv)) < 0:
        vsv = -vsv
    cos_sv = abs(float(np.vdot(vt, vsv)))
    ones = np.ones(len(yn))
    ones = ones / np.linalg.norm(ones)
    cos_1 = abs(float(np.vdot(vt, ones)))
    eul, ip2, ip1 = euler_energy(yn, vt)
    rel = geo_relres(yn, vt)
    alpha_sv = float(vsv @ (TT - I) @ vsv)
    check("G10-w9-euler-is-constant-content",
          abs(eul - ip2) <= 1e-12
          and abs(eul - W9_EUL) / W9_EUL <= 0.02,
          "Sum nu|<ET,v>|^2=%.5f = |<1,v>|^2=%.5f (E_p+T_p=1)"
          % (eul, ip2))
    check("G11-w9-euler-not-alpha",
          alpha_T < 0.0
          and abs(alpha_T - W9_ALPHA_T) / abs(W9_ALPHA_T) <= 0.02
          and abs(eul - abs(alpha_T)) > 0.04
          and abs(alpha_sv - W9_ALPHA_SV) / W9_ALPHA_SV <= 0.02,
          "alpha_T=%.5f (contractive) vs euler=%.5f; "
          "true SV alpha=%.5f" % (alpha_T, eul, alpha_sv))
    check("G12-w9-vtop-not-SV",
          abs(cos_sv - W9_COS_SV) <= 0.01
          and cos_sv < 0.72
          and abs(cos_1 - W9_COS_ONES) <= 0.005,
          "cos(v_top,v_SV)=%.4f != 1; cos(v_top,1)=%.4f"
          % (cos_sv, cos_1))
    check("G13-w9-geo-span-miss",
          rel >= 0.70 and abs(rel - W9_GEO_REL) <= 0.05,
          "geo-span relres=%.4f (v_top not in Euler dictionary)"
          % rel)
    # MAIN-18: cheap A0 cosine (equals SV cosine by dictionary)
    r18 = edge_row(18)
    check("G14-main18-vtop-not-defect",
          r18["cos_neg"] <= MAIN18_COS_HI and r18["nnegA0"] == 1,
          "MAIN-18 cos(v_top,vneg)=%.4f with nnegA0=1 "
          "(formula is not the bulk defect)"
          % r18["cos_neg"])
    return dict(g=g, vt=vt, yn=yn, wY=wY, alpha_T=alpha_T,
                cos_sv=cos_sv, eul=eul, rel=rel, mz=mz)


def part_leg2(w9leg):
    section("S3  LEG 2 -- ALPHA/BETA IN THE r401 CHART (w9 + chi)")
    r9 = edge_row(9)
    sch = r9["sch"]
    ab = r9["ab"]
    w = r9["w"]
    check("G20-w9-chart-identity",
          abs(ab["ba"] - (-sch)) <= ID_RES
          and abs(w["eta"] - W9_ETA) <= 5e-5
          and abs(w["Delta"] - W9_DLT) / W9_DLT <= 0.01
          and abs(ab["kappa"] - W9_KAPPA) / W9_KAPPA <= 0.01,
          "beta-alpha=%.6f=-sch; eta=%.5f D=%.4e kappa=%.5f"
          % (ab["ba"], w["eta"], w["Delta"], ab["kappa"]))
    # ones control = r405
    wo = E405.ones_woodbury_Y(r9["A0"], r9["U"])
    kap_o = wo["Delta"] / (-sch)
    check("G21-ones-reproduces-r405",
          abs(wo["Delta"] - E405.W9_DLT) / E405.W9_DLT <= 0.01
          and abs(wo["c2"] - E405.W9_C2) <= 5e-5
          and abs(kap_o - E405.W9_KAPPA) / E405.W9_KAPPA <= 0.02,
          "ones Delta=%.6e c2=%.6f kappa=%.5f (R405 pins)"
          % (wo["Delta"], wo["c2"], kap_o))
    check("G22-w9-H-not-PD",
          w["nnegH"] == 1,
          "nneg(A0+v_top v_top^T)=1 -- not a one-defect split")
    rl = edge_row(9, chi=(DMF.Q_CHI3, DMF.LPQ3))
    rd = edge_row(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G23-chi-sign-split",
          rl["sch"] < 0 and rl["ab"]["ba"] > 0
          and rd["sch"] > 0 and rd["ab"]["ba"] < 0
          and abs(rl["ab"]["ba"] - (-rl["sch"])) <= ID_RES
          and abs(rd["ab"]["ba"] - (-rd["sch"])) <= ID_RES,
          "live chi3-9 sch=%.4f ba=%.4f; dead-15 sch=%+.4f ba=%+.4f"
          % (rl["sch"], rl["ab"]["ba"], rd["sch"], rd["ab"]["ba"]))
    return r9, rl, rd, wo


def part_leg3(r9):
    section("S4  LEG 3 -- CLOSED KAPPA / POSITIVE SOURCE")
    w = r9["w"]
    kap = r9["ab"]["kappa"]
    check("G30-closed-kappa-mismatch",
          abs(w["kap_f"] - kap) > 0.05,
          "kap_emp=%.5f vs -(1-eta)detK2/detKw=%.5f "
          "(2-col U is not Phi U)" % (kap, w["kap_f"]))
    # unscaled Delta vs -sch: scale mismatch (r405, now on v_top)
    check("G31-Delta-not-minus-sch",
          abs(w["Delta"] - (-r9["sch"])) > 0.05
          and w["Delta"] > 0,
          "Delta=%.4e vs -sch=%.4f -- kappa is not 1; "
          "Euler energy is not a source of Delta"
          % (w["Delta"], -r9["sch"]))
    return None


def part_kills(r9, w9leg):
    section("S5  LEG 4 -- KILLS")
    yn, wY, vt = w9leg["yn"], w9leg["wY"], w9leg["vt"]
    v_om = v_wrong_omega(yn, wY)
    v_p = v_wrong_P(yn, wY)
    g = w9leg["g"]
    _U, _s, Vt = np.linalg.svd(g["T0"], full_matrices=False)
    vsv = Vt[0]
    c_ok = abs(float(np.vdot(vt, vsv)))
    c_om = abs(float(np.vdot(v_om, vsv)))
    c_p = abs(float(np.vdot(v_p, vsv)))
    check("G40-kill-wrong-omega",
          c_om < c_ok - 0.15,
          "1/P' (no sqrt u^vee) cos(SV)=%.4f < v_top %.4f"
          % (c_om, c_ok))
    check("G41-kill-wrong-Pprime",
          c_p < 0.20,
          "fake P'=y-mean cos(SV)=%.4f (not the defect)" % c_p)
    mzP = P1.reweight(V.build_measures(9), "permute", 1000)
    gP = B.pack_graph(mzP)
    gS = B.pack_graph(HM.scramble_mz())
    check("G42-kill-permute-scramble",
          gP["nneg"] >= PERM_NNEG_LO and gS["nneg"] == SCR_NNEG,
          "PERM nneg(I-TT)=%d SCR nneg=%d -- bulk already "
          "dead, one-mode edge balance is irrelevant"
          % (gP["nneg"], gS["nneg"]))
    # border omitted: 2x2 K2 mixed on living AND dead
    rd = edge_row(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G43-kill-border-omitted",
          r9["nnegK2"] == 1 and rd["nnegK2"] == 1
          and r9["sch"] < 0 and rd["sch"] > 0,
          "K2 mixed (nneg=1) on live w9 AND dead chi15; "
          "without the SM border there is no living/dead scalar")
    return gP, gS


def part_full():
    section("S6  CENSUS -- MAIN 42 + living chi 78 + dead chi 6")
    core = list(V.admissible_indices())
    main = [edge_row(kz) for kz in core]
    n_ba = sum(1 for r in main if r["ab"]["ba"] > 0)
    n_sch = sum(1 for r in main if r["sch"] < 0)
    n_hpd = sum(1 for r in main if r["w"]["nnegH"] == 0)
    cmin = min(r["cos_neg"] for r in main)
    cmax = max(r["cos_neg"] for r in main)
    mx = max(abs(r["ab"]["ba"] - (-r["sch"])) for r in main)
    check("G50-main42-beta-gt-alpha",
          n_ba == CORE_N and n_sch == CORE_N and mx <= ID_RES,
          "MAIN beta>alpha %d/%d = sch<0; max |ba-(-sch)|=%.1e"
          % (n_ba, CORE_N, mx))
    check("G51-main42-H-not-always-PD",
          n_hpd == HPD_MAIN
          and COS_LO <= cmin and cmax <= COS_HI,
          "H PD only %d/%d; cos(v_top,vneg) in [%.3f, %.3f] "
          "-- v_top is not a uniform one-defect split"
          % (n_hpd, CORE_N, cmin, cmax))
    live3, dead3 = [], []
    for kz in core:
        r = edge_row(kz, chi=(DMF.Q_CHI3, DMF.LPQ3))
        (dead3 if kz in ES.DEAD_CHI3 else live3).append(r)
    ok3l = (len(live3) == CHI3_LIVE_N
            and all(r["ab"]["ba"] > 0 and r["sch"] < 0 for r in live3))
    ok3d = (len(dead3) == CHI3_DEAD_N
            and all(r["ab"]["ba"] < 0 and r["sch"] > 0 for r in dead3))
    check("G52-chi3-sign",
          ok3l and ok3d,
          "chi3 live %d/%d beta>alpha; dead %d/%d beta<alpha "
          "(death = chart sch>0, not a top-mode overflow)"
          % (len(live3), CHI3_LIVE_N, len(dead3), CHI3_DEAD_N))
    live4, dead4 = [], []
    for kz in core:
        r = edge_row(kz, chi=(DMF.Q_CHI4, DMF.LPQ4))
        (dead4 if kz in ES.DEAD_CHI4 else live4).append(r)
    ok4l = (len(live4) == CHI4_LIVE_N
            and all(r["ab"]["ba"] > 0 and r["sch"] < 0 for r in live4))
    ok4d = (len(dead4) == CHI4_DEAD_N
            and all(r["ab"]["ba"] < 0 and r["sch"] > 0 for r in dead4))
    check("G53-chi4-sign",
          ok4l and ok4d,
          "chi4 live %d/%d beta>alpha; dead %d/%d beta<alpha "
          "(living 78 / dead 6 with chi3)"
          % (len(live4), CHI4_LIVE_N, len(dead4), CHI4_DEAD_N))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("top_mode_edge_probe -- "
          "PRIME.RDAGGER.TOP_MODE_EDGE.01 (round 415)")
    print("SPEC_SHA %s   (ES %s / E405 %s / B %s / DI %s)"
          % (SPEC_SHA[:16], ES.SPEC_SHA[:16], E405.SPEC_SHA[:16],
             B.SPEC_SHA[:16], DI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3-42 + chi4-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and E405.SPEC_SHA.startswith(E405_SHA_PREFIX)
              and B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and MH.SPEC_SHA.startswith(MH_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / E405 %s / B %s / DI %s"
          % (ES.SPEC_SHA[:8], E405.SPEC_SHA[:8],
             B.SPEC_SHA[:8], DI.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    w9leg = part_leg1()
    r9, _rl, _rd, _wo = part_leg2(w9leg)
    part_leg3(r9)
    part_kills(r9, w9leg)
    if not smoke:
        part_full()
    else:
        section("S6  FULL CENSUS skipped (--smoke)")

    section("S7  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G60-verdict",
          prev_ok,
          "CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT: "
          "-sch=beta-alpha SATZ as r405 rewrite; v_top is "
          "not the T0/A0 defect; Euler is constant content; "
          "living/dead is r401 sch.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("TOP MODE EDGE %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("TOP MODE EDGE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
