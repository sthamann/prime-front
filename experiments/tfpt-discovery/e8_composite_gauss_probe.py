#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_composite_gauss_probe -- r647  E8.GAUSS.COMPOSITE.01

Experiments-only exact reduction and cost audit.  No factoring breakthrough.

Let G be the determinant-one E8 Gram matrix used by v535 and

    Q(x) = x^T G x / 2.

For odd N and t mod N define

    S_N(t) = sum_{x in (Z/NZ)^8} exp(2 pi i t Q(x)/N).

If d=gcd(t,N), reduction to N/d and the ordinary one-dimensional quadratic
Gauss sum give

    S_N(t) = N^4 d^4.

Rank 8 removes the t/Jacobi and epsilon phases; det(G)=1 removes the
determinant phase.  Therefore

    Z_N := #{x mod N : Q(x)=0}
         = N^(-1) sum_t S_N(t)
         = N^3 sum_t gcd(t,N)^4.

For N=pq,

    Z_N/N^3 = (p^4+p-1)(q^4+q-1).

Writing S=p+q turns this into one fixed quartic, so the exact E8 zero count
plus N deterministically factors a promised semiprime in polynomial time.
The free projective isotropic-line count is likewise

    L_N=f(p)f(q),
    f(r)=(r+1)^2(r^2+1)(r^2-r+1),

matching v535's prime formula (1+r^3)(r^4-1)/(r-1).

The missing algorithm is exact evaluation of Z_N without factoring.  This
probe implements the natural discrete-to-dynamic route: contract the E8
Dynkin tree for every Fourier clock t.  A tree edge is the N x N quadratic
Fourier kernel exp(-2 pi i t ab/N), with exact rank N/gcd(t,N).  One fixed-t
contraction costs O(7N^2), all N clocks cost O(N^3), and the generic bond
dimension is N.  Symbolically replacing each contraction by its Gauss
formula leaves the gcd moment, whose exact evaluation is itself
factoring-equivalent on promised semiprimes.

Gates:

  G1  det(G)=1 and Q is integral;
  G2  brute small-vector census matches p^7+p^4-p^3;
  G3  E8 tree contraction matches N^4 gcd(t,N)^4 for every t at several
      odd prime, prime-power and composite moduli;
  G4  Fourier average matches direct gcd moment and CRT zero count;
  G5  prime projective formula matches v535;
  G6  fixed quartic recovers p+q and factors both small semiprimes and
      RSA-260 from an exact synthetic count;
  G7  bond rank and operation ledger expose O(N^3), not poly(log N);
  G8  sampling and zero-probability precision scale polynomially in N.

Verdict:
  E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT
  E8_GAUSS_FORMULA_BROKEN
  E8_FAST_READOUT_FOUND

Claim boundary: experiments only.  Not a ledger/paper/RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
import time
from dataclasses import dataclass
from math import gcd, isqrt
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROUND = 647
SEED = 647202609
CONTRACT = "E8.GAUSS.COMPOSITE.01"
FENCE = "Exploration; no factoring breakthrough claim; no RH claim"
TAG = "r647"
RESULT_JSON = HERE / "e8_composite_gauss_result.json"

TREE_MODULI = (3, 5, 7, 9, 15, 21)
BRUTE_PRIMES = (3, 5)
TREE_TOLERANCE = 5e-8
DECISIONS = (
    "E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT",
    "E8_GAUSS_FORMULA_BROKEN",
    "E8_FAST_READOUT_FOUND",
)

# Canonical v535 coefficient-basis Gram matrix.
E8_GRAM = np.array(
    [
        [2, 0, -1, 0, 0, 0, 0, 0],
        [0, 2, 0, -1, 0, 0, 0, 0],
        [-1, 0, 2, -1, 0, 0, 0, 0],
        [0, -1, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, -1],
        [0, 0, 0, 0, 0, 0, -1, 2],
    ],
    dtype=np.int64,
)

