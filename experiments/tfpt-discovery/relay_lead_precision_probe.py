#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relay_lead_precision_probe -- r635  PRIME.RELAY.LEAD.PRECISION.01

Experiments-only precision study of the r619 support-event leads Δ_q.
Copied/imported (not reinvented):

  * r619  window Weil form Q_L = POLE+ARCH−PRIME on [−L,L], events
    q≤32 with Λ(q)>0, L_q = (1/2) log q, lead Δ_q, L_det census.
  * r628  mp/40-digit window-form builder, GL nodes, interval Cholesky.
  * r630b tall-QR N-sweep {40,60,80,120,160}, damped3 vs plain
    Legendre, |Δ(120)−Δ(80)|<0.002 convergence (adapted from λ*).
  * r623  predecessor POLE+ARCH and translation P_q = overlap(log q).

P1  r619 predecessor (read from sealed source): drop=1 ancestor
    n_keep = j_ev−1, i.e. only events q'<q, no later entries.
    That is D2 "frozen predecessor".  This probe reports BOTH
      D1  "true minus q": every other event present as it enters,
          only q missing;
      D2  "frozen predecessor": only q'<q, later entries withheld.

P2  mp dps=40 for L_q≤1.2 (q≤11), dps=80 for q=13…32.
    N∈{40,60,80,120} all events, N=160 for q≤7; bases damped3 and
    plain.  Δ_q(N) by LDLᵀ/Cholesky PSD-boundary bisection in L
    to ±0.0005 (no full mp eigensolve).  Converged iff
    |Δ(120)−Δ(80)|<0.002 and |Δ(160)−Δ(120)|<0.002 where present.

P3  Null: s_q = L_{q_next}−L_q = (1/2) log(q_next/q); report Δ_q/s_q.
    At q=31→32, s_q≈0.016.

P4  Per event: λ*(L_q) true-form margin at entry (q not yet
    strictly active) and r_q = −dλ_min(Q⁻)/dL just after L_q,
    finite differences in mp, for r636.

Decision: LEAD_CONVERGED_CONSTANT / LEAD_CONVERGED_VARYING /
LEAD_PARTIAL / LEAD_N_ARTIFACT / LEAD_SPACING_LIMITED.

Kill: if L_q≤1 leads drift with N, Δ≈0.015 is a basis artifact and
the just-in-time reading is withdrawn (LEAD_N_ARTIFACT).

Primes/ARCH are prime-side; no zero table is used.
Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: Exploration on sealed objects; no RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from gmpy2 import (  # noqa: E402
    cosh as gcosh,
    exp as gexp,
    get_context,
    log as glog,
    mpfr,
    sinh as gsinh,
    sqrt as gsqrt,
)

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import support_relay_census_probe as R619  # noqa: E402
import window_box_verifier_probe as R628  # noqa: E402
import margin_law_symreg_probe as R630  # noqa: E402
import semilocal_p2_dilation_probe as R623  # noqa: E402

ROUND = 635
SEED = 635202609
CONTRACT = "PRIME.RELAY.LEAD.PRECISION.01"
FENCE = "Exploration on sealed objects; no RH claim"
TAG = "r635"
R619_SHA_PREFIX = "7299737ded85418e"
R628_SHA_PREFIX = "36c0e66a71c6b8a3"
R630_SHA_PREFIX = "87febb97aaee5dcd"
R623_SHA_PREFIX = "5890676d194739b1"

Q_MAX_FULL = 32
Q_MAX_SMOKE = 5
N_SWEEP = (40, 60, 80, 120)
N_SWEEP_SMOKE = (40, 80)
N_EXTRA = 160
N_Q_EXTRA = 7
L_DPS40 = 1.2
DPS_LO = 40
DPS_HI = 80
DPS_SMOKE = 25
LEAD_TOL_FULL = 0.0005
LEAD_TOL_SMOKE = 0.002
CONV_ABS = 0.002
BAND_WIDTH = 0.005
SPACING_REL = 0.20
SPACING_QMIN = 8
DAMP_POWER = 3
SEARCH_PAD = 0.08
H_FD = 0.001
N_P4 = 80
N_OUTER_LO = 24
N_OUTER_HI = 32
N_OUTER_SMOKE = 16
COARSE_OFFSETS = (0.0, 0.004, 0.010, 0.018, 0.030, 0.050, 0.080)
RESULT_PATH = HERE / "relay_lead_precision_result.json"

DECISIONS = (
    "LEAD_CONVERGED_CONSTANT",
    "LEAD_CONVERGED_VARYING",
    "LEAD_PARTIAL",
    "LEAD_N_ARTIFACT",
    "LEAD_SPACING_LIMITED",
)

SPEC = {
    "round": ROUND,
    "tag": TAG,
    "contract": CONTRACT,
    "parent_r619": "support_relay_census_probe D2 frozen predecessor",
    "r619_predecessor": (
        "drop=1 n_keep=j_ev-1; only q'<q; later entries withheld"
    ),
    "definitions": ["D1_true_minus_q", "D2_frozen_predecessor"],
    "events": "prime_powers_q_le_32_Lambda_gt_0",
    "L_q": "0.5*log(q)",
    "lead": "first L>L_q with lambda_min(Q^-(L))<0; Delta=L-L_q",
    "identity": "Q=POLE+ARCH-PRIME",
    "pole": "2*Fplus*Fminus",
    "arch": "int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0)",
    "kernel": "exp(x/2)/sinh(x)",
    "P_q": "overlap_matrix(L, log q)  (r623 translation)",
    "w_q": "2*Lambda(q)*q**(-1/2)",
    "spaces": ["damped3", "plain"],
    "damp_power": DAMP_POWER,
    "N_sweep": list(N_SWEEP),
    "N_extra": N_EXTRA,
    "N_extra_q_le": N_Q_EXTRA,
    "dps_lo": DPS_LO,
    "dps_hi": DPS_HI,
    "dps_cut_L": L_DPS40,
    "lead_tol": LEAD_TOL_FULL,
    "conv_abs": CONV_ABS,
    "psd": "gmpy2 Cholesky of Q (Sylvester: sign(lambda_min pencil)=sign(Q))",
    "no_eigensolve": True,
    "no_zero_table": True,
    "s_q": "0.5*log(q_next/q)",
    "r_q": "-d lambda_min(Q^-)/dL just after L_q, FD h=0.001",
    "seed": SEED,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": FENCE,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []
_GL_GMPY: dict[tuple[int, int], tuple[list, list]] = {}
_CL_GMPY: dict[tuple[float, int], object] = {}


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


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


def fmt(value, digits: int = 16) -> str:
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
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    ).hexdigest()


