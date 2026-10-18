#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_inequality_evosearch_probe -- r603

Round 603.  Experiments-only genetic-programming search for
inequalities on prime von-Mangoldt data, with a built-in
two-key filter.

  An inequality L(X) ≤ R(X) is a SURVIVOR only if
    (i)  it holds on true primes for every X in the train AND
         holdout grids,
    (ii) it is violated on density-preserving scrambled primes
         for every scramble seed (key 1: uses prime LOCATIONS,
         not mere density — Beurling / Diamond–Montgomery–
         Vorhauer logic),
    (iii) it is violated in a world with an artificial off-line
         zero (key 2: RH-sensitive in the intended direction).

  Anything that holds in every world is a density/trivial
  statement and is discarded.  A SURVIVOR is a HYPOTHESIS
  (a proof assignment), not a result.

CLAIM BOUNDARY.  Finite deterministic arithmetic on n ≤ 10^6.
NO RH claim, NO anti-RH claim, NO ledger/paper/Lean/next.txt
edit.  Grammar constants are a frozen finite set — no fitted
free constants.

Verdicts:
  SURVIVORS_FOUND(n) | ONLY_ONE_KEY(n) | NO_SURVIVOR
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

import numpy as np  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA hashes grammar + grids + seeds.
# ---------------------------------------------------------------------------
ROUND = 603
X_MAX = 10 ** 6
SEED = 20260902
POP = 300
GENS = 60
TOURNAMENT_K = 5
CX_P = 0.6
MUT_P = 0.3
ELITE = 10
MAX_DEPTH = 5
MAX_SIZE = 25
TEMPLATE_FRAC = 0.45
SLACK_EPS = 1e-9
DIV_EPS = 1e-12
LOOSE_THR = 0.5
LOOSE_PEN = 0.5
SIZE_PEN = 0.02
PROFILE_CAP = 15
H_EXP = 0.6
SCRAMBLE_SEEDS = (SEED, SEED + 1, SEED + 2)
OFF_WORLDS = ((0.75, 30.0), (0.6, 120.0))
S_LIST = (0.0, 0.5, 1.0)
S_NAMES = ("0", "1/2", "1")
T_LIST = (0.0, 1.0, 2.0, 5.0, 10.0, 14.134725, 21.022040, 50.0)
T_NAMES = ("0", "1", "2", "5", "10", "14.134725", "21.022040", "50")
A_LIST = (0.5, 1.0, 2.0)
A_NAMES = ("0.5", "1", "2")
OMEGA_LIST = (0.0, 10.0, 14.134725, 21.022040, 50.0)
OMEGA_NAMES = ("0", "10", "14.134725", "21.022040", "50")
UNOPS = ("abs", "sqrtabs", "log1pabs")
BINOPS = ("add", "sub", "mul", "div", "max", "min")
COMM_OPS = ("add", "mul", "max", "min")
CONST_PAIRS = (("1", 1.0), ("2", 2.0), ("1/2", 0.5), ("pi", math.pi), ("e", math.e))
SANITY_X = (10 ** 4, 10 ** 5, 10 ** 6)


def log_grid(lo: int, hi: int, n: int, cap: int) -> tuple[int, ...]:
    out: list[int] = []
    for i in range(n):
        t = i / float(n - 1)
        x = lo * math.exp(t * math.log(hi / float(lo)))
        out.append(int(min(cap, max(2, round(x)))))
    return tuple(out)


TRAIN_X = log_grid(2 * 10 ** 3, 3 * 10 ** 5, 20, X_MAX)
HOLDOUT_X = log_grid(3 * 10 ** 5, 10 ** 6, 10, X_MAX)
PROFILE_X = log_grid(2 * 10 ** 3, 10 ** 6, 6, X_MAX)


def _all_x() -> tuple[int, ...]:
    seen = set()
    ordered: list[int] = []
    for x in TRAIN_X + HOLDOUT_X + PROFILE_X + SANITY_X:
        if x not in seen:
            seen.add(x)
            ordered.append(int(x))
    ordered.sort()
    return tuple(ordered)


ALL_X = _all_x()


def _term_catalog() -> tuple[list[str], list[tuple[str, object]]]:
    names: list[str] = []
    meta: list[tuple[str, object]] = []
    for s_name, s_val in zip(S_NAMES, S_LIST):
        for t_name, t_val in zip(T_NAMES, T_LIST):
            names.append("Sc(%s,%s)" % (s_name, t_name))
            meta.append(("Sc", (s_val, t_val)))
            names.append("Ss(%s,%s)" % (s_name, t_name))
            meta.append(("Ss", (s_val, t_val)))
    for a_name, a_val in zip(A_NAMES, A_LIST):
        for w_name, w_val in zip(OMEGA_NAMES, OMEGA_LIST):
            names.append("G(%s,%s)" % (a_name, w_name))
            meta.append(("G", (a_val, w_val)))
    for name in ("PSI", "PSIERR", "X", "sqrtX", "logX", "loglogX"):
        names.append(name)
        meta.append((name, None))
    for name, val in CONST_PAIRS:
        names.append(name)
        meta.append(("const", val))
    return names, meta


TERM_NAMES, TERM_META = _term_catalog()
TERM_INDEX = {name: i for i, name in enumerate(TERM_NAMES)}
N_TERMS = len(TERM_NAMES)

SENSITIVE_NAMES = []
SCALE_NAMES = []
CONST_NAMES = [p[0] for p in CONST_PAIRS]
for i, (name, meta) in enumerate(zip(TERM_NAMES, TERM_META)):
    kind = meta[0]
    if name in CONST_NAMES:
        continue
    if name in ("X", "sqrtX", "logX", "loglogX", "PSI"):
        SCALE_NAMES.append(name)
        continue
    if kind == "Sc":
        _s, t_val = meta[1]
        if t_val == 0.0:
            SCALE_NAMES.append(name)
        else:
            SENSITIVE_NAMES.append(name)
        continue
    if kind == "Ss":
        SENSITIVE_NAMES.append(name)
        continue
    if kind == "G":
        _a, w_val = meta[1]
        if w_val == 0.0:
            SCALE_NAMES.append(name)
        else:
            SENSITIVE_NAMES.append(name)
        continue
    if name == "PSIERR":
        SENSITIVE_NAMES.append(name)

SENSITIVE_IDX = tuple(TERM_INDEX[n] for n in SENSITIVE_NAMES)
SCALE_IDX = tuple(TERM_INDEX[n] for n in SCALE_NAMES)
CONST_IDX = tuple(TERM_INDEX[n] for n in CONST_NAMES)
RHS_IDX = SCALE_IDX + CONST_IDX

WORLD_NAMES = (
    "W_TRUE",
    "W_SCR0",
    "W_SCR1",
    "W_SCR2",
    "W_OFF075_30",
    "W_OFF06_120",
)
W_TRUE = 0
SCR_IDX = (1, 2, 3)
OFF_IDX = (4, 5)
N_WORLDS = 6

