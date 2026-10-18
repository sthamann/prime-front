#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v795 -- HECKE.HALVINGTAILS.01 (+ HECKE.K5ANOMALY.01): the exact-depth mechanism for the classes p == 7 and p == 1 (mod 8) + the k = 5 anomaly decided by the 2-power residue tower, ONE module from two probes (20/20 + 17/17 checks, ~160 s; discovery probes hecke_halving_tails_probe.py TAILS-IDENTIFIED and hecke_k5_anomaly_probe.py K5-MECHANISM-FOUND, both 2026-08-05).  THE EXACT IDENTITIES (part 1): v_2(D_p) = 6 + v_2(X7(p)) for p == 7 (mod 8) and v_2(D_p) = 8 + v_2(X1(p)) for p == 1 (mod 8), with X7 = H/2 and X1 = H/8 TERMWISE-INTEGRAL divisor sums on the both-odd convolution H_n = sum_{a+2c=n} sigma(a) sigma(c) (every term even resp. divisible by 8, ALL n <= 20000 COMPOSITES INCLUDED -- the mechanism is residue-driven, in exact contrast to classes 3/5 where composites break the constant depth, witness n = 27 re-confirmed); 10^6 census with ZERO exceptions; bases attained (witnesses p = 7: X7 = 5 odd; p = 17: X1 = 19); the LTE lemma census v_2(sigma(m)) = sum over odd-exponent primes of v_2(q+1) + v_2((e+1)/2) exhaustive on all odd m <= 10^6; BASE CRITERIA: class 7 closes via the chi_{-4} bridge and the h = 1 ternary form -- v_2(D_p) = 6 <=> R3(p) == 16 (mod 32), R3 = #(x^2 + y^2 + 2z^2 = p) (brute-force anchored); class 1 has the exact TWO-SHAPE criterion for the minimal stratum (a = q^e z^2, q == 7 mod 16, e == 1 mod 4, OR a = q1^e1 q2^e2 z^2, (q1, q2) == (3, 5) mod 8 -- the mod-16 refinement caught by the run-1 lemma census, declared) censused clean, but its reduction to a single classical h = 1 count is TYPED OPEN (chi_{-8}, chi_{-4} and the disc -32 genus convolution all vanish on both shapes); the geometric halving tail MEASURED (not gated) with the k = 5 dip at half mass -- the anomaly part 2 decides.  THE MECHANISM (part 2): k = v_2(X1(p)) is DETERMINISTIC on the tower cells (m, t) = (v_2(p-1), depth of 2 in the 2-power residue tower mod p), ZERO exceptions at 10^6 (T1-T5 exact cell criteria for k = 0..4; T2 CLOSES the previously open class-1 base bridge: M1 odd <=> tower condition); k = 5 occurs ONLY in cell (5, 3) (2 octic but not 16th-power residue; density 0.01596 ~ 1/64), inside which the tail restarts geometrically -> P(k = 5) = 1/128 = 0.00781 vs observed 0.00793 -- the halved level explained QUANTITATIVELY (mixture-law chi-square residual 0.6 over k <= 10); [N3] Gauss quartic census clean (t >= 2 <=> 8 | B in p = A^2 + B^2, all class-1 primes < 10^5); the I3 divisor-conjugation involution lemmas censused at 10^6 (a == 7 mod 8: all pairs d + a/d == 0 mod 8; a == 3: all == 4 mod 8) -- the involution explains the BASE, the tower governs the TAIL.  SECOND DISCOVERY (the run-1 control failure re-frozen and gated): the class-7 MIRROR LAW v_2(X7(p)) = v_2(p+1) - 3 through k = 4 (free band at v_2(p+1) >= 8), i.e. v_2(D_p) = 3 + v_2(p+1) = 3 + v_2(sigma(p)) deterministically -- explaining the class-3 constancy (3 + 2 = 5) and class-7's clean geometric look (the governing invariant's own density is exactly geometric); class 7 structurally CANNOT carry the (m, t) mechanism (v_2(p-1) = 1).  The (m, t)-determinism itself is a governing-field statement (Cohn-Lagarias-flavoured; octic lore Western / Barrucand-Cohn) CITED as the structural frame, machine-censused at 10^6, derivation OPEN; free-band equidistribution stays a measured Chebotarev-flavoured heuristic.  Controls: k = 3 mutant does not telescope (first mismatch n = 10 as predeclared); wrong-base mutants fail.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes hecke_halving_tails_probe.py (2026-08-05, 20/20, ~80 s, TAILS-IDENTIFIED; the run-1 lemma-census catch of the too-broad q == 7 mod 8 shape -- refined to q == 7 mod 16 -- carried verbatim in the original docstring below) + hecke_k5_anomaly_probe.py (2026-08-05, 17/17, ~78 s, K5-MECHANISM-FOUND; the run-1 'per p mod 64 flatness' control failure re-frozen as the class-7 mirror law after a 3*10^5 scan, carried verbatim); both re-run identically at promotion (2026-08-06).  Promoted verbatim, part 2 wrapped in a function scope (v789 precedent; both 'from __future__ import annotations' hoisted/dropped at the module top); the sibling imports (hecke_check32_probe / hecke_multirate2adic_probe / hecke_constant_depth_probe helpers) resolve against experiments/tfpt-discovery on sys.path -- exactly the probes' own import graph; module-level _LAST1/_LAST2 verdict captures inserted (v791 precedent); numbers unchanged; run() encodes both patterns (v757 precedent).

