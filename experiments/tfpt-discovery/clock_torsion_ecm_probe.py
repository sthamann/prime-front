#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""clock_torsion_ecm_probe -- r641  CLOCK.CM.ECM.01

The one factoring lane with a genuinely TFPT-specific ingredient: the
compiler clocks (mu4 of order 4, the order-12 compiler clock, the 48-cycle,
the Coxeter clock of order 30) read as *torsion subgroups of elliptic
curves*, which is exactly how "clocks" enter the only known sub-exponential
factoring family that uses group structure -- Lenstra's ECM.  Torsion over Q
forces divisibility of #E(F_p) for every good prime p and thereby raises the
probability that #E is B1-smooth: the ECM-torsion parametrisations
(Suyama Z/6, Montgomery Z/12, Atkin-Morain Z/2xZ/8) are the literal
"clocks in series" of ECM.

What is measured (exact group orders by vectorised point counting on
16-17-bit primes, both residue classes mod 4, deterministic seeds):

  T1  parametrisation gates: Suyama and Montgomery-Z/12 curves have
      12 | #E(F_p) for every sampled (p, seed); the generic Montgomery
      baseline only 2 | #E.  (Self-check of the formulas; a failure here
      would invalidate the family, not the theory.)
  T2  the clock gain: mean 2- and 3-adic valuations of #E and the
      probability that #E is B1-smooth per family, B1 in {30, 60, 120, 240},
      ratio to the Z/2 baseline.  Known result to be reproduced: a
      CONSTANT factor (order 1.2 .. 2), never a change of exponent.
  T3  the mu4 clock as CM: y^2 = x^3 + D x (j = 1728, automorphism of order
      4 = the mu4 clock).  For p = 3 mod 4: #E = p + 1 for all four quartic
      twists (supersingular) -> ECM degenerates to Williams p+1.  For
      p = 1 mod 4: #E in {p+1 +- 2a, p+1 +- 2b} with p = a^2 + b^2, i.e.
      only four group orders instead of a random family -> the rigid clock
      is WORSE than a random curve unless one of the four orders happens to
      be smooth.  Smoothness of the CM family measured against the baseline.
  T4  Mazur's cap (theorem, quoted; consistency-checked on the data): the
      rational torsion of an elliptic curve over Q is one of Z/n (n <= 10 or
      12) or Z/2 x Z/2n (n <= 4).  So the order-12 compiler clock is exactly
      the largest cyclic clock ECM can use over Q; the 48-cycle and the
      Coxeter clock of order 30 cannot be realised as rational torsion.
      Over Q(i) (the Z[i] structure) Z/4 x Z/4 exists (Kamienny-Kenku-
      Momose) -- the Brier-Clavier family for primes p = 1 mod 4.

Decision: CLOCK_IS_TORSION_CONSTANT_GAIN (gains are constant factors and
CM is rigid -> the lane reproduces known ECM engineering; STOP unless a
torsion structure beyond Mazur's list is proposed over a number field with
cheap arithmetic mod N) / CLOCK_NO_GAIN / CLOCK_SUPERLINEAR_GAIN (gain grows
with B1 or p in a way inconsistent with a constant factor -- would be news).

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: no factoring claim; no RH claim.  Nothing here beats GNFS or ECM.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROUND = 641
SEED = 641202609
CONTRACT = "CLOCK.CM.ECM.01"
FENCE = "Exploration; no factoring claim; no RH claim"
TAG = "r641"
RESULT_JSON = HERE / "clock_torsion_ecm_result.json"

PRIME_BITS = 16                 # exact point counting is O(p): keep p ~ 6e4..1.3e5
N_PRIMES = 48                   # balanced between p = 1 mod 4 and p = 3 mod 4
CURVES_PER_FAMILY = 24
B1_GRID = (30, 60, 120, 240)
MAZUR_CYCLIC = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
MAZUR_NONCYCLIC = ((2, 2), (2, 4), (2, 6), (2, 8))
TFPT_CLOCKS = {"mu4": 4, "compiler": 12, "cycle48": 48, "coxeter": 30}
CONSTANT_GAIN_MAX = 4.0         # a torsion clock cannot buy more than a constant; 4x is generous
DECISIONS = ("CLOCK_IS_TORSION_CONSTANT_GAIN", "CLOCK_NO_GAIN", "CLOCK_SUPERLINEAR_GAIN")

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(s: str = "") -> None:
    LINES.append(s)
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


# --- arithmetic ------------------------------------------------------------
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


