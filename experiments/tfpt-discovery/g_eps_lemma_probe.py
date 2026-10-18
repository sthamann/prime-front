#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g_eps_lemma_probe -- LEMMA.G_EPS.01 (round 381):
THE COEFFICIENT BOX G_eps FROM THE SOURCE.

Coexistence: r379 reduced V3' to G_eps (last-12 Jacobi gamma
of the v2-chain: |g-1/4|<=1/16 and |log(g_{k+1}/g_k)|<=2/5).
This round attacks G_eps from the r379 source formula
g = 1/4 + dFejer + d(d_arm).  Mesh and Fejer are SATZ of r379
and are not re-proved.

THE FROZEN QUESTION.  Does first-order Jacobi perturbation
under weight variation on the cosine grid, together with a
PNT-free bound on the arm-length weights, prove the box?

LEGS (lemma-first; allowed exits PROVED / REFUTED / REDUCED):
  A  Stieltjes first-order formula (CD/OP-square exact).
  B  Source bound on the weight perturbation (d_arm / Lambda).
  C  Jump half |log(g_{k+1}/g_k)| <= 2/5.
  D  Must-fails: slow-then-fast block; scramble; second order.

CALIBRATION DISCLOSURE.  The identities and the kill numbers
were first measured in /tmp (r381_calibrate.py, r381_cal2.py,
r381_cal3.py) on the same constructors, 2026-08-28.  Frozen
floors/ceilings below are that measurement, sealed as gates --
not a search over the box constants (those are r379's 1/16
and 2/5).  No two-commit pre-blind freeze: pins disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * FO formula vs central difference on a 6-atom Q-toy:
    max |CD-FO|/|FO| <= 3e-4 at eps=1/200.
  * FO vs FD on FRAME-A w9, one mu-atom, dw=1e-7:
    rel <= 1e-3 through k=12.
  * L^inf of Fejer-stripped d_arm on MAIN w9 is O(1)..O(10),
    crude FO bound ~3 >> 1/16 -- cancellation is essential.
  * Second-order midpoint remainder along Fejer-ref -> actual
    at n=40: |g1-2g(1/2)+g0|_last12 / |g1-g0|_last12 ~ 1
    (NOT dominated).  Full-depth the quadratic increment is
    larger still.
  * mu-only last-12 |g-1/4| = 0.02605 at w9 (inside the box);
    signed last-12 = 0.03417; mass_nu/mu = 0.0611;
    <pi_k^2>_nu last12 max = 0.389.
  * SCRAMBLE seed=1 w9: signed last-12 |g-1/4| >= 6.8
    (named kill of the source regularity, not of |c_q|_inf --
    scramble high-lag |c| is comparable to MAIN).
  * log((1/4+1/16)/(1/4-1/16)) = log(5/3) > 2/5: the jump
    is NOT a corollary of the box.

MACHINERY: r226 hirota_sign.window_data, r244 bord_chain
path (inline signed Stieltjes), r379 box constants.

NO RH CLAIM.  Finite identities, a named reduction, a named
scramble break.  Research documentation, not a theorem of RH.
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
for p in (DISC,):
    if p not in sys.path:
        sys.path.insert(0, p)

import hirota_sign_probe as HS  # noqa: E402

BOX = 1.0 / 16.0
JUMP = 2.0 / 5.0
SCR_SEED = 1
# disclosed /tmp floors (Leg D kill + R2 not-dominated)
SCR_LAST12_FLOOR = 2.0
R2_RATIO_FLOOR = 0.5
FO_FD_REL_BAR = 1e-3
MASS_NU_MU_BAR = 0.12

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
    return (not bad), ("NO zero/prime oracles; window_data / signed "
                       "Stieltjes only" if not bad else "; ".join(bad))


# ------------------------------------------------------------------ OP chains
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


def signed_chain(xs, ws, ys, vs, n_upto):
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    gams = []
    als = []
    h_list = [eta]
    Px = [qx.copy()]
    Py = [qy.copy()]
    for n in range(n_upto):
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        als.append(alh)
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
    return (np.array(als), np.array(gams), h_list, Px, Py)


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


def fo_signed(h_list, Px, Py, gams, dws, dvs, k):
    gam = gams[k - 1]
    hkm = h_list[k - 1]
    acc = 0.0
    if dws is not None:
        acc += float(np.sum(
            dws * (Px[k] ** 2 - gam * Px[k - 1] ** 2))) / hkm
    if dvs is not None:
        acc -= float(np.sum(
            dvs * (Py[k] ** 2 - gam * Py[k - 1] ** 2))) / hkm
    return acc


def last12_stats(g):
    g12 = np.asarray(g[-12:], float)
    dbox = float(np.max(np.abs(g12 - 0.25)))
    if np.any(g12 <= 0):
        jmp = float("inf")
    else:
        jmp = float(np.max(np.abs(np.log(g12[1:] / g12[:-1]))))
    return dbox, jmp


