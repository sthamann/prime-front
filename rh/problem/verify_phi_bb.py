#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_phi_bb.py -- machine check of every numbered
lemma in rh/problem/phi_bb_sign.tex (round 418,
SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT).

PART A (STANDALONE OVER Q):
  G1  P1 toy phibb = c_J + Sigma = -3
  G2  VAC toy phibb = -1
  G3  C-resolvent A0^{-1} = 2(C+I)(C-I)^{-1}
  G4  pole-save mutant toy flips
  G5  drop-border: no phibb scalar

PART B (CONSTRUCTION PINS):
  G10 w9 split + C-residual; pins
  G11 w9 defect-mutant does NOT flip
  G12 dead chi3-15 phibb<0 (pole on death), sch>0
  G13 scramble nnegA0=21; two-period >=4
  G14 MAIN-42: P1 28/28 <0, VAC 6 overflow;
      EXT-119 phibb<0; pole-saves 3/28

Exit: per-gate PASS/FAIL and the final line
"PHI BB SIGN VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, a named refutation.
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

import phi_bb_sign_probe as S  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

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
    section("PART A  SPLIT / C-RESOLVENT / MUTANT")
    t1 = S.phibb_Q_p1()
    check("G1-P1-Q",
          t1["phibb"] == Fr(-3) and t1["cJ"] == Fr(-1),
          "phibb=%s" % t1["phibb"])
    t0 = S.phibb_Q_vac()
    check("G2-VAC-Q",
          t0["phibb"] == Fr(-1) and t0["qbb"] == Fr(1, 2),
          "phibb=%s" % t0["phibb"])
    ai, tw = S.C_resolvent_Q()
    check("G3-C-resolvent-Q",
          ai == tw,
          "A0^{-1}=2(C+I)(C-I)^{-1}")
    tm = S.phibb_Q_pole_save()
    check("G4-pole-save-Q",
          tm["phibb"] == Fr(-6) and tm["noD"] == Fr(4),
          "phibb=%s noD=%s" % (tm["phibb"], tm["noD"]))
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G5-drop-border",
          nK == nA0 == 1,
          "nneg K2=%d == nneg A0" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    p = S.split_pack(9)
    check("G10-w9-identity",
          abs(p["phibb"] - (p["cJ"] + p["qbb"])) <= 1e-12
          and abs(p["phibb"] - S.W9_PHIBB) <= 0.001
          and p["dSig"] <= 1e-10 and p["P1"],
          "phibb=%.5f dSig=%.1e" % (p["phibb"], p["dSig"]))
    check("G11-w9-no-flip",
          p["phibb"] < 0 and p["phibb_noD"] < 0
          and abs(p["phibb_noD"] - S.W9_NOD) <= 0.001,
          "noD=%.5f still <0" % p["phibb_noD"])
    uu, ww, _nn, _ch = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(15, uu, ww, 1.0, DMF.LPQ3)
    c15 = S.split_pack(15, mz=mzc, chi=True, q=DMF.Q_CHI3, lpq=DMF.LPQ3)
    r15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    check("G12-dead-chi",
          c15["phibb"] < 0 and c15["D"] < -1.0
          and r15["sch"] > 0 and (not r15["shift"]),
          "phibb=%.4f D=%.3f sch=%+.4f" % (
              c15["phibb"], c15["D"], r15["sch"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G13-scramble-two-period",
          oS["nneg"] == S.SCR_NNEG and oT["nneg"] >= S.TP21_NNEG,
          "scr nneg=%d two-period nneg=%d" % (oS["nneg"], oT["nneg"]))
    core = list(V.admissible_indices())
    n_p1_neg = n_vac_pos = n_save = 0
    vac_pos = []
    saves = []
    for kz in core:
        r = S.split_pack(kz)
        if r["P1"] and r["phibb"] < 0:
            n_p1_neg += 1
        if (not r["P1"]) and r["phibb"] > 0:
            n_vac_pos += 1
            vac_pos.append(kz)
        if r["P1"] and r["phibb"] < 0 and r["phibb_noD"] >= 0:
            n_save += 1
            saves.append(kz)
    p119 = S.split_pack(119)
    check("G14-census",
          n_p1_neg == S.P1_N
          and tuple(sorted(vac_pos)) == tuple(sorted(S.VAC_POS))
          and tuple(sorted(saves)) == tuple(sorted(S.P1_SAVE))
          and p119["ok"] and p119["phibb"] < 0
          and p119["Nw"] == 1119,
          "P1 28/28 <0; VAC overflow %s; saves %s; "
          "EXT-119 N=%d phibb=%.5f"
          % (vac_pos, saves, p119["Nw"], p119["phibb"]))


def main():
    print("=" * 72)
    print("verify_phi_bb.py -- round 418")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("PHI BB SIGN VERIFIED")
        return 0
    print("PHI BB SIGN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
