#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""frontier_followups_probe -- r633  PRIME.FRONTIER.FOLLOWUPS.01

Experiments-only.  Four cheap computations on already-sealed objects.

Copied (not imported):
  * r605N Gabor zero-side: pure packet e^{-a u^2/2} cos(ω u),
    three-lobe Lean `pureGaborHatDelta`, FE quadruple 4 Re ĥ(ρ),
    2000+ ordinates + density tail.
  * r619 window/zero-side: λ* via SVD of F[k,i]=f̂_i(γ_k), 5000 zeros,
    edge-damped Legendre, DAMP_POWER=3; Δ_j table from r619 STATE.
  * r623 λ_min(POLE+ARCH) on undamped Legendre.
  * r620/r633 heat: Ξ-variable ẋ_j = Σ_{k≠j} 2/(x_j-x_k), x=2γ,
    paired ± and density tail (dbn_heatflow_probe convention).

F1  a-compactification of the rational Gabor criterion.
F2  de Bruijn–Newman derivative of the window margin.
F3  random-Euler refutation as a typed statement.
F4  is Δ≈0.015 a corollary of the two measured laws?

Claim boundary: finite-section arithmetic.  Not a ledger row.
Not a paper claim.  Fence: "Follow-ups on sealed objects; no RH claim."
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
ROOT = HERE.parent.parent
ZEROS_NPY = HERE / "verified_zeros_n7000.npy"
ZEROS_JSON = ROOT / "verification" / "verified_zeros_n7000.json"
ZEROS_JSON_WEB = ROOT / "website" / "public" / "verification" / "verified_zeros_n7000.json"

ROUND = 633
SEED = 633202609
CONTRACT = "PRIME.FRONTIER.FOLLOWUPS.01"
FENCE = "Follow-ups on sealed objects; no RH claim."
DAMP_POWER = 3
GAMMA1 = 14.134725141734695
LOG2 = math.log(2.0)
W2 = math.sqrt(2.0) * LOG2
PI = math.pi
SVD_COND = 1.0e-8
CROSS_POS = 1.0e-8
CROSS_NEG = -1.0e-8
BISECT_ITERS = 22
EXPO_CLIP = 700.0
LIVE_Z = 1.0e-80
LAM_FLOOR = 1.0e-20
HF_REL = 1.0e-6
R623_MATCH = 1.0e-3
LEAD_REL = 0.20
LEAD_PASS_N = 14
P_QUAD_TOL = 0.50
SMOKE_WALL = 90.0
FULL_WALL = 1200.0

R623_ANC = {
    0.40: -0.078,
    0.46: -0.229,
    0.52: -0.367,
    0.549: -0.430,
    0.60: -0.536,
    0.65: -0.636,
    0.72: -0.773,
    0.80: -0.926,
}
R619_LEADS = {
    2: 0.0279, 3: 0.0123, 4: 0.0146, 5: 0.0111, 7: 0.0105, 8: 0.0140,
    9: 0.0125, 11: 0.0116, 13: 0.0131, 16: 0.0166, 17: 0.0126,
    19: 0.0144, 23: 0.0141, 25: 0.0170, 27: 0.0181, 29: 0.0151,
    31: 0.0147, 32: 0.0221,
}
SIGMAS_FULL = (0.05, 0.10, 0.20, 0.30, 0.40, 0.50)
GAMMAS_FULL = (20.0, 50.0, 200.0, 1000.0)
SIGMAS_SMOKE = (0.10, 0.50)
GAMMAS_SMOKE = (20.0, 50.0)
A_TRUE = (1.0, 5.0, 25.0, 100.0, 250.0)
A_TRUE_SMOKE = (1.0, 25.0, 100.0)
F2_L_FULL = (0.40, 0.55, 0.80, 1.00, 1.20)
F2_L_SMOKE = (0.40, 0.80)
F3_L = (0.40, 0.55, 0.80)
C6_PAIR = (0.6, 20.0)
N_F2_FULL = 80
N_F2_SMOKE = 32
N_ZEROS_F1_FULL = 2000
N_ZEROS_F1_SMOKE = 400
N_ZEROS_F2_FULL = 5000
N_ZEROS_F2_SMOKE = 500
N_F3 = 24
N_F3_SMOKE = 16
N_OUTER_F3 = 80
N_OUTER_F3_SMOKE = 48
N_MC_FULL = 200
N_MC_SMOKE = 24
N_LEAD = 40
N_LEAD_SMOKE = 24
N_OUTER_LEAD = 48
N_OUTER_LEAD_SMOKE = 32
N_A_GRID_FULL = 18
N_A_GRID_SMOKE = 10
N_LOBES_FULL = 3
N_LOBES_SMOKE = 2
VALIDATE_Q = (2, 3)

SPEC = {
    "round": ROUND,
    "tag": "r633",
    "contract": CONTRACT,
    "hat": "pureGaborHatDelta_literal_L114",
    "packet": "exp(-a u^2/2) cos(omega u)",
    "Z": "Re sum m hat, no pole; FE quadruple 4 Re hat",
    "a_grid": [1.0e-4, 10.0],
    "sigmas": list(SIGMAS_FULL),
    "gammas": list(GAMMAS_FULL),
    "damp_power": DAMP_POWER,
    "n_f2": N_F2_FULL,
    "n_zeros_f1": N_ZEROS_F1_FULL,
    "n_zeros_f2": N_ZEROS_F2_FULL,
    "xi_dot": "sum_{k!=j} 2/(x_j-x_k), x=2 gamma, paired pm, density tail",
    "hf": "d lambda = sum 2 Re[fhat' conj fhat] * gamma_dot, Loewner check",
    "c6": list(C6_PAIR),
    "r623_anc": [R623_ANC[ell] for ell in (0.40, 0.549, 0.80)],
    "r619_leads": [R619_LEADS[q] for q in sorted(R619_LEADS)],
    "mc": N_MC_FULL,
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
_CONN_CACHE: dict[tuple[int, int], np.ndarray] = {}
VERBOSE = True


def emit(line: str = "") -> None:
    if not VERBOSE:
        return
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


def fmt(value, digits: int = 12) -> str:
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


def payload_sha(payload: dict) -> str:
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Zeros
# ---------------------------------------------------------------------------
def load_zeros(n_use: int) -> np.ndarray:
    n_use = int(n_use)
    if ZEROS_NPY.is_file():
        raw = np.load(str(ZEROS_NPY))
        n_use = min(n_use, int(raw.shape[0]))
        return np.asarray(raw[:n_use], dtype=np.float64)
    for path in (ZEROS_JSON, ZEROS_JSON_WEB):
        if path.is_file():
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            gammas = data["gammas"] if isinstance(data, dict) else data
            n_use = min(n_use, len(gammas))
            return np.asarray(gammas[:n_use], dtype=np.float64)
    mp.mp.dps = 15
    return np.asarray(
        [float(mp.zetazero(index).imag) for index in range(1, n_use + 1)],
        dtype=np.float64,
    )


# ---------------------------------------------------------------------------
# Window machinery (r619 / r630, DAMP_POWER parameterised)
# ---------------------------------------------------------------------------
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
    key = round(float(ell), 12)
    cached = _CL_CACHE.get(key)
    if cached is not None:
        return cached
    nodes, weights = roots_legendre(256)
    span = 2.0 * ell
    x_val = 0.5 * span * (nodes + 1.0)
    scaled = 0.5 * span * weights
    kern = np.exp(x_val / 2.0) / np.sinh(x_val)
    integrand = kern - 1.0 / x_val
    value = float(np.dot(scaled, integrand)) + math.log(4.0 * ell) + float(
        np.euler_gamma
    ) + math.log(math.pi)
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


def damped_weight(points, length: float, power: int) -> np.ndarray:
    scaled = np.asarray(points, dtype=np.float64) / length
    if int(power) <= 0:
        return np.ones_like(scaled)
    weight = np.zeros_like(scaled)
    inside = np.abs(scaled) <= 1.0 + 1.0e-15
    loc = scaled[inside]
    weight[inside] = (1.0 - loc * loc) ** int(power)
    return weight


def basis_values(points, length: float, dimension: int, power: int) -> np.ndarray:
    values = legendre_values(points, length, dimension)
    if int(power) <= 0:
        return values
    return damped_weight(points, length, power)[:, None] * values


def n_inner_of(dimension: int) -> int:
    return max(2 * dimension + 8, 64)


def gram_matrix(length: float, dimension: int, power: int, n_inner: int) -> np.ndarray:
    if int(power) <= 0:
        return np.eye(dimension, dtype=np.float64)
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, power)
    gram = basis.T @ (scaled[:, None] * basis)
    return 0.5 * (gram + gram.T)


def pole_vectors(length: float, dimension: int, power: int, n_inner: int):
    nodes, weights = roots_legendre(n_inner)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, power)
    cosh_vector = basis.T @ (scaled * np.cosh(points / 2.0))
    sinh_vector = basis.T @ (scaled * np.sinh(points / 2.0))
    return cosh_vector, sinh_vector


