#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cj_sigma_probe -- PRIME.RDAGGER.CJ_SIGMA_THRESHOLD.01
(round 420): the source-pure balance c_J < -Sigma on
the vacuous branch at large N.  r419 reduced cofinal
VAC sch<0 to phibb<0, i.e. c_J + Sigma < 0.  The two
sides: c_J = den-2 is an explicit border datum;
Sigma = 2 s^T (C+I)(C-I)^{-1} s is the bulk
self-energy of the SM border (razor pole irrelevant:
s perp C_min at 1e-10).

THE OBJECT.
  den = 1 + ||bvec||^2 / B_w - vt·s
  B_w = S_{N-2} + 5/7,   S = cumsum rho_k,  rho = F^2/h
  (r362/r397 border chain; von Mangoldt / budget).
  c_J = den - 2.  den<2 iff the budget-normalised
  border mass plus the SM correction stays below 1.
  Sigma = s^T A0^{-1} s.  Reserve R = -c_J - Sigma
  = -phibb.  Living large-N VAC: R>0.

CALIBRATION DISCLOSURE.  den identity, occupation
spectrum, naive occupied-max bound, reserve trend,
selected k=4..9, EXT, dead VAC, P1 one-balance,
scramble / drop-2 first measured in /tmp
(r420_cal.py) on the r362/r407/r418 constructors,
2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall ~80 s
(bar 120 s).  k=8 kz69 N=5690 computed in /tmp
(res=+0.0476) and NOT re-gated live (cost).
k=10 kz197 border-fail / not computed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * DEN SATZ: den = 1 + gam - vt·s with
    gam = ||bvec||^2 / B_w, B_w = S_{N-2}+5/7.
    w9: den=1.60111, gam=0.6778, B_w=8.382.
    ALL 42 core den in [1.460, 1.652] < 2;
    gap-to-2 in [0.348, 0.540] -- O(1) budget
    statement, FLAT (VAC den~N slope -0.03).
    VAC gam in [0.559, 0.724].
  * SIGMA: s occupies moderate C-modes
    (mass-weighted lam ~ 3.2..4.6).  Top-5
    share is small (kz26: 0.24).  Razor share
    <= 3e-7.  Naive bound
    Sigma <= 2||s||^2 max_occ (lam+1)/(lam-1)
    is USELESS (200..24000 x Sigma) because
    near-razor modes with occ~1e-6 blow the
    max.  ||s||^2 ~ 0.06 FLAT (slope +0.03).
    Sigma itself O(0.40) FLAT (slope +0.01).
    NO tight source-pure upper bound.
  * RESERVE R=-phibb.  Healthy VAC
    [0.011, 0.068]; OVF negative (the 6).
    Selected k=4..9 ALL phibb<0; R shrinks
    0.105 (k=5) -> 0.038 (k=9).  VAC pair
    k=6,7: 0.068 -> 0.052.  EXT VAC R in
    [0.029, 0.037].  The hoped O(1) gap is
    REFUTED: the gap is O(0.03) and shrinking.
  * ONE BALANCE: phibb = c_J + Sigma on BOTH
    charts.  P1 R_+/|Sigma| med 1.009 --
    almost all of Sigma is the positive rest.
    P1 25/28 have c_J+R_+<0; 28/28 have
    c_J+Sigma<0.  The whole edge is one
    c_J-vs-self-energy balance.
  * DEAD VAC: C3-23/33, C4-20 have R<0
    (Sigma>|c_J|) AND tau2<phibb.
  * KILLS: drop the -2 flips the sign
    (w9 den+Sigma=+1.914); scramble nneg=21;
    two-period nneg=4; s-scale does not
    change the C-occupation shape.

AUSGANG DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS
/ COFINAL_OPEN.
SATZ: the den formula.  REFUTED: an O(1)
source-pure gap c_J + Sigma < -delta.
REDUZIERT: cofinal VAC c_J<-Sigma is a
shrinking-O(0.03) census on large-N / selected
(k=4..9), no k0, no tight Sigma bound.
The 6 remain a named finite class (R<0, live
by tau).  Does not move the mincut.
No RH claim.

