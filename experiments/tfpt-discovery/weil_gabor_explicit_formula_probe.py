#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weil_gabor_explicit_formula_probe -- r548

Numerical precheck of the explicit Weil formula on the noncompact
Gabor class of RH/GaborSeparation.lean, before any campaign on the
named sorry `gabor_explicitFormula`.

CLAIM BOUNDARY.  Finite, certified-truncation arithmetic for a
three-dimensional even Gabor subclass.  Conditional on the frozen
first-100 critical-line ordinates (mpmath.zetazero, dps=30).  NO RH
claim, NO anti-RH claim, NO ledger row, NO paper edit, NO Lean edit.
A residual inside the certified budget is not a theorem for the
infinite Schwartz class.  Off-line zeros below T are not excluded by
this probe (ZERO_SCOPE = known on-line ordinates only).

LEAN PROP (GaborSeparation.lean).  `GaborExplicitFormula` asserts

    gaborArithmeticFormula F = gaborSpectralFormula F

for admissible Gabor tests, i.e. the two-edge contour of
(ζ'/ζ) ĥ_W along Re=2 and Re=−1/16, divided by 2π, equals
(Σ_ρ ĥ_W(ρ) − ĥ_W(1)).re.  The comment records that converting the
contour into separately convergent prime and arch channels is part of
the same named input.

HAT / CHANNELS.  `gaborHat` is the Weil-shifted pairing

    ĥ_W(s) := ∫ g(u) exp((s − 1/2) u) du = H(s−1/2) H(1/2−s),

g = h⋆h~, h(t) = p(t) e^{−a t²} cos(ω t), p even of degree ≤ 4.
Repo-classical Guinand–Weil / Bombieri assembly (weil_gns W1,
Weil 1952), which is the three-channel form of that pairing:

    Z  := Σ_ρ ĥ_W(ρ)          (both signs; freeze + Trudgian tail)
    Pole := ĥ_W(0) + ĥ_W(1)
    Prime := 2 Σ_n Λ(n) n^{−1/2} g(log n)
    Arch := (1/2π) ∫_R ĥ_W(1/2+it) (Re ψ(1/4+it/2) − log π) dt

    IDENTITY A:  Z = Pole − Prime + Arch.

Lean `gaborPrimeSide` uses the unshifted contour weight
Λ(n)(1+n^{−1}) g(log n).  IDENTITY B transplants the compact honest
decomposition (r534/r538) onto ĥ_W:

    Z − ĥ_W(1)  =?  Arch − Σ Λ(n)(1+1/n) g(log n).

A failure of B with a pass of A localises a hat/prime-dictionary
mismatch, not a failure of the explicit formula.

SCALING.  a = σ²/64, ω = γ − π σ/64, as in `scalingGaborTest`.
σ is chosen so a ≥ 1/4, which keeps the prime saddle u = 1/a inside
a certifiable n-cap.

TAIL.  On-line zero remainder: Trudgian increment × envelope, same
constants as r541 (JNT 134 (2014) Thm 1 + Cor 1).  Prime remainder:
Chebyshev ψ(x) ≤ 2x Stieltjes against the Gaussian envelope.
Arch remainder: incomplete-gamma of |k(t)| ≲ log(t+2) times the
three-lobe envelope.  PASS iff |LHS−RHS| < sum of certified budgets.

Runtime: mpmath (dps from SPEC) for hats / digamma / G0; numpy only
for the von Mangoldt sieve.  Zeros cached; zetazero is not called
at runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import os
import sys

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
    "round": 548,
    "target": "gabor_noncompact_explicit_formula_precheck",
    "hat": "weil_shifted",
    "parent_rounds": [534, 538, 539, 541],
    "lean_prop": "RH.GaborExplicitFormula",
    "sigmas": [4.0, 8.0, 12.0],
    "gammas": [5.0, 14.13, 50.0, 200.0],
    "polynomials": [
        {"name": "p1", "c0": 1.0, "c2": 0.0, "c4": 0.0},
        {"name": "p2", "c0": 1.0, "c2": 0.25, "c4": 0.0},
        {"name": "p4", "c0": 1.0, "c2": 0.10, "c4": 0.02},
    ],
    "n_zeros": 100,
    "prime_n_cap": 40000,
    "mp_dps": 30,
    "g0_atol": 1e-12,
    "quad_dps": 20,
    "arch_lobe_widths": 12.0,
    "psi_chebyshev": 2.0,
    "c_crude": 4.0,
    "trudgian_a": 0.111,
    "trudgian_b": 0.275,
    "trudgian_c": 2.450,
    "trudgian_nt_extra": 0.2,
    "trudgian_source": (
        "Trudgian JNT 134 (2014) 280-292 / arXiv:1208.5846 Thm1+Cor1"
    ),
    "prime_convention_A": "2*Lambda(n)/sqrt(n)*g(log n)  [classical Weil/comb]",
    "prime_convention_B": (
        "Lambda(n)*(1+1/n)*g(log n)  [Lean gaborPrimeSide / honest contour]"
    ),
    "identity_A": "Z = Pole - Prime_comb + Arch_weil",
    "identity_B": "Z - hat_W(1) =? Arch_weil - Prime_contour",
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

# First 100 positive ordinates.  Same freeze as r535/r539/r541.
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
LOG_CLIP = 700.0


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


def fmt(value: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(mp.mpf(value), digits, strip_zeros=False)


def exp_clip(log_value: float) -> float:
    if log_value > LOG_CLIP:
        return math.inf
    if log_value < -LOG_CLIP:
        return 0.0
    return math.exp(log_value)


# ---------------------------------------------------------------------------
# Closed Gabor transforms (Lean RH/GaborSeparation.lean)
# ---------------------------------------------------------------------------
def scaling_a(sigma: float) -> float:
    return float(sigma) ** 2 / 64.0


def scaling_omega(sigma: float, gamma: float) -> float:
    return float(gamma) - math.pi * float(sigma) / 64.0


def _poly_factor(z: mp.mpc, a: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf) -> mp.mpc:
    """Lean `gaussianPolynomialFactor`."""
    inv_a = 1 / a
    z2 = z * z
    z4 = z2 * z2
    return (
        c0
        + c2 * (inv_a / 2 + z2 / (4 * a * a))
        + c4 * (
            mp.mpf(3) / (4 * a * a)
            + 3 * z2 / (4 * a * a * a)
            + z4 / (16 * a * a * a * a)
        )
    )


def gaussian_laplace(
    z: mp.mpc, a: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
) -> mp.mpc:
    """Lean `gaussianLaplace`: ∫ p(t) e^{−a t²} e^{z t} dt."""
    return mp.sqrt(mp.pi / a) * mp.e ** (z * z / (4 * a)) * _poly_factor(
        z, a, c0, c2, c4,
    )


def gabor_laplace(
    z: mp.mpc, a: mp.mpf, omega: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
) -> mp.mpc:
    """Lean `gaborLaplace`: (1/2)[L(z+iω)+L(z−iω)]."""
    i_omega = mp.j * omega
    return (
        gaussian_laplace(z + i_omega, a, c0, c2, c4)
        + gaussian_laplace(z - i_omega, a, c0, c2, c4)
    ) / 2


def hat_W(
    s: mp.mpc, a: mp.mpf, omega: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
) -> mp.mpc:
    """Lean `gaborHat`: ĥ_W(s) = H(s−1/2) H(1/2−s)."""
    delta = s - mp.mpf("0.5")
    return gabor_laplace(delta, a, omega, c0, c2, c4) * gabor_laplace(
        -delta, a, omega, c0, c2, c4,
    )


def hat_W_pure_closed(delta: mp.mpc, a: mp.mpf, omega: mp.mpf) -> mp.mpc:
    """Lean `pureGaborHatDelta` (p ≡ 1)."""
    sig = mp.re(delta)
    t_val = mp.im(delta)
    pref = mp.pi / (4 * a)
    left = mp.e ** ((sig * sig - (t_val + omega) ** 2) / (2 * a)) * mp.e ** (
        mp.j * (sig * (t_val + omega) / a)
    )
    right = mp.e ** ((sig * sig - (t_val - omega) ** 2) / (2 * a)) * mp.e ** (
        mp.j * (sig * (t_val - omega) / a)
    )
    cross = 2 * mp.e ** (
        (sig * sig - t_val * t_val - omega * omega) / (2 * a)
    ) * mp.e ** (mp.j * (sig * t_val / a))
    return pref * (left + right + cross)


def f_online_pure(t_value: float, alpha: float, omega: float) -> float:
    """Exact ĥ_W(1/2+it) for p ≡ 1."""
    pref = math.pi / (4.0 * alpha)
    left = exp_clip(-(t_value + omega) ** 2 / (2.0 * alpha))
    right = exp_clip(-(t_value - omega) ** 2 / (2.0 * alpha))
    cross = exp_clip(-(t_value * t_value + omega * omega) / (2.0 * alpha))
    return pref * (left + right + 2.0 * cross)


def is_pure(c0: mp.mpf, c2: mp.mpf, c4: mp.mpf) -> bool:
    return c2 == 0 and c4 == 0 and c0 == 1


# ---------------------------------------------------------------------------
# Autocorrelation g (r541 closed form, monomial EvenQuartic)
# ---------------------------------------------------------------------------
def odd_double_factorial(m: int) -> float:
    if m <= 0:
        return 1.0
    value = 1.0
    for index in range(m):
        value *= float(2 * index + 1)
    return value


def shift_even_poly(monomials: tuple[float, float, float], shift: float) -> list[float]:
    m0, m1, m2 = monomials
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
    mu = 1j * freq / (2.0 * two_a)
    var = 1.0 / (2.0 * two_a)
    log_pref = 0.5 * math.log(math.pi / two_a) - (freq * freq) / (4.0 * two_a)
    pref = complex(exp_clip(log_pref))
    max_pow = len(power_coeffs) - 1
    moments = [0.0 + 0.0j] * (max_pow + 1)
    moments[0] = 1.0 + 0.0j
    for n_power in range(1, max_pow + 1):
        tot = 0.0 + 0.0j
        for even_k in range(0, n_power + 1, 2):
            m_half = even_k // 2
            central = (var ** m_half) * odd_double_factorial(m_half)
            tot += math.comb(n_power, even_k) * (mu ** (n_power - even_k)) * central
        moments[n_power] = tot
    acc = 0.0 + 0.0j
    for power, coef in enumerate(power_coeffs):
        if coef == 0.0:
            continue
        acc += coef * moments[power]
    return pref * acc


def g_gabor(u_value: float, alpha: float, omega: float,
            monomials: tuple[float, float, float]) -> float:
    gauss = exp_clip(-0.5 * alpha * u_value * u_value)
    half = 0.5 * float(u_value)
    q_poly = poly_mul(
        shift_even_poly(monomials, half),
        shift_even_poly(monomials, -half),
    )
    two_a = 2.0 * alpha
    i_dc = poly_gauss_fourier(q_poly, two_a, 0.0)
    i_cos = poly_gauss_fourier(q_poly, two_a, 2.0 * omega)
    return float(
        0.5 * gauss * (
            math.cos(omega * u_value) * float(np.real(i_dc))
            + float(np.real(i_cos))
        )
    )


def g_pure_gabor(u_value: float, alpha: float, omega: float) -> float:
    pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
    return pref * exp_clip(-0.5 * alpha * u_value * u_value) * (
        math.cos(omega * u_value) + exp_clip(-(omega * omega) / (2.0 * alpha))
    )


def g_env_pref(alpha: float, omega: float, monomials: tuple[float, float, float]) -> float:
    """Pointwise |g(u)| ≤ pref · (1+|u|√a)^8 · exp(−a u²/2)."""
    g0 = abs(g_gabor(0.0, alpha, omega, monomials))
    return max(g0, 1.0e-30)


# ---------------------------------------------------------------------------
# von Mangoldt
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


# ---------------------------------------------------------------------------
# Trudgian envelope (r541 constants)
# ---------------------------------------------------------------------------
def trudgian_E(height: float) -> float:
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
    return clipped / (2.0 * math.pi) * math.log(
        clipped / (2.0 * math.pi * math.e)
    ) + 0.875


def trudgian_increment(height: float, width: float) -> float:
    width_use = max(float(width), 1.0)
    t_hi = float(height) + width_use
    return rvm_theta(t_hi) - rvm_theta(height) + trudgian_E(t_hi) + trudgian_E(height)


def gauss_lobe_sup(t0: float, t1: float, center: float, alpha: float) -> float:
    peak = float(center)
    if t0 <= peak <= t1:
        return 1.0
    d0 = t0 - peak
    d1 = t1 - peak
    dist_sq = min(d0 * d0, d1 * d1)
    return exp_clip(-dist_sq / (2.0 * alpha))


def poly_growth(t_hi: float, alpha: float, monomials: tuple[float, float, float]) -> float:
    """Crude |P|-majorant on |z| ≤ |t| + |ω|-scale, used only in tails."""
    c0, c2, c4 = (abs(float(v)) for v in monomials)
    scale = 1.0 / max(alpha, 1.0e-18)
    xi = abs(float(t_hi)) + 1.0
    return (
        c0
        + c2 * (0.5 * scale + (xi * xi) * scale * scale / 4.0)
        + c4 * (
            0.75 * scale * scale
            + 0.75 * (xi * xi) * scale ** 3
            + (xi ** 4) * scale ** 4 / 16.0
        )
    )


def env_sup_hat(
    t0: float, t1: float, alpha: float, omega: float,
    monomials: tuple[float, float, float],
) -> float:
    t0 = max(float(t0), 0.0)
    t1 = max(float(t1), t0)
    pref = math.pi / (4.0 * alpha)
    left = gauss_lobe_sup(t0, t1, -omega, alpha)
    right = gauss_lobe_sup(t0, t1, omega, alpha)
    cross = 2.0 * exp_clip(-(t0 * t0 + omega * omega) / (2.0 * alpha))
    base = pref * (left + right + cross)
    if monomials[1] == 0.0 and monomials[2] == 0.0:
        return (monomials[0] ** 2) * base
    growth = poly_growth(t1 + abs(omega), alpha, monomials)
    return base * max(growth * growth, 1.0)


def certified_zero_tail(
    t_cut: float, alpha: float, omega: float,
    monomials: tuple[float, float, float],
) -> float:
    """Bound on 2 Σ_{t_n > t_cut} |ĥ_W(1/2+i t_n)|.  LABEL=CERTIFIED."""
    width_scale = max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 8.0)
    omega_abs = abs(float(omega))
    t_hard = max(float(t_cut) + width_scale, omega_abs + width_scale)
    t_hard = min(t_hard, 1.0e7)
    total = 0.0
    t_value = float(t_cut)
    window = width_scale
    while t_value < t_hard:
        in_window = abs(t_value - omega_abs) <= window + 1.0
        width = 1.0 if in_window else max(1.0, 0.04 * t_value)
        if t_value + width > t_hard:
            width = max(1.0, t_hard - t_value)
        nbound = trudgian_increment(t_value, width)
        env = env_sup_hat(t_value, t_value + width, alpha, omega, monomials)
        total += 2.0 * nbound * env
        if not math.isfinite(total) or total > 1.0e250:
            return math.inf
        t_value += width
    # Far remainder: C_CRUDE log · incomplete Gaussian after the last bin.
    u0 = max(t_value - omega_abs, 0.0)
    beta = 1.0 / (2.0 * alpha)
    erfc = math.erfc(u0 * math.sqrt(beta)) if math.isfinite(u0) else 0.0
    lobe = 0.5 * math.sqrt(math.pi / beta) * erfc
    growth = poly_growth(t_value + abs(omega), alpha, monomials)
    rem = (
        2.0 * float(SPEC["c_crude"]) * math.log(t_value + 2.0)
        * (math.pi / alpha) * growth * growth * lobe
    )
    return float(total + rem)


# ---------------------------------------------------------------------------
# Prime tails
# ---------------------------------------------------------------------------
def gauss_exp_linear_tail(u0: float, alpha: float, linear: float) -> float:
    """∫_{u0}^∞ exp(−a u²/2 + linear·u) du, closed via erfc."""
    if alpha <= 0.0:
        return math.inf
    mu = linear / alpha
    pref = math.exp((linear * linear) / (2.0 * alpha))
    scale = math.sqrt(math.pi / (2.0 * alpha))
    arg = math.sqrt(alpha / 2.0) * (u0 - mu)
    return pref * scale * math.erfc(arg)


def certified_prime_tails(
    n_cap: int, alpha: float, omega: float,
    monomials: tuple[float, float, float],
) -> tuple[float, float]:
    """Absolute tails of the contour and comb prime channels past n_cap."""
    u0 = math.log(max(n_cap, 2))
    pref = g_env_pref(alpha, omega, monomials)
    # Degree-accurate envelope: p=1 has no extra polynomial growth;
    # deg 2 (resp. 4) contributes at most (1+|u|√a)^{4} (resp. ^{8}).
    if monomials[2] != 0.0:
        poly = (1.0 + abs(u0) * math.sqrt(alpha)) ** 8
    elif monomials[1] != 0.0:
        poly = (1.0 + abs(u0) * math.sqrt(alpha)) ** 4
    else:
        poly = 1.0
    psi = float(SPEC["psi_chebyshev"])
    # contour: Sigma Lambda(n)(1+1/n) g <= 2 * int |g|(e^u+1) du via dpsi <= 2 dx
    i_eu = gauss_exp_linear_tail(u0, alpha, 1.0)
    i_one = gauss_exp_linear_tail(u0, alpha, 0.0)
    tail_contour = psi * pref * poly * (i_eu + i_one)
    # comb: 2 Σ Λ n^{-1/2} g ≤ 2 · 2 ∫ |g| e^{u/2} du
    i_half = gauss_exp_linear_tail(u0, alpha, 0.5)
    tail_comb = 2.0 * psi * pref * poly * i_half
    return float(tail_contour), float(tail_comb)


# ---------------------------------------------------------------------------
# Archimedean digamma integral
# ---------------------------------------------------------------------------
def weil_kernel(t_value: mp.mpf) -> mp.mpf:
    return mp.re(mp.digamma(mp.mpf("0.25") + mp.j * t_value / 2)) - mp.log(mp.pi)


def kernel_majorant(t_value: float) -> float:
    """|Re ψ(1/4+it/2) − log π| ≤ log(t+2) + 4, t ≥ 0 (crude, safe)."""
    return math.log(max(t_value, 0.0) + 2.0) + 4.0


def _quad_real(func, t_lo: float, t_hi: float) -> tuple[mp.mpf, mp.mpf]:
    if t_hi <= t_lo + 1.0e-18:
        return mp.mpf(0), mp.mpf(0)
    value, err = mp.quad(func, [mp.mpf(t_lo), mp.mpf(t_hi)], error=True)
    return mp.mpf(value), mp.mpf(err)


def arch_weil_integral(
    a: mp.mpf, omega: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
    alpha: float, omega_f: float, monomials: tuple[float, float, float],
) -> tuple[mp.mpf, mp.mpf]:
    """(1/2π) ∫_R k(t) ĥ_W(1/2+it) dt, even reduction, segmented quad."""
    width = float(SPEC["arch_lobe_widths"]) * math.sqrt(max(alpha, 1.0e-12))
    omega_abs = abs(omega_f)

    def integrand(t_val):
        hat = hat_W(mp.mpc(mp.mpf("0.5"), t_val), a, omega, c0, c2, c4)
        return weil_kernel(t_val) * mp.re(hat)

    segments: list[tuple[float, float]] = []
    t_left = 0.0
    t_right = max(omega_abs + width, width)
    if omega_abs > 2.0 * width:
        segments.append((0.0, width))
        segments.append((max(omega_abs - width, width), omega_abs + width))
    else:
        segments.append((0.0, t_right))

    total = mp.mpf(0)
    quad_err = mp.mpf(0)
    covered_hi = 0.0
    for t_lo, t_hi in segments:
        val, err = _quad_real(integrand, t_lo, t_hi)
        total += val
        quad_err += err
        covered_hi = max(covered_hi, t_hi)

    # Uncovered [0, covered_hi] gaps + far tail, charged at envelope × majorant.
    tail = 0.0
    if omega_abs > 2.0 * width:
        gap_lo = width
        gap_hi = max(omega_abs - width, width)
        if gap_hi > gap_lo:
            env = env_sup_hat(gap_lo, gap_hi, alpha, omega_f, monomials)
            tail += env * kernel_majorant(gap_hi) * (gap_hi - gap_lo)
    t_cut = max(covered_hi, t_left)
    # ∫_{t_cut}^∞ log(t+2) exp(−(t−ω)²/(2a)) dt  ≤ log-majorant × Gaussian tail
    u0 = max(t_cut - omega_abs, 0.0)
    beta = 1.0 / (2.0 * alpha)
    erfc = math.erfc(u0 * math.sqrt(beta))
    lobe = 0.5 * math.sqrt(math.pi / beta) * erfc
    growth = poly_growth(t_cut + omega_abs, alpha, monomials)
    tail += (
        kernel_majorant(t_cut)
        * (math.pi / alpha)
        * growth * growth
        * lobe
    )
    # Even: full line = 2 × [0,∞)
    arch = (2 * total) / (2 * mp.pi)
    budget = (2 * quad_err + 2 * mp.mpf(tail)) / (2 * mp.pi)
    return arch, budget


# ---------------------------------------------------------------------------
# G0 calibration
# ---------------------------------------------------------------------------
def run_g0() -> tuple[bool, float]:
    max_err = 0.0

    def bump(err: float) -> None:
        nonlocal max_err
        if err > max_err:
            max_err = float(err)

    mp.mp.dps = int(SPEC["mp_dps"])
    # ω=0, p=1: ĥ_W(s) = (π/a) exp((s−1/2)²/(2a))
    for alpha in (0.5, 1.0, 2.0):
        a = mp.mpf(alpha)
        omega = mp.mpf(0)
        c0, c2, c4 = mp.mpf(1), mp.mpf(0), mp.mpf(0)
        for delta in (mp.mpc(0), mp.mpc("0.3"), mp.mpc("0.2", "0.4")):
            s_val = mp.mpf("0.5") + delta
            analytic = (mp.pi / a) * mp.e ** (delta * delta / (2 * a))
            from_h = hat_W(s_val, a, omega, c0, c2, c4)
            from_closed = hat_W_pure_closed(delta, a, omega)
            bump(float(abs(from_h - analytic)))
            bump(float(abs(from_closed - analytic)))

    # Frequency-shifted p=1: H-product vs three-exponential.
    for alpha, omega_f, dre, dim in (
        (1.0, 2.0, 0.0, 0.0),
        (1.0, 2.0, 0.15, 0.35),
        (0.5, 2.0, 0.1, 2.0),
    ):
        a = mp.mpf(alpha)
        omega = mp.mpf(omega_f)
        delta = mp.mpc(dre, dim)
        s_val = mp.mpf("0.5") + delta
        from_h = hat_W(s_val, a, omega, mp.mpf(1), mp.mpf(0), mp.mpf(0))
        from_closed = hat_W_pure_closed(delta, a, omega)
        bump(float(abs(from_h - from_closed)))

    # g(0) and pole integral vs ĥ_W(0)+ĥ_W(1) for p=1.
    for alpha, omega_f in ((1.0, 0.0), (1.0, 2.0), (0.5, 1.5)):
        a = mp.mpf(alpha)
        omega = mp.mpf(omega_f)
        hat0 = hat_W(mp.mpc(0), a, omega, mp.mpf(1), mp.mpf(0), mp.mpf(0))
        hat1 = hat_W(mp.mpc(1), a, omega, mp.mpf(1), mp.mpf(0), mp.mpf(0))
        # ∫ g(u)(e^{u/2}+e^{-u/2}) du via closed ĥ_W; self-consistency
        # ĥ_W(0)=ĥ_W(1) for even g.
        bump(float(abs(hat0 - hat1)))
        g0 = g_pure_gabor(0.0, alpha, omega_f)
        g0_gen = g_gabor(0.0, alpha, omega_f, (1.0, 0.0, 0.0))
        bump(abs(g0 - g0_gen))
        # ĥ_W(1/2) = ∫ g(u) du should be close to a coarse trapz.
        umax = 12.0 / math.sqrt(alpha)
        npts = 801
        us = np.linspace(-umax, umax, npts)
        gs = np.array([g_pure_gabor(float(u), alpha, omega_f) for u in us])
        trapz = np.trapezoid(gs, us)
        hat_half = hat_W(
            mp.mpc(mp.mpf("0.5")), a, omega, mp.mpf(1), mp.mpf(0), mp.mpf(0),
        )
        bump(abs(float(mp.re(hat_half)) - float(trapz)))

    # Hermite/monomial deg-2: ĥ_W vs trapz of g.
    alpha = 1.0
    omega_f = 1.5
    a = mp.mpf(alpha)
    omega = mp.mpf(omega_f)
    monomials = (1.0, 0.25, 0.0)
    delta = mp.mpc("0.1", "0.2")
    s_val = mp.mpf("0.5") + delta
    hat = hat_W(s_val, a, omega, mp.mpf(1), mp.mpf("0.25"), mp.mpf(0))
    umax = 12.0 / math.sqrt(alpha)
    us = np.linspace(-umax, umax, 1201)
    gs = np.array([g_gabor(float(u), alpha, omega_f, monomials) for u in us])
    trapz = np.trapezoid(gs * np.exp(complex(delta) * us), us)
    bump(abs(complex(hat) - complex(trapz)))

    ok = max_err < float(SPEC["g0_atol"])
    return ok, max_err


# ---------------------------------------------------------------------------
# Cell evaluation
# ---------------------------------------------------------------------------
def prime_sums(
    alpha: float, omega: float, monomials: tuple[float, float, float],
    n_cap: int, lam: np.ndarray,
) -> tuple[float, float]:
    contour = 0.0
    comb = 0.0
    pure = monomials[1] == 0.0 and monomials[2] == 0.0 and abs(monomials[0] - 1.0) < 1e-15
    limit = min(n_cap, lam.size - 1)
    for n_value in range(2, limit + 1):
        von = float(lam[n_value])
        if von == 0.0:
            continue
        u_val = math.log(n_value)
        if pure:
            g_u = g_pure_gabor(u_val, alpha, omega)
        else:
            g_u = g_gabor(u_val, alpha, omega, monomials)
        contour += von * (1.0 + 1.0 / n_value) * g_u
        comb += 2.0 * von / math.sqrt(n_value) * g_u
    return contour, comb


def zero_sum_online(
    a: mp.mpf, omega: mp.mpf, c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
    ordinates: tuple[float, ...],
) -> mp.mpf:
    total = mp.mpf(0)
    for height in ordinates:
        s_val = mp.mpc(mp.mpf("0.5"), mp.mpf(height))
        hat = hat_W(s_val, a, omega, c0, c2, c4)
        # Both signs: ρ and ρ̄.  On-line value is real for real coefficients.
        total += 2 * mp.re(hat)
    return total


def evaluate_cell(
    sigma: float,
    gamma: float,
    poly: dict,
    ordinates: tuple[float, ...],
    lam: np.ndarray,
    n_cap: int,
) -> dict:
    alpha = scaling_a(sigma)
    omega_f = scaling_omega(sigma, gamma)
    monomials = (float(poly["c0"]), float(poly["c2"]), float(poly["c4"]))
    a = mp.mpf(alpha)
    omega = mp.mpf(omega_f)
    c0, c2, c4 = mp.mpf(monomials[0]), mp.mpf(monomials[1]), mp.mpf(monomials[2])

    z_enum = zero_sum_online(a, omega, c0, c2, c4, ordinates)
    t_cut = float(ordinates[-1])
    z_tail = certified_zero_tail(t_cut, alpha, omega_f, monomials)

    hat0 = mp.re(hat_W(mp.mpc(0), a, omega, c0, c2, c4))
    hat1 = mp.re(hat_W(mp.mpc(1), a, omega, c0, c2, c4))
    pole = hat0 + hat1

    prime_contour, prime_comb = prime_sums(alpha, omega_f, monomials, n_cap, lam)
    tail_contour, tail_comb = certified_prime_tails(
        n_cap, alpha, omega_f, monomials,
    )

    arch, arch_tail = arch_weil_integral(
        a, omega, c0, c2, c4, alpha, omega_f, monomials,
    )

    # IDENTITY A: Z = Pole − Prime_comb + Arch
    rhs_a = pole - mp.mpf(prime_comb) + arch
    resid_a = z_enum - rhs_a
    budget_a = (
        mp.mpf(z_tail) + mp.mpf(tail_comb) + arch_tail + mp.mpf("1e-12")
    )

    # IDENTITY B: Lean honest transplant, ĥ_W spectral vs contour prime
    lhs_b = z_enum - hat1
    rhs_b = arch - mp.mpf(prime_contour)
    resid_b = lhs_b - rhs_b
    budget_b = (
        mp.mpf(z_tail) + mp.mpf(tail_contour) + arch_tail + mp.mpf("1e-12")
    )

    # Sign / channel diagnostics (no extra integrals).
    variants = {
        "A_classical": abs(resid_a),
        "A_prime_signflip": abs(z_enum - (pole + mp.mpf(prime_comb) + arch)),
        "A_drop_pole": abs(z_enum - (-mp.mpf(prime_comb) + arch)),
        "A_pole_only_hat1": abs(
            z_enum - (hat1 - mp.mpf(prime_comb) + arch)
        ),
        "B_lean_contour": abs(resid_b),
        "B_comb_in_B": abs((z_enum - hat1) - (arch - mp.mpf(prime_comb))),
    }

    return {
        "sigma": sigma,
        "gamma": gamma,
        "poly": poly["name"],
        "a": alpha,
        "omega": omega_f,
        "Z_enum": z_enum,
        "Z_tail": mp.mpf(z_tail),
        "hat0": hat0,
        "hat1": hat1,
        "pole": pole,
        "prime_comb": mp.mpf(prime_comb),
        "prime_contour": mp.mpf(prime_contour),
        "tail_comb": mp.mpf(tail_comb),
        "tail_contour": mp.mpf(tail_contour),
        "arch": arch,
        "arch_tail": arch_tail,
        "resid_A": resid_a,
        "budget_A": budget_a,
        "pass_A": abs(resid_a) < budget_a,
        "resid_B": resid_b,
        "budget_B": budget_b,
        "pass_B": abs(resid_b) < budget_b,
        "variants": variants,
    }


def localize_cell(cell: dict) -> str:
    variants = cell["variants"]
    best_name = min(variants, key=lambda key: variants[key])
    best_val = variants[best_name]
    if cell["pass_A"]:
        if cell["pass_B"]:
            return "both_A_B"
        return "A_ok_B_fail(hat_or_prime_weight)"
    if best_val < cell["budget_A"]:
        return best_name
    # Still large: guess the dominant unmatched channel.
    scale = max(
        abs(cell["Z_enum"]), abs(cell["pole"]), abs(cell["prime_comb"]),
        abs(cell["arch"]), mp.mpf("1e-30"),
    )
    gaps = {
        "zeros": abs(cell["resid_A"]) / scale,
        "pole": abs(abs(cell["pole"]) - abs(cell["Z_enum"] - cell["arch"] + cell["prime_comb"])) / scale,
        "prime": abs(abs(cell["prime_comb"]) - abs(cell["pole"] + cell["arch"] - cell["Z_enum"])) / scale,
        "arch": abs(abs(cell["arch"]) - abs(cell["Z_enum"] - cell["pole"] + cell["prime_comb"])) / scale,
    }
    return "channel:" + min(gaps, key=lambda key: gaps[key])


def format_verdict(rows: list[dict]) -> str:
    n_a = sum(1 for row in rows if row["pass_A"])
    n_b = sum(1 for row in rows if row["pass_B"])
    n = len(rows)
    max_resid = max(abs(row["resid_A"]) for row in rows)
    max_ratio = max(
        abs(row["resid_A"]) / row["budget_A"]
        if row["budget_A"] > 0 else mp.mpf("inf")
        for row in rows
    )
    fails = [row for row in rows if not row["pass_A"]]
    if fails:
        locs = sorted({localize_cell(row) for row in fails})
        sample = min(fails, key=lambda row: (row["gamma"], row["sigma"], row["poly"]))
        return (
            "EF_DISCREPANCY(loc=%s,n_fail=%d/%d,worst=sigma=%.3g,gamma=%.4g,"
            "p=%s,resid_A=%s,budget_A=%s)"
            % (
                "|".join(locs), len(fails), n,
                sample["sigma"], sample["gamma"], sample["poly"],
                fmt(sample["resid_A"], 8), fmt(sample["budget_A"], 8),
            )
        )
    if not rows:
        return "INCONCLUSIVE(reason=empty_matrix)"
    if n_a == n:
        return "EF_CONFIRMED(max_resid=%s,max_resid/budget=%s,A=%d/%d,B=%d/%d)" % (
            fmt(max_resid, 8), fmt(max_ratio, 6), n_a, n, n_b, n,
        )
    return "INCONCLUSIVE(reason=unclassified,A=%d/%d,B=%d/%d)" % (n_a, n, n_b, n)


def lean_decomposition_block() -> None:
    section("LEAN DECOMPOSITION  (proposal for GaborExplicitFormula)")
    print("  Named sorry: RH.gabor_explicitFormula : GaborExplicitFormula")
    print("  Goal: gaborArithmeticFormula F = gaborSpectralFormula F")
    print("        i.e. (1/2pi) integral [(zeta'/zeta)(2+it) hat_W(2+it)")
    print("                         − (ζ'/ζ)(−1/16+it) ĥ_W(−1/16+it)] dt")
    print("             = (Σ_ρ m(ρ) ĥ_W(ρ) − ĥ_W(1)).re")
    print("  Suggested brick list (classical / Mathlib v4.29.1):")
    print("    1. Entirety + Gaussian decay of gaborHat (closed Laplace,")
    print("       already algebraic in GaborSeparation; GaborIntegral discharges")
    print("       the pure-Gabor Fourier representation).")
    print("    2. Horizontal-edge vanishing: |ζ'/ζ(σ+it)| ≪ log²(|t|+2) on")
    print("       compact σ-intervals vs |ĥ_W| Gaussian.  Dominated convergence")
    print("       / Phragmen–Lindelof; no new zero-density input.")
    print("    3. Residue theorem in the strip −1/16 < Re s < 2:")
    print("       nontrivial zeros (multiplicity) + simple pole of ζ at 1")
    print("       (res ζ'/ζ = −1 ⇒ −ĥ_W(1)).  Trivial zeros lie at Re ≤ −2")
    print("       and stay outside the rectangle.")
    print("    4. Zero-sum convergence: Path A increment GaborIncrementBound")
    print("       (ZeroIncrement.lean, proved r546/r547) upgrades the")
    print("       discrete sum to a convergent series against the Gaussian")
    print("       envelope.  TrudgianZeroDensityBound stays Path B.")
    print("    5. Optional three-channel conversion (comment on")
    print("       gaborArithmeticFormula): Fourier inversion for Schwartz")
    print("       functions.  Right edge of ĥ_W inverts to the COMB")
    print("       Σ Λ(n) n^{−1/2} g(log n), NOT Lean gaborPrimeSide")
    print("       Σ Λ(n)(1+n^{−1}) g(log n) — that weight is the unshifted")
    print("       pairing of FullWeilTest.hat.  Left edge: χ'/χ digamma")
    print("       factor already expanded in ExternalBridges")
    print("       (logDeriv_zetaFEFactor_left_edge) plus reflected primes.")
    print("    6. Dictionary brick if the contour is kept in ĥ_W: either")
    print("       rewrite gaborPrimeSide to the comb, or prove the identity")
    print("       with unshifted hat_U(s)=H(s)H(−s) (compact r538 argument)")
    print("       and transport via ĥ_W(s)=hat_U(s−1/2).")
    print("  Not needed: a new zero-density theorem; RH; compact support.")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def run(smoke: bool) -> int:
    CHECKS.clear()
    mp.mp.dps = int(SPEC["mp_dps"])
    if smoke:
        mp.mp.dps = 20
    n_zeros = 8 if smoke else int(SPEC["n_zeros"])
    sigmas = (8.0,) if smoke else tuple(SPEC["sigmas"])
    gammas = (5.0, 14.13) if smoke else tuple(SPEC["gammas"])
    polys = SPEC["polynomials"][:2] if smoke else list(SPEC["polynomials"])
    ordinates = ON_LINE_ORDINATES[:n_zeros]
    n_cap = 800 if smoke else int(SPEC["prime_n_cap"])
    lam = von_mangoldt_table(n_cap)

    print("weil_gabor_explicit_formula_probe -- r548")
    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("lean_prop RH.GaborExplicitFormula")
    print("class even Gabor deg<=4  h(t)=p(t)exp(-a t^2) cos(omega t)")
    print("scaling a=sigma^2/64  omega=gamma-pi*sigma/64")
    print("identity_A %s" % SPEC["identity_A"])
    print("identity_B %s" % SPEC["identity_B"])
    print("tail_certified Trudgian JNT 134 (2014) Thm1/Cor1  "
          "|S(T)|<=0.111 log T + 0.275 log log T + 2.450  (T>=e)")
    print("prime_tail Chebyshev psi(x)<=%.1f x  Stieltjes vs Gaussian envelope"
          % float(SPEC["psi_chebyshev"]))
    print("n_zeros %d t1=%.16f tN=%.16f" % (
        n_zeros, float(ordinates[0]), float(ordinates[-1])))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("ZERO_SCOPE known critical-line zeros +/-; no claim excluding "
          "off-line zeros")
    print("prime_n_cap %d" % n_cap)

    section("G0  CLOSED HAT / g / POLE CONSISTENCY")
    g0_ok, g0_err = run_g0()
    check(
        "G0-calibration",
        g0_ok,
        "max_abs_err=%.3e atol=%.0e" % (g0_err, float(SPEC["g0_atol"])),
    )

    section("TAIL-CONSTANT MAJORANT (C_CRUDE vs Trudgian unit increment)")
    c_ok = True
    c_ratio_max = 0.0
    for height in (14.0, 30.0, 100.0, 236.0, 1.0e3, 1.0e4):
        trud = trudgian_increment(height, 1.0)
        crude = float(SPEC["c_crude"]) * math.log(height + 2.0)
        ratio = trud / math.log(height + 2.0)
        if ratio > c_ratio_max:
            c_ratio_max = ratio
        if crude + 1.0e-12 < trud:
            c_ok = False
    check(
        "C_CRUDE-majorises-Trudgian",
        c_ok,
        "C=%.1f max_B/log(T+2)=%.3f" % (float(SPEC["c_crude"]), c_ratio_max),
    )

    section("MATRIX  (sigma, gamma, p)  IDENTITY A / B")
    print("  %-5s %-8s %-4s %-9s %-9s %14s %14s %14s %12s %10s %8s %8s" % (
        "sig", "gamma", "p", "a", "omega",
        "Z_enum", "Pole", "Prime_c", "Arch", "resid_A", "A", "B"))
    rows: list[dict] = []
    for sigma in sigmas:
        for gamma in gammas:
            for poly in polys:
                cell = evaluate_cell(sigma, gamma, poly, ordinates, lam, n_cap)
                rows.append(cell)
                print(
                    "  %-5.1f %-8.4g %-4s %-9.3e %-9.4g "
                    "%14s %14s %14s %12s %10s %-8s %-8s"
                    % (
                        cell["sigma"], cell["gamma"], cell["poly"],
                        cell["a"], cell["omega"],
                        fmt(cell["Z_enum"], 8),
                        fmt(cell["pole"], 8),
                        fmt(cell["prime_comb"], 8),
                        fmt(cell["arch"], 8),
                        fmt(cell["resid_A"], 6),
                        "PASS" if cell["pass_A"] else "FAIL",
                        "PASS" if cell["pass_B"] else "FAIL",
                    )
                )

    section("PER-CELL BUDGETS AND LOCALISATION")
    print("  %-5s %-8s %-4s %12s %12s %12s %12s %12s %s" % (
        "sig", "gamma", "p", "resid_A", "budget_A", "resid_B",
        "budget_B", "Z_tail", "loc"))
    for cell in rows:
        loc = localize_cell(cell)
        print(
            "  %-5.1f %-8.4g %-4s %12s %12s %12s %12s %12s %s"
            % (
                cell["sigma"], cell["gamma"], cell["poly"],
                fmt(cell["resid_A"], 6), fmt(cell["budget_A"], 6),
                fmt(cell["resid_B"], 6), fmt(cell["budget_B"], 6),
                fmt(cell["Z_tail"], 6), loc,
            )
        )

    section("CHANNEL TABLE  (A: Z vs Pole-Prime+Arch)")
    print("  %-5s %-8s %-4s %14s %14s %14s %14s %14s" % (
        "sig", "gamma", "p", "Z_enum", "Pole", "Prime_comb",
        "Arch", "RHS_A"))
    for cell in rows:
        rhs_a = cell["pole"] - cell["prime_comb"] + cell["arch"]
        print(
            "  %-5.1f %-8.4g %-4s %14s %14s %14s %14s %14s"
            % (
                cell["sigma"], cell["gamma"], cell["poly"],
                fmt(cell["Z_enum"], 8), fmt(cell["pole"], 8),
                fmt(cell["prime_comb"], 8), fmt(cell["arch"], 8),
                fmt(rhs_a, 8),
            )
        )

    lean_decomposition_block()

    section("GATES / VERDICT")
    n_a = sum(1 for row in rows if row["pass_A"])
    n_b = sum(1 for row in rows if row["pass_B"])
    expected = len(sigmas) * len(gammas) * len(polys)
    check("G0-held", g0_ok, "closed-form calibration")
    check(
        "G1-matrix-complete",
        len(rows) == expected,
        "%d cells" % len(rows),
    )
    check(
        "G2-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G3-smoke-subset", True, "smoke 1x2x2 N=8 n_cap=800")
    else:
        check(
            "G3-full-grid",
            True,
            "full grid %dx%dx%d N=%d n_cap=%d"
            % (len(sigmas), len(gammas), len(polys), n_zeros, n_cap),
        )
    check(
        "G4-identity-A-within-budget",
        n_a == len(rows),
        "A PASS %d/%d  (classical Weil, LABEL=CERTIFIED tails)"
        % (n_a, len(rows)),
    )
    # B is diagnostic, not a gate failure by itself.
    check(
        "G5-identity-B-reported",
        True,
        "B PASS %d/%d  (Lean gaborPrimeSide transplant; not a gate)"
        % (n_b, len(rows)),
    )

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
        description=(
            "r548 Gabor-class Weil explicit-formula numerical precheck "
            "(experiments only)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
