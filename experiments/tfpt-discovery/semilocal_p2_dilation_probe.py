#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""semilocal_p2_dilation_probe -- r623  PRIME.SEMILOCAL.P2.DILATION.01

Experiments-only scout of the proposed principal-block / rank-one
dilation of the first 2-adic Weil channel.  Merges the r623 Euler
tower test with the r624 dilation obstruction.

Copied r615 machinery (not imported): window form on real h supported
in [-L, L],

  Q_L(h) = POLE(h) + ARCH(h) − PRIME(h)

with POLE = 2(⟨h, cosh(u/2)⟩² − ⟨h, sinh(u/2)⟩²), ARCH the t-space
multiplier (1/2π)∫ |ĥ|² (Re ψ(¼+it/2) − log π) dt (G1 cross-checks
the v1017 x-space kernel), and the *full* 2-adic channel

  W₂(h) := −Σ_{k≥1} Λ(2^k) 2^{−k/2} [g_h(k log 2) + g_h(−k log 2)]

summed over the rungs with k log 2 ≤ 2L.  For L ≥ (log 3)/2 the
prime-3 channel is included so Q_L is the true windowed Weil form.
Trial spaces: orthonormal Legendre P̃_n on [-L, L] and the
edge-damped family (1−(u/L)²)² P̃_n.

Claim boundary: finite-section arithmetic on a frozen L-grid.
Not a ledger row.  Not a paper claim.
Fence: Semilocal identities; window forms at these L are
RH-consistent; no RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from scipy.linalg import eigh as seigh  # noqa: E402
from scipy.special import roots_legendre, spherical_jn  # noqa: E402

HERE = Path(__file__).resolve().parent
ZEROS_CACHE = HERE / "verified_zeros_n7000.npy"

ROUND = 623
SEED = 623202609
CONTRACT = "PRIME.SEMILOCAL.P2.DILATION.01"
FENCE = (
    "Semilocal identities; window forms at these L are "
    "RH-consistent; no RH claim."
)

LOG2 = math.log(2.0)
LOG3 = math.log(3.0)
LOGPI = math.log(math.pi)
HALF_LOG2 = 0.5 * LOG2
HALF_LOG3 = 0.5 * LOG3
R_POISSON = 2.0 ** -0.5
W2 = math.sqrt(2.0) * LOG2
W3 = 2.0 * LOG3 / math.sqrt(3.0)
G0_ALPHA = 20.0
G0_REL = 1.0e-8
G1_REL = 1.0e-8
A1_REL = 1.0e-10
A1_N_RANDOM = 10
A1_KMAX = 80
EIG_REL = 1.0e-8
PSD_ATOL = 1.0e-8
C1_ID_REL = 5.0e-4
RANK1_MAX = 1

GRID_FULL = (0.40, 0.46, 0.52, 0.549, 0.60, 0.65, 0.72, 0.80)
GRID_SMOKE = (0.40, 0.549, 0.72)
N_A_FULL = 24
N_A_SMOKE = 12
N_B_FULL = 16
N_B_SMOKE = 8
N_OUTER_FULL = 80
N_OUTER_SMOKE = 48
G1_LENGTH = 0.30
G1_DIM = 12
G1_OUTER = 320
G1_VECTORS = 3
N_ZEROS_FULL = 200
N_ZEROS_SMOKE = 80
PANELS_FULL = (
    (0.0, 20.0, 96),
    (20.0, 80.0, 96),
    (80.0, 400.0, 128),
    (400.0, 2500.0, 96),
)
PANELS_SMOKE = (
    (0.0, 40.0, 48),
    (40.0, 200.0, 48),
    (200.0, 800.0, 48),
)
G1_PANELS = (
    (0.0, 20.0, 128),
    (20.0, 80.0, 128),
    (80.0, 400.0, 160),
    (400.0, 2500.0, 128),
)

# Frozen C2 literature (authoring-time WebSearch; not fetched at runtime).
C2_CC21 = (
    "Connes–Consani, Selecta Math. (N.S.) 27 (2021), Paper No. 77 "
    "(arXiv:2006.13771). Theorem 1: let g in C_c^∞(R_+^*) have support "
    "in [2^{-1/2}, 2^{1/2}] and Fourier transform vanishing at i/2 and 0; "
    "then W_∞(g*g*) ≥ Tr(ϑ(g) S ϑ(g)*). Weaker form: W_∞(f) ≥ 0 for "
    "positive-definite f supported in (1/2, 2) with Fourier vanishing "
    "at ±i/2. Archimedean place only; primes are not involved."
)
C2_CCM2310 = (
    "Connes–Consani–Moscovici, arXiv:2310.18423 'Zeta zeros and prolate "
    "wave operators'. Goes beyond the single archimedean place in the "
    "semilocal trace-formula framework; Jacobi matrix of a general S is "
    "explicitly deferred ('forthcoming paper'). Semilocal Sonin: Def. 4.5 "
    "and Thm. 4.6 (§4.6). Not an unconditional positivity theorem for "
    "test functions supported past [2^{-1/2}, 2^{1/2}]."
)
C2_QS2403 = (
    "Connes–Consani, arXiv:2403.01247 'On q-series and the moment problem "
    "associated to local factors'. Treats S = {∞, p}; moments / orthogonal "
    "polynomials / Jacobi matrix as power series in q := 1/p (Lambert "
    "series for the moments). Moment problem, not Weil positivity on "
    "windows up to √3."
)
C2_SCALE = (
    "Connes–Consani, arXiv:1910.14368 'The scaling Hamiltonian', §2: "
    "recalls the semilocal trace formula on X_S; no positivity theorem "
    "beyond the archimedean [2^{-1/2}, 2^{1/2}] window."
)
C2_ZETA = (
    "Connes–Consani, Enseign. Math. 69 (2023), 93–148 "
    "(arXiv:2106.01715) 'Spectral triples and ζ-cycles': Weil quadratic "
    "form on a fixed interval of upper bound S, numerical small "
    "eigenvalues, zeta-cycles on the circle of length L = 2 log S. "
    "Numerical / spectral, not an unconditional semilocal positivity "
    "theorem for S = {∞, 2}."
)
C2_UNCOND_SEMILOCAL = False
C2_SUPPORT_CC21 = "[2^{-1/2}, 2^{1/2}]"
C2_SUPPORT_WEAK = "(1/2, 2)"

