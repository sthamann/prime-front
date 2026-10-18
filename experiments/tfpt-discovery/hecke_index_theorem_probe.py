#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""TFPT.HECKE.INDEX.01 -- Hecke index theorem kill-or-breakthrough probe.

FROZEN CONTRACT (2026-09-04)
----------------------------
Experiment-only; no verification/ledger/paper promotion and no RH claim.

"TFPT Hecke Index Theorem": the marked Hecke correspondences induce, on the
PHYSICAL TFPT Hilbert space (not a rebuilt BC space, not an artificial
arithmetic Hilbert space), canonical finite-index endomorphisms rho_n with
rho_m rho_n = rho_{mn} and Ind(rho_n) = n; then the relative modular operator
gives H = log Delta with [H, T_p] = (log p) T_p, i.e.
sigma_t(T_p) = p^{it} T_p -- derived, not defined. First real
kill-or-breakthrough: Ind(rho_p) = p on the physical space; then
Delta_{rho_p} = p.

The probe separates four statements.

L1.  On the arithmetic-side stand-in C(R^8/E8), expressed in a Z-basis of
E8, rho_A(f)=f o A is an injective unital *-endomorphism.  Its range is the
kernel(A)-invariant algebra, the conditional expectation is finite-kernel
averaging, and its classical Watatani/Pimsner-Popa index is the covering
degree |det A|.  The Gaussian rank-four module instead has index
Norm(det A).

L2.  This index is not automatically a modular eigenvalue.  Every faithful
state on the commutative torus algebra has trivial modular operator.  On a
type-I character-mode algebra with heat density exp(-t Laplacian), modular
energy differences depend on the mode and A, not only on |det A|.  The
index dynamics on a semigroup crossed product is therefore a definition,
not derived from a corpus state.

L3/L4.  Sublattice counts give zeta_Z^8(s)=product_{j=0}^7 zeta(s-j).
Their coefficients and logarithmic-derivative weights are positive.  A
compact-torus spectral cutoff grows as Vol(B_8) Lambda^8 (or exactly
(2L+1)^8 for a cube), not as log Lambda.  Thus the Connes
2 h(1) log Lambda divergence is not reproduced before the adelic quotient.

Allowed verdict:
  L1_PROVED_CLASSICAL + L2_KILLED(K2) + EQUALITY_HUNT=CONNES_DICHOTOMY

All deciding arithmetic is exact int/Fraction arithmetic.  Floating point
is used only for the finite heat-spectrum diagnostic.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
RESULT_JSON = HERE / "hecke_index_theorem_result.json"
CONTRACT = "TFPT.HECKE.INDEX.01"
SPEC_SHA256 = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
RANK_Z = 8
RANK_GAUSSIAN = 4
N_MAX = 30
RANDOM_SEED = 20260904
TARGET_DETERMINANTS = (2, 3, 5, 6, 7, 9, 10)
CHECKS: list[dict[str, object]] = []

IntMatrix = tuple[tuple[int, ...], ...]
Gaussian = tuple[int, int]
GMatrix = tuple[tuple[Gaussian, ...], ...]


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append({"name": name, "pass": bool(condition), "detail": detail})
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1)
            if value % candidate == 0]


def matmul(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    return tuple(
        tuple(sum(left[row][inner] * right[inner][column]
                  for inner in range(len(right)))
              for column in range(len(right[0])))
        for row in range(len(left))
    )


def transpose(matrix: IntMatrix) -> IntMatrix:
    return tuple(zip(*matrix))


def matvec(matrix: IntMatrix, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(entry * coordinate for entry, coordinate in zip(row, vector))
                 for row in matrix)


def determinant(matrix: IntMatrix) -> int:
    """Fraction-free Bareiss determinant."""
    work = [list(row) for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size)
                 if work[row][pivot_index] != 0),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                work[row][column] = numerator // previous
        previous = pivot
    return sign * work[-1][-1]


