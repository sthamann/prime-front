#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_jp_increment.py -- machine check of every numbered
lemma in rh/problem/jp_increment.tex (round 457,
INCREMENT_DRIFT / RACE_EATS_K10 / LEMMA_REDUCED).

PART A (STANDALONE):
  G1  verdicts + r456 VACUOUS_CONFIRMED accepted
  G2  kz17 cliff dq at J_P
  G3  kz17 post-J_P Delta rho all positive

PART B (CONSTRUCTION PINS):
  G10 kz17 race in (0.4, 0.6) and q_full < 1
  G11 kz197 race eats the margin
  G12 scramble breaks (q_SCR(30)>1)

Exit: "JP INCREMENT VERIFIED" iff every gate passed.
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

import jp_increment_probe as S  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import vacuity_redteam_probe as S456  # noqa: E402

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
    section("PART A  VERDICT / CLIFF / DRIFT")
    check("G1-verdict",
          S.VERDICT_A == "INCREMENT_DRIFT"
          and S.VERDICT_B == "RACE_EATS_K10"
          and S.VERDICT_C == "LEMMA_REDUCED"
          and S456.VERDICT == "VACUOUS_CONFIRMED",
          "%s / %s / %s (r456 accepted)"
          % (S.VERDICT_A, S.VERDICT_B, S.VERDICT_C))
    b = S.budget(17)
    pM = S451.pack_at(b["mzM"], b["jp"], b["border"])
    pA = S451.pack_at(b["mzA"], b["jp"], b["border"])
    dq = pM["qdag"] - pA["qdag"]
    check("G2-cliff",
          abs(dq - S.CLIFF_17) < 1e-8,
          "dq=%.8f" % dq)
    import numpy as np
    import deep_builder_probe as S445
    bpM = S445.bord_pack_slim(
        b["mzM"]["xp"], b["mzM"]["wp"], b["mzM"]["yn"], b["mzM"]["vn"],
        *b["border"], b["Nw"], engine="numpy", require_pos=False)
    bpA = S445.bord_pack_slim(
        b["mzA"]["xp"], b["mzA"]["wp"], b["mzA"]["yn"], b["mzA"]["vn"],
        *b["border"], b["Nw"], engine="numpy", require_pos=False)
    dlt = (np.asarray(bpM["rho"])[b["jp"]:]
           - np.asarray(bpA["rho"])[b["jp"]:])
    check("G3-drho",
          int((dlt > 0).sum()) == len(dlt),
          "npos=%d/%d" % (int((dlt > 0).sum()), len(dlt)))


def part_b():
    section("PART B  RACE / K10 / SCRAMBLE")
    r17 = S.budget(17)
    check("G10-race17",
          0.4 < r17["race"] < 0.6 and r17["qM"] < 1.0,
          "race=%.3f qM=%.5f" % (r17["race"], r17["qM"]))
    r197 = S.budget(197)
    check("G11-k10",
          r197["race"] > S.RACE_197_BAR and r197["qM"] > 0.99,
          "race=%.3f qM=%.5f" % (r197["race"], r197["qM"]))
    mzS = S451.scramble_mz(r17["mzM"], S.SCRAMBLE_SEED)
    pS = S451.pack_at(mzS, 30, r17["border"])
    check("G12-scramble",
          pS["qdag"] > 1.0,
          "q_SCR(30)=%.5f" % pS["qdag"])


def main():
    print("verify_jp_increment -- r457")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("JP INCREMENT VERIFIED")
        return 0
    print("JP INCREMENT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
