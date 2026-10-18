#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g_eps_mu_probe -- LEMMA.G_EPS_MU.01 (round 390):
G_eps^mu, the sibling lemma of the POSITIVE mu-chain.

Coexistence: r381 reduced G_eps to G_eps^mu ^ C_eps ^ R2.
r388 adjudicated C_eps and R2 as cancellation objects (the
signed majorant-meta-trap; four dead routes).  G_eps^mu is a
SIZE lemma on the positive chain: last-12 monic Jacobi gamma
of mu satisfy |g-1/4|<=1/16 and |log(g_{k+1}/g_k)|<=2/5.
Measured r381: mu-only last-12 max 0.02605, jump 0.1224.
The r342 digamma dictionary (F_A(xi)=-log pi + Re psi(1/4+i xi/2)
plus the two-cell tent, v_pred < 1e-4) is the language of the
d_arm multiplier.  mu is POSITIVE: classical OP perturbation
is admissible.

THE FROZEN QUESTION.  Does the exact Fejer chain on the cosine
grid, plus a Szego/Nevai/Rakhmanov bound under the digamma
multiplier, prove the box?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  Fejer-basis exact.  Continuous Jacobi-(0,1) is SATZ of
     r379: g=n(n+1)/(2n+1)^2.  Discrete Fejer on the FULL
     cosine grid is Bernstein-Szego (all g_k = 1/4 at residual
     2e-6), NOT Jacobi-(0,1).  Occupied-only Fejer (nu-nodes
     deleted) last-12 |g-1/4|=0.036 < 1/16 at w9 -- ALREADY
     INSIDE; the r381 0.071 was SIGNED Fejer.  Directed pull:
     d_arm helps 40/42 (jump especially).
  B  Positive perturbation.  w = w_Fejer*(1+eps) with the
     digamma/tent profile.  Ratio kappa=sup(1+eps)/inf(1+eps)
     =4200 at w9 -- true and useless.  Smooth powers of (1-x)
     stay IN; random permutation of the SAME weights on the
     SAME nodes kills 17/20 -- NOT construction-pure.
  C  Cofinality.  Deeper N improves (kz82 n=532: 0.0085).
     No m4: the box holds on every core-42 window including
     the smallest (n=140).  Census, not a cofinal theorem.
  D  Kills: perm-scramble; scramble_seed mu (occupation
     moves); two-period weight a<=0.95 stays IN; mutant
     JUMP=1/10 fails mu; Fejer-occ jump 0.394 vs 2/5 is thin.

CALIBRATION DISCLOSURE.  Identities, w9 mu/Fejer/signed-Fejer
last-12, full-grid residual, kappa, perm 20 seeds, two-period
a-scan, and the core-42 census were first measured in /tmp
(r390_cal.py, r390_cal2.py, r390_cal3.py) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are
that measurement, sealed as gates.  No two-commit pre-blind
freeze: pins disclosed.  Builder fallback: core-42 only
(MAIN-85 aborted at >2 min on EXT windows; no 181-pack).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Jacobi-(0,1) n(n+1)/(2n+1)^2 exact over Q (r379 SATZ).
    Chebyshev-U monic: gamma_k=1/4 for k>=1 (p2=x^2-1/4).
  * w9 n=182 S+=263: mu last-12 |g-1/4|=0.02605 jump=0.1224 IN;
    Fejer-occupied 0.03596 / 0.2379 IN; signed-Fejer 0.07136 /
    0.4576 OUT (r381 0.071 reproduced).  Equal-wt occupied
    0.04074 IN.
  * Full cosine-grid Fejer (union = 367 = S++S-): max|g-1/4|
    k>=2 = 1.836e-6 (Bernstein-Szego discrete, NOT Jacobi-(0,1)
    whose n=182 residual is the same 1.88e-6 by coincidence of
    scale, but gamma_1=0.250 not 2/9).  Small h=12: 4.0e-4
    = O(1/S^2), bar 5e-4 (disclosed; not the w9 residual).
  * kappa=4200.56, ||eps||_inf=5.166 -- ratio image of the
    Fejer last-12 is [1e-4, 1163], misses the box.
  * Directed pull w9 |mu-Fejer|_12=0.030; core-42 d_arm helps
    40/42 (mu closer to 1/4 than Fejer).
  * Perm 20 seeds on SAME nodes: 17 OUT, worst 0.101 / 0.621.
    Seed 3: 0.07445 / 0.4590.  Seed 1 happened to stay IN.
  * scramble_seed=1 mu-only: 0.07407 / 0.3518 OUT (occupation
    AND weights move).
  * Two-period weight a=0.00..0.95 on occupied Fejer: all IN
    (a=0.95 jump 0.385 still < 2/5).
  * Core-42: mu 0/42 OUT maxd=0.03304 (kz14) maxj=0.2469;
    Fejer-occ 0/42 OUT maxd=0.04892 (kz55) maxj=0.3942
    (jump half razor-thin: margin 0.0058).
  * Mutant: mu vs 1/32 holds (0.02605<0.03125); vs JUMP=1/10
    fails (0.1224>0.10).  No m4 (smallest core n=140 IN).

