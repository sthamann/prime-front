#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_tropical_heat_probe -- r608

Experiments-only scout of GABOR.TROPICAL.01: Laplace principle for
the pure-Gabor zero-side Z(a,ω) = Re Σ_ρ m(ρ) ĥ_{a,ω}(ρ), the heat
identity in (a,ω), and the source-side cancellation budget.

  Score S_ρ(ω) = σ² − (|t| − ω)²,  F(ω) = sup_ρ S_ρ(ω).
  L(a,ω)  := 2a · log|Z(a,ω)|          (signed; can vanish)
  L⁺(a,ω) := 2a · log(Σ_ρ m |ĥ(ρ)|)   (unsigned envelope)

Sealed r605N: exposed-orbit phase locking gives Z < 0 in every ¬RH
configuration.  This round asks whether the a→0⁺ envelope is the
tropical maximum of S, whether ĥ is a heat flow in a, and how much
prime-side cancellation the true-world source needs.

HAT CONVENTION.  Literal Lean `pureGaborHatDelta` via r605N
`gabor_exposed_orbit_probe.hat_delta_mp` (GaborSeparation.lean
L114–123).  δ = s − 1/2, third lobe 2 exp((σ²−t²−ω²)/(2a)) exp(i σ t/a).
Checkpoint ĥ_{1,0}(1) = π e^{1/8}.  A σ>0 orbit expands to four strip
partners; σ=0 expands to two.  T1 Z is the pure zero side (no pole).

T2 HEAT.  Each traveling lobe φ(a,ω) = a^{−1/2} exp((σ+i(t−ω))²/(2a))
satisfies ∂_a φ = (1/2) ∂²_ω φ.  The Weil hat is
ĥ = (π/(4a)) (E₊ + E₋ + 2 E_×) = (π/4) a^{−1/2} Σ φ_ℓ, hence
  ∂_a ĥ = (1/2) ∂²_ω ĥ − ĥ/(2a)
when a traveling lobe dominates (the DC/cross term is a heat kernel
at ω=0 times a Tychonoff factor and is negligible for |ω| ≳ 2).
The parent wrote f = e^{(σ+i(t−ω))²/(2a)}/a with the uncorrected
PDE; that /a form needs the Euler term −f/(2a).  Both are checked.

Consequence: Z(a,·) is a heat-flow in a (after the √a weight) with
singular a→0⁺ data Σ m δ_{±γ} under RH; an off-line zero corresponds
to complex-shifted delta data, i.e. Tychonoff-type growth e^{σ²/(2a)}
at the initial singularity — a maximum principle for a>0 cannot see it.

T3 SOURCE.  Identity A (r548/r601): Z = POLE + ARCH − PRIME with
  g(u) = (1/2) √(π/(2a)) e^{−a u²/2} (cos(ω u) + e^{−ω²/(2a)})
  PRIME = Σ_n 2 Λ(n) n^{−1/2} g(log n)
The parent sketch h(x) ∝ e^{−a x²/2}(cos(ωx)+1) misses the DC Gaussian
e^{−ω²/(2a)} of the third lobe; this probe uses the r601 carrier.

(H) limsup 2a·log|H| ≤ 0 on the source side is the Gaussian-smoothed
magnitude statement ψ(x) − x = O(√x · x^{o(1)}); by
PRIME.NOGO.COMPOSITE.01 (T1) magnitude-class inputs are RH-strength —
this probe measures, it does not prove.

CLAIM BOUNDARY.  Finite closed-form / seeded arithmetic on synthetic
off-line catalogs plus a frozen on-line ordinate table, and a
truncated von Mangoldt comb.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/verification/website/next.txt edit.  KEIN RH-CLAIM.

On-line background: first 2000 positive ordinates from
verified_zeros_n7000.npy (mpmath.zetazero, dps=15).

Verdicts:
  TROPICAL_CONFIRMED(c=…)
  LAPLACE_FAILS(<where>) / HEAT_IDENTITY_FAILS
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import gabor_exposed_orbit_probe as r605  # noqa: E402  (r605N sealed hat/orbit)

ROUND = 608
SEED = 608202609
DPS_T1 = 60
DPS_T2 = 40
N_ONLINE = 2000
N_T2 = 30
EXPO_SKIP = -40.0
PI = math.pi
LOG_CLIP = 700.0
N_PRIME_CAP = 5_000_000
TAIL_TARGET = 1e-20
FAKE_BETA_SIGMA = 0.4  # β = 0.9 + 100i  ⇒  σ = 0.4, σ² = 0.16
FAKE_BETA_T = 100.0
FAKE_M = 1
C_LAPLACE_MAX = 30.0
HEAT_REL_TOL = 1e-6
EF_ABS_TOL = 1e-10

A_T1 = (0.2, 0.1, 0.05, 0.02, 0.01, 0.005)
OMEGA_T1 = (99.5, 99.9, 99.975, 100.0, 100.05, 100.5, 250.0)
A_T3 = (0.2, 0.1, 0.05, 0.02)
OMEGA_T3 = (14.1347, 20.0, 100.0)
OMEGA_SYN = 99.975

