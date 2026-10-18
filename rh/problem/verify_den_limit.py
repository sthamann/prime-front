#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_den_limit.py -- machine check of every numbered
lemma in rh/problem/den_limit.tex (round 423,
FORMULA_EXACT / GAMMA_LT1_CENSUS / LIMIT_OPEN /
SUBSUM_REFUTED).

PART A (STANDALONE OVER Q):
  G1  den = 1+gam-vts = 3/2
  G2  gam<1 => 1+gam<2 even at vts=0
  G3  drop-border

PART B (CONSTRUCTION PINS):
  G10 w9 formula; drop-5/7 still gam<1
  G11 w9 ||b||^2 is not a subsum of S
  G12 kz26 gam<1 vts>0
  G13 dead den<2; scramble

Exit: "DEN LIMIT VERIFIED" iff every gate passed.
NO RH CLAIM.
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

import den_limit_probe as S  # noqa: E402
import cj_sigma_probe as S420  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402

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
    section("PART A  den FORMULA / gam<1 / DROP-BORDER")
    t = S.den_Q()
    check("G1-den-Q",
          t["den"] == Fr(3, 2) and t["gam"] < Fr(1),
          "den=%s" % t["den"])
    check("G2-drop-vts",
          Fr(1) + t["gam"] < Fr(2),
          "1+gam<2")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G3-drop-border", nK == nA0 == 1, "nneg=%d" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.den_rich(9)
    check("G10-w9",
          abs(w["den"] - S.W9_DEN) <= 0.001
          and w["gam"] < 1 and w["gam_no57"] < 1,
          "den=%.5f no57=%.4f" % (w["den"], w["gam_no57"]))
    check("G11-not-subsum",
          w["pref_ratio"] > w["end_ratio"]
          and w["end_ratio"] < 0.80,
          "b2/S %.3f -> %.3f" % (w["pref_ratio"], w["end_ratio"]))
    h = S420.den_pack(26)
    check("G12-kz26",
          h["gam"] < 1 and h["vts"] > 0 and (not h["P1"]),
          "gam=%.4f" % h["gam"])
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G13-dead-scramble",
          float(p23["den"]) < 2 and c23["phibb"] > 0
          and oS["nneg"] == S.SCR_NNEG,
          "dead den=%.4f scr nneg=%d" % (float(p23["den"]), oS["nneg"]))


def main():
    print("=" * 72)
    print("verify_den_limit.py -- round 423")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("DEN LIMIT VERIFIED")
        return 0
    print("DEN LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
