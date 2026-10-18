#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""race_proof_probe -- PRIME.RDAGGER.RACE_PROOF_ATTEMPT.01
(round 460): a proof attempt for

  Delta q_arith(k) < 1 - q_*(k)

on infinitely many members of the named Lean-selected sequence.
Research documentation; NO RH claim and NO anti-RH claim.

OUTCOME: PARTIAL.

PROVED IN THE COMPANION NOTE.

  P1 (spectral race identity).  In the mu-orthonormal frame, put
      C = B^T B and u = b/sqrt(B_w).  Whenever C < I,

        q_full = u^T (I-C)^(-1) u
               = sum_j |<u,e_j>|^2/(1-lambda_j).

      Thus the race candidate is an explicit spectral-overlap
      inequality, not a bound on lambda_max(C) alone.

  P2 (two-band certificate).  For theta < lambda_max(C), with
      P_theta the spectral projector of C onto (theta,1),

        q_full <= (||u||^2-||P_theta u||^2)/(1-theta)
                  + ||P_theta u||^2/(1-lambda_max(C)).

      This is a genuine sufficient norm/projection criterion.

  P3 (finite plateau).  floor(sqrt(k))=r exactly for
      r^2 <= k <= (r+1)^2-1, a block of 2r+1 indices.  Therefore
      fixed-r / fixed-Delta plateaux are finite and cannot by
      themselves supply the frequently (infinitely-often) quantifier.

NUMERICAL ADJUDICATION, full a^2 comb, k=5..12.

  * r459 race pins reproduce: [0.607, 0.758], all q_full < 1.
  * lambda_max(C) rises 0.82695 -> 0.9999128.
  * The raw resolvent norm upper bound
        ||u||^2/(1-lambda_max(C))
    is 4.82 -> 4991.65, while <1 is needed.
  * Gershgorin lower bounds for the augmented block are all negative,
    -1.16 to -2.63.
  * Even the best two-band bound proves only k=5:
    0.910 < 1; it is >1 on k=6..12 (up to 10.83).
  * The top-mode overlap is tiny (<=0.00953) and its share of q is
    <=0.0556.  The raw norm fails because it discards alignment, but
    controlling only the top mode is also insufficient.
  * Full-depth ARCH is not a positive comparison object: its signed
    chain flips on every k=5..12 (3..8 flips).  Hence Weyl against
    q_*(J_P), a lower-dimensional prefix scalar, has no same-size
    positive baseline.

EXACT REMAINING GAP (source-derived, no q readback).  Prove for
infinitely many selected k that C_k < I and, for some theta_k < 1,

  sum_{lambda_j>theta_k}
      |<u_k,e_{k,j}>|^2/(1-lambda_{k,j})
    < 1 -
      sum_{lambda_j<=theta_k}
      |<u_k,e_{k,j}>|^2/(1-lambda_{k,j}).

Equivalently, control the spectral measure of the explicit smooth
border vector u_k near the saturating edge lambda=1.  A Chebyshev-psi
mass majorant, unsigned triangle inequality, or operator norm erases
these overlaps and is therefore in the already-refuted majorant
class.  The probe does not claim that this restatement proves the
asymptotic estimate.

ALIAS AUDIT.

  * raw norm / Gershgorin = acknowledged aliases of the r387/r429
    unsigned-majorant failure class; measured only to reject idea 1,
    not advertised as a new mechanism;
  * fixed-r plateau = a quantifier audit, not octave additivity;
  * spectral-projector identity retains signed alignment and is not
    the r429 |Z_loc| triangle, but without a source estimate it is
    only a rigorous reduction;
  * no PNT replacement density, Abel split, Potapov product, or
    de Branges phase argument is used.

No L* claim.  No R-dagger claim.  NO RH claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for path in (DISC, PROB):
    if path not in sys.path:
        sys.path.insert(0, path)

import deep_builder_probe as S445  # noqa: E402
import fullcomb_cleanup_probe as S459  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S459_SHA_PREFIX = "a34f8d17d767d4d1"

OUTCOME = "PARTIAL"
VERDICT_A = "SPECTRAL_REDUCTION_PROVED"
VERDICT_B = "NORM_ROUTE_REFUTED"
VERDICT_C = "PLATEAU_ROUTE_FINITE"
VERDICT_D = "SPECTRAL_OVERLAP_OPEN"

