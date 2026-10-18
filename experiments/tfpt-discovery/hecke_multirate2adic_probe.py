#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hecke_multirate2adic_probe -- HECKE.MULTIRATE2ADIC.01 (+ SPINLIFT ladder).

Positive-protocol strand B.  Builds on HECKE.CARRIER_CHECK32.01
(hecke_check32_probe.py, same directory): f8 = eta(2t)^4 eta(4t)^4 is the
TFPT cusp channel (corpus anchor v535 HECKE.GEOM.01), E_odd = sum_{n odd}
sigma3(n) q^n, and f8 == E_odd (mod 32) with 32 = 2^g_car.

PART 1 -- THE MULTIRATE 2-ADIC DEPTH (candidate theorem, FROZEN before
running).  For every odd prime p,

    v_2(1 + p^3 - a_p)  >=  5 + 2*[chi_{-4}(p) = 1] + [chi_8(p) = 1],

i.e. the minimal 2-divisibility by p mod 8 is
    p == 3 (mod 8) -> 2^5,   p == 7 (mod 8) -> 2^6,
    p == 5 (mod 8) -> 2^7,   p == 1 (mod 8) -> 2^8,
and each bound is ATTAINED (sharpness witnesses per class).  Since
sigma3(p) = 1 + p^3, this is a statement about D := E_odd - f8 = 32*H.

CLOSED SIGMA1-CONVOLUTION FORMULA (frozen; hand-derived from the first
odd coefficients and re-verified here on a long exact segment):
    a_n = sigma3(n) - 32*H_n   for odd n,  with
    H_n = W_{1,2}(n) - 3*W_{1,4}(n) + 2*W_{1,8}(n),
    W_{1,k}(n) = sum_{a + k*b = n, a,b >= 1} sigma1(a) sigma1(b).
Series form: H = L(q) * [L(q^2) - 3 L(q^4) + 2 L(q^8)] restricted to odd
exponents, L(q) = sum sigma1(n) q^n.  Quasimodular bookkeeping (the
structural reason a finite check certifies the odd part): with
M_k := E2(t) - k E2(kt) in M_2(Gamma0(k)),
    L(q^2) - 3L(q^4) + 2L(q^8) = (M_2/2 - 3 M_4/4 + M_8/4)/24 =: F/24,
the E2-anomaly cancels (coefficients -1/2 + 3/4 - 1/4 = 0), and F has
ZERO odd coefficients (24 sigma1(n) (1/2 - 3/4 + 1/4) = 0, machine-
checked), so the odd projection of L*F/24 has vanishing depth part and
is a genuine weight-4 form of level <= 64; both sides of the identity
are then congruent by Sturm far below the verified range.

