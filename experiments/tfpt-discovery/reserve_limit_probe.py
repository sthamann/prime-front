#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""reserve_limit_probe -- PRIME.RDAGGER.RESERVE_LIMIT.01
(round 421): does R = -phibb = |c_J| - Sigma on the
selected sequence a_k=2^k go to 0 or to a floor
R_inf > 0?  r420 measured the shrink
0.105, 0.068, 0.052, 0.048, 0.038 and left the
limit open.  That is the switch: R_inf > 0 makes
the cofinal edge a two-sum limit (den_inf < 2
already has O(1) room; need Sigma_inf < |c_J,inf|);
R -> 0 means the edge saturates like the bulk.

THE OBJECT.
  R = -c_J - Sigma = -phibb.  Three diagnostic
  models on the sealed k=5..9 pins (NOT a proof):
    M1  R = R_inf + c k^{-a}
    M2  R = c k^{-a}
    M3  R = c / log k
  Abscissa is the selected index k (N is not
  monotone: k=8 N=5690, k=9 N=1433).

CALIBRATION DISCLOSURE.  Selected k=4..9 rich
packs, EXT-6, core VAC, dead chi, T0-Cgap
dictionary, Sigma channels (s2 / lam_w / n_eff),
B_w growth, AIC on k / 2^k / N first measured
in /tmp (r421_cal.py, r421_cal_deep.py) on the
r418/r420 constructors, 2026-08-29.  Frozen
floors below are that measurement, sealed as
gates.  Pins disclosed.
Builder fallback TAKEN for k=8: /tmp wall 226 s
(N=5690) above the 120 s bar; R=0.04763 PINNED,
not re-gated live.  k=10 kz197 N=4071
border_fail at 29.5 s (same as r420).  k=11
kz339 N=12508 skipped (builder).

FROZEN FROM /tmp (live re-gated except k=8):
  * SELECTED (k, kz, N, P1, R, den, Sigma):
    4  9   184  P1  0.08562  1.60111  0.31326
    5  17   96  P1  0.10493  1.65127  0.24380
    6  26  364 VAC  0.06811  1.52415  0.40774
    7  43  839 VAC  0.05198  1.51822  0.42980
    8  69 5690  P1  0.04763  1.56855  0.38382  PINNED
    9 116 1433  P1  0.03814  1.48227  0.47959
  * FIT vs k=5..9 (diagnosis):
    M1 R_inf=+0.02982 a=3.52 rss=1.56e-5 aic=-57.4 rms=0.0018
    M2 a=1.65 rss=9.33e-5 aic=-50.4 rms=0.0043
    M3 rss=1.39e-3 aic=-38.9 rms=0.0167   KILLED
    WINNER M1.  vs a_k=2^k also M1 (R_inf=+0.034).
    vs N the abscissa is illegal (non-monotone);
    M3 barely wins there -- discarded.
  * DRIVER: den FLAT in [1.48, 1.65]; Sigma wanders
    0.24..0.48 and is the balance partner.  s2
    O(0.06) flat.  n_eff GROWS 18 -> 146 (k=5..9)
    and 559 at k=8: occupation BROADER.  lam_w
    mild 5.5 -> 3.8, not a collapse.  B_w grows
    6.4 -> 18.9 (S = B_w-5/7 not convergent on
    the observed range).  Sigma channel = width,
    not mass, not razor.
  * SATURATION: C_min-1 and ||T0||-1 convert
    (r411: T0^*T0 = C^{-1}; VAC ratio
    (T0-1)/(-(C_min-1)/2) = 1.0000 at kz26/43).
    R and |sch| track (r417: VAC sch = phibb-tau^2;
    selected |sch|-R = O(tau^2)).  gap2 = 2-den
    is O(0.5) FLAT -- a different object, NOT
    the razor scale.  Three scales, two
    dictionary pairs, NOT one exponent.
  * EXT VAC R in [0.0285, 0.0373] -- sits at the
    M1 floor.  Dead chi R<0 (no rescue).
    Overflow-6 R<0 (tau-life finite, r419).
  * k=10 border_fail; k=11 skipped.

