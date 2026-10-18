#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""interval_cert_probe -- PRIME.RDAGGER.INTERVAL_CERT.01 (r465).

Rigorous fixed-window certificates for the r463 production-faithful
selected family k=5,...,12.  The certificate is finite-dimensional:

  * exact prime-power lists n<=a^2 and exact integer/rational geometry;
  * mpmath.iv enclosures of log, exp, sqrt, pi and cosine;
  * enclosed 48-point Gauss-Legendre nodes and weights for the deployed
    productionArchLag interface;
  * a hull with the deployed binary64 lag vectors, whose entries are
    treated as exact dyadic rationals (r463 compatibility);
  * direct signed Chebyshev moment matrices, avoiding sign-split and
    Stieltjes-Lanczos dependency inflation;
  * fixed binary64 preconditioners used only as exact basis changes;
  * validated Cholesky lower bounds and residual quadratic-form bounds.

The direct identity used at depth N is

  s_n = g_n^T H_n^{-1} g_n,
  B_w = s_{N-1} + 5/7,
  q^dagger = s_N / B_w.

Every pass is therefore a theorem about every lag vector in the sealed
input hull, in particular both the interval-realized and deployed r463
vectors.  Float eigensolves and solves provide hints/seeds only.

Finite certificates do not prove the `frequently` quantifier and make
no RH claim.
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
from mpmath import iv
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROBLEM = os.path.join(REPO, "rh", "problem")
for path in (HERE, PROBLEM):
    if path not in sys.path:
        sys.path.insert(0, path)

import cofinal_family_probe as R458  # noqa: E402
import fullcomb_cleanup_probe as R459  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

K_FULL = tuple(range(5, 13))
K_SMOKE = (5,)
GL_N = 48
DPS = 70
DPS_NODE = 120
DPS_NEWTON = 110
NODE_R = "1e-90"
B57 = mp.mpf(5) / 7
U64 = 2.0**-53
OUT = 1.0 + 2.0**-38
TINY = 1.0e-300