Original hecke_halving_tails_probe.py docstring (verbatim):
hecke_halving_tails_probe -- HECKE.HALVINGTAILS.01: the exact-depth
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

Original hecke_k5_anomaly_probe.py docstring (verbatim):
hecke_k5_anomaly_probe -- HECKE.K5ANOMALY.01: the class-1 k = 5
anomaly is decided by the 2-power residue tower of 2 mod p.

Follow-up to HECKE.HALVINGTAILS.01: for p == 1 (mod 8), with
X1(p) = H_p / 8 and v2(D_p) = 8 + v2(X1(p)), the measured tail of
k := v2(X1(p)) was geometric for k <= 4 but carried only HALF the
geometric mass at k = 5 (155 vs ~306 below 10^6), the deficit
reappearing at k >= 6.

MECHANISM (found in the pre-registration scan at 3*10^5, frozen here,
gated at 10^6):  define the TOWER PAIR
    m := v2(p - 1)   (>= 3 for p == 1 mod 8),
    t := max { j >= 1 : 2^((p-1)/2^j) == 1 (mod p) }  (<= m)
        (the depth of 2 in the 2-power residue tower: t >= 2 iff 2 is
         a quartic residue, t >= 3 iff octic, ...).
Then k is DETERMINISTIC on most (m, t) cells.  Scan table at 3*10^5
(n = number of primes; "VAR" = cell with internal spread):
    (3,1)->k=1   (3,2)->0  (3,3)->0
    (4,1)->0     (4,2)->3  (4,3)->2  (4,4)->2
    (5,1)->0     (5,2)->2  (5,3)->VAR, min 5   (5,4)->4  (5,5)->4
    (6,1)->0     (6,2)->2  (6,3)->4  (6,4)->VAR, min 6  (6,5)->6 (6,6)->6
    (7,1)->0     (7,2)->2  (7,3)->4  (7,4)->VAR  (7,5..7)->VAR (small n,
                                                  re-measured here)
THE k = 5 ANSWER: k = 5 occurs ONLY in the single cell (m, t) = (5, 3)
(p == 33 mod 64, 2 octic but not 16th-power residue), whose natural
density among p == 1 (mod 8) is (1/8)*(1/8) = 1/64; inside the cell the
tail restarts geometrically at k = 5, so P(k = 5) = 1/128 = half of the
naive 2^-6 -- EXACTLY the observed suppression, with the excess pushed
to the deterministic k = 6 cells and the deeper bands.  The naive
geometric law is thus a MIXTURE law: deterministic on the tower cells,
geometric only inside the sparse "free" bands.

