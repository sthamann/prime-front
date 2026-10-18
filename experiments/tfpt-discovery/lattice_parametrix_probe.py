#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lattice_parametrix_probe -- PRIME.PORT.LATTICE.PARAMETRIX.01
(EXPLORATION ONLY, experiments/; round 40, work package 2 of the
closing-cylinder plan: WHICH part of the prime discreteness must
live in the Riemann-Hilbert main parametrix?, 2026-08-09).

CONTEXT: the smooth continuum dr-model VIOLATES the floor
(MODEL-SUPERCRITICAL, tau_model = -1.26 -> -0.11): the prime
discreteness rescues positivity.  But 'discreteness' has two
separable parts: (P) the POSITIONS (the prime-power lattice
{log n}) and (M) the MASSES (the actual Lambda(n) values with
their fluctuations).  The parametrix design question: does the
main problem need only the lattice with SMOOTH masses (then the
Lambda-fluctuations are the perturbative remainder -- the ideal
case), or the actual masses too?

THE THREE-PLUS-ONE WORLDS (frozen; identical pipeline, pencil
floor tau for each):
  A   TRUE:      masses 2 Lambda(n)/sqrt(n) at u_n = log n
                 (tau_A > 0, known);
  B1  LATTICE-SMOOTH: prime-power positions, fully smooth
                 quadrature masses m_n = 2 e^{u_n/2} du_n
                 (midpoint cells) -- NO Lambda information at all;
  B2  LOCAL-AVERAGE: B1 masses rescaled per +-1/2 log-unit window
                 to preserve the TRUE local mass sums -- kills
                 in-window Lambda fluctuations, keeps local PNT
                 mass exactly;
  C   CONTINUUM: fine D/8 grid (tau_C < 0, known -- re-warded).

TYPED OUTCOMES (the deliverable):
  LATTICE-SUFFICIENT      iff tau_B1 > 0 on every heavy rung
    (the parametrix = Mellin-Cauchy + bare prime-power lattice;
    Lambda entirely perturbative -- the ideal case);
  LOCAL-MASS-REQUIRED     iff tau_B1 < 0 somewhere but tau_B2 > 0
    everywhere (the parametrix needs the local PNT mass on the
    lattice; only in-window fluctuations perturbative);
  FLUCTUATIONS-REQUIRED   iff tau_B2 < 0 somewhere (the actual
    Lambda values are load-bearing -- the parametrix must carry
    them; the remainder split must be finer).

 C1  CONTROLS/WARDS: tau_A > 0 and tau_C < 0 re-warded on every
     heavy rung (the two known anchors of the dichotomy).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 an anchor ward
fails -> ANCHOR-BROKEN.

VERDICT (frozen enum): PARAMETRIX-MEASURED (+ typed outcome) /
PIPELINE-BROKEN / ANCHOR-BROKEN.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan; the
worlds are built from the deployed tables and deterministic
transforms); v563 READ-ONLY; no RNG; stdout only.

Sources (read-only): v563_paper2_readouts; mellin_model_operator
probe (round 39, the continuum anchor), v882 (source law).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/lattice_parametrix_probe.py
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


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def main():
    section("PRIME.PORT.LATTICE.PARAMETRIX.01 -- which "
            "discreteness must the parametrix carry? "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic worlds; no marker "
          "moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("W -- the four worlds (heavy rungs)")
    okA = okC = True
    b1_signs, b2_signs = [], []
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_ar = np.asarray(core.arch_lags(M, D), float)

        def tau_of(pos, mass):
            c_at, _ = core.atom_lags_at(alpha, M, pos, mass)
            return floor_of(c_ar + np.asarray(c_at, float), M)

        tau_A = tau_of(uu, mm)
        du = cell_widths(uu)
        m_b1 = 2.0 * np.exp(uu / 2.0) * du
        tau_B1 = tau_of(uu, m_b1)
        # B2: rescale B1 masses to preserve true local sums
        m_b2 = m_b1.copy()
        for i in range(len(uu)):
            w = np.abs(uu - uu[i]) <= 0.5
            s_true = float(np.sum(mm[w]))
            s_b1 = float(np.sum(m_b1[w]))
            m_b2[i] = m_b1[i] * (s_true / s_b1 if s_b1 > 0
                                 else 1.0)
        tau_B2 = tau_of(uu, m_b2)
        U = float(np.max(uu))
        dug = D / 8.0
        ug = np.arange(dug / 2.0, U, dug)
        tau_C = tau_of(ug, 2.0 * np.exp(ug / 2.0) * dug)
        okA &= (tau_A is not None and tau_A > 0)
        okC &= (tau_C is not None and tau_C < 0)
        b1_signs.append(tau_B1)
        b2_signs.append(tau_B2)
        print("    kz %-3d h %4d: tau_A %+0.3e | tau_B1(lattice-"
              "smooth) %+0.3e | tau_B2(local-avg) %+0.3e | tau_C"
              "(continuum) %+0.3e"
              % (kz, h, tau_A, tau_B1, tau_B2, tau_C))
    check("C1 ANCHOR WARDS: tau_A > 0 and tau_C < 0 on every "
          "heavy rung", okA and okC, kill="K2")
    if all(t is not None and t > 0 for t in b1_signs):
        outcome = "LATTICE-SUFFICIENT"
    elif all(t is not None and t > 0 for t in b2_signs):
        outcome = "LOCAL-MASS-REQUIRED"
    else:
        outcome = "FLUCTUATIONS-REQUIRED"
    check("W.1 typed: %s -- %s"
          % (outcome,
             "the parametrix = Mellin-Cauchy + bare prime-power "
             "lattice; Lambda entirely perturbative (ideal case)"
             if outcome == "LATTICE-SUFFICIENT" else
             "the parametrix needs the local PNT mass on the "
             "lattice; in-window fluctuations perturbative"
             if outcome == "LOCAL-MASS-REQUIRED" else
             "the actual Lambda values are load-bearing; the "
             "remainder split must be finer than mass-smoothing"),
          True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("ANCHOR-BROKEN" if KILLS else
               "PARAMETRIX-MEASURED")
    print("\n  VERDICT: %s (%s)" % (VERDICT, outcome))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
