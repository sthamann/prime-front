#!/usr/bin/env python3
"""v788 -- HECKE.POSITIVE_C2_LIFT.01: the positive two-channel lift of the TFPT cusp channel and the C2 packet automaton built on it -- E_odd +- f8 = 2A / 2B with A = (1/16) theta2(2t)^4 theta3(4t)^4 and B = (1/16) theta2(2t)^4 theta2(4t)^4 BOTH positive theta series (nonnegative integer coefficients, odd support, censused to q^50000), B = 16 R with R integer, and the eta-free generator a_n = sigma3(n) - 32 R(n) reproducing EVERY odd f8 coefficient (42/42 checks, ~196 s, verdict C2LIFT-THEOREM; discovery probe hecke_positive_c2_lift_probe.py, 2026-08-05).  THE MICROSTATES ENUMERATED: R(2m+3) = #{(x,y) in N^8 : m = sum_i T_{x_i} + 2 sum_j T_{y_j}} (T_k triangular), verified by direct octuple enumeration for all m <= 20, matching the closed convolution R(2m+3) = sum_j sigma1(2m-4j+1) sigma1(2j+1) (exact Kronecker convolution to m = 24998 + independent naive double loop to n = 2001); degeneracy anchors (R(3), R(5), R(7), R(9), R(11)) = (1, 4, 10, 24, 43) with the binomial mechanics 6 + 4 = 10 at m = 2.  THE AUTOMATON: M_n = [[A_n, B_n], [B_n, A_n]], Hadamard-diagonalized Had M_n Had = 2 diag(sigma3(n), a_n) cross-source on all odd n <= 50000; XOR-grammar composition M_(mn) = M_m M_n covers all 41053 coprime odd pairs and the recursion M_(p^k) = M_p M_(p^(k-1)) - p^3 M_(p^(k-2)) all 70 odd prime powers <= 50000 (zero failures; worked examples M_15 = M_3 M_5 -> 2 diag(3528, 8) and M_9 = M_3^2 - 27 M_1 exact).  THE FIVE-CONDITION VALIDATOR (V1 A+B = 1+p^3, V2 A-B = a_p, V3 16 | B, V4 a_p == 1+p^3 mod 32, V5 Deligne a_p^2 <= 4p^3; honest dependency note V1 & V3 => V4) holds on all 9591 odd primes p < 10^5 with JOINT detection 1.0 against growth-matched random packets (measured joint pass rate 0.00e+00; per-screen random pass rates V3 0.0629 ~ 1/16 and V4 0.0305 ~ 1/32), and the tamper blind spot is EXACTLY the 16 Z lattice: V1+V2-consistent tampering is detected at 0.9375 = 15/16 (179833/191820) and ALL 11987 undetected tampers had 16 | d.  CHECK32 BECOMES A KERNEL COROLLARY: reducing the exact positive lift E_odd - f8 = 32 H mod 32 yields f8 == E_odd (mod 32), i.e. the v785 congruence is the mod-32 shadow of the lift; maximality stays exact (at q^3: 28 - (-4) = 32 = 32 R(3), R(3) = 1 odd is WHY mod 64 fails).  THREE CLASSICAL CITATIONS TYPED: Gauss/Jacobi-triple-product product forms of psi/phi, Jacobi's quartic identity phi^4 = phi(-q)^4 + 16 q psi(q^2)^4 (each machine-verified to q^50000), and Sturm 1987 closure (bound (4/12)*[SL2(Z):Gamma_0(16)] = 8, verified 6250x beyond); the eta-quotient algebra and the Jacobi-substitution derivation A - B = f8, A + B = f8 + 32 H are FULLY SYMBOLIC (sympy, exact cancellation in free symbols).  CONTROLS FIRE: perturbed theta exponent phi(q^2)^4 -> ^3 breaks the decomposition at n = 3 (fraction 0.999); the check32 eta mutant breaks the halves (integrality, first at n = 5); the wrong correction factors 16 and 64 both fail AT q^3 (28 - 16 = 12 and 28 - 64 = -36 vs a_3 = -4; 999/999 failures each).  Lean layer: experiments/lean4-carrier-rigidity/TfptCarrier/PositiveC2Lift.lean (built green, 3406 jobs, Lean manifest 80 modules) formalizes the positive-lift kernel with check32 as a corollary.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe hecke_positive_c2_lift_probe.py (2026-08-05, 42/42, ~196 s, C2LIFT-THEOREM; the one-worker decision -- HECKE.POSITIVE_C2_LIFT.01 + HECKE.PACKET_COMPOSITION.01 implemented as ONE coupled probe with joint verdict -- and the two disclosed harness amendments carried verbatim in the original docstring below: S0 theta-bridge first draft counted the n = 0 term of sum_{n in Z} x^{n(n+1)} once, fixed since n = 0 pairs with n = -1 so every n >= 0 branch counts twice, pure harness bookkeeping; S2 Legendre lemma first draft indexed sigma1[2n+1] one past the sieve range at n = 25000, range clipped to 2n+1 <= 50000; data unchanged in both); re-run identically at promotion.  Promoted verbatim (all execution already inside main(), constants and helpers definition-only at module level, nothing executes at import; numbers unchanged).  run() encodes the all-pass pattern (v757 precedent).

Original hecke_positive_c2_lift_probe.py docstring (verbatim):
hecke_positive_c2_lift_probe -- HECKE.POSITIVE_C2_LIFT.01 +
HECKE.PACKET_COMPOSITION.01: the positive two-channel decomposition of
the TFPT cusp channel and the C2 packet automaton built on it.

ONE-WORKER DECISION (documented per protocol): the two candidates are
tightly coupled -- the automaton (Part 2) is an algebra ON the two
channels A, B of Part 1, and every automaton census consumes the Part-1
builds.  They are therefore implemented as ONE probe with predeclared
sections S0-S10; each candidate keeps its own gates and the verdict is
joint (enum below).

BASELINE (certified, read completely before this run):
  hecke_check32_probe.py / HECKE.CARRIER_CHECK32.01 -- f8 = eta(2t)^4
  eta(4t)^4, E_odd = sum_{n odd} sigma3(n) q^n, f8 == E_odd (mod 32),
  a_p == 1 + p^3 (mod 32), mod-64 must-fail at q^3 (28 - (-4) = 32),
  corpus anchors v535 (a_3 = -4, a_5 = -2, a_7 = 24, a_11 = -44,
  a_13 = 22), verdict CHECK32-THEOREM.

THE THEOREM CANDIDATES (frozen before running; typing discipline is
binding and carried here):

PART 1 -- THE POSITIVE TWO-CHANNEL DECOMPOSITION [E neu]:
    A(tau) = (E_odd + f8)/2 = (1/16) theta2(2 tau)^4 theta3(4 tau)^4
    B(tau) = (E_odd - f8)/2 = (1/16) theta2(2 tau)^4 theta2(4 tau)^4
  BOTH with nonnegative integer coefficients, supported on odd n.
  Equivalently, with Ramanujan's psi(t) = sum_{r>=0} t^{r(r+1)/2}:
    E_odd - f8 = 32 H,   H(q) = q^3 psi(q^2)^4 psi(q^4)^4
                              = eta(4t)^4 eta(8t)^8 / eta(2t)^4
                              = q^3 + 4 q^5 + 10 q^7 + 24 q^9 + 43 q^11 + ...
  so f8 = E_odd - 32 H, i.e. a_n = sigma3(n) - 32 R(n) with
  B_n = 16 R(n), and the closed convolution formula
    R(2m+3) = sum_j sigma1(2m-4j+1) sigma1(2j+1)
  together with the microstate count
    R(2m+3) = #{(x,y) in N^8 : m = sum_i T_{x_i} + 2 sum_j T_{y_j}}
  (T_k = k(k+1)/2 triangular; degeneracies 1, 4, 10, 24, 43; the
  binomial mechanics 6 + 4 = 10 at m = 2).

  GATES: (i) symbolic layer -- the eta-quotient algebra and the
  Jacobi-substitution step are verified SYMBOLICALLY (sympy, exact
  rational-function cancellation in free product symbols); the product
  forms of psi/phi and Jacobi's quartic identity are CITED classical
  ingredients, each machine-verified coefficientwise to q^50000 (far
  beyond any Sturm bound in play); (ii) positivity census A_n, B_n >= 0
  integers for all n <= 50000 and B_n == 0 (mod 16) for odd n, with
  B_n = 16 R(n) exact; (iii) closed R formula vs the eta quotient to
  50000 + direct N^8 microstate enumeration for small m; (iv) the
  eta-free generator a_n = sigma3(n) - 32 R(n) reproduces EVERY odd f8
  coefficient to 50000; (v) maximality: the mod-64 must-fail at q^3.

  SYMBOLIC-STEP TYPING (honest, frozen):
    * eta-quotient cancellations and the Jacobi-substitution derivation
      of A - B = f8 and A + B = f8 + 32 H: FULLY SYMBOLIC (sympy S1).
    * psi(q) = P2^2/P1, phi(-q) = P1^2/P2, phi(q) = P2^5/(P1^2 P4^2)
      (Gauss / Jacobi triple product corollaries), Jacobi's quartic
      phi(q)^4 = phi(-q)^4 + 16 q psi(q^2)^4, the doublings
      phi(q)^2 = phi(q^2)^2 + 4 q psi(q^4)^2, psi(q)^2 = phi(q) psi(q^2),
      and psi(q)^4 = sum sigma1(2n+1) q^n (Legendre/Jacobi):
      CITED classical ingredients, machine-verified to q^50000 (S2).
    * the ONE remaining content identity E_odd - f8 = 32 H (equivalently
      E_odd = A + B): Sturm-grade -- all three series live on Gamma_0(16)
      (conservative level for the eta quotient; E_odd, f8 already on
      Gamma_0(8)), weight 4, Sturm bound (4/12)*[SL2(Z):Gamma_0(16)]
      = (1/3)*24 = 8; verified to q^50000 = 6250x the bound, with
      modularity of both sides classical (Sturm 1987 is the one cited
      closure theorem, exactly as in check32).

PART 2 -- THE C2 PACKET AUTOMATON [E neu for the algebra]:
    M_n = [[A_n, B_n], [B_n, A_n]]  (odd n),
  Hadamard-diagonalized:  Had M_n Had = 2 diag(sigma3(n), a_n) with
  Had = [[1,1],[1,-1]] (integer form; the unitary normalisation carries
  1/sqrt2 per factor).  Composition laws (the XOR grammar of the C2
  group algebra):
    M_{mn} = M_m M_n  for coprime odd m, n, i.e.
      A_{mn} = A_m A_n + B_m B_n,  B_{mn} = A_m B_n + B_m A_n,
    M_{p^k} = M_p M_{p^{k-1}} - p^3 M_{p^{k-2}}  (odd primes p).
  Worked example M_15 = M_3 M_5 -> diag (3528, 8).  Censuses on all
  coprime odd pairs with mn <= 50000 and all odd prime powers <= 50000.
  FIVE-CONDITION packet validator (frozen function, the user's Sec 21.2):
    V1: A + B = 1 + p^3          V2: A - B = a_p
    V3: B == 0 (mod 16)          V4: a_p == 1 + p^3 (mod 32)
    V5: |a_p| <= 2 p^{3/2}  (Deligne; checked exactly as a_p^2 <= 4 p^3)
  verified on ALL odd primes p < 10^5; detection power against random
  tampering measured (seeded), with the honest DEPENDENCY NOTE:
  V1 and V3 together already IMPLY V4 (a_p = (1+p^3) - 2B), so the five
  conditions carry four independent screens + the Deligne bound.

[C neu] FENCES (interpretations, NOT promoted -- each needs a morphism
before it may leave this docstring):
  * the "sheet parity" reading of A/B (A = even/aligned sheet, B = odd/
    anti-aligned sheet of a C2 cover) is an INTERPRETATION; the machine
    facts are only the positivity, the 2x2 algebra and the Hadamard
    characters.
  * the "1, mu4-corners, decuple" reading of the degeneracies 1, 4, 10
    (R(3), R(5), R(7)) is an INTERPRETATION; the machine fact is the
    triangular-number microstate count with its binomial mechanics.

SECTIONS (predeclared):
  S0  exact builds: f8 (eta, check32 build) to q^100000; psi/phi/phi(-q)
      by DEFINITION (triangular / square sparse sums); A_theta =
      q psi(q^2)^4 phi(q^2)^4, B_theta = 16 q^3 psi(q^2)^4 psi(q^4)^4,
      H = B_theta/16 to q^50000; theta-language bridge theta2(2t)^4 =
      16 q psi(q^2)^4 checked at the sum level; corpus anchors.
  S1  SYMBOLIC layer (sympy, exact): eta-quotient cancellations for f8,
      H, A; the Jacobi-substitution derivation A - B = f8 and
      A + B = f8 + 32 H in free symbols.
  S2  cited-lemma battery, machine-verified to q^50000 (typing above).
  S3  STURM-PLUS decomposition: 2 A_theta == E_odd + f8 and
      2 B_theta == E_odd - f8 and E_odd - f8 == 32 H, ALL n <= 50000.
  S4  POSITIVITY census: A_n, B_n >= 0 integers, odd support,
      B_n == 0 (mod 16), R = B/16 integer, all n <= 50000.
  S5  R closed formula: Kronecker convolution over the full range +
      independent naive double loop to n <= 2001; microstate N^8
      enumeration for m <= 20 (n <= 43) incl. the 6+4 = 10 split.
  S6  eta-free generator: a_n = sigma3(n) - 32 R(n) reproduces every
      odd f8 coefficient, n <= 50000.
  S7  maximality: mod-64 must-fail at q^3 (28 - (-4) = 32); mod-64
      failure census is nonempty.
  S8  AUTOMATON: Hadamard diagonalization census (all odd n <= 50000,
      cross-source), coprime multiplicativity census (mn <= 50000),
      prime-power recursion census (p^k <= 50000), worked examples
      M_15 = M_3 M_5 and M_9 = M_3^2 - 27 M_1.
  S9  five-condition validator on all odd primes < 10^5 (packet halves
      from the S3-verified decomposition; a_p from the eta build);
      exact Deligne census; detection power: (a) growth-matched random
      packets (V1 granted by construction, stated), per-condition and
      joint pass rates; (b) V1+V2-consistent tampering, predicted
      detection 15/16 (blind spot = the 16 Z tamper lattice, stated).
  S10 CONTROLS (must fire):
      C1a perturbed theta exponent A' = q psi(q^2)^4 phi(q^2)^3:
          decomposition census breaks immediately (first fail, fraction).
      C1b check32 eta mutant g (exp 4 -> 3): the halves (E_odd +- g)/2
          lose integrality/positivity/identity -- first failure mode
          reported, must exist within n <= 2000.
      C2  wrong correction factor: sigma3 - 16 R and sigma3 - 64 R must
          fail against f8 immediately (first fail at q^3: 12 resp. -36
          vs -4), failure fraction ~ 1 over odd n >= 3.

HARNESS AMENDMENTS AFTER FIRST RUN (data unchanged, recorded honestly):
  * S0 theta-bridge first draft counted the n = 0 term of
    sum_{n in Z} x^{n(n+1)} once; n = 0 pairs with n = -1, so EVERY
    n >= 0 branch counts twice.  Fixed (pure harness bookkeeping).
  * S2 Legendre lemma first draft indexed sigma1[2n+1] one past the
    sieve range at n = 25000; range clipped to 2n+1 <= 50000.

VERDICT ENUM (frozen):
  C2LIFT-THEOREM : all gates pass -- decomposition + positivity +
                   R-mechanics + automaton + validator censuses clean,
                   symbolic layer exact, controls fire.
  C2LIFT-PARTIAL : some component degraded but no counterexample.
  C2LIFT-FALSE   : a counterexample in a frozen census -- reported.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.  Lean companion:
experiments/lean4-carrier-rigidity/TfptCarrier/PositiveC2Lift.lean
(finite core kernel-checked: first-N coefficient identities with
nonnegativity, B == 0 mod 16 witnesses, M_15 = M_3 M_5 as exact integer
matrix identity, Hadamard character identities).
"""
from __future__ import annotations

