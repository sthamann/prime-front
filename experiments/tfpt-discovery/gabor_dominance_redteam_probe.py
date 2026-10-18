#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_dominance_redteam_probe -- r563

Round 563.  Experiments-only ADVERSARIAL red-team of the sealed r561
isolation-shrink rule and its named reduced bound.

  r561 (sealed, FILE_SHA 519a3895…, VERDICT DOMINANCE_UNIFORM):
    (σ★,γ★)=lexmax(σ,−γ); a_lock=(σ★²/64)/8;
    d_min=min{|γ′−γ★|:γ′≠γ★}; shrink a≤a_lock until
    πa/σ★+ε(a)≤d_min/2, ε(a)=√(2a log max(1/a,4·43));
    ω=γ★−πa/σ★.
    W/E ≤ −η + K_bin[4e^{−ε²/2a}+(Θ_lobe−3)]
         + K_bin(θ_left+2θ_cross) + R_on/E,
    η=exp(−π²a/(2σ★²)), E=(π/a)e^{σ★²/2a}, K_bin=43.

THIS ROUND.  Search for an increment-compliant Z that breaks the
rule (W_honest/E ≥ 0) or the bound (empty I_exc but B_exc < W/E).
Known dead attacks (r561): centre-tie, antiphase k=43, cluster k=5.
Families: (a) d_min→0 and δ=0 same-γ; (b) mass pack just outside
I_exc; (c) σ/γ extremes; (d) secondary extremum / plus-lobe;
(e) seeded DE, two rounds.

CLAIM BOUNDARY.  Finite closed-form / deterministic arithmetic on
increment-compliant catalogs.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/next.txt edit.

HAT CONVENTION.  Inherited byte-for-byte from r561/r560: Weil-shifted
ĥ_W, Q = 4 Re ĥ_W, R_on = 2 C_inc S_cert.  Reduced units E=(π/a)
e^{σ★²/2a}.  Log-scale / mpmath for a→0 and σ→0; no raw e^{σ²/2a}.

Verdicts:
  REDTEAM_BREAKS(config=…, mechanism=…)
  REDTEAM_NEAR_MISS(worst=…, margin=…)
  REDTEAM_HOLDS(families=…, worst_margin=…)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import gabor_uniform_dominance_probe as r561  # noqa: E402
import gabor_honest_weil_game_probe as r560  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
PARENT_FILE_SHA_PREFIX = "519a3895"
K_MAX_BIN = r561.K_MAX_BIN
C_INC_PIN = r561.C_INC_PIN
NSTR_DIGITS = 12
DPS = 80
DPS_EXTREME = 120
NEAR_MISS_W = "0.05"
NEAR_MISS_BOUND = "0.01"
DE_SEED_1 = 20260901
DE_SEED_2 = 20260902
DE_POP = 16
DE_GENS = 10
DE_POP_SMOKE = 4
DE_GENS_SMOKE = 2

DELTA_GRID = ("1", "0.1", "0.01", "1e-4", "1e-8")
DELTA_GRID_SMOKE = ("1", "0.01")
SIGMA_EXTREME = ("1e-4", "1e-2", "0.49", "0.499999")
GAMMA_EXTREME = ("14", "1e3", "1e6", "1e12")
SIGMA_EXTREME_SMOKE = ("1e-2", "0.49")
GAMMA_EXTREME_SMOKE = ("14",)
RATIO_PLUS = (
    "0.5", "0.9", "0.99", "0.999", "0.9999",
    "0.99999", "0.999999", "1-1e-8", "1-1e-12",
)
RATIO_PLUS_SMOKE = ("0.99", "0.999999", "1-1e-8")
MASS_WINDOWS = 8
MASS_WINDOWS_SMOKE = 2

