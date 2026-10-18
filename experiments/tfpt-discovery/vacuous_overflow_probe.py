#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""vacuous_overflow_probe -- PRIME.RDAGGER.VACUOUS_OVERFLOW.01
(round 419): the tension between r417 (tau_un->0 so
sch->phibb, phibb the asymptotic sign carrier) and
r418 (6/14 vacuous core windows have phibb>0 and
still live via sch = phibb - (a_un^2+b_un^2)).
Those two cannot both be cofinal.  Three hypotheses.

THE OBJECT.  On the vacuous chart J2=I,
  sch = phibb - tau2,   tau2 = a_un^2 + b_un^2,
  phibb = c_J + Sigma,  c_J = den-2,
  Sigma = 2 s^T (C+I)(C-I)^{-1} s   (C > I).
Living overflow: phibb>0 and tau2>phibb.
Dead VAC:        phibb>0 and tau2<phibb.

H1  the 6 trend through zero with N (small-N artefacts).
H2  vacuous tau_un does NOT vanish (r417 was P1-dominated);
    then a source-pure LOWER bound on the couplings.
H3  the vacuous family empties with N (windows migrate
    to P1; overflow is asymptotically vacant).

CALIBRATION DISCLOSURE.  Core-42 + EXT-6 + selected 2^k
branch split, C_min-1, r377 products, dead-chi VAC vs
live overflow, razor-mode overlap of s, scramble /
two-period / drop-tau mutant first measured in /tmp
(r419_cal.py, r419_cal2.py) on the r401/r407/r418
constructors, 2026-08-29.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall ~80 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * H1 CENSUS not law.  The 6 stay phibb>0 on
    N in [151,540]; signed d(phibb)/d(log N)=-0.003
    (FLAT, no sign crossing).  kz49 N=540 still
    +0.0197.  Healthy VAC start at N=344 already
    negative -- N-ranges OVERLAP.  EXT VAC (70,42,72)
    and selected VAC (kz26,43) have phibb<0.
  * H2 FINITE ONLY.  r417 |t|->0 is VAC-driven:
    VAC |t| slope=-1.24, |t_un| slope=-0.99;
    P1 |t| slope=+0.05, |t_un| slope=+0.03 (FLAT).
    The 6 live NOW by tau2>phibb (margins
    0.0015..0.046).  A cofinal tau FLOOR fails
    because vacuous tau_un is the one that vanishes.
  * H3 REFUTED.  Core VAC 14/42.  Terciles by N:
    LO 3/14, MID 4/14, HI 7/14 -- VAC GROWS.
    EXT 3/6 VAC.  Selected mixed (k4 P1, k5 P1,
    k6 VAC, k7 VAC, k9 P1).  Not emptying.
  * RAZOR-POLE REFUTED.  ALL 14 VAC sit at
    C_min-1 in [1.3e-7, 7.5e-5] (healthy are
    CLOSER).  Razor-mode overlap of s is
    ~1e-10; razor share of Sigma <=0.022
    (kz39) else ~0.  Overflow is NOT
    (C-I)^{-1} explosion.  r377 prod=+1 on
    every VAC (OVF and healthy) -- not a
    separator.  kz12 LATE prototype is OVF.
  * LIFE of the overflow class vs dead VAC:
    live OVF tau2>phibb; dead VAC (chi3-23/33,
    chi4-20) tau2<phibb.  THAT is the
    separator.  Dead VAC Cgap is larger
    (1e-4..3e-3) -- further from the razor.
  * w9 (P1 control): phibb=-0.08562, not VAC.
    kz12: phibb=+0.01558, sch=-0.00594,
    tau2=0.02152, Cgap=7.36e-5, c_J=-0.4037,
    Sigma=0.4192.
    kz26 healthy: phibb=-0.06811, tau2=0.00079.
  * KILLS: drop-tau on OVF => sch=phibb>0 (dies);
    scramble nnegA0=21; two-period nneg=4;
    drop-border: no sch scalar.

AUSGANG H3_REFUTED / RAZOR_POLE_REFUTED /
TAU_SAVE_FINITE / COFINAL_OPEN.
SATZ: vacuous sch=phibb-tau2; overflow lives
iff tau2>phibb.  REDUZIERT: cofinal VAC sch<0
cannot use a tau floor (H2 cofinal fails) and
cannot use branch-emptying (H3 refuted); it
reduces to phibb<0 on large-N VAC (EXT/selected
census, the 6 themselves do not cross).  The
6 are a named finite class, not a cofinal
phenomenon.  Does not move the mincut.
No RH claim.

