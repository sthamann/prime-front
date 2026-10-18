#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_compose_premises.py -- machine check of every numbered
lemma in rh/problem/compose_premises.tex (round 383, COMPOSE
premises (R)(L)(Z)).

PART A (STANDALONE): probe toys G1--G7 plus
  G8  pref <= sqrt(m)+1 (r378 H-rule)
  G9  T1-floor algebra and compose phi formula

PART B (CONSTRUCTION PINS): probe G10--G14
  (w9, scramble M3-kill of (L), kz37 R_star, kz16 Z_star,
   kz111 E_pi spike / T1-combo)

PART C (--full): probe G20--G27, the 181-window census.

Exit: per-gate PASS/FAIL and the final line
"COMPOSE PREMISES VERIFIED" iff every (selected) gate passed.

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

import compose_premises_probe as CPP  # noqa: E402

CHECKS = []
M_W = CPP.M_W
R0 = CPP.R0
Z0 = CPP.Z0
LAMBDA = CPP.LAMBDA
CAP = CPP.CAP


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


def pref_of(m):
    H = max(2, int(math.ceil(math.sqrt(m))))
    return H, Fr(m + H - 1, H)


def part_extra():
    section("PART A extra -- H-rule, T1-floor, phi")
    ok = True
    for m in range(1, 400):
        _H, pref = pref_of(m)
        ok &= float(pref) <= math.sqrt(m) + 1.0 + 1e-12
    check("G8-pref-H-rule", ok,
          "pref <= sqrt(m)+1 for m=1..399")
    b2 = CPP.t1_m3(5.0, 100)
    hand = (8.0 / 3.0) ** 2 * 25.0 * (math.log(100.0) ** 2) / 10000.0
    check("G9-T1-floor-algebra",
          abs(b2 - hand) < 1e-12,
          "M3 <= ((8/3) C_K log m / m)^2 at C_K=5 m=100")
    ph = CPP.phi_of(100, R0, LAMBDA, Z0)
    gap = M_W - Z0
    pref = math.sqrt(100.0) + 1.0
    handp = (gap ** 4) / (pref ** 2 * R0 ** 2 * LAMBDA ** 4)
    check("G9b-phi-formula",
          abs(ph - handp) < 1e-15 and ph > 0 and Z0 < M_W,
          "phi(100)=%.6e; M-Z0=%.6f; Z0=4/5 < M" % (ph, gap))
    # r378 compose implication on the w9 numbers: sufficient
    # |Zloc| + sqrt(pref R0) L1 M3^{1/4} < M ?
    # (not claimed as a census here; the algebra is the SATZ)
    m = 35
    H, prefF = pref_of(m)
    rhs = math.sqrt(float(prefF) * R0) * 0.4038 * (0.004726 ** 0.25)
    check("G9c-compose-shape-w9",
          0.1572 + rhs < M_W,
          "w9 toy numbers: |Zloc|+sqrt(pref R0) L1 M3^{1/4}="
          "%.4f < M=%.4f (shape of COMPOSE-)"
          % (0.1572 + rhs, M_W))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--full", action="store_true")
    args = par.parse_args()
    print("verify_compose_premises.py -- COMPOSE premises (R)(L)(Z) "
          "(round 383)")
    print("NO RH CLAIM.", flush=True)
    CPP.CHECKS.clear()
    CPP.part_toys()
    part_extra()
    CPP.part_pins()
    if args.full:
        CPP.part_full()
    allc = list(CPP.CHECKS) + list(CHECKS)
    npass = sum(1 for _n, ok in allc if ok)
    nfail = sum(1 for _n, ok in allc if not ok)
    print("\n" + "=" * 72)
    print("%d/%d gates  (%d FAIL)" % (npass, len(allc), nfail))
    if nfail:
        print("COMPOSE PREMISES FAILED")
        sys.exit(1)
    print("COMPOSE PREMISES VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
