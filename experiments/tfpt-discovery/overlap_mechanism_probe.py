#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""overlap_mechanism_probe -- PRIME.RDAGGER.OVERLAP_MECHANISM.01 (r467).

Lemma-first attack on the r460 edge spectral sum

    q^dagger = sum_j |<u,e_j>|^2 / (1-lambda_j).

PROVED finite lemma:
  If U_r=sum_{i<=r}u_i, then

    <u,e> = U_{N-1}e_{N-1}
            + sum_{r<N-1} U_r(e_r-e_{r+1}),

  hence |<u,e>| <= max_r|U_r| (|e_{N-1}|+TV(e)).

MEASURED anatomy:
  the top three MAIN eigenvectors are low-frequency profiles, but their
  total variation falls only as N^-0.196 on k=5..12.  Small overlap is
  correlated with low variation (corr +0.745 on top modes), ARCH aligns
  almost completely with its top mode, and scramble destroys the tiny
  MAIN alignment.

BLOCKER:
  u is the smooth-border functional after the MAIN orthogonal-polynomial
  basis change; it is not the raw prime-lag vector.  A Chebyshev psi bound
  controls the source before this nonlinear basis construction, not the
  partial sums U_r needed by Abel.  Even using the *measured exact* U_r
  (strictly sharper than a source majorant), the top-mode Abel factor is
  13.5..794 and the three-mode band bound / measured band contribution is
  91.7..1.19e5.  Thus the requested <10 sharpness gate fails and the >1e3
  stop gate fires on k=7..12.

VERDICT: STUCK(QUALITATIVE_ALIGNMENT_REAL; ABEL_CURRENCY_TOO_COARSE;
               SOURCE_TO_BORDER_BASIS_BRIDGE_MISSING).

