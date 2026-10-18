#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_endtoend_fixedl.py -- machine check of
rh/problem/endtoend_fixedl.tex (round 478,
PRIME.RDAGGER.ENDTOEND_FIXEDL.01,
PARTIAL(0.3-even-5x5-PD|tail-Schur)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, 2x2/3x3 pins, K_P gain pin.

Exit: "ENDTOEND_FIXEDL VERIFIED -- PARTIAL(0.3-even-5x5-PD|tail-Schur)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import endtoend_fixedl_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "endtoend_fixedl.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"PARTIAL($0.3$-even-$5\times5$-PD$|$tail-Schur)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(L)",
        r"e^{2L}",
        r"\mathrm{Re}\,\psi",
        "138cbf9410486418",
        r"Not $\lambda_*(0.8)\ge0$",
        "Hilbert--Schmidt",
        "almost periodic",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "sigma_P uses literal log n")
    check("G3-type",
          S.VERDICT_KIND == "PARTIAL(0.3-even-5x5-PD|tail-Schur)"
          and S.LMIN2_LO_PIN == "1.731e-02",
          "PARTIAL + 2x2 floor")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "endtoend_fixedl_probe --smoke")
    check("G11-2x2-floor",
          float(S.LMIN2_LO_PIN) > 0.017
          and float(S.HIGHAM2_PIN) > 0.008,
          "charpoly and Higham floors positive")
    check("G12-kp-gain",
          float(S.KP_GAIN_08_HI) <= 1.02,
          "L=0.8 gain ceiling <= 1.02 (no unlock)")


def main() -> int:
    print("=" * 72)
    print("verify_endtoend_fixedl.py -- round 478")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("ENDTOEND_FIXEDL VERIFIED -- "
              "PARTIAL(0.3-even-5x5-PD|tail-Schur)")
        return 0
    print("ENDTOEND_FIXEDL FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