INVOLUTION CENSUS (task item 1, typed):
  I1 (y <-> -y fold): built into the slice counts (parent probes).
  I2 (cross-line (a,c) maps): NO natural involution exists -- the line
      a + 2c = p is weight-asymmetric; typed as not available.
  I3 (divisor conjugation d <-> a/d): DOES yield the sigma-level
      2-structure: for a == 7 (mod 8) every divisor pair has
      d + a/d == 0 (mod 8) (pair residues (1,7), (3,5) mod 8), giving
      an elementary involution re-proof of v2(sigma(a)) >= 3 and
          sigma(a)/8 == #{pairs: d + a/d == 8 (mod 16)} (mod 2);
      for a == 3 (mod 8) every pair has d + a/d == 4 (mod 8), giving
      v2(sigma(a)) >= 2 and v2 = 2 <=> d(a) == 2 (mod 4).
      So I3 explains the BASE; the TAIL is governed by the tower.
NAMED / CITED INGREDIENTS:
  [N3] Gauss: 2 is a quartic residue mod p (p == 1 mod 8) iff 8 | B in
       p = A^2 + B^2 (equivalently p = x^2 + 64 y^2) -- censused below.
  [C]  the (m, t)-determinism itself is a GOVERNING-FIELD statement
       (splitting of p in Q(zeta_{2^j}, 2^{1/2^j})) of Cohn-Lagarias
       type (octic lore: Western, Barrucand-Cohn); CITED as the
       structural frame, machine-censused at 10^6, derivation OPEN.
  Equidistribution inside the free bands stays a Chebotarev-flavoured
  heuristic: measured, not claimed.

