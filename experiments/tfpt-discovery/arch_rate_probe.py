#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arch_rate_probe -- PRIME.RDAGGER.ARCH_IDENTITY_AND_RATE.01 (r475).

Seals the arch tent rate at fixed f and isolates F1(ii).
Mathlib v4.29.1 still lists Gauss's digamma integral as TODO;
the r464 exact-equality quantifier forces Delta = log a/(m+1)
to grow at fixed mesh.  The correct remnant is O(Delta_k^2)
along the selected sequence for each fixed GridElement.

SCRAMBLE GATE (r469 anti-list item 3).  This probe proposes no
bound on q^dagger.  It measures one native arch tent error
against the classical u-space pairing at unscrambled selected
windows k=5..12 for one frozen test function.  A source scramble
would change the lags; the round does not claim
scramble-invariance.

VERDICT: IDENTITY_ISOLATED + RATE_O_DELTA2.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

import numpy as np
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROB = os.path.join(REPO, "rh", "problem")
for p in (HERE, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import cofinal_family_probe as R458  # noqa: E402
import quadrep_probe as Q  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

mp.dps = 50
PIN_ARCH_CL = 0.2131977998658999
PIN_ERR = {
    5: 0.119793278323,
    6: 0.119793278323,
    7: 0.119793278323,
    8: 0.119793278323,
    9: 0.028876619985,
    10: 0.028876619985,
    11: 0.028876619985,
    12: 0.028876619985,
}
PIN_ERR_OVER_D2_LO = 3.84
PIN_ERR_OVER_D2_HI = 4.00


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")


def read(relative: str) -> str:
    with open(os.path.join(REPO, relative), encoding="utf-8") as handle:
        return handle.read()


def arch_read_window(x, mesh, m, car, Delta):
    d0 = 2.0 ** (-mesh)
    acf = Q.acf_of(x, d0)
    F = lambda u: Q.to_fun(acf, d0, u)
    arch = float(car[0] * F(0.0))
    for i in range(1, m + 1):
        arch += 2.0 * float(car[i] * F(i * Delta))
    return arch


def text_gates() -> None:
    elementwise = read("rh/lean/RH/Elementwise.lean")
    inner = read("rh/lean/RH/InnerBridges.lean")
    digamma = read(
        "rh/lean/.lake/packages/mathlib/Mathlib/Analysis/"
        "SpecialFunctions/Gamma/Digamma.lean"
    )
    check("weil-side-concrete",
          "noncomputable def weilArchSide" in elementwise
          and "opaque weilArchSide" not in elementwise
          and "def weilArchUIntegrand" in elementwise)
    check("gauss-isolated-not-sorry",
          "def GaussDigammaIntegralRepresentation" in elementwise
          and "Prove Gauss' integral representation" in digamma)
    check("exact-identity-unasserted-r638L",
          "def ArchGaussMellinDigammaIdentity" in elementwise
          and "theorem arch_gauss_mellin_digamma_identity" not in elementwise
          and "(hArch : ArchGaussMellinDigammaIdentity)" in elementwise)
    check("delta-blows-at-fixed-mesh",
          "theorem productionArchDelta_tendsto_atTop" in inner
          and "\n  sorry" not in inner)
    check("quadratic-rate-named",
          "def SelectedArchErrorQuadraticRate" in inner
          and "theorem selectedArchError_tendsto_zero_of_rate" in inner)


def numerical_gates() -> None:
    shp5 = R458.lean_shape(5)
    a, m, M, Delta = shp5["a"], shp5["m"], shp5["M"], shp5["D"]
    car = V.arch_lags(M, Delta)
    mask = V.PP <= a * a
    T = Q.hess_full(Q.PIN_STEPS_COVER, Q.PIN_MESHEXP_COVER, m, car, Delta,
                    V.U[mask], V.W_VM[mask])
    ev, evec = np.linalg.eigh(T)
    x = evec[:, 0] / np.linalg.norm(evec[:, 0])
    table = {}
    for k in range(5, 13):
        shp = R458.lean_shape(k)
        aw = arch_read_window(
            x, Q.PIN_MESHEXP_COVER, shp["m"],
            V.arch_lags(shp["M"], shp["D"]), shp["D"])
        err = PIN_ARCH_CL - aw
        table[k] = (shp["D"], err, err / (shp["D"] ** 2))
        print(f"    k={k:2d}  D={shp['D']:.10f}  err={err:.12f}  "
              f"err/D2={err / (shp['D'] ** 2):.4f}")
    check("k5-err-matches-r473",
          abs(table[5][1] - PIN_ERR[5]) < 2e-12,
          f"err5={table[5][1]:.12f}")
    check("table-pins-5-to-12",
          all(abs(table[k][1] - PIN_ERR[k]) < 2e-12 for k in PIN_ERR),
          "8/8 k-pins")
    ratios = [table[k][2] for k in range(5, 13)]
    check("quadratic-ratio-stable",
          all(PIN_ERR_OVER_D2_LO <= r <= PIN_ERR_OVER_D2_HI for r in ratios),
          f"err/D2 in [{min(ratios):.4f},{max(ratios):.4f}]")
    check("error-falls-when-delta-halves",
          table[9][1] < table[5][1] / 3.5
          and abs(table[5][0] / table[9][0] - 2.0) < 1e-12,
          f"err9/err5={table[9][1] / table[5][1]:.4f}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("arch_rate_probe -- r475")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    text_gates()
    numerical_gates()
    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("ARCH RATE PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
