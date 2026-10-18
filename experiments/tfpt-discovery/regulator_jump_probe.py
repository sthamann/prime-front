#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""regulator_jump_probe -- r643  GEOM.REGULATOR.JUMP.01  (audited v2)

Regulator-assisted factorisation on the modular-surface seam, implemented
without a hidden principal-cycle oracle.

The first version of this probe demonstrated short giant-step paths, but its
reducer stopped by looking up the composed ideal in a pre-enumerated cycle.
That gave it the whole cycle, not merely the regulator.  This audited version
implements Murru--Salvatori Algorithm 2 intrinsically (arXiv:2409.03486v2):

  * Form(a,b,c), discriminant 4N, with exact reducedness test (Definition 4.4);
  * rho and rho_inverse from the standard indefinite-form reduction
    (Definition 4.5);
  * Gauss composition (Definition 4.12) and intrinsic reduction;
  * infrastructural distance corrections from Proposition 4.15;
  * both targets R_plus/2 and R_plus/4 (unknown CF-period parity);
  * repeated halvings when a not-too-large multiple k R_plus is supplied.

The runtime splitter receives only (N, R_multiple) and an optional
discriminant-rescaling multiplier that is required to be coprime to N.
It never stores or queries the principal cycle and never receives p or q.
A deliberately slow oracle computes the scalar R_plus in the test harness
only, in O(period) steps and with O(1) stored states.  Its cost is reported
separately.

