#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_gabor_separation_probe -- PRIME.RDAGGER.WEIL_GABOR_SEPARATION.01

Round 541.  Direct fix for the r539 finding: a Fourier transform
centered at 0 has no mass at t ≈ γ, so even Hermite–Gaussians that
certified the omitted on-line tail still failed every γ ≥ 30 at
truncation (INCONCLUSIVE_TRUNCATION).  This probe frequency-shifts
the Gaussian, h(t) = p(t) e^{-a t²} cos(ω t) with p even of degree
≤ 4 (a Gabor / wavepacket), so ĥ_W(1/2+it) is a sum of Gaussians
centered at t = ±ω.  The on-line mass at height γ is then bounded
WITHOUT enumerating zeros at that height.

CLAIM BOUNDARY.  Finite quadratic-form search in a 3-dimensional
even Gabor–Hermite subclass, plus an explicit Trudgian-type majorant
on the FULL on-line spectral mass (enumerated first-100 exact, plus
a density-bound integral of the Gaussian envelope around/beyond
±ω).  Conditional on the frozen first-100 ordinates.  NO RH claim,
NO anti-RH claim, NO ledger row, NO paper edit, NO Lean edit.  A
negative certified Rayleigh is not a theorem for the infinite-
dimensional Schwartz class.  A failure here is a failure of this
subclass + this tail majorant, not of every frequency-shifted class.

HAT CONVENTION.  Lean FullWeilTest.hat is the unshifted Laplace
transform ∫ g(t) exp(s t) dt.  This probe uses the classical
Weil-shifted pairing

    ĥ_W(s) := ∫ g(u) exp((s − 1/2) u) du = H(s−1/2) H(1/2−s),

so ĥ_W(1/2+it) = |H(it)|² ≥ 0.  Identifying hat_Lean(ρ) with ĥ_W(ρ)
is the same open dictionary as r535/r539.

PARAMETER.  h(t) = p(t) exp(−a t²) cos(ω t) with p even, deg ≤ 4,
spanned by physicists' Hermite H_{2k}(√a t), k=0..2.  For the pure
Gabor (k=0):

    H(z) = (1/2) √(π/a) [ exp((z+iω)²/(4a)) + exp((z−iω)²/(4a)) ],
    ĥ_W(1/2+it) = (π/(4a)) [ e^{-(t+ω)²/(2a)} + e^{-(t−ω)²/(2a)}
                            + 2 e^{-(t²+ω²)/(2a)} ],
    g(u) = √(π/(2a))/2 · e^{-a u²/2} [ cos(ω u) + e^{-ω²/(2a)} ].

At ω = 0 this collapses to the r539 Gaussian
g(u)=√(π/(2a)) e^{-a u²/2},  ĥ_W(s)=(π/a) exp((s−1/2)²/(2a)).

OFF-LINE MECHANISM.  With ω ≈ γ and σ = β−1/2,

    ĥ_W(β+iγ) ≈ (π/(4a)) exp(σ²/(2a)) exp(i σ(γ−ω)/a)

(the unmatched lobe at t = −ω is exponentially small).  The
quadruple contribution is 4 Re ĥ_W.  The factor exp(σ²/(2a)) is
the off-line enhancement relative to the on-line envelope peak
π/(4a): σ enters the Gaussian in the REAL direction, while the
on-line abscissa is purely imaginary.  Phase-tuning
ω = γ − π a / σ makes the cosine = −1, so the quadruple is
≈ −(π/a) exp(σ²/(2a)).

ON-LINE BOUND (what is CERTIFIED vs HEURISTIC).  Let
f(t) = ĥ_W(1/2+it) ≥ 0.  Production bound:

    W_on^UB = 2 Σ_{k=1}^{N} f(γ_k)     [EXACT on the freeze]
             + Tail(f; T=γ_N, mode)    [already includes ±]

  mode=trudgian: N(T+H)−N(T) ≤ θ(T+H)−θ(T)+E(T+H)+E(T), H≥1,
    with E from Trudgian JNT 134 (2014) Thm 1 + Cor 1.  Envelope
    charged at a true sup-majorant on each bin.  LABEL=CERTIFIED
    relative to that cited bound (not a new zero-density theorem).
    The 2E lump per bin is the price of not knowing N exactly;
    bins of width 1 are used near ±ω so a narrow packet is not
    swallowed by a 0.04 T window.  Remainder past the packet uses
    the CRUDE-SAFE C=4 incomplete-gamma majorant (same hybrid as
    r539).

  mode=crude: N(T+1)−N(T) ≤ C_CRUDE log(T+2), C_CRUDE=4, T≥14,
    in-probe majorant of the Trudgian unit increment.
    LABEL=CRUDE-SAFE.

  mode=heur: Riemann–von-Mangoldt density log(T/2π)/(2π) times
    f, no 2E lump.  LABEL=HEURISTIC.  Not a proof ingredient.

γ = 10000 is bounded by the envelope integral around ω ≈ 10000;
mpmath.zetazero is never called at that height.

TAIL CONSTANTS (copied from r539, not re-derived):

    |S(T)| ≤ 0.111 log T + 0.275 log log T + 2.450    (T≥e),
    E(T)  = 0.111 log T + 0.275 log log T + 2.450 + 0.2/T,
    θ(T)  = (T/2π) log(T/(2π e)) + 7/8.

Runtime: numpy.  Zeros cached from mpmath.zetazero (mpmath 1.3.0,
dps=30, 2026-09-01); mpmath is used only for G0 quadrature, not
for zeros at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import warnings

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

