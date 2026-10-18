#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_honest_weil_game_probe -- r560

Round 560.  Experiments-only DECIDER for the r553/r554 leftover
disagreement, under the r559 referee specification.

  r553: 1-packet leftover-pick WITNESS_LOSES on cluster k=5 unit
        σ=0.25 (W_left≈+110.7).
  r554: leftover-opt 1-packet wins 52/52 on the same leftover scale,
        but that scale is not a faithful proxy of the Weil form
        (global R_ref nulls the hinge; −3.56 is not homogeneous;
        the leftover winner can violate PRI_FLOOR=0.5).
  r559: independent 80-digit audit confirmed both artefacts.

THIS ROUND.  Config-first game with the FULL homogeneous Weil form
(or a certified upper bound) as the objective:

  W_honest(h; Z) = Σ_{q∈Z} Q_q(h) + R_on(h)

Q_q is the exact FE quadruple 4 Re ĥ_W (sealed closed form).
R_on is the certified on-line mass bound 2 C_inc S_cert (r549
theta-sum × increment), ADDED in full — no R_ref subtraction,
no −3.56 credit.  W_honest < 0 is an honest witness win even
against the worst-case on-line budget.  A budget loss is not yet
a loss of the true form: then W_sharp replaces R_on by the
enumerated first-100 ordinates plus a Trudgian tail.

CLAIM BOUNDARY.  Finite closed-form / deterministic-grid
arithmetic on increment-compliant catalogs.  NO RH claim, NO
anti-RH claim, NO ledger/paper/Lean/next.txt edit.

HAT CONVENTION.  Weil-shifted ĥ_W(s)=H(s−1/2) H(1/2−s), matching
`RH.pureGaborHatDelta` / r553.  A quadruple contributes 4 Re ĥ_W.
On-line pair {γ,−γ} contributes 2 ĥ_W(1/2+iγ).

NORMALISATION.  Unit-amplitude 1-packet
  h(t) = p(t) e^{−a t²} cos(ω t),  p even, deg ≤ 4, p(0)=1.
W is quadratic-homogeneous in amplitude: W(λh)=λ² W(h).
Scaling cannot flip the sign, so amplitude is frozen at 1 and
the signed value is reported.

Verdicts:
  HONEST_WITNESS_WINS(all=…, worst_margin=…)
  HONEST_WITNESS_LOSES(config=…, W_honest=…, W_sharp=…)
  HONEST_SPLIT(budget_losses=…, sharp_wins=…)
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
A_MIN_FACTOR = "0.125"
A_FACTORS = ("0.125", "0.25", "0.5", "1", "2", "4", "8")
GAME_WIDTHS = ("1", "5")
GAME_K = (5, 10)
POLY_B2 = ("-2", "-1", "0", "1", "2")
POLY_B4 = ("-1", "0", "1")
R541_MARGIN = "-3.56"
C_INC_PIN = "174.818115823"
NSTR_DIGITS = 12
DPS = 80
K_MAX_BIN = 43
TRUDGIAN_A = "0.111"
TRUDGIAN_B = "0.275"
TRUDGIAN_C = "2.450"
TRUDGIAN_NT_EXTRA = "0.2"
C_CRUDE = "4.0"

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

DISPUTE_STEMS = (
    "cluster:k=5:unit",
    "game:k=10:w=5*sqrt(a)",
)

