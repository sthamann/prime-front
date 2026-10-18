#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""support_relay_census_probe -- r619  PRIME.SUPPORT.RELAY.CENSUS.01

Experiments-only census of successive prime-power support events of
the Weil form on windows [-L, L].  Copied (not imported) from the
sealed r615 probe: Q = POLE + ARCH − PRIME, v1017 x-space kernel,
w_q = 2 Λ(q) q^{-1/2}, G0/G1 calibration, zero-side leakage.

For q_1=2 < q_2=3 < … ≤ 32 (Λ(q)>0), L_j = (1/2) log q_j and
L ∈ [L_j, L_{j+1}) the form is exactly

  Q_j(L) = POLE + ARCH − Σ_{r≤j} w_{q_r} g_h(log q_r)

with g_h the autocorrelation.  Trial space: edge-damped Legendre
(1−(u/L)^2)^3 P_n, N≤80.  λ*(L) is reported two ways: (a) Ritz of
the x-space form (cancellation depth D); (b) zero-side
Σ_γ |f̂(γ)|^2 + tail via the sample matrix F[k,i]=f̂_i(γ_k), with
λ*_disc = 2 σ_min(F_white)^2 to account for ±γ (matches r615 T1).

ĥ_H(ρ) = f̂(ρ) f̂(1−ρ̄)*  for H = f ⋆ f̃.  On the line this is |f̂(γ)|^2.
An off-line quadruple {β±iγ, (1−β)±iγ} contributes
4 Re[ f̂(1/2+σ+iγ) f̂(1/2−σ+iγ)* ] to the full spectral sum
(σ=β−1/2).  Fence: window positivity on the scanned L is
RH-consistent; no RH claim.

Claim boundary: finite-section arithmetic.  Not a ledger row.
Not a paper claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.linalg import eigh as seigh  # noqa: E402
from scipy.linalg import svdvals  # noqa: E402
from scipy.special import roots_legendre, spherical_jn  # noqa: E402

HERE = Path(__file__).resolve().parent
ZEROS_CACHE = HERE / "verified_zeros_n7000.npy"

ROUND = 619
SEED = 619202609
CONTRACT = "PRIME.SUPPORT.RELAY.CENSUS.01"
GAMMA1 = 14.134725141734695
LOG2 = math.log(2.0)
W2 = math.sqrt(2.0) * LOG2
G0_ALPHA = 20.0
G0_REL = 1.0e-8
G1_REL = 1.0e-8
AB_REL = 5.0e-2
D_UNREL = 1.0e12
SVD_COND = 1.0e-8
T9_EDGE = 0.1
R615_SLOPE = -44.8
SLEPIAN_SLOPE = -2.0 * GAMMA1
DAMP_POWER = 3
CROSS_TOL = 1.0e-4
CROSS_POS = 1.0e-8
CROSS_NEG = -1.0e-8
BISECT_ITERS = 24
Q_MAX_FULL = 32
Q_MAX_SMOKE = 8
N_FULL = 80
N_SMOKE = 40
N_CROSS = 40
N_C6_FULL = 80
N_C6_SMOKE = 40
N_ZEROS_FULL = 5000
N_ZEROS_SMOKE = 1000
N_OUTER_FULL = 80
N_OUTER_SMOKE = 48
N_OUTER_G1 = 320
N_CTRL = 32
C6_L_LO = 0.25
C6_L_HI = 3.0
C6_STEP_FULL = 0.05
C6_STEP_SMOKE = 0.10
C6_PAIRS = ((0.6, 20.0), (0.75, 20.0), (0.6, 50.0), (0.9, 20.0))
EXT_PAD = 0.5

SPEC = {
    "round": ROUND,
    "tag": "r619",
    "contract": CONTRACT,
    "q_max": Q_MAX_FULL,
    "events": "prime_powers_q_le_32_Lambda_gt_0",
    "L_j": "0.5*log(q_j)",
    "w_q": "2*Lambda(q)*q**(-1/2)",
    "w2": "sqrt(2)*log(2)",
    "identity": "Q=POLE+ARCH-PRIME",
    "pole": "2*Fplus*Fminus",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "c_L": "int_0^{2L}(k-1/x)+log(4L)+euler+log(pi)",
    "space": "(1-(u/L)^2)^3 * P_n",
    "damp_power": DAMP_POWER,
    "n": N_FULL,
    "n_zeros": N_ZEROS_FULL,
    "zeros_cache": "verified_zeros_n7000.npy (recompute if absent; no new npy)",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "lambda_a": "Ritz Q_j in damped space; UNRELIABLE if D>1e12",
    "lambda_b": "2*sigma_min(F_white)^2 + tail, F[k,i]=hat_i(gamma_k)",
    "factor2": "plus/minus gamma; matches r615 T1 discrete=2*sum |hat|^2",
    "ab_rel": AB_REL,
    "g0_alpha": G0_ALPHA,
    "g0_rel": G0_REL,
    "g1_rel": G1_REL,
    "n_outer": N_OUTER_FULL,
    "n_c6": N_C6_FULL,
    "n_c6_note": "capped at 80; N=120 Gram cond ~1e16 makes online form indefinite at L=0.25",
    "c6_pairs": [list(pair) for pair in C6_PAIRS],
    "c6_scan": [C6_L_LO, C6_L_HI, C6_STEP_FULL],
    "hat_H": "fhat(rho)*conj(fhat(1-conj(rho)))",
    "offline": "4*Re[F(sigma,g)*conj(F(-sigma,g))] for the quadruple",
    "seed": SEED,
    "scramble": "uniform(log2, log q_max), same weights",
    "wperm": "permutation of weights, same positions",
    "epstein": "keep 2^k only",
    "cross_tol": CROSS_TOL,
    "cross_floor": [CROSS_POS, CROSS_NEG],
    "slepian": SLEPIAN_SLOPE,
    "r615_slope": R615_SLOPE,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": "Window positivity for the scanned L is RH-consistent; no RH claim.",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
_CL_CACHE: dict[float, float] = {}


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
    """Re ψ(1/4+it/2) − log π.  Copied Stirling/recurrence from r608/r615."""
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


def c_L_mp(ell: float) -> float:
    mp.mp.dps = 40
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


def c_L_numpy(ell: float, n_quad: int = 256) -> float:
    nodes, weights = roots_legendre(n_quad)
    span = 2.0 * ell
    x_val = 0.5 * span * (nodes + 1.0)
    scaled = 0.5 * span * weights
    kern = np.exp(x_val / 2.0) / np.sinh(x_val)
    integrand = kern - 1.0 / x_val
    return float(np.dot(scaled, integrand)) + math.log(4.0 * ell) + float(
        np.euler_gamma
    ) + math.log(math.pi)


def c_L_of(ell: float) -> float:
    key = round(float(ell), 12)
    cached = _CL_CACHE.get(key)
    if cached is not None:
        return cached
    value = c_L_numpy(float(ell))
    _CL_CACHE[key] = value
    return value


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
        result[:, degree + 1] = math.sqrt((2 * degree + 3) / two_l) * following
        previous, current = current, following
    return result


def damped_weight(points, length: float) -> np.ndarray:
    scaled = np.asarray(points, dtype=np.float64) / length
    weight = np.zeros_like(scaled)
    inside = np.abs(scaled) <= 1.0 + 1.0e-15
    loc = scaled[inside]
    weight[inside] = (1.0 - loc * loc) ** DAMP_POWER
    return weight


def basis_values(points, length: float, dimension: int) -> np.ndarray:
    values = legendre_values(points, length, dimension)
    return damped_weight(points, length)[:, None] * values


def gram_matrix(length: float, dimension: int, n_inner: int) -> np.ndarray:
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension)
    gram = basis.T @ (scaled[:, None] * basis)
    return 0.5 * (gram + gram.T)


