#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_operator_residual.py -- machine check of
rh/problem/operator_residual.tex (round 490,
PRIME.RDAGGER.OPERATOR_RESIDUAL.01,
STUCK(off/s=5.86-eats-1000x; GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, A-nogo and r488 midpoint pins.

Exit: "OPERATOR_RESIDUAL VERIFIED -- STUCK(off/s=5.86-eats-1000x; GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import operator_residual_probe as R  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "operator_residual.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"STUCK(off/s=5.86-eats-1000x; GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "off/s",
        "5.86",
        "Fourier--HS",
        "not reused",
        "r488",
        "B1",
        "ideas",
        "FINAL",
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
          R.VERDICT_KIND.startswith("STUCK")
          and "FINAL_CHECKPOINT" in R.VERDICT_KIND
          and "off/s=5.86" in R.VERDICT_KIND,
          R.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = R.run(True)
    check("G10-smoke", rc == 0, "operator_residual_probe --smoke")
    check("G11-nogo",
          float(R.OFF_M5_I1_PIN) >= 5.0
          and float(R.MARGIN_PIN) < 1e-2,
          "certificate residual pin vs margin")
    check("G12-r488",
          abs(float(R.R488_GBG5_PIN) - 0.9944) < 1e-4
          and R.S_SHIFT == 0.05,
          "r488 midpoint pin")


def main() -> int:
    print("=" * 72)
    print("verify_operator_residual.py -- round 490")
    print("probe SPEC_SHA", R.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("OPERATOR_RESIDUAL VERIFIED -- "
              "STUCK(off/s=5.86-eats-1000x; "
              "GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)")
        return 0
    print("OPERATOR_RESIDUAL FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
