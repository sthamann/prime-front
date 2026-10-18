#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""collective_rescue_probe -- PRIME.SCREW.COLLECTIVE.RESCUE.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, zero table, paper, ledger, website or
verification file, and makes NO RH claim.

TARGET.  Round 92 (PRIME.SCREW.VERBLUNSKY.INVARIANT.01, SPEC_SHA
c730781e8d0874d3) observed a "collective rescue": adding complete
prime packets Delta c_d(p) = -log p sum_m p^{-m/2} phi_d(m log p) in
prime order to the archimedean background at mesh delta=0.006 on the
window L=2.568, the Verblunsky stream exits the unit Schur disk after
the prefixes {2},{2,3},{2,3,5},{2,3,5,7} (ALPHA_EXIT at
r=1.122/1.620/1.950/2.400), re-enters after p=11 (max|alpha|=0.313)
and stays inside after p=13/full (0.184).  This probe tests the cheap
hypothesis FIRST: a truncated prime stream is a WRONG-DENSITY world
beyond its last packet (zero mass where the true measure continues),
the exit is the mirrored twin of the smooth death at r=0.264, and the
re-entry is nothing but the next packet supplying mass where the
window reaches.

CAUSALITY LEMMA (elementary; machine-checked as wards W4/W5/W6).  The
tent moment c_d reads only atoms with |u - d*delta| < delta.  Removing
every atom with u >= u_miss leaves c_0..c_{d0-1} unchanged,
d0 = floor(u_miss/delta), and the Levinson recursion leaves
alpha_0..alpha_{d0-2} bit-identical to the full stream.  Hence
(i)  EXACT LOWER BOUND: a truncated stream cannot exit before the
     onset index  onset = d0 - 1;
(ii) RESCUE = CAUSAL IDENTITY: a truncation whose first missing
     support lies at or beyond the window is bit-identical to the
     full stream on the whole window; nothing is dynamically rescued;
(iii) the only EMPIRICAL law content is the upper offset
     J(k) = fail_k - onset(k) >= 0: how few lags past onset the
     blow-up completes.
The claimed law: J(k) <= 8 lags (0.048 depth) for every prime
truncation k=1..10 on the extended window (L1); survivor rule: a rung
survives the window iff its onset lies beyond it (L2); the k=0 rung
(archimedean only, first missing support log 2) exits inside the
missing-2 span before the log-3 onset (L3); the law is mesh-robust at
delta=0.008 (L4); and the rescue is carried by the single boundary
atom, not the packet and not the prime (L5/L6).

WORLDS AND LADDERS (all frozen; no post-hoc rung selection).
 WARD WORLD   delta=0.006, n=428 (L=2.568), dps=100: regression
   against round 92 (full max 0.183932, P5 max 0.312863, truncation
   exits 187/270/325/400, SMOOTH exit 44 / attempted -2.537735,
   SCRARITH exit 124 / attempted -2.370365, golden-permuted weights
   verbatim).
 C1 LADDER    delta=0.006, n=600 (L=3.6), dps=60: rungs k=0..11
   (first k primes of 2,3,5,7,11,13,17,19,23,29,31; first missing
   support log p_{k+1}; for k=11 log 37 = 3.611 >= L predicts
   survival).  Exit table with onset, offset, attempted alpha,
   missing-density mass at exit M = 2(e^{r/2}-e^{u/2}), pre-onset
   local max|alpha| (40 lags), and three prediction laws:
   A support-onset (calibration-free), B constant-missing-mass
   (calibrated on k=1), C Mertens-like r = u + c*/u (calibrated on
   k=1).  Offset carrier: Pearson correlation of the offset against
   the pre-onset local alpha level, printed.
 C1 MESH SCREEN delta=0.008, n=450 (L=3.6), dps=60: rungs k=0..4.
 C2 DEEP      delta=0.006, n=800 (L=4.8), dps=60 and
              delta=0.008, n=600 (L=4.8), dps=60: the completed
   stream (all packets).  Cumulative and band max|alpha| at depths
   2.568/3.0/3.6/4.2/window-end, band-slope and log-margin fits
   (float64 diagnostics).  Comfort bar (L7): cumulative max < 0.5 on
   the measured prefix in both mesh worlds.  This is a MEASUREMENT of
   the localized-positivity margin in the screw coordinate; it is
   never evidence for the all-depth quantifier.
 C3 RESCUE DECOMPOSITION  n=600, dps=60: {2}+only-3^1 must move the
   exit into the log-5 onset window (L5); {2}+only-3^2 must leave the
   exit index exactly unchanged (L6); the P4->P5 repair at n=428 is
   printed lag-by-lag (the p=11 packet inside L=2.568 is a single
   atom touching two lags; banded Toeplitz, displacement rank <= 2 by
   structure).  LYAPUNOV CANDIDATE PROGRAM: K1 common-prefix Szego
   entropy sum_{j<180} log(1-alpha_j^2) across rungs (constant by
   causality => non-discriminating, typed kill); K2 frontier entropy
   drop over the last 40 lags before exit (fraction carried by the
   last 8 lags printed; if dominated by the blow-up it is the exit
   itself, circular, typed kill); K3 final prediction error at exit.
 C4 CONTROLS  n=600, dps=60: SMOOTH-SHIFTED (PNT density e^{u/2}
   started at the true support point log 2 -- support right, mass
   profile right on average, atoms absent) and MASS-RESTORED
   truncation ({2,3,5,7} complete + density tail from log 11 --
   missing mass restored without atoms).  Exit-pattern table across
   all worlds (exit, onset offset where defined, attempted alpha,
   frontier entropy).  tau/mesh screen: the law bar 8 lags stays
   below the minimal missing-support gap (log 31 - log 29 = 0.0667 >
   0.060, precondition ward A2).

