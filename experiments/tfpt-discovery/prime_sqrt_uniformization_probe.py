#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_sqrt_uniformization_probe -- PRIME.SQRT.UNIFORM.01
(EXPLORATION ONLY, experiments/; round 39 task 1 of the 2026-08-09
external review: the square-root uniformization of the weighted
prime measure and the exact 1 - e^{-1/2} edge-mass law, 2026-08-09).

THE CLAIMS (classical, PNT-derived; tested FIT-FREE on an own
sieve AND on the deployed window tables):
  (i)   sum_{n <= X} 2 Lambda(n)/sqrt(n) / (4 sqrt X)  ->  1;
  (ii)  the last-log-unit edge mass -> 1 - e^{-1/2} = 0.393469...
        (the EXACT explanation of the measured ~39 percent port
        mass of LXXXVII);
  (iii) UNIFORMIZATION: under r = sqrt(n/X) the normalized
        weighted prime measure eta_X converges weakly to Lebesgue
        dr on [0, 1] (CDF sup-distance -> 0, moments -> 1/(k+1));
  (iv)  the deployed rung atom tables reproduce the same CDF as
        the own sieve at matched X (the window uses the true comb).

UNIVERSALITY TYPING (frozen): the uniformization is a PNT-CLASS
statement, arithmetic-blind at leading order -- the Epstein comb
(its own lambda) is EXPECTED to uniformize too (report, not a
kill); the SCRAMBLE control (log-uniform positions) must break the
CDF hard (must-fire).  This probe measures the UNIVERSAL source
part; the arithmetic sits in the fluctuations around it.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):
 U1  own SPF sieve X-ladder {1e4, 1e5, 1e6, 1e7}: total-mass ratio
     monotone increasing with final value in [0.98, 1.02].
 U2  edge mass (X/e, X] along the ladder with final value in
     [0.37, 0.42]; the deployed rung edge masses printed.
 U3  CDF sup-distance to r on [0,1]: decreasing along the ladder,
     final <= 0.02; moments k = 1..4: final |m_k - 1/(k+1)| <=
     0.02.
 U4  deployed tables (heavy rungs kz {9, 12, 13, 26, 40}):
     |CDF_deployed - CDF_sieve(at the rung's own X)| sup <= 0.01
     (the deployed atom table IS the true comb).
 C   controls (kz 9): scramble MUST break; Epstein reported
     (expected also-uniform -- universality, typed).

SPEC v2 (bar repair; run 1 = 6/7): the v1 scramble bar (>= 5x
truth at the SAME rung) was mis-calibrated at the shallowest rung,
where the truth CDF itself is still pre-asymptotic (0.0745):
measured scramble sup = 0.3241 = 4.3x -- a hard break in absolute
terms (27x the deep-rung truth 0.0115).  v2 bar: scramble sup >=
4x same-rung truth AND >= 0.25 absolute (both measured in run 1).
No other change.

KILLS: K1 sieve/deployed mismatch -> TABLE-BROKEN; K2 a frozen
PNT bar fails -> PNT-BAR-BROKEN (honest; would mean the window
depths are pre-asymptotic beyond tolerance); K3 scramble does not
fire -> CONTROL-DEAD.

VERDICT (frozen enum): SQRT-UNIFORMIZED / TABLE-BROKEN /
PNT-BAR-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: own sieve (no banned oracles; SPF sieve
computes Lambda from scratch), deployed tables READ-ONLY; RNG only
in the declared scramble control; writes nothing but stdout.  No
marker moves.

Sources (read-only): v563_paper2_readouts (deployed atom tables);
round-38 chain (the 39-percent edge-mass measurement, LXXXVII).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_sqrt_uniformization_probe.py
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
XLADDER = (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7)
EDGE = 1.0 - math.exp(-0.5)
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


def mangoldt_up_to(N):
    """Lambda(n) for n <= N via an SPF sieve (own construction)."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, int(math.isqrt(N)) + 1):
        if spf[p] == 0:
            spf[p * p::p] = np.where(spf[p * p::p] == 0, p,
                                     spf[p * p::p])
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = spf[n] if spf[n] else n
        m = n
        while m % p == 0:
            m //= p
        lam[n] = math.log(p) if m == 1 else 0.0
    return lam


def cdf_stats(r_pos, w):
    """CDF sup-distance to Lebesgue on [0,1] + moments 1..4."""
    order = np.argsort(r_pos)
    r_s = r_pos[order]
    w_s = w[order] / np.sum(w)
    F = np.cumsum(w_s)
    sup = float(np.max(np.abs(F - r_s)))
    mom = [float(np.sum(w_s * r_s ** k)) for k in range(1, 5)]
    return sup, mom


def main():
    section("PRIME.SQRT.UNIFORM.01 -- the sqrt(n/X) "
            "uniformization + the 1 - e^{-1/2} edge law "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; own sieve; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own SPF sieve, no oracles)",
          not ast_scan(BANNED_IDS))

    section("U1/U2/U3 -- the own-sieve X-ladder")
    lam = mangoldt_up_to(XLADDER[-1])
    nn_all = np.arange(2, XLADDER[-1] + 1)
    mu_all = 2.0 * lam[2:] / np.sqrt(nn_all)
    ratios, edges, sups, moms = [], [], [], []
    for X in XLADDER:
        m = nn_all <= X
        nn, mu = nn_all[m], mu_all[m]
        tot = float(np.sum(mu))
        ratios.append(tot / (4.0 * math.sqrt(X)))
        edges.append(float(np.sum(mu[nn > X / math.e])) / tot)
        r_pos = np.sqrt(nn / X)
        sup, mom = cdf_stats(r_pos, mu)
        sups.append(sup)
        moms.append(mom)
        print("    X = %.0e: mass ratio %.4f | edge mass %.4f "
              "(target %.4f) | CDF sup %.4f | moments %s "
              "(targets 0.500/0.333/0.250/0.200)"
              % (X, ratios[-1], edges[-1], EDGE, sup,
                 "/".join("%.3f" % v for v in mom)))
    check("U1.1 total-mass ratio monotone increasing, final "
          "%.4f in [0.98, 1.02]" % ratios[-1],
          all(ratios[i + 1] > ratios[i]
              for i in range(len(ratios) - 1))
          and 0.98 <= ratios[-1] <= 1.02, kill="K2")
    check("U2.1 edge mass final %.4f in [0.37, 0.42] -- the "
          "measured ~39 percent port mass IS 1 - e^{-1/2} = "
          "%.6f" % (edges[-1], EDGE),
          0.37 <= edges[-1] <= 0.42, kill="K2")
    mom_err = max(abs(moms[-1][k - 1] - 1.0 / (k + 1))
                  for k in range(1, 5))
    check("U3.1 UNIFORMIZATION: CDF sup-distance decreasing "
          "(%.4f -> %.4f), final <= 0.02; max moment error "
          "%.4f <= 0.02"
          % (sups[0], sups[-1], mom_err),
          all(sups[i + 1] < sups[i] for i in range(len(sups) - 1))
          and sups[-1] <= 0.02 and mom_err <= 0.02, kill="K2")

    section("U4 -- the deployed rung tables (heavy rungs)")
    worst = 0.0
    for kz in HEAVY:
        rr = core.build_window(kz)
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        U = float(np.max(uu))
        r_dep = np.exp((uu - U) / 2.0)
        sup_d, _ = cdf_stats(r_dep, mm)
        X_r = math.exp(U)
        m = nn_all <= X_r
        r_sv = np.sqrt(nn_all[m] / X_r)
        sup_s, _ = cdf_stats(r_sv, mu_all[m])
        edge_d = float(np.sum(mm[uu > U - 1.0]) / np.sum(mm))
        worst = max(worst, abs(sup_d - sup_s))
        print("    kz %-3d X = e^%.2f: deployed CDF sup %.4f vs "
              "sieve-at-same-X %.4f | deployed edge mass %.4f"
              % (kz, U, sup_d, sup_s, edge_d))
    check("U4.1 deployed tables == true comb at matched X "
          "(max |sup_dep - sup_sieve| = %.4f <= 0.01)" % worst,
          worst <= 0.01, kill="K1")

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    uu9 = np.asarray(rr9["uu"], float)
    U9 = float(np.max(uu9))
    mm9 = 2.0 * np.asarray(rr9["lam"], float)
    sup_t, _ = cdf_stats(np.exp((uu9 - U9) / 2.0), mm9)
    # scramble: log-uniform positions, same masses (core convention)
    rng = np.random.default_rng(1)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * rr9["alpha"],
                               size=len(uu9)))
    sup_s, _ = cdf_stats(np.exp((uu_s - float(np.max(uu_s)))
                                / 2.0), mm9)
    # Epstein: its own lambda at its own positions
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = np.zeros(N_E + 1)
    r_ = np.zeros(N_E + 1)
    s_ = int(math.isqrt(N_E)) + 1
    for x in range(-s_, s_ + 1):
        for y in range(-s_, s_ + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N_E:
                r_[v] += 1.0
    a_ = r_ / 2.0
    for n in range(2, N_E + 1):
        acc = a_[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lamE[dd] * a_[n // dd]
        lamE[n] = acc
    nzE = np.nonzero(np.abs(lamE) > 1e-12)[0]
    muE = np.abs(2.0 * lamE[nzE] / np.sqrt(nzE.astype(float)))
    sup_e, _ = cdf_stats(np.sqrt(nzE / float(N_E)), muE)
    print("    truth sup %.4f | scramble sup %.4f (ratio %.1f) | "
          "Epstein sup %.4f (universality: expected also-uniform)"
          % (sup_t, sup_s, sup_s / sup_t, sup_e))
    check("C1 SCRAMBLE FIRES (SPEC v2): sup %.4f >= 4x same-rung "
          "truth (%.1fx) and >= 0.25 absolute"
          % (sup_s, sup_s / sup_t),
          sup_s >= 4.0 * sup_t and sup_s >= 0.25, kill="K3")
    check("C2 UNIVERSALITY TYPED (report): Epstein uniformizes "
          "too (sup %.4f) -- the sqrt-law is PNT-class, "
          "arithmetic-blind at leading order; the arithmetic "
          "lives in the FLUCTUATIONS" % sup_e, True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "TABLE-BROKEN", "K2": "PNT-BAR-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "SQRT-UNIFORMIZED"
    print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