SPEC = {
    "round": ROUND,
    "tag": "r608",
    "contract": "GABOR.TROPICAL.01",
    "hat": "pureGaborHatDelta_literal_L114",
    "score": "S=sigma^2-(|gamma|-omega)^2",
    "envelope": "F=sup_rho S_rho",
    "L": "2a log|Z|",
    "Lplus": "2a log(sum m |hat|)",
    "identity_A": "Z = Pole + Arch - Prime_comb",
    "prime_convention": "2*Lambda(n)/sqrt(n)*g(log n)",
    "g_carrier": "r601 pureGaborAutocorrelation (cos + exp(-w^2/(2a)))",
    "fake_zero": "bookkeeping 4 Re hat(0.9+100i), not a change of Lambda",
    "seed": SEED,
    "n_online": N_ONLINE,
    "zeros_cache": "verified_zeros_n7000.npy[:2000]",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "dps_t1": DPS_T1,
    "dps_t2": DPS_T2,
    "parent_hat": "gabor_exposed_orbit_probe r605N",
    "parent_arith": "r548/r601 pole-arch-prime identity A",
    "claim_boundary": "NO_RH_CLAIM experiments_only",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-42s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def fmt(x: float, n: int = 12) -> str:
    if x is None or not math.isfinite(float(x)):
        return "nan" if x is None or math.isnan(float(x)) else (
            "+inf" if float(x) > 0.0 else "-inf"
        )
    return "%+.*e" % (n, float(x))


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def trapz(y_val: np.ndarray, x_val: np.ndarray) -> float:
    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(y_val, x_val))
    return float(np.trapz(y_val, x_val))


def exp_clip(log_value: float) -> float:
    if log_value > LOG_CLIP:
        return math.inf
    if log_value < -LOG_CLIP:
        return 0.0
    return math.exp(log_value)


# ---------------------------------------------------------------------------
# Hat: r605N literal Lean pureGaborHatDelta, with Laplace scaling
# ---------------------------------------------------------------------------
def hat_delta_scaled_mp(
    a: mp.mpf, omega: mp.mpf, sigma: mp.mpf, t_val: mp.mpf, f_env: mp.mpf,
) -> mp.mpc:
    """ĥ · exp(−F/(2a)).  Same three lobes as r605.hat_delta_mp."""
    pref = mp.pi / (4 * a)
    shift = f_env / (2 * a)
    two_a = 2 * a
    term_plus = mp.exp(
        (sigma ** 2 - (t_val + omega) ** 2) / two_a - shift
    ) * mp.exp(mp.j * (sigma * (t_val + omega) / a))
    term_minus = mp.exp(
        (sigma ** 2 - (t_val - omega) ** 2) / two_a - shift
    ) * mp.exp(mp.j * (sigma * (t_val - omega) / a))
    term_cross = (
        2
        * mp.exp((sigma ** 2 - t_val ** 2 - omega ** 2) / two_a - shift)
        * mp.exp(mp.j * (sigma * t_val / a))
    )
    return pref * (term_plus + term_minus + term_cross)


def lobe_lead_score(sigma: float, t_val: float, omega: float) -> float:
    s2 = sigma * sigma
    return max(
        s2 - (t_val + omega) ** 2,
        s2 - (t_val - omega) ** 2,
        s2 - t_val * t_val - omega * omega,
    )


def catalog_points(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
) -> list[tuple[float, float, int]]:
    """Expanded FE partners.  Attribution: r605.expand_partners."""
    out: list[tuple[float, float, int]] = []
    for sig, gam, mult in r605.merge_orbits(off):
        out.extend(r605.expand_partners(sig, gam, mult))
    for gam in online:
        out.extend(r605.expand_partners(0.0, float(gam), 1))
    return out


def envelope_F(
    points: list[tuple[float, float, int]], omega: float,
) -> float:
    best = -1.0e300
    for sig, t_val, _m in points:
        s_val = r605.score_S(sig, t_val, omega)
        if s_val > best:
            best = s_val
    return best


def t1_configs(
    online: tuple[float, ...],
) -> list[tuple[str, list[tuple[float, float, int]], tuple[float, ...]]]:
    raw = {name: off for name, off, _extra in r605.named_configs()}
    return [
        ("C1", r605.merge_orbits(raw["C1"]), online),
        ("C4", r605.merge_orbits(raw["C4"]), online),
        ("C2m", r605.merge_orbits(raw["C2m"]), online),
        ("ON", [], online),
    ]


def sum_zero_side(
    points: list[tuple[float, float, int]],
    a: float,
    omega: float,
    f_env: float,
) -> tuple[float, float, int]:
    """Return (Re Z, Σ m |ĥ|, n_used) via scaled hats, mp.dps DPS_T1."""
    mp.mp.dps = DPS_T1
    a_mp = mp.mpf(a)
    w_mp = mp.mpf(omega)
    f_mp = mp.mpf(f_env)
    z_acc = mp.mpc(0)
    abs_acc = mp.mpf(0)
    n_used = 0
    two_a = 2.0 * a
    for sig, t_val, mult in points:
        lead = lobe_lead_score(sig, t_val, omega)
        if (lead - f_env) / two_a < EXPO_SKIP:
            continue
        h_sc = hat_delta_scaled_mp(
            a_mp, w_mp, mp.mpf(sig), mp.mpf(t_val), f_mp,
        )
        z_acc += mult * h_sc
        abs_acc += mult * abs(h_sc)
        n_used += 1
    z_sc = float(mp.re(z_acc))
    abs_sc = float(abs_acc)
    # Z = e^{F/(2a)} Z_scaled; restore only if needed by caller via F.
    return z_sc, abs_sc, n_used


def L_from_scaled(f_env: float, a: float, scaled: float) -> float:
    mag = abs(float(scaled))
    if not math.isfinite(mag) or mag <= 0.0:
        return float("-inf")
    return f_env + 2.0 * a * math.log(mag)