def pole_vectors(length: float, dimension: int, n_inner: int):
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension)
    cosh_vector = basis.T @ (scaled * np.cosh(points / 2.0))
    sinh_vector = basis.T @ (scaled * np.sinh(points / 2.0))
    return cosh_vector, sinh_vector


def overlap_matrix(
    length: float,
    shift: float,
    dimension: int,
    n_inner: int,
) -> np.ndarray:
    two_l = 2.0 * length
    if shift <= 0.0 or shift >= two_l - 1.0e-15:
        return np.zeros((dimension, dimension), dtype=np.float64)
    overlap_length = two_l - shift
    nodes, weights = roots_legendre(n_inner)
    points = -length + 0.5 * overlap_length * (nodes + 1.0)
    scaled = 0.5 * overlap_length * weights
    left = basis_values(points, length, dimension)
    right = basis_values(points + shift, length, dimension)
    forward = right.T @ (scaled[:, None] * left)
    return 0.5 * (forward + forward.T)


def arch_matrix(
    length: float,
    dimension: int,
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
        left = basis_values(points, length, dimension)
        right = basis_values(points + distance, length, dimension)
        overlap = right.T @ (scaled[:, None] * left)
        symmetric = 0.5 * (overlap + overlap.T)
        difference += (weight_x * kern_x) * (gram - symmetric)
    return difference - c_l * gram


def pole_matrix(cosh_vector, sinh_vector) -> np.ndarray:
    return (
        2.0 * np.outer(cosh_vector, cosh_vector)
        - 2.0 * np.outer(sinh_vector, sinh_vector)
    )


def n_inner_of(dimension: int) -> int:
    return max(2 * dimension + 8, 64)


def min_rayleigh(quadratic, gram) -> tuple[float, np.ndarray]:
    quadratic = 0.5 * (quadratic + quadratic.T)
    gram = 0.5 * (gram + gram.T)
    dim = gram.shape[0]
    ridge = 1.0e-14 * (np.trace(gram) / max(dim, 1) + 1.0e-30)
    gram = gram + ridge * np.eye(dim)
    try:
        values, vectors = seigh(
            quadratic, gram, subset_by_index=[0, 0], check_finite=False,
        )
        return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)
    except Exception:
        values, vectors = np.linalg.eigh(quadratic)
        return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)


def damped_connection(n_max: int) -> np.ndarray:
    """(1-x^2)^3 P_n = sum_k a[n,k] P_k, k <= n+6."""
    extra = 2 * DAMP_POWER
    width = n_max + extra + 1
    order = max(2 * width + 8, 64)
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
    damp = (1.0 - nodes * nodes) ** DAMP_POWER
    coeff = np.zeros((n_max, width), dtype=np.float64)
    for index in range(n_max):
        field = damp * legend[:, index]
        for degree in range(min(index + extra + 1, width)):
            coeff[index, degree] = (degree + 0.5) * float(
                np.dot(weights, field * legend[:, degree])
            )
    return coeff


def bessel_damped_hat(
    length: float, t_values, n_max: int, connection: np.ndarray,
) -> np.ndarray:
    t_arr = np.real(np.asarray(t_values, dtype=np.float64))
    extra = 2 * DAMP_POWER
    width = n_max + extra + 1
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


def basis_hat_complex(
    length: float, t_values, dimension: int, n_quad: int | None = None,
) -> np.ndarray:
    t_arr = np.atleast_1d(np.asarray(t_values, dtype=np.complex128))
    t_scale = float(np.max(np.abs(t_arr))) if t_arr.size else 1.0
    n_quad = n_quad or max(8 * dimension, int(2.0 * length * t_scale) + 96, 192)
    n_quad = min(n_quad, 2048)
    nodes, weights = roots_legendre(n_quad)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension)
    phase = np.exp(1j * np.outer(t_arr, points))
    return (phase * scaled) @ basis


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
    }


def fit_slope(x_values, y_values) -> float:
    xs = np.asarray(x_values, dtype=np.float64)
    ys = np.asarray(y_values, dtype=np.float64)
    mask = np.isfinite(xs) & np.isfinite(ys)
    xs, ys = xs[mask], ys[mask]
    if xs.size < 2:
        return float("nan")
    matrix = np.vstack((xs, np.ones_like(xs))).T
    slope, _intercept = np.linalg.lstsq(matrix, ys, rcond=None)[0]
    return float(slope)


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


def prime_powers_upto(q_max: int):
    cap = max(q_max * 2, 64)
    lam = von_mangoldt_table(cap)
    qs = [index for index in range(2, q_max + 1) if lam[index] > 0.0]
    q_next = q_max + 1
    while q_next < lam.size and lam[q_next] == 0.0:
        q_next += 1
    logqs = np.array([math.log(q_val) for q_val in qs], dtype=np.float64)
    weights = np.array(
        [2.0 * lam[q_val] / math.sqrt(q_val) for q_val in qs], dtype=np.float64,
    )
    ells = 0.5 * logqs
    return qs, logqs, weights, ells, int(q_next), lam


def interval_grid(left: float, right: float) -> np.ndarray:
    gap = right - left
    if gap <= 0.0:
        return np.array([left], dtype=np.float64)
    if gap < 0.020:
        count = 3
    elif gap < 0.050:
        count = 5
    else:
        count = 8
    return np.linspace(left, right, count)


def n_active(length: float, logqs: np.ndarray) -> int:
    two_l = 2.0 * length
    return int(np.sum(logqs < two_l - 1.0e-15))


