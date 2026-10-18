#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_filon_enclosure.py -- machine check of
rh/problem/filon_enclosure.tex (round 483,
PRIME.RDAGGER.FILON_ENCLOSURE.01,
REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, leftover and Higham pins.

Exit: "FILON_ENCLOSURE VERIFIED -- REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import filon_enclosure_probe as F  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "filon_enclosure.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "Filon",
        "leftover",
        "Fourier--HS",
        "not reused",
        "sign bookkeeping",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          F.SCRAMBLE_SENSITIVE is True
          and "log n" in F.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          F.VERDICT_KIND.startswith("REDUCED")
          and "leftover-C-HS" in F.VERDICT_KIND,
          F.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = F.run(True)
    check("G10-smoke", rc == 0, "filon_enclosure_probe --smoke")
    check("G11-eps",
          float(F.EPS_HI_PIN) < 2e-8
          and float(F.C_TAIL_LO_PIN) > 0.24,
          "epsilon and c_tail pins")
    check("G12-deficit",
          float(F.LEFTOVER_F_PIN) > float(F.LEFTOVER_BUDGET_PIN),
          "leftover HS exceeds SATZ budget")


def main() -> int:
    print("=" * 72)
    print("verify_filon_enclosure.py -- round 483")
    print("probe SPEC_SHA", F.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("FILON_ENCLOSURE VERIFIED -- "
              "REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)")
        return 0
    print("FILON_ENCLOSURE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
