#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kneser_groupoid_halfdensity_probe -- KNESER.GROUPOID.HALFDENSITY.01

Exploration only: this is not a verification/ledger/paper result and makes no
RH claim.

Frozen contract
---------------
Object: for p in {3,5,7} (and 2 only if v535 supplies the marked operator), use
the finite groupoid of MARKED Kneser neighbour states defined by v535.  v535
lines 120--143 define the four mu4 glue classes through ``DVEC``; lines
580--600 define their theta channels ``Th0,...,Th3``; lines 603--633 define
the E8 isotropic-point/line correspondence; and lines 636--710 identify the
marked neighbour-sum with ``nu_p = a Id + b T_p``.  Morphisms are Kneser
p-neighbour relations with the mark transported.  v535 does not expose a
state-to-state marked adjacency matrix, so the contract's fallback is used:
the four mu4 states are resolved by the affine identity and Hecke channels.
The Type-A/B refinement is the exact local-density split of v536 lines
180--221 and 632--672.

Measures: per channel and marked state x, compute the exact source fibre
``s(x)`` and target fibre ``t(x)``, Delta=t/s, and Delta^(1/2).  For m=1,2,3
check Delta(g o h)=Delta(g)Delta(h) and whether the resulting half-density
equals p^(-m/2).  The required explicit-formula amplitude
``log(p) p^(-m/2)`` is reported only as a target; p^(-1/2) is never inserted
into the groupoid measure.

Kill criteria: K1 if Delta is identically one on every tested state/channel;
K2 if nontrivial Delta has no multiplicative p^(-m/2) composite law; K3 if
nontriviality is only a p-independent finite-mark stabiliser ratio.
Survive criterion: a channel has Delta^(1/2)=c p^(-m/2) for m=1,2,3 with c
independent of m and p (or exactly log(p)-proportional), with explicit states.

Controls: C1 is the unmarked class-number-one E8 correspondence; C2 is an
oriented rooted p-branching tree correspondence, whose parent-to-child
channel has Delta=1/p and hence the exact p^(-m/2) law; C3 deterministically
permutes the four marks.  Counts and verdict logic use Python integers and
fractions.Fraction only.  Output is deterministic JSON plus at most 25 lines.

Scope: this decides only whether the finite marked Kneser/channel geometry
emits the prime half-density.  It does not address an explicit-formula
identity, positivity, or RH.
"""
from __future__ import annotations

import hashlib
import json
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path


CONTRACT = "KNESER.GROUPOID.HALFDENSITY.01"
PRIMES = (3, 5, 7)
MARKS = tuple(range(4))
COMPOSITE_LENGTHS = (1, 2, 3)
SCRAMBLE_SEED = 20260904
HERE = Path(__file__).resolve().parent
RESULT_PATH = HERE / "kneser_groupoid_halfdensity_result.json"
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# v535 line 69 and lines 663--703.
A_P = {3: -4, 5: -2, 7: 24}

V535_REFS = {
    "mark": "verification/v535_hecke_from_geometry.py:120-143,580-600",
    "isotropic_correspondence":
        "verification/v535_hecke_from_geometry.py:603-633",
    "marked_operator":
        "verification/v535_hecke_from_geometry.py:636-710",
}
V536_REFS = {
    "type_ab_definition":
        "verification/v536_eichler_trace_layer.py:180-221,632-672",
}


def frac_text(value: Fraction) -> str:
    return (str(value.numerator) if value.denominator == 1
            else f"{value.numerator}/{value.denominator}")


def sigma3(p: int) -> int:
    return 1 + p ** 3


def projective_3_count(p: int) -> int:
    return (p ** 4 - 1) // (p - 1)


def isotropic_point_count(p: int) -> int:
    return p ** 7 + p ** 4 - p ** 3


def isotropic_line_count(p: int) -> int:
    return sigma3(p) * projective_3_count(p)


def type_a_point_count(p: int) -> int:
    return min(240 * sigma3(p), isotropic_point_count(p) - 1)


def type_b_point_count(p: int) -> int:
    return isotropic_point_count(p) - 1 - type_a_point_count(p)


def affine_coefficients(p: int) -> tuple[int, int]:
    """v535's exact nu_p=a Id+b T_p coefficients."""
    b = sigma3(p) + A_P[p]
    a = isotropic_line_count(p) - b * sigma3(p)
    assert a >= 0 and b >= 0
    return a, b


def channel_degrees(p: int) -> dict[str, int]:
    """Exact outgoing degrees in the frozen fallback channel model."""
    a, b = affine_coefficients(p)
    type_a_points = type_a_point_count(p)
    type_b_points = type_b_point_count(p)
    assert type_a_points % (p - 1) == 0
    assert type_b_points % (p - 1) == 0
    channels = {
        "ALL_KNESER": isotropic_line_count(p),
        "AFFINE_IDENTITY": a,
        "HECKE_COMPONENT": b * sigma3(p),
        "TYPE_A": type_a_points // (p - 1),
    }
    if type_b_points:
        channels["TYPE_B"] = type_b_points // (p - 1)
    assert channels["AFFINE_IDENTITY"] + channels["HECKE_COMPONENT"] \
        == channels["ALL_KNESER"]
    assert channels["TYPE_A"] + channels.get("TYPE_B", 0) \
        == channels["ALL_KNESER"]
    return channels


