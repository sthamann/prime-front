#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_debranges_index.py -- machine check of every
numbered lemma in rh/problem/debranges_index.tex
(round 416, PHASE_DOMINANCE_REFUTED / HB_CENSUS).

PART A (STANDALONE OVER Q):
  G1  Wronskian of the monic 3-atom X pair is -gamma_1
  G2  discriminant of p2 > 0 (interlacing)
  G3  constructor audit (no T0 / pack_graph / SVD)
  G4  toy HB both systems

PART B (CONSTRUCTION PINS):
  G10 w9 degree balance d0 = n_X < |X|-1, n_Y = q-1
  G11 w9 HB + Herglotz both; nnegT=1
  G12 w9 yyA=3 (PRIMARY FAIL of <=1); yyS=24
  G13 permute yyA=4 not many; scramble 16 != 21
  G14 MAIN-42 HB; P1 yyA<=1 only 3/28; chi death
      is fewer Ruecklaeufe

Exit: per-gate PASS/FAIL and the final line
"DEBRANGES INDEX VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named refutation.
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

import debranges_index_probe as D  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
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
    section("PART A  WRONSKIAN / INTERLACING / CONSTRUCTOR OVER Q")
    a0, a1, g1, _h0, _h1 = D.monic_X_Q()
    w0 = D.wronskian_Q(a0, a1, g1, Fr(0))
    w1 = D.wronskian_Q(a0, a1, g1, Fr(1))
    check("G1-wronskian-Q",
          w0 == w1 == -g1 and g1 > 0,
          "W=-gamma_1=%s" % (-g1,))
    disc = (a0 - a1) * (a0 - a1) + Fr(4) * g1
    check("G2-disc-Q",
          disc > 0,
          "disc=%s" % disc)
    leak = D.scope_audit("hb_pair") + D.scope_audit("hb_of")
    check("G3-constructor-clean",
          leak == [],
          "no T0/SVD/pack_graph" if not leak else "; ".join(leak))
    D.CHECKS.clear()
    D.part_satz()
    oks = dict(D.CHECKS)
    check("G4-toy-HB", oks.get("G04-toy-HB-both", False))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    d = D.pack_row(mz)
    check("G10-w9-balance",
          d["n_X"] == D.W9_NX and d["n_Y"] == D.W9_NY
          and d["d0"] == D.W9_D0 and d["nX"] == D.W9_X,
          "n_X=%d n_Y=%d d0=%d |X|=%d" % (
              d["n_X"], d["n_Y"], d["d0"], d["nX"]))
    check("G11-w9-HB-herglotz-nneg",
          d["X"]["ok"] and d["Y"]["ok"]
          and d["imX"] > 0 and d["imY"] > 0
          and d["nnegT"] == 1
          and abs(d["op"] - D.W9_OP) <= 1e-8,
          "HB both; nnegT=1 ||T||=%.6f" % d["op"])
    check("G12-w9-primary-yyA",
          d["yyA"] == D.W9_YYA and d["yyA"] > 1
          and d["yyS"] == D.W9_YYS,
          "yyA=%d yyS=%d (not <=1)" % (d["yyA"], d["yyS"]))
    dP = D.pack_row(P1.reweight(mz, "permute", 1000))
    dS = D.pack_row(HM.scramble_mz())
    check("G13-kills",
          dP["yyA"] == D.PERM_YYA and dP["nnegT"] >= D.PERM_NNEG_LO
          and dS["yyA"] == D.SCR_YYA and dS["nnegT"] == D.SCR_NNEG,
          "PERM yyA=%d nneg=%d; SCR yyA=%d nneg=%d"
          % (dP["yyA"], dP["nnegT"], dS["yyA"], dS["nnegT"]))
    core = list(V.admissible_indices())
    n_hb = p1_n = le1 = pd_n = pd0 = 0
    for kz in core:
        dd = D.pack_row(V.build_measures(kz))
        n_hb += int(dd["X"]["ok"] and dd["Y"]["ok"])
        if dd["op"] > 1.0 + 1e-9:
            p1_n += 1
            le1 += int(dd["yyA"] <= 1)
        else:
            pd_n += 1
            pd0 += int(dd["yyA"] == 0)
    dL = D.pack_row(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = D.pack_row(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G14-census-and-chi",
          n_hb == D.CORE_N and p1_n == D.P1_N and le1 == D.P1_LE1
          and pd_n == D.PD_N and pd0 == D.PD_ZERO
          and dL["yyA"] >= dD["yyA"],
          "HB %d/42; P1 yyA<=1 %d/%d; PD yyA=0 %d/%d; "
          "chi9 yyA=%d >= dead-15 yyA=%d"
          % (n_hb, le1, p1_n, pd0, pd_n, dL["yyA"], dD["yyA"]))


def main():
    print("=" * 72)
    print("verify_debranges_index.py -- round 416")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("DEBRANGES INDEX VERIFIED")
        return 0
    print("DEBRANGES INDEX FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
