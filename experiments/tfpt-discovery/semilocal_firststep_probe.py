#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""semilocal_firststep_probe -- r615  PRIME.SEMILOCAL.FIRSTSTEP.01

Experiments-only scout of the first prime step of the Weil form in
the multiplicative variable u = log x.  For real h supported in
[-L, L], g is the autocorrelation, ĥ(t) = ∫ h(u) e^{itu} du, and

  Q_L(h) = POLE(h) + ARCH(h) − PRIME(h)

with POLE = 2 F₊ F₋, F± = ∫ h e^{±u/2}, ARCH the v1017 x-space
kernel k(x)=e^{x/2}/sinh(x) plus c_L, and PRIME empty for
2L < log 2 and equal to w₂ g(log 2) for (log 2)/2 < L < (log 3)/2,
w₂ = 2 Λ(2) 2^{-1/2} = √2 log 2.

Constants are pinned by a Schwartz Gaussian identity
Z = POLE + ARCH − PRIME against the first 2000 on-line ordinates
(same assembly as the sealed r608 EF residual).  Compact-support
Ritz sections use copied v1017 formulae (not an import).

T8 reports variational (Ritz-from-above) convergence only; it is not a
lower bound.  FIRSTSTEP_CERTIFIABLE is defined but requires a rigorous
lower-bound certificate on λ*(L) and cannot fire here (r496 / Schur
cross-block ‖Q_12‖ ≉ 0).  T9 characterises the POLE+ARCH minimizer.

Claim boundary: finite-section arithmetic on a frozen L-grid.
Not a ledger row.  Not a paper claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.linalg import eigh as seigh  # noqa: E402
from scipy.special import roots_legendre, spherical_jn  # noqa: E402

HERE = Path(__file__).resolve().parent
ZEROS_CACHE = HERE / "verified_zeros_n7000.npy"

ROUND = 615
SEED = 615202609
CONTRACT = "PRIME.SEMILOCAL.FIRSTSTEP.01"
GAMMA1 = 14.134725141734695
LOG2 = math.log(2.0)
LOG3 = math.log(3.0)
HALF_LOG2 = 0.5 * LOG2
HALF_LOG3 = 0.5 * LOG3
W2 = math.sqrt(2.0) * LOG2
W3 = 2.0 * LOG3 / math.sqrt(3.0)
CLAIM_C = 2.1e-3
G0_ALPHA = 20.0
G0_REL = 1.0e-8
G1_REL = 1.0e-8
T1_REL = 5.0e-2
N_ZEROS_FULL = 2000
GRID_FULL = (
    0.25, 0.30, 0.33, 0.3465, 0.3467, 0.37,
    0.40, 0.43, 0.46, 0.49, 0.52, 0.549,
)
T7_L_FULL = (0.40, 0.46, 0.52)
T9_L_FULL = (0.40, 0.46, 0.52, 0.549)
T9_EDGE = 0.1
T9_Q_TOL = 1.0e-12
N_A_FULL = 160
N_B_FULL = 80
N_CONV_A_FULL = (20, 40, 80, 160)
N_CONV_B_FULL = (20, 40, 80)
N_T8_FULL = (40, 80, 160)
N_BIG_FULL = 240
N_OUTER_FULL = 96
GRID_SMOKE = (0.30, 0.3465, 0.3467, 0.40, 0.52)
T7_L_SMOKE = (0.40,)
T9_L_SMOKE = (0.40, 0.52)
N_A_SMOKE = 24
N_B_SMOKE = 16
N_CONV_A_SMOKE = (8, 16, 24)
N_CONV_B_SMOKE = (8, 16)
N_T8_SMOKE = (8, 16, 24)
N_BIG_SMOKE = 48
N_OUTER_SMOKE = 64
N_ZEROS_SMOKE = 200
BISECT_ITERS = 48
SCRAMBLE_K = 3
SLEPIAN_SLOPE = -2.0 * GAMMA1