WARDS (any failure => INSTRUMENT-EDGE, exit 1, no mathematical
verdict): A1 source-only AST firewall (no repository reads, no zeta
or zero calls); A2 frozen ladder arithmetic + sharpness precondition;
W1 full-428 regression at dps=100 and dps=60 (cross-dps bar 1e-12,
regression bar 5e-5); W2 truncation exits 187/270/325/400 and P5 max
0.312863 (dps=100); W3 SMOOTH/SCRARITH regression (exit indices
44/124, attempted-value bar 1e-4); W4 P5 structure: argmax = 426 (the
single differing alpha), P5 == full below 426 and P4 == P5 below 398
(bar 1e-60); W5 causality lower bound fail_k >= onset on every
truncation-family run and exit-index invariance across n and dps for
rungs 1..4; W6 rung-11 == full-600 bit-level (bar 1e-60) and K1
common-prefix entropy constancy (bar 1e-60); A3 runtime <= 900 s.

LAW GATES (failures are mathematical outcomes, not instrument edges):
L1 offsets J(k) in [0,8] for k=1..10; L2 rung 11 survives the window;
L3 rung 0 exits in [onset(log2), onset(log3)); L4 mesh-world offsets
J(k) in [0,8] for k=1..4; L5 {2}+3^1 exit lands in the log-5 onset
window; L6 {2}+3^2 exit index equals the rung-1 exit index;
L7 C2 comfort bar (reported; excluded from the support verdict).

VERDICT ENUM (priority order):
 COLLECTIVE-IS-SUPPORT(law stated)      -- L1..L6 all pass;
 COLLECTIVE-LAW-FOUND(stated)           -- support gates fail but the
   measured offsets stay <= 30 lags with a measured carrier;
 COLLECTIVE-LYAPUNOV(candidate stated)  -- support gates fail and a
   frontier functional is monotone on truth and broken on controls;
 COLLECTIVE-UNEXPLAINED(exclusions)     -- otherwise;
 INSTRUMENT-EDGE                        -- any ward failed.

DECLARED NUMERICS AND COSTS.  Moment rows are built at dps=115
(mpmath); Levinson recursions run at the declared per-world dps
(100 wards / 60 ladders); every lag and every prime-power atom with
u < 4.8 is used (primes 2..113, all powers in window); no
subsampling anywhere; float64 only for fits, correlations and
printing.  Runtime bar 900 s.

NO RH CLAIM.  NO ALL-DEPTH POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np


T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

DELTA_TEXT = "0.006"
DELTA = 0.006
DELTA2_TEXT = "0.008"
DELTA2 = 0.008
DPS_BUILD = 115
DPS_WARD = 100
DPS_MAIN = 60
N_WARD = 428
L_WARD = 2.568
N_C1 = 600
L_C1 = 3.6
N_C1B = 450
N_C2 = 800
L_C2 = 4.8
N_C2B = 600
OFFSET_MAX = 8
LAWFOUND_OFFSET_CAP = 30
W_FRONT = 40
J0_PREFIX = 180
COMFORT_BAR = 0.5
RUNTIME_BAR = 900.0
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
C1_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
DEPTHS_COMMON = (2.568, 3.0, 3.6, 4.2)
WARD_EXITS = (187, 270, 325, 400)
WARD_FULL_MAX = 0.183932
WARD_P5_MAX = 0.312863
WARD_SMOOTH_EXIT = 44
WARD_SCRAM_EXIT = 124
WARD_SMOOTH_ATT = -2.537735
WARD_SCRAM_ATT = -2.370365

WARDS: list[tuple[str, bool, str]] = []
LAWS: list[tuple[str, bool, str]] = []


