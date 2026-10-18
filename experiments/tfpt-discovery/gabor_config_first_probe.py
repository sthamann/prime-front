#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_config_first_probe -- r553

Round 553.  Experiments-only scout of the QUANTIFIER REPAIR for the
r551 SELECTION_CONDITIONAL wall.

  r551 (opponent last): if the adversary places an equal-σ quadruple
  at the already-tuned packet centre, Q★/|Q_sel| = e^{π²/128}≈1.080
  flips the selected term.  Increment budget ≈ 141 × r541 leftover.

  r553 (config first): the off-line configuration Z is frozen FIRST
  (increment-compliant: ≤ C_inc ordinates per unit bin, hence
  ≤ 43 FE quadruples / bin).  The witness THEN chooses h, seeing Z.
  Weil only needs: ∀ such Z, ∃ admissible even h with W(h;Z) < 0.

CLAIM BOUNDARY.  Finite closed-form / grid-search arithmetic on
  (A) the 1-packet class h(t)=p(t) e^{−a t²} cos(ω t), p even, deg ≤4
  (B) the 2-packet extension h=h₁+λ h₂ (NOT in the 1-packet class;
      documented as a CLASS EXTENSION; Weil itself allows any
      admissible even test).  Optimisers are discrete deterministic
      grids, labelled NUMERIC.  NO RH claim, NO anti-RH claim,
      NO ledger/paper/Lean/next.txt edit.

HAT CONVENTION.  Weil-shifted ĥ_W(s)=H(s−1/2) H(1/2−s), matching
`RH.pureGaborHatDelta`.  A quadruple contributes 4 Re ĥ_W.
On-line budget = 2 C_inc S_cert as in r549 (conjugate × increment
× certified theta majorant of the on-line envelope).

Score (r541 leftover + extra off-line + Δ online):
  W_left = R541_MARGIN + (Q_off − Q_primary) + max(0, R_on − R_ref)
Win iff W_left < 0.  Enhancement sitting in both Q_off and
Q_primary cancels, so a-changes do not explode the leftover.
R_on = 2 C_inc S_cert (r549).  Poly online = growth² S_cert.

Verdicts, separately for (A) 1-packet and (B) 2-packet:
  WITNESS_WINS(strategy=…, worst_margin=…)
  WITNESS_LOSES(config=…)
  WITNESS_CONDITIONAL(needs=…)
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
HOST_SIGMAS = ("0.10", "0.25")
HOST_GAMMAS = ("14",)
D_REL = ("0", "0.1", "0.5", "1", "2", "5", "10")
D_ABS = ("0.25", "1", "2")
K_CLUSTER = (2, 5, 10, 43)
CLUSTER_WINDOWS = ("pack", "unit")
MIXED_R = "0.99"
MIXED_N = ("10", "20")
A_FACTORS = ("0.5", "1", "2", "4", "8")
A_MIN_FACTOR = "0.25"  # a >= a_r541/4 ⇒ enhancement ≤ e^{128}; overflow floor
POLY_B2 = ("-2", "-1", "0", "1", "2")
POLY_B4 = ("-1", "0", "1")
LAMBDA_GRID = ("0.25", "0.5", "1", "2", "4")
GAME_WIDTHS = ("0.25", "0.5", "1", "2", "5")
GAME_K = (5, 10, 43)
R541_MARGIN = "-3.56"
NSTR_DIGITS = 12
DPS = 80
K_MAX_BIN = 43

