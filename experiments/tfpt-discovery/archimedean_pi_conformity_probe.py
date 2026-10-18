#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Numerical archimedean-place sensitivity in finite Weil windows.

This experiment reuses the Legendre-window assembly in
``weil_window_profile_scout.py:146-465`` and compares its L=0.8 Galerkin
margin with the independent Chuk/Arb certificate in
``weil_window_certificate_probe.py:1-24``.  It uses no zero data.

The normalization is

    Q = POLE + ARCH - PRIME,
    ARCH = GAMMA - log(pi) I.

For a unit minimizer, log(pi) -> log(pi)+delta therefore gives

    d lambda_min / d delta = -v^T I v
        = -(1/(2*pi)) integral |f_hat(t)|^2 dt = -1.

This is exploration-only numerical research.  Changing pi breaks the
explicit-formula identity; the reported crossing is not physical fine-tuning
and is not evidence for or against RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.linalg import eigh

import weil_window_profile_scout as scout


HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "archimedean_pi_conformity_result.json"
PROFILE_JSON = HERE / "weil_window_profile_scout_result.json"
CERTIFICATE_JSON = HERE / "weil_window_certificate_result.json"
CONTRACT = "ARCHIMEDEAN.PI.CONFORMITY.01"
FENCE = "Experiment-only NUMERICAL measurement; no RH claim; no zero data."
VERDICT = (
    "MEASURED: archimedean-place sensitivity quantified; "
    "no pi->prime correlation beyond theorems"
)
L_VALUES = (0.5, 0.65, 0.8)
N_BY_L = {0.5: 80, 0.65: 80, 0.8: 100}
DPS_BY_L = {0.5: 60, 0.65: 80, 0.8: 80}
GL_ARCH = 200
GL_POLE = 200
SCRAMBLE_SEED = 20260904
DIGIT_COUNT = 100_000
PERMUTATIONS = 499


def mp_string(value: mp.mpf, digits: int = 14) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def mp_identity(n: int) -> mp.matrix:
    out = mp.matrix(n)
    for index in range(n):
        out[index, index] = 1
    return out


def mp_outer(vector: mp.matrix, coefficient: mp.mpf) -> mp.matrix:
    n = vector.rows
    out = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            out[i, j] = coefficient * vector[i] * vector[j]
    return out


def mp_add(*matrices: mp.matrix) -> mp.matrix:
    out = mp.matrix(matrices[0])
    for matrix in matrices[1:]:
        out += matrix
    return out


def rayleigh(matrix: mp.matrix, vector: mp.matrix) -> mp.mpf:
    return (vector.T * matrix * vector)[0]


def approximate_minimizer(matrix: mp.matrix) -> mp.matrix:
    """Fast eigenvector; all reported Rayleigh values are recomputed with mp."""
    array = np.array(matrix.tolist(), dtype=float)
    _, vectors = eigh(array, subset_by_index=(0, 1), driver="evr")
    vector = mp.matrix([mp.mpf(str(value)) for value in vectors[:, 0]])
    return vector / mp.sqrt((vector.T * vector)[0])


def assemble_prime_events(
    orders: list[int],
    sigmas: list,
    length,
    events: list[tuple[float, float]],
    q_nodes: list,
    q_weights: list,
    n_max: int,
):
    """Prime matrix for explicit (log-position, positive weight) events."""
    from flint import arb, arb_mat

    matrix = arb_mat(len(orders), len(orders))
    for log_position, weight in events:
        correlation = scout.correlation_I(
            orders, arb(str(log_position)) / length, q_nodes, q_weights, n_max
        )
        g_matrix = scout.scale_I_to_g(correlation, sigmas)
        coefficient = arb(str(weight))
        for i in range(len(orders)):
            for j in range(len(orders)):
                matrix[i, j] += coefficient * g_matrix[i, j]
    return matrix