SPEC = {
    "round": ROUND,
    "tag": "r615",
    "contract": CONTRACT,
    "grid": list(GRID_FULL),
    "half_log2": HALF_LOG2,
    "half_log3": HALF_LOG3,
    "w2": "sqrt(2)*log(2)",
    "w3": "2*log(3)/sqrt(3)",
    "g0_alpha": G0_ALPHA,
    "g0_rel": G0_REL,
    "g1_rel": G1_REL,
    "t1_rel": T1_REL,
    "n_zeros": N_ZEROS_FULL,
    "zeros_cache": "verified_zeros_n7000.npy[:2000]",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "n_a": N_A_FULL,
    "n_b": N_B_FULL,
    "n_conv_a": list(N_CONV_A_FULL),
    "n_conv_b": list(N_CONV_B_FULL),
    "n_t8": list(N_T8_FULL),
    "n_big": N_BIG_FULL,
    "n_outer": N_OUTER_FULL,
    "space_a": "legendre_P_n on [-L,L]",
    "space_b": "(1-(u/L)^2)^2 * P_n",
    "pole": "2*Fplus*Fminus",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "c_L": "int_0^{2L}(k-1/x)+log(4L)+euler+log(pi)",
    "prime": "w2*g(log 2) for 2L>log 2 else 0",
    "identity": "Q = POLE + ARCH - PRIME",
    "seed": SEED,
    "claim_c": CLAIM_C,
    "gamma1": GAMMA1,
    "slepian_pred": "4*sqrt(pi*c)*exp(-2c), c=L*gamma1",
    "t5_slope_window": "L<=(log2)/2 + 2e-4 (prime-free plus kink)",
    "t8": "variational_convergence_not_a_lower_bound",
    "certifiable_requires": "rigorous_lower_bound_on_lambda_star",
    "schur_R": "0.25/lambda_N for L>0.3466; implied |t|~exp(R)",
    "t9": "POLE+ARCH minimizer h1 on space (a); odd/edge/g(log2)",
    "t9_L": list(T9_L_FULL),
    "t9_edge": T9_EDGE,
    "t2": "lambda_a(0.30)>=2.1e-3; factor reported not gated",
    "claim_boundary": "experiments_only_not_a_ledger_claim",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-44s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def section(title: str) -> None:
    emit("")
    emit("=" * 74)
    emit(title)
    emit("=" * 74)


def fmt(value, digits: int = 16) -> str:
    if value is None:
        return "nan"
    if isinstance(value, (bool, np.bool_)):
        return "1" if value else "0"
    if isinstance(value, (int, np.integer)) and not isinstance(value, (bool, np.bool_)):
        return "%d" % int(value)
    number = float(value)
    if math.isnan(number):
        return "nan"
    if not math.isfinite(number):
        return "+inf" if number > 0.0 else "-inf"
    return "%+.*e" % (digits, number)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def load_zeros(n_use: int) -> np.ndarray:
    n_use = int(n_use)
    if ZEROS_CACHE.is_file():
        raw = np.load(str(ZEROS_CACHE))
        n_use = min(n_use, int(raw.shape[0]))
        return np.asarray(raw[:n_use], dtype=np.float64)
    mp.mp.dps = 15
    return np.asarray(
        [float(mp.zetazero(index).imag) for index in range(1, n_use + 1)],
        dtype=np.float64,
    )


def k_kernel(t_values) -> np.ndarray:
    """Re ψ(1/4+it/2) − log π.  Copied Stirling/recurrence from r608."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    y_val = 0.5 * t_arr
    x_val = np.full_like(t_arr, 0.25, dtype=np.float64)
    acc = np.zeros_like(t_arr)
    for _ in range(80):
        r2 = x_val * x_val + y_val * y_val
        need = r2 < 100.0
        if not np.any(need):
            break
        acc = np.where(need, acc - x_val / np.maximum(r2, 1e-300), acc)
        x_val = np.where(need, x_val + 1.0, x_val)
    r2 = x_val * x_val + y_val * y_val
    inv_re = x_val / r2
    inv_im = -y_val / r2
    log_re = 0.5 * np.log(r2)
    inv2_re = inv_re * inv_re - inv_im * inv_im
    inv2_im = 2.0 * inv_re * inv_im

    def mul(a_re, a_im, b_re, b_im):
        return a_re * b_re - a_im * b_im, a_re * b_im + a_im * b_re

    inv4_re, inv4_im = mul(inv2_re, inv2_im, inv2_re, inv2_im)
    inv6_re, inv6_im = mul(inv4_re, inv4_im, inv2_re, inv2_im)
    inv8_re, inv8_im = mul(inv4_re, inv4_im, inv4_re, inv4_im)
    inv10_re, _inv10_im = mul(inv8_re, inv8_im, inv2_re, inv2_im)
    psi_re = (
        log_re
        - 0.5 * inv_re
        - (1.0 / 12.0) * inv2_re
        + (1.0 / 120.0) * inv4_re
        - (1.0 / 252.0) * inv6_re
        + (1.0 / 240.0) * inv8_re
        - (1.0 / 132.0) * inv10_re
        + acc
    )
    return psi_re - math.log(math.pi)


def von_mangoldt_table(n_max: int) -> np.ndarray:
    lam = np.zeros(n_max + 1, dtype=np.float64)
    is_prime = np.ones(n_max + 1, dtype=bool)
    is_prime[:2] = False
    for prime in range(2, n_max + 1):
        if not is_prime[prime]:
            continue
        log_p = math.log(prime)
        power = prime
        while power <= n_max:
            lam[power] = log_p
            if power > n_max // prime:
                break
            power *= prime
        start = prime * prime
        if start > n_max:
            continue
        is_prime[start:n_max + 1:prime] = False
    return lam


def c_L_of(ell: float) -> float:
    """v1017 high_precision_constants, any L."""
    mp.mp.dps = 50
    length = mp.mpf(ell)
    span = 2 * length

    def k_mp(point):
        return mp.exp(point / 2) / mp.sinh(point)

    value = (
        mp.quad(lambda point: k_mp(point) - 1 / point, [0, span])
        + mp.log(4 * length)
        + mp.euler
        + mp.log(mp.pi)
    )
    return float(value)


def kernel_x(x_values):
    values = np.asarray(x_values, dtype=np.float64)
    out = np.empty_like(values)
    small = np.abs(values) < 1.0e-12
    out[small] = 0.5
    large = ~small
    xv = values[large]
    out[large] = np.exp(xv / 2.0) / np.sinh(xv)
    return out


def legendre_values(points, length: float, dimension: int) -> np.ndarray:
    values_x = np.asarray(points, dtype=np.float64)
    two_l = 2.0 * length
    result = np.empty((values_x.size, dimension), dtype=np.float64)
    result[:, 0] = 1.0 / math.sqrt(two_l)
    if dimension == 1:
        return result
    scaled = values_x / length
    result[:, 1] = math.sqrt(3.0 / two_l) * scaled
    previous = np.ones_like(scaled)
    current = scaled.copy()
    for degree in range(1, dimension - 1):
        following = (
            ((2 * degree + 1) * scaled * current - degree * previous)
            / (degree + 1)
        )
        result[:, degree + 1] = (
            math.sqrt((2 * degree + 3) / two_l) * following
        )
        previous, current = current, following
    return result


def damped_weight(points, length: float) -> np.ndarray:
    scaled = np.asarray(points, dtype=np.float64) / length
    weight = np.zeros_like(scaled)
    inside = np.abs(scaled) <= 1.0 + 1.0e-15
    loc = scaled[inside]
    weight[inside] = (1.0 - loc * loc) ** 2
    return weight


def basis_values(points, length: float, dimension: int, damped: bool) -> np.ndarray:
    values = legendre_values(points, length, dimension)
    if not damped:
        return values
    return damped_weight(points, length)[:, None] * values


def gram_matrix(length: float, dimension: int, damped: bool, n_inner: int) -> np.ndarray:
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, damped)
    gram = basis.T @ (scaled[:, None] * basis)
    return 0.5 * (gram + gram.T)


def pole_vectors(length: float, dimension: int, damped: bool, n_inner: int):
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, damped)
    cosh_vector = basis.T @ (scaled * np.cosh(points / 2.0))
    sinh_vector = basis.T @ (scaled * np.sinh(points / 2.0))
    return cosh_vector, sinh_vector


def overlap_matrix(
    length: float,
    shift: float,
    dimension: int,
    damped: bool,
    n_inner: int,
) -> np.ndarray:
    two_l = 2.0 * length
    if shift <= 0.0 or shift >= two_l - 1.0e-15:
        return np.zeros((dimension, dimension), dtype=np.float64)
    overlap_length = two_l - shift
    nodes, weights = roots_legendre(n_inner)
    points = -length + 0.5 * overlap_length * (nodes + 1.0)
    scaled = 0.5 * overlap_length * weights
    left = basis_values(points, length, dimension, damped)
    right = basis_values(points + shift, length, dimension, damped)
    forward = right.T @ (scaled[:, None] * left)
    return 0.5 * (forward + forward.T)


def arch_matrix(
    length: float,
    dimension: int,
    damped: bool,
    gram: np.ndarray,
    c_l: float,
    n_outer: int,
    n_inner: int,
) -> np.ndarray:
    two_l = 2.0 * length
    outer_nodes, outer_weights = roots_legendre(n_outer)
    distances = 0.5 * two_l * (outer_nodes + 1.0)
    distance_weights = 0.5 * two_l * outer_weights
    inner_nodes, inner_weights = roots_legendre(n_inner)
    kern = kernel_x(distances)
    difference = np.zeros((dimension, dimension), dtype=np.float64)
    for distance, weight_x, kern_x in zip(distances, distance_weights, kern):
        overlap_length = two_l - distance
        points = -length + 0.5 * overlap_length * (inner_nodes + 1.0)
        scaled = 0.5 * overlap_length * inner_weights
        left = basis_values(points, length, dimension, damped)
        right = basis_values(points + distance, length, dimension, damped)
        overlap = right.T @ (scaled[:, None] * left)
        symmetric = 0.5 * (overlap + overlap.T)
        difference += (weight_x * kern_x) * (gram - symmetric)
    return difference - c_l * gram


def pole_matrix(cosh_vector, sinh_vector) -> np.ndarray:
    return (
        2.0 * np.outer(cosh_vector, cosh_vector)
        - 2.0 * np.outer(sinh_vector, sinh_vector)
    )


def assemble_forms(
    length: float,
    dimension: int,
    damped: bool,
    c_l: float,
    n_outer: int,
    include_prime: bool,
    shift: float = LOG2,
    weight: float = W2,
) -> dict:
    n_inner = max(dimension + 8, 48)
    gram = (
        np.eye(dimension)
        if not damped
        else gram_matrix(length, dimension, True, n_inner)
    )
    arch = arch_matrix(
        length, dimension, damped, gram, c_l, n_outer, n_inner,
    )
    cosh_vector, sinh_vector = pole_vectors(
        length, dimension, damped, n_inner,
    )
    pole = pole_matrix(cosh_vector, sinh_vector)
    overlap = overlap_matrix(length, shift, dimension, damped, n_inner)
    free = 0.5 * ((arch + pole) + (arch + pole).T)
    prime = weight * overlap if include_prime and shift < 2.0 * length else (
        np.zeros((dimension, dimension), dtype=np.float64)
    )
    full = 0.5 * ((free - prime) + (free - prime).T)
    gram = 0.5 * (gram + gram.T)
    return {
        "gram": gram,
        "arch": arch,
        "pole": pole,
        "free": free,
        "overlap": overlap,
        "prime": prime,
        "full": full,
        "cosh": cosh_vector,
        "sinh": sinh_vector,
        "n_inner": n_inner,
    }


def min_rayleigh(quadratic, gram) -> tuple[float, np.ndarray]:
    quadratic = 0.5 * (quadratic + quadratic.T)
    gram = 0.5 * (gram + gram.T)
    identity = np.allclose(gram, np.eye(gram.shape[0]), atol=1.0e-10, rtol=0.0)
    if identity:
        values, vectors = np.linalg.eigh(quadratic)
        return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)
    values, vectors = seigh(
        quadratic, gram, subset_by_index=[0, 0], check_finite=False,
    )
    return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)


def rayleigh_of(quadratic, gram, coeff: np.ndarray) -> float:
    num = float(coeff @ quadratic @ coeff)
    den = float(coeff @ gram @ coeff)
    return num / den if abs(den) > 1.0e-30 else float("nan")


def damped_connection(n_max: int) -> np.ndarray:
    """(1-x^2)^2 P_n = sum_k a[n,k] P_k, k <= n+4."""
    width = n_max + 5
    order = max(n_max + 16, 48)
    nodes, weights = roots_legendre(order)
    legend = np.zeros((order, width), dtype=np.float64)
    legend[:, 0] = 1.0
    if width > 1:
        legend[:, 1] = nodes
    for degree in range(1, width - 1):
        legend[:, degree + 1] = (
            ((2 * degree + 1) * nodes * legend[:, degree]
             - degree * legend[:, degree - 1])
            / (degree + 1)
        )
    damp = (1.0 - nodes * nodes) ** 2
    coeff = np.zeros((n_max, width), dtype=np.float64)
    for index in range(n_max):
        field = damp * legend[:, index]
        for degree in range(min(index + 5, width)):
            coeff[index, degree] = (degree + 0.5) * float(
                np.dot(weights, field * legend[:, degree])
            )
    return coeff


def bessel_legendre_hat(length: float, t_values, n_max: int) -> np.ndarray:
    """ĥ of orthonormal P̃_n, shape (len(t), n_max), complex."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    argument = length * t_arr
    out = np.zeros((t_arr.size, n_max), dtype=np.complex128)
    for degree in range(n_max):
        scale = math.sqrt(2.0 * length * (2 * degree + 1))
        out[:, degree] = scale * ((1j) ** degree) * spherical_jn(degree, argument)
    return out


def bessel_damped_hat(
    length: float, t_values, n_max: int, connection: np.ndarray,
) -> np.ndarray:
    t_arr = np.asarray(t_values, dtype=np.float64)
    width = n_max + 5
    argument = length * t_arr
    bessel = [spherical_jn(degree, argument) for degree in range(width)]
    out = np.zeros((t_arr.size, n_max), dtype=np.complex128)
    for index in range(n_max):
        mix = connection[index, :width]
        combo = np.zeros(t_arr.size, dtype=np.complex128)
        for degree in range(width):
            amp = mix[degree]
            if abs(amp) <= 1.0e-18:
                continue
            combo += amp * ((1j) ** degree) * bessel[degree]
        out[:, index] = math.sqrt(2.0 * length * (2 * index + 1)) * combo
    return out


def hat_combination(basis_hat: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    return basis_hat @ coeff.astype(np.complex128)


def arch_tspace_from_hat(t_panels, hat_fn) -> float:
    total = 0.0
    for left, right, order in t_panels:
        nodes, weights = roots_legendre(order)
        t_values = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        scaled = 0.5 * (right - left) * weights
        hats = hat_fn(t_values)
        phi = np.abs(hats) ** 2
        total += float(np.dot(scaled, phi * k_kernel(t_values)))
    return total / math.pi


def slepian_prediction(length: float) -> float:
    bandwidth = length * GAMMA1
    if bandwidth <= 0.0:
        return float("nan")
    return 4.0 * math.sqrt(math.pi * bandwidth) * math.exp(-2.0 * bandwidth)


def fit_slope(x_values, y_values) -> float:
    xs = np.asarray(x_values, dtype=np.float64)
    ys = np.asarray(y_values, dtype=np.float64)
    if xs.size < 2:
        return float("nan")
    matrix = np.vstack((xs, np.ones_like(xs))).T
    slope, _intercept = np.linalg.lstsq(matrix, ys, rcond=None)[0]
    return float(slope)


def extrapolate_gap(values: list[float]) -> float:
    if len(values) < 2:
        return abs(values[-1]) if values else float("nan")
    last = abs(values[-1] - values[-2])
    if len(values) < 3:
        return last
    prev = abs(values[-2] - values[-3])
    if prev <= 1.0e-30:
        return last
    rho = last / prev
    if 0.0 < rho < 0.99:
        return last * rho / (1.0 - rho)
    return last


def monotone_from_above(values: list[float]) -> bool:
    if len(values) < 2:
        return True
    for left, right in zip(values, values[1:]):
        scale = max(1.0, abs(left), abs(right))
        if right > left + 1.0e-10 * scale:
            return False
    return True


def bisect_crossing(func, lo: float, hi: float, n_iter: int = BISECT_ITERS):
    f_lo = func(lo)
    f_hi = func(hi)
    if not (math.isfinite(f_lo) and math.isfinite(f_hi)):
        return float("nan"), f_lo, f_hi
    if f_lo == 0.0:
        return lo, f_lo, f_hi
    if f_hi == 0.0:
        return hi, f_lo, f_hi
    if f_lo * f_hi > 0.0:
        return float("nan"), f_lo, f_hi
    left, right = lo, hi
    f_left = f_lo
    for _ in range(n_iter):
        mid = 0.5 * (left + right)
        f_mid = func(mid)
        if f_left * f_mid <= 0.0:
            right = mid
        else:
            left = mid
            f_left = f_mid
    return 0.5 * (left + right), f_lo, f_hi


def gaussian_g0(zeros: np.ndarray) -> dict:
    alpha = G0_ALPHA
    mp.mp.dps = 40
    a_mp = mp.mpf(alpha)
    pole = float((4 * mp.pi / a_mp) * mp.e ** (1 / (4 * a_mp)))

    def kappa_mp(t_val):
        return mp.re(mp.digamma(mp.mpf("0.25") + mp.j * t_val / 2)) - mp.log(mp.pi)

    arch = float(
        (mp.mpf(1) / a_mp)
        * mp.quad(
            lambda t_val: mp.exp(-t_val * t_val / a_mp) * kappa_mp(t_val),
            [-mp.mpf(120), 0, mp.mpf(120)],
        )
    )
    n_max = 20000
    lam = von_mangoldt_table(n_max)
    g_pref = math.sqrt(math.pi / alpha)
    prime = 0.0
    for index in range(2, n_max + 1):
        if lam[index] == 0.0:
            continue
        log_n = math.log(index)
        g_val = g_pref * math.exp(-0.25 * alpha * log_n * log_n)
        prime += 2.0 * lam[index] / math.sqrt(index) * g_val
    phi = (2.0 * math.pi / alpha) * np.exp(-(zeros ** 2) / alpha)
    z_zeros = float(2.0 * np.sum(phi))
    z_src = pole + arch - prime
    scale = max(abs(z_zeros), abs(z_src), 1.0e-30)
    rel = abs(z_src - z_zeros) / scale
    term_scale = max(abs(pole), abs(arch), abs(prime), 1.0e-30)
    rel_term = abs(z_src - z_zeros) / term_scale
    return {
        "alpha": alpha,
        "pole": pole,
        "arch": arch,
        "prime": prime,
        "z_src": z_src,
        "z_zeros": z_zeros,
        "rel": rel,
        "rel_term": rel_term,
        "w2": W2,
        "n_primes": int(np.count_nonzero(lam)),
    }


def fraction_below_gamma1(hat_fn, n_quad: int = 128) -> float:
    nodes, weights = roots_legendre(n_quad)
    t_values = 0.5 * GAMMA1 * (nodes + 1.0)
    scaled = 0.5 * GAMMA1 * weights
    hats = hat_fn(t_values)
    return float(np.dot(scaled, np.abs(hats) ** 2) / math.pi)


def spectral_peak(hat_fn, t_max: float = 40.0, n_pts: int = 2001) -> tuple[float, float]:
    t_values = np.linspace(0.0, t_max, n_pts)
    power = np.abs(hat_fn(t_values)) ** 2
    index = int(np.argmax(power))
    return float(t_values[index]), float(power[index])


def zero_leakage(hat_fn, zeros: np.ndarray, t_tail_extra: float = 4000.0) -> dict:
    hats = hat_fn(zeros)
    discrete = float(2.0 * np.sum(np.abs(hats) ** 2))
    t_cut = float(zeros[-1]) if zeros.size else 1.0
    nodes, weights = roots_legendre(96)
    t_values = t_cut + 0.5 * t_tail_extra * (nodes + 1.0)
    scaled = 0.5 * t_tail_extra * weights
    tail_hats = hat_fn(t_values)
    log_term = np.log(np.maximum(t_values / (2.0 * math.pi), 1.0e-12))
    tail = float(
        2.0 * np.dot(scaled, (np.abs(tail_hats) ** 2) * log_term / (2.0 * math.pi))
    )
    return {"discrete": discrete, "tail": tail, "leakage": discrete + tail, "t_cut": t_cut}


def slepian_overlap(
    length: float,
    damped: bool,
    gram: np.ndarray,
    coeff: np.ndarray,
    connection,
    n_quad: int = 96,
) -> float:
    dimension = coeff.size
    nodes, weights = roots_legendre(n_quad)
    t_values = 0.5 * GAMMA1 * (nodes + 1.0)
    scaled = 0.5 * GAMMA1 * weights
    if damped:
        basis_hat = bessel_damped_hat(length, t_values, dimension, connection)
    else:
        basis_hat = bessel_legendre_hat(length, t_values, dimension)
    weight = np.sqrt(scaled / math.pi)
    mixed = weight[:, None] * basis_hat
    kernel = np.real(mixed.conj().T @ mixed)
    kernel = 0.5 * (kernel + kernel.T)
    _value, vector = min_rayleigh(-kernel, gram)
    psi = vector
    # both G-normalized by eigh
    inner = float(coeff @ gram @ psi)
    return inner * inner


def principal_mins(quadratic, gram, n_list: tuple[int, ...]) -> list[float]:
    out = []
    for dimension in n_list:
        qn = quadratic[:dimension, :dimension]
        gn = gram[:dimension, :dimension]
        value, _vec = min_rayleigh(qn, gn)
        out.append(value)
    return out


def characterize_h1(
    length: float,
    dimension: int,
    damped: bool,
    coeff: np.ndarray,
    forms: dict,
    n_nodes: int = 256,
) -> dict:
    """Parity / edge / pole split / g(log 2) of a unit vector in the trial space."""
    nodes, weights = roots_legendre(n_nodes)
    points = length * nodes
    scaled = length * weights
    samples = basis_values(points, length, dimension, damped) @ coeff
    flipped = samples[::-1]
    even = 0.5 * (samples + flipped)
    odd = 0.5 * (samples - flipped)
    nrm2 = float(np.dot(scaled, samples * samples))
    even_e = float(np.dot(scaled, even * even))
    odd_e = float(np.dot(scaled, odd * odd))
    denom = math.sqrt(max(nrm2, 1.0e-30))
    parity = math.sqrt(float(np.dot(scaled, (samples - flipped) ** 2))) / denom
    edge = np.abs(points) >= (length - T9_EDGE)
    edge_frac = float(np.dot(scaled[edge], samples[edge] ** 2)) / max(nrm2, 1.0e-30)
    f_cosh = float(coeff @ forms["cosh"])
    f_sinh = float(coeff @ forms["sinh"])
    cosh2 = f_cosh * f_cosh
    sinh2 = f_sinh * f_sinh
    pole = 2.0 * (cosh2 - sinh2)
    arch = float(coeff @ forms["arch"] @ coeff)
    g_log2 = float(coeff @ forms["overlap"] @ coeff)
    prime = W2 * g_log2 if (2.0 * length) > LOG2 + 1.0e-15 else 0.0
    q_val = pole + arch - prime
    return {
        "parity": parity,
        "even_e": even_e / max(nrm2, 1.0e-30),
        "odd_e": odd_e / max(nrm2, 1.0e-30),
        "edge_frac": edge_frac,
        "cosh2": cosh2,
        "sinh2": sinh2,
        "pole": pole,
        "arch": arch,
        "g_log2": g_log2,
        "prime": prime,
        "q": q_val,
        "mu": pole + arch,
        "nrm2": nrm2,
    }


def operator_norm_offblock(block: np.ndarray) -> float:
    if block.size == 0:
        return 0.0
    return float(np.linalg.norm(block, ord=2))


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()

    if smoke:
        grid = GRID_SMOKE
        n_a = N_A_SMOKE
        n_b = N_B_SMOKE
        n_conv_a = N_CONV_A_SMOKE
        n_conv_b = N_CONV_B_SMOKE
        n_t8 = N_T8_SMOKE
        n_big = N_BIG_SMOKE
        n_outer = N_OUTER_SMOKE
        n_zeros = N_ZEROS_SMOKE
        t7_grid = T7_L_SMOKE
        t9_grid = T9_L_SMOKE
        g1_vectors = 3
    else:
        grid = GRID_FULL
        n_a = N_A_FULL
        n_b = N_B_FULL
        n_conv_a = N_CONV_A_FULL
        n_conv_b = N_CONV_B_FULL
        n_t8 = N_T8_FULL
        n_big = N_BIG_FULL
        n_outer = N_OUTER_FULL
        n_zeros = N_ZEROS_FULL
        t7_grid = T7_L_FULL
        t9_grid = T9_L_FULL
        g1_vectors = 3

    emit("semilocal_firststep_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("w2 %s  w3 %s  half_log2 %s  half_log3 %s" % (
        fmt(W2, 16), fmt(W3, 16), fmt(HALF_LOG2, 16), fmt(HALF_LOG3, 16),
    ))
    emit("claim_boundary experiments_only_not_a_ledger_claim")

    zeros = load_zeros(n_zeros)
    emit("zeros n=%d gamma1=%s gammaN=%s source=%s" % (
        int(zeros.size), fmt(float(zeros[0]), 12), fmt(float(zeros[-1]), 12),
        "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
    ))

    connection_b = damped_connection(n_b)
    connection_g1 = damped_connection(max(n_b, 12))

    section("G0  GAUSSIAN EF PIN")
    g0 = gaussian_g0(zeros)
    emit(
        "  alpha=%s POLE=%s ARCH=%s PRIME=%s Z_src=%s Z_zeros=%s rel=%s rel_term=%s w2=%s"
        % (
            fmt(g0["alpha"], 4), fmt(g0["pole"], 12), fmt(g0["arch"], 12),
            fmt(g0["prime"], 12), fmt(g0["z_src"], 12), fmt(g0["z_zeros"], 12),
            fmt(g0["rel"], 6), fmt(g0["rel_term"], 6), fmt(g0["w2"], 12),
        )
    )
    g0_ok = check(
        "G0-EF-identity",
        g0["rel"] <= G0_REL,
        "rel=%s <= %s" % (fmt(g0["rel"], 6), fmt(G0_REL, 2)),
    )
    check(
        "G0-w2-pin",
        abs(g0["w2"] - W2) <= 1.0e-15,
        "w2=%s" % fmt(W2, 16),
    )

    c_l_map = {float(length): c_L_of(length) for length in grid}
    if 0.3 in c_l_map or any(abs(length - 0.3) < 1.0e-12 for length in grid):
        c03 = c_l_map[0.3] if 0.3 in c_l_map else c_L_of(0.3)
        check(
            "G0-cL-0.3",
            2.19240491113 < c03 < 2.19240491114,
            "c_L(0.3)=%s" % fmt(c03, 16),
        )

    section("G1  ARCH x-space vs t-space")
    g1_length = 0.30 if abs(min(grid, key=lambda value: abs(value - 0.30)) - 0.30) < 1.0e-12 else float(grid[0])
    if g1_length not in c_l_map:
        c_l_map[g1_length] = c_L_of(g1_length)
    g1_dim = min(12, n_b)
    g1_forms = assemble_forms(
        g1_length, g1_dim, True, c_l_map[g1_length], 320, False,
    )
    g1_conn = connection_g1 if g1_dim <= connection_g1.shape[0] else damped_connection(g1_dim)
    g1_ok_all = True
    g1_rows = []
    for index in range(g1_vectors):
        coeff = np.zeros(g1_dim, dtype=np.float64)
        coeff[min(2 * index, g1_dim - 1)] = 1.0
        norm = math.sqrt(float(coeff @ g1_forms["gram"] @ coeff))
        coeff = coeff / max(norm, 1.0e-30)
        arch_x = float(coeff @ g1_forms["arch"] @ coeff)
        pole_x = float(coeff @ g1_forms["pole"] @ coeff)

        def hat_fn(t_values, c=coeff.copy()):
            basis = bessel_damped_hat(g1_length, t_values, g1_dim, g1_conn)
            return hat_combination(basis, c)

        arch_t = arch_tspace_from_hat(
            (
                (0.0, 20.0, 128),
                (20.0, 80.0, 128),
                (80.0, 400.0, 160),
                (400.0, 2500.0, 128),
            ),
            hat_fn,
        )
        rel = abs(arch_x - arch_t) / max(abs(arch_t), abs(arch_x), 1.0e-30)
        g1_rows.append((index, arch_x, arch_t, rel, pole_x))
        emit(
            "  vec%d ARCH_x=%s ARCH_t=%s rel=%s POLE=%s"
            % (index, fmt(arch_x, 12), fmt(arch_t, 12), fmt(rel, 6), fmt(pole_x, 12))
        )
        ok = rel <= G1_REL
        g1_ok_all = g1_ok_all and ok
        check("G1-vec%d" % index, ok, "rel=%s" % fmt(rel, 6))

    section("RITZ  spaces (a) Legendre / (b) edge-damped")
    rows = []
    t1_ok_all = True
    t4_hi_ok = True
    overlap_lo = None
    overlap_hi = None
    frac_lo = None
    frac_hi = None
    peak_lo = None
    peak_hi = None

    for length in grid:
        c_l = c_l_map[length]
        prime_on = (2.0 * length) > LOG2 + 1.0e-15
        forms_a = assemble_forms(
            length, n_a, False, c_l, n_outer, prime_on,
        )
        forms_b = assemble_forms(
            length, n_b, True, c_l, n_outer, prime_on,
        )
        conv_a = principal_mins(forms_a["full"], forms_a["gram"], n_conv_a)
        conv_b = principal_mins(forms_b["full"], forms_b["gram"], n_conv_b)
        lam_a = conv_a[-1]
        lam_b, vec_b = min_rayleigh(forms_b["full"], forms_b["gram"])
        mu_b, _mu_vec = min_rayleigh(forms_b["free"], forms_b["gram"])
        mu_a, vec_mu_a = min_rayleigh(forms_a["free"], forms_a["gram"])
        pole_h = float(vec_b @ forms_b["pole"] @ vec_b)
        arch_h = float(vec_b @ forms_b["arch"] @ vec_b)
        prime_h = float(vec_b @ forms_b["prime"] @ vec_b)
        depth = max(abs(pole_h), abs(arch_h), abs(prime_h)) / max(abs(lam_b), 1.0e-30)

        def hat_b(t_values, c=vec_b.copy()):
            basis = bessel_damped_hat(length, t_values, n_b, connection_b)
            return hat_combination(basis, c)

        leak = zero_leakage(hat_b, zeros)
        t1_rel = abs(leak["leakage"] / lam_b - 1.0) if abs(lam_b) > 1.0e-30 else float("inf")
        t1_ok = t1_rel <= T1_REL
        t1_ok_all = t1_ok_all and t1_ok
        frac = fraction_below_gamma1(hat_b)
        peak_t, peak_p = spectral_peak(hat_b)
        overlap = slepian_overlap(
            length, True, forms_b["gram"], vec_b, connection_b,
        )
        pred = slepian_prediction(length)
        ratio = lam_b / pred if pred > 0.0 else float("nan")
        gap_a = extrapolate_gap(conv_a)
        var_g = gap_a / abs(lam_a) if abs(lam_a) > 1.0e-30 else float("inf")
        mono_a = monotone_from_above(conv_a)
        schur_r = (
            0.25 / abs(lam_a) if (length > 0.3466 and abs(lam_a) > 1.0e-30)
            else float("nan")
        )

        off_norms = []
        pole_out = []
        if n_big > max(n_t8):
            n_inner_big = max(n_big + 32, 96)
            shift_big = overlap_matrix(length, LOG2, n_big, False, n_inner_big)
            cosh_big, sinh_big = pole_vectors(length, n_big, False, n_inner_big)
            for dim in n_t8:
                if dim >= n_big:
                    off_norms.append(0.0)
                    pole_out.append(0.0)
                    continue
                off = shift_big[:dim, dim:]
                off_norms.append(operator_norm_offblock(off))
                full_plus = math.sqrt(float(np.dot(cosh_big, cosh_big)))
                full_minus = math.sqrt(float(np.dot(sinh_big, sinh_big)))
                out_plus = math.sqrt(float(np.dot(cosh_big[dim:], cosh_big[dim:])))
                out_minus = math.sqrt(float(np.dot(sinh_big[dim:], sinh_big[dim:])))
                pole_out.append(
                    0.5 * (
                        (out_plus / full_plus if full_plus > 0 else 0.0)
                        + (out_minus / full_minus if full_minus > 0 else 0.0)
                    )
                )
        else:
            off_norms = [float("nan")] * len(n_t8)
            pole_out = [float("nan")] * len(n_t8)

        row = {
            "L": length,
            "prime_on": prime_on,
            "lam_a": lam_a,
            "lam_b": lam_b,
            "mu_b": mu_b,
            "conv_a": conv_a,
            "conv_b": conv_b,
            "pole": pole_h,
            "arch": arch_h,
            "prime": prime_h,
            "depth": depth,
            "leakage": leak["leakage"],
            "leak_disc": leak["discrete"],
            "leak_tail": leak["tail"],
            "t1_rel": t1_rel,
            "t1_ok": t1_ok,
            "frac": frac,
            "peak_t": peak_t,
            "peak_p": peak_p,
            "overlap": overlap,
            "pred": pred,
            "ratio": ratio,
            "var_g": var_g,
            "schur_r": schur_r,
            "mono_a": mono_a,
            "off": off_norms,
            "pole_out": pole_out,
            "c_L": c_l,
            "mu_a": mu_a,
            "vec_mu_a": vec_mu_a,
            "forms_a": forms_a,
        }
        rows.append(row)
        if abs(length - 0.3465) < 1.0e-12:
            overlap_lo, frac_lo, peak_lo = overlap, frac, peak_t
        if abs(length - 0.3467) < 1.0e-12:
            overlap_hi, frac_hi, peak_hi = overlap, frac, peak_t
        if length >= 0.37 - 1.0e-12:
            if frac < 0.99 or overlap < 0.95:
                t4_hi_ok = False
        check(
            "T1-L%s" % fmt(length, 4),
            t1_ok,
            "rel=%s leak=%s lam=%s" % (
                fmt(t1_rel, 6), fmt(leak["leakage"], 12), fmt(lam_b, 12),
            ),
        )
        emit(
            "  L=%s prime=%d lam_a=%s lam_b=%s mu_b=%s POLE=%s ARCH=%s PRIME=%s D=%s"
            % (
                fmt(length, 6), int(prime_on), fmt(lam_a, 12), fmt(lam_b, 12),
                fmt(mu_b, 12), fmt(pole_h, 12), fmt(arch_h, 12),
                fmt(prime_h, 12), fmt(depth, 6),
            )
        )
        emit(
            "    T1 leak=%s disc=%s tail=%s rel=%s  T4 frac=%s peak_t=%s ov=%s"
            % (
                fmt(leak["leakage"], 12), fmt(leak["discrete"], 12),
                fmt(leak["tail"], 12), fmt(t1_rel, 6), fmt(frac, 12),
                fmt(peak_t, 8), fmt(overlap, 12),
            )
        )
        emit(
            "    T5 pred=%s ratio=%s  T8 varG=%s R=%s mono=%d conv_a=%s conv_b=%s"
            % (
                fmt(pred, 12), fmt(ratio, 6), fmt(var_g, 6), fmt(schur_r, 6),
                int(mono_a),
                ",".join(fmt(val, 8) for val in conv_a),
                ",".join(fmt(val, 8) for val in conv_b),
            )
        )
        emit(
            "    T8 offN=%s pole_out=%s c_L=%s"
            % (
                ",".join(fmt(val, 8) for val in off_norms),
                ",".join(fmt(val, 8) for val in pole_out),
                fmt(c_l, 12),
            )
        )

    section("T2  v1017 CONSISTENCY at L=0.30")
    row30 = next((row for row in rows if abs(row["L"] - 0.30) < 1.0e-12), None)
    if row30 is None:
        check("T2-present", False, "L=0.30 not on grid")
        t2_ok = False
        factor30 = float("nan")
        lam30 = float("nan")
    else:
        lam30 = row30["lam_a"]
        factor30 = lam30 / CLAIM_C
        t2_ok = check(
            "T2-ritz-from-above",
            lam30 >= CLAIM_C,
            "lam_a=%s >= %s" % (fmt(lam30, 12), fmt(CLAIM_C, 6)),
        )
        emit(
            "  lam_a(0.30)=%s  padded_floor=%s  factor_vs_floor=%s  "
            "(floor is 3x-tail padded, not the min eig; factor is reported)"
            % (fmt(lam30, 16), fmt(CLAIM_C, 6), fmt(factor30, 8))
        )

    section("T5  SLEPIAN LAW")
    fit_L = [row["L"] for row in rows if row["lam_b"] > 0.0]
    fit_log = [math.log(row["lam_b"]) for row in rows if row["lam_b"] > 0.0]
    slope = fit_slope(fit_L, fit_log)
    slope_rel = abs(slope - SLEPIAN_SLOPE) / abs(SLEPIAN_SLOPE) if fit_L else float("inf")
    window = [row for row in rows if row["L"] <= HALF_LOG2 + 2.0e-4 and row["lam_b"] > 0.0]
    slope_w = fit_slope(
        [row["L"] for row in window],
        [math.log(row["lam_b"]) for row in window],
    )
    slope_w_rel = (
        abs(slope_w - SLEPIAN_SLOPE) / abs(SLEPIAN_SLOPE) if window else float("inf")
    )
    ratio_ok_each = [
        0.1 <= row["ratio"] <= 10.0 if math.isfinite(row["ratio"]) else False
        for row in rows
    ]
    ratio_ok_window = [
        0.1 <= row["ratio"] <= 10.0 if math.isfinite(row["ratio"]) else False
        for row in window
    ]
    t5_ratio_all = all(ratio_ok_each) if ratio_ok_each else False
    t5_ratio_window = all(ratio_ok_window) if ratio_ok_window else False
    t5_slope_ok = slope_w_rel <= 0.20
    t5_pass = t5_ratio_window and t5_slope_ok
    emit(
        "  slope_full=%s rel_full=%s  slope_primefree=%s rel_w=%s  target=%s"
        % (
            fmt(slope, 8), fmt(slope_rel, 6), fmt(slope_w, 8),
            fmt(slope_w_rel, 6), fmt(SLEPIAN_SLOPE, 8),
        )
    )
    emit(
        "  ratio_all=%d/%d  ratio_window=%d/%d"
        % (
            sum(ratio_ok_each), len(ratio_ok_each),
            sum(ratio_ok_window), len(ratio_ok_window),
        )
    )
    for row in rows:
        emit(
            "    L=%s lam_b=%s pred=%s ratio=%s"
            % (fmt(row["L"], 6), fmt(row["lam_b"], 12), fmt(row["pred"], 12), fmt(row["ratio"], 6))
        )
    check("T5-slope-20pct", t5_slope_ok, "rel_w=%s" % fmt(slope_w_rel, 6))
    check(
        "T5-ratio-O1",
        t5_ratio_window,
        "window n_ok=%d/%d full=%d/%d" % (
            sum(ratio_ok_window), len(ratio_ok_window),
            sum(ratio_ok_each), len(ratio_ok_each),
        ),
    )

    section("T6  KINK at prime entry")
    row_lo = next((row for row in rows if abs(row["L"] - 0.3465) < 1.0e-12), None)
    row_hi = next((row for row in rows if abs(row["L"] - 0.3467) < 1.0e-12), None)
    if row_lo is None or row_hi is None:
        check("T6-grid", False, "missing 0.3465/0.3467")
        t6_char_stable = False
        jump_lam = float("nan")
        jump_free = float("nan")
    else:
        jump_lam = row_hi["lam_b"] - row_lo["lam_b"]
        jump_free = row_hi["lam_b"] - row_hi["mu_b"]
        emit(
            "  lam(0.3465)=%s lam(0.3467)=%s mu(0.3467)=%s jump_lam=%s lam-mu=%s"
            % (
                fmt(row_lo["lam_b"], 12), fmt(row_hi["lam_b"], 12),
                fmt(row_hi["mu_b"], 12), fmt(jump_lam, 12), fmt(jump_free, 12),
            )
        )
        emit(
            "  ov(0.3465)=%s ov(0.3467)=%s frac_lo=%s frac_hi=%s peak_lo=%s peak_hi=%s"
            % (
                fmt(overlap_lo, 12), fmt(overlap_hi, 12),
                fmt(frac_lo, 12), fmt(frac_hi, 12),
                fmt(peak_lo, 8), fmt(peak_hi, 8),
            )
        )
        ov_delta = abs((overlap_hi or 0.0) - (overlap_lo or 0.0))
        t6_char_stable = ov_delta <= 1.0e-2
        check("T6-overlap-stable", t6_char_stable, "d_ov=%s" % fmt(ov_delta, 6))
        for row in rows:
            if row["L"] > HALF_LOG2:
                emit(
                    "    fict L=%s lam_b=%s mu_b=%s d=%s"
                    % (
                        fmt(row["L"], 6), fmt(row["lam_b"], 12),
                        fmt(row["mu_b"], 12), fmt(row["lam_b"] - row["mu_b"], 12),
                    )
                )

    frac_drop = False
    peak_move = False
    ov_drop = False
    if row_lo is not None and row_hi is not None:
        frac_drop = (frac_hi or 1.0) < 0.9 or ((frac_lo or 1.0) - (frac_hi or 1.0) > 0.1)
        peak_move = abs((peak_hi or 0.0) - (peak_lo or 0.0)) > 1.0
        ov_drop = ((overlap_lo or 1.0) - (overlap_hi or 1.0)) > 0.1
    character_change = frac_drop or peak_move or ov_drop
    emit(
        "  character_change=%d frac_drop=%d peak_move=%d ov_drop=%d"
        % (int(character_change), int(frac_drop), int(peak_move), int(ov_drop))
    )

    section("T7  PINNING / TWO-KEY")
    rng = np.random.RandomState(SEED)
    t7_rows = []
    for length in t7_grid:
        c_l = c_l_map.get(length, c_L_of(length))
        forms = assemble_forms(length, n_b, True, c_l, n_outer, True)
        gram = forms["gram"]
        free = forms["free"]
        overlap0 = forms["overlap"]

        def lam_of_weight(weight: float) -> float:
            quadratic = free - weight * overlap0
            value, _vec = min_rayleigh(quadratic, gram)
            return value

        lam_w2 = lam_of_weight(W2)
        # increase w2
        if lam_w2 <= 0.0:
            delta_crit = 0.0
        else:
            weight_hi = W2
            lam_hi = lam_w2
            found = False
            for _scale in range(1, 25):
                weight_hi = W2 * (1.5 ** _scale)
                lam_hi = lam_of_weight(weight_hi)
                if lam_hi <= 0.0:
                    found = True
                    break
            if found:
                def f_delta(delta: float) -> float:
                    return lam_of_weight(W2 * (1.0 + delta))

                delta_hi = weight_hi / W2 - 1.0
                delta_crit, _, _ = bisect_crossing(f_delta, 0.0, delta_hi)
            else:
                delta_crit = float("inf")

        def lam_of_shift(shift: float) -> float:
            n_inner = forms["n_inner"]
            overlap = overlap_matrix(length, shift, n_b, True, n_inner)
            quadratic = free - W2 * overlap
            value, _vec = min_rayleigh(quadratic, gram)
            return value

        two_l = 2.0 * length
        eps_plus, _, _ = bisect_crossing(
            lam_of_shift, LOG2, max(LOG2 + 1.0e-8, two_l - 1.0e-8),
        )
        if math.isfinite(eps_plus):
            eps_plus = eps_plus - LOG2
        eps_minus, _, _ = bisect_crossing(
            lam_of_shift, min(LOG2 - 1.0e-8, 1.0e-8), LOG2,
        )
        if math.isfinite(eps_minus):
            eps_minus = eps_minus - LOG2

        # WPERM: weight of prime 3 at position log 2
        lam_wperm = lam_of_weight(W3)
        positions = rng.uniform(0.60, two_l, size=SCRAMBLE_K)
        scramble = []
        for pos in positions:
            n_inner = forms["n_inner"]
            overlap = overlap_matrix(length, float(pos), n_b, True, n_inner)
            quadratic = free - W2 * overlap
            value, _vec = min_rayleigh(quadratic, gram)
            scramble.append(float(value))
        row_match = next((row for row in rows if abs(row["L"] - length) < 1.0e-12), None)
        leak_over_prime = float("nan")
        if row_match is not None and abs(row_match["prime"]) > 1.0e-30:
            leak_over_prime = row_match["leakage"] / abs(row_match["prime"])
        t7_rows.append({
            "L": length,
            "lam": lam_w2,
            "delta": delta_crit,
            "eps_plus": eps_plus,
            "eps_minus": eps_minus,
            "wperm": lam_wperm,
            "scramble": scramble,
            "positions": [float(pos) for pos in positions],
            "leak_over_prime": leak_over_prime,
        })
        emit(
            "  L=%s lam=%s d_crit=%s eps+=%s eps-=%s WPERM=%s leak/|PRIME|=%s"
            % (
                fmt(length, 6), fmt(lam_w2, 12), fmt(delta_crit, 8),
                fmt(eps_plus, 8), fmt(eps_minus, 8), fmt(lam_wperm, 12),
                fmt(leak_over_prime, 6),
            )
        )
        emit(
            "    SCRAMBLE pos=%s lam=%s"
            % (
                ",".join(fmt(pos, 8) for pos in positions),
                ",".join(fmt(val, 12) for val in scramble),
            )
        )

    section("T8  VARIATIONAL CONVERGENCE (not a lower bound)")
    emit(
        "  Ritz e_N/lam is variational convergence from above.  "
        "It is not a certificate.  FIRSTSTEP_CERTIFIABLE requires a "
        "rigorous lower bound on lambda*(L); none is implemented."
    )
    emit(
        "  Schur route would need lambda_min(Q_22) >= ||Q_12||^2 / lam* "
        "with ||Q_12||~0.5 so R := 0.25/lam*_N.  ARCH grows like log|t|, "
        "implied |t|~exp(R) is infeasible."
    )
    for row in rows:
        schur_r = row["schur_r"]
        log10_t = (
            schur_r / math.log(10.0) if math.isfinite(schur_r) else float("nan")
        )
        emit(
            "  L=%s eN=%s varG=%s mono=%d off=%s R=%s implied_|t|~10^%s"
            % (
                fmt(row["L"], 6),
                fmt(extrapolate_gap(row["conv_a"]), 12),
                fmt(row["var_g"], 6),
                int(row["mono_a"]),
                ",".join(fmt(val, 8) for val in row["off"]),
                fmt(schur_r, 6),
                fmt(log10_t, 4),
            )
        )
    emit("  CERTIFIABLE held as enum; cannot fire without a lower-bound scheme")

    section("T9  ODD/EDGE  POLE+ARCH MINIMIZER h1 (space a)")
    t9_ok_all = True
    t9_rows = []
    for length in t9_grid:
        row = next((item for item in rows if abs(item["L"] - length) < 1.0e-12), None)
        if row is None:
            t9_ok_all = False
            check("T9-L%s" % fmt(length, 4), False, "L not on grid")
            continue
        profile = characterize_h1(
            length, n_a, False, row["vec_mu_a"], row["forms_a"],
        )
        q_ok = profile["q"] >= row["lam_a"] - T9_Q_TOL
        t9_ok_all = t9_ok_all and q_ok
        t9_rows.append((length, profile, row["lam_a"], q_ok))
        emit(
            "  L=%s mu_a=%s parity||h-h(-)||/||h||=%s even_e=%s odd_e=%s edge=%s"
            % (
                fmt(length, 6), fmt(profile["mu"], 12), fmt(profile["parity"], 8),
                fmt(profile["even_e"], 8), fmt(profile["odd_e"], 8),
                fmt(profile["edge_frac"], 8),
            )
        )
        emit(
            "    <cosh>^2=%s <sinh>^2=%s POLE=%s ARCH=%s g(log2)=%s PRIME=%s"
            % (
                fmt(profile["cosh2"], 12), fmt(profile["sinh2"], 12),
                fmt(profile["pole"], 12), fmt(profile["arch"], 12),
                fmt(profile["g_log2"], 12), fmt(profile["prime"], 12),
            )
        )
        emit(
            "    Q(h1)=%s lam_a=%s restore=-w2*g=%s Q>=lam=%d"
            % (
                fmt(profile["q"], 12), fmt(row["lam_a"], 12),
                fmt(-W2 * profile["g_log2"], 12), int(q_ok),
            )
        )
    check(
        "T9-Q-h1-ge-lam",
        t9_ok_all,
        "Q(h1) >= lam_a - %s on %d L" % (fmt(T9_Q_TOL, 2), len(t9_grid)),
    )

    section("VERDICT")
    t4_controlled = t4_hi_ok
    for row in rows:
        if row["L"] >= 0.37 - 1.0e-12:
            emit(
                "  T4 L=%s frac=%s ov=%s peak=%s"
                % (fmt(row["L"], 6), fmt(row["frac"], 12), fmt(row["overlap"], 12), fmt(row["peak_t"], 8))
            )
    check("T1-all-L", t1_ok_all, "n=%d" % len(rows))
    check("T4-slepian-shape", t4_controlled, "frac>=0.99 and ov>=0.95 for L>=0.37")
    check("T5-law", t5_pass, "slope_ok=%d ratio_ok=%d" % (int(t5_slope_ok), int(t5_ratio_window)))

    emit(
        "  FIRSTSTEP_CERTIFIABLE requires a rigorous lower bound on "
        "lambda*(L), not Ritz-from-above / varG.  No such certificate "
        "is implemented; the enum is defined and cannot fire."
    )
    if not t1_ok_all:
        verdict = "INCONCLUSIVE"
        why = "T1 leakage identity failed on at least one L"
    elif character_change:
        verdict = "FIRSTSTEP_ARITHMETIC_EXTREMAL"
        why = "h0 character changes at prime entry"
    elif t1_ok_all and t4_controlled and t5_pass and t6_char_stable:
        verdict = "FIRSTSTEP_LEAKAGE_CONTROLLED"
        why = "T1/T4/T5/T6 held; no lower-bound certificate so not CERTIFIABLE"
    else:
        verdict = "INCONCLUSIVE"
        why = "T1 held but T4/T5/T6 did not meet the controlled-leakage pattern"

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r615 first-step Weil Ritz scout (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