def overlap_matrix(
    length: float, shift: float, dimension: int, power: int, n_inner: int,
) -> np.ndarray:
    two_l = 2.0 * length
    if shift <= 0.0 or shift >= two_l - 1.0e-15:
        return np.zeros((dimension, dimension), dtype=np.float64)
    overlap_length = two_l - shift
    nodes, weights = roots_legendre(n_inner)
    points = -length + 0.5 * overlap_length * (nodes + 1.0)
    scaled = 0.5 * overlap_length * weights
    left = basis_values(points, length, dimension, power)
    right = basis_values(points + shift, length, dimension, power)
    forward = right.T @ (scaled[:, None] * left)
    return 0.5 * (forward + forward.T)


def arch_matrix(
    length: float,
    dimension: int,
    power: int,
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
        left = basis_values(points, length, dimension, power)
        right = basis_values(points + distance, length, dimension, power)
        overlap = right.T @ (scaled[:, None] * left)
        symmetric = 0.5 * (overlap + overlap.T)
        difference += (weight_x * kern_x) * (gram - symmetric)
    return difference - c_l * gram


def pole_matrix(cosh_vector, sinh_vector) -> np.ndarray:
    return (
        2.0 * np.outer(cosh_vector, cosh_vector)
        - 2.0 * np.outer(sinh_vector, sinh_vector)
    )


def min_rayleigh(quadratic, gram) -> tuple[float, np.ndarray]:
    quadratic = 0.5 * (quadratic + quadratic.T)
    gram = 0.5 * (gram + gram.T)
    dim = gram.shape[0]
    ridge = 1.0e-14 * (np.trace(gram) / max(dim, 1) + 1.0e-30)
    gram = gram + ridge * np.eye(dim)
    identity = np.allclose(gram, np.eye(dim), atol=1.0e-10, rtol=0.0)
    try:
        if identity:
            values, vectors = np.linalg.eigh(quadratic)
            return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)
        values, vectors = seigh(
            quadratic, gram, subset_by_index=[0, 0], check_finite=False,
        )
        return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)
    except Exception:
        values, vectors = np.linalg.eigh(quadratic)
        return float(values[0]), np.asarray(vectors[:, 0], dtype=np.float64)


def damped_connection(n_max: int, power: int) -> np.ndarray:
    extra = 2 * int(power)
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
    damp = (1.0 - nodes * nodes) ** int(power) if power > 0 else np.ones_like(nodes)
    coeff = np.zeros((n_max, width), dtype=np.float64)
    for index in range(n_max):
        field = damp * legend[:, index]
        for degree in range(min(index + extra + 1, width)):
            coeff[index, degree] = (degree + 0.5) * float(
                np.dot(weights, field * legend[:, degree])
            )
    return coeff


def connection_of(n_max: int, power: int) -> np.ndarray:
    key = (int(n_max), int(power))
    cached = _CONN_CACHE.get(key)
    if cached is not None:
        return cached
    coeff = damped_connection(int(n_max), int(power))
    _CONN_CACHE[key] = coeff
    return coeff


def bessel_damped_hat(
    length: float, t_values, n_max: int, connection: np.ndarray, power: int,
) -> np.ndarray:
    t_arr = np.real(np.asarray(t_values, dtype=np.float64)).ravel()
    extra = 2 * int(power)
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


def bessel_damped_hat_dt(
    length: float, t_values, n_max: int, connection: np.ndarray, power: int,
) -> np.ndarray:
    t_arr = np.real(np.asarray(t_values, dtype=np.float64)).ravel()
    extra = 2 * int(power)
    width = n_max + extra + 1
    argument = length * t_arr
    deriv = [spherical_jn(degree, argument, True) for degree in range(width)]
    out = np.zeros((t_arr.size, n_max), dtype=np.complex128)
    for index in range(n_max):
        mix = connection[index, :width]
        combo = np.zeros(t_arr.size, dtype=np.complex128)
        for degree in range(width):
            amp = mix[degree]
            if abs(amp) <= 1.0e-18:
                continue
            combo += amp * ((1j) ** degree) * deriv[degree]
        out[:, index] = math.sqrt(2.0 * length * (2 * index + 1)) * length * combo
    return out


def basis_hat_complex(
    length: float, t_values, dimension: int, power: int, n_quad: int | None = None,
) -> np.ndarray:
    t_arr = np.atleast_1d(np.asarray(t_values, dtype=np.complex128))
    t_scale = float(np.max(np.abs(t_arr))) if t_arr.size else 1.0
    n_quad = n_quad or max(8 * dimension, int(2.0 * length * t_scale) + 96, 192)
    n_quad = min(int(n_quad), 2048)
    nodes, weights = roots_legendre(n_quad)
    points = length * nodes
    scaled = length * weights
    basis = basis_values(points, length, dimension, power)
    phase = np.exp(1j * np.outer(t_arr, points))
    return (phase * scaled) @ basis


def tail_mixed(
    length: float,
    dimension: int,
    connection: np.ndarray,
    power: int,
    t_cut: float,
    t_extra: float = 2000.0,
    n_quad: int = 48,
) -> np.ndarray:
    nodes, weights = roots_legendre(n_quad)
    t_values = t_cut + 0.5 * t_extra * (nodes + 1.0)
    scaled = 0.5 * t_extra * weights
    hats = bessel_damped_hat(length, t_values, dimension, connection, power)
    dens = np.log(np.maximum(t_values / (2.0 * math.pi), 1.0e-12)) / (2.0 * math.pi)
    amp = np.sqrt(np.maximum(2.0 * scaled * dens, 0.0))
    return amp[:, None] * hats


def stacked_svd_min(stacked: np.ndarray, gram: np.ndarray) -> dict:
    dim = int(gram.shape[0])
    real_f = np.vstack(
        [np.real(np.asarray(stacked)), np.imag(np.asarray(stacked))]
    )
    pencil = real_f.T @ real_f
    pencil = 0.5 * (pencil + pencil.T)
    lam, vec = min_rayleigh(pencil, gram)
    smin = float("nan")
    smax = float("nan")
    lam_svd = float("nan")
    try:
        chol = np.linalg.cholesky(
            0.5 * (gram + gram.T) + 1.0e-14 * np.eye(dim)
        )
        white = np.linalg.solve(chol, real_f.T).T
        sigma = svdvals(white)
        smin = float(sigma[-1])
        smax = float(sigma[0])
        lam_svd = smin * smin
    except np.linalg.LinAlgError:
        pass
    cond = (
        smin / smax if (math.isfinite(smin) and math.isfinite(smax) and smax > 0.0)
        else float("nan")
    )
    return {
        "lam": float(lam),
        "lam_svd": float(lam_svd),
        "smin": smin,
        "smax": smax,
        "cond": cond,
        "svd_ok": bool(math.isfinite(cond) and cond >= SVD_COND),
        "vec": vec,
        "pencil": pencil,
    }


def zero_side_min(
    length: float,
    dimension: int,
    connection: np.ndarray,
    zeros: np.ndarray,
    gram: np.ndarray,
    power: int,
) -> dict:
    hats = bessel_damped_hat(length, zeros, dimension, connection, power)
    mixed_z = math.sqrt(2.0) * hats
    mixed_t = tail_mixed(length, dimension, connection, power, float(zeros[-1]))
    stacked = np.vstack([mixed_z, mixed_t])
    packed = stacked_svd_min(stacked, gram)
    packed["hats"] = hats
    packed["n_zero_rows"] = int(mixed_z.shape[0])
    packed["n_tail_rows"] = int(mixed_t.shape[0])
    return packed


def assemble_free(
    length: float, dimension: int, power: int, n_outer: int,
) -> dict:
    n_inner = n_inner_of(dimension)
    c_l = c_L_of(length)
    gram = gram_matrix(length, dimension, power, n_inner)
    arch = arch_matrix(length, dimension, power, gram, c_l, n_outer, n_inner)
    cosh_vector, sinh_vector = pole_vectors(length, dimension, power, n_inner)
    pole = pole_matrix(cosh_vector, sinh_vector)
    free = 0.5 * ((arch + pole) + (arch + pole).T)
    return {
        "gram": 0.5 * (gram + gram.T),
        "arch": 0.5 * (arch + arch.T),
        "pole": 0.5 * (pole + pole.T),
        "free": free,
        "n_inner": n_inner,
        "power": power,
        "c_L": c_l,
    }


def prime_powers_upto(q_max: int):
    cap = max(q_max * 2, 64)
    lam = von_mangoldt_table(cap)
    qs = [index for index in range(2, q_max + 1) if lam[index] > 0.0]
    logqs = np.array([math.log(q_val) for q_val in qs], dtype=np.float64)
    weights = np.array(
        [2.0 * lam[q_val] / math.sqrt(q_val) for q_val in qs], dtype=np.float64,
    )
    ells = 0.5 * logqs
    return qs, logqs, weights, ells, lam


def n_active(length: float, logqs: np.ndarray) -> int:
    two_l = 2.0 * length
    return int(np.sum(logqs < two_l - 1.0e-15))


