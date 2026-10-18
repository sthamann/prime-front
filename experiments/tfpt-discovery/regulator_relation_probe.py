#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""regulator_relation_probe -- r644  GEOM.REGULATOR.RELATION.01

Replace r643's deliberately slow scalar-regulator oracle by many cheap,
individually weak relations.

This is a transparent single-polynomial index-calculus baseline, not a new
factoring method.  For

    A_x = floor(sqrt(N)) + x,
    Q(x) = A_x^2 - N = Norm(A_x + sqrt(N)),

the split primes p <= B form a factor base.  A logarithmic prime-power sieve
finds x for which Q(x) is factor-base smooth.  Every exact smooth value yields

    (alpha_x) = product P_p^(e_p),              alpha_x=A_x+sqrt(N),
    lambda_x = log(alpha_x) - 1/2 log(Q(x)).

The signed e_p records which of the two primes above p divides alpha_x.  An
integer dependency k among relation rows cancels the prime ideals, hence

    sum_x k_x lambda_x = m R

for an integer m and the regulator R of Z[sqrt(N)].  An approximate real gcd
of several nonzero dependency values produces kR.  The value 2kR is always an
integer multiple of Murru--Salvatori's R_plus: R_plus=R for a norm +1
fundamental unit and R_plus=2R for a norm -1 fundamental unit.  It is fed to
r643, which accepts a polynomially bounded multiple of R_plus.

Runtime inputs are N and public search parameters (B, X).  p, q and the slow
continued-fraction oracle are used only after the run for exact validation.

This relation construction is the classical "third kind" missed by the first
blindness taxonomy: no row contains a factor, but enough rows plus linear
algebra expose a period.  It is also the honest finite Hylæan fibre picture:
each prime power creates two local residue wells in x, their additive
outbalancing energy is the logarithmic sieve score, and exact relations are
the simultaneous intersections.  A field implementation may parallelise
this sieve; it does not gain information beyond it unless it creates more
independent smooth rows for the same fully counted work.

Measured on blind balanced Blum semiprimes (24..56 bit):

  G1  every accepted Q(x) is exactly factor-base smooth and its signed ideal
      row is valid;
  G2  every emitted dependency cancels the integer relation vector exactly;
  G3  for audit sizes <=40 bit, dependency logs are integer multiples of R
      (checked only after collection against the slow scalar oracle);
  G4  the relation-derived 2kR, without the oracle, makes r643 return a factor;
  G5  relation rank, dependency count, sieve updates, exact divisions,
      precision and full cost ledger are reported;
  G6  no hidden p/q, full cycle or factor table occurs in the runtime call
      graph.

Decision:
  RELATIONS_RECOVER_REGULATOR_BASELINE
  RELATION_SEARCH_INCOMPLETE
  RUNTIME_ORACLE_LEAK

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: no factoring breakthrough claim; no RH claim.  The algorithmic class
is the known Buchmann/SIQS/CFRAC L[1/2] family; GNFS remains asymptotically
faster for general large N.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import math
import sys
import time
from dataclasses import asdict, dataclass
from fractions import Fraction
from math import gcd, isqrt, lcm
from pathlib import Path

import mpmath
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import regulator_jump_probe as R643  # noqa: E402

SQUFOF_BASELINE_BUDGET = 3_000_000
POLLARD_BASELINE_BUDGET = 12_000_000

ROUND = 644
SEED = 644202609
CONTRACT = "GEOM.REGULATOR.RELATION.01"
FENCE = "Exploration; no factoring breakthrough claim; no RH claim"
TAG = "r644"
RESULT_JSON = HERE / "regulator_relation_result.json"