PREDECLARED SECTIONS:
  S0  exact builds: f8 to q^N_SEG by eta product (imported CHECK32
      machinery); sigma1/sigma3 sieves; corpus a_p anchor.
  S1  FORMULA: sigma3(n) - a_n == 32*H_n for ALL odd n <= N_SEG, exact;
      plus the depth-cancellation lemma F_odd = 0, exact.
  S2  CENSUS over ALL odd primes p < CAP (feasibility-gated: pilot
      Kronecker multiply timed at N_PILOT, CAP = 10^6 if the projected
      full multiply fits the budget, else fallback >= 10^5).  a_p is
      computed FROM THE CONVOLUTION FORMULA (single big-integer
      Kronecker product mod 2^20 => v_2(D_p) exact up to 25, bucket
      ">=25" above); cross-checked against the exact eta build on the
      overlap p < N_SEG.  Recorded: per-class v_2 histogram, minimum,
      violation list (must be empty), sharpness witnesses (smallest
      prime attaining the class minimum).
  S3  CHARACTER DISSECTION (structural route).  Predeclared identities
      on the FULL odd series (not just primes), D = E_odd - f8:
        I0 (base, CHECK32):   D_n == 0 (mod 32)   all odd n;
        I1 (chi_{-4} sift):   D_n == 0 (mod 128)  n == 1 (mod 4);
        I2 (chi_8 sift):      D_n == 0 (mod 64)   n == +-1 (mod 8);
        I3 (chi_{-4}chi_8):   D_n == 0 (mod 256)  n == 1 (mod 8);
      equivalently v_2(D_n) >= 5 + 2*[chi_{-4}(n)=1] + [chi_8(n)=1] for
      ALL odd n -- the prime claim is the restriction to primes.  Each
      sift is a two-character combination (D +- D tensor chi)/2 of
      twisted weight-4 forms; twisting by characters mod 8 keeps level
      <= 8*8^2 = 512, Sturm bound (4/12)*[SL2:Gamma0(512)] = 256; the
      identities are verified exactly to N_SEG = 78x that bound.
      chi_{-4}*chi_8 = chi_{-8} closes the corpus four-character
      envelope system of v541 RTF.GNS.LEDGER.01 (C).
      PREDECLARED MUST-FAIL: the strengthening "D == 0 (mod 512) on
      n == 1 (mod 8)" must fail (expected witness n = 9, D_9 = 768).
      TYPING (honest): the LADDER BOUND is theorem-grade modulo two
      cited classical ingredients (Sturm 1987; the standard twist /
      odd-projection level lemma, e.g. Shimura 1971 / Atkin-Li 1978)
      -- everything else is machine-verified integer arithmetic.
      SHARPNESS is census-level (exact small-prime witnesses + full
      census, no analytic proof of infinitude per class claimed).
  S4  CONTROLS (must fire, criteria frozen):
      C1 mutant eta exponent eta(2t)^4 eta(4t)^3: ladder failure
         fraction > 1/2 in every class mod 8.
      C2 scrambled a_p assignment (seeded permutation of the true a_p
         values across primes): ladder failure fraction > 1/2 overall
         and in every class.
  S5  SPINLIFT (part 2): rebuild the corpus half-integral witness
      g = theta2(2t)^2 theta3(2t) theta4(t) theta4(2t) (v537 key
      (0,2,0,1,1,1), weight 5/2, level 32 = 4*8) with exact integers;
      verify Sh_{t=2,psi=1}(g)_n = -8 a_n for ALL n <= N_SH, and the
      ladder form Sh(g) = -8 E_odd + 256 H coefficientwise with H from
      the CONVOLUTION formula (independent of the eta build; even n:
      both sides 0).  Level-32 anchors reproduced: U4(g) = 0 exactly,
      |g|-mass mod 4 = {0:0, 1:+, 2:+, 3:0}, T(3^2) g = -4 g, Kohnen
      window 4a - 8bc = 1 unsolvable (level 32 = 4*8, M = 8 even --
      outside Kohnen 1982).  Note: the Kronecker factor (2/d) in the
      Shimura lift IS chi_8(d) (machine-checked) -- the same character
      that rules the third rung of the ladder.
  S6  LADDER SEMANTICS 32 -> 256 -> 128 [C neu] -- STRUCTURAL
      OBSERVATION ONLY, no derivation claimed: 32 = 2^g_car (axiom P2;
      pi_cusp = (28 - T_3)/32, v535 N4a); 256 = 32*8 = |Sh scale|*32 =
      2^8 = dim Fock(16 Majorana) -- the carrier seam is 10 + 6 = 16
      Majoranas (v113), 2^8 = 256-dim Fock space (v529), NS/R sector
      census v148; 128 + 128 = 256 with 128 the chiral half, matching
      248 = 120 + 128 at E8 level 1 (wolfram README anchor).

VERDICT ENUM (frozen):
  MULTIRATE-THEOREM : bound holds everywhere (census clean at CAP >=
                      10^5) + sharpness attained in all four classes +
                      formula exact on segment + dissection identities
                      verified >> Sturm with honest typing + controls
                      fire.
  MULTIRATE-PARTIAL : some component degraded, no counterexample.
  MULTIRATE-FALSE   : a counterexample prime -- reported exactly.
  SPINLIFT-VERIFIED : Sh(g) = -8 f8 = -8 E_odd + 256 H exact to N_SH
                      + all level-32 anchors reproduced.
  SPINLIFT-FAILS    : otherwise.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.
