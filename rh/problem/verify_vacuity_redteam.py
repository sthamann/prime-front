#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_vacuity_redteam.py -- machine check of every numbered
lemma in rh/problem/vacuity_redteam.tex (round 456,
VACUOUS_CONFIRMED).

PART A (STANDALONE):
  G1  verdict VACUOUS_CONFIRMED
  G2  comb U=2 pin / blind zero
  G3  Iff.rfl is a naming (Lean text)

PART B (CONSTRUCTION PINS):
  G10 kz17 prefix n=8 world-blind; J_P cliff
  G11 kz69 n_stab world-blind; n_f splits

Exit: "VACUITY REDTEAM VERIFIED" iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import math
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import vacuity_redteam_probe as S  # noqa: E402
import prefix_mincut_probe as S450  # noqa: E402

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
    section("PART A  VERDICT / COMB / LEAN NAME")
    check("G1-verdict",
          S.VERDICT == "VACUOUS_CONFIRMED",
          "verdict=%s" % S.VERDICT)
    c2, n2 = S.comb_read(S.U_F)
    cb, nb = S.comb_read(S.U_BLIND)
    check("G2-comb",
          abs(c2 - S.COMB_PIN) < 1e-12 and n2 == 5
          and cb == 0.0 and nb == 0,
          "U2=%.16f n=%d; blind=0" % (c2, n2))
    h = S.lean_map()
    check("G3-iff-naming",
          h["iff_rfl"] and h["mincut_cap"] and h["fullRead"]
          and h["combRead"],
          "Iff.rfl present; cone is W.cap; fullRead has comb")


def part_b():
    section("PART B  WORLDS / HONEST DEPTH")
    r8 = S.dq_at(17, 8)
    r19 = S.dq_at(17, 19)
    check("G10-kz17",
          r8["dq"] < 1e-14
          and abs(r19["dq"] - S.CLIFF_17) < 1e-8
          and r19["dq"] > 0.04
          and abs(S.dq_at(17, 18)["dM"] - S450.D_PRE[17]) < 1e-12,
          "n8 dq=%.3e  J_P dq=%.5f" % (r8["dq"], r19["dq"]))
    r119 = S.dq_at(69, 119)
    r2053 = S.dq_at(69, 2053)
    check("G11-kz69",
          r119["dq"] < 1e-14
          and abs(r2053["dq"] - S.HONEST_69) < 1e-8
          and r2053["dq"] > 1e-3,
          "n_stab dq=%.3e  n_f dq=%.6f" % (r119["dq"], r2053["dq"]))
    _a, _M, _L, _Nw, D = __import__(
        "verify_lstar_instance", fromlist=["window_shape"]).window_shape(197)
    n_f = int(math.ceil(S.U_F / D - 1e-12))
    flip = __import__("flip_vs_stab_probe").FLIPS[197]
    check("G12-tail-U2",
          flip > n_f,
          "kz197 flip=%d > n_f=%d (TAIL_ONLY vs U=2)" % (flip, n_f))


def main():
    print("verify_vacuity_redteam -- r456")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("VACUITY REDTEAM VERIFIED")
        return 0
    print("VACUITY REDTEAM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