# ---------------------------------------------------------------------------
# T2 heat finite differences (mpmath dps 40, relative step 1e-6)
# ---------------------------------------------------------------------------
def fd_heat(
    func,
    a: mp.mpf,
    omega: mp.mpf,
    h_rel: mp.mpf,
) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    h_a = h_rel * a
    h_w = h_rel * max(abs(omega), mp.mpf("1"))
    d_a = (func(a + h_a, omega) - func(a - h_a, omega)) / (2 * h_a)
    d2_w = (
        func(a, omega + h_w)
        - 2 * func(a, omega)
        + func(a, omega - h_w)
    ) / (h_w ** 2)
    val = func(a, omega)
    return d_a, d2_w, val


def rel_heat(
    d_a: mp.mpc, d2_w: mp.mpc, val: mp.mpc, a: mp.mpf, euler: bool,
) -> float:
    rhs = mp.mpf("0.5") * d2_w
    if euler:
        num = abs(d_a - rhs + val / (2 * a))
        den = abs(d_a) + abs(rhs) + abs(val) / (2 * abs(a)) + mp.mpf("1e-40")
    else:
        num = abs(d_a - rhs)
        den = abs(d_a) + abs(rhs) + mp.mpf("1e-40")
    if abs(val) < mp.mpf("1e-30") and abs(d_a) < mp.mpf("1e-30"):
        return 0.0
    return float(num / den)


def t2_points(n_pts: int, rng: random.Random) -> list[tuple[float, float, float, float]]:
    pts = []
    for idx in range(n_pts):
        alpha = math.exp(rng.uniform(math.log(0.05), math.log(0.8)))
        omega = rng.uniform(5.0, 30.0)
        sigma = rng.uniform(-0.4, 0.4)
        if idx % 3 == 0:
            t_val = omega + rng.uniform(-1.2, 1.2)
        elif idx % 3 == 1:
            t_val = -omega + rng.uniform(-1.2, 1.2)
        else:
            t_val = rng.uniform(-20.0, 20.0)
        pts.append((alpha, omega, sigma, t_val))
    return pts


def run_t2(n_pts: int) -> dict:
    mp.mp.dps = DPS_T2
    h_rel = mp.mpf("1e-6")
    rng = random.Random(SEED + 2)
    pts = t2_points(n_pts, rng)
    max_lobe_sqrt = 0.0
    max_lobe_parent = 0.0
    max_hat_euler = 0.0
    max_hat_parent = 0.0
    n_ok_lobe = 0
    n_ok_hat = 0
    n_used = 0
    extra = 0
    for alpha, omega, sigma, t_val in pts:
        a_mp = mp.mpf(alpha)
        w_mp = mp.mpf(omega)
        s_mp = mp.mpf(sigma)
        t_mp = mp.mpf(t_val)

        def lobe_sqrt(aa: mp.mpf, ww: mp.mpf) -> mp.mpc:
            z_val = s_mp + mp.j * (t_mp - ww)
            return mp.e ** (z_val ** 2 / (2 * aa)) / mp.sqrt(aa)

        def lobe_a(aa: mp.mpf, ww: mp.mpf) -> mp.mpc:
            z_val = s_mp + mp.j * (t_mp - ww)
            return mp.e ** (z_val ** 2 / (2 * aa)) / aa

        def hat_fn(aa: mp.mpf, ww: mp.mpf) -> mp.mpc:
            return r605.hat_delta_mp(aa, ww, s_mp, t_mp)

        d_a, d2, val = fd_heat(lobe_sqrt, a_mp, w_mp, h_rel)
        r_sqrt = rel_heat(d_a, d2, val, a_mp, euler=False)
        d_a, d2, val = fd_heat(lobe_a, a_mp, w_mp, h_rel)
        r_parent_lobe = rel_heat(d_a, d2, val, a_mp, euler=False)
        d_a, d2, val = fd_heat(hat_fn, a_mp, w_mp, h_rel)
        r_hat_eu = rel_heat(d_a, d2, val, a_mp, euler=True)
        r_hat_st = rel_heat(d_a, d2, val, a_mp, euler=False)
        mag = abs(val)
        if mag < mp.mpf("1e-20"):
            extra += 1
            if extra > 40:
                break
            alpha = math.exp(rng.uniform(math.log(0.08), math.log(0.6)))
            omega = rng.uniform(6.0, 25.0)
            sigma = rng.uniform(-0.35, 0.35)
            t_val = omega + rng.uniform(-0.8, 0.8)
            pts.append((alpha, omega, sigma, t_val))
            continue
        n_used += 1
        max_lobe_sqrt = max(max_lobe_sqrt, r_sqrt)
        max_lobe_parent = max(max_lobe_parent, r_parent_lobe)
        max_hat_euler = max(max_hat_euler, r_hat_eu)
        max_hat_parent = max(max_hat_parent, r_hat_st)
        if r_sqrt < HEAT_REL_TOL:
            n_ok_lobe += 1
        if r_hat_eu < HEAT_REL_TOL:
            n_ok_hat += 1
    ok = (
        n_used >= n_pts
        and max_lobe_sqrt < HEAT_REL_TOL
        and max_hat_euler < 1e-4
    )
    return {
        "n_pts": n_pts,
        "n_used": n_used,
        "max_lobe_sqrt": max_lobe_sqrt,
        "max_lobe_parent": max_lobe_parent,
        "max_hat_euler": max_hat_euler,
        "max_hat_parent": max_hat_parent,
        "n_ok_lobe": n_ok_lobe,
        "n_ok_hat": n_ok_hat,
        "ok": ok,
    }