def tail_matrix(
    length: float,
    dimension: int,
    connection: np.ndarray,
    t_cut: float,
    t_extra: float = 2000.0,
    n_quad: int = 48,
) -> np.ndarray:
    nodes, weights = roots_legendre(n_quad)
    t_values = t_cut + 0.5 * t_extra * (nodes + 1.0)
    scaled = 0.5 * t_extra * weights
    hats = bessel_damped_hat(length, t_values, dimension, connection)
    dens = np.log(np.maximum(t_values / (2.0 * math.pi), 1.0e-12)) / (2.0 * math.pi)
    amp = np.sqrt(np.maximum(2.0 * scaled * dens, 0.0))
    mixed = amp[:, None] * hats
    tail = np.real(mixed.conj().T @ mixed)
    return 0.5 * (tail + tail.T)


def zero_side_min(
    length: float,
    dimension: int,
    connection: np.ndarray,
    zeros: np.ndarray,
    gram: np.ndarray,
) -> dict:
    hats = bessel_damped_hat(length, zeros, dimension, connection)
    gram_h = 2.0 * np.real(hats.conj().T @ hats)
    gram_h = 0.5 * (gram_h + gram_h.T)
    tail = tail_matrix(length, dimension, connection, float(zeros[-1]))
    pencil = gram_h + tail
    lam, vec = min_rayleigh(pencil, gram)
    denom = float(vec @ gram @ vec)
    tail_at = float(vec @ tail @ vec) / max(denom, 1.0e-30)
    disc_at = float(vec @ gram_h @ vec) / max(denom, 1.0e-30)
    smin = float("nan")
    smax = float("nan")
    lam_svd = float("nan")
    try:
        chol = np.linalg.cholesky(
            0.5 * (gram + gram.T) + 1.0e-14 * np.eye(dimension)
        )
        white = np.linalg.solve(chol, hats.T).T
        sigma = svdvals(white)
        smin = float(sigma[-1])
        smax = float(sigma[0])
        lam_svd = 2.0 * smin * smin
    except np.linalg.LinAlgError:
        pass
    cond = (
        smin / smax if (math.isfinite(smin) and math.isfinite(smax) and smax > 0.0)
        else float("nan")
    )
    return {
        "lam": lam,
        "vec": vec,
        "tail": tail_at,
        "disc": disc_at,
        "smin": smin,
        "smax": smax,
        "cond": cond,
        "lam_svd": lam_svd,
        "svd_ok": bool(math.isfinite(cond) and cond >= SVD_COND),
        "hats": hats,
        "gram_h": gram_h,
        "tail_mat": tail,
    }


def offline_matrix(v_plus: np.ndarray, v_minus: np.ndarray) -> np.ndarray:
    """Quadratic form 4 Re[(v+·c) conj(v-·c)] for real c."""
    plus = np.asarray(v_plus, dtype=np.complex128).ravel()
    minus = np.asarray(v_minus, dtype=np.complex128).ravel()
    real_p, imag_p = np.real(plus), np.imag(plus)
    real_m, imag_m = np.real(minus), np.imag(minus)
    matrix = np.outer(real_p, real_m) + np.outer(imag_p, imag_m)
    matrix = 0.5 * (matrix + matrix.T)
    return 4.0 * matrix


def characterize(
    length: float,
    dimension: int,
    coeff: np.ndarray,
    log_q: float,
    n_nodes: int = 512,
) -> dict:
    nodes, weights = roots_legendre(n_nodes)
    points = length * nodes
    scaled = length * weights
    samples = basis_values(points, length, dimension) @ coeff
    flipped = samples[::-1]
    even = 0.5 * (samples + flipped)
    odd = 0.5 * (samples - flipped)
    nrm2 = float(np.dot(scaled, samples * samples))
    even_e = float(np.dot(scaled, even * even)) / max(nrm2, 1.0e-30)
    odd_e = float(np.dot(scaled, odd * odd)) / max(nrm2, 1.0e-30)
    edge = np.abs(points) >= (length - T9_EDGE)
    edge_frac = float(np.dot(scaled[edge], samples[edge] ** 2)) / max(nrm2, 1.0e-30)
    inner_cut = log_q - length
    inner = np.abs(points) < inner_cut
    inner_mass = float(np.dot(scaled[inner], samples[inner] ** 2)) / max(
        nrm2, 1.0e-30,
    )
    left = log_q - length
    right = length
    overlap_len = right - left
    plus_e = 0.0
    minus_e = 0.0
    if overlap_len > 1.0e-14:
        loc_nodes, loc_w = roots_legendre(n_nodes)
        x_ov = left + 0.5 * overlap_len * (loc_nodes + 1.0)
        w_ov = 0.5 * overlap_len * loc_w
        field = basis_values(x_ov, length, dimension) @ coeff
        reflected = basis_values(log_q - x_ov, length, dimension) @ coeff
        plus = 0.5 * (field + reflected)
        minus = 0.5 * (field - reflected)
        plus_e = float(np.dot(w_ov, plus * plus))
        minus_e = float(np.dot(w_ov, minus * minus))
    return {
        "even_e": even_e,
        "odd_e": odd_e,
        "parity": "odd" if odd_e > even_e else "even",
        "edge_frac": edge_frac,
        "inner_mass": inner_mass,
        "plus2": plus_e,
        "minus2": minus_e,
        "nrm2": nrm2,
    }


class FormCache:
    def __init__(self, dimension: int, n_outer: int, logqs: np.ndarray, weights: np.ndarray):
        self.dimension = int(dimension)
        self.n_outer = int(n_outer)
        self.n_inner = n_inner_of(self.dimension)
        self.logqs = np.asarray(logqs, dtype=np.float64)
        self.weights = np.asarray(weights, dtype=np.float64)
        self.free: dict[float, dict] = {}
        self.ov: dict[tuple[float, int], np.ndarray] = {}

    def free_at(self, length: float) -> dict:
        key = round(float(length), 12)
        packed = self.free.get(key)
        if packed is not None:
            return packed
        c_l = c_L_of(length)
        gram = gram_matrix(length, self.dimension, self.n_inner)
        arch = arch_matrix(
            length, self.dimension, gram, c_l, self.n_outer, self.n_inner,
        )
        cosh_vector, sinh_vector = pole_vectors(length, self.dimension, self.n_inner)
        pole = pole_matrix(cosh_vector, sinh_vector)
        free = 0.5 * ((arch + pole) + (arch + pole).T)
        packed = {
            "gram": 0.5 * (gram + gram.T),
            "arch": arch,
            "pole": pole,
            "free": free,
            "cosh": cosh_vector,
            "sinh": sinh_vector,
            "c_L": c_l,
        }
        self.free[key] = packed
        return packed

    def overlap_at(self, length: float, index: int) -> np.ndarray:
        key = (round(float(length), 12), int(index))
        cached = self.ov.get(key)
        if cached is not None:
            return cached
        matrix = overlap_matrix(
            length, float(self.logqs[index]), self.dimension, self.n_inner,
        )
        self.ov[key] = matrix
        return matrix

    def assemble(self, length: float, n_ev: int) -> dict:
        packed = self.free_at(length)
        prime = np.zeros((self.dimension, self.dimension), dtype=np.float64)
        two_l = 2.0 * length
        n_use = max(0, min(int(n_ev), int(self.logqs.size)))
        overlaps = []
        for index in range(n_use):
            overlap = self.overlap_at(length, index)
            overlaps.append(overlap)
            if 0.0 < self.logqs[index] < two_l - 1.0e-15:
                prime = prime + self.weights[index] * overlap
        full = 0.5 * ((packed["free"] - prime) + (packed["free"] - prime).T)
        return {
            **packed,
            "prime": prime,
            "full": full,
            "overlaps": overlaps,
            "n_ev": n_use,
        }


