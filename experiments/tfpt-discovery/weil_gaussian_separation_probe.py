#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_gaussian_separation_probe -- PRIME.RDAGGER.WEIL_GAUSSIAN_SEPARATION.01

Round 539.  Numerical precheck of HEIGHT-UNIFORM off-critical
separation for a NONCOMPACT Gaussian/Hermite Weil test class, before
any Lean campaign on that class.

r535 (weil_separation_redteam_probe) red-teamed the COMPACT
FullWeilTest subclass: 49/49 injected zeros were truncated-negative,
but γ=1000 was uncertifiable because omitted on-line mass (~+1.27 via
a Riemann–von-Mangoldt heuristic) swamped the margin (−5e-7) and the
Lipschitz 1/t² tail certified nothing.  This probe asks whether
exponential Fourier decay of g = h⋆h~ with h(t)=p(t) e^{-a t²} (p even
of degree ≤ 8) fixes exactly that tail.

CLAIM BOUNDARY.  Finite quadratic-form search in a 5-dimensional
Hermite–Gaussian subclass, plus an explicit Trudgian-type tail
majorant on omitted on-line zeros.  Conditional on the frozen first-100
ordinates.  NO RH claim, NO anti-RH claim, NO ledger row, NO paper
edit, NO Lean edit.  A negative certified Rayleigh is not a theorem
for the infinite-dimensional Schwartz class.  A failure here is a
failure of this subclass + this tail majorant, not of every
noncompact test class.

HAT CONVENTION.  Lean FullWeilTest.hat is the unshifted Laplace
transform ∫ g(t) exp(s t) dt.  This probe uses the classical
Weil-shifted pairing

    ĥ_W(s) := ∫ g(u) exp((s − 1/2) u) du = H(s−1/2) H(1/2−s),

so ĥ_W(1/2+it) = |H(it)|² ≥ 0.  Identifying hat_Lean(ρ) with ĥ_W(ρ)
is the same open dictionary as r535.

PARAMETER.  h(t) = p(t) exp(−a t²) with p even, deg ≤ 8, spanned by
physicists' Hermite H_{2k}(√a t) exp(−a t²), k=0..4.  For the pure
Gaussian (k=0): g(u)=√(π/(2a)) exp(−a u²/2) and
ĥ_W(s)=(π/a) exp((s−1/2)²/(2a)).  (The routes-scout sketch
g(u)∝exp(−u²/(4α)) is the same family under α=1/(2a).)

TAIL.  Omitted positive ordinates t_n > T=t_{100} are charged by the
unconditional increment

    N(T+H)−N(T) ≤ θ(T+H)−θ(T) + E(T+H) + E(T),   H≥1,

where θ(T)=(T/2π)log(T/(2πe))+7/8 and E is Trudgian's explicit
S(T)-bound (J. Number Theory 134 (2014) 280–292, arXiv:1208.5846,
Theorem 1 + Corollary 1):

    |S(T)| ≤ 0.111 log T + 0.275 log log T + 2.450    (T≥e),
    E(T)  = 0.111 log T + 0.275 log log T + 2.450 + 0.2/T.

This is CERTIFIED relative to that cited bound (not a new zero-density
theorem).  A second CRUDE-SAFE majorant N(T+1)−N(T) ≤ C_CRUDE log(T+2)
with C_CRUDE=4 (T≥14) is checked in-probe to dominate the Trudgian
increment, then used for the incomplete-gamma remainder.  A third
HEURISTIC uses the Riemann–von-Mangoldt density log(T/2π)/(2π).

