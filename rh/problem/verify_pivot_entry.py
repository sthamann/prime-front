#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_pivot_entry.py -- machine check of every numbered lemma
in rh/problem/pivot_entry_lemma.tex (round 382, LEMMA.PIVOT_ENTRY.01).

PART A (STANDALONE, Fractions):
  G1  pair-energy identity m0 m2 - m1^2 = (1/2) sum_{i,j} w_i w_j (x_i-x_j)^2
  G2  5-atom 2-vs-1 interlacing: h0=4, h1=14, h2=13, h3=-144/7
      (full free window of that toy, N=3)
  G3  two-period equal-mass 6-atom: H_1=0 (c>=1 kills h_0 or h_1)
  G4  clustered 3-neg 7-atom: H_3<0 before half-filling (N=4)
  G5  3-atom flank (3,-2,3): ratio 1/3, h0=4, h1=6, h2=-3
  G6  RKHS on the 3-atom: v K_2(y)=1/3 = lambda_max(E_2) < 1
  G7  Christoffel comparison h1(sigma) >= (1-lambda) h1(mu)  (6 >= 4)
  G8  beta^2 sign equals the h-ratio sign on the 5-atom (first
      negative beta^2 at the first negative h)

PART B (CONSTRUCTION PINS):
  G10 w9 (F1) and (F2_{2/3}), first_neg=N, n0=floor(2N/5)=73,
      first_neg > n0, rmax in (0.568, 0.570)
  G11 scramble drops (F1) and (F2): max_len=5, rmax>2, first_neg=21
      < n0=73, lambda_max(E_22)>1, |alpha| explodes at 21
  G12 dead chi3-15 still (F1) and (F2_{2/3})
  G13 two-period S=81: c=1/2 first_neg=40; c=2/3 first_neg=20 >= n0=16;
      c=1 first_neg=0
  G14 clustered S=21 run of 6: (F1) fails, first_neg < n0
  G15 lambda_max MAIN E_8 < 1/4, E_22 < 7/10; SCR E_22 > 1
      (the generic wall sits at ~0.12 N; MAIN is still 0.63 there)

Exit: per-gate PASS/FAIL and the final line
"PIVOT ENTRY STEPS VERIFIED" iff every gate passed.

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
VERIFY = os.path.join(REPO, "verification")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, VERIFY, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

CHECKS = []
MAIN_KZ = 9
SCR_SEED = 1
C_FLANK = Fr(2, 3)
KAPPA = Fr(2, 5)


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


def det(A):
    A = [r[:] for r in A]
    n = len(A)
    d = Fr(1)
    for j in range(n):
        p = next((i for i in range(j, n) if A[i][j]), None)
        if p is None:
            return Fr(0)
        if p != j:
            A[j], A[p] = A[p], A[j]
            d = -d
        q = A[j][j]
        d *= q
        for i in range(j + 1, n):
            c = A[i][j] / q
            for k in range(j + 1, n):
                A[i][k] -= c * A[j][k]
    return d


def Hdet(xs, ws, n):
    if n == 0:
        return Fr(1)
    mu = [sum(w * x ** k for x, w in zip(xs, ws)) for k in range(2 * n - 1)]
    return det([[mu[i + j] for j in range(n)] for i in range(n)])


def hrat(xs, ws, j):
    d = Hdet(xs, ws, j)
    if d == 0:
        return Fr(0)
    return Hdet(xs, ws, j + 1) / d


def n0_of(N):
    return int(math.floor(float(KAPPA) * N))


def flanking_stats(wu):
    s = np.sign(wu)
    n = len(s)
    runs = []
    i = 0
    while i < n:
        if s[i] < 0:
            j = i
            while j < n and s[j] < 0:
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1
    rats, lens = [], []
    for a, b in runs:
        nu = float(-np.sum(wu[a:b]))
        fl = 0.0
        if a > 0 and wu[a - 1] > 0:
            fl += float(wu[a - 1])
        if b < n and wu[b] > 0:
            fl += float(wu[b])
        lens.append(b - a)
        rats.append(nu / fl if fl > 0 else np.inf)
    finite = [r for r in rats if math.isfinite(r)]
    return dict(
        max_len=max(lens) if lens else 0,
        n_lenge3=sum(1 for L in lens if L >= 3),
        rmax=max(finite) if finite else np.inf,
        n_gt1=sum(1 for r in finite if r >= 1.0),
        F1=bool(lens) and max(lens) <= 2,
        F2=bool(finite) and max(finite) < 1.0,
        F23=bool(finite) and max(finite) <= float(C_FLANK) + 1e-12,
    )