def set_dps(dps: int) -> None:
    digits = int(dps)
    get_context().precision = int(digits * math.log2(10.0)) + 16
    mp.mp.dps = digits


def gl_gmpy(n_min: int, dps: int):
    key = (int(n_min), int(dps))
    cached = _GL_GMPY.get(key)
    if cached is not None:
        return cached
    xs_mp, ws_mp = R628.mp_gl_nodes(n_min, dps)
    xs = [mpfr(str(val)) for val in xs_mp]
    ws = [mpfr(str(val)) for val in ws_mp]
    _GL_GMPY[key] = (xs, ws)
    return xs, ws


def c_L_gmpy(length: float, dps: int):
    key = (round(float(length), 12), int(dps))
    cached = _CL_GMPY.get(key)
    if cached is not None:
        return cached
    set_dps(dps)
    ell = mpfr(str(float(length)))
    span = 2 * ell
    n_quad = 96 if int(dps) >= 80 else 64
    nodes, weights = gl_gmpy(n_quad, dps)
    acc = mpfr(0)
    half = mpfr("0.5") * span
    for node, weight in zip(nodes, weights):
        x_val = half * (node + 1)
        w_val = half * weight
        if x_val < mpfr("1e-18"):
            integrand = mpfr("-0.5")
        else:
            kern = gmpy_exp_half_over_sinh(x_val)
            integrand = kern - 1 / x_val
        acc += w_val * integrand
    euler = mpfr(str(mp.euler))
    value = acc + glog(4 * ell) + euler + glog(mpfr(str(math.pi)))
    _CL_GMPY[key] = value
    return value


def gmpy_exp_half_over_sinh(x_val):
    if x_val < mpfr("1e-18"):
        return mpfr("0.5")
    return gexp(x_val / 2) / gsinh(x_val)


def basis_gmpy(points, length, dimension: int, power: int):
    two_l = 2 * length
    scale0 = 1 / gsqrt(two_l)
    rows = []
    dim = int(dimension)
    pow_i = int(power)
    for point in points:
        row = [scale0]
        if dim == 1:
            rows.append(_damp_row(row, point, length, pow_i))
            continue
        scaled = point / length
        row.append(gsqrt(mpfr(3) / two_l) * scaled)
        previous, current = mpfr(1), scaled
        for degree in range(1, dim - 1):
            following = (
                ((2 * degree + 1) * scaled * current - degree * previous)
                / (degree + 1)
            )
            row.append(gsqrt(mpfr(2 * degree + 3) / two_l) * following)
            previous, current = current, following
        rows.append(_damp_row(row, point, length, pow_i))
    return rows


def _damp_row(row, point, length, power: int):
    if power <= 0:
        return row
    loc = point / length
    damp = (1 - loc * loc) ** power
    return [damp * value for value in row]


def syrk(left, right, scaled, dimension: int, symmetric_src: bool = False):
    dim = int(dimension)
    out = [[mpfr(0) for _ in range(dim)] for _ in range(dim)]
    if symmetric_src:
        for weight, lrow, rrow in zip(scaled, left, right):
            for ii in range(dim):
                left_w = weight * lrow[ii]
                row = out[ii]
                for jj in range(ii, dim):
                    row[jj] += left_w * rrow[jj]
        for ii in range(dim):
            for jj in range(ii):
                out[ii][jj] = out[jj][ii]
        return out
    for weight, lrow, rrow in zip(scaled, left, right):
        for ii in range(dim):
            left_w = weight * lrow[ii]
            row = out[ii]
            for jj in range(dim):
                row[jj] += left_w * rrow[jj]
    half = mpfr("0.5")
    for ii in range(dim):
        for jj in range(ii):
            acc = half * (out[ii][jj] + out[jj][ii])
            out[ii][jj] = acc
            out[jj][ii] = acc
    return out


def mat_add(mat_a, mat_b, scale_b=1, dimension: int | None = None):
    dim = int(dimension if dimension is not None else len(mat_a))
    out = [[mpfr(0) for _ in range(dim)] for _ in range(dim)]
    for ii in range(dim):
        for jj in range(dim):
            out[ii][jj] = mat_a[ii][jj] + scale_b * mat_b[ii][jj]
    return out


def axpy_pair(mat_q, mat_g, sigma, dimension: int):
    dim = int(dimension)
    out = [[mpfr(0) for _ in range(dim)] for _ in range(dim)]
    for ii in range(dim):
        for jj in range(dim):
            out[ii][jj] = mat_q[ii][jj] - sigma * mat_g[ii][jj]
    return out


def mat_scale(matrix, scale, dimension: int):
    dim = int(dimension)
    out = [[mpfr(0) for _ in range(dim)] for _ in range(dim)]
    for ii in range(dim):
        for jj in range(dim):
            out[ii][jj] = scale * matrix[ii][jj]
    return out


