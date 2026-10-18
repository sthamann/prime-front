#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jet_deflated_ldet_probe -- r632  PRIME.WINDOW.JETDEFLATION.01

Experiments-only scout of reviewer-proposed *jet deflation* of the
window Weil form.  Copied (not imported) from the sealed r619
support_relay_census_probe: Q = POLE + ARCH − PRIME, v1017 x-space
kernel, edge-damped Legendre (1−(u/L)^2)^3 P_n with N≤80, zero-side
λ*(L) = min Σ_γ |f̂(γ)|² + density tail via SVD (5000 zeros), and
the C6 off-line quadruple injection that produced

  L_det(β=0.6, γ=20)=0.55, (0.75,20)=0.55, (0.6,50)=0.80, (0.9,20)=0.50.

A displaced zero at ordinate t_j contributes
  ΔQ(f) = −c₁ σ² |f̂'(t_j)|² + O(σ⁴).
On the jet-deflated sector
  V_{L,m}(T) = {f : f̂^{(r)}(t_j)=0 for t_j∈T, 0≤r≤m}
the first-order sensitivity vanishes for m≥1, so positivity on V
should be far less RH-sensitive (L_det much larger), while the RH
content is pushed into a finite complement K_{L,m} of dimension
≤ 2(m+1)|T|.  Question: does sectorization buy a genuinely large
L_det gain, and does dim K grow at the zero-counting rate until V
collapses (recoordinatization kill)?

C6 injection (copied): quadruple {β±iγ, (1−β)±iγ} contributes
4 Re[ f̂(½+σ+iγ) conj(f̂(½−σ+iγ)) ] (σ=β−1/2) in place of the
on-line pair 2|f̂(γ)|².  The factor 4 is the ±γ fold of the two
real-part zeros; at σ=0 this is 4|f̂|² = 2 × (on-line pair).
A separate 2 Re check validates that 2 Re[F conj(F)] = 2|f̂|²
recovers the on-line pair (user/reviewer σ=0 identity).

Fence: "Sector diagnostics of the window Weil form; no RH claim."
Claim boundary: finite-section arithmetic.  Not a ledger row.
Not a paper claim.  Experiments only.
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

ROUND = 632
SEED = 632202609
CONTRACT = "PRIME.WINDOW.JETDEFLATION.01"
FENCE = "Sector diagnostics of the window Weil form; no RH claim."
PARENT = "r619 support_relay_census_probe"

GAMMA1 = 14.134725141734695
LOG2 = math.log(2.0)
W2 = math.sqrt(2.0) * LOG2
DAMP_POWER = 3
SVD_COND = 1.0e-8
NULL_RTOL = 1e-8
NULL_ATOL = 1e-10
T1_TOL = 0.05
AB_REL = 5.0e-2
C_L_LO = 2.19240491113
C_L_HI = 2.19240491114
SIG0_REL = 1.0e-8
SIG0_RECOVER = 5.0e-8
JET_FD_REL = 5.0e-4
R619_LDET = {
    (0.6, 20.0): 0.55,
    (0.9, 20.0): 0.50,
    (0.6, 50.0): 0.80,
    (0.75, 20.0): 0.55,
}
C6_PAIRS_T1 = ((0.6, 20.0), (0.9, 20.0), (0.6, 50.0))
C6_EXTRA = (0.75, 20.0)
INJECT_DEFLATED = ((0.6, 20.0), (0.9, 20.0))
INJECT_CONTROL = (0.6, 50.0)
L_STAR_GRID = (0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2)
L_STAR_SMOKE = (0.6, 1.0)
T4_LENGTHS = (0.50, 0.60)
T3_GAMMAS = (50.0, 100.0, 200.0)
T3_L = 1.0
T3_M = 1
N_FULL = 80
N_SMOKE = 40
N_ZEROS_FULL = 5000
N_ZEROS_SMOKE = 800
N_OUTER_FULL = 80
N_OUTER_SMOKE = 48
C6_L_LO = 0.25
C6_L_HI_FULL = 3.0
C6_L_HI_SMOKE = 1.60
C6_STEP_FULL = 0.05
C6_STEP_SMOKE = 0.10
T4_PEAK_CUT = 6.5
CTRL_MOVE_TOL = 0.05

