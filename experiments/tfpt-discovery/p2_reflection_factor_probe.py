#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""p2_reflection_factor_probe -- r620  PRIME.P2.REFLECTION.FACTOR.01

Experiments-only scout of the prime-2 *reflection factor* on the odd
sector of the first-step window form (r615 machinery, copied not
imported).

For real h supported in [-L, L],

  Q_L(h) = POLE(h) + ARCH(h) − w₂ g_h(log 2)

with POLE = 2(⟨h, cosh(u/2)⟩² − ⟨h, sinh(u/2)⟩²), ARCH the v1017
x-space kernel k(x)=e^{x/2}/sinh(x) plus c_L, and
w₂ = √2 log 2.  Write A := POLE + ARCH (prime-free).

On the odd sector, d = log 2, I = [d−L, L] (nonempty for L > d/2,
and d−L > 0 for L < d).  With f = h|_I and (Rf)(x) = f(d−x)
(involution of I about d/2), f± = ½(f ± Rf),

  g_h(d) = ∫_I h(x) h(x−d) dx
         = −∫_I h(x) h(d−x) dx
         = −⟨f, R f⟩
         = −(‖f₊‖² − ‖f₋‖²).

Hence −w₂ g_h(d) = w₂(‖f₊‖² − ‖f₋‖²): prime 2 stabilizes the
R-symmetric edge sector and destabilizes the R-antisymmetric one.
The oriented statement is

  ⟨h, A^{odd} h⟩ + w₂(‖f₊‖² − ‖f₋‖²) ≥ 0   for all odd h,

which is Q_L on the odd sector (Weil, RH-consistent at these L).

Odd trial spaces: odd Legendre P_{2k+1} on [-L,L], plain and
edge-damped (1−(u/L)²)² P_{2k+1}, N_odd ≤ 60.  G0/G1 copied from
r615.  Finite-section arithmetic on a frozen L-grid.

Claim boundary: experiments only, not a ledger row, not a paper
claim.  Fence: "First-prime-step structure; window forms at these L
are RH-consistent; no RH claim."
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
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

ROUND = 620
SEED = 620202609
CONTRACT = "PRIME.P2.REFLECTION.FACTOR.01"
FENCE = (
    "First-prime-step structure; window forms at these L "
    "are RH-consistent; no RH claim."
)
LEMMA_RETYPE = (
    "for odd h: ⟨h, A^{odd} h⟩ + w₂(‖f₊‖² − ‖f₋‖²) ≥ 0, with the "
    "negative directions of A^{odd} confined to the R-symmetric edge sector"
)

LOG2 = math.log(2.0)
HALF_LOG2 = 0.5 * LOG2
W2 = math.sqrt(2.0) * LOG2
G0_ALPHA = 20.0
G0_REL = 1.0e-8
G1_REL = 1.0e-8
T1_REL = 1.0e-12
T2_ABS = 1.0e-12
T5_FLOOR = 1.0e-12
NEG_EIG = 1.0e-12
J_SPLIT = 0.5
MASS_PLUS_CUT = 0.95
N_T1_RANDOM = 20
N_ZEROS_FULL = 2000
N_ZEROS_SMOKE = 200

GRID_FULL = (0.36, 0.37, 0.38, 0.40, 0.43, 0.46, 0.49, 0.52, 0.549)
GRID_SMOKE = (0.36, 0.40, 0.52)
N_ODD_FULL = 60
N_ODD_SMOKE = 16
N_DAMP_FULL = 40
N_DAMP_SMOKE = 12
N_CONV_FULL = (20, 40, 60)
N_CONV_SMOKE = (8, 16)
N_STAR_FULL = 80
N_STAR_SMOKE = 24
N_OUTER_FULL = 80
N_OUTER_SMOKE = 48
G1_LENGTH = 0.30
G1_DIM = 12
G1_OUTER = 320

SPEC = {
    "round": ROUND,
    "tag": "r620",
    "contract": CONTRACT,
    "grid": list(GRID_FULL),
    "half_log2": HALF_LOG2,
    "w2": "sqrt(2)*log(2)",
    "g0_alpha": G0_ALPHA,
    "g0_rel": G0_REL,
    "g1_rel": G1_REL,
    "t1_rel": T1_REL,
    "t2_abs": T2_ABS,
    "t5_floor": T5_FLOOR,
    "j_split": J_SPLIT,
    "mass_plus_cut": MASS_PLUS_CUT,
    "n_t1_random": N_T1_RANDOM,
    "n_zeros": N_ZEROS_FULL,
    "n_odd": N_ODD_FULL,
    "n_damp": N_DAMP_FULL,
    "n_conv": list(N_CONV_FULL),
    "n_star": N_STAR_FULL,
    "n_outer": N_OUTER_FULL,
    "space_plain": "odd_legendre_P_{2k+1} on [-L,L]",
    "space_damped": "(1-(u/L)^2)^2 * odd_P",
    "pole": "2*(<h,cosh(u/2)>^2 - <h,sinh(u/2)>^2)",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "prime": "w2*g(log 2)",
    "identity": "g(d) = -(||f+||^2 - ||f-||^2) for odd h",
    "oriented": "<A odd> + w2 (||f+||^2 - ||f-||^2) >= 0",
    "seed": SEED,
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
    """Re ψ(1/4+it/2) − log π.  Copied Stirling/recurrence from r615/r608."""
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


def basis_values(
    points, length: float, dimension: int, damped: bool, parity: str = "all",
) -> np.ndarray:
    if parity == "odd":
        n_full = 2 * int(dimension)
        values = legendre_values(points, length, n_full)[:, 1::2]
    else:
        values = legendre_values(points, length, dimension)
    if not damped:
        return values
    return damped_weight(points, length)[:, None] * values


def gram_matrix(
    length: float, dimension: int, damped: bool, n_inner: int,
    parity: str = "all",
) -> np.ndarray:
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, damped, parity)
    gram = basis.T @ (scaled[:, None] * basis)
    return 0.5 * (gram + gram.T)


