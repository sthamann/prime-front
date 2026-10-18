#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tfpt_spectrum_zero_crosscorr_probe -- r604

QUESTION.  Do TFPT-native spectral data (complex dimensions of the
transfer-string Moran kernel, comb tones ω1,ω2,ω3, E8-clock integers)
correlate with the Riemann-zero ordinates γ_n?  Parent expectation:
NEGATIVE.  This probe decides that with a frozen null and with
explicit-formula positive controls.

FIREWALL.  experiments/tfpt-discovery only.  Search surface, not a
claim.  NO RH claim, NO anti-RH claim, NO ledger/paper/Lean/website/
next.txt edit.  mpmath.zetazero is used as a classical ordinate
table (Odlyzko/Riemann–Siegel), never as evidence for RH.

KERNEL (verbatim fractal_selfsimilarity_hunt F3).
  f(s) = 1 − exp(−a s) − exp(−b s),  a = 6 ln(3/2),  b = 6 ln 3.
  Complex dimensions: zeros of f with Im s > 0, Newton from seeds
  Im = 0.3..T step 0.3, Re seed 0.1, keep −4 < Re < 0.2, T = 300.
  Tones: ω1 = 2π/a, ω2 = 2π/b, ω3 = 2π/(6 ln 2).
  Labelled resonance t = 18.097 (strongest in the T ≤ 60 hunt).
  Clock integers: E8 exponents {1,7,11,13,17,19,23,29}, h = 30,
  register 210, |W(E8)| = 696729600, 240, 248.

ZETA.  γ_n = Im mpmath.zetazero(n), n = 1..N, N = 4000 (≥ 2000).
Loaded from verified_zeros_n7000.npy (pedigree: mpmath.zetazero,
dps 15) when present; otherwise computed and saved beside this
probe.  Spot-checked against zetazero at frozen indices.

TESTS (frozen in SPEC / SPEC_SHA; not fitted after seeing data).
  T1  Spectral comb S(ω) = |Σ_n w(γ_n) exp(i ω γ_n)|, Gaussian
      window over γ.  Null: 2000 uniform random ω in the candidate
      range.  POSITIVES log 2,3,5,7 must have z ≥ 5.  CANDIDATES:
      ω1,ω2,ω3, k ω1 + l ω2 (|k|,|l| ≤ 3, ω > 0), 2π/ln n for
      n ∈ {2,3,5,7,30,210}, log 30, log 210, log 240, log 248.
      Each candidate reports z and distance to the nearest log p^k
      line (so a “hit” at ω1 is immediately unmasked if it is just
      log 13).
  T2  Nearest-neighbour |t_k − nearest γ| for complex dimensions
      t_k ≤ 300 vs γ_n ≤ 300.  Nulls (2000 each): (a) cyclic shift
      of t_k by U(0,20), (b) Poisson of equal count on [0,300],
      (c) GUE unfolded spectra (Hermitian Gaussian eigs, semicircle
      unfolding, folded by inverse Riemann–von Mangoldt).  Two-sided MC
      p-value; tail closer/farther vs null median is reported.
  T3  γ_n mod {2π/ln 30, 2π/ln 210, ω1, ω2} vs uniform (Kuiper V
      and Rayleigh).  Null: 2000 random moduli in the same period
      band.  NOT a positive-control channel (γ mod 2π/ln p is the
      wrong dual); T1 carries the explicit-formula positive.
  T4  Repeat T1–T3 on unfolded ordinates γ̃ = N(γ) (Riemann–von
      Mangoldt main term) so a density gradient cannot pass as a
      TFPT line.

VERDICTS.
  NO_CORRELATION
  POSITIVE_CONTROL_FAILED
  CANDIDATE_FIRES(<name>, z, nearest log p^k)
  ARTIFACT          (z ≥ 5 only on a log p^k alias, or T4-only)

DETERMINISM.  Frozen seeds, no timestamps in stdout, two process
runs byte-identical.  Prints SPEC_SHA, FILE_SHA256, PAYLOAD_SHA256.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA hashes the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
HERE = Path(os.path.abspath(__file__)).resolve().parent
ROUND = 604
N_ZEROS = 4000
T_COMPLEX = 300.0
N_NULL = 2000
Z_FIRE = 5.0
WINDOW_SIGMA_FRAC = 0.25
NEWTON_STEP = 0.3
NEWTON_RE_SEED = 0.1
NEWTON_ITERS = 80
NEWTON_DPS = 25
ZEROS_DPS = 15
SHIFT_U_HI = 20.0
ARTIFACT_ABS = 0.03
KL_MAX = 3
SEED_MASTER = 20260902
SPOT_INDICES = (1, 10, 100)
TWO_PI_LN_N = (2, 3, 5, 7, 30, 210)
LOG_CLOCK_N = (30, 210, 240, 248)
E8_EXPONENTS = (1, 7, 11, 13, 17, 19, 23, 29)
RESONANCE_LABEL = 18.097
GAMMA1_LABEL = 14.134725141734693
GAMMA2_LABEL = 21.022039638771556
VERIFIED_CACHE = HERE / "verified_zeros_n7000.npy"
OWN_CACHE = HERE / "tfpt_spectrum_zero_crosscorr_zeros.npy"

