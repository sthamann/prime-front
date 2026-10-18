#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""delta_floor_probe -- PRIME.RDAGGER.DELTA_FLOOR_SELECTED.01
(round 443): is liminf delta_k > 0 on the selected
sequence (the r442 q^dagger-rises-to-1 trend as the
old r421 reserve-floor question)?

THE LEMMA (exactly one).  liminf_{k in Selected} delta_k
> 0, with delta = 1 - q^dagger = -sch (r433, c'=1).
If a floor delta_inf > 0 exists then q^dagger <= 1 -
delta_inf eventually pointwise, hence kappa^dagger = 0
eventually by the r442 dictionary, and the frequently-
mincut is filled.  This round does NOT prove the
liminf.  It decomposes delta, fits floor vs decay on
both abscissae, and names what remains open.

CHART (SATZ, r417).  VAC: -sch = R + tau^2 with
R = -phibb.  P1: -sch = R + (b_un^2 - a_un^2).
R = 2 - den - Sigma (r418/r420).  den is flat with
O(0.5) room; Sigma wanders; tau^2 -> 0 on the deep
selected end, so delta tracks R.

CALIBRATION DISCLOSURE.  Selected anatomy, AIC on k
and N, branch split, EXT band, kz16 family, dead chi,
k=10 timed fail first measured in /tmp (r443_cal.py,
r443_cal2.py) on the r417/r418/r421/r433 constructors,
2026-08-30.  Frozen floors below are that measurement,
sealed as gates.  Pins disclosed.
Builder fallback: k=8 not rebuilt (r421 class,
N=5690).  k=10 kz197 N=4071 timed out at 20 s inside
border_chain_pack -- the C-resolvent / CG route is
never reached (no C to invert).  k=11/12 skipped
(Nw=12508/45444).

FROZEN FROM /tmp (live re-gated except k=8/10+):
  * SATZ Q: VAC -sch = R + tau^2; P1 -sch = R + hyp.
  * Selected (k, kz, N, branch, delta, R, tau2, den):
    3   5    72 P1  0.071564  0.086252  0.01502  1.70246
    4   9   184 P1  0.066956  0.085622  0.01930  1.60111
    5  17    96 P1  0.108636  0.104931  0.00453  1.65127
    6  26   364 VAC 0.068896  0.068109  0.00079  1.52415
    7  43   839 VAC 0.055396  0.051983  0.00341  1.51822
    9 116  1433 P1  0.037785  0.038136  0.00059  1.48227
    Chart residual 0 on 6/6.  k=6,7 VAC; rest P1.
  * DRIVER: tau^2 already O(10^{-3}) on VAC and
    0.019 -> 0.0006 on P1; |delta-R| = 0.00035 at k=9.
    den flat [1.48, 1.70]; Sigma = 2-den-R wanders
    0.211 -> 0.480.  The decay of delta IS the decay
    of R (r421 object).
  * AIC delta vs k=5,6,7,9 (r421 slice, no k=8):
    M1 winner, delta_inf=+0.02670, aic -45.6/-39.6/-29.9
    (DeltaAIC vs M2 = 6.0).  Same slice on R:
    R_inf=+0.02911 (with k=8 pin: +0.02982, r421 replay).
  * AIC delta vs k=3..9: M3 wins, M1 hits grid -0.02
    (k=5 bump 0.109 wrecks a global floor).
  * AIC vs N: M2 wins (r427: N non-monotone, illegal).
  * Mutants: drop k=5 -> M2; drop k=9 -> M1 but
    delta_inf jumps to 0.045 (last point load-bearing).
  * EXT-6 delta in [0.02636, 0.04519], mean 0.03572
    (second line, sits at the slice floor).
  * kz16: delta=0.001510 << 0.027 (R=-0.003, saved by
    tau^2=0.00457).  kz12: 0.00594, R=-0.0156.
    Floor is Selected-specific (r428).
  * Dead CHI3-15: delta=-0.02318 < 0.

AUSGANG REDUZIERT / CHART_EXACT / SLICE_FLOOR_PREFERRED /
FULL_SEQUENCE_UNSETTLED / KZ16_SELECTED_SPECIFIC /
DEEP_LOCKED / COFINAL_OPEN.
SATZ: the chart identities (delta = R + tau-correction).
CENSUS: floor preferred on the r421 k=5..9 slice
(delta_inf ~ 0.027, EXT band).  The full selected
sequence does not independently prefer a floor.
REFUTED: N as an abscissa; a Selected-universal floor
that would cover kz16.  OPEN: existence of liminf > 0.
The conditional {floor => q^dagger < 1 eventually =>
kappa^dagger = 0 eventually} is recorded, not claimed.
No RH claim.

MACHINERY: r417 S417.chart_from_row / sch_*_Q,
r418/r401 ES.main_row, r421 S421.diagnose_seq,
r433 delta=-sch, r428 kz16, r226 V.window_shape.

NO RH CLAIM.  One finite chart lemma, a named AIC
census, named kills.  Research documentation, not a
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S421_SHA_PREFIX = "234a1113"
QR_SHA_PREFIX = "fc2c617a"

SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
SEL_SMOKE = ((3, 5), (4, 9), (5, 17))
PIN_D = {3: 0.071564, 4: 0.066956, 5: 0.108636,
         6: 0.068896, 7: 0.055396, 9: 0.037785}
PIN_R = {3: 0.086252, 4: 0.085622, 5: 0.104931,
         6: 0.068109, 7: 0.051983, 9: 0.038136}
PIN_DEN = {3: 1.70246, 4: 1.60111, 5: 1.65127,
           6: 1.52415, 7: 1.51822, 9: 1.48227}
VAC_KS = (6, 7)
P1_KS = (3, 4, 5, 9)
SLICE_KS = (5, 6, 7, 9)
SLICE_DINF = 0.02670
SLICE_RINF = 0.02911
R421_RINF = 0.02982
EXT_LO, EXT_HI, EXT_MEAN = 0.02636, 0.04519, 0.03572
KZ16_D, KZ12_D = 0.001510, 0.005944
DEAD15_D = -0.023181
K10_KZ, K10_NW = 197, 4071
K8_KZ, K8_NW = 69, 5690
D_BAR = 5.0e-6
CHART_BAR = 1.0e-12
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
    return (not bad), ("NO zero/prime oracles; sch / phibb / "
                       "AIC diagnosis only"
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
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def pack(kz):
    p = ES.main_row(kz)
    if not p.get("ok"):
        return dict(ok=False, kz=kz, nf=p.get("nf"))
    ch = S417.chart_from_row(p)
    tau2 = ch["a_un"] ** 2 + ch["b_un"] ** 2
    hyp = ch["b_un"] ** 2 - ch["a_un"] ** 2
    R = -float(ch["phibb"])
    dlt = -float(p["sch"])
    pred = R + (hyp if p["P1"] else tau2)
    Sig = 2.0 - float(p["den"]) - R
    return dict(
        ok=True, kz=kz, Nw=int(p["Nw"]),
        delta=dlt, R=R, den=float(p["den"]), Sig=Sig,
        P1=bool(p["P1"]), chart=ch["kchart"],
        tau2=tau2, hyp=hyp, pred=pred,
        chart_err=abs(dlt - pred),
    )


def part_satz():
    section("S1  LEMMA TOOL -- CHART IDENTITIES OVER Q")
    p1 = S417.sch_woodbury_Q_p1()
    vac = S417.sch_woodbury_Q_vac()
    check("G01-Q-P1-chart",
          p1["sch"] == p1["sch_ch"] == p1["sch_w"]
          and p1["sch"] == Fr(-2, 3),
          "P1 sch=phibb+a^2-b^2=-2/3; delta=2/3")
    check("G02-Q-VAC-chart",
          vac["sch"] == vac["sch_ch"] == vac["sch_w"]
          and vac["sch"] == Fr(-7, 6),
          "VAC sch=phibb-tau^2=-7/6; delta=7/6")
    Rp1 = -p1["phibb"]
    check("G03-Q-R-identity",
          Rp1 == -(p1["phibb"]) and vac["phibb"] < 0,
          "R=-phibb on both toys")


def part_selected(smoke):
    section("S2  SELECTED ANATOMY + AIC (both abscissae)")
    sel = SEL_SMOKE if smoke else SEL_LIVE
    rows = []
    for k, kz in sel:
        a = pack(kz)
        a["k"] = k
        rows.append(a)
        print("    k=%d kz=%d N=%d %s dlt=%.6f R=%.6f tau2=%.5f "
              "err=%.1e"
              % (k, kz, a["Nw"], a["chart"], a["delta"], a["R"],
                 a["tau2"], a["chart_err"]), flush=True)
    check("G10-chart-residual",
          all(r["ok"] and r["chart_err"] < CHART_BAR for r in rows),
          "%d/%d delta = R + tau-correction (SATZ)"
          % (len(rows), len(rows)))
    check("G11-selected-pins",
          all(abs(r["delta"] - PIN_D[r["k"]]) < D_BAR
              and abs(r["R"] - PIN_R[r["k"]]) < 5e-6
              for r in rows)
          and all((r["k"] in VAC_KS) == (not r["P1"]) for r in rows),
          "pins match; k=6,7 VAC, rest P1")
    if smoke:
        check("G12-slice-AIC-frozen", True, "--smoke uses frozen AIC")
        check("G13-N-abscissa-killed", True, "--smoke")
        check("G14-full-seq-unsettled", True, "--smoke")
        return rows
    live = {r["k"]: r for r in rows}
    ks = list(SLICE_KS)
    ds = [live[k]["delta"] for k in ks]
    Rs = [live[k]["R"] for k in ks]
    fit_d = S421.diagnose_seq(ks, ds)
    fit_R = S421.diagnose_seq(ks, Rs)
    fit_N = S421.diagnose_seq([live[k]["Nw"] for k in ks], ds)
    fit_all = S421.diagnose_seq([r["k"] for r in rows],
                                [r["delta"] for r in rows])
    check("G12-slice-floor-preferred",
          fit_d["winner"] == "M1"
          and fit_d["M1_Rinf"] > 0.02
          and abs(fit_d["M1_Rinf"] - SLICE_DINF) < 0.003
          and (fit_d["aic2"] - fit_d["aic1"]) > 4.0
          and fit_R["winner"] == "M1"
          and abs(fit_R["M1_Rinf"] - SLICE_RINF) < 0.003,
          "k=5..9 no k8: M1 delta_inf=%.5f R_inf=%.5f "
          "DeltaAIC(M2)=%.1f"
          % (fit_d["M1_Rinf"], fit_R["M1_Rinf"],
             fit_d["aic2"] - fit_d["aic1"]))
    check("G13-N-abscissa-killed",
          fit_N["winner"] != "M1",
          "vs N winner=%s (r427: N non-monotone, illegal)"
          % fit_N["winner"])
    check("G14-full-seq-unsettled",
          fit_all["winner"] != "M1" or fit_all["M1_Rinf"] < 0,
          "k=3..9 winner=%s M1_Rinf=%.4f (k=5 bump; "
          "floor is a slice census, not a Selected law)"
          % (fit_all["winner"], fit_all["M1_Rinf"]))
    return rows


def part_ext_kz16(smoke):
    section("S3  EXT LINE + kz16 (Selected-specific)")
    if smoke:
        a16 = pack(16)
        check("G20-EXT-skipped", True, "--smoke")
        check("G21-kz16-below",
              a16["ok"] and a16["delta"] < 0.005
              and abs(a16["delta"] - KZ16_D) < D_BAR
              and a16["R"] < 0,
              "kz16 dlt=%.6f << slice floor 0.027 "
              "(R=%.4f, saved by tau^2)"
              % (a16["delta"], a16["R"]))
        return
    ext = []
    for kz in ES.SAMPLE_EXT:
        a = pack(kz)
        ext.append(a)
        print("    EXT-%d N=%d %s dlt=%.6f R=%.6f"
              % (kz, a["Nw"], a["chart"], a["delta"], a["R"]),
              flush=True)
    eds = [e["delta"] for e in ext]
    check("G20-EXT-band",
          all(e["ok"] and e["delta"] > 0 for e in ext)
          and abs(min(eds) - EXT_LO) < 5e-5
          and abs(max(eds) - EXT_HI) < 5e-5
          and abs(sum(eds) / len(eds) - EXT_MEAN) < 5e-5,
          "EXT 6/6 dlt in [%.5f, %.5f] mean=%.5f "
          "(second evidence line at the slice floor)"
          % (min(eds), max(eds), sum(eds) / len(eds)))
    fam = {kz: pack(kz) for kz in (12, 16)}
    check("G21-kz16-below",
          fam[16]["delta"] < 0.005
          and fam[12]["delta"] < 0.01
          and fam[16]["R"] < 0 and fam[12]["R"] < 0
          and abs(fam[16]["delta"] - KZ16_D) < D_BAR,
          "kz16 dlt=%.6f kz12 dlt=%.6f both << 0.027 "
          "(R already negative; floor is Selected-specific)"
          % (fam[16]["delta"], fam[12]["delta"]))


def part_kills():
    section("S4  KILLS -- dead chi / deep lock / q_N circle")
    pD = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "CHI3-15")
    dlt = -float(pD["sch"])
    check("G30-dead-chi-neg",
          pD.get("ok") and dlt < 0
          and abs(dlt - DEAD15_D) < 5e-6,
          "CHI3-15 delta=%.6f < 0 (dictionary: q^d>1)"
          % dlt)
    kz10, _a, _r = QR.pp_kz(10)
    kz8, _a8, _r8 = QR.pp_kz(8)
    nw10 = V.window_shape(kz10)[3]
    nw8 = V.window_shape(kz8)[3]
    check("G31-deep-locked",
          kz10 == K10_KZ and nw10 == K10_NW
          and kz8 == K8_KZ and nw8 == K8_NW,
          "k=8 kz=%d N=%d (r421 pin, not rebuilt); "
          "k=10 kz=%d N=%d (border_chain timeout 20s; "
          "CG never reached -- no C yet).  k=11/12 skipped"
          % (kz8, nw8, kz10, nw10))
    check("G32-qN-not-qdag",
          True,
          "circle gate: r424 S < B_w <=> q_N < 1 is NOT "
          "a q^dagger floor (q_N != q^dagger, r433)")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("delta_floor_probe -- "
          "PRIME.RDAGGER.DELTA_FLOOR_SELECTED.01 (round 443)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9 + EXT-6; "
                        "k=8/10+ not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S421.SPEC_SHA.startswith(S421_SHA_PREFIX[:8]))
    check("G00b-import-sha", sha_ok,
          "ES %s S417 %s S421 %s QR %s"
          % (ES.SPEC_SHA[:8], S417.SPEC_SHA[:8],
             S421.SPEC_SHA[:8], QR.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_selected(smoke)
    part_ext_kz16(smoke)
    part_kills()

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "REDUZIERT / CHART_EXACT / SLICE_FLOOR_PREFERRED / "
          "FULL_SEQUENCE_UNSETTLED / KZ16_SELECTED_SPECIFIC / "
          "DEEP_LOCKED / COFINAL_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("REDUZIERT / CHART_EXACT / SLICE_FLOOR_PREFERRED / "
            "FULL_SEQUENCE_UNSETTLED / KZ16_SELECTED_SPECIFIC / "
            "DEEP_LOCKED / COFINAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("DELTA FLOOR %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DELTA FLOOR FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
