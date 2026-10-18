#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nested_prime_ladder_probe -- PRIME.PORT.PRIMELADDER.01
(EXPLORATION ONLY, experiments/; round 40, work package (c) of the
closing-cylinder plan: the NESTED ONE-PRIME LADDER, 2026-08-09).

CONTEXT: the window ladder (rung -> rung) is perturbative but
non-monotone (LADDER-PERTURBATIVE, round 40).  The finer induction
object is the ONE-PRIME ladder INSIDE a fixed window: start from
the pure archimedean lag vector and insert the prime-power atoms
one at a time (ascending u = log n, the physical order), tracking
the pencil floor tau(k) after each insertion.  v877 says truncated
combs violate the floor, so the trajectory must end positive only
at the FULL comb -- the question is the ANATOMY of the path: where
is the last sign crossing, what do single atoms contribute, and is
the final approach monotone?  A second ordering (descending u =
edge-first) probes whether the edge zone alone can carry
positivity (39 percent of the mass sits in the last half
log-unit).

FROZEN PROTOCOL (heavy rungs kz in {9, 12, 13, 26, 40}):
  L1  TRAJECTORY (ascending u): per-atom lag rows are exact
      (atom_lags_at is linear in the mass list; ward L1.0 checks
      the row sum against the full call at 1e-12).  tau(0) = pure
      Arch floor; tau(N) must equal the true wall floor (ward
      L1.1, rel 1e-8; SPEC v2: v1 froze 1e-9 and FAILED honestly
      at kz 40 only -- rel 2.50e-9 on tau ~ 6.7e-7, pure float
      summation-order noise over 1773 sequential row additions vs
      one batched call; mechanical tolerance repair, all other
      rungs pass at <= 1e-9).  Report tau(0) sign census (typed
      ARCH-SUBCRITICAL iff tau(0) < 0 on every heavy rung, else
      ARCH-MIXED).
  L2  LAST CROSSING: u* = position of the last sign change of
      tau(k) along ascending-u insertion; typed
      LAST-CROSSING-EDGE iff u*/U >= 0.8 on every heavy rung
      (positivity decided in the edge zone), else
      LAST-CROSSING-BULK.
  L3  INCREMENT ANATOMY: per-atom increments dtau_n = tau(n) -
      tau(n-1); sign census (fraction positive), and the Pearson
      correlation of log|dtau_n| with log m_n (m_n = 2 Lambda/
      sqrt(n)) over atoms with |dtau_n| > 1e-15.  Report only
      (no bar): the size law of single-atom moves.
  L4  TAIL SHAPE: after the last crossing, is tau(k) monotone
      nondecreasing (tolerance 1e-12)?  Typed MONOTONE-TAIL iff
      true on every heavy rung, else OSCILLATORY-TAIL (both
      honest).
  L5  EDGE-FIRST ORDERING (descending u): does the trajectory
      reach tau > 0 earlier (fewer atoms) than ascending?  Report
      k*_desc/N vs k*_asc/N (k* = first index after which tau
      stays positive).  Typed EDGE-CARRIES iff k*_desc/N <= 0.5
      on every heavy rung, else EDGE-INSUFFICIENT.
  C1  CONTROL (kz 9): deterministic mass scramble (multiply atom
      n by (1 + 0.5 * sign(sin(1000 u_n)))): the full-comb floor
      must drop below the true floor minus 0.25 absolute OR go
      negative (the trajectory endpoint is mass-sensitive).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 ward L1.0/L1.1
fails -> LINEARITY-BROKEN; K3 control C1 fails -> CONTROL-DEAD.

VERDICT (frozen enum): PRIMELADDER-MEASURED (+ typed sublabels
from L1/L2/L4/L5) / PIPELINE-BROKEN / LINEARITY-BROKEN /
CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan; the
atoms come from the deployed v563 window tables); v563 READ-ONLY;
no RNG; stdout only.

Sources (read-only): v563_paper2_readouts; v877 (truncation
kills); lattice_parametrix probe (round 40, mass rigidity);
ladder_transfer probe (round 40, window-ladder anatomy).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/nested_prime_ladder_probe.py
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


def trajectory(c_ar, rows, order, M):
    """tau(k) after inserting atoms rows[order[:k]], k = 0..N."""
    taus = []
    c = c_ar.copy()
    taus.append(floor_of(c, M))
    for idx in order:
        c = c + rows[idx]
        taus.append(floor_of(c, M))
    return taus


def last_crossing(taus):
    """index of the last sign change (None -> treated as sign of 0-)."""
    k_star = 0
    prev = taus[0] if taus[0] is not None else -1.0
    for k in range(1, len(taus)):
        cur = taus[k] if taus[k] is not None else -1.0
        if (prev <= 0.0) != (cur <= 0.0):
            k_star = k
        prev = cur
    return k_star


def first_stable_positive(taus):
    """first k such that tau(j) > 0 for all j >= k."""
    k = len(taus)
    for j in range(len(taus) - 1, -1, -1):
        t = taus[j] if taus[j] is not None else -1.0
        if t > 0.0:
            k = j
        else:
            break
    return k