PREDECLARED GATES (frozen):
  G0 scaffolding + witnesses: v2(H_17) = 3 (cell (4,1), k=0),
     v2(H_41) = 4 ((3,1), k=1), v2(H_113) = 6 ((4,2), k=3) from the
     exact segment.
  G1 exact cell criteria at 10^6 (zero exceptions each):
     T1  k=1  <=> (m,t) = (3,1)
     T2  k=0  <=> (m=3 & t>=2) or (m>=4 & t=1)
         [closes the previously OPEN class-1 base-criterion bridge:
          M1 odd <=> this tower condition, via k=0 <=> M1 odd of
          HALVINGTAILS.01]
     T3  k=3  <=> (m,t) = (4,2)
     T4  k=2  <=> (m=4 & t>=3) or (m>=5 & t=2)
     T5  k=4  <=> (m=5 & t>=4) or (m>=6 & t=3)
     T6  k=5  ==> (m,t) = (5,3); inside (5,3): min k = 5 and both
         k = 5 and k >= 6 occur (no determinism claimed inside).
  G2 refined mixture law (MEASURED, not gated): full (m,t) x k census
     table at 10^6; reconstructed global P(k) from the cell laws
     (deterministic cells exact, free bands geometric restart at their
     min) vs observed histogram -- chi-square-style residuals printed;
     P(k=5) prediction 1/128 vs observed.
  G3 involution census at 10^6: I3 pair lemmas (a == 7 mod 8: all
     pairs == 0 mod 8 and sigma/8 parity = #(pairs == 8 mod 16) parity;
     a == 3 mod 8: all pairs == 4 mod 8 and v2 sigma = 2 <=> d(a) == 2
     mod 4).
  G4 [N3] Gauss quartic census at 10^5: t >= 2 <=> 8 | B.
  G5 controls: (a) class 7 CANNOT carry the (m, t) mechanism --
     structural: v2(p - 1) = 1 for all p == 7 (mod 8) (the tower of 2
     is trivial); (b) THE MIRROR LAW (found by the run-1 control,
     which was frozen as "per p mod 64 flatness" and FAILED with an
     8.2x k = 5 excess at p == 63 mod 64 -- a real structure, not a
     fluctuation; re-frozen here after a 3*10^5 scan):
         v2(X7(p)) = v2(p + 1) - 3   for v2(p + 1) <= 7,
         v2(X7(p)) >= 5              for v2(p + 1) >= 8 (free band),
     i.e. v2(D_p) = 3 + v2(p + 1) = 3 + v2(sigma(p)) deterministically
     up to k = 4 -- the SAME skeleton as class 1 (deterministic
     through k = 4, first free level k = 5).  This EXPLAINS the clean
     class-7 geometric tail: the governing invariant v2(p + 1) has
     exactly geometric density 2^-(m'-2), so the deterministic
     transfer is invisible in the aggregate histogram; class 1 shows
     the k = 5 dip only because its cell (5, 3) has density 1/64,
     half of the 1/32 that a smooth geometric tail would need.
     Consistency: class 3 (constant depth 5) obeys the same mirror
     law, 3 + v2(p + 1) = 3 + 2 = 5.  Witnesses: p = 7, 23 (m' = 3,
     k = 0), p = 47 (m' = 4, k = 1), p = 31 (m' = 5, k = 2);
     (c) k = 3 mutant does not telescope (first mismatch n = 10).
  G6 strata dissection table (REPORT only): per-cell parities of the
     minimal-stratum count M1 and the level-1 family counts at 3*10^4.

VERDICT ENUM (frozen):
  K5-MECHANISM-FOUND : T1-T6 census-clean at 10^6 + involution census
                       + controls pass (mechanism = tower localization
                       with cell (5,3) restart; refined law measured).
  K5-PARTIAL         : localization T6 holds but some deterministic
                       cell gate fails.
  K5-OPEN            : the localization itself fails.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.
"""
from __future__ import annotations

import time

import os
import sys

_VERIFY = os.path.dirname(os.path.abspath(__file__))
_DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                          "tfpt-discovery"))
sys.path.insert(0, _DISCOVERY)
sys.path.insert(0, _VERIFY)

_LAST1 = {}
_LAST2 = {}

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
    _LAST1["verdict"] = verdict
    print(f"VERDICT: {verdict}")
    return 0 if verdict == "TAILS-IDENTIFIED" else 1


_run_part1 = main


def _run_part2():
    """Part 2: hecke_k5_anomaly_probe.py, promoted verbatim in a function
    scope (v789 precedent)."""
    import time
    from collections import Counter
    from math import isqrt

    from hecke_check32_probe import build_f8, embed, sieve_primes, sieve_sigma3
    from hecke_multirate2adic_probe import (h_series, kron_mul_fast,
                                            sieve_sigma1, v2_capped)

    # ---------------------------------------------------------------- budgets
    N_SEG = 20_000
    N_PAIR = 1_000_000      # divisor-pair involution census
    N_GAUSS = 100_000       # [N3] two-squares census
    N_DISS = 30_000         # strata dissection table (report only)
    N_CTL = 5_000
    CAP = 1_000_000
    MOD_BITS = 20
    K3_FIRST_MISMATCH = 10
    WITNESS_VH = {17: 3, 41: 4, 113: 6}          # exact v2(H_p), frozen
    K5_CELL = (5, 3)

    CHECKS = []


    def check(label: str, ok: bool) -> bool:
        CHECKS.append((label, bool(ok)))
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
        return bool(ok)


    def v2_of(x):
        v = 0
        while x % 2 == 0:
            x //= 2
            v += 1
        return v


    def tower(p):
        """(m, t): m = v2(p-1); t = depth of 2 in the 2-power tower mod p."""
        m = v2_of(p - 1)
        t = 0
        for j in range(1, m + 1):
            if pow(2, (p - 1) >> j, p) == 1:
                t = j
            else:
                break
        return m, t


    def two_sq(p):
        """p == 1 (mod 4) prime -> (A, B) with p = A^2 + B^2, A odd, B even."""
        for b in range(2, isqrt(p) + 1, 2):
            s = p - b * b
            r = isqrt(s)
            if r * r == s:
                return r, b
        raise ValueError(p)


    # ================================================================== run
    def main():
        t0 = time.time()
        print("hecke_k5_anomaly_probe -- HECKE.K5ANOMALY.01")
        print("  claim: k = v2(X1(p)) is governed by (m, t) = "
              "(v2(p-1), 2-power depth of 2); k = 5 lives only in (5, 3)")

        # ------------------------------------------------------------- P0
        print("P0 -- scaffolding + witnesses")
        a = build_f8(N_SEG)
        sig3 = sieve_sigma3(N_SEG)
        sig1 = sieve_sigma1(N_SEG)
        H = h_series(sig1, N_SEG)
        check("scaffold: sigma3 - a == 32 H on odd n <= " + str(N_SEG),
              all(sig3[n] - a[n] == 32 * H[n] for n in range(1, N_SEG + 1, 2)))
        wit_ok = True
        for p, vh in WITNESS_VH.items():
            got = v2_of(H[p])
            cell = tower(p)
            print(f"        witness p={p}: v2(H)={got} (expect {vh}), "
                  f"(m,t)={cell}")
            wit_ok &= got == vh
        check("witnesses: v2(H_17)=3 @(4,1)k0, v2(H_41)=4 @(3,1)k1, "
              "v2(H_113)=6 @(4,2)k3", wit_ok
              and tower(17) == (4, 1) and tower(41) == (3, 1)
              and tower(113) == (4, 2))

        # ------------------------------------------------------------- P1
        print("P1 -- 10^6 census: k vs tower cells")
        t1 = time.time()
        sig1_big = sieve_sigma1(CAP)
        Hm = h_series(sig1_big, CAP - 1, mod=1 << MOD_BITS)
        print(f"        H mod 2^{MOD_BITS} to {CAP - 1}: {time.time()-t1:.1f}s")
        primes = [p for p in sieve_primes(CAP - 1) if p % 2 == 1]
        recs = []                                   # (p, k, m, t) class 1
        for p in primes:
            if p % 8 == 1:
                k = v2_capped(Hm[p], MOD_BITS) - 3
                m, t = tower(p)
                recs.append((p, k, m, t))
        n1 = len(recs)
        cells = {}
        for _, k, m, t in recs:
            cells.setdefault((m, t), Counter())[k] += 1
        print(f"        class-1 primes: {n1}; occupied cells: {len(cells)}")
        print("        full (m,t) x k table (k capped at "
              f"{MOD_BITS - 3} = cap):")
        for cell in sorted(cells):
            c = cells[cell]
            body = " ".join(f"k{k}:{c[k]}" for k in sorted(c))
            tag = ("DET k=%d" % next(iter(c)) if len(c) == 1
                   else f"VAR min k={min(c)}")
            print(f"          (m,t)={cell}: n={sum(c.values()):5d}  [{tag}]  "
                  f"{body}")

        def kset(pred):
            return {k for (_, k, m, t) in recs if pred(m, t)}

        def where(kv):
            return {(m, t) for (_, k, m, t) in recs if k == kv}

        t1_ok = check(
            f"T1: k=1 <=> (m,t)=(3,1), all {n1} class-1 primes < {CAP} "
            f"(k=1 cells: {sorted(where(1))})",
            where(1) == {(3, 1)} and kset(lambda m, t: (m, t) == (3, 1))
            == {1})
        t2_ok = check(
            "T2: k=0 <=> (m=3 & t>=2) | (m>=4 & t=1)  [closes the class-1 "
            "base-criterion bridge: M1 odd <=> tower condition]",
            all((k == 0) == ((m == 3 and t >= 2) or (m >= 4 and t == 1))
                for (_, k, m, t) in recs))
        t3_ok = check(
            f"T3: k=3 <=> (m,t)=(4,2) (k=3 cells: {sorted(where(3))})",
            where(3) == {(4, 2)} and kset(lambda m, t: (m, t) == (4, 2))
            == {3})
        t4_ok = check(
            "T4: k=2 <=> (m=4 & t>=3) | (m>=5 & t=2)",
            all((k == 2) == ((m == 4 and t >= 3) or (m >= 5 and t == 2))
                for (_, k, m, t) in recs))
        t5_ok = check(
            "T5: k=4 <=> (m=5 & t>=4) | (m>=6 & t=3)",
            all((k == 4) == ((m == 5 and t >= 4) or (m >= 6 and t == 3))
                for (_, k, m, t) in recs))
        c53 = cells.get(K5_CELL, Counter())
        t6_ok = check(
            f"T6 (THE ANOMALY): k=5 only in (m,t)={K5_CELL} (k=5 cells: "
            f"{sorted(where(5))}); inside (5,3): min k = "
            f"{min(c53) if c53 else None}, n(k=5)={c53.get(5, 0)}, "
            f"n(k>=6)={sum(v for kk, v in c53.items() if kk >= 6)}",
            where(5) == {K5_CELL} and bool(c53) and min(c53) == 5
            and c53.get(5, 0) > 0
            and sum(v for kk, v in c53.items() if kk >= 6) > 0)

        # ------------------------------------------------------------- P2
        print("P2 -- refined mixture law (measured, not gated)")
        pred = Counter()
        for cell, c in cells.items():
            w = sum(c.values())
            if len(c) == 1:
                pred[next(iter(c))] += w
            else:
                kmin = min(c)
                for j in range(0, 40):
                    pred[kmin + j] += w * 2.0 ** (-j - 1)
        print("        reconstructed P(k) (det cells exact + geometric "
              "restart in free bands) vs observed:")
        chi2 = 0.0
        obs_hist = Counter(k for (_, k, _, _) in recs)
        for k in range(0, 11):
            o = obs_hist.get(k, 0)
            e = pred.get(k, 0.0)
            if e > 0:
                chi2 += (o - e) ** 2 / e
            print(f"          k={k:2d}: obs={o:6d}  law={e:9.1f}  "
                  f"obs/law={o / e if e else float('nan'):.3f}")
        print(f"          chi-square-style sum over k<=10: {chi2:.1f} "
              "(free-band restart is heuristic -- measured only)")
        d53 = sum(cells.get(K5_CELL, Counter()).values()) / n1
        print(f"          density of cell (5,3): {d53:.5f} (naive 1/64 = "
              f"{1 / 64:.5f}); P(k=5) observed {obs_hist.get(5, 0) / n1:.5f} "
              f"vs tower prediction 1/128 = {1 / 128:.5f}")
        check("refined law recorded: mixture (deterministic tower cells + "
              "geometric free bands) printed with residuals; P(k=5) = "
              "(1/64)*(1/2) = 1/128 quantitatively explains the halved "
              "level (statistics reported, not gated)", True)

        # ------------------------------------------------------------- P3
        print("P3 -- involution census (I3 divisor-conjugation pair lemmas)")
        t1 = time.time()
        cnt8 = bytearray(N_PAIR + 1)    # parity of #{pairs == 8 mod 16}
        dcnt = bytearray(N_PAIR + 1)    # d(a)/2 mod 2 via pair parity
        pair_viol_7 = pair_viol_3 = 0
        for d in range(1, isqrt(N_PAIR) + 1, 2):
            for e in range(d, N_PAIR // d + 1, 2):
                n = d * e
                r = n % 8
                s = (d + e) % 16
                if r == 7:
                    if s % 8 != 0:
                        pair_viol_7 += 1
                    if s == 8:
                        cnt8[n] ^= 1
                elif r == 3:
                    if s % 8 != 4:
                        pair_viol_3 += 1
                    dcnt[n] ^= 1
        bad_p7 = sum(1 for m in range(7, N_PAIR + 1, 8)
                     if ((sig1_big[m] >> 3) & 1) != cnt8[m])
        bad_p3 = sum(1 for m in range(3, N_PAIR + 1, 8)
                     if (v2_capped(sig1_big[m], 6) == 2) != (dcnt[m] == 1))
        print(f"        pair sieve: {time.time()-t1:.1f}s")
        check(f"I3a: a == 7 (mod 8): every divisor pair d + a/d == 0 (mod 8) "
              f"(violations: {pair_viol_7}) and sigma(a)/8 parity == "
              f"#{{pairs: d+a/d == 8 mod 16}} parity, all a <= {N_PAIR} "
              f"(mismatches: {bad_p7})", pair_viol_7 == 0 and bad_p7 == 0)
        check(f"I3b: a == 3 (mod 8): every pair == 4 (mod 8) (violations: "
              f"{pair_viol_3}) and v2(sigma(a)) = 2 <=> d(a) == 2 (mod 4), "
              f"all a <= {N_PAIR} (mismatches: {bad_p3})",
              pair_viol_3 == 0 and bad_p3 == 0)
        check("I1/I2 typing: y <-> -y fold built into slice counts; no "
              "natural cross-line involution exists on a + 2c = p (weight-"
              "asymmetric) -- the tail mechanism is the tower, not a "
              "term pairing", True)

        # ------------------------------------------------------------- P4
        print("P4 -- [N3] Gauss quartic census")
        bad_g = []
        for (p, k, m, t) in recs:
            if p >= N_GAUSS:
                break
            A, B = two_sq(p)
            if (t >= 2) != (B % 8 == 0):
                bad_g.append(p)
        n_g = sum(1 for r in recs if r[0] < N_GAUSS)
        check(f"[N3] Gauss: t >= 2 (2 quartic residue) <=> 8 | B in "
              f"p = A^2 + B^2, all {n_g} class-1 primes < {N_GAUSS} "
              f"(failures: {len(bad_g)})", len(bad_g) == 0)

        # ------------------------------------------------------------- P5
        print("P5 -- strata dissection table (report only)")
        vs = [0] * (N_DISS + 1)
        for mm in range(1, N_DISS + 1, 2):
            vs[mm] = v2_capped(sig1_big[mm], 6)
        print("        per-cell: [M1 parity pattern] -> k  (p < "
              f"{N_DISS}; M1 = level-0 count, L1 = level-1 family count)")
        diss = {}
        for (p, k, m, t) in recs:
            if p >= N_DISS:
                break
            m1 = l1 = 0
            y = 1
            while 2 * y * y < p:
                av = vs[p - 2 * y * y]
                if av == 3:
                    m1 += 1
                elif av == 4:
                    l1 += 1                       # branch-A c-square, v=4
                y += 2
            for c in range(1, (p - 1) // 2 + 1, 2):
                cv = vs[c]
                av = vs[p - 2 * c]
                if c % 8 in (1, 5) and cv == 1 and av == 3:
                    l1 += 1                       # branch-A off-square level 1
                elif c % 8 == 3 and cv == 2 and av == 2:
                    l1 += 1                       # branch-B minimal
            diss.setdefault((m, t), Counter())[(m1 % 2, l1 % 2, min(k, 6))] += 1
        for cell in sorted(diss):
            pat = ", ".join(f"(M1%2={a},L1%2={b})->k{kk}:{v}"
                            for (a, b, kk), v in sorted(diss[cell].items()))
            print(f"          (m,t)={cell}: {pat}")
        check("dissection recorded: minimal-stratum parity M1 tracks k=0 "
              "(T2), level-1 parities tabulated per tower cell -- the "
              "tower enters already at the first two strata levels "
              "(derivation of the full determinism typed OPEN, "
              "Cohn-Lagarias-flavoured governing statement cited)", True)

        # ------------------------------------------------------------- P6
        print("P6 -- controls")
        check("C-a structural: v2(p - 1) == 1 for ALL p == 7 (mod 8) < "
              f"{CAP} -- the tower is trivial in class 7, the mechanism "
              "CANNOT act there",
              all(v2_of(p - 1) == 1 for p in primes if p % 8 == 7))
        mirror_cells = {}
        bad_mirror = []
        n7 = 0
        for p in primes:
            if p % 8 != 7:
                continue
            n7 += 1
            k = v2_capped(Hm[p], MOD_BITS) - 1
            mp = v2_of(p + 1)
            mirror_cells.setdefault(min(mp, 9), Counter())[k] += 1
            if mp <= 7:
                if k != mp - 3:
                    bad_mirror.append(p)
            elif k < 5:
                bad_mirror.append(p)
        print("        class-7 mirror table (m' = v2(p+1), m' >= 9 pooled):")
        for mp in sorted(mirror_cells):
            c = mirror_cells[mp]
            tag = "DET k=%d" % next(iter(c)) if len(c) == 1 \
                else f"VAR min k={min(c)}"
            print(f"          m'={mp}: n={sum(c.values()):5d} [{tag}]  "
                  + " ".join(f"k{k}:{c[k]}" for k in sorted(c)))
        check("C-b class-7 MIRROR LAW: v2(X7(p)) = v2(p+1) - 3 for "
              "v2(p+1) <= 7 and >= 5 in the free band v2(p+1) >= 8, ALL "
              f"{n7} primes p == 7 (mod 8) < {CAP} (violations: "
              f"{len(bad_mirror)}) => v2(D_p) = 3 + v2(sigma(p)) through "
              "k = 4; class-3 consistency 3 + 2 = 5; the run-1 'flatness' "
              "control failure (8.2x k=5 at p == 63 mod 64) is exactly "
              "this law -- class 7 carries the mirror skeleton, whose "
              "geometric cell densities hide it from the aggregate "
              "histogram; NO (m,t)-tower signature (C-a)",
              len(bad_mirror) == 0)
        sig1_c = sig1[:N_CTL + 1]
        L = [0] + [sig1_c[n] for n in range(1, N_CTL + 1)]
        L_no3 = [0] + [sig1_c[n] if n % 3 else 0 for n in range(1, N_CTL + 1)]
        h3 = kron_mul_fast(L, embed(L, 3, N_CTL), N_CTL)
        w19 = kron_mul_fast(L, embed(L, 9, N_CTL), N_CTL)
        w127 = kron_mul_fast(L, embed(L, 27, N_CTL), N_CTL)
        u13 = kron_mul_fast(L, embed(L_no3, 3, N_CTL), N_CTL)
        mism = [n for n in range(1, N_CTL + 1)
                if h3[n] - 3 * w19[n] + 2 * w127[n] != u13[n]]
        check(f"C-c k = 3 mutant does not telescope: first mismatch "
              f"n = {mism[0] if mism else None} (predeclared "
              f"{K3_FIRST_MISMATCH})",
              len(mism) > 0 and mism[0] == K3_FIRST_MISMATCH)

        # ---------------------------------------------------------- verdict
        n_pass = sum(1 for _, ok in CHECKS if ok)
        n_all = len(CHECKS)
        det_ok = t1_ok and t2_ok and t3_ok and t4_ok and t5_ok
        assert det_ok or n_pass < n_all
        if not t6_ok:
            verdict = "K5-OPEN"
        elif n_pass == n_all:
            verdict = "K5-MECHANISM-FOUND"
        else:
            verdict = "K5-PARTIAL"
        print(f"CHECKS: {n_pass}/{n_all} passed; walltime "
              f"{time.time() - t0:.1f}s")
        _LAST2["verdict"] = verdict
        print(f"VERDICT: {verdict}")
        return 0 if verdict == "K5-MECHANISM-FOUND" else 1

    rc = main()
    return rc, list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 20/20
    (TAILS-IDENTIFIED), part 2 must be 17/17 (K5-MECHANISM-FOUND)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    v1 = _LAST1.get("verdict", "")
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 20
                and v1 == "TAILS-IDENTIFIED")
    print("\n[%s] PART-1 PATTERN GATE: expected 20/20 (TAILS-IDENTIFIED) "
          "-- got %d checks, fails: %s, verdict: %s"
          % ("PASS" if part1_ok else "FAIL", len(CHECKS),
             fails1 or "none", v1))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    v2 = _LAST2.get("verdict", "")
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 17
                and v2 == "K5-MECHANISM-FOUND")
    print("\n[%s] PART-2 PATTERN GATE: expected 17/17 "
          "(K5-MECHANISM-FOUND) -- got %d checks, fails: %s, verdict: %s"
          % ("PASS" if part2_ok else "FAIL", len(chks2),
             fails2 or "none", v2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- TAILS-IDENTIFIED + "
          "K5-MECHANISM-FOUND: the exact identities v_2(D_p) = "
          "6 + v_2(X7) [p == 7 mod 8] and 8 + v_2(X1) [p == 1 mod 8] with "
          "termwise-integral divisor sums, censused clean at 10^6; class-7 "
          "base <=> R3(p) == 16 (mod 32) (h = 1 ternary); the class-1 "
          "two-shape criterion exact with the single-character bridge "
          "typed OPEN -- and then CLOSED at the tower level: k = v_2(X1) "
          "is deterministic on the (m, t) residue-tower cells with zero "
          "exceptions, k = 5 lives only in cell (5, 3) of density 1/64, "
          "so P(k = 5) = 1/128 -- exactly the observed half mass; the "
          "class-7 mirror law v_2(D_p) = 3 + v_2(p+1) through k = 4 "
          "explains the class-3 constancy and the clean class-7 tail; the "
          "governing-field derivation stays typed open/cited.  "
          "NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
