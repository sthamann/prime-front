#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Machine verifier for kernel_redteam.tex (round 495).

Checks the independent derivation/audit tokens, sealed probe contract,
exact rational boundary tests, false-world failure, complete
Hilbert--Schmidt block accounting, outward floor arithmetic, and the
under-60-second smoke route.

Final success line:
  KERNEL REDTEAM VERIFIED -- CONFIRMED(c=2.1000e-3)
"""
from __future__ import annotations

import os
import sys


REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISCOVERY = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISCOVERY not in sys.path:
    sys.path.insert(0, DISCOVERY)

import kernel_redteam_probe as S  # noqa: E402


SEALED_SPEC_SHA = (
    "431251a9bcfd40a12d36f5e4a2bc76751afdcdd980a177f9de9597687e21a053"
)
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-38s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def note_audit() -> None:
    note_path = os.path.join(REPO, "rh", "problem", "kernel_redteam.tex")
    with open(note_path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "CONFIRMED($c=2.1000",
        r"\widehat h(i/2)\widehat h(-i/2)",
        "Five non-calibration",
        "2.12\\cdot10^{-61}",
        "whole-line identities are exact",
        "-1.9249512553313268",
        "-2.188167590810956",
        "1.501365808845941",
        "6.794869\\cdot10^{-4}",
        r"2\|Q T_wP\|_{\rm HS}^2+\|Q T_wQ\|_{\rm HS}^2",
        "6.2971739\\cdot10^{-4}",
        "2.122014890249863",
        "not an RH claim",
        "not an anti-RH claim",
    )
    missing = [token for token in tokens if token not in text]
    check(
        "note-evidence-and-boundary",
        not missing,
        "all tokens present" if not missing
        else "missing: " + ", ".join(missing),
    )


def static_contract() -> None:
    check("sealed-SPEC-SHA", S.SPEC_SHA == SEALED_SPEC_SHA,
          S.SPEC_SHA[:16])
    check(
        "fixed-support-contract",
        S.L == S.mp.mpf("0.3")
        and S.SPAN == S.mp.mpf("0.6")
        and S.SECTION_N == 401
        and S.CLAIM_C == S.mp.mpf("0.0021"),
        "L=.3 span=.6 n=401 c=.0021",
    )
    exact_rows = S.attack_a2()
    check(
        "exact-boundary-strip-contract",
        len(exact_rows) == 6
        and all(row["correlation"] == row["whole"] for row in exact_rows)
        and all(row["boundary"] > 0 for row in exact_rows),
        "6/6 identities, 6/6 positive strips",
    )
    outward_floor = (
        S.R494_KAPPA_LO - S.R494_C_HI - S.R494_SECTION_UPPER
        - 3 * S.R494_TAIL_UPPER
    )
    check(
        "outward-floor-arithmetic",
        outward_floor >= S.CLAIM_C,
        "%s" % S.mp.nstr(outward_floor, 18),
    )


def rerun_probe() -> None:
    started = S.time.perf_counter()
    result = S.run(True)
    elapsed = S.time.perf_counter() - started
    check(
        "sealed-smoke-under-60s",
        result == 0 and elapsed < 60,
        "result=%d elapsed=%.2fs" % (result, elapsed),
    )


def main() -> int:
    print("=" * 74)
    print("verify_kernel_redteam.py -- round 495")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 74)
    note_audit()
    static_contract()
    rerun_probe()
    failures = [name for name, passed in CHECKS if not passed]
    print("\nRESULT: %d/%d gates PASS" % (
        len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("KERNEL REDTEAM VERIFIED -- CONFIRMED(c=2.1000e-3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