def source_split(coeff: np.ndarray, forms: dict) -> dict:
    pole = float(coeff @ forms["pole"] @ coeff)
    arch = float(coeff @ forms["arch"] @ coeff)
    prime = float(coeff @ forms["prime"] @ coeff)
    q_val = pole + arch - prime
    depth = max(abs(pole), abs(arch), abs(prime)) / max(abs(q_val), 1.0e-30)
    return {"pole": pole, "arch": arch, "prime": prime, "q": q_val, "depth": depth}


def g_at(coeff: np.ndarray, overlap: np.ndarray) -> float:
    return float(coeff @ overlap @ coeff)


def first_negative(
    cache: FormCache,
    n_ev_fn,
    start: float,
    stop: float,
    step: float,
) -> tuple[float, float]:
    prev_l = start
    prev_v = float("nan")
    length = start
    while length <= stop + 1.0e-12:
        n_ev = n_ev_fn(length)
        forms = cache.assemble(length, n_ev)
        value, _vec = min_rayleigh(forms["full"], forms["gram"])
        if math.isfinite(prev_v) and prev_v > CROSS_POS and value <= CROSS_NEG:
            def func(point, _cache=cache, n_fn=n_ev_fn):
                packed = _cache.assemble(point, n_fn(point))
                val, _ = min_rayleigh(packed["full"], packed["gram"])
                return val

            root, _, _ = bisect_crossing(func, prev_l, length)
            return float(root), value
        if (not math.isfinite(prev_v)) and value <= CROSS_NEG:
            return float(length), value
        prev_l, prev_v = length, value
        length += step
    return float("inf"), prev_v


def sanitize_mu(value: float) -> float:
    """Treat |μ| < CROSS_POS as still positive (Slepian roundoff, not an O(1) crash)."""
    if value > -CROSS_POS:
        return max(float(value), CROSS_POS)
    return float(value)


def scan_crossing(mu_fn, left: float, scan_hi: float, gap: float):
    """O(1) ancestor sign-change; ignore ~1e-12 Slepian roundoff."""
    step = max(min(0.04, 0.25 * max(gap, 0.02)), 0.01)
    value, vec, pack = mu_fn(left)
    mu_min = float(value)
    if sanitize_mu(value) <= CROSS_NEG:
        return float(left), float(value), vec, pack, mu_min, float(left)
    prev, prev_raw = left, value
    probe = left
    while probe < scan_hi - 1.0e-14:
        nxt = min(probe + step, scan_hi)
        val_n, vec_n, pack_n = mu_fn(nxt)
        mu_min = min(mu_min, float(val_n))
        if sanitize_mu(prev_raw) > 0.0 and sanitize_mu(val_n) <= CROSS_NEG:
            def scalar(point, _fn=mu_fn):
                val, _vec, _pack = _fn(point)
                return sanitize_mu(val)

            root, _, _ = bisect_crossing(scalar, prev, nxt)
            if not math.isfinite(root):
                root = float(nxt)
            mu_r, vec_r, pack_r = mu_fn(root)
            char_l = float(root)
            if mu_r > -1.0e-4:
                walk = float(root)
                while walk < scan_hi - 1.0e-14:
                    walk = min(walk + min(0.01, step), scan_hi)
                    mu2, vec2, pack2 = mu_fn(walk)
                    mu_min = min(mu_min, float(mu2))
                    if mu2 <= -1.0e-4:
                        vec_r, pack_r = vec2, pack2
                        mu_r = float(mu2)
                        char_l = float(walk)
                        break
            return float(root), float(mu_r), vec_r, pack_r, mu_min, char_l
        prev, prev_raw, probe = nxt, val_n, nxt
    return float("inf"), float(value), None, None, mu_min, float("nan")