SPEC = {
    "round": ROUND,
    "tag": "r632",
    "contract": CONTRACT,
    "parent": PARENT,
    "identity": "Q=POLE+ARCH-PRIME",
    "pole": "2*Fplus*Fminus",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "space": "(1-(u/L)^2)^3 * P_n",
    "damp_power": DAMP_POWER,
    "n": N_FULL,
    "n_zeros": N_ZEROS_FULL,
    "zeros_cache": "verified_zeros_n7000.npy (recompute if absent; no new npy)",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "lambda_star": "2*sigma_min(F_white)^2 + tail, F[k,i]=hat_i(gamma_k)",
    "factor2": "plus/minus gamma",
    "hat_H": "fhat(rho)*conj(fhat(1-conj(rho)))",
    "offline_r619": "4*Re[F(sigma,g)*conj(F(-sigma,g))] for the quadruple",
    "offline_sigma0_pair": "2*Re[F(0)*conj(F(0))]=2*|hat|^2 recovers on-line pair",
    "c6_pairs_t1": [list(pair) for pair in C6_PAIRS_T1],
    "r619_ldet": {"0.6_20": 0.55, "0.9_20": 0.50, "0.6_50": 0.80, "0.75_20": 0.55},
    "t1_tol": T1_TOL,
    "c6_scan": [C6_L_LO, C6_L_HI_FULL, C6_STEP_FULL],
    "l_star_grid": list(L_STAR_GRID),
    "sectors": [
        {"T": [20.0], "m": 0},
        {"T": [20.0], "m": 1},
        {"T": [20.0], "m": 2},
        {"T": [20.0, 25.0], "m": 1},
        {"T": "gamma_1_to_8", "m": 1},
    ],
    "dim_K": "2*(m+1)*|T| real constraints; f real => hat(-t)=(-1)^r conj hat^(r)(t)",
    "t3_Gamma": list(T3_GAMMAS),
    "t3_L": T3_L,
    "t3_m": T3_M,
    "n_Gamma": "(Gamma/2pi)*log(Gamma/(2pi*e))",
    "n_nyquist": "2*L*Gamma/pi",
    "t4": "lmin(POLE+ARCH) on V_{L,1}({20}) vs full; odd-sector r620",
    "t4_peak_cut": T4_PEAK_CUT,
    "sig0_rel": SIG0_REL,
    "sig0_recover": SIG0_RECOVER,
    "seed": SEED,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": FENCE,
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
    if dim <= 0:
        return float("nan"), np.zeros(0, dtype=np.float64)
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
    moment: int = 0,
) -> np.ndarray:
    """hat^{(r)}(t) = ∫ f(u) (i u)^r e^{i t u} du, r = moment."""
    t_arr = np.atleast_1d(np.asarray(t_values, dtype=np.complex128))
    t_scale = float(np.max(np.abs(t_arr))) if t_arr.size else 1.0
    n_quad = n_quad or max(8 * dimension, int(2.0 * length * t_scale) + 96, 192)
    n_quad = min(int(n_quad), 2048)
    nodes, weights = roots_legendre(n_quad)
    points = length * nodes
    scaled = length * weights
    if moment:
        scaled = scaled * ((1j * points) ** int(moment))
    basis = basis_values(points, length, dimension)
    phase = np.exp(1j * np.outer(t_arr, points))
    return (phase * scaled) @ basis


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
    hats: np.ndarray | None = None,
    tail: np.ndarray | None = None,
) -> dict:
    if hats is None:
        hats = bessel_damped_hat(length, zeros, dimension, connection)
    gram_h = 2.0 * np.real(hats.conj().T @ hats)
    gram_h = 0.5 * (gram_h + gram_h.T)
    if tail is None:
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
            0.5 * (gram + gram.T) + 1.0e-14 * np.eye(gram.shape[0])
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


def offline_matrix(v_plus: np.ndarray, v_minus: np.ndarray, scale: float = 4.0) -> np.ndarray:
    """Quadratic form scale * Re[(v+·c) conj(v-·c)] for real c.

    r619 uses scale=4 (full quadruple, ±γ folded).  scale=2 recovers
    the on-line pair 2|hat|^2 at σ=0.
    """
    plus = np.asarray(v_plus, dtype=np.complex128).ravel()
    minus = np.asarray(v_minus, dtype=np.complex128).ravel()
    real_p, imag_p = np.real(plus), np.imag(plus)
    real_m, imag_m = np.real(minus), np.imag(minus)
    matrix = np.outer(real_p, real_m) + np.outer(imag_p, imag_m)
    matrix = 0.5 * (matrix + matrix.T)
    return float(scale) * matrix


def n_riemann(gamma: float) -> float:
    """Leading Riemann–von Mangoldt: (Γ/2π) log(Γ/(2π e))."""
    if gamma <= 2.0 * math.pi * math.e:
        return 0.0
    return (gamma / (2.0 * math.pi)) * math.log(gamma / (2.0 * math.pi * math.e))


def n_nyquist(length: float, gamma: float) -> float:
    return 2.0 * length * gamma / math.pi


def dim_k_formula(m_jet: int, n_t: int) -> int:
    return 2 * (int(m_jet) + 1) * int(n_t)


def jet_constraint_matrix(
    length: float,
    dimension: int,
    ordinates: np.ndarray,
    m_jet: int,
) -> np.ndarray:
    """Real rows: Re/Im of hat^{(r)}(t_j) for r=0..m, t_j in T (t_j>0)."""
    t_arr = np.atleast_1d(np.asarray(ordinates, dtype=np.float64))
    t_arr = t_arr[np.isfinite(t_arr) & (t_arr > 0.0)]
    if t_arr.size == 0 or m_jet < 0:
        return np.zeros((0, dimension), dtype=np.float64)
    rows = []
    for order in range(int(m_jet) + 1):
        hats = basis_hat_complex(length, t_arr, dimension, moment=order)
        for index in range(t_arr.size):
            vec = hats[index]
            rows.append(np.real(vec))
            rows.append(np.imag(vec))
    return np.vstack(rows)


def nullspace_basis(constraints: np.ndarray, dimension: int) -> dict:
    if constraints.size == 0:
        eye = np.eye(dimension, dtype=np.float64)
        return {
            "Q": eye,
            "rank": 0,
            "dim_v": dimension,
            "dim_k": 0,
            "smax": 0.0,
            "smin_kept": 0.0,
        }
    matrix = np.asarray(constraints, dtype=np.float64)
    try:
        _u, sigma, vt = np.linalg.svd(matrix, full_matrices=True)
    except np.linalg.LinAlgError:
        eye = np.eye(dimension, dtype=np.float64)
        return {
            "Q": eye,
            "rank": 0,
            "dim_v": dimension,
            "dim_k": 0,
            "smax": float("nan"),
            "smin_kept": float("nan"),
        }
    smax = float(sigma[0]) if sigma.size else 0.0
    thresh = max(NULL_ATOL, NULL_RTOL * max(smax, 1.0e-30))
    rank = int(np.sum(sigma > thresh))
    rank = max(0, min(rank, dimension))
    q_mat = vt[rank:, :].T.copy()
    if q_mat.size == 0:
        q_mat = np.zeros((dimension, 0), dtype=np.float64)
    smin_kept = float(sigma[rank - 1]) if rank > 0 else 0.0
    return {
        "Q": q_mat,
        "rank": rank,
        "dim_v": int(q_mat.shape[1]),
        "dim_k": rank,
        "smax": smax,
        "smin_kept": smin_kept,
    }


def restrict_pencil(matrix: np.ndarray, gram: np.ndarray, q_mat: np.ndarray):
    if q_mat.size == 0 or q_mat.shape[1] == 0:
        z = np.zeros((0, 0), dtype=np.float64)
        return z, z
    a_v = q_mat.T @ matrix @ q_mat
    g_v = q_mat.T @ gram @ q_mat
    return 0.5 * (a_v + a_v.T), 0.5 * (g_v + g_v.T)


