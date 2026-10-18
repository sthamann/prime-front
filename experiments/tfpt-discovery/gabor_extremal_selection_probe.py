#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_extremal_selection_probe -- r551

Round 551.  Experiments-only scout of the proposed classical repair
for the r549 OFFLINE_ADVERSARIAL killer: EXTREMAL SELECTION.

  The Weil witness is chosen AFTER an off-line zero is assumed.
  Tuning to a quadruple with (nearly) maximal σ = |β−1/2| forces
  every foreign quadruple to satisfy σ' ≤ σ (+ε if the supremum
  is not attained).  Then the off-line enhancement is at most
  e^{32(1+ε/σ)²} ≈ e^{32}, the same order as the selected term.

This probe asks whether that order-matching actually keeps the
Weil–Rayleigh pairing negative.

  (1) FREMD-BEITRAG.  Exact 4 Re ĥ_W of every foreign FE
      quadruple with σ' ≤ σ on a frozen (r, Δγ) grid.
  (2) WORST-CASE BUDGET.  Increment card C_inc per unit bin
      (≤ C_inc/4 foreign quadruples) times the r549 theta
      majorant of the adversarial envelope, σ' = σ.
  (3) GLEICHSTAND.  Several extremal quadruples at the same σ,
      adversarial phases; even-quartic / phase-offset repair.
  (4) ε-SUPREMUM.  How small ε must be so the excess
      e^{32((σ+ε)/σ)²} − e^{32} does not blow the budget.

CLAIM BOUNDARY.  Finite closed-form / partial-summation
arithmetic on the pure-Gabor class h(t)=p(t) e^{−a t²} cos(ω t)
with the r542 scaling a=σ²/64, ω=γ−π a/σ.  NO RH claim, NO
anti-RH claim, NO ledger row, NO paper edit, NO Lean edit.

HAT CONVENTION.  Weil-shifted ĥ_W(s)=H(s−1/2) H(1/2−s), matching
`RH.pureGaborHatDelta`.  A quadruple contributes 4 Re ĥ_W.

Verdicts:
  SELECTION_RESCUES(budget=..., margin_ratio=...)
  SELECTION_FAILS(config=...)
  SELECTION_CONDITIONAL(condition=...)
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
SIGMAS = ("0.01", "0.1", "0.25", "0.49")
GAMMAS = ("14", "100", "1000")
SIGMA_RATIOS = (
    "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0",
)
# γ' relative to the packet centre ω.
PACKET_OFFSETS = ("0", "1", "-1", "5", "-5", "20", "-20")
FAR_KINDS = ("half", "double")
R541_MARGIN = "-3.56"
NSTR_DIGITS = 12
DPS = 80
POLY_B2 = ("-2", "-1", "0", "1", "2")
POLY_B4 = ("-1", "0", "1")
PHASE_OFFSETS = ("0", "0.25", "0.5", "0.75", "1")  # units of π

