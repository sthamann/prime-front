#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_prime_error_feshbach_probe -- PRIME.PORT.FESHBACH.01
(EXPLORATION ONLY, experiments/; round 39 task 6 of the 2026-08-09
external review: the wall margin as a scalar prime-error
functional (Feshbach reading) + the two-level detector law --
WITH the review's Section-10 exponent CORRECTED against the
measured data, 2026-08-09).

PART F1, THE FESHBACH BUDGET: with a FIXED reference vector v_ref
(top eigenvector of the deepest rung's port section at matched j),
the rank-one Rayleigh functional q_h = v_ref^T A_h v_ref gives
1 - q_h >= tau_h with excess controlled by the misalignment:
1 - q_h ~ tau_h + sin^2(angle) * (spectral gap).  MEASURE the
ratio (1 - q_h)/tau_h and the required alignment budget
eps*_h = sqrt(tau_h / (lam_1 - lam_2)) per rung -- the honest
quantification of HOW precisely v_infty must be known before the
wall margin becomes a single explicit quadratic functional of the
prime comb.  (No bar -- the budget IS the deliverable.)

FROZEN AMPLITUDE CONVENTION (fixed here once, per the round-39
follow-up review, so it need never be re-discussed): A is the
amplitude of the lag injection Delta c(tau) = A cos(gamma0 tau)
(cosh(delta tau) - 1) with A = 2 corresponding to ONE off-line
zero quadruple; delta is the off-line displacement in the
s-variable.  In THIS normalization the measured response is
    Delta lambda = O(A^2 delta^4),   NOT O(A^2 delta^2)
(the delta^2 enters LINEARLY in Delta c through cosh - 1 and the
floor responds QUADRATICALLY in ||Delta c||), whence
A* ~ sqrt(tau)/delta^2.

PART F2, THE TWO-LEVEL LAW (review Section 10, CORRECTED): the
review derives A* ~ sqrt(tau)/|delta| from Delta-lambda ~ A^2
delta^2.  The LXXXVIII data CONTRADICT the delta-exponent
(measured A*(0.05)/A*(0.10) = 4.02-4.08 = (0.10/0.05)^2, not 2).
The corrected derivation: the injected lag signature is
Delta c = A cos(gamma0 u)(cosh(delta u) - 1) ~ A delta^2 u^2 / 2
-- LINEAR in A, QUADRATIC in delta -- and the floor response is
second order in ||Delta c|| (the LXXXVIII energy law), hence
    Delta-lambda ~ A^2 delta^4  ==>  A* ~ sqrt(tau)/delta^2.
FROZEN TEST: recompute A* by bisection on rungs kz {9, 13, 26} x
delta {0.05, 0.10} x gamma0 {10, 40}; the delta-pair ratio
    rho = [A*(0.05) * 0.05^2] / [A*(0.10) * 0.10^2]
must lie in [0.85, 1.15] for every (rung, gamma0) cell (the
delta^2 exponent); the prefactor c(gamma0, rung) = A* delta^2 /
sqrt(tau) printed (its rung-dependence = the gamma0-coupling,
report).  Typed TWO-LEVEL-LAW-CONFIRMED / LAW-BROKEN.

 C   CONTROLS: the built-in null control of the injection
     (delta = 0 -> Delta c == 0 exactly) re-warded.

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 the delta^2 law
fails -> LAW-BROKEN (would revive the review's delta^1 form);
K3 null control fails -> CONTROL-DEAD.

VERDICT (frozen enum): FESHBACH-MEASURED (+ typed sublabel) /
PIPELINE-BROKEN / LAW-BROKEN / CONTROL-DEAD.

NO RH claim; the two-level law is a DETECTOR-SCALING statement
([E]-grade candidate), not progress on the conjecture -- typed
per the review's own Section-10 instruction.

FIREWALL: no zeros, no prime oracles (AST scan; gamma0 generic
frozen frequencies); v563 READ-ONLY; no RNG; stdout only.

Sources (read-only): v563_paper2_readouts; round-38/39 chain
(errorterm_demand_curve LXXXVIII + port_fixed_space, declared
inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_prime_error_feshbach_probe.py
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

RUNGS_F2 = (9, 13, 26)
DELTAS = (0.05, 0.10)
GAMMAS = (10.0, 40.0)
HEAVY = (12, 13, 26, 40)
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


def build_lags(kz):
    rr = core.build_window(kz)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return dict(c=c_ar + np.asarray(c_at, float), M=M, D=D,
                alpha=alpha, h=h, L=2 * M - 2)


def floor_of(c, M):
    K = core.odd_toeplitz(c, M)
    d = grid_density(c)
    c_abs = np.real(np.fft.ifft(np.abs(d)))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    Gp = 0.5 * (Tabs + K)
    Gm = 0.5 * (Tabs - K)
    ev, V = np.linalg.eigh(Gp)
    if float(ev[0]) <= 0.0:
        return None
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    lam = np.linalg.eigvalsh(0.5 * (A + A.T))
    return 1.0 - float(lam[-1])


def zero_signature(M, D, delta, gamma0):
    tt = np.arange(M) * D
    return np.cos(gamma0 * tt) * (np.cosh(delta * tt) - 1.0)


def critical_A(b, sig, steps=16):
    best = float("inf")
    for s in (+1.0, -1.0):
        hi = 4.0
        t_hi = floor_of(b["c"] + s * hi * sig, b["M"])
        grow = 0
        while (t_hi is None or t_hi > 0.0) and grow < 8:
            hi *= 4.0
            t_hi = floor_of(b["c"] + s * hi * sig, b["M"])
            grow += 1
        if t_hi is None or t_hi > 0.0:
            continue
        lo = 0.0
        for _ in range(steps):
            mid = 0.5 * (lo + hi)
            t_m = floor_of(b["c"] + s * mid * sig, b["M"])
            if t_m is None or t_m < 0.0:
                hi = mid
            else:
                lo = mid
        best = min(best, hi)
    return best


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


def port_section(kz):
    rr = core.build_window(kz)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
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
    kk = [idx[j] for j in jav]
    return dict(A=DP[np.ix_(kk, kk)], jav=jav, h=h,
                lamD=float(np.linalg.eigvalsh(DP)[-1]))


def main():
    section("PRIME.PORT.FESHBACH.01 -- the prime-error functional "
            "budget + the corrected two-level law (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("F1 -- the Feshbach alignment budget")
    secs = {kz: port_section(kz) for kz in HEAVY}
    deep = secs[40]
    jref = deep["jav"]
    evd, Vd = np.linalg.eigh(deep["A"])
    vref_full = Vd[:, -1]
    for kz in HEAVY:
        r = secs[kz]
        common = [j for j in jref if j in r["jav"]]
        ir = [jref.index(j) for j in common]
        ic = [r["jav"].index(j) for j in common]
        v = vref_full[ir]
        v = v / np.linalg.norm(v)
        A = r["A"][np.ix_(ic, ic)]
        q = float(v @ A @ v)
        ev = np.linalg.eigvalsh(r["A"])
        tau = 1.0 - r["lamD"]
        gap = float(ev[-1] - ev[-2])
        eps = math.sqrt(tau / gap)
        print("    kz %-3d h %4d: (1-q)/tau = %8.1f | gap %.2e | "
              "alignment budget eps* = sqrt(tau/gap) = %.2e"
              % (kz, r["h"], (1.0 - q) / tau, gap, eps))
    check("F1.1 FESHBACH BUDGET measured (report): the wall "
          "margin becomes a single explicit prime-comb "
          "functional exactly when v_infty is known to precision "
          "eps* = sqrt(tau/gap) -- the printed budget IS the "
          "quantified demand on the limit eigenvector", True)

    section("F2 -- the corrected two-level law A* ~ sqrt(tau)/"
            "delta^2")
    sig0 = zero_signature(512, 0.01, 0.0, GAMMAS[0])
    check("C0 NULL CONTROL: delta = 0 injection identically zero "
          "(max %.1e)" % float(np.max(np.abs(sig0))),
          float(np.max(np.abs(sig0))) == 0.0, kill="K3")
    ok_law = True
    for kz in RUNGS_F2:
        b = build_lags(kz)
        tau0 = floor_of(b["c"], b["M"])
        for ga in GAMMAS:
            As = {}
            for de in DELTAS:
                sig = zero_signature(b["M"], b["D"], de, ga)
                As[de] = critical_A(b, sig)
            rho = (As[0.05] * 0.05 ** 2) / (As[0.10] * 0.10 ** 2)
            cpre = As[0.10] * 0.10 ** 2 / math.sqrt(tau0)
            ok_cell = 0.85 <= rho <= 1.15
            ok_law &= ok_cell
            print("    kz %-3d gamma0 %4.0f: A*(0.05) %.3e, "
                  "A*(0.10) %.3e | delta^2-ratio %.3f %s | "
                  "prefactor c = A* d^2/sqrt(tau) = %.3e"
                  % (kz, ga, As[0.05], As[0.10], rho,
                     "OK" if ok_cell else "BAD", cpre))
    law_type = ("TWO-LEVEL-LAW-CONFIRMED" if ok_law
                else "LAW-BROKEN")
    check("F2.1 typed: %s -- A* delta^2 is delta-invariant on "
          "every cell (bar [0.85, 1.15]): the corrected law is "
          "A* ~ sqrt(tau)/delta^2 (review Section 10 exponent "
          "delta^1 REFUTED by the same data; detector-scaling "
          "statement, NOT RH progress)" % law_type, ok_law,
          kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN", "K2": "LAW-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "FESHBACH-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, law_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