SPEC = {
    "round": ROUND,
    "contract": "PRIME.INEQUALITY.EVOSEARCH.01",
    "claim_boundary": "hypothesis_generator; no RH claim",
    "X_max": X_MAX,
    "grammar": {
        "unops": list(UNOPS),
        "binops": list(BINOPS),
        "max_depth": MAX_DEPTH,
        "max_size": MAX_SIZE,
        "terminals": list(TERM_NAMES),
        "constants": [p[0] for p in CONST_PAIRS],
        "no_free_fit": True,
    },
    "grid": {
        "train": list(TRAIN_X),
        "holdout": list(HOLDOUT_X),
        "profile": list(PROFILE_X),
        "sanity": list(SANITY_X),
    },
    "seeds": {
        "gp": SEED,
        "scramble": list(SCRAMBLE_SEEDS),
    },
    "gp": {
        "pop": POP,
        "gens": GENS,
        "tournament_k": TOURNAMENT_K,
        "cx": CX_P,
        "mut": MUT_P,
        "elite": ELITE,
        "template_frac": TEMPLATE_FRAC,
    },
    "scramble": {
        "H": "p^%.1f" % H_EXP,
        "U": "uniform[-1/2,1/2]",
        "collision": "nearest_free_forward_then_back",
    },
    "off": [{"beta": b, "gamma": g} for b, g in OFF_WORLDS],
    "fitness": {
        "slack_eps": SLACK_EPS,
        "size_pen": SIZE_PEN,
        "loose_thr": LOOSE_THR,
        "loose_pen": LOOSE_PEN,
        "keys_on": "train",
        "profile_cap": PROFILE_CAP,
    },
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
        flush=True,
    )
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(rows: object) -> str:
    blob = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def fmt(x: float, digits: int = 10) -> str:
    v = float(x)
    if not math.isfinite(v):
        if math.isnan(v):
            return "nan"
        return "inf" if v > 0.0 else "-inf"
    return "%+.*e" % (digits, v)


def canon_float(x: float) -> float:
    v = float(x)
    if not math.isfinite(v):
        return v
    return float("%.12e" % v)


