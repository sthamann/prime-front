#!/usr/bin/env python3
"""Nyman--Beurling dyadic block-capture probe (experiment only).

The production ladder uses the Vasyunin cotangent closed form and float64
Cholesky after high-precision entry and N=32 solve checks.  This is intentional:
an O(N^3) mpmath solve at N=512 does not fit the five-minute contract, while the
observed condition numbers and independent checks support the requested eight
displayed digits.  No asymptotic or RH claim is inferred from the ladder.
"""

from __future__ import annotations

import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sla


OUTPUT = Path(__file__).with_name("nb_dyadic_capture_probe_result.json")
MAX_INDEX = 1024
LADDER = (8, 16, 32, 64, 128, 256, 512)
MP_DPS = 80
USER_E = {
    8: 0.02424453,
    16: 0.01793627,
    32: 0.01407701,
    64: 0.01139247,
    128: 0.00967035,
    256: 0.008242256,
}
USER_ETA = {
    8: 0.06398542,
    16: 0.10074020,
    32: 0.12003952,
    64: 0.11520039,
    128: 0.12526017,
}


class MpVasyuninGram:
    def __init__(self) -> None:
        self.constant = mp.log(2 * mp.pi) - mp.euler
        self.cot: dict[int, list[mp.mpf]] = {}
        self.values: dict[tuple[int, int], mp.mpf] = {}

    def V(self, p: int, q: int) -> mp.mpf:
        if q == 1 or p == 0:
            return mp.mpf(0)
        if q not in self.cot:
            self.cot[q] = [mp.cot(mp.pi * j / q) for j in range(1, q)]
        return mp.fsum(
            mp.mpf((j * p) % q) / q * self.cot[q][j - 1]
            for j in range(1, q)
        )

    def e(self, m: int, n: int) -> mp.mpf:
        if m > n:
            m, n = n, m
        d = math.gcd(m, n)
        p, q = m // d, n // d
        key = (p, q)
        if key not in self.values:
            pp, qq = mp.mpf(p), mp.mpf(q)
            self.values[key] = (
                self.constant / 2 * (1 / pp + 1 / qq)
                + (qq - pp) / (2 * pp * qq) * mp.log(pp / qq)
                - mp.pi
                / (2 * pp * qq)
                * (self.V(p, q) + self.V(q % p if p > 1 else 0, p))
            )
        return self.values[key] / d

    def r(self, m: int, n: int) -> mp.mpf:
        return (
            self.e(m, n)
            - self.e(m, 1) / n
            - self.e(1, n) / m
            + self.e(1, 1) / (m * n)
        )


def periodic_r_inner(m: int, n: int) -> mp.mpf:
    period = math.lcm(m, n)
    total = mp.mpf(0)
    for r in range(1, period + 1):
        coefficient = mp.mpf(r % m) * (r % n) / (m * n)
        if coefficient:
            tail = (
                mp.digamma(mp.mpf(r + 1) / period)
                - mp.digamma(mp.mpf(r) / period)
            ) / period
            total += coefficient * tail
    return total


def periodic_r_mean(n: int) -> mp.mpf:
    total = mp.mpf(0)
    for r in range(1, n + 1):
        coefficient = mp.mpf(r % n) / n
        if coefficient:
            total += coefficient * (
                mp.digamma(mp.mpf(r + 1) / n)
                - mp.digamma(mp.mpf(r) / n)
            ) / n
    return total