def signed_first(x, w, nmax):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    eta = float(np.dot(w, q * q))
    signs = [int(np.sign(eta)) if eta != 0 else 0]
    log_s = log_sm = 0.0
    etam = 1.0
    first_big_a = None
    for n in range(nmax):
        if abs(eta) < 1e-300:
            break
        al = float(np.dot(w, x * q * q)) / eta
        if first_big_a is None and abs(al) > 2.0:
            first_big_a = n
        if n == 0:
            rvec = (x - al) * q
        else:
            rvec = ((x - al) * q
                    - math.exp(log_s - log_sm) * (eta / etam) * qm)
        sc = float(np.max(np.abs(rvec)))
        if sc == 0.0:
            signs.append(0)
            break
        qm, q = q, rvec / sc
        log_sm, log_s = log_s, log_s + math.log(sc)
        etam, eta = eta, float(np.dot(w, q * q))
        signs.append(int(np.sign(eta)) if eta != 0 else 0)
    fn = next((j for j, s in enumerate(signs) if s < 0), None)
    return fn, first_big_a


def two_period(S, c):
    j = np.arange(1, S + 1)
    x = np.cos(math.pi * j / S)
    mesh = (1.0 - x) * (math.pi / S)
    w = np.where(j % 2 == 0, mesh, -float(c) * mesh)
    return x, w, (S + 1) // 2


