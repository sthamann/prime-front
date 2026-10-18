#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_weil_positivity_subfamily_probe -- r601

Experiments-only scout of a *subfamily* of the pure Gabor Weil tests
on which Z ≥ 0 is read from primes + digamma, without zeros.

CLAIM BOUNDARY.  Finite certified-truncation arithmetic on the pure
Gabor packet h(t)=e^{−a t²} cos(ω t).  NO RH claim, NO anti-RH claim,
NO hpos* claim, NO ledger/paper/Lean/website/next.txt edit.  Weil
positivity for the whole class (Z ≥ 0 for all a>0, ω) is equivalent
to RH and is NOT the subject of this probe.  The target is the
Bombieri / Connes–Consani *small-support / large-width* subfamily.

EXPLICIT FORMULA (Lean r581, numerically sealed r548).  For the
Weil-shifted pairing ĥ_W(s)=H(s−1/2)H(1/2−s),

    Z := Re Σ_ρ m_ρ ĥ_W(ρ) = Pole − Prime_comb + Arch

    Pole = Re(ĥ_W(0)+ĥ_W(1))
    Prime_comb = Σ_n (2 Λ(n)/√n) g(log n)
    Arch = (1/2π) ∫ ĥ_W(1/2+it) (Re ψ(1/4+it/2) − log π) dt

g = h⋆h̃ is `pureGaborAutocorrelation` (Lean closed form).  ĥ_W is
`pureGaborHatDelta` with δ = s−1/2.  Comb convention 2Λ(n)/√n is the
r548 identity-A dictionary.

Z_arith is the three-channel right-hand side.  W_lower is a
zero-free lower bound Pole_lower − Prime_upper + Arch_lower.
POS_CERT means W_lower ≥ 0 (positivity from primes+digamma).
POS_NUM means Z_arith ≥ 0 but W_lower < 0 (cancellation not
certified).  NEG_NUM with |Z| above the signed-tail budget would be
a convention bug, not an anti-RH finding.

