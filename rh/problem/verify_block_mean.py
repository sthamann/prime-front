#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_block_mean.py -- machine check of every numbered
lemma in rh/problem/block_mean.tex (round 442,
REDUZIERT / DICTIONARY_EXACT /
UNSIGNED_MAJORANT_REFUTED / SELECTED_POINTWISE_CENSUS /
MEAN_BOUND_OPEN).

PART A (STANDALONE OVER Q):
  G1  last-pivot dictionary: q^dagger = 263/450,
      delta = 187/450 = -sch
  G2  living toy: q^dagger < 1 so kappa-pred = 0
  G3  MI2 linearity on the r440 Q pair

PART B (CONSTRUCTION PINS):
  G10 w9 dictionary kappa = 1{q>1} = 0; source form
  G11 selected k=3,4,5 all q<1, kappa=0
  G12 dead CHI3-15 q>1 and kappa=1; live CHI3-9
      q<1 and kappa=0; unsigned |b| envelope >>1

Exit: "BLOCK MEAN VERIFIED" iff every gate passed.
NO RH CLAIM.
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

import block_mean_probe as S  # noqa: E402
import edge_redheffer_probe as ER  # noqa: E402
import mean_tau_index_probe as MT  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

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
    section("PART A  DICTIONARY / MI2 OVER Q")
    T = ER.mixed_toy_blocks()
    qQ = Fr(263, 450)
    dlt = Fr(187, 450)
    check("G1-Q-pivot-dictionary",
          T["sch"] == -dlt and (Fr(1) - qQ) == -T["sch"],
          "q^d=263/450; delta=-sch=187/450")
    check("G2-Q-living",
          qQ < 1,
          "kappa-pred=0")
    Gf = np.array([[2.0, 0.0], [0.0, 0.5]])
    G2 = np.diag([0.4, 0.3])
    w1 = MT.winding_circle(Gf, 0.5, 0.40, n=64)
    w2 = MT.winding_circle(G2, 0.5, 0.40, n=64)
    wm = MT.winding_mean([Gf, G2], 0.5, 0.40, n=64)
    check("G3-MI2-linearity-Q",
          abs(wm - 0.5 * (w1 + w2)) < 1e-12
          and abs(w1.real - 1.0) < 1e-8
          and abs(w2.real) < 1e-8,
          "mean winds=%.6f avg-integrand=%.6f"
          % ((w1.real + w2.real) / 2, wm.real))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    p = S.kappa_of(9)
    m = ER._measures(9)
    r = ER.redheffer_of(m)
    src = S.source_q(m)
    check("G10-w9-dictionary-source",
          p["kappa_G"] == 0 and int(r["qdag"] > 1) == 0
          and abs(r["qdag"] - S.W9_QDAG) <= 1e-8
          and abs(src["qform"] - r["qdag"]) < S.SRC_RES
          and src["qabs"] > 10.0,
          "kappa=1{q>1}=0; source res=%.2e; |b|-env=%.2f"
          % (abs(src["qform"] - r["qdag"]), src["qabs"]))
    for k, kz in ((3, 5), (4, 9), (5, 17)):
        rr = ER.redheffer_of(ER._measures(kz))
        pp = S.kappa_of(kz)
        check("G11-sel-k%d" % k,
              pp["kappa_G"] == 0 and rr["qdag"] < 1.0
              and abs(rr["qdag"] - S.SEL_Q[k]) < S.Q_BAR,
              "k=%d kappa=0 q^d=%.8f" % (k, rr["qdag"]))
    rD = ER.redheffer_of(ER._measures(
        15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15")))
    pD = S.kappa_of(15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"))
    rL = ER.redheffer_of(ER._measures(
        9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9")))
    pL = S.kappa_of(9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G12-chi-dictionary",
          pD["kappa_G"] == 1 and rD["qdag"] > 1.0
          and pL["kappa_G"] == 0 and rL["qdag"] < 1.0,
          "dead15 q=%.6f kappa=1; live9 q=%.6f kappa=0"
          % (rD["qdag"], rL["qdag"]))


def main():
    print("=" * 72)
    print("verify_block_mean.py -- round 442")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("BLOCK MEAN VERIFIED")
        return 0
    print("BLOCK MEAN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
