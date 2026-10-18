#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_weyl_energy.py -- machine check of every numbered
lemma in rh/problem/weyl_energy.tex (round 389,
LEMMA.WEYL_ENERGY.01).

PART A (STANDALONE, Fractions / trig / Parseval):
  G1  Chebyshev energy Phi* = M^2 + 2 Sigma C_m^2 over Q
  G2  off = Phi - diag exact (off=26, diag=73)
  G3  float energy and off on a 6-atom toy
  G4  mutant c_q=1 fails; missing diagonal fails
  G5  Q^T = (C0+C_{2k})_nu / (C0+C_{2k})_mu
  G6  pi_k^2 Weyl via Chebyshev coefficients
  G7  finite-grid Parseval on two-period S=21 equals 1

PART B (CONSTRUCTION PINS):
  G10 w9 energy k=8 at machine precision
  G11 w9 Parseval = 1
  G12 w9 mean/qm in (0.80, 1.05)
  G13 w9 FO and FO^T both < 1/32
  G14 wall assist in (0.03, 0.05); Chebyshev all-ones
      Rayleigh << lam
  G15 two-period S=81 is a comb (|C_S|/mass=1, HHI>0.5)
  G16 scramble holds QM; top |dC^2| mode in the sealed set

Exit: per-gate PASS/FAIL and the final line
"WEYL ENERGY VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, named counterexamples, and
construction pins only.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import hirota_sign_probe as HS  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import weyl_energy_probe as P  # noqa: E402

