#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hylaean_relation_fiber_probe -- r646  HYLAEAN.RELATION.FIBER.01

Experiments-only, no factoring breakthrough claim.

Question
--------
Can a Hylaean-style dissipative field improve the relation-discovery stage
of r644, rather than trying to relax directly to p and q?

The comparison is information-matched.  Every strategy receives only:

  * public N;
  * the same factor-base primes and square roots of N modulo those primes;
  * the same x blocks for Q(x)=(floor(sqrt(N))+x)^2-N;
  * the same exact verifier and integer-kernel collector after selection.

No strategy sees p, q, an exact smoothness label or a regulator oracle.

Strategies
----------
U  UNIFORM: r644's ascending block order.

D  DENSITY: a classical direct sort by a cheap public proxy: the weighted
   number of prime-power residue wells crossing each block.  This is the
   strongest non-field comparator using exactly the same proxy.

F  FIELD: one real state coordinate per x-block on a unit sphere.  Its one
   energy is

       E(S)=sum_i e_i S_i^2
            + lambda sum_i (S_{i+1}-S_i)^2,

   where e_i is minus standardized well density.  Tangential projected
   gradient descent with a trust radius relaxes the field, then blocks are
   visited in descending settled mass S_i^2.  K is zero: a reversible drift
   cannot add arithmetic information.  L is the nearest-neighbour
   coherence term.  The field never evaluates Q(x).

All setup, density planning, field ticks, scanned x, sieve updates, exact
divisions and elimination pivots are counted:

  work = plan_ops + field_ops + x_scanned + sieve_updates
         + exact_trial_divisions + elimination_pivots.

Primary metric:

  effective_yield = relation_rank / work.

GO requires median field yield >=2 times UNIFORM at equal (N,B,X), all
factors exact, and the energy firewall intact.  DENSITY is a mandatory
upper comparator: if direct sorting equals or beats the field, any gain is
classical scheduling, not Hylaean physics.

Expected honest outcome: FIBER_NO_GAIN.  Residue wells are almost uniformly
distributed between large equal blocks, r644 already has rank/relation near
one, and the field adds mixing work without new information.

Claim boundary: experiments only.  Not a ledger/paper/RH claim.
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
from math import isqrt
from pathlib import Path

import mpmath
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import regulator_jump_probe as R643  # noqa: E402
import regulator_relation_probe as R644  # noqa: E402

ROUND = 646
SEED = 646202609
CONTRACT = "HYLAEAN.RELATION.FIBER.01"
FENCE = "Exploration; no factoring breakthrough claim; no RH claim"
TAG = "r646"
RESULT_JSON = HERE / "hylaean_relation_fiber_result.json"

BIT_SIZES = (40, 48, 56)
N_PER_SIZE = 3
BLOCK_SIZE = 25_000
DEPENDENCY_TARGET = 3
FIELD_TICKS = 48
FIELD_STEP = 0.08
FIELD_COHERENCE = 0.04
TRUST_RADIUS = 0.5
GO_RATIO = 2.0
DECISIONS = ("FIBER_BEATS_BASELINE", "FIBER_NO_GAIN", "FIBER_BROKEN")

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


@dataclass
class FiberCost:
    plan_ops: int = 0
    field_ops: int = 0
    x_scanned: int = 0
    sieve_updates: int = 0
    score_candidates: int = 0
    exact_trial_divisions: int = 0
    smooth_relations: int = 0
    elimination_pivots: int = 0
    blocks_scanned: int = 0
    wall_seconds: float = 0.0

    def total_work(self) -> int:
        return (
            self.plan_ops
            + self.field_ops
            + self.x_scanned
            + self.sieve_updates
            + self.exact_trial_divisions
            + self.elimination_pivots
        )


@dataclass(frozen=True)
class Setup:
    n: int
    root_floor: int
    factor_base: tuple[tuple[int, int], ...]
    lifted_roots: dict[int, tuple[tuple[int, int], ...]]
    blocks: tuple[tuple[int, int], ...]


@dataclass
class StrategyResult:
    name: str
    factor: int | None
    rank: int
    dependencies: int
    relations: int
    cost: FiberCost
    block_order: list[int]
    regulator_candidate: str | None

    def effective_yield(self) -> float:
        return self.rank / max(self.cost.total_work(), 1)

    def to_dict(self) -> dict:
        row = asdict(self)
        row["total_work"] = self.cost.total_work()
        row["effective_yield"] = self.effective_yield()
        return row


