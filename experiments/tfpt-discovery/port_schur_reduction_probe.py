#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_schur_reduction_probe -- PRIME.PORT.SCHUR.01
(EXPLORATION ONLY, experiments/; round 38 continuation, executing
the LXXXV named object (b): the port-local certificate class made
EXACT via Schur complement / Haynsworth inertia, 2026-08-09).

THE EXACT REDUCTION (classical, frozen before the run): split the
Carleson embedding E (PSD, lam_max = 1 - tau) along the predeclared
PORT set (nodes with tau_m <= tau_max/10, the seat of the worst
testing quotient and of 100 percent of the soft-mode mass):
    E = [[P, X], [X^T, R]]   (port block first).
Then with the DRESSED PORT  D_P := P + X (I - R)^{-1} X^T:
    I - E >= 0   <=>   I - R >= 0  AND  I - D_P >= 0,
and Haynsworth: In(I - E) = In(I - R) + In(I - D_P) EXACTLY.  This
is a NON-decompositional reduction (one Schur complement, no cell
bookkeeping, no absolute values): the cofinal wall demand becomes
(i) a BULK margin 1 - lam_max(R) and (ii) a SMALL dressed-port
matrix inequality lam_max(D_P) <= 1.

THE MARGIN LEDGER (the honest question after the testing probe):
the testing margin 1 - T_h ~ h^{-0.70} is large vs tau ~ e^{-2.4a};
the off-diagonal lift consumes almost all of it.  WHERE does the
margin die -- in the bulk R (then the port block is not the wall),
or in the dressed port D_P (then the wall IS a small prime-comb
matrix family)?  Per rung print: 1 - T_h, 1 - lam_max(P),
1 - lam_max(R), 1 - lam_max(D_P), tau.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
rungs kz {9, 12, 13} + holdouts {26, 40}; controls kz 9 Epstein +
scramble seed 1):

 T1  EXACTNESS: Haynsworth inertia identity holds with INTEGER
     match on all rungs AND both controls (negative-eigenvalue
     counts of I-E vs I-R plus I-D_P); on truth rungs all three
     are PSD; lam_max(D_P) <= lam_max(E) + 1e-8.

 T2  THE SEAT: 1 - lam_max(D_P) vs tau (ratio printed); typed
     PORT-IS-THE-WALL iff (1 - lam_max(D_P))/tau <= 3 on all truth
     rungs (the dressed port carries the entire criticality) AND
     the bulk margin 1 - lam_max(R) exceeds 100 x tau everywhere;
     else typed BULK-SHARES-THE-WALL.

 T3  BULK MARGIN LAW: 1 - lam_max(R) values + log-log slope vs h
     (is the bulk h-uniformly safe? report; typed BULK-SAFE iff
     min >= 1e-3), and the port size fraction s_h = |port|/n.

 T4  DRESSING WEIGHT: ||X (I-R)^{-1} X^T||_2 vs 1 - lam_max(P):
     the fraction of the raw port margin consumed by bulk feedback
     (printed; the measure of non-locality that remains).

 T5  PORT-FAMILY CONVERGENCE: the dressed-port top eigenvector at
     matched grid indices j (the folded port nodes j = 2, 3, ...):
     pairwise cosine similarity across all five rungs; typed
     PORT-LIMIT-STABLE iff all pairwise cos >= 0.98 (the h -> inf
     limit object exists in the j-coordinate), else DRIFTING.

 C   CONTROLS (must fire): overall lam_max(E) > 1 on both; the
     inertia ledger localizes the failure (how many negative
     directions sit in I - D_P vs I - R) -- printed.

KILLS: K1 chain/pipeline breaks -> PIPELINE-BROKEN; K2 Haynsworth
integer identity breaks -> SCHUR-BROKEN; K3 a control does not
fire -> CONTROL-DEAD.

VERDICT (frozen enum): PORT-SCHUR-EXACT (+ typed sublabels from
T2/T3/T5) / PIPELINE-BROKEN / SCHUR-BROKEN / CONTROL-DEAD.