BIT_SIZES = (24, 32, 40, 48, 56)
N_PER_SIZE = 3
PARAMETERS = {
    24: (100, 250_000),
    32: (180, 600_000),
    40: (300, 1_500_000),
    48: (500, 4_000_000),
    56: (800, 8_000_000),
}
SCALE_PARAMETERS = {
    64: (1_200, 16_000_000),
    72: (1_800, 32_000_000),
    80: (2_600, 64_000_000),
}
BLOCK_SIZE = 25_000
DEPENDENCY_TARGET = 3
MAX_PARAMETER_ATTEMPTS = 3
SCORE_TOLERANCE = 1e-6
RELATION_DPS = 120
ORACLE_AUDIT_MAX_BITS = 40
REAL_GCD_RELATIVE_TOLERANCE = mpmath.mpf("1e-60")
DECISIONS = (
    "RELATIONS_RECOVER_REGULATOR_BASELINE",
    "RELATION_SEARCH_INCOMPLETE",
    "RUNTIME_ORACLE_LEAK",
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


def prime_sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for prime in range(2, isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start : limit + 1 : prime] = b"\x00" * (((limit - start) // prime) + 1)
    return [prime for prime in range(3, limit + 1, 2) if flags[prime]]


def sqrt_mod_prime(value: int, prime: int) -> int | None:
    """Tonelli--Shanks; return the smaller root or None."""
    value %= prime
    if value == 0:
        return 0
    if pow(value, (prime - 1) // 2, prime) != 1:
        return None
    if prime % 4 == 3:
        root = pow(value, (prime + 1) // 4, prime)
        return min(root, prime - root)
    odd = prime - 1
    exponent = 0
    while odd % 2 == 0:
        odd //= 2
        exponent += 1
    nonresidue = 2
    while pow(nonresidue, (prime - 1) // 2, prime) != prime - 1:
        nonresidue += 1
    c = pow(nonresidue, odd, prime)
    root = pow(value, (odd + 1) // 2, prime)
    residue = pow(value, odd, prime)
    current_exponent = exponent
    while residue != 1:
        index = 1
        square = residue * residue % prime
        while square != 1:
            square = square * square % prime
            index += 1
        correction = pow(c, 1 << (current_exponent - index - 1), prime)
        root = root * correction % prime
        residue = residue * correction * correction % prime
        c = correction * correction % prime
        current_exponent = index
    return min(root, prime - root)


def build_factor_base(n: int, bound: int) -> tuple[list[tuple[int, int]], int | None]:
    base = []
    for prime in prime_sieve(bound):
        common = gcd(n, prime)
        if 1 < common < n:
            return base, common
        root = sqrt_mod_prime(n, prime)
        if root is not None:
            base.append((prime, root))
    return base, None


def hensel_roots(n: int, prime: int, root: int, maximum: int) -> list[tuple[int, int]]:
    """Root of z^2=N modulo p^k for all p^k <= maximum."""
    lifted = []
    modulus = prime
    while modulus <= maximum:
        lifted.append((modulus, root))
        quotient = (root * root - n) // modulus
        correction = (-quotient * pow(2 * root, -1, prime)) % prime
        root += correction * modulus
        modulus *= prime
    return lifted


@dataclass(frozen=True)
class Relation:
    x: int
    q_value: int
    row: tuple[int, ...]
    log_generator: str


@dataclass
class RelationCost:
    x_scanned: int = 0
    sieve_updates: int = 0
    score_candidates: int = 0
    exact_trial_divisions: int = 0
    smooth_relations: int = 0
    elimination_pivots: int = 0
    dependencies: int = 0
    real_gcd_iterations: int = 0
    relation_seconds: float = 0.0
    linear_seconds: float = 0.0
    jump_seconds: float = 0.0

    def add(self, other: "RelationCost") -> None:
        for field_name in (
            "x_scanned",
            "sieve_updates",
            "score_candidates",
            "exact_trial_divisions",
            "smooth_relations",
            "elimination_pivots",
            "dependencies",
            "real_gcd_iterations",
            "relation_seconds",
            "linear_seconds",
            "jump_seconds",
        ):
            setattr(self, field_name, getattr(self, field_name) + getattr(other, field_name))


class IncrementalKernel:
    """Exact left-kernel dependencies by incremental rational elimination."""

    def __init__(self, columns: int):
        self.columns = columns
        self.rows = 0
        self.pivots: dict[int, tuple[dict[int, Fraction], dict[int, Fraction]]] = {}

    def add(self, row: tuple[int, ...]) -> dict[int, int] | None:
        row_index = self.rows
        self.rows += 1
        vector = {index: Fraction(value) for index, value in enumerate(row) if value}
        combination = {row_index: Fraction(1)}
        for pivot in sorted(self.pivots):
            if pivot not in vector:
                continue
            multiplier = vector[pivot]
            pivot_row, pivot_combination = self.pivots[pivot]
            for index, value in pivot_row.items():
                updated = vector.get(index, Fraction(0)) - multiplier * value
                if updated:
                    vector[index] = updated
                else:
                    vector.pop(index, None)
            for index, value in pivot_combination.items():
                updated = combination.get(index, Fraction(0)) - multiplier * value
                if updated:
                    combination[index] = updated
                else:
                    combination.pop(index, None)
        if vector:
            pivot = min(vector)
            divisor = vector[pivot]
            normalized_row = {index: value / divisor for index, value in vector.items()}
            normalized_combination = {
                index: value / divisor for index, value in combination.items()
            }
            self.pivots[pivot] = (normalized_row, normalized_combination)
            return None
        denominator = 1
        for value in combination.values():
            denominator = lcm(denominator, value.denominator)
        dependency = {index: int(value * denominator) for index, value in combination.items()}
        content = 0
        for value in dependency.values():
            content = gcd(content, abs(value))
        return {index: value // content for index, value in dependency.items()}

    @property
    def rank(self) -> int:
        return len(self.pivots)


def exact_relation(
    n: int,
    x: int,
    factor_base: list[tuple[int, int]],
) -> Relation | None:
    root_floor = isqrt(n)
    a_value = root_floor + x
    q_value = a_value * a_value - n
    if q_value <= 0 or q_value % 2 == 0:
        return None
    remainder = q_value
    row = []
    for prime, root in factor_base:
        exponent = 0
        while remainder % prime == 0:
            remainder //= prime
            exponent += 1
        if not exponent:
            row.append(0)
            continue
        positive_orientation = (a_value + root) % prime == 0
        negative_orientation = (a_value - root) % prime == 0
        if positive_orientation == negative_orientation:
            return None
        row.append(exponent if positive_orientation else -exponent)
    if remainder != 1 or not any(row):
        return None
    log_generator = (
        mpmath.log(a_value + mpmath.sqrt(n))
        - mpmath.log(q_value) / 2
    )
    return Relation(
        x=x,
        q_value=q_value,
        row=tuple(row),
        log_generator=mpmath.nstr(log_generator, n=RELATION_DPS),
    )


def relation_is_exact(
    relation: Relation,
    factor_base: list[tuple[int, int]],
) -> bool:
    reconstructed = 1
    for exponent, (prime, _root) in zip(relation.row, factor_base):
        reconstructed *= prime ** abs(exponent)
    return reconstructed == relation.q_value


@dataclass
class CollectionResult:
    direct_factor: int | None
    factor_base: list[tuple[int, int]]
    relations: list[Relation]
    dependencies: list[dict[int, int]]
    dependency_values: list[str]
    regulator_candidate: str | None
    rank: int
    cost: RelationCost


def approximate_real_gcd(
    values: list[mpmath.mpf],
    cost: RelationCost,
) -> mpmath.mpf | None:
    positive = sorted(abs(value) for value in values if abs(value) > mpmath.mpf("1e-80"))
    if not positive:
        return None
    tolerance = max(positive) * REAL_GCD_RELATIVE_TOLERANCE
    current = positive[0]
    for value in positive[1:]:
        larger, smaller = max(current, value), min(current, value)
        for _ in range(2_000):
            remainder = abs(larger - mpmath.nint(larger / smaller) * smaller)
            cost.real_gcd_iterations += 1
            if remainder <= tolerance:
                current = smaller
                break
            larger, smaller = smaller, remainder
        else:
            raise RuntimeError("approximate real gcd did not converge")
    return current


def collect_regulator_relations(
    n: int,
    factor_base_bound: int,
    x_limit: int,
    *,
    dependency_target: int = DEPENDENCY_TARGET,
) -> CollectionResult:
    """Runtime relation collector: no factors, cycle or regulator oracle."""
    if n <= 1 or n % 2 == 0 or isqrt(n) ** 2 == n:
        raise ValueError("n must be an odd positive nonsquare")
    mpmath.mp.dps = RELATION_DPS
    wall_start = time.perf_counter()
    cost = RelationCost()
    factor_base, direct_factor = build_factor_base(n, factor_base_bound)
    if direct_factor is not None:
        return CollectionResult(
            direct_factor,
            factor_base,
            [],
            [],
            [],
            None,
            0,
            cost,
        )
    if not factor_base:
        raise RuntimeError("empty factor base")

    root_floor = isqrt(n)
    maximum_q = (root_floor + x_limit) ** 2 - n
    lifted_roots = {
        prime: hensel_roots(n, prime, root, maximum_q)
        for prime, root in factor_base
    }
    kernel = IncrementalKernel(len(factor_base))
    relations: list[Relation] = []
    dependencies: list[dict[int, int]] = []
    dependency_values: list[mpmath.mpf] = []

    for start in range(1, x_limit + 1, BLOCK_SIZE):
        stop = min(x_limit + 1, start + BLOCK_SIZE)
        x_values = np.arange(start, stop, dtype=np.int64)
        x_float = x_values.astype(float)
        # Avoid int64 overflow above 62 bits.  This float is only the
        # logarithmic sieve accumulator; every shortlisted Q(x) is rebuilt
        # as an exact Python integer by exact_relation().
        q_values_float = (
            x_float * x_float
            + 2.0 * float(root_floor) * x_float
            + float(root_floor * root_floor - n)
        )
        if np.any(q_values_float <= 0):
            raise ArithmeticError("sieve polynomial must be positive on the scan")
        score = np.log(q_values_float)
        valid = (x_values + (root_floor & 1)) % 2 == 0
        for prime, root in factor_base:
            logarithm = math.log(prime)
            for modulus, lifted_root in lifted_roots[prime]:
                roots_x = {
                    (-root_floor - lifted_root) % modulus,
                    (-root_floor + lifted_root) % modulus,
                }
                for root_x in roots_x:
                    first = root_x
                    if first < start:
                        first += ((start - first + modulus - 1) // modulus) * modulus
                    if first >= stop:
                        continue
                    score[first - start :: modulus] -= logarithm
                    cost.sieve_updates += (stop - 1 - first) // modulus + 1
        candidate_offsets = np.flatnonzero(valid & (np.abs(score) < SCORE_TOLERANCE))
        cost.x_scanned += len(x_values)
        cost.score_candidates += len(candidate_offsets)
        for offset in candidate_offsets:
            cost.exact_trial_divisions += 1
            relation = exact_relation(n, int(x_values[offset]), factor_base)
            if relation is None:
                continue
            relation_index = len(relations)
            relations.append(relation)
            cost.smooth_relations += 1
            rank_before = kernel.rank
            dependency = kernel.add(relation.row)
            if kernel.rank > rank_before:
                cost.elimination_pivots += 1
            if dependency is None:
                continue
            if max(dependency) != relation_index:
                raise ArithmeticError("dependency indices do not match relation order")
            dependencies.append(dependency)
            value = abs(
                sum(
                    mpmath.mpf(coefficient)
                    * mpmath.mpf(relations[index].log_generator)
                    for index, coefficient in dependency.items()
                )
            )
            if value > mpmath.mpf("1e-80"):
                dependency_values.append(value)
                cost.dependencies += 1
            if len(dependency_values) >= dependency_target:
                break
        if len(dependency_values) >= dependency_target:
            break

    relation_end = time.perf_counter()
    regulator_candidate = approximate_real_gcd(dependency_values, cost)
    cost.relation_seconds = relation_end - wall_start
    cost.linear_seconds = time.perf_counter() - relation_end
    return CollectionResult(
        direct_factor,
        factor_base,
        relations,
        dependencies,
        [mpmath.nstr(value, n=RELATION_DPS) for value in dependency_values],
        None
        if regulator_candidate is None
        else mpmath.nstr(regulator_candidate, n=RELATION_DPS),
        kernel.rank,
        cost,
    )


def dependency_cancels(
    relations: list[Relation],
    dependency: dict[int, int],
) -> bool:
    if not relations:
        return False
    total = [0] * len(relations[0].row)
    for relation_index, coefficient in dependency.items():
        for column, value in enumerate(relations[relation_index].row):
            total[column] += coefficient * value
    return not any(total)


def runtime_oracle_firewall() -> tuple[bool, list[str]]:
    runtime_functions = (
        collect_regulator_relations,
        exact_relation,
        approximate_real_gcd,
        build_factor_base,
        hensel_roots,
        IncrementalKernel.add,
    )
    source = "\n".join(inspect.getsource(function) for function in runtime_functions)
    forbidden = (
        "slow_regulator_oracle(",
        "build_small_audit_cycle(",
        "known_factor",
        "factor_p",
        "factor_q",
        "sympy.factorint",
    )
    hits = [token for token in forbidden if token in source]
    return not hits, hits


def run_instance(
    n: int,
    p: int,
    q: int,
    bits_requested: int,
    factor_base_bound: int,
    x_limit: int,
) -> dict:
    attempts = []
    aggregate_cost = RelationCost()
    collection = None
    used_bound = factor_base_bound
    used_limit = x_limit
    for attempt in range(MAX_PARAMETER_ATTEMPTS):
        used_bound = factor_base_bound * (2**attempt)
        used_limit = x_limit * (2**attempt)
        collection = collect_regulator_relations(n, used_bound, used_limit)
        aggregate_cost.add(collection.cost)
        attempts.append(
            {
                "factor_base_bound": used_bound,
                "x_limit": used_limit,
                "factor_base_size": len(collection.factor_base),
                "relations": len(collection.relations),
                "rank": collection.rank,
                "dependency_values": len(collection.dependency_values),
                "x_scanned": collection.cost.x_scanned,
            }
        )
        if collection.direct_factor is not None or collection.regulator_candidate is not None:
            break
    assert collection is not None
    collection.cost = aggregate_cost
    if collection.direct_factor is not None:
        factor = collection.direct_factor
        jump = None
    elif collection.regulator_candidate is None:
        factor = None
        jump = None
    else:
        jump_start = time.perf_counter()
        # 2*kR is always an integer multiple of R_plus, regardless of the
        # fundamental unit's norm.
        r_multiple = 2 * mpmath.mpf(collection.regulator_candidate)
        jump = R643.regulator_assisted_split(
            n,
            mpmath.nstr(r_multiple, n=RELATION_DPS),
        )
        collection.cost.jump_seconds = time.perf_counter() - jump_start
        factor = jump.factor

    exact_relations = all(
        relation_is_exact(relation, collection.factor_base)
        for relation in collection.relations
    )
    exact_dependencies = all(
        dependency_cancels(collection.relations, dependency)
        for dependency in collection.dependencies
    )
    oracle_ratio = None
    oracle_integer_error = None
    oracle_steps = None
    if bits_requested <= ORACLE_AUDIT_MAX_BITS and collection.regulator_candidate is not None:
        try:
            oracle = R643.slow_regulator_oracle(n)
        except RuntimeError:
            oracle = None
        if oracle is not None:
            oracle_steps = oracle.oracle_steps
            ratio = 2 * mpmath.mpf(collection.regulator_candidate) / mpmath.mpf(oracle.r_plus)
            oracle_ratio = float(ratio)
            oracle_integer_error = float(abs(ratio - mpmath.nint(ratio)))

    return {
        "bits_requested": bits_requested,
        "n": n,
        "factor_base_bound": used_bound,
        "x_limit": used_limit,
        "parameter_attempts": attempts,
        "factor_base_size": len(collection.factor_base),
        "relation_count": len(collection.relations),
        "relation_rank": collection.rank,
        "dependency_count": len(collection.dependency_values),
        "regulator_candidate": collection.regulator_candidate,
        "exact_relations": exact_relations,
        "exact_dependencies": exact_dependencies,
        "oracle_ratio_2R_to_Rplus": oracle_ratio,
        "oracle_integer_error": oracle_integer_error,
        "oracle_steps": oracle_steps,
        "factor_found": factor in (p, q),
        "exact_factor": factor is not None and n % factor == 0,
        "jump_halving": None if jump is None else jump.target_halving,
        "jump_steps": None if jump is None else jump.cost.elementary_steps(),
        "cost": asdict(collection.cost),
    }


def size_summary(rows: list[dict], bits: int) -> dict:
    subset = [row for row in rows if row["bits_requested"] == bits]
    return {
        "n": len(subset),
        "successes": sum(row["factor_found"] for row in subset),
        "median_x_scanned": float(np.median([row["cost"]["x_scanned"] for row in subset])),
        "median_relations": float(np.median([row["relation_count"] for row in subset])),
        "median_rank": float(np.median([row["relation_rank"] for row in subset])),
        "median_sieve_updates": float(np.median([row["cost"]["sieve_updates"] for row in subset])),
        "median_exact_divisions": float(
            np.median([row["cost"]["exact_trial_divisions"] for row in subset])
        ),
        "median_seconds": float(
            np.median(
                [
                    row["cost"]["relation_seconds"]
                    + row["cost"]["linear_seconds"]
                    + row["cost"]["jump_seconds"]
                    for row in subset
                ]
            )
        ),
    }


def benchmark_classical_routes(row: dict) -> dict:
    """Same-Python controls for the --scale lane; excluded from relation cost."""
    import seam_geodesic_factor as baseline

    out = {}
    for method, budget in (
        ("squfof", SQUFOF_BASELINE_BUDGET),
        ("rho", POLLARD_BASELINE_BUDGET),
    ):
        started = time.perf_counter()
        result = baseline.factor_integer(
            row["n"],
            method=method,
            seed=SEED + row["bits_requested"],
            max_iterations=budget,
            squfof_bit_limit=100,
        )
        elapsed = time.perf_counter() - started
        out[method] = {
            "verified": result.verified,
            "seconds": elapsed,
            "iterations": sum(event.iterations for event in result.events),
            "events": len(result.events),
            "first_method": result.events[0].method if result.events else "prime",
        }
    relation_seconds = (
        row["cost"]["relation_seconds"]
        + row["cost"]["linear_seconds"]
        + row["cost"]["jump_seconds"]
    )
    out["relation_seconds"] = relation_seconds
    out["relation_over_squfof"] = relation_seconds / out["squfof"]["seconds"]
    out["relation_over_rho"] = relation_seconds / out["rho"]["seconds"]
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument(
        "--scale",
        action="store_true",
        help="run one blind input at 64/72/80 bits with overflow-safe sieve scores",
    )
    args = parser.parse_args()
    if args.scale:
        sizes = tuple(SCALE_PARAMETERS)
        per_size = 1
    else:
        sizes = (24, 32) if args.smoke else BIT_SIZES
        per_size = 1 if args.smoke else N_PER_SIZE
    rng = np.random.default_rng(SEED)
    wall_start = time.time()
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))

    section("G1-G4  weak relations -> real kernel -> regulator multiple -> r643 jump")
    rows = []
    for bits in sizes:
        bound, x_limit = (
            SCALE_PARAMETERS[bits] if bits in SCALE_PARAMETERS else PARAMETERS[bits]
        )
        for _ in range(per_size):
            n, p, q = R643.random_semiprime(rng, bits, blum=True)
            row = run_instance(n, p, q, bits, bound, x_limit)
            rows.append(row)
            emit(
                "  %2d bit: B=%3d FB=%2d scan=%7d rel/rank/dep=%d/%d/%d "
                "exact-div=%d jump=%s factor=%s sec=%.3f"
                % (
                    bits,
                    bound,
                    row["factor_base_size"],
                    row["cost"]["x_scanned"],
                    row["relation_count"],
                    row["relation_rank"],
                    row["dependency_count"],
                    row["cost"]["exact_trial_divisions"],
                    row["jump_steps"],
                    row["factor_found"],
                    row["cost"]["relation_seconds"]
                    + row["cost"]["linear_seconds"]
                    + row["cost"]["jump_seconds"],
                )
            )

    if args.scale:
        section("G4b  same-input classical route controls")
        for row in rows:
            controls = benchmark_classical_routes(row)
            row["classical_baselines"] = controls
            emit(
                "  %2d bit: relation %.4fs, SQUFOF %.4fs (%d iter), "
                "Pollard-Brent %.4fs (%d iter); ratios %.2fx / %.2fx"
                % (
                    row["bits_requested"],
                    controls["relation_seconds"],
                    controls["squfof"]["seconds"],
                    controls["squfof"]["iterations"],
                    controls["rho"]["seconds"],
                    controls["rho"]["iterations"],
                    controls["relation_over_squfof"],
                    controls["relation_over_rho"],
                )
            )
        check(
            "G4b-classical-controls-exact",
            all(
                row["classical_baselines"][method]["verified"]
                for row in rows
                for method in ("squfof", "rho")
            ),
            "SQUFOF and Pollard-Brent multiply back exactly on every scale input",
        )

    check(
        "G1-all-accepted-relations-exactly-smooth",
        all(row["exact_relations"] for row in rows),
        "product p^|e_p| equals Q(x) for every accepted relation",
    )
    check(
        "G2-all-kernel-dependencies-cancel-exactly",
        all(row["exact_dependencies"] for row in rows),
        "sum k_i e_i = 0 over Z, not merely mod 2",
    )
    audited = [row for row in rows if row["oracle_integer_error"] is not None]
    if audited:
        check(
            "G3-relation-real-gcd-is-a-regulator-multiple-on-audit-sizes",
            all(row["oracle_integer_error"] < 1e-12 for row in audited),
            "%d audited rows; max distance to integer of 2*kR/R_plus = %.1e; "
            "slow oracle queried only after collection"
            % (
                len(audited),
                max(row["oracle_integer_error"] for row in audited),
            ),
        )
    else:
        check(
            "G3-regulator-oracle-audit-not-applicable-above-40-bit",
            args.scale,
            "no slow cycle oracle is called on the 64/72/80-bit scale lane; "
            "the exact factor output is the independent certificate",
        )
    check(
        "G4-relation-derived-regulator-factors-all-blind-inputs",
        all(row["factor_found"] and row["exact_factor"] for row in rows),
        "%d/%d, no scalar-regulator oracle supplied to runtime"
        % (sum(row["factor_found"] for row in rows), len(rows)),
    )

    section("G5-G6  cost ledger and oracle firewall")
    summaries = {str(bits): size_summary(rows, bits) for bits in sizes}
    for bits in sizes:
        summary = summaries[str(bits)]
        emit(
            "  %2d bit median: scan %.0f, smooth relations/rank %.0f/%.0f, "
            "sieve updates %.0f, exact divisions %.0f, end-to-end %.3f s"
            % (
                bits,
                summary["median_x_scanned"],
                summary["median_relations"],
                summary["median_rank"],
                summary["median_sieve_updates"],
                summary["median_exact_divisions"],
                summary["median_seconds"],
            )
        )
    check(
        "G5-at-least-one-nonzero-regulator-relation-reached",
        all(row["dependency_count"] >= 1 for row in rows),
        "one integer-kernel value already equals an unknown integer multiple of R; "
        "up to %d are collected for a stable real gcd" % DEPENDENCY_TARGET,
    )
    firewall_ok, firewall_hits = runtime_oracle_firewall()
    check(
        "G6-runtime-has-no-cycle-regulator-or-factor-oracle",
        firewall_ok,
        "forbidden source hits: %s" % firewall_hits,
    )

    if not firewall_ok:
        verdict = "RUNTIME_ORACLE_LEAK"
        why = "relation runtime references a forbidden cycle/regulator/factor oracle"
    elif all(condition for _name, condition in CHECKS):
        verdict = "RELATIONS_RECOVER_REGULATOR_BASELINE"
        why = (
            "many factor-base-smooth principal-ideal relations plus exact integer-kernel "
            "dependencies recover a multiple of the real-quadratic regulator and make the "
            "oracle-free r643 jump factor every tested input; this is the known SIQS/Buchmann "
            "L[1/2] mechanism, not a new complexity class"
        )
    else:
        verdict = "RELATION_SEARCH_INCOMPLETE"
        why = "%d gate(s) failed" % sum(1 for _name, condition in CHECKS if not condition)
    check("G-verdict-enum", verdict in DECISIONS, verdict)

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "round": ROUND,
        "fence": FENCE,
        "verdict": verdict,
        "why": why,
        "parameters": {
            "sizes": sizes,
            "per_size": per_size,
            "table": {
                str(bits): (
                    SCALE_PARAMETERS[bits]
                    if bits in SCALE_PARAMETERS
                    else PARAMETERS[bits]
                )
                for bits in sizes
            },
            "block_size": BLOCK_SIZE,
            "dependency_target": DEPENDENCY_TARGET,
            "precision_digits": RELATION_DPS,
        },
        "rows": rows,
        "summaries": summaries,
        "gates": {name: condition for name, condition in CHECKS},
    }
    payload["result_sha"] = payload_sha(payload)
    payload["file_sha256"] = file_sha256()
    if not args.smoke:
        RESULT_JSON.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n")
    passed = sum(condition for _name, condition in CHECKS)
    emit("")
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (passed, len(CHECKS)))
    emit("FILE_SHA256 %s" % payload["file_sha256"])
    emit("RESULT_SHA %s" % payload["result_sha"])
    emit("WALL_S %.3f" % (time.time() - wall_start))
    emit(
        "ALL CHECKS PASSED"
        if passed == len(CHECKS)
        else "GATE_FAILURES " + ",".join(name for name, condition in CHECKS if not condition)
    )
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
