#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""inner_bridges_probe -- PRIME.RDAGGER.INNER_BRIDGES.01 (r464).

Pins the productive Archimedean lag transcription at k=5,9,10 and
audits the exact finite-PSD/channel split.  The numerical values are
diagnostic pins for the Lean definitions, not sampled proofs.

VERDICT: FINITE_PSD_CLOSED / ARCH_LAGS_TRANSCRIBED / TWO_NAMED_REMAINDERS.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import cofinal_family_probe as R458  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SAMPLE_K = (5, 9, 10)
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
PINS = {
    5: (0.294628394551426, -0.735655442925938,
        -0.033473428435046304, -2.169368995630352),
    9: (1.0092563972652342, -0.7146280027138086,
        -0.003999307221655523, -2.0911325718759217),
    10: (1.0092563972652342, -0.7146280027138086,
         -0.00282792759867232, -2.1175899313202695),
}
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")


def read(relative: str) -> str:
    with open(os.path.join(REPO, relative), encoding="utf-8") as handle:
        return handle.read()


def text_gates() -> None:
    elementwise = read("rh/lean/RH/Elementwise.lean")
    inner = read("rh/lean/RH/InnerBridges.lean")
    frequent = read("rh/lean/RH/FrequentlySelected.lean")
    digamma = read(
        "rh/lean/.lake/packages/mathlib/Mathlib/Analysis/"
        "SpecialFunctions/Gamma/Digamma.lean"
    )
    check("arch-lag-not-opaque",
          "noncomputable def productionArchLag" in elementwise
          and "opaque productionArchLag" not in elementwise)
    check("near-cell-transcribed",
          "def productionArchLagNear" in elementwise
          and "Real.eulerMascheroniConstant" in elementwise)
    check("far-cell-transcribed",
          "def productionArchLagFar" in elementwise
          and "productionArchFarIntegrand" in elementwise)
    check("arch-contract-unasserted-r638L",
          "def ArchGaussMellinDigammaIdentity" in elementwise
          and "theorem arch_gauss_mellin_digamma_identity" not in elementwise
          and "theorem arch_elementwise_stabilization" in elementwise
          and "(hArch : ArchGaussMellinDigammaIdentity)" in elementwise)
    check("mathlib-gauss-integral-todo",
          "Prove Gauss' integral representation" in digamma)
    check("finite-psd-lemma-proved",
          "theorem selectedACapPsdImpliesPlainReads_of_representation" in inner
          and "dotProduct_mulVec_nonneg" in inner
          and "\n  sorry" not in inner)
    check("channel-remainder-named",
          "def SelectedReadQuadraticRepresentation" in inner
          and "SelectedReadQuadraticRepresentation" in frequent)


def numerical_gates() -> None:
    for k in SAMPLE_K:
        shape = R458.lean_shape(k)
        coeffs = V.arch_lags(shape["M"], shape["D"])
        observed = (
            float(coeffs[0]), float(coeffs[1]),
            float(coeffs[-1]), float(np.sum(coeffs)),
        )
        pin_ok = all(abs(x - y) < 2e-12 for x, y in zip(observed, PINS[k]))
        near_far_ok = (
            abs(coeffs[0] - V.arch_A_near(0.0, shape["D"])) < 2e-12
            and abs(coeffs[1] - V.arch_A_far(
                np.asarray([shape["D"]]), shape["D"])[0]) < 2e-12
        )
        check(f"k{k}-arch-lag-pin", pin_ok and near_far_ok,
              f"c0/c1/last/sum="
              f"{observed[0]:.12g}/{observed[1]:.12g}/"
              f"{observed[2]:.12g}/{observed[3]:.12g}")

    # The old bridge quantifies only meshExp <= selectedMesh.  It does
    # not bound GridElement.steps, while A_cap is finite-dimensional.
    # This arithmetic witness records the quantifier mismatch without
    # pretending to be a counterexample to RH or to fullRead positivity.
    shape = R458.lean_shape(5)
    cap = (shape["m"] + 1) // 2
    mesh_exp = shape["m"]
    steps = cap + 1
    check("unbounded-steps-witness",
          mesh_exp <= shape["m"] and steps > cap,
          f"k=5 meshExp={mesh_exp} steps={steps} cap={cap}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("inner_bridges_probe -- r464")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    text_gates()
    numerical_gates()
    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("INNER BRIDGES PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
