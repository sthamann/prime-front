#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hecke_halving_tails_probe -- HECKE.HALVINGTAILS.01: the exact-depth
mechanism for the classes p == 7 and p == 1 (mod 8).

Follow-up to HECKE.CONSTDEPTH.01 (constant depth in classes 3, 5 mod 8)
on the both-odd convolution identity
    H_n = sum_{a + 2c = n, a, c odd} sigma(a) sigma(c),
    D_n = sigma3(n) - a_n = 32 * H_n        (multirate formula).

DERIVED MECHANISM (frozen; hand-derivation summarised, every step gated):

  BRANCH TABLES (pure residue bookkeeping on the line a + 2c = p):
    p == 7 (mod 8):  c == 1,5 (mod 8) -> a == 5 (mod 8);
                     c == 3,7 (mod 8) -> a == 1 (mod 8).
    p == 1 (mod 8):  c == 1,5 -> a == 7 (mod 8);  c == 3,7 -> a == 3.
  With the sigma 2-adic classification lemmas (v2(sigma(m)) for odd m:
  = 0 iff m square; = 1 => m == 1,5 mod 8; m == 3 mod 8 => >= 2;
  m == 7 mod 8 => >= 3), the per-term valuations satisfy:
    class 7: every term sigma(a)sigma(c) is EVEN (min total valuation 1,
             attained exactly on the stratum {c = y^2 odd,
             v2(sigma(p - 2y^2)) = 1});
    class 1: every term is divisible by 8 (min valuation 3, attained
             exactly on {c = y^2 odd, v2(sigma(p - 2y^2)) = 3}; the
             a == 3 branch has >= 2 + 2 = 4).

  THE EXPLICIT DIVISOR SUMS (the deliverable objects):
    X7(p) := sum_{c odd, 2c < p} sigma(p - 2c) sigma(c) / 2   (termwise
             integral by the above), and EXACTLY
                 v2(D_p) = 6 + v2(X7(p))        for p == 7 (mod 8);
    X1(p) := sum_{c odd, 2c < p} sigma(p - 2c) sigma(c) / 8   (termwise
             integral), and EXACTLY
                 v2(D_p) = 8 + v2(X1(p))        for p == 1 (mod 8).
    (D = 64 X7 = 256 X1 identically; the CONTENT is the termwise
    divisibility theorem -- it re-proves the parent ladder bounds >= 6
    resp. >= 8 elementarily -- plus base sharpness.)

  BASE CRITERIA (minimal-stratum parity):
    X7 == M7(p) (mod 2),  M7 = #{y odd >= 1: v2(sigma(p - 2y^2)) = 1};
    via the chi_-4 bridge on a == 5 (mod 8) ({v2 sigma = 1} =
    {rho4 == 2 mod 4}, rho4 = sum_{d|m} chi_-4(d)) and the slice count
    r2 = 4 rho4 [N2], M7 == R3(p)/16 (mod 2) for the h = 1 ternary form
        R3(p) = #{(x,y,z) in Z^3 : x^2 + y^2 + 2z^2 = p}
    (z odd is automatic for p == 7 mod 8).  Hence
        v2(D_p) = 6  <=>  R3(p) == 16 (mod 32).
    Hand-checked: p = 7 (R3 = 16, v2 = 6), p = 23 (16, 6),
    p = 31 (32, 8), p = 47 (32, 7).
    X1 == M1(p) (mod 2),  M1 = #{y odd >= 1: v2(sigma(p - 2y^2)) = 3};
    the stratum {a == 7 mod 8, v2 sigma(a) = 3} has EXACTLY TWO shapes
    (via v2(sigma(q^e)) = v2(q+1) + v2((e+1)/2), an LTE-elementary
    lemma):  a = q^e z^2 (q == 7 mod 16, e == 1 mod 4)  OR
    a = q1^e1 q2^e2 z^2 (q1 == 3, q2 == 5 mod 8, e1, e2 == 1 mod 4).
    [The mod-16 refinement in shape 1 was CAUGHT BY THE LEMMA CENSUS in
    run 1 (13080 mismatches from the too-broad q == 7 mod 8): v2(q+1)
    = 3 exactly iff q == 7 (mod 16); e.g. v2(sigma(31)) = 5.]
    Hand-checked: p = 17 (M1 = 1, v2 = 8), p = 41 (M1 = 2, v2 = 9),
    p = 73 (M1 = 3, v2 = 8).
    TYPED OPEN: a single-character bridge for the class-1 stratum does
    NOT exist (chi_-8, chi_-4 and the disc -32 genus-character
    convolution all vanish identically on both shapes -- shown in the
    derivation); reducing M1-parity to one classical h = 1 count
    remains OPEN.  The two-shape criterion itself is exact and censused.

  TAIL LAW (measured, NOT gated): if the minimal-stratum residuals
  equidistribute 2-adically, P(v2(X) = k) = 2^{-k-1} -- the observed
  geometric halving tails.  The equidistribution is a Chebotarev/
  Sato-Tate-flavoured expectation for the 2-adic residual of a non-CM
  weight-4 eigenform; it is CITED as heuristic and MEASURED here, not
  claimed.

