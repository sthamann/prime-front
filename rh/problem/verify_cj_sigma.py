#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_cj_sigma.py -- machine check of every numbered
lemma in rh/problem/cj_sigma.tex (round 420,
DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS / COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  den = 1+gam-vts = 3/2
  G2  den<2
  G3  drop-border

PART B (CONSTRUCTION PINS):
  G10 w9 den identity + pins
  G11 kz26 healthy R>0; naive bound loose
  G12 kz12 overflow R<0
  G13 dead VAC both sides; scramble
  G14 CORE den<2; OKV R>0 OVF R<0;
      selected k=4..9 all R>0 shrinking

Exit: "CJ SIGMA VERIFIED" iff every gate passed.
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

import cj_sigma_probe as S  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
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
    section("PART A  den FORMULA / DROP-BORDER")
    t = S.den_Q()
    check("G1-den-Q",
          t["den"] == Fr(3, 2) and t["cJ"] == Fr(-1, 2),
          "den=%s" % t["den"])
    check("G2-den-lt-2",
          t["den"] < Fr(2),
          "den<2")
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -S.FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -S.FLOOR))
    check("G3-drop-border", nK == nA0 == 1, "nneg=%d" % nK)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.den_pack(9)
    check("G10-w9",
          abs(w["den"] - (1.0 + w["gam"] - w["vts"])) <= 1e-12
          and abs(w["den"] - S.W9_DEN) <= 0.001
          and w["reserve"] > 0,
          "den=%.5f R=%.5f" % (w["den"], w["reserve"]))
    h = S.den_pack(26)
    check("G11-kz26",
          h["reserve"] > 0 and h["bound_ratio"] > 50
          and (not h["P1"]),
          "R=%.5f bound/Sig=%.0f" % (h["reserve"], h["bound_ratio"]))
    o = S.den_pack(12)
    check("G12-kz12",
          o["reserve"] < 0 and (not o["P1"]),
          "R=%.5f" % o["reserve"])
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    c23 = S417.chart_from_row(p23)
    tau2 = c23["a_un"] ** 2 + c23["b_un"] ** 2
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G13-dead-scramble",
          c23["phibb"] > 0 and tau2 < c23["phibb"]
          and oS["nneg"] == S.SCR_NNEG,
          "dead phibb=%+.4f scr nneg=%d" % (c23["phibb"], oS["nneg"]))
    n_okv = n_ovf = 0
    dens = []
    for kz in V.admissible_indices():
        r = S418.split_pack(kz)
        dens.append(r["den"])
        if (not r["P1"]) and r["phibb"] < 0:
            n_okv += 1
        if (not r["P1"]) and r["phibb"] > 0:
            n_ovf += 1
    p26 = S418.split_pack(26)
    p43 = S418.split_pack(43)
    p116 = S418.split_pack(116)
    check("G14-census",
          all(d < 2 for d in dens) and n_okv == S.OKV_N
          and n_ovf == S.OVF_N
          and p26["phibb"] < 0 and p43["phibb"] < 0
          and p116["phibb"] < 0
          and (-p26["phibb"]) > (-p43["phibb"]) > (-p116["phibb"]),
          "den<2; OKV %d OVF %d; selected R shrinks"
          % (n_okv, n_ovf))


def main():
    print("=" * 72)
    print("verify_cj_sigma.py -- round 420")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("CJ SIGMA VERIFIED")
        return 0
    print("CJ SIGMA FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
