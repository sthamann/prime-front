#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_p2_determinant.py -- machine check of every numbered
lemma in rh/problem/p2_determinant.tex (round 436,
REDUZIERT / IDENTITY_EXACT / ANATOMY_MIXED /
COARSE_KILLED_AT_KZ46 / ALTERNATION_EXPLAINED).

PART A (STANDALONE OVER Q):
  G1  reverse-CS identity det K2 = det(K2_+)-Q = -7
  G2  Q = ||p||^2 + p^T adj(R_+) p
  G3  drop-psi toy: det(K2_+)>0
  G4  tiny-overlap adversary: P1 without P2

PART B (CONSTRUCTION PINS):
  G10 w9 identity + C_min cosine = 1
  G11 kz18 min excess; kz46 coarse lmax FAILS
  G12 kz12 vacuous no-pole; CHI3-15 nneg-1 det<0
  G13 scramble nneg=21; wrong J sign-flips

Exit: "P2 DETERMINANT VERIFIED" iff every gate passed.
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

import p2_determinant_probe as S  # noqa: E402
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
    section("PART A  REVERSE-CS / DROP-PSI / ADVERSARY")
    T = S.toy_blocks()
    check("G1-reverse-CS-Q",
          T["detK"] == S.TOY_DETK
          and T["det_id"] == T["detK"]
          and T["detp"] == S.TOY_DETP
          and T["Q"] == S.TOY_Q
          and T["Qadj"] == T["Q"],
          "det K2 = %s = %s - %s" % (T["detK"], T["detp"], T["Q"]))
    check("G2-J-plus-R-split",
          T["pnorm2"] + T["QR"] == T["Q"]
          and T["pnorm2"] == Fr(5),
          "Q = ||p||^2 + p^T adj(R_+) p = 5+4")
    check("G3-drop-psi-toy",
          T["detp"] > 0 and T["detK"] < 0,
          "det(K2_+)=%s>0 without the pole" % T["detp"])
    A0a = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ua = 0.05 * np.array([[1.0, 0.0], [0.0, 1.0],
                          [0.0, 0.0], [0.0, 0.0]])
    sA = S.anatomy(A0a, Ua)
    check("G4-adversary",
          sA["nneg"] == 1 and sA["detK"] > 0 and sA["ray"] < 1,
          "P1 without P2: detK=%+.4f" % sA["detK"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w9 = S.row_of(S.MAIN_KZ, with_c=True)
    check("G10-w9-identity-Cmin",
          w9["P1"] and w9["P2"]
          and w9["err_id"] <= S.ID_BAR
          and abs(w9["detK"] / S.W9_DETK - 1.0) <= S.REL
          and w9["cos_cmin"] >= 1.0 - 1e-10
          and w9["nC"] == 1 and w9["alt"],
          "detK=%.4f ray=%.4f cosC=%.1e nC=%d"
          % (w9["detK"], w9["ray"],
             1.0 - w9["cos_cmin"], w9["nC"]))
    k18 = S.row_of(18)
    k46 = S.row_of(46)
    check("G11-kz18-floor-kz46-kill",
          abs(k18["detK"] / S.K18_DETK - 1.0) <= S.REL
          and abs(k18["excess"] - S.K18_EXCESS) <= 5e-3
          and (not k46["coarse_lmax"]) and k46["P2"]
          and k46["align"] > 0.95,
          "kz18 excess=%.4f; kz46 ||p||^2=%.4f < lmax=%.4f"
          % (k18["excess"], k46["pnorm2"], k46["lmaxp"]))
    k12 = S.row_of(12)
    d15 = S.row_of(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G12-vacuous-and-dead-chi",
          k12["nneg"] == 0 and k12["detK"] > 0
          and (not k12["alt"])
          and d15["nneg"] == 1 and d15["detK"] < 0
          and d15["alt"],
          "kz12 nneg=0 detK=%+.3f; CHI3-15 nneg=1 detK=%.2f"
          % (k12["detK"], d15["detK"]))
    aS, _oS = S.scramble_w9()
    detw = S.wrong_J_det(w9["_A0"], w9["_U"])
    check("G13-scramble-wrongJ",
          aS["nneg"] == S.SCR_NNEG
          and abs(aS["detK"] / S.SCR_DETK - 1.0) <= 5e-2
          and detw > 0 and w9["detK"] < 0,
          "scramble nneg=%d; wrong-J det=%+.3f"
          % (aS["nneg"], detw))


def main():
    print("=" * 72)
    print("verify_p2_determinant.py -- round 436")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("P2 DETERMINANT VERIFIED")
        return 0
    print("P2 DETERMINANT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