On-line zeros (mpmath.zetazero) appear only in the EF sanity check
and in the cancellation-distance d(ω), labelled as such.
"""
from __future__ import annotations

import argparse
import hashlib
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
from scipy.special import psi as scipy_psi  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
A_GRID = (
    0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0,
)
OMEGA_GRID = (
    0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 500.0,
    1000.0, 10000.0,
)
SANITY_CELLS = (
    (1.0, 0.0),
    (1.0, 2.0),
    (1.5, 5.0),
    (2.0, 10.0),
    (3.0, 20.0),
    (5.0, 50.0),
)
CANCEL_A = (0.05, 0.1, 0.2)

# First 100 positive ordinates.  Same freeze as r535/r539/r541/r548.
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

SPEC = {
    "round": 601,
    "target": "gabor_weil_positivity_subfamily",
    "parent_rounds": [548, 581],
    "hat": "weil_shifted_pure_gabor",
    "identity": "Z = Pole - Prime_comb + Arch",
    "prime_convention": "2*Lambda(n)/sqrt(n)*g(log n)",
    "class": "pure_gabor_not_hpos_star",
    "a_grid": list(A_GRID),
    "omega_grid": list(OMEGA_GRID),
    "sanity_cells": [list(cell) for cell in SANITY_CELLS],
    "cancel_a": list(CANCEL_A),
    "n_zeros_sanity": 2000,
    "mp_dps": 30,
    "n_max": 2000000,
    "psi_chebyshev": 2.0,
    "rel_tail": 1e-12,
    "ef_rel_tol": 1e-8,
    "hermite_n": 48,
    "hermite_n_lo": 32,
    "weierstrass_floor": 400,
    "g0_atol": 1e-9,
    "claim_boundary": "NO_RH_CLAIM experiments_only subfamily_not_hpos_star",
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LOG_CLIP = 700.0
EULER = 0.577215664901532860606512090082
K0_EXACT = (
    -EULER - 3.0 * math.log(2.0) - 0.5 * math.pi - math.log(math.pi)
)
# Unique positive root of Re ψ(1/4+it/2) − log π.  log-asymptote
# vanishes at |t|=2π; sealed by bisection against scipy.psi.
T_STAR = 6.2898359888369075


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" % (
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


def fmt(value: float, digits: int = 6) -> str:
    if not math.isfinite(value):
        return "inf" if value > 0 else "-inf"
    return "%.*e" % (digits, float(value))


def exp_clip(log_value: float) -> float:
    if log_value > LOG_CLIP:
        return math.inf
    if log_value < -LOG_CLIP:
        return 0.0
    return math.exp(log_value)


def payload_sha(blob: object) -> str:
    return hashlib.sha256(
        json.dumps(blob, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


# ---------------------------------------------------------------------------
# Closed forms (Lean RH/GaborSeparation.lean, r548 dictionary)
# ---------------------------------------------------------------------------
def g_pure_gabor(u_value: float, alpha: float, omega: float) -> float:
    """Lean `pureGaborAutocorrelation`."""
    pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
    return pref * exp_clip(-0.5 * alpha * u_value * u_value) * (
        math.cos(omega * u_value) + exp_clip(-(omega * omega) / (2.0 * alpha))
    )


def g_env_pref(alpha: float, omega: float) -> float:
    return 0.5 * math.sqrt(math.pi / (2.0 * alpha)) * (
        1.0 + exp_clip(-(omega * omega) / (2.0 * alpha))
    )


def hat_online(t_value: float, alpha: float, omega: float) -> float:
    """Lean `pureGaborOnLine`: ĥ_W(1/2+it) ≥ 0."""
    pref = math.pi / (4.0 * alpha)
    return pref * (
        exp_clip(-(t_value + omega) ** 2 / (2.0 * alpha))
        + exp_clip(-(t_value - omega) ** 2 / (2.0 * alpha))
        + 2.0 * exp_clip(-(t_value * t_value + omega * omega) / (2.0 * alpha))
    )


def re_hat_delta(sigma: float, t_value: float, alpha: float, omega: float) -> float:
    """Lean `re_pureGaborHatDelta`."""
    pref = math.pi / (4.0 * alpha)
    a2 = 2.0 * alpha
    return pref * (
        exp_clip((sigma * sigma - (t_value + omega) ** 2) / a2)
        * math.cos(sigma * (t_value + omega) / alpha)
        + exp_clip((sigma * sigma - (t_value - omega) ** 2) / a2)
        * math.cos(sigma * (t_value - omega) / alpha)
        + 2.0 * exp_clip((sigma * sigma - t_value * t_value - omega * omega) / a2)
        * math.cos(sigma * t_value / alpha)
    )


def pole_closed(alpha: float, omega: float) -> float:
    """Pole = ĥ_W(0)+ĥ_W(1) = (π/a) e^{1/(8a)−ω²/(2a)} (1+cos(ω/(2a))) ≥ 0."""
    return (
        (math.pi / alpha)
        * exp_clip(1.0 / (8.0 * alpha) - (omega * omega) / (2.0 * alpha))
        * (1.0 + math.cos(omega / (2.0 * alpha)))
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


# ---------------------------------------------------------------------------
# Digamma kernel
# ---------------------------------------------------------------------------
def k_kernel(t_values) -> np.ndarray:
    """k(t) = Re ψ(1/4+it/2) − log π.  Even, increasing on [0,∞)."""
    arr = np.asarray(t_values, dtype=np.float64)
    z_val = 0.25 + 0.5j * arr
    return np.real(scipy_psi(z_val)) - math.log(math.pi)


def k_weierstrass_lower(t_value: float, n_terms: int | None = None) -> float:
    """Weierstrass truncation of Re ψ(x+iy), x=1/4, y=t/2.

    Remainder Re Σ_{n>N} z/(n(n+z)) has nonnegative real part for
    x>0, so dropping it is a pointwise lower bound of k.
    """
    x_val = 0.25
    y_val = 0.5 * abs(float(t_value))
    if n_terms is None:
        n_terms = max(int(SPEC["weierstrass_floor"]), min(800, int(2.0 * y_val) + 80))
    acc = -EULER - x_val / (x_val * x_val + y_val * y_val)
    for index in range(1, n_terms + 1):
        nx_val = index + x_val
        acc += 1.0 / index - nx_val / (nx_val * nx_val + y_val * y_val)
    return acc - math.log(math.pi)


# ---------------------------------------------------------------------------
# von Mangoldt sieve (r548)
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


def pack_primes(lam: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    idx = np.nonzero(lam)[0]
    idx = idx[idx >= 2]
    u_val = np.log(idx.astype(np.float64))
    weight = 2.0 * lam[idx] / np.sqrt(idx.astype(np.float64))
    return u_val, weight


def gauss_exp_linear_tail(u0: float, alpha: float, linear: float) -> float:
    """∫_{u0}^∞ exp(−a u²/2 + linear·u) du, closed via erfc."""
    if alpha <= 0.0:
        return math.inf
    mu = linear / alpha
    log_pref = (linear * linear) / (2.0 * alpha)
    if log_pref > LOG_CLIP:
        return math.inf
    pref = math.exp(log_pref)
    scale = math.sqrt(math.pi / (2.0 * alpha))
    arg = math.sqrt(alpha / 2.0) * (u0 - mu)
    if arg > 20.0:
        return 0.0
    return pref * scale * math.erfc(arg)


def comb_smooth_tail(u0: float, alpha: float, omega: float) -> float:
    """PNT tail 2 ∫_{u0}^∞ g(u) e^{u/2} du via complex erfc."""
    a_mp = mp.mpf(alpha)
    omega_mp = mp.mpf(omega)
    u_mp = mp.mpf(u0)
    pref = mp.mpf("0.5") * mp.sqrt(mp.pi / (2 * a_mp))
    dc = mp.e ** (-omega_mp * omega_mp / (2 * a_mp))

    def incomplete(shift: mp.mpc) -> mp.mpc:
        z_arg = mp.sqrt(a_mp / 2) * (u_mp - shift / a_mp)
        return (
            mp.e ** (shift * shift / (2 * a_mp))
            * mp.sqrt(2 * mp.pi / a_mp)
            * mp.mpf("0.5")
            * mp.erfc(z_arg)
        )

    icos = mp.re(incomplete(mp.mpf("0.5") + mp.j * omega_mp))
    idc = incomplete(mp.mpf("0.5"))
    return float(2 * pref * (icos + dc * idc))


def prime_channels(
    alpha: float,
    omega: float,
    u_all: np.ndarray,
    weight: np.ndarray,
    n_used: int,
) -> tuple[float, float, float, float]:
    """Signed comb, |g| comb, PNT tail, envelope tail.  n_used is the cap."""
    u_cut = math.log(max(n_used, 2))
    mask = u_all <= u_cut + 1.0e-15
    u_val = u_all[mask]
    w_val = weight[mask]
    env = 0.5 * math.sqrt(math.pi / (2.0 * alpha)) * np.exp(
        -0.5 * alpha * u_val * u_val
    )
    dc = exp_clip(-(omega * omega) / (2.0 * alpha))
    g_val = env * (np.cos(omega * u_val) + dc)
    prime = float(np.dot(w_val, g_val))
    prime_abs = float(np.dot(w_val, np.abs(g_val)))
    pnt_tail = comb_smooth_tail(u_cut, alpha, omega)
    env_pref = g_env_pref(alpha, omega)
    i_half = gauss_exp_linear_tail(u_cut, alpha, 0.5)
    env_tail = 2.0 * float(SPEC["psi_chebyshev"]) * env_pref * i_half
    return prime, prime_abs, pnt_tail, env_tail


# ---------------------------------------------------------------------------
# Archimedean channel
# ---------------------------------------------------------------------------
def hat_online_vec(t_values, alpha: float, omega: float) -> np.ndarray:
    t_arr = np.asarray(t_values, dtype=np.float64)
    pref = math.pi / (4.0 * alpha)
    two_a = 2.0 * alpha
    return pref * (
        np.exp(-(t_arr + omega) ** 2 / two_a)
        + np.exp(-(t_arr - omega) ** 2 / two_a)
        + 2.0 * np.exp(-(t_arr * t_arr + omega * omega) / two_a)
    )


def _arch_segments(alpha: float, omega: float) -> list[tuple[float, float]]:
    width = 16.0 * math.sqrt(max(alpha, 1.0e-18))
    omega_abs = abs(float(omega))
    if omega_abs > 2.0 * width:
        return [(0.0, width), (omega_abs - width, omega_abs + width)]
    return [(0.0, max(omega_abs + width, width, T_STAR + width))]


def arch_trapz(alpha: float, omega: float, n_per: int) -> float:
    """(1/π) ∫_0^∞ ĥ k dt by evenness, segmented trapezoid."""
    total = 0.0
    for t_lo, t_hi in _arch_segments(alpha, omega):
        if t_hi <= t_lo:
            continue
        n_pts = max(65, int(n_per * max(t_hi - t_lo, 1.0) / max(math.sqrt(alpha), 0.25)))
        ts = np.linspace(t_lo, t_hi, n_pts)
        total += float(np.trapezoid(hat_online_vec(ts, alpha, omega) * k_kernel(ts), ts))
    return total / math.pi


def hat_interval(t0: float, t1: float, alpha: float, omega: float) -> float:
    """∫_{t0}^{t1} ĥ_W(1/2+it) dt, closed erf of three Gaussians."""
    scale = math.sqrt(2.0 * alpha)
    dc = exp_clip(-(omega * omega) / (2.0 * alpha))
    gauss_mass = math.sqrt(2.0 * math.pi * alpha)

    def slice_gauss(center: float) -> float:
        def cdf(t_val: float) -> float:
            if t_val == math.inf:
                return 1.0
            if t_val == -math.inf:
                return 0.0
            return 0.5 * (1.0 + math.erf((t_val - center) / scale))
        return gauss_mass * (cdf(t1) - cdf(t0))

    return (math.pi / (4.0 * alpha)) * (
        slice_gauss(-omega) + slice_gauss(omega) + 2.0 * dc * slice_gauss(0.0)
    )


def arch_monotone_lower(alpha: float, omega: float) -> float:
    """Left-endpoint Riemann of increasing k_lower against exact ĥ bins.

    k is increasing on [0,∞).  On each bin [t_i, t_{i+1}] ⊂ [0,∞),
    k(t) ≥ k_lower(t_i).  ĥ ≥ 0, so
        (1/π) Σ k_lower(t_i) ∫_{t_i}^{t_{i+1}} ĥ
    lower-bounds (1/π) ∫_0^∞ ĥ k = Arch.
    The gap (t_star, |ω|−12√a) with k>0 is dropped (conservative).
    """
    width = 12.0 * math.sqrt(max(alpha, 1.0e-18))
    omega_abs = abs(float(omega))
    dt = max(0.04, 0.20 * math.sqrt(alpha))
    points: list[float] = []

    def fill(t_lo: float, t_hi: float) -> None:
        t_val = t_lo
        points.append(t_val)
        while t_val + 0.5 * dt < t_hi:
            t_val += dt
            points.append(t_val)
        if points[-1] < t_hi:
            points.append(t_hi)

    fill(0.0, T_STAR)
    lobe_lo = max(T_STAR, omega_abs - width)
    lobe_hi = omega_abs + width
    if omega_abs <= T_STAR + width:
        fill(T_STAR, max(lobe_hi, T_STAR + width))
    else:
        fill(lobe_lo, lobe_hi)
    unique = sorted(set(round(val, 12) for val in points))
    total = 0.0
    for left, right in zip(unique[:-1], unique[1:]):
        if right <= left:
            continue
        mass = hat_interval(left, right, alpha, omega)
        total += k_weierstrass_lower(left) * mass
    t_end = unique[-1]
    k_end = k_weierstrass_lower(t_end)
    if k_end > 0.0:
        total += k_end * hat_interval(t_end, math.inf, alpha, omega)
    return total / math.pi


def arch_channels(alpha: float, omega: float) -> tuple[float, float, float]:
    arch_hi = arch_trapz(alpha, omega, 48)
    arch_lo_nodes = arch_trapz(alpha, omega, 24)
    quad_err = abs(arch_hi - arch_lo_nodes)
    arch_mono = arch_monotone_lower(alpha, omega)
    arch_lower = arch_mono - 2.0 * max(quad_err, 1.0e-14)
    return float(arch_hi), float(arch_lower), float(quad_err)


# ---------------------------------------------------------------------------
# Zeros (sanity / cancellation distance only)
# ---------------------------------------------------------------------------
_ZERO_CACHE: dict[int, tuple[float, ...]] = {}
_NEAR_CACHE: dict[int, tuple[float, ...]] = {}


def ordinates_first_n(n_zeros: int, dps: int = 20) -> tuple[float, ...]:
    if n_zeros in _ZERO_CACHE:
        return _ZERO_CACHE[n_zeros]
    if n_zeros <= len(ON_LINE_ORDINATES):
        out = ON_LINE_ORDINATES[:n_zeros]
        _ZERO_CACHE[n_zeros] = out
        return out
    prev = mp.mp.dps
    mp.mp.dps = int(dps)
    acc = list(ON_LINE_ORDINATES)
    for index in range(len(ON_LINE_ORDINATES) + 1, n_zeros + 1):
        acc.append(float(mp.zetazero(index).imag))
    mp.mp.dps = prev
    out = tuple(acc)
    _ZERO_CACHE[n_zeros] = out
    return out


def zeros_near_height(height: float, dps: int = 20) -> tuple[float, ...]:
    """A few on-line ordinates near |ω|, labelled ONLINE_ASSUMPTION."""
    t_val = abs(float(height))
    if t_val < ON_LINE_ORDINATES[-1] + 1.0:
        return ON_LINE_ORDINATES
    n_est = max(
        1,
        int(
            t_val
            / (2.0 * math.pi)
            * math.log(max(t_val / (2.0 * math.pi * math.e), math.e))
        ),
    )
    prev = mp.mp.dps
    mp.mp.dps = int(dps)
    lo = max(1, n_est - 4)
    hi = n_est + 5
    out = [float(mp.zetazero(index).imag) for index in range(lo, hi)]
    mp.mp.dps = prev
    return tuple(out)


def nearest_d(omega: float, gammas: tuple[float, ...]) -> float:
    if not gammas:
        return float("inf")
    w_abs = abs(float(omega))
    return min(abs(w_abs - gamma) for gamma in gammas)


def zero_sum_online(
    alpha: float, omega: float, gammas: tuple[float, ...],
) -> float:
    """Σ_ρ ĥ_W(ρ) over listed on-line ±γ.  ONLINE_ASSUMPTION."""
    total = 0.0
    for height in gammas:
        total += 2.0 * hat_online(float(height), alpha, omega)
    return total


# ---------------------------------------------------------------------------
# Cell
# ---------------------------------------------------------------------------
def n_cap_of(alpha: float, n_max: int) -> int:
    u_cap = 1.0 / (2.0 * alpha) + 6.0 * math.sqrt(2.0 / alpha)
    n_val = int(math.ceil(exp_clip(min(u_cap, 40.0))))
    return max(32, min(n_max, n_val))


def classify(z_arith: float, w_lower: float, err: float, scale: float) -> str:
    if w_lower >= 0.0:
        return "POS_CERT"
    floor = max(float(err), 1.0e-12 * max(scale, 1.0), 1.0e-14)
    if z_arith + floor >= 0.0:
        return "POS_NUM"
    return "NEG_NUM"


def evaluate_cell(
    alpha: float,
    omega: float,
    u_all: np.ndarray,
    weight: np.ndarray,
    n_max: int,
) -> dict:
    n_used = n_cap_of(alpha, n_max)
    pole = pole_closed(alpha, omega)
    prime, prime_abs, pnt_tail, env_tail = prime_channels(
        alpha, omega, u_all, weight, n_used,
    )
    prime_arith = prime + pnt_tail
    prime_upper = prime_abs + env_tail
    arch, arch_lower, arch_err = arch_channels(alpha, omega)
    z_arith = pole - prime_arith + arch
    pole_lower = max(0.0, pole)
    w_lower = pole_lower - prime_upper + arch_lower
    tail_err = env_tail
    scale = max(abs(pole), abs(prime_arith), abs(arch), abs(z_arith), 1.0e-12)
    verd = classify(z_arith, w_lower, tail_err, scale)
    return {
        "a": float(alpha),
        "omega": float(omega),
        "n_used": int(n_used),
        "pole": float(pole),
        "pole_lower": float(pole_lower),
        "prime": float(prime_arith),
        "prime_abs": float(prime_abs),
        "pnt_tail": float(pnt_tail),
        "env_tail": float(env_tail),
        "prime_upper": float(prime_upper),
        "arch": float(arch),
        "arch_lower": float(arch_lower),
        "arch_err": float(arch_err),
        "Z_arith": float(z_arith),
        "W_lower": float(w_lower),
        "tail_err": float(tail_err),
        "verd": verd,
    }


def pub_cell(row: dict) -> dict:
    keys = (
        "a", "omega", "n_used", "pole", "prime", "prime_upper",
        "arch", "arch_lower", "Z_arith", "W_lower", "verd",
    )
    out = {}
    for key in keys:
        val = row[key]
        out[key] = val if key in ("n_used", "verd") else fmt(float(val), 12)
    return out


# ---------------------------------------------------------------------------
# G0
# ---------------------------------------------------------------------------
def run_g0() -> float:
    max_err = 0.0

    def bump(err: float) -> None:
        nonlocal max_err
        max_err = max(max_err, float(err))

    mp.mp.dps = int(SPEC["mp_dps"])
    for alpha, omega_f in ((1.0, 0.0), (1.0, 2.0), (0.5, 1.5), (5.0, 10.0)):
        a_mp = mp.mpf(alpha)
        omega_mp = mp.mpf(omega_f)
        hat0 = mp.re(hat_W_pure_closed(mp.mpc("-0.5"), a_mp, omega_mp))
        hat1 = mp.re(hat_W_pure_closed(mp.mpc("0.5"), a_mp, omega_mp))
        pole = pole_closed(alpha, omega_f)
        bump(abs(float(hat0 - hat1)))
        bump(abs(float(hat0 + hat1) - pole))
        bump(abs(re_hat_delta(-0.5, 0.0, alpha, omega_f) - float(hat0)))
        g0 = g_pure_gabor(0.0, alpha, omega_f)
        pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
        g0_closed = pref * (1.0 + math.exp(-(omega_f * omega_f) / (2.0 * alpha)))
        bump(abs(g0 - g0_closed))
        online = hat_online(0.0, alpha, omega_f)
        closed_half = re_hat_delta(0.0, 0.0, alpha, omega_f)
        bump(abs(online - closed_half))

    bump(abs(float(k_kernel(0.0)) - K0_EXACT))
    bump(abs(float(k_kernel(T_STAR))))
    for t_val in (0.0, 1.0, 6.0, 14.13, 50.0, 200.0):
        lower = k_weierstrass_lower(t_val)
        true = float(k_kernel(t_val))
        bump(0.0 if lower <= true + 1.0e-9 else (lower - true))

    # Arch GH vs even-segment trapz on a compact window.
    for alpha, omega_f in ((1.0, 0.0), (1.0, 2.0), (5.0, 10.0)):
        arch, _, err = arch_channels(alpha, omega_f)
        width = 12.0 * math.sqrt(alpha)
        t_hi = abs(omega_f) + width
        ts = np.linspace(0.0, t_hi, 4001)
        hats = np.array([hat_online(float(t_val), alpha, omega_f) for t_val in ts])
        ks = k_kernel(ts)
        trapz = (2.0 / (2.0 * math.pi)) * np.trapezoid(hats * ks, ts)
        bump(abs(arch - float(trapz)))
        bump(0.0 if err < 1.0e-8 else err)

    # Comb PNT full-line vs pole at ω=0 (saddle on u>0, not an identity).
    # At a=1, ω=0: discrete Prime + tiny tail + Arch + Pole ≈ 0.
    lam = von_mangoldt_table(4000)
    u_all, weight = pack_primes(lam)
    row = evaluate_cell(1.0, 0.0, u_all, weight, 4000)
    bump(abs(row["Z_arith"]))
    bump(0.0 if row["pole"] >= 0.0 else 1.0)
    bump(0.0 if row["verd"] in ("POS_CERT", "POS_NUM") else 1.0)
    return max_err


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
def omega0_of(rows: list[dict]) -> float | None:
    """Smallest grid-ω after which every later cell is POS_CERT."""
    ordered = sorted(rows, key=lambda row: row["omega"])
    last_fail = None
    for row in ordered:
        if row["verd"] != "POS_CERT":
            last_fail = row["omega"]
    if last_fail is None:
        return float(ordered[0]["omega"]) if ordered else None
    later = [row["omega"] for row in ordered if row["omega"] > last_fail]
    if not later:
        return None
    if all(
        row["verd"] == "POS_CERT"
        for row in ordered if row["omega"] > last_fail
    ):
        return float(min(later))
    return None


def a0_of(by_a: dict[float, list[dict]]) -> float | None:
    alphas = sorted(by_a)
    for index, alpha in enumerate(alphas):
        if all(row["verd"] == "POS_CERT" for row in by_a[alpha]):
            rest = alphas[index:]
            if all(
                all(row["verd"] == "POS_CERT" for row in by_a[other])
                for other in rest
            ):
                return float(alpha)
    return None


def global_verdict(a0: float | None, omega0: dict) -> str:
    if a0 is None:
        return "DOMINANCE_FAILS"
    table = ",".join(
        "a=%s:w0=%s" % (fmt(alpha, 2), fmt(omega0[alpha], 2) if omega0[alpha] is not None else "none")
        for alpha in sorted(omega0)
    )
    return "ARCH_DOMINATES(a0=%s, omega0={%s})" % (fmt(a0, 2), table)


def compute(
    smoke: bool,
    gammas_sanity: tuple[float, ...],
    extra_gamma: dict[float, tuple[float, ...]],
) -> dict:
    mp.mp.dps = 20 if smoke else int(SPEC["mp_dps"])
    alphas = (1.0, 5.0) if smoke else tuple(A_GRID)
    omegas = (0.0, 10.0, 50.0) if smoke else tuple(OMEGA_GRID)
    n_max = 4000 if smoke else int(SPEC["n_max"])
    lam = von_mangoldt_table(n_max)
    u_all, weight = pack_primes(lam)
    rows: list[dict] = []
    by_key: dict[tuple[float, float], dict] = {}
    for alpha in alphas:
        for omega in omegas:
            row = evaluate_cell(alpha, omega, u_all, weight, n_max)
            rows.append(row)
            by_key[(alpha, omega)] = row
    sanity = []
    sanity_pairs = SANITY_CELLS if not smoke else ((1.0, 0.0), (5.0, 10.0))
    for alpha, omega in sanity_pairs:
        row = by_key.get((alpha, omega))
        if row is None:
            row = evaluate_cell(alpha, omega, u_all, weight, n_max)
        z_zeros = zero_sum_online(alpha, omega, gammas_sanity)
        scale = max(
            abs(row["Z_arith"]), abs(z_zeros), abs(row["pole"]),
            abs(row["prime"]), abs(row["arch"]), 1.0e-12,
        )
        rel = abs(row["Z_arith"] - z_zeros) / scale
        sanity.append({
            "a": alpha,
            "omega": omega,
            "Z_arith": row["Z_arith"],
            "Z_zeros": z_zeros,
            "rel": rel,
            "n_zeros": len(gammas_sanity),
            "pass": rel <= float(SPEC["ef_rel_tol"]),
        })
    cancel = []
    cancel_as = tuple(alpha for alpha in alphas if alpha in set(CANCEL_A if not smoke else alphas))
    gammas_d = gammas_sanity if gammas_sanity else ON_LINE_ORDINATES
    for alpha in cancel_as:
        for omega in omegas:
            row = by_key[(alpha, omega)]
            pool = gammas_d + extra_gamma.get(omega, ())
            dist = nearest_d(omega, pool)
            pred = (0.125 + 0.5 * dist * dist) / alpha
            denom = max(abs(row["Z_arith"]), 1.0e-30)
            measured = math.log(max(row["prime_upper"], 1.0e-30) / denom)
            cancel.append({
                "a": alpha,
                "omega": omega,
                "d": dist,
                "pred": pred,
                "measured": measured,
                "Z_arith": row["Z_arith"],
                "prime_upper": row["prime_upper"],
            })
    by_a: dict[float, list[dict]] = {}
    for row in rows:
        by_a.setdefault(row["a"], []).append(row)
    omega0 = {alpha: omega0_of(by_a[alpha]) for alpha in by_a}
    a0 = a0_of(by_a)
    return {
        "rows": rows,
        "sanity": sanity,
        "cancel": cancel,
        "omega0": omega0,
        "a0": a0,
        "n_max": n_max,
        "n_zeros": len(gammas_sanity),
        "smoke": smoke,
    }


def run(smoke: bool) -> int:
    CHECKS.clear()
    mp.mp.dps = int(SPEC["mp_dps"])
    print("gabor_weil_positivity_subfamily_probe -- r601")
    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM NOT_HPOS_STAR")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("identity Z = Pole - Prime_comb + Arch   (r548/r581)")
    print("g Lean pureGaborAutocorrelation")
    print("hat Lean pureGaborHatDelta / re_pureGaborHatDelta")
    print("prime_convention 2*Lambda(n)/sqrt(n)*g(log n)")
    print("psi_chebyshev %.1f  (Rosser-Schoenfeld-safe; r548)" % float(SPEC["psi_chebyshev"]))
    print("k(0) = -gamma_E - 3 log 2 - pi/2 - log pi = %s" % fmt(K0_EXACT, 12))
    print("T_STAR %s  (k(t)=0)" % fmt(T_STAR, 12))
    print("ZERO_SCOPE sanity/cancellation: on-line mpmath.zetazero only")

    section("G0  CLOSED POLE / g / k / ARCH")
    g0_err = run_g0()
    check(
        "G0-calibration",
        g0_err < float(SPEC["g0_atol"]),
        "max_abs_err=%s atol=%s" % (fmt(g0_err, 3), fmt(float(SPEC["g0_atol"]), 1)),
    )

    section("G1  GRID  Z_arith / W_lower")
    n_zeros = 20 if smoke else int(SPEC["n_zeros_sanity"])
    gammas_sanity = ON_LINE_ORDINATES[:n_zeros] if smoke else ordinates_first_n(n_zeros, dps=20)
    extra_gamma: dict[float, tuple[float, ...]] = {}
    if not smoke:
        for omega in OMEGA_GRID:
            if omega > ON_LINE_ORDINATES[-1]:
                extra_gamma[omega] = zeros_near_height(omega)
    data1 = compute(smoke, gammas_sanity, extra_gamma)
    data2 = compute(smoke, gammas_sanity, extra_gamma)
    seal1 = payload_sha({
        "SPEC_SHA": SPEC_SHA,
        "rows": [pub_cell(row) for row in data1["rows"]],
        "sanity": [
            {key: (fmt(val, 12) if isinstance(val, float) else val)
             for key, val in item.items()}
            for item in data1["sanity"]
        ],
        "a0": None if data1["a0"] is None else fmt(data1["a0"], 12),
        "omega0": {
            fmt(alpha, 12): (None if omega is None else fmt(omega, 12))
            for alpha, omega in data1["omega0"].items()
        },
    })
    seal2 = payload_sha({
        "SPEC_SHA": SPEC_SHA,
        "rows": [pub_cell(row) for row in data2["rows"]],
        "sanity": [
            {key: (fmt(val, 12) if isinstance(val, float) else val)
             for key, val in item.items()}
            for item in data2["sanity"]
        ],
        "a0": None if data2["a0"] is None else fmt(data2["a0"], 12),
        "omega0": {
            fmt(alpha, 12): (None if omega is None else fmt(omega, 12))
            for alpha, omega in data2["omega0"].items()
        },
    })
    check("G3-determinism-two-run", seal1 == seal2, "payload hashed twice")
    data = data1
    print("  a        omega      Z_arith      W_lower     verd       pole         prime        arch         pu")
    for row in data["rows"]:
        print("  %-8s %-10s %-12s %-11s %-10s %-12s %-12s %-12s %s" % (
            fmt(row["a"], 2), fmt(row["omega"], 2),
            fmt(row["Z_arith"], 4), fmt(row["W_lower"], 4),
            row["verd"],
            fmt(row["pole"], 4), fmt(row["prime"], 4),
            fmt(row["arch"], 4), fmt(row["prime_upper"], 4),
        ))
        if row["verd"] == "NEG_NUM":
            print("    NOTE NEG_NUM: convention-bug candidate, NOT an anti-RH finding")

    section("G2  EF SANITY  (on-line zeros, ONLINE_ASSUMPTION)")
    print("  labelled ONLINE_ASSUMPTION: first %d mpmath.zetazero" % data["n_zeros"])
    for item in data["sanity"]:
        print("  a=%s omega=%s Z_arith=%s Z_zeros=%s rel=%s %s" % (
            fmt(item["a"], 2), fmt(item["omega"], 2),
            fmt(item["Z_arith"], 6), fmt(item["Z_zeros"], 6),
            fmt(item["rel"], 3),
            "PASS" if item["pass"] else "FAIL",
        ))
        check(
            "EF-a=%s-w=%s" % (fmt(item["a"], 2), fmt(item["omega"], 2)),
            bool(item["pass"]),
            "rel=%s tol=%s" % (fmt(item["rel"], 3), fmt(float(SPEC["ef_rel_tol"]), 1)),
        )

    section("G4  a0 / omega0 / CANCELLATION")
    print("  a0 %s" % ("none" if data["a0"] is None else fmt(data["a0"], 4)))
    for alpha in sorted(data["omega0"]):
        omega0 = data["omega0"][alpha]
        print("  omega0(a=%s) %s" % (
            fmt(alpha, 2),
            "none" if omega0 is None else fmt(omega0, 4),
        ))
    print("  log(Prime_upper/|Z_arith|) vs L3 (1/8+d^2/2)/a")
    print("  d = dist(omega, nearest listed on-line ordinate); truncated if omega>>T_max")
    for item in data["cancel"]:
        print("  a=%s omega=%s d=%s pred=%s meas=%s Z=%s pu=%s" % (
            fmt(item["a"], 2), fmt(item["omega"], 2),
            fmt(item["d"], 4), fmt(item["pred"], 4),
            fmt(item["measured"], 4),
            fmt(item["Z_arith"], 4), fmt(item["prime_upper"], 4),
        ))

    n_cert = sum(1 for row in data["rows"] if row["verd"] == "POS_CERT")
    n_num = sum(1 for row in data["rows"] if row["verd"] == "POS_NUM")
    n_neg = sum(1 for row in data["rows"] if row["verd"] == "NEG_NUM")
    print("  counts POS_CERT=%d POS_NUM=%d NEG_NUM=%d / %d" % (
        n_cert, n_num, n_neg, len(data["rows"])))
    check("G4-no-negnum-outside-tail", n_neg == 0, "NEG_NUM=%d" % n_neg)

    section("G5  VERDICT")
    verd = global_verdict(data["a0"], data["omega0"])
    print("VERDICT %s" % verd)
    print("INTERPRETATION small-support/large-width positivity (Bombieri")
    print("  Remarks on Weil's quadratic functional; Connes-Consani 2021")
    print("  archimedean positivity).  Subfamily, NOT hpos*.")
    print("PAYLOAD_SHA256 %s" % seal1)
    print("NO_RH_CLAIM")
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        return 1
    print("ALL CHECKS PASSED")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "r601 Gabor Weil positivity subfamily (experiments only, no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