# ---------------------------------------------------------------------------
# T3 arithmetic side — copied from r601 / r548 (no scipy)
# g = Lean `pureGaborAutocorrelation`; Pole closed form; comb 2Λ/√n.
# ---------------------------------------------------------------------------
def g_pure_gabor(u_value: float, alpha: float, omega: float) -> float:
    """Lean `pureGaborAutocorrelation` (r601)."""
    pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
    return pref * exp_clip(-0.5 * alpha * u_value * u_value) * (
        math.cos(omega * u_value) + exp_clip(-(omega * omega) / (2.0 * alpha))
    )


def pole_closed(alpha: float, omega: float) -> float:
    """Pole = ĥ(0)+ĥ(1) = (π/a) e^{1/(8a)−ω²/(2a)} (1+cos(ω/(2a)))."""
    return (
        (math.pi / alpha)
        * exp_clip(1.0 / (8.0 * alpha) - (omega * omega) / (2.0 * alpha))
        * (1.0 + math.cos(omega / (2.0 * alpha)))
    )


def hat_online(t_value: float, alpha: float, omega: float) -> float:
    """r601 / Lean `pureGaborOnLine`."""
    pref = math.pi / (4.0 * alpha)
    return pref * (
        exp_clip(-(t_value + omega) ** 2 / (2.0 * alpha))
        + exp_clip(-(t_value - omega) ** 2 / (2.0 * alpha))
        + 2.0 * exp_clip(-(t_value * t_value + omega * omega) / (2.0 * alpha))
    )


def hat_online_vec(t_values, alpha: float, omega: float) -> np.ndarray:
    t_arr = np.asarray(t_values, dtype=np.float64)
    pref = math.pi / (4.0 * alpha)
    two_a = 2.0 * alpha
    return pref * (
        np.exp(-(t_arr + omega) ** 2 / two_a)
        + np.exp(-(t_arr - omega) ** 2 / two_a)
        + 2.0 * np.exp(-(t_arr * t_arr + omega * omega) / two_a)
    )


def k_kernel(t_values) -> np.ndarray:
    """k(t) = Re ψ(1/4+it/2) − log π.  Stirling + recurrence, no scipy."""
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
    """r548/r601 sieve."""
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
    """r601: ∫_{u0}^∞ exp(−a u²/2 + linear·u) du via erfc."""
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
    """r601: PNT tail 2 ∫_{u0}^∞ g(u) e^{u/2} du via complex erfc."""
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


def pnt_weight(alpha: float, x_val: float) -> float:
    """e^{−a X²/2} e^{X/2} envelope used to choose the prime cutoff."""
    return exp_clip(-0.5 * alpha * x_val * x_val + 0.5 * x_val)


def required_X(alpha: float, target: float = TAIL_TARGET) -> float:
    """Decaying-side root of −a X²/2 + X/2 = log(target), X > 1/(2a)."""
    logt = math.log(target)
    disc = 1.0 - 8.0 * alpha * logt
    return (1.0 + math.sqrt(max(disc, 0.0))) / (2.0 * alpha)


def choose_prime_cutoff(
    alpha: float, n_cap: int,
) -> dict:
    x20 = required_X(alpha, TAIL_TARGET)
    n20 = math.exp(min(x20, 40.0))
    x_sad = 1.0 / (2.0 * alpha)
    n_sad = math.exp(min(x_sad, 40.0))
    x_cap = math.log(max(n_cap, 2))
    if n20 <= n_cap:
        n_used = max(32, min(int(math.ceil(n20)), n_cap))
        return {
            "status": "TAIL_1e-20",
            "n_used": n_used,
            "X": math.log(n_used),
            "X_1e-20": x20,
            "n_1e-20": n20,
            "X_saddle": x_sad,
            "weight_cut": pnt_weight(alpha, math.log(n_used)),
        }
    if n_sad > n_cap:
        return {
            "status": "SKIPPED_PRIMES",
            "n_used": 0,
            "X": x20,
            "X_1e-20": x20,
            "n_1e-20": n20,
            "X_saddle": x_sad,
            "weight_cut": pnt_weight(alpha, x_cap),
        }
    return {
        "status": "CAPPED",
        "n_used": int(n_cap),
        "X": x_cap,
        "X_1e-20": x20,
        "n_1e-20": n20,
        "X_saddle": x_sad,
        "weight_cut": pnt_weight(alpha, x_cap),
    }


def prime_channels(
    alpha: float,
    omega: float,
    u_all: np.ndarray,
    weight: np.ndarray,
    n_used: int,
) -> tuple[float, float, float]:
    """Signed comb, Σ|terms|, Chebyshev envelope tail.  r601."""
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
    env_pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha)) * (1.0 + dc)
    i_half = gauss_exp_linear_tail(u_cut, alpha, 0.5)
    env_tail = 4.0 * env_pref * i_half
    return prime, prime_abs, env_tail


def _arch_segments(alpha: float, omega: float) -> list[tuple[float, float]]:
    width = 16.0 * math.sqrt(max(alpha, 1.0e-18))
    omega_abs = abs(float(omega))
    if omega_abs > 2.0 * width:
        return [(0.0, width), (omega_abs - width, omega_abs + width)]
    return [(0.0, max(omega_abs + width, width))]


def arch_trapz(alpha: float, omega: float, n_per: int) -> float:
    """(1/π) ∫_0^∞ ĥ k dt by evenness = (1/2π) ∫_R.  r601 segmentation."""
    total = 0.0
    for t_lo, t_hi in _arch_segments(alpha, omega):
        if t_hi <= t_lo:
            continue
        n_pts = max(
            65,
            int(n_per * max(t_hi - t_lo, 1.0) / max(math.sqrt(alpha), 0.25)),
        )
        ts = np.linspace(t_lo, t_hi, n_pts)
        total += trapz(hat_online_vec(ts, alpha, omega) * k_kernel(ts), ts)
    return total / math.pi


