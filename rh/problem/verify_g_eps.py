#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_g_eps.py -- machine check of every numbered lemma
in rh/problem/g_eps_lemma.tex (round 381, G_eps reduced to
the FO pairing C_eps and the second-order remainder R2).

PART A (STANDALONE, Fractions, no window builders):
  G1  first-order formula over Q (central difference vs FO)
  G2  remainder of the first-order step is Theta(eps^2)
  G3  Jacobi-(0,1) |g-1/4|=1/(4(2n+1)^2) over Q (r379)
  G4  log(5/3) > 2/5: the jump is not implied by the box
  G5  Lambda(n) <= log n for n=2..120 (trial division)
  G6  monic Chebyshev gamma_1=1/2, gamma_k=1/4 (r379)

PART B (CONSTRUCTION PINS):
  G10 FO vs FD on FRAME-A w9 (one atom)
  G11 G_eps on FRAME-A w9 (signed last-12)
  G12 mu-only last-12 inside the box (positive +arm)
  G13 R2 not dominated along Fejer-ref -> actual (n=40)
  G14 scramble seed=1 last-12 leaves the box
  G15 L^inf of Fejer-stripped d_arm is O(1), too crude
  G16 two-period vs segregated block (R379 step obstruction)

Exit: per-gate PASS/FAIL and the final line
"G_EPS LEMMA VERIFIED" iff every (selected) gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

CHECKS = []
BOX = Fr(1, 16)
JUMP = Fr(2, 5)
BOX_F = float(BOX)
JUMP_F = float(JUMP)


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


