#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_diag_lifts.py -- machine check of every
numbered lemma in rh/problem/diag_lifts_loewner.tex
(round 441, REDUZIERT).

PART A (STANDALONE OVER Q):
  G1  5-atom: Gram, L ND, lift count 1, d_min, CS
  G2  6-node: interlacing does not set L-inertia;
      d_min>1 and n_-=2 (universal REFUTED)
  G3  constructor audit

PART B (CONSTRUCTION PINS):
  G10 w9: n(WK<1)=n_-(D0)=1, nneg_diag=0, d_min
  G11 kz52: one slip (r438 razor is another depth)
  G12 PERM many slips + CHI3-9 PD / CHI3-15 one

Exit: "DIAG LIFTS VERIFIED" iff every gate passed.
NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import diag_lifts_loewner_probe as D  # noqa: E402
import residual_loewner_probe as RL  # noqa: E402
import source_potapov_probe as S  # noqa: E402
import r431_audit_probe as A  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
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
    section("PART A  GRAM / LIFT COUNT / UNIVERSAL REFUTE")
    xs, u, ud, iX, iY, d0, _ = S.prime_toy()
    t5 = RL.toy_bundle(xs, ud, iX, iY, 2)
    mt = [RL.m_tilde_Q(t5["xX"], t5["wX"], t5["ys"], y)
          for y in t5["ys"]]
    mtp = [RL.m_tilde_prime_Q(t5["xX"], t5["wX"], t5["ys"], y)
           for y in t5["ys"]]
    Lm = RL.loewner_Q(t5["ys"], mt, mtp)
    Gram = D.cauchy_gram_Q(t5["xX"], t5["wX"], t5["ys"])
    Lnm = [[-a for a in row] for row in Lm]
    dsh = D.pair_shift_Q(t5["wY"], t5["pr"])
    _ev, nb = D.n_below_minus1_Q(Lnm, dsh)
    K5 = RL.kernel_YY_Q(t5["xX"], t5["wX"], t5["ys"], 2)
    _ew, nlt = D.wk_nlt1_Q(K5, t5["wY"])
    _kii, wk = D.christoffel_diag_Q(K5, t5["wY"])
    cs = t5["S0"][0][0] * K5[0][0]
    check("G1-5atom-gram-lift",
          RL.mat_eq(Lm, Gram) and S.inertia_fr(Lnm) == (0, 2, 0)
          and nb == 1 and nlt == 1 and min(wk) == D.DMIN5
          and cs == D.CS5,
          "Gram; L ND; lift 1; dmin=%s" % D.DMIN5)
    xs2, ud2, iX2, iY2 = A.second_toy()
    t6 = RL.toy_bundle(xs2, ud2, iX2, iY2, 3)
    mt6 = [RL.m_tilde_Q(t6["xX"], t6["wX"], t6["ys"], y)
           for y in t6["ys"]]
    mtp6 = [RL.m_tilde_prime_Q(t6["xX"], t6["wX"], t6["ys"], y)
            for y in t6["ys"]]
    Lm6 = RL.loewner_Q(t6["ys"], mt6, mtp6)
    Lnm6 = [[-a for a in row] for row in Lm6]
    K6 = RL.kernel_YY_Q(t6["xX"], t6["wX"], t6["ys"], 3)
    _e, nlt6 = D.wk_nlt1_Q(K6, t6["wY"])
    _k6, wk6 = D.christoffel_diag_Q(K6, t6["wY"])
    check("G2-6node-universal-refute",
          RL.mat_eq(Lm6, D.cauchy_gram_Q(t6["xX"], t6["wX"], t6["ys"]))
          and S.inertia_fr(Lnm6) == (0, 3, 0)
          and D.x_in_yspan(t6["xX"], t6["ys"]) == 1
          and nlt6 == 2 and min(wk6) == D.DMIN6 and D.DMIN6 > 1,
          "L ND despite one X in Y-span; dmin>1 and n_-=2")
    leak = []
    for fn in D.CONSTRUCTORS:
        leak.extend(D.scope_audit(fn))
    check("G3-constructor-clean",
          leak == [],
          "no eig/SVD/pack_C/pack_graph"
          if not leak else "; ".join(leak))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    w9 = D.wk_row(B.pack_graph(V.build_measures(9)))
    check("G10-w9-wk",
          w9["n_lt1"] == 1 and w9["nneg"] == 1
          and w9["nneg_diag"] == 0
          and D.W9_DMIN_LO <= w9["dmin"] <= D.W9_DMIN_HI,
          "n_lt1=1 dmin=%.5f gap_lo=%.5f" %
          (w9["dmin"], w9["gap_lo"]))
    r52 = D.wk_row(B.pack_graph(V.build_measures(52)))
    check("G11-kz52",
          r52["n_lt1"] == 1
          and D.KZ52_DMIN_LO <= r52["dmin"] <= D.KZ52_DMIN_HI,
          "kz52 n_lt1=1 dmin=%.5f" % r52["dmin"])
    mz = V.build_measures(9)
    pP = D.wk_row(B.pack_graph(P1.reweight(mz, "permute", 1000)))
    c9 = D.wk_row(B.pack_graph(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)))
    c15 = D.wk_row(B.pack_graph(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)))
    check("G12-kills-chi",
          pP["n_lt1"] >= D.PERM_NLT1_LO and pP["dmin"] < D.PERM_DMIN_HI
          and c9["n_lt1"] == 0 and c15["n_lt1"] == 1,
          "PERM n_lt1=%d dmin=%.4f; CHI3-9/15 %d/%d"
          % (pP["n_lt1"], pP["dmin"], c9["n_lt1"], c15["n_lt1"]))


def main():
    print("=" * 72)
    print("verify_diag_lifts.py -- diag_lifts_loewner.tex")
    print("SPEC_SHA %s" % D.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("DIAG LIFTS VERIFIED")
        return 0
    print("DIAG LIFTS NOTE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