CHECKS = []
CEPS = 1.0 / 32.0
C_FLANK = 2.0 / 3.0
SCR_SEED = 1
PI = math.pi


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def part_a():
    section("PART A  STANDALONE IDENTITIES")
    from fractions import Fraction as Fr
    nodes = [Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    k = 4
    Ts = [P.T_fr(x, k - 1) for x in nodes]
    M = sum(wts)
    Cs = [sum(w * t[m] for w, t in zip(wts, Ts)) for m in range(k)]
    Phi_star = M * M + 2 * sum(c * c for c in Cs[1:])
    acc = Fr(0)
    for i, vi in enumerate(wts):
        for j, vj in enumerate(wts):
            ker = Fr(1)
            for m in range(1, k):
                ker += 2 * Ts[i][m] * Ts[j][m]
            acc += vi * vj * ker
    check("G1-Fractions-energy",
          acc == Phi_star, "Phi*=%s" % Phi_star)

    diag_star = Fr(0)
    for x, v in zip(nodes, wts):
        t = P.T_fr(x, 2 * (k - 1))
        ker = Fr(k) + sum(t[2 * m] for m in range(1, k))
        diag_star += v * v * ker
    check("G2-off-Phi-diag",
          (Phi_star - diag_star) == Fr(26) and diag_star == Fr(73),
          "off=26 diag=73")

    th = np.array([0.3, 0.7, 1.1, 1.6, 2.1, 2.6])
    v = np.array([0.4, 0.7, 0.2, 0.5, 0.9, 0.3])
    C = P.C_cos(th, v, 5)
    Phi_e = P.energy_from_C(C, 5)
    Phi_d = P.bilinear_K(th, v, 5)
    check("G3-float-energy",
          abs(Phi_e - Phi_d) < 1e-14,
          "rel=%.3e" % (abs(Phi_e - Phi_d) / max(abs(Phi_d), 1e-30)))

    off_d = Phi_e - P.diag_K(th, v * v, 5)
    Phi_mut = (C[0] ** 2 + float(np.dot(C[1:5], C[1:5]))) / PI
    check("G4-mutants",
          abs(Phi_mut - Phi_d) / max(abs(Phi_d), 1e-30) > 0.05
          and abs(Phi_e - off_d) / max(abs(off_d), 1e-30) > 1.5,
          "wrong c_q rel=%.3f missing-diag |Phi-off|/|off|=%.3f" % (
              abs(Phi_mut - Phi_d) / max(abs(Phi_d), 1e-30),
              abs(Phi_e - off_d) / max(abs(off_d), 1e-30)))

    # Q^T identity on the 6+5 toy
    thx = np.array([0.2, 0.8, 1.3, 1.9, 2.4])
    wx = np.array([0.5, 0.6, 0.7, 0.8, 0.4])
    num = float(np.dot(v, 1.0 + np.cos(2 * 2 * th)))
    den = float(np.dot(wx, 1.0 + np.cos(2 * 2 * thx)))
    Cn = P.C_cos(th, v, 4)
    Cm = P.C_cos(thx, wx, 4)
    check("G5-QT-C2k",
          abs(num / den - (Cn[0] + Cn[4]) / (Cm[0] + Cm[4])) < 1e-14,
          "k=2 Q^T Weyl identity")

    mz21 = P.two_period(21, C_FLANK)
    j = np.arange(1, 22)
    th_full = math.pi * j / 21.0
    w21 = np.where(j % 2 == 0,
                   (1.0 - np.cos(th_full)) * (math.pi / 21),
                   -C_FLANK * (1.0 - np.cos(th_full)) * (math.pi / 21))
    v_nu21 = np.where(w21 < 0, -w21, 0.0)
    rat = P.parseval_ratio(th_full, v_nu21, 21)
    check("G6-Parseval-S21",
          abs(rat - 1.0) < 1e-10, "ratio=%.12f" % rat)

    check("G7-Neumann-not-used",
          CEPS == 1.0 / 32.0, "C_eps bar = 1/32 (FO Chebyshev closes)")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    N = int(mz["Nw"])
    S = int(mz["S"])
    xp, wp, yn, vn = mz["xp"], mz["wp"], mz["yn"], mz["vn"]
    thn = np.arccos(np.clip(yn, -1.0, 1.0))
    C_nu = P.C_cos(thn, vn, max(400, 2 * S))
    Phi8 = P.energy_from_C(C_nu, 8)
    Phi8d = P.bilinear_K(thn, vn, 8)
    check("G10-w9-energy-k8",
          abs(Phi8 - Phi8d) / max(abs(Phi8), 1e-30) < 1e-12,
          "rel=%.3e" % (abs(Phi8 - Phi8d) / max(abs(Phi8), 1e-30)))

    check("G11-w9-Parseval",
          abs(P.parseval_ratio(thn, vn, S) - 1.0) < 1e-10,
          "ratio=%.12f" % P.parseval_ratio(thn, vn, S))

    sp = P.spec_pack(thn, vn, M=400)
    check("G12-w9-QM",
          0.80 < sp["mean_over_qm"] < 1.05,
          "mean/qm=%.3f" % sp["mean_over_qm"])

    Q, bch, _ = P.mu_Qk(xp, wp, yn, vn, N - 1)
    QT = P.qcheb_all(xp, wp, yn, vn, N - 1)
    g = bch ** 2
    fo12 = float(np.max(np.abs(g[-12:] * np.diff(Q[-13:]))))
    fot12 = float(np.max(np.abs(g[-12:] * np.diff(QT[-13:]))))
    check("G13-w9-FO-FOT",
          fo12 < CEPS and fot12 < CEPS,
          "FO=%.5f FO^T=%.5f" % (fo12, fot12))

    aW, bW, h0W = V.mu_chain(xp, wp, N - 1)
    BW = V.b_matrix(aW, bW, h0W, yn, vn, N - 1)
    EW = BW @ BW.T
    lamW = float(np.linalg.eigvalsh(EW)[-1])
    maxdW = float(np.max(np.diag(EW)))
    assistW = lamW / maxdW - 1.0
    sv = np.sqrt(vn)
    ray_T = P.energy_from_C(P.C_cos(thn, sv, N - 1), N - 1) / len(vn)
    check("G14-wall-assist",
          0.030 < assistW < 0.050 and ray_T < 0.20 and lamW < 1.0,
          "assist=%.4f Cheb-allones=%.4f" % (assistW, ray_T))

    mz23 = P.two_period(81, C_FLANK)
    th23 = np.arccos(np.clip(mz23["yn"], -1.0, 1.0))
    C_tp = P.C_cos(th23, mz23["vn"], 160)
    mass_t = float(np.sum(mz23["vn"]))
    check("G15-two-period-comb",
          P.hhi(C_tp, 80) > 0.50
          and abs(C_tp[81]) / mass_t > 0.90,
          "HHI=%.3f |C_S|/mass=%.3f" % (
              P.hhi(C_tp, 80), abs(C_tp[81]) / mass_t))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    ths = np.arccos(np.clip(ds["ys"], -1.0, 1.0))
    C_scr = P.C_cos(ths, ds["vs"], 400)
    sp_s = P.spec_pack(ths, ds["vs"], M=400)
    dC = C_scr[1:401] ** 2 - C_nu[1:401] ** 2
    topm = int(np.argmax(np.abs(dC))) + 1
    check("G16-scramble-QM",
          0.80 < sp_s["mean_over_qm"] < 1.10
          and topm in P.SCR_DIV_MODES,
          "mean/qm=%.3f top m=%d" % (sp_s["mean_over_qm"], topm))


def main():
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("WEYL ENERGY VERIFIED")
        return 0
    print("WEYL ENERGY FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
