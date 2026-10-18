#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""testing_mnt_law_probe -- PRIME.SUMRULE.MNT.01
(EXPLORATION ONLY, experiments/; round 39 solve-step (b): the
analytic seed of the sum-rule theorem -- the testing quotient as a
Mate-Nevai-Totik two-density law, 2026-08-09).

THE SEED (frozen): MNT universality says (1/h) K_h(y, y) ->
1/(pi sqrt(1 - y^2) w_+(y)) in the bulk of a regular measure
(w_+ = the ac density of mu~+).  The testing quotient then obeys
    T_m = nu~_m K_h(y_m, y_m)
        ~ (h/pi) * nu~_m / (sqrt(1 - y_m^2) w_+(y_m)),
i.e. TESTING IS A TWO-DENSITY STATEMENT: the neg-arm mass per node
against the pos-arm density in equilibrium normalization -- and
T <= 1 becomes the NYQUIST bound nu~_m <= pi sqrt(1-y^2) w_+ / h.
If this law holds in the bulk, the sum-rule/testing theorem
(diagonal half of the wall) reduces to classical MNT/Totik
regularity of the deployed measure family -- provable terrain.

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
controls kz 9):

 M1  THE LAW (bulk): for neg nodes in tau-deciles 3..8 compute
     T_m and the MNT prediction That_m with w_+ estimated by the
     frozen k = 8 nearest pos-node mass/span estimator; bar:
     median |T/That - 1| <= 0.25 on every heavy rung (bulk
     universality); the port region (decile 0) reported
     separately (Bessel edge regime, expected to deviate).

 M2  THE NYQUIST READING (report): per rung the bulk histogram
     of T/That and the port values -- where the criticality sits
     relative to the two-density law.

 C   CONTROLS (kz 9): the law itself is measure-UNIVERSAL
     (Epstein/scramble also satisfy MNT in their bulk -- typed
     universality, NOT a kill); must-fire: their testing MAXIMA
     exceed 1 (arithmetic in the VALUE, as always).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 controls silent
-> CONTROL-DEAD.  M1 may FAIL honestly (typed).

VERDICT (frozen enum): MNT-LAWFUL / MNT-IRREGULAR (+ both with
census) / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim: the law reduces the DIAGONAL half to classical
regularity; the coherent lift stays RH-hard (LXXXVIII).

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carleson_testing_law
(T = nu~ K identity) + case_sum_rule (KS class), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/testing_mnt_law_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

HEAVY = (9, 12, 13, 26, 40)
KNN = 8
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def rung_T(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = vs * Kdiag
    tau_m = (2.0 * math.pi * uf_n / L) / D
    dec = np.minimum((10 * tau_m / np.max(tau_m)).astype(int), 9)
    # MNT prediction with kNN density estimate of w_+ at y_m
    order = np.argsort(xs)
    xs_s, ws_s = xs[order], ws[order]
    That = np.zeros(len(ys))
    for m in range(len(ys)):
        i0 = np.searchsorted(xs_s, ys[m])
        lo = max(0, i0 - KNN // 2)
        hi = min(len(xs_s), lo + KNN)
        lo = max(0, hi - KNN)
        span = xs_s[hi - 1] - xs_s[lo]
        if span <= 0:
            That[m] = np.nan
            continue
        wloc = float(np.sum(ws_s[lo:hi])) / span
        That[m] = (h / math.pi) * vs[m] / (
            math.sqrt(max(1.0 - ys[m] ** 2, 1e-12)) * wloc)
    return dict(T=T, That=That, dec=dec, h=h)


def main():
    section("PRIME.SUMRULE.MNT.01 -- testing as a two-density MNT "
            "law (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("M1/M2 -- the law on the bulk (heavy rungs)")
    ok_law = True
    for kz in HEAVY:
        r = rung_T(kz)
        bulk = (r["dec"] >= 3) & (r["dec"] <= 8) \
            & np.isfinite(r["That"])
        ratio = r["T"][bulk] / r["That"][bulk]
        med = float(np.median(np.abs(ratio - 1.0)))
        ok_law &= (med <= 0.25)
        port = r["dec"] == 0
        print("    kz %-3d h %4d: bulk median |T/That - 1| = "
              "%.3f (n = %d); bulk ratio quartiles %.2f/%.2f/"
              "%.2f | port T/That: %s"
              % (kz, r["h"], med, int(np.sum(bulk)),
                 float(np.percentile(ratio, 25)),
                 float(np.percentile(ratio, 50)),
                 float(np.percentile(ratio, 75)),
                 " ".join("%.2f" % v for v in
                          (r["T"][port] / r["That"][port])[:5])))
    m1_type = "MNT-LAWFUL" if ok_law else "MNT-IRREGULAR"
    check("M1.1 typed: %s (bar: bulk median dev <= 0.25 on every "
          "heavy rung) -- if LAWFUL, the diagonal testing bound "
          "T <= 1 is the NYQUIST statement nu~ <= pi sqrt(1-y^2) "
          "w_+/h: classical MNT/Totik terrain, the sum-rule "
          "theorem's analytic seed" % m1_type, ok_law)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = rung_T(9, **kw)
        tmax = float(np.max(r["T"]))
        ok &= tmax > 1.0
        bulk = (r["dec"] >= 3) & (r["dec"] <= 8) \
            & np.isfinite(r["That"])
        med = float(np.median(np.abs(
            r["T"][bulk] / r["That"][bulk] - 1.0)))
        print("    %-8s: max T %.3e (fires) | bulk MNT dev %.3f "
              "(universality: the LAW is measure-blind, the "
              "VALUE is arithmetic)" % (nmc, tmax, med))
    check("C1 CONTROLS FIRE on the value (max T > 1)", ok,
          kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("CONTROL-DEAD" if KILLS else "MNT-MEASURED")
    print("\n  VERDICT: %s (%s)" % (VERDICT, m1_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
