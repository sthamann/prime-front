#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_fixed_space_limit_probe -- PRIME.PORT.FIXEDSPACE.01
(EXPLORATION ONLY, experiments/; round 39 task 4 of the 2026-08-09
external review: operator convergence in a FIXED space -- entrywise
tables shall no longer carry the limit statement, 2026-08-09).

THE FIXED FRAME (frozen; measured justification): the stable label
across rungs is the alias index j of the folded port nodes
(LXXXVII T5: eigenvector cos >= 0.985 at matched j; the review's
r-coordinate is the SOURCE frame -- for the operator the j-lattice
is the measured stable frame).  Embed U_h: port -> l2(N) by
j-matching and take the FIXED window J = {2, 4, ..., 24} (12
indices, inside every heavy-rung port).

FROZEN PROTOCOL (2026-08-09; ladder h <= 900 for trends, heavy
rungs kz {9, 12, 13, 26, 40} printed; controls kz 9):

 F1  SECTION CONVERGENCE (the limit statement in norm): A_h =
     section of D_P(h) on J; against the deepest ladder rung:
     both ||A_h - A_deep||_2 (operator) and ||.||_F (HS)
     DECREASING with h (log-log slope <= -0.2 on h <= h_deep/2);
     typed NORM-CONVERGENT / NORM-DRIFTING.

 F2  TAIL CONTROL (does the fixed window carry the physics?):
     |lam_max(A_h) - lam_max(D_P(h))| per rung; typed
     TAIL-CARRIES iff the difference exceeds tau_h by more than
     100x on some rung (the criticality does NOT live in the
     fixed window alone -- honest), else WINDOW-CARRIES; both
     printed with the eigenvector mass inside J.

 C   CONTROLS (kz 9, must fire): edge crossed on both.

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 controls silent
-> CONTROL-DEAD.  F1/F2 typed.

VERDICT (frozen enum): FIXEDSPACE-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; round-38/39 chain
(port_schur_reduction / port_limit_operator, declared inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_fixed_space_limit_probe.py
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
    return dict(DP=DP, jj=uf_n[ip], h=h,
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def sect(r, jwin):
    idx = {int(j): k for k, j in enumerate(r["jj"])}
    if any(j not in idx for j in jwin):
        return None
    kk = [idx[j] for j in jwin]
    return r["DP"][np.ix_(kk, kk)]


def main():
    section("PRIME.PORT.FIXEDSPACE.01 -- operator convergence in "
            "the fixed j-window (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("F1/F2 -- section norms + tail control")
    rows = []
    for kz in core.frame_a_zones():
        r = dressed_port(kz)
        if r in (None, "TOO-DEEP"):
            continue
        A = sect(r, JWIN)
        if A is None:
            continue
        evD = np.linalg.eigvalsh(r["DP"])
        evA = np.linalg.eigvalsh(A)
        vfull = np.linalg.eigh(r["DP"])[1][:, -1]
        idx = {int(j): k for k, j in enumerate(r["jj"])}
        mass_in = float(np.sum(vfull[[idx[j] for j in JWIN]] ** 2))
        rows.append(dict(h=r["h"], kz=kz, A=A,
                         lamD=float(evD[-1]),
                         lamA=float(evA[-1]),
                         tau=1.0 - float(evD[-1]),
                         mass=mass_in))
    rows.sort(key=lambda x: x["h"])
    deep = rows[-1]
    for x in rows:
        if x["kz"] in HEAVY:
            print("    kz %-3d h %4d: lam(D_P) %.8f | lam(A_J) "
                  "%.8f | diff %.1e (tau %.1e) | soft-mass in J "
                  "%.3f"
                  % (x["kz"], x["h"], x["lamD"], x["lamA"],
                     abs(x["lamD"] - x["lamA"]), x["tau"],
                     x["mass"]))
    hh, d2, dF = [], [], []
    for x in rows[:-1]:
        hh.append(x["h"])
        d2.append(float(np.linalg.norm(x["A"] - deep["A"], 2)))
        dF.append(float(np.linalg.norm(x["A"] - deep["A"])))
    hh = np.array(hh, float)
    d2 = np.array(d2)
    dF = np.array(dF)
    mask = hh <= deep["h"] / 2.0
    sl2 = float(np.polyfit(np.log(hh[mask]), np.log(d2[mask]),
                           1)[0])
    slF = float(np.polyfit(np.log(hh[mask]), np.log(dF[mask]),
                           1)[0])
    f1_type = ("NORM-CONVERGENT" if sl2 <= -0.2 and slF <= -0.2
               else "NORM-DRIFTING")
    check("F1.1 typed: %s -- ||A_h - A_deep||: op %.4f -> %.4f "
          "(slope %+.3f), HS %.4f -> %.4f (slope %+.3f); bars "
          "<= -0.2"
          % (f1_type, d2[0], d2[-1], sl2, dF[0], dF[-1], slF),
          sl2 <= -0.2 and slF <= -0.2)
    worst_ratio = max(abs(x["lamD"] - x["lamA"]) / x["tau"]
                      for x in rows)
    f2_type = ("TAIL-CARRIES" if worst_ratio > 100.0
               else "WINDOW-CARRIES")
    check("F2.1 typed: %s -- max |lam(D_P) - lam(A_J)|/tau = "
          "%.1f; soft-mass in J: %.3f..%.3f"
          % (f2_type, worst_ratio,
             min(x["mass"] for x in rows),
             max(x["mass"] for x in rows)), True)

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
        r = dressed_port(9, **kw)
        ok &= r["lamE"] > 1.0
        print("    %-8s: lam(E) %.3e" % (nmc, r["lamE"]))
    check("C1 CONTROLS FIRE", ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("CONTROL-DEAD" if any(k == "K2" for k in KILLS)
               else "FIXEDSPACE-MEASURED")
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, f1_type,
                                         f2_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
