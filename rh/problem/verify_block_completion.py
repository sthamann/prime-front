#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_block_completion.py -- machine check of
rh/problem/block_completion.tex (round 484,
PRIME.RDAGGER.BLOCK_COMPLETION.01,
STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, leftover and garbage-jet pins.

Exit: "BLOCK_COMPLETION VERIFIED -- STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import block_completion_probe as B  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72, flush=True)


def part_a() -> None:
    section("PART A  NOTE / TYPE")
    path = os.path.join(REPO, "rh", "problem", "block_completion.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "garbage",
        "QR",
        "leftover",
        "Fourier--HS",
        "not reused",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          B.SCRAMBLE_SENSITIVE is True
          and "log n" in B.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          B.VERDICT_KIND.startswith("STUCK")
          and "20x-drop-falsified" in B.VERDICT_KIND,
          B.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = B.run(True)
    check("G10-smoke", rc == 0, "block_completion_probe --smoke")
    check("G11-pins",
          float(B.N96_LEFT20_PIN) > 50.0 * float(B.BUDGET_PIN)
          and float(B.R483_LEFT_PIN) > 0.02,
          "n=96 leftover over budget; r483 leftover not a pad")
    check("G12-garbage",
          "jets>=10-garbage" in B.VERDICT_KIND,
          "garbage criterion is part of the type")


def main() -> int:
    print("=" * 72)
    print("verify_block_completion.py -- round 484")
    print("probe SPEC_SHA", B.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("BLOCK_COMPLETION VERIFIED -- "
              "STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)")
        return 0
    print("BLOCK_COMPLETION FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