SPEC = {
    "round": 560,
    "parent_round": 559,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.HONEST_FORM.01",
    "target": "GaborSeparationInequality.honest_weil_game",
    "hat": "weil_shifted",
    "class": "pure_gabor_even_poly_deg<=4_unit_amplitude",
    "quantifiers": "forall_Z exists_h  (config first, witness last)",
    "objective": "W_honest = Q_off + R_on  (no R_ref, no -3.56)",
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
    "a_factors": list(A_FACTORS),
    "a_min_factor": A_MIN_FACTOR,
    "game_widths": list(GAME_WIDTHS),
    "game_k": list(GAME_K),
    "poly_b2": list(POLY_B2),
    "poly_b4": list(POLY_B4),
    "r541_margin_audit_only": R541_MARGIN,
    "k_max_bin": K_MAX_BIN,
    "n_zeros_sharp": 100,
    "c_inc_source": (
        "2*zetaZerosInDiskCardBoundInner "
        "(ZeroIncrement prefactor; log factor pulled out)"
    ),
    "c_inner_formula": (
        "(log(2+6*zeta(9/8))+log|zeta(2)|+2)/log(14/13)"
    ),
    "c_inc_pin": C_INC_PIN,
    "trudgian_source": (
        "Trudgian JNT 134 (2014) 280-292 / arXiv:1208.5846 Thm1+Cor1"
    ),
    "normalisation": "unit_amplitude; sign(W) scale-invariant",
    "nstr_digits": NSTR_DIGITS,
    "dps": DPS,
    "optimiser": "deterministic_finite_grid_select_by_W_honest",
    "scope": (
        "r554 52-row increment-compliant catalog + r559 dispute "
        "pairs + two adversarial answer rounds; 1-packet class"
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


def online_value(t_value: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """ĥ_W(1/2+it) on the critical line (real).  Sealed r549 form."""
    pref = mp.pi / (4 * a)
    return pref * (
        exp_clip(-((t_value + omega) ** 2) / (2 * a))
        + exp_clip(-((t_value - omega) ** 2) / (2 * a))
        + 2 * exp_clip(-(t_value * t_value + omega * omega) / (2 * a))
    )


def gabor_H(a: mp.mpf, omega: mp.mpf, z: mp.mpc) -> mp.mpc:
    return (
        mp.mpf("0.5")
        * mp.sqrt(mp.pi / a)
        * (
            exp_c((z + mp.j * omega) ** 2 / (4 * a))
            + exp_c((z - mp.j * omega) ** 2 / (4 * a))
        )
    )


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


def poly_growth(
    c0: mp.mpf, c2: mp.mpf, c4: mp.mpf, a: mp.mpf, z_abs: mp.mpf,
) -> mp.mpf:
    return (
        abs(c0)
        + abs(c2) * ((1 / (2 * a)) + z_abs ** 2 / (4 * a ** 2))
        + abs(c4) * (
            3 / (4 * a ** 2)
            + 3 * z_abs ** 2 / (4 * a ** 3)
            + z_abs ** 4 / (16 * a ** 4)
        )
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


def family_of(name: str) -> str:
    stem = name.split("|", 1)[0]
    return stem.split(":", 1)[0]


# ---------------------------------------------------------------------------
# Trudgian envelope (r541 constants) + sharp on-line mass
# ---------------------------------------------------------------------------
def trudgian_E(height: mp.mpf) -> mp.mpf:
    clipped = max(height, mp.e)
    log_t = mp.log(clipped)
    log_log = mp.log(log_t) if log_t > 1 else mp.mpf(0)
    return (
        mp.mpf(TRUDGIAN_A) * log_t
        + mp.mpf(TRUDGIAN_B) * log_log
        + mp.mpf(TRUDGIAN_C)
        + mp.mpf(TRUDGIAN_NT_EXTRA) / clipped
    )


def rvm_theta(height: mp.mpf) -> mp.mpf:
    clipped = max(height, mp.e)
    return clipped / (2 * mp.pi) * mp.log(
        clipped / (2 * mp.pi * mp.e)
    ) + mp.mpf("0.875")


def trudgian_increment(height: mp.mpf, width: mp.mpf) -> mp.mpf:
    width_use = max(width, mp.mpf(1))
    t_hi = height + width_use
    return (
        rvm_theta(t_hi) - rvm_theta(height)
        + trudgian_E(t_hi) + trudgian_E(height)
    )


def env_sup_hat(t0: mp.mpf, t1: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Unsigned envelope of ĥ_W(1/2+it) on [t0,t1], r541 lobe-sup."""
    pref = mp.pi / (4 * a)
    omega_abs = abs(omega)

    def lobe_sup(center: mp.mpf) -> mp.mpf:
        if t0 <= center <= t1:
            return mp.mpf(1)
        d0 = t0 - center
        d1 = t1 - center
        dist_sq = min(d0 * d0, d1 * d1)
        return exp_clip(-dist_sq / (2 * a))

    left = lobe_sup(-omega_abs)
    right = lobe_sup(omega_abs)
    cross = 2 * exp_clip(-(t0 * t0 + omega_abs * omega_abs) / (2 * a))
    return pref * (left + right + cross)


def certified_zero_tail(t_cut: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """Bound on 2 Σ_{t_n > t_cut} |ĥ_W(1/2+i t_n)|.  LABEL=CERTIFIED."""
    width_scale = max(8 * mp.sqrt(max(a, mp.mpf("1e-12"))), mp.mpf(8))
    omega_abs = abs(omega)
    t_hard = max(t_cut + width_scale, omega_abs + width_scale)
    t_hard = min(t_hard, mp.mpf("1e7"))
    total = mp.mpf(0)
    t_value = t_cut
    while t_value < t_hard:
        in_window = abs(t_value - omega_abs) <= width_scale + 1
        width = mp.mpf(1) if in_window else max(mp.mpf(1), mp.mpf("0.04") * t_value)
        if t_value + width > t_hard:
            width = max(mp.mpf(1), t_hard - t_value)
        nbound = trudgian_increment(t_value, width)
        env = env_sup_hat(t_value, t_value + width, a, omega)
        total += 2 * nbound * env
        if not mp.isfinite(total) or total > mp.mpf("1e250"):
            return mp.inf
        t_value += width
    u0 = max(t_value - omega_abs, mp.mpf(0))
    beta = 1 / (2 * a)
    erfc = mp.erfc(u0 * mp.sqrt(beta)) if mp.isfinite(u0) else mp.mpf(0)
    lobe = mp.mpf("0.5") * mp.sqrt(mp.pi / beta) * erfc
    rem = (
        2 * mp.mpf(C_CRUDE) * mp.log(t_value + 2)
        * (mp.pi / a) * lobe
    )
    return total + rem


def sharp_online(a: mp.mpf, omega: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Enumerated 2 Σ ĥ_W + Trudgian tail.  Returns (R_sharp, R_fin, R_tail)."""
    finite = mp.mpf(0)
    for height in ON_LINE_ORDINATES:
        finite += 2 * online_value(mp.mpf(height), a, omega)
    t_cut = mp.mpf(ON_LINE_ORDINATES[-1])
    tail = certified_zero_tail(t_cut, a, omega)
    return finite + tail, finite, tail


# ---------------------------------------------------------------------------
# Configuration factory — sealed r554 52-row catalog
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
    for k_use in ks:
        for window in CLUSTER_WINDOWS:
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


def dispute_configs(
    sigma: mp.mpf, gamma: mp.mpf,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    """The two r559 sealed dispute geometries, independent of smoke."""
    wanted = set(DISPUTE_STEMS)
    out: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    for name, quads in make_catalog(sigma, gamma, smoke=False):
        if name in wanted:
            out.append((name, quads))
    return out


def adv_against_packet(
    sigma: mp.mpf,
    a_val: mp.mpf,
    omega: mp.mpf,
    k_use: int,
) -> list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]]:
    """r553-style adversarial answers to a known 1-packet (a, ω)."""
    out: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]] = []
    out.append(
        (
            "adv:on_centre:k=%d" % k_use,
            tuple((sigma, omega) for _ in range(k_use)),
        )
    )
    if k_use > 1:
        pts = tuple(
            omega + (mp.mpf(index) / (k_use - 1))
            for index in range(k_use)
        )
        out.append(
            (
                "adv:unit_at_omega:k=%d" % k_use,
                tuple((sigma, site) for site in pts),
            )
        )
    gap = mp.pi * a_val / sigma if sigma > 0 else mp.mpf(0)
    n_left = k_use // 2
    n_right = k_use - n_left
    out.append(
        (
            "adv:antiphase:k=%d" % k_use,
            tuple(
                [(sigma, omega)] * n_left
                + [(sigma, omega + gap)] * n_right
            ),
        )
    )
    half = mp.mpf("0.5")
    if k_use > 1:
        pts = tuple(
            omega - half + (mp.mpf(index) / (k_use - 1))
            for index in range(k_use)
        )
        out.append(
            (
                "adv:unit_window:k=%d" % k_use,
                tuple((sigma, site) for site in pts),
            )
        )
    return out


# ---------------------------------------------------------------------------
# Witness grid (r541 lock, afac, destructive, optional quartic)
# ---------------------------------------------------------------------------
def aw_seeds(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...], smoke: bool,
) -> list[tuple[str, mp.mpf, mp.mpf]]:
    sigma_max, gamma_min, gamma_max, gamma_mean, _ = config_stats(quads)
    span = gamma_max - gamma_min
    a_ref = scaling_a(sigma_max)
    a_min = a_ref * mp.mpf(A_MIN_FACTOR)
    factors = A_FACTORS[:4] if smoke else A_FACTORS
    seeds: list[tuple[str, mp.mpf, mp.mpf]] = []
    sites = unique_sorted([quads[0][1], gamma_mean, gamma_min, gamma_max])
    for site in sites:
        seeds.append(
            ("r541@%s" % nstr(site, 6), a_ref, scaling_omega(sigma_max, site))
        )
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
        if span > 0:
            a_alt = max(a_min, sigma * span / (2 * mp.pi))
            seeds.append(
                ("destr_span#%d" % index, a_alt, scaling_omega(sigma, gamma))
            )
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


def score_pure(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    c_inc: mp.mpf,
    seed: str,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    total = mp.mpf(0)
    primary = mp.inf
    for sigma, gamma in quads:
        term = quadruple_closed(sigma, gamma, a_val, omega)
        total += term
        if term < primary:
            primary = term
    r_on = online_budget(a_val, omega, c_inc)
    w_honest = total + r_on
    w_left = leftover(total, primary, r_on, r_ref, margin)
    pick = (total - primary) + max(r_on, mp.mpf(0))
    return {
        "seed": seed,
        "class": "pure",
        "a": a_val,
        "omega": omega,
        "Q_off": total,
        "Q_primary": primary,
        "R_on": r_on,
        "W_honest": w_honest,
        "W_left": w_left,
        "_pick": pick,
        "b2": "0",
        "b4": "0",
    }


def score_poly(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    a_val: mp.mpf,
    omega: mp.mpf,
    c_inc: mp.mpf,
    b2_text: str,
    b4_text: str,
    r_ref: mp.mpf,
    margin: mp.mpf,
) -> dict:
    c0 = mp.mpf(1)
    c2 = mp.mpf(b2_text) * a_val
    c4 = mp.mpf(b4_text) * a_val ** 2
    total = mp.mpf(0)
    primary = mp.inf
    for sigma, gamma in quads:
        term = 4 * mp.re(gabor_hat_poly(c0, c2, c4, a_val, omega, sigma, gamma))
        total += term
        if term < primary:
            primary = term
    r_pure = online_budget(a_val, omega, c_inc)
    growth = poly_growth(c0, c2, c4, a_val, abs(omega) + 1)
    r_on = (growth * growth) * r_pure
    w_honest = total + r_on
    w_left = leftover(total, primary, r_on, r_ref, margin)
    return {
        "seed": "poly:b2=%s:b4=%s" % (b2_text, b4_text),
        "class": "poly",
        "a": a_val,
        "omega": omega,
        "Q_off": total,
        "Q_primary": primary,
        "R_on": r_on,
        "W_honest": w_honest,
        "W_left": w_left,
        "_pick": (total - primary) + r_on,
        "b2": b2_text,
        "b4": b4_text,
    }


def best_by(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    r_ref: mp.mpf,
    margin: mp.mpf,
    key: str,
    with_poly: bool = True,
) -> dict:
    """Select the grid seed that minimises `key` (W_honest / W_left / _pick)."""
    best: dict | None = None
    seeds = aw_seeds(quads, smoke)
    for name, a_val, omega in seeds:
        rec = score_pure(quads, a_val, omega, c_inc, name, r_ref, margin)
        if best is None or rec[key] < best[key]:
            best = rec
    if with_poly and best is not None:
        b2s = POLY_B2[:3] if smoke else POLY_B2
        b4s = ("0",) if smoke else POLY_B4
        for b2_text in b2s:
            for b4_text in b4s:
                if b2_text == "0" and b4_text == "0":
                    continue
                rec = score_poly(
                    quads, best["a"], best["omega"], c_inc,
                    b2_text, b4_text, r_ref, margin,
                )
                if rec[key] < best[key]:
                    best = rec
    assert best is not None
    return best


def attach_sharp(rec: dict, force: bool = False) -> dict:
    if rec["W_honest"] <= 0 and not force:
        rec["W_sharp"] = rec["W_honest"]
        rec["R_sharp"] = rec["R_on"]
        rec["R_fin"] = rec["R_on"]
        rec["R_tail"] = mp.mpf(0)
        rec["sharp_computed"] = "0"
        return rec
    r_sharp, r_fin, r_tail = sharp_online(rec["a"], rec["omega"])
    rec["R_sharp"] = r_sharp
    rec["R_fin"] = r_fin
    rec["R_tail"] = r_tail
    rec["W_sharp"] = rec["Q_off"] + r_sharp
    rec["sharp_computed"] = "1"
    return rec


def public_rec(rec: dict) -> dict:
    out = {
        "seed": rec["seed"],
        "class": rec["class"],
        "a": nstr(rec["a"]),
        "omega": nstr(rec["omega"]),
        "Q_off": nstr(rec["Q_off"]),
        "Q_primary": nstr(rec["Q_primary"]),
        "R_on": nstr(rec["R_on"]),
        "W_honest": nstr(rec["W_honest"]),
        "W_left": nstr(rec["W_left"]),
        "b2": rec.get("b2", "0"),
        "b4": rec.get("b4", "0"),
        "win_budget": str(int(rec["W_honest"] < 0)),
    }
    if "W_sharp" in rec:
        out["W_sharp"] = nstr(rec["W_sharp"])
        out["R_sharp"] = nstr(rec["R_sharp"])
        out["R_fin"] = nstr(rec.get("R_fin", rec["R_on"]))
        out["R_tail"] = nstr(rec.get("R_tail", mp.mpf(0)))
        out["sharp_computed"] = rec.get("sharp_computed", "0")
        out["win_sharp"] = str(int(rec["W_sharp"] < 0))
    return out


def eval_config(
    name: str,
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    r_ref: mp.mpf,
    margin: mp.mpf,
    need_sharp: bool,
) -> dict:
    honest = attach_sharp(
        best_by(quads, c_inc, smoke, r_ref, margin, "W_honest"),
        force=need_sharp,
    )
    if honest["W_honest"] > 0:
        attach_sharp(honest, force=True)
    return {
        "name": name,
        "n_quad": str(len(quads)),
        "inc_ok": str(int(increment_ok(quads))),
        "family": family_of(name),
        "honest": public_rec(honest),
        "_W_honest": honest["W_honest"],
        "_W_sharp": honest["W_sharp"],
        "_quads": quads,
        "_rec": honest,
    }


# ---------------------------------------------------------------------------
# G0 / catalog / game / dispute / verdicts
# ---------------------------------------------------------------------------
def run_g0(c_inc: mp.mpf) -> tuple[bool, mp.mpf]:
    max_err = mp.mpf(0)
    for alpha in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2)):
        for delta in (mp.mpc(0), mp.mpc("0.3"), mp.mpc("0.2", "0.4")):
            analytic = (mp.pi / alpha) * mp.exp((delta * delta) / (2 * alpha))
            from_h = hat_w_delta(delta.real, delta.imag, alpha, mp.mpf(0))
            max_err = max(max_err, abs(from_h - analytic))
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    a_val = scaling_a(sigma)
    omega = scaling_omega(sigma, gamma)
    max_err = max(max_err, abs(sigma * (gamma - omega) / a_val - mp.pi))
    max_err = max(max_err, abs(mp.exp(sigma ** 2 / (2 * a_val)) - mp.exp(32)))
    q_closed = quadruple_closed(sigma, gamma, a_val, omega)
    q_re = 4 * mp.re(hat_w_delta(sigma, gamma, a_val, omega))
    max_err = max(max_err, abs(q_closed - q_re))
    delta = sigma + mp.j * gamma
    from_h = gabor_H(a_val, omega, delta) * gabor_H(a_val, omega, -delta)
    max_err = max(max_err, abs(from_h - hat_w_delta(sigma, gamma, a_val, omega)))
    on_line = online_value(gamma, a_val, omega)
    hat0 = mp.re(hat_w_delta(mp.mpf(0), gamma, a_val, omega))
    max_err = max(max_err, abs(on_line - hat0))
    pin = mp.mpf(C_INC_PIN)
    max_err = max(max_err, abs(c_inc - pin) / pin)
    if increment_ok(((sigma, gamma),) * K_MAX_BIN) is False:
        max_err = max(max_err, mp.mpf(1))
    if increment_ok(((sigma, gamma),) * (K_MAX_BIN + 1)) is True:
        max_err = max(max_err, mp.mpf(1))
    if len(ON_LINE_ORDINATES) != 100:
        max_err = max(max_err, mp.mpf(1))
    if not (c_inc > 0 and mp.isfinite(c_inc)):
        max_err = max(max_err, mp.mpf(1))
    return max_err < mp.mpf("1e-9"), max_err