# ---------------------------------------------------------------------------
# Sieve, scramble, off-line worlds
# ---------------------------------------------------------------------------
def sieve_von_mangoldt(xmax: int) -> tuple[np.ndarray, np.ndarray]:
    lam = np.zeros(xmax + 1, dtype=np.float64)
    is_prime = np.ones(xmax + 1, dtype=bool)
    is_prime[:2] = False
    primes: list[int] = []
    for p in range(2, xmax + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        log_p = math.log(p)
        power = p
        while power <= xmax:
            lam[power] = log_p
            if power > xmax // p:
                break
            power *= p
        start = p * p
        if start <= xmax:
            is_prime[start : xmax + 1 : p] = False
    return lam, np.asarray(primes, dtype=np.int64)


def _nearest_free(occupied: np.ndarray, q0: int, xmax: int) -> int:
    q0 = int(min(max(q0, 2), xmax))
    if not occupied[q0]:
        return q0
    for delta in range(1, xmax + 1):
        qf = q0 + delta
        if qf <= xmax and not occupied[qf]:
            return int(qf)
        qb = q0 - delta
        if qb >= 2 and not occupied[qb]:
            return int(qb)
    return q0


def scramble_lambda(
    primes: np.ndarray, xmax: int, seed: int, exponent: float = H_EXP,
) -> np.ndarray:
    rng = np.random.RandomState(int(seed))
    n_p = int(primes.size)
    u_vals = rng.uniform(-0.5, 0.5, size=n_p)
    occupied = np.zeros(xmax + 1, dtype=bool)
    qs = np.empty(n_p, dtype=np.int64)
    for i in range(n_p):
        p = int(primes[i])
        shift = u_vals[i] * (p ** exponent)
        q = int(round(p + shift))
        q = _nearest_free(occupied, q, xmax)
        occupied[q] = True
        qs[i] = q
    lam = np.zeros(xmax + 1, dtype=np.float64)
    order = np.argsort(qs, kind="mergesort")
    for idx in order:
        q = int(qs[idx])
        if q < 2:
            continue
        log_q = math.log(q)
        lam[q] = log_q
        if q > xmax // q:
            continue
        power = q * q
        while power <= xmax:
            if lam[power] == 0.0:
                lam[power] = log_q
            if power > xmax // q:
                break
            power *= q
    return lam, int(occupied.sum())


def lambda_off(lam: np.ndarray, beta: float, gamma: float) -> np.ndarray:
    out = lam.copy()
    n = np.arange(lam.size, dtype=np.float64)
    sl = slice(2, None)
    logn = np.log(n[sl])
    cosg = np.cos(gamma * logn)
    term = 2.0 * (np.exp((beta - 1.0) * logn) + np.exp(-beta * logn)) * cosg
    out[sl] = lam[sl] - term
    out[0] = 0.0
    out[1] = 0.0
    return out


def dyadic_sums(lam: np.ndarray, xmax: int) -> list[tuple[int, int, float]]:
    rows: list[tuple[int, int, float]] = []
    lo = 2
    while lo <= xmax:
        hi = min(lo * 2, xmax + 1)
        total = float(lam[lo:hi].sum())
        rows.append((lo, hi - 1, total))
        lo *= 2
    return rows


def max_rel_dyadic(
    true_rows: list[tuple[int, int, float]],
    scr_rows: list[tuple[int, int, float]],
    min_lo: int = 1,
) -> tuple[float, int, int]:
    worst = 0.0
    worst_lo = 2
    worst_hi = 2
    found = False
    for (lo, hi, a), (_, _, b) in zip(true_rows, scr_rows):
        if lo < min_lo:
            continue
        den = max(abs(a), 1e-12)
        rel = abs(b - a) / den
        if (not found) or rel > worst:
            worst = rel
            worst_lo = lo
            worst_hi = hi
            found = True
    if not found:
        return 0.0, 0, 0
    return worst, worst_lo, worst_hi


# ---------------------------------------------------------------------------
# Terminal tables (prefix snapshots → O(1) lookup)
# ---------------------------------------------------------------------------
def _weights(xmax: int) -> dict[str, np.ndarray]:
    n = np.arange(xmax + 1, dtype=np.float64)
    n_safe = np.maximum(n, 1.0)
    logn = np.log(n_safe)
    logn[0] = 0.0
    ones = np.ones(xmax + 1, dtype=np.float64)
    ones[0] = 0.0
    inv_sqrt = 1.0 / np.sqrt(n_safe)
    inv_sqrt[0] = 0.0
    inv_n = 1.0 / n_safe
    inv_n[0] = 0.0
    pows = {0.0: ones, 0.5: inv_sqrt, 1.0: inv_n}
    cos_t = np.empty((len(T_LIST), xmax + 1), dtype=np.float64)
    sin_t = np.empty((len(T_LIST), xmax + 1), dtype=np.float64)
    for ti, t_val in enumerate(T_LIST):
        arg = t_val * logn
        cos_t[ti] = np.cos(arg)
        sin_t[ti] = np.sin(arg)
        cos_t[ti, 0] = 0.0
        sin_t[ti, 0] = 0.0
    gabor = np.empty((len(A_LIST), len(OMEGA_LIST), xmax + 1), dtype=np.float64)
    logn2 = logn * logn
    for ai, a_val in enumerate(A_LIST):
        gauss = np.exp(-0.5 * a_val * logn2)
        gauss[0] = 0.0
        for wi, w_val in enumerate(OMEGA_LIST):
            gabor[ai, wi] = inv_sqrt * gauss * np.cos(w_val * logn)
            gabor[ai, wi, 0] = 0.0
    return {"pows": pows, "cos_t": cos_t, "sin_t": sin_t, "gabor": gabor}


def used_term_ids(node: tuple) -> set[int]:
    if node[0] == "T":
        return {int(node[1])}
    if node[0] == "U":
        return used_term_ids(node[2])
    return used_term_ids(node[2]) | used_term_ids(node[3])


def remap_tree(node: tuple, mapping: dict[int, int]) -> tuple:
    if node[0] == "T":
        return ("T", mapping[node[1]])
    if node[0] == "U":
        return ("U", node[1], remap_tree(node[2], mapping))
    return (
        "B",
        node[1],
        remap_tree(node[2], mapping),
        remap_tree(node[3], mapping),
    )


def term_full_column(
    k: int, lam: np.ndarray, weights: dict[str, np.ndarray],
) -> np.ndarray:
    xmax = int(lam.size - 1)
    xs = np.arange(xmax + 1, dtype=np.float64)
    kind, payload = TERM_META[k]
    if kind == "Sc":
        s_val, t_val = payload
        ti = T_LIST.index(t_val)
        return np.cumsum(lam * weights["pows"][s_val] * weights["cos_t"][ti])
    if kind == "Ss":
        s_val, t_val = payload
        ti = T_LIST.index(t_val)
        return np.cumsum(lam * weights["pows"][s_val] * weights["sin_t"][ti])
    if kind == "G":
        a_val, w_val = payload
        ai = A_LIST.index(a_val)
        wi = OMEGA_LIST.index(w_val)
        return np.cumsum(lam * weights["gabor"][ai, wi])
    if kind == "PSI":
        return np.cumsum(lam)
    if kind == "PSIERR":
        return np.cumsum(lam) - xs
    if kind == "X":
        return xs
    if kind == "sqrtX":
        out = np.sqrt(np.maximum(xs, 0.0))
        out[0] = 0.0
        return out
    if kind == "logX":
        out = np.zeros_like(xs)
        out[1:] = np.log(np.maximum(xs[1:], 1.0))
        return out
    if kind == "loglogX":
        out = np.zeros_like(xs)
        out[3:] = np.log(np.log(xs[3:]))
        return out
    if kind == "const":
        return np.full(xmax + 1, float(payload), dtype=np.float64)
    raise RuntimeError("unknown terminal %s" % TERM_NAMES[k])


def dense_true_min(
    left: tuple,
    right: tuple,
    lam: np.ndarray,
    weights: dict[str, np.ndarray],
    n0: int,
    n1: int,
    col_cache: dict[int, np.ndarray] | None = None,
) -> tuple[float, int]:
    if col_cache is None:
        col_cache = {}
    ids = sorted(used_term_ids(left) | used_term_ids(right))
    mapping = {old: i for i, old in enumerate(ids)}
    block = np.empty((n1 - n0 + 1, len(ids)), dtype=np.float64)
    for old, i in mapping.items():
        if old not in col_cache:
            col_cache[old] = term_full_column(old, lam, weights)
        block[:, i] = col_cache[old][n0 : n1 + 1]
    with np.errstate(all="ignore"):
        lv = eval_tree(remap_tree(left, mapping), block)
        rv = eval_tree(remap_tree(right, mapping), block)
        sl = slack_arr(lv, rv)
    j = int(np.argmin(sl))
    return float(sl[j]), int(n0 + j)


def snapshot_world(
    lam: np.ndarray, xs: np.ndarray, weights: dict[str, np.ndarray],
) -> np.ndarray:
    xmax = int(lam.size - 1)
    table = np.zeros((len(xs), N_TERMS), dtype=np.float64)
    psi = np.cumsum(lam)
    x_idx = xs.astype(np.int64)
    pows = weights["pows"]
    cos_t = weights["cos_t"]
    sin_t = weights["sin_t"]
    gabor = weights["gabor"]
    for k, (name, meta) in enumerate(zip(TERM_NAMES, TERM_META)):
        kind = meta[0]
        if kind == "Sc":
            s_val, t_val = meta[1]
            ti = T_LIST.index(t_val)
            acc = np.cumsum(lam * pows[s_val] * cos_t[ti])
            table[:, k] = acc[x_idx]
        elif kind == "Ss":
            s_val, t_val = meta[1]
            ti = T_LIST.index(t_val)
            acc = np.cumsum(lam * pows[s_val] * sin_t[ti])
            table[:, k] = acc[x_idx]
        elif kind == "G":
            a_val, w_val = meta[1]
            ai = A_LIST.index(a_val)
            wi = OMEGA_LIST.index(w_val)
            acc = np.cumsum(lam * gabor[ai, wi])
            table[:, k] = acc[x_idx]
        elif kind == "PSI":
            table[:, k] = psi[x_idx]
        elif kind == "PSIERR":
            table[:, k] = psi[x_idx] - xs.astype(np.float64)
        elif kind == "X":
            table[:, k] = xs.astype(np.float64)
        elif kind == "sqrtX":
            table[:, k] = np.sqrt(xs.astype(np.float64))
        elif kind == "logX":
            table[:, k] = np.log(xs.astype(np.float64))
        elif kind == "loglogX":
            table[:, k] = np.log(np.log(xs.astype(np.float64)))
        elif kind == "const":
            table[:, k] = float(meta[1])
        else:
            raise RuntimeError("unknown terminal %s" % name)
    return table


def build_tables(
    worlds: list[np.ndarray], xs: np.ndarray, weights: dict[str, np.ndarray],
) -> np.ndarray:
    # tables[w, x, k]
    out = np.empty((len(worlds), xs.size, N_TERMS), dtype=np.float64)
    for w, lam in enumerate(worlds):
        out[w] = snapshot_world(lam, xs, weights)
    return out


# ---------------------------------------------------------------------------
# Expression trees
# ---------------------------------------------------------------------------
def depth_of(node: tuple) -> int:
    if node[0] == "T":
        return 0
    if node[0] == "U":
        return 1 + depth_of(node[2])
    return 1 + max(depth_of(node[2]), depth_of(node[3]))


def size_of(node: tuple) -> int:
    if node[0] == "T":
        return 1
    if node[0] == "U":
        return 1 + size_of(node[2])
    return 1 + size_of(node[2]) + size_of(node[3])


def _fmt_un(op: str, child: str) -> str:
    if op == "abs":
        return "abs(%s)" % child
    if op == "sqrtabs":
        return "sqrt(abs(%s))" % child
    return "log(1+abs(%s))" % child


def _fmt_bin(op: str, left: str, right: str) -> str:
    if op == "add":
        return "(%s+%s)" % (left, right)
    if op == "sub":
        return "(%s-%s)" % (left, right)
    if op == "mul":
        return "(%s*%s)" % (left, right)
    if op == "div":
        return "(%s/%s)" % (left, right)
    if op == "max":
        return "max(%s,%s)" % (left, right)
    return "min(%s,%s)" % (left, right)


def normalize(node: tuple) -> tuple[str, tuple]:
    if node[0] == "T":
        s = TERM_NAMES[node[1]]
        return s, ("T", node[1])
    if node[0] == "U":
        cs, ct = normalize(node[2])
        s = _fmt_un(node[1], cs)
        return s, ("U", node[1], ct)
    ls, lt = normalize(node[2])
    rs, rt = normalize(node[3])
    if node[1] in COMM_OPS and rs < ls:
        ls, rs, lt, rt = rs, ls, rt, lt
    s = _fmt_bin(node[1], ls, rs)
    return s, ("B", node[1], lt, rt)


def canon_tree(node: tuple) -> str:
    return normalize(node)[0]


def canon_pair(left: tuple, right: tuple) -> str:
    return "%s <= %s" % (canon_tree(left), canon_tree(right))


def eval_tree(node: tuple, block: np.ndarray) -> np.ndarray:
    # block: (n_worlds, n_x, n_terms) or (n_x, n_terms)
    if node[0] == "T":
        return block[..., node[1]]
    if node[0] == "U":
        child = eval_tree(node[2], block)
        op = node[1]
        if op == "abs":
            return np.abs(child)
        if op == "sqrtabs":
            return np.sqrt(np.abs(child))
        return np.log1p(np.abs(child))
    left = eval_tree(node[2], block)
    right = eval_tree(node[3], block)
    op = node[1]
    if op == "add":
        return left + right
    if op == "sub":
        return left - right
    if op == "mul":
        return left * right
    if op == "div":
        return np.where(np.abs(right) > DIV_EPS, left / right, 0.0)
    if op == "max":
        return np.maximum(left, right)
    return np.minimum(left, right)


def _rand_term(rng: random.Random, pool: tuple[int, ...] | None = None) -> tuple:
    if pool is None:
        return ("T", rng.randrange(N_TERMS))
    return ("T", pool[rng.randrange(len(pool))])


def random_tree(rng: random.Random, max_depth: int, method: str) -> tuple:
    if max_depth <= 0:
        return _rand_term(rng)
    grow_leaf = method == "grow" and rng.random() < 0.35
    if grow_leaf:
        return _rand_term(rng)
    if rng.random() < 0.35:
        return ("U", rng.choice(UNOPS), random_tree(rng, max_depth - 1, method))
    op = rng.choice(BINOPS)
    return (
        "B",
        op,
        random_tree(rng, max_depth - 1, method),
        random_tree(rng, max_depth - 1, method),
    )


def enforce(node: tuple, rng: random.Random) -> tuple:
    for _ in range(24):
        if size_of(node) <= MAX_SIZE and depth_of(node) <= MAX_DEPTH:
            return normalize(node)[1]
        node = random_tree(rng, min(3, MAX_DEPTH), "grow")
    return _rand_term(rng)


def template_pair(rng: random.Random) -> tuple[tuple, tuple]:
    kind = rng.randrange(4)
    t_idx = SENSITIVE_IDX[rng.randrange(len(SENSITIVE_IDX))]
    left: tuple
    if kind == 0:
        left = ("U", "abs", ("T", t_idx))
    elif kind == 1:
        left = ("T", t_idx)
    else:
        left = ("U", "abs", ("T", t_idx))
    n_fac = rng.randint(1, 3)
    right = _rand_term(rng, RHS_IDX)
    for _ in range(n_fac - 1):
        right = ("B", "mul", right, _rand_term(rng, RHS_IDX))
    if kind == 3:
        extra = ("U", "abs", _rand_term(rng, SENSITIVE_IDX))
        right = ("B", "add", extra, right)
    return enforce(left, rng), enforce(right, rng)


def random_pair(rng: random.Random) -> tuple[tuple, tuple]:
    if rng.random() < TEMPLATE_FRAC:
        return template_pair(rng)
    method_l = "full" if rng.random() < 0.5 else "grow"
    method_r = "full" if rng.random() < 0.5 else "grow"
    left = enforce(random_tree(rng, rng.randint(1, MAX_DEPTH), method_l), rng)
    right = enforce(random_tree(rng, rng.randint(1, MAX_DEPTH), method_r), rng)
    return left, right


def collect_nodes(node: tuple) -> list[tuple]:
    out = [node]
    if node[0] == "U":
        out.extend(collect_nodes(node[2]))
    elif node[0] == "B":
        out.extend(collect_nodes(node[2]))
        out.extend(collect_nodes(node[3]))
    return out


def replace_nth(node: tuple, target: int, new: tuple, counter: list[int]) -> tuple:
    if counter[0] == target:
        counter[0] += 1
        return new
    counter[0] += 1
    if node[0] == "T":
        return node
    if node[0] == "U":
        return ("U", node[1], replace_nth(node[2], target, new, counter))
    return (
        "B",
        node[1],
        replace_nth(node[2], target, new, counter),
        replace_nth(node[3], target, new, counter),
    )


def point_mutate(node: tuple, rng: random.Random) -> tuple:
    nodes = collect_nodes(node)
    k = rng.randrange(len(nodes))
    old = nodes[k]
    if old[0] == "T":
        new = _rand_term(rng)
    elif old[0] == "U":
        new = ("U", rng.choice(UNOPS), old[2])
    else:
        new = ("B", rng.choice(BINOPS), old[2], old[3])
    counter = [0]
    return enforce(replace_nth(node, k, new, counter), rng)


def subtree_mutate(node: tuple, rng: random.Random) -> tuple:
    nodes = collect_nodes(node)
    k = rng.randrange(len(nodes))
    new = random_tree(rng, rng.randint(0, 3), "grow")
    counter = [0]
    return enforce(replace_nth(node, k, new, counter), rng)


def crossover(a: tuple, b: tuple, rng: random.Random) -> tuple:
    na = collect_nodes(a)
    nb = collect_nodes(b)
    ia = rng.randrange(len(na))
    ib = rng.randrange(len(nb))
    counter = [0]
    return enforce(replace_nth(a, ia, nb[ib], counter), rng)


def mutate_pair(
    left: tuple, right: tuple, rng: random.Random,
) -> tuple[tuple, tuple]:
    side = rng.randrange(2)
    fn = point_mutate if rng.random() < 0.5 else subtree_mutate
    if side == 0:
        return fn(left, rng), right
    return left, fn(right, rng)


def crossover_pair(
    p1: tuple[tuple, tuple], p2: tuple[tuple, tuple], rng: random.Random,
) -> tuple[tuple, tuple]:
    side = rng.randrange(2)
    if side == 0:
        return crossover(p1[0], p2[0], rng), p1[1]
    return p1[0], crossover(p1[1], p2[1], rng)


# ---------------------------------------------------------------------------
# Fitness / class
# ---------------------------------------------------------------------------
def slack_arr(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    num = right - left
    den = np.abs(right) + np.abs(left) + SLACK_EPS
    out = num / den
    return np.where(np.isfinite(out), out, -1.0)


def classify(s_train: float, s_hold: float, key1: float, key2: float) -> str:
    if s_train < 0.0:
        return "INVALID"
    both = key1 == 1.0 and key2 == 1.0
    xor = (key1 == 1.0) != (key2 == 1.0)
    if both and s_hold >= 0.0:
        return "SURVIVOR"
    if xor:
        return "ONE_KEY"
    return "DENSITY"


def evaluate_pair(
    left: tuple,
    right: tuple,
    tables: np.ndarray,
    train_idx: np.ndarray,
    hold_idx: np.ndarray,
) -> dict:
    with np.errstate(all="ignore"):
        lv = eval_tree(left, tables)
        rv = eval_tree(right, tables)
        sl = slack_arr(lv, rv)
    s_train = float(np.min(sl[W_TRUE, train_idx]))
    if hold_idx.size:
        s_hold = float(np.min(sl[W_TRUE, hold_idx]))
    else:
        s_hold = s_train
    breaks1 = 0
    scr_mins: list[float] = []
    scr_at: list[int] = []
    for w in SCR_IDX:
        row = sl[w, train_idx]
        j = int(np.argmin(row))
        m = float(row[j])
        scr_mins.append(m)
        scr_at.append(int(j))
        if m < 0.0:
            breaks1 += 1
    key1 = breaks1 / float(len(SCR_IDX))
    breaks2 = 0
    off_mins: list[float] = []
    off_at: list[int] = []
    for w in OFF_IDX:
        row = sl[w, train_idx]
        j = int(np.argmin(row))
        m = float(row[j])
        off_mins.append(m)
        off_at.append(int(j))
        if m < 0.0:
            breaks2 += 1
    key2 = breaks2 / float(len(OFF_IDX))
    size = size_of(left) + size_of(right)
    if s_train < 0.0:
        fitness = s_train
    else:
        fitness = 1.0 + key1 + key2 - SIZE_PEN * size
        if s_train > LOOSE_THR:
            fitness -= LOOSE_PEN
    klass = classify(s_train, s_hold, key1, key2)
    expr = canon_pair(left, right)
    return {
        "expr": expr,
        "fitness": float(fitness),
        "s_train": float(s_train),
        "s_hold": float(s_hold),
        "key1": float(key1),
        "key2": float(key2),
        "size": int(size),
        "class": klass,
        "scr_mins": scr_mins,
        "off_mins": off_mins,
        "scr_at": scr_at,
        "off_at": off_at,
        "slack": sl,
        "left": left,
        "right": right,
    }


def seeded_battery(rng: random.Random) -> list[tuple[tuple, tuple]]:
    def T(name: str) -> tuple:
        return ("T", TERM_INDEX[name])

    raw = [
        (("U", "abs", T("PSIERR")),
         ("B", "mul", ("B", "mul", T("1/2"), T("sqrtX")), T("logX"))),
        (("U", "abs", T("G(1,14.134725)")),
         ("B", "mul", T("2"), T("logX"))),
        (("U", "abs", T("Sc(1/2,10)")), T("Sc(1/2,0)")),
        (("U", "abs", T("PSIERR")), T("sqrtX")),
        (("U", "abs", T("PSIERR")),
         ("B", "mul", T("sqrtX"), T("logX"))),
        (("U", "abs", T("PSIERR")),
         ("B", "mul", T("pi"), T("sqrtX"))),
        (("U", "abs", T("PSIERR")),
         ("B", "mul", T("e"), T("sqrtX"))),
        (("U", "abs", T("PSIERR")),
         ("B", "mul", ("B", "mul", T("1/2"), T("sqrtX")), T("loglogX"))),
        (("U", "abs", T("G(1,14.134725)")), T("logX")),
        (("U", "abs", T("G(0.5,14.134725)")),
         ("B", "mul", T("2"), T("logX"))),
        (("U", "abs", T("G(1,21.022040)")),
         ("B", "mul", T("2"), T("logX"))),
        (("U", "abs", T("Sc(1/2,14.134725)")), T("Sc(1/2,0)")),
        (("U", "abs", T("Ss(1/2,14.134725)")), T("Sc(1/2,0)")),
        (("U", "abs", T("PSIERR")),
         ("B", "mul", T("2"), T("sqrtX"))),
        (T("PSI"), ("B", "mul", T("2"), T("X"))),
        (T("PSIERR"), ("B", "mul", T("sqrtX"), T("logX"))),
        (("U", "abs", T("G(2,14.134725)")),
         ("B", "mul", T("2"), T("logX"))),
        (("U", "abs", T("Sc(0,14.134725)")),
         ("B", "mul", T("sqrtX"), T("logX"))),
    ]
    out = []
    for left, right in raw:
        out.append((enforce(left, rng), enforce(right, rng)))
    return out


# ---------------------------------------------------------------------------
# Controls (hard-wired, evaluated before GP)
# ---------------------------------------------------------------------------
def control_LR(
    name: str, tables: np.ndarray, xs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    def col(term_name: str) -> np.ndarray:
        return tables[:, :, TERM_INDEX[term_name]]

    x = xs.reshape(1, -1)
    if name == "C1":
        left = np.abs(col("PSIERR"))
        right = 0.5 * np.sqrt(x) * np.log(x)
        right = np.broadcast_to(right, left.shape).copy()
        return left, right
    if name == "C2":
        left = np.abs(col("G(1,14.134725)"))
        right = 2.0 * np.log(x)
        right = np.broadcast_to(right, left.shape).copy()
        return left, right
    if name == "C3":
        left = col("PSI")
        right = 1.2 * x
        right = np.broadcast_to(right, left.shape).copy()
        return left, right
    if name == "C4":
        left = np.abs(col("Sc(1/2,10)"))
        right = col("Sc(1/2,0)")
        return left, right
    raise KeyError(name)


def evaluate_control(
    name: str,
    tables: np.ndarray,
    xs: np.ndarray,
    train_idx: np.ndarray,
    hold_idx: np.ndarray,
) -> dict:
    with np.errstate(all="ignore"):
        left, right = control_LR(name, tables, xs)
        sl = slack_arr(left, right)
    s_train = float(np.min(sl[W_TRUE, train_idx]))
    s_hold = float(np.min(sl[W_TRUE, hold_idx])) if hold_idx.size else s_train
    key1_hits = []
    for w, seed in zip(SCR_IDX, SCRAMBLE_SEEDS):
        row = sl[w, train_idx]
        j = int(np.argmin(row))
        key1_hits.append(
            {
                "seed": int(seed),
                "min_slack": float(row[j]),
                "X": int(xs[train_idx[j]]),
                "breaks": bool(row[j] < 0.0),
            }
        )
    key1 = sum(1 for h in key1_hits if h["breaks"]) / float(len(SCR_IDX))
    key2_hits = []
    for w, (beta, gamma) in zip(OFF_IDX, OFF_WORLDS):
        row = sl[w, train_idx]
        j = int(np.argmin(row))
        key2_hits.append(
            {
                "beta": float(beta),
                "gamma": float(gamma),
                "min_slack": float(row[j]),
                "X": int(xs[train_idx[j]]),
                "breaks": bool(row[j] < 0.0),
            }
        )
    key2 = sum(1 for h in key2_hits if h["breaks"]) / float(len(OFF_IDX))
    klass = classify(s_train, s_hold, key1, key2)
    return {
        "name": name,
        "s_train": s_train,
        "s_hold": s_hold,
        "key1": float(key1),
        "key2": float(key2),
        "class": klass,
        "key1_hits": key1_hits,
        "key2_hits": key2_hits,
        "slack": sl,
    }


def amplitude_diag(xs: np.ndarray) -> list[dict]:
    rows = []
    for beta, gamma in OFF_WORLDS:
        rho_abs = math.hypot(beta, gamma)
        for x in xs:
            xf = float(x)
            amp = 2.0 * (xf ** beta) / rho_abs
            bound_c1 = 0.5 * math.sqrt(xf) * math.log(xf)
            bound_c2 = 2.0 * math.log(xf)
            rows.append(
                {
                    "beta": beta,
                    "gamma": gamma,
                    "X": int(x),
                    "amp": amp,
                    "C1_bound": bound_c1,
                    "C2_bound": bound_c2,
                    "amp_over_C1": amp / bound_c1,
                    "amp_over_C2": amp / bound_c2,
                }
            )
    return rows


# ---------------------------------------------------------------------------
# GP
# ---------------------------------------------------------------------------
def tournament(
    pop: list[dict], rng: random.Random, k: int = TOURNAMENT_K,
) -> dict:
    pick = [pop[rng.randrange(len(pop))] for _ in range(k)]
    pick.sort(key=lambda r: (-r["fitness"], r["expr"]))
    return pick[0]


def run_gp(
    tables: np.ndarray,
    xs: np.ndarray,
    train_idx: np.ndarray,
    hold_idx: np.ndarray,
    pop_n: int,
    n_gen: int,
    rng: random.Random,
) -> tuple[dict[str, dict], list[dict]]:
    hall: dict[str, dict] = {}

    def consider(left: tuple, right: tuple) -> dict:
        left = normalize(left)[1]
        right = normalize(right)[1]
        expr = canon_pair(left, right)
        cached = hall.get(expr)
        if cached is not None:
            return cached
        rec = evaluate_pair(left, right, tables, train_idx, hold_idx)
        slim = {k: rec[k] for k in (
            "expr", "fitness", "s_train", "s_hold", "key1", "key2",
            "size", "class", "scr_mins", "off_mins", "scr_at", "off_at",
        )}
        slim["left"] = rec["left"]
        slim["right"] = rec["right"]
        slim["slack"] = rec["slack"]
        hall[expr] = slim
        return slim

    population: list[dict] = []
    seen: set[str] = set()
    for left, right in seeded_battery(rng):
        rec = consider(left, right)
        if rec["expr"] not in seen:
            seen.add(rec["expr"])
            population.append(rec)
    guard = 0
    while len(population) < pop_n and guard < pop_n * 40:
        guard += 1
        left, right = random_pair(rng)
        rec = consider(left, right)
        if rec["expr"] in seen:
            continue
        seen.add(rec["expr"])
        population.append(rec)
    while len(population) < pop_n:
        left, right = random_pair(rng)
        rec = consider(left, right)
        population.append(rec)

    for _gen in range(n_gen):
        population.sort(key=lambda r: (-r["fitness"], r["expr"]))
        next_pop = population[:ELITE]
        next_seen = {r["expr"] for r in next_pop}
        guard = 0
        while len(next_pop) < pop_n and guard < pop_n * 60:
            guard += 1
            u = rng.random()
            if u < CX_P:
                p1 = tournament(population, rng)
                p2 = tournament(population, rng)
                child = crossover_pair(
                    (p1["left"], p1["right"]),
                    (p2["left"], p2["right"]),
                    rng,
                )
            elif u < CX_P + MUT_P:
                p = tournament(population, rng)
                child = mutate_pair(p["left"], p["right"], rng)
            else:
                p = tournament(population, rng)
                child = (p["left"], p["right"])
            rec = consider(child[0], child[1])
            if rec["expr"] in next_seen:
                continue
            next_seen.add(rec["expr"])
            next_pop.append(rec)
        while len(next_pop) < pop_n:
            p = tournament(population, rng)
            rec = consider(p["left"], p["right"])
            next_pop.append(rec)
        population = next_pop

    population.sort(key=lambda r: (-r["fitness"], r["expr"]))
    return hall, population


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------
def family_tag(expr: str) -> str:
    work = expr
    hits: list[str] = []
    for name in sorted(SENSITIVE_NAMES, key=lambda s: (-len(s), s)):
        if name in work:
            hits.append(name)
            work = work.replace(name, "#" * len(name))
    hits.sort()
    return "+".join(hits) if hits else "other"


def slim_record(rec: dict) -> dict:
    return {
        "expr": rec["expr"],
        "fitness": canon_float(rec["fitness"]),
        "s_train": canon_float(rec["s_train"]),
        "s_hold": canon_float(rec["s_hold"]),
        "key1": canon_float(rec["key1"]),
        "key2": canon_float(rec["key2"]),
        "size": int(rec["size"]),
        "class": rec["class"],
        "scr_mins": [canon_float(v) for v in rec["scr_mins"]],
        "off_mins": [canon_float(v) for v in rec["off_mins"]],
    }


def profile_payload(rec: dict, xs: np.ndarray, prof_idx: np.ndarray) -> dict:
    sl = rec["slack"]
    worlds = {}
    for w, wname in enumerate(WORLD_NAMES):
        worlds[wname] = [
            {"X": int(xs[i]), "slack": canon_float(float(sl[w, i]))}
            for i in prof_idx
        ]
    return {"expr": rec["expr"], "worlds": worlds}


def print_control(ctrl: dict, xs: np.ndarray, train_idx: np.ndarray) -> None:
    print(
        "%s  class=%s  s_train=%s  s_hold=%s  key1=%s  key2=%s"
        % (
            ctrl["name"],
            ctrl["class"],
            fmt(ctrl["s_train"]),
            fmt(ctrl["s_hold"]),
            fmt(ctrl["key1"], 4),
            fmt(ctrl["key2"], 4),
        )
    )
    for hit in ctrl["key1_hits"]:
        print(
            "    SCR seed=%d  breaks=%d  min_slack=%s  X=%d"
            % (hit["seed"], int(hit["breaks"]), fmt(hit["min_slack"]), hit["X"])
        )
    for hit in ctrl["key2_hits"]:
        print(
            "    OFF beta=%.2f gamma=%.1f  breaks=%d  min_slack=%s  X=%d"
            % (
                hit["beta"],
                hit["gamma"],
                int(hit["breaks"]),
                fmt(hit["min_slack"]),
                hit["X"],
            )
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def run(smoke: bool) -> int:
    xmax = 2 * 10 ** 4 if smoke else X_MAX
    pop_n = 40 if smoke else POP
    n_gen = 4 if smoke else GENS
    train_x = tuple(x for x in TRAIN_X if x <= xmax)
    hold_x = tuple(x for x in HOLDOUT_X if x <= xmax)
    prof_x = tuple(x for x in PROFILE_X if x <= xmax)
    sanity_x = tuple(x for x in SANITY_X if x <= xmax)
    xs_list = []
    seen = set()
    for x in train_x + hold_x + prof_x + sanity_x:
        if x not in seen and x <= xmax:
            seen.add(x)
            xs_list.append(int(x))
    xs_list.sort()
    xs = np.asarray(xs_list, dtype=np.int64)
    train_idx = np.asarray([int(np.where(xs == x)[0][0]) for x in train_x], dtype=np.int64)
    hold_idx = np.asarray(
        [int(np.where(xs == x)[0][0]) for x in hold_x], dtype=np.int64,
    ) if hold_x else np.zeros(0, dtype=np.int64)
    prof_idx = np.asarray([int(np.where(xs == x)[0][0]) for x in prof_x], dtype=np.int64)

    print("prime_inequality_evosearch_probe -- r603")
    print("CLAIM_BOUNDARY hypothesis_generator; NO_RH_CLAIM")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("X_MAX_RUN %d" % xmax)
    print("N_TERMS %d" % N_TERMS)
    print("TRAIN_X " + " ".join(str(x) for x in train_x))
    print("HOLDOUT_X " + " ".join(str(x) for x in hold_x))
    print("PROFILE_X " + " ".join(str(x) for x in prof_x))

    check("G0-train-count", len(train_x) == (20 if not smoke else len(train_x)),
          "n_train=%d" % len(train_x))
    check("G0b-holdout-count",
          (len(hold_x) == 10) if not smoke else True,
          "n_hold=%d" % len(hold_x))
    check("G0c-spec-sha", len(SPEC_SHA) == 64, SPEC_SHA[:16])

    section("WORLDS")
    lam_true, primes = sieve_von_mangoldt(xmax)
    worlds = [lam_true]
    true_dy = dyadic_sums(lam_true, xmax)
    dy_report = []
    for seed in SCRAMBLE_SEEDS:
        lam_s, n_mapped = scramble_lambda(primes, xmax, seed)
        worlds.append(lam_s)
        scr_dy = dyadic_sums(lam_s, xmax)
        rel, lo, hi = max_rel_dyadic(true_dy, scr_dy)
        rel256, lo256, hi256 = max_rel_dyadic(true_dy, scr_dy, min_lo=256)
        rel4k, lo4k, hi4k = max_rel_dyadic(true_dy, scr_dy, min_lo=4096)
        n_sites = int(np.count_nonzero(lam_s > 0.0))
        dy_report.append(
            {
                "seed": int(seed),
                "max_rel": float(rel),
                "dyad": [lo, hi],
                "max_rel_lo256": float(rel256),
                "dyad256": [lo256, hi256],
                "max_rel_lo4096": float(rel4k),
                "dyad4096": [lo4k, hi4k],
                "n_sites": n_sites,
                "n_mapped": int(n_mapped),
            }
        )
    for beta, gamma in OFF_WORLDS:
        worlds.append(lambda_off(lam_true, beta, gamma))

    n_primes = int(primes.size)
    check(
        "G1-sieve-primes",
        n_primes > 100,
        "pi(%d)=%d" % (xmax, n_primes),
    )
    mapped_ok = all(r["n_mapped"] == n_primes for r in dy_report)
    check(
        "G1a-scramble-count",
        mapped_ok,
        "n_mapped=%s pi=%d" % ([r["n_mapped"] for r in dy_report], n_primes),
    )
    for rec in dy_report:
        print(
            "SCRAMBLE_DENSITY seed=%d max_rel=%s dyad=[%d,%d] "
            "max_rel_lo256=%s dyad256=[%d,%d] "
            "max_rel_lo4096=%s dyad4096=[%d,%d] n_mapped=%d n_sites=%d"
            % (
                rec["seed"],
                fmt(rec["max_rel"]), rec["dyad"][0], rec["dyad"][1],
                fmt(rec["max_rel_lo256"]), rec["dyad256"][0], rec["dyad256"][1],
                fmt(rec["max_rel_lo4096"]), rec["dyad4096"][0], rec["dyad4096"][1],
                rec["n_mapped"], rec["n_sites"],
            )
        )
    max_rel_all = max(r["max_rel"] for r in dy_report)
    max_rel_large = max(r["max_rel_lo4096"] for r in dy_report)
    check(
        "G1b-scramble-density-finite",
        math.isfinite(max_rel_all) and math.isfinite(max_rel_large),
        "max_rel=%s max_rel_lo4096=%s" % (fmt(max_rel_all), fmt(max_rel_large)),
    )

    print("PSIERR_SANITY  (psi(X)-X)")
    sanity_rows = []
    for w, wname in enumerate(WORLD_NAMES):
        psi = np.cumsum(worlds[w])
        row = {"world": wname}
        parts = []
        for x in sanity_x:
            err = float(psi[x] - x)
            row[str(x)] = err
            parts.append("X=%d %s" % (x, fmt(err)))
        sanity_rows.append(row)
        print("  %s  %s" % (wname, "  ".join(parts)))

    section("TABLES")
    weights = _weights(xmax)
    tables = build_tables(worlds, xs, weights)
    check(
        "G2-table-shape",
        tables.shape == (N_WORLDS, xs.size, N_TERMS),
        "shape=%s" % (tables.shape,),
    )
    check(
        "G2b-true-psi-match",
        abs(float(tables[W_TRUE, int(np.where(xs == sanity_x[-1])[0][0]),
                         TERM_INDEX["PSIERR"]])
            - float(np.cumsum(lam_true)[sanity_x[-1]] - sanity_x[-1])) < 1e-8,
        "psierr snapshot consistent",
    )

    section("CONTROLS")
    controls = [
        evaluate_control(name, tables, xs, train_idx, hold_idx)
        for name in ("C1", "C2", "C3", "C4")
    ]
    for ctrl in controls:
        print_control(ctrl, xs, train_idx)
    amp_rows = amplitude_diag(np.asarray(list(sanity_x) + list(train_x[-3:]), dtype=np.int64))
    need_amp = any(
        (c["name"] in ("C1", "C2") and c["key2"] < 1.0) for c in controls
    )
    if need_amp:
        print("AMPLITUDE_DIAGNOSIS  (C1/C2 did not fully break on W_OFF)")
        print("  formula 2 X^beta / |rho0|  vs  C1: 0.5 sqrt(X) log X   C2: 2 log X")
        for row in amp_rows:
            print(
                "  beta=%.2f gamma=%.1f X=%d  amp=%s  C1=%s amp/C1=%s  C2=%s amp/C2=%s"
                % (
                    row["beta"],
                    row["gamma"],
                    row["X"],
                    fmt(row["amp"]),
                    fmt(row["C1_bound"]),
                    fmt(row["amp_over_C1"]),
                    fmt(row["C2_bound"]),
                    fmt(row["amp_over_C2"]),
                )
            )
    check("G3-controls-ran", len(controls) == 4, "n=4")

    section("GP")
    rng = random.Random(SEED)
    hall, population = run_gp(
        tables, xs, train_idx, hold_idx, pop_n, n_gen, rng,
    )
    records = list(hall.values())
    n_surv = sum(1 for r in records if r["class"] == "SURVIVOR")
    n_one = sum(1 for r in records if r["class"] == "ONE_KEY")
    n_den = sum(1 for r in records if r["class"] == "DENSITY")
    n_inv = sum(1 for r in records if r["class"] == "INVALID")
    n_twokey_holdfail = sum(
        1 for r in records
        if r["key1"] == 1.0 and r["key2"] == 1.0 and r["s_hold"] < 0.0
        and r["s_train"] >= 0.0
    )
    print("N_UNIQUE %d" % len(records))
    print("N_SURVIVOR %d" % n_surv)
    print("N_ONE_KEY %d" % n_one)
    print("N_DENSITY %d" % n_den)
    print("N_INVALID %d" % n_inv)
    print("N_TWOKEY_HOLDOUT_FAIL %d" % n_twokey_holdfail)

    ranked = sorted(records, key=lambda r: (-r["fitness"], r["expr"]))
    top15 = ranked[:15]
    print("TOP15")
    print(
        "rank fitness class key1 key2 size s_train s_hold expr"
    )
    for i, rec in enumerate(top15, 1):
        print(
            "%2d %s %-9s %s %s %3d %s %s  %s"
            % (
                i,
                fmt(rec["fitness"]),
                rec["class"],
                fmt(rec["key1"], 4),
                fmt(rec["key2"], 4),
                rec["size"],
                fmt(rec["s_train"]),
                fmt(rec["s_hold"]),
                rec["expr"],
            )
        )

    survivors = [r for r in ranked if r["class"] == "SURVIVOR"]
    fam_counts: dict[str, int] = {}
    for rec in survivors:
        tag = family_tag(rec["expr"])
        fam_counts[tag] = fam_counts.get(tag, 0) + 1
    fam_rows = sorted(fam_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    print("SURVIVOR_FAMILIES n_tags=%d" % len(fam_rows))
    for tag, cnt in fam_rows[:20]:
        print("  %4d  %s" % (cnt, tag))
    shown = survivors[:PROFILE_CAP]
    print("SURVIVOR_PROFILES n=%d shown=%d  X=%s" % (
        len(survivors),
        len(shown),
        " ".join(str(int(xs[i])) for i in prof_idx),
    ))
    for rec in shown:
        print("  EXPR %s" % rec["expr"])
        sl = rec["slack"]
        for w, wname in enumerate(WORLD_NAMES):
            bits = " ".join(
                "%d:%s" % (int(xs[i]), fmt(float(sl[w, i]), 4))
                for i in prof_idx
            )
            print("    %s  %s" % (wname, bits))
        for i, w in enumerate(SCR_IDX):
            j = rec["scr_at"][i]
            print(
                "    FIRE %s X=%d slack=%s"
                % (WORLD_NAMES[w], int(xs[train_idx[j]]), fmt(rec["scr_mins"][i]))
            )
        for i, w in enumerate(OFF_IDX):
            j = rec["off_at"][i]
            print(
                "    FIRE %s X=%d slack=%s"
                % (WORLD_NAMES[w], int(xs[train_idx[j]]), fmt(rec["off_mins"][i]))
            )

    n0_dense = int(train_x[0]) if train_x else 2000
    print("DENSE_TRUE_AUDIT n0=%d n1=%d" % (n0_dense, xmax))
    dense_rows: list[dict] = []
    col_cache: dict[int, np.ndarray] = {}
    n_grid_only = 0
    n_dense_hold = 0
    for rec in shown:
        m, at = dense_true_min(
            rec["left"], rec["right"], lam_true, weights,
            n0_dense, xmax, col_cache,
        )
        status = "HOLDS" if m >= 0.0 else "GRID_ONLY"
        if status == "GRID_ONLY":
            n_grid_only += 1
        else:
            n_dense_hold += 1
        print(
            "  %s min_slack=%s at X=%d  %s"
            % (status, fmt(m), at, rec["expr"])
        )
        dense_rows.append(
            {
                "expr": rec["expr"],
                "status": status,
                "min_slack": canon_float(m),
                "X": int(at),
            }
        )
    print(
        "DENSE_TRUE_SUMMARY shown=%d HOLDS=%d GRID_ONLY=%d"
        % (len(shown), n_dense_hold, n_grid_only)
    )
    check(
        "G3c-dense-audit",
        len(dense_rows) == len(shown),
        "HOLDS=%d GRID_ONLY=%d" % (n_dense_hold, n_grid_only),
    )

    if n_surv > 0:
        verdict = "SURVIVORS_FOUND(%d)" % n_surv
    elif n_one > 0:
        verdict = "ONLY_ONE_KEY(%d)" % n_one
    else:
        verdict = "NO_SURVIVOR"
    print("VERDICT %s" % verdict)

    payload = {
        "SPEC_SHA": SPEC_SHA,
        "smoke": int(smoke),
        "xmax": xmax,
        "verdict": verdict,
        "n_unique": len(records),
        "n_survivor": n_surv,
        "n_one_key": n_one,
        "n_density": n_den,
        "n_invalid": n_inv,
        "n_twokey_holdfail": n_twokey_holdfail,
        "survivor_families": [
            {"tag": tag, "n": int(cnt)} for tag, cnt in fam_rows
        ],
        "top15": [slim_record(r) for r in top15],
        "survivors": [slim_record(r) for r in shown],
        "survivor_profiles": [
            profile_payload(r, xs, prof_idx) for r in shown
        ],
        "dense_true_audit": dense_rows,
        "controls": [
            {
                "name": c["name"],
                "class": c["class"],
                "s_train": canon_float(c["s_train"]),
                "s_hold": canon_float(c["s_hold"]),
                "key1": canon_float(c["key1"]),
                "key2": canon_float(c["key2"]),
                "key1_hits": [
                    {
                        "seed": h["seed"],
                        "min_slack": canon_float(h["min_slack"]),
                        "X": h["X"],
                        "breaks": int(h["breaks"]),
                    }
                    for h in c["key1_hits"]
                ],
                "key2_hits": [
                    {
                        "beta": h["beta"],
                        "gamma": h["gamma"],
                        "min_slack": canon_float(h["min_slack"]),
                        "X": h["X"],
                        "breaks": int(h["breaks"]),
                    }
                    for h in c["key2_hits"]
                ],
            }
            for c in controls
        ],
        "scramble_density": [
            {
                "seed": r["seed"],
                "max_rel": canon_float(r["max_rel"]),
                "dyad": r["dyad"],
                "max_rel_lo256": canon_float(r["max_rel_lo256"]),
                "dyad256": r["dyad256"],
                "max_rel_lo4096": canon_float(r["max_rel_lo4096"]),
                "dyad4096": r["dyad4096"],
                "n_sites": r["n_sites"],
                "n_mapped": r["n_mapped"],
            }
            for r in dy_report
        ],
        "psierr_sanity": [
            {k: (canon_float(v) if k != "world" else v) for k, v in row.items()}
            for row in sanity_rows
        ],
        "amplitude": [
            {k: (canon_float(v) if isinstance(v, float) else v) for k, v in row.items()}
            for row in amp_rows
        ],
    }
    seal = payload_sha(payload)
    seal2 = payload_sha(payload)
    check("G4-payload-repeat", seal == seal2, seal[:16])

    rng_b = random.Random(SEED)
    hall_b, _pop_b = run_gp(
        tables, xs, train_idx, hold_idx, pop_n, n_gen, rng_b,
    )
    exprs_a = sorted(hall.keys())
    exprs_b = sorted(hall_b.keys())
    check(
        "G5-inprocess-gp-replay",
        exprs_a == exprs_b,
        "n_unique=%d" % len(exprs_a),
    )
    if exprs_a == exprs_b:
        fit_ok = all(
            hall[e]["fitness"] == hall_b[e]["fitness"]
            and hall[e]["class"] == hall_b[e]["class"]
            for e in exprs_a
        )
        check("G5b-fitness-replay", fit_ok, "fitness+class match")
    else:
        check("G5b-fitness-replay", False, "expr sets differ")

    next_suggest = (
        "r603: %s unique=%d surv=%d onekey=%d density=%d; "
        "C1=%s C2=%s C3=%s C4=%s; scramble max_rel=%s max_rel_lo4096=%s. "
        "KEIN RH-CLAIM; Survivor=Hypothese."
        % (
            verdict,
            len(records),
            n_surv,
            n_one,
            n_den,
            controls[0]["class"],
            controls[1]["class"],
            controls[2]["class"],
            controls[3]["class"],
            fmt(max_rel_all),
            fmt(max_rel_large),
        )
    )
    print("PAYLOAD_SHA256 %s" % seal)
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
            "r603 two-key GP inequality search on von Mangoldt data "
            "(experiments only; no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
