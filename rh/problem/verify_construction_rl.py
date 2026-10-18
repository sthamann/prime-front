#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_construction_rl.py -- machine check of every numbered
lemma in rh/problem/construction_rl.tex (round 391,
LEMMA.CONSTRUCTION_PURE.RL.01).

PART A (STANDALONE): probe toys G1--G8 plus
  G8b  K=4 vs K/2=2 and C_MAIN=3/10 over Q
  G9   eta identity and CS counting on a second Q-tuple

PART B (CONSTRUCTION PINS): probe G10--G16

Exit: per-gate PASS/FAIL and the final line
"CONSTRUCTION PURE RL VERIFIED" iff every (selected) gate passed.

NO RH CLAIM.  Finite identities and named reductions.
"""
from __future__ import annotations

import argparse
import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import construction_pure_rl_probe as P  # noqa: E402

CHECKS = []
K_STAR = P.K_STAR
K_HALF = P.K_HALF
C_MAIN = P.C_MAIN


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
    section("PART A extra -- K vs K/2, eta, CS counting")
    check("G8b-K-over-Q",
          Fr(K_STAR) == Fr(4) and Fr(K_HALF) == Fr(2)
          and Fr(3, 10) == Fr(C_MAIN).limit_denominator(100)
          and K_HALF < 2.9752 < K_STAR,
          "K=4, K/2=2; star 2.975 sits strictly between; "
          "C_MAIN=3/10")
    # second Q-tuple for eta: Pb=(1,0,-1), Pw=(0,1,1)
    Pb = np.array([Fr(1), Fr(0), Fr(-1)], dtype=object)
    Pw = np.array([Fr(0), Fr(1), Fr(1)], dtype=object)
    Sig = Pb + Pw
    Del = Pb - Pw
    lhs = sum(Sig * Sig) + sum(Del * Del)
    rhs = 2 * (sum(Pb * Pb) + sum(Pw * Pw))
    eta_n = 2 * sum(Pb * Pw)
    eta_d = sum(Pb * Pb) + sum(Pw * Pw)
    check("G9-eta-and-CS-second-tuple",
          lhs == rhs
          and eta_n == Fr(-2) and eta_d == Fr(4)
          and sum(abs(t) for t in Del) ** 2 <= Fr(3) * sum(Del * Del),
          "split SATZ; eta=-1/2; CS counting on Delta")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--full", action="store_true")
    args = par.parse_args()
    print("verify_construction_rl.py -- construction-pure (R)(L) "
          "(round 391)")
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
        print("CONSTRUCTION PURE RL FAILED")
        sys.exit(1)
    print("CONSTRUCTION PURE RL VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
