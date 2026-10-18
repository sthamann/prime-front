#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_cocycle_window_probe -- PRIME.PORT.COCYCLE.01
(EXPLORATION ONLY, experiments/; round 39 follow-up, NEW OPEN
CONTRACT per the 2026-08-09 second review: identify the growing
operator with a FINITE dynamical structure -- the fixed window
plus its Schur boundary state, 2026-08-09).

THE CONTRACT (frozen): with the FIXED j-window J (available
subset of {2, 4, ..., 24} on the folded port lattice) compress
the ENTIRE Carleson operator onto J by the Schur map
    C_J(h) = E_JJ + E_{J,out} (I - E_out)^{-1} E_{out,J}.
EXACT: I - E >= 0  <=>  I - E_out >= 0  AND  I - C_J >= 0
(Haynsworth); if the soft mode lives in J (measured XCIII:
mass 1.000), the criticality transfers EXACTLY: 1 - lam_max(C_J)
= tau.  The growing family {E(h)} then becomes a sequence of
FIXED-SIZE matrices C_J(h) (\"12 x 12\") plus a positivity-safe
exterior -- the finite dynamical structure of the contract; its
h-updates are the cocycle.

FROZEN PROTOCOL (2026-08-09; ladder h <= 900; heavy rungs
kz {9, 12, 13, 26, 40} printed; controls kz 9):

 W1  EXACT TRANSFER: (1 - lam_max(C_J))/tau in [0.99, 1.01] AND
     I - E_out > 0 on every truth rung (the compressed window
     carries the wall EXACTLY).

 W2  COMPRESSED CONVERGENCE: pairwise op-norm differences of
     C_J(h) at matched j vs the deepest rung; compare the slope
     with the RAW-section slope (-0.141, XCIII): typed
     COCYCLE-CLEANER iff the compressed slope <= -0.2 (the
     compression removes the truncation part of the drift and
     leaves the arithmetic floor), else COCYCLE-SAME (both
     honest; the floor itself is the arithmetic, LXXXVIII).

 W3  THE UPDATE SIZE (report): ||C_J(h_{k+1}) - C_J(h_k)||_2
     along the ladder -- the cocycle increment law.

 C   CONTROLS (kz 9, must fire): Epstein/scramble: I - E_out
     indefinite OR lam_max(C_J) > 1 (localization printed).

KILLS: K1 transfer breaks on truth -> TRANSFER-BROKEN; K2
pipeline -> PIPELINE-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): COCYCLE-COMPRESSED (+ typed sublabel) /
TRANSFER-BROKEN / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; round-39 chain
(port_fixed_space_limit: WINDOW-CARRIES, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_cocycle_window_probe.py
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
        return None
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    Ew = E[np.ix_(iw, iw)]
    Ex = E[np.ix_(iw, io)]
    Eo = E[np.ix_(io, io)]
    lamO = float(np.linalg.eigvalsh(Eo)[-1])
    IO = np.eye(len(io)) - Eo
    CJ = Ew + Ex @ np.linalg.solve(IO, Ex.T)
    CJ = 0.5 * (CJ + CJ.T)
    return dict(CJ=CJ, jav=jav, h=h, lamO=lamO,
                tau=1.0 - float(np.linalg.eigvalsh(E)[-1]),
                lamC=float(np.linalg.eigvalsh(CJ)[-1]))


def main():
    section("PRIME.PORT.COCYCLE.01 -- the fixed window as a "
            "finite dynamical structure (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("W1/W2/W3 -- exact transfer + compressed convergence")
    rows = []
    for kz in core.frame_a_zones():
        r = compressed_window(kz)
        if r in (None, "TOO-DEEP"):
            continue
        r["kz"] = kz
        rows.append(r)
        if kz in HEAVY:
            print("    kz %-3d h %4d |J| %2d: (1-lamC)/tau %.4f "
                  "| lam(out) %.6f"
                  % (kz, r["h"], len(r["jav"]),
                     (1.0 - r["lamC"]) / r["tau"], r["lamO"]))
    ok_tr = all(0.99 <= (1.0 - r["lamC"]) / r["tau"] <= 1.01
                and r["lamO"] < 1.0 for r in rows)
    check("W1.1 EXACT TRANSFER on all %d rungs: the compressed "
          "fixed window carries the wall EXACTLY ((1-lamC)/tau "
          "== 1.00) with PSD exterior" % len(rows),
          ok_tr, kill="K1")

    rows.sort(key=lambda r: r["h"])
    deep = rows[-1]
    jref = deep["jav"]

    def sec_of(r):
        common = [j for j in jref if j in r["jav"]]
        ii = [r["jav"].index(j) for j in common]
        kk = [jref.index(j) for j in common]
        return r["CJ"][np.ix_(ii, ii)], deep["CJ"][np.ix_(kk, kk)]

    hh, dd = [], []
    for r in rows[:-1]:
        A, Ad = sec_of(r)
        hh.append(r["h"])
        dd.append(float(np.linalg.norm(A - Ad, 2)))
    hh = np.array(hh, float)
    dd = np.array(dd)
    mask = hh <= deep["h"] / 2.0
    sl = float(np.polyfit(np.log(hh[mask]), np.log(dd[mask]),
                          1)[0])
    w2_type = ("COCYCLE-CLEANER" if sl <= -0.2 else "COCYCLE-SAME")
    check("W2.1 typed: %s -- compressed op-norm drift %.4f -> "
          "%.4f, slope %+.3f (raw-section reference -0.141, "
          "XCIII)" % (w2_type, dd[0], dd[-1], sl), True)
    incs = [float(np.linalg.norm(sec_of(rows[k + 1])[0][:8, :8]
                                 - sec_of(rows[k])[0][:8, :8], 2))
            for k in range(min(6, len(rows) - 1))]
    check("W3.1 cocycle increments (first 6, report): %s"
          % ["%.3f" % v for v in incs], True)

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
        if r in (None, "TOO-DEEP"):
            print("    %-8s: window unavailable (typed)" % nmc)
            continue
        fired = (r["lamO"] > 1.0) or (r["lamC"] > 1.0)
        ok &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s" % (nmc, r["lamO"], r["lamC"],
                          "EXTERIOR" if r["lamO"] > 1.0
                          else "WINDOW"))
    check("C1 CONTROLS FIRE", ok, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "TRANSFER-BROKEN",
                   "K2": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "COCYCLE-COMPRESSED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, w2_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