def pole_vectors(
    length: float, dimension: int, damped: bool, n_inner: int,
    parity: str = "all",
):
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, damped, parity)
    cosh_vector = basis.T @ (scaled * np.cosh(points / 2.0))
    sinh_vector = basis.T @ (scaled * np.sinh(points / 2.0))
    return cosh_vector, sinh_vector


def overlap_matrix(
    length: float,
    shift: float,
    dimension: int,
    damped: bool,
    n_inner: int,
    parity: str = "all",
) -> np.ndarray:
    two_l = 2.0 * length
    if shift <= 0.0 or shift >= two_l - 1.0e-15:
        return np.zeros((dimension, dimension), dtype=np.float64)
    overlap_length = two_l - shift
    nodes, weights = roots_legendre(n_inner)
    points = -length + 0.5 * overlap_length * (nodes + 1.0)
    scaled = 0.5 * overlap_length * weights
    left = basis_values(points, length, dimension, damped, parity)
    right = basis_values(points + shift, length, dimension, damped, parity)
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
    parity: str = "all",
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
        left = basis_values(points, length, dimension, damped, parity)
        right = basis_values(
            points + distance, length, dimension, damped, parity,
        )
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
    parity: str = "all",
) -> dict:
    deg = 2 * dimension if parity == "odd" else dimension
    n_inner = max(deg + 8, 48)
    if (not damped) and parity != "odd":
        gram = np.eye(dimension)
    elif (not damped) and parity == "odd":
        gram = np.eye(dimension)
    else:
        gram = gram_matrix(length, dimension, True, n_inner, parity)
    arch = arch_matrix(
        length, dimension, damped, gram, c_l, n_outer, n_inner, parity,
    )
    cosh_vector, sinh_vector = pole_vectors(
        length, dimension, damped, n_inner, parity,
    )
    pole = pole_matrix(cosh_vector, sinh_vector)
    overlap = overlap_matrix(
        length, shift, dimension, damped, n_inner, parity,
    )
    free = 0.5 * ((arch + pole) + (arch + pole).T)
    prime = (
        weight * overlap
        if include_prime and shift < 2.0 * length
        else np.zeros((dimension, dimension), dtype=np.float64)
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


def gen_eigh(quadratic, gram):
    quadratic = 0.5 * (quadratic + quadratic.T)
    gram = 0.5 * (gram + gram.T)
    identity = np.allclose(gram, np.eye(gram.shape[0]), atol=1.0e-10, rtol=0.0)
    if identity:
        values, vectors = np.linalg.eigh(quadratic)
        return np.asarray(values, dtype=np.float64), np.asarray(
            vectors, dtype=np.float64,
        )
    values, vectors = seigh(quadratic, gram, check_finite=False)
    return np.asarray(values, dtype=np.float64), np.asarray(
        vectors, dtype=np.float64,
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


def gaussian_g0(zeros: np.ndarray) -> dict:
    alpha = G0_ALPHA
    mp.mp.dps = 40
    a_mp = mp.mpf(alpha)
    pole = float((4 * mp.pi / a_mp) * mp.e ** (1 / (4 * a_mp)))

    def kappa_mp(t_val):
        return mp.re(mp.digamma(mp.mpf("0.25") + mp.j * t_val / 2)) - mp.log(
            mp.pi
        )

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


def _interval_quad(left: float, right: float, n_quad: int):
    nodes, weights = roots_legendre(n_quad)
    mid = 0.5 * (left + right)
    half = 0.5 * (right - left)
    points = mid + half * nodes
    scaled = half * weights
    return points, scaled


def _sym(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (matrix + matrix.T)


def sector_masses(
    length: float,
    dimension: int,
    damped: bool,
    n_quad: int,
    parity: str = "odd",
) -> dict:
    """L²[-L,L] compressions of inner / R-plus / R-minus for odd functions.

    I = [d−L, L], (Rf)(x) = f(d−x).  Three-panel Gram
    G = ∫_{|x|<a} + ∫_I + ∫_{−I}.  Full-line masses:
      M_in  = ∫_{|x|<a} φ_i φ_j
      M±    = 2 ∫_I φ_i^± φ_j^±     (odd extension of the edge)
    so M_in + M₊ + M₋ = G on the same panels.  I-only masses
    M±_I = ∫_I φ^± φ^± satisfy ⟨h, M±_I h⟩ = ‖f±‖² and
    Q = A + w₂ (M₊_I − M₋_I).
    """
    delta = LOG2
    inner_edge = delta - length
    zeros = np.zeros((dimension, dimension), dtype=np.float64)
    if inner_edge <= 1.0e-14 or length <= HALF_LOG2 + 1.0e-14:
        gram_l = gram_matrix(
            length, dimension, damped, max(n_quad, 48), parity,
        )
        return {
            "in": gram_l,
            "plus": zeros.copy(),
            "minus": zeros.copy(),
            "plus_I": zeros.copy(),
            "minus_I": zeros.copy(),
            "gram_3": gram_l,
            "overlap_shift": zeros.copy(),
            "overlap_odd": zeros.copy(),
            "a": inner_edge,
            "empty_I": True,
        }
    pts_in, w_in = _interval_quad(-inner_edge, inner_edge, n_quad)
    b_in = basis_values(pts_in, length, dimension, damped, parity)
    mass_in = _sym(b_in.T @ (w_in[:, None] * b_in))

    pts_i, w_i = _interval_quad(inner_edge, length, n_quad)
    b_i = basis_values(pts_i, length, dimension, damped, parity)
    b_r = basis_values(delta - pts_i, length, dimension, damped, parity)
    b_shift = basis_values(pts_i - delta, length, dimension, damped, parity)
    b_plus = 0.5 * (b_i + b_r)
    b_minus = 0.5 * (b_i - b_r)
    mass_plus_i = _sym(b_plus.T @ (w_i[:, None] * b_plus))
    mass_minus_i = _sym(b_minus.T @ (w_i[:, None] * b_minus))
    overlap_shift = _sym(b_i.T @ (w_i[:, None] * b_shift))
    overlap_odd = _sym(-(b_i.T @ (w_i[:, None] * b_r)))

    pts_neg, w_neg = _interval_quad(-length, -inner_edge, n_quad)
    b_neg = basis_values(pts_neg, length, dimension, damped, parity)
    mass_neg = _sym(b_neg.T @ (w_neg[:, None] * b_neg))
    mass_pos = _sym(b_i.T @ (w_i[:, None] * b_i))
    gram_3 = _sym(mass_in + mass_pos + mass_neg)
    return {
        "in": mass_in,
        "plus": 2.0 * mass_plus_i,
        "minus": 2.0 * mass_minus_i,
        "plus_I": mass_plus_i,
        "minus_I": mass_minus_i,
        "gram_3": gram_3,
        "overlap_shift": overlap_shift,
        "overlap_odd": overlap_odd,
        "a": inner_edge,
        "empty_I": False,
    }


def opnorm(matrix: np.ndarray) -> float:
    if matrix.size == 0:
        return 0.0
    return float(np.linalg.norm(matrix, ord=2))


def g_orthonormalize(columns: np.ndarray, gram: np.ndarray) -> np.ndarray:
    if columns.size == 0 or columns.shape[1] == 0:
        return np.zeros((gram.shape[0], 0), dtype=np.float64)
    metric = columns.T @ gram @ columns
    metric = 0.5 * (metric + metric.T)
    values, vectors = np.linalg.eigh(metric)
    keep = values > 1.0e-14
    if not np.any(keep):
        return np.zeros((gram.shape[0], 0), dtype=np.float64)
    whitened = columns @ vectors[:, keep] / np.sqrt(values[keep])
    return whitened


def spectral_split(operator, gram, plus_cut: float, minus_cut: float):
    values, vectors = gen_eigh(operator, gram)
    plus_idx = np.where(values > plus_cut)[0]
    minus_idx = np.where(values < minus_cut)[0]
    inner_idx = np.where((values <= plus_cut) & (values >= minus_cut))[0]
    q_plus = g_orthonormalize(vectors[:, plus_idx], gram)
    q_minus = g_orthonormalize(vectors[:, minus_idx], gram)
    q_inner = g_orthonormalize(vectors[:, inner_idx], gram)
    return {
        "values": values,
        "plus": q_plus,
        "minus": q_minus,
        "inner": q_inner,
        "n_plus": int(q_plus.shape[1]),
        "n_minus": int(q_minus.shape[1]),
        "n_inner": int(q_inner.shape[1]),
    }


def projector(columns: np.ndarray, gram: np.ndarray) -> np.ndarray:
    if columns.size == 0 or columns.shape[1] == 0:
        return np.zeros_like(gram)
    return columns @ (columns.T @ gram)


def subspace_eigh(quadratic, gram, columns: np.ndarray):
    if columns.size == 0 or columns.shape[1] == 0:
        return np.asarray([], dtype=np.float64), columns
    q_on = columns.T @ quadratic @ columns
    g_on = columns.T @ gram @ columns
    values, vectors = gen_eigh(q_on, g_on)
    return values, columns @ vectors


def schur_complement(quadratic, gram, q_plus, q_rest) -> dict:
    """Schur of the plus block onto the rest (minus+inner)."""
    empty = {
        "s_min": float("nan"),
        "a_pp_min": float("nan"),
        "a_rr_min": float("nan"),
        "cross": 0.0,
        "n_plus": 0,
        "n_rest": 0,
        "reading": "EMPTY",
    }
    n_plus = 0 if q_plus.size == 0 else q_plus.shape[1]
    n_rest = 0 if q_rest.size == 0 else q_rest.shape[1]
    if n_plus == 0 or n_rest == 0:
        empty["n_plus"] = n_plus
        empty["n_rest"] = n_rest
        if n_rest > 0:
            rest_vals, _ = subspace_eigh(quadratic, gram, q_rest)
            empty["a_rr_min"] = float(rest_vals[0]) if rest_vals.size else float("nan")
            empty["s_min"] = empty["a_rr_min"]
            empty["reading"] = "NO_PLUS_BLOCK"
        elif n_plus > 0:
            plus_vals, _ = subspace_eigh(quadratic, gram, q_plus)
            empty["a_pp_min"] = float(plus_vals[0]) if plus_vals.size else float("nan")
            empty["reading"] = "NO_REST_BLOCK"
        return empty
    a_pp = q_plus.T @ quadratic @ q_plus
    a_rr = q_rest.T @ quadratic @ q_rest
    a_pr = q_plus.T @ quadratic @ q_rest
    a_pp = 0.5 * (a_pp + a_pp.T)
    a_rr = 0.5 * (a_rr + a_rr.T)
    plus_vals = np.linalg.eigvalsh(a_pp)
    rest_vals = np.linalg.eigvalsh(a_rr)
    cross = opnorm(a_pr)
    try:
        schur = a_rr - a_pr.T @ np.linalg.solve(a_pp, a_pr)
        schur = 0.5 * (schur + schur.T)
        s_vals = np.linalg.eigvalsh(schur)
        s_min = float(s_vals[0])
    except np.linalg.LinAlgError:
        s_min = float("nan")
    a_pp_min = float(plus_vals[0])
    a_rr_min = float(rest_vals[0])
    if math.isfinite(s_min) and s_min >= -T5_FLOOR:
        reading = "PLUS_SCHUR_PSD_WITHOUT_PRIME"
    elif a_rr_min >= -T5_FLOOR:
        reading = "MINUS_BLOCK_PSD_COUPLING_OPTIONAL"
    else:
        reading = "COUPLING_MATTERS"
    return {
        "s_min": s_min,
        "a_pp_min": a_pp_min,
        "a_rr_min": a_rr_min,
        "cross": cross,
        "n_plus": n_plus,
        "n_rest": n_rest,
        "reading": reading,
    }


def analyze_odd(
    length: float,
    forms: dict,
    sectors: dict,
    n_conv: tuple[int, ...],
    rng: np.random.RandomState,
    tag: str,
) -> dict:
    gram = forms["gram"]
    arch = forms["free"]  # A = POLE + ARCH
    overlap = forms["overlap"]
    full_q = forms["full"]
    dim = gram.shape[0]
    mass_in = sectors["in"]
    mass_plus = sectors["plus"]
    mass_minus = sectors["minus"]
    mass_plus_i = sectors["plus_I"]
    mass_minus_i = sectors["minus_I"]

    gram_3 = sectors["gram_3"]
    overlap_shift = sectors["overlap_shift"]
    overlap_odd = sectors["overlap_odd"]
    residual = mass_in + mass_plus + mass_minus - gram_3
    t2_err = opnorm(residual)

    # T1: g(d)=∫_I h(x)h(x-d) vs −(‖f₊‖²−‖f₋‖²), 20 random odd h.
    # Both sides use the I-panel so the identity is the odd-extension
    # + reflection algebra, not a cross-quadrature artefact.
    t1_errs = []
    for _ in range(N_T1_RANDOM):
        coeff = rng.normal(size=dim)
        denom = math.sqrt(float(coeff @ gram @ coeff))
        coeff = coeff / max(denom, 1.0e-30)
        g_shift = float(coeff @ overlap_shift @ coeff)
        g_odd = float(coeff @ overlap_odd @ coeff)
        f_plus = float(coeff @ mass_plus_i @ coeff)
        f_minus = float(coeff @ mass_minus_i @ coeff)
        g_pm = -(f_plus - f_minus)
        scale = max(
            abs(g_shift), abs(g_odd), abs(g_pm),
            f_plus + f_minus, 1.0e-12,
        )
        t1_errs.append(
            max(abs(g_shift - g_odd), abs(g_shift - g_pm), abs(g_odd - g_pm))
            / scale
        )
    t1_max = max(t1_errs) if t1_errs else float("inf")
    ident = overlap_shift + (mass_plus_i - mass_minus_i)
    t1_mat = opnorm(ident) / max(opnorm(overlap_shift), opnorm(overlap), 1.0)

    a_vals, a_vecs = gen_eigh(arch, gram)
    neg_mask = a_vals < -NEG_EIG
    dim_em = int(np.count_nonzero(neg_mask))
    lam_min_a = float(a_vals[0])
    e_minus = a_vecs[:, neg_mask]
    if dim_em > 0:
        masses = []
        for index in range(dim_em):
            vec = a_vecs[:, index]
            nrm = float(vec @ gram @ vec)
            masses.append((
                float(vec @ mass_in @ vec) / nrm,
                float(vec @ mass_plus @ vec) / nrm,
                float(vec @ mass_minus @ vec) / nrm,
            ))
        mass_avg = tuple(float(np.mean([row[k] for row in masses])) for k in range(3))
        mass_minplus = min(row[1] for row in masses)
        mass_ground = masses[0]
    else:
        masses = []
        mass_avg = (0.0, 0.0, 0.0)
        mass_minplus = 1.0
        mass_ground = (0.0, 0.0, 0.0)

    # Spectral split of J = P₊ − P₋ (full-line compressions)
    j_op = mass_plus - mass_minus
    split = spectral_split(j_op, gram, J_SPLIT, -J_SPLIT)
    if split["n_minus"] == 0:
        split = spectral_split(j_op, gram, J_SPLIT, 0.0)

    q_plus = split["plus"]
    q_minus = split["minus"]
    q_inner = split["inner"]
    q_rest = (
        np.hstack([q_minus, q_inner])
        if q_inner.shape[1] or q_minus.shape[1]
        else np.zeros((dim, 0), dtype=np.float64)
    )
    if q_minus.shape[1] == 0 and q_inner.shape[1]:
        q_rest = q_inner
    elif q_minus.shape[1] and q_inner.shape[1] == 0:
        q_rest = q_minus

    p_minus_ref = projector(q_minus, gram)
    p_plus_ref = projector(q_plus, gram)
    p_arch = projector(e_minus, gram) if dim_em > 0 else np.zeros_like(gram)
    overlap_pm_arch = opnorm(p_minus_ref @ p_arch)

    if q_minus.shape[1] > 0:
        a_on_minus, minus_modes = subspace_eigh(arch, gram, q_minus)
        lam_g_minus = float(a_on_minus[0])
        h_star = minus_modes[:, 0]
        f_minus_star = float(h_star @ mass_minus_i @ h_star)
        a_star = float(h_star @ arch @ h_star)
        lam_i_minus = (
            a_star / f_minus_star if abs(f_minus_star) > 1.0e-18 else float("nan")
        )
    else:
        lam_g_minus = float("nan")
        lam_i_minus = float("nan")
        h_star = None
        f_minus_star = float("nan")
        a_star = float("nan")

    cross = opnorm(p_plus_ref @ arch @ p_minus_ref)

    q_oriented = arch + W2 * (mass_plus_i - mass_minus_i)
    q_oriented = 0.5 * (q_oriented + q_oriented.T)
    t5_from_blocks, _ = min_rayleigh(q_oriented, gram)
    t5_from_q, _ = min_rayleigh(full_q, gram)
    t5_match = abs(t5_from_blocks - t5_from_q)

    conv_a = []
    conv_dim = []
    for n_keep in n_conv:
        if n_keep > dim:
            continue
        vals_n, _ = gen_eigh(arch[:n_keep, :n_keep], gram[:n_keep, :n_keep])
        conv_a.append(float(vals_n[0]))
        conv_dim.append(int(np.count_nonzero(vals_n < -NEG_EIG)))

    schur_a = schur_complement(arch, gram, q_plus, q_rest)
    schur_q = schur_complement(full_q, gram, q_plus, q_rest)

    # T6: g>0 candidates in the antisymmetric sector / near E₋
    witnesses = []

    def consider(coeff, origin: str) -> None:
        nrm = float(coeff @ gram @ coeff)
        if nrm <= 1.0e-30:
            return
        coeff = coeff / math.sqrt(nrm)
        g_val = float(coeff @ overlap @ coeff)
        a_val = float(coeff @ arch @ coeff)
        witnesses.append({
            "origin": origin,
            "g": g_val,
            "a": a_val,
            "w2abs": W2 * abs(g_val),
            "gap": a_val - W2 * abs(g_val),
            "q": a_val - W2 * g_val,
        })

    if h_star is not None:
        consider(h_star, "lammin_A_on_Pminus")
    if dim_em > 0 and q_minus.shape[1] > 0:
        projected = p_minus_ref @ e_minus
        for col in range(projected.shape[1]):
            consider(projected[:, col], "Pminus_Eminus_%d" % col)
    minus_vals_m, minus_vecs_m = gen_eigh(mass_minus, gram)
    for col in range(min(4, minus_vals_m.size)):
        if minus_vals_m[-(col + 1)] < 1.0e-8:
            continue
        consider(minus_vecs_m[:, -(col + 1)], "top_Mminus_%d" % col)

    t6 = None
    for item in witnesses:
        if item["g"] > 1.0e-14 and item["a"] < item["w2abs"] - 1.0e-14:
            if t6 is None or item["gap"] < t6["gap"]:
                t6 = item
    if t6 is None and witnesses:
        # closest approach among g>0
        positive = [item for item in witnesses if item["g"] > 1.0e-14]
        if positive:
            t6_closest = min(positive, key=lambda item: item["gap"])
        else:
            t6_closest = min(witnesses, key=lambda item: item["gap"])
    else:
        t6_closest = t6

    return {
        "L": length,
        "tag": tag,
        "dim": dim,
        "t1_max": t1_max,
        "t1_mat": t1_mat,
        "t2_err": t2_err,
        "dim_em": dim_em,
        "lam_min_a": lam_min_a,
        "mass_avg": mass_avg,
        "mass_minplus": mass_minplus,
        "mass_ground": mass_ground,
        "n_plus": split["n_plus"],
        "n_minus": split["n_minus"],
        "n_inner": split["n_inner"],
        "j_vals": split["values"],
        "pm_arch": overlap_pm_arch,
        "lam_g_minus": lam_g_minus,
        "lam_i_minus": lam_i_minus,
        "lam_i_minus_w2": (
            lam_i_minus - W2 if math.isfinite(lam_i_minus) else float("nan")
        ),
        "cross": cross,
        "t5": t5_from_q,
        "t5_blocks": t5_from_blocks,
        "t5_match": t5_match,
        "conv_a": conv_a,
        "conv_dim": conv_dim,
        "schur_a": schur_a,
        "schur_q": schur_q,
        "t6": t6,
        "t6_closest": t6_closest,
        "a_vals": a_vals,
        "q_min": t5_from_q,
    }


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    started = time.time()
    rng = np.random.RandomState(SEED)

    if smoke:
        grid = GRID_SMOKE
        n_odd = N_ODD_SMOKE
        n_damp = N_DAMP_SMOKE
        n_conv = N_CONV_SMOKE
        n_star = N_STAR_SMOKE
        n_outer = N_OUTER_SMOKE
        n_zeros = N_ZEROS_SMOKE
        g1_vectors = 2
    else:
        grid = GRID_FULL
        n_odd = N_ODD_FULL
        n_damp = N_DAMP_FULL
        n_conv = N_CONV_FULL
        n_star = N_STAR_FULL
        n_outer = N_OUTER_FULL
        n_zeros = N_ZEROS_FULL
        g1_vectors = 3

    emit("p2_reflection_factor_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("w2 %s  half_log2 %s  d=log2 %s" % (
        fmt(W2, 16), fmt(HALF_LOG2, 16), fmt(LOG2, 16),
    ))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    zeros = load_zeros(n_zeros)
    emit("zeros n=%d gamma1=%s source=%s" % (
        int(zeros.size), fmt(float(zeros[0]), 12),
        "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
    ))

    section("G0  GAUSSIAN EF PIN")
    g0 = gaussian_g0(zeros)
    emit(
        "  alpha=%s POLE=%s ARCH=%s PRIME=%s Z_src=%s Z_zeros=%s rel=%s w2=%s"
        % (
            fmt(g0["alpha"], 4), fmt(g0["pole"], 12), fmt(g0["arch"], 12),
            fmt(g0["prime"], 12), fmt(g0["z_src"], 12), fmt(g0["z_zeros"], 12),
            fmt(g0["rel"], 6), fmt(g0["w2"], 12),
        )
    )
    check(
        "G0-EF-identity",
        g0["rel"] <= G0_REL,
        "rel=%s <= %s" % (fmt(g0["rel"], 6), fmt(G0_REL, 2)),
    )
    check(
        "G0-w2-pin",
        abs(g0["w2"] - W2) <= 1.0e-15,
        "w2=%s" % fmt(W2, 16),
    )

    lengths_needed = set(float(value) for value in grid)
    lengths_needed.add(G1_LENGTH)
    c_l_map = {float(length): c_L_of(length) for length in sorted(lengths_needed)}
    c03 = c_l_map[G1_LENGTH]
    check(
        "G0-cL-0.3",
        2.19240491113 < c03 < 2.19240491114,
        "c_L(0.3)=%s" % fmt(c03, 16),
    )

    section("G1  ARCH x-space vs t-space")
    g1_conn = damped_connection(G1_DIM)
    g1_forms = assemble_forms(
        G1_LENGTH, G1_DIM, True, c_l_map[G1_LENGTH], G1_OUTER, False,
        parity="all",
    )
    g1_ok_all = True
    for index in range(g1_vectors):
        coeff = np.zeros(G1_DIM, dtype=np.float64)
        coeff[min(2 * index, G1_DIM - 1)] = 1.0
        norm = math.sqrt(float(coeff @ g1_forms["gram"] @ coeff))
        coeff = coeff / max(norm, 1.0e-30)
        arch_x = float(coeff @ g1_forms["arch"] @ coeff)

        def hat_fn(t_values, c=coeff.copy()):
            basis = bessel_damped_hat(G1_LENGTH, t_values, G1_DIM, g1_conn)
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
            "  vec%d ARCH_x=%s ARCH_t=%s rel=%s"
            % (index, fmt(arch_x, 12), fmt(arch_t, 12), fmt(rel, 6))
        )
        ok = rel <= G1_REL
        g1_ok_all = g1_ok_all and ok
        check("G1-vec%d" % index, ok, "rel=%s" % fmt(rel, 6))
    check("G1-all", g1_ok_all, "n=%d" % g1_vectors)

    section("ODD SECTOR  A = POLE+ARCH  and oriented Q")
    rows = []
    n_quad = max(2 * n_odd + 32, 96)
    n_quad_d = max(4 * n_damp + 48, 160)

    for length in grid:
        c_l = c_l_map[length]
        forms_odd = assemble_forms(
            length, n_odd, False, c_l, n_outer, True, parity="odd",
        )
        sectors_odd = sector_masses(
            length, n_odd, False, n_quad, parity="odd",
        )
        row = analyze_odd(
            length, forms_odd, sectors_odd, n_conv, rng, "plain",
        )
        forms_star = assemble_forms(
            length, n_star, False, c_l, n_outer, True, parity="all",
        )
        lam_star, _ = min_rayleigh(forms_star["full"], forms_star["gram"])
        row["lam_star"] = lam_star
        row["t5_ratio"] = (
            row["t5"] / lam_star
            if abs(lam_star) > 1.0e-30 else float("nan")
        )
        forms_d = assemble_forms(
            length, n_damp, True, c_l, n_outer, True, parity="odd",
        )
        sectors_d = sector_masses(
            length, n_damp, True, n_quad_d, parity="odd",
        )
        row_d = analyze_odd(
            length, forms_d, sectors_d, n_conv[:2], rng, "damped",
        )
        row["damped"] = row_d
        rows.append(row)

        check(
            "T1-L%s" % fmt(length, 4),
            row["t1_max"] <= T1_REL,
            "maxrel=%s mat=%s" % (fmt(row["t1_max"], 6), fmt(row["t1_mat"], 6)),
        )
        check(
            "T2-L%s" % fmt(length, 4),
            row["t2_err"] <= T2_ABS,
            "||Pin+P++P--I||=%s n(+/-/in)=%d/%d/%d" % (
                fmt(row["t2_err"], 6),
                row["n_plus"], row["n_minus"], row["n_inner"],
            ),
        )
        check(
            "T5-L%s" % fmt(length, 4),
            row["t5"] >= -T5_FLOOR,
            "lminQ=%s blocks=%s match=%s ratio_star=%s" % (
                fmt(row["t5"], 12), fmt(row["t5_blocks"], 12),
                fmt(row["t5_match"], 6), fmt(row["t5_ratio"], 6),
            ),
        )
        check(
            "T1d-L%s" % fmt(length, 4),
            row_d["t1_max"] <= T1_REL,
            "damped maxrel=%s" % fmt(row_d["t1_max"], 6),
        )
        check(
            "T2d-L%s" % fmt(length, 4),
            row_d["t2_err"] <= T2_ABS,
            "damped ||sum-G||=%s" % fmt(row_d["t2_err"], 6),
        )
        check(
            "T5d-L%s" % fmt(length, 4),
            row_d["t5"] >= -T5_FLOOR,
            "damped lminQ=%s" % fmt(row_d["t5"], 12),
        )
        emit(
            "  L=%s dimE-=%d lminA=%s mass(in/+/−)=%s/%s/%s "
            "lminA|P−-w2=%s cross=%s T5=%s star=%s"
            % (
                fmt(length, 6), row["dim_em"], fmt(row["lam_min_a"], 12),
                fmt(row["mass_avg"][0], 6), fmt(row["mass_avg"][1], 6),
                fmt(row["mass_avg"][2], 6),
                fmt(row["lam_i_minus_w2"], 8), fmt(row["cross"], 8),
                fmt(row["t5"], 12), fmt(row["lam_star"], 12),
            )
        )
        emit(
            "    ground masses in/+/−=%s/%s/%s  min_+mass=%s  "
            "||P−Parch||=%s  conv_lmin=%s conv_dim=%s"
            % (
                fmt(row["mass_ground"][0], 6), fmt(row["mass_ground"][1], 6),
                fmt(row["mass_ground"][2], 6), fmt(row["mass_minplus"], 6),
                fmt(row["pm_arch"], 8),
                ",".join(fmt(val, 8) for val in row["conv_a"]),
                ",".join(str(val) for val in row["conv_dim"]),
            )
        )
        emit(
            "    T7 A: S=%s App=%s Arr=%s ||+A−||=%s  %s"
            % (
                fmt(row["schur_a"]["s_min"], 8),
                fmt(row["schur_a"]["a_pp_min"], 8),
                fmt(row["schur_a"]["a_rr_min"], 8),
                fmt(row["schur_a"]["cross"], 8),
                row["schur_a"]["reading"],
            )
        )
        emit(
            "    T7 Q: S=%s App=%s Arr=%s  %s  damped dimE-=%d lminA=%s"
            % (
                fmt(row["schur_q"]["s_min"], 8),
                fmt(row["schur_q"]["a_pp_min"], 8),
                fmt(row["schur_q"]["a_rr_min"], 8),
                row["schur_q"]["reading"],
                row_d["dim_em"], fmt(row_d["lam_min_a"], 12),
            )
        )

    section("T3–T4  NEGATIVE SPACE / FOUR NUMBERS")
    for row in rows:
        emit(
            "  L=%s  dimE-(Aodd)=%d  ||P−ref P−arch||=%s  "
            "lmin(A|P−)_I=%s  lmin-w2=%s  ||P+ A P−||=%s"
            % (
                fmt(row["L"], 6), row["dim_em"], fmt(row["pm_arch"], 8),
                fmt(row["lam_i_minus"], 12), fmt(row["lam_i_minus_w2"], 8),
                fmt(row["cross"], 8),
            )
        )
        check(
            "T4-Pminus-resolved-L%s" % fmt(row["L"], 4),
            row["n_minus"] >= 1 or row["L"] <= HALF_LOG2 + 0.02,
            "n_minus=%d j_min=%s" % (
                row["n_minus"],
                fmt(float(row["j_vals"][0]) if row["j_vals"].size else float("nan"), 6),
            ),
        )

    section("T6  |g| LEMMA RETYPE")
    t6_any = False
    t6_best = None
    for row in rows:
        item = row["t6"]
        closest = row["t6_closest"]
        if item is not None:
            t6_any = True
            if t6_best is None or item["gap"] < t6_best["gap"]:
                t6_best = dict(item)
                t6_best["L"] = row["L"]
            emit(
                "  WITNESS L=%s origin=%s g=%s A=%s w2|g|=%s A-w2|g|=%s Q=%s"
                % (
                    fmt(row["L"], 6), item["origin"], fmt(item["g"], 12),
                    fmt(item["a"], 12), fmt(item["w2abs"], 12),
                    fmt(item["gap"], 12), fmt(item["q"], 12),
                )
            )
        elif closest is not None:
            emit(
                "  no-witness L=%s closest origin=%s g=%s A=%s w2|g|=%s "
                "A-w2|g|=%s"
                % (
                    fmt(row["L"], 6), closest["origin"],
                    fmt(closest["g"], 12), fmt(closest["a"], 12),
                    fmt(closest["w2abs"], 12), fmt(closest["gap"], 12),
                )
            )
        else:
            emit("  no-candidate L=%s" % fmt(row["L"], 6))
    if t6_any:
        emit(
            "  |g|-lemma FALSE as stated on antisymmetric sector "
            "(witness A < w2|g| with g>0)"
        )
    else:
        emit(
            "  no A < w2|g| with g>0 in the trial section; the |g| form "
            "fails as a *statement of Q* because Q uses signed "
            "(‖f₊‖²−‖f₋‖²), not |g| — on g>0 the prime HURTS"
        )

    section("T7  2x2 SCHUR")
    readings = [row["schur_a"]["reading"] for row in rows]
    for row in rows:
        emit(
            "  L=%s  A: %s S=%s  Q: %s S=%s  cross_A=%s"
            % (
                fmt(row["L"], 6),
                row["schur_a"]["reading"], fmt(row["schur_a"]["s_min"], 8),
                row["schur_q"]["reading"], fmt(row["schur_q"]["s_min"], 8),
                fmt(row["schur_a"]["cross"], 8),
            )
        )
    if all(item == "PLUS_SCHUR_PSD_WITHOUT_PRIME" for item in readings):
        t7_global = "PLUS_SCHUR_PSD_WITHOUT_PRIME"
    elif all(
        item in ("PLUS_SCHUR_PSD_WITHOUT_PRIME", "MINUS_BLOCK_PSD_COUPLING_OPTIONAL")
        for item in readings
    ):
        t7_global = "MINUS_SAFE_PLUS_CARRIES"
    else:
        t7_global = "COUPLING_MATTERS"
    emit("  T7-global %s" % t7_global)

    section("VERDICT")
    t1_ok = all(ok for name, ok in CHECKS if name.startswith("T1-L"))
    t2_ok = all(ok for name, ok in CHECKS if name.startswith("T2-L"))
    t5_ok = all(ok for name, ok in CHECKS if name.startswith("T5-L"))
    check("T1-all-plain", t1_ok, "identity g=-(||f+||^2-||f-||^2)")
    check("T2-all-plain", t2_ok, "Pin+P++P-=I")
    check("T5-all-plain", t5_ok, "oriented Q>=0")

    high = [row for row in rows if row["L"] >= 0.38 - 1.0e-12]
    plus_mass_ok = True
    minus_safe_ok = True
    for row in high:
        if row["dim_em"] == 0:
            continue
        if not (row["mass_minplus"] >= MASS_PLUS_CUT):
            plus_mass_ok = False
        if not (
            math.isfinite(row["lam_i_minus"]) and row["lam_i_minus"] >= W2 - 1.0e-8
        ):
            minus_safe_ok = False
    if not t1_ok or not t2_ok or not t5_ok:
        verdict = "INCONCLUSIVE"
        why = "T1/T2/T5 failed"
    elif high and plus_mass_ok and minus_safe_ok:
        verdict = "REFLECTION_SYMMETRIC_REPAIR"
        why = (
            "for L>=0.38, E_-(Aodd) has >=0.95 mass in Ran P+^ref "
            "and lmin(A|P-) >= w2"
        )
    else:
        verdict = "MIXED_SECTOR"
        why = "negative mass not confined to P+ and/or antisymmetric sector not >= w2"

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    if verdict == "REFLECTION_SYMMETRIC_REPAIR":
        emit("LEMMA %s" % LEMMA_RETYPE)
    emit("T7 %s" % t7_global)
    if t6_best is not None:
        emit(
            "T6 WITNESS L=%s origin=%s g=%s A=%s w2|g|=%s gap=%s"
            % (
                fmt(t6_best["L"], 6), t6_best["origin"],
                fmt(t6_best["g"], 12), fmt(t6_best["a"], 12),
                fmt(t6_best["w2abs"], 12), fmt(t6_best["gap"], 12),
            )
        )
    else:
        emit("T6 WITNESS none")
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    elapsed = time.time() - started
    print("TIME_S %s" % fmt(elapsed, 4), file=sys.stderr)
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    section("STATE")
    emit("STATE r%d %s" % (ROUND, CONTRACT))
    emit("SHA %s" % file_sha256())
    emit("SPEC %s" % SPEC_SHA)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("VERDICT %s" % verdict)
    emit(
        "L dimE- lminA massIn/+/- lminA|P--w2 cross T5"
    )
    for row in rows:
        emit(
            "%s %d %s %s/%s/%s %s %s %s"
            % (
                fmt(row["L"], 4), row["dim_em"], fmt(row["lam_min_a"], 6),
                fmt(row["mass_avg"][0], 4), fmt(row["mass_avg"][1], 4),
                fmt(row["mass_avg"][2], 4),
                fmt(row["lam_i_minus_w2"], 6), fmt(row["cross"], 6),
                fmt(row["t5"], 6),
            )
        )
    if t6_best is not None:
        emit(
            "T6 L=%s %s g=%s A-w2|g|=%s"
            % (
                fmt(t6_best["L"], 4), t6_best["origin"],
                fmt(t6_best["g"], 6), fmt(t6_best["gap"], 6),
            )
        )
    else:
        emit("T6 none")
    emit("T7 %s" % t7_global)
    emit("FENCE %s" % FENCE)
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r620 prime-2 reflection-factor odd-sector scout "
                    "(experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