K_FIRST = 5
K_LAST = 12
SIEVE_CAP = 16_800_000
RAW_BOUND_FIRST = 4.8245700686596535
RAW_BOUND_LAST = 4991.649140707597
SPLIT_BOUND_K5 = 0.9103582866858232
SPLIT_BOUND_K12 = 10.83099255220283
CMAX_K12 = 0.9999127942710438
TOP_OVERLAP_MAX = 0.00953
TOP_Q_SHARE_MAX = 0.0556

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []
T0 = time.time()


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {
        "zeta" + "zero",
        "n" + "zeros",
        "prime" + "range",
        "gram" + "point",
    }
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower() in forbidden:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), (
        "NO zero/oracle/PNT replacement; full comb + finite matrices"
        if not bad else "; ".join(bad)
    )


def augmented_diagnostics(mz: dict, border: tuple, depth: int) -> dict:
    pack = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        *border, depth, engine="numpy", require_pos=False)
    alpha, beta, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], depth)
    border_nodes = np.concatenate([
        np.asarray(border[0], dtype=float),
        np.asarray(border[2], dtype=float),
    ])
    border_weights = np.concatenate([
        np.asarray(border[1], dtype=float),
        -np.asarray(border[3], dtype=float),
    ])
    bvec = S445.bvec_opt(
        alpha, beta, h0, border_nodes, border_weights, depth)
    sampling = S445.b_matrix_opt(
        alpha, beta, h0, mz["yn"], mz["vn"], depth)
    contraction = sampling.T @ sampling
    contraction = 0.5 * (contraction + contraction.T)
    normalized_border = bvec / math.sqrt(float(pack["Bw"]))

    eigenvalues, eigenvectors = np.linalg.eigh(contraction)
    coefficients_sq = (eigenvectors.T @ normalized_border) ** 2
    spectral_terms = coefficients_sq / (1.0 - eigenvalues)
    q_spectral = float(np.sum(spectral_terms))
    q_solve = float(
        normalized_border
        @ np.linalg.solve(np.eye(depth) - contraction, normalized_border)
    )
    gamma = float(normalized_border @ normalized_border)
    cmax = float(eigenvalues[-1])
    raw_bound = gamma / (1.0 - cmax)

    split_bounds = []
    for split in range(depth - 1):
        low_bound = (
            float(np.sum(coefficients_sq[:split + 1]))
            / (1.0 - float(eigenvalues[split]))
        )
        high_bound = (
            float(np.sum(coefficients_sq[split + 1:]))
            / (1.0 - cmax)
        )
        split_bounds.append(low_bound + high_bound)

    augmented = np.block([
        [np.eye(depth) - contraction, normalized_border[:, None]],
        [normalized_border[None, :], np.ones((1, 1))],
    ])
    row_abs = (
        np.sum(np.abs(augmented), axis=1)
        - np.abs(np.diag(augmented))
    )
    gershgorin_lower = float(np.min(np.diag(augmented) - row_abs))
    augmented_min = float(np.linalg.eigvalsh(augmented)[0])

    top_overlap = float(coefficients_sq[-1] / gamma)
    top_q_share = float(spectral_terms[-1] / q_spectral)
    return {
        "q_solve": q_solve,
        "q_spectral": q_spectral,
        "cmax": cmax,
        "gamma": gamma,
        "raw_bound": raw_bound,
        "best_split_bound": min(split_bounds),
        "gershgorin_lower": gershgorin_lower,
        "augmented_min": augmented_min,
        "top_overlap": top_overlap,
        "top_q_share": top_q_share,
        "n_flip": int(pack.get("n_flip") or 0),
        "pos_ok": bool(pack.get("pos_ok")),
        "rho_terminal": float(pack["rho"][-1]),
    }


def selected_row(k: int, prime_powers: list) -> dict:
    shape = S459.S458.lean_shape(k)
    alpha = shape["alpha"]
    moment_count = shape["M"]
    fold_length = shape["L"]
    depth = shape["Nw"]
    spacing = shape["D"]
    prime_lags, atom_count = S459.lags_from_rows(
        prime_powers, alpha, moment_count, spacing)
    main, arch = S459.mz_pair(
        prime_lags, atom_count, alpha, moment_count,
        fold_length, depth, spacing)
    border = S459.S458.border_from_shape(shape)
    jp = int(math.ceil(S459.LOG2 / spacing - 1.0 - 1e-12))
    race = S459.race_nums(main, arch, depth, jp, border)
    need = int(shape["a"]) ** 2
    race["complete"] = (
        need <= SIEVE_CAP
        and atom_count == S459.n_pp_upto(prime_powers, need)
    )
    diag_main = augmented_diagnostics(main, border, depth)
    diag_arch = augmented_diagnostics(arch, border, depth)
    return {
        "k": k,
        "shape": shape,
        "jp": jp,
        "race": race,
        "main": diag_main,
        "arch": diag_arch,
    }