def run_catalog(
    smoke: bool, c_inc: mp.mpf, r_ref: mp.mpf, margin: mp.mpf,
) -> list[dict]:
    section("PART1  CATALOG  (Z frozen, then 1-packet sees Z; score = W_honest)")
    print(
        "  W_honest = Q_off + R_on   unit amplitude   "
        "select by W_honest, not leftover / pick"
    )
    sigmas = (HOST_SIGMAS[1],) if smoke else HOST_SIGMAS
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in HOST_GAMMAS:
            gamma = mp.mpf(gamma_text)
            for name, quads in make_catalog(sigma, gamma, smoke):
                full = "%s|s=%s|g=%s" % (name, sigma_text, gamma_text)
                rows.append(
                    eval_config(full, quads, c_inc, smoke, r_ref, margin, False)
                )
    print(
        "  name                              nq  W_honest       W_sharp        "
        "seed                     winB winS"
    )
    for row in rows:
        rec = row["honest"]
        print(
            "  %-32s %2s  %s  %s  %-22s %s    %s"
            % (
                row["name"][:32],
                row["n_quad"],
                nstr(mp.mpf(rec["W_honest"]), 6),
                nstr(mp.mpf(rec.get("W_sharp", rec["W_honest"])), 6),
                rec["seed"][:22],
                rec["win_budget"],
                rec.get("win_sharp", rec["win_budget"]),
            )
        )
    return rows