def mat_copy_n(matrix, dimension: int):
    dim = int(dimension)
    return [[matrix[ii][jj] for jj in range(dim)] for ii in range(dim)]


def chol_ok(matrix, dimension: int, tiny) -> bool:
    dim = int(dimension)
    work = [[matrix[ii][jj] for jj in range(dim)] for ii in range(dim)]
    for ii in range(dim):
        for jj in range(ii):
            acc = work[ii][jj]
            for kk in range(jj):
                acc -= work[ii][kk] * work[jj][kk]
            diag = work[jj][jj]
            if diag <= tiny:
                return False
            work[ii][jj] = acc / diag
        acc = work[ii][ii]
        for kk in range(ii):
            acc -= work[ii][kk] * work[ii][kk]
        if acc <= tiny:
            return False
        work[ii][ii] = gsqrt(acc)
    return True


def psd_q(matrix, dimension: int, dps: int) -> bool:
    scale = mpfr(10) ** mpfr(-(int(dps) - 8))
    return chol_ok(matrix, dimension, scale)


def lam_min_shift(matrix, gram, dimension: int, dps: int) -> float:
    """Generalized λ_min of (Q,G) by PSD-boundary bisection in the shift σ."""
    dim = int(dimension)
    tiny = mpfr(10) ** mpfr(-(int(dps) - 8))
    g_use = mat_copy_n(gram, dim)

    def shifted(sigma):
        return axpy_pair(matrix, g_use, sigma, dim)

    pos0 = chol_ok(matrix, dim, tiny)
    if pos0:
        lo, hi = mpfr(0), mpfr("1e-4")
        guard = 0
        while chol_ok(shifted(hi), dim, tiny) and hi < mpfr("1e6") and guard < 80:
            lo = hi
            hi *= 4
            guard += 1
        if chol_ok(shifted(hi), dim, tiny):
            return float(hi)
        for _ in range(56):
            mid = (lo + hi) / 2
            if chol_ok(shifted(mid), dim, tiny):
                lo = mid
            else:
                hi = mid
        return float((lo + hi) / 2)
    lo, hi = mpfr("-1e-4"), mpfr(0)
    guard = 0
    while (not chol_ok(shifted(lo), dim, tiny)) and lo > mpfr("-1e6") and guard < 80:
        hi = lo
        lo *= 4
        guard += 1
    if not chol_ok(shifted(lo), dim, tiny):
        return float("nan")
    for _ in range(56):
        mid = (lo + hi) / 2
        if chol_ok(shifted(mid), dim, tiny):
            lo = mid
        else:
            hi = mid
    return float((lo + hi) / 2)


class GmpyAssembler:
    """POLE+ARCH+P_q at N_max; nested N-sections are principal submatrices."""

    def __init__(
        self,
        n_max: int,
        power: int,
        dps: int,
        n_outer: int,
        logqs: np.ndarray,
        weights: np.ndarray,
    ):
        self.n_max = int(n_max)
        self.power = int(power)
        self.dps = int(dps)
        self.n_outer = int(n_outer)
        self.n_inner = max(self.n_max + 8, 24)
        self.logqs = np.asarray(logqs, dtype=np.float64)
        self.weights = np.asarray(weights, dtype=np.float64)
        self.cache: dict[float, dict] = {}

    def assemble(self, length: float) -> dict:
        key = round(float(length), 12)
        packed = self.cache.get(key)
        if packed is not None:
            return packed
        set_dps(self.dps)
        n_max = self.n_max
        length_m = mpfr(str(float(length)))
        two_l = 2 * length_m
        nodes_i, weights_i = gl_gmpy(self.n_inner, self.dps)
        points_g = [length_m * node for node in nodes_i]
        scaled_g = [length_m * weight for weight in weights_i]
        basis_g = basis_gmpy(points_g, length_m, n_max, self.power)
        gram = syrk(basis_g, basis_g, scaled_g, n_max, symmetric_src=True)

        cosh_v = [mpfr(0)] * n_max
        sinh_v = [mpfr(0)] * n_max
        for point, weight, row in zip(points_g, scaled_g, basis_g):
            chv = gcosh(point / 2)
            shv = gsinh(point / 2)
            for index in range(n_max):
                amp = weight * row[index]
                cosh_v[index] += amp * chv
                sinh_v[index] += amp * shv
        pole = [[mpfr(0) for _ in range(n_max)] for _ in range(n_max)]
        for ii in range(n_max):
            for jj in range(n_max):
                pole[ii][jj] = (
                    2 * cosh_v[ii] * cosh_v[jj] - 2 * sinh_v[ii] * sinh_v[jj]
                )

        overlaps = []
        for shift_f in self.logqs:
            shift = mpfr(str(float(shift_f)))
            if shift <= 0 or shift >= two_l:
                overlaps.append(None)
                continue
            overlap_length = two_l - shift
            points = [
                -length_m + mpfr("0.5") * overlap_length * (node + 1)
                for node in nodes_i
            ]
            scaled = [
                mpfr("0.5") * overlap_length * weight for weight in weights_i
            ]
            left = basis_gmpy(points, length_m, n_max, self.power)
            right = basis_gmpy(
                [point + shift for point in points], length_m, n_max, self.power,
            )
            overlaps.append(syrk(left, right, scaled, n_max))

        c_l = c_L_gmpy(float(length), self.dps)
        nodes_o, weights_o = gl_gmpy(self.n_outer, self.dps)
        arch = [[mpfr(0) for _ in range(n_max)] for _ in range(n_max)]
        for node, weight in zip(nodes_o, weights_o):
            distance = length_m * (node + 1)
            dist_w = length_m * weight
            kern = gmpy_exp_half_over_sinh(distance)
            overlap_length = two_l - distance
            points = [
                -length_m + mpfr("0.5") * overlap_length * (inode + 1)
                for inode in nodes_i
            ]
            scaled = [
                mpfr("0.5") * overlap_length * iweight for iweight in weights_i
            ]
            left = basis_gmpy(points, length_m, n_max, self.power)
            right = basis_gmpy(
                [point + distance for point in points], length_m, n_max, self.power,
            )
            overlap = syrk(left, right, scaled, n_max)
            factor = dist_w * kern
            for ii in range(n_max):
                for jj in range(ii, n_max):
                    delta = factor * (gram[ii][jj] - overlap[ii][jj])
                    arch[ii][jj] += delta
        for ii in range(n_max):
            for jj in range(ii, n_max):
                arch[ii][jj] = arch[ii][jj] - c_l * gram[ii][jj]
                arch[jj][ii] = arch[ii][jj]
        free = mat_add(arch, pole, 1, n_max)
        packed = {
            "gram": gram,
            "pole": pole,
            "arch": arch,
            "free": free,
            "overlaps": overlaps,
            "c_L": c_l,
            "length": float(length),
        }
        self.cache[key] = packed
        return packed

    def quadratic(self, length: float, dimension: int, indices) -> object:
        packed = self.assemble(length)
        dim = int(dimension)
        two_l = 2.0 * float(length)
        full = mat_copy_n(packed["free"], dim)
        for index in indices:
            log_q = float(self.logqs[index])
            if not (0.0 < log_q < two_l - 1.0e-15):
                continue
            overlap = packed["overlaps"][index]
            if overlap is None:
                continue
            w_q = mpfr(str(float(self.weights[index])))
            for ii in range(dim):
                for jj in range(dim):
                    full[ii][jj] -= w_q * overlap[ii][jj]
        return full