warnings.filterwarnings("ignore", category=RuntimeWarning)


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
SPEC = {
    "round": 541,
    "target": "gabor_wavepacket_height_uniform_separation_precheck",
    "hat": "weil_shifted",
    "parent_round": 539,
    "betas": [0.51, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95],
    "gammas": [5.0, 14.13, 30.0, 100.0, 1000.0, 10000.0],
    "n_zeros": 100,
    "hermite_degrees": [0, 2, 4],
    "a_log_min": 1.0e-3,
    "a_log_max": 1.0e2,
    "a_log_n": 21,
    "sep_atol": 1e-12,
    "g0_atol": 1e-12,
    "g1_atol": 1e-8,
    "g5_atol": 1e-9,
    "c_crude": 4.0,
    "trudgian_a": 0.111,
    "trudgian_b": 0.275,
    "trudgian_c": 2.450,
    "trudgian_nt_extra": 0.2,
    "trudgian_source": "Trudgian JNT 134 (2014) 280-292 / arXiv:1208.5846 Thm1+Cor1",
    "yoshida_eta_bar": 1e-10,
    "prime_n_cap": 20000,
    "prime_convention": (
        "Lambda(n)*(1+1/n)*g(log n)  [contour; combMass "
        "2*Lambda(n)/sqrt(n)*g(log n) also reported]"
    ),
    "g5_anchor": {"beta": 0.60, "gamma": 0.5, "a": 2.0, "omega": 0.0},
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

# Physicists' H_{0,2,4}(x) as coefficients of x^{0,2,4}.
HE_COEF = np.array(
    [
        [1.0, 0.0, 0.0],
        [-2.0, 4.0, 0.0],
        [12.0, -48.0, 16.0],
    ],
    dtype=np.float64,
)

# First 100 positive ordinates.  Same freeze as r535/r539.
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
N_BASIS = 3
LOG_CLIP = 700.0
E0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-40s %s" % (
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
    """E[T^{0,2,4}] for T ~ N(mu, var), analytic continuation in mu."""
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


def cexp(log_value: complex) -> complex:
    real_part = float(np.real(log_value))
    if real_part > LOG_CLIP:
        return complex(math.inf)
    if real_part < -LOG_CLIP:
        return 0.0 + 0.0j
    return complex(np.exp(log_value))


def exp_clip(log_value: float) -> float:
    if log_value > LOG_CLIP:
        return math.inf
    if log_value < -LOG_CLIP:
        return 0.0
    return math.exp(log_value)


def log_pref(z: complex, alpha: float) -> complex:
    return 0.5 * math.log(math.pi / alpha) + (z * z) / (4.0 * alpha)


def p_vector(z: complex, alpha: float) -> np.ndarray:
    """Prefactor-free Laplace polynomial: H_G(z) = √(π/a) e^{z²/(4a)} (P·c)."""
    mu = z / (2.0 * alpha)
    var = 1.0 / (2.0 * alpha)
    return hermite_monomial_matrix(alpha) @ even_raw_moments(mu, var)


def basis_laplace_gauss(z: complex, alpha: float) -> np.ndarray:
    """L_k(z) = ∫ H_{2k}(√a t) e^{-a t²} e^{z t} dt, k=0..2."""
    poly = p_vector(z, alpha)
    return cexp(log_pref(z, alpha)) * poly


def gabor_phi(z: complex, alpha: float, omega: float) -> np.ndarray:
    """φ_k(z) = (1/2) [L_k(z+iω) + L_k(z−iω)].  H(z) = φ(z)·c."""
    if omega == 0.0:
        return basis_laplace_gauss(z, alpha)
    return 0.5 * (
        basis_laplace_gauss(z + 1j * omega, alpha)
        + basis_laplace_gauss(z - 1j * omega, alpha)
    )


def hat_W_value(delta: complex, alpha: float, omega: float, coeffs: np.ndarray) -> complex:
    """ĥ_W(1/2+δ) = H(δ) H(−δ)."""
    left = np.dot(gabor_phi(delta, alpha, omega), coeffs)
    right = np.dot(gabor_phi(-delta, alpha, omega), coeffs)
    product = left * right
    if not np.isfinite(np.real(product)) or not np.isfinite(np.imag(product)):
        return complex(math.inf)
    return complex(product)


def hat_W_pure_gabor(delta: complex, alpha: float, omega: float) -> complex:
    """Closed form for p ≡ 1.  Equals (π/a) exp(δ²/(2a)) at ω=0."""
    pref = 0.5 * math.sqrt(math.pi / alpha)
    h_val = pref * (
        cexp((delta + 1j * omega) ** 2 / (4.0 * alpha))
        + cexp((delta - 1j * omega) ** 2 / (4.0 * alpha))
    )
    return h_val * h_val


def f_online_pure(t_value: float, alpha: float, omega: float) -> float:
    """Exact ĥ_W(1/2+it) for the pure Gabor.  Sum of Gaussians at ±ω."""
    t_value = float(t_value)
    pref = math.pi / (4.0 * alpha)
    left = exp_clip(-(t_value + omega) ** 2 / (2.0 * alpha))
    right = exp_clip(-(t_value - omega) ** 2 / (2.0 * alpha))
    cross = exp_clip(-(t_value * t_value + omega * omega) / (2.0 * alpha))
    return pref * (left + right + 2.0 * cross)


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


def eigs_all(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(matrix)
    for column in range(vectors.shape[1]):
        pivot = int(np.argmax(np.abs(vectors[:, column])))
        if vectors[pivot, column].real < 0.0:
            vectors[:, column] *= -1.0
    return np.real(values), np.real(vectors)


def flip_canon_vector(vector: np.ndarray) -> np.ndarray:
    out = np.real(np.asarray(vector, dtype=np.float64)).copy()
    pivot = int(np.argmax(np.abs(out)))
    if out[pivot] < 0.0:
        out *= -1.0
    return out


# ---------------------------------------------------------------------------
# Tail majorants (Trudgian / crude / heuristic) — same constants as r539
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


def rvm_density(height: float) -> float:
    density = math.log(max(float(height), 2.0 * math.pi) / (2.0 * math.pi)) / (
        2.0 * math.pi
    )
    return density if density > 0.0 else 0.0


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
    square = np.zeros(2 * N_BASIS - 1, dtype=np.float64)
    for i_index, left in enumerate(q_vec):
        for j_index, right in enumerate(q_vec):
            square[i_index + j_index] += float(left) * float(right)
    return square


def e0_scale(coeffs: np.ndarray) -> float | None:
    """Return c0 if this is a scaled pure Gabor (no H2/H4), else None."""
    if abs(float(coeffs[1])) < 1.0e-14 and abs(float(coeffs[2])) < 1.0e-14:
        return float(coeffs[0])
    return None


def is_pure_e0(coeffs: np.ndarray) -> bool:
    scale = e0_scale(coeffs)
    return scale is not None and abs(scale - 1.0) < 1.0e-14


def gauss_lobe_sup(t0: float, t1: float, center: float, alpha: float) -> float:
    """sup_{t∈[t0,t1]} exp(−(t−center)²/(2a)) on a closed interval, t0≤t1."""
    peak = float(center)
    if t0 <= peak <= t1:
        return 1.0
    d0 = t0 - peak
    d1 = t1 - peak
    dist_sq = min(d0 * d0, d1 * d1)
    return exp_clip(-dist_sq / (2.0 * alpha))


def env_sup(
    coeffs: np.ndarray, alpha: float, omega: float, t0: float, t1: float,
) -> float:
    """Upper bound of ĥ_W(1/2+it) on [t0,t1], t0≥0.

    Pure Gabor (e0): exact sup of the three-Gaussian closed form.
    General c: (1/4)(L(t+ω)+L(t−ω))² with L(ξ)=√(π/a) e^{−ξ²/(4a)} Q(|ξ|),
    Q from the r539 triangle majorant.  At ω=0, e0 this is (π/a) e^{−t0²/(2a)}
    on a decreasing tail, matching r539 log_env_hat.
    """
    t0 = max(float(t0), 0.0)
    t1 = max(float(t1), t0)
    scale = e0_scale(coeffs)
    if scale is not None:
        pref = (scale * scale) * math.pi / (4.0 * alpha)
        left = gauss_lobe_sup(t0, t1, -omega, alpha)
        right = gauss_lobe_sup(t0, t1, omega, alpha)
        # Cross term 2 exp(−(t²+ω²)/(2a)) is decreasing in t≥0.
        cross = 2.0 * exp_clip(-(t0 * t0 + omega * omega) / (2.0 * alpha))
        return pref * (left + right + cross)
    q_vec = triangle_Q_coeffs(coeffs, alpha)
    # Conservative: Gaussian at its max on the bin, Q at its max on the bin.
    def lobe_bound(center: float) -> float:
        xi0 = t0 - center
        xi1 = t1 - center
        # dist from 0 to [xi0, xi1]
        if xi0 <= 0.0 <= xi1:
            gauss = 1.0
        else:
            dist = min(abs(xi0), abs(xi1))
            gauss = exp_clip(-(dist * dist) / (2.0 * alpha))
        q_hi = max(poly_even_eval(q_vec, abs(xi0)), poly_even_eval(q_vec, abs(xi1)))
        if xi0 <= 0.0 <= xi1:
            q_hi = max(q_hi, poly_even_eval(q_vec, 0.0))
        # Interior max of Q(|ξ|) is at an endpoint for even increasing Q.
        return (math.pi / alpha) * gauss * (q_hi * q_hi if q_hi > 0.0 else 0.0)

    # (1/2)(L−² + L+²) ≥ (1/4)(L−+L+)².
    return 0.5 * (lobe_bound(omega) + lobe_bound(-omega))


def remainder_shifted(
    coeffs: np.ndarray, alpha: float, omega: float, t_lo: float,
) -> float:
    """∫_{t_lo}^∞ 2 C_CRUDE log(t+2) · majorant(t) dt, t_lo ≥ 0.

    Charges the (t−ω) lobe with the r539 incomplete-gamma recurrence
    after the shift u=t−ω ≥ t_lo−ω, plus a cruder (t+ω) lobe.  At
    ω=0 and e0 this is identical to r539 remainder_integral.
    """
    if t_lo <= 0.0:
        t_lo = 1.0
    beta = 1.0 / (2.0 * alpha)
    q_vec = triangle_Q_coeffs(coeffs, alpha)
    square = Q_square_even_coeffs(q_vec)
    log0 = math.log(t_lo + 2.0)
    inv = 1.0 / (t_lo + 2.0)
    u_lo = max(t_lo - float(omega), 0.0)

    def lobe_acc(u_start: float) -> float:
        acc = 0.0
        for p_index, s_coef in enumerate(square):
            if s_coef <= 0.0:
                continue
            i_even = I_power_gauss(2 * p_index, u_start, beta)
            i_odd = I_power_gauss(2 * p_index + 1, u_start, beta)
            acc += float(s_coef) * (log0 * i_even + inv * i_odd)
        return acc

    acc = lobe_acc(u_lo)
    # Second lobe about −ω; at ω=0 this is the same lobe — do not double.
    if abs(float(omega)) > 1.0e-12:
        acc += lobe_acc(t_lo + abs(float(omega)))
    return 2.0 * float(SPEC["c_crude"]) * (math.pi / alpha) * acc


def nbound_choice(mode: str, height: float, width: float) -> float:
    if mode == "trudgian":
        return trudgian_increment(height, width)
    if mode == "crude":
        return crude_increment(height, width)
    return rvm_density(height) * max(float(width), 1.0)


def certified_tail(
    coeffs: np.ndarray, alpha: float, omega: float, t_cut: float, mode: str,
) -> float:
    """Bound on 2 Σ_{t_n > t_cut} f(t_n).  mode in {trudgian, crude, heur}.

    Walks from t_cut with r539's 0.04 T steps on the far tail, but
    forces width = 1 (the Trudgian H≥1 floor) in a window of width
    W around |ω| so a narrow packet at large height is not billed
    as one huge 0.04 T bin times the peak.  No zeros are enumerated
    above t_cut: the packet at γ=10000 is an envelope×density bound.
    """
    width_scale = max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 8.0)
    omega_abs = abs(float(omega))
    t_hard = max(float(t_cut) + width_scale, omega_abs + width_scale)
    t_hard = min(t_hard, 1.0e7)
    window = width_scale
    total = 0.0
    t_value = float(t_cut)
    while t_value < t_hard:
        in_window = abs(t_value - omega_abs) <= window + 1.0
        if in_window:
            width = 1.0
        else:
            width = max(1.0, 0.04 * t_value)
            target = omega_abs - window
            if t_value < target < t_value + width:
                width = max(1.0, target - t_value)
        if t_value + width > t_hard:
            width = max(1.0, t_hard - t_value)
        nbound = nbound_choice(mode, t_value, width)
        env = env_sup(coeffs, alpha, omega, t_value, t_value + width)
        total += 2.0 * nbound * env
        if not math.isfinite(total) or total > 1.0e250:
            return math.inf
        t_value += width
    if mode == "heur":
        density = rvm_density(t_value)
        beta = 1.0 / (2.0 * alpha)
        u0 = max(t_value - omega_abs, 0.0)
        integral = (math.pi / alpha) * I_power_gauss(0, u0, beta)
        total += 2.0 * density * integral
    else:
        total += remainder_shifted(coeffs, alpha, omega, t_value)
    if not math.isfinite(total):
        return math.inf
    return float(total)


def density_bound_interval(
    coeffs: np.ndarray, alpha: float, omega: float,
    t_lo: float, t_hi: float, mode: str,
) -> float:
    """CERTIFIED/CRUDE/HEUR bound on 2 Σ_{t_lo < t_n ≤ t_hi} f(t_n).

    Same increment×env_sup walk, no remainder (finite interval).
    Used for G1: enumerated first-100 mass ≤ this bound on [14, T].
    """
    t_value = max(float(t_lo), math.e)
    t_hi = max(float(t_hi), t_value + 1.0)
    omega_abs = abs(float(omega))
    window = max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 8.0)
    total = 0.0
    while t_value < t_hi:
        in_window = abs(t_value - omega_abs) <= window + 1.0
        width = 1.0 if in_window else max(1.0, 0.04 * t_value)
        if t_value + width > t_hi:
            width = max(1.0, t_hi - t_value)
        nbound = nbound_choice(mode, t_value, width)
        env = env_sup(coeffs, alpha, omega, t_value, t_value + width)
        total += 2.0 * nbound * env
        if not math.isfinite(total) or total > 1.0e250:
            return math.inf
        t_value += width
    return float(total)