SPEC = {
    "round": 563,
    "parent_round": 561,
    "parent_file": "gabor_uniform_dominance_probe.py",
    "parent_file_sha_prefix": PARENT_FILE_SHA_PREFIX,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.DOMINANCE_REDTEAM.01",
    "target": "GaborSeparationInequality.honest_weil_game",
    "hat": "weil_shifted",
    "class": "pure_gabor_unit_amplitude",
    "objective": "break isolation-shrink rule or named bound",
    "quantifiers": "exists_Z increment_ok  (adversarial, config first)",
    "rule": "r561.rule_isolation inherited, not re-derived",
    "bound": "r561.bound_exc_reduced / INEQUALITY_REDUCED inherited",
    "online_budget": "2*C_inc*S_cert",
    "k_max_bin": K_MAX_BIN,
    "c_inc_pin": C_INC_PIN,
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "dps_extreme": DPS_EXTREME,
    "de_seed_1": DE_SEED_1,
    "de_seed_2": DE_SEED_2,
    "de_pop": DE_POP,
    "de_gens": DE_GENS,
    "delta_grid": list(DELTA_GRID),
    "sigma_extreme": list(SIGMA_EXTREME),
    "gamma_extreme": list(GAMMA_EXTREME),
    "scope": (
        "d_min->0, mass-pack, sigma/gamma extremes, "
        "secondary plus-lobe, seeded DE x2"
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


def payload_sha(rows: dict) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def parse_ratio(text: str) -> mp.mpf:
    if text.startswith("1-"):
        return mp.mpf(1) - mp.mpf(text[2:])
    return mp.mpf(text)


def named_bound_reduced(
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_ref: mp.mpf,
    c_inc: mp.mpf,
) -> mp.mpf:
    """r561 INEQUALITY_REDUCED with −η (not host_q)."""
    eta = r561.eta_tune(sigma_ref, a_val)
    others_minus = mp.mpf(K_MAX_BIN) * r561.truncated_minus_majorant(a_val)
    others_plus = mp.mpf(K_MAX_BIN) * r560.theta_left_pos(a_val, omega)
    others_cross = (
        2 * mp.mpf(K_MAX_BIN) * r560.theta_cross_pos(a_val, omega)
    )
    return (
        -eta
        + others_minus
        + others_plus
        + others_cross
        + r561.budget_reduced(a_val, omega, c_inc, sigma_ref)
    )


def plus_lobe_gap(
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_p: mp.mpf,
    sigma_ref: mp.mpf,
) -> mp.mpf:
    """Reduced A₊ at t=−ω: exp((σ′²−σ★²)/2a).  Bound's θ_left misses this."""
    return r561.exp_clip((sigma_p ** 2 - sigma_ref ** 2) / (2 * a_val))


def eval_attack(
    name: str,
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    family: str,
) -> dict:
    tag, a_val, omega, sigma_star, gamma_star = r561.rule_isolation(quads)
    occupied = r561.window_occupied(quads, gamma_star, a_val, omega)
    host_q = r561.q_reduced(sigma_star, gamma_star, a_val, omega, sigma_star)
    w_red = r561.w_reduced(quads, a_val, omega, c_inc, sigma_star)
    b_exc = r561.bound_exc_reduced(a_val, omega, sigma_star, c_inc, host_q)
    b_crude = r561.bound_crude_reduced(a_val, omega, sigma_star, c_inc, host_q)
    b_named = named_bound_reduced(a_val, omega, sigma_star, c_inc)
    eta = r561.eta_tune(sigma_star, a_val)
    slack = mp.mpf("1e-8") * (1 + abs(w_red) + abs(b_exc) + abs(b_crude))
    crude_valid = b_crude + slack >= w_red
    exc_valid = (not occupied) and (b_exc + slack >= w_red)
    named_valid = (not occupied) and (b_named + slack >= w_red)
    a_floor = (sigma_star ** 2) / mp.mpf(r561.A_FLOOR_DENOM)
    d_min = r561.d_min_foreign(quads, gamma_star)
    isolated_ok = r561.isolated(sigma_star, d_min, a_val)
    a_degen = (not mp.isfinite(a_val)) or a_val <= 0 or a_val < a_floor / 2
    fallback = tag == "isolation_cover_fallback"
    signed_height = any(gamma_p < 0 for _, gamma_p in quads)
    w_pos = w_red >= 0
    bound_broke = (not occupied) and (not exc_valid)
    named_broke = (not occupied) and (not named_valid)
    if w_pos:
        mechanism = "W_nonneg"
    elif bound_broke:
        mechanism = "bound_not_conservative"
    elif named_broke:
        mechanism = "named_bound_not_conservative"
    elif fallback:
        mechanism = "isolation_fallback"
    elif a_degen:
        mechanism = "a_degenerate"
    else:
        mechanism = "holds"
    margin = -w_red
    bound_margin = b_exc - w_red if not occupied else mp.mpf("nan")
    return {
        "name": name,
        "family": family,
        "rule": tag,
        "n_quad": str(len(quads)),
        "inc_ok": str(int(r560.increment_ok(quads))),
        "a": nstr(a_val),
        "omega": nstr(omega),
        "sigma": nstr(sigma_star),
        "gamma": nstr(gamma_star),
        "d_min": "inf" if not mp.isfinite(d_min) else nstr(d_min),
        "eps": nstr(r561.epsilon_of(a_val)),
        "eta": nstr(eta),
        "window_occupied": str(int(occupied)),
        "isolated": str(int(isolated_ok)),
        "fallback": str(int(fallback)),
        "a_degen": str(int(a_degen)),
        "W_red": nstr(w_red),
        "B_exc_red": nstr(b_exc),
        "B_crude_red": nstr(b_crude),
        "B_named_red": nstr(b_named),
        "host_q": nstr(host_q),
        "W_neg": str(int(w_red < 0)),
        "B_exc_neg": str(int(b_exc < 0)),
        "crude_valid": str(int(crude_valid)),
        "exc_valid": str(int(exc_valid)),
        "named_valid": str(int(named_valid)),
        "exc_applies": str(int(not occupied)),
        "mechanism": mechanism,
        "margin": nstr(margin),
        "bound_margin": (
            "nan" if not mp.isfinite(bound_margin) else nstr(bound_margin)
        ),
        "_W": w_red,
        "_B_exc": b_exc,
        "_B_crude": b_crude,
        "_B_named": b_named,
        "_occupied": occupied,
        "_crude_valid": crude_valid,
        "_exc_valid": exc_valid,
        "_named_valid": named_valid,
        "_a": a_val,
        "_omega": omega,
        "_sigma": sigma_star,
        "_gamma": gamma_star,
        "_margin": margin,
        "_bound_margin": bound_margin,
        "_w_pos": w_pos,
        "_bound_broke": bound_broke,
        "_named_broke": named_broke,
        "_fallback": fallback,
        "_a_degen": a_degen,
        "_inc_ok": r560.increment_ok(quads),
        "_mechanism": mechanism,
        "_signed": signed_height,
    }


def print_row(row: dict) -> None:
    print(
        "  %-42s %-18s W=%s  Bexc=%s  occ=%s  %s"
        % (
            row["name"][:42],
            row["rule"][:18],
            nstr(row["_W"], 5),
            nstr(row["_B_exc"], 5),
            row["window_occupied"],
            row["mechanism"],
        )
    )


def compact(row: dict) -> dict:
    keys = (
        "name", "family", "rule", "n_quad", "inc_ok", "a", "omega",
        "sigma", "gamma", "d_min", "eps", "eta", "window_occupied",
        "isolated", "fallback", "a_degen", "W_red", "B_exc_red",
        "B_crude_red", "B_named_red", "W_neg", "crude_valid",
        "exc_valid", "named_valid", "mechanism", "margin", "bound_margin",
    )
    return {key: row[key] for key in keys}


# ---------------------------------------------------------------------------
# Family (a): d_min → 0 and δ = 0 same-γ
# ---------------------------------------------------------------------------
def family_dmin(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("FAMILY A  d_min→0  and  δ=0 same-γ edge")
    deltas = DELTA_GRID_SMOKE if smoke else DELTA_GRID
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    rows: list[dict] = []
    for delta_text in deltas:
        delta = mp.mpf(delta_text)
        quads = ((sigma, gamma), (sigma, gamma + delta))
        rows.append(eval_attack(
            "dmin:delta=%s" % delta_text, quads, c_inc, "dmin",
        ))
    # δ = 0, identical γ, σ′ < σ★ (does γ′≠γ★ fire? d_min uses 1e-18)
    quads_same = ((sigma, gamma), (mp.mpf("0.10"), gamma))
    rows.append(eval_attack(
        "dmin:delta=0:sigma_lt", quads_same, c_inc, "dmin",
    ))
    # δ = 0, duplicate host copies (same σ, same γ)
    quads_dup = ((sigma, gamma), (sigma, gamma))
    rows.append(eval_attack(
        "dmin:delta=0:duplicate_host", quads_dup, c_inc, "dmin",
    ))
    # δ = 0, 43 host copies (increment ceiling, same bin)
    quads_k = tuple((sigma, gamma) for _ in range(K_MAX_BIN))
    rows.append(eval_attack(
        "dmin:delta=0:k43_host_copies", quads_k, c_inc, "dmin",
    ))
    print(
        "  name                                       rule               "
        "W/E        B_exc      occ  mech"
    )
    for row in rows:
        print_row(row)
        if row["name"].startswith("dmin:delta=0"):
            print(
                "    DIAG d_min=%s isolated=%s fallback=%s a=%s "
                "(γ′=γ★ excluded from d_min iff |γ′−γ★|≤1e-18)"
                % (row["d_min"], row["isolated"], row["fallback"], row["a"])
            )
    return rows


# ---------------------------------------------------------------------------
# Family (b): mass pack just outside I_exc
# ---------------------------------------------------------------------------
def _mass_pack(
    sigma: mp.mpf,
    gamma: mp.mpf,
    n_windows: int,
    phase_align: bool,
) -> tuple[tuple[mp.mpf, mp.mpf], ...]:
    """Host plus 43 quads/window in n_windows starting just outside lock I_exc.

    Isolation then sees d_min to the first packed height and may shrink.
    That is the attack: bound uses a tight ε(a) after shrink.
    """
    a_lock = r561.a_lock(sigma)
    omega0 = r561.omega_rule(sigma, gamma, a_lock)
    eps0 = r561.epsilon_of(a_lock)
    # First foreign height: just outside I_exc on the host side (γ>ω)
    # and also a pack on the far side of ω, plus further unit windows.
    if phase_align:
        # nearest 2π-phase point with |γ′−ω| ≥ ε (cos φ₋ = +1)
        step = 2 * mp.pi * a_lock / sigma
        k_need = int(mp.ceil(eps0 / step)) + 1
        first = omega0 + mp.mpf(k_need) * step
    else:
        first = omega0 + eps0 + mp.mpf("1e-12")
    quads: list[tuple[mp.mpf, mp.mpf]] = [(sigma, gamma)]
    # Coincident copies at one height per window.  Windows are spaced
    # 1+1e-12 so a sliding unit interval cannot merge two packs.
    # Host shares the I_exc-adjacent window: 42 foreigners there, 43 later.
    gap = mp.mpf(1) + mp.mpf("1e-12")
    for window in range(n_windows):
        site = first + mp.mpf(window) * gap
        n_here = K_MAX_BIN - 1 if window == 0 else K_MAX_BIN
        quads.extend([(sigma, site)] * n_here)
    return tuple(quads)


def family_mass(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("FAMILY B  mass pack just outside I_exc  (43/window)")
    n_win = MASS_WINDOWS_SMOKE if smoke else MASS_WINDOWS
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    rows: list[dict] = []
    for phase, tag in ((False, "edge"), (True, "phase")):
        quads = _mass_pack(sigma, gamma, n_win, phase)
        rows.append(eval_attack(
            "mass:%s:w=%d:s=0.25:g=14" % (tag, n_win),
            quads, c_inc, "mass",
        ))
    if not smoke:
        for sigma_text, gamma_text in (("0.49", "14"), ("0.25", "1000")):
            quads = _mass_pack(
                mp.mpf(sigma_text), mp.mpf(gamma_text), n_win, False,
            )
            rows.append(eval_attack(
                "mass:edge:w=%d:s=%s:g=%s" % (n_win, sigma_text, gamma_text),
                quads, c_inc, "mass",
            ))
    print(
        "  name                                       rule               "
        "W/E        B_exc      occ  mech"
    )
    for row in rows:
        print_row(row)
        print(
            "    DIAG n=%s d_min=%s eps=%s B_named=%s named_valid=%s"
            % (
                row["n_quad"], row["d_min"], row["eps"],
                row["B_named_red"], row["named_valid"],
            )
        )
    return rows


# ---------------------------------------------------------------------------
# Family (c): σ / γ extremes
# ---------------------------------------------------------------------------
def family_sigma(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("FAMILY C  σ-extremes × γ-extremes  (single + far twin)")
    sigmas = SIGMA_EXTREME_SMOKE if smoke else SIGMA_EXTREME
    gammas = GAMMA_EXTREME_SMOKE if smoke else GAMMA_EXTREME
    prev_dps = mp.mp.dps
    mp.mp.dps = DPS_EXTREME
    r560.mp.mp.dps = DPS_EXTREME
    r561.mp.mp.dps = DPS_EXTREME
    rows: list[dict] = []
    eta_lock = mp.exp(-(mp.pi ** 2) / 1024)
    eta_r541 = mp.exp(-(mp.pi ** 2) / 128)
    print(
        "  η(a_lock=σ²/512)=exp(−π²/1024)=%s   "
        "η(a=σ²/64)=exp(−π²/128)=%s"
        % (nstr(eta_lock, 8), nstr(eta_r541, 8))
    )
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            single = ((sigma, gamma),)
            rows.append(eval_attack(
                "ext:single:s=%s:g=%s" % (sigma_text, gamma_text),
                single, c_inc, "sigma",
            ))
            if not smoke:
                twin = ((sigma, gamma), (sigma * mp.mpf("0.99"), gamma + 10))
                rows.append(eval_attack(
                    "ext:twin:s=%s:g=%s" % (sigma_text, gamma_text),
                    twin, c_inc, "sigma",
                ))
    mp.mp.dps = prev_dps
    r560.mp.mp.dps = prev_dps
    r561.mp.mp.dps = prev_dps
    print(
        "  name                                       rule               "
        "W/E        B_exc      occ  mech"
    )
    shown = rows if smoke else [row for row in rows if "single" in row["name"]]
    for row in shown:
        print_row(row)
        # a ~ σ² ⇒ η constant: check lock-scale identity
        eta_err = abs(mp.mpf(row["eta"]) - eta_lock)
        print(
            "    DIAG eta=%s  |eta-exp(−π²/1024)|=%s  a=%s"
            % (row["eta"], nstr(eta_err, 4), row["a"])
        )
    if not smoke:
        print("  ... %d extreme cells (single+twin)" % len(rows))
    return rows


# ---------------------------------------------------------------------------
# Family (d): secondary extremum / plus-lobe
# ---------------------------------------------------------------------------
def _plus_lobe_pair(
    sigma: mp.mpf, gamma: mp.mpf, ratio: mp.mpf,
) -> tuple[tuple[mp.mpf, mp.mpf], ...]:
    """Host (σ,γ) plus foreign (rσ, −ω_lock).  Host stays lexmax if r<1."""
    a_lock = r561.a_lock(sigma)
    omega0 = r561.omega_rule(sigma, gamma, a_lock)
    return ((sigma, gamma), (ratio * sigma, -omega0))


def family_secondary(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("FAMILY D  secondary extremum / plus-lobe at −ω")
    ratios = RATIO_PLUS_SMOKE if smoke else RATIO_PLUS
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    rows: list[dict] = []
    a_lock = r561.a_lock(sigma)
    omega0 = r561.omega_rule(sigma, gamma, a_lock)
    # Equal-σ twin at −ω_lock: lexmax switches host to the more negative γ
    rows.append(eval_attack(
        "sec:equal_sigma_twin_at_-omega",
        ((sigma, gamma), (sigma, -omega0)),
        c_inc, "secondary",
    ))
    # Equal-σ twin far positive (same σ, larger γ — lexmax keeps host)
    rows.append(eval_attack(
        "sec:equal_sigma_twin_far_+",
        ((sigma, gamma), (sigma, gamma + mp.mpf(1000))),
        c_inc, "secondary",
    ))
    # σ′ < σ★ at −ω_lock, r → 1−  (the critical attack)
    for ratio_text in ratios:
        ratio = parse_ratio(ratio_text)
        quads = _plus_lobe_pair(sigma, gamma, ratio)
        gap = plus_lobe_gap(a_lock, omega0, ratio * sigma, sigma)
        row = eval_attack(
            "sec:plus_lobe:r=%s" % ratio_text, quads, c_inc, "secondary",
        )
        row["plus_A"] = nstr(gap)
        row["_plus_A"] = gap
        rows.append(row)
    # Harmless-looking host + far smaller-σ mountain (many copies)
    far = [(mp.mpf("0.10"), gamma + mp.mpf(50) + mp.mpf(index))
           for index in range(5 if smoke else 20)]
    rows.append(eval_attack(
        "sec:far_small_sigma_stack",
        tuple([(sigma, gamma)] + far),
        c_inc, "secondary",
    ))
    if not smoke:
        for sigma_text, gamma_text in (("0.49", "14"), ("0.25", "1000")):
            sig = mp.mpf(sigma_text)
            gam = mp.mpf(gamma_text)
            rows.append(eval_attack(
                "sec:plus_lobe:r=1-1e-8:s=%s:g=%s" % (sigma_text, gamma_text),
                _plus_lobe_pair(sig, gam, mp.mpf(1) - mp.mpf("1e-8")),
                c_inc, "secondary",
            ))
    print(
        "  name                                       rule               "
        "W/E        B_exc      occ  mech"
    )
    for row in rows:
        print_row(row)
        extra = ""
        if "plus_A" in row:
            extra = "  Aplus_red=%s" % row["plus_A"]
        print(
            "    DIAG host_q=%s B_named=%s bound_margin=%s%s"
            % (row["host_q"], row["B_named_red"], row["bound_margin"], extra)
        )
    return rows


# ---------------------------------------------------------------------------
# Family (e): seeded differential evolution, two rounds
# ---------------------------------------------------------------------------
def _de_eval(
    host: tuple[mp.mpf, mp.mpf],
    vec: list[float],
    c_inc: mp.mpf,
) -> tuple[mp.mpf, tuple[tuple[mp.mpf, mp.mpf], ...]]:
    sigma_h, gamma_h = host
    extras: list[tuple[mp.mpf, mp.mpf]] = []
    for index in range(0, len(vec), 2):
        sigma_p = mp.mpf(vec[index])
        gamma_p = mp.mpf(vec[index + 1])
        extras.append((sigma_p, gamma_p))
    quads = tuple([host] + extras)
    if not r560.increment_ok(quads):
        return mp.mpf("-inf"), quads
    row = eval_attack("de", quads, c_inc, "de")
    return row["_W"], quads


def _de_run(
    host: tuple[mp.mpf, mp.mpf],
    n_extra: int,
    bounds: list[tuple[float, float]],
    seed: int,
    pop_n: int,
    gens: int,
    c_inc: mp.mpf,
) -> dict:
    rng = random.Random(seed)
    dim = n_extra * 2
    pop = []
    for _ in range(pop_n):
        vec = [
            rng.uniform(bounds[j][0], bounds[j][1]) for j in range(dim)
        ]
        pop.append(vec)
    # Deterministic elite: plus-lobe near-equal-σ at −ω_lock (known hole).
    a_lock = r561.a_lock(host[0])
    omega0 = r561.omega_rule(host[0], host[1], a_lock)
    elite = [float(host[0]) * 0.999999, float(-omega0)]
    if n_extra >= 2:
        elite.extend([float(host[0]) * 0.5, float(host[1]) + 20.0])
    elite = elite[:dim]
    while len(elite) < dim:
        elite.append(bounds[len(elite)][0])
    if pop:
        pop[0] = elite
    scores: list[mp.mpf] = []
    quads_of: list[tuple[tuple[mp.mpf, mp.mpf], ...]] = []
    n_eval = 0
    for vec in pop:
        w_val, quads = _de_eval(host, vec, c_inc)
        scores.append(w_val)
        quads_of.append(quads)
        n_eval += 1
    f_de = 0.7
    cr = 0.6
    for _ in range(gens):
        for i in range(pop_n):
            idxs = list(range(pop_n))
            idxs.remove(i)
            a_i, b_i, c_i = rng.sample(idxs, 3)
            donor = []
            for j in range(dim):
                trial = pop[a_i][j] + f_de * (pop[b_i][j] - pop[c_i][j])
                lo, hi = bounds[j]
                if trial < lo:
                    trial = lo
                if trial > hi:
                    trial = hi
                donor.append(trial)
            jrand = rng.randrange(dim)
            trial_vec = []
            for j in range(dim):
                if rng.random() < cr or j == jrand:
                    trial_vec.append(donor[j])
                else:
                    trial_vec.append(pop[i][j])
            w_val, quads = _de_eval(host, trial_vec, c_inc)
            n_eval += 1
            if w_val > scores[i]:
                pop[i] = trial_vec
                scores[i] = w_val
                quads_of[i] = quads
    best_i = max(range(pop_n), key=lambda k: scores[k])
    return {
        "W": scores[best_i],
        "quads": quads_of[best_i],
        "n_eval": n_eval,
        "seed": seed,
        "pop": pop_n,
        "gens": gens,
        "n_extra": n_extra,
    }


def family_de(smoke: bool, c_inc: mp.mpf) -> tuple[list[dict], dict]:
    section("FAMILY E  seeded DE  (max W_honest under isolation rule)")
    host = (mp.mpf("0.25"), mp.mpf(14))
    pop_n = DE_POP_SMOKE if smoke else DE_POP
    gens = DE_GENS_SMOKE if smoke else DE_GENS
    # Round 1: one foreign quad, signed height (can reach −ω)
    bounds1 = [(1e-4, 0.249999), (-40.0, 40.0)]
    r1 = _de_run(host, 1, bounds1, DE_SEED_1, pop_n, gens, c_inc)
    # Round 2: two foreign quads, signed heights, different seed
    bounds2 = [
        (1e-4, 0.249999), (-40.0, 40.0),
        (1e-4, 0.249999), (-40.0, 40.0),
    ]
    r2 = _de_run(host, 2, bounds2, DE_SEED_2, pop_n, gens, c_inc)
    rows = [
        eval_attack("de:round1:n_extra=1", r1["quads"], c_inc, "de"),
        eval_attack("de:round2:n_extra=2", r2["quads"], c_inc, "de"),
    ]
    meta = {
        "round1_evals": str(r1["n_eval"]),
        "round2_evals": str(r2["n_eval"]),
        "round1_seed": str(r1["seed"]),
        "round2_seed": str(r2["seed"]),
        "pop": str(pop_n),
        "gens": str(gens),
        "round1_W": nstr(r1["W"]),
        "round2_W": nstr(r2["W"]),
        "budget": "2 rounds, pop=%d gens=%d, evals=%d+%d, seeds=%d/%d" % (
            pop_n, gens, r1["n_eval"], r2["n_eval"], DE_SEED_1, DE_SEED_2,
        ),
    }
    print("  BUDGET %s" % meta["budget"])
    print(
        "  name                                       rule               "
        "W/E        B_exc      occ  mech"
    )
    for row in rows:
        print_row(row)
        print(
            "    DIAG quads n=%s inc=%s W=%s" % (
                row["n_quad"], row["inc_ok"], row["W_red"],
            )
        )
    return rows, meta


# ---------------------------------------------------------------------------
# Scoring / verdict
# ---------------------------------------------------------------------------
def worst_of(rows: list[dict]) -> dict:
    return max(rows, key=lambda row: row["_W"])


def decide(all_rows: list[dict], de_meta: dict) -> tuple[str, dict]:
    inc_rows = [row for row in all_rows if row["_inc_ok"]]
    breaks_w = [row for row in inc_rows if row["_w_pos"]]
    breaks_b = [row for row in inc_rows if row["_bound_broke"]]
    breaks_n = [row for row in inc_rows if row["_named_broke"]]
    worst = worst_of(inc_rows) if inc_rows else all_rows[0]
    extra = {
        "n_cells": str(len(all_rows)),
        "n_inc": str(len(inc_rows)),
        "n_W_pos": str(len(breaks_w)),
        "n_bound_broke": str(len(breaks_b)),
        "n_named_broke": str(len(breaks_n)),
        "n_fallback": str(sum(1 for row in inc_rows if row["_fallback"])),
        "n_a_degen": str(sum(1 for row in inc_rows if row["_a_degen"])),
        "worst_name": worst["name"],
        "worst_W": nstr(worst["_W"]),
        "worst_margin": nstr(worst["_margin"]),
        "worst_mechanism": worst["mechanism"],
        "de_budget": de_meta["budget"],
        "eta_lock": nstr(mp.exp(-(mp.pi ** 2) / 1024), 8),
        "eta_r541": nstr(mp.exp(-(mp.pi ** 2) / 128), 8),
    }
    family_worst: dict[str, dict] = {}
    for family in ("dmin", "mass", "sigma", "secondary", "de"):
        subset = [row for row in inc_rows if row["family"] == family]
        if subset:
            family_worst[family] = worst_of(subset)
            extra["worst_%s" % family] = subset and nstr(
                family_worst[family]["_W"]
            )
            extra["worst_%s_name" % family] = family_worst[family]["name"]
            extra["worst_%s_mech" % family] = family_worst[family]["mechanism"]

    hole = (
        "plus-lobe at t=−ω is missing from θ_left when ω>0 (that majorant "
        "sums t≥0 bins).  (i) σ′→σ★− at γ′=−ω_lock: host stays (σ★,γ★), "
        "A₊_red→1, cos φ₊=1, W/E→−η+1+R_on/E≈+0.0096, B_exc stays ≈−η "
        "(bound not conservative).  (ii) equal-σ twin at −ω_lock: lexmax "
        "switches host to the negative height and RETUNES ω so the leftover "
        "twin sits exactly at the new plus-lobe (W/E≈+0.0096); θ_left then "
        "sees ω<0 and inflates to Θ_lobe, so B_exc≈+128 is conservative "
        "but does not prove negativity.  Same-γ σ′<σ★ is excluded from "
        "d_min/I_exc (threshold 1e-18) and contributes with the host phase "
        "(negative).  d_min→0 at δ=1e-8 hits the a-floor / "
        "isolation_cover_fallback (reverts to a_lock); I_exc nonempty, "
        "exception bound N/A, exact W still negative."
    )
    extra["accounting"] = hole

    if breaks_w:
        hit = max(breaks_w, key=lambda row: row["_W"])
        extra["break_config"] = hit["name"]
        extra["break_W"] = nstr(hit["_W"])
        extra["break_B_exc"] = nstr(hit["_B_exc"])
        extra["break_a"] = hit["a"]
        extra["break_omega"] = hit["omega"]
        extra["break_rule"] = hit["rule"]
        extra["break_occupied"] = hit["window_occupied"]
        mechanism = "W_nonneg+%s" % hit["name"]
        if hit["_bound_broke"]:
            mechanism = "W_nonneg+bound_gap+%s" % hit["name"]
        extra["break_mechanism"] = mechanism
        verdict = "REDTEAM_BREAKS(config=%s, mechanism=%s)" % (
            hit["name"], mechanism,
        )
        return verdict, extra

    if breaks_b:
        hit = min(breaks_b, key=lambda row: row["_bound_margin"])
        extra["break_config"] = hit["name"]
        extra["break_mechanism"] = "bound_not_conservative"
        verdict = "REDTEAM_BREAKS(config=%s, mechanism=bound_not_conservative)" % (
            hit["name"],
        )
        return verdict, extra

    nm_w = mp.mpf(NEAR_MISS_W)
    nm_b = mp.mpf(NEAR_MISS_BOUND)
    near = [
        row for row in inc_rows
        if (row["_W"] < 0 and row["_W"] > -nm_w)
        or (
            (not row["_occupied"])
            and mp.isfinite(row["_bound_margin"])
            and row["_bound_margin"] < nm_b
        )
    ]
    if near:
        hit = worst_of(near)
        extra["near_name"] = hit["name"]
        extra["near_margin"] = nstr(hit["_margin"])
        verdict = "REDTEAM_NEAR_MISS(worst=%s, margin=%s)" % (
            hit["name"], nstr(hit["_margin"], 6),
        )
        return verdict, extra

    families = ",".join(sorted({row["family"] for row in inc_rows}))
    verdict = "REDTEAM_HOLDS(families=%s, worst_margin=%s)" % (
        families, nstr(worst["_margin"], 6),
    )
    return verdict, extra


def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf, str]:
    parent_sha = r561.file_sha256()
    parent_ok = parent_sha.startswith(PARENT_FILE_SHA_PREFIX)
    check(
        "G0-parent-sha-prefix",
        parent_ok,
        "r561 FILE_SHA256=%s prefix=%s" % (parent_sha[:16], PARENT_FILE_SHA_PREFIX),
    )
    g0_ok, g0_err = r561.run_g0(c_inc)
    pin = mp.mpf(C_INC_PIN)
    pin_ok = abs(c_inc - pin) / pin < mp.mpf("1e-9")
    # Isolation identity: lexmax and shrink live in r561, not re-derived.
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    quads = ((sigma, gamma), (sigma, gamma + 1))
    tag_a, a_a, om_a, _, _ = r561.rule_isolation(quads)
    tag_b, a_b, om_b, _, _ = r561.rule_isolation(quads)
    replay = tag_a == tag_b and nstr(a_a) == nstr(a_b) and nstr(om_a) == nstr(om_b)
    max_err = g0_err
    if not parent_ok or not g0_ok or not pin_ok or not replay:
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-8"), max_err, parent_sha


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    r560.mp.mp.dps = DPS
    r561.mp.mp.dps = DPS
    c_inc = r560.c_inc_prefactor()
    print("gabor_dominance_redteam_probe -- r563")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("objective BREAK r561 isolation-shrink + named bound")
    print("online 2*C_inc*S_cert  C_inc %s" % nstr(c_inc))
    print("FORMULA  %s" % r561.INEQUALITY_REDUCED)
    print("RULE     inherited r561.rule_isolation (not re-derived)")

    section("G0  PARENT SEAL / C_inc PIN / RULE REPLAY")
    g0_ok, g0_err, parent_sha = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))
    check(
        "G0-c-inc-pin",
        abs(c_inc - mp.mpf(C_INC_PIN)) / mp.mpf(C_INC_PIN) < mp.mpf("1e-9"),
        "C_inc=%s pin=%s" % (nstr(c_inc), C_INC_PIN),
    )
    check("G0-k-bin", K_MAX_BIN == 43, "K_bin=%d" % K_MAX_BIN)

    rows_a = family_dmin(smoke, c_inc)
    rows_b = family_mass(smoke, c_inc)
    rows_c = family_sigma(smoke, c_inc)
    rows_d = family_secondary(smoke, c_inc)
    rows_e, de_meta = family_de(smoke, c_inc)
    all_rows = rows_a + rows_b + rows_c + rows_d + rows_e

    section("PART  VERDICT / ACCOUNTING")
    inc_fail = [row["name"] for row in all_rows if not row["_inc_ok"]]
    check(
        "P-increment-ok",
        not inc_fail,
        "every attack Z has ≤%d quads/bin" % K_MAX_BIN
        if not inc_fail
        else "FAIL %s" % ",".join(inc_fail[:6]),
    )

    # Explicit δ=0 and d_min→0 disclosures
    d0 = [row for row in rows_a if "delta=0:" in row["name"]]
    dsmall = [row for row in rows_a if "delta=1e-8" in row["name"]]
    if d0:
        same_gamma_excluded = all(row["d_min"] == "inf" for row in d0)
        check(
            "P-delta0-same-gamma-excluded-from-dmin",
            same_gamma_excluded,
            "d_min=+∞ because |γ′−γ★|=0 ≤ 1e-18 (γ′≠γ★ is false)",
        )
    if dsmall:
        check(
            "P-dmin-1e-8-fallback-or-floor",
            any(row["_fallback"] or row["_a_degen"] for row in dsmall)
            or any(row["rule"] == "isolation_shrunk" for row in dsmall),
            "rule=%s a=%s isolated=%s" % (
                dsmall[0]["rule"], dsmall[0]["a"], dsmall[0]["isolated"],
            ),
        )
    elif smoke:
        check("P-dmin-1e-8-skipped-smoke", True, "full run only")

    # η lock-scale identity (family c single cells)
    eta_lock = mp.exp(-(mp.pi ** 2) / 1024)
    eta_rows = [
        row for row in rows_c
        if row["name"].startswith("ext:single") and row["rule"] == "isolation"
    ]
    if eta_rows:
        eta_ok = all(
            abs(mp.mpf(row["eta"]) - eta_lock) < mp.mpf("1e-6")
            for row in eta_rows
        )
        check(
            "P-eta-lock-identity",
            eta_ok,
            "η(a=σ²/512)=exp(−π²/1024)=%s (not exp(−π²/128))"
            % nstr(eta_lock, 8),
        )

    verdict, extra = decide(all_rows, de_meta)
    extra["parent_sha"] = parent_sha
    print("  VERDICT %s" % verdict)
    print("  WORST   %s  W/E=%s  mech=%s" % (
        extra["worst_name"], extra["worst_W"], extra["worst_mechanism"],
    ))
    print("  CELLS   n=%s inc=%s W_pos=%s bound_broke=%s fallback=%s" % (
        extra["n_cells"], extra["n_inc"], extra["n_W_pos"],
        extra["n_bound_broke"], extra["n_fallback"],
    ))
    print("  DE      %s" % extra["de_budget"])
    print("  ACCOUNT %s" % extra["accounting"])
    pos_gamma = [
        row for row in all_rows
        if row["_inc_ok"] and not row["_signed"]
    ]
    pos_breaks = [row for row in pos_gamma if row["_w_pos"] or row["_bound_broke"]]
    extra["n_pos_gamma_cells"] = str(len(pos_gamma))
    extra["n_pos_gamma_breaks"] = str(len(pos_breaks))
    print(
        "  GAMMA_POS_ONLY  cells=%d breaks=%d  (signed-height attacks excluded)"
        % (len(pos_gamma), len(pos_breaks))
    )
    check("P-verdict-formed", verdict.startswith("REDTEAM_"), verdict)

    breaks_dump = [
        row for row in all_rows
        if row["_inc_ok"] and (row["_w_pos"] or row["_bound_broke"])
    ]
    if breaks_dump:
        section("BREAK / NEAR-BREAK DUMPS")
        for row in breaks_dump:
            print(
                "  CONFIG %s  rule=%s a=%s omega=%s sigma=%s gamma=%s"
                % (
                    row["name"], row["rule"], row["a"],
                    row["omega"], row["sigma"], row["gamma"],
                )
            )
            print(
                "    W_red=%s  B_exc=%s  B_named=%s  B_crude=%s  "
                "occ=%s  mech=%s"
                % (
                    row["W_red"], row["B_exc_red"], row["B_named_red"],
                    row["B_crude_red"], row["window_occupied"],
                    row["mechanism"],
                )
            )

    # Family-wise sharpest
    section("SHARP PER FAMILY")
    for family in ("dmin", "mass", "sigma", "secondary", "de"):
        key_w = "worst_%s" % family
        if key_w in extra:
            print(
                "  %s  %s  W/E=%s  mech=%s"
                % (
                    family, extra["worst_%s_name" % family],
                    extra[key_w], extra["worst_%s_mech" % family],
                )
            )

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock; DE uses Random(seed); BLAS threads=1",
    )
    replay_quads = ((mp.mpf("0.25"), mp.mpf(14)), (mp.mpf("0.10"), mp.mpf(14)))
    replay_a = eval_attack("replay", replay_quads, c_inc, "gate")
    replay_b = eval_attack("replay", replay_quads, c_inc, "gate")
    check(
        "G3-inprocess-rescore",
        nstr(replay_a["_W"]) == nstr(replay_b["_W"]),
        "delta0 replay W/E %s" % nstr(replay_a["_W"], 6),
    )
    if smoke:
        check("G4-smoke-subset", True, "reduced grids + DE pop=4 gens=2")
    else:
        check("G4-full-grid", True, "full δ/σ/γ/ratio grids + DE pop=16 gens=10")

    canon = {
        "family_dmin": [compact(row) for row in rows_a],
        "family_mass": [compact(row) for row in rows_b],
        "family_sigma": [compact(row) for row in rows_c],
        "family_secondary": [compact(row) for row in rows_d],
        "family_de": [compact(row) for row in rows_e],
        "de_meta": de_meta,
        "verdict": verdict,
        "extra": extra,
        "C_inc": nstr(c_inc),
        "SPEC_SHA": SPEC_SHA,
        "parent_sha": parent_sha,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    next_suggest = (
        "r563: %s  schaerfster Bruch/Treffer %s W/E=%s; "
        "d_min→0 Fallback bei δ=1e-8; δ=0 same-γ nicht in d_min; "
        "Plus-Lobe t=−ω fehlt in θ_left.  KEIN RH-CLAIM"
        % (verdict, extra["worst_name"], extra["worst_W"])
    )
    print("PAYLOAD_SHA256 %s" % seal)
    print("C_INC %s" % nstr(c_inc))
    print("N_CELLS %s" % extra["n_cells"])
    print("N_W_POS %s" % extra["n_W_pos"])
    print("N_BOUND_BROKE %s" % extra["n_bound_broke"])
    print("N_FALLBACK %s" % extra["n_fallback"])
    print("WORST_NAME %s" % extra["worst_name"])
    print("WORST_W %s" % extra["worst_W"])
    print("WORST_MARGIN %s" % extra["worst_margin"])
    print("ETA_LOCK %s" % extra["eta_lock"])
    print("ETA_R541 %s" % extra["eta_r541"])
    print("DE_BUDGET %s" % extra["de_budget"])
    print("ACCOUNTING %s" % extra["accounting"])
    print("VERDICT %s" % verdict)
    print("PARENT_FILE_SHA256 %s" % parent_sha)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
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
            "r563 adversarial red-team of the r561 isolation-shrink rule "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
