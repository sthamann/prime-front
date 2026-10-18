#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gap_scaling_variable_probe -- PRIME.PORT.GAPSCALE.01
(EXPLORATION ONLY, experiments/; round 38, executing the XC named
object (b): find the scaling variable of the edge gaps of the
dressed port family, informed by the Weyl-m finding that the edge
measure CONDENSES onto a single atom (gamma -> 0, w_1 -> 0.72) --
so the top gap g_1 = tau separates from the rest and the sub-
leading gaps need their own scale, 2026-08-09).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}, deep triple {13, 26,
40}; controls kz 9):

 G1  CANDIDATE TABLE: for the sub-leading gaps g_3..g_8 (i = 1,2
     excluded uniformly: g_1 is the separating atom, g_2 the
     first rest-gap used by one candidate), normalize by each
     FROZEN candidate scale:
       (v1) tau = g_1            (the atom gap -- XC showed drift),
       (v2) g_2                  (rest-spectrum self-scale),
       (v3) 1 - T_h              (testing margin),
       (v4) 1 - lam_max(R)       (bulk margin),
       (v5) 1/m^2                (port-size Weyl scale),
       (v6) mean(g_2..g_6)       (rest-mean).
     Metric: pairwise max relative deviation of the normalized
     vectors over the deep triple; the full table printed.

 G2  THE WINNER: typed SCALE-FOUND(v_k) iff the best candidate
     reaches dev <= 0.20, else NO-SCALE (honest either way; the
     XC X1 failure used v1 on i <= 5 -- if v2/v6 win, the drift
     was pure atom-separation).

 G3  RETRACK (report-only, diagnostic zero cache as in XC): with
     the winning scale, compare the normalized rest-gaps against
     (gamma_i/gamma_1)^p, p in {1, 2} (report; no bar -- the
     naive mapping already died in XC, this records whether the
     right scale revives anything).

 C   CONTROLS (kz 9, must fire): Epstein/scramble: edge crossed
     (min gap < 0) -- no truth-side gap ladder exists.

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 a control does
not fire -> CONTROL-DEAD.  G2 is a typed dichotomy.

VERDICT (frozen enum): GAPSCALE-MEASURED (+ typed sublabel) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: construction zero-free (AST scan); the
zero cache enters ONLY the G3 report (declared diagnostic, XC
precedent); v563 READ-ONLY; RNG only in the declared scramble
control; writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38 chain
(port_schur / weyl_m probes as declared inputs);
zero_comb_cache_n2000.json (diagnostic target only).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gap_scaling_variable_probe.py
"""

import ast
import hashlib
import json
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


def rung_data(kz, **kw):
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
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = float(np.max(vs * Kdiag))
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    lamR = float(np.linalg.eigvalsh(R)[-1])
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    ev = np.linalg.eigvalsh(DP)[::-1]
    g = 1.0 - ev
    return dict(g=g, m=DP.shape[0], h=h, T=T, lamR=lamR)


def main():
    section("PRIME.PORT.GAPSCALE.01 -- the scaling variable of "
            "the sub-leading edge gaps (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; zero cache DIAGNOSTIC-ONLY (G3).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (construction zero-free)",
          not ast_scan(BANNED_IDS))

    section("G1 -- candidate table (gaps g_3..g_8, deep triple)")
    res = {}
    for kz in HEAVY:
        r = rung_data(kz)
        res[kz] = r
        print("    kz %-3d h %4d m %3d: g_1..g_8 = %s"
              % (kz, r["h"], r["m"],
                 " ".join("%.2e" % v for v in r["g"][:8])))

    def scale_of(r, name):
        g = r["g"]
        if name == "v1 tau":
            return float(g[0])
        if name == "v2 g2":
            return float(g[1])
        if name == "v3 1-T":
            return 1.0 - r["T"]
        if name == "v4 bulk":
            return 1.0 - r["lamR"]
        if name == "v5 1/m^2":
            return 1.0 / r["m"] ** 2
        return float(np.mean(g[1:6]))          # v6 rest-mean

    cands = ("v1 tau", "v2 g2", "v3 1-T", "v4 bulk", "v5 1/m^2",
             "v6 mean")
    table = {}
    for name in cands:
        vecs = {}
        for kz in DEEP3:
            r = res[kz]
            vecs[kz] = r["g"][2:8] / scale_of(r, name)
        dev = 0.0
        for a_ in range(len(DEEP3)):
            for b_ in range(a_ + 1, len(DEEP3)):
                va, vb = vecs[DEEP3[a_]], vecs[DEEP3[b_]]
                k = min(len(va), len(vb))
                dev = max(dev, float(np.max(
                    np.abs(va[:k] - vb[:k])
                    / np.maximum(np.abs(vb[:k]), 1e-30))))
        table[name] = dev
        print("    %-9s: pairwise max rel dev %.3f  (norm. gaps "
              "kz40: %s)"
              % (name, dev,
                 " ".join("%.2f" % v
                          for v in vecs[40][:6])))
    winner = min(table, key=table.get)
    g2_type = ("SCALE-FOUND(%s)" % winner
               if table[winner] <= 0.20 else "NO-SCALE")
    check("G2.1 typed: %s (best dev %.3f, bar 0.20; full table "
          "printed)" % (g2_type, table[winner]), True)

    section("G3 -- retrack with the winner (report-only)")
    cache = json.load(open(os.path.join(
        _HERE, "zero_comb_cache_n2000.json")))
    gam = np.array([float(x) for x in cache["gammas"][:10]])
    r40 = res[40]
    vn = r40["g"][2:8] / scale_of(r40, winner)
    for p in (1, 2):
        rr_ = (gam[2:8] / gam[2]) ** p * vn[0]
        md = float(np.max(np.abs(vn - rr_)
                          / np.maximum(rr_, 1e-30)))
        print("    p = %d: scaled rest-gaps %s vs gamma-law %s "
              "-> max rel dev %.2f"
              % (p, " ".join("%.2f" % v for v in vn),
                 " ".join("%.2f" % v for v in rr_), md))
    check("G3.1 retrack recorded (report-only; no bar)", True)

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
        r = rung_data(9, **kw)
        fired = bool(np.any(r["g"] < 0))
        ok_ctl &= fired
        print("    %-8s: min gap %+0.3e -> edge crossed: %s"
              % (nmc, float(np.min(r["g"])), fired))
    check("C1 CONTROLS FIRE: edge crossed on both", ok_ctl,
          kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "GAPSCALE-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, g2_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
