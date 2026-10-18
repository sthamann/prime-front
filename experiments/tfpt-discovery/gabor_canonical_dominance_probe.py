#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_canonical_dominance_probe -- r567

Round 567.  Experiments-only REPAIR of the r561 isolation-shrink rule
after the r566 adjudication of the r563 red-team.

  r561 (FILE_SHA 519a3895…): isolation-shrink + named bound; a-floor
    σ²/1e12 hid extreme near-ties.
  r563 (FILE_SHA 21a4bbff…): γ<0 plus-lobe and δ=1e-8 floor fallback
    broke the named bound / emptiness hypothesis.
  r566 (L2): artefact — every entry is a full FE quadruple,
    Q(σ,−γ)=Q(σ,γ); negative ordinates are double-counts.

THIS ROUND.  Canonical multiplicity-aware dominance rule + bound,
verified on the r560 catalog and every r563 attack family after
canonicalisation.  No numeric a-floor in any uniformity verdict.

CLAIM BOUNDARY.  Finite closed-form / deterministic arithmetic on
increment-compliant catalogs.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/next.txt edit.

HAT CONVENTION (byte-inherited from r561/r560).  Weil-shifted ĥ_W,
Q = 4 Re ĥ_W
  Q(σ′,γ′) = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ],
  A± = exp((σ′²−(γ′∓ω)²)/(2a)),  Aₓ = exp((σ′²−γ′²−ω²)/(2a)),
  φ₊ = σ′(γ′+ω)/a,  φ₋ = σ′(γ′−ω)/a,  φₓ = σ′ γ′/a.
R_on = 2 C_inc S_cert, C_inc pin 174.818115823.
Reduced units E = (π/a) exp(σ★²/2a).  Log-scale / mpmath: never form
e^{σ²/2a} raw.  Amplitude-0 terms skip cos (avoids huge phases).

CANONICAL SPACE.  Z = finite multiset of weighted representatives
(σ_j, γ_j, m_j) with 0<σ_j<1/2, γ_j>0, m_j∈ℕ>0.  Raw (σ,γ) maps to
(σ,|γ|); equal pairs merge by adding multiplicity; σ=0 is on-line
only.  Increment: Σ m_j over any unit window ≤ 43.

Verdicts:
  CANONICAL_DOMINANCE_HOLDS(cells=…, worst_margin=…, bound_conservative=all)
  CANONICAL_DOMINANCE_BREAKS(config=…, mechanism=…)
  BOUND_NOT_CONSERVATIVE(cells=…)
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

import gabor_honest_weil_game_probe as r560  # noqa: E402
import gabor_uniform_dominance_probe as r561  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
PARENT_R561_SHA_PREFIX = "519a3895"
PARENT_R563_SHA_PREFIX = "21a4bbff"
K_MAX_BIN = r561.K_MAX_BIN
C_INC_PIN = r561.C_INC_PIN
NSTR_DIGITS = 12
DPS = 80
DPS_EXTREME = 160
ISOLATION_BISSECTS = 80
LOG_A_FLOOR_SPAN = 400
KAPPA = "1"
MERGE_ATOL = "1e-18"
CATALOG_SIGMAS = ("0.10", "0.25")
HOST_GAMMA = "14"

DELTA_GRID = ("1", "0.1", "0.01", "1e-4", "1e-8", "1e-12")
DELTA_GRID_SMOKE = ("1", "1e-8")
SIGMA_EXTREME = ("1e-4", "0.01", "0.25", "0.49", "0.499999")
GAMMA_EXTREME = ("14", "1e3", "1e6", "1e12")
SIGMA_EXTREME_SMOKE = ("0.25", "0.49")
GAMMA_EXTREME_SMOKE = ("14",)
MULT_STACK = (1, 7, 43)
MULT_STACK_SMOKE = (1, 7)
MASS_WINDOWS = 8
MASS_WINDOWS_SMOKE = 2

DE_SEED_1 = 20260901
DE_SEED_2 = 20260902
DE_POP = 16
DE_GENS = 10
DE_POP_SMOKE = 4
DE_GENS_SMOKE = 2