def zero_sum_online(
    alpha: float, omega: float, gammas: tuple[float, ...],
) -> float:
    total = 0.0
    for height in gammas:
        total += 2.0 * hat_online(float(height), alpha, omega)
    return total


def re_hat_delta(sigma: float, t_value: float, alpha: float, omega: float) -> float:
    """r601 `re_pureGaborHatDelta`."""
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


def fit_slope_inv_a(a_list: list[float], y_list: list[float]) -> float | None:
    """Least-squares slope of y vs 1/a (for log B ~ c/a)."""
    pairs = [
        (1.0 / a_val, y_val)
        for a_val, y_val in zip(a_list, y_list)
        if a_val > 0.0 and math.isfinite(y_val)
    ]
    if len(pairs) < 2:
        return None
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    n_val = len(xs)
    xbar = sum(xs) / n_val
    ybar = sum(ys) / n_val
    den = sum((x_val - xbar) ** 2 for x_val in xs)
    if den <= 0.0:
        return None
    num = sum((x_val - xbar) * (y_val - ybar) for x_val, y_val in zip(xs, ys))
    return num / den


# ---------------------------------------------------------------------------
# T1 Laplace
# ---------------------------------------------------------------------------
def run_t1(
    online: tuple[float, ...],
    a_grid: tuple[float, ...],
    omega_grid: tuple[float, ...],
) -> dict:
    mp.mp.dps = DPS_T1
    a1 = mp.mpf("1")
    w0 = mp.mpf("0")
    hat1 = r605.hat_delta_mp(a1, w0, mp.mpf("0.5"), mp.mpf("0"))
    target = mp.pi * mp.e ** (mp.mpf("1") / 8)
    err = abs(hat1 - target)
    checkpoint_ok = err < mp.mpf("1e-12") and abs(mp.im(hat1)) < mp.mpf("1e-12")

    configs = t1_configs(online)
    cells: list[dict] = []
    max_d_plus: dict[float, float] = {a_val: 0.0 for a_val in a_grid}
    c_cells: list[float] = []
    fail_where: list[str] = []
    on_from_above = True
    on_f_nonpos = True

    for name, off, on_use in configs:
        points = catalog_points(off, on_use)
        for omega in omega_grid:
            f_env = envelope_F(points, omega)
            if name == "ON":
                dist = min(abs(abs(p[1]) - omega) for p in points)
                f_check = -(dist ** 2)
                if abs(f_env - f_check) > 1e-12:
                    fail_where.append("ON_F_formula@w=%s" % fmt(omega, 4))
                if f_env > 1e-14:
                    on_f_nonpos = False
            for a_val in a_grid:
                z_sc, abs_sc, n_used = sum_zero_side(points, a_val, omega, f_env)
                l_signed = L_from_scaled(f_env, a_val, z_sc)
                l_plus = L_from_scaled(f_env, a_val, abs_sc)
                d_plus = abs(l_plus - f_env) if math.isfinite(l_plus) else math.inf
                denom = a_val * math.log(1.0 / a_val)
                c_here = d_plus / denom if denom > 0.0 else math.inf
                c_cells.append(c_here)
                if d_plus > max_d_plus[a_val]:
                    max_d_plus[a_val] = d_plus
                vanish = (not math.isfinite(l_signed)) or abs(z_sc) < 1e-30
                if name == "ON" and (not vanish) and l_signed + 1e-8 < f_env:
                    on_from_above = False
                cells.append({
                    "name": name,
                    "omega": omega,
                    "a": a_val,
                    "F": f_env,
                    "L": l_signed,
                    "Lp": l_plus,
                    "dLp": d_plus,
                    "C": c_here,
                    "n_used": n_used,
                    "vanish": vanish,
                })
                if not math.isfinite(l_plus):
                    fail_where.append("%s a=%s w=%s Lplus" % (
                        name, fmt(a_val, 3), fmt(omega, 4),
                    ))

    c_fit = max(c_cells) if c_cells else math.inf
    holds = (
        checkpoint_ok
        and not fail_where
        and math.isfinite(c_fit)
        and c_fit <= C_LAPLACE_MAX
        and on_f_nonpos
    )
    # unsigned envelope should shrink toward F as a decreases
    a_sorted = sorted(a_grid, reverse=True)
    decay_ok = True
    if len(a_sorted) >= 2:
        d_hi = max_d_plus[a_sorted[0]]
        d_lo = max_d_plus[a_sorted[-1]]
        if d_lo > d_hi * 1.5 + 1e-9:
            decay_ok = False
            fail_where.append("Lplus_not_decaying")
    holds = holds and decay_ok
    return {
        "checkpoint_ok": bool(checkpoint_ok),
        "hat1_err": float(err),
        "cells": cells,
        "max_d_plus": max_d_plus,
        "C": float(c_fit),
        "holds": holds,
        "fail_where": fail_where,
        "on_from_above": on_from_above,
        "on_f_nonpos": on_f_nonpos,
        "decay_ok": decay_ok,
    }