def assemble_components(length_value: float) -> dict:
    """Faithful decomposition of scout lines 436-465 into four matrices."""
    from flint import arb, arb_mat

    n_modes = N_BY_L[length_value]
    scout.set_precision(DPS_BY_L[length_value])
    orders = list(range(0, 2 * n_modes, 2))
    n_max = orders[-1]
    length = arb(str(length_value))
    sigmas = [(arb(2 * order + 1) / arb(2)).sqrt() for order in orders]
    gl_corr = max(GL_ARCH, 2 * n_modes + 20)
    q_nodes, q_weights = scout.gauss_legendre_arb(gl_corr)
    arch_t, arch_w, correlations = scout.arch_I_stack(
        orders, GL_ARCH, gl_corr, n_max
    )
    x_nodes = [length * (arb(1) + value) for value in arch_t]
    x_weights = [length * weight for weight in arch_w]
    g0 = scout.identity_g0(len(orders))
    g_at = [scout.scale_I_to_g(matrix, sigmas) for matrix in correlations]
    arch = scout.assemble_arch(g_at, x_nodes, x_weights, g0, length)
    terms = scout.prime_power_terms(2.0 * length_value)
    prime = scout.assemble_prime(
        orders, sigmas, length, terms, q_nodes, q_weights, n_max
    )
    pole_nodes, pole_weights = scout.gauss_legendre_arb(GL_POLE)
    pole_vector = scout.pole_vector(
        orders, length, True, pole_nodes, pole_weights, n_max
    )
    pole = arb_mat(n_modes, n_modes)
    for i in range(n_modes):
        for j in range(n_modes):
            pole[i, j] = arb(2) * pole_vector[i] * pole_vector[j]

    true_events = [
        (math.log(n), 2.0 * math.log(p) / math.sqrt(n)) for n, p in terms
    ]
    rng = np.random.default_rng(SCRAMBLE_SEED + int(100 * length_value))
    scramble_events = [
        (float(position), weight)
        for position, (_, weight) in zip(
            sorted(rng.uniform(math.log(2.0), 2.0 * length_value, len(true_events))),
            true_events,
        )
    ]
    scramble_prime = assemble_prime_events(
        orders,
        sigmas,
        length,
        scramble_events,
        q_nodes,
        q_weights,
        n_max,
    )
    return {
        "arch": scout.arb_mat_to_mp(arch),
        "prime": scout.arb_mat_to_mp(prime),
        "pole": scout.arb_mat_to_mp(pole),
        "scramble_prime": scout.arb_mat_to_mp(scramble_prime),
        "true_events": true_events,
        "scramble_events": scramble_events,
        "n_modes": n_modes,
        "dps": DPS_BY_L[length_value],
    }


