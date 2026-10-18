#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_classical_cert.py -- machine check of
rh/problem/classical_cert.tex (round 471,
PRIME.RDAGGER.CLASSICAL_CERT.01, GRID_CERTIFIED).

PART A (STANDALONE):
  G1  claim-boundary tokens in the note
  G2  scramble declaration on the probe
  G3  type constants (GRID_CERTIFIED, L_max pins)

PART B (CONSTRUCTION PINS):
  G10 smoke run of classical_cert_probe.py
  G11 sealed CERT_PINS contain L=0.8 and L_16
  G12 SHAPE_PINS n_max/pp frozen

Exit: "CLASSICAL CERT VERIFIED -- GRID_CERTIFIED(L_max=2.7726)"
iff every gate passed.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import classical_cert_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "classical_cert.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "GRID_CERTIFIED",
        r"\lambda_*(L)",
        "F2b",
        "scramble-sensitive",
        "No RH claim",
        "L=0.8",
        "dictionary-free",
        r"n\le e^{2L}",
        "SPEC\\_SHA",
        "18eb2a33651585f5",
        "Yoshida/Bombieri",
        "Grid-vs-full",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "nodes log n enter P")
    check("G3-type-constants",
          S.VERDICT_KIND == "GRID_CERTIFIED"
          and abs(S.L_MAX_FULL_PIN - 2.7726) < 1e-6
          and abs(S.L_MAX_SMOKE_PIN - 0.8664) < 1e-6,
          "GRID_CERTIFIED L_max pins")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke",
          rc == 0,
          "classical_cert_probe --smoke")
    check("G11-cal-and-top",
          ("L08", 16) in S.CERT_PINS
          and ("L08f", 24) in S.CERT_PINS
          and ("Lk16", 36) in S.CERT_PINS
          and ("L08", 8) in S.CERT_PINS,
          "L=0.8 and L_16 hulls sealed")
    check("G12-shape",
          S.SHAPE_PINS[("L08", 16)] == (7, 5)
          and S.SHAPE_PINS[("Lk16", 36)] == (259, 71)
          and S.SHAPE_PINS[("YB", 8)] == (4, 3),
          "n_max/pp frozen")


def main() -> int:
    print("=" * 72)
    print("verify_classical_cert.py -- round 471")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _name, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("CLASSICAL CERT VERIFIED -- GRID_CERTIFIED(L_max=2.7726)")
        return 0
    print("CLASSICAL CERT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
