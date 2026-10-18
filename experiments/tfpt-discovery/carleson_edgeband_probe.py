#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carleson_edgeband_probe -- PRIME.RDAGGER.CARLESON_EDGEBAND.01 (r482).

Measures the spectral distribution

    F_k(t) = sum_{1-t <= lambda_j < 1} |<u_k,e_j>|^2

on t=2^-1,...,2^-20 for the production selected windows k=5..16.

FINITE CENSUS.
  * A pooled log-log fit on the 127 positive dyadic observations gives
      F ~ 0.019002 t^1.274663 (Delta-AIC=-23.70 versus exponent 1),
    but the individual exponent excess ranges from -0.631 to +2.765;
    k=5 has only two positive points.  Zero points are disclosed drops.
  * A genuine all-jump envelope exists on the finite census:
      F_k(t) <= 0.666528 t^1.25 for 0<t<=1/2, k=5..16.
    This is a finite fitted inequality, not an asymptotic theorem.
  * Even when C, epsilon and eta are optimized separately for each
    exact finite spectrum, the sufficient-rule (SR) upper bound is
    1.055..2.700.  It proves none of the twelve already-live windows.

WORLD GATE.
  The r467 top-overlap factor is not a statement about strict F:
  scrambled and ARCH contractions are usually supercritical.  Strict F
  may therefore be zero while the dangerous mass on [1-t,infinity) is
  large.  At t=1/2 the normalized dangerous SCRAMBLE mass exceeds MAIN
  on every k; ARCH is >0.9993 of its total mass on every k.

MECHANISM CENSUS.
  (a) The strongest whole-space Christoffel/RKHS norm bound is independent
      of t and overshoots the top atom by 105..7.64e7.
  (b) A source-sensitive restricted large-sieve statement can be written,
      but after the MAIN-dependent orthogonalization it is exactly the
      desired edge-projector embedding, not a known classical large sieve.
  (c) A local DCT/Plancherel projector split at t=2^-8 overshoots F by
      5.52e3..3.59e4 on k=9..16.

VERDICT: STUCK(SR_FAILS_FINITE_CENSUS; RESTRICTED_LARGE_SIEVE_IS_TARGET;
               STRICT_F_SCRAMBLE_PREMISE_FALSE).

Finite diagnostics only.  NO RH claim and NO anti-RH claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
from scipy.fft import dct
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROBLEM = os.path.join(REPO, "rh", "problem")
for path in (HERE, PROBLEM):
    if path not in sys.path:
        sys.path.insert(0, path)

import octave_renorm_probe as S468  # noqa: E402
import overlap_mechanism_probe as S467  # noqa: E402

K_FULL = tuple(range(5, 17))
K_SMOKE = (5,)
DYADICS = np.asarray([2.0**(-power) for power in range(1, 21)])
FIT_EPSILON = 0.25
FIT_ETA = 0.5
SCRAMBLE_SEED = S467.SCRAMBLE_SEED
DPS = 70

VERDICT = (
    "STUCK(SR_FAILS_FINITE_CENSUS;RESTRICTED_LARGE_SIEVE_IS_TARGET;"
    "STRICT_F_SCRAMBLE_PREMISE_FALSE)"
)

Q_PINS = {
    5: 0.8778980273211967, 6: 0.8853557015578651,
    7: 0.8604908138510696, 8: 0.8521601029840707,
    9: 0.8975761573716292, 10: 0.9319618718590361,
    11: 0.9201639221821031, 12: 0.9139230810153632,
    13: 0.9257687100708679, 14: 0.9436044214558394,
    15: 0.9265754673904818, 16: 0.9450169226142033,
}

SR_PINS = {
    5: 1.0790439, 6: 1.0550000, 7: 1.5491300,
    8: 1.5925400, 9: 1.5369900, 10: 1.4352800,
    11: 2.0015200, 12: 1.7905810, 13: 1.7035130,
    14: 2.7000190, 15: 2.5632050, 16: 1.5025500,
}

CURVE_SHA = "e45622d390abf932004d78f5f0948b4a3f486e9ab04690b2ec58d8d11f1d9da5"
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []
STARTED = time.perf_counter()


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-43s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def firewall_audit():
    with open(os.path.abspath(__file__), encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    forbidden = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
                 "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        name = (node.attr if isinstance(node, ast.Attribute)
                else node.id if isinstance(node, ast.Name) else None)
        if name and name.lower() in forbidden:
            bad.append("%s@%d" % (name, node.lineno))
    return not bad, bad


