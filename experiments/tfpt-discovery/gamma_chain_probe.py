#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gamma_chain_probe -- PRIME.RDAGGER.GAMMA_CHAIN.01
(round 424): is gamma = ||b||^2 / B_w < 1 a
border-chain inequality (so den<2 follows from
1+gamma<2 even at v_t·s = 0)?

THE OBJECT.
  b is the mu-orthonormal border vector
  (ABD.bvec_chunked): b_k = sum_a w_a phat_k(t_a),
  the pairings of the signed border measure sigma
  against the mu-OP frame.  Parseval:
  ||b||^2 = sum_k (int phat_k^mu d sigma)^2
  equals BH.mu_side_budget (machine identity).
  B_w = S_{N-2}+5/7 lives on the OTHER chain
  (mu-tilde, rho_k = F_k^2/h_k).  So gamma<1 is a
  CROSS-CHAIN comparison, not a same-frame Bessel.

CALIBRATION DISCLOSURE.  b vs mu-side, w_k =
b_k^2/rho_k, ||b||^2 vs S vs B_w, unnorm mutant,
permute/scramble, core-42, selected, EXT, dead
chi first measured in /tmp (r424_cal.py,
r424_cal2.py) on the r420 constructors,
2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback TAKEN for k=8: r421 pin
gamma=0.6386, not re-gated live.

FROZEN FROM /tmp (live re-gated except k=8):
  * BESSEL SATZ: ||b||^2 == mu_side_budget
    (dmsb ~ 1e-13 on w9).  Q-toy: b=(3/5,4/5),
    leftover 7/9 => ||b||^2=1 < 16/9 = ||phi||^2.
  * w_k NOT uniform: ~43% of terms >1, max
    10^6..10^9 (tiny rho).  Median ~0.6, w_0~0.94.
    SUBSUM already dead (r423); termwise wbar<1
    is also REFUTED.
  * ||b||^2 < S on every measured world
    (selected max gam_S=0.799 at k=5; core max
    0.766).  So the 5/7 buffer is NOT needed for
    the census inequality.  Sharp census:
    ||b||^2 <= 0.80 S.  gamma <= 0.724.
  * DEAD chi keep gamma<1 and gam_S<1.
    Scramble / shuffle-wp: border_fail (no
    tilde chain).  Reorder atoms: gamma
    unchanged.  Unnorm b (drop 1/sqrt(h0)):
    gamma=2.51>1 -- orthonormality is load-bearing.
  * k=8 pin gamma=0.6386.

AUSGANG BESSEL_EXACT / W_TERM_REFUTED /
SHARP_CENSUS / GAMMA_OPEN.
SATZ: b is the mu-Parseval coefficient of sigma.
REFUTED: uniform w_k <= wbar<1.
CENSUS: ||b||^2 <= 0.80 S and gamma<1 on
42/42+EXT+dead.  gamma<1 as a theorem is OPEN
(cross-chain).  REDUZIERT.  Does not move the
mincut.  No RH claim.

MACHINERY: ABD.bvec_chunked / BH.mu_side_budget
/ ABD.border_chain_pack / r420 den_pack.

NO RH CLAIM.  Finite identity, a named
refutation of termwise w_k, a named census.
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

