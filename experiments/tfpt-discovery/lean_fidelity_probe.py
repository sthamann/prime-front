#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lean_fidelity_probe -- PRIME.RDAGGER.LEAN_FIDELITY_REPAIR.01 (r463).

Independent numerical mirror of RH/FaithfulFold.lean, compared with
the production FFT builder at k=5,9,10.  The Lean real functions are
not executable (`Real.log`/`Real.cos`), so these exported values pin
the transcription.  No `native_decide` or sampled theorem is used.

VERDICT: FAITHFUL_OBJECT_PINNED / BRIDGES_TYPED / CENSUS_8.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import cofinal_family_probe as R458  # noqa: E402
import fullcomb_cleanup_probe as R459  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SAMPLE_K = (5, 9, 10)
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
PINS = {
    5: (198, 19, 10, 1.036602206605489, -0.7258976122862184,
        0.6049435070777798, 1.0302838374773637),
    9: (23150, 71, 36, 1.9073651794520652, -1.156832914821134,
        1.0648361775435493, 1.7238843999790427),
    10: (82267, 79, 40, 1.912109514622476, -1.1523609272942765,
         1.0306623671323438, 1.7238843999790432),
}
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:35s} {detail}")


def faithful_transcription(rows: list[tuple[int, float]], k: int) -> dict[str, float]:
    """Evaluate the formulas transcribed in RH/FaithfulFold.lean."""
    shape = R458.lean_shape(k)
    a, m, M, L, delta = (
        shape["a"], shape["m"], shape["M"], shape["L"], shape["D"]
    )
    c_prime = np.zeros(M)
    atoms = 0
    for n, logp in rows:
        if n > a * a:
            break
        atoms += 1
        u = math.log(n)
        mass = 2.0 * logp / math.sqrt(n)
        for i in range(M):
            ordinary = max(0.0, 1.0 - abs(i * delta - u) / delta)
            reflected = max(0.0, 1.0 - abs(i * delta + u) / delta)
            c_prime[i] -= 0.5 * mass * (ordinary + reflected)

    c = V.arch_lags(M, delta) + c_prime
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    density = np.asarray([
        c[0]
        + 2.0 * sum(c[r] * math.cos(r * th) for r in range(1, M - 1))
        + c[M - 1] * math.cos((M - 1) * th)
        for th in theta
    ])
    weights = (2.0 / L) * (1.0 - np.cos(theta)) * density
    weights[-1] *= 0.5
    positive = weights > 0.0
    x_pos, w_pos = np.cos(theta)[positive], weights[positive]
    return {
        "atoms": atoms,
        "support": len(weights),
        "cap": (len(weights) + 1) // 2,
        "mu_h00": float(np.sum(w_pos)),
        "mu_h01": float(np.sum(w_pos * x_pos)),
        "mu_h11": float(np.sum(w_pos * x_pos**2)),
        "signed_h00": float(np.sum(weights)),
        "density_fft_error": float(np.max(np.abs(density - V.spectral_density(c)[jj]))),
    }


def production_builder(rows: list[tuple[int, float]], k: int) -> dict[str, float]:
    shape = R458.lean_shape(k)
    c_prime, atoms = R459.lags_from_rows(
        rows, shape["alpha"], shape["M"], shape["D"]
    )
    main, _ = R459.mz_pair(
        c_prime, atoms, shape["alpha"], shape["M"], shape["L"],
        shape["Nw"], shape["D"]
    )
    signed = np.concatenate((main["wp"], -np.asarray(main["vn"])))
    return {
        "atoms": atoms,
        "support": len(main["xp"]) + len(main["yn"]),
        "cap": (len(main["xp"]) + len(main["yn"]) + 1) // 2,
        "mu_h00": float(np.sum(main["wp"])),
        "mu_h01": float(np.sum(main["wp"] * main["xp"])),
        "mu_h11": float(np.sum(main["wp"] * main["xp"]**2)),
        "signed_h00": float(np.sum(signed)),
    }


def text_gates() -> None:
    faithful = open(os.path.join(REPO, "rh/lean/RH/FaithfulFold.lean"),
                    encoding="utf-8").read()
    selected = open(os.path.join(REPO, "rh/lean/RH/Selected.lean"),
                    encoding="utf-8").read()
    frequent = open(os.path.join(REPO, "rh/lean/RH/FrequentlySelected.lean"),
                    encoding="utf-8").read()
    external = open(os.path.join(REPO, "rh/lean/RH/ExternalBridges.lean"),
                    encoding="utf-8").read()
    check("L=2M-2", "2 * productionM m - 2" in faithful)
    check("spectral-density-transcribed", "def exactSpectralDensity" in faithful)
    check("sign-split-transcribed", "def exactPositiveFoldWeight" in faithful
          and "def exactNegativeFoldWeight" in faithful)
    check("selected-uses-production-fold", "productionFold a m" in selected)
    check("honest-compound-mincut", "def FrequentlySelectedInternalMincut" in frequent)
    check("internal-endpoint-renamed",
          "theorem internal_weil_nonneg_of_frequently_selected" in frequent
          and re.search(r"^theorem rh_of_frequently_selected\b",
                        frequent, re.MULTILINE) is None)
    check("r638L-one-external-brick", external.count("\n  sorry") == 1
          and "theorem grid_dense_extension : GridDenseExtension :=" in external
          and "fullWeil_fixedSupport_completion" in external
          and "def StandardExplicitFormulaIdentification" in external
          and "theorem standard_explicit_formula_identification :" not in external
          and "standard_weil_criterion_to_mathlib_rh_of_separation" in external)
    check("mathlib-rh-interface", "RiemannHypothesis" in external
          and "Mathlib.NumberTheory.LSeries.RiemannZeta" in external)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("lean_fidelity_probe -- r463")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    text_gates()
    rows = R459.sieve_pp(1_100_000)
    for k in SAMPLE_K:
        lean = faithful_transcription(rows, k)
        prod = production_builder(rows, k)
        pin = PINS[k]
        values = ("atoms", "support", "cap", "mu_h00", "mu_h01",
                  "mu_h11", "signed_h00")
        agree = all(
            lean[key] == prod[key] if key in {"atoms", "support", "cap"}
            else abs(lean[key] - prod[key]) < 2e-12
            for key in values
        )
        pinned = all(
            lean[key] == pin[i] if key in {"atoms", "support", "cap"}
            else abs(lean[key] - pin[i]) < 2e-12
            for i, key in enumerate(values)
        )
        check(f"k{k}-lean-vs-python", agree and pinned
              and lean["density_fft_error"] < 2e-12,
              f"atoms/S/cap={lean['atoms']}/{lean['support']}/{lean['cap']} "
              f"H=[{lean['mu_h00']:.12g},{lean['mu_h01']:.12g},"
              f"{lean['mu_h11']:.12g}]")
    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("LEAN FIDELITY VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
