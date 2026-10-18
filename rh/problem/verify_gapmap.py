#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify the numbered claims in endtoend_gapmap.tex (round 462).

Exit line: GAPMAP VERIFIED.  Research documentation; NO RH CLAIM.
"""
from __future__ import annotations

import hashlib
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import gapmap_probe as GAP  # noqa: E402

LEAN = os.path.join(REPO, "rh", "lean", "RH")
INVENTORY = os.path.join(REPO, "rh", "INVENTORY.json")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{' -- ' + detail if detail else ''}")


def text(name: str) -> str:
    with open(os.path.join(LEAN, name), encoding="utf-8") as handle:
        return handle.read()


def digest(path: str) -> str:
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def verify_path() -> None:
    frequent = text("FrequentlySelected.lean")
    elementwise = text("Elementwise.lean")
    selected = text("Selected.lean")
    check(
        "G1-mincut-is-hypothesis",
        "def frequently_selected_augDualResolvent_ge_half : Prop" in frequent,
    )
    check(
        "G2-read-bridge-is-hypothesis",
        "def SelectedACapPsdImpliesPlainReads : Prop" in frequent,
    )
    check(
        "G3-conclusion-is-custom-form",
        re.search(
            r"theorem rh_of_frequently_selected[\s\S]*?"
            r"∀ f : GridElement, 0 ≤ weilForm f",
            frequent,
        )
        is not None,
    )
    check(
        "G4-no-zeta-interface",
        all(token not in frequent for token in ("Complex.zeta", "RiemannHypothesis")),
    )
    check(
        "G5-spectral-side-absent",
        "spectral/zero side of the explicit\nformula is not formalized" in frequent,
    )
    check(
        "G6-arch-sorry-on-path",
        re.search(
            r"theorem arch_elementwise_stabilization[\s\S]*?^\s+sorry\s*$",
            elementwise,
            re.MULTILINE,
        )
        is not None,
    )
    check(
        "G7-exactfold-grid-mismatch",
        "let L : ℝ := 2 * (m + 1 : ℝ)" in selected
        and "2 * (m + 1 : ℝ) - 2" not in selected,
    )


def verify_sorry_census() -> None:
    declarations: list[tuple[str, int]] = []
    for entry in sorted(os.listdir(LEAN)):
        if not entry.endswith(".lean"):
            continue
        source = text(entry)
        for match in re.finditer(r"(?m)^\s+sorry\s*$", source):
            declarations.append((entry, source.count("\n", 0, match.start()) + 1))
    expected = {
        ("Canonical.lean", 264),
        ("Canonical.lean", 273),
        ("Canonical.lean", 396),
        ("Elementwise.lean", 697),
        ("Source.lean", 1008),
    }
    check(
        "G8-five-sorries",
        len(declarations) == 5,
        ", ".join(f"{name}:{line}" for name, line in declarations),
    )
    check("G9-sorry-locations", set(declarations) == expected)


def verify_numeric_samples() -> None:
    rows = GAP.R459.sieve_pp(1_100_000)
    expected = {
        5: (194, 97, 19, 10),
        9: (23142, 11571, 71, 36),
        10: (82258, 41129, 79, 40),
    }
    for k, pin in expected.items():
        lean = GAP.lean_literal_rows(rows, k)
        python = GAP.python_builder_rows(rows, k)
        got = (
            int(lean["support"]),
            int(lean["cap"]),
            int(python["support"]),
            int(python["cap"]),
        )
        check(f"G{10 + k}-source-k{k}", got == pin, f"{got}")


def main() -> int:
    print("verify_gapmap.py -- round 462")
    before = digest(INVENTORY)
    verify_path()
    verify_sorry_census()
    verify_numeric_samples()
    after = digest(INVENTORY)
    check("G20-inventory-byte-identical", before == after, before[:16])
    check("G21-verdict", GAP.VERDICT == "HIDDEN_GAP_FOUND", GAP.VERDICT)
    failed = [name for name, ok in CHECKS if not ok]
    print(f"\nRESULT: {len(CHECKS) - len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("GAPMAP VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