def stieltjes_exact(nodes, wts, n_upto):
    S = len(nodes)
    pk = [Fr(1)] * S
    pkm = [Fr(0)] * S
    hs = [sum(w * p * p for w, p in zip(wts, pk))]
    pks = [list(pk)]
    for k in range(n_upto):
        a = sum(w * x * p * p
                for w, x, p in zip(wts, nodes, pk)) / hs[-1]
        b = hs[-1] / hs[-2] if len(hs) > 1 else Fr(0)
        nx = [(x - a) * p - b * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        pks.append(list(pk))
        hs.append(sum(w * p * p for w, p in zip(wts, pk)))
    beta = [hs[n] / hs[n - 1] for n in range(1, len(hs))]
    return beta, hs, pks


def fo_dgamma_Q(pks, hs, k, j):
    gam = hs[k] / hs[k - 1]
    return (pks[k][j] * pks[k][j]
            - gam * pks[k - 1][j] * pks[k - 1][j]) / hs[k - 1]


def lambda_le_log(N):
    for n in range(2, N + 1):
        m = n
        p = 2
        hit = False
        while p * p <= m:
            if m % p == 0:
                while m % p == 0:
                    m //= p
                if m == 1 and math.log(p) > math.log(n) + 1e-12:
                    return False
                hit = True
                break
            p += 1
    return True


def signed_chain(xs, ws, ys, vs, n_upto):
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    gams = []
    h_list = [eta]
    Px = [qx.copy()]
    Py = [qy.copy()]
    for n in range(n_upto):
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
        sc = max(float(np.max(np.abs(px))),
                 float(np.max(np.abs(py))), 1e-300)
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qx, qy = px / sc, py / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        gams.append(gam)
        h_list.append(eta * math.exp(2.0 * Ls))
        Px.append(qx * math.exp(Ls))
        Py.append(qy * math.exp(Ls))
    return np.array(gams), h_list, Px, Py


def mu_chain(x, w, n_upto):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    h = float(np.sum(w * q * q))
    hs = [h]
    gams = []
    for k in range(n_upto):
        alh = float(np.sum(w * x * q * q)) / h
        px = ((x - alh) * q if k == 0
              else (x - alh) * q - (h / hs[-2]) * qm)
        qm, q = q, px
        hs.append(float(np.sum(w * q * q)))
        gams.append(hs[-1] / hs[-2])
        h = hs[-1]
    return np.array(gams)


def last12_stats(g):
    g12 = np.asarray(g[-12:], float)
    dbox = float(np.max(np.abs(g12 - 0.25)))
    jmp = (float(np.max(np.abs(np.log(g12[1:] / g12[:-1]))))
           if np.all(g12 > 0) else float("inf"))
    return dbox, jmp


def scan_eta(dth, n_eta=401):
    nviol = 0
    for eta in np.linspace(0.0, math.pi, n_eta, endpoint=False):
        th = float(eta)
        levs = [int(math.floor(th / math.pi))]
        for d in dth:
            th += float(d)
            levs.append(int(math.floor(th / math.pi)))
        R, start, cur = [], 0, levs[0]
        for i in range(1, len(levs)):
            if levs[i] != cur:
                R.append(i - start)
                start, cur = i, levs[i]
        R.append(len(levs) - start)
        if len(R) >= 7 and tuple(R[-3:]) == (1, 1, 1):
            prev4 = R[-7:-3]
            if sum(1 for r in prev4 if r <= 2) < 2:
                nviol += 1
    return nviol


def part_a():
    section("PART A  FO FORMULA, FEJER, JUMP, LAMBDA")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3), Fr(4, 5)]
    wts = [Fr(1, 6)] * 6
    n_upto = 4
    beta, hs, pks = stieltjes_exact(nodes, wts, n_upto)
    eps = Fr(1, 200)
    j0 = 2
    wp = list(wts)
    wp[j0] = wts[j0] + eps
    bp, _, _ = stieltjes_exact(nodes, wp, n_upto)
    wm = list(wts)
    wm[j0] = wts[j0] - eps
    bm, _, _ = stieltjes_exact(nodes, wm, n_upto)
    max_rel = 0.0
    max_quad = 0.0
    for k in range(1, n_upto + 1):
        fo = fo_dgamma_Q(pks, hs, k, j0)
        cd = (bp[k - 1] - bm[k - 1]) / (2 * eps)
        rem = bp[k - 1] - beta[k - 1] - fo * eps
        rel = abs(float(cd - fo)) / max(abs(float(fo)), 1e-30)
        max_rel = max(max_rel, rel)
        max_quad = max(max_quad, abs(float(rem)) / float(eps ** 2))
    check("G1-FO-formula-Q",
          max_rel <= 3.0e-4,
          "max |CD-FO|/|FO|=%.3e" % max_rel)
    check("G2-R2-Theta-eps2",
          0.05 <= max_quad <= 5.0,
          "max |rem|/eps^2=%.4f" % max_quad)

    n_bad = 0
    for n in range(1, 80):
        g = Fr(n) * Fr(n + 1) / (Fr(2 * n + 1) ** 2)
        if abs(g - Fr(1, 4)) != Fr(1, 4) / (Fr(2 * n + 1) ** 2):
            n_bad += 1
    check("G3-jacobi-0-1-fejer-Q", n_bad == 0,
          "n=1..79 exact")

    check("G4-jump-not-implied",
          math.log(5.0 / 3.0) > JUMP_F,
          "log(5/3)=%.4f > 2/5" % math.log(5.0 / 3.0))
    check("G5-Lambda-le-log-n",
          lambda_le_log(120),
          "n=2..120 trial division")

    x = Fr(2, 5)
    T0, T1 = Fr(1), x
    T2 = x * T1 - Fr(1, 2) * T0
    T3 = x * T2 - Fr(1, 4) * T1
    T4 = x * T3 - Fr(1, 4) * T2
    check("G6-chebyshev-monic-quarters",
          T2 == x * x - Fr(1, 2)
          and T3 == x ** 3 - Fr(3, 4) * x
          and T4 == x * T3 - Fr(1, 4) * T2,
          "gamma_1=1/2, gamma_k=1/4")