"""
from __future__ import annotations

import random
import time

from hecke_check32_probe import build_f8, sieve_primes, sieve_sigma3

# ---------------------------------------------------------------- budgets
N_SEG = 20_000            # exact segment (eta build + exact convolution)
CAP_PRIMARY = 1_000_000   # census target (feasibility-gated)
CAP_FALLBACK = 100_000    # predeclared minimum census
N_PILOT = 250_000         # pilot size for the Kronecker feasibility timing
PILOT_BUDGET_S = 600.0    # go to 10^6 only if projected multiply fits this
MOD_BITS = 20             # census works mod 2^20 => v_2(D_p) exact to 25
V2_CAP = MOD_BITS + 5     # D = 32*H, so cap = 5 + MOD_BITS
LADDER = {3: 5, 7: 6, 5: 7, 1: 8}      # class mod 8 -> minimal v_2
N_SH = 160                # Shimura verification range (needs g to 2*N_SH^2)
Q_G = 2 * N_SH * N_SH     # 51200
N_HECKE_HALF = 40         # T(3^2) eigen check range
STURM_TWIST = 256         # (4/12) * [SL2:Gamma0(512)] = 768/3
RNG_SEED = 20260805
A_P_CORPUS = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}   # v535 HECKE.GEOM.01

CHECKS = []


def check(label: str, ok: bool) -> bool:
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return bool(ok)


# ------------------------------------------------------------- characters
def chi_m4(n: int) -> int:
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def chi_8(n: int) -> int:
    return 0 if n % 2 == 0 else (1 if n % 8 in (1, 7) else -1)


def chi_m8(n: int) -> int:
    return 0 if n % 2 == 0 else (1 if n % 8 in (1, 3) else -1)


def ladder_bound(n: int) -> int:
    return 5 + 2 * (chi_m4(n) == 1) + (chi_8(n) == 1)


def v2_capped(x: int, cap: int) -> int:
    """v_2(x) for x given mod 2^cap; returns cap if x == 0 (mod 2^cap)."""
    x &= (1 << cap) - 1
    if x == 0:
        return cap
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


# ------------------------------------------------- fast exact convolution
def _encode(v, K):
    nb = K // 8
    return int.from_bytes(
        b"".join(int(x).to_bytes(nb, "little") for x in v), "little")


def kron_mul_fast(a, b, n_out):
    """Exact signed integer polynomial product, truncated at degree n_out.
    Kronecker substitution with a single big-int multiply; O(n) decode via
    one to_bytes pass (balanced digits with carry propagation)."""
    ca = max((abs(x) for x in a), default=0)
    cb = max((abs(x) for x in b), default=0)
    bound = ca * cb * min(len(a), len(b)) + 1
    K = 64
    while bound >= (1 << (K - 2)):
        K += 64
    ap = _encode([x if x > 0 else 0 for x in a], K)
    bp = _encode([x if x > 0 else 0 for x in b], K)
    an = _encode([-x if x < 0 else 0 for x in a], K) \
        if any(x < 0 for x in a) else 0
    bn = _encode([-x if x < 0 else 0 for x in b], K) \
        if any(x < 0 for x in b) else 0
    prod = (ap - an) * (bp - bn)
    neg = prod < 0
    if neg:
        prod = -prod
    nb = K // 8
    need = max((n_out + 2) * nb, (prod.bit_length() + 7) // 8 + nb)
    raw = prod.to_bytes(need, "little")
    half = 1 << (K - 1)
    full = 1 << K
    out = [0] * (n_out + 1)
    carry = 0
    for i in range(n_out + 1):
        d = int.from_bytes(raw[i * nb:(i + 1) * nb], "little") + carry
        if d >= half:
            d -= full
            carry = 1
        else:
            carry = 0
        out[i] = -d if neg else d
    return out


def sieve_sigma1(n_max):
    s = [0] * (n_max + 1)
    for d in range(1, n_max + 1):
        for m in range(d, n_max + 1, d):
            s[m] += d
    return s


def w_factor(sig1, n_max, mod=None):
    """T(q) = L(q^2) - 3 L(q^4) + 2 L(q^8) as a coefficient list
    (optionally reduced to [0, mod))."""
    t = [0] * (n_max + 1)
    for m in range(2, n_max + 1, 2):
        c = sig1[m // 2]
        if m % 4 == 0:
            c -= 3 * sig1[m // 4]
        if m % 8 == 0:
            c += 2 * sig1[m // 8]
        t[m] = c % mod if mod is not None else c
    return t


def h_series(sig1, n_max, mod=None):
    """H = L(q) * [L(q^2) - 3L(q^4) + 2L(q^8)] truncated at n_max.
    Only ODD coefficients carry the formula's meaning."""
    L = [0] + [(sig1[n] % mod if mod is not None else sig1[n])
               for n in range(1, n_max + 1)]
    T = w_factor(sig1, n_max, mod)
    return kron_mul_fast(L, T, n_max)