def d1_indices(n_events: int, skip: int) -> list[int]:
    return [index for index in range(n_events) if index != skip]


def d2_indices(skip: int) -> list[int]:
    return list(range(int(skip)))


def true_indices(length: float, logqs: np.ndarray) -> list[int]:
    two_l = 2.0 * float(length)
    return [
        index for index, log_q in enumerate(logqs)
        if 0.0 < float(log_q) < two_l - 1.0e-15
    ]


def r619_predecessor_is_d2() -> tuple[bool, str]:
    source = inspect.getsource(R619.run)
    has_drop = "n_keep = max(0, j_ev - drop)" in source
    uses_one = "mu_anc(point, 1)" in source
    assemble_cap = "assemble(point, n_keep)" in source
    ok = has_drop and uses_one and assemble_cap
    detail = (
        "r619 mu_anc drop=1 => n_keep=j_ev-1, events q'<q only (D2 frozen)"
        if ok else "r619 ancestor pattern not found"
    )
    return ok, detail


def round_or_none(value, digits: int):
    if value is None:
        return None
    number = float(value)
    if not math.isfinite(number):
        return None
    return round(number, digits)


def n_list_for(q_val: int, smoke: bool) -> list[int]:
    ns = list(N_SWEEP_SMOKE if smoke else N_SWEEP)
    if (not smoke) and int(q_val) <= N_Q_EXTRA and N_EXTRA not in ns:
        ns.append(N_EXTRA)
    return ns


def dps_for_lq(ell: float, smoke: bool) -> int:
    if smoke:
        return DPS_SMOKE
    return DPS_LO if float(ell) <= L_DPS40 + 1.0e-12 else DPS_HI


def expand_and_bisect(
    assembler: GmpyAssembler,
    skip: int,
    n_events: int,
    ell_q: float,
    ns: list[int],
    tol: float,
    s_q: float,
) -> dict:
    """Shared-L PSD bisection for all N and both definitions."""
    lo0 = float(ell_q)
    keys = []
    for dim in ns:
        keys.append(("D1", int(dim)))
        keys.append(("D2", int(dim)))
    signs: dict[tuple[str, int], dict[float, bool]] = {key: {} for key in keys}

    def eval_at(length: float) -> None:
        loc = round(float(length), 12)
        assembler.assemble(loc)
        for defn, dim in keys:
            if loc in signs[(defn, dim)]:
                continue
            indices = (
                d1_indices(n_events, skip) if defn == "D1" else d2_indices(skip)
            )
            quad = assembler.quadratic(loc, dim, indices)
            signs[(defn, dim)][loc] = psd_q(quad, dim, assembler.dps)

    span = min(max(SEARCH_PAD, 1.2 * max(float(s_q), 0.02)), 0.16)
    probes = [lo0 + float(off) for off in COARSE_OFFSETS if off <= span + 1.0e-15]
    if probes[-1] < lo0 + span:
        probes.append(lo0 + span)
    for length in probes:
        eval_at(length)

    brackets = {}
    for key in keys:
        ordered = sorted(signs[key].items())
        prev_l, prev_p = ordered[0]
        if not prev_p:
            brackets[key] = (lo0, lo0, True)
            continue
        found = False
        for loc, pos in ordered[1:]:
            if prev_p and (not pos):
                brackets[key] = (prev_l, loc, True)
                found = True
                break
            prev_l, prev_p = loc, pos
        if found:
            continue
        extra = ordered[-1][0]
        last_pos = prev_p
        while extra < lo0 + 0.22:
            extra = min(extra + 0.04, lo0 + 0.22)
            eval_at(extra)
            pos = signs[key][round(extra, 12)]
            if last_pos and (not pos):
                brackets[key] = (prev_l, extra, True)
                found = True
                break
            prev_l, last_pos = extra, pos
            if extra >= lo0 + 0.22 - 1.0e-15:
                break
        if not found:
            brackets[key] = (float("inf"), float("inf"), False)

    pending = [
        key for key, (lo_b, hi_b, finite) in brackets.items()
        if finite and hi_b > lo_b + tol
    ]
    while pending:
        mids = []
        for key in pending:
            lo_b, hi_b, _finite = brackets[key]
            mids.append(0.5 * (lo_b + hi_b))
        mid = 0.5 * (min(mids) + max(mids))
        # if the open brackets have spread mids, evaluate each unique mid
        unique = []
        for val in sorted(mids):
            if not unique or abs(val - unique[-1]) > 0.25 * tol:
                unique.append(val)
        if len(unique) > 4:
            unique = [mid]
        for loc in unique:
            eval_at(loc)
        nxt = []
        for key in pending:
            lo_b, hi_b, finite = brackets[key]
            if not finite or hi_b - lo_b <= tol:
                continue
            probe = unique[0]
            if len(unique) > 1:
                probe = min(unique, key=lambda val, a=lo_b, b=hi_b: abs(val - 0.5 * (a + b)))
            probe = round(probe, 12)
            if probe <= lo_b or probe >= hi_b:
                probe = round(0.5 * (lo_b + hi_b), 12)
                eval_at(probe)
            pos = signs[key][probe]
            if pos:
                lo_b = probe
            else:
                hi_b = probe
            brackets[key] = (lo_b, hi_b, True)
            if hi_b - lo_b > tol:
                nxt.append(key)
        pending = nxt

    out = {}
    for defn, dim in keys:
        lo_b, hi_b, finite = brackets[(defn, dim)]
        if not finite:
            out[(defn, dim)] = float("inf")
        else:
            out[(defn, dim)] = 0.5 * (lo_b + hi_b) - lo0
    return out