NO RH claim: the reduction relocates the wall into (R, D_P); the
positivity of the dressed port family remains the open arithmetic
statement.

FIREWALL: no zeros, no prime-table oracles (AST scan); v563
READ-ONLY; RNG only inside the declared scramble control; writes
nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; the round-38 chain
(cd_pick_scalarization / omega_source_law / loewner_interlace /
carleson_testing_law probes, declared inputs); v866 (heavy set).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_schur_reduction_probe.py
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

RUNGS = (9, 12, 13, 26, 40)
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
    c = c_ar + c_at
    d = grid_density(c)
    L = 2 * M - 2
    return dict(d=d, L=L, D=D, alpha=alpha, h=h)


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


def neg_count(A, tol=0.0):
    return int(np.sum(np.linalg.eigvalsh(0.5 * (A + A.T)) < tol))


def anatomy(kz, tag, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h + 1)
    # plain Carleson Gram (gauge-equivalent to E, round-38 v2)
    KCD = Pn[:, :h] @ Pn[:, :h].T
    G = np.sqrt(vs)[:, None] * KCD * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip = np.where(port)[0]
    ib = np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    lamE = float(np.linalg.eigvalsh(G)[-1])
    lamP = float(np.linalg.eigvalsh(P)[-1])
    lamR = float(np.linalg.eigvalsh(R)[-1])
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    evD, VD = np.linalg.eigh(DP)
    lamD = float(evD[-1])
    dress = float(np.linalg.norm(
        X @ np.linalg.solve(IR, X.T), 2))
    # Haynsworth integer ledger
    nE = neg_count(np.eye(n) - G)
    nR = neg_count(IR)
    nD = neg_count(np.eye(len(ip)) - DP)
    T_test = float(np.max(np.diag(G)))
    tau = 1.0 - lamE
    print("    %-20s h %4d  n %4d  |port| %3d (%.3f)"
          % (tag, h, n, len(ip), len(ip) / n))
    print("      margin ledger: 1-T %.3e | 1-lamP %.3e | 1-lamR "
          "%.3e | 1-lamD %.3e | tau %.3e"
          % (1.0 - T_test, 1.0 - lamP, 1.0 - lamR, 1.0 - lamD,
             tau))
    print("      Haynsworth: neg(I-E) %d == neg(I-R) %d + "
          "neg(I-D_P) %d | dressing ||X(I-R)^-1X^T|| %.3e vs raw "
          "port margin %.3e"
          % (nE, nR, nD, dress, 1.0 - lamP))
    # top eigenvector of D_P at matched j indices
    vtop = VD[:, -1]
    vtop = vtop * np.sign(vtop[np.argmax(np.abs(vtop))])
    jj_port = uf_n[ip]
    return dict(h=h, n=n, np_=len(ip), lamE=lamE, lamP=lamP,
                lamR=lamR, lamD=lamD, dress=dress, nE=nE, nR=nR,
                nD=nD, T=T_test, tau=tau, vtop=vtop,
                jj_port=jj_port)


