#!/usr/bin/env python3
"""Program evolution over RH-neutral selected-window measurements."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
import time
from pathlib import Path

import numpy as np
from numpy.polynomial import Chebyshev, Legendre
from scipy.signal.windows import dpss

HERE = Path(__file__).resolve().parent
DISCOVERY = HERE.parent
REPO = DISCOVERY.parent.parent
PROBLEM = REPO / "rh" / "problem"
CATALOG = REPO / "rh" / "catalog"
for import_path in (HERE, DISCOVERY, PROBLEM, CATALOG):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

import cofinal_family_probe as COFINAL  # noqa: E402
import deep_builder_probe as BUILDER  # noqa: E402
import quadrep_probe as QUAD  # noqa: E402
import verify_lstar_instance as INSTANCE  # noqa: E402
from fitness import (  # noqa: E402
    accuracy,
    fit_jackson_program,
    fit_rate_program,
    jackson_programs,
    rate_programs,
    second_difference_metrics,
    threshold_classifier_programs,
)
from openai_service import OpenAIService  # noqa: E402

RESULTS = HERE / "results"
RESULT_PATH = RESULTS / "evolution_result.json"
PROPOSAL_PATH = RESULTS / "proposal_log.json"
PROFILE_RESULT = DISCOVERY / "weil_window_profile_scout_result.json"
SEED = 20260904
BUDGET_USD = 25.0
WALL_LIMIT_SECONDS = 45.0 * 60.0
TOLERANCE = 1.0e-11
SELECTED_K = tuple(range(5, 17))
RATE_K = tuple(range(5, 17))
PROFILE_LENGTHS = (0.5, 0.65, 0.8, 1.0)


class StopEvolution(RuntimeError):
    pass


def check_wall(started: float) -> None:
    if time.monotonic() - started > WALL_LIMIT_SECONDS:
        raise StopEvolution("wall-clock limit reached")


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def firewall() -> None:
    source = Path(__file__).read_text(encoding="utf-8") + (HERE / "fitness.py").read_text(encoding="utf-8")
    assert all(marker not in source.replace(assertion, "") for marker in ("zero", "gamma_", "riemann_" + "zeros") for assertion in [next(line for line in source.splitlines() if "assert all(marker" in line)])


def test_profiles() -> list[dict]:
    count = 64
    coordinate = np.linspace(-1.0, 1.0, count, endpoint=False) + 1.0 / count
    profiles: list[tuple[str, np.ndarray]] = []
    for width in (0.20, 0.35, 0.50):
        profiles.append((f"gaussian_{width:.2f}", np.exp(-0.5 * (coordinate / width) ** 2)))
    profiles.append(("legendre_window", (1.0 - coordinate**2) * Legendre.basis(2)(coordinate)))
    profiles.append(("prolate_dpss", dpss(count, 3.0, Kmax=1, sym=True)[0]))
    bump = np.exp(-1.0 / np.maximum(1.0 - coordinate**2, 1.0e-12))
    profiles.append(("smooth_bump", bump))
    return [
        {"name": name, "x": values / max(float(np.linalg.norm(values)), 1.0e-15)}
        for name, values in profiles
    ]


def correlation_data(profile: dict, mesh_exp: int = 5) -> dict:
    spacing = 2.0 ** (-mesh_exp)
    acf = QUAD.acf_of(profile["x"], spacing)
    support = (len(acf) - 1) * spacing
    return {
        "name": profile["name"],
        "mesh_exp": mesh_exp,
        "spacing": spacing,
        "acf": acf,
        "support": support,
        "metrics": second_difference_metrics(acf, spacing),
    }


def classical_arch(data: dict) -> float:
    from extraction_joint_probe import arch_classical, g_pl

    evaluate = lambda u: g_pl(data["acf"], data["spacing"], u)
    return float(arch_classical(evaluate, data["support"]))


def selected_arch(data: dict, k: int) -> dict:
    shape = COFINAL.lean_shape(k)
    coefficients = INSTANCE.arch_lags(shape["M"], shape["D"])
    evaluate = lambda u: QUAD.to_fun(data["acf"], data["spacing"], u)
    value = float(coefficients[0] * evaluate(0.0))
    for index in range(1, shape["m"] + 1):
        value += 2.0 * float(coefficients[index] * evaluate(index * shape["D"]))
    return {"k": k, "delta": shape["D"], "arch_read": value}


def evolve_rate(proposals: list[dict], started: float) -> dict:
    rows = []
    for profile in test_profiles():
        data = correlation_data(profile)
        reference = classical_arch(data)
        for k in RATE_K:
            check_wall(started)
            selected = selected_arch(data, k)
            error = abs(selected["arch_read"] - reference)
            rows.append(
                {
                    "profile": data["name"],
                    "k": k,
                    "delta": selected["delta"],
                    "error": error,
                    "err_over_delta2": error / selected["delta"] ** 2,
                    "metrics": data["metrics"],
                }
            )
    constants = sorted(
        {
            1.0 / 12.0,
            math.pi**2 / 6.0,
            *[2.0 ** (power / 4.0) for power in range(-24, 33)],
        }
    )
    fitted = [fit_rate_program(program, rows, constants) for program in rate_programs()]
    proposals.extend({"target": "T1", **candidate} for candidate in fitted)
    best = min(fitted, key=lambda item: item["fitness"])
    by_profile = {}
    for name in sorted({row["profile"] for row in rows}):
        sample = [row for row in rows if row["profile"] == name]
        ratios = [row["err_over_delta2"] for row in sample]
        distinct = []
        for row in sample:
            if not distinct or abs(row["delta"] - distinct[-1]["delta"]) > 1.0e-15:
                distinct.append({"k": row["k"], "delta": row["delta"], "ratio": row["err_over_delta2"]})
        by_profile[name] = {
            "ratio_min": min(ratios),
            "ratio_max": max(ratios),
            "distinct_mesh_rows": distinct,
        }
    return {"best": best, "candidates": fitted, "rows": rows, "by_profile": by_profile}


def evolve_polynomial(proposals: list[dict]) -> dict:
    rows = []
    for profile in test_profiles():
        data = correlation_data(profile)
        sample_u = np.linspace(0.0, data["support"], 2001)
        sample_g = QUAD.to_fun(data["acf"], data["spacing"], sample_u)
        for k in (5, 9, 16):
            degree = COFINAL.lean_shape(k)["Nw"] - 1
            fit = Chebyshev.fit(sample_u, sample_g, degree, domain=[0.0, data["support"]])
            sup_error = float(np.max(np.abs(fit(sample_u) - sample_g)))
            rows.append(
                {
                    "profile": data["name"],
                    "k": k,
                    "degree": degree,
                    "sup_error": sup_error,
                    "metrics": data["metrics"],
                }
            )
    fitted = [fit_jackson_program(program, rows) for program in jackson_programs()]
    proposals.extend({"target": "T2", **candidate} for candidate in fitted)
    return {
        "best": min(fitted, key=lambda item: item["fitness"]),
        "candidates": fitted,
        "rows": rows,
        "type_check": (
            "Uniform polynomial error is not the scalar selectedReadQuadratic "
            "dictionary required by the Lean proposition."
        ),
    }


def selected_spectral_row(k: int) -> dict:
    shape = COFINAL.lean_shape(k)
    measure = COFINAL.mz_from_shape(shape)
    bx, bw, by, bv = COFINAL.border_from_shape(shape)
    depth = int(measure["Nw"])
    pack = BUILDER.bord_pack_slim(
        measure["xp"], measure["wp"], measure["yn"], measure["vn"],
        bx, bw, by, bv, depth, require_pos=False,
    )
    if not pack.get("ok"):
        return {
            "k": k, "delta": shape["D"], "window_length": shape["alpha"],
            "prime_power_count": int(np.sum(INSTANCE.U <= shape["alpha"])),
            "comb_alignment": float("nan"), "margin": float("nan"),
            "good": False, "available": False, "failure": "chain incomplete",
        }
    chain_a, chain_b, mass0 = BUILDER.mu_chain_opt(measure["xp"], measure["wp"], depth)
    locations = np.concatenate([np.asarray(bx, float), np.asarray(by, float)])
    weights = np.concatenate([np.asarray(bw, float), -np.asarray(bv, float)])
    border = BUILDER.bvec_opt(chain_a, chain_b, mass0, locations, weights, depth)
    matrix_b = BUILDER.b_matrix_opt(
        chain_a, chain_b, mass0, measure["yn"], measure["vn"], depth
    )
    beta = border / math.sqrt(float(pack["Bw"]))
    gram = matrix_b @ matrix_b.T
    vector = matrix_b @ beta
    augmented = np.empty((len(vector) + 1, len(vector) + 1))
    augmented.fill(0.0)
    augmented[:-1, :-1] = gram
    augmented[:-1, -1] = vector
    augmented[-1, :-1] = vector
    augmented[-1, -1] = float(beta @ beta)
    top = float(np.linalg.eigvalsh(0.5 * (augmented + augmented.T))[-1])
    margin = 1.0 / (1.0 + top) - 0.5
    mask = INSTANCE.U <= shape["alpha"]
    phases = INSTANCE.U[mask] / shape["D"]
    phase_weights = INSTANCE.W_VM[mask]
    alignment = float(
        np.average(np.abs(phases - np.rint(phases)), weights=np.abs(phase_weights))
    ) if phases.size else 0.0
    return {
        "k": k,
        "delta": shape["D"],
        "window_length": shape["alpha"],
        "prime_power_count": int(np.sum(mask)),
        "comb_alignment": alignment,
        "lambda_max_augmented_gram": top,
        "lambda_min_Rdagger_minus_half": margin,
        "margin": margin,
        "good": bool(margin >= -TOLERANCE and pack.get("pos_ok", False)),
        "available": True,
        "chain_positive": bool(pack.get("pos_ok", False)),
        "n_flip": int(pack.get("n_flip") or 0),
    }


def permutation_baseline(train: list[dict], holdout: list[dict], rng: random.Random) -> dict:
    labels = [bool(row["good"]) for row in train + holdout]
    scores = []
    hold_count = len(holdout)
    for _ in range(1000):
        shuffled = labels[:]
        rng.shuffle(shuffled)
        training = shuffled[:-hold_count]
        majority = sum(training) * 2 >= len(training)
        scores.append(float(np.mean([label == majority for label in shuffled[-hold_count:]])))
    return {
        "mean_accuracy": float(np.mean(scores)),
        "p95_accuracy": float(np.quantile(scores, 0.95)),
        "repetitions": len(scores),
    }


def evolve_classifier(proposals: list[dict], started: float, rng: random.Random) -> dict:
    rows = []
    for k in SELECTED_K:
        check_wall(started)
        rows.append(selected_spectral_row(k))
    usable = [row for row in rows if row["available"]]
    holdout = [row for index, row in enumerate(usable) if index % 3 == 2]
    train = [row for row in usable if row not in holdout]
    features = ["k", "delta", "window_length", "prime_power_count", "comb_alignment"]
    programs = threshold_classifier_programs(features, train)
    scored = []
    for program in programs:
        item = {
            **program,
            "train_accuracy": accuracy(program, train),
            "holdout_accuracy": accuracy(program, holdout),
        }
        item["fitness"] = 1.0 - item["train_accuracy"] + 1.0e-6 * len(item["source"])
        scored.append(item)
    best = min(scored, key=lambda item: item["fitness"])
    proposals.extend({"target": "T3-classifier", **item} for item in scored)
    return {
        "best": best,
        "null": permutation_baseline(train, holdout, rng),
        "rows": rows,
        "train_k": [row["k"] for row in train],
        "holdout_k": [row["k"] for row in holdout],
        "label_counts": {
            "good": sum(bool(row["good"]) for row in usable),
            "bad": sum(not bool(row["good"]) for row in usable),
        },
    }


def infimum_profile(proposals: list[dict]) -> dict:
    payload = json.loads(PROFILE_RESULT.read_text(encoding="utf-8"))
    records = {float(row["L"]): row for row in payload["per_L"]}
    rows = []
    for length in PROFILE_LENGTHS:
        row = records[length]
        value = float(row["lambda_1_even"])
        reference = payload.get("validation", [])
        reference_row = next((item for item in reference if float(item["L"]) == length), None)
        scout_value = value if reference_row is None else float(reference_row["ours_even"])
        candidate = {
            "source": f"return lowest_even_Legendre_mode(degree={int(row['N_even'])})",
            "L": length,
            "degree": int(row["N_even"]),
            "infimum": value,
            "scout_lambda": scout_value,
            "difference": value - scout_value,
            "bug": bool(value < -TOLERANCE),
        }
        rows.append(candidate)
        proposals.append({"target": "T3-hardest-window", **candidate, "fitness": value})
    return {
        "rows": rows,
        "pipeline_bug": any(row["bug"] for row in rows),
        "source": "weil_window_profile_scout.py Galerkin Legendre minimizers",
    }


def api_context() -> tuple[OpenAIService, dict, str]:
    env_key = bool(os.environ.get("OPENAI_API_KEY", "").strip())
    service = OpenAIService(
        budget_usd=BUDGET_USD,
        dry_run=not env_key,
        cache_dir=str(RESULTS / "llm_cache"),
    )
    estimate = service.estimate_cost(12)
    if estimate["total_usd"] > BUDGET_USD:
        raise StopEvolution("estimated API cost exceeds budget")
    return service, estimate, "llm" if env_key else "deterministic-local"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Reserved compatibility flag")
    parser.parse_args()
    started = time.monotonic()
    RESULTS.mkdir(parents=True, exist_ok=True)
    firewall()
    rng = random.Random(SEED)
    service, estimate, mode = api_context()
    proposals: list[dict] = []
    stopped_reason = None
    try:
        t1 = evolve_rate(proposals, started)
        t2 = evolve_polynomial(proposals)
        classifier = evolve_classifier(proposals, started, rng)
        profile = infimum_profile(proposals)
    except StopEvolution as exc:
        stopped_reason = str(exc)
        t1 = t2 = classifier = profile = None
    runtime = time.monotonic() - started
    proposal_payload = {
        "seed": SEED,
        "mode": mode,
        "proposals": proposals,
        "spent_usd": service.spent_usd,
    }
    PROPOSAL_PATH.write_text(json.dumps(proposal_payload, indent=2) + "\n", encoding="utf-8")
    result = {
        "contract": "PRIME.RDAGGER.PROGRAM_EVOLUTION.01",
        "fence": "Experiment-only finite and classical measurements; no RH claim.",
        "seed": SEED,
        "mode": mode,
        "api": {
            "budget_usd": BUDGET_USD,
            "estimate": estimate,
            "spent_usd": service.spent_usd,
        },
        "wall_limit_seconds": WALL_LIMIT_SECONDS,
        "runtime_seconds": runtime,
        "stopped_reason": stopped_reason,
        "sources": {
            "arch": "arch_rate_probe.py / extraction_joint_probe.py",
            "selected_operator": "cofinal_family_probe.py / deep_builder_probe.py",
            "window_profile": "weil_window_profile_scout.py",
        },
        "T1": t1,
        "T2": t2,
        "T3_classifier": classifier,
        "T3_infimum_profile": profile,
        "source_sha256": {
            "evolve_props.py": file_sha(Path(__file__)),
            "fitness.py": file_sha(HERE / "fitness.py"),
        },
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        f"EVOLUTION COMPLETE mode={mode} proposals={len(proposals)} "
        f"spent_usd={service.spent_usd:.6f} runtime={runtime:.2f}s"
    )
    if stopped_reason:
        print(f"STOPPED {stopped_reason}")
        return 2
    print(
        f"T1 best={t1['best']['source']} c={t1['best']['constant']:.9g} "
        f"worst={t1['best']['worst_normalized_ratio']:.6g}"
    )
    print(
        f"T2 best={t2['best']['source']} c={t2['best']['constant']:.9g}; "
        "dictionary remains unproved"
    )
    print(
        f"T3 classifier holdout={classifier['best']['holdout_accuracy']:.3f} "
        f"null={classifier['null']['mean_accuracy']:.3f} "
        f"labels={classifier['label_counts']}"
    )
    print("T3 profile " + ", ".join(f"L={row['L']}: {row['infimum']:.6e}" for row in profile["rows"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