def sqrt_mod(a: int, p: int) -> int | None:
    """Tonelli-Shanks; None if a is a non-residue."""
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


def two_squares(p: int) -> tuple[int, int]:
    """p = a^2 + b^2 for p = 1 mod 4 (Cornacchia)."""
    r = sqrt_mod(p - 1, p)
    assert r is not None
    a, b = p, r
    lim = math.isqrt(p)
    while b > lim:
        a, b = b, a % b
    c = p - b * b
    d = math.isqrt(c)
    assert d * d == c
    return max(b, d), min(b, d)


def valuation(n: int, q: int) -> int:
    v = 0
    while n % q == 0 and n:
        n //= q
        v += 1
    return v


def is_smooth(n: int, B: int, small_primes: list[int]) -> bool:
    for q in small_primes:
        if q > B:
            break
        while n % q == 0:
            n //= q
    return n == 1


class Counter:
    """#E(F_p) for y^2 = f(x) by a quadratic-character table (exact, vectorised)."""

    def __init__(self, p: int):
        self.p = p
        x = np.arange(p, dtype=np.int64)
        sq = np.zeros(p, dtype=bool)
        sq[(x * x) % p] = True
        self.chi = np.where(sq, 1, -1).astype(np.int64)
        self.chi[0] = 0
        self.x = x

    def count(self, a2: int, a4: int, a6: int, twist_chi: int = 1) -> int:
        p, x = self.p, self.x
        f = (x * x % p * x + a2 * x % p * x + a4 * x + a6) % p
        return p + 1 + twist_chi * int(np.sum(self.chi[f]))


# --- curve families ----------------------------------------------------------
def montgomery_order(cnt: Counter, A: int, xz: tuple[int, int]) -> int:
    """#E for B y^2 = x^3 + A x^2 + x through the projective point (x0 : z0)."""
    p = cnt.p
    x0, z0 = xz
    x = x0 * pow(z0, -1, p) % p
    Bclass = (x * x % p * x + A * x % p * x + x) % p          # B mod squares (y0 = 1)
    tw = int(cnt.chi[Bclass]) if Bclass else 1
    return cnt.count(A, 1, 0, tw)


def family_generic(rng: np.random.Generator, p: int) -> tuple[int, tuple[int, int]] | None:
    """Montgomery curve with random A: only the 2-torsion point (0,0) forced."""
    A = int(rng.integers(3, p - 2))
    x0 = int(rng.integers(1, p - 1))
    if (A * A - 4) % p == 0:
        return None
    return A, (x0, 1)


def family_suyama(rng: np.random.Generator, p: int) -> tuple[int, tuple[int, int]] | None:
    """Suyama: sigma -> curve with 12 | #E(F_p)."""
    sigma = int(rng.integers(6, p - 1))
    u = (sigma * sigma - 5) % p
    v = (4 * sigma) % p
    if u == 0 or v == 0:
        return None
    x0 = pow(u, 3, p)
    z0 = pow(v, 3, p)
    num = pow((v - u) % p, 3, p) * ((3 * u + v) % p) % p
    den = 4 * x0 % p * v % p
    if den == 0:
        return None
    A = (num * pow(den, -1, p) - 2) % p
    if (A * A - 4) % p == 0:
        return None
    return A, (x0, z0)


def family_z12(rng: np.random.Generator, p: int) -> tuple[int, tuple[int, int]] | None:
    """Montgomery's Z/12 torsion family from a point (u, v) on v^2 = u^3 - 12 u."""
    for _ in range(64):
        u = int(rng.integers(1, p))
        rhs = (u * u % p * u - 12 * u) % p
        v = sqrt_mod(rhs, p)
        if v is None or v == 0:
            continue
        t = v * pow(2 * u % p, -1, p) % p
        t2 = t * t % p
        if (t2 + 3) % p == 0:
            continue
        a = (t2 - 1) * pow((t2 + 3) % p, -1, p) % p
        if a == 0:
            continue
        x0 = (3 * a * a + 1) % p
        z0 = 4 * a % p
        A = (-(3 * pow(a, 4, p) + 6 * a * a - 1)) * pow(4 * pow(a, 3, p) % p, -1, p) % p
        if (A * A - 4) % p == 0:
            continue
        return A, (x0, z0)
    return None


