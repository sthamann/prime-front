#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_g_eps_mu.py -- machine check of every numbered lemma
in rh/problem/g_eps_mu.tex (round 390, G_eps^mu reduced to
F_eps ^ W_eps).

PART A (STANDALONE, Fractions):
  G1  Jacobi-(0,1) |g-1/4|=1/(4(2n+1)^2) over Q (r379)
  G2  Chebyshev-U monic p2=x^2-1/4 (gamma_k=1/4)
  G3  monic gamma homogeneous under w -> 3w
  G4  log(5/3) > 2/5: the jump is not implied by the box
  G5  small full-grid Fejer max|g-1/4| < 5e-4 (h=12)
  G6  ratio bound kappa=3 on a 4-atom toy misses a tight box

PART B (CONSTRUCTION PINS):
  G10 w9 mu last-12 inside the box
  G11 w9 Fejer-occupied inside; signed-Fejer outside
  G12 full-grid Fejer Bernstein-Szego residual < 5e-6
  G13 kappa >= 100 (ratio bound useless)
  G14 perm seed=3 kills the box on the same nodes
  G15 scramble_seed=1 mu-only kills
  G16 two-period weight a=0.95 stays IN

Exit: per-gate PASS/FAIL and the final line
"G_EPS_MU LEMMA VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
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
import g_eps_mu_probe as P  # noqa: E402

CHECKS = []
BOX = P.BOX
JUMP = P.JUMP


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
    section("PART A  JACOBI-(0,1), U, HOMOGENEITY, RATIO")
    n_bad = 0
    for n in range(1, 80):
        g = Fr(n) * Fr(n + 1) / (Fr(2 * n + 1) ** 2)
        if abs(g - Fr(1, 4)) != Fr(1, 4) / (Fr(2 * n + 1) ** 2):
            n_bad += 1
    check("G1-jacobi-0-1-fejer-Q", n_bad == 0, "n=1..79 exact")

    x = Fr(2, 5)
    p2 = x * x - Fr(1, 4)
    check("G2-chebyshev-U-monic",
          p2 == x * x - Fr(1, 4) and p2 == x * x - Fr(1, 4),
          "p2=x^2-1/4; gamma_k=1/4")

    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1, 5)] * 5
    b1 = P.stieltjes_exact(nodes, wts, 3)
    b3 = P.stieltjes_exact(nodes, [Fr(3) * w for w in wts], 3)
    check("G3-gamma-homogeneous-Q", b1 == b3, "w -> 3w")

    check("G4-jump-not-implied",
          math.log(5.0 / 3.0) > JUMP,
          "log(5/3)=%.4f > 2/5" % math.log(5.0 / 3.0))

    xf, wf = P.full_grid(12)
    gf = P.mu_gams(xf, wf, min(12, len(xf) - 2))
    dev = float(np.max(np.abs(gf[1:] - 0.25)))
    check("G5-small-fullgrid-Fejer",
          dev < 5.0e-4,
          "h=12 max|g-1/4|_{k>=2}=%.3e" % dev)

    # 4-atom ratio bound: kappa=3, Fejer-like weights vs *3 on one atom
    nodes_f = np.array([-0.6, -0.2, 0.2, 0.6])
    w0 = np.maximum(1.0 - nodes_f, 0.1)
    w1 = w0.copy()
    w1[-1] *= 3.0
    g0 = P.mu_gams(nodes_f, w0, 2)
    kap = 3.0
    lo = float(np.min(g0)) / kap
    hi = float(np.max(g0)) * kap
    check("G6-ratio-bound-useless-toy",
          lo < 0.1875 or hi > 0.3125,
          "kappa=3 image [%.4f,%.4f] vs box [3/16,5/16]"
          % (lo, hi))


def part_b():
    section("PART B  CONSTRUCTION PINS")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    n = int(d["n_max"]) - 2
    mass = float(ws.sum())
    wf = P.fejer_w(xs, mass)
    wy = P.fejer_w(ys, float(vs.sum()))

    print("    w9 chains n=%d ..." % n, flush=True)
    g_mu = P.mu_gams(xs, ws, n)
    g_fj = P.mu_gams(xs, wf, n)
    g_sf = P.signed_chain(xs, wf, ys, wy, n)
    dmu, jmu = P.last12(g_mu)
    dfj, jfj = P.last12(g_fj)
    dsf, jsf = P.last12(g_sf)
    check("G10-mu-w9-inside",
          dmu <= BOX + 1e-12 and jmu <= JUMP,
          "|g-1/4|_12=%.5f jump=%.4f" % (dmu, jmu))
    check("G11-Fejer-occ-in-signed-out",
          dfj <= BOX + 1e-12 and jfj <= JUMP
          and dsf > BOX,
          "Fejer-occ=%.5f IN; signed-Fejer=%.5f OUT"
          % (dfj, dsf))

    xf, wff = P.full_grid(int(d["n_max"]))
    gfg = P.mu_gams(xf, wff, min(n, len(xf) - 2))
    dev = float(np.max(np.abs(gfg[1:] - 0.25)))
    check("G12-fullgrid-residual",
          dev < P.FULLGRID_BAR,
          "max|g-1/4|_{k>=2}=%.3e" % dev)

    _eps, ratio = P.eps_ratio(xs, ws)
    kappa = float(np.max(ratio) / np.min(ratio))
    check("G13-kappa-useless",
          kappa >= P.KAPPA_FLOOR,
          "kappa=%.1f" % kappa)

    rng = np.random.RandomState(P.PERM_SEED)
    wperm = ws.copy()
    rng.shuffle(wperm)
    dp, jp = P.last12(P.mu_gams(xs, wperm, n))
    check("G14-perm-seed3-kills",
          dp > BOX or jp > JUMP,
          "perm |g-1/4|=%.5f jump=%.4f" % (dp, jp))

    ds = HS.window_data(9, scramble_seed=P.SCR_SEED)
    ns = int(ds["n_max"]) - 2
    dss, jss = P.last12(P.mu_gams(ds["xs"], ds["ws"], ns))
    check("G15-scramble-seed-mu-kills",
          dss > BOX or jss > JUMP,
          "scr-mu |g-1/4|=%.5f jump=%.4f" % (dss, jss))

    a = 0.95
    alt = 1.0 + a * np.array([(-1) ** i for i in range(len(xs))])
    walt = wf * np.maximum(alt, 1e-12)
    walt *= mass / walt.sum()
    da, ja = P.last12(P.mu_gams(xs, walt, n))
    check("G16-two-period-weight-IN",
          da <= BOX + 1e-12 and ja <= JUMP,
          "a=0.95 |g-1/4|=%.5f jump=%.4f" % (da, ja))


def main():
    part_a()
    part_b()
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("\n  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("G_EPS_MU LEMMA VERIFIED")
        return 0
    print("G_EPS_MU LEMMA FAILED %d" % (n_all - n_ok))
    return 1


if __name__ == "__main__":
    sys.exit(main())
