#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_first_contact_selberg_probe -- r638  GABOR.CONTACT.SELBERG.01

SPEC r638 — GABOR.CONTACT.SELBERG.01  (pre-registered)

Object. Pure-Gabor zero side G(a,ω) := POLE − PRIME + ARCH (= Z of r608
identity A). Attack under test: "first contact + Selberg square
completion": if G<0 somewhere, the first touching point (a*,ω*) as a
decreases from large a satisfies G=0, ∂_ωG=0, ∂²_ωG≥0, ∂_aG≥0;
derivatives insert powers of u=log n into PRIME; Selberg's symmetry
Λ(n)log n + (Λ∗Λ)(n) = Λ₂(n) := Σ_{d|n} μ(d) log²(n/d) is supposed to
produce a square ‖A‖² so that some operator ℒ gives ℒG = ‖A‖² + R ≥ 0
at contact, contradicting the contact conditions.

Toeplitz gate (pre-registered kill). A square of a prime Dirichlet
polynomial |Σ a_n n^{iω}|² has ω-frequencies log m − log n (Toeplitz).
The Selberg convolution term Σ_N (Λ∗Λ)(N) ψ(log N) =
Σ_{m,n} Λ(m)Λ(n) ψ(log m + log n) has frequencies log m + log n (Hankel).
A Hankel form is a nonnegative quadratic form iff the kernel matrix
[ψ(u_i+u_j)] is PSD (exponential convexity). Gate G2: does any real
combination of the operator-generated ψ's give a PSD Hankel matrix on
the prime-power nodes? Pre-registered: FAIL ⇒ TOEPLITZ_GATE_FAIL ⇒
lane KILLED(STRUCTURAL). Only if G2 passes does T4 decide.

Closed forms (u = log n, D := e^{−ω²/(2a)}, C := √(π/(2a)),
w(n) := Λ(n) n^{−1/2} e^{−au²/2}):
  PRIME      = C Σ w(n) [cos(ωu) + D]
  ∂_ω PRIME  = C Σ w(n) [−u sin(ωu) − (ω/a) D]
  ∂²_ω PRIME = C Σ w(n) [−u² cos(ωu) + (ω²/a² − 1/a) D]
  ∂_a PRIME  = C Σ w(n) [−(u²/2 + 1/(2a)) cos(ωu)
                        + (−u²/2 − 1/(2a) + ω²/(2a²)) D]
Selberg insertion: Λ(n)u = Λ₂(n) − (Λ∗Λ)(n);
Λ(n)u² = [Λ₂(n) − (Λ∗Λ)(n)]·u.
Structural values (verified against direct divisor-sum convolution):
n=p^k: Λ₂=(2k−1)log²p, (Λ∗Λ)=(k−1)log²p;
n=p^a q^b (two distinct primes): Λ₂=(Λ∗Λ)=2 log p log q; otherwise both 0.
Selberg part of ∂_ω PRIME  := +C Σ_N (Λ∗Λ)(N) N^{−1/2} e^{−a(log N)²/2}
  sin(ω log N)      (Λ₂ part = −C Σ Λ₂(N)(...)sin)
Selberg part of ∂²_ω PRIME := +C Σ_N (Λ∗Λ)(N) N^{−1/2} e^{−a(log N)²/2}
  (log N) cos(ω log N)  (Λ₂ part = −C Σ Λ₂(N)(...)(log N)cos)
"Helpful" sign at a local minimum of G: the Selberg part of ∂²_ω PRIME
is < 0 (it then pushes ∂²_ωG = ∂²_ω(POLE+ARCH) − ∂²_ω PRIME upward).

Constants: ROUND=638, SEED=638202609, A_T1=(0.5,0.3),
OMEGA_T1=(14.134725,21.022040,25.010858,30.424876,40.0),
N_SELBERG_VERIFY=200000, N_HANKEL=3000, A_GATE=(1.0,0.5,0.3,0.1,0.05),
OMEGA_GATE=(14.134725,30.0,100.0), K_MAX=4, N_STARTS=64, GATE_TOL=1e-9,
A_T4=(1.0,0.5,0.3), OMEGA_T4_LO=10.0, OMEGA_T4_HI=50.0, OMEGA_T4_STEP=0.01,
TAIL_TARGET=1e-12, N_PRIME_CAP=15000000, N_ONLINE=2000,
CATALOGS=((0.4,100.0),(0.25,100.0),(0.1,100.0),(0.4,250.0)) as (σ,γ₀),
A_SCAN_HI=5.0, A_SCAN_LO=1e-3, N_A_SCAN=60, BISECT_ITERS=40,
OMEGA_HALFWIDTH=3.0, N_OMEGA_GRID=6001, FD_REL=1e-4, HEAT_TOL_COS=1e-8,
HEAT_TOL_LOBE=1e-12, SIGN_STRUCTURAL_H=0.9, SIGN_STRUCTURAL_F=0.5,
WORLD_BLIND_DH=0.15, MIN_MINIMA=30, EULER_LOCAL_A_MAX=0.3,
EULER_LOCAL_OMEGA_MIN=30.0. T0 FD points {(0.5,14.134725),(0.5,30.0),
(0.3,21.022040)}, h_ω=1e-4, h_a=1e-5·a, T0_FD_MATCH rel≤1e-6,
T0_COS_HEAT_EXACT cosine heat residual 1e-12 relative.
T1_SELBERG_IDENTITY max|Λ log n + Λ∗Λ − Λ₂|≤1e-9·max Λ₂.
T1_SIGN_INDEFINITE ≥10 sign changes of Selberg ∂²_ω PRIME on ω∈[10,50]
step 0.01 at a=0.5 and a=0.3.
T2 family Ψ(a,ω)={t^k e^{−t/2} e^{−at²/2}·φ(t): k=0..K_MAX,
φ∈{cos(ωt),sin(ωt),1}} (15). G2 projected gradient ascent step 0.1
with backtracking, 500 iterations, N_STARTS random + 15 coordinate
directions. GATE_PASS iff best λ_min≥−GATE_TOL at ANY (a,ω), else
TOEPLITZ_GATE_FAIL. T2_GATE_EVALUATED: all 15 matrices finite symmetric.
G3 b_{p,k}=2Λ(p^k)p^{−k/2}·½√(π/(2a))e^{−a(k log p)²/2};
DC_lower=Σ_p(|b_{p,1}|−Σ_{k≥2}|b_{p,k}|); M=r608 prime_abs; B=POLE+ARCH.
EULER_LOCAL_SQUARE_COSTS_TRIVIAL_MAJORANT if min DC_lower/B over
a≤EULER_LOCAL_A_MAX, ω≥EULER_LOCAL_OMEGA_MIN is >1, else
EULER_LOCAL_BUDGET_OK.
T3 multiplicity: on-line conjugate pair m=1 each, summed as
2·hat_online(γ) (r608.zero_sum_online); off-line FE quadruple m=1 each
via r605.expand_partners + r608.re_hat_delta (= 4 Re ĥ(σ+iγ₀) by
evenness). Z_lobe = Re Σ m(ρ)(π/(4a)) e^{(δ−iω)²/(2a)} (E₋ lobe only;
δ=ρ−1/2; four partners off-line, both ρ and ρ̄ on-line).
T3_CONTACT_FOUND a*∈(A_SCAN_LO,A_SCAN_HI); T3_CONTACT_CONDITIONS
|Z|≤1e-6·background, ∂²_ωZ≥−1e-6·background/a*, ∂_aZ≥−1e-6·background/a*;
T3_CONTACT_OFFLINE_DRIVEN |off-line|≥0.5·|on-line| at (a*,ω*) for every
catalog; T3_HEAT_REDUNDANCY_LOBE r_heat≤HEAT_TOL_LOBE; T3_HEAT_REDUNDANCY_COS
r_heat≤HEAT_TOL_COS; T3_NEGATIVITY_DOWNSET m(a*/2,4,8) all<0;
T3_MAIN_POSITIVE all MAIN min_ω Z>0; T3_MP_AGREE rel 1e-9.
T3 a* := a_pos (last m≥0 bracket end); ω* := argmin_ω Z(a_neg,ω).
T4_EF_SANITY rel 1e-6 vs Σ 2·hat_online at a∈{1.0,0.5},
ω∈{14.134725,30.0}. SELBERG_SIGN_STRUCTURAL if some MAIN a has
n_minima≥MIN_MINIMA and h≥SIGN_STRUCTURAL_H and median f2≥SIGN_STRUCTURAL_F,
else SELBERG_SIGN_INDEFINITE. WORLD_BLIND if |h_MAIN−h_SCR|<WORLD_BLIND_DH
and |h_MAIN−h_WPERM|<WORLD_BLIND_DH at every a, else WORLD_SEPARATING.
If a=0.3 in T4 is too slow, OMEGA_T4_HI is reduced to 40.0 for a=0.3
only (recorded here). Single-threaded env vars as r608. All randomness
from numpy default_rng(SEED). n_per arch: r608 full 48 / smoke 24.

Smoke (--smoke): T0 one point; T1 N=20000 and one (a,ω)=(0.5,14.134725),
sign-change count on ω∈[10,20] step 0.05; T2 one (a,ω)=(0.5,30.0),
N_HANKEL=500, N_STARTS=8, 100 iterations; G3 one point (0.5,30.0);
T3 one catalog (0.4,100.0), N_OMEGA_GRID=1201, N_A_SCAN=20,
BISECT_ITERS=20, Z_cos only plus Z_lobe at the found point; T4 a=1.0
only, ω∈[10,30] step 0.05, MAIN + SCRAMBLE only; MAIN control at one a.

CLAIM BOUNDARY.  Finite closed-form / seeded arithmetic on synthetic
off-line catalogs plus a frozen on-line ordinate table, and a
truncated von Mangoldt comb.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/verification/website/next.txt edit.  KEIN RH-CLAIM.

Verdict tokens:
  KILLED(STRUCTURAL: selberg-convolution-is-hankel)
  TOEPLITZ_GATE_FAIL(best_lambda_min=…)
  GATE_PASS(a=…,omega=…,c=…)
  EULER_LOCAL_SQUARE_COSTS_TRIVIAL_MAJORANT
  EULER_LOCAL_BUDGET_OK
  CONTACT_CONDITIONS_COLLAPSE(r_heat_lobe=…, r_heat_cos=…)
  NEGATIVITY_DOWNSET
  SELBERG_SIGN_STRUCTURAL / SELBERG_SIGN_INDEFINITE
  WORLD_BLIND / WORLD_SEPARATING

r638 seal note: T3 argmin taken on the negative bracket side (first seal
reported the on-line-gap argmin for (0.1,100)); CHECK
T3_CONTACT_OFFLINE_DRIVEN added.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
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

import gabor_tropical_heat_probe as r608  # noqa: E402

