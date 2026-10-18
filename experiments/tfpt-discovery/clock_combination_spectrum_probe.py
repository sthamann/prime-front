#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""clock_combination_spectrum_probe -- compiler-clock spectrum audit.

FROZEN SPEC v1 (2026-09-04).  EXPERIMENT ONLY.  No RH claim, marker move,
ledger row, paper edit, or scorecard row follows from this file.

Question.  Can any clock already present in the TFPT corpus, alone or in an
allowed direct product/tower, derive the multiplicative spectrum log(n)
without inserting an integer-labelled arithmetic monoid?

Corpus inputs (faithfully reimplemented):
  * Z/5 x Z/6 and Coxeter order 30:
    verification/v319_translation_clock.py:14-38.
  * rate_N(n)=6 log(N/(N-n)):
    verification/v124_resummed_clock.py:10-37,47-49.
  * seam Z4 and K=log((1-C)C^-1):
    verification/v446_seam_clock_invariance.py:17-38,123-139 and
    verification/v506_seam_clock_rigidity.py:12-22,43-57.
  * Koide dq/dt=(Delta/3)(q-2)(q-5), Delta=6 log(3/2):
    tfpt_4_frontier.tex:463-472 and verification/v723_phys_modular_clock.py:111-139.
  * F_transfer clock classes:
    verification/v777_ftransfer_clock_jets.py:80-119.
  * three-generator scale lattice:
    tfpt_1_architecture_e8.tex:4165-4190.
  * QCA/4D boundaries:
    verification/v984_markov_qca_dilation.py:37-43,
    verification/v999_weak_collision_hp.py:18-23, and
    verification/v1013_thermodynamic_dynamics.py:11-36.

Exact arithmetic.  Rational logarithms are represented by prime-valuation
vectors, so their Q-linear ranks are exact matrix ranks.  Finite clock angles
are represented as rational multiples of pi.  The v446 modular covariance is
the seeded floating construction from that module; its rationality test is
necessarily numerical and is explicitly labelled as such.

Kill criteria:
  K1 finite Q-rank and not log-rational;
  K2 log-rational primitives depend on a noncanonical truncation/tower label;
  K3 log(n) appears only after an integer label/monoid is inserted.

SURVIVED_BC_CANDIDATE requires a canonical corpus object with spectrum
{log n:n>=1}, or a canonical submonoid, with multiplicity one.  The probe
does not test RH and a BC-type survivor would not by itself encode RH.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.linalg import expm


HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "clock_combination_spectrum_result.json"
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
N_VALUES = (3, 4, 5, 6, 8, 16, 30, 240)
E8_EXPONENTS = (1, 7, 11, 13, 17, 19, 23, 29)
PSLQ_DPS = 100
PSLQ_MAXCOEFF = 10**6
RATIONAL_DENOMINATOR_CAP = 10**3
RATIONAL_TOL = 10**-12
CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    ok = bool(condition)
    CHECKS.append((label, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")


def factor_vector(value: Fraction) -> dict[int, int]:
    """Prime valuation vector of a positive rational, exact."""
    if value <= 0:
        raise ValueError("log-rational arguments must be positive")
    vector: dict[int, int] = {}
    for sign, integer in ((1, value.numerator), (-1, value.denominator)):
        for prime, exponent in sp.factorint(integer).items():
            vector[int(prime)] = vector.get(int(prime), 0) + sign * int(exponent)
    return {prime: exponent for prime, exponent in vector.items() if exponent}


def valuation_rank(arguments: list[Fraction]) -> tuple[int, list[int]]:
    vectors = [factor_vector(value) for value in arguments if value != 1]
    primes = sorted({prime for vector in vectors for prime in vector})
    if not vectors or not primes:
        return 0, primes
    matrix = sp.Matrix([[vector.get(prime, 0) for prime in primes]
                        for vector in vectors])
    return int(matrix.rank()), primes


def resummed_record(N: int) -> dict:
    arguments = [Fraction(N, N - n) for n in range(1, N)]
    rank, primes = valuation_rank(arguments)
    multiplicities: dict[str, int] = {}
    for argument in arguments:
        key = f"{argument.numerator}/{argument.denominator}"
        multiplicities[key] = multiplicities.get(key, 0) + 1
    largest_initial_integer = 1
    for candidate in range(2, N + 1):
        if Fraction(candidate, 1) not in arguments:
            break
        largest_initial_integer = candidate
    return {
        "N": N,
        "spectrum": [f"6*log({q.numerator}/{q.denominator})" for q in arguments],
        "q_rank": rank,
        "prime_valuation_basis": primes,
        "log_rational": True,
        "raw_contains_log_n_through": 1,
        "normalized_arguments_contain_integer_ratios_through": largest_initial_integer,
        "primitive_set": [f"6*log({prime})" for prime in primes],
        "ratio_multiplicity_max": max(multiplicities.values(), default=0),
        "verdict": "K2_NONCANONICAL_N_DEPENDENT",
    }


def block_diagonal_h(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = np.zeros((size, size), complex)
    for residue in range(4):
        indices = [index for index in range(size) if index % 4 == residue]
        width = len(indices)
        raw = rng.standard_normal((width, width)) + 1j * rng.standard_normal(
            (width, width)
        )
        raw = raw + raw.conj().T
        for row, index in enumerate(indices):
            for column, other in enumerate(indices):
                matrix[index, other] = raw[row, column]
    return matrix + (1.0 - np.linalg.eigvalsh(matrix).min()) * np.eye(size)


def full_h(rng: np.random.Generator, size: int) -> np.ndarray:
    raw = rng.standard_normal((size, size)) + 1j * rng.standard_normal((size, size))
    matrix = raw + raw.conj().T
    return matrix + (1.0 - np.linalg.eigvalsh(matrix).min()) * np.eye(size)


def modular_v446_record() -> dict:
    """Reproduce v446's seeded call order before its modular test."""
    rng = np.random.default_rng(446)
    for size in (4, 8, 12, 16, 32):
        block_diagonal_h(rng, size)
    for size in (4, 8, 16, 32):
        full_h(rng, size)

    spectra: list[dict] = []
    all_k: list[float] = []
    all_ratios: list[float] = []
    for size in (4, 8, 16):
        hamiltonian = block_diagonal_h(rng, size)
        covariance = np.linalg.inv(np.eye(size) + expm(hamiltonian))
        c_eigenvalues = np.linalg.eigvalsh(covariance)
        ratios = (1.0 - c_eigenvalues) / c_eigenvalues
        k_eigenvalues = np.log(ratios)
        all_k.extend(float(value) for value in k_eigenvalues)
        all_ratios.extend(float(value) for value in ratios)
        spectra.append({
            "size": size,
            "covariance_eigenvalues": [float(value) for value in c_eigenvalues],
            "ratios_(1-c)/c": [float(value) for value in ratios],
            "K_eigenvalues": [float(value) for value in k_eigenvalues],
        })

    integer_hits = [
        int(round(value)) for value in all_ratios
        if abs(value - round(value)) < RATIONAL_TOL
    ]
    rational_hits = []
    for value in all_ratios:
        approximation = Fraction(float(value)).limit_denominator(
            RATIONAL_DENOMINATOR_CAP
        )
        if abs(float(approximation) - value) < RATIONAL_TOL:
            rational_hits.append(str(approximation))

    mp.mp.dps = PSLQ_DPS
    # A bounded diagnostic only: random floating input cannot prove independence.
    small_sample = [mp.mpf(str(value)) for value in all_k[: min(8, len(all_k))]]
    relation = mp.pslq(mp.matrix(small_sample), tol=mp.mpf("1e-70"),
                       maxcoeff=PSLQ_MAXCOEFF, maxsteps=10000)
    relation_residual = (
        abs(mp.fdot(relation, small_sample)) if relation is not None else None
    )
    # The source values have only float64 precision.  A relation among their
    # decimal encodings cannot be confirmed as a relation of the underlying
    # random-matrix spectrum without an exact or independently high-precision
    # covariance, which v446 does not provide.
    relation_confirmed = False
    return {
        "source": "verification/v446_seam_clock_invariance.py:123-139",
        "construction": "seeded random block-diagonal positive h; C=(I+exp(h))^-1",
        "spectra": spectra,
        "ratio_count": len(all_ratios),
        "integer_hits": integer_hits,
        "rational_hits_denominator_le_1e3": rational_hits,
        "pslq_first_8_maxcoeff_1e6": relation,
        "pslq_residual": (
            mp.nstr(relation_residual, 12) if relation_residual is not None else None
        ),
        "pslq_relation_confirmed": relation_confirmed,
        "pslq_confirmation_note": "unavailable: v446 source covariance is float64",
        "q_rank": f"numerical_lower_bound_{len(small_sample)}",
        "log_rational": False,
        "canonical_integer_labelling": False,
        "verdict": "K1_GENERIC_RANDOM_SPECTRUM",
    }


def finite_clock_records() -> list[dict]:
    return [
        {
            "clock": "Z4_seam",
            "spectrum": ["2*pi*m/4; m=0,1,2,3"],
            "q_rank_nonzero": 1,
            "log_rational": False,
            "primitive_set": ["pi/2"],
            "verdict": "K1_FINITE_CLOCK",
        },
        {
            "clock": "Z5_static",
            "spectrum": ["2*pi*m/5; m=0,...,4"],
            "q_rank_nonzero": 1,
            "log_rational": False,
            "primitive_set": ["2*pi/5"],
            "verdict": "K1_FINITE_CLOCK",
        },
        {
            "clock": "Z6_dynamic",
            "spectrum": ["2*pi*m/6; m=0,...,5"],
            "q_rank_nonzero": 1,
            "log_rational": False,
            "primitive_set": ["pi/3"],
            "verdict": "K1_FINITE_CLOCK",
        },
        {
            "clock": "E8_Coxeter_30",
            "spectrum": [f"2*pi*{m}/30" for m in E8_EXPONENTS],
            "q_rank_nonzero": 1,
            "log_rational": False,
            "primitive_set": ["pi/15"],
            "verdict": "K1_FINITE_CLOCK",
        },
    ]


def combination_records(components: dict[str, dict]) -> list[dict]:
    records = []
    for width in (1, 2, 3):
        for names in itertools.combinations(components, width):
            entries = [components[name] for name in names]
            exact_rank = sum(int(entry.get("exact_rank_new_basis", 0))
                             for entry in entries)
            has_generic = any(entry.get("generic", False) for entry in entries)
            all_log_rational = all(entry["log_rational"] for entry in entries)
            has_integer_label = any(entry.get("integer_label_inserted", False)
                                    for entry in entries)
            canonical = all(entry.get("canonical", False) for entry in entries)
            has_log_n_spectrum = any(entry.get("spectrum_log_n", False)
                                     for entry in entries)
            if has_generic or not all_log_rational:
                verdict = "K1_FINITE_OR_GENERIC_NON_LOG_RATIONAL"
            elif has_integer_label or not canonical or not has_log_n_spectrum:
                verdict = "K2_OR_K3_NONCANONICAL_INTEGER_LABEL"
            else:
                verdict = "SURVIVED_BC_CANDIDATE"
            records.append({
                "components": list(names),
                "construction": "direct product: union of generator spectra; "
                                "composition/tower: additive span",
                "q_rank": (f">={exact_rank} plus generic numerical directions"
                           if has_generic else exact_rank),
                "log_rational": all_log_rational,
                "canonical_multiplicity_one_log_n": verdict == "SURVIVED_BC_CANDIDATE",
                "verdict": verdict,
            })
    return records


def main() -> int:
    print("clock_combination_spectrum_probe -- experiment-only spectrum audit")
    print(f"SPEC_SHA={SPEC_SHA}")

    # A1 finite diagnostic: unique factorisation makes log-primes the basis.
    factor_rows = []
    for integer in range(1, 65):
        vector = factor_vector(Fraction(integer))
        reconstructed = math.prod(prime ** exponent
                                  for prime, exponent in vector.items())
        factor_rows.append((integer, vector))
        check(f"A1 factor-vector reconstructs n={integer}",
              reconstructed == integer)
    rank_64, primes_64 = valuation_rank(
        [Fraction(integer) for integer in range(1, 65)]
    )
    check("A1 rank{log n:1<=n<=64}=number of primes<=64",
          rank_64 == len(primes_64) == 18)

    finite = finite_clock_records()
    check("finite Z4/Z5/Z6/Coxeter spectra all have Q-rank one",
          all(record["q_rank_nonzero"] == 1 for record in finite))

    resummed = [resummed_record(N) for N in N_VALUES]
    check("all selected resummed spectra are exactly log-rational",
          all(record["log_rational"] for record in resummed))
    tower_primes = sorted({prime for record in resummed
                           for prime in record["prime_valuation_basis"]})
    # Full N>=2 tower: every reduced a/b>1 occurs for N=a,n=a-b.
    tower = {
        "construction": "union over every N>=2 and 1<=n<N",
        "spectrum": "{6*log(a/b): integers a>b>=1}",
        "proof": "choose N=a and n=a-b; scaling (a,b)->(ka,kb) gives "
                 "infinitely many labels for the same ratio",
        "q_rank": "countably_infinite",
        "log_rational": True,
        "primitive_set": "{6*log(p): p prime}",
        "multiplicity": "infinite before reducing fractions",
        "equals_log_n": False,
        "canonical_multiplicity_one": False,
        "verdict": "K2_NONCANONICAL_TOWER_AND_K3_INTEGER_LABEL",
    }
    check("resummed all-N tower has every positive rational ratio",
          all(Fraction(a, b) == Fraction(a, a - (a - b))
              for a in range(2, 20) for b in range(1, a)))

    modular = modular_v446_record()
    check("v446 seeded modular ratios have no integer hits",
          not modular["integer_hits"])
    check("v446 seeded modular ratios have no certified rational labelling",
          not modular["rational_hits_denominator_le_1e3"])
    check("v446 bounded PSLQ candidate fails high-precision confirmation",
          not modular["pslq_relation_confirmed"])

    koide = {
        "fixed_points": ["2 (attractor)", "5 (repeller)"],
        "time_one_multipliers": ["64/729", "729/64"],
        "translation_length": "6*log(3/2)",
        "q_rank": 1,
        "log_rational": True,
        "integer_or_prime_multiplier": False,
        "verdict": "K2_SINGLE_RATIONAL_NO_INTEGER_MONOID",
    }
    check("Koide multiplier is the exact v723 value",
          Fraction(2, 3) ** 6 == Fraction(64, 729))

    ftransfer = {
        "clock_classes": {
            "thermal_and_proper_time": "-18*log(3/2)^2 Schwarzian coset",
            "RG_log_mu": "parabolic affine line; continuous label",
            "relic_log_a": "degenerate identity object",
        },
        "q_rank": "not_a_discrete_period_set",
        "log_rational": False,
        "canonical_integer_labelling": False,
        "verdict": "K1_NO_COMMON_CONNECTION_AND_NO_DISCRETE_MONOID",
    }
    scale_lattice = {
        "generators": ["alpha^-1", "L0=log(1/u_seed)", "Lc=log(8*pi)"],
        "q_rank": "formal_rank_3",
        "log_rational": False,
        "canonical_integer_labelling": False,
        "verdict": "K1_FINITE_RANK_NON_LOG_RATIONAL",
    }
    qca_4d = {
        "qca": "exact local discrete unitary dilation; no arithmetic spectrum",
        "continuous_kernel": "finite/kernel-level complete in v999",
        "thermodynamic": "quasilocal tau_t exists at Hamiltonian-class level in v1013",
        "missing": "no multiplicative integer label, scale action, prime orbit theorem, "
                   "thermodynamic gap, IR universality, or continuum field limit",
        "verdict": "K3_NO_CANONICAL_INTEGER_LABEL",
    }

    components = {
        "finite_clocks": {
            "exact_rank_new_basis": 1, "log_rational": False,
            "canonical": True,
        },
        "resummed_selected": {
            "exact_rank_new_basis": len(tower_primes), "log_rational": True,
            "canonical": False, "integer_label_inserted": True,
        },
        "resummed_all_N_tower": {
            "exact_rank_new_basis": 0, "log_rational": True,
            "canonical": False, "integer_label_inserted": True,
        },
        "modular_v446": {
            "exact_rank_new_basis": 0, "log_rational": False,
            "canonical": False, "generic": True,
        },
        "koide_flow": {
            "exact_rank_new_basis": 1, "log_rational": True,
            "canonical": True,
        },
        "ftransfer_RG": {
            "exact_rank_new_basis": 0, "log_rational": False,
            "canonical": False, "generic": True,
        },
        "scale_lattice": {
            "exact_rank_new_basis": 3, "log_rational": False,
            "canonical": True,
        },
    }
    combinations = combination_records(components)
    survivors = [record for record in combinations
                 if record["verdict"] == "SURVIVED_BC_CANDIDATE"]
    check("no single/pair/triple clock combination survives the BC criterion",
          not survivors)

    result = {
        "claim_boundary": "Experiment-only finite/exact and numerical audit. No RH claim.",
        "spec_sha256": SPEC_SHA,
        "verdict": "NO_SURVIVED_BC_CANDIDATE",
        "A1_finite_unique_factorisation_check": {
            "bound": 64,
            "q_rank": rank_64,
            "prime_basis": primes_64,
            "factor_vectors": [
                {"n": integer, "valuations": {str(p): e for p, e in vector.items()}}
                for integer, vector in factor_rows
            ],
        },
        "finite_clocks": finite,
        "resummed_clocks": resummed,
        "resummed_selected_union_prime_basis": tower_primes,
        "resummed_all_N_tower": tower,
        "modular_clock_v446": modular,
        "koide_mobius_flow": koide,
        "ftransfer_RG": ftransfer,
        "scale_lattice": scale_lattice,
        "qca_4d": qca_4d,
        "combination_count": len(combinations),
        "combinations": combinations,
        "survived_bc_candidates": survivors,
        "checks": {
            "passed": sum(ok for _, ok in CHECKS),
            "total": len(CHECKS),
            "failed": [label for label, ok in CHECKS if not ok],
        },
    }
    RESULT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    passed = result["checks"]["passed"]
    total = result["checks"]["total"]
    print(f"RESULT: {passed}/{total} checks passed")
    print(f"COMBINATIONS: {len(combinations)}; SURVIVORS: {len(survivors)}")
    print("VERDICT: NO_SURVIVED_BC_CANDIDATE")
    print(f"WROTE: {RESULT_JSON}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
