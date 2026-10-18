#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_geodesic_infrastructure_probe -- r642  GEOM.SEAM.GEODESIC.01

The continuous / dynamical / iterative processes of TFPT live on fixed
spaces (R^8 and the E8 roots, a 3x3 Markov kernel, the modular surface
with the seam Re(tau) = 0 and the mu4 fixed point tau = i).  Applied to an
integer N = p q, the ONE such process whose state depends on N is the
geodesic flow on the modular surface at discriminant 4N -- classically the
Gauss reduction cycle of indefinite binary quadratic forms, i.e. the
continued fraction of sqrt(N).  This probe writes the factoring problem in
exactly that TFPT geometry and measures what the flow can and cannot do.

  S1  SEAM IDENTITIES (exact).  Ambiguous forms of discriminant 4N are the
      closed geodesics that cross the seam Re(tau) = 0 perpendicularly:
      (1, 0, -N) crosses at i sqrt(N) (trivial factorisation), (p, 0, -q)
      crosses at i sqrt(q/p) (the factorisation).  The mu4 clock
      S: tau -> -1/tau swaps (p,0,-q) <-> (q,0,-p).  The hyperbolic distance
      along the seam between the trivial and the non-trivial crossing is
      exactly log p -- the Weil atom of p sits on the seam.
  S2  THE FLOW (Gauss reduction = continued fraction of sqrt N) on random
      balanced semiprimes, 16..32 bit: period length ell(N) of the principal
      cycle (= regulator scale), its palindromic symmetry, and the position
      of the second ambiguous form at ell/2 -- the factorisation is the
      MIDPOINT of the closed geodesic when it lies on the principal cycle.
      Scaling exponent of median ell vs N (expected ~ 1/2).
  S3  THE SHORTCUT THAT EXISTS: Shanks' SQUFOF -- run the same flow until a
      square form appears (~ N^{1/4} steps), take its square root (jump to a
      cycle of an order-2 class), run to ITS symmetry point.  Success rate
      and step-count exponent (expected ~ 1/4).
  S4  THE SHORTCUT THAT WOULD BE NEEDED: reaching the midpoint in
      poly(log N) requires the period (the regulator R): with R known the
      midpoint is O(log R) giant steps away in the infrastructure (Shanks;
      Lenstra 1982: factoring in O(N^{1/5+eps}) under GRH via the regulator;
      Hallgren 2002: quantum poly-time regulator = the continuous analogue
      of Shor's order finding).  Recorded as literature, not measured.

Decision: GEODESIC_FLOW_IS_SQUFOF (exponents 1/2 and 1/4 confirmed; the
midpoint is the factorisation; the shortcut is the regulator, whose
classical cost is exponential, whose quantum cost is polynomial) /
ANOMALY (exponents off) / LEAK (midpoint reached in o(N^{1/4}) steps).

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: no factoring claim; no RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from math import gcd, isqrt
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROUND = 642
SEED = 642202609
CONTRACT = "GEOM.SEAM.GEODESIC.01"
FENCE = "Exploration; no factoring claim; no RH claim"
TAG = "r642"
RESULT_JSON = HERE / "seam_geodesic_infrastructure_result.json"

BIT_SIZES = (16, 20, 24, 28, 32)
N_PER_SIZE = 24
PERIOD_CAP = 3_000_000
SQUFOF_STEP_CAP = 200_000
EXP_PERIOD, EXP_SQUFOF, EXP_TOL = 0.5, 0.25, 0.13
DECISIONS = ("GEODESIC_FLOW_IS_SQUFOF", "ANOMALY", "LEAK")

CHECKS: list[tuple[str, bool]] = []


def emit(s: str = "") -> None:
    print(s)


def section(title: str) -> None:
    emit("")
    emit("== " + title)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    emit("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    return bool(ok)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_semiprime(rng: np.random.Generator, bits: int) -> tuple[int, int, int]:
    half = bits // 2
    while True:
        p = int(rng.integers(1 << (half - 1), 1 << half)) | 1
        q = int(rng.integers(1 << (half - 1), 1 << half)) | 1
        if p != q and is_prime(p) and is_prime(q):
            N = p * q
            if isqrt(N) ** 2 != N:
                return N, min(p, q), max(p, q)


# --- the flow: continued fraction of sqrt(N) = Gauss reduction on the principal cycle -----
def cf_period(N: int, cap: int) -> dict:
    """d_k sequence of sqrt(N) (the |Q_k| of the principal cycle of discriminant 4N)."""
    a0 = isqrt(N)
    m, d, a = 0, 1, a0
    ds = [1]
    partials = [a0]
    k = 0
    while True:
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        k += 1
        ds.append(d)
        partials.append(a)
        if d == 1:
            break
        if k >= cap:
            return {"ell": None, "capped": True}
    ell = k
    inner = partials[1:ell]
    palindrome = inner == inner[::-1]
    # ambiguous forms sit where d_k = d_{ell-k}; midpoint k = ell/2 (even ell) or the pair around it (odd)
    mid = ell // 2
    mid_d = ds[mid]
    factor = None
    if ell % 2 == 0:
        g = gcd(mid_d, N)
        if 1 < g < N:
            factor = g
        elif mid_d % 2 == 0:
            g = gcd(mid_d // 2, N)
            if 1 < g < N:
                factor = g
    return {"ell": ell, "capped": False, "palindrome": palindrome, "mid_d": mid_d,
            "mid_divides_2N": (2 * N) % mid_d == 0, "midpoint_factor": factor,
            "symmetric": all(ds[k] == ds[ell - k] for k in range(ell + 1))}


def squfof(N: int, cap: int) -> dict:
    """Shanks' square form factorisation, multiplier 1; counts forward steps (~N^{1/4})."""
    P0 = isqrt(N)
    Pprev, Qprev, Q = P0, 1, N - P0 * P0
    steps = 0
    squares_tried = 0
    tried_roots: set[int] = set()
    i = 1
    while steps < cap:
        b = (P0 + Pprev) // Q
        P = b * Q - Pprev
        Qnext = Qprev + b * (Pprev - P)
        Pprev, Qprev, Q = P, Q, Qnext
        i += 1
        steps += 1
        if i % 2 == 0:
            r = isqrt(Q)
            if r * r == Q and r not in tried_roots:
                tried_roots.add(r)
                squares_tried += 1
                # second cycle: square root form
                b0 = (P0 - Pprev) // r
                P2 = b0 * r + Pprev
                Q2prev = r
                Q2 = (N - P2 * P2) // r
                steps2 = 0
                while steps2 < cap:
                    b = (P0 + P2) // Q2
                    Pnew = b * Q2 - P2
                    Qnew = Q2prev + b * (P2 - Pnew)
                    steps2 += 1
                    if Pnew == P2:
                        break
                    Q2prev, Q2, P2 = Q2, Qnew, Pnew
                for cand in (Q2, Q2 // 2 if Q2 % 2 == 0 else 1, Q2prev, Q2prev // 2 if Q2prev % 2 == 0 else 1):
                    g = gcd(cand, N)
                    if 1 < g < N:
                        return {"factor": g, "forward_steps": steps, "second_steps": steps2, "squares_tried": squares_tried}
    return {"factor": None, "forward_steps": steps, "second_steps": 0, "squares_tried": squares_tried}


def fit_exponent(Ns: list[float], ys: list[float]) -> float:
    x = np.log(np.array(Ns, dtype=float))
    y = np.log(np.array(ys, dtype=float))
    return float(np.polyfit(x, y, 1)[0])


# --- sections ---------------------------------------------------------------------
def s1_seam_identities() -> dict:
    section("S1  seam identities: ambiguous forms of discriminant 4N are the seam crossings")
    p, q = 1009, 1013
    N = p * q
    # geodesic of the form (a, b, c): semicircle with endpoints the roots of a x^2 + b x + c = 0
    def crossing_height(a: int, b: int, c: int) -> float:
        disc = b * b - 4 * a * c
        assert disc > 0 and b == 0
        return math.sqrt(-c / a)
    h_triv = crossing_height(1, 0, -N)
    h_fact = crossing_height(p, 0, -q)
    check("S1a-trivial-crossing-at-i-sqrtN", abs(h_triv - math.sqrt(N)) < 1e-9)
    check("S1b-factor-crossing-at-i-sqrt(q/p)", abs(h_fact - math.sqrt(q / p)) < 1e-12)
    # mu4 clock S: tau -> -1/tau acts on forms by (a, b, c) -> (c, -b, a); on the seam y -> 1/y
    S_form = (-q, 0, p)
    check("S1c-mu4-clock-swaps-the-two-factor-crossings",
          crossing_height(-S_form[0], 0, -S_form[2]) == math.sqrt(p / q) and abs(1.0 / h_fact - math.sqrt(p / q)) < 1e-12,
          "(p,0,-q) <-> (q,0,-p), i sqrt(q/p) <-> i sqrt(p/q)")
    seam_dist = abs(math.log(h_triv) - math.log(h_fact))
    check("S1d-seam-distance-between-crossings-is-log-p", abs(seam_dist - math.log(p)) < 1e-9,
          "d_hyp(i sqrt N, i sqrt(q/p)) = log p = the Weil atom of p; the flow cannot slide along the seam")
    disc_ok = all(b * b - 4 * a * c == 4 * N for a, b, c in ((1, 0, -N), (p, 0, -q), (q, 0, -p)))
    check("S1e-all-three-have-discriminant-4N", disc_ok)
    return {"p": p, "q": q, "h_trivial": h_triv, "h_factor": h_fact, "seam_distance": seam_dist}


def s2_flow_period(rng: np.random.Generator, n_per_size: int) -> dict:
    section("S2  the flow: period ell of the principal cycle (continued fraction of sqrt N) and its midpoint")
    per_size: dict[int, dict] = {}
    midpoint_hits = 0
    even_periods = 0
    n_total = 0
    sym_ok = True
    pal_ok = True
    mid_div_ok = True
    for bits in BIT_SIZES:
        ells = []
        capped = 0
        for _ in range(n_per_size):
            N, p, q = random_semiprime(rng, bits)
            r = cf_period(N, PERIOD_CAP)
            if r["capped"]:
                capped += 1
                continue
            n_total += 1
            ells.append(r["ell"])
            sym_ok &= r["symmetric"]
            pal_ok &= r["palindrome"]
            if r["ell"] % 2 == 0:
                even_periods += 1
                mid_div_ok &= r["mid_divides_2N"]
                if r["midpoint_factor"] in (p, q):
                    midpoint_hits += 1
        per_size[bits] = {"median_ell": float(np.median(ells)) if ells else float("nan"),
                          "max_ell": int(max(ells)) if ells else -1, "capped": capped, "n": len(ells)}
        emit("  %2d bit: median ell = %9.0f  max = %9d  capped = %d  (sqrt N ~ %.0f)"
             % (bits, per_size[bits]["median_ell"], per_size[bits]["max_ell"], capped, 2 ** (bits / 2)))
    check("S2a-cycle-is-symmetric-d_k=d_(ell-k)", sym_ok, "the closed geodesic is its own mirror image")
    check("S2b-partial-quotients-palindromic", pal_ok)
    check("S2c-midpoint-of-even-period-divides-2N", mid_div_ok,
          "even ell: %d/%d; the second ambiguous form sits exactly at ell/2" % (even_periods, n_total))
    frac = midpoint_hits / max(even_periods, 1)
    emit("  midpoint of the principal cycle yields a nontrivial factor for %d/%d even-period N (%.2f); "
         "otherwise the non-trivial ambiguous class is not principal (order-2 class elsewhere)" % (midpoint_hits, even_periods, frac))
    check("S2d-midpoint-is-the-factorisation-when-principal", midpoint_hits > 0 and frac > 0.15,
          "the factorisation IS a point of the flow, at distance ell/2")
    sizes = [b for b in BIT_SIZES if math.isfinite(per_size[b]["median_ell"])]
    expo = fit_exponent([2.0 ** b for b in sizes], [per_size[b]["median_ell"] for b in sizes])
    check("S2e-period-scales-like-N^(1/2)", abs(expo - EXP_PERIOD) < EXP_TOL,
          "fitted exponent %.3f (regulator ~ sqrt N up to logs): the distance to the midpoint is exponential in log N" % expo)
    return {"per_size": {str(k): v for k, v in per_size.items()}, "exponent": expo,
            "midpoint_hits": midpoint_hits, "even_periods": even_periods, "n_total": n_total}


def s3_squfof(rng: np.random.Generator, n_per_size: int) -> dict:
    section("S3  the shortcut that exists: SQUFOF (square form -> square root -> symmetry point)")
    per_size: dict[int, dict] = {}
    for bits in BIT_SIZES:
        fwd, ok = [], 0
        for _ in range(n_per_size):
            N, p, q = random_semiprime(rng, bits)
            r = squfof(N, SQUFOF_STEP_CAP)
            if r["factor"] in (p, q):
                ok += 1
                fwd.append(r["forward_steps"] + r["second_steps"])
        per_size[bits] = {"success": ok / n_per_size, "median_steps": float(np.median(fwd)) if fwd else float("nan")}
        emit("  %2d bit: success %5.2f  median total steps = %8.0f  (N^(1/4) ~ %.0f)"
             % (bits, per_size[bits]["success"], per_size[bits]["median_steps"], 2 ** (bits / 4)))
    check("S3a-squfof-success-rate", all(v["success"] >= 0.75 for v in per_size.values()),
          "multiplier 1 only; failures are the known trivial-square-form cases")
    sizes = [b for b in BIT_SIZES if math.isfinite(per_size[b]["median_steps"])]
    expo = fit_exponent([2.0 ** b for b in sizes], [per_size[b]["median_steps"] for b in sizes])
    check("S3b-squfof-steps-scale-like-N^(1/4)", abs(expo - EXP_SQUFOF) < EXP_TOL,
          "fitted exponent %.3f: the square-form jump halves the exponent, from the period 1/2 to 1/4, and stops there" % expo)
    return {"per_size": {str(k): v for k, v in per_size.items()}, "exponent": expo}


def s4_infrastructure_statement() -> dict:
    section("S4  the shortcut that would be needed: the period (regulator) of the flow")
    emit("  With the period R known, the midpoint is O(log R) giant steps away (Shanks' infrastructure, distance is additive")
    emit("  under composition).  Computing R classically: Lenstra 1982 O(N^{1/5+eps}) under GRH, class-group methods L[1/2].")
    emit("  Computing R quantumly: Hallgren 2002, poly(log N) -- the continuous-period analogue of Shor's order finding.")
    emit("  So the TFPT geodesic picture reproduces the known ladder exactly: 1/2 (naive flow) -> 1/4 (SQUFOF) -> 1/5 (GRH,")
    emit("  regulator) -> L[1/2] (relations) -> L[1/3] (NFS, a DIFFERENT N-dependent geometry) -> poly (quantum period).")
    check("S4-ladder-recorded", True, "literature, not measured here")
    return {"ladder": ["1/2 flow", "1/4 SQUFOF", "1/5 Lenstra-GRH", "L[1/2] class group", "L[1/3] NFS", "poly Hallgren/Shor"]}


def decide(res: dict) -> tuple[str, str]:
    e2, e3 = res["s2"]["exponent"], res["s3"]["exponent"]
    if e3 < EXP_SQUFOF - EXP_TOL and res["s3"]["per_size"][str(BIT_SIZES[-1])]["success"] >= 0.75:
        return "LEAK", "SQUFOF-type steps grow slower than N^(1/4): %.3f" % e3
    if abs(e2 - EXP_PERIOD) >= EXP_TOL or abs(e3 - EXP_SQUFOF) >= EXP_TOL:
        return "ANOMALY", "exponents period %.3f (exp 0.5), squfof %.3f (exp 0.25)" % (e2, e3)
    return "GEODESIC_FLOW_IS_SQUFOF", ("the geodesic flow of discriminant 4N reaches the factorisation at its midpoint after ~N^(1/2) "
                                       "steps (exp %.2f); the square-form jump gives N^(1/4) (exp %.2f); every further shortcut is the "
                                       "period of the flow (regulator), exponential classically, polynomial only by quantum period finding"
                                       % (e2, e3))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    n_per_size = 6 if args.smoke else N_PER_SIZE
    wall0 = time.time()
    rng = np.random.default_rng(SEED)
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))
    res = {"s1": s1_seam_identities(), "s2": s2_flow_period(rng, n_per_size), "s3": s3_squfof(rng, n_per_size),
           "s4": s4_infrastructure_statement()}
    verdict, why = decide(res)
    check("G-verdict-enum", verdict in DECISIONS, verdict)
    payload = {"contract": CONTRACT, "tag": TAG, "round": ROUND, "fence": FENCE, "verdict": verdict, "why": why,
               "result": json.loads(json.dumps(res, default=float)), "gates": {n: ok for n, ok in CHECKS}}
    payload["result_sha"] = payload_sha(payload)
    payload["file_sha256"] = file_sha256()
    if not args.smoke:
        RESULT_JSON.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    emit("")
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, len(CHECKS)))
    emit("FILE_SHA256 %s" % payload["file_sha256"])
    emit("RESULT_SHA %s" % payload["result_sha"])
    emit("WALL_S %.3f" % (time.time() - wall0))
    emit("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "GATE_FAILURES " + ",".join(n for n, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