PREDECLARED GATES:
  G0 scaffolding (eta build == parent convolution).
  G1 lemma censuses: (L0-LTE) v2(sigma(m)) == sum over odd-exponent
     primes of v2(q+1) + v2((e+1)/2), ALL odd m <= 10^6 (SPF factor-
     isation vs sigma table); (L6) on m == 5 (mod 8): {v2 sigma = 1} ==
     {rho4 == 2 (mod 4)}; (L7) on m == 7 (mod 8): v2 sigma >= 3 and
     {v2 sigma = 3} == the two-shape set (SPF census), ALL m <= 10^6.
  G2 termwise divisibility on the segment (every term even / == 0 mod
     8) for ALL n == 7 resp. 1 (mod 8), n <= 20000 -- composites
     included (the mechanism is residue-driven).
  G3 exact identities: D == 64 X7 == 2^6 * X7 (class 7) and D == 256 X1
     (class 1) on the segment; 10^6 census: v2(H_p) >= 1 resp. >= 3
     with ZERO exceptions; bases attained: min v2(D) == 6 (witness
     p = 7, X7(7) = 5 odd) resp. == 8 (witness p = 17, X1(17) = 19).
  G4 base criterion class 7: [v2(H_p) = 1] <=> M7(p) odd for ALL
     p == 7 (mod 8) < 10^5; M7 == R3/16 (mod 2) via the rho4 slice sum
     (S even, M7 == S/2 mod 2); R3 == 8*S by brute-force ternary
     enumeration for p <= 3000.
  G5 base criterion class 1: [v2(H_p) = 3] <=> M1(p) odd for ALL
     p == 1 (mod 8) < 10^5.
  G6 tail law: histograms of v2(X7), v2(X1) at 10^6 vs geometric
     2^{-k-1} -- REPORTED with deviations, not gated.
  G7 controls: (C1) k = 3 mutant does not telescope (predeclared first
     mismatch n = 10); (C2) wrong-base mutants fail: base 7 in class 7
     (termwise 4-divisibility fails at (p, c) = (7, 1), term
     sigma(5)sigma(1) = 6; census min stays 6) and base 9 in class 1
     (16-divisibility fails at (17, 1), term sigma(15)sigma(1) = 24;
     census min stays 8); (C3) HONEST composite scope: the 7/1
     identities are residue-driven and EXTEND to composites (verified
     on the segment, including the base criterion [v2 = 6 <=> M7 odd]
     for ALL odd n == 7 mod 8) -- contrasted with classes 3/5 where
     composites DO break the constant depth (prime-pinned h = 1
     counts; witness n = 27 re-confirmed).  The task-sheet control
     "composites break the identity" is therefore replaced by the
     verified statement of what composites do and do not break.

VERDICT ENUM (frozen):
  TAILS-IDENTIFIED : exact X identities census-clean in both classes,
                     base criteria certified, tail law measured.
  TAILS-PARTIAL    : some gate degraded, no counterexample.
  TAILS-OPEN       : the identity or strata derivation fails.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.
