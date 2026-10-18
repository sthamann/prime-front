#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sigma_limit_probe -- PRIME.RDAGGER.SIGMA_LIMIT.01
(round 422): is Sigma_k = 2 s^T (C+I)(C-I)^{-1} s
bounded on the selected sequence with
lim sup Sigma < |c_J,inf| = 2 - den_inf, source-pure?

r421: den has O(0.5) room (flat), ||s||^2 ~ 0.06
flat, n_eff grows 18 -> 146 -> 559.  Why is the
trace bounded while occupation breaks?
  Sigma = 2 sum_i occ_i g(lam_i),  g=(lam+1)/(lam-1).
Boundedness requires occ-mass not to walk into
the g-pole at lam -> 1.

THE OBJECT.
  Exact Stieltjes form (r407):
    Sigma = 2||s||^2 + 4 s^T (C-I)^{-1} s
          = 2||s||^2 + 4 m_occ(1).
  occ_n is the spectral measure of C in the
  direction s.  Near-1 mass
    mu([1, 1+delta]) for delta in {0.1, 0.3, 1.0}.

CALIBRATION DISCLOSURE.  Selected k=5,6,7,9 occ
spectra, W1/KS, near-1 masses, Stieltjes identity,
1-pole/Cauchy closed-form attempt, overflow-6,
dead chi, EXT, first measured in /tmp
(r422_cal.py) on the r418/r420/r421 constructors,
2026-08-29.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback TAKEN for k=8: occ spectrum NOT
recomputed (r421 pin, wall 226 s).  k=10/11 not
attempted.

