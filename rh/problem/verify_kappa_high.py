#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_kappa_high.py -- machine check of
rh/problem/kappa_high.tex (round 480,
PRIME.RDAGGER.KAPPA_HIGH.01,
REDUCED(refined-Schur; crude-kappa_high-killed@0.30)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, crude-kill and refined-Schur pins.

Exit: "KAPPA_HIGH VERIFIED -- REDUCED(refined-Schur; crude-kappa_high-killed@0.30)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import kappa_high_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "kappa_high.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(refined-Schur; crude-$\kappa_{\mathrm{high}}$-killed@$0.30$)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        r"\kappa_{\mathrm{high}}",
        "Yoshida--Bombieri",
        "integration-by-parts",
        "Fourier--HS",
        "not reused",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "literal log n")
    check("G3-type",
          S.VERDICT_KIND.startswith("REDUCED")
          and "killed" in S.VERDICT_KIND,
          S.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "kappa_high_probe --smoke")
    check("G11-crude-floor",
          float(S.KAPPA_HIGH_LO_PIN) >= 0.25
          and float(S.KAPPA_HIGH_NEED) < 0.02,
          "named bound 0.0179 killed by floor 0.25")
    check("G12-schur-pin",
          float(S.SCHUR_EVEN_LO_PIN) > 0.0
          and float(S.SCHUR_ODD_LO_PIN) > 0.1,
          "refined Schur working floors")


def main() -> int:
    print("=" * 72)
    print("verify_kappa_high.py -- round 480")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("KAPPA_HIGH VERIFIED -- "
              "REDUCED(refined-Schur; crude-kappa_high-killed@0.30)")
        return 0
    print("KAPPA_HIGH FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