ROUND = 638
SEED = 638202609
A_T1 = (0.5, 0.3)
OMEGA_T1 = (14.134725, 21.022040, 25.010858, 30.424876, 40.0)
N_SELBERG_VERIFY = 200_000
N_HANKEL = 3000
A_GATE = (1.0, 0.5, 0.3, 0.1, 0.05)
OMEGA_GATE = (14.134725, 30.0, 100.0)
K_MAX = 4
N_STARTS = 64
GATE_TOL = 1e-9
A_T4 = (1.0, 0.5, 0.3)
OMEGA_T4_LO = 10.0
OMEGA_T4_HI = 50.0
OMEGA_T4_STEP = 0.01
TAIL_TARGET = 1e-12
N_PRIME_CAP = 15_000_000
N_ONLINE = 2000
CATALOGS = ((0.4, 100.0), (0.25, 100.0), (0.1, 100.0), (0.4, 250.0))
A_SCAN_HI = 5.0
A_SCAN_LO = 1e-3
N_A_SCAN = 60
BISECT_ITERS = 40
OMEGA_HALFWIDTH = 3.0
N_OMEGA_GRID = 6001
FD_REL = 1e-4
HEAT_TOL_COS = 1e-8
HEAT_TOL_LOBE = 1e-12
SIGN_STRUCTURAL_H = 0.9
SIGN_STRUCTURAL_F = 0.5
WORLD_BLIND_DH = 0.15
MIN_MINIMA = 30
EULER_LOCAL_A_MAX = 0.3
EULER_LOCAL_OMEGA_MIN = 30.0
T0_POINTS = ((0.5, 14.134725), (0.5, 30.0), (0.3, 21.022040))
H_OMEGA_T0 = 1e-4
N_ARCH_FULL = 48
N_ARCH_SMOKE = 24
PHI_GOLDEN = 0.5 * (1.0 + math.sqrt(5.0))
RESULT_PATH = HERE / "gabor_first_contact_selberg_result.json"
PSI_PHIS = ("cos", "sin", "dc")

SPEC = {
    "round": ROUND,
    "tag": "r638",
    "contract": "GABOR.CONTACT.SELBERG.01",
    "parent": "r608 GABOR.TROPICAL.01",
    "seed": SEED,
    "A_T1": list(A_T1),
    "OMEGA_T1": list(OMEGA_T1),
    "N_SELBERG_VERIFY": N_SELBERG_VERIFY,
    "N_HANKEL": N_HANKEL,
    "A_GATE": list(A_GATE),
    "OMEGA_GATE": list(OMEGA_GATE),
    "K_MAX": K_MAX,
    "N_STARTS": N_STARTS,
    "GATE_TOL": GATE_TOL,
    "A_T4": list(A_T4),
    "OMEGA_T4_LO": OMEGA_T4_LO,
    "OMEGA_T4_HI": OMEGA_T4_HI,
    "OMEGA_T4_STEP": OMEGA_T4_STEP,
    "TAIL_TARGET": TAIL_TARGET,
    "N_PRIME_CAP": N_PRIME_CAP,
    "N_ONLINE": N_ONLINE,
    "CATALOGS": [list(c) for c in CATALOGS],
    "A_SCAN_HI": A_SCAN_HI,
    "A_SCAN_LO": A_SCAN_LO,
    "N_A_SCAN": N_A_SCAN,
    "BISECT_ITERS": BISECT_ITERS,
    "OMEGA_HALFWIDTH": OMEGA_HALFWIDTH,
    "N_OMEGA_GRID": N_OMEGA_GRID,
    "FD_REL": FD_REL,
    "HEAT_TOL_COS": HEAT_TOL_COS,
    "HEAT_TOL_LOBE": HEAT_TOL_LOBE,
    "SIGN_STRUCTURAL_H": SIGN_STRUCTURAL_H,
    "SIGN_STRUCTURAL_F": SIGN_STRUCTURAL_F,
    "WORLD_BLIND_DH": WORLD_BLIND_DH,
    "MIN_MINIMA": MIN_MINIMA,
    "EULER_LOCAL_A_MAX": EULER_LOCAL_A_MAX,
    "EULER_LOCAL_OMEGA_MIN": EULER_LOCAL_OMEGA_MIN,
    "identity_A": "Z = POLE + ARCH - PRIME",
    "hat": "pureGaborHatDelta r608",
    "multiplicity": (
        "on-line m=1 each of {γ,-γ} as 2*hat_online; "
        "off-line FE quadruple m=1 via expand_partners"
    ),
    "omega_t4_hi_a03_fallback": 40.0,
    "t3_a_star": "a_pos",
    "t3_omega_star": "argmin_at_a_neg",
    "seal_note": (
        "T3 argmin on negative bracket side; T3_CONTACT_OFFLINE_DRIVEN"
    ),
    "claim_boundary": "NO_RH_CLAIM experiments_only",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
RESULT: dict = {}


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line, flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-42s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def py(value):
    if isinstance(value, dict):
        return {str(key): py(val) for key, val in value.items()}
    if isinstance(value, (list, tuple)):
        return [py(val) for val in value]
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        number = float(value)
        if not math.isfinite(number):
            return None
        return number
    if isinstance(value, np.ndarray):
        return py(value.tolist())
    return value


def rec(key: str, value):
    RESULT[key] = py(value)
    if isinstance(value, str):
        emit("%s %s" % (key, value))
    else:
        emit("%s %s" % (key, repr(py(value))))
    return value


def np_exp(log_value):
    return np.exp(np.clip(np.asarray(log_value, dtype=np.float64), -700.0, 700.0))


def C_of(alpha: float) -> float:
    return math.sqrt(math.pi / (2.0 * alpha))


def D_of(alpha: float, omega: float) -> float:
    return r608.exp_clip(-(omega * omega) / (2.0 * alpha))


def cutoff_n(alpha: float, n_cap: int) -> tuple[int, float]:
    x_val = r608.required_X(alpha, TAIL_TARGET)
    n_used = int(min(max(2, math.ceil(math.exp(min(x_val, 40.0)))), n_cap))
    if x_val <= 40.0:
        n_used = int(min(max(2, math.ceil(math.exp(x_val))), n_cap))
    else:
        n_used = int(n_cap)
    return n_used, float(x_val)


def node_w(alpha: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray) -> np.ndarray:
    return lam_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)


