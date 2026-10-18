#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_reserve_limit.py -- machine check of every numbered
lemma in rh/problem/reserve_limit.tex (round 421,
FLOOR_PREFERRED / LOG_KILLED / K10_BORDER_FAIL /
COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  R = -phibb = -c_J - Sigma
  G2  T0 linearisation
  G3  drop-border

PART B (CONSTRUCTION PINS):
  G10 w9 R identity
  G11 kz26 T0-Cgap dictionary
  G12 kz12 overflow R<0
  G13 AIC: M1 wins, M3 killed
  G14 dead VAC R<0; scramble

Exit: "RESERVE LIMIT VERIFIED" iff every gate passed.
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

import reserve_limit_probe as S  # noqa: E402
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
    section("PART A  R IDENTITY / T0 LIN / DROP-BORDER")
    t = S.reserve_Q()
    check("G1-R-identity-Q",
          t["R"] == Fr(1) and t["R"] == -t["phibb"],
          "R=%s" % t["R"])
    d = S.t0_lin_Q()
    check("G2-T0-lin",
          d["err"] < float(d["eps"]) ** 2,
          "err=%.2e" % d["err"])
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G3-drop-border", nK == nA0 == 1, "nneg=%d" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S420.den_pack(9)
    check("G10-w9",
          abs(w["reserve"] - S.W9_RES) <= 0.001
          and abs(w["reserve"] + w["cJ"] + w["Sig"]) <= 1e-12,
          "R=%.5f" % w["reserve"])
    h = S.occ_extra(26)
    ratio = h["T0m1"] / (-0.5 * h["Cgap"])
    check("G11-kz26-dict",
          h["reserve"] > 0 and 0.999 <= ratio <= 1.001
          and (not h["P1"]),
          "R=%.5f ratio=%.6f" % (h["reserve"], ratio))
    o = S420.den_pack(12)
    check("G12-kz12",
          o["reserve"] < 0 and (not o["P1"]),
          "R=%.5f" % o["reserve"])
    d = S.diagnose_seq(S.SEQ_K, S.SEQ_R)
    check("G13-aic",
          d["winner"] == "M1" and d["aic3"] - d["aic1"] > 10
          and 0.025 <= d["M1_Rinf"] <= 0.040,
          "M1 R_inf=%+.4f; M3 killed" % d["M1_Rinf"])
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G14-dead-scramble",
          c23["phibb"] > 0 and oS["nneg"] == S.SCR_NNEG,
          "dead R=%+.4f scr nneg=%d" % (-c23["phibb"], oS["nneg"]))


def main():
    print("=" * 72)
    print("verify_reserve_limit.py -- round 421")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("RESERVE LIMIT VERIFIED")
        return 0
    print("RESERVE LIMIT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
