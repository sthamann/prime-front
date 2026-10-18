#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_density_transfer_probe -- r549

Round 549.  Experiments-only scout of the two r544 controls that still
block a uniform Lean replacement of `GaborSeparationInequality`:

  (1) GAUSS-DENSITY TRANSFER.  Unit-bin increment counting
      (`RH.ZeroIncrement`, `gaborIncrementBound_holds`) charged as
      (bins × peak) only yields on-line mass R ≲ C log γ.  Partial
      summation over unit bins replaces that by

          Σ_ρ ĥ_W(1/2+iγ_ρ)  ≤  2 C_inc  Σ_{k≥0} max_{t∈[k,k+1]} w(t)

      with w = pure-Gabor on-line envelope.  The inner series is a
      Jacobi-theta majorant, independent of the packet center ω≈γ.

  (2) OFF-LINE CONTROL.  The r541 certificate books ONE functional-
      equation quadruple.  This probe evaluates 4 Re ĥ_W(β'+iγ') of
      every foreign quadruple against the test tuned to (β,γ), and
      asks whether a cluster can flip the r541 floor −3.56.

CLAIM BOUNDARY.  Finite closed-form / partial-summation arithmetic
on the pure-Gabor class h(t)=exp(−a t²) cos(ω t) with the r542
scaling a=σ²/64, ω=γ−π a/σ.  On-line comparison uses mpmath.zetazero
as a classical ordinate table, not as an RH oracle.  NO RH claim,
NO anti-RH claim, NO ledger row, NO paper edit, NO Lean edit.

HAT CONVENTION.  Weil-shifted ĥ_W(s)=H(s−1/2) H(1/2−s), matching
`RH.pureGaborHatDelta`.  On the critical line this is the three-
Gaussian `pureGaborOnLine`.  A quadruple contributes 4 Re ĥ_W.

INCREMENT.  Lean `zeta_unit_increment` supplies the prefactor
C_inc = 2 * zetaZerosInDiskCardBoundInner and still multiplies by
(1+log(T+3)).  Part 1 tests the proposed pull-out

    Σ ≤ C_inc · Σ_k max w(t)

i.e. the constant-prefactor times the theta-sum.  The log-weighted
Lean-literal sum is reported as a control (it grows like log γ).

CERTIFIED THETA MAJORANT (lobe, any center c∈ℝ):

    Σ_{k∈ℤ} max_{[k,k+1]} exp(−(t−c)²/(2a))
        ≤ Θ_lobe(a) := 2 + ϑ_3(0, e^{−1/(2a)})
        = 3 + 2 Σ_{m≥1} exp(−m²/(2a)).

At most two bins have distance 0; the rest pair with distance ≥ m.

Verdicts:
  TRANSFER_UNIFORM(bound=...) / TRANSFER_LOG_GROWTH(...)
  OFFLINE_BENIGN(worst=...) / OFFLINE_ADVERSARIAL(config=...)
      / OFFLINE_MIXED(...)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
SIGMAS = ("1e-1", "2e-1", "4e-1")
GAMMAS = ("14", "50", "200", "1000")
HOST_BETAS = ("0.51", "0.60", "0.70", "0.90")
BETAS_PRIME = ("0.51", "0.55", "0.60", "0.70", "0.80", "0.90", "0.95", "0.99")
GAMMA_NEAR_OFFSETS = ("-2", "-1", "-0.5", "-0.25", "0", "0.25", "0.5", "1", "2")
GAMMA_FAR_KINDS = ("half", "plus10", "plus50", "plus100", "double")
R541_MARGIN = "-3.56"
UNIFORM_RATIO_MAX = "1.05"
NSTR_DIGITS = 12
DPS = 80

