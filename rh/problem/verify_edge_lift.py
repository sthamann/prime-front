#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_edge_lift.py -- machine check of every numbered
lemma in rh/problem/edge_contractive_lift.tex (round 405,
edge contractive lift, EDGE_LIFT_PARTIAL).

PART A (STANDALONE):
  G1  Euler tail over Q
  G2  omit-tail remainder z^{K+1} != 0 over Q
  G3  disk Parseval over Q
  G4  Woodbury kappa_closed identity over Q
  G5  2-point Cauchy Gram PD over Q
  G6  wrong-sign J mixed residual != 0

PART B (CONSTRUCTION PINS):
  G10 w9 geometric ones residual 0
  G11 w9 ones-split Delta>0, c2<1, kappa>0
  G12 border is not the aggregated tail
  G13 dead chi3-15 kappa<0 and c2<1
  G14 live chi3-9 kappa>0 and c2<1
  G15 scramble nneg=21; permute nneg>=15

Exit: per-gate PASS/FAIL and the final line
"EDGE LIFT VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and named refutations.
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

import edge_contractive_lift_probe as E  # noqa: E402
import mixed_haynsworth_probe as MH  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
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
    section("PART A  EULER / DISK / WOODBURY / CAUCHY / J")
    et = E.euler_tail_Q()
    check("G1-euler-tail-Q",
          et["ok"] and et["lhs"] == Fr(728, 729),
          "z=1/3 K=5 lhs=%s" % et["lhs"])
    check("G2-omit-tail-Q",
          et["rem"] == Fr(1, 3) ** 6 and et["rem"] != 0,
          "remainder z^{K+1}=%s" % et["rem"])
    dp = E.disk_parseval_Q()
    check("G3-disk-parseval-Q",
          dp["ok"] and (Fr(1) - dp["rhs"]) == Fr(1, 128),
          "reserve q^{K+1}=1/128")
    kq = E.kappa_closed_Q()
    check("G4-kappa-closed-Q",
          kq["equal"] and kq["Delta"] == Fr(7, 36),
          "Delta=%s = kappa*(-sch)" % kq["Delta"])
    detC, pdC = E.cauchy_gram_Q()
    check("G5-cauchy-gram-Q",
          pdC and detC == Fr(1, 72),
          "det=%s" % detC)
    Tm = MH.mixed_update_toy()
    check("G6-wrong-J",
          Tm["dev"] == 0 and Tm["dev_w"] > 0,
          "wrong-sign J residual %s" % Tm["dev_w"])


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w, cut, mz = E.ones_row(9)
    yn = mz["yn"]
    geo = E.geometric_ones(yn)
    check("G10-w9-E1",
          geo["res"] <= E.GEO_RES_HI,
          "ones residual %.3e" % geo["res"])
    check("G11-w9-Woodbury",
          w["Delta"] > 0 and w["c2"] < 1.0 and w["kappa"] > 0
          and abs(w["Delta"] / E.W9_DLT - 1.0) <= E.REL,
          "Delta=%.4e c2=%.5f kappa=%.4f" % (
              w["Delta"], w["c2"], w["kappa"]))
    sY = E.sm_border_Y(9, cut)
    rel_t, corr_t = E.tail_span_relres(sY, yn)
    check("G12-border-ne-tail",
          rel_t >= E.TAIL_RELRES_LO and abs(corr_t) < 0.3,
          "relres=%.3f corr=%.3f" % (rel_t, corr_t))
    wd, _c, _m = E.ones_row(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G13-dead-no-overflow",
          wd["sch"] > 0 and wd["kappa"] < 0 and wd["c2"] < 1.0,
          "sch=%+.4f c2=%.5f kappa=%.3f" % (
              wd["sch"], wd["c2"], wd["kappa"]))
    wl, _c, _m = E.ones_row(9, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G14-live-contractive",
          wl["sch"] < 0 and wl["kappa"] > 0 and wl["c2"] < 1.0,
          "sch=%.4f c2=%.5f" % (wl["sch"], wl["c2"]))
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                      mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    mz = V.build_measures(9)
    mz_p = P1.reweight(mz, "permute", 1)
    pp = P1.spec_of(mz_p, need_ref=False)
    check("G15-kills",
          oS["nneg"] == E.SCR_NNEG and pp["nneg"] >= E.PERM_NNEG_LO,
          "scramble nneg=%d perm nneg=%d" % (oS["nneg"], pp["nneg"]))


def main():
    print("verify_edge_lift.py -- round 405")
    print("NO RH CLAIM")
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("EDGE LIFT VERIFIED")
        return 0
    print("EDGE LIFT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
