#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""case_sum_rule_probe -- PRIME.CASE.SUMRULE.01
(EXPLORATION ONLY, experiments/; round 39 follow-up, step 1 of the
solve plan: the criticality budget as a Case/Killip-Simon sum
rule -- the measured half, plus the registered analytic contract,
2026-08-09).

CONTEXT: the criticality budget of LXXXVII (PNT growth +1.405 +
geometry -1.674 + Christoffel +0.284 = +0.015 == d log T/d alpha)
is the numerical shadow of a sum rule: in Case/Killip-Simon
theory, spectral statements at the edge are EQUIVALENT to
coefficient functionals of the Jacobi chain -- with no margin, no
absolute values, no partitions (the only certificate class left
open by the no-gos N1-N4).  This probe measures the KS-class
status of the deployed chains and REGISTERS the analytic contract.

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
controls kz 9):

 K1  KS FUNCTIONAL: G(m) = sum_{k <= m} [a_k^2 + (2 b_k - 1)^2]
     of the mu~+ chain (a_k should be ~0 by near-symmetry, b_k ->
     1/2 by the Szego signature): G bounded along the chain
     interior with SHRINKING increments (G(3h/4) - G(h/2) <
     G(h/2) - G(h/4)) on every heavy rung -- the numerical
     Killip-Simon-class signature; the chain-end spike (the
     truncation boundary) reported separately.

 K2  SZEGO PARTIAL SUMS: s(m) = -sum_{k <= m} log(2 b_k):
     stabilization on the interior (|s(3h/4) - s(h/2)| <
     |s(h/2) - s(h/4)|); values printed (the finite Szego
     integral estimate).

 K3  THE REGISTERED CONTRACT (printed, the analytic target):
     PRIME.CASE.SUMRULE.01 -- prove the C0/C1 Case sum rule for
     the deployed tilde-measure family and derive from it the
     UNCONDITIONAL testing bound T_h <= 1 (the diagonal half of
     the wall); the measured budget identity is the target
     equation; success = the first proven h-uniform statement of
     the route; the off-diagonal lift stays open (RH-hard, per
     LXXXVIII).

 C   CONTROLS (kz 9): scramble chain compared (its KS functional
     and Szego sums printed; the source side is expected to be
     KS-regular too -- universality typed, NOT a kill); must-fire
     only on pipeline sanity (chain completes).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN.  K1/K2 stabilization
bars may FAIL honestly (typed, kept).

VERDICT (frozen enum): KSCLASS-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; LXXXVII budget +
LXXXIX survey (Case/Killip-Simon reading), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/case_sum_rule_probe.py
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


def chain_of(kz, scramble_seed=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    jj = np.arange(L)
    keep = d > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (d[keep] / (2.0 * L)) * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    xs, wagg = xs[m], wagg[m]
    n = h + 1
    m0 = float(np.sum(wagg))
    Q = np.zeros((len(xs), n))
    Q[:, 0] = np.sqrt(wagg) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(n - 1)
    for k in range(n):
        z = xs * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        nb = float(np.linalg.norm(z))
        if nb <= 1e-14:
            return None
        be[k] = nb
        Q[:, k + 1] = z / nb
    return dict(a=al[:h], b=be[:h], h=h)


def main():
    section("PRIME.CASE.SUMRULE.01 -- the KS-class measurement + "
            "the registered analytic contract (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("K1/K2 -- KS functional + Szego sums (heavy rungs)")
    ok_ks = ok_sz = True
    for kz in HEAVY:
        c = chain_of(kz)
        if c is None:
            check("K0 chain short at kz %d" % kz, False,
                  kill="K1")
            continue
        a, b, h = c["a"], c["b"], c["h"]
        G = np.cumsum(a ** 2 + (2.0 * b - 1.0) ** 2)
        s = -np.cumsum(np.log(2.0 * b))
        q1, q2, q3 = h // 4, h // 2, (3 * h) // 4
        dG1, dG2 = G[q2] - G[q1], G[q3] - G[q2]
        dS1, dS2 = abs(s[q2] - s[q1]), abs(s[q3] - s[q2])
        ok_ks &= (dG2 < dG1)
        ok_sz &= (dS2 < dS1)
        print("    kz %-3d h %4d: G(h/4|h/2|3h/4|h-1) = "
              "%.3f|%.3f|%.3f|%.3f (incr %.3f -> %.3f) | s: "
              "%.3f|%.3f|%.3f (incr %.3f -> %.3f)"
              % (kz, h, G[q1], G[q2], G[q3], G[-1], dG1, dG2,
                 s[q1], s[q2], s[q3], dS1, dS2))
    check("K1.1 KS FUNCTIONAL: interior increments shrink on all "
          "heavy rungs (numerical Killip-Simon-class signature)",
          ok_ks)
    check("K2.1 SZEGO SUMS: interior stabilization on all heavy "
          "rungs", ok_sz)

    section("K3 -- the registered analytic contract")
    print("""    PRIME.CASE.SUMRULE.01 (registered): PROVE the
    C0/C1 Case sum rule for the deployed tilde-measure family
    (source-only data: PNT growth of nu~, window geometry,
    Christoffel/chain coefficients b_k -> 1/2) and DERIVE the
    unconditional testing bound T_h <= 1 -- the diagonal half of
    the wall.  Target equation = the measured LXXXVII budget
    identity (s_d + s_geo + s_K = 0).  The off-diagonal lift
    remains RH-hard (LXXXVIII).  Success = the first proven
    h-uniform statement of the route.""")
    check("K3.1 contract registered (statement printed)", True)

    section("C -- control comparison (kz 9 scramble)")
    c = chain_of(9, scramble_seed=1)
    if c is not None:
        a, b, h = c["a"], c["b"], c["h"]
        G = np.cumsum(a ** 2 + (2.0 * b - 1.0) ** 2)
        print("    scramble: G(h/2) %.3f vs G(h-1) %.3f "
              "(universality: source side KS-regular too, typed "
              "-- the arithmetic is NOT in the chain class)"
              % (G[h // 2], G[-1]))
    check("C1 pipeline sanity (scramble chain completes)",
          c is not None, kill="K1")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("PIPELINE-BROKEN" if KILLS else "KSCLASS-MEASURED")
    print("\n  VERDICT: %s (%s + %s)"
          % (VERDICT,
             "KS-SHRINKING" if ok_ks else "KS-IRREGULAR",
             "SZEGO-STABLE" if ok_sz else "SZEGO-DRIFTING"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