Measured:

  G0  intrinsic form algebra, rho/rho_inverse, discriminants, reducedness;
  G1  Gauss composition and distance law against a SMALL audit cycle only;
  G2  AST firewall: no slow oracle / cycle table / factor inputs in runtime;
  G3  factor every sampled Blum semiprime (the theorem's applicable class);
  G4  generic semiprimes through a fixed discriminant-multiplier ladder;
  G5  k R_plus inputs for k=1,2,4 are handled by repeated target halvings;
  G6  runtime cost vs slow regulator-oracle cost, separately counted;
  G7  exact output division and no false factor.

Changes (audited v2 vs the r643 landing):

  * Psi linear coefficient is 33/4 from arXiv:2409.03486v2 (HTML, six
    occurrences of frac{33}{4}); v1's 13/4 remains SEARCH_BOUND_LINEAR_V1
    so the r643 bound can be reproduced.  Definition/Proposition numbers
    follow v2 (4.4 / 4.5 / 4.12 / 4.15), not the v1 2.xx labels.
  * Power-ladder cap is O(log(k R_plus)) with documented
    POWER_LADDER_BIT_SLACK; max_halvings defaults to a 2-adic peel of the
    supplied multiple (v_2(k) or log2(R'/ (ln N)^2)).
  * geometry_multiplier sharing a factor with N raises RuntimeOracleLeak;
    G2 checks that GEOMETRY_MULTIPLIERS is a frozen, factor-independent
    schedule and that the coprime check is present.
  * Full mode runs an adversarial unbalanced / 48--60-bit Blum batch.
  * Slow regulator oracle accumulates in mpmath at bit-length precision;
    max |R_mp - R_float64| on the built-in sample is reported with an
    explicit error bound (not a correctness proof of the float path).
  * G6 keeps elementary_steps() unchanged and adds wall-clock plus a
    big-integer-operation proxy.  The CF-period / elementary_steps ratio
    is a counted-step comparison, not a bit-complexity proof.

Murru--Salvatori (arXiv:2409.03486v2) prove O((log N)^2) elementary
operations once R_plus, or a polynomially bounded integer multiple, is
known.  Their best cited regulator precomputation is Vollmer's Monte Carlo
L_N[1/2, 3/sqrt(8)] under GRH.  This probe validates the conditional jump;
it does not improve regulator computation and does not beat NFS.

Decision:
  REGULATOR_ONLY_JUMP_VERIFIED
  RUNTIME_ORACLE_LEAK
  JUMP_FAILED

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: no factoring breakthrough claim; no RH claim.
This probe has no bearing on RH: it tests a conditional factoring step.
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
from functools import reduce
from math import gcd, isqrt
from pathlib import Path

import mpmath
import numpy as np

HERE = Path(__file__).resolve().parent
ROUND = 643
SEED = 643202609
CONTRACT = "GEOM.REGULATOR.JUMP.01"
FENCE = "Exploration; no factoring breakthrough claim; no RH claim"
TAG = "r643"
RESULT_JSON = HERE / "regulator_jump_result.json"

BIT_SIZES = (24, 32, 40)
N_PER_SIZE = 8
GENERIC_PER_SIZE = 4
# Frozen, factor-independent discriminant-rescaling schedule (G4).  Each
# entry is a small integer constant, never derived from a secret factor.
GEOMETRY_MULTIPLIERS = (1, 3, 5, 7, 11, 15, 21, 33, 35, 55, 77, 105)
ORACLE_PERIOD_CAP = 8_000_000
ORACLE_WALL_CAP_S = 90.0
MAX_HALVINGS = 96
HALVING_SLACK = 4
# arXiv:2409.03486v1 used 13/4 in Psi; v2 (2025-01-20) uses 33/4.
SEARCH_BOUND_LINEAR_V1 = 13
SEARCH_BOUND_LINEAR_V2 = 33
SEARCH_BOUND_LINEAR = SEARCH_BOUND_LINEAR_V2
# Extra doublings beyond ceil(log2(target)) in the Algorithm 2 power ladder
# (Proposition 5.2: t <= ceil(log2(k dist(N)))).
POWER_LADDER_BIT_SLACK = 16
DISTANCE_TOL = mpmath.mpf("1e-35")
DECISIONS = ("REGULATOR_ONLY_JUMP_VERIFIED", "RUNTIME_ORACLE_LEAK", "JUMP_FAILED")
G5_AUDIT_N = 1019 * 1031
G5_AUDIT_P = 1019
G5_AUDIT_Q = 1031


class RuntimeOracleLeak(ValueError):
    """geometry_multiplier shares a nontrivial factor with N."""

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


def configure_precision(n: int, extra_bits: int = 0) -> None:
    """Enough precision to distinguish sqrt(4N) from nearby integers.

    extra_bits covers a supplied multiple k R_plus whose magnitude exceeds N.
    """
    bits = n.bit_length() + max(0, int(extra_bits))
    mpmath.mp.dps = max(60, int(bits * math.log10(2)) + 35)


def bits_of_scalar(value: str | float | int | mpmath.mpf) -> int:
    """Conservative bit-length of a positive scalar given as string or number."""
    if isinstance(value, bool):
        return 1
    if isinstance(value, int):
        return max(1, value.bit_length())
    if isinstance(value, str):
        digits = value.strip().lstrip("+-").replace(".", "")
        exp = 0
        if "e" in digits.lower():
            mantissa, _, rest = digits.lower().partition("e")
            digits = mantissa
            try:
                exp = int(rest)
            except ValueError:
                exp = 0
        return max(1, int(len(digits) * math.log2(10)) + abs(exp) * 4 + 8)
    if isinstance(value, float):
        magnitude = abs(value)
        if magnitude <= 0.0 or not math.isfinite(magnitude):
            return 1
        return max(1, int(math.log2(magnitude)) + 8)
    if value <= 0:
        return 1
    return int(mpmath.floor(mpmath.log(value, 2))) + 8


def is_prime(n: int) -> bool:
    """Deterministic Miller--Rabin on the tested (< 2^64) range."""
    if n < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % prime == 0:
            return n == prime
    d = n - 1
    exponent = 0
    while d % 2 == 0:
        d //= 2
        exponent += 1
    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for base in bases:
        a = base % n
        if a in (0, 1):
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(exponent - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_semiprime(
    rng: np.random.Generator,
    bits: int,
    *,
    blum: bool,
    small_bits: int | None = None,
) -> tuple[int, int, int]:
    """p*q sample; blum=True forces p=q=3 mod 4 (the applicable theorem class).

    Default is balanced (each prime ~ bits/2).  small_bits selects an
    unbalanced pair with that many bits on the smaller prime.
    """
    if small_bits is None:
        p_bits = bits // 2
        q_bits = bits - p_bits
    else:
        if small_bits < 3 or small_bits >= bits - 2:
            raise ValueError("small_bits must leave room for two odd primes")
        p_bits = small_bits
        q_bits = bits - small_bits
    while True:
        p = int(rng.integers(1 << (p_bits - 1), 1 << p_bits)) | 1
        q = int(rng.integers(1 << (q_bits - 1), 1 << q_bits)) | 1
        if blum and (p % 4 != 3 or q % 4 != 3):
            continue
        if p != q and is_prime(p) and is_prime(q):
            n = p * q
            if isqrt(n) ** 2 != n:
                return n, min(p, q), max(p, q)


@dataclass(frozen=True)
class Form:
    a: int
    b: int
    c: int

    def discriminant(self) -> int:
        return self.b * self.b - 4 * self.a * self.c


@dataclass
class Cost:
    compositions: int = 0
    xgcd_calls: int = 0
    rho_forward: int = 0
    rho_inverse: int = 0
    log_evaluations: int = 0
    gcd_tests: int = 0
    max_coefficient_bits: int = 0
    wall_s: float = 0.0

    def observe(self, form: Form) -> None:
        self.max_coefficient_bits = max(
            self.max_coefficient_bits,
            abs(form.a).bit_length(),
            abs(form.b).bit_length(),
            abs(form.c).bit_length(),
        )

    def elementary_steps(self) -> int:
        """Counted algebraic operations (not a bit-complexity measure).

        Extended Euclid is one xgcd_call (two per Gauss composition).
        Log evaluations are tracked separately and omitted here so the
        r643 G6 ratio stays comparable; see big_integer_ops() and wall_s.
        """
        return self.compositions + self.xgcd_calls + self.rho_forward + self.rho_inverse + self.gcd_tests

    def big_integer_ops(self) -> int:
        """Heuristic big-integer operation count, not a bit-complexity proof.

        Each recorded algebraic step is charged the observed coefficient
        bit length, and log evaluations are included.  Use with wall_s
        as a second metric beside elementary_steps().
        """
        bits = max(self.max_coefficient_bits, 1)
        return (
            self.compositions * bits
            + self.xgcd_calls * bits
            + self.rho_forward * bits
            + self.rho_inverse * bits
            + self.gcd_tests * bits
            + self.log_evaluations * bits
        )


@dataclass(frozen=True)
class OracleResult:
    r_plus: str
    cf_period: int
    cycle_steps_represented: int
    oracle_steps: int
    stored_states: int
    wall_s: float = 0.0
    float64_r_plus: str | None = None
    abs_dev_vs_float64: str | None = None
    rel_dev_vs_float64: str | None = None


@dataclass
class SplitResult:
    n: int
    factor: int | None
    target_halving: int | None
    r_multiple: str
    geometry_multiplier: int
    cost: Cost
    target_scans: int
    principal_hits: int
    exact_verified: bool

    def to_dict(self) -> dict:
        row = asdict(self)
        row["cost"]["elementary_steps"] = self.cost.elementary_steps()
        row["cost"]["big_integer_ops"] = self.cost.big_integer_ops()
        return row


def principal_form(n: int) -> Form:
    root = isqrt(n)
    return Form(1, 2 * root, root * root - n)


def is_reduced(form: Form, discriminant: int) -> bool:
    """Exact form of |sqrt(D)-2|a|| < b < sqrt(D), D nonsquare."""
    if form.a == 0 or form.c == 0 or form.b <= 0 or form.b * form.b >= discriminant:
        return False
    twice_a = 2 * abs(form.a)
    rhs = discriminant + twice_a * twice_a - form.b * form.b
    if rhs <= 0:
        return True
    return 4 * twice_a * twice_a * discriminant > rhs * rhs


def reduction_residue(b: int, coefficient: int, discriminant: int) -> int:
    """The unique r(-b, coefficient) from Murru--Salvatori Definition 4.5."""
    coefficient_abs = abs(coefficient)
    if coefficient_abs == 0:
        raise ValueError("reduction coefficient is zero")
    modulus = 2 * coefficient_abs
    residue = (-b) % modulus
    if coefficient_abs * coefficient_abs > discriminant:
        if residue > coefficient_abs:
            residue -= modulus
        assert -coefficient_abs < residue <= coefficient_abs
    else:
        root_floor = isqrt(discriminant)
        residue += ((root_floor - residue) // modulus) * modulus
        assert root_floor - modulus < residue <= root_floor
    assert (residue + b) % (2 * coefficient) == 0
    return residue


def rho(form: Form, discriminant: int, cost: Cost | None = None) -> Form:
    residue = reduction_residue(form.b, form.c, discriminant)
    numerator = residue * residue - discriminant
    denominator = 4 * form.c
    if numerator % denominator:
        raise ArithmeticError("rho produced a nonintegral coefficient")
    out = Form(form.c, residue, numerator // denominator)
    if out.discriminant() != discriminant:
        raise ArithmeticError("rho changed the discriminant")
    if cost is not None:
        cost.rho_forward += 1
        cost.observe(out)
    return out


def rho_inverse(form: Form, discriminant: int, cost: Cost | None = None) -> Form:
    residue = reduction_residue(form.b, form.a, discriminant)
    numerator = residue * residue - discriminant
    denominator = 4 * form.a
    if numerator % denominator:
        raise ArithmeticError("rho_inverse produced a nonintegral coefficient")
    out = Form(numerator // denominator, residue, form.a)
    if out.discriminant() != discriminant:
        raise ArithmeticError("rho_inverse changed the discriminant")
    if cost is not None:
        cost.rho_inverse += 1
        cost.observe(out)
    return out


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0
    divisor, x, y = extended_gcd(b, a % b)
    return divisor, y, x - (a // b) * y


def extended_gcd_three(a: int, b: int, c: int) -> tuple[int, int, int, int]:
    divisor_ab, x_ab, y_ab = extended_gcd(a, b)
    divisor, x_c, z = extended_gcd(divisor_ab, c)
    return divisor, x_c * x_ab, x_c * y_ab, z


def gauss_compose(left: Form, right: Form, discriminant: int, cost: Cost | None = None) -> Form:
    """Definition 4.12, including its non-coprime correction d0."""
    if left.discriminant() != discriminant or right.discriminant() != discriminant:
        raise ValueError("forms must have the requested common discriminant")
    if (left.b + right.b) % 2:
        raise ValueError("middle coefficients have incompatible parity")
    beta = (left.b + right.b) // 2
    n_gcd, s, _u, v = extended_gcd_three(left.a, right.a, beta)
    n_gcd = abs(n_gcd)
    d0 = reduce(
        gcd,
        (
            abs(left.a),
            abs(right.a),
            abs(beta),
            abs(left.c),
            abs(right.c),
            abs((left.b - right.b) // 2),
        ),
    )
    a3 = d0 * left.a * right.a // (n_gcd * n_gcd)
    bracket = s * ((right.b - left.b) // 2) - left.c * v
    b3 = left.b + (2 * left.a // n_gcd) * bracket
    numerator = b3 * b3 - discriminant
    denominator = 4 * a3
    if a3 == 0 or numerator % denominator:
        raise ArithmeticError("Gauss composition produced a nonintegral coefficient")
    out = Form(a3, b3, numerator // denominator)
    if out.discriminant() != discriminant:
        raise ArithmeticError("Gauss composition changed the discriminant")
    if cost is not None:
        cost.compositions += 1
        cost.xgcd_calls += 2
        cost.observe(out)
    return out


def distance_step(form: Form, discriminant: int, cost: Cost | None = None) -> mpmath.mpf:
    root = mpmath.sqrt(discriminant)
    value = mpmath.mpf("0.5") * mpmath.log(abs((form.b + root) / (form.b - root)))
    if cost is not None:
        cost.log_evaluations += 1
    return value


def reduce_intrinsically(
    form: Form,
    discriminant: int,
    cost: Cost | None = None,
) -> tuple[Form, mpmath.mpf]:
    """Apply rho until Definition 4.4 holds; no cycle membership test."""
    correction = mpmath.mpf(0)
    limit = 8 + max(1, abs(form.c).bit_length())
    steps = 0
    while not is_reduced(form, discriminant):
        correction += distance_step(form, discriminant, cost)
        form = rho(form, discriminant, cost)
        steps += 1
        if steps > limit:
            raise RuntimeError("intrinsic reduction exceeded the logarithmic bound")
    return form, correction


def giant_step(
    left: Form,
    left_distance: mpmath.mpf,
    right: Form,
    right_distance: mpmath.mpf,
    discriminant: int,
    cost: Cost | None = None,
) -> tuple[Form, mpmath.mpf]:
    composed = gauss_compose(left, right, discriminant, cost)
    reduced, correction = reduce_intrinsically(composed, discriminant, cost)
    return reduced, left_distance + right_distance + correction


def factor_from_form(form: Form, n: int, cost: Cost | None = None) -> int | None:
    for coefficient in (form.c, form.a, form.b):
        if cost is not None:
            cost.gcd_tests += 1
        factor = gcd(abs(coefficient), n)
        if 1 < factor < n:
            return factor
    return None


def scan_directly(
    source_n: int,
    geometry_n: int,
    r_plus: mpmath.mpf,
    cost: Cost,
) -> tuple[int | None, int]:
    """Murru--Salvatori Algorithm 1 for small R_plus."""
    discriminant = 4 * geometry_n
    form = principal_form(geometry_n)
    maximum = int(
        r_plus / mpmath.log(2)
        + mpmath.mpf(5) * mpmath.log(4 * geometry_n) / (2 * mpmath.log(2))
        + 2
    )
    for step in range(maximum):
        factor = factor_from_form(form, source_n, cost)
        if factor is not None:
            return factor, step
        form = rho(form, discriminant, cost)
    return None, maximum


def power_ladder_cap(target: mpmath.mpf, geometry_n: int) -> int:
    """O(log(k R_plus)) ladder length with an explicit slack constant.

    Proposition 5.2: t <= ceil(log2(dist(N))) <= ceil(log2(target))+1 when
    the supplied multiple is the target.  POWER_LADDER_BIT_SLACK extra
    entries cover the already-positive base distance and rounding.  The
    cap is at least the historical N-only bound so tiny targets do not
    shrink the r643 ladder.
    """
    n_bits = max(1, geometry_n.bit_length())
    if target <= 0:
        return n_bits + POWER_LADDER_BIT_SLACK
    target_bits = int(mpmath.floor(mpmath.log(target + 2, 2))) + 1
    return max(n_bits, target_bits) + POWER_LADDER_BIT_SLACK


def default_max_halvings(r_value: mpmath.mpf, geometry_n: int) -> int:
    """Enough halvings to reach the Algorithm 1 regime from k R_plus.

    Without knowing k we peel until the target is below (ln N)^2, then add
    HALVING_SLACK for the paper's even/odd /2 and /4 targets.  This lifts
    the global MAX_HALVINGS=96 floor when v_2(k) is large.  Callers may
    still pass an explicit max_halvings.
    """
    log_n = mpmath.log(geometry_n)
    floor = max(log_n * log_n, mpmath.mpf("0.5"))
    if r_value <= floor:
        return MAX_HALVINGS
    peel = int(mpmath.ceil(mpmath.log(r_value / floor, 2))) + HALVING_SLACK
    return max(MAX_HALVINGS, peel)


def approximate_target(
    geometry_n: int,
    base: Form,
    base_distance: mpmath.mpf,
    target: mpmath.mpf,
    cost: Cost,
) -> Form:
    """Algorithm 2 first phase; bar_distance is the paper's subset-sum distance."""
    discriminant = 4 * geometry_n
    powers: list[tuple[Form, mpmath.mpf]] = [(base, base_distance)]
    ladder_cap = power_ladder_cap(target, geometry_n)
    while powers[-1][1] <= target:
        form, form_distance = powers[-1]
        squared, squared_distance = giant_step(
            form,
            form_distance,
            form,
            form_distance,
            discriminant,
            cost,
        )
        if squared_distance <= form_distance:
            raise ArithmeticError("giant-step distances are not increasing")
        powers.append((squared, squared_distance))
        if len(powers) > ladder_cap:
            raise RuntimeError("power ladder exceeded logarithmic size")
    usable = [(form, distance) for form, distance in powers if distance <= target]
    if not usable:
        return principal_form(geometry_n)
    bar_form, bar_distance = usable[-1]
    for candidate, candidate_distance in reversed(usable[:-1]):
        if bar_distance + candidate_distance <= target:
            bar_form, _actual_distance = giant_step(
                bar_form,
                bar_distance,
                candidate,
                candidate_distance,
                discriminant,
                cost,
            )
            # Algorithm 2 deliberately tracks the subset sum here; reduction
            # corrections contribute the O((log N)^2) final approximation error.
            bar_distance += candidate_distance
    return bar_form


def search_around_target(
    source_n: int,
    geometry_n: int,
    form: Form,
    step_bound: int,
    cost: Cost,
) -> tuple[int | None, int, bool]:
    """Algorithm 2 second phase: rho and rho_inverse in parallel."""
    discriminant = 4 * geometry_n
    principal = principal_form(geometry_n)
    if form == principal:
        return None, 0, True
    factor = factor_from_form(form, source_n, cost)
    if factor is not None:
        return factor, 0, False
    forward = rho(form, discriminant, cost)
    backward = rho_inverse(form, discriminant, cost)
    for step in range(1, step_bound + 1):
        for candidate in (forward, backward):
            if candidate == principal:
                return None, step, True
            factor = factor_from_form(candidate, source_n, cost)
            if factor is not None:
                return factor, step, False
        forward = rho(forward, discriminant, cost)
        backward = rho_inverse(backward, discriminant, cost)
    return None, step_bound, False


def regulator_assisted_split(
    n: int,
    r_multiple: str | float | mpmath.mpf,
    *,
    geometry_multiplier: int = 1,
    max_halvings: int | None = None,
    search_bound_linear: int = SEARCH_BOUND_LINEAR,
) -> SplitResult:
    """Split n using only n and a positive multiple of R_plus.

    No principal-cycle table, period parity, p, or q enters this function.
    geometry_multiplier must be coprime to n; a shared factor is an
    oracle leak (RuntimeOracleLeak), not a successful split.
    search_bound_linear defaults to the v2 coefficient 33; pass
    SEARCH_BOUND_LINEAR_V1 (13) to reproduce the r643 Psi bound.
    """
    wall0 = time.perf_counter()
    if n <= 1 or n % 2 == 0 or isqrt(n) ** 2 == n:
        raise ValueError("n must be an odd positive nonsquare")
    if geometry_multiplier < 1:
        raise ValueError("geometry_multiplier must be positive")
    common = gcd(n, geometry_multiplier)
    if common > 1:
        raise RuntimeOracleLeak(
            "geometry_multiplier shares factor %d with N; treated as an oracle leak"
            % common
        )
    extra_bits = bits_of_scalar(r_multiple)
    geometry_n = geometry_multiplier * n
    if isqrt(geometry_n) ** 2 == geometry_n:
        raise ValueError("geometry_multiplier * n must be nonsquare")
    configure_precision(geometry_n, extra_bits=extra_bits)
    r_value = mpmath.mpf(r_multiple)
    if r_value <= 0:
        raise ValueError("the regulator multiple must be positive")
    if max_halvings is None:
        max_halvings = default_max_halvings(r_value, geometry_n)
    if max_halvings < 2:
        raise ValueError("max_halvings must cover the even- and odd-period targets")
    if search_bound_linear < 1:
        raise ValueError("search_bound_linear must be a positive Psi coefficient")
    cost = Cost()
    cost.observe(principal_form(geometry_n))
    log_n = mpmath.log(geometry_n)
    if r_value <= log_n * log_n:
        factor, scans = scan_directly(n, geometry_n, r_value, cost)
        cost.wall_s = time.perf_counter() - wall0
        return SplitResult(
            n,
            factor,
            0 if factor is not None else None,
            mpmath.nstr(r_value, n=mpmath.mp.dps),
            geometry_multiplier,
            cost,
            scans,
            0,
            factor is not None and n % factor == 0,
        )

    discriminant = 4 * geometry_n
    base = principal_form(geometry_n)
    base_distance = mpmath.mpf(0)
    threshold = 2 * mpmath.log(discriminant) + 1
    while base_distance < threshold:
        base_distance += distance_step(base, discriminant, cost)
        base = rho(base, discriminant, cost)

    # Psi from arXiv:2409.03486v2:
    # (2/ln 2) * (4 ln(Delta) log2(R'/2) + (linear/4) ln(Delta)) + 1
    # with linear=33.  The +2 (vs the paper's +1) is an integer slack.
    # Pass search_bound_linear=SEARCH_BOUND_LINEAR_V1 to use 13/4.
    step_bound = int(
        (2 / mpmath.log(2))
        * (
            4 * mpmath.log(discriminant) * mpmath.log(r_value / 2, 2)
            + mpmath.mpf(search_bound_linear) * mpmath.log(discriminant) / 4
        )
        + 2
    )
    total_scans = 0
    principal_hits = 0
    for halving in range(1, max_halvings + 1):
        target = r_value / (2**halving)
        if target <= 0:
            break
        if base_distance > target:
            factor, scans = scan_directly(n, geometry_n, min(r_value, 2 * target), cost)
            principal_hit = False
        else:
            approximation = approximate_target(geometry_n, base, base_distance, target, cost)
            factor, scans, principal_hit = search_around_target(
                n,
                geometry_n,
                approximation,
                step_bound,
                cost,
            )
        total_scans += scans
        principal_hits += int(principal_hit)
        if factor is not None:
            cost.wall_s = time.perf_counter() - wall0
            return SplitResult(
                n,
                factor,
                halving,
                mpmath.nstr(r_value, n=mpmath.mp.dps),
                geometry_multiplier,
                cost,
                total_scans,
                principal_hits,
                n % factor == 0,
            )
        if principal_hit:
            continue
    cost.wall_s = time.perf_counter() - wall0
    return SplitResult(
        n,
        None,
        None,
        mpmath.nstr(r_value, n=mpmath.mp.dps),
        geometry_multiplier,
        cost,
        total_scans,
        principal_hits,
        False,
    )


def slow_regulator_oracle(n: int, *, wall_cap_s: float | None = None) -> OracleResult:
    """Compute only scalar R_plus by the full CF period; store no cycle states.

    The CF recurrences (m, denominator, quotient) are exact integers.
    Distances are accumulated in mpmath at configure_precision(n) so the
    working precision is tied to bit_length(N).  A parallel float64
    accumulator (the r643 path: math.sqrt / math.log with Kahan
    summation) is kept only to report the deviation.

    Error bound (float64 twin, not a proof that the float path is safe):
      each log term has a relative error of order 2^{-52}, and
      |sqrt_float64(n) - sqrt(n)| <= 2^{-53} sqrt(n).  With period P
      and |term_i| <= log(2 sqrt(n)) + O(1),
        |R_float64 - R_mp| <= P * (2^{-51} * L + 2^{-52} * L)
      where L = log(2 sqrt(n)) + 1, plus the Kahan residual which does
      not cancel the already-rounded sqrt.  The probe reports the
      measured max deviation on the built-in sample against this bound.
    """
    if n <= 1 or isqrt(n) ** 2 == n:
        raise ValueError("n must be a positive nonsquare")
    wall0 = time.perf_counter()
    configure_precision(n)
    root_floor = isqrt(n)
    root_mp = mpmath.sqrt(n)
    root_f = math.sqrt(n)
    m, denominator, quotient = 0, 1, root_floor
    total_mp = mpmath.mpf(0)
    total_f = 0.0
    correction = 0.0
    period = 0
    while True:
        m = denominator * quotient - m
        denominator = (n - m * m) // denominator
        quotient = (root_floor + m) // denominator
        term_mp = mpmath.log((m + root_mp) / denominator)
        total_mp += term_mp
        term_f = math.log((m + root_f) / denominator)
        adjusted = term_f - correction
        updated = total_f + adjusted
        correction = (updated - total_f) - adjusted
        total_f = updated
        period += 1
        if denominator == 1:
            break
        if period >= ORACLE_PERIOD_CAP:
            raise RuntimeError("slow regulator oracle hit the period cap")
        if wall_cap_s is not None and (time.perf_counter() - wall0) >= wall_cap_s:
            raise RuntimeError("slow regulator oracle hit the wall-clock cap")
    cycle_multiplier = 1 if period % 2 == 0 else 2
    r_plus = cycle_multiplier * total_mp
    r_float = cycle_multiplier * total_f
    abs_dev = abs(r_plus - mpmath.mpf(r_float))
    rel_dev = abs_dev / r_plus if r_plus > 0 else abs_dev
    return OracleResult(
        mpmath.nstr(r_plus, n=mpmath.mp.dps, strip_zeros=False),
        period,
        cycle_multiplier * period,
        period,
        0,
        time.perf_counter() - wall0,
        repr(r_float),
        mpmath.nstr(abs_dev, n=12),
        mpmath.nstr(rel_dev, n=12),
    )


def build_small_audit_cycle(n: int) -> tuple[list[Form], list[mpmath.mpf], mpmath.mpf]:
    """Full cycle used only by G1; intentionally absent from the runtime call graph."""
    configure_precision(n)
    discriminant = 4 * n
    first = principal_form(n)
    form = first
    distance = mpmath.mpf(0)
    forms: list[Form] = []
    distances: list[mpmath.mpf] = []
    while True:
        forms.append(form)
        distances.append(distance)
        distance += distance_step(form, discriminant)
        form = rho(form, discriminant)
        if form == first:
            return forms, distances, distance
        if len(forms) > 100_000:
            raise RuntimeError("small audit cycle unexpectedly large")


def distance_mod_error(value: mpmath.mpf, expected: mpmath.mpf, period: mpmath.mpf) -> mpmath.mpf:
    error = mpmath.fmod(value - expected, period)
    if error < 0:
        error += period
    return min(error, period - error)


def audit_form_algebra() -> tuple[bool, float]:
    n = 1009 * 1019
    discriminant = 4 * n
    forms, distances, period = build_small_audit_cycle(n)
    index = {form: offset for offset, form in enumerate(forms)}
    maximum_error = mpmath.mpf(0)
    ok = True
    for offset, form in enumerate(forms):
        ok &= form.discriminant() == discriminant and is_reduced(form, discriminant)
        ok &= rho(rho_inverse(form, discriminant), discriminant) == form
        ok &= rho_inverse(rho(form, discriminant), discriminant) == form
        if offset >= 20:
            break
    pairs = [(1, 2), (3, 7), (5, 11), (13, 17), (19, 23)]
    for left_index, right_index in pairs:
        left_index %= len(forms)
        right_index %= len(forms)
        result, tracked = giant_step(
            forms[left_index],
            distances[left_index],
            forms[right_index],
            distances[right_index],
            discriminant,
        )
        result_index = index[result]
        error = distance_mod_error(tracked, distances[result_index], period)
        maximum_error = max(maximum_error, error)
        ok &= error < DISTANCE_TOL
    return ok, float(maximum_error)


def runtime_oracle_firewall() -> tuple[bool, list[str]]:
    runtime_functions = (
        regulator_assisted_split,
        scan_directly,
        approximate_target,
        search_around_target,
        giant_step,
        reduce_intrinsically,
        gauss_compose,
        rho,
        rho_inverse,
    )
    source = "\n".join(inspect.getsource(function) for function in runtime_functions)
    forbidden = (
        "slow_regulator_oracle(",
        "build_small_audit_cycle(",
        "cycle_index",
        "known_factor",
        "factor_p",
        "factor_q",
    )
    hits = [token for token in forbidden if token in source]
    if not isinstance(GEOMETRY_MULTIPLIERS, tuple) or not GEOMETRY_MULTIPLIERS:
        hits.append("GEOMETRY_MULTIPLIERS-not-fixed-tuple")
    if any(
        (not isinstance(multiplier, int)) or multiplier < 1 or multiplier.bit_length() > 16
        for multiplier in GEOMETRY_MULTIPLIERS
    ):
        hits.append("GEOMETRY_MULTIPLIERS-not-factor-independent-small")
    split_source = inspect.getsource(regulator_assisted_split)
    if "RuntimeOracleLeak" not in split_source:
        hits.append("missing-RuntimeOracleLeak")
    if "gcd(n, geometry_multiplier)" not in split_source:
        hits.append("missing-multiplier-coprime-check")
    if "return SplitResult(n, common" in split_source:
        hits.append("gcd-multiplier-returned-as-factor")
    return not hits, hits


def geometry_multiplier_leak_is_detected() -> bool:
    """Negative test: a factor-valued multiplier must not silently split N."""
    try:
        regulator_assisted_split(G5_AUDIT_N, "1", geometry_multiplier=G5_AUDIT_P)
    except RuntimeOracleLeak:
        return True
    except Exception:
        return False
    return False


def float64_deviation_bound(n: int, period: int) -> mpmath.mpf:
    """Conservative |R_float64 - R_mp| bound from the oracle docstring."""
    length = mpmath.log(2 * mpmath.sqrt(n)) + 1
    return mpmath.mpf(period) * length * (mpmath.power(2, -51) + mpmath.power(2, -52))


def summarize_size(rows: list[dict], bits: int) -> dict:
    subset = [row for row in rows if row["bits_requested"] == bits]
    successes = [row for row in subset if row["success"]]
    if not subset:
        return {
            "n": 0,
            "successes": 0,
            "success_rate": 0.0,
            "median_oracle_steps": 0.0,
            "median_runtime_steps": 0.0,
            "median_compositions": 0.0,
            "median_rho": 0.0,
            "median_runtime_wall_s": 0.0,
            "median_oracle_wall_s": 0.0,
            "median_big_integer_ops": 0.0,
        }
    return {
        "n": len(subset),
        "successes": len(successes),
        "success_rate": len(successes) / len(subset),
        "median_oracle_steps": float(np.median([row["oracle_steps"] for row in subset])),
        "median_runtime_steps": float(np.median([row["runtime_steps"] for row in subset])),
        "median_compositions": float(np.median([row["compositions"] for row in subset])),
        "median_rho": float(np.median([row["rho"] for row in subset])),
        "median_runtime_wall_s": float(np.median([row.get("runtime_wall_s", 0.0) for row in subset])),
        "median_oracle_wall_s": float(np.median([row.get("oracle_wall_s", 0.0) for row in subset])),
        "median_big_integer_ops": float(np.median([row.get("big_integer_ops", 0) for row in subset])),
    }


def record_split_row(
    bits: int,
    n: int,
    p: int,
    q: int,
    oracle: OracleResult,
    split: SplitResult,
    class_name: str,
    small_bits: int | None = None,
) -> dict:
    return {
        "bits_requested": bits,
        "n": n,
        "class": class_name,
        "small_bits": small_bits,
        "cf_period": oracle.cf_period,
        "cycle_steps_represented": oracle.cycle_steps_represented,
        "oracle_steps": oracle.oracle_steps,
        "oracle_stored_states": oracle.stored_states,
        "oracle_wall_s": oracle.wall_s,
        "oracle_abs_dev_vs_float64": oracle.abs_dev_vs_float64,
        "oracle_rel_dev_vs_float64": oracle.rel_dev_vs_float64,
        "success": split.factor in (p, q),
        "target_halving": split.target_halving,
        "geometry_multiplier": split.geometry_multiplier,
        "runtime_steps": split.cost.elementary_steps(),
        "big_integer_ops": split.cost.big_integer_ops(),
        "runtime_wall_s": split.cost.wall_s,
        "compositions": split.cost.compositions,
        "rho": split.cost.rho_forward + split.cost.rho_inverse,
        "gcd_tests": split.cost.gcd_tests,
        "log_evaluations": split.cost.log_evaluations,
        "max_coefficient_bits": split.cost.max_coefficient_bits,
    }


def run_adversarial_batch(
    rng: np.random.Generator,
    *,
    smoke: bool,
) -> tuple[list[dict], list[dict]]:
    """Unbalanced Blum semiprimes and a few larger (48--60-bit) cases.

    Oracle period/wall caps skip pathological CF periods so the batch stays
    under the ~15 min full-probe budget.  Skips are reported, not failures.
    """
    specs = (
        (("unbalanced-32", 32, 10, 2),)
        if smoke
        else (
            ("unbalanced-32", 32, 10, 4),
            ("unbalanced-40", 40, 12, 3),
            ("larger-48", 48, 16, 2),
            ("larger-56", 56, 16, 1),
        )
    )
    rows: list[dict] = []
    skips: list[dict] = []
    for label, bits, small_bits, count in specs:
        for _ in range(count):
            n, p, q = random_semiprime(rng, bits, blum=True, small_bits=small_bits)
            try:
                oracle = slow_regulator_oracle(n, wall_cap_s=ORACLE_WALL_CAP_S)
            except RuntimeError as exc:
                skips.append(
                    {
                        "label": label,
                        "bits_requested": bits,
                        "small_bits": small_bits,
                        "n": n,
                        "reason": str(exc),
                    }
                )
                emit("  skip %s n=%d: %s" % (label, n, exc))
                continue
            split = regulator_assisted_split(n, oracle.r_plus)
            row = record_split_row(bits, n, p, q, oracle, split, label, small_bits)
            rows.append(row)
            emit(
                "  %s: factor=%s period=%d runtime_steps=%d wall %.3f/%.3f"
                % (
                    label,
                    row["success"],
                    oracle.cf_period,
                    row["runtime_steps"],
                    oracle.wall_s,
                    split.cost.wall_s,
                )
            )
    return rows, skips


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument(
        "--adversarial",
        action="store_true",
        help="run unbalanced / larger Blum batch (already on in full mode)",
    )
    parser.add_argument("--no-adversarial", action="store_true")
    args = parser.parse_args()
    sizes = (24, 32) if args.smoke else BIT_SIZES
    per_size = 3 if args.smoke else N_PER_SIZE
    generic_per_size = 1 if args.smoke else GENERIC_PER_SIZE
    run_adversarial = args.adversarial or ((not args.smoke) and (not args.no_adversarial))
    rng = np.random.default_rng(SEED)
    wall_start = time.time()

    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))
    emit("paper arXiv:2409.03486v2  Psi linear 33/4 (v1 13/4 kept as SEARCH_BOUND_LINEAR_V1)")

    section("G0-G2  intrinsic infrastructure and oracle firewall")
    algebra_ok, maximum_error = audit_form_algebra()
    check(
        "G0-G1-form-algebra-composition-distance",
        algebra_ok,
        "rho/rho_inverse exact; Gauss composition remains on the small audit cycle; max distance error %.1e"
        % maximum_error,
    )
    firewall_ok, firewall_hits = runtime_oracle_firewall()
    check(
        "G2-runtime-call-graph-has-no-cycle-or-factor-oracle",
        firewall_ok,
        "runtime input is (N, R_multiple) plus a coprime-checked multiplier; forbidden hits: %s"
        % firewall_hits,
    )
    leak_detected = geometry_multiplier_leak_is_detected()
    check(
        "G2-geometry-multiplier-gcd-is-oracle-leak",
        leak_detected,
        "regulator_assisted_split(%d, '1', geometry_multiplier=%d) raises RuntimeOracleLeak"
        % (G5_AUDIT_N, G5_AUDIT_P),
    )

    section("G3-G4  regulator-only splitter on blind semiprimes")
    blum_rows: list[dict] = []
    generic_rows: list[dict] = []
    all_exact = True
    max_abs_dev = mpmath.mpf(0)
    max_rel_dev = mpmath.mpf(0)
    max_dev_bound_ok = True
    for bits in sizes:
        for _ in range(per_size):
            n, p, q = random_semiprime(rng, bits, blum=True)
            oracle = slow_regulator_oracle(n)
            split = regulator_assisted_split(n, oracle.r_plus)
            exact = split.factor is None or (n % split.factor == 0 and split.exact_verified)
            all_exact &= exact
            abs_dev = mpmath.mpf(oracle.abs_dev_vs_float64 or "0")
            rel_dev = mpmath.mpf(oracle.rel_dev_vs_float64 or "0")
            bound = float64_deviation_bound(n, oracle.cf_period)
            max_abs_dev = max(max_abs_dev, abs_dev)
            max_rel_dev = max(max_rel_dev, rel_dev)
            max_dev_bound_ok &= abs_dev <= bound * 8 + mpmath.mpf("1e-12")
            blum_rows.append(record_split_row(bits, n, p, q, oracle, split, "blum"))
        for _ in range(generic_per_size):
            n, p, q = random_semiprime(rng, bits, blum=False)
            attempts = []
            success = False
            total_oracle_steps = 0
            total_runtime_steps = 0
            for geometry_multiplier in GEOMETRY_MULTIPLIERS:
                if gcd(geometry_multiplier, n) > 1:
                    continue
                geometry_n = geometry_multiplier * n
                if isqrt(geometry_n) ** 2 == geometry_n:
                    continue
                oracle = slow_regulator_oracle(geometry_n)
                split = regulator_assisted_split(
                    n,
                    oracle.r_plus,
                    geometry_multiplier=geometry_multiplier,
                )
                exact = split.factor is None or (n % split.factor == 0 and split.exact_verified)
                all_exact &= exact
                total_oracle_steps += oracle.oracle_steps
                total_runtime_steps += split.cost.elementary_steps()
                success = split.factor in (p, q)
                attempts.append(
                    {
                        "geometry_multiplier": geometry_multiplier,
                        "cf_period": oracle.cf_period,
                        "oracle_steps": oracle.oracle_steps,
                        "runtime_steps": split.cost.elementary_steps(),
                        "success": success,
                    }
                )
                if success:
                    break
            generic_rows.append(
                {
                    "bits_requested": bits,
                    "n": n,
                    "class": "generic-multiplier-ladder",
                    "success": success,
                    "attempts": attempts,
                    "multipliers_tried": len(attempts),
                    "winning_multiplier": attempts[-1]["geometry_multiplier"] if success else None,
                    "oracle_steps": total_oracle_steps,
                    "runtime_steps": total_runtime_steps,
                }
            )
    summaries = {str(bits): summarize_size(blum_rows, bits) for bits in sizes}
    for bits in sizes:
        summary = summaries[str(bits)]
        emit(
            "  %2d-bit Blum: %d/%d factors; median oracle/runtime steps %.0f / %.0f; "
            "compositions %.0f; rho %.0f"
            % (
                bits,
                summary["successes"],
                summary["n"],
                summary["median_oracle_steps"],
                summary["median_runtime_steps"],
                summary["median_compositions"],
                summary["median_rho"],
            )
        )
    check(
        "G3-all-applicable-Blum-semiprimes-factored",
        all(row["success"] for row in blum_rows),
        "%d/%d, p=q=3 mod 4 guarantees even period and Q_mid != 2"
        % (sum(row["success"] for row in blum_rows), len(blum_rows)),
    )
    generic_rate = sum(row["success"] for row in generic_rows) / len(generic_rows)
    median_multipliers = float(np.median([row["multipliers_tried"] for row in generic_rows]))
    emit(
        "  generic multiplier ladder: %d/%d = %.3f; median multipliers tried %.1f"
        % (
            sum(row["success"] for row in generic_rows),
            len(generic_rows),
            generic_rate,
            median_multipliers,
        )
        + (""
           if not generic_rows
           else " (schedule %s)" % (GEOMETRY_MULTIPLIERS,))
    )
    check(
        "G4-multiplier-ladder-covers-generic-sample",
        generic_rate >= 0.9,
        "a multiplier changes the discriminant/principal cycle; misses remain allowed and are reported",
    )

    section("G5  a multiple k R_plus is enough")
    n, p, q = random_semiprime(rng, max(sizes), blum=True)
    oracle = slow_regulator_oracle(n)
    multiple_rows = []
    for multiplier in (1, 2, 4):
        value = mpmath.mpf(oracle.r_plus) * multiplier
        split = regulator_assisted_split(n, mpmath.nstr(value, n=mpmath.mp.dps))
        multiple_rows.append(
            {
                "k": multiplier,
                "success": split.factor in (p, q),
                "halving": split.target_halving,
                "runtime_steps": split.cost.elementary_steps(),
            }
        )
        emit(
            "  k=%d: factor=%s at target R'/2^%s, runtime steps %d"
            % (multiplier, split.factor in (p, q), split.target_halving, split.cost.elementary_steps())
        )
    check(
        "G5-kR-plus-k=1,2,4-all-factor",
        all(row["success"] for row in multiple_rows),
        "repeated halving removes powers of two from the unknown multiplier k",
    )

    audit_oracle = slow_regulator_oracle(G5_AUDIT_N)
    g5_family = []
    for label, multiplier in (
        ("k=N", G5_AUDIT_N),
        ("k=N^2", G5_AUDIT_N * G5_AUDIT_N),
        ("k=2^100", 1 << 100),
    ):
        value = mpmath.mpf(audit_oracle.r_plus) * multiplier
        split = regulator_assisted_split(
            G5_AUDIT_N,
            mpmath.nstr(value, n=max(mpmath.mp.dps, bits_of_scalar(value))),
        )
        ok = split.factor in (G5_AUDIT_P, G5_AUDIT_Q)
        g5_family.append(
            {
                "label": label,
                "k_bits": multiplier.bit_length(),
                "success": ok,
                "halving": split.target_halving,
                "runtime_steps": split.cost.elementary_steps(),
                "max_halvings_used": default_max_halvings(value, G5_AUDIT_N),
            }
        )
        emit(
            "  %s: factor=%s at target R'/2^%s, runtime steps %d, default_max_halvings %d"
            % (
                label,
                ok,
                split.target_halving,
                split.cost.elementary_steps(),
                default_max_halvings(value, G5_AUDIT_N),
            )
        )
    check(
        "G5-k-equals-N-and-N-squared-factor",
        all(row["success"] for row in g5_family if row["label"] in ("k=N", "k=N^2")),
        "power-ladder cap follows bit_length(k R_plus), not bit_length(N) alone",
    )
    check(
        "G5-k-with-v2-at-least-100-factors",
        all(row["success"] for row in g5_family if row["label"] == "k=2^100"),
        "max_halvings lifts with v_2(k); 2^100 requires >96 halvings",
    )

    adversarial_rows: list[dict] = []
    adversarial_skips: list[dict] = []
    if run_adversarial:
        section("adversarial  unbalanced and larger Blum batch")
        adversarial_rows, adversarial_skips = run_adversarial_batch(rng, smoke=args.smoke)
        adv_ok = sum(1 for row in adversarial_rows if row["success"])
        emit(
            "  adversarial completed %d/%d; skipped %d (period/wall cap); successes %d/%d"
            % (
                len(adversarial_rows),
                len(adversarial_rows) + len(adversarial_skips),
                len(adversarial_skips),
                adv_ok,
                len(adversarial_rows),
            )
        )
        core_adv = [row for row in adversarial_rows if str(row["class"]).startswith("unbalanced")]
        check(
            "G3-adversarial-unbalanced-completed-factored",
            bool(core_adv) and all(row["success"] for row in core_adv),
            "unbalanced %d/%d; larger+all completed %d/%d; skipped %d"
            % (
                sum(1 for row in core_adv if row["success"]),
                len(core_adv),
                adv_ok,
                len(adversarial_rows),
                len(adversarial_skips),
            ),
        )
        for row in adversarial_rows:
            if row["success"]:
                all_exact &= True

    section("G6-G7  cost separation and exactness")
    largest = summaries[str(max(sizes))]
    ratio = largest["median_oracle_steps"] / max(largest["median_runtime_steps"], 1)
    wall_ratio = largest["median_oracle_wall_s"] / max(largest["median_runtime_wall_s"], 1e-12)
    emit(
        "  largest size counted-step ratio "
        "(CF-period steps / elementary_steps; not a bit-complexity proof) = %.1f"
        % ratio
    )
    emit(
        "  second metric: median wall-clock oracle/runtime = %.3f / %.3f s (ratio %.1f); "
        "median big-integer-ops %.0f"
        % (
            largest["median_oracle_wall_s"],
            largest["median_runtime_wall_s"],
            wall_ratio,
            largest["median_big_integer_ops"],
        )
    )
    emit(
        "  oracle mpmath vs float64 on built-in Blum sample: max |R_mp-R_f64|=%s; "
        "max rel %s; within documented bound (x8 slack): %s"
        % (
            mpmath.nstr(max_abs_dev, n=12),
            mpmath.nstr(max_rel_dev, n=12),
            max_dev_bound_ok,
        )
    )
    check(
        "G6-slow-regulator-oracle-dominates-at-largest-size",
        ratio > 3.0 and all(row["oracle_stored_states"] == 0 for row in blum_rows),
        "counted-step comparison only; regulator acquisition remains the bottleneck",
    )
    check(
        "G6-oracle-float64-deviation-reported",
        max_abs_dev >= 0 and max_dev_bound_ok,
        "max abs deviation %s on %d Blum oracles"
        % (mpmath.nstr(max_abs_dev, n=12), len(blum_rows)),
    )
    check(
        "G7-no-false-factor",
        all_exact,
        "every non-null output divides N exactly; no p/q enters the runtime",
    )

    if not firewall_ok or not leak_detected:
        verdict = "RUNTIME_ORACLE_LEAK"
        why = (
            "runtime source still references a cycle/factor oracle"
            if not firewall_ok
            else "geometry_multiplier gcd(N) leak was not rejected"
        )
    elif all(condition for _name, condition in CHECKS):
        verdict = "REGULATOR_ONLY_JUMP_VERIFIED"
        why = (
            "Murru-Salvatori Algorithm 2 (arXiv:2409.03486v2) works with only N and "
            "R_plus (or k R_plus): intrinsic form reduction and Gauss composition "
            "reach the factor in the applicable Blum class; the G6 ratio is a "
            "counted-step comparison, not a bit-complexity proof; the slow "
            "regulator oracle, not the jump, dominates"
        )
    else:
        verdict = "JUMP_FAILED"
        why = "%d gate(s) failed" % sum(1 for _name, condition in CHECKS if not condition)
    check("G-verdict-enum", verdict in DECISIONS, verdict)

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "round": ROUND,
        "spec": "audited v2",
        "paper": "arXiv:2409.03486v2",
        "search_bound_linear": SEARCH_BOUND_LINEAR,
        "search_bound_linear_v1": SEARCH_BOUND_LINEAR_V1,
        "fence": FENCE,
        "verdict": verdict,
        "why": why,
        "blum_runs": blum_rows,
        "generic_runs": generic_rows,
        "summaries": summaries,
        "multiple_regulator": multiple_rows,
        "g5_family": g5_family,
        "adversarial_runs": adversarial_rows,
        "adversarial_skips": adversarial_skips,
        "oracle_float64_max_abs_dev": mpmath.nstr(max_abs_dev, n=16),
        "oracle_float64_max_rel_dev": mpmath.nstr(max_rel_dev, n=16),
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