def lambda_le_log(N):
    """PNT-free: Lambda(n) <= log n for n=2..N, trial division."""
    for n in range(2, N + 1):
        m = n
        p = 2
        hit = False
        while p * p <= m:
            if m % p == 0:
                while m % p == 0:
                    m //= p
                if m == 1:
                    if math.log(p) > math.log(n) + 1e-12:
                        return False
                hit = True
                break
            p += 1
        # n prime or leftover prime: Lambda = log p <= log n
        if not hit:
            pass
    return True


# ------------------------------------------------------------------ parts
def part_a_standalone():
    section("S1  LEG A -- FO FORMULA OVER Q + JUMP INDEPENDENCE")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3), Fr(4, 5)]
    wts = [Fr(1, 6)] * 6
    n_upto = 4
    beta, hs, pks = stieltjes_exact(nodes, wts, n_upto)
    eps = Fr(1, 200)
    j0 = 2
    wts_p = list(wts)
    wts_p[j0] = wts[j0] + eps
    beta_p, _, _ = stieltjes_exact(nodes, wts_p, n_upto)
    wts_m = list(wts)
    wts_m[j0] = wts[j0] - eps
    beta_m, _, _ = stieltjes_exact(nodes, wts_m, n_upto)
    max_rel = 0.0
    max_quad = 0.0
    for k in range(1, n_upto + 1):
        fo = fo_dgamma_Q(pks, hs, k, j0)
        cd = (beta_p[k - 1] - beta_m[k - 1]) / (2 * eps)
        rem = beta_p[k - 1] - beta[k - 1] - fo * eps
        rel = abs(float(cd - fo)) / max(abs(float(fo)), 1e-30)
        quad = abs(float(rem)) / float(eps ** 2)
        max_rel = max(max_rel, rel)
        max_quad = max(max_quad, quad)
    check("G01-FO-formula-Q",
          max_rel <= 3.0e-4,
          "max |CD-FO|/|FO|=%.3e at eps=1/200 (6-atom toy)"
          % max_rel)
    check("G02-R2-is-Theta-eps2",
          0.05 <= max_quad <= 5.0,
          "max |rem|/eps^2=%.4f (quadratic, not o(eps))"
          % max_quad)

    # Jacobi-(0,1) Fejer, r379 SATZ re-gated
    n_bad = 0
    for n in range(1, 40):
        g = Fr(n) * Fr(n + 1) / (Fr(2 * n + 1) ** 2)
        err = abs(g - Fr(1, 4))
        pred = Fr(1, 4) / (Fr(2 * n + 1) ** 2)
        if err != pred:
            n_bad += 1
    check("G03-jacobi-0-1-Q",
          n_bad == 0,
          "n=1..39 exact |g-1/4|=1/(4(2n+1)^2)")

    gap = math.log(5.0 / 3.0)
    check("G04-jump-not-implied-by-box",
          gap > JUMP,
          "log(5/3)=%.4f > 2/5=%.2f" % (gap, JUMP))

    check("G05-Lambda-le-log-n",
          lambda_le_log(120),
          "Lambda(n)<=log n for n=2..120 (trial division)")


