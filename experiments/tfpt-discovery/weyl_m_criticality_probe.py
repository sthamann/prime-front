#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weyl_m_criticality_probe -- PRIME.DINFTY.WEYLM.01
(EXPLORATION ONLY, experiments/; round 38, executing the XC named
object (a): the BASIS-FREE criticality test of the port limit
operator via the Weyl-m boundary asymptotics at lambda -> 1+,
after the raw-chain Jordan test fired its falsifier, 2026-08-09).

WHY THIS COORDINATE: the e1-Lanczos chain of D_P is not slowly
varying (XC), so the pointwise transfer-matrix trichotomy is not
applicable there.  The basis-free object is the boundary behavior
of the Weyl function
    m_h(1 + s) = e1^T ((1+s) I - D_P(h))^{-1} e1
              = sum_i w_i / (s + g_i),
w_i = <e1, v_i>^2, g_i = 1 - lam_i > 0 (truth side), together
with the e1-SPECTRAL MEASURE at the edge, W_h(eps) = sum_{g_i <=
eps} w_i.  The criticality class of D_infty is read off the
h-stability of (i) the log-log slope sigma of m(1+s) on a frozen
s-window (spectral-measure exponent gamma = sigma + 1) and (ii)
the normalized edge-measure profile W_h(eps)/W_h(0.1).  HYPOTHESIS
FROZEN (informed by XC): the bare gap ratios drift, but the
WEIGHTED spectral measure may be the h-stable edge object -- if
so, this also answers XC object (b) at the measure level.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}, e1 = the first port node
= the pole-port seat; controls kz 9):

 W1  PIPELINE: D_P built as in round 38; m(1+s) and W(eps) via
     exact eigendecomposition; all g_i > 0 on truth rungs (the
     truth spectrum stays below 1 -- re-ward).

 W2  THE EXPONENT: slope sigma_h of log m(1+s) vs log s on the
     frozen geometric grid s in [10 tau_h, 0.1] (12 points, per
     rung its own tau); typed EXPONENT-STABLE iff the three
     deepest rungs (kz 13, 26, 40) agree within |Delta sigma| <=
     0.15, else EXPONENT-DRIFTING; the class reading printed:
     gamma = sigma + 1 (gamma < 1 = divergent-m hard edge; sigma
     = -1 = atom-dominated edge).

 W3  THE EDGE-MEASURE COLLAPSE: F_h(t) := W_h(t * 0.1)/W_h(0.1)
     on the frozen grid t in {0.001, 0.003, 0.01, 0.03, 0.1,
     0.3, 1}; typed EDGE-MEASURE-STABLE iff the pairwise sup-
     distance of F_h over the three deepest rungs is <= 0.15,
     else EDGE-MEASURE-DRIFTING.  (If STABLE while the bare gap
     ratios drift (XC X1), the h-stable edge object is the
     WEIGHTED measure -- the answer to the scaling question at
     the measure level.)

 W4  WEIGHT ANATOMY (report): w_1 (top-mode weight at e1), the
     cumulative share W(10 tau)/W(0.1), and the participation
     ratio of the weights -- where the e1 mass sits spectrally.

 C   CONTROLS (kz 9, must fire): Epstein and scramble have
     eigenvalues ABOVE 1 (min gap < 0) -- the truth-side Herglotz
     window does not exist for them.

SPEC v2 (control-criterion repair; run 1 = 4/5): the v1 must-fire
demanded sign changes of m(1+s) on the s-window, but the control
poles sit at gap -5.9 (Epstein) and -7.4e5 (scramble) -- far
BELOW the window [1e-4, 0.1], so no crossing can occur there by
construction; the correct and sufficient must-fire is min gap < 0
on both (the edge is crossed), which run 1 measured.  No other
change; the truth-side wards (positive monotone m) unchanged.

KILLS: K1 pipeline breaks / negative truth gaps ->
PIPELINE-BROKEN; K2 truth m not positive-monotone -> M-BROKEN;
K3 a control does not fire -> CONTROL-DEAD.  W2/W3 are typed
dichotomies (all outcomes honest).

