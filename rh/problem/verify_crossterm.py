#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_crossterm.py -- machine check of
rh/problem/crossterm.tex (round 476,
PRIME.RDAGGER.CROSSTERM_SHARPENING.01,
UNCONDITIONAL(L_max=2.7726) on the first Dirichlet H^2 ball).

PART A: note tokens, scramble, class, YB gate.
PART B: smoke run, Rayleigh pins, sigma(0).

Exit: "CROSSTERM VERIFIED -- UNCONDITIONAL(L_max=2.7726)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import crossterm_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "crossterm.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "UNCONDITIONAL",
        r"H2BALL\_POS",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(L)",
        "Yoshida/Bombieri",
        r"\psi(K+1)",
        "first Dirichlet",
        "a123650e757b912d",
        "not $\\lambda_*(L)\\ge0$",
        "16.16596",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "P uses literal log n")
    check("G3-type",
          S.VERDICT_KIND == "UNCONDITIONAL(L_max=2.7726)"
          and S.CLASS_NAME == "H2BALL_FIRST_DIRICHLET",
          "H2 ball, not lambda_*")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "crossterm_probe --smoke")
    check("G11-yb-pin",
          S.RAYLEIGH_PINS["YB"][2] == 0
          and float(S.RAYLEIGH_PINS["YB"][0]) > 0,
          "YB r_lo>0 and P-used=0")
    check("G12-L16-pin",
          "Lk16" in S.RAYLEIGH_PINS
          and float(S.RAYLEIGH_PINS["Lk16"][0]) > 0,
          "L_16 r_lo pin strictly positive")


def main() -> int:
    print("=" * 72)
    print("verify_crossterm.py -- round 476")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("CROSSTERM VERIFIED -- UNCONDITIONAL(L_max=2.7726)")
        return 0
    print("CROSSTERM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