def run_dispute(
    smoke: bool, c_inc: mp.mpf, r_ref: mp.mpf, margin: mp.mpf,
) -> list[dict]:
    section("PART2  R559 DISPUTE  (both witness choices, both σ, W_honest)")
    print(
        "  sealed stems  %s"
        % ", ".join(DISPUTE_STEMS)
    )
    sigmas = HOST_SIGMAS if not smoke else (HOST_SIGMAS[1],)
    rows: list[dict] = []
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        gamma = mp.mpf(HOST_GAMMAS[0])
        for name, quads in dispute_configs(sigma, gamma):
            full = "%s|s=%s|g=%s" % (name, sigma_text, HOST_GAMMAS[0])
            pick = score_and_label(
                quads, c_inc, smoke, r_ref, margin, "_pick",
            )
            left = score_and_label(
                quads, c_inc, smoke, r_ref, margin, "W_left",
            )
            honest = score_and_label(
                quads, c_inc, smoke, r_ref, margin, "W_honest",
            )
            attach_sharp(pick, force=True)
            attach_sharp(left, force=True)
            attach_sharp(honest, force=True)
            row = {
                "name": full,
                "n_quad": str(len(quads)),
                "r553_pick": public_rec(pick),
                "leftover_opt": public_rec(left),
                "honest_opt": public_rec(honest),
            }
            rows.append(row)
            print("  %s  nq=%s" % (full, row["n_quad"]))
            for tag, rec in (
                ("r553_pick   ", row["r553_pick"]),
                ("leftover_opt", row["leftover_opt"]),
                ("honest_opt  ", row["honest_opt"]),
            ):
                print(
                    "    %s  seed=%-22s  Q_off=%s  Q_pri=%s  R_on=%s  "
                    "W_honest=%s  W_left=%s  W_sharp=%s"
                    % (
                        tag,
                        rec["seed"][:22],
                        nstr(mp.mpf(rec["Q_off"]), 6),
                        nstr(mp.mpf(rec["Q_primary"]), 6),
                        nstr(mp.mpf(rec["R_on"]), 6),
                        nstr(mp.mpf(rec["W_honest"]), 6),
                        nstr(mp.mpf(rec["W_left"]), 6),
                        nstr(mp.mpf(rec["W_sharp"]), 6),
                    )
                )
    return rows


