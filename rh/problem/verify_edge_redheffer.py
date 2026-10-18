#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_edge_redheffer.py -- machine check of every numbered
lemma in rh/problem/edge_redheffer.tex (round 433,
REDHEFFER_EXACT / PIVOT_IS_ONE_MINUS_QDAG /
QUARTER_NOT_UNIVERSAL).

PART A (STANDALONE OVER Q):
  G1  mixed form == Redheffer load, den=23/30
  G2  sequential CD-then-border residual 0
  G3  last-pivot dictionary: sch=-187/450,
      sch_b=187/1426, delta=-sch
  G4  1/4 < 5/7; drop-border Y-block != M^dagger

PART B (CONSTRUCTION PINS):
  G10 w9 Redheffer residual; 1-q^dagger=-sch
  G11 k=3 |Z_loc| air and delta>0
  G12 dead CHI3-15 delta<0; living CHI3-9
      delta>0 but qtr<0
  G13 ones-Woodbury Delta is not the pivot

Exit: "EDGE REDHEFFER VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import edge_redheffer_probe as S  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import edge_contractive_lift_probe as E405  # noqa: E402

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
    section("PART A  REDHEFFER / LAST PIVOT / DICTIONARY")
    T = S.mixed_toy_blocks()
    check("G1-Redheffer-mixed-Q",
          T["dev_mix"] == 0 and T["den"] == S.TOY_DEN,
          "den=%s residual 0" % T["den"])
    check("G2-sequential-Q",
          T["dev_seq"] == 0,
          "CD-then-border residual 0")
    dlt = S.delta_from_schb(T["sch_b"])
    check("G3-pivot-dictionary-Q",
          T["sch"] == S.TOY_SCH
          and T["sch_b"] == S.TOY_SCHB
          and dlt == -T["sch"],
          "sch=%s sch_b=%s delta=%s" % (T["sch"], T["sch_b"], dlt))
    t = S.dict_Q()
    check("G4-quarter-and-drop-border",
          t["qtr_lt_M2"] and T["dev2"] != 0
          and t["qN_at_half"] == Fr(7, 20),
          "1/4<5/7; drop-border kills the 3x3 pivot")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.row_of(9)
    check("G10-w9-Redheffer-identity",
          w["ok"] and w["dev_load"] < 1e-12
          and w["id_q"] < S.ID_RES
          and abs(w["sch"] - S.W9_SCH) <= 1e-10,
          "residual %.1e; 1-q^d=-sch (%.1e)"
          % (w["dev_load"], w["id_q"]))
    k3 = S.row_of(5)
    check("G11-k3-margin",
          abs(k3["absZ"] - S.K3_ZLOC) <= 2e-6
          and k3["delta"] > 0 and k3["qtr"] > 0,
          "|Zloc|=%.6f air=%.6f delta=%.6f"
          % (k3["absZ"], 0.5 - k3["absZ"], k3["delta"]))
    d15 = S.row_of(15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"))
    live9 = S.row_of(9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G12-dead-live-chi",
          d15["delta"] < 0 and live9["delta"] > 0
          and live9["qtr"] < 0,
          "dead15 delta=%+.4f; live9 delta=%+.4f qtr=%+.4f"
          % (d15["delta"], live9["delta"], live9["qtr"]))
    R = PX.build_rung(9)
    mz = R["mz"]
    c9 = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                      R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                      keep=True)
    ones = E405.ones_woodbury_Y(c9["A0"], c9["U"])
    check("G13-ones-kill",
          abs(ones["Delta"] - w["delta"]) > 0.05,
          "ones Delta=%.3e != delta=%.3e"
          % (ones["Delta"], w["delta"]))


def main():
    print("=" * 72)
    print("verify_edge_redheffer.py -- round 433")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("EDGE REDHEFFER VERIFIED")
        return 0
    print("EDGE REDHEFFER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
