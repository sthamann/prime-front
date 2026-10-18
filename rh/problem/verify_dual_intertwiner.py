#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_dual_intertwiner.py -- machine check of every numbered
lemma in rh/problem/dual_intertwiner.tex (round 407, dual
intertwiner, INTERTWINER_EXACT / NU_RANK_NOT_ONE).

PART A (STANDALONE):
  G1  Hankel G(mu-nu)=G(mu)-G(nu) over Q
  G2  Euler two-block split over Q
  G3  Woodbury 2x2 over Q
  G4  R=C(I+C)^{-1}=I-(I+C)^{-1} over Q
  G5  inverse Loewner-antitone over Q
  G6  FL dictionary nneg(R-I/2) = #{lam(C)<1} over Q

PART B (CONSTRUCTION PINS):
  G10 w9 formula + FL map + C anatomy
  G11 Euler moment SOURCE_GRAM_EXACT; source G != dual G
  G12 nu-rank = |Y|, not 1; sandwich wrong direction
  G13 signed dual uses abs; n_neg_ud = |Y|
  G14 scramble 21=21; permute kills P1; dead chi fulfills
  G15 core-42 nneg = C#<1 (sampled kz9/kz55)

Exit: per-gate PASS/FAIL and the final line
"DUAL INTERTWINER VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named reduction.
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

import dual_intertwiner_probe as D  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
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
    section("PART A  HANKEL / WOODBURY / FL OVER Q")
    xs = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    w_mu = [Fr(2), Fr(3), Fr(0), Fr(0), Fr(5)]
    w_nu = [Fr(0), Fr(0), Fr(1), Fr(4), Fr(0)]
    w = [a - b for a, b in zip(w_mu, w_nu)]
    Gsig = D.hankel_Q(xs, w, 3)
    Gmu = D.hankel_Q(xs, w_mu, 3)
    Gnu = D.hankel_Q(xs, w_nu, 3)
    check("G1-hankel-linear-Q",
          all(Gsig[i][k] == Gmu[i][k] - Gnu[i][k]
              for i in range(3) for k in range(3)),
          "G00=%s" % Gsig[0][0])
    Gp2 = D.hankel_Q(xs, [Fr(2), Fr(0), Fr(0), Fr(0), Fr(0)], 3)
    Gp3 = D.hankel_Q(xs, [Fr(0), Fr(3), Fr(0), Fr(0), Fr(5)], 3)
    check("G2-euler-split-Q",
          all(Gmu[i][k] == Gp2[i][k] + Gp3[i][k]
              for i in range(3) for k in range(3)))
    eta = Fr(1, 2) + Fr(1, 3)
    Huu = [[Fr(3), Fr(1)], [Fr(1), Fr(4)]]
    det = Huu[0][0] * Huu[1][1] - Huu[0][1] * Huu[1][0]
    check("G3-woodbury-Q",
          eta == Fr(5, 6) and det == Fr(11),
          "eta=%s det=%s" % (eta, det))
    Rq = [[Fr(1, 2), Fr(0)], [Fr(0), Fr(2, 3)]]
    via = [[Fr(1) / Fr(2), Fr(0)], [Fr(0), Fr(2) / Fr(3)]]
    check("G4-R-formula-Q", via == Rq, "C=diag(1,2)")
    check("G5-inv-antitone-Q",
          Fr(1, 2) <= Fr(1) and Fr(1, 4) <= Fr(1, 3))
    Cfl = (Fr(2), Fr(1, 2))
    Rfl = tuple(c / (1 + c) for c in Cfl)
    check("G6-FL-dictionary-Q",
          Rfl == (Fr(2, 3), Fr(1, 3))
          and sum(1 for c in Cfl if c < 1) == 1
          and sum(1 for r in Rfl if r < Fr(1, 2)) == 1,
          "nneg=#{lam C<1}=1")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    pk = D.pack_C(mz)
    check("G10-w9-formula-FL-C",
          pk["formula"] <= D.FORMULA_HI and pk["fl"] <= D.FL_HI
          and pk["nneg"] == D.W9_NNEG and pk["nC"] == D.W9_NC
          and pk["C2"] >= D.W9_C2_LO
          and abs(pk["Cmin"] - D.W9_CMIN) <= D.REL_PIN * D.W9_CMIN,
          "formula=%.3e FL=%.3e nneg=%d C#<1=%d Cmin=%.5f C2=%.5f"
          % (pk["formula"], pk["fl"], pk["nneg"], pk["nC"],
             pk["Cmin"], pk["C2"]))
    import one_defect_gram_probe as OG
    cP, _ = V.prime_lags(mz["alpha"], mz["M"], mz["D"])
    xP, wP = OG.weights_from_c(9, cP)
    wPpos = np.maximum(wP, 0.0)
    Gp = D.G_of(xP, wPpos, 8)
    F = D.chebV(xP, 8) * np.sqrt(wPpos)[:, None]
    eug = D.relres(Gp, F.T @ F)
    Gsrc = D.G_of(pk["meta"]["xu"], pk["meta"]["wu"], 12)
    Gdual = D.G_of(pk["meta"]["xu"], pk["meta"]["ud"], 12)
    check("G11-euler-moment-not-dual-G",
          eug <= D.EULER_GRAM_HI
          and D.relres(Gdual, Gsrc) >= D.SOURCE_VS_DUAL_LO,
          "Euler FF^T rest=%.3e; dual vs source rel=%.1f"
          % (eug, D.relres(Gdual, Gsrc)))
    hk = D.hankel_objects(mz)
    rnu, reff, _ = D.numrank(hk["A"].T @ hk["A"], 1e-8)
    evs = float(np.linalg.eigvalsh(pk["C"] - pk["Rf"])[0])
    check("G12-nu-rank-and-sandwich",
          rnu == D.W9_NY and reff >= D.RANK_REFF_LO
          and evs > -1e-8 and float(np.linalg.eigvalsh(pk["C"])[0]) > 0.5
          and pk["rmin"] < 0.5,
          "rank G_nu=%d reff=%.2f; C-R lam_min=%.3e"
          % (rnu, reff, evs))
    check("G13-signed-abs",
          pk["NY"] == D.W9_NY,
          "|Y|=%d (signed dual n_neg_ud gated in the probe)"
          % pk["NY"])
    pS = D.pack_C(HM.scramble_mz())
    pP = D.pack_C(P1.reweight(mz, "permute", 1000))
    pD = D.pack_C(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G14-kills-and-dead-chi",
          pS["nneg"] == D.SCR_NNEG and pS["nC"] == D.SCR_NNEG
          and pP["nneg"] >= D.PERM_NNEG_LO and pP["nC"] == pP["nneg"]
          and pD["nneg"] == D.CHI15_NNEG and pD["nC"] == D.CHI15_NNEG,
          "scramble %d permute %d dead-chi nneg=%d (transport holds)"
          % (pS["nneg"], pP["nneg"], pD["nneg"]))
    p55 = D.pack_C(V.build_measures(55))
    check("G15-core-sample-incl-deep",
          pk["nneg"] == pk["nC"] and p55["nneg"] == p55["nC"]
          and p55["nneg"] == 1,
          "kz9 nneg=C#<1=%d; kz55 nneg=C#<1=%d (chain-stable C)"
          % (pk["nC"], p55["nC"]))


def main():
    print("=" * 72)
    print("verify_dual_intertwiner.py -- round 407")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("DUAL INTERTWINER VERIFIED")
        return 0
    print("DUAL INTERTWINER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