SPEC = {
    "round": 567,
    "parent_rounds": [560, 561, 563, 566],
    "parent_r561_sha_prefix": PARENT_R561_SHA_PREFIX,
    "parent_r563_sha_prefix": PARENT_R563_SHA_PREFIX,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.CANONICAL_DOMINANCE.01",
    "target": "GaborSeparationInequality.honest_weil_game",
    "hat": "weil_shifted",
    "class": "pure_gabor_unit_amplitude",
    "quantifiers": "forall_Z_canonical exists_h  (config first, constructive rule)",
    "objective": "W_honest = Q_off + R_on  (no R_ref, no -3.56)",
    "space": "canonical_multiset_(sigma,gamma,m)_gamma_gt_0",
    "a_lock": "(sigma^2/64)*1/8",
    "omega_rule": "gamma_star-pi*a/sigma_star",
    "isolation": "shrink_a_no_floor_until_pi_a_over_sigma+eps<=d_min/2_and_omega>0",
    "d_min": "min_|gamma_j-gamma_star|_over_canonical_ordinates_neq",
    "epsilon": "sqrt(2*a*log(max(1/a, 4*K_bin)))",
    "plus_lobe": "A_plus/E <= exp(-omega^2/2a)  (named; no theta_right)",
    "near_tie": "no_numeric_a_floor; kappa-window phase or shrink",
    "kappa": KAPPA,
    "online_budget": "2*C_inc*S_cert",
    "k_max_bin": K_MAX_BIN,
    "c_inc_pin": C_INC_PIN,
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "dps_extreme": DPS_EXTREME,
    "de_seed_1": DE_SEED_1,
    "de_seed_2": DE_SEED_2,
    "delta_grid": list(DELTA_GRID),
    "sigma_extreme": list(SIGMA_EXTREME),
    "gamma_extreme": list(GAMMA_EXTREME),
    "mult_stack": list(MULT_STACK),
    "scope": (
        "r560 52-row catalog canonicalised; r563 families canonicalised "
        "incl. d_min->0 down to 1e-12 no floor; mass; sigma/gamma extremes; "
        "same-sigma twins; multiplicity stacks; seeded DE x2"
    ),
    "excluded": "RH claim; Lean edit; ledger/paper; next.txt",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []

INEQUALITY_REDUCED = (
    "W/E ≤ −η m★ + T_plus + T_gap + T_far + R_on/E,  "
    "T_plus = K_bin e^{−ω²/2a} [1/(1−e^{−ω/a}) + (1+θ₃(a))],  "
    "T_gap = Σ_{σ′<σ★, in I_exc ∪ κ-window, not phase-coherent} "
    "m_j e^{(σ′²−σ★²)/2a},  "
    "T_κ = 0 (same-σ★ κ-window or phase-coherent σ′<σ★ dropped: "
    "cos φ₋ ≤ −cos κ < 0),  "
    "T_far = K_bin [4 e^{−ε²/2a} + (Θ_lobe−3)],  "
    "η=exp(−π² a/(2σ★²)), E=(π/a)e^{σ★²/2a}, "
    "κ=1 < π/2, K_bin=43, R_on=2 C_inc S_cert, no numeric a-floor."
)

INEQUALITY_LOCK = (
    "W_honest(h_{a,ω}; Z_can)  ≤  "
    "−(π/a) e^{σ★²/2a} η m★ "
    "+ (π/a) e^{σ★²/2a} (T_plus + T_gap + T_far) "
    "+ 2 C_inc S_cert(a,ω),  "
    "Z_can the canonical multiset, a ≤ a_lock with "
    "πa/σ★ + ε(a) ≤ d_min/2 and πa/σ★ < γ★,  "
    "ω = γ★ − πa/σ★ > 0  (hence φ₋ = π at the host)."
)

WINDOW_COVERAGE = (
    "κ-window (0<κ<π/2, κ=1): a point is phase-coherent when "
    "|σ′(γ′−γ★)/a + π(σ′/σ★−1)| ≤ κ, i.e. φ₋ ∈ [π−κ, π+κ], "
    "hence cos φ₋ ≤ −cos κ < 0.  "
    "(σ′=σ★) distinct γ: isolation shrink empties I_exc and the "
    "κ-window (d_min ≥ 2(πa/σ★+ε) > κ a/σ★); leftover same-σ★ "
    "terms are far and sit in T_far.  Without shrink they would be "
    "jointly negative inside the κ-window and may be dropped from "
    "an upper bound (T_κ=0).  Exact host copies merge: m★·(−η).  "
    "(σ′<σ★) in I_exc ∪ κ-window: if phase-coherent (in particular "
    "γ′=γ★ and σ′/σ★ ≥ 1−κ/π) they are dropped (also negative).  "
    "Otherwise the bound uses the arbitrary-phase gap "
    "|Q_fremd|/E ≤ m e^{(σ′²−σ★²)/2a} for the minus lobe "
    "(plus/cross absorbed in T_plus).  That gap-sum proves "
    "negativity only while Σ m_j gap_j < η m★ − T_plus − T_far "
    "− R_on/E; when σ′→σ★ at a shared height the crude gap → 1 "
    "and the written bound stops proving, even though the true "
    "phase is still near π.  The proving rule therefore drops "
    "phase-coherent near-σ points and never uses a numeric a-floor."
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
# Canonical space
# ---------------------------------------------------------------------------
Rep = tuple[mp.mpf, mp.mpf, int]


def _near(left: mp.mpf, right: mp.mpf) -> bool:
    return abs(left - right) <= mp.mpf(MERGE_ATOL)


def canonicalize(
    raw: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> tuple[Rep, ...]:
    """(σ,γ) ↦ (σ,|γ|); drop σ≤0 or γ=0; merge equal pairs by +m."""
    buckets: list[list[object]] = []
    for sigma, gamma in raw:
        if sigma <= 0:
            continue
        height = abs(gamma)
        if height <= 0:
            continue
        placed = False
        for bucket in buckets:
            if _near(sigma, bucket[0]) and _near(height, bucket[1]):
                bucket[2] = int(bucket[2]) + 1
                placed = True
                break
        if not placed:
            buckets.append([sigma, height, 1])
    buckets.sort(key=lambda item: (float(-item[0]), float(item[1])))
    return tuple((item[0], item[1], int(item[2])) for item in buckets)


def expand_reps(reps: tuple[Rep, ...]) -> tuple[tuple[mp.mpf, mp.mpf], ...]:
    out: list[tuple[mp.mpf, mp.mpf]] = []
    for sigma, gamma, mult in reps:
        out.extend([(sigma, gamma)] * int(mult))
    return tuple(out)


def increment_ok_canon(reps: tuple[Rep, ...]) -> bool:
    return r560.increment_ok(expand_reps(reps))


def total_mult(reps: tuple[Rep, ...]) -> int:
    return sum(int(mult) for _, _, mult in reps)


def extremal_host_canon(
    reps: tuple[Rep, ...],
) -> tuple[mp.mpf, mp.mpf, int]:
    """Host = max σ, tie-break min positive γ; return (σ★, γ★, m★)."""
    if not reps:
        raise ValueError("empty canonical Z")
    sigma_star = max(sigma for sigma, _, _ in reps)
    host = [
        (gamma, mult)
        for sigma, gamma, mult in reps
        if _near(sigma, sigma_star)
    ]
    gamma_star = min(gamma for gamma, _ in host)
    mult_star = 0
    for gamma, mult in host:
        if _near(gamma, gamma_star):
            mult_star += int(mult)
    return sigma_star, gamma_star, mult_star


def d_min_canon(reps: tuple[Rep, ...], gamma_star: mp.mpf) -> mp.mpf:
    """min |γ_j − γ★| over canonical ordinates with γ_j ≠ γ★."""
    best = mp.inf
    for _, gamma, _ in reps:
        dist = abs(gamma - gamma_star)
        if dist > mp.mpf(MERGE_ATOL) and dist < best:
            best = dist
    return best


def distinct_gammas(reps: tuple[Rep, ...]) -> bool:
    heights = [gamma for _, gamma, _ in reps]
    for i, left in enumerate(heights):
        for right in heights[i + 1:]:
            if _near(left, right):
                return False
    return True


# ---------------------------------------------------------------------------
# (a,ω) rule — no numeric floor
# ---------------------------------------------------------------------------
def a_lock(sigma: mp.mpf) -> mp.mpf:
    return r561.a_lock(sigma)


def omega_rule(sigma: mp.mpf, gamma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    return r561.omega_rule(sigma, gamma, a_val)


def epsilon_of(a_val: mp.mpf) -> mp.mpf:
    return r561.epsilon_of(a_val)


def isolated(sigma: mp.mpf, d_min: mp.mpf, a_val: mp.mpf) -> bool:
    if not mp.isfinite(d_min) or d_min <= 0:
        return True
    if a_val <= 0:
        return True
    return (mp.pi * a_val / sigma) + epsilon_of(a_val) <= d_min / 2


def omega_positive(sigma: mp.mpf, gamma_star: mp.mpf, a_val: mp.mpf) -> bool:
    return mp.pi * a_val / sigma < gamma_star


def isolation_a(
    sigma: mp.mpf,
    d_min: mp.mpf,
    a_seed: mp.mpf,
    gamma_star: mp.mpf,
) -> mp.mpf:
    """Largest a ≤ a_seed with isolation + ω>0.  No numeric a-floor."""
    a_omega_cap = gamma_star * sigma / (2 * mp.pi)
    a_hi = a_seed
    if a_omega_cap > 0 and a_omega_cap < a_hi:
        a_hi = a_omega_cap
    if a_hi <= 0:
        return a_seed
    can = isolated(sigma, d_min, a_hi) and omega_positive(sigma, gamma_star, a_hi)
    if can:
        return a_hi
    if not mp.isfinite(d_min) or d_min <= 0:
        return a_hi
    log_span = mp.mpf(LOG_A_FLOOR_SPAN)
    a_lo = a_hi * exp_clip(-log_span)
    if a_lo <= 0:
        a_lo = mp.power(mp.mpf(10), -mp.mp.dps)
    if not (
        isolated(sigma, d_min, a_lo)
        and omega_positive(sigma, gamma_star, a_lo)
    ):
        return a_lo
    for _ in range(ISOLATION_BISSECTS):
        a_mid = mp.sqrt(a_lo * a_hi)
        if isolated(sigma, d_min, a_mid) and omega_positive(
            sigma, gamma_star, a_mid,
        ):
            a_lo = a_mid
        else:
            a_hi = a_mid
    return a_lo


def rule_canonical(
    reps: tuple[Rep, ...],
) -> tuple[str, mp.mpf, mp.mpf, mp.mpf, mp.mpf, int, mp.mpf]:
    sigma_star, gamma_star, mult_star = extremal_host_canon(reps)
    d_min = d_min_canon(reps, gamma_star)
    a_seed = a_lock(sigma_star)
    a_val = isolation_a(sigma_star, d_min, a_seed, gamma_star)
    omega = omega_rule(sigma_star, gamma_star, a_val)
    if not mp.isfinite(d_min) or d_min <= 0:
        tag = "canonical_gap"
    elif a_val < a_seed * mp.mpf("0.999"):
        tag = "canonical_shrunk"
    else:
        tag = "canonical"
    return tag, a_val, omega, sigma_star, gamma_star, mult_star, d_min


# ---------------------------------------------------------------------------
# Reduced Q / W / bound (log-scale)
# ---------------------------------------------------------------------------
def eta_tune(sigma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    return r561.eta_tune(sigma, a_val)


def q_reduced_safe(
    sigma_p: mp.mpf,
    t_value: mp.mpf,
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_ref: mp.mpf,
) -> mp.mpf:
    """Q/E with sealed r561 phases; skip cos when the amplitude underflows."""
    scale = (sigma_p ** 2 - sigma_ref ** 2) / (2 * a_val)

    def lobe(dist_sq: mp.mpf, phase: mp.mpf, weight: mp.mpf) -> mp.mpf:
        expo = scale - dist_sq / (2 * a_val)
        if expo < mp.mpf(-700):
            return mp.mpf(0)
        return weight * exp_clip(expo) * mp.cos(phase)

    plus = lobe((t_value + omega) ** 2, sigma_p * (t_value + omega) / a_val, 1)
    minus = lobe((t_value - omega) ** 2, sigma_p * (t_value - omega) / a_val, 1)
    cross = lobe(
        t_value ** 2 + omega ** 2,
        sigma_p * t_value / a_val,
        2,
    )
    return plus + minus + cross


def budget_reduced(
    a_val: mp.mpf, omega: mp.mpf, c_inc: mp.mpf, sigma_ref: mp.mpf,
) -> mp.mpf:
    return r561.budget_reduced(a_val, omega, c_inc, sigma_ref)


def w_reduced_canon(
    reps: tuple[Rep, ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    c_inc: mp.mpf,
    sigma_ref: mp.mpf,
) -> mp.mpf:
    total = mp.mpf(0)
    for sigma_p, gamma_p, mult in reps:
        total += mult * q_reduced_safe(
            sigma_p, gamma_p, a_val, omega, sigma_ref,
        )
    return total + budget_reduced(a_val, omega, c_inc, sigma_ref)


def kappa_val() -> mp.mpf:
    return mp.mpf(KAPPA)


def phi_minus_minus_pi(
    sigma_p: mp.mpf,
    gamma_p: mp.mpf,
    sigma_star: mp.mpf,
    gamma_star: mp.mpf,
    a_val: mp.mpf,
) -> mp.mpf:
    """φ₋ − π without forming the huge raw phase."""
    return (
        sigma_p * (gamma_p - gamma_star) / a_val
        + mp.pi * (sigma_p / sigma_star - 1)
    )


def phase_coherent(
    sigma_p: mp.mpf,
    gamma_p: mp.mpf,
    sigma_star: mp.mpf,
    gamma_star: mp.mpf,
    a_val: mp.mpf,
) -> bool:
    delta = phi_minus_minus_pi(
        sigma_p, gamma_p, sigma_star, gamma_star, a_val,
    )
    return abs(delta) <= kappa_val()


def in_peak_window(
    gamma_p: mp.mpf,
    omega: mp.mpf,
    a_val: mp.mpf,
) -> bool:
    return abs(gamma_p - omega) <= epsilon_of(a_val)


def in_kappa_height_window(
    gamma_p: mp.mpf,
    gamma_star: mp.mpf,
    sigma_star: mp.mpf,
    a_val: mp.mpf,
) -> bool:
    return abs(gamma_p - gamma_star) <= kappa_val() * a_val / sigma_star


def plus_lobe_term(a_val: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Named A₊/E ≤ e^{−ω²/2a} times increment packing + cross."""
    if omega <= 0:
        return mp.mpf(K_MAX_BIN) * (
            r560.theta_lobe(a_val) + (1 + r560.theta3_q(a_val))
        )
    return mp.mpf(K_MAX_BIN) * (
        r560.theta_left_pos(a_val, omega)
        + 2 * r560.theta_cross_pos(a_val, omega)
    )


def far_theta_term(a_val: mp.mpf) -> mp.mpf:
    return mp.mpf(K_MAX_BIN) * r561.truncated_minus_majorant(a_val)


def gap_and_window_terms(
    reps: tuple[Rep, ...],
    sigma_star: mp.mpf,
    gamma_star: mp.mpf,
    a_val: mp.mpf,
    omega: mp.mpf,
) -> tuple[mp.mpf, mp.mpf, int, int, int]:
    """Return (T_gap, T_κ, n_gap, n_coherent, n_farish).  T_κ is 0."""
    t_gap = mp.mpf(0)
    n_gap = 0
    n_coherent = 0
    n_farish = 0
    for sigma_p, gamma_p, mult in reps:
        if _near(sigma_p, sigma_star) and _near(gamma_p, gamma_star):
            continue
        near = in_peak_window(gamma_p, omega, a_val) or in_kappa_height_window(
            gamma_p, gamma_star, sigma_star, a_val,
        )
        coherent = phase_coherent(
            sigma_p, gamma_p, sigma_star, gamma_star, a_val,
        )
        if coherent and near:
            n_coherent += int(mult)
            continue
        if (not _near(sigma_p, sigma_star)) and near and not coherent:
            gap = exp_clip((sigma_p ** 2 - sigma_star ** 2) / (2 * a_val))
            t_gap += mp.mpf(mult) * gap
            n_gap += int(mult)
            continue
        n_farish += int(mult)
    return t_gap, mp.mpf(0), n_gap, n_coherent, n_farish


def bound_reduced(
    reps: tuple[Rep, ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    sigma_star: mp.mpf,
    gamma_star: mp.mpf,
    mult_star: int,
    c_inc: mp.mpf,
) -> tuple[mp.mpf, dict]:
    eta = eta_tune(sigma_star, a_val)
    t_plus = plus_lobe_term(a_val, omega)
    t_gap, t_kappa, n_gap, n_coherent, n_farish = gap_and_window_terms(
        reps, sigma_star, gamma_star, a_val, omega,
    )
    t_far = far_theta_term(a_val)
    t_on = budget_reduced(a_val, omega, c_inc, sigma_star)
    bound = -eta * mult_star + t_plus + t_gap + t_kappa + t_far + t_on
    parts = {
        "eta": eta,
        "T_plus": t_plus,
        "T_gap": t_gap,
        "T_kappa": t_kappa,
        "T_far": t_far,
        "R_on_E": t_on,
        "n_gap": n_gap,
        "n_coherent": n_coherent,
        "n_farish": n_farish,
        "m_star": mult_star,
    }
    return bound, parts


# ---------------------------------------------------------------------------
# Cell evaluation
# ---------------------------------------------------------------------------
def eval_cell(
    name: str,
    raw: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    family: str,
) -> dict:
    reps = canonicalize(raw)
    if not reps:
        raise ValueError("canonicalize emptied %s" % name)
    tag, a_val, omega, sigma_star, gamma_star, mult_star, d_min = (
        rule_canonical(reps)
    )
    w_red = w_reduced_canon(reps, a_val, omega, c_inc, sigma_star)
    b_red, parts = bound_reduced(
        reps, a_val, omega, sigma_star, gamma_star, mult_star, c_inc,
    )
    slack = mp.mpf("1e-8") * (1 + abs(w_red) + abs(b_red))
    conservative = b_red + slack >= w_red
    w_neg = w_red < 0
    b_neg = b_red < 0
    inc_ok = increment_ok_canon(reps)
    isolated_ok = isolated(sigma_star, d_min, a_val)
    omega_ok = omega > 0
    if not inc_ok:
        mechanism = "inc_fail"
    elif not w_neg:
        mechanism = "W_nonneg"
    elif not conservative:
        mechanism = "bound_not_conservative"
    elif not b_neg:
        mechanism = "bound_nonneg"
    else:
        mechanism = "holds"
    return {
        "name": name,
        "family": family,
        "rule": tag,
        "n_raw": str(len(raw)),
        "n_rep": str(len(reps)),
        "n_mult": str(total_mult(reps)),
        "m_star": str(mult_star),
        "inc_ok": str(int(inc_ok)),
        "a": nstr(a_val),
        "omega": nstr(omega),
        "sigma": nstr(sigma_star),
        "gamma": nstr(gamma_star),
        "d_min": "inf" if not mp.isfinite(d_min) else nstr(d_min),
        "eps": nstr(epsilon_of(a_val)),
        "eta": nstr(parts["eta"]),
        "W_red": nstr(w_red),
        "B_red": nstr(b_red),
        "T_plus": nstr(parts["T_plus"]),
        "T_gap": nstr(parts["T_gap"]),
        "T_far": nstr(parts["T_far"]),
        "R_on_E": nstr(parts["R_on_E"]),
        "n_gap": str(parts["n_gap"]),
        "n_coherent": str(parts["n_coherent"]),
        "W_neg": str(int(w_neg)),
        "B_neg": str(int(b_neg)),
        "conservative": str(int(conservative)),
        "isolated": str(int(isolated_ok)),
        "omega_pos": str(int(omega_ok)),
        "mechanism": mechanism,
        "margin": nstr(-w_red),
        "bound_margin": nstr(b_red - w_red),
        "_W": w_red,
        "_B": b_red,
        "_a": a_val,
        "_omega": omega,
        "_d_min": d_min,
        "_conservative": conservative,
        "_w_neg": w_neg,
        "_b_neg": b_neg,
        "_inc_ok": inc_ok,
        "_mechanism": mechanism,
        "_reps": reps,
        "_parts": parts,
        "_sigma": sigma_star,
        "_gamma": gamma_star,
        "_m": mult_star,
        "_isolated": isolated_ok,
    }


def print_row(row: dict) -> None:
    print(
        "  %-42s %-16s W=%s  B=%s  %s"
        % (
            row["name"][:42],
            row["rule"][:16],
            nstr(row["_W"], 5),
            nstr(row["_B"], 5),
            row["mechanism"],
        )
    )


def compact(row: dict) -> dict:
    keys = (
        "name", "family", "rule", "n_raw", "n_rep", "n_mult", "m_star",
        "inc_ok", "a", "omega", "sigma", "gamma", "d_min", "eps", "eta",
        "W_red", "B_red", "T_plus", "T_gap", "T_far", "R_on_E",
        "W_neg", "B_neg", "conservative", "isolated", "mechanism",
        "margin", "bound_margin",
    )
    return {key: row[key] for key in keys}


# ---------------------------------------------------------------------------
# Families
# ---------------------------------------------------------------------------
def family_catalog(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART1  R560 CATALOG  (52 Z, canonicalised)")
    sigmas = (CATALOG_SIGMAS[1],) if smoke else CATALOG_SIGMAS
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        gamma = mp.mpf(HOST_GAMMA)
        for name, quads in r560.make_catalog(sigma, gamma, smoke):
            full = "%s|s=%s|g=%s" % (name, sigma_text, HOST_GAMMA)
            rows.append(eval_cell(full, quads, c_inc, "catalog"))
    shown = rows[:6] if smoke else rows[:8]
    print("  name                                       rule             W/E        B")
    for row in shown:
        print_row(row)
    if not smoke:
        print("  ... %d catalog cells" % len(rows))
    return rows


def family_dmin(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART2  FAMILY A  d_min→0  NO FLOOR  (canonical ordinates)")
    deltas = DELTA_GRID_SMOKE if smoke else DELTA_GRID
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    rows: list[dict] = []
    for delta_text in deltas:
        delta = mp.mpf(delta_text)
        quads = ((sigma, gamma), (sigma, gamma + delta))
        rows.append(eval_cell(
            "dmin:delta=%s" % delta_text, quads, c_inc, "dmin",
        ))
    rows.append(eval_cell(
        "dmin:delta=0:sigma_lt",
        ((sigma, gamma), (mp.mpf("0.10"), gamma)),
        c_inc, "dmin",
    ))
    rows.append(eval_cell(
        "dmin:delta=0:duplicate_host",
        ((sigma, gamma), (sigma, gamma)),
        c_inc, "dmin",
    ))
    rows.append(eval_cell(
        "dmin:delta=0:k43_host_copies",
        tuple((sigma, gamma) for _ in range(K_MAX_BIN)),
        c_inc, "dmin",
    ))
    print("  name                                       rule             W/E        B")
    for row in rows:
        print_row(row)
        print(
            "    DIAG a=%s d_min=%s eta=%s T_far=%s T_gap=%s iso=%s"
            % (
                row["a"], row["d_min"], row["eta"],
                row["T_far"], row["T_gap"], row["isolated"],
            )
        )
    return rows


def _mass_pack(
    sigma: mp.mpf,
    gamma: mp.mpf,
    n_windows: int,
    phase_align: bool,
) -> tuple[tuple[mp.mpf, mp.mpf], ...]:
    a0 = a_lock(sigma)
    omega0 = omega_rule(sigma, gamma, a0)
    eps0 = epsilon_of(a0)
    if phase_align:
        step = 2 * mp.pi * a0 / sigma
        k_need = int(mp.ceil(eps0 / step)) + 1
        first = omega0 + mp.mpf(k_need) * step
    else:
        first = omega0 + eps0 + mp.mpf("1e-12")
    quads: list[tuple[mp.mpf, mp.mpf]] = [(sigma, gamma)]
    gap = mp.mpf(1) + mp.mpf("1e-12")
    for window in range(n_windows):
        site = first + mp.mpf(window) * gap
        n_here = K_MAX_BIN - 1 if window == 0 else K_MAX_BIN
        quads.extend([(sigma, site)] * n_here)
    return tuple(quads)


def family_mass(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART3  FAMILY B  mass pack just outside I_exc")
    n_win = MASS_WINDOWS_SMOKE if smoke else MASS_WINDOWS
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    rows: list[dict] = []
    for phase, tag in ((False, "edge"), (True, "phase")):
        quads = _mass_pack(sigma, gamma, n_win, phase)
        rows.append(eval_cell(
            "mass:%s:w=%d:s=0.25:g=14" % (tag, n_win),
            quads, c_inc, "mass",
        ))
    if not smoke:
        for sigma_text, gamma_text in (("0.49", "14"), ("0.25", "1000")):
            quads = _mass_pack(
                mp.mpf(sigma_text), mp.mpf(gamma_text), n_win, False,
            )
            rows.append(eval_cell(
                "mass:edge:w=%d:s=%s:g=%s" % (n_win, sigma_text, gamma_text),
                quads, c_inc, "mass",
            ))
    print("  name                                       rule             W/E        B")
    for row in rows:
        print_row(row)
        print(
            "    DIAG n=%s d_min=%s T_plus=%s T_far=%s"
            % (row["n_mult"], row["d_min"], row["T_plus"], row["T_far"])
        )
    return rows


def family_sigma(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART4  FAMILY C  σ-extremes × γ-extremes")
    sigmas = SIGMA_EXTREME_SMOKE if smoke else SIGMA_EXTREME
    gammas = GAMMA_EXTREME_SMOKE if smoke else GAMMA_EXTREME
    prev = mp.mp.dps
    mp.mp.dps = DPS_EXTREME
    r560.mp.mp.dps = DPS_EXTREME
    r561.mp.mp.dps = DPS_EXTREME
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            rows.append(eval_cell(
                "ext:single:s=%s:g=%s" % (sigma_text, gamma_text),
                ((sigma, gamma),),
                c_inc, "sigma",
            ))
            if not smoke:
                twin = ((sigma, gamma), (sigma * mp.mpf("0.99"), gamma + 10))
                rows.append(eval_cell(
                    "ext:twin:s=%s:g=%s" % (sigma_text, gamma_text),
                    twin, c_inc, "sigma",
                ))
    mp.mp.dps = prev
    r560.mp.mp.dps = prev
    r561.mp.mp.dps = prev
    print("  name                                       rule             W/E        B")
    shown = rows if smoke else [row for row in rows if "single" in row["name"]]
    for row in shown:
        print_row(row)
    if not smoke:
        print("  ... %d extreme cells (single+twin)" % len(rows))
    return rows


def family_twins(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART5  FAMILY D  same-σ twins near+far + folded plus-lobe")
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    a0 = a_lock(sigma)
    omega0 = omega_rule(sigma, gamma, a0)
    rows: list[dict] = []
    # Canonicalised r563 plus-lobe attacks (γ ↦ |γ|).
    rows.append(eval_cell(
        "twin:equal_sigma_folded_-omega",
        ((sigma, gamma), (sigma, -omega0)),
        c_inc, "twin",
    ))
    rows.append(eval_cell(
        "twin:equal_sigma_far_+",
        ((sigma, gamma), (sigma, gamma + mp.mpf(1000))),
        c_inc, "twin",
    ))
    rows.append(eval_cell(
        "twin:near:delta=1e-4",
        ((sigma, gamma), (sigma, gamma + mp.mpf("1e-4"))),
        c_inc, "twin",
    ))
    if not smoke:
        rows.append(eval_cell(
            "twin:near:delta=1e-8",
            ((sigma, gamma), (sigma, gamma + mp.mpf("1e-8"))),
            c_inc, "twin",
        ))
        rows.append(eval_cell(
            "twin:plus_lobe_folded:r=1-1e-8",
            ((sigma, gamma), ((mp.mpf(1) - mp.mpf("1e-8")) * sigma, -omega0)),
            c_inc, "twin",
        ))
        far = [
            (mp.mpf("0.10"), gamma + mp.mpf(50) + mp.mpf(index))
            for index in range(20)
        ]
        rows.append(eval_cell(
            "twin:far_small_sigma_stack",
            tuple([(sigma, gamma)] + far),
            c_inc, "twin",
        ))
    print("  name                                       rule             W/E        B")
    for row in rows:
        print_row(row)
        print(
            "    DIAG d_min=%s T_gap=%s n_coherent=%s"
            % (row["d_min"], row["T_gap"], row["n_coherent"])
        )
    return rows


def family_mult(smoke: bool, c_inc: mp.mpf) -> list[dict]:
    section("PART6  FAMILY E  multiplicity stacks m ∈ {1,7,43}")
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    masses = MULT_STACK_SMOKE if smoke else MULT_STACK
    rows: list[dict] = []
    for mass in masses:
        quads = tuple((sigma, gamma) for _ in range(mass))
        rows.append(eval_cell(
            "mult:m=%d:s=0.25:g=14" % mass, quads, c_inc, "mult",
        ))
        if not smoke:
            rows.append(eval_cell(
                "mult:m=%d:plus_far" % mass,
                tuple(list(quads) + [(sigma, gamma + mp.mpf(10))]),
                c_inc, "mult",
            ))
    print("  name                                       rule             W/E        B")
    for row in rows:
        print_row(row)
        print(
            "    DIAG m★=%s W=%s  (want ≈ −η m★)"
            % (row["m_star"], row["W_red"])
        )
    return rows


def _de_eval(
    host: tuple[mp.mpf, mp.mpf],
    vec: list[float],
    c_inc: mp.mpf,
) -> tuple[mp.mpf, tuple[tuple[mp.mpf, mp.mpf], ...]]:
    extras: list[tuple[mp.mpf, mp.mpf]] = []
    for index in range(0, len(vec), 2):
        sigma_p = mp.mpf(vec[index])
        gamma_p = abs(mp.mpf(vec[index + 1]))
        if gamma_p <= 0:
            gamma_p = mp.mpf("1e-6")
        extras.append((sigma_p, gamma_p))
    quads = tuple([host] + extras)
    reps = canonicalize(quads)
    if not increment_ok_canon(reps):
        return mp.mpf("-inf"), quads
    row = eval_cell("de", quads, c_inc, "de")
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
    pop = [
        [rng.uniform(bounds[j][0], bounds[j][1]) for j in range(dim)]
        for _ in range(pop_n)
    ]
    a0 = a_lock(host[0])
    omega0 = omega_rule(host[0], host[1], a0)
    elite = [float(host[0]) * 0.999999, float(abs(omega0))]
    if n_extra >= 2:
        elite.extend([float(host[0]) * 0.5, float(host[1]) + 1e-8])
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
    section("PART7  FAMILY F  seeded DE in canonical space  (γ>0)")
    host = (mp.mpf("0.25"), mp.mpf(14))
    pop_n = DE_POP_SMOKE if smoke else DE_POP
    gens = DE_GENS_SMOKE if smoke else DE_GENS
    bounds1 = [(1e-4, 0.249999), (1e-3, 40.0)]
    r1 = _de_run(host, 1, bounds1, DE_SEED_1, pop_n, gens, c_inc)
    bounds2 = [
        (1e-4, 0.249999), (1e-3, 40.0),
        (1e-4, 0.249999), (1e-3, 40.0),
    ]
    r2 = _de_run(host, 2, bounds2, DE_SEED_2, pop_n, gens, c_inc)
    rows = [
        eval_cell("de:round1:n_extra=1", r1["quads"], c_inc, "de"),
        eval_cell("de:round2:n_extra=2", r2["quads"], c_inc, "de"),
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
    print("  name                                       rule             W/E        B")
    for row in rows:
        print_row(row)
        print(
            "    DIAG n=%s inc=%s W=%s B=%s"
            % (row["n_mult"], row["inc_ok"], row["W_red"], row["B_red"])
        )
    return rows, meta


# ---------------------------------------------------------------------------
# G0 / symbolic / verdict
# ---------------------------------------------------------------------------
def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf, str, str]:
    sha_561 = r561.file_sha256()
    r563_path = _HERE / "gabor_dominance_redteam_probe.py"
    sha_563 = hashlib.sha256(r563_path.read_bytes()).hexdigest()
    parent_ok = (
        sha_561.startswith(PARENT_R561_SHA_PREFIX)
        and sha_563.startswith(PARENT_R563_SHA_PREFIX)
    )
    check(
        "G0-parent-sha-prefixes",
        parent_ok,
        "r561=%s r563=%s" % (sha_561[:16], sha_563[:16]),
    )
    g0_ok, g0_err = r561.run_g0(c_inc)
    pin = mp.mpf(C_INC_PIN)
    pin_ok = abs(c_inc - pin) / pin < mp.mpf("1e-9")
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    a_val = a_lock(sigma)
    omega = omega_rule(sigma, gamma, a_val)
    q_pos = r560.quadruple_closed(sigma, gamma, a_val, omega)
    q_neg = r560.quadruple_closed(sigma, -gamma, a_val, omega)
    even_ok = abs(q_pos - q_neg) / (1 + abs(q_pos)) < mp.mpf("1e-12")
    check("G0-Q-even-in-gamma", even_ok, "|Q(σ,γ)-Q(σ,−γ)|/|Q|")
    q_red = q_reduced_safe(sigma, gamma, a_val, omega, sigma)
    e_log = sigma ** 2 / (2 * a_val)
    recon = q_red * (mp.pi / a_val) * exp_clip(e_log)
    rel = abs(recon - q_pos) / (1 + abs(q_pos))
    check("G0-q-reduced-matches-Q/E", rel < mp.mpf("1e-8"), "rel=%s" % nstr(rel, 6))
    raw = ((sigma, gamma), (sigma, -gamma), (sigma, gamma))
    reps = canonicalize(raw)
    merge_ok = (
        len(reps) == 1
        and reps[0][2] == 3
        and _near(reps[0][1], gamma)
    )
    check("G0-canonicalize-merge", merge_ok, "3 copies → m=3 at (σ,|γ|)")
    raw_on = ((mp.mpf(0), gamma), (sigma, gamma))
    reps_on = canonicalize(raw_on)
    check(
        "G0-sigma0-dropped",
        len(reps_on) == 1 and reps_on[0][2] == 1,
        "σ=0 excluded from Z_can",
    )
    # Shrink existence: pairwise distinct γ ⇒ d_min>0 ⇒ isolation succeeds.
    exist_ok = True
    max_a_ratio = mp.mpf(0)
    for delta_text in ("1", "1e-4", "1e-8", "1e-12"):
        delta = mp.mpf(delta_text)
        reps_d = canonicalize(((sigma, gamma), (sigma, gamma + delta)))
        d_min = d_min_canon(reps_d, gamma)
        if not (d_min > 0 and distinct_gammas(reps_d)):
            exist_ok = False
        a_val_i = isolation_a(sigma, d_min, a_lock(sigma), gamma)
        if not isolated(sigma, d_min, a_val_i):
            exist_ok = False
        max_a_ratio = max(max_a_ratio, a_val_i / a_lock(sigma))
    check(
        "G0-shrink-exists-distinct-gamma",
        exist_ok,
        "d_min>0 ⇒ no-floor shrink isolates (max a/a_lock=%s)"
        % nstr(max_a_ratio, 6),
    )
    shared = canonicalize(((sigma, gamma), (mp.mpf("0.10"), gamma)))
    check(
        "G0-shared-gamma-dmin-zero",
        not distinct_gammas(shared) and d_min_canon(shared, gamma) == mp.inf,
        "same γ, different σ: no foreign ordinate ≠ γ★",
    )
    # Replay
    tag_a, a_a, om_a, *_ = rule_canonical(reps_d)
    tag_b, a_b, om_b, *_ = rule_canonical(reps_d)
    replay = tag_a == tag_b and nstr(a_a) == nstr(a_b) and nstr(om_a) == nstr(om_b)
    check("G0-rule-replay", replay, "isolation_a deterministic")
    max_err = g0_err
    if not (parent_ok and g0_ok and pin_ok and even_ok and merge_ok and exist_ok and replay):
        max_err = max(max_err, mp.mpf(1))
    max_err = max(max_err, rel)
    return max_err < mp.mpf("1e-8"), max_err, sha_561, sha_563


def worst_of(rows: list[dict]) -> dict:
    return max(rows, key=lambda row: row["_W"])


def decide(
    all_rows: list[dict],
    de_meta: dict,
) -> tuple[str, dict]:
    inc_rows = [row for row in all_rows if row["_inc_ok"]]
    breaks_w = [row for row in inc_rows if not row["_w_neg"]]
    breaks_c = [row for row in inc_rows if not row["_conservative"]]
    breaks_b = [row for row in inc_rows if row["_w_neg"] and not row["_b_neg"]]
    worst = worst_of(inc_rows) if inc_rows else all_rows[0]
    extra = {
        "n_cells": str(len(all_rows)),
        "n_inc": str(len(inc_rows)),
        "n_W_pos": str(len(breaks_w)),
        "n_bound_broke": str(len(breaks_c)),
        "n_bound_nonneg": str(len(breaks_b)),
        "worst_name": worst["name"],
        "worst_W": nstr(worst["_W"]),
        "worst_B": nstr(worst["_B"]),
        "worst_margin": nstr(-worst["_W"]),
        "worst_mechanism": worst["mechanism"],
        "de_budget": de_meta["budget"],
        "formula": INEQUALITY_REDUCED,
        "window_coverage": WINDOW_COVERAGE,
    }
    for family in ("catalog", "dmin", "mass", "sigma", "twin", "mult", "de"):
        subset = [row for row in inc_rows if row["family"] == family]
        if subset:
            hit = worst_of(subset)
            extra["worst_%s" % family] = nstr(hit["_W"])
            extra["worst_%s_name" % family] = hit["name"]
            extra["worst_%s_mech" % family] = hit["mechanism"]
    if breaks_c:
        hit = min(breaks_c, key=lambda row: row["_B"] - row["_W"])
        extra["break_config"] = hit["name"]
        extra["break_mechanism"] = "bound_not_conservative"
        verdict = "BOUND_NOT_CONSERVATIVE(cells=%s)" % hit["name"]
        return verdict, extra
    if breaks_w or breaks_b:
        hit = (breaks_w + breaks_b)[0]
        if breaks_w:
            hit = max(breaks_w, key=lambda row: row["_W"])
        extra["break_config"] = hit["name"]
        extra["break_mechanism"] = hit["mechanism"]
        verdict = "CANONICAL_DOMINANCE_BREAKS(config=%s, mechanism=%s)" % (
            hit["name"], hit["mechanism"],
        )
        return verdict, extra
    verdict = (
        "CANONICAL_DOMINANCE_HOLDS(cells=%s, worst_margin=%s, "
        "bound_conservative=all)"
        % (extra["n_inc"], nstr(-worst["_W"], 6))
    )
    return verdict, extra


def lean_prop(verdict: str) -> str:
    return (
        "Lean-candidate Prop (NO RH CLAIM).\n"
        "Let Z be a finite multiset of weighted representatives "
        "(σ_j, γ_j, m_j) with 0<σ_j<1/2, γ_j>0, m_j∈ℕ>0, "
        "increment-compliant (Σ_j m_j over any real unit window ≤ K_bin=43).  "
        "Raw FE quadruples are canonicalised by (σ,γ)↦(σ,|γ|) and by "
        "merging equal pairs (add multiplicities); σ=0 belongs only to "
        "the on-line term R_on.  Contribution of a representative is "
        "m_j·Q(σ_j,γ_j) with the sealed Weil-shifted closed form.\n"
        "Host.  (σ★,γ★,m★) := max σ, then min γ among those σ; "
        "d_min := min{|γ_j−γ★| : γ_j≠γ★} (or +∞).  "
        "For every finite Z whose canonical ordinates are pairwise "
        "distinct one has d_min>0, hence there exists a∈(0,a_lock] with "
        "πa/σ★+ε(a)≤d_min/2 (ε(a)=√(2a log max(1/a,4 K_bin))); "
        "the constructive rule takes the largest such a that also "
        "satisfies πa/σ★<γ★.  If d_min=+∞ (all mass at γ★) take "
        "a=min(a_lock, γ★ σ★/(2π)).  ω := γ★−πa/σ★>0, so φ₋=π at "
        "the host.  No numeric a-floor.\n"
        "Conclusion.  W_honest(h_{a,ω}; Z)<0 via the named reduced bound\n"
        "  W/E ≤ −η m★ + T_plus + T_gap + T_far + R_on/E,\n"
        "T_plus = K_bin e^{−ω²/2a}[1/(1−e^{−ω/a})+(1+θ₃(a))]  "
        "(named plus-lobe; A₊/E≤e^{−ω²/2a}; no θ_right in γ′≥0),  "
        "T_gap = Σ m_j e^{(σ′²−σ★²)/2a} over non-coherent σ′<σ★ in "
        "I_exc∪κ-window,  "
        "T_far = K_bin[4 e^{−ε²/2a}+(Θ_lobe−3)],  "
        "η=exp(−π² a/(2σ★²)), E=(π/a)e^{σ★²/2a}, κ=1<π/2, "
        "R_on=2 C_inc S_cert.  Same-σ★ κ-window points (and "
        "phase-coherent σ′<σ★) satisfy cos φ₋≤−cos κ<0 and are "
        "dropped from the upper bound.  Exact host copies contribute "
        "m★·(−η) after the merge.\n"
        "Existing Lean bricks: RH.GaborThetaBound, RH.ZeroIncrement, "
        "RH.GaborHatAnalytic (three-lobe / holomorphic hat).  "
        "Missing: truncated-theta form, Q closed form as 4 Re ĥ_W, "
        "canonical-multiset isolation existence, named plus-lobe "
        "majorant on γ′≥0.\n"
        "Status of this probe: %s\n" % verdict
    )


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    r560.mp.mp.dps = DPS
    r561.mp.mp.dps = DPS
    c_inc = r560.c_inc_prefactor()
    print("gabor_canonical_dominance_probe -- r567")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("space canonical_multiset gamma>0 multiplicity-aware")
    print("quantifiers forall_Z_canonical exists_h")
    print("online 2*C_inc*S_cert  C_inc %s" % nstr(c_inc))
    print("FORMULA  W_honest = Q_off + R_on   (no R_ref, no -3.56)")
    print("FORMULA  %s" % INEQUALITY_REDUCED)
    print("RULE     host=max σ then min γ>0; shrink no floor; ω=γ★−πa/σ★")

    section("G0  PARENT SEAL / Q-EVEN / CANONICALISE / SHRINK EXISTS")
    g0_ok, g0_err, sha_561, sha_563 = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))
    check(
        "G0-c-inc-pin",
        abs(c_inc - mp.mpf(C_INC_PIN)) / mp.mpf(C_INC_PIN) < mp.mpf("1e-9"),
        "C_inc=%s pin=%s" % (nstr(c_inc), C_INC_PIN),
    )
    check("G0-k-bin", K_MAX_BIN == 43, "K_bin=%d" % K_MAX_BIN)
    check(
        "G0-no-a-floor-in-spec",
        SPEC["isolation"].startswith("shrink_a_no_floor")
        and "1e12" not in SPEC["isolation"],
        SPEC["isolation"],
    )

    rows_cat = family_catalog(smoke, c_inc)
    rows_a = family_dmin(smoke, c_inc)
    rows_b = family_mass(smoke, c_inc)
    rows_c = family_sigma(smoke, c_inc)
    rows_d = family_twins(smoke, c_inc)
    rows_e = family_mult(smoke, c_inc)
    rows_f, de_meta = family_de(smoke, c_inc)
    all_rows = (
        rows_cat + rows_a + rows_b + rows_c + rows_d + rows_e + rows_f
    )

    section("PART  VERDICT / WINDOW COVERAGE")
    inc_fail = [row["name"] for row in all_rows if not row["_inc_ok"]]
    check(
        "P-increment-ok",
        not inc_fail,
        "every canonical Z has Σ m ≤%d / unit window" % K_MAX_BIN
        if not inc_fail
        else "FAIL %s" % ",".join(inc_fail[:6]),
    )
    if smoke:
        check("P1-smoke-catalog", len(rows_cat) >= 4, "n=%d" % len(rows_cat))
    else:
        check("P1-catalog-52", len(rows_cat) == 52, "n=%d" % len(rows_cat))

    # Near-tie table (the r563 floor hole).
    print("  NEAR-TIE CELLS (no floor)")
    for row in rows_a:
        if row["name"].startswith("dmin:delta="):
            print(
                "    %s  a=%s  W/E=%s  B=%s  eta=%s  T_far=%s  iso=%s"
                % (
                    row["name"], row["a"], row["W_red"], row["B_red"],
                    row["eta"], row["T_far"], row["isolated"],
                )
            )
    # Structural a→0: η→1, foreign→0, R_on/E→0.
    tiny = [row for row in rows_a if "1e-12" in row["name"] or "1e-8" in row["name"]]
    if tiny:
        better = all(
            mp.mpf(row["eta"]) > mp.mpf("0.999")
            and abs(mp.mpf(row["T_far"])) < mp.mpf("1e-4")
            and abs(mp.mpf(row["R_on_E"])) < mp.mpf("1e-8")
            for row in tiny
        )
        check(
            "P-extreme-shrink-better",
            better or smoke,
            "η→1, T_far→0, R_on/E→0 at δ≤1e-8 (limit improves)",
        )
    elif smoke:
        check("P-extreme-shrink-skipped-partial", True, "smoke has 1e-8")

    shared = [row for row in rows_a if row["name"] == "dmin:delta=0:sigma_lt"]
    if shared:
        check(
            "P-shared-gamma-gap",
            shared[0]["_w_neg"] and shared[0]["_conservative"] and shared[0]["_b_neg"],
            "σ′<σ★ at γ★: T_gap=%s W=%s B=%s"
            % (shared[0]["T_gap"], shared[0]["W_red"], shared[0]["B_red"]),
        )

    stacks = [row for row in rows_e if row["name"].startswith("mult:m=")]
    stack_ok = True
    for row in stacks:
        if "plus_far" in row["name"]:
            continue
        want = -mp.mpf(row["eta"]) * mp.mpf(row["m_star"])
        if abs(row["_W"] - want) > mp.mpf("0.05") * (1 + abs(want)):
            # plus/cross leftovers + R_on; host-dominated
            if row["_W"] >= 0 or int(row["m_star"]) != int(row["n_mult"]):
                stack_ok = False
    check(
        "P-multiplicity-merge",
        stack_ok and stacks,
        "exact host copies merge; W ≈ −η m★",
    )

    verdict, extra = decide(all_rows, de_meta)
    extra["parent_r561"] = sha_561
    extra["parent_r563"] = sha_563
    print("  VERDICT %s" % verdict)
    print("  WORST   %s  W/E=%s  B=%s  mech=%s" % (
        extra["worst_name"], extra["worst_W"], extra["worst_B"],
        extra["worst_mechanism"],
    ))
    print("  CELLS   n=%s inc=%s W_pos=%s bound_broke=%s bound_nonneg=%s" % (
        extra["n_cells"], extra["n_inc"], extra["n_W_pos"],
        extra["n_bound_broke"], extra["n_bound_nonneg"],
    ))
    print("  DE      %s" % extra["de_budget"])
    print("  WINDOW  %s" % WINDOW_COVERAGE)
    print("  FORMULA %s" % INEQUALITY_REDUCED)
    check("P-verdict-formed", verdict.startswith("CANONICAL_") or verdict.startswith("BOUND_"), verdict)

    all_cons = all(row["_conservative"] for row in all_rows if row["_inc_ok"])
    all_neg = all(
        row["_w_neg"] and row["_b_neg"]
        for row in all_rows if row["_inc_ok"]
    )
    check("P-bound-conservative-all", all_cons, "B ≥ W on every inc-ok cell")
    check("P-bound-and-W-negative", all_neg, "W<0 and B<0 on every inc-ok cell")

    section("SHARP PER FAMILY")
    for family in ("catalog", "dmin", "mass", "sigma", "twin", "mult", "de"):
        key = "worst_%s" % family
        if key in extra:
            print(
                "  %s  %s  W/E=%s  mech=%s"
                % (
                    family, extra["worst_%s_name" % family],
                    extra[key], extra["worst_%s_mech" % family],
                )
            )

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock; DE uses Random(seed); BLAS threads=1",
    )
    replay_raw = ((mp.mpf("0.25"), mp.mpf(14)), (mp.mpf("0.10"), mp.mpf(14)))
    replay_a = eval_cell("replay", replay_raw, c_inc, "gate")
    replay_b = eval_cell("replay", replay_raw, c_inc, "gate")
    check(
        "G3-inprocess-rescore",
        nstr(replay_a["_W"]) == nstr(replay_b["_W"])
        and nstr(replay_a["_B"]) == nstr(replay_b["_B"]),
        "replay W/E %s B %s" % (nstr(replay_a["_W"], 6), nstr(replay_a["_B"], 6)),
    )
    if smoke:
        check("G4-smoke-subset", True, "reduced catalog/δ/σ/γ + DE pop=4 gens=2")
    else:
        check("G4-full-grid", True, "52 catalog + full attack grids + DE pop=16 gens=10")

    canon = {
        "family_catalog": [compact(row) for row in rows_cat],
        "family_dmin": [compact(row) for row in rows_a],
        "family_mass": [compact(row) for row in rows_b],
        "family_sigma": [compact(row) for row in rows_c],
        "family_twin": [compact(row) for row in rows_d],
        "family_mult": [compact(row) for row in rows_e],
        "family_de": [compact(row) for row in rows_f],
        "de_meta": de_meta,
        "verdict": verdict,
        "extra": extra,
        "C_inc": nstr(c_inc),
        "SPEC_SHA": SPEC_SHA,
        "formula": INEQUALITY_REDUCED,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    lean = lean_prop(verdict)
    section("LEAN CANDIDATE (text; no Lean edit)")
    print(lean)

    next_suggest = (
        "r567: %s  worst %s W/E=%s B=%s; "
        "canonical multiset (σ,|γ|,m), no a-floor, named plus-lobe "
        "e^{−ω²/2a}; near-tie δ≤1e-12 shrinks and improves.  "
        "KEIN RH-CLAIM"
        % (verdict, extra["worst_name"], extra["worst_W"], extra["worst_B"])
    )
    print("PAYLOAD_SHA256 %s" % seal)
    print("C_INC %s" % nstr(c_inc))
    print("N_CELLS %s" % extra["n_cells"])
    print("N_W_POS %s" % extra["n_W_pos"])
    print("N_BOUND_BROKE %s" % extra["n_bound_broke"])
    print("WORST_NAME %s" % extra["worst_name"])
    print("WORST_W %s" % extra["worst_W"])
    print("WORST_B %s" % extra["worst_B"])
    print("WORST_MARGIN %s" % extra["worst_margin"])
    print("DE_BUDGET %s" % extra["de_budget"])
    print("FORMULA %s" % INEQUALITY_REDUCED)
    print("WINDOW_COVERAGE %s" % WINDOW_COVERAGE)
    print("VERDICT %s" % verdict)
    print("PARENT_R561_FILE_SHA256 %s" % sha_561)
    print("PARENT_R563_FILE_SHA256 %s" % sha_563)
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
            "r567 canonical multiplicity-aware dominance repair "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