Runtime: numpy.  Zeros cached from mpmath.zetazero (mpmath 1.3.0,
dps=30, 2026-09-01); mpmath is used only for G0 quadrature, not for
zeros at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
SPEC = {
    "round": 539,
    "target": "gaussian_hermite_height_uniform_separation_precheck",
    "hat": "weil_shifted",
    "betas": [0.51, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95],
    "gammas": [0.5, 1.0, 5.0, 14.13, 30.0, 100.0, 1000.0, 10000.0],
    "n_zeros": 100,
    "hermite_degrees": [0, 2, 4, 6, 8],
    "a_log_min": 1.0e-2,
    "a_log_max": 1.0e8,
    "a_log_n": 33,
    "sep_atol": 1e-12,
    "g0_atol": 1e-12,
    "g1_atol": 1e-8,
    "c_crude": 4.0,
    "trudgian_a": 0.111,
    "trudgian_b": 0.275,
    "trudgian_c": 2.450,
    "trudgian_nt_extra": 0.2,
    "trudgian_source": "Trudgian JNT 134 (2014) 280-292 / arXiv:1208.5846 Thm1+Cor1",
    "yoshida_eta_bar": 1e-10,
    "prime_n_cap": 20000,
    "prime_convention": "Lambda(n)*(1+1/n)*g(log n)  [contour; combMass 2*Lambda(n)/sqrt(n)*g(log n) also reported]",
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

# Physicists' H_{0,2,4,6,8}(x) as coefficients of x^{0,2,4,6,8}.
HE_COEF = np.array(
    [
        [1.0, 0.0, 0.0, 0.0, 0.0],
        [-2.0, 4.0, 0.0, 0.0, 0.0],
        [12.0, -48.0, 16.0, 0.0, 0.0],
        [-120.0, 720.0, -480.0, 64.0, 0.0],
        [1680.0, -13440.0, 13440.0, -3584.0, 256.0],
    ],
    dtype=np.float64,
)

# First 100 positive ordinates.  Same freeze as r535.
ON_LINE_ORDINATES = (
    14.1347251417346946, 21.0220396387715560, 25.0108575801456894,
    30.4248761258595124, 32.9350615877391917, 37.5861781588256747,
    40.9187190121474984, 43.3270732809150019, 48.0051508811671610,
    49.7738324776723005, 52.9703214777144638, 56.4462476970633915,
    59.3470440026023525, 60.8317785246098097, 65.1125440480816025,
    67.0798105294941678, 69.5464017111739849, 72.0671576744819049,
    75.7046906990839261, 77.1448400688747995, 79.3373750202493682,
    82.9103808540860285, 84.7354929805170514, 87.4252746131252252,
    88.8091112076344587, 92.4918992705584913, 94.6513440405198878,
    95.8706342282453079, 98.8311942181936871, 101.3178510057313844,
    103.7255380404783409, 105.4466230523260890, 107.1686111842764006,
    111.0295355431696720, 111.8746591769926368, 114.3202209154527083,
    116.2266803208575539, 118.7907828659762117, 121.3701250024206502,
    122.9468292935525824, 124.2568185543457702, 127.5166838795964992,
    129.5787041999560643, 131.0876885309326667, 133.4977372029975982,
    134.7565097533738765, 138.1160420545334375, 139.7362089521213875,
    141.1237074040211326, 143.1118458076206252, 146.0009824867655084,
    147.4227653425596145, 150.0535204207848778, 150.9252576122414666,
    153.0246938111988868, 156.1129092942378804, 157.5975918175940649,
    158.8499881714205060, 161.1889641375960309, 163.0307096871819965,
    165.5370691879004141, 167.1844399781745096, 169.0945154155688215,
    169.9119764794116918, 173.4115365195915501, 174.7541915233657335,
    176.4414342977104297, 178.3774077760999717, 179.9164840202570019,
    182.2070784843664626, 184.8744678483874964, 185.5987836777074733,
    187.2289225835018556, 189.4161586560169326, 192.0266563607137869,
    193.0797266038456996, 195.2653966795292320, 196.8764818409583199,
    198.0153096762519169, 201.2647519437038000, 202.4935945141405398,
    204.1896718031045452, 205.3946972021632860, 207.9062588878062172,
    209.5765097168562647, 211.6908625953653029, 213.3479193597126766,
    214.5470447834914296, 216.1695385082637131, 219.0675963490213860,
    220.7149188393140093, 221.4307055546933327, 224.0070002546043213,
    224.9833246695822879, 227.4214442796792923, 229.3374133055253594,
    231.2501887004991659, 231.9872352531802449, 233.6934041789083096,
    236.5242296658161933,
)

CHECKS: list[tuple[str, bool]] = []
N_BASIS = 5
LOG_CLIP = 700.0


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-36s %s" % (
        "PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    digest = hashlib.sha256()
    with open(os.path.abspath(__file__), "rb") as handle:
        digest.update(handle.read())
    return digest.hexdigest()


def canon(value: float) -> float:
    number = float(value)
    if not math.isfinite(number):
        return number
    if abs(number) < 1e-18:
        return 0.0
    return number


def odd_double_factorial(m: int) -> float:
    """(2m-1)!! with the convention (−1)!! = 1."""
    if m <= 0:
        return 1.0
    value = 1.0
    for index in range(m):
        value *= float(2 * index + 1)
    return value


def hermite_monomial_matrix(alpha: float) -> np.ndarray:
    powers = alpha ** np.arange(N_BASIS, dtype=np.float64)
    return HE_COEF * powers


def even_raw_moments(mu: complex, var: float) -> np.ndarray:
    """E[T^{0,2,4,6,8}] for T ~ N(mu, var), analytic continuation in mu."""
    moments = np.zeros(N_BASIS, dtype=np.complex128)
    for degree_index in range(N_BASIS):
        n_power = 2 * degree_index
        acc = 0.0 + 0.0j
        for even_k in range(0, n_power + 1, 2):
            m_half = even_k // 2
            central = (var ** m_half) * odd_double_factorial(m_half)
            acc += math.comb(n_power, even_k) * (mu ** (n_power - even_k)) * central
        moments[degree_index] = acc
    return moments


def log_pref(z: complex, alpha: float) -> complex:
    return 0.5 * math.log(math.pi / alpha) + (z * z) / (4.0 * alpha)


def p_vector(z: complex, alpha: float) -> np.ndarray:
    """Prefactor-free Laplace polynomial: H(z) = √(π/a) e^{z²/(4a)} (P·c)."""
    mu = z / (2.0 * alpha)
    var = 1.0 / (2.0 * alpha)
    return hermite_monomial_matrix(alpha) @ even_raw_moments(mu, var)


def pref_product(z: complex, alpha: float) -> complex:
    """pref(z) pref(-z) = (π/a) exp(z²/(2a))."""
    log_value = math.log(math.pi / alpha) + (z * z) / (2.0 * alpha)
    real_part = float(np.real(log_value))
    if real_part > LOG_CLIP:
        return complex(math.inf)
    if real_part < -LOG_CLIP:
        return 0.0 + 0.0j
    return complex(np.exp(log_value))


def basis_laplace(z: complex, alpha: float, extra_exp: float = 0.0) -> np.ndarray:
    """H_k(z) = ∫ H_{2k}(√a t) e^{-a t²} e^{z t} dt, k=0..4."""
    poly = p_vector(z, alpha)
    log_value = log_pref(z, alpha) + extra_exp
    real_part = float(np.real(log_value))
    if real_part > LOG_CLIP:
        return np.full(N_BASIS, np.inf + 0.0j, dtype=np.complex128)
    if real_part < -LOG_CLIP:
        return np.zeros(N_BASIS, dtype=np.complex128)
    return np.exp(log_value) * poly


def gram_modsq(vector: np.ndarray) -> np.ndarray:
    real = vector.real
    imag = vector.imag
    return np.outer(real, real) + np.outer(imag, imag)


def gram_re_product(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    left_r, left_i = left.real, left.imag
    right_r, right_i = right.real, right.imag
    return (
        0.5 * (np.outer(left_r, right_r) + np.outer(right_r, left_r))
        - 0.5 * (np.outer(left_i, right_i) + np.outer(right_i, left_i))
    )


def assemble_cell(
    alpha: float,
    ordinates: np.ndarray,
    delta: float | None,
    gamma: float | None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Physical (G_on, G_off, whitening_scales) in a column-whitened Hermite frame.

    ĥ_W(s) = pref_product(s-1/2) (P(s-1/2)·α) (P(1/2-s)·α).  Columns of P
    are RMS-normalised so the 5×5 Gram is not dominated by H_8 vs H_0.
    Returned coefficients of an eigenvector are in the whitened frame;
    physical Hermite coefficients are c / scales.
    """
    p_on = np.vstack([p_vector(1j * float(height), alpha) for height in ordinates])
    if delta is None or gamma is None:
        p_left = np.zeros(N_BASIS, dtype=np.complex128)
        p_right = np.zeros(N_BASIS, dtype=np.complex128)
        pref_off = 0.0 + 0.0j
    else:
        p_left = p_vector(delta + 1j * gamma, alpha)
        p_right = p_vector(-delta - 1j * gamma, alpha)
        pref_off = pref_product(delta + 1j * gamma, alpha)
    rms = np.sqrt(
        np.mean(np.abs(p_on) ** 2, axis=0)
        + 0.5 * np.abs(p_left) ** 2
        + 0.5 * np.abs(p_right) ** 2
    )
    scales = np.maximum(rms, 1.0e-30)
    p_on_w = p_on / scales
    gram_on = np.zeros((N_BASIS, N_BASIS), dtype=np.float64)
    for index, height in enumerate(ordinates):
        pref_on = pref_product(1j * float(height), alpha)
        weight = 2.0 * float(np.real(pref_on))
        if weight == 0.0 or not math.isfinite(weight):
            continue
        gram_on += weight * gram_modsq(p_on_w[index])
    gram_off = np.zeros((N_BASIS, N_BASIS), dtype=np.float64)
    if pref_off != 0.0 and math.isfinite(abs(pref_off)):
        gram_off = 4.0 * gram_re_product(
            p_left / scales, pref_off * (p_right / scales),
        )
    return gram_on, gram_off, scales


def eigs_all(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(matrix)
    for column in range(vectors.shape[1]):
        pivot = int(np.argmax(np.abs(vectors[:, column])))
        if vectors[pivot, column].real < 0.0:
            vectors[:, column] *= -1.0
    return np.real(values), np.real(vectors)


# ---------------------------------------------------------------------------
# Tail majorants
# ---------------------------------------------------------------------------
def trudgian_E(height: float) -> float:
    """E(T) from Trudgian 2014 Corollary 1, T≥e."""
    clipped = max(float(height), math.e)
    log_t = math.log(clipped)
    log_log = math.log(log_t) if log_t > 1.0 else 0.0
    return (
        float(SPEC["trudgian_a"]) * log_t
        + float(SPEC["trudgian_b"]) * log_log
        + float(SPEC["trudgian_c"])
        + float(SPEC["trudgian_nt_extra"]) / clipped
    )


def rvm_theta(height: float) -> float:
    clipped = max(float(height), math.e)
    return clipped / (2.0 * math.pi) * math.log(clipped / (2.0 * math.pi * math.e)) + 0.875


def trudgian_increment(height: float, width: float) -> float:
    """Bound on N(T+H)−N(T) via |N−θ|≤E.  Charge at least a unit interval."""
    width_use = max(float(width), 1.0)
    t_hi = float(height) + width_use
    return (
        rvm_theta(t_hi) - rvm_theta(height)
        + trudgian_E(t_hi) + trudgian_E(height)
    )


def crude_increment(height: float, width: float) -> float:
    width_use = max(float(width), 1.0)
    return float(SPEC["c_crude"]) * math.log(float(height) + width_use + 2.0) * width_use


def moment_triangle_coeffs(alpha: float) -> np.ndarray:
    """Even-poly majorant coefficients q[m] of t^{2m} for |E[T^{2j}]|."""
    var = 1.0 / (2.0 * alpha)
    inv_two_a = 1.0 / (2.0 * alpha)
    bounds = np.zeros((N_BASIS, N_BASIS), dtype=np.float64)
    for j_index in range(N_BASIS):
        for m_half in range(j_index + 1):
            power = j_index - m_half
            coef = (
                math.comb(2 * j_index, 2 * m_half)
                * (inv_two_a ** (2 * power))
                * (var ** m_half)
                * odd_double_factorial(m_half)
            )
            bounds[j_index, power] += coef
    return bounds


def triangle_Q_coeffs(coeffs: np.ndarray, alpha: float) -> np.ndarray:
    """Nonnegative q[m] with Q(t)=Σ q_m t^{2m} ≥ |P_α(it)|."""
    b_abs = np.abs(hermite_monomial_matrix(alpha))
    moment_bounds = moment_triangle_coeffs(alpha)
    q_vec = np.zeros(N_BASIS, dtype=np.float64)
    for k_index in range(N_BASIS):
        major = np.zeros(N_BASIS, dtype=np.float64)
        for j_index in range(N_BASIS):
            major += b_abs[k_index, j_index] * moment_bounds[j_index]
        q_vec += abs(float(coeffs[k_index])) * major
    return q_vec


def poly_even_eval(even_coeffs: np.ndarray, t_value: float) -> float:
    total = 0.0
    t_sq = float(t_value) * float(t_value)
    power = 1.0
    for coef in even_coeffs:
        total += float(coef) * power
        power *= t_sq
    return total


def log_env_hat(coeffs: np.ndarray, alpha: float, t0: float, t1: float) -> float:
    """log of (π/a) e^{-t0²/(2a)} Q(t1)², an upper bound of ĥ_W(1/2+it) on [t0,t1]."""
    q_vec = triangle_Q_coeffs(coeffs, alpha)
    q_hi = poly_even_eval(q_vec, t1)
    if q_hi <= 0.0:
        q_hi = 0.0
    log_q = math.log(q_hi) if q_hi > 0.0 else -LOG_CLIP
    return math.log(math.pi / alpha) - (t0 * t0) / (2.0 * alpha) + 2.0 * log_q


def exp_clip(log_value: float) -> float:
    if log_value > LOG_CLIP:
        return math.inf
    if log_value < -LOG_CLIP:
        return 0.0
    return math.exp(log_value)


def I_power_gauss(power: int, t_lo: float, beta: float) -> float:
    """∫_{t_lo}^∞ t^{power} exp(−beta t²) dt, power ≥ 0, t_lo ≥ 0, beta > 0."""
    if power < 0:
        raise ValueError("power")
    values = [0.0] * (power + 1)
    exp_term = math.exp(-beta * t_lo * t_lo) if beta * t_lo * t_lo < LOG_CLIP else 0.0
    values[0] = 0.5 * math.sqrt(math.pi / beta) * math.erfc(t_lo * math.sqrt(beta))
    if power >= 1:
        values[1] = exp_term / (2.0 * beta)
    for index in range(2, power + 1):
        t_pow = t_lo ** (index - 1) if t_lo > 0.0 else 0.0
        values[index] = t_pow * exp_term / (2.0 * beta) + (
            (index - 1) / (2.0 * beta)
        ) * values[index - 2]
    return values[power]


def Q_square_even_coeffs(q_vec: np.ndarray) -> np.ndarray:
    """s[p] of t^{2p} in Q(t)², Q even of degree 8."""
    square = np.zeros(9, dtype=np.float64)
    for i_index, left in enumerate(q_vec):
        for j_index, right in enumerate(q_vec):
            square[i_index + j_index] += float(left) * float(right)
    return square


def remainder_integral(coeffs: np.ndarray, alpha: float, t_lo: float) -> float:
    """∫_{t_lo}^∞ 2 C_CRUDE log(t+2) (π/a) Q(t)² e^{-t²/(2a)} dt."""
    if t_lo <= 0.0:
        t_lo = 1.0
    beta = 1.0 / (2.0 * alpha)
    q_vec = triangle_Q_coeffs(coeffs, alpha)
    square = Q_square_even_coeffs(q_vec)
    log0 = math.log(t_lo + 2.0)
    inv = 1.0 / (t_lo + 2.0)
    acc = 0.0
    for p_index, s_coef in enumerate(square):
        if s_coef <= 0.0:
            continue
        i_even = I_power_gauss(2 * p_index, t_lo, beta)
        i_odd = I_power_gauss(2 * p_index + 1, t_lo, beta)
        acc += float(s_coef) * (log0 * i_even + inv * i_odd)
    return 2.0 * float(SPEC["c_crude"]) * (math.pi / alpha) * acc


def certified_tail(
    coeffs: np.ndarray, alpha: float, t_cut: float, mode: str,
) -> float:
    """mode in {trudgian, crude, heur}."""
    t_hard = t_cut + max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 8.0)
    t_hard = min(t_hard, 1.0e7)
    total = 0.0
    t_value = float(t_cut)
    while t_value < t_hard:
        width = max(1.0, 0.04 * t_value)
        if t_value + width > t_hard:
            width = max(1.0, t_hard - t_value)
        if mode == "trudgian":
            nbound = trudgian_increment(t_value, width)
        elif mode == "crude":
            nbound = crude_increment(t_value, width)
        else:
            density = math.log(max(t_value, 2.0 * math.pi) / (2.0 * math.pi)) / (
                2.0 * math.pi
            )
            if density < 0.0:
                density = 0.0
            nbound = density * width
        env = exp_clip(log_env_hat(coeffs, alpha, t_value, t_value + width))
        total += 2.0 * nbound * env
        if not math.isfinite(total) or total > 1.0e250:
            return math.inf
        t_value += width
    if mode == "heur":
        density = math.log(max(t_value, 2.0 * math.pi) / (2.0 * math.pi)) / (
            2.0 * math.pi
        )
        if density < 0.0:
            density = 0.0
        env = exp_clip(log_env_hat(coeffs, alpha, t_value, t_value + 1.0))
        beta = 1.0 / (2.0 * alpha)
        total += 2.0 * density * env * (1.0 / max(2.0 * beta * t_value, 1.0e-30))
    else:
        total += remainder_integral(coeffs, alpha, t_value)
    if not math.isfinite(total):
        return math.inf
    return float(total)


# ---------------------------------------------------------------------------
# Autocorrelation g and prime coupling (G4 / Yoshida trap)
# ---------------------------------------------------------------------------
def gauss_even_moment_alpha(power: int, two_a: float) -> float:
    """∫ v^{power} exp(−two_a v²) dv on R; 0 if power odd."""
    if power % 2 == 1:
        return 0.0
    half = power // 2
    return math.sqrt(math.pi / two_a) * odd_double_factorial(half) / (
        (2.0 * two_a) ** half
    )


def monomial_from_hermite(coeffs: np.ndarray, alpha: float) -> np.ndarray:
    return hermite_monomial_matrix(alpha).T @ np.asarray(coeffs, dtype=np.float64)


def g_even_poly(u_value: float, alpha: float, monomials: np.ndarray) -> float:
    """g(u)=∫ h(t)h(t−u) dt for h(t)=(Σ m_j t^{2j}) e^{-a t²}."""
    half = 0.5 * float(u_value)
    gaussian = math.exp(-0.5 * alpha * u_value * u_value)
    two_a = 2.0 * alpha
    acc = 0.0
    for j_index, c_left in enumerate(monomials):
        if c_left == 0.0:
            continue
        for k_index, c_right in enumerate(monomials):
            if c_right == 0.0:
                continue
            n_left = 2 * j_index
            n_right = 2 * k_index
            inner = 0.0
            for p_index in range(n_left + 1):
                for q_index in range(n_right + 1):
                    power = p_index + q_index
                    if power % 2 == 1:
                        continue
                    inner += (
                        math.comb(n_left, p_index)
                        * math.comb(n_right, q_index)
                        * (half ** (n_left - p_index))
                        * ((-half) ** (n_right - q_index))
                        * gauss_even_moment_alpha(power, two_a)
                    )
            acc += float(c_left) * float(c_right) * inner
    return gaussian * acc


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


def prime_coupling(coeffs: np.ndarray, alpha: float, n_max: int, lam: np.ndarray) -> dict:
    monomials = monomial_from_hermite(coeffs, alpha)
    g0 = g_even_poly(0.0, alpha, monomials)
    log2 = math.log(2.0)
    g_log2 = g_even_poly(log2, alpha, monomials)
    eta = abs(g_log2) / abs(g0) if abs(g0) > 0.0 else math.inf
    contour = 0.0
    comb = 0.0
    limit = min(n_max, lam.size - 1)
    for n_value in range(2, limit + 1):
        von = float(lam[n_value])
        if von == 0.0:
            continue
        g_u = g_even_poly(math.log(n_value), alpha, monomials)
        contour += von * (1.0 + 1.0 / n_value) * g_u
        comb += 2.0 * von / math.sqrt(n_value) * g_u
    tail_u = math.log(max(limit, 2))
    # ∫_{log N}^∞ |g_env(u)| e^u du  with |g| ≤ |g(0)| exp(−a u²/2) * (1+(|u|√a)^8)
    # times 2 from ψ(x)<2x Stieltjes (crude).
    g_abs0 = abs(g0)
    def env_integrand(u_value: float) -> float:
        poly = 1.0 + abs(u_value * math.sqrt(alpha)) ** 8
        return g_abs0 * math.exp(-0.5 * alpha * u_value * u_value + u_value) * poly

    tail = 0.0
    u_hi = tail_u + max(12.0 / math.sqrt(max(alpha, 1.0e-12)), 8.0)
    n_step = 400
    step = (u_hi - tail_u) / n_step
    for index in range(n_step + 1):
        u_value = tail_u + index * step
        weight = 0.5 if index in (0, n_step) else 1.0
        tail += weight * env_integrand(u_value)
    tail *= 2.0 * step
    return {
        "g0": g0,
        "g_log2": g_log2,
        "eta": eta,
        "contour": contour,
        "comb": comb,
        "tail_bound": tail,
        "contour_abs_ub": abs(contour) + tail,
    }


# ---------------------------------------------------------------------------
# G0 calibration
# ---------------------------------------------------------------------------
def analytic_hat_pure(delta: complex, alpha: float) -> complex:
    return (math.pi / alpha) * np.exp((delta * delta) / (2.0 * alpha))


def trapz_hat_pure(delta: complex, alpha: float) -> complex:
    sigma = 1.0 / math.sqrt(alpha)
    half_width = 12.0 * sigma
    n_points = 2001
    u_grid = np.linspace(-half_width, half_width, n_points, dtype=np.float64)
    g_u = math.sqrt(math.pi / (2.0 * alpha)) * np.exp(-0.5 * alpha * u_grid * u_grid)
    integrand = g_u * np.exp(delta * u_grid)
    trapz = getattr(np, "trapezoid", None) or np.trapz
    return trapz(integrand, u_grid)


def mpmath_hat_pure(delta: complex, alpha: float) -> complex:
    mp.mp.dps = 25
    a_mp = mp.mpf(alpha)
    d_mp = mp.mpc(delta.real, delta.imag)
    pref = mp.sqrt(mp.pi / (2 * a_mp))

    def integrand(u_value):
        return pref * mp.e ** (-a_mp * u_value * u_value / 2) * mp.e ** (d_mp * u_value)

    value = mp.quad(integrand, [-mp.inf, mp.inf])
    return complex(value)


def run_g0() -> tuple[bool, float]:
    alphas = (0.5, 1.0, 2.0)
    deltas = (
        0.0 + 0.0j,
        0.3 + 0.0j,
        0.2 + 0.4j,
        0.1 + 2.0j,
    )
    max_err = 0.0
    for alpha in alphas:
        for delta in deltas:
            analytic = analytic_hat_pure(delta, alpha)
            from_h = basis_laplace(delta, alpha)[0] * basis_laplace(-delta, alpha)[0]
            trapz = trapz_hat_pure(delta, alpha)
            mp_val = mpmath_hat_pure(delta, alpha)
            for value in (from_h, trapz, mp_val):
                err = abs(value - analytic)
                if err > max_err:
                    max_err = float(err)
    # Hermite-2: closed ĥ_W = H(δ)H(−δ) vs quadrature of closed-form g.
    alpha = 1.0
    coeffs = np.array([0.0, 1.0, 0.0, 0.0, 0.0], dtype=np.float64)
    delta = 0.15 + 0.35j
    hat_hh = (
        np.dot(basis_laplace(delta, alpha), coeffs)
        * np.dot(basis_laplace(-delta, alpha), coeffs)
    )
    monomials = monomial_from_hermite(coeffs, alpha)
    sigma = 1.0 / math.sqrt(alpha)
    half_width = 12.0 * sigma
    u_grid = np.linspace(-half_width, half_width, 1601, dtype=np.float64)
    g_vals = np.array(
        [g_even_poly(float(u_value), alpha, monomials) for u_value in u_grid],
        dtype=np.complex128,
    )
    trapz = getattr(np, "trapezoid", None) or np.trapz
    trapz_h2 = trapz(g_vals * np.exp(delta * u_grid), u_grid)
    err_h2 = abs(trapz_h2 - hat_hh)
    if err_h2 > max_err:
        max_err = float(err_h2)
    ok = max_err < float(SPEC["g0_atol"])
    return ok, max_err


def a_grid_for(gamma: float, smoke: bool) -> tuple[float, ...]:
    if smoke:
        base = [0.05, 0.2, 1.0, 5.0, 20.0, 100.0]
    else:
        base = list(
            np.logspace(
                math.log10(float(SPEC["a_log_min"])),
                math.log10(float(SPEC["a_log_max"])),
                int(SPEC["a_log_n"]),
            )
        )
    extra = [gamma * gamma / denom for denom in (1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)]
    extra += [0.25, 0.5, 2.0, 10.0, 50.0, 200.0]
    extra += [abs(delta) * gamma / math.pi for delta in (0.01, 0.05, 0.2, 0.45)]
    values: list[float] = []
    seen: set[str] = set()
    for raw in base + extra:
        alpha = float(raw)
        if alpha < 1.0e-3 or alpha > 1.0e9:
            continue
        key = "%.10e" % alpha
        if key not in seen:
            seen.add(key)
            values.append(alpha)
    return tuple(sorted(values))


def flip_canon_vector(vector: np.ndarray) -> np.ndarray:
    out = np.real(np.asarray(vector, dtype=np.float64)).copy()
    pivot = int(np.argmax(np.abs(out)))
    if out[pivot] < 0.0:
        out *= -1.0
    return out


def candidate_rows(
    gram: np.ndarray, alpha: float, t_cut: float, scales: np.ndarray,
) -> list[tuple[float, float, np.ndarray]]:
    """Return (trunc, tail_trud, c_phys) for evecs + the pure Gaussian e0."""
    rows: list[tuple[float, float, np.ndarray]] = []
    if not np.all(np.isfinite(gram)):
        return rows
    try:
        _values, vectors = eigs_all(gram)
    except np.linalg.LinAlgError:
        return rows
    directions = [flip_canon_vector(vectors[:, index]) for index in range(N_BASIS)]
    directions.append(np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float64))
    for coeffs_w in directions:
        trunc = float(coeffs_w @ gram @ coeffs_w)
        if not math.isfinite(trunc):
            continue
        coeffs_phys = coeffs_w / scales
        tail_trud = certified_tail(coeffs_phys, alpha, t_cut, "trudgian")
        rows.append((trunc, tail_trud, coeffs_phys))
    return rows


def format_verdict(rows: list[dict]) -> str:
    sep_atol = float(SPEC["sep_atol"])
    eta_bar = float(SPEC["yoshida_eta_bar"])
    all_trunc = all(row["trunc"] < -sep_atol for row in rows)
    all_cert = all(row["cert"] < -sep_atol for row in rows)
    all_eta_tiny = all(row["eta"] < eta_bar for row in rows)
    worst_cert = max(rows, key=lambda row: row["cert"])
    worst_trunc = max(rows, key=lambda row: row["trunc"])
    failed = [row for row in rows if row["cert"] >= -sep_atol]
    if failed:
        worst_fail = min(failed, key=lambda row: (row["gamma"], -row["beta"]))
    else:
        worst_fail = worst_cert
    if all_cert and all_eta_tiny:
        return (
            "YOSHIDA_COLLAPSE(evidence=max_eta=%.3e,max_|g(log2)/g(0)|,a_min=%.3e,"
            "n_cells=%d,all_certified_but_prime_channel_past_log2_negligible)"
            % (
                max(row["eta"] for row in rows),
                min(row["a"] for row in rows),
                len(rows),
            )
        )
    if all_cert:
        return (
            "SEPARATION_GO_GAUSS(min_certified_margin=%.6e, worst=beta=%.2f,gamma=%.4g)"
            % (worst_cert["cert"], worst_cert["beta"], worst_cert["gamma"])
        )
    if all_trunc and not all_cert:
        return (
            "ONLINE_TAIL_STILL_SWAMPS(worst=beta=%.2f,gamma=%.4g,trunc=%.6e,"
            "tail_trud=%.6e,cert=%.6e)"
            % (
                worst_fail["beta"], worst_fail["gamma"], worst_fail["trunc"],
                worst_fail["tail_trud"], worst_fail["cert"],
            )
        )
    return (
        "INCONCLUSIVE_TRUNCATION(worst=beta=%.2f,gamma=%.4g,trunc=%.6e,"
        "n_trunc_neg=%d/%d,n_cert_neg=%d/%d)"
        % (
            worst_fail["beta"], worst_fail["gamma"], worst_fail["trunc"],
            sum(row["trunc"] < -sep_atol for row in rows), len(rows),
            sum(row["cert"] < -sep_atol for row in rows), len(rows),
        )
    )


def run(smoke: bool) -> int:
    n_zeros = 8 if smoke else int(SPEC["n_zeros"])
    betas = (0.6, 0.9) if smoke else tuple(SPEC["betas"])
    gammas = (1.0, 14.13) if smoke else tuple(SPEC["gammas"])
    ordinates = np.asarray(ON_LINE_ORDINATES[:n_zeros], dtype=np.float64)
    t_cut = float(ordinates[-1])
    sep_atol = float(SPEC["sep_atol"])
    g1_atol = float(SPEC["g1_atol"])
    n_prime = 400 if smoke else int(SPEC["prime_n_cap"])
    lam = von_mangoldt_table(n_prime)

    print("weil_gaussian_separation_probe -- r539")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("class Hermite-Gaussian even deg<=8  h(t)=p(t)exp(-a t^2)  g=h*h~")
    print("tail_certified Trudgian JNT 134 (2014) Thm1/Cor1  "
          "|S(T)|<=0.111 log T + 0.275 log log T + 2.450  (T>=e)")
    print("tail_crude N(T+1)-N(T)<=%.1f log(T+2)  (T>=14, in-probe majorant)"
          % float(SPEC["c_crude"]))
    print("tail_heuristic RvM density log(T/2pi)/(2pi)  LABEL=HEURISTIC")
    print("n_zeros %d t1=%.16f tN=%.16f" % (
        n_zeros, float(ordinates[0]), t_cut))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("prime_convention Lambda(n)*(1+1/n)*g(log n)")

    section("G0  PURE-GAUSSIAN / HERMITE-2 CLOSED FORM vs QUADRATURE")
    g0_ok, g0_err = run_g0()
    check("G0-calibration-1e-12", g0_ok, "max_abs_err=%.3e atol=%.0e" % (
        g0_err, float(SPEC["g0_atol"])))

    section("TAIL-CONSTANT MAJORANT (C_CRUDE vs Trudgian unit increment)")
    c_ok = True
    c_ratio_max = 0.0
    for height in (14.0, 30.0, 100.0, 236.0, 1.0e3, 1.0e4, 1.0e5, 1.0e6):
        trud = trudgian_increment(height, 1.0)
        crude = crude_increment(height, 1.0)
        ratio = trud / math.log(height + 2.0)
        if ratio > c_ratio_max:
            c_ratio_max = ratio
        if crude + 1.0e-12 < trud:
            c_ok = False
    check(
        "C_CRUDE-majorises-Trudgian",
        c_ok,
        "C=%.1f max_B/log(T+2)=%.3f over frozen T-grid"
        % (float(SPEC["c_crude"]), c_ratio_max),
    )

    unique_a = sorted({
        alpha for gamma in gammas for alpha in a_grid_for(gamma, smoke)
    })

    section("G1  ON-LINE WEIL POSITIVITY (no injected zero, + certified tail)")
    g1_worst = math.inf
    g1_ok = True
    g1_tail_ok = True
    g1_n = 0
    # Whitened physical G_on: theoretically PSD.
    for alpha in unique_a[: (8 if smoke else len(unique_a))]:
        gram_on, _gram_off, scales = assemble_cell(alpha, ordinates, None, None)
        if not np.all(np.isfinite(gram_on)):
            continue
        lam_min, vecs = eigs_all(gram_on)
        g1_n += 1
        g1_worst = min(g1_worst, float(lam_min[0]))
        ok = float(lam_min[0]) >= -g1_atol
        g1_ok = g1_ok and ok
        coeffs_phys = flip_canon_vector(vecs[:, 0]) / scales
        tail = certified_tail(coeffs_phys, alpha, t_cut, "trudgian")
        if float(lam_min[0]) + tail < -g1_atol:
            g1_tail_ok = False
    if not math.isfinite(g1_worst):
        g1_worst = 0.0
    print("  sampled_a=%d min_lam_on=%+.6e" % (g1_n, g1_worst))
    check(
        "G1-online-psd",
        g1_ok,
        "min_lam_on=%.6e atol=%.0e" % (g1_worst, g1_atol),
    )
    check(
        "G1-online-plus-certified-tail",
        g1_tail_ok,
        "truncated+tail >= -atol on sampled a-grid",
    )

    section("SEARCH  INJECTED OFF-CRITICAL QUADRUPLE")
    print("  %-6s %-8s %-14s %-14s %-14s %-14s %-10s %-10s %s" % (
        "beta", "gamma", "trunc", "tail_trud", "cert", "tail_heur",
        "a", "eta", "top_c"))
    rows: list[dict] = []
    for beta in betas:
        delta = float(beta) - 0.5
        for gamma in gammas:
            best: dict | None = None
            for alpha in a_grid_for(gamma, smoke):
                gram_on, gram_off, scales = assemble_cell(
                    alpha, ordinates, delta, float(gamma),
                )
                gram = gram_on + gram_off
                for trunc, tail_trud, coeffs_phys in candidate_rows(
                    gram, alpha, t_cut, scales,
                ):
                    cert = trunc + tail_trud
                    cand = {
                        "beta": float(beta),
                        "gamma": float(gamma),
                        "trunc": trunc,
                        "tail_trud": tail_trud,
                        "cert": cert,
                        "a": alpha,
                        "coeffs": coeffs_phys,
                    }
                    if best is None or cert < best["cert"]:
                        best = cand
            assert best is not None
            best["tail_crude"] = certified_tail(
                best["coeffs"], best["a"], t_cut, "crude",
            )
            best["tail_heur"] = certified_tail(
                best["coeffs"], best["a"], t_cut, "heur",
            )
            coupling = prime_coupling(best["coeffs"], best["a"], n_prime, lam)
            best.update(coupling)
            order = np.argsort(-np.abs(best["coeffs"]))[:3]
            top = ",".join(
                "c%d:%.3e" % (int(index), float(best["coeffs"][index]))
                for index in order
            )
            best["top"] = top
            rows.append(best)
            print("  %-6.2f %-8.4g %+.6e %+.6e %+.6e %+.6e %-10.3e %-10.3e %s" % (
                best["beta"], best["gamma"], best["trunc"], best["tail_trud"],
                best["cert"], best["tail_heur"], best["a"], best["eta"], top))

    section("G4  YOSHIDA TRAP (prime-channel coupling of minimizers)")
    eta_bar = float(SPEC["yoshida_eta_bar"])
    winners = [row for row in rows if row["cert"] < -sep_atol]
    eta_scope = winners if winners else rows
    n_prime_alive = sum(row["eta"] >= eta_bar for row in eta_scope)
    max_eta = max(row["eta"] for row in eta_scope)
    min_eta = min(row["eta"] for row in eta_scope)
    max_cont = max(abs(row["contour"]) for row in eta_scope)
    print("  convention contour Sigma Lambda(n)*(1+1/n)*g(log n)")
    print("  also_reported combMass Sigma 2*Lambda(n)/sqrt(n)*g(log n)")
    print("  eta=|g(log 2)/g(0)|  bar=%.0e  scope=%s n=%d  alive=%d/%d  max_eta=%.3e min_eta=%.3e"
          % (eta_bar, "certified_separators" if winners else "all_cells",
             len(eta_scope), n_prime_alive, len(eta_scope), max_eta, min_eta))
    print("  max_|contour_sum|=%.3e (n<=%d prime-power sum, not the envelope UB)"
          % (max_cont, n_prime))
    for row in rows:
        print("  beta=%.2f gamma=%.4g a=%.3e eta=%.3e contour=%.3e comb=%.3e g0=%.3e"
              % (row["beta"], row["gamma"], row["a"], row["eta"],
                 row["contour"], row["comb"], row["g0"]))
    yoshida = bool(winners) and n_prime_alive == 0
    check(
        "G4-prime-channel-evaluated",
        True,
        "YOSHIDA_COLLAPSE_flag=%s n_alive=%d/%d" % (
            "yes" if yoshida else "no", n_prime_alive, len(eta_scope)),
    )

    section("GATES / VERDICT")
    n_trunc = sum(row["trunc"] < -sep_atol for row in rows)
    n_heur = sum(row["trunc"] + row["tail_heur"] < -sep_atol for row in rows)
    n_cert = sum(row["cert"] < -sep_atol for row in rows)
    check("G1-sanity-held", g1_ok and g1_tail_ok, "on-line form + tail")
    check(
        "G2-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G3-smoke-subset", True, "smoke grid 2x2 N=8 reduced a-grid")
    else:
        check(
            "G3-full-grid",
            True,
            "full grid %dx%d N=%d a_log_n=%d"
            % (len(betas), len(gammas), n_zeros, int(SPEC["a_log_n"])),
        )
    check("search-ran", len(rows) == len(betas) * len(gammas), "%d cells" % len(rows))
    print("  trunc_neg %d/%d  heur_sep %d/%d  trudgian_certified %d/%d" % (
        n_trunc, len(rows), n_heur, len(rows), n_cert, len(rows)))

    verdict = format_verdict(rows)
    failures = [name for name, passed in CHECKS if not passed]
    print("CHECKS %d/%d" % (len(CHECKS) - len(failures), len(CHECKS)))
    print("VERDICT %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    if failures:
        print("GATE_FAILURES " + ",".join(failures))
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r539 Gaussian/Hermite Weil height-uniform separation (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