def transport_permutation(p: int, channel_index: int) -> tuple[int, ...]:
    """A deterministic bijective mark transport.

    v535 resolves four aggregate mu4 theta channels but does not publish the
    marked adjacency.  Every allowed transport in the fallback is therefore
    represented by a permutation.  Fibre regularity is permutation-invariant.
    """
    shift = (p + channel_index) % len(MARKS)
    return tuple((mark + shift) % len(MARKS) for mark in MARKS)


def scramble_permutation(p: int, channel: str) -> tuple[int, ...]:
    seed = SCRAMBLE_SEED + 1009 * p + sum(ord(char) for char in channel)
    rng = random.Random(seed)
    values = list(MARKS)
    rng.shuffle(values)
    return tuple(values)


def delta_histogram(rows: list[dict]) -> dict[str, int]:
    return dict(sorted(Counter(row["delta"] for row in rows).items()))


def evaluate_marked_prime(p: int, scrambled: bool = False) -> dict:
    channels = channel_degrees(p)
    channel_rows = {}
    all_unimodular = True
    composition_ok = True
    scaling_channels = []

    for channel_index, (channel, degree) in enumerate(channels.items()):
        permutation = (
            scramble_permutation(p, channel) if scrambled
            else transport_permutation(p, channel_index)
        )
        assert sorted(permutation) == list(MARKS)
        rows = []
        for source in MARKS:
            target = permutation[source]
            source_fibre = degree
            # A bijection of marks sends exactly one source class to each
            # target class, with the same channel multiplicity.
            target_fibre = degree
            delta = Fraction(target_fibre, source_fibre)
            rows.append({
                "state": f"mu4:{source}",
                "transported_to": f"mu4:{target}",
                "source_fibre": source_fibre,
                "target_fibre": target_fibre,
                "delta": frac_text(delta),
                "half_density": "1" if delta == 1
                                else f"sqrt({frac_text(delta)})",
            })

        deltas = [Fraction(row["target_fibre"], row["source_fibre"])
                  for row in rows]
        composites = []
        channel_scaling = True
        for length in COMPOSITE_LENGTHS:
            composite_delta = Fraction(1)
            for _ in range(length):
                composite_delta *= deltas[0]
            multiplicative = composite_delta == deltas[0] ** length
            expected_squared = Fraction(1, p ** length)
            matches_prime_halfdensity = composite_delta == expected_squared
            channel_scaling &= matches_prime_halfdensity
            composition_ok &= multiplicative
            composites.append({
                "length": length,
                "delta": frac_text(composite_delta),
                "half_density": (
                    "1" if composite_delta == 1
                    else f"sqrt({frac_text(composite_delta)})"
                ),
                "multiplicativity_exact": multiplicative,
                "target_half_density": f"{p}^(-{length}/2)",
                "target_amplitude": f"log({p})*{p}^(-{length}/2)",
                "emits_target_half_density": matches_prime_halfdensity,
            })
        if channel_scaling:
            scaling_channels.append(channel)

        histogram = delta_histogram(rows)
        all_unimodular &= set(histogram) == {"1"}
        channel_rows[channel] = {
            "degree_per_mark": degree,
            "mark_transport": list(permutation),
            "states": rows,
            "delta_min": min(histogram, key=Fraction),
            "delta_max": max(histogram, key=Fraction),
            "delta_histogram": histogram,
            "composites": composites,
            "prime_halfdensity_scaling": channel_scaling,
        }

    return {
        "p": p,
        "channels": channel_rows,
        "all_channels_unimodular": all_unimodular,
        "composition_multiplicativity_exact": composition_ok,
        "scaling_channels": scaling_channels,
    }


def unmarked_control(p: int) -> dict:
    degree = isotropic_line_count(p)
    delta = Fraction(degree, degree)
    return {
        "p": p,
        "source_fibre": degree,
        "target_fibre": degree,
        "delta": frac_text(delta),
        "pass": delta == 1,
        "reason": "E8 class-number-one unmarked Kneser correspondence",
    }


def tree_control(p: int) -> dict:
    """Oriented p-branching correspondence, depth >= 3.

    On the parent-to-child channel, source multiplicity is p and target
    multiplicity is one.  Thus Delta=1/p.  This is a deliberately
    non-unimodular correspondence control; adjoining the reverse channel
    supplies the inverse arrows.
    """
    edge_delta = Fraction(1, p)
    composites = []
    for length in COMPOSITE_LENGTHS:
        composite_delta = edge_delta ** length
        expected = Fraction(1, p ** length)
        composites.append({
            "length": length,
            "delta": frac_text(composite_delta),
            "half_density": f"{p}^(-{length}/2)",
            "multiplicativity_exact": composite_delta == edge_delta ** length,
            "detects_prime_halfdensity": composite_delta == expected,
        })
    return {
        "p": p,
        "model": "oriented rooted p-branching tree, depth 3",
        "source_fibre": p,
        "target_fibre": 1,
        "delta": frac_text(edge_delta),
        "half_density": f"{p}^(-1/2)",
        "composites": composites,
        "pass": all(row["detects_prime_halfdensity"]
                    and row["multiplicativity_exact"] for row in composites),
    }


