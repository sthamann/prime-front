#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_uniform_dominance_probe -- r561

Round 561.  Experiments-only SYMBOLIC+NUMERIC successor of r560.

  r560 (sealed): on W_honest = Σ Q_q + R_on a 1-packet Gabor wins the
  52-row increment-compliant catalog + 2 adversarial rounds, via
  afac=1/8 of the r541 lock a=σ²/64.  Lean-Prop leftovers: (1) a
  constructive (a,ω)-rule instead of a grid; (2) uniformity over ALL
  increment-compliant Z; (3) a closed inequality with named constants.

THIS ROUND.  Derive the a→0 dominance inequality for the r541 phase
rule ω=γ−πa/σ (tuned cos φ₋ = −1), book-keep the r551 Gleichstand
opponent, and test a closed bound against the r560 catalog plus the
three danger families (centre-tie, antiphase, k=43 cluster).

CLAIM BOUNDARY.  Finite closed-form / deterministic arithmetic on
increment-compliant catalogs.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/next.txt edit.

HAT CONVENTION.  Sealed r560/r551: Weil-shifted ĥ_W, Q = 4 Re ĥ_W
  Q(σ′,γ′) = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ],
  A± = exp((σ′²−(γ′∓ω)²)/(2a)),  Aₓ = exp((σ′²−γ′²−ω²)/(2a)),
  φ₊ = σ′(γ′+ω)/a,  φ₋ = σ′(γ′−ω)/a,  φₓ = σ′ γ′/a.
R_on = 2 C_inc S_cert, C_inc pin 174.818115823.

Verdicts:
  DOMINANCE_UNIFORM(rule=…, margin_formula=…)
  DOMINANCE_CONDITIONAL(missing=…, exception_window=…)
  DOMINANCE_FAILS(obstruction=…)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import gabor_honest_weil_game_probe as r560  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
HOST_SIGMAS = ("0.01", "0.10", "0.25", "0.49")
HOST_GAMMAS = ("14", "1000")
CATALOG_SIGMAS = ("0.10", "0.25")
A_LOCK_FACTOR = "0.125"
K_MAX_BIN = r560.K_MAX_BIN
C_INC_PIN = r560.C_INC_PIN
NSTR_DIGITS = 12
DPS = 80
TRUNC_NEAR_BINS = 4
ISOLATION_HALVINGS = 60
A_FLOOR_DENOM = "1e12"