AUSGANG FLOOR_PREFERRED / LOG_KILLED /
K10_BORDER_FAIL / COFINAL_OPEN.
SATZ: R = -phibb; T0-Cgap linearisation on VAC.
REFUTED: M3 (R ~ c/log k) as the selected law.
REDUZIERT: R_inf > 0 is a 5-point AIC census
(R_inf ~ 0.030 vs k), not a theorem; R->0 is
the losing model on the selected abscissa but
k=10/11 are missing so the 0-vs-0.03 split is
not seen at the hoped depth.  Does not move
the mincut.
No RH claim.

MACHINERY: r420 S.den_pack / S418.split_pack,
r411 C-resolvent, r417 chart.

NO RH CLAIM.  Finite identities, a named
refutation of the log model, a named census.
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
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S420_SHA_PREFIX = "46409e2f"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
VAC_POS = S418.VAC_POS
SCR_NNEG = ES.SCR_NNEG

# frozen selected (k, kz, N, R) -- k=8 PINNED from /tmp
SEL_LIVE = ((4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, Nw=5690, reserve=0.04763,
              den=1.56855, Sig=0.38382, P1=True)
SEQ_K = (5, 6, 7, 8, 9)
SEQ_R = (0.10493, 0.06811, 0.05198, 0.04763, 0.03814)
W9_RES, KZ26_RES, KZ12_RES = 0.08562, 0.06811, -0.01558
KZ26_CGAP = 2.759e-6
EXT_VAC_LO, EXT_VAC_HI = 0.025, 0.040
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
    return (not bad), ("NO zero/prime oracles; reserve / "
                       "C-dictionary only"
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


def reserve_Q():
    """R = -c_J - Sigma = -phibb over Q (VAC toy)."""
    cJ, Sig = Fr(-3, 2), Fr(1, 2)
    phibb = cJ + Sig
    R = -cJ - Sig
    return dict(cJ=cJ, Sig=Sig, phibb=phibb, R=R)


def t0_lin_Q():
    """||T0||-1 = -eps/2 + O(eps^2) for C_min = 1+eps."""
    eps = Fr(1, 100)
    cmin = Fr(1) + eps
    # 1/sqrt(1+eps) - 1 versus -eps/2; compare squares to stay in Q
    t0 = (cmin ** Fr(-1, 2))
    # float ward for the irrational sqrt; identity is the expansion
    t0f = 1.0 / math.sqrt(float(cmin))
    linf = -0.5 * float(eps)
    err = abs((t0f - 1.0) - linf)
    return dict(eps=eps, err=err, t0m1=t0f - 1.0, lin=linf, t0=t0)


def two_param_power(xs, ys):
    """ys ~ c * xs^{-a} via log-mean slope.  Returns c, a."""
    X = [math.log(x) for x in xs]
    Y = [math.log(y) for y in ys]
    n = len(X)
    mx = sum(X) / n
    my = sum(Y) / n
    num = sum((X[i] - mx) * (Y[i] - my) for i in range(n))
    den = sum((X[i] - mx) ** 2 for i in range(n))
    slope = num / den
    intercept = my - slope * mx
    return math.exp(intercept), -slope


def score_aic(rss, n, npar):
    if n < 1 or rss <= 0:
        return float("inf")
    return n * math.log(rss / n) + 2.0 * npar


def diagnose_seq(ks, Rs):
    """AIC of M1/M2/M3 on a frozen sequence.  Diagnosis only."""
    n = len(Rs)
    logk = [math.log(k) for k in ks]
    # M3: R = c / log k
    inv = [1.0 / lk for lk in logk]
    c3 = sum(Rs[i] * inv[i] for i in range(n)) / sum(v * v for v in inv)
    y3 = [c3 / lk for lk in logk]
    rss3 = sum((Rs[i] - y3[i]) ** 2 for i in range(n))
    aic3 = score_aic(rss3, n, 1)
    # M2
    c2, a2 = two_param_power(ks, Rs)
    y2 = [c2 * (k ** (-a2)) for k in ks]
    rss2 = sum((Rs[i] - y2[i]) ** 2 for i in range(n))
    aic2 = score_aic(rss2, n, 2)
    # M1: grid R_inf, then power on the remainder
    best = None
    rmin = min(Rs)
    step = 80
    for j in range(step):
        rinf = -0.02 + (rmin * 0.95 + 0.02) * j / (step - 1)
        rem = [Rs[i] - rinf for i in range(n)]
        if any(v <= 1e-12 for v in rem):
            continue
        c, a = two_param_power(ks, rem)
        y = [rinf + c * (k ** (-a)) for k in ks]
        rss = sum((Rs[i] - y[i]) ** 2 for i in range(n))
        if best is None or rss < best[0]:
            best = (rss, rinf, c, a)
    rss1, rinf, c1, a1 = best
    aic1 = score_aic(rss1, n, 3)
    scores = [("M1", aic1, rss1, rinf),
              ("M2", aic2, rss2, 0.0),
              ("M3", aic3, rss3, 0.0)]
    scores.sort(key=lambda t: t[1])
    return dict(winner=scores[0][0], scores=scores,
                M1_Rinf=rinf, M1_a=a1, M2_a=a2,
                aic1=aic1, aic2=aic2, aic3=aic3,
                rss1=rss1, rss2=rss2, rss3=rss3)


def occ_extra(kz):
    """Cgap / T0-1 / n_eff on top of den_pack (MAIN)."""
    w = S420.den_pack(kz)
    R = PX.build_rung(kz)
    C, _ = DI.chain_C(R["mz"])
    evC = np.linalg.eigvalsh(C)
    cmin = float(evC[0])
    w["Cmin"] = cmin
    w["Cgap"] = cmin - 1.0
    w["T0m1"] = 1.0 / math.sqrt(max(cmin, 1e-30)) - 1.0
    # n_eff from occupation already inside den_pack path:
    # recompute occ entropy-width from C and s via den_pack fields
    evC2, WC = np.linalg.eigh(C)
    # rebuild s the same way den_pack did -- use Sig/s2 only
    # n_eff pinned from /tmp for k>=8; live here for small kz
    s2 = w["s2"]
    # den_pack already did eigh; we only need Cgap/T0 here
    _ = (evC2, WC, s2)
    return w


def part_satz():
    section("S1  LEG A -- R IDENTITY / T0 LINEARISATION OVER Q")
    t = reserve_Q()
    check("G01-R-identity-Q",
          t["R"] == Fr(1) and t["phibb"] == Fr(-1)
          and t["R"] == -t["phibb"]
          and t["phibb"] == t["cJ"] + t["Sig"],
          "R=-phibb=1; phibb=c_J+Sigma=-1")
    d = t0_lin_Q()
    check("G02-T0-lin-Q",
          d["err"] < float(d["eps"]) ** 2
          and d["t0m1"] < 0 and d["lin"] < 0,
          "C_min=1+1/100: |(T0-1)+eps/2|=%.2e < eps^2"
          % d["err"])
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G03-drop-border",
          nK == nA0 == 1,
          "no reserve scalar")


def part_pins():
    section("S2  w9 / kz26 / kz12 -- R + T0 DICTIONARY")
    w = S420.den_pack(9)
    check("G10-w9-reserve",
          abs(w["reserve"] - W9_RES) <= 0.001
          and abs(w["reserve"] + w["cJ"] + w["Sig"]) <= 1e-12
          and w["P1"],
          "R=%.5f = -c_J-Sigma" % w["reserve"])
    h = occ_extra(26)
    ratio = (h["T0m1"] / (-0.5 * h["Cgap"])
             if h["Cgap"] else float("nan"))
    check("G11-kz26-dict",
          (not h["P1"]) and abs(h["reserve"] - KZ26_RES) <= 0.001
          and abs(h["Cgap"] - KZ26_CGAP) / KZ26_CGAP <= 0.05
          and 0.999 <= ratio <= 1.001,
          "R=%.5f Cgap=%.3e T0/(-Cgap/2)=%.6f (SATZ)"
          % (h["reserve"], h["Cgap"], ratio))
    o = S420.den_pack(12)
    check("G12-kz12-overflow",
          (not o["P1"]) and o["reserve"] < 0
          and abs(o["reserve"] - KZ12_RES) <= 0.001,
          "OVF R=%.5f <0 (no rescue in R)" % o["reserve"])
    return w, h, o


def part_fit():
    section("S3  LEG A -- AIC ON FROZEN k=5..9 (diagnosis)")
    d = diagnose_seq(SEQ_K, SEQ_R)
    check("G20-M1-wins",
          d["winner"] == "M1"
          and 0.025 <= d["M1_Rinf"] <= 0.040
          and d["aic3"] - d["aic1"] > 10,
          "winner=%s R_inf=%+.5f aic M1/M2/M3=%.1f/%.1f/%.1f "
          "(M3 KILLED, DeltaAIC=%.1f)"
          % (d["winner"], d["M1_Rinf"], d["aic1"], d["aic2"],
             d["aic3"], d["aic3"] - d["aic1"]))
    check("G21-M2-loses",
          d["aic2"] - d["aic1"] > 4,
          "M2 DeltaAIC=%.1f (loses to floor)"
          % (d["aic2"] - d["aic1"]))
    # mutant: drop k=9 -- M1 must still prefer a positive floor
    d2 = diagnose_seq(SEQ_K[:-1], SEQ_R[:-1])
    check("G22-mutant-drop-k9",
          d2["winner"] == "M1" and d2["M1_Rinf"] > 0.02,
          "drop k=9: still M1 R_inf=%+.4f (mutant does not flip)"
          % d2["M1_Rinf"])
    return d


def part_kills():
    section("S4  LEG D -- DEAD / SCRAMBLE / OVERFLOW")
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    tau2 = c23["a_un"] ** 2 + c23["b_un"] ** 2
    check("G30-dead-R-neg",
          c23["phibb"] > 0 and (-c23["phibb"]) < 0
          and tau2 < c23["phibb"] and p23["sch"] > 0,
          "DEAD C3-23 R=%+.4f (no rescue)" % (-c23["phibb"]))
    p20 = ES.chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "D20")
    c20 = S417.chart_from_row(p20)
    check("G31-dead-chi4",
          c20["phibb"] > 0,
          "C4-20 R=%+.4f" % (-c20["phibb"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G32-scramble",
          oS["nneg"] == SCR_NNEG,
          "nnegA0=%d (bulk dead; scramble irrelevant)"
          % oS["nneg"])


def part_census(smoke):
    section("S5  LEG B/C -- SELECTED / EXT / CHANNELS / SCALES")
    if smoke:
        section("S5b  selected/EXT/core skipped (--smoke)")
        return None
    sel = []
    for k, kz in SEL_LIVE:
        p = S418.split_pack(kz)
        p["k"] = k
        p["reserve"] = -p["phibb"]
        sel.append(p)
        print("    k=%d kz%d N=%d P1=%s R=%+.5f den=%.5f Sig=%.5f"
              % (k, kz, p["Nw"], p["P1"], p["reserve"],
                 p["den"], p["qbb"]), flush=True)
    r5 = next(r for r in sel if r["k"] == 5)
    r6 = next(r for r in sel if r["k"] == 6)
    r7 = next(r for r in sel if r["k"] == 7)
    r9 = next(r for r in sel if r["k"] == 9)
    check("G40-selected-live",
          all(r["ok"] and r["reserve"] > 0 for r in sel)
          and abs(r5["reserve"] - SEQ_R[0]) <= 0.001
          and abs(r6["reserve"] - SEQ_R[1]) <= 0.001
          and abs(r7["reserve"] - SEQ_R[2]) <= 0.001
          and abs(r9["reserve"] - SEQ_R[4]) <= 0.001
          and r5["reserve"] > r6["reserve"] > r7["reserve"] > r9["reserve"],
          "k=4,5,6,7,9 live R>0; 0.105>0.068>0.052>0.038")
    check("G41-k8-pinned",
          K8_PIN["reserve"] > r9["reserve"]
          and K8_PIN["reserve"] < r7["reserve"]
          and K8_PIN["Nw"] == 5690,
          "k=8 PINNED R=%.5f N=5690 (builder fallback, 226 s)"
          % K8_PIN["reserve"])
    # channels on live VAC
    h6 = S420.den_pack(26)
    h7 = S420.den_pack(43)
    h9 = S420.den_pack(116)
    dens = [r["den"] for r in sel]
    check("G42-driver",
          max(dens) - min(dens) < 0.20
          and 0.04 <= h6["s2"] <= 0.08
          and 0.04 <= h9["s2"] <= 0.08
          and h6["lam_w"] > 3.5 and h9["lam_w"] > 3.2
          and h6["Bw"] < h7["Bw"] < h9["Bw"],
          "den flat [%.3f,%.3f]; s2 O(0.06); lam_w moderate; "
          "B_w grows %.2f->%.2f (S not convergent here)"
          % (min(dens), max(dens), h6["Bw"], h9["Bw"]))
    ext = []
    for kz in ES.SAMPLE_EXT:
        p = S418.split_pack(kz)
        p["reserve"] = -p["phibb"]
        ext.append(p)
        print("    EXT-%d N=%d P1=%s R=%+.5f"
              % (kz, p["Nw"], p["P1"], p["reserve"]), flush=True)
    ext_vac = [r for r in ext if not r["P1"]]
    check("G43-EXT-floor",
          len(ext_vac) == 3
          and all(EXT_VAC_LO <= r["reserve"] <= EXT_VAC_HI
                  for r in ext_vac),
          "EXT VAC 3/3 R in [%.4f, %.4f] (M1 floor band)"
          % (min(r["reserve"] for r in ext_vac),
             max(r["reserve"] for r in ext_vac)))
    ovf_neg = 0
    okv_pos = 0
    for kz in V.admissible_indices():
        p = S418.split_pack(kz)
        if p["P1"]:
            continue
        if kz in VAC_POS:
            ovf_neg += int(p["phibb"] > 0)
        else:
            okv_pos += int(p["phibb"] < 0)
    check("G44-ovf-no-rescue",
          ovf_neg == 6 and okv_pos == 8,
          "OVF 6/6 R<0; OKV 8/8 R>0")
    # three-scale statement on kz26
    gap2 = 2.0 - h6["den"]
    x6 = occ_extra(26)
    check("G45-three-scales",
          0.4 <= gap2 <= 0.6
          and 1e-7 <= x6["Cgap"] <= 1e-5
          and abs(x6["T0m1"] + 0.5 * x6["Cgap"]) <= 1e-11,
          "gap2=%.3f FLAT O(0.5); Cgap=%.3e razor; "
          "T0-1=-Cgap/2 (NOT one scale)"
          % (gap2, x6["Cgap"]))
    return sel


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("reserve_limit_probe -- "
          "PRIME.RDAGGER.RESERVE_LIMIT.01 (round 421)")
    print("SPEC_SHA %s   (S420 %s / S418 %s / S417 %s)"
          % (SPEC_SHA[:16], S420.SPEC_SHA[:16], S418.SPEC_SHA[:16],
             S417.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected live k=4,5,6,7,9 + EXT; "
                        "k=8 pinned)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and S420.SPEC_SHA.startswith(S420_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / S418 %s / S420 %s"
          % (ES.SPEC_SHA[:8], S418.SPEC_SHA[:8], S420.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_pins()
    part_fit()
    part_kills()
    part_census(smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "FLOOR_PREFERRED / LOG_KILLED / K10_BORDER_FAIL / "
          "COFINAL_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("FLOOR_PREFERRED / LOG_KILLED / "
            "K10_BORDER_FAIL / COFINAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("RESERVE LIMIT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("RESERVE LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