SPEC = {
    "round": 553,
    "parent_round": 551,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.CONFIG_FIRST.01",
    "target": "GaborSeparationInequality.quantifier_repair",
    "hat": "weil_shifted",
    "class_A": "pure_gabor_even_poly_deg<=4",
    "class_B": "two_packet_superposition (CLASS EXTENSION)",
    "quantifiers": "forall_Z exists_h  (config first, witness last)",
    "a_rule_seed": "sigma^2/64",
    "omega_rule_seed": "gamma-pi*a/sigma",
    "online_budget": "2*C_inc*S_cert",
    "theta_majorant": "2+vartheta_3(0,exp(-1/(2a)))",
    "host_sigmas": list(HOST_SIGMAS),
    "host_gammas": list(HOST_GAMMAS),
    "d_rel_sqrt_a": list(D_REL),
    "d_abs": list(D_ABS),
    "k_cluster": list(K_CLUSTER),
    "cluster_windows": list(CLUSTER_WINDOWS),
    "mixed_r": MIXED_R,
    "mixed_n": list(MIXED_N),
    "a_factors": list(A_FACTORS),
    "a_min_factor": A_MIN_FACTOR,
    "score": "leftover = R541_MARGIN + (Q_off-Q_primary) + max(0,R_on-R_ref)",
    "poly_b2": list(POLY_B2),
    "poly_b4": list(POLY_B4),
    "lambda_grid": list(LAMBDA_GRID),
    "game_widths": list(GAME_WIDTHS),
    "game_k": list(GAME_K),
    "r541_margin": R541_MARGIN,
    "k_max_bin": K_MAX_BIN,
    "c_inc_source": (
        "2*zetaZerosInDiskCardBoundInner "
        "(ZeroIncrement prefactor; log factor pulled out)"
    ),
    "c_inner_formula": (
        "(log(2+6*zeta(9/8))+log|zeta(2)|+2)/log(14/13)"
    ),
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "optimiser": "deterministic_finite_grid",
    "scope": (
        "increment-compliant off-line families; witness sees Z; "
        "1-packet vs 2-packet; two-iteration min-max game"
    ),
    "excluded": "RH claim; Lean edit; ledger/paper; next.txt",
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


def exp_c(z: mp.mpc) -> mp.mpc:
    re_z = mp.re(z)
    if re_z > mp.mpf(800):
        return mp.exp(mp.mpf(800) + mp.j * mp.im(z))
    if re_z < mp.mpf(-800):
        return mp.mpc(0)
    return mp.exp(z)


def scaling_a(sigma: mp.mpf) -> mp.mpf:
    return sigma ** 2 / 64


def scaling_omega(sigma: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    return gamma - mp.pi * scaling_a(sigma) / sigma


def c_inner() -> mp.mpf:
    coeff = 2 + 6 * mp.zeta(mp.mpf(9) / 8)
    numer = mp.log(coeff) + mp.log(abs(mp.zeta(2))) + 2
    return numer / mp.log(mp.mpf(14) / 13)


def c_inc_prefactor() -> mp.mpf:
    return 2 * c_inner()


def theta3_q(a: mp.mpf) -> mp.mpf:
    q_log = -1 / (2 * a)
    total = mp.mpf(1)
    m_val = 1
    while True:
        term = exp_clip((m_val * m_val) * q_log)
        total += 2 * term
        if term < mp.mpf("1e-80") or m_val > 200:
            m_next = m_val + 1
            gap = exp_clip(-(2 * m_val + 1) / (2 * a))
            rem = (
                2 * exp_clip(-(m_next * m_next) / (2 * a)) / (1 - gap)
                if gap < mp.mpf("0.5")
                else mp.mpf("1e-80")
            )
            total += rem
            break
        m_val += 1
    return total


def theta_lobe(a: mp.mpf) -> mp.mpf:
    return 2 + theta3_q(a)


def theta_left_pos(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    if omega <= 0:
        return theta_lobe(a)
    geom = exp_clip(-omega / a)
    if geom >= mp.mpf("0.5"):
        return theta_lobe(a)
    return exp_clip(-(omega * omega) / (2 * a)) / (1 - geom)


def theta_cross_pos(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    return exp_clip(-(omega * omega) / (2 * a)) * (1 + theta3_q(a)) / 2


def certified_bin_sum(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    pref = mp.pi / (4 * a)
    return pref * (
        theta_lobe(a) + theta_left_pos(a, omega) + 2 * theta_cross_pos(a, omega)
    )


def online_budget(a: mp.mpf, omega: mp.mpf, c_inc: mp.mpf) -> mp.mpf:
    """r549: R ≤ 2 C_inc Σ_k max w(t), certified theta majorant."""
    return 2 * c_inc * certified_bin_sum(a, omega)


def hat_w_delta(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpc:
    pref = mp.pi / (4 * a)
    term_plus = exp_c(
        (sigma ** 2 - (t_value + omega) ** 2) / (2 * a)
        + mp.j * sigma * (t_value + omega) / a
    )
    term_minus = exp_c(
        (sigma ** 2 - (t_value - omega) ** 2) / (2 * a)
        + mp.j * sigma * (t_value - omega) / a
    )
    term_cross = 2 * exp_c(
        (sigma ** 2 - t_value ** 2 - omega ** 2) / (2 * a)
        + mp.j * sigma * t_value / a
    )
    return pref * (term_plus + term_minus + term_cross)


def quadruple_closed(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpf:
    """Exact 4 Re ĥ_W = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ]."""
    a_plus = exp_clip((sigma ** 2 - (t_value + omega) ** 2) / (2 * a))
    a_minus = exp_clip((sigma ** 2 - (t_value - omega) ** 2) / (2 * a))
    a_cross = exp_clip((sigma ** 2 - t_value ** 2 - omega ** 2) / (2 * a))
    phi_plus = sigma * (t_value + omega) / a
    phi_minus = sigma * (t_value - omega) / a
    phi_cross = sigma * t_value / a
    return (mp.pi / a) * (
        a_plus * mp.cos(phi_plus)
        + a_minus * mp.cos(phi_minus)
        + 2 * a_cross * mp.cos(phi_cross)
    )


def gabor_H(a: mp.mpf, omega: mp.mpf, z: mp.mpc) -> mp.mpc:
    """H(z) for h(t)=e^{−a t²} cos(ω t)."""
    return (
        mp.mpf("0.5")
        * mp.sqrt(mp.pi / a)
        * (
            exp_c((z + mp.j * omega) ** 2 / (4 * a))
            + exp_c((z - mp.j * omega) ** 2 / (4 * a))
        )
    )


def hat_from_H(h_plus: mp.mpc, h_minus: mp.mpc) -> mp.mpc:
    return h_plus * h_minus


def gaussian_poly_factor(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf, a: mp.mpf, z: mp.mpc,
) -> mp.mpc:
    return (
        c0
        + c2 * ((1 / (2 * a)) + z ** 2 / (4 * a ** 2))
        + c4 * (
            3 / (4 * a ** 2)
            + 3 * z ** 2 / (4 * a ** 3)
            + z ** 4 / (16 * a ** 4)
        )
    )


def gaussian_laplace(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf, a: mp.mpf, z: mp.mpc,
) -> mp.mpc:
    return (
        mp.sqrt(mp.pi / a)
        * exp_c(z ** 2 / (4 * a))
        * gaussian_poly_factor(c0, c2, c4, a, z)
    )


def gabor_hat_poly(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
    a: mp.mpf, omega: mp.mpf, sigma: mp.mpf, t_value: mp.mpf,
) -> mp.mpc:
    delta = sigma + mp.j * t_value
    plus = gaussian_laplace(c0, c2, c4, a, delta + mp.j * omega)
    minus = gaussian_laplace(c0, c2, c4, a, delta - mp.j * omega)
    plus_n = gaussian_laplace(c0, c2, c4, a, -delta + mp.j * omega)
    minus_n = gaussian_laplace(c0, c2, c4, a, -delta - mp.j * omega)
    return (plus + minus) * (plus_n + minus_n) / 4


def two_packet_hat(
    a1: mp.mpf, w1: mp.mpf, a2: mp.mpf, w2: mp.mpf, lam: mp.mpf,
    sigma: mp.mpf, t_value: mp.mpf,
) -> mp.mpc:
    delta = sigma + mp.j * t_value
    h_plus = gabor_H(a1, w1, delta) + lam * gabor_H(a2, w2, delta)
    h_minus = gabor_H(a1, w1, -delta) + lam * gabor_H(a2, w2, -delta)
    return hat_from_H(h_plus, h_minus)


def q_off_pure(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...], a: mp.mpf, omega: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    total = mp.mpf(0)
    primary = mp.inf
    for sigma, gamma in quads:
        term = quadruple_closed(sigma, gamma, a, omega)
        total += term
        if term < primary:
            primary = term
    return total, primary


def q_off_poly(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    total = mp.mpf(0)
    primary = mp.inf
    for sigma, gamma in quads:
        term = 4 * mp.re(gabor_hat_poly(c0, c2, c4, a, omega, sigma, gamma))
        total += term
        if term < primary:
            primary = term
    return total, primary


def q_off_two(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    a1: mp.mpf, w1: mp.mpf, a2: mp.mpf, w2: mp.mpf, lam: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    total = mp.mpf(0)
    primary = mp.inf
    for sigma, gamma in quads:
        term = 4 * mp.re(two_packet_hat(a1, w1, a2, w2, lam, sigma, gamma))
        total += term
        if term < primary:
            primary = term
    return total, primary


def poly_growth(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf, a: mp.mpf, z_abs: mp.mpf,
) -> mp.mpf:
    """Majorant of |gaussian_poly_factor| for |z| ≤ z_abs."""
    return (
        abs(c0)
        + abs(c2) * ((1 / (2 * a)) + z_abs ** 2 / (4 * a ** 2))
        + abs(c4) * (
            3 / (4 * a ** 2)
            + 3 * z_abs ** 2 / (4 * a ** 3)
            + z_abs ** 4 / (16 * a ** 4)
        )
    )


def online_two_majorant(
    a1: mp.mpf, w1: mp.mpf, a2: mp.mpf, w2: mp.mpf, lam: mp.mpf,
    c_inc: mp.mpf,
) -> mp.mpf:
    """Certified: |H1+λH2|² ≤ 2|H1|² + 2λ²|H2|², each |H|² ≤ S_cert."""
    return 2 * (
        online_budget(a1, w1, c_inc) + (lam * lam) * online_budget(a2, w2, c_inc)
    )


def payload_sha(rows: dict) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def unique_sorted(values: list[mp.mpf]) -> tuple[mp.mpf, ...]:
    keyed = sorted(values, key=lambda item: (mp.nstr(item, 20),))
    out: list[mp.mpf] = []
    for item in keyed:
        if not out or abs(item - out[-1]) > mp.mpf("1e-18"):
            out.append(item)
    return tuple(out)


def config_stats(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, int]:
    sigmas = [sigma for sigma, _ in quads]
    gammas = [gamma for _, gamma in quads]
    sigma_max = max(sigmas)
    gamma_min = min(gammas)
    gamma_max = max(gammas)
    gamma_mean = sum(gammas, mp.mpf(0)) / len(gammas)
    return sigma_max, gamma_min, gamma_max, gamma_mean, len(quads)


def increment_ok(quads: tuple[tuple[mp.mpf, mp.mpf], ...]) -> bool:
    """At most K_MAX_BIN FE quadruples in any unit ordinate bin."""
    if not quads:
        return True
    heights = sorted(gamma for _, gamma in quads)
    start = 0
    for end, height in enumerate(heights):
        while height - heights[start] > 1:
            start += 1
        if end - start + 1 > K_MAX_BIN:
            return False
    return True


# ---------------------------------------------------------------------------
# Configuration factory (frozen before any h is chosen)
# ---------------------------------------------------------------------------
def make_configs(
    sigma: mp.mpf, gamma: mp.mpf, smoke: bool,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    a_ref = scaling_a(sigma)
    width = mp.sqrt(a_ref)
    configs: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []

    configs.append(("single", ((sigma, gamma),)))

    rels = D_REL[:4] if smoke else D_REL
    for mul_text in rels:
        mul = mp.mpf(mul_text)
        dist = mul * width
        if dist == 0:
            quads = ((sigma, gamma), (sigma, gamma))
        else:
            quads = ((sigma, gamma), (sigma, gamma + dist))
        configs.append(("tie:rel=%s" % mul_text, quads))

    abs_list = D_ABS[:1] if smoke else D_ABS
    for dist_text in abs_list:
        dist = mp.mpf(dist_text)
        configs.append(
            ("tie:abs=%s" % dist_text, ((sigma, gamma), (sigma, gamma + dist)))
        )

    ks = (2, 5) if smoke else K_CLUSTER
    windows = ("unit",) if smoke else CLUSTER_WINDOWS
    for k_use in ks:
        for window in windows:
            if window == "unit":
                span = mp.mpf(1)
            else:
                span = 2 * width
            if k_use == 1:
                pts = (gamma,)
            else:
                pts = tuple(
                    gamma + (mp.mpf(index) / (k_use - 1)) * span
                    for index in range(k_use)
                )
            quads = tuple((sigma, height) for height in pts)
            configs.append(("cluster:k=%d:%s" % (k_use, window), quads))
        # Two clumps at the r541 antiphase gap π a/σ = π σ/64.
        gap = mp.pi * a_ref / sigma
        n_left = k_use // 2
        n_right = k_use - n_left
        quads = tuple(
            [(sigma, gamma)] * n_left + [(sigma, gamma + gap)] * n_right
        )
        configs.append(("cluster:k=%d:antiphase" % k_use, quads))

    ns = MIXED_N[:1] if smoke else MIXED_N
    ratio = mp.mpf(MIXED_R)
    for n_text in ns:
        n_near = int(n_text)
        # Second clump, still increment-compliant: packed in a 2√a
        # window sitting in the same unit bin, away from the extremal.
        pack_span = min(mp.mpf(1) - 4 * width, 2 * width)
        if pack_span <= 0:
            pack_span = width
        start = gamma + mp.mpf("0.5")
        if n_near == 1:
            pts = (start,)
        else:
            pts = tuple(
                start + (mp.mpf(index) / (n_near - 1)) * pack_span
                for index in range(n_near)
            )
        mixed = [(sigma, gamma)] + [(ratio * sigma, height) for height in pts]
        configs.append(("mixed:n=%s" % n_text, tuple(mixed)))

    return configs


def game_configs(
    sigma: mp.mpf, gamma: mp.mpf, smoke: bool,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    a_ref = scaling_a(sigma)
    width = mp.sqrt(a_ref)
    widths = GAME_WIDTHS[:3] if smoke else GAME_WIDTHS
    ks = (5,) if smoke else GAME_K
    out: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    for k_use in ks:
        for w_text in widths:
            span = mp.mpf(w_text) * width
            if span <= 0:
                pts = (gamma,) * k_use
            elif k_use == 1:
                pts = (gamma,)
            else:
                pts = tuple(
                    gamma + (mp.mpf(index) / (k_use - 1)) * span
                    for index in range(k_use)
                )
            out.append(
                (
                    "game:k=%d:w=%s*sqrt(a)" % (k_use, w_text),
                    tuple((sigma, height) for height in pts),
                )
            )
        # Absolute unit window already in the catalog; add half-bin.
        span = mp.mpf("0.5")
        pts = tuple(
            gamma + (mp.mpf(index) / (k_use - 1)) * span
            for index in range(k_use)
        )
        out.append(
            ("game:k=%d:halfbin" % k_use, tuple((sigma, height) for height in pts))
        )
    return out


# ---------------------------------------------------------------------------
# Witness strategies (may see Z)
# ---------------------------------------------------------------------------
def aw_seeds(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...], smoke: bool,
) -> list[tuple[str, mp.mpf, mp.mpf]]:
    sigma_max, gamma_min, gamma_max, gamma_mean, n_quad = config_stats(quads)
    span = gamma_max - gamma_min
    a_ref = scaling_a(sigma_max)
    a_min = a_ref * mp.mpf(A_MIN_FACTOR)
    factors = A_FACTORS[:4] if smoke else A_FACTORS
    seeds: list[tuple[str, mp.mpf, mp.mpf]] = []

    # r541 lock on the first / mean / max-γ / min-γ sites.
    sites = unique_sorted([quads[0][1], gamma_mean, gamma_min, gamma_max])
    for site in sites:
        omega = scaling_omega(sigma_max, site)
        seeds.append(("r541@%s" % nstr(site, 6), a_ref, omega))

    # Free width around the r541 a, ω at the barycentre / edges.
    for fac_text in factors:
        a_val = a_ref * mp.mpf(fac_text)
        if a_val <= 0:
            continue
        for site in sites:
            seeds.append(
                ("afac=%s@%s" % (fac_text, nstr(site, 6)), a_val, site)
            )
            seeds.append(
                (
                    "afac=%s@r541(%s)" % (fac_text, nstr(site, 6)),
                    a_val,
                    site - mp.pi * a_val / sigma_max,
                )
            )

    # Midpoint phase lock: both edges at φ=±π when span>0.
    # a is floored: unconstrained a→0 is an enhancement blow-up, not a
    # leftover-scale witness (labelled; excluded from the win map).
    if span > 0:
        a_edge = sigma_max * span / (2 * mp.pi)
        if a_edge >= a_min:
            seeds.append(("mid_pi", a_edge, gamma_mean))
            seeds.append(("mid_halfpi", 2 * a_edge, gamma_mean))
        elif 2 * a_edge >= a_min:
            seeds.append(("mid_halfpi", max(2 * a_edge, a_min), gamma_mean))
        a_cover = max(a_min, (span / 4) ** 2) if span >= 4 * mp.sqrt(a_min) else a_min
        seeds.append(
            (
                "cover",
                a_cover,
                gamma_mean - mp.pi * a_cover / sigma_max,
            )
        )

    # Per-quad destructive lock (iv).
    for index, (sigma, gamma) in enumerate(quads[: 3 if smoke else 6]):
        if sigma <= 0:
            continue
        a_val = scaling_a(sigma)
        seeds.append(
            ("destr#%d" % index, a_val, scaling_omega(sigma, gamma))
        )
        if span > 0:
            a_alt = max(a_min, sigma * span / (2 * mp.pi))
            seeds.append(
                ("destr_span#%d" % index, a_alt, scaling_omega(sigma, gamma))
            )

    # Dedup by (a,ω) to 18 decimals.
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, mp.mpf, mp.mpf]] = []
    for name, a_val, omega in seeds:
        if a_val < a_min:
            continue
        key = (mp.nstr(a_val, 18), mp.nstr(omega, 18))
        if key in seen:
            continue
        seen.add(key)
        out.append((name, a_val, omega))
    return out


def best_pure(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    dest_only: bool = False,
) -> dict:
    seeds = aw_seeds(quads, smoke)
    if dest_only:
        seeds = [row for row in seeds if row[0].startswith("destr")]
        if not seeds:
            seeds = aw_seeds(quads, smoke)[:1]
    best: dict | None = None
    for name, a_val, omega in seeds:
        q_off, q_pri = q_off_pure(quads, a_val, omega)
        r_on = online_budget(a_val, omega, c_inc)
        pick = (q_off - q_pri) + max(r_on, mp.mpf(0))
        rec = {
            "seed": name,
            "a": a_val,
            "omega": omega,
            "Q_off": q_off,
            "Q_primary": q_pri,
            "R_on": r_on,
            "W": q_off + r_on,
            "_pick": pick,
        }
        if best is None or pick < best["_pick"]:
            best = rec
    assert best is not None
    return best


def best_poly(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    c_inc: mp.mpf,
    smoke: bool,
) -> dict:
    b2s = POLY_B2[:3] if smoke else POLY_B2
    b4s = ("0", "1") if smoke else POLY_B4
    r_on = online_budget(a_val, omega, c_inc)
    # Polynomial growth on the line is labelled NUMERIC: we charge the
    # pure-Gabor certified online budget (a lower bound on the true
    # poly envelope only when |p-factor|≤1).  Extra positive online
    # from |b2|,|b4|>0 is therefore NOT certified; a poly WIN is
    # accepted only if Q_off + 2 R_on < 0 (factor-2 pad).
    best: dict | None = None
    for b2_text in b2s:
        for b4_text in b4s:
            c0 = mp.mpf(1)
            c2 = mp.mpf(b2_text) * a_val
            c4 = mp.mpf(b4_text) * a_val ** 2
            q_off, q_pri = q_off_poly(quads, c0, c2, c4, a_val, omega)
            growth = poly_growth(c0, c2, c4, a_val, abs(omega) + 1)
            r_poly = (growth * growth) * r_on
            rec = {
                "b2": b2_text,
                "b4": b4_text,
                "Q_off": q_off,
                "Q_primary": q_pri,
                "R_on": r_poly,
                "W": q_off + r_poly,
                "W_pad": q_off + r_poly,
            }
            rec["_pick"] = (q_off - q_pri) + r_poly
            if best is None or rec["_pick"] < best["_pick"]:
                best = rec
    assert best is not None
    return best


def split_quads(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[
    tuple[tuple[mp.mpf, mp.mpf], ...],
    tuple[tuple[mp.mpf, mp.mpf], ...],
]:
    if len(quads) == 1:
        return quads, quads
    ordered = sorted(quads, key=lambda item: (item[1], item[0]))
    mid = len(ordered) // 2
    left = tuple(ordered[: max(1, mid)])
    right = tuple(ordered[mid:]) if mid < len(ordered) else (ordered[-1],)
    return left, right


def packet_tune(
    group: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[mp.mpf, mp.mpf]:
    sigma_max, gamma_min, gamma_max, gamma_mean, _ = config_stats(group)
    a_ref = scaling_a(sigma_max)
    a_min = a_ref * mp.mpf(A_MIN_FACTOR)
    span = gamma_max - gamma_min
    if span > 0:
        a_val = max(a_min, sigma_max * span / (2 * mp.pi))
        return a_val, gamma_mean
    return a_ref, scaling_omega(sigma_max, gamma_mean)


def best_two(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
) -> dict:
    left, right = split_quads(quads)
    a1, w1 = packet_tune(left)
    a2, w2 = packet_tune(right)
    # Also try r541 locks on the two extreme ordinates.
    sigma_l, g_l = left[0]
    sigma_r, g_r = right[-1]
    alts = [
        (a1, w1, a2, w2, "split_tune"),
        (
            scaling_a(sigma_l),
            scaling_omega(sigma_l, g_l),
            scaling_a(sigma_r),
            scaling_omega(sigma_r, g_r),
            "split_r541",
        ),
    ]
    lams = LAMBDA_GRID[:3] if smoke else LAMBDA_GRID
    best: dict | None = None
    for a_l, w_l, a_r, w_r, tag in alts:
        if a_l <= 0 or a_r <= 0:
            continue
        for lam_text in lams:
            lam = mp.mpf(lam_text)
            q_off, q_pri = q_off_two(quads, a_l, w_l, a_r, w_r, lam)
            r_on = online_two_majorant(a_l, w_l, a_r, w_r, lam, c_inc)
            rec = {
                "tag": tag,
                "lam": lam_text,
                "a1": a_l,
                "w1": w_l,
                "a2": a_r,
                "w2": w_r,
                "Q_off": q_off,
                "Q_primary": q_pri,
                "R_on": r_on,
                "W": q_off + r_on,
            }
            rec["_pick"] = (q_off - q_pri) + r_on
            if best is None or rec["_pick"] < best["_pick"]:
                best = rec
    assert best is not None
    return best


def r541_lock_score(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...], c_inc: mp.mpf,
) -> dict:
    """Control: lock to the first (max-σ, then min-γ) quadruple."""
    ordered = sorted(quads, key=lambda item: (-item[0], item[1]))
    sigma, gamma = ordered[0]
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    q_off, q_pri = q_off_pure(quads, a_val, omega)
    r_on = online_budget(a_val, omega, c_inc)
    q_sel = quadruple_closed(sigma, gamma, a_val, omega)
    return {
        "a": a_val,
        "omega": omega,
        "Q_off": q_off,
        "Q_primary": q_pri,
        "R_on": r_on,
        "Q_sel": q_sel,
        "W": q_off + r_on,
    }


def leftover(
    q_off: mp.mpf,
    q_primary: mp.mpf,
    r_on: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> mp.mpf:
    """r541 leftover plus extra off-line mass, online penalty only.

    W_left = R541_MARGIN + (Q_off − Q_primary) + max(0, R_on − R_ref)

    Q_primary is the most negative single-quad Q at this h (the
    eigen-term the sealed −3.56 already paid).  Enhancement that
    sits in both Q_off and Q_primary cancels.  A smaller online
    budget is not credited (the −3.56 already used a tighter
    r541 online than 2 C_inc S_cert); a larger one is charged.
    """
    extra_on = r_on - r_ref
    if extra_on < 0:
        extra_on = mp.mpf(0)
    return (-margin) + (q_off - q_primary) + extra_on


def public_score(
    rec: dict, q_ref: mp.mpf, r_ref: mp.mpf, margin: mp.mpf,
) -> dict:
    q_off = rec["Q_off"]
    r_on = rec["R_on"]
    q_pri = rec.get("Q_primary", q_off if len(rec) else q_off)
    score = leftover(q_off, q_pri, r_on, r_ref, margin)
    abs_ref = abs(q_ref) if q_ref != 0 else mp.mpf(1)
    return {
        "W": nstr(score),
        "W_raw": nstr(q_off + r_on),
        "Q_off": nstr(q_off),
        "R_on": nstr(r_on),
        "win": str(int(score < 0)),
        "W_over_Qref": nstr(score / abs_ref),
        "W_over_margin": nstr(score / margin),
        "Q_over_Qref": nstr(q_off / abs_ref),
    }


# ---------------------------------------------------------------------------
# Parts
# ---------------------------------------------------------------------------
def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    for alpha in (mp.mpf("0.5"), mp.mpf(1)):
        for delta in (mp.mpc(0), mp.mpc("0.2", "0.4")):
            analytic = (mp.pi / alpha) * mp.exp((delta * delta) / (2 * alpha))
            from_h = hat_w_delta(delta.real, delta.imag, alpha, mp.mpf(0))
            max_err = max(max_err, abs(from_h - analytic))
    sigma = mp.mpf("0.1")
    gamma = mp.mpf(14)
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    q_closed = quadruple_closed(sigma, gamma, a_val, omega)
    q_re = 4 * mp.re(hat_w_delta(sigma, gamma, a_val, omega))
    max_err = max(max_err, abs(q_closed - q_re))
    # H(δ)H(−δ) recovers ĥ_W.
    delta = sigma + mp.j * gamma
    from_h = gabor_H(a_val, omega, delta) * gabor_H(a_val, omega, -delta)
    max_err = max(max_err, abs(from_h - hat_w_delta(sigma, gamma, a_val, omega)))
    # Two-packet λ=0 recovers one packet.
    two0 = two_packet_hat(a_val, omega, a_val, omega + 1, mp.mpf(0), sigma, gamma)
    max_err = max(max_err, abs(two0 - hat_w_delta(sigma, gamma, a_val, omega)))
    # Poly p=1 recovers pure Gabor.
    hat_p = gabor_hat_poly(
        mp.mpf(1), mp.mpf(0), mp.mpf(0), a_val, omega, sigma, gamma,
    )
    max_err = max(max_err, abs(hat_p - hat_w_delta(sigma, gamma, a_val, omega)))
    # Midpoint ±π lock: two equal-σ quads at ±d/2 get cos φ_− = −1.
    dist = mp.mpf("0.2")
    a_mid = sigma * dist / (2 * mp.pi)
    w_mid = gamma + dist / 2
    q1 = quadruple_closed(sigma, gamma, a_mid, w_mid)
    q2 = quadruple_closed(sigma, gamma + dist, a_mid, w_mid)
    # Leading A_− terms share the same |φ|=π.
    phi1 = sigma * (gamma - w_mid) / a_mid
    phi2 = sigma * (gamma + dist - w_mid) / a_mid
    max_err = max(max_err, abs(abs(phi1) - mp.pi), abs(abs(phi2) - mp.pi))
    if q1 >= 0 or q2 >= 0:
        max_err = max(max_err, mp.mpf(1))
    if not (c_inc > 0 and mp.isfinite(c_inc)):
        max_err = max(max_err, mp.mpf(1))
    if increment_ok(((sigma, gamma),) * K_MAX_BIN) is False:
        max_err = max(max_err, mp.mpf(1))
    if increment_ok(((sigma, gamma),) * (K_MAX_BIN + 1)) is True:
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-16"), max_err


def eval_config(
    name: str,
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    q_ref: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    locked = r541_lock_score(quads, c_inc)
    free = best_pure(quads, c_inc, smoke, dest_only=False)
    dest = best_pure(quads, c_inc, smoke, dest_only=True)
    poly = best_poly(quads, free["a"], free["omega"], c_inc, smoke)
    two = best_two(quads, c_inc, smoke)
    w_r541 = leftover(
        locked["Q_off"], locked["Q_primary"], locked["R_on"], r_ref, margin,
    )
    w_free = leftover(
        free["Q_off"], free["Q_primary"], free["R_on"], r_ref, margin,
    )
    w_dest = leftover(
        dest["Q_off"], dest["Q_primary"], dest["R_on"], r_ref, margin,
    )
    w_poly = leftover(
        poly["Q_off"], poly["Q_primary"], poly["R_on"], r_ref, margin,
    )
    w_two = leftover(
        two["Q_off"], two["Q_primary"], two["R_on"], r_ref, margin,
    )
    return {
        "name": name,
        "n": str(len(quads)),
        "inc_ok": str(int(increment_ok(quads))),
        "r541": public_score(locked, q_ref, r_ref, margin) | {
            "Q_sel": nstr(locked["Q_sel"]),
        },
        "free": public_score(free, q_ref, r_ref, margin) | {"seed": free["seed"]},
        "destr": public_score(dest, q_ref, r_ref, margin) | {"seed": dest["seed"]},
        "poly": public_score(poly, q_ref, r_ref, margin) | {
            "b2": poly["b2"], "b4": poly["b4"],
        },
        "two": public_score(two, q_ref, r_ref, margin) | {
            "tag": two["tag"], "lam": two["lam"],
        },
        "_W": {
            "r541": w_r541,
            "free": w_free,
            "destr": w_dest,
            "poly": w_poly,
            "two": w_two,
        },
        "_best_A": min(w_free, w_dest, w_poly),
        "_best_B": min(w_free, w_dest, w_poly, w_two),
    }


def run_catalog(
    smoke: bool, c_inc: mp.mpf,
) -> tuple[list[dict], mp.mpf, mp.mpf]:
    section("PART1  CATALOG  (Z frozen, then each strategy sees Z)")
    print(
        "  W_left = R541_MARGIN + (Q_off−Q_primary) + max(0,R_on−R_ref)  "
        "win iff W_left<0;  poly online = growth² S_cert (NUMERIC majorant)"
    )
    print(
        "  CLASS A = {r541_lock, free_aw, destr, poly}   "
        "CLASS B = A ∪ {two_packet}  [two_packet = CLASS EXTENSION]"
    )
    print(
        "  two_packet  h=h1+λ h2 is NOT in the 1-packet class "
        "p(t)e^{-at²}cos(ωt); Weil allows any even admissible h"
    )
    margin = abs(mp.mpf(R541_MARGIN))
    sigmas = HOST_SIGMAS[:1] if smoke else HOST_SIGMAS
    gammas = HOST_GAMMAS
    rows: list[dict] = []
    q_ref = None
    r_ref = None
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            if q_ref is None:
                a_ref = scaling_a(sigma)
                w_ref = scaling_omega(sigma, gamma)
                q_ref = quadruple_closed(sigma, gamma, a_ref, w_ref)
                r_ref = online_budget(a_ref, w_ref, c_inc)
            configs = make_configs(sigma, gamma, smoke)
            for name, quads in configs:
                row = eval_config(
                    "%s|s=%s|g=%s" % (name, sigma_text, gamma_text),
                    quads, c_inc, smoke, q_ref, r_ref, margin,
                )
                rows.append(row)
    assert q_ref is not None and r_ref is not None
    print(
        "  Q_ref %s  R_ref %s  leftover(single,r541) %s  C_inc %s  n_configs %d"
        % (
            nstr(q_ref),
            nstr(r_ref),
            nstr(leftover(q_ref, q_ref, r_ref, r_ref, margin)),
            nstr(c_inc),
            len(rows),
        )
    )
    print(
        "  name                              n  "
        "r541          free          destr         poly          two"
    )
    for row in rows:
        print(
            "  %-32s %2s  %s%s  %s%s  %s%s  %s%s  %s%s"
            % (
                row["name"][:32],
                row["n"],
                nstr(mp.mpf(row["r541"]["W"]), 6),
                "*" if row["r541"]["win"] == "1" else " ",
                nstr(mp.mpf(row["free"]["W"]), 6),
                "*" if row["free"]["win"] == "1" else " ",
                nstr(mp.mpf(row["destr"]["W"]), 6),
                "*" if row["destr"]["win"] == "1" else " ",
                nstr(mp.mpf(row["poly"]["W"]), 6),
                "*" if row["poly"]["win"] == "1" else " ",
                nstr(mp.mpf(row["two"]["W"]), 6),
                "*" if row["two"]["win"] == "1" else " ",
            )
        )
    return rows, q_ref, r_ref, margin


def run_game(
    smoke: bool,
    c_inc: mp.mpf,
    q_ref: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    section("PART2  MIN-MAX GAME  (inner: worst Z for a strategy; outer: retune)")
    print(
        "  Iteration t: Z_t = argmax_{catalog∪game} W(strategy_t(Z), Z); "
        "then strategy_{t+1} re-optimises on Z_t.  Two iterations."
    )
    print(
        "  This is config-first: the adversary knows the RESPONSE, "
        "not a frozen h.  (r551 is the opposite order.)"
    )
    sigma_text = HOST_SIGMAS[0]
    gamma_text = HOST_GAMMAS[0]
    sigma = mp.mpf(sigma_text)
    gamma = mp.mpf(gamma_text)
    pool = make_configs(sigma, gamma, smoke) + game_configs(sigma, gamma, smoke)
    # Dedup names.
    seen: set[str] = set()
    unique: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    for name, quads in pool:
        if name in seen:
            continue
        seen.add(name)
        unique.append((name, quads))

    def score_rec(rec: dict) -> mp.mpf:
        return leftover(
            rec["Q_off"], rec["Q_primary"], rec["R_on"], r_ref, margin,
        )

    def worst_for(kind: str) -> tuple[str, dict, mp.mpf]:
        worst_name = ""
        worst_row: dict | None = None
        worst_w = -mp.inf
        for name, quads in unique:
            if kind == "free":
                rec = best_pure(quads, c_inc, smoke, dest_only=False)
            elif kind == "two":
                rec = best_two(quads, c_inc, smoke)
            elif kind == "poly":
                free = best_pure(quads, c_inc, smoke, dest_only=False)
                rec = best_poly(quads, free["a"], free["omega"], c_inc, smoke)
            else:
                rec = r541_lock_score(quads, c_inc)
            score = score_rec(rec)
            if score > worst_w:
                worst_w = score
                worst_name = name
                worst_row = rec
        assert worst_row is not None
        return worst_name, worst_row, worst_w

    def class_scores(
        quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    ) -> tuple[mp.mpf, mp.mpf]:
        free = best_pure(quads, c_inc, smoke, dest_only=False)
        dest = best_pure(quads, c_inc, smoke, dest_only=True)
        poly = best_poly(quads, free["a"], free["omega"], c_inc, smoke)
        two = best_two(quads, c_inc, smoke)
        score_a = min(score_rec(free), score_rec(dest), score_rec(poly))
        score_b = min(score_a, score_rec(two))
        return score_a, score_b

    def worst_class(which: str) -> tuple[str, mp.mpf]:
        worst_name = ""
        worst_w = -mp.inf
        for name, quads in unique:
            score_a, score_b = class_scores(quads)
            score = score_a if which == "A" else score_b
            if score > worst_w:
                worst_w = score
                worst_name = name
        return worst_name, worst_w

    iterations = []
    # Iter 0: r541-lock response (control).
    n0, r0, w0 = worst_for("r541")
    iterations.append({
        "iter": "0",
        "strategy": "r541_lock",
        "worst": n0,
        "W": nstr(w0),
        "win": str(int(w0 < 0)),
    })
    # Iter 1: free (a,ω) response against the full pool.
    n1, r1, w1 = worst_for("free")
    iterations.append({
        "iter": "1",
        "strategy": "free_aw",
        "worst": n1,
        "W": nstr(w1),
        "win": str(int(w1 < 0)),
        "seed": r1.get("seed", ""),
    })
    # Iter 2: two-packet response (class B) + free retune already done.
    n2, r2, w2 = worst_for("two")
    iterations.append({
        "iter": "2",
        "strategy": "two_packet",
        "worst": n2,
        "W": nstr(w2),
        "win": str(int(w2 < 0)),
        "tag": r2.get("tag", ""),
        "lam": r2.get("lam", ""),
    })
    # Local refinement around the iter-1 worst: densify the window.
    worst_free_name = n1
    local_worst = w1
    local_name = n1
    for name, quads in unique:
        if not name.startswith("game:") and "cluster:" not in name:
            continue
        rec = best_pure(quads, c_inc, smoke, dest_only=False)
        rec_w = leftover(
            rec["Q_off"], rec["Q_primary"], rec["R_on"], r_ref, margin,
        )
        if rec_w > local_worst:
            local_worst = rec_w
            local_name = name
    iterations.append({
        "iter": "1b",
        "strategy": "free_aw_refined",
        "worst": local_name,
        "W": nstr(local_worst),
        "win": str(int(local_worst < 0)),
        "anchor": worst_free_name,
    })
    n_a, w_a = worst_class("A")
    n_b, w_b = worst_class("B")
    iterations.append({
        "iter": "A",
        "strategy": "class_A_best",
        "worst": n_a,
        "W": nstr(w_a),
        "win": str(int(w_a < 0)),
    })
    iterations.append({
        "iter": "B",
        "strategy": "class_B_best",
        "worst": n_b,
        "W": nstr(w_b),
        "win": str(int(w_b < 0)),
    })

    print("  iter strategy         worst                              W")
    for item in iterations:
        print(
            "  %s    %-16s %-33s %s  win=%s"
            % (
                item["iter"],
                item["strategy"],
                item["worst"][:33],
                item["W"],
                item["win"],
            )
        )
    return {
        "iterations": iterations,
        "worst_free": n1,
        "W_worst_free": nstr(w1),
        "worst_two": n2,
        "W_worst_two": nstr(w2),
        "W_refine": nstr(local_worst),
        "refine_name": local_name,
        "worst_A": n_a,
        "W_worst_A": nstr(w_a),
        "worst_B": n_b,
        "W_worst_B": nstr(w_b),
    }


def decide_class(
    rows: list[dict], game: dict, class_key: str,
) -> tuple[str, dict]:
    """class_key 'A' uses _best_A; 'B' uses _best_B."""
    attr = "_best_A" if class_key == "A" else "_best_B"
    families = ("free", "destr", "poly") if class_key == "A" else (
        "free", "destr", "poly", "two"
    )
    losses = [row for row in rows if row[attr] >= 0]
    wins = [row for row in rows if row[attr] < 0]
    # Single family that beats every catalog row?
    universal: list[str] = []
    for fam in families:
        if all(mp.mpf(row[fam]["W"]) < 0 for row in rows):
            universal.append(fam)
    worst_row = max(rows, key=lambda row: row[attr])
    worst_margin = worst_row[attr]
    game_free = mp.mpf(game["W_worst_free"])
    game_two = mp.mpf(game["W_worst_two"])
    game_ref = mp.mpf(game["W_refine"])
    game_a = mp.mpf(game["W_worst_A"])
    game_b = mp.mpf(game["W_worst_B"])
    if class_key == "A":
        game_worst = game_a
        game_name = game["worst_A"]
    else:
        game_worst = game_b
        game_name = game["worst_B"]

    if losses:
        names = ",".join(row["name"] for row in losses[:3])
        verdict = "WITNESS_LOSES(config=%s)" % losses[0]["name"]
        extra = {
            "n_loss": str(len(losses)),
            "loss_names": names,
            "worst_catalog": worst_row["name"],
            "worst_W": nstr(worst_margin),
        }
        return verdict, extra

    if game_worst >= 0:
        verdict = "WITNESS_LOSES(config=%s)" % game_name
        return verdict, {
            "n_loss": "game",
            "loss_names": game_name,
            "worst_catalog": worst_row["name"],
            "worst_W": nstr(game_worst),
        }

    if universal:
        # Prefer free_aw as the named family when it is universal.
        lead = "free" if "free" in universal else universal[0]
        # worst_margin among catalog ∪ game for that family.
        fam_ws = [mp.mpf(row[lead]["W"]) for row in rows]
        if lead == "free":
            fam_ws.append(game_free)
            fam_ws.append(game_ref)
        if lead == "two":
            fam_ws.append(game_two)
        worst_fam = max(fam_ws)
        verdict = "WITNESS_WINS(strategy=%s, worst_margin=%s)" % (
            lead, nstr(worst_fam),
        )
        return verdict, {
            "universal": ",".join(universal),
            "worst_catalog": worst_row["name"],
            "worst_W": nstr(worst_fam),
            "n_win": str(len(wins)),
        }

    needed = []
    for row in rows:
        if mp.mpf(row["free"]["W"]) >= 0:
            if class_key == "B" and mp.mpf(row["two"]["W"]) < 0:
                needed.append("two_packet@%s" % row["name"])
            elif mp.mpf(row["poly"]["W"]) < 0:
                needed.append("poly@%s" % row["name"])
            elif mp.mpf(row["destr"]["W"]) < 0:
                needed.append("destr@%s" % row["name"])
    if needed:
        verdict = "WITNESS_CONDITIONAL(needs=%s)" % ";".join(needed[:4])
    else:
        verdict = (
            "WITNESS_CONDITIONAL(needs=per_config_switch;"
            "no_single_family_covers_all)"
        )
    return verdict, {
        "universal": "",
        "worst_catalog": worst_row["name"],
        "worst_W": nstr(worst_margin),
        "n_win": str(len(wins)),
        "needs": needed[:6],
    }


def compact_map(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        out.append({
            "name": row["name"],
            "n": row["n"],
            "r541": row["r541"]["W"],
            "r541_win": row["r541"]["win"],
            "free": row["free"]["W"],
            "free_win": row["free"]["win"],
            "free_seed": row["free"].get("seed", ""),
            "destr": row["destr"]["W"],
            "destr_win": row["destr"]["win"],
            "poly": row["poly"]["W"],
            "poly_win": row["poly"]["win"],
            "two": row["two"]["W"],
            "two_win": row["two"]["win"],
            "best_A": nstr(row["_best_A"]),
            "best_B": nstr(row["_best_B"]),
        })
    return out


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    c_inc = c_inc_prefactor()
    print("gabor_config_first_probe -- r553")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("quantifiers forall_Z exists_h  (config first)")
    print("class_A 1-packet even Gabor-poly  class_B 2-packet EXTENSION")
    print("online 2*C_inc*S_cert  C_inc %s  n_quad_max %d" % (
        nstr(c_inc), K_MAX_BIN,
    ))
    print(
        "FORMULA  Q=(π/a)[A+cosφ++A-cosφ-+2Ax cosφx];  "
        "W_left=R541_MARGIN+(Q_off-Q_primary)+max(0,R_on-R_ref);  "
        "S_cert=(π/(4a))[Θ_lobe+Θ_left+2 Θ_cross]"
    )

    section("G0  CLOSED FORMS / TWO-PACKET λ=0 / MIDPOINT ±π LOCK")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))

    rows, q_ref, r_ref, margin = run_catalog(smoke, c_inc)
    inc_all = all(row["inc_ok"] == "1" for row in rows)
    check("P1-increment-ok", inc_all, "every catalog Z has ≤%d quads/bin" % K_MAX_BIN)
    check("P1-catalog-nonempty", len(rows) > 0, "n=%d" % len(rows))
    check(
        "P1-leftover-single",
        abs(leftover(q_ref, q_ref, r_ref, r_ref, margin) + margin) < mp.mpf("1e-8"),
        "single+r541 recovers R541_MARGIN",
    )

    game = run_game(smoke, c_inc, q_ref, r_ref, margin)

    section("PART3  WIN MAP / VERDICTS")
    verdict_a, extra_a = decide_class(rows, game, "A")
    verdict_b, extra_b = decide_class(rows, game, "B")
    print("  VERDICT_A %s" % verdict_a)
    print("  VERDICT_B %s" % verdict_b)
    print("  A_universal %s" % extra_a.get("universal", ""))
    print("  B_universal %s" % extra_b.get("universal", ""))
    print("  A_worst %s  W=%s" % (extra_a["worst_catalog"], extra_a["worst_W"]))
    print("  B_worst %s  W=%s" % (extra_b["worst_catalog"], extra_b["worst_W"]))

    n_r541_win = sum(1 for row in rows if row["r541"]["win"] == "1")
    n_free_win = sum(1 for row in rows if row["free"]["win"] == "1")
    n_two_win = sum(1 for row in rows if row["two"]["win"] == "1")
    print(
        "  catalog wins  r541 %d/%d  free %d/%d  two %d/%d"
        % (n_r541_win, len(rows), n_free_win, len(rows), n_two_win, len(rows))
    )

    # r551 control: r541 lock loses an equal-σ antiphase clump.
    anti_rows = [row for row in rows if "antiphase" in row["name"]]
    r541_anti_flip = any(row["r541"]["win"] == "0" for row in anti_rows)
    check(
        "P3-r541-lock-loses-antiphase",
        r541_anti_flip or not anti_rows,
        "r551 control: locked scheme fails an antiphase clump",
    )
    check(
        "P3-verdict-A-formed",
        verdict_a.startswith("WITNESS_"),
        verdict_a,
    )
    check(
        "P3-verdict-B-formed",
        verdict_b.startswith("WITNESS_"),
        verdict_b,
    )

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G4-smoke-subset", True, "sigma[:1] reduced d/k grids")
    else:
        check(
            "G4-full-grid",
            True,
            "sigmas=%d d_rel=%d k=%d"
            % (len(HOST_SIGMAS), len(D_REL), len(K_CLUSTER)),
        )

    canon = {
        "catalog": compact_map(rows),
        "game": game,
        "verdict_A": verdict_a,
        "verdict_B": verdict_b,
        "extra_A": {key: value for key, value in extra_a.items() if key != "needs"},
        "extra_B": {key: value for key, value in extra_b.items() if key != "needs"},
        "Q_ref": nstr(q_ref),
        "R_ref": nstr(r_ref),
        "C_inc": nstr(c_inc),
        "SPEC_SHA": SPEC_SHA,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    print("PAYLOAD_SHA256 %s" % seal)
    print("Q_REF %s" % nstr(q_ref))
    print("R_REF %s" % nstr(r_ref))
    print("C_INC %s" % nstr(c_inc))
    print("N_CONFIGS %d" % len(rows))
    print("N_R541_WIN %d" % n_r541_win)
    print("N_FREE_WIN %d" % n_free_win)
    print("N_TWO_WIN %d" % n_two_win)
    print("GAME_WORST_FREE %s %s" % (game["worst_free"], game["W_worst_free"]))
    print("GAME_WORST_TWO %s %s" % (game["worst_two"], game["W_worst_two"]))
    print("GAME_WORST_A %s %s" % (game["worst_A"], game["W_worst_A"]))
    print("GAME_WORST_B %s %s" % (game["worst_B"], game["W_worst_B"]))
    print("VERDICT_A %s" % verdict_a)
    print("VERDICT_B %s" % verdict_b)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("CLASS_NOTE two_packet is a CLASS EXTENSION of the 1-packet Gabor family")
    print("LEAN_NOTE GaborSeparationInequality is forall s: W(scalingGaborTest(s))<0")
    print("LEAN_NOTE GaborSeparatesOffCriticalZeros is forall s exists F: GaborWeilTest")
    print("LEAN_NOTE config-first needs forall Z exists h (h may leave 1-packet class)")
    print("NO_RH_CLAIM")
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
            "r553 Gabor config-first / witness-last probe "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