def nearest_entry(length: float, entries: np.ndarray) -> tuple[float, float]:
    if entries.size == 0 or not math.isfinite(length):
        return float("nan"), float("nan")
    delta = np.abs(entries - length)
    index = int(np.argmin(delta))
    return float(entries[index]), float(delta[index])


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    _CL_CACHE.clear()
    wall0 = time.time()

    if smoke:
        q_max = Q_MAX_SMOKE
        dimension = N_SMOKE
        n_zeros = N_ZEROS_SMOKE
        n_outer = N_OUTER_SMOKE
        n_c6 = N_C6_SMOKE
        c6_step = C6_STEP_SMOKE
        n_cross = min(N_CROSS, N_SMOKE)
    else:
        q_max = Q_MAX_FULL
        dimension = N_FULL
        n_zeros = N_ZEROS_FULL
        n_outer = N_OUTER_FULL
        n_c6 = N_C6_FULL
        c6_step = C6_STEP_FULL
        n_cross = min(N_CROSS, N_FULL)

    qs, logqs, weights, ells, q_next, lam_table = prime_powers_upto(q_max)
    n_events = len(qs)
    ell_next = 0.5 * math.log(q_next)
    ells_ext = np.concatenate([ells, np.array([ell_next], dtype=np.float64)])
    log_hi = math.log(float(q_max))

    emit("support_relay_census_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("q_max %d  n_events %d  q_next %d  N=%d  n_zeros=%d  n_outer=%d" % (
        q_max, n_events, q_next, dimension, n_zeros, n_outer,
    ))
    emit("events %s" % ",".join(str(q_val) for q_val in qs))
    emit("w2 %s  w[0] %s  damp (1-(u/L)^2)^%d" % (
        fmt(W2, 16), fmt(float(weights[0]), 16), DAMP_POWER,
    ))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit(
        "C1 R_j is RH-consistent positivity, not a decider.  "
        "Window positivity for the scanned L is RH-consistent; no RH claim."
    )

    zeros = load_zeros(n_zeros)
    emit("zeros n=%d gamma1=%s gammaN=%s source=%s" % (
        int(zeros.size), fmt(float(zeros[0]), 12), fmt(float(zeros[-1]), 12),
        "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
    ))

    n_conn = max(dimension, n_c6, n_cross, 12)
    connection = damped_connection(n_conn)

    section("G0  GAUSSIAN EF PIN")
    g0 = gaussian_g0(zeros)
    emit(
        "  alpha=%s POLE=%s ARCH=%s PRIME=%s Z_src=%s Z_zeros=%s rel=%s rel_term=%s"
        % (
            fmt(g0["alpha"], 4), fmt(g0["pole"], 12), fmt(g0["arch"], 12),
            fmt(g0["prime"], 12), fmt(g0["z_src"], 12), fmt(g0["z_zeros"], 12),
            fmt(g0["rel"], 6), fmt(g0["rel_term"], 6),
        )
    )
    check("G0-EF-identity", g0["rel"] <= G0_REL, "rel=%s" % fmt(g0["rel"], 6))
    check("G0-w2-pin", abs(g0["w2"] - W2) <= 1.0e-15, "w2=%s" % fmt(W2, 16))
    check(
        "G0-w2-event",
        abs(float(weights[0]) - W2) <= 1.0e-12,
        "w[q=2]=%s" % fmt(float(weights[0]), 16),
    )
    c03_mp = c_L_mp(0.3)
    c03_np = c_L_numpy(0.3)
    emit("  c_L(0.3) mp=%s numpy=%s" % (fmt(c03_mp, 16), fmt(c03_np, 16)))
    check(
        "G0-cL-0.3",
        2.19240491113 < c03_mp < 2.19240491114,
        "c_L(0.3)=%s" % fmt(c03_mp, 16),
    )
    check(
        "G0-cL-numpy",
        abs(c03_np - c03_mp) / max(abs(c03_mp), 1.0e-30) <= 1.0e-10,
        "rel=%s" % fmt(abs(c03_np - c03_mp) / max(abs(c03_mp), 1.0e-30), 6),
    )
    _CL_CACHE[round(0.3, 12)] = c03_np

    section("G1  ARCH x-space vs t-space")
    g1_length = 0.30
    g1_dim = 12
    g1_n_inner = n_inner_of(g1_dim)
    g1_gram = gram_matrix(g1_length, g1_dim, g1_n_inner)
    g1_arch = arch_matrix(
        g1_length, g1_dim, g1_gram, c_L_of(g1_length), N_OUTER_G1, g1_n_inner,
    )
    g1_cosh, g1_sinh = pole_vectors(g1_length, g1_dim, g1_n_inner)
    g1_pole = pole_matrix(g1_cosh, g1_sinh)
    g1_conn = connection
    g1_ok_all = True
    for index in range(3):
        coeff = np.zeros(g1_dim, dtype=np.float64)
        coeff[min(2 * index, g1_dim - 1)] = 1.0
        norm = math.sqrt(float(coeff @ g1_gram @ coeff))
        coeff = coeff / max(norm, 1.0e-30)
        arch_x = float(coeff @ g1_arch @ coeff)
        pole_x = float(coeff @ g1_pole @ coeff)

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
        emit(
            "  vec%d ARCH_x=%s ARCH_t=%s rel=%s POLE=%s"
            % (index, fmt(arch_x, 12), fmt(arch_t, 12), fmt(rel, 6), fmt(pole_x, 12))
        )
        ok = rel <= G1_REL
        g1_ok_all = g1_ok_all and ok
        check("G1-vec%d" % index, ok, "rel=%s" % fmt(rel, 6))

    section("CENSUS  λ*(L)  (a) source Ritz / (b) zero-side SVD")
    cache = FormCache(dimension, n_outer, logqs, weights)
    grids = []
    census_L = []
    for index in range(n_events):
        left = float(ells_ext[index])
        right = float(ells_ext[index + 1])
        grid = interval_grid(left, right)
        grids.append(grid)
        for point in grid:
            census_L.append(float(point))
    census_L = sorted(set(round(val, 12) for val in census_L))
    census_L = [float(val) for val in census_L]

    rows = []
    ab_ok_all = True
    n_ab = 0
    n_unrel = 0
    for length in census_L:
        j_act = max(n_active(length, logqs), 0)
        forms = cache.assemble(length, j_act)
        lam_a, vec_a = min_rayleigh(forms["full"], forms["gram"])
        split = source_split(vec_a, forms)
        zside = zero_side_min(length, dimension, connection, zeros, forms["gram"])
        lam_b = float(zside["lam"])
        if -1.0e-12 < lam_b < 0.0:
            lam_b = 0.0
        reliable = split["depth"] <= D_UNREL and math.isfinite(lam_a)
        if not reliable:
            n_unrel += 1
        ratio = float("nan")
        if reliable and abs(lam_b) > 1.0e-30 and math.isfinite(lam_b):
            ratio = lam_a / lam_b - 1.0
            n_ab += 1
            if abs(ratio) > AB_REL:
                ab_ok_all = False
        j_interval = max(1, min(n_events, j_act if j_act >= 1 else 1))
        if length + 1.0e-12 >= float(ells[0]):
            j_interval = 1
            for idx in range(n_events):
                if length + 1.0e-12 >= float(ells[idx]):
                    j_interval = idx + 1
        row = {
            "L": length,
            "j": j_interval,
            "j_act": j_act,
            "lam_a": lam_a,
            "lam_b": lam_b,
            "depth": split["depth"],
            "reliable": reliable,
            "ratio": ratio,
            "pole": split["pole"],
            "arch": split["arch"],
            "prime": split["prime"],
            "tail": zside["tail"],
            "cond": zside["cond"],
            "lam_svd": zside["lam_svd"],
            "vec_a": vec_a,
        }
        rows.append(row)
        emit(
            "  L=%s j=%d act=%d (a)=%s D=%s rel=%d (b)=%s tail=%s cond=%s ratio=%s svd=%s"
            % (
                fmt(length, 6), j_interval, j_act, fmt(lam_a, 10),
                fmt(split["depth"], 4), int(reliable), fmt(lam_b, 10),
                fmt(zside["tail"], 8), fmt(zside["cond"], 6), fmt(ratio, 6),
                fmt(zside["lam_svd"], 10),
            )
        )
    check(
        "C-AB-ratio",
        ab_ok_all and n_ab >= 1,
        "ok=%d n_rel=%d n_unrel=%d" % (int(ab_ok_all), n_ab, n_unrel),
    )

    section("C1  RELAY CONSISTENCY R_j  (RH-consistent, not a decider)")
    c1_rows = []
    c1_all = True
    for index in range(n_events):
        left = float(ells_ext[index])
        right = float(ells_ext[index + 1])
        interval = [
            row for row in rows
            if row["L"] + 1.0e-12 >= left and row["L"] <= right + 1.0e-12
        ]
        if not interval:
            c1_all = False
            c1_rows.append({
                "j": index + 1, "q": qs[index], "L": left,
                "min_b": float("nan"), "R": 0,
            })
            continue
        min_b = min(float(row["lam_b"]) for row in interval)
        r_j = 1 if min_b > -1.0e-12 else 0
        if r_j < 1:
            c1_all = False
        c1_rows.append({
            "j": index + 1, "q": qs[index], "L": left, "gap": right - left,
            "min_b": min_b, "R": r_j,
        })
        emit(
            "  j=%d q=%d L_j=%s gap=%s min_λ*(b)=%s R_j=%d"
            % (
                index + 1, qs[index], fmt(left, 8), fmt(right - left, 8),
                fmt(min_b, 10), r_j,
            )
        )
    check("C1-Rj-all", c1_all, "all R_j>=1 (RH-consistent, not a decider)")

    section("C2/C3  LEAD AND FAILING MODE")
    cache_x = FormCache(n_cross, n_outer, logqs, weights)
    event_table = []
    for index in range(n_events):
        j_ev = index + 1
        left = float(ells_ext[index])
        right = float(ells_ext[index + 1])
        gap = right - left
        scan_hi = right + EXT_PAD

        def mu_anc(point, drop: int):
            n_keep = max(0, j_ev - drop)
            packed = cache_x.assemble(point, n_keep)
            value, vec = min_rayleigh(packed["full"], packed["gram"])
            return value, vec, packed

        crossing, mu_at, vec_x, forms_x, mu_min, char_l = scan_crossing(
            lambda point: mu_anc(point, 1), left, scan_hi, gap,
        )
        if j_ev >= 2:
            c_mm, _mu2, _v2, _p2, _m2, _c2 = scan_crossing(
                lambda point: mu_anc(point, 2), left, scan_hi, gap,
            )
        else:
            c_mm = float("nan")

        if math.isfinite(crossing):
            delta = crossing - left
            ratio_gap = delta / gap if gap > 1.0e-15 else float("inf")
            c_print = crossing
        else:
            delta = float("inf")
            ratio_gap = float("inf")
            c_print = float("inf")

        log_q = float(logqs[index])
        w_j = float(weights[index])
        g_val = float("nan")
        q_repair = float("nan")
        repair = False
        profile = {
            "parity": "n/a", "even_e": float("nan"), "odd_e": float("nan"),
            "edge_frac": float("nan"), "inner_mass": float("nan"),
            "plus2": float("nan"), "minus2": float("nan"),
        }
        g_sign = "n/a"
        if (
            math.isfinite(crossing)
            and vec_x is not None
            and forms_x is not None
        ):
            mode_L = char_l if math.isfinite(char_l) else crossing
            ov_new = overlap_matrix(
                mode_L, log_q, n_cross, n_inner_of(n_cross),
            )
            g_val = g_at(vec_x, ov_new)
            q_repair = mu_at - w_j * g_val
            repair = (-w_j * g_val) > abs(mu_at)
            profile = characterize(mode_L, n_cross, vec_x, log_q)
            g_sign = "+" if g_val > 0.0 else ("-" if g_val < 0.0 else "0")

        load_bearing = 0
        if math.isfinite(crossing) and delta < gap:
            load_bearing = 1
            if math.isfinite(c_mm) and (c_mm - left) < gap:
                load_bearing = 2

        rec = {
            "j": j_ev,
            "q": qs[index],
            "L": left,
            "gap": gap,
            "crossing": c_print,
            "delta": delta,
            "ratio_gap": ratio_gap,
            "c_mm": c_mm,
            "mu": mu_at,
            "mu_min": mu_min,
            "g": g_val,
            "g_sign": g_sign,
            "repair": repair,
            "Qj_h1": q_repair,
            "parity": profile["parity"],
            "even_e": profile["even_e"],
            "odd_e": profile["odd_e"],
            "edge": profile["edge_frac"],
            "inner": profile["inner_mass"],
            "plus2": profile["plus2"],
            "minus2": profile["minus2"],
            "plus_gt_minus": (
                math.isfinite(profile["plus2"])
                and math.isfinite(profile["minus2"])
                and profile["plus2"] > profile["minus2"]
            ),
            "load_bearing": load_bearing,
        }
        event_table.append(rec)
        c_str = (
            ">L_{j+1}+0.5" if not math.isfinite(c_print)
            else fmt(c_print, 6)
        )
        if j_ev == 1:
            c2_str = "n/a"
        elif math.isinf(c_mm):
            c2_str = ">L_{j+1}+0.5"
        else:
            c2_str = fmt(c_mm, 6)
        emit(
            "  j=%d q=%d L_j=%s Δ=%s Δ/gap=%s c^-=%s c^{--}=%s μ=%s μmin=%s "
            "parity=%s edge=%s |f+|²=%s |f-|²=%s g=%s sgn=%s repair=%d Qj(h1)=%s inner=%s"
            % (
                j_ev, qs[index], fmt(left, 6), fmt(delta, 6), fmt(ratio_gap, 4),
                c_str, c2_str, fmt(mu_at, 8), fmt(mu_min, 6), profile["parity"],
                fmt(profile["edge_frac"], 4), fmt(profile["plus2"], 6),
                fmt(profile["minus2"], 6), fmt(g_val, 6), g_sign,
                int(repair), fmt(q_repair, 8), fmt(profile["inner_mass"], 4),
            )
        )

    section("C4  SCALING  log λ*(L) vs L")
    xs = [row["L"] for row in rows if row["lam_b"] > 0.0 and math.isfinite(row["lam_b"])]
    ys = [
        math.log(row["lam_b"]) for row in rows
        if row["lam_b"] > 0.0 and math.isfinite(row["lam_b"])
    ]
    slope_global = fit_slope(xs, ys)
    emit(
        "  global slope=%s  Slepian -2γ1=%s  r615=%s"
        % (fmt(slope_global, 6), fmt(SLEPIAN_SLOPE, 6), fmt(R615_SLOPE, 4))
    )
    piece = []
    for index in range(n_events):
        left = float(ells_ext[index])
        right = float(ells_ext[index + 1])
        xs_i = []
        ys_i = []
        for row in rows:
            if row["L"] + 1.0e-12 < left or row["L"] > right + 1.0e-12:
                continue
            if row["lam_b"] > 0.0 and math.isfinite(row["lam_b"]):
                xs_i.append(row["L"])
                ys_i.append(math.log(row["lam_b"]))
        slope_i = fit_slope(xs_i, ys_i)
        piece.append(slope_i)
        emit(
            "  interval j=%d q=%d slope=%s n=%d"
            % (index + 1, qs[index], fmt(slope_i, 6), len(xs_i))
        )

    section("C5  TWO-KEY CONTROLS")
    rng = np.random.RandomState(SEED)
    pos_scr = np.sort(rng.uniform(LOG2 + 1.0e-9, log_hi - 1.0e-9, size=n_events))
    w_perm = weights[rng.permutation(n_events)]
    cache_scr = FormCache(N_CTRL, n_outer, pos_scr, weights)
    cache_wperm = FormCache(N_CTRL, n_outer, logqs, w_perm)
    two_k = [q_val for q_val in qs if (q_val & (q_val - 1)) == 0]
    log_2k = np.array([math.log(q_val) for q_val in two_k], dtype=np.float64)
    w_2k = np.array(
        [2.0 * lam_table[q_val] / math.sqrt(q_val) for q_val in two_k],
        dtype=np.float64,
    )
    cache_eps = FormCache(N_CTRL, n_outer, log_2k, w_2k)
    scan_lo = float(ells[0]) - 1.0e-3
    scan_hi = float(ell_next) + EXT_PAD
    scan_step = 0.05 if not smoke else 0.08

    def n_ev_from(log_arr):
        def _fn(length, arr=log_arr):
            return n_active(length, arr)
        return _fn

    L_scr, _v_scr = first_negative(
        cache_scr, n_ev_from(pos_scr), scan_lo, scan_hi, scan_step,
    )
    L_wperm, _v_wp = first_negative(
        cache_wperm, n_ev_from(logqs), scan_lo, scan_hi, scan_step,
    )
    L_eps, _v_eps = first_negative(
        cache_eps, n_ev_from(log_2k), scan_lo, scan_hi, scan_step,
    )
    scr_entries = 0.5 * pos_scr
    near_scr, dist_scr = nearest_entry(L_scr, scr_entries)
    true_entries = ells
    near_true, dist_true = nearest_entry(L_scr, true_entries)
    coincide_scr = math.isfinite(L_scr) and math.isfinite(dist_scr) and dist_scr <= 0.03
    emit("  SCRAMBLE pos=%s" % ",".join(fmt(val, 6) for val in pos_scr))
    emit(
        "  SCRAMBLE first_neg L=%s  nearest_scr_entry=%s dist=%s coincide=%d"
        % (fmt(L_scr, 6), fmt(near_scr, 6), fmt(dist_scr, 6), int(coincide_scr))
    )
    emit(
        "    vs true entries nearest=%s dist=%s"
        % (fmt(near_true, 6), fmt(dist_true, 6))
    )
    emit("  WPERM first_neg L=%s" % fmt(L_wperm, 6))
    emit(
        "  EPSTEIN 2^k=%s first_neg L=%s"
        % (",".join(str(q_val) for q_val in two_k), fmt(L_eps, 6))
    )

    section("C6  DETECTION THRESHOLD  (off-line injection, zero-side)")
    emit(
        "  ĥ_H(ρ)=f̂(ρ) f̂(1-ρ̄)* .  On-line: |f̂(γ)|^2.  "
        "Quadruple {β±iγ,(1-β)±iγ} adds 4 Re[F(σ,γ) F(-σ,γ)*], σ=β-1/2, "
        "replacing the ±γ0 on-line pair 2|f̂(γ0)|^2."
    )
    c6_L = np.arange(C6_L_LO, C6_L_HI + 0.5 * c6_step, c6_step)
    cache_c6_gram = {}

    def gram_c6(length: float):
        key = round(float(length), 12)
        packed = cache_c6_gram.get(key)
        if packed is None:
            packed = gram_matrix(length, n_c6, n_inner_of(n_c6))
            cache_c6_gram[key] = packed
        return packed

    # validate ĥ_H on an on-line zero with a unit trial vector
    val_L = 0.50
    val_gram = gram_c6(val_L)
    val_hats = bessel_damped_hat(val_L, zeros[: min(20, zeros.size)], n_c6, connection)
    coeff_val = np.zeros(n_c6, dtype=np.float64)
    coeff_val[0] = 1.0
    norm_val = math.sqrt(float(coeff_val @ val_gram @ coeff_val))
    coeff_val = coeff_val / max(norm_val, 1.0e-30)
    hat_on = hat_combination(val_hats, coeff_val)
    k0_val = int(np.argmin(np.abs(zeros[: min(20, zeros.size)] - 20.0)))
    f_rho = hat_on[k0_val]
    hat_h = f_rho * np.conj(f_rho)
    online_sq = np.abs(f_rho) ** 2
    rel_h = abs(hat_h - online_sq) / max(abs(online_sq), 1.0e-30)
    emit(
        "  validate ĥ_H(1/2+iγ)=|f̂|²  γ=%s rel=%s"
        % (fmt(float(zeros[k0_val]), 8), fmt(float(np.abs(rel_h)), 6))
    )
    check("C6-H-online", float(np.abs(rel_h)) <= 1.0e-10, "rel=%s" % fmt(float(np.abs(rel_h)), 6))

    floor_L = float(c6_L[0])
    gram0 = gram_c6(floor_L)
    hats0 = bessel_damped_hat(floor_L, zeros, n_c6, connection)
    gram_h0 = 2.0 * np.real(hats0.conj().T @ hats0)
    gram_h0 = 0.5 * (gram_h0 + gram_h0.T)
    tail0 = tail_matrix(
        floor_L, n_c6, connection, float(zeros[-1]), t_extra=1500.0, n_quad=32,
    )
    lam_on, _ = min_rayleigh(gram_h0 + tail0, gram0)
    emit(
        "  online-only λ*(L=%s, N=%d)=%s  (must stay >0; C6 injection may go negative)"
        % (fmt(floor_L, 4), n_c6, fmt(lam_on, 8))
    )
    check("C6-online-positive", lam_on > 0.0, "lam=%s" % fmt(lam_on, 8))

    ldet = {}
    for beta, gamma in C6_PAIRS:
        sigma = beta - 0.5
        found_L = float("inf")
        k0 = int(np.argmin(np.abs(zeros - gamma)))
        gamma0 = float(zeros[k0])
        for length in c6_L:
            gram = gram_c6(float(length))
            hats = bessel_damped_hat(float(length), zeros, n_c6, connection)
            gram_h = 2.0 * np.real(hats.conj().T @ hats)
            row = hats[k0]
            gram_h = gram_h - 2.0 * np.real(np.outer(np.conj(row), row))
            gram_h = 0.5 * (gram_h + gram_h.T)
            # inject the quadruple at the requested γ (not γ0); t = γ ∓ iσ
            t_plus = gamma - 1j * sigma
            t_minus = gamma + 1j * sigma
            hats_c = basis_hat_complex(float(length), [t_plus, t_minus], n_c6)
            off = offline_matrix(hats_c[0], hats_c[1])
            tail = tail_matrix(
                float(length), n_c6, connection, float(zeros[-1]),
                t_extra=1500.0, n_quad=32,
            )
            pencil = 0.5 * ((gram_h + off + tail) + (gram_h + off + tail).T)
            lam, _vec = min_rayleigh(pencil, gram)
            if lam < 0.0:
                found_L = float(length)
                break
        ldet[(beta, gamma)] = found_L
        if math.isfinite(found_L) and abs(found_L - floor_L) < 0.5 * c6_step:
            ldet_str = "<= %s (scan floor)" % fmt(found_L, 4)
        elif not math.isfinite(found_L):
            ldet_str = "> 3.0"
        else:
            ldet_str = fmt(found_L, 4)
        emit(
            "  L_det(β=%s, γ=%s) γ0=%s  %s"
            % (fmt(beta, 4), fmt(gamma, 4), fmt(gamma0, 6), ldet_str)
        )

    section("L_det TABLE")
    emit("  beta   gamma   L_det")
    for beta, gamma in C6_PAIRS:
        val = ldet[(beta, gamma)]
        if not math.isfinite(val):
            shown = "> 3.0"
        elif abs(val - floor_L) < 0.5 * c6_step:
            shown = "<= %s (scan floor)" % fmt(val, 4)
        else:
            shown = fmt(val, 4)
        emit("  %s  %s  %s" % (fmt(beta, 4), fmt(gamma, 4), shown))
    emit("Window positivity for the scanned L is RH-consistent; no RH claim.")

    section("VERDICT")
    finite_leads = []
    partial_list = []
    mixed_list = []
    repair_fail = []
    for rec in event_table:
        finite = math.isfinite(rec["delta"]) and rec["delta"] > 0.0
        finite_leads.append(finite)
        if not math.isfinite(rec["delta"]):
            partial_list.append("j=%d(q=%d,no_O1_cross)" % (rec["j"], rec["q"]))
        elif rec["delta"] <= 0.0:
            partial_list.append("j=%d(q=%d,delta<=0)" % (rec["j"], rec["q"]))
        elif rec["delta"] >= rec["gap"] - 1.0e-12:
            partial_list.append("j=%d(q=%d,Δ/gap=%s)" % (
                rec["j"], rec["q"], fmt(rec["ratio_gap"], 4),
            ))
        if finite and not rec["repair"]:
            repair_fail.append("j=%d" % rec["j"])
            partial_list.append("j=%d(repair)" % rec["j"])
        if finite and not rec["plus_gt_minus"]:
            mixed_list.append("j=%d" % rec["j"])

    if (not ab_ok_all) or (not c1_all):
        verdict = "INCONCLUSIVE"
        why = "C-AB disagree where valid or some R_j failed (numerical, not a result)"
    elif (
        all(finite_leads)
        and not partial_list
        and not repair_fail
        and not mixed_list
    ):
        verdict = "RELAY_UNIVERSAL"
        why = "every event has finite positive lead and repair with |f+|²>|f-|²"
    elif all(finite_leads) and mixed_list:
        verdict = "RELAY_MIXED_SECTOR"
        why = "leads finite; failing mode not reflection-symmetric at " + ",".join(mixed_list)
    else:
        verdict = "RELAY_PARTIAL"
        why = "not load-bearing before next entry or repair fail: " + (
            ",".join(partial_list) if partial_list else "see table"
        )

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    wall = time.time() - wall0
    payload = {
        "verdict": verdict,
        "gates": "%d/%d" % (n_pass, n_gate),
        "events": [
            {
                "j": rec["j"], "q": rec["q"],
                "L": round(rec["L"], 10),
                "delta": rec["delta"] if math.isfinite(rec["delta"]) else None,
                "ratio": rec["ratio_gap"] if math.isfinite(rec["ratio_gap"]) else None,
                "repair": bool(rec["repair"]),
                "plus": rec["plus2"], "minus": rec["minus2"],
                "parity": rec["parity"], "gsign": rec["g_sign"],
            }
            for rec in event_table
        ],
        "slope": slope_global,
        "L_scr": L_scr if math.isfinite(L_scr) else None,
        "L_wperm": L_wperm if math.isfinite(L_wperm) else None,
        "L_eps": L_eps if math.isfinite(L_eps) else None,
        "L_det": {
            "%s_%s" % (beta, gamma): (
                ldet[(beta, gamma)] if math.isfinite(ldet[(beta, gamma)]) else None
            )
            for beta, gamma in C6_PAIRS
        },
    }
    result_sha = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    ).hexdigest()

    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % result_sha)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")

    section("STATE")
    emit("round r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % result_sha)
    emit("smoke %d  q_max %d  N %d  n_zeros %d  wall_s %s" % (
        int(smoke), q_max, dimension, n_zeros, fmt(wall, 4),
    ))
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("C1 R_j RH-consistent not a decider: %s" % ("all>=1" if c1_all else "FAIL"))
    emit(
        "C4 slope_global=%s Slepian=%s r615=%s"
        % (fmt(slope_global, 5), fmt(SLEPIAN_SLOPE, 4), fmt(R615_SLOPE, 3))
    )
    emit("C4 piece " + ",".join(fmt(val, 3) for val in piece))
    emit(
        "C5 SCRAMBLE L-=%s coincide_entry=%d  WPERM L-=%s  EPSTEIN L-=%s"
        % (fmt(L_scr, 5), int(coincide_scr), fmt(L_wperm, 5), fmt(L_eps, 5))
    )
    emit("C6 L_det " + " ".join(
        "(%s,%s)=%s" % (
            fmt(beta, 2), fmt(gamma, 2),
            (
                ">3.0" if not math.isfinite(ldet[(beta, gamma)])
                else (
                    "<=%s" % fmt(ldet[(beta, gamma)], 3)
                    if abs(ldet[(beta, gamma)] - floor_L) < 0.5 * c6_step
                    else fmt(ldet[(beta, gamma)], 3)
                )
            ),
        )
        for beta, gamma in C6_PAIRS
    ))
    emit("table j q L_j Δ Δ/gap c-- parity edge |f+|² |f-|² g_sgn repair")
    for rec in event_table:
        emit(
            "  %d %d %s %s %s %s %s %s %s %s %s %d"
            % (
                rec["j"], rec["q"], fmt(rec["L"], 5),
                (">inf" if not math.isfinite(rec["delta"]) else fmt(rec["delta"], 4)),
                (">inf" if not math.isfinite(rec["ratio_gap"]) else fmt(rec["ratio_gap"], 3)),
                (
                    "n/a" if rec["j"] == 1
                    else (
                        ">pad" if not math.isfinite(rec["c_mm"])
                        else fmt(rec["c_mm"], 4)
                    )
                ),
                rec["parity"], fmt(rec["edge"], 3),
                fmt(rec["plus2"], 4), fmt(rec["minus2"], 4),
                rec["g_sign"], int(rec["repair"]),
            )
        )
    emit("Window positivity for the scanned L is RH-consistent; no RH claim.")
    emit("END_STATE")
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r619 support-relay census (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
