"""Deterministic fitness functions for the selected-window evolution tool."""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

import numpy as np


VIOLATION_PENALTY = 1.0e6
EPSILON = 1.0e-15


@dataclass(frozen=True)
class FormulaProgram:
    name: str
    source: str
    evaluate: Callable[[dict[str, float]], float]


def second_difference_metrics(values: np.ndarray, spacing: float) -> dict[str, float]:
    """Discrete C2 surrogates for an even piecewise-linear correlation."""
    values = np.asarray(values, dtype=float)
    first = np.diff(values) / spacing
    second = np.diff(values, n=2) / (spacing * spacing)
    return {
        "sup_d2": float(np.max(np.abs(second))) if second.size else 0.0,
        "l1_d2": float(np.sum(np.abs(second)) * spacing),
        "h2": float(
            math.sqrt(
                np.sum(values * values) * spacing
                + np.sum(first * first) * spacing
                + np.sum(second * second) * spacing
            )
        ),
        "boundary_slope": float(abs(first[-1] - first[0])) if first.size else 0.0,
        "mass": float(np.sum(np.abs(values)) * spacing),
    }


def rate_programs() -> list[FormulaProgram]:
    """Closed-form candidate library; constants are evolved separately."""
    return [
        FormulaProgram("sup_d2", "C(g)=c*||g''||_inf", lambda m: m["sup_d2"]),
        FormulaProgram("l1_d2", "C(g)=c*integral|g''|", lambda m: m["l1_d2"]),
        FormulaProgram("h2", "C(g)=c*||g||_H2", lambda m: m["h2"]),
        FormulaProgram(
            "em_boundary",
            "C(g)=c*|g'(b)-g'(0)|",
            lambda m: m["boundary_slope"],
        ),
        FormulaProgram(
            "hybrid",
            "C(g)=c*(integral|g''|+||g||_H2)",
            lambda m: m["l1_d2"] + m["h2"],
        ),
    ]


def fit_rate_program(
    program: FormulaProgram,
    rows: list[dict],
    constants: list[float],
) -> dict:
    """Minimise a valid majorant, with a hard penalty for any violation."""
    exact_required = max(
        row["err_over_delta2"] / max(program.evaluate(row["metrics"]), EPSILON)
        for row in rows
    )
    constants = sorted({*constants, exact_required * (1.0 + 1.0e-12)})
    best = None
    for constant in constants:
        ratios = []
        violations = 0
        for row in rows:
            bound = constant * max(program.evaluate(row["metrics"]), EPSILON)
            ratio = row["err_over_delta2"] / bound
            ratios.append(ratio)
            violations += int(ratio > 1.0 + 1.0e-12)
        worst = max(ratios)
        score = constant + VIOLATION_PENALTY * violations + max(0.0, worst - 1.0)
        candidate = {
            "program": program.name,
            "source": program.source,
            "constant": float(constant),
            "worst_normalized_ratio": float(worst),
            "violations": violations,
            "fitness": float(score),
        }
        if best is None or candidate["fitness"] < best["fitness"]:
            best = candidate
    assert best is not None
    return best


def jackson_programs() -> list[FormulaProgram]:
    return [
        FormulaProgram(
            "jackson_sup_d2",
            "E_n(g)<=c*||g''||_inf/n^2",
            lambda m: m["sup_d2"],
        ),
        FormulaProgram(
            "jackson_l1_d2",
            "E_n(g)<=c*integral|g''|/n^2",
            lambda m: m["l1_d2"],
        ),
        FormulaProgram(
            "jackson_h2",
            "E_n(g)<=c*||g||_H2/n^2",
            lambda m: m["h2"],
        ),
    ]


def fit_jackson_program(program: FormulaProgram, rows: list[dict]) -> dict:
    needed = []
    for row in rows:
        scale = max(program.evaluate(row["metrics"]), EPSILON)
        needed.append(row["sup_error"] * row["degree"] ** 2 / scale)
    constant = max(needed)
    return {
        "program": program.name,
        "source": program.source,
        "constant": float(constant),
        "worst_normalized_ratio": float(
            max(
                row["sup_error"]
                / max(constant * program.evaluate(row["metrics"]) / row["degree"] ** 2, EPSILON)
                for row in rows
            )
        ),
        "fitness": float(constant),
    }


def threshold_classifier_programs(feature_names: list[str], train: list[dict]) -> list[dict]:
    """Evolve one-feature thresholds and constants as executable programs."""
    candidates = [
        {"source": "return True", "feature": None, "threshold": None, "direction": 1},
        {"source": "return False", "feature": None, "threshold": None, "direction": -1},
    ]
    for feature in feature_names:
        values = sorted({float(row[feature]) for row in train})
        cuts = values[:1] + [
            0.5 * (left + right) for left, right in zip(values, values[1:])
        ] + values[-1:]
        for cut in cuts:
            candidates.append(
                {
                    "source": f"return {feature} <= {cut:.17g}",
                    "feature": feature,
                    "threshold": cut,
                    "direction": -1,
                }
            )
            candidates.append(
                {
                    "source": f"return {feature} >= {cut:.17g}",
                    "feature": feature,
                    "threshold": cut,
                    "direction": 1,
                }
            )
    return candidates


def predict(program: dict, row: dict) -> bool:
    feature = program["feature"]
    if feature is None:
        return program["direction"] > 0
    value = float(row[feature])
    if program["direction"] > 0:
        return value >= float(program["threshold"])
    return value <= float(program["threshold"])


def accuracy(program: dict, rows: list[dict]) -> float:
    return float(np.mean([predict(program, row) == bool(row["good"]) for row in rows]))