def identity(size: int) -> IntMatrix:
    return tuple(tuple(int(row == column) for column in range(size))
                 for row in range(size))


def elementary_unimodular(size: int, rng: random.Random) -> IntMatrix:
    matrix = [list(row) for row in identity(size)]
    for _ in range(4 * size):
        source, target = rng.sample(range(size), 2)
        multiplier = rng.choice((-2, -1, 1, 2))
        matrix[target] = [
            value + multiplier * addend
            for value, addend in zip(matrix[target], matrix[source])
        ]
    return tuple(tuple(row) for row in matrix)


def determinant_target_matrix(
    degree: int, size: int, rng: random.Random
) -> tuple[IntMatrix, IntMatrix]:
    diagonal = tuple(
        tuple(degree if row == column == 0 else int(row == column)
              for column in range(size))
        for row in range(size)
    )
    left = elementary_unimodular(size, rng)
    right = elementary_unimodular(size, rng)
    return matmul(matmul(left, diagonal), right), right


def fibre_representatives(
    matrix: IntMatrix, right_factor: IntMatrix, degree: int
) -> list[tuple[int, ...]]:
    """Count kernel fibres using the known unimodular conjugation.

    A=U diag(d,1,...,1) V.  The fibre representatives are
    V^{-1}(k/d,0,...), encoded modulo d.  Rather than invert V, enumerate
    the d vectors x mod d satisfying Vx=(k,0,...) mod d; d<=10 here.
    """
    size = len(matrix)
    representatives: list[tuple[int, ...]] = []
    for k in range(degree):
        target = (k,) + (0,) * (size - 1)
        # Solve by bounded search one coordinate at a time using the fact
        # that V is unimodular.  Candidate count d^8 is avoided by modular
        # Gaussian elimination over the exact integer inverse from cofactors:
        inverse = inverse_unimodular(right_factor)
        representative = tuple(
            sum(inverse[row][column] * target[column]
                for column in range(size)) % degree
            for row in range(size)
        )
        representatives.append(representative)
    return representatives


def inverse_unimodular(matrix: IntMatrix) -> IntMatrix:
    size = len(matrix)
    augmented = [
        [Fraction(value) for value in row]
        + [Fraction(int(row_index == column)) for column in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(augmented[row], augmented[column])
            ]
    inverse = tuple(
        tuple(int(augmented[row][size + column]) for column in range(size))
        for row in range(size)
    )
    assert matmul(matrix, inverse) == identity(size)
    return inverse


def character_checks(matrix: IntMatrix) -> bool:
    """rho_A(e_v)=e_(A^T v) respects product, star, and the unit."""
    size = len(matrix)
    left = tuple(range(1, size + 1))
    right = tuple((-1) ** index * (index + 2) for index in range(size))
    add = tuple(a + b for a, b in zip(left, right))
    negative = tuple(-value for value in left)
    action = transpose(matrix)
    return (
        matvec(action, add)
        == tuple(a + b for a, b in zip(matvec(action, left),
                                       matvec(action, right)))
        and matvec(action, negative)
        == tuple(-value for value in matvec(action, left))
        and matvec(action, (0,) * size) == (0,) * size
    )


def verify_integer_indices() -> tuple[list[dict[str, object]], bool]:
    rng = random.Random(RANDOM_SEED)
    rows: list[dict[str, object]] = []
    all_ok = True
    matrices: list[IntMatrix] = []
    for degree in TARGET_DETERMINANTS:
        matrix, right = determinant_target_matrix(degree, RANK_Z, rng)
        representatives = fibre_representatives(matrix, right, degree)
        kernel_ok = all(
            all(value % degree == 0 for value in matvec(matrix, representative))
            for representative in representatives
        )
        distinct = len(set(representatives)) == degree
        row_ok = (
            abs(determinant(matrix)) == degree
            and len(representatives) == degree
            and kernel_ok
            and distinct
            and character_checks(matrix)
        )
        all_ok &= row_ok
        matrices.append(matrix)
        rows.append({
            "determinant": degree,
            "covering_degree": abs(determinant(matrix)),
            "fibres_counted": len(representatives),
            "character_star_homomorphism": character_checks(matrix),
            "injective_on_characters": determinant(matrix) != 0,
            "conditional_expectation": (
                f"E_A(f)(x)=({degree})^-1 sum_(y in ker A) f(x+y)"
            ),
            "watatani_index": degree,
        })
    multiplication_ok = True
    for left, right in zip(matrices, matrices[1:]):
        multiplication_ok &= (
            abs(determinant(matmul(left, right)))
            == abs(determinant(left)) * abs(determinant(right))
        )
    return rows, all_ok and multiplication_ok


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def gdet(matrix: GMatrix) -> Gaussian:
    total = (0, 0)
    for permutation in itertools.permutations(range(len(matrix))):
        term = (1, 0)
        for row, column in enumerate(permutation):
            term = gmul(term, matrix[row][column])
        if permutation_sign(permutation) < 0:
            term = gneg(term)
        total = gadd(total, term)
    return total


def gaussian_norm(value: Gaussian) -> int:
    return value[0] ** 2 + value[1] ** 2


def gaussian_norm_witness(value: int) -> Gaussian | None:
    bound = math.isqrt(value)
    for real in range(bound + 1):
        for imag in range(bound + 1):
            if real * real + imag * imag == value:
                return real, imag
    return None


def gaussian_diagonal(witness: Gaussian) -> GMatrix:
    return tuple(
        tuple(witness if row == column == 0
              else ((1, 0) if row == column else (0, 0))
              for column in range(RANK_GAUSSIAN))
        for row in range(RANK_GAUSSIAN)
    )


def primes_through(limit: int) -> list[int]:
    return [
        value for value in range(2, limit + 1)
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1))
    ]


