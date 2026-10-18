#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_modulus_upgrade.py -- machine check of
rh/problem/modulus_upgrade.tex (round 474,
PRIME.RDAGGER.MODULUS_UPGRADE.01, PARTIAL).

PART A: note tokens, scramble, type constants.
PART B: smoke run, S_eff(YB)=0, omega pins.

Exit: "MODULUS UPGRADE VERIFIED -- PARTIAL"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import modulus_upgrade_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "modulus_upgrade.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "PARTIAL",
        "SHORT",
        "F2b",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(L)",
        r"S_{\mathrm{eff}}",
        r"\delta^2/\pi^2",
        "Yoshida/Bombieri",
        "GRID_CERTIFIED",
        "modulus is too crude",
        "45db1c92384913e8",
    )
    missing = [tok for tok in tokens if tok not in text]
    check("G1-note-tokens",
          not missing,
          "all present" if not missing else "missing " + ", ".join(missing))
    check("G2-scramble",
          S.SCRAMBLE_SENSITIVE is True
          and "log n" in S.SCRAMBLE_REASON,
          "S_eff uses literal log n")
    check("G3-type",
          S.VERDICT_KIND == "PARTIAL"
          and S.JACKSON_L2 == "1/pi^2",
          "PARTIAL + Jackson 1/pi^2")


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "modulus_upgrade_probe --smoke")
    check("G11-yb-Seff",
          S.S_EFF_PINS["YB"] == ("0.0", "0.0", 0),
          "S_eff(L=0.3)=0")
    check("G12-omega-ceiling",
          ("YB", 8) in S.OMEGA_PINS and ("Lk16", 36) in S.OMEGA_PINS,
          "YB and L_16 omega pins present")


def main() -> int:
    print("=" * 72)
    print("verify_modulus_upgrade.py -- round 474")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("MODULUS UPGRADE VERIFIED -- PARTIAL")
        return 0
    print("MODULUS UPGRADE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