"""
from __future__ import annotations

import time

from hecke_check32_probe import build_f8, embed, sieve_primes, sieve_sigma3
from hecke_multirate2adic_probe import (h_series, kron_mul_fast,
                                        sieve_sigma1, v2_capped)
from hecke_constant_depth_probe import sieve_rho4

# ---------------------------------------------------------------- budgets
N_SEG = 20_000        # exact segment (termwise loops, X integrality)
N_INST = 100_000      # per-prime base-criterion census
N_BRUTE_T = 3_000     # brute-force ternary enumeration bound
N_CTL = 5_000         # k = 3 mutant control range
CAP = 1_000_000       # full census
MOD_BITS = 20
BASE = {7: 6, 1: 8}                 # class mod 8 -> exact 2-adic base
HBASE = {7: 1, 1: 3}                # same, on H = D/32
WITNESS = {7: 7, 1: 17}             # base-sharpness witness primes
K3_FIRST_MISMATCH = 10
HIST_KMAX = 10

CHECKS = []


def check(label: str, ok: bool) -> bool:
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return bool(ok)


def sieve_spf(n_max):
    spf = list(range(n_max + 1))
    i = 2
    while i * i <= n_max:
        if spf[i] == i:
            for j in range(i * i, n_max + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def factor_odd(m, spf):
    out = []
    while m > 1:
        q = spf[m]
        e = 0
        while m % q == 0:
            m //= q
            e += 1
        out.append((q, e))
    return out


def v2_of(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


# ================================================================== run
def main():
    t0 = time.time()
    print("hecke_halving_tails_probe -- HECKE.HALVINGTAILS.01")
    print("  claim: v2(D_p) = 6 + v2(X7(p)) [p == 7 mod 8], "
          "= 8 + v2(X1(p)) [p == 1 mod 8]")

    # ------------------------------------------------------------- P0
    print("P0 -- scaffolding")
    a = build_f8(N_SEG)
    sig3 = sieve_sigma3(N_SEG)
    sig1 = sieve_sigma1(N_SEG)
    H = h_series(sig1, N_SEG)
    check("scaffold: sigma3(n) - a_n == 32 H_n (parent convolution) on "
          f"odd n <= {N_SEG}",
          all(sig3[n] - a[n] == 32 * H[n] for n in range(1, N_SEG + 1, 2)))

    # ------------------------------------------------------------- P1
    print("P1 -- lemma censuses (L0-LTE, L6, L7) at 10^6")
    t1 = time.time()
    sig1_big = sieve_sigma1(CAP)
    vs = [0] * (CAP + 1)
    for m in range(1, CAP + 1, 2):
        vs[m] = v2_capped(sig1_big[m], 6)          # 6 means >= 6
    spf = sieve_spf(CAP)
    rho4 = sieve_rho4(CAP)
    print(f"        sieves (sigma1, v2, SPF, rho4) to {CAP}: "
          f"{time.time() - t1:.1f}s")
    t1 = time.time()
    l0_bad = 0
    l7_bad = 0
    for m in range(3, CAP + 1, 2):
        fac = factor_odd(m, spf)
        v_formula = 0
        odd_exp = []
        for q, e in fac:
            if e % 2 == 1:
                v_formula += v2_of(q + 1) + v2_of((e + 1) // 2)
                odd_exp.append((q, e))
        if min(v_formula, 6) != vs[m]:
            l0_bad += 1
        if m % 8 == 7:
            shape1 = (len(odd_exp) == 1 and odd_exp[0][0] % 16 == 7
                      and odd_exp[0][1] % 4 == 1)
            shape2 = (len(odd_exp) == 2
                      and {odd_exp[0][0] % 8, odd_exp[1][0] % 8} == {3, 5}
                      and odd_exp[0][1] % 4 == 1 and odd_exp[1][1] % 4 == 1)
            if (vs[m] == 3) != (shape1 or shape2):
                l7_bad += 1
    print(f"        factorisation census: {time.time() - t1:.1f}s")
    check(f"L0 (LTE lemma): v2(sigma(m)) == sum over odd-exponent primes "
          f"of v2(q+1) + v2((e+1)/2), ALL odd m <= {CAP} "
          f"(mismatches: {l0_bad})", l0_bad == 0)
    check(f"L6: on m == 5 (mod 8): {{v2 sigma = 1}} == {{rho4 == 2 "
          f"(mod 4)}}, ALL m <= {CAP}",
          all((vs[m] == 1) == (rho4[m] % 4 == 2)
              for m in range(5, CAP + 1, 8)))
    check(f"L7: on m == 7 (mod 8): v2 sigma >= 3, and {{v2 sigma = 3}} == "
          f"two-shape set {{q^(e=1 mod 4) z^2, q = 7 mod 16}} u "
          f"{{q1^e1 q2^e2 z^2, (q1,q2) = (3,5) mod 8, e_i = 1 mod 4}}, "
          f"ALL m <= {CAP} (mismatches: {l7_bad})",
          l7_bad == 0 and all(vs[m] >= 3 for m in range(7, CAP + 1, 8)))

    # ------------------------------------------------------------- P2
    print("P2 -- termwise divisibility theorem (segment, composites incl.)")
    bad7 = []
    bad1 = []
    for n in range(7, N_SEG + 1, 2):
        r = n % 8
        if r not in (1, 7):
            continue
        need = HBASE[r]
        for c in range(1, (n - 1) // 2 + 1, 2):
            t = sig1[n - 2 * c] * sig1[c]
            if t % (1 << need) != 0:
                (bad7 if r == 7 else bad1).append((n, c))
                break
    check(f"class 7: EVERY term sigma(a)sigma(c) of H_n is even, for ALL "
          f"n == 7 (mod 8) <= {N_SEG} incl. composites "
          f"(violations: {len(bad7)})", len(bad7) == 0)
    check(f"class 1: EVERY term divisible by 8, for ALL n == 1 (mod 8) "
          f"<= {N_SEG} incl. composites (violations: {len(bad1)})",
          len(bad1) == 0)
    check("branch bookkeeping (exhaustive residue table): p == 7: "
          "(a,c) == (5,{1,5}) or (1,{3,7}) mod 8; p == 1: (7,{1,5}) or "
          "(3,{3,7}) -- minima 1 resp. 3 by L0/L6/L7 classification",
          all((7 - 2 * c) % 8 == (5 if c % 8 in (1, 5) else 1)
              for c in (1, 3, 5, 7))
          and all((1 - 2 * c) % 8 == (7 if c % 8 in (1, 5) else 3)
                  for c in (1, 3, 5, 7)))

    # ------------------------------------------------------------- P3
    print("P3 -- the exact divisor-sum identities + 10^6 census")
    x7_17 = H[7] // 2
    x1_17 = H[17] // 8
    check("segment identities: D_n == 64 * X7(n) with X7 = H/2 integral "
          "(n == 7 mod 8) and D_n == 256 * X1(n) with X1 = H/8 integral "
          f"(n == 1 mod 8), ALL n <= {N_SEG}; witnesses X7(7) = "
          f"{x7_17} (odd), X1(17) = {x1_17} (odd)",
          all(H[n] % 2 == 0 and sig3[n] - a[n] == 64 * (H[n] // 2)
              for n in range(7, N_SEG + 1, 8))
          and all(H[n] % 8 == 0 and sig3[n] - a[n] == 256 * (H[n] // 8)
                  for n in range(9, N_SEG + 1, 8))
          and x7_17 == 5 and x1_17 == 19)
    t1 = time.time()
    Hm = h_series(sig1_big, CAP - 1, mod=1 << MOD_BITS)
    print(f"        census H mod 2^{MOD_BITS} to {CAP - 1}: "
          f"{time.time() - t1:.1f}s")
    primes = [p for p in sieve_primes(CAP - 1) if p % 2 == 1]
    v7 = {p: v2_capped(Hm[p], MOD_BITS) for p in primes if p % 8 == 7}
    v1 = {p: v2_capped(Hm[p], MOD_BITS) for p in primes if p % 8 == 1}
    check(f"census: v2(H_p) >= 1 for ALL {len(v7)} primes p == 7 (mod 8) "
          f"< {CAP} (=> X7 integral; exceptions: "
          f"{sum(1 for v in v7.values() if v < 1)})",
          all(v >= 1 for v in v7.values()))
    check(f"census: v2(H_p) >= 3 for ALL {len(v1)} primes p == 1 (mod 8) "
          f"< {CAP} (=> X1 integral; exceptions: "
          f"{sum(1 for v in v1.values() if v < 3)})",
          all(v >= 3 for v in v1.values()))
    check("bases attained: min v2(D_p) == 6 in class 7 (witness p = 7) "
          "and == 8 in class 1 (witness p = 17)",
          min(v7.values()) == 1 and v7[WITNESS[7]] == 1
          and min(v1.values()) == 3 and v1[WITNESS[1]] == 3)

    # ------------------------------------------------------------- P4
    print("P4 -- base criteria (minimal-stratum parity)")
    primes_inst = [p for p in primes if p < N_INST]

    def m_count(p, level):
        cnt = 0
        y = 1
        while 2 * y * y < p:
            if vs[p - 2 * y * y] == level:
                cnt += 1
            y += 2
        return cnt

    p7 = [p for p in primes_inst if p % 8 == 7]
    bad_m7 = [p for p in p7 if (v2_capped(Hm[p], MOD_BITS) == 1)
              != (m_count(p, 1) % 2 == 1)]
    check(f"class 7 criterion: v2(D_p) = 6 <=> M7(p) odd, M7 = #{{y odd: "
          f"v2(sigma(p-2y^2)) = 1}}, ALL {len(p7)} primes p == 7 (mod 8) "
          f"< {N_INST} (failures: {len(bad_m7)})", len(bad_m7) == 0)
    bad_s = []
    for p in p7:
        S = 0
        y = 1
        while 2 * y * y < p:
            S += rho4[p - 2 * y * y]
            y += 2
        if S % 2 != 0 or (S // 2) % 2 != m_count(p, 1) % 2:
            bad_s.append(p)
    check(f"chi_-4 bridge: S = sum_y rho4(p - 2y^2) is even and "
          f"M7 == S/2 == R3(p)/16 (mod 2), ALL p == 7 (mod 8) < {N_INST} "
          f"(failures: {len(bad_s)})", len(bad_s) == 0)
    # brute-force ternary anchor: R3 = 8 * S for p <= N_BRUTE_T
    r3 = [0] * (N_BRUTE_T + 1)
    xm = int(N_BRUTE_T ** 0.5) + 1
    for x in range(-xm, xm + 1):
        for y in range(-xm, xm + 1):
            n0 = x * x + y * y
            if n0 > N_BRUTE_T:
                continue
            z = 0
            while n0 + 2 * z * z <= N_BRUTE_T:
                if z == 0:
                    r3[n0] += 1
                else:
                    r3[n0 + 2 * z * z] += 2
                z += 1
    bad_r3 = []
    for p in [q for q in p7 if q <= N_BRUTE_T]:
        S = sum(rho4[p - 2 * y * y]
                for y in range(1, int((p / 2) ** 0.5) + 1, 2)
                if 2 * y * y < p)
        if r3[p] != 8 * S or (r3[p] % 32 == 16) != (v2_capped(
                Hm[p], MOD_BITS) == 1):
            bad_r3.append(p)
    check(f"ternary anchor [N2]: R3(p) = #(x^2+y^2+2z^2 = p) == 8*S by "
          f"brute enumeration, and v2(D_p) = 6 <=> R3(p) == 16 (mod 32), "
          f"ALL p == 7 (mod 8) <= {N_BRUTE_T} (failures: {len(bad_r3)}); "
          "hand witnesses R3(7) = 16, R3(31) = 32",
          len(bad_r3) == 0 and r3[7] == 16 and r3[31] == 32)
    p1 = [p for p in primes_inst if p % 8 == 1]
    bad_m1 = [p for p in p1 if (v2_capped(Hm[p], MOD_BITS) == 3)
              != (m_count(p, 3) % 2 == 1)]
    check(f"class 1 criterion: v2(D_p) = 8 <=> M1(p) odd, M1 = #{{y odd: "
          f"v2(sigma(p-2y^2)) = 3}} (two-shape stratum, L7), ALL "
          f"{len(p1)} primes p == 1 (mod 8) < {N_INST} "
          f"(failures: {len(bad_m1)})", len(bad_m1) == 0)
    check("TYPING: class-7 chain closes with [N2] (r2 = 4 rho4, disc -4, "
          "h = 1) like the parent; class-1 minimal stratum is EXACT and "
          "censused (L7) but its reduction to a single classical h = 1 "
          "count is OPEN (chi_-8, chi_-4 and the disc -32 genus "
          "convolution vanish on both shapes); tail equidistribution is "
          "cited (Chebotarev/Sato-Tate-flavoured), MEASURED not claimed",
          True)

    # ------------------------------------------------------------- P5
    print("P5 -- tail law (measured, NOT gated)")
    for label, vv, base in (("class 7 (X7)", v7, 1), ("class 1 (X1)", v1, 3)):
        n_tot = len(vv)
        hist = {}
        for v in vv.values():
            k = v - base
            hist[k] = hist.get(k, 0) + 1
        print(f"        {label}: v2(X) histogram vs geometric 2^(-k-1), "
              f"n = {n_tot}")
        max_dev = 0.0
        for k in range(HIST_KMAX + 1):
            obs = hist.get(k, 0) / n_tot
            exp = 2.0 ** (-k - 1)
            dev = abs(obs / exp - 1) if exp else 0.0
            if k <= 8:
                max_dev = max(max_dev, dev)
            print(f"          k={k:2d}: n={hist.get(k, 0):6d}  "
                  f"obs={obs:.5f}  geom={exp:.5f}  ratio={obs / exp:.3f}")
        ratios = [hist.get(k, 0) / hist.get(k + 1, 1)
                  for k in range(6)]
        print(f"          halving ratios n_k/n_(k+1), k=0..5: "
              f"{[round(r, 3) for r in ratios]}; max |obs/geom - 1| "
              f"(k <= 8): {max_dev:.3f}")
    check("tail law recorded: histograms and halving ratios printed for "
          "both classes; equidistribution typed as cited heuristic "
          "(statistics reported, not gated)", True)

    # ------------------------------------------------------------- P6
    print("P6 -- controls")
    sig1_c = sig1[:N_CTL + 1]
    L = [0] + [sig1_c[n] for n in range(1, N_CTL + 1)]
    L_no3 = [0] + [sig1_c[n] if n % 3 else 0 for n in range(1, N_CTL + 1)]
    h3 = kron_mul_fast(L, embed(L, 3, N_CTL), N_CTL)
    w19 = kron_mul_fast(L, embed(L, 9, N_CTL), N_CTL)
    w127 = kron_mul_fast(L, embed(L, 27, N_CTL), N_CTL)
    u13 = kron_mul_fast(L, embed(L_no3, 3, N_CTL), N_CTL)
    mism = [n for n in range(1, N_CTL + 1)
            if h3[n] - 3 * w19[n] + 2 * w127[n] != u13[n]]
    check(f"C1 k = 3 mutant does not telescope: first mismatch at "
          f"n = {mism[0] if mism else None} (predeclared "
          f"{K3_FIRST_MISMATCH}), {len(mism)} mismatches on n <= {N_CTL}",
          len(mism) > 0 and mism[0] == K3_FIRST_MISMATCH)
    t71 = sig1[5] * sig1[1]
    t171 = sig1[15] * sig1[1]
    check("C2 wrong-base mutants fail: base 7 in class 7 -- term "
          f"sigma(5)sigma(1) = {t71} not divisible by 4, census min "
          "v2(D) stays 6; base 9 in class 1 -- term sigma(15)sigma(1) = "
          f"{t171} not divisible by 16, census min stays 8",
          t71 % 4 != 0 and min(v7.values()) == 1
          and t171 % 16 != 0 and min(v1.values()) == 3)
    prime_set = set(primes_inst)
    comp7 = [n for n in range(15, N_SEG + 1, 8) if n not in prime_set]
    bad_c7 = [n for n in comp7
              if (v2_capped(sig3[n] - a[n], 40) == 6)
              != (m_count(n, 1) % 2 == 1)]
    d27 = sig3[27] - a[27]
    check("C3 HONEST composite scope: the class-7 identity and base "
          f"criterion EXTEND to composites (all {len(comp7)} composite "
          f"n == 7 (mod 8) <= {N_SEG}: [v2(D)=6 <=> M7 odd], failures: "
          f"{len(bad_c7)}) -- residue-driven mechanism; CONTRAST: in "
          "class 3 composites DO break the constant depth (witness "
          f"n = 27: v2(D) = {v2_capped(d27, 40)} != 5, prime-pinned "
          "h = 1 count lost)",
          len(bad_c7) == 0 and v2_capped(d27, 40) == 6)

    # ---------------------------------------------------------- verdict
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    identity_ok = (all(v >= 1 for v in v7.values())
                   and all(v >= 3 for v in v1.values())
                   and len(bad7) == 0 and len(bad1) == 0)
    if not identity_ok:
        verdict = "TAILS-OPEN"
    elif n_pass == n_all:
        verdict = "TAILS-IDENTIFIED"
    else:
        verdict = "TAILS-PARTIAL"
    print(f"CHECKS: {n_pass}/{n_all} passed; walltime {time.time() - t0:.1f}s")
    print(f"VERDICT: {verdict}")
    return 0 if verdict == "TAILS-IDENTIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