# ---------------------------------------------------------------------------
# T3 source-side budget
# ---------------------------------------------------------------------------
def run_t3(
    online: tuple[float, ...],
    a_grid: tuple[float, ...],
    omega_grid: tuple[float, ...],
    n_cap: int,
    n_arch: int,
) -> dict:
    cuts = {a_val: choose_prime_cutoff(a_val, n_cap) for a_val in a_grid}
    n_sieve = 0
    for a_val, cut in cuts.items():
        if cut["status"] != "SKIPPED_PRIMES":
            n_sieve = max(n_sieve, int(cut["n_used"]))
    u_all = np.zeros(0, dtype=np.float64)
    weight = np.zeros(0, dtype=np.float64)
    n_prime_terms = 0
    if n_sieve >= 2:
        lam = von_mangoldt_table(n_sieve)
        u_all, weight = pack_primes(lam)
        n_prime_terms = int(u_all.size)

    # k_kernel vs mpmath at a few t
    mp.mp.dps = 25
    k_err = 0.0
    for t_ck in (0.0, 14.13, 100.0):
        z_ck = mp.mpf("0.25") + mp.j * mp.mpf(t_ck) / 2
        k_mp = float(mp.re(mp.digamma(z_ck)) - mp.log(mp.pi))
        k_np = float(k_kernel([t_ck])[0])
        k_err = max(k_err, abs(k_np - k_mp))

    cells: list[dict] = []
    skipped: list[dict] = []
    for a_val in a_grid:
        cut = cuts[a_val]
        if cut["status"] == "SKIPPED_PRIMES":
            skipped.append({"a": a_val, **cut, "n_primes": 0})
            continue
        n_used = int(cut["n_used"])
        n_primes = int(np.sum(u_all <= math.log(n_used) + 1e-15))
        for omega in omega_grid:
            pole = pole_closed(a_val, omega)
            prime, prime_abs, env_tail = prime_channels(
                a_val, omega, u_all, weight, n_used,
            )
            u_cut = math.log(max(n_used, 2))
            pnt_tail = comb_smooth_tail(u_cut, a_val, omega)
            arch = arch_trapz(a_val, omega, n_arch)
            z_src = pole + arch - (prime + pnt_tail)
            z_zeros = zero_sum_online(a_val, omega, online)
            ef_res = abs(z_zeros - z_src)
            mag_z = abs(z_zeros)
            budget = prime_abs / mag_z if mag_z > 0.0 else math.inf
            cells.append({
                "a": a_val,
                "omega": omega,
                "status": cut["status"],
                "n_used": n_used,
                "X": cut["X"],
                "n_primes": n_primes,
                "weight_cut": cut["weight_cut"],
                "X_1e-20": cut["X_1e-20"],
                "n_1e-20": cut["n_1e-20"],
                "env_tail": env_tail,
                "pnt_tail": pnt_tail,
                "pole": pole,
                "arch": arch,
                "prime": prime,
                "prime_abs": prime_abs,
                "Z_src": z_src,
                "Z_zeros": z_zeros,
                "ef_res": ef_res,
                "B": budget,
            })

    # synthetic ¬RH bookkeeping injection at ω = 99.975.
    # Spectral Z_zeros is used (2000 ordinates suffice at this height);
    # PRIME' := PRIME − 4 Re ĥ(β) is bookkeeping, not a change of Λ(n).
    points_on = catalog_points([], online)
    f_true = envelope_F(points_on, OMEGA_SYN)
    syn_rows: list[dict] = []
    for a_val in a_grid:
        cut = cuts[a_val]
        omega = OMEGA_SYN
        z_true = zero_sum_online(a_val, omega, online)
        inj = 4.0 * FAKE_M * re_hat_delta(
            FAKE_BETA_SIGMA, FAKE_BETA_T, a_val, omega,
        )
        z_syn = z_true + inj
        l_true = (
            2.0 * a_val * math.log(abs(z_true))
            if abs(z_true) > 0.0 else float("-inf")
        )
        l_syn = (
            2.0 * a_val * math.log(abs(z_syn))
            if abs(z_syn) > 0.0 else float("-inf")
        )
        syn_rows.append({
            "a": a_val,
            "status": cut["status"],
            "Z_true": z_true,
            "Z_syn": z_syn,
            "inj": inj,
            "L_true": l_true,
            "L_syn": l_syn,
            "F_true": f_true,
            "sigma2": FAKE_BETA_SIGMA ** 2,
        })

    def _fit_rows(rows: list[dict]) -> float | None:
        aa = []
        lb = []
        for row in rows:
            if row["B"] > 0.0 and math.isfinite(row["B"]):
                if row["env_tail"] > 0.05 * max(row["prime_abs"], 1.0):
                    continue
                aa.append(row["a"])
                lb.append(math.log(row["B"]))
        return fit_slope_inv_a(aa, lb)

    fit_om = OMEGA_T3[0]
    c_exp = _fit_rows(
        [row for row in cells if abs(row["omega"] - fit_om) < 1e-12]
    )
    c_by_omega: dict[float, float | None] = {}
    for omega in omega_grid:
        c_by_omega[omega] = _fit_rows(
            [row for row in cells if abs(row["omega"] - omega) < 1e-12]
        )

    tight = [row for row in cells if row["env_tail"] <= 1e-6]
    ef_ok = (not tight) or all(row["ef_res"] <= EF_ABS_TOL for row in tight)
    poly_ok = True
    for row in syn_rows:
        l_true = row["L_true"]
        a_val = row["a"]
        bound = C_LAPLACE_MAX * a_val * math.log(1.0 / a_val)
        if not math.isfinite(l_true) or l_true > bound:
            poly_ok = False

    return {
        "cuts": cuts,
        "n_sieve": n_sieve,
        "n_prime_terms": n_prime_terms,
        "k_err": k_err,
        "cells": cells,
        "skipped": skipped,
        "syn": syn_rows,
        "c": c_exp,
        "c_by_omega": c_by_omega,
        "ef_ok": ef_ok,
        "poly_ok": poly_ok,
    }