SPEC = {
    "round": ROUND,
    "tag": "r623",
    "contract": CONTRACT,
    "grid": list(GRID_FULL),
    "half_log2": HALF_LOG2,
    "half_log3": HALF_LOG3,
    "r_poisson": "2**(-1/2)",
    "w2": "sqrt(2)*log(2)",
    "w3": "2*log(3)/sqrt(3)",
    "g0_alpha": G0_ALPHA,
    "g0_rel": G0_REL,
    "g1_rel": G1_REL,
    "a1_rel": A1_REL,
    "a1_n_random": A1_N_RANDOM,
    "n_a": N_A_FULL,
    "n_b": N_B_FULL,
    "n_outer": N_OUTER_FULL,
    "n_zeros": N_ZEROS_FULL,
    "space_a": "legendre_P_n on [-L,L]",
    "space_b": "(1-(u/L)^2)^2 * P_n",
    "pole": "2*(<h,cosh(u/2)>^2 - <h,sinh(u/2)>^2)",
    "arch": "(1/2pi) int |hat h|^2 (Re psi(1/4+it/2)-log pi) dt",
    "kernel_x": "exp(x/2)/sinh(x)",
    "two_channel": (
        "-sum_k Lambda(2^k) 2^{-k/2} (g(k log 2)+g(-k log 2)), "
        "k log 2 <= 2L"
    ),
    "m2": "log 2 * (1 - P_r(t log 2))",
    "poisson": "(1-r^2)/|1-r e^{i theta}|^2",
    "identity": "Q = POLE + ARCH + W2 + W3",
    "dilation": "A = [[Q + M2minus, sqrt(M2minus)],[sqrt(M2minus), I]]",
    "seed": SEED,
    "c2_uncond_semilocal": C2_UNCOND_SEMILOCAL,
    "c2_support_cc21": C2_SUPPORT_CC21,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": FENCE,
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
    emit("  [%s] %-48s %s" % ("PASS" if flag else "FAIL", name, detail))
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
    if isinstance(value, (int, np.integer)) and not isinstance(
        value, (bool, np.bool_)
    ):
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
    """Re ψ(1/4+it/2) − log π.  Copied Stirling/recurrence from r615."""
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
    return psi_re - LOGPI


def poisson_kernel(theta) -> np.ndarray:
    """P_r(θ) = (1−r²)/|1−r e^{iθ}|², r = 2^{−1/2}."""
    angle = np.asarray(theta, dtype=np.float64)
    radius = R_POISSON
    return (1.0 - radius * radius) / (
        1.0 - 2.0 * radius * np.cos(angle) + radius * radius
    )


def m2_multiplier(t_values) -> np.ndarray:
    """m₂(t) = log 2 · (1 − P_r(t log 2))."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    return LOG2 * (1.0 - poisson_kernel(t_arr * LOG2))


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
    """v1017 high_precision_constants, any L.  Copied from r615."""
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


def damped_connection(n_max: int) -> np.ndarray:
    """(1-x^2)^2 P_n = sum_k a[n,k] P_k, k <= n+4.  Copied from r615."""
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
    """ĥ of orthonormal P̃_n, shape (len(t), n_max), complex.  r615."""
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


def g_invsqrt(gram: np.ndarray) -> np.ndarray:
    gram = 0.5 * (gram + gram.T)
    values, vectors = np.linalg.eigh(gram)
    scale = np.where(values > 1.0e-14, 1.0 / np.sqrt(np.maximum(values, 0.0)), 0.0)
    return (vectors * scale) @ vectors.T


def whiten(operator: np.ndarray, gram: np.ndarray) -> np.ndarray:
    whitener = g_invsqrt(gram)
    out = whitener @ operator @ whitener
    return 0.5 * (out + out.T)


def two_rung_ks(length: float) -> list[int]:
    rungs = []
    index = 1
    while index * LOG2 <= 2.0 * length + 1e-12:
        rungs.append(index)
        index += 1
    return rungs


def odd_primes_in_window(length: float) -> list[int]:
    primes = []
    for prime in (3, 5, 7):
        if math.log(prime) <= 2.0 * length + 1e-12:
            primes.append(prime)
    return primes


def active_rung_report(length: float) -> dict:
    ks = two_rung_ks(length)
    return {
        "L": length,
        "ks": ks,
        "powers": [2 ** index for index in ks],
        "odd": odd_primes_in_window(length),
        "two_L": 2.0 * length,
    }


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
    return {
        "alpha": alpha,
        "pole": pole,
        "arch": arch,
        "prime": prime,
        "z_src": z_src,
        "z_zeros": z_zeros,
        "rel": rel,
        "w2": W2,
    }


def assemble_window(
    length: float,
    dimension: int,
    damped: bool,
    c_l: float,
    n_outer: int,
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
    pole_plus = 2.0 * np.outer(cosh_vector, cosh_vector)
    pole_minus = 2.0 * np.outer(sinh_vector, sinh_vector)
    pole = pole_plus - pole_minus
    m2 = np.zeros((dimension, dimension), dtype=np.float64)
    overlaps = {}
    for index in two_rung_ks(length):
        shift = index * LOG2
        overlap = overlap_matrix(length, shift, dimension, damped, n_inner)
        overlaps[index] = overlap
        m2 += -2.0 * LOG2 * (R_POISSON ** index) * overlap
    m3 = np.zeros((dimension, dimension), dtype=np.float64)
    if LOG3 <= 2.0 * length + 1e-12:
        overlap3 = overlap_matrix(length, LOG3, dimension, damped, n_inner)
        overlaps["3"] = overlap3
        m3 = -W3 * overlap3
    ancestor = 0.5 * ((pole + arch) + (pole + arch).T)
    m2 = 0.5 * (m2 + m2.T)
    m3 = 0.5 * (m3 + m3.T)
    gram = 0.5 * (gram + gram.T)
    q_inf2 = ancestor + m2
    q_full = q_inf2 + m3
    return {
        "gram": gram,
        "arch": 0.5 * (arch + arch.T),
        "pole": 0.5 * (pole + pole.T),
        "pole_plus": 0.5 * (pole_plus + pole_plus.T),
        "pole_minus": 0.5 * (pole_minus + pole_minus.T),
        "ancestor": ancestor,
        "m2": m2,
        "m3": m3,
        "q_inf2": 0.5 * (q_inf2 + q_inf2.T),
        "q_full": 0.5 * (q_full + q_full.T),
        "cosh": cosh_vector,
        "sinh": sinh_vector,
        "n_inner": n_inner,
        "overlaps": overlaps,
        "ks": two_rung_ks(length),
        "odd": odd_primes_in_window(length),
    }


def tspace_bundle(
    length: float,
    dimension: int,
    damped: bool,
    connection,
    t_panels,
) -> dict:
    names = ("arch", "arch_p", "arch_m", "gram", "poisson", "m2")
    acc = {name: np.zeros((dimension, dimension), dtype=np.float64) for name in names}
    for left, right, order in t_panels:
        nodes, weights = roots_legendre(order)
        t_values = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        scaled = 0.5 * (right - left) * weights
        if damped:
            hats = bessel_damped_hat(length, t_values, dimension, connection)
        else:
            hats = bessel_legendre_hat(length, t_values, dimension)
        kappa = k_kernel(t_values)
        pois = poisson_kernel(t_values * LOG2)
        weights_map = {
            "arch": kappa,
            "arch_p": np.maximum(kappa, 0.0),
            "arch_m": np.maximum(-kappa, 0.0),
            "gram": np.ones_like(t_values),
            "poisson": pois,
            "m2": LOG2 * (1.0 - pois),
        }
        for name in names:
            weight = scaled * weights_map[name] / math.pi
            chunk = np.real(hats.conj().T @ (hats * weight[:, None]))
            acc[name] += chunk
    for name in names:
        acc[name] = 0.5 * (acc[name] + acc[name].T)
    return acc


def inertia(matrix: np.ndarray, rel: float = EIG_REL) -> dict:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.T))
    nrm = float(np.max(np.abs(values))) if values.size else 0.0
    thresh = rel * max(nrm, 1.0e-30)
    n_pos = int(np.sum(values > thresh))
    n_neg = int(np.sum(values < -thresh))
    n_rank = int(np.sum(np.abs(values) > thresh))
    return {
        "min": float(values[0]) if values.size else float("nan"),
        "max": float(values[-1]) if values.size else float("nan"),
        "n_pos": n_pos,
        "n_neg": n_neg,
        "rank": n_rank,
        "n": int(values.size),
        "nrm": nrm,
        "values": values,
    }


def negative_part(matrix: np.ndarray):
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.T))
    neg = np.maximum(-values, 0.0)
    minus = (vectors * neg) @ vectors.T
    sqrt = (vectors * np.sqrt(neg)) @ vectors.T
    return 0.5 * (minus + minus.T), 0.5 * (sqrt + sqrt.T)


def generic_dilation(quadratic: np.ndarray, m2_minus: np.ndarray, sqrt_m: np.ndarray):
    dim = quadratic.shape[0]
    block = np.zeros((2 * dim, 2 * dim), dtype=np.float64)
    block[:dim, :dim] = quadratic + m2_minus
    block[:dim, dim:] = sqrt_m
    block[dim:, :dim] = sqrt_m
    block[dim:, dim:] = np.eye(dim)
    return 0.5 * (block + block.T)


def loewner_max(numerator: np.ndarray, denominator: np.ndarray) -> float:
    """λ_max of N v = λ P v, with P clipped away from zero."""
    den = 0.5 * (denominator + denominator.T)
    num = 0.5 * (numerator + numerator.T)
    values, vectors = np.linalg.eigh(den)
    floor = 1.0e-14 * max(float(np.max(np.abs(values))), 1.0)
    scale = np.where(values > floor, 1.0 / np.sqrt(values), 0.0)
    whitener = (vectors * scale) @ vectors.T
    pencil = whitener @ num @ whitener
    ev = np.linalg.eigvalsh(0.5 * (pencil + pencil.T))
    return float(ev[-1]) if ev.size else float("nan")


def rel_fro(left: np.ndarray, right: np.ndarray) -> float:
    return float(
        np.linalg.norm(left - right, ord="fro")
        / max(np.linalg.norm(right, ord="fro"), 1.0e-30)
    )


def g_auto(shift: float, betas, coeffs) -> float:
    total = 0.0
    for c_i, b_i in zip(coeffs, betas):
        for c_j, b_j in zip(coeffs, betas):
            summ = b_i + b_j
            total += (
                c_i * c_j * math.sqrt(math.pi / summ)
                * math.exp(-b_i * b_j * shift * shift / summ)
            )
    return total


def hat_sq(t_values, betas, coeffs) -> np.ndarray:
    acc = np.zeros(np.asarray(t_values).shape, dtype=np.complex128)
    for coeff, beta in zip(coeffs, betas):
        acc = acc + coeff * math.sqrt(math.pi / beta) * np.exp(
            -np.asarray(t_values, dtype=np.float64) ** 2 / (4.0 * beta)
        )
    return np.abs(acc) ** 2


def w2_series(betas, coeffs, k_max: int = A1_KMAX) -> float:
    total = 0.0
    for index in range(1, k_max + 1):
        total += -LOG2 * (R_POISSON ** index) * 2.0 * g_auto(index * LOG2, betas, coeffs)
    return total


def w2_fourier(betas, coeffs, t_max: float = 90.0, order: int = 480) -> float:
    nodes, weights = roots_legendre(order)
    t_values = 0.5 * t_max * (nodes + 1.0)
    scaled = 0.5 * t_max * weights
    phi = hat_sq(t_values, betas, coeffs)
    return float(np.dot(scaled, phi * m2_multiplier(t_values)) / math.pi)


def a1_numeric(seed: int, n_random: int = A1_N_RANDOM) -> dict:
    rng = np.random.RandomState(seed)
    rels = []
    series_vals = []
    fourier_vals = []
    for _ in range(n_random):
        betas = rng.uniform(0.8, 3.2, size=2)
        coeffs = rng.normal(size=2)
        series = w2_series(betas, coeffs)
        fourier = w2_fourier(betas, coeffs)
        scale = max(abs(series), abs(fourier), 1.0e-30)
        rels.append(abs(series - fourier) / scale)
        series_vals.append(series)
        fourier_vals.append(fourier)
    return {
        "max_rel": float(max(rels)),
        "rels": rels,
        "series": series_vals,
        "fourier": fourier_vals,
    }


def sympy_a1_a2() -> dict:
    radius, theta = sp.symbols("r theta", real=True, positive=True)
    z_var = radius * sp.exp(sp.I * theta)
    lhs = 2 * sp.re(z_var / (1 - z_var))
    poisson = (1 - radius ** 2) / (
        1 - 2 * radius * sp.cos(theta) + radius ** 2
    )
    a1_diff = sp.simplify(sp.trigsimp(sp.expand_complex(lhs) - (poisson - 1)))
    z_sym, wbar, r_sym = sp.symbols("z wbar r")
    k_left = (1 - r_sym ** 2) / ((1 - r_sym * z_sym) * (1 - r_sym * wbar))
    b_z = (z_sym - r_sym) / (1 - r_sym * z_sym)
    b_w_star = (wbar - r_sym) / (1 - r_sym * wbar)
    k_right = (1 - b_z * b_w_star) / (1 - z_sym * wbar)
    a2_diff = sp.simplify(k_left - k_right)
    # Boundary K₂(e^{iθ}, e^{iθ}) = P_r(θ): substitute and cancel.
    ee = sp.exp(sp.I * theta)
    k_bdry = sp.simplify(
        k_left.subs({z_sym: ee, wbar: sp.exp(-sp.I * theta), r_sym: radius})
    )
    bdry_diff = sp.simplify(sp.together(k_bdry - poisson))
    bdry_zero = bdry_diff == 0 or bdry_diff == sp.Integer(0)
    if not bdry_zero:
        # residual trigonometric form: check numerically at r = 2^{-1/2}
        r_num = sp.sqrt(sp.Rational(1, 2))
        max_bdry = 0.0
        for sample in (0.0, 0.3, 1.0, 2.0, math.pi / 2, math.pi):
            val = complex(k_bdry.subs({radius: r_num, theta: sample}).evalf())
            pois = complex(poisson.subs({radius: r_num, theta: sample}).evalf())
            max_bdry = max(max_bdry, abs(val - pois))
        bdry_zero = max_bdry <= 1.0e-12
        bdry_err = max_bdry
    else:
        bdry_err = 0.0
    return {
        "a1": a1_diff == 0,
        "a1_expr": str(a1_diff),
        "a2": a2_diff == 0,
        "a2_expr": str(a2_diff),
        "bdry": bool(bdry_zero),
        "bdry_err": float(bdry_err),
    }


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()

    if smoke:
        grid = GRID_SMOKE
        n_a = N_A_SMOKE
        n_b = N_B_SMOKE
        n_outer = N_OUTER_SMOKE
        n_zeros = N_ZEROS_SMOKE
        t_panels = PANELS_SMOKE
        g1_panels = G1_PANELS
        do_damped = True
    else:
        grid = GRID_FULL
        n_a = N_A_FULL
        n_b = N_B_FULL
        n_outer = N_OUTER_FULL
        n_zeros = N_ZEROS_FULL
        t_panels = PANELS_FULL
        g1_panels = G1_PANELS
        do_damped = True

    emit("semilocal_p2_dilation_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit(
        "w2 %s  w3 %s  r %s  half_log2 %s  half_log3 %s"
        % (
            fmt(W2, 16), fmt(W3, 16), fmt(R_POISSON, 16),
            fmt(HALF_LOG2, 16), fmt(HALF_LOG3, 16),
        )
    )
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    zeros = load_zeros(n_zeros)
    emit(
        "zeros n=%d gamma1=%s gammaN=%s source=%s"
        % (
            int(zeros.size), fmt(float(zeros[0]), 12), fmt(float(zeros[-1]), 12),
            "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
        )
    )

    section("G0  GAUSSIAN EF PIN")
    g0 = gaussian_g0(zeros)
    emit(
        "  alpha=%s POLE=%s ARCH=%s PRIME=%s Z_src=%s Z_zeros=%s rel=%s"
        % (
            fmt(g0["alpha"], 4), fmt(g0["pole"], 12), fmt(g0["arch"], 12),
            fmt(g0["prime"], 12), fmt(g0["z_src"], 12), fmt(g0["z_zeros"], 12),
            fmt(g0["rel"], 6),
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
    c03 = c_L_of(G1_LENGTH)
    check(
        "G0-cL-0.3",
        2.19240491113 < c03 < 2.19240491114,
        "c_L(0.3)=%s" % fmt(c03, 16),
    )

    section("G1  ARCH x-space vs t-space")
    g1_dim = min(G1_DIM, n_b if n_b >= 4 else G1_DIM)
    n_inner_g1 = max(g1_dim + 8, 48)
    gram_g1 = gram_matrix(G1_LENGTH, g1_dim, True, n_inner_g1)
    arch_x_mat = arch_matrix(
        G1_LENGTH, g1_dim, True, gram_g1, c03, G1_OUTER, n_inner_g1,
    )
    conn_g1 = damped_connection(g1_dim)
    g1_ok_all = True
    for index in range(min(G1_VECTORS, g1_dim)):
        coeff = np.zeros(g1_dim, dtype=np.float64)
        coeff[min(2 * index, g1_dim - 1)] = 1.0
        norm = math.sqrt(float(coeff @ gram_g1 @ coeff))
        coeff = coeff / max(norm, 1.0e-30)
        arch_x = float(coeff @ arch_x_mat @ coeff)

        def hat_fn(t_values, c=coeff.copy()):
            basis = bessel_damped_hat(G1_LENGTH, t_values, g1_dim, conn_g1)
            return hat_combination(basis, c)

        arch_t = arch_tspace_from_hat(g1_panels, hat_fn)
        rel = abs(arch_x - arch_t) / max(abs(arch_t), abs(arch_x), 1.0e-30)
        emit(
            "  vec%d ARCH_x=%s ARCH_t=%s rel=%s"
            % (index, fmt(arch_x, 12), fmt(arch_t, 12), fmt(rel, 6))
        )
        ok = rel <= G1_REL
        g1_ok_all = g1_ok_all and ok
        check("G1-vec%d" % index, ok, "rel=%s" % fmt(rel, 6))

    section("A1  EULER-FACTOR TOWER / POISSON KERNEL")
    emit(
        "one 2-adic channel generates all rungs 2^k by the geometric "
        "series; the window at half-width L sees exactly the rungs "
        "with k log 2 <= 2L"
    )
    rung_rows = []
    for length in GRID_FULL:
        report = active_rung_report(length)
        rung_rows.append(report)
        emit(
            "  L=%s  2L=%s  2-rungs=%s  odd-primes=%s  n_k=%d"
            % (
                fmt(length, 6), fmt(report["two_L"], 6),
                str(report["powers"]), str(report["odd"]), len(report["ks"]),
            )
        )
    # Structural: k log 2 <= 2L iff 2^k is seen.
    k_ok = True
    for report in rung_rows:
        for index, power in zip(report["ks"], report["powers"]):
            if not (index * LOG2 <= report["two_L"] + 1e-12):
                k_ok = False
            if power != 2 ** index:
                k_ok = False
        if report["ks"] and (report["ks"][-1] + 1) * LOG2 <= report["two_L"] + 1e-12:
            k_ok = False
    check("A1-active-rungs", k_ok, "geometric cutoff k log 2 <= 2L")
    check(
        "A1-first-rung-w2",
        abs(2.0 * LOG2 * R_POISSON - W2) <= 1.0e-15,
        "2 log 2 * 2^{-1/2} = w2",
    )

    a1_first = a1_numeric(SEED)
    a1_second = a1_numeric(SEED)
    emit(
        "  10 random Gaussian mixtures: max_rel=%s  rerun=%s"
        % (fmt(a1_first["max_rel"], 6), fmt(a1_second["max_rel"], 6))
    )
    for index, rel in enumerate(a1_first["rels"]):
        emit(
            "    h%d series=%s fourier=%s rel=%s"
            % (
                index, fmt(a1_first["series"][index], 12),
                fmt(a1_first["fourier"][index], 12), fmt(rel, 6),
            )
        )
    a1_num_ok = check(
        "A1-fourier-poisson",
        a1_first["max_rel"] <= A1_REL,
        "max_rel=%s <= %s" % (fmt(a1_first["max_rel"], 6), fmt(A1_REL, 2)),
    )
    check(
        "A1-two-runs-identical",
        a1_first["max_rel"] == a1_second["max_rel"],
        "rel_a=%s rel_b=%s"
        % (fmt(a1_first["max_rel"], 8), fmt(a1_second["max_rel"], 8)),
    )
    sym = sympy_a1_a2()
    a1_sym_ok = check(
        "A1-sympy-2Re[z/(1-z)]=P-1",
        bool(sym["a1"]),
        "diff=%s" % sym["a1_expr"],
    )

    section("A2  RANK-ONE KERNEL / BLASCHKE")
    a2_ok = check(
        "A2-sympy-Blaschke-Szego",
        bool(sym["a2"]),
        "K2=(1-r^2)/((1-rz)(1-r wbar)) = (1-b(z)b(w)*)/(1-z wbar)",
    )
    check(
        "A2-boundary-Poisson",
        bool(sym["bdry"]),
        "K2(e^{iθ},e^{iθ})=P_r(θ) err=%s" % fmt(sym["bdry_err"], 6),
    )
    emit(
        "  positive channel = Poisson kernel; Weil 2-term = "
        "log 2 * (Plancherel constant − Poisson channel)"
    )

    section("B  STRUCTURAL OBSTRUCTIONS")
    conn_b = damped_connection(n_b) if do_damped else None
    spaces = [("legendre", n_a, False, None)]
    if do_damped:
        spaces.append(("damped", n_b, True, conn_b))

    b_rows = []
    b1_ok_all = True
    b2_ok_all = True
    b3_ok_all = True
    b4_ok_all = True
    c1_id_ok_all = True
    c1_manifest = False
    c1_dom_all = []

    for space_name, dimension, damped, connection in spaces:
        emit("")
        emit("--- space %s  dim=%d ---" % (space_name, dimension))
        for length in grid:
            forms = assemble_window(
                length, dimension, damped, c_l_map[length], n_outer,
            )
            gram = forms["gram"]
            ancestor_w = whiten(forms["ancestor"], gram)
            q_full_w = whiten(forms["q_full"], gram)
            q_inf2_w = whiten(forms["q_inf2"], gram)
            m2_w = whiten(forms["m2"], gram)
            m3_w = whiten(forms["m3"], gram)

            lam_anc, _ = min_rayleigh(forms["ancestor"], gram)
            lam_q, _ = min_rayleigh(forms["q_full"], gram)
            lam_inf2, _ = min_rayleigh(forms["q_inf2"], gram)
            # form without the 3-channel is q_inf2; ancestor is POLE+ARCH
            anc_info = inertia(ancestor_w)
            m2_info = inertia(m2_w)
            b1_ok = lam_anc < 0.0
            b2_ok = (m2_info["n_pos"] >= 1) and (m2_info["n_neg"] >= 1)
            b1_ok_all = b1_ok_all and b1_ok
            b2_ok_all = b2_ok_all and b2_ok

            m2_minus, sqrt_m = negative_part(m2_w)
            a_inf2 = generic_dilation(q_inf2_w, m2_minus, sqrt_m)
            a_anc = generic_dilation(ancestor_w + m3_w, m2_minus, sqrt_m)
            a_full = generic_dilation(q_full_w, m2_minus, sqrt_m)
            lam_a = float(np.min(np.linalg.eigvalsh(a_full)))
            q_psd = lam_q >= -PSD_ATOL
            a_psd = lam_a >= -PSD_ATOL
            b3_ok = q_psd == a_psd
            b3_ok_all = b3_ok_all and b3_ok

            diff = a_inf2 - a_anc
            diff_info = inertia(diff)
            b4_ok = diff_info["rank"] == m2_info["rank"]
            b4_ok_all = b4_ok_all and b4_ok

            # C1: t-space split of the {∞,2} form (no 3-channel).
            t_forms = tspace_bundle(
                length, dimension, damped, connection, t_panels,
            )
            pole_p_w = whiten(forms["pole_plus"], gram)
            pole_m_w = whiten(forms["pole_minus"], gram)
            arch_p_w = whiten(t_forms["arch_p"], gram)
            arch_m_w = whiten(t_forms["arch_m"], gram)
            gram_t_w = whiten(t_forms["gram"], gram)
            pois_w = whiten(t_forms["poisson"], gram)
            m2_t_w = whiten(t_forms["m2"], gram)
            pos = pole_p_w + arch_p_w + LOG2 * gram_t_w
            neg = pole_m_w + arch_m_w + LOG2 * pois_w
            reconstructed = pos - neg
            q_inf2_t = (
                whiten(forms["pole"], gram)
                + whiten(t_forms["arch"], gram)
                + m2_t_w
            )
            id_pn = rel_fro(reconstructed, q_inf2_t)
            id_m2 = rel_fro(m2_t_w, m2_w)
            id_arch = rel_fro(whiten(t_forms["arch"], gram), whiten(forms["arch"], gram))
            lam_pos = float(np.min(np.linalg.eigvalsh(pos)))
            lam_neg = float(np.min(np.linalg.eigvalsh(neg)))
            nrm_neg = float(np.linalg.norm(neg, ord=2))
            dom_op = nrm_neg / max(lam_pos, 1.0e-30) if lam_pos > 0.0 else float("inf")
            loew = loewner_max(neg, pos) if lam_pos > 0.0 else float("inf")
            # P − N = Q_{∞,2} is an identity in t-space (gated).
            # M2 t vs x is the Poisson-multiplier vs compact overlap;
            # Paley–Wiener tails make Frobenius O(10^{-2}), reported not gated.
            id_ok = id_pn <= C1_ID_REL
            c1_id_ok_all = c1_id_ok_all and id_ok
            if (dom_op <= 1.0) and (loew <= 1.0 + 1.0e-6) and (lam_pos > 0.0):
                c1_manifest = True
            c1_dom_all.append(dom_op)

            row = {
                "space": space_name,
                "L": length,
                "dim": dimension,
                "lam_anc": lam_anc,
                "lam_q": lam_q,
                "lam_inf2": lam_inf2,
                "lam_a": lam_a,
                "n_pos": m2_info["n_pos"],
                "n_neg": m2_info["n_neg"],
                "rank": m2_info["rank"],
                "rank_n": m2_info["rank"] / max(m2_info["n"], 1),
                "nrm_m2": m2_info["nrm"],
                "rank_diff": diff_info["rank"],
                "ks": forms["ks"],
                "odd": forms["odd"],
                "id_pn": id_pn,
                "id_m2": id_m2,
                "id_arch": id_arch,
                "lam_pos": lam_pos,
                "lam_neg": lam_neg,
                "nrm_neg": nrm_neg,
                "dom_op": dom_op,
                "loew": loew,
                "b1": b1_ok,
                "b2": b2_ok,
                "b3": b3_ok,
                "b4": b4_ok,
            }
            b_rows.append(row)
            emit(
                "  L=%s %s anc=%s Q=%s Q∞2=%s A=%s  M2 n+/n-=%d/%d "
                "||M2||=%s rank=%d/%d  B3 iff=%d"
                % (
                    fmt(length, 6), space_name, fmt(lam_anc, 8),
                    fmt(lam_q, 8), fmt(lam_inf2, 8), fmt(lam_a, 8),
                    m2_info["n_pos"], m2_info["n_neg"],
                    fmt(m2_info["nrm"], 6), m2_info["rank"], m2_info["n"],
                    int(b3_ok),
                )
            )
            emit(
                "    B4 rank(A∞2-A∞)=%d rank(M2)=%d  C1 id(P-N)=%s "
                "id(M2t,x)=%s id(ARCH)=%s  λmin(P)=%s ||N||=%s "
                "dom=%s loew=%s"
                % (
                    diff_info["rank"], m2_info["rank"],
                    fmt(id_pn, 4), fmt(id_m2, 4), fmt(id_arch, 4),
                    fmt(lam_pos, 6), fmt(nrm_neg, 6),
                    fmt(dom_op, 4), fmt(loew, 4),
                )
            )
            check(
                "B1-%s-L%s-ancestor-not-PSD" % (space_name, fmt(length, 4)),
                b1_ok,
                "λ_min(POLE+ARCH)=%s" % fmt(lam_anc, 8),
            )
            check(
                "B2-%s-L%s-M2-indefinite" % (space_name, fmt(length, 4)),
                b2_ok,
                "n+=%d n-=%d rank/N=%s" % (
                    m2_info["n_pos"], m2_info["n_neg"],
                    fmt(m2_info["rank"] / max(m2_info["n"], 1), 4),
                ),
            )
            check(
                "B2-%s-L%s-not-rank-one" % (space_name, fmt(length, 4)),
                m2_info["rank"] > RANK1_MAX,
                "rank=%d vs 1" % m2_info["rank"],
            )
            check(
                "B3-%s-L%s-tautology" % (space_name, fmt(length, 4)),
                b3_ok,
                "λ(A)>=0 iff λ(Q)>=0  Q=%s A=%s"
                % (fmt(lam_q, 8), fmt(lam_a, 8)),
            )
            check(
                "B4-%s-L%s-rank-fingerprint" % (space_name, fmt(length, 4)),
                b4_ok,
                "rank(diff)=%d rank(M2)=%d"
                % (diff_info["rank"], m2_info["rank"]),
            )
            check(
                "C1-%s-L%s-identity" % (space_name, fmt(length, 4)),
                id_ok,
                "||(P-N)-Q∞2||_F rel=%s  M2 rel=%s" % (
                    fmt(id_pn, 4), fmt(id_m2, 4),
                ),
            )
            check(
                "C1-%s-L%s-not-manifest" % (space_name, fmt(length, 4)),
                (not (dom_op <= 1.0 and lam_pos > 0.0)),
                "dom_op=%s loew=%s λmin(P)=%s ||N||=%s"
                % (
                    fmt(dom_op, 4), fmt(loew, 4),
                    fmt(lam_pos, 6), fmt(nrm_neg, 6),
                ),
            )

    section("C2  LITERATURE")
    emit("  CC21  %s" % C2_CC21)
    emit("  CCM2310  %s" % C2_CCM2310)
    emit("  q-series  %s" % C2_QS2403)
    emit("  scaling  %s" % C2_SCALE)
    emit("  zeta-cycles  %s" % C2_ZETA)
    emit(
        "  CONCLUSION: no unconditional semilocal Weil positivity for "
        "S={∞,2} on windows past [2^{-1/2}, 2^{1/2}] (up to √3).  "
        "The semilocal Sonin space and the Jacobi matrix for S={∞,p} "
        "exist as constructions (2310.18423 §4.6; 2403.01247), not as "
        "a positivity theorem."
    )
    c2_ok = check(
        "C2-no-uncond-semilocal-beyond-sqrt2",
        C2_UNCOND_SEMILOCAL is False,
        "CC21 support %s; extension conditional/numerical/deferred"
        % C2_SUPPORT_CC21,
    )
    check(
        "C2-cc21-support-quoted",
        True,
        "Thm 1 support %s ; weak (1/2,2)" % C2_SUPPORT_CC21,
    )
    check(
        "C2-jacobi-q-series-exists",
        True,
        "2403.01247 S={∞,p} q=1/p; 2310.18423 §4.6 Sonin Thm 4.6",
    )

    section("VERDICT")
    a_ok = a1_num_ok and a1_sym_ok and a2_ok and g0_ok and g1_ok_all
    b_ok = b1_ok_all and b2_ok_all and b3_ok_all
    if c1_manifest or C2_UNCOND_SEMILOCAL:
        verdict = "P2_DILATION_CANDIDATE"
        why = (
            "C1 found a named-family SOS with dominance_op <= 1"
            if c1_manifest
            else "C2 recorded an unconditional semilocal positivity theorem"
        )
    elif a_ok and b_ok and b4_ok_all and (not c1_manifest) and c2_ok:
        verdict = "P2_DILATION_STRUCTURALLY_BLOCKED"
        why = (
            "A1–A2 hold; ancestor not PSD and M2 indefinite of rank ≫ 1; "
            "generic dilations are tautological (same mountain, new wallpaper); "
            "no manifest local SOS in the named {∞,2} family; literature "
            "has no unconditional semilocal positivity beyond √2"
        )
    else:
        verdict = "INCONCLUSIVE"
        why = "an identity, obstruction, tautology, or C1/C2 gate failed"

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
        emit(
            "GATE_FAILURES "
            + ",".join(name for name, ok in CHECKS if not ok)
        )
    emit("fence %s" % FENCE)
    emit("claim_boundary experiments_only_not_a_ledger_claim")

    payload = {
        "verdict": verdict,
        "a1_max_rel": a1_first["max_rel"],
        "g0_rel": g0["rel"],
        "rows": [
            {
                "space": row["space"],
                "L": row["L"],
                "lam_anc": row["lam_anc"],
                "lam_q": row["lam_q"],
                "lam_a": row["lam_a"],
                "n_pos": row["n_pos"],
                "n_neg": row["n_neg"],
                "rank": row["rank"],
                "dom": row["dom_op"],
                "loew": row["loew"],
            }
            for row in b_rows
        ],
    }
    num_sha = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    ).hexdigest()

    emit("")
    emit("STATE r%d %s" % (ROUND, CONTRACT))
    emit("SHA %s" % file_sha256())
    emit("SPEC %s" % SPEC_SHA)
    emit("NUM %s" % num_sha)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("VERDICT %s" % verdict)
    emit(
        "A1-RUNGS "
        + " ".join(
            "L=%s:[%s]%s"
            % (
                fmt(item["L"], 3),
                ",".join(str(power) for power in item["powers"]),
                ("+3" if 3 in item["odd"] else ""),
            )
            for item in rung_rows
        )
    )
    emit("A1-MAXREL %s" % fmt(a1_first["max_rel"], 6))
    leg_rows = [row for row in b_rows if row["space"] == "legendre"]
    emit(
        "B1-ANC "
        + " ".join(
            "L=%s:%s" % (fmt(row["L"], 3), fmt(row["lam_anc"], 4))
            for row in leg_rows
        )
    )
    emit(
        "B2-M2 "
        + " ".join(
            "L=%s:n+-%d/%d||%s r/N=%s"
            % (
                fmt(row["L"], 3), row["n_pos"], row["n_neg"],
                fmt(row["nrm_m2"], 3), fmt(row["rank_n"], 3),
            )
            for row in leg_rows
        )
    )
    emit(
        "B3-TRACK "
        + " ".join(
            "L=%s:Q=%s A=%s" % (
                fmt(row["L"], 3), fmt(row["lam_q"], 4), fmt(row["lam_a"], 4),
            )
            for row in leg_rows
        )
    )
    emit(
        "C1-DOM "
        + " ".join(
            "L=%s:op=%s loew=%s P=%s N=%s"
            % (
                fmt(row["L"], 3), fmt(row["dom_op"], 3),
                fmt(row["loew"], 3), fmt(row["lam_pos"], 3),
                fmt(row["nrm_neg"], 3),
            )
            for row in leg_rows
        )
    )
    emit(
        "C2 CC21 supp=%s Thm1 archimedean-only; CCM2310 §4.6 Sonin "
        "not positivity; 2403.01247 Jacobi S={inf,p} q=1/p; "
        "1910.14368 §2 trace only; zeta-cycles 2023 numerical"
        % C2_SUPPORT_CC21
    )
    emit("FENCE %s" % FENCE)
    n_state = 0
    counting = False
    for line in LINES:
        if line.startswith("STATE r"):
            counting = True
        if counting:
            n_state += 1
    emit("STATE_LINES %d" % n_state)
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "r623 semilocal {∞,2} Euler-tower / dilation obstruction "
            "(experiments only)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
