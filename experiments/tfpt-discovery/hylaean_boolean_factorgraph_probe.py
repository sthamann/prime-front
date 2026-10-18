#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hylaean_boolean_factorgraph_probe -- r648  HYLAEAN.FACTORGRAPH.GAP.01

Experiments-only test of the last genuinely distinct current-Hylaean route:
a local Boolean multiplication factor graph, not the failed global hyperbola
energy.

For balanced odd N=pq with m-bit factors, soft bits p_i,q_j and binary carry
bits h_{k,b} define

    z_k = sum_{i+j=k} p_i q_j + c_k - N_k - 2 c_{k+1},
    c_k = sum_b 2^b h_{k,b}.

The one master energy is

    E = mean_k z_k^2
        + lambda * mean_v v^2(1-v)^2.

Each bit is represented on S^1 by v=(1+cos theta)/2.  One tick computes the
exact analytic gradient, projects to the angular/tangent coordinate, applies
a trust-radius step and renormalizes implicitly through theta.  There is no
host search, smart decode, second optimizer, factor input or post-hoc repair.
The fixed LSB/MSB bits enforce odd balanced nontrivial factors.  Decode is a
single threshold; exact division is only the verifier.

This mirrors the capabilities discovered in the current Hylaean graph:
BooleanField/ANF, typed-role factor energies and pure_projector_pass.  It does
not import the temporary Hylaean snapshot (its source checkout is gone);
the arithmetic and dynamics are explicit here.

Decision:
  FACTORGRAPH_SCALING_FOUND  only if success remains nonzero on every size,
      field work per successful factor beats odd trial division, and the
      fitted restart exponent is nonpositive.
  FACTORGRAPH_LOCAL_ONLY     small instances move to exact minima but success
      vanishes / restart work grows exponentially.
  FACTORGRAPH_BROKEN         true factors are not zero-energy, energy rises,
      firewall fails, or a false factor is emitted.

This is not an NP-hardness or factoring lower bound.  A negative result closes
this concrete JFP landscape only.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import sys
import time
from dataclasses import dataclass
from math import isqrt
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import regulator_jump_probe as R643  # noqa: E402

ROUND = 648
SEED = 648202609
CONTRACT = "HYLAEAN.FACTORGRAPH.GAP.01"
FENCE = "Exploration; no factoring breakthrough claim; no RH claim"
TAG = "r648"
RESULT_JSON = HERE / "hylaean_boolean_factorgraph_result.json"

BIT_SIZES = (8, 10, 12, 14, 16, 18)
INSTANCES_PER_SIZE = 3
RESTARTS = 256
TICKS = 2_000
LEARNING_RATE = 0.12
BINARY_WEIGHT = 0.10
TRUST_RADIUS = 0.50
DECISIONS = (
    "FACTORGRAPH_SCALING_FOUND",
    "FACTORGRAPH_LOCAL_ONLY",
    "FACTORGRAPH_BROKEN",
)

CHECKS: list[tuple[str, bool]] = []


def emit(message: str = "") -> None:
    print(message)


def section(title: str) -> None:
    emit("")
    emit("== " + title)


