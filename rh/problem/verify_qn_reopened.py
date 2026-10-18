#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_qn_reopened.py -- machine check of every numbered
lemma in rh/problem/qn_reopened.tex (round 428,
SELECTED_MARGIN_GO / OVERLAP_VAC_ONLY /
ZLOC_WINS / COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  q_N = (7/5) Z^2; Z=1/2 => 7/20
  G2  Z0_sel = 1/2 < M
  G3  living inner product 0 vs dead 1

PART B (CONSTRUCTION PINS):
  G10 prime-power map k=4 -> kz=9
  G11 w9 four coordinates + COMPOSE room
  G12 k=6 VAC overlap 1e-8 class; Nyquist face
      refuted; dead-15 death channel;
      kz=16 false-anchor

Exit: "QN REOPENED VERIFIED" iff every gate passed.
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

import qn_reopened_probe as S  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402
import edge_signature_probe as ES  # noqa: E402

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
    section("PART A  DICTIONARY / Z0 / ORTHOGONALITY")
    t = S.dict_Q()
    check("G1-dictionary-Q",
          t["q"] == Fr(7, 20) and t["lt"] and t["q_lt"],
          "7/20 < 1 iff (1/2)^2 < 5/7")
    check("G2-Z0sel-Q",
          t["z0"] == Fr(1, 2) and t["z0_lt_M"],
          "1/2 < M")
    o = S.orth_Q()
    check("G3-orth-Q",
          o["live"] == Fr(0) and o["ratio"] == Fr(10000),
          "living 0; 1e-4/1e-8 = 10^4")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    kz, a, rec = S.pp_kz(4)
    check("G10-pp-map",
          kz == 9 and a == 16 and abs(rec - 16.0) <= 1e-9,
          "2^4 is the kz=9 prime power")
    w = S.four_pack(9, compose=True)
    check("G11-w9",
          w["qN"] < 0.22 and w["sch"] < 0
          and w["absZloc"] < S.Z0_SEL < S.M_W
          and w["R"] < S.R0 and w["L1"] < S.LAMBDA
          and abs(w["qN"] - S.W9_QN) <= 0.001,
          "qN=%.4f |Zloc|=%.4f R=%.3f" % (
              w["qN"], w["absZloc"], w["R"]))
    k6 = S.four_pack(26, compose=True)
    c_p1 = S.nyquist_cos(9)
    c_vac = S.nyquist_cos(26)
    d15 = C2.row2(C2.chi_pack("CHI3", 15))
    p15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    a16 = S.four_pack(16, compose=True)
    check("G12-vac-dead-anchor",
          k6["razor"] <= 1e-6 and (not k6["P1"])
          and abs(c_p1) >= S.NYQ_P1_ABS
          and abs(c_vac) <= S.NYQ_VAC_ABS
          and d15["qN"] > 1 and p15["sch"] > 0
          and d15["absZloc"] > S.M_W
          and a16["qN"] > 0.97 and a16["qN"] < 1
          and a16["razor"] <= 1e-7,
          "k6 raz=%.2e nyq P1/VAC=%.2f/%.3f; "
          "dead15 qN=%.3f; kz16 qN=%.4f raz=%.2e"
          % (k6["razor"], c_p1, c_vac, d15["qN"],
             a16["qN"], a16["razor"]))


def main():
    print("=" * 72)
    print("verify_qn_reopened.py -- round 428")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("QN REOPENED VERIFIED")
        return 0
    print("QN REOPENED FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