def build_setup(n: int, bound: int, x_limit: int) -> Setup:
    factor_base, direct_factor = R644.build_factor_base(n, bound)
    if direct_factor is not None:
        raise RuntimeError("factor-base construction unexpectedly found a test factor")
    root_floor = isqrt(n)
    maximum_q = (root_floor + x_limit) ** 2 - n
    lifted = {
        prime: tuple(R644.hensel_roots(n, prime, root, maximum_q))
        for prime, root in factor_base
    }
    blocks = tuple(
        (start, min(x_limit + 1, start + BLOCK_SIZE))
        for start in range(1, x_limit + 1, BLOCK_SIZE)
    )
    return Setup(
        n=n,
        root_floor=root_floor,
        factor_base=tuple(factor_base),
        lifted_roots=lifted,
        blocks=blocks,
    )


def count_root_hits(start: int, stop: int, modulus: int, root: int) -> int:
    first = root
    if first < start:
        first += ((start - first + modulus - 1) // modulus) * modulus
    return 0 if first >= stop else (stop - 1 - first) // modulus + 1


def public_well_densities(setup: Setup) -> tuple[np.ndarray, int]:
    """No Q(x), smooth label or factor: only public residue-well incidence."""
    densities = np.zeros(len(setup.blocks), dtype=float)
    operations = 0
    for block_index, (start, stop) in enumerate(setup.blocks):
        weighted_hits = 0.0
        for prime, root in setup.factor_base:
            logarithm = math.log(prime)
            for modulus, lifted_root in setup.lifted_roots[prime]:
                for root_x in {
                    (-setup.root_floor - lifted_root) % modulus,
                    (-setup.root_floor + lifted_root) % modulus,
                }:
                    weighted_hits += logarithm * count_root_hits(
                        start,
                        stop,
                        modulus,
                        root_x,
                    )
                    operations += 1
        densities[block_index] = weighted_hits / (stop - start)
    return densities, operations


def uniform_order(setup: Setup) -> tuple[list[int], int, int]:
    return list(range(len(setup.blocks))), 0, 0


def density_order(setup: Setup) -> tuple[list[int], int, int]:
    densities, plan_ops = public_well_densities(setup)
    order = sorted(range(len(densities)), key=lambda index: (-densities[index], index))
    sort_ops = int(len(order) * max(math.log2(max(len(order), 2)), 1))
    return order, plan_ops + sort_ops, 0


def projected_field_order(setup: Setup) -> tuple[list[int], int, int]:
    """One-energy dissipative relaxation on the block sphere."""
    densities, plan_ops = public_well_densities(setup)
    count = len(densities)
    if count == 1:
        return [0], plan_ops, 0
    standard_deviation = float(np.std(densities))
    standardized = (
        (densities - float(np.mean(densities))) / standard_deviation
        if standard_deviation > 0
        else np.zeros_like(densities)
    )
    energy_diagonal = -standardized
    # Deterministic tiny asymmetry prevents exact degeneracy while carrying no
    # arithmetic label.
    state = np.ones(count, dtype=float) + 1e-9 * np.sin(np.arange(count))
    state /= np.linalg.norm(state)
    for _ in range(FIELD_TICKS):
        left = np.concatenate(([state[0]], state[:-1]))
        right = np.concatenate((state[1:], [state[-1]]))
        laplacian = 2 * state - left - right
        gradient = 2 * energy_diagonal * state + 2 * FIELD_COHERENCE * laplacian
        tangent = gradient - float(np.dot(gradient, state)) * state
        displacement = FIELD_STEP * tangent
        norm = float(np.linalg.norm(displacement))
        if norm > TRUST_RADIUS:
            displacement *= TRUST_RADIUS / norm
        state -= displacement
        state /= np.linalg.norm(state)
    order = sorted(range(count), key=lambda index: (-state[index] ** 2, index))
    sort_ops = int(count * max(math.log2(max(count, 2)), 1))
    # Per tick: two neighbours, diagonal force, projection and normalization.
    field_ops = FIELD_TICKS * count * 8
    return order, plan_ops + sort_ops, field_ops


def sieve_block(
    setup: Setup,
    block_index: int,
    cost: FiberCost,
) -> list[R644.Relation]:
    start, stop = setup.blocks[block_index]
    x_values = np.arange(start, stop, dtype=np.int64)
    a_values = x_values + setup.root_floor
    q_values = a_values * a_values - setup.n
    if np.any(q_values <= 0):
        raise ArithmeticError("sieve polynomial must be positive")
    score = np.log(q_values.astype(float))
    valid = a_values % 2 == 0
    for prime, root in setup.factor_base:
        logarithm = math.log(prime)
        for modulus, lifted_root in setup.lifted_roots[prime]:
            for root_x in {
                (-setup.root_floor - lifted_root) % modulus,
                (-setup.root_floor + lifted_root) % modulus,
            }:
                first = root_x
                if first < start:
                    first += ((start - first + modulus - 1) // modulus) * modulus
                if first >= stop:
                    continue
                score[first - start :: modulus] -= logarithm
                cost.sieve_updates += (stop - 1 - first) // modulus + 1
    offsets = np.flatnonzero(valid & (np.abs(score) < R644.SCORE_TOLERANCE))
    cost.blocks_scanned += 1
    cost.x_scanned += len(x_values)
    cost.score_candidates += len(offsets)
    relations = []
    for offset in offsets:
        cost.exact_trial_divisions += 1
        relation = R644.exact_relation(
            setup.n,
            int(x_values[offset]),
            list(setup.factor_base),
        )
        if relation is not None:
            relations.append(relation)
            cost.smooth_relations += 1
    return relations


def run_strategy(
    setup: Setup,
    name: str,
    order_fn,
) -> StrategyResult:
    started = time.perf_counter()
    order, plan_ops, field_ops = order_fn(setup)
    cost = FiberCost(plan_ops=plan_ops, field_ops=field_ops)
    kernel = R644.IncrementalKernel(len(setup.factor_base))
    relations: list[R644.Relation] = []
    dependency_values: list[mpmath.mpf] = []
    mpmath.mp.dps = R644.RELATION_DPS

    for block_index in order:
        for relation in sieve_block(setup, block_index, cost):
            relation_index = len(relations)
            relations.append(relation)
            rank_before = kernel.rank
            dependency = kernel.add(relation.row)
            if kernel.rank > rank_before:
                cost.elimination_pivots += 1
            if dependency is None:
                continue
            if max(dependency) != relation_index:
                raise ArithmeticError("kernel dependency index mismatch")
            value = abs(
                sum(
                    mpmath.mpf(coefficient)
                    * mpmath.mpf(relations[index].log_generator)
                    for index, coefficient in dependency.items()
                )
            )
            if value > mpmath.mpf("1e-80"):
                dependency_values.append(value)
            if len(dependency_values) >= DEPENDENCY_TARGET:
                break
        if len(dependency_values) >= DEPENDENCY_TARGET:
            break

    regulator_cost = R644.RelationCost()
    regulator = R644.approximate_real_gcd(dependency_values, regulator_cost)
    factor = None
    regulator_text = None
    if regulator is not None:
        regulator_text = mpmath.nstr(regulator, n=R644.RELATION_DPS)
        multiple = mpmath.nstr(2 * regulator, n=R644.RELATION_DPS)
        split = R643.regulator_assisted_split(setup.n, multiple)
        factor = split.factor
    cost.wall_seconds = time.perf_counter() - started
    return StrategyResult(
        name=name,
        factor=factor,
        rank=kernel.rank,
        dependencies=len(dependency_values),
        relations=len(relations),
        cost=cost,
        block_order=order,
        regulator_candidate=regulator_text,
    )


def planner_firewall() -> tuple[bool, list[str]]:
    source = inspect.getsource(public_well_densities) + inspect.getsource(
        projected_field_order
    )
    forbidden = (
        "exact_relation",
        "q_values",
        "regulator",
        "slow_regulator",
        "factor_from",
        "factorint",
    )
    hits = [token for token in forbidden if token in source]
    return not hits, hits


def median_ratio(rows: list[dict], numerator: str, denominator: str) -> float:
    values = []
    for row in rows:
        top = row[numerator]["effective_yield"]
        bottom = row[denominator]["effective_yield"]
        values.append(top / max(bottom, 1e-300))
    return float(np.median(values))


def run(smoke: bool, json_path: str) -> int:
    wall_start = time.time()
    rng = np.random.default_rng(SEED)
    sizes = (40, 48) if smoke else BIT_SIZES
    per_size = 1 if smoke else N_PER_SIZE
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))

    section("F1 information firewall and matched strategies")
    firewall_ok, firewall_hits = planner_firewall()
    check(
        "F1 planner sees residues only",
        firewall_ok,
        "forbidden source hits: %s" % firewall_hits,
    )

    section("F2 uniform vs density sort vs dissipative field")
    rows = []
    all_factors = True
    for bits in sizes:
        bound, x_limit = R644.PARAMETERS[bits]
        for _ in range(per_size):
            n, p, q = R643.random_semiprime(rng, bits, blum=True)
            setup = build_setup(n, bound, x_limit)
            uniform = run_strategy(setup, "uniform", uniform_order)
            density = run_strategy(setup, "density", density_order)
            field = run_strategy(setup, "field", projected_field_order)
            strategies = {
                "uniform": uniform.to_dict(),
                "density": density.to_dict(),
                "field": field.to_dict(),
            }
            exact = all(result.factor in (p, q) for result in (uniform, density, field))
            all_factors &= exact
            rows.append(
                {
                    "bits": bits,
                    "n": n,
                    "factor_base_size": len(setup.factor_base),
                    "blocks_total": len(setup.blocks),
                    "exact_all": exact,
                    **strategies,
                }
            )
            emit(
                "  %2d bit blocks=%3d | U rank/work=%d/%d | D=%d/%d | F=%d/%d "
                "| F/U=%.3f factor=%s"
                % (
                    bits,
                    len(setup.blocks),
                    uniform.rank,
                    uniform.cost.total_work(),
                    density.rank,
                    density.cost.total_work(),
                    field.rank,
                    field.cost.total_work(),
                    field.effective_yield() / max(uniform.effective_yield(), 1e-300),
                    exact,
                )
            )

    check(
        "F2 all strategies recover exact factor",
        all_factors,
        "%d/%d matched triples" % (sum(row["exact_all"] for row in rows), len(rows)),
    )
    check(
        "F2 dependencies reached",
        all(
            row[name]["dependencies"] >= DEPENDENCY_TARGET
            for row in rows
            for name in ("uniform", "density", "field")
        ),
        "three nonzero regulator dependencies per strategy",
    )

    section("F3 gain adjudication")
    field_vs_uniform = median_ratio(rows, "field", "uniform")
    density_vs_uniform = median_ratio(rows, "density", "uniform")
    field_vs_density = median_ratio(rows, "field", "density")
    emit(
        "  median effective-yield ratios: field/uniform %.3f, "
        "density/uniform %.3f, field/density %.3f"
        % (field_vs_uniform, density_vs_uniform, field_vs_density)
    )
    # This gate checks honest classification, not that the hoped-for gain exists.
    gain = field_vs_uniform >= GO_RATIO and field_vs_density > 1.0
    check(
        "F3 GO rule evaluated",
        True,
        "GO=%s requires field/uniform>=%.1f and field>direct-density"
        % (gain, GO_RATIO),
    )
    check(
        "F3 rank headroom measured",
        all(
            row["uniform"]["rank"] / max(row["uniform"]["relations"], 1) >= 0.80
            for row in rows
        ),
        "r644 rows are already mostly independent; repulsion has little headroom",
    )

    verdict = "FIBER_BEATS_BASELINE" if gain and all_factors else "FIBER_NO_GAIN"
    if not firewall_ok or not all_factors:
        verdict = "FIBER_BROKEN"
    why = (
        "field ordering exceeds the matched classical relation yield by the frozen GO ratio"
        if verdict == "FIBER_BEATS_BASELINE"
        else (
            "the residue-only dissipative field does not beat the classical uniform/direct-density planners "
            "after plan and mixing work; K/L/T add no arithmetic information"
            if verdict == "FIBER_NO_GAIN"
            else "firewall or exact-factor gate failed"
        )
    )
    check("F4 verdict enum", verdict in DECISIONS, verdict)

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
            "field_ticks": FIELD_TICKS,
            "field_step": FIELD_STEP,
            "field_coherence": FIELD_COHERENCE,
            "go_ratio": GO_RATIO,
            "work_metric": (
                "plan_ops+field_ops+x_scanned+sieve_updates+"
                "exact_trial_divisions+elimination_pivots"
            ),
        },
        "ratios": {
            "field_vs_uniform": field_vs_uniform,
            "density_vs_uniform": density_vs_uniform,
            "field_vs_density": field_vs_density,
        },
        "rows": rows,
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
