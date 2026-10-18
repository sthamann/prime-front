#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_threshold_identity.py -- machine check of every
numbered lemma in rh/problem/threshold_identity.tex
(round 411, ENERGY_SPLIT_EXACT / SATURATION_REFUTED).

PART A (STANDALONE OVER Q):
  G1  T*T = C^{-1} and ||T||=1/sqrt(Cmin)
  G2  P_Y is kernel (Y-energy 0)
  G3  projection identity on K0^perp
  G4  u^vee=1/u and d0-1 break the identity

PART B (CONSTRUCTION PINS):
  G10 w9 dictionary + Fourier miss
  G11 kz42 gap (saturation REFUTED)
  G12 k=36/37 eigenvalue crossing, Klast>2
  G13 permute K-collapse; scramble; 1010
  G14 chi9 split holds / chi15 excess; death is edge

Exit: per-gate PASS/FAIL and the final line
"THRESHOLD IDENTITY VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, one named refutation.
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

import threshold_identity_probe as T  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import c_threshold_probe as CT  # noqa: E402

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
    section("PART A  DICTIONARY / KERNEL / PROJECTION OVER Q")
    # reuse the probe's Q gates by calling the constructors
    T.CHECKS.clear()
    T.part_satz()
    names = [n for n, _ok in T.CHECKS]
    oks = dict(T.CHECKS)
    check("G1-dict-Q", oks.get("G01-toy-TT-equals-Cinv", False))
    check("G2-kernel-Q", oks.get("G02-toy-PY-is-kernel", False))
    check("G3-proj-Q", oks.get("G03-toy-proj-identity", False))
    check("G4-mutants-Q",
          oks.get("G04-mustfail-uvee-without-Pprime2", False)
          and oks.get("G05-mustfail-d0-shift", False),
          "uvee and d0-1")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    d = T.dict_pack(mz)
    _s, v = T.top_right(d["g"]["T0"])
    vF, _k = T.fourier_face(d["g"]["yn"], v)
    nTF = float(np.linalg.norm(d["g"]["T0"] @ vF))
    check("G10-w9-dict-and-Fourier-miss",
          d["rest"] <= T.FORMULA_HI and d["dT"] <= T.FORMULA_HI
          and T.W9_TF_LO <= nTF <= T.W9_TF_HI,
          "||TT-Cinv||=%.3e ||T vF||=%.6f" % (d["rest"], nTF))
    d42 = T.dict_pack(V.build_measures(42))
    check("G11-kz42-gap",
          T.KZ42_GAP_LO <= d42["gap"] <= T.KZ42_GAP_HI
          and d42["g"]["opnorm"] < 1.0,
          "Cmin-1=%.3e" % d42["gap"])
    p36 = T.DI.pack_C(T.theta_prefix(mz, 36))
    p37 = T.DI.pack_C(T.theta_prefix(mz, 37))
    check("G12-k37-crossing",
          p36["nC"] == 0 and p36["Cmin"] > 1.0
          and p37["nC"] == 1 and p37["Cmin"] < 1.0,
          "k36 Cmin-1=%.3e; k37 Cmin-1=%.3e"
          % (p36["Cmin"] - 1.0, p37["Cmin"] - 1.0))
    dP = T.dict_pack(P1.reweight(mz, "permute", 1000))
    dS = T.dict_pack(HM.scramble_mz())
    d20 = T.dict_pack(CT.with_xp(HM.two_period_mz(20, 1.0)))
    C, meta = T.DI.chain_C(P1.reweight(mz, "permute", 1000))
    Kmin = float((np.diag(C) / np.maximum(
        meta["ud"][meta["iY"]], 1e-300)).min())
    check("G13-kills",
          dP["pk"]["nC"] >= T.PERM_NC_LO and Kmin <= T.PERM_KMIN_HI
          and dS["pk"]["nC"] == T.SCR_NC
          and d20["g"]["opnorm"] > 10.0,
          "PERM nC=%d Kmin=%.4f SCR nC=%d 1010 ||T||=%.1f"
          % (dP["pk"]["nC"], Kmin, dS["pk"]["nC"],
             d20["g"]["opnorm"]))
    dL = T.dict_pack(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = T.dict_pack(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G14-chi",
          dL["g"]["opnorm"] < 1.0 and dD["g"]["opnorm"] > 1.0,
          "chi9 ||T||=%.6f; dead-15 ||T||=%.6f"
          % (dL["g"]["opnorm"], dD["g"]["opnorm"]))


def main():
    print("=" * 72)
    print("verify_threshold_identity.py -- round 411")
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("THRESHOLD IDENTITY VERIFIED")
        return 0
    print("THRESHOLD IDENTITY FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