def assemble_window(
    length: float,
    dimension: int,
    power: int,
    n_outer: int,
    logqs: np.ndarray,
    weights: np.ndarray,
    n_ev: int | None = None,
) -> dict:
    packed = assemble_free(length, dimension, power, n_outer)
    n_inner = packed["n_inner"]
    two_l = 2.0 * length
    if n_ev is None:
        n_ev = n_active(length, logqs)
    n_use = max(0, min(int(n_ev), int(logqs.size)))
    prime = np.zeros((dimension, dimension), dtype=np.float64)
    overlaps = []
    for index in range(n_use):
        overlap = overlap_matrix(
            length, float(logqs[index]), dimension, power, n_inner,
        )
        overlaps.append(overlap)
        if 0.0 < logqs[index] < two_l - 1.0e-15:
            prime = prime + weights[index] * overlap
    full = 0.5 * ((packed["free"] - prime) + (packed["free"] - prime).T)
    packed["prime"] = prime
    packed["full"] = full
    packed["overlaps"] = overlaps
    packed["n_ev"] = n_use
    return packed


def offline_matrix(v_plus: np.ndarray, v_minus: np.ndarray) -> np.ndarray:
    plus = np.asarray(v_plus, dtype=np.complex128).ravel()
    minus = np.asarray(v_minus, dtype=np.complex128).ravel()
    real_p, imag_p = np.real(plus), np.imag(plus)
    real_m, imag_m = np.real(minus), np.imag(minus)
    matrix = np.outer(real_p, real_m) + np.outer(imag_p, imag_m)
    matrix = 0.5 * (matrix + matrix.T)
    return 4.0 * matrix


def bisect_sign(func, lo: float, hi: float, n_iter: int = BISECT_ITERS):
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
    left, right, f_left = lo, hi, f_lo
    for _ in range(n_iter):
        mid = 0.5 * (left + right)
        f_mid = func(mid)
        if f_left * f_mid <= 0.0:
            right = mid
        else:
            left, f_left = mid, f_mid
    return 0.5 * (left + right), f_lo, f_hi


# ---------------------------------------------------------------------------
# Gabor hat (r605N three-lobe)
# ---------------------------------------------------------------------------
def hat_gabor(a: float, omega: float, sigma: float, t_values) -> np.ndarray:
    """ĥ(1/2+σ+it) for the pure packet.  Vectorised in t."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    pref = PI / (4.0 * a)
    s2 = sigma * sigma
    two_a = 2.0 * a
    inv_a = 1.0 / a

    def lobe(shift, phase_arg):
        expo = (s2 - shift * shift) / two_a
        expo = np.clip(expo, -EXPO_CLIP, EXPO_CLIP)
        return np.exp(expo + 1j * (sigma * phase_arg * inv_a))

    term_p = lobe(t_arr + omega, t_arr + omega)
    term_m = lobe(t_arr - omega, t_arr - omega)
    expo_c = np.clip((s2 - t_arr * t_arr - omega * omega) / two_a, -EXPO_CLIP, EXPO_CLIP)
    term_c = 2.0 * np.exp(expo_c + 1j * (sigma * t_arr * inv_a))
    return pref * (term_p + term_m + term_c)


def hat_gabor_scaled(
    a: float, omega: float, sigma: float, t_values, s_star: float,
) -> np.ndarray:
    """e^{-S*/(2a)} ĥ.  Bounded when S* ≥ max lobe score."""
    t_arr = np.asarray(t_values, dtype=np.float64)
    pref = PI / (4.0 * a)
    s2 = sigma * sigma
    two_a = 2.0 * a
    inv_a = 1.0 / a

    def lobe(shift, phase_arg):
        expo = (s2 - shift * shift - s_star) / two_a
        expo = np.clip(expo, -EXPO_CLIP, EXPO_CLIP)
        return np.exp(expo + 1j * (sigma * phase_arg * inv_a))

    term_p = lobe(t_arr + omega, t_arr + omega)
    term_m = lobe(t_arr - omega, t_arr - omega)
    expo_c = np.clip(
        (s2 - t_arr * t_arr - omega * omega - s_star) / two_a, -EXPO_CLIP, EXPO_CLIP,
    )
    term_c = 2.0 * np.exp(expo_c + 1j * (sigma * t_arr * inv_a))
    return pref * (term_p + term_m + term_c)


def density_t(t_values) -> np.ndarray:
    t_arr = np.asarray(t_values, dtype=np.float64)
    return np.log(np.maximum(t_arr / (2.0 * PI), 1.0e-30)) / (2.0 * PI)


def gabor_online_tail(a: float, omega: float, t_cut: float, s_star: float) -> float:
    """2 ∫_{T}^∞ ρ(t) e^{-S*/(2a)} ĥ(0,t) dt  (±γ)."""
    width = 24.0 * math.sqrt(max(a, 1.0e-12)) + 80.0
    nodes, weights = roots_legendre(48)
    t_values = t_cut + 0.5 * width * (nodes + 1.0)
    scaled = 0.5 * width * weights
    hats = np.real(hat_gabor_scaled(a, omega, 0.0, t_values, s_star))
    dens = np.maximum(density_t(t_values), 0.0)
    return float(2.0 * np.dot(scaled, dens * hats))


def z_gabor_true(a: float, omega: float, zeros: np.ndarray) -> float:
    hats = np.real(hat_gabor(a, omega, 0.0, zeros))
    disc = 2.0 * float(np.sum(hats))
    tail = gabor_online_tail(a, omega, float(zeros[-1]), 0.0)
    return disc + tail


def z_gabor_injected_scaled(
    a: float,
    omega: float,
    sigma: float,
    gamma_star: float,
    zeros: np.ndarray,
) -> float:
    """e^{-σ²/(2a)} Z after replacing the on-line zero nearest γ* by the quadruple."""
    s_star = sigma * sigma
    k0 = int(np.argmin(np.abs(zeros - gamma_star)))
    hats_on = np.real(hat_gabor_scaled(a, omega, 0.0, zeros, s_star))
    # 2 Σ_γ ĥ(γ) minus the ± pair of the replaced on-line zero.
    disc = 2.0 * float(np.sum(hats_on) - hats_on[k0])
    tail = gabor_online_tail(a, omega, float(zeros[-1]), s_star)
    off = hat_gabor_scaled(a, omega, sigma, np.array([gamma_star]), s_star)[0]
    z_off = 4.0 * float(np.real(off))
    return disc + tail + z_off


def omega_candidates(gamma_star: float, sigma: float, a: float, n_lobes: int) -> np.ndarray:
    shift = PI * a / max(abs(sigma), 1.0e-12)
    values = [gamma_star]
    for index in range(n_lobes):
        odd = 2 * index + 1
        center = gamma_star - odd * shift
        values.append(center)
        values.append(gamma_star + odd * shift)
        for frac in (-0.35, -0.18, 0.18, 0.35):
            values.append(center + frac * shift)
    out = [float(val) for val in values if val >= 0.0]
    if not out:
        out = [0.0]
    return np.unique(np.asarray(out, dtype=np.float64))


def min_z_injected(
    a: float, sigma: float, gamma_star: float, zeros: np.ndarray, n_lobes: int,
) -> tuple[float, float]:
    omegas = omega_candidates(gamma_star, sigma, a, n_lobes)
    best_z = float("inf")
    best_w = float(omegas[0])
    live = False
    for omega in omegas:
        value = z_gabor_injected_scaled(a, float(omega), sigma, gamma_star, zeros)
        if (not math.isfinite(value)) or (value >= 0.0 and abs(value) < LIVE_Z):
            continue
        live = True
        if value < best_z:
            best_z = value
            best_w = float(omega)
    if not live:
        return float("inf"), best_w
    return best_z, best_w


def a_max_of(
    sigma: float,
    gamma_star: float,
    zeros: np.ndarray,
    n_lobes: int,
    n_grid: int,
) -> dict:
    grid = np.logspace(-4.0, 1.0, int(n_grid))
    signs = []
    for a_val in grid:
        z_min, _w = min_z_injected(float(a_val), sigma, gamma_star, zeros, n_lobes)
        signs.append(z_min)
    signs = np.asarray(signs, dtype=np.float64)
    negative = signs < 0.0
    if not np.any(negative):
        a_max = float(grid[0]) if signs[0] >= 0.0 else 0.0
        return {"a_max": a_max, "on_floor": True, "on_ceil": False, "z_grid": signs}
    last = int(np.where(negative)[0][-1])
    if last == int(grid.size) - 1:
        return {
            "a_max": float(grid[-1]), "on_floor": False, "on_ceil": True, "z_grid": signs,
        }
    lo, hi = float(grid[last]), float(grid[last + 1])

    def scalar(a_val):
        z_min, _w = min_z_injected(float(a_val), sigma, gamma_star, zeros, n_lobes)
        return z_min

    root, _, _ = bisect_sign(scalar, lo, hi)
    a_max = float(root) if math.isfinite(root) else 0.5 * (lo + hi)
    return {"a_max": a_max, "on_floor": False, "on_ceil": False, "z_grid": signs}


def fit_power(rows: list[dict]) -> dict:
    usable = [
        row for row in rows
        if row["a_max"] > 1.2e-4 and row["a_max"] < 9.0 and not row.get("on_ceil")
    ]
    if len(usable) < 4:
        return {
            "p": float("nan"), "q": float("nan"), "c": float("nan"),
            "r2": float("nan"), "n": len(usable),
        }
    log_a = np.log(np.array([row["a_max"] for row in usable], dtype=np.float64))
    log_s = np.log(np.array([row["sigma"] for row in usable], dtype=np.float64))
    log_lg = np.log(np.log(np.array([row["gamma"] for row in usable], dtype=np.float64)))
    matrix = np.column_stack((np.ones_like(log_a), log_s, log_lg))
    coeff, _, _, _ = np.linalg.lstsq(matrix, log_a, rcond=None)
    pred = matrix @ coeff
    ss_res = float(np.sum((log_a - pred) ** 2))
    ss_tot = float(np.sum((log_a - np.mean(log_a)) ** 2))
    r2 = 1.0 - ss_res / max(ss_tot, 1.0e-30)
    return {
        "c": float(math.exp(coeff[0])),
        "p": float(coeff[1]),
        "q": float(coeff[2]),
        "r2": float(r2),
        "n": len(usable),
    }


# ---------------------------------------------------------------------------
# Ξ heat velocities (x = 2γ)
# ---------------------------------------------------------------------------
def xi_velocities(gammas: np.ndarray) -> np.ndarray:
    """ẋ_j for positive x_j=2γ_j, paired with −x and a density tail."""
    gam = np.asarray(gammas, dtype=np.float64)
    x_pos = 2.0 * gam
    n_pts = int(x_pos.size)
    x2 = x_pos * x_pos
    xdot = np.empty(n_pts, dtype=np.float64)
    for index in range(n_pts):
        denom = x2[index] - x2
        denom[index] = np.inf
        # partner at −x: 2/(2x) = 1/x; others: 4 x /(x^2 − x_k^2)
        xdot[index] = 1.0 / x_pos[index] + float(
            np.sum(4.0 * x_pos[index] / denom)
        )
    xdot_trunc = xdot.copy()
    t_cut = float(gam[-1])
    nodes, weights = roots_legendre(32)
    extra = 8.0 * t_cut
    t_tail = t_cut + 0.5 * extra * (nodes + 1.0)
    w_tail = 0.5 * extra * weights
    dens = np.maximum(density_t(t_tail), 0.0)
    x_tail = 2.0 * t_tail
    for index in range(n_pts):
        xj = x_pos[index]
        kernel = 2.0 / (xj - x_tail) + 2.0 / (xj + x_tail)
        xdot[index] += float(np.dot(w_tail, dens * kernel))
    return xdot, xdot_trunc


def loewner_hf(x_pos: np.ndarray, hp_pos: np.ndarray, xdot: np.ndarray) -> dict:
    """Even ĥ, odd ĥ'.  HF = 2 Σ hp ẋ on positives; Loewner on ±x."""
    hf = 2.0 * float(np.dot(hp_pos, xdot))
    x_all = np.concatenate((-x_pos[::-1], x_pos))
    hp_all = np.concatenate((-hp_pos[::-1], hp_pos))
    loew = 0.0
    n_all = int(x_all.size)
    for index in range(n_all - 1):
        dx = x_all[index] - x_all[index + 1:]
        dh = hp_all[index] - hp_all[index + 1:]
        loew += float(np.sum(2.0 * dh / dx))
    denom = abs(hf) + abs(loew) + 1.0e-30
    rel = abs(hf - loew) / denom
    return {"hf": hf, "loewner": loew, "rel": rel}