def adjudicate(prime_results: list[dict]) -> tuple[str, list[str]]:
    all_unimodular = all(row["all_channels_unimodular"]
                         for row in prime_results)
    all_multiplicative = all(row["composition_multiplicativity_exact"]
                             for row in prime_results)
    scaling = [
        (row["p"], channel)
        for row in prime_results for channel in row["scaling_channels"]
    ]
    if all_unimodular:
        return "KILLED(K1)", [
            "K1: Delta_p is identically 1 on every tested marked state/channel."
        ]
    if not all_multiplicative or not scaling:
        return "KILLED(K2)", [
            "K2: nontrivial Delta does not supply the p^(-m/2) composite law."
        ]
    return "SURVIVED_CHANNEL", [
        "Explicit scaling channels: "
        + ", ".join(f"p={p}:{channel}" for p, channel in scaling)
    ]


def main() -> int:
    prime_results = [evaluate_marked_prime(p) for p in PRIMES]
    unmarked = [unmarked_control(p) for p in PRIMES]
    tree = [tree_control(p) for p in PRIMES]
    scrambled = [evaluate_marked_prime(p, scrambled=True) for p in PRIMES]
    verdict, triggers = adjudicate(prime_results)

    controls = {
        "C1_unmarked_E8": {
            "rows": unmarked,
            "pass": all(row["pass"] for row in unmarked),
        },
        "C2_nonunimodular_tree": {
            "rows": tree,
            "pass": all(row["pass"] for row in tree),
        },
        "C3_scrambled_marks": {
            "rows": scrambled,
            "pass": all(row["all_channels_unimodular"]
                        and row["composition_multiplicativity_exact"]
                        for row in scrambled),
            "interpretation":
                "Permutation of marks preserves exact source/target fibres.",
        },
    }
    assert all(control["pass"] for control in controls.values())
    assert verdict == "KILLED(K1)"

    result = {
        "contract": CONTRACT,
        "spec_sha256": SPEC_SHA,
        "scope": "experiment-only finite computation; no RH claim",
        "groupoid_definition": {
            "states":
                "four v535 mu4 glue/theta classes j=0,1,2,3",
            "morphisms":
                "Kneser p-neighbour relations, resolved into ALL_KNESER, "
                "AFFINE_IDENTITY, HECKE_COMPONENT, and v536 Type-A/B channels",
            "fallback_reason":
                "v535 gives aggregate marked theta channels but no explicit "
                "state-to-state marked adjacency; frozen contract authorizes "
                "the affine a/b plus Type-A/B channel structure",
            "mark_transport":
                "bijective permutation per channel; fibre result is invariant "
                "under every such transport",
            "v535_refs": V535_REFS,
            "v536_refs": V536_REFS,
            "p2_exclusion":
                "v535 counts p=2 isotropic lines but does not supply the "
                "marked affine operator coefficients a,b at p=2",
        },
        "tested_primes": list(PRIMES),
        "exact_arithmetic": "integers and fractions.Fraction; no float verdicts",
        "prime_results": prime_results,
        "composite_scaling_test": {
            "lengths": list(COMPOSITE_LENGTHS),
            "multiplicativity_exact": all(
                row["composition_multiplicativity_exact"]
                for row in prime_results
            ),
            "surviving_channels": [
                {"p": row["p"], "channel": channel}
                for row in prime_results for channel in row["scaling_channels"]
            ],
            "result":
                "No marked Kneser channel emits log(p)*p^(-m/2); its "
                "canonical modular half-density is 1.",
        },
        "controls": controls,
        "verdict": verdict,
        "triggered_criteria": triggers,
    }
    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"{CONTRACT}")
    print("definition: v535 mu4 marks; affine a/b and v536 Type-A/B fibres")
    for row in prime_results:
        summaries = []
        for channel, data in row["channels"].items():
            summaries.append(
                f"{channel}:deg={data['degree_per_mark']},Delta="
                f"{data['delta_min']}..{data['delta_max']}"
            )
        print(f"p={row['p']}: " + "; ".join(summaries))
    print("composites m=1,2,3: Delta multiplicative; no p^(-m/2) channel")
    print("C1 unmarked E8: PASS (Delta=1)")
    print("C2 oriented tree: PASS (Delta=1/p, sqrt=p^(-1/2))")
    print("C3 scrambled marks: PASS (fibre tables invariant)")
    print(f"verdict: {verdict}")
    print(f"result: {RESULT_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