def check_ward(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    WARDS.append((name, result, detail))
    print("  [%s] %-52s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def gate_law(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    LAWS.append((name, result, detail))
    print("  [%s] %-48s %s"
          % ("LAW-PASS" if result else "LAW-FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fmt_mp(x, digits: int = 8) -> str:
    return mp.nstr(x, digits, min_fixed=0, max_fixed=0)


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {
        "__future__", "ast", "hashlib", "math", "os", "time",
        "mpmath", "numpy",
    }
    forbidden_calls = {
        "load", "loadtxt", "genfromtxt", "fromfile",
        "zetazero", "zetazeros", "nzeros", "siegelz", "siegeltheta",
    }
    forbidden_attrs = {
        "zeta", "zetazero", "zetazeros", "nzeros",
        "siegelz", "siegeltheta",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    return not bad, "violations=%s" % (bad or "none")


# ---------------------------------------------------------- prime arithmetic
def sieve_primes(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    if limit >= 1:
        bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def prime_atoms(L: float) -> list[tuple[int, int, mp.mpf, mp.mpf]]:
    """(p,m,u,w) with u=m log p<L and w=log(p)/sqrt(p^m)."""
    limit = int(math.exp(L)) + 1
    out: list[tuple[int, int, mp.mpf, mp.mpf]] = []
    with mp.workdps(DPS_BUILD):
        for p in sieve_primes(limit):
            lp = mp.log(p)
            q = p
            m = 1
            while m * float(lp) < L - 1e-14:
                out.append((p, m, m * lp, lp / mp.sqrt(q)))
                if q > limit // p:
                    break
                q *= p
                m += 1
    out.sort(key=lambda item: item[2])
    return out


def atom_row(u, weight, n: int, delta_text: str) -> list[mp.mpf]:
    """The exact tent read -weight*phi_d(u), d=0..n-1, at mesh delta."""
    with mp.workdps(DPS_BUILD):
        out = [mp.mpf(0) for _ in range(n)]
        x = u / mp.mpf(delta_text)
        lo = int(mp.floor(x))
        for d in (lo, lo + 1):
            if 0 <= d < n:
                value = 1 - abs(x - d)
                if value > 0:
                    out[d] -= weight * value
    return out


def packet_rows(atoms, n: int, delta_text: str) -> dict[int, list[mp.mpf]]:
    packets: dict[int, list[mp.mpf]] = {}
    with mp.workdps(DPS_BUILD):
        for p, _m, u, weight in atoms:
            if p not in packets:
                packets[p] = [mp.mpf(0) for _ in range(n)]
            ar = atom_row(u, weight, n, delta_text)
            packets[p] = [a + b for a, b in zip(packets[p], ar)]
    return packets


def add_rows(*rows: list[mp.mpf]) -> list[mp.mpf]:
    with mp.workdps(DPS_BUILD):
        return [mp.fsum(values) for values in zip(*rows)]


# ---------------------------------------------------------- corpus screw g
MP_CONST: dict[str, mp.mpf] = {}
S_CACHE: dict[tuple[str, int], mp.mpf] = {}


def setup_constants() -> None:
    with mp.workdps(DPS_BUILD + 20):
        MP_CONST["psi14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["logpi"] = mp.log(mp.pi)
        MP_CONST["phi1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)


def s_arch_grid(index: int, delta_text: str) -> mp.mpf:
    """S(t)=(1/4)e^(-t/2)Phi(e^(-2t),2,1/4), t=index*delta."""
    key = (delta_text, index)
    if key in S_CACHE:
        return S_CACHE[key]
    with mp.workdps(DPS_BUILD):
        t = mp.mpf(index) * mp.mpf(delta_text)
        if index == 0:
            value = MP_CONST["phi1"] / 4
        elif t < mp.mpf("0.3"):
            value = (mp.exp(-t / 2)
                     * mp.lerchphi(mp.exp(-2 * t), 2, mp.mpf(1) / 4) / 4)
        else:
            z = mp.exp(-2 * t)
            total = mp.mpf(0)
            power = mp.mpf(1)
            k = 0
            floor = mp.mpf(10) ** (-(DPS_BUILD + 8))
            while power > floor * (1 + abs(total)):
                total += power / (mp.mpf(k) + mp.mpf(1) / 4) ** 2
                power *= z
                k += 1
            value = mp.exp(-t / 2) * total / 4
    S_CACHE[key] = value
    return value


def base_g_values(n: int, delta_text: str) -> list[mp.mpf]:
    """Archimedean background, including the pole layer, no primes."""
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        for j in range(n + 1):
            t = j * dl
            value = -8 * (mp.cosh(t / 2) - 1)
            value -= (t / 2) * (MP_CONST["psi14"] - MP_CONST["logpi"])
            value -= MP_CONST["phi1"] / 4
            value += s_arch_grid(j, delta_text)
            values.append(value)
    return values


def lag_row_from_g(values: list[mp.mpf], delta_text: str) -> list[mp.mpf]:
    with mp.workdps(DPS_BUILD):
        dl = mp.mpf(delta_text)
        n = len(values) - 1
        row = [-2 * values[1] / dl]
        for d in range(1, n):
            row.append(-(values[d - 1] - 2 * values[d] + values[d + 1]) / dl)
    return row


def tail_ramp_row(u0, n: int, delta_text: str) -> list[mp.mpf]:
    """lag row of g_tail(t)=int_{u0}^t (t-u) e^{u/2} du (0 for t<u0)."""
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        eh = mp.exp(u0 / 2)
        for j in range(n + 1):
            t = j * dl
            if t <= u0:
                values.append(mp.mpf(0))
            else:
                values.append(4 * mp.exp(t / 2) - eh * (2 * (t - u0) + 4))
    return lag_row_from_g(values, delta_text)


def scrambled_row(base_row: list[mp.mpf], atoms,
                  delta_text: str) -> tuple[list[mp.mpf], list[mp.mpf]]:
    q_values = [p ** m for p, m, _u, _w in atoms]
    order = sorted(range(len(atoms)),
                   key=lambda i: (q_values[i] * GOLDEN) % 1.0)
    weights = [atoms[i][3] for i in order]
    row = list(base_row)
    for atom, weight in zip(atoms, weights):
        ar = atom_row(atom[2], weight, len(row), delta_text)
        row = add_rows(row, ar)
    return row, weights


# ----------------------------------------------------- Levinson / Szego
def szego(row: list[mp.mpf], dps: int) -> dict:
    with mp.workdps(dps):
        c0 = row[0]
        if c0 <= 0:
            return {"ok": False, "alphas": [], "prediction": [],
                    "fail_k": 0, "fail_kind": "C0_NONPOSITIVE",
                    "attempted": mp.nan, "fail_den": mp.nan, "c0": c0}
        moments = [value / c0 for value in row]
        phi = [mp.mpf(1)]
        phi_star = [mp.mpf(1)]
        alphas: list[mp.mpf] = []
        prediction: list[mp.mpf] = []
        fail_k = -1
        fail_kind = ""
        attempted = mp.nan
        fail_den = mp.nan
        for k in range(len(moments) - 1):
            numerator = mp.fdot(phi, moments[1:k + 2])
            denominator = mp.fdot(phi_star, moments[0:k + 1])
            if denominator <= 0:
                fail_k = k
                fail_kind = "DEN_NONPOSITIVE"
                fail_den = denominator
                break
            alpha = numerator / denominator
            if abs(alpha) >= 1:
                fail_k = k
                fail_kind = "ALPHA_EXIT"
                attempted = alpha
                fail_den = denominator
                break
            alphas.append(alpha)
            prediction.append(denominator)
            zphi = [mp.mpf(0)] + phi
            phi_pad = phi_star + [mp.mpf(0)]
            phi = [zphi[j] - alpha * phi_pad[j] for j in range(k + 2)]
            phi_star = [phi_pad[j] - alpha * zphi[j] for j in range(k + 2)]
        return {"ok": fail_k < 0, "alphas": alphas, "prediction": prediction,
                "fail_k": fail_k, "fail_kind": fail_kind,
                "attempted": attempted, "fail_den": fail_den, "c0": c0}


def max_abs(alphas, count: int | None = None) -> float:
    values = alphas if count is None else alphas[:count]
    return max([abs(float(a)) for a in values], default=0.0)


def onset_index(u: float, delta: float) -> int:
    return int(math.floor(u / delta)) - 1


def frontier_entropy(alphas, width: int = W_FRONT) -> float:
    window = alphas[-width:]
    return -sum(math.log(1.0 - float(a) ** 2) for a in window)


def entropy_prefix_mp(alphas, count: int, dps: int) -> mp.mpf:
    with mp.workdps(dps):
        return mp.fsum(mp.log(1 - a ** 2) for a in alphas[:count])


def local_pre_onset_max(alphas, onset: int, width: int = W_FRONT) -> float:
    lo = max(0, onset - width)
    return max([abs(float(a)) for a in alphas[lo:onset]], default=0.0)


def dev_prefix(a_list, b_list, count: int) -> mp.mpf:
    n = min(count, len(a_list), len(b_list))
    with mp.workdps(DPS_BUILD):
        return max([abs(a_list[j] - b_list[j]) for j in range(n)],
                   default=mp.mpf(0))


def main() -> int:
    print("=" * 78)
    print("collective_rescue_probe  PRIME.SCREW.COLLECTIVE.RESCUE.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    section("A. FIREWALL + FROZEN LADDERS")
    fw_ok, fw_detail = firewall_audit()
    check_ward("A1 source-only AST firewall", fw_ok, fw_detail)
    logs = [math.log(p) for p in C1_PRIMES]
    min_gap = min(logs[i + 1] - logs[i] for i in range(len(logs) - 1))
    ladder_ok = (abs(N_WARD * DELTA - L_WARD) < 1e-12
                 and abs(N_C1 * DELTA - L_C1) < 1e-12
                 and abs(N_C1B * DELTA2 - L_C1) < 1e-12
                 and abs(N_C2 * DELTA - L_C2) < 1e-12
                 and abs(N_C2B * DELTA2 - L_C2) < 1e-12
                 and logs[-1] > L_C1 > logs[-2]
                 and (OFFSET_MAX + 2) * DELTA < min_gap)
    check_ward("A2 frozen ladders + sharpness precondition", ladder_ok,
               "n*delta==L all worlds; log37=%.4f>=L_C1; min missing-gap"
               " %.4f > (J+2)delta=%.3f"
               % (logs[-1], min_gap, (OFFSET_MAX + 2) * DELTA))
    setup_constants()

    atoms = prime_atoms(L_C2)
    primes_all = sorted({p for p, _m, _u, _w in atoms})
    print("  atoms(u<%.1f): %d over primes %d..%d" %
          (L_C2, len(atoms), primes_all[0], primes_all[-1]))

    base_g_800 = base_g_values(N_C2, DELTA_TEXT)
    base_row_800 = lag_row_from_g(base_g_800, DELTA_TEXT)
    base_row_600 = base_row_800[:N_C1]
    base_row_428 = base_row_800[:N_WARD]
    packets_428 = packet_rows(atoms, N_WARD, DELTA_TEXT)
    packets_600 = packet_rows(atoms, N_C1, DELTA_TEXT)
    packets_800 = packet_rows(atoms, N_C2, DELTA_TEXT)
    primes_sorted = sorted(packets_800)

    # ============================================================ WARDS
    section("B. ROUND-92 REGRESSION WARDS (delta=0.006, n=428, dps=100)")
    rung_428: dict[int, dict] = {}
    state = list(base_row_428)
    for k, p in enumerate(primes_sorted, start=1):
        if p > 13:
            break
        state = add_rows(state, packets_428[p])
        rung_428[k] = szego(state, DPS_WARD)
    full_428_row = list(base_row_428)
    for p in primes_sorted:
        full_428_row = add_rows(full_428_row, packets_428[p])
    full_428 = szego(full_428_row, DPS_WARD)
    full_428_lo = szego(full_428_row, DPS_MAIN)
    full_max = max_abs(full_428["alphas"])
    cross_dev = abs(full_max - max_abs(full_428_lo["alphas"]))
    check_ward("W1 full-stream regression + cross-dps",
               full_428["ok"] and abs(full_max - WARD_FULL_MAX) < 5e-5
               and cross_dev < 1e-12,
               "max|alpha|=%.6f (round92 %.6f); dps60 dev=%.2e"
               % (full_max, WARD_FULL_MAX, cross_dev))

    exits_now = tuple(rung_428[k]["fail_k"] for k in (1, 2, 3, 4))
    p5_max = max_abs(rung_428[5]["alphas"])
    check_ward("W2 truncation exits + P5 regression",
               exits_now == WARD_EXITS and rung_428[5]["ok"]
               and abs(p5_max - WARD_P5_MAX) < 5e-5,
               "exits=%s (round92 %s); P5 max=%.6f (round92 %.6f)"
               % (exits_now, WARD_EXITS, p5_max, WARD_P5_MAX))

    smooth_row_428 = add_rows(base_row_428,
                              tail_ramp_row(mp.mpf(0), N_WARD, DELTA_TEXT))
    smooth_428 = szego(smooth_row_428, DPS_WARD)
    atoms_ward = [a for a in atoms if float(a[2]) < L_WARD - 1e-14]
    scram_row_428, _w = scrambled_row(base_row_428, atoms_ward, DELTA_TEXT)
    scram_428 = szego(scram_row_428, DPS_WARD)
    check_ward("W3 SMOOTH/SCRARITH control regression",
               smooth_428["fail_k"] == WARD_SMOOTH_EXIT
               and scram_428["fail_k"] == WARD_SCRAM_EXIT
               and abs(float(smooth_428["attempted"]) - WARD_SMOOTH_ATT) < 1e-4
               and abs(float(scram_428["attempted"]) - WARD_SCRAM_ATT) < 1e-4,
               "SMOOTH exit=%d att=%.6f; SCRARITH exit=%d att=%.6f"
               % (smooth_428["fail_k"], float(smooth_428["attempted"]),
                  scram_428["fail_k"], float(scram_428["attempted"])))

    p5_alphas = rung_428[5]["alphas"]
    p5_argmax = max(range(len(p5_alphas)),
                    key=lambda j: abs(float(p5_alphas[j])))
    dev_p5_full = dev_prefix(p5_alphas, full_428["alphas"], 426)
    p4_alphas = rung_428[4]["alphas"]
    dev_p4_p5 = dev_prefix(p4_alphas, p5_alphas, 398)
    check_ward("W4 P5 frontier structure (causal identity)",
               p5_argmax == 426 and dev_p5_full < mp.mpf("1e-60")
               and dev_p4_p5 < mp.mpf("1e-60"),
               "argmax(P5)=%d alpha_426: P5=%.6f full=%.6f;"
               " dev(P5,full;j<426)=%s dev(P4,P5;j<398)=%s"
               % (p5_argmax, float(p5_alphas[426]),
                  float(full_428["alphas"][426]),
                  fmt_mp(dev_p5_full, 3), fmt_mp(dev_p4_p5, 3)))

    # ======================================================== C1 LADDER
    section("C1. SUPPORT-LAW LADDER (delta=0.006, n=600, L=3.6, dps=60)")
    rung_600: dict[int, dict] = {}
    state = list(base_row_600)
    rung_600[0] = szego(state, DPS_MAIN)
    for k in range(1, 12):
        state = add_rows(state, packets_600[C1_PRIMES[k - 1]])
        rung_600[k] = szego(state, DPS_MAIN)
    full_600_row = list(base_row_600)
    for p in primes_sorted:
        full_600_row = add_rows(full_600_row, packets_600[p])
    full_600 = szego(full_600_row, DPS_MAIN)

    onsets = {k: onset_index(logs[k], DELTA) for k in range(12)}
    offsets: dict[int, int] = {}
    table_rows = []
    r1 = None
    for k in range(12):
        res = rung_600[k]
        u_miss = logs[k]
        onset = onsets[k]
        if res["ok"]:
            table_rows.append((k, u_miss, onset, None, res))
            continue
        offsets[k] = res["fail_k"] - onset
        table_rows.append((k, u_miss, onset, res["fail_k"], res))
        if k == 1:
            r1 = res["fail_k"] * DELTA
    m_star = 2 * (math.exp(r1 / 2) - math.exp(logs[1] / 2))
    c_star = (r1 - logs[1]) * logs[1]
    print("  k | miss q | u_miss  | onset | exit | off | kind"
          "         | attempted  | M_exit  | preloc | resA   | resB    |"
          " resC    | D_front")
    res_a: dict[int, float] = {}
    res_b: dict[int, float] = {}
    res_c: dict[int, float] = {}
    d_front: dict[int, float] = {}
    for k, u_miss, onset, fail, res in table_rows:
        if fail is None:
            print("  %2d | %6d | %.5f | %5d |   SURVIVES window"
                  " (max|alpha|=%.6f, n_alpha=%d)"
                  % (k, C1_PRIMES[k], u_miss, onset,
                     max_abs(res["alphas"]), len(res["alphas"])))
            continue
        r_exit = fail * DELTA
        res_a[k] = r_exit - onset * DELTA
        res_b[k] = r_exit - 2 * math.log(math.exp(u_miss / 2) + m_star / 2)
        res_c[k] = r_exit - (u_miss + c_star / u_miss)
        m_exit = 2 * (math.exp(r_exit / 2) - math.exp(u_miss / 2))
        preloc = local_pre_onset_max(res["alphas"], onset)
        d_front[k] = frontier_entropy(res["alphas"])
        att = (float(res["attempted"])
               if res["fail_kind"] == "ALPHA_EXIT" else float("nan"))
        print("  %2d | %6d | %.5f | %5d | %4d | %3d | %-12s | %+9.4f"
              "  | %.5f | %.4f | %+.4f | %+.5f | %+.5f | %.5f"
              % (k, C1_PRIMES[k], u_miss, onset, fail, offsets[k],
                 res["fail_kind"], att, m_exit, preloc,
                 res_a[k], res_b[k], res_c[k], d_front[k]))
    print("  law A (support onset, calibration-free): max|res| k=2..10"
          " = %.5f" % max(abs(res_a[k]) for k in res_a if k >= 2))
    print("  law B (constant missing mass M*=%.5f):    max|res| k=2..10"
          " = %.5f" % (m_star, max(abs(res_b[k]) for k in res_b if k >= 2)))
    print("  law C (Mertens-like c*=%.5f):             max|res| k=2..10"
          " = %.5f" % (c_star, max(abs(res_c[k]) for k in res_c if k >= 2)))

    causal_ok = all(rung_600[k]["fail_k"] >= onsets[k]
                    for k in offsets)
    invariance_ok = all(rung_600[k]["fail_k"] == rung_428[k]["fail_k"]
                        for k in (1, 2, 3, 4))
    check_ward("W5 causality lower bound + n/dps invariance",
               causal_ok and invariance_ok,
               "all exits >= onset; rung1..4 exits equal at (428,dps100)"
               " and (600,dps60)")

    exits_16 = all(k in offsets for k in range(1, 11))
    l1 = gate_law("L1 offsets J(k) in [0,%d], k=1..10" % OFFSET_MAX,
                  exits_16 and all(0 <= offsets[k] <= OFFSET_MAX
                                   for k in range(1, 11)),
                  "offsets=%s" % [offsets.get(k) for k in range(1, 11)])
    l2 = gate_law("L2 survivor rule (rung 11, onset beyond window)",
                  rung_600[11]["ok"] and onsets[11] > N_C1 - 2,
                  "onset(log37)=%d > %d; rung11 max|alpha|=%.6f"
                  % (onsets[11], N_C1 - 2, max_abs(rung_600[11]["alphas"])))
    l3 = gate_law("L3 rung 0 exits inside missing-2 span",
                  (not rung_600[0]["ok"])
                  and onsets[0] <= rung_600[0]["fail_k"] < onsets[1],
                  "exit=%d in [%d,%d); r=%.3f (log2=%.4f, log3=%.4f)"
                  % (rung_600[0]["fail_k"], onsets[0], onsets[1],
                     rung_600[0]["fail_k"] * DELTA, logs[0], logs[1]))

    off_list = [offsets[k] for k in range(1, 11)]
    pre_list = [local_pre_onset_max(rung_600[k]["alphas"], onsets[k])
                for k in range(1, 11)]
    corr = float(np.corrcoef(np.array(off_list, dtype=float),
                             np.array(pre_list, dtype=float))[0, 1])
    print("  offset carrier: Pearson(offset, pre-onset local max|alpha|)"
          " = %+.4f" % corr)

    dev_11_full = dev_prefix(rung_600[11]["alphas"], full_600["alphas"],
                             N_C1)
    s180 = [entropy_prefix_mp(rung_600[k]["alphas"], J0_PREFIX, DPS_MAIN)
            for k in range(1, 12)]
    s180_dev = max(s180) - min(s180)
    check_ward("W6 rung11==full600 + K1 prefix-entropy constancy",
               rung_600[11]["ok"] == full_600["ok"]
               and dev_11_full < mp.mpf("1e-60")
               and s180_dev < mp.mpf("1e-60"),
               "dev(rung11,full600)=%s; K1(j<%d)=%s, spread=%s"
               % (fmt_mp(dev_11_full, 3), J0_PREFIX,
                  fmt_mp(s180[0], 8), fmt_mp(s180_dev, 3)))

    # ------------------------------------------------ C1 mesh screen
    section("C1b. MESH SCREEN (delta=0.008, n=450, L=3.6, dps=60)")
    base_g_2 = base_g_values(N_C2B, DELTA2_TEXT)
    base_row_2 = lag_row_from_g(base_g_2, DELTA2_TEXT)
    packets_450 = packet_rows(atoms, N_C1B, DELTA2_TEXT)
    onsets2 = {k: onset_index(logs[k], DELTA2) for k in range(5)}
    state = list(base_row_2[:N_C1B])
    rung_2: dict[int, dict] = {0: szego(state, DPS_MAIN)}
    for k in range(1, 5):
        state = add_rows(state, packets_450[C1_PRIMES[k - 1]])
        rung_2[k] = szego(state, DPS_MAIN)
    offsets2 = {}
    for k in range(5):
        res = rung_2[k]
        if res["ok"]:
            print("  k=%d SURVIVES (unexpected)" % k)
            continue
        offsets2[k] = res["fail_k"] - onsets2[k]
        print("  k=%d onset=%3d exit=%3d off=%2d r=%.3f kind=%s"
              % (k, onsets2[k], res["fail_k"], offsets2[k],
                 res["fail_k"] * DELTA2, res["fail_kind"]))
    causal2 = all(k in offsets2 and rung_2[k]["fail_k"] >= onsets2[k]
                  for k in range(5))
    check_ward("W5b mesh-world causality lower bound", causal2,
               "all delta=0.008 exits >= onset")
    l4 = gate_law("L4 mesh-robust offsets J(k) in [0,%d], k=1..4"
                  % OFFSET_MAX,
                  all(k in offsets2 and 0 <= offsets2[k] <= OFFSET_MAX
                      for k in range(1, 5)),
                  "offsets(delta=0.008)=%s"
                  % [offsets2.get(k) for k in range(1, 5)])

    # ================================================================ C2
    section("C2. COMPLETED-STREAM MARGIN (all packets; two mesh worlds)")
    full_800_row = list(base_row_800)
    for p in primes_sorted:
        full_800_row = add_rows(full_800_row, packets_800[p])
    full_800 = szego(full_800_row, DPS_MAIN)
    packets_600b = packet_rows(atoms, N_C2B, DELTA2_TEXT)
    full_2_row = list(base_row_2)
    for p in sorted(packets_600b):
        full_2_row = add_rows(full_2_row, packets_600b[p])
    full_2 = szego(full_2_row, DPS_MAIN)

    worlds = (("delta=0.006 n=800", full_800, DELTA, N_C2 - 2),
              ("delta=0.008 n=600", full_2, DELTA2, N_C2B - 2))
    comfort_ok = True
    for label, res, dl, last_idx in worlds:
        if not res["ok"]:
            comfort_ok = False
            print("  %s: EXITED at r=%.3f (%s)"
                  % (label, res["fail_k"] * dl, res["fail_kind"]))
            continue
        depths = list(DEPTHS_COMMON) + [last_idx * dl]
        idxs = [int(round(d / dl)) for d in depths]
        print("  %s:" % label)
        print("    depth  | cum max|alpha| | band max | margin")
        prev = 0
        band_mids = []
        band_maxs = []
        for d, i in zip(depths, idxs):
            i = min(i, len(res["alphas"]))
            cum = max_abs(res["alphas"], i)
            band = max_abs(res["alphas"][prev:i])
            band_mids.append((prev + i) / 2 * dl)
            band_maxs.append(band)
            print("    %.3f  | %.6f       | %.6f | %.6f"
                  % (d, cum, band, 1 - cum))
            prev = i
        final_cum = max_abs(res["alphas"])
        slope = float(np.polyfit(band_mids, band_maxs, 1)[0])
        logm = [math.log(1 - b) for b in band_maxs]
        slope_log = float(np.polyfit(band_mids, logm, 1)[0])
        print("    band-max slope=%.5f /unit depth;"
              " dlog(1-bandmax)/dr=%.5f" % (slope, slope_log))
        comfort_ok &= final_cum < COMFORT_BAR
    l7 = gate_law("L7 C2 comfort bar (cum max < %.2f both worlds)"
                  % COMFORT_BAR, comfort_ok,
                  "0.006-world max=%.6f, 0.008-world max=%.6f"
                  % (max_abs(full_800["alphas"]) if full_800["ok"] else 1.0,
                     max_abs(full_2["alphas"]) if full_2["ok"] else 1.0))
    print("  MEASUREMENT ONLY: finite-prefix margin in the screw"
          " coordinate; NOT evidence for the all-depth quantifier.")

    # ================================================================ C3
    section("C3. RESCUE DECOMPOSITION + LYAPUNOV CANDIDATES (n=600)")
    atom3 = next(a for a in atoms if a[0] == 3 and a[1] == 1)
    atom9 = next(a for a in atoms if a[0] == 3 and a[1] == 2)
    row_31 = add_rows(base_row_600, packets_600[2],
                      atom_row(atom3[2], atom3[3], N_C1, DELTA_TEXT))
    row_32 = add_rows(base_row_600, packets_600[2],
                      atom_row(atom9[2], atom9[3], N_C1, DELTA_TEXT))
    res_31 = szego(row_31, DPS_MAIN)
    res_32 = szego(row_32, DPS_MAIN)
    onset5 = onset_index(math.log(5), DELTA)
    l5 = gate_law("L5 {2}+3^1 exit lands in log-5 onset window",
                  (not res_31["ok"])
                  and 0 <= res_31["fail_k"] - onset5 <= OFFSET_MAX,
                  "exit=%d, onset(log5)=%d, off=%d, r=%.3f"
                  % (res_31["fail_k"], onset5,
                     res_31["fail_k"] - onset5, res_31["fail_k"] * DELTA))
    l6 = gate_law("L6 {2}+3^2 exit index unchanged vs rung 1",
                  (not res_32["ok"])
                  and res_32["fail_k"] == rung_600[1]["fail_k"],
                  "exit=%d == rung1 exit=%d (atom 9 sits at lag %d,"
                  " causally invisible)"
                  % (res_32["fail_k"], rung_600[1]["fail_k"],
                     int(math.log(9) // DELTA)))

    p11_row = packets_428[11]
    touched = [d for d, v in enumerate(p11_row) if v != 0]
    print("  p=11 packet inside L=2.568: single atom u=log11=%.5f,"
          " touched lags=%s (banded Toeplitz, displacement rank<=2"
          " by structure)" % (math.log(11), touched))
    print("  P4 exit: k=%d attempted=%.4f; after p=11, alpha_398..403 ="
          % (rung_428[4]["fail_k"], float(rung_428[4]["attempted"])))
    print("    %s" % ["%+.5f" % float(a) for a in p5_alphas[398:404]])
    print("  => the 'rescue' rewrites ONLY j>=398; P4==P5 for j<398"
          " (ward W4); nothing collective is transported.")

    d_exit = {k: d_front[k] for k in sorted(d_front)}
    frac8 = {}
    for k in sorted(d_exit):
        alphas_k = rung_600[k]["alphas"]
        d8 = -sum(math.log(1.0 - float(a) ** 2) for a in alphas_k[-8:])
        frac8[k] = d8 / d_exit[k] if d_exit[k] > 0 else float("nan")
    seq = [d_exit[k] for k in range(1, 11)]
    mono_inc = all(seq[i + 1] > seq[i] for i in range(len(seq) - 1))
    mono_dec = all(seq[i + 1] < seq[i] for i in range(len(seq) - 1))
    print("  K2 frontier entropy D_k (last %d lags) and last-8 fraction:"
          % W_FRONT)
    for k in range(1, 11):
        print("    k=%2d  D=%.5f  frac(last8)=%.3f" % (k, d_exit[k],
                                                       frac8[k]))
    print("  K2 monotone increasing=%s decreasing=%s (over k=1..10)"
          % (mono_inc, mono_dec))
    print("  K3 final prediction error at exit:")
    for k in range(1, 11):
        print("    k=%2d  den=%.6e" % (k, float(rung_600[k]["fail_den"])))
    print("  TYPED KILL (causality): any functional of a fixed alpha")
    print("  prefix is bit-identical to the full stream before onset (K1")
    print("  spread %s) and is the blow-up itself after onset (last-8"
          % fmt_mp(s180_dev, 2))
    print("  fraction above); no packet-addition Lyapunov functional on")
    print("  fixed windows can discriminate truncated from completed")
    print("  streams except by reading the exit it should predict.")

    # ================================================================ C4
    section("C4. CONTROLS (n=600, dps=60)")
    ss_row = add_rows(base_row_600,
                      tail_ramp_row(mp.log(2), N_C1, DELTA_TEXT))
    ss = szego(ss_row, DPS_MAIN)
    mr_row = add_rows(base_row_600, packets_600[2], packets_600[3],
                      packets_600[5], packets_600[7],
                      tail_ramp_row(mp.log(11), N_C1, DELTA_TEXT))
    mr = szego(mr_row, DPS_MAIN)
    onset13 = onset_index(math.log(13), DELTA)

    def describe(name: str, res: dict, dl: float) -> str:
        if res["ok"]:
            return ("%-22s SURVIVES window, max|alpha|=%.6f, D_front=%.5f"
                    % (name, max_abs(res["alphas"]),
                       frontier_entropy(res["alphas"])))
        att = (float(res["attempted"])
               if res["fail_kind"] == "ALPHA_EXIT" else float("nan"))
        return ("%-22s exit=%4d r=%.3f kind=%s attempted=%+.4f"
                " D_front=%.5f"
                % (name, res["fail_k"], res["fail_k"] * dl,
                   res["fail_kind"], att,
                   frontier_entropy(res["alphas"])))

    print("  " + describe("SMOOTH (u0=0):", smooth_428, DELTA))
    print("  " + describe("SCRARITH:", scram_428, DELTA))
    print("  " + describe("SMOOTH-SHIFTED (log2):", ss, DELTA))
    print("  " + describe("MASS-RESTORED {2..7}:", mr, DELTA))
    print("  " + describe("TRUNC k=0 (arch):", rung_600[0], DELTA))
    print("  exit-pattern comparison: truncation offsets are %d..%d lags"
          % (min(off_list), max(off_list)))
    print("  after onset; SMOOTH needs %d lags from its (u=0) defect"
          " onset;" % smooth_428["fail_k"])
    mr_rescues = mr["ok"] or mr["fail_k"] > onset13 + OFFSET_MAX
    if mr_rescues:
        mr_r = (N_C1 - 2) * DELTA if mr["ok"] else mr["fail_k"] * DELTA
        mr_note = ("mass-without-atoms carries the stream past the log-13"
                   " onset (to r=%.3f): the rescue is MASS bookkeeping,"
                   " measure-generic at this mesh" % mr_r)
    else:
        mr_note = ("mass-without-atoms FAILS at r=%.3f (< log13 onset"
                   " +%d): in-window survival needs the exact atomic"
                   " weights (consistent with SCRARITH r=0.744); the exit"
                   " LAW is support bookkeeping, the survival margin is"
                   " arithmetic" % (mr["fail_k"] * DELTA, OFFSET_MAX))
    print("  MASS-RESTORED typing: %s" % mr_note)
    if ss["ok"]:
        ss_note = ("support-corrected density survives the whole window:"
                   " the pre-window phenomenon is measure-generic"
                   " (support+mass suffice)")
    else:
        ss_note = ("support-corrected density still dies at r=%.3f"
                   " (SMOOTH died 0.264, SCRARITH 0.744): support fixes"
                   " the first death, atoms/weights are needed beyond"
                   % (ss["fail_k"] * DELTA))
    print("  SMOOTH-SHIFTED typing: %s" % ss_note)

    # ======================================================== ADJUDICATION
    section("D. ADJUDICATION")
    wall = time.time() - T0
    check_ward("A3 runtime", wall <= RUNTIME_BAR,
               "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))
    instrument_ok = all(ok for _n, ok, _d in WARDS)
    support_ok = l1 and l2 and l3 and l4 and l5 and l6
    n_ward = sum(1 for _n, ok, _d in WARDS if ok)
    n_law = sum(1 for _n, ok, _d in LAWS if ok)

    controls_d = [frontier_entropy(res["alphas"])
                  for res in (smooth_428, scram_428, ss, mr)
                  if not res["ok"]]
    truth_lo, truth_hi = min(seq), max(seq)
    controls_break = all(d < truth_lo or d > truth_hi for d in controls_d)
    lyapunov_candidate = ((mono_inc or mono_dec) and controls_break)

    if support_ok:
        verdict = (
            "COLLECTIVE-IS-SUPPORT(law: exact causal lower bound"
            " fail>=onset(log p_{k+1}); measured upper offset <= %d lags"
            " = %.3f depth on k=1..10 at delta=0.006 and k=1..4 at"
            " delta=0.008; survivor rule = onset beyond window, rung 11"
            " bit-identical to the full stream; the 'rescue' is the"
            " single boundary atom (L5/L6), not the packet and not a"
            " prime conspiracy; %s)"
            % (OFFSET_MAX, OFFSET_MAX * DELTA,
               "mass-restored control rescues => measure-generic"
               if mr_rescues else
               "mass-restored control fails => survival needs exact"
               " arithmetic weights"))
    elif (all(k in offsets for k in range(1, 11))
          and max(off_list) <= LAWFOUND_OFFSET_CAP):
        verdict = (
            "COLLECTIVE-LAW-FOUND(exits stay support-anchored but the"
            " offset exceeds the %d-lag bar: offsets=%s, carrier"
            " correlation with pre-onset level %+.3f)"
            % (OFFSET_MAX, off_list, corr))
    elif lyapunov_candidate:
        verdict = (
            "COLLECTIVE-LYAPUNOV(candidate: frontier entropy D_k monotone"
            " on truth (inc=%s dec=%s) and broken on all exiting"
            " controls; remaining: show D controls the exit independently"
            " of the support prediction)" % (mono_inc, mono_dec))
    else:
        verdict = (
            "COLLECTIVE-UNEXPLAINED(excluded: support-onset law at bar"
            " %d lags (offsets=%s), survivor rule=%s, boundary-atom"
            " rescue=%s/%s, constant-missing-mass law maxres=%.4f,"
            " Mertens-like law maxres=%.4f, fixed-prefix Lyapunov killed"
            " by causality)"
            % (OFFSET_MAX, [offsets.get(k) for k in range(1, 11)],
               rung_600[11]["ok"], l5, l6,
               max(abs(res_b[k]) for k in res_b if k >= 2),
               max(abs(res_c[k]) for k in res_c if k >= 2)))

    print("\n" + "=" * 78)
    print("WARDS %d/%d PASS   LAW GATES %d/%d PASS   runtime %.1f s"
          % (n_ward, len(WARDS), n_law, len(LAWS), wall))
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    if not instrument_ok:
        print("VERDICT: INSTRUMENT-EDGE (failed ward; no mathematical"
              " verdict)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    print("VERDICT: %s" % verdict)
    print("C2 MARGIN: measurement only, comfort bar %s; the all-depth"
          " statement remains localized Weil positivity in new currency."
          % ("held" if l7 else "NOT held"))
    print("NO RH CLAIM. NO ALL-DEPTH POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
