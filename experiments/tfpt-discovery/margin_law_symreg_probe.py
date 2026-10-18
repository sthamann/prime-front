#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""margin_law_symreg_probe -- r630b  PRIME.MARGIN.LAW.SYMREG.01

Experiments-only symbolic-regression scout of the Weil-window margin.
r630b addendum: tall QR/SVD (never F^H F) + N-sweep in {40,60,80,120,160},
mpmath dps=40 refinement of the N×N R-factor, synthetic zero-set controls,
nulling counts, and the dBN gap functional.
Copied (not imported) machinery:

  * r619 zero-side SVD: edge-damped (1-(u/L)^2)^3 P_n, F stacked from
    ĥ_i(γ_k) on the first 5000 ordinates (×√2 for ±γ) plus a density
    tail with ρ(t)=(1/2π)log(t/2π).  λ*(L) = σ_min(F G^{-1/2})^2.
  * r615 source-side window form Q = POLE + ARCH − PRIME, v1017
    x-space kernel, pinning δ_crit by a relative w₂ perturbation.

r619 STATE leads Δ_j (q ≤ 32), recomputed here:

  2: 0.0279, 3: 0.0123, 4: 0.0146, 5: 0.0111, 7: 0.0105, 8: 0.0140,
  9: 0.0125, 11: 0.0116, 13: 0.0131, 16: 0.0166, 17: 0.0126,
  19: 0.0144, 23: 0.0141, 25: 0.0170, 27: 0.0181, 29: 0.0151,
  31: 0.0147, 32: 0.0221.

Claim boundary: finite-section arithmetic.  Not a ledger row.
Not a paper claim.  Fence: "Empirical laws of the window margin;
sampling-theoretic reading; no RH claim."
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
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
from scipy.linalg import qr as sqr  # noqa: E402
from scipy.linalg import svd as ssvd  # noqa: E402
from scipy.linalg import svdvals  # noqa: E402
from scipy.special import roots_legendre, spherical_jn  # noqa: E402

HERE = Path(__file__).resolve().parent
ZEROS_CACHE = HERE / "verified_zeros_n7000.npy"

ROUND = 630
SEED = 630202609
CONTRACT = "PRIME.MARGIN.LAW.SYMREG.01"
ADDENDUM = "r630b"
FENCE = (
    "Empirical laws of the window margin; sampling-theoretic reading; "
    "no RH claim."
)
GAMMA1 = 14.134725141734695
TWO_GAMMA1 = 2.0 * GAMMA1
LOG2 = math.log(2.0)
W2 = math.sqrt(2.0) * LOG2
DAMP_ZERO = 3
DAMP_SRC = 2
SVD_COND = 1.0e-8
LAM_FLOOR = 1.0e-16
G0_ALPHA = 20.0
CROSS_POS = 1.0e-8
CROSS_NEG = -1.0e-8
BISECT_ITERS = 28
EXT_PAD = 0.5
Q_MAX_FULL = 32
Q_MAX_SMOKE = 8
N_ZERO_FULL = 64
N_ZERO_SMOKE = 24
N_ZEROS_FULL = 5000
N_ZEROS_SMOKE = 400
N_SRC_FULL = 40
N_SRC_SMOKE = 16
N_LEAD_FULL = 40
N_LEAD_SMOKE = 20
N_PIN_FULL = 80
N_PIN_SMOKE = 24
N_OUTER_FULL = 64
N_OUTER_SMOKE = 32
L_LO = 0.25
L_HI = 1.40
L_STEP_FULL = 0.01
L_STEP_SMOKE = 0.10
MU_LO = 0.25
MU_HI = 0.60
MU_STEP_FULL = 0.01
MU_STEP_SMOKE = 0.05
PIN_L = (0.40, 0.46, 0.52)
R615_DCRIT = {0.40: 5.79e-2, 0.46: 1.08e-3, 0.52: 2.48e-5}
R619_LEADS = {
    2: 0.0279, 3: 0.0123, 4: 0.0146, 5: 0.0111, 7: 0.0105, 8: 0.0140,
    9: 0.0125, 11: 0.0116, 13: 0.0131, 16: 0.0166, 17: 0.0126,
    19: 0.0144, 23: 0.0141, 25: 0.0170, 27: 0.0181, 29: 0.0151,
    31: 0.0147, 32: 0.0221,
}
CLOSED = (
    ("gamma1", GAMMA1),
    ("2gamma1", TWO_GAMMA1),
    ("gamma1^2/pi", GAMMA1 * GAMMA1 / math.pi),
    ("pi", math.pi),
    ("log2", LOG2),
    ("e", math.e),
)
FIT_CUT = 1.0
REL_WIN = 5.0e-2
MATCH_TOL = 1.0e-2
SMOKE_WALL = 60.0
FULL_WALL = 900.0
LCROSS_REF = 0.372
N_SWEEP = (40, 60, 80, 120, 160)
N_SWEEP_SMOKE = (40, 80)
L_N1_LO = 0.30
L_N1_HI = 1.40
L_N1_STEP_FULL = 0.02
L_N1_STEP_SMOKE = 0.20
MP_DPS = 40
CONV_REL = 0.10
LAM_TRUST = 1.0e-32
NULL_FRAC = 1.0e-3
N4_WINDOW = 2000
N4_COMPRESS = 0.3
BANDS = ((0.30, 0.60), (0.60, 1.00), (1.00, 1.40))

SPEC = {
    "round": ROUND,
    "tag": "r630b",
    "addendum": ADDENDUM,
    "contract": CONTRACT,
    "parent_zero": "r619 support_relay_census_probe",
    "parent_src": "r615 semilocal_firststep_probe",
    "lambda_star": "sigma_min(F_white)^2, F stacked zeros+tail",
    "F": "F[k,i]=hat_i(gamma_k); plus/minus via sqrt(2); tail density",
    "n_zeros": N_ZEROS_FULL,
    "zeros_cache": "verified_zeros_n7000.npy (recompute if absent; no new npy)",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "space_zero": "(1-(u/L)^2)^3 * P_n",
    "damp_zero": DAMP_ZERO,
    "n_zero": N_ZERO_FULL,
    "L_grid": [L_LO, L_HI, L_STEP_FULL],
    "mu_grid": [MU_LO, MU_HI, MU_STEP_FULL],
    "mu_star": "min(POLE+ARCH) undamped Legendre, odd sector",
    "L_cross_ref": LCROSS_REF,
    "q_max": Q_MAX_FULL,
    "w_q": "2*Lambda(q)*q**(-1/2)",
    "pin_L": list(PIN_L),
    "r615_dcrit": [R615_DCRIT[ell] for ell in PIN_L],
    "pole": "2*Fplus*Fminus",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "fit_cut": FIT_CUT,
    "holdout": "L in (1.0, 1.4] reliable",
    "slepian": "log lambda ~ -2*gamma1*L + c",
    "widom_arc": "-A L^2 - B L log L + c",
    "landau_widom": "log(1-lambda0(c))~log(4*sqrt(pi*c))-2c, c=L*gamma1",
    "grammar_atoms": ["L", "L2", "LlogL", "logL", "1"],
    "grammar_depth": 3,
    "seed": SEED,
    "n1_N": list(N_SWEEP),
    "n1_L": [L_N1_LO, L_N1_HI, L_N1_STEP_FULL],
    "n1_spaces": ["damped3", "plain"],
    "n1_method": "tall_QR_then_mpmath_svd_of_R",
    "n1_mp_dps": MP_DPS,
    "n1_conv_rel": CONV_REL,
    "n1_laws": ["-2g1 L + 0.5 log L + c", "-C L^2 + b L + c", "-a L log L + b L + c", "grammar"],
    "n2_null_frac": NULL_FRAC,
    "n3_worlds": ["true", "flat_gap", "scale_W10", "scale_W20", "first_to_20"],
    "n4_window": N4_WINDOW,
    "n4_compress": N4_COMPRESS,
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


def payload_sha(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    ).hexdigest()


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
    bessel = np.stack(
        [spherical_jn(degree, argument) for degree in range(width)], axis=1,
    )
    phases = (1j) ** np.arange(width, dtype=np.int64)
    combo = (bessel * phases[None, :]) @ np.asarray(
        connection[:n_max, :width], dtype=np.float64,
    ).T
    scales = np.sqrt(2.0 * length * (2 * np.arange(n_max) + 1))
    return combo * scales[None, :]


def assemble_source(
    length: float, dimension: int, power: int, n_outer: int, include_prime: bool,
) -> dict:
    n_inner = n_inner_of(dimension)
    c_l = c_L_of(length)
    gram = gram_matrix(length, dimension, power, n_inner)
    arch = arch_matrix(length, dimension, power, gram, c_l, n_outer, n_inner)
    cosh_vector, sinh_vector = pole_vectors(length, dimension, power, n_inner)
    pole = pole_matrix(cosh_vector, sinh_vector)
    free = 0.5 * ((arch + pole) + (arch + pole).T)
    overlap = overlap_matrix(length, LOG2, dimension, power, n_inner)
    prime = (
        W2 * overlap
        if include_prime and LOG2 < 2.0 * length - 1.0e-15
        else np.zeros((dimension, dimension), dtype=np.float64)
    )
    full = 0.5 * ((free - prime) + (free - prime).T)
    return {
        "gram": 0.5 * (gram + gram.T),
        "arch": arch,
        "pole": pole,
        "free": free,
        "overlap": overlap,
        "prime": prime,
        "full": full,
        "c_L": c_l,
        "n_inner": n_inner,
        "power": power,
    }


def odd_min(quadratic, gram) -> float:
    dim = int(quadratic.shape[0])
    odd_idx = np.arange(1, dim, 2)
    if odd_idx.size < 1:
        return float("nan")
    quad = quadratic[np.ix_(odd_idx, odd_idx)]
    grm = gram[np.ix_(odd_idx, odd_idx)]
    value, _vec = min_rayleigh(quad, grm)
    return float(value)


def tail_mixed(
    length: float,
    dimension: int,
    connection: np.ndarray,
    power: int,
    t_cut: float,
    t_extra: float = 2000.0,
    n_quad: int = 48,
    dens_scale: float | None = None,
) -> np.ndarray:
    nodes, weights = roots_legendre(n_quad)
    t_values = t_cut + 0.5 * t_extra * (nodes + 1.0)
    scaled = 0.5 * t_extra * weights
    hats = bessel_damped_hat(length, t_values, dimension, connection, power)
    if dens_scale is not None and dens_scale > 0.0:
        dens = np.full(t_values.shape, float(dens_scale))
    else:
        dens = np.log(np.maximum(t_values / (2.0 * math.pi), 1.0e-12)) / (2.0 * math.pi)
    amp = np.sqrt(np.maximum(2.0 * scaled * dens, 0.0))
    return amp[:, None] * hats


def stacked_svd_min(stacked: np.ndarray, gram: np.ndarray) -> dict:
    """Real trial coefficients: stack Re F and Im F, then σ_min(F G^{-1/2})^2."""
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
    }


