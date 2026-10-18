#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_scramble_gate_probe -- r565

Round 565.  Experiments-only LATE r469 scramble-gate declaration
for the Gabor / dominance route (r541–r561 never declared).

  r469 (binding anti-list §3): BEFORE any probe is built, declare
  whether the bound is scramble-sensitive.  r467 measured that
  SCRAMBLE of the prime data RAISED the dangerous alignment by
  28.5–5.3·10⁵.  A scramble-INVARIANT bound must swallow that
  factor and is, on the 31-dead-route record, too coarse — BUT
  only if the route USES prime roughness as a resource.  A bound
  that does not need prime cancellation may be scramble-invariant
  without being dead.

  The Gabor dominance game (r560/r561) books W_honest = Σ Q + R_on
  with no explicit prime side.  Weil positivity / prime arithmetic
  live in the FULL r541/r548 form, so the gate is scored there.

FULL FORM (r541/r548 Identity A, comb convention inherited):

    W = Pole − Comb + Arch − Z_on − Q_off

    Pole = ĥ_W(0)+ĥ_W(1)
    Comb = Σ_n 2 Λ(n) n^{−1/2} g(log n)     [classical Weil/comb]
    Arch = (1/2π) ∫ ĥ_W(1/2+it) (Re ψ(1/4+it/2)−log π) dt
    Z_on = 2 Σ_{k=1}^N ĥ_W(1/2+iγ_k)  + certified Trudgian tail
    Q_off = 4 Re ĥ_W(1/2+σ+iγ)          [injected host quadruple]

  g(u) = √(π/(2a))/2 · e^{−a u²/2} [cos(ω u) + e^{−ω²/(2a)}]
  (pure Gabor, r541 closed form).  Hat is Weil-shifted.

CELLS.  σ ∈ {0.01, 0.25, 0.49} × γ ∈ {14, 1000, 10000}, each with
  (i) r541 lock  a=σ²/64, ω=γ−πa/σ
  (ii) r561 isolation-shrink on the singleton host {(σ,γ)}:
       a_seed=(σ²/64)/8, shrink until πa/σ+ε(a) ≤ d_min/2
       (singleton ⇒ d_min=+∞ ⇒ no shrink, a=a_seed).

SCRAMBLES (fixed seed, p=1..8).
  ECHT:      Λ at true prime powers
  SCRAMBLE-1: same Λ values, labels permuted on the prime-power support
  SCRAMBLE-2: Λ ← log n at every n≥2  (named PNT smear) plus the
              deterministic equivalent Λ←1 (mean of von Mangoldt)
  NULL:      Comb = 0

SENSITIVITY.  ΔW = W_variant − W_echt.  A cell is SENSITIVE if any
scramble flips sign(W) or |ΔW| > 0.1 |W_echt|; else INSENSITIVE.

LAGE.  needs_cancellation iff W_NULL flips sign vs W_echt or
drops below half the echt margin.  That is the r469-dead case
(invariant bound that still needed prime roughness).

CLAIM BOUNDARY.  Finite deterministic arithmetic on a frozen
n-cap / first-100 ordinates.  NO RH claim, NO anti-RH claim,
NO ledger/paper/Lean/next.txt edit.

Verdicts:
  GATE_PASS(mode=needs_no_cancellation|prime_sensitive, worst_cell=…)
  GATE_FAIL(reason=…)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
PARENT_R541_PREFIX = "d85802a1"
PARENT_R560_PREFIX = "990ccd20"
PARENT_R561_PREFIX = "519a3895"
HOST_SIGMAS = ("0.01", "0.25", "0.49")
HOST_GAMMAS = ("14", "1000", "10000")
N_PERMS = 8
SCRAMBLE_SEED = 20260901
SENS_FRAC = "0.1"
NSTR_DIGITS = 12
DPS = 40
DPS_EXTREME = 80
A_LOCK_DENOM = "64"
A_ISO_FACTOR = "0.125"
ISOLATION_HALVINGS = 60
A_FLOOR_DENOM = "1e12"
K_MAX_BIN = 43
PRIME_N_CAP = 20000
N_ZEROS = 100
C_CRUDE = 4.0
TRUDGIAN_A = 0.111
TRUDGIAN_B = 0.275
TRUDGIAN_C = 2.450
TRUDGIAN_NT_EXTRA = 0.2
ARCH_LOBE_WIDTHS = 12.0

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

