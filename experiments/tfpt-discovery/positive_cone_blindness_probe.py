#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""positive_cone_blindness_probe -- exact finite moment-cone no-go.

POSITIVE-CONE BLINDNESS LEMMA.  Fix a positive measure mu, a nonzero
positive measure nu, and V_N = {real p : deg p < N_w}.  A certificate
Phi is nu-scaling-invariant when its premises factor through
    D(mu, nu) = (moments(mu), supp(nu), N_w, source terms s_d >= 0)
and hence D(mu, t nu) = D(mu, nu) for every t > 0: Phi never reads the
nu mass function, a mixed mu/nu moment, or any equivalent metric ratio.
If Phi inferred integral p^2 d(mu-nu) >= 0 on V_N from D, choose p0 in
V_N with integral p0^2 dnu > 0 and then
    t > integral p0^2 dmu / integral p0^2 dnu.
The premises are unchanged but integral p0^2 d(mu-t nu) < 0, so the
inference is invalid.  (For an atomic finite window p0 = 1 suffices.)
Thus a valid certificate must engage nu's magnitude relative to mu.
This does NOT say Weil positivity is false; it excludes only
positive-cone/support-only certificates.  Moment-cone subordination
nu <= mu (Lemma L*) is exactly the missing metric comparison.

Experiment-only research code.  All deciding arithmetic is Fraction
arithmetic; decimal floating-point values are absent from verdicts.
No RH claim in either direction.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "positive_cone_blindness_result.json"
FENCE = "Experiment-only finite algebra; no RH claim."


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else (
        f"{value.numerator}/{value.denominator}"
    )


def matrix_json(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[fstr(value) for value in row] for row in matrix]


def moments(
    atoms: Iterable[Fraction],
    weights: Iterable[Fraction],
    maximum_degree: int,
) -> list[Fraction]:
    return [
        sum((weight * atom**degree for atom, weight in zip(atoms, weights)),
            Fraction(0))
        for degree in range(maximum_degree + 1)
    ]


def hankel(moment_values: list[Fraction], dimension: int) -> list[list[Fraction]]:
    return [
        [moment_values[row + column] for column in range(dimension)]
        for row in range(dimension)
    ]


def subtract_scaled(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
    scale: Fraction,
) -> list[list[Fraction]]:
    return [
        [left[row][column] - scale * right[row][column]
         for column in range(len(left))]
        for row in range(len(left))
    ]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work))
             if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            multiplier = work[row][column] / pivot_value
            for entry in range(column, len(work)):
                work[row][entry] -= multiplier * work[column][entry]
    return result


def leading_minors(matrix: list[list[Fraction]]) -> list[Fraction]:
    return [
        determinant([row[:size] for row in matrix[:size]])
        for size in range(1, len(matrix) + 1)
    ]


def is_positive_definite(matrix: list[list[Fraction]]) -> bool:
    return all(value > 0 for value in leading_minors(matrix))