def tall_qr_min(stacked: np.ndarray, gram: np.ndarray, mp_refine: bool = False) -> dict:
    """λ* = σ_min(F G^{-1/2})^2 via tall QR, never F^H F.  Optional mpmath SVD of R."""
    dim = int(gram.shape[0])
    real_f = np.vstack(
        [np.real(np.asarray(stacked)), np.imag(np.asarray(stacked))]
    )
    ridge = 1.0e-18 * (float(np.trace(gram)) / max(dim, 1) + 1.0e-30)
    gram_r = 0.5 * (gram + gram.T) + ridge * np.eye(dim)
    try:
        chol = np.linalg.cholesky(gram_r)
    except np.linalg.LinAlgError:
        evals, evecs = np.linalg.eigh(gram_r)
        evals = np.maximum(evals, 1.0e-18)
        chol = evecs @ np.diag(np.sqrt(evals))
    q_mat, r_mat = sqr(real_f, mode="economic")
    r_w = np.linalg.solve(chol, r_mat.T).T
    try:
        u_mat, sigma, vt_mat = ssvd(r_w, full_matrices=False)
    except Exception:
        sigma = svdvals(r_w)
        u_mat, vt_mat = None, None
    smin = float(sigma[-1]) if sigma.size else float("nan")
    smax = float(sigma[0]) if sigma.size else float("nan")
    lam = smin * smin if math.isfinite(smin) else float("nan")
    vec = np.zeros(dim, dtype=np.float64)
    if vt_mat is not None:
        vec = np.linalg.solve(chol.T, vt_mat[-1].real)
        nrm = math.sqrt(max(float(vec @ gram_r @ vec), 1.0e-30))
        vec = vec / nrm
    mp_smin = float("nan")
    mp_lam = float("nan")
    if mp_refine and dim <= 80 and math.isfinite(smin):
        prev = mp.mp.dps
        mp.mp.dps = MP_DPS
        try:
            r_mp = mp.matrix([[float(r_w[i, j]) for j in range(dim)] for i in range(dim)])
            _u, s_mp, _v = mp.svd(r_mp)
            try:
                diag = [float(s_mp[index, index]) for index in range(dim)]
            except Exception:
                diag = [float(s_mp[index]) for index in range(dim)]
            mp_smin = min(abs(val) for val in diag) if diag else float("nan")
            mp_lam = mp_smin * mp_smin
        except Exception:
            pass
        finally:
            mp.mp.dps = prev
    cond = (
        smin / smax if (math.isfinite(smin) and math.isfinite(smax) and smax > 0.0)
        else float("nan")
    )
    return {
        "lam": float(lam),
        "lam_svd": float(lam),
        "lam_mp": float(mp_lam),
        "smin": smin,
        "smax": smax,
        "mp_smin": mp_smin,
        "cond": cond,
        "svd_ok": bool(math.isfinite(lam) and lam > LAM_TRUST),
        "vec": vec,
    }