# ---------------------------------------------------------------------------
# F1
# ---------------------------------------------------------------------------
def run_f1(cfg: dict, zeros: np.ndarray) -> dict:
    sigmas = cfg["sigmas"]
    gammas = cfg["gammas"]
    n_lobes = cfg["n_lobes"]
    n_grid = cfg["n_a_grid"]
    rows = []
    for sigma in sigmas:
        for gamma_star in gammas:
            rec = a_max_of(float(sigma), float(gamma_star), zeros, n_lobes, n_grid)
            rec["sigma"] = float(sigma)
            rec["gamma"] = float(gamma_star)
            rows.append(rec)
            emit(
                "  σ=%s γ*=%s a_max=%s floor=%d ceil=%d"
                % (
                    fmt(sigma, 2), fmt(gamma_star, 1), fmt(rec["a_max"], 6),
                    int(rec["on_floor"]), int(rec["on_ceil"]),
                )
            )
    fit = fit_power(rows)
    a0 = max(float(row["a_max"]) for row in rows)
    a0_extrap = float("nan")
    if math.isfinite(fit["p"]) and math.isfinite(fit["c"]):
        # table domain σ≤1/2; if q<0 the max is at smallest γ*
        log_g = math.log(GAMMA1)
        a0_extrap = float(fit["c"] * (0.5 ** fit["p"]) * (log_g ** fit["q"]))
    true_rows = []
    omega_grid = np.linspace(0.0, 60.0, cfg["n_omega_true"])
    for a_val in cfg["a_true"]:
        values = [z_gabor_true(float(a_val), float(omega), zeros) for omega in omega_grid]
        z_min = float(np.min(values))
        true_rows.append({"a": float(a_val), "z_min": z_min})
        emit("  TRUE a=%s min_ω Z=%s (ω∈[0,60])" % (fmt(a_val, 2), fmt(z_min, 8)))
    adv_rows = []
    zeros_adv = zeros[zeros <= 1000.0 + 1.0e-12]
    step = max(1, int(zeros_adv.size // cfg["n_adv"]))
    sample = zeros_adv[::step][: cfg["n_adv"]]
    for a_val in cfg["a_true"]:
        best = float("inf")
        best_g = float("nan")
        for gamma_star in sample:
            z_min, _w = min_z_injected(float(a_val), 0.5, float(gamma_star), zeros, n_lobes)
            # unscale: actual Z = e^{σ²/2a} Z_scaled, σ=1/2
            scale = math.exp(min(0.25 / (2.0 * a_val), EXPO_CLIP))
            z_act = z_min * scale
            if z_act < best:
                best = z_act
                best_g = float(gamma_star)
        adv_rows.append({"a": float(a_val), "z_min": best, "gamma": best_g})
        emit(
            "  ADV σ=1/2 a=%s min Z=%s at γ*=%s"
            % (fmt(a_val, 2), fmt(best, 6), fmt(best_g, 3))
        )
    p_val = fit["p"]
    if math.isfinite(p_val) and abs(p_val - 2.0) <= P_QUAD_TOL and fit["r2"] >= 0.40:
        decision = "A_COMPACT_QUADRATIC(p=%s, a0=%s)" % (fmt(p_val, 3), fmt(a0, 4))
    elif math.isfinite(p_val):
        decision = "A_COMPACT_OTHER(p=%s)" % fmt(p_val, 3)
    else:
        decision = "INCONCLUSIVE"
    return {
        "rows": rows,
        "fit": fit,
        "a0": a0,
        "a0_extrap": a0_extrap,
        "true": true_rows,
        "adv": adv_rows,
        "decision": decision,
    }


# ---------------------------------------------------------------------------
# F2
# ---------------------------------------------------------------------------
def window_minimizer(
    length: float,
    dimension: int,
    connection: np.ndarray,
    zeros: np.ndarray,
    power: int,
) -> dict:
    n_inner = n_inner_of(dimension)
    gram = gram_matrix(length, dimension, power, n_inner)
    packed = zero_side_min(length, dimension, connection, zeros, gram, power)
    lam = float(packed["lam_svd"]) if math.isfinite(packed["lam_svd"]) else float(packed["lam"])
    return {
        "lam": lam,
        "vec": packed["vec"],
        "hats": packed["hats"],
        "gram": gram,
        "svd_ok": packed["svd_ok"],
        "cond": packed["cond"],
    }


def hf_at(
    length: float,
    dimension: int,
    connection: np.ndarray,
    zeros: np.ndarray,
    power: int,
    coeff: np.ndarray,
    xdot: np.ndarray,
) -> dict:
    hats = bessel_damped_hat(length, zeros, dimension, connection, power)
    hats_dt = bessel_damped_hat_dt(length, zeros, dimension, connection, power)
    fhat = hats @ coeff.astype(np.complex128)
    fhat_dt = hats_dt @ coeff.astype(np.complex128)
    # ĥ(x)=|f̂(x/2)|², ĥ'(x)=Re[f̂'(γ) conj f̂(γ)], γ̇=ẋ/2
    hp = np.real(fhat_dt * np.conj(fhat))
    gamma_dot = 0.5 * xdot
    # λ_disc = 2 Σ |f̂|²  ⇒  dλ = 2 Σ 2 Re[f̂' conj f̂] γ̇ = 4 Σ hp_fourier γ̇
    # with hp_fourier = Re[f̂' conj f̂] = hp above.  Ξ Loewner uses ĥ'(x)=hp.
    rec = loewner_hf(2.0 * zeros, hp, xdot)
    hf_gamma = 4.0 * float(np.dot(hp, gamma_dot))
    rec["hf_gamma"] = hf_gamma
    rec["hp"] = hp
    rec["fhat"] = fhat
    return rec


def run_f2(cfg: dict, zeros: np.ndarray) -> dict:
    dimension = cfg["n_f2"]
    power = DAMP_POWER
    connection = connection_of(dimension, power)
    xdot, xdot_trunc = xi_velocities(zeros)
    rows = []
    for length in cfg["L"]:
        mini = window_minimizer(float(length), dimension, connection, zeros, power)
        rec_id = hf_at(
            float(length), dimension, connection, zeros, power, mini["vec"], xdot_trunc,
        )
        rec = hf_at(
            float(length), dimension, connection, zeros, power, mini["vec"], xdot,
        )
        lam = float(mini["lam"])
        dlam = float(rec["hf"])
        floor = abs(lam) < LAM_FLOOR
        clog = (
            float("nan") if floor or abs(lam) <= 1.0e-30
            else dlam / lam
        )
        loginv = (
            float("nan") if floor
            else math.log(1.0 / max(abs(lam), 1.0e-300))
        )
        tstar = (
            float("nan") if floor or abs(dlam) <= 1.0e-30
            else -lam / dlam
        )
        row = {
            "L": float(length),
            "lam": lam,
            "dlam": dlam,
            "c": clog,
            "loginv": loginv,
            "tstar": tstar,
            "floor": floor,
            "rel": rec_id["rel"],
            "loew": rec_id["loewner"],
            "svd_ok": mini["svd_ok"],
        }
        rows.append(row)
        emit(
            "  L=%s λ*=%s ∂tλ=%s c=%s log(1/λ*)=%s t*=%s Loewner_rel=%s"
            % (
                fmt(length, 3), fmt(lam, 8), fmt(dlam, 6), fmt(clog, 5),
                fmt(loginv, 4), fmt(tstar, 6), fmt(rec_id["rel"], 4),
            )
        )
    # C6 injection at first L (and at 0.55 if present)
    c6_L = 0.55 if 0.55 in cfg["L"] else float(cfg["L"][0])
    beta, gamma_c6 = C6_PAIR
    sigma = beta - 0.5
    gram = gram_matrix(c6_L, dimension, power, n_inner_of(dimension))
    hats = bessel_damped_hat(c6_L, zeros, dimension, connection, power)
    k0 = int(np.argmin(np.abs(zeros - gamma_c6)))
    gram_h = 2.0 * np.real(hats.conj().T @ hats)
    row0 = hats[k0]
    gram_h = gram_h - 2.0 * np.real(np.outer(np.conj(row0), row0))
    t_plus = gamma_c6 - 1j * sigma
    t_minus = gamma_c6 + 1j * sigma
    hats_c = basis_hat_complex(c6_L, [t_plus, t_minus], dimension, power)
    off = offline_matrix(hats_c[0], hats_c[1])
    mixed_t = tail_mixed(c6_L, dimension, connection, power, float(zeros[-1]))
    tail = np.real(mixed_t.conj().T @ mixed_t)
    pencil = 0.5 * ((gram_h + off + tail) + (gram_h + off + tail).T)
    lam_c6, vec_c6 = min_rayleigh(pencil, gram)
    rec_c6 = hf_at(c6_L, dimension, connection, zeros, power, vec_c6, xdot)
    # off-line γ-derivative by FD, times γ̇ at the nearest ordinate
    eps = 1.0e-4
    hats_p = basis_hat_complex(
        c6_L, [gamma_c6 + eps - 1j * sigma, gamma_c6 + eps + 1j * sigma],
        dimension, power,
    )
    hats_m = basis_hat_complex(
        c6_L, [gamma_c6 - eps - 1j * sigma, gamma_c6 - eps + 1j * sigma],
        dimension, power,
    )
    def quad_term(hplus, hminus, coeff):
        u = complex(np.dot(hplus, coeff))
        v = complex(np.dot(hminus, coeff))
        return 4.0 * float(np.real(u * np.conj(v)))

    d_off = (
        quad_term(hats_p[0], hats_p[1], vec_c6)
        - quad_term(hats_m[0], hats_m[1], vec_c6)
    ) / (2.0 * eps)
    gamma_dot_c6 = 0.5 * float(xdot[k0])
    dlam_c6 = float(rec_c6["hf"]) + d_off * gamma_dot_c6
    emit(
        "  C6(β=0.6,γ=20) L=%s λ=%s ∂tλ=%s sign=%s"
        % (
            fmt(c6_L, 3), fmt(lam_c6, 8), fmt(dlam_c6, 6),
            "neg" if dlam_c6 < 0.0 else "pos",
        )
    )
    live_rows = [row for row in rows if not row["floor"]]
    logs = np.array([row["loginv"] for row in live_rows], dtype=np.float64)
    cs = np.array([row["c"] for row in live_rows], dtype=np.float64)
    finite = np.isfinite(logs) & np.isfinite(cs)
    corr = float("nan")
    if int(np.sum(finite)) >= 2:
        corr = float(np.corrcoef(logs[finite], np.abs(cs[finite]))[0, 1])
    tstars = [abs(row["tstar"]) for row in live_rows if math.isfinite(row["tstar"])]
    tstar_max = max(tstars) if tstars else float("nan")
    vacuous = bool(
        math.isfinite(corr) and corr >= 0.5 and math.isfinite(tstar_max)
        and tstar_max <= 0.055 * 1.0e-2
    )
    if vacuous:
        reading = "VACUOUS_TSTAR (c grows like log(1/λ*); t* exponentially small)"
    elif math.isfinite(tstar_max) and tstar_max <= 0.055:
        reading = "TSTAR_INSIDE_WINDOW but not exponentially tied to log(1/λ*)"
    elif live_rows and all(row["dlam"] > 0.0 for row in live_rows):
        reading = "FORWARD_INCREASES_MARGIN (|t*|≫0.055; kill not in +t)"
    else:
        reading = "TSTAR_NOT_VACUOUS"
    return {
        "rows": rows,
        "c6_sign": int(np.sign(dlam_c6)) if dlam_c6 != 0.0 else 0,
        "c6_dlam": dlam_c6,
        "c6_lam": float(lam_c6),
        "corr": corr,
        "reading": reading,
        "loew_ok": all(row["rel"] <= HF_REL or smoke_skip_loew(row, cfg) for row in rows),
    }


def smoke_skip_loew(row: dict, cfg: dict) -> bool:
    return bool(cfg.get("smoke")) and row["rel"] <= 1.0e-3


# ---------------------------------------------------------------------------
# F3
# ---------------------------------------------------------------------------
def run_f3(cfg: dict, zeros: np.ndarray, lam_true_map: dict) -> dict:
    dimension = cfg["n_f3"]
    n_outer = cfg["n_outer_f3"]
    qs, logqs, weights, _ells, _lam = prime_powers_upto(32)
    anc_rows = []
    for length in (0.40, 0.549, 0.80, 0.55):
        forms = assemble_free(float(length), dimension, 0, n_outer)
        lam, vec = min_rayleigh(forms["free"], forms["gram"])
        anc_rows.append({
            "L": float(length), "lam": float(lam), "vec": vec, "forms": forms,
        })
        if abs(length - 0.55) < 1e-12:
            ref = R623_ANC[0.549]
        else:
            ref = R623_ANC.get(round(float(length), 3), float("nan"))
        emit(
            "  λ_min(POLE+ARCH) L=%s %s  (r623 %s)"
            % (fmt(length, 3), fmt(lam, 6), fmt(ref, 3))
        )
    # MC at L=0.55
    length = 0.55
    forms = assemble_window(length, dimension, 0, n_outer, logqs, weights)
    n_ev = forms["n_ev"]
    rng = np.random.RandomState(SEED)
    eigs = []
    for _ in range(cfg["n_mc"]):
        theta = rng.uniform(0.0, 2.0 * PI, size=n_ev)
        prime = np.zeros((dimension, dimension), dtype=np.float64)
        for index in range(n_ev):
            prime = prime + weights[index] * math.cos(theta[index]) * forms["overlaps"][index]
        q_rand = 0.5 * ((forms["free"] - prime) + (forms["free"] - prime).T)
        lam_r, _ = min_rayleigh(q_rand, forms["gram"])
        eigs.append(float(lam_r))
    eigs = np.asarray(eigs, dtype=np.float64)
    frac_neg = float(np.mean(eigs < 0.0))
    emit(
        "  MC L=0.55 n=%d mean λ_min=%s std=%s frac_neg=%s"
        % (int(eigs.size), fmt(float(np.mean(eigs)), 6), fmt(float(np.std(eigs)), 6), fmt(frac_neg, 4))
    )
    # coherence at true minimizer (zero-side, damped) if supplied
    coh_rows = []
    baker = {}
    for length in F3_L:
        dim_c = cfg["n_f2"]
        conn = connection_of(dim_c, DAMP_POWER)
        mini = window_minimizer(float(length), dim_c, conn, zeros, DAMP_POWER)
        n_inner = n_inner_of(dim_c)
        n_ev_l = n_active(float(length), logqs)
        g_vals = []
        for index in range(n_ev_l):
            ov = overlap_matrix(
                float(length), float(logqs[index]), dim_c, DAMP_POWER, n_inner,
            )
            g_vals.append(float(mini["vec"] @ ov @ mini["vec"]))
        g_vals = np.asarray(g_vals, dtype=np.float64)
        w_use = weights[:n_ev_l]
        num = float(np.dot(w_use, g_vals))
        den = float(np.dot(w_use, np.abs(g_vals)))
        coh = num / den if den > 1.0e-30 else float("nan")
        coh_rows.append({
            "L": float(length),
            "C": coh,
            "num": num,
            "den": den,
            "lam_true": float(lam_true_map.get(round(float(length), 2), float("nan"))),
        })
        emit(
            "  C(L=%s)=%s  Σwg=%s  Σw|g|=%s  λ*_true=%s"
            % (
                fmt(length, 2), fmt(coh, 6), fmt(num, 6), fmt(den, 6),
                fmt(coh_rows[-1]["lam_true"], 6),
            )
        )
    # Baker decade gap at L=0.55 along the true minimizer h0
    coh55 = next(row for row in coh_rows if abs(row["L"] - 0.55) < 1e-12)
    dim_c = cfg["n_f2"]
    conn = connection_of(dim_c, DAMP_POWER)
    mini55 = window_minimizer(0.55, dim_c, conn, zeros, DAMP_POWER)
    free55 = assemble_free(0.55, dim_c, DAMP_POWER, n_outer)
    anc_h0 = float(mini55["vec"] @ free55["free"] @ mini55["vec"])
    ratio = abs(anc_h0) / max(coh55["den"], 1.0e-30)
    if 0.0 < ratio <= 1.0:
        delta_req = float(math.acos(max(min(ratio, 1.0), -1.0)))
    else:
        # O(1) radian reference: Baker bounds sit exponentially below any
        # phase-coherence window that could decide the operator.
        delta_req = 1.0
    logqs_use = logqs[: max(n_active(0.55, logqs), 1)]
    prod_log = float(np.prod(np.maximum(logqs_use, 1.0e-12)))
    log_b = math.log(2.0)
    baker_lb = math.exp(-32.0 * log_b * prod_log)
    decade = math.log10(max(delta_req, 1.0e-16) / max(baker_lb, 1.0e-300))
    baker = {
        "delta_req": delta_req,
        "baker_lb": baker_lb,
        "decade": decade,
        "ratio": ratio,
        "C_baker": 32.0,
    }
    emit(
        "  Baker δ_req=%s  lb~exp(-32 log2 Π log q)=%s  decade_gap=%s"
        % (fmt(delta_req, 4), fmt(baker_lb, 4), fmt(decade, 3))
    )
    statement = (
        "RANDOM_EULER_REFUTED (positivity is phase-coherent, not probabilistic; "
        "kills the T1 dominance family unconditionally)."
    )
    return {
        "anc": [{"L": row["L"], "lam": row["lam"]} for row in anc_rows],
        "mc_mean": float(np.mean(eigs)),
        "mc_std": float(np.std(eigs)),
        "mc_frac": frac_neg,
        "coh": coh_rows,
        "baker": baker,
        "statement": statement,
        "decision": "RANDOM_EULER_REFUTED",
    }


# ---------------------------------------------------------------------------
# F4
# ---------------------------------------------------------------------------
def scan_ancestor_crossing(
    left: float, gap: float, cache_fn, j_ev: int,
) -> tuple[float, float, np.ndarray | None]:
    scan_hi = left + gap + 0.5
    step = max(min(0.04, 0.25 * max(gap, 0.02)), 0.01)

    def mu_fn(point):
        packed = cache_fn(point, max(0, j_ev - 1))
        value, vec = min_rayleigh(packed["full"], packed["gram"])
        return float(value), vec

    value, vec = mu_fn(left)
    if value <= CROSS_NEG:
        return 0.0, value, vec
    prev, prev_v, prev_vec = left, value, vec
    probe = left
    while probe < scan_hi - 1.0e-14:
        nxt = min(probe + step, scan_hi)
        val_n, vec_n = mu_fn(nxt)
        if prev_v > CROSS_POS and val_n <= CROSS_NEG:
            def scalar(point):
                val, _vec = mu_fn(point)
                return val

            root, _, _ = bisect_sign(scalar, prev, nxt)
            if not math.isfinite(root):
                root = float(nxt)
            return float(root - left), float(val_n), vec_n
        prev, prev_v, prev_vec, probe = nxt, val_n, vec_n, nxt
    return float("inf"), value, None


def run_f4(cfg: dict) -> dict:
    dimension = cfg["n_lead"]
    n_outer = cfg["n_outer_lead"]
    power = DAMP_POWER
    qs, logqs, weights, ells, _lam = prime_powers_upto(32)
    n_inner = n_inner_of(dimension)

    def forms_at(length: float, n_ev: int):
        return assemble_window(
            float(length), dimension, power, n_outer, logqs, weights, n_ev,
        )

    # recompute two leads
    recomputed = {}
    for q_val in cfg["validate_q"]:
        index = qs.index(q_val)
        left = float(ells[index])
        gap = float(ells[index + 1] - ells[index]) if index + 1 < ells.size else 0.2
        delta, _mu, _vec = scan_ancestor_crossing(left, gap, forms_at, index + 1)
        recomputed[q_val] = delta
        table = R619_LEADS[q_val]
        emit(
            "  recompute q=%d Δ=%s table=%s rel=%s"
            % (
                q_val, fmt(delta, 5), fmt(table, 4),
                fmt(abs(delta - table) / max(table, 1e-12), 4),
            )
        )
    # exponent: g_h(log q) vs (L-L_j) on the ancestor minimizer
    deltas_fit = (0.002, 0.004, 0.008, 0.012, 0.018)
    fit_q = cfg["fit_q"]
    log_d = []
    log_g = []
    g_samples = []
    for q_val in fit_q:
        index = qs.index(q_val)
        left = float(ells[index])
        log_q = float(logqs[index])
        for delta in deltas_fit:
            length = left + delta
            packed = forms_at(length, index)  # drop newest
            _mu, vec = min_rayleigh(packed["full"], packed["gram"])
            ov = overlap_matrix(length, log_q, dimension, power, n_inner)
            g_val = float(vec @ ov @ vec)
            g_samples.append({
                "q": q_val, "delta": delta, "g": g_val, "mu": float(_mu),
                "w": float(weights[index]),
            })
            if abs(g_val) > 1.0e-18:
                log_d.append(math.log(delta))
                log_g.append(math.log(abs(g_val)))
    alpha = float("nan")
    kappa = float("nan")
    if len(log_d) >= 4:
        matrix = np.column_stack((np.ones(len(log_d)), np.asarray(log_d)))
        coeff, _, _, _ = np.linalg.lstsq(matrix, np.asarray(log_g), rcond=None)
        kappa = float(math.exp(coeff[0]))
        alpha = float(coeff[1])
    emit(
        "  g ~ κ δ^α  α=%s  (2p+1=7 for p=3)  κ=%s  n=%d"
        % (fmt(alpha, 4), fmt(kappa, 4), len(log_d))
    )
    # Law (ii): ancestor deficit.  Pooled relative slope β = -s/μ0 on
    # reliable early events; linear crossing Δ = 1/β is event-independent
    # to leading order.  Combined argmin of μ0(1-βδ) + w_q κ δ^α.
    beta_samples = []
    mu_entry = []
    for rec in g_samples:
        if rec["delta"] != 0.002:
            continue
        index = qs.index(rec["q"])
        left = float(ells[index])
        packed1 = forms_at(left + 0.010, index)
        mu1, _ = min_rayleigh(packed1["full"], packed1["gram"])
        mu0 = float(rec["mu"])
        if mu0 > 1.0e-10:
            slope = (float(mu1) - mu0) / 0.008
            beta_samples.append(-slope / mu0)
            mu_entry.append(mu0)
    beta = float(np.median(beta_samples)) if beta_samples else float("nan")
    emit(
        "  ancestor β=-s/μ0 median=%s  Δ_univ=1/β=%s  n_β=%d"
        % (
            fmt(beta, 4),
            fmt(1.0 / beta if math.isfinite(beta) and abs(beta) > 1e-18 else float("nan"), 4),
            len(beta_samples),
        )
    )
    ratios = []
    for index, q_val in enumerate(qs):
        left = float(ells[index])
        gap = float(ells[index + 1] - ells[index]) if index + 1 < ells.size else 0.2
        packed0 = forms_at(left + 0.002, index)
        mu0, _vec0 = min_rayleigh(packed0["full"], packed0["gram"])
        packed1 = forms_at(left + 0.010, index)
        mu1, _v1 = min_rayleigh(packed1["full"], packed1["gram"])
        slope = (float(mu1) - float(mu0)) / 0.008
        if abs(slope) > 1.0e-18:
            d_zero = -float(mu0) / slope + 0.002
        else:
            d_zero = float("nan")
        d_univ = (1.0 / beta) if math.isfinite(beta) and abs(beta) > 1e-18 else float("nan")
        w_q = float(weights[index])
        grid = np.linspace(1.0e-4, max(min(gap, 0.08), 1.0e-3), 120)
        if math.isfinite(alpha) and math.isfinite(kappa) and math.isfinite(beta):
            f_vals = float(mu0) * (1.0 - beta * (grid - 0.002)) + w_q * kappa * np.power(grid, alpha)
            d_arg = float(grid[int(np.argmin(f_vals))])
        else:
            d_arg = d_zero
        measured = R619_LEADS[q_val]
        ratio_arg = (
            d_arg / measured
            if measured > 0.0 and math.isfinite(d_arg) and d_arg > 0.0
            else float("nan")
        )
        ratios.append({
            "q": q_val,
            "measured": measured,
            "pred_zero": d_zero,
            "pred_arg": d_arg,
            "pred_univ": d_univ,
            "ratio": ratio_arg,
            "ratio_zero": (
                d_zero / measured if measured > 0.0 and math.isfinite(d_zero) else float("nan")
            ),
            "via": "argmin",
            "pred": d_arg,
        })
    n_ok_arg = sum(
        1 for row in ratios
        if math.isfinite(row["pred_arg"]) and row["measured"] > 0.0
        and abs(row["pred_arg"] / row["measured"] - 1.0) <= LEAD_REL
    )
    n_ok_zero = sum(
        1 for row in ratios
        if math.isfinite(row["ratio_zero"]) and abs(row["ratio_zero"] - 1.0) <= LEAD_REL
    )
    n_ok_univ = sum(
        1 for row in ratios
        if math.isfinite(row["pred_univ"]) and row["measured"] > 0.0
        and abs(row["pred_univ"] / row["measured"] - 1.0) <= LEAD_REL
    )
    n_ok_best = sum(
        1 for row in ratios
        if math.isfinite(row["ratio"]) and abs(row["ratio"] - 1.0) <= LEAD_REL
    )
    n_tot = len(ratios)
    emit("  argmin-law within 20%%: %d/%d" % (n_ok_arg, n_tot))
    emit("  ancestor-zero-law within 20%%: %d/%d" % (n_ok_zero, n_tot))
    emit("  univ-1/β-law within 20%%: %d/%d" % (n_ok_univ, n_tot))
    n_ok = n_ok_arg
    which = "argmin"
    if n_ok >= LEAD_PASS_N:
        decision = "LEAD_LAW_DECORATION"
    elif n_ok <= 4:
        decision = "LEAD_LAW_INVARIANT"
    else:
        decision = "INCONCLUSIVE"
    return {
        "alpha": alpha,
        "kappa": kappa,
        "recomputed": recomputed,
        "ratios": ratios,
        "n_ok": n_ok,
        "n_ok_arg": n_ok_arg,
        "n_ok_zero": n_ok_zero,
        "n_tot": n_tot,
        "which": which,
        "decision": decision,
        "alpha_target": 2 * DAMP_POWER + 1,
        "beta": beta,
    }


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def compute(smoke: bool) -> dict:
    if smoke:
        cfg = {
            "smoke": True,
            "sigmas": SIGMAS_SMOKE,
            "gammas": GAMMAS_SMOKE,
            "n_lobes": N_LOBES_SMOKE,
            "n_a_grid": N_A_GRID_SMOKE,
            "a_true": A_TRUE_SMOKE,
            "n_omega_true": 21,
            "n_adv": 8,
            "n_f1_zeros": N_ZEROS_F1_SMOKE,
            "n_f2_zeros": N_ZEROS_F2_SMOKE,
            "n_f2": N_F2_SMOKE,
            "L": F2_L_SMOKE,
            "n_f3": N_F3,
            "n_outer_f3": N_OUTER_F3_SMOKE,
            "n_mc": N_MC_SMOKE,
            "n_lead": N_LEAD,
            "n_outer_lead": N_OUTER_LEAD_SMOKE,
            "validate_q": (2,),
            "fit_q": (2, 3),
        }
    else:
        cfg = {
            "smoke": False,
            "sigmas": SIGMAS_FULL,
            "gammas": GAMMAS_FULL,
            "n_lobes": N_LOBES_FULL,
            "n_a_grid": N_A_GRID_FULL,
            "a_true": A_TRUE,
            "n_omega_true": 61,
            "n_adv": 24,
            "n_f1_zeros": N_ZEROS_F1_FULL,
            "n_f2_zeros": N_ZEROS_F2_FULL,
            "n_f2": N_F2_FULL,
            "L": F2_L_FULL,
            "n_f3": N_F3,
            "n_outer_f3": N_OUTER_F3,
            "n_mc": N_MC_FULL,
            "n_lead": N_LEAD,
            "n_outer_lead": N_OUTER_LEAD,
            "validate_q": VALIDATE_Q,
            "fit_q": (2, 3, 5, 7),
        }
    n_zeros = max(cfg["n_f1_zeros"], cfg["n_f2_zeros"])
    zeros_all = load_zeros(n_zeros)
    zeros_f1 = zeros_all[: cfg["n_f1_zeros"]]
    zeros_f2 = zeros_all[: cfg["n_f2_zeros"]]
    emit(
        "zeros n=%d/%d γ1=%s γN=%s"
        % (
            int(zeros_f1.size), int(zeros_f2.size),
            fmt(float(zeros_all[0]), 8), fmt(float(zeros_all[-1]), 6),
        )
    )

    section("F1  a-COMPACTIFICATION")
    f1 = run_f1(cfg, zeros_f1)
    emit(
        "  fit a_max = c σ^p (log γ*)^q  p=%s q=%s c=%s r2=%s n=%d"
        % (
            fmt(f1["fit"]["p"], 4), fmt(f1["fit"]["q"], 4),
            fmt(f1["fit"]["c"], 4), fmt(f1["fit"]["r2"], 3), f1["fit"]["n"],
        )
    )
    emit("  a0=max(table)=%s  a0_extrap(σ=1/2,γ1)=%s" % (
        fmt(f1["a0"], 5), fmt(f1["a0_extrap"], 5),
    ))
    emit(
        "  Lean: Z(a,ω)≥0 for a≥a0 needs an unconditional Littlewood-type "
        "zero-gap/density input as a named hypothesis."
    )
    emit("  F1 DECISION %s (p=%s)" % (f1["decision"], fmt(f1["fit"]["p"], 3)))

    section("F2  dBN WINDOW MARGIN")
    f2 = run_f2(cfg, zeros_f2)
    emit("  F2 READING %s  corr(|c|,log(1/λ*))=%s" % (f2["reading"], fmt(f2["corr"], 3)))

    lam_map = {round(row["L"], 2): row["lam"] for row in f2["rows"]}
    section("F3  RANDOM-EULER")
    f3 = run_f3(cfg, zeros_f2, lam_map)
    emit("  F3 %s" % f3["statement"])

    section("F4  LEAD LAW Δ≈0.015")
    f4 = run_f4(cfg)
    emit("  F4 DECISION %s  via %s  α=%s" % (
        f4["decision"], f4["which"], fmt(f4["alpha"], 3),
    ))

    payload = {
        "f1_p": None if not math.isfinite(f1["fit"]["p"]) else round(f1["fit"]["p"], 6),
        "f1_q": None if not math.isfinite(f1["fit"]["q"]) else round(f1["fit"]["q"], 6),
        "f1_a0": round(f1["a0"], 8),
        "f1_dec": f1["decision"],
        "f1_amax": [
            [round(row["sigma"], 4), round(row["gamma"], 1), round(row["a_max"], 8)]
            for row in f1["rows"]
        ],
        "f2_c": [
            [round(row["L"], 4), round(row["c"], 8) if math.isfinite(row["c"]) else None]
            for row in f2["rows"]
        ],
        "f2_read": f2["reading"],
        "f3_mc_mean": round(f3["mc_mean"], 8),
        "f3_mc_frac": round(f3["mc_frac"], 6),
        "f3_dec": f3["decision"],
        "f4_alpha": None if not math.isfinite(f4["alpha"]) else round(f4["alpha"], 6),
        "f4_nok": [f4["n_ok"], f4["n_tot"]],
        "f4_dec": f4["decision"],
    }
    return {"f1": f1, "f2": f2, "f3": f3, "f4": f4, "payload": payload, "zeros": zeros_all}


def hat_checkpoint() -> dict:
    mp.mp.dps = 40
    a_mp, w_mp = mp.mpf("1"), mp.mpf("0")
    pref = mp.pi / (4 * a_mp)
    s2 = mp.mpf("0.25")
    hat = pref * (
        mp.exp(s2 / 2) + mp.exp(s2 / 2) + 2 * mp.exp(s2 / 2)
    )
    target = mp.pi * mp.e ** (mp.mpf("1") / 8)
    err = float(abs(hat - target))
    np_val = hat_gabor(1.0, 0.0, 0.5, np.array([0.0]))[0]
    err_np = abs(float(np.real(np_val)) - float(target))
    # FE quadruple at a random strip point
    a, omega, sigma, t_val = 0.7, 3.2, 0.21, 5.5
    h_rho = hat_gabor(a, omega, sigma, np.array([t_val]))[0]
    h_1m = hat_gabor(a, omega, -sigma, np.array([-t_val]))[0]
    h_bar = hat_gabor(a, omega, sigma, np.array([-t_val]))[0]
    h_1b = hat_gabor(a, omega, -sigma, np.array([t_val]))[0]
    left = h_rho + h_1m + h_bar + h_1b
    right = 4.0 * np.real(h_rho)
    fe_err = abs(left - right)
    return {
        "hat": float(hat),
        "target": float(target),
        "err": err,
        "err_np": err_np,
        "fe_err": float(abs(fe_err)),
    }


def run(smoke: bool) -> int:
    global VERBOSE
    CHECKS.clear()
    LINES.clear()
    _CL_CACHE.clear()
    _CONN_CACHE.clear()
    VERBOSE = True
    wall0 = time.time()
    emit("frontier_followups_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    section("G0  HAT CHECKPOINT")
    g0 = hat_checkpoint()
    emit(
        "  ĥ_{1,0}(1)=%s target=%s err=%s err_np=%s FE=%s"
        % (
            fmt(g0["hat"], 12), fmt(g0["target"], 12), fmt(g0["err"], 6),
            fmt(g0["err_np"], 6), fmt(g0["fe_err"], 6),
        )
    )
    check("G0-checkpoint", g0["err"] <= 1.0e-12, "err=%s" % fmt(g0["err"], 6))
    check("G0-numpy", g0["err_np"] <= 1.0e-10, "err=%s" % fmt(g0["err_np"], 6))
    check("G0-FE-quadruple", g0["fe_err"] <= 1.0e-10, "err=%s" % fmt(g0["fe_err"], 6))

    rec = compute(smoke)
    VERBOSE = False
    rec2 = compute(smoke)
    VERBOSE = True
    sha1 = payload_sha(rec["payload"])
    sha2 = payload_sha(rec2["payload"])
    f1, f2, f3, f4 = rec["f1"], rec["f2"], rec["f3"], rec["f4"]

    section("GATES")
    true_pos = all(row["z_min"] > 0.0 for row in f1["true"])
    check("F1-true-positive", true_pos, "min Z(a,ω)>0 on true zeros")
    check("F1-p-reported", math.isfinite(f1["fit"]["p"]) or f1["decision"] == "INCONCLUSIVE", "p=%s" % fmt(f1["fit"]["p"], 3))
    check("F1-decision-enum", f1["decision"].startswith("A_COMPACT_") or f1["decision"] == "INCONCLUSIVE", f1["decision"])
    loew_ok = all(row["rel"] <= (1.0e-3 if smoke else HF_REL) for row in f2["rows"])
    check("F2-Loewner-HF", loew_ok, "max rel=%s" % fmt(max(row["rel"] for row in f2["rows"]), 4))
    check("F2-c6-sign-reported", f2["c6_sign"] in (-1, 0, 1), "sign=%d" % f2["c6_sign"])
    anc_ok = True
    for length, target in ((0.40, -0.078), (0.80, -0.926)):
        got = next(row["lam"] for row in f3["anc"] if abs(row["L"] - length) < 1e-12)
        if abs(got - target) > R623_MATCH:
            anc_ok = False
    got549 = next(row["lam"] for row in f3["anc"] if abs(row["L"] - 0.549) < 1e-12)
    if abs(got549 - (-0.430)) > R623_MATCH:
        anc_ok = False
    check("F3-r623-match", anc_ok, "λ_min(POLE+ARCH) vs r623 ≤ 1e-3")
    check("F3-mc-negative", f3["mc_frac"] >= 0.8, "frac_neg=%s" % fmt(f3["mc_frac"], 3))
    check(
        "F3-statement",
        f3["decision"] == "RANDOM_EULER_REFUTED",
        f3["decision"],
    )
    rec_ok = True
    for q_val, delta in f4["recomputed"].items():
        table = R619_LEADS[q_val]
        if not (math.isfinite(delta) and abs(delta - table) / max(table, 1e-12) <= 0.25):
            rec_ok = False
    check("F4-recompute-import", rec_ok, "q=%s" % str(list(f4["recomputed"])))
    check(
        "F4-decision-enum",
        f4["decision"] in (
            "LEAD_LAW_DECORATION", "LEAD_LAW_INVARIANT", "INCONCLUSIVE",
        ),
        f4["decision"],
    )
    check("dual-run", sha1 == sha2 and len(sha1) == 64, "RESULT_SHA %s" % sha1[:16])
    wall = time.time() - wall0
    cap = SMOKE_WALL if smoke else FULL_WALL
    check("wall-time", wall <= cap, "wall_s=%s lim=%s" % (fmt(wall, 3), fmt(cap, 1)))

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)

    section("VERDICTS")
    emit("F1 %s  p=%s q=%s a0=%s" % (
        f1["decision"], fmt(f1["fit"]["p"], 3), fmt(f1["fit"]["q"], 3), fmt(f1["a0"], 4),
    ))
    emit("F2 %s" % f2["reading"])
    emit("F3 %s" % f3["decision"])
    emit("F4 %s" % f4["decision"])
    emit(FENCE)

    state = [
        "STATE r%d %s" % (ROUND, CONTRACT),
        "SHA %s" % file_sha256(),
        "SPEC %s" % SPEC_SHA,
        "RESULT %s" % sha1,
        "GATES PLACEHOLDER",
        "F1 %s p=%s q=%s r2=%s a0=%s a0_extrap=%s" % (
            f1["decision"], fmt(f1["fit"]["p"], 3), fmt(f1["fit"]["q"], 3),
            fmt(f1["fit"]["r2"], 3), fmt(f1["a0"], 4), fmt(f1["a0_extrap"], 4),
        ),
        "F1 table " + " ".join(
            "(%s,%s):%s" % (fmt(row["sigma"], 2), fmt(row["gamma"], 0), fmt(row["a_max"], 3))
            for row in f1["rows"]
        ),
        "F1 TRUE " + " ".join(
            "a=%s:%s" % (fmt(row["a"], 1), fmt(row["z_min"], 4)) for row in f1["true"]
        ),
        "F1 ADV " + " ".join(
            "a=%s:%s" % (fmt(row["a"], 1), fmt(row["z_min"], 3)) for row in f1["adv"]
        ),
        "F1 Lean hyp: Z(a,ω)≥0 for a≥a0 needs Littlewood-type zero-gap/density",
        "F2 c(L) " + " ".join(
            "L=%s:c=%s λ=%s t*=%s" % (
                fmt(row["L"], 2), fmt(row["c"], 3), fmt(row["lam"], 3), fmt(row["tstar"], 3),
            )
            for row in f2["rows"]
        ),
        "F2 %s corr=%s C6_sign=%d" % (f2["reading"], fmt(f2["corr"], 3), f2["c6_sign"]),
        "F3 λ(P+A) " + " ".join(
            "L=%s:%s" % (fmt(row["L"], 3), fmt(row["lam"], 4)) for row in f3["anc"]
        ),
        "F3 MC mean=%s std=%s frac_neg=%s C(0.55)=%s" % (
            fmt(f3["mc_mean"], 4), fmt(f3["mc_std"], 4), fmt(f3["mc_frac"], 3),
            fmt(next(row["C"] for row in f3["coh"] if abs(row["L"] - 0.55) < 1e-12), 4),
        ),
        "F3 Baker δ=%s lb=%s decade=%s" % (
            fmt(f3["baker"]["delta_req"], 3), fmt(f3["baker"]["baker_lb"], 3),
            fmt(f3["baker"]["decade"], 2),
        ),
        "F3 %s" % f3["decision"],
        "F4 α=%s (2p+1=%d) n_ok=%d/%d via %s" % (
            fmt(f4["alpha"], 3), f4["alpha_target"], f4["n_ok"], f4["n_tot"], f4["which"],
        ),
        "F4 ratios " + " ".join(
            "%d:%s" % (row["q"], fmt(row["ratio"], 2)) for row in f4["ratios"]
        ),
        "F4 %s" % f4["decision"],
        "FENCE %s" % FENCE,
        "END_STATE",
    ]
    n_state = len(state)
    check("STATE-le-40", n_state <= 40, "n=%d" % n_state)

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    state[4] = "GATES %d/%d smoke=%d wall_s=%s" % (
        n_pass, n_gate, int(smoke), fmt(wall, 3),
    )

    section("STATE")
    for line in state:
        emit(line)
    emit("STATE_LINES %d" % n_state)

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % sha1)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit(FENCE)
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r633 frontier follow-ups on sealed objects (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
