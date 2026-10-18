#!/usr/bin/env python3
"""Independent verifier for the r482 Carleson-edgeband note."""
from __future__ import annotations

import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISCOVERY = os.path.join(ROOT, "experiments", "tfpt-discovery")
if DISCOVERY not in sys.path:
    sys.path.insert(0, DISCOVERY)

import carleson_edgeband_probe as C  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    worlds = C.build_worlds(C.K_FULL)

    record = C.curve_record(worlds)
    curve_sha = hashlib.sha256(record.encode("ascii")).hexdigest()
    require(curve_sha == C.CURVE_SHA, "curve seal mismatch")

    pooled = C.pooled_fit(worlds)
    require(abs(pooled["epsilon"] - 0.2746633536610459) < 2e-12,
            "pooled epsilon")
    require(abs(pooled["C"] - 0.019002023524658948) < 2e-14,
            "pooled C")
    require(pooled["n"] == 127 and pooled["delta_aic"] < -23.6,
            "pooled AIC and drops")

    constants = [
        C.envelope_constant(world["main"], C.FIT_EPSILON)
        for world in worlds
    ]
    require(abs(max(constants) - 0.6665278419525172) < 2e-12,
            "uniform finite envelope")

    sr_values = []
    strict_reversals = 0
    world_gate = True
    for world in worlds:
        k = world["k"]
        sr = C.optimize_sr(world["main"])
        sr_values.append(sr["value"])
        require(abs(sr["value"] - C.SR_PINS[k]) < 5e-6,
                "SR pin k=%d" % k)

        main_curve = C.distribution(world["main"])
        scramble_curve = C.distribution(world["scramble"])
        if scramble_curve[0] < main_curve[0]:
            strict_reversals += 1
        main_danger = (
            C.danger_mass(world["main"], 0.5)
            / float(world["main"]["u"] @ world["main"]["u"])
        )
        scramble_danger = (
            C.danger_mass(world["scramble"], 0.5)
            / float(world["scramble"]["u"] @ world["scramble"]["u"])
        )
        world_gate = world_gate and scramble_danger > main_danger

    require(min(sr_values) > 1.05 and max(sr_values) > 2.70 - 1e-4,
            "SR must close no finite window")
    require(strict_reversals == 2 and world_gate,
            "strict-F / dangerous-mass world distinction")

    christoffel = [
        C.christoffel_factor(world["main"]) for world in worlds
    ]
    planch = [
        C.local_plancherel_bound(world["main"])
        for world in worlds if world["k"] >= 9
    ]
    require(min(christoffel) > 100 and max(christoffel) > 7e7,
            "Christoffel sharpness")
    require(min(row["factor"] for row in planch) > 5e3,
            "Plancherel sharpness")

    enclosures = [
        C.binary64_enclosure_ward(world["main"]) for world in worlds
    ]
    require(max(row["residual"] for row in enclosures) < 2e-14,
            "eigen residual")
    require(min(row["classification_ratio"] for row in enclosures) > 1e8,
            "dyadic classification enclosure")

    note_path = os.path.join(ROOT, "rh", "problem",
                             "carleson_edgeband.tex")
    with open(note_path, encoding="utf-8") as handle:
        note = handle.read()
    required_text = (
        "STUCK(SR_FAILS_FINITE_CENSUS",
        "0.666528",
        "0.274663",
        "STRICT_F_SCRAMBLE_PREMISE_FALSE",
        "RESTRICTED_LARGE_SIEVE_IS_TARGET",
        "No RH claim",
    )
    for token in required_text:
        require(token in note, "note token missing: " + token)

    print(
        "VERIFIED carleson_edgeband "
        "curve=%s SR=[%.6f,%.6f] verdict=%s"
        % (curve_sha[:16], min(sr_values), max(sr_values), C.VERDICT)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