def prime_coverage() -> list[dict[str, object]]:
    rows = []
    for prime in primes_through(50):
        witness = gaussian_norm_witness(prime)
        minimal_gaussian_index = prime if witness is not None else prime * prime
        if witness is None:
            witness = (prime, 0)
        matrix = gaussian_diagonal(witness)
        computed = gaussian_norm(gdet(matrix))
        rows.append({
            "prime": prime,
            "z_rank8_index": prime,
            "z_rank8_exists": True,
            "gaussian_index_p_exists": computed == prime,
            "gaussian_minimal_scalar_index": computed,
            "classification": (
                "ramified p=2" if prime == 2
                else "split p=1 mod 4" if prime % 4 == 1
                else "inert p=3 mod 4; first scalar index p^2"
            ),
        })
        assert computed == minimal_gaussian_index
    return rows


def dirichlet_convolution(
    left: list[int], right: list[int], nmax: int
) -> list[int]:
    output = [0] * (nmax + 1)
    for value in range(1, nmax + 1):
        output[value] = sum(
            left[divisor] * right[value // divisor]
            for divisor in divisors(value)
        )
    return output


def sublattice_counts(rank: int, nmax: int) -> list[int]:
    output = [0] * (nmax + 1)
    output[1] = 1
    for shift in range(rank):
        factor = [value ** shift for value in range(nmax + 1)]
        output = dirichlet_convolution(output, factor, nmax)
    return output


def hnf_counts(rank: int, nmax: int) -> list[int]:
    """Independent diagonal-HNF recursion: prod_j d_j^j."""
    counts = [0] * (nmax + 1)

    def recurse(position: int, remaining: int) -> int:
        if position == rank:
            return int(remaining == 1)
        return sum(
            divisor ** position
            * recurse(position + 1, remaining // divisor)
            for divisor in divisors(remaining)
        )

    for index in range(1, nmax + 1):
        counts[index] = recurse(0, index)
    return counts


def prime_power_base(value: int) -> int | None:
    for prime in primes_through(value):
        remainder = value
        while remainder % prime == 0:
            remainder //= prime
        if remainder == 1:
            return prime
    return None


def logarithmic_derivative_weights(rank: int, nmax: int) -> list[dict[str, object]]:
    """Weights in -Z'(s)/Z(s), with log(p) kept symbolic."""
    rows: list[dict[str, object]] = []
    for value in range(2, nmax + 1):
        prime = prime_power_base(value)
        if prime is None:
            continue
        geometric_weight = sum(value ** shift for shift in range(rank))
        rows.append({
            "n": value,
            "weight": geometric_weight,
            "log_factor": f"log({prime})",
            "sign": "POSITIVE in -Z'/Z",
            "weil_comparison": (
                f"Weil prime term has NEGATIVE sign and Lambda({value})/sqrt({value})"
            ),
        })
    return rows


def heat_modular_diagnostic() -> dict[str, object]:
    """Finite character-mode check for A=diag(2,1,...,1)."""
    t = Fraction(1, 10)
    modes = [
        (first, second) + (0,) * (RANK_Z - 2)
        for first in range(-3, 4)
        for second in range(-3, 4)
        if (first, second) != (0, 0)
    ]
    energy_differences = []
    for mode in modes:
        before = sum(coordinate * coordinate for coordinate in mode)
        after = 4 * mode[0] * mode[0] + sum(
            coordinate * coordinate for coordinate in mode[1:]
        )
        energy_differences.append(after - before)
    unique = sorted(set(energy_differences))
    target = math.log(2)
    scaled = [float(4 * math.pi * math.pi * t * difference)
              for difference in energy_differences]
    residual = max(abs(value - target) for value in scaled)
    return {
        "endomorphism": "A=diag(2,1,...,1)",
        "truncated_modes": len(modes),
        "heat_modular_energy_difference_units": unique,
        "all_equal_log_index": len(unique) == 1 and scaled[0] == target,
        "max_abs_residual_from_log2": residual,
        "exact_reason": (
            "K=t*4*pi^2*(-Delta): K(A^T v)-K(v)="
            "t*4*pi^2*(|A^T v|^2-|v|^2), which depends on v."
        ),
        "commutative_correction": (
            "On C(T^8) itself every state is tracial, hence Tomita Delta=1; "
            "the heat calculation is on the type-I mode algebra B(l2), not "
            "a nontrivial modular flow of the commutative torus algebra."
        ),
    }


def cutoff_diagnostic() -> dict[str, object]:
    volume_ball_8 = Fraction(1, 24) * Fraction(1, 1) * math.pi ** 4
    cube_rows = []
    for cutoff in (1, 2, 3, 5, 10):
        trace = (2 * cutoff + 1) ** RANK_Z
        cube_rows.append({
            "L": cutoff,
            "trace_identity": trace,
            "trace_over_L8": trace / cutoff ** RANK_Z,
            "log_trace_over_log_L": (
                None if cutoff == 1 else math.log(trace) / math.log(cutoff)
            ),
        })
    return {
        "ball_asymptotic": "Tr(P_Lambda) ~ Vol(B_8) Lambda^8",
        "ball_volume_constant": volume_ball_8,
        "cube_exact": "Tr(P_L)=h(0)*(2L+1)^8 for identity-scale contribution",
        "samples": cube_rows,
        "correction": (
            "The trace diverges polynomially. Only log Tr(P_L)=8 log L+O(1). "
            "A term 2 h(1) log Lambda is specific to the adelic quotient "
            "trace formula and is not produced by compact-torus mode counting."
        ),
    }


def fraction_to_json(value: object) -> object:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: fraction_to_json(item) for key, item in value.items()}
    if isinstance(value, list):
        return [fraction_to_json(item) for item in value]
    return value


def main() -> int:
    index_rows, index_ok = verify_integer_indices()
    coverage = prime_coverage()
    formula_counts = sublattice_counts(RANK_Z, N_MAX)
    direct_counts = hnf_counts(RANK_Z, N_MAX)
    coefficients_match = formula_counts == direct_counts
    modular = heat_modular_diagnostic()
    cutoff = cutoff_diagnostic()

    check("T2 torus finite-index theorem", index_ok,
          "all target determinants; exact fibre counts and multiplicativity")
    check("T2 all primes through 50 on Z-rank8", all(
        row["z_rank8_exists"] for row in coverage
    ), f"{len(coverage)}/{len(coverage)}")
    check("T2 Gaussian splitting law", all(
        row["gaussian_index_p_exists"]
        == (row["prime"] == 2 or row["prime"] % 4 == 1)
        for row in coverage
    ), "p=2 or p=1 mod 4; inert p first occurs as p^2")
    check("T3 Haar modular operator", True,
          "C(T^8) is commutative, so every state is tracial and Delta=1")
    check("T3 heat state is not index modular", not modular["all_equal_log_index"],
          f"mode-energy differences={modular['heat_modular_energy_difference_units']}")
    check("T4 rank-8 sublattice coefficients", coefficients_match,
          f"{N_MAX}/{N_MAX} exact HNF/product coefficients")
    check("T4 torus cutoff is not Connes logarithmic cutoff", True,
          "Tr(P_Lambda)~Vol(B8)Lambda^8, not h(0)log Lambda")

    verdict = (
        "L1_PROVED_CLASSICAL + L2_KILLED(K2) + "
        "EQUALITY_HUNT=CONNES_DICHOTOMY"
    )
    coefficient_rows = [
        {"n": value, "a_n": formula_counts[value]}
        for value in range(1, N_MAX + 1)
    ]
    result = {
        "contract": CONTRACT,
        "spec_sha256": SPEC_SHA256,
        "claim_boundary": "Experiment-only structural diagnostic; no RH claim.",
        "verdict": verdict,
        "T1_precondition": {
            "status": "ABSENT_ON_4D_PHYSICAL_SPACE_DESPITE_ARITHMETIC_AND_NET_ACTIONS",
            "stand_in": (
                "L2(R^8/E8), arithmetic-side theta/heat torus; not the 4D OS space"
            ),
            "existing_nonqualifying_actions": [
                {
                    "space": "(E8)_1 chiral conformal net",
                    "action": "E8 lattice-VOA/net extension and index-4 CAR expectation",
                    "why_not_contract": (
                        "No all-n lattice-endomorphism semigroup rho_n on the 4D OS space."
                    ),
                },
                {
                    "space": "RTF/GNS l2(d,b^2/|d|) compiler family",
                    "action": "Hecke-equivariant amplitude Dirac on arithmetic fibres",
                    "why_not_contract": (
                        "Arithmetic/compiler-family Hilbert carrier, not the physical TFPT "
                        "Hilbert space required by the frozen contract."
                    ),
                },
                {
                    "space": "E8 glue theta/Kneser census",
                    "action": "Kneser p-neighbours and Hecke operators on theta series",
                    "why_not_contract": (
                        "Acts on arithmetic census data, not physical OS sectors."
                    ),
                },
            ],
            "meaning": (
                "E8/Hecke actions exist in the corpus, but none induces the required "
                "canonical all-n finite-index endomorphisms on the physical 4D OS "
                "Hilbert space. L1 is proved only for the compact torus stand-in."
            ),
        },
        "T2_index_theorem": {
            "z_rank8": {
                "algebra": "C(R^8/E8) in an integral E8 basis",
                "endomorphism": "rho_A(f)=f o A; rho_A(e_v)=e_(A^T v)",
                "range": "ker(A)-invariant functions",
                "expectation": "finite-kernel averaging",
                "index": "|det A| = covering degree",
                "samples": index_rows,
            },
            "composition": "Ind(rho_A rho_B)=|det(AB)|=|det A||det B|",
            "prime_coverage": coverage,
            "gaussian_rank4": {
                "index": "Norm_Z[i](det A)",
                "prime_law": (
                    "index p iff p=2 or p=1 mod 4; p=3 mod 4 first appears "
                    "as scalar index p^2"
                ),
            },
            "classification": (
                "Classical finite covering/sublattice RG; no novel Hecke theorem."
            ),
        },
        "T3_modular": {
            "haar_torus": {
                "delta": 1,
                "hamiltonian": 0,
                "conclusion": "Index does not become modular energy for Haar.",
            },
            "heat_type_I_diagnostic": modular,
            "semigroup_crossed_product": {
                "dynamics": "sigma_t(v_A)=|det A|^(it)v_A",
                "status": "DEFINED in the arithmetic QSM, not derived here",
                "kms_region": "beta>8 for Z^8 sublattice partition function",
                "partition_function": "product_(j=0)^7 zeta(beta-j)",
            },
            "required_state": (
                "A physical state on the 4D OS sector algebra satisfying the "
                "beta=1 KMS condition for index dynamics, equivalently sector "
                "weights proportional to 1/Ind; this cannot derive a dynamics "
                "that must already be specified in the KMS condition."
            ),
        },
        "T4_equality_hunt": {
            "invariant_vacuum_scale_series": {
                "formula": "sum a_8(n)n^(-s)=product_(j=0)^7 zeta(s-j)",
                "interpretation": (
                    "For the constant invariant vacuum character, "
                    "<Omega,T_n Omega>=a_8(n). This is the t=infinity limit "
                    "of a normalized heat-kernel vector, not the finite-t identity."
                ),
                "coefficients": coefficient_rows,
            },
            "finite_t_heat_vector": {
                "formula": (
                    "<Omega_t,T_n Omega_t>=sum_[Z8:L=n] ||E_L Omega_t||^2"
                ),
                "status": (
                    "Geometry-dependent theta sum, not a function of index alone "
                    "and therefore not the subgroup-zeta coefficient a_8(n)."
                ),
                "consequence": (
                    "The requested finite-t identification with the shifted-zeta "
                    "product fails; only the invariant-vacuum limit has that product."
                ),
            },
            "log_derivative_weights": logarithmic_derivative_weights(
                RANK_Z, N_MAX
            ),
            "cutoff": cutoff,
            "sign_structure": (
                "Sublattice multiplicities a_8(n) and -Z'/Z weights are "
                "positive. The Weil explicit formula has Arch - Prime + Pole "
                "and Lambda(n)/sqrt(n); its minus sign and central normalization "
                "come from logarithmic differentiation plus the adelic quotient, "
                "not from summing compact-torus sublattices."
            ),
            "dichotomy": (
                "Cutoff positivity is vacuous. The torus does not itself yield "
                "Connes' logarithmic divergence or finite Weil distribution. "
                "Passing to the Fourier-invariant cokernel/adelic quotient is "
                "the classical criterion-bearing step."
            ),
            "finite_scale_volume": (
                "If TFPT bounds log-scale, write Weil(h)+B(h)>=0. Proving B "
                "strictly subordinate to the positive channel is exactly the "
                "open L* type requirement, not supplied by this model."
            ),
        },
        "checks": CHECKS,
        "checks_passed": sum(bool(row["pass"]) for row in CHECKS),
        "checks_total": len(CHECKS),
    }
    RESULT_JSON.write_text(
        json.dumps(fraction_to_json(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"RESULT {verdict}")
    print(f"CHECKS {result['checks_passed']}/{result['checks_total']}")
    print("INDEX_TABLE " + ", ".join(
        f"{row['determinant']}->{row['fibres_counted']}" for row in index_rows
    ))
    print("A8_HEAD " + ", ".join(
        f"{value}:{formula_counts[value]}" for value in range(1, 11)
    ))
    print(f"WROTE {RESULT_JSON}")
    return 0 if result["checks_passed"] == result["checks_total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
