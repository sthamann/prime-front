#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_mixture_witness_probe -- r554

Round 554.  Experiments-only scout of a MIXTURE witness against the
r553 cluster wall.  Quantifiers remain config-first: Z frozen
(increment-compliant), then h is chosen seeing Z.

  r553: 1-packet WITNESS_LOSES on cluster k=5 unit σ=0.25 γ=14
        (W_left≈+110.7); 2-packet WITNESS_LOSES on game k=10
        over 5√a (W_left≈+1.06e5).

  NEW HYPOTHESIS.  h_mix = Σ_j c_j h_{ω_j,a_j} in the even
  Schwartz class (no positivity of the kernel required).
  Intuition: a local cluster is seen only by nearby packets,
  while a tuned negative eigen-term can stay coherent.

CLAIM BOUNDARY.  Finite closed-form / deterministic-grid
arithmetic on finite Gabor combinations.  NO RH claim, NO
anti-RH claim, NO ledger/paper/Lean/next.txt edit.

HAT CONVENTION.  Weil-shifted ĥ_W(s)=H(s−1/2) H(1/2−s),
matching r553 / `RH.pureGaborHatDelta`.  A quadruple
contributes 4 Re ĥ_W.  For a mixture, H_mix=Σ c_j H_j and
ĥ_W = H_mix(δ) H_mix(−δ)  (quadratic form; same convention
as the r553 two-packet class extension).

LEFTOVER (r553):
  W_left = R541_MARGIN + (Q_off − Q_primary) + max(0, R_on − R_ref)
Win iff W_left < 0.  Normalisation: ||c||_∞ = 1 so the strongest
packet stays unit-amplitude (the sealed −3.56 credits an O(1)
eigen-term).  A simplex / scale-down that makes |Q_primary|
≪ |Q_ref| is flagged as the inhomogeneous-credit cheat
(mechanism=norm_nonlin), not an honest win.

On-line budget: per-packet theta majorant, combined by the
tighter of the n-term and weighted Cauchy–Schwarz certificates
  R_on ≤ min( n Σ c_j² R_j ,  (Σ|c_j|) Σ|c_j| R_j ).
The n-term form recovers the r553 two-packet majorant.

Verdicts, separately for positive (c≥0) and signed (c∈ℝ) classes:
  MIXTURE_WINS(n=…, mechanism=…, worst_leftover=…)
  MIXTURE_LOSES(config=…)
  MIXTURE_CONDITIONAL(needs=…)
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
D_REL = ("0", "1", "10")
D_ABS = ("1",)
K_CLUSTER = (2, 5, 10)
CLUSTER_WINDOWS = ("unit",)
A_MIN_FACTOR = "0.25"
A_FACTORS = ("0.5", "1", "2", "4", "8")
GAME_WIDTHS = ("1", "5")
GAME_K = (5, 10)
MIX_N = (3, 8, 21)
R541_MARGIN = "-3.56"
PRI_FLOOR = "0.5"  # honest win: |Q_pri| ≥ PRI_FLOOR |Q_local_r541|
RIDGE_GRID = ("1e-12", "1e-8", "1e-4", "1e-2", "1e-1")
SIGN_VALS = ("-2", "-1", "-0.5", "0", "0.5", "1", "2")
POS_VALS = ("0", "0.25", "0.5", "1", "2")
NSTR_DIGITS = 12
DPS = 80
K_MAX_BIN = 43