A_FLOAT = 6.0 * math.log(1.5)
B_FLOAT = 6.0 * math.log(3.0)
OMEGA1 = 2.0 * math.pi / A_FLOAT
OMEGA2 = 2.0 * math.pi / B_FLOAT
OMEGA3 = 2.0 * math.pi / (6.0 * math.log(2.0))

SPEC = {
    "round": ROUND,
    "target": "tfpt_spectrum_zero_crosscorr",
    "claim_boundary": "NO_RH_CLAIM experiments_only",
    "n_zeros": N_ZEROS,
    "T_complex": T_COMPLEX,
    "newton_seed_im_step": NEWTON_STEP,
    "newton_seed_re": NEWTON_RE_SEED,
    "newton_filter_re": [-4.0, 0.2],
    "newton_iters": NEWTON_ITERS,
    "newton_dps": NEWTON_DPS,
    "n_null": N_NULL,
    "z_fire": Z_FIRE,
    "window": "gaussian_mid",
    "window_sigma_frac": WINDOW_SIGMA_FRAC,
    "shift_null_u": [0.0, SHIFT_U_HI],
    "artifact_abs": ARTIFACT_ABS,
    "kl_max": KL_MAX,
    "seed_master": SEED_MASTER,
    "zeros_dps": ZEROS_DPS,
    "spot_indices": list(SPOT_INDICES),
    "positives_T1": ["log2", "log3", "log5", "log7"],
    "two_pi_ln_n": list(TWO_PI_LN_N),
    "log_clock": list(LOG_CLOCK_N),
    "t3_moduli": ["2pi_ln30", "2pi_ln210", "omega1", "omega2"],
    "resonance_label": RESONANCE_LABEL,
    "unfolding": "riemann_von_mangoldt_main",
    "gue": "hermitian_gaussian_semicircle_unfold",
    "e8_exponents": list(E8_EXPONENTS),
    "h_e8": 30,
    "register": 210,
    "weyl_e8": 696729600,
    "clock_240": 240,
    "clock_248": 248,
    "kernel": "f(s)=1-exp(-a s)-exp(-b s)",
    "a": "6*ln(3/2)",
    "b": "6*ln 3",
}

SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % (
        "PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    digest = hashlib.sha256()
    with open(os.path.abspath(__file__), "rb") as handle:
        digest.update(handle.read())
    return digest.hexdigest()


def fmt(value: float, digits: int = 6) -> str:
    if not math.isfinite(value):
        return "inf" if value > 0 else "-inf"
    return "%.*e" % (digits, float(value))


def payload_sha(blob: object) -> str:
    return hashlib.sha256(
        json.dumps(blob, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rvm(t: np.ndarray | float) -> np.ndarray | float:
    """Riemann–von Mangoldt main term N(T) = (T/2π) log(T/2π) − T/2π + 7/8."""
    arr = np.asarray(t, dtype=np.float64)
    scalar = arr.ndim == 0
    t_abs = np.maximum(arr, 1.0e-12)
    arg = t_abs / (2.0 * math.pi)
    out = arg * np.log(arg) - arg + 0.875
    if scalar:
        return float(out)
    return out


def inv_rvm(n_val: np.ndarray) -> np.ndarray:
    """Monotone inverse of rvm on a frozen interpolant (no live Newton)."""
    t_grid = np.linspace(2.0, T_COMPLEX + 40.0, 16001)
    n_grid = np.asarray(rvm(t_grid), dtype=np.float64)
    return np.interp(
        np.asarray(n_val, dtype=np.float64), n_grid, t_grid,
    )


def gauss_weights(x: np.ndarray) -> np.ndarray:
    lo = float(x[0])
    hi = float(x[-1])
    span = hi - lo
    mu = 0.5 * (lo + hi)
    sigma = WINDOW_SIGMA_FRAC * span
    w = np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return w


def comb_S(omega: np.ndarray, gamma: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """S(ω) = |Σ w(γ) exp(i ω γ)|, vectorised over ω."""
    om = np.asarray(omega, dtype=np.float64).reshape(-1)
    # chunk to keep the outer product modest
    out = np.empty(om.shape[0], dtype=np.float64)
    chunk = 256
    for start in range(0, om.shape[0], chunk):
        sl = om[start:start + chunk]
        phase = np.exp(1j * sl[:, None] * gamma[None, :])
        out[start:start + chunk] = np.abs(phase @ weights)
    return out


def sieve_primes(limit: int) -> np.ndarray:
    flags = np.ones(limit + 1, dtype=bool)
    flags[:2] = False
    cap = int(limit ** 0.5) + 1
    for p in range(2, cap):
        if flags[p]:
            flags[p * p::p] = False
    return np.nonzero(flags)[0].astype(np.int64)


def log_pk_table(omega_hi: float) -> tuple[np.ndarray, tuple[tuple[int, int, float], ...]]:
    """Ascending log(p^k) up to omega_hi + 1, with (p, k, log) records."""
    cap = int(math.exp(omega_hi + 1.0)) + 8
    cap = max(cap, 32)
    primes = sieve_primes(cap)
    recs: list[tuple[int, int, float]] = []
    hi = omega_hi + 1.0
    for p in primes:
        pk = float(p)
        logv = math.log(pk)
        k = 1
        while logv <= hi:
            recs.append((int(p), k, logv))
            pk *= float(p)
            if pk > 1.0e16:
                break
            logv = math.log(pk)
            k += 1
    recs.sort(key=lambda row: row[2])
    logs = np.array([row[2] for row in recs], dtype=np.float64)
    return logs, tuple(recs)


def nearest_logpk(
    omega: float,
    logs: np.ndarray,
    recs: tuple[tuple[int, int, float], ...],
) -> tuple[float, int, int, float]:
    idx = int(np.searchsorted(logs, omega))
    best_d = float("inf")
    best = (2, 1, 0.0)
    for j in (idx - 1, idx):
        if 0 <= j < len(recs):
            p_val, k_val, logv = recs[j]
            dist = abs(float(logv) - float(omega))
            if dist < best_d:
                best_d = dist
                best = (p_val, k_val, logv)
    return best_d, best[0], best[1], best[2]


def nearest_abs(query: np.ndarray, ref: np.ndarray) -> np.ndarray:
    ref_sorted = np.sort(np.asarray(ref, dtype=np.float64))
    q = np.asarray(query, dtype=np.float64)
    idx = np.searchsorted(ref_sorted, q)
    dist = np.full(q.shape, np.inf, dtype=np.float64)
    for j in (idx - 1, idx):
        mask = (j >= 0) & (j < ref_sorted.size)
        dist[mask] = np.minimum(
            dist[mask], np.abs(q[mask] - ref_sorted[j[mask]]),
        )
    return dist


def kuiper_v(frac: np.ndarray) -> float:
    xs = np.sort(np.mod(np.asarray(frac, dtype=np.float64), 1.0))
    n_val = xs.size
    i = np.arange(1, n_val + 1, dtype=np.float64)
    dplus = float(np.max(i / n_val - xs))
    dminus = float(np.max(xs - (i - 1.0) / n_val))
    return dplus + dminus


def rayleigh_r2(frac: np.ndarray) -> float:
    theta = 2.0 * math.pi * np.mod(np.asarray(frac, dtype=np.float64), 1.0)
    n_val = theta.size
    c_val = float(np.sum(np.cos(theta)))
    s_val = float(np.sum(np.sin(theta)))
    return (c_val * c_val + s_val * s_val) / n_val


def mc_p_two_sided(obs: float, null: np.ndarray) -> float:
    n_val = float(null.size)
    lo = float(np.sum(null <= obs))
    hi = float(np.sum(null >= obs))
    return float(min(1.0, 2.0 * min(lo, hi) / n_val))


def mc_p_right(obs: float, null: np.ndarray) -> float:
    n_val = float(null.size)
    return float(np.sum(null >= obs) / n_val)


def gue_unfolded(n_pts: int, rng: np.random.Generator) -> np.ndarray:
    """Unfolded GUE spectrum: Hermitian Gaussian eigs, semicircle law."""
    if n_pts <= 1:
        return np.array([0.5], dtype=np.float64)
    real = rng.normal(size=(n_pts, n_pts))
    imag = rng.normal(size=(n_pts, n_pts))
    herm = 0.5 * (
        (real + real.T) + 1j * (imag - imag.T)
    ) / math.sqrt(float(n_pts))
    eigs = np.linalg.eigvalsh(herm)
    clipped = np.clip(eigs, -2.0 + 1.0e-12, 2.0 - 1.0e-12)
    unfolded = n_pts * (
        0.5
        + (
            clipped * np.sqrt(4.0 - clipped * clipped)
            + 4.0 * np.arcsin(clipped / 2.0)
        ) / (4.0 * math.pi)
    )
    return np.sort(unfolded)


def hunt_complex_dimensions(t_max: float) -> tuple[np.ndarray, np.ndarray]:
    """Newton hunt as in fractal_selfsimilarity_hunt.py, extended to t_max."""
    prev = mp.mp.dps
    mp.mp.dps = int(NEWTON_DPS)
    a = 6 * mp.log(mp.mpf(3) / 2)
    b = 6 * mp.log(3)

    def f(s: mp.mpc) -> mp.mpc:
        return 1 - mp.e ** (-a * s) - mp.e ** (-b * s)

    def fp(s: mp.mpc) -> mp.mpc:
        return a * mp.e ** (-a * s) + b * mp.e ** (-b * s)

    roots: dict[float, complex] = {}
    t_seed = mp.mpf("0.3")
    step = mp.mpf(str(NEWTON_STEP))
    re0 = mp.mpf(str(NEWTON_RE_SEED))
    while t_seed <= t_max:
        s = mp.mpc(re0, t_seed)
        ok = False
        for _ in range(NEWTON_ITERS):
            deriv = fp(s)
            if abs(deriv) < mp.mpf("1e-30"):
                break
            stepv = f(s) / deriv
            s = s - stepv
            if abs(stepv) < mp.mpf("1e-20"):
                ok = True
                break
        if (
            ok
            and abs(f(s)) < mp.mpf("1e-18")
            and 0.05 < s.imag <= t_max + 0.5
            and -4 < s.real < 0.2
        ):
            key = round(float(s.imag), 6)
            if key not in roots:
                roots[key] = complex(float(s.real), float(s.imag))
        t_seed += step
    mp.mp.dps = prev
    keys = sorted(roots)
    t_arr = np.array(keys, dtype=np.float64)
    re_arr = np.array([roots[k].real for k in keys], dtype=np.float64)
    return t_arr, re_arr


def compute_zetazero(n_zeros: int) -> np.ndarray:
    prev = mp.mp.dps
    mp.mp.dps = int(ZEROS_DPS)
    out = np.empty(n_zeros, dtype=np.float64)
    for index in range(1, n_zeros + 1):
        out[index - 1] = float(mp.zetazero(index).imag)
    mp.mp.dps = prev
    return out


def load_or_compute_zeros(n_zeros: int) -> tuple[np.ndarray, str]:
    if VERIFIED_CACHE.is_file():
        arr = np.asarray(np.load(VERIFIED_CACHE), dtype=np.float64)
        if arr.size >= n_zeros:
            sl = np.ascontiguousarray(arr[:n_zeros])
            return sl, sha256_bytes(sl.tobytes())
    if OWN_CACHE.is_file():
        arr = np.asarray(np.load(OWN_CACHE), dtype=np.float64)
        if arr.size >= n_zeros:
            sl = np.ascontiguousarray(arr[:n_zeros])
            return sl, sha256_bytes(sl.tobytes())
    arr = compute_zetazero(n_zeros)
    np.save(OWN_CACHE, arr)
    sl = np.ascontiguousarray(arr)
    return sl, sha256_bytes(sl.tobytes())


def spot_check_zeros(gamma: np.ndarray) -> list[tuple[int, float, float]]:
    prev = mp.mp.dps
    mp.mp.dps = int(ZEROS_DPS)
    rows: list[tuple[int, float, float]] = []
    for index in SPOT_INDICES:
        if index < 1 or index > gamma.size:
            continue
        ref = float(mp.zetazero(index).imag)
        got = float(gamma[index - 1])
        rows.append((index, got, abs(got - ref)))
    mp.mp.dps = prev
    return rows


def candidate_catalog() -> list[tuple[str, float]]:
    items: list[tuple[str, float]] = [
        ("omega1", OMEGA1),
        ("omega2", OMEGA2),
        ("omega3", OMEGA3),
    ]
    seen = {round(OMEGA1, 10), round(OMEGA2, 10), round(OMEGA3, 10)}
    for k in range(-KL_MAX, KL_MAX + 1):
        for l in range(-KL_MAX, KL_MAX + 1):
            omega = k * OMEGA1 + l * OMEGA2
            if omega <= 1.0e-12:
                continue
            key = round(omega, 10)
            if key in seen:
                continue
            seen.add(key)
            items.append(("k%+d_l%+d" % (k, l), float(omega)))
    for n_val in TWO_PI_LN_N:
        omega = 2.0 * math.pi / math.log(float(n_val))
        key = round(omega, 10)
        if key in seen:
            continue
        seen.add(key)
        items.append(("2pi_ln%d" % n_val, float(omega)))
    for n_val in LOG_CLOCK_N:
        omega = math.log(float(n_val))
        key = round(omega, 10)
        if key in seen:
            continue
        seen.add(key)
        items.append(("log%d" % n_val, float(omega)))
    items.sort(key=lambda row: row[1])
    return items


def t3_moduli() -> list[tuple[str, float]]:
    return [
        ("2pi_ln30", 2.0 * math.pi / math.log(30.0)),
        ("2pi_ln210", 2.0 * math.pi / math.log(210.0)),
        ("omega1", OMEGA1),
        ("omega2", OMEGA2),
    ]


def t1_block(
    gamma: np.ndarray,
    rng: np.random.Generator,
    candidates: list[tuple[str, float]],
    positives: list[tuple[str, float]],
) -> dict:
    weights = gauss_weights(gamma)
    omegas = [row[1] for row in candidates]
    omega_lo = min(omegas)
    omega_hi = max(omegas)
    null_om = rng.uniform(omega_lo, omega_hi, N_NULL)
    s_null = comb_S(null_om, gamma, weights)
    mu = float(np.mean(s_null))
    sd = float(np.std(s_null, ddof=1))
    logs, recs = log_pk_table(omega_hi)

    def pack(name: str, omega: float) -> dict:
        s_val = float(comb_S(np.array([omega]), gamma, weights)[0])
        z_val = (s_val - mu) / sd if sd > 0.0 else 0.0
        dist, p_val, k_val, logv = nearest_logpk(omega, logs, recs)
        return {
            "name": name,
            "omega": float(omega),
            "S": s_val,
            "z": float(z_val),
            "d_logpk": float(dist),
            "near_p": int(p_val),
            "near_k": int(k_val),
            "near_log": float(logv),
            "fires": bool(z_val >= Z_FIRE),
            "artifact": bool(z_val >= Z_FIRE and dist <= ARTIFACT_ABS),
        }

    pos_rows = [pack(name, omega) for name, omega in positives]
    cand_rows = [pack(name, omega) for name, omega in candidates]
    return {
        "omega_lo": float(omega_lo),
        "omega_hi": float(omega_hi),
        "null_mean": mu,
        "null_std": sd,
        "linewidth": float(1.0 / (WINDOW_SIGMA_FRAC * (float(gamma[-1]) - float(gamma[0])))),
        "positives": pos_rows,
        "candidates": cand_rows,
    }


def gue_on_interval(
    n_pts: int,
    lo: float,
    hi: float,
    rng: np.random.Generator,
    fold_rvm: bool,
) -> np.ndarray:
    unfolded = gue_unfolded(n_pts, rng)
    span = unfolded[-1] - unfolded[0]
    if span <= 0.0:
        return np.full(n_pts, 0.5 * (lo + hi))
    unit = (unfolded - unfolded[0]) / span
    if fold_rvm:
        n0 = float(rvm(max(lo, 14.0)))
        n1 = float(rvm(hi))
        return inv_rvm(n0 + unit * (n1 - n0))
    return lo + unit * (hi - lo)


def t2_block(
    t_vals: np.ndarray,
    gamma_cut: np.ndarray,
    rng: np.random.Generator,
    resonance: float,
    window_hi: float,
    fold_rvm: bool,
) -> dict:
    obs_d = nearest_abs(t_vals, gamma_cut)
    obs_mean = float(np.mean(obs_d))
    obs_med = float(np.median(obs_d))
    n_t = int(t_vals.size)
    n_g = int(gamma_cut.size)
    t_lo = 0.0
    t_hi = float(window_hi)

    null_a = np.empty(N_NULL, dtype=np.float64)
    null_b = np.empty(N_NULL, dtype=np.float64)
    null_c = np.empty(N_NULL, dtype=np.float64)
    g_lo = float(gamma_cut[0]) if n_g else t_lo
    g_hi = float(gamma_cut[-1]) if n_g else t_hi
    for i in range(N_NULL):
        offset = float(rng.uniform(0.0, SHIFT_U_HI))
        shifted = np.sort(t_lo + np.mod(t_vals - t_lo + offset, t_hi - t_lo))
        null_a[i] = float(np.mean(nearest_abs(shifted, gamma_cut)))
        pois = np.sort(rng.uniform(t_lo, t_hi, n_t))
        null_b[i] = float(np.mean(nearest_abs(pois, gamma_cut)))
        gue = gue_on_interval(n_g, g_lo, g_hi, rng, fold_rvm)
        null_c[i] = float(np.mean(nearest_abs(t_vals, gue)))

    res_d = nearest_abs(np.array([resonance]), gamma_cut)
    res_obs = float(res_d[0])
    res_a = np.empty(N_NULL, dtype=np.float64)
    res_b = np.empty(N_NULL, dtype=np.float64)
    res_c = np.empty(N_NULL, dtype=np.float64)
    for i in range(N_NULL):
        offset = float(rng.uniform(0.0, SHIFT_U_HI))
        shifted = t_lo + np.mod(resonance - t_lo + offset, t_hi - t_lo)
        res_a[i] = float(nearest_abs(np.array([shifted]), gamma_cut)[0])
        pois = float(rng.uniform(t_lo, t_hi))
        res_b[i] = float(nearest_abs(np.array([pois]), gamma_cut)[0])
        gue = gue_on_interval(n_g, g_lo, g_hi, rng, fold_rvm)
        res_c[i] = float(nearest_abs(np.array([resonance]), gue)[0])

    g1 = float(gamma_cut[0]) if gamma_cut.size else GAMMA1_LABEL
    g2 = float(gamma_cut[1]) if gamma_cut.size > 1 else GAMMA2_LABEL

    def tail_of(obs: float, null: np.ndarray) -> str:
        return "closer" if obs < float(np.median(null)) else "farther"

    return {
        "n_t": n_t,
        "n_gamma_le_T": n_g,
        "mean": obs_mean,
        "median": obs_med,
        "p_shift": mc_p_two_sided(obs_mean, null_a),
        "p_poisson": mc_p_two_sided(obs_mean, null_b),
        "p_gue": mc_p_two_sided(obs_mean, null_c),
        "tail_shift": tail_of(obs_mean, null_a),
        "tail_poisson": tail_of(obs_mean, null_b),
        "tail_gue": tail_of(obs_mean, null_c),
        "resonance": float(resonance),
        "res_nearest": res_obs,
        "res_d_g1": abs(resonance - g1),
        "res_d_g2": abs(resonance - g2),
        "res_g1": g1,
        "res_g2": g2,
        "res_p_shift": mc_p_two_sided(res_obs, res_a),
        "res_p_poisson": mc_p_two_sided(res_obs, res_b),
        "res_p_gue": mc_p_two_sided(res_obs, res_c),
        "res_tail_shift": tail_of(res_obs, res_a),
        "res_tail_poisson": tail_of(res_obs, res_b),
        "res_tail_gue": tail_of(res_obs, res_c),
    }


def t3_block(
    gamma: np.ndarray,
    rng: np.random.Generator,
) -> dict:
    moduli = t3_moduli()
    periods = [row[1] for row in moduli]
    lo = min(periods)
    hi = max(periods)
    null_mod = rng.uniform(lo, hi, N_NULL)
    null_v = np.empty(N_NULL, dtype=np.float64)
    for i, period in enumerate(null_mod):
        null_v[i] = kuiper_v(gamma / period)
    rows = []
    for name, period in moduli:
        frac = gamma / period
        v_val = kuiper_v(frac)
        r2 = rayleigh_r2(frac)
        rows.append({
            "name": name,
            "period": float(period),
            "kuiper_V": float(v_val),
            "rayleigh_R2": float(r2),
            "kuiper_p": mc_p_right(v_val, null_v),
            "rayleigh_p": float(math.exp(-r2)),
        })
    return {
        "mod_lo": float(lo),
        "mod_hi": float(hi),
        "rows": rows,
    }


def global_verdict(t1: dict, t4: dict) -> str:
    pos = t1["positives"]
    if any(row["z"] < Z_FIRE for row in pos):
        return "POSITIVE_CONTROL_FAILED"
    genuine = [
        row for row in t1["candidates"]
        if row["fires"] and not row["artifact"]
    ]
    artifacts = [row for row in t1["candidates"] if row["artifact"]]
    t4_only = [
        row for row in t4["candidates"]
        if row["fires"] and not row["artifact"]
        and not any(
            c["name"] == row["name"] and c["fires"] and not c["artifact"]
            for c in t1["candidates"]
        )
    ]
    if genuine:
        top = max(genuine, key=lambda row: row["z"])
        return "CANDIDATE_FIRES(%s, z=%s, nearest=log(%d^%d))" % (
            top["name"], fmt(top["z"], 3), top["near_p"], top["near_k"],
        )
    if artifacts or t4_only:
        return "ARTIFACT"
    return "NO_CORRELATION"


def pub_t1_row(row: dict) -> dict:
    return {
        "name": row["name"],
        "omega": fmt(row["omega"], 12),
        "S": fmt(row["S"], 12),
        "z": fmt(row["z"], 12),
        "d_logpk": fmt(row["d_logpk"], 12),
        "near": "log(%d^%d)" % (row["near_p"], row["near_k"]),
        "fires": row["fires"],
        "artifact": row["artifact"],
    }


def compute_payload(gamma: np.ndarray, t_all: np.ndarray, re_all: np.ndarray) -> dict:
    t_cut = t_all[t_all <= T_COMPLEX]
    re_cut = re_all[t_all <= T_COMPLEX]
    gamma_cut = gamma[gamma <= T_COMPLEX]
    candidates = candidate_catalog()
    positives = [
        ("log2", math.log(2.0)),
        ("log3", math.log(3.0)),
        ("log5", math.log(5.0)),
        ("log7", math.log(7.0)),
    ]
    # labelled resonance: nearest hunted t to 18.097 (F3 T≤60 strongest)
    if t_cut.size:
        res_idx = int(np.argmin(np.abs(t_cut - RESONANCE_LABEL)))
        resonance = float(t_cut[res_idx])
        strongest_idx = int(np.argmax(re_cut))
        strongest_t = float(t_cut[strongest_idx])
        strongest_re = float(re_cut[strongest_idx])
    else:
        resonance = float(RESONANCE_LABEL)
        strongest_t = float("nan")
        strongest_re = float("nan")

    rng1 = np.random.default_rng(SEED_MASTER)
    t1 = t1_block(gamma, rng1, candidates, positives)
    rng2 = np.random.default_rng(SEED_MASTER + 1)
    t2 = t2_block(
        t_cut, gamma_cut, rng2, resonance,
        window_hi=T_COMPLEX, fold_rvm=True,
    )
    rng3 = np.random.default_rng(SEED_MASTER + 2)
    t3 = t3_block(gamma, rng3)

    gamma_u = np.asarray(rvm(gamma), dtype=np.float64)
    t_u = np.asarray(rvm(t_cut), dtype=np.float64)
    gamma_u_cut = np.asarray(rvm(gamma_cut), dtype=np.float64)
    rng4 = np.random.default_rng(SEED_MASTER + 3)
    t1u = t1_block(gamma_u, rng4, candidates, positives)
    rng5 = np.random.default_rng(SEED_MASTER + 4)
    t2u = t2_block(
        t_u, gamma_u_cut, rng5, float(rvm(resonance)),
        window_hi=float(np.max(gamma_u_cut)), fold_rvm=False,
    )
    rng6 = np.random.default_rng(SEED_MASTER + 5)
    t3u = t3_block(gamma_u, rng6)

    verd = global_verdict(t1, t1u)
    z_map = {row["name"]: row["z"] for row in t1["candidates"]}
    zu_map = {row["name"]: row["z"] for row in t1u["candidates"]}
    t4_dev = []
    for name in sorted(z_map):
        dz = zu_map[name] - z_map[name]
        t4_dev.append((name, z_map[name], zu_map[name], dz))
    return {
        "n_zeros": int(gamma.size),
        "gamma_1": float(gamma[0]),
        "gamma_N": float(gamma[-1]),
        "n_complex": int(t_cut.size),
        "expected_density": B_FLOAT * T_COMPLEX / (2.0 * math.pi),
        "max_re": float(np.max(re_cut)) if re_cut.size else float("nan"),
        "resonance": resonance,
        "strongest_t": strongest_t,
        "strongest_re": strongest_re,
        "t1": t1,
        "t2": t2,
        "t3": t3,
        "t1u": t1u,
        "t2u": t2u,
        "t3u": t3u,
        "t4_dev": t4_dev,
        "verdict": verd,
    }


def seal_of(data: dict) -> str:
    t1 = data["t1"]
    t2 = data["t2"]
    t3 = data["t3"]
    t1u = data["t1u"]
    t2u = data["t2u"]
    t3u = data["t3u"]
    blob = {
        "SPEC_SHA": SPEC_SHA,
        "n_zeros": data["n_zeros"],
        "gamma_1": fmt(data["gamma_1"], 12),
        "gamma_N": fmt(data["gamma_N"], 12),
        "n_complex": data["n_complex"],
        "resonance": fmt(data["resonance"], 12),
        "t1_pos": [pub_t1_row(row) for row in t1["positives"]],
        "t1_cand": [pub_t1_row(row) for row in t1["candidates"]],
        "t1_null": [fmt(t1["null_mean"], 12), fmt(t1["null_std"], 12)],
        "t2": {
            "mean": fmt(t2["mean"], 12),
            "median": fmt(t2["median"], 12),
            "p_shift": fmt(t2["p_shift"], 12),
            "p_poisson": fmt(t2["p_poisson"], 12),
            "p_gue": fmt(t2["p_gue"], 12),
            "tail_shift": t2["tail_shift"],
            "tail_gue": t2["tail_gue"],
            "res": fmt(t2["res_nearest"], 12),
            "res_d_g1": fmt(t2["res_d_g1"], 12),
            "res_d_g2": fmt(t2["res_d_g2"], 12),
            "res_p_shift": fmt(t2["res_p_shift"], 12),
            "res_p_poisson": fmt(t2["res_p_poisson"], 12),
            "res_p_gue": fmt(t2["res_p_gue"], 12),
        },
        "t3": [
            {
                "name": row["name"],
                "V": fmt(row["kuiper_V"], 12),
                "p": fmt(row["kuiper_p"], 12),
            }
            for row in t3["rows"]
        ],
        "t1u_pos_z": [fmt(row["z"], 12) for row in t1u["positives"]],
        "t1u_cand": [pub_t1_row(row) for row in t1u["candidates"]],
        "t2u_p": [
            fmt(t2u["p_shift"], 12),
            fmt(t2u["p_poisson"], 12),
            fmt(t2u["p_gue"], 12),
        ],
        "t3u": [fmt(row["kuiper_p"], 12) for row in t3u["rows"]],
        "verdict": data["verdict"],
    }
    return payload_sha(blob)


def print_t1(title: str, block: dict) -> None:
    section(title)
    print("  window gaussian_mid  sigma_frac=%s  linewidth~%s" % (
        fmt(WINDOW_SIGMA_FRAC, 2), fmt(block["linewidth"], 3)))
    print("  null U(omega) in [%s, %s]  mean S=%s  std=%s  n=%d" % (
        fmt(block["omega_lo"], 6), fmt(block["omega_hi"], 6),
        fmt(block["null_mean"], 6), fmt(block["null_std"], 6), N_NULL))
    print("  POSITIVES  (need z >= %s)" % fmt(Z_FIRE, 1))
    for row in block["positives"]:
        print("    %-10s  omega=%s  S=%s  z=%s  near=log(%d^%d) d=%s" % (
            row["name"], fmt(row["omega"], 8), fmt(row["S"], 6),
            fmt(row["z"], 4), row["near_p"], row["near_k"],
            fmt(row["d_logpk"], 3)))
    print("  CANDIDATES")
    print("    %-16s %10s %10s %8s %18s %10s %s" % (
        "name", "omega", "z", "fires", "nearest log p^k", "d", "tag"))
    for row in block["candidates"]:
        tag = (
            "ARTIFACT" if row["artifact"]
            else ("FIRE" if row["fires"] else ".")
        )
        print("    %-16s %10s %10s %8s %18s %10s %s" % (
            row["name"], fmt(row["omega"], 6), fmt(row["z"], 4),
            "yes" if row["fires"] else "no",
            "log(%d^%d)" % (row["near_p"], row["near_k"]),
            fmt(row["d_logpk"], 4), tag))


def print_t2(title: str, block: dict) -> None:
    section(title)
    print("  n_complex=%d  n_gamma<=T=%d  mean|dt|=%s  median=%s" % (
        block["n_t"], block["n_gamma_le_T"],
        fmt(block["mean"], 6), fmt(block["median"], 6)))
    print("  p_shift=%s (%s)  p_poisson=%s (%s)  p_gue=%s (%s)  (two-sided, n_null=%d)" % (
        fmt(block["p_shift"], 4), block["tail_shift"],
        fmt(block["p_poisson"], 4), block["tail_poisson"],
        fmt(block["p_gue"], 4), block["tail_gue"], N_NULL))
    print("  resonance t=%s  nearest_gamma=%s" % (
        fmt(block["resonance"], 9), fmt(block["res_nearest"], 6)))
    print("  |t-gamma1|=%s (gamma1=%s)  |t-gamma2|=%s (gamma2=%s)" % (
        fmt(block["res_d_g1"], 6), fmt(block["res_g1"], 9),
        fmt(block["res_d_g2"], 6), fmt(block["res_g2"], 9)))
    print("  resonance p_shift=%s (%s)  p_poisson=%s (%s)  p_gue=%s (%s)" % (
        fmt(block["res_p_shift"], 4), block["res_tail_shift"],
        fmt(block["res_p_poisson"], 4), block["res_tail_poisson"],
        fmt(block["res_p_gue"], 4), block["res_tail_gue"]))


def print_t3(title: str, block: dict) -> None:
    section(title)
    print("  Kuiper vs 2000 random moduli in [%s, %s]; Rayleigh p = exp(-R^2)" % (
        fmt(block["mod_lo"], 4), fmt(block["mod_hi"], 4)))
    print("    %-12s %12s %12s %12s %12s" % (
        "name", "period", "Kuiper_V", "Kuiper_p", "Rayleigh_p"))
    for row in block["rows"]:
        print("    %-12s %12s %12s %12s %12s" % (
            row["name"], fmt(row["period"], 6), fmt(row["kuiper_V"], 6),
            fmt(row["kuiper_p"], 4), fmt(row["rayleigh_p"], 4)))


def run() -> int:
    CHECKS.clear()
    print("tfpt_spectrum_zero_crosscorr_probe -- r604")
    print("CLAIM_BOUNDARY EXPERIMENT_ONLY NO_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("omega1=%s  omega2=%s  omega3=%s" % (
        fmt(OMEGA1, 8), fmt(OMEGA2, 8), fmt(OMEGA3, 8)))

    section("G0  ZEROS AND COMPLEX DIMENSIONS")
    gamma, zeros_sha = load_or_compute_zeros(N_ZEROS)
    print("  N=%d  gamma_1=%s  gamma_N=%s" % (
        gamma.size, fmt(float(gamma[0]), 12), fmt(float(gamma[-1]), 12)))
    print("  ZEROS_SHA256 %s" % zeros_sha)
    spots = spot_check_zeros(gamma)
    for index, got, err in spots:
        check(
            "G0-spot-n=%d" % index,
            err < 1.0e-10,
            "got=%s  abserr=%s" % (fmt(got, 12), fmt(err, 3)),
        )
    t_all, re_all = hunt_complex_dimensions(T_COMPLEX)
    expected = B_FLOAT * T_COMPLEX / (2.0 * math.pi)
    print("  complex dims n=%d  expected b T / 2pi ~ %s  max Re=%s" % (
        t_all.size, fmt(expected, 3),
        fmt(float(np.max(re_all)) if re_all.size else float("nan"), 6)))
    check(
        "G0-hunt-populated",
        t_all.size >= 0.7 * expected,
        "n=%d expected~%s" % (t_all.size, fmt(expected, 2)),
    )
    check(
        "G0-nonlattice-Re",
        re_all.size == 0 or float(np.max(re_all)) < 1.0 / 6.0 - 1.0e-9,
        "maxRe=%s" % fmt(float(np.max(re_all)) if re_all.size else float("nan"), 6),
    )

    data1 = compute_payload(gamma, t_all, re_all)
    data2 = compute_payload(gamma, t_all, re_all)
    seal1 = seal_of(data1)
    seal2 = seal_of(data2)
    check("G0-determinism-two-run", seal1 == seal2, "payload hashed twice")
    data = data1

    print_t1("T1  SPECTRAL COMB  (raw ordinates)", data["t1"])
    pos_ok = all(row["z"] >= Z_FIRE for row in data["t1"]["positives"])
    check(
        "T1-positive-controls-z>=5",
        pos_ok,
        "z=" + ",".join(fmt(row["z"], 3) for row in data["t1"]["positives"]),
    )

    print_t2("T2  NEAREST NEIGHBOUR  t_k vs gamma (T<=300)", data["t2"])
    print_t3("T3  CLOCK MODULI  (Kuiper / Rayleigh; null random moduli)", data["t3"])

    print_t1("T4  T1 ON UNFOLDED  gamma-tilde = N(gamma)", data["t1u"])
    print_t2("T4  T2 ON UNFOLDED", data["t2u"])
    print_t3("T4  T3 ON UNFOLDED", data["t3u"])
    section("T4  Z-SCORE SHIFTS  (unfolded minus raw)")
    print("    %-16s %10s %10s %10s" % ("name", "z_raw", "z_unf", "delta"))
    max_abs_dz = 0.0
    for name, z_raw, z_unf, dz in data["t4_dev"]:
        max_abs_dz = max(max_abs_dz, abs(dz))
        flag = ""
        if z_unf >= Z_FIRE and z_raw < Z_FIRE:
            flag = " T4_ONLY"
        print("    %-16s %10s %10s %10s%s" % (
            name, fmt(z_raw, 4), fmt(z_unf, 4), fmt(dz, 4), flag))
    print("  max |z_unf - z_raw| = %s" % fmt(max_abs_dz, 4))

    section("G5  VERDICT")
    verd = data["verdict"]
    print("VERDICT %s" % verd)
    print("INTERPRETATION experiments-only; classical ordinates; no RH claim.")
    print("PAYLOAD_SHA256 %s" % seal1)
    print("ZEROS_SHA256 %s" % zeros_sha)
    print("NO_RH_CLAIM")
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
