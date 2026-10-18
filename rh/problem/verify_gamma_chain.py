#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_gamma_chain.py -- machine check of every numbered
lemma in rh/problem/gamma_chain.tex (round 424,
BESSEL_EXACT / W_TERM_REFUTED / SHARP_CENSUS /
GAMMA_OPEN).

PART A (STANDALONE OVER Q):
  G1  Bessel leftover: ||b||^2=1 < 16/9
  G2  bookkeeping gamma=7/13<1
  G3  1+gamma<2

PART B (CONSTRUCTION PINS):
  G10 w9 Parseval ||b||^2 == mu_side
  G11 w9 w_k not uniform (frac>1, wmax>>1)
  G12 kz26 gamma<1 and gam_S<0.80
  G13 dead gamma<1; scramble border_fail;
      unnorm gamma>1

Exit: "GAMMA CHAIN VERIFIED" iff every gate passed.
NO RH CLAIM.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import gamma_chain_probe as S  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
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
    section("PART A  BESSEL / GAMMA BOOKKEEPING")
    t = S.bessel_Q()
    check("G1-bessel-Q",
          t["b2"] == Fr(1) and t["phi2"] == Fr(16, 9)
          and t["b2"] < t["phi2"],
          "||b||^2=%s < %s" % (t["b2"], t["phi2"]))
    check("G2-gamma-Q",
          t["gam"] == Fr(7, 13) and t["gam"] < Fr(1),
          "gam=%s" % t["gam"])
    check("G3-drop-vts",
          Fr(1) + t["gam"] < Fr(2),
          "1+gam<2")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S.chain_pack(9)
    check("G10-parseval",
          w["dmsb"] <= 1e-10 and w["gam"] < 1
          and abs(w["b2"] - S.W9_B2) <= 0.002,
          "b2=%.4f dmsb=%.1e" % (w["b2"], w["dmsb"]))
    check("G11-wterm",
          w["frac_gt1"] >= 0.35 and w["wmax"] > 10.0
          and w["w0"] < 1.0,
          "frac>1=%.2f wmax=%.1e" % (w["frac_gt1"], w["wmax"]))
    h = S.chain_pack(26)
    check("G12-kz26",
          h["gam"] < 1 and h["gam_S"] < S.QBAR,
          "gam=%.4f gamS=%.4f" % (h["gam"], h["gam_S"]))
    uu, ww, _nn, _ch = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d23 = S.chain_pack(23, mz=mzc, chi=True, lpq=DMF.LPQ3)
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    scr = S.chain_pack(0, mz=mz_s)
    check("G13-dead-scramble-unnorm",
          d23["ok"] and d23["gam"] < 1
          and oS["nneg"] == S.SCR_NNEG and (not scr.get("ok"))
          and w["bun_gam"] >= S.UNNORM_GAM_LO,
          "dead gam=%.4f scr fail unnorm=%.3f"
          % (d23["gam"], w["bun_gam"]))


def main():
    print("=" * 72)
    print("verify_gamma_chain.py -- round 424")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("GAMMA CHAIN VERIFIED")
        return 0
    print("GAMMA CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
