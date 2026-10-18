#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_top_mode_edge.py -- machine check of every
numbered lemma in rh/problem/top_mode_edge.tex
(round 415, CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT).

PART A (STANDALONE OVER Q):
  G1  Euler tail
  G2  disk Parseval
  G3  alpha/beta Woodbury-Schur identity
      (beta-alpha = -sch over Q)

PART B (CONSTRUCTION PINS):
  G10 w9 Euler energy = |<1,v_top>|^2, not alpha_T
  G11 w9 v_top is not the T0 top SV
  G12 w9 chart identity + ones control = r405
  G13 live/dead chi sign split
  G14 permute/scramble bulk death; wrong omega/P'
  G15 MAIN-18 cosine; H not PD; K2 mixed both worlds

Exit: per-gate PASS/FAIL and the final line
"TOP MODE EDGE VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and named refutations.
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

import top_mode_edge_probe as T  # noqa: E402
import edge_contractive_lift_probe as E405  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402

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
    section("PART A  EULER / DISK / ALPHA-BETA OVER Q")
    et = E405.euler_tail_Q()
    check("G1-euler-tail-Q",
          et["ok"] and et["lhs"] == Fr(728, 729),
          "z=1/3 K=5 lhs=%s" % et["lhs"])
    dp = E405.disk_parseval_Q()
    check("G2-disk-parseval-Q",
          dp["ok"] and (Fr(1) - dp["rhs"]) == Fr(1, 128),
          "reserve 1/128")
    t = T.ab_identity_Q()
    check("G3-alpha-beta-Q",
          t["equal"] and t["alpha"] == Fr(-9, 8)
          and t["beta"] == Fr(-15, 4),
          "beta-alpha=%s=-sch" % t["ba"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    g = B.pack_graph(mz)
    yn, wY = g["yn"], g["wY"]
    vt = T.v_top_of(yn, wY)
    eul, ip2, _ip = T.euler_energy(yn, vt)
    alpha_T = float(vt @ (g["TT"] - np.eye(len(yn))) @ vt)
    check("G10-w9-euler-not-alpha",
          abs(eul - ip2) <= 1e-12 and alpha_T < 0.0
          and abs(eul - abs(alpha_T)) > 0.04,
          "euler=%.5f alpha_T=%.5f" % (eul, alpha_T))
    _U, _s, Vt = np.linalg.svd(g["T0"], full_matrices=False)
    cos = abs(float(np.vdot(vt, Vt[0])))
    check("G11-w9-vtop-not-SV",
          abs(cos - T.W9_COS_SV) <= 0.01 and cos < 0.72,
          "cos(v_top,v_SV)=%.4f" % cos)
    r9 = T.edge_row(9)
    wo = E405.ones_woodbury_Y(r9["A0"], r9["U"])
    kap_o = wo["Delta"] / (-r9["sch"])
    check("G12-w9-chart-and-ones",
          abs(r9["ab"]["ba"] - (-r9["sch"])) <= T.ID_RES
          and abs(wo["Delta"] - E405.W9_DLT) / E405.W9_DLT <= 0.01
          and r9["w"]["nnegH"] == 1,
          "ba=-sch; ones Delta=%.3e; nnegH=1"
          % wo["Delta"])
    rl = T.edge_row(9, chi=(DMF.Q_CHI3, DMF.LPQ3))
    rd = T.edge_row(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G13-chi-sign",
          rl["sch"] < 0 and rl["ab"]["ba"] > 0
          and rd["sch"] > 0 and rd["ab"]["ba"] < 0,
          "live ba=%.4f; dead ba=%+.4f"
          % (rl["ab"]["ba"], rd["ab"]["ba"]))
    gP = B.pack_graph(P1.reweight(mz, "permute", 1000))
    gS = B.pack_graph(HM.scramble_mz())
    c_om = abs(float(np.vdot(T.v_wrong_omega(yn, wY), Vt[0])))
    check("G14-kills",
          gP["nneg"] >= T.PERM_NNEG_LO and gS["nneg"] == T.SCR_NNEG
          and c_om < cos - 0.15,
          "PERM nneg=%d SCR nneg=%d omega-kill cos=%.4f"
          % (gP["nneg"], gS["nneg"], c_om))
    r18 = T.edge_row(18)
    check("G15-main18-and-K2",
          r18["cos_neg"] <= T.MAIN18_COS_HI
          and r9["nnegK2"] == 1 and rd["nnegK2"] == 1,
          "MAIN-18 cos=%.4f; K2 mixed live and dead"
          % r18["cos_neg"])


def main():
    print("=" * 72)
    print("verify_top_mode_edge.py -- round 415")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("TOP MODE EDGE VERIFIED")
        return 0
    print("TOP MODE EDGE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