VERDICT (frozen enum): WEYLM-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / M-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime-table oracles (AST
scan); v563 READ-ONLY; RNG only inside the declared scramble
control; writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38 chain (XC
Jordan-test outcome as declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/weyl_m_criticality_probe.py
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
DEEP3 = (13, 26, 40)
TGRID = (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0)
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


def dressed_port(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    ev, V = np.linalg.eigh(DP)
    w1 = V[0, :] ** 2                       # e1 weights
    return dict(ev=ev[::-1], w=w1[::-1], h=b["h"],
                m=DP.shape[0])


def m_of(r, s):
    g = 1.0 - r["ev"]
    return float(np.sum(r["w"] / (s + g)))


def main():
    section("PRIME.DINFTY.WEYLM.01 -- the basis-free Weyl-m "
            "criticality test (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("W1/W2/W4 -- the exponent and the weights")
    res = {}
    ok_gap = ok_mono = True
    for kz in HEAVY:
        r = dressed_port(kz)
        res[kz] = r
        g = 1.0 - r["ev"]
        tau = float(g[0])
        ok_gap &= bool(np.all(g > 0))
        ss = np.geomspace(10.0 * tau, 0.1, 12)
        mv = np.array([m_of(r, s) for s in ss])
        ok_mono &= bool(np.all(mv > 0)
                        and np.all(np.diff(mv) < 0))
        sig = float(np.polyfit(np.log(ss), np.log(mv), 1)[0])
        r["sigma"] = sig
        W01 = float(np.sum(r["w"][g <= 0.1]))
        share = float(np.sum(r["w"][g <= 10 * tau])) / W01
        pr = float((np.sum(r["w"]) ** 2)
                   / np.sum(r["w"] ** 2)) / r["m"]
        print("    kz %-3d h %4d m %3d tau %.2e: sigma %+0.3f "
              "(gamma %+0.3f) | w_1 %.3f | W(10tau)/W(0.1) %.3f "
              "| participation %.2f"
              % (kz, r["h"], r["m"], tau, sig, sig + 1.0,
                 float(r["w"][0]), share, pr))
    check("W1.1 truth spectra below 1 (all gaps > 0) and m(1+s) "
          "positive + strictly decreasing on every rung",
          ok_gap and ok_mono,
          kill="K1" if not ok_gap else ("K2" if not ok_mono
                                        else None))
    sig3 = [res[kz]["sigma"] for kz in DEEP3]
    dsig = max(sig3) - min(sig3)
    w2_type = ("EXPONENT-STABLE" if dsig <= 0.15
               else "EXPONENT-DRIFTING")
    check("W2.1 typed: %s (sigma over kz %s = %s, spread %.3f, "
          "bar 0.15); class reading gamma = sigma + 1 = %s"
          % (w2_type, DEEP3,
             ["%+.3f" % s for s in sig3], dsig,
             ["%+.3f" % (s + 1) for s in sig3]), True)

    section("W3 -- the edge-measure collapse")
    curves = {}
    for kz in HEAVY:
        r = res[kz]
        g = 1.0 - r["ev"]
        W01 = float(np.sum(r["w"][g <= 0.1]))
        curves[kz] = np.array([float(np.sum(
            r["w"][g <= t * 0.1])) / W01 for t in TGRID])
        print("    kz %-3d F(t): %s"
              % (kz, " ".join("%.3f" % v for v in curves[kz])))
    dev = 0.0
    for a_ in range(len(DEEP3)):
        for b_ in range(a_ + 1, len(DEEP3)):
            dev = max(dev, float(np.max(np.abs(
                curves[DEEP3[a_]] - curves[DEEP3[b_]]))))
    w3_type = ("EDGE-MEASURE-STABLE" if dev <= 0.15
               else "EDGE-MEASURE-DRIFTING")
    check("W3.1 typed: %s (pairwise sup-distance over kz %s: "
          "%.3f, bar 0.15)%s"
          % (w3_type, DEEP3, dev,
             " -- the WEIGHTED edge measure is the h-stable "
             "object even though bare gap ratios drift (XC X1): "
             "the scaling answer at the measure level"
             if dev <= 0.15 else ""), True)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = dressed_port(9, **kw)
        g = 1.0 - r["ev"]
        fired = bool(np.any(g < 0))
        ok_ctl &= fired
        print("    %-8s: min gap %+0.3e -> edge crossed: %s"
              % (nmc, float(np.min(g)), fired))
    check("C1 CONTROLS FIRE (SPEC v2): both have spectrum above "
          "1 (min gap < 0) -- no truth-side Herglotz window "
          "exists for them", ok_ctl, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN", "K2": "M-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "WEYLM-MEASURED"
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, w2_type,
                                         w3_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