def injected_pencil(
    gram_h: np.ndarray,
    hats: np.ndarray,
    zeros: np.ndarray,
    tail: np.ndarray,
    length: float,
    dimension: int,
    beta: float,
    gamma: float,
    scale: float,
) -> np.ndarray:
    sigma = beta - 0.5
    k0 = int(np.argmin(np.abs(zeros - gamma)))
    row = hats[k0]
    reduced = gram_h - 2.0 * np.real(np.outer(np.conj(row), row))
    t_plus = gamma - 1j * sigma
    t_minus = gamma + 1j * sigma
    hats_c = basis_hat_complex(float(length), [t_plus, t_minus], dimension)
    off = offline_matrix(hats_c[0], hats_c[1], scale=scale)
    pencil = reduced + off + tail
    return 0.5 * (pencil + pencil.T)


def ldet_from_scan(values: list[tuple[float, float]], floor: float, step: float):
    """First L on the scan with lam < 0; inf if none."""
    found = float("inf")
    for length, lam in values:
        if math.isfinite(lam) and lam < 0.0:
            found = float(length)
            break
    return found


def shown_ldet(value: float, floor: float, step: float) -> str:
    if not math.isfinite(value):
        return "> %.2f" % C6_L_HI_FULL
    if abs(value - floor) < 0.5 * step:
        return "<= %s" % fmt(value, 4)
    return fmt(value, 4)


def odd_mask(dimension: int) -> np.ndarray:
    return np.arange(dimension) % 2 == 1


def peak_frequency(
    length: float,
    coeff: np.ndarray,
    connection: np.ndarray,
    t_hi: float = 40.0,
    n_grid: int = 401,
) -> tuple[float, float]:
    if coeff.size == 0 or not np.any(np.isfinite(coeff)):
        return float("nan"), float("nan")
    t_grid = np.linspace(0.05, t_hi, n_grid)
    hats = bessel_damped_hat(length, t_grid, int(coeff.size), connection)
    amp = np.abs(hats @ coeff.astype(np.complex128))
    index = int(np.argmax(amp))
    return float(t_grid[index]), float(amp[index])


class PackCache:
    """Zero-side packs (gram, hats, tail) reused across sectors at fixed L."""

    def __init__(self, dimension: int, n_outer: int, connection: np.ndarray, zeros: np.ndarray):
        self.dimension = int(dimension)
        self.n_outer = int(n_outer)
        self.n_inner = n_inner_of(self.dimension)
        self.connection = connection
        self.zeros = zeros
        self.zero: dict[float, dict] = {}
        self.free: dict[float, dict] = {}
        self.nulls: dict[tuple, dict] = {}
        self.inj: dict[tuple, np.ndarray] = {}

    def zero_at(self, length: float) -> dict:
        key = round(float(length), 12)
        packed = self.zero.get(key)
        if packed is not None:
            return packed
        gram = gram_matrix(length, self.dimension, self.n_inner)
        hats = bessel_damped_hat(length, self.zeros, self.dimension, self.connection)
        gram_h = 2.0 * np.real(hats.conj().T @ hats)
        gram_h = 0.5 * (gram_h + gram_h.T)
        tail = tail_matrix(
            length, self.dimension, self.connection, float(self.zeros[-1]),
            t_extra=1500.0, n_quad=32,
        )
        packed = {
            "gram": 0.5 * (gram + gram.T),
            "hats": hats,
            "gram_h": gram_h,
            "tail": tail,
        }
        self.zero[key] = packed
        return packed

    def free_at(self, length: float) -> dict:
        key = round(float(length), 12)
        packed = self.free.get(key)
        if packed is not None:
            return packed
        gram = self.zero_at(length)["gram"] if key in self.zero else gram_matrix(
            length, self.dimension, self.n_inner,
        )
        c_l = c_L_of(length)
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
            "c_L": c_l,
        }
        self.free[key] = packed
        return packed

    def sector_at(self, length: float, ordinates, m_jet: int) -> dict:
        t_key = tuple(round(float(val), 10) for val in np.atleast_1d(ordinates))
        key = (round(float(length), 12), t_key, int(m_jet))
        cached = self.nulls.get(key)
        if cached is not None:
            return cached
        constraints = jet_constraint_matrix(
            length, self.dimension, np.asarray(ordinates, dtype=np.float64), m_jet,
        )
        packed = nullspace_basis(constraints, self.dimension)
        packed["C"] = constraints
        packed["n_cons"] = int(constraints.shape[0])
        packed["dim_k_formula"] = dim_k_formula(m_jet, len(t_key))
        self.nulls[key] = packed
        return packed

    def injected_at(
        self, length: float, zeros: np.ndarray, beta: float, gamma: float, scale: float,
    ) -> np.ndarray:
        key = (round(float(length), 12), round(float(beta), 8), round(float(gamma), 8), float(scale))
        cached = self.inj.get(key)
        if cached is not None:
            return cached
        pack = self.zero_at(length)
        pencil = injected_pencil(
            pack["gram_h"], pack["hats"], zeros, pack["tail"],
            length, self.dimension, beta, gamma, scale,
        )
        self.inj[key] = pencil
        return pencil


