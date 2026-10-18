#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_resolvent_solve.py -- machine check of
rh/problem/resolvent_solve.tex (round 488,
PRIME.RDAGGER.RESOLVENT_SOLVE.01,
REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; operator-R-gap-open)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, coercivity and G-certificate pins.

Exit: "RESOLVENT_SOLVE VERIFIED -- REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; operator-R-gap-open)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import resolvent_solve_probe as R  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "resolvent_solve.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; operator-R-gap-open)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "coerciv",
        "Birman",
        "Fourier--HS",
        "not reused",
        "shift",
        "r486",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          R.SCRAMBLE_SENSITIVE is True
          and "log n" in R.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          R.VERDICT_KIND.startswith("REDUCED")
          and "R-not-coercive" in R.VERDICT_KIND
          and "operator-R-gap-open" in R.VERDICT_KIND,
          R.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = R.run(True)
    check("G10-smoke", rc == 0, "resolvent_solve_probe --smoke")
    check("G11-shift",
          abs(R.S_SHIFT - 0.05) < 1e-15
          and float(R.N3_BUDGET_OVER_PIN) > 1.0,
          "s=0.05; N=3 crude tail overshoots")
    check("G12-r486",
          abs(float(R.R486_BSE_PIN) - 0.993651) < 1e-6
          and float(R.GBG5_PIN) < 1.0,
          "r486 midpoint and GBG<1 pins")


def main() -> int:
    print("=" * 72)
    print("verify_resolvent_solve.py -- round 488")
    print("probe SPEC_SHA", R.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("RESOLVENT_SOLVE VERIFIED -- "
              "REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; "
              "operator-R-gap-open)")
        return 0
    print("RESOLVENT_SOLVE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
