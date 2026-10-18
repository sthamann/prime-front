#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Machine verifier for interval_cert.tex (round 465).

It regenerates all eight interval certificates, checks the sealed
decimal hulls and r459/r463 reference points, verifies the finite
linear-algebra identity on exact rationals, and audits the note's
claim boundary.

Final success line:
  INTERVAL CERTIFICATE VERIFIED -- CERTIFIED(k=5..12)
"""
from __future__ import annotations

from fractions import Fraction
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISCOVERY = os.path.join(REPO, "experiments", "tfpt-discovery")
if DISCOVERY not in sys.path:
    sys.path.insert(0, DISCOVERY)

import interval_cert_probe as S  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-35s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def exact_residual_ward() -> None:
    # H=[[2,1],[1,3]], g=[1,2], x=[1/5,3/5].
    # The residual identity equals g^T H^-1 g = 7/5 exactly.
    H = ((Fraction(2), Fraction(1)),
         (Fraction(1), Fraction(3)))
    g = (Fraction(1), Fraction(2))
    x = (Fraction(1, 5), Fraction(3, 5))
    residual = tuple(
        g[row] - sum(H[row][column] * x[column] for column in range(2))
        for row in range(2)
    )
    base = (2 * sum(g[index] * x[index] for index in range(2))
            - sum(x[row] * H[row][column] * x[column]
                  for row in range(2) for column in range(2)))
    inverse = ((Fraction(3, 5), Fraction(-1, 5)),
               (Fraction(-1, 5), Fraction(2, 5)))
    remainder = sum(
        residual[row] * inverse[row][column] * residual[column]
        for row in range(2) for column in range(2)
    )
    check("exact-residual-identity",
          base + remainder == Fraction(7, 5)
          and residual == (Fraction(0), Fraction(0)),
          "g^T H^-1 g = 7/5 exactly")


def note_audit() -> None:
    path = os.path.join(REPO, "rh", "problem", "interval_cert.tex")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = (
        r"k\in\{5,\ldots,12\}",
        r"\Rd(W_k)\succeq\tfrac12 I",
        r"native\_decide",
        r"norm\_num",
        "does not prove the frequently",
        "No RH claim",
        r"GL\_N=48",
        "DPS=70",
        "5/7",
    )
    check("note-object-and-boundary",
          all(token in text for token in tokens),
          "theorem, constants, Lean design, finite boundary")


def regenerate() -> None:
    nodes, weights, lemma = S.gl_nodes_enclosed(S.GL_N)
    check("GL-node-lemma",
          lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains_two"],
          "48 disjoint root intervals; weight sum encloses 2")
    max_a = 2**max(S.K_FULL)
    rows = S.prime_power_rows(max_a * max_a)
    results = [S.certify(k, rows, nodes, weights) for k in S.K_FULL]
    check("shape-and-source-pins",
          all(result["shape_ok"] for result in results),
          "atoms/S/cap pinned for k=5..12")
    check("outward-decimal-hulls",
          all(result["raw_inside_pin"] for result in results),
          "8/8 live enclosures inside sealed hulls")
    check("r459-r463-consistency",
          all(result["reference_inside"] for result in results),
          "8/8 point values enclosed")
    check("positive-moment-blocks",
          all(result["mu_previous"] > 0 and result["mu_full"] > 0
              for result in results),
          "validated Cholesky lower bounds all positive")
    check("qdag-strictly-below-one",
          all(result["q_lo"] > 0 and result["q_hi"] < 1
              and result["certified"] for result in results),
          "CERTIFIED(k=5..12)")
    expected_reach = (10, 12, 11, 11, 10, 10, 9, 8)
    check("chain-explosion-switch",
          tuple(result["chain_reach"] for result in results)
          == expected_reach,
          "reaches 10/10,12/12,11/14,11/16,10/36,10/40,9/44,8/48")
    check("width-pins",
          tuple(S.CERT_PINS[k] for k in S.K_FULL)
          == (
              ("0.877898027316", "0.877898027326"),
              ("0.885355701542", "0.885355701573"),
              ("0.860490813792", "0.860490813910"),
              ("0.852160102837", "0.852160103131"),
              ("0.8975761165", "0.8975761982"),
              ("0.9319617974", "0.9319619463"),
              ("0.9201637350", "0.9201641094"),
              ("0.9139227630", "0.9139233990"),
          ),
          "published intervals byte-pinned")


def main() -> int:
    print("=" * 72)
    print("verify_interval_cert.py -- round 465")
    print("probe SPEC_SHA", S.SPEC_SHA[:16])
    print("=" * 72)
    exact_residual_ward()
    note_audit()
    regenerate()
    failures = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS" %
          (len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("INTERVAL CERTIFICATE VERIFIED -- CERTIFIED(k=5..12)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
