#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_vacuous_overflow.py -- machine check of every
numbered lemma in rh/problem/vacuous_overflow.tex
(round 419, H3_REFUTED / RAZOR_POLE_REFUTED /
TAU_SAVE_FINITE / COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  VAC chart sch = phibb - tau2 = -3/20
  G2  drop-tau mutant: sch = phibb > 0
  G3  drop-border: no sch scalar

PART B (CONSTRUCTION PINS):
  G10 kz12 overflow: phibb>0, tau2>phibb, sch<0
  G11 kz26 healthy: phibb<0; razor share tiny
  G12 dead chi3-23: tau2<phibb, sch>0
  G13 scramble nnegA0=21; two-period >=4
  G14 CORE: 6 OVF tau-saved; H3 VAC grows;
      EXT VAC 3/6 phibb<0  (8 gates)

Exit: per-gate PASS/FAIL and the final line
"VACUOUS OVERFLOW VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, named refutations.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import vacuous_overflow_probe as S  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def part_a():
    section("PART A  VAC CHART / DROP-TAU / DROP-BORDER")
    t = S.sch_vac_Q()
    check("G1-VAC-Q",
          t["sch"] == Fr(-3, 20) and t["phibb"] == Fr(1, 10),
          "sch=%s" % t["sch"])
    check("G2-drop-tau-Q",
          t["sch_drop"] > 0,
          "sch_drop=%s" % t["sch_drop"])
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G3-drop-border",
          nK == nA0 == 1,
          "nneg K2=%d == nneg A0" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    r12 = S.decorate(12)
    check("G10-kz12",
          r12["phibb"] > 0 and r12["sch"] < 0
          and r12["tau2"] > r12["phibb"]
          and abs(r12["phibb"] - S.KZ12_PHIBB) <= 0.001
          and (not r12["P1"]),
          "phibb=%+.5f sch=%+.5f tau2=%.5f" % (
              r12["phibb"], r12["sch"], r12["tau2"]))
    r26 = S.decorate(26)
    z12 = S.razor_share(12)
    check("G11-kz26-razor",
          r26["phibb"] < 0 and (not r26["P1"])
          and z12["share"] <= S.RAZOR_SHARE_HI,
          "kz26 phibb=%+.5f; kz12 razor share=%.4f" % (
              r26["phibb"], z12["share"]))
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    tau2 = c23["a_un"] ** 2 + c23["b_un"] ** 2
    check("G12-dead-vac",
          p23["sch"] > 0 and c23["phibb"] > 0
          and tau2 < c23["phibb"] and p23["nnegA0"] == 0,
          "phibb=%+.4f tau2=%.4f sch=%+.4f" % (
              c23["phibb"], tau2, p23["sch"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G13-scramble-two-period",
          oS["nneg"] == S.SCR_NNEG and oT["nneg"] >= S.TP21_NNEG,
          "scr nneg=%d two-period nneg=%d" % (oS["nneg"], oT["nneg"]))
    core = list(V.admissible_indices())
    n_ovf = n_okv = n_vac_hi = 0
    byN = []
    for kz in core:
        r = S.decorate(kz)
        byN.append(r)
        if (not r["P1"]) and r["phibb"] > 0 and r["sch"] < 0:
            n_ovf += 1
        if (not r["P1"]) and r["phibb"] < 0:
            n_okv += 1
    byN.sort(key=lambda r: r["Nw"])
    hi = byN[2 * len(byN) // 3:]
    n_vac_hi = sum(1 for r in hi if not r["P1"])
    ext_vac_neg = 0
    for kz in ES.SAMPLE_EXT:
        r = S.decorate(kz)
        if (not r["P1"]) and r["phibb"] < 0:
            ext_vac_neg += 1
    check("G14-census",
          n_ovf == S.OVF_N and n_okv == S.OKV_N
          and n_vac_hi >= 6 and ext_vac_neg == 3,
          "OVF %d OKV %d; HI-tercile VAC %d; EXT VAC healthy %d"
          % (n_ovf, n_okv, n_vac_hi, ext_vac_neg))


def main():
    print("=" * 72)
    print("verify_vacuous_overflow.py -- round 419")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("VACUOUS OVERFLOW VERIFIED")
        return 0
    print("VACUOUS OVERFLOW FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