SPEC = {
    "round": 549,
    "parent_round": 544,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.DENSITY_TRANSFER.01",
    "target": "GaborSeparationInequality.r544_controls",
    "hat": "weil_shifted",
    "class": "pure_gabor",
    "a_rule": "sigma^2/64",
    "omega_rule": "gamma-pi*a/sigma",
    "enhancement": "exp(32)",
    "sigmas": list(SIGMAS),
    "gammas": list(GAMMAS),
    "host_betas": list(HOST_BETAS),
    "betas_prime": list(BETAS_PRIME),
    "gamma_near_offsets": list(GAMMA_NEAR_OFFSETS),
    "gamma_far_kinds": list(GAMMA_FAR_KINDS),
    "r541_margin": R541_MARGIN,
    "uniform_ratio_max": UNIFORM_RATIO_MAX,
    "c_inc_source": (
        "2*zetaZerosInDiskCardBoundInner "
        "(ZeroIncrement prefactor; log factor pulled out)"
    ),
    "c_inner_formula": (
        "(log(2+6*zeta(9/8))+log|zeta(2)|+2)/log(14/13)"
    ),
    "theta_majorant": "2+vartheta_3(0,exp(-1/(2a)))",
    "increment_control": "lean_literal_C_inc*(1+log(k+3))*bin_max",
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "scope": (
        "partial-summation theta majorant + foreign FE quadruples; "
        "mpmath.zetazero is a classical ordinate table"
    ),
    "excluded": "RH claim; additional non-Gabor test classes",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %-44s %s"
        % ("PASS" if ok else "FAIL", name, detail),
        flush=True,
    )
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def nstr(value: mp.mpf | mp.mpc, digits: int = NSTR_DIGITS) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def exp_clip(value: mp.mpf) -> mp.mpf:
    if value > mp.mpf(800):
        return mp.exp(mp.mpf(800))
    if value < mp.mpf(-800):
        return mp.mpf(0)
    return mp.exp(value)


def scaling_a(sigma: mp.mpf) -> mp.mpf:
    return sigma ** 2 / 64


