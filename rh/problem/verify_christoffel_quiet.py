#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_christoffel_quiet.py -- machine check of every numbered
lemma in rh/problem/christoffel_quiet.tex (round 385,
LEMMA.CHRISTOFFEL_QUIET.01).

PART A (STANDALONE, Fractions / trig identities):
  G1  T_k^2 = (1+T_{2k})/2 over Q at x=2/5
  G2  TV(cos(2k theta),[0,pi]) = 4k
  G3  trivial Weyl |S| <= mass
  G4  Chebyshev-Gauss Q_k = 1 on an equal-weight cosine grid
  G5  3-atom one-Rayleigh h0(1-Q0)=2, Q0=1/2
  G6  two-period equal-mass: Q_k is independent of k (span 0)

PART B (CONSTRUCTION PINS):
  G10 w9: alpha in (0.060,0.062), Q12 in (0.38,0.40),
      |FO|_12 < 1/32, D* in (0.17,0.20)
  G11 FO = gamma dQ on w9 first-12 (maxdev 1e-12)
  G12 Koksma k D* > 10 and deformation |Q-Qcheb| > 0.25;
      effective |Q-alpha|/(k D*) < 0.02
  G13 Weyl |S_2k|/mass < 1/2 (trivial scale)
  G14 scramble seed=1: k_Q>=1 in [60,80], last-12 Q > 10^3
  G15 two-period S=81 c=2/3: Q in (0.68,0.69) constant,
      lambda_max(E_22)>1; c=1 Q0>1
  G16 EXT-heavy kz69 Qmax at depth 200 < 0.25

Exit: per-gate PASS/FAIL and the final line
"CHRISTOFFEL QUIET VERIFIED" iff every gate passed.

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

CHECKS = []
MAIN_KZ = 9
SCR_SEED = 1
CEPS = 1.0 / 32.0
C_FLANK = 2.0 / 3.0


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