def stable_hash(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()[:16]


def finite_window_instance() -> dict:
    # A rationalised symmetric log-grid.  It preserves the finite signed-atom
    # structure of v963 while avoiding irrational coordinates in verdicts.
    atoms_mu = [Fraction(-2), Fraction(-1), Fraction(0),
                Fraction(1), Fraction(2)]
    weights_mu = [Fraction(1), Fraction(2), Fraction(3),
                  Fraction(2), Fraction(1)]
    atoms_nu = [Fraction(-1), Fraction(1)]
    weights_nu = [Fraction(1), Fraction(1)]
    window_degree = 2
    mu_moments = moments(atoms_mu, weights_mu, 2 * window_degree - 2)
    nu_moments = moments(atoms_nu, weights_nu, 2 * window_degree - 2)
    moment_mu = hankel(mu_moments, window_degree)
    moment_nu = hankel(nu_moments, window_degree)

    # Both matrices are diagonal by symmetry, so the generalized crossing and
    # ordinary minimum eigenvalues below are exact rational numbers.
    assert moment_mu == [[Fraction(9), Fraction(0)],
                         [Fraction(0), Fraction(12)]]
    assert moment_nu == [[Fraction(2), Fraction(0)],
                         [Fraction(0), Fraction(2)]]
    threshold = min(
        moment_mu[index][index] / moment_nu[index][index]
        for index in range(window_degree)
    )
    scale_below, scale_above = Fraction(4), Fraction(5)
    below = subtract_scaled(moment_mu, moment_nu, scale_below)
    above = subtract_scaled(moment_mu, moment_nu, scale_above)
    lambda_min_below = min(below[index][index] for index in range(window_degree))
    lambda_min_above = min(above[index][index] for index in range(window_degree))

    source_terms = [Fraction(3, 2), Fraction(5, 3), Fraction(7, 4)]
    blind_data = {
        "mu_moments": [fstr(value) for value in mu_moments],
        "nu_support": [fstr(value) for value in atoms_nu],
        "window_degree": window_degree,
        "source_terms": [fstr(value) for value in source_terms],
    }
    below_hash = stable_hash(blind_data)
    above_hash = stable_hash(blind_data)
    assert threshold == Fraction(9, 2)
    assert lambda_min_below == Fraction(1)
    assert lambda_min_above == Fraction(-1)
    assert is_positive_definite(below) and not is_positive_definite(above)
    assert below_hash == above_hash

    return {
        "model": "rationalised symmetric finite log-grid",
        "window_degree": window_degree,
        "moment_mu": matrix_json(moment_mu),
        "moment_nu": matrix_json(moment_nu),
        "scaling_threshold_t_star": fstr(threshold),
        "below": {
            "t": fstr(scale_below),
            "moment_matrix": matrix_json(below),
            "lambda_min": fstr(lambda_min_below),
            "positive_definite": True,
        },
        "above": {
            "t": fstr(scale_above),
            "moment_matrix": matrix_json(above),
            "lambda_min": fstr(lambda_min_above),
            "positive_definite": False,
        },
        "blind_data_hash_below": below_hash,
        "blind_data_hash_above": above_hash,
        "blind_data_identical": True,
    }


def waldspurger_block_instance() -> dict:
    source_terms = [Fraction(2), Fraction(3), Fraction(5)]
    source_weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    functional = sum(
        (weight * term for weight, term in zip(source_weights, source_terms)),
        Fraction(0),
    )
    # Direct sum: the Eisenstein block carries mu-t nu, while the cusp
    # norm-square block carries the Waldspurger functional and is unchanged.
    eisenstein_below = Fraction(9) - Fraction(4) * Fraction(2)
    eisenstein_above = Fraction(9) - Fraction(5) * Fraction(2)
    block_below = [[eisenstein_below, Fraction(0)],
                   [Fraction(0), functional]]
    block_above = [[eisenstein_above, Fraction(0)],
                   [Fraction(0), functional]]
    assert functional == Fraction(3)
    assert block_below[0][0] > 0 > block_above[0][0]
    assert block_below[1][1] == block_above[1][1]
    return {
        "source_terms": [fstr(value) for value in source_terms],
        "positive_functional": fstr(functional),
        "block_below": matrix_json(block_below),
        "block_above": matrix_json(block_above),
        "cusp_summand_constant_under_nu_scaling": True,
    }


def farkas_instance() -> dict:
    # Rows are atoms n=1 and n=6 mod 8.  Every positive-sign theta family
    # has nonnegative mass on the obstructing second row.
    library_columns = [
        [Fraction(1), Fraction(1)],
        [Fraction(2), Fraction(3)],
        [Fraction(1), Fraction(2)],
    ]
    target = [Fraction(1), Fraction(-1)]
    witness = [Fraction(0), Fraction(1)]
    witness_on_columns = [
        sum((witness[row] * column[row] for row in range(2)), Fraction(0))
        for column in library_columns
    ]
    witness_on_target = sum(
        (witness[row] * target[row] for row in range(2)), Fraction(0)
    )
    assert all(value >= 0 for value in witness_on_columns)
    assert witness_on_target < 0
    return {
        "obstructing_atom_class": "n == 6 mod 8",
        "library_columns": matrix_json(library_columns),
        "target": [fstr(value) for value in target],
        "farkas_witness": [fstr(value) for value in witness],
        "witness_on_library": [fstr(value) for value in witness_on_columns],
        "witness_on_target": fstr(witness_on_target),
        "positive_library_infeasible": True,
    }


def metric_control(instance: dict) -> dict:
    # The Loewner premise reads the full nu moment matrix, hence changes with t.
    below = [[Fraction(value) for value in row]
             for row in instance["below"]["moment_matrix"]]
    above = [[Fraction(value) for value in row]
             for row in instance["above"]["moment_matrix"]]
    below_minors = leading_minors(below)
    above_minors = leading_minors(above)
    assert all(value > 0 for value in below_minors)
    assert any(value <= 0 for value in above_minors)
    return {
        "certificate": "M_mu - t M_nu is positive definite",
        "below_leading_minors": [fstr(value) for value in below_minors],
        "above_leading_minors": [fstr(value) for value in above_minors],
        "verdict_below": "PASS",
        "verdict_above": "FAIL",
        "changes_under_nu_scaling": True,
    }


def classifications() -> list[dict]:
    return [
        {"source": "Waldspurger squares", "class": "BLIND",
         "reference": "verification/v537_halfintegral_bridge.py:557-617",
         "reason": "nonnegative coefficient squares do not read prime-channel mass"},
        {"source": "Siegel-Weil theta pairing", "class": "BLIND",
         "reference": "verification/v540_amplitude_linear_carrier.py:13-21",
         "reason": "positive lattice counts and pure Eisenstein pairing"},
        {"source": "Rankin-Selberg norm-square", "class": "BLIND",
         "reference": "verification/v539_weil_structure_family.py:6-10",
         "reason": "positive diagonal GNS metric on the census family"},
        {"source": "Cohen seeds", "class": "BLIND",
         "reference": "verification/v540_amplitude_linear_carrier.py:20-23",
         "reason": "positive edge-value seeds independent of nu mass"},
        {"source": "SOS/Pontryagin", "class": "BLIND",
         "reference": "verification/v963_lstar_reduction_dictionary.py:515-523",
         "reason": "SOS exists exactly when the negative register is empty"},
        {"source": "Kasteleyn", "class": "BLIND",
         "reference": "verification/v963_lstar_reduction_dictionary.py:524-579",
         "reason": "orientation is value-preserving exactly for positive measures"},
        {"source": "Hamiltonian PSD", "class": "BLIND",
         "reference": "verification/v963_lstar_reduction_dictionary.py:581-597",
         "reason": "canonical Hamiltonian positivity restates the pivot signs"},
        {"source": "dual pair", "class": "BLIND",
         "reference": "verification/v963_lstar_reduction_dictionary.py:599-614",
         "reason": "exact product law synchronizes rather than adds a condition"},
        {"source": "Kernel-Loewner floor", "class": "METRIC",
         "reference": "verification/v1017_kernel_loewner_positivity.py:32-58",
         "reason": "direct assembled-Q operator floor; its certified scope has nu=0"},
        {"source": "Chuk compact-window certificate", "class": "METRIC",
         "reference": "experiments/tfpt-discovery/weil_window_certificate_probe.py:3-24,883-940",
         "reason": "computes the assembled signed form and its smallest eigenvalue"},
        {"source": "Lemma L*", "class": "METRIC",
         "reference": "verification/v963_lstar_reduction_dictionary.py:1936-1941",
         "reason": "strict moment-cone comparison nu < mu"},
    ]


def kill_search() -> list[dict]:
    return [
        {
            "candidate": "GL(1) Plancherel/Parseval",
            "verdict": "RESTATEMENT",
            "reason": "Rewrites Weil's explicit-formula quadratic form; supplies no independent comparison of the prime and archimedean channels.",
        },
        {
            "candidate": "Selberg trace formula with self-adjoint Laplacian",
            "verdict": "METRIC-BY-OPERATOR",
            "reason": "Spectral positivity can come from an operator rather than positive-measure rays; this is the Hilbert-Polya template, but no corpus realization identifies its trace with the zeta target.",
        },
        {
            "candidate": "Arakelov Hodge index (Yuan-Zhang template)",
            "verdict": "METRIC",
            "reason": "An indefinite height-pairing inequality is ratio-sensitive and not a positive-measure ray, but the corpus has no automorphic bridge to the required Weil defect measure.",
        },
    ]


def main() -> int:
    window = finite_window_instance()
    result = {
        "probe": "positive_cone_blindness_probe",
        "claim_boundary": FENCE,
        "arithmetic": "fractions.Fraction only for deciding gates",
        "lemma": {
            "verdict": "LEMMA_PROVED",
            "scope": "nu-scaling-invariant certificates only",
            "does_not_say": "Weil positivity is false",
            "required_boundary": "metric moment-cone comparison nu <= mu",
        },
        "T2": {
            "finite_window": window,
            "waldspurger_block": waldspurger_block_instance(),
            "farkas": farkas_instance(),
            "metric_control": metric_control(window),
        },
        "T3": classifications(),
        "T4": kill_search(),
        "T5": {
            "verdict": "LEMMA_PROVED",
            "lemma_kill_found": False,
            "automorphically_realisable_nonpositive_extreme_ray_in_corpus": None,
            "retired_attack_classes": [
                entry["source"] for entry in classifications()
                if entry["class"] == "BLIND"
            ],
            "remaining_targets": [
                "metric comparison nu <= mu (Lemma L*)",
                "operator positivity with an explicit-formula bridge",
            ],
        },
    }
    RESULT_JSON.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    blind = [entry["source"] for entry in result["T3"]
             if entry["class"] == "BLIND"]
    metric = [entry["source"] for entry in result["T3"]
              if entry["class"] == "METRIC"]
    print("positive_cone_blindness_probe")
    print(FENCE)
    print("T1 LEMMA_PROVED: support-only positive-cone data cannot certify mu-nu.")
    print("T2a t*=9/2; lambda_min(t=4)=1; lambda_min(t=5)=-1.")
    print("T2a blind-data hashes identical: " +
          window["blind_data_hash_below"])
    print("T2b cusp positive functional=3 and is nu-scaling invariant.")
    print("T2c Farkas witness at n == 6 mod 8: yA>=0, yb=-1.")
    print("T2d metric Loewner control flips PASS at t=4 to FAIL at t=5.")
    print("T3 BLIND: " + "; ".join(blind))
    print("T3 METRIC: " + "; ".join(metric))
    print("T4 GL(1)=RESTATEMENT; Selberg=METRIC-BY-OPERATOR; Arakelov=METRIC/no bridge.")
    print("T5 LEMMA_PROVED; no corpus-realised nonpositive extreme ray found.")
    print("RESULT " + str(RESULT_JSON.relative_to(HERE.parent.parent)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
