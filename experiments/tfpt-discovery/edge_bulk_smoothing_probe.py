#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_bulk_smoothing_probe -- PRIME.PORT.LATTICE.PARAMETRIX.02
(EXPLORATION ONLY, experiments/; round 40, work package 4: WHERE
are the Lambda fluctuations load-bearing -- the edge zone (last
log unit, 39 percent of the mass) or the interior?, 2026-08-09).

CONTEXT: lattice_parametrix_probe (XCVI) decided FLUCTUATIONS-
REQUIRED with GLOBAL mass smoothing.  This refinement smooths
ZONE-WISE (B2-style local-average masses preserving +-1/2
log-unit sums, the mildest smoothing that kills fluctuations):
  A    TRUE comb                          (tau_A > 0, ward);
  Z1   edge-only smoothing  (u > U - 1)   -- interior exact;
  Z2   interior-only smoothing (u <= U-1) -- edge exact;
  Z3   GLOBAL smoothing                   (= XCVI B2, ward < 0).

TYPED OUTCOMES: EDGE-CARRIES iff Z1 breaks (tau < 0) while Z2
survives on every heavy rung (the non-perturbative core is the
last log unit -- a massive simplification of the parametrix);
INTERIOR-CARRIES iff the reverse; BOTH-REQUIRED iff both break;
NEITHER (both survive) would contradict XCVI and fire a kill.

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 ward fails
(tau_A <= 0 or Z3 >= 0 somewhere) -> ANCHOR-BROKEN; K3 both
zones survive -> XCVI-CONTRADICTION.

VERDICT (frozen enum): ZONES-MEASURED (+ typed outcome) /
PIPELINE-BROKEN / ANCHOR-BROKEN / XCVI-CONTRADICTION.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
deterministic transforms of the deployed tables; v563 READ-ONLY;
no RNG; stdout only.

Sources (read-only): v563_paper2_readouts;
lattice_parametrix_probe (XCVI, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/edge_bulk_smoothing_probe.py
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


def smoothed_masses(uu, mm, zone_mask):
    """B2-style local-average masses inside the zone, exact
    outside: quadrature shape rescaled to preserve +-1/2 log-unit
    TRUE mass sums, applied only where zone_mask holds."""
    du = cell_widths(uu)
    m_shape = 2.0 * np.exp(uu / 2.0) * du
    out = mm.copy()
    for i in np.where(zone_mask)[0]:
        w = (np.abs(uu - uu[i]) <= 0.5) & zone_mask
        s_true = float(np.sum(mm[w]))
        s_shape = float(np.sum(m_shape[w]))
        out[i] = m_shape[i] * (s_true / s_shape
                               if s_shape > 0 else 1.0)
    return out


def main():
    section("PRIME.PORT.LATTICE.PARAMETRIX.02 -- edge vs bulk "
            "smoothing (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("Z -- the zone worlds (heavy rungs)")
    okA = okZ3 = True
    z1_all, z2_all = [], []
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        U = float(np.max(uu))

        def tau_of(mass):
            c_at, _ = core.atom_lags_at(alpha, M, uu, mass)
            return floor_of(c_ar + np.asarray(c_at, float), M)

        edge = uu > U - 1.0
        tau_A = tau_of(mm)
        tau_Z1 = tau_of(smoothed_masses(uu, mm, edge))
        tau_Z2 = tau_of(smoothed_masses(uu, mm, ~edge))
        tau_Z3 = tau_of(smoothed_masses(
            uu, mm, np.ones(len(uu), bool)))
        okA &= (tau_A is not None and tau_A > 0)
        okZ3 &= (tau_Z3 is not None and tau_Z3 < 0)
        z1_all.append(tau_Z1)
        z2_all.append(tau_Z2)
        print("    kz %-3d h %4d (edge mass %.2f): tau_A %+0.3e "
              "| Z1 edge-smoothed %+0.3e | Z2 interior-smoothed "
              "%+0.3e | Z3 global %+0.3e"
              % (kz, h, float(np.sum(mm[edge]) / np.sum(mm)),
                 tau_A, tau_Z1, tau_Z2, tau_Z3))
    check("C1 ANCHOR WARDS: tau_A > 0 and tau_Z3 < 0 on every "
          "heavy rung", okA and okZ3, kill="K2")
    z1_pos = all(t is not None and t > 0 for t in z1_all)
    z2_pos = all(t is not None and t > 0 for t in z2_all)
    if z1_pos and z2_pos:
        outcome = "XCVI-CONTRADICTION"
    elif (not z1_pos) and z2_pos:
        outcome = "EDGE-CARRIES"
    elif z1_pos and (not z2_pos):
        outcome = "INTERIOR-CARRIES"
    else:
        outcome = "BOTH-REQUIRED"
    check("Z.1 typed: %s -- %s"
          % (outcome,
             "the non-perturbative core is the LAST LOG UNIT; "
             "interior Lambda fluctuations are perturbative (a "
             "massive parametrix simplification)"
             if outcome == "EDGE-CARRIES" else
             "the interior carries; the edge is perturbative"
             if outcome == "INTERIOR-CARRIES" else
             "both zones' fluctuations are load-bearing -- the "
             "Euler-product pairing is globally rigid"
             if outcome == "BOTH-REQUIRED" else
             "inspect: contradicts XCVI"),
          outcome != "XCVI-CONTRADICTION", kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN", "K2": "ANCHOR-BROKEN",
                   "K3": "XCVI-CONTRADICTION"}[KILLS[0]]
    else:
        VERDICT = "ZONES-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, outcome))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