def cm_1728_orders(cnt: Counter) -> list[int]:
    """#E for the four quartic twists y^2 = x^3 + D x, D over F_p^* / (F_p^*)^4."""
    p = cnt.p
    g = 2
    while pow(g, (p - 1) // 2, p) != p - 1:      # a non-residue generates the twist classes
        g += 1
    reps = [pow(g, k, p) for k in range(4)]
    return [cnt.count(0, D, 0) for D in reps]


# --- main measurement ----------------------------------------------------------
def run(n_primes: int, curves: int) -> dict:
    rng = np.random.default_rng(SEED)
    small_primes = [q for q in range(2, max(B1_GRID) + 1) if is_prime(q)]

    # balanced prime sample
    primes: list[int] = []
    want = {1: n_primes // 2, 3: n_primes - n_primes // 2}
    while sum(want.values()):
        c = int(rng.integers(1 << PRIME_BITS, 1 << (PRIME_BITS + 1))) | 1
        if is_prime(c) and want[c % 4] > 0:
            primes.append(c)
            want[c % 4] -= 1
    primes.sort()

    families = {"Z2_generic": family_generic, "Z6_suyama": family_suyama, "Z12_montgomery": family_z12}
    orders: dict[str, list[int]] = {k: [] for k in families}
    orders_by_res: dict[str, dict[int, list[int]]] = {k: {1: [], 3: []} for k in families}
    div12 = {k: 0 for k in families}
    div2 = {k: 0 for k in families}
    cm_orders: dict[int, list[int]] = {1: [], 3: []}
    cm_ok_supersingular = True
    cm_ok_split = True

    section("T1  parametrisation gates on %d primes (%d-%d bit, %d of each class mod 4), %d curves per family"
            % (len(primes), PRIME_BITS, PRIME_BITS + 1, n_primes // 2, curves))
    for p in primes:
        cnt = Counter(p)
        for name, fam in families.items():
            got = 0
            while got < curves:
                cur = fam(rng, p)
                if cur is None:
                    continue
                A, xz = cur
                n = montgomery_order(cnt, A, xz)
                assert abs(n - (p + 1)) <= 2 * math.isqrt(p) + 1, "Hasse violated: counting bug"
                orders[name].append(n)
                orders_by_res[name][p % 4].append(n)
                div12[name] += (n % 12 == 0)
                div2[name] += (n % 2 == 0)
                got += 1
        # CM family j = 1728
        os_ = cm_1728_orders(cnt)
        cm_orders[p % 4].extend(os_)
        if p % 4 == 3:
            cm_ok_supersingular &= all(n == p + 1 for n in os_)
        else:
            a, b = two_squares(p)
            allowed = {p + 1 + 2 * a, p + 1 - 2 * a, p + 1 + 2 * b, p + 1 - 2 * b}
            cm_ok_split &= set(os_) == allowed

    total = len(primes) * curves
    check("T1a-suyama-12-divides-#E-always", div12["Z6_suyama"] == total, "%d/%d" % (div12["Z6_suyama"], total))
    check("T1b-montgomery-Z12-12-divides-#E-always", div12["Z12_montgomery"] == total,
          "%d/%d" % (div12["Z12_montgomery"], total))
    check("T1c-generic-2-divides-#E-always-12-not-forced", div2["Z2_generic"] == total and div12["Z2_generic"] < 0.9 * total,
          "2 | #E: %d/%d, 12 | #E: %d/%d (generic Montgomery: 12 | #E only by chance, ~50 %%)"
          % (div2["Z2_generic"], total, div12["Z2_generic"], total))

    section("T2  the clock gain: valuations and B1-smoothness of #E per family")
    stats: dict[str, dict] = {}
    for name in families:
        arr = orders[name]
        v2 = float(np.mean([valuation(n, 2) for n in arr]))
        v3 = float(np.mean([valuation(n, 3) for n in arr]))
        smooth = {B: float(np.mean([is_smooth(n, B, small_primes) for n in arr])) for B in B1_GRID}
        stats[name] = {"v2_mean": v2, "v3_mean": v3, "smooth": {str(B): s for B, s in smooth.items()}}
        emit("  %-15s  <v2>=%.3f  <v3>=%.3f  P(B1-smooth): %s"
             % (name, v2, v3, "  ".join("B1=%d: %.4f" % (B, smooth[B]) for B in B1_GRID)))
    ratios = {}
    for name in ("Z6_suyama", "Z12_montgomery"):
        ratios[name] = {}
        for B in B1_GRID:
            base = stats["Z2_generic"]["smooth"][str(B)]
            ratios[name][str(B)] = (stats[name]["smooth"][str(B)] / base) if base > 0 else float("nan")
        emit("  gain vs Z2_generic  %-15s  %s" % (name, "  ".join("B1=%d: x%.2f" % (B, ratios[name][str(B)]) for B in B1_GRID)))
    gains = [g for name in ratios for g in ratios[name].values() if math.isfinite(g)]
    check("T2a-clock-gain-is-a-constant-factor", 1.0 <= min(gains) and max(gains) <= CONSTANT_GAIN_MAX,
          "min x%.2f  max x%.2f  (a torsion clock multiplies the smoothness probability by O(1); the exponent L_p[1/2] is untouched)"
          % (min(gains), max(gains)))
    # Barbulescu-Bos-Bouvier-Kleinjung-Montgomery (2012), average valuations of #E(F_p):
    #   Suyama (Z/6):        <v2> = 10/3, <v3> = 27/16 ;  Montgomery Z/12:  <v2> = 11/3, <v3> = 27/16
    bbbkm = {"Z6_suyama": (10 / 3, 27 / 16), "Z12_montgomery": (11 / 3, 27 / 16)}
    dev = {name: (abs(stats[name]["v2_mean"] - t[0]), abs(stats[name]["v3_mean"] - t[1])) for name, t in bbbkm.items()}
    tol = math.sqrt(N_PRIMES * CURVES_PER_FAMILY / total)      # statistical tolerance scales with 1/sqrt(sample)
    check("T2b-valuations-match-BBBKM12-clock-averages",
          all(d2 < 0.12 * tol and d3 < 0.10 * tol for d2, d3 in dev.values())
          and stats["Z6_suyama"]["v3_mean"] > stats["Z2_generic"]["v3_mean"] + 0.5,
          "Suyama <v2>,<v3> = %.3f, %.3f (10/3, 27/16); Z/12 = %.3f, %.3f (11/3, 27/16); generic <v3> = %.3f: "
          "the clock is a shift of the 2- and 3-adic valuation averages, nothing more"
          % (stats["Z6_suyama"]["v2_mean"], stats["Z6_suyama"]["v3_mean"], stats["Z12_montgomery"]["v2_mean"],
             stats["Z12_montgomery"]["v3_mean"], stats["Z2_generic"]["v3_mean"]))

    section("T3  the mu4 clock as CM: y^2 = x^3 + D x (j = 1728), four quartic twists")
    check("T3a-p=3mod4-supersingular-#E=p+1-all-twists", cm_ok_supersingular,
          "the rigid clock collapses ECM to Williams p+1 on half of all primes")
    check("T3b-p=1mod4-orders-are-p+1+-2a,p+1+-2b", cm_ok_split, "p = a^2 + b^2: the Z[i] norm form dictates the four orders")
    cm_smooth = {}
    for res in (1, 3):
        arr = cm_orders[res]
        cm_smooth[res] = {B: float(np.mean([is_smooth(n, B, small_primes) for n in arr])) for B in B1_GRID}
        emit("  CM j=1728, p=%d mod 4 (%d orders)  P(B1-smooth): %s"
             % (res, len(arr), "  ".join("B1=%d: %.4f" % (B, cm_smooth[res][B]) for B in B1_GRID)))
    base_by_res = {res: {B: float(np.mean([is_smooth(n, B, small_primes) for n in orders_by_res["Z2_generic"][res]]))
                         for B in B1_GRID} for res in (1, 3)}
    emit("  Z2_generic split by class: p=1: %s | p=3: %s"
         % ("  ".join("%.4f" % base_by_res[1][B] for B in B1_GRID), "  ".join("%.4f" % base_by_res[3][B] for B in B1_GRID)))
    # A rigid CM clock has only 4 orders per prime; the generic family samples fresh orders per curve.
    # Success per *prime* for CM = 1 if any of the four orders is smooth; generic: 1 - (1-P)^4 with four curves.
    cm_per_prime = {}
    gen_per_prime = {}
    for res in (1, 3):
        chunks = [cm_orders[res][i:i + 4] for i in range(0, len(cm_orders[res]), 4)]
        cm_per_prime[res] = {B: float(np.mean([any(is_smooth(n, B, small_primes) for n in ch) for ch in chunks])) for B in B1_GRID}
        gen_per_prime[res] = {B: 1.0 - (1.0 - base_by_res[res][B]) ** 4 for B in B1_GRID}
    for B in B1_GRID:
        emit("  per-prime success with 4 curves, B1=%3d: CM p=1: %.3f vs generic %.3f | CM p=3: %.3f vs generic %.3f"
             % (B, cm_per_prime[1][B], gen_per_prime[1][B], cm_per_prime[3][B], gen_per_prime[3][B]))
    cm_avg = {B: 0.5 * (cm_per_prime[1][B] + cm_per_prime[3][B]) for B in B1_GRID}
    gen_avg = {B: 0.5 * (gen_per_prime[1][B] + gen_per_prime[3][B]) for B in B1_GRID}
    check("T3c-rigid-CM-clock-not-better-than-random-curves-on-average",
          all(cm_avg[B] <= gen_avg[B] + 0.05 for B in B1_GRID),
          "averaged over both classes mod 4: CM %s vs generic %s -- one forced order on half the primes is the cost of rigidity"
          % (["%.2f" % cm_avg[B] for B in B1_GRID], ["%.2f" % gen_avg[B] for B in B1_GRID]))

    section("T4  Mazur's cap: which TFPT clocks can be rational torsion at all")
    realisable = {name: (k in MAZUR_CYCLIC or any(m * n_ == k for m, n_ in MAZUR_NONCYCLIC))
                  for name, k in TFPT_CLOCKS.items()}
    emit("  rational torsion over Q (Mazur 1977): Z/n, n in %s; Z/2 x Z/2n, n <= 4" % (MAZUR_CYCLIC,))
    emit("  TFPT clocks realisable as rational torsion: %s" % realisable)
    check("T4a-order-12-clock-is-Mazur-maximal-cyclic", realisable["compiler"] and max(MAZUR_CYCLIC) == 12,
          "the compiler clock is exactly the largest cyclic ECM torsion over Q")
    check("T4b-48-and-30-clocks-not-rational-torsion", not realisable["cycle48"] and not realisable["coxeter"],
          "cannot be forced into #E(F_p) for all p by a curve over Q; over Q(i): Z/4 x Z/4 (order 16) is the maximum "
          "with a mu4 x mu4 shape (Kamienny-Kenku-Momose; Brier-Clavier ECM family for p = 1 mod 4)")
    # data consistency: 48 | #E is never forced in any family
    forced48 = {name: all(n % 48 == 0 for n in orders[name]) for name in families}
    check("T4c-no-family-forces-48|#E", not any(forced48.values()), str(forced48))

    return {"n_primes": len(primes), "curves_per_family": curves, "prime_bits": PRIME_BITS, "stats": stats,
            "gain_vs_generic": ratios, "cm_smooth": {str(k): {str(B): v for B, v in d.items()} for k, d in cm_smooth.items()},
            "cm_per_prime": {str(k): {str(B): v for B, v in d.items()} for k, d in cm_per_prime.items()},
            "generic_per_prime": {str(k): {str(B): v for B, v in d.items()} for k, d in gen_per_prime.items()},
            "mazur_realisable": realisable}


def decide(res: dict) -> tuple[str, str]:
    gains = [g for fam in res["gain_vs_generic"].values() for g in fam.values() if math.isfinite(g)]
    if not gains or max(gains) < 1.05:
        return "CLOCK_NO_GAIN", "torsion families do not raise B1-smoothness above the generic Montgomery baseline"
    # superlinear: gain growing with B1 monotonically by more than 2x across the grid
    for fam, d in res["gain_vs_generic"].items():
        seq = [d[str(B)] for B in B1_GRID]
        if all(math.isfinite(s) for s in seq) and seq[-1] > 2.0 * seq[0] and all(b >= a for a, b in zip(seq, seq[1:])):
            return "CLOCK_SUPERLINEAR_GAIN", "%s gain grows with B1: %s" % (fam, ["%.2f" % s for s in seq])
    return "CLOCK_IS_TORSION_CONSTANT_GAIN", ("the TFPT clocks map onto the ECM torsion families (Z/6, Z/12; Z/4 x Z/4 over Q(i)); "
                                             "the gain is a constant factor x%.2f..x%.2f, the CM (mu4) curve is rigid, and Mazur caps "
                                             "the clock at 12 (cyclic) / 16 over Q -- known ECM engineering, no new exponent"
                                             % (min(gains), max(gains)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    n_primes, curves = (12, 8) if args.smoke else (N_PRIMES, CURVES_PER_FAMILY)
    wall0 = time.time()
    emit("%s  %s  round %d  fence: %s" % (TAG, CONTRACT, ROUND, FENCE))
    res = run(n_primes, curves)
    verdict, why = decide(res)
    check("G-verdict-enum", verdict in DECISIONS, verdict)
    payload = {"contract": CONTRACT, "tag": TAG, "round": ROUND, "fence": FENCE, "verdict": verdict, "why": why,
               "result": res, "gates": {name: ok for name, ok in CHECKS}}
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
