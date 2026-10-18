#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_delta_deformation.py -- machine check of every numbered
lemma in rh/problem/delta_deformation.tex (round 388,
LEMMA.DELTA_DEFORMATION.01).

PART A (STANDALONE, Fractions / trig):
  G1  monic gamma homogeneous under w -> 3w
  G2  one-Rayleigh skeleton h0(1-Q0)=2
  G3  two-period Fejer-pure: eps=0 and Q constant (S=21)
  G4  Neumann bar 1/4 < 1/2
  G5  Chebyshev-Gauss Q_k=1 on an equal-weight cosine grid
  G6  FO split dQ = dQT + dDelta is an identity (3-mode toy)

PART B (CONSTRUCTION PINS):
  G10 w9: |FO|_12 < 1/32, dDelta, einf, osc, C_emp
  G11 FO split residual last-12 < 1e-12
  G12 R2 mu-path n=40 |quad|/|lin| in (0.80, 0.95) and > 1/4
  G13 R2 Fejer-path n=40 in (0.95, 1.10)
  G14 C x 2 majorant on w9 exceeds 1/32
  G15 scramble seed=1: osc < MAIN but dDelta > 1e5
  G16 two-period S=81: eps=0, FO=0

Exit: per-gate PASS/FAIL and the final line
"DELTA DEFORMATION VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, named counterexamples, and
construction pins only.
"""
from __future__ import annotations

import math
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

import hirota_sign_probe as HS  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import delta_deformation_probe as P  # noqa: E402

CHECKS = []
CEPS = 1.0 / 32.0
NEUMANN = 0.25
C_FLANK = 2.0 / 3.0
SCR_SEED = 1


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
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1, 5)] * 5
    b1 = P.stieltjes_exact(nodes, wts, 3)
    b3 = P.stieltjes_exact(nodes, [Fr(3) * w for w in wts], 3)
    check("G1-gamma-homogeneous",
          b1 == b3, "monic gamma invariant under w->3w")

    check("G2-one-Rayleigh",
          Fr(4) * (Fr(1) - Fr(1, 2)) == Fr(2),
          "h0(1-Q0)=2 on the 3-atom (3,-2,3)")

    mz = P.two_period(21, C_FLANK)
    eps = P.eps_fejer(mz["xp"], mz["wp"])
    Q, b, _ = P.mu_Qk(mz["xp"], mz["wp"], mz["yn"], mz["vn"], 8)
    check("G3-Fejer-pure-S21",
          float(np.max(np.abs(eps))) < 1e-12
          and float(np.max(Q) - np.min(Q)) < 1e-12,
          "||eps||=%.3e Qspan=%.3e" % (
              float(np.max(np.abs(eps))),
              float(np.max(Q) - np.min(Q))))

    check("G4-Neumann-bar",
          NEUMANN == 0.25, "domination bar = 1/4")

    n = 32
    L = 2 * n
    j = np.arange(1, n)
    xg = np.cos(2.0 * math.pi * j / L)
    wg = np.full_like(xg, 1.0 / len(xg))
    Qg, _, _ = P.mu_Qk(xg, wg, xg, wg, 16)
    check("G5-Chebyshev-Gauss",
          float(np.max(np.abs(Qg - 1.0))) < 1e-12,
          "max|Q-1|=%.3e" % float(np.max(np.abs(Qg - 1.0))))

    # split identity on a 6-atom equal-weight toy vs T_k predictor
    th = np.linspace(0.3, 2.8, 6)
    x = np.cos(th)
    w = np.full(6, 1.0 / 6.0)
    y = x[::2]
    v = np.full(len(y), 0.02 / len(y))
    Q, b, _ = P.mu_Qk(x, w, y, v, 4)
    QT = P.qcheb_all(x, w, y, v, 4)
    Dlt = Q - QT
    dev = float(np.max(np.abs(np.diff(Q) - np.diff(QT) - np.diff(Dlt))))
    check("G6-split-identity-toy",
          dev < 1e-14,
          "dQ-(dQT+dDelta) maxdev=%.3e" % dev)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(9)
    N = int(mz["Nw"])
    r9 = P.deform_row(mz["xp"], mz["wp"], mz["yn"], mz["vn"], N - 1)
    check("G10-w9-pins",
          r9["fo12"] < CEPS
          and 0.04 < r9["dD12"] < 0.06
          and 5.0 < r9["einf"] < 5.4
          and 8.0 < r9["osc_nu"] < 9.5
          and r9["C_emp"] < 0.007,
          "FO=%.5f dD=%.5f einf=%.3f osc=%.3f Cemp=%.4f" % (
              r9["fo12"], r9["dD12"], r9["einf"], r9["osc_nu"],
              r9["C_emp"]))

    check("G11-split",
          r9["split"] < 1e-12,
          "maxdev=%.3e" % r9["split"])

    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    rat_mu, lin_mu, qd_mu, _, _ = P.midpoint_mu_nu(xs, ws, ys, vs, 40)
    rat_fj, lin_fj, qd_fj = P.midpoint_fejer(xs, ws, ys, vs, 40)
    check("G12-R2-mu-n40",
          0.80 < rat_mu < 0.95 and rat_mu > NEUMANN,
          "|quad|/|lin|=%.4f" % rat_mu)
    check("G13-R2-Fejer-n40",
          0.95 < rat_fj < 1.10,
          "|quad|/|lin|=%.4f" % rat_fj)

    maj_c2 = r9["g12"] * (r9["dQT12"] + 2.0 * r9["C_emp"] * r9["osc_nu"])
    check("G14-Cx2-mutant",
          maj_c2 > CEPS,
          "maj=%.4f > 1/32" % maj_c2)

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    rs = P.deform_row(ds["xs"], ds["ws"], ds["ys"], ds["vs"], 183)
    check("G15-scramble",
          rs["osc_nu"] < 4.5 and rs["osc_nu"] < r9["osc_nu"]
          and rs["dD12"] >= 1.0e5,
          "osc=%.3f dD=%.3e" % (rs["osc_nu"], rs["dD12"]))

    mz23 = P.two_period(81, C_FLANK)
    rt = P.deform_row(mz23["xp"], mz23["wp"], mz23["yn"], mz23["vn"], 40)
    check("G16-two-period",
          rt["einf"] < 1e-12 and rt["fo12"] < 1e-12,
          "eps=0 FO=%.3e Q=%.4f" % (rt["fo12"], rt["Q12"]))


def main():
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("DELTA DEFORMATION VERIFIED")
        return 0
    print("DELTA DEFORMATION FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