def zside_on_Q(pack: dict, q_mat: np.ndarray) -> dict:
    if q_mat.size == 0 or q_mat.shape[1] == 0:
        return {
            "lam": float("nan"), "lam_svd": float("nan"), "cond": float("nan"),
            "dim_v": 0, "svd_ok": False,
        }
    hats = pack["hats"] @ q_mat
    gram_v = q_mat.T @ pack["gram"] @ q_mat
    tail_v = q_mat.T @ pack["tail"] @ q_mat
    gram_h = 2.0 * np.real(hats.conj().T @ hats)
    gram_h = 0.5 * (gram_h + gram_h.T)
    pencil = gram_h + tail_v
    lam, vec = min_rayleigh(pencil, gram_v)
    if -1.0e-12 < lam < 0.0:
        lam = 0.0
    lam_svd = float("nan")
    cond = float("nan")
    try:
        dim = gram_v.shape[0]
        chol = np.linalg.cholesky(
            0.5 * (gram_v + gram_v.T) + 1.0e-14 * np.eye(dim)
        )
        white = np.linalg.solve(chol, hats.T).T
        sigma = svdvals(white)
        smin = float(sigma[-1])
        smax = float(sigma[0])
        lam_svd = 2.0 * smin * smin
        cond = smin / smax if smax > 0.0 else float("nan")
    except np.linalg.LinAlgError:
        pass
    return {
        "lam": lam,
        "lam_svd": lam_svd,
        "cond": cond,
        "dim_v": int(q_mat.shape[1]),
        "svd_ok": bool(math.isfinite(cond) and cond >= SVD_COND),
        "vec": vec,
    }


def rayleigh_on_Q(matrix: np.ndarray, gram: np.ndarray, q_mat: np.ndarray) -> float:
    if q_mat.size == 0 or q_mat.shape[1] == 0:
        return float("nan")
    a_v, g_v = restrict_pencil(matrix, gram, q_mat)
    lam, _vec = min_rayleigh(a_v, g_v)
    return lam


def inject_min_on_Q(
    cache: PackCache,
    pack: dict,
    q_mat: np.ndarray,
    length: float,
    zeros: np.ndarray,
    beta: float,
    gamma: float,
    scale: float,
) -> float:
    if q_mat.size == 0 or q_mat.shape[1] == 0:
        return float("nan")
    pencil = cache.injected_at(length, zeros, beta, gamma, scale)
    a_v, g_v = restrict_pencil(pencil, pack["gram"], q_mat)
    lam, _vec = min_rayleigh(a_v, g_v)
    return lam


def scan_ldet(
    cache: PackCache,
    q_of,
    zeros: np.ndarray,
    beta: float,
    gamma: float,
    grid: np.ndarray,
    scale: float,
) -> float:
    for length in grid:
        pack = cache.zero_at(float(length))
        q_mat = q_of(float(length))
        lam = inject_min_on_Q(
            cache, pack, q_mat, float(length), zeros, beta, gamma, scale,
        )
        if math.isfinite(lam) and lam < 0.0:
            return float(length)
    return float("inf")


def identity_Q(dimension: int):
    eye = np.eye(dimension, dtype=np.float64)

    def _fn(_length, q=eye):
        return q
    return _fn