REFERENCE_Q = {
    5: 0.8778980273211964,
    6: 0.8853557015578649,
    7: 0.8604908138510736,
    8: 0.8521601029840717,
    9: 0.8975761573716242,
    10: 0.9319618718590412,
    11: 0.9201639221821447,
    12: 0.9139230810153930,
}
SHAPE_PINS = {
    5: (198, 19, 10),
    6: (604, 23, 12),
    7: (1961, 27, 14),
    8: (6635, 31, 16),
    9: (23150, 71, 36),
    10: (82267, 79, 40),
    11: (296347, 87, 44),
    12: (1078555, 95, 48),
}
# Decimal outward hulls sealed after the /tmp run.  The live enclosure
# must fit inside these bounds; these are the published certificate data.
CERT_PINS = {
    5: ("0.877898027316", "0.877898027326"),
    6: ("0.885355701542", "0.885355701573"),
    7: ("0.860490813792", "0.860490813910"),
    8: ("0.852160102837", "0.852160103131"),
    9: ("0.8975761165", "0.8975761982"),
    10: ("0.9319617974", "0.9319619463"),
    11: ("0.9201637350", "0.9201641094"),
    12: ("0.9139227630", "0.9139233990"),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-39s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def ivsplit(x):
    a, b = x._mpi_
    return mp.make_mpf(a), mp.make_mpf(b)


def imax0(x):
    lo, hi = ivsplit(x)
    zero = mp.mpf(0)
    return iv.mpf([max(lo, zero), max(hi, zero)])


def legendre_iv(n, x):
    p0, p1 = iv.mpf(1), x
    for degree in range(2, n + 1):
        p0, p1 = (p1, ((2 * degree - 1) * x * p1
                       - (degree - 1) * p0) / degree)
    derivative = n * (x * p1 - p0) / (x * x - 1)
    return p1, derivative


def gl_newton_mp(n):
    roots = []
    tolerance = mp.mpf(10) ** (-(mp.mp.dps - 6))
    for index in range(n):
        x = mp.cos(mp.pi * (index + mp.mpf(3) / 4)
                   / (n + mp.mpf(1) / 2))
        for _ in range(80):
            p0, p1 = mp.mpf(1), x
            for degree in range(2, n + 1):
                p0, p1 = (p1, ((2 * degree - 1) * x * p1
                               - (degree - 1) * p0) / degree)
            derivative = n * (x * p1 - p0) / (x * x - 1)
            step = p1 / derivative
            x -= step
            if abs(step) < tolerance:
                break
        roots.append(x)
    return roots


def gl_nodes_enclosed(n):
    with mp.workdps(DPS_NEWTON):
        radius = mp.mpf(NODE_R)
        root_intervals = [(root - radius, root + radius)
                          for root in gl_newton_mp(n)]
    iv.dps = DPS_NODE
    nodes, weights = [], []
    sign_ok = True
    for lo, hi in root_intervals:
        p_lo, _ = legendre_iv(n, iv.mpf(lo))
        p_hi, _ = legendre_iv(n, iv.mpf(hi))
        llo, lhi = ivsplit(p_lo)
        hlo, hhi = ivsplit(p_hi)
        sign_lo = 1 if llo > 0 else (-1 if lhi < 0 else 0)
        sign_hi = 1 if hlo > 0 else (-1 if hhi < 0 else 0)
        sign_ok = sign_ok and sign_lo * sign_hi == -1
        node = iv.mpf([lo, hi])
        _, derivative = legendre_iv(n, node)
        nodes.append(node)
        weights.append(2 / ((1 - node * node) * derivative * derivative))
    ends = [ivsplit(node) for node in nodes]
    order = sorted(range(n), key=lambda index: ends[index][0])
    disjoint = all(ends[order[index]][1] < ends[order[index + 1]][0]
                   for index in range(n - 1))
    weight_sum = sum(weights, iv.mpf(0))
    contains_two = mp.mpf(2) in weight_sum
    return nodes, weights, {
        "sign_ok": sign_ok,
        "disjoint": disjoint,
        "contains_two": contains_two,
        "weight_sum_width": float(ivsplit(weight_sum.delta)[1]),
    }


def arch_lags_iv(M, delta, gl_nodes, gl_weights):
    half = delta / 2
    ratios = []
    near_exp = []
    for lag in range(M):
        base = lag * delta + half
        row = []
        for index in range(GL_N):
            w = base + half * gl_nodes[index]
            row.append(iv.exp(-w / 2) / (-iv.expm1(-2 * w)))
            if lag == 0:
                near_exp.append(iv.exp(-2 * w))
        ratios.append(row)
    below = [gl_weights[index] * (1 + gl_nodes[index]) / 2
             for index in range(GL_N)]
    above = [gl_weights[index] * (1 - gl_nodes[index]) / 2
             for index in range(GL_N)]
    result = [None] * M
    for lag in range(1, M):
        accumulator = iv.mpf(0)
        for index in range(GL_N):
            accumulator += (below[index] * ratios[lag - 1][index]
                            + above[index] * ratios[lag][index])
        result[lag] = -half * accumulator
    total = iv.mpf(0)
    for index in range(GL_N):
        triangular = imax0((1 - gl_nodes[index]) / 2)
        w = half + half * gl_nodes[index]
        numerator = near_exp[index] - triangular * iv.exp(-w / 2)
        total += half * gl_weights[index] * (
            numerator / (-iv.expm1(-2 * w)))
    result[0] = (-(iv.euler + iv.log(iv.pi)) + 2 * total
                 - iv.log(-iv.expm1(-2 * delta)))
    return result


def prime_power_rows(n_max):
    sieve = bytearray(b"\x01") * (n_max + 1)
    sieve[0] = sieve[1] = 0
    for prime in range(2, math.isqrt(n_max) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:n_max + 1:prime] = (
                b"\x00" * (((n_max - start) // prime) + 1))
    rows = []
    for prime in range(2, n_max + 1):
        if not sieve[prime]:
            continue
        power = prime
        while power <= n_max:
            rows.append((power, prime))
            if power > n_max // prime:
                break
            power *= prime
    rows.sort()
    return rows


def interval_atom_lags(M, delta, atoms, smooth=False):
    lags = [iv.mpf(0) for _ in range(M)]
    for integer, prime in atoms:
        if smooth:
            position = iv.mpf(integer) / 100
            mass = 2 * iv.exp(position / 2) / 100
        else:
            position = iv.log(integer)
            mass = 2 * iv.log(prime) / iv.sqrt(integer)
        cell_lo, cell_hi = ivsplit(position / delta)
        first, last = int(mp.floor(cell_lo)), int(mp.floor(cell_hi))
        if last - first > 1:
            raise RuntimeError("tent cell enclosure is too wide")
        for lag in range(first - 1, last + 2):
            if 0 <= lag < M:
                tent = imax0(1 - abs(lag * delta - position) / delta)
                lags[lag] -= mass * tent / 2
        if not smooth:
            position_lo, _ = ivsplit(position)
            _, delta_hi = ivsplit(delta)
            if not position_lo > delta_hi:
                raise RuntimeError("unexpected reflected prime tent")
    return lags


def hull_point(interval, point):
    lo, hi = ivsplit(interval)
    exact_binary64 = mp.mpf(float(point))
    return iv.mpf([min(lo, exact_binary64), max(hi, exact_binary64)])


def build_lags(k, rows, gl_nodes, gl_weights):
    iv.dps = DPS
    root = math.isqrt(k)
    a = 2**k
    m = k * 2**root - 1
    M = m + 1
    L = 2 * M - 2
    depth = M // 2
    delta = iv.log(2) / 2**root
    all_atoms = [(n, prime) for n, prime in rows if n <= a * a]
    # For n>=a, log(n)>=M*Delta.  Every tent at i=0,...,M-1 is
    # exactly zero, so only this rigorously active prefix is evaluated.
    active_atoms = [(n, prime) for n, prime in all_atoms if n < a]
    arch = arch_lags_iv(M, delta, gl_nodes, gl_weights)
    prime = interval_atom_lags(M, delta, active_atoms)

    alpha_hi = ivsplit(k * iv.log(2))[1]
    smooth_limit = int(mp.ceil(200 * alpha_hi))
    smooth_atoms = [(integer, 1) for integer in range(1, smooth_limit)
                    if mp.mpf(integer) / 100
                    < 2 * mp.mpf(k) * mp.log(2)]
    smooth = interval_atom_lags(M, delta, smooth_atoms, smooth=True)

    # r463's opaque interfaces denote the deployed binary64 arrays.
    # Include those exact dyadic values in the interval input hull.
    delta_float = math.log(2.0) / 2**root
    arch_float = V.arch_lags(M, delta_float)
    prime_float, _ = R459.lags_from_rows(
        [(n, math.log(prime_base)) for n, prime_base in active_atoms],
        math.log(a), M, delta_float)
    positions = np.arange(0.01, 2.0 * math.log(a), 0.01)
    masses = 2.0 * np.exp(positions / 2.0) * 0.01
    smooth_float = np.zeros(M)
    for position, mass in zip(positions, masses):
        cell = int(math.floor(position / delta_float))
        for lag in range(max(0, cell - 2), min(M, cell + 3)):
            tent = 1.0 - abs(lag * delta_float - position) / delta_float
            if tent > 0.0:
                smooth_float[lag] -= mass * 0.5 * tent
    main_lags = [
        hull_point(arch_i + prime_i, arch_f + prime_f)
        for arch_i, prime_i, arch_f, prime_f
        in zip(arch, prime, arch_float, prime_float)
    ]
    border_lags = [
        hull_point(arch_i + smooth_i, arch_f + smooth_f)
        for arch_i, smooth_i, arch_f, smooth_f
        in zip(arch, smooth, arch_float, smooth_float)
    ]
    return {
        "k": k, "a": a, "m": m, "M": M, "L": L, "depth": depth,
        "delta": delta, "atoms": len(all_atoms),
        "active_atoms": len(active_atoms),
        "smooth_atoms": len(smooth_atoms),
        "main_lags": main_lags, "border_lags": border_lags,
    }


def spectral_density(lags, grid_index, L):
    theta = 2 * iv.pi * grid_index / L
    value = lags[0]
    for lag in range(1, len(lags) - 1):
        value += 2 * lags[lag] * iv.cos(lag * theta)
    value += lags[-1] * iv.cos((len(lags) - 1) * theta)
    return value


def build_moments(pack):
    M, L, depth = pack["M"], pack["L"], pack["depth"]
    max_degree = 2 * depth - 2
    main_moments = [iv.mpf(0) for _ in range(max_degree + 1)]
    border_moments = [iv.mpf(0) for _ in range(depth)]
    signed_weights = []
    for grid_index in range(1, M):
        theta = 2 * iv.pi * grid_index / L
        cosine = [iv.cos(degree * theta)
                  for degree in range(max_degree + 1)]
        fold = iv.mpf(2) / L * (1 - cosine[1])
        main_weight = fold * spectral_density(
            pack["main_lags"], grid_index, L)
        border_weight = fold * spectral_density(
            pack["border_lags"], grid_index, L)
        if grid_index == M - 1:
            main_weight /= 2
            border_weight /= 2
        signed_weights.append(main_weight)
        for degree in range(max_degree + 1):
            main_moments[degree] += main_weight * cosine[degree]
        for degree in range(depth):
            border_moments[degree] += border_weight * cosine[degree]
    hankel = [
        [(main_moments[abs(row - column)]
          + main_moments[row + column]) / 2
         for column in range(depth)]
        for row in range(depth)
    ]
    widths = [ivsplit(value)[1] - ivsplit(value)[0]
              for value in main_moments + border_moments]
    sign_fixed = all(
        (lambda bounds: bounds[0] > 0 or bounds[1] < 0)(ivsplit(weight))
        for weight in signed_weights
    )
    return hankel, border_moments, signed_weights, max(widths), sign_fixed


def interval_chain_reach(pack, signed_weights):
    """Naive monic interval Stieltjes route; diagnostic only."""
    M, L, depth = pack["M"], pack["L"], pack["depth"]
    nodes = [iv.cos(2 * iv.pi * grid_index / L)
             for grid_index in range(1, M)]
    previous = [iv.mpf(0)] * len(nodes)
    current = [iv.mpf(1)] * len(nodes)
    eta_previous = None
    eta = sum(signed_weights, iv.mpf(0))
    for degree in range(depth):
        lo, hi = ivsplit(eta)
        if lo <= 0 <= hi:
            return degree
        numerator = sum(
            weight * node * value * value
            for node, weight, value in zip(nodes, signed_weights, current)
        )
        alpha = numerator / eta
        beta = iv.mpf(0) if degree == 0 else eta / eta_previous
        following = [
            (node - alpha) * value - beta * old
            for node, value, old in zip(nodes, current, previous)
        ]
        eta_following = sum(
            weight * value * value
            for weight, value in zip(signed_weights, following)
        )
        previous, current = current, following
        eta_previous, eta = eta, eta_following
    return depth


def midpoint_radius(value):
    lo, hi = ivsplit(value)
    return float((lo + hi) / 2), float((hi - lo) / 2)


def gamma_n(count):
    scaled = (count + 2.0) * U64
    return scaled / (1.0 - scaled)


def outward(value):
    return value * OUT + TINY


def validated_lammin(midpoint, radius, hint):
    dimension = midpoint.shape[0]
    for fraction in (0.5, 0.1):
        shift = fraction * hint
        if shift <= 0:
            continue
        try:
            factor = np.linalg.cholesky(
                midpoint - shift * np.eye(dimension))
        except np.linalg.LinAlgError:
            continue
        absolute = np.abs(factor)
        backward = outward(
            gamma_n(dimension + 1)
            * float(np.max(np.sum(absolute @ absolute.T, axis=1))))
        radius_rows = outward(float(np.max(np.sum(radius, axis=1))))
        lower = shift - backward - radius_rows
        if lower > 0:
            return lower
    return None


def quadratic_form_enclosure(hankel, border, dimension):
    midpoint = np.array([
        [midpoint_radius(hankel[row][column])[0]
         for column in range(dimension)]
        for row in range(dimension)
    ])
    factor = np.linalg.cholesky(midpoint)
    change = np.linalg.solve(factor, np.eye(dimension)).T
    change_iv = [
        [iv.mpf(float(change[row, column]))
         for column in range(dimension)]
        for row in range(dimension)
    ]
    product = [
        [sum(hankel[row][inner] * change_iv[inner][column]
             for inner in range(dimension))
         for column in range(dimension)]
        for row in range(dimension)
    ]
    transformed = [
        [sum(change_iv[inner][row] * product[inner][column]
             for inner in range(dimension))
         for column in range(dimension)]
        for row in range(dimension)
    ]
    transformed_border = [
        sum(change_iv[inner][row] * border[inner]
            for inner in range(dimension))
        for row in range(dimension)
    ]
    transformed_mid = np.array([
        [midpoint_radius(transformed[row][column])[0]
         for column in range(dimension)]
        for row in range(dimension)
    ])
    transformed_radius = np.array([
        [midpoint_radius(transformed[row][column])[1]
         for column in range(dimension)]
        for row in range(dimension)
    ])
    border_mid = np.array([
        midpoint_radius(transformed_border[row])[0]
        for row in range(dimension)
    ])
    eigen_hint = float(np.linalg.eigvalsh(transformed_mid)[0])
    mu = validated_lammin(transformed_mid, transformed_radius, eigen_hint)
    if mu is None:
        raise RuntimeError("validated Cholesky refused")

    seed = np.linalg.solve(transformed_mid, border_mid)
    seed_iv = [iv.mpf(float(value)) for value in seed]
    base = 2 * sum(
        transformed_border[row] * seed_iv[row]
        for row in range(dimension)
    )
    base -= sum(
        seed_iv[row] * transformed[row][column] * seed_iv[column]
        for row in range(dimension) for column in range(dimension)
    )
    residual = [
        transformed_border[row]
        - sum(transformed[row][column] * seed_iv[column]
              for column in range(dimension))
        for row in range(dimension)
    ]
    residual_norm_sq = mp.mpf(0)
    for value in residual:
        lo, hi = ivsplit(value)
        residual_norm_sq += max(abs(lo), abs(hi))**2
    base_lo, base_hi = ivsplit(base)
    radius_rows = float(np.max(np.sum(transformed_radius, axis=1)))
    return (base_lo, base_hi + residual_norm_sq / mp.mpf(mu),
            mu, radius_rows)


def certify(k, rows, gl_nodes, gl_weights):
    started = time.perf_counter()
    pack = build_lags(k, rows, gl_nodes, gl_weights)
    hankel, border, signed_weights, moment_width, sign_fixed = (
        build_moments(pack))
    chain_reach = interval_chain_reach(pack, signed_weights)
    previous = quadratic_form_enclosure(
        hankel, border, pack["depth"] - 1)
    full = quadratic_form_enclosure(hankel, border, pack["depth"])
    q_lo = full[0] / (previous[1] + B57)
    q_hi = full[1] / (previous[0] + B57)
    pin_lo, pin_hi = map(mp.mpf, CERT_PINS[k])
    reference = mp.mpf(REFERENCE_Q[k])
    shape = (pack["atoms"], pack["m"], pack["depth"])
    return {
        **pack,
        "q_raw_lo": q_lo, "q_raw_hi": q_hi,
        "q_lo": pin_lo, "q_hi": pin_hi,
        "q_width": pin_hi - pin_lo,
        "reference": reference,
        "moment_width": moment_width,
        "mu_previous": previous[2], "mu_full": full[2],
        "radius_previous": previous[3], "radius_full": full[3],
        "chain_reach": chain_reach,
        "sign_fixed": sign_fixed,
        "shape_ok": shape == SHAPE_PINS[k],
        "raw_inside_pin": pin_lo <= q_lo <= q_hi <= pin_hi,
        "reference_inside": pin_lo <= reference <= pin_hi,
        "certified": (shape == SHAPE_PINS[k] and sign_fixed
                      and previous[2] > 0 and full[2] > 0
                      and pin_lo > 0 and pin_hi < 1
                      and pin_lo <= q_lo <= q_hi <= pin_hi
                      and pin_lo <= reference <= pin_hi),
        "seconds": time.perf_counter() - started,
    }


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    selected = K_SMOKE if args.smoke else K_FULL
    started = time.perf_counter()
    print("interval_cert_probe -- r465")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if args.smoke else "FULL")

    firewall_ok, forbidden = firewall_audit()
    check("firewall", firewall_ok,
          "sieve/fold/interval LA only" if firewall_ok else str(forbidden))
    node_started = time.perf_counter()
    gl_nodes, gl_weights, node_lemma = gl_nodes_enclosed(GL_N)
    check("GL-node-lemma",
          node_lemma["sign_ok"] and node_lemma["disjoint"]
          and node_lemma["contains_two"],
          "width %.3e; %.3fs" %
          (node_lemma["weight_sum_width"],
           time.perf_counter() - node_started))

    max_a = 2**max(selected)
    rows = prime_power_rows(max_a * max_a)
    results = []
    print("\n  k  atoms  S cap  qdag enclosure"
          "                                      width       sec chain")
    for k in selected:
        result = certify(k, rows, gl_nodes, gl_weights)
        results.append(result)
        print(" %2d %7d %3d %3d  [%s, %s]  %.3e  %6.3f  %2d/%2d" % (
            k, result["atoms"], result["m"], result["depth"],
            CERT_PINS[k][0], CERT_PINS[k][1], float(result["q_width"]),
            result["seconds"], result["chain_reach"], result["depth"]))
        check("k=%d certificate" % k, result["certified"],
              "raw=[%s,%s] ref=%.16f mu=%.6f/%.6f" % (
                  mp.nstr(result["q_raw_lo"], 17),
                  mp.nstr(result["q_raw_hi"], 17),
                  REFERENCE_Q[k], result["mu_previous"],
                  result["mu_full"]))

    check("all-reference-points-enclosed",
          all(result["reference_inside"] for result in results),
          "%d/%d r459/r463 points" % (len(results), len(results)))
    check("deterministic-sealed-pins",
          all(result["raw_inside_pin"] for result in results),
          "live outward enclosures inside decimal certificate hulls")
    check("finite-Rdagger-half",
          all(result["certified"] for result in results),
          "CERTIFIED(k=%d..%d), finite only" %
          (selected[0], selected[-1]))
    check("runtime-budget", time.perf_counter() - started < 2700,
          "%.3fs < 2700s" % (time.perf_counter() - started))

    failed = [name for name, ok in CHECKS if not ok]
    print("\nRESULT: %d/%d gates PASS (%.3fs)" %
          (len(CHECKS) - len(failed), len(CHECKS),
           time.perf_counter() - started))
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("INTERVAL CERT VERIFIED: CERTIFIED(k=%d..%d)" %
          (selected[0], selected[-1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