MACHINERY: r418 S418.split_pack, r362 ABD
border_chain_pack, r407 DI.chain_C, r419
overflow class.

NO RH CLAIM.  Finite identities, a named
refutation of the O(1) gap, a named census.
Research documentation, not a theorem of RH.
No L* claim.  No R-dagger claim.
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
import vacuous_overflow_probe as S419  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S419_SHA_PREFIX = "4809213d"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
CORE_N, P1_N, VAC_N, OVF_N, OKV_N = 42, 28, 14, 6, 8
SCR_NNEG, TP21_NNEG = ES.SCR_NNEG, ES.TP21_NNEG

W9_DEN, W9_GAM, W9_BW = 1.60111, 0.67777, 8.38240
W9_CJ, W9_SIG, W9_RES = -0.39889, 0.31326, 0.08562
KZ26_RES, KZ26_DEN = 0.06811, 1.52415
KZ12_RES = -0.01558
DEN_LO, DEN_HI = 1.45, 1.66
GAP2_LO, GAP2_HI = 0.34, 0.55
S2_LO, S2_HI = 0.04, 0.08
RES_OKV_LO = 0.010
SEL = ((4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
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
    return (not bad), ("NO zero/prime oracles; border chain / "
                       "C-resolvent only"
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


def den_Q():
    """Rational den = 1 + gam - vts."""
    gam, vts = Fr(2, 3), Fr(1, 6)
    den = Fr(1) + gam - vts
    cJ = den - Fr(2)
    return dict(den=den, cJ=cJ, gam=gam)


def den_pack(kz):
    """den pieces + occupation (MAIN only)."""
    R = PX.build_rung(kz)
    mz = R["mz"]
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
    Bw = float(bp["Bw"])
    gam = float(bvec @ bvec) / Bw
    vt = cut["epsY"] * (R["B"] @ (bvec / math.sqrt(Bw)))
    s = np.asarray(cut["Rm"] @ vt, float)
    vts = float(vt @ s)
    den = (1.0 + gam) - vts
    cJ = den - 2.0
    Sig = float(s @ np.linalg.solve(cut["A0"], s))
    s2 = float(s @ s)
    C, _ = DI.chain_C(mz)
    evC, WC = np.linalg.eigh(C)
    occ = (WC.T @ s) ** 2
    occ_n = occ / s2 if s2 > 0 else occ
    ratio = 2.0 * (evC + 1.0) / (evC - 1.0)
    mask = (occ_n > 1e-6) & (np.abs(evC - 1.0) > FLOOR)
    rmax = float(np.max(ratio[mask])) if np.any(mask) else float("nan")
    bound = rmax * s2 if np.isfinite(rmax) else float("nan")
    lam_w = (float(np.average(evC[mask], weights=occ_n[mask]))
             if np.any(mask) else float("nan"))
    return dict(
        kz=kz, Nw=int(R["Nw"]), den=den, cJ=cJ, Sig=Sig,
        reserve=-cJ - Sig, gam=gam, Bw=Bw, vts=vts, s2=s2,
        qN=float(bp["qN"]), razor_share=float(occ_n[0]),
        bound=bound, bound_ratio=bound / Sig if Sig else float("nan"),
        lam_w=lam_w, P1=int(cut["nneg"]) >= 1,
    )


def part_satz():
    section("S1  LEG A -- den FORMULA OVER Q")
    t = den_Q()
    check("G01-den-Q",
          t["den"] == Fr(3, 2) and t["cJ"] == Fr(-1, 2),
          "den=1+2/3-1/6=3/2; c_J=-1/2")
    check("G02-den-lt-2-Q",
          t["den"] < Fr(2),
          "den<2 is the budget statement")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G03-drop-border",
          nK == nA0 == 1,
          "no phibb scalar")


def part_pins():
    section("S2  w9 / kz26 / kz12 -- den + occupation")
    w = den_pack(9)
    check("G10-w9-den-identity",
          abs(w["den"] - (1.0 + w["gam"] - w["vts"])) <= 1e-12
          and abs(w["den"] - W9_DEN) <= 0.001
          and abs(w["gam"] - W9_GAM) <= 0.002
          and abs(w["Bw"] / W9_BW - 1.0) <= REL
          and abs(w["cJ"] - W9_CJ) <= 0.001
          and abs(w["reserve"] - W9_RES) <= 0.001,
          "den=1+gam-vts=%.5f gam=%.5f Bw=%.4f R=%.5f"
          % (w["den"], w["gam"], w["Bw"], w["reserve"]))
    check("G11-false-cJ",
          w["den"] + w["Sig"] > 1.5,
          "drop the -2: den+Sigma=%.4f >0 (kills the sign)"
          % (w["den"] + w["Sig"]))
    h = den_pack(26)
    check("G12-kz26-healthy",
          (not h["P1"]) and h["reserve"] > 0
          and abs(h["reserve"] - KZ26_RES) <= 0.001
          and abs(h["den"] - KZ26_DEN) <= 0.002
          and S2_LO <= h["s2"] <= S2_HI
          and 3.0 <= h["lam_w"] <= 5.0
          and h["razor_share"] < 1e-6
          and h["bound_ratio"] > 50,
          "R=%.5f s2=%.3f lam_w=%.2f razor=%.2e bound/Sig=%.0f "
          "(naive bound LOOSE)"
          % (h["reserve"], h["s2"], h["lam_w"], h["razor_share"],
             h["bound_ratio"]))
    o = den_pack(12)
    check("G13-kz12-overflow-reserve",
          (not o["P1"]) and o["reserve"] < 0
          and abs(o["reserve"] - KZ12_RES) <= 0.001,
          "OVF R=%.5f <0 (Sigma>|c_J|; lives by tau)"
          % o["reserve"])
    return w, h, o


def part_kills():
    section("S3  LEG D -- DEAD VAC / SCRAMBLE")
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    tau2 = c23["a_un"] ** 2 + c23["b_un"] ** 2
    check("G20-dead-vac-both-sides",
          c23["phibb"] > 0 and tau2 < c23["phibb"]
          and p23["sch"] > 0 and p23["nnegA0"] == 0,
          "DEAD: R=%+.4f AND tau2<phibb (both sides)"
          % (-c23["phibb"]))
    p20 = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    c20 = S417.chart_from_row(p20)
    check("G21-dead-chi4",
          c20["phibb"] > 0 and p20["sch"] > 0,
          "chi4-20 phibb=%+.4f sch=%+.4f" % (
              c20["phibb"], p20["sch"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d" % oS["nneg"])
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G23-two-period",
          oT["nneg"] >= TP21_NNEG,
          "nnegA0=%d" % oT["nneg"])


def part_census(smoke):
    section("S4  LEG B/C -- RESERVE / SELECTED / ONE-BALANCE")
    if smoke:
        section("S4b  core/EXT/selected skipped (--smoke)")
        return None
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        p = S418.split_pack(kz)
        p["reserve"] = -p["phibb"]
        rows.append(p)
        tag = ("OVF" if kz in VAC_POS else
               ("VAC" if not p["P1"] else "P1 "))
        print("    %s kz%d N=%d den=%.4f cJ=%.4f Sig=%.4f R=%+.4f"
              % (tag, kz, p["Nw"], p["den"], p["cJ"], p["qbb"],
                 p["reserve"]), flush=True)
    ok = [r for r in rows if r.get("ok")]
    p1 = [r for r in ok if r["P1"]]
    vac = [r for r in ok if not r["P1"]]
    ovf = [r for r in vac if r["kz"] in VAC_POS]
    okv = [r for r in vac if r["kz"] not in VAC_POS]
    dens = [r["den"] for r in ok]
    check("G30-den-lt-2",
          len(ok) == CORE_N
          and DEN_LO <= min(dens) and max(dens) <= DEN_HI
          and all(r["den"] < 2 for r in ok)
          and GAP2_LO <= 2 - max(dens) and 2 - min(dens) <= GAP2_HI,
          "den [%.3f, %.3f] < 2; gap-to-2 [%.3f, %.3f] (O(1) budget)"
          % (min(dens), max(dens), 2 - max(dens), 2 - min(dens)))
    check("G31-reserve-split",
          len(p1) == P1_N and len(vac) == VAC_N
          and all(r["reserve"] > 0 for r in okv)
          and all(r["reserve"] < 0 for r in ovf)
          and min(r["reserve"] for r in okv) >= RES_OKV_LO,
          "OKV R>0 in [%.4f, %.4f]; OVF all R<0"
          % (min(r["reserve"] for r in okv),
             max(r["reserve"] for r in okv)))
    check("G32-one-balance",
          all(abs(r["phibb"] - (r["cJ"] + r["qbb"])) <= 1e-12
              for r in ok)
          and all(r["phibb"] < 0 for r in p1)
          and sum(r["cJ"] + r["Rpos"] < 0 for r in p1) == 25,
          "phibb=c_J+Sigma on both charts; P1 25/28 c_J+R_+<0, "
          "28/28 c_J+Sigma<0 -- ONE balance")
    ext = []
    for kz in ES.SAMPLE_EXT:
        p = S418.split_pack(kz)
        p["reserve"] = -p["phibb"]
        ext.append(p)
        print("    EXT-%d N=%d P1=%s R=%+.4f den=%.4f"
              % (kz, p["Nw"], p["P1"], p["reserve"], p["den"]),
              flush=True)
    ext_vac = [r for r in ext if not r["P1"]]
    check("G33-EXT-VAC-reserve",
          len(ext_vac) == 3
          and all(r["reserve"] > 0 and r["den"] < 2 for r in ext_vac)
          and all(0.02 <= r["reserve"] <= 0.05 for r in ext_vac),
          "EXT VAC 3/3 R in [%.4f, %.4f] (positive, O(0.03))"
          % (min(r["reserve"] for r in ext_vac),
             max(r["reserve"] for r in ext_vac)))
    sel = []
    for k, kz in SEL:
        p = S418.split_pack(kz)
        p["k"] = k
        p["reserve"] = -p["phibb"]
        sel.append(p)
        print("    k=%d kz%d N=%d P1=%s R=%+.5f"
              % (k, kz, p["Nw"], p["P1"], p["reserve"]), flush=True)
    r6 = next(r for r in sel if r["k"] == 6)
    r7 = next(r for r in sel if r["k"] == 7)
    r9 = next(r for r in sel if r["k"] == 9)
    check("G34-selected-neg",
          all(r["phibb"] < 0 and r["reserve"] > 0 for r in sel)
          and r6["reserve"] > r7["reserve"]
          and r7["reserve"] > r9["reserve"],
          "k=4..9 all R>0; VAC 0.068->0.052 then k9 0.038 "
          "(SHRINKS, not an O(1) gap)")
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("cj_sigma_probe -- "
          "PRIME.RDAGGER.CJ_SIGMA_THRESHOLD.01 (round 420)")
    print("SPEC_SHA %s   (S418 %s / S419 %s / DI %s)"
          % (SPEC_SHA[:16], S418.SPEC_SHA[:16], S419.SPEC_SHA[:16],
             DI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + EXT-6 + selected k=4..9)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and S419.SPEC_SHA.startswith(S419_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / S418 %s / S419 %s / DI %s"
          % (ES.SPEC_SHA[:8], S418.SPEC_SHA[:8], S419.SPEC_SHA[:8],
             DI.SPEC_SHA[:8]))
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
          "DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS / "
          "COFINAL_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS / COFINAL_OPEN"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("CJ SIGMA %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("CJ SIGMA FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
