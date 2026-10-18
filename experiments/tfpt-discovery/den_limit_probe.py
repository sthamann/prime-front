#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""den_limit_probe -- PRIME.RDAGGER.DEN_LIMIT.01
(round 423): does den_k -> den_inf < 2 on the
selected sequence, with den_inf source-pure
(or at least lim sup den <= dbar < 2 explicit)?

Formula (r420 SATZ):
  den = 1 + gam - vts,  gam = ||b||^2 / B_w,
  B_w = S_{N-2} + 5/7,  S = cumsum rho, rho = F^2/h.
Measured: den in [1.48, 1.65], gap-to-2 >= 0.348.

THE OBJECT.
  Hierarchy: (i) den_inf as a constructed limit
  (Stolz-Cesaro on the rho series + vts limit);
  (ii) lim sup gam <= gbar explicit (is ||b||^2
  <= B_w a chain inequality?);
  (iii) census with deeper points.

CALIBRATION DISCLOSURE.  Selected k=4,5,6,7,9
rich packs, core-42 den_pack, EXT-6, dead chi,
prefix ||b||^2 vs S, drop-5/7, first measured
in /tmp (r423_cal.py) on the r420 constructors,
2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback TAKEN for k=8: r421 pin
den=1.56855 gam=0.6386, not re-gated live.

FROZEN FROM /tmp (live re-gated except k=8):
  * FORMULA SATZ: den = 1+gam-vts.  Q: gam=2/3,
    vts=1/6 => den=3/2 < 2.
  * gam < 1 on 42/42 + EXT 6/6 + dead 2/2
    (core [0.548, 0.724]).  vts > 0 on all
    those (core [0.067, 0.096]).  Hence
    den <= 1+0.724-0.067 = 1.657 < 2 on the
    census; measured max den=1.652, gap min
    0.348.  If gam<1 were a theorem, den<2
    would follow from the formula even at
    vts=0 (den=1+gam<2).  gam<1 is NOT proved.
  * ||b||^2 is NOT a subsum of S: prefix
    b2/S falls 0.92 -> 0.65.  Drop 5/7:
    b2/S_{N-2} still < 1 (selected max 0.80).
  * NO den_inf: den wanders [1.460, 1.652].
    gam selected 0.678, 0.712, 0.609, 0.604,
    0.576 -- not a constructed limit.
    Stolz increments Delta b2 / Delta Bw
    ~ 0.58, 0.52 (diagnosis, not a theorem).
    rho last -> 0 on selected; rho0 share
    0.46 -> 0.26; S still grows (more terms).
  * vts O(0.08), all positive, mild rise
    0.061 -> 0.093 on selected.  Not a limit.
  * DEAD chi: den=1.546, 1.597 both < 2
    (death is Sigma/razor, not den).
  * k=8 pin den=1.56855.

AUSGANG FORMULA_EXACT / GAMMA_LT1_CENSUS /
LIMIT_OPEN / SUBSUM_REFUTED.
SATZ: the den formula.  Hierarchy (i) not
reached.  Hierarchy (ii): gam<1 is a universal
census, not a chain SATZ; ||b||^2 is not a
subsum of B_w.  Hierarchy (iii): den<2 with
explicit census dbar=1.66, gap>=0.348.
REDUZIERT.  Does not move the mincut.
No RH claim.

MACHINERY: r420 S420.den_pack / ABD border
chain / bvec.