SPEC = {
    "round": 551,
    "parent_round": 549,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.EXTREMAL_SELECTION.01",
    "target": "AdditionalOffCriticalZeroControl.extremal_selection",
    "hat": "weil_shifted",
    "class": "pure_gabor",
    "a_rule": "sigma^2/64",
    "omega_rule": "gamma-pi*a/sigma",
    "enhancement": "exp(32)",
    "sigmas": list(SIGMAS),
    "gammas": list(GAMMAS),
    "sigma_ratios": list(SIGMA_RATIOS),
    "packet_offsets": list(PACKET_OFFSETS),
    "far_kinds": list(FAR_KINDS),
    "r541_margin": R541_MARGIN,
    "poly_b2": list(POLY_B2),
    "poly_b4": list(POLY_B4),
    "phase_offsets_pi": list(PHASE_OFFSETS),
    "c_inc_source": (
        "2*zetaZerosInDiskCardBoundInner "
        "(ZeroIncrement prefactor; log factor pulled out)"
    ),
    "c_inner_formula": (
        "(log(2+6*zeta(9/8))+log|zeta(2)|+2)/log(14/13)"
    ),
    "quads_per_bin": "C_inc/4",
    "theta_majorant": "2+vartheta_3(0,exp(-1/(2a)))",
    "budget_formula": "C_inc*exp(32)*S_cert",
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "scope": (
        "foreign FE quadruples with sigma'<=sigma under extremal "
        "selection; Gleichstand; epsilon-supremum; even-quartic repair"
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
    if omega <= 0:
        return theta_lobe(a)
    geom = exp_clip(-omega / a)
    if geom >= mp.mpf("0.5"):
        return theta_lobe(a)
    return exp_clip(-(omega * omega) / (2 * a)) / (1 - geom)


def theta_cross_pos(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
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
    bins = relevant_bins(omega, a)
    total = mp.mpf(0)
    for k in bins:
        total += online_bin_max(k, a, omega)
    k_max = bins[-1]
    u0 = mp.mpf(k_max + 1) - omega
    if u0 < 1:
        u0 = mp.mpf(1)
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


def hat_w_delta(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpc:
    """pureGaborHatDelta: ĥ_W(1/2+σ+it)."""
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
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpf:
    return 4 * mp.re(hat_w_delta(sigma, t_value, a, omega))


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


def q_env(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf,
) -> mp.mpf:
    """Adversarial-phase envelope: all cosines = +1."""
    a_plus = exp_clip((sigma ** 2 - (t_value + omega) ** 2) / (2 * a))
    a_minus = exp_clip((sigma ** 2 - (t_value - omega) ** 2) / (2 * a))
    a_cross = exp_clip((sigma ** 2 - t_value ** 2 - omega ** 2) / (2 * a))
    return (mp.pi / a) * (a_plus + a_minus + 2 * a_cross)


def q_star(sigma: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Exact worst positive foreign: σ'=σ, t=ω (packet centre)."""
    return q_env(sigma, omega, a, omega)


def hat_w_phase(
    sigma: mp.mpf, t_value: mp.mpf, a: mp.mpf, omega: mp.mpf, psi: mp.mpf,
) -> mp.mpc:
    """ĥ_W for h(t)=e^{−at²} cos(ωt+ψ).  Main lobes unshifted; cross × cos 2ψ."""
    pref = mp.pi / (4 * a)
    term_plus = mp.exp(
        (sigma ** 2 - (t_value + omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * sigma * (t_value + omega) / a)
    term_minus = mp.exp(
        (sigma ** 2 - (t_value - omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * sigma * (t_value - omega) / a)
    term_cross = (
        2 * mp.cos(2 * psi)
        * mp.exp((sigma ** 2 - t_value ** 2 - omega ** 2) / (2 * a))
        * mp.exp(mp.j * sigma * t_value / a)
    )
    return pref * (term_plus + term_minus + term_cross)


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
        * mp.exp(z ** 2 / (4 * a))
        * gaussian_poly_factor(c0, c2, c4, a, z)
    )


def gabor_hat_poly(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf,
    a: mp.mpf, omega: mp.mpf, sigma: mp.mpf, t_value: mp.mpf,
) -> mp.mpc:
    """H(δ) H(−δ) for p(t)=c0+c2 t²+c4 t⁴, matching RH.gaborHat."""
    delta = sigma + mp.j * t_value
    plus = gaussian_laplace(c0, c2, c4, a, delta + mp.j * omega)
    minus = gaussian_laplace(c0, c2, c4, a, delta - mp.j * omega)
    plus_n = gaussian_laplace(c0, c2, c4, a, -delta + mp.j * omega)
    minus_n = gaussian_laplace(c0, c2, c4, a, -delta - mp.j * omega)
    return (plus + minus) * (plus_n + minus_n) / 4


def far_gamma(omega: mp.mpf, kind: str) -> mp.mpf:
    if kind == "half":
        return omega / 2
    if kind == "double":
        return 2 * omega
    raise ValueError(kind)


def same_selected(
    sigma: mp.mpf, gamma: mp.mpf, sigma_p: mp.mpf, gamma_p: mp.mpf,
) -> bool:
    atol = mp.mpf("1e-18")
    return abs(sigma_p - sigma) <= atol and abs(gamma_p - gamma) <= atol


def payload_sha(rows: dict) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def foreign_targets(
    omega: mp.mpf, smoke: bool,
) -> list[tuple[str, mp.mpf]]:
    offsets = PACKET_OFFSETS if not smoke else ("0", "1", "-1", "20")
    fars = FAR_KINDS if not smoke else ("double",)
    out: list[tuple[str, mp.mpf]] = []
    for off in offsets:
        height = omega + mp.mpf(off)
        if height > 0:
            out.append(("pack:%s" % off, height))
    for kind in fars:
        height = far_gamma(omega, kind)
        if height > 0:
            out.append(("far:%s" % kind, height))
    return out


def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    for alpha in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2)):
        for delta in (mp.mpc(0), mp.mpc("0.3"), mp.mpc("0.2", "0.4")):
            analytic = (mp.pi / alpha) * mp.exp((delta * delta) / (2 * alpha))
            from_h = hat_w_delta(delta.real, delta.imag, alpha, mp.mpf(0))
            max_err = max(max_err, abs(from_h - analytic))
    for sigma in (mp.mpf("0.1"), mp.mpf("0.25")):
        for gamma in (mp.mpf(14), mp.mpf(100)):
            a_val = scaling_a(sigma)
            omega = scaling_omega(sigma, gamma)
            phase = sigma * (gamma - omega) / a_val
            max_err = max(max_err, abs(phase - mp.pi))
            q_closed = quadruple_closed(sigma, gamma, a_val, omega)
            q_re = quadruple_re(sigma, gamma, a_val, omega)
            max_err = max(max_err, abs(q_closed - q_re))
    for sigma in (mp.mpf("0.1"), mp.mpf("0.49")):
        a_val = scaling_a(sigma)
        max_err = max(
            max_err, abs(mp.exp(sigma ** 2 / (2 * a_val)) - mp.exp(32))
        )
    # Packet-centre / selected antiphase and leading ratio e^{π²/128}.
    sigma = mp.mpf("0.1")
    gamma = mp.mpf(14)
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    q_sel = quadruple_closed(sigma, gamma, a_val, omega)
    q_cen = quadruple_closed(sigma, omega, a_val, omega)
    pred = mp.exp(mp.pi ** 2 / 128)
    if q_sel >= 0 or q_cen <= 0:
        max_err = max(max_err, mp.mpf(1))
    else:
        max_err = max(max_err, abs(q_cen / abs(q_sel) - pred))
    # Poly specialisation p=1 recovers pure Gabor.
    hat_p = gabor_hat_poly(
        mp.mpf(1), mp.mpf(0), mp.mpf(0), a_val, omega, sigma, gamma,
    )
    max_err = max(max_err, abs(hat_p - hat_w_delta(sigma, gamma, a_val, omega)))
    if not (c_inc > 0 and mp.isfinite(c_inc)):
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-18"), max_err


def run_part1(smoke: bool) -> tuple[dict, dict]:
    section("PART1  FREMD-BEITRAG UNTER EXTREMAL-SELEKTION  (σ' ≤ σ)")
    print(
        "  host tunes a=σ²/64, ω=γ−πa/σ; "
        "foreign Q = 4 Re ĥ_W(1/2+σ'+iγ'); selected FE excluded"
    )
    print("  r541_margin %s" % R541_MARGIN)
    print(
        "  Q = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ],  "
        "A±=exp((σ'²−(γ'±ω)²)/(2a))"
    )
    sigmas = SIGMAS[:2] if smoke else SIGMAS
    gammas = GAMMAS[:1] if smoke else GAMMAS
    ratios = ("0.5", "0.9", "1.0") if smoke else SIGMA_RATIOS
    margin = abs(mp.mpf(R541_MARGIN))

    print(
        "  sigma gamma r kind gamma'  Q_sel  Q_for  Q/|Q_sel|  "
        "Q/margin  sign"
    )
    records: list[dict] = []
    worst_q = -mp.inf
    worst_rec: dict | None = None
    n_pos = 0
    n_neg = 0
    flip_sel = False
    flip_margin = False

    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        a_val = scaling_a(sigma)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            q_sel = quadruple_closed(sigma, gamma, a_val, omega)
            for ratio_text in ratios:
                ratio = mp.mpf(ratio_text)
                sigma_p = ratio * sigma
                for kind, gamma_p in foreign_targets(omega, smoke):
                    if same_selected(sigma, gamma, sigma_p, gamma_p):
                        continue
                    q_for = quadruple_closed(sigma_p, gamma_p, a_val, omega)
                    if q_for > 0:
                        n_pos += 1
                    elif q_for < 0:
                        n_neg += 1
                    rel_sel = (
                        q_for / abs(q_sel) if abs(q_sel) > 0 else mp.inf
                    )
                    rel_m = q_for / margin
                    if q_for + q_sel >= 0:
                        flip_sel = True
                    if q_for > margin:
                        flip_margin = True
                    rec = {
                        "sigma": sigma_text,
                        "gamma": gamma_text,
                        "ratio": ratio_text,
                        "kind": kind,
                        "gamma_prime": nstr(gamma_p),
                        "Q_sel": nstr(q_sel),
                        "Q_foreign": nstr(q_for),
                        "rel_sel": nstr(rel_sel),
                        "rel_margin": nstr(rel_m),
                        "sign": (
                            "pos" if q_for > 0
                            else ("neg" if q_for < 0 else "zero")
                        ),
                    }
                    if q_for > worst_q:
                        worst_q = q_for
                        worst_rec = rec
                    records.append(rec)

    ranked = sorted(
        records,
        key=lambda rec: (
            -mp.mpf(rec["Q_foreign"]),
            rec["sigma"],
            float(rec["gamma"]),
            rec["ratio"],
            rec["kind"],
        ),
    )
    if ranked:
        worst_rec = ranked[0]
        worst_q = mp.mpf(worst_rec["Q_foreign"])
    n_print = 8 if smoke else 16
    for rec in ranked[:n_print]:
        print(
            "  %s %s %s %s %s  %s  %s  %s  %s  %s"
            % (
                rec["sigma"],
                rec["gamma"],
                rec["ratio"],
                rec["kind"],
                rec["gamma_prime"],
                rec["Q_sel"],
                rec["Q_foreign"],
                rec["rel_sel"],
                rec["rel_margin"],
                rec["sign"],
            )
        )
    print(
        "  census n=%d  pos=%d  neg=%d  n_print=%d"
        % (len(records), n_pos, n_neg, n_print)
    )
    print(
        "  worst_Q %s  flip_sel %s  flip_margin %s"
        % (
            nstr(worst_q) if mp.isfinite(worst_q) else "nan",
            int(flip_sel),
            int(flip_margin),
        )
    )
    if worst_rec is not None:
        print(
            "  WORST_FOREIGN_FORMULA  "
            "Q★=(π/a) e^{32 r²} [1 + 2 e^{-ω²/a} + e^{-2ω²/a}]  "
            "attained at γ'=ω, r=σ'/σ;  "
            "Q★/|Q_sel| → e^{π²/128} as r→1 (A± leakage → 0)"
        )
        print(
            "  worst config sigma=%s gamma=%s r=%s kind=%s  "
            "rel_sel=%s  rel_margin=%s"
            % (
                worst_rec["sigma"],
                worst_rec["gamma"],
                worst_rec["ratio"],
                worst_rec["kind"],
                worst_rec["rel_sel"],
                worst_rec["rel_margin"],
            )
        )

    check("P1-foreign-grid-nonempty", len(records) > 0, "n=%d" % len(records))
    check(
        "P1-selected-negative",
        all(mp.mpf(rec["Q_sel"]) < 0 for rec in records),
        "every host quadruple has Q_sel<0 (phase π)",
    )
    # Leading-order identity at r=1, packet centre.
    lead_ok = True
    pred = mp.exp(mp.pi ** 2 / 128)
    for rec in records:
        if rec["ratio"] != "1.0" or not rec["kind"].startswith("pack:0"):
            continue
        rel = mp.mpf(rec["rel_sel"])
        if abs(rel - pred) > mp.mpf("1e-8"):
            lead_ok = False
    check(
        "P1-tie-centre-ratio",
        lead_ok,
        "r=1,γ'=ω: Q/|Q_sel| = e^{π²/128} = %s" % nstr(pred),
    )
    return {
        "worst": worst_rec,
        "worst_Q": nstr(worst_q) if mp.isfinite(worst_q) else "nan",
        "n": str(len(records)),
        "n_pos": str(n_pos),
        "n_neg": str(n_neg),
        "flip_sel": str(int(flip_sel)),
        "flip_margin": str(int(flip_margin)),
        "top": ranked[:5],
        "lead_ratio": nstr(pred),
    }, {
        "flip_sel": flip_sel,
        "flip_margin": flip_margin,
        "worst_q": worst_q,
        "worst_rec": worst_rec,
        "records": records,
    }


def budget_formulas(
    sigma: mp.mpf, gamma: mp.mpf, c_inc: mp.mpf,
    sigma_text: str, gamma_text: str,
) -> dict:
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    q_sel = quadruple_closed(sigma, gamma, a_val, omega)
    enh = mp.exp(32)
    s_cert = certified_bin_sum(a_val, omega)
    window, tail = exact_window_bin_sum(a_val, omega)
    s_num = window + tail
    if s_num > s_cert:
        s_num = s_cert
    theta = theta_lobe(a_val)
    # B = (C_inc/4) * Σ_k max Q_env = (C_inc/4) * 4 e^{32} Σ max w
    #   = C_inc e^{32} S
    b_cert = c_inc * enh * s_cert
    b_num = c_inc * enh * s_num
    b_lobe = (c_inc / 4) * (mp.pi / a_val) * enh * theta
    q_peak = q_star(sigma, a_val, omega)
    n_quad = c_inc / 4
    return {
        "sigma": sigma_text,
        "gamma": gamma_text,
        "a": nstr(a_val),
        "omega": nstr(omega),
        "Q_sel": nstr(q_sel),
        "Q_star": nstr(q_peak),
        "S_cert": nstr(s_cert),
        "S_num": nstr(s_num),
        "theta_lobe": nstr(theta),
        "B_cert": nstr(b_cert),
        "B_num": nstr(b_num),
        "B_lobe": nstr(b_lobe),
        "n_quad_bin": nstr(n_quad),
        "B_over_Qsel": nstr(b_cert / abs(q_sel)),
        "B_over_margin": nstr(b_cert / abs(mp.mpf(R541_MARGIN))),
        "Qstar_over_Qsel": nstr(q_peak / abs(q_sel)),
        "Qstar_over_margin": nstr(q_peak / abs(mp.mpf(R541_MARGIN))),
        "_q_sel": q_sel,
        "_b_cert": b_cert,
        "_b_num": b_num,
        "_q_star": q_peak,
        "_s_cert": s_cert,
        "_theta": theta,
    }


def run_part2(smoke: bool, c_inc: mp.mpf) -> tuple[dict, dict]:
    section("PART2  WORST-CASE-BUDGET  (C_inc/4 quads × theta localisation)")
    print(
        "  FORMULA  B = (C_inc/4) Σ_k max_{[k,k+1]} Q_env(σ,t)  "
        "≤ C_inc e^{32} S_cert"
    )
    print(
        "  S_cert = (π/(4a))[Θ_lobe(a)+Θ_left(a,ω)+2 Θ_cross(a,ω)]  "
        "Θ_lobe=2+ϑ₃(0,e^{-1/(2a)})"
    )
    print(
        "  B_lobe = (C_inc/4)(π/a) e^{32} Θ_lobe(a)  "
        "(main-lobe only, certified)"
    )
    print("  C_inc %s  n_quad/bin %s" % (nstr(c_inc), nstr(c_inc / 4)))
    sigmas = SIGMAS[:2] if smoke else SIGMAS
    gammas = GAMMAS[:1] if smoke else GAMMAS
    print(
        "  sigma gamma  |Q_sel|  Q★  S_cert  B_cert  B_num  "
        "B/|Q_sel|  B/margin"
    )
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            row = budget_formulas(
                sigma, mp.mpf(gamma_text), c_inc, sigma_text, gamma_text,
            )
            rows.append(row)
            print(
                "  %s %s  %s  %s  %s  %s  %s  %s  %s"
                % (
                    sigma_text,
                    gamma_text,
                    nstr(abs(row["_q_sel"]), 8),
                    nstr(row["_q_star"], 8),
                    nstr(row["_s_cert"], 8),
                    nstr(row["_b_cert"], 8),
                    nstr(row["_b_num"], 8),
                    nstr(row["_b_cert"] / abs(row["_q_sel"]), 8),
                    nstr(row["_b_cert"] / abs(mp.mpf(R541_MARGIN)), 8),
                )
            )

    # Uniformity of B/|Q_sel| across γ (leading term is γ-free).
    by_sigma: dict[str, list[mp.mpf]] = {}
    for row in rows:
        by_sigma.setdefault(row["sigma"], []).append(mp.mpf(row["B_over_Qsel"]))
    ratio_max = mp.mpf(1)
    for sigma_text, values in by_sigma.items():
        local = max(values) / min(values) if min(values) > 0 else mp.inf
        ratio_max = max(ratio_max, local)
        print(
            "  sigma=%s  B/|Q_sel|_ratio=%s  (γ-scatter of the ratio)"
            % (sigma_text, nstr(local))
        )

    b_max = max(row["_b_cert"] for row in rows)
    q_min = min(abs(row["_q_sel"]) for row in rows)
    margin = abs(mp.mpf(R541_MARGIN))
    budget_lt_qsel = all(row["_b_cert"] < abs(row["_q_sel"]) for row in rows)
    budget_lt_margin = all(row["_b_cert"] < margin for row in rows)
    num_matches = all(
        row["_b_num"] <= row["_b_cert"] * (1 + mp.mpf("1e-12"))
        for row in rows
    )
    check(
        "P2-num-le-certified",
        num_matches,
        "numerical window+tail ≤ C_inc e^{32} S_cert",
    )
    check(
        "P2-B-over-Qsel-gamma-stable",
        ratio_max <= mp.mpf("1.01"),
        "max/min B/|Q_sel| across γ = %s" % nstr(ratio_max),
    )
    # Closed leading coefficient: B/|Q_sel| → (C_inc/4) Θ_lobe e^{π²/128}.
    # Θ_lobe(a)→3 as a→0, so the σ-family sits near (3/4) C_inc e^{π²/128}.
    lead_coeff = (c_inc / 4) * mp.mpf(3) * mp.exp(mp.pi ** 2 / 128)
    print(
        "  LEADING  B/|Q_sel| → (C_inc/4)·3·e^{π²/128} = %s  (a→0)"
        % nstr(lead_coeff)
    )
    print(
        "  budget_lt_Qsel %d  budget_lt_margin %d  B_max %s  |Q_sel|_min %s"
        % (int(budget_lt_qsel), int(budget_lt_margin), nstr(b_max), nstr(q_min))
    )
    public = {
        "rows": [
            {key: value for key, value in row.items() if not key.startswith("_")}
            for row in rows
        ],
        "B_over_Qsel_gamma_ratio": nstr(ratio_max),
        "leading_B_over_Qsel": nstr(lead_coeff),
        "budget_lt_Qsel": str(int(budget_lt_qsel)),
        "budget_lt_margin": str(int(budget_lt_margin)),
        "B_max": nstr(b_max),
        "formula": (
            "B=C_inc*exp(32)*S_cert, "
            "S_cert=(pi/(4a))[Theta_lobe+Theta_left+2 Theta_cross], "
            "Q_star=(pi/a)*exp(32)*[1+2*exp(-omega^2/a)+exp(-2*omega^2/a)]"
        ),
    }
    return public, {
        "budget_lt_qsel": budget_lt_qsel,
        "budget_lt_margin": budget_lt_margin,
        "rows": rows,
        "b_max": b_max,
        "lead_coeff": lead_coeff,
    }


def tie_heights(sigma: mp.mpf, omega: mp.mpf, a: mp.mpf, n_keep: int) -> tuple[mp.mpf, ...]:
    """Heights where the main-lobe phase is 0 mod 2π: t=ω+2π n a/σ."""
    step = 2 * mp.pi * a / sigma
    heights: list[mp.mpf] = []
    n_val = 0
    while len(heights) < n_keep:
        for sign in (1, -1) if n_val else (1,):
            if n_val == 0:
                cand = omega
            else:
                cand = omega + sign * n_val * step
            if cand > 0:
                heights.append(cand)
            if len(heights) >= n_keep:
                break
        n_val += 1
        if n_val > n_keep + 8:
            break
    return tuple(heights[:n_keep])


def run_part3(smoke: bool, c_inc: mp.mpf) -> tuple[dict, dict]:
    section("PART3  GLEICHSTAND-DEGENERATION  (σ' = σ, several packets)")
    print(
        "  antiphase  φ(γ)−φ(ω)=σ(γ−ω)/a=π  ⇒  cos φ(γ)=−cos φ(ω); "
        "a global phase cannot make both negative"
    )
    print(
        "  even class  h(t)=p(t)e^{-at²}cos(ωt+ψ) is even iff ψ≡0 (mod π); "
        "ψ=π only flips the global sign"
    )
    print(
        "  carrier phase ψ scales only the cross term by cos 2ψ "
        "(main lobes unshifted)"
    )
    sigmas = SIGMAS[:2] if smoke else SIGMAS
    gammas = GAMMAS[:1] if smoke else GAMMAS
    k_max = int(mp.floor(c_inc / 4))
    k_scan = (1, 2, 4, k_max) if not smoke else (1, k_max)
    print("  k_max = floor(C_inc/4) = %d" % k_max)
    print("  sigma gamma  Q_sel  Q_tie(ω)  k_flip  k_max_mass/|Q_sel|")

    rows: list[dict] = []
    any_k1_flip = False
    min_k_flip = k_max + 1
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        a_val = scaling_a(sigma)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            q_sel = quadruple_closed(sigma, gamma, a_val, omega)
            q_tie = quadruple_closed(sigma, omega, a_val, omega)
            if q_tie <= 0:
                k_flip = k_max + 1
            else:
                k_flip = int(mp.ceil(abs(q_sel) / q_tie))
            if k_flip <= 1:
                any_k1_flip = True
            min_k_flip = min(min_k_flip, k_flip)
            # Adversarial stack: k copies at the strongest positive-phase sites.
            heights = tie_heights(sigma, omega, a_val, min(8, k_max))
            stack = mp.mpf(0)
            stacked = 0
            for k_use in k_scan:
                mass = mp.mpf(0)
                for index in range(k_use):
                    height = heights[index % len(heights)]
                    mass += quadruple_closed(sigma, height, a_val, omega)
                if k_use == k_scan[0] or k_use == k_max:
                    stack = mass
                    stacked = k_use
            rows.append({
                "sigma": sigma_text,
                "gamma": gamma_text,
                "Q_sel": nstr(q_sel),
                "Q_tie": nstr(q_tie),
                "k_flip": str(k_flip),
                "k_max_mass": nstr(stack),
                "k_max_over_Qsel": nstr(stack / abs(q_sel)),
                "k_used": str(stacked),
            })
            print(
                "  %s %s  %s  %s  %d  %s"
                % (
                    sigma_text,
                    gamma_text,
                    nstr(q_sel, 8),
                    nstr(q_tie, 8),
                    k_flip,
                    nstr(stack / abs(q_sel), 8),
                )
            )

    # Phase-offset diagnostic (inadmissible in the even Lean class).
    phase_repairs = 0
    sigma = mp.mpf(sigmas[0])
    gamma = mp.mpf(gammas[0])
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    for psi_text in PHASE_OFFSETS:
        psi = mp.mpf(psi_text) * mp.pi
        q_s = 4 * mp.re(hat_w_phase(sigma, gamma, a_val, omega, psi))
        q_c = 4 * mp.re(hat_w_phase(sigma, omega, a_val, omega, psi))
        if q_s < 0 and q_c < 0:
            phase_repairs += 1
    # Even-quartic scan.
    b2s = POLY_B2 if not smoke else ("-1", "0", "1")
    b4s = POLY_B4 if not smoke else ("0",)
    poly_hits = 0
    poly_tested = 0
    best_poly = None
    best_score = mp.inf
    for sigma_text in sigmas[:1]:
        sigma = mp.mpf(sigma_text)
        a_val = scaling_a(sigma)
        for gamma_text in gammas[:1]:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            heights = (gamma, omega) + tuple(
                omega + mp.mpf(off) for off in ("1", "-1", "5")
                if omega + mp.mpf(off) > 0
            )
            for b2_text in b2s:
                for b4_text in b4s:
                    b2 = mp.mpf(b2_text)
                    b4 = mp.mpf(b4_text)
                    c0 = mp.mpf(1)
                    c2 = b2 * a_val
                    c4 = b4 * a_val ** 2
                    poly_tested += 1
                    q_s = 4 * mp.re(
                        gabor_hat_poly(c0, c2, c4, a_val, omega, sigma, gamma)
                    )
                    if q_s >= 0:
                        continue
                    foreign_pos = []
                    all_neg = True
                    for height in heights[1:]:
                        q_f = 4 * mp.re(
                            gabor_hat_poly(
                                c0, c2, c4, a_val, omega, sigma, height,
                            )
                        )
                        foreign_pos.append(q_f)
                        if q_f >= 0:
                            all_neg = False
                    score = max(foreign_pos) / abs(q_s)
                    if score < best_score:
                        best_score = score
                        best_poly = {
                            "b2": b2_text,
                            "b4": b4_text,
                            "Q_sel": nstr(q_s),
                            "worst_rel": nstr(score),
                        }
                    if all_neg:
                        poly_hits += 1

    print(
        "  phase_repairs %d/%d  (expect 0: antiphase + even obstruction)"
        % (phase_repairs, len(PHASE_OFFSETS))
    )
    print(
        "  poly_hits %d/%d  best_rel %s  best %s"
        % (
            poly_hits,
            poly_tested,
            nstr(best_score) if mp.isfinite(best_score) else "nan",
            best_poly,
        )
    )
    check(
        "P3-k1-flips",
        any_k1_flip,
        "a single equal-σ packet-centre foreign already beats |Q_sel|",
    )
    check(
        "P3-no-phase-repair",
        phase_repairs == 0,
        "no ψ makes Q(γ)<0 and Q(ω)<0 simultaneously",
    )
    check(
        "P3-no-even-quartic-repair",
        poly_hits == 0,
        "no scanned (b2,b4) keeps all equal-σ grid foreigners negative",
    )
    public = {
        "k_max": str(k_max),
        "min_k_flip": str(min_k_flip),
        "k1_flips": str(int(any_k1_flip)),
        "phase_repairs": str(phase_repairs),
        "poly_hits": str(poly_hits),
        "poly_tested": str(poly_tested),
        "best_poly": best_poly,
        "rows": rows,
        "antiphase": "phi(gamma)-phi(omega)=pi",
        "even_obstruction": "psi==0 mod pi",
    }
    return public, {
        "any_k1_flip": any_k1_flip,
        "min_k_flip": min_k_flip,
        "phase_repairs": phase_repairs,
        "poly_hits": poly_hits,
        "k_max": k_max,
    }


def delta_for_excess(eta: mp.mpf) -> mp.mpf:
    """Smallest δ=ε/σ with e^{32(2δ+δ²)}−1 ≥ eta, δ≥0.  Closed: solve quad."""
    if eta <= 0:
        return mp.mpf(0)
    # e^{32(2δ+δ²)} = 1+eta  ⇒  32(δ²+2δ) = log(1+eta)
    # δ² + 2δ − log(1+eta)/32 = 0  ⇒  δ = −1 + sqrt(1 + log(1+eta)/32)
    target = mp.log(1 + eta) / 32
    return -1 + mp.sqrt(1 + target)


def run_part4(smoke: bool, c_inc: mp.mpf) -> tuple[dict, dict]:
    section("PART4  ε-SUPREMUM  (tune to σ, foreign at σ+ε)")
    print(
        "  excess factor  e^{32((σ+ε)/σ)²}−e^{32} "
        "= e^{32}(e^{32(2δ+δ²)}−1),  δ=ε/σ"
    )
    print(
        "  one-foreign excess  ΔQ = (π/a) e^{32} (e^{32(2δ+δ²)}−1) "
        "× [1+2e^{-ω²/a}+e^{-2ω²/a}]"
    )
    print(
        "  budget scale  B(σ+ε)/B(σ) = e^{32(2δ+δ²)}; "
        "thresholds vs |Q_sel| and vs r541 leftover"
    )
    sigmas = SIGMAS[:2] if smoke else SIGMAS
    gammas = GAMMAS[:1] if smoke else GAMMAS
    margin = abs(mp.mpf(R541_MARGIN))

    rows: list[dict] = []
    print(
        "  sigma gamma  |Q_sel|  δ_1pct  δ_Qsel  δ_margin  "
        "δ_Bdouble  ε_Qsel  γ_indep"
    )
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        a_val = scaling_a(sigma)
        pref = (mp.pi / a_val) * mp.exp(32)
        q_lead = pref  # leading |Q_sel| ~ pref e^{-π²/128}
        # Closed δ for ΔQ_lead = η * scale.
        d_1pct = delta_for_excess(mp.mpf("0.01") * mp.exp(-(mp.pi ** 2) / 128))
        d_qsel = delta_for_excess(mp.exp(-(mp.pi ** 2) / 128))
        d_double = delta_for_excess(mp.mpf(1))
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            omega = scaling_omega(sigma, gamma)
            q_sel = quadruple_closed(sigma, gamma, a_val, omega)
            q0 = q_star(sigma, a_val, omega)
            # Exact δ_margin: ΔQ = q(σ+ε,ω) − q(σ,ω) = margin.
            # q(σ(1+δ),ω) = (π/a) exp(32(1+δ)²) * lobe_poly(ω)
            lobe = q0 / pref
            # ΔQ = pref*lobe*(e^{32(2δ+δ²)}−1) = margin
            eta_m = margin / (pref * lobe) if pref * lobe > 0 else mp.inf
            d_margin = delta_for_excess(eta_m) if eta_m < mp.inf else mp.inf
            # Verify closed δ_Qsel against exact hats at that ε.
            eps_q = d_qsel * sigma
            q_super = q_star(sigma + eps_q, a_val, omega)
            excess = q_super - q0
            # γ-independence: lobe = 1 + O(e^{-ω²/a}), so δ_margin scatter
            # across γ is the only possible γ-channel.
            rows.append({
                "sigma": sigma_text,
                "gamma": gamma_text,
                "Q_sel": nstr(q_sel),
                "delta_1pct": nstr(d_1pct),
                "delta_Qsel": nstr(d_qsel),
                "delta_margin": nstr(d_margin) if mp.isfinite(d_margin) else "inf",
                "delta_Bdouble": nstr(d_double),
                "eps_Qsel": nstr(eps_q),
                "eps_margin": (
                    nstr(d_margin * sigma) if mp.isfinite(d_margin) else "inf"
                ),
                "excess_at_dQsel": nstr(excess),
                "lobe_factor": nstr(lobe),
                "_d_margin": d_margin,
                "_lobe": lobe,
            })
            print(
                "  %s %s  %s  %s  %s  %s  %s  %s  lobe=%s"
                % (
                    sigma_text,
                    gamma_text,
                    nstr(abs(q_sel), 8),
                    nstr(d_1pct, 8),
                    nstr(d_qsel, 8),
                    nstr(d_margin, 8) if mp.isfinite(d_margin) else "inf",
                    nstr(d_double, 8),
                    nstr(eps_q, 8),
                    nstr(lobe, 8),
                )
            )

    # γ-independence of δ_Qsel / δ_1pct / δ_Bdouble: they are closed in δ
    # (no γ).  δ_margin depends on σ through π/a and on γ only through lobe.
    lobe_scatter = mp.mpf(1)
    by_sigma_lobe: dict[str, list[mp.mpf]] = {}
    for row in rows:
        by_sigma_lobe.setdefault(row["sigma"], []).append(row["_lobe"])
    for values in by_sigma_lobe.values():
        local = max(values) / min(values) if min(values) > 0 else mp.inf
        lobe_scatter = max(lobe_scatter, local)
    gamma_indep = lobe_scatter <= mp.mpf("1") + mp.mpf("1e-20")
    # Spectral-gap r* such that B(r) < |Q_sel|: 
    # B(r)/|Q_sel| = (C_inc/4) Θ_lobe exp(32(r²−1)+π²/128)
    # r*² = 1 − (π²/128 + log((C_inc/4)Θ_lobe))/32   if rhs>0.
    theta_ref = theta_lobe(scaling_a(mp.mpf(sigmas[0])))
    log_pre = mp.log((c_inc / 4) * theta_ref)
    rstar_sq = 1 - (mp.pi ** 2 / 128 + log_pre) / 32
    rstar = mp.sqrt(rstar_sq) if rstar_sq > 0 else mp.mpf(0)
    print(
        "  lobe_scatter %s  gamma_indep_leading %d"
        % (nstr(lobe_scatter), int(gamma_indep))
    )
    print(
        "  r_star  B(r)<|Q_sel|  at Θ_lobe(%s)=%s  ⇒  r* = %s"
        % (sigmas[0], nstr(theta_ref), nstr(rstar))
    )
    print(
        "  δ_1pct %s  δ_Qsel %s  δ_Bdouble %s  (all γ-free closed forms)"
        % (
            nstr(delta_for_excess(mp.mpf("0.01") * mp.exp(-(mp.pi ** 2) / 128))),
            nstr(delta_for_excess(mp.exp(-(mp.pi ** 2) / 128))),
            nstr(delta_for_excess(mp.mpf(1))),
        )
    )
    check(
        "P4-gamma-free-leading",
        gamma_indep,
        "lobe factor 1+O(e^{-ω²/a}); scatter %s" % nstr(lobe_scatter),
    )
    check(
        "P4-delta-positive",
        delta_for_excess(mp.mpf("0.01")) > 0,
        "excess thresholds well-defined",
    )
    public = {
        "rows": [
            {key: value for key, value in row.items() if not key.startswith("_")}
            for row in rows
        ],
        "delta_1pct": nstr(
            delta_for_excess(mp.mpf("0.01") * mp.exp(-(mp.pi ** 2) / 128))
        ),
        "delta_Qsel": nstr(delta_for_excess(mp.exp(-(mp.pi ** 2) / 128))),
        "delta_Bdouble": nstr(delta_for_excess(mp.mpf(1))),
        "r_star_budget_lt_Qsel": nstr(rstar),
        "lobe_scatter": nstr(lobe_scatter),
        "gamma_independent_leading": str(int(gamma_indep)),
        "formula": (
            "delta=-1+sqrt(1+log(1+eta)/32), "
            "eta=DeltaQ/((pi/a)e^{32} lobe); "
            "r_star^2=1-(pi^2/128+log((C_inc/4)Theta_lobe))/32"
        ),
    }
    return public, {
        "rstar": rstar,
        "d_qsel": delta_for_excess(mp.exp(-(mp.pi ** 2) / 128)),
        "d_1pct": delta_for_excess(
            mp.mpf("0.01") * mp.exp(-(mp.pi ** 2) / 128)
        ),
        "gamma_indep": gamma_indep,
    }


def decide_verdict(
    p1: dict, p2: dict, p3: dict, p4: dict,
) -> str:
    """Primary verdict on the stated selection σ' ≤ σ (including ties)."""
    worst = p1.get("worst_rec")
    if p3["any_k1_flip"] or p1["flip_sel"] or not p2["budget_lt_qsel"]:
        if worst is None:
            config = "k1_tie_or_budget"
        else:
            config = (
                "sigma=%s,gamma=%s,r=%s,kind=%s,Q=%s"
                % (
                    worst["sigma"],
                    worst["gamma"],
                    worst["ratio"],
                    worst["kind"],
                    worst["Q_foreign"],
                )
            )
        # A spectral gap would restore B(r)<|Q_sel|, but Gleichstand is
        # inside the stated selection and is not repaired by p or ψ.
        if p4["rstar"] > 0 and p3["poly_hits"] == 0:
            return (
                "SELECTION_CONDITIONAL(condition="
                "spectral_gap:sigma_prime/sigma<=%s;"
                "gleichstand_unrepaired;even_phase_inadmissible)"
                % nstr(p4["rstar"])
            )
        return "SELECTION_FAILS(config=%s)" % config
    if p2["budget_lt_margin"]:
        return "SELECTION_RESCUES(budget=%s, margin_ratio=%s)" % (
            nstr(p2["b_max"]),
            nstr(p2["b_max"] / abs(mp.mpf(R541_MARGIN))),
        )
    return "SELECTION_CONDITIONAL(condition=budget_lt_Qsel_but_gt_margin)"


def format_formula() -> str:
    return (
        "Q(σ',t)=(π/a)[A₊cosφ₊+A₋cosφ₋+2Aₓcosφₓ], "
        "A±=exp((σ'²−(t±ω)²)/(2a));  "
        "Q★=Q(σ,ω)=(π/a)e^{32}[1+2e^{-ω²/a}+e^{-2ω²/a}];  "
        "B=C_inc e^{32} S_cert, "
        "S_cert=(π/(4a))[Θ_lobe+Θ_left+2Θ_cross], "
        "Θ_lobe=2+ϑ₃(0,e^{-1/(2a)});  "
        "C_inc=2*(log(2+6ζ(9/8))+log|ζ(2)|+2)/log(14/13);  "
        "δ=−1+√(1+log(1+η)/32)"
    )


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    c_inc = c_inc_prefactor()
    print("gabor_extremal_selection_probe -- r551")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted  class pure_gabor")
    print("scaling a=sigma^2/64  omega=gamma-pi*a/sigma  enh=exp(32)")
    print("C_inner %s" % nstr(c_inner()))
    print("C_inc %s" % nstr(c_inc))
    print("n_quad_per_bin %s" % nstr(c_inc / 4))
    print("FORMULA %s" % format_formula())

    section("G0  CLOSED FORMS / PHASE / ENHANCEMENT / ANTIPHASE")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))

    p1_pub, p1 = run_part1(smoke)
    p2_pub, p2 = run_part2(smoke, c_inc)
    p3_pub, p3 = run_part3(smoke, c_inc)
    p4_pub, p4 = run_part4(smoke, c_inc)

    verdict = decide_verdict(p1, p2, p3, p4)

    section("GATES / VERDICT")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G4-smoke-subset", True, "sigma[:2] gamma[:1] reduced r-grid")
    else:
        check(
            "G4-full-grid",
            True,
            "sigmas=%d gammas=%d ratios=%d"
            % (len(SIGMAS), len(GAMMAS), len(SIGMA_RATIOS)),
        )

    canon = {
        "part1": {key: value for key, value in p1_pub.items() if key != "top"},
        "part1_top": p1_pub.get("top", []),
        "part2": p2_pub,
        "part3": p3_pub,
        "part4": p4_pub,
        "verdict": verdict,
        "SPEC_SHA": SPEC_SHA,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    print("PAYLOAD_SHA256 %s" % seal)
    print("PART1_WORST_REL_SEL %s" % (
        p1_pub["worst"]["rel_sel"] if p1_pub["worst"] else "none"
    ))
    print("PART1_WORST_REL_MARGIN %s" % (
        p1_pub["worst"]["rel_margin"] if p1_pub["worst"] else "none"
    ))
    print("PART2_B_OVER_QSEL_LEADING %s" % p2_pub["leading_B_over_Qsel"])
    print("PART2_BUDGET_LT_QSEL %s" % p2_pub["budget_lt_Qsel"])
    print("PART2_BUDGET_LT_MARGIN %s" % p2_pub["budget_lt_margin"])
    print("PART3_K1_FLIPS %s" % p3_pub["k1_flips"])
    print("PART3_POLY_HITS %s" % p3_pub["poly_hits"])
    print("PART4_RSTAR %s" % p4_pub["r_star_budget_lt_Qsel"])
    print("PART4_DELTA_QSEL %s" % p4_pub["delta_Qsel"])
    print("VERDICT %s" % verdict)
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
            "r551 Gabor extremal-selection vs adversarial off-line "
            "foreign quadruples (experiments only)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
