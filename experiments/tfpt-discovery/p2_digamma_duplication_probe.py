#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""p2_digamma_duplication_probe -- r621  PRIME.P2.DIGAMMA.DUPLICATION.01

Experiments-only scout: is the prime-2 repair of the odd Weil sector
(r615 T9) an exact *duplication factor* of the archimedean operator,
or only an identity-constant cousin of the duplication formula?

Digamma duplication
  ψ(z) + ψ(z+1/2) = 2 ψ(2z) − 2 log 2
at z = 1/4 + i t/2 reads
  Re ψ(1/4+it/2) + Re ψ(3/4+it/2) = 2 Re ψ(1/2+it) − 2 log 2.

Window form (copied r615): for real h supported in [-L, L],
  Q_L(h) = POLE(h) + ARCH(h) − w₂ g_h(log 2)
with w₂ = √2 log 2, g the autocorrelation, and ARCH the t-space
multiplier (1/2π)∫ |ĥ|² (Re ψ(1/4+it/2) − log π) dt (G1 cross-checks
the v1017 x-space kernel).  Three archimedean channels:

  ARCH_1/4  : Re ψ(1/4+it/2) − log π     (Γ_ℝ(s), ζ)
  ARCH_3/4  : Re ψ(3/4+it/2) − log π     (Γ_ℝ(s+1), odd/χ)
  ARCH_ℂ    : 2 Re ψ(1/2+it) − 2 log π   (Λ_K conductor-inclusive)

Operator identity (T2):  ARCH_1/4 = ARCH_ℂ − ARCH_3/4 − 2 log 2 · G.
The constant −2 log 2 is a multiple of the identity.  The prime-2
term is the translation P₂ := −w₂ T_{log 2}.  Parent caution: those
are different operators; the translation lives in the *multiplicative*
identity through 2^{−s}, i.e. in ζ_{ℚ(i)} = ζ L(s, χ_{-4}) as the
ramified prime (1+i) of norm 2.

T4 is a structural comparison of the windowed Weil form of ζ_{ℚ(i)},
not a proof step.  χ_{-4} zeros are not in mpmath and are not cached
here; T4 is prime-side only.

Claim boundary: finite-section arithmetic on a frozen L-grid.
Not a ledger row.  Not a paper claim.
Fence: Archimedean identities; window forms at these L are
RH-consistent; no RH claim.
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

ROUND = 621
SEED = 621202609
CONTRACT = "PRIME.P2.DIGAMMA.DUPLICATION.01"
LOG2 = math.log(2.0)
LOG3 = math.log(3.0)
LOGPI = math.log(math.pi)
LOG2PI = math.log(2.0 * math.pi)
HALF_LOG2 = 0.5 * LOG2
HALF_LOG3 = 0.5 * LOG3
W2 = math.sqrt(2.0) * LOG2
W2_K = 2.0 * LOG2 * math.sqrt(0.5)  # 2 log 2 * 2^{-1/2}
RESIDUE_K = 0.25 * math.pi  # Res_{s=1} ζ_{ℚ(i)} = π/4
G0_ALPHA = 20.0
G0_REL = 1.0e-8
G1_REL = 1.0e-8
T1_ATOL = 1.0e-13
T1_N_FULL = 2000
T1_N_SMOKE = 400
T1_TMAX = 200.0
T1_DPS = 25
T2_REL = 1.0e-9
T3_CAND = 1.0e-6
T3_CONST = 0.1
T3_TINY = 1.0e-8
EIG_NEG = -1.0e-10
N_ZEROS_FULL = 2000
N_ZEROS_SMOKE = 200
L_FULL = (0.40, 0.46, 0.52, 0.549)
L_SMOKE = (0.40, 0.52)
T4_L_EXTRA_FULL = (0.30, 0.34, 0.37, 0.38)
T4_L_EXTRA_SMOKE = (0.38,)
N_ODD_FULL = 40
N_ODD_SMOKE = 12
N_FULL_FULL = 40
N_FULL_SMOKE = 12
N_G1_FULL = 12
N_G1_SMOKE = 12
N_OUTER_G1_FULL = 320
N_OUTER_G1_SMOKE = 320
PANELS_FULL = (
    (0.0, 20.0, 128),
    (20.0, 80.0, 128),
    (80.0, 400.0, 160),
    (400.0, 2500.0, 128),
)
PANELS_SMOKE = (
    (0.0, 40.0, 64),
    (40.0, 200.0, 64),
    (200.0, 800.0, 64),
)
G1_PANELS = PANELS_FULL

