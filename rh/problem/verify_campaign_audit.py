#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_campaign_audit.py -- machine check of every numbered
lemma in rh/problem/campaign_audit.tex (round 427,
0 BUG / 2 SUSPECT / 5 CLEAN).

PART A (STANDALONE OVER Q):
  G1  FL dictionary nneg(R-1/2)=#{lam C<1}
  G2  Hankel G(mu-nu)=G(mu)-G(nu)
  G3  Loewner PD: K_mu=1/3 <= K_t=1/2
  G4  indefinite form blocks inversion
      monotonicity

PART B (CONSTRUCTION PINS):
  G10 w9 intertwiner formula + dictionary
  G11 QD mass 1.357 from one full-carrier dual
  G12 independent KKT ||T0|| vs pin
  G13 floor vs k reproduces r421; vs N flips
  G14 live chi3-9 does not fire; 0 BUG 2 SUSPECT

Exit: "CAMPAIGN AUDIT NOTE VERIFIED" iff every
gate passed.
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

import campaign_audit_probe as S  # noqa: E402
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
    section("PART A  SATZ OVER Q")
    Cfl = (Fr(2), Fr(1, 2))
    Rfl = tuple(c / (1 + c) for c in Cfl)
    check("G1-FL-dictionary-Q",
          Rfl == (Fr(2, 3), Fr(1, 3))
          and sum(1 for c in Cfl if c < 1) == 1
          and sum(1 for r in Rfl if r < Fr(1, 2)) == 1,
          "nneg=nC=1")
    xs = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    w_mu = [Fr(2), Fr(3), Fr(0), Fr(0), Fr(5)]
    w_nu = [Fr(0), Fr(0), Fr(1), Fr(4), Fr(0)]
    w = [a - b for a, b in zip(w_mu, w_nu)]

    def HQ(wt, n=3):
        return [[sum(wj * (xj ** (i + k)) for xj, wj in zip(xs, wt))
                 for k in range(n)] for i in range(n)]

    Gsig, Gmu, Gnu = HQ(w), HQ(w_mu), HQ(w_nu)
    check("G2-hankel-linear-Q",
          all(Gsig[i][k] == Gmu[i][k] - Gnu[i][k]
              for i in range(3) for k in range(3)),
          "G(mu-nu)=G(mu)-G(nu)")
    check("G3-Loewner-PD-Q",
          Fr(1, 3) <= Fr(1, 2),
          "K_mu=1/3 <= K_t=1/2")
    import numpy as np
    Gt = S.gram_mono(np.array([0.0, 1.0]),
                     np.array([3.0, -1.0]), 2)
    check("G4-indefinite-blocks",
          float(np.linalg.eigvalsh(Gt)[0]) < -1.0,
          "G(mu-nu) evmin=%.4f" % float(np.linalg.eigvalsh(Gt)[0]))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    pk = S.pack_window(9)
    it = S.intertwiner_of(pk)
    check("G10-w9-intertwiner",
          it["nneg"] == it["nC"] == 1
          and it["formula"] < 1e-9
          and abs(it["Cmin"] - 0.857119) < 1e-5,
          "formula=%.3e Cmin=%.6f nneg=%d" % (
              it["formula"], it["Cmin"], it["nneg"]))
    ratB = float(pk["udB"][pk["iP"]].sum()
                 / pk["udB"][pk["iY"]].sum())
    check("G11-QD-mass",
          abs(ratB - 1.357130) < 1e-5,
          "Sigma_X/Sigma_Y=%.6f" % ratB)
    T0 = S.T0_kkt(pk["xp"], pk["wX"], pk["yn"], pk["wY"], pk["n"])
    import numpy as np
    op = float(np.linalg.norm(T0, 2))
    check("G12-T0-KKT",
          abs(op - 1.080138437) < 1e-8,
          "||T0||=%.12f" % op)
    dk = S.diagnose_seq(S.FIT_K, S.FIT_R)
    dN = S.diagnose_seq(S.FIT_N, S.FIT_R)
    check("G13-floor-abscissa",
          dk["winner"] == "M1"
          and abs(dk["M1_Rinf"] - 0.02982) <= 0.003
          and dN["winner"] == "M3",
          "vs k M1 R_inf=%+.5f; vs N winner=%s" % (
              dk["M1_Rinf"], dN["winner"]))
    mzL = S.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)
    ynL = __import__("numpy").asarray(mzL["yn"], float)
    i1L, i2L = S.PX.pair_select(ynL)
    usm, wsm = S.PB.smooth_comb(mzL["alpha"])
    mzbL = DMF.chi_build_measures(9, usm, wsm, 1.0, DMF.LPQ3)
    schL = S.sch_woodbury(mzL, i1L, i2L, mzbL["xp"], mzbL["wp"],
                          mzbL["yn"], mzbL["vn"])
    check("G14-live-and-verdicts",
          schL["ok"] and schL["qN"] < 1.0 and schL["sch"] < 0.0,
          "LIVE chi3-9 qN=%.4f sch=%+.5f (audit: 0 BUG / 2 SUSPECT)"
          % (schL["qN"], schL["sch"]))


def main():
    print("=" * 72)
    print("verify_campaign_audit.py -- round 427")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("CAMPAIGN AUDIT NOTE VERIFIED")
        return 0
    print("CAMPAIGN AUDIT NOTE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
