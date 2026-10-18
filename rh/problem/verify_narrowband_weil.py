#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_narrowband_weil.py -- round 461 machine check.

Checks the frozen Lean map, selected-support arithmetic, r459 race
pins, and the literal classical mincut translation carried by
rh/problem/narrowband_weil.tex.

Exit line: NARROWBAND WEIL VERIFIED.
NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import narrowband_weil_probe as S  # noqa: E402

NOTE = os.path.join(REPO, "rh", "problem", "narrowband_weil.tex")
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def main() -> int:
    print("=" * 72)
    print("verify_narrowband_weil.py -- round 461")
    print("probe SPEC_SHA %s" % S.SPEC_SHA)
    print("=" * 72)

    facts = S.lean_map()
    check("G1-verdict", S.VERDICT == "FORK_SHARPENED", S.VERDICT)
    check("G2-lean-class",
          facts["grid_structure"] and facts["support"]
          and facts["full_read"] and facts["selected_formula"],
          "GridElement autocorrelation + fullRead + selected covering")
    check("G3-not-closed-RH",
          facts["arch_sorry"] and facts["density_absent"]
          and facts["spectral_absent"] and facts["named_bridge"]
          and facts["sorry_on_path"],
          "arch sorryAx; density/zero side absent; bridge named")

    pins = [S.selected_pin(k) for k in S.K_VALUES]
    check("G4-support-identity",
          all(abs(float(pin["support"])
                  - int(pin["k"]) * S.LOG2 / 2.0) < 1e-14
              for pin in pins),
          "U_k=k log(2)/2 for k=5..12")
    check("G5-outside-classical",
          all(float(pin["support"]) > S.CLASSICAL_AUTOCORR_SUPPORT
              for pin in pins),
          "all U_k > log(2)")
    check("G6-outside-recent",
          all(float(pin["support"]) > S.RECENT_AUTOCORR_SUPPORT
              for pin in pins),
          "all U_k > 1.6")
    check("G7-tail-pins",
          [int(pin["recent_tail"]) for pin in pins]
          == [1, 3, 5, 7, 18, 22, 26, 30],
          "conditional depths 1,3,5,7,18,22,26,30")
    races = [float(pin["race"]) for pin in pins]
    check("G8-race-band", min(races) > 0.60 and max(races) < 0.76,
          "%.12f..%.12f" % (min(races), max(races)))

    with open(NOTE, encoding="utf-8") as handle:
        note = handle.read()
    required = (
        "Literal translation",
        "cofinal compact-window Weil positivity",
        "SelectedACapPsdImpliesPlainReads",
        "arch_elementwise_stabilization",
        "FORK\\_SHARPENED",
        "No RH claim",
        "arXiv:2608.24827",
        "Bombieri--Lagarias",
    )
    check("G9-note-contract", all(token in note for token in required),
          "literal mincut, gaps, literature, verdict, claim boundary")

    failures = sum(1 for _name, passed in CHECKS if not passed)
    print("\nRESULT: %d/%d gates PASS" % (len(CHECKS) - failures, len(CHECKS)))
    if failures == 0:
        print("NARROWBAND WEIL VERIFIED")
        print("NO RH CLAIM.  NO anti-RH claim.")
        return 0
    print("NARROWBAND WEIL FAILED %d" % failures)
    return 1


if __name__ == "__main__":
    sys.exit(main())
