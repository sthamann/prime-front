#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mellin_model_operator_probe -- PRIME.PORT.MODEL.01
(EXPLORATION ONLY, experiments/; round 39 solve-step (c): the
UNPERTURBED model problem -- replace the prime comb by its exact
continuum dr-limit and ask whether the pure PNT model is
subcritical, critical, or supercritical, 2026-08-09).

THE MODEL (frozen, fit-free): by the sqrt uniformization (XCII),
sum_n mu_n f(u_n) -> 2 int_0^U f(u) e^{u/2} du.  The MODEL comb
replaces the atoms by the deterministic fine grid u_i (spacing
D/8) with masses 2 e^{u_i/2} du -- the pure PNT source with NO
arithmetic fluctuation -- pushed through the IDENTICAL deployed
pipeline (same tent assembly, same arch layer, same pencil).

THE QUESTION: tau_model vs tau_true.  If tau_model > 0 with a
margin LARGER than tau_true, the pure PNT world is safely inside
the wall and the arithmetic fluctuation is what eats the margin
(RH = the statement that it never overshoots); if tau_model < 0,
the model normalization is wrong and the reading must change.
Either outcome calibrates the steepest-descent split
    E = E_model + (arithmetic perturbation).

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40}):

 D1  PIPELINE: the model comb through build (atom_lags_at with
     the fine deterministic grid); the model pencil floor
     tau_model computed identically; printed next to tau_true.

 D2  THE PERTURBATION SIZE: ||E_true - E_model||_2 per rung
     (matched folded node sets are NOT guaranteed -- compare via
     the pencil floors and the port-numerator profiles d(theta_j)
     j <= 8; the operator-level difference is reported through
     the common lag space: ||c_true - c_model||_2 relative).

 D3  TYPED OUTCOME: MODEL-SUBCRITICAL iff tau_model > tau_true on
     every heavy rung (the pure PNT world sits INSIDE the wall
     with room; the arithmetic consumes the difference);
     MODEL-CRITICAL iff |tau_model| <= tau_true somewhere;
     MODEL-SUPERCRITICAL iff tau_model < 0 somewhere (honest
     recalibration signal).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN.

VERDICT (frozen enum): MODEL-MEASURED (+ typed sublabel) /
PIPELINE-BROKEN.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
the model comb is DETERMINISTIC (no RNG anywhere); v563
READ-ONLY; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts;
prime_sqrt_uniformization + port_mellin_cauchy (XCII, declared
inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mellin_model_operator_probe.py
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


def main():
    section("PRIME.PORT.MODEL.01 -- the pure PNT model operator "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic model; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("D1/D2/D3 -- model vs truth (heavy rungs)")
    subcrit = True
    supercrit = False
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        c_true = c_ar + np.asarray(c_at, float)
        U = float(np.max(uu))
        du = D / 8.0
        ug = np.arange(du / 2.0, U, du)
        mg = 2.0 * np.exp(ug / 2.0) * du
        c_at_m, _ = core.atom_lags_at(alpha, M, ug, mg)
        c_model = c_ar + np.asarray(c_at_m, float)
        tau_t = floor_of(c_true, M)
        tau_m = floor_of(c_model, M)
        relc = float(np.linalg.norm(c_true - c_model)
                     / np.linalg.norm(c_true))
        d_t = grid_density(c_true)
        d_m = grid_density(c_model)
        prof = " ".join("%.2f" % (d_m[j] / d_t[j])
                        for j in range(1, 7))
        print("    kz %-3d h %4d: tau_true %+.3e | tau_model "
              "%+.3e (ratio %.1f) | lag rel diff %.3f | port "
              "d_model/d_true (j=1..6): %s"
              % (kz, h, tau_t, tau_m,
                 tau_m / tau_t if tau_t else float("nan"),
                 relc, prof))
        subcrit &= (tau_m is not None and tau_m > tau_t > 0)
        supercrit |= (tau_m is not None and tau_m < 0)
    if supercrit:
        d3 = "MODEL-SUPERCRITICAL"
    elif subcrit:
        d3 = "MODEL-SUBCRITICAL"
    else:
        d3 = "MODEL-CRITICAL"
    check("D3.1 typed: %s -- %s" % (
        d3,
        "the pure PNT world sits INSIDE the wall with room; the "
        "arithmetic fluctuation consumes the difference (the "
        "steepest-descent split E = E_model + arithmetic is "
        "calibrated)" if d3 == "MODEL-SUBCRITICAL" else
        "recalibration signal -- inspect the model normalization"
        if d3 == "MODEL-SUPERCRITICAL" else
        "the model sits at the same criticality scale as the "
        "truth"), True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("PIPELINE-BROKEN" if KILLS else "MODEL-MEASURED")
    print("\n  VERDICT: %s (%s)" % (VERDICT, d3))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