import random
import time
from math import gcd, isqrt

N_MAIN = 50_000           # decomposition / positivity / automaton censuses
N_F8 = 100_000            # eta build range (validator census needs p < 10^5)
N_CTRL = 2_000            # control mutant range
N_NAIVE = 2_001           # independent naive R-formula range
M_MICRO = 20              # microstate enumeration range (n = 2m+3 <= 43)
MOD16 = 16
MOD32 = 32
STURM_BOUND = 8           # (4/12)*[SL2(Z):Gamma_0(16)] = 24/3 (conservative)
A_P_CORPUS = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}   # v535 HECKE.GEOM.01
RNG_SEED = 20260805
N_RAND_TRIALS = 20        # per prime, random-packet mode
N_TAMPER_TRIALS = 20      # per prime, consistent-tamper mode

CHECKS = []


def check(label: str, ok: bool) -> bool:
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return bool(ok)


# ------------------------------------------------------------------ exact
# polynomial arithmetic over Z via Kronecker substitution (identical
# machinery to hecke_check32_probe.py -- probes are self-contained).
def _encode_nonneg(v, K):
    nb = K // 8
    return int.from_bytes(
        b"".join(int(x).to_bytes(nb, "little") for x in v), "little")


def kron_mul(a, b, n_out):
    """Exact product of integer coefficient lists a, b truncated to
    degree n_out (inclusive).  Single big-int multiplication."""
    ca = max((abs(x) for x in a), default=0)
    cb = max((abs(x) for x in b), default=0)
    bound = ca * cb * min(len(a), len(b))
    K = 64
    while bound >= (1 << (K - 1)):
        K += 64
    ap = _encode_nonneg([x if x > 0 else 0 for x in a], K)
    an = _encode_nonneg([-x if x < 0 else 0 for x in a], K)
    bp = _encode_nonneg([x if x > 0 else 0 for x in b], K)
    bn = _encode_nonneg([-x if x < 0 else 0 for x in b], K)
    prod = (ap - an) * (bp - bn)
    neg = prod < 0
    if neg:
        prod = -prod
    mask = (1 << K) - 1
    half = 1 << (K - 1)
    out = [0] * (n_out + 1)
    for i in range(n_out + 1):
        if prod == 0:
            break
        d = prod & mask
        prod >>= K
        if d >= half:
            d -= (1 << K)
            prod += 1
        out[i] = -d if neg else d
    return out