def p4_row(
    assembler: GmpyAssembler,
    skip: int,
    n_events: int,
    ell_q: float,
    logqs: np.ndarray,
    dim: int,
) -> dict:
    dim = min(int(dim), assembler.n_max)
    h_fd = H_FD

    def pencil(length, indices):
        packed = assembler.assemble(length)
        quad = assembler.quadratic(length, dim, indices)
        gram = mat_copy_n(packed["gram"], dim)
        return lam_min_shift(quad, gram, dim, assembler.dps)

    lam_star = pencil(ell_q, true_indices(ell_q, logqs))
    lam_pred0 = pencil(ell_q, d2_indices(skip))
    lam_pred1 = pencil(ell_q + h_fd, d2_indices(skip))
    lam_pred2 = pencil(ell_q + 2.0 * h_fd, d2_indices(skip))
    lam_true1 = pencil(ell_q + h_fd, true_indices(ell_q + h_fd, logqs))
    r_q = float("nan")
    if math.isfinite(lam_pred1) and math.isfinite(lam_pred0):
        r_q = -(lam_pred1 - lam_pred0) / h_fd
    r_q2 = float("nan")
    if math.isfinite(lam_pred2) and math.isfinite(lam_pred1):
        r_q2 = -(lam_pred2 - lam_pred1) / h_fd
    c_log = float("nan")
    if (
        math.isfinite(lam_star) and math.isfinite(lam_true1)
        and lam_star > 0.0 and lam_true1 > 0.0
    ):
        c_log = (math.log(lam_true1) - math.log(lam_star)) / h_fd
    return {
        "lam_star": lam_star,
        "lam_pred0": lam_pred0,
        "lam_pred1": lam_pred1,
        "lam_pred2": lam_pred2,
        "lam_true1": lam_true1,
        "r_q": r_q,
        "r_q2": r_q2,
        "c_log": c_log,
        "n_p4": dim,
    }


def decide(rows: list[dict], smoke: bool) -> tuple[str, str]:
    primary = []
    small = []
    large = []
    for rec in rows:
        delta = rec["delta_d2_damped"]
        conv = bool(rec["conv_d2_damped"])
        ell = float(rec["L"])
        if conv and math.isfinite(delta):
            primary.append(delta)
            if ell <= 1.0 + 1.0e-12:
                small.append(rec)
            else:
                large.append(rec)
        elif ell <= 1.0 + 1.0e-12:
            small.append(rec)

    small_events = [rec for rec in rows if rec["L"] <= 1.0 + 1.0e-12]
    small_pos = [
        rec for rec in small_events
        if rec["conv_d2_damped"] and rec["delta_d2_damped"] > 2.0 * LEAD_TOL_FULL
    ]
    small_drift = False
    for rec in small_events:
        d80 = rec["delta_d2_damped_80"]
        d120 = rec["delta_d2_damped_120"]
        if (
            math.isfinite(d80) and math.isfinite(d120)
            and d80 > 2.0 * LEAD_TOL_FULL and d120 > 2.0 * LEAD_TOL_FULL
            and abs(d120 - d80) >= CONV_ABS
        ):
            small_drift = True
        d160 = rec.get("delta_d2_damped_160")
        if (
            d160 is not None and math.isfinite(d160) and math.isfinite(d120)
            and d160 > 2.0 * LEAD_TOL_FULL and d120 > 2.0 * LEAD_TOL_FULL
            and abs(d160 - d120) >= CONV_ABS
        ):
            small_drift = True

    if small_drift:
        return (
            "LEAD_N_ARTIFACT",
            "L_q<=1 leads drift with N; Delta~0.015 withdrawn as basis artifact",
        )

    spacing_rows = [
        rec for rec in rows
        if rec["q"] >= SPACING_QMIN and rec["conv_d2_damped"]
        and math.isfinite(rec["delta_d2_damped"]) and rec["s"] > 0.0
    ]
    if spacing_rows and all(
        abs(rec["delta_d2_damped"] / rec["s"] - 1.0) <= SPACING_REL
        for rec in spacing_rows
    ):
        n_big = sum(1 for rec in rows if rec["q"] >= SPACING_QMIN)
        if len(spacing_rows) >= max(3, n_big - 2) or smoke:
            return (
                "LEAD_SPACING_LIMITED",
                "q>=8 converged Delta tracks s_q within 20 percent",
            )

    n_conv = sum(1 for rec in rows if rec["conv_d2_damped"])
    n_small = len(small_events)
    n_small_conv = sum(1 for rec in small_events if rec["conv_d2_damped"])
    if n_conv < len(rows):
        if n_small_conv == n_small and n_small > 0:
            return (
                "LEAD_PARTIAL",
                "converged only for L_q<=1 (%d/%d events)" % (n_conv, len(rows)),
            )
        if small_pos:
            return (
                "LEAD_PARTIAL",
                "positive N-stable leads only at small L_q (%d/%d events; "
                "later events already indefinite at entry)"
                % (n_conv, len(rows)),
            )
        return (
            "LEAD_PARTIAL",
            "converged %d/%d events" % (n_conv, len(rows)),
        )

    if len(primary) >= 2:
        spread = max(primary) - min(primary)
        if spread < BAND_WIDTH:
            return (
                "LEAD_CONVERGED_CONSTANT",
                "all converged D2-damped leads in a band of width %s < 0.005"
                % fmt(spread, 4),
            )
        return (
            "LEAD_CONVERGED_VARYING",
            "converged D2-damped spread %s >= 0.005; structure vs q in table"
            % fmt(spread, 4),
        )
    return ("LEAD_PARTIAL", "too few converged leads")