def build_e_gram_f64(limit: int) -> np.ndarray:
    constant = float(mp.log(2 * mp.pi) - mp.euler)
    v_tables: list[np.ndarray | None] = [None, np.zeros(1)]
    for q in range(2, limit + 1):
        j = np.arange(1, q, dtype=np.int64)
        cotangent = 1.0 / np.tan(np.pi * j / q)
        numerators = np.arange(1, q, dtype=np.int64)
        numerators = numerators[np.gcd(numerators, q) == 1]
        table = np.full(q, np.nan)
        for start in range(0, numerators.size, 128):
            block = numerators[start : start + 128]
            fractions = ((block[:, None] * j[None, :]) % q) / float(q)
            table[block] = fractions @ cotangent
        v_tables.append(table)

    gram = np.zeros((limit, limit))
    indices = np.arange(1, limit + 1, dtype=float)
    gram[np.arange(limit), np.arange(limit)] = constant / indices
    for q in range(2, limit + 1):
        numerators = np.arange(1, q, dtype=np.int64)
        numerators = numerators[np.gcd(numerators, q) == 1]
        first = v_tables[q][numerators]  # type: ignore[index]
        second = np.array(
            [
                v_tables[p][q % p] if p > 1 else 0.0  # type: ignore[index]
                for p in numerators
            ]
        )
        pf = numerators.astype(float)
        values = (
            0.5 * constant * (1.0 / pf + 1.0 / q)
            + (q - pf) / (2.0 * pf * q) * np.log(pf / q)
            - np.pi / (2.0 * pf * q) * (first + second)
        )
        for d in range(1, limit // q + 1):
            rows = d * numerators - 1
            column = d * q - 1
            gram[rows, column] = values / d
            gram[column, rows] = values / d
    return gram


def build_r_system(limit: int) -> tuple[np.ndarray, np.ndarray]:
    e_gram = build_e_gram_f64(limit)
    indices = np.arange(2, limit + 1, dtype=float)
    e_mean = (1.0 - float(mp.euler) + np.log(np.arange(1, limit + 1))) / np.arange(
        1, limit + 1
    )
    r_gram = (
        e_gram[1:, 1:]
        - e_gram[1:, [0]] / indices[None, :]
        - e_gram[[0], 1:] / indices[:, None]
        + e_gram[0, 0] / (indices[:, None] * indices[None, :])
    )
    r_mean = e_mean[1:] - e_mean[0] / indices
    return r_gram, r_mean


def high_precision_checks(r_gram: np.ndarray, r_mean: np.ndarray) -> dict[str, object]:
    mp.mp.dps = MP_DPS
    gram = MpVasyuninGram()
    pairs = ((2, 2), (2, 3), (3, 5), (4, 6), (7, 12), (9, 10))
    periodic_errors = [
        abs(gram.r(m, n) - periodic_r_inner(m, n)) for m, n in pairs
    ]
    mean_errors = [
        abs(periodic_r_mean(n) - mp.log(n) / n) for n in (2, 3, 5, 8)
    ]
    entry_errors = [
        abs(mp.mpf(r_gram[m - 2, n - 2]) - gram.r(m, n))
        / abs(gram.r(m, n))
        for m, n in pairs
    ]

    dimension = 31  # r_2,...,r_32
    matrix = mp.matrix(dimension)
    vector = mp.matrix(dimension, 1)
    for i, m in enumerate(range(2, 33)):
        vector[i] = mp.log(m) / m
        for j, n in enumerate(range(2, 33)):
            matrix[i, j] = gram.r(m, n)
    solution = mp.cholesky_solve(matrix, vector)
    e_mp = 1 - mp.fdot(vector, solution)
    factor = sla.cho_factor(r_gram[:dimension, :dimension])
    e_f64 = 1 - r_mean[:dimension] @ sla.cho_solve(factor, r_mean[:dimension])
    return {
        "mp_dps": MP_DPS,
        "periodic_digamma_vs_vasyunin_max_abs": mp.nstr(max(periodic_errors), 12),
        "mean_formula_max_abs": mp.nstr(max(mean_errors), 12),
        "float_entry_max_relative": mp.nstr(max(entry_errors), 12),
        "E_32_mpmath": mp.nstr(e_mp, 18),
        "E_32_float64": e_f64,
        "E_32_relative_difference": float(abs(e_mp - e_f64) / e_mp),
    }


def ladder_rows(r_gram: np.ndarray, r_mean: np.ndarray) -> list[dict[str, object]]:
    rows = []
    errors: dict[int, float] = {}
    factors: dict[int, tuple[np.ndarray, bool]] = {}
    for n in (*LADDER, 1024):
        dimension = n - 1
        factors[n] = sla.cho_factor(r_gram[:dimension, :dimension])
        coefficients = sla.cho_solve(factors[n], r_mean[:dimension])
        errors[n] = float(1 - r_mean[:dimension] @ coefficients)

    for n in LADDER:
        dimension = n - 1
        factor = factors[n]
        residual_coefficients = sla.cho_solve(factor, r_mean[:dimension])
        block_indices = np.arange(n // 2 + 1, n + 1)
        transform = np.zeros((2 * n - 1, len(block_indices)))
        for column, index in enumerate(block_indices):
            transform[2 * index - 2, column] = 2.0
            transform[index - 2, column] = -1.0
        full = r_gram[: 2 * n - 1, : 2 * n - 1]
        cross = r_gram[:dimension, : 2 * n - 1] @ transform
        block = transform.T @ full @ transform
        block_mean = r_mean[: 2 * n - 1] @ transform
        schur = block - cross.T @ sla.cho_solve(factor, cross)
        residual_block_mean = block_mean - cross.T @ residual_coefficients
        eta = float(
            residual_block_mean
            @ np.linalg.solve(schur, residual_block_mean)
            / errors[n]
        )
        total_eta = 1.0 - errors[2 * n] / errors[n]
        condition = float(np.linalg.cond(r_gram[:dimension, :dimension]))
        rows.append(
            {
                "N": n,
                "E_N": errors[n],
                "eta_k": eta,
                "k_eta_k": math.log2(n) * eta,
                "total_dyadic_capture": total_eta,
                "capture_fraction_of_total": eta / total_eta,
                "condition_number": condition,
                "user_E_absolute_difference": (
                    abs(errors[n] - USER_E[n]) if n in USER_E else None
                ),
                "user_eta_absolute_difference": (
                    abs(eta - USER_ETA[n]) if n in USER_ETA else None
                ),
            }
        )
    return rows


def main() -> int:
    started = time.time()
    r_gram, r_mean = build_r_system(MAX_INDEX)
    precision = high_precision_checks(r_gram, r_mean)
    rows = ladder_rows(r_gram, r_mean)
    burnol_simple_rh_constant = float(2 + mp.euler - mp.log(4 * mp.pi))
    fitted_constant = float(
        np.mean([row["E_N"] * math.log(row["N"]) for row in rows[-3:]])
    )
    max_user_e_error = max(
        row["user_E_absolute_difference"]
        for row in rows
        if row["user_E_absolute_difference"] is not None
    )
    max_user_eta_error = max(
        row["user_eta_absolute_difference"]
        for row in rows
        if row["user_eta_absolute_difference"] is not None
    )
    result = {
        "claim_boundary": "Experiment only; no RH claim.",
        "verdict": "MEASURED",
        "basis": (
            "r_n(x)={1/(nx)}-(1/n){1/x}; V_N=span(r_2,...,r_N); "
            "<1,r_n>=log(n)/n"
        ),
        "block": (
            "u_n=2r_(2n)-r_n; <1,u_n>=||u_n||^2=log(2)/n; "
            "eta_k=||Proj_W R_N||^2/E_N"
        ),
        "precision_checks": precision,
        "rows": rows,
        "agreement": {
            "max_user_E_absolute_difference": max_user_e_error,
            "max_user_eta_absolute_difference": max_user_eta_error,
            "displayed_digits_reproduced": (
                max_user_e_error < 5e-9 and max_user_eta_error < 5e-9
            ),
        },
        "burnol": {
            "unconditional_safe_statement": (
                "liminf E_N log N >= sum_{Re rho=1/2} "
                "m(rho)^2/|rho|^2"
            ),
            "under_RH_and_simple_zeros_constant": burnol_simple_rh_constant,
            "constant_closed_form": "2+EulerGamma-log(4*pi)",
        },
        "rate_comparison": {
            "fit_C_mean_last_three_for_E_N_approx_C_over_log_N": fitted_constant,
            "fit_over_Burnol_simple_RH_constant": (
                fitted_constant / burnol_simple_rh_constant
            ),
            "interpretation": (
                "k*eta_k near one is compatible with a 1/log N rate but "
                "oscillates and does not establish a limit."
            ),
        },
        "classification": (
            "The eta lower bound is a well-posed positive-geometry conjecture "
            "stronger than a bare Baez-Duarte rate statement: it requires the "
            "dyadic block itself to capture a harmonic fraction of the residual."
        ),
        "literature_search_note": (
            "No occurrence of u_n=2r_(2n)-r_n was found in the searched "
            "Nyman--Beurling literature; this is an absence-of-hit report, not "
            "a priority claim."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("VERDICT MEASURED")
    for row in rows:
        print(
            "N={N:4d} E={E_N:.12f} eta={eta_k:.10f} "
            "k_eta={k_eta_k:.10f} cond={condition_number:.3e}".format(**row)
        )
    print(
        f"C_fit={fitted_constant:.12f} C_Burnol={burnol_simple_rh_constant:.12f} "
        f"runtime={time.time() - started:.3f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