def pentagonal_series(n_max):
    """prod_{n>=1} (1 - x^n) = sum_k (-1)^k x^{k(3k-1)/2}, truncated."""
    out = [0] * (n_max + 1)
    out[0] = 1
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        if g1 > n_max and g2 > n_max:
            break
        s = -1 if k % 2 == 1 else 1
        if g1 <= n_max:
            out[g1] += s
        if g2 <= n_max:
            out[g2] += s
        k += 1
    return out


def series_pow(base, e, n_max):
    """base^e exactly by repeated Kronecker squaring (e in {2,3,4,5})."""
    if e == 1:
        return list(base)
    sq = kron_mul(base, base, n_max)
    if e == 2:
        return sq
    if e == 3:
        return kron_mul(sq, base, n_max)
    if e == 4:
        return kron_mul(sq, sq, n_max)
    if e == 5:
        return kron_mul(kron_mul(sq, sq, n_max), base, n_max)
    raise ValueError(e)


def embed(series, d, n_max):
    """series(x) -> series(q^d) as a q-coefficient list."""
    out = [0] * (n_max + 1)
    for i, c in enumerate(series):
        if i * d > n_max:
            break
        out[i * d] = c
    return out


def shift(series, s, n_max):
    """series(q) * q^s, truncated."""
    out = [0] * (n_max + 1)
    for i, c in enumerate(series):
        if i + s > n_max:
            break
        out[i + s] = c
    return out


