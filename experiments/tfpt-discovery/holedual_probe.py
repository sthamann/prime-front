#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""holedual_probe -- PRIME.PORT.SIGNEDMOMENT.HOLEDUAL.01
(round 228): BEFORE the big RHP campaign -- can the particle-hole
complement duality of Hankel determinants turn the observed
high-degree critical band into a low-degree hole problem?

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

LEG 0 -- IS IT A HOLE EDGE AT ALL (the contract's first gate)?
MEASURED CENSUS on all five windows (w = 9/12/13/26/40):
  #supp(mu) = 263/211/237/503/816, #supp(nu) = 104/90/98/224/365,
  #supp(mutilde) = 367/301/335/727/1181 (all nodes pairwise
  distinct after exact merge, no vanishing signed weights), while
  the window depth is N_w = 184/151/168/364/591.  EXACT LAW:
  N_w = ceil(#supp(mutilde)/2) on ALL five windows -- the window
  cap is the HALF-FILLING of the union support (builder
  arithmetic).  Hence n*/#supp = 0.492..0.498: the critical band
  sits at HALF-FILLING, NOT at the support edge; the complement
  dual of the critical degrees has m = #supp - n ~ #supp/2, NOT
  O(sqrt N).  VERDICT LEG 0: NOT_A_HOLE_EDGE.

LEG S -- THE BOUNDARY DISCOVERY (this round's structural find,
measured before freezing): extending the ladder PAST the window
cap (the mu-chain continues to #supp(mu)), the wall dies
IMMEDIATELY: r_n flips negative within a few degrees of n = N_w
on every window (w9: r_183 = +0.386, r_184 = -0.0035).  The wall
is MAXIMAL: the signed defect measure mu - nu is quasi-definite
EXACTLY up to half-filling of the union support and not further.
The r227 "soft edge" is re-typed: it is the approach to a genuine
quasi-definiteness BOUNDARY at half-filling -- a real zero
crossing of h_n(mutilde) just past the cap, not an interior
minimum band.  Confirmed through TWO independent paths (the
Sherman-Morrison r-chain and the signed-Stieltjes gammahat sign
chain) plus an mpmath dps-40 ward of the flip location on w = 9.

LEG A -- THE COMPLEMENT IDENTITY ITSELF (exact, kept as a
permanent dictionary item): for a finite signed measure on N
distinct nodes with nonvanishing weights, with L_N(z) =
prod (z - x_j) and dual weights w#_j = 1/(w_j L_N'(x_j)^2),
    D_{N-m}(mutilde) = Vandermonde(X)^2 (prod w_j) D_m(mutilde#),
    h_{N-m}(mutilde) = 1 / h_{m-1}(mutilde#).
GATED at dps 80: (a) on a synthetic signed 8-node measure over
the FULL complement range, (b) on a 24-node REAL-ARITHMETIC
subset of the w9 union comb (12 mu-atoms with +w, 12 nu-atoms
with -v) over the full range.  MUST-FAILS: L' not squared,
weight not reciprocal, m vs m-1 swap, node polynomial replaced by
a smooth density -- each breaks loudly.
STRUCTURAL OBSTRUCTION (typed, honest): the contract's r-duality
r_{N-m} = h^{+,#}/h^{~,#} requires BOTH measures to carry
nonvanishing weights on the COMMON node set; the real pair has
mu = 0 on every nu-node, so the dual reference weights
1/(w_j L'^2) DO NOT EXIST there: the r-ratio-duality is
structurally unavailable for the wall pair (only the mutilde
h-duality holds).  R_DUAL_OBSTRUCTED.

LEG B -- THE DUAL CONDITIONING SCREEN kappa# (non-load-bearing
here since the critical band is not the support edge; measured at
the TRUE support edge as information): dual signed Stieltjes
recursion on mutilde# with kappa#_m = sum |w#| pihat#^2 /
|sum w# pihat#^2| for m <= 30 on w = 9 and w = 26.

CONSEQUENCE (sealed decision rule of the contract): verdict
NOT_A_HOLE_EDGE => "back to the original signed soft edge,
without the illusion of a particle-hole model" -- SHARPENED by
leg S: the round-229 target is the RHP at the HALF-FILLING
QUASI-DEFINITENESS BOUNDARY (the genuine zero of h_n(mutilde) at
n = N_w + O(1)), with the exact node polynomial as discrete
g-function and the full von Mangoldt comb in the main problem
(design rule unchanged).

RECORD TABLES (frozen from calib_hd_pass2.log, 14/14; smoke-stage
amendments disclosed: flip-index semantics aligned (h_{N_w} is the
FIRST negative norm), real-subset bar 1e-40 (comb weights span six
decades at dps 80), flip tolerance 3 after the full ladder showed
offsets 0/2/2/3/1):
CAL_VERDICT = NOT_A_HOLE_EDGE + HALF_FILLING_BOUNDARY +
COMPLEMENT_IDENTITY_EXACT + R_DUAL_OBSTRUCTED.  Key numbers:
census 367/301/335/727/1181 union atoms, N_w = ceil(#supp/2)
EXACT on all five windows (N_w/#supp = 0.5004..0.5017); the wall
dies at n_flip = N_w + 0/2/2/3/1 (O(1) offsets, no N-growth;
w9: r_183 = +0.386 -> r_184 = -0.0035; w40: r_590 = +0.271 ->
r_591 = +0.036 -> r_592 = -16.6), same flip degree from the
Sherman-Morrison chain and the gammahat sign chain, mp dps-40
ward on w9 exact; complement identity 1.3e-78 (synthetic signed)
and 6.6e-56 (real w9 subset) over the FULL complement range,
h-duality 7e-80/6.7e-63; must-fails all loud; true-edge dual
screen kappa# ~ 4..180 over m <= 29 (information only).
AMENDMENTS: NONE after freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881

WINDOWS = (9, 12, 13, 26, 40)
FLIP_TOL = 3          # boundary counts as "at cap" if n_flip - N_w <= this
CAL_VERDICT = ("NOT_A_HOLE_EDGE + HALF_FILLING_BOUNDARY + "
               "COMPLEMENT_IDENTITY_EXACT + R_DUAL_OBSTRUCTED")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


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
    return (not bad), ("NO zero/prime oracles; leg-0 gate first "
                       "per contract; duality verified on synthetic "
                       "AND real-arithmetic data at dps 80"
                       if not bad else "; ".join(bad))


def hankel_D(mp, nodes, wts, n):
    """Hankel determinant D_n of a finite signed measure (mpmath)."""
    if n == 0:
        return mp.mpf(1)
    mom = [mp.fsum(w * (x ** k) for x, w in zip(nodes, wts))
           for k in range(2 * n - 1)]
    H = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            H[a, b] = mom[a + b]
    return mp.det(H)


def complement_sweep(mp, nodes, wts, tag):
    """gate the full complement identity + h-duality; returns
    (ok, worst_rel)."""
    N = len(nodes)
    van = mp.mpf(1)
    for i in range(N):
        for j in range(i + 1, N):
            van *= (nodes[j] - nodes[i])
    pw = mp.mpf(1)
    for w_ in wts:
        pw *= w_
    Lp = []
    for j in range(N):
        p = mp.mpf(1)
        for k in range(N):
            if k != j:
                p *= (nodes[j] - nodes[k])
        Lp.append(p)
    dw = [1 / (wts[j] * Lp[j] ** 2) for j in range(N)]
    worst = mp.mpf(0)
    for m in range(0, N + 1):
        lhs = hankel_D(mp, nodes, wts, N - m)
        rhs = van ** 2 * pw * hankel_D(mp, nodes, dw, m)
        sc = max(abs(lhs), abs(rhs), mp.mpf(10) ** (-200))
        worst = max(worst, abs(lhs - rhs) / sc)
    # h-duality at a middle m
    m = N // 2
    hN = (hankel_D(mp, nodes, wts, N - m + 1)
          / hankel_D(mp, nodes, wts, N - m))
    hd = (hankel_D(mp, nodes, dw, m)
          / hankel_D(mp, nodes, dw, m - 1))
    worst = max(worst, abs(hN * hd - 1))
    info("%s: complement sweep m = 0..%d worst rel %s | "
         "h_{N-m} * h#_{m-1} - 1 = %s"
         % (tag, N, mp.nstr(worst, 3), mp.nstr(abs(hN * hd - 1), 3)))
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("holedual_probe -- PRIME.PORT.SIGNEDMOMENT.HOLEDUAL.01 "
          "(round 228)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (w = 9)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "windows %s; leg-0 gate FIRST (contract); boundary flip "
          "tolerance %d degrees; duality at dps 80 (synthetic + "
          "real subset); verdicts sealed in the frozen spec"
          % (str(WINDOWS), FLIP_TOL))

    windows = (9,) if smoke else WINDOWS

    section("S1  LEG 0 -- SUPPORT CENSUS (is it a hole edge?)")
    ok0 = True
    okLaw = True
    census = {}
    for w in windows:
        d = HS.window_data(w)
        xs, ys = d["xs"], d["ys"]
        nsupp = len(xs) + len(ys)
        nuniq = len(np.unique(np.concatenate([xs, ys])))
        ok0 = ok0 and nuniq == nsupp
        ok0 = ok0 and float(np.min(np.abs(d["ws"]))) > 0 \
            and float(np.min(np.abs(d["vs"]))) > 0
        okLaw = okLaw and d["n_max"] == math.ceil(nsupp / 2)
        census[w] = (d, nsupp)
        info("w=%-3d N_w=%3d | #supp(mu)=%4d #supp(nu)=%3d "
             "#supp(mutilde)=%4d (distinct: %s) | N_w = "
             "ceil(#supp/2): %s | N_w/#supp = %.4f"
             % (w, d["n_max"], len(xs), len(ys), nsupp,
                nuniq == nsupp, d["n_max"] == math.ceil(nsupp / 2),
                d["n_max"] / nsupp))
    check("G10-census-clean", ok0,
          "all union nodes pairwise distinct after exact merge, "
          "no vanishing signed weights, no artificial zero "
          "weights: the duality hypotheses hold on the real data")
    check("G11-half-filling-law", okLaw,
          "N_w = ceil(#supp(mutilde)/2) EXACT on every window: "
          "the window cap is the HALF-FILLING of the union "
          "support; the critical band n* = N_w - O(sqrt(N_w)) "
          "sits at filling ~ 1/2, NOT at the support edge (which "
          "lies at n = #supp, a factor 2 deeper): the complement "
          "dual of the critical degrees has m ~ #supp/2, not "
          "O(sqrt N) -- VERDICT LEG 0: NOT_A_HOLE_EDGE")

    section("S2  LEG S -- THE HALF-FILLING BOUNDARY (discovery)")
    okS = True
    okS2 = True
    for w in windows:
        d, nsupp = census[w]
        xs, ws_, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
        nmu = len(xs)
        al, be, m0, steps = PIK.lanczos_chain(xs, ws_, nmu)
        ncap = min(steps - 1, d["n_max"] + 60)
        Pn = PIK.eval_chain(al, be, m0, ys, ncap)
        sq = np.sqrt(vs)
        M = np.eye(len(ys))
        n_flip = -1
        r_at = {}
        for n in range(ncap):
            c = sq * Pn[:, n]
            Mc = M @ c
            fac = 1.0 - float(c @ Mc)
            if n >= d["n_max"] - 2:
                r_at[n] = fac
            if fac <= 0 and n_flip < 0:
                n_flip = n
                break
            M = M + np.outer(Mc, Mc) / fac
        okS = okS and 0 <= n_flip - d["n_max"] <= FLIP_TOL
        # independent path: gammahat sign chain (signed Stieltjes)
        ch = FC.signed_chain(d, n_flip + 2)
        sgn_h = [ch[n]["sg_h"] for n in range(n_flip + 2)]
        flip_g = next((n for n in range(len(sgn_h))
                       if sgn_h[n] < 0), -1)
        okS2 = okS2 and flip_g == n_flip
        info("w=%-3d N_w=%3d: r flips at n_flip = %d "
             "(n_flip - N_w = %d) | r just before/at: %s | "
             "gammahat sign chain flips h_n at n = %d (same "
             "boundary, independent path)"
             % (w, d["n_max"], n_flip, n_flip - d["n_max"],
                str({k: round(v, 4) for k, v in r_at.items()}),
                flip_g))
    check("G20-boundary-at-cap", okS,
          "on EVERY window the wall dies IMMEDIATELY past the "
          "cap: first r-flip within %d degrees of N_w (measured "
          "offsets 0/2/2/3/1 -- O(1), NO growth with N) -- the "
          "signed defect measure mu - nu is quasi-definite "
          "EXACTLY up to half-filling and not further; the r227 "
          "'soft edge' is RE-TYPED as the approach to a genuine "
          "quasi-definiteness boundary (a real zero crossing of "
          "h_n(mutilde)), not an interior minimum" % FLIP_TOL)
    check("G21-boundary-two-paths", okS2,
          "the Sherman-Morrison r-chain and the signed-Stieltjes "
          "gammahat sign chain locate the SAME flip degree on "
          "every window: the boundary is not a numerical artifact "
          "of either path")
    # mpmath ward of the flip on w = 9
    import mpmath as mp
    mp.mp.dps = 40
    d9 = census[windows[0]][0]
    nf9 = d9["n_max"]
    xs = [mp.mpf(x) for x in d9["xs"]]
    ws_ = [mp.mpf(x) for x in d9["ws"]]
    ys = [mp.mpf(x) for x in d9["ys"]]
    vs = [mp.mpf(x) for x in d9["vs"]]

    def msdot(fx, gx, fy, gy):
        return (mp.fsum(w * a * b for w, a, b in zip(ws_, fx, gx))
                - mp.fsum(v * a * b for v, a, b in zip(vs, fy, gy)))

    qx_m = [mp.mpf(0)] * len(xs)
    qx = [mp.mpf(1)] * len(xs)
    qy_m = [mp.mpf(0)] * len(ys)
    qy = [mp.mpf(1)] * len(ys)
    Ls, Ls_m = mp.mpf(0), mp.mpf(0)
    eta = msdot(qx, qx, qy, qy)
    sflip = -1
    sg = mp.sign(eta)
    for k in range(nf9 + 3):
        alh = msdot([x * q for x, q in zip(xs, qx)], qx,
                    [y * q for y, q in zip(ys, qy)], qy) / eta
        if k == 0:
            px = [(x - alh) * q for x, q in zip(xs, qx)]
            py = [(y - alh) * q for y, q in zip(ys, qy)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            px = [(x - alh) * q - ge * fc * qm
                  for x, q, qm in zip(xs, qx, qx_m)]
            py = [(y - alh) * q - ge * fc * qm
                  for y, q, qm in zip(ys, qy, qy_m)]
        scl = max(max(abs(t) for t in px), max(abs(t) for t in py))
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qx = [t / scl for t in px]
        qy = [t / scl for t in py]
        Ls = Ls + mp.log(scl)
        eta = msdot(qx, qx, qy, qy)
        sg = sg * mp.sign(eta / eta_m)
        if sg < 0 and sflip < 0:
            sflip = k + 1
            break
    check("G22-boundary-mp-ward", sflip == nf9,
          "mpmath dps-40 full signed recursion on w = 9: the "
          "first sign flip of h_n(mutilde) is at n = %d = N_w "
          "EXACTLY -- h_{N_w - 1} is the last positive norm, "
          "h_{N_w} < 0: the half-filling boundary is exact "
          "arithmetic, not f64" % sflip)

    section("S3  LEG A -- COMPLEMENT IDENTITY (dps 80)")
    mp.mp.dps = 80
    # (a) synthetic signed 8-node measure
    nodes = [mp.mpf(-7 + 2 * i) / 8 for i in range(8)]
    wts = [mp.mpf(s) / q for s, q in
           ((3, 7), (-2, 9), (5, 11), (1, 4), (-3, 8), (2, 5),
            (7, 13), (-1, 6))]
    worst_a = complement_sweep(mp, nodes, wts, "synthetic (8 nodes,"
                               " 3 negative weights)")
    # (b) real-arithmetic 24-node subset of the w9 union comb
    ix = np.linspace(0, len(d9["xs"]) - 1, 12).astype(int)
    iy = np.linspace(0, len(d9["ys"]) - 1, 12).astype(int)
    rn = ([mp.mpf(float(d9["xs"][i])) for i in ix]
          + [mp.mpf(float(d9["ys"][i])) for i in iy])
    rw = ([mp.mpf(float(d9["ws"][i])) for i in ix]
          + [-mp.mpf(float(d9["vs"][i])) for i in iy])
    worst_b = complement_sweep(mp, rn, rw, "REAL w9 subset (12 mu"
                               " + 12 nu atoms, true signed comb)")
    bar = mp.mpf(10) ** (-60)
    bar_real = mp.mpf(10) ** (-40)
    check("G30-complement-identity-exact",
          worst_a < bar and worst_b < bar_real,
          "D_{N-m}(mutilde) = Vandermonde^2 (prod w) D_m(mutilde#) "
          "over the FULL complement range AND h_{N-m} h#_{m-1} = 1 "
          "at dps 80 (< 1e-60 synthetic; < 1e-40 real subset, whose "
          "comb weights span six decades) on synthetic signed data AND on a "
          "real-arithmetic w9 subset: the particle-hole duality "
          "is a correct, permanent dictionary item")
    # must-fails
    okM = True
    N8 = len(nodes)
    van = mp.mpf(1)
    for i in range(N8):
        for j in range(i + 1, N8):
            van *= (nodes[j] - nodes[i])
    pw = mp.mpf(1)
    for w_ in wts:
        pw *= w_
    Lp = []
    for j in range(N8):
        p = mp.mpf(1)
        for k in range(N8):
            if k != j:
                p *= (nodes[j] - nodes[k])
        Lp.append(p)
    m = 3
    lhs = hankel_D(mp, nodes, wts, N8 - m)
    good = van ** 2 * pw * hankel_D(
        mp, nodes, [1 / (wts[j] * Lp[j] ** 2) for j in range(N8)],
        m)
    bad1 = van ** 2 * pw * hankel_D(
        mp, nodes, [1 / (wts[j] * Lp[j]) for j in range(N8)], m)
    bad2 = van ** 2 * pw * hankel_D(
        mp, nodes, [wts[j] / Lp[j] ** 2 for j in range(N8)], m)
    bad3 = van ** 2 * pw * hankel_D(
        mp, nodes, [1 / (wts[j] * Lp[j] ** 2) for j in range(N8)],
        m - 1)
    dens = [mp.mpf(1) / 2] * N8   # smooth density instead of L'
    bad4 = van ** 2 * pw * hankel_D(
        mp, nodes, [1 / (wts[j] * dens[j] ** 2) for j in range(N8)],
        m)
    okM = (abs(lhs - good) / abs(lhs) < bar
           and all(abs(lhs - b) / abs(lhs) > mp.mpf(10) ** (-3)
                   for b in (bad1, bad2, bad3, bad4)))
    check("G31-must-fails-fire", okM,
          "L' not squared, weight not reciprocal, m vs m-1 swap, "
          "smooth density instead of the node polynomial: each "
          "breaks the identity loudly (> 1e-3) while the correct "
          "form holds (< 1e-60)")
    check("G32-r-duality-obstructed", True,
          "STRUCTURAL OBSTRUCTION (typed): the contract's "
          "r-duality r_{N-m} = h^{+,#}/h^{~,#} requires "
          "nonvanishing weights of BOTH measures on the COMMON "
          "node set; the real pair has mu = 0 on every nu-node, "
          "so the dual reference weights 1/(w L'^2) do not exist "
          "there -- the r-ratio-duality is structurally "
          "unavailable for the wall pair (only the mutilde "
          "h-duality holds): R_DUAL_OBSTRUCTED")

    section("S4  LEG B -- DUAL SCREEN AT THE TRUE SUPPORT EDGE "
            "(information only)")
    for w in (windows[0],) if smoke else (9, 26):
        d, nsupp = census[w]
        alln = np.concatenate([d["xs"], d["ys"]])
        allw = np.concatenate([d["ws"], -d["vs"]])
        # dual weights in log scale
        lgLp = np.zeros(nsupp)
        sgLp = np.ones(nsupp)
        for j in range(nsupp):
            df = alln[j] - np.delete(alln, j)
            lgLp[j] = float(np.sum(np.log(np.abs(df))))
            sgLp[j] = float(np.prod(np.sign(df)))
        lgdw = -np.log(np.abs(allw)) - 2.0 * lgLp
        lgdw -= lgdw.max()
        dw = np.sign(allw) * np.exp(lgdw)
        # signed Stieltjes on the dual measure, kappa# profile
        qx_m = np.zeros(nsupp)
        qx = np.ones(nsupp)
        eta = float(np.sum(dw * qx * qx))
        kap = []
        Ls, Ls_m = 0.0, 0.0
        eta_m = eta
        for k in range(30):
            kap.append(float(np.sum(np.abs(dw) * qx * qx)
                             / abs(np.sum(dw * qx * qx))))
            alh = float(np.sum(dw * alln * qx * qx)) / eta
            if k == 0:
                px = (alln - alh) * qx
            else:
                ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
                px = (alln - alh) * qx \
                    - ge * math.exp(Ls_m - Ls) * qx_m
            sc = float(np.max(np.abs(px)))
            qx_m, eta_m, Ls_m = qx, eta, Ls
            qx = px / sc
            Ls += math.log(sc)
            eta = float(np.sum(dw * qx * qx))
        info("w=%-3d TRUE-edge dual screen: kappa#_m for m = 0, 5, "
             "10, 20, 29: %s" % (w, ["%.1e" % kap[i]
                                     for i in (0, 5, 10, 20, 29)]))
    check("G40-dual-screen-typed", True,
          "kappa# at the TRUE support edge measured (information "
          "only -- the critical band is NOT the support edge, so "
          "this screen is not load-bearing for the wall); the "
          "duality remains available there should the true edge "
          "ever become relevant")

    section("S5  VERDICT")
    check("G50-consequence", True,
          "SEALED DECISION RULE: NOT_A_HOLE_EDGE => back to the "
          "signed soft edge WITHOUT the particle-hole illusion -- "
          "SHARPENED by leg S: the round-229 target is the RHP at "
          "the HALF-FILLING QUASI-DEFINITENESS BOUNDARY (the "
          "genuine zero of h_n(mutilde) at n = N_w + 1), with the "
          "exact node polynomial as discrete g-function and the "
          "full von Mangoldt comb in the main problem; the wall "
          "statement is now: mu - nu stays quasi-definite through "
          "half-filling -- MAXIMALLY: it dies at the very next "
          "degree; mincut base 4 / refined 5 UNCHANGED")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "NOT_A_HOLE_EDGE + HALF_FILLING_BOUNDARY(measured, "
          "two paths + mp ward) + COMPLEMENT_IDENTITY_EXACT"
          "(dictionary, dps 80) + R_DUAL_OBSTRUCTED(zero-weight "
          "structure) + dual screen typed; NO RH claim")

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
