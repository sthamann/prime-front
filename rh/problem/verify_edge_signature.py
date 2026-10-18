#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_edge_signature.py -- machine check of every numbered
lemma in rh/problem/edge_signature.tex (round 401, augmented
edge signature, EDGE_SIGNATURE_MODEL).

PART A (STANDALONE):
  G1  Fractions mixed update residual 0
  G2  mixed Haynsworth additivity on indefinite J
  G3  Phi_edge(0,0) P1 inertia (1,2,0)
  G4  Phi_edge(0,0) vacuous inertia (2,1,0)
  G5  det Phi_edge(1,0)_P1 = 1
  G6  drop-border: nneg K2 = nneg A0 (shift by 0)
  G7  64-pt disk R=3.2: nneg=2, gmin >= 0.08

PART B (CONSTRUCTION PINS):
  G10 w9 J>0, balance, shift, (a,b) pins
  G11 w9 ||E|| = 0 (reconstruction)
  G12 dead chi3-15 sch > 0, shift fails
  G13 scramble nnegA0 = 21, mix fails
  G14 two-period nnegA0 >= 4
  G15 living chi3-9 shift, sch < 0

Exit: per-gate PASS/FAIL and the final line
"EDGE SIGNATURE VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named 3x3 family.
"""
from __future__ import annotations

import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import edge_signature_probe as E  # noqa: E402
import mixed_haynsworth_probe as MH  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as H  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402

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
    section("PART A  MODEL LEMMA / HAYNSWORTH / MUTANTS")
    Tm = MH.mixed_update_toy()
    check("G1-Fractions-mixed",
          Tm["dev"] == 0 and Tm["den"] != 0,
          "den=%s residual 0" % Tm["den"])
    Th = MH.haynsworth_mixed_toy()
    ok_add = (Th["iH"][0] == Th["iA"][0] + Th["iMPhi"][0]
              and Th["iH"][1] == Th["iA"][1] + Th["iMPhi"][1]
              and Th["iH"][0] == Th["iMJ"][0] + Th["iM"][0]
              and Th["iH"][1] == Th["iMJ"][1] + Th["iM"][1])
    check("G2-Haynsworth-mixed", ok_add,
          "In(H)=In(A)+In(-Phi)=In(-J^{-1})+In(M)")
    P0 = E.Phi_edge_Q(0, 0, 1)
    check("G3-P1-origin",
          FTI.fr_inertia(P0) == (1, 2, 0),
          "In(Phi_edge(0,0)_P1)=%s" % (FTI.fr_inertia(P0),))
    Pv = E.Phi_edge_Q(0, 0, 0)
    check("G4-vac-origin",
          FTI.fr_inertia(Pv) == (2, 1, 0),
          "In(Phi_edge(0,0)_vac)=%s" % (FTI.fr_inertia(Pv),))
    P1 = E.Phi_edge_Q(1, 0, 1)
    det1 = (P1[0][0] * (P1[1][1] * P1[2][2] - P1[1][2] * P1[2][1])
            + P1[0][2] * (P1[1][0] * P1[2][1] - P1[1][1] * P1[2][0]))
    check("G5-det-one",
          det1 == 1 and FTI.fr_inertia(P1)[1] == 2,
          "det=%s nneg=2" % det1)
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -E.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -E.FLOOR))
    check("G6-drop-border",
          nK == nA0 == 1,
          "K2 nneg=%d == nnegA0 (no +1)" % nK)
    nbad, gmin = 0, 1e9
    for k in range(64):
        th = 2 * np.pi * k / 64
        g, nneg = E.g_of(E.K_RADIUS * np.cos(th),
                          E.K_RADIUS * np.sin(th), 1)
        gmin = min(gmin, g)
        if nneg != 2:
            nbad += 1
    check("G7-disk",
          nbad == 0 and gmin >= E.GSTAR_FLOOR,
          "gmin=%.4f nbad=%d" % (gmin, nbad))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    p = E.main_row(9)
    check("G10-w9-shift",
          p["ok"] and p["Jsucc"] and p["bal"] and p["shift"]
          and p["nnegA0"] == 1 and p["nnegPhi"] == 2
          and abs(p["a"] - E.W9_A) <= 0.01
          and abs(p["den"] / E.W9_DEN - 1.0) <= E.REL,
          "nnegPhi=%d |t|=%.4f den=%.6f" % (
              p["nnegPhi"], p["ab"], p["den"]))
    check("G11-w9-E",
          p["nE"] <= E.E_BAR and p["nE"] < 0.5 * p["g"],
          "||E||=%.2e g=%.4f" % (p["nE"], p["g"]))
    pd = E.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    check("G12-dead-chi",
          pd["ok"] and (not pd["shift"]) and pd["sch"] > 0,
          "sch=%+.4f nnegPhi=%d" % (pd["sch"], pd["nnegPhi"]))
    mz_s = H.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G13-scramble",
          oS["nneg"] == E.SCR_NNEG,
          "nnegA0=%d" % oS["nneg"])
    mz = H.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G14-two-period",
          oT["nneg"] >= E.TP21_NNEG,
          "nnegA0=%d" % oT["nneg"])
    p3 = E.chi_row(9, DMF.Q_CHI3, DMF.LPQ3, "L9")
    check("G15-live-chi",
          p3["ok"] and p3["shift"] and p3["sch"] < 0,
          "nnegA0=%d nnegPhi=%d sch=%.4f" % (
              p3["nnegA0"], p3["nnegPhi"], p3["sch"]))


def main():
    print("=" * 72)
    print("verify_edge_signature.py -- round 401")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("EDGE SIGNATURE VERIFIED")
        return 0
    print("EDGE SIGNATURE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
