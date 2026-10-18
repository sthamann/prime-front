#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_zloc_head.py -- machine check of every numbered
lemma in rh/problem/zloc_head.tex (round 429,
FORMULA_SATZ / TRIANGLE_REFUTED /
BOUND_CENSUS / NO_K0).

PART A (STANDALONE OVER Q):
  G1  q_N = (7/5) Z^2; Z=1/2 => 7/20
  G2  Z = Zloc + t_bulk; unsigned triangle
      can exceed 1/2
  G3  Z0 = 1/2 < M; 2/3 > 3/5

PART B (CONSTRUCTION PINS):
  G10 w9 formula t_loc + chain = 0.157211
  G11 triangle >> 1/2; scramble > 1/2;
      dead-15 > M
  G12 kz=16 reproduces 0.756; k=3,4,5
      all |Zloc| <= 1/2

Exit: "ZLOC HEAD VERIFIED" iff every gate passed.
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

import zloc_head_probe as S  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402

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
    section("PART A  DICTIONARY / SPLIT / HALF")
    t = S.dict_Q()
    check("G1-dictionary-Q",
          t["q"] == Fr(7, 20) and t["z0_lt_M"],
          "7/20 < 1 iff (1/2)^2 < 5/7")
    s = S.split_Q()
    check("G2-split-Q",
          s["split"] and s["tri_gt_half"]
          and s["Zloc"] == Fr(-3, 5),
          "identity; triangle 3/5 > 1/2")
    check("G3-half-and-L1",
          t["z0"] == Fr(1, 2) and S.L1_23 > Fr(3, 5),
          "1/2 < M; 2/3 > 3/5")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    d4 = S.dissect(S.pack(9))
    check("G10-w9-formula",
          abs(d4["absZloc"] - S.K4_ZLOC) <= 2e-6
          and abs(d4["t_loc"] + d4["chain"] - d4["Zloc"]) <= 1e-12
          and d4["n_edge"] == S.K4_NEDGE,
          "|Zloc|=%.6f = t_loc+chain; n_edge=%d"
          % (d4["absZloc"], d4["n_edge"]))
    s = S.dissect(S.pack(9, scramble_seed=1))
    d15 = S.dissect(C2.chi_pack("CHI3", 15))
    check("G11-triangle-kills",
          d4["tri"] > 0.5 and s["absZloc"] > 0.5
          and d15["absZloc"] > S.M_W,
          "tri=%.3f SCR=%.4f dead15=%.4f"
          % (d4["tri"], s["absZloc"], d15["absZloc"]))
    a16 = S.dissect(S.pack(16))
    d3 = S.dissect(S.pack(5))
    d5 = S.dissect(S.pack(17))
    check("G12-selected-and-razor",
          abs(a16["absZloc"] - S.KZ16_ZLOC) <= 0.002
          and d3["absZloc"] < 0.5
          and d4["absZloc"] < 0.5
          and d5["absZloc"] < 0.5,
          "kz16=%.4f; k=3,4,5 all <= 1/2"
          % a16["absZloc"])


def main():
    print("=" * 72)
    print("verify_zloc_head.py -- round 429")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("ZLOC HEAD VERIFIED")
        return 0
    print("ZLOC HEAD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
