#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gapmap_probe -- PRIME.RDAGGER.ENDTOEND_GAPMAP.01 (round 462).

Adversarial source and proof-path audit of the claimed
FrequentlySelected -> RH route.  The probe compares the literal Lean
`ExactPrimeSource`/`ExactFold`/`combHankel` object with the production
Python builder at k=5,9,10 and checks the declarations on the minimal
path.  Research documentation.  NO RH claim.  NO anti-RH claim.

VERDICT: HIDDEN_GAP_FOUND.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import cofinal_family_probe as R458  # noqa: E402
import fullcomb_cleanup_probe as R459  # noqa: E402

SELECTED = os.path.join(REPO, "rh", "lean", "RH", "Selected.lean")
FREQUENT = os.path.join(REPO, "rh", "lean", "RH", "FrequentlySelected.lean")
ELEMENTWISE = os.path.join(REPO, "rh", "lean", "RH", "Elementwise.lean")

VERDICT = "HIDDEN_GAP_FOUND"
SAMPLE_K = (5, 9, 10)
CHECKS: list[tuple[str, bool]] = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:34s} {detail}", flush=True)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def lean_literal_rows(rows: list[tuple[int, float]], k: int) -> dict[str, float]:
    """Evaluate the literal Lean comb channel before opaque completion.

    For `a=2^k`, `exactFoldMap` simplifies to
    `cos(pi*log(n)/log(a))`.  Aggregation preserves moment sums, so raw
    rows evaluate `combHankel` exactly up to floating evaluation.
    The only exact prime-power fold collisions are
    `2^r <-> 2^(2k-r)`, hence `k-1` merged duplicates.
    """
    a = 2**k
    source = [(n, lam) for n, lam in rows if n <= a * a]
    atom_count = len(source)
    support = atom_count - (k - 1)
    cap = (support + 1) // 2
    log_anchor = math.log(a)
    nodes = np.asarray(
        [math.cos(math.pi * math.log(n) / log_anchor) for n, _ in source]
    )
    weights = np.asarray([lam for _, lam in source])
    moments = [float(np.sum(weights * nodes**degree)) for degree in range(3)]
    return {
        "atom_count": atom_count,
        "support": support,
        "cap": cap,
        "h00": moments[0],
        "h01": moments[1],
        "h11": moments[2],
    }


def python_builder_rows(rows: list[tuple[int, float]], k: int) -> dict[str, float]:
    """Evaluate the production lag/spectral-density/fold builder."""
    shape = R458.lean_shape(k)
    prime_lags, atom_count = R459.lags_from_rows(
        rows, shape["alpha"], shape["M"], shape["D"]
    )
    main, _arch = R459.mz_pair(
        prime_lags,
        atom_count,
        shape["alpha"],
        shape["M"],
        shape["L"],
        shape["Nw"],
        shape["D"],
    )
    nodes = np.concatenate([np.asarray(main["xp"]), np.asarray(main["yn"])])
    signed = np.concatenate([np.asarray(main["wp"]), -np.asarray(main["vn"])])
    mu_nodes = np.asarray(main["xp"])
    mu_weights = np.asarray(main["wp"])
    return {
        "atom_count": atom_count,
        "support": len(nodes),
        "cap": (len(nodes) + 1) // 2,
        "declared_nw": shape["Nw"],
        "mu_h00": float(np.sum(mu_weights)),
        "mu_h01": float(np.sum(mu_weights * mu_nodes)),
        "mu_h11": float(np.sum(mu_weights * mu_nodes**2)),
        "signed_h00": float(np.sum(signed)),
    }


def lean_text_audit() -> None:
    selected = read(SELECTED)
    frequent = read(FREQUENT)
    elementwise = read(ELEMENTWISE)
    print("\nLEAN PATH TEXT AUDIT")
    gates = {
        "fold-L-is-2mplus2": "let L : ℝ := 2 * (m + 1 : ℝ)" in selected,
        "python-L-is-not-transcribed": "2 * (m + 1 : ℝ) - 2" not in selected,
        "fold-passes-border-through": "(ExactFold a m ha).u = ExactBorder a m"
        in selected,
        "named-read-bridge": "def SelectedACapPsdImpliesPlainReads : Prop"
        in frequent,
        "arch-sorry": "theorem arch_elementwise_stabilization" in elementwise
        and "\n  sorry" in elementwise,
        "custom-weil-form": "noncomputable def weilForm" in elementwise,
        "no-zeta-interface": "RiemannHypothesis" not in frequent
        and "riemannHypothesis" not in frequent
        and "Complex.zeta" not in frequent,
        "spectral-side-disclaimed":
        "spectral/zero side of the explicit\nformula is not formalized" in frequent,
    }
    for name, ok in gates.items():
        check(name, ok)


def source_audit() -> None:
    print("\nSOURCE FIDELITY: ExactFold/combHankel vs production builder")
    rows = R459.sieve_pp(1_100_000)
    for k in SAMPLE_K:
        lean = lean_literal_rows(rows, k)
        python = python_builder_rows(rows, k)
        complete = lean["atom_count"] == python["atom_count"]
        support_mismatch = lean["support"] != python["support"]
        cap_mismatch = lean["cap"] != python["cap"]
        print(
            "  k=%d a=%d atoms=%d | Lean S/cap=%d/%d | Python S/cap=%d/%d "
            "(declared Nw=%d)"
            % (
                k,
                2**k,
                lean["atom_count"],
                lean["support"],
                lean["cap"],
                python["support"],
                python["cap"],
                python["declared_nw"],
            )
        )
        print(
            "    combHankel Lean [H00,H01,H11]=[%.9g, %.9g, %.9g]"
            % (lean["h00"], lean["h01"], lean["h11"])
        )
        print(
            "    production mu [H00,H01,H11]=[%.9g, %.9g, %.9g], "
            "signed H00=%.9g"
            % (
                python["mu_h00"],
                python["mu_h01"],
                python["mu_h11"],
                python["signed_h00"],
            )
        )
        check(
            f"k{k}-inventory-complete",
            complete,
            f"both enumerate {lean['atom_count']} prime powers through a^2",
        )
        check(
            f"k{k}-object-mismatch-detected",
            support_mismatch and cap_mismatch,
            f"cap ratio={lean['cap'] / python['cap']:.1f}",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("gapmap_probe -- PRIME.RDAGGER.ENDTOEND_GAPMAP.01 (round 462)")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    lean_text_audit()
    source_audit()
    all_previous = all(ok for _, ok in CHECKS)
    check("verdict", all_previous and VERDICT == "HIDDEN_GAP_FOUND", VERDICT)
    failed = [name for name, ok in CHECKS if not ok]
    print(f"\nRESULT: {len(CHECKS) - len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("GAPMAP VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