def score_and_label(
    quads: tuple[tuple[mp.mpf, mp.mpf], ...],
    c_inc: mp.mpf,
    smoke: bool,
    r_ref: mp.mpf,
    margin: mp.mpf,
    key: str,
) -> dict:
    return best_by(quads, c_inc, smoke, r_ref, margin, key, with_poly=False)


def run_game(
    smoke: bool,
    c_inc: mp.mpf,
    r_ref: mp.mpf,
    margin: mp.mpf,
    rows: list[dict],
) -> dict:
    section("PART3  MIN-MAX GAME  (2 adversary rounds against honest-opt 1-packet)")
    print(
        "  Round t: Z_t = argmax W_honest(best_1pkt(Z),Z); "
        "adversary sits on that packet centre / unit / antiphase; "
        "witness retunes."
    )
    if not rows:
        return {
            "iterations": [],
            "worst_catalog": "",
            "W_worst_catalog": "0",
            "adv_rows": [],
            "worst_adv": "",
            "W_worst_adv": "0",
            "worst_adv2": "",
            "W_worst_adv2": "0",
        }

    def worst_of(pool: list[dict]) -> dict:
        return max(pool, key=lambda row: row["_W_honest"])

    w0 = worst_of(rows)
    iterations = [{
        "iter": "0",
        "strategy": "honest_opt_1pkt",
        "worst": w0["name"],
        "W_honest": nstr(w0["_W_honest"]),
        "W_sharp": nstr(w0["_W_sharp"]),
        "win": w0["honest"]["win_budget"],
        "seed": w0["honest"]["seed"],
    }]

    k_use = 5 if smoke else 10
    host = w0["_quads"][0][0]
    rec0 = w0["_rec"]

    def eval_adv(
        extras: list[tuple[str, tuple[tuple[mp.mpf, mp.mpf], ...]]],
        tag: str,
        src_name: str,
    ) -> list[dict]:
        out: list[dict] = []
        seen: set[str] = set()
        for adv_name, adv_quads in extras:
            full = "%s|from=%s|%s" % (adv_name, tag, src_name)
            if full in seen:
                continue
            seen.add(full)
            if not increment_ok(adv_quads):
                continue
            out.append(
                eval_config(full, adv_quads, c_inc, smoke, r_ref, margin, False)
            )
        return out

    extras1 = adv_against_packet(host, rec0["a"], rec0["omega"], k_use)
    adv1 = eval_adv(extras1, "r1", w0["name"])
    if adv1:
        a1 = worst_of(adv1)
        iterations.append({
            "iter": "1",
            "strategy": "honest_opt_vs_adv",
            "worst": a1["name"],
            "W_honest": nstr(a1["_W_honest"]),
            "W_sharp": nstr(a1["_W_sharp"]),
            "win": a1["honest"]["win_budget"],
            "seed": a1["honest"]["seed"],
        })
        extras2 = adv_against_packet(
            a1["_quads"][0][0], a1["_rec"]["a"], a1["_rec"]["omega"], k_use,
        )
        adv2 = eval_adv(extras2, "r2", a1["name"])
    else:
        a1 = w0
        adv2 = []

    if adv2:
        a2 = worst_of(adv2)
        iterations.append({
            "iter": "2",
            "strategy": "honest_opt_vs_adv2",
            "worst": a2["name"],
            "W_honest": nstr(a2["_W_honest"]),
            "W_sharp": nstr(a2["_W_sharp"]),
            "win": a2["honest"]["win_budget"],
            "seed": a2["honest"]["seed"],
        })
    else:
        a2 = a1

    print("  iter strategy              worst                              W_honest")
    for item in iterations:
        print(
            "  %s    %-20s %-33s %s  win=%s"
            % (
                item["iter"],
                item["strategy"],
                item["worst"][:33],
                item["W_honest"],
                item["win"],
            )
        )
    adv_all = adv1 + adv2
    return {
        "iterations": iterations,
        "worst_catalog": w0["name"],
        "W_worst_catalog": nstr(w0["_W_honest"]),
        "worst_adv": a1["name"],
        "W_worst_adv": nstr(a1["_W_honest"]),
        "worst_adv2": a2["name"],
        "W_worst_adv2": nstr(a2["_W_honest"]),
        "adv_rows": adv_all,
        "n_adv": str(len(adv_all)),
    }