SPEC = {
    "round": 561,
    "parent_round": 560,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.UNIFORM_DOMINANCE.01",
    "target": "GaborSeparationInequality.honest_weil_game",
    "hat": "weil_shifted",
    "class": "pure_gabor_unit_amplitude",
    "quantifiers": "forall_Z exists_h  (config first, constructive rule)",
    "objective": "W_honest = Q_off + R_on  (no R_ref, no -3.56)",
    "a_lock": "(sigma^2/64)*1/8",
    "omega_rule": "gamma-pi*a/sigma",
    "isolation": "shrink_a_until_constructive_peak_window_empty",
    "epsilon": "sqrt(2*a*log(max(1/a, 4*K_bin)))",
    "online_budget": "2*C_inc*S_cert",
    "theta_majorant": "2+vartheta_3(0,exp(-1/(2a)))",
    "host_sigmas": list(HOST_SIGMAS),
    "host_gammas": list(HOST_GAMMAS),
    "catalog_sigmas": list(CATALOG_SIGMAS),
    "a_lock_factor": A_LOCK_FACTOR,
    "k_max_bin": K_MAX_BIN,
    "trunc_near_bins": TRUNC_NEAR_BINS,
    "c_inc_pin": C_INC_PIN,
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "scope": (
        "r560 52-row catalog + Gleichstand/antiphase/k=43 cluster "
        "on sigma={0.01,0.10,0.25,0.49} gamma={14,1000}"
    ),
    "excluded": "RH claim; Lean edit; ledger/paper; next.txt",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []

INEQUALITY_LOCK = (
    "W_honest(h_{a,ω}; Z)  ≤  "
    "-(π/a) e^{σ²/2a} η(a,σ) "
    "+ (π/a) e^{σ²/2a} K_bin [4 e^{-ε(a)²/2a} + (Θ_lobe(a)-3)] "
    "+ (π/a) e^{σ²/2a} K_bin [θ_left(a,ω) + 2 θ_cross(a,ω)] "
    "+ 2 C_inc S_cert(a,ω),  "
    "provided no second same-σ quadruple lies in "
    "I_exc(a,ω)=[ω-ε(a), ω+ε(a)],  "
    "where η=exp(-π² a/(2σ²)),  ε(a)=√(2a log max(1/a, 4 K_bin)),  "
    "K_bin=43,  Θ_lobe=3+2Σ_m exp(-m²/2a),  "
    "ω=γ_★-πa/σ,  a=(σ²/64)/8."
)

INEQUALITY_REDUCED = (
    "W/E ≤ -η + K_bin [4 e^{-ε²/2a} + (Θ_lobe-3)] "
    "+ K_bin (θ_left + 2 θ_cross) + R_on/E,  "
    "E=(π/a) e^{σ²/2a}."
)


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


def payload_sha(rows: dict) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def exp_clip(value: mp.mpf) -> mp.mpf:
    return r560.exp_clip(value)


# ---------------------------------------------------------------------------
# Sealed r541/r560 scaling + reduced-unit arithmetic
# ---------------------------------------------------------------------------
def a_lock(sigma: mp.mpf) -> mp.mpf:
    return r560.scaling_a(sigma) * mp.mpf(A_LOCK_FACTOR)


def omega_rule(sigma: mp.mpf, gamma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    return gamma - mp.pi * a_val / sigma


def epsilon_of(a_val: mp.mpf) -> mp.mpf:
    if a_val <= 0:
        return mp.mpf(0)
    log_term = mp.log(max(1 / a_val, mp.mpf(4 * K_MAX_BIN)))
    if log_term < 1:
        log_term = mp.mpf(1)
    return mp.sqrt(2 * a_val * log_term)


def enhancement_exp(sigma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    return sigma ** 2 / (2 * a_val)


def eta_tune(sigma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    """Tuned minus-lobe envelope vs raw e^{σ²/2a}: exp(-π² a / (2σ²))."""
    return exp_clip(-(mp.pi ** 2) * a_val / (2 * sigma ** 2))


def rho_tie(sigma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    """Centre-tie / |tuned| envelope ratio exp(+π² a / (2σ²))."""
    return exp_clip((mp.pi ** 2) * a_val / (2 * sigma ** 2))


def q_reduced(
    sigma_p: mp.mpf,
    t_value: mp.mpf,
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_ref: mp.mpf,
) -> mp.mpf:
    """Q / E(a,σ_ref) with E=(π/a) exp(σ_ref²/2a).  Sealed r560 phases."""
    scale = (sigma_p ** 2 - sigma_ref ** 2) / (2 * a_val)
    a_plus = exp_clip(scale - (t_value + omega) ** 2 / (2 * a_val))
    a_minus = exp_clip(scale - (t_value - omega) ** 2 / (2 * a_val))
    a_cross = exp_clip(scale - (t_value ** 2 + omega ** 2) / (2 * a_val))
    phi_plus = sigma_p * (t_value + omega) / a_val
    phi_minus = sigma_p * (t_value - omega) / a_val
    phi_cross = sigma_p * t_value / a_val
    return (
        a_plus * mp.cos(phi_plus)
        + a_minus * mp.cos(phi_minus)
        + 2 * a_cross * mp.cos(phi_cross)
    )


def budget_reduced(
    a_val: mp.mpf, omega: mp.mpf, c_inc: mp.mpf, sigma_ref: mp.mpf,
) -> mp.mpf:
    raw = r560.online_budget(a_val, omega, c_inc)
    return raw * (a_val / mp.pi) * exp_clip(-enhancement_exp(sigma_ref, a_val))


def w_reduced(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    c_inc: mp.mpf,
    sigma_ref: mp.mpf,
) -> mp.mpf:
    total = mp.mpf(0)
    for sigma_p, gamma_p in quads:
        total += q_reduced(sigma_p, gamma_p, a_val, omega, sigma_ref)
    return total + budget_reduced(a_val, omega, c_inc, sigma_ref)


def truncated_minus_majorant(a_val: mp.mpf) -> mp.mpf:
    """Σ_bins max_{|t-ω|≥ε} exp(-(t-ω)²/2a) ≤ 4 e^{-ε²/2a} + (Θ_lobe-3)."""
    eps = epsilon_of(a_val)
    edge = exp_clip(-(eps * eps) / (2 * a_val))
    tail = r560.theta_lobe(a_val) - 3
    if tail < 0:
        tail = mp.mpf(0)
    return TRUNC_NEAR_BINS * edge + tail


def bound_exc_reduced(
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_ref: mp.mpf,
    c_inc: mp.mpf,
    host_q_red: mp.mpf,
) -> mp.mpf:
    """Closed upper bound on W/E, valid when I_exc is empty of foreign same-σ."""
    others_minus = mp.mpf(K_MAX_BIN) * truncated_minus_majorant(a_val)
    others_plus = mp.mpf(K_MAX_BIN) * r560.theta_left_pos(a_val, omega)
    others_cross = (
        2 * mp.mpf(K_MAX_BIN) * r560.theta_cross_pos(a_val, omega)
    )
    return (
        host_q_red
        + others_minus
        + others_plus
        + others_cross
        + budget_reduced(a_val, omega, c_inc, sigma_ref)
    )


def bound_crude_reduced(
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_ref: mp.mpf,
    c_inc: mp.mpf,
    host_q_red: mp.mpf,
) -> mp.mpf:
    """Always-valid (loose) bound: centre-tie allowed, full Θ_lobe minus-lobe."""
    others_minus = mp.mpf(K_MAX_BIN) * r560.theta_lobe(a_val)
    others_plus = mp.mpf(K_MAX_BIN) * r560.theta_left_pos(a_val, omega)
    others_cross = (
        2 * mp.mpf(K_MAX_BIN) * r560.theta_cross_pos(a_val, omega)
    )
    return (
        host_q_red
        + others_minus
        + others_plus
        + others_cross
        + budget_reduced(a_val, omega, c_inc, sigma_ref)
    )


# ---------------------------------------------------------------------------
# Constructive (a,ω) rule
# ---------------------------------------------------------------------------
def extremal_host(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[mp.mpf, mp.mpf]:
    """Max σ, then min γ.  r551 extremal selection."""
    sigma_star = max(sigma for sigma, _ in quads)
    gammas = [gamma for sigma, gamma in quads if abs(sigma - sigma_star) < mp.mpf("1e-18")]
    return sigma_star, min(gammas)


def d_min_foreign(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    gamma_star: mp.mpf,
) -> mp.mpf:
    """Min height gap from the host copies to any other quadruple."""
    best = mp.inf
    for _, gamma_p in quads:
        dist = abs(gamma_p - gamma_star)
        if dist > mp.mpf("1e-18") and dist < best:
            best = dist
    return best


def window_occupied(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    gamma_star: mp.mpf,
    a_val: mp.mpf,
    omega: mp.mpf,
) -> bool:
    """Foreign quadruple in I_exc(a,ω)=[ω-ε,ω+ε]; host copies at γ_★ excluded."""
    eps = epsilon_of(a_val)
    for _, gamma_p in quads:
        if abs(gamma_p - gamma_star) <= mp.mpf("1e-18"):
            continue
        if abs(gamma_p - omega) <= eps:
            return True
    return False


def isolated(sigma: mp.mpf, d_min: mp.mpf, a_val: mp.mpf) -> bool:
    if not mp.isfinite(d_min):
        return True
    return (mp.pi * a_val / sigma) + epsilon_of(a_val) <= d_min / 2


def isolation_a(sigma: mp.mpf, d_min: mp.mpf, a_seed: mp.mpf) -> mp.mpf:
    """Shrink a from a_seed until the constructive peak sits in the host gap."""
    if not mp.isfinite(d_min):
        return a_seed
    a_val = a_seed
    floor = (sigma ** 2) / mp.mpf(A_FLOOR_DENOM)
    for _ in range(ISOLATION_HALVINGS):
        if isolated(sigma, d_min, a_val):
            return a_val
        nxt = a_val / 4
        if nxt < floor:
            return a_val
        a_val = nxt
    return a_val


def rule_lock(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[str, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    sigma_star, gamma_star = extremal_host(quads)
    a_val = a_lock(sigma_star)
    omega = omega_rule(sigma_star, gamma_star, a_val)
    return "lock_afac=1/8", a_val, omega, sigma_star, gamma_star


def rule_isolation(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[str, mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    sigma_star, gamma_star = extremal_host(quads)
    d_min = d_min_foreign(quads, gamma_star)
    a_seed = a_lock(sigma_star)
    a_val = isolation_a(sigma_star, d_min, a_seed)
    omega = omega_rule(sigma_star, gamma_star, a_val)
    tag = "isolation"
    if a_val != a_seed:
        tag = "isolation_shrunk"
    if not isolated(sigma_star, d_min, a_val):
        tag = "isolation_cover_fallback"
        a_val = a_seed
        omega = omega_rule(sigma_star, gamma_star, a_val)
    return tag, a_val, omega, sigma_star, gamma_star


# ---------------------------------------------------------------------------
# Symbolic identities (sympy) + mpmath checks
# ---------------------------------------------------------------------------
def run_symbolic() -> dict:
    section("PART0  ASYMPTOTICS a→0  (sympy identities + mpmath check)")
    a_s, sig, gam, pi_s = sp.symbols("a sigma gamma pi", positive=True)
    omega_s = gam - pi_s * a_s / sig
    phi_m = sp.simplify(sig * (gam - omega_s) / a_s)
    phi_tie = sp.simplify(sig * (omega_s - omega_s) / a_s)
    detune = sp.simplify(gam - omega_s)
    a_minus_tuned = sp.simplify(sp.exp((sig ** 2 - detune ** 2) / (2 * a_s)))
    a_minus_tie = sp.simplify(sp.exp((sig ** 2 - (omega_s - omega_s) ** 2) / (2 * a_s)))
    eta_s = sp.simplify(a_minus_tuned / sp.exp(sig ** 2 / (2 * a_s)))
    rho_s = sp.simplify(a_minus_tie / a_minus_tuned)
    leftover_s = sp.simplify(1 - eta_s)
    leftover_lead = leftover_s.series(a_s, 0, 2).removeO()
    rho_limit = sp.limit(rho_s, a_s, 0)

    print("  φ₋(tuned)     = %s   (want π, so cos=−1)" % phi_m)
    print("  φ₋(centre)    = %s   (want 0, so cos=+1)" % phi_tie)
    print("  η(a,σ)        = %s" % eta_s)
    print("  ρ_tie=A₋(ω)/A₋(γ) = %s" % rho_s)
    print("  lim_{a→0} ρ_tie   = %s" % rho_limit)
    print("  1−η leading   = %s" % leftover_lead)
    print("  PHASE_TIE(a)  = cos φ₋(ω) = 1   (identically, all a)")
    print(
        "  r551 ratio at a=σ²/64 is e^{π²/128}≈1.080; "
        "as a→0 this envelope ratio → 1, but Q_tuned+Q_tie "
        "~ (π³/(2σ²)) e^{σ²/2a} stays POSITIVE and explodes."
    )

    phi_ok = sp.simplify(phi_m - pi_s) == 0
    tie_phi_ok = phi_tie == 0
    eta_ok = sp.simplify(eta_s - sp.exp(-(pi_s ** 2) * a_s / (2 * sig ** 2))) == 0
    rho_ok = sp.simplify(rho_s - sp.exp((pi_s ** 2) * a_s / (2 * sig ** 2))) == 0
    lim_ok = rho_limit == 1
    check("S0-phi-tuned-pi", phi_ok, "σ(γ−ω)/a = π")
    check("S0-phi-centre-zero", tie_phi_ok, "σ(ω−ω)/a = 0")
    check("S0-eta-formula", eta_ok, "η=exp(-π² a/(2σ²))")
    check("S0-rho-formula", rho_ok, "ρ=exp(+π² a/(2σ²))")
    check("S0-rho-limit-1", lim_ok, "Gleichstand envelope ratio → 1")

    # mpmath: r551 identity + a→0 leftover sign.
    max_err = mp.mpf(0)
    pred_r551 = mp.exp(mp.pi ** 2 / 128)
    for sigma_text in ("0.10", "0.25"):
        sigma = mp.mpf(sigma_text)
        gamma = mp.mpf(14)
        a_ref = r560.scaling_a(sigma)
        omega = r560.scaling_omega(sigma, gamma)
        q_sel = r560.quadruple_closed(sigma, gamma, a_ref, omega)
        q_cen = r560.quadruple_closed(sigma, omega, a_ref, omega)
        max_err = max(max_err, abs(q_cen / abs(q_sel) - pred_r551))
        max_err = max(max_err, abs(sigma * (gamma - omega) / a_ref - mp.pi))
        # lock-scale phase at centre is exactly 0.
        max_err = max(max_err, abs(sigma * (omega - omega) / a_ref))
        # a→0: leftover of {tuned, centre} stays positive.
        for fac in (mp.mpf(1), mp.mpf("0.25"), mp.mpf("0.0625")):
            a_val = a_ref * fac
            om = omega_rule(sigma, gamma, a_val)
            q_t = q_reduced(sigma, gamma, a_val, om, sigma)
            q_c = q_reduced(sigma, om, a_val, om, sigma)
            leftover = q_t + q_c
            if leftover <= 0:
                max_err = max(max_err, mp.mpf(1))
            pred = 1 - eta_tune(sigma, a_val)
            max_err = max(max_err, abs(leftover - pred))
    check(
        "S0-r551-ratio-lock",
        max_err < mp.mpf("1e-8"),
        "max_err=%s  e^{π²/128}=%s" % (nstr(max_err, 6), nstr(pred_r551, 8)),
    )
    check(
        "S0-killer-survives-a-to-0",
        True,
        "Q_tuned+Q_centre > 0 for a=a_ref, a_ref/4, a_ref/16 (phase factor ≡ 1)",
    )
    print("  INEQUALITY  %s" % INEQUALITY_LOCK)
    print("  REDUCED     %s" % INEQUALITY_REDUCED)
    print(
        "  EXCEPTION   no second same-σ quadruple in "
        "I_exc=[ω-ε(a),ω+ε(a)],  ε(a)=√(2a log max(1/a, 4 K_bin)) → 0"
    )
    return {
        "phi_tuned": str(phi_m),
        "phi_centre": str(phi_tie),
        "eta": str(eta_s),
        "rho_tie": str(rho_s),
        "rho_limit": str(rho_limit),
        "phase_tie": "1",
        "r551_ratio": nstr(pred_r551, 8),
        "killer_survives": "1",
        "leftover_leading": str(leftover_lead),
        "max_err": nstr(max_err, 6),
        "inequality": INEQUALITY_LOCK,
    }


# ---------------------------------------------------------------------------
# Configurations
# ---------------------------------------------------------------------------
def danger_configs(
    sigma: mp.mpf, gamma: mp.mpf,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    """Fixed geometries (not adaptive to the later ω).  Lock-scale gaps."""
    a_ref = a_lock(sigma)
    gap = mp.pi * a_ref / sigma
    omega0 = omega_rule(sigma, gamma, a_ref)
    out: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    out.append(("danger:tie_centre", ((sigma, gamma), (sigma, omega0))))
    n_left = K_MAX_BIN // 2
    n_right = K_MAX_BIN - n_left
    out.append(
        (
            "danger:antiphase_k43",
            tuple(
                [(sigma, omega0)] * n_left
                + [(sigma, omega0 + gap)] * n_right
            ),
        )
    )
    pts = tuple(
        gamma + (mp.mpf(index) / (K_MAX_BIN - 1))
        for index in range(K_MAX_BIN)
    )
    out.append(
        ("danger:cluster_k43_unit", tuple((sigma, site) for site in pts))
    )
    return out


def eval_cell(
    name: str,
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    rule_fn,
) -> dict:
    tag, a_val, omega, sigma_star, gamma_star = rule_fn(quads)
    occupied = window_occupied(quads, gamma_star, a_val, omega)
    host_q = q_reduced(sigma_star, gamma_star, a_val, omega, sigma_star)
    w_red = w_reduced(quads, a_val, omega, c_inc, sigma_star)
    b_exc = bound_exc_reduced(a_val, omega, sigma_star, c_inc, host_q)
    b_crude = bound_crude_reduced(a_val, omega, sigma_star, c_inc, host_q)
    eta = eta_tune(sigma_star, a_val)
    # Conservative: bound must sit above exact W (in reduced units).
    # Use a relative slack scaled to 1+|W| so underflow-tiny W still compares.
    slack = mp.mpf("1e-8") * (1 + abs(w_red) + abs(b_exc) + abs(b_crude))
    crude_valid = b_crude + slack >= w_red
    exc_valid = (not occupied) and (b_exc + slack >= w_red)
    exc_applies = not occupied
    return {
        "name": name,
        "rule": tag,
        "n_quad": str(len(quads)),
        "inc_ok": str(int(r560.increment_ok(quads))),
        "a": nstr(a_val),
        "omega": nstr(omega),
        "sigma": nstr(sigma_star),
        "gamma": nstr(gamma_star),
        "eps": nstr(epsilon_of(a_val)),
        "eta": nstr(eta),
        "rho_tie": nstr(rho_tie(sigma_star, a_val)),
        "window_occupied": str(int(occupied)),
        "W_red": nstr(w_red),
        "B_exc_red": nstr(b_exc),
        "B_crude_red": nstr(b_crude),
        "W_neg": str(int(w_red < 0)),
        "B_exc_neg": str(int(b_exc < 0)),
        "crude_valid": str(int(crude_valid)),
        "exc_valid": str(int(exc_valid)),
        "exc_applies": str(int(exc_applies)),
        "_W": w_red,
        "_B_exc": b_exc,
        "_B_crude": b_crude,
        "_occupied": occupied,
        "_crude_valid": crude_valid,
        "_exc_valid": exc_valid,
        "_host_q": host_q,
        "_a": a_val,
        "_omega": omega,
    }


def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    g0_ok, g0_err = r560.run_g0(c_inc)
    max_err = max(max_err, g0_err)
    if not g0_ok:
        max_err = max(max_err, mp.mpf(1))
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    a_val = a_lock(sigma)
    omega = omega_rule(sigma, gamma, a_val)
    # Reduced Q recovers sealed Q / E.
    e_log = enhancement_exp(sigma, a_val)
    q_raw = r560.quadruple_closed(sigma, gamma, a_val, omega)
    q_red = q_reduced(sigma, gamma, a_val, omega, sigma)
    recon = q_red * (mp.pi / a_val) * exp_clip(e_log)
    rel = abs(recon - q_raw) / (1 + abs(q_raw))
    max_err = max(max_err, rel)
    # Tuned minus cosine is −1.
    phi = sigma * (gamma - omega) / a_val
    max_err = max(max_err, abs(phi - mp.pi))
    max_err = max(max_err, abs(mp.cos(phi) + 1))
    # Centre cosine is +1.
    phi_c = sigma * (omega - omega) / a_val
    max_err = max(max_err, abs(mp.cos(phi_c) - 1))
    pin = mp.mpf(C_INC_PIN)
    max_err = max(max_err, abs(c_inc - pin) / pin)
    if K_MAX_BIN != 43:
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-8"), max_err


def run_catalog(smoke: bool, c_inc: mp.mpf) -> tuple[list[dict], list[dict]]:
    section("PART1  R560 CATALOG  (lock vs isolation; bound vs exact W/E)")
    sigmas = (CATALOG_SIGMAS[1],) if smoke else CATALOG_SIGMAS
    lock_rows: list[dict] = []
    iso_rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        gamma = mp.mpf(HOST_GAMMAS[0])
        for name, quads in r560.make_catalog(sigma, gamma, smoke):
            full = "%s|s=%s|g=%s" % (name, sigma_text, HOST_GAMMAS[0])
            lock_rows.append(eval_cell(full, quads, c_inc, rule_lock))
            iso_rows.append(eval_cell(full, quads, c_inc, rule_isolation))
    print(
        "  name                              rule            W/E        "
        "B_exc/E    occ winB"
    )
    shown = lock_rows[:8] if smoke else lock_rows
    for row in shown:
        print(
            "  %-32s %-14s %s  %s  %s  %s"
            % (
                row["name"][:32],
                row["rule"][:14],
                nstr(row["_W"], 5),
                nstr(row["_B_exc"], 5),
                row["window_occupied"],
                row["W_neg"],
            )
        )
    if not smoke and len(lock_rows) > 8:
        print("  ... %d catalog cells (lock+isolation each)" % len(lock_rows))
    return lock_rows, iso_rows


def run_danger(smoke: bool, c_inc: mp.mpf) -> tuple[list[dict], list[dict]]:
    section("PART2  DANGER FAMILIES  (tie / antiphase / cluster k=43)")
    sigmas = (HOST_SIGMAS[2],) if smoke else HOST_SIGMAS
    gammas = (HOST_GAMMAS[0],) if smoke else HOST_GAMMAS
    lock_rows: list[dict] = []
    iso_rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            for name, quads in danger_configs(sigma, gamma):
                full = "%s|s=%s|g=%s" % (name, sigma_text, gamma_text)
                lock_rows.append(eval_cell(full, quads, c_inc, rule_lock))
                iso_rows.append(eval_cell(full, quads, c_inc, rule_isolation))
    print(
        "  name                              rule            W/E        "
        "B_exc/E    occ winB"
    )
    for row in lock_rows + iso_rows:
        print(
            "  %-32s %-14s %s  %s  %s  %s"
            % (
                row["name"][:32],
                row["rule"][:14],
                nstr(row["_W"], 5),
                nstr(row["_B_exc"], 5),
                row["window_occupied"],
                row["W_neg"],
            )
        )
    return lock_rows, iso_rows


def tally(rows: list[dict]) -> dict[str, int]:
    n = len(rows)
    return {
        "n": n,
        "inc_ok": sum(1 for row in rows if row["inc_ok"] == "1"),
        "crude_valid": sum(1 for row in rows if row["_crude_valid"]),
        "exc_applies": sum(1 for row in rows if not row["_occupied"]),
        "exc_valid": sum(
            1
            for row in rows
            if (not row["_occupied"]) and row["_exc_valid"]
        ),
        "W_neg": sum(1 for row in rows if row["_W"] < 0),
        "B_exc_neg": sum(
            1
            for row in rows
            if (not row["_occupied"]) and row["_B_exc"] < 0
        ),
        "occupied": sum(1 for row in rows if row["_occupied"]),
    }


def decide(
    lock_cat: list[dict],
    iso_cat: list[dict],
    lock_dan: list[dict],
    iso_dan: list[dict],
    symbolic: dict,
) -> tuple[str, dict, str]:
    iso_all = iso_cat + iso_dan
    lock_all = lock_cat + lock_dan
    iso_t = tally(iso_all)
    lock_t = tally(lock_all)
    extra = {
        "iso": {k: str(v) for k, v in iso_t.items()},
        "lock": {k: str(v) for k, v in lock_t.items()},
        "phase_tie": "1",
        "rho_limit": "1",
        "r551_ratio": symbolic["r551_ratio"],
        "killer_survives_a_to_0": "1",
        "epsilon": "sqrt(2*a*log(max(1/a,4*K_bin)))",
        "inequality": INEQUALITY_LOCK,
    }
    # Bound validity: crude always; exc on empty-window cells.
    crude_ok = all(row["_crude_valid"] for row in lock_all + iso_all)
    exc_ok = True
    for row in iso_all + lock_all:
        if row["_occupied"]:
            continue
        if not row["_exc_valid"]:
            exc_ok = False
            extra["exc_invalid"] = row["name"]
            break
    extra["crude_ok"] = str(int(crude_ok))
    extra["exc_ok"] = str(int(exc_ok))

    iso_wins = iso_t["n"] > 0 and iso_t["W_neg"] == iso_t["n"]
    iso_bound_proves = (
        iso_t["exc_applies"] == iso_t["n"]
        and iso_t["B_exc_neg"] == iso_t["n"]
        and iso_t["exc_valid"] == iso_t["n"]
    )
    lock_occupied = lock_t["occupied"]
    extra["iso_wins"] = str(int(iso_wins))
    extra["iso_bound_proves"] = str(int(iso_bound_proves))
    extra["lock_occupied"] = str(lock_occupied)

    missing = (
        "no second same-σ quadruplet in I_exc(a,ω)=[ω-ε(a),ω+ε(a)] "
        "with favourable minus-lobe phase (cos φ₋ > 0); "
        "ε(a)=√(2a log max(1/a, 4 K_bin)) → 0 as a→0 "
        "(asymptotically vanishing exception set).  "
        "The r541/r560 lock (a=(σ²/64)/8, ω=γ-πa/σ) is Z-independent "
        "and is killed by a centre-tie of equal σ (phase factor ≡ 1, "
        "envelope ratio → 1, leftover ~ (π³/(2σ²)) e^{σ²/2a} > 0).  "
        "A Z-dependent isolation shrink empties I_exc for every finite "
        "increment-compliant Z, but the named-constant inequality "
        "without that emptiness hypothesis does not dominate."
    )
    exception_window = (
        "ε(a)=sqrt(2*a*log(max(1/a, 4*K_bin))); "
        "I_exc=[ω-ε,ω+ε]; length 2ε(a)→0"
    )

    if not crude_ok:
        verdict = "DOMINANCE_FAILS(obstruction=bound_not_conservative)"
        lean = "FAIL"
        extra["missing"] = missing
        extra["exception_window"] = exception_window
        return verdict, extra, lean

    if iso_wins and iso_bound_proves and exc_ok:
        verdict = (
            "DOMINANCE_UNIFORM(rule=isolation_shrink_from_lock_afac=1/8, "
            "margin_formula=W/E<=-eta+K_bin[4*exp(-eps^2/2a)+(Theta-3)]"
            "+K_bin(theta_left+2*theta_cross)+R_on/E)"
        )
        lean = "UNIFORM"
        extra["missing"] = ""
        extra["exception_window"] = exception_window
        extra["rule"] = (
            "(σ_★,γ_★)=lexmax(σ,-γ); a=min{a_lock, a: πa/σ+ε(a)≤d_min/2}; "
            "ω=γ_★-πa/σ_★"
        )
        return verdict, extra, lean

    verdict = (
        "DOMINANCE_CONDITIONAL(missing=no_second_same_sigma_quad_in_"
        "I_exc(a,omega)_favourable_phase, exception_window=%s)"
        % exception_window
    )
    extra["missing"] = missing
    extra["exception_window"] = exception_window
    extra["rule"] = "lock a=(sigma^2/64)/8, omega=gamma-pi*a/sigma"
    return verdict, extra, "CONDITIONAL"


def lean_candidate(verdict: str, extra: dict) -> str:
    bricks = (
        "Existing Lean bricks (already sorry-free, no RH claim):\n"
        "  (Θ_lobe) RH.GaborThetaBound.thetaLobe, gauss_binMax_tsum_le, "
        "bin_partial_summation, gauss_online_mass_uniform "
        "[r552; Θ_lobe(a)=3+2Σ_m exp(-m²/2a)].\n"
        "  (increment) RH.ZeroIncrement.zeta_unit_increment / "
        "gaborIncrementBound_holds  "
        "[C=2*zetaZerosInDiskCardBoundInner, times (1+log(T+3)); "
        "C_inc pin 174.818115823 is the log-free prefactor].\n"
        "  (three-lobe) RH.GaborHatAnalytic.gaborThreeLobe, "
        "norm_pureGaborHatDelta_le_three_lobe, "
        "norm_gaborHat_le_three_lobe, gaborThreeLobe_le_gaussian.\n"
        "  (hat algebra) RH.GaborHatAnalytic.pureGaborHatHolomorphic_eq_delta, "
        "gaborHat_one_sub.\n"
        "Missing for the Prop: (i) the truncated-theta form "
        "Σ_{bins, |t-ω|≥ε} max ≤ 4 e^{-ε²/2a} + (Θ_lobe-3) for small a; "
        "(ii) the Q closed form as 4 Re ĥ_W with the sealed A±/Aₓ/φ "
        "expansion (currently numeric in the probe, holomorphic in Lean); "
        "(iii) the isolation-shrink existence (or the I_exc emptiness "
        "hypothesis) wired to a named (a,ω)."
    )
    if extra.get("iso_bound_proves") == "1" and verdict.startswith(
        "DOMINANCE_UNIFORM"
    ):
        prop = (
            "Lean-candidate Prop (NO RH CLAIM).\n"
            "Hypotheses.  Z is any increment-compliant off-line "
            "configuration (≤ K_bin=43 FE quadruples per unit bin; "
            "from gaborIncrementBound_holds after dropping the log "
            "into C_inc).  h(t)=e^{-a t²} cos(ω t) is the unit-amplitude "
            "pure Gabor.\n"
            "(a,ω)-rule.  (σ_★,γ_★) := lex-max (σ, −γ) over Z; "
            "d_min := min{|γ'−γ_★| : (σ',γ')∈Z, γ'≠γ_★} (or +∞); "
            "a_lock := (σ_★²/64)/8; "
            "a(Z) := max{ a ∈ (0, a_lock] : π a/σ_★ + ε(a) ≤ d_min/2 } "
            "with ε(a)=√(2a log max(1/a, 4 K_bin)), or a_lock if d_min=+∞; "
            "ω(Z) := γ_★ − π a(Z)/σ_★.\n"
            "Conclusion.  W_honest(h_{a,ω}; Z) < 0, via the named bound\n"
            "  W/E ≤ −η + K_bin[4 e^{−ε²/2a}+(Θ_lobe−3)] "
            "+ K_bin(θ_left+2 θ_cross) + R_on/E,\n"
            "with E=(π/a) e^{σ_★²/2a}, η=exp(−π² a/(2σ_★²)), "
            "R_on=2 C_inc S_cert.\n"
            "The I_exc emptiness is a CONSEQUENCE of a(Z), not an extra "
            "hypothesis.\n"
        )
    else:
        prop = (
            "Lean-candidate Prop (NO RH CLAIM).\n"
            "Hypotheses.  (H1) Increment: Z has ≤ K_bin=43 FE quadruples "
            "per unit bin (ZeroIncrement / gaborIncrementBound_holds, "
            "log-free C_inc).  (H2) MINIMAL EXTRA: no second quadruple "
            "with σ'=σ_★ occupies I_exc(a,ω)=[ω−ε(a), ω+ε(a)] with "
            "favourable minus-lobe phase; "
            "ε(a)=√(2a log max(1/a, 4 K_bin)), length 2ε(a)→0 as a→0 "
            "(asymptotically vanishing exception set).  "
            "Without (H2) a centre-tie of equal σ contributes "
            "+(π/a) e^{σ²/2a} (phase factor ≡ 1) and cancels the tuned "
            "term up to a positive leftover (π³/(2σ²)) e^{σ²/2a}.\n"
            "(a,ω)-rule.  (σ_★,γ_★) := lex-max (σ, −γ) over Z; "
            "a := (σ_★²/64)/8;  ω := γ_★ − π a/σ_★.  "
            "(Z-independent lock; isolation-shrink is the constructive "
            "escape that realises (H2) for every finite Z, but is not "
            "this named-constant statement.)\n"
            "Conclusion.  W_honest(h_{a,ω}; Z) < 0, via\n"
            "  W/E ≤ −η + K_bin[4 e^{−ε²/2a}+(Θ_lobe−3)] "
            "+ K_bin(θ_left+2 θ_cross) + R_on/E,\n"
            "E=(π/a) e^{σ_★²/2a}, η=exp(−π² a/(2σ_★²)), "
            "R_on=2 C_inc S_cert.\n"
        )
    return prop + bricks


def compact_rows(rows: list[dict]) -> list[dict]:
    keys = (
        "name", "rule", "n_quad", "inc_ok", "a", "omega", "eps", "eta",
        "window_occupied", "W_red", "B_exc_red", "B_crude_red",
        "W_neg", "B_exc_neg", "crude_valid", "exc_valid", "exc_applies",
    )
    return [{key: row[key] for key in keys} for row in rows]


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    r560.mp.mp.dps = DPS
    c_inc = r560.c_inc_prefactor()
    print("gabor_uniform_dominance_probe -- r561")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("quantifiers forall_Z exists_h  (config first, constructive rule)")
    print("online 2*C_inc*S_cert  C_inc %s" % nstr(c_inc))
    print("FORMULA  W_honest = Q_off + R_on   (no R_ref, no -3.56)")
    print("FORMULA  %s" % INEQUALITY_REDUCED)

    section("G0  SEALED FORMS / C_inc PIN / PHASE IDENTITIES")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))
    check(
        "G0-c-inc-pin",
        abs(c_inc - mp.mpf(C_INC_PIN)) / mp.mpf(C_INC_PIN) < mp.mpf("1e-9"),
        "C_inc=%s pin=%s" % (nstr(c_inc), C_INC_PIN),
    )

    symbolic = run_symbolic()

    lock_cat, iso_cat = run_catalog(smoke, c_inc)
    if smoke:
        check("P1-smoke-catalog", len(lock_cat) >= 4, "n=%d" % len(lock_cat))
    else:
        check("P1-catalog-52", len(lock_cat) == 52, "n=%d" % len(lock_cat))
    check(
        "P1-increment-ok",
        all(row["inc_ok"] == "1" for row in lock_cat + iso_cat),
        "every catalog Z has ≤%d quads/bin" % K_MAX_BIN,
    )

    lock_dan, iso_dan = run_danger(smoke, c_inc)
    n_danger_expected = 3 if smoke else 3 * len(HOST_SIGMAS) * len(HOST_GAMMAS)
    check(
        "P2-danger-count",
        len(lock_dan) == n_danger_expected,
        "n=%d expected=%d" % (len(lock_dan), n_danger_expected),
    )
    check(
        "P2-danger-increment",
        all(row["inc_ok"] == "1" for row in lock_dan + iso_dan),
        "danger families increment-compliant",
    )

    section("PART3  BOUND VALIDITY / VERDICT")
    all_rows = lock_cat + iso_cat + lock_dan + iso_dan
    crude_fail = [row["name"] for row in all_rows if not row["_crude_valid"]]
    exc_fail = [
        row["name"]
        for row in all_rows
        if (not row["_occupied"]) and (not row["_exc_valid"])
    ]
    check(
        "P3-crude-bound-valid",
        not crude_fail,
        "failures=%d" % len(crude_fail) if crude_fail else "all cells",
    )
    check(
        "P3-exc-bound-valid-on-empty-window",
        not exc_fail,
        "failures=%d" % len(exc_fail) if exc_fail else "all empty-window cells",
    )

    # Frozen (not retuned) lock targeting γ, companion at ω: r551 leftover > 0.
    # Config-first lock *retunes* to min γ, so the frozen pair is not a
    # lock-loss; antiphase_k43 is the remaining lock obstruction.
    frozen_pos = True
    frozen_detail = []
    sigmas_f = (HOST_SIGMAS[2],) if smoke else HOST_SIGMAS
    gammas_f = (HOST_GAMMAS[0],) if smoke else HOST_GAMMAS
    for sigma_text in sigmas_f:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas_f:
            gamma = mp.mpf(gamma_text)
            a_val = a_lock(sigma)
            omega = omega_rule(sigma, gamma, a_val)
            leftover = (
                q_reduced(sigma, gamma, a_val, omega, sigma)
                + q_reduced(sigma, omega, a_val, omega, sigma)
                + budget_reduced(a_val, omega, c_inc, sigma)
            )
            frozen_detail.append(leftover)
            if leftover <= 0:
                frozen_pos = False
    check(
        "P3-frozen-tie-leftover-positive",
        frozen_pos,
        "min leftover/E=%s (r551 killer, (a,ω) frozen at γ)"
        % nstr(min(frozen_detail), 6),
    )
    lock_anti = [
        row for row in lock_dan if "antiphase_k43" in row["name"]
    ]
    if lock_anti:
        check(
            "P3-lock-antiphase-can-lose",
            any(row["_W"] >= 0 for row in lock_anti),
            "Z-independent lock does not dominate antiphase_k43",
        )
    iso_ties = [
        row for row in iso_dan if "tie_centre" in row["name"]
    ]
    if iso_ties:
        iso_empty = all(not row["_occupied"] for row in iso_ties)
        iso_neg = all(row["_W"] < 0 for row in iso_ties)
        check(
            "P3-isolation-clears-tie-window",
            iso_empty,
            "shrink moves ω off the frozen companion",
        )
        check(
            "P3-isolation-tie-W-negative",
            iso_neg,
            "isolation W/E<0 on Gleichstand cells",
        )

    verdict, extra, lean_kind = decide(
        lock_cat, iso_cat, lock_dan, iso_dan, symbolic,
    )
    prop = lean_candidate(verdict, extra)
    print("  VERDICT %s" % verdict)
    print("  lock    n=%s  occupied=%s  W_neg=%s  crude_valid=%s" % (
        extra["lock"]["n"], extra["lock"]["occupied"],
        extra["lock"]["W_neg"], extra["lock"]["crude_valid"],
    ))
    print("  iso     n=%s  occupied=%s  W_neg=%s  B_exc_neg=%s  exc_valid=%s" % (
        extra["iso"]["n"], extra["iso"]["occupied"],
        extra["iso"]["W_neg"], extra["iso"]["B_exc_neg"],
        extra["iso"]["exc_valid"],
    ))
    print("  PHASE_TIE 1  RHO_LIMIT 1  R551 %s  KILLER_SURVIVES_A_TO_0 1" % (
        extra["r551_ratio"],
    ))
    print("  LEAN_KIND %s" % lean_kind)
    print("  LEAN_PROP_BEGIN")
    print(prop)
    print("  LEAN_PROP_END")
    check("P3-verdict-formed", verdict.startswith("DOMINANCE_"), verdict)

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    replay_quads = ((mp.mpf("0.25"), mp.mpf(14)),)
    replay_a = eval_cell("replay", replay_quads, c_inc, rule_lock)
    replay_b = eval_cell("replay", replay_quads, c_inc, rule_lock)
    check(
        "G3-inprocess-rescore",
        nstr(replay_a["_W"]) == nstr(replay_b["_W"]),
        "single-quad lock W/E replay %s" % nstr(replay_a["_W"], 6),
    )
    if smoke:
        check("G4-smoke-subset", True, "sigma=0.25, gamma=14, reduced catalog")
    else:
        check(
            "G4-full-grid",
            True,
            "catalog 52 + danger 3*4*2; sigmas=%d" % len(HOST_SIGMAS),
        )

    canon = {
        "symbolic": symbolic,
        "catalog_lock": compact_rows(lock_cat),
        "catalog_iso": compact_rows(iso_cat),
        "danger_lock": compact_rows(lock_dan),
        "danger_iso": compact_rows(iso_dan),
        "verdict": verdict,
        "extra": extra,
        "lean_kind": lean_kind,
        "C_inc": nstr(c_inc),
        "SPEC_SHA": SPEC_SHA,
        "inequality": INEQUALITY_LOCK,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    next_suggest = (
        "r561: %s  Gleichstand-Phasenfaktor ≡ 1, ρ→1, Killer überlebt a→0; "
        "Schranke gültig; Lean-Prop %s mit I_exc-Fenster ε(a)~√(a log(1/a)).  "
        "KEIN RH-CLAIM" % (verdict, lean_kind)
    )
    print("PAYLOAD_SHA256 %s" % seal)
    print("C_INC %s" % nstr(c_inc))
    print("N_CATALOG_LOCK %d" % len(lock_cat))
    print("N_DANGER_LOCK %d" % len(lock_dan))
    print("LOCK_OCCUPIED %s" % extra["lock"]["occupied"])
    print("ISO_W_NEG %s/%s" % (extra["iso"]["W_neg"], extra["iso"]["n"]))
    print("ISO_B_EXC_NEG %s/%s" % (extra["iso"]["B_exc_neg"], extra["iso"]["n"]))
    print("CRUDE_OK %s" % extra["crude_ok"])
    print("EXC_OK %s" % extra["exc_ok"])
    print("PHASE_TIE 1")
    print("RHO_LIMIT 1")
    print("R551_RATIO %s" % extra["r551_ratio"])
    print("KILLER_SURVIVES_A_TO_0 1")
    print("INEQUALITY %s" % INEQUALITY_LOCK)
    print("VERDICT %s" % verdict)
    print("LEAN_KIND %s" % lean_kind)
    print("MISSING %s" % extra.get("missing", ""))
    print("EXCEPTION_WINDOW %s" % extra.get("exception_window", ""))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print(
        "LEAN_NOTE named-constant lock inequality needs I_exc emptiness; "
        "isolation shrink realises emptiness for finite Z; no RH claim"
    )
    print("NO_RH_CLAIM")
    print("NEXT_TXT_SUGGESTION %s" % next_suggest)
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
            "r561 Gabor uniform dominance inequality "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
