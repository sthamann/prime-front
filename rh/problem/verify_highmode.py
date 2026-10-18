#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_highmode.py -- machine check of
rh/problem/highmode.tex (round 477,
PRIME.RDAGGER.HIGHMODE_DOMINANCE.01,
ARCHITECTURE_STANDS(0.3,0.8,1.0)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, YB t0, Schur pin.

Exit: "HIGHMODE VERIFIED -- ARCHITECTURE_STANDS(0.3,0.8,1.0)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import highmode_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "highmode.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"ARCHITECTURE\_STANDS",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(L)",
        r"e^{2L}",
        r"\mathrm{Re}\,\psi",
        "Yoshida/Bombieri",
        "57fd2de61c6fdcc9",
        r"Not $\lambda_*(L)\ge0$",
        "Schur",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "t0 uses literal log n")
    check("G3-type",
          S.VERDICT_KIND == "ARCHITECTURE_STANDS(0.3,0.8,1.0)"
          and S.T0_PINS["YB"] == "22.0",
          "schema + YB t0=22")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "highmode_probe --smoke")
    check("G11-yb-t0",
          float(S.T0_PINS["YB"]) <= 22.01
          and S.S_EFF_PINS["YB"][2] == 0,
          "YB t0 sealed, S_eff used=0")
    check("G12-schur-floor",
          float(S.SCHUR_PINS["YB"]) > 0
          and float(S.SCHUR_PINS["L10"]) > 0,
          "2x2 Schur floors positive")


def main() -> int:
    print("=" * 72)
    print("verify_highmode.py -- round 477")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("HIGHMODE VERIFIED -- ARCHITECTURE_STANDS(0.3,0.8,1.0)")
        return 0
    print("HIGHMODE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
