#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_weighted_schur.py -- machine check of
rh/problem/weighted_schur.tex (round 485,
PRIME.RDAGGER.WEIGHTED_SCHUR.01,
REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT).

PART A: note tokens, scramble, e^{2L}, type, checkpoint.
PART B: smoke run, A-GO and S_w pins.

Exit: "WEIGHTED_SCHUR VERIFIED -- REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import weighted_schur_probe as W  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "weighted_schur.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "weighted",
        "orthocomplement",
        "Fourier--HS",
        "not reused",
        "checkpoint",
        "Erd",
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
          and "A-GO" in W.VERDICT_KIND
          and "CHECKPOINT" in W.VERDICT_KIND
          and "operator-M_inf-open" in W.VERDICT_KIND,
          W.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = W.run(True)
    check("G10-smoke", rc == 0, "weighted_schur_probe --smoke")
    check("G11-a-go",
          float(W.HI_FRAC_PIN) > 0.95
          and float(W.C08_PIN) < 1e-8,
          "A-GO pins: hi-frac and [0,8] edge")
    check("G12-sw",
          float(W.SW150_PIN) > float(W.R483_EVEN_PIN)
          and float(W.DMIN150_PIN) < 0.24,
          "finite S_w beats r483 flat; D undershoots")


def main() -> int:
    print("=" * 72)
    print("verify_weighted_schur.py -- round 485")
    print("probe SPEC_SHA", W.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("WEIGHTED_SCHUR VERIFIED -- "
              "REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)+CHECKPOINT")
        return 0
    print("WEIGHTED_SCHUR FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
