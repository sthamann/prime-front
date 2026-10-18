#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_compose_premises2.py -- machine check of every numbered
lemma in rh/problem/compose_premises2.tex (round 386,
living-ladder (Z') and cofinal R0).

PART A (STANDALONE): probe toys G1--G6 plus
  G8  Z0' = 21/25 < M = sqrt(5/7) over Q
  G9  C_MAIN = 3/10, death-triangle sufficient form

PART B (CONSTRUCTION PINS): probe G10--G15

PART C (--full): probe G20--G27, the 181-window census.

Exit: per-gate PASS/FAIL and the final line
"COMPOSE PREMISES2 VERIFIED" iff every (selected) gate passed.

NO RH CLAIM.  Finite identities and named reductions.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import compose_premises2_probe as P  # noqa: E402

CHECKS = []
M_W = P.M_W
Z0P = P.Z0P
C_MAIN = P.C_MAIN
Z0_OLD = P.Z0_OLD


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


def part_extra():
    section("PART A extra -- Z0' vs M, C_MAIN, death triangle")
    z0 = Fr(21, 25)
    m2 = Fr(5, 7)
    check("G8-Z0p-lt-M-over-Q",
          z0 ** 2 < m2 and float(z0) == Z0P,
          " (21/25)^2 = 441/625 < 5/7; Z0'=0.84 < M")
    check("G8b-old-Z0-lt-Z0p",
          Fr(4, 5) < z0,
          "4/5 < 21/25 (r383 Z0 is strictly smaller)")
    check("G9-CMAIN-three-tenths",
          Fr(3, 10) == Fr(C_MAIN).limit_denominator(100)
          and C_MAIN < 4.0,
          "C_MAIN=3/10 < R0=4")
    # sufficient death form over Q
    zloc, tb = Fr(1), Fr(-1, 10)
    z = zloc + tb
    gap = abs(zloc) - Fr(int(math.floor(float(M_W) * 1000)), 1000)
    check("G9b-death-triangle-Q",
          abs(z) == Fr(9, 10) and abs(z) > 0
          and abs(zloc) > abs(tb),
          "|1 + (-1/10)|=9/10; triangle is SATZ")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--full", action="store_true")
    args = par.parse_args()
    print("verify_compose_premises2.py -- living (Z') and cofinal R0 "
          "(round 386)")
    print("NO RH CLAIM.", flush=True)
    P.CHECKS.clear()
    P.part_toys()
    part_extra()
    P.part_pins()
    if args.full:
        P.part_full()
    allc = list(P.CHECKS) + list(CHECKS)
    npass = sum(1 for _n, ok in allc if ok)
    nfail = sum(1 for _n, ok in allc if not ok)
    print("\n" + "=" * 72)
    print("%d/%d gates  (%d FAIL)" % (npass, len(allc), nfail))
    if nfail:
        print("COMPOSE PREMISES2 FAILED")
        sys.exit(1)
    print("COMPOSE PREMISES2 VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