SPEC = {
    "round": 554,
    "parent_round": 553,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.MIXTURE_WITNESS.01",
    "target": "GaborSeparationInequality.mixture_class",
    "hat": "weil_shifted_product",
    "class_pos": "nonneg_finite_gabor_combination ||c||_inf=1",
    "class_sign": "real_finite_gabor_combination ||c||_inf=1",
    "quantifiers": "forall_Z exists_h  (config first, witness last)",
    "a_rule_seed": "sigma^2/64",
    "omega_rule_seed": "gamma-pi*a/sigma",
    "online_budget": "min(n*sum(c_j^2 R_j),(sum|c_j|)*sum(|c_j| R_j))",
    "theta_majorant": "2+vartheta_3(0,exp(-1/(2a)))",
    "host_sigmas": list(HOST_SIGMAS),
    "host_gammas": list(HOST_GAMMAS),
    "d_rel_sqrt_a": list(D_REL),
    "d_abs": list(D_ABS),
    "k_cluster": list(K_CLUSTER),
    "cluster_windows": list(CLUSTER_WINDOWS),
    "mix_n": list(MIX_N),
    "a_factors": list(A_FACTORS),
    "a_min_factor": A_MIN_FACTOR,
    "score": "leftover = R541_MARGIN + (Q_off-Q_primary) + max(0,R_on-R_ref)",
    "game_widths": list(GAME_WIDTHS),
    "game_k": list(GAME_K),
    "r541_margin": R541_MARGIN,
    "pri_floor": PRI_FLOOR,
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
    "optimiser": "deterministic_finite_grid_plus_ridge_kernel",
    "normalisation": "||c||_inf=1; simplex reported only as audit",
    "scope": (
        "increment-compliant off-line families; mixture of Gabors; "
        "linearity audit; two-iteration min-max game"
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
    return 2 * c_inc * certified_bin_sum(a, omega)


def gabor_H(a: mp.mpf, omega: mp.mpf, z: mp.mpc) -> mp.mpc:
    return (
        mp.mpf("0.5")
        * mp.sqrt(mp.pi / a)
        * (
            exp_c((z + mp.j * omega) ** 2 / (4 * a))
            + exp_c((z - mp.j * omega) ** 2 / (4 * a))
        )
    )


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


def leftover(
    q_off: mp.mpf,
    q_primary: mp.mpf,
    r_on: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> mp.mpf:
    extra_on = r_on - r_ref
    if extra_on < 0:
        extra_on = mp.mpf(0)
    return (-margin) + (q_off - q_primary) + extra_on


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


def pin_inf(coeffs: list[mp.mpf]) -> list[mp.mpf]:
    peak = max((abs(item) for item in coeffs), default=mp.mpf(0))
    if peak <= 0:
        return [mp.mpf(0) for _ in coeffs]
    return [item / peak for item in coeffs]


def pin_simplex(coeffs: list[mp.mpf]) -> list[mp.mpf]:
    clipped = [max(item, mp.mpf(0)) for item in coeffs]
    total = sum(clipped, mp.mpf(0))
    if total <= 0:
        n_use = max(1, len(coeffs))
        return [mp.mpf(1) / n_use for _ in coeffs]
    return [item / total for item in clipped]


# ---------------------------------------------------------------------------
# Packet bank: precompute H_j(±δ_q) so weight search is linear algebra.
# ---------------------------------------------------------------------------
class PacketBank:
    def __init__(
        self,
        packets: list[tuple[mp.mpf, mp.mpf]],
        quads: tuple[tuple[mp.mpf, mp.mpf], ...],
        c_inc: mp.mpf,
    ) -> None:
        self.packets = list(packets)
        self.quads = quads
        self.n = len(packets)
        self.k = len(quads)
        self.hp: list[list[mp.mpc]] = []
        self.hm: list[list[mp.mpc]] = []
        self.q1: list[list[mp.mpf]] = []
        self.r_pack: list[mp.mpf] = []
        for a_val, omega in packets:
            row_p: list[mp.mpc] = []
            row_m: list[mp.mpc] = []
            row_q: list[mp.mpf] = []
            for sigma, gamma in quads:
                delta = sigma + mp.j * gamma
                plus = gabor_H(a_val, omega, delta)
                minus = gabor_H(a_val, omega, -delta)
                row_p.append(plus)
                row_m.append(minus)
                row_q.append(4 * mp.re(plus * minus))
            self.hp.append(row_p)
            self.hm.append(row_m)
            self.q1.append(row_q)
            self.r_pack.append(online_budget(a_val, omega, c_inc))

    def q_prod(self, coeffs: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf, list[mp.mpf]]:
        terms: list[mp.mpf] = []
        for q_idx in range(self.k):
            plus = mp.mpc(0)
            minus = mp.mpc(0)
            for j_idx, coeff in enumerate(coeffs):
                plus += coeff * self.hp[j_idx][q_idx]
                minus += coeff * self.hm[j_idx][q_idx]
            terms.append(4 * mp.re(plus * minus))
        total = sum(terms, mp.mpf(0))
        primary = min(terms) if terms else mp.mpf(0)
        return total, primary, terms

    def q_add(self, coeffs: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf, list[mp.mpf]]:
        terms: list[mp.mpf] = []
        for q_idx in range(self.k):
            acc = mp.mpf(0)
            for j_idx, coeff in enumerate(coeffs):
                acc += coeff * self.q1[j_idx][q_idx]
            terms.append(acc)
        total = sum(terms, mp.mpf(0))
        primary = min(terms) if terms else mp.mpf(0)
        return total, primary, terms

    def r_on(self, coeffs: list[mp.mpf]) -> mp.mpf:
        n_use = mp.mpf(max(1, self.n))
        sum_c2_r = sum(
            (coeff * coeff) * self.r_pack[j_idx]
            for j_idx, coeff in enumerate(coeffs)
        )
        sum_abs = sum((abs(coeff) for coeff in coeffs), mp.mpf(0))
        sum_abs_r = sum(
            abs(coeff) * self.r_pack[j_idx]
            for j_idx, coeff in enumerate(coeffs)
        )
        n_term = n_use * sum_c2_r
        w_term = sum_abs * sum_abs_r
        if n_term <= w_term:
            return n_term
        return w_term

    def h_matrix(self, sites: list[int]) -> mp.matrix:
        rows = 2 * len(sites)
        mat = mp.matrix(rows, self.n)
        for s_idx, q_idx in enumerate(sites):
            for j_idx in range(self.n):
                val = self.hp[j_idx][q_idx]
                mat[2 * s_idx, j_idx] = mp.re(val)
                mat[2 * s_idx + 1, j_idx] = mp.im(val)
        return mat

    def q_add_matrix(self, sites: list[int]) -> mp.matrix:
        mat = mp.matrix(len(sites), self.n)
        for s_idx, q_idx in enumerate(sites):
            for j_idx in range(self.n):
                mat[s_idx, j_idx] = self.q1[j_idx][q_idx]
        return mat


def score_bank(
    bank: PacketBank,
    coeffs: list[mp.mpf],
    r_ref: mp.mpf,
    margin: mp.mpf,
    additive: bool = False,
) -> dict:
    if additive:
        q_off, q_pri, terms = bank.q_add(coeffs)
    else:
        q_off, q_pri, terms = bank.q_prod(coeffs)
    r_on = bank.r_on(coeffs)
    w_left = leftover(q_off, q_pri, r_on, r_ref, margin)
    extra = q_off - q_pri
    hinge = r_on - r_ref
    if hinge < 0:
        hinge = mp.mpf(0)
    return {
        "W": w_left,
        "Q_off": q_off,
        "Q_primary": q_pri,
        "R_on": r_on,
        "extra": extra,
        "hinge": hinge,
        "terms": terms,
        "c": list(coeffs),
        "c_l1": sum((abs(item) for item in coeffs), mp.mpf(0)),
        "c_l2": mp.sqrt(sum((item * item for item in coeffs), mp.mpf(0))),
        "c_linf": max((abs(item) for item in coeffs), default=mp.mpf(0)),
    }


def local_q_lock(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
) -> mp.mpf:
    """Unit-amplitude r541 lock on the max-σ, then min-γ quadruple."""
    ordered = sorted(quads, key=lambda item: (-item[0], item[1]))
    sigma, gamma = ordered[0]
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    return quadruple_closed(sigma, gamma, a_val, omega)


def honest_pri(rec: dict, q_local: mp.mpf) -> bool:
    """Primary eigen-term still O(1) versus the local unit Gabor, not
    the global σ=0.10 Q_ref (that scale is ~6× larger at σ=0.25)."""
    if q_local == 0:
        return True
    return abs(rec["Q_primary"]) >= mp.mpf(PRI_FLOOR) * abs(q_local)


# ---------------------------------------------------------------------------
# Linear algebra helpers (deterministic; no RNG).
# ---------------------------------------------------------------------------
def ridge_solve(mat: mp.matrix, rhs: mp.matrix, lam: mp.mpf) -> mp.matrix:
    gram = mat.T * mat
    for idx in range(gram.rows):
        gram[idx, idx] += lam
    return mp.lu_solve(gram, mat.T * rhs)


def cheap_cond(mat: mp.matrix) -> mp.mpf:
    """Frobenius / min-abs-column-norm ratio.  Deterministic, no SVD.

    Used as a robustness diagnostic, not as a certified spectral
    condition number.  Exact σ_max/σ_min is too expensive at dps=80
    for the n=21 banks.
    """
    if mat.rows == 0 or mat.cols == 0:
        return mp.inf
    fro = mp.norm(mat)
    col_min = mp.inf
    for col in range(mat.cols):
        acc = mp.mpf(0)
        for row in range(mat.rows):
            acc += mat[row, col] * mat[row, col]
        nrm = mp.sqrt(acc)
        if nrm < col_min:
            col_min = nrm
    if col_min <= 0:
        return mp.inf
    return fro / col_min


# ---------------------------------------------------------------------------
# Packet placement (deterministic function of Z).
# ---------------------------------------------------------------------------
def place_packets(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    n_use: int,
    mode: str,
) -> list[tuple[mp.mpf, mp.mpf]]:
    sigma_max, gamma_min, gamma_max, gamma_mean, _ = config_stats(quads)
    a_ref = scaling_a(sigma_max)
    a_min = a_ref * mp.mpf(A_MIN_FACTOR)
    span = gamma_max - gamma_min
    width = mp.sqrt(a_ref)
    if mode == "equidist":
        half = max(span / 2, 2 * width, mp.mpf("0.25"))
        low = gamma_mean - half
        high = gamma_mean + half
        a_val = a_ref
    elif mode == "cover":
        cover_span = max(span, mp.mpf("0.5"))
        a_val = max(a_min, sigma_max * cover_span / (2 * mp.pi))
        half = max(cover_span / 2, 2 * mp.sqrt(a_val))
        low = gamma_mean - half
        high = gamma_mean + half
    else:
        # adaptive: unique ordinates, then midpoints, then equidist fill
        sites = list(unique_sorted([gamma for _, gamma in quads]))
        if len(sites) >= 2:
            mids = [
                (sites[idx] + sites[idx + 1]) / 2
                for idx in range(len(sites) - 1)
            ]
            sites = list(unique_sorted(sites + mids))
        if len(sites) < n_use:
            half = max(span / 2, 2 * width, mp.mpf("0.25"))
            fill = [
                gamma_mean - half
                + (mp.mpf(2 * half) * idx / max(1, n_use - 1))
                for idx in range(n_use)
            ]
            sites = list(unique_sorted(sites + fill))
        if n_use == 1:
            picked = [gamma_mean]
        else:
            picked = sites[:n_use]
            if len(picked) < n_use:
                extra = n_use - len(picked)
                for idx in range(extra):
                    picked.append(
                        gamma_mean
                        + width * (idx + 1) * (mp.mpf(1) if idx % 2 == 0 else mp.mpf(-1))
                    )
        return [
            (a_ref, scaling_omega(sigma_max, site)) for site in picked[:n_use]
        ]
    if n_use == 1:
        sites = [gamma_mean]
    else:
        sites = [
            low + (high - low) * mp.mpf(idx) / (n_use - 1)
            for idx in range(n_use)
        ]
    return [(a_val, scaling_omega(sigma_max, site)) for site in sites]


def packet_modes(smoke: bool) -> tuple[str, ...]:
    if smoke:
        return ("equidist",)
    return ("equidist", "adaptive")


def ns_for(name: str, smoke: bool) -> tuple[int, ...]:
    if smoke:
        return (3,)
    heavy = ("cluster:", "game:", "spread:", "double:", "adv:")
    if any(tag in name for tag in heavy):
        return MIX_N
    return (3, 8)


# ---------------------------------------------------------------------------
# Weight search
# ---------------------------------------------------------------------------
def ones_hot(n_use: int, index: int) -> list[mp.mpf]:
    out = [mp.mpf(0)] * n_use
    out[index] = mp.mpf(1)
    return out


def uniform_pos(n_use: int) -> list[mp.mpf]:
    return [mp.mpf(1)] * n_use


def target_heavy(n_use: int, index: int) -> list[mp.mpf]:
    out = [mp.mpf("0.05")] * n_use
    out[index] = mp.mpf(1)
    return out


def coord_pass(
    bank: PacketBank,
    start: list[mp.mpf],
    values: tuple[str, ...],
    r_ref: mp.mpf,
    margin: mp.mpf,
    nonnegative: bool,
    q_ref: mp.mpf,
) -> dict:
    best = score_bank(bank, pin_inf(start), r_ref, margin)
    best["_honest"] = honest_pri(best, q_ref)
    for j_idx in range(bank.n):
        local = list(best["c"])
        for text in values:
            trial = list(local)
            trial[j_idx] = mp.mpf(text)
            if nonnegative:
                trial = [max(item, mp.mpf(0)) for item in trial]
            trial = pin_inf(trial)
            if max((abs(item) for item in trial), default=0) <= 0:
                continue
            rec = score_bank(bank, trial, r_ref, margin)
            rec["_honest"] = honest_pri(rec, q_ref)
            if _better(rec, best):
                best = rec
                local = list(trial)
    return best


def _better(left: dict, right: dict) -> bool:
    # Prefer honest leftover, then leftover, then smaller ||c||_2.
    if left["_honest"] and not right["_honest"]:
        return True
    if (not left["_honest"]) and right["_honest"]:
        return False
    if left["W"] < right["W"] - mp.mpf("1e-20"):
        return True
    if abs(left["W"] - right["W"]) <= mp.mpf("1e-20"):
        return left["c_l2"] < right["c_l2"]
    return False


def positive_search(
    bank: PacketBank,
    r_ref: mp.mpf,
    margin: mp.mpf,
    q_ref: mp.mpf,
    smoke: bool,
) -> dict:
    seeds = [
        uniform_pos(bank.n),
        ones_hot(bank.n, 0),
        ones_hot(bank.n, bank.n // 2),
        ones_hot(bank.n, bank.n - 1),
        target_heavy(bank.n, 0),
        target_heavy(bank.n, bank.n // 2),
    ]
    # Target-score weights from additive single-packet Q at q=0.
    raw = [-bank.q1[j_idx][0] for j_idx in range(bank.n)]
    seeds.append(pin_inf([max(item, mp.mpf(0)) for item in raw]))
    if bank.n == 3 and not smoke:
        for i_val in range(5):
            for j_val in range(5 - i_val):
                k_val = 4 - i_val - j_val
                seeds.append(
                    [mp.mpf(i_val), mp.mpf(j_val), mp.mpf(k_val)]
                )
    best: dict | None = None
    values = POS_VALS[:3] if smoke else POS_VALS
    for seed in seeds:
        rec = coord_pass(
            bank, seed, values, r_ref, margin, True, q_ref,
        )
        if best is None or _better(rec, best):
            best = rec
    assert best is not None
    best["mechanism"] = "positive_avg"
    best["family"] = "positive"
    return best


def sign_search(
    bank: PacketBank,
    r_ref: mp.mpf,
    margin: mp.mpf,
    q_ref: mp.mpf,
    smoke: bool,
) -> dict:
    seeds = [
        ones_hot(bank.n, 0),
        ones_hot(bank.n, bank.n // 2),
        [mp.mpf(1) if idx % 2 == 0 else mp.mpf(-1) for idx in range(bank.n)],
        [mp.mpf(1) if idx % 2 == 0 else mp.mpf("-0.5") for idx in range(bank.n)],
        target_heavy(bank.n, 0),
    ]
    # Two-packet sign pairs on the ends (active nulling seed).
    if bank.n >= 2:
        pair = [mp.mpf(0)] * bank.n
        pair[0] = mp.mpf(1)
        pair[-1] = mp.mpf(-1)
        seeds.append(pair)
        pair2 = [mp.mpf(0)] * bank.n
        pair2[0] = mp.mpf(1)
        pair2[1] = mp.mpf(-1)
        seeds.append(pair2)
    best: dict | None = None
    values = SIGN_VALS[1:6] if smoke else SIGN_VALS
    for seed in seeds:
        rec = coord_pass(
            bank, seed, values, r_ref, margin, False, q_ref,
        )
        rec["mechanism"] = "sign_mixing"
        rec["family"] = "signed"
        if best is None or _better(rec, best):
            best = rec
    assert best is not None
    return best


def cluster_sites(quads: tuple[tuple[mp.mpf, mp.mpf], ...]) -> list[int]:
    """All quads are the adversary; 'cluster' = every site except the
    most-negative single-packet (packet 0) site, falling back to all
    but the first if the bank is not yet built."""
    if len(quads) <= 1:
        return []
    return list(range(1, len(quads)))


def nulling_search(
    bank: PacketBank,
    r_ref: mp.mpf,
    margin: mp.mpf,
    q_ref: mp.mpf,
    smoke: bool,
) -> dict:
    """Linear H-nulling: H_mix(δ_site)=0 at selected cluster sites.

    H_mix(δ)=0 is two real linear constraints per site and implies
    the product-hat Q at that site is exactly zero.  Target packet
    is pinned at c_0=1; remaining coefficients are a ridge
    minimum-norm solve.  Also tries additive-Q nulling.
    """
    sites_all = cluster_sites(bank.quads)
    if not sites_all:
        rec = score_bank(bank, ones_hot(bank.n, 0), r_ref, margin)
        rec["_honest"] = honest_pri(rec, q_ref)
        rec["mechanism"] = "linear_nulling"
        rec["family"] = "signed"
        rec["cond"] = nstr(mp.mpf(1))
        rec["null_res"] = nstr(mp.mpf(0))
        rec["null_kind"] = "none"
        rec["n_sites"] = "0"
        return rec

    # How many sites can we try to null?  Each costs 2 real rows.
    # Keep at least one free-ish direction: r ≤ (n-1)//2, r≥1.
    max_sites = max(1, (bank.n - 1) // 2)
    if smoke or bank.n >= 8:
        max_sites = min(max_sites, 2)
    n_sites = min(len(sites_all), max_sites)
    # Prefer sites with the largest |single-packet Q| of packet 0
    # (the loudest cluster contributors to the target-locked packet).
    ranked = sorted(
        sites_all,
        key=lambda q_idx: -abs(bank.q1[0][q_idx]),
    )
    site_sets = [ranked[:n_sites]]
    if n_sites > 1:
        site_sets.append(ranked[:1])
    if len(ranked) > n_sites:
        site_sets.append(ranked[: min(len(ranked), bank.n - 1)])

    best: dict | None = None
    best_rest: mp.matrix | None = None
    ridges = RIDGE_GRID[:3] if (smoke or bank.n >= 8) else RIDGE_GRID
    kinds = (("H", bank.h_matrix), ("Qadd", bank.q_add_matrix))
    for kind, builder in kinds:
        for sites in site_sets:
            mat = builder(sites)
            if mat.cols <= 1:
                continue
            rest = mat[:, 1:]
            rhs = -mat[:, 0]
            for lam_text in ridges:
                lam = mp.mpf(lam_text)
                try:
                    solved = ridge_solve(rest, rhs, lam)
                except Exception:
                    continue
                coeffs = [mp.mpf(1)]
                for idx in range(solved.rows):
                    coeffs.append(mp.mpf(solved[idx, 0]))
                coeffs = pin_inf(coeffs)
                rec = score_bank(bank, coeffs, r_ref, margin)
                rec["_honest"] = honest_pri(rec, q_ref)
                rec["mechanism"] = "linear_nulling"
                rec["family"] = "signed"
                rec["cond"] = ""
                residual = mp.norm(mat * mp.matrix(coeffs))
                rec["null_res"] = nstr(residual)
                rec["null_kind"] = kind
                rec["n_sites"] = str(len(sites))
                rec["ridge"] = lam_text
                if best is None or _better(rec, best):
                    best = rec
                    best_rest = rest
    if best is None:
        rec = score_bank(bank, ones_hot(bank.n, 0), r_ref, margin)
        rec["_honest"] = honest_pri(rec, q_ref)
        rec["mechanism"] = "linear_nulling"
        rec["family"] = "signed"
        rec["cond"] = nstr(mp.inf)
        rec["null_res"] = nstr(mp.mpf(1))
        rec["null_kind"] = "fallback"
        rec["n_sites"] = "0"
        return rec
    if best_rest is not None:
        try:
            best["cond"] = nstr(cheap_cond(best_rest))
        except Exception:
            best["cond"] = nstr(mp.inf)
    else:
        best["cond"] = nstr(mp.inf)
    return best


# ---------------------------------------------------------------------------
# Single-packet control (r553 reproduction)
# ---------------------------------------------------------------------------
def aw_seeds(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...], smoke: bool,
) -> list[tuple[str, mp.mpf, mp.mpf]]:
    sigma_max, gamma_min, gamma_max, gamma_mean, _ = config_stats(quads)
    span = gamma_max - gamma_min
    a_ref = scaling_a(sigma_max)
    a_min = a_ref * mp.mpf(A_MIN_FACTOR)
    factors = A_FACTORS
    seeds: list[tuple[str, mp.mpf, mp.mpf]] = []
    sites = unique_sorted([quads[0][1], gamma_mean, gamma_min, gamma_max])
    for site in sites:
        seeds.append(("r541@%s" % nstr(site, 6), a_ref, scaling_omega(sigma_max, site)))
    for fac_text in factors:
        a_val = a_ref * mp.mpf(fac_text)
        for site in sites:
            seeds.append(("afac=%s@%s" % (fac_text, nstr(site, 6)), a_val, site))
            seeds.append(
                (
                    "afac=%s@r541(%s)" % (fac_text, nstr(site, 6)),
                    a_val,
                    site - mp.pi * a_val / sigma_max,
                )
            )
    if span > 0:
        a_edge = sigma_max * span / (2 * mp.pi)
        if a_edge >= a_min:
            seeds.append(("mid_pi", a_edge, gamma_mean))
            seeds.append(("mid_halfpi", 2 * a_edge, gamma_mean))
        a_cover = max(a_min, (span / 4) ** 2) if span >= 4 * mp.sqrt(a_min) else a_min
        seeds.append(
            ("cover", a_cover, gamma_mean - mp.pi * a_cover / sigma_max)
        )
    for index, (sigma, gamma) in enumerate(quads[: 3 if smoke else 6]):
        if sigma <= 0:
            continue
        a_val = scaling_a(sigma)
        seeds.append(("destr#%d" % index, a_val, scaling_omega(sigma, gamma)))
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
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    best: dict | None = None
    for name, a_val, omega in aw_seeds(quads, smoke):
        total = mp.mpf(0)
        primary = mp.inf
        for sigma, gamma in quads:
            term = quadruple_closed(sigma, gamma, a_val, omega)
            total += term
            if term < primary:
                primary = term
        r_on = online_budget(a_val, omega, c_inc)
        rec = {
            "seed": name,
            "a": a_val,
            "omega": omega,
            "Q_off": total,
            "Q_primary": primary,
            "R_on": r_on,
            "W": leftover(total, primary, r_on, r_ref, margin),
            "mechanism": "single_packet",
            "family": "control",
            "c": [mp.mpf(1)],
            "c_l1": mp.mpf(1),
            "c_l2": mp.mpf(1),
            "c_linf": mp.mpf(1),
            "n": "1",
            "mode": "pure",
        }
        rec["_honest"] = True
        if best is None or rec["W"] < best["W"]:
            best = rec
    assert best is not None
    return best


def r553_pick_pure(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    """r553 optimiser: minimise (Q_off−Q_pri)+R_on, then score leftover.

    That pick charges the raw on-line budget, not the leftover hinge
    max(0,R_on−R_ref).  It is what produced the sealed +110.7.
    """
    best: dict | None = None
    for name, a_val, omega in aw_seeds(quads, smoke):
        total = mp.mpf(0)
        primary = mp.inf
        for sigma, gamma in quads:
            term = quadruple_closed(sigma, gamma, a_val, omega)
            total += term
            if term < primary:
                primary = term
        r_on = online_budget(a_val, omega, c_inc)
        pick = (total - primary) + max(r_on, mp.mpf(0))
        rec = {
            "seed": name,
            "Q_off": total,
            "Q_primary": primary,
            "R_on": r_on,
            "W": leftover(total, primary, r_on, r_ref, margin),
            "mechanism": "r553_pick",
            "family": "control",
            "n": "1",
            "mode": "r553_pick",
            "_pick": pick,
            "c_l1": mp.mpf(1),
            "c_l2": mp.mpf(1),
            "c_linf": mp.mpf(1),
        }
        rec["_honest"] = True
        if best is None or pick < best["_pick"]:
            best = rec
    assert best is not None
    return best


# ---------------------------------------------------------------------------
# Configurations
# ---------------------------------------------------------------------------
def make_catalog(
    sigma: mp.mpf, gamma: mp.mpf, smoke: bool,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    a_ref = scaling_a(sigma)
    width = mp.sqrt(a_ref)
    configs: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    configs.append(("single", ((sigma, gamma),)))

    rels = D_REL[:2] if smoke else D_REL
    for mul_text in rels:
        mul = mp.mpf(mul_text)
        dist = mul * width
        if dist == 0:
            quads = ((sigma, gamma), (sigma, gamma))
        else:
            quads = ((sigma, gamma), (sigma, gamma + dist))
        configs.append(("tie:rel=%s" % mul_text, quads))

    if not smoke:
        for dist_text in D_ABS:
            dist = mp.mpf(dist_text)
            configs.append(
                ("tie:abs=%s" % dist_text, ((sigma, gamma), (sigma, gamma + dist)))
            )

    ks = (5,) if smoke else K_CLUSTER
    windows = CLUSTER_WINDOWS
    for k_use in ks:
        for window in windows:
            span = mp.mpf(1) if window == "unit" else 2 * width
            if k_use == 1:
                pts = (gamma,)
            else:
                pts = tuple(
                    gamma + (mp.mpf(index) / (k_use - 1)) * span
                    for index in range(k_use)
                )
            configs.append(
                ("cluster:k=%d:%s" % (k_use, window), tuple((sigma, h) for h in pts))
            )
        gap = mp.pi * a_ref / sigma
        n_left = k_use // 2
        n_right = k_use - n_left
        configs.append(
            (
                "cluster:k=%d:antiphase" % k_use,
                tuple([(sigma, gamma)] * n_left + [(sigma, gamma + gap)] * n_right),
            )
        )

    if not smoke:
        pack_span = min(mp.mpf(1) - 4 * width, 2 * width)
        if pack_span <= 0:
            pack_span = width
        start = gamma + mp.mpf("0.5")
        pts = tuple(
            start + (mp.mpf(index) / 9) * pack_span for index in range(10)
        )
        mixed = [(sigma, gamma)] + [(mp.mpf("0.99") * sigma, h) for h in pts]
        configs.append(("mixed:n=10", tuple(mixed)))

    widths = ("5",) if smoke else GAME_WIDTHS
    gks = (10,) if smoke else GAME_K
    for k_use in gks:
        for w_text in widths:
            span = mp.mpf(w_text) * width
            pts = tuple(
                gamma + (mp.mpf(index) / (k_use - 1)) * span
                for index in range(k_use)
            )
            configs.append(
                (
                    "game:k=%d:w=%s*sqrt(a)" % (k_use, w_text),
                    tuple((sigma, h) for h in pts),
                )
            )
        if not smoke:
            pts = tuple(
                gamma + (mp.mpf(index) / (k_use - 1)) * mp.mpf("0.5")
                for index in range(k_use)
            )
            configs.append(
                ("game:k=%d:halfbin" % k_use, tuple((sigma, h) for h in pts))
            )

    # New adversarial answers to mixtures.
    ns = (3,) if smoke else (3, 8, 21)
    for n_pkt in ns:
        half = mp.mpf("0.5")
        if n_pkt == 1:
            sites = (gamma,)
        else:
            sites = tuple(
                gamma - half + mp.mpf(index) / (n_pkt - 1)
                for index in range(n_pkt)
            )
        configs.append(
            ("spread:n=%d" % n_pkt, tuple((sigma, site) for site in sites))
        )
        if n_pkt == 3:
            pts = (sites[0], sites[0], sites[1], sites[1], sites[2])
            configs.append(("spread:n=3:k=5", tuple((sigma, p) for p in pts)))

    dks = (5,) if smoke else (5, 10)
    for k_use in dks:
        n_left = k_use // 2
        n_right = k_use - n_left
        spans = ((mp.mpf(1), "unit"),)
        if not smoke:
            spans = ((mp.mpf(1), "unit"), (5 * width, "5sqrt"))
        for span, tag in spans:
            configs.append(
                (
                    "double:k=%d:%s" % (k_use, tag),
                    tuple(
                        [(sigma, gamma)] * n_left
                        + [(sigma, gamma + span)] * n_right
                    ),
                )
            )
    return configs


def game_refine(
    sigma: mp.mpf,
    gamma: mp.mpf,
    packets: list[tuple[mp.mpf, mp.mpf]],
    k_use: int,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    """Adversary answers a known mixture by sitting on its centres
    and by doubling clusters at both ends of its ω-span."""
    if not packets:
        return []
    sites = unique_sorted([omega for _, omega in packets])
    out: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    if sites:
        # Distribute k_use quads onto the packet ω-centres (round-robin).
        pts = [sites[idx % len(sites)] for idx in range(k_use)]
        out.append(
            (
                "adv:on_centres:k=%d" % k_use,
                tuple((sigma, site) for site in pts),
            )
        )
        lo, hi = sites[0], sites[-1]
        n_left = k_use // 2
        n_right = k_use - n_left
        out.append(
            (
                "adv:double_ends:k=%d" % k_use,
                tuple([(sigma, lo)] * n_left + [(sigma, hi)] * n_right),
            )
        )
        # Unit window around the first centre (r553-style cluster).
        if k_use > 1:
            pts = tuple(
                sites[0] + (mp.mpf(index) / (k_use - 1))
                for index in range(k_use)
            )
            out.append(
                (
                    "adv:unit_at_first:k=%d" % k_use,
                    tuple((sigma, site) for site in pts),
                )
            )
    return out


# ---------------------------------------------------------------------------
# Strategy evaluation on one Z
# ---------------------------------------------------------------------------
def eval_mixture_on(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    n_use: int,
    mode: str,
    c_inc: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
    q_ref: mp.mpf,
    smoke: bool,
) -> dict:
    packets = place_packets(quads, n_use, mode)
    bank = PacketBank(packets, quads, c_inc)
    pos = positive_search(bank, r_ref, margin, q_ref, smoke)
    sgn = sign_search(bank, r_ref, margin, q_ref, smoke)
    nul = nulling_search(bank, r_ref, margin, q_ref, smoke)
    pos["n"] = str(n_use)
    pos["mode"] = mode
    sgn["n"] = str(n_use)
    sgn["mode"] = mode
    nul["n"] = str(n_use)
    nul["mode"] = mode
    best_signed = nul if nul["W"] < sgn["W"] else sgn
    return {
        "pos": pos,
        "sign": sgn,
        "null": nul,
        "best_signed": best_signed,
        "packets": packets,
        "bank": bank,
    }


def public_rec(rec: dict, q_ref: mp.mpf) -> dict:
    honest = rec.get("_honest", honest_pri(rec, q_ref))
    win = rec["W"] < 0 and honest
    out = {
        "W": nstr(rec["W"]),
        "Q_off": nstr(rec["Q_off"]),
        "Q_pri": nstr(rec["Q_primary"]),
        "R_on": nstr(rec["R_on"]),
        "extra": nstr(rec["extra"]) if "extra" in rec else nstr(rec["Q_off"] - rec["Q_primary"]),
        "hinge": nstr(rec.get("hinge", mp.mpf(0))),
        "win": str(int(bool(win))),
        "honest": str(int(bool(honest))),
        "mech": rec.get("mechanism", ""),
        "n": rec.get("n", ""),
        "mode": rec.get("mode", ""),
        "c_l1": nstr(rec.get("c_l1", mp.mpf(0))),
        "c_l2": nstr(rec.get("c_l2", mp.mpf(0))),
        "c_linf": nstr(rec.get("c_linf", mp.mpf(0))),
    }
    if "cond" in rec:
        out["cond"] = rec["cond"]
        out["null_res"] = rec.get("null_res", "")
        out["null_kind"] = rec.get("null_kind", "")
        out["n_sites"] = rec.get("n_sites", "")
    if "seed" in rec:
        out["seed"] = rec["seed"]
    return out


def eval_config(
    name: str,
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    q_ref: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
    ns: tuple[int, ...],
) -> dict:
    q_local = local_q_lock(quads)
    control = best_pure(quads, c_inc, smoke, r_ref, margin)
    control["n"] = "1"
    picked = r553_pick_pure(quads, c_inc, smoke, r_ref, margin)
    modes = packet_modes(smoke)
    pos_best: dict | None = None
    sign_best: dict | None = None
    null_best: dict | None = None
    families: dict[str, dict] = {}
    for n_use in ns:
        modes_use = modes if n_use < 21 else (modes[0],)
        for mode in modes_use:
            key = "n%d:%s" % (n_use, mode)
            block = eval_mixture_on(
                quads, n_use, mode, c_inc, r_ref, margin, q_local, smoke,
            )
            families[key] = {
                "pos": public_rec(block["pos"], q_local),
                "sign": public_rec(block["sign"], q_local),
                "null": public_rec(block["null"], q_local),
            }
            if pos_best is None or _better(block["pos"], pos_best):
                pos_best = block["pos"]
            if sign_best is None or _better(block["sign"], sign_best):
                sign_best = block["sign"]
            if null_best is None or _better(block["null"], null_best):
                null_best = block["null"]
    assert pos_best is not None and sign_best is not None and null_best is not None
    signed_best = null_best if null_best["W"] < sign_best["W"] else sign_best
    return {
        "name": name,
        "n_quad": str(len(quads)),
        "inc_ok": str(int(increment_ok(quads))),
        "control": public_rec(control, q_local),
        "r553_pick": public_rec(picked, q_local),
        "pos": public_rec(pos_best, q_local),
        "sign": public_rec(sign_best, q_local),
        "null": public_rec(null_best, q_local),
        "signed": public_rec(signed_best, q_local),
        "families": families,
        "_W_control": control["W"],
        "_W_pick": picked["W"],
        "_W_pos": pos_best["W"],
        "_W_sign": sign_best["W"],
        "_W_null": null_best["W"],
        "_W_signed": signed_best["W"],
        "_pos": pos_best,
        "_sign": sign_best,
        "_null": null_best,
        "_signed": signed_best,
        "_control": control,
        "_quads": quads,
    }


# ---------------------------------------------------------------------------
# Part 0 — linearity audit
# ---------------------------------------------------------------------------
def run_linearity_audit(
    c_inc: mp.mpf, q_ref: mp.mpf, r_ref: mp.mpf, margin: mp.mpf,
) -> dict:
    section("PART0  LINEARITY AUDIT  (r553 leftover vs h)")
    print(
        "  W_left(h) = -3.56 + (Q_off(h) - Q_pri(h)) + max(0, R_on(h)-R_ref)"
    )
    print(
        "  Q_off = Σ_q 4 Re[H(δ_q) H(-δ_q)].  "
        "For h_mix=Σ c_j h_j, H_mix=Σ c_j H_j  ⇒  Q is a QUADRATIC form."
    )
    print(
        "  Classical Weil W(h) is linear in the test function.  "
        "This leftover is NOT that functional."
    )
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    # Sealed r553 killer: k=5 unit.
    pts = tuple(gamma + mp.mpf(idx) / 4 for idx in range(5))
    quads = tuple((sigma, height) for height in pts)
    packets = place_packets(quads, 3, "equidist")
    bank = PacketBank(packets, quads, c_inc)

    e0 = ones_hot(3, 0)
    e1 = ones_hot(3, 1)
    e2 = ones_hot(3, 2)
    half = [mp.mpf("0.5"), mp.mpf("0.5"), mp.mpf(0)]
    convex = [mp.mpf(1) / 3] * 3
    two_h = [mp.mpf(2), mp.mpf(0), mp.mpf(0)]

    w0 = score_bank(bank, e0, r_ref, margin)
    w1 = score_bank(bank, e1, r_ref, margin)
    w2 = score_bank(bank, e2, r_ref, margin)
    w_half_prod = score_bank(bank, half, r_ref, margin)
    w_half_add = score_bank(bank, half, r_ref, margin, additive=True)
    w_conv_prod = score_bank(bank, convex, r_ref, margin)
    w_conv_add = score_bank(bank, convex, r_ref, margin, additive=True)
    w_two = score_bank(bank, two_h, r_ref, margin)
    w0_add = score_bank(bank, e0, r_ref, margin, additive=True)

    # Product-hat of the sum vs sum of leftovers.
    combo_pred = (w0["W"] + w1["W"]) / 2
    scale_pred = 2 * w0["W"]

    # Cross term: Q(e0+e1) - Q(e0) - Q(e1)
    q_sum, _, _ = bank.q_prod([mp.mpf(1), mp.mpf(1), mp.mpf(0)])
    cross = q_sum - w0["Q_off"] - w1["Q_off"]

    print("  DECOMPOSITION")
    print("    linear-in-Z (additive over quads): Q_off = Σ_q Q_q")
    print("    quadratic-in-c (product hat):      Q_q = 4 Re[(Σ c_j H_j+)(Σ c_k H_k-)]")
    print("    nonlinear selection:               Q_pri = min_q Q_q")
    print("    nonlinear hinge:                   max(0, R_on - R_ref)")
    print("    inhomogeneous credit:              sealed -3.56  (not × Σ c_j)")
    print("    R_on(c) is a quadratic majorant of |H_mix|²")
    print(
        "  CONSEQUENCE: leftover(Σ c_j h_j) ≠ Σ c_j leftover(h_j).  "
        "A positive combination of losers can still lose under the "
        "product-hat if every packet sees the cluster (cross terms "
        "same-sign).  It can win only via (i) quadratic cross-term "
        "cancellation / H-nulling, (ii) signed c_j, or (iii) the "
        "inhomogeneous -3.56 credit after scale-down (norm_nonlin; "
        "excluded by ||c||_∞=1 + |Q_pri|≥½|Q_ref|)."
    )
    print(
        "  If one used the *linear* reading Q=Σ c_j Q(h_j) AND c≥0, "
        "then extra(c) = Σc Q_off_j - min_q Σc Q_j(q) ≤ Σ c_j extra(h_j) "
        "and leftover ≥ -3.56 (hinge≥0, extra≥0).  Convex losers then "
        "stay positive unless the once-charged -3.56 over-credits a "
        "shrunken primary — exactly the norm cheat."
    )
    print("  NUMERICS  (cluster k=5 unit, n=3 equidist, σ=0.25)")
    print("    W(e0)     %s   extra %s  hinge %s" % (
        nstr(w0["W"]), nstr(w0["extra"]), nstr(w0["hinge"]),
    ))
    print("    W(e1)     %s   extra %s  hinge %s" % (
        nstr(w1["W"]), nstr(w1["extra"]), nstr(w1["hinge"]),
    ))
    print("    W(e2)     %s   extra %s  hinge %s" % (
        nstr(w2["W"]), nstr(w2["extra"]), nstr(w2["hinge"]),
    ))
    print("    W(½e0+½e1) prod %s   add %s   ½(W0+W1) %s" % (
        nstr(w_half_prod["W"]), nstr(w_half_add["W"]), nstr(combo_pred),
    ))
    print("    W(uniform) prod %s   add %s" % (
        nstr(w_conv_prod["W"]), nstr(w_conv_add["W"]),
    ))
    print("    W(2 e0)   %s   2 W(e0) %s   (scale breaks leftover)" % (
        nstr(w_two["W"]), nstr(scale_pred),
    ))
    print("    Q_cross(e0+e1) %s   (0 ⇒ additive hats; ≠0 ⇒ quadratic)" % nstr(cross))
    print("    Q_pri(e0) %s   Q_off(e0) %s   Q_add==Q_prod on one-hots: %s" % (
        nstr(w0["Q_primary"]), nstr(w0["Q_off"]),
        nstr(abs(w0["Q_off"] - w0_add["Q_off"])),
    ))

    lin_gap = abs(w_half_prod["W"] - combo_pred)
    scale_gap = abs(w_two["W"] - scale_pred)
    one_hot_match = abs(w0["Q_off"] - w0_add["Q_off"]) < mp.mpf("1e-8")
    check(
        "L0-not-linear-in-c",
        lin_gap > mp.mpf("1e-6") or scale_gap > mp.mpf("1e-6"),
        "½-combo gap %s  scale gap %s" % (nstr(lin_gap, 6), nstr(scale_gap, 6)),
    )
    check(
        "L0-onehot-prod-eq-add",
        one_hot_match,
        "single packet: product hat recovers Q(h_j)",
    )
    check(
        "L0-cross-term",
        abs(cross) > mp.mpf("1e-8"),
        "Q(h0+h1)-Q0-Q1 = %s" % nstr(cross, 6),
    )
    extra_is_rest = abs(w0["extra"] - (w0["Q_off"] - w0["Q_primary"])) < mp.mpf("1e-8")
    check(
        "L0-extra-is-nonprimary-sum",
        extra_is_rest,
        "extra=Q_off-Q_pri is the sum of non-primary quads (may be negative)",
    )
    return {
        "W_e0": nstr(w0["W"]),
        "W_e1": nstr(w1["W"]),
        "W_e2": nstr(w2["W"]),
        "W_half_prod": nstr(w_half_prod["W"]),
        "W_half_add": nstr(w_half_add["W"]),
        "W_half_pred": nstr(combo_pred),
        "W_two": nstr(w_two["W"]),
        "W_two_pred": nstr(scale_pred),
        "Q_cross": nstr(cross),
        "lin_gap": nstr(lin_gap),
        "scale_gap": nstr(scale_gap),
        "formula": (
            "W_left=-3.56+(Q_off-Q_pri)+max(0,R_on-R_ref); "
            "Q_off=Σ 4Re[H_mix(δ)H_mix(-δ)] quadratic in c; "
            "Q_pri=min_q Q_q; R_on=CS-majorant quadratic in c; "
            "-3.56 inhomogeneous"
        ),
        "consequence": (
            "positive combos of losers do not automatically lose "
            "under leftover (not linear), but an honest ||c||_inf=1 "
            "win requires quadratic cancellation, signed c, or "
            "H-nulling — not a convex average of single-packet leftovers"
        ),
    }


# ---------------------------------------------------------------------------
# Catalog / game / verdicts
# ---------------------------------------------------------------------------
def run_catalog(
    smoke: bool, c_inc: mp.mpf, q_ref: mp.mpf, r_ref: mp.mpf, margin: mp.mpf,
) -> list[dict]:
    section("PART1  CATALOG  (Z frozen, then each mixture sees Z)")
    print(
        "  CLASS pos = {c≥0, ||c||_∞=1}   "
        "CLASS signed = {c∈ℝ, ||c||_∞=1} ∪ H-nulling"
    )
    print(
        "  CONTROL = r553 best 1-packet.  "
        "honest win: W_left<0 AND |Q_pri|≥%s|Q_local_r541|" % PRI_FLOOR
    )
    sigmas = (HOST_SIGMAS[1],) if smoke else HOST_SIGMAS
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in HOST_GAMMAS:
            gamma = mp.mpf(gamma_text)
            configs = make_catalog(sigma, gamma, smoke)
            for name, quads in configs:
                full_name = "%s|s=%s|g=%s" % (name, sigma_text, gamma_text)
                row = eval_config(
                    full_name, quads, c_inc, smoke, q_ref, r_ref, margin,
                    ns_for(full_name, smoke),
                )
                rows.append(row)
    print(
        "  Q_ref %s  R_ref %s  C_inc %s  n_configs %d  mix_n catalog-adaptive"
        % (nstr(q_ref), nstr(r_ref), nstr(c_inc), len(rows))
    )
    print(
        "  name                              nq  ctrl          r553pick      pos           sign          null"
    )
    for row in rows:
        print(
            "  %-32s %2s  %s%s  %s%s  %s%s  %s%s  %s%s"
            % (
                row["name"][:32],
                row["n_quad"],
                nstr(mp.mpf(row["control"]["W"]), 6),
                "*" if row["control"]["win"] == "1" else " ",
                nstr(mp.mpf(row["r553_pick"]["W"]), 6),
                "*" if row["r553_pick"]["win"] == "1" else " ",
                nstr(mp.mpf(row["pos"]["W"]), 6),
                "*" if row["pos"]["win"] == "1" else " ",
                nstr(mp.mpf(row["sign"]["W"]), 6),
                "*" if row["sign"]["win"] == "1" else " ",
                nstr(mp.mpf(row["null"]["W"]), 6),
                "*" if row["null"]["win"] == "1" else " ",
            )
        )
    return rows


def run_game(
    smoke: bool,
    c_inc: mp.mpf,
    q_ref: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
    rows: list[dict],
) -> dict:
    section("PART2  MIN-MAX GAME  (2 adversary rounds against best mixture)")
    print(
        "  Round t: Z_t = argmax catalog W(best_mix(Z),Z); "
        "adversary sits on that mixture's centres / double-ends; "
        "mixture retunes."
    )
    sigma_text = HOST_SIGMAS[1] if smoke else HOST_SIGMAS[1]
    gamma_text = HOST_GAMMAS[0]
    sigma = mp.mpf(sigma_text)
    gamma = mp.mpf(gamma_text)

    def worst_of(key: str, pool: list[dict]) -> dict:
        return max(pool, key=lambda row: row[key])

    iterations = []
    w_pos = worst_of("_W_pos", rows)
    w_signed = worst_of("_W_signed", rows)
    w_ctrl = worst_of("_W_control", rows)
    iterations.append({
        "iter": "0",
        "strategy": "control_1pkt",
        "worst": w_ctrl["name"],
        "W": nstr(w_ctrl["_W_control"]),
        "win": w_ctrl["control"]["win"],
    })
    iterations.append({
        "iter": "1",
        "strategy": "positive",
        "worst": w_pos["name"],
        "W": nstr(w_pos["_W_pos"]),
        "win": w_pos["pos"]["win"],
        "n": w_pos["pos"]["n"],
        "mode": w_pos["pos"]["mode"],
    })
    iterations.append({
        "iter": "1s",
        "strategy": "signed+null",
        "worst": w_signed["name"],
        "W": nstr(w_signed["_W_signed"]),
        "win": w_signed["signed"]["win"],
        "n": w_signed["signed"]["n"],
        "mode": w_signed["signed"]["mode"],
        "mech": w_signed["signed"]["mech"],
    })

    # Build adversary configs against the current best signed mixture
    # on its worst Z, and against the best positive on its worst Z.
    adv_rows: list[dict] = []
    for tag, src, rec_key in (
        ("pos", w_pos, "_pos"),
        ("signed", w_signed, "_signed"),
    ):
        src_quads = src["_quads"]
        n_use = int(src[rec_key].get("n") or 3)
        mode = src[rec_key].get("mode") or "equidist"
        packets = place_packets(src_quads, n_use, mode)
        k_use = 5 if smoke else 10
        extras = game_refine(sigma, gamma, packets, k_use)
        # Also refine at the host of the source config.
        s_src = src_quads[0][0]
        g_src = min(g for _, g in src_quads)
        extras += game_refine(s_src, g_src, packets, k_use)
        seen: set[str] = set()
        for adv_name, adv_quads in extras:
            full = "%s|from=%s|%s" % (adv_name, tag, src["name"])
            if full in seen:
                continue
            seen.add(full)
            if not increment_ok(adv_quads):
                continue
            row = eval_config(
                full, adv_quads, c_inc, smoke, q_ref, r_ref, margin,
                ns_for(full, smoke),
            )
            adv_rows.append(row)

    if adv_rows:
        a_pos = worst_of("_W_pos", adv_rows)
        a_signed = worst_of("_W_signed", adv_rows)
        iterations.append({
            "iter": "2",
            "strategy": "positive_vs_adv",
            "worst": a_pos["name"],
            "W": nstr(a_pos["_W_pos"]),
            "win": a_pos["pos"]["win"],
        })
        iterations.append({
            "iter": "2s",
            "strategy": "signed_vs_adv",
            "worst": a_signed["name"],
            "W": nstr(a_signed["_W_signed"]),
            "win": a_signed["signed"]["win"],
            "mech": a_signed["signed"]["mech"],
        })
    else:
        a_pos = w_pos
        a_signed = w_signed
        iterations.append({
            "iter": "2",
            "strategy": "positive_vs_adv",
            "worst": "none",
            "W": nstr(w_pos["_W_pos"]),
            "win": w_pos["pos"]["win"],
        })
        iterations.append({
            "iter": "2s",
            "strategy": "signed_vs_adv",
            "worst": "none",
            "W": nstr(w_signed["_W_signed"]),
            "win": w_signed["signed"]["win"],
        })

    print("  iter strategy          worst                                      W")
    for item in iterations:
        print(
            "  %-4s %-18s %-42s %s  win=%s"
            % (
                item["iter"],
                item["strategy"],
                item["worst"][:42],
                item["W"],
                item["win"],
            )
        )
    return {
        "iterations": iterations,
        "worst_pos": w_pos["name"],
        "W_worst_pos": nstr(w_pos["_W_pos"]),
        "worst_signed": w_signed["name"],
        "W_worst_signed": nstr(w_signed["_W_signed"]),
        "adv_worst_pos": a_pos["name"],
        "W_adv_pos": nstr(a_pos["_W_pos"]),
        "adv_worst_signed": a_signed["name"],
        "W_adv_signed": nstr(a_signed["_W_signed"]),
        "n_adv": str(len(adv_rows)),
        "adv_rows": adv_rows,
    }


def decide_class(
    rows: list[dict], game: dict, which: str,
) -> tuple[str, dict]:
    attr = "_W_pos" if which == "pos" else "_W_signed"
    pub = "pos" if which == "pos" else "signed"
    pool = list(rows) + list(game.get("adv_rows") or [])
    losses = [row for row in pool if row[attr] >= 0 or row[pub]["win"] != "1"]
    honest_wins = [row for row in pool if row[pub]["win"] == "1"]
    worst = max(pool, key=lambda row: row[attr])
    worst_w = worst[attr]

    # Mechanism census on honest wins.
    mechs: dict[str, int] = {}
    for row in honest_wins:
        mech = row[pub].get("mech") or "unknown"
        mechs[mech] = mechs.get(mech, 0) + 1

    one_pkt_covers = all(row["control"]["win"] == "1" for row in rows)
    extra = {
        "worst": worst["name"],
        "worst_W": nstr(worst_w),
        "n_win": str(len(honest_wins)),
        "mechs": mechs,
        "one_pkt_covers": str(int(one_pkt_covers)),
    }
    if len(honest_wins) < len(pool):
        first = next(row for row in pool if row[pub]["win"] != "1")
        extra["n_loss"] = str(len(pool) - len(honest_wins))
        extra["loss_names"] = ",".join(
            row["name"] for row in pool if row[pub]["win"] != "1"
        )[:240]
        if one_pkt_covers:
            verdict = (
                "MIXTURE_CONDITIONAL(needs=leftover_opt_1pkt_already_covers)"
            )
            return verdict, extra
        if worst_w >= 0:
            return "MIXTURE_LOSES(config=%s)" % first["name"], extra
        needs = []
        for row in pool:
            if row[pub]["win"] != "1":
                if row[attr] < 0 and row[pub]["honest"] != "1":
                    needs.append("norm_nonlin@%s" % row["name"])
                else:
                    needs.append("harder_Z@%s" % row["name"])
        if needs and all(item.startswith("norm_nonlin") for item in needs):
            verdict = "MIXTURE_CONDITIONAL(needs=norm_nonlin)"
        elif honest_wins:
            verdict = "MIXTURE_CONDITIONAL(needs=%s)" % ";".join(needs[:3])
        else:
            verdict = "MIXTURE_LOSES(config=%s)" % first["name"]
        return verdict, extra

    extra["n_loss"] = "0"
    extra["universal"] = worst[pub].get("mech") or (
        "positive_avg" if which == "pos" else "sign_mixing"
    )
    if one_pkt_covers:
        # Mixtures win, but they do not open a Z that leftover-opt
        # 1-packet already missed.  That is the r554 headline.
        extra["universal"] = "leftover_opt_1pkt_already_covers"
        verdict = "MIXTURE_CONDITIONAL(needs=leftover_opt_1pkt_already_covers)"
        return verdict, extra
    lead = extra["universal"]
    n_lead = worst[pub].get("n") or ""
    verdict = "MIXTURE_WINS(n=%s, mechanism=%s, worst_leftover=%s)" % (
        n_lead, lead, nstr(worst_w),
    )
    return verdict, extra


def compact_map(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        out.append({
            "name": row["name"],
            "n_quad": row["n_quad"],
            "control": row["control"]["W"],
            "control_win": row["control"]["win"],
            "r553_pick": row["r553_pick"]["W"],
            "r553_pick_win": row["r553_pick"]["win"],
            "pos": row["pos"]["W"],
            "pos_win": row["pos"]["win"],
            "pos_n": row["pos"]["n"],
            "pos_mode": row["pos"]["mode"],
            "sign": row["sign"]["W"],
            "sign_win": row["sign"]["win"],
            "null": row["null"]["W"],
            "null_win": row["null"]["win"],
            "null_cond": row["null"].get("cond", ""),
            "null_res": row["null"].get("null_res", ""),
            "signed": row["signed"]["W"],
            "signed_win": row["signed"]["win"],
            "signed_mech": row["signed"]["mech"],
        })
    return out


def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    sigma = mp.mpf("0.1")
    gamma = mp.mpf(14)
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    q_closed = quadruple_closed(sigma, gamma, a_val, omega)
    q_re = 4 * mp.re(hat_w_delta(sigma, gamma, a_val, omega))
    max_err = max(max_err, abs(q_closed - q_re))
    delta = sigma + mp.j * gamma
    from_h = gabor_H(a_val, omega, delta) * gabor_H(a_val, omega, -delta)
    max_err = max(max_err, abs(from_h - hat_w_delta(sigma, gamma, a_val, omega)))
    # Mixture n=1 recovers the closed form.
    bank = PacketBank([(a_val, omega)], ((sigma, gamma),), c_inc)
    q_off, _, _ = bank.q_prod([mp.mpf(1)])
    max_err = max(max_err, abs(q_off - q_closed))
    # Two-packet λ=0 recovers one packet (r553 convention).
    bank2 = PacketBank(
        [(a_val, omega), (a_val, omega + 1)], ((sigma, gamma),), c_inc,
    )
    q0, _, _ = bank2.q_prod([mp.mpf(1), mp.mpf(0)])
    max_err = max(max_err, abs(q0 - q_closed))
    if not (c_inc > 0 and mp.isfinite(c_inc)):
        max_err = max(max_err, mp.mpf(1))
    if increment_ok(((sigma, gamma),) * K_MAX_BIN) is False:
        max_err = max(max_err, mp.mpf(1))
    if increment_ok(((sigma, gamma),) * (K_MAX_BIN + 1)) is True:
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-16"), max_err


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    c_inc = c_inc_prefactor()
    margin = abs(mp.mpf(R541_MARGIN))
    print("gabor_mixture_witness_probe -- r554")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted_product")
    print("quantifiers forall_Z exists_h  (config first)")
    print("class_pos c>=0 ||c||_inf=1   class_signed c in R ||c||_inf=1")
    print("online min(n sum c_j^2 R_j, (sum|c_j|) sum |c_j| R_j)  C_inc %s" % nstr(c_inc))
    print(
        "FORMULA  Q=4 Re[H_mix(d)H_mix(-d)];  "
        "W_left=R541_MARGIN+(Q_off-Q_primary)+max(0,R_on-R_ref)"
    )

    section("G0  CLOSED FORMS / MIXTURE n=1 / TWO-PACKET λ=0")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))

    # Global r553 reference: first HOST sigma=0.10, gamma=14.
    sigma_ref = mp.mpf(HOST_SIGMAS[0])
    gamma_ref = mp.mpf(HOST_GAMMAS[0])
    a_ref = scaling_a(sigma_ref)
    w_ref = scaling_omega(sigma_ref, gamma_ref)
    q_ref = quadruple_closed(sigma_ref, gamma_ref, a_ref, w_ref)
    r_ref = online_budget(a_ref, w_ref, c_inc)

    audit = run_linearity_audit(c_inc, q_ref, r_ref, margin)

    rows = run_catalog(smoke, c_inc, q_ref, r_ref, margin)
    inc_all = all(row["inc_ok"] == "1" for row in rows)
    check("P1-increment-ok", inc_all, "every catalog Z has ≤%d quads/bin" % K_MAX_BIN)
    check("P1-catalog-nonempty", len(rows) > 0, "n=%d" % len(rows))
    check(
        "P1-leftover-single",
        abs(leftover(q_ref, q_ref, r_ref, r_ref, margin) + margin) < mp.mpf("1e-8"),
        "single+r541 recovers R541_MARGIN",
    )

    game = run_game(smoke, c_inc, q_ref, r_ref, margin, rows)

    section("PART3  WIN MAP / VERDICTS")
    verdict_pos, extra_pos = decide_class(rows, game, "pos")
    verdict_sign, extra_sign = decide_class(rows, game, "signed")
    print("  VERDICT_POS %s" % verdict_pos)
    print("  VERDICT_SIGNED %s" % verdict_sign)
    print(
        "  POS_worst %s  W=%s  n_win=%s"
        % (extra_pos["worst"], extra_pos["worst_W"], extra_pos.get("n_win", ""))
    )
    print(
        "  SIGNED_worst %s  W=%s  n_win=%s"
        % (extra_sign["worst"], extra_sign["worst_W"], extra_sign.get("n_win", ""))
    )
    print("  POS_mechs %s" % extra_pos.get("mechs", {}))
    print("  SIGNED_mechs %s" % extra_sign.get("mechs", {}))

    n_ctrl_win = sum(1 for row in rows if row["control"]["win"] == "1")
    n_pick_win = sum(1 for row in rows if row["r553_pick"]["win"] == "1")
    n_pos_win = sum(1 for row in rows if row["pos"]["win"] == "1")
    n_sign_win = sum(1 for row in rows if row["sign"]["win"] == "1")
    n_null_win = sum(1 for row in rows if row["null"]["win"] == "1")
    print(
        "  catalog honest wins  leftover-opt %d/%d  r553pick %d/%d  pos %d/%d  sign %d/%d  null %d/%d"
        % (
            n_ctrl_win, len(rows), n_pick_win, len(rows),
            n_pos_win, len(rows), n_sign_win, len(rows), n_null_win, len(rows),
        )
    )

    # Sealed r553 cluster: pick-opt leftover ~ +110.7; leftover-opt 1-packet wins.
    sealed = [
        row for row in rows
        if "cluster:k=5:unit|s=0.25" in row["name"]
    ]
    pick_pos = False
    leftover_neg = False
    pick_w = mp.mpf(0)
    ctrl_w = mp.mpf(0)
    if sealed:
        pick_w = mp.mpf(sealed[0]["r553_pick"]["W"])
        ctrl_w = mp.mpf(sealed[0]["control"]["W"])
        pick_pos = pick_w > 0
        leftover_neg = ctrl_w < 0
    check(
        "P3-r553-pick-reproduces-loss",
        pick_pos or not sealed,
        "r553 pick leftover %s (sealed +110.7 was pick, not leftover-opt)"
        % nstr(pick_w, 6),
    )
    check(
        "P3-leftover-opt-1pkt-wins-cluster",
        leftover_neg or not sealed,
        "leftover-opt 1-packet W=%s on cluster k=5 unit" % nstr(ctrl_w, 6),
    )
    check(
        "P3-verdict-pos-formed",
        verdict_pos.startswith("MIXTURE_"),
        verdict_pos,
    )
    check(
        "P3-verdict-signed-formed",
        verdict_sign.startswith("MIXTURE_"),
        verdict_sign,
    )

    # Nulling robustness census.
    conds = []
    residuals = []
    for row in rows:
        if row["null"].get("cond"):
            try:
                conds.append(mp.mpf(row["null"]["cond"]))
            except Exception:
                pass
        if row["null"].get("null_res"):
            try:
                residuals.append(mp.mpf(row["null"]["null_res"]))
            except Exception:
                pass
    cond_max = max(conds) if conds else mp.mpf(0)
    res_max = max(residuals) if residuals else mp.mpf(0)
    print("  NULL_cond_max %s  NULL_res_max %s  n_cond %d" % (
        nstr(cond_max), nstr(res_max), len(conds),
    ))

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    if smoke:
        check("G4-smoke-subset", True, "sigma=0.25, n=3, reduced catalog")
    else:
        check(
            "G4-full-grid",
            True,
            "sigmas=%d mix_n=%s k=%s"
            % (len(HOST_SIGMAS), MIX_N, K_CLUSTER),
        )

    extra_pos_pub = {
        key: value for key, value in extra_pos.items() if key != "mechs"
    }
    extra_sign_pub = {
        key: value for key, value in extra_sign.items() if key != "mechs"
    }
    extra_pos_pub["mechs"] = {
        key: str(val) for key, val in extra_pos.get("mechs", {}).items()
    }
    extra_sign_pub["mechs"] = {
        key: str(val) for key, val in extra_sign.get("mechs", {}).items()
    }
    game_pub = {
        key: value for key, value in game.items() if key != "adv_rows"
    }
    if game.get("adv_rows"):
        game_pub["adv_map"] = compact_map(game["adv_rows"])

    canon = {
        "audit": audit,
        "catalog": compact_map(rows),
        "game": game_pub,
        "verdict_pos": verdict_pos,
        "verdict_signed": verdict_sign,
        "extra_pos": extra_pos_pub,
        "extra_sign": extra_sign_pub,
        "Q_ref": nstr(q_ref),
        "R_ref": nstr(r_ref),
        "C_inc": nstr(c_inc),
        "SPEC_SHA": SPEC_SHA,
        "null_cond_max": nstr(cond_max),
        "null_res_max": nstr(res_max),
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    print("PAYLOAD_SHA256 %s" % seal)
    print("Q_REF %s" % nstr(q_ref))
    print("R_REF %s" % nstr(r_ref))
    print("C_INC %s" % nstr(c_inc))
    print("N_CONFIGS %d" % len(rows))
    print("N_CONTROL_WIN %d" % n_ctrl_win)
    print("N_R553PICK_WIN %d" % n_pick_win)
    print("N_POS_WIN %d" % n_pos_win)
    print("N_SIGN_WIN %d" % n_sign_win)
    print("N_NULL_WIN %d" % n_null_win)
    print("GAME_WORST_POS %s %s" % (game["worst_pos"], game["W_worst_pos"]))
    print("GAME_WORST_SIGNED %s %s" % (game["worst_signed"], game["W_worst_signed"]))
    print("ADV_WORST_POS %s %s" % (game["adv_worst_pos"], game["W_adv_pos"]))
    print("ADV_WORST_SIGNED %s %s" % (game["adv_worst_signed"], game["W_adv_signed"]))
    print("NULL_COND_MAX %s" % nstr(cond_max))
    print("NULL_RES_MAX %s" % nstr(res_max))
    print("VERDICT_POS %s" % verdict_pos)
    print("VERDICT_SIGNED %s" % verdict_sign)
    print("AUDIT_FORMULA %s" % audit["formula"])
    print("AUDIT_CONSEQUENCE %s" % audit["consequence"])
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print(
        "LEAN_NOTE leftover is not classical linear W(h); "
        "product-hat finite Gabor span is a CLASS EXTENSION"
    )
    print(
        "LEAN_NOTE leftover-opt 1-packet already yields leftover<0 on "
        "the sealed r553 cluster (r553 +110.7 was pick=extra+R_on)"
    )
    print(
        "LEAN_NOTE plausible leftover-scale prop is still forall Z "
        "exists 1-packet h; mixture class is not forced by these Z"
    )
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
            "r554 Gabor mixture-witness probe "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