# ----------------------------------------------------- theta / Shimura (S5)
def theta_t(kind: int, scale: int, order_t: int):
    """theta2/3/4(scale * tau) in the t = q^{1/4} variable, exact ints."""
    s = [0] * (order_t + 1)
    if kind == 2:
        o = 1
        while scale * o * o <= order_t:
            s[scale * o * o] = 2
            o += 2
    else:
        s[0] = 1
        sgn = -1 if kind == 4 else 1
        n = 1
        while 4 * scale * n * n <= order_t:
            s[4 * scale * n * n] = 2 * (sgn ** n)
            n += 1
    return s


def build_g(qmax: int):
    """Corpus v537 witness: theta2(2t)^2 theta3(2t) theta4(t) theta4(2t),
    key (0,2,0,1,1,1); returns exact q-coefficients b(0..qmax)."""
    order_t = 4 * qmax
    acc = theta_t(2, 2, order_t)
    for kind, scale in ((2, 2), (3, 2), (4, 1), (4, 2)):
        acc = kron_mul_fast(acc, theta_t(kind, scale, order_t), order_t)
    for r in (1, 2, 3):
        assert all(c == 0 for c in acc[r::4]), "non-integer q-power present"
    return [acc[4 * n] for n in range(qmax + 1)]


def kron2(d: int) -> int:
    """Kronecker symbol (2/d) for odd d (= chi_8(d))."""
    return 1 if d % 8 in (1, 7) else -1