NO RH CLAIM.  Finite identities, a named
refutation of the subsum reading, a named
census.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
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
import sigma_limit_probe as S422  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S420_SHA_PREFIX = "46409e2f"
S422_SHA_PREFIX = "d81fc5fc"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
SCR_NNEG = ES.SCR_NNEG
SEL_LIVE = ((4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, den=1.56855, gam=0.6386)
W9_DEN, W9_GAM, W9_VTS, W9_BW = 1.60111, 0.67777, 0.07665, 8.38240
GAM_HI, VTS_LO, DEN_HI, GAP2_LO = 0.73, 0.060, 1.66, 0.34
CORE_N = 42
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
    return (not bad), ("NO zero/prime oracles; den / "
                       "border chain only"
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
    """den = 1+gam-vts over Q; gam<1 and vts>0."""
    t = S420.den_Q()
    t["vts"] = Fr(1, 6)
    t["gap2"] = Fr(2) - t["den"]
    return t


def den_rich(kz):
    """den pieces + ||b||^2 vs S (MAIN)."""
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
    out = dict(ok=False, kz=kz, Nw=int(R["Nw"]))
    if not bp.get("ok"):
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(mz["xp"], float),
                                  np.asarray(mz["wp"], float), R["Nw"])
    bxa = np.concatenate([np.asarray(dsm["xs"], float),
                          np.asarray(dsm["ys"], float)])
    bwa = np.concatenate([np.asarray(dsm["ws"], float),
                          -np.asarray(dsm["vs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, R["Nw"])
    b2 = float(bvec @ bvec)
    Bw = float(bp["Bw"])
    Nw = int(R["Nw"])
    SN2 = float(bp["S"][Nw - 2])
    SN1 = float(bp["S"][Nw - 1])
    gam = b2 / Bw
    vt = cut["epsY"] * (R["B"] @ (bvec / math.sqrt(Bw)))
    s = np.asarray(cut["Rm"] @ vt, float)
    vts = float(vt @ s)
    den = (1.0 + gam) - vts
    mid = Nw // 2
    b2_mid = float(np.sum(bvec[:mid] ** 2))
    S_mid = float(bp["S"][mid - 1]) if mid else 0.0
    out.update(
        ok=True, den=den, gam=gam, vts=vts, b2=b2, Bw=Bw,
        SN2=SN2, SN1=SN1, gam_no57=b2 / SN2 if SN2 else float("nan"),
        pref_ratio=b2_mid / S_mid if S_mid else float("nan"),
        end_ratio=b2 / SN1 if SN1 else float("nan"),
        P1=int(cut["nneg"]) >= 1,
        last=float(bp["rho"][Nw - 1]),
        rho0_share=float(bp["rho"][0]) / SN1 if SN1 else float("nan"),
    )
    return out


def part_satz():
    section("S1  LEG C -- den FORMULA / gam<1 OVER Q")
    t = den_Q()
    check("G01-den-Q",
          t["den"] == Fr(3, 2) and t["gam"] == Fr(2, 3)
          and t["vts"] == Fr(1, 6) and t["gam"] < Fr(1)
          and t["vts"] > Fr(0) and t["den"] < Fr(2),
          "den=1+2/3-1/6=3/2; gam<1 and vts>0")
    check("G02-drop-vts-Q",
          Fr(1) + t["gam"] < Fr(2),
          "even vts=0: 1+gam=5/3<2 if gam<1")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G03-drop-border",
          nK == nA0 == 1,
          "no den scalar")


def part_pins():
    section("S2  w9 / kz26 -- formula + not-subsum")
    w = den_rich(9)
    check("G10-w9-formula",
          w["ok"]
          and abs(w["den"] - (1.0 + w["gam"] - w["vts"])) <= 1e-12
          and abs(w["den"] - W9_DEN) <= 0.001
          and abs(w["gam"] - W9_GAM) <= 0.002
          and abs(w["vts"] - W9_VTS) <= 0.002
          and w["gam"] < 1 and w["vts"] > 0
          and w["gam_no57"] < 1,
          "den=%.5f gam=%.4f vts=%.4f; drop-5/7 gam=%.4f<1"
          % (w["den"], w["gam"], w["vts"], w["gam_no57"]))
    check("G11-w9-not-subsum",
          w["pref_ratio"] < 0.95 and w["end_ratio"] < 0.80
          and w["pref_ratio"] > w["end_ratio"],
          "b2/S prefix %.3f -> end %.3f (NOT a subsum of S)"
          % (w["pref_ratio"], w["end_ratio"]))
    h = S420.den_pack(26)
    check("G12-kz26",
          (not h["P1"]) and h["gam"] < 1 and h["vts"] > 0
          and h["den"] < 2 and abs(h["den"] - 1.52415) <= 0.001,
          "VAC den=%.5f gam=%.4f vts=%.4f" % (
              h["den"], h["gam"], h["vts"]))
    return w, h


def part_kills():
    section("S3  LEG D -- DEAD / SCRAMBLE")
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    den23 = float(p23["den"])
    check("G20-dead-den",
          c23["phibb"] > 0 and den23 < 2,
          "DEAD C3-23 den=%.4f <2 (death is Sigma, not den); "
          "phibb=%+.4f" % (den23, c23["phibb"]))
    p20 = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    check("G21-dead-chi4-den",
          float(p20["den"]) < 2,
          "C4-20 den=%.4f <2" % float(p20["den"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d" % oS["nneg"])


def part_census(smoke):
    section("S4  LEG A/B/C -- CORE / SELECTED / EXT")
    if smoke:
        section("S4b  core/EXT skipped (--smoke)")
        return None
    rows = []
    for kz in V.admissible_indices():
        w = S420.den_pack(kz)
        rows.append(w)
    gams = [r["gam"] for r in rows]
    vtss = [r["vts"] for r in rows]
    dens = [r["den"] for r in rows]
    check("G30-core-gam-lt1",
          len(rows) == CORE_N
          and all(g < 1 for g in gams)
          and max(gams) <= GAM_HI
          and all(v > 0 for v in vtss)
          and min(vtss) >= VTS_LO
          and all(d < 2 for d in dens)
          and max(dens) <= DEN_HI
          and min(2 - d for d in dens) >= GAP2_LO,
          "42/42 gam[%.3f,%.3f]<1; vts[%.3f,%.3f]>0; "
          "den[%.3f,%.3f]<2; gap>=%.3f"
          % (min(gams), max(gams), min(vtss), max(vtss),
             min(dens), max(dens), min(2 - d for d in dens)))
    sel = []
    for k, kz in SEL_LIVE:
        r = den_rich(kz)
        r["k"] = k
        sel.append(r)
        print("    k=%d kz%d den=%.5f gam=%.4f vts=%.4f "
              "b2/SN1=%.3f last=%.4f"
              % (k, kz, r["den"], r["gam"], r["vts"],
                 r["end_ratio"], r["last"]), flush=True)
    r4 = next(r for r in sel if r["k"] == 4)
    r9 = next(r for r in sel if r["k"] == 9)
    check("G31-selected-no-limit",
          all(r["ok"] and r["gam"] < 1 and r["vts"] > 0
              and r["den"] < 2 and r["gam_no57"] < 1
              for r in sel)
          and r4["den"] > r9["den"]
          and r4["end_ratio"] > r9["end_ratio"]
          and r9["last"] < 0.01,
          "selected gam<1; den shrinks 1.601->1.482 "
          "(NO constructed den_inf); last rho->0; "
          "k=8 pin den=%.5f" % K8_PIN["den"])
    ext = []
    for kz in ES.SAMPLE_EXT:
        w = S420.den_pack(kz)
        ext.append(w)
        print("    EXT-%d den=%.5f gam=%.4f vts=%.4f"
              % (kz, w["den"], w["gam"], w["vts"]), flush=True)
    check("G32-EXT",
          all(w["gam"] < 1 and w["vts"] > 0 and w["den"] < DEN_HI
              for w in ext),
          "EXT 6/6 gam<1 vts>0 den<=%.3f"
          % max(w["den"] for w in ext))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("den_limit_probe -- "
          "PRIME.RDAGGER.DEN_LIMIT.01 (round 423)")
    print("SPEC_SHA %s   (S420 %s / S422 %s)"
          % (SPEC_SHA[:16], S420.SPEC_SHA[:16], S422.SPEC_SHA[:16]))
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
              and S422.SPEC_SHA.startswith(S422_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "S420 %s / S422 %s" % (S420.SPEC_SHA[:8], S422.SPEC_SHA[:8]))
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
          "FORMULA_EXACT / GAMMA_LT1_CENSUS / LIMIT_OPEN / "
          "SUBSUM_REFUTED.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("FORMULA_EXACT / GAMMA_LT1_CENSUS / "
            "LIMIT_OPEN / SUBSUM_REFUTED")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("DEN LIMIT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DEN LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
