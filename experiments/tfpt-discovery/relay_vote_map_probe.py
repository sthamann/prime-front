#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relay_vote_map_probe -- r637  PRIME.RELAY.VOTE.MAP.01

Experiments-only.  Vote map of the lowest eigenmodes of the window
Weil form Q_L = POLE + ARCH − PRIME, asking whether the r633
unanimity C(L)=1 at h₀ is (i) arithmetic, (ii) generic for
translation-type minimizers, or (iii) specific to the critical mode.

Reused verbatim (import):
  * r628 window_box_verifier_probe: 40-digit mp form builder
    assemble_mp (low eigenvectors of Q_L are meaningless in float
    once λ* < 1e-12, i.e. L ≳ 0.6).
  * r619 support_relay_census_probe: events q < e^{2L}, w_q, form
    Q_L, SCRAMBLE / WPERM / EPSTEIN controls, first_negative,
    characterize.
  * r620 p2_reflection_factor_probe: oriented identity
    g_h(d) = −(‖f₊‖² − ‖f₋‖²) for the prime translation term with
    reflection about d/2 on the overlap I=[−L+d, L], P₊/P₋
    projectors, odd/even sectors (f± = ½(f ± R_d f)).
  * r633 frontier_followups_probe F3: coherence
    C = |Σ_q g| / Σ_q |g|, Haar-phase Monte Carlo (cos θ_q),
    min_rayleigh / assemble_window.

V1  Vote map of the lowest m=10 modes on the L-grid.
V2  Parity balance of h₀ on every overlap (r620 identity).
V3  Euler coherence S[k,p^m] vs S[k,p].
V4  Decisive controls: SCRAMBLE, WPERM, EPSTEIN, POLE+ARCH.
V5  Flip test: local R_q-odd projection on overlaps with g>0.
V6  Haar refinement: 200 draws, frac_neg and corr(C, λ_min).

Decision enums (preregistered):
  VOTE_UNANIMITY_GENERIC, VOTE_UNANIMITY_ARITHMETIC,
  VOTE_MODE_SPECIFIC, VOTE_NOT_UNIVERSAL,
  plus V5: FLIP_LEMMA_SUPPORTED / FLIP_COUNTEREXAMPLE.

Kill conditions (preregistered): dual-run RESULT_SHA mismatch;
Gram not PD; C_k ∉ [0,1]; wall cap; identity residual on an odd
trial exceeding 1e-6 (numerical, not a theory result).

Claim boundary: finite-section arithmetic.  Not a ledger row.
Not a paper claim.  Fence: "Exploration on sealed objects; no RH claim."
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
from scipy.linalg import eigh as seigh  # noqa: E402

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import frontier_followups_probe as F3P  # noqa: E402
import p2_reflection_factor_probe as P2RF  # noqa: E402
import support_relay_census_probe as SRC  # noqa: E402
import window_box_verifier_probe as WBV  # noqa: E402

ROUND = 637
SEED = 637202609
CONTRACT = "PRIME.RELAY.VOTE.MAP.01"
FENCE = "Exploration on sealed objects; no RH claim."
PARENTS = "r619/r620/r628/r633"

MP_DPS = int(WBV.MP_DPS)
DAMP_POWER = int(WBV.DAMP_POWER)
PI = math.pi
LOG2 = float(P2RF.LOG2)
UNAN_EPS = 1.0e-10
SIGN_REL = 1.0e-6
G_ZERO = 1.0e-18
ID_REL = 1.0e-6
FLIP_ABS = 1.0e-10
N120_C_TOL = 0.15
LAM_TINY = 1.0e-12
SMOKE_WALL = 180.0
# Dual-run wall: 60 min per compute (user budget), two seal runs.
FULL_WALL = 7200.0

L_GRID_FULL = (0.40, 0.45, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 1.00)
L_GRID_SMOKE = (0.45, 0.55)
N_FULL = 80
N_SMOKE = 24
N_CHECK = 120
N_CHECK_L = (0.55, 0.80)
M_FULL = 10
M_SMOKE = 4
N_MC_FULL = 200
N_MC_SMOKE = 16
L_MC_FULL = (0.45, 0.55, 0.70)
L_MC_SMOKE = (0.55,)
N_OUTER_FULL = int(WBV.N_OUTER_MP_FULL)
N_OUTER_SMOKE = int(WBV.N_OUTER_MP_SMOKE)
N_QUAD = 256
EULER_PAIRS = ((2, 4), (2, 8), (2, 16), (3, 9), (3, 27), (5, 25))
VOTE_ENUMS = (
    "VOTE_UNANIMITY_GENERIC",
    "VOTE_UNANIMITY_ARITHMETIC",
    "VOTE_MODE_SPECIFIC",
    "VOTE_NOT_UNIVERSAL",
)
FLIP_ENUMS = ("FLIP_LEMMA_SUPPORTED", "FLIP_COUNTEREXAMPLE")