SPEC = {
    "round": ROUND,
    "tag": "r621",
    "contract": CONTRACT,
    "grid": list(L_FULL),
    "half_log2": HALF_LOG2,
    "half_log3": HALF_LOG3,
    "w2": "sqrt(2)*log(2)",
    "w2_K": "2*log(2)*2**(-1/2)",
    "residue_K": "pi/4",
    "pole_K": "weil_logderiv_same_as_zeta_not_times_residue",
    "g0_alpha": G0_ALPHA,
    "g0_rel": G0_REL,
    "g1_rel": G1_REL,
    "t1_atol": T1_ATOL,
    "t1_n": T1_N_FULL,
    "t1_tmax": T1_TMAX,
    "t2_rel": T2_REL,
    "t3_cand": T3_CAND,
    "t3_const": T3_CONST,
    "n_odd": N_ODD_FULL,
    "n_full": N_FULL_FULL,
    "arch_q": "Re psi(1/4+it/2)-log pi",
    "arch_tq": "Re psi(3/4+it/2)-log pi",
    "arch_C": "2 Re psi(1/2+it)-2 log pi",
    "arch_GammaC": "2 Re psi(1/2+it)-2 log(2pi)",
    "identity": "ARCH_q = ARCH_C - ARCH_tq - 2 log 2 * G",
    "P2": "-w2 * T_{log 2}",
    "t3": "lstsq P2 ~ a ARCH_tq + b G on E- and on odd space",
    "t4_zero_side": "skipped_no_chi_m4_zeros",
    "seed": SEED,
    "space_odd": "odd Legendre P_{2k+1} and edge-damped",
    "claim_boundary": "experiments_only_not_a_ledger_claim",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
STATE: list[str] = []


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


def psi_real(x0: float, y_values, n_rec: int = 80, r2_min: float = 100.0) -> np.ndarray:
    """Re ψ(x0 + i y).  Copied Stirling/recurrence from r615 k_kernel."""
    y_val = np.asarray(y_values, dtype=np.float64)
    x_val = np.full_like(y_val, float(x0), dtype=np.float64)
    acc = np.zeros_like(y_val)
    for _ in range(n_rec):
        r2 = x_val * x_val + y_val * y_val
        need = r2 < r2_min
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
    return (
        log_re
        - 0.5 * inv_re
        - (1.0 / 12.0) * inv2_re
        + (1.0 / 120.0) * inv4_re
        - (1.0 / 252.0) * inv6_re
        + (1.0 / 240.0) * inv8_re
        - (1.0 / 132.0) * inv10_re
        + acc
    )


def k_kernel(t_values) -> np.ndarray:
    """Re ψ(1/4 + i t/2) − log π.  r615 ARCH_1/4 multiplier."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    return psi_real(0.25, 0.5 * t_arr) - LOGPI


def kappa_quarter(t_values) -> np.ndarray:
    return k_kernel(t_values)


def kappa_three_quarter(t_values) -> np.ndarray:
    t_arr = np.asarray(t_values, dtype=np.float64)
    return psi_real(0.75, 0.5 * t_arr) - LOGPI


def kappa_complex(t_values) -> np.ndarray:
    """2 Re ψ(1/2 + i t) − 2 log π  (Λ_K, conductor inside the arch factor)."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    return 2.0 * psi_real(0.5, t_arr) - 2.0 * LOGPI


def kappa_gammac(t_values) -> np.ndarray:
    """2 Re ψ(1/2 + i t) − 2 log(2π)  (Γ_ℂ only, no |d|^{s/2})."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    return 2.0 * psi_real(0.5, t_arr) - 2.0 * LOG2PI


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


def chi_m4(n: int) -> int:
    residue = n % 4
    if residue == 1:
        return 1
    if residue == 3:
        return -1
    return 0


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


def spatial_blocks(length: float, dimension: int, damped: bool) -> dict:
    n_inner = max(dimension + 8, 48)
    gram = (
        np.eye(dimension)
        if not damped
        else gram_matrix(length, dimension, True, n_inner)
    )
    cosh_vector, sinh_vector = pole_vectors(length, dimension, damped, n_inner)
    pole = pole_matrix(cosh_vector, sinh_vector)
    overlap = overlap_matrix(length, LOG2, dimension, damped, n_inner)
    gram = 0.5 * (gram + gram.T)
    return {
        "gram": gram,
        "pole": 0.5 * (pole + pole.T),
        "overlap": 0.5 * (overlap + overlap.T),
        "cosh": cosh_vector,
        "sinh": sinh_vector,
        "n_inner": n_inner,
    }


def extract(block: np.ndarray, indices: np.ndarray) -> np.ndarray:
    return np.asarray(block[np.ix_(indices, indices)], dtype=np.float64)


def tspace_arch_bundle(
    length: float,
    n_max: int,
    indices: np.ndarray,
    damped: bool,
    connection,
    t_panels,
) -> dict:
    dim = int(indices.size)
    names = ("q", "tq", "c", "gc", "pl")
    acc = {name: np.zeros((dim, dim), dtype=np.float64) for name in names}

    def kappa_one(t_values):
        return np.ones_like(np.asarray(t_values, dtype=np.float64))

    kappas = {
        "q": kappa_quarter,
        "tq": kappa_three_quarter,
        "c": kappa_complex,
        "gc": kappa_gammac,
        "pl": kappa_one,
    }
    for left, right, order in t_panels:
        nodes, weights = roots_legendre(order)
        t_values = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        scaled = 0.5 * (right - left) * weights
        if damped:
            hats_full = bessel_damped_hat(length, t_values, n_max, connection)
        else:
            hats_full = bessel_legendre_hat(length, t_values, n_max)
        hats = hats_full[:, indices]
        for name in names:
            weight = scaled * kappas[name](t_values) / math.pi
            chunk = np.real(hats.conj().T @ (hats * weight[:, None]))
            acc[name] += chunk
    for name in names:
        acc[name] = 0.5 * (acc[name] + acc[name].T)
    return acc


def g_invsqrt(gram: np.ndarray) -> np.ndarray:
    gram = 0.5 * (gram + gram.T)
    values, vectors = np.linalg.eigh(gram)
    values = np.maximum(values, 0.0)
    scale = np.where(values > 1.0e-14, 1.0 / np.sqrt(values), 0.0)
    return (vectors * scale) @ vectors.T


def whiten(operator: np.ndarray, gram: np.ndarray) -> np.ndarray:
    whitener = g_invsqrt(gram)
    out = whitener @ operator @ whitener
    return 0.5 * (out + out.T)


def fro(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord="fro"))


def rel_fro(numer: np.ndarray, denom: np.ndarray) -> float:
    scale = fro(denom)
    if scale <= 1.0e-30:
        return float("inf")
    return fro(numer) / scale


def fit_alpha_beta(p2: np.ndarray, arch_tq: np.ndarray, gram: np.ndarray):
    """HS-fit P2 ≈ α ARCH_3/4 + β G after G-whitening.  Returns α, β, rel."""
    p_w = whiten(p2, gram)
    a_w = whiten(arch_tq, gram)
    identity = np.eye(p_w.shape[0], dtype=np.float64)
    design = np.column_stack((a_w.ravel(), identity.ravel()))
    target = p_w.ravel()
    coef, _, _, _ = np.linalg.lstsq(design, target, rcond=None)
    alpha, beta = float(coef[0]), float(coef[1])
    residual = p_w - alpha * a_w - beta * identity
    return alpha, beta, rel_fro(residual, p_w)


def g_orthonormalize(columns: np.ndarray, gram: np.ndarray, tol: float = 1.0e-10):
    if columns.size == 0 or columns.shape[1] == 0:
        return np.zeros((gram.shape[0], 0), dtype=np.float64)
    sqrtg_inv = g_invsqrt(gram)
    values, vectors = np.linalg.eigh(0.5 * (gram + gram.T))
    values = np.maximum(values, 0.0)
    scale = np.sqrt(values)
    sqrtg = (vectors * scale) @ vectors.T
    euclidean = sqrtg @ columns
    q_mat, r_mat = np.linalg.qr(euclidean, mode="reduced")
    diag = np.abs(np.diag(r_mat)) if r_mat.size else np.zeros(0)
    if diag.size == 0:
        return np.zeros((gram.shape[0], 0), dtype=np.float64)
    keep = diag > tol * max(float(diag.max()), 1.0)
    if not np.any(keep):
        return np.zeros((gram.shape[0], 0), dtype=np.float64)
    return sqrtg_inv @ q_mat[:, keep]


def fit_on_subspace(
    p2: np.ndarray,
    arch_tq: np.ndarray,
    gram: np.ndarray,
    basis: np.ndarray,
):
    if basis.size == 0 or basis.shape[1] == 0:
        return float("nan"), float("nan"), float("nan"), 0
    p_v = basis.T @ p2 @ basis
    a_v = basis.T @ arch_tq @ basis
    g_v = basis.T @ gram @ basis
    alpha, beta, rel = fit_alpha_beta(p_v, a_v, g_v)
    return alpha, beta, rel, int(basis.shape[1])


def gen_eigvals(operator: np.ndarray, gram: np.ndarray) -> np.ndarray:
    operator = 0.5 * (operator + operator.T)
    gram = 0.5 * (gram + gram.T)
    identity = np.allclose(gram, np.eye(gram.shape[0]), atol=1.0e-10, rtol=0.0)
    if identity:
        values, _vectors = np.linalg.eigh(operator)
        return np.asarray(values, dtype=np.float64)
    values, _vectors = seigh(operator, gram, check_finite=False)
    return np.asarray(values, dtype=np.float64)


def gen_eigh(operator: np.ndarray, gram: np.ndarray):
    operator = 0.5 * (operator + operator.T)
    gram = 0.5 * (gram + gram.T)
    identity = np.allclose(gram, np.eye(gram.shape[0]), atol=1.0e-10, rtol=0.0)
    if identity:
        values, vectors = np.linalg.eigh(operator)
        return np.asarray(values, dtype=np.float64), np.asarray(vectors, dtype=np.float64)
    values, vectors = seigh(operator, gram, check_finite=False)
    return np.asarray(values, dtype=np.float64), np.asarray(vectors, dtype=np.float64)


def min_rayleigh(quadratic, gram) -> tuple[float, np.ndarray]:
    values, vectors = gen_eigh(quadratic, gram)
    return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)


def hs_cos(left: np.ndarray, right: np.ndarray, gram: np.ndarray) -> float:
    a_w = whiten(left, gram)
    b_w = whiten(right, gram)
    num = float(np.vdot(a_w.ravel(), b_w.ravel()).real)
    den = fro(a_w) * fro(b_w)
    if den <= 1.0e-30:
        return float("nan")
    return num / den


def spectral_pack(values: np.ndarray) -> dict:
    if values.size == 0:
        return {
            "min": float("nan"), "max": float("nan"),
            "n_neg": 0, "n_pos": 0, "n_tiny": 0, "n": 0,
        }
    scale = max(1.0, float(np.max(np.abs(values))))
    tiny = T3_TINY * scale
    return {
        "min": float(values[0]),
        "max": float(values[-1]),
        "n_neg": int(np.sum(values < EIG_NEG)),
        "n_pos": int(np.sum(values > -EIG_NEG)),
        "n_tiny": int(np.sum(np.abs(values) < tiny)),
        "n": int(values.size),
    }


def t1_duplication(n_pts: int, t_max: float, dps: int) -> dict:
    mp.mp.dps = int(dps)
    grid = np.linspace(0.0, float(t_max), int(n_pts))
    two_log2 = 2 * mp.log(mp.mpf(2))
    max_err = 0.0
    argmax_t = 0.0
    for t_val in grid:
        z_val = mp.mpf("0.25") + mp.j * mp.mpf(t_val) / 2
        lhs = mp.re(mp.digamma(z_val)) + mp.re(mp.digamma(z_val + mp.mpf("0.5")))
        rhs = 2 * mp.re(mp.digamma(mp.mpf("0.5") + mp.j * mp.mpf(t_val))) - two_log2
        err = abs(float(lhs - rhs))
        if err >= max_err:
            max_err = err
            argmax_t = float(t_val)
    return {"max_err": max_err, "argmax_t": argmax_t, "n": int(n_pts)}


def gaussian_g0(zeros: np.ndarray) -> dict:
    """r615 Gaussian EF pin, ARCH via the numpy digamma kernel (same identity)."""
    alpha = G0_ALPHA
    pole = (4.0 * math.pi / alpha) * math.exp(1.0 / (4.0 * alpha))
    panels = (
        (0.0, 20.0, 160),
        (20.0, 80.0, 160),
        (80.0, 400.0, 160),
        (400.0, 2500.0, 128),
    )
    arch = 0.0
    nrm = 0.0
    arch_tq = 0.0
    arch_c = 0.0
    arch_gc = 0.0
    for left, right, order in panels:
        nodes, weights = roots_legendre(order)
        t_values = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        scaled = 0.5 * (right - left) * weights
        gauss = np.exp(-(t_values * t_values) / alpha)
        # full line, even integrand: (2/α) ∫_0^∞ exp(-t²/α) κ(t) dt
        pref = 2.0 / alpha
        arch += float(pref * np.dot(scaled, gauss * kappa_quarter(t_values)))
        arch_tq += float(pref * np.dot(scaled, gauss * kappa_three_quarter(t_values)))
        arch_c += float(pref * np.dot(scaled, gauss * kappa_complex(t_values)))
        arch_gc += float(pref * np.dot(scaled, gauss * kappa_gammac(t_values)))
        nrm += float(pref * np.dot(scaled, gauss))
    n_max = 20000
    lam = von_mangoldt_table(n_max)
    g_pref = math.sqrt(math.pi / alpha)
    prime = 0.0
    prime_k = 0.0
    for index in range(2, n_max + 1):
        if lam[index] == 0.0:
            continue
        log_n = math.log(index)
        g_val = g_pref * math.exp(-0.25 * alpha * log_n * log_n)
        term = 2.0 * lam[index] / math.sqrt(index) * g_val
        prime += term
        prime_k += term * (1.0 + float(chi_m4(index)))
    phi = (2.0 * math.pi / alpha) * np.exp(-(zeros ** 2) / alpha)
    z_zeros = float(2.0 * np.sum(phi))
    z_src = pole + arch - prime
    scale = max(abs(z_zeros), abs(z_src), 1.0e-30)
    rel = abs(z_src - z_zeros) / scale
    id_c = abs(arch_c - (arch + arch_tq + 2.0 * LOG2 * nrm)) / max(abs(arch_c), 1.0e-30)
    id_gc = abs(arch_gc - (arch + arch_tq)) / max(abs(arch_gc), 1.0e-30)
    return {
        "alpha": alpha,
        "pole": pole,
        "arch": arch,
        "arch_tq": arch_tq,
        "arch_c": arch_c,
        "arch_gc": arch_gc,
        "nrm": nrm,
        "prime": prime,
        "prime_k": prime_k,
        "z_src": z_src,
        "z_zeros": z_zeros,
        "rel": rel,
        "id_c": id_c,
        "id_gc": id_gc,
        "w2": W2,
    }


def build_trial(
    length: float,
    n_fun: int,
    odd: bool,
    damped: bool,
    t_panels,
    connections: dict,
) -> dict:
    n_max = 2 * n_fun if odd else n_fun
    indices = (
        np.arange(1, n_max, 2, dtype=int) if odd
        else np.arange(n_max, dtype=int)
    )
    connection = None
    if damped:
        if n_max not in connections:
            connections[n_max] = damped_connection(n_max)
        connection = connections[n_max]
    spatial = spatial_blocks(length, n_max, damped)
    gram = extract(spatial["gram"], indices)
    pole = extract(spatial["pole"], indices)
    overlap = extract(spatial["overlap"], indices)
    archs = tspace_arch_bundle(
        length, n_max, indices, damped, connection, t_panels,
    )
    p2 = -W2 * overlap
    return {
        "n_max": n_max,
        "indices": indices,
        "damped": damped,
        "odd": odd,
        "gram": gram,
        "pole": pole,
        "overlap": overlap,
        "p2": p2,
        "arch_q": archs["q"],
        "arch_tq": archs["tq"],
        "arch_c": archs["c"],
        "arch_gc": archs["gc"],
        "gram_t": archs["pl"],
        "connection": connection,
    }


def identity_residual(trial: dict, use_tgram: bool = True) -> float:
    """ARCH_q = ARCH_C − ARCH_tq − 2 log 2 · G.

    G is the Plancherel Gram from the same t-panels (the discrete
    multiplier identity).  The x-space Gram differs by the ĥ-tail
    past the last panel; that gap is reported separately and is not
    a duplication failure.
    """
    gram = trial["gram_t"] if use_tgram else trial["gram"]
    predicted = trial["arch_c"] - trial["arch_tq"] - 2.0 * LOG2 * gram
    return rel_fro(trial["arch_q"] - predicted, trial["arch_q"])


def gammac_residual(trial: dict) -> float:
    predicted = trial["arch_q"] + trial["arch_tq"]
    return rel_fro(trial["arch_gc"] - predicted, trial["arch_gc"])


def t3_block(trial: dict) -> dict:
    gram = trial["gram"]
    a_odd = trial["pole"] + trial["arch_q"]
    values, vectors = gen_eigh(a_odd, gram)
    neg = values < EIG_NEG
    e_minus = vectors[:, neg]
    image = trial["arch_q"] @ e_minus
    stacked = (
        np.hstack((e_minus, image)) if e_minus.size else e_minus
    )
    basis = g_orthonormalize(stacked, gram)
    a_e, b_e, r_e, dim_v = fit_on_subspace(
        trial["p2"], trial["arch_tq"], gram, basis,
    )
    a_w, b_w, r_w = fit_alpha_beta(trial["p2"], trial["arch_tq"], gram)
    eig_p2 = spectral_pack(gen_eigvals(trial["p2"], gram))
    eig_tq = spectral_pack(gen_eigvals(trial["arch_tq"], gram))
    return {
        "dim_em": int(np.sum(neg)),
        "lam_min_A": float(values[0]),
        "alpha_em": a_e,
        "beta_em": b_e,
        "rel_em": r_e,
        "dim_v": dim_v,
        "alpha_odd": a_w,
        "beta_odd": b_w,
        "rel_odd": r_w,
        "eig_p2": eig_p2,
        "eig_tq": eig_tq,
        "cos_tq": hs_cos(trial["p2"], trial["arch_tq"], gram),
        "cos_g": hs_cos(trial["p2"], gram, gram),
        "lam_min_Q": float(gen_eigvals(a_odd + trial["p2"], gram)[0]),
        "lam_min_K": float(
            gen_eigvals(trial["pole"] + trial["arch_c"] + trial["p2"], gram)[0]
        ),
        "lam_min_A_K": float(
            gen_eigvals(trial["pole"] + trial["arch_c"], gram)[0]
        ),
        "lam_min_A_gc": float(
            gen_eigvals(trial["pole"] + trial["arch_gc"], gram)[0]
        ),
        "lam_min_Q_gc": float(
            gen_eigvals(trial["pole"] + trial["arch_gc"] + trial["p2"], gram)[0]
        ),
    }


def numpy_duplication_grid(n_pts: int = 501, t_max: float = 200.0) -> float:
    t_values = np.linspace(0.0, t_max, n_pts)
    lhs = kappa_quarter(t_values) + kappa_three_quarter(t_values)
    rhs = kappa_complex(t_values) - 2.0 * LOG2
    return float(np.max(np.abs(lhs - rhs)))


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    STATE.clear()

    if smoke:
        grid = L_SMOKE
        t4_extra = T4_L_EXTRA_SMOKE
        n_odd = N_ODD_SMOKE
        n_full = N_FULL_SMOKE
        n_g1 = N_G1_SMOKE
        n_outer_g1 = N_OUTER_G1_SMOKE
        n_zeros = N_ZEROS_SMOKE
        t_panels = PANELS_SMOKE
        t1_n = T1_N_SMOKE
        g1_panels = G1_PANELS
    else:
        grid = L_FULL
        t4_extra = T4_L_EXTRA_FULL
        n_odd = N_ODD_FULL
        n_full = N_FULL_FULL
        n_g1 = N_G1_FULL
        n_outer_g1 = N_OUTER_G1_FULL
        n_zeros = N_ZEROS_FULL
        t_panels = PANELS_FULL
        t1_n = T1_N_FULL
        g1_panels = G1_PANELS

    emit("p2_digamma_duplication_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("w2 %s  w2_K %s  half_log3 %s  residue_K %s" % (
        fmt(W2, 16), fmt(W2_K, 16), fmt(HALF_LOG3, 16), fmt(RESIDUE_K, 16),
    ))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit(
        "fence Archimedean identities; window forms at these L are "
        "RH-consistent; no RH claim."
    )

    zeros = load_zeros(n_zeros)
    emit("zeros n=%d gamma1=%s gammaN=%s source=%s" % (
        int(zeros.size), fmt(float(zeros[0]), 12), fmt(float(zeros[-1]), 12),
        "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
    ))

    section("T1  DIGAMMA DUPLICATION (mpmath)")
    t1_a = t1_duplication(t1_n, T1_TMAX, T1_DPS)
    t1_b = t1_duplication(t1_n, T1_TMAX, T1_DPS)
    emit(
        "  n=%d tmax=%s dps=%d max|lhs-rhs|=%s at t=%s  rerun=%s"
        % (
            t1_a["n"], fmt(T1_TMAX, 4), T1_DPS,
            fmt(t1_a["max_err"], 6), fmt(t1_a["argmax_t"], 6),
            fmt(t1_b["max_err"], 6),
        )
    )
    t1_ok = check(
        "T1-duplication-mpmath",
        t1_a["max_err"] <= T1_ATOL,
        "|err|=%s <= %s" % (fmt(t1_a["max_err"], 6), fmt(T1_ATOL, 2)),
    )
    check(
        "T1-two-runs-identical",
        t1_a["max_err"] == t1_b["max_err"],
        "err_a=%s err_b=%s" % (fmt(t1_a["max_err"], 8), fmt(t1_b["max_err"], 8)),
    )
    np_dup = numpy_duplication_grid(501, T1_TMAX)
    check(
        "T1-numpy-stirling-identity",
        np_dup <= 1.0e-12,
        "max|κ_q+κ_tq-κ_C+2log2|=%s" % fmt(np_dup, 6),
    )

    section("G0  GAUSSIAN EF PIN + CHANNEL IDENTITY")
    g0 = gaussian_g0(zeros)
    emit(
        "  alpha=%s POLE=%s ARCH_q=%s PRIME=%s Z_src=%s Z_zeros=%s rel=%s"
        % (
            fmt(g0["alpha"], 4), fmt(g0["pole"], 12), fmt(g0["arch"], 12),
            fmt(g0["prime"], 12), fmt(g0["z_src"], 12), fmt(g0["z_zeros"], 12),
            fmt(g0["rel"], 6),
        )
    )
    emit(
        "  ARCH_tq=%s ARCH_C=%s ARCH_Γℂ=%s nrm=%s id_C=%s id_Γℂ=%s PRIME_K=%s"
        % (
            fmt(g0["arch_tq"], 12), fmt(g0["arch_c"], 12), fmt(g0["arch_gc"], 12),
            fmt(g0["nrm"], 12), fmt(g0["id_c"], 6), fmt(g0["id_gc"], 6),
            fmt(g0["prime_k"], 12),
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
    check(
        "G0-w2K-equals-w2",
        abs(W2_K - W2) <= 1.0e-15,
        "w2_K=%s" % fmt(W2_K, 16),
    )
    check(
        "G0-channel-ARCH_C",
        g0["id_c"] <= 1.0e-8,
        "id_C=%s" % fmt(g0["id_c"], 6),
    )
    check(
        "G0-channel-ARCH_GammaC",
        g0["id_gc"] <= 1.0e-8,
        "id_GammaC=%s" % fmt(g0["id_gc"], 6),
    )

    section("G1  ARCH_1/4 x-space vs t-space")
    g1_length = float(grid[0])
    c_g1 = c_L_of(g1_length)
    g1_dim = min(n_g1, 12)
    n_inner_g1 = max(g1_dim + 8, 48)
    gram_g1 = gram_matrix(g1_length, g1_dim, True, n_inner_g1)
    arch_x_mat = arch_matrix(
        g1_length, g1_dim, True, gram_g1, c_g1, n_outer_g1, n_inner_g1,
    )
    conn_g1 = damped_connection(g1_dim)
    g1_ok_all = True
    for index in range(min(3, g1_dim)):
        coeff = np.zeros(g1_dim, dtype=np.float64)
        coeff[min(2 * index, g1_dim - 1)] = 1.0
        norm = math.sqrt(float(coeff @ gram_g1 @ coeff))
        coeff = coeff / max(norm, 1.0e-30)
        arch_x = float(coeff @ arch_x_mat @ coeff)

        def hat_fn(t_values, c=coeff.copy()):
            basis = bessel_damped_hat(g1_length, t_values, g1_dim, conn_g1)
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

    connections: dict = {}
    t2_rows = []
    t3_rows = []
    t4_rows = []

    section("T2  OPERATOR IDENTITY  ARCH_q = ARCH_C - ARCH_tq - 2 log 2 G")
    emit(
        "  G in the gate is the Plancherel Gram from the same t-panels "
        "(discrete multiplier identity).  rel_xG uses the x-space trial "
        "Gram; that gap is the ĥ tail, not a duplication failure."
    )
    kinds = (
        ("odd_undamped", n_odd, True, False),
        ("odd_damped", n_odd, True, True),
        ("full_undamped", n_full, False, False),
    )
    t2_ok_all = True
    max_t2_rel = 0.0
    for length in grid:
        emit("  L=%s  2L<log3=%d" % (
            fmt(length, 6), int(2.0 * length < LOG3 - 1.0e-15),
        ))
        for name, n_fun, odd, damped in kinds:
            trial = build_trial(
                length, n_fun, odd, damped, t_panels, connections,
            )
            rel_id = identity_residual(trial, use_tgram=True)
            rel_id_x = identity_residual(trial, use_tgram=False)
            rel_gc = gammac_residual(trial)
            rel_pl = rel_fro(trial["gram_t"] - trial["gram"], trial["gram"])
            max_t2_rel = max(max_t2_rel, rel_id)
            t2_ok = rel_id <= T2_REL and rel_gc <= T2_REL
            t2_ok_all = t2_ok_all and t2_ok
            check(
                "T2-%s-L%s" % (name, fmt(length, 4)),
                t2_ok,
                "rel_tG=%s rel_xG=%s pl_tail=%s GammaC=%s" % (
                    fmt(rel_id, 6), fmt(rel_id_x, 6),
                    fmt(rel_pl, 6), fmt(rel_gc, 6),
                ),
            )
            pack = {
                "L": length,
                "name": name,
                "trial": trial,
                "rel_id": rel_id,
                "rel_id_x": rel_id_x,
                "rel_pl": rel_pl,
                "rel_gc": rel_gc,
            }
            t2_rows.append(pack)
            if odd:
                t3 = t3_block(trial)
                t3["L"] = length
                t3["name"] = name
                t3["rel_id"] = rel_id
                t3_rows.append(t3)

    section("T3  DECIDING TEST  P2 vs α ARCH_3/4 + β G")
    emit(
        "  P2 = -w2 T_log2.  Fit after G-whitening (HS/Frobenius).  "
        "E- = negative eigenspace of A^odd = POLE + ARCH_1/4; "
        "V = E- ⊕ ARCH_1/4(E-)."
    )
    odd_whole = []
    for row in t3_rows:
        eig_p2 = row["eig_p2"]
        eig_tq = row["eig_tq"]
        emit(
            "  L=%s %s  dim E-=%d lamA=%s  "
            "V: a=%s b=%s rel=%s dimV=%d  "
            "odd: a=%s b=%s rel=%s"
            % (
                fmt(row["L"], 6), row["name"], row["dim_em"],
                fmt(row["lam_min_A"], 12),
                fmt(row["alpha_em"], 8), fmt(row["beta_em"], 8),
                fmt(row["rel_em"], 6), row["dim_v"],
                fmt(row["alpha_odd"], 8), fmt(row["beta_odd"], 8),
                fmt(row["rel_odd"], 6),
            )
        )
        emit(
            "    spec P2 n=%d nneg=%d npos=%d ntiny=%d min=%s max=%s  "
            "ARCH_tq min=%s max=%s nneg=%d  cos(P2,tq)=%s cos(P2,G)=%s"
            % (
                eig_p2["n"], eig_p2["n_neg"], eig_p2["n_pos"], eig_p2["n_tiny"],
                fmt(eig_p2["min"], 8), fmt(eig_p2["max"], 8),
                fmt(eig_tq["min"], 8), fmt(eig_tq["max"], 8), eig_tq["n_neg"],
                fmt(row["cos_tq"], 6), fmt(row["cos_g"], 6),
            )
        )
        check(
            "T3-dimE--%s-L%s" % (row["name"], fmt(row["L"], 4)),
            row["dim_em"] >= 1,
            "dim E-=%d lamA=%s" % (row["dim_em"], fmt(row["lam_min_A"], 12)),
        )
        if row["name"] == "odd_damped":
            odd_whole.append(row["rel_odd"])
            check(
                "T3-P2-indefinite-%s-L%s" % (row["name"], fmt(row["L"], 4)),
                eig_p2["n_neg"] >= 1 and eig_p2["n_pos"] >= 1,
                "nneg=%d npos=%d ntiny=%d" % (
                    eig_p2["n_neg"], eig_p2["n_pos"], eig_p2["n_tiny"],
                ),
            )

    section("T4  GAUSSIAN-INTEGER WINDOW (prime side only)")
    emit(
        "  ζ_{Q(i)} = ζ L(s, χ_{-4}).  Completed Λ_K(s) = "
        "2^s (2π)^{-s} Γ(s) ζ_K(s) = 2^{s-1} Γ_ℂ(s) ζ_K(s)."
    )
    emit(
        "  ARCH multiplier of Λ_K: 2 Re ψ(1/2+it) − 2 log π  "
        "(= ARCH_q + ARCH_tq + 2 log 2 G).  Γ_ℂ-only drops the "
        "conductor and subtracts another 2 log 2 (identity, not a shift)."
    )
    emit(
        "  POLE: Res(ζ_K'/ζ_K, s=1) = −1, same as ζ, so POLE_K = 2 F+ F- "
        "as for ζ.  Res(ζ_K, 1) = π/4 does not scale the Weil polar term."
    )
    emit(
        "  PRIME for 2L < log 3: only the ramified prime (1+i), N=2, "
        "weight 2 log 2 · 2^{-1/2} = w2 (same as ζ).  χ_{-4}(2)=0 so L "
        "does not see 2.  Zero-side SKIPPED: no χ_{-4} ordinates in mpmath "
        "and no cache under experiments/tfpt-discovery."
    )
    t4_scan_L = tuple(dict.fromkeys(list(grid) + list(t4_extra)))
    for length in t4_scan_L:
        if not (2.0 * length < LOG3 - 1.0e-15):
            emit("  SKIP L=%s  2L>=log3" % fmt(length, 6))
            continue
        # reuse T3 odd_damped trial when present
        reused = next(
            (
                row for row in t3_rows
                if row["name"] == "odd_damped" and abs(row["L"] - length) < 1.0e-12
            ),
            None,
        )
        if reused is None:
            trial = build_trial(
                length, min(n_odd, 16) if smoke else min(n_odd, 24),
                True, True, t_panels, connections,
            )
            t3 = t3_block(trial)
            t3["L"] = length
            t3["name"] = "odd_damped"
        else:
            t3 = reused
        t4_rows.append(t3)
        emit(
            "  L=%s  ζ: lam(A^odd)=%s lam(Q^odd)=%s  "
            "K(Λ): lam(A)=%s lam(Q)=%s  "
            "K(Γℂ): lam(A)=%s lam(Q)=%s"
            % (
                fmt(length, 6),
                fmt(t3["lam_min_A"], 12), fmt(t3["lam_min_Q"], 12),
                fmt(t3["lam_min_A_K"], 12), fmt(t3["lam_min_K"], 12),
                fmt(t3["lam_min_A_gc"], 12), fmt(t3["lam_min_Q_gc"], 12),
            )
        )

    def first_negative(key: str):
        ordered = sorted(t4_rows, key=lambda row: row["L"])
        prev = None
        for row in ordered:
            if row[key] < 0.0:
                return row["L"], row[key], None if prev is None else prev["L"]
            prev = row
        return None, None, None if not ordered else ordered[-1]["L"]

    l_az, v_az, pre_az = first_negative("lam_min_A")
    l_ak, v_ak, pre_ak = first_negative("lam_min_A_K")
    l_agc, v_agc, pre_agc = first_negative("lam_min_A_gc")
    emit(
        "  fictitious (no ramified 2): ζ A^odd first Ritz-neg at L=%s "
        "val=%s (last nonnegative L=%s);  K(Λ) at L=%s val=%s "
        "(last nonnegative L=%s);  K(Γℂ) at L=%s val=%s "
        "(last nonnegative L=%s).  Ritz-from-above: true crossing <= reported L."
        % (
            fmt(l_az, 6) if l_az is not None else "none",
            fmt(v_az, 12) if v_az is not None else "nan",
            fmt(pre_az, 6) if pre_az is not None else "n/a",
            fmt(l_ak, 6) if l_ak is not None else "none",
            fmt(v_ak, 12) if v_ak is not None else "nan",
            fmt(pre_ak, 6) if pre_ak is not None else "n/a",
            fmt(l_agc, 6) if l_agc is not None else "none",
            fmt(v_agc, 12) if v_agc is not None else "nan",
            fmt(pre_agc, 6) if pre_agc is not None else "n/a",
        )
    )
    k_needs = (
        "YES_same_pattern" if l_ak is not None
        else "NO_A_K_stays_nonneg_on_grid"
    )
    emit("  T4_STRUCT K(Λ) needs its ramified 2: %s" % k_needs)
    check(
        "T4-window-below-half-log3",
        all(2.0 * length < LOG3 - 1.0e-15 for length in grid),
        "max 2L=%s log3=%s" % (fmt(2.0 * max(grid), 12), fmt(LOG3, 12)),
    )

    section("T5  FACTORIZATION (12)")
    # verdict from whole-odd-space damped residuals
    damped_whole = [
        row["rel_odd"] for row in t3_rows if row["name"] == "odd_damped"
    ]
    undamped_whole = [
        row["rel_odd"] for row in t3_rows if row["name"] == "odd_undamped"
    ]
    all_whole = damped_whole + undamped_whole
    if all_whole and all(rel <= T3_CAND for rel in all_whole):
        t3_verdict = "DUPLICATION_FACTOR_CANDIDATE"
    elif all_whole and all(rel >= T3_CONST for rel in all_whole):
        t3_verdict = "DUPLICATION_CONSTANT_ONLY"
    else:
        t3_verdict = "INCONCLUSIVE"

    if t3_verdict != "DUPLICATION_FACTOR_CANDIDATE":
        emit(
            "  SKIPPED (T3 verdict is %s; factorization search only "
            "runs on DUPLICATION_FACTOR_CANDIDATE)"
            % t3_verdict
        )
        check("T5-skipped", True, t3_verdict)
    else:
        emit("  T3 fired CANDIDATE; closed-form search is out of this worker's mandate")
        check("T5-candidate-not-implemented", False, "would search (12) here")

    section("VERDICT")
    if not t1_ok or not g0_ok or not g1_ok_all or not t2_ok_all:
        verdict = "INCONCLUSIVE"
        why = "an identity/G0/G1/T2 gate failed; T3 numbers are reported but not sealed"
    else:
        verdict = t3_verdict
        why = (
            "whole-odd HS residual of P2 vs span{ARCH_3/4, G} "
            "(damped+undamped, all L)"
        )
    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("VERDICT %s" % verdict)
    emit("T4_STRUCT %s" % k_needs)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit(
        "fence Archimedean identities; window forms at these L are "
        "RH-consistent; no RH claim."
    )
    emit("claim_boundary experiments_only_not_a_ledger_claim")

    # compact STATE (<= 30 lines)
    payload = {
        "verdict": verdict,
        "t4": k_needs,
        "t1": t1_a["max_err"],
        "t2": max_t2_rel,
        "t3_damped": [
            {
                "L": row["L"],
                "rel_em": row["rel_em"],
                "rel_odd": row["rel_odd"],
                "a": row["alpha_odd"],
                "b": row["beta_odd"],
                "a_em": row["alpha_em"],
                "b_em": row["beta_em"],
                "dim_em": row["dim_em"],
            }
            for row in t3_rows if row["name"] == "odd_damped"
        ],
        "spec": [
            {
                "L": row["L"],
                "p2_tiny": row["eig_p2"]["n_tiny"],
                "p2_neg": row["eig_p2"]["n_neg"],
                "p2_pos": row["eig_p2"]["n_pos"],
                "tq_min": row["eig_tq"]["min"],
                "tq_max": row["eig_tq"]["max"],
                "cos_tq": row["cos_tq"],
                "cos_g": row["cos_g"],
            }
            for row in t3_rows if row["name"] == "odd_damped"
        ],
        "t4_nums": [
            {
                "L": row["L"],
                "Az": row["lam_min_A"],
                "Qz": row["lam_min_Q"],
                "AK": row["lam_min_A_K"],
                "QK": row["lam_min_K"],
            }
            for row in t4_rows
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
    emit("T1_ERR %s" % fmt(t1_a["max_err"], 6))
    emit("T2_ID_REL %s" % fmt(max_t2_rel, 6))
    for row in t3_rows:
        if row["name"] != "odd_damped":
            continue
        emit(
            "T3 L=%s relE=%s (a,b)E=(%s,%s) relOdd=%s (a,b)=(%s,%s) dimE=%d"
            % (
                fmt(row["L"], 4), fmt(row["rel_em"], 6),
                fmt(row["alpha_em"], 6), fmt(row["beta_em"], 6),
                fmt(row["rel_odd"], 6),
                fmt(row["alpha_odd"], 6), fmt(row["beta_odd"], 6),
                row["dim_em"],
            )
        )
    spec_bits = []
    for row in t3_rows:
        if row["name"] != "odd_damped":
            continue
        e_p = row["eig_p2"]
        e_t = row["eig_tq"]
        spec_bits.append(
            "L=%s P2(nneg=%d npos=%d ntiny=%d min=%s) tq=[%s,%s] cos_tq=%s"
            % (
                fmt(row["L"], 2), e_p["n_neg"], e_p["n_pos"], e_p["n_tiny"],
                fmt(e_p["min"], 3), fmt(e_t["min"], 3), fmt(e_t["max"], 3),
                fmt(row["cos_tq"], 3),
            )
        )
    emit("SPECTRAL " + " || ".join(spec_bits))
    emit(
        "T4 Az_neg_L=%s AK_neg_L=%s AGc_neg_L=%s struct=%s zero_side=SKIPPED"
        % (
            fmt(l_az, 4) if l_az is not None else "none",
            fmt(l_ak, 4) if l_ak is not None else "none",
            fmt(l_agc, 4) if l_agc is not None else "none",
            k_needs,
        )
    )
    grid_set = set(float(length) for length in grid)
    for row in t4_rows:
        if min((abs(row["L"] - length) for length in grid_set), default=1.0) > 1.0e-12:
            continue
        emit(
            "T4 L=%s Az=%s Qz=%s AK=%s QK=%s"
            % (
                fmt(row["L"], 4), fmt(row["lam_min_A"], 8),
                fmt(row["lam_min_Q"], 8), fmt(row["lam_min_A_K"], 8),
                fmt(row["lam_min_K"], 8),
            )
        )
    emit("T5 SKIPPED" if t3_verdict != "DUPLICATION_FACTOR_CANDIDATE" else "T5 OPEN")
    emit(
        "FENCE Archimedean identities; window forms at these L are "
        "RH-consistent; no RH claim."
    )
    n_state = sum(
        1 for line in LINES
        if line.startswith("STATE ") or line.startswith("SHA ")
        or line.startswith("SPEC ") or line.startswith("NUM ")
        or line.startswith("GATES ") or line.startswith("VERDICT ")
        or line.startswith("T1_") or line.startswith("T2_")
        or line.startswith("T3 ") or line.startswith("T4 ")
        or line.startswith("T5 ") or line.startswith("SPECTRAL ")
        or line.startswith("FENCE ")
    )
    emit("STATE_LINES %d" % n_state)
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r621 digamma-duplication vs prime-2 translation (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
