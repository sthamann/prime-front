#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_source_sch.py -- machine check of every numbered
lemma in rh/problem/source_sch_sign.tex (round 417,
CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN).

PART A (STANDALONE OVER Q):
  G1  P1 toy Woodbury = chart = -2/3
  G2  VAC toy Woodbury = chart = -7/6
  G3  VAC phibb<0: whole disk sch<0
  G4  P1 hyperbola is not the whole disk
  G5  drop-border: nneg K2 = nneg A0 (no sch scalar)

PART B (CONSTRUCTION PINS):
  G10 w9 Woodbury/chart residual 0; pins
  G11 w9 pivot product <0 and detK<0
  G12 dead chi3-15 sch>0, dist small, disk escape;
      detK<0 still
  G13 scramble nnegA0=21; two-period >=4
  G14 MAIN-42 sch<0; EXT-119 |t|~0.075; dead geometry

Exit: per-gate PASS/FAIL and the final line
"SOURCE SCH SIGN VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, a named census, an open rate.
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

import source_sch_sign_probe as S  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
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
    section("PART A  WOODBURY / CHART / SIGN MAP / MUTANT")
    t1 = S.sch_woodbury_Q_p1()
    check("G1-P1-Q",
          t1["sch"] == t1["sch_w"] == t1["sch_ch"] == Fr(-2, 3),
          "sch=%s" % t1["sch"])
    t0 = S.sch_woodbury_Q_vac()
    check("G2-VAC-Q",
          t0["sch"] == t0["sch_w"] == t0["sch_ch"] == Fr(-7, 6),
          "sch=%s" % t0["sch"])
    n1, t1n, _g = S.grid_sign(-0.05, 0.40, "VAC")
    check("G3-VAC-whole-disk",
          n1 == t1n and t1n >= 1000,
          "%d/%d" % (n1, t1n))
    n2, t2n, _g = S.grid_sign(-0.05, 0.40, "P1")
    frac = n2 / float(t2n)
    check("G4-P1-hyperbola",
          S.P1_GRID_LO <= frac <= S.P1_GRID_HI,
          "frac=%.3f" % frac)
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G5-drop-border",
          nK == nA0 == 1,
          "nneg K2=%d == nneg A0" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    p, ch, sch_w, sch_ch, _den = S.woodbury_w9()
    check("G10-w9-identity",
          abs(sch_w - p["sch"]) <= 1e-12
          and abs(sch_ch - p["sch"]) <= 1e-12
          and abs(p["sch"] / S.W9_SCH - 1.0) <= 0.02
          and ch["kchart"] == "P1",
          "sch=%.5f dsch_w=%.1e" % (p["sch"], abs(sch_w - p["sch"])))
    check("G11-w9-pivot",
          p["detK"] < 0 and p["sch"] < 0 and p["nnegA0"] == 1,
          "detK=%+.3f sch<0" % p["detK"])
    p15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    c15 = S.chart_from_row(p15)
    check("G12-dead-chi",
          p15["sch"] > 0 and (not p15["shift"])
          and c15["dist"] <= S.DIST_DEAD_MED_HI
          and p15["ab"] > ES.K_RADIUS and p15["detK"] < 0,
          "sch=%+.4f dist=%.3f |t|=%.2f" % (
              p15["sch"], c15["dist"], p15["ab"]))
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
    n_neg = 0
    for kz in core:
        r = ES.main_row(kz)
        n_neg += int(r.get("ok") and r["sch"] < 0)
    p119 = ES.main_row(119)
    check("G14-census",
          n_neg == S.CORE_N
          and p119["ok"] and p119["sch"] < 0
          and abs(p119["ab"] - S.EXT119_AB) <= 0.01
          and p119["Nw"] == S.EXT119_N,
          "MAIN sch<0 %d/42; EXT-119 N=%d |t|=%.4f"
          % (n_neg, p119["Nw"], p119["ab"]))


def main():
    print("=" * 72)
    print("verify_source_sch.py -- round 417")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("SOURCE SCH SIGN VERIFIED")
        return 0
    print("SOURCE SCH SIGN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