SPEC = {
    "round": ROUND,
    "tag": "r637",
    "contract": CONTRACT,
    "parents": PARENTS,
    "identity": "Q=POLE+ARCH-PRIME",
    "g_identity": "g(d)=-(||f+||^2-||f-||^2) on I=[-L+d,L], R:(x)->(d-x)",
    "C": "|sum_q g| / sum_q |g| unweighted",
    "unan": "significant signs equal; |g| > 1e-6 * max|g|",
    "L_grid": list(L_GRID_FULL),
    "N": N_FULL,
    "N_check": N_CHECK,
    "N_check_L": list(N_CHECK_L),
    "m": M_FULL,
    "mp_dps": MP_DPS,
    "n_outer": N_OUTER_FULL,
    "space": "(1-(u/L)^2)^3 * P_n",
    "damp_power": DAMP_POWER,
    "events": "q < exp(2L), Lambda(q)>0, w_q=2*Lambda(q)*q**(-1/2)",
    "euler_pairs": [list(pair) for pair in EULER_PAIRS],
    "controls": ["SCRAMBLE", "WPERM", "EPSTEIN", "POLE+ARCH"],
    "scramble": "uniform(log2, 2 L_max), same weights, frozen seed",
    "wperm": "permutation of weights, same positions, frozen seed",
    "epstein": "keep 2^k only",
    "pole_arch": "minimizer of A; true-prime votes on that h",
    "haar": "Q_theta = A - sum w_q cos(theta_q) Ov_q, n_mc=200",
    "L_mc": list(L_MC_FULL),
    "n_mc": N_MC_FULL,
    "seed": SEED,
    "flip": "local R_q-odd projection on I_q, Gram-renormalize, Delta Q",
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": FENCE,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
VERBOSE = True


def emit(line: str = "") -> None:
    if not VERBOSE:
        return
    LINES.append(line)
    print(line, flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-44s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def section(title: str) -> None:
    emit("")
    emit("=" * 74)
    emit(title)
    emit("=" * 74)


def fmt(value, digits: int = 12) -> str:
    if value is None:
        return "nan"
    if isinstance(value, (bool, np.bool_)):
        return "1" if value else "0"
    if isinstance(value, (int, np.integer)) and not isinstance(value, (bool, np.bool_)):
        return "%d" % int(value)
    number = float(value)
    if math.isnan(number):
        return "nan"
    if not math.isfinite(number):
        return "+inf" if number > 0.0 else "-inf"
    return "%+.*e" % (digits, number)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(payload: dict) -> str:
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def r12(value) -> float | None:
    if value is None:
        return None
    number = float(value)
    if not math.isfinite(number):
        return None
    return float("%.12e" % number)


def is_unan(coh: float) -> bool:
    return math.isfinite(coh) and coh >= 1.0 - UNAN_EPS


def mp_zeros(dimension: int):
    return [[mp.mpf(0) for _ in range(dimension)] for _ in range(dimension)]


def mp_add(mat_a, mat_b, scale_b=1):
    dimension = len(mat_a)
    out = mp_zeros(dimension)
    for ii in range(dimension):
        for jj in range(dimension):
            out[ii][jj] = mat_a[ii][jj] + scale_b * mat_b[ii][jj]
    return WBV.mp_sym(out)


def mp_quad(vec, matrix):
    total = mp.mpf(0)
    dimension = len(matrix)
    for ii in range(dimension):
        inner = mp.mpf(0)
        row = matrix[ii]
        for jj in range(dimension):
            inner += row[jj] * vec[jj]
        total += vec[ii] * inner
    return total


def mp_overlap_at(length, shift, dimension, nodes_i, weights_i):
    """Copy of r628 assemble_mp prime-overlap inner loop, one shift."""
    length_m = mp.mpf(length)
    two_l = 2 * length_m
    shift_m = mp.mpf(float(shift))
    dim = int(dimension)
    out = mp_zeros(dim)
    if shift_m <= 0 or shift_m >= two_l:
        return out
    overlap_length = two_l - shift_m
    points = [
        -length_m + mp.mpf("0.5") * overlap_length * (node + 1)
        for node in nodes_i
    ]
    scaled = [mp.mpf("0.5") * overlap_length * weight for weight in weights_i]
    left = WBV.mp_basis_values(points, length_m, dim)
    right = WBV.mp_basis_values(
        [point + shift_m for point in points], length_m, dim,
    )
    for index_p, weight in enumerate(scaled):
        for ii in range(dim):
            left_w = weight * left[index_p][ii]
            for jj in range(dim):
                out[ii][jj] += left_w * right[index_p][jj]
    return WBV.mp_sym(out)


def mp_lowest_modes(q_mp, g_mp, n_modes: int) -> list[dict]:
    """Generalized eigen Qv=λGv via Cholesky whitening at MP_DPS."""
    mp.mp.dps = MP_DPS
    q_mat = mp.matrix(q_mp)
    g_mat = mp.matrix(g_mp)
    dim = int(q_mat.rows)
    chol = mp.cholesky(g_mat)
    left_inv = chol ** -1
    white = left_inv * q_mat * left_inv.T
    white = (white + white.T) / 2
    eigs, vecs = mp.eigsy(white)
    modes = []
    n_keep = min(int(n_modes), dim)
    for index in range(n_keep):
        col = mp.matrix(dim, 1)
        for row in range(dim):
            col[row] = vecs[row, index]
        vec = left_inv.T * col
        coeff = np.array([float(vec[row]) for row in range(dim)], dtype=np.float64)
        modes.append({
            "lam": float(eigs[index]),
            "coeff": coeff,
            "mp": vec,
        })
    return modes


def votes_from_g(g_vals: np.ndarray) -> dict:
    g_vals = np.asarray(g_vals, dtype=np.float64)
    abs_g = np.abs(g_vals)
    den = float(np.sum(abs_g))
    num = float(np.sum(g_vals))
    mag = float(np.max(abs_g)) if abs_g.size else 0.0
    cut = max(G_ZERO, SIGN_REL * mag)
    if den <= G_ZERO:
        coh = float("nan")
        signs = [0] * int(g_vals.size)
        gauge = 1
        g_out = [float(val) for val in g_vals]
    else:
        gauge = 1 if num >= 0.0 else -1
        g_fix = gauge * g_vals
        num = float(np.sum(g_fix))
        coh = abs(num) / den
        signs = [int(np.sign(val)) if abs(val) > cut else 0 for val in g_fix]
        g_out = [float(val) for val in g_fix]
    sig = [sgn for sgn in signs if sgn != 0]
    unan = (len(sig) <= 1) or all(sgn == sig[0] for sgn in sig)
    dissent = [index for index, sgn in enumerate(signs) if sgn < 0]
    return {
        "C": float(coh),
        "gauge": int(gauge),
        "signs": signs,
        "g": g_out,
        "dissent": dissent,
        "unan": bool(unan),
        "cut": float(cut),
    }


def overlap_pm(length: float, dimension: int, log_q: float, n_quad: int = N_QUAD):
    """r620 P± compressions on I=[d−L, L], WBV damped basis, P2 quadrature."""
    delta = float(log_q)
    left = -float(length) + delta
    right = float(length)
    zeros = np.zeros((dimension, dimension), dtype=np.float64)
    if right - left <= 1.0e-14:
        return {"plus": zeros, "minus": zeros, "empty": True}
    pts_i, w_i = P2RF._interval_quad(left, right, n_quad)
    b_i = WBV.basis_values(pts_i, length, dimension)
    b_r = WBV.basis_values(delta - pts_i, length, dimension)
    b_plus = 0.5 * (b_i + b_r)
    b_minus = 0.5 * (b_i - b_r)
    mass_plus = P2RF._sym(b_plus.T @ (w_i[:, None] * b_plus))
    mass_minus = P2RF._sym(b_minus.T @ (w_i[:, None] * b_minus))
    return {"plus": mass_plus, "minus": mass_minus, "empty": False}


def project_rq_odd(
    length: float,
    dimension: int,
    coeff: np.ndarray,
    gram: np.ndarray,
    log_q: float,
    n_quad: int = N_QUAD,
) -> np.ndarray:
    """L² projection of (identity off I, R_q-odd on I) back into the trial space."""
    delta = float(log_q)
    left_i = -float(length) + delta
    rhs = np.zeros(dimension, dtype=np.float64)
    if left_i > -float(length) + 1.0e-14:
        pts, weights = P2RF._interval_quad(-float(length), left_i, n_quad)
        basis = WBV.basis_values(pts, length, dimension)
        field = basis @ coeff
        rhs = rhs + basis.T @ (weights * field)
    if float(length) - left_i > 1.0e-14:
        pts, weights = P2RF._interval_quad(left_i, float(length), n_quad)
        basis = WBV.basis_values(pts, length, dimension)
        reflected = WBV.basis_values(delta - pts, length, dimension)
        field = basis @ coeff
        odd = 0.5 * (field - reflected @ coeff)
        rhs = rhs + basis.T @ (weights * odd)
    try:
        updated = np.linalg.solve(gram, rhs)
    except np.linalg.LinAlgError:
        updated = np.linalg.lstsq(gram, rhs, rcond=None)[0]
    nrm = float(updated @ gram @ updated)
    if nrm <= 1.0e-30:
        return coeff.copy()
    return updated / math.sqrt(nrm)


def odd_trial(dimension: int) -> np.ndarray:
    coeff = np.zeros(dimension, dtype=np.float64)
    coeff[1 if dimension > 1 else 0] = 1.0
    return coeff


def coherence_of(g_vals) -> float:
    rec = votes_from_g(np.asarray(g_vals, dtype=np.float64))
    return float(rec["C"])


def float_modes(quadratic, gram, n_modes: int) -> list[dict]:
    quadratic = 0.5 * (quadratic + quadratic.T)
    gram = 0.5 * (gram + gram.T)
    dim = gram.shape[0]
    ridge = 1.0e-14 * (float(np.trace(gram)) / max(dim, 1) + 1.0e-30)
    gram_r = gram + ridge * np.eye(dim)
    last = min(int(n_modes), dim) - 1
    try:
        values, vectors = seigh(
            quadratic, gram_r, subset_by_index=[0, last], check_finite=False,
        )
    except Exception:
        values, vectors = np.linalg.eigh(quadratic)
        values = values[: last + 1]
        vectors = vectors[:, : last + 1]
    modes = []
    for index in range(int(values.shape[0])):
        coeff = np.asarray(vectors[:, index], dtype=np.float64)
        nrm = float(coeff @ gram @ coeff)
        if nrm > 1.0e-30:
            coeff = coeff / math.sqrt(nrm)
        modes.append({"lam": float(values[index]), "coeff": coeff, "mp": None})
    return modes


def present_events(length: float):
    qs, logqs, weights = WBV.primes_for_length(float(length))
    return qs, np.asarray(logqs, dtype=np.float64), np.asarray(weights, dtype=np.float64)


def freeze_controls(qs, logqs, weights, length_max: float, seed: int):
    rng = np.random.RandomState(int(seed))
    n_ev = int(len(qs))
    log_hi = 2.0 * float(length_max)
    if n_ev == 0:
        pos = np.zeros(0, dtype=np.float64)
        w_perm = np.zeros(0, dtype=np.float64)
    else:
        pos = np.sort(rng.uniform(LOG2 + 1.0e-9, log_hi - 1.0e-9, size=n_ev))
        w_perm = np.asarray(weights, dtype=np.float64)[rng.permutation(n_ev)]
    two_k = [q_val for q_val in qs if (q_val & (q_val - 1)) == 0]
    log_2k = np.array([math.log(q_val) for q_val in two_k], dtype=np.float64)
    w_2k = np.array(
        [float(weights[qs.index(q_val)]) for q_val in two_k], dtype=np.float64,
    )
    return {
        "scr_pos": pos,
        "scr_w": np.asarray(weights, dtype=np.float64).copy(),
        "w_perm": w_perm,
        "logqs": np.asarray(logqs, dtype=np.float64).copy(),
        "eps_q": two_k,
        "eps_log": log_2k,
        "eps_w": w_2k,
        "qs": list(qs),
        "weights": np.asarray(weights, dtype=np.float64).copy(),
    }


def active_mask(logqs: np.ndarray, length: float) -> np.ndarray:
    two_l = 2.0 * float(length)
    return np.asarray(logqs, dtype=np.float64) < two_l - 1.0e-15


def assemble_prime_mp(length, shifts, weights, dimension, nodes_i, weights_i):
    dim = int(dimension)
    prime = mp_zeros(dim)
    overlaps = []
    two_l = 2.0 * float(length)
    for shift, weight in zip(shifts, weights):
        ov = mp_overlap_at(length, float(shift), dim, nodes_i, weights_i)
        overlaps.append(ov)
        if 0.0 < float(shift) < two_l - 1.0e-15:
            wq = mp.mpf(float(weight))
            for ii in range(dim):
                for jj in range(dim):
                    prime[ii][jj] += wq * ov[ii][jj]
    return WBV.mp_sym(prime), overlaps


def g_list_mp(vec, overlaps) -> np.ndarray:
    return np.array(
        [float(mp_quad(vec, ov)) for ov in overlaps], dtype=np.float64,
    )


def g_list_float(coeff: np.ndarray, overlaps_np: list[np.ndarray]) -> np.ndarray:
    return np.array(
        [float(coeff @ ov @ coeff) for ov in overlaps_np], dtype=np.float64,
    )


def identity_residual(length: float, dimension: int, coeff: np.ndarray, log_q: float):
    packed = overlap_pm(length, dimension, log_q)
    if packed["empty"]:
        return 0.0, 0.0, 0.0, True
    plus2 = float(coeff @ packed["plus"] @ coeff)
    minus2 = float(coeff @ packed["minus"] @ coeff)
    g_id = minus2 - plus2
    delta = float(log_q)
    left = -float(length) + delta
    right = float(length)
    pts, weights = P2RF._interval_quad(left, right, N_QUAD)
    field = WBV.basis_values(pts, length, dimension) @ coeff
    shifted = WBV.basis_values(pts - delta, length, dimension) @ coeff
    g_ov = float(np.dot(weights, field * shifted))
    scale = max(abs(g_ov), abs(g_id), 1.0e-30)
    return plus2, minus2, abs(g_ov - g_id) / scale, False


def haar_block(length: float, dimension: int, n_outer: int, n_mc: int, seed: int) -> dict:
    """r633 F3 Haar-phase MC, plus per-draw C and corr(C, λ_min)."""
    qs, logqs, weights = present_events(length)
    packed = F3P.assemble_window(
        float(length), int(dimension), DAMP_POWER, int(n_outer), logqs, weights,
    )
    n_ev = int(packed["n_ev"])
    rng = np.random.RandomState(int(seed) + int(round(1000.0 * float(length))))
    lams = np.zeros(n_mc, dtype=np.float64)
    cohs = np.zeros(n_mc, dtype=np.float64)
    unans = np.zeros(n_mc, dtype=np.float64)
    for draw in range(n_mc):
        theta = rng.uniform(0.0, 2.0 * PI, size=n_ev)
        prime = np.zeros((dimension, dimension), dtype=np.float64)
        for index in range(n_ev):
            prime = prime + weights[index] * math.cos(theta[index]) * packed["overlaps"][index]
        q_rand = 0.5 * ((packed["free"] - prime) + (packed["free"] - prime).T)
        lam_r, vec_r = F3P.min_rayleigh(q_rand, packed["gram"])
        g_vals = np.array(
            [float(vec_r @ packed["overlaps"][index] @ vec_r) for index in range(n_ev)],
            dtype=np.float64,
        )
        lams[draw] = float(lam_r)
        voted = votes_from_g(g_vals)
        cohs[draw] = voted["C"]
        unans[draw] = 1.0 if voted["unan"] else 0.0
    frac_neg = float(np.mean(lams < 0.0))
    frac_unan = float(np.mean(unans))
    finite = np.isfinite(cohs) & np.isfinite(lams)
    corr = float("nan")
    if int(np.sum(finite)) >= 3 and float(np.std(cohs[finite])) > 1.0e-15:
        corr = float(np.corrcoef(cohs[finite], lams[finite])[0, 1])
    return {
        "L": float(length),
        "n_mc": int(n_mc),
        "n_ev": n_ev,
        "frac_neg": frac_neg,
        "frac_unan": frac_unan,
        "mean_lam": float(np.mean(lams)),
        "std_lam": float(np.std(lams)),
        "mean_C": float(np.nanmean(cohs)),
        "corr": corr,
        "qs": list(qs),
    }


def decide(v1, v4, v5) -> dict:
    h0_unan = all(row["modes"][0]["unan"] for row in v1["rows"] if row["modes"])
    dissent_h0 = []
    for row in v1["rows"]:
        if not row["modes"]:
            continue
        mode0 = row["modes"][0]
        if not mode0["unan"]:
            qs_d = [row["qs"][index] for index in mode0["dissent"]]
            dissent_h0.append({"L": row["L"], "q": qs_d, "signs": mode0["signs"]})
    k_thr = None
    n_modes = max((len(row["modes"]) for row in v1["rows"]), default=0)
    for index in range(n_modes):
        ok = all(
            (index >= len(row["modes"])) or row["modes"][index]["unan"]
            for row in v1["rows"]
        )
        if not ok:
            k_thr = index
            break
    ctrl_nontriv = []
    for rec in v4["samples"]:
        if int(rec["n_ev"]) < 2:
            continue
        ctrl_nontriv.append(bool(rec["unan"]))
    ctrl_unan = bool(ctrl_nontriv) and all(ctrl_nontriv)
    if not h0_unan:
        vote = "VOTE_NOT_UNIVERSAL"
    elif k_thr is not None and k_thr > 0:
        vote = "VOTE_MODE_SPECIFIC"
    elif ctrl_unan:
        vote = "VOTE_UNANIMITY_GENERIC"
    else:
        vote = "VOTE_UNANIMITY_ARITHMETIC"
    return {
        "vote": vote,
        "flip": v5["enum"],
        "k_thr": k_thr,
        "h0_unan": h0_unan,
        "ctrl_unan": ctrl_unan,
        "dissent_h0": dissent_h0,
        "n_ctrl_nontriv": len(ctrl_nontriv),
    }


def compute(smoke: bool) -> dict:
    if smoke:
        l_grid = L_GRID_SMOKE
        dimension = N_SMOKE
        n_modes = M_SMOKE
        n_outer = N_OUTER_SMOKE
        n_mc = N_MC_SMOKE
        l_mc = L_MC_SMOKE
        n_check = 0
        check_l = ()
        n_quad = 96
    else:
        l_grid = L_GRID_FULL
        dimension = N_FULL
        n_modes = M_FULL
        n_outer = N_OUTER_FULL
        n_mc = N_MC_FULL
        l_mc = L_MC_FULL
        n_check = N_CHECK
        check_l = N_CHECK_L
        n_quad = N_QUAD

    length_max = float(max(l_grid))
    qs_max, logqs_max, w_max = present_events(length_max)
    controls = freeze_controls(qs_max, logqs_max, w_max, length_max, SEED)

    section("G0  ODD-TRIAL r620 IDENTITY")
    g0_L = 0.55 if 0.55 in l_grid else float(l_grid[0])
    g0_coeff = odd_trial(dimension)
    gram0 = WBV.gram_matrix(g0_L, dimension, WBV.n_inner_of(dimension))
    nrm0 = float(g0_coeff @ gram0 @ g0_coeff)
    g0_coeff = g0_coeff / math.sqrt(max(nrm0, 1.0e-30))
    plus2, minus2, resid, empty = identity_residual(
        g0_L, dimension, g0_coeff, LOG2,
    )
    emit(
        "  odd trial L=%s N=%d  ||f+||^2=%s ||f-||^2=%s resid=%s empty=%d"
        % (
            fmt(g0_L, 3), dimension, fmt(plus2, 6), fmt(minus2, 6),
            fmt(resid, 4), int(empty),
        )
    )
    g0_ok = (not empty) and resid <= ID_REL

    mp.mp.dps = MP_DPS
    inner_need = max(int(dimension) + 8, 24)
    nodes_i, weights_i = WBV.mp_gl_nodes(inner_need, MP_DPS)

    v1_rows = []
    v2_rows = []
    v3_hits = []
    v4_samples = []
    v5_flips = []
    n120_rows = []

    section("V1–V5  MP VOTE MAP")
    emit(
        "  scramble pos=%s"
        % ",".join(fmt(val, 5) for val in controls["scr_pos"])
    )
    t_loop = time.time()
    for length in l_grid:
        t_l = time.time()
        emit(
            "  assembling L=%s N=%d dps=%d n_outer=%d"
            % (fmt(length, 3), dimension, MP_DPS, n_outer)
        )
        packed = WBV.assemble_mp(float(length), dimension, n_outer, MP_DPS)
        qs = list(packed["qs"])
        _, logqs, weights = present_events(length)
        overlaps = [
            mp_overlap_at(length, float(shift), dimension, nodes_i, weights_i)
            for shift in logqs
        ]
        overlaps_np = [WBV.mp_to_numpy(ov) for ov in overlaps]
        gram_mp = packed["gram"]
        full_mp = packed["full"]
        gram_np = WBV.mp_to_numpy(gram_mp)
        q_np = WBV.mp_to_numpy(full_mp)
        a_mp = mp_add(packed["pole"], packed["arch"])
        a_np = WBV.mp_to_numpy(a_mp)
        try:
            modes = mp_lowest_modes(full_mp, gram_mp, n_modes)
            gram_pd = True
        except Exception as exc:
            emit("  mp eigh fallback L=%s (%s)" % (fmt(length, 3), exc))
            modes = float_modes(q_np, gram_np, n_modes)
            gram_pd = False
        mode_recs = []
        for index, mode in enumerate(modes):
            if mode["mp"] is not None:
                g_vals = g_list_mp(mode["mp"], overlaps)
            else:
                g_vals = g_list_float(mode["coeff"], overlaps_np)
            voted = votes_from_g(g_vals)
            mode_recs.append({
                "k": index,
                "lam": float(mode["lam"]),
                "C": voted["C"],
                "unan": voted["unan"],
                "signs": voted["signs"],
                "g": voted["g"],
                "dissent": voted["dissent"],
                "coeff": mode["coeff"],
            })
            emit(
                "    k=%d λ=%s C=%s unan=%d signs=%s"
                % (
                    index, fmt(mode["lam"], 6), fmt(voted["C"], 6),
                    int(voted["unan"]),
                    ",".join("%d:%+d" % (qs[j], voted["signs"][j]) for j in range(len(qs))),
                )
            )
        v1_rows.append({
            "L": float(length),
            "qs": qs,
            "n_ev": len(qs),
            "gram_pd": gram_pd,
            "modes": mode_recs,
            "lam0": float(mode_recs[0]["lam"]) if mode_recs else float("nan"),
        })

        # V2 h0
        h0 = mode_recs[0]["coeff"] if mode_recs else odd_trial(dimension)
        v2_q = []
        all_odd = True
        for q_val, log_q in zip(qs, logqs):
            pm = overlap_pm(float(length), dimension, float(log_q), n_quad)
            if pm["empty"]:
                continue
            plus2 = float(h0 @ pm["plus"] @ h0)
            minus2 = float(h0 @ pm["minus"] @ h0)
            ratio = minus2 / plus2 if plus2 > 1.0e-30 else float("inf")
            odd_dom = minus2 > plus2
            all_odd = all_odd and odd_dom
            g_true = None
            if mode_recs:
                g_true = mode_recs[0]["g"][qs.index(q_val)]
            v2_q.append({
                "q": int(q_val),
                "plus2": plus2,
                "minus2": minus2,
                "ratio": float(ratio),
                "odd_dom": bool(odd_dom),
                "g": g_true,
                "g_id": minus2 - plus2,
                "even_id": plus2 - minus2,
            })
            emit(
                "    V2 q=%d ||f-||^2/||f+||^2=%s odd_dom=%d g=%s g_id=%s"
                % (
                    int(q_val), fmt(ratio, 4), int(odd_dom),
                    fmt(g_true, 6), fmt(minus2 - plus2, 6),
                )
            )
        v2_rows.append({
            "L": float(length),
            "all_odd": bool(all_odd and v2_q),
            "qs": v2_q,
        })

        # V3 Euler
        sign_by_q = {}
        if mode_recs:
            for index_k, mode in enumerate(mode_recs):
                for q_val, sgn in zip(qs, mode["signs"]):
                    sign_by_q[(index_k, int(q_val))] = int(sgn)
        for index_k in range(len(mode_recs)):
            for p_val, power in EULER_PAIRS:
                if (index_k, p_val) not in sign_by_q:
                    continue
                if (index_k, power) not in sign_by_q:
                    continue
                agree = sign_by_q[(index_k, p_val)] == sign_by_q[(index_k, power)]
                if sign_by_q[(index_k, p_val)] == 0 or sign_by_q[(index_k, power)] == 0:
                    continue
                v3_hits.append({
                    "L": float(length),
                    "k": index_k,
                    "p": int(p_val),
                    "pm": int(power),
                    "agree": bool(agree),
                })

        # V4 controls, reusing A = POLE+ARCH
        def control_vote(name, shifts, wts, on_true_primes=False):
            mask = active_mask(np.asarray(shifts, dtype=np.float64), length)
            sh = np.asarray(shifts, dtype=np.float64)[mask]
            ww = np.asarray(wts, dtype=np.float64)[mask]
            if on_true_primes:
                q_ctrl = a_np
                n_ev = len(qs)
                ov_use = overlaps_np
                labels = qs
            else:
                prime_mp, ov_mp = assemble_prime_mp(
                    length, sh, ww, dimension, nodes_i, weights_i,
                )
                q_mp = mp_add(a_mp, prime_mp, scale_b=-1)
                q_ctrl = WBV.mp_to_numpy(q_mp)
                n_ev = int(sh.size)
                ov_use = [WBV.mp_to_numpy(ov) for ov in ov_mp]
                labels = [r12(float(val)) for val in sh]
            if n_ev == 0:
                return None
            try:
                lam_c, vec_c = WBV.min_rayleigh(q_ctrl, gram_np)
            except Exception:
                lam_c, vec_c = float("nan"), np.zeros(dimension)
            g_c = g_list_float(vec_c, ov_use)
            if on_true_primes:
                g_c = g_list_float(vec_c, overlaps_np)
            voted = votes_from_g(g_c)
            rec = {
                "name": name,
                "L": float(length),
                "lam": float(lam_c),
                "C": voted["C"],
                "unan": voted["unan"],
                "n_ev": int(n_ev),
                "signs": voted["signs"],
                "labels": labels,
                "positive": bool(math.isfinite(lam_c) and lam_c > LAM_TINY),
            }
            emit(
                "    V4 %s λ=%s C=%s unan=%d n_ev=%d pos=%d"
                % (
                    name, fmt(lam_c, 6), fmt(voted["C"], 6),
                    int(voted["unan"]), n_ev, int(rec["positive"]),
                )
            )
            return rec

        v4_samples.append(control_vote(
            "SCRAMBLE", controls["scr_pos"], controls["scr_w"],
        ))
        v4_samples.append(control_vote(
            "WPERM", controls["logqs"], controls["w_perm"],
        ))
        v4_samples.append(control_vote(
            "EPSTEIN", controls["eps_log"], controls["eps_w"],
        ))
        v4_samples.append(control_vote(
            "POLE+ARCH", logqs, weights, on_true_primes=True,
        ))

        # V5 flip on h0, positive votes after gauge
        if mode_recs:
            h0c = mode_recs[0]["coeff"]
            q_old = float(mode_recs[0]["lam"])
            nrm_h = float(h0c @ gram_np @ h0c)
            if nrm_h > 1.0e-30:
                h0n = h0c / math.sqrt(nrm_h)
            else:
                h0n = h0c
            q_old_ray = float(h0n @ q_np @ h0n)
            g_scale = max((abs(val) for val in mode_recs[0]["g"]), default=0.0)
            g_cut = max(G_ZERO, 1.0e-10 * max(g_scale, 1.0e-30))
            for q_val, log_q, g_val in zip(qs, logqs, mode_recs[0]["g"]):
                if g_val <= g_cut:
                    continue
                h_flip = project_rq_odd(
                    float(length), dimension, h0n, gram_np, float(log_q), n_quad,
                )
                q_new = float(h_flip @ q_np @ h_flip)
                delta = q_new - q_old_ray
                a_old = float(h0n @ a_np @ h0n)
                a_new = float(h_flip @ a_np @ h_flip)
                rec_f = {
                    "L": float(length),
                    "q": int(q_val),
                    "g": float(g_val),
                    "q_old": q_old_ray,
                    "q_new": q_new,
                    "delta": delta,
                    "dA": a_new - a_old,
                    "lam_mp": q_old,
                    "lowers": bool(delta < -FLIP_ABS),
                    "raises": bool(delta > FLIP_ABS),
                }
                v5_flips.append(rec_f)
                emit(
                    "    V5 q=%d g=%s ΔQ=%s dA=%s lowers=%d"
                    % (
                        int(q_val), fmt(g_val, 6), fmt(delta, 6),
                        fmt(rec_f["dA"], 6), int(rec_f["lowers"]),
                    )
                )
        emit(
            "  L=%s wall_dt=%s"
            % (fmt(length, 3), fmt(time.time() - t_l, 3))
        )

    v4_samples = [rec for rec in v4_samples if rec is not None]

    # Keep V4 samples at L where the control is positive, plus first negative L.
    v4_kept = []
    by_name: dict[str, list] = {}
    for rec in v4_samples:
        by_name.setdefault(rec["name"], []).append(rec)
    for name, recs in by_name.items():
        recs = sorted(recs, key=lambda item: item["L"])
        seen_neg = False
        for rec in recs:
            if rec["positive"]:
                v4_kept.append(rec)
            elif not seen_neg:
                v4_kept.append(rec)
                seen_neg = True
    v4 = {"samples": v4_kept, "all": v4_samples}

    if not v3_hits:
        v3_frac = float("nan")
        v3_n = 0
        v3_agree = 0
    else:
        v3_agree = sum(1 for hit in v3_hits if hit["agree"])
        v3_n = len(v3_hits)
        v3_frac = v3_agree / max(v3_n, 1)

    section("V3  EULER COHERENCE")
    emit(
        "  comparable pairs=%d agree=%d frac=%s  (8,9,16,25,27 absent for L<=1)"
        % (v3_n, v3_agree, fmt(v3_frac, 4))
    )
    for hit in v3_hits:
        emit(
            "    L=%s k=%d p=%d vs %d agree=%d"
            % (fmt(hit["L"], 3), hit["k"], hit["p"], hit["pm"], int(hit["agree"]))
        )

    if not v5_flips:
        v5_enum = "FLIP_LEMMA_SUPPORTED"
        v5_why = "no positive votes after gauge (vacuous on the scanned grid)"
        v5_counter = None
    elif any(rec["raises"] for rec in v5_flips):
        v5_enum = "FLIP_COUNTEREXAMPLE"
        v5_counter = next(rec for rec in v5_flips if rec["raises"])
        v5_why = "flip raised Q at L=%s q=%d ΔQ=%s" % (
            fmt(v5_counter["L"], 3), v5_counter["q"], fmt(v5_counter["delta"], 6),
        )
    else:
        v5_enum = "FLIP_LEMMA_SUPPORTED"
        n_low = sum(1 for rec in v5_flips if rec["lowers"])
        v5_why = (
            "no positive-vote flip raised <h,Q h> (%d lowered, rest already "
            "R_q-odd to numerical floor); conjecture: minimizers of Q_L are "
            "R_q-odd-dominant on every overlap I_q, provided the POLE/ARCH "
            "cost of the flip is bounded by the prime-term gain "
            "w_q (g(h)-g(P_- h))" % n_low
        )
        v5_counter = None
    v5 = {
        "enum": v5_enum,
        "why": v5_why,
        "counter": v5_counter,
        "n": len(v5_flips),
        "n_lower": sum(1 for rec in v5_flips if rec["lowers"]),
        "flips": v5_flips,
    }
    section("V5  FLIP TEST")
    emit("  %s  n=%d n_lower=%d" % (v5_enum, v5["n"], v5["n_lower"]))
    emit("  %s" % v5_why)

    section("V6  HAAR REFINEMENT")
    haar_n = dimension
    haar_outer = n_outer if n_outer >= 32 else 48
    if smoke:
        haar_n = min(dimension, 24)
        haar_outer = min(n_outer, 32)
    v6_rows = []
    for length in l_mc:
        rec = haar_block(float(length), haar_n, haar_outer, n_mc, SEED)
        v6_rows.append(rec)
        emit(
            "  L=%s n_mc=%d frac_neg=%s frac_unan=%s meanλ=%s meanC=%s corr(C,λ)=%s"
            % (
                fmt(length, 3), rec["n_mc"], fmt(rec["frac_neg"], 4),
                fmt(rec["frac_unan"], 4), fmt(rec["mean_lam"], 5),
                fmt(rec["mean_C"], 4), fmt(rec["corr"], 4),
            )
        )

    if n_check and check_l:
        section("N=120 CHECK")
        inner120 = max(int(n_check) + 8, 24)
        nodes120, w120 = WBV.mp_gl_nodes(inner120, MP_DPS)
        for length in check_l:
            if length not in l_grid:
                continue
            emit("  assembling N=120 L=%s" % fmt(length, 3))
            packed = WBV.assemble_mp(float(length), n_check, n_outer, MP_DPS)
            qs = list(packed["qs"])
            _, logqs, _w = present_events(length)
            ovs = [
                mp_overlap_at(length, float(shift), n_check, nodes120, w120)
                for shift in logqs
            ]
            try:
                modes = mp_lowest_modes(packed["full"], packed["gram"], n_modes)
            except Exception:
                modes = float_modes(
                    WBV.mp_to_numpy(packed["full"]),
                    WBV.mp_to_numpy(packed["gram"]),
                    n_modes,
                )
            row80 = next(item for item in v1_rows if abs(item["L"] - length) < 1e-12)
            recs = []
            for index, mode in enumerate(modes):
                if mode["mp"] is not None:
                    g_vals = g_list_mp(mode["mp"], ovs)
                else:
                    g_vals = g_list_float(
                        mode["coeff"], [WBV.mp_to_numpy(ov) for ov in ovs],
                    )
                voted = votes_from_g(g_vals)
                c80 = row80["modes"][index]["C"] if index < len(row80["modes"]) else float("nan")
                recs.append({
                    "k": index,
                    "C": voted["C"],
                    "C80": c80,
                    "unan": voted["unan"],
                    "lam": float(mode["lam"]),
                })
                emit(
                    "    k=%d C120=%s C80=%s unan=%d"
                    % (index, fmt(voted["C"], 6), fmt(c80, 6), int(voted["unan"]))
                )
            n120_rows.append({"L": float(length), "modes": recs, "qs": qs})

    v1 = {"rows": v1_rows}
    n_pairs = 0
    n_unan = 0
    c_table = []
    for row in v1_rows:
        c_row = []
        for mode in row["modes"]:
            n_pairs += 1
            n_unan += int(mode["unan"])
            c_row.append(r12(mode["C"]))
        c_table.append({"L": r12(row["L"]), "C": c_row, "lam0": r12(row["lam0"])})
    unan_frac = n_unan / max(n_pairs, 1)

    decision = decide(v1, v4, v5)
    emit("  DECISION %s  FLIP %s  k_thr=%s" % (
        decision["vote"], decision["flip"],
        "None" if decision["k_thr"] is None else str(decision["k_thr"]),
    ))

    payload = {
        "C": c_table,
        "unan_frac": r12(unan_frac),
        "n_unan": [n_unan, n_pairs],
        "v2": [
            {
                "L": r12(row["L"]),
                "all_odd": int(row["all_odd"]),
                "ratio": [
                    [item["q"], r12(item["ratio"]), int(item["odd_dom"])]
                    for item in row["qs"]
                ],
            }
            for row in v2_rows
        ],
        "v3": [r12(v3_frac), v3_agree, v3_n],
        "v4": [
            [
                rec["name"], r12(rec["L"]), r12(rec["C"]), int(rec["unan"]),
                int(rec["positive"]), rec["n_ev"], r12(rec["lam"]),
            ]
            for rec in v4_kept
        ],
        "v5": v5_enum,
        "v5_n": [v5["n_lower"], v5["n"]],
        "v5_counter": (
            None if v5_counter is None
            else [r12(v5_counter["L"]), v5_counter["q"], r12(v5_counter["delta"])]
        ),
        "v6": [
            [
                r12(rec["L"]), r12(rec["frac_neg"]), r12(rec["corr"]),
                r12(rec["mean_C"]), r12(rec["mean_lam"]), r12(rec["frac_unan"]),
            ]
            for rec in v6_rows
        ],
        "n120": [
            [
                r12(row["L"]),
                [r12(mode["C"]) for mode in row["modes"]],
                [r12(mode["C80"]) for mode in row["modes"]],
            ]
            for row in n120_rows
        ],
        "vote": decision["vote"],
        "flip": decision["flip"],
        "k_thr": decision["k_thr"],
        "dissent": [
            [r12(item["L"]), list(item["q"])] for item in decision["dissent_h0"]
        ],
        "g0_resid": r12(resid),
    }
    return {
        "payload": payload,
        "v1": v1,
        "v2": v2_rows,
        "v3": {"frac": v3_frac, "n": v3_n, "agree": v3_agree, "hits": v3_hits},
        "v4": v4,
        "v5": v5,
        "v6": v6_rows,
        "n120": n120_rows,
        "decision": decision,
        "g0_resid": resid,
        "g0_ok": g0_ok,
        "unan_frac": unan_frac,
        "n_unan": n_unan,
        "n_pairs": n_pairs,
        "gram_pd": all(row["gram_pd"] for row in v1_rows),
        "controls": controls,
        "cfg": {
            "smoke": smoke,
            "N": dimension,
            "m": n_modes,
            "L": list(l_grid),
        },
    }


def compact_c0(v1_rows) -> str:
    parts = []
    for row in v1_rows:
        c0 = row["modes"][0]["C"] if row["modes"] else float("nan")
        parts.append("%s:%s" % (fmt(row["L"], 2), fmt(c0, 4)))
    return " ".join(parts)


def compact_v2(v2_rows) -> str:
    parts = []
    for row in v2_rows:
        if not row["qs"]:
            continue
        ratios = ",".join(
            "%d:%s" % (item["q"], fmt(item["ratio"], 3)) for item in row["qs"]
        )
        parts.append(
            "%s odd=%d [%s]" % (fmt(row["L"], 2), int(row["all_odd"]), ratios)
        )
    return " | ".join(parts)


def compact_v4(samples) -> str:
    parts = []
    by_name: dict[str, list] = {}
    for rec in samples:
        by_name.setdefault(rec["name"], []).append(rec)
    for name in ("SCRAMBLE", "WPERM", "EPSTEIN", "POLE+ARCH"):
        recs = by_name.get(name, [])
        if not recs:
            continue
        bits = []
        for rec in recs:
            bits.append(
                "%s:C=%s u=%d p=%d" % (
                    fmt(rec["L"], 2), fmt(rec["C"], 3),
                    int(rec["unan"]), int(rec["positive"]),
                )
            )
        parts.append("%s {%s}" % (name, " ".join(bits)))
    return " || ".join(parts)


def compact_v6(rows) -> str:
    parts = []
    for rec in rows:
        parts.append(
            "%s fn=%s u=%s corr=%s C=%s"
            % (
                fmt(rec["L"], 2), fmt(rec["frac_neg"], 3),
                fmt(rec["frac_unan"], 3), fmt(rec["corr"], 3),
                fmt(rec["mean_C"], 3),
            )
        )
    return " ".join(parts)


def run(smoke: bool) -> int:
    global VERBOSE
    CHECKS.clear()
    LINES.clear()
    VERBOSE = True
    wall0 = time.time()
    emit("relay_vote_map_probe r%d" % ROUND)
    emit("contract %s" % CONTRACT)
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("smoke %d" % int(smoke))
    emit("seed %d" % SEED)
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("fence %s" % FENCE)

    rec = compute(smoke)
    VERBOSE = False
    rec2 = compute(smoke)
    VERBOSE = True
    sha1 = payload_sha(rec["payload"])
    sha2 = payload_sha(rec2["payload"])
    decision = rec["decision"]
    v1_rows = rec["v1"]["rows"]
    v5 = rec["v5"]
    v6 = rec["v6"]

    section("GATES")
    check(
        "G0-odd-identity",
        rec["g0_ok"],
        "resid=%s" % fmt(rec["g0_resid"], 6),
    )
    c_ok = True
    for row in v1_rows:
        for mode in row["modes"]:
            coh = mode["C"]
            if math.isfinite(coh) and not (0.0 <= coh <= 1.0 + 1.0e-12):
                c_ok = False
    check("V1-C-in-unit", c_ok, "C_k in [0,1]")
    check("V1-h0-ran", all(row["modes"] for row in v1_rows), "h0 present at every L")
    check(
        "V1-lam-finite",
        all(math.isfinite(row["lam0"]) for row in v1_rows),
        "lam0 finite",
    )
    check("Gram-PD", rec["gram_pd"], "gram_pd=%d" % int(rec["gram_pd"]))
    check(
        "V3-frac",
        rec["v3"]["n"] == 0 or (0.0 <= rec["v3"]["frac"] <= 1.0),
        "frac=%s n=%d" % (fmt(rec["v3"]["frac"], 4), rec["v3"]["n"]),
    )
    check("V4-ran", len(rec["v4"]["samples"]) > 0, "n=%d" % len(rec["v4"]["samples"]))
    check("V5-enum", v5["enum"] in FLIP_ENUMS, v5["enum"])
    check("V6-ran", len(v6) > 0, "n_L=%d" % len(v6))
    check(
        "decision-enum",
        decision["vote"] in VOTE_ENUMS,
        decision["vote"],
    )
    n120_ok = True
    for row in rec["n120"]:
        for mode in row["modes"]:
            if mode["C80"] is None or not math.isfinite(mode["C80"]):
                continue
            if abs(float(mode["C"]) - float(mode["C80"])) > N120_C_TOL:
                n120_ok = False
    if smoke:
        check("N120-skip", True, "smoke")
    else:
        check("N120-agree-C", n120_ok and len(rec["n120"]) == len(N_CHECK_L), "tol=%s" % fmt(N120_C_TOL, 2))
    check("dual-run", sha1 == sha2 and len(sha1) == 64, "RESULT_SHA %s" % sha1[:16])
    wall = time.time() - wall0
    cap = SMOKE_WALL if smoke else FULL_WALL
    check("wall-time", wall <= cap, "wall_s=%s lim=%s" % (fmt(wall, 3), fmt(cap, 1)))

    lemma = (
        "minimizers of Q_L are R_q-odd-dominant on every overlap I_q, "
        "hyp: POLE/ARCH cost of the local flip bounded by the prime-term gain"
    )
    if v5["enum"] == "FLIP_COUNTEREXAMPLE" and v5["counter"] is not None:
        lemma = "COUNTEREXAMPLE L=%s q=%d ΔQ=%s" % (
            fmt(v5["counter"]["L"], 3), v5["counter"]["q"],
            fmt(v5["counter"]["delta"], 6),
        )

    dissent_txt = "none"
    if decision["dissent_h0"]:
        dissent_txt = ",".join(
            "%s:%s" % (fmt(item["L"], 2), "/".join(str(q) for q in item["q"]))
            for item in decision["dissent_h0"]
        )

    state = [
        "STATE r%d %s" % (ROUND, CONTRACT),
        "SHA %s" % file_sha256(),
        "SPEC %s" % SPEC_SHA,
        "RESULT %s" % sha1,
        "GATES PLACEHOLDER",
        "C0 " + compact_c0(v1_rows),
        "unan_frac=%s n=%d/%d k_thr=%s" % (
            fmt(rec["unan_frac"], 4), rec["n_unan"], rec["n_pairs"],
            "None" if decision["k_thr"] is None else str(decision["k_thr"]),
        ),
        "V2 " + compact_v2(rec["v2"]),
        "V3 agree=%s n=%d (pairs with both p and p^m present)" % (
            fmt(rec["v3"]["frac"], 4), rec["v3"]["n"],
        ),
        "V4 " + compact_v4(rec["v4"]["samples"]),
        "V5 %s n_lower=%d/%d" % (v5["enum"], v5["n_lower"], v5["n"]),
        "V5 lemma: %s" % lemma,
        "V6 " + compact_v6(v6),
        "DEC %s + %s  h0_unan=%d ctrl_unan=%d dissent=%s" % (
            decision["vote"], decision["flip"],
            int(decision["h0_unan"]), int(decision["ctrl_unan"]), dissent_txt,
        ),
        "FENCE %s" % FENCE,
        "END_STATE",
    ]
    n_state = len(state)
    check("STATE-le-40", n_state <= 40, "n=%d" % n_state)

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    state[4] = "GATES %d/%d smoke=%d wall_s=%s" % (
        n_pass, n_gate, int(smoke), fmt(wall, 3),
    )

    section("STATE")
    for line in state:
        emit(line)
    emit("STATE_LINES %d" % n_state)

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % sha1)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit(FENCE)
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r637 relay vote map on sealed objects (experiments only)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
