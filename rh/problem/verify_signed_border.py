#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_signed_border.py -- machine check of every numbered
lemma in rh/problem/signed_border_mean.tex (round 444,
ZIRKULAER / TRIPLE_SUM_EXACT / POLE_NOT_CARRIER /
DIAGONAL_OVERFLOWS / OFFDIAG_LOADBEARING /
DEAD_CHI_POLE_OVERSHOOT).

PART A (STANDALONE OVER Q):
  G1  triple-sum expansion: q = 9 = 5 + 4
  G2  pole/regular split: q = 10/3 = 2 + 4/3
  G3  diagonal of the Q toy is NOT the whole q

PART B (CONSTRUCTION PINS):
  G10 w9 triple-sum identity + diag/off/pole
  G11 selected k=3,4,5 pole_share < 0.01, q<1
  G12 dead CHI3-15 pole overshoot; live CHI3-9 not;
      |b|-envelope >>1; kernel not cosine

Exit: "SIGNED BORDER MEAN VERIFIED" iff every gate passed.
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

import signed_border_mean_probe as S  # noqa: E402
import edge_redheffer_probe as ER  # noqa: E402
import block_mean_probe as BM  # noqa: E402
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
    section("PART A  TRIPLE SUM / POLE SPLIT OVER Q")
    q = Fr(9)
    qd = Fr(5)
    qo = Fr(4)
    check("G1-Q-triple-sum",
          q == qd + qo and qd > 0 and qo > 0,
          "q=9 = diag=5 + off=4")
    qp = Fr(10, 3)
    qpole = Fr(2)
    qreg = Fr(4, 3)
    check("G2-Q-pole-split",
          qp == qpole + qreg,
          "q=10/3 = pole=2 + reg=4/3")
    check("G3-Q-diag-not-whole",
          qd != q and qd < q,
          "unsigned skeleton (diag) does not exhaust q")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.split_q(9, phase=True)
    r = ER.redheffer_of(ER._measures(9))
    check("G10-w9-identity-split",
          abs(w["qform"] - r["qdag"]) < S.SRC_RES
          and abs(w["q_diag"] - S.W9_QDIAG) < S.SPLIT_BAR
          and abs(w["q_pole"] - S.W9_QPOLE) < S.POLE_BAR
          and w["pole_share"] < 0.01
          and w["recon_res"] < S.RECON_BAR
          and w["qabs"] > 10.0
          and abs(w["corr_cos"]) < S.CORR_BAR,
          "q=%.8f diag=%.8f pole=%.6f recon=%.2e corr=%.4f"
          % (w["qform"], w["q_diag"], w["q_pole"],
             w["recon_res"], w["corr_cos"]))
    for k, kz in ((3, 5), (4, 9), (5, 17)):
        row = S.split_q(kz)
        check("G11-sel-k%d" % k,
              row["qform"] < 1.0
              and row["pole_share"] < 0.01
              and abs(row["q_diag"] - S.SEL_QDIAG[k]) < S.SPLIT_BAR
              and abs(row["qform"] - BM.SEL_Q[k]) < S.Q_BAR,
              "k=%d q=%.8f diag=%.8f share=%.4f"
              % (k, row["qform"], row["q_diag"], row["pole_share"]))
    d = S.spectral_only(
        15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"))
    live = S.spectral_only(
        9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G12-chi-overshoot",
          d["qform"] > 1.0 and d["q_reg"] < 1.0
          and d["q_pole"] > (1.0 - d["q_reg"])
          and live["qform"] < 1.0 and live["q_pole"] < 0.01,
          "dead15 q=%.6f pole=%.5f overshoot; live9 pole=%.5f"
          % (d["qform"], d["q_pole"], live["q_pole"]))


def main():
    print("=" * 72)
    print("verify_signed_border.py -- round 444")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("SIGNED BORDER MEAN VERIFIED")
        return 0
    print("SIGNED BORDER MEAN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