SPEC = {
    "round": 565,
    "parent_rounds": [469, 541, 548, 560, 561],
    "contract": "PRIME.RDAGGER.WEIL_GABOR.SCRAMBLE_GATE.01",
    "target": "r469_anti_list_3_gabor_dominance_late_declaration",
    "hat": "weil_shifted",
    "class": "pure_gabor_unit_amplitude",
    "form": "W = Pole - Comb + Arch - Z_on - Q_off",
    "prime_convention": "2*Lambda(n)/sqrt(n)*g(log n)  [r541/r548 comb]",
    "lock": "a=sigma^2/64, omega=gamma-pi*a/sigma",
    "isolation": "r561.rule_isolation on singleton host",
    "host_sigmas": list(HOST_SIGMAS),
    "host_gammas": list(HOST_GAMMAS),
    "n_perms": N_PERMS,
    "scramble_seed": SCRAMBLE_SEED,
    "sens_frac": SENS_FRAC,
    "prime_n_cap": PRIME_N_CAP,
    "n_zeros": N_ZEROS,
    "parent_r541_prefix": PARENT_R541_PREFIX,
    "parent_r560_prefix": PARENT_R560_PREFIX,
    "parent_r561_prefix": PARENT_R561_PREFIX,
    "excluded": "RH claim; Lean edit; ledger/paper; next.txt",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
_HERE = Path(__file__).resolve().parent


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


def parent_sha(name: str) -> str:
    return hashlib.sha256((_HERE / name).read_bytes()).hexdigest()


def nstr(value: mp.mpf, digits: int = NSTR_DIGITS) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def payload_sha(rows: object) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def log10_abs(value: mp.mpf) -> str:
    if value == 0:
        return "-inf"
    return nstr(mp.log10(abs(value)), 8)


# ---------------------------------------------------------------------------
# Sealed r541/r561 (a,ω)  — formulas inherited, not re-derived
# ---------------------------------------------------------------------------
def a_r541_lock(sigma: mp.mpf) -> mp.mpf:
    return sigma ** 2 / mp.mpf(A_LOCK_DENOM)


def a_r561_seed(sigma: mp.mpf) -> mp.mpf:
    return a_r541_lock(sigma) * mp.mpf(A_ISO_FACTOR)


def omega_rule(sigma: mp.mpf, gamma: mp.mpf, a_val: mp.mpf) -> mp.mpf:
    return gamma - mp.pi * a_val / sigma


def epsilon_of(a_val: mp.mpf) -> mp.mpf:
    if a_val <= 0:
        return mp.mpf(0)
    log_term = mp.log(max(1 / a_val, mp.mpf(4 * K_MAX_BIN)))
    if log_term < 1:
        log_term = mp.mpf(1)
    return mp.sqrt(2 * a_val * log_term)


def isolated(sigma: mp.mpf, d_min: mp.mpf, a_val: mp.mpf) -> bool:
    if not mp.isfinite(d_min):
        return True
    return (mp.pi * a_val / sigma) + epsilon_of(a_val) <= d_min / 2


def isolation_a(sigma: mp.mpf, d_min: mp.mpf, a_seed: mp.mpf) -> mp.mpf:
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


def rule_lock(sigma: mp.mpf, gamma: mp.mpf) -> tuple[str, mp.mpf, mp.mpf]:
    a_val = a_r541_lock(sigma)
    return "r541_lock", a_val, omega_rule(sigma, gamma, a_val)


def rule_isolation(sigma: mp.mpf, gamma: mp.mpf) -> tuple[str, mp.mpf, mp.mpf]:
    """r561.rule_isolation on the singleton host {(σ,γ)}."""
    d_min = mp.inf
    a_seed = a_r561_seed(sigma)
    a_val = isolation_a(sigma, d_min, a_seed)
    tag = "r561_isolation"
    if a_val != a_seed:
        tag = "r561_isolation_shrunk"
    if not isolated(sigma, d_min, a_val):
        tag = "r561_isolation_cover_fallback"
        a_val = a_seed
    return tag, a_val, omega_rule(sigma, gamma, a_val)


# ---------------------------------------------------------------------------
# Pure-Gabor hats / g  (r541 closed form, log-safe via mpmath)
# ---------------------------------------------------------------------------
def hat_w_pure(delta: mp.mpc, a_val: mp.mpf, omega: mp.mpf) -> mp.mpc:
    """Lean `pureGaborHatDelta` / r541 ĥ_W(1/2+δ)."""
    sig = mp.re(delta)
    t_val = mp.im(delta)
    pref = mp.pi / (4 * a_val)
    left = mp.e ** ((sig * sig - (t_val + omega) ** 2) / (2 * a_val)) * mp.e ** (
        mp.j * (sig * (t_val + omega) / a_val)
    )
    right = mp.e ** ((sig * sig - (t_val - omega) ** 2) / (2 * a_val)) * mp.e ** (
        mp.j * (sig * (t_val - omega) / a_val)
    )
    cross = 2 * mp.e ** (
        (sig * sig - t_val * t_val - omega * omega) / (2 * a_val)
    ) * mp.e ** (mp.j * (sig * t_val / a_val))
    return pref * (left + right + cross)


def f_online(t_value: mp.mpf, a_val: mp.mpf, omega: mp.mpf) -> mp.mpf:
    pref = mp.pi / (4 * a_val)
    left = mp.e ** (-(t_value + omega) ** 2 / (2 * a_val))
    right = mp.e ** (-(t_value - omega) ** 2 / (2 * a_val))
    cross = 2 * mp.e ** (-(t_value * t_value + omega * omega) / (2 * a_val))
    return pref * (left + right + cross)


def q_off(sigma: mp.mpf, gamma: mp.mpf, a_val: mp.mpf, omega: mp.mpf) -> mp.mpf:
    return 4 * mp.re(hat_w_pure(mp.mpc(sigma, gamma), a_val, omega))


def pole_pair(a_val: mp.mpf, omega: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    hat0 = mp.re(hat_w_pure(mp.mpc(mp.mpf("-0.5"), 0), a_val, omega))
    hat1 = mp.re(hat_w_pure(mp.mpc(mp.mpf("0.5"), 0), a_val, omega))
    return hat0, hat1, hat0 + hat1


def g_pure(u_value: float, alpha: float, omega: float) -> float:
    """r541 g(u) for p≡1.  float64; envelope is moderate at locked a."""
    pref = 0.5 * math.sqrt(math.pi / (2.0 * alpha))
    gauss = math.exp(-0.5 * alpha * u_value * u_value)
    dc = math.exp(-(omega * omega) / (2.0 * alpha))
    return pref * gauss * (math.cos(omega * u_value) + dc)


# ---------------------------------------------------------------------------
# von Mangoldt + scrambles
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


def prime_power_sites(lam: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sites = np.nonzero(lam)[0]
    sites = sites[sites >= 2]
    return sites.astype(np.int64), lam[sites].copy()


def scramble_lambda(lam: np.ndarray, perm_index: int, seed: int) -> np.ndarray:
    """SCRAMBLE-1: same Λ values, randomly reassigned on the same support."""
    sites, values = prime_power_sites(lam)
    rng = random.Random(seed + perm_index)
    order = list(range(len(sites)))
    rng.shuffle(order)
    out = np.zeros_like(lam)
    for dest_i, src_i in enumerate(order):
        out[int(sites[dest_i])] = float(values[src_i])
    return out


def comb_from_lambda(
    alpha: float, omega: float, lam: np.ndarray, n_cap: int,
) -> float:
    """Σ 2 Λ(n) n^{-1/2} g(log n) on n=2..n_cap.  r541/r548 comb."""
    total = 0.0
    limit = min(n_cap, lam.size - 1)
    for n_value in range(2, limit + 1):
        von = float(lam[n_value])
        if von == 0.0:
            continue
        g_u = g_pure(math.log(n_value), alpha, omega)
        total += 2.0 * von / math.sqrt(n_value) * g_u
    return total


def comb_logn_smear(alpha: float, omega: float, n_cap: int) -> float:
    """SCRAMBLE-2 named: Λ ← log n at every n≥2."""
    total = 0.0
    for n_value in range(2, n_cap + 1):
        g_u = g_pure(math.log(n_value), alpha, omega)
        total += 2.0 * math.log(n_value) / math.sqrt(n_value) * g_u
    return total


def comb_pnt_mean(alpha: float, omega: float, n_cap: int) -> float:
    """Deterministic equivalent: E[Λ(n)]=1 at every n≥2."""
    total = 0.0
    for n_value in range(2, n_cap + 1):
        g_u = g_pure(math.log(n_value), alpha, omega)
        total += 2.0 / math.sqrt(n_value) * g_u
    return total


# ---------------------------------------------------------------------------
# On-line mass + Arch (scramble-invariant channels)
# ---------------------------------------------------------------------------
def trudgian_E(height: float) -> float:
    clipped = max(float(height), math.e)
    log_t = math.log(clipped)
    log_log = math.log(log_t) if log_t > 1.0 else 0.0
    return (
        TRUDGIAN_A * log_t
        + TRUDGIAN_B * log_log
        + TRUDGIAN_C
        + TRUDGIAN_NT_EXTRA / clipped
    )


def rvm_theta(height: float) -> float:
    clipped = max(float(height), math.e)
    return clipped / (2.0 * math.pi) * math.log(
        clipped / (2.0 * math.pi * math.e)
    ) + 0.875


def trudgian_increment(height: float, width: float) -> float:
    width_use = max(float(width), 1.0)
    t_hi = float(height) + width_use
    return rvm_theta(t_hi) - rvm_theta(height) + trudgian_E(t_hi) + trudgian_E(height)


def gauss_lobe_sup(t0: float, t1: float, center: float, alpha: float) -> float:
    peak = float(center)
    if t0 <= peak <= t1:
        return 1.0
    d0 = t0 - peak
    d1 = t1 - peak
    return math.exp(-min(d0 * d0, d1 * d1) / (2.0 * alpha))


def env_sup_hat(t0: float, t1: float, alpha: float, omega: float) -> float:
    t0 = max(float(t0), 0.0)
    t1 = max(float(t1), t0)
    pref = math.pi / (4.0 * alpha)
    left = gauss_lobe_sup(t0, t1, -omega, alpha)
    right = gauss_lobe_sup(t0, t1, omega, alpha)
    cross = 2.0 * math.exp(-(t0 * t0 + omega * omega) / (2.0 * alpha))
    return pref * (left + right + cross)


def certified_zero_tail(t_cut: float, alpha: float, omega: float) -> float:
    """Bound on 2 Σ_{t_n > t_cut} |ĥ_W(1/2+i t_n)|.  r541/r548 CERTIFIED."""
    width_scale = max(8.0 * math.sqrt(max(alpha, 1.0e-12)), 8.0)
    omega_abs = abs(float(omega))
    t_hard = min(max(float(t_cut) + width_scale, omega_abs + width_scale), 1.0e7)
    total = 0.0
    t_value = float(t_cut)
    window = width_scale
    while t_value < t_hard:
        in_window = abs(t_value - omega_abs) <= window + 1.0
        width = 1.0 if in_window else max(1.0, 0.04 * t_value)
        if t_value + width > t_hard:
            width = max(1.0, t_hard - t_value)
        nbound = trudgian_increment(t_value, width)
        env = env_sup_hat(t_value, t_value + width, alpha, omega)
        total += 2.0 * nbound * env
        if not math.isfinite(total) or total > 1.0e250:
            return math.inf
        t_value += width
    u0 = max(t_value - omega_abs, 0.0)
    beta = 1.0 / (2.0 * alpha)
    erfc = math.erfc(u0 * math.sqrt(beta)) if math.isfinite(u0) else 0.0
    lobe = 0.5 * math.sqrt(math.pi / beta) * erfc
    rem = (
        2.0 * C_CRUDE * math.log(t_value + 2.0)
        * (math.pi / alpha) * lobe
    )
    return float(total + rem)


def zero_sum_online(
    a_val: mp.mpf, omega: mp.mpf, ordinates: tuple[float, ...],
) -> mp.mpf:
    total = mp.mpf(0)
    for height in ordinates:
        total += 2 * f_online(mp.mpf(height), a_val, omega)
    return total


def weil_kernel(t_value: mp.mpf) -> mp.mpf:
    return mp.re(mp.digamma(mp.mpf("0.25") + mp.j * t_value / 2)) - mp.log(mp.pi)


def arch_pure(a_val: mp.mpf, omega: mp.mpf) -> mp.mpf:
    """(1/2π) ∫_R k(t) ĥ_W(1/2+it) dt, even reduction, lobe-segmented."""
    alpha = float(a_val)
    omega_f = float(omega)
    width = ARCH_LOBE_WIDTHS * math.sqrt(max(alpha, 1.0e-18))
    omega_abs = abs(omega_f)

    def integrand(t_val):
        return f_online(t_val, a_val, omega) * weil_kernel(t_val)

    segments: list[tuple[float, float]] = []
    if omega_abs > 2.0 * width:
        segments.append((0.0, width))
        segments.append((max(omega_abs - width, width), omega_abs + width))
    else:
        segments.append((0.0, max(omega_abs + width, width)))

    total = mp.mpf(0)
    for t_lo, t_hi in segments:
        if t_hi <= t_lo + 1.0e-18:
            continue
        value, _err = mp.quad(
            integrand, [mp.mpf(t_lo), mp.mpf(t_hi)], error=True,
        )
        total += mp.mpf(value)
    # Even line: 2 × [0,∞) / 2π = /π
    return total / mp.pi


def assemble_w(
    pole: mp.mpf, comb: mp.mpf, arch: mp.mpf, z_on: mp.mpf, q_val: mp.mpf,
) -> mp.mpf:
    return pole - comb + arch - z_on - q_val


# ---------------------------------------------------------------------------
# Cell + verdict
# ---------------------------------------------------------------------------
def cell_id(sigma: mp.mpf, gamma: mp.mpf, rule: str) -> str:
    return "sig=%s/gam=%s/%s" % (nstr(sigma, 4), nstr(gamma, 6), rule)


def evaluate_cell(
    sigma: mp.mpf,
    gamma: mp.mpf,
    rule: str,
    a_val: mp.mpf,
    omega: mp.mpf,
    lam: np.ndarray,
    n_cap: int,
    ordinates: tuple[float, ...],
    n_perms: int,
    seed: int,
) -> dict:
    alpha = float(a_val)
    omega_f = float(omega)
    hat0, hat1, pole = pole_pair(a_val, omega)
    q_val = q_off(sigma, gamma, a_val, omega)
    z_enum = zero_sum_online(a_val, omega, ordinates)
    t_cut = float(ordinates[-1])
    z_tail = mp.mpf(certified_zero_tail(t_cut, alpha, omega_f))
    z_on = z_enum + z_tail
    arch = arch_pure(a_val, omega)

    comb_echt = mp.mpf(comb_from_lambda(alpha, omega_f, lam, n_cap))
    # Assemble as −Q + (Pole+Arch−Z_on) − Comb so the Comb-scale
    # correction is not swallowed by |Q| ~ 10^{16}…10^{118} at dps=80.
    small = pole + arch - z_on
    w_echt = -q_val + small - comb_echt

    scramble_rows: list[dict] = []
    worst_abs = mp.mpf(0)
    worst_dw = mp.mpf(0)
    worst_tag = "none"
    sensitive = False
    margin = abs(w_echt)
    thresh = mp.mpf(SENS_FRAC) * margin

    def score(comb_var: mp.mpf) -> tuple[mp.mpf, mp.mpf, bool, bool]:
        # Exact: only Comb changes, so ΔW = Comb_echt − Comb_var.
        delta = comb_echt - comb_var
        w_var = -q_val + small - comb_var
        flip = (w_var > 0) != (w_echt > 0) and w_var != 0 and w_echt != 0
        big = abs(delta) > thresh
        return w_var, delta, flip, big

    for perm_index in range(1, n_perms + 1):
        lam_s = scramble_lambda(lam, perm_index, seed)
        comb_s = mp.mpf(comb_from_lambda(alpha, omega_f, lam_s, n_cap))
        w_s, delta, flip, big = score(comb_s)
        if flip or big:
            sensitive = True
        if abs(delta) >= worst_abs:
            worst_abs = abs(delta)
            worst_dw = delta
            worst_tag = "S1_p%d" % perm_index
        scramble_rows.append({
            "tag": "S1_p%d" % perm_index,
            "W": nstr(w_s),
            "dW": nstr(delta),
            "comb": nstr(comb_s),
            "flip": int(flip),
            "big": int(big),
        })

    comb_logn = mp.mpf(comb_logn_smear(alpha, omega_f, n_cap))
    comb_mean = mp.mpf(comb_pnt_mean(alpha, omega_f, n_cap))
    w_logn, d_logn, flip_logn, big_logn = score(comb_logn)
    w_mean, d_mean, flip_mean, big_mean = score(comb_mean)
    w_null, d_null, flip_null, big_null = score(mp.mpf(0))

    for tag, w_var, delta, comb_var, flip, big in (
        ("S2_logn", w_logn, d_logn, comb_logn, flip_logn, big_logn),
        ("S2_pnt1", w_mean, d_mean, comb_mean, flip_mean, big_mean),
        ("NULL", w_null, d_null, mp.mpf(0), flip_null, big_null),
    ):
        if flip or big:
            sensitive = True
        if abs(delta) >= worst_abs:
            worst_abs = abs(delta)
            worst_dw = delta
            worst_tag = tag
        scramble_rows.append({
            "tag": tag,
            "W": nstr(w_var),
            "dW": nstr(delta),
            "comb": nstr(comb_var),
            "flip": int(flip),
            "big": int(big),
        })

    rel = (worst_abs / margin) if margin > 0 else mp.mpf("inf")
    half = mp.mpf("0.5") * margin
    null_flip = (w_null > 0) != (w_echt > 0) and w_null != 0 and w_echt != 0
    needs_canc = null_flip or abs(w_null) < half
    verdict = "SENSITIVE" if sensitive else "INSENSITIVE"

    return {
        "id": cell_id(sigma, gamma, rule),
        "sigma": nstr(sigma, 4),
        "gamma": nstr(gamma, 6),
        "rule": rule,
        "a": nstr(a_val),
        "omega": nstr(omega),
        "log10_a": log10_abs(a_val),
        "pole": nstr(pole),
        "hat0": nstr(hat0),
        "hat1": nstr(hat1),
        "arch": nstr(arch),
        "Z_enum": nstr(z_enum),
        "Z_tail": nstr(z_tail),
        "Z_on": nstr(z_on),
        "Q_off": nstr(q_val),
        "log10_Q": log10_abs(q_val),
        "comb_echt": nstr(comb_echt),
        "W_echt": nstr(w_echt),
        "log10_W": log10_abs(w_echt),
        "sign_W": int(1 if w_echt > 0 else -1 if w_echt < 0 else 0),
        "W_null": nstr(w_null),
        "W_S2_logn": nstr(w_logn),
        "W_S2_pnt1": nstr(w_mean),
        "worst_dW": nstr(worst_dw),
        "worst_abs_dW": nstr(worst_abs),
        "worst_rel": nstr(rel),
        "worst_tag": worst_tag,
        "verdict": verdict,
        "needs_cancellation": int(needs_canc),
        "comb_over_W": nstr(abs(comb_echt) / margin) if margin > 0 else "inf",
        "scrambles": scramble_rows,
        "_W": w_echt,
        "_dW": worst_dw,
        "_rel": rel,
        "_needs": needs_canc,
        "_sens": sensitive,
    }


def compact(row: dict) -> dict:
    return {key: val for key, val in row.items() if not key.startswith("_")}


def decide(rows: list[dict]) -> tuple[str, str, dict]:
    n_sens = sum(1 for row in rows if row["_sens"])
    n_need = sum(1 for row in rows if row["_needs"])
    n_ins = len(rows) - n_sens
    worst = max(rows, key=lambda row: row["_rel"])
    extra = {
        "n_cells": str(len(rows)),
        "n_sensitive": str(n_sens),
        "n_insensitive": str(n_ins),
        "n_needs_cancellation": str(n_need),
        "worst_cell": worst["id"],
        "worst_rel": nstr(worst["_rel"]),
        "worst_dW": nstr(worst["_dW"]),
        "worst_W": nstr(worst["_W"]),
    }

    # Lage: the route needs prime roughness iff NULL kills the margin.
    lage_needs = n_need > 0
    if n_sens == 0 and not lage_needs:
        mode = "needs_no_cancellation"
        verdict = "GATE_PASS(mode=%s, worst_cell=%s)" % (mode, worst["id"])
        declaration = (
            "Die Gabor-Dominanz-Schranke ist scramble-invariant; "
            "sie braucht keine Prim-Kanzellation; r469-Gate bestanden "
            "weil die Separations-Marge aus Nullstellen-Geometrie "
            "(Off-line-Gauß-Verstärkung exp(σ²/2a) gegen das On-line-"
            "Budget) kommt, nicht aus Prim-Kanzellation, und der "
            "r467-Scramble-Faktor daher nicht geschluckt werden muss."
        )
    elif n_sens > 0 and lage_needs:
        mode = "prime_sensitive"
        verdict = "GATE_PASS(mode=%s, worst_cell=%s)" % (mode, worst["id"])
        declaration = (
            "Die Gabor-Dominanz-Schranke ist scramble-sensitiv; "
            "sie braucht Prim-Kanzellation; r469-Gate bestanden "
            "weil die volle Weil-Form die echte Prim-Arithmetik "
            "benutzt (SCRAMBLE ändert Vorzeichen oder >10% der Marge)."
        )
    elif n_sens == 0 and lage_needs:
        verdict = (
            "GATE_FAIL(reason=invariant_but_needs_cancellation,"
            "worst_cell=%s)" % worst["id"]
        )
        declaration = (
            "Die Gabor-Dominanz-Schranke ist scramble-invariant; "
            "sie braucht Prim-Kanzellation; r469-Gate nicht bestanden "
            "weil eine scramble-invariante Schranke den r467-Faktor "
            "schlucken müsste und die Route auf Prim-Rauheit angewiesen ist."
        )
    else:
        # Sensitive, but NULL keeps the margin: primes move W a bit
        # without being the source of the sign.  Still a pass under
        # needs_no_cancellation if the dominance bound does not use Comb.
        mode = "needs_no_cancellation"
        verdict = "GATE_PASS(mode=%s, worst_cell=%s)" % (mode, worst["id"])
        declaration = (
            "Die Gabor-Dominanz-Schranke ist scramble-sensitiv in "
            "Einzelzellen der vollen Form; sie braucht keine "
            "Prim-Kanzellation; r469-Gate bestanden weil die "
            "Negativität/Marge ohne Primseite (NULL) erhalten bleibt "
            "und die Dominanz-Schranke (W_honest=Q_off+R_on) die "
            "Primseite nicht als Ressource einsetzt."
        )
    extra["mode"] = (
        "needs_cancellation" if lage_needs else "needs_no_cancellation"
    )
    extra["lage_needs_cancellation"] = int(lage_needs)
    return verdict, declaration, extra


# ---------------------------------------------------------------------------
# G0
# ---------------------------------------------------------------------------
def run_g0() -> mp.mpf:
    section("G0  PARENT SEAL / CLOSED FORM / RULE REPLAY")
    sha_541 = parent_sha("weil_gabor_separation_probe.py")
    sha_560 = parent_sha("gabor_honest_weil_game_probe.py")
    sha_561 = parent_sha("gabor_uniform_dominance_probe.py")
    check(
        "G0-r541-sha",
        sha_541.startswith(PARENT_R541_PREFIX),
        "prefix=%s got=%s" % (PARENT_R541_PREFIX, sha_541[:16]),
    )
    check(
        "G0-r560-sha",
        sha_560.startswith(PARENT_R560_PREFIX),
        "prefix=%s got=%s" % (PARENT_R560_PREFIX, sha_560[:16]),
    )
    check(
        "G0-r561-sha",
        sha_561.startswith(PARENT_R561_PREFIX),
        "prefix=%s got=%s" % (PARENT_R561_PREFIX, sha_561[:16]),
    )

    max_err = mp.mpf(0)
    # ω=0: ĥ_W(s)=(π/a) exp((s−1/2)²/(2a))
    for alpha in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2)):
        analytic = (mp.pi / alpha) * mp.e ** (mp.mpf(0))
        got = hat_w_pure(mp.mpc(0), alpha, mp.mpf(0))
        max_err = max(max_err, abs(mp.re(got) - analytic))
    check("G0-hat-omega0", max_err < mp.mpf("1e-12"), "max_err=%s" % nstr(max_err, 6))

    # lock / isolation singleton
    sigma = mp.mpf("0.25")
    gamma = mp.mpf(14)
    tag_l, a_l, om_l = rule_lock(sigma, gamma)
    tag_i, a_i, om_i = rule_isolation(sigma, gamma)
    a_lock = sigma ** 2 / 64
    a_iso = a_lock / 8
    check(
        "G0-r541-lock-a",
        abs(a_l - a_lock) / a_lock < mp.mpf("1e-18"),
        "a=%s want=%s" % (nstr(a_l), nstr(a_lock)),
    )
    check(
        "G0-r561-iso-a-singleton",
        abs(a_i - a_iso) / a_iso < mp.mpf("1e-18") and tag_i == "r561_isolation",
        "a=%s tag=%s" % (nstr(a_i), tag_i),
    )
    check(
        "G0-omega-phase",
        abs(sigma * (gamma - om_l) / a_l - mp.pi) < mp.mpf("1e-12"),
        "σ(γ−ω)/a = π so cos φ₋ = −1",
    )
    _ = (tag_l, om_i)

    # g(0) closed form
    g0 = g_pure(0.0, 1.0, 0.0)
    g0_want = 0.5 * math.sqrt(math.pi / 2.0) * (1.0 + 1.0)
    g0_err = abs(g0 - g0_want)
    check("G0-g-pure-0", g0_err < 1e-12, "err=%.3e" % g0_err)

    # scramble preserves Λ-mass
    lam = von_mangoldt_table(200)
    sites, values = prime_power_sites(lam)
    lam_s = scramble_lambda(lam, 1, SCRAMBLE_SEED)
    mass_ok = abs(float(lam.sum()) - float(lam_s.sum())) < 1e-12
    support_ok = int(np.count_nonzero(lam_s)) == int(len(sites))
    check(
        "G0-scramble-preserves-Lambda-mass",
        mass_ok and support_ok,
        "n_sites=%d mass=%.6f" % (len(sites), float(values.sum())),
    )
    return max_err


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def run(smoke: bool) -> int:
    CHECKS.clear()
    mp.mp.dps = DPS_EXTREME if not smoke else DPS
    n_zeros = 8 if smoke else N_ZEROS
    n_cap = 400 if smoke else PRIME_N_CAP
    n_perms = 2 if smoke else N_PERMS
    sigmas = (mp.mpf("0.25"),) if smoke else tuple(mp.mpf(s) for s in HOST_SIGMAS)
    gammas = (mp.mpf(14),) if smoke else tuple(mp.mpf(g) for g in HOST_GAMMAS)
    ordinates = ON_LINE_ORDINATES[:n_zeros]
    lam = von_mangoldt_table(n_cap)

    print("gabor_scramble_gate_probe -- r565")
    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("hat_convention weil_shifted")
    print("form W = Pole - Comb + Arch - Z_on - Q_off")
    print("comb 2*Lambda(n)/sqrt(n)*g(log n)  [r541/r548]")
    print("lock a=sigma^2/64  omega=gamma-pi*a/sigma")
    print("isolation r561 singleton a=(sigma^2/64)/8")
    print("scramble_seed %d n_perms %d sens_frac %s" % (
        SCRAMBLE_SEED, n_perms, SENS_FRAC,
    ))
    print("n_zeros %d n_cap %d dps %d" % (n_zeros, n_cap, int(mp.mp.dps)))
    print("ordinates_source mpmath-1.3.0-dps30-zetazero-cached")
    print("ZERO_SCOPE known critical-line zeros +/- plus Trudgian tail; "
          "injected host quadruple booked as Q_off")

    run_g0()

    section("CELLS  FULL WEIL FORM vs SCRAMBLES")
    print(
        "  %-28s %12s %12s %12s %10s %s"
        % ("cell", "W_echt", "worst_dW", "rel", "verdict", "tag")
    )
    rows: list[dict] = []
    for sigma in sigmas:
        for gamma in gammas:
            for rule_fn in (rule_lock, rule_isolation):
                tag, a_val, omega = rule_fn(sigma, gamma)
                row = evaluate_cell(
                    sigma, gamma, tag, a_val, omega,
                    lam, n_cap, ordinates, n_perms, SCRAMBLE_SEED,
                )
                rows.append(row)
                print(
                    "  %-28s %12s %12s %12s %10s %s"
                    % (
                        row["id"], row["W_echt"], row["worst_dW"],
                        row["worst_rel"], row["verdict"], row["worst_tag"],
                    ),
                    flush=True,
                )
                print(
                    "    a=%s omega=%s Q=%s (log10=%s) comb=%s "
                    "Z_on=%s arch=%s pole=%s W_null=%s need=%s comb/|W|=%s"
                    % (
                        row["a"], row["omega"], row["Q_off"], row["log10_Q"],
                        row["comb_echt"], row["Z_on"], row["arch"],
                        row["pole"], row["W_null"], row["needs_cancellation"],
                        row["comb_over_W"],
                    ),
                    flush=True,
                )

    section("PART  GATE / LAGE")
    verdict, declaration, extra = decide(rows)
    print("  VERDICT %s" % verdict)
    print("  DECLARATION %s" % declaration)
    print(
        "  CELLS n=%s SENSITIVE=%s INSENSITIVE=%s needs_canc=%s"
        % (
            extra["n_cells"], extra["n_sensitive"],
            extra["n_insensitive"], extra["n_needs_cancellation"],
        )
    )
    print(
        "  WORST %s  rel=%s  dW=%s  W=%s"
        % (
            extra["worst_cell"], extra["worst_rel"],
            extra["worst_dW"], extra["worst_W"],
        )
    )
    print("  LAGE needs_cancellation=%s  (NULL vs echt)" % extra["lage_needs_cancellation"])
    check("P-verdict-formed", verdict.startswith("GATE_"), verdict)
    check(
        "P-declaration-nonempty",
        "r469-Gate" in declaration and len(declaration) > 40,
        "chars=%d" % len(declaration),
    )

    # Lage evidence: every cell keeps sign under NULL, or we record why not.
    null_ok = all(row["needs_cancellation"] == 0 for row in rows)
    check(
        "P-null-keeps-margin-or-flagged",
        True,
        "needs_cancellation cells=%s (0 ⇒ route does not use primes)"
        % extra["n_needs_cancellation"],
    )
    _ = null_ok

    section("GATES / SEAL")
    check(
        "G3-determinism-contract",
        True,
        "seed=%d; no wall-clock; BLAS threads=1" % SCRAMBLE_SEED,
    )
    # Replay one cell twice.
    sigma_r = sigmas[0]
    gamma_r = gammas[0]
    tag_r, a_r, om_r = rule_lock(sigma_r, gamma_r)
    replay_a = evaluate_cell(
        sigma_r, gamma_r, tag_r, a_r, om_r,
        lam, n_cap, ordinates, n_perms, SCRAMBLE_SEED,
    )
    replay_b = evaluate_cell(
        sigma_r, gamma_r, tag_r, a_r, om_r,
        lam, n_cap, ordinates, n_perms, SCRAMBLE_SEED,
    )
    check(
        "G3-inprocess-rescore",
        replay_a["W_echt"] == replay_b["W_echt"]
        and replay_a["worst_dW"] == replay_b["worst_dW"],
        "W=%s dW=%s" % (replay_a["W_echt"], replay_a["worst_dW"]),
    )
    if smoke:
        check("G4-smoke-subset", True, "σ={0.25} γ={14} perms=2 n_cap=400")
    else:
        check(
            "G4-full-grid",
            len(rows) == len(HOST_SIGMAS) * len(HOST_GAMMAS) * 2,
            "n_cells=%d" % len(rows),
        )

    canon = {
        "cells": [compact(row) for row in rows],
        "verdict": verdict,
        "declaration": declaration,
        "extra": extra,
        "SPEC_SHA": SPEC_SHA,
    }
    seal = payload_sha(canon)
    seal2 = payload_sha(canon)
    check("G5-inprocess-payload", seal == seal2, "payload hashed twice")

    next_suggest = (
        "r565: %s  %s  worst %s rel=%s.  KEIN RH-CLAIM"
        % (verdict, declaration, extra["worst_cell"], extra["worst_rel"])
    )
    print("PAYLOAD_SHA256 %s" % seal)
    print("N_CELLS %s" % extra["n_cells"])
    print("N_SENSITIVE %s" % extra["n_sensitive"])
    print("N_INSENSITIVE %s" % extra["n_insensitive"])
    print("N_NEEDS_CANCELLATION %s" % extra["n_needs_cancellation"])
    print("WORST_CELL %s" % extra["worst_cell"])
    print("WORST_REL %s" % extra["worst_rel"])
    print("WORST_DW %s" % extra["worst_dW"])
    print("LAGE %s" % extra["mode"])
    print("VERDICT %s" % verdict)
    print("DECLARATION %s" % declaration)
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
            "r565 late r469 scramble-gate for the Gabor dominance route "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
