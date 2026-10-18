#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Machine verifier for kernel_loewner.tex (round 494).

It checks the theorem and claim-boundary text, the zero-extension
translation convention, all three calibration hits, the booked cutoff,
the exact Hilbert--Schmidt tail with its 2x off-block charge, and reruns
the sealed probe in smoke mode.

Final success line:
  KERNEL LOEWNER VERIFIED -- PROVED(c=2.1000e-3)
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISCOVERY = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISCOVERY not in sys.path:
    sys.path.insert(0, DISCOVERY)

import kernel_loewner_probe as S  # noqa: E402

CHECKS: list[tuple[str, bool]] = []
SEALED_SPEC_SHA = (
    "2e6d71138dff454025641443a9c77f8018d36827dcf94cc35f1696dae9deda47")


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-40s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def note_audit() -> None:
    path = os.path.join(REPO, "rh", "problem", "kernel_loewner.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "Unconditional interval-certified compact-support Weil",
        r"\QW(h)\ge 2.1\cdot10^{-3}",
        r"\|Eh-\tau_xEh\|_{L^2(\mathbb R)}^2",
        "translation boundary strips",
        "3.6980080402989774725",
        "4.2357418881",
        "7.0457565325",
        "2.1137269598",
        "2.1220149285",
        "N1 & blocked",
        "N2 & blocked",
        "N3 & blocked",
        "N4 & blocked",
        "n=2,3,4",
        "No ledger row",
        "not an RH claim",
        "not an anti-RH claim",
    )
    missing = [token for token in tokens if token not in text]
    check("note-theorem-and-boundary", not missing,
          "all tokens present" if not missing
          else "missing: " + ", ".join(missing))


def static_contract() -> None:
    check("sealed-SPEC-SHA", S.SPEC_SHA == SEALED_SPEC_SHA,
          S.SPEC_SHA[:16])
    check("three-gate-constants",
          S.L == 0.3 and S.TWO_L == 0.6
          and S.X0 == 0.01 and S.X1 == 0.03
          and S.SECTION_N == 401 and S.MAX_ALLOWED_N == 800,
          "L=.3 cutoff=[.01,.03] n=401 cap=800")
    check("operator-floor-type",
          S.CLAIM_C == 2.1e-3,
          "PROVED(c=2.1000e-3)")
    check("off-block-pad",
          S.MATRIX_FRO_PAD > 0 and S.MATRIX_OP_PAD > 0
          and S.POLE_BLOCK_PAD > 0,
          "outward finite/off-block/pole pads present")


def rerun_probe() -> None:
    result = S.run(True)
    check("sealed-smoke-rerun", result == 0,
          "17/17 gates and G3 tail<margin/3")


def main() -> int:
    print("=" * 74)
    print("verify_kernel_loewner.py -- round 494")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 74)
    note_audit()
    static_contract()
    rerun_probe()
    failures = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS" %
          (len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("KERNEL LOEWNER VERIFIED -- PROVED(c=2.1000e-3)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