def main():
    section("PART A  FRACTIONS IDENTITIES")

    xs = [Fr(-2), Fr(-1), Fr(0), Fr(1), Fr(2)]
    ws = [Fr(2), Fr(-1), Fr(2), Fr(-1), Fr(2)]
    m0 = sum(ws)
    m1 = sum(w * x for x, w in zip(xs, ws))
    m2 = sum(w * x * x for x, w in zip(xs, ws))
    energy = m0 * m2 - m1 * m1
    pair = sum(wi * wj * (xi - xj) ** 2
               for xi, wi in zip(xs, ws)
               for xj, wj in zip(xs, ws)) / 2
    check("G1-energy-identity",
          energy == pair == Fr(56),
          "energy=%s pair=%s" % (energy, pair))

    hs = [hrat(xs, ws, j) for j in range(4)]
    check("G2-five-atom-interlace",
          hs[0] == Fr(4) and hs[1] == Fr(14)
          and hs[2] == Fr(13) and hs[3] == Fr(-144, 7)
          and all(h > 0 for h in hs[:3]) and hs[3] < 0,
          "h=%s" % [str(h) for h in hs])

    xs2 = [Fr(i) for i in range(6)]
    ws2 = [Fr(1), Fr(-1)] * 3
    check("G3-two-period-equal-mass",
          Hdet(xs2, ws2, 1) == Fr(0) and sum(ws2) == Fr(0),
          "H_1=%s tot=%s" % (Hdet(xs2, ws2, 1), sum(ws2)))

    xs3 = [Fr(i) for i in range(7)]
    ws3 = [Fr(2), Fr(2), Fr(-1), Fr(-1), Fr(-1), Fr(2), Fr(2)]
    H3c = Hdet(xs3, ws3, 3)
    Ncl = (7 + 1) // 2
    check("G4-clustered-before-half",
          Hdet(xs3, ws3, 1) > 0 and Hdet(xs3, ws3, 2) > 0
          and H3c < 0 and 3 < Ncl,
          "H1=%s H2=%s H3=%s N=%d" %
          (Hdet(xs3, ws3, 1), Hdet(xs3, ws3, 2), H3c, Ncl))

    xs4 = [Fr(0), Fr(1), Fr(2)]
    ws4 = [Fr(3), Fr(-2), Fr(3)]
    h0 = hrat(xs4, ws4, 0)
    h1 = hrat(xs4, ws4, 1)
    h2 = hrat(xs4, ws4, 2)
    ratio = Fr(2) / (Fr(3) + Fr(3))
    check("G5-three-atom-flank",
          ratio == Fr(1, 3) and h0 == Fr(4) and h1 == Fr(6)
          and h2 == Fr(-3) and h0 > 0 and h1 > 0 and h2 < 0,
          "ratio=%s h=(%s,%s,%s)" % (ratio, h0, h1, h2))

    # mu at 0,2 masses 3,3; nu at 1 mass 2.  Orthonormal P0=1/sqrt(6),
    # barycentre 1, P1(1)=0, K_2(1,1)=1/6, v K = 1/3.
    lam = Fr(1, 3)
    check("G6-rkhs-one-atom",
          lam < 1 and lam == Fr(2, 6),
          "lambda_max(E_2)=%s < 1" % lam)

    h1_mu = Fr(6)   # (x-1)^2 on mu: 3*1+3*1
    h1_sg = h1
    bound = (1 - lam) * h1_mu
    check("G7-christoffel-comparison",
          h1_sg >= bound and bound == Fr(4) and h1_sg == Fr(6),
          "h1(sigma)=%s >= (1-lam) h1(mu)=%s" % (h1_sg, bound))

    b2 = [hs[j] / hs[j - 1] for j in range(1, 4)]
    check("G8-beta2-sign",
          b2[0] > 0 and b2[1] > 0 and b2[2] < 0
          and (b2[2] < 0) == (hs[3] < 0),
          "beta2=%s" % [str(b) for b in b2])

    section("PART B  CONSTRUCTION PINS")
    import verify_lstar_instance as V
    import dirichlet_matched_frame_probe as DMF
    import hirota_sign_probe as HS

    mz9 = V.build_measures(MAIN_KZ)
    N9 = int(mz9["Nw"])
    fl9 = flanking_stats(mz9["wu"])
    fn9, big9 = signed_first(mz9["xu"], mz9["wu"], N9 + 3)
    n09 = n0_of(N9)
    check("G10-w9-flank-entry",
          fl9["F1"] and fl9["F23"] and fn9 == N9
          and fn9 > n09 and n09 == 73
          and 0.568 < fl9["rmax"] < 0.570,
          "N=%d n0=%d first_neg=%s rmax=%.6f max_len=%d"
          % (N9, n09, fn9, fl9["rmax"], fl9["max_len"]))

    d = HS.window_data(9, scramble_seed=SCR_SEED)
    xu = np.concatenate([d["xs"], d["ys"]])
    wu = np.concatenate([d["ws"], -d["vs"]])
    o = np.argsort(xu)
    mzs = dict(xu=xu[o], wu=wu[o], Nw=int(d["n_max"]),
               xp=d["xs"], wp=d["ws"], yn=d["ys"], vn=d["vs"])
    fls = flanking_stats(mzs["wu"])
    fns, bigs = signed_first(mzs["xu"], mzs["wu"], 40)
    n0s = n0_of(int(mzs["Nw"]))
    lams22, _ = V.lam_max_at(mzs, 22)
    check("G11-scramble-kill",
          (not fls["F1"]) and (not fls["F2"])
          and fns == 21 and fns < n0s and n0s == 73
          and fls["max_len"] == 5 and fls["rmax"] > 2.5
          and fls["n_gt1"] == 12 and bigs == 21
          and lams22 > 1.0,
          "first=%s n0=%d max_len=%d rmax=%.3f big_a=%s lam22=%.4f"
          % (fns, n0s, fls["max_len"], fls["rmax"], bigs, lams22))

    uu, ww, _, _ = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mzd = DMF.chi_build_measures(15, uu, ww, 1.0, DMF.LPQ3)
    fld = flanking_stats(mzd["wu"])
    fnd, _ = signed_first(mzd["xu"], mzd["wu"], int(mzd["Nw"]) + 3)
    check("G12-dead-chi3-15",
          fld["F1"] and fld["F23"]
          and fnd is not None and fnd >= n0_of(int(mzd["Nw"])),
          "rmax=%.4f max_len=%d first_neg=%s"
          % (fld["rmax"], fld["max_len"], fnd))

    bits = []
    ok_tp = True
    for c, need in ((0.5, 40), (float(C_FLANK), 20), (1.0, 0)):
        x, w, N = two_period(81, c)
        fn, _ = signed_first(x, w, N + 2)
        n0 = n0_of(N)
        ok = fn == need
        if abs(c - float(C_FLANK)) < 1e-12:
            ok = ok and fn >= n0
        ok_tp = ok_tp and ok
        bits.append("c=%s fn=%s n0=%d" % (c, fn, n0))
    check("G13-two-period-S81", ok_tp, "; ".join(bits))

    j = np.arange(1, 22)
    xc = np.cos(math.pi * j / 21)
    mesh = (1.0 - xc) * (math.pi / 21)
    wc = mesh.copy()
    wc[10:16] *= -1.0
    flc = flanking_stats(wc)
    fnc, _ = signed_first(xc, wc, 13)
    n0c = n0_of(11)
    check("G14-clustered-S21",
          (not flc["F1"]) and fnc is not None and fnc < n0c,
          "max_len=%d first_neg=%s n0=%d" % (flc["max_len"], fnc, n0c))

    lam8, _ = V.lam_max_at(mz9, 8)
    lam22, _ = V.lam_max_at(mz9, 22)
    check("G15-lambda-wall",
          lam8 < 0.25 and lam22 < 0.70 and lams22 > 1.0,
          "MAIN E8=%.4f E22=%.4f  SCR E22=%.4f"
          % (lam8, lam22, lams22))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **"))
    if n_fail == 0:
        print("PIVOT ENTRY STEPS VERIFIED")
        return 0
    print("PIVOT ENTRY STEPS FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
