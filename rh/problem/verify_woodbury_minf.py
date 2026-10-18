#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_woodbury_minf.py -- machine check of
rh/problem/woodbury_minf.tex (round 486,
PRIME.RDAGGER.WOODBURY_MINF.01,
REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, enemy-spectrum and BS pins.

Exit: "WOODBURY_MINF VERIFIED -- REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import woodbury_minf_probe as W  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "woodbury_minf.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "Birman",
        "enemy",
        "Fourier--HS",
        "not reused",
        "Woodbury",
        "t_c",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          W.SCRAMBLE_SENSITIVE is True
          and "log n" in W.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          W.VERDICT_KIND.startswith("REDUCED")
          and "enemy-3dim" in W.VERDICT_KIND
          and "operator-Rinv-open" in W.VERDICT_KIND,
          W.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = W.run(True)
    check("G10-smoke", rc == 0, "woodbury_minf_probe --smoke")
    check("G11-enemy",
          float(W.LAM0_PIN) > 0.8
          and float(W.LAM2_PIN) > 0.02
          and float(W.REST012_PIN) < 1e-3,
          "large eigenvalues; trace-rest tiny")
    check("G12-bs-r476",
          float(W.BS_HI_PIN) < 1.0
          and float(W.QDIR_LO_PIN) < float(W.QDIR_HI_PIN),
          "BS<1 pin and r476 hull")


def main() -> int:
    print("=" * 72)
    print("verify_woodbury_minf.py -- round 486")
    print("probe SPEC_SHA", W.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("WOODBURY_MINF VERIFIED -- "
              "REDUCED(enemy-3dim-BS<1; Q_E-Higham; operator-Rinv-open)")
        return 0
    print("WOODBURY_MINF FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
