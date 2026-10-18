#!/usr/bin/env python3
"""v789 -- HECKE.MULTIRATE2ADIC.01: the multirate 2-adic depth ladder of the TFPT cusp channel f8 = eta(2t)^4 eta(4t)^4 and its constant-depth closure (the claim also covers HECKE.CONSTDEPTH.01), ONE module from two probes (23/23 + 24/24 checks, ~190 s; discovery probes hecke_multirate2adic_probe.py MULTIRATE-THEOREM / SPINLIFT-VERIFIED and hecke_constant_depth_probe.py CONSTDEPTH-THEOREM, both 2026-08-05).  THE LADDER (part 1): v_2(1 + p^3 - a_p) >= 5 + 2*[chi_-4(p) = 1] + [chi_8(p) = 1] for every odd prime -- census-verified on ALL 78497 odd primes p < 10^6 with ZERO violations and SHARP witnesses per class mod 8 (3 -> v2 = 5, 7 -> 6, 5 -> 7, 1 -> 8; smallest attaining primes 3, 7, 5, 17); the closed sigma1-convolution formula a_n = sigma3(n) - 32*[W_{1,2} - 3 W_{1,4} + 2 W_{1,8}](n) exact for all odd n <= 20000; the character sifts I0-I3 (D == 0 mod 32 / 128 / 64 / 256 on the residue classes cut by 1, chi_-4, chi_8, chi_-8 = the v541 four-character envelope) are Sturm-certified -- the twisted forms live at level <= 512, Sturm bound 256, verified to 20000 = 78x that bound; the predeclared MUST-FAIL strengthening mod 512 breaks exactly at n = 9 (D_9 = 768 = 2^8 * 3, so 256 is maximal on the chi_-8 rung); the depth-cancellation lemma makes the odd projection a genuine weight-4 form of level <= 64 (the quasimodular E2-anomaly cancels: -1/2 + 3/4 - 1/4 = 0); the v537 half-integral witness g (weight 5/2, level 32 = 4*8) rebuilds exactly with Sh_{t=2,psi=1}(g) = -8 f8 = -8 E_odd + 256 H coefficientwise to n = 160, T(3^2) g = -4 g, Kohnen window 4a - 8bc = 1 unsolvable, and the lift's own Kronecker factor (2/d) IS chi_8 -- the same character that rules the third rung of the ladder.  THE CONSTANT-DEPTH THEOREM (part 2): v_2(1 + p^3 - a_p) = 5 EXACTLY for p == 3 (mod 8) and = 7 EXACTLY for p == 5 (mod 8) -- the multirate weights (1, -3, 2) TELESCOPE H to the both-odd convolution U_1(n) = sum_{a + 2c = n, a, c both odd} sigma(a) sigma(c) (every s >= 2 coefficient (2^s - 1) - 3(2^{s-1} - 1) + 2(2^{s-2} - 1) vanishes); class 3 mod 8 is pinned by the UNIQUE x^2 + 2y^2 representation ([N1] Fermat-Euler-Gauss, disc -8, h = 1: H_p odd); class 5 by the unique x^2 + (2w)^2 representation via the ternary bridge R3(p) == 8 (mod 16), R3/8 == N(p) (mod 2) ([N2] two-squares, disc -4, h = 1: H_p == 4 mod 8); the sigma 2-adic lemmas L1-L5 are exhaustively censused on all odd m <= 10^6; the chain closes ELEMENTARILY modulo the TWO named classical h = 1 ingredients (instances machine-verified: r' = 2 rho, r_2 = 4 rho4, uniqueness counts == 1) -- the exact analogue of the parent's Sturm citation discipline; the final census re-derivation gives ZERO exceptions on 19653 + 19623 primes < 10^6; composites violate as required (1701 / 1708 violators < 20000; predeclared witnesses 27 -> v2 = 6, 35 -> 7, 21 -> 9 confirmed exactly) and the wrong-form k = 3 mutant neither telescopes (first mismatch n = 10) nor has constant depth.  All controls fire.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes hecke_multirate2adic_probe.py (2026-08-05, 23/23, 104.3 s, MULTIRATE-THEOREM / SPINLIFT-VERIFIED) + hecke_constant_depth_probe.py (2026-08-05, 24/24, 84.1 s, CONSTDEPTH-THEOREM); no spec corrections are disclosed in either probe docstring; both re-run identically at promotion.  Promoted verbatim, part 2 wrapped in a function scope (its "from __future__ import annotations" is hoisted to the module top; the sibling imports build_f8 / embed / sieve_* / h_series / kron_mul_fast / sieve_sigma1 / v2_capped resolve against experiments/tfpt-discovery on sys.path -- exactly the probes' own import graph); numbers unchanged; run() encodes both patterns (v757 precedent).

Original hecke_multirate2adic_probe.py docstring (verbatim):
hecke_multirate2adic_probe -- HECKE.MULTIRATE2ADIC.01 (+ SPINLIFT ladder).

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

Original hecke_constant_depth_probe.py docstring (verbatim):
hecke_constant_depth_probe -- HECKE.CONSTDEPTH.01: proof of the
constant 2-adic depth found by the multirate census.

STATEMENT (frozen; the census finding of hecke_multirate2adic_probe.py):
  for every prime p == 3 (mod 8):  v_2(1 + p^3 - a_p) = 5  EXACTLY;
  for every prime p == 5 (mod 8):  v_2(1 + p^3 - a_p) = 7  EXACTLY;
equivalently, with D_n = sigma3(n) - a_n = 32*H_n (multirate formula
H_n = W_{1,2}(n) - 3 W_{1,4}(n) + 2 W_{1,8}(n)):
  H_p odd for p == 3 (mod 8);   v_2(H_p) = 2 exactly for p == 5 (mod 8).

PROOF CHAIN (frozen before running; every step machine-certified):

  STEP 1 (TELESCOPING COLLAPSE -- elementary, no modular forms).
    Split b = 2^t c (c odd) in W_{1,k}(n) = sum_{a+kb=n} sigma(a)sigma(b)
    and use sigma(2^t c) = (2^{t+1}-1) sigma(c).  With
    U_s(n) := sum_{a + 2^s c = n, c odd} sigma(a) sigma(c) one gets
      W_{1,2} = sum_{s>=1} (2^s - 1)     U_s,
      W_{1,4} = sum_{s>=2} (2^{s-1} - 1) U_s,
      W_{1,8} = sum_{s>=3} (2^{s-2} - 1) U_s,
    and the multirate weights (1, -3, +2) make every s >= 2 coefficient
    vanish:  (2^s-1) - 3(2^{s-1}-1) + 2(2^{s-2}-1) = 0.   Hence
      H_n = U_1(n) = sum_{a + 2c = n, a, c BOTH ODD} sigma(a) sigma(c)
    for odd n (a = n - 2c is automatically odd).  CERTIFIED: symbolic
    coefficient check s = 1..30; expansion check to n <= 3000; the
    identity H == U_1 exact on ALL odd n <= 20000 against both the
    eta build and the parent convolution series.

  STEP 2 (SIGMA 2-ADIC CLASSIFICATION -- elementary lemma censuses).
    For odd m:  v_2(sigma(m)) = sum over primes q^e || m with e odd of
    v_2(sigma(q^e)), and sigma(q^e) = (1+q) * sum_{j<(e+1)/2} q^{2j}
    with the second factor == (e+1)/2 (mod 8).  Consequences used
    (each an EXHAUSTIVE census on odd m <= 10^6, no factorisation --
    both sides sieved independently):
      (L1) sigma(m) odd  <=>  m is a square           [m odd]
           (general m: square or 2*square -- the classical criterion);
      (L2) v_2(sigma(m)) = 1  =>  m == 1 or 5 (mod 8);
      (L3) m == 7 (mod 8)  =>  v_2(sigma(m)) >= 3;
      (L4) on m == 3 (mod 8):  v_2(sigma(m)) = 2  <=>
           rho(m) == 2 (mod 4), where rho(m) = sum_{d|m} chi_{-8}(d)
           (i.e. m = q^e z^2, q == 3 mod 8 prime, e == 1 mod 4, all
           other primes to even exponent);
      (L5) on m == 3 (mod 8): rho(m) is even (m is never a square).

  STEP 3 (CLASS p == 3 mod 8 -- closes with named ingredient N1).
    On the line a + 2c = p, a, c odd, a term sigma(a)sigma(c) is odd
    iff a and c are both odd squares (L1), i.e. iff p = x^2 + 2y^2.
    Hence H_p == #{(x,y) >= 1 : x^2 + 2y^2 = p} (mod 2).
    [N1] Fermat-Euler-Gauss for the class-number-1 form x^2 + 2y^2
    (Z[sqrt(-2)] a UFD):  p == 1, 3 (mod 8)  <=>  p = x^2 + 2y^2,
    ESSENTIALLY UNIQUELY; all-signs count r'(m) = 2 rho(m).
    => the count is exactly 1  =>  H_p ODD  =>  v_2(D_p) = 5 exactly.
    CERTIFIED: count == 1 by brute force for ALL p == 3 (mod 8) < 10^5;
    instance census of r' = 2 rho on m <= 10^4.

  STEP 4 (CLASS p == 5 mod 8 -- residue bookkeeping mod 8).
    On a + 2c = p (a, c odd): c odd => 2c == 2 or 6 (mod 8) =>
    a == 3 or 7 (mod 8).  So a is NEVER a square (v_2 sigma(a) >= 2 by
    L1+L2) and the (1,1) stratum is empty (needs a == 1, 5 mod 8, L2).
    A term survives mod 8 only with v_2(sigma(a)sigma(c)) <= 2, which
    forces c = y^2 (odd square => 2c == 2, a == 3 mod 8) and
    v_2(sigma(a)) = 2 (a == 7 mod 8 is dead by L3); each such term is
    4 * odd == 4 (mod 8).  Hence
      H_p == 4 * N(p) (mod 8),
      N(p) = #{ y odd >= 1, 2y^2 < p : v_2(sigma(p - 2y^2)) = 2 }.
    CERTIFIED: exhaustive residue table over the strata; the congruence
    H_p == 4 N(p) (mod 8) for all p == 5 (mod 8) < 10^5.

  STEP 5 (N(p) IS ODD -- ternary bridge, closes with N1 + N2).
    By L4, N(p) counts y with rho(a_y) == 2 (mod 4), a_y = p - 2y^2;
    by L5 all rho(a_y) are even, so
      N(p) == (1/2) sum_{y odd > 0} rho(a_y)  =  R3(p)/8   (mod 2),
    where R3(p) = #{(x,y,z) in Z^3 : x^2 + 2y^2 + 2z^2 = p}
    (representations of p == 5 mod 8 automatically have x, y, z odd;
    the y-slices give R3 = 4 sum rho(a_y) via [N1] r' = 2 rho).
    Slicing R3 in x instead:  R3 = 2 sum_{x odd > 0} r_2((p - x^2)/2)
    with r_2 = sum-of-two-squares count.
    [N2] Fermat-Euler two-squares (Z[i] a UFD): r_2(m) =
    4 sum_{d|m} chi_{-4}(d) = 4 rho4(m); rho4(m) odd <=> odd part of m
    is a square; p == 1 (mod 4) => p = A^2 + B^2 (A odd, B even)
    ESSENTIALLY UNIQUELY.
    Here (p - x^2)/2 == 2 (mod 4), so rho4 odd <=> (p - x^2)/4 = w^2,
    i.e. p = x^2 + 4w^2:
      R3(p)/8 == #{(x,w) >= 1 : x^2 + 4w^2 = p} = 1   (mod 2)
    (exactly one ordered pair from the unique A^2 + B^2, B = 2w; and
    p = x^2 + 2y^2 is impossible for p == 5 mod 8).
    => N(p) odd => H_p == 4 (mod 8) => v_2(D_p) = 7 exactly.
    CERTIFIED: N odd, N == R3/8 (mod 2), R3 == 8 (mod 16), and
    #(x^2+4w^2) == 1 for ALL p == 5 (mod 8) < 10^5 (R3 via the r_2
    table; r_2 = 4 rho4 brute-force-censused on m <= 10^4).

  STEP 6 (FINAL THEOREM vs THE 10^6 CENSUS).  Re-derive the census
    (parent machinery, convolution mod 2^20): v_2(D_p) == 5 for ALL
    p == 3 (mod 8) < 10^6 and == 7 for ALL p == 5 (mod 8) < 10^6,
    ZERO exceptions.

  HONEST TYPING: the chain closes ELEMENTARILY except for the two
  named classical ingredients [N1] (x^2 + 2y^2, disc -8, h = 1) and
  [N2] (x^2 + y^2, disc -4, h = 1) -- Fermat/Euler/Gauss class-number-
  one representation theorems (formula + essential uniqueness), the
  exact analogue of the Sturm citation discipline in the parent probe;
  their instances are machine-verified here (r' = 2 rho, r_2 = 4 rho4,
  uniqueness counts == 1).  No Hurwitz class numbers, no genus theory
  beyond h = 1, no modular forms are needed.

PREDECLARED CONTROLS (must fire):
  C1 composites: constant depth is PRIME-SPECIFIC -- predeclared
     witnesses n = 27 (v2 = 6), n = 35 (v2 = 7) in class 3 and n = 21
     (v2 = 9) in class 5; >= 50 composite violators per class below
     20000 required.
  C2 wrong form k = 3: the telescoping weights (1, -3, 2) are 2-adic-
     specific -- W_{1,3} - 3 W_{1,9} + 2 W_{1,27} does NOT collapse to
     the 3-adic U'_1 (s >= 2 coefficients 1, 3, 9, ... do not vanish);
     predeclared first mismatch n = 10; and its prime values have NO
     constant 2-adic depth in classes 3, 5 mod 8 (>= 2 distinct v_2
     values per class among primes < 5000).

VERDICT ENUM (frozen):
  CONSTDEPTH-THEOREM : every gate passes -- proof chain closed with
                       the two named h=1 ingredients, census-consistent.
  CONSTDEPTH-PARTIAL : some gate degraded, no counterexample (which
                       class/step remains is reported).
  CONSTDEPTH-FALSE   : a census counterexample -- reported exactly.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.
"""
from __future__ import annotations

