#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Machine verifier for overlap_mechanism.tex (round 467).

Final success line:
  OVERLAP MECHANISM NOTE VERIFIED -- VERDICT STUCK
"""
from __future__ import annotations

import os
import sys

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISCOVERY = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISCOVERY not in sys.path:
    sys.path.insert(0, DISCOVERY)

import overlap_mechanism_probe as S  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-36s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def note_audit() -> None:
    path = os.path.join(REPO, "rh", "problem", "overlap_mechanism.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        "STUCK",
        r"U_r=\sum_{i=0}^{r}u_i",
        r"N^{-0.196225}",
        "119482.632",
        "SOURCE\\_TO\\_BORDER\\_BASIS\\_BRIDGE\\_MISSING",
        "thirty-one",
        "r429",
        "No RH claim",
        "does not prove",
    )
    check("note-content-and-boundary",
          all(token in text for token in tokens),
          "lemma, anatomy, stop gate, alias audit, claim boundary")


def regenerate() -> None:
    prime_powers = S.S459.sieve_pp(S.SIEVE_CAP)
    worlds = [S.selected_worlds(k, prime_powers) for k in S.K_FULL]
    top_rows = []
    band_factors = []
    arch_fractions = []
    scramble_ratios = []
    for world in worlds:
        for name in ("main", "arch", "scramble"):
            world[name]["k"] = world["k"]
        modes = S.mode_anatomy(world["main"])
        arch = S.mode_anatomy(world["arch"], 1)[-1]
        scramble = S.mode_anatomy(world["scramble"], 1)[-1]
        top = modes[-1]
        top_rows.append(top)
        measured = sum(mode["q_term"] for mode in modes)
        bound = sum(mode["abel_bound"]**2 / mode["gap"]
                    for mode in modes)
        band_factors.append(bound / measured)
        arch_fractions.append(arch["overlap_fraction"])
        scramble_ratios.append(
            scramble["overlap_fraction"] / top["overlap_fraction"])

    check("exact-Abel-ward", S.exact_abel_ward(),
          "rational summation by parts")
    check("top-mode-pins",
          all(
              abs(top["lambda"] - S.TOP_PINS[k][0]) < 2e-12
              and abs(top["overlap_fraction"] - S.TOP_PINS[k][1]) < 2e-12
              for k, top in zip(S.K_FULL, top_rows)
          ),
          "8/8 eigenvalue and normalized-overlap pins")
    check("band-factor-pins",
          all(abs(observed / S.BAND_FACTOR_PINS[k] - 1.0) < 2e-10
              for k, observed in zip(S.K_FULL, band_factors)),
          "91.703..119482.632")
    check("stop-gate",
          sum(factor > 1e3 for factor in band_factors) == 6
          and min(top["abel_factor"] for top in top_rows) > 10.0,
          "k=7..12 exceed 1e3; no top factor below 10")
    check("world-controls",
          min(arch_fractions) > 0.995
          and min(scramble_ratios) > 25.0,
          "ARCH aligns; SCR/MAIN fraction ratio >=28.5")

    dimensions = np.asarray(
        [world["shape"]["Nw"] for world in worlds], dtype=float)
    variations = np.asarray(
        [top["variation"] for top in top_rows], dtype=float)
    overlaps = np.asarray(
        [top["overlap_sq"] for top in top_rows], dtype=float)
    slope = float(np.polyfit(
        np.log(dimensions), np.log(variations), 1)[0])
    correlation = float(np.corrcoef(
        variations, np.log10(overlaps))[0, 1])
    check("smoothness-census",
          abs(slope + 0.19622529315605727) < 1e-12
          and abs(correlation - 0.7453435536628458) < 1e-12,
          "TV slope %.6f; correlation %.6f" % (slope, correlation))

    wards = [
        S.high_precision_ward(world["main"], S.mode_anatomy(world["main"]))
        for world in worlds
    ]
    check("dps80-ward",
          max(ward["eigen_error"] for ward in wards) < 2e-15
          and max(ward["overlap_error"] for ward in wards) < 2e-12
          and max(ward["residual"] for ward in wards) < 2e-14,
          "edge decomposition stable at dps=80")
    check("verdict-pin",
          S.VERDICT.startswith("STUCK(")
          and "SOURCE_TO_BORDER_BASIS_BRIDGE_MISSING" in S.VERDICT,
          S.VERDICT)


def main() -> int:
    print("=" * 72)
    print("verify_overlap_mechanism.py -- round 467")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    note_audit()
    regenerate()
    failures = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS" %
          (len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("OVERLAP MECHANISM NOTE VERIFIED -- VERDICT STUCK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