def prime_closed(
    alpha: float, omega: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    dc = D_of(alpha, omega)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    return float(pref * np.dot(weights, np.cos(omega * u_arr) + dc))


def d_omega_prime(
    alpha: float, omega: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    dc = D_of(alpha, omega)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    bracket = -u_arr * np.sin(omega * u_arr) - (omega / alpha) * dc
    return float(pref * np.dot(weights, bracket))


def d2_omega_prime(
    alpha: float, omega: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    dc = D_of(alpha, omega)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    bracket = -u_arr * u_arr * np.cos(omega * u_arr) + (
        (omega * omega) / (alpha * alpha) - 1.0 / alpha
    ) * dc
    return float(pref * np.dot(weights, bracket))


def d_a_prime(
    alpha: float, omega: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    dc = D_of(alpha, omega)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    u2 = u_arr * u_arr
    cos_b = -(0.5 * u2 + 0.5 / alpha) * np.cos(omega * u_arr)
    dc_b = (-0.5 * u2 - 0.5 / alpha + (omega * omega) / (2.0 * alpha * alpha)) * dc
    return float(pref * np.dot(weights, cos_b + dc_b))


def heat_split(
    alpha: float, omega: float, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> tuple[float, float, float, float]:
    pref = C_of(alpha)
    dc = D_of(alpha, omega)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    u2 = u_arr * u_arr
    cosu = np.cos(omega * u_arr)
    p_cos = float(pref * np.dot(weights, cosu))
    p_dc = float(pref * np.dot(weights, np.full_like(weights, dc)))
    da_cos = float(pref * np.dot(weights, -(0.5 * u2 + 0.5 / alpha) * cosu))
    da_dc = float(
        pref * np.dot(
            weights,
            (-0.5 * u2 - 0.5 / alpha + (omega * omega) / (2.0 * alpha * alpha)) * dc,
        )
    )
    d2_cos = float(pref * np.dot(weights, -u2 * cosu))
    d2_dc = float(
        pref * np.dot(
            weights, ((omega * omega) / (alpha * alpha) - 1.0 / alpha) * dc * np.ones_like(weights)
        )
    )
    res_cos = da_cos - 0.5 * d2_cos + p_cos / (2.0 * alpha)
    res_dc = da_dc - 0.5 * d2_dc + p_dc / (2.0 * alpha)
    den_cos = abs(p_cos) + abs(da_cos) + abs(d2_cos) + 1.0e-300
    return res_cos, abs(res_cos) / den_cos, res_dc, p_dc


def selberg_d_omega(
    alpha: float, omega: float, n_arr: np.ndarray, conv_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    wgt = conv_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)
    return float(pref * np.dot(wgt, np.sin(omega * u_arr)))


def lam2_d_omega(
    alpha: float, omega: float, n_arr: np.ndarray, lam2_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    wgt = lam2_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)
    return float(-pref * np.dot(wgt, np.sin(omega * u_arr)))


def selberg_d2_omega(
    alpha: float, omega: float, n_arr: np.ndarray, conv_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    wgt = conv_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)
    return float(pref * np.dot(wgt, u_arr * np.cos(omega * u_arr)))


def lam2_d2_omega(
    alpha: float, omega: float, n_arr: np.ndarray, lam2_arr: np.ndarray, u_arr: np.ndarray,
) -> float:
    pref = C_of(alpha)
    wgt = lam2_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)
    return float(-pref * np.dot(wgt, u_arr * np.cos(omega * u_arr)))


def rel_err(closed: float, fd_val: float) -> float:
    return abs(closed - fd_val) / (abs(closed) + abs(fd_val) + 1.0e-300)


def primes_from_lam(lam: np.ndarray) -> np.ndarray:
    n_max = int(lam.size - 1)
    ns = np.arange(n_max + 1, dtype=np.float64)
    with np.errstate(over="ignore"):
        p_est = np.rint(np_exp(lam))
    mask = (lam > 0.0) & (p_est == ns)
    mask[0] = False
    mask[1] = False
    return np.flatnonzero(mask).astype(np.int64)


def fill_prime_power_selberg(
    lam: np.ndarray, primes: np.ndarray, n_max: int,
) -> tuple[np.ndarray, np.ndarray]:
    lam2 = np.zeros(n_max + 1, dtype=np.float64)
    conv = np.zeros(n_max + 1, dtype=np.float64)
    for p in primes.tolist():
        p_int = int(p)
        logp = float(lam[p_int])
        logp2 = logp * logp
        pk = p_int
        k = 1
        while pk <= n_max:
            lam2[pk] = (2 * k - 1) * logp2
            conv[pk] = (k - 1) * logp2
            if pk > n_max // p_int:
                break
            pk *= p_int
            k += 1
    return lam2, conv


def dirichlet_square(f_arr: np.ndarray, primes: np.ndarray, n_max: int) -> np.ndarray:
    out = np.zeros(n_max + 1, dtype=np.float64)
    for p in primes.tolist():
        p_int = int(p)
        vals = []
        pk = p_int
        while pk <= n_max:
            vals.append(float(f_arr[pk]))
            if pk > n_max // p_int:
                break
            pk *= p_int
        n_pk = p_int * p_int
        for k in range(2, len(vals) + 1):
            acc = 0.0
            for idx in range(1, k):
                acc += vals[idx - 1] * vals[k - idx - 1]
            out[n_pk] = acc
            if k == len(vals):
                break
            n_pk *= p_int
    n_p = int(primes.size)
    for i in range(n_p):
        p_int = int(primes[i])
        pa = p_int
        while pa <= n_max:
            f_a = float(f_arr[pa])
            if f_a != 0.0:
                limit = n_max // pa
                j = i + 1
                while j < n_p:
                    q_int = int(primes[j])
                    if q_int > limit:
                        break
                    qb = q_int
                    while qb <= limit:
                        out[pa * qb] = 2.0 * f_a * float(f_arr[qb])
                        if qb > limit // q_int:
                            break
                        qb *= q_int
                    j += 1
            if pa > n_max // p_int:
                break
            pa *= p_int
    return out


def fill_two_prime_structural(
    lam2: np.ndarray, conv: np.ndarray, lam: np.ndarray, primes: np.ndarray, n_max: int,
) -> None:
    n_p = int(primes.size)
    for i in range(n_p):
        p_int = int(primes[i])
        pa = p_int
        while pa <= n_max:
            f_a = float(lam[pa])
            if f_a != 0.0:
                limit = n_max // pa
                j = i + 1
                while j < n_p:
                    q_int = int(primes[j])
                    if q_int > limit:
                        break
                    qb = q_int
                    while qb <= limit:
                        val = 2.0 * f_a * float(lam[qb])
                        n_val = pa * qb
                        conv[n_val] = val
                        lam2[n_val] = val
                        if qb > limit // q_int:
                            break
                        qb *= q_int
                    j += 1
            if pa > n_max // p_int:
                break
            pa *= p_int


def conv_direct_divisor(lam: np.ndarray, n_max: int) -> np.ndarray:
    out = np.zeros(n_max + 1, dtype=np.float64)
    idx = np.flatnonzero(lam[: n_max + 1])
    idx = idx[idx >= 2]
    for d in idx.tolist():
        d_int = int(d)
        maxm = n_max // d_int
        ms = idx[idx <= maxm]
        out[d_int * ms] += lam[d_int] * lam[ms]
    return out


def pack_support(*cols: np.ndarray) -> tuple[np.ndarray, list[np.ndarray]]:
    mask = np.zeros(cols[0].shape, dtype=bool)
    for col in cols:
        mask |= col != 0.0
    mask[0] = False
    idx = np.flatnonzero(mask).astype(np.int64)
    n_arr = idx.astype(np.float64)
    packed = [col[idx] for col in cols]
    return n_arr, packed


def env_tail_of(
    alpha: float, omega: float, u_all: np.ndarray, weight: np.ndarray, n_used: int,
) -> float:
    _prime, _pabs, tail = r608.prime_channels(alpha, omega, u_all, weight, n_used)
    return float(tail)


def slice_le(n_arr: np.ndarray, *cols: np.ndarray, n_used: int):
    mask = n_arr <= float(n_used) + 1.0e-12
    return (n_arr[mask],) + tuple(col[mask] for col in cols)


def psi_eval(t_arr: np.ndarray, alpha: float, omega: float, k_pow: int, phi: str) -> np.ndarray:
    base = np.power(t_arr, k_pow) * np_exp(-0.5 * t_arr) * np_exp(-0.5 * alpha * t_arr * t_arr)
    if phi == "cos":
        return base * np.cos(omega * t_arr)
    if phi == "sin":
        return base * np.sin(omega * t_arr)
    return base


def min_eigenpair(
    mat: np.ndarray, v0: np.ndarray | None = None, k_lan: int = 28,
) -> tuple[float, np.ndarray]:
    n_dim = int(mat.shape[0])
    m_sym = 0.5 * (mat + mat.T)
    if n_dim <= 120 or k_lan >= n_dim - 1:
        evals, evecs = np.linalg.eigh(m_sym)
        return float(evals[0]), np.ascontiguousarray(evecs[:, 0])
    if v0 is None or v0.size != n_dim:
        vec = np.ones(n_dim, dtype=np.float64)
        vec[1::2] = -0.37
    else:
        vec = np.array(v0, dtype=np.float64, copy=True)
    nrm0 = float(np.linalg.norm(vec))
    vec = vec / (nrm0 if nrm0 > 0.0 else 1.0)
    k_use = int(k_lan)
    basis = np.zeros((n_dim, k_use), dtype=np.float64)
    tri = np.zeros((k_use, k_use), dtype=np.float64)
    basis[:, 0] = vec
    w_vec = m_sym @ vec
    alpha = float(vec @ w_vec)
    tri[0, 0] = alpha
    w_vec = w_vec - alpha * vec
    used = 1
    for j in range(1, k_use):
        beta = float(np.linalg.norm(w_vec))
        if beta < 1.0e-14:
            break
        basis[:, j] = w_vec / beta
        tri[j - 1, j] = beta
        tri[j, j - 1] = beta
        w_vec = m_sym @ basis[:, j] - beta * basis[:, j - 1]
        proj = basis[:, : j + 1].T @ w_vec
        w_vec = w_vec - basis[:, : j + 1] @ proj
        proj = basis[:, : j + 1].T @ w_vec
        w_vec = w_vec - basis[:, : j + 1] @ proj
        alpha = float(basis[:, j] @ w_vec)
        tri[j, j] = alpha
        w_vec = w_vec - alpha * basis[:, j]
        used = j + 1
    t_use = tri[:used, :used]
    v_use = basis[:, :used]
    t_evals, t_evecs = np.linalg.eigh(t_use)
    ritz = v_use @ t_evecs[:, 0]
    ritz = ritz / (float(np.linalg.norm(ritz)) + 1.0e-300)
    lam = float(ritz @ (m_sym @ ritz))
    return lam, ritz


def exact_lambda_min(mat: np.ndarray) -> float:
    evals = np.linalg.eigvalsh(0.5 * (mat + mat.T))
    return float(evals[0])


def combine(c_vec: np.ndarray, stack: np.ndarray) -> np.ndarray:
    return np.tensordot(c_vec, stack, axes=(0, 0))


def projected_ascent(
    stack: np.ndarray, rng: np.random.Generator, n_starts: int, n_iter: int,
) -> tuple[float, np.ndarray]:
    n_psi = int(stack.shape[0])
    starts = [np.eye(n_psi, dtype=np.float64)[i] for i in range(n_psi)]
    gauss = rng.normal(size=(n_starts, n_psi))
    for row in gauss:
        nrm = float(np.linalg.norm(row))
        if nrm > 0.0:
            starts.append(row / nrm)
    best_lam = -1.0e300
    best_c = starts[0].copy()
    for c_init in starts:
        c_vec = np.array(c_init, dtype=np.float64, copy=True)
        mat = combine(c_vec, stack)
        lam, vec = min_eigenpair(mat)
        stalled = False
        for _it in range(n_iter):
            if stalled:
                break
            grad = np.einsum("i,aij,j->a", vec, stack, vec)
            step = 0.1
            accepted = False
            for _bt in range(20):
                c_try = c_vec + step * grad
                nrm = float(np.linalg.norm(c_try))
                if nrm < 1.0e-18:
                    step *= 0.5
                    continue
                c_try = c_try / nrm
                mat_try = combine(c_try, stack)
                lam_try, vec_try = min_eigenpair(mat_try, vec)
                if lam_try + 1.0e-16 >= lam:
                    c_vec, lam, vec = c_try, lam_try, vec_try
                    accepted = True
                    break
                step *= 0.5
            if not accepted:
                stalled = True
        lam_exact = exact_lambda_min(combine(c_vec, stack))
        if lam_exact > best_lam:
            best_lam = lam_exact
            best_c = c_vec.copy()
    return float(best_lam), best_c


def golden_min(func, lo: float, hi: float, n_iter: int) -> tuple[float, float]:
    inv = 1.0 / PHI_GOLDEN
    x1 = hi - (hi - lo) * inv
    x2 = lo + (hi - lo) * inv
    f1 = float(func(x1))
    f2 = float(func(x2))
    for _ in range(n_iter):
        if f1 < f2:
            hi = x2
            x2 = x1
            f2 = f1
            x1 = hi - (hi - lo) * inv
            f1 = float(func(x1))
        else:
            lo = x1
            x1 = x2
            f1 = f2
            x2 = lo + (hi - lo) * inv
            f2 = float(func(x2))
    mid = 0.5 * (lo + hi)
    return float(mid), float(func(mid))


def sign_changes(values: np.ndarray) -> int:
    signs = np.sign(values)
    return int(np.sum(signs[1:] * signs[:-1] < 0.0))


def re_hat_delta_vec(sigma: float, t_val: float, alpha: float, omegas: np.ndarray) -> np.ndarray:
    pref = math.pi / (4.0 * alpha)
    a2 = 2.0 * alpha
    omg = np.asarray(omegas, dtype=np.float64)
    return pref * (
        np_exp((sigma * sigma - (t_val + omg) ** 2) / a2) * np.cos(sigma * (t_val + omg) / alpha)
        + np_exp((sigma * sigma - (t_val - omg) ** 2) / a2) * np.cos(sigma * (t_val - omg) / alpha)
        + 2.0 * np_exp((sigma * sigma - t_val * t_val - omg * omg) / a2) * np.cos(sigma * t_val / alpha)
    )


def z_online_cos_vec(alpha: float, omegas: np.ndarray, gammas: np.ndarray) -> np.ndarray:
    pref = math.pi / (4.0 * alpha)
    two_a = 2.0 * alpha
    g_arr = np.asarray(gammas, dtype=np.float64)
    w_arr = np.asarray(omegas, dtype=np.float64)
    acc = np.zeros(w_arr.size, dtype=np.float64)
    block = 256
    for i0 in range(0, g_arr.size, block):
        gg = g_arr[i0:i0 + block]
        gp = gg[None, :] + w_arr[:, None]
        gm = gg[None, :] - w_arr[:, None]
        g2 = (gg * gg)[None, :]
        w2 = (w_arr * w_arr)[:, None]
        acc += np_exp(-(gp * gp) / two_a).sum(axis=1)
        acc += np_exp(-(gm * gm) / two_a).sum(axis=1)
        acc += 2.0 * np_exp(-(g2 + w2) / two_a).sum(axis=1)
    return 2.0 * pref * acc


def z_offline_cos_vec(alpha: float, omegas: np.ndarray, sigma: float, gamma0: float) -> np.ndarray:
    acc = np.zeros(np.asarray(omegas).size, dtype=np.float64)
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        acc = acc + mlt * re_hat_delta_vec(sig, t_val, alpha, omegas)
    return acc


def lobe_term_vec(sigma: float, t_val: float, alpha: float, omegas: np.ndarray) -> np.ndarray:
    pref = math.pi / (4.0 * alpha)
    dt = t_val - np.asarray(omegas, dtype=np.float64)
    return pref * np_exp((sigma * sigma - dt * dt) / (2.0 * alpha)) * np.cos(sigma * dt / alpha)


def z_online_lobe_vec(alpha: float, omegas: np.ndarray, gammas: np.ndarray) -> np.ndarray:
    pref = math.pi / (4.0 * alpha)
    two_a = 2.0 * alpha
    g_arr = np.asarray(gammas, dtype=np.float64)
    w_arr = np.asarray(omegas, dtype=np.float64)
    acc = np.zeros(w_arr.size, dtype=np.float64)
    block = 256
    for i0 in range(0, g_arr.size, block):
        gg = g_arr[i0:i0 + block]
        gp = gg[None, :] + w_arr[:, None]
        gm = gg[None, :] - w_arr[:, None]
        acc += np_exp(-(gm * gm) / two_a).sum(axis=1)
        acc += np_exp(-(gp * gp) / two_a).sum(axis=1)
    return pref * acc


def z_offline_lobe_vec(alpha: float, omegas: np.ndarray, sigma: float, gamma0: float) -> np.ndarray:
    acc = np.zeros(np.asarray(omegas).size, dtype=np.float64)
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        acc = acc + mlt * lobe_term_vec(sig, t_val, alpha, omegas)
    return acc


def z_cos_scalar(alpha: float, omega: float, gammas: tuple[float, ...], sigma: float, gamma0: float) -> float:
    z_on = r608.zero_sum_online(alpha, omega, gammas)
    z_off = 0.0
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        z_off += mlt * r608.re_hat_delta(sig, t_val, alpha, omega)
    return float(z_on + z_off)


def z_lobe_scalar(alpha: float, omega: float, gammas: tuple[float, ...], sigma: float, gamma0: float) -> float:
    acc = 0.0
    pref = math.pi / (4.0 * alpha)
    for height in gammas:
        for t_val in (float(height), -float(height)):
            dt = t_val - omega
            acc += pref * r608.exp_clip(-(dt * dt) / (2.0 * alpha))
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        dt = t_val - omega
        acc += mlt * pref * r608.exp_clip(
            (sig * sig - dt * dt) / (2.0 * alpha)
        ) * math.cos(sig * dt / alpha)
    return float(acc)


def z_cos_mp(alpha: float, omega: float, gammas: tuple[float, ...], sigma: float, gamma0: float) -> float:
    mp.mp.dps = 30
    a_mp = mp.mpf(alpha)
    w_mp = mp.mpf(omega)
    f_mp = mp.mpf(0)
    acc = mp.mpc(0)
    for height in gammas:
        for sig, t_val, mlt in r608.r605.expand_partners(0.0, float(height), 1):
            acc += mlt * r608.hat_delta_scaled_mp(
                a_mp, w_mp, mp.mpf(sig), mp.mpf(t_val), f_mp,
            )
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        acc += mlt * r608.hat_delta_scaled_mp(
            a_mp, w_mp, mp.mpf(sig), mp.mpf(t_val), f_mp,
        )
    return float(mp.re(acc))


def window_min(
    z_vec_fn, z_scalar_fn, alpha: float, gamma0: float, n_grid: int, n_gold: int,
) -> tuple[float, float]:
    lo = gamma0 - OMEGA_HALFWIDTH
    hi = gamma0 + OMEGA_HALFWIDTH
    grid = np.linspace(lo, hi, n_grid, dtype=np.float64)
    vals = z_vec_fn(alpha, grid)
    order = np.argpartition(vals, min(3, vals.size - 1))[:3]
    best_i = int(np.argmin(vals))
    best_w = float(grid[best_i])
    best_z = float(vals[best_i])
    dw = float(grid[1] - grid[0]) if grid.size > 1 else 0.0
    for idx in order:
        i_val = int(idx)
        w_lo = float(grid[max(i_val - 1, 0)])
        w_hi = float(grid[min(i_val + 1, grid.size - 1)])
        if w_hi <= w_lo:
            w_lo = best_w - dw
            w_hi = best_w + dw
        mid, z_mid = golden_min(lambda w, fn=z_scalar_fn, a=alpha: fn(a, float(w)), w_lo, w_hi, n_gold)
        if z_mid < best_z:
            best_z = z_mid
            best_w = mid
    return best_w, best_z


def lobe_derivs(sigma: float, t_val: float, alpha: float, omega: float) -> tuple[float, float, float, float]:
    """L, ∂_ωL, ∂²_ωL, ∂_aL for Re[(π/(4a)) exp((σ+i(t−ω))²/(2a))]."""
    pref = math.pi / (4.0 * alpha)
    x_val = t_val - omega
    energy = r608.exp_clip((sigma * sigma - x_val * x_val) / (2.0 * alpha))
    cosu = math.cos(sigma * x_val / alpha)
    sinu = math.sin(sigma * x_val / alpha)
    val = pref * energy * cosu
    d1 = pref * (energy / alpha) * (x_val * cosu + sigma * sinu)
    d2 = pref * (energy / alpha) * (
        (x_val * x_val / alpha - 1.0 - sigma * sigma / alpha) * cosu
        + (2.0 * sigma * x_val / alpha) * sinu
    )
    d_a = (
        (-pref / alpha) * energy * cosu
        + pref * energy * (-(sigma * sigma - x_val * x_val) / (2.0 * alpha * alpha)) * cosu
        + pref * energy * sinu * (sigma * x_val / (alpha * alpha))
    )
    return val, d1, d2, d_a


def z_lobe_derivs(
    alpha: float, omega: float, gammas: tuple[float, ...], sigma: float, gamma0: float,
) -> tuple[float, float, float, float]:
    acc = [0.0, 0.0, 0.0, 0.0]
    for height in gammas:
        for t_val in (float(height), -float(height)):
            parts = lobe_derivs(0.0, t_val, alpha, omega)
            for i in range(4):
                acc[i] += parts[i]
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        parts = lobe_derivs(sig, t_val, alpha, omega)
        for i in range(4):
            acc[i] += mlt * parts[i]
    return acc[0], acc[1], acc[2], acc[3]


def cross_derivs(sigma: float, t_val: float, alpha: float, omega: float) -> tuple[float, float, float, float]:
    """L, ∂_ω, ∂²_ω, ∂_a of 2·Re[(π/(4a)) exp((σ²−t²−ω²)/(2a)+i σ t/a)]."""
    pref = math.pi / (4.0 * alpha)
    energy = r608.exp_clip((sigma * sigma - t_val * t_val - omega * omega) / (2.0 * alpha))
    cosu = math.cos(sigma * t_val / alpha)
    sinu = math.sin(sigma * t_val / alpha)
    two = 2.0 * pref
    val = two * energy * cosu
    d1 = two * energy * (-omega / alpha) * cosu
    d2 = two * ((omega * omega) / (alpha * alpha) - 1.0 / alpha) * energy * cosu
    d_a = two * (
        (-1.0 / alpha) * energy * cosu
        + energy * (-(sigma * sigma - t_val * t_val - omega * omega) / (2.0 * alpha * alpha)) * cosu
        + energy * sinu * (sigma * t_val / (alpha * alpha))
    )
    return val, d1, d2, d_a


def re_hat_derivs(sigma: float, t_val: float, alpha: float, omega: float) -> tuple[float, float, float, float]:
    minus = lobe_derivs(sigma, t_val, alpha, omega)
    plus = lobe_derivs(sigma, t_val, alpha, -omega)
    cross = cross_derivs(sigma, t_val, alpha, omega)
    return (
        minus[0] + plus[0] + cross[0],
        minus[1] - plus[1] + cross[1],
        minus[2] + plus[2] + cross[2],
        minus[3] + plus[3] + cross[3],
    )


def z_cos_derivs(
    alpha: float, omega: float, gammas: tuple[float, ...], sigma: float, gamma0: float,
) -> tuple[float, float, float, float]:
    acc = [0.0, 0.0, 0.0, 0.0]
    for height in gammas:
        for sig, t_val, mlt in r608.r605.expand_partners(0.0, float(height), 1):
            parts = re_hat_derivs(sig, t_val, alpha, omega)
            for i in range(4):
                acc[i] += mlt * parts[i]
    for sig, t_val, mlt in r608.r605.expand_partners(sigma, gamma0, 1):
        parts = re_hat_derivs(sig, t_val, alpha, omega)
        for i in range(4):
            acc[i] += mlt * parts[i]
    return acc[0], acc[1], acc[2], acc[3]


def r_heat_of(z0: float, d2: float, da: float, alpha: float) -> float:
    return abs(da - 0.5 * d2 + z0 / (2.0 * alpha)) / (abs(d2) + 1.0e-300)


def fd_zw(z_fn, alpha: float, omega: float) -> tuple[float, float, float, float]:
    h_w = FD_REL * math.sqrt(max(alpha, 1.0e-18))
    h_a = FD_REL * alpha
    z0 = float(z_fn(alpha, omega))
    zp = float(z_fn(alpha, omega + h_w))
    zm = float(z_fn(alpha, omega - h_w))
    d1 = (zp - zm) / (2.0 * h_w)
    d2 = (zp - 2.0 * z0 + zm) / (h_w * h_w)
    da = (float(z_fn(alpha + h_a, omega)) - float(z_fn(alpha - h_a, omega))) / (2.0 * h_a)
    return z0, d1, d2, da


def prime_on_grid(
    alpha: float, omegas: np.ndarray, n_arr: np.ndarray, lam_arr: np.ndarray, u_arr: np.ndarray,
) -> np.ndarray:
    pref = C_of(alpha)
    weights = node_w(alpha, n_arr, lam_arr, u_arr)
    wsum = float(weights.sum())
    acc = np.zeros(omegas.size, dtype=np.float64)
    block_w = max(1, min(48, int(4_000_000 / max(int(u_arr.size), 1))))
    for i0 in range(0, omegas.size, block_w):
        ow = omegas[i0:i0 + block_w]
        acc[i0:i0 + block_w] = np.cos(ow[:, None] * u_arr[None, :]) @ weights
    dc = np_exp(-(omegas * omegas) / (2.0 * alpha))
    return pref * (acc + dc * wsum)


def selberg_d2_on_grid(
    alpha: float, omegas: np.ndarray, n_arr: np.ndarray, conv_arr: np.ndarray, u_arr: np.ndarray,
) -> np.ndarray:
    pref = C_of(alpha)
    wgt = conv_arr * np.power(n_arr, -0.5) * np_exp(-0.5 * alpha * u_arr * u_arr)
    acc = np.zeros(omegas.size, dtype=np.float64)
    uu = u_arr
    block_w = max(1, min(48, int(4_000_000 / max(int(uu.size), 1))))
    for i0 in range(0, omegas.size, block_w):
        ow = omegas[i0:i0 + block_w]
        acc[i0:i0 + block_w] = (np.cos(ow[:, None] * uu[None, :]) * uu[None, :]) @ wgt
    return pref * acc


def interior_minima(values: np.ndarray) -> np.ndarray:
    if values.size < 3:
        return np.zeros(0, dtype=np.int64)
    return np.flatnonzero((values[1:-1] < values[:-2]) & (values[1:-1] < values[2:])) + 1


def median_finite(values) -> float:
    arr = np.asarray(list(values), dtype=np.float64)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return float("nan")
    return float(np.median(arr))


def g3_coeff(alpha: float, p_int: int, k_pow: int, logp: float) -> float:
    n_val = p_int ** k_pow
    u_val = k_pow * logp
    return (
        2.0 * logp * math.pow(n_val, -0.5)
        * 0.5 * C_of(alpha)
        * r608.exp_clip(-0.5 * alpha * u_val * u_val)
    )


def dc_lower_of(alpha: float, primes: np.ndarray, n_used: int) -> float:
    total = 0.0
    for p in primes.tolist():
        p_int = int(p)
        if p_int > n_used:
            break
        logp = math.log(p_int)
        b1 = abs(g3_coeff(alpha, p_int, 1, logp))
        rest = 0.0
        pk = p_int * p_int
        k_pow = 2
        while pk <= n_used:
            rest += abs(g3_coeff(alpha, p_int, k_pow, logp))
            if pk > n_used // p_int:
                break
            pk *= p_int
            k_pow += 1
        total += b1 - rest
    return float(total)


def run_t0(pp_n, pp_lam, pp_u, points) -> dict:
    emit("T0 DERIVATIVE ALGEBRA")
    rels = []
    heat_rel_cos = []
    heat_dc = []
    rows = []
    for alpha, omega in points:
        n_used, x_val = cutoff_n(alpha, N_PRIME_CAP)
        n_arr, lam_arr, u_arr = slice_le(pp_n, pp_lam, pp_u, n_used=n_used)
        p0 = prime_closed(alpha, omega, n_arr, lam_arr, u_arr)
        dw = d_omega_prime(alpha, omega, n_arr, lam_arr, u_arr)
        d2 = d2_omega_prime(alpha, omega, n_arr, lam_arr, u_arr)
        da = d_a_prime(alpha, omega, n_arr, lam_arr, u_arr)
        h_w = H_OMEGA_T0
        h_a = 1.0e-5 * alpha
        dw_fd = (
            prime_closed(alpha, omega + h_w, n_arr, lam_arr, u_arr)
            - prime_closed(alpha, omega - h_w, n_arr, lam_arr, u_arr)
        ) / (2.0 * h_w)
        d2_fd = (
            prime_closed(alpha, omega + h_w, n_arr, lam_arr, u_arr)
            - 2.0 * p0
            + prime_closed(alpha, omega - h_w, n_arr, lam_arr, u_arr)
        ) / (h_w * h_w)
        da_fd = (
            prime_closed(alpha + h_a, omega, n_arr, lam_arr, u_arr)
            - prime_closed(alpha - h_a, omega, n_arr, lam_arr, u_arr)
        ) / (2.0 * h_a)
        r_dw = rel_err(dw, dw_fd)
        r_d2 = rel_err(d2, d2_fd)
        r_da = rel_err(da, da_fd)
        res_cos, rel_cos, res_dc, _p_dc = heat_split(alpha, omega, n_arr, lam_arr, u_arr)
        rels.extend([r_dw, r_d2, r_da])
        heat_rel_cos.append(rel_cos)
        heat_dc.append(res_dc)
        row = {
            "a": alpha, "omega": omega, "n_used": n_used, "X": x_val,
            "PRIME": p0, "d_omega": dw, "d2_omega": d2, "d_a": da,
            "d_omega_fd": dw_fd, "d2_omega_fd": d2_fd, "d_a_fd": da_fd,
            "rel_d_omega": r_dw, "rel_d2_omega": r_d2, "rel_d_a": r_da,
            "heat_res_cos": res_cos, "heat_rel_cos": rel_cos, "heat_res_dc": res_dc,
        }
        rows.append(row)
        rec("T0_a_%s_w_%s" % (repr(alpha), repr(omega)), row)
    max_rel = max(rels) if rels else float("inf")
    max_heat = max(heat_rel_cos) if heat_rel_cos else float("inf")
    rec("T0_max_fd_rel", max_rel)
    rec("T0_max_cos_heat_rel", max_heat)
    rec("T0_dc_heat_sizes", heat_dc)
    check("T0_FD_MATCH", max_rel <= 1.0e-6, "max_rel=%s" % repr(max_rel))
    check("T0_COS_HEAT_EXACT", max_heat <= 1.0e-12, "max_rel=%s" % repr(max_heat))
    return {"rows": rows, "max_rel": max_rel, "max_heat": max_heat}


def run_t1(
    lam_dense, lam2, conv, pp_n, pp_lam, pp_u, sel_n, sel_conv, sel_lam2, sel_u,
    u_all, weight, n_selberg, a_list, omega_list, omega_lo, omega_hi, omega_step,
    max_conv_diff: float, check_lo: float, check_hi: float, check_step: float,
) -> dict:
    emit("T1 SELBERG REWRITE")
    n_id = int(n_selberg)
    logn = np.zeros(n_id + 1, dtype=np.float64)
    if n_id >= 2:
        logn[2:] = np.log(np.arange(2, n_id + 1, dtype=np.float64))
    ident = np.abs(
        lam_dense[: n_id + 1] * logn + conv[: n_id + 1] - lam2[: n_id + 1]
    )
    max_ident = float(ident.max()) if ident.size else 0.0
    max_lam2 = float(np.max(np.abs(lam2[: n_id + 1]))) if n_id >= 0 else 1.0
    rec("T1_max_identity", max_ident)
    rec("T1_max_lam2", max_lam2)
    rec("T1_max_conv_diff", max_conv_diff)
    ident_ok = (
        max_ident <= 1.0e-9 * max(max_lam2, 1.0e-300)
        and max_conv_diff <= 1.0e-9 * max(max_lam2, 1.0e-300)
    )
    check(
        "T1_SELBERG_IDENTITY",
        ident_ok,
        "max=%s convdiff=%s bound=%s"
        % (repr(max_ident), repr(max_conv_diff), repr(1.0e-9 * max_lam2)),
    )
    rows = []
    for alpha in a_list:
        n_used, x_val = cutoff_n(alpha, N_PRIME_CAP)
        n_pp, lam_pp, u_pp = slice_le(pp_n, pp_lam, pp_u, n_used=n_used)
        n_se, c_se, l2_se, u_se = slice_le(sel_n, sel_conv, sel_lam2, sel_u, n_used=n_used)
        for omega in omega_list:
            d2 = d2_omega_prime(alpha, omega, n_pp, lam_pp, u_pp)
            d2_s = selberg_d2_omega(alpha, omega, n_se, c_se, u_se)
            d2_l = lam2_d2_omega(alpha, omega, n_se, l2_se, u_se)
            d1 = d_omega_prime(alpha, omega, n_pp, lam_pp, u_pp)
            d1_s = selberg_d_omega(alpha, omega, n_se, c_se, u_se)
            d1_l = lam2_d_omega(alpha, omega, n_se, l2_se, u_se)
            f2 = abs(d2_s) / (abs(d2) + 1.0e-300)
            f1 = abs(d1_s) / (abs(d1) + 1.0e-300)
            tail = env_tail_of(alpha, omega, u_all, weight, n_used)
            row = {
                "a": alpha, "omega": omega, "n_used": n_used, "X": x_val,
                "env_tail": tail, "d2": d2, "d2_lam2": d2_l, "d2_selberg": d2_s,
                "f2": f2, "d1": d1, "d1_lam2": d1_l, "d1_selberg": d1_s, "f1": f1,
            }
            rows.append(row)
            rec("T1_cell_a_%s_w_%s" % (repr(alpha), repr(omega)), row)
    sign_rows = {}
    check_rows = {}
    all_ok = True
    for alpha in a_list:
        n_used, _x = cutoff_n(alpha, N_PRIME_CAP)
        n_se, c_se, u_se = slice_le(sel_n, sel_conv, sel_u, n_used=n_used)
        grid = np.arange(omega_lo, omega_hi + 0.5 * omega_step, omega_step, dtype=np.float64)
        vals = selberg_d2_on_grid(alpha, grid, n_se, c_se, u_se)
        n_ch = sign_changes(vals)
        sign_rows[repr(alpha)] = n_ch
        rec("T1_sign_changes_a_%s" % repr(alpha), n_ch)
        if abs(check_lo - omega_lo) > 1.0e-15 or abs(check_hi - omega_hi) > 1.0e-15 or abs(check_step - omega_step) > 1.0e-15:
            grid_c = np.arange(check_lo, check_hi + 0.5 * check_step, check_step, dtype=np.float64)
            n_chk = sign_changes(selberg_d2_on_grid(alpha, grid_c, n_se, c_se, u_se))
        else:
            n_chk = n_ch
        check_rows[repr(alpha)] = n_chk
        rec("T1_sign_changes_check_a_%s" % repr(alpha), n_chk)
        if n_chk < 10:
            all_ok = False
    rec("T1_sign_changes", sign_rows)
    rec("T1_sign_changes_check", check_rows)
    check("T1_SIGN_INDEFINITE", all_ok, "n=%s" % repr(check_rows))
    return {"rows": rows, "sign_changes": sign_rows, "max_identity": max_ident}


def run_t2(pp_n, a_list, omega_list, n_hankel, n_starts, n_iter, rng) -> dict:
    emit("T2 HANKEL GATE")
    mask = (pp_n >= 2.0) & (pp_n <= float(n_hankel) + 1.0e-12)
    u_nodes = np.log(pp_n[mask])
    rec("T2_n_nodes", int(u_nodes.size))
    rec("T2_n_hankel", int(n_hankel))
    cells = []
    all_finite = True
    best_global = -1.0e300
    best_meta = {"a": None, "omega": None, "c": None, "lam": None}
    family = [(k, phi) for k in range(K_MAX + 1) for phi in PSI_PHIS]
    rec("T2_family", [(int(k), phi) for k, phi in family])
    for alpha in a_list:
        for omega in omega_list:
            stack = []
            g1 = []
            for k_pow, phi in family:
                s_sum = u_nodes[:, None] + u_nodes[None, :]
                mat = psi_eval(s_sum, alpha, omega, k_pow, phi)
                mat = 0.5 * (mat + mat.T)
                finite = bool(np.isfinite(mat).all())
                symmetric = bool(np.allclose(mat, mat.T, atol=1.0e-12, rtol=0.0))
                all_finite = all_finite and finite and symmetric
                frob = float(np.linalg.norm(mat))
                if frob > 0.0:
                    mat = mat / frob
                evals = np.linalg.eigvalsh(mat)
                lmin = float(evals[0])
                lmax = float(evals[-1])
                g1.append({"k": k_pow, "phi": phi, "lambda_min": lmin, "lambda_max": lmax})
                stack.append(mat)
            stack_a = np.stack(stack, axis=0)
            lam_best, c_best = projected_ascent(stack_a, rng, n_starts, n_iter)
            psi_dc = psi_eval
            t2u = 2.0 * u_nodes
            psi_d = psi_dc(t2u, alpha, omega, 0, "dc")
            psi_s = psi_dc(u_nodes[:, None] + u_nodes[None, :], alpha, omega, 0, "dc")
            lhs = psi_d[:, None] * psi_d[None, :]
            rhs = psi_s * psi_s
            off = ~np.eye(u_nodes.size, dtype=bool)
            n_off = int(np.sum(off))
            n_viol = int(np.sum((lhs < rhs) & off))
            frac = n_viol / max(n_off, 1)
            worst = min(g1, key=lambda row: row["lambda_min"])
            cell = {
                "a": alpha, "omega": omega, "best_lambda_min": lam_best,
                "c": [float(x) for x in c_best],
                "worst_psi_lambda_min": worst["lambda_min"],
                "worst_psi_lambda_max": worst["lambda_max"],
                "worst_psi": {"k": worst["k"], "phi": worst["phi"]},
                "g1": g1,
                "dc_minor_violation_frac": frac,
            }
            cells.append(cell)
            rec(
                "T2_cell_a_%s_w_%s" % (repr(alpha), repr(omega)),
                {
                    "best_lambda_min": lam_best,
                    "worst_psi_lambda_min": worst["lambda_min"],
                    "worst_psi_lambda_max": worst["lambda_max"],
                    "dc_minor_violation_frac": frac,
                },
            )
            if lam_best > best_global:
                best_global = lam_best
                best_meta = {"a": alpha, "omega": omega, "c": [float(x) for x in c_best], "lam": lam_best}
    rec("T2_best_lambda_min", best_global)
    rec("T2_best_meta", best_meta)
    gate_pass = bool(best_global >= -GATE_TOL)
    rec("T2_GATE_PASS", int(gate_pass))
    check("T2_GATE_EVALUATED", all_finite, "n_cells=%d" % len(cells))
    RESULT["T2_cells"] = py(cells)
    return {
        "cells": cells, "best": best_meta, "best_lambda_min": best_global,
        "gate_pass": gate_pass,
    }


def run_g3(pp_n, pp_lam, pp_u, u_all, weight, primes, points, n_arch) -> dict:
    emit("G3 EULER-LOCAL DC COST")
    rows = []
    selected = []
    for alpha, omega in points:
        n_used, x_val = cutoff_n(alpha, N_PRIME_CAP)
        n_pp, lam_pp, u_pp = slice_le(pp_n, pp_lam, pp_u, n_used=n_used)
        pole = r608.pole_closed(alpha, omega)
        arch = r608.arch_trapz(alpha, omega, n_arch)
        budget = pole + arch
        _pr, prime_abs, tail = r608.prime_channels(alpha, omega, u_all, weight, n_used)
        dc_lo = dc_lower_of(alpha, primes[primes <= n_used], n_used)
        ratio = dc_lo / (budget if budget != 0.0 else 1.0e-300)
        m_ratio = prime_abs / (budget if budget != 0.0 else 1.0e-300)
        row = {
            "a": alpha, "omega": omega, "n_used": n_used, "X": x_val,
            "DC_lower": dc_lo, "M": prime_abs, "B": budget, "POLE": pole,
            "ARCH": arch, "DC_lower_over_B": ratio, "M_over_B": m_ratio,
            "env_tail": tail,
        }
        rows.append(row)
        rec("G3_cell_a_%s_w_%s" % (repr(alpha), repr(omega)), row)
        if alpha <= EULER_LOCAL_A_MAX and omega >= EULER_LOCAL_OMEGA_MIN:
            selected.append(ratio)
    if selected:
        min_ratio = float(min(selected))
        token = (
            "EULER_LOCAL_SQUARE_COSTS_TRIVIAL_MAJORANT"
            if min_ratio > 1.0 else "EULER_LOCAL_BUDGET_OK"
        )
    else:
        min_ratio = float("nan")
        token = "EULER_LOCAL_BUDGET_OK"
    rec("G3_min_ratio_selected", min_ratio)
    rec("G3_token", token)
    return {"rows": rows, "token": token, "min_ratio": min_ratio}


def run_t3(gammas, catalogs, n_grid, n_a_scan, n_bisect, n_gold, do_lobe_scan: bool) -> dict:
    emit("T3 FIRST-CONTACT GEOMETRY")
    g_arr = np.asarray(gammas, dtype=np.float64)
    g_tup = tuple(float(x) for x in gammas)
    a_grid = np.exp(np.linspace(math.log(A_SCAN_HI), math.log(A_SCAN_LO), n_a_scan))
    rec("T3_a_grid_n", int(a_grid.size))
    rec("T3_n_omega_grid", int(n_grid))
    contacts = []
    r_heat_lobe_all = []
    r_heat_cos_all = []
    found_ok = True
    cond_ok = True
    offline_ok = True
    heat_lobe_ok = True
    heat_cos_ok = True
    down_ok = True
    offline_ratios = []
    main_mins = []
    a_stars = []

    def scan_variant(kind: str, sigma: float, gamma0: float):
        if kind == "cos":
            z_vec_on = lambda a, w: z_online_cos_vec(a, w, g_arr)
            z_vec = lambda a, w: z_online_cos_vec(a, w, g_arr) + z_offline_cos_vec(a, w, sigma, gamma0)
            z_sc = lambda a, w: z_cos_scalar(a, w, g_tup, sigma, gamma0)
        else:
            z_vec_on = lambda a, w: z_online_lobe_vec(a, w, g_arr)
            z_vec = lambda a, w: z_online_lobe_vec(a, w, g_arr) + z_offline_lobe_vec(a, w, sigma, gamma0)
            z_sc = lambda a, w: z_lobe_scalar(a, w, g_tup, sigma, gamma0)

        def m_of(alpha: float):
            _w, z_min = window_min(z_vec, z_sc, alpha, gamma0, n_grid, n_gold)
            return _w, z_min

        ms = []
        for a_val in a_grid:
            w_m, z_m = m_of(float(a_val))
            ms.append((float(a_val), w_m, z_m))
        neg = [i for i, row in enumerate(ms) if row[2] < 0.0]
        if not neg or neg[0] == 0:
            return {
                "found": False, "a_star": float("nan"), "omega_star": float("nan"),
                "ms": ms, "kind": kind, "sigma": sigma, "gamma0": gamma0,
            }
        i_neg = neg[0]
        a_pos, _wp, _zp = ms[i_neg - 1]
        a_neg, w_neg, z_neg = ms[i_neg]
        w_star = w_neg
        for _ in range(n_bisect):
            mid = math.exp(0.5 * (math.log(a_pos) + math.log(a_neg)))
            w_m, z_m = m_of(mid)
            if z_m < 0.0:
                a_neg, w_star, z_neg = mid, w_m, z_m
            else:
                a_pos = mid
        # a* := a_pos (last m≥0); ω* := argmin on the negative side.
        w_star, z_neg = m_of(a_neg)
        a_star = a_pos
        z0, d1, d2, da = fd_zw(z_sc, a_star, w_star)
        r_heat_fd = r_heat_of(z0, d2, da, a_star)
        if kind == "lobe":
            _za, _d1a, d2a, daa = z_lobe_derivs(a_star, w_star, g_tup, sigma, gamma0)
            r_heat = r_heat_of(_za, d2a, daa, a_star)
        else:
            _za, _d1a, d2a, daa = z_cos_derivs(a_star, w_star, g_tup, sigma, gamma0)
            r_heat = r_heat_of(_za, d2a, daa, a_star)
        z_on = float(z_vec_on(a_star, np.array([w_star]))[0])
        z_off = z0 - z_on
        grid = np.linspace(gamma0 - OMEGA_HALFWIDTH, gamma0 + OMEGA_HALFWIDTH, n_grid)
        z_on_grid = z_vec_on(a_star, grid)
        background_local = abs(z_on) + 1.0e-300
        background = max(float(np.max(np.abs(z_on_grid))), abs(z_on), abs(z_off), 1.0e-300)
        predicted_offset = math.pi * a_star / (2.0 * sigma)
        measured_offset = w_star - gamma0
        offline_online_ratio = abs(z_off) / (abs(z_on) + 1.0e-300)
        downs = {}
        for fac, name in ((2.0, "half"), (4.0, "quarter"), (8.0, "eighth")):
            _wd, zd = m_of(a_star / fac)
            downs[name] = zd
        main_min = float(np.min(z_on_grid))
        return {
            "found": True, "kind": kind, "sigma": sigma, "gamma0": gamma0,
            "a_star": a_star, "omega_star": w_star, "Z": z0, "d_omega": d1,
            "d2_omega": d2, "d_a": da, "r_heat": r_heat, "z_offline": z_off,
            "z_online": z_on, "background": background, "background_local": background_local,
            "downset": downs,
            "main_min": main_min, "m_scan": [(r[0], r[2]) for r in ms[:: max(1, len(ms) // 8)]],
            "r_heat_fd": r_heat_fd,
            "a_neg": a_neg, "a_pos": a_pos,
            "omega_minus_gamma0": measured_offset,
            "predicted_offset": predicted_offset,
            "offline_online_ratio": offline_online_ratio,
        }

    mp_target = None
    for sigma, gamma0 in catalogs:
        variants = ["cos"]
        if do_lobe_scan:
            variants.append("lobe")
        cos_contact = None
        for kind in variants:
            row = scan_variant(kind, float(sigma), float(gamma0))
            contacts.append(row)
            rec(
                "T3_%s_sig_%s_g0_%s" % (kind, repr(sigma), repr(gamma0)),
                {k: row[k] for k in row if k not in ("m_scan", "ms")},
            )
            if not row["found"]:
                found_ok = False
                continue
            a_star = row["a_star"]
            if not (A_SCAN_LO < a_star < A_SCAN_HI):
                found_ok = False
            bg = row["background"]
            a_s = row["a_star"]
            if abs(row["Z"]) > 1.0e-6 * bg:
                cond_ok = False
            if row["d2_omega"] < -1.0e-6 * bg / a_s:
                cond_ok = False
            if row["d_a"] < -1.0e-6 * bg / a_s:
                cond_ok = False
            ratio = row["offline_online_ratio"]
            offline_ratios.append(ratio)
            if ratio < 0.5:
                offline_ok = False
            downs = row["downset"]
            if not (downs["half"] < 0.0 and downs["quarter"] < 0.0 and downs["eighth"] < 0.0):
                down_ok = False
            main_mins.append(row["main_min"])
            a_stars.append(a_star)
            if kind == "cos":
                r_heat_cos_all.append(row["r_heat"])
                if row["r_heat"] > HEAT_TOL_COS:
                    heat_cos_ok = False
                cos_contact = row
            else:
                r_heat_lobe_all.append(row["r_heat"])
                if row["r_heat"] > HEAT_TOL_LOBE:
                    heat_lobe_ok = False
        if not do_lobe_scan and cos_contact is not None:
            a_s = cos_contact["a_star"]
            w_s = cos_contact["omega_star"]
            z_fn = lambda a, w, s=sigma, g0=gamma0: z_lobe_scalar(a, w, g_tup, s, g0)
            z0, d1, d2, da = fd_zw(z_fn, a_s, w_s)
            r_heat_fd = r_heat_of(z0, d2, da, a_s)
            _za, _d1a, d2a, daa = z_lobe_derivs(a_s, w_s, g_tup, float(sigma), float(gamma0))
            r_heat = r_heat_of(_za, d2a, daa, a_s)
            r_heat_lobe_all.append(r_heat)
            rec(
                "T3_lobe_at_cos_contact_sig_%s_g0_%s" % (repr(sigma), repr(gamma0)),
                {"Z": z0, "d_omega": d1, "d2_omega": d2, "d_a": da, "r_heat": r_heat, "r_heat_fd": r_heat_fd},
            )
            if r_heat > HEAT_TOL_LOBE:
                heat_lobe_ok = False
        if mp_target is None and cos_contact is not None:
            mp_target = (cos_contact, float(sigma), float(gamma0))

    rec("T3_r_heat_cos", r_heat_cos_all)
    rec("T3_r_heat_lobe", r_heat_lobe_all)
    rec("T3_MAIN_mins", main_mins)
    rec("T3_offline_online_ratios", offline_ratios)
    check("T3_CONTACT_FOUND", found_ok, "n=%d" % len(contacts))
    check("T3_CONTACT_CONDITIONS", cond_ok, "")
    if not offline_ratios:
        offline_ok = False
    check("T3_CONTACT_OFFLINE_DRIVEN", offline_ok, "ratios=%s" % repr(offline_ratios))
    max_lobe = max(r_heat_lobe_all) if r_heat_lobe_all else float("inf")
    max_cos = max(r_heat_cos_all) if r_heat_cos_all else float("inf")
    check("T3_HEAT_REDUNDANCY_LOBE", heat_lobe_ok, "max=%s" % repr(max_lobe))
    check("T3_HEAT_REDUNDANCY_COS", heat_cos_ok, "max=%s" % repr(max_cos))
    check("T3_NEGATIVITY_DOWNSET", down_ok, "")
    main_pos = all(val > 0.0 for val in main_mins) if main_mins else False
    check("T3_MAIN_POSITIVE", main_pos, "mins=%s" % repr(main_mins))
    mp_rel = float("inf")
    if mp_target is not None:
        row, sigma, gamma0 = mp_target
        z_mp = z_cos_mp(row["a_star"], row["omega_star"], g_tup, sigma, gamma0)
        z_np = z_cos_scalar(row["a_star"], row["omega_star"], g_tup, sigma, gamma0)
        den = abs(row.get("z_online", 0.0)) + abs(row.get("z_offline", 0.0)) + 1.0e-300
        mp_rel = abs(z_mp - z_np) / den
        rec("T3_mp_Z", z_mp)
        rec("T3_np_Z", z_np)
        rec("T3_mp_rel", mp_rel)
        rec("T3_mp_rel_vs_cancelled_Z", abs(z_mp - z_np) / (abs(z_np) + abs(z_mp) + 1.0e-300))
    check("T3_MP_AGREE", mp_rel <= 1.0e-9, "rel=%s" % repr(mp_rel))
    return {
        "contacts": contacts, "r_heat_lobe": r_heat_lobe_all, "r_heat_cos": r_heat_cos_all,
        "main_mins": main_mins, "mp_rel": mp_rel,
    }


def analyze_world(
    name: str, alpha: float, omegas: np.ndarray, g_grid: np.ndarray, n_arch: int,
    n_pp, lam_pp, u_pp, n_se, c_se, l2_se, u_se, n_gold: int,
) -> dict:
    mins_idx = interior_minima(g_grid)
    rec("%s_a_%s_n_grid_neg" % (name, repr(alpha)), int(np.sum(g_grid < 0.0)))
    rec("%s_a_%s_minG" % (name, repr(alpha)), float(np.min(g_grid)))
    rec("%s_a_%s_maxG" % (name, repr(alpha)), float(np.max(g_grid)))
    med_g = float(np.median(g_grid))
    helpful = []
    f2s = []
    r1s = []
    neg_min = 0
    depths = []
    dw = float(omegas[1] - omegas[0]) if omegas.size > 1 else OMEGA_T4_STEP

    def g_call(omega: float) -> float:
        pole = r608.pole_closed(alpha, omega)
        arch = r608.arch_trapz(alpha, omega, n_arch)
        prime = prime_closed(alpha, omega, n_pp, lam_pp, u_pp)
        return pole + arch - prime

    omega_mins = []
    for idx in mins_idx.tolist():
        lo = float(omegas[max(idx - 1, 0)])
        hi = float(omegas[min(idx + 1, omegas.size - 1)])
        if hi <= lo:
            lo = float(omegas[idx]) - dw
            hi = float(omegas[idx]) + dw
        w_min, g_min = golden_min(g_call, lo, hi, n_gold)
        omega_mins.append(w_min)
        if g_min < 0.0:
            neg_min += 1
        d2 = d2_omega_prime(alpha, w_min, n_pp, lam_pp, u_pp)
        d2_s = selberg_d2_omega(alpha, w_min, n_se, c_se, u_se)
        f2 = abs(d2_s) / (abs(d2) + 1.0e-300)
        f2s.append(f2)
        helpful.append(1.0 if d2_s < 0.0 else 0.0)
        d1_s = selberg_d_omega(alpha, w_min, n_se, c_se, u_se)
        d1_l = lam2_d_omega(alpha, w_min, n_se, l2_se, u_se)
        r1s.append(abs(d1_s) / (abs(d1_l) + 1.0e-300))
        depths.append(g_min / (med_g if med_g != 0.0 else 1.0e-300))
    n_min = int(len(omega_mins))
    h_frac = float(np.mean(helpful)) if helpful else float("nan")
    out = {
        "n_minima": n_min,
        "neg_minima_frac": (neg_min / n_min) if n_min else float("nan"),
        "h": h_frac,
        "median_f2": median_finite(f2s),
        "median_selberg1_over_lam21": median_finite(r1s),
        "median_depth": median_finite(depths),
        "n_neg_minima": neg_min,
    }
    rec("%s_a_%s_summary" % (name, repr(alpha)), out)
    return out


def run_t4(
    gammas, pp_n, pp_lam, pp_u, sel_n, sel_conv, sel_lam2, sel_u,
    lam_dense, primes, a_list, omega_lo, omega_hi, omega_step, n_arch,
    do_wperm: bool, rng, n_gold: int, omega_hi_by_a: dict,
) -> dict:
    emit("T4 REAL-WORLD SIGN TEST")
    g_tup = tuple(float(x) for x in gammas)
    worlds = {}
    ef_rows = []
    ef_ok = True
    for alpha in a_list:
        hi = float(omega_hi_by_a.get(alpha, omega_hi))
        omegas = np.arange(omega_lo, hi + 0.5 * omega_step, omega_step, dtype=np.float64)
        n_used, x_val = cutoff_n(alpha, N_PRIME_CAP)
        rec("T4_cutoff_a_%s" % repr(alpha), {"n_used": n_used, "X": x_val})
        n_pp, lam_pp, u_pp = slice_le(pp_n, pp_lam, pp_u, n_used=n_used)
        n_se, c_se, l2_se, u_se = slice_le(sel_n, sel_conv, sel_lam2, sel_u, n_used=n_used)
        _pr0, _ab0, tail = r608.prime_channels(
            alpha, float(omegas[0]), *r608.pack_primes(lam_dense[: n_used + 1]), n_used,
        )
        rec("T4_env_tail_a_%s" % repr(alpha), tail)
        prime_grid = prime_on_grid(alpha, omegas, n_pp, lam_pp, u_pp)
        pole_grid = np.array([r608.pole_closed(alpha, float(w)) for w in omegas])
        arch_grid = np.array([r608.arch_trapz(alpha, float(w), n_arch) for w in omegas])
        g_main = pole_grid + arch_grid - prime_grid
        worlds.setdefault("MAIN", {})[alpha] = analyze_world(
            "MAIN", alpha, omegas, g_main, n_arch, n_pp, lam_pp, u_pp, n_se, c_se, l2_se, u_se, n_gold,
        )
        if alpha in (1.0, 0.5):
            for omega in (14.134725, 30.0):
                if omega < omega_lo - 1.0e-12 or omega > hi + 1.0e-12:
                    continue
                pole = r608.pole_closed(alpha, omega)
                arch = r608.arch_trapz(alpha, omega, n_arch)
                prime = prime_closed(alpha, omega, n_pp, lam_pp, u_pp)
                g_val = pole + arch - prime
                z_val = r608.zero_sum_online(alpha, omega, g_tup)
                rel = abs(g_val - z_val) / (abs(g_val) + abs(z_val) + 1.0e-300)
                ef_rows.append({"a": alpha, "omega": omega, "G": g_val, "Z": z_val, "rel": rel})
                rec("T4_EF_a_%s_w_%s" % (repr(alpha), repr(omega)), ef_rows[-1])
                if rel > 1.0e-6:
                    ef_ok = False
        signs = rng.choice(np.array([-1.0, 1.0]), size=int(n_pp.size))
        f_scr_pp = lam_pp * signs
        f_dense = np.zeros(n_used + 1, dtype=np.float64)
        idx_pp = n_pp.astype(np.int64)
        f_dense[idx_pp] = f_scr_pp
        conv_scr = dirichlet_square(f_dense, primes[primes <= n_used], n_used)
        ns = np.arange(n_used + 1, dtype=np.float64)
        lam2_scr = f_dense * np.log(np.maximum(ns, 2.0)) + conv_scr
        n_se_s, pack_s = pack_support(conv_scr, lam2_scr)
        c_s, l2_s = pack_s
        u_s = np.log(n_se_s)
        prime_scr = prime_on_grid(alpha, omegas, n_pp, f_scr_pp, u_pp)
        g_scr = pole_grid + arch_grid - prime_scr
        worlds.setdefault("SCRAMBLE", {})[alpha] = analyze_world(
            "SCRAMBLE", alpha, omegas, g_scr, n_arch, n_pp, f_scr_pp, u_pp,
            n_se_s, c_s, l2_s, u_s, n_gold,
        )
        if do_wperm:
            f_perm = rng.permutation(lam_pp)
            f_dense_p = np.zeros(n_used + 1, dtype=np.float64)
            f_dense_p[idx_pp] = f_perm
            conv_p = dirichlet_square(f_dense_p, primes[primes <= n_used], n_used)
            lam2_p = f_dense_p * np.log(np.maximum(ns.astype(np.float64), 2.0)) + conv_p
            n_se_p, pack_p = pack_support(conv_p, lam2_p)
            c_p, l2_p = pack_p
            u_p = np.log(n_se_p)
            prime_p = prime_on_grid(alpha, omegas, n_pp, f_perm, u_pp)
            g_p = pole_grid + arch_grid - prime_p
            worlds.setdefault("WPERM", {})[alpha] = analyze_world(
                "WPERM", alpha, omegas, g_p, n_arch, n_pp, f_perm, u_pp,
                n_se_p, c_p, l2_p, u_p, n_gold,
            )
    rec("T4_EF_rows", ef_rows)
    check("T4_EF_SANITY", ef_ok, "n=%d" % len(ef_rows))
    structural = False
    for alpha, summary in worlds.get("MAIN", {}).items():
        if (
            summary["n_minima"] >= MIN_MINIMA
            and math.isfinite(summary["h"])
            and summary["h"] >= SIGN_STRUCTURAL_H
            and math.isfinite(summary["median_f2"])
            and summary["median_f2"] >= SIGN_STRUCTURAL_F
        ):
            structural = True
    t4_sign = "SELBERG_SIGN_STRUCTURAL" if structural else "SELBERG_SIGN_INDEFINITE"
    blind = True
    for alpha in a_list:
        h_m = worlds.get("MAIN", {}).get(alpha, {}).get("h", float("nan"))
        h_s = worlds.get("SCRAMBLE", {}).get(alpha, {}).get("h", float("nan"))
        if not (math.isfinite(h_m) and math.isfinite(h_s) and abs(h_m - h_s) < WORLD_BLIND_DH):
            blind = False
        if do_wperm:
            h_w = worlds.get("WPERM", {}).get(alpha, {}).get("h", float("nan"))
            if not (math.isfinite(h_m) and math.isfinite(h_w) and abs(h_m - h_w) < WORLD_BLIND_DH):
                blind = False
    t4_world = "WORLD_BLIND" if blind else "WORLD_SEPARATING"
    rec("T4_sign_token", t4_sign)
    rec("T4_world_token", t4_world)
    RESULT["T4_worlds"] = py(worlds)
    return {"worlds": worlds, "sign_token": t4_sign, "world_token": t4_world, "ef": ef_rows}


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    RESULT.clear()
    t_wall0 = time.perf_counter()
    rng = np.random.default_rng(SEED)

    n_selberg = 20_000 if smoke else N_SELBERG_VERIFY
    n_hankel = 500 if smoke else N_HANKEL
    n_starts = 8 if smoke else N_STARTS
    n_pg_iter = 100 if smoke else 500
    n_arch = N_ARCH_SMOKE if smoke else N_ARCH_FULL
    n_online = N_ONLINE
    t0_points = T0_POINTS[:1] if smoke else T0_POINTS
    a_t1 = (0.5,) if smoke else A_T1
    omega_t1 = (14.134725,) if smoke else OMEGA_T1
    t1_lo, t1_hi, t1_step = (10.0, 20.0, 0.05) if smoke else (10.0, 50.0, 0.01)
    a_gate = (0.5,) if smoke else A_GATE
    omega_gate = (30.0,) if smoke else OMEGA_GATE
    g3_points = ((0.5, 30.0),) if smoke else tuple(
        (a_val, w_val) for a_val in (1.0, 0.5, 0.3) for w_val in (14.134725, 30.0, 50.0)
    )
    catalogs = CATALOGS[:1] if smoke else CATALOGS
    n_grid = 1201 if smoke else N_OMEGA_GRID
    n_a_scan = 20 if smoke else N_A_SCAN
    n_bisect = 20 if smoke else BISECT_ITERS
    n_gold = 20 if smoke else 40
    do_lobe_scan = not smoke
    a_t4 = (1.0,) if smoke else A_T4
    t4_lo, t4_hi, t4_step = (10.0, 30.0, 0.05) if smoke else (OMEGA_T4_LO, OMEGA_T4_HI, OMEGA_T4_STEP)
    do_wperm = not smoke
    omega_hi_by_a = {}
    if not smoke:
        omega_hi_by_a[0.3] = OMEGA_T4_HI

    emit("round %d" % ROUND)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("smoke %d" % int(smoke))
    emit("KEIN RH-CLAIM")
    rec("file_sha256", file_sha256())
    rec("n_arch", n_arch)

    gammas = r608.r605.load_online(n_online)
    rec("n_online", len(gammas))
    rec("gamma_1", float(gammas[0]))
    rec("gamma_N", float(gammas[-1]))

    n_need = n_selberg
    for a_val in set(list(a_t1) + list(a_t4) + [p[0] for p in t0_points] + [p[0] for p in g3_points]):
        n_used, _x = cutoff_n(a_val, N_PRIME_CAP)
        n_need = max(n_need, n_used)
    n_need = max(n_need, n_hankel)
    rec("n_sieve", n_need)
    lam_dense = r608.von_mangoldt_table(n_need)
    primes = primes_from_lam(lam_dense)
    lam2, conv = fill_prime_power_selberg(lam_dense, primes, n_need)
    fill_two_prime_structural(lam2, conv, lam_dense, primes, n_need)
    conv_chk = dirichlet_square(lam_dense, primes, n_selberg)
    conv_dir = conv_direct_divisor(lam_dense, n_selberg)
    max_conv_diff = float(max(
        np.max(np.abs(conv[: n_selberg + 1] - conv_chk)),
        np.max(np.abs(conv[: n_selberg + 1] - conv_dir)),
    ))
    rec("T1_generic_conv_maxdiff", max_conv_diff)
    pp_idx = np.flatnonzero(lam_dense) 
    pp_idx = pp_idx[pp_idx >= 2]
    pp_n = pp_idx.astype(np.float64)
    pp_lam = lam_dense[pp_idx]
    pp_u = np.log(pp_n)
    sel_n, packed = pack_support(conv, lam2)
    sel_conv, sel_lam2 = packed
    sel_u = np.log(np.maximum(sel_n, 2.0))
    u_all, weight = r608.pack_primes(lam_dense)
    rec("n_prime_powers", int(pp_n.size))
    rec("n_selberg_nodes", int(sel_n.size))

    t0 = run_t0(pp_n, pp_lam, pp_u, t0_points)
    t1 = run_t1(
        lam_dense, lam2, conv, pp_n, pp_lam, pp_u, sel_n, sel_conv, sel_lam2, sel_u,
        u_all, weight, n_selberg, a_t1, omega_t1, t1_lo, t1_hi, t1_step,
        max_conv_diff, 10.0, 50.0, 0.01,
    )
    t2 = run_t2(pp_n, a_gate, omega_gate, n_hankel, n_starts, n_pg_iter, rng)
    g3 = run_g3(pp_n, pp_lam, pp_u, u_all, weight, primes, g3_points, n_arch)
    t3 = run_t3(gammas, catalogs, n_grid, n_a_scan, n_bisect, n_gold, do_lobe_scan)
    t4 = run_t4(
        gammas, pp_n, pp_lam, pp_u, sel_n, sel_conv, sel_lam2, sel_u,
        lam_dense, primes, a_t4, t4_lo, t4_hi, t4_step, n_arch, do_wperm, rng, n_gold,
        omega_hi_by_a,
    )

    r_lobe = max(t3["r_heat_lobe"]) if t3["r_heat_lobe"] else float("nan")
    r_cos = max(t3["r_heat_cos"]) if t3["r_heat_cos"] else float("nan")
    g3_token = g3["token"]
    if t2["gate_pass"]:
        meta = t2["best"]
        verdict = (
            "GATE_PASS(a=%s,omega=%s,c=%s) | %s | CONTACT_CONDITIONS_COLLAPSE("
            "r_heat_lobe=%s, r_heat_cos=%s) | NEGATIVITY_DOWNSET | %s | %s"
            % (
                repr(meta["a"]), repr(meta["omega"]), repr(meta["c"]),
                g3_token, repr(r_lobe), repr(r_cos),
                t4["sign_token"], t4["world_token"],
            )
        )
    else:
        verdict = (
            "KILLED(STRUCTURAL: selberg-convolution-is-hankel) | "
            "TOEPLITZ_GATE_FAIL(best_lambda_min=%s) | %s | "
            "CONTACT_CONDITIONS_COLLAPSE(r_heat_lobe=%s, r_heat_cos=%s) | "
            "NEGATIVITY_DOWNSET | %s | %s"
            % (
                repr(t2["best_lambda_min"]), g3_token,
                repr(r_lobe), repr(r_cos),
                t4["sign_token"], t4["world_token"],
            )
        )
    rec("VERDICT", verdict)
    emit("KEIN RH-CLAIM")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    rec("CHECKS_pass", len(CHECKS) - n_fail)
    rec("CHECKS_total", len(CHECKS))
    emit("CHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    else:
        emit("ALL CHECKS PASSED")

    payload = py(RESULT)
    payload["SPEC"] = SPEC
    payload["SPEC_SHA"] = SPEC_SHA
    payload["smoke"] = int(smoke)
    payload["CHECKS"] = [(name, bool(ok)) for name, ok in CHECKS]
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    RESULT_PATH.write_bytes(blob)
    result_sha = hashlib.sha256(blob).hexdigest()
    emit("RESULT_SHA %s" % result_sha)
    elapsed = time.perf_counter() - t_wall0
    print("elapsed %s" % repr(elapsed), file=sys.stderr)
    return 0 if n_fail == 0 else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r638 Gabor first-contact / Selberg Hankel scout (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