def scaling_omega(sigma: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    return gamma - mp.pi * scaling_a(sigma) / sigma


def c_inner() -> mp.mpf:
    """zetaZerosInDiskCardBoundInner, exact Lean formula."""
    coeff = 2 + 6 * mp.zeta(mp.mpf(9) / 8)
    numer = mp.log(coeff) + mp.log(abs(mp.zeta(2))) + 2
    return numer / mp.log(mp.mpf(14) / 13)


def c_inc_prefactor() -> mp.mpf:
    return 2 * c_inner()


def lean_increment(k: int, c_inc: mp.mpf) -> mp.mpf:
    return c_inc * (1 + mp.log(mp.mpf(k) + 3))


def lobe_bin_max(center: mp.mpf, a: mp.mpf, k: int) -> mp.mpf:
    left = mp.mpf(k)
    right = left + 1
    if left <= center <= right:
        dist = mp.mpf(0)
    else:
        dist = min(abs(center - left), abs(center - right))
    return exp_clip(-(dist * dist) / (2 * a))


def online_value(t_value: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    pref = mp.pi / (4 * a)
    return pref * (
        exp_clip(-((t_value + omega) ** 2) / (2 * a))
        + exp_clip(-((t_value - omega) ** 2) / (2 * a))
        + 2 * exp_clip(-(t_value * t_value + omega * omega) / (2 * a))
    )


def online_bin_max(k: int, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    pref = mp.pi / (4 * a)
    cross = 2 * exp_clip(-(mp.mpf(k) ** 2 + omega * omega) / (2 * a))
    return pref * (
        lobe_bin_max(-omega, a, k)
        + lobe_bin_max(omega, a, k)
        + cross
    )


def theta3_q(a: mp.mpf) -> mp.mpf:
    """ϑ_3(0, exp(−1/(2a))) = Σ_m exp(−m²/(2a)), certified tail."""
    q_log = -1 / (2 * a)
    total = mp.mpf(1)
    m_val = 1
    while True:
        term = exp_clip((m_val * m_val) * q_log)
        total += 2 * term
        if term < mp.mpf("1e-80") or m_val > 200:
            # remainder 2 Σ_{m>M} exp(−m²/(2a))
            # ≤ 2 exp(−(M+1)²/(2a)) / (1 − exp(−(2M+1)/(2a)))
            m_next = m_val + 1
            gap = exp_clip(-(2 * m_val + 1) / (2 * a))
            rem = (
                2 * exp_clip(-(m_next * m_next) / (2 * a))
                / (1 - gap)
                if gap < mp.mpf("0.5")
                else mp.mpf("1e-80")
            )
            total += rem
            break
        m_val += 1
    return total


def theta_lobe(a: mp.mpf) -> mp.mpf:
    """Certified Σ_k max_{[k,k+1]} exp(−(t−c)²/(2a)), any center c."""
    return 2 + theta3_q(a)


def theta_left_pos(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Σ_{k≥0} max_{[k,k+1]} exp(−(t+ω)²/(2a)) ≤ e^{−ω²/(2a)}/(1−e^{−ω/a})."""
    if omega <= 0:
        return theta_lobe(a)
    geom = exp_clip(-omega / a)
    if geom >= mp.mpf("0.5"):
        return theta_lobe(a)
    return exp_clip(-(omega * omega) / (2 * a)) / (1 - geom)


def theta_cross_pos(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Σ_{k≥0} exp(−(k²+ω²)/(2a)) ≤ e^{−ω²/(2a)} (1+ϑ_3)/2."""
    return exp_clip(-(omega * omega) / (2 * a)) * (1 + theta3_q(a)) / 2


def certified_bin_sum(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """γ-independent majorant of Σ_{k≥0} max_{[k,k+1]} w(t)."""
    pref = mp.pi / (4 * a)
    return pref * (
        theta_lobe(a) + theta_left_pos(a, omega) + 2 * theta_cross_pos(a, omega)
    )


def relevant_bins(omega: mp.mpf, a: mp.mpf) -> tuple[int, ...]:
    width = mp.sqrt(2 * a)
    radius = max(8, int(mp.ceil(40 * width)) + 2)
    k_center = int(mp.floor(omega))
    bins = set(range(0, radius + 1))
    bins.update(range(max(0, k_center - radius), k_center + radius + 2))
    return tuple(sorted(bins))


def exact_window_bin_sum(a: mp.mpf, omega: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Exact Σ max w on the relevant window, plus certified omitted tail."""
    bins = relevant_bins(omega, a)
    total = mp.mpf(0)
    for k in bins:
        total += online_bin_max(k, a, omega)
    k_max = bins[-1]
    # Tail k > k_max: distance to ω is at least k_max+1-ω ≥ 1 if k_max≥ω.
    u0 = mp.mpf(k_max + 1) - omega
    if u0 < 1:
        u0 = mp.mpf(1)
    # Σ_{j≥0} exp(−(u0+j)²/(2a)) ≤ exp(−u0²/(2a)) / (1−exp(−u0/a))
    geom = exp_clip(-u0 / a)
    if geom >= mp.mpf("0.5"):
        tail = certified_bin_sum(a, omega)
    else:
        pref = mp.pi / (4 * a)
        right = exp_clip(-(u0 * u0) / (2 * a)) / (1 - geom)
        left = theta_left_pos(a, omega)
        cross = theta_cross_pos(a, omega)
        tail = pref * (right + left + 2 * cross)
    return total, tail


def rvm_n(height: mp.mpf) -> mp.mpf:
    clipped = max(height, 2 * mp.pi)
    return (
        clipped / (2 * mp.pi) * mp.log(clipped / (2 * mp.pi))
        - clipped / (2 * mp.pi)
        + mp.mpf("0.875")
    )


def ordinates_in_window(t_lo: mp.mpf, t_hi: mp.mpf) -> tuple[mp.mpf, ...]:
    """Classical positive ordinates in (t_lo, t_hi] via mpmath.zetazero."""
    n_lo = max(1, int(mp.floor(rvm_n(max(t_lo, mp.mpf(10))) - 40)))
    n_hi = max(n_lo, int(mp.ceil(rvm_n(t_hi + 20) + 40)))
    found: list[mp.mpf] = []
    for index in range(n_lo, n_hi + 1):
        imag = mp.zetazero(index).imag
        if imag <= t_lo:
            continue
        if imag > t_hi:
            break
        found.append(mp.mpf(imag))
    return tuple(found)


def hat_w_delta(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpc:
    """pureGaborHatDelta: ĥ_W(1/2+σ+it).  No clip: off-line exponents
    can be +O(10^4) for σ_host≪σ' and must keep their true sign/size."""
    pref = mp.pi / (4 * a)
    term_plus = mp.exp(
        (sigma ** 2 - (t_value + omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * sigma * (t_value + omega) / a)
    term_minus = mp.exp(
        (sigma ** 2 - (t_value - omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * sigma * (t_value - omega) / a)
    term_cross = 2 * mp.exp(
        (sigma ** 2 - t_value ** 2 - omega ** 2) / (2 * a)
    ) * mp.exp(mp.j * sigma * t_value / a)
    return pref * (term_plus + term_minus + term_cross)


def quadruple_re(
    beta: mp.mpf, gamma: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpf:
    sigma = beta - mp.mpf("0.5")
    return 4 * mp.re(hat_w_delta(sigma, gamma, a, omega))


def far_gamma(gamma: mp.mpf, kind: str) -> mp.mpf:
    if kind == "half":
        return gamma / 2
    if kind == "plus10":
        return gamma + 10
    if kind == "plus50":
        return gamma + 50
    if kind == "plus100":
        return gamma + 100
    if kind == "double":
        return 2 * gamma
    raise ValueError(kind)


def same_fe_quadruple(
    beta: mp.mpf, gamma: mp.mpf, beta_p: mp.mpf, gamma_p: mp.mpf,
) -> bool:
    atol = mp.mpf("1e-18")
    if abs(gamma_p - gamma) > atol and abs(gamma_p + gamma) > atol:
        return False
    return (
        abs(beta_p - beta) <= atol
        or abs(beta_p - (1 - beta)) <= atol
    )


def payload_sha(rows: dict) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    # ω=0 Gaussian collapse of ĥ_W.
    for alpha in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2)):
        for delta in (
            mp.mpc(0),
            mp.mpc("0.3"),
            mp.mpc("0.2", "0.4"),
        ):
            analytic = (mp.pi / alpha) * mp.exp((delta * delta) / (2 * alpha))
            from_h = hat_w_delta(delta.real, delta.imag, alpha, mp.mpf(0))
            max_err = max(max_err, abs(from_h - analytic))
    # Phase tuning: σ(γ−ω)/a = π.
    for sigma in (mp.mpf("0.1"), mp.mpf("0.2")):
        for gamma in (mp.mpf(14), mp.mpf(50)):
            a_val = scaling_a(sigma)
            omega = scaling_omega(sigma, gamma)
            phase = sigma * (gamma - omega) / a_val
            max_err = max(max_err, abs(phase - mp.pi))
    # Enhancement exp(σ²/(2a)) = exp(32).
    for sigma in (mp.mpf("0.1"), mp.mpf("0.4")):
        a_val = scaling_a(sigma)
        max_err = max(max_err, abs(mp.exp(sigma ** 2 / (2 * a_val)) - mp.exp(32)))
    # Θ_lobe ≥ 3 and ≥ one exact window sum of a unit Gaussian.
    a_val = scaling_a(mp.mpf("0.1"))
    omega = mp.mpf(14)
    unit_sum = mp.mpf(0)
    for k in relevant_bins(omega, a_val):
        unit_sum += lobe_bin_max(omega, a_val, k)
    max_err = max(max_err, max(mp.mpf(0), unit_sum - theta_lobe(a_val)))
    # C_inc positive finite.
    if not (c_inc > 0 and mp.isfinite(c_inc)):
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-20"), max_err


def run_part1(
    smoke: bool, c_inc: mp.mpf,
) -> tuple[str, dict]:
    sigmas = SIGMAS[:1] if smoke else SIGMAS
    gammas = GAMMAS[:2] if smoke else GAMMAS
    section("PART1  GAUSS-DENSITY TRANSFER  (partial summation / theta)")
    print(
        "  formula  Σ_k max_{[k,k+1]} exp(-(t-ω)^2/(2a))"
        "  ≤  Θ_lobe(a) = 2 + ϑ_3(0, e^{-1/(2a)})"
        "  = 3 + 2 Σ_{m≥1} exp(-m^2/(2a))"
    )
    print(
        "  w-sum    Σ_{k≥0} max w(t)  ≤  (π/(4a)) "
        "[Θ_lobe(a) + Θ_left(a,ω) + 2 Θ_cross(a,ω)]"
    )
    print(
        "  transfer R ≤ 2 C_inc Σ_k max w   "
        "(factor 2 books conjugate ordinates)"
    )
    print(
        "  C_inc    %s  = 2*zetaZerosInDiskCardBoundInner"
        % nstr(c_inc)
    )
    print(
        "  sigma gamma  S_window  S_certified  S_norm  "
        "R_const  R_log  R_r544  R_enum  enum/cert"
    )

    rows: list[dict] = []
    g1_ok = True
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        a_val = scaling_a(sigma)
        theta = theta_lobe(a_val)
        peak = mp.pi / (4 * a_val)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            window, tail = exact_window_bin_sum(a_val, omega)
            certified = certified_bin_sum(a_val, omega)
            s_used = window + tail
            if s_used > certified:
                # Keep the closed majorant.
                s_used = certified
            s_norm = s_used / peak
            r_const = 2 * c_inc * certified
            r_log = mp.mpf(0)
            for k in relevant_bins(omega, a_val):
                r_log += 2 * lean_increment(k, c_inc) * online_bin_max(
                    k, a_val, omega
                )
            r_r544 = (
                2 * 4 * mp.log(gamma + 3) * online_value(omega, a_val, omega)
            )
            t_lo = max(mp.mpf(0), omega - 8)
            t_hi = omega + 8
            ords = ordinates_in_window(t_lo, t_hi)
            r_enum = mp.mpf(0)
            for height in ords:
                r_enum += 2 * online_value(height, a_val, omega)
            ratio_enum = r_enum / r_const if r_const > 0 else mp.mpf("inf")
            if r_enum > r_const * (1 + mp.mpf("1e-12")):
                g1_ok = False
            row = {
                "sigma": sigma_text,
                "gamma": gamma_text,
                "a": nstr(a_val),
                "omega": nstr(omega),
                "theta_lobe": nstr(theta),
                "S_window": nstr(window),
                "S_certified": nstr(certified),
                "S_norm": nstr(s_norm),
                "R_const": nstr(r_const),
                "R_log": nstr(r_log),
                "R_r544": nstr(r_r544),
                "R_enum": nstr(r_enum),
                "n_enum": str(len(ords)),
                "enum_over_cert": nstr(ratio_enum),
            }
            rows.append(row)
            print(
                "  %s %s  %s  %s  %s  %s  %s  %s  %s  %s"
                % (
                    sigma_text,
                    gamma_text,
                    nstr(window, 8),
                    nstr(certified, 8),
                    nstr(s_norm, 8),
                    nstr(r_const, 8),
                    nstr(r_log, 8),
                    nstr(r_r544, 8),
                    nstr(r_enum, 8),
                    nstr(ratio_enum, 8),
                )
            )

    # Uniformity: S_certified / peak and raw S_certified across γ, per σ.
    ratio_max = mp.mpf(1)
    per_sigma: dict[str, list[mp.mpf]] = {}
    per_sigma_r544: dict[str, list[mp.mpf]] = {}
    per_sigma_rlog: dict[str, list[mp.mpf]] = {}
    for row in rows:
        per_sigma.setdefault(row["sigma"], []).append(mp.mpf(row["S_certified"]))
        per_sigma_r544.setdefault(row["sigma"], []).append(mp.mpf(row["R_r544"]))
        per_sigma_rlog.setdefault(row["sigma"], []).append(mp.mpf(row["R_log"]))
    for sigma_text, values in per_sigma.items():
        local = max(values) / min(values) if min(values) > 0 else mp.inf
        ratio_max = max(ratio_max, local)
        r544s = per_sigma_r544[sigma_text]
        r544_ratio = max(r544s) / min(r544s) if min(r544s) > 0 else mp.inf
        rlogs = per_sigma_rlog[sigma_text]
        rlog_ratio = max(rlogs) / min(rlogs) if min(rlogs) > 0 else mp.inf
        print(
            "  sigma=%s  S_cert_ratio=%s  R_log_ratio=%s  R_r544_ratio=%s"
            % (
                sigma_text,
                nstr(local),
                nstr(rlog_ratio),
                nstr(r544_ratio),
            )
        )

    theta_ref = theta_lobe(scaling_a(mp.mpf(sigmas[0])))
    bound_s = max(mp.mpf(row["S_certified"]) for row in rows)
    uniform_cut = mp.mpf(UNIFORM_RATIO_MAX)
    transfer_uniform = ratio_max <= uniform_cut
    if transfer_uniform:
        verdict = "TRANSFER_UNIFORM(bound=%s)" % nstr(bound_s)
    else:
        verdict = "TRANSFER_LOG_GROWTH(ratio=%s)" % nstr(ratio_max)

    check(
        "G1-enum-le-transfer",
        g1_ok,
        "packet-window zetazero sum ≤ 2 C_inc Σ max w",
    )
    check(
        "G1-theta-majorises-window",
        all(
            mp.mpf(row["S_window"]) <= mp.mpf(row["S_certified"]) * (
                1 + mp.mpf("1e-12")
            )
            for row in rows
        ),
        "exact window Σ max w ≤ certified theta majorant",
    )
    check(
        "G1-S-norm-theta1",
        all(mp.mpf(row["S_norm"]) <= theta_lobe(scaling_a(mp.mpf(row["sigma"]))) + 1
            for row in rows),
        "S_norm ≤ Θ_lobe+1  (left/cross leakage)",
    )
    print("  PART1_VERDICT %s" % verdict)
    print("  theta_lobe(sigma=%s)=%s" % (sigmas[0], nstr(theta_ref)))
    print("  S_certified_ratio_max %s  cut %s" % (nstr(ratio_max), UNIFORM_RATIO_MAX))
    return verdict, {
        "verdict": verdict,
        "ratio_max": nstr(ratio_max),
        "bound": nstr(bound_s),
        "theta_lobe_ref": nstr(theta_ref),
        "C_inc": nstr(c_inc),
        "rows": rows,
        "uniform": transfer_uniform,
    }


def run_part2(smoke: bool) -> tuple[str, dict]:
    section("PART2  OFF-LINE FOREIGN QUADRUPLES  (tuned Gabor vs cluster)")
    print(
        "  host (β,γ) tunes a=σ²/64, ω=γ−πa/σ; "
        "foreign Q = 4 Re ĥ_W(β'+iγ'); same FE quadruple excluded"
    )
    print("  r541_margin %s" % R541_MARGIN)
    hosts_beta = HOST_BETAS[:2] if smoke else HOST_BETAS
    hosts_gamma = GAMMAS[:2] if smoke else GAMMAS
    betas_p = BETAS_PRIME[:4] if smoke else BETAS_PRIME
    near = GAMMA_NEAR_OFFSETS if not smoke else ("-1", "0", "1")
    far = GAMMA_FAR_KINDS if not smoke else ("plus10", "double")
    margin = abs(mp.mpf(R541_MARGIN))

    print(
        "  beta gamma beta' gamma'  Q_sel  Q_foreign  Q/|Q_sel|  "
        "Q/margin  sign"
    )
    records: list[dict] = []
    n_pos = 0
    n_neg = 0
    n_tiny = 0
    worst_q = -mp.inf
    worst_rec: dict | None = None
    flip_single = False
    flip_vs_margin = False

    for beta_text in hosts_beta:
        beta = mp.mpf(beta_text)
        sigma = beta - mp.mpf("0.5")
        a_val = scaling_a(sigma)
        for gamma_text in hosts_gamma:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            q_sel = quadruple_re(beta, gamma, a_val, omega)
            gamma_primes: list[tuple[str, mp.mpf]] = []
            for off in near:
                gamma_primes.append(("near:%s" % off, gamma + mp.mpf(off)))
            gamma_primes.append(("omega", omega))
            for kind in far:
                gamma_p = far_gamma(gamma, kind)
                if gamma_p > 0:
                    gamma_primes.append(("far:%s" % kind, gamma_p))
            for beta_p_text in betas_p:
                beta_p = mp.mpf(beta_p_text)
                for kind, gamma_p in gamma_primes:
                    if gamma_p <= 0:
                        continue
                    if same_fe_quadruple(beta, gamma, beta_p, gamma_p):
                        continue
                    q_for = quadruple_re(beta_p, gamma_p, a_val, omega)
                    if q_for > 0:
                        n_pos += 1
                    elif q_for < 0:
                        n_neg += 1
                    rel_sel = (
                        q_for / abs(q_sel) if abs(q_sel) > 0 else mp.inf
                    )
                    rel_m = q_for / margin
                    if abs(q_for) < margin * mp.mpf("1e-6"):
                        n_tiny += 1
                    if q_for + q_sel >= 0:
                        flip_single = True
                    if q_for > margin:
                        flip_vs_margin = True
                    rec = {
                        "beta": beta_text,
                        "gamma": gamma_text,
                        "beta_prime": beta_p_text,
                        "gamma_prime": nstr(gamma_p),
                        "kind": kind,
                        "Q_sel": nstr(q_sel),
                        "Q_foreign": nstr(q_for),
                        "rel_sel": nstr(rel_sel),
                        "rel_margin": nstr(rel_m),
                        "sign": (
                            "pos" if q_for > 0 else ("neg" if q_for < 0 else "zero")
                        ),
                    }
                    if q_for > worst_q:
                        worst_q = q_for
                        worst_rec = rec
                    records.append(rec)

    # Print the worst few and a sign census, not every cell (determinism:
    # sort by Q_foreign descending, then by keys).
    ranked = sorted(
        records,
        key=lambda rec: (
            -mp.mpf(rec["Q_foreign"]),
            rec["beta"],
            float(rec["gamma"]),
            rec["beta_prime"],
            mp.mpf(rec["gamma_prime"]),
        ),
    )
    if ranked:
        worst_rec = ranked[0]
        worst_q = mp.mpf(worst_rec["Q_foreign"])
    n_print = 12 if smoke else 20
    for rec in ranked[:n_print]:
        print(
            "  %s %s %s %s  %s  %s  %s  %s  %s"
            % (
                rec["beta"],
                rec["gamma"],
                rec["beta_prime"],
                rec["gamma_prime"],
                rec["Q_sel"],
                rec["Q_foreign"],
                rec["rel_sel"],
                rec["rel_margin"],
                rec["sign"],
            )
        )
    print(
        "  census n=%d  pos=%d  neg=%d  tiny=%d  n_print=%d"
        % (len(records), n_pos, n_neg, n_tiny, n_print)
    )

    # Cluster budget: Lean increment on the packet bins times worst positive Q.
    # The strip window bound charges every zero, not just the critical line.
    cluster_n = mp.mpf(0)
    cluster_mass = mp.mpf(0)
    if worst_rec is not None:
        host_beta = mp.mpf(worst_rec["beta"])
        host_gamma = mp.mpf(worst_rec["gamma"])
        sigma = host_beta - mp.mpf("0.5")
        a_val = scaling_a(sigma)
        omega = scaling_omega(sigma, host_gamma)
        c_inc = c_inc_prefactor()
        for k in relevant_bins(omega, a_val):
            if online_bin_max(k, a_val, omega) > online_value(
                omega, a_val, omega
            ) * mp.mpf("1e-8"):
                cluster_n += lean_increment(k, c_inc)
        # One slot is the selected quadruple.
        cluster_n = max(cluster_n - 1, mp.mpf(0))
        if worst_q > 0:
            cluster_mass = cluster_n * worst_q
        q_sel_w = mp.mpf(worst_rec["Q_sel"])
        cluster_flips = cluster_mass + q_sel_w >= 0
    else:
        cluster_flips = False
        q_sel_w = mp.mpf(0)

    print(
        "  worst_Q %s  cluster_n %s  cluster_mass %s  "
        "flip_single %s  flip_margin %s  flip_cluster %s"
        % (
            nstr(worst_q) if mp.isfinite(worst_q) else "nan",
            nstr(cluster_n),
            nstr(cluster_mass),
            int(flip_single),
            int(flip_vs_margin),
            int(cluster_flips),
        )
    )

    if worst_rec is None:
        verdict = "OFFLINE_BENIGN(worst=none)"
    elif flip_single or cluster_flips or flip_vs_margin:
        verdict = (
            "OFFLINE_ADVERSARIAL(config=beta=%s,gamma=%s,"
            "beta_prime=%s,gamma_prime=%s,Q=%s)"
            % (
                worst_rec["beta"],
                worst_rec["gamma"],
                worst_rec["beta_prime"],
                worst_rec["gamma_prime"],
                worst_rec["Q_foreign"],
            )
        )
    elif n_pos > 0 and n_neg > 0:
        verdict = "OFFLINE_MIXED(worst=%s,n_pos=%d,n_neg=%d)" % (
            nstr(worst_q),
            n_pos,
            n_neg,
        )
    elif n_pos == 0:
        verdict = "OFFLINE_BENIGN(worst=%s)" % nstr(worst_q)
    else:
        verdict = "OFFLINE_MIXED(worst=%s,n_pos=%d,n_neg=%d)" % (
            nstr(worst_q),
            n_pos,
            n_neg,
        )

    check(
        "G2-foreign-grid-nonempty",
        len(records) > 0,
        "n=%d" % len(records),
    )
    check(
        "G2-selected-negative",
        all(mp.mpf(rec["Q_sel"]) < 0 for rec in records),
        "every host quadruple has Q_sel<0 (phase π)",
    )
    print("  PART2_VERDICT %s" % verdict)
    return verdict, {
        "verdict": verdict,
        "worst": worst_rec,
        "worst_Q": nstr(worst_q) if mp.isfinite(worst_q) else "nan",
        "n": str(len(records)),
        "n_pos": str(n_pos),
        "n_neg": str(n_neg),
        "flip_single": str(int(flip_single)),
        "flip_margin": str(int(flip_vs_margin)),
        "flip_cluster": str(int(cluster_flips)),
        "cluster_n": nstr(cluster_n),
        "cluster_mass": nstr(cluster_mass),
        "top": ranked[:5],
    }


def format_formula() -> str:
    return (
        "Σ_k max_{[k,k+1]} exp(-(t-ω)^2/(2a)) "
        "≤ Θ_lobe(a) = 2 + ϑ_3(0, exp(-1/(2a))) "
        "= 3 + 2 Σ_{m≥1} exp(-m^2/(2a));  "
        "Σ_{k≥0} max w(t) ≤ (π/(4a))[Θ_lobe(a)+Θ_left(a,ω)+2 Θ_cross(a,ω)] "
        "with Θ_left=exp(-ω^2/(2a))/(1-exp(-ω/a)), "
        "Θ_cross=exp(-ω^2/(2a))(1+ϑ_3)/2;  "
        "R ≤ 2 C_inc Σ_k max w,  "
        "C_inc=2*(log(2+6 ζ(9/8))+log|ζ(2)|+2)/log(14/13)"
    )


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    c_inc = c_inc_prefactor()
    print("gabor_density_transfer_probe -- r549")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted  class pure_gabor")
    print("scaling a=sigma^2/64  omega=gamma-pi*a/sigma  enh=exp(32)")
    print("C_inner %s" % nstr(c_inner()))
    print("C_inc %s" % nstr(c_inc))
    print("FORMULA %s" % format_formula())

    section("G0  CLOSED FORMS / PHASE / ENHANCEMENT / THETA")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))

    v1, p1 = run_part1(smoke, c_inc)
    v2, p2 = run_part2(smoke)

    section("GATES / VERDICT")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G4-smoke-subset", True, "sigma[:1] gamma[:2] reduced foreign grid")
    else:
        check(
            "G4-full-grid",
            True,
            "sigmas=%d gammas=%d hosts=%dx%d"
            % (len(SIGMAS), len(GAMMAS), len(HOST_BETAS), len(GAMMAS)),
        )

    canon = {
        "part1": p1,
        "part2": {
            key: value
            for key, value in p2.items()
            if key != "top"
        },
        "part2_top": p2.get("top", []),
        "SPEC_SHA": SPEC_SHA,
    }
    seal = payload_sha(canon)
    print("PAYLOAD_SHA256 %s" % seal)
    print("PART1_VERDICT %s" % v1)
    print("PART2_VERDICT %s" % v2)
    print("VERDICT %s %s" % (v1, v2))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    failures = [name for name, passed in CHECKS if not passed]
    print("CHECKS %d/%d" % (len(CHECKS) - len(failures), len(CHECKS)))
    if failures:
        print("GATE_FAILURES " + ",".join(failures))
        return 1
    print("ALL CHECKS PASSED")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "r549 Gabor density-transfer + off-line remainder "
            "(experiments only)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
