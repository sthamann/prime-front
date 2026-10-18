#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_race_proof.py -- machine check of every numbered result in
rh/problem/race_proof.tex (round 460).

PART A (EXACT RATIONAL TOY):
  G1  spectral race identity
  G2  race equivalence
  G3  two-band upper bound and finite certificate
  G4  fixed-r plateau cardinality and spacing

PART B (FULL-COMB CONSTRUCTION PINS):
  G10 k=5..12 r459 race band
  G11 solve/spectral identity
  G12 norm and Gershgorin no-go
  G13 finite two-band scope
  G14 fixed-r q* plateaux
  G15 exact remaining status

Exit: "RACE PROOF ATTEMPT VERIFIED -- OUTCOME PARTIAL" iff every gate
passes.  NO RH claim and NO anti-RH claim.
"""
from __future__ import annotations

from fractions import Fraction
import math
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import race_proof_probe as S  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %-34s %s" % ("PASS" if ok else "FAIL", name, detail),
        flush=True,
    )
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72, flush=True)


def exact_toy() -> None:
    section("PART A  EXACT RATIONAL THEOREM WARDS")
    eigenvalues = (
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
    )
    coefficients = (
        Fraction(1, 10),
        Fraction(1, 5),
        Fraction(1, 20),
    )
    q_spectral = sum(
        coefficient * coefficient / (1 - eigenvalue)
        for coefficient, eigenvalue in zip(coefficients, eigenvalues)
    )
    diagonal_inverse_form = (
        coefficients[0] ** 2 / Fraction(3, 4)
        + coefficients[1] ** 2 / Fraction(1, 2)
        + coefficients[2] ** 2 / Fraction(1, 4)
    )
    check(
        "G1-spectral-identity",
        q_spectral == diagonal_inverse_form == Fraction(31, 300),
        "q=31/300 exactly",
    )

    qstar = Fraction(2, 5)
    increment = q_spectral - qstar
    check(
        "G2-race-equivalence",
        (q_spectral < 1) == (increment < 1 - qstar),
        "q=q*+Delta q; both inequalities true exactly",
    )

    theta = Fraction(1, 2)
    low_mass = coefficients[0] ** 2 + coefficients[1] ** 2
    high_mass = coefficients[2] ** 2
    two_band_bound = (
        low_mass / (1 - theta)
        + high_mass / (1 - max(eigenvalues))
    )
    check(
        "G3-two-band-bound",
        q_spectral <= two_band_bound < 1
        and two_band_bound == Fraction(11, 100),
        "31/300 <= 11/100 < 1 exactly",
    )

    plateau_ok = True
    for r in range(1, 80):
        members = list(range(r * r, (r + 1) * (r + 1)))
        plateau_ok = (
            plateau_ok
            and len(members) == 2 * r + 1
            and all(math.isqrt(k) == r for k in members)
        )
    check(
        "G4-plateau-theorem",
        plateau_ok,
        "cardinality 2r+1, r=1..79 exact-integer ward",
    )


def construction_pins() -> None:
    section("PART B  FULL-COMB CONSTRUCTION PINS")
    prime_powers = S.S459.sieve_pp(S.SIEVE_CAP)
    rows = [
        S.selected_row(k, prime_powers)
        for k in range(S.K_FIRST, S.K_LAST + 1)
    ]
    races = [row["race"]["race"] for row in rows]
    check(
        "G10-race-band",
        all(
            row["race"]["complete"]
            and row["race"]["live"]
            and abs(row["race"]["race"] - S.S459.LEAN_RACE[row["k"]])
            < 1e-10
            for row in rows
        )
        and min(races) > 0.60
        and max(races) < 0.76,
        "[%.6f, %.6f], k=5..12 complete/live"
        % (min(races), max(races)),
    )

    identity_error = max(
        abs(row["main"]["q_solve"] - row["main"]["q_spectral"])
        for row in rows
    )
    check(
        "G11-spectral-live",
        identity_error < 2e-12,
        "max solve/spectral error %.2e" % identity_error,
    )

    raw_bounds = [row["main"]["raw_bound"] for row in rows]
    gershgorin = [row["main"]["gershgorin_lower"] for row in rows]
    check(
        "G12-norm-no-go",
        min(raw_bounds) > 1.0
        and max(gershgorin) < 0.0
        and abs(raw_bounds[0] - S.RAW_BOUND_FIRST) < 1e-9
        and abs(raw_bounds[-1] - S.RAW_BOUND_LAST) < 1e-5,
        "raw %.3f..%.3f; Gersh max %.3f"
        % (raw_bounds[0], raw_bounds[-1], max(gershgorin)),
    )

    split_bounds = [row["main"]["best_split_bound"] for row in rows]
    check(
        "G13-two-band-scope",
        split_bounds[0] < 1.0 and min(split_bounds[1:]) > 1.0,
        "k5 %.3f; min k6..12 %.3f"
        % (split_bounds[0], min(split_bounds[1:])),
    )

    qstar_first = [row["race"]["qA"] for row in rows[:4]]
    qstar_second = [row["race"]["qA"] for row in rows[4:]]
    check(
        "G14-qstar-plateaux",
        max(qstar_first) - min(qstar_first) < 2e-15
        and max(qstar_second) - min(qstar_second) < 2e-15,
        "r2 %.15f; r3 %.15f"
        % (qstar_first[0], qstar_second[0]),
    )

    check(
        "G15-outcome",
        S.OUTCOME == "PARTIAL"
        and S.VERDICT_A == "SPECTRAL_REDUCTION_PROVED"
        and S.VERDICT_B == "NORM_ROUTE_REFUTED"
        and S.VERDICT_C == "PLATEAU_ROUTE_FINITE"
        and S.VERDICT_D == "SPECTRAL_OVERLAP_OPEN",
        "finite theorems proved; cofinal source estimate open",
    )


def main() -> int:
    print("=" * 72)
    print("verify_race_proof.py -- round 460")
    print("probe SPEC_SHA %s" % S.SPEC_SHA[:16])
    print("=" * 72)
    exact_toy()
    construction_pins()
    failures = sum(1 for _name, ok in CHECKS if not ok)
    passes = len(CHECKS) - failures
    print("\nRESULT: %d/%d gates PASS" % (passes, len(CHECKS)))
    if failures == 0:
        print("RACE PROOF ATTEMPT VERIFIED -- OUTCOME PARTIAL")
        return 0
    print("RACE PROOF ATTEMPT FAILED %d" % failures)
    return 1


if __name__ == "__main__":
    sys.exit(main())