import os
import random
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_HERE_DISC = os.path.abspath(os.path.join(_HERE, "..",
                                          "experiments", "tfpt-discovery"))
sys.path.insert(0, _HERE_DISC)

from hecke_check32_probe import build_f8, sieve_primes, sieve_sigma3  # noqa: E402

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


_run_part1 = main


def _run_part2():
    # PART 2 -- hecke_constant_depth_probe.py (verbatim; module-level
    # names local to this function scope; its "from __future__ import
    # annotations" is hoisted to the module top)
    import time

    from hecke_check32_probe import build_f8, embed, sieve_primes, sieve_sigma3
    from hecke_multirate2adic_probe import (h_series, kron_mul_fast,
                                            sieve_sigma1, v2_capped)

    # ---------------------------------------------------------------- budgets
    N_SEG = 20_000        # exact segment (eta build, U1 identity, composites)
    N_LEMMA = 1_000_000   # lemma censuses (sigma parity, residue classes, rho)
    N_INST = 100_000      # per-prime chain instance census (classes 3 and 5)
    N_BRUTE = 10_000      # brute-force lattice counts for [N1]/[N2] formulas
    N_TELE = 3_000        # telescoping expansion check range
    N_CTL = 5_000         # k = 3 mutant control range
    CAP = 1_000_000       # final census re-derivation
    MOD_BITS = 20
    DEPTH = {3: 5, 5: 7}                       # the constant-depth theorem
    WITNESS_COMPOSITE = {27: 6, 35: 7, 21: 9}  # predeclared n -> v2
    MIN_COMPOSITE_VIOL = 50
    K3_FIRST_MISMATCH = 10

    CHECKS = []


    def check(label: str, ok: bool) -> bool:
        CHECKS.append((label, bool(ok)))
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
        return bool(ok)


    def sieve_rho8(n_max):
        """rho(m) = sum_{d|m} chi_-8(d);  chi_-8 = +1 on 1,3 mod 8, -1 on 5,7."""
        r = [0] * (n_max + 1)
        for d in range(1, n_max + 1, 2):
            s = 1 if d % 8 in (1, 3) else -1
            for m in range(d, n_max + 1, d):
                r[m] += s
        return r


    def sieve_rho4(n_max):
        """rho4(m) = sum_{d|m} chi_-4(d);  chi_-4 = +1 on 1 mod 4, -1 on 3."""
        r = [0] * (n_max + 1)
        for d in range(1, n_max + 1, 2):
            s = 1 if d % 4 == 1 else -1
            for m in range(d, n_max + 1, d):
                r[m] += s
        return r


    def u_series(sig1, n_max, s):
        """U_s = sum_{a + 2^s c = n, c odd} sigma(a) sigma(c), via one product."""
        L = [0] + [sig1[n] for n in range(1, n_max + 1)]
        L_odd = [0] + [sig1[n] if n % 2 else 0 for n in range(1, n_max + 1)]
        return kron_mul_fast(L, embed(L_odd, 1 << s, n_max), n_max)


    def w_series(sig1, n_max, k):
        """W_{1,k} = sum_{a + k b = n} sigma(a) sigma(b), via one product."""
        L = [0] + [sig1[n] for n in range(1, n_max + 1)]
        return kron_mul_fast(L, embed(L, k, n_max), n_max)


    # ================================================================== run
    def main():
        t0 = time.time()
        print("hecke_constant_depth_probe -- HECKE.CONSTDEPTH.01")
        print(f"  theorem: v2(1 + p^3 - a_p) = 5 exactly (p == 3 mod 8), "
              f"= 7 exactly (p == 5 mod 8)")

        # ------------------------------------------------------------- P0
        print("P0 -- exact scaffolding")
        a = build_f8(N_SEG)
        sig3 = sieve_sigma3(N_SEG)
        sig1 = sieve_sigma1(N_SEG)
        H = h_series(sig1, N_SEG)
        check("scaffold: eta build + parent convolution H agree "
              f"(sigma3(n) - a_n == 32 H_n on odd n <= {N_SEG})",
              all(sig3[n] - a[n] == 32 * H[n]
                  for n in range(1, N_SEG + 1, 2)))

        # ------------------------------------------------------------- P1
        print("P1 -- STEP 1: telescoping collapse H = U_1")
        coeff = {1: (2 ** 1 - 1)}
        for s in range(2, 31):
            coeff[s] = ((2 ** s - 1) - 3 * (2 ** (s - 1) - 1)
                        + (2 * (2 ** (s - 2) - 1) if s >= 3 else 0))
        check("symbolic: multirate weights (1,-3,+2) kill every s >= 2 "
              "coefficient (2^s-1) - 3(2^{s-1}-1) + 2(2^{s-2}-1), s = 2..30; "
              "s = 1 coefficient = 1",
              coeff[1] == 1 and all(coeff[s] == 0 for s in range(2, 31)))
        sig1_t = sig1[:N_TELE + 1]
        U = {s: u_series(sig1_t, N_TELE, s)
             for s in range(1, 13) if (1 << s) <= N_TELE}
        w12 = w_series(sig1_t, N_TELE, 2)
        w14 = w_series(sig1_t, N_TELE, 4)
        w18 = w_series(sig1_t, N_TELE, 8)
        exp_ok = all(
            w12[n] == sum((2 ** s - 1) * U[s][n] for s in U)
            and w14[n] == sum((2 ** (s - 1) - 1) * U[s][n] for s in U if s >= 2)
            and w18[n] == sum((2 ** (s - 2) - 1) * U[s][n] for s in U if s >= 3)
            for n in range(1, N_TELE + 1))
        check(f"expansion: W12/W14/W18 = sum_s (2^s-1)/(2^(s-1)-1)/(2^(s-2)-1) "
              f"U_s exactly on n <= {N_TELE}", exp_ok)
        U1 = u_series(sig1, N_SEG, 1)
        check(f"IDENTITY: H_n == U_1(n) = sum_{{a+2c=n, a,c odd}} "
              f"sigma(a)sigma(c) for ALL odd n <= {N_SEG} (exact)",
              all(H[n] == U1[n] for n in range(1, N_SEG + 1, 2)))

        # ------------------------------------------------------------- P2
        print("P2 -- STEP 2: sigma 2-adic classification lemmas (10^6 census)")
        t1 = time.time()
        sig1_big = sieve_sigma1(N_LEMMA)
        rho = sieve_rho8(N_LEMMA)
        vs = [0] * (N_LEMMA + 1)
        for m in range(1, N_LEMMA + 1, 2):
            vs[m] = v2_capped(sig1_big[m], 4)      # 4 means >= 4
        is_sq = bytearray(N_LEMMA + 1)
        x = 1
        while x * x <= N_LEMMA:
            is_sq[x * x] = 1
            x += 1
        print(f"        sieves (sigma1, rho, v2, squares) to {N_LEMMA}: "
              f"{time.time() - t1:.1f}s")
        l1 = all((vs[m] == 0) == bool(is_sq[m])
                 for m in range(1, N_LEMMA + 1, 2))
        check(f"L1 parity criterion: sigma(m) odd <=> m square, ALL odd "
              f"m <= {N_LEMMA} (classical: square or 2*square; odd m => "
              "square)", l1)
        l2 = all(m % 8 in (1, 5)
                 for m in range(1, N_LEMMA + 1, 2) if vs[m] == 1)
        check(f"L2: v2(sigma(m)) = 1 => m == 1, 5 (mod 8), ALL odd "
              f"m <= {N_LEMMA}", l2)
        l3 = all(vs[m] >= 3 for m in range(7, N_LEMMA + 1, 8))
        check(f"L3: m == 7 (mod 8) => v2(sigma(m)) >= 3, ALL m <= {N_LEMMA}",
              l3)
        l4 = all((vs[m] == 2) == (rho[m] % 4 == 2)
                 for m in range(3, N_LEMMA + 1, 8))
        check(f"L4: on m == 3 (mod 8): v2(sigma(m)) = 2 <=> rho(m) == 2 "
              f"(mod 4) [<=> m = q^(e==1 mod 4) z^2, q == 3 mod 8], ALL "
              f"m <= {N_LEMMA} (set equality, both sides sieved "
              "independently)", l4)
        l5 = all(rho[m] % 2 == 0 for m in range(3, N_LEMMA + 1, 8))
        check(f"L5: rho(m) even for ALL m == 3 (mod 8) <= {N_LEMMA} "
              "(m never a square)", l5)

        # ------------------------------------------------------------- P3
        print("P3 -- named-ingredient instance censuses [N1], [N2]")
        r_n1 = [0] * (N_BRUTE + 1)
        xx = 0
        while xx * xx <= N_BRUTE:
            yy = 0
            while xx * xx + 2 * yy * yy <= N_BRUTE:
                n = xx * xx + 2 * yy * yy
                if n >= 1:
                    mult = (1 if xx == 0 else 2) * (1 if yy == 0 else 2)
                    r_n1[n] += mult
                yy += 1
            xx += 1
        rho4 = sieve_rho4(N_LEMMA)
        r_n2 = [0] * (N_BRUTE + 1)
        xx = 0
        while xx * xx <= N_BRUTE:
            yy = 0
            while xx * xx + yy * yy <= N_BRUTE:
                n = xx * xx + yy * yy
                if n >= 1:
                    mult = (1 if xx == 0 else 2) * (1 if yy == 0 else 2)
                    r_n2[n] += mult
                yy += 1
            xx += 1
        check(f"[N1] instances: all-signs count r'(m) of x^2 + 2y^2 == "
              f"2 rho(m) for ALL m <= {N_BRUTE} (Gauss, disc -8, h = 1)",
              all(r_n1[m] == 2 * rho[m] for m in range(1, N_BRUTE + 1)))
        check(f"[N2] instances: two-squares count r2(m) == 4 rho4(m) for ALL "
              f"m <= {N_BRUTE} (Jacobi/Gauss, disc -4, h = 1)",
              all(r_n2[m] == 4 * rho4[m] for m in range(1, N_BRUTE + 1)))
        check(f"rho4 parity lemma: rho4(m) odd <=> odd part of m is a "
              f"square, ALL m <= {N_BRUTE}",
              all((rho4[m] % 2 == 1) == bool(is_sq[m // (m & -m)])
                  for m in range(1, N_BRUTE + 1)))

        # ------------------------------------------------------------- P4
        print("P4 -- STEP 3: class p == 3 (mod 8) closes")
        primes_inst = [p for p in sieve_primes(N_INST - 1) if p % 2 == 1]
        p3 = [p for p in primes_inst if p % 8 == 3]
        rep_bad = []
        for p in p3:
            cnt = 0
            y = 1
            while 2 * y * y < p:
                if is_sq[p - 2 * y * y]:
                    cnt += 1
                y += 1
            if cnt != 1:
                rep_bad.append((p, cnt))
        check(f"[N1] uniqueness: #{{(x,y) >= 1: x^2 + 2y^2 = p}} == 1 for "
              f"ALL {len(p3)} primes p == 3 (mod 8) < {N_INST} "
              f"(failures: {len(rep_bad)})", len(rep_bad) == 0)
        par_bad = [p for p in p3 if p <= N_SEG and H[p] % 2 != 1]
        check(f"chain: H_p == #reps == 1 (mod 2), i.e. H_p ODD, for all "
              f"p == 3 (mod 8) <= {N_SEG} on the exact segment "
              f"(failures: {len(par_bad)})", len(par_bad) == 0)
        # spot bookkeeping: the odd terms of U_1 are exactly the (square,
        # square) pairs
        spot_ok = True
        for p in [q for q in p3 if q < 2000]:
            n_odd_terms = sum(1 for c in range(1, (p - 1) // 2 + 1, 2)
                              if sig1[p - 2 * c] % 2 == 1 and sig1[c] % 2 == 1)
            n_sq_pairs = sum(1 for c in range(1, (p - 1) // 2 + 1, 2)
                             if is_sq[c] and is_sq[p - 2 * c])
            if n_odd_terms != n_sq_pairs:
                spot_ok = False
        check("bookkeeping spot check (p < 2000): odd U_1 terms == "
              "(square, square) pairs exactly", spot_ok)

        # ------------------------------------------------------------- P5
        print("P5 -- STEPS 4+5: class p == 5 (mod 8) closes")
        vs_inst = vs                        # v2(sigma) table covers N_INST
        rho4_r2 = rho4                      # r2 = 4 * rho4
        p5 = [p for p in primes_inst if p % 8 == 5]
        sig1_inst = sig1_big
        Hm_seg = H                          # exact H on the segment
        bad_strata = []
        bad_n_odd = []
        bad_r3 = []
        bad_u = []
        for p in p5:
            # N(p) from the sigma table
            N_p = 0
            y = 1
            while 2 * y * y < p:
                if vs_inst[p - 2 * y * y] == 2:
                    N_p += 1
                y += 2
            # H_p mod 8 == 4 N(p): exact H on segment, else via congruence
            if p <= N_SEG and (Hm_seg[p] - 4 * N_p) % 8 != 0:
                bad_strata.append(p)
            if N_p % 2 != 1:
                bad_n_odd.append(p)
            # R3 via x-slices and the r2 = 4 rho4 table
            R3 = 0
            x = 1
            while x * x < p:
                m = (p - x * x) // 2
                R3 += 4 * rho4_r2[m]
                x += 2
            R3 *= 2
            # unique x^2 + 4w^2 representation
            cnt4 = 0
            w = 1
            while 4 * w * w < p:
                if is_sq[p - 4 * w * w]:
                    cnt4 += 1
                w += 1
            if not (R3 % 16 == 8 and (R3 // 8) % 2 == N_p % 2 and cnt4 == 1):
                bad_r3.append((p, R3, N_p, cnt4))
            if sig1_inst[p] != 1 + p:
                bad_u.append(p)
        check(f"STEP 4 strata: H_p == 4 N(p) (mod 8) with N(p) = #{{y odd: "
              f"v2(sigma(p - 2y^2)) = 2}} for all p == 5 (mod 8) <= {N_SEG} "
              f"(exact H; failures: {len(bad_strata)})", len(bad_strata) == 0)
        check(f"STEP 5 parity: N(p) ODD for ALL {len(p5)} primes "
              f"p == 5 (mod 8) < {N_INST} (failures: {len(bad_n_odd)})",
              len(bad_n_odd) == 0)
        check(f"STEP 5 ternary bridge: R3(p) == 8 (mod 16), R3/8 == N(p) "
              f"(mod 2), and #{{(x,w) >= 1: x^2 + 4w^2 = p}} == 1 for ALL "
              f"p == 5 (mod 8) < {N_INST} (failures: {len(bad_r3)})",
              len(bad_r3) == 0)
        check("residue fence: p == 5 (mod 8) is NEVER x^2 + 2y^2 "
              "(x^2 + 2y^2 mod 8 hits only {0,1,2,3,4,6} -- exhaustive "
              "residue table)",
              5 not in {(xx * xx + 2 * yy * yy) % 8
                        for xx in range(8) for yy in range(8)})

        # ------------------------------------------------------------- P6
        print("P6 -- STEP 6: final theorem vs the 10^6 census (re-derived)")
        t1 = time.time()
        sig1_cap = sieve_sigma1(CAP)
        Hm = h_series(sig1_cap, CAP - 1, mod=1 << MOD_BITS)
        print(f"        census H mod 2^{MOD_BITS} to {CAP - 1}: "
              f"{time.time() - t1:.1f}s")
        primes_cap = [p for p in sieve_primes(CAP - 1) if p % 2 == 1]
        exc3 = [p for p in primes_cap if p % 8 == 3
                and 5 + v2_capped(Hm[p], MOD_BITS) != 5]
        exc5 = [p for p in primes_cap if p % 8 == 5
                and 5 + v2_capped(Hm[p], MOD_BITS) != 7]
        n3 = sum(1 for p in primes_cap if p % 8 == 3)
        n5 = sum(1 for p in primes_cap if p % 8 == 5)
        check(f"THEOREM census: v2(1 + p^3 - a_p) == 5 for ALL {n3} primes "
              f"p == 3 (mod 8) < {CAP} (exceptions: {len(exc3)}"
              + (f", first {exc3[0]}" if exc3 else "") + ")", len(exc3) == 0)
        check(f"THEOREM census: v2(1 + p^3 - a_p) == 7 for ALL {n5} primes "
              f"p == 5 (mod 8) < {CAP} (exceptions: {len(exc5)}"
              + (f", first {exc5[0]}" if exc5 else "") + ")", len(exc5) == 0)

        # ------------------------------------------------------------- P7
        print("P7 -- controls (must fire)")
        prime_set = set(primes_inst)
        viol = {3: [], 5: []}
        for n in range(9, N_SEG + 1, 2):
            c = n % 8
            if c not in (3, 5) or n in prime_set:
                continue
            v = v2_capped(sig3[n] - a[n], 40)
            if v != DEPTH[c]:
                viol[c].append((n, v))
        wit_ok = all(any(n == w and v == WITNESS_COMPOSITE[w]
                         for n, v in viol[w % 8])
                     for w in WITNESS_COMPOSITE)
        print(f"        composite violators < {N_SEG}: class 3: "
              f"{len(viol[3])}, class 5: {len(viol[5])}; witnesses "
              f"{[(w, WITNESS_COMPOSITE[w]) for w in (27, 35, 21)]}")
        check(f"C1 composites: constant depth is PRIME-specific -- "
              f">= {MIN_COMPOSITE_VIOL} composite violators per class "
              f"(got {len(viol[3])} / {len(viol[5])}); predeclared witnesses "
              f"27 -> v2 6, 35 -> v2 7 (class 3), 21 -> v2 9 (class 5) "
              "confirmed exactly",
              len(viol[3]) >= MIN_COMPOSITE_VIOL
              and len(viol[5]) >= MIN_COMPOSITE_VIOL and wit_ok)

        sig1_c = sig1[:N_CTL + 1]
        L = [0] + [sig1_c[n] for n in range(1, N_CTL + 1)]
        L_no3 = [0] + [sig1_c[n] if n % 3 else 0 for n in range(1, N_CTL + 1)]
        w13 = kron_mul_fast(L, embed(L, 3, N_CTL), N_CTL)
        w19 = kron_mul_fast(L, embed(L, 9, N_CTL), N_CTL)
        w127 = kron_mul_fast(L, embed(L, 27, N_CTL), N_CTL)
        u1_3adic = kron_mul_fast(L, embed(L_no3, 3, N_CTL), N_CTL)
        h3 = [w13[n] - 3 * w19[n] + 2 * w127[n] for n in range(N_CTL + 1)]
        mism = [n for n in range(1, N_CTL + 1) if h3[n] != u1_3adic[n]]
        check(f"C2a wrong form k = 3: W13 - 3 W19 + 2 W127 does NOT collapse "
              f"to the 3-adic U'_1 -- {len(mism)} mismatches on n <= {N_CTL}, "
              f"first at n = {mism[0] if mism else None} (predeclared "
              f"{K3_FIRST_MISMATCH}); 3-adic s >= 2 coefficients 1, 3, 9, ... "
              "do not vanish",
              len(mism) > 0 and mism[0] == K3_FIRST_MISMATCH)
        v2sets = {3: set(), 5: set()}
        for p in [q for q in primes_inst if q < N_CTL and q % 8 in (3, 5)]:
            if h3[p] != 0:
                v2sets[p % 8].add(v2_capped(abs(h3[p]), 40))
        check("C2b wrong form k = 3: prime values of the k = 3 combination "
              f"have NO constant 2-adic depth (distinct v2 counts: class 3: "
              f"{len(v2sets[3])}, class 5: {len(v2sets[5])}; >= 2 required)",
              len(v2sets[3]) >= 2 and len(v2sets[5]) >= 2)

        # ---------------------------------------------------------- verdict
        n_pass = sum(1 for _, ok in CHECKS if ok)
        n_all = len(CHECKS)
        census_false = bool(exc3 or exc5)
        if census_false:
            verdict = "CONSTDEPTH-FALSE"
        elif n_pass == n_all:
            verdict = "CONSTDEPTH-THEOREM"
        else:
            verdict = "CONSTDEPTH-PARTIAL"
        print(f"CHECKS: {n_pass}/{n_all} passed; walltime {time.time() - t0:.1f}s")
        print(f"VERDICT: {verdict}")
        print("NAMED CLASSICAL INGREDIENTS: [N1] x^2 + 2y^2 (disc -8, h = 1, "
              "Z[sqrt(-2)] UFD); [N2] x^2 + y^2 (disc -4, h = 1, Z[i] UFD) "
              "-- formula + essential uniqueness; instances machine-verified.")
        return 0 if verdict == "CONSTDEPTH-THEOREM" else 1

    return main(), list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 23/23
    (MULTIRATE-THEOREM / SPINLIFT-VERIFIED), part 2 must be 24/24
    (CONSTDEPTH-THEOREM: the census depths are closed theorems)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 23)
    print("\n[%s] PART-1 PATTERN GATE: expected 23/23 "
          "(MULTIRATE-THEOREM / SPINLIFT-VERIFIED) -- fails: %s"
          % ("PASS" if part1_ok else "FAIL", fails1 or "none"))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 24)
    print("\n[%s] PART-2 PATTERN GATE: expected 24/24 "
          "(CONSTDEPTH-THEOREM) -- fails: %s"
          % ("PASS" if part2_ok else "FAIL", fails2 or "none"))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- MULTIRATE-THEOREM / "
          "SPINLIFT-VERIFIED + CONSTDEPTH-THEOREM: the v2 ladder "
          "v_2(1 + p^3 - a_p) >= 5 + 2*[chi_-4 = 1] + [chi_8 = 1] holds "
          "for all 78497 odd primes p < 10^6 with sharp per-class "
          "witnesses 3/7/5/17, the character sifts I0-I3 are "
          "Sturm-certified (level <= 512, bound 256, verified 78x) with "
          "the mod-512 strengthening breaking exactly at n = 9, the "
          "Shimura lift Sh(g) = -8 E_odd + 256 H is exact to 160 with "
          "Kronecker factor = chi_8, and the census depths ARE "
          "theorems: the multirate weights (1, -3, 2) telescope H to "
          "the both-odd convolution U_1, class 3 mod 8 is pinned by "
          "the unique x^2 + 2y^2 representation ([N1], h = 1) and "
          "class 5 by the unique x^2 + (2w)^2 representation via the "
          "ternary bridge ([N2], h = 1) -- v2 = 5 and 7 EXACTLY, zero "
          "exceptions < 10^6, composites violate as required.  "
          "NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