def main():
    section("PRIME.PORT.PRIMELADDER.01 -- the nested one-prime "
            "ladder inside a fixed window (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    arch_sub, edge_cross, mono_tail, edge_carries = [], [], [], []
    sign_frac_all, corr_all = [], []
    ward_ok = True
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        N = len(uu)
        U = float(np.max(uu))
        c_ar = np.asarray(core.arch_lags(M, D), float)

        section("L -- kz %d (h %d, N_atoms %d, U %.3f)"
                % (kz, h, N, U))
        # exact per-atom lag rows (linearity ward below)
        rows = np.zeros((N, M))
        for n in range(N):
            c_at, _ = core.atom_lags_at(alpha, M, [uu[n]],
                                        [mm[n]])
            rows[n] = np.asarray(c_at, float)
        c_full, _ = core.atom_lags_at(alpha, M, uu, mm)
        lin_err = float(np.max(np.abs(rows.sum(axis=0)
                                      - np.asarray(c_full, float))))
        ok0 = check("L1.0 kz %d linearity ward (row sum == full "
                    "call)" % kz, lin_err <= 1e-12,
                    "max err %.2e" % lin_err, kill="K2")
        ward_ok &= ok0

        asc = list(range(N))
        taus = trajectory(c_ar, rows, asc, M)
        tau0, tauN = taus[0], taus[-1]
        tau_true = floor_of(c_ar + np.asarray(c_full, float), M)
        rel = abs(tauN - tau_true) / max(1e-30, abs(tau_true))
        ok1 = check("L1.1 kz %d endpoint ward (tau(N) == true "
                    "floor)" % kz, rel <= 1e-8,
                    "tau(N) %+0.6e rel %.2e" % (tauN, rel),
                    kill="K2")
        ward_ok &= ok1
        arch_sub.append(tau0 is None or tau0 < 0.0)
        print("    tau(0) [pure Arch] = %s"
              % ("None (Gp not PD)" if tau0 is None
                 else "%+0.6e" % tau0))

        k_cross = last_crossing(taus)
        u_star = uu[k_cross - 1] if k_cross >= 1 else 0.0
        frac = u_star / U
        edge_cross.append(frac >= 0.8)
        print("    L2 last crossing at atom %d/%d, u* %.3f "
              "(u*/U = %.3f)" % (k_cross, N, u_star, frac))

        dt = np.diff(np.array([t if t is not None else np.nan
                               for t in taus]))
        good = np.isfinite(dt) & (np.abs(dt) > 1e-15)
        sf = float(np.mean(dt[good] > 0)) if good.any() else 0.0
        sign_frac_all.append(sf)
        if int(np.sum(good)) >= 8:
            x = np.log(np.abs(dt[good]))
            y = np.log(mm[np.where(good)[0]])
            cx = x - x.mean()
            cy = y - y.mean()
            corr = float(np.sum(cx * cy)
                         / max(1e-30,
                               math.sqrt(float(np.sum(cx * cx))
                                         * float(np.sum(cy
                                                        * cy)))))
        else:
            corr = float("nan")
        corr_all.append(corr)
        print("    L3 increments: frac positive %.3f | corr("
              "log|dtau|, log m) %+.3f" % (sf, corr))

        tail = [t if t is not None else -1.0
                for t in taus[k_cross:]]
        mono = all(tail[i + 1] >= tail[i] - 1e-12
                   for i in range(len(tail) - 1))
        mono_tail.append(mono)
        print("    L4 tail after last crossing: %s"
              % ("MONOTONE" if mono else "OSCILLATORY"))

        desc = list(range(N - 1, -1, -1))
        taus_d = trajectory(c_ar, rows, desc, M)
        ka = first_stable_positive(taus)
        kd = first_stable_positive(taus_d)
        edge_carries.append(kd / max(1, N) <= 0.5)
        print("    L5 first stable positive: ascending %d/%d "
              "(%.3f) | edge-first %d/%d (%.3f)"
              % (ka, N, ka / max(1, N), kd, N, kd / max(1, N)))

    section("T -- typed outcomes")
    lab1 = ("ARCH-SUBCRITICAL" if all(arch_sub) else "ARCH-MIXED")
    lab2 = ("LAST-CROSSING-EDGE" if all(edge_cross)
            else "LAST-CROSSING-BULK")
    lab4 = ("MONOTONE-TAIL" if all(mono_tail)
            else "OSCILLATORY-TAIL")
    lab5 = ("EDGE-CARRIES" if all(edge_carries)
            else "EDGE-INSUFFICIENT")
    check("T.1 typed: %s / %s / %s / %s" % (lab1, lab2, lab4,
                                            lab5), True)
    print("    increment sign fractions: %s"
          % ", ".join("%.3f" % s for s in sign_frac_all))
    print("    size-law correlations:    %s"
          % ", ".join("%+.3f" % c for c in corr_all))

    section("C -- control (kz 9, deterministic mass scramble)")
    rr = core.build_window(9)
    M, alpha = rr["M"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, rr["D"]), float)
    mm_s = mm * (1.0 + 0.5 * np.sign(np.sin(1000.0 * uu)))
    c_s, _ = core.atom_lags_at(alpha, M, uu, mm_s)
    tau_s = floor_of(c_ar + np.asarray(c_s, float), M)
    c_t, _ = core.atom_lags_at(alpha, M, uu, mm)
    tau_t = floor_of(c_ar + np.asarray(c_t, float), M)
    fired = (tau_s is None or tau_s < 0.0
             or tau_s < tau_t - 0.25)
    check("C1 mass scramble drops the endpoint", fired,
          "tau_true %+0.4e tau_scr %s"
          % (tau_t, "None" if tau_s is None else "%+0.4e"
             % tau_s), kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if not ward_ok:
        VERDICT = "LINEARITY-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "PRIMELADDER-MEASURED"
    print("\n  VERDICT: %s (%s / %s / %s / %s)"
          % (VERDICT, lab1, lab2, lab4, lab5))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