AUSGANG REDUZIERT.  SATZ: Jacobi-(0,1); Chebyshev-U gamma=1/4;
monic gamma homogeneous; full-grid Fejer is Bernstein-Szego
discrete (residual 2e-6); ratio bound true-and-useless.
NOT proved: the box.  Occupied-Fejer already in |g-1/4| (max
0.04892) with jump margin 0.0058; d_arm is load-bearing for
JUMP headroom and against permutation.  Remaining, strictly
smaller: F_eps (Fejer-on-occupied last-12, i.e. node-deletion
of the nu-complement from the Bernstein-Szego grid) AND W_eps
(the r342 digamma/tent multiplier vs scramble-of-weights).
G_eps^mu is NOT construction-pure.  The arithmetic weight of
the G_eps triple that lives in the weights (not the nodes)
stays in C_eps on the signed side; on this sibling it is W_eps.

MACHINERY: r226 hirota_sign.window_data, r379 box constants,
r381 mu_chain, r342 dictionary as language (not re-proved).

NO RH CLAIM.  Finite identities, a named reduction, named
kills.  Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import hirota_sign_probe as HS  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

BOX = 1.0 / 16.0
JUMP = 2.0 / 5.0
SCR_SEED = 1
PERM_SEED = 3
CORE_N = 42
N_PERM = 20

# disclosed /tmp pins
W9_MU_D_HI = 0.030
W9_MU_J_HI = 0.150
W9_FJ_D_LO, W9_FJ_D_HI = 0.030, 0.045
W9_SF_D_FLOOR = 0.065
FULLGRID_BAR = 5.0e-6
KAPPA_FLOOR = 100.0
PERM_D_FLOOR = 0.060
PERM_OUT_MIN = 10
CORE_MU_D_BAR = 0.040
CORE_FJ_D_BAR = 0.055
CORE_MU_J_BAR = 0.30
CORE_FJ_J_BAR = 0.40
HELP_MIN = 35
PULL_W9_BAR = 0.040
EQ_D_HI = 0.050

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "scaled Stieltjes only"
                       if not bad else "; ".join(bad))


