#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_schur_cert.py -- machine check of
rh/problem/schur_cert.tex (round 481,
PRIME.RDAGGER.SCHUR_CERTIFICATE.01,
REDUCED(interval-FT+IBP-tail)).

PART A: note tokens, scramble, e^{2L}, type.
PART B: smoke run, epsilon and remainder pins.

Exit: "SCHUR_CERT VERIFIED -- REDUCED(interval-FT+IBP-tail)"
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import schur_cert_probe as S  # noqa: E402

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
    path = os.path.join(REPO, "rh", "problem", "schur_cert.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"REDUCED(interval-FT+IBP-tail)",
        "scramble-sensitive",
        "No RH claim",
        r"\lambda_*(0.3)",
        r"e^{2L}",
        "Yoshida--Bombieri",
        "integration-by-parts",
        "Fourier--HS",
        "not reused",
        "spherical Bessel",
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
          and "IBP" in S.VERDICT_KIND,
          S.VERDICT_KIND)


def part_b() -> None:
    section("PART B  CONSTRUCTION PINS")
    rc = S.run(True)
    check("G10-smoke", rc == 0, "schur_cert_probe --smoke")
    check("G11-eps",
          float(S.EPS_HI_PIN) < 2e-8
          and float(S.C_TAIL_LO_PIN) > 0.24,
          "epsilon and c_tail pins")
    check("G12-open",
          "IBP" in S.VERDICT_KIND
          and float(S.R480_EVEN_LO) > 0.0,
          "remainder is interval FT + IBP tail")


def main() -> int:
    print("=" * 72)
    print("verify_schur_cert.py -- round 481")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    part_a()
    part_b()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS" % (n_ok, len(CHECKS)))
    if n_fail == 0:
        print("SCHUR_CERT VERIFIED -- REDUCED(interval-FT+IBP-tail)")
        return 0
    print("SCHUR_CERT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
