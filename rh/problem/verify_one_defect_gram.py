#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_one_defect_gram.py -- machine check of every numbered
lemma in rh/problem/one_defect_gram.tex (round 404, source
one-defect Gram, CLASS 3 not reached).

PART A (STANDALONE):
  G1  Chebyshev addition over Q
  G2  Cauchy kernel telescopes over Q
  G3  Loewner identity (psi vs nsum, mpmath)
  G4  folded weights linear in lags

PART B (CONSTRUCTION PINS):
  G10 FRAME-A inertia / Gram / Q^T A0 Q PD
  G11 no Fourier k-subset recovers Vn
  G12 Euler Gram is not M; Loewner Gram is not A0
  G13 only-Gram leaves 13; cross share
  G14 Cholesky tautology on MAIN; permute M not PD
  G15 ones-mode is not the defect
  G16 mutants stay O(1)

Exit: per-gate PASS/FAIL and the final line
"ONE DEFECT GRAM VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and one named class audit.
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

import one_defect_gram_probe as G  # noqa: E402
import p1_construction_probe as P  # noqa: E402
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
    section("PART A  ADDITION / LOEWNER / FOLD")
    x = Fr(3, 7)
    T0, T1 = Fr(1), x
    T2 = 2 * x * T1 - T0
    T3 = 2 * x * T2 - T1
    check("G1-chebyshev-Q",
          2 * T2 * T1 == T3 + T1,
          "T2 T1=(T3+T1)/2")
    z, w, m = Fr(1, 4), Fr(3, 4), Fr(2)
    check("G2-cauchy-Q",
          1 / ((m + z) * (m + w))
          == (1 / (z - w)) * (1 / (m + w) - 1 / (m + z)),
          "kernel telescopes")
    import mpmath as mp
    mp.mp.dps = 40
    zz = mp.mpc("1/4", "7/10")
    ww = mp.mpc("1/4", "-3/10")
    lhs = ((mp.digamma(zz) - mp.conj(mp.digamma(ww)))
           / (zz - mp.conj(ww)))
    rhs = mp.nsum(lambda k: 1 / ((k + zz) * (k + mp.conj(ww))),
                  [0, mp.inf])
    check("G3-loewner-psi",
          float(abs(lhs - rhs)) <= G.LOEWNER_MP_HI,
          "|psi-nsum|=%.3e" % float(abs(lhs - rhs)))
    mz = V.build_measures(9)
    cP, _ = V.prime_lags(mz["alpha"], mz["M"], mz["D"])
    cA = V.arch_lags(mz["M"], mz["D"])
    _x, wP = G.weights_from_c(9, cP)
    _x, wA = G.weights_from_c(9, cA)
    _x, wF = G.weights_from_c(9, cP + cA)
    lin = float(np.linalg.norm(wF - (wP + wA))) / (
        float(np.linalg.norm(wF)) + 1e-30)
    check("G4-fold-linear",
          lin <= G.FOLD_LIN_HI,
          "rel=%.3e" % lin)
    return mz


def part_b(mz):
    section("PART B  CLASS-AUDIT PINS")
    pk = G.pack_ref(mz)
    g = P.gram_of(mz)
    Vn, M, yn = pk["Vn"], pk["M"], pk["yn"]
    evQ = np.linalg.eigvalsh(pk["QA0"])
    check("G10-w9-PD-compression",
          pk["nneg"] == G.W9_NNEG and pk["nneg_ref"] == G.W9_NNEG_REF
          and g["nneg_M"] == 0 and int(np.sum(evQ < -1e-12)) == 0
          and float(evQ[0]) >= G.QMIN_LO,
          "nneg=%d nneg_ref=%d QA0_min=%.4e"
          % (pk["nneg"], pk["nneg_ref"], float(evQ[0])))
    Ublk = G.chebU_on_Y(yn, 1, 1 + pk["nneg_ref"])
    ang = G.prin_maxang_deg(Ublk, Vn)
    check("G11-no-fourier-subset",
          ang >= G.MAXANG_LO,
          "first-49 U maxang=%.1f deg" % ang)
    Fe = G.euler_F(mz, yn)
    rE = G.relres(Vn.T @ (Fe @ Fe.T) @ Vn, M)
    Fg = G.cauchy_F(yn, 0.25, 80)
    rL = G.relres(Fg @ Fg.T, pk["A0"])
    aE = G.align_fro(Vn.T @ (Fe @ Fe.T) @ Vn, M)
    check("G12-euler-loewner-not-exact",
          rE >= G.REL_EULER_LO and rL >= G.REL_LOEWNER_LO
          and G.ALIGN_EULER_LO <= aE <= G.ALIGN_EULER_HI,
          "Euler rel=%.1f align=%.3f; Loewner-vs-A0 rel=%.1f"
          % (rE, aE, rL))
    Pneg = Vn @ Vn.T
    share = float(np.linalg.norm(pk["B"] - Pneg @ pk["B"] @ Pneg)) / (
        float(np.linalg.norm(pk["B"])) + 1e-30)
    check("G13-onlyGram-cross",
          g["nneg_gram"] == G.W9_ONLYGRAM and share >= G.CROSS_SHARE_LO,
          "only-Gram=%d cross=%.3f" % (g["nneg_gram"], share))
    rest = G.cholesky_tautology_control(M)
    gP = P.gram_of(P.reweight(mz, "permute", 1000))
    check("G14-cholesky-tautology",
          rest <= G.CHOL_REST_HI and gP["nneg_M"] >= G.PERM_NNEG_M_LO,
          "chol rest=%.3e permute nneg_M=%d" % (rest, gP["nneg_M"]))
    ones = np.ones(pk["n"])
    cos1 = abs(float(pk["vneg"] @ ones)) / (
        float(np.linalg.norm(pk["vneg"]) * np.linalg.norm(ones)) + 1e-30)
    cosVn = float(np.linalg.norm(Vn.T @ pk["vneg"]))
    check("G15-null-not-ones",
          cos1 <= G.COS_ONES_HI and G.COS_VN_LO <= cosVn <= G.COS_VN_HI,
          "|cos|(v-,1)=%.4f |cos|(v-,Vn)=%.3f" % (cos1, cosVn))
    rng = np.random.default_rng(404)
    ka = int(mz["ka"])
    lam_p = V.LAM.copy()
    pp = np.asarray(V.PP[:ka], int)
    lam_p[pp] = rng.permutation(lam_p[pp])
    rP = G.relres(Vn.T @ (G.euler_F(mz, yn, lam=lam_p)
                          @ G.euler_F(mz, yn, lam=lam_p).T) @ Vn, M)
    check("G16-mutant-perm-O1",
          rP >= G.MUT_REL_LO,
          "Lambda-perm Euler rel=%.1f (MAIN %.1f)" % (rP, rE))


def main():
    print("=" * 72)
    print("verify_one_defect_gram.py -- round 404")
    print("=" * 72)
    mz = part_a()
    part_b(mz)
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s" % (
        n_ok, len(CHECKS), "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("ONE DEFECT GRAM VERIFIED")
        return 0
    print("ONE DEFECT GRAM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