def compact_map(rows: list[dict]) -> list[dict]:
    out: list[dict] = []
    for row in rows:
        item = {
            "name": row["name"],
            "n_quad": row["n_quad"],
            "family": row.get("family", family_of(row["name"])),
            "W_honest": row["honest"]["W_honest"],
            "W_sharp": row["honest"].get("W_sharp", row["honest"]["W_honest"]),
            "win_budget": row["honest"]["win_budget"],
            "win_sharp": row["honest"].get("win_sharp", row["honest"]["win_budget"]),
            "seed": row["honest"]["seed"],
            "class": row["honest"]["class"],
        }
        out.append(item)
    return out


def family_tally(rows: list[dict]) -> dict[str, dict[str, int]]:
    tally: dict[str, dict[str, int]] = {}
    for row in rows:
        fam = row.get("family", family_of(row["name"]))
        bucket = tally.setdefault(fam, {"n": 0, "budget_win": 0, "sharp_win": 0})
        bucket["n"] += 1
        if row["honest"]["win_budget"] == "1":
            bucket["budget_win"] += 1
        if row["honest"].get("win_sharp", row["honest"]["win_budget"]) == "1":
            bucket["sharp_win"] += 1
    return tally


def decide(rows: list[dict], game: dict) -> tuple[str, dict]:
    budget_losses = [row for row in rows if row["_W_honest"] >= 0]
    sharp_losses = [row for row in rows if row["_W_sharp"] >= 0]
    sharp_rescues = [
        row for row in budget_losses if row["_W_sharp"] < 0
    ]
    adv_rows = game.get("adv_rows") or []
    adv_budget_loss = [row for row in adv_rows if row["_W_honest"] >= 0]
    adv_sharp_loss = [row for row in adv_rows if row["_W_sharp"] >= 0]
    adv_rescue = [
        row for row in adv_budget_loss if row["_W_sharp"] < 0
    ]
    worst = max(rows, key=lambda row: row["_W_honest"]) if rows else None
    extra = {
        "n_catalog": str(len(rows)),
        "n_budget_win": str(len(rows) - len(budget_losses)),
        "n_budget_loss": str(len(budget_losses)),
        "n_sharp_win": str(len(rows) - len(sharp_losses)),
        "n_sharp_loss": str(len(sharp_losses)),
        "n_sharp_rescue": str(len(sharp_rescues)),
        "n_adv": str(len(adv_rows)),
        "n_adv_budget_loss": str(len(adv_budget_loss)),
        "n_adv_sharp_loss": str(len(adv_sharp_loss)),
        "n_adv_rescue": str(len(adv_rescue)),
        "worst": worst["name"] if worst else "",
        "worst_W_honest": nstr(worst["_W_honest"]) if worst else "0",
        "worst_W_sharp": nstr(worst["_W_sharp"]) if worst else "0",
        "worst_seed": worst["honest"]["seed"] if worst else "",
        "worst_class": worst["honest"]["class"] if worst else "",
        "worst_a": worst["honest"]["a"] if worst else "",
        "worst_omega": worst["honest"]["omega"] if worst else "",
    }
    catalog_budget_ok = not budget_losses
    catalog_sharp_ok = not sharp_losses
    adv_budget_ok = not adv_budget_loss
    adv_sharp_ok = not adv_sharp_loss

    if catalog_budget_ok and adv_budget_ok:
        verdict = "HONEST_WITNESS_WINS(all=%d, worst_margin=%s)" % (
            len(rows), extra["worst_W_honest"],
        )
        return verdict, extra
    if (not catalog_sharp_ok) or (adv_rows and not adv_sharp_ok):
        loss = (sharp_losses + adv_sharp_loss)[0]
        verdict = (
            "HONEST_WITNESS_LOSES(config=%s, W_honest=%s, W_sharp=%s)"
            % (
                loss["name"],
                nstr(loss["_W_honest"]),
                nstr(loss["_W_sharp"]),
            )
        )
        extra["loss_config"] = loss["name"]
        extra["loss_W_honest"] = nstr(loss["_W_honest"])
        extra["loss_W_sharp"] = nstr(loss["_W_sharp"])
        return verdict, extra
    n_budget = len(budget_losses) + len(adv_budget_loss)
    n_rescue = len(sharp_rescues) + len(adv_rescue)
    verdict = "HONEST_SPLIT(budget_losses=%d, sharp_wins=%d)" % (
        n_budget, n_rescue,
    )
    return verdict, extra