def finalize_rec(rec: dict, ns: list[int], smoke: bool) -> dict:
    d2d = rec["deltas"]["damped"]["D2"]
    d80 = d2d.get("80", d2d.get(str(max(ns))))
    d120 = d2d.get("120", float("nan"))
    d160 = d2d.get("160", float("nan"))
    d40 = d2d.get("40", float("nan"))
    rec["delta_d2_damped"] = float(
        d120 if (d120 is not None and math.isfinite(float(d120)))
        else (d80 if d80 is not None else float("nan"))
    )
    rec["delta_d2_damped_80"] = float(d80) if d80 is not None else float("nan")
    rec["delta_d2_damped_120"] = (
        float(d120) if d120 is not None else float("nan")
    )
    rec["delta_d2_damped_160"] = (
        float(d160) if d160 is not None else float("nan")
    )
    rec["delta_d2_damped_40"] = float(d40) if d40 is not None else float("nan")
    conv80_120 = True
    if "80" in d2d and "120" in d2d:
        a_val, b_val = float(d2d["80"]), float(d2d["120"])
        conv80_120 = (
            math.isfinite(a_val) and math.isfinite(b_val)
            and abs(b_val - a_val) < CONV_ABS
        )
    elif smoke and "40" in d2d and "80" in d2d:
        a_val, b_val = float(d2d["40"]), float(d2d["80"])
        conv80_120 = (
            math.isfinite(a_val) and math.isfinite(b_val)
            and abs(b_val - a_val) < CONV_ABS
        )
    conv160 = True
    if "160" in d2d and "120" in d2d:
        a_val, b_val = float(d2d["120"]), float(d2d["160"])
        conv160 = (
            math.isfinite(a_val) and math.isfinite(b_val)
            and abs(b_val - a_val) < CONV_ABS
        )
    rec["conv_d2_damped"] = bool(
        conv80_120 and conv160
        and math.isfinite(rec["delta_d2_damped"])
        and rec["delta_d2_damped"] > 2.0 * LEAD_TOL_FULL
    )
    rec["n_conv_ok"] = rec["conv_d2_damped"]
    rec["delta_d1_damped"] = float(
        rec["deltas"]["damped"]["D1"].get(
            "120", rec["deltas"]["damped"]["D1"].get("80", float("nan")),
        )
    )
    s_q = float(rec["s"])
    rec["ratio"] = (
        rec["delta_d2_damped"] / s_q
        if s_q > 0.0 and math.isfinite(rec["delta_d2_damped"])
        else float("nan")
    )
    rec["lam_star"] = float(rec["p4"].get("lam_star", float("nan")))
    rec["r_q"] = float(rec["p4"].get("r_q", float("nan")))
    rec["c_log"] = float(rec["p4"].get("c_log", float("nan")))
    return rec


