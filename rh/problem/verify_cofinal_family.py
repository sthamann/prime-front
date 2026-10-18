#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_cofinal_family.py -- machine check of every numbered
lemma in rh/problem/cofinal_family.tex (round 458,
FAMILY_CANDIDATE / TABLE_CAP_ARTEFACT /
RESIDUAL_DEEP_DEATH).

PART A (STANDALONE):
  G1  verdict FAMILY_CANDIDATE
  G2  sealed grid size 76
  G3  capped a-wall 631/641
  G4  Lean selectedMesh formula k=10

PART B (CONSTRUCTION PINS):
  G10 Lean k=10 cap-live at pin q
  G11 kz197 capped-dead at n=3788

Exit: "COFINAL FAMILY VERIFIED" iff every gate passed.
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

import cofinal_family_probe as S  # noqa: E402

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
    section("PART A  VERDICT / GRID / WALL")
    check("G1-verdict",
          S.VERDICT == "FAMILY_CANDIDATE",
          "verdict=%s" % S.VERDICT)
    check("G2-grid",
          len(S.SCAN_KZ) == 76,
          "n=%d" % len(S.SCAN_KZ))
    check("G3-wall",
          S.MAX_LIVE_A == 631 and S.MIN_DEAD_A == 641
          and S.N_SCAN_LIVE == 55,
          "live a<=%d dead a>=%d" % (S.MAX_LIVE_A, S.MIN_DEAD_A))
    shp = S.lean_shape(10)
    check("G4-lean-mesh",
          shp["a"] == 1024 and shp["m"] == 79 and shp["Nw"] == 40,
          "a=%d m=%d N=%d" % (shp["a"], shp["m"], shp["Nw"]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    pk, _shp = S.lean_pack(10)
    check("G10-lean10",
          pk.get("ok") and abs(pk["qdag"] - S.LEAN10_Q) < 1e-12
          and (pk.get("n_flip") or 0) == 0 and pk.get("pos_ok"),
          "q=%.12f" % pk.get("qdag", -1))
    r = S.frame_first(197)
    check("G11-kz197-capped",
          (not r["live"]) and r["first"] == S.KZ197_CAPPED_FIRST,
          "first=%s" % r["first"])


def main():
    print("=" * 72)
    print("verify_cofinal_family.py -- round 458")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("COFINAL FAMILY VERIFIED")
        return 0
    print("COFINAL FAMILY FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