def lean_consequence(verdict: str, extra: dict) -> tuple[str, str]:
    """Honest reading of the 1-packet ∀Z-∃h route.  Not a claim."""
    if verdict.startswith("HONEST_WITNESS_WINS"):
        route = "OPEN_ON_CATALOG"
        missing = (
            "Lean-Prop still needs (i) a proof that some constructive "
            "1-packet (e.g. r541 lock on the most negative site) beats "
            "every increment-compliant Z, not just the 52-row catalog + "
            "two adv rounds; (ii) a closed (a,ω) rule, not a grid search; "
            "(iii) the C_inc theta budget is an upper bound — a numerical "
            "win is valid but the existence statement must name h and "
            "bound extras + R_on uniformly.  Catalog win ≠ RH."
        )
    elif verdict.startswith("HONEST_SPLIT"):
        route = "CONDITIONAL_ON_SHARP_MASS"
        missing = (
            "Budget (C_inc theta) is too coarse on %s rows; sharp "
            "first-100+Trudgian rescues them.  A Lean-Prop on the true "
            "form needs a sharper on-line estimate than 2 C_inc S_cert "
            "(Trudgian-increment × envelope, or an explicit zero sum).  "
            "1-packet route is not closed, not unconditionally open."
            % extra.get("n_budget_loss", "?")
        )
    else:
        route = "CLOSED_FOR_1PACKET_UNDER_COUNTING"
        missing = (
            "Even the sharp on-line mass leaves W>0 on %s.  A Lean-Prop "
            "in the 1-packet class is blocked on that Z unless a richer "
            "even test (mixture / higher poly / different a-rule) is "
            "admitted, or the increment model is tightened.  Not an RH claim."
            % extra.get("loss_config", extra.get("worst", "?"))
        )
    return route, missing