def scan_event(task: dict) -> dict:
    logqs = np.asarray(task["logqs"], dtype=np.float64)
    weights = np.asarray(task["weights"], dtype=np.float64)
    index = int(task["index"])
    q_val = int(task["q"])
    ell_q = float(task["L"])
    s_q = float(task["s"])
    dps = int(task["dps"])
    ns = [int(val) for val in task["ns"]]
    n_events = int(task["n_events"])
    smoke = bool(task["smoke"])
    bases = tuple((str(name), int(power)) for name, power in task["bases"])
    n_max = max(ns)
    n_outer = int(task["n_outer"])
    tol = float(task["tol"])
    lam_q = float(task["Lambda"])
    w_q = float(task["w"])
    rec = {
        "j": index + 1,
        "q": q_val,
        "L": ell_q,
        "s": s_q,
        "dps": dps,
        "Lambda": lam_q,
        "w": w_q,
        "deltas": {},
    }
    p4 = None
    for bname, power in bases:
        assembler = GmpyAssembler(
            n_max, power, dps, n_outer, logqs, weights,
        )
        deltas = expand_and_bisect(
            assembler, index, n_events, ell_q, ns, tol, s_q,
        )
        rec["deltas"][bname] = {
            "D1": {str(dim): deltas[("D1", dim)] for dim in ns},
            "D2": {str(dim): deltas[("D2", dim)] for dim in ns},
        }
        if bname == "damped" and p4 is None:
            p4 = p4_row(
                assembler, index, n_events, ell_q, logqs,
                min(N_P4, n_max),
            )
    rec["p4"] = p4 or {}
    return finalize_rec(rec, ns, smoke)


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    _GL_GMPY.clear()
    _CL_GMPY.clear()
    wall0 = time.time()

    q_max = Q_MAX_SMOKE if smoke else Q_MAX_FULL
    qs, logqs, weights, ells, q_next, lam_tab = R619.prime_powers_upto(q_max)
    n_events = len(qs)
    ells_ext = np.concatenate(
        [ells, np.array([0.5 * math.log(q_next)], dtype=np.float64)]
    )
    spacings = [
        float(ells_ext[index + 1] - ells_ext[index]) for index in range(n_events)
    ]
    bases = (("damped", DAMP_POWER),) if smoke else (
        ("damped", DAMP_POWER), ("plain", 0),
    )
    tol = LEAD_TOL_SMOKE if smoke else LEAD_TOL_FULL

    section("r635  PRIME.RELAY.LEAD.PRECISION.01")
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("FENCE %s" % FENCE)
    emit("q_max %d  n_events %d  q_next %d  smoke=%d" % (
        q_max, n_events, q_next, int(smoke),
    ))
    emit("events %s" % ",".join(str(q_val) for q_val in qs))

    ok_d2, d2_detail = r619_predecessor_is_d2()
    check("G01-r619-predecessor-D2", ok_d2, d2_detail)
    check(
        "G02-import-SPEC",
        R619.SPEC_SHA.startswith(R619_SHA_PREFIX)
        and R628.SPEC_SHA.startswith(R628_SHA_PREFIX)
        and R630.SPEC_SHA.startswith(R630_SHA_PREFIX)
        and R623.SPEC_SHA.startswith(R623_SHA_PREFIX),
        "r619 %s r628 %s r630 %s r623 %s"
        % (
            R619.SPEC_SHA[:8], R628.SPEC_SHA[:8],
            R630.SPEC_SHA[:8], R623.SPEC_SHA[:8],
        ),
    )
    check(
        "G03-events-Lambda",
        n_events >= (3 if smoke else 18) and all(lam_tab[q_val] > 0.0 for q_val in qs),
        "n=%d" % n_events,
    )
    s31 = 0.5 * math.log(32.0 / 31.0) if (not smoke and 31 in qs) else float("nan")
    check(
        "G04-s31",
        smoke or abs(s31 - 0.0159) < 0.001,
        "s(31->32)=%s" % fmt(s31, 4),
    )

    tasks = []
    for index, q_val in enumerate(qs):
        ell_q = float(ells[index])
        dps = dps_for_lq(ell_q, smoke)
        ns = n_list_for(q_val, smoke)
        tasks.append({
            "index": index,
            "q": int(q_val),
            "L": ell_q,
            "s": float(spacings[index]),
            "dps": dps,
            "ns": ns,
            "n_events": n_events,
            "smoke": bool(smoke),
            "bases": bases,
            "n_outer": (
                N_OUTER_SMOKE if smoke else (
                    N_OUTER_HI if dps >= DPS_HI else N_OUTER_LO
                )
            ),
            "tol": tol,
            "Lambda": float(lam_tab[int(q_val)]),
            "w": float(weights[index]),
            "logqs": logqs.tolist(),
            "weights": weights.tolist(),
        })
    rows = []
    workers = 1 if smoke else min(8, max(1, n_events), os.cpu_count() or 4)
    emit("scan workers=%d" % workers)
    if workers == 1:
        for task in tasks:
            rec = scan_event(task)
            rows.append(rec)
            for bname, _power in bases:
                d2 = rec["deltas"][bname]["D2"]
                emit(
                    "  q=%d %s D2 N-sweep %s"
                    % (
                        rec["q"], bname,
                        " ".join(
                            "N%s=%s" % (
                                dim,
                                (
                                    ">inf"
                                    if not math.isfinite(float(val))
                                    else fmt(float(val), 4)
                                ),
                            )
                            for dim, val in d2.items()
                        ),
                    )
                )
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(scan_event, task): task["index"] for task in tasks}
            by_index = {}
            for fut in as_completed(futures):
                rec = fut.result()
                by_index[int(rec["j"]) - 1] = rec
        rows = [by_index[index] for index in range(n_events)]
        for rec in rows:
            for bname, _power in bases:
                d2 = rec["deltas"][bname]["D2"]
                emit(
                    "  q=%d %s D2 N-sweep %s"
                    % (
                        rec["q"], bname,
                        " ".join(
                            "N%s=%s" % (
                                dim,
                                (
                                    ">inf"
                                    if not math.isfinite(float(val))
                                    else fmt(float(val), 4)
                                ),
                            )
                            for dim, val in d2.items()
                        ),
                    )
                )

    section("P1  DEFINITIONS")
    emit("  r619 used D2 frozen predecessor (drop=1, n_keep=j_ev-1).")
    emit("  D1 = true minus q (later events enter); D2 = frozen q'<q.")
    d1_eq = True
    for rec in rows:
        d1 = rec["delta_d1_damped"]
        d2 = rec["delta_d2_damped"]
        if math.isfinite(d1) and math.isfinite(d2) and d2 < rec["s"] - 2.0 * tol:
            if abs(d1 - d2) > 4.0 * tol:
                d1_eq = False
    check(
        "G05-D1-eq-D2-before-next",
        d1_eq,
        "D1=D2 when crossing is before next entry (2L filter)",
    )

    section("P2  DELTA vs N  (D2 damped primary)")
    emit(
        "  q   L_q     s_q    D2N80    D2N120   D2N160   conv  D1N120  D1/s"
    )
    for rec in rows:
        emit(
            "  %2d %s %s %s %s %s  %d   %s %s"
            % (
                rec["q"], fmt(rec["L"], 4), fmt(rec["s"], 4),
                fmt(rec["delta_d2_damped_80"], 4),
                fmt(rec["delta_d2_damped_120"], 4),
                fmt(rec["delta_d2_damped_160"], 4),
                int(rec["conv_d2_damped"]),
                fmt(rec["delta_d1_damped"], 4),
                fmt(rec["ratio"], 3),
            )
        )

    section("P3  SPACING NULL  Delta/s_q  (D2 damped)")
    n_space = 0
    n_space_hit = 0
    for rec in rows:
        hit = (
            rec["q"] >= SPACING_QMIN
            and math.isfinite(rec["ratio"])
            and abs(rec["ratio"] - 1.0) <= SPACING_REL
        )
        if rec["q"] >= SPACING_QMIN:
            n_space += 1
            n_space_hit += int(hit)
        emit(
            "  q=%d Delta/s=%s  spacing_limited=%d"
            % (rec["q"], fmt(rec["ratio"], 4), int(hit))
        )
    check("G06-spacing-reported", True, "n_q>=8 %d hit %d" % (n_space, n_space_hit))

    section("P4  MARGIN AND RATE")
    emit("  q   lam*(L_q)           r_q                 c(L_q)")
    n_p4_ok = 0
    for rec in rows:
        ok_p4 = math.isfinite(rec["lam_star"]) or math.isfinite(rec["r_q"])
        n_p4_ok += int(ok_p4)
        emit(
            "  %2d %s %s %s"
            % (
                rec["q"], fmt(rec["lam_star"], 6),
                fmt(rec["r_q"], 6), fmt(rec["c_log"], 4),
            )
        )
    check("G07-P4-rows", n_p4_ok == len(rows), "%d/%d" % (n_p4_ok, len(rows)))

    verdict, why = decide(rows, smoke)
    check("G08-verdict-enum", verdict in DECISIONS, verdict)
    check("G09-fence", FENCE in SPEC["fence"], FENCE)
    check(
        "G10-no-zeros",
        "no_zero_table" in SPEC and SPEC["no_zero_table"] is True,
        "prime-side forms only",
    )

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "verdict": verdict,
        "why": why,
        "r619_predecessor": "D2_frozen_predecessor",
        "smoke": bool(smoke),
        "events": [
            {
                "q": rec["q"],
                "L": round_or_none(rec["L"], 10),
                "s": round_or_none(rec["s"], 10),
                "dps": rec["dps"],
                "w": round_or_none(rec["w"], 10),
                "Lambda": round_or_none(rec["Lambda"], 10),
                "conv_d2_damped": bool(rec["conv_d2_damped"]),
                "delta_d2_damped": round_or_none(rec["delta_d2_damped"], 6),
                "delta_d1_damped": round_or_none(rec["delta_d1_damped"], 6),
                "delta_d2_N": {
                    str(n_dim): round_or_none(val, 6)
                    for n_dim, val in rec["deltas"]["damped"]["D2"].items()
                },
                "delta_d1_N": {
                    str(n_dim): round_or_none(val, 6)
                    for n_dim, val in rec["deltas"]["damped"]["D1"].items()
                },
                "delta_d2_plain": (
                    {
                        str(n_dim): round_or_none(val, 6)
                        for n_dim, val in rec["deltas"]["plain"]["D2"].items()
                    }
                    if "plain" in rec["deltas"] else {}
                ),
                "ratio": round_or_none(rec["ratio"], 6),
                "lam_star": rec["lam_star"] if math.isfinite(rec["lam_star"]) else None,
                "r_q": rec["r_q"] if math.isfinite(rec["r_q"]) else None,
                "r_q2": rec["p4"].get("r_q2"),
                "c_log": rec["c_log"] if math.isfinite(rec["c_log"]) else None,
                "lam_pred0": rec["p4"].get("lam_pred0"),
                "lam_pred1": rec["p4"].get("lam_pred1"),
                "lam_pred2": rec["p4"].get("lam_pred2"),
            }
            for rec in rows
        ],
    }
    result = payload_sha(payload)
    payload["result_sha"] = result
    payload["spec_sha"] = SPEC_SHA
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    RESULT_PATH.write_text(text + "\n", encoding="utf-8")
    check("G11-json-written", RESULT_PATH.is_file(), str(RESULT_PATH.name))

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    wall = time.time() - wall0

    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % result)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("FENCE %s" % FENCE)

    section("STATE")
    emit("round r%d contract %s" % (ROUND, CONTRACT))
    emit("FILE_SHA256 %s" % file_sha256())
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("RESULT_SHA %s" % result)
    emit("GATES %d/%d smoke=%d wall_s=%s" % (n_pass, n_gate, int(smoke), fmt(wall, 3)))
    emit("P1 r619 predecessor = D2 frozen (drop=1); D1 true-minus-q also reported")
    emit("table q L s D2N80 D2N120 D2N160 conv D1N120 D/s lam* r_q")
    for rec in rows:
        emit(
            "  %d %s %s %s %s %s %d %s %s %s %s"
            % (
                rec["q"], fmt(rec["L"], 4), fmt(rec["s"], 4),
                fmt(rec["delta_d2_damped_80"], 4),
                fmt(rec["delta_d2_damped_120"], 4),
                fmt(rec["delta_d2_damped_160"], 4),
                int(rec["conv_d2_damped"]),
                fmt(rec["delta_d1_damped"], 4),
                fmt(rec["ratio"], 3),
                fmt(rec["lam_star"], 3),
                fmt(rec["r_q"], 3),
            )
        )
    emit("DECISION %s" % verdict)
    emit("WHY %s" % why)
    emit("FENCE %s" % FENCE)
    emit("END_STATE")
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r635 relay-lead precision (experiments only; no RH claim)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