def stieltjes_exact(nodes, wts, n_upto):
    pk = [Fr(1)] * len(nodes)
    pkm = [Fr(0)] * len(nodes)
    hs = [sum(w * p * p for w, p in zip(wts, pk))]
    beta = []
    for _k in range(n_upto):
        a = sum(w * x * p * p
                for w, x, p in zip(wts, nodes, pk)) / hs[-1]
        b = hs[-1] / hs[-2] if len(hs) > 1 else Fr(0)
        nx = [(x - a) * p - b * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(sum(w * p * p for w, p in zip(wts, pk)))
        beta.append(hs[-1] / hs[-2])
    return beta


def mu_gams(x, w, n_upto):
    """scaled monic Stieltjes (overflow-safe)."""
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    Ls = Ls_m = 0.0
    h = float(np.sum(w * q * q))
    eta_m = h
    gams = []
    for k in range(n_upto):
        alh = float(np.sum(w * x * q * q)) / h
        if k == 0:
            px = (x - alh) * q
        else:
            ge = (h / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (x - alh) * q - ge * fc * qm
        sc = max(float(np.max(np.abs(px))), 1e-300)
        qm, eta_m, Ls_m = q, h, Ls
        q = px / sc
        Ls += math.log(sc)
        h = float(np.sum(w * q * q))
        gams.append((h / eta_m) * math.exp(2.0 * (Ls - Ls_m)))
    return np.array(gams)


def signed_chain(xs, ws, ys, vs, n_upto):
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    gams = []
    for _n in range(n_upto):
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if _n == 0:
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
        gams.append((eta / eta_m) * math.exp(2.0 * (Ls - Ls_m)))
    return np.array(gams)


def last12(g):
    g12 = np.asarray(g[-12:], float)
    dbox = float(np.max(np.abs(g12 - 0.25)))
    jmp = (float(np.max(np.abs(np.log(g12[1:] / g12[:-1]))))
           if np.all(g12 > 0) else float("inf"))
    return dbox, jmp


def in_box(g):
    d, j = last12(g)
    return d <= BOX + 1e-12 and j <= JUMP, d, j


def fejer_w(x, mass):
    f = np.maximum(1.0 - np.asarray(x, float), 1e-15)
    return f * (mass / float(np.sum(f)))


def eps_ratio(x, w):
    f = np.maximum(1.0 - np.asarray(x, float), 1e-15)
    r = np.asarray(w, float) / f
    r = r / float(np.mean(r))
    return r - 1.0, r


def full_grid(h):
    L = 4 * h - 2
    uf = np.unique(np.minimum(np.arange(L), L - np.arange(L)))
    xf = np.cos(2.0 * math.pi * uf / L)
    mpos = xf < 1.0 - 1e-12
    xf = xf[mpos]
    return xf, fejer_w(xf, 1.0)


def part_a_standalone():
    section("S1  LEG A -- JACOBI-(0,1), CHEBYSHEV-U, HOMOGENEITY")
    n_bad = 0
    for n in range(1, 80):
        g = Fr(n) * Fr(n + 1) / (Fr(2 * n + 1) ** 2)
        if abs(g - Fr(1, 4)) != Fr(1, 4) / (Fr(2 * n + 1) ** 2):
            n_bad += 1
    check("G01-jacobi-0-1-Q",
          n_bad == 0,
          "n=1..79 exact |g-1/4|=1/(4(2n+1)^2)")

    x = Fr(2, 5)
    p0, p1 = Fr(1), x
    p2 = x * p1 - Fr(1, 4) * p0
    check("G02-chebyshev-U-quarters",
          p2 == x * x - Fr(1, 4),
          "monic U: p2=x^2-1/4, gamma_k=1/4 (k>=1)")

    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1, 5)] * 5
    b1 = stieltjes_exact(nodes, wts, 3)
    b3 = stieltjes_exact(nodes, [Fr(3) * w for w in wts], 3)
    check("G03-gamma-homogeneous-Q",
          b1 == b3,
          "monic gamma invariant under w -> 3w")

    check("G04-jump-not-implied",
          math.log(5.0 / 3.0) > JUMP,
          "log(5/3)=%.4f > 2/5" % math.log(5.0 / 3.0))

    # small full cosine + Fejer ~ 1/4 (Bernstein-Szego discrete)
    xf, wf = full_grid(12)
    gf = mu_gams(xf, wf, min(12, len(xf) - 2))
    dev = float(np.max(np.abs(gf[1:] - 0.25)))
    check("G05-small-fullgrid-Fejer",
          dev < 5.0e-4,
          "h=12 S=%d max|g-1/4|_{k>=2}=%.3e (O(1/S^2); w9 is 2e-6)"
          % (len(xf), dev))

    check("G06-box-constants",
          BOX == 1.0 / 16.0 and JUMP == 2.0 / 5.0,
          "r379 box 1/16 and jump 2/5")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- w9 Fejer vs mu, kills")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2
    mass = float(ws.sum())
    wf = fejer_w(xs, mass)
    wy = fejer_w(ys, float(vs.sum()))
    eps, ratio = eps_ratio(xs, ws)
    kappa = float(np.max(ratio) / np.min(ratio))
    einf = float(np.max(np.abs(eps)))

    print("    w9 chains n=%d S+=%d ..." % (n, len(xs)), flush=True)
    g_mu = mu_gams(xs, ws, n)
    g_fj = mu_gams(xs, wf, n)
    g_sf = signed_chain(xs, wf, ys, wy, n)
    weq = np.full_like(ws, mass / len(ws))
    g_eq = mu_gams(xs, weq, n)

    imu, dmu, jmu = in_box(g_mu)
    ifj, dfj, jfj = in_box(g_fj)
    isf, dsf, jsf = in_box(g_sf)
    ieq, deq, jeq = in_box(g_eq)
    pull = float(np.max(np.abs(g_mu[-12:] - g_fj[-12:])))

    check("G10-w9-mu-inside",
          imu and dmu < W9_MU_D_HI and jmu < W9_MU_J_HI,
          "|g-1/4|=%.5f jump=%.4f (positive mu-chain)"
          % (dmu, jmu))
    check("G11-w9-Fejer-occupied-inside",
          ifj and W9_FJ_D_LO < dfj < W9_FJ_D_HI,
          "|g-1/4|=%.5f jump=%.4f -- ALREADY IN; r381 0.071 "
          "was signed Fejer" % (dfj, jfj))
    check("G12-w9-signed-Fejer-outside",
          (not isf) and dsf >= W9_SF_D_FLOOR,
          "|g-1/4|=%.5f jump=%.4f (r381 0.071 reproduced)"
          % (dsf, jsf))
    check("G13-w9-equal-wt-inside",
          ieq and deq < EQ_D_HI,
          "equal-wt occupied |g-1/4|=%.5f jump=%.4f" % (deq, jeq))
    check("G14-kappa-useless",
          kappa >= KAPPA_FLOOR and einf > 1.0,
          "kappa=%.1f ||eps||=%.3f; ratio image misses the box"
          % (kappa, einf))
    check("G15-directed-pull",
          pull < PULL_W9_BAR and dmu < dfj,
          "|mu-Fejer|_12=%.5f (d_arm pulls IN at w9)" % pull)

    xf, wff = full_grid(N)
    nfg = min(n, len(xf) - 2)
    print("    full-grid Fejer S=%d n=%d ..." % (len(xf), nfg),
          flush=True)
    gfg = mu_gams(xf, wff, nfg)
    dev_fg = float(np.max(np.abs(gfg[1:] - 0.25)))
    check("G16-fullgrid-Bernstein-Szego",
          dev_fg < FULLGRID_BAR
          and abs(len(xf) - (len(xs) + len(ys))) <= 1,
          "max|g-1/4|_{k>=2}=%.3e union=%d fullS=%d"
          % (dev_fg, len(xs) + len(ys), len(xf)))

    rng = np.random.RandomState(PERM_SEED)
    wperm = ws.copy()
    rng.shuffle(wperm)
    gperm = mu_gams(xs, wperm, n)
    ip, dp, jp = in_box(gperm)
    check("G17-perm-seed3-kills",
          (not ip) and dp >= PERM_D_FLOOR,
          "perm seed=%d |g-1/4|=%.5f jump=%.4f -- NOT "
          "construction-pure" % (PERM_SEED, dp, jp))

    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    ns = int(ds["n_max"]) - 2
    gss = mu_gams(ds["xs"], ds["ws"], ns)
    iss, dss, jss = in_box(gss)
    check("G18-scramble-seed-mu-kills",
          (not iss) and dss >= W9_SF_D_FLOOR,
          "scr-seed=%d mu |g-1/4|=%.5f jump=%.4f (occupation moves)"
          % (SCR_SEED, dss, jss))

    a = 0.95
    alt = 1.0 + a * np.array([(-1) ** i for i in range(len(xs))])
    walt = wf * np.maximum(alt, 1e-12)
    walt *= mass / walt.sum()
    galt = mu_gams(xs, walt, n)
    ia, da, ja = in_box(galt)
    check("G19-two-period-weight-stays",
          ia,
          "a=0.95 |g-1/4|=%.5f jump=%.4f (smooth osc does NOT kill)"
          % (da, ja))

    check("G19b-mutant-JUMP-1-10",
          jmu > 0.10,
          "mu jump=%.4f > 1/10: the jump half is not 1/10-tight"
          % jmu)

    if smoke:
        return

    section("S3  FULL CENSUS -- core-42 + perm battery")
    core = list(V.admissible_indices())
    check("G20-ladder-size",
          len(core) == CORE_N,
          "core %d" % len(core))

    n_mu_out = n_fj_out = help_ = 0
    max_mu = max_fj = max_jmu = max_jfj = 0.0
    for i, kz in enumerate(core):
        dk = HS.window_data(kz)
        nk = int(dk["n_max"]) - 2
        xk, wk = dk["xs"], dk["ws"]
        wfk = fejer_w(xk, float(wk.sum()))
        gm = mu_gams(xk, wk, nk)
        gf = mu_gams(xk, wfk, nk)
        dm, jm = last12(gm)
        df, jf = last12(gf)
        max_mu, max_fj = max(max_mu, dm), max(max_fj, df)
        max_jmu, max_jfj = max(max_jmu, jm), max(max_jfj, jf)
        if dm > BOX or jm > JUMP:
            n_mu_out += 1
        if df > BOX or jf > JUMP:
            n_fj_out += 1
        if dm < df:
            help_ += 1
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)

    check("G21-core42-mu-inside",
          n_mu_out == 0
          and max_mu < CORE_MU_D_BAR and max_jmu < CORE_MU_J_BAR,
          "OUT %d/42 maxd=%.5f maxj=%.4f" % (n_mu_out, max_mu, max_jmu))
    check("G22-core42-Fejer-occ-inside",
          n_fj_out == 0
          and max_fj < CORE_FJ_D_BAR and max_jfj < CORE_FJ_J_BAR,
          "OUT %d/42 maxd=%.5f maxj=%.4f (jump margin %.4f)"
          % (n_fj_out, max_fj, max_jfj, JUMP - max_jfj))
    check("G23-d-arm-helps",
          help_ >= HELP_MIN,
          "d_arm pulls IN on %d/42" % help_)
    check("G24-Fejer-jump-thin",
          max_jfj > 0.35,
          "Fejer-occ max jump=%.4f vs 2/5 -- d_arm is load-bearing "
          "for JUMP headroom" % max_jfj)

    n_out = 0
    worst = 0.0
    for seed in range(1, N_PERM + 1):
        rng = np.random.RandomState(seed)
        w = ws.copy()
        rng.shuffle(w)
        dd, jj = last12(mu_gams(xs, w, n))
        worst = max(worst, dd)
        if dd > BOX or jj > JUMP:
            n_out += 1
    check("G25-perm-battery-kills",
          n_out >= PERM_OUT_MIN,
          "%d/%d perm seeds OUT, worst |g-1/4|=%.5f"
          % (n_out, N_PERM, worst))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("g_eps_mu_probe -- LEMMA.G_EPS_MU.01 (round 390)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_construction(smoke)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = "G_EPS_MU LEMMA SMOKE" if smoke else "G_EPS_MU LEMMA"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
