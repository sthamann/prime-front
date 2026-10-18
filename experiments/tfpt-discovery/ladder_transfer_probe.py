#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ladder_transfer_probe -- PRIME.PORT.LADDER.TRANSFER.01
(EXPLORATION ONLY, experiments/; round 40, work package 1 of the
parallel closing push: is the LADDER STEP perturbative -- the
forced direction after FLUCTUATIONS-REQUIRED killed comb-space
perturbation theory, 2026-08-09).

THE QUESTION: comb deformations cannot be the small parameter
(lattice_parametrix_probe: the Euler-product pairing is load-
bearing).  The remaining perturbative direction is ALONG THE
LADDER: the compressed fixed-window family C_J(h) converges fast
(slope -2.80, XCIV), so consecutive rungs are CLOSE.  If the
one-step update is (a) first-order accurate on the top eigenpair
and (b) sign/size-structured, an INDUCTION shape opens: wall
positivity propagates rung to rung -- a proof form that never
needs a uniform margin, only step stability.

FROZEN PROTOCOL (2026-08-09; ALL ladder rungs h <= 900 sorted by
h; the compressed fixed-window objects C_J on the common j-window
J = {2,...,24} subset per pair; consecutive pairs (k, k+1)):

 L1  FIRST-ORDER TRANSFER: with v_k the top eigenvector of
     C_J(h_k) and Delta_k = C_J(h_{k+1}) - C_J(h_k) on the common
     j-subset: predict lam_{k+1} ~ lam_k + <v_k, Delta_k v_k>;
     measure the accuracy ratio acc_k = |predicted - actual| /
     |actual move|; typed LADDER-PERTURBATIVE iff median acc <=
     0.5 (the step is first-order tractable), else LADDER-ROUGH.

 L2  STEP ANATOMY (report): per step the increment norm
     ||Delta_k||_2, the perturbative ratio ||Delta_k||/gap_k
     (gap = lam_1 - lam_2 of rung k), and the inertia of Delta_k
     (positive/negative eigenvalue counts -- is the step
     sign-structured?).

 L3  MONOTONICITY: is lam_max(C_J) increasing at (almost) every
     step (the approach-from-below in step form)?  Typed
     MONOTONE iff >= 90 percent of steps increase lam, else
     NON-MONOTONE (both honest; monotone would be the induction
     invariant candidate).

 C   CONTROLS (kz 9, must fire): Epstein/scramble lam(E) > 1
     (value; the transfer structure is not probed there --
     different criticality side).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 controls silent
-> CONTROL-DEAD.  L1/L3 typed dichotomies.

SPEC v2 (control-scope repair; run 1 = 4/5): the v1 control used
the compressed-window object, but the SCRAMBLE comb's folded port
does not contain the fixed J-window (different sign pattern of
d), so the constructor returned None although lam(E) > 1 is
long-established for it -- a mechanical scope slip.  v2 fires the
control on lam(E) of the plain Carleson Gram (no window
requirement); the window unavailability is typed in the print.
No other change.

VERDICT (frozen enum): LADDER-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; port_cocycle_window
probe (XCIV, the compression machinery), lattice_parametrix
probe (XCVI, the forcing result).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ladder_transfer_probe.py
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


def compressed_window(kz, **kw):
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
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < 8:
        return dict(CJ=None, jav=jav, h=h,
                    lamE=float(np.linalg.eigvalsh(E)[-1]))
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    IO = np.eye(len(io)) - E[np.ix_(io, io)]
    CJ = E[np.ix_(iw, iw)] + E[np.ix_(iw, io)] @ np.linalg.solve(
        IO, E[np.ix_(io, iw)])
    CJ = 0.5 * (CJ + CJ.T)
    return dict(CJ=CJ, jav=jav, h=h,
                lamE=float(np.linalg.eigvalsh(E)[-1]))


def main():
    section("PRIME.PORT.LADDER.TRANSFER.01 -- is the ladder step "
            "perturbative? (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("L1/L2/L3 -- the one-step transfer along the ladder")
    rows = []
    for kz in core.frame_a_zones():
        r = compressed_window(kz)
        if r in (None, "TOO-DEEP") or r["CJ"] is None:
            continue
        rows.append(r)
    rows.sort(key=lambda r: r["h"])
    accs, ratios, mono = [], [], []
    pos_counts, neg_counts = [], []
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        common = [j for j in a["jav"] if j in b["jav"]]
        if len(common) < 8:
            continue
        ia = [a["jav"].index(j) for j in common]
        ib = [b["jav"].index(j) for j in common]
        A = a["CJ"][np.ix_(ia, ia)]
        B = b["CJ"][np.ix_(ib, ib)]
        evA, VA = np.linalg.eigh(A)
        evB = np.linalg.eigvalsh(B)
        v = VA[:, -1]
        Dlt = B - A
        move = float(evB[-1] - evA[-1])
        pred = float(v @ Dlt @ v)
        acc = abs(pred - move) / max(abs(move), 1e-30)
        accs.append(acc)
        gap = float(evA[-1] - evA[-2])
        nrm = float(np.linalg.norm(Dlt, 2))
        ratios.append(nrm / max(gap, 1e-30))
        evD = np.linalg.eigvalsh(Dlt)
        pos_counts.append(int(np.sum(evD > 1e-12)))
        neg_counts.append(int(np.sum(evD < -1e-12)))
        mono.append(move > 0)
    accs = np.array(accs)
    ratios = np.array(ratios)
    med_acc = float(np.median(accs))
    l1_type = ("LADDER-PERTURBATIVE" if med_acc <= 0.5
               else "LADDER-ROUGH")
    check("L1.1 typed: %s -- first-order transfer accuracy over "
          "%d steps: median %.3f, quartiles %.3f/%.3f (bar 0.5)"
          % (l1_type, len(accs), med_acc,
             float(np.percentile(accs, 25)),
             float(np.percentile(accs, 75))), True)
    check("L2.1 STEP ANATOMY (report): ||Delta||/gap quartiles "
          "%.1f/%.1f/%.1f; increment inertia (pos, neg) medians "
          "(%d, %d) of 12 -- sign-structure census"
          % (float(np.percentile(ratios, 25)),
             float(np.percentile(ratios, 50)),
             float(np.percentile(ratios, 75)),
             int(np.median(pos_counts)),
             int(np.median(neg_counts))), True)
    frac_mono = float(np.mean(mono))
    l3_type = "MONOTONE" if frac_mono >= 0.9 else "NON-MONOTONE"
    check("L3.1 typed: %s -- lam_max increases on %.0f percent "
          "of steps (bar 90)" % (l3_type, 100 * frac_mono), True)

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
        r = compressed_window(9, **kw)
        fired = (r not in (None, "TOO-DEEP")) and r["lamE"] > 1.0
        ok &= fired
        print("    %-8s: lam(E) %s -> fires %s%s"
              % (nmc, "%.3e" % r["lamE"]
                 if r not in (None, "TOO-DEEP") else "n/a", fired,
                 "" if r in (None, "TOO-DEEP")
                 or r["CJ"] is not None
                 else " (window unavailable, typed -- SPEC v2)"))
    check("C1 CONTROLS FIRE (SPEC v2: on the plain-Gram value)",
          ok, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("CONTROL-DEAD" if KILLS else "LADDER-MEASURED")
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, l1_type,
                                         l3_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
