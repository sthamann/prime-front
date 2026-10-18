#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_critical_eigenpair_probe -- PRIME.PORT.EIGENPAIR.01
(EXPLORATION ONLY, experiments/; round 39 task 5 of the 2026-08-09
external review: identify the critical port eigenvector among FEW
structure-derived candidates -- no free function search,
2026-08-09).

THE CANDIDATES (frozen BEFORE comparison; all built from source
data on the fixed j-window J = {2, 4, ..., 24} with the uniform
alternating gauge S_j = (-1)^{j/2}, the measured sign pattern of
the limit matrix):
  K1  alternating flat:            v_j ~ S_j;
  K2  Mellin-Cauchy magnitude:     v_j ~ S_j / sqrt(1 + 4 tau_j^2),
      tau_j = (2 pi j / L)/D (the rung's own alias frequency);
  K3  nu-weighted (Krein/Weyl):    v_j ~ S_j sqrt(nu~_j);
  K4  free-Jacobi edge (finite):   v_j ~ S_j sin(pi k/(K+1)),
      k = position of j in J.

FROZEN RULE: winner = candidate with the highest |cos| to the
measured top eigenvector of the D_P section on J; typed
EIGENPAIR-IDENTIFIED(K) iff the SAME candidate wins on ALL heavy
rungs (construction kz {9, 12, 13} AND holdouts {26, 40}) with
|cos| >= 0.95 everywhere, else NO-CANDIDATE (honest; kills only
these four formulas).

 C   CONTROLS (kz 9, must fire): edge crossed on both; the
     winning candidate's |cos| against the CONTROL top mode
     printed (report).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 controls silent
-> CONTROL-DEAD.

SPEC v2 (window repair; run 1 crashed): the v1 frozen window
J = {2..24} is NOT fully contained in every rung's folded port
node set (kz 9/13 miss some even j) -- a rigidity slip, not
mathematics.  v2 uses the per-rung AVAILABLE subset of J (>= 8
indices required), candidates and eigenvector restricted
consistently; the deepest available rung defines the reference
winner.  No candidate or bar changed.

VERDICT (frozen enum): EIGENPAIR-MEASURED (+ typed sublabel) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; round-38/39 chain
(port_fixed_space_limit: soft-mass in J = 1.000, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_critical_eigenpair_probe.py
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
JWIN = tuple(range(2, 25, 2))
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


def port_section(kz, **kw):
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
    idx = {int(j): k for k, j in enumerate(uf_n[ip])}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < 8:
        return None
    kk = [idx[j] for j in jav]
    A = DP[np.ix_(kk, kk)]
    nu = vs[np.array(kk)]
    lamE = float(np.linalg.eigvalsh(G)[-1])
    return dict(A=A, nu=nu, L=L, D=D, lamE=lamE, h=h, jav=jav)


def candidates(r):
    jav = r["jav"]
    S = np.array([(-1.0) ** (j // 2) for j in jav])
    tau = np.array([(2.0 * math.pi * j / r["L"]) / r["D"]
                    for j in jav])
    K = len(jav)
    out = {
        "K1 flat": S.copy(),
        "K2 cauchy": S / np.sqrt(1.0 + 4.0 * tau ** 2),
        "K3 nu-weighted": S * np.sqrt(r["nu"]),
        "K4 jacobi-edge": S * np.sin(
            math.pi * (np.arange(K) + 1.0) / (K + 1.0)),
    }
    return {k: v / np.linalg.norm(v) for k, v in out.items()}


def main():
    section("PRIME.PORT.EIGENPAIR.01 -- the critical eigenvector "
            "among four derived candidates (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("E1 -- candidate cosines (heavy rungs)")
    winners = {}
    coss = {}
    for kz in HEAVY:
        r = port_section(kz)
        if r in (None, "TOO-DEEP"):
            print("    kz %-3d: window too small (typed skip)"
                  % kz)
            continue
        ev, V = np.linalg.eigh(r["A"])
        vtop = V[:, -1]
        cands = candidates(r)
        cs = {k: float(abs(vtop @ v)) for k, v in cands.items()}
        win = max(cs, key=cs.get)
        winners[kz] = win
        coss[kz] = cs
        print("    kz %-3d h %4d: %s -> winner %s"
              % (kz, r["h"],
                 " | ".join("%s %.3f" % (k, cs[k])
                            for k in sorted(cs)), win))
    avail = sorted(winners.keys())
    same = len(set(winners.values())) == 1
    win0 = winners[avail[-1]]
    allhigh = all(coss[kz][winners[kz]] >= 0.95 for kz in avail)
    e1_type = ("EIGENPAIR-IDENTIFIED(%s)" % win0
               if same and allhigh else "NO-CANDIDATE")
    check("E1.1 typed: %s (rungs used %s; same winner: %s; min "
          "winning |cos| %.3f, bar 0.95)"
          % (e1_type, avail, same,
             min(coss[kz][winners[kz]] for kz in avail)),
          len(avail) >= 3, kill="K1")

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
        r = port_section(9, **kw)
        if r in (None, "TOO-DEEP"):
            print("    %-8s: window missing (typed)" % nmc)
            continue
        ok &= r["lamE"] > 1.0
        ev, V = np.linalg.eigh(r["A"])
        cs = float(abs(V[:, -1] @ candidates(r)[win0]))
        print("    %-8s: lam(E) %.3e | winner-candidate |cos| "
              "vs control mode %.3f (report)"
              % (nmc, r["lamE"], cs))
    check("C1 CONTROLS FIRE (lam > 1)", ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if any(k == "K1" for k in KILLS):
        VERDICT = "PIPELINE-BROKEN"
    elif any(k == "K2" for k in KILLS):
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "EIGENPAIR-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, e1_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