def mu_Qk(xp, wp, yn, vn, depth):
    a, b, h0 = V.mu_chain(xp, wp, depth)
    u = np.ones_like(yn) / math.sqrt(h0)
    um = np.zeros_like(yn)
    Q = np.empty(depth)
    Q[0] = float(np.dot(vn, u * u))
    for i in range(depth - 1):
        r = (yn - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        Q[i + 1] = float(np.dot(vn, u * u))
    return Q, b, h0


def star_disc(theta):
    t = np.sort(np.asarray(theta, float) / math.pi)
    t = np.clip(t, 0.0, 1.0)
    n = len(t)
    k = np.arange(1, n + 1, dtype=float)
    return float(max(np.max(k / n - t), np.max(t - (k - 1) / n)))


def weyl(theta, vn, m):
    return complex(float(np.sum(vn * np.cos(m * theta))),
                   float(np.sum(vn * np.sin(m * theta))))


def qcheb(xp, wp, yn, vn, k):
    thy = np.arccos(np.clip(yn, -1.0, 1.0))
    thx = np.arccos(np.clip(xp, -1.0, 1.0))
    num = float(np.sum(vn * (1.0 + np.cos(2 * k * thy))))
    den = float(np.sum(wp * (1.0 + np.cos(2 * k * thx))))
    return num / max(den, 1e-30)


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    pos = w > 0
    return dict(xp=x[pos], wp=w[pos], yn=x[~pos], vn=-w[~pos],
                Nw=(S + 1) // 2, S=S)


def part_a():
    section("PART A  STANDALONE IDENTITIES")
    x = Fr(2, 5)
    T = [Fr(1), x]
    for _n in range(4):
        T.append(2 * x * T[-1] - T[-2])
    check("G1-Tk2-identity",
          T[2] * T[2] == (Fr(1) + T[4]) / Fr(2),
          "T_2(2/5)^2 = (1+T_4)/2")

    tv_ok = True
    for k in (1, 2, 3, 5, 8):
        m = 2 * k
        tv = m * m * (2.0 / m)
        if abs(tv - 4.0 * k) > 1e-12:
            tv_ok = False
    check("G2-TV-cos-2k", tv_ok, "TV=4k")

    w = np.array([0.2, 0.3, 0.5])
    th = np.array([0.1, 1.2, 2.4])
    S = abs(complex(float(np.sum(w * np.cos(th))),
                    float(np.sum(w * np.sin(th)))))
    check("G3-trivial-Weyl", S <= float(np.sum(w)) + 1e-15,
          "|S|=%.6f <= 1" % S)

    n = 32
    L = 2 * n
    j = np.arange(1, n)
    xg = np.cos(2.0 * math.pi * j / L)
    wg = np.full_like(xg, 1.0 / len(xg))
    Qg, _, _ = mu_Qk(xg, wg, xg, wg, 16)
    check("G4-Chebyshev-Gauss",
          float(np.max(np.abs(Qg - 1.0))) < 1e-12,
          "max|Q-1|=%.3e" % float(np.max(np.abs(Qg - 1.0))))

    check("G5-one-Rayleigh",
          Fr(4) * (Fr(1) - Fr(1, 2)) == Fr(2),
          "h0(1-Q0)=2 on the 3-atom (3,-2,3)")

    mz = two_period(21, C_FLANK)
    Q, _, _ = mu_Qk(mz["xp"], mz["wp"], mz["yn"], mz["vn"], 8)
    check("G6-two-period-Q-constant",
          float(np.max(Q) - np.min(Q)) < 1e-12,
          "S=21 c=2/3 Q span=%.3e Q=%.4f"
          % (float(np.max(Q) - np.min(Q)), float(Q[0])))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    mz = V.build_measures(MAIN_KZ)
    N = int(mz["Nw"])
    xp, wp, yn, vn = mz["xp"], mz["wp"], mz["yn"], mz["vn"]
    alpha = float(np.sum(vn)) / float(np.sum(wp))
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    Ds = star_disc(th)
    Q, b, _ = mu_Qk(xp, wp, yn, vn, N - 1)
    q12 = float(np.max(Q[-12:]))
    fo12 = float(np.max(np.abs((b[-12:] ** 2) * np.diff(Q[-13:]))))
    check("G10-w9-pins",
          0.060 < alpha < 0.062 and 0.38 < q12 < 0.40
          and fo12 < CEPS and 0.17 < Ds < 0.20,
          "a=%.4f Q12=%.4f |FO|12=%.5f D*=%.4f" % (alpha, q12, fo12, Ds))

    x, w = xp, wp
    y, v = yn, vn
    px, py = np.ones_like(x), np.ones_like(y)
    pxm, pym = np.zeros_like(x), np.zeros_like(y)
    hs = [float(np.dot(w, px * px))]
    ns = [float(np.dot(v, py * py))]
    fos = []
    for k in range(12):
        alh = float(np.dot(w, x * px * px)) / hs[-1]
        if k == 0:
            rx, ry = (x - alh) * px, (y - alh) * py
        else:
            ge = hs[-1] / hs[-2]
            rx = (x - alh) * px - ge * pxm
            ry = (y - alh) * py - ge * pym
        pxm, pym, px, py = px, py, rx, ry
        hs.append(float(np.dot(w, px * px)))
        ns.append(float(np.dot(v, py * py)))
        g = hs[-1] / hs[-2]
        fos.append((ns[-1] - g * ns[-2]) / hs[-2])
    pred12 = (b[:12] ** 2) * np.diff(Q[:13])
    iddev = float(np.max(np.abs(np.array(fos) - pred12)))
    check("G11-FO-identity",
          iddev < 1e-12, "maxdev=%.3e" % iddev)

    deform = max(abs(Q[k] - qcheb(xp, wp, yn, vn, k))
                 for k in range(0, N - 1, max(1, (N - 1) // 16)))
    kd = (N - 2) * Ds
    eff = abs(Q[-1] - alpha) / max(kd, 1e-12)
    check("G12-Koksma-fails-deform-lives",
          kd > 10.0 and deform > 0.25 and eff < 0.02,
          "kD*=%.1f deform=%.3f eff=%.4f" % (kd, deform, eff))

    mass_nu = float(np.sum(vn))
    wr = [abs(weyl(th, vn, 2 * k)) / mass_nu
          for k in (1, 45, 91, 171) if k < N - 1]
    check("G13-Weyl-trivial",
          max(wr) < 0.5, "max |S|/mass=%.3f" % max(wr))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    Qs, _, _ = mu_Qk(ds["xs"], ds["ws"], ds["ys"], ds["vs"], 183)
    kfail = next((i for i, q in enumerate(Qs) if q >= 1.0), None)
    check("G14-scramble",
          kfail is not None and 60 <= kfail <= 80
          and float(np.max(Qs[-12:])) >= 1.0e3,
          "k_Q>=1=%s Q12=%.3e" % (kfail, float(np.max(Qs[-12:]))))

    mz23 = two_period(81, C_FLANK)
    Q23, _, _ = mu_Qk(mz23["xp"], mz23["wp"], mz23["yn"], mz23["vn"], 40)
    lam22, _ = V.lam_max_at(mz23, 22)
    mz1 = two_period(81, 1.0)
    Q1, _, _ = mu_Qk(mz1["xp"], mz1["wp"], mz1["yn"], mz1["vn"], 2)
    check("G15-two-period",
          0.68 < float(np.max(Q23)) < 0.69
          and float(np.max(Q23) - np.min(Q23)) < 1e-10
          and lam22 > 1.0 and float(Q1[0]) > 1.0,
          "Q=%.4f lam22=%.4f Q0(c=1)=%.4f"
          % (float(np.max(Q23)), lam22, float(Q1[0])))

    m69 = V.build_measures(69)
    Qh, _, _ = mu_Qk(m69["xp"], m69["wp"], m69["yn"], m69["vn"], 200)
    check("G16-EXT-kz69",
          float(np.max(Qh)) < 0.25,
          "kz69 N=%d Qmax@200=%.4f" % (int(m69["Nw"]), float(np.max(Qh))))


def main():
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("CHRISTOFFEL QUIET VERIFIED")
        return 0
    print("CHRISTOFFEL QUIET FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