import cj_sigma_probe as S420  # noqa: E402
import den_limit_probe as S423  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S420_SHA_PREFIX = "46409e2f"
S423_SHA_PREFIX = "15693316"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
SCR_NNEG = ES.SCR_NNEG
SEL_LIVE = ((4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, gam=0.6386)
W9_B2, W9_GAM, W9_GAMS = 5.6813, 0.6778, 0.7264
W9_W0, W9_FRAC_GT1 = 0.939, 0.43
KZ26_GAM, KZ26_GAMS = 0.6089, 0.6540
GAM_HI, GAMS_HI, QBAR = 0.73, 0.81, 0.80
CORE_N = 42
UNNORM_GAM_LO = 2.0

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
    return (not bad), ("NO zero/prime oracles; border "
                       "chain / mu-Parseval only"
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


def bessel_Q():
    """orthonormal leftover Bessel over Q, plus gamma bookkeeping."""
    a0, a1, leftover2 = Fr(3, 5), Fr(4, 5), Fr(7, 9)
    b2 = a0 * a0 + a1 * a1
    phi2 = b2 + leftover2
    S = Fr(3)
    Bw = S + Fr(5, 7)
    gam = Fr(2) / Bw
    return dict(b2=b2, phi2=phi2, leftover2=leftover2,
                gam=gam, Bw=Bw, S=S)


def bvec_unnorm(a_mu, b_mu, h0_mu, bxa, bwa, Nw):
    """mutant: drop the 1/sqrt(h0) start."""
    b = np.zeros(Nw)
    t = np.asarray(bxa, float)
    w = np.asarray(bwa, float)
    u = np.ones_like(t)
    um = np.zeros_like(t)
    b[0] += float(w @ u)
    for i in range(Nw - 1):
        r = (t - a_mu[i]) * u - (b_mu[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b_mu[i]
        b[i + 1] += float(w @ u)
    return b


def chain_pack(kz, mz=None, chi=False, lpq=None, xp=None, wp=None):
    """b, rho, B_w, mu-side, w_k on one window.  No cut_rung."""
    if mz is None and xp is None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        Nw = R["Nw"]
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        xp, wp = mz["xp"], mz["wp"]
        yn, vn = mz["yn"], mz["vn"]
        bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
    elif xp is not None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        Nw = R["Nw"]
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        yn, vn = mz["yn"], mz["vn"]
        bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
        wp = mz["wp"] if wp is None else wp
    else:
        Nw = mz["Nw"]
        xp, wp = mz["xp"], mz["wp"]
        yn, vn = mz["yn"], mz["vn"]
        if chi:
            usm, wsm = PB.smooth_comb(mz["alpha"])
            mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
            bxs, bws, bys, bvs = (mzb["xp"], mzb["wp"],
                                  mzb["yn"], mzb["vn"])
        else:
            alk = float(mz.get("alpha", 1.0))
            dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
            bxs, bws, bys, bvs = (dsm["xs"], dsm["ws"],
                                  dsm["ys"], dsm["vs"])
    xp = np.asarray(xp, float)
    wp = np.asarray(wp, float)
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bp = ABD.border_chain_pack(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw)
    out = dict(ok=False, kz=kz, Nw=int(Nw))
    if not bp.get("ok"):
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(xp, wp, Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    b2 = float(bvec @ bvec)
    msb = float(BH.mu_side_budget(xp, wp, bxa, bwa, Nw))
    rho = np.asarray(bp["rho"], float)
    Nw = int(Nw)
    SN2 = float(bp["S"][Nw - 2])
    SN1 = float(bp["S"][Nw - 1])
    Bw = float(bp["Bw"])
    mask = rho > 1e-18
    wk = np.full(Nw, np.nan)
    wk[mask] = (bvec[mask] ** 2) / rho[mask]
    finite = wk[np.isfinite(wk)]
    n_gt1 = int(np.sum(finite > 1.0))
    bun = bvec_unnorm(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    bun2 = float(bun @ bun)
    out.update(
        ok=True, b2=b2, msb=msb, dmsb=abs(b2 - msb),
        Bw=Bw, SN2=SN2, SN1=SN1,
        gam=b2 / Bw, gam_S=b2 / SN1, gam_S2=b2 / SN2,
        wmax=float(np.nanmax(wk)) if finite.size else float("nan"),
        wmed=float(np.nanmedian(wk)) if finite.size else float("nan"),
        w0=float(wk[0]) if np.isfinite(wk[0]) else float("nan"),
        n_gt1=n_gt1,
        n_w=int(finite.size),
        frac_gt1=n_gt1 / max(int(finite.size), 1),
        bun_gam=bun2 / Bw,
        qN=float(bp["qN"]),
    )
    return out


def part_satz():
    section("S1  LEG A -- BESSEL OVER Q / BOOKKEEPING")
    t = bessel_Q()
    check("G01-bessel-Q",
          t["b2"] == Fr(1) and t["phi2"] == Fr(16, 9)
          and t["b2"] < t["phi2"],
          "||b||^2=1 < 16/9=||phi||^2 (leftover 7/9)")
    check("G02-gamma-Q",
          t["gam"] == Fr(7, 13) and t["gam"] < Fr(1)
          and t["S"] + Fr(5, 7) == t["Bw"],
          "bookkeeping gam=2/(3+5/7)=7/13<1")
    check("G03-drop-vts-Q",
          Fr(1) + t["gam"] < Fr(2),
          "1+gam=20/13<2 if gam<1")


def part_pins():
    section("S2  w9 / kz26 -- Parseval + w_k anatomy")
    w = chain_pack(9)
    check("G10-w9-parseval",
          w["ok"]
          and w["dmsb"] <= 1e-10
          and abs(w["b2"] - W9_B2) <= 0.002
          and abs(w["gam"] - W9_GAM) <= 0.002
          and abs(w["gam_S"] - W9_GAMS) <= 0.003
          and w["gam"] < 1 and w["gam_S"] < 1
          and w["gam_S2"] < 1,
          "b2=%.4f msb=%.4f dmsb=%.1e gam=%.4f gamS=%.4f"
          % (w["b2"], w["msb"], w["dmsb"], w["gam"], w["gam_S"]))
    check("G11-w9-wterm",
          w["frac_gt1"] >= 0.35 and w["wmax"] > 10.0
          and w["w0"] < 1.0 and abs(w["w0"] - W9_W0) <= 0.02
          and w["wmed"] < 1.0,
          "frac(w>1)=%.2f wmax=%.1e w0=%.3f wmed=%.3f "
          "(NO uniform wbar<1)"
          % (w["frac_gt1"], w["wmax"], w["w0"], w["wmed"]))
    h = chain_pack(26)
    check("G12-kz26",
          h["ok"] and h["dmsb"] <= 1e-10
          and abs(h["gam"] - KZ26_GAM) <= 0.003
          and abs(h["gam_S"] - KZ26_GAMS) <= 0.003
          and h["gam"] < 1 and h["gam_S"] < QBAR,
          "VAC gam=%.4f gamS=%.4f" % (h["gam"], h["gam_S"]))
    return w, h


def part_kills():
    section("S3  LEG D -- DEAD / SCRAMBLE / MUTANT / PERMUTE")
    uu, ww, _nn, _ch = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d23 = chain_pack(23, mz=mzc, chi=True, lpq=DMF.LPQ3)
    check("G20-dead-gamma",
          d23["ok"] and d23["gam"] < 1 and d23["gam_S"] < 1
          and d23["dmsb"] <= 1e-10,
          "DEAD C3-23 gam=%.4f gamS=%.4f (chain, no arith)"
          % (d23["gam"], d23["gam_S"]))
    uu4, ww4, _n4, _c4 = DMF.chi_window_comb(20, DMF.Q_CHI4)
    mz4 = DMF.chi_build_measures(20, uu4, ww4, 1.0, DMF.LPQ4)
    d20 = chain_pack(20, mz=mz4, chi=True, lpq=DMF.LPQ4)
    check("G21-dead-chi4",
          d20["ok"] and d20["gam"] < 1 and d20["gam_S"] < 1,
          "C4-20 gam=%.4f gamS=%.4f" % (d20["gam"], d20["gam_S"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    scr = chain_pack(0, mz=mz_s)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG and (not scr.get("ok")),
          "nnegA0=%d border_fail=%s" % (oS["nneg"], not scr.get("ok")))
    w = chain_pack(9)
    check("G23-unnorm",
          w["bun_gam"] >= UNNORM_GAM_LO,
          "unnorm gam=%.3f>1 (h0-norm is load-bearing)"
          % w["bun_gam"])
    R = PX.build_rung(9)
    wrv = chain_pack(9, xp=R["mz"]["xp"][::-1], wp=R["mz"]["wp"][::-1])
    check("G24-permute-same",
          wrv["ok"] and abs(wrv["gam"] - w["gam"]) <= 1e-9,
          "rev-xp gam=%.4f == true (atom order free)"
          % wrv["gam"])


def part_census(smoke):
    section("S4  LEG B/C -- CORE / SELECTED / EXT")
    if smoke:
        section("S4b  core/EXT skipped (--smoke)")
        return None
    rows = []
    for kz in V.admissible_indices():
        r = chain_pack(kz)
        rows.append(r)
    gams = [r["gam"] for r in rows]
    gamS = [r["gam_S"] for r in rows]
    dmsbs = [r["dmsb"] for r in rows]
    n_gt = [r["n_gt1"] for r in rows]
    check("G30-core-parseval-gamma",
          len(rows) == CORE_N
          and all(r["ok"] for r in rows)
          and max(dmsbs) <= 1e-9
          and all(g < 1 for g in gams)
          and max(gams) <= GAM_HI
          and all(g < 1 for g in gamS)
          and max(gamS) <= GAMS_HI
          and all(n > 0 for n in n_gt),
          "42/42 parseval; gam[%.3f,%.3f]<1; "
          "gamS[%.3f,%.3f]<0.81; w>1 on 42/42"
          % (min(gams), max(gams), min(gamS), max(gamS)))
    sel = []
    for k, kz in SEL_LIVE:
        r = chain_pack(kz)
        r["k"] = k
        sel.append(r)
        print("    k=%d kz%d gam=%.4f gamS=%.4f b2=%.3f "
              "w0=%.3f frac>1=%.2f"
              % (k, kz, r["gam"], r["gam_S"], r["b2"],
                 r["w0"], r["frac_gt1"]), flush=True)
    r5 = next(r for r in sel if r["k"] == 5)
    check("G31-selected-sharp",
          all(r["ok"] and r["gam"] < 1 and r["gam_S"] <= QBAR
              and r["dmsb"] <= 1e-9 for r in sel)
          and r5["gam_S"] >= 0.79 and r5["gam_S"] <= QBAR,
          "selected gamS<=0.80; k=5 tightest gamS=%.4f; "
          "k=8 pin gam=%.4f" % (r5["gam_S"], K8_PIN["gam"]))
    ext = []
    for kz in ES.SAMPLE_EXT:
        r = chain_pack(kz)
        ext.append(r)
        print("    EXT-%d gam=%.4f gamS=%.4f"
              % (kz, r["gam"], r["gam_S"]), flush=True)
    check("G32-EXT",
          all(r["ok"] and r["gam"] < 1 and r["gam_S"] <= QBAR
              for r in ext),
          "EXT 6/6 gam<1 gamS<=0.80")
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("gamma_chain_probe -- "
          "PRIME.RDAGGER.GAMMA_CHAIN.01 (round 424)")
    print("SPEC_SHA %s   (S420 %s / S423 %s)"
          % (SPEC_SHA[:16], S420.SPEC_SHA[:16], S423.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + selected + EXT; k=8 pinned)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and S420.SPEC_SHA.startswith(S420_SHA_PREFIX)
              and S423.SPEC_SHA.startswith(S423_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "S420 %s / S423 %s" % (S420.SPEC_SHA[:8], S423.SPEC_SHA[:8]))
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
          "BESSEL_EXACT / W_TERM_REFUTED / SHARP_CENSUS / "
          "GAMMA_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("BESSEL_EXACT / W_TERM_REFUTED / "
            "SHARP_CENSUS / GAMMA_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("GAMMA CHAIN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("GAMMA CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