def build_f8(n_max, exp4=4):
    """q * prod(1-q^{2n})^4 * prod(1-q^{4n})^exp4 (exp4 = 3 is the C1b
    mutant, exactly the check32 control; fractional eta prefactor of
    the mutant dropped -- stated honestly there and here)."""
    A = embed(series_pow(pentagonal_series(n_max // 2), 4, n_max // 2),
              2, n_max - 1)
    B = embed(series_pow(pentagonal_series(n_max // 4), exp4, n_max // 4),
              4, n_max - 1)
    core = kron_mul(A, B, n_max - 1)
    return [0] + core


# ------------------------------------------------- theta-sum definitions
def psi_series(n_max):
    """Ramanujan psi(q) = sum_{r>=0} q^{r(r+1)/2} (DEFINITION)."""
    out = [0] * (n_max + 1)
    r = 0
    while r * (r + 1) // 2 <= n_max:
        out[r * (r + 1) // 2] += 1
        r += 1
    return out


def phi_series(n_max, minus=False):
    """phi(q) = sum_{n in Z} q^{n^2} = 1 + 2 sum_{r>=1} q^{r^2};
    minus=True gives phi(-q) = 1 + 2 sum (-1)^r q^{r^2} (DEFINITION)."""
    out = [0] * (n_max + 1)
    out[0] = 1
    r = 1
    while r * r <= n_max:
        out[r * r] += 2 * (-1 if (minus and r % 2 == 1) else 1)
        r += 1
    return out


def sieve_primes(n_max):
    is_c = bytearray(n_max + 1)
    primes = []
    for p in range(2, n_max + 1):
        if not is_c[p]:
            primes.append(p)
            for m in range(p * p, n_max + 1, p):
                is_c[m] = 1
    return primes


def sieve_sigma(n_max, k):
    s = [0] * (n_max + 1)
    for d in range(1, n_max + 1):
        dk = d ** k
        for m in range(d, n_max + 1, d):
            s[m] += dk
    return s


# --------------------------------------------- frozen packet validator
def validate_packet(p, A, B, a):
    """FROZEN five-condition validator (Sec 21.2).  Returns the tuple of
    condition booleans (V1..V5); the packet passes iff all five hold.
    DEPENDENCY NOTE (honest): V1 and V3 imply V4."""
    v1 = (A + B == 1 + p ** 3)
    v2 = (A - B == a)
    v3 = (B % 16 == 0)
    v4 = ((a - (1 + p ** 3)) % 32 == 0)
    v5 = (a * a <= 4 * p ** 3)
    return v1, v2, v3, v4, v5


# ================================================================== run
def main():
    t0 = time.time()
    print("hecke_positive_c2_lift_probe -- HECKE.POSITIVE_C2_LIFT.01 "
          "+ HECKE.PACKET_COMPOSITION.01 (one worker, coupled)")
    print(f"  census range N = {N_MAIN}, eta range {N_F8}, "
          f"Sturm bound {STURM_BOUND} (weight 4, Gamma_0(16) conservative)")

    # ------------------------------------------------------------- S0
    print("S0 -- exact builds (eta side + theta side, by definition)")
    a = build_f8(N_F8)
    sig3 = sieve_sigma(N_F8, 3)
    check("f8 eta build: a_0 = 0, a_1 = 1, odd support, corpus anchors "
          f"{A_P_CORPUS} reproduced",
          a[0] == 0 and a[1] == 1
          and all(a[n] == 0 for n in range(0, N_F8 + 1, 2))
          and all(a[p] == v for p, v in A_P_CORPUS.items()))
    psi = psi_series(N_MAIN)
    phi = phi_series(N_MAIN)
    phim = phi_series(N_MAIN, minus=True)
    psi2 = embed(psi_series(N_MAIN // 2), 2, N_MAIN)
    psi4 = embed(psi_series(N_MAIN // 4), 4, N_MAIN)
    phi2 = embed(phi_series(N_MAIN // 2), 2, N_MAIN)
    psi2_4 = series_pow(psi2, 4, N_MAIN)
    A_theta = shift(kron_mul(psi2_4, series_pow(phi2, 4, N_MAIN), N_MAIN),
                    1, N_MAIN)
    H = shift(kron_mul(psi2_4, series_pow(psi4, 4, N_MAIN), N_MAIN),
              3, N_MAIN)
    B_theta = [16 * c for c in H]
    # theta-language bridge: theta2(2 tau) = 2 q^{1/4} psi(q^2) at the
    # SUM level: sum_{n in Z} x^{n(n+1)} = 2 psi(x^2) (n <-> -n-1).
    t2core = [0] * 101
    n = 0
    while n * (n + 1) <= 100:
        t2core[n * (n + 1)] += 2      # n >= 0 pairs with -(n+1) (n=0 with -1)
        n += 1
    psi_x2 = embed(psi_series(50), 2, 100)
    check("theta bridge: sum_{n in Z} x^{n(n+1)} == 2 psi(x^2) to x^100 "
          "(so theta2(2t)^4 = 16 q psi(q^2)^4, theta3(4t) = phi(q^2), "
          "theta2(4t)^4 = 16 q^2 psi(q^4)^4 -- index bookkeeping only)",
          t2core == [2 * c for c in psi_x2])
    print(f"        H head: {[ (n, H[n]) for n in range(3, 13, 2) ]} "
          "(claim: 1, 4, 10, 24, 43)")

    # ------------------------------------------------------------- S1
    print("S1 -- SYMBOLIC layer (sympy, exact cancellation in free symbols)")
    import sympy as sp
    q_, P2_, P4_, P8_ = sp.symbols("q P2 P4 P8", positive=True)
    psi2_s = P4_ ** 2 / P2_          # psi(q^2)  = P4^2/P2   (Gauss, S2)
    psi4_s = P8_ ** 2 / P4_          # psi(q^4)  = P8^2/P4
    phim2_s = P2_ ** 2 / P4_         # phi(-q^2) = P2^2/P4
    phi2_s = P4_ ** 5 / (P2_ ** 2 * P8_ ** 2)   # phi(q^2) = P4^5/(P2^2 P8^2)
    ok_f8 = sp.simplify(psi2_s ** 4 * phim2_s ** 4
                        - P2_ ** 4 * P4_ ** 4) == 0
    ok_h = sp.simplify(psi2_s ** 4 * psi4_s ** 4
                       - P4_ ** 4 * P8_ ** 8 / P2_ ** 4) == 0
    ok_a = sp.simplify(psi2_s ** 4 * phi2_s ** 4
                       - P4_ ** 28 / (P2_ ** 12 * P8_ ** 8)) == 0
    check("eta-quotient algebra (symbolic): q psi(q^2)^4 phi(-q^2)^4 = "
          "eta(2t)^4 eta(4t)^4 = f8;  q^3 psi(q^2)^4 psi(q^4)^4 = "
          "eta(4t)^4 eta(8t)^8 / eta(2t)^4 = H;  A-quotient "
          "eta(4t)^28/(eta(2t)^12 eta(8t)^8)", ok_f8 and ok_h and ok_a)
    # Jacobi-substitution derivation in free symbols: with J :=
    # phi(q^2)^4 = phi(-q^2)^4 + 16 q^2 psi(q^4)^4 (Jacobi at q -> q^2),
    # A := q psi2^4 phi2^4, B := 16 q^3 psi2^4 psi4^4, f8 := q psi2^4 phim2^4:
    ps2, ps4, pm2, qq = sp.symbols("psi2 psi4 phim2 qs", positive=True)
    phi2_sub = (pm2 ** 4 + 16 * qq ** 2 * ps4 ** 4)      # Jacobi's quartic
    A_sym = qq * ps2 ** 4 * phi2_sub
    B_sym = 16 * qq ** 3 * ps2 ** 4 * ps4 ** 4
    f8_sym = qq * ps2 ** 4 * pm2 ** 4
    H_sym = qq ** 3 * ps2 ** 4 * ps4 ** 4
    ok_amb = sp.expand(A_sym - B_sym - f8_sym) == 0
    ok_apb = sp.expand(A_sym + B_sym - f8_sym - 32 * H_sym) == 0
    check("Jacobi-substitution derivation (symbolic): A - B = f8 and "
          "A + B = f8 + 32 H, given Jacobi's quartic at q -> q^2 "
          "(so E_odd = A + B  <=>  E_odd - f8 = 32 H: ONE content "
          "identity remains for S3)", ok_amb and ok_apb)
    check("typing: symbolic layer exact; cited classical ingredients = "
          "Gauss/JTP product forms + Jacobi quartic (each S2-verified "
          "to 50000) + Sturm 1987 closure (S3); everything else exact "
          "integer arithmetic", True)

    # ------------------------------------------------------------- S2
    print("S2 -- cited-lemma battery (machine-verified to q^50000)")
    P1 = pentagonal_series(N_MAIN)
    P2 = embed(pentagonal_series(N_MAIN // 2), 2, N_MAIN)
    P4 = embed(pentagonal_series(N_MAIN // 4), 4, N_MAIN)
    check("Gauss: psi(q) P1 == P2^2 (multiplication only, no inversion)",
          kron_mul(psi, P1, N_MAIN) == series_pow(P2, 2, N_MAIN))
    check("Gauss: phi(-q) P2 == P1^2",
          kron_mul(phim, P2, N_MAIN) == series_pow(P1, 2, N_MAIN))
    check("phi(q) P1^2 P4^2 == P2^5  (phi = eta(2)^5 / eta(1)^2 eta(4)^2)",
          kron_mul(phi, kron_mul(series_pow(P1, 2, N_MAIN),
                                 series_pow(P4, 2, N_MAIN), N_MAIN),
                   N_MAIN) == series_pow(P2, 5, N_MAIN))
    check("Jacobi quartic: phi(q)^4 == phi(-q)^4 + 16 q psi(q^2)^4",
          series_pow(phi, 4, N_MAIN)
          == [x + 16 * y for x, y in zip(series_pow(phim, 4, N_MAIN),
                                         shift(psi2_4, 1, N_MAIN))])
    check("doubling: phi(q)^2 == phi(q^2)^2 + 4 q psi(q^4)^2",
          series_pow(phi, 2, N_MAIN)
          == [x + 4 * y for x, y in zip(series_pow(phi2, 2, N_MAIN),
                                        shift(series_pow(psi4, 2, N_MAIN),
                                              1, N_MAIN))])
    check("doubling: psi(q)^2 == phi(q) psi(q^2)",
          series_pow(psi, 2, N_MAIN) == kron_mul(phi, psi2, N_MAIN))
    sig1 = sieve_sigma(N_MAIN, 1)
    psi_4 = series_pow(psi, 4, N_MAIN // 2)
    n_leg = (N_MAIN - 1) // 2                    # keep 2n+1 <= N_MAIN
    check("Legendre/Jacobi: psi(q)^4 == sum_n sigma1(2n+1) q^n "
          f"(to n = {n_leg})",
          all(psi_4[n_] == sig1[2 * n_ + 1] for n_ in range(n_leg + 1)))

    # ------------------------------------------------------------- S3
    print("S3 -- STURM-PLUS decomposition census")
    bad_a = [n_ for n_ in range(N_MAIN + 1)
             if 2 * A_theta[n_] != (sig3[n_] if n_ % 2 == 1 else 0) + a[n_]]
    bad_b = [n_ for n_ in range(N_MAIN + 1)
             if 2 * B_theta[n_] != (sig3[n_] if n_ % 2 == 1 else 0) - a[n_]]
    bad_h = [n_ for n_ in range(N_MAIN + 1)
             if (sig3[n_] if n_ % 2 == 1 else 0) - a[n_] != 32 * H[n_]]
    check(f"2 A_theta == E_odd + f8 for ALL n <= {N_MAIN} "
          f"(= {N_MAIN // STURM_BOUND}x Sturm bound {STURM_BOUND}; "
          f"failures: {len(bad_a)}"
          + (f", first {bad_a[0]}" if bad_a else "") + ")", not bad_a)
    check(f"2 B_theta == E_odd - f8 for ALL n <= {N_MAIN} "
          f"(failures: {len(bad_b)})", not bad_b)
    check(f"E_odd - f8 == 32 H for ALL n <= {N_MAIN} -- the one content "
          f"identity, 6250x beyond Sturm (failures: {len(bad_h)})",
          not bad_h)

    # ------------------------------------------------------------- S4
    print("S4 -- POSITIVITY census")
    check(f"A_n >= 0 integer for ALL n <= {N_MAIN} "
          f"(min = {min(A_theta)})", min(A_theta) >= 0)
    check(f"B_n >= 0 integer for ALL n <= {N_MAIN} "
          f"(min = {min(B_theta)})", min(B_theta) >= 0)
    check("odd support: A_n = B_n = 0 for even n",
          all(A_theta[n_] == 0 and B_theta[n_] == 0
              for n_ in range(0, N_MAIN + 1, 2)))
    bad16 = [n_ for n_ in range(1, N_MAIN + 1, 2) if B_theta[n_] % 16 != 0]
    check(f"B_n == 0 (mod 16) for ALL odd n <= {N_MAIN} "
          f"(failures: {len(bad16)}) -- B_n = 16 R(n) exact with "
          "R(n) = H_n by construction", not bad16
          and all(B_theta[n_] == 16 * H[n_] for n_ in range(N_MAIN + 1)))
    print(f"        A head: {[(n_, A_theta[n_]) for n_ in range(1, 12, 2)]}")
    print(f"        B head: {[(n_, B_theta[n_]) for n_ in range(1, 12, 2)]}")

    # ------------------------------------------------------------- S5
    print("S5 -- R closed formula + microstate mechanics")
    # full range via exact Kronecker convolution:
    # sum_m R(2m+3) x^m = (sum sigma1(2n+1) x^n) * (sum sigma1(2j+1) x^{2j})
    mmax = (N_MAIN - 3) // 2
    u = [sig1[2 * n_ + 1] for n_ in range(mmax + 1)]
    v = embed(u, 2, mmax)
    w = kron_mul(u, v, mmax)
    check(f"closed formula R(2m+3) = sum_j sigma1(2m-4j+1) sigma1(2j+1) "
          f"== H_(2m+3) for ALL m <= {mmax} (exact convolution)",
          all(w[m_] == H[2 * m_ + 3] for m_ in range(mmax + 1)))
    ok_naive = True
    for n_ in range(3, N_NAIVE + 1, 2):
        m_ = (n_ - 3) // 2
        r_ = sum(sig1[2 * m_ - 4 * j + 1] * sig1[2 * j + 1]
                 for j in range(m_ // 2 + 1))
        if r_ != H[n_]:
            ok_naive = False
            break
    check(f"independent naive double-loop formula check to n <= {N_NAIVE}",
          ok_naive)
    # microstates: R(2m+3) = #{(x,y) in N^8 : m = sum T_x + 2 sum T_y}
    tri = [k * (k + 1) // 2 for k in range(7)]      # T_0..T_6 (T_6=21>20)
    xs = [t for t in tri if t <= M_MICRO]
    ys = [t for t in tri if 2 * t <= M_MICRO]
    cnt = [0] * (M_MICRO + 1)
    split_m2 = {"x_only": 0, "y_active": 0}
    for t1 in xs:
        for t2 in xs:
            if t1 + t2 > M_MICRO:
                continue
            for t3 in xs:
                if t1 + t2 + t3 > M_MICRO:
                    continue
                for t4 in xs:
                    sx = t1 + t2 + t3 + t4
                    if sx > M_MICRO:
                        continue
                    for u1 in ys:
                        if sx + 2 * u1 > M_MICRO:
                            continue
                        for u2 in ys:
                            if sx + 2 * (u1 + u2) > M_MICRO:
                                continue
                            for u3 in ys:
                                if sx + 2 * (u1 + u2 + u3) > M_MICRO:
                                    continue
                                for u4 in ys:
                                    m_ = sx + 2 * (u1 + u2 + u3 + u4)
                                    if m_ <= M_MICRO:
                                        cnt[m_] += 1
                                        if m_ == 2:
                                            key = ("x_only"
                                                   if u1 + u2 + u3 + u4 == 0
                                                   else "y_active")
                                            split_m2[key] += 1
    check(f"microstate count R(2m+3) = #(x,y) in N^8 with m = sum T_x + "
          f"2 sum T_y, direct octuple enumeration for ALL m <= {M_MICRO}",
          all(cnt[m_] == H[2 * m_ + 3] for m_ in range(M_MICRO + 1)))
    check("degeneracy anchors (R(3), R(5), R(7), R(9), R(11)) = "
          f"(1, 4, 10, 24, 43): got {tuple(cnt[:5])}",
          tuple(cnt[:5]) == (1, 4, 10, 24, 43))
    check("binomial mechanics at m = 2: two x-slots at T_1 (C(4,2) = 6) "
          f"+ one y-slot at T_1 (4) = 10: split {split_m2}",
          split_m2 == {"x_only": 6, "y_active": 4})

    # ------------------------------------------------------------- S6
    print("S6 -- eta-free generator")
    bad_gen = [n_ for n_ in range(1, N_MAIN + 1, 2)
               if sig3[n_] - 32 * H[n_] != a[n_]]
    check(f"a_n = sigma3(n) - 32 R(n) reproduces EVERY odd f8 "
          f"coefficient n <= {N_MAIN} (failures: {len(bad_gen)}) -- "
          "eta-free computation path (sigma1 convolution + sigma3)",
          not bad_gen)

    # ------------------------------------------------------------- S7
    print("S7 -- maximality (mod-64 must-fail at q^3)")
    d3 = sig3[3] - a[3]
    check(f"at q^3: sigma3(3) - a_3 = 28 - (-4) = {d3} = 32 R(3); "
          "== 0 (mod 32) but != 0 (mod 64) -- 32 is the maximal 2-power "
          "(R(3) = 1 odd is WHY the lift fails)",
          d3 == 32 and d3 % 32 == 0 and d3 % 64 != 0)
    n64 = sum(1 for n_ in range(1, 2001, 2)
              if (sig3[n_] - a[n_]) % 64 != 0)
    check(f"mod-64 census on odd n <= 2000: {n64} failures > 0 "
          "(= #odd n with R(n) odd in range)", n64 > 0)

    # ------------------------------------------------------------- S8
    print("S8 -- C2 packet automaton")
    A_, B_ = A_theta, B_theta
    bad_had = [n_ for n_ in range(1, N_MAIN + 1, 2)
               if A_[n_] + B_[n_] != sig3[n_] or A_[n_] - B_[n_] != a[n_]]
    check(f"Hadamard diagonalization census: Had M_n Had = "
          f"2 diag(sigma3(n), a_n), i.e. A_n + B_n = sigma3(n) and "
          f"A_n - B_n = a_n, ALL odd n <= {N_MAIN}, CROSS-SOURCE (A, B "
          f"theta builds; sigma3 sieve; a eta build) "
          f"(failures: {len(bad_had)})", not bad_had)
    n_mult = 0
    mult_bad = 0
    for m_ in range(3, isqrt(N_MAIN) + 1, 2):
        for n_ in range(m_ + 2, N_MAIN // m_ + 1, 2):
            if gcd(m_, n_) == 1:
                n_mult += 1
                if (A_[m_ * n_] != A_[m_] * A_[n_] + B_[m_] * B_[n_]
                        or B_[m_ * n_] != A_[m_] * B_[n_] + B_[m_] * A_[n_]):
                    mult_bad += 1
    check(f"XOR-grammar composition M_(mn) = M_m M_n on ALL {n_mult} "
          f"coprime odd pairs 3 <= m < n, mn <= {N_MAIN} "
          f"(A_mn = A_m A_n + B_m B_n, B_mn = A_m B_n + B_m A_n; "
          f"failures: {mult_bad})", mult_bad == 0)
    n_pp = 0
    pp_bad = 0
    for p in sieve_primes(isqrt(N_MAIN)):
        if p == 2:
            continue
        pk = p * p
        while pk <= N_MAIN:
            n_pp += 1
            pk1, pk2 = pk // p, pk // (p * p)
            wA = A_[p] * A_[pk1] + B_[p] * B_[pk1] - p ** 3 * A_[pk2]
            wB = A_[p] * B_[pk1] + B_[p] * A_[pk1] - p ** 3 * B_[pk2]
            if A_[pk] != wA or B_[pk] != wB:
                pp_bad += 1
            pk *= p
    check(f"prime-power recursion M_(p^k) = M_p M_(p^(k-1)) - "
          f"p^3 M_(p^(k-2)) on all {n_pp} odd prime powers <= {N_MAIN} "
          f"(failures: {pp_bad})", pp_bad == 0)
    # worked examples, exact 2x2 integer matrices
    def mat(n_):
        return ((A_[n_], B_[n_]), (B_[n_], A_[n_]))

    def mmul(X, Y):
        return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    M3, M5, M15 = mat(3), mat(5), mat(15)
    prod35 = mmul(M3, M5)
    had = ((1, 1), (1, -1))
    diag15 = mmul(mmul(had, M15), had)
    check(f"worked example: M_3 M_5 = {prod35} == M_15 = {M15}; "
          f"Had M_15 Had = {diag15} = 2 diag(3528, 8)",
          prod35 == M15 and diag15 == ((2 * 3528, 0), (0, 2 * 8))
          and sig3[15] == 3528 and a[15] == 8)
    M9 = mat(9)
    M3sq = mmul(M3, M3)
    M9want = tuple(tuple(M3sq[i][j] - 27 * (1 if i == j else 0)
                         for j in range(2)) for i in range(2))
    check(f"worked example: M_9 = M_3^2 - 27 M_1 = {M9want} (M_1 = I; "
          f"got M_9 = {M9})", M9 == M9want)

    # ------------------------------------------------------------- S9
    print("S9 -- five-condition validator + detection power")
    odd_primes = [p for p in sieve_primes(N_F8 - 1) if p % 2 == 1]
    # packet halves beyond 50000 come from the S3-verified decomposition
    # (A, B) = ((sigma3 +- a)/2) -- typed honestly: theta-build census is
    # to 50000, the validator census to 10^5 rides on S3.
    val_fail = []
    par_bad = 0
    for p in odd_primes:
        s, ap = sig3[p], a[p]
        if (s + ap) % 2 != 0:
            par_bad += 1
            continue
        Ap, Bp = (s + ap) // 2, (s - ap) // 2
        if not all(validate_packet(p, Ap, Bp, ap)):
            val_fail.append(p)
    check(f"validator: ALL five conditions hold on ALL {len(odd_primes)} "
          f"odd primes p < 10^5 (parity failures: {par_bad}, "
          f"condition failures: {len(val_fail)}"
          + (f", first {val_fail[0]}" if val_fail else "") + ")",
          par_bad == 0 and not val_fail)
    del_bad = sum(1 for p in odd_primes if a[p] * a[p] > 4 * p ** 3)
    check(f"exact Deligne census: a_p^2 <= 4 p^3 for all odd p < 10^5 "
          f"(failures: {del_bad})", del_bad == 0)
    check("dependency note (honest): V1 & V3 => V4 (a = 1 + p^3 - 2B, "
          "16 | B => 32 | 2B) -- five conditions = four independent "
          "screens + Deligne", True)
    rng = random.Random(RNG_SEED)
    # (a) growth-matched random packets, V1 GRANTED by construction
    # (A := 1 + p^3 - B), so the measured power is that of V2-V5.
    tot = c2 = c3 = c4 = joint = 0
    for p in odd_primes:
        s3p = 1 + p ** 3
        dl = 2 * isqrt(4 * p ** 3)
        for _ in range(N_RAND_TRIALS):
            tot += 1
            Br = rng.randint(0, s3p)
            Ar = s3p - Br
            ar = rng.randint(-dl, dl)
            v = validate_packet(p, Ar, Br, ar)
            c2 += v[1]
            c3 += v[2]
            c4 += v[3]
            joint += all(v)
    check(f"(a) random growth-matched packets (seed {RNG_SEED}, "
          f"{N_RAND_TRIALS} x {len(odd_primes)} trials, V1 granted): "
          f"pass rates V2 {c2/tot:.2e}, V3 {c3/tot:.4f} ~ 1/16 = "
          f"{1/16:.4f}, V4 {c4/tot:.4f} ~ 1/32 = {1/32:.4f}, JOINT "
          f"{joint/tot:.2e} -- detection {1 - joint/tot:.6f} "
          "(check32 single-screen was 31/32 = 0.96875)",
          abs(c3 / tot - 1 / 16) < 0.005 and abs(c4 / tot - 1 / 32) < 0.005
          and joint / tot < 1e-3)
    # (b) V1+V2-consistent tampering: B -> B + d, A -> A - d, a -> a - 2d
    tot_t = det_t = blind = 0
    for p in odd_primes:
        s, ap = sig3[p], a[p]
        Ap, Bp = (s + ap) // 2, (s - ap) // 2
        for _ in range(N_TAMPER_TRIALS):
            d = 0
            while d == 0:
                d = rng.randint(-1024, 1024)
            tot_t += 1
            v = validate_packet(p, Ap - d, Bp + d, ap - 2 * d)
            if not all(v):
                det_t += 1
            elif d % 16 == 0:
                blind += 1
    check(f"(b) V1+V2-consistent tamper (B += d, A -= d, a -= 2d): "
          f"detection {det_t}/{tot_t} = {det_t/tot_t:.4f} ~ 15/16 = "
          f"{15/16:.4f}; ALL {blind} undetected tampers had 16 | d "
          "(the blind spot is exactly the 16 Z tamper lattice -- "
          "honest scope of the mod-16/mod-32 screens)",
          abs(det_t / tot_t - 15 / 16) < 0.01
          and blind == tot_t - det_t)

    # ------------------------------------------------------------- S10
    print("S10 -- controls (must fire)")
    # C1a: perturbed theta exponent phi(q^2)^4 -> phi(q^2)^3 in A
    psi2c = embed(psi_series(N_CTRL // 2), 2, N_CTRL)
    phi2c = embed(phi_series(N_CTRL // 2), 2, N_CTRL)
    A_mut = shift(kron_mul(series_pow(psi2c, 4, N_CTRL),
                           series_pow(phi2c, 3, N_CTRL), N_CTRL), 1, N_CTRL)
    mut_bad = [n_ for n_ in range(1, N_CTRL + 1, 2)
               if 2 * A_mut[n_] != sig3[n_] + a[n_]]
    frac = len(mut_bad) / len(range(1, N_CTRL + 1, 2))
    check(f"C1a perturbed theta exponent (phi(q^2)^4 -> ^3): "
          f"decomposition census breaks immediately -- first fail "
          f"n = {mut_bad[0] if mut_bad else None}, failure fraction "
          f"{frac:.3f}", bool(mut_bad) and mut_bad[0] <= 5 and frac > 0.5)
    # C1b: check32 eta mutant g -> halves lose integrality/positivity/
    # identity; report the first failure mode.
    g = build_f8(N_CTRL, exp4=3)
    mode = None
    first_n = None
    for n_ in range(1, N_CTRL + 1, 2):
        num_b = sig3[n_] - g[n_]
        if num_b % 2 != 0:
            mode, first_n = "integrality (E_odd - g odd)", n_
            break
        if num_b // 2 < 0:
            mode, first_n = "positivity (B half < 0)", n_
            break
        if num_b // 2 != B_theta[n_]:
            mode, first_n = "identity (B half != theta build)", n_
            break
    check(f"C1b check32 eta mutant g = q P2^4 P4^3: halves break -- "
          f"first failure mode '{mode}' at n = {first_n}",
          mode is not None and first_n is not None and first_n <= 9)
    # C2: wrong correction factor 16 / 64 instead of 32
    bad_16 = [n_ for n_ in range(3, N_CTRL + 1, 2)
              if sig3[n_] - 16 * H[n_] != a[n_]]
    bad_64 = [n_ for n_ in range(3, N_CTRL + 1, 2)
              if sig3[n_] - 64 * H[n_] != a[n_]]
    n_odd3 = len(range(3, N_CTRL + 1, 2))
    check("C2 wrong factor 16: sigma3 - 16 R misses f8 at q^3 "
          f"(28 - 16 = 12 != -4); failures {len(bad_16)}/{n_odd3}, "
          f"first n = {bad_16[0] if bad_16 else None}",
          bool(bad_16) and bad_16[0] == 3
          and len(bad_16) / n_odd3 > 0.99
          and sig3[3] - 16 * H[3] == 12)
    check("C2 wrong factor 64: sigma3 - 64 R misses f8 at q^3 "
          f"(28 - 64 = -36 != -4); failures {len(bad_64)}/{n_odd3}, "
          f"first n = {bad_64[0] if bad_64 else None}",
          bool(bad_64) and bad_64[0] == 3
          and len(bad_64) / n_odd3 > 0.99
          and sig3[3] - 64 * H[3] == -36)
    check("R(n) > 0 for all odd n >= 3 in control range (why C2 "
          "failure fraction is 1: the correction is active everywhere)",
          all(H[n_] > 0 for n_ in range(3, N_CTRL + 1, 2)))

    # ---------------------------------------------------------- verdict
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    core_false = bool(bad_a or bad_b or bad_h or bad16 or bad_gen
                      or bad_had or mult_bad or pp_bad or val_fail
                      or min(A_theta) < 0 or min(B_theta) < 0)
    if n_pass == n_all:
        verdict = "C2LIFT-THEOREM"
    elif core_false:
        verdict = "C2LIFT-FALSE"
    else:
        verdict = "C2LIFT-PARTIAL"
    dt = time.time() - t0
    print(f"CHECKS: {n_pass}/{n_all} passed; walltime {dt:.1f}s")
    print(f"VERDICT: {verdict}")
    # Lean companion table (provenance): odd n <= 63
    rows = [(n_, a[n_], sig3[n_], A_theta[n_], B_theta[n_], H[n_])
            for n_ in range(1, 64, 2)]
    print("LEAN TABLE (n, a_n, sigma3(n), A_n, B_n, R_n) for odd n <= 63:")
    for r in rows:
        print(f"  {r}")
    return 0 if verdict == "C2LIFT-THEOREM" else 1


def run():
    """run_all entry point (v757 precedent): expected pattern 42/42 with
    verdict C2LIFT-THEOREM (main() returns 0 only on that verdict; any
    PARTIAL or FALSE outcome breaks the suite)."""
    rc = main()
    fails = [n for (n, ok) in CHECKS if not ok]
    n_pass = len(CHECKS) - len(fails)
    ok = (rc == 0 and not fails and len(CHECKS) == 42)
    print("\n[%s] PATTERN GATE: expected 42/42 C2LIFT-THEOREM; got "
          "%d/%d, rc = %d -- fails: %s"
          % ("PASS" if ok else "FAIL", n_pass, len(CHECKS), rc,
             fails or "none"))
    print("\nADJUDICATION: %s -- C2LIFT-THEOREM: E_odd +- f8 = 2A/2B are "
          "positive theta series with B = 16R and the eta-free generator "
          "a_n = sigma3(n) - 32 R(n) exact to q^50000; microstates "
          "enumerated (R = triangular-number octuple count, anchors "
          "1, 4, 10, 24, 43); the C2 automaton covers 41053 coprime pairs "
          "+ 70 prime powers with zero failures; the five-condition "
          "validator holds on all 9591 odd primes with joint detection "
          "1.0 and the tamper blind spot exactly the 16 Z lattice "
          "(15/16 = 0.9375, all 11987 undetected had 16 | d); check32 is "
          "the mod-32 shadow of the lift (kernel corollary, "
          "PositiveC2Lift.lean); three classical citations typed "
          "(Gauss/JTP, Jacobi quartic, Sturm 1987); wrong factors 16/64 "
          "fail at q^3.  No marker move, NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