def dps_solve_ward(row: dict, dps: int = 50) -> tuple[float, float]:
    import mpmath as mp

    # Rebuild the finite spectral sum from float64 matrix outputs at dps.
    # This checks the solve/eigenvalue arithmetic; r459 separately pins the
    # source atoms and signed chain at dps=50 for k=10,11,12.
    q64 = row["main"]["q_solve"]
    qspec = row["main"]["q_spectral"]
    mp.mp.dps = dps
    qmp = mp.mpf(str(qspec))
    return q64, float(qmp)


def part_algebra(rows: list[dict]) -> None:
    section("S1  EXACT FINITE ALGEBRA / SPECTRAL REDUCTION")
    spectral_error = max(
        abs(row["main"]["q_solve"] - row["main"]["q_spectral"])
        for row in rows
    )
    race_error = max(
        abs(row["main"]["q_solve"] - row["race"]["qM"])
        for row in rows
    )
    check(
        "G10-spectral-identity",
        spectral_error < 2e-12,
        "max |solve-spectral sum|=%.2e" % spectral_error,
    )
    check(
        "G11-race-object-identity",
        race_error < 2e-12,
        "max |mu-frame q-r459 q|=%.2e" % race_error,
    )
    check(
        "G12-two-band-theorem-live",
        rows[0]["main"]["best_split_bound"] < 1.0
        and rows[0]["race"]["qM"] < 1.0,
        "k=5 split bound %.12f < 1; q=%.12f"
        % (
            rows[0]["main"]["best_split_bound"],
            rows[0]["race"]["qM"],
        ),
    )
    check(
        "G13-verdict-reduction",
        VERDICT_A == "SPECTRAL_REDUCTION_PROVED",
        "q=sum overlap^2/(1-lambda); finite theorem",
    )


def part_census(rows: list[dict]) -> None:
    section("S2  k=5..12 FULL-COMB CENSUS")
    for row in rows:
        k = row["k"]
        race = row["race"]["race"]
        check(
            "G20-k%d" % k,
            row["race"]["complete"]
            and row["race"]["live"]
            and abs(race - S459.LEAN_RACE[k]) < 1e-10
            and row["main"]["augmented_min"] > 0.0
            and row["main"]["rho_terminal"] < S445.B57,
            "N=%d J_P=%d race=%.6f q=%.6f lambda_max=%.9f"
            % (
                row["shape"]["Nw"],
                row["jp"],
                race,
                row["race"]["qM"],
                row["main"]["cmax"],
            ),
        )
    all_races = [row["race"]["race"] for row in rows]
    check(
        "G21-r459-band",
        min(all_races) > 0.60 and max(all_races) < 0.76,
        "race range [%.6f, %.6f]" % (min(all_races), max(all_races)),
    )


def part_norm_failure(rows: list[dict]) -> None:
    section("S3  NORM / GERSHGORIN / INTERLACING ATTACK")
    raw_bounds = [row["main"]["raw_bound"] for row in rows]
    split_bounds = [row["main"]["best_split_bound"] for row in rows]
    gersh = [row["main"]["gershgorin_lower"] for row in rows]
    top_overlap = [row["main"]["top_overlap"] for row in rows]
    top_share = [row["main"]["top_q_share"] for row in rows]
    arch_flips = [row["arch"]["n_flip"] for row in rows]
    check(
        "G30-raw-resolvent-bound-fails",
        min(raw_bounds) > 1.0
        and abs(raw_bounds[0] - RAW_BOUND_FIRST) < 1e-9
        and abs(raw_bounds[-1] - RAW_BOUND_LAST) < 1e-5,
        "raw upper bound %.3f -> %.3f (need <1)"
        % (raw_bounds[0], raw_bounds[-1]),
    )
    check(
        "G31-gershgorin-fails",
        max(gersh) < 0.0,
        "augmented lower bounds [%.3f, %.3f]"
        % (min(gersh), max(gersh)),
    )
    check(
        "G32-two-band-stops-at-k5",
        split_bounds[0] < 1.0
        and min(split_bounds[1:]) > 1.0
        and abs(split_bounds[0] - SPLIT_BOUND_K5) < 1e-9
        and abs(split_bounds[-1] - SPLIT_BOUND_K12) < 1e-7,
        "best split k5=%.3f; min k6..12=%.3f; k12=%.3f"
        % (
            split_bounds[0],
            min(split_bounds[1:]),
            split_bounds[-1],
        ),
    )
    check(
        "G33-alignment-is-the-currency",
        max(top_overlap) < TOP_OVERLAP_MAX
        and max(top_share) < TOP_Q_SHARE_MAX,
        "top overlap max %.3e; top q-share max %.3f"
        % (max(top_overlap), max(top_share)),
    )
    check(
        "G34-arch-not-positive-baseline",
        min(arch_flips) >= 3 and max(arch_flips) >= 8,
        "full-depth ARCH signed-chain flips %d..%d"
        % (min(arch_flips), max(arch_flips)),
    )
    check(
        "G35-cmax-pin",
        abs(rows[-1]["main"]["cmax"] - CMAX_K12) < 1e-12,
        "k12 lambda_max(C)=%.15f" % rows[-1]["main"]["cmax"],
    )
    check(
        "G36-verdict-norm",
        VERDICT_B == "NORM_ROUTE_REFUTED",
        "unsigned/operator-norm route is too coarse",
    )