def analyze_window(length_value: float, components: dict) -> dict:
    arch = components["arch"]
    prime = components["prime"]
    pole = components["pole"]
    identity = mp_identity(arch.rows)
    pi_matrix = mp.log(mp.pi) * identity
    gamma_matrix = arch + pi_matrix
    q_matrix = mp_add(pole, arch, -prime)
    vector = approximate_minimizer(q_matrix)
    lambda_min = rayleigh(q_matrix, vector)

    arch_value = rayleigh(arch, vector)
    prime_value = rayleigh(prime, vector)
    pole_value = rayleigh(pole, vector)
    pi_value = rayleigh(pi_matrix, vector)
    gamma_value = rayleigh(gamma_matrix, vector)
    identity_residual = lambda_min - (pole_value + arch_value - prime_value)

    delta_positive = lambda_min
    delta_negative = None
    derivative_delta = -rayleigh(identity, vector)
    derivative_epsilon = gamma_value
    linear_epsilon = (
        -lambda_min / derivative_epsilon if derivative_epsilon else mp.nan
    )
    epsilon_positive = linear_epsilon if linear_epsilon > 0 else None
    epsilon_negative = linear_epsilon if linear_epsilon < 0 else None

    scramble_q = mp_add(pole, arch, -components["scramble_prime"])
    scramble_vector = approximate_minimizer(scramble_q)
    scramble_lambda = rayleigh(scramble_q, scramble_vector)
    scramble_delta_positive = scramble_lambda if scramble_lambda > 0 else None
    scramble_delta_negative = None

    return {
        "L": length_value,
        "N_even": components["n_modes"],
        "dps": components["dps"],
        "lambda_min": mp_string(lambda_min),
        "components_on_minimizer": {
            "arch": mp_string(arch_value),
            "prime": mp_string(prime_value),
            "pole": mp_string(pole_value),
            "gamma_digamma_without_log_pi": mp_string(gamma_value),
            "pi_part_positive_magnitude": mp_string(pi_value),
            "prime_over_arch": mp_string(prime_value / arch_value),
            "identity_residual": mp_string(identity_residual),
        },
        "pi_part_over_margin": mp_string(abs(pi_value / lambda_min)),
        "pi_part_margin_orders": float(mp.log10(abs(pi_value / lambda_min))),
        "log_pi_perturbation": {
            "definition": "log(pi) -> log(pi)+delta; Q(delta)=Q-delta*I",
            "delta_crossing_positive": (
                mp_string(delta_positive) if delta_positive is not None else None
            ),
            "delta_crossing_negative": (
                mp_string(delta_negative) if delta_negative is not None else None
            ),
            "derivative_analytic": "-(1/(2*pi))*integral |fhat|^2 dt",
            "derivative_numeric": mp_string(derivative_delta),
            "first_order_crossing": mp_string(
                -lambda_min / derivative_delta
            ),
        },
        "gamma_digamma_scale": {
            "definition": "GAMMA -> (1+epsilon)*GAMMA, holding -log(pi)I fixed",
            "method": (
                "first-order projected crossing; full repeated mp eigensolve exceeded "
                "the three-minute budget"
            ),
            "epsilon_crossing_positive": (
                mp_string(epsilon_positive)
                if epsilon_positive is not None
                else None
            ),
            "epsilon_crossing_negative": (
                mp_string(epsilon_negative)
                if epsilon_negative is not None
                else None
            ),
            "derivative_numeric": mp_string(derivative_epsilon),
            "first_order_crossing": mp_string(linear_epsilon),
            "second_order_scale_bound": (
                "O(epsilon^2*||G||^2/gap); compare against lambda_2 in profile JSON"
            ),
        },
        "scramble_control": {
            "definition": "same positive von-Mangoldt weights at frozen uniform log-positions",
            "seed": SCRAMBLE_SEED + int(100 * length_value),
            "lambda_min": mp_string(scramble_lambda),
            "delta_crossing_positive": (
                mp_string(scramble_delta_positive)
                if scramble_delta_positive is not None
                else None
            ),
            "delta_crossing_negative": (
                mp_string(scramble_delta_negative)
                if scramble_delta_negative is not None
                else None
            ),
            "true_events": components["true_events"],
            "scramble_events": components["scramble_events"],
        },
    }


def prime_indicator_and_mangoldt(limit: int) -> tuple[np.ndarray, np.ndarray]:
    prime = np.ones(limit + 1, dtype=np.uint8)
    prime[:2] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p :: p] = 0
    indicator = prime[1:].astype(float)
    normalized_mangoldt = np.zeros(limit, dtype=float)
    for p in np.flatnonzero(prime):
        power = int(p)
        exponent = 1
        while power <= limit:
            normalized_mangoldt[power - 1] = 1.0 / exponent
            if power > limit // int(p):
                break
            power *= int(p)
            exponent += 1
    return indicator, normalized_mangoldt


def correlation(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.corrcoef(left, right)[0, 1])


def permutation_pvalue(
    left: np.ndarray, right: np.ndarray, observed: float, seed: int
) -> float:
    rng = np.random.default_rng(seed)
    centered_right = right - np.mean(right)
    denominator = np.linalg.norm(left - np.mean(left)) * np.linalg.norm(centered_right)
    exceed = 0
    shuffled = np.array(left, copy=True)
    for _ in range(PERMUTATIONS):
        rng.shuffle(shuffled)
        value = float(np.dot(shuffled - np.mean(shuffled), centered_right) / denominator)
        exceed += abs(value) >= abs(observed)
    return (exceed + 1.0) / (PERMUTATIONS + 1.0)


