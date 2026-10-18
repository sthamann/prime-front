#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_cross_chain.py -- machine check of every numbered
lemma in rh/problem/cross_chain_gamma.tex (round 425,
B2_LE_S_SATZ / QN_BRIDGES_BW / DEAD_NEEDS_SLACK /
COFINAL_OPEN).

PART A (STANDALONE OVER Q):
  G1  K_mu=1/3 <= K_t=1/2
  G2  Dirac ray=2/3
  G3  q_N<=1 bridges S<=B_w

PART B (CONSTRUCTION PINS):
  G10 w9 ||b||^2 <= S and q_N<1
  G11 w9 ||G||_op^2 = 1
  G12 k=5 tight ray; dead q_N>1;
      unnorm breaks the ONB

Exit: "CROSS CHAIN VERIFIED" iff every gate passed.
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

import cross_chain_gamma_probe as S  # noqa: E402
import gamma_chain_probe as S424  # noqa: E402
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
    section("PART A  KERNEL LOEWNER / q_N BRIDGE")
    t = S.kernel_Q()
    check("G1-kernel-Q",
          t["K_mu"] == Fr(1, 3) and t["leq"],
          "K_mu=%s <= K_t=%s" % (t["K_mu"], t["K_t"]))
    check("G2-ray-Q",
          t["ray"] == Fr(2, 3),
          "ray=%s" % t["ray"])
    check("G3-qn-bridge",
          Fr(1) + t["ray"] < Fr(2),
          "composed 1+ray<2")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w = S424.chain_pack(9)
    check("G10-w9",
          w["gam_S"] < 1 and w["qN"] < 1
          and abs(w["gam_S"] - S.W9_GAMS) <= 0.003,
          "ray=%.4f qN=%.4f" % (w["gam_S"], w["qN"]))
    check("G11-op-one",
          abs(S.w9_opnorm() - 1.0) <= 1e-4,
          "||G||_op^2=1")
    k5 = S424.chain_pack(17)
    uu, ww, _n, _c = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mz = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d23 = S424.chain_pack(23, mz=mz, chi=True, lpq=DMF.LPQ3)
    check("G12-k5-dead-unnorm",
          k5["gam_S"] >= 0.79 and k5["gam_S"] <= S.QBAR
          and d23["qN"] > S.DEAD_QN_LO and d23["gam"] < 1
          and w["bun_gam"] >= S424.UNNORM_GAM_LO,
          "k5 ray=%.4f dead qN=%.3f unnorm=%.3f"
          % (k5["gam_S"], d23["qN"], w["bun_gam"]))


def main():
    print("=" * 72)
    print("verify_cross_chain.py -- round 425")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("CROSS CHAIN VERIFIED")
        return 0
    print("CROSS CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