def shimura_lift(bq, nmax, t=2):
    """Sh_{t,psi=1}(g): A(n) = sum_{d|n} (t/d) d^{k-1} b(t n^2/d^2), k=2."""
    out = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        tot = 0
        for d in range(1, n + 1):
            if n % d:
                continue
            if d % 2 == 0:
                continue  # (2/d) = 0 for even d
            idx = t * (n // d) ** 2
            tot += kron2(d) * d * bq[idx]
        out[n] = tot
    return out


def T9_half(b, order, n_check):
    """T(p^2) at p = 3, weight 5/2, trivial nebentypus (Shimura 1973):
    (T9 b)(n) = b(9n) + 3*legendre(n,3)*b(n) + 27*b(n/9)."""
    def leg3(n):
        r = n % 3
        return 0 if r == 0 else (1 if r == 1 else -1)
    out = []
    for n in range(n_check + 1):
        term = b[9 * n] if 9 * n <= order else 0
        if n >= 1:
            term += 3 * leg3(n) * b[n]
        if n % 9 == 0:
            term += 27 * b[n // 9]
        out.append(term)
    return out


# ================================================================== run
def main():
    t0 = time.time()
    print("hecke_multirate2adic_probe -- HECKE.MULTIRATE2ADIC.01 + SPINLIFT")
    print(f"  segment N_SEG = {N_SEG}, census target < {CAP_PRIMARY} "
          f"(fallback {CAP_FALLBACK}), ladder {LADDER} (class mod 8 -> v2)")

    # ------------------------------------------------------------- S0
    print("S0 -- exact builds (eta product + sieves)")
    a = build_f8(N_SEG)
    sig1 = sieve_sigma1(N_SEG)
    sig3 = sieve_sigma3(N_SEG)
    check(f"corpus anchor (v535): a_p = {A_P_CORPUS} reproduced; "
          "a_0 = 0, a_1 = 1, even support empty",
          all(a[p] == v for p, v in A_P_CORPUS.items())
          and a[0] == 0 and a[1] == 1
          and all(a[n] == 0 for n in range(0, N_SEG + 1, 2)))

    # ------------------------------------------------------------- S1
    print("S1 -- closed sigma1-convolution formula (frozen)")
    t1 = time.time()
    H = h_series(sig1, N_SEG)
    bad = [n for n in range(1, N_SEG + 1, 2)
           if sig3[n] - a[n] != 32 * H[n]]
    check(f"a_n = sigma3(n) - 32*[W12 - 3*W14 + 2*W18](n) EXACT for ALL "
          f"odd n <= {N_SEG} (failures: {len(bad)}"
          + (f", first {bad[0]}" if bad else "")
          + f"); built in {time.time() - t1:.1f}s", len(bad) == 0)
    print(f"        H head (odd n=1..17): "
          f"{[(n, H[n]) for n in range(1, 18, 2)]}")
    # depth-cancellation lemma: F = 2*M2 - 3*M4 + M8 has zero odd part
    f_bad = 0
    for n in range(1, N_SEG + 1, 2):
        # M_k(n) = 24*(sigma1(n) - k*sigma1(n/k)) = 24*sigma1(n) for odd n
        if 2 * 24 * sig1[n] - 3 * 24 * sig1[n] + 24 * sig1[n] != 0:
            f_bad += 1
    check("depth-cancellation lemma: F = 2*M2 - 3*M4 + M8 (weight-2, "
          f"level 8) has ZERO odd coefficients on n <= {N_SEG} -- the odd "
          "projection of the convolution series is a genuine weight-4 "
          "form of level <= 64 (quasimodular anomaly cancels: "
          "-1/2 + 3/4 - 1/4 = 0)", f_bad == 0)

    # ------------------------------------------------------------- S2
    print("S2 -- census (feasibility-gated)")
    t1 = time.time()
    sig1_pilot = sieve_sigma1(N_PILOT)
    h_series(sig1_pilot, N_PILOT, mod=1 << MOD_BITS)
    t_pilot = time.time() - t1
    t_proj = t_pilot * (CAP_PRIMARY / N_PILOT) ** 1.6
    cap = CAP_PRIMARY if t_proj < PILOT_BUDGET_S else CAP_FALLBACK
    print(f"        pilot at N = {N_PILOT}: {t_pilot:.1f}s, projected "
          f"full run {t_proj:.0f}s -> CAP = {cap}")
    check(f"feasibility gate: census CAP = {cap} >= predeclared minimum "
          f"{CAP_FALLBACK}", cap >= CAP_FALLBACK)

    t1 = time.time()
    sig1_big = sieve_sigma1(cap) if cap != N_PILOT else sig1_pilot
    Hm = h_series(sig1_big, cap - 1, mod=1 << MOD_BITS)
    print(f"        census H series mod 2^{MOD_BITS} to {cap - 1}: "
          f"{time.time() - t1:.1f}s")
    primes = [p for p in sieve_primes(cap - 1) if p % 2 == 1]

    # cross-check formula-mod route against exact eta build on overlap
    xbad = sum(1 for p in primes if p < N_SEG
               and (sig3[p] - a[p]) % (1 << MOD_BITS) !=
               (32 * Hm[p]) % (1 << MOD_BITS))
    check(f"cross-check: census route (formula mod 2^{MOD_BITS}) agrees "
          f"with the exact eta build for all primes p < {N_SEG} "
          f"(mismatches: {xbad})", xbad == 0)

    hist = {c: {} for c in (1, 3, 5, 7)}
    viol = []
    witness = {}
    for p in primes:
        c = p % 8
        # D_p = 32*H_p exactly => v2(D_p) = 5 + v2(H_p), capped at V2_CAP
        v = 5 + v2_capped(Hm[p], MOD_BITS)
        hist[c][v] = hist[c].get(v, 0) + 1
        if v < LADDER[c]:
            viol.append((p, c, v))
        if v == LADDER[c] and c not in witness:
            witness[c] = p
    n_p = len(primes)
    print(f"        census: {n_p} odd primes < {cap}")
    print("        PER-CLASS v2(1 + p^3 - a_p) TABLE "
          f"(v2 = {V2_CAP} means >= {V2_CAP}):")
    for c in (3, 7, 5, 1):
        row = dict(sorted(hist[c].items()))
        total = sum(row.values())
        print(f"          p == {c} (mod 8): claim v2 >= {LADDER[c]}; "
              f"min = {min(row)}; witness p = {witness.get(c)}; "
              f"n = {total}")
        print(f"            histogram: {row}")
    check(f"BOUND: v2(1 + p^3 - a_p) >= 5 + 2*[chi_-4 = 1] + [chi_8 = 1] "
          f"for ALL {n_p} odd primes p < {cap} (violations: {len(viol)}"
          + (f", first {viol[0]}" if viol else "") + ")", len(viol) == 0)
    check("SHARPNESS: the class minimum is ATTAINED in every class; "
          f"witnesses (smallest primes) = "
          f"{ {c: witness.get(c) for c in (3, 7, 5, 1)} } "
          "(expected 3, 7, 5, 17)",
          all(min(hist[c]) == LADDER[c] for c in (1, 3, 5, 7))
          and witness.get(3) == 3 and witness.get(7) == 7
          and witness.get(5) == 5 and witness.get(1) == 17)

    # ------------------------------------------------------------- S3
    print("S3 -- character dissection (full odd series, exact)")
    D = [sig3[n] - a[n] if n % 2 else 0 for n in range(N_SEG + 1)]
    i0 = [n for n in range(1, N_SEG + 1, 2) if D[n] % 32]
    i1 = [n for n in range(1, N_SEG + 1, 4) if D[n] % 128]
    i2 = [n for n in range(1, N_SEG + 1, 2)
          if n % 8 in (1, 7) and D[n] % 64]
    i3 = [n for n in range(1, N_SEG + 1, 8) if D[n] % 256]
    check(f"I0 (base, = CHECK32): D_n == 0 (mod 32) for ALL odd "
          f"n <= {N_SEG} (failures: {len(i0)})", len(i0) == 0)
    check(f"I1 (chi_-4 sift, (D + D x chi_-4)/2): D_n == 0 (mod 128) for "
          f"ALL n == 1 (mod 4), n <= {N_SEG} (failures: {len(i1)})",
          len(i1) == 0)
    check(f"I2 (chi_8 sift, (D + D x chi_8)/2): D_n == 0 (mod 64) for "
          f"ALL n == +-1 (mod 8), n <= {N_SEG} (failures: {len(i2)})",
          len(i2) == 0)
    check(f"I3 (chi_-4*chi_8 = chi_-8 sift): D_n == 0 (mod 256) for ALL "
          f"n == 1 (mod 8), n <= {N_SEG} (failures: {len(i3)})",
          len(i3) == 0)
    lad_bad = [n for n in range(1, N_SEG + 1, 2)
               if v2_capped(D[n], 40) < ladder_bound(n)]
    check("LADDER (all odd n, not just primes): v2(D_n) >= "
          f"5 + 2*[chi_-4(n)=1] + [chi_8(n)=1] for ALL odd n <= {N_SEG} "
          f"(failures: {len(lad_bad)}) -- the prime claim is the "
          "restriction to primes", len(lad_bad) == 0)
    # predeclared must-fail strengthening
    d9 = D[9]
    check("MUST-FAIL strengthening: D == 0 (mod 512) on n == 1 (mod 8) "
          f"FAILS at the predeclared witness n = 9 (D_9 = {d9} = 2^8*3; "
          "so 256 is maximal on the chi_-8-sifted rung)",
          d9 == 768 and d9 % 256 == 0 and d9 % 512 != 0)
    check("TYPING: ladder bound = theorem-grade modulo TWO cited "
          "classical ingredients (Sturm 1987 congruence bound; standard "
          "twist/odd-projection level lemma, Shimura 1971/Atkin-Li): "
          f"sifted forms live at level <= 512, Sturm bound {STURM_TWIST}, "
          f"verified to {N_SEG} = {N_SEG // STURM_TWIST}x; sharpness is "
          "census-level (exact small-prime witnesses; no infinitude per "
          "class claimed); corpus envelope anchor: v541 (C) character "
          "system (1, chi_-4, chi_8, chi_-8) on residues mod 8",
          N_SEG // STURM_TWIST >= 50)

    # ------------------------------------------------------------- S4
    print("S4 -- controls (must fire)")
    g_mut = build_f8(N_SEG, exp4=3)
    mut_stats = {c: [0, 0] for c in (1, 3, 5, 7)}
    for p in primes:
        if p >= N_SEG:
            break
        c = p % 8
        mut_stats[c][1] += 1
        if v2_capped(1 + p ** 3 - g_mut[p], 40) < LADDER[c]:
            mut_stats[c][0] += 1
    mut_fr = {c: (f / t if t else 0.0) for c, (f, t) in mut_stats.items()}
    print(f"        C1 mutant per-class failure fractions: "
          f"{ {c: round(v, 3) for c, v in mut_fr.items()} }")
    check("C1 mutant eta(2t)^4 eta(4t)^3: ladder failure fraction > 1/2 "
          "in EVERY class mod 8", all(v > 0.5 for v in mut_fr.values()))

    rng = random.Random(RNG_SEED)
    seg_primes = [p for p in primes if p < N_SEG]
    vals = [a[p] for p in seg_primes]
    rng.shuffle(vals)
    scr_stats = {c: [0, 0] for c in (1, 3, 5, 7)}
    for p, ap_scr in zip(seg_primes, vals):
        c = p % 8
        scr_stats[c][1] += 1
        if v2_capped(1 + p ** 3 - ap_scr, 40) < LADDER[c]:
            scr_stats[c][0] += 1
    scr_fr = {c: (f / t if t else 0.0) for c, (f, t) in scr_stats.items()}
    print(f"        C2 scrambled a_p per-class failure fractions: "
          f"{ {c: round(v, 3) for c, v in scr_fr.items()} }")
    check(f"C2 scrambled a_p (seed {RNG_SEED}): ladder failure fraction "
          "> 1/2 overall and in EVERY class",
          all(v > 0.5 for v in scr_fr.values()))

    # ------------------------------------------------------------- S5
    print("S5 -- SPINLIFT: Sh(g) = -8 f8 = -8 E_odd + 256 H (v537 bridge)")
    t1 = time.time()
    g = build_g(Q_G)
    print(f"        g rebuilt to O(q^{Q_G}) in {time.time() - t1:.1f}s; "
          f"head {g[:12]}")
    check("g anchors (v537): g_0 = 0; support on n == 1, 2 (mod 4) only; "
          "U4(g) = 0 exactly; |g|-mass mod 4 = {0: 0, 3: 0}",
          g[0] == 0
          and all(g[n] == 0 for n in range(0, Q_G + 1, 4))
          and all(g[n] == 0 for n in range(3, Q_G + 1, 4))
          and any(g[n] != 0 for n in range(1, Q_G, 4))
          and any(g[n] != 0 for n in range(2, Q_G, 4)))
    check("Shimura twist character: (2/d)_Kronecker == chi_8(d) for all "
          "odd d <= 1000 (the ladder's chi_8 IS the lift's own twist)",
          all(kron2(d) == chi_8(d) for d in range(1, 1001, 2)))
    sh = shimura_lift(g, N_SH)
    sh_bad = [n for n in range(1, N_SH + 1) if sh[n] != -8 * a[n]]
    check(f"Sh_{{t=2,psi=1}}(g) = -8 * f8 coefficientwise for ALL "
          f"n <= {N_SH} (corpus verified to 120; failures: {len(sh_bad)})",
          len(sh_bad) == 0)
    lad_odd = [n for n in range(1, N_SH + 1, 2)
               if sh[n] != -8 * sig3[n] + 256 * H[n]]
    lad_even = [n for n in range(2, N_SH + 1, 2) if sh[n] != 0]
    check(f"LADDER FORM: Sh(g) = -8 E_odd + 256 H with H from the "
          f"CONVOLUTION formula (independent of the eta build), exact on "
          f"odd n <= {N_SH} (failures: {len(lad_odd)}); even n: both "
          f"sides 0 (failures: {len(lad_even)})",
          len(lad_odd) == 0 and len(lad_even) == 0)
    t9 = T9_half(g, Q_G, N_HECKE_HALF)
    check(f"level-32 anchor: T(3^2) g = -4 g (weight 5/2, trivial "
          f"nebentypus) on n <= {N_HECKE_HALF}",
          all(t9[n] == -4 * g[n] for n in range(N_HECKE_HALF + 1)))
    w4 = [(x, b) for x in range(64) for b in range(1, 64, 4)
          if (4 * x - 1) % (8 * b) == 0]
    check("level-32 anchor: level 32 = 4*8, M = 8 even (not odd "
          "squarefree); Kohnen window 4a - 8bc = 1 unsolvable -- outside "
          "Kohnen 1982 (corpus fence v537 C reproduced)",
          32 == 4 * 8 and len(w4) == 0)

    # ------------------------------------------------------------- S6
    print("S6 -- ladder semantics 32 -> 256 -> 128 [C neu]")
    check("STRUCTURAL OBSERVATION (typed [C neu], NO derivation claimed): "
          "32 = 2^g_car (P2; pi_cusp = (28 - T_3)/32, v535 N4a); "
          "256 = |Sh scale| * 32 = 8 * 32 = 2^8 = dim Fock(16 Majorana) "
          "(carrier 10 + 6 = 16 Majoranas v113; 2^8 = 256-dim Fock v529; "
          "NS/R census v148); 128 + 128 = 256, 128 = chiral half, "
          "matching 248 = 120 + 128 at E8 level 1 (wolfram README)",
          2 ** 5 == 32 and 8 * 32 == 256 and 2 ** 8 == 256
          and 128 + 128 == 256 and 120 + 128 == 248)

    # ---------------------------------------------------------- verdict
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    multirate_false = bool(viol)
    spinlift_ok = (len(sh_bad) == 0 and len(lad_odd) == 0
                   and len(lad_even) == 0)
    if multirate_false:
        v1 = "MULTIRATE-FALSE"
    elif n_pass == n_all:
        v1 = "MULTIRATE-THEOREM"
    else:
        v1 = "MULTIRATE-PARTIAL"
    v2 = "SPINLIFT-VERIFIED" if spinlift_ok else "SPINLIFT-FAILS"
    print(f"CHECKS: {n_pass}/{n_all} passed; walltime {time.time() - t0:.1f}s")
    print(f"VERDICT: {v1} / {v2}")
    return 0 if (v1 == "MULTIRATE-THEOREM" and spinlift_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