RSA260_P = int(
    "4397328654844826923795068102505872571721883526553349659561256924505973939597"
    "593482272505698004801207988043088656411102133523080581"
)
RSA260_Q = int(
    "5028695206842569864686141618253083416610081090075366674776775706538324961364"
    "412200138116378509733307971876652984898985905923678379"
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


def q_e8(vector: tuple[int, ...] | np.ndarray) -> int:
    values = np.asarray(vector, dtype=np.int64)
    doubled = int(values @ E8_GRAM @ values)
    if doubled % 2:
        raise ArithmeticError("E8 half-norm is not integral")
    return doubled // 2


def e8_edges() -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(8)
        for j in range(i + 1, 8)
        if E8_GRAM[i, j] == -1
    ]


def iso_points_prime_formula(prime: int) -> int:
    return prime**7 + prime**4 - prime**3


def iso_lines_prime_formula(prime: int) -> int:
    return (1 + prime**3) * ((prime**4 - 1) // (prime - 1))


def brute_zero_count(modulus: int) -> int:
    return sum(
        q_e8(vector) % modulus == 0
        for vector in itertools.product(range(modulus), repeat=8)
    )


@dataclass(frozen=True)
class TreeResult:
    value: complex
    edge_kernel_rank: int
    multiply_adds: int
    peak_bond: int


def tree_gauss_sum(modulus: int, clock: int) -> TreeResult:
    """Exact E8 factor graph, numerically contracted on its Dynkin tree."""
    edges = e8_edges()
    adjacency = {node: [] for node in range(8)}
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    root = 3
    omega = np.exp(2j * np.pi / modulus)
    residues = np.arange(modulus, dtype=np.int64)
    unary = omega ** ((clock * residues * residues) % modulus)
    edge_kernel = omega ** (
        (-clock * np.outer(residues, residues)) % modulus
    )
    operations = 0

    def message(node: int, parent: int | None) -> np.ndarray | complex:
        nonlocal operations
        local = unary.copy()
        for child in adjacency[node]:
            if child == parent:
                continue
            child_message = message(child, node)
            local *= np.asarray(child_message)
            operations += modulus
        if parent is None:
            operations += modulus
            return complex(np.sum(local))
        operations += modulus * modulus
        # entry [x_node, x_parent] carries exp(-t*x_node*x_parent/N)
        return local @ edge_kernel

    value = complex(message(root, None))
    divisor = gcd(clock, modulus)
    rank = modulus // divisor
    return TreeResult(value, rank, operations, modulus)


def gauss_formula(modulus: int, clock: int) -> int:
    return modulus**4 * gcd(clock, modulus) ** 4


def gcd_moment(modulus: int, power: int = 4) -> int:
    return sum(gcd(clock, modulus) ** power for clock in range(modulus))


def zero_count_formula(modulus: int) -> int:
    return modulus**3 * gcd_moment(modulus, 4)


def semiprime_zero_count(p: int, q: int) -> int:
    modulus = p * q
    return modulus**3 * (p**4 + p - 1) * (q**4 + q - 1)


def projective_semiprime_count(p: int, q: int) -> int:
    def local(prime: int) -> int:
        return (prime + 1) ** 2 * (prime**2 + 1) * (prime**2 - prime + 1)

    return local(p) * local(q)


def recover_semiprime_from_zero_count(
    modulus: int,
    zero_count: int,
) -> tuple[int, int] | None:
    """Fixed quartic inversion; does not receive or search over p/q."""
    if zero_count % modulus**3:
        return None
    moment = zero_count // modulus**3
    sum_symbol = sp.symbols("sum_pq")
    polynomial = (
        modulus**4
        - sum_symbol**4
        + modulus * sum_symbol**3
        + 4 * modulus * sum_symbol**2
        - 3 * modulus**2 * sum_symbol
        - 2 * modulus**2
        + modulus
        - sum_symbol
        + 1
        - moment
    )
    roots = sp.Poly(polynomial, sum_symbol, domain=sp.ZZ).ground_roots()
    for root, multiplicity in roots.items():
        if multiplicity < 1 or not root.is_Integer:
            continue
        total = int(root)
        discriminant = total * total - 4 * modulus
        if discriminant < 0:
            continue
        square = isqrt(discriminant)
        if square * square != discriminant or (total + square) % 2:
            continue
        p = (total - square) // 2
        q = (total + square) // 2
        if 1 < p <= q and p * q == modulus:
            return p, q
    return None


def sampling_costs(p: int, q: int) -> dict:
    modulus = p * q
    probability = (p + q - 2) / modulus
    classical_queries = 1.0 / probability
    amplitude_queries = 1.0 / math.sqrt(probability)
    mean = gcd_moment(modulus, 4) / modulus
    second = gcd_moment(modulus, 8) / modulus
    variance = second - mean * mean
    zero_probability = zero_count_formula(modulus) / modulus**8
    return {
        "nonunit_probability": probability,
        "classical_queries": classical_queries,
        "amplitude_queries": amplitude_queries,
        "mean_gcd4": mean,
        "variance_gcd4": variance,
        "zero_probability": zero_probability,
    }


def run(smoke: bool, json_path: str) -> int:
    wall_start = time.time()
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))

    section("G1 E8 convention")
    determinant = int(sp.Matrix(E8_GRAM.tolist()).det())
    even_test = all(
        int(np.asarray(vector) @ E8_GRAM @ np.asarray(vector)) % 2 == 0
        for vector in itertools.product(range(3), repeat=8)
    )
    check(
        "G1 det(E8)=1 and Q=xTGx/2 integral",
        determinant == 1 and even_test and len(e8_edges()) == 7,
        "det=%d, Dynkin edges=%d" % (determinant, len(e8_edges())),
    )

    section("G2 prime-field zero census")
    brute_rows = []
    for prime in ((3,) if smoke else BRUTE_PRIMES):
        observed = brute_zero_count(prime)
        expected = iso_points_prime_formula(prime)
        brute_rows.append({"p": prime, "observed": observed, "expected": expected})
        emit("  p=%d brute=%d formula=%d" % (prime, observed, expected))
    check(
        "G2 brute prime counts match p^7+p^4-p^3",
        all(row["observed"] == row["expected"] for row in brute_rows),
    )

    section("G3-G4 composite Gauss sums by E8 tree contraction")
    moduli = (3, 9, 15) if smoke else TREE_MODULI
    tree_rows = []
    all_tree = True
    all_zero = True
    for modulus in moduli:
        values = []
        operation_count = 0
        ranks = set()
        for clock in range(modulus):
            contracted = tree_gauss_sum(modulus, clock)
            expected = gauss_formula(modulus, clock)
            error = abs(contracted.value - expected) / max(expected, 1)
            all_tree &= error < TREE_TOLERANCE
            values.append(contracted.value.real)
            operation_count += contracted.multiply_adds
            ranks.add(contracted.edge_kernel_rank)
        zero_from_fourier = int(round(sum(values) / modulus))
        zero_from_moment = zero_count_formula(modulus)
        all_zero &= zero_from_fourier == zero_from_moment
        tree_rows.append(
            {
                "N": modulus,
                "max_relative_error": max(
                    abs(values[t] - gauss_formula(modulus, t))
                    / gauss_formula(modulus, t)
                    for t in range(modulus)
                ),
                "zero_fourier": zero_from_fourier,
                "zero_formula": zero_from_moment,
                "multiply_adds_all_clocks": operation_count,
                "kernel_ranks": sorted(ranks),
            }
        )
        emit(
            "  N=%2d maxrel=%.2e zeros=%d ops=%d bond-ranks=%s"
            % (
                modulus,
                tree_rows[-1]["max_relative_error"],
                zero_from_fourier,
                operation_count,
                sorted(ranks),
            )
        )
    check(
        "G3 tree sums equal N^4*gcd(t,N)^4",
        all_tree,
        "all t for moduli %s" % (moduli,),
    )
    check(
        "G4 Fourier zero count equals N^3*sum gcd^4",
        all_zero,
    )

    section("G5 prime/projective and CRT formulas")
    prime_formula_ok = all(
        iso_lines_prime_formula(prime)
        == (prime + 1) ** 2 * (prime**2 + 1) * (prime**2 - prime + 1)
        for prime in (3, 5, 7, 11)
    )
    p_small, q_small = 3, 5
    crt_zero = semiprime_zero_count(p_small, q_small)
    crt_lines = projective_semiprime_count(p_small, q_small)
    check(
        "G5 v535 projective formula and N=15 CRT values",
        prime_formula_ok
        and crt_zero == 176_198_625
        and crt_lines == 22_014_720,
        "Z15=%d L15=%d" % (crt_zero, crt_lines),
    )

    section("G6 exact count-to-factor inversion")
    inversion_rows = []
    for p, q, label in (
        (1009, 1013, "small"),
        (RSA260_P, RSA260_Q, "RSA-260"),
    ):
        modulus = p * q
        zero_count = semiprime_zero_count(p, q)
        started = time.perf_counter()
        recovered = recover_semiprime_from_zero_count(modulus, zero_count)
        elapsed = time.perf_counter() - started
        inversion_rows.append(
            {
                "label": label,
                "N_bits": modulus.bit_length(),
                "recovered": recovered == (min(p, q), max(p, q)),
                "quartic_seconds": elapsed,
                "zero_count_digits": len(str(zero_count)),
            }
        )
        emit(
            "  %s: N=%d bits, count=%d digits, quartic %.4fs, recovered=%s"
            % (
                label,
                modulus.bit_length(),
                len(str(zero_count)),
                elapsed,
                recovered == (min(p, q), max(p, q)),
            )
        )
    check(
        "G6 exact E8 count factors promised semiprimes",
        all(row["recovered"] for row in inversion_rows),
        "fixed quartic, including RSA-260 synthetic exact count",
    )

    section("G7-G8 cost barrier")
    cost_rows = []
    for modulus in (15, 21, 35):
        operations = sum(
            tree_gauss_sum(modulus, clock).multiply_adds
            for clock in range(modulus)
        )
        max_unit_rank = max(
            tree_gauss_sum(modulus, clock).edge_kernel_rank
            for clock in range(1, modulus)
            if gcd(clock, modulus) == 1
        )
        cost_rows.append(
            {
                "N": modulus,
                "tree_ops": operations,
                "ops_over_N3": operations / modulus**3,
                "generic_bond": max_unit_rank,
            }
        )
    check(
        "G7 tree contraction is cubic with generic bond N",
        all(row["generic_bond"] == row["N"] for row in cost_rows)
        and all(6.0 <= row["ops_over_N3"] <= 9.0 for row in cost_rows),
        str(cost_rows),
    )
    sample = sampling_costs(1009, 1013)
    balanced_scale = math.sqrt(1009 * 1013)
    check(
        "G8 rare nonunit sampling is sqrt(N), amplitude N^(1/4)",
        0.4 * balanced_scale
        < sample["classical_queries"]
        < 0.6 * balanced_scale
        and 0.6 * balanced_scale**0.5
        < sample["amplitude_queries"]
        < 0.8 * balanced_scale**0.5,
        "classical %.1f, amplitude %.1f, sqrtN %.1f"
        % (
            sample["classical_queries"],
            sample["amplitude_queries"],
            balanced_scale,
        ),
    )

    if all(ok for _name, ok in CHECKS):
        verdict = "E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT"
        why = (
            "rank-8 unimodularity makes the composite E8 Gauss sum exactly "
            "N^4*gcd(t,N)^4 and the exact zero count factors N, but the natural "
            "tree/clock readout costs O(N^3) with bond N; symbolic collapse leaves "
            "the factoring-equivalent gcd moment"
        )
    else:
        verdict = "E8_GAUSS_FORMULA_BROKEN"
        why = "%d gate(s) failed" % sum(not ok for _name, ok in CHECKS)
    check("G9 verdict enum", verdict in DECISIONS, verdict)

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "round": ROUND,
        "fence": FENCE,
        "verdict": verdict,
        "why": why,
        "gram": E8_GRAM.tolist(),
        "brute_rows": brute_rows,
        "tree_rows": tree_rows,
        "inversion_rows": inversion_rows,
        "cost_rows": cost_rows,
        "sampling": sample,
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