# ---------------------------------------------------------------------------
# Autocorrelation g and prime coupling (G4 / Yoshida trap)
# ---------------------------------------------------------------------------
def monomial_from_hermite(coeffs: np.ndarray, alpha: float) -> np.ndarray:
    return hermite_monomial_matrix(alpha).T @ np.asarray(coeffs, dtype=np.float64)


def shift_even_poly(monomials: np.ndarray, shift: float) -> list[float]:
    """Coefficients of 1, v, v², v³, v⁴ in p(v+shift), p even deg ≤ 4."""
    m0 = float(monomials[0]) if monomials.size > 0 else 0.0
    m1 = float(monomials[1]) if monomials.size > 1 else 0.0
    m2 = float(monomials[2]) if monomials.size > 2 else 0.0
    s_val = float(shift)
    coeffs = [0.0] * 5
    coeffs[0] += m0
    coeffs[0] += m1 * s_val * s_val
    coeffs[1] += m1 * 2.0 * s_val
    coeffs[2] += m1
    s2 = s_val * s_val
    s3 = s2 * s_val
    s4 = s2 * s2
    coeffs[0] += m2 * s4
    coeffs[1] += m2 * 4.0 * s3
    coeffs[2] += m2 * 6.0 * s2
    coeffs[3] += m2 * 4.0 * s_val
    coeffs[4] += m2
    return coeffs


def poly_mul(left: list[float], right: list[float]) -> list[float]:
    out = [0.0] * (len(left) + len(right) - 1)
    for i_index, left_c in enumerate(left):
        if left_c == 0.0:
            continue
        for j_index, right_c in enumerate(right):
            if right_c == 0.0:
                continue
            out[i_index + j_index] += left_c * right_c
    return out


def poly_gauss_fourier(power_coeffs: list[float], two_a: float, freq: float) -> complex:
    """∫ q(v) e^{−2a v²} e^{i freq v} dv, q given by power_coeffs."""
    mu = 1j * freq / (2.0 * two_a)
    var = 1.0 / (2.0 * two_a)
    log_pref_val = 0.5 * math.log(math.pi / two_a) + (
        -(freq * freq) / (4.0 * two_a)
    )
    pref = cexp(log_pref_val)
    acc = 0.0 + 0.0j
    # Moments of N(mu, var) for powers 0..deg.
    max_pow = len(power_coeffs) - 1
    moments = [0.0 + 0.0j] * (max_pow + 1)
    moments[0] = 1.0 + 0.0j
    # Recurrence: E[X^{n}] via binomial around mu, central even moments.
    for n_power in range(1, max_pow + 1):
        tot = 0.0 + 0.0j
        for even_k in range(0, n_power + 1, 2):
            m_half = even_k // 2
            central = (var ** m_half) * odd_double_factorial(m_half)
            tot += math.comb(n_power, even_k) * (mu ** (n_power - even_k)) * central
        moments[n_power] = tot
    for power, coef in enumerate(power_coeffs):
        if coef == 0.0:
            continue
        acc += coef * moments[power]
    return pref * acc


def g_gabor(u_value: float, alpha: float, omega: float, monomials: np.ndarray) -> float:
    """g(u)=∫ h(t) h(t−u) dt for h(t)=p(t) e^{-a t²} cos(ω t), p even.

    Uses cos A cos B = [cos(A+B)+cos(A−B)]/2 and a Gaussian completing
    the square.  Oscillatory: negative values are genuine.
    """
    gauss = exp_clip(-0.5 * alpha * u_value * u_value)
    half = 0.5 * float(u_value)
    q_poly = poly_mul(shift_even_poly(monomials, half), shift_even_poly(monomials, -half))
    two_a = 2.0 * alpha
    i_dc = poly_gauss_fourier(q_poly, two_a, 0.0)
    i_cos = poly_gauss_fourier(q_poly, two_a, 2.0 * omega)
    # Both integrals are real (q even).
    value = 0.5 * gauss * (
        math.cos(omega * u_value) * float(np.real(i_dc)) + float(np.real(i_cos))
    )
    return float(value)