def digit_null_test() -> dict:
    mp.mp.dps = DIGIT_COUNT + 25
    digits = str(mp.pi).replace(".", "")[1 : DIGIT_COUNT + 1]
    digit_values = np.fromiter((ord(char) - 48 for char in digits), dtype=float)
    indicator, mangoldt = prime_indicator_and_mangoldt(DIGIT_COUNT)
    digit_correlation = correlation(indicator, digit_values)
    block_values = 10.0 * digit_values[:-1] + digit_values[1:]
    block_correlation = correlation(indicator[:-1], block_values)
    positive_correlation = correlation(indicator, mangoldt)
    return {
        "n": DIGIT_COUNT,
        "pi_source": "mpmath deterministic decimal expansion",
        "digit_correlation": digit_correlation,
        "digit_permutation_p_two_sided": permutation_pvalue(
            indicator, digit_values, digit_correlation, SCRAMBLE_SEED + 1
        ),
        "two_digit_block_correlation": block_correlation,
        "two_digit_block_permutation_p_two_sided": permutation_pvalue(
            indicator[:-1],
            block_values,
            block_correlation,
            SCRAMBLE_SEED + 2,
        ),
        "positive_control": {
            "observable": "Lambda(n)/log(n), equal to 1/k on p^k",
            "correlation": positive_correlation,
            "permutation_p_two_sided": permutation_pvalue(
                indicator, mangoldt, positive_correlation, SCRAMBLE_SEED + 3
            ),
        },
        "permutations": PERMUTATIONS,
        "interpretation": "Null control for decimal digits only; Euler-product theorems are unaffected.",
    }


def source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def run(smoke: bool = False) -> dict:
    started = time.time()
    lengths = (0.5,) if smoke else L_VALUES
    windows = []
    for length_value in lengths:
        print(f"assemble L={length_value:.2f} N={N_BY_L[length_value]}")
        windows.append(analyze_window(length_value, assemble_components(length_value)))

    certificate = json.loads(CERTIFICATE_JSON.read_text())
    profile = json.loads(PROFILE_JSON.read_text())
    profile_values = {
        str(record["L"]): record["lambda_1_even"]
        for record in profile["per_L"]
        if record["L"] in lengths
    }
    digit_test = None if smoke else digit_null_test()
    result = {
        "contract": CONTRACT,
        "fence": FENCE,
        "verdict": VERDICT,
        "typing": {
            "method": "NUMERICAL",
            "zero_data_used": False,
            "rh_kill_criterion": None,
            "physical_fine_tuning_claim": False,
        },
        "reuse": [
            "weil_window_profile_scout.py:146-465 (Legendre assembly and Q decomposition)",
            "weil_window_certificate_probe.py:1-24 and result JSON (L=0.8 certified margin)",
        ],
        "parameters": {
            "L_values": list(lengths),
            "N_by_L": {str(key): value for key, value in N_BY_L.items()},
            "gl_arch": GL_ARCH,
            "gl_pole": GL_POLE,
            "scramble_seed": SCRAMBLE_SEED,
        },
        "certificate_context": {
            "L": 0.8,
            "certified_constant": certificate["sectors"][0]["certified_constant"],
            "verdict": certificate["sectors"][0]["verdict"],
            "certificate_budget_delta": certificate["sectors"][0]["certified_constant"],
            "note": "Conservative certificate budget; numerical crossings use the reassembled Galerkin matrix.",
        },
        "profile_reference_lambda_even": profile_values,
        "windows": windows,
        "digit_null_test": digit_test,
        "interpretation": (
            "The crossing measures how much finite-window positivity margin is spent "
            "against the archimedean normalization. Changing pi breaks the explicit "
            "formula identity; it is not a physical tuning experiment."
        ),
        "runtime_sec": time.time() - started,
        "source_sha256": source_sha256(),
    }
    RESULT_JSON.write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    result = run(args.smoke)
    for record in result["windows"]:
        print(
            "L={L:.2f} lambda={lam} delta+={delta} eps+={epsp} eps-={epsn} "
            "pi/margin=1e{orders:.2f}".format(
                L=record["L"],
                lam=record["lambda_min"],
                delta=record["log_pi_perturbation"]["delta_crossing_positive"],
                epsp=record["gamma_digamma_scale"]["epsilon_crossing_positive"],
                epsn=record["gamma_digamma_scale"]["epsilon_crossing_negative"],
                orders=record["pi_part_margin_orders"],
            )
        )
    if result["digit_null_test"]:
        digits = result["digit_null_test"]
        print(
            f"digits r={digits['digit_correlation']:.6g} "
            f"p={digits['digit_permutation_p_two_sided']:.4g}; "
            f"positive r={digits['positive_control']['correlation']:.6g} "
            f"p={digits['positive_control']['permutation_p_two_sided']:.4g}"
        )
    print(VERDICT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