def sector_Q(cache: PackCache, ordinates, m_jet: int):
    t_arr = np.asarray(ordinates, dtype=np.float64)

    def _fn(length, t=t_arr, m=m_jet, cc=cache):
        return cc.sector_at(length, t, m)["Q"]
    return _fn


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    _CL_CACHE.clear()
    wall0 = time.time()

    if smoke:
        dimension = N_SMOKE
        n_zeros = N_ZEROS_SMOKE
        n_outer = N_OUTER_SMOKE
        c6_step = C6_STEP_SMOKE
        c6_hi = C6_L_HI_SMOKE
        l_star = L_STAR_SMOKE
        t4_ls = (T4_LENGTHS[0],)
        n_true_t = 4
    else:
        dimension = N_FULL
        n_zeros = N_ZEROS_FULL
        n_outer = N_OUTER_FULL
        c6_step = C6_STEP_FULL
        c6_hi = C6_L_HI_FULL
        l_star = L_STAR_GRID
        t4_ls = T4_LENGTHS
        n_true_t = 8

    emit("jet_deflated_ldet_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("N=%d  n_zeros=%d  n_outer=%d  damp (1-(u/L)^2)^%d" % (
        dimension, n_zeros, n_outer, DAMP_POWER,
    ))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit(FENCE)

    zeros = load_zeros(n_zeros)
    emit("zeros n=%d gamma1=%s gammaN=%s source=%s" % (
        int(zeros.size), fmt(float(zeros[0]), 12), fmt(float(zeros[-1]), 12),
        "verified_zeros_n7000.npy" if ZEROS_CACHE.is_file() else "mpmath.zetazero",
    ))
    true_t = np.asarray(zeros[:n_true_t], dtype=np.float64)
    emit("T_true (first %d zeros) %s" % (
        n_true_t, ",".join(fmt(float(val), 6) for val in true_t),
    ))

    connection = damped_connection(dimension)
    cache = PackCache(dimension, n_outer, connection, zeros)
    c6_grid = np.arange(C6_L_LO, c6_hi + 0.5 * c6_step, c6_step)
    q_full = identity_Q(dimension)

    section("PIN  c_L AND σ=0 PAIR IDENTITY")
    c03 = c_L_numpy(0.3)
    emit("  c_L(0.3)=%s" % fmt(c03, 16))
    check(
        "PIN-cL-0.3",
        C_L_LO < c03 < C_L_HI,
        "c_L(0.3)=%s" % fmt(c03, 16),
    )
    _CL_CACHE[round(0.3, 12)] = c03

    val_L = 0.50
    pack_val = cache.zero_at(val_L)
    k0_val = int(np.argmin(np.abs(zeros[: min(40, zeros.size)] - 20.0)))
    gamma0 = float(zeros[k0_val])
    coeff = np.zeros(dimension, dtype=np.float64)
    coeff[0] = 1.0
    nrm = math.sqrt(float(coeff @ pack_val["gram"] @ coeff))
    coeff = coeff / max(nrm, 1.0e-30)
    f_rho = complex(pack_val["hats"][k0_val] @ coeff)
    hat_h = f_rho * np.conj(f_rho)
    online_sq = np.abs(f_rho) ** 2
    rel_h = abs(hat_h - online_sq) / max(abs(online_sq), 1.0e-30)
    emit(
        "  ĥ_H(1/2+iγ)=|f̂|²  γ=%s rel=%s"
        % (fmt(gamma0, 8), fmt(float(np.abs(rel_h)), 6))
    )
    check("PIN-H-online", float(np.abs(rel_h)) <= 1.0e-10, "rel=%s" % fmt(float(np.abs(rel_h)), 6))

    row = pack_val["hats"][k0_val]
    pair = 2.0 * np.real(np.outer(np.conj(row), row))
    pair = 0.5 * (pair + pair.T)
    two_re = offline_matrix(row, row, scale=2.0)
    four_re = offline_matrix(row, row, scale=4.0)
    rel_2 = float(np.linalg.norm(two_re - pair) / max(np.linalg.norm(pair), 1.0e-30))
    rel_4 = float(np.linalg.norm(four_re - 2.0 * pair) / max(np.linalg.norm(pair), 1.0e-30))
    emit(
        "  σ=0  2Re vs on-line pair rel=%s  4Re vs 2×pair rel=%s"
        % (fmt(rel_2, 6), fmt(rel_4, 6))
    )
    check("PIN-sigma0-2Re", rel_2 <= SIG0_REL, "rel=%s" % fmt(rel_2, 6))
    check("PIN-sigma0-4Re-double", rel_4 <= SIG0_REL, "rel=%s" % fmt(rel_4, 6))

    # Recover λ* by replacing the on-line pair with 2 Re at σ=0.
    gram_h = pack_val["gram_h"]
    tail = pack_val["tail"]
    gram = pack_val["gram"]
    lam_on, _ = min_rayleigh(gram_h + tail, gram)
    reduced = gram_h - pair
    lam_2, _ = min_rayleigh(reduced + two_re + tail, gram)
    rel_rec = abs(lam_2 - lam_on) / max(abs(lam_on), 1.0e-30)
    abs_rec = abs(lam_2 - lam_on)
    emit(
        "  recover λ* at σ=0 with 2Re: on=%s rec=%s rel=%s abs=%s"
        % (fmt(lam_on, 10), fmt(lam_2, 10), fmt(rel_rec, 6), fmt(abs_rec, 6))
    )
    check(
        "PIN-sigma0-recover-2Re",
        abs_rec <= 1.0e-10 or rel_rec <= SIG0_RECOVER,
        "rel=%s abs=%s" % (fmt(rel_rec, 6), fmt(abs_rec, 6)),
    )

    # Jet derivative vs finite difference at t=20.
    t_fd = 20.0
    h_fd = 1.0e-4
    hat0 = basis_hat_complex(val_L, [t_fd], dimension, moment=0)[0]
    hat1 = basis_hat_complex(val_L, [t_fd], dimension, moment=1)[0]
    hat_p = basis_hat_complex(val_L, [t_fd + h_fd], dimension, moment=0)[0]
    hat_m = basis_hat_complex(val_L, [t_fd - h_fd], dimension, moment=0)[0]
    fd = (hat_p - hat_m) / (2.0 * h_fd)
    rel_fd = float(np.linalg.norm(hat1 - fd) / max(np.linalg.norm(hat1), 1.0e-30))
    emit("  jet r=1 vs FD at t=20 rel=%s" % fmt(rel_fd, 6))
    check("PIN-jet-FD", rel_fd <= JET_FD_REL, "rel=%s" % fmt(rel_fd, 6))
    # Bessel vs quadrature at real t (order 0).
    hat_b = bessel_damped_hat(val_L, np.array([t_fd]), dimension, connection)[0]
    rel_bq = float(np.linalg.norm(hat_b - hat0) / max(np.linalg.norm(hat_b), 1.0e-30))
    emit("  Bessel vs quad hat(20) rel=%s" % fmt(rel_bq, 6))
    check("PIN-bessel-quad", rel_bq <= 1.0e-6, "rel=%s" % fmt(rel_bq, 6))

    section("T1  BASELINE L_det  (r619 C6, N=%d, 4 Re quadruple)" % dimension)
    ldet_full = {}
    for beta, gamma in list(C6_PAIRS_T1) + [C6_EXTRA]:
        found = scan_ldet(cache, q_full, zeros, beta, gamma, c6_grid, 4.0)
        ldet_full[(beta, gamma)] = found
        ref = R619_LDET.get((beta, gamma))
        emit(
            "  L_det(β=%s, γ=%s)=%s  r619=%s"
            % (
                fmt(beta, 2), fmt(gamma, 2), shown_ldet(found, C6_L_LO, c6_step),
                fmt(ref, 2) if ref is not None else "n/a",
            )
        )
    t1_ok = True
    if not smoke:
        for beta, gamma in C6_PAIRS_T1:
            found = ldet_full[(beta, gamma)]
            ref = R619_LDET[(beta, gamma)]
            ok = math.isfinite(found) and abs(found - ref) <= T1_TOL + 1.0e-12
            t1_ok = t1_ok and ok
            check(
                "T1-Ldet-%s-%s" % (fmt(beta, 2), fmt(gamma, 2)),
                ok,
                "got=%s ref=%s tol=%.2f" % (
                    shown_ldet(found, C6_L_LO, c6_step), fmt(ref, 2), T1_TOL,
                ),
            )
    else:
        emit("  T1 numeric match skipped in --smoke (N=%d, coarse grid)" % dimension)
        check(
            "T1-smoke-ran",
            all(pair in ldet_full for pair in C6_PAIRS_T1),
            "smoke L_det computed for %d pairs" % len(C6_PAIRS_T1),
        )

    section("T2  DEFLATED SECTORS")
    sectors = [
        ("full", None, -1),
        ("T20", np.array([20.0]), 0),
        ("T20", np.array([20.0]), 1),
        ("T20", np.array([20.0]), 2),
        ("T20_25", np.array([20.0, 25.0]), 1),
        ("Ttrue", true_t, 1),
    ]
    t2_rows = []
    for name, ordinates, m_jet in sectors:
        if ordinates is None:
            q_fn = q_full
            dim_k_th = 0
            n_t = 0
            t_list = []
        else:
            q_fn = sector_Q(cache, ordinates, m_jet)
            n_t = int(np.atleast_1d(ordinates).size)
            dim_k_th = dim_k_formula(m_jet, n_t)
            t_list = [float(val) for val in np.atleast_1d(ordinates)]

        floors = {}
        dim_v_at = {}
        rank_at = {}
        for length in l_star:
            pack = cache.zero_at(float(length))
            if ordinates is None:
                q_mat = q_full(float(length))
                dim_k_num = 0
                dim_v = dimension
            else:
                sec = cache.sector_at(float(length), ordinates, m_jet)
                q_mat = sec["Q"]
                dim_k_num = sec["dim_k"]
                dim_v = sec["dim_v"]
                resid = float(np.linalg.norm(sec["C"] @ q_mat)) if sec["C"].size and q_mat.size else 0.0
                emit(
                    "  %s m=%s L=%s  dimK_th=%d dimK_num=%d dimV=%d  ||CQ||=%s"
                    % (
                        name, m_jet, fmt(length, 2), dim_k_th, dim_k_num, dim_v,
                        fmt(resid, 4),
                    )
                )
            zs = zside_on_Q(pack, q_mat)
            floors[float(length)] = zs
            dim_v_at[float(length)] = zs["dim_v"]
            rank_at[float(length)] = dim_k_num if ordinates is not None else 0
            emit(
                "    λ*_V=%s  λ*_svd=%s  cond=%s  dimV=%d"
                % (
                    fmt(zs["lam"], 8), fmt(zs["lam_svd"], 8),
                    fmt(zs["cond"], 4), zs["dim_v"],
                )
            )

        ldet_sec = {}
        for beta, gamma in C6_PAIRS_T1:
            ldet_sec[(beta, gamma)] = scan_ldet(
                cache, q_fn, zeros, beta, gamma, c6_grid, 4.0,
            )
        in_t_20 = ordinates is not None and any(abs(val - 20.0) < 1.0e-12 for val in t_list)
        in_t_50 = ordinates is not None and any(abs(val - 50.0) < 1.0e-12 for val in t_list)
        g20a = ldet_sec[(0.6, 20.0)] - ldet_full[(0.6, 20.0)]
        g20b = ldet_sec[(0.9, 20.0)] - ldet_full[(0.9, 20.0)]
        g50 = ldet_sec[(0.6, 50.0)] - ldet_full[(0.6, 50.0)]
        row = {
            "name": name,
            "m": m_jet,
            "T": t_list,
            "n_T": n_t,
            "dim_k_th": dim_k_th,
            "floors": floors,
            "dim_v_at": dim_v_at,
            "rank_at": rank_at,
            "ldet": ldet_sec,
            "in_t_20": in_t_20,
            "in_t_50": in_t_50,
            "G_06_20": g20a,
            "G_09_20": g20b,
            "G_06_50": g50,
        }
        t2_rows.append(row)
        emit(
            "  %s m=%s  L_det (0.6,20)=%s%s (0.9,20)=%s%s (0.6,50)=%s%s"
            % (
                name, m_jet,
                shown_ldet(ldet_sec[(0.6, 20.0)], C6_L_LO, c6_step),
                " defl" if in_t_20 else " ctrl",
                shown_ldet(ldet_sec[(0.9, 20.0)], C6_L_LO, c6_step),
                " defl" if in_t_20 else " ctrl",
                shown_ldet(ldet_sec[(0.6, 50.0)], C6_L_LO, c6_step),
                " defl" if in_t_50 else " ctrl",
            )
        )
        emit(
            "    G (0.6,20)=%s  (0.9,20)=%s  (0.6,50)=%s"
            % (fmt(g20a, 4), fmt(g20b, 4), fmt(g50, 4))
        )

    # Rank gate at L=0.6 for T={20}, m=1.
    sec_ref = cache.sector_at(0.6, np.array([20.0]), 1)
    check(
        "T2-rank-T20-m1",
        sec_ref["dim_k"] == dim_k_formula(1, 1),
        "dimK_num=%d formula=%d dimV=%d" % (
            sec_ref["dim_k"], dim_k_formula(1, 1), sec_ref["dim_v"],
        ),
    )
    resid_ref = float(np.linalg.norm(sec_ref["C"] @ sec_ref["Q"])) if sec_ref["Q"].size else 0.0
    check(
        "T2-null-T20-m1",
        resid_ref <= 1.0e-8 * max(sec_ref["smax"], 1.0),
        "||CQ||=%s" % fmt(resid_ref, 6),
    )

    section("T3  COMPLEMENT BOOKKEEPING  (m=1, L=1.0, cover zeros to Γ)")
    t3_rows = []
    n_trial = N_FULL
    for gamma in T3_GAMMAS:
        n_asymp = n_riemann(gamma)
        n_act = int(np.sum(zeros <= gamma + 1.0e-12))
        n_nyq = n_nyquist(T3_L, gamma)
        dim_k_as = 2 * (T3_M + 1) * n_asymp
        dim_k_act = 2 * (T3_M + 1) * n_act
        ratio_n = dim_k_act / max(n_trial, 1)
        ratio_as = dim_k_as / max(n_trial, 1)
        ratio_nyq = dim_k_act / max(n_nyq, 1.0e-30)
        collapse_v = bool(dim_k_act >= n_trial - 0.5)
        over_nyq = bool(dim_k_act >= n_nyq)
        rec = {
            "Gamma": gamma,
            "N_asymp": n_asymp,
            "N_act": n_act,
            "n_nyq": n_nyq,
            "dimK_asymp": dim_k_as,
            "dimK_act": dim_k_act,
            "dimK_over_N": ratio_n,
            "dimK_over_N_asymp": ratio_as,
            "dimK_over_nyq": ratio_nyq,
            "collapse": collapse_v,
            "over_nyq": over_nyq,
            "dimV_left": max(n_trial - dim_k_act, 0),
        }
        t3_rows.append(rec)
        emit(
            "  Γ=%s  N~%s N_act=%d  dimK=2(m+1)|T|=%s  dimK/N=%s  "
            "Nyq=2LΓ/π=%s  dimK/Nyq=%s  V_left=%d  collapse_V=%d over_Nyq=%d"
            % (
                fmt(gamma, 2), fmt(n_asymp, 4), n_act, fmt(dim_k_act, 2),
                fmt(ratio_n, 4), fmt(n_nyq, 4), fmt(ratio_nyq, 4),
                rec["dimV_left"], int(collapse_v), int(over_nyq),
            )
        )
    ratio50 = t3_rows[0]["dimK_over_N"]
    collapse50 = t3_rows[0]["collapse"]
    check(
        "T3-ratios-finite",
        all(math.isfinite(row["dimK_over_N"]) for row in t3_rows),
        "Γ=50 dimK/N=%s" % fmt(ratio50, 4),
    )
    emit(
        "  reviewer kill: if dim K grows at the zero-counting rate, "
        "full coverage recoordinatizes the trial space.  "
        "At Γ=50, L=1, m=1: dimK/N=%s  (LARGE needs ≤0.2)."
        % fmt(ratio50, 4)
    )

    section("T4  POLE+ARCH ON V_{L,1}({20})  (odd-sector failure, r620)")
    t4_rows = []
    t20 = np.array([20.0])
    for length in t4_ls:
        free = cache.free_at(float(length))
        gram = free["gram"]
        a_mat = free["free"]
        lam_full, vec_full = min_rayleigh(a_mat, gram)
        mask = odd_mask(dimension)
        q_odd = np.eye(dimension, dtype=np.float64)[:, mask]
        lam_odd = rayleigh_on_Q(a_mat, gram, q_odd)
        sec = cache.sector_at(float(length), t20, 1)
        q_v = sec["Q"]
        lam_v = rayleigh_on_Q(a_mat, gram, q_v)
        # odd ∩ V: nullspace of jet constraints inside the odd subspace
        c_odd = jet_constraint_matrix(float(length), dimension, t20, 1)[:, mask]
        ns_odd = nullspace_basis(c_odd, int(np.count_nonzero(mask)))
        q_odd_v = q_odd @ ns_odd["Q"] if ns_odd["Q"].size else np.zeros((dimension, 0))
        lam_odd_v = rayleigh_on_Q(a_mat, gram, q_odd_v)
        peak_full, amp_full = peak_frequency(float(length), vec_full, connection)
        # odd ground state
        a_o, g_o = restrict_pencil(a_mat, gram, q_odd)
        _lam_o, vec_o_c = min_rayleigh(a_o, g_o)
        vec_odd = q_odd @ vec_o_c if vec_o_c.size else np.zeros(dimension)
        peak_odd, amp_odd = peak_frequency(float(length), vec_odd, connection)
        still_neg = bool(lam_full < 0.0 and lam_v < 0.0)
        lifted = bool(lam_full < -1.0e-12 and lam_v >= -1.0e-12)
        rec = {
            "L": float(length),
            "lam_full": lam_full,
            "lam_odd": lam_odd,
            "lam_V": lam_v,
            "lam_odd_V": lam_odd_v,
            "peak_full": peak_full,
            "peak_odd": peak_odd,
            "still_neg": still_neg,
            "lifted": lifted,
        }
        t4_rows.append(rec)
        emit(
            "  L=%s  λmin(A)=%s  odd=%s  V={20},m=1=%s  odd∩V=%s"
            % (
                fmt(length, 2), fmt(lam_full, 8), fmt(lam_odd, 8),
                fmt(lam_v, 8), fmt(lam_odd_v, 8),
            )
        )
        emit(
            "    |f̂| peak full t=%s  odd t=%s  (r620 failure ≲ %.1f, not 20)"
            % (fmt(peak_full, 4), fmt(peak_odd, 4), T4_PEAK_CUT)
        )
        emit(
            "    still_neg=%d  lifted_by_deflation=%d"
            % (int(still_neg), int(lifted))
        )
    t4_no_effect = all(
        (not row["lifted"]) and row["still_neg"] for row in t4_rows
    ) if t4_rows else False
    t4_finite = bool(t4_rows) and all(
        math.isfinite(row["lam_full"]) and math.isfinite(row["lam_V"])
        for row in t4_rows
    )
    check(
        "T4-finite",
        t4_finite,
        "deflation removes odd-sector A<0: %s; odd peak=%s" % (
            "yes (unexpected)" if (t4_rows and t4_rows[0]["lifted"]) else "no",
            fmt(t4_rows[0]["peak_odd"], 4) if t4_rows else "nan",
        ),
    )

    section("VERDICT")
    # Headline G: T={20}, m=1, deflated (0.6, 20).
    row_m1 = next(
        (row for row in t2_rows if row["name"] == "T20" and row["m"] == 1),
        None,
    )
    row_full = next((row for row in t2_rows if row["name"] == "full"), None)
    g_head = float("nan")
    g_ctrl = float("nan")
    g_09 = float("nan")
    if row_m1 is not None:
        g_head = float(row_m1["G_06_20"])
        g_ctrl = float(row_m1["G_06_50"])
        g_09 = float(row_m1["G_09_20"])
        if not math.isfinite(row_m1["ldet"][(0.6, 20.0)]):
            # never went negative on the scan: gain at least (scan_hi - baseline)
            base = ldet_full[(0.6, 20.0)]
            if math.isfinite(base):
                g_head = (c6_hi + c6_step) - base
    ctrl_moved = (
        math.isfinite(g_head) and math.isfinite(g_ctrl)
        and abs(g_ctrl) + 1.0e-12 >= abs(g_head) - CTRL_MOVE_TOL
        and abs(g_ctrl) >= 0.05
    )
    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    t1_gate_ok = all(ok for name, ok in CHECKS if name.startswith("T1-Ldet-"))
    if smoke:
        t1_gate_ok = all(ok for name, ok in CHECKS if name.startswith("PIN-") or name.startswith("T1-smoke"))

    G_LARGE = 0.3
    G_SMALL = 0.1
    g_cmp = g_head + 1.0e-12 if math.isfinite(g_head) else g_head
    if n_pass < n_gate:
        verdict = "INCONCLUSIVE"
        why = "gate failure: " + ",".join(name for name, ok in CHECKS if not ok)
    elif (not smoke) and (not t1_gate_ok):
        verdict = "INCONCLUSIVE"
        why = "T1 did not reproduce r619 L_det within ±0.05"
    elif (not math.isfinite(g_head)) or ctrl_moved or g_cmp < G_SMALL:
        verdict = "JET_NO_GAIN"
        if ctrl_moved:
            why = (
                "control L_det(0.6,50) moved as much as deflated "
                "G_ctrl=%s G=%s" % (fmt(g_ctrl, 4), fmt(g_head, 4))
            )
        else:
            why = "G=%s < 0.1 on T={20} m=1 (0.6,20)" % fmt(g_head, 4)
    elif g_cmp >= G_LARGE and ratio50 <= 0.2:
        verdict = "JET_GAIN_LARGE"
        why = (
            "G=%s ≥ 0.3 at T={20} m=1 and dimK/N=%s ≤ 0.2 at Γ=50"
            % (fmt(g_head, 4), fmt(ratio50, 4))
        )
    elif g_cmp >= G_SMALL:
        verdict = "JET_GAIN_SMALL"
        if g_cmp >= G_LARGE and ratio50 > 0.2:
            why = (
                "G=%s ≥ 0.3 but dimK/N=%s > 0.2 at Γ=50 "
                "(coverage kill: not LARGE)"
                % (fmt(g_head, 4), fmt(ratio50, 4))
            )
        else:
            why = "0.1 ≤ G=%s < 0.3 at T={20} m=1" % fmt(g_head, 4)
    else:
        verdict = "JET_NO_GAIN"
        why = "G=%s" % fmt(g_head, 4)

    payload = {
        "verdict": verdict,
        "g_head": g_head,
        "g_ctrl": g_ctrl,
        "ratio50": ratio50,
        "t1": {
            "%s_%s" % (beta, gamma): (
                ldet_full[(beta, gamma)] if math.isfinite(ldet_full[(beta, gamma)]) else None
            )
            for beta, gamma in C6_PAIRS_T1
        },
        "t2": [
            {
                "name": row["name"], "m": row["m"],
                "lam06": row["floors"].get(0.6, {}).get("lam") if 0.6 in row["floors"] else (
                    row["floors"][min(row["floors"], key=lambda x: abs(x - 0.6))]["lam"]
                    if row["floors"] else None
                ),
                "G06": row["G_06_20"] if math.isfinite(row["G_06_20"]) else None,
                "G50": row["G_06_50"] if math.isfinite(row["G_06_50"]) else None,
            }
            for row in t2_rows
        ],
        "t4_no_effect": t4_no_effect,
    }
    result_sha = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    ).hexdigest()
    wall = time.time() - wall0

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
    emit("fence %s" % FENCE)

    section("STATE")
    emit("STATE r%d %s" % (ROUND, CONTRACT))
    emit("SHA %s" % file_sha256())
    emit("SPEC %s" % SPEC_SHA)
    emit("RESULT %s" % result_sha)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("T1 L_det (0.6,20)=%s (0.9,20)=%s (0.6,50)=%s  r619 0.55/0.50/0.80" % (
        shown_ldet(ldet_full[(0.6, 20.0)], C6_L_LO, c6_step),
        shown_ldet(ldet_full[(0.9, 20.0)], C6_L_LO, c6_step),
        shown_ldet(ldet_full[(0.6, 50.0)], C6_L_LO, c6_step),
    ))
    emit("T2 sector m λ*V@0.6 λ*V@1.0 Ldet(0.6,20) Ldet(0.9,20) Ldet(0.6,50) G20 G50")
    for row in t2_rows:
        def pick(target):
            if not row["floors"]:
                return float("nan")
            if target in row["floors"]:
                return row["floors"][target]["lam"]
            nearest = min(row["floors"], key=lambda x: abs(x - target))
            if abs(nearest - target) < 0.06:
                return row["floors"][nearest]["lam"]
            return float("nan")

        emit(
            "  %s m=%s  %s %s  %s %s %s  G20=%s G50=%s"
            % (
                row["name"], row["m"],
                fmt(pick(0.6), 4), fmt(pick(1.0), 4),
                shown_ldet(row["ldet"][(0.6, 20.0)], C6_L_LO, c6_step),
                shown_ldet(row["ldet"][(0.9, 20.0)], C6_L_LO, c6_step),
                shown_ldet(row["ldet"][(0.6, 50.0)], C6_L_LO, c6_step),
                fmt(row["G_06_20"], 3), fmt(row["G_06_50"], 3),
            )
        )
    emit("T2 headline T={20} m=1  G(0.6,20)=%s G(0.9,20)=%s Gctrl(0.6,50)=%s" % (
        fmt(g_head, 4), fmt(g_09, 4), fmt(g_ctrl, 4),
    ))
    emit("T3 m=1 L=1.0 N=%d  " % N_FULL + "  ".join(
        "Γ=%s Nact=%d dimK=%s dimK/N=%s Nyq=%s collV=%d overNyq=%d" % (
            fmt(row["Gamma"], 0), row["N_act"], fmt(row["dimK_act"], 1),
            fmt(row["dimK_over_N"], 3), fmt(row["n_nyq"], 2),
            int(row["collapse"]), int(row["over_nyq"]),
        )
        for row in t3_rows
    ))
    if t4_rows:
        emit("T4 L=%s λA=%s λV=%s λodd=%s peak_odd=%s no_effect=%d" % (
            fmt(t4_rows[0]["L"], 2), fmt(t4_rows[0]["lam_full"], 4),
            fmt(t4_rows[0]["lam_V"], 4), fmt(t4_rows[0]["lam_odd"], 4),
            fmt(t4_rows[0]["peak_odd"], 3), int(t4_no_effect),
        ))
    emit("smoke %d  N %d  n_zeros %d  wall_s %s" % (
        int(smoke), dimension, n_zeros, fmt(wall, 4),
    ))
    emit(FENCE)
    emit("END_STATE")
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r632 jet-deflated L_det scout (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