def run(smoke: bool) -> int:
    LINES.clear()
    CHECKS.clear()

    if smoke:
        a_t1 = (0.2, 0.05)
        om_t1 = (99.975, 100.0)
        n_on = 80
        n_t2 = 6
        a_t3 = (0.2,)
        om_t3 = (14.1347, 100.0)
        n_cap = 20000
        n_arch = 24
    else:
        a_t1 = A_T1
        om_t1 = OMEGA_T1
        n_on = N_ONLINE
        n_t2 = N_T2
        a_t3 = A_T3
        om_t3 = OMEGA_T3
        n_cap = N_PRIME_CAP
        n_arch = 48

    emit("gabor_tropical_heat_probe r608")
    emit("KEIN RH-CLAIM")
    emit("SPEC_DESIGN %s" % SPEC_SHA[:16])
    emit("file_sha %s" % file_sha256()[:16])
    emit("smoke %d" % int(smoke))
    emit(
        "zeros_source verified_zeros_n7000.npy[:%d] mpmath.zetazero dps=15"
        % n_on
    )
    emit("hat r605N Lean pureGaborHatDelta L114-123 third-lobe phase I*sigma*t/a")
    emit(
        "HEAT  traveling lobe phi=a^{-1/2} exp((sigma+i(t-w))^2/(2a)) "
        "satisfies d_a phi = (1/2) d_ww phi;  hat = (pi/4) a^{-1} Sigma E "
        "obeys d_a hat = (1/2) d_ww hat - hat/(2a) when a traveling lobe "
        "dominates.  Parent /a form needs the Euler term.  Z(a,.) is a "
        "heat-flow in a with singular a->0+ data Sigma m delta_{pm gamma} "
        "under RH; off-line zeros are complex-shifted deltas (Tychonoff "
        "e^{sigma^2/(2a)}) — a maximum principle for a>0 cannot see them."
    )
    emit(
        "(H) limsup 2a log|H| <= 0 on the source side is the "
        "Gaussian-smoothed magnitude statement psi(x)-x = O(sqrt(x) x^{o(1)}); "
        "by PRIME.NOGO.COMPOSITE.01 (T1) magnitude-class inputs are "
        "RH-strength — this probe measures, it does not prove."
    )
    emit("g_carrier r601 (1/2)sqrt(pi/(2a)) e^{-a u^2/2} (cos(w u)+e^{-w^2/(2a)})")
    emit("g_vs_parent DC term is e^{-w^2/(2a)}, not +1 (third lobe)")

    online = r605.load_online(n_on)
    emit("n_online %d gamma_1=%s gamma_N=%s" % (
        len(online), fmt(online[0], 6), fmt(online[-1], 6),
    ))

    emit("T1 LAPLACE")
    t1 = run_t1(online, a_t1, om_t1)
    emit("  hat_{1,0}(1) err=%s" % fmt(t1["hat1_err"], 4))
    check("T1-checkpoint", t1["checkpoint_ok"], "err=%s" % fmt(t1["hat1_err"], 4))
    emit("  max|L+-F| per a:")
    for a_val in a_t1:
        d_val = t1["max_d_plus"][a_val]
        denom = a_val * math.log(1.0 / a_val)
        emit(
            "    a=%s  max|Lp-F|=%s  / (a log(1/a))=%s"
            % (fmt(a_val, 4), fmt(d_val, 6), fmt(d_val / denom, 4))
        )
    emit("  C_fit=%s  ON F<=0 %d  ON L from above %d  decay %d" % (
        fmt(t1["C"], 4),
        int(t1["on_f_nonpos"]),
        int(t1["on_from_above"]),
        int(t1["decay_ok"]),
    ))
    # a few representative cells
    for cell in t1["cells"]:
        if cell["a"] not in (a_t1[0], a_t1[-1]):
            continue
        if cell["omega"] not in (om_t1[0], 100.0, om_t1[-1]):
            continue
        emit(
            "  %s a=%s w=%s F=%s L=%s Lp=%s dLp=%s vanish=%d n=%d"
            % (
                cell["name"], fmt(cell["a"], 3), fmt(cell["omega"], 4),
                fmt(cell["F"], 5), fmt(cell["L"], 5), fmt(cell["Lp"], 5),
                fmt(cell["dLp"], 5), int(cell["vanish"]), cell["n_used"],
            )
        )
    check("T1-ON-F-nonpos", t1["on_f_nonpos"], "")
    check("T1-C-bounded", t1["C"] <= C_LAPLACE_MAX, "C=%s" % fmt(t1["C"], 4))
    check("T1-Lplus-decay", t1["decay_ok"], "")
    if t1["holds"]:
        t1_verd = "LAPLACE_HOLDS C=%s" % fmt(t1["C"], 4)
    else:
        where = ",".join(t1["fail_where"][:6]) if t1["fail_where"] else "C_or_decay"
        t1_verd = "LAPLACE_FAILS(%s)" % where
    emit("T1 VERDICT %s" % t1_verd)

    emit("T2 HEAT")
    t2 = run_t2(n_t2)
    emit(
        "  n=%d used=%d  max_rel lobe_sqrt=%s lobe_parent_/a=%s "
        "hat_euler=%s hat_parent=%s"
        % (
            t2["n_pts"], t2["n_used"],
            fmt(t2["max_lobe_sqrt"], 4),
            fmt(t2["max_lobe_parent"], 4),
            fmt(t2["max_hat_euler"], 4),
            fmt(t2["max_hat_parent"], 4),
        )
    )
    emit(
        "  parent stated PDE on /a-lobe and on hat is the Euler-uncorrected "
        "form; traveling-lobe heat kernel is a^{-1/2} exp(...)."
    )
    check(
        "T2-lobe-sqrt-heat",
        t2["max_lobe_sqrt"] < HEAT_REL_TOL,
        "max=%s" % fmt(t2["max_lobe_sqrt"], 4),
    )
    check(
        "T2-hat-euler",
        t2["max_hat_euler"] < 1e-4,
        "max=%s" % fmt(t2["max_hat_euler"], 4),
    )
    t2_ok = t2["ok"]
    t2_verd = "HEAT_IDENTITY_OK" if t2_ok else "HEAT_IDENTITY_FAILS"
    emit("T2 VERDICT %s" % t2_verd)

    emit("T3 SOURCE")
    t3 = run_t3(online, a_t3, om_t3, n_cap, n_arch)
    emit("  k_kernel vs mp.digamma max|d|=%s" % fmt(t3["k_err"], 4))
    check("T3-k-kernel", t3["k_err"] < 1e-10, "err=%s" % fmt(t3["k_err"], 4))
    emit("  sieve n<=%d prime_powers=%d" % (t3["n_sieve"], t3["n_prime_terms"]))
    for a_val, cut in t3["cuts"].items():
        emit(
            "  cutoff a=%s status=%s X=%s n_used=%d X_1e-20=%s n_1e-20=%s "
            "saddle=%s wt=%s"
            % (
                fmt(a_val, 3), cut["status"], fmt(cut["X"], 4),
                int(cut["n_used"]), fmt(cut["X_1e-20"], 4),
                fmt(cut["n_1e-20"], 3), fmt(cut["X_saddle"], 4),
                fmt(cut["weight_cut"], 3),
            )
        )
    for row in t3["skipped"]:
        emit(
            "  SKIP a=%s primes needed n_1e-20=%s > cap  (saddle n=e^{1/(2a)}=%s)"
            % (fmt(row["a"], 3), fmt(row["n_1e-20"], 3),
               fmt(math.exp(min(row["X_saddle"], 40.0)), 3))
        )
    emit("  EF / budget:")
    for row in t3["cells"]:
        emit(
            "    a=%s w=%s n_pr=%d |POLE|=%s |ARCH|=%s |PRIME|=%s "
            "Sigma|t|=%s |Z0|=%s B=%s EF|Z0-(P+A-Pr-pnt)|=%s pnt=%s env_tail=%s"
            % (
                fmt(row["a"], 3), fmt(row["omega"], 4), row["n_primes"],
                fmt(abs(row["pole"]), 4), fmt(abs(row["arch"]), 4),
                fmt(abs(row["prime"]), 4), fmt(row["prime_abs"], 4),
                fmt(abs(row["Z_zeros"]), 4), fmt(row["B"], 4),
                fmt(row["ef_res"], 4), fmt(row["pnt_tail"], 3),
                fmt(row["env_tail"], 3),
            )
        )
    c_exp = t3["c"]
    emit("  c_fit log B vs 1/a at w=14.1347: c=%s  (parent ~1/16=6.25e-2; "
         "e^{-a u^2/2}+e^{u/2} saddle is 1/(8a) => c~1/8)"
         % (fmt(c_exp, 4) if c_exp is not None else "na"))
    for omega, c_w in t3["c_by_omega"].items():
        emit("    c(w=%s)=%s" % (
            fmt(omega, 4), fmt(c_w, 4) if c_w is not None else "na",
        ))
    emit("  synthetic bookkeeping fake pair beta=0.9 +/- 100 i  "
         "(PRIME' = PRIME - 4 Re hat; NOT a change of Lambda; L from Z_zeros):")
    for row in t3["syn"]:
        emit(
            "    a=%s status=%s L_true=%s F_on=%s L_syn=%s sigma^2=%s inj=%s"
            % (
                fmt(row["a"], 3), row["status"], fmt(row["L_true"], 5),
                fmt(row["F_true"], 5), fmt(row["L_syn"], 5),
                fmt(row["sigma2"], 4), fmt(row["inj"], 4),
            )
        )
    ef_all = t3["ef_ok"]
    check("T3-EF-sanity", ef_all, "tight cells |res|<=%s" % fmt(EF_ABS_TOL, 2))
    check("T3-true-source-poly", t3["poly_ok"], "L <= C a log(1/a)")

    c_str = fmt(c_exp, 4) if c_exp is not None else "na"
    if t1["holds"] and t2_ok:
        verdict = "TROPICAL_CONFIRMED(c=%s)" % c_str
    elif not t1["holds"]:
        verdict = t1_verd.split()[0] if t1_verd.startswith("LAPLACE_FAILS") else t1_verd
    else:
        verdict = "HEAT_IDENTITY_FAILS"

    emit("VERDICT: %s" % verdict)
    emit("KEIN RH-CLAIM")
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    emit("CHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        emit("GATE_FAILURES " + ",".join(n for n, ok in CHECKS if not ok))
    else:
        emit("ALL CHECKS PASSED")

    body = "\n".join(LINES) + "\n"
    spec = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
    print("SPEC %s" % spec)
    return 0 if (t1["holds"] and t2_ok and n_fail == 0) else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "r608 Gabor tropical / heat / source-budget scout "
            "(experiments only, no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