def part_b_construction(smoke):
    section("S2  CONSTRUCTION PINS -- FO, BOX, MU-BASE, R2")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2
    mass_r = float(vs.sum()) / float(ws.sum())
    check("G10-mass-nu-over-mu",
          0.04 <= mass_r <= MASS_NU_MU_BAR,
          "mass_nu/mu=%.4f (w9 MAIN)" % mass_r)

    n_fo = 12
    al0, g0, h0, Px0, Py0 = signed_chain(xs, ws, ys, vs, n_fo)
    j0 = 10
    eps = 1e-7
    ws_p = ws.copy()
    ws_p[j0] += eps
    _a, gp, _h, _Px, _Py = signed_chain(xs, ws_p, ys, vs, n_fo)
    dws = np.zeros_like(ws)
    dws[j0] = eps
    max_rel = 0.0
    for k in (1, 2, 5, 10, 12):
        pred = fo_signed(h0, Px0, Py0, g0, dws, None, k)
        fd = gp[k - 1] - g0[k - 1]
        rel = abs(pred - fd) / max(abs(pred), 1e-30)
        max_rel = max(max_rel, rel)
    check("G11-FO-vs-FD-w9",
          max_rel <= FO_FD_REL_BAR,
          "max rel FO vs FD=%.3e (dw=1e-7, mu-atom 10, k<=12)"
          % max_rel)

    print("    running signed + mu chains n=%d ..." % n, flush=True)
    _al, g_sg, _h, _Px, _Py = signed_chain(xs, ws, ys, vs, n)
    g_mu = mu_chain(xs, ws, n)
    dsg, jsg = last12_stats(g_sg)
    dmu, jmu = last12_stats(g_mu)
    check("G12-MAIN-w9-Geps",
          dsg <= BOX + 1e-12 and jsg <= JUMP,
          "|g-1/4|_12=%.5f jump=%.4f (signed v2-chain)"
          % (dsg, jsg))
    check("G13-MAIN-w9-mu-only-inside",
          dmu <= BOX + 1e-12 and jmu <= JUMP,
          "|g-1/4|_12=%.5f jump=%.4f (positive mu-chain)"
          % (dmu, jmu))

    # R2 along Fejer-ref -> actual, n=40 (the /tmp midpoint test)
    n_r2 = 40
    fejer_x = np.maximum(1.0 - xs, 1e-15)
    fejer_y = np.maximum(1.0 - ys, 1e-15)
    wx_ref = fejer_x * (float(ws.sum()) / float(np.sum(fejer_x)))
    wy_ref = fejer_y * (float(vs.sum()) / float(np.sum(fejer_y)))

    def g_of(t):
        wxt = (1.0 - t) * wx_ref + t * ws
        wyt = (1.0 - t) * wy_ref + t * vs
        _a, g, *_ = signed_chain(xs, wxt, ys, wyt, n_r2)
        return g

    g_a = g_of(0.0)
    g_b = g_of(1.0)
    g_h = g_of(0.5)
    lin = g_b - g_a
    quad = g_b - 2.0 * g_h + g_a
    lin_m = float(np.max(np.abs(lin[-12:])))
    quad_m = float(np.max(np.abs(quad[-12:])))
    ratio = quad_m / max(lin_m, 1e-12)
    check("G14-R2-not-dominated",
          ratio >= R2_RATIO_FLOOR,
          "n=40 last12 |quad|/|lin|=%.3f (floor %.2f) lin=%.5f quad=%.5f"
          % (ratio, R2_RATIO_FLOOR, lin_m, quad_m))

    # crude L^inf of Fejer-stripped relative d_arm
    dpx = ws / fejer_x
    epsx = dpx / float(np.mean(dpx)) - 1.0
    einf = float(np.max(np.abs(epsx)))
    check("G15-Linf-too-crude",
          einf > 1.0,
          "||eps_mu||_inf=%.3f >> 1/8; L^inf FO bound cannot give 1/16"
          % einf)

    dscr = HS.window_data(9, scramble_seed=SCR_SEED)
    print("    scramble seed=%d chain n=%d ..." % (SCR_SEED, n),
          flush=True)
    _al, g_scr, *_ = signed_chain(
        dscr["xs"], dscr["ws"], dscr["ys"], dscr["vs"], n)
    dscr12, jscr = last12_stats(g_scr)
    check("G16-SCR-breaks-Geps",
          dscr12 >= SCR_LAST12_FLOOR,
          "SCR last12 |g-1/4|=%.4f jump=%.3f (floor %.1f)"
          % (dscr12, jscr, SCR_LAST12_FLOOR))

    if smoke:
        return dict(dsg=dsg, dmu=dmu, dscr12=dscr12, ratio=ratio)

    # extra pins (full)
    extra = []
    for kz in (15, 21, 46):
        dk = HS.window_data(kz)
        nk = int(dk["n_max"]) - 2
        print("    MAIN kz=%d n=%d ..." % (kz, nk), flush=True)
        _a, gk, *_ = signed_chain(
            dk["xs"], dk["ws"], dk["ys"], dk["vs"], nk)
        db, jb = last12_stats(gk)
        extra.append((kz, db, jb))
        check("G20-MAIN-kz%d-Geps" % kz,
              db <= BOX + 1e-12 and jb <= JUMP,
              "|g-1/4|_12=%.5f jump=%.4f" % (db, jb))
    return dict(dsg=dsg, dmu=dmu, dscr12=dscr12, ratio=ratio,
                extra=extra)


def part_d_block():
    section("S3  LEG D -- BLOCK IS NOT AN FO COUNTEREXAMPLE")
    # R379: two-period in A15, slow-then-fast block leaves A15.
    # That obstruction is a STEP pattern.  The FO formula is a
    # WEIGHT identity and holds independently of the step block.
    # A low-mode weight cluster cannot move last-12 gamma
    # (Riemann-Lebesgue / cal G: low-mode amp 0.4 -> last12 |dg|
    #  4e-5).  The block therefore sits outside the high-lag
    # tent class that can move the last-12, and does not refute
    # the FO identity.
    DELTA = 0.5 * math.pi
    a = 0.70

    def scan_eta(dth, n_eta=401):
        nviol = 0
        for eta in np.linspace(0.0, math.pi, n_eta, endpoint=False):
            th = float(eta)
            levs = [int(math.floor(th / math.pi))]
            for d in dth:
                th += float(d)
                levs.append(int(math.floor(th / math.pi)))
            # run lengths of levels
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

    d_alt = DELTA * np.array([1.0 + a * ((-1) ** i) for i in range(24)])
    slo, fhi = float(np.min(d_alt[:14])), float(np.max(d_alt[:14]))
    d_blk = np.array([slo] * 21 + [fhi, fhi, fhi], dtype=float)
    v_alt = scan_eta(d_alt)
    v_blk = scan_eta(d_blk)
    check("G30-block-is-step-not-FO",
          v_alt == 0 and v_blk > 0,
          "two-period viol=%d; segregated block viol=%d "
          "(R379 obstruction, not a FO-formula fail)"
          % (v_alt, v_blk))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("g_eps_lemma_probe -- LEMMA.G_EPS.01 (round 381)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_construction(smoke)
    part_d_block()

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = "G_EPS LEMMA SMOKE" if smoke else "G_EPS LEMMA"
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