def stacked_from_hats(
    length: float,
    dimension: int,
    connection: np.ndarray,
    zeros: np.ndarray,
    power: int,
    dens_scale: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    hats = bessel_damped_hat(length, zeros, dimension, connection, power)
    mixed_z = math.sqrt(2.0) * hats
    mixed_t = tail_mixed(
        length, dimension, connection, power, float(zeros[-1]),
        dens_scale=dens_scale,
    )
    return np.vstack([mixed_z, mixed_t]), hats


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
    packed["n_zero_rows"] = int(mixed_z.shape[0])
    packed["n_tail_rows"] = int(mixed_t.shape[0])
    return packed


def outband_min(
    length: float,
    dimension: int,
    connection: np.ndarray,
    gram: np.ndarray,
    power: int,
    t_lo: float,
    dens_kind: str,
) -> dict:
    panels = (
        (t_lo, max(t_lo + 1.0, 40.0), 64),
        (max(t_lo + 1.0, 40.0), 200.0, 48),
        (200.0, 4000.0, 48),
    )
    blocks = []
    for left, right, order in panels:
        if right <= left + 1.0e-12:
            continue
        nodes, weights = roots_legendre(order)
        t_values = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        scaled = 0.5 * (right - left) * weights
        hats = bessel_damped_hat(length, t_values, dimension, connection, power)
        if dens_kind == "flat":
            dens = np.full(t_values.shape, 1.0 / (2.0 * math.pi))
        else:
            dens = np.log(np.maximum(t_values / (2.0 * math.pi), 1.0e-12)) / (
                2.0 * math.pi
            )
            dens = np.maximum(dens, 0.0)
        amp = np.sqrt(np.maximum(2.0 * scaled * dens, 0.0))
        blocks.append(amp[:, None] * hats)
    stacked = np.vstack(blocks) if blocks else np.zeros((1, dimension), dtype=np.complex128)
    return stacked_svd_min(stacked, gram)


def landau_widom_asymp(length: float) -> float:
    bandwidth = float(length) * GAMMA1
    if bandwidth <= 0.0:
        return float("nan")
    return 4.0 * math.sqrt(math.pi * bandwidth) * math.exp(-2.0 * bandwidth)


def sinc_lambda0(length: float, omega: float, n_quad: int = 96) -> tuple[float, float]:
    nodes, weights = roots_legendre(n_quad)
    u_val = length * nodes
    wts = length * weights
    delta = u_val[:, None] - u_val[None, :]
    kern = np.empty_like(delta)
    small = np.abs(delta) < 1.0e-14
    kern[small] = omega / math.pi
    kern[~small] = np.sin(omega * delta[~small]) / (math.pi * delta[~small])
    sw = np.sqrt(np.maximum(wts, 0.0))
    mat = sw[:, None] * kern * sw[None, :]
    evs = np.linalg.eigvalsh(mat)
    lam0 = float(np.clip(evs[-1], 0.0, 1.0))
    return lam0, max(0.0, 1.0 - lam0)


def fit_slope(x_values, y_values) -> tuple[float, float]:
    xs = np.asarray(x_values, dtype=np.float64)
    ys = np.asarray(y_values, dtype=np.float64)
    mask = np.isfinite(xs) & np.isfinite(ys)
    xs, ys = xs[mask], ys[mask]
    if xs.size < 2:
        return float("nan"), float("nan")
    matrix = np.vstack((xs, np.ones_like(xs))).T
    slope, intercept = np.linalg.lstsq(matrix, ys, rcond=None)[0]
    return float(slope), float(intercept)


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
        if not math.isfinite(f_mid):
            break
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


def omega_k_of(q_val: int) -> tuple[int, int]:
    remaining = int(q_val)
    total = 0
    k_exp = 0
    prime = 2
    first = None
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exp = 0
            while remaining % prime == 0:
                remaining //= prime
                exp += 1
                total += 1
            if first is None:
                first = prime
                k_exp = exp
        prime = prime + 1 if prime == 2 else prime + 2
    if remaining > 1:
        total += 1
        if first is None:
            k_exp = 1
        elif remaining == first:
            k_exp += 1
    return total, k_exp


def sanitize_mu(value: float) -> float:
    if value > -CROSS_POS:
        return max(float(value), CROSS_POS)
    return float(value)


class FormCache:
    def __init__(
        self, dimension: int, n_outer: int, power: int,
        logqs: np.ndarray, weights: np.ndarray,
    ):
        self.dimension = int(dimension)
        self.n_outer = int(n_outer)
        self.power = int(power)
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
        gram = gram_matrix(length, self.dimension, self.power, self.n_inner)
        arch = arch_matrix(
            length, self.dimension, self.power, gram, c_l,
            self.n_outer, self.n_inner,
        )
        cosh_vector, sinh_vector = pole_vectors(
            length, self.dimension, self.power, self.n_inner,
        )
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

    def overlap_at(self, length: float, index: int) -> np.ndarray:
        key = (round(float(length), 12), int(index))
        cached = self.ov.get(key)
        if cached is not None:
            return cached
        matrix = overlap_matrix(
            length, float(self.logqs[index]), self.dimension,
            self.power, self.n_inner,
        )
        self.ov[key] = matrix
        return matrix

    def assemble(self, length: float, n_ev: int) -> dict:
        packed = self.free_at(length)
        prime = np.zeros((self.dimension, self.dimension), dtype=np.float64)
        two_l = 2.0 * length
        n_use = max(0, min(int(n_ev), int(self.logqs.size)))
        for index in range(n_use):
            if 0.0 < self.logqs[index] < two_l - 1.0e-15:
                prime = prime + self.weights[index] * self.overlap_at(length, index)
        full = 0.5 * ((packed["free"] - prime) + (packed["free"] - prime).T)
        return {**packed, "prime": prime, "full": full, "n_ev": n_use}


def scan_crossing(mu_fn, left: float, scan_hi: float, gap: float):
    step = max(min(0.04, 0.25 * max(gap, 0.02)), 0.01)
    value, vec, pack = mu_fn(left)
    if sanitize_mu(value) <= CROSS_NEG:
        return float(left), float(value), vec, pack
    prev, prev_raw = left, value
    probe = left
    while probe < scan_hi - 1.0e-14:
        nxt = min(probe + step, scan_hi)
        val_n, vec_n, pack_n = mu_fn(nxt)
        if sanitize_mu(prev_raw) > 0.0 and sanitize_mu(val_n) <= CROSS_NEG:
            def scalar(point, _fn=mu_fn):
                val, _vec, _pack = _fn(point)
                return sanitize_mu(val)

            root, _, _ = bisect_crossing(scalar, prev, nxt)
            if not math.isfinite(root):
                root = float(nxt)
            mu_r, vec_r, pack_r = mu_fn(root)
            return float(root), float(mu_r), vec_r, pack_r
        prev, prev_raw, probe = nxt, val_n, nxt
    return float("inf"), float(value), None, None


def closed_matches(value: float, tol: float = MATCH_TOL) -> list[str]:
    hits = []
    if not math.isfinite(value) or abs(value) < 1.0e-18:
        return hits
    for name, target in CLOSED:
        if abs(target) < 1.0e-18:
            continue
        if abs(abs(float(value)) - abs(target)) / abs(target) <= tol:
            hits.append("%s~%s" % (fmt(value, 4), name))
    return hits


def rel_lambda_err(log_true: np.ndarray, log_pred: np.ndarray) -> float:
    lam_t = np.exp(np.clip(np.asarray(log_true, dtype=np.float64), -700.0, 700.0))
    lam_p = np.exp(np.clip(np.asarray(log_pred, dtype=np.float64), -700.0, 700.0))
    mask = np.isfinite(lam_t) & np.isfinite(lam_p) & (lam_t > 0.0)
    if int(np.sum(mask)) < 1:
        return float("inf")
    ratio = lam_p[mask] / lam_t[mask] - 1.0
    return float(np.sqrt(np.mean(ratio * ratio)))


def aic_like(log_true: np.ndarray, log_pred: np.ndarray, n_par: int) -> float:
    resid = np.asarray(log_true, dtype=np.float64) - np.asarray(log_pred, dtype=np.float64)
    mask = np.isfinite(resid)
    n_use = int(np.sum(mask))
    if n_use < 1:
        return float("inf")
    rss = float(np.dot(resid[mask], resid[mask]))
    return n_use * math.log(rss / n_use + 1.0e-30) + 2.0 * n_par


def ols_predict(x_fit, y_fit, x_all):
    coeff, _, _, _ = np.linalg.lstsq(x_fit, y_fit, rcond=None)
    return coeff, x_all @ coeff


def l_atoms(ell: np.ndarray) -> dict[str, np.ndarray]:
    ell = np.asarray(ell, dtype=np.float64)
    logl = np.log(np.maximum(ell, 1.0e-30))
    return {
        "1": np.ones_like(ell),
        "L": ell,
        "L2": ell * ell,
        "LlogL": ell * logl,
        "logL": logl,
    }


def grammar_monomials(base: dict[str, np.ndarray], depth: int = 3) -> dict[str, np.ndarray]:
    names = list(base.keys())
    feats: dict[str, np.ndarray] = {}
    seen: dict[tuple[int, ...], str] = {}
    for deg in range(1, depth + 1):
        for combo in itertools.combinations_with_replacement(names, deg):
            parts = [name for name in combo if name != "1"]
            key = "1" if not parts else "*".join(parts)
            arr = np.ones_like(next(iter(base.values())))
            for name in combo:
                arr = arr * base[name]
            sig = (
                round(float(arr[0]), 10),
                round(float(arr[arr.size // 2]), 10),
                round(float(arr[-1]), 10),
                round(float(np.dot(arr, arr) / max(arr.size, 1)), 10),
            )
            if sig in seen:
                continue
            seen[sig] = key
            feats[key] = arr
    return feats


def rank_grammar(
    feats: dict[str, np.ndarray],
    y_log: np.ndarray,
    fit_mask: np.ndarray,
    test_mask: np.ndarray,
    max_terms: int = 3,
) -> list[dict]:
    names = [name for name in feats if name != "1"]
    ranked = []
    for k_terms in range(1, max_terms + 1):
        for combo in itertools.combinations(names, k_terms):
            cols = [feats["1"]] + [feats[name] for name in combo]
            x_all = np.column_stack(cols)
            x_fit = x_all[fit_mask]
            y_fit = y_log[fit_mask]
            if x_fit.shape[0] < x_fit.shape[1] + 1:
                continue
            coeff, pred = ols_predict(x_fit, y_fit, x_all)
            hold = rel_lambda_err(y_log[test_mask], pred[test_mask]) if np.any(test_mask) else float("inf")
            fit_e = rel_lambda_err(y_log[fit_mask], pred[fit_mask])
            ranked.append({
                "name": " + ".join(["c0"] + list(combo)),
                "terms": combo,
                "coeff": [float(val) for val in coeff],
                "hold": hold,
                "fit": fit_e,
                "aic": aic_like(y_log[fit_mask], pred[fit_mask], len(coeff)),
                "kind": "sampling-theoretic",
                "pred": pred,
            })
    ranked.sort(key=lambda row: (row["hold"], row["aic"], len(row["terms"])))
    return ranked


def loo_rel(x_all: np.ndarray, y: np.ndarray) -> float:
    n_row = int(x_all.shape[0])
    if n_row < 3:
        return float("inf")
    preds = np.empty(n_row, dtype=np.float64)
    for index in range(n_row):
        mask = np.ones(n_row, dtype=bool)
        mask[index] = False
        coeff, _, _, _ = np.linalg.lstsq(x_all[mask], y[mask], rcond=None)
        preds[index] = float(x_all[index] @ coeff)
    resid = preds - y
    scale = np.maximum(np.abs(y), 1.0e-12)
    return float(np.sqrt(np.mean((resid / scale) ** 2)))


def l_grid(step: float) -> np.ndarray:
    ells = []
    point = L_LO
    while point <= L_HI + 1.0e-12:
        ells.append(round(float(point), 10))
        point += step
    return np.asarray(ells, dtype=np.float64)


def n1_grid(step: float) -> np.ndarray:
    ells = []
    point = L_N1_LO
    while point <= L_N1_HI + 1.0e-12:
        ells.append(round(float(point), 10))
        point += step
    return np.asarray(ells, dtype=np.float64)


def band_slope(ells, lams, lo: float, hi: float) -> float:
    xs, ys = [], []
    for ell, lam in zip(ells, lams):
        if lo - 1.0e-12 <= ell <= hi + 1.0e-12 and math.isfinite(lam) and lam > LAM_TRUST:
            xs.append(ell)
            ys.append(math.log(lam))
    if len(xs) < 2:
        return float("nan")
    slope, _ = fit_slope(xs, ys)
    return float(slope)


def fit_n1_laws(ell: np.ndarray, y_log: np.ndarray) -> dict:
    fit_mask = ell <= FIT_CUT + 1.0e-12
    test_mask = ell > FIT_CUT + 1.0e-12
    if int(np.sum(fit_mask)) < 3 or int(np.sum(test_mask)) < 2:
        return {
            "decision": "N_LIMITED_ARTIFACT",
            "reason": "holdout empty or too few converged points",
            "named": [],
            "n_fit": int(np.sum(fit_mask)),
            "n_test": int(np.sum(test_mask)),
        }
    logl = np.log(np.maximum(ell, 1.0e-30))
    laws = []

    def pack(name, pred, n_par, coeff, extra=None):
        rec_n = {
            "name": name,
            "hold": rel_lambda_err(y_log[test_mask], pred[test_mask]),
            "fit": rel_lambda_err(y_log[fit_mask], pred[fit_mask]),
            "aic": aic_like(y_log[fit_mask], pred[fit_mask], n_par),
            "coeff": [float(val) for val in coeff],
        }
        if extra:
            rec_n.update(extra)
        laws.append(rec_n)

    shape_i = -TWO_GAMMA1 * ell + 0.5 * logl
    c_i = float(np.mean(y_log[fit_mask] - shape_i[fit_mask]))
    pack("slepian_-2g1 L + 1/2 log L + c", shape_i + c_i, 1, [c_i])

    x_q = np.column_stack((ell * ell, ell, np.ones_like(ell)))
    c_q, pred_q = ols_predict(x_q[fit_mask], y_log[fit_mask], x_q)
    pack("quad_-C L^2 + b L + c", pred_q, 3, c_q, extra={"C": float(-c_q[0])})

    x_a = np.column_stack((ell * logl, ell, np.ones_like(ell)))
    c_a, pred_a = ols_predict(x_a[fit_mask], y_log[fit_mask], x_a)
    pack("LlogL_-a L log L + b L + c", pred_a, 3, c_a, extra={"a": float(-c_a[0])})

    x_g = np.column_stack((np.ones_like(ell), ell, ell ** 3))
    c_g, pred_g = ols_predict(x_g[fit_mask], y_log[fit_mask], x_g)
    pack("grammar_r630_c0+L+L3", pred_g, 3, c_g)

    atoms = l_atoms(ell)
    feats = grammar_monomials(atoms, 3)
    gram = rank_grammar(feats, y_log, fit_mask, test_mask, max_terms=3)
    if gram:
        pack("grammar_best " + gram[0]["name"], gram[0]["pred"], len(gram[0]["coeff"]), gram[0]["coeff"])

    laws.sort(key=lambda row: (row["hold"], row["aic"]))
    best = laws[0]
    if best["name"].startswith("slepian"):
        decision = "SLEPIAN_LINEAR"
    elif best["name"].startswith("quad"):
        c_val = float(best.get("C", float("nan")))
        decision = "QUADRATIC(C=%s)" % fmt(c_val, 4)
    else:
        decision = "OTHER(%s)" % best["name"]
    return {
        "decision": decision,
        "reason": "best=%s hold=%s" % (best["name"], fmt(best["hold"], 3)),
        "named": laws,
        "best": best,
        "n_fit": int(np.sum(fit_mask)),
        "n_test": int(np.sum(test_mask)),
    }


def compute_n1(zeros: np.ndarray, smoke: bool) -> dict:
    ns = list(N_SWEEP_SMOKE if smoke else N_SWEEP)
    step = L_N1_STEP_SMOKE if smoke else L_N1_STEP_FULL
    ells = n1_grid(step)
    spaces = (("damped", DAMP_ZERO),) if smoke else (("damped", DAMP_ZERO), ("plain", 0))
    n_max = max(ns)
    table = {}
    n2_rows: list[dict] = []
    for space, power in spaces:
        conn = connection_of(n_max, power)
        table[space] = {n_dim: [] for n_dim in ns}
        for length in ells:
            stacked, hats = stacked_from_hats(float(length), n_max, conn, zeros, power)
            for n_dim in ns:
                gram = gram_matrix(float(length), n_dim, power, n_inner_of(n_dim))
                mp_on = (
                    (not smoke)
                    and space == "damped"
                    and n_dim <= 80
                    and abs(length * 5.0 - round(length * 5.0)) < 1.0e-9
                    and length >= 0.59
                )
                packed = tall_qr_min(stacked[:, :n_dim], gram, mp_refine=mp_on)
                table[space][n_dim].append({
                    "L": float(length),
                    "lam": float(packed["lam"]),
                    "lam_mp": float(packed["lam_mp"]),
                    "smin": float(packed["smin"]),
                    "smax": float(packed["smax"]),
                    "cond": float(packed["cond"]),
                })
                if space == spaces[0][0]:
                    vec = packed["vec"]
                    field = hats[:, : vec.size] @ vec.astype(np.complex128)
                    abs2 = np.abs(field) ** 2
                    peak = float(np.max(abs2)) if abs2.size else 0.0
                    n2_rows.append({
                        "L": float(length),
                        "N": int(n_dim),
                        "n_null": int(np.sum(abs2 < NULL_FRAC * max(peak, 1.0e-300))),
                        "n_zeros": int(abs2.size),
                        "peak": peak,
                    })
    slopes = {}
    for space, _power in spaces:
        slopes[space] = {}
        for n_dim in ns:
            rows = table[space][n_dim]
            ell_n = [row["L"] for row in rows]
            lam_n = [row["lam"] for row in rows]
            slopes[space][n_dim] = {
                "b06": band_slope(ell_n, lam_n, 0.30, 0.60),
                "b10": band_slope(ell_n, lam_n, 0.60, 1.00),
                "b14": band_slope(ell_n, lam_n, 1.00, 1.40),
            }
    conv = []
    n_hi, n_lo = ns[-1], ns[-2] if len(ns) >= 2 else ns[-1]
    unconv = 0
    n_hi_rows = table[spaces[0][0]][n_hi]
    n_lo_rows = table[spaces[0][0]][n_lo]
    for hi_row, lo_row in zip(n_hi_rows, n_lo_rows):
        lam_hi, lam_lo = hi_row["lam"], lo_row["lam"]
        rel = (
            abs(lam_hi - lam_lo) / max(abs(lam_hi), abs(lam_lo), 1.0e-300)
            if math.isfinite(lam_hi) and math.isfinite(lam_lo) and max(abs(lam_hi), abs(lam_lo)) > LAM_TRUST
            else float("inf")
        )
        near_floor = math.isfinite(lam_hi) and lam_hi < 1.0e-28
        ok = (
            rel <= CONV_REL
            and math.isfinite(lam_hi)
            and lam_hi > LAM_TRUST
            and not near_floor
        )
        if not ok:
            unconv += 1
        conv.append({
            "L": hi_row["L"],
            "lam": lam_hi,
            "rel": rel,
            "ok": ok,
            "floor": near_floor,
        })

    test_band = [row for row in conv if row["L"] > FIT_CUT]
    n_test_ok = sum(1 for row in test_band if row["ok"])
    artifact = (
        len(test_band) < 2
        or (len(test_band) > 0 and n_test_ok / max(len(test_band), 1) < 0.5)
    )
    use_rows = [row for row in conv if row["ok"]]
    if not use_rows:
        use_rows = [row for row in conv if math.isfinite(row["lam"]) and row["lam"] > LAM_TRUST]
    ell = np.array([row["L"] for row in use_rows], dtype=np.float64)
    y_log = np.log(np.array([max(row["lam"], LAM_TRUST) for row in use_rows], dtype=np.float64))
    conv_lo = [row for row in use_rows if row["L"] <= FIT_CUT + 1.0e-12]
    desc = {}
    if len(conv_lo) >= 4:
        ell_d = np.array([row["L"] for row in conv_lo], dtype=np.float64)
        y_d = np.log(np.array([max(row["lam"], LAM_TRUST) for row in conv_lo], dtype=np.float64))
        logl_d = np.log(np.maximum(ell_d, 1.0e-30))
        x_q = np.column_stack((ell_d * ell_d, ell_d, np.ones_like(ell_d)))
        c_q, _ = ols_predict(x_q, y_d, x_q)
        x_a = np.column_stack((ell_d * logl_d, ell_d, np.ones_like(ell_d)))
        c_a, _ = ols_predict(x_a, y_d, x_a)
        desc = {
            "C": float(-c_q[0]),
            "a": float(-c_a[0]),
            "n": int(ell_d.size),
            "note": "OLS on converged L<=1 only; no holdout",
        }
    if artifact:
        laws = {
            "decision": "N_LIMITED_ARTIFACT",
            "reason": "lambda* does not converge  N=%d→%d on L>1 (ok=%d/%d)" % (
                n_lo, n_hi, n_test_ok, len(test_band),
            ),
            "named": [],
            "n_fit": int(len(conv_lo)),
            "n_test": n_test_ok,
            "desc": desc,
        }
    else:
        laws = fit_n1_laws(ell, y_log)
        laws["desc"] = desc
    anchors = {}
    for want in (0.60, 1.00, 1.40):
        row = min(n_hi_rows, key=lambda item, w=want: abs(item["L"] - w))
        anchors[want] = float(row["lam"])
    return {
        "ns": ns,
        "ells": [float(val) for val in ells],
        "spaces": [name for name, _p in spaces],
        "table": table,
        "slopes": slopes,
        "conv": conv,
        "n_unconv": unconv,
        "laws": laws,
        "anchors": anchors,
        "n2": n2_rows,
        "n_max": n_max,
        "space0": spaces[0][0],
    }


def compute_n2(n1: dict) -> list[dict]:
    return list(n1.get("n2") or [])


def synthetic_zeros(zeros: np.ndarray, kind: str) -> tuple[np.ndarray, float | None]:
    gamma1 = float(zeros[0])
    n_use = int(zeros.size)
    dens_scale = None
    if kind == "true":
        return zeros.copy(), None
    if kind == "flat_gap":
        gap = 2.0 * math.pi / math.log(max(gamma1, math.e))
        out = gamma1 + gap * np.arange(n_use, dtype=np.float64)
        return out, 1.0 / gap
    if kind.startswith("scale_W"):
        width = float(kind.replace("scale_W", ""))
        return zeros * (width / gamma1), None
    if kind == "first_to_20":
        out = zeros.copy()
        out[0] = 20.0
        return out, None
    return zeros.copy(), None


def compute_n3(zeros: np.ndarray, smoke: bool) -> dict:
    worlds = ("true", "flat_gap", "scale_W10", "scale_W20", "first_to_20")
    n_dim = 40 if smoke else 160
    step = 0.20 if smoke else 0.10
    ells = n1_grid(step)
    power = DAMP_ZERO
    conn = connection_of(n_dim, power)
    n_inner = n_inner_of(n_dim)
    out = {}
    for kind in worlds:
        z_use, dens = synthetic_zeros(zeros, kind)
        rows = []
        for length in ells:
            stacked, _hats = stacked_from_hats(
                float(length), n_dim, conn, z_use, power, dens_scale=dens,
            )
            gram = gram_matrix(float(length), n_dim, power, n_inner)
            packed = tall_qr_min(stacked, gram, mp_refine=False)
            rows.append({"L": float(length), "lam": float(packed["lam"])})
        use = [
            row for row in rows
            if math.isfinite(row["lam"]) and row["lam"] > 1.0e-28
        ]
        ell = np.array([row["L"] for row in use], dtype=np.float64)
        if ell.size < 4:
            out[kind] = {
                "alpha": float("nan"), "C": float("nan"), "a": float("nan"),
                "c": float("nan"), "n": int(ell.size), "decision": "N_LIMITED_ARTIFACT",
            }
            continue
        y_log = np.log(np.array([row["lam"] for row in use], dtype=np.float64))
        logl = np.log(np.maximum(ell, 1.0e-30))
        x_lin = np.column_stack((ell, 0.5 * logl, np.ones_like(ell)))
        c_lin, _ = ols_predict(x_lin, y_log, x_lin)
        x_q = np.column_stack((ell * ell, ell, np.ones_like(ell)))
        c_q, _ = ols_predict(x_q, y_log, x_q)
        x_a = np.column_stack((ell * logl, ell, np.ones_like(ell)))
        c_a, _ = ols_predict(x_a, y_log, x_a)
        laws = fit_n1_laws(ell, y_log)
        out[kind] = {
            "alpha": float(-c_lin[0]),
            "C": float(-c_q[0]),
            "a": float(-c_a[0]),
            "c": float(c_lin[2]),
            "n": int(ell.size),
            "decision": laws.get("decision", "OTHER"),
            "hold_best": (
                float(laws["best"]["hold"]) if laws.get("best") else float("nan")
            ),
        }
    true_a = out.get("true", {}).get("alpha", float("nan"))
    w10 = out.get("scale_W10", {}).get("alpha", float("nan"))
    w20 = out.get("scale_W20", {}).get("alpha", float("nan"))
    flat_a = out.get("flat_gap", {}).get("alpha", float("nan"))
    first20 = out.get("first_to_20", {}).get("alpha", float("nan"))
    scale_ok = (
        math.isfinite(w10) and math.isfinite(w20) and w20 > 0.0
        and abs(w20 / max(w10, 1e-30) - 2.0) < 0.45
    )
    dens_insens = (
        math.isfinite(true_a) and math.isfinite(flat_a)
        and abs(true_a - flat_a) / max(abs(true_a), 1.0) < 0.35
    )
    band_edge = (
        math.isfinite(first20) and math.isfinite(true_a)
        and first20 > true_a * 1.15
    )
    if scale_ok and dens_insens:
        reading = "sampling-theoretic (band-edge; alpha ~ 2W, density-insensitive)"
    elif scale_ok and band_edge:
        reading = "sampling-theoretic (tracks first-zero W)"
    elif (not dens_insens) and (not scale_ok):
        reading = "arithmetic (density-driven)"
    else:
        reading = "mixed / unresolved"
    return {"worlds": out, "reading": reading, "scale_ok": scale_ok, "dens_insens": dens_insens}


def dbn_tail(xk: float, xkp: float, t_lo: float, t_hi: float, n_quad: int = 32) -> float:
    if t_hi <= t_lo + 1.0e-12:
        return 0.0
    nodes, weights = roots_legendre(n_quad)
    t_val = 0.5 * (t_hi - t_lo) * nodes + 0.5 * (t_hi + t_lo)
    scaled = 0.5 * (t_hi - t_lo) * weights
    dens = np.log(np.maximum(t_val / (2.0 * math.pi), 1.0e-12)) / (2.0 * math.pi)
    den = (xkp - t_val) * (xk - t_val)
    den = np.where(np.abs(den) < 1.0e-30, np.nan, den)
    integrand = dens / den
    integrand = np.where(np.isfinite(integrand), integrand, 0.0)
    return float(np.dot(scaled, integrand))


def _bk_one(x_val: np.ndarray, index: int, window: int) -> float:
    n_use = int(x_val.size)
    xk = float(x_val[index])
    xkp = float(x_val[index + 1])
    j_lo = max(0, index - window)
    j_hi = min(n_use, index + 2 + window)
    others = np.concatenate((x_val[j_lo:index], x_val[index + 2:j_hi]))
    if others.size:
        den = (xkp - others) * (xk - others)
        core = float(np.sum(1.0 / np.where(np.abs(den) < 1.0e-30, np.nan, den)))
        if not math.isfinite(core):
            core = 0.0
    else:
        core = 0.0
    tail_l = dbn_tail(xk, xkp, 2.0 * math.pi, float(x_val[j_lo])) if j_lo > 0 else 0.0
    if j_hi < n_use:
        tail_r = dbn_tail(xk, xkp, float(x_val[j_hi - 1]), float(x_val[-1]) + 2000.0)
    else:
        tail_r = dbn_tail(xk, xkp, float(x_val[-1]), float(x_val[-1]) + 2000.0)
    return ((xkp - xk) ** 2) * (core + tail_l + tail_r)


def compute_n4(zeros: np.ndarray) -> dict:
    x_val = np.asarray(zeros, dtype=np.float64)
    n_use = int(x_val.size)
    window = min(N4_WINDOW, max(n_use - 2, 1))
    b_vals = np.empty(n_use - 1, dtype=np.float64)
    for index in range(n_use - 1):
        b_vals[index] = _bk_one(x_val, index, window)
    finite = b_vals[np.isfinite(b_vals)]
    mid = (n_use - 1) // 2
    x2 = x_val.copy()
    x2[mid + 1] = x_val[mid] + N4_COMPRESS * (x_val[mid + 1] - x_val[mid])
    b_comp = _bk_one(x2, mid, window)
    return {
        "n": int(finite.size),
        "max": float(np.max(finite)) if finite.size else float("nan"),
        "p99": float(np.percentile(finite, 99)) if finite.size else float("nan"),
        "frac_lt2": float(np.mean(finite < 2.0)) if finite.size else float("nan"),
        "median": float(np.median(finite)) if finite.size else float("nan"),
        "b_compress": float(b_comp),
        "b_mid": float(b_vals[mid]) if math.isfinite(b_vals[mid]) else float("nan"),
        "k_mid": int(mid),
    }


def _lam_close(a: float, b: float) -> bool:
    if not (math.isfinite(a) and math.isfinite(b)):
        return False
    hi = max(abs(a), abs(b))
    if hi < 1.0e-24:
        return True
    return abs(a - b) / max(hi, 1.0e-30) <= 1.0e-8


def _n1_row(n1: dict, space: str, n_dim: int, want: float) -> dict:
    rows = n1["table"][space][n_dim]
    return min(rows, key=lambda item, w=want: abs(item["L"] - w))


def fingerprint_n1(n1: dict, zeros: np.ndarray, smoke: bool) -> bool:
    space = n1["space0"]
    power = DAMP_ZERO
    if smoke:
        n1_b = compute_n1(zeros, True)
        for want in (0.60, 1.00, 1.40):
            a_row = _n1_row(n1, space, n1["ns"][-1], want)
            b_row = _n1_row(n1_b, space, n1_b["ns"][-1], want)
            if not _lam_close(a_row["lam"], b_row["lam"]):
                return False
        return True
    n_dim = int(n1["ns"][-1])
    conn = connection_of(n_dim, power)
    n_inner = n_inner_of(n_dim)
    ok = True
    for want in (0.60, 1.00, 1.40):
        row = _n1_row(n1, space, n_dim, want)
        length = float(row["L"])
        stacked, _hats = stacked_from_hats(length, n_dim, conn, zeros, power)
        gram = gram_matrix(length, n_dim, power, n_inner)
        packed = tall_qr_min(stacked, gram, mp_refine=False)
        if not _lam_close(float(packed["lam"]), float(row["lam"])):
            ok = False
    return ok


def fingerprint_dual(rec: dict, smoke: bool, n1: dict | None = None) -> bool:
    """Second identical evaluation of λ* (D1 grid + N1 anchors)."""
    zeros = load_zeros(rec["n_zeros"])
    if smoke:
        _CL_CACHE.clear()
        rec2 = compute(True)
        sha1 = payload_sha({
            "lam": [[round(row["L"], 6), round(row["lam"], 16)] for row in rec["lam_rows"]],
            "L_cross": rec["L_cross"],
            "delta": [[int(row["q"]), row["delta"]] for row in rec["lead_rows"]],
        })
        sha2 = payload_sha({
            "lam": [[round(row["L"], 6), round(row["lam"], 16)] for row in rec2["lam_rows"]],
            "L_cross": rec2["L_cross"],
            "delta": [[int(row["q"]), row["delta"]] for row in rec2["lead_rows"]],
        })
        n1_ok = True if n1 is None else fingerprint_n1(n1, zeros, True)
        return sha1 == sha2 and n1_ok
    dimension = int(rec["dimension"])
    conn = connection_of(dimension, DAMP_ZERO)
    n_inner_z = n_inner_of(dimension)
    ok = True
    for want in (0.30, 0.40, 0.50):
        row = min(rec["lam_rows"], key=lambda item, w=want: abs(item["L"] - w))
        length = float(row["L"])
        gram = gram_matrix(length, dimension, DAMP_ZERO, n_inner_z)
        zside = zero_side_min(length, dimension, conn, zeros, gram, DAMP_ZERO)
        if not _lam_close(float(zside["lam"]), float(row["lam"])):
            ok = False
    if n1 is not None:
        ok = ok and fingerprint_n1(n1, zeros, False)
    return ok


def compute(smoke: bool) -> dict:
    if smoke:
        dimension = N_ZERO_SMOKE
        n_zeros = N_ZEROS_SMOKE
        n_src = N_SRC_SMOKE
        n_lead = N_LEAD_SMOKE
        n_pin = N_PIN_SMOKE
        n_outer = N_OUTER_SMOKE
        step = L_STEP_SMOKE
        mu_step = MU_STEP_SMOKE
        q_max = Q_MAX_SMOKE
        pin_grid = (0.40,)
    else:
        dimension = N_ZERO_FULL
        n_zeros = N_ZEROS_FULL
        n_src = N_SRC_FULL
        n_lead = N_LEAD_FULL
        n_pin = N_PIN_FULL
        n_outer = N_OUTER_FULL
        step = L_STEP_FULL
        mu_step = MU_STEP_FULL
        q_max = Q_MAX_FULL
        pin_grid = PIN_L

    zeros = load_zeros(n_zeros)
    conn = connection_of(dimension, DAMP_ZERO)
    ells = l_grid(step)
    n_inner_z = n_inner_of(dimension)

    lam_rows = []
    for length in ells:
        gram = gram_matrix(length, dimension, DAMP_ZERO, n_inner_z)
        zside = zero_side_min(length, dimension, conn, zeros, gram, DAMP_ZERO)
        n_slep = min(24, dimension)
        gram_s = gram[:n_slep, :n_slep]
        conn_s = conn[:n_slep, :]
        slep = outband_min(
            length, n_slep, conn_s, gram_s, DAMP_ZERO, GAMMA1, "flat",
        )
        twob = outband_min(
            length, n_slep, conn_s, gram_s, DAMP_ZERO, GAMMA1, "density",
        )
        lam = float(zside["lam"]) if math.isfinite(zside["lam"]) else float(zside["lam_svd"])
        floor_hit = bool(
            (not zside["svd_ok"])
            or (not math.isfinite(lam))
            or lam <= LAM_FLOOR
            or (math.isfinite(zside["lam_svd"]) and zside["lam_svd"] <= LAM_FLOOR)
        )
        reliable = bool(
            math.isfinite(lam)
            and lam > LAM_FLOOR
            and zside["svd_ok"]
            and math.isfinite(zside["lam_svd"])
            and zside["lam_svd"] > LAM_FLOOR
        )
        lam_rows.append({
            "L": float(length),
            "lam": lam,
            "lam_ray": float(zside["lam"]),
            "lam_svd": float(zside["lam_svd"]),
            "cond": float(zside["cond"]),
            "smin": float(zside["smin"]),
            "svd_ok": bool(zside["svd_ok"]),
            "floor": bool(floor_hit),
            "reliable": reliable,
            "slep": float(slep["lam"]) if math.isfinite(slep["lam"]) else float(slep["lam_svd"]),
            "twob": float(twob["lam"]) if math.isfinite(twob["lam"]) else float(twob["lam_svd"]),
            "widom": landau_widom_asymp(float(length)),
        })

    floor_L = float("nan")
    for row in lam_rows:
        if row["floor"]:
            floor_L = float(row["L"])
            break

    mu_count = int(round((MU_HI - MU_LO) / mu_step)) + 1
    mu_ells = np.round(MU_LO + mu_step * np.arange(mu_count), 10)
    mu_rows = []
    for length in mu_ells:
        forms = assemble_source(float(length), n_src, 0, n_outer, False)
        mu_full, _vec = min_rayleigh(forms["free"], forms["gram"])
        mu_odd = odd_min(forms["free"], forms["gram"])
        mu_rows.append({
            "L": float(length),
            "mu_full": float(mu_full),
            "mu_odd": float(mu_odd),
        })

    l_cross = float("nan")
    for prev, nxt in zip(mu_rows, mu_rows[1:]):
        a_val, b_val = prev["mu_odd"], nxt["mu_odd"]
        if math.isfinite(a_val) and math.isfinite(b_val) and a_val > 0.0 >= b_val:
            def mu_fn(point, dim=n_src, nout=n_outer):
                packed = assemble_source(float(point), dim, 0, nout, False)
                return odd_min(packed["free"], packed["gram"])

            root, _, _ = bisect_crossing(mu_fn, prev["L"], nxt["L"])
            l_cross = float(root) if math.isfinite(root) else float(nxt["L"])
            break
    if not math.isfinite(l_cross):
        for prev, nxt in zip(mu_rows, mu_rows[1:]):
            a_val, b_val = prev["mu_full"], nxt["mu_full"]
            if math.isfinite(a_val) and math.isfinite(b_val) and a_val > 0.0 >= b_val:
                def mu_fn2(point, dim=n_src, nout=n_outer):
                    packed = assemble_source(float(point), dim, 0, nout, False)
                    val, _ = min_rayleigh(packed["free"], packed["gram"])
                    return float(val)

                root, _, _ = bisect_crossing(mu_fn2, prev["L"], nxt["L"])
                l_cross = float(root) if math.isfinite(root) else float(nxt["L"])
                break

    qs, logqs, weights, ell_ev, q_next, _lam_tab = prime_powers_upto(q_max)
    ells_ext = np.concatenate(
        [ell_ev, np.array([0.5 * math.log(q_next)], dtype=np.float64)]
    )
    cache = FormCache(n_lead, n_outer, DAMP_ZERO, logqs, weights)
    lead_rows = []
    n_events = len(qs)
    for index in range(n_events):
        left = float(ells_ext[index])
        right = float(ells_ext[index + 1])
        gap = right - left
        j_ev = index + 1

        def mu_anc(point, drop=1, keep=j_ev):
            n_keep = max(0, keep - drop)
            packed = cache.assemble(point, n_keep)
            value, vec = min_rayleigh(packed["full"], packed["gram"])
            return value, vec, packed

        crossing, _mu_at, _vec_x, _forms_x = scan_crossing(
            mu_anc, left, right + EXT_PAD, gap,
        )
        delta = crossing - left if math.isfinite(crossing) else float("inf")
        omega, k_exp = omega_k_of(int(qs[index]))
        lead_rows.append({
            "j": j_ev,
            "q": int(qs[index]),
            "L": left,
            "gap": float(gap),
            "delta": float(delta),
            "w": float(weights[index]),
            "logq": float(logqs[index]),
            "Omega": int(omega),
            "k": int(k_exp),
            "frozen": float(R619_LEADS.get(int(qs[index]), float("nan"))),
        })

    pin_rows = []
    for length in pin_grid:
        forms = assemble_source(float(length), n_pin, DAMP_SRC, n_outer, True)
        gram = forms["gram"]
        free = forms["free"]
        overlap0 = forms["overlap"]

        def lam_of_weight(weight: float, _free=free, _ov=overlap0, _g=gram):
            quadratic = _free - weight * _ov
            value, _vec = min_rayleigh(quadratic, _g)
            return value

        lam_w2, vec_w2 = min_rayleigh(forms["full"], gram)
        prime_h = float(vec_w2 @ forms["prime"] @ vec_w2)
        if lam_w2 <= 0.0:
            delta_crit = 0.0
        else:
            weight_hi = W2
            found = False
            for _scale in range(1, 25):
                weight_hi = W2 * (1.5 ** _scale)
                if lam_of_weight(weight_hi) <= 0.0:
                    found = True
                    break
            if found:
                def f_delta(delta: float) -> float:
                    return lam_of_weight(W2 * (1.0 + delta))

                delta_hi = weight_hi / W2 - 1.0
                delta_crit, _, _ = bisect_crossing(f_delta, 0.0, delta_hi)
            else:
                delta_crit = float("inf")
        ratio = (
            float(delta_crit) * abs(prime_h) / abs(lam_w2)
            if abs(lam_w2) > 1.0e-30 and math.isfinite(delta_crit)
            else float("nan")
        )
        pin_rows.append({
            "L": float(length),
            "lam": float(lam_w2),
            "delta": float(delta_crit),
            "prime": float(prime_h),
            "ratio": float(ratio),
            "r615": float(R615_DCRIT.get(float(length), float("nan"))),
        })

    sinc40 = sinc_lambda0(0.40, GAMMA1)
    near40 = min(lam_rows, key=lambda row: abs(row["L"] - 0.40))

    return {
        "smoke": bool(smoke),
        "n_zeros": int(zeros.size),
        "gamma1": float(zeros[0]) if zeros.size else float("nan"),
        "gammaN": float(zeros[-1]) if zeros.size else float("nan"),
        "zeros_src": "npy" if ZEROS_CACHE.is_file() else "mpmath",
        "dimension": int(dimension),
        "n_src": int(n_src),
        "n_lead": int(n_lead),
        "n_pin": int(n_pin),
        "q_max": int(q_max),
        "lam_rows": lam_rows,
        "floor_L": float(floor_L),
        "mu_rows": mu_rows,
        "L_cross": float(l_cross),
        "lead_rows": lead_rows,
        "pin_rows": pin_rows,
        "sinc40_lam0": float(sinc40[0]),
        "sinc40_leak": float(sinc40[1]),
        "slep40": float(near40["slep"]),
        "cL03": c_L_of(0.3),
    }


def fit_margin_laws(rec: dict) -> dict:
    rows = [row for row in rec["lam_rows"] if row["reliable"] and row["lam"] > 0.0]
    ell = np.array([row["L"] for row in rows], dtype=np.float64)
    y_log = np.log(np.array([row["lam"] for row in rows], dtype=np.float64))
    slep = np.array([row["slep"] for row in rows], dtype=np.float64)
    twob = np.array([row["twob"] for row in rows], dtype=np.float64)
    widom = np.array([row["widom"] for row in rows], dtype=np.float64)
    fit_mask = ell <= FIT_CUT + 1.0e-12
    test_mask = ell > FIT_CUT + 1.0e-12
    if int(np.sum(test_mask)) < 2:
        n_use = int(ell.size)
        n_hold = max(1, n_use // 4)
        order = np.argsort(ell)
        test_mask = np.zeros(n_use, dtype=bool)
        test_mask[order[-n_hold:]] = True
        fit_mask = ~test_mask
        if int(np.sum(fit_mask)) < 3:
            fit_mask = np.ones(n_use, dtype=bool)
            test_mask = fit_mask.copy()
    named = []

    def named_from_pred(name, pred, n_par, coeff, kind, extra=None):
        hold = rel_lambda_err(y_log[test_mask], pred[test_mask])
        fit_e = rel_lambda_err(y_log[fit_mask], pred[fit_mask])
        rec_n = {
            "name": name,
            "hold": hold,
            "fit": fit_e,
            "aic": aic_like(y_log[fit_mask], pred[fit_mask], n_par),
            "coeff": [float(val) for val in coeff],
            "kind": kind,
            "n_par": n_par,
        }
        if extra:
            rec_n.update(extra)
        return rec_n

    x_quad = np.column_stack((ell * ell, ell, np.ones_like(ell)))
    c_quad, pred_quad = ols_predict(x_quad[fit_mask], y_log[fit_mask], x_quad)
    named.append(named_from_pred(
        "quad_-C L^2+bL+c", pred_quad, 3, c_quad, "sampling-theoretic",
        extra={"C": float(-c_quad[0])},
    ))

    pred_slepian = -TWO_GAMMA1 * ell
    c_sl = float(np.mean(y_log[fit_mask] - pred_slepian[fit_mask]))
    named.append(named_from_pred(
        "slepian_-2gamma1 L+c", pred_slepian + c_sl, 1, [c_sl], "sampling-theoretic",
    ))

    logl = np.log(np.maximum(ell, 1.0e-30))
    x_arc = np.column_stack((ell * ell, ell * logl, np.ones_like(ell)))
    c_arc, pred_arc = ols_predict(x_arc[fit_mask], y_log[fit_mask], x_arc)
    named.append(named_from_pred(
        "widom_arc_-A L^2-B L logL+c", pred_arc, 3, c_arc, "sampling-theoretic",
        extra={"A": float(-c_arc[0]), "B": float(-c_arc[1])},
    ))

    def affine_log(src, name):
        src = np.asarray(src, dtype=np.float64)
        good = np.isfinite(src) & (src > LAM_FLOOR)
        if int(np.sum(good & fit_mask)) < 2:
            pred = np.full_like(y_log, np.nan)
            return named_from_pred(name, pred, 1, [float("nan")], "sampling-theoretic")
        log_src = np.log(np.maximum(src, 1.0e-300))
        x_aff = np.column_stack((log_src, np.ones_like(log_src)))
        coeff, pred = ols_predict(x_aff[fit_mask], y_log[fit_mask], x_aff)
        return named_from_pred(name, pred, 2, coeff, "sampling-theoretic")

    named.append(affine_log(slep, "plunge_exact_1-lambda0"))
    named.append(affine_log(widom, "plunge_asymp_LandauWidom"))
    named.append(affine_log(twob, "plunge_twoband_density"))

    atoms = l_atoms(ell)
    feats = grammar_monomials(atoms, 3)
    grammar = rank_grammar(feats, y_log, fit_mask, test_mask, max_terms=3)
    top3 = grammar[:3]

    matches = []
    for law in named:
        for coeff in law["coeff"]:
            matches.extend("%s:%s" % (law["name"], hit) for hit in closed_matches(coeff))
        if "C" in law:
            matches.extend("C:%s" % hit for hit in closed_matches(law["C"]))
        if "A" in law:
            matches.extend("A:%s" % hit for hit in closed_matches(law["A"]))
            matches.extend("B:%s" % hit for hit in closed_matches(law["B"]))
    for law in top3:
        for coeff in law["coeff"]:
            matches.extend("%s:%s" % (law["name"], hit) for hit in closed_matches(coeff))

    named_sorted = sorted(named, key=lambda row: (row["hold"], row["aic"]))
    best_named = named_sorted[0] if named_sorted else None
    best_gram = top3[0] if top3 else None
    quad = next(row for row in named if row["name"].startswith("quad"))
    plunge_group = [row for row in named if row["name"].startswith("plunge")]
    best_plunge = min(plunge_group, key=lambda row: row["hold"]) if plunge_group else None

    candidates = []
    if best_named is not None:
        candidates.append(("named", best_named))
    if best_gram is not None:
        candidates.append(("grammar", best_gram))
    winner = min(candidates, key=lambda pair: pair[1]["hold"]) if candidates else None

    quad_terms = {"L2", "L", "1", "c0"}
    gram_is_quad = False
    if best_gram is not None:
        terms = set(best_gram["terms"]) | {"1", "c0"}
        gram_is_quad = terms <= {"L2", "L", "1"} or set(best_gram["terms"]) <= {"L2", "L"}

    margin_verdict = "MARGIN_LAW_UNRESOLVED"
    margin_detail = ""
    if winner is not None:
        hold_w = float(winner[1]["hold"])
        is_quad = (
            winner[1]["name"].startswith("quad")
            or (winner[0] == "grammar" and gram_is_quad)
        )
        is_plunge = winner[1]["name"].startswith("plunge") or (
            best_plunge is not None
            and winner[1]["hold"] >= best_plunge["hold"] - 1.0e-15
            and best_plunge["hold"] <= hold_w + 1.0e-15
            and (best_named is not None and best_named["name"].startswith("plunge"))
        )
        if is_quad and hold_w <= REL_WIN:
            c_val = float(quad["C"])
            hits = closed_matches(c_val)
            closest = hits[0] if hits else "no_closed_1pct"
            margin_verdict = "MARGIN_LAW_QUADRATIC(C=%s,%s)" % (fmt(c_val, 4), closest)
            margin_detail = "hold=%s" % fmt(hold_w, 4)
        elif (
            (is_plunge or (best_plunge is not None and best_plunge["hold"] <= hold_w + 1e-15
                           and best_plunge["hold"] <= quad["hold"]))
            and best_plunge is not None
            and best_plunge["hold"] <= min(quad["hold"], hold_w) + 1e-15
        ):
            margin_verdict = "MARGIN_LAW_PLUNGE"
            margin_detail = "%s hold=%s" % (best_plunge["name"], fmt(best_plunge["hold"], 4))
        elif is_plunge:
            margin_verdict = "MARGIN_LAW_PLUNGE"
            margin_detail = "%s hold=%s" % (winner[1]["name"], fmt(hold_w, 4))
        else:
            margin_verdict = "MARGIN_LAW_UNRESOLVED"
            margin_detail = "best=%s hold=%s" % (winner[1]["name"], fmt(hold_w, 4))

    n_fit = int(np.sum(fit_mask))
    n_test = int(np.sum(test_mask))
    return {
        "named": named_sorted,
        "grammar_top": top3,
        "matches": matches,
        "verdict": margin_verdict,
        "detail": margin_detail,
        "quad": quad,
        "best_plunge": best_plunge,
        "n_fit": n_fit,
        "n_test": n_test,
        "n_rel": int(ell.size),
    }


def fit_lead_laws(lead_rows: list[dict]) -> dict:
    usable = [
        row for row in lead_rows
        if math.isfinite(row["delta"]) and not math.isinf(row["delta"])
    ]
    if len(usable) < 3:
        return {
            "verdict": "LEAD_LAW_CONST",
            "top": [],
            "const_loo": float("nan"),
            "const": float("nan"),
            "detail": "too_few",
        }
    y_val = np.array([row["delta"] for row in usable], dtype=np.float64)
    q_val = np.array([row["q"] for row in usable], dtype=np.float64)
    logq = np.array([row["logq"] for row in usable], dtype=np.float64)
    gap = np.array([row["gap"] for row in usable], dtype=np.float64)
    w_val = np.array([row["w"] for row in usable], dtype=np.float64)
    omega = np.array([row["Omega"] for row in usable], dtype=np.float64)
    k_val = np.array([row["k"] for row in usable], dtype=np.float64)
    base = {
        "1": np.ones_like(y_val),
        "q": q_val,
        "logq": logq,
        "gap": gap,
        "w": w_val,
        "Omega": omega,
        "k": k_val,
    }
    feats = grammar_monomials(base, 3)
    names = [name for name in feats if name != "1"]
    ranked = []
    const = float(np.mean(y_val))
    const_loo = float(
        np.sqrt(np.mean(((y_val - const) / np.maximum(np.abs(y_val), 1e-12)) ** 2))
    )
    # leave-one-out mean
    loo_c = []
    for index in range(y_val.size):
        mean_i = float(np.mean(np.delete(y_val, index)))
        loo_c.append((mean_i - y_val[index]) / max(abs(y_val[index]), 1e-12))
    const_loo = float(np.sqrt(np.mean(np.square(loo_c))))
    ranked.append({
        "name": "const",
        "loo": const_loo,
        "coeff": [const],
        "terms": (),
    })
    for k_terms in range(1, 3):
        for combo in itertools.combinations(names, k_terms):
            x_all = np.column_stack([feats["1"]] + [feats[name] for name in combo])
            if x_all.shape[0] <= x_all.shape[1] + 1:
                continue
            loo = loo_rel(x_all, y_val)
            coeff, _, _, _ = np.linalg.lstsq(x_all, y_val, rcond=None)
            ranked.append({
                "name": " + ".join(["c0"] + list(combo)),
                "loo": loo,
                "coeff": [float(val) for val in coeff],
                "terms": combo,
            })
    ranked.sort(key=lambda row: (row["loo"], len(row["terms"])))
    top = ranked[:3]
    best = top[0]
    if best["name"] == "const" or const_loo <= best["loo"] + 1.0e-15:
        verdict = "LEAD_LAW_CONST"
        detail = "const=%s loo=%s" % (fmt(const, 4), fmt(const_loo, 4))
    else:
        verdict = "LEAD_LAW(%s)" % best["name"]
        detail = "loo=%s const_loo=%s" % (fmt(best["loo"], 4), fmt(const_loo, 4))
    matches = []
    for law in top:
        for coeff in law["coeff"]:
            matches.extend("%s:%s" % (law["name"], hit) for hit in closed_matches(coeff))
    return {
        "verdict": verdict,
        "top": top,
        "const_loo": const_loo,
        "const": const,
        "detail": detail,
        "matches": matches,
        "n": int(y_val.size),
    }


def fit_pinning(rec: dict, laws: dict) -> dict:
    pins = rec["pin_rows"]
    ell = np.array([row["L"] for row in pins], dtype=np.float64)
    dcrit = np.array([row["delta"] for row in pins], dtype=np.float64)
    logs = np.log(np.maximum(dcrit, 1.0e-30))
    finite = np.isfinite(logs) & np.isfinite(dcrit) & (dcrit > 0.0)
    slope_d, intercept_d = (
        fit_slope(ell[finite], logs[finite]) if int(np.sum(finite)) >= 2
        else (float("nan"), float("nan"))
    )
    rel_rows = [
        row for row in rec["lam_rows"]
        if row["reliable"] and 0.36 <= row["L"] <= 0.56 and row["lam"] > 0.0
    ]
    if len(rel_rows) >= 2:
        slope_l, _ = fit_slope(
            [row["L"] for row in rel_rows],
            [math.log(row["lam"]) for row in rel_rows],
        )
    else:
        slope_l = float("nan")
    ratios = [row["ratio"] for row in pins if math.isfinite(row["ratio"])]
    ratio_med = float(np.median(ratios)) if ratios else float("nan")
    return {
        "slope_dcrit": float(slope_d),
        "intercept_dcrit": float(intercept_d),
        "slope_lam": float(slope_l),
        "ratio_med": ratio_med,
        "ratios": [float(row["ratio"]) for row in pins],
        "kind": "sampling-theoretic",
    }


def numeric_payload(rec: dict, laws: dict, leads: dict, pin: dict, n1=None, n3=None, n4=None) -> dict:
    payload = {
        "lam": [
            [round(row["L"], 6), round(row["lam"], 18) if math.isfinite(row["lam"]) else None]
            for row in rec["lam_rows"]
        ],
        "floor_L": rec["floor_L"],
        "L_cross": rec["L_cross"],
        "delta": [
            [int(row["q"]), round(row["delta"], 8) if math.isfinite(row["delta"]) else None]
            for row in rec["lead_rows"]
        ],
        "dcrit": [
            [round(row["L"], 4), round(row["delta"], 12) if math.isfinite(row["delta"]) else None]
            for row in rec["pin_rows"]
        ],
        "margin": laws["verdict"],
        "lead": leads["verdict"],
    }
    if n1 is not None:
        payload["n1_decision"] = n1["laws"]["decision"]
        payload["n1_anchors"] = [
            [want, round(n1["anchors"][want], 18) if math.isfinite(n1["anchors"][want]) else None]
            for want in (0.60, 1.00, 1.40)
        ]
        payload["n1_unconv"] = n1["n_unconv"]
    if n3 is not None:
        payload["n3"] = {
            kind: {
                "alpha": world.get("alpha"),
                "C": world.get("C"),
                "a": world.get("a"),
            }
            for kind, world in n3["worlds"].items()
        }
        payload["n3_reading"] = n3["reading"]
    if n4 is not None:
        payload["n4"] = {
            "max": n4["max"],
            "p99": n4["p99"],
            "frac_lt2": n4["frac_lt2"],
            "b_compress": n4["b_compress"],
        }
    return payload


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    _CL_CACHE.clear()
    _CONN_CACHE.clear()
    wall0 = time.time()

    emit("margin_law_symreg_probe r%d %s" % (ROUND, ADDENDUM))
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    rec = compute(smoke)
    zeros = load_zeros(rec["n_zeros"])
    n1 = compute_n1(zeros, smoke)
    n2 = compute_n2(n1)
    n3 = compute_n3(zeros, smoke)
    n4 = compute_n4(zeros)
    dual_ok = fingerprint_dual(rec, smoke, n1)

    laws = fit_margin_laws(rec)
    leads = fit_lead_laws(rec["lead_rows"])
    pin = fit_pinning(rec, laws)
    result = payload_sha(numeric_payload(rec, laws, leads, pin, n1, n3, n4))

    section("D1  lambda*(L)  ZERO-SIDE SVD + mu*(L) SOURCE")
    emit(
        "  zeros n=%d gamma1=%s gammaN=%s src=%s  N=%d"
        % (
            rec["n_zeros"], fmt(rec["gamma1"], 10), fmt(rec["gammaN"], 6),
            rec["zeros_src"], rec["dimension"],
        )
    )
    emit("  c_L(0.3)=%s" % fmt(rec["cL03"], 12))
    n_rel = sum(1 for row in rec["lam_rows"] if row["reliable"])
    n_floor = sum(1 for row in rec["lam_rows"] if row["floor"])
    for row in rec["lam_rows"]:
        if abs(row["L"] * 100 - round(row["L"] * 100)) > 1.0e-8 and not smoke:
            continue
        if smoke or abs(row["L"] / 0.05 - round(row["L"] / 0.05)) < 1.0e-8 or row["floor"]:
            emit(
                "  L=%s lam=%s svd=%s cond=%s rel=%d floor=%d slep=%s twob=%s widom=%s"
                % (
                    fmt(row["L"], 4), fmt(row["lam"], 10), fmt(row["lam_svd"], 10),
                    fmt(row["cond"], 4), int(row["reliable"]), int(row["floor"]),
                    fmt(row["slep"], 8), fmt(row["twob"], 8), fmt(row["widom"], 8),
                )
            )
    emit(
        "  n_grid=%d n_rel=%d n_floor=%d SVD_floor_L=%s"
        % (len(rec["lam_rows"]), n_rel, n_floor, fmt(rec["floor_L"], 4))
    )
    emit("  L_cross=%s  (r615/r620 ~0.372)" % fmt(rec["L_cross"], 6))
    for row in rec["mu_rows"]:
        if smoke or abs(row["L"] / 0.05 - round(row["L"] / 0.05)) < 1.0e-8:
            emit(
                "  mu L=%s full=%s odd=%s"
                % (fmt(row["L"], 4), fmt(row["mu_full"], 8), fmt(row["mu_odd"], 8))
            )
    check(
        "D1-cL-0.3",
        2.1924049 < rec["cL03"] < 2.1924050,
        "c_L(0.3)=%s" % fmt(rec["cL03"], 10),
    )
    check(
        "D1-lambda-positive-lo",
        any(row["reliable"] and row["lam"] > 0.0 and row["L"] < 0.5 for row in rec["lam_rows"]),
        "n_rel=%d" % n_rel,
    )
    check(
        "D1-floor-reported",
        math.isfinite(rec["floor_L"]) or n_rel == len(rec["lam_rows"]),
        "floor_L=%s" % fmt(rec["floor_L"], 4),
    )
    check(
        "D1-Lcross-window",
        math.isfinite(rec["L_cross"]) and 0.34 <= rec["L_cross"] <= 0.42,
        "L_cross=%s" % fmt(rec["L_cross"], 6),
    )
    emit(
        "  sinc_eig L=0.40  lambda0=%s 1-lam0=%s  outband_slep=%s"
        % (fmt(rec["sinc40_lam0"], 8), fmt(rec["sinc40_leak"], 8), fmt(rec["slep40"], 8))
    )
    leak = rec["sinc40_leak"]
    slep40 = rec["slep40"]
    sinc_rel = (
        abs(slep40 - leak) / max(abs(leak), abs(slep40), 1.0e-30)
        if leak > 1.0e-18 and slep40 > 0.0
        else float("nan")
    )
    check(
        "D1-slepian-crosscheck",
        (not math.isfinite(sinc_rel)) or sinc_rel < 0.8 or leak < 1.0e-12,
        "rel=%s" % fmt(sinc_rel, 4),
    )

    section("D2  LEADS  Delta_j")
    lead_ok = True
    for row in rec["lead_rows"]:
        frozen = row["frozen"]
        delta = row["delta"]
        rel = (
            abs(delta - frozen) / max(abs(frozen), 1.0e-12)
            if math.isfinite(delta) and math.isfinite(frozen) and not math.isinf(delta)
            else float("inf")
        )
        emit(
            "  q=%d L_j=%s Delta=%s frozen=%s rel=%s gap=%s w=%s Omega=%d k=%d"
            % (
                row["q"], fmt(row["L"], 5), fmt(row["delta"], 5),
                fmt(frozen, 5), fmt(rel, 4), fmt(row["gap"], 5),
                fmt(row["w"], 5), row["Omega"], row["k"],
            )
        )
        finite = math.isfinite(delta) and not math.isinf(delta) and delta > 0.0
        if smoke:
            if not finite:
                lead_ok = False
        elif math.isfinite(frozen) and finite:
            if rel > 0.35:
                lead_ok = False
        else:
            lead_ok = False
    check("D2-leads-recomputed", lead_ok, "n=%d" % len(rec["lead_rows"]))

    section("D3  PINNING  delta_crit")
    pin_ok = True
    for row in rec["pin_rows"]:
        emit(
            "  L=%s lam=%s d_crit=%s r615=%s PRIME=%s ratio=%s"
            % (
                fmt(row["L"], 4), fmt(row["lam"], 10), fmt(row["delta"], 6),
                fmt(row["r615"], 6), fmt(row["prime"], 8), fmt(row["ratio"], 4),
            )
        )
        if math.isfinite(row["r615"]) and math.isfinite(row["delta"]) and row["delta"] > 0.0:
            rel = abs(math.log(row["delta"] / row["r615"]))
            if rel > 1.6:
                pin_ok = False
        elif not smoke:
            pin_ok = False
    check("D3-pinning", pin_ok, "n=%d" % len(rec["pin_rows"]))

    section("S1  LAWS  log lambda*(L)")
    emit("  n_rel=%d n_fit=%d n_test=%d" % (laws["n_rel"], laws["n_fit"], laws["n_test"]))
    for law in laws["named"]:
        extra = ""
        if "C" in law:
            extra += " C=%s" % fmt(law["C"], 5)
        if "A" in law:
            extra += " A=%s B=%s" % (fmt(law["A"], 5), fmt(law["B"], 5))
        emit(
            "  %s hold=%s fit=%s aic=%s coeff=%s kind=%s%s"
            % (
                law["name"], fmt(law["hold"], 4), fmt(law["fit"], 4),
                fmt(law["aic"], 4),
                ",".join(fmt(val, 5) for val in law["coeff"]),
                law["kind"], extra,
            )
        )
    emit("  grammar top-3 (depth<=3, OLS, holdout):")
    for law in laws["grammar_top"]:
        emit(
            "    %s hold=%s fit=%s aic=%s coeff=%s kind=%s"
            % (
                law["name"], fmt(law["hold"], 4), fmt(law["fit"], 4),
                fmt(law["aic"], 4),
                ",".join(fmt(val, 5) for val in law["coeff"]),
                law["kind"],
            )
        )
    emit("  closed-form matches (1%%): %s" % (", ".join(laws["matches"]) if laws["matches"] else "none"))
    emit("  S4 all L-laws sampling-theoretic (L, gamma1, N(T) density); lambda* data is zero-side.")
    check("S1-laws-fitted", laws["n_rel"] >= 4, "n_rel=%d" % laws["n_rel"])

    section("S2  LAWS  Delta_j")
    emit("  const=%s loo=%s n=%d" % (fmt(leads["const"], 5), fmt(leads["const_loo"], 4), leads.get("n", 0)))
    for law in leads["top"]:
        emit(
            "  %s loo=%s coeff=%s"
            % (
                law["name"], fmt(law["loo"], 4),
                ",".join(fmt(val, 5) for val in law["coeff"]),
            )
        )
    emit("  %s" % leads["detail"])
    check("S2-lead-laws", leads.get("n", 0) >= 3, leads["verdict"])

    section("S3  delta_crit vs lambda*")
    emit(
        "  slope log d_crit=%s  slope log lambda*=%s  median d*|PRIME|/lam=%s"
        % (fmt(pin["slope_dcrit"], 4), fmt(pin["slope_lam"], 4), fmt(pin["ratio_med"], 4))
    )
    emit("  ratios %s" % ",".join(fmt(val, 4) for val in pin["ratios"]))
    slope_ok = (
        math.isfinite(pin["slope_dcrit"]) and math.isfinite(pin["slope_lam"])
        and pin["slope_dcrit"] * pin["slope_lam"] > 0.0
    )
    ratio_ok = math.isfinite(pin["ratio_med"]) and 0.05 <= pin["ratio_med"] <= 20.0
    check("S3-slope-sign", slope_ok or smoke, "same sign of d log / dL")
    check("S3-ratio-order", ratio_ok or smoke, "ratio=%s" % fmt(pin["ratio_med"], 4))

    section("N1  PRECISION + N-SWEEP  tall QR / mpmath R")
    emit("  N=%s  spaces=%s  L=[%s,%s] step=%s  mp_dps=%d" % (
        ",".join(str(val) for val in n1["ns"]),
        ",".join(n1["spaces"]),
        fmt(L_N1_LO, 2), fmt(L_N1_HI, 2),
        fmt(L_N1_STEP_SMOKE if smoke else L_N1_STEP_FULL, 2),
        MP_DPS,
    ))
    emit("  method=tall_QR(ReF|ImF)+chol(G); never F^H F; mp.svd(R) at selected (L,N<=80)")
    for space in n1["spaces"]:
        emit("  slopes space=%s  band 0.3-0.6 / 0.6-1.0 / 1.0-1.4" % space)
        for n_dim in n1["ns"]:
            slp = n1["slopes"][space][n_dim]
            emit(
                "    N=%d  %s  %s  %s"
                % (n_dim, fmt(slp["b06"], 3), fmt(slp["b10"], 3), fmt(slp["b14"], 3))
            )
    rels = [row["rel"] for row in n1["conv"] if math.isfinite(row["rel"])]
    rels_hi = [
        row["rel"] for row in n1["conv"]
        if row["L"] > FIT_CUT and math.isfinite(row["rel"])
    ]
    n_ok = sum(1 for row in n1["conv"] if row["ok"])
    emit(
        "  conv N=%d→%d  n_ok=%d/%d  med_rel=%s  med_rel(L>1)=%s"
        % (
            n1["ns"][-2] if len(n1["ns"]) >= 2 else n1["ns"][-1],
            n1["ns"][-1],
            n_ok, len(n1["conv"]),
            fmt(float(np.median(rels)) if rels else float("nan"), 3),
            fmt(float(np.median(rels_hi)) if rels_hi else float("nan"), 3),
        )
    )
    emit(
        "  lam* N=%d  L=0.60:%s  L=1.00:%s  L=1.40:%s"
        % (
            n1["ns"][-1],
            fmt(n1["anchors"][0.60], 6),
            fmt(n1["anchors"][1.00], 6),
            fmt(n1["anchors"][1.40], 6),
        )
    )
    n1_laws = n1["laws"]
    emit("  n_fit=%d n_test=%d  %s" % (
        n1_laws.get("n_fit", 0), n1_laws.get("n_test", 0), n1_laws.get("reason", ""),
    ))
    for law in n1_laws.get("named", []):
        extra = ""
        if "C" in law:
            extra += " C=%s" % fmt(law["C"], 4)
        if "a" in law:
            extra += " a=%s" % fmt(law["a"], 4)
        emit(
            "    %s hold=%s fit=%s%s"
            % (law["name"], fmt(law["hold"], 3), fmt(law["fit"], 3), extra)
        )
    desc = n1_laws.get("desc") or {}
    if desc:
        emit(
            "  desc L<=1 conv  C=%s  a=%s  n=%d  (no holdout; test band N-limited)"
            % (fmt(desc.get("C", float("nan")), 4), fmt(desc.get("a", float("nan")), 4), int(desc.get("n", 0)))
        )
    emit("  N1 DECISION %s" % n1_laws["decision"])
    check(
        "N1-tables-present",
        bool(n1["table"]) and all(n1["slopes"][n1["spaces"][0]][n_dim] for n_dim in n1["ns"]),
        "spaces=%d N=%d" % (len(n1["spaces"]), len(n1["ns"])),
    )
    check(
        "N1-decision-set",
        n1_laws["decision"].split("(")[0] in (
            "SLEPIAN_LINEAR", "QUADRATIC", "OTHER", "N_LIMITED_ARTIFACT",
        ),
        n1_laws["decision"],
    )

    section("N2  NULLING COUNT  |hat|^2 < 1e-3 max")
    n_max = n1["ns"][-1]
    n2_hi = [row for row in n2 if row["N"] == n_max]
    for row in n2_hi:
        if smoke or abs(row["L"] / 0.20 - round(row["L"] / 0.20)) < 1.0e-8:
            emit("  L=%s N=%d n_null=%d / %d" % (
                fmt(row["L"], 4), row["N"], row["n_null"], row["n_zeros"],
            ))
    emit("  vs N at L=1.00:")
    for n_dim in n1["ns"]:
        row = min(
            (item for item in n2 if item["N"] == n_dim),
            key=lambda item: abs(item["L"] - 1.00),
            default=None,
        )
        if row is not None:
            emit("    N=%d L=%s n_null=%d" % (n_dim, fmt(row["L"], 4), row["n_null"]))
    check(
        "N2-counts",
        all(row["n_null"] >= 0 for row in n2) and len(n2) > 0,
        "n=%d" % len(n2),
    )

    section("N3  SYNTHETIC CONTROLS  (flat gap = spacing 2π/log γ₁)")
    emit("  2γ1=%s  γ1^2/π=%s" % (fmt(TWO_GAMMA1, 4), fmt(GAMMA1 * GAMMA1 / math.pi, 4)))
    emit("  world            alpha(-αL+½logL+c)     C(-CL²+bL+c)      a(-a L log L)")
    for kind, world in n3["worlds"].items():
        emit(
            "  %-14s  α=%s  C=%s  a=%s  n=%d  %s"
            % (
                kind, fmt(world.get("alpha", float("nan")), 4),
                fmt(world.get("C", float("nan")), 4),
                fmt(world.get("a", float("nan")), 4),
                int(world.get("n", 0)),
                world.get("decision", ""),
            )
        )
    emit("  reading %s" % n3["reading"])
    check(
        "N3-completed",
        len(n3["worlds"]) == 5 and all(
            math.isfinite(world.get("alpha", float("nan"))) or smoke
            for world in n3["worlds"].values()
        ),
        n3["reading"],
    )

    section("N4  dBN GAP FUNCTIONAL  |j-k|<=2000 + density tail")
    emit(
        "  n=%d  max=%s  p99=%s  frac(B<2)=%s  median=%s"
        % (
            n4["n"], fmt(n4["max"], 4), fmt(n4["p99"], 4),
            fmt(n4["frac_lt2"], 4), fmt(n4["median"], 4),
        )
    )
    emit(
        "  compress gap×0.3 at k=%d  B_mid=%s  B_comp=%s"
        % (n4["k_mid"], fmt(n4["b_mid"], 4), fmt(n4["b_compress"], 4))
    )
    check(
        "N4-finite",
        n4["n"] > 0 and math.isfinite(n4["max"]) and math.isfinite(n4["b_compress"]),
        "n=%d" % n4["n"],
    )

    section("SEAL")
    check("dual-run", dual_ok, "identical" if dual_ok else "recompute mismatch")
    wall = time.time() - wall0
    wall_lim = SMOKE_WALL if smoke else FULL_WALL
    check("wall-time", wall <= wall_lim, "wall_s=%s lim=%s" % (fmt(wall, 3), fmt(wall_lim, 1)))

    n1_dec = n1_laws["decision"]
    verdict = n1_dec
    quad = laws["quad"]
    n1_best = n1_laws.get("best") or {}
    test_band = [row for row in n1["conv"] if row["L"] > FIT_CUT]
    n_test_ok = sum(1 for row in test_band if row["ok"])

    def _n2_at(ell: float, n_dim: int) -> int:
        cands = [row for row in n2 if row["N"] == n_dim]
        if not cands:
            return -1
        return min(cands, key=lambda item, w=ell: abs(item["L"] - w))["n_null"]

    state_body = [
        "STATE r%d %s %s" % (ROUND, CONTRACT, ADDENDUM),
        "SHA %s" % file_sha256(),
        "SPEC %s" % SPEC_SHA,
        "RESULT %s" % result,
        "GATES PLACEHOLDER",
        "VERDICT %s" % verdict,
        "N1 slopes damped 0.3-0.6/0.6-1.0/1.0-1.4 " + " ".join(
            "N%d:%s/%s/%s" % (
                n_dim,
                fmt(n1["slopes"]["damped"][n_dim]["b06"], 2),
                fmt(n1["slopes"]["damped"][n_dim]["b10"], 2),
                fmt(n1["slopes"]["damped"][n_dim]["b14"], 2),
            )
            for n_dim in n1["ns"]
        ),
    ]
    if "plain" in n1["slopes"]:
        state_body.append("N1 slopes plain " + " ".join(
            "N%d:%s/%s/%s" % (
                n_dim,
                fmt(n1["slopes"]["plain"][n_dim]["b06"], 2),
                fmt(n1["slopes"]["plain"][n_dim]["b10"], 2),
                fmt(n1["slopes"]["plain"][n_dim]["b14"], 2),
            )
            for n_dim in n1["ns"]
        ))
    state_body.extend([
        "N1 conv120→160 n_ok=%d/%d L>1 ok=%d/%d med_rel=%s"
        % (
            n_ok, len(n1["conv"]), n_test_ok, len(test_band),
            fmt(float(np.median(rels)) if rels else float("nan"), 3),
        ),
        "N1 lam*(0.6/1.0/1.4)=%s/%s/%s"
        % (
            fmt(n1["anchors"][0.60], 4),
            fmt(n1["anchors"][1.00], 4),
            fmt(n1["anchors"][1.40], 4),
        ),
        "N1 law %s hold=%s C/a(L<=1)=%s/%s"
        % (
            n1_best.get("name", n1_dec),
            fmt(n1_best.get("hold", float("nan")), 3),
            fmt((n1_laws.get("desc") or {}).get("C", n1_best.get("C", float("nan"))), 3),
            fmt((n1_laws.get("desc") or {}).get("a", n1_best.get("a", float("nan"))), 3),
        ),
        "N1 DECISION %s  2γ1=%s γ1²/π=%s" % (
            n1_dec, fmt(TWO_GAMMA1, 3), fmt(GAMMA1 * GAMMA1 / math.pi, 3),
        ),
        "N2 null N=%d L=0.6/1.0/1.4 %d/%d/%d  vsN@L=1 %s"
        % (
            n_max,
            _n2_at(0.60, n_max), _n2_at(1.00, n_max), _n2_at(1.40, n_max),
            " ".join("N%d:%d" % (n_dim, _n2_at(1.00, n_dim)) for n_dim in n1["ns"]),
        ),
        "N3 α true/flat/W10/W20/f20=%s/%s/%s/%s/%s"
        % tuple(
            fmt(n3["worlds"][kind].get("alpha", float("nan")), 3)
            for kind in ("true", "flat_gap", "scale_W10", "scale_W20", "first_to_20")
        ),
        "N3 C  true/flat/W10/W20/f20=%s/%s/%s/%s/%s"
        % tuple(
            fmt(n3["worlds"][kind].get("C", float("nan")), 3)
            for kind in ("true", "flat_gap", "scale_W10", "scale_W20", "first_to_20")
        ),
        "N3 reading %s" % n3["reading"],
        "N4 max=%s p99=%s frac<2=%s Bmid=%s B×0.3=%s"
        % (
            fmt(n4["max"], 3), fmt(n4["p99"], 3), fmt(n4["frac_lt2"], 3),
            fmt(n4["b_mid"], 3), fmt(n4["b_compress"], 3),
        ),
        "r630 L_cross=%s SVD_floor=%s n_rel=%d %s %s"
        % (
            fmt(rec["L_cross"], 5), fmt(rec["floor_L"], 4), laws["n_rel"],
            laws["verdict"], leads["verdict"],
        ),
        "r630 quad C=%s hold=%s"
        % (fmt(quad.get("C", float("nan")), 3), fmt(quad["hold"], 3)),
        "FENCE %s" % FENCE,
        "END_STATE",
    ])
    n_state = len(state_body)
    check("STATE-le-40", n_state <= 40, "n=%d" % n_state)

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    state_body[4] = "GATES %d/%d smoke=%d wall_s=%s" % (
        n_pass, n_gate, int(smoke), fmt(wall, 3),
    )
    emit("VERDICT %s" % verdict)
    emit("WHY %s | %s" % (laws["detail"], leads["detail"]))
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % result)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("FENCE %s" % FENCE)

    section("STATE")
    for line in state_body:
        emit(line)
    emit("STATE_LINES %d" % n_state)
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r630b window-margin law (N-sweep / synthetics; experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