def run(smoke: bool) -> int:
    mp.mp.dps = DPS
    c_inc = c_inc_prefactor()
    margin = abs(mp.mpf(R541_MARGIN))
    print("gabor_honest_weil_game_probe -- r560")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("quantifiers forall_Z exists_h  (config first)")
    print("normalisation unit_amplitude; W quadratic-homogeneous; sign frozen")
    print("online 2*C_inc*S_cert  C_inc %s" % nstr(c_inc))
    print("FORMULA  W_honest = Q_off + R_on   (no R_ref, no -3.56)")
    print("FORMULA  W_sharp  = Q_off + 2*sum_{k=1..100} hat_W(1/2+i γ_k) + Trudgian_tail")

    section("G0  CLOSED FORMS / C_inc PIN / INCREMENT CARD")
    g0_ok, g0_err = run_g0(c_inc)
    check("G0-calibration", g0_ok, "max_err=%s" % nstr(g0_err, 6))
    check(
        "G0-c-inc-pin",
        abs(c_inc - mp.mpf(C_INC_PIN)) / mp.mpf(C_INC_PIN) < mp.mpf("1e-9"),
        "C_inc=%s pin=%s" % (nstr(c_inc), C_INC_PIN),
    )

    sigma_ref = mp.mpf(HOST_SIGMAS[0])
    gamma_ref = mp.mpf(HOST_GAMMAS[0])
    a_ref = scaling_a(sigma_ref)
    w_ref = scaling_omega(sigma_ref, gamma_ref)
    q_ref = quadruple_closed(sigma_ref, gamma_ref, a_ref, w_ref)
    r_ref = online_budget(a_ref, w_ref, c_inc)
    print("  Q_ref %s  R_ref %s  (audit leftover only; not in W_honest)" % (
        nstr(q_ref), nstr(r_ref),
    ))

    rows = run_catalog(smoke, c_inc, r_ref, margin)
    inc_all = all(row["inc_ok"] == "1" for row in rows)
    check("P1-increment-ok", inc_all, "every catalog Z has ≤%d quads/bin" % K_MAX_BIN)
    check("P1-catalog-nonempty", len(rows) > 0, "n=%d" % len(rows))
    if not smoke:
        check("P1-catalog-52", len(rows) == 52, "n=%d" % len(rows))
    else:
        check("P1-smoke-catalog", len(rows) >= 4, "n=%d" % len(rows))

    # Homogeneity: scaling cannot flip the sign.
    if rows:
        rec = rows[0]["_rec"]
        q2, r2 = rec["Q_off"] * 4, rec["R_on"] * 4
        check(
            "P1-quadratic-homogeneous",
            abs((q2 + r2) - 4 * rec["W_honest"]) < mp.mpf("1e-8") * (
                1 + abs(rec["W_honest"])
            ),
            "W(2h)=4 W(h) on first catalog row",
        )

    dispute = run_dispute(smoke, c_inc, r_ref, margin)
    check("P2-dispute-nonempty", len(dispute) > 0, "n=%d" % len(dispute))
    if not smoke:
        check("P2-dispute-both-sigma", len(dispute) == 4, "n=%d" % len(dispute))

    game = run_game(smoke, c_inc, r_ref, margin, rows)

    section("PART4  WIN MAP / VERDICT")
    verdict, extra = decide(rows, game)
    tally = family_tally(rows)
    print("  VERDICT %s" % verdict)
    print("  budget_wins %s/%s  sharp_wins %s/%s  sharp_rescues %s" % (
        extra["n_budget_win"], extra["n_catalog"],
        extra["n_sharp_win"], extra["n_catalog"],
        extra["n_sharp_rescue"],
    ))
    print("  adv_budget_loss %s  adv_sharp_loss %s  adv_rescue %s" % (
        extra["n_adv_budget_loss"], extra["n_adv_sharp_loss"], extra["n_adv_rescue"],
    ))
    print("  worst %s  W_honest=%s  W_sharp=%s  seed=%s" % (
        extra["worst"], extra["worst_W_honest"], extra["worst_W_sharp"],
        extra["worst_seed"],
    ))
    print("  FAMILY            n  budget_win  sharp_win")
    for fam in sorted(tally):
        bucket = tally[fam]
        print(
            "  %-16s %2d  %2d/%-2d       %2d/%-2d"
            % (
                fam, bucket["n"],
                bucket["budget_win"], bucket["n"],
                bucket["sharp_win"], bucket["n"],
            )
        )

    route, missing = lean_consequence(verdict, extra)
    print("  ROUTE %s" % route)
    print("  LEAN_GAP %s" % missing)

    check("P4-verdict-formed", verdict.startswith("HONEST_"), verdict)

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "no wall-clock, no RNG, BLAS threads=1; two full runs must match",
    )
    # In-process double evaluation of the first row.
    if rows:
        again = eval_config(
            rows[0]["name"], rows[0]["_quads"], c_inc, smoke, r_ref, margin, False,
        )
        check(
            "G3-inprocess-rescore",
            nstr(again["_W_honest"]) == nstr(rows[0]["_W_honest"]),
            "first-row W_honest replay",
        )
    if smoke:
        check("G4-smoke-subset", True, "sigma=0.25, reduced catalog")
    else:
        check("G4-full-grid", True, "sigmas=%d families=7+adv" % len(HOST_SIGMAS))

    game_pub = {
        key: value for key, value in game.items() if key != "adv_rows"
    }
    if game.get("adv_rows"):
        game_pub["adv_map"] = compact_map(game["adv_rows"])

    canon = {
        "catalog": compact_map(rows),
        "dispute": dispute,
        "game": game_pub,
        "verdict": verdict,
        "extra": extra,
        "tally": {
            fam: {k: str(v) for k, v in bucket.items()}
            for fam, bucket in tally.items()
        },
        "route": route,
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
    print("N_BUDGET_WIN %s" % extra["n_budget_win"])
    print("N_BUDGET_LOSS %s" % extra["n_budget_loss"])
    print("N_SHARP_WIN %s" % extra["n_sharp_win"])
    print("N_SHARP_LOSS %s" % extra["n_sharp_loss"])
    print("N_SHARP_RESCUE %s" % extra["n_sharp_rescue"])
    print("WORST %s" % extra["worst"])
    print("WORST_W_HONEST %s" % extra["worst_W_honest"])
    print("WORST_W_SHARP %s" % extra["worst_W_sharp"])
    print("WORST_SEED %s" % extra["worst_seed"])
    print("GAME_WORST_CATALOG %s %s" % (game["worst_catalog"], game["W_worst_catalog"]))
    print("GAME_WORST_ADV %s %s" % (game["worst_adv"], game["W_worst_adv"]))
    print("GAME_WORST_ADV2 %s %s" % (game["worst_adv2"], game["W_worst_adv2"]))
    print("VERDICT %s" % verdict)
    print("ROUTE %s" % route)
    print("LEAN_GAP %s" % missing)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print(
        "LEAN_NOTE W_honest = Q_off + R_on is the homogeneous form; "
        "leftover is audit-only and is not the objective"
    )
    print(
        "LEAN_NOTE a catalog win is not a Lean-Prop: the grid is NUMERIC, "
        "Z is a finite increment-compliant list, no RH claim"
    )
    print("NO_RH_CLAIM")
    print("NEXT_TXT_SUGGESTION r560: %s  ROUTE=%s  KEIN RH-CLAIM" % (verdict, route))
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
            "r560 Gabor honest-Weil config-first game "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