def main():
    section("PRIME.PORT.SCHUR.01 -- the exact port reduction + "
            "margin ledger (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("T1-T5 -- rungs %s (26/40 = holdouts)" % (RUNGS,))
    res = {}
    for kz in RUNGS:
        res[kz] = anatomy(kz, "kz %d%s"
                          % (kz, " (HOLDOUT)"
                             if kz in (26, 40) else ""))
    ok_all = all(r is not None for r in res.values())
    check("T0 all chains complete", ok_all, kill="K1")

    if ok_all:
        hay_ok = all(r["nE"] == r["nR"] + r["nD"]
                     for r in res.values())
        psd_ok = all(r["nE"] == 0 and r["nR"] == 0 and r["nD"] == 0
                     for r in res.values())
        dp_ok = all(r["lamD"] <= r["lamE"] + 1e-8
                    for r in res.values())
        check("T1 EXACTNESS: Haynsworth integer identity on all "
              "rungs (%s); truth all-PSD (%s); lam(D_P) <= lam(E)"
              % (hay_ok, psd_ok), hay_ok and psd_ok and dp_ok,
              kill="K2")
        ratios = [(1.0 - r["lamD"]) / r["tau"]
                  for r in res.values()]
        bulk_over_tau = [(1.0 - r["lamR"]) / r["tau"]
                         for r in res.values()]
        seat = ("PORT-IS-THE-WALL"
                if max(ratios) <= 3.0
                and min(bulk_over_tau) >= 100.0
                else "BULK-SHARES-THE-WALL")
        check("T2 THE SEAT: (1 - lam(D_P))/tau in [%.2f, %.2f]; "
              "bulk margin / tau >= %.1e -> %s"
              % (min(ratios), max(ratios), min(bulk_over_tau),
                 seat), True)
        bulk_m = [1.0 - r["lamR"] for r in res.values()]
        hh = np.array([r["h"] for r in res.values()], float)
        sl_bulk = float(np.polyfit(np.log(hh),
                                   np.log(bulk_m), 1)[0])
        bulk_type = ("BULK-SAFE" if min(bulk_m) >= 1e-3
                     else "BULK-THIN")
        check("T3 BULK MARGIN: 1 - lam(R) in [%.3e, %.3e], "
              "log-log slope vs h %+.3f -> %s; port fraction %s"
              % (min(bulk_m), max(bulk_m), sl_bulk, bulk_type,
                 ["%.3f" % (r["np_"] / r["n"])
                  for r in res.values()]), True)
        eaten = [r["dress"] / max(1.0 - r["lamP"], 1e-300)
                 for r in res.values()]
        check("T4 DRESSING WEIGHT: bulk feedback consumes "
              "fraction %s of the raw port margin (printed)"
              % ["%.3f" % e for e in eaten], True)
        # T5 convergence at matched j
        jset = None
        for r in res.values():
            s = set(int(j) for j in r["jj_port"])
            jset = s if jset is None else (jset & s)
        jlist = sorted(jset)[:10]
        vecs = []
        for r in res.values():
            idx = {int(j): k for k, j in enumerate(r["jj_port"])}
            v = np.array([r["vtop"][idx[j]] for j in jlist])
            vecs.append(v / np.linalg.norm(v))
        cosmin = 1.0
        for a in range(len(vecs)):
            for b2 in range(a + 1, len(vecs)):
                cosmin = min(cosmin,
                             float(abs(vecs[a] @ vecs[b2])))
        conv = ("PORT-LIMIT-STABLE" if cosmin >= 0.98
                else "DRIFTING")
        check("T5 PORT-FAMILY CONVERGENCE: top eigenvector of "
              "D_P at matched j %s: min pairwise cos %.4f -> %s"
              % (jlist, cosmin, conv), True)
    else:
        seat = bulk_type = conv = "N/A"

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = anatomy(9, "Epstein (control)",
                             comb=(np.log(nn.astype(float)),
                                   2.0 * lamE_[nn]
                                   / np.sqrt(nn.astype(float))))
    ctl["scramble"] = anatomy(9, "scramble (control)",
                              scramble_seed=1)
    ctl_ok = all(c is not None for c in ctl.values())
    fired = ctl_ok and all(c["lamE"] > 1.0 for c in ctl.values())
    hay_c = ctl_ok and all(c["nE"] == c["nR"] + c["nD"]
                           for c in ctl.values())
    check("C1 CONTROLS FIRE (lam(E) > 1 on both) and the "
          "Haynsworth ledger localizes the failure "
          "(Epstein: %s neg in D_P / %s in R; scramble: %s / %s)"
          % ((ctl["Epstein"]["nD"], ctl["Epstein"]["nR"],
              ctl["scramble"]["nD"], ctl["scramble"]["nR"])
             if ctl_ok else ("-",) * 4),
          fired and hay_c, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if not fired:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "SCHUR-BROKEN"}.get(KILLS[0],
                                             "CONTROL-DEAD")
    else:
        VERDICT = "PORT-SCHUR-EXACT"
    print("\n  VERDICT: %s (%s + %s + %s)"
          % (VERDICT, seat, bulk_type, conv))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