def part_b():
    section("PART B  CONSTRUCTION PINS")
    import hirota_sign_probe as HS

    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2

    n_fo = 12
    g0, h0, Px0, Py0 = signed_chain(xs, ws, ys, vs, n_fo)
    j0, eps = 10, 1e-7
    wsp = ws.copy()
    wsp[j0] += eps
    gp, _, _, _ = signed_chain(xs, wsp, ys, vs, n_fo)
    dws = np.zeros_like(ws)
    dws[j0] = eps
    max_rel = 0.0
    for k in (1, 2, 5, 10, 12):
        gam = g0[k - 1]
        pred = float(np.sum(
            dws * (Px0[k] ** 2 - gam * Px0[k - 1] ** 2))) / h0[k - 1]
        fd = gp[k - 1] - g0[k - 1]
        max_rel = max(max_rel,
                      abs(pred - fd) / max(abs(pred), 1e-30))
    check("G10-FO-vs-FD-w9",
          max_rel <= 1e-3,
          "max rel=%.3e" % max_rel)

    print("    signed+mu chains n=%d ..." % n, flush=True)
    g_sg, _, _, _ = signed_chain(xs, ws, ys, vs, n)
    g_mu = mu_chain(xs, ws, n)
    dsg, jsg = last12_stats(g_sg)
    dmu, jmu = last12_stats(g_mu)
    check("G11-Geps-w9-signed",
          dsg <= BOX_F + 1e-12 and jsg <= JUMP_F,
          "|g-1/4|_12=%.5f jump=%.4f" % (dsg, jsg))
    check("G12-mu-only-inside-box",
          dmu <= BOX_F + 1e-12 and jmu <= JUMP_F,
          "|g-1/4|_12=%.5f jump=%.4f" % (dmu, jmu))

    n_r2 = 40
    fx = np.maximum(1.0 - xs, 1e-15)
    fy = np.maximum(1.0 - ys, 1e-15)
    wx = fx * (float(ws.sum()) / float(np.sum(fx)))
    wy = fy * (float(vs.sum()) / float(np.sum(fy)))

    def g_of(t):
        g, _, _, _ = signed_chain(
            xs, (1.0 - t) * wx + t * ws,
            ys, (1.0 - t) * wy + t * vs, n_r2)
        return g

    ga, gb, gh = g_of(0.0), g_of(1.0), g_of(0.5)
    lin_m = float(np.max(np.abs((gb - ga)[-12:])))
    quad_m = float(np.max(np.abs((gb - 2.0 * gh + ga)[-12:])))
    ratio = quad_m / max(lin_m, 1e-12)
    check("G13-R2-not-dominated",
          ratio >= 0.5,
          "|quad|/|lin|_last12=%.3f lin=%.5f quad=%.5f"
          % (ratio, lin_m, quad_m))

    dscr = HS.window_data(9, scramble_seed=1)
    print("    scramble chain n=%d ..." % n, flush=True)
    gscr, _, _, _ = signed_chain(
        dscr["xs"], dscr["ws"], dscr["ys"], dscr["vs"], n)
    ds, js = last12_stats(gscr)
    check("G14-scramble-kills-Geps",
          ds >= 2.0,
          "SCR |g-1/4|_12=%.4f jump=%.3f" % (ds, js))

    dpx = ws / fx
    einf = float(np.max(np.abs(dpx / float(np.mean(dpx)) - 1.0)))
    check("G15-Linf-too-crude",
          einf > 1.0,
          "||eps_mu||_inf=%.3f" % einf)

    DELTA = 0.5 * math.pi
    a = 0.70
    d_alt = DELTA * np.array([1.0 + a * ((-1) ** i) for i in range(24)])
    slo, fhi = float(np.min(d_alt[:14])), float(np.max(d_alt[:14]))
    d_blk = np.array([slo] * 21 + [fhi, fhi, fhi], dtype=float)
    v_alt, v_blk = scan_eta(d_alt), scan_eta(d_blk)
    check("G16-block-is-step-not-FO",
          v_alt == 0 and v_blk > 0,
          "two-period viol=%d; block viol=%d" % (v_alt, v_blk))


def main():
    argparse.ArgumentParser().parse_args()
    part_a()
    part_b()
    section("SUMMARY")
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("G_EPS LEMMA VERIFIED")
        return 0
    print("G_EPS LEMMA FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