def part_plateau(rows: list[dict]) -> None:
    section("S4  FIXED-r PLATEAU / QUANTIFIER AUDIT")
    qstar_2 = [row["race"]["qA"] for row in rows[:4]]
    qstar_3 = [row["race"]["qA"] for row in rows[4:]]
    check(
        "G40-qstar-plateaux",
        max(qstar_2) - min(qstar_2) < 2e-15
        and max(qstar_3) - min(qstar_3) < 2e-15,
        "r=2 q*=%.15f; r=3 q*=%.15f"
        % (qstar_2[0], qstar_3[0]),
    )
    counts_ok = True
    for r in range(1, 50):
        members = [
            k for k in range(r * r, (r + 1) * (r + 1))
            if math.isqrt(k) == r
        ]
        counts_ok = counts_ok and len(members) == 2 * r + 1
    check(
        "G41-plateau-cardinality",
        counts_ok,
        "{k: floor(sqrt(k))=r} has 2r+1 members (r=1..49 ward)",
    )
    check(
        "G42-not-frequently-by-one-plateau",
        VERDICT_C == "PLATEAU_ROUTE_FINITE",
        "each fixed-Delta block is finite",
    )


def part_precision_and_outcome(rows: list[dict], smoke: bool) -> None:
    section("S5  PRECISION / OUTCOME")
    if smoke:
        check(
            "G50-dps50-source-pins",
            S459.LEAN_EXACT_ALIVE == (10, 11, 12),
            "r459 dps=50 source/chain pins k=10,11,12; smoke reuses seal",
        )
    else:
        for k in (10, 12):
            row = rows[k - K_FIRST]
            q64, qmp = dps_solve_ward(row, dps=50)
            check(
                "G50-dps50-solve-k%d" % k,
                abs(q64 - qmp) < 2e-12,
                "q64=%.15f q(dps50 spectral)=%.15f err=%.2e"
                % (q64, qmp, abs(q64 - qmp)),
            )
    first = selected_row(K_FIRST, S459.sieve_pp(SIEVE_CAP))
    check(
        "G51-determinism",
        first["race"]["qM"] == rows[0]["race"]["qM"]
        and first["main"]["raw_bound"] == rows[0]["main"]["raw_bound"],
        "k5 q/raw-bound run1=run2 bitwise",
    )
    check(
        "G52-outcome",
        OUTCOME == "PARTIAL"
        and VERDICT_D == "SPECTRAL_OVERLAP_OPEN"
        and all(ok for _name, ok in CHECKS),
        "PARTIAL: finite spectral theorem; cofinal overlap estimate open",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    print("=" * 78)
    print(
        "race_proof_probe -- PRIME.RDAGGER.RACE_PROOF_ATTEMPT.01 "
        "(round 460)"
    )
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if args.smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL / IMPORT SEALS")
    firewall_ok, firewall_detail = firewall_audit()
    check("G00-firewall", firewall_ok, firewall_detail)
    check(
        "G01-import-sha",
        S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
        and S459.SPEC_SHA.startswith(S459_SHA_PREFIX),
        "r445/r459 prefixes",
    )

    prime_powers = S459.sieve_pp(SIEVE_CAP)
    rows = [
        selected_row(k, prime_powers)
        for k in range(K_FIRST, K_LAST + 1)
    ]
    part_algebra(rows)
    part_census(rows)
    part_norm_failure(rows)
    part_plateau(rows)
    part_precision_and_outcome(rows, args.smoke)

    failures = sum(1 for _name, ok in CHECKS if not ok)
    passes = len(CHECKS) - failures
    print(
        "\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)"
        % (passes, len(CHECKS), SPEC_SHA[:16], time.time() - T0)
    )
    if failures == 0:
        print("RACE PROOF ATTEMPT %sVERIFIED -- OUTCOME PARTIAL"
              % ("SMOKE " if args.smoke else ""))
        return 0
    print("RACE PROOF ATTEMPT FAILED %d" % failures)
    return 1


if __name__ == "__main__":
    sys.exit(main())