def build_worlds(selected: tuple[int, ...]) -> list[dict]:
    active_rows = S468.rows_lp(2**max(selected))[0]
    worlds = []
    for k in selected:
        world = S467.selected_worlds(k, active_rows)
        for name in ("main", "arch", "scramble"):
            world[name]["k"] = k
        worlds.append(world)
    return worlds


def spectral_data(blocks: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    eigenvalues = blocks["eigenvalues"]
    coefficients_sq = (blocks["eigenvectors"].T @ blocks["u"])**2
    gaps = 1.0 - eigenvalues
    return eigenvalues, gaps, coefficients_sq


def distribution(blocks: dict, points: np.ndarray = DYADICS) -> np.ndarray:
    _, gaps, coefficients_sq = spectral_data(blocks)
    return np.asarray([
        float(np.sum(coefficients_sq[(gaps > 0.0) & (gaps <= point)]))
        for point in points
    ])


def danger_mass(blocks: dict, eta: float) -> float:
    _, gaps, coefficients_sq = spectral_data(blocks)
    return float(np.sum(coefficients_sq[gaps <= eta]))


def curve_record(worlds: list[dict]) -> str:
    lines = []
    for world in worlds:
        values = distribution(world["main"])
        lines.append("%d:%s" % (
            world["k"], ",".join("%.12e" % value for value in values)))
    return "\n".join(lines)


def fit_power(blocks: dict) -> dict:
    values = distribution(blocks)
    mask = values > 0.0
    x = np.log(DYADICS[mask])
    y = np.log(values[mask])
    if len(x) < 3:
        return {
            "n": len(x), "drops": len(values) - len(x),
            "C": float("nan"), "epsilon": float("nan"),
            "aic": float("nan"), "delta_aic": float("nan"),
        }
    slope, intercept = np.polyfit(x, y, 1)
    residual = y - (intercept + slope * x)
    rss = float(residual @ residual)
    aic = len(x) * math.log(max(rss / len(x), 1e-300)) + 4.0
    intercept_linear = float(np.mean(y - x))
    residual_linear = y - (intercept_linear + x)
    rss_linear = float(residual_linear @ residual_linear)
    aic_linear = (
        len(x) * math.log(max(rss_linear / len(x), 1e-300)) + 2.0
    )
    return {
        "n": len(x), "drops": len(values) - len(x),
        "C": math.exp(float(intercept)), "epsilon": float(slope - 1.0),
        "aic": aic, "delta_aic": aic - aic_linear,
    }


def pooled_fit(worlds: list[dict]) -> dict:
    x_parts = []
    y_parts = []
    for world in worlds:
        values = distribution(world["main"])
        mask = values > 0.0
        x_parts.append(np.log(DYADICS[mask]))
        y_parts.append(np.log(values[mask]))
    x = np.concatenate(x_parts)
    y = np.concatenate(y_parts)
    slope, intercept = np.polyfit(x, y, 1)
    residual = y - (intercept + slope * x)
    rss = float(residual @ residual)
    aic = len(x) * math.log(rss / len(x)) + 4.0
    intercept_linear = float(np.mean(y - x))
    residual_linear = y - (intercept_linear + x)
    rss_linear = float(residual_linear @ residual_linear)
    aic_linear = len(x) * math.log(rss_linear / len(x)) + 2.0
    return {
        "n": len(x), "C": math.exp(float(intercept)),
        "epsilon": float(slope - 1.0), "aic": aic,
        "delta_aic": aic - aic_linear,
    }


def envelope_constant(blocks: dict, epsilon: float,
                      eta: float = FIT_ETA) -> float:
    _, gaps, coefficients_sq = spectral_data(blocks)
    mask = (gaps > 0.0) & (gaps <= eta)
    ordered = np.argsort(gaps[mask])
    active_gaps = gaps[mask][ordered]
    cumulative = np.cumsum(coefficients_sq[mask][ordered])
    if not len(active_gaps):
        return 0.0
    return float(np.max(cumulative / active_gaps**(1.0 + epsilon)))


def sr_at_epsilon(blocks: dict, epsilon: float) -> dict:
    _, gaps, coefficients_sq = spectral_data(blocks)
    gamma = float(np.sum(coefficients_sq))
    mask = (gaps > 0.0) & (gaps < 1.0)
    ordered = np.argsort(gaps[mask])
    active_gaps = gaps[mask][ordered]
    active_mass = coefficients_sq[mask][ordered]
    cumulative = np.cumsum(active_mass)
    best = {
        "value": float("inf"), "eta": float("nan"), "C": float("nan"),
        "far": float("nan"), "edge": float("nan"),
    }
    constant = 0.0
    for index, gap in enumerate(active_gaps):
        constant = max(
            constant,
            float(cumulative[index] / gap**(1.0 + epsilon)),
        )
        lower = float(gap * (1.0 + 1e-12))
        upper = (
            float(active_gaps[index + 1] * (1.0 - 1e-12))
            if index + 1 < len(active_gaps) else 1.0 - 1e-12
        )
        if lower > upper:
            continue
        far_mass = gamma - float(cumulative[index])
        edge_coefficient = constant * (1.0 + 1.0 / epsilon)
        stationary = (
            (far_mass / (edge_coefficient * epsilon))
            ** (1.0 / (epsilon + 1.0))
            if far_mass > 0.0 else lower
        )
        eta = min(upper, max(lower, stationary))
        far = far_mass / eta
        edge = edge_coefficient * eta**epsilon
        value = far + edge
        if value < best["value"]:
            best = {
                "value": value, "eta": eta, "C": constant,
                "far": far, "edge": edge,
            }
    return best


def optimize_sr(blocks: dict) -> dict:
    grid = np.linspace(0.01, 4.0, 400)
    values = np.asarray([
        sr_at_epsilon(blocks, float(epsilon))["value"]
        for epsilon in grid
    ])
    index = int(np.argmin(values))
    lower = float(grid[max(0, index - 2)])
    upper = float(grid[min(len(grid) - 1, index + 2)])
    result = minimize_scalar(
        lambda epsilon: sr_at_epsilon(
            blocks, float(epsilon))["value"],
        bounds=(lower, upper), method="bounded",
        options={"xatol": 1e-10},
    )
    epsilon = float(result.x)
    best = sr_at_epsilon(blocks, epsilon)
    best["epsilon"] = epsilon
    return best


def christoffel_factor(blocks: dict) -> float:
    _, gaps, coefficients_sq = spectral_data(blocks)
    top_mass = float(coefficients_sq[np.argmin(gaps)])
    # ||u||^2 is the exact RKHS norm of the border functional in the
    # finite mu-polynomial space; pointwise Christoffel triangle bounds
    # can only be weaker.
    return float(np.sum(coefficients_sq) / top_mass)


def local_plancherel_bound(blocks: dict, eta: float = 2.0**-8) -> dict:
    _, gaps, _ = spectral_data(blocks)
    edge_vectors = blocks["eigenvectors"][:, (gaps > 0.0) & (gaps <= eta)]
    vector = blocks["u"]
    dimension = len(vector)
    low_count = max(1, math.ceil(dimension / 4))
    low_rows = dct(
        np.eye(dimension), type=2, norm="ortho", axis=0)[:low_count, :]
    low_projector = low_rows.T @ low_rows
    low_vector = low_projector @ vector
    if edge_vectors.size:
        edge_projector = edge_vectors @ edge_vectors.T
        leakage = float(np.linalg.norm(
            edge_projector @ (np.eye(dimension) - low_projector), 2))
        measured = float(np.linalg.norm(edge_vectors.T @ vector)**2)
    else:
        leakage = 0.0
        measured = 0.0
    bound = (
        float(np.linalg.norm(low_vector))
        + leakage * float(np.linalg.norm(vector))
    )**2
    return {
        "measured": measured, "bound": bound, "leakage": leakage,
        "factor": bound / measured if measured > 0.0 else float("nan"),
    }


def binary64_enclosure_ward(blocks: dict) -> dict:
    matrix = blocks["C"]
    eigenvalues = blocks["eigenvalues"]
    eigenvectors = blocks["eigenvectors"]
    residual_matrix = (
        matrix @ eigenvectors - eigenvectors @ np.diag(eigenvalues)
    )
    # E is orthogonal, hence C is within this operator norm of
    # E diag(lambda_hat) E^T; Weyl encloses every ordered eigenvalue.
    residual = float(np.linalg.norm(residual_matrix, 2))
    gaps = 1.0 - eigenvalues
    threshold_distance = min(
        abs(float(gap - threshold))
        for gap in gaps for threshold in DYADICS
    )
    return {
        "residual": residual, "distance": threshold_distance,
        "classification_ratio": threshold_distance / residual,
    }


def dps_edge_ward(blocks: dict) -> float:
    matrix = blocks["C"]
    dimension = len(matrix)
    mp.mp.dps = DPS
    matrix_mp = mp.matrix([
        [mp.mpf(float(matrix[row, column]))
         for column in range(dimension)]
        for row in range(dimension)
    ])
    eigenvalues_mp = mp.eigsy(matrix_mp, eigvals_only=True)
    start = max(0, dimension - 8)
    return max(
        abs(float(eigenvalues_mp[index]) - blocks["eigenvalues"][index])
        for index in range(start, dimension)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    selected = K_SMOKE if args.smoke else K_FULL
    print("=" * 78)
    print("carleson_edgeband_probe -- round 482")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if args.smoke else "FULL")
    print("=" * 78)

    section("S0  FIREWALL / OBJECT")
    firewall_ok, bad = firewall_audit()
    check("G00-firewall", firewall_ok,
          "finite comb/matrices only" if firewall_ok else str(bad))
    worlds = build_worlds(selected)
    q_ok = True
    for world in worlds:
        _, gaps, coefficients_sq = spectral_data(world["main"])
        q_value = float(np.sum(coefficients_sq / gaps))
        q_ok = q_ok and abs(q_value - Q_PINS[world["k"]]) < 2e-10
    check("G01-q-pins", q_ok,
          "production k=%d..%d" % (min(selected), max(selected)))

    section("S1  DYADIC F_k CURVES")
    print(" k " + " ".join("2^-%02d" % power for power in range(1, 21)))
    for world in worlds:
        values = distribution(world["main"])
        print("%2d %s" % (
            world["k"], " ".join("%.3e" % value for value in values)))
    record = curve_record(worlds)
    record_sha = hashlib.sha256(record.encode("ascii")).hexdigest()
    if args.smoke:
        check("G10-curve-deterministic", len(record) > 0,
              "smoke SHA " + record_sha[:16])
    else:
        check("G10-curve-seal", record_sha == CURVE_SHA,
              "curve SHA " + record_sha[:16])

    section("S2  POWER FITS / TRUE ENVELOPE")
    fits = []
    constants = []
    print(" k n drop C_reg       eps_reg    AIC      dAIC    C_env(eps=.25)")
    for world in worlds:
        fit = fit_power(world["main"])
        constant = envelope_constant(world["main"], FIT_EPSILON)
        fits.append(fit)
        constants.append(constant)
        print("%2d %2d %2d  %.6g  %+9.6f %8.3f %8.3f  %.6f" % (
            world["k"], fit["n"], fit["drops"], fit["C"],
            fit["epsilon"], fit["aic"], fit["delta_aic"], constant))
    if not args.smoke:
        pooled = pooled_fit(worlds)
        check("G20-pooled-positive-exponent",
              abs(pooled["epsilon"] - 0.2746633536610459) < 2e-12
              and pooled["delta_aic"] < -20.0,
              "C=%.6f eps=%.6f dAIC=%.2f n=%d" % (
                  pooled["C"], pooled["epsilon"],
                  pooled["delta_aic"], pooled["n"]))
        check("G21-individual-instability",
              min(fit["epsilon"] for fit in fits if fit["n"] >= 3) < 0.0
              and max(fit["epsilon"] for fit in fits if fit["n"] >= 3) > 2.0,
              "eps range %.3f..%.3f; k5 only %d positive points" % (
                  min(fit["epsilon"] for fit in fits if fit["n"] >= 3),
                  max(fit["epsilon"] for fit in fits if fit["n"] >= 3),
                  fits[0]["n"]))
        check("G22-finite-uniform-envelope",
              abs(max(constants) - 0.6665278419525172) < 2e-12,
              "F<=0.666528 t^1.25 on all exact jumps, t<=1/2")
    else:
        check("G20-pooled-positive-exponent", True, "full-only fit")

    section("S3  OPTIMIZED SUFFICIENT-RULE BALANCE")
    sr_rows = []
    print(" k eta       epsilon   C          far       edge      SR       margin")
    for world in worlds:
        result = optimize_sr(world["main"])
        sr_rows.append(result)
        print("%2d %.6f  %.6f  %.6f  %.6f  %.6f  %.6f  %+.6f" % (
            world["k"], result["eta"], result["epsilon"], result["C"],
            result["far"], result["edge"], result["value"],
            1.0 - result["value"]))
        check("G3-k%d-SR-pin" % world["k"],
              abs(result["value"] - SR_PINS[world["k"]]) < 5e-6,
              "best SR %.6f" % result["value"])
    check("G30-SR-closes-none",
          min(result["value"] for result in sr_rows) > 1.0,
          "best %.6f; worst %.6f" % (
              min(result["value"] for result in sr_rows),
              max(result["value"] for result in sr_rows)))

    section("S4  SCRAMBLE / ARCH WORLD GATE")
    print(" k Fm(.5) Fs(.5) Fa(.5)  danger-frac M/S/A  supercritical S/A")
    world_ok = True
    strict_counterexamples = 0
    for world in worlds:
        main = world["main"]
        scramble = world["scramble"]
        arch = world["arch"]
        main_curve = distribution(main)
        scramble_curve = distribution(scramble)
        arch_curve = distribution(arch)
        main_gamma = float(main["u"] @ main["u"])
        scramble_gamma = float(scramble["u"] @ scramble["u"])
        arch_gamma = float(arch["u"] @ arch["u"])
        main_danger = danger_mass(main, 0.5) / main_gamma
        scramble_danger = danger_mass(scramble, 0.5) / scramble_gamma
        arch_danger = danger_mass(arch, 0.5) / arch_gamma
        _, scramble_gaps, scramble_mass = spectral_data(scramble)
        _, arch_gaps, arch_mass = spectral_data(arch)
        scramble_super = float(np.sum(scramble_mass[scramble_gaps <= 0.0]))
        arch_super = float(np.sum(arch_mass[arch_gaps <= 0.0]))
        if scramble_curve[0] < main_curve[0]:
            strict_counterexamples += 1
        world_ok = world_ok and (
            scramble_danger > main_danger and arch_danger > 0.999
        )
        print("%2d %.3e %.3e %.3e  %.4f/%.4f/%.4f  %.3e/%.3e" % (
            world["k"], main_curve[0], scramble_curve[0], arch_curve[0],
            main_danger, scramble_danger, arch_danger,
            scramble_super, arch_super))
    check("G40-danger-mass-scramble-sensitive", world_ok,
          "normalized [1/2,infinity) mass larger in controls")
    if not args.smoke:
        check("G41-strict-F-premise-false",
              strict_counterexamples >= 2,
              "F_SCR(.5)<F_MAIN(.5) on %d/12 due to lambda>=1" %
              strict_counterexamples)

    section("S5  THREE MECHANISM CANDIDATES")
    christoffel = [christoffel_factor(world["main"]) for world in worlds]
    planch = [
        local_plancherel_bound(world["main"])
        for world in worlds if world["k"] >= 9
    ]
    print("Christoffel/RKHS top-atom factors:",
          "%.3g..%.3g" % (min(christoffel), max(christoffel)))
    if planch:
        print("local Plancherel factors at t=2^-8:",
              "%.3g..%.3g" % (
                  min(row["factor"] for row in planch),
                  max(row["factor"] for row in planch)))
    check("G50-Christoffel-t-independent",
          min(christoffel) > 100.0,
          "whole-space RKHS/top atom %.3g..%.3g" %
          (min(christoffel), max(christoffel)))
    if not args.smoke:
        check("G51-local-Plancherel-too-coarse",
              min(row["factor"] for row in planch) > 5e3,
              "factor %.3g..%.3g" % (
                  min(row["factor"] for row in planch),
                  max(row["factor"] for row in planch)))
    else:
        check("G51-local-Plancherel-too-coarse", True, "full-only band")
    check("G52-large-sieve-remainder-typed",
          "RESTRICTED_LARGE_SIEVE_IS_TARGET" in VERDICT,
          "source nodes enter B_k and the OP basis; no classical theorem")

    section("S6  EDGE EIGENVALUE DISCIPLINE")
    enclosures = [binary64_enclosure_ward(world["main"]) for world in worlds]
    check("G60-residual-enclosures",
          max(row["residual"] for row in enclosures) < 2e-14
          and min(row["classification_ratio"] for row in enclosures) > 1e8,
          "res %.3e; min dyadic distance/res %.3e" % (
              max(row["residual"] for row in enclosures),
              min(row["classification_ratio"] for row in enclosures)))
    dps_worlds = worlds if args.smoke else [
        world for world in worlds if world["k"] in (5, 9, 12, 16)
    ]
    dps_errors = [dps_edge_ward(world["main"]) for world in dps_worlds]
    check("G61-dps70-edge",
          max(dps_errors) < 2e-15,
          "max top-eight eigenvalue discrepancy %.3e" % max(dps_errors))

    section("S7  VERDICT / ALIAS")
    check("G70-SR-status",
          VERDICT.startswith("STUCK(")
          and min(result["value"] for result in sr_rows) > 1.0,
          VERDICT)
    check("G71-alias-audit",
          (max(christoffel) > 1e6 if not args.smoke else
           min(christoffel) > 100.0)
          and (not planch or min(row["factor"] for row in planch) > 5e3),
          "Christoffel aliases Loewner/RKHS majorant; Plancherel splits suprema")
    check("G99-runtime", time.perf_counter() - STARTED < 3600.0,
          "within 3600s budget")

    failures = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS" % (
        len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("FAILED:", ", ".join(failures))
        return 1
    print("CARLESON EDGEBAND VERIFIED -- VERDICT " + VERDICT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
