#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_p1_overload.py -- machine check of every
numbered lemma in rh/problem/p1_overload.tex
(round 435, DEPTH_CHAIN_EXACT / GK_UNIVERSAL_REFUTED /
SAVE_RATE_CENSUS).

PART A (STANDALONE OVER Q):
  G1  2x2 r409 toy: D0 inertia (1,1,0), det=-3740/243
  G2  depth 2->3 lifts to PD; rank-1 PSD update
  G3  3x3 second toy nneg 2,1,0 (GK universal fails)
  G4  2x2 ND witness inertia (0,2,0), det=113/2880000
  G5  constructor audit (no eig/SVD/pack_C)

PART B (CONSTRUCTION PINS):
  G10 w9 nC curve 104 -> 43(|Y|) -> 1; hit1=178
  G11 permute nCend=20, scramble 21, two-period 4
  G12 false depth N_w-1 lifts MAIN to nC=0

Exit: "P1 OVERLOAD VERIFIED" iff every gate passed.
NO RH CLAIM.  Finite identities, one named refutation,
one named census.
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

import p1_overload_probe as P  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
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
    section("PART A  CAUCHY-PI / DEPTH LIFT / GK OVER Q")
    xs, u, ud, iX, iY, _d0, _lab = S.prime_toy()
    _S0, D0k0, _I, k0, _ = S.dressed_ITT_Q(xs, ud, iX, iY, 2)
    det = D0k0[0][0] * D0k0[1][1] - D0k0[0][1] * D0k0[1][0]
    check("G1-2x2-toy-Q",
          k0 == 0 and S.inertia_fr(D0k0) == (1, 1, 0)
          and det == P.DET_TOY and D0k0[1][1] == P.D11_TOY,
          "det=%s inertia (1,1,0)" % det)
    _S1, D01, _I1, k1, _ = S.dressed_ITT_Q(xs, ud, iX, iY, 3)
    dlt = B.fr_sub(D01, D0k0)
    check("G2-depth-lift-Q",
          k1 == 1 and S.inertia_fr(D01) == (2, 0, 0)
          and S.inertia_fr(dlt) == (1, 0, 1))
    xs3, ud3, iX3, iY3 = P.second_toy()
    inns = [S.inertia_fr(S.dressed_ITT_Q(
        xs3, ud3, iX3, iY3, d)[1])[1] for d in (3, 4, 5)]
    check("G3-3x3-GK-fail-Q", inns == [2, 1, 0],
          "nneg %s" % inns)
    xsN, udN, iXN, iYN = P.nd_toy()
    _Sn, D0n, _In, kn, _ = S.dressed_ITT_Q(xsN, udN, iXN, iYN, 2)
    detn = D0n[0][0] * D0n[1][1] - D0n[0][1] * D0n[1][0]
    check("G4-2x2-ND-Q",
          kn == 0 and S.inertia_fr(D0n) == (0, 2, 0)
          and detn == P.DET_ND,
          "det=%s inertia (0,2,0)" % detn)
    leak = []
    for fn in P.CONSTRUCTORS:
        leak.extend(P.scope_audit(fn))
    check("G5-constructor-clean",
          leak == [],
          "no eig/SVD/pack_C" if not leak else "; ".join(leak))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    r = P.world_row(mz)
    g = B.pack_graph(mz)
    check("G10-w9-curve",
          r["nC1"] == P.W9_NC1 and r["nCY"] == P.W9_NCY
          and r["nCend"] == P.W9_NCEND and r["hit1"] == P.W9_HIT1
          and r["last"] == P.W9_LAST and g["nneg"] == 1,
          "nC 104/43/1 hit1=178 last=%s" % (r["last"],))
    rP = P.world_row(P1.reweight(mz, "permute", 1000))
    rS = P.world_row(HM.scramble_mz())
    rT = P.world_row(HM.two_period_mz(21, 2.0 / 3.0))
    check("G11-adversaries",
          rP["nCend"] == P.PERM_NCEND and rP["hit1"] is None
          and rS["nCend"] == P.SCR_NCEND
          and rT["nCend"] == P.TP_NCEND
          and rT["nmax"] < rT["nY"],
          "PERM %d SCR %d 2PER %d" % (
              rP["nCend"], rS["nCend"], rT["nCend"]))
    _C, m1 = DI.chain_C(mz, n=int(mz["Nw"]) - 1)
    nC1, ev1 = P.nC_at(m1["B"], int(mz["Nw"]) - 1)
    check("G12-false-depth",
          nC1 == 0 and float(ev1[0]) > 1.0,
          "N_w-1 nC=0 cmin=%.5f" % float(ev1[0]))


def main():
    print("=" * 72)
    print("verify_p1_overload.py -- p1_overload.tex")
    print("=" * 72, flush=True)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("P1 OVERLOAD VERIFIED")
        return 0
    print("P1 OVERLOAD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
