#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_sigma_limit.py -- machine check of every numbered
lemma in rh/problem/sigma_limit.tex (round 422,
STIELTJES_EXACT / DENSITY_REFUTED / NEAR1_STABLE /
LIMITS_OPEN).

PART A (STANDALONE OVER Q):
  G1  Sigma = 2 s2 + 4 m(1) = 2 sum occ g
  G2  g=1 (no pole) fails
  G3  drop-border

PART B (CONSTRUCTION PINS):
  G10 w9 Stieltjes identity
  G11 kz26 near-1 stable; pole density refuted
  G12 kz12 overflow has more near-1 mass
  G13 dead razor; scramble

Exit: "SIGMA LIMIT VERIFIED" iff every gate passed.
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

import sigma_limit_probe as S  # noqa: E402
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
    section("PART A  STIELTJES / NO-FLAT-G / DROP-BORDER")
    t = S.sigma_Q()
    check("G1-Stieltjes-Q",
          t["Sig_st"] == t["Sig_occ"] == Fr(28, 3),
          "Sig=%s" % t["Sig_st"])
    check("G2-no-flat-g",
          Fr(2) * t["s2"] != t["Sig_st"],
          "g=1 loses")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G3-drop-border", nK == nA0 == 1, "nneg=%d" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.occ_spec(9)
    check("G10-w9",
          w["dSt"] < 1e-10 and abs(w["Sig"] - S.W9_SIG) <= 0.001,
          "Sig=%.5f dSt=%.1e" % (w["Sig"], w["dSt"]))
    h = S.occ_spec(26)
    check("G11-kz26",
          h["near"][0.10] < 0.02 and h["pole_rel"] > 0.5
          and (not h["P1"]),
          "near01=%.4f pole-rel=%.2f" % (h["near"][0.10],
                                         h["pole_rel"]))
    o = S.occ_spec(12)
    check("G12-kz12",
          o["near"][0.10] > h["near"][0.10] and o["Sig"] > -o["cJ"],
          "OVF near01=%.4f" % o["near"][0.10])
    uu, ww, _nn, _ch = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d = S.occ_spec(23, mz=mzc, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G13-dead-scramble",
          d["razor"] >= S.DEAD_RAZOR_LO and c23["phibb"] > 0
          and oS["nneg"] == S.SCR_NNEG,
          "dead razor=%.2e scr nneg=%d" % (d["razor"], oS["nneg"]))


def main():
    print("=" * 72)
    print("verify_sigma_limit.py -- round 422")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("SIGMA LIMIT VERIFIED")
        return 0
    print("SIGMA LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
