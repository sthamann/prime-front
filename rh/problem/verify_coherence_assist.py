#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_coherence_assist.py -- machine check of every numbered
lemma in rh/problem/coherence_assist.tex (round 387,
LEMMA.COHERENCE_ASSIST.01).

PART A (STANDALONE):
  G1  Chebyshev-T CD = Dirichlet combination
  G2  lambda = maxdiag*(1+assist) on [[2,1],[1,2]]
  G3  Gershgorin equals lambda on that 2x2
  G4  two-period S=21 is a global AP (rho_AP=1)
  G5  cosine mesh step = pi/S
  G6  1/3 < 3/8 (floor does not upgrade nu-gaps)

PART B (CONSTRUCTION PINS):
  G10 w9 k_gersh=21 < n0=73
  G11 w9 k=183 maxdiag in (0.95,0.97), assist in (0.03,0.05),
      lam<1, cancellation > 0.99
  G12 w9 rho_AP<0.10, cv>0.70, dmin/dmed=1/3, dmin=1 mesh
  G13 Dirichlet max-row k=22: source<0.35, TP>0.80
  G14 two-period c=2/3: rho_AP=1, Q in (0.68,0.69), lam22>1
  G15 scramble: k_lam in [20,25], k_maxd in [45,55], rho_AP<0.10
  G16 c=1 lam1>1; clustered run-3 k_lam < n0 and rho_AP=1

Exit: per-gate PASS/FAIL and the final line
"COHERENCE ASSIST VERIFIED" iff every gate passed.

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

import coherence_assist_probe as P  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402

CHECKS = []


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
    ok = True
    for n, th, ph in ((5, 0.3, 1.1), (12, 0.7, 0.7), (8, 0.0, math.pi)):
        if abs(P.cheb_K_closed(n, th, ph) - P.cheb_K_sum(n, th, ph)) > 1e-12:
            ok = False
    check("G1-Chebyshev-CD-Dirichlet", ok)

    E = np.array([[2.0, 1.0], [1.0, 2.0]])
    lam = float(np.linalg.eigvalsh(E)[-1])
    maxd = float(np.max(np.diag(E)))
    assist = lam / maxd - 1.0
    gersh = float(np.max(np.sum(np.abs(E), axis=1)))
    check("G2-bookkeeping",
          abs(lam - 3.0) < 1e-12 and abs(assist - 0.5) < 1e-12
          and abs(lam - maxd * (1.0 + assist)) < 1e-12)
    check("G3-Gershgorin",
          abs(gersh - 3.0) < 1e-12 and gersh >= lam - 1e-15)

    mz = P.two_period(21, P.C_FLANK)
    ap = P.angle_pack(mz["yn"], 21)
    d = np.diff(np.sort(ap["th"]))
    uniq = len(np.unique(np.round(d, 8)))
    check("G4-two-period-global-AP",
          ap["frac"] == 1.0 and ap["ap"] == ap["n"] and uniq == 1)

    S = 16
    j = np.array([3, 4])
    th = np.arccos(np.cos(math.pi * j / S))
    check("G5-mesh-pi-over-S",
          abs(abs(th[1] - th[0]) - math.pi / S) < 1e-14)
    check("G6-three-eighths-no-upgrade",
          (1.0 / 3.0) < 0.375)


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(P.MAIN_KZ)
    N = int(mz["Nw"])
    S = int(mz["S"])
    n0 = (2 * N) // 5
    ap = P.angle_pack(mz["yn"], S)
    B = P.make_B(mz, N - 1)
    m = B.shape[0]
    E = np.zeros((m, m))
    k_g = None
    wall = None
    for k in range(1, N):
        E += np.outer(B[:, k - 1], B[:, k - 1])
        diag = np.diag(E)
        off = np.abs(E).copy()
        np.fill_diagonal(off, 0.0)
        gersh = float(np.max(diag + off.sum(axis=1)))
        if k_g is None and gersh >= 1.0:
            k_g = k
        if k == N - 1:
            maxd = float(np.max(diag))
            lam = P.gram_lam(B[:, :k])
            gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
            assist = lam / maxd - 1.0
            wall = dict(lam=lam, maxd=maxd, assist=assist,
                        canc=1.0 - assist / max(gA, 1e-12))
    check("G10-w9-k-gersh",
          k_g == 21 and k_g < n0,
          "k_g=%d n0=%d" % (k_g, n0))
    check("G11-w9-wall",
          0.95 < wall["maxd"] < 0.97
          and 0.03 < wall["assist"] < 0.05
          and wall["lam"] < 1.0 and wall["canc"] > 0.99,
          "lam=%.6f maxd=%.4f assist=%.4f" % (
              wall["lam"], wall["maxd"], wall["assist"]))
    check("G12-w9-AP",
          ap["frac"] < 0.10 and ap["cv"] > 0.70
          and abs(ap["ratio"] - 1.0 / 3.0) < 0.01
          and abs(ap["dmin_mesh"] - 1.0) < 1e-6,
          "rho_AP=%.4f cv=%.3f" % (ap["frac"], ap["cv"]))

    mz23 = P.two_period(81, P.C_FLANK)
    ap23 = P.angle_pack(mz23["yn"], 81)
    lam22 = P.gram_lam(P.make_B(mz23, 22))
    Q0 = float(np.sum(mz23["vn"])) / float(np.sum(mz23["wp"]))
    drow_s = P.dirichlet_maxrow(ap["th"], mz["vn"], 22)
    drow_t = P.dirichlet_maxrow(ap23["th"], mz23["vn"], 22)
    check("G13-Dirichlet-maxrow",
          drow_s < 0.35 and drow_t > 0.80 and drow_t > 2.0 * drow_s,
          "src=%.3f TP=%.3f" % (drow_s, drow_t))
    check("G14-two-period",
          ap23["frac"] == 1.0 and lam22 > 1.0
          and 0.68 < Q0 < 0.69,
          "Q=%.4f lam22=%.4f" % (Q0, lam22))

    ds = HS.window_data(9, scramble_seed=1)
    mzs = dict(xp=ds["xs"], wp=ds["ws"], yn=ds["ys"], vn=ds["vs"])
    _kg, kls, kds, _la, _B, _E = P.walk_cross(mzs, 80)
    aps = P.angle_pack(ds["ys"], S)
    check("G15-scramble",
          kls is not None and 20 <= kls <= 25
          and kds is not None and 45 <= kds <= 55
          and aps["frac"] < 0.10,
          "k_lam=%s k_maxd=%s rho_AP=%.3f" % (kls, kds, aps["frac"]))

    lam1 = P.gram_lam(P.make_B(P.two_period(81, 1.0), 1))
    mz_c3 = P.clustered(81, 3)
    _g, kl3, _d, _l, _b, _e = P.walk_cross(mz_c3, 24, stop="lam")
    n0_tp = (2 * 41) // 5
    apc = P.angle_pack(mz_c3["yn"], 81)
    check("G16-c1-cluster3",
          lam1 > 1.0 and kl3 is not None and kl3 < n0_tp
          and apc["frac"] == 1.0,
          "lam1=%.4f CL3 k_lam=%s n0=%d" % (lam1, kl3, n0_tp))


def main():
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("COHERENCE ASSIST VERIFIED")
        return 0
    print("COHERENCE ASSIST FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