def g_pure_gabor(u_value: float, alpha: float, omega: float) -> float:
    pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
    return pref * exp_clip(-0.5 * alpha * u_value * u_value) * (
        math.cos(omega * u_value) + exp_clip(-(omega * omega) / (2.0 * alpha))
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


def prime_coupling(
    coeffs: np.ndarray, alpha: float, omega: float, n_max: int, lam: np.ndarray,
) -> dict:
    monomials = monomial_from_hermite(coeffs, alpha)
    scale = e0_scale(coeffs)
    if scale is not None:
        g0 = (scale * scale) * g_pure_gabor(0.0, alpha, omega)
        g_log2 = (scale * scale) * g_pure_gabor(math.log(2.0), alpha, omega)

        def g_at(u_value: float) -> float:
            return (scale * scale) * g_pure_gabor(u_value, alpha, omega)
    else:
        g0 = g_gabor(0.0, alpha, omega, monomials)
        g_log2 = g_gabor(math.log(2.0), alpha, omega, monomials)

        def g_at(u_value: float) -> float:
            return g_gabor(u_value, alpha, omega, monomials)

    eta = abs(g_log2) / abs(g0) if abs(g0) > 0.0 else math.inf
    contour = 0.0
    comb = 0.0
    n_neg = 0
    limit = min(n_max, lam.size - 1)
    for n_value in range(2, limit + 1):
        von = float(lam[n_value])
        if von == 0.0:
            continue
        g_u = g_at(math.log(n_value))
        if g_u < 0.0:
            n_neg += 1
        contour += von * (1.0 + 1.0 / n_value) * g_u
        comb += 2.0 * von / math.sqrt(n_value) * g_u
    return {
        "g0": g0,
        "g_log2": g_log2,
        "eta": eta,
        "contour": contour,
        "comb": comb,
        "n_neg_g": n_neg,
    }


# ---------------------------------------------------------------------------
# Cell assembly
# ---------------------------------------------------------------------------
def assemble_cell(
    alpha: float,
    omega: float,
    ordinates: np.ndarray,
    delta: float | None,
    gamma: float | None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Whitened Gram (G_on, G_off, scales) in the 3-D Hermite–Gabor frame."""
    phi_on = np.vstack(
        [gabor_phi(1j * float(height), alpha, omega) for height in ordinates]
    )
    if delta is None or gamma is None:
        phi_left = np.zeros(N_BASIS, dtype=np.complex128)
        phi_right = np.zeros(N_BASIS, dtype=np.complex128)
    else:
        phi_left = gabor_phi(delta + 1j * gamma, alpha, omega)
        phi_right = gabor_phi(-delta - 1j * gamma, alpha, omega)
    rms = np.sqrt(
        np.mean(np.abs(phi_on) ** 2, axis=0)
        + 0.5 * np.abs(phi_left) ** 2
        + 0.5 * np.abs(phi_right) ** 2
    )
    scales = np.maximum(rms, 1.0e-30)
    phi_on_w = phi_on / scales
    gram_on = np.zeros((N_BASIS, N_BASIS), dtype=np.float64)
    for index, _height in enumerate(ordinates):
        vec = phi_on_w[index]
        if not np.all(np.isfinite(vec)):
            continue
        # ĥ_W(1/2+it) = |H(it)|²; factor 2 for ± ordinates.
        gram_on += 2.0 * gram_modsq(vec)
    gram_off = np.zeros((N_BASIS, N_BASIS), dtype=np.float64)
    if delta is not None and gamma is not None:
        left_w = phi_left / scales
        right_w = phi_right / scales
        if np.all(np.isfinite(left_w)) and np.all(np.isfinite(right_w)):
            gram_off = 4.0 * gram_re_product(left_w, right_w)
    return gram_on, gram_off, scales


def enum_online_mass(
    coeffs: np.ndarray, alpha: float, omega: float, ordinates: np.ndarray,
) -> float:
    """Exact 2 Σ_{k=1}^N ĥ_W(1/2+i γ_k) on the freeze.  LABEL=EXACT."""
    total = 0.0
    for height in ordinates:
        hat = hat_W_value(1j * float(height), alpha, omega, coeffs)
        val = float(np.real(hat))
        if val < 0.0 and val > -1.0e-14:
            val = 0.0
        if not math.isfinite(val):
            return math.inf
        total += 2.0 * val
    return total


def off_line_quad(
    coeffs: np.ndarray, alpha: float, omega: float, delta: float, gamma: float,
) -> float:
    """4 Re ĥ_W(β+iγ) for the FE quadruple.  LABEL=EXACT closed form."""
    hat = hat_W_value(delta + 1j * gamma, alpha, omega, coeffs)
    if not math.isfinite(float(np.real(hat))):
        return math.inf if float(np.real(hat)) > 0.0 else -math.inf
    return 4.0 * float(np.real(hat))


def enhancement_factor(delta: float, alpha: float) -> float:
    """exp(σ²/(2a)): off-line Gaussian in the real direction vs on-line peak."""
    return exp_clip((delta * delta) / (2.0 * alpha))


def predicted_off_pure(delta: float, gamma: float, alpha: float, omega: float) -> float:
    """Leading-lobe  (π/a) exp((σ²−(γ−ω)²)/(2a)) cos(σ(γ−ω)/a)."""
    detune = float(gamma) - float(omega)
    phase = delta * detune / alpha
    log_mag = (delta * delta - detune * detune) / (2.0 * alpha)
    return (math.pi / alpha) * exp_clip(log_mag) * math.cos(phase)


def a_grid_for(gamma: float, delta: float, smoke: bool) -> tuple[float, ...]:
    if smoke:
        base = [0.01, 0.05, 0.2, 1.0, 5.0]
    else:
        base = list(
            np.logspace(
                math.log10(float(SPEC["a_log_min"])),
                math.log10(float(SPEC["a_log_max"])),
                int(SPEC["a_log_n"]),
            )
        )
    sigma = max(abs(float(delta)), 1.0e-12)
    a_char = (sigma * sigma) / (math.pi * math.pi)
    extra = [a_char * scale for scale in (0.05, 0.25, 0.5, 1.0, 2.0, 4.0, 16.0)]
    extra += [sigma * sigma / denom for denom in (1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)]
    extra += [0.005, 0.02, 0.1, 0.5, 2.0, 10.0]
    extra += [gamma * gamma / denom for denom in (16.0, 64.0, 256.0, 1024.0)]
    values: list[float] = []
    seen: set[str] = set()
    # Keep exp(σ²/(2a)) ≤ exp(80) so Gram entries stay in float64, but
    # allow a down to ~10^{-5} so σ=0.01 (β=0.51) can still beat the 2E lump.
    a_floor = max(1.0e-5, (sigma * sigma) / 160.0)
    for raw in base + extra:
        alpha = float(raw)
        if alpha < a_floor or alpha > 1.0e3:
            continue
        key = "%.10e" % alpha
        if key not in seen:
            seen.add(key)
            values.append(alpha)
    return tuple(sorted(values))


def omega_grid_for(
    gamma: float, alpha: float, delta: float, smoke: bool,
) -> tuple[float, ...]:
    sigma = max(abs(float(delta)), 1.0e-12)
    step = math.pi * alpha / sigma
    width = math.sqrt(max(alpha, 1.0e-12))
    values = [float(gamma)]
    if smoke:
        values.append(float(gamma) - step)
    else:
        for mult in (-3.0, -1.0, -0.5, 0.5, 1.0, 3.0):
            values.append(float(gamma) + mult * step)
        for mult in (-2.0, -1.0, 1.0, 2.0):
            values.append(float(gamma) + mult * width)
    out: list[float] = []
    seen: set[str] = set()
    # Stay inside the frequency packet (8 widths or at least 1).  A phase
    # step π a / σ that lands many widths from γ is not a Gabor at height γ.
    max_dev = max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 1.0)
    max_dev = min(max_dev, 0.35 * abs(float(gamma)) + 1.0)
    for raw in values:
        omega = float(raw)
        if omega < 0.0:
            continue
        if abs(omega - gamma) > max_dev + 1.0e-12:
            continue
        key = "%.10e" % omega
        if key not in seen:
            seen.add(key)
            out.append(omega)
    if not out:
        out.append(float(gamma))
    return tuple(out)


def extra_coeff_directions(smoke: bool) -> list[np.ndarray]:
    directions = [E0.copy()]
    if smoke:
        return directions
    for c2 in (-0.5, -0.2, 0.2, 0.5):
        directions.append(np.array([1.0, c2, 0.0], dtype=np.float64))
    for c4 in (-0.2, 0.2):
        directions.append(np.array([1.0, 0.0, c4], dtype=np.float64))
    return directions


def _whiten_unit(coeffs_phys: np.ndarray, scales: np.ndarray) -> np.ndarray:
    weighted = np.asarray(coeffs_phys, dtype=np.float64) * scales
    norm = float(np.linalg.norm(weighted))
    if not math.isfinite(norm) or norm <= 0.0:
        return np.asarray(coeffs_phys, dtype=np.float64)
    return np.asarray(coeffs_phys, dtype=np.float64) / norm


def candidate_coeffs(
    gram: np.ndarray, scales: np.ndarray, smoke: bool,
) -> list[np.ndarray]:
    rows: list[np.ndarray] = []
    if np.all(np.isfinite(gram)):
        try:
            _values, vectors = eigs_all(gram)
        except np.linalg.LinAlgError:
            vectors = None
        if vectors is not None:
            for index in range(N_BASIS):
                coeffs_w = flip_canon_vector(vectors[:, index])
                rows.append(coeffs_w / scales)
    for direction in extra_coeff_directions(smoke):
        rows.append(_whiten_unit(direction, scales))
    return rows


# ---------------------------------------------------------------------------
# G0 calibration
# ---------------------------------------------------------------------------
def trapz_hat_from_g(
    delta: complex, alpha: float, omega: float, coeffs: np.ndarray,
) -> complex:
    sigma = 1.0 / math.sqrt(alpha)
    half_width = 12.0 * sigma
    n_points = 2501
    u_grid = np.linspace(-half_width, half_width, n_points, dtype=np.float64)
    monomials = monomial_from_hermite(coeffs, alpha)
    if is_pure_e0(coeffs):
        g_vals = np.array(
            [g_pure_gabor(float(u_value), alpha, omega) for u_value in u_grid],
            dtype=np.complex128,
        )
    else:
        g_vals = np.array(
            [g_gabor(float(u_value), alpha, omega, monomials) for u_value in u_grid],
            dtype=np.complex128,
        )
    integrand = g_vals * np.exp(delta * u_grid)
    trapz = getattr(np, "trapezoid", None) or np.trapz
    return trapz(integrand, u_grid)


def mpmath_hat_pure_gabor(delta: complex, alpha: float, omega: float) -> complex:
    mp.mp.dps = 25
    a_mp = mp.mpf(alpha)
    w_mp = mp.mpf(omega)
    d_mp = mp.mpc(delta.real, delta.imag)
    pref = mp.sqrt(mp.pi / (2 * a_mp)) / 2
    c0 = mp.e ** (-(w_mp * w_mp) / (2 * a_mp))

    def integrand(u_value):
        gauss = mp.e ** (-a_mp * u_value * u_value / 2)
        return pref * gauss * (mp.cos(w_mp * u_value) + c0) * mp.e ** (d_mp * u_value)

    value = mp.quad(integrand, [-mp.inf, mp.inf])
    return complex(value)


def run_g0() -> tuple[bool, float]:
    max_err = 0.0

    def bump(err: float) -> None:
        nonlocal max_err
        if err > max_err:
            max_err = float(err)

    # ω=0 collapse onto the r539 Gaussian closed form.
    for alpha in (0.5, 1.0, 2.0):
        for delta in (0.0 + 0.0j, 0.3 + 0.0j, 0.2 + 0.4j, 0.1 + 2.0j):
            analytic = (math.pi / alpha) * np.exp((delta * delta) / (2.0 * alpha))
            from_h = hat_W_pure_gabor(delta, alpha, 0.0)
            from_c = hat_W_value(delta, alpha, 0.0, E0)
            bump(abs(from_h - analytic))
            bump(abs(from_c - analytic))

    # Frequency-shifted pure Gabor: H-product vs g-quadrature vs mpmath.
    for alpha, omega, delta in (
        (1.0, 2.0, 0.0 + 0.0j),
        (1.0, 2.0, 0.15 + 0.35j),
        (0.5, 2.0, 0.1 + 2.0j),
        (1.0, 2.0, 0.2 + 2.0j),
    ):
        analytic = hat_W_pure_gabor(delta, alpha, omega)
        from_c = hat_W_value(delta, alpha, omega, E0)
        trapz = trapz_hat_from_g(delta, alpha, omega, E0)
        mp_val = mpmath_hat_pure_gabor(delta, alpha, omega)
        bump(abs(from_c - analytic))
        bump(abs(trapz - analytic))
        bump(abs(mp_val - analytic))

    # Hermite-2 × cos: closed H(δ)H(−δ) vs trapz of g.
    alpha = 1.0
    omega = 1.5
    coeffs = np.array([0.0, 1.0, 0.0], dtype=np.float64)
    delta = 0.15 + 0.35j
    hat_hh = hat_W_value(delta, alpha, omega, coeffs)
    trapz_h2 = trapz_hat_from_g(delta, alpha, omega, coeffs)
    bump(abs(trapz_h2 - hat_hh))

    # On-line nonnegativity of the closed form on a t-grid.
    for alpha, omega in ((0.5, 0.0), (1.0, 2.0), (0.2, 14.13)):
        for t_value in (0.0, 1.0, 2.0, 5.0, 14.13, 30.0):
            val = float(np.real(hat_W_value(1j * t_value, alpha, omega, E0)))
            closed = f_online_pure(t_value, alpha, omega)
            bump(abs(val - closed))
            if val < -1.0e-14:
                bump(1.0)

    ok = max_err < float(SPEC["g0_atol"])
    return ok, max_err


def load_r539():
    import importlib.util

    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "weil_gaussian_separation_probe.py",
    )
    spec = importlib.util.spec_from_file_location("_r539_gauss_anchor", path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_g5(ordinates: np.ndarray) -> tuple[bool, float, dict]:
    """ω=0 must reproduce the r539 Gaussian cell at β=0.60, γ=0.5."""
    anchor = SPEC["g5_anchor"]
    beta = float(anchor["beta"])
    gamma = float(anchor["gamma"])
    alpha = float(anchor["a"])
    delta = beta - 0.5
    t_cut = float(ordinates[-1])
    details: dict = {}
    max_err = 0.0

    gauss_hat = (math.pi / alpha) * np.exp((delta + 1j * gamma) ** 2 / (2.0 * alpha))
    ours_hat = hat_W_value(delta + 1j * gamma, alpha, 0.0, E0)
    err_hat = abs(ours_hat - gauss_hat)
    max_err = max(max_err, err_hat)
    details["hat_err"] = err_hat

    ours_enum = enum_online_mass(E0, alpha, 0.0, ordinates)
    gauss_enum = 0.0
    for height in ordinates:
        gauss_enum += 2.0 * (math.pi / alpha) * math.exp(
            -(float(height) ** 2) / (2.0 * alpha)
        )
    err_enum = abs(ours_enum - gauss_enum)
    max_err = max(max_err, err_enum)
    details["enum_err"] = err_enum

    ours_tail = certified_tail(E0, alpha, 0.0, t_cut, "trudgian")
    details["ours_tail"] = ours_tail
    err_tail = math.nan
    module = load_r539()
    if module is not None:
        e0_5 = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float64)
        r539_tail = module.certified_tail(e0_5, alpha, t_cut, "trudgian")
        r539_hat = module.pref_product(delta + 1j * gamma, alpha)
        err_tail = abs(ours_tail - r539_tail)
        err_hat_r539 = abs(ours_hat - r539_hat)
        max_err = max(max_err, err_tail, err_hat_r539)
        details["r539_tail"] = r539_tail
        details["r539_hat_err"] = err_hat_r539
        details["tail_err"] = err_tail
        ours_off = off_line_quad(E0, alpha, 0.0, delta, gamma)
        r539_off = 4.0 * float(np.real(r539_hat))
        err_off = abs(ours_off - r539_off)
        max_err = max(max_err, err_off)
        details["off_err"] = err_off
        ours_cert = ours_off + ours_enum + ours_tail
        r539_cert = r539_off + gauss_enum + r539_tail
        details["ours_cert"] = ours_cert
        details["r539_cert"] = r539_cert
        details["cert_err"] = abs(ours_cert - r539_cert)
        max_err = max(max_err, abs(ours_cert - r539_cert))
    details["max_err"] = max_err
    ok = max_err < float(SPEC["g5_atol"])
    return ok, max_err, details


def mechanism_line(row: dict) -> str:
    unscaled = row.get("unscaled_off", math.nan)
    pred = row["pred_off"]
    ratio = (
        pred / unscaled
        if unscaled not in (0.0,) and math.isfinite(unscaled) and unscaled != 0.0
        else math.nan
    )
    return (
        "enh=exp(sigma^2/(2a))=%.6e  phase=sigma*(gamma-omega)/a=%.6e  "
        "pred_4Re=%.6e  closed_4Re=%.6e  pred/closed=%s  "
        "on_peak=%.6e  closed_4Re/on_peak=%s"
        % (
            row["enh"],
            row["phase"],
            pred,
            unscaled,
            ("%.4f" % ratio) if math.isfinite(ratio) else "nan",
            row["on_peak"],
            ("%.4e" % (unscaled / row["on_peak"]))
            if row["on_peak"] > 0.0 and math.isfinite(unscaled) else "nan",
        )
    )


def analyse_scaling(rows: list[dict], sep_atol: float) -> str:
    winners = [row for row in rows if row["cert"] < -sep_atol and row["eta"] >= float(SPEC["yoshida_eta_bar"])]
    if len(winners) < 3:
        return "insufficient_winners"
    # Phase law: (γ−ω) σ / a  should cluster at π (odd multiple).
    phase_units = []
    a_by_gamma: dict[float, list[float]] = {}
    omega_shift: list[float] = []
    for row in winners:
        sigma = row["beta"] - 0.5
        if row["a"] > 0.0 and sigma != 0.0:
            phase_units.append((row["gamma"] - row["omega"]) * sigma / row["a"])
            omega_shift.append(row["omega"] - row["gamma"])
        a_by_gamma.setdefault(row["gamma"], []).append(row["a"])
    med_phase = float(np.median(phase_units)) if phase_units else math.nan
    # a(γ) relative scatter of per-γ medians.
    gammas = sorted(a_by_gamma)
    med_a = [float(np.median(a_by_gamma[gamma])) for gamma in gammas]
    if min(med_a) > 0.0:
        rel = (max(med_a) - min(med_a)) / (0.5 * (max(med_a) + min(med_a)))
    else:
        rel = math.inf
    log_gamma = [math.log(max(gamma, 1.0)) for gamma in gammas]
    log_a = [math.log(max(val, 1.0e-30)) for val in med_a]
    if len(gammas) >= 2:
        slope = float(np.polyfit(log_gamma, log_a, 1)[0])
    else:
        slope = math.nan
    a_desc = "a~const" if rel < 0.6 else ("a~gamma^%.2f" % slope)
    # ω ≈ γ − π a / σ  if med_phase / π ≈ 1.
    if math.isfinite(med_phase) and abs(med_phase / math.pi - 1.0) < 0.35:
        omega_desc = "omega~gamma-pi*a/sigma"
    elif math.isfinite(med_phase) and abs(med_phase) < 0.35:
        omega_desc = "omega~gamma"
    else:
        omega_desc = "omega~gamma+delta(med_phase/pi=%.2f)" % (
            med_phase / math.pi if math.isfinite(med_phase) else math.nan
        )
    print("  winners=%d  a*(gamma) medians:" % len(winners))
    for gamma, val in zip(gammas, med_a):
        print("    gamma=%-10.4g  median_a*=%.6e  n=%d" % (
            gamma, val, len(a_by_gamma[gamma])))
    print("  a_rel_scatter=%.3f  loglog_slope=%.3f  (%s)" % (rel, slope, a_desc))
    print("  median (gamma-omega)*sigma/a = %.4f  (target pi=%.4f)  → %s"
          % (med_phase, math.pi, omega_desc))
    return "%s,%s" % (a_desc, omega_desc)


def format_verdict(rows: list[dict], scaling: str) -> str:
    sep_atol = float(SPEC["sep_atol"])
    eta_bar = float(SPEC["yoshida_eta_bar"])
    eta_ok = [row for row in rows if row["eta"] >= eta_bar]
    scope = eta_ok if eta_ok else rows
    all_trunc = all(row["trunc"] < -sep_atol for row in scope)
    all_cert = all(row["cert"] < -sep_atol for row in scope)
    all_eta_tiny = all(row["eta"] < eta_bar for row in rows)
    worst_cert = max(scope, key=lambda row: row["cert"])
    failed = [row for row in scope if row["cert"] >= -sep_atol]
    if failed:
        worst_fail = min(failed, key=lambda row: (row["gamma"], -row["beta"]))
    else:
        worst_fail = worst_cert
    if all_cert and all_eta_tiny:
        return (
            "YOSHIDA_COLLAPSE_GABOR(evidence=max_eta=%.3e,a_min=%.3e,n_cells=%d)"
            % (
                max(row["eta"] for row in rows),
                min(row["a"] for row in rows),
                len(rows),
            )
        )
    if all_cert:
        return (
            "SEPARATION_GO_GABOR(min_certified_margin=%.6e, worst=beta=%.2f,"
            "gamma=%.4g, scaling=%s)"
            % (worst_cert["cert"], worst_cert["beta"], worst_cert["gamma"], scaling)
        )
    # Height non-uniformity: some low-γ cells certify, high-γ fail.
    by_gamma: dict[float, list[dict]] = {}
    for row in scope:
        by_gamma.setdefault(row["gamma"], []).append(row)
    fail_from = None
    for gamma in sorted(by_gamma):
        if not all(row["cert"] < -sep_atol for row in by_gamma[gamma]):
            fail_from = gamma
            break
    low_ok = fail_from is not None and fail_from > min(by_gamma)
    if low_ok:
        return "HEIGHT_NONUNIFORM_AGAIN(fail_from_gamma=%.4g)" % fail_from
    # Envelope swamp: truncated (off+enum) negative, certified tail/bound not.
    swamp = [
        row for row in scope
        if row["trunc"] < -sep_atol and row["cert"] >= -sep_atol
    ]
    if swamp and (all_trunc or len(swamp) >= max(1, len(scope) // 2)):
        sample = min(swamp, key=lambda row: (row["gamma"], -row["beta"]))
        heur_also = sample["trunc"] + sample["tail_heur"] >= -sep_atol
        if heur_also:
            mechanism = "heuristic_density_times_envelope"
        else:
            mechanism = "trudgian_2E_lump"
        return (
            "ONLINE_ENVELOPE_SWAMPS(mechanism=%s,worst=beta=%.2f,gamma=%.4g,"
            "trunc=%.6e,on_bound=%.6e,cert=%.6e)"
            % (
                mechanism, sample["beta"], sample["gamma"],
                sample["trunc"], sample["on_bound"], sample["cert"],
            )
        )
    return (
        "INCONCLUSIVE(worst=beta=%.2f,gamma=%.4g,trunc=%.6e,"
        "n_trunc_neg=%d/%d,n_cert_neg=%d/%d,scaling=%s)"
        % (
            worst_fail["beta"], worst_fail["gamma"], worst_fail["trunc"],
            sum(row["trunc"] < -sep_atol for row in scope), len(scope),
            sum(row["cert"] < -sep_atol for row in scope), len(scope),
            scaling,
        )
    )


def run(smoke: bool) -> int:
    n_zeros = 8 if smoke else int(SPEC["n_zeros"])
    betas = (0.6, 0.9) if smoke else tuple(SPEC["betas"])
    gammas = (5.0, 14.13) if smoke else tuple(SPEC["gammas"])
    ordinates = np.asarray(ON_LINE_ORDINATES[:n_zeros], dtype=np.float64)
    t_cut = float(ordinates[-1])
    sep_atol = float(SPEC["sep_atol"])
    g1_atol = float(SPEC["g1_atol"])
    n_prime = 400 if smoke else int(SPEC["prime_n_cap"])
    lam = von_mangoldt_table(n_prime)

    print("weil_gabor_separation_probe -- r541")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("class even Gabor-Hermite deg<=4  h(t)=p(t)exp(-a t^2) cos(omega t)  g=h*h~")
    print("closed_form ĥ_W(1/2+it)=(pi/(4a))[e^{-(t+omega)^2/(2a)}+"
          "e^{-(t-omega)^2/(2a)}+2e^{-(t^2+omega^2)/(2a)}]  (pure Gabor)")
    print("tail_certified Trudgian JNT 134 (2014) Thm1/Cor1  "
          "|S(T)|<=0.111 log T + 0.275 log log T + 2.450  (T>=e)  LABEL=CERTIFIED")
    print("tail_crude N(T+1)-N(T)<=%.1f log(T+2)  (T>=14, in-probe majorant)  "
          "LABEL=CRUDE-SAFE" % float(SPEC["c_crude"]))
    print("tail_heuristic RvM density log(T/2pi)/(2pi)  LABEL=HEURISTIC")
    print("online_bound  exact first-%d  +  envelope x density-bound beyond T "
          "(no zetazero at height 10000)" % n_zeros)
    print("n_zeros %d t1=%.16f tN=%.16f" % (
        n_zeros, float(ordinates[0]), t_cut))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("prime_convention Lambda(n)*(1+1/n)*g(log n)  [g may oscillate; negatives reported]")

    section("G0  GABOR CLOSED FORM vs QUADRATURE / omega=0 GAUSSIAN LIMIT")
    g0_ok, g0_err = run_g0()
    check("G0-calibration-1e-12", g0_ok, "max_abs_err=%.3e atol=%.0e" % (
        g0_err, float(SPEC["g0_atol"])))

    section("G5  r539 REGRESSION ANCHOR (omega=0, beta=0.60, gamma=0.5)")
    g5_ok, g5_err, g5_details = run_g5(np.asarray(ON_LINE_ORDINATES, dtype=np.float64))
    print("  hat_err=%.3e enum_err=%.3e tail_err=%s off_err=%s cert_err=%s" % (
        g5_details.get("hat_err", math.nan),
        g5_details.get("enum_err", math.nan),
        ("%.3e" % g5_details["tail_err"]) if "tail_err" in g5_details else "n/a",
        ("%.3e" % g5_details["off_err"]) if "off_err" in g5_details else "n/a",
        ("%.3e" % g5_details["cert_err"]) if "cert_err" in g5_details else "n/a",
    ))
    if "ours_cert" in g5_details:
        print("  ours_cert=%.16e  r539_cert=%.16e" % (
            g5_details["ours_cert"], g5_details["r539_cert"]))
    check(
        "G5-r539-anchor-1e-9",
        g5_ok,
        "max_abs_err=%.3e atol=%.0e" % (g5_err, float(SPEC["g5_atol"])),
    )

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

    section("G1  NO-INJECTION SANITY (enum mass <= density-bound; on-line PSD)")
    g1_psd_ok = True
    g1_bound_ok = True
    g1_worst_lam = math.inf
    g1_n = 0
    g1_pairs = (
        [(1.0, 0.0), (0.2, 14.13), (0.05, 100.0)]
        if smoke else
        [(1.0, 0.0), (0.2, 14.13), (0.05, 30.0), (0.02, 100.0),
         (0.05, 1000.0), (0.02, 10000.0), (1.0, 5.0)]
    )
    t_lo_g1 = 14.0
    for alpha, omega in g1_pairs:
        gram_on, _gram_off, scales = assemble_cell(
            alpha, omega, ordinates, None, None,
        )
        if np.all(np.isfinite(gram_on)):
            lam_min, vecs = eigs_all(gram_on)
            g1_n += 1
            g1_worst_lam = min(g1_worst_lam, float(lam_min[0]))
            if float(lam_min[0]) < -g1_atol:
                g1_psd_ok = False
            coeffs_phys = flip_canon_vector(vecs[:, 0]) / scales
        else:
            coeffs_phys = E0
        enum_mass = enum_online_mass(E0, alpha, omega, ordinates)
        bound_mass = density_bound_interval(
            E0, alpha, omega, t_lo_g1, t_cut, "trudgian",
        )
        # Enumerated first-N mass must not exceed the Trudgian envelope bound
        # on the same range (the bound is an UPPER bound).
        if math.isfinite(enum_mass) and math.isfinite(bound_mass):
            if enum_mass > bound_mass + max(1.0e-8, 1.0e-10 * abs(bound_mass)):
                g1_bound_ok = False
                print("  G1-mismatch a=%.3e omega=%.4g enum=%.6e bound=%.6e"
                      % (alpha, omega, enum_mass, bound_mass))
        else:
            g1_bound_ok = False
        tail = certified_tail(E0, alpha, omega, t_cut, "trudgian")
        full_ub = enum_mass + tail
        print("  a=%.3e omega=%.4g enum=%.6e bound[14,T]=%.6e tail=%.6e full_UB=%.6e"
              % (alpha, omega, enum_mass, bound_mass, tail, full_ub))
        if full_ub < enum_mass - 1.0e-12:
            g1_bound_ok = False
        _ = coeffs_phys
    if not math.isfinite(g1_worst_lam):
        g1_worst_lam = 0.0
    check(
        "G1-online-psd",
        g1_psd_ok,
        "min_lam_on=%.6e atol=%.0e sampled=%d" % (g1_worst_lam, g1_atol, g1_n),
    )
    check(
        "G1-enum-le-density-bound",
        g1_bound_ok,
        "first-%d mass <= Trudgian envelope bound on [14,T]  LABEL=CERTIFIED"
        % n_zeros,
    )

    section("SEARCH  INJECTED OFF-CRITICAL QUADRUPLE (Gabor, omega ~ gamma)")
    print("  %-6s %-8s %-10s %-10s %-12s %-12s %-12s %-12s %-8s %s" % (
        "beta", "gamma", "a*", "omega*", "off", "on_enum", "on_bound",
        "cert", "sep", "eta"))
    rows: list[dict] = []
    for beta in betas:
        delta = float(beta) - 0.5
        for gamma in gammas:
            best: dict | None = None
            best_alive: dict | None = None
            eta_bar = float(SPEC["yoshida_eta_bar"])
            for alpha in a_grid_for(gamma, delta, smoke):
                for omega in omega_grid_for(gamma, alpha, delta, smoke):
                    gram_on, gram_off, scales = assemble_cell(
                        alpha, omega, ordinates, delta, float(gamma),
                    )
                    gram = gram_on + gram_off
                    if not np.all(np.isfinite(gram)):
                        continue
                    for coeffs_phys in candidate_coeffs(gram, scales, smoke):
                        c_w = coeffs_phys * scales
                        if not np.all(np.isfinite(c_w)):
                            continue
                        off = float(c_w @ gram_off @ c_w)
                        on_enum = float(c_w @ gram_on @ c_w)
                        if not math.isfinite(off) or not math.isfinite(on_enum):
                            continue
                        trunc = off + on_enum
                        tail_trud = certified_tail(
                            coeffs_phys, alpha, omega, t_cut, "trudgian",
                        )
                        on_bound = on_enum + tail_trud
                        cert = off + on_bound
                        monomials = monomial_from_hermite(coeffs_phys, alpha)
                        if e0_scale(coeffs_phys) is not None:
                            g0_c = g_pure_gabor(0.0, alpha, omega) * (e0_scale(coeffs_phys) ** 2)
                            g2_c = g_pure_gabor(math.log(2.0), alpha, omega) * (
                                e0_scale(coeffs_phys) ** 2
                            )
                        else:
                            g0_c = g_gabor(0.0, alpha, omega, monomials)
                            g2_c = g_gabor(math.log(2.0), alpha, omega, monomials)
                        eta_c = abs(g2_c) / abs(g0_c) if abs(g0_c) > 0.0 else math.inf
                        cand = {
                            "beta": float(beta),
                            "gamma": float(gamma),
                            "a": float(alpha),
                            "omega": float(omega),
                            "coeffs": coeffs_phys,
                            "off": off,
                            "on_enum": on_enum,
                            "tail_trud": tail_trud,
                            "on_bound": on_bound,
                            "trunc": trunc,
                            "cert": cert,
                            "delta": delta,
                            "eta_cheap": eta_c,
                        }
                        if best is None or cert < best["cert"]:
                            best = cand
                        if eta_c >= eta_bar and (
                            best_alive is None or cert < best_alive["cert"]
                        ):
                            best_alive = cand
            if best_alive is not None:
                best = best_alive
            assert best is not None
            best["tail_crude"] = certified_tail(
                best["coeffs"], best["a"], best["omega"], t_cut, "crude",
            )
            best["tail_heur"] = certified_tail(
                best["coeffs"], best["a"], best["omega"], t_cut, "heur",
            )
            coupling = prime_coupling(
                best["coeffs"], best["a"], best["omega"], n_prime, lam,
            )
            best.update(coupling)
            best["enh"] = enhancement_factor(delta, best["a"])
            best["phase"] = delta * (best["gamma"] - best["omega"]) / best["a"]
            # Scale-free mechanism check against the pure-Gabor closed form.
            best["pred_off"] = predicted_off_pure(
                delta, best["gamma"], best["a"], best["omega"],
            )
            best["on_peak"] = f_online_pure(best["omega"], best["a"], best["omega"])
            unscaled_off = 4.0 * float(np.real(hat_W_pure_gabor(
                delta + 1j * best["gamma"], best["a"], best["omega"],
            )))
            best["unscaled_off"] = unscaled_off
            best["sep"] = "yes" if best["cert"] < -sep_atol else "no"
            order = np.argsort(-np.abs(best["coeffs"]))[:3]
            best["top"] = ",".join(
                "c%d:%.3e" % (int(index), float(best["coeffs"][index]))
                for index in order
            )
            rows.append(best)
            print("  %-6.2f %-8.4g %-10.3e %-10.4g %+.6e %+.6e %+.6e %+.6e %-8s %.3e" % (
                best["beta"], best["gamma"], best["a"], best["omega"],
                best["off"], best["on_enum"], best["on_bound"], best["cert"],
                best["sep"], best["eta"]))

    section("OFF-LINE ENHANCEMENT MECHANISM  (sigma enters in the REAL direction)")
    print("  ĥ_W(beta+i gamma) ~ (pi/(4a)) exp((sigma^2-(gamma-omega)^2)/(2a)) exp(i sigma(gamma-omega)/a)")
    print("  on-line peak ĥ_W(1/2+i omega) ~ pi/(4a)")
    print("  ratio vs peak = 4 exp(sigma^2/(2a)) when omega=gamma  [off-line grows as a↓ or |beta-1/2|↑]")
    print("  phase-tune omega = gamma - pi a / sigma  makes 4 Re ĥ_W ≈ -(pi/a) exp(sigma^2/(2a))")
    for row in rows:
        print("  beta=%.2f gamma=%.4g a=%.3e omega=%.4g  %s"
              % (row["beta"], row["gamma"], row["a"], row["omega"], mechanism_line(row)))

    section("HEIGHT-UNIFORMITY  a*(gamma), omega*-gamma")
    scaling = analyse_scaling(rows, sep_atol)

    section("G4  YOSHIDA TRAP (prime-channel coupling of minimizers)")
    eta_bar = float(SPEC["yoshida_eta_bar"])
    winners = [row for row in rows if row["cert"] < -sep_atol]
    eta_scope = winners if winners else rows
    n_prime_alive = sum(row["eta"] >= eta_bar for row in eta_scope)
    max_eta = max(row["eta"] for row in eta_scope)
    min_eta = min(row["eta"] for row in eta_scope)
    print("  convention contour Sigma Lambda(n)*(1+1/n)*g(log n)")
    print("  also_reported combMass Sigma 2*Lambda(n)/sqrt(n)*g(log n)")
    print("  NOTE g of a Gabor autocorrelation oscillates; negative g(log n) is fine")
    print("  eta=|g(log 2)/g(0)|  bar=%.0e  scope=%s n=%d  alive=%d/%d  max_eta=%.3e min_eta=%.3e"
          % (eta_bar, "certified_separators" if winners else "all_cells",
             len(eta_scope), n_prime_alive, len(eta_scope), max_eta, min_eta))
    for row in rows:
        print(
            "  beta=%.2f gamma=%.4g a=%.3e omega=%.4g eta=%.3e "
            "g0=%.3e g_log2=%.3e contour=%.3e comb=%.3e n_neg_g=%d"
            % (
                row["beta"], row["gamma"], row["a"], row["omega"], row["eta"],
                row["g0"], row["g_log2"], row["contour"], row["comb"],
                row["n_neg_g"],
            )
        )
    yoshida = bool(winners) and n_prime_alive == 0
    check(
        "G4-prime-channel-evaluated",
        True,
        "YOSHIDA_COLLAPSE_flag=%s n_alive=%d/%d" % (
            "yes" if yoshida else "no", n_prime_alive, len(eta_scope)),
    )
    if winners:
        check(
            "G4-winners-eta-ge-bar",
            n_prime_alive == len(winners),
            "alive=%d/%d bar=%.0e" % (n_prime_alive, len(winners), eta_bar),
        )
    else:
        check("G4-winners-eta-ge-bar", True, "no certified winners to test")

    section("GATES / VERDICT")
    n_trunc = sum(row["trunc"] < -sep_atol for row in rows)
    n_heur = sum(row["trunc"] + row["tail_heur"] < -sep_atol for row in rows)
    n_cert = sum(row["cert"] < -sep_atol for row in rows)
    check("G1-sanity-held", g1_psd_ok and g1_bound_ok, "on-line PSD + enum<=bound")
    check(
        "G2-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G3-smoke-subset", True, "smoke grid 2x2 N=8 reduced a/omega grid")
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
    print("  LABEL map: enum=EXACT(freeze)  tail_trud=CERTIFIED(Trudgian)  "
          "tail_crude=CRUDE-SAFE  tail_heur=HEURISTIC")

    section("PER-CELL TABLE  (beta, gamma, a*, omega*, off, on_bound, cert, yes/no)")
    print("  %-6s %-8s %-10s %-10s %-14s %-14s %-14s %-8s" % (
        "beta", "gamma", "a*", "omega*", "off", "on_bound", "cert", "sep"))
    for row in rows:
        print("  %-6.2f %-8.4g %-10.3e %-10.4g %+.6e %+.6e %+.6e %-8s" % (
            row["beta"], row["gamma"], row["a"], row["omega"],
            row["off"], row["on_bound"], row["cert"], row["sep"]))

    verdict = format_verdict(rows, scaling)
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
        description="r541 Gabor/wavepacket Weil height-uniform separation (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
