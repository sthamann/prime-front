#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_fullcomb_cleanup.py -- machine check of every numbered
lemma in rh/problem/fullcomb_cleanup.tex (round 459,
RACE_TREND_BROKEN / LEANFAM_EXACT_ALIVE(12) /
KZ137_OUTSIDE_MINCUT).

PART A (STANDALONE):
  G1  verdicts
  G2  frame-A race pins (197/230 < 136)
  G3  Lean race band k=5..12
  G4  Lean mesh k=10

PART B (CONSTRUCTION PINS):
  G10 kz17 full-comb race
  G11 Lean k=10 race + q
  G12 Lean a=641 k=9 lives

Exit: "FULLCOMB CLEANUP VERIFIED" iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import fullcomb_cleanup_probe as S  # noqa: E402

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
    section("PART A  VERDICTS / PINS")
    check("G1-verdicts",
          S.VERDICT_A == "RACE_TREND_BROKEN"
          and S.VERDICT_B == "LEANFAM_EXACT_ALIVE(12)"
          and S.VERDICT_C == "KZ137_OUTSIDE_MINCUT",
          "%s / %s / %s" % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    check("G2-fa-broken",
          S.FA_RACE[197] < S.FA_RACE[136]
          and S.FA_RACE[230] < 0.80
          and S.FA_RACE[17] < 0.50,
          "197=%.4f < 136=%.4f; 230=%.4f"
          % (S.FA_RACE[197], S.FA_RACE[136], S.FA_RACE[230]))
    lr = [S.LEAN_RACE[k] for k in range(5, 13)]
    check("G3-lean-band",
          max(lr) < 0.80 and min(lr) > 0.55,
          "[%.3f, %.3f]" % (min(lr), max(lr)))
    shp = S.S458.lean_shape(10)
    check("G4-lean-mesh",
          shp["a"] == 1024 and shp["m"] == 79 and shp["Nw"] == 40,
          "a=%d m=%d N=%d" % (shp["a"], shp["m"], shp["Nw"]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    rows = S.sieve_pp(1_100_000)
    r17 = S.fa_budget(17, rows)
    check("G10-kz17",
          r17["complete"] and r17["live"]
          and abs(r17["race"] - S.FA_RACE[17]) < 1e-10,
          "race=%.12f ka=%d" % (r17["race"], r17["ka"]))
    r10 = S.lean_budget(10, rows)
    check("G11-lean10",
          r10["complete"] and r10["live"]
          and abs(r10["qM"] - S.LEAN10_Q) < 1e-12
          and abs(r10["race"] - S.LEAN_RACE[10]) < 1e-10,
          "q=%.12f race=%.12f" % (r10["qM"], r10["race"]))
    r9 = S.lean_budget(9, rows, a=641)
    check("G12-lean641",
          r9["live"] and r9["complete"]
          and abs(r9["race"] - S.LEAN641_RACE9) < 1e-9,
          "a=641 m=%d race=%.12f" % (r9["m"], r9["race"]))


def main():
    print("=" * 72)
    print("verify_fullcomb_cleanup.py -- round 459")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("FULLCOMB CLEANUP VERIFIED")
        return 0
    print("FULLCOMB CLEANUP FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