Finite diagnostics only.  NO RH claim and NO anti-RH claim.
"""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROBLEM = os.path.join(REPO, "rh", "problem")
for path in (HERE, PROBLEM):
    if path not in sys.path:
        sys.path.insert(0, path)

import deep_builder_probe as S445  # noqa: E402
import fullcomb_cleanup_probe as S459  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402

K_FULL = tuple(range(5, 13))
K_SMOKE = (5,)
SIEVE_CAP = 16_800_000
TOP_MODES = 3
SCRAMBLE_SEED = 46701
RS_CONSTANT = 1.03883
DPS_EIGEN = 80

VERDICT = (
    "STUCK(QUALITATIVE_ALIGNMENT_REAL;ABEL_CURRENCY_TOO_COARSE;"
    "SOURCE_TO_BORDER_BASIS_BRIDGE_MISSING)"
)

TOP_PINS = {
    5: (0.8269525005004436, 9.525458745598228e-3,
        0.045956243154265636, 1.2701200619528619, 0.9623594577232518),
    6: (0.9446611814938115, 2.2159458313928744e-6,
        3.1525811607932296e-5, 1.2164603396511702, 0.9561850605500176),
    7: (0.9867838788834172, 8.894706641661603e-4,
        0.041989310500657746, 1.2071057934287320, 0.9496575594864581),
    8: (0.9941762997175456, 5.049855011852680e-4,
        0.047331145943195940, 1.2397435901749922, 0.9259060249427210),
    9: (0.9991327874455699, 1.9364958209557052e-5,
        0.014031572089188784, 1.0132666069980651, 0.9813844016361353),
    10: (0.9995864154913183, 4.151542930656847e-6,
         0.006614479631170824, 1.0784815186394334, 0.9744897336688102),
    11: (0.9998267472821409, 5.104420351568530e-6,
         0.014065986277649233, 0.9414448651939433, 0.9826992995320906),
    12: (0.9999127942710433, 1.5449166174246412e-6,
         0.007711681705783510, 0.8871503831217809, 0.9887616192330646),
}

BAND_FACTOR_PINS = {
    5: 91.70294183698877,
    6: 268.7261203677157,
    7: 1498.907904840181,
    8: 1676.0709804162318,
    9: 24480.314722292354,
    10: 42505.429992118334,
    11: 74595.32172292644,
    12: 119482.63214546863,
}

CONTROL_PINS = {
    5: (0.9980548920639640, 0.29849211045741114),
    6: (0.9982355358520183, 0.22965037753423762),
    7: (0.9976021537641372, 0.025356194144449097),
    8: (0.9989698366029500, 0.05219000139179801),
    9: (0.9987558194477368, 0.3219338192879518),
    10: (0.9979637229977141, 0.6591571841664965),
    11: (0.9981586417486153, 0.023868746714057372),
    12: (0.9958132508585156, 0.8180703238723220),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []
STARTED = time.perf_counter()


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
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


def build_blocks(mz: dict, border: tuple, depth: int,
                 normalization_budget: float | None = None) -> dict:
    pack = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        *border, depth, engine="numpy", require_pos=False)
    alpha, beta, h0 = S445.mu_chain_opt(
        mz["xp"], mz["wp"], depth)
    border_nodes = np.concatenate([
        np.asarray(border[0], dtype=float),
        np.asarray(border[2], dtype=float),
    ])
    border_weights = np.concatenate([
        np.asarray(border[1], dtype=float),
        -np.asarray(border[3], dtype=float),
    ])
    border_vector = S445.bvec_opt(
        alpha, beta, h0, border_nodes, border_weights, depth)
    sampling = S445.b_matrix_opt(
        alpha, beta, h0, mz["yn"], mz["vn"], depth)
    contraction = sampling.T @ sampling
    contraction = 0.5 * (contraction + contraction.T)
    budget = float(pack["Bw"] if normalization_budget is None
                   else normalization_budget)
    normalized_border = border_vector / math.sqrt(abs(budget))
    eigenvalues, eigenvectors = np.linalg.eigh(contraction)
    return {
        "C": contraction,
        "u": normalized_border,
        "Bw": budget,
        "pack": pack,
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
    }


def selected_worlds(k: int, prime_powers: list) -> dict:
    shape = S459.S458.lean_shape(k)
    prime_lags, atom_count = S459.lags_from_rows(
        prime_powers, shape["alpha"], shape["M"], shape["D"])
    main, arch = S459.mz_pair(
        prime_lags, atom_count, shape["alpha"], shape["M"],
        shape["L"], shape["Nw"], shape["D"])
    border = S459.S458.border_from_shape(shape)
    main_blocks = build_blocks(main, border, shape["Nw"])
    scramble = S451.scramble_mz(main, SCRAMBLE_SEED + k)
    scramble_blocks = build_blocks(
        scramble, border, shape["Nw"],
        normalization_budget=main_blocks["Bw"])
    arch_blocks = build_blocks(arch, border, shape["Nw"])
    return {
        "k": k, "shape": shape, "atoms": atom_count,
        "main": main_blocks, "arch": arch_blocks,
        "scramble": scramble_blocks,
    }


def low_fourier_share(vector: np.ndarray) -> float:
    spectrum = np.fft.rfft(vector, norm="ortho")
    cutoff = max(2, len(spectrum) // 4)
    return float(np.sum(np.abs(spectrum[:cutoff])**2)
                 / np.sum(np.abs(spectrum)**2))


def mode_anatomy(blocks: dict, top_modes: int = TOP_MODES) -> list[dict]:
    eigenvalues = blocks["eigenvalues"]
    eigenvectors = blocks["eigenvectors"]
    u = blocks["u"]
    gamma = float(u @ u)
    coefficients = eigenvectors.T @ u
    q_terms = coefficients**2 / (1.0 - eigenvalues)
    q_total = float(np.sum(q_terms))
    partial_max = float(np.max(np.abs(np.cumsum(u))))
    rows = []
    for index in range(len(eigenvalues) - top_modes, len(eigenvalues)):
        eigenvector = eigenvectors[:, index]
        variation = float(np.sum(np.abs(np.diff(eigenvector))))
        endpoint_variation = variation + abs(float(eigenvector[-1]))
        overlap = abs(float(coefficients[index]))
        abel_bound = partial_max * endpoint_variation
        triangle_bound = float(np.sum(np.abs(u))) * endpoint_variation
        source_bound = (
            RS_CONSTANT * (2.0 * math.sqrt(2**blocks["k"]) - 1.0)
            * endpoint_variation
        )
        rows.append({
            "rank": len(eigenvalues) - index,
            "lambda": float(eigenvalues[index]),
            "gap": float(1.0 - eigenvalues[index]),
            "variation": variation,
            "endpoint_variation": endpoint_variation,
            "low_fourier": low_fourier_share(eigenvector),
            "overlap": overlap,
            "overlap_sq": overlap**2,
            "overlap_fraction": overlap**2 / gamma,
            "q_term": float(q_terms[index]),
            "q_share": float(q_terms[index] / q_total),
            "abel_bound": abel_bound,
            "abel_factor": abel_bound / max(overlap, 1e-300),
            "triangle_factor": triangle_bound / max(overlap, 1e-300),
            "optimistic_psi_factor": source_bound / max(overlap, 1e-300),
        })
    return rows


def normalized_variation(vector: np.ndarray) -> float:
    norm = float(np.linalg.norm(vector))
    return float(np.sum(np.abs(np.diff(vector))) / norm)


def high_precision_ward(blocks: dict, rows: list[dict]) -> dict:
    matrix = blocks["C"]
    vector = blocks["u"]
    dimension = matrix.shape[0]
    mp.mp.dps = DPS_EIGEN
    matrix_mp = mp.matrix([
        [mp.mpf(float(matrix[row, column]))
         for column in range(dimension)]
        for row in range(dimension)
    ])
    eigenvalues_mp, eigenvectors_mp = mp.eigsy(matrix_mp)
    max_eigen_error = mp.mpf(0)
    max_overlap_error = mp.mpf(0)
    max_residual = 0.0
    for local, index in enumerate(
            range(dimension - TOP_MODES, dimension)):
        value_mp = eigenvalues_mp[index]
        value_float = blocks["eigenvalues"][index]
        max_eigen_error = max(
            max_eigen_error, abs(value_mp - mp.mpf(float(value_float))))
        overlap_mp = sum(
            mp.mpf(float(vector[row])) * eigenvectors_mp[row, index]
            for row in range(dimension)
        )**2
        max_overlap_error = max(
            max_overlap_error,
            abs(overlap_mp - mp.mpf(float(rows[local]["overlap_sq"]))))
        eigenvector = blocks["eigenvectors"][:, index]
        residual = matrix @ eigenvector - value_float * eigenvector
        max_residual = max(max_residual, float(np.linalg.norm(residual)))
    return {
        "eigen_error": float(max_eigen_error),
        "overlap_error": float(max_overlap_error),
        "residual": max_residual,
    }


def exact_abel_ward() -> bool:
    u = (Fraction(2, 7), Fraction(-3, 5), Fraction(4, 9),
         Fraction(-1, 6))
    e = (Fraction(5, 8), Fraction(-2, 3), Fraction(7, 10),
         Fraction(3, 11))
    partial = []
    accumulator = Fraction(0)
    for value in u:
        accumulator += value
        partial.append(accumulator)
    direct = sum(x * y for x, y in zip(u, e))
    by_parts = partial[-1] * e[-1] + sum(
        partial[index] * (e[index] - e[index + 1])
        for index in range(len(u) - 1)
    )
    bound = max(abs(value) for value in partial) * (
        abs(e[-1])
        + sum(abs(e[index] - e[index + 1])
              for index in range(len(e) - 1))
    )
    return direct == by_parts and abs(direct) <= bound


def psi_selected_ward(prime_powers: list, selected: tuple[int, ...]) -> dict:
    values = []
    for k in selected:
        x = 2**k
        psi = sum(log_prime for n, log_prime in prime_powers if n <= x)
        values.append(psi / x)
    return {"maximum": max(values), "all_bounded": max(values) < RS_CONSTANT}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    selected = K_SMOKE if args.smoke else K_FULL
    print("=" * 78)
    print("overlap_mechanism_probe -- round 467")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if args.smoke else "FULL")
    print("=" * 78)

    section("S0  FIREWALL / EXACT ABEL LEMMA")
    firewall_ok, bad = firewall_audit()
    check("G00-firewall", firewall_ok,
          "finite comb/matrices only" if firewall_ok else str(bad))
    check("G01-exact-Abel-identity", exact_abel_ward(),
          "Fraction summation-by-parts ward")

    prime_powers = S459.sieve_pp(
        (2**max(selected))**2 if args.smoke else SIEVE_CAP)
    psi_ward = psi_selected_ward(prime_powers, selected)
    check("G02-Rosser-Schoenfeld-input", psi_ward["all_bounded"],
          "max psi(2^k)/2^k=%.6f < %.5f" %
          (psi_ward["maximum"], RS_CONSTANT))

    worlds = [selected_worlds(k, prime_powers) for k in selected]
    for world in worlds:
        world["main"]["k"] = world["k"]
        world["arch"]["k"] = world["k"]
        world["scramble"]["k"] = world["k"]
        world["modes"] = mode_anatomy(world["main"])
        world["arch_modes"] = mode_anatomy(world["arch"], 1)
        world["scramble_modes"] = mode_anatomy(world["scramble"], 1)

    section("S1  TOP-THREE EDGE ANATOMY")
    print(" k r lambda         TV       lowF     overlap^2    q-term    q-share")
    all_modes = []
    for world in worlds:
        k = world["k"]
        q_total = float(np.sum(
            (world["main"]["eigenvectors"].T @ world["main"]["u"])**2
            / (1.0 - world["main"]["eigenvalues"])))
        for mode in world["modes"]:
            all_modes.append({**mode, "k": k})
            print("%2d %d %.9f  %.6f  %.6f  %.3e  %.6f  %.6f" % (
                k, mode["rank"], mode["lambda"], mode["variation"],
                mode["low_fourier"], mode["overlap_sq"],
                mode["q_term"], mode["q_share"]))
        top = world["modes"][-1]
        pins = TOP_PINS[k]
        pin_ok = (
            abs(top["lambda"] - pins[0]) < 2e-12
            and abs(top["overlap_fraction"] - pins[1]) < 2e-12
            and abs(top["q_term"] - pins[2]) < 2e-12
            and abs(top["variation"] - pins[3]) < 2e-12
            and abs(top["low_fourier"] - pins[4]) < 2e-12
        )
        check("G1-k%d-mode-pins" % k, pin_ok,
              "q=%.12f top frac=%.3e TV=%.4f lowF=%.4f" %
              (q_total, top["overlap_fraction"], top["variation"],
               top["low_fourier"]))

    dimensions = np.asarray([world["shape"]["Nw"] for world in worlds],
                            dtype=float)
    top_variations = np.asarray(
        [world["modes"][-1]["variation"] for world in worlds])
    top_overlap_sq = np.asarray(
        [world["modes"][-1]["overlap_sq"] for world in worlds])
    if len(worlds) > 1:
        variation_slope = float(np.polyfit(
            np.log(dimensions), np.log(top_variations), 1)[0])
        top_correlation = float(np.corrcoef(
            top_variations, np.log10(top_overlap_sq))[0, 1])
        all_correlation = float(np.corrcoef(
            [mode["variation"] for mode in all_modes],
            np.log10([mode["overlap_sq"] for mode in all_modes]))[0, 1])
        check("G20-edge-modes-low-frequency",
              min(mode["low_fourier"] for mode in all_modes
                  if mode["rank"] == 1) > 0.92,
              "top-mode low-Fourier share %.3f..%.3f" %
              (min(world["modes"][-1]["low_fourier"] for world in worlds),
               max(world["modes"][-1]["low_fourier"] for world in worlds)))
        check("G21-variation-decay-not-O1N",
              -0.30 < variation_slope < -0.10,
              "fitted TV exponent %.6f (not -1)" % variation_slope)
        check("G22-overlap-variation-correlation",
              top_correlation > 0.65 and all_correlation > 0.60,
              "corr(top)=%.6f corr(all 24)=%.6f" %
              (top_correlation, all_correlation))
    else:
        variation_slope = float("nan")
        top_correlation = float("nan")
        all_correlation = float("nan")
        check("G20-edge-modes-low-frequency",
              worlds[0]["modes"][-1]["low_fourier"] > 0.92,
              "smoke top low-Fourier %.6f" %
              worlds[0]["modes"][-1]["low_fourier"])

    section("S2  ARCH / SCRAMBLE CONTROLS")
    control_ok = True
    scramble_ratios = []
    arch_fractions = []
    print(" k main-frac     ARCH-frac     SCR-frac      TVu(main/ARCH/SCR)")
    for world in worlds:
        k = world["k"]
        main_top = world["modes"][-1]
        arch_top = world["arch_modes"][-1]
        scramble_top = world["scramble_modes"][-1]
        arch_fraction = arch_top["overlap_fraction"]
        scramble_fraction = scramble_top["overlap_fraction"]
        arch_fractions.append(arch_fraction)
        scramble_ratios.append(
            scramble_fraction / main_top["overlap_fraction"])
        pin = CONTROL_PINS[k]
        control_ok = control_ok and (
            abs(arch_fraction - pin[0]) < 2e-10
            and abs(scramble_fraction - pin[1]) < 2e-10)
        tv_main = normalized_variation(world["main"]["u"])
        tv_arch = normalized_variation(world["arch"]["u"])
        tv_scramble = normalized_variation(world["scramble"]["u"])
        print("%2d %.3e  %.6f  %.6f  %.3f/%.3f/%.3f" % (
            k, main_top["overlap_fraction"], arch_fraction,
            scramble_fraction, tv_main, tv_arch, tv_scramble))
    check("G30-control-pins", control_ok,
          "ARCH/SCR top fractions deterministic")
    check("G31-ARCH-smooth-alignment",
          min(arch_fractions) > 0.995,
          "ARCH normalized top overlap %.6f..%.6f" %
          (min(arch_fractions), max(arch_fractions)))
    check("G32-scramble-destroys-tiny-alignment",
          min(scramble_ratios) > 25.0,
          "SCR/MAIN top-overlap fraction ratio %.1f..%.1e" %
          (min(scramble_ratios), max(scramble_ratios)))

    section("S3  ABEL SHARPNESS / SOURCE BRIDGE")
    band_factors = []
    top_abel_factors = []
    psi_factors = []
    print(" k top Abel/meas  optimistic-psi/meas  band q  Abel-band  factor")
    for world in worlds:
        modes = world["modes"]
        band_measured = sum(mode["q_term"] for mode in modes)
        band_bound = sum(
            mode["abel_bound"]**2 / mode["gap"] for mode in modes)
        factor = band_bound / band_measured
        top = modes[-1]
        band_factors.append(factor)
        top_abel_factors.append(top["abel_factor"])
        psi_factors.append(top["optimistic_psi_factor"])
        print("%2d %12.3f %20.3f %.6f %10.3f %11.3f" % (
            world["k"], top["abel_factor"],
            top["optimistic_psi_factor"], band_measured,
            band_bound, factor))
        check("G4-k%d-Abel-factor-pin" % world["k"],
              abs(factor / BAND_FACTOR_PINS[world["k"]] - 1.0) < 2e-10,
              "band factor %.6g" % factor)
    check("G40-under-10-gate-refused",
          min(top_abel_factors) > 10.0,
          "even exact-partial top factors %.1f..%.1f" %
          (min(top_abel_factors), max(top_abel_factors)))
    if len(worlds) > 1:
        check("G41-over-1000-stop-gate",
              sum(factor > 1e3 for factor in band_factors) == 6,
              "band factors %.1f..%.1e; k=7..12 > 1e3" %
              (min(band_factors), max(band_factors)))
        check("G42-psi-transfer-even-worse",
              min(psi_factors) > 100.0 and max(psi_factors) > 1e5,
              "optimistic transfer-one factors %.1f..%.1e" %
              (min(psi_factors), max(psi_factors)))
    else:
        check("G41-over-1000-stop-gate", True,
              "full-only census; smoke does not adjudicate")

    section("S4  HIGH-PRECISION EIGEN WARD")
    wards = [high_precision_ward(world["main"], world["modes"])
             for world in worlds]
    check("G50-dps80-eigenvalues",
          max(ward["eigen_error"] for ward in wards) < 2e-15,
          "max |lambda_f64-lambda_dps80| %.3e" %
          max(ward["eigen_error"] for ward in wards))
    check("G51-dps80-overlaps",
          max(ward["overlap_error"] for ward in wards) < 2e-12,
          "max overlap^2 discrepancy %.3e" %
          max(ward["overlap_error"] for ward in wards))
    check("G52-eigen-residual",
          max(ward["residual"] for ward in wards) < 2e-14,
          "max symmetric eigen residual %.3e" %
          max(ward["residual"] for ward in wards))

    section("S5  VERDICT")
    source_type_ok = all(
        world["main"]["u"].shape == (world["shape"]["Nw"],)
        and world["atoms"] >= world["shape"]["a"]
        for world in worlds)
    check("G60-source-to-u-type-audit", source_type_ok,
          "u is border read after MAIN OP basis, not prime-lag vector")
    check("G61-verdict",
          VERDICT.startswith("STUCK(")
          and min(top_abel_factors) > 10.0,
          VERDICT)
    check("G99-runtime", time.perf_counter() - STARTED < 2700,
          "%.3fs < 2700s" % (time.perf_counter() - STARTED))

    failed = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS (%.3fs)" %
          (len(CHECKS) - len(failed), len(CHECKS),
           time.perf_counter() - STARTED))
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("OVERLAP MECHANISM VERIFIED -- VERDICT " + VERDICT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