FROZEN FROM /tmp (live re-gated except k=8):
  * STIELTJES SATZ: Sigma = 2 s2 + 4 m(1)
    = 2 sum occ g(lam)  (resid 1e-13..1e-9).
    w9 / kz26 / selected all close.
  * CLOSED DENSITY REFUTED: 1-pole at lam_w
    misses m(1) by rel 0.73; 2-moment Cauchy
    by rel 0.95.  No elementary occ(lam).
  * NEAR-1 STABLE: selected VAC/P1
    mu([1,1.1]) = 0.0069, 0.0089, 0.0108
    (k=6,7,9) -- O(0.01), not exploding.
    mu([1,1.3]) ~ 0.06-0.07 FLAT.
    n_eff growth is BULK broadening
    (q50 -> 2.33, q75 -> 4.04), not razor creep.
    Razor share on living VAC ~ 1e-8..1e-10.
  * WEAK CONV CENSUS: KS(k5,k6)=0.140,
    KS(k6,k7)=0.096, KS(k7,k9)=0.044 -- falling.
    W1 1.28 -> 0.43 -> 0.31.  Not a theorem.
  * THREE-NUMBER: R = 2-den-Sigma is the
    finite identity (r418/r420).  den wanders
    [1.48, 1.65], Sigma [0.24, 0.48] on selected;
    EXT large-N Sigma 0.405 / 0.430 (NOT above
    k=9's 0.480).  Limits den_inf, Sigma_inf
    are NOT constructed.  Floor 0.030 is the
    residual of two O(0.5) wanderers, consistent
    but not a closed triple.
  * OVERFLOW: mu([1,1.1]) = 0.010..0.017
    (higher than living VAC 0.007).  Visible.
  * DEAD chi: razor 1.9e-4..5.7e-4
    (4-5 orders above living VAC).

AUSGANG STIELTJES_EXACT / DENSITY_REFUTED /
NEAR1_STABLE / LIMITS_OPEN.
SATZ: the Stieltjes / occupation-trace identity.
REFUTED: an elementary closed occ density;
the reading "n_eff growth => mass walks into
the pole".
REDUZIERT: lim sup Sigma < 2-den_inf is a
census (near-1 stable, Sigma not growing with
N on EXT) -- neither limit is constructed.
Does not move the mincut.
No RH claim.

MACHINERY: r420 den_pack constructors,
r407 C-resolvent, r421 selected map.

NO RH CLAIM.  Finite identities, a named
refutation of a closed density, a named census.
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
import reserve_limit_probe as S421  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S420_SHA_PREFIX = "46409e2f"
S421_SHA_PREFIX = "234a1113"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
SCR_NNEG = ES.SCR_NNEG
SEL_LIVE = ((5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, Nw=5690, Sig=0.38382, den=1.56855)
DELTAS = (0.10, 0.30, 1.00)

W9_SIG, W9_S2 = 0.31326, 0.05571
KZ26_SIG, KZ26_N01 = 0.40774, 0.0069
KZ12_SIG, KZ12_N01 = 0.41924, 0.0154
KZ26_N03, KZ9_N01 = 0.0731, 0.0108
KS79_BAR = 0.06
DEAD_RAZOR_LO = 1.0e-4
SIG_EXT_HI = 0.52
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
    return (not bad), ("NO zero/prime oracles; occ / "
                       "Stieltjes only"
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


def sigma_Q():
    """Sigma = 2 s2 + 4 m(1) = 2 sum occ g over Q."""
    # C = diag(2, 4), s = (1, 1)
    s2 = Fr(2)
    m1 = Fr(1) / Fr(1) + Fr(1) / Fr(3)  # 4/3
    Sig_st = Fr(2) * s2 + Fr(4) * m1     # 28/3
    g2, g4 = Fr(3), Fr(5, 3)
    Sig_occ = Fr(2) * (Fr(1) * g2 + Fr(1) * g4)
    return dict(s2=s2, m1=m1, Sig_st=Sig_st, Sig_occ=Sig_occ)


def occ_spec(kz, keep=False, mz=None, chi=False, q=None, lpq=None):
    """Occupation spectrum + Stieltjes identity (MAIN / chi)."""
    if mz is None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        i1, i2, Nw, S, L, Bm = (R["i1"], R["i2"], R["Nw"],
                                R["S"], mz["L"], R["B"])
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        xp, wp = mz["xp"], mz["wp"]
        bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
    else:
        j1, j2 = PX.pair_select(mz["yn"])
        i1, i2, Nw, S, L, Bm = j1, j2, mz["Nw"], mz["S"], mz["L"], None
        xp, wp = mz["xp"], mz["wp"]
        if chi:
            usm, wsm = PB.smooth_comb(mz["alpha"])
            mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
            bxs, bws, bys, bvs = (mzb["xp"], mzb["wp"],
                                  mzb["yn"], mzb["vn"])
        else:
            alk = float(mz.get("alpha", V.window_shape(kz)[0]))
            dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
            bxs, bws, bys, bvs = (dsm["xs"], dsm["ws"],
                                  dsm["ys"], dsm["vs"])
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       Nw, S, L, i1, i2, keep=True)
    yn, vn = np.asarray(mz["yn"], float), np.asarray(mz["vn"], float)
    bp = ABD.border_chain_pack(np.asarray(xp, float),
                               np.asarray(wp, float),
                               yn, vn, bxs, bws, bys, bvs, Nw)
    out = dict(ok=False, kz=kz, Nw=int(Nw))
    if not bp.get("ok"):
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                  np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    Bw = float(bp["Bw"])
    vt = cut["epsY"] * (Bm @ (bvec / math.sqrt(Bw)))
    s = np.asarray(cut["Rm"] @ vt, float)
    den = (1.0 + float(bvec @ bvec) / Bw) - float(vt @ s)
    C, _ = DI.chain_C(mz)
    evC, WC = np.linalg.eigh(C)
    occ = (WC.T @ s) ** 2
    s2 = float(s @ s)
    occ_n = occ / s2 if s2 > 0 else occ
    g = (evC + 1.0) / (evC - 1.0)
    Sig_occ = float(2.0 * np.sum(occ * g))
    I = np.eye(C.shape[0])
    m1 = float(s @ np.linalg.solve(C - I, s))
    Sig_st = 2.0 * s2 + 4.0 * m1
    Sig = float(s @ np.linalg.solve(cut["A0"], s))
    near = {d: float(np.sum(occ_n[(evC > 1.0) & (evC <= 1.0 + d)]))
            for d in DELTAS}
    n_eff = float(1.0 / np.sum(occ_n * occ_n))
    # 1-pole closed-form attempt
    lam_w = float(np.average(evC, weights=occ_n))
    m_pole = s2 / (lam_w - 1.0) if abs(lam_w - 1.0) > FLOOR else float("nan")
    out.update(
        ok=True, den=den, cJ=den - 2.0, Sig=Sig,
        Sig_occ=Sig_occ, Sig_st=Sig_st,
        dSt=abs(Sig - Sig_st), dOcc=abs(Sig - Sig_occ),
        s2=s2, m1=m1, n_eff=n_eff, near=near,
        razor=float(occ_n[0]), Cgap=float(evC[0] - 1.0),
        P1=int(cut["nneg"]) >= 1, lam_w=lam_w,
        pole_rel=abs(m_pole - m1) / abs(m1) if m1 else float("nan"),
        g_flat=2.0 * s2,
    )
    if keep:
        out["evC"] = evC
        out["occ_n"] = occ_n
    return out


def ks_dist(a, b):
    la, pa = a["evC"], a["occ_n"]
    lb, pb = b["evC"], b["occ_n"]
    xs = np.sort(np.unique(np.concatenate([la, lb])))

    def cdf(lams, ps, grid):
        order = np.argsort(lams)
        c = np.cumsum(ps[order])
        return np.interp(grid, lams[order], c, left=0.0, right=1.0)

    return float(np.max(np.abs(cdf(la, pa, xs) - cdf(lb, pb, xs))))


def part_satz():
    section("S1  LEG B -- STIELTJES IDENTITY OVER Q")
    t = sigma_Q()
    check("G01-Stieltjes-Q",
          t["Sig_st"] == t["Sig_occ"] == Fr(28, 3),
          "2 s2+4 m(1)=2 sum occ g=28/3")
    check("G02-no-flat-g-Q",
          Fr(2) * t["s2"] != t["Sig_st"],
          "g=1 (no pole) gives 4, not 28/3")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G03-drop-border",
          nK == nA0 == 1,
          "no Sigma scalar")


def part_pins():
    section("S2  w9 / kz26 / kz12 -- identity + near-1")
    w = occ_spec(9)
    check("G10-w9-Stieltjes",
          w["ok"] and w["dSt"] < 1e-10 and w["dOcc"] < 1e-10
          and abs(w["Sig"] - W9_SIG) <= 0.001
          and abs(w["s2"] - W9_S2) <= 0.002
          and w["g_flat"] < w["Sig"],
          "Sig=%.5f=2s2+4m1; g=1 gives %.5f (mutant loses)"
          % (w["Sig"], w["g_flat"]))
    h = occ_spec(26)
    check("G11-kz26-near1",
          (not h["P1"]) and abs(h["Sig"] - KZ26_SIG) <= 0.001
          and abs(h["near"][0.10] - KZ26_N01) <= 0.002
          and abs(h["near"][0.30] - KZ26_N03) <= 0.005
          and h["near"][0.10] < 0.02
          and h["razor"] < 1e-6
          and h["pole_rel"] > 0.5,
          "near[0.1]=%.4f stable; razor=%.2e; pole-rel=%.2f "
          "(closed density REFUTED)"
          % (h["near"][0.10], h["razor"], h["pole_rel"]))
    o = occ_spec(12)
    check("G12-kz12-overflow-near",
          (not o["P1"]) and o["Sig"] > -o["cJ"]
          and o["near"][0.10] > h["near"][0.10]
          and abs(o["near"][0.10] - KZ12_N01) <= 0.003,
          "OVF near[0.1]=%.4f > living %.4f (visible)"
          % (o["near"][0.10], h["near"][0.10]))
    return w, h, o


def part_kills():
    section("S3  LEG D -- DEAD / SCRAMBLE")
    uu, ww, _nn, _ch = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d = occ_spec(23, mz=mzc, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    check("G20-dead-razor",
          d["ok"] and d["razor"] >= DEAD_RAZOR_LO
          and c23["phibb"] > 0,
          "DEAD razor=%.2e (4-5 orders above living); R=%+.4f"
          % (d["razor"], -c23["phibb"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G21-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d (bulk dead)" % oS["nneg"])


def part_census(smoke):
    section("S4  LEG A/C -- SELECTED OCC / KS / BALANCE")
    if smoke:
        section("S4b  selected/EXT skipped (--smoke)")
        return None
    sel = []
    for k, kz in SEL_LIVE:
        keep = k in (7, 9)
        r = occ_spec(kz, keep=keep)
        r["k"] = k
        r["reserve"] = -r["cJ"] - r["Sig"]
        sel.append(r)
        print("    k=%d kz%d N=%d Sig=%.5f den=%.5f near01=%.4f "
              "neff=%.1f dSt=%.1e"
              % (k, kz, r["Nw"], r["Sig"], r["den"],
                 r["near"][0.10], r["n_eff"], r["dSt"]), flush=True)
    r6 = next(r for r in sel if r["k"] == 6)
    r7 = next(r for r in sel if r["k"] == 7)
    r9 = next(r for r in sel if r["k"] == 9)
    check("G30-selected-near1",
          all(r["ok"] and r["dSt"] < 1e-8 for r in sel)
          and r6["near"][0.10] < 0.02
          and r7["near"][0.10] < 0.02
          and abs(r9["near"][0.10] - KZ9_N01) <= 0.003
          and r6["near"][0.30] < 0.10 and r9["near"][0.30] < 0.10,
          "k=6,7,9 near[0.1] O(0.01) stable; Stieltjes resid <1e-8")
    ks79 = ks_dist(r7, r9)
    check("G31-KS-falling",
          ks79 < KS79_BAR,
          "KS(k7,k9)=%.4f < %.2f (weak-conv census, not a theorem)"
          % (ks79, KS79_BAR))
    dens = [r["den"] for r in sel]
    sigs = [r["Sig"] for r in sel]
    check("G32-balance-identity",
          all(abs(r["reserve"] - (2.0 - r["den"] - r["Sig"])) <= 1e-12
              for r in sel)
          and 1.45 <= min(dens) and max(dens) <= 1.66
          and max(sigs) < 0.52
          and K8_PIN["Sig"] < 0.52,
          "R=2-den-Sigma; den[%.3f,%.3f]; Sigma<=%.3f "
          "(k=8 pin %.3f); limits NOT constructed"
          % (min(dens), max(dens), max(sigs), K8_PIN["Sig"]))
    ext_vac = []
    for kz in ES.SAMPLE_EXT:
        r = occ_spec(kz)
        if r["ok"] and (not r["P1"]):
            ext_vac.append(r)
            print("    EXT-%d N=%d Sig=%.5f near01=%.4f"
                  % (kz, r["Nw"], r["Sig"], r["near"][0.10]),
                  flush=True)
    check("G33-EXT-bounded",
          len(ext_vac) == 3
          and all(r["Sig"] < SIG_EXT_HI for r in ext_vac)
          and all(r["near"][0.10] < 0.03 for r in ext_vac),
          "EXT VAC Sigma in [%.3f, %.3f] < 0.52; near-1 stable"
          % (min(r["Sig"] for r in ext_vac),
             max(r["Sig"] for r in ext_vac)))
    return sel


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("sigma_limit_probe -- "
          "PRIME.RDAGGER.SIGMA_LIMIT.01 (round 422)")
    print("SPEC_SHA %s   (S421 %s / S420 %s / S418 %s)"
          % (SPEC_SHA[:16], S421.SPEC_SHA[:16], S420.SPEC_SHA[:16],
             S418.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=5,6,7,9 + EXT; k=8 pinned)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and S420.SPEC_SHA.startswith(S420_SHA_PREFIX)
              and S421.SPEC_SHA.startswith(S421_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "S421 %s / S420 %s / S418 %s"
          % (S421.SPEC_SHA[:8], S420.SPEC_SHA[:8], S418.SPEC_SHA[:8]))
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
          "STIELTJES_EXACT / DENSITY_REFUTED / NEAR1_STABLE / "
          "LIMITS_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("STIELTJES_EXACT / DENSITY_REFUTED / "
            "NEAR1_STABLE / LIMITS_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("SIGMA LIMIT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("SIGMA LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