MACHINERY: r418 S418.split_pack, r417
S417.chart_from_row, r401 ES.main_row / chi_row,
r407 DI.chain_C, r377 PC.row_from_mz.

NO RH CLAIM.  Finite identities, named
refutations, a named reduction.  Research
documentation, not a theorem of RH.  No L*
claim.  No R-dagger claim.
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
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import postcap_pivots_probe as PC  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
CORE_N, P1_N, VAC_N, OVF_N, OKV_N = 42, 28, 14, 6, 8
SCR_NNEG, TP21_NNEG = ES.SCR_NNEG, ES.TP21_NNEG

KZ12_PHIBB, KZ12_SCH, KZ12_TAU2 = 0.01558, -0.00594, 0.02152
KZ12_CGAP = 7.36e-5
KZ26_PHIBB, KZ26_TAU2 = -0.06811, 0.00079
W9_PHIBB = S418.W9_PHIBB

SLOPE_P1_LO, SLOPE_P1_HI = -0.20, 0.30
SLOPE_VAC_LO, SLOPE_VAC_HI = -1.80, -0.60
OVF_SIGNED_ABS = 0.05
RAZOR_SHARE_HI = 0.05
REL = 5.0e-3

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
    return (not bad), ("NO zero/prime oracles; vacuous chart / "
                       "C-resolvent / SM border only"
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


def loglog_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    m = (xs > 0) & (ys > 0) & np.isfinite(xs) & np.isfinite(ys)
    if int(m.sum()) < 3:
        return float("nan")
    X, Y = np.log(xs[m]), np.log(ys[m])
    Xc = X - X.mean()
    den = float(Xc @ Xc)
    if den < 1e-18:
        return float("nan")
    return float((Xc @ (Y - Y.mean())) / den)


def slope_signed(xs, ys):
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    X = np.log(xs)
    Xc = X - X.mean()
    den = float(Xc @ Xc)
    if den < 1e-18:
        return float("nan")
    return float((Xc @ (ys - ys.mean())) / den)


def sch_vac_Q():
    """VAC chart: sch = phibb - tau2 over Q."""
    phibb = Fr(1, 10)
    au, bu = Fr(1, 2), Fr(0)
    tau2 = au * au + bu * bu
    sch = phibb - tau2
    return dict(phibb=phibb, tau2=tau2, sch=sch,
                sch_drop=phibb)


def decorate(kz, mz=None, chi=False, q=None, lpq=None):
    """split_pack + chart + C_min + razor share."""
    sp = S418.split_pack(kz, mz=mz, chi=chi, q=q, lpq=lpq)
    out = dict(sp)
    if mz is None:
        p = ES.main_row(kz)
        mz_use = PX.build_rung(kz)["mz"]
    else:
        p = None
        mz_use = mz
    if p and p.get("ok"):
        ch = S417.chart_from_row(p)
        out["sch"] = float(p["sch"])
        out["ab"] = float(p["ab"])
        out["a_un"] = ch["a_un"]
        out["b_un"] = ch["b_un"]
        out["ab_un"] = ch["ab_un"]
        out["tau2"] = ch["a_un"] ** 2 + ch["b_un"] ** 2
        out["kchart"] = ch["kchart"]
        out["detK"] = float(p.get("detK", float("nan")))
    try:
        C, _ = DI.chain_C(mz_use)
        ev = np.linalg.eigvalsh(C)
        c0 = float(ev[0])
        out["Cmin"] = c0
        out["Cgap"] = c0 - 1.0
        out["razor_share"] = float("nan")
    except Exception:
        out["Cmin"] = float("nan")
        out["Cgap"] = float("nan")
        out["razor_share"] = float("nan")
    try:
        piv = PC.row_from_mz("r%d" % kz, kz, mz_use)
        out["prod"] = int(piv["sN"] * piv["sNp1"])
    except Exception:
        out["prod"] = None
    return out


def razor_share(kz):
    """Razor-mode share of Sigma (MAIN only)."""
    sp = S418.split_pack(kz)
    R = PX.build_rung(kz)
    mz = R["mz"]
    C, _ = DI.chain_C(mz)
    ev, W = np.linalg.eigh(C)
    c0, psi = float(ev[0]), W[:, 0]
    # rebuild s (same constructors as split_pack MAIN)
    import hirota_sign_probe as HS
    import principal_bessel_probe as PB
    import augmented_borodin_duality_probe as ABD
    alk = float(V.window_shape(kz)[0])
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                       keep=True)
    yn, vn = np.asarray(mz["yn"], float), np.asarray(mz["vn"], float)
    bp = ABD.border_chain_pack(np.asarray(mz["xp"], float),
                               np.asarray(mz["wp"], float),
                               yn, vn, dsm["xs"], dsm["ws"],
                               dsm["ys"], dsm["vs"], R["Nw"])
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(mz["xp"], float),
                                  np.asarray(mz["wp"], float), R["Nw"])
    bxa = np.concatenate([np.asarray(dsm["xs"], float),
                          np.asarray(dsm["ys"], float)])
    bwa = np.concatenate([np.asarray(dsm["ws"], float),
                          -np.asarray(dsm["vs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, R["Nw"])
    vt = cut["epsY"] * (R["B"] @ (bvec / math.sqrt(bp["Bw"])))
    s = np.asarray(cut["Rm"] @ vt, float)
    ov = float(s @ psi) ** 2
    pole = 2.0 * (c0 + 1.0) / (c0 - 1.0)
    razor = pole * ov
    share = abs(razor) / abs(sp["qbb"]) if abs(sp["qbb"]) > 1e-14 else 0.0
    return dict(kz=kz, Cgap=c0 - 1.0, ov=ov, razor=razor,
                share=share, Sig=sp["qbb"], phibb=sp["phibb"],
                P1=sp["P1"])


def part_satz():
    section("S1  LEG A -- VAC CHART OVER Q + DROP-TAU")
    t = sch_vac_Q()
    check("G01-VAC-chart-Q",
          t["sch"] == Fr(-3, 20) and t["tau2"] == Fr(1, 4)
          and t["phibb"] == Fr(1, 10)
          and t["sch"] == t["phibb"] - t["tau2"],
          "sch=phibb-tau2=-3/20; tau2 saves a positive phibb")
    check("G02-drop-tau-Q",
          t["sch_drop"] == Fr(1, 10) and t["sch_drop"] > 0,
          "drop tau: sch=phibb>0 (overflow DIES)")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G03-drop-border",
          nK == nA0 == 1,
          "K2 nneg=%d == nnegA0 (no sch scalar)" % nK)


def part_pins():
    section("S2  FLAGSHIP PINS -- kz12 OVF / kz26 OKV / w9")
    r12 = decorate(12)
    check("G10-kz12-overflow",
          r12["ok"] and (not r12["P1"])
          and r12["phibb"] > 0 and r12["sch"] < 0
          and r12["tau2"] > r12["phibb"]
          and abs(r12["phibb"] - KZ12_PHIBB) <= 0.001
          and abs(r12["sch"] - KZ12_SCH) <= 0.001
          and abs(r12["tau2"] - KZ12_TAU2) <= 0.001
          and r12["Cgap"] > 0 and r12["Cgap"] < 1e-3,
          "kz12 phibb=%+.5f sch=%+.5f tau2=%.5f Cgap=%.2e "
          "(tau2>phibb saves)"
          % (r12["phibb"], r12["sch"], r12["tau2"], r12["Cgap"]))
    check("G11-drop-tau-kz12",
          r12["phibb"] > 0,
          "mutant sch=phibb=%+.5f >0 -- overflow DIES without tau"
          % r12["phibb"])
    r26 = decorate(26)
    check("G12-kz26-healthy",
          r26["ok"] and (not r26["P1"])
          and r26["phibb"] < 0 and r26["sch"] < 0
          and abs(r26["phibb"] - KZ26_PHIBB) <= 0.001
          and r26["tau2"] < 0.002
          and r26["Cgap"] > 0 and r26["Cgap"] < 1e-5,
          "kz26 phibb=%+.5f tau2=%.5f Cgap=%.2e (no tau needed)"
          % (r26["phibb"], r26["tau2"], r26["Cgap"]))
    r9 = S418.split_pack(9)
    check("G13-w9-not-VAC",
          r9["P1"] and r9["phibb"] < 0
          and abs(r9["phibb"] - W9_PHIBB) <= 0.001,
          "w9 P1 phibb=%.5f (control)" % r9["phibb"])
    z12 = razor_share(12)
    z26 = razor_share(26)
    check("G14-razor-not-pole",
          z12["share"] <= RAZOR_SHARE_HI
          and z26["share"] <= RAZOR_SHARE_HI
          and z12["ov"] < 1e-6 and z26["ov"] < 1e-6,
          "kz12 share=%.4f ov=%.2e; kz26 share=%.4f ov=%.2e "
          "(s orthogonal to the razor mode)"
          % (z12["share"], z12["ov"], z26["share"], z26["ov"]))
    return r12, r26


def part_kills():
    section("S3  LEG C -- DEAD VAC / SCRAMBLE / TWO-PERIOD")
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    tau2_23 = c23["a_un"] ** 2 + c23["b_un"] ** 2
    check("G20-dead-vac-chi3-23",
          p23["ok"] and (not p23["shift"]) and p23["sch"] > 0
          and c23["phibb"] > 0 and tau2_23 < c23["phibb"]
          and p23["nnegA0"] == 0,
          "DEAD VAC: phibb=%+.4f tau2=%.4f < phibb; sch=%+.4f"
          % (c23["phibb"], tau2_23, p23["sch"]))
    p33 = ES.chi_row(33, DMF.Q_CHI3, DMF.LPQ3, "D33")
    c33 = S417.chart_from_row(p33)
    tau2_33 = c33["a_un"] ** 2 + c33["b_un"] ** 2
    p20 = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    c20 = S417.chart_from_row(p20)
    tau2_20 = c20["a_un"] ** 2 + c20["b_un"] ** 2
    check("G21-dead-vac-class",
          p33["sch"] > 0 and tau2_33 < c33["phibb"]
          and p20["sch"] > 0 and tau2_20 < c20["phibb"]
          and c33["phibb"] > 0 and c20["phibb"] > 0,
          "chi3-33 and chi4-20: tau2<phibb (same death)")
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d (chart dies)" % oS["nneg"])
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G23-two-period",
          oT["nneg"] >= TP21_NNEG,
          "nnegA0=%d >= 4" % oT["nneg"])


def part_census(smoke):
    section("S4  H1 / H2 / H3 -- CORE + EXT + SELECTED")
    if smoke:
        section("S4b  core/EXT skipped (--smoke)")
        return None
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        r = decorate(kz)
        rows.append(r)
        tag = ("OVF" if kz in VAC_POS else
               ("VAC" if not r["P1"] else "P1 "))
        print("    %s kz%d N=%d phibb=%+.5f sch=%+.5f tau2=%.5f "
              "Cgap=%+.2e"
              % (tag, kz, r["Nw"], r["phibb"], r.get("sch", float("nan")),
                 r.get("tau2", float("nan")), r["Cgap"]), flush=True)
    ok = [r for r in rows if r.get("ok") and "sch" in r]
    p1 = [r for r in ok if r["P1"]]
    vac = [r for r in ok if not r["P1"]]
    ovf = [r for r in vac if r["kz"] in VAC_POS]
    okv = [r for r in vac if r["kz"] not in VAC_POS]
    check("G30-core-split",
          len(ok) == CORE_N and len(p1) == P1_N
          and len(vac) == VAC_N and len(ovf) == OVF_N
          and len(okv) == OKV_N
          and all(r["phibb"] > 0 and r["sch"] < 0
                  and r["tau2"] > r["phibb"] for r in ovf)
          and all(r["phibb"] < 0 and r["sch"] < 0 for r in okv),
          "P1 %d VAC %d OVF %d OKV %d; OVF all tau2>phibb"
          % (len(p1), len(vac), len(ovf), len(okv)))
    sl_ovf = slope_signed([r["Nw"] for r in ovf],
                          [r["phibb"] for r in ovf])
    check("G31-H1-no-cross",
          all(r["phibb"] > 0 for r in ovf)
          and abs(sl_ovf) <= OVF_SIGNED_ABS
          and max(r["Nw"] for r in ovf) >= 500
          and min(r["Nw"] for r in okv) <= 350,
          "OVF signed slope=%.4f (FLAT); N overlap "
          "OVF max %d / OKV min %d -- not small-N artefacts"
          % (sl_ovf, max(r["Nw"] for r in ovf),
             min(r["Nw"] for r in okv)))
    sl_t_p1 = loglog_slope([r["Nw"] for r in p1], [r["ab"] for r in p1])
    sl_t_vac = loglog_slope([r["Nw"] for r in vac], [r["ab"] for r in vac])
    sl_tu_p1 = loglog_slope([r["Nw"] for r in p1],
                            [r["ab_un"] for r in p1])
    sl_tu_vac = loglog_slope([r["Nw"] for r in vac],
                             [r["ab_un"] for r in vac])
    check("G32-H2-VAC-drives-tau",
          SLOPE_P1_LO <= sl_t_p1 <= SLOPE_P1_HI
          and SLOPE_VAC_LO <= sl_t_vac <= SLOPE_VAC_HI
          and sl_tu_vac < -0.50
          and sl_tu_p1 > -0.20,
          "P1 |t|=%.3f |t_un|=%.3f (FLAT); VAC |t|=%.3f "
          "|t_un|=%.3f (FALLS) -- r417 trend is VAC-driven"
          % (sl_t_p1, sl_tu_p1, sl_t_vac, sl_tu_vac))
    byN = sorted(ok, key=lambda r: r["Nw"])
    n = len(byN)
    lo, hi = byN[:n // 3], byN[2 * n // 3:]
    nlo = sum(1 for r in lo if not r["P1"])
    nhi = sum(1 for r in hi if not r["P1"])
    check("G33-H3-VAC-grows",
          nlo <= 4 and nhi >= 6
          and all(r["prod"] == 1 for r in vac if r.get("prod") is not None),
          "tercile VAC %d/14 -> %d/14 (GROWS); r377 prod=+1 "
          "on every VAC (not a separator)" % (nlo, nhi))
    check("G34-Cgap-all-razor",
          all(0 < r["Cgap"] < 1e-3 for r in vac)
          and min(r["Cgap"] for r in okv) < min(r["Cgap"] for r in ovf),
          "all VAC Cgap in (0,1e-3); healthy CLOSER "
          "(min OKV %.2e < min OVF %.2e) -- not a nearer pole"
          % (min(r["Cgap"] for r in okv), min(r["Cgap"] for r in ovf)))

    ext = []
    for kz in ES.SAMPLE_EXT:
        r = decorate(kz)
        ext.append(r)
        print("    EXT-%d N=%d P1=%s phibb=%+.5f Cgap=%+.2e"
              % (kz, r["Nw"], r["P1"], r["phibb"], r["Cgap"]),
              flush=True)
    ext_vac = [r for r in ext if not r["P1"]]
    check("G35-EXT-VAC-healthy",
          len(ext_vac) == 3
          and all(r["phibb"] < 0 and r["sch"] < 0 for r in ext_vac)
          and all(0 < r["Cgap"] < 1e-6 for r in ext_vac),
          "EXT VAC %d/6 all phibb<0; Cgap ~ 1e-8" % len(ext_vac))
    check("G36-EXT-VAC-frac",
          len(ext_vac) / float(len(ext)) >= 0.4,
          "EXT VAC frac=%.2f (not emptying)" % (
              len(ext_vac) / float(len(ext))))

    r26 = next(r for r in ok if r["kz"] == 26)
    r43 = next(r for r in ok if r["kz"] == 43)
    r116 = decorate(116)
    check("G37-selected-VAC-healthy",
          (not r26["P1"]) and r26["phibb"] < 0
          and (not r43["P1"]) and r43["phibb"] < 0
          and r116["P1"] and r116["phibb"] < 0,
          "selected VAC kz26/43 phibb<0; k9 P1 phibb<0")
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("vacuous_overflow_probe -- "
          "PRIME.RDAGGER.VACUOUS_OVERFLOW.01 (round 419)")
    print("SPEC_SHA %s   (ES %s / S417 %s / S418 %s / DI %s)"
          % (SPEC_SHA[:16], ES.SPEC_SHA[:16], S417.SPEC_SHA[:16],
             S418.SPEC_SHA[:16], DI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + EXT-6 + selected + razor)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / S417 %s / S418 %s / DI %s / HM %s / FTI %s / DMF %s"
          % (ES.SPEC_SHA[:8], S417.SPEC_SHA[:8], S418.SPEC_SHA[:8],
             DI.SPEC_SHA[:8], HM.SPEC_SHA[:8], FTI.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_pins()
    part_kills()
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "H3_REFUTED / RAZOR_POLE_REFUTED / TAU_SAVE_FINITE / "
          "COFINAL_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("H3_REFUTED / RAZOR_POLE_REFUTED / "
            "TAU_SAVE_FINITE / COFINAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("VACUOUS OVERFLOW %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("VACUOUS OVERFLOW FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