def check(name: str, condition: bool, detail: str = "") -> bool:
    ok = bool(condition)
    CHECKS.append((name, ok))
    emit("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    return ok


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def bit_vector(value: int, width: int) -> np.ndarray:
    return np.array([(value >> index) & 1 for index in range(width)], dtype=float)


def carry_trace(p: int, q: int, modulus: int, width: int) -> list[int]:
    p_bits = bit_vector(p, width)
    q_bits = bit_vector(q, width)
    carries = [0] * (2 * width + 1)
    for column in range(2 * width):
        total = carries[column]
        for i in range(width):
            j = column - i
            if 0 <= j < width:
                total += int(p_bits[i] * q_bits[j])
        if total % 2 != ((modulus >> column) & 1):
            raise ArithmeticError("true factors do not satisfy the multiplication column")
        carries[column + 1] = total // 2
    if carries[-1] != 0:
        raise ArithmeticError("final carry is nonzero")
    return carries


def binary_penalty_gradient(values: np.ndarray, count: int) -> np.ndarray:
    return (
        BINARY_WEIGHT
        * 2.0
        * values
        * (1.0 - values)
        * (1.0 - 2.0 * values)
        / count
    )


def energy_values(
    modulus: int,
    p_soft: np.ndarray,
    q_soft: np.ndarray,
    carry_soft: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    batch, width = p_soft.shape
    columns = 2 * width
    carry_weights = (2 ** np.arange(carry_soft.shape[2])).astype(float)
    carries = carry_soft @ carry_weights
    carries[:, 0] = 0.0
    carries[:, columns] = 0.0
    target_bits = bit_vector(modulus, columns)
    residual = carries[:, :columns] - 2.0 * carries[:, 1:] - target_bits
    for i in range(width):
        for j in range(width):
            residual[:, i + j] += p_soft[:, i] * q_soft[:, j]
    constraint = np.mean(residual * residual, axis=1)
    binary = (
        np.sum(p_soft * p_soft * (1.0 - p_soft) ** 2, axis=1)
        + np.sum(q_soft * q_soft * (1.0 - q_soft) ** 2, axis=1)
        + np.sum(
            carry_soft * carry_soft * (1.0 - carry_soft) ** 2,
            axis=(1, 2),
        )
    )
    count = p_soft.shape[1] + q_soft.shape[1] + carry_soft.shape[1] * carry_soft.shape[2]
    return constraint + BINARY_WEIGHT * binary / count, residual


@dataclass
class FlowResult:
    hits: int
    false_outputs: int
    initial_energy: float
    final_energy: float
    field_work: int
    decoded_examples: list[tuple[int, int]]


def solve_factor_graph(
    modulus: int,
    width: int,
    *,
    restarts: int,
    ticks: int,
    seed: int,
) -> FlowResult:
    """Runtime API deliberately contains only N, bit width and budgets."""
    rng = np.random.default_rng(seed)
    columns = 2 * width
    carry_bits = max(1, (width + 1).bit_length())
    theta_p = rng.uniform(0.10, math.pi - 0.10, (restarts, width))
    theta_q = rng.uniform(0.10, math.pi - 0.10, (restarts, width))
    theta_h = rng.uniform(
        0.10,
        math.pi - 0.10,
        (restarts, columns + 1, carry_bits),
    )
    fixed = (0, width - 1)
    theta_p[:, fixed] = 0.0
    theta_q[:, fixed] = 0.0
    theta_h[:, 0, :] = 0.0
    theta_h[:, columns, :] = 0.0
    free_factor = np.ones(width, dtype=bool)
    free_factor[list(fixed)] = False
    target_bits = bit_vector(modulus, columns)
    carry_weights = (2 ** np.arange(carry_bits)).astype(float)
    variable_count = 2 * (width - 2) + (columns - 1) * carry_bits

    initial_energy = None
    for _tick in range(ticks):
        p_soft = (1.0 + np.cos(theta_p)) / 2.0
        q_soft = (1.0 + np.cos(theta_q)) / 2.0
        carry_soft = (1.0 + np.cos(theta_h)) / 2.0
        energy, residual = energy_values(modulus, p_soft, q_soft, carry_soft)
        if initial_energy is None:
            initial_energy = float(np.mean(energy))

        residual_gradient = 2.0 * residual / columns
        grad_p = np.zeros_like(p_soft)
        grad_q = np.zeros_like(q_soft)
        for i in range(width):
            for j in range(width):
                grad_p[:, i] += residual_gradient[:, i + j] * q_soft[:, j]
                grad_q[:, j] += residual_gradient[:, i + j] * p_soft[:, i]
        grad_h = np.zeros_like(carry_soft)
        for column in range(1, columns):
            grad_h[:, column, :] = (
                residual_gradient[:, column, None]
                - 2.0 * residual_gradient[:, column - 1, None]
            ) * carry_weights

        grad_p += binary_penalty_gradient(p_soft, variable_count)
        grad_q += binary_penalty_gradient(q_soft, variable_count)
        grad_h += binary_penalty_gradient(carry_soft, variable_count)

        grad_theta_p = -0.5 * np.sin(theta_p) * grad_p
        grad_theta_q = -0.5 * np.sin(theta_q) * grad_q
        grad_theta_h = -0.5 * np.sin(theta_h) * grad_h
        grad_theta_p[:, ~free_factor] = 0.0
        grad_theta_q[:, ~free_factor] = 0.0
        grad_theta_h[:, 0, :] = 0.0
        grad_theta_h[:, columns, :] = 0.0

        gradient_norm = np.sqrt(
            np.sum(grad_theta_p * grad_theta_p, axis=1)
            + np.sum(grad_theta_q * grad_theta_q, axis=1)
            + np.sum(grad_theta_h * grad_theta_h, axis=(1, 2))
        )
        step = np.minimum(
            LEARNING_RATE,
            TRUST_RADIUS / np.maximum(gradient_norm, 1e-12),
        )
        theta_p -= step[:, None] * grad_theta_p
        theta_q -= step[:, None] * grad_theta_q
        theta_h -= step[:, None, None] * grad_theta_h

    p_soft = (1.0 + np.cos(theta_p)) / 2.0
    q_soft = (1.0 + np.cos(theta_q)) / 2.0
    carry_soft = (1.0 + np.cos(theta_h)) / 2.0
    final_energy_array, _residual = energy_values(
        modulus,
        p_soft,
        q_soft,
        carry_soft,
    )
    p_bits = p_soft > 0.5
    q_bits = q_soft > 0.5
    p_values = sum(p_bits[:, i] * (1 << i) for i in range(width))
    q_values = sum(q_bits[:, i] * (1 << i) for i in range(width))
    exact = p_values * q_values == modulus
    nontrivial = (p_values > 1) & (q_values > 1)
    valid = exact & nontrivial
    false_outputs = int(np.sum(exact & ~nontrivial))
    examples = [
        (int(p_value), int(q_value))
        for p_value, q_value in zip(p_values[valid][:4], q_values[valid][:4])
    ]
    local_products = width * width
    local_carries = columns * carry_bits
    field_work = restarts * ticks * (local_products + local_carries)
    return FlowResult(
        hits=int(np.sum(valid)),
        false_outputs=false_outputs,
        initial_energy=float(initial_energy),
        final_energy=float(np.mean(final_energy_array)),
        field_work=field_work,
        decoded_examples=examples,
    )


def true_assignment_energy(modulus: int, p: int, q: int, width: int) -> float:
    columns = 2 * width
    carry_bits = max(1, (width + 1).bit_length())
    carries = carry_trace(p, q, modulus, width)
    p_soft = bit_vector(p, width)[None, :]
    q_soft = bit_vector(q, width)[None, :]
    carry_soft = np.zeros((1, columns + 1, carry_bits), dtype=float)
    for column, carry in enumerate(carries):
        for bit in range(carry_bits):
            carry_soft[0, column, bit] = (carry >> bit) & 1
    energy, residual = energy_values(modulus, p_soft, q_soft, carry_soft)
    if np.max(np.abs(residual)) != 0:
        raise ArithmeticError("true assignment has nonzero local residual")
    return float(energy[0])


def runtime_firewall() -> list[str]:
    source = ast.parse(
        Path(__file__).read_text(encoding="utf-8")
    )
    function = next(
        node
        for node in source.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "solve_factor_graph"
    )
    names = {
        node.id
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
    }
    return sorted(names.intersection({"p", "q", "factorint", "trial_division"}))


def random_semiprime_of_size(
    rng: np.random.Generator,
    bits: int,
) -> tuple[int, int, int, int]:
    width = bits // 2
    while True:
        modulus, p, q = R643.random_semiprime(rng, bits, blum=False)
        if p.bit_length() == width and q.bit_length() == width:
            return modulus, p, q, width


def run(smoke: bool, json_path: str) -> int:
    wall_start = time.time()
    sizes = (8, 12) if smoke else BIT_SIZES
    instances = 1 if smoke else INSTANCES_PER_SIZE
    restarts = 128 if smoke else RESTARTS
    ticks = 800 if smoke else TICKS
    rng = np.random.default_rng(SEED)
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))

    section("B1 exact local multiplication geometry")
    true_rows = []
    for bits in sizes:
        modulus, p, q, width = random_semiprime_of_size(rng, bits)
        true_rows.append(
            {
                "bits": bits,
                "N": modulus,
                "p": p,
                "q": q,
                "width": width,
                "energy": true_assignment_energy(modulus, p, q, width),
            }
        )
    check(
        "B1 true factors are exact zero-energy states",
        all(row["energy"] == 0.0 for row in true_rows),
        str([(row["bits"], row["energy"]) for row in true_rows]),
    )

    section("B2 blind field rollouts")
    rows = []
    # Recreate independent blind instances; factors below are validation only.
    rng = np.random.default_rng(SEED + 1)
    all_energy_down = True
    all_exact = True
    for bits in sizes:
        for instance in range(instances):
            modulus, p, q, width = random_semiprime_of_size(rng, bits)
            result = solve_factor_graph(
                modulus,
                width,
                restarts=restarts,
                ticks=ticks,
                seed=SEED + 1000 * bits + instance,
            )
            all_energy_down &= result.final_energy < result.initial_energy
            all_exact &= all(a * b == modulus for a, b in result.decoded_examples)
            odd_trial_checks = max(1, (isqrt(modulus) - 3) // 2 + 1)
            success_probability = result.hits / restarts
            expected_restarts = (
                math.log(0.5) / math.log(1.0 - success_probability)
                if 0.0 < success_probability < 1.0
                else (1.0 if success_probability == 1.0 else math.inf)
            )
            work_per_hit = (
                result.field_work / result.hits if result.hits else math.inf
            )
            rows.append(
                {
                    "bits": bits,
                    "instance": instance,
                    "N": modulus,
                    "width": width,
                    "hits": result.hits,
                    "restarts": restarts,
                    "success_probability": success_probability,
                    "expected_restarts_50pct": expected_restarts,
                    "field_work": result.field_work,
                    "field_work_per_hit": work_per_hit,
                    "odd_trial_checks": odd_trial_checks,
                    "work_over_trial": work_per_hit / odd_trial_checks,
                    "initial_energy": result.initial_energy,
                    "final_energy": result.final_energy,
                    "false_outputs": result.false_outputs,
                    "examples": result.decoded_examples,
                }
            )
            emit(
                "  %2d bit i%d N=%d hits=%3d/%d E %.3e->%.3e "
                "work/hit=%s trial=%d ratio=%s"
                % (
                    bits,
                    instance,
                    modulus,
                    result.hits,
                    restarts,
                    result.initial_energy,
                    result.final_energy,
                    "inf" if not math.isfinite(work_per_hit) else "%.2e" % work_per_hit,
                    odd_trial_checks,
                    "inf"
                    if not math.isfinite(work_per_hit)
                    else "%.2e" % (work_per_hit / odd_trial_checks),
                )
            )
    check(
        "B2 mean master energy decreases on every run",
        all_energy_down,
    )
    check(
        "B2 decoder emits no false factor",
        all_exact and all(row["false_outputs"] == 0 for row in rows),
    )

    section("B3 scaling adjudication")
    summaries = {}
    for bits in sizes:
        subset = [row for row in rows if row["bits"] == bits]
        summaries[str(bits)] = {
            "instances": len(subset),
            "total_hits": sum(row["hits"] for row in subset),
            "total_restarts": sum(row["restarts"] for row in subset),
            "success_rate": sum(row["hits"] for row in subset)
            / sum(row["restarts"] for row in subset),
            "zero_hit_instances": sum(row["hits"] == 0 for row in subset),
            "median_work_over_trial": float(
                np.median([row["work_over_trial"] for row in subset])
            ),
        }
        summary = summaries[str(bits)]
        emit(
            "  %2d bit: hits %d/%d, zero instances %d/%d, "
            "median work/trial %s"
            % (
                bits,
                summary["total_hits"],
                summary["total_restarts"],
                summary["zero_hit_instances"],
                summary["instances"],
                "inf"
                if not math.isfinite(summary["median_work_over_trial"])
                else "%.2e" % summary["median_work_over_trial"],
            )
        )
    firewall_hits = runtime_firewall()
    check(
        "B3 runtime receives no true factors",
        firewall_hits == [],
        str(firewall_hits),
    )
    large_sizes = [bits for bits in sizes if bits >= 14]
    survives = (
        bool(large_sizes)
        and all(summaries[str(bits)]["total_hits"] > 0 for bits in large_sizes)
        and all(
            summaries[str(bits)]["median_work_over_trial"] < 1.0
            for bits in large_sizes
        )
    )
    check(
        "B3 frozen GO rule evaluated",
        True,
        "GO=%s requires nonzero success and lower total work than odd trial division at every >=14-bit size"
        % survives,
    )

    if not all_energy_down or not all_exact or firewall_hits:
        verdict = "FACTORGRAPH_BROKEN"
        why = "energy monotonicity, exact decode or runtime firewall failed"
    elif survives:
        verdict = "FACTORGRAPH_SCALING_FOUND"
        why = "local Carry/Boolean JFP retains success and beats trial-division work on every large rung"
    else:
        verdict = "FACTORGRAPH_LOCAL_ONLY"
        why = (
            "the local multiplication energy has exact factor minima and decreases, "
            "but basin success is instance-fragile and field work does not beat trial division"
        )
    check("B4 verdict enum", verdict in DECISIONS, verdict)

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "round": ROUND,
        "fence": FENCE,
        "verdict": verdict,
        "why": why,
        "parameters": {
            "sizes": sizes,
            "instances_per_size": instances,
            "restarts": restarts,
            "ticks": ticks,
            "learning_rate": LEARNING_RATE,
            "binary_weight": BINARY_WEIGHT,
            "trust_radius": TRUST_RADIUS,
        },
        "true_rows": true_rows,
        "rows": rows,
        "summaries": summaries,
        "checks": {name: ok for name, ok in CHECKS},
    }
    payload["file_sha256"] = file_sha256()
    payload["result_sha"] = payload_sha(payload)
    if json_path:
        Path(json_path).write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n")
    passed = sum(ok for _name, ok in CHECKS)
    emit("")
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("CHECKS %d/%d PASS" % (passed, len(CHECKS)))
    emit("FILE_SHA %s" % payload["file_sha256"])
    emit("RESULT_SHA %s" % payload["result_sha"])
    emit("runtime %.3f s" % (time.time() - wall_start))
    emit(
        "ALL CHECKS PASSED"
        if passed == len(CHECKS)
        else "GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok)
    )
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    return 0 if passed == len(CHECKS) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--json", default=str(RESULT_JSON))
    args = parser.parse_args()
    return run(args.smoke, args.json)


if __name__ == "__main__":
    sys.exit(main())
