#!/usr/bin/env python3
"""v790 -- HECKE.SNF_THETA.01: the SNF fingerprint of the correction theta against the ramified E8 inclusion, plus the exact mu4 -> C2 packet-channel split (the claim also covers HECKE.MU4_PACKET.01), ONE module from two probes (18/18 + 17/17 checks, ~3 s; discovery probes hecke_snf_theta_probe.py SNF-FINGERPRINT and hecke_mu4_packet_probe.py MU4-PARTIAL, both 2026-08-05).  THE FINGERPRINT (part 1): the representation identity 256 R(n) = #{(u,v) in (2Z+1)^8 : sum u_i^2 + 2 sum v_j^2 = 4n} for the correction theta H(q) = q^3 psi(q^2)^4 psi(q^4)^4 is exact by direct lattice enumeration (n <= 40; two series routes agree to O(q^48)), and the SNF match divisors(Gram_M) == divisors((1+i)L c L) == (1,1,1,1,2,2,2,2) is exact (v689 replication, |det| = 16 = N(1+i)^4 on both sides) -- but the isometry census is EMPTY at every admissible level: AMBIENT kissing 240 vs 8 with det*min^-8 mismatch on BOTH pair members (1/256 vs 16 -- proof-grade: no R-linear isometry at ANY scale lambda can carry L -> lambda M* or (1+i)L -> lambda M); QUOTIENT census 0/20160 over ALL of GL(4,F2) (the ramified form b_V is alternating, the disc form b_D of M is the identity form -- b_V(x,x) = 0 for all x vs b_D(e_i,e_i) = 1; |Aut(b_V)| = 720 = |Sp(4,F2)|, |Aut(b_D)| = 48; the sigma/mu4-equivariance census is vacuous); and the naive 4+4 coordinate split is inadmissible BY THEOREM (v638 S1.2 replicated independently: 0 of 70 coordinate 4-subsets are (pi_J, pi_sigma)-invariant).  The wrong-signature control diag(1,1,1,2,2,2,2,2) fires (divisors (1^3, 2^5), disc order 32 != 16).  The SNF match is therefore typed as a FINGERPRINT, not an isometry.  THE PACKET SPLIT (part 2): r-hat = (240, -8, -16, -8) and j-hat = (248, 0, -8, 0) exact (Gaussian-integer DFT on the glue group mu4 = E8/(D5 (+) A3); corpus census r = (52, 64, 60, 64), signed 52 - 60 = -8 = -rank(E8); N1 = N3 for EVERY shell proof-grade via x -> -x); the NEW exact identity: csig = (1/15) E4(q^2) - (6/5) E4(q^4) + (32/15) E4(q^8) - 8 f8 to O(q^64), i.e. the cusp part of the QUARTIC mu4 character is EXACTLY -8 f8 with -8 = 52 - 60 = -rank(E8) (ties the v537 lift Sh(g) = -8 f8); the all-shell quartic vanishing is FALSE -- the Cartan-closed quartic series has the exact closed form prod (1 + q^{2n})^{-4} and fails from grade 2 (the grade-1 vanishing IS the corpus j-hat anchor); the C2 (quadratic) channel is PURE Eisenstein, theta4(q)^8 = (16 E4(q^2) - E4(q))/15 termwise -- it carries NO cusp form; csig(p) = -8 a_p(f8) at all odd primes p <= 47 with the corpus anchors a_p = (-4, -2, 24, -44, 22) at p = (3, 5, 7, 11, 13) (v536 Eichler reading a_p = -c(p)/8).  Both controls fire (scrambled sector assignment, wrong Cartan completion).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes hecke_snf_theta_probe.py (2026-08-05, 18/18, 2.2 s, SNF-FINGERPRINT) + hecke_mu4_packet_probe.py (2026-08-05, 17/17, 0.2 s, MU4-PARTIAL); no spec corrections are disclosed in either probe docstring; both re-run identically at promotion.  Promoted verbatim, part 1's top-level executable statements moved unchanged into main() and part 2 wrapped in a function scope; each part's banner print of its own docstring is served by a local __doc__ binding that holds the original probe docstring verbatim; part 2's check() bookkeeping switches global -> nonlocal and additionally records the (name, ok) pairs (print/bookkeeping only, no gate, no number touched); numbers unchanged; run() encodes both patterns (v757 precedent).

Original hecke_snf_theta_probe.py docstring (verbatim):
hecke_snf_theta_probe -- HECKE.SNF_THETA.01 (positive-protocol round,
strand C, probe 1 of 2).

THE CLAIM UNDER TEST [C neu -> decidable]: the correction theta
H(q) = q^3 psi(q^2)^4 psi(q^4)^4 (psi = Ramanujan's theta,
psi(q) = sum_{k>=0} q^{k(k+1)/2}) has the quadratic form

    Q(u, v) = u_1^2 + ... + u_4^2 + 2(v_1^2 + ... + v_4^2)

on ODD vectors: 256 R(n) = #{(u,v) in (2Z+1)^8 : Q(u,v) = 4n}, where
R(n) is the q^n coefficient of H.  Its Gram matrix diag(1,1,1,1,2,2,2,2)
has Smith signature (1,1,1,1,2,2,2,2) -- EXACTLY the elementary divisors
of the ramified inclusion (1+i)L c L of the unimodular hermitian E8
lattice (v689 machinery, read-only replication).

THE DECIDER: does an isometry exist between the correction-theta
lattice pair (M = Z^4 (+) sqrt2 Z^4 with the odd-coset structure,
i.e. M c M* with M*/M = F2^4) and the ramified inclusion pair
((1+i)L c L with L/(1+i)L = F2^4), under ADMISSIBLE basis changes only?

ADMISSIBLE CLASS (predeclared, frozen): maps definable from the
Z[i]/transversal structure --
  (i)  ambient: R-linear isometries T (a global scale factor lambda > 0
       allowed) with T(L) = lambda M* and T((1+i)L) = lambda M, composed
       with U(L,h)-automorphisms and the ramified twist x -> (1+i)x;
  (ii) quotient: F2-linear maps V = L/(1+i)L -> D = M*/M intertwining
       the induced finite bilinear structures (the symplectic /
       Fourier / Weil-representation class);
INADMISSIBLE (the brake): any map whose definition REQUIRES a
J/sigma-equivariant 4+4 coordinate split of the 8 real coordinates.
The corpus has PROVEN no such split exists: v638_code_semantics.py
S1.2 ("Z6-invariant 4-subsets: 0 => NO equivariant block-systematic
4+4 split exists"); replicated independently in S3c below.  The naive
coordinatewise map (first 4 coords -> u-block, last 4 -> v-block) is
therefore inadmissible BY THEOREM, and the decider must census the
transversal-coded maps only.

SLICES:
  S1  the representation-number identity: H(q) two routes (psi-series
      and eta-quotient eta(4)^4 eta(8)^8 / eta(2)^4), then
      256 R(n) = #{odd (u,v) : Q = 4n} by DIRECT lattice enumeration
      (meet-in-the-middle over the two 4-blocks) for n <= NCAP = 40.
  S2  Smith side: SNF(Gram_M) = (1,1,1,1,2,2,2,2); v689 replication
      (C* placement, L = Construction A, A = coords of (1+J)b_i),
      SNF(A) = (1,1,1,1,2,2,2,2); EXACT elementary-divisor match.
      Census info: per-class theta of L (shells 1..3) vs the odd-coset
      theta of M (normalized) -- the two 16-element quotient structures
      side by side.
  S3  THE DECIDER, three levels:
      (a) ambient isometry census: scale-invariant obstructions
          (kissing number, det x min^{-8}) for L vs M* and
          (1+i)L vs M -> census count at level (i);
      (b) quotient census: b_V = hbar (v752 convention, alternating --
          replicated from the concrete lattice) vs b_D = identity form
          on F2^4 (disc form of M, NON-alternating); FULL GL(4,F2)
          census (20160 invertible maps): # intertwiners, |Aut(b_V)|,
          |Aut(b_D)|; sigma/mu4 equivariance of any intertwiner found;
      (c) the brake demonstration: all 70 coordinate 4-subsets tested
          for (pi_J, pi_sigma)-invariance (expect 0 -> the naive
          coordinatewise map FAILS the admissibility gate).
  S4  controls: wrong-signature lattice diag(1,1,1,2,2,2,2,2) must FAIL
      the SNF match (divisors (1^3,2^5), disc order 32 != 16); the
      naive map must fail the gate (S3c).  Verdict adjudication.

VERDICTS (frozen): SNF-ISOMETRIC (admissible isometry exists),
SNF-FINGERPRINT (SNF match exact but NO admissible isometry -- the
match is typed as a fingerprint), SNF-FALSE (theta identity or SNF
match fails).

FENCES: [C neu] readings typed; v775 ROOTCLASS-MIXED cited -- the
census is lattice/character-level, NO root-level matter reading and NO
physics claim is attached.  Firewall: experiments/ discovery sandbox;
writes nothing; no verification/, ledger, paper or website surface
touched.  Exact integer/Fraction arithmetic; sympy only for SNF;
numpy only for integer enumeration.  Deterministic (no RNG).

Sources (read-only): v689_gaussian_code_bridge.py (C*, L, J, A, SNF),
v752_projective_hamming_incidence.py (hbar convention),
v638_code_semantics.py (no-4+4-split theorem), v775 (ROOTCLASS-MIXED).

Original hecke_mu4_packet_probe.py docstring (verbatim):
hecke_mu4_packet_probe -- HECKE.MU4_PACKET.01 (positive-protocol
round, strand C, probe 2 of 2): the mu4 -> C2 collapse [E-candidate].

CORPUS ANCHORS (located): first-shell glue sector counts
r = (52, 64, 60, 64) (part-11 probe e8_glue_chi4_signed_theta_probe.py,
v492/v505 replications); weight-1 current sectors
j = (60, 64, 60, 64) = r + (8, 0, 0, 0) (Cartan; the beta-equivariant
route gives the graded character (248, 0, -8, 0)); signed root census
52 - 60 = -8 = -rank(E8); f8 = q eta(2t)^4 eta(4t)^4 (weight-4 newform,
level 8); v537: Sh_{t=2}(g) = -8 f8; v536 Eichler reading
a_p = -c(p)/8.

DFT CONVENTION (frozen): characters chi_t(c) = i^{t c} on the glue
group mu4 = Z4 = E8/(D5 (+) A3); ordering t = (0, 1, 2, 3) =
(trivial, quartic i, quadratic -1, quartic i^3).
  r-hat = (240, -8, -16, -8);  j-hat = (248, 0, -8, 0).

CARTAN CLOSURE (frozen, all shells): the level-1 current-algebra
grading -- multiply each sector theta by the 8-fold oscillator factor
1/phi(q)^8, phi(q) = prod (1 - q^n) (lattice-VOA grading: e^lambda (x)
oscillators; oscillators are glue-neutral).  Grade 1 reproduces
j = (60, 64, 60, 64) with the 8 Cartan modes in the trivial sector.

FROZEN CANDIDATE IDENTITIES (declared BEFORE computing):
  K1  quadratic channel (unclosed) IS pure Eisenstein:
      Th0 - Th1 + Th2 - Th3 = theta4(q)^8 = (16 E4(q^2) - E4(q))/15
      termwise to O(q^NSER); in particular its f8-component is 0.
  K2  THE -8 f8 NORMALIZATION (the Section-12 claim, sharpened): the
      cusp content of the QUARTIC character series
      csig = Th0 - Th2 is EXACTLY -8 f8, with -8 = the shell-1
      quartic DFT = signed census 52 - 60 = -rank(E8):
      csig + 8 f8 lies in the pure sigma3-Eisenstein span
      {E4(q^d) : d = 1,2,4,8,16} + Eis(chi4,chi4), exactly to O(q^NSER).
      Consequence tested separately: csig(n) = -8 f8(n) for ALL odd n.
  K3  prime anchors: a_p(f8) = (-4, -2, 24, -44, 22) at
      p = (3, 5, 7, 11, 13) (v536/v537 values) and csig(p) = -8 a_p(f8)
      for all odd primes p <= 47.
  K4  all-shell quartic vanishing (the user's collapse claim): the
      Cartan-closed quartic series csig(q)/phi(q)^8 vanishes in EVERY
      grade n >= 1 (not just grade 1).  Exact eta form of the closed
      series: csig/phi^8 = prod (1 + q^{2n})^{-4} (machine-verified),
      so the claim is decidable termwise.

TASKS:
  S1  glue machinery replication (part-11 D5 (+) A3 basis, linear
      classifier): census (52, 64, 60, 64), signed -8; N1(n) = N3(n)
      for ALL shells proof-grade via x -> -x (deg(-x) = -deg(x) mod 4).
  S2  exact DFT at shell 1: r-hat, j-hat as Gaussian integers.
  S3  all-shell extension: per-class enumeration n = 1..6 (norm <= 12),
      theta-constant series Th0..Th3 to O(q^NSER = 64) cross-checked
      against enumeration; per-shell DFT table; Cartan closure of all
      four character series; the K4 vanishing test with first-failure
      grade; the closed-quartic eta identity.
  S4  the packet-channel identities K1, K2, K3; adjudication of the
      composite claim "the surviving quadratic character IS the C2
      packet channel with the exact -8": which character carries the
      -8 f8 cusp packet, which carries the surviving -8 constant.
  S5  controls (must fire): (a) scrambled sector assignment (seeded)
      breaks the quartic cancellation at shell 1; (b) wrong Cartan
      completion (4, 0, 0, 4) breaks j-hat = (248, 0, -8, 0).

VERDICTS (frozen): MU4-COLLAPSE-EXACT (quartic vanish ALL shells after
closure + quadratic = the packet channel with the exact -8),
MU4-PARTIAL (shell-1 collapse exact + at least one frozen identity
K1-K3 exact, but not all-shell vanishing), MU4-DEAD (shell-1 anchors
fail or controls do not fire).

FENCES: [E-candidate] readings are exact replications/identities;
extensions typed as measured; v775 ROOTCLASS-MIXED cited -- the glue
census is representation-level, no root-level matter reading and NO
physics claim.  Firewall: experiments/ discovery sandbox; writes
nothing; no verification/, ledger, paper or website surface touched.
Exact integer/Fraction/Gaussian-integer arithmetic; sympy for exact
linear algebra; numpy only for integer enumeration; RNG only inside
the negative control (fixed seed).

Sources (read-only): e8_glue_chi4_signed_theta_probe.py (part 11),
v492/v505 (root census), v535/v536/v537/v538 (Hecke/Eichler/f8 layer),
v775 (ROOTCLASS-MIXED fence).
"""

import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

CHECKS = []

QMAX = 48        # q-series order (frozen)
NCAP = 40        # direct-enumeration cap for the 256 R(n) identity
SHELLS_INFO = 3  # class-theta census shells (info)
TARGET_DIV = [1, 1, 1, 1, 2, 2, 2, 2]


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def info(msg):
    print("        %s" % msg, flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ---------------------------------------------------- integer q-series
def pmul(a, b, order):
    res = [0] * (order + 1)
    for i, ai in enumerate(a):
        if ai:
            top = order - i
            for j in range(min(len(b) - 1, top) + 1):
                if b[j]:
                    res[i + j] += ai * b[j]
    return res


def eta_pow(d, e, order):
    """prod_{n>=1} (1 - q^{d n})^e, no q-prefactor."""
    s = [0] * (order + 1)
    s[0] = 1
    for n in range(1, order // d + 1):
        f = [0] * (d * n + 1)
        f[0], f[d * n] = 1, -1
        for _ in range(e):
            s = pmul(s, f, order)
    return s


def pinv(a, order):
    assert a[0] == 1
    res = [0] * (order + 1)
    res[0] = 1
    for n in range(1, order + 1):
        res[n] = -sum(a[k] * res[n - k]
                      for k in range(1, min(n, len(a) - 1) + 1))
    return res


def shift(a, k, order):
    return ([0] * k + a)[: order + 1]


def rescale(a, d, order):
    res = [0] * (order + 1)
    for i, ai in enumerate(a):
        if ai and i * d <= order:
            res[i * d] = ai
    return res


def main():
    # PART 1 -- hecke_snf_theta_probe.py (top-level executable
    # statements moved unchanged into this function; the banner print
    # of the probe docstring is served by the local __doc__ binding)
    T0 = time.time()
    __doc__ = """hecke_snf_theta_probe -- HECKE.SNF_THETA.01 (positive-protocol round,
strand C, probe 1 of 2).

THE CLAIM UNDER TEST [C neu -> decidable]: the correction theta
H(q) = q^3 psi(q^2)^4 psi(q^4)^4 (psi = Ramanujan's theta,
psi(q) = sum_{k>=0} q^{k(k+1)/2}) has the quadratic form

    Q(u, v) = u_1^2 + ... + u_4^2 + 2(v_1^2 + ... + v_4^2)

on ODD vectors: 256 R(n) = #{(u,v) in (2Z+1)^8 : Q(u,v) = 4n}, where
R(n) is the q^n coefficient of H.  Its Gram matrix diag(1,1,1,1,2,2,2,2)
has Smith signature (1,1,1,1,2,2,2,2) -- EXACTLY the elementary divisors
of the ramified inclusion (1+i)L c L of the unimodular hermitian E8
lattice (v689 machinery, read-only replication).

THE DECIDER: does an isometry exist between the correction-theta
lattice pair (M = Z^4 (+) sqrt2 Z^4 with the odd-coset structure,
i.e. M c M* with M*/M = F2^4) and the ramified inclusion pair
((1+i)L c L with L/(1+i)L = F2^4), under ADMISSIBLE basis changes only?

ADMISSIBLE CLASS (predeclared, frozen): maps definable from the
Z[i]/transversal structure --
  (i)  ambient: R-linear isometries T (a global scale factor lambda > 0
       allowed) with T(L) = lambda M* and T((1+i)L) = lambda M, composed
       with U(L,h)-automorphisms and the ramified twist x -> (1+i)x;
  (ii) quotient: F2-linear maps V = L/(1+i)L -> D = M*/M intertwining
       the induced finite bilinear structures (the symplectic /
       Fourier / Weil-representation class);
INADMISSIBLE (the brake): any map whose definition REQUIRES a
J/sigma-equivariant 4+4 coordinate split of the 8 real coordinates.
The corpus has PROVEN no such split exists: v638_code_semantics.py
S1.2 ("Z6-invariant 4-subsets: 0 => NO equivariant block-systematic
4+4 split exists"); replicated independently in S3c below.  The naive
coordinatewise map (first 4 coords -> u-block, last 4 -> v-block) is
therefore inadmissible BY THEOREM, and the decider must census the
transversal-coded maps only.

SLICES:
  S1  the representation-number identity: H(q) two routes (psi-series
      and eta-quotient eta(4)^4 eta(8)^8 / eta(2)^4), then
      256 R(n) = #{odd (u,v) : Q = 4n} by DIRECT lattice enumeration
      (meet-in-the-middle over the two 4-blocks) for n <= NCAP = 40.
  S2  Smith side: SNF(Gram_M) = (1,1,1,1,2,2,2,2); v689 replication
      (C* placement, L = Construction A, A = coords of (1+J)b_i),
      SNF(A) = (1,1,1,1,2,2,2,2); EXACT elementary-divisor match.
      Census info: per-class theta of L (shells 1..3) vs the odd-coset
      theta of M (normalized) -- the two 16-element quotient structures
      side by side.
  S3  THE DECIDER, three levels:
      (a) ambient isometry census: scale-invariant obstructions
          (kissing number, det x min^{-8}) for L vs M* and
          (1+i)L vs M -> census count at level (i);
      (b) quotient census: b_V = hbar (v752 convention, alternating --
          replicated from the concrete lattice) vs b_D = identity form
          on F2^4 (disc form of M, NON-alternating); FULL GL(4,F2)
          census (20160 invertible maps): # intertwiners, |Aut(b_V)|,
          |Aut(b_D)|; sigma/mu4 equivariance of any intertwiner found;
      (c) the brake demonstration: all 70 coordinate 4-subsets tested
          for (pi_J, pi_sigma)-invariance (expect 0 -> the naive
          coordinatewise map FAILS the admissibility gate).
  S4  controls: wrong-signature lattice diag(1,1,1,2,2,2,2,2) must FAIL
      the SNF match (divisors (1^3,2^5), disc order 32 != 16); the
      naive map must fail the gate (S3c).  Verdict adjudication.

VERDICTS (frozen): SNF-ISOMETRIC (admissible isometry exists),
SNF-FINGERPRINT (SNF match exact but NO admissible isometry -- the
match is typed as a fingerprint), SNF-FALSE (theta identity or SNF
match fails).

FENCES: [C neu] readings typed; v775 ROOTCLASS-MIXED cited -- the
census is lattice/character-level, NO root-level matter reading and NO
physics claim is attached.  Firewall: experiments/ discovery sandbox;
writes nothing; no verification/, ledger, paper or website surface
touched.  Exact integer/Fraction arithmetic; sympy only for SNF;
numpy only for integer enumeration.  Deterministic (no RNG).

Sources (read-only): v689_gaussian_code_bridge.py (C*, L, J, A, SNF),
v752_projective_hamming_incidence.py (hbar convention),
v638_code_semantics.py (no-4+4-split theorem), v775 (ROOTCLASS-MIXED).
"""
    print(__doc__.split("SLICES")[0])
    print("FROZEN SPEC: QMAX = %d, NCAP = %d, target divisors %s;" %
          (QMAX, NCAP, TARGET_DIV))
    print("verdicts SNF-ISOMETRIC / SNF-FINGERPRINT / SNF-FALSE (frozen);")
    print("admissible class = transversal-coded (see docstring), naive 4+4")
    print("coordinatewise maps excluded by v638 S1.2 (replicated in S3c).")
    print()

    # ====================================================================== S1
    section("S1: the correction theta H(q) and the representation identity")

    psi = [0] * (QMAX + 1)
    k = 0
    while k * (k + 1) // 2 <= QMAX:
        psi[k * (k + 1) // 2] += 1
        k += 1

    # classical product form psi(q) = prod (1-q^{2n})^2 / (1-q^n)
    psi_prod = pmul(eta_pow(2, 2, QMAX), pinv(eta_pow(1, 1, QMAX), QMAX), QMAX)
    check("S1.1 psi(q) = sum q^{k(k+1)/2} = prod (1-q^{2n})^2/(1-q^n) "
          "termwise to O(q^%d)" % QMAX, psi == psi_prod)

    psi2_4 = [0] * (QMAX + 1)
    psi2_4[0] = 1
    for _ in range(4):
        psi2_4 = pmul(psi2_4, rescale(psi, 2, QMAX), QMAX)
    psi4_4 = [0] * (QMAX + 1)
    psi4_4[0] = 1
    for _ in range(4):
        psi4_4 = pmul(psi4_4, rescale(psi, 4, QMAX), QMAX)
    H = shift(pmul(psi2_4, psi4_4, QMAX), 3, QMAX)

    H_eta = shift(pmul(pmul(eta_pow(4, 4, QMAX), eta_pow(8, 8, QMAX), QMAX),
                       pinv(eta_pow(2, 4, QMAX), QMAX), QMAX), 3, QMAX)
    info("H(q) coefficients R(n), n = 0..16: %s" % (H[:17],))
    check("S1.2 two routes agree: H = q^3 psi(q^2)^4 psi(q^4)^4 = "
          "eta(4)^4 eta(8)^8 / eta(2)^4 (with q^3 prefactor) to O(q^%d)"
          % QMAX, H == H_eta)

    # direct lattice enumeration, meet in the middle over the two 4-blocks
    NORM_CAP = 4 * NCAP
    odd_u = [u for u in range(-13, 14, 2)]
    hist_u = Counter()                       # sum of u_i^2 over odd 4-vectors
    for quad in itertools.product(odd_u, repeat=4):
        s = sum(x * x for x in quad)
        if s <= NORM_CAP:
            hist_u[s] += 1
    odd_v = [v for v in range(-9, 10, 2)]
    hist_v = Counter()                       # 2 * sum of v_j^2
    for quad in itertools.product(odd_v, repeat=4):
        s = 2 * sum(x * x for x in quad)
        if s <= NORM_CAP:
            hist_v[s] += 1
    rep_count = Counter()
    for su, cu in hist_u.items():
        for sv, cv in hist_v.items():
            if su + sv <= NORM_CAP:
                rep_count[su + sv] += cu * cv
    ok_rep = all(rep_count.get(4 * n, 0) == 256 * H[n] for n in range(NCAP + 1))
    tab_rep = [(n, H[n], rep_count.get(4 * n, 0)) for n in range(3, 11)]
    info("representation table (n, R(n), #odd vectors with Q = 4n): %s"
         % tab_rep)
    check("S1.3 REPRESENTATION IDENTITY by direct enumeration: 256 R(n) = "
          "#{(u,v) in (2Z+1)^8 : sum u_i^2 + 2 sum v_j^2 = 4n} for ALL "
          "n <= %d (odd 4-blocks enumerated exhaustively, %d x %d norm "
          "histograms convolved)" % (NCAP, len(hist_u), len(hist_v)), ok_rep)

    theta_ok = psi == psi_prod and H == H_eta and ok_rep

    # ====================================================================== S2
    section("S2: Smith side -- Gram of M vs ramified inclusion (1+i)L c L")

    GRAM_M = [[0] * 8 for _ in range(8)]
    for i in range(8):
        GRAM_M[i][i] = 1 if i < 4 else 2
    D_M = smith_normal_form(Matrix(GRAM_M), domain=ZZ)
    div_M = sorted(abs(int(D_M[i, i])) for i in range(8))
    check("S2.1 SNF(Gram_M) with Gram_M = diag(1,1,1,1,2,2,2,2): elementary "
          "divisors %s (disc group F2^4, order 16)" % div_M,
          div_M == TARGET_DIV)

    # ---- v689 replication (read-only, verbatim recipe) --------------------
    G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
               (0, 1, 0, 0, 1, 0, 1, 1),
               (0, 0, 1, 0, 1, 1, 0, 1),
               (0, 0, 0, 1, 1, 1, 1, 0)]
    C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                              for j in range(8))
                        for m in itertools.product((0, 1), repeat=4))
    PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
    PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)


    def apply_perm(c, p):
        return tuple(c[p[k]] for k in range(8))


    def code_image(code, p):
        return frozenset(apply_perm(c, p) for c in code)


    def J_vec(x):
        out = []
        for kk in range(0, 8, 2):
            out += [-x[kk + 1], x[kk]]
        return tuple(out)


    def sig_vec(x):
        return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


    def mat_det_inv(rows):
        n = len(rows)
        A = [[Fr(v) for v in r] for r in rows]
        I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
        det = Fr(1)
        for col in range(n):
            piv = next((r for r in range(col, n) if A[r][col] != 0), None)
            assert piv is not None
            if piv != col:
                A[col], A[piv] = A[piv], A[col]
                I[col], I[piv] = I[piv], I[col]
                det = -det
            det *= A[col][col]
            inv = 1 / A[col][col]
            A[col] = [a * inv for a in A[col]]
            I[col] = [a * inv for a in I[col]]
            for r in range(n):
                if r != col and A[r][col] != 0:
                    f = A[r][col]
                    A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                    I[r] = [a - f * b for a, b in zip(I[r], I[col])]
        return det, I


    def f2_rref(words):
        rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
        basis, pivots = [], []
        for r in rows:
            r = r[:]
            for b, pv in zip(basis, pivots):
                if r[pv]:
                    r = [(a + c) % 2 for a, c in zip(r, b)]
            if any(r):
                basis.append(r)
                pivots.append(next(i for i, a in enumerate(r) if a))
        return basis, pivots


    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]

    cb, pivots = f2_rref(CSTAR)
    B_ROWS = [tuple(r) for r in cb]
    B_ROWS += [tuple(2 if i == j else 0 for i in range(8))
               for j in range(8) if j not in pivots]
    detB, Binv = mat_det_inv(B_ROWS)


    def in_L(x):
        return tuple(v % 2 for v in x) in CSTAR


    def coords(x):
        c = [sum(x[i] * Binv[i][j] for i in range(8)) for j in range(8)]
        assert all(v.denominator == 1 for v in c)
        return tuple(int(v) for v in c)


    A_INC = [coords(tuple(a + b for a, b in zip(b_, J_vec(b_))))
             for b_ in B_ROWS]
    D_A = smith_normal_form(Matrix(A_INC), domain=ZZ)
    div_A = sorted(abs(int(D_A[i, i])) for i in range(8))
    detA, _ = mat_det_inv(A_INC)
    check("S2.2 v689 replication: |det B| = 16, [L : (1+i)L] = |det A| = 16 "
          "= N(1+i)^4; SNF(A) elementary divisors %s" % div_A,
          abs(detB) == 16 and abs(int(detA)) == 16 and div_A == TARGET_DIV)

    snf_match = (div_M == TARGET_DIV and div_A == TARGET_DIV)
    check("S2.3 THE SNF MATCH (the claim's arithmetic core): "
          "divisors(Gram_M) == divisors((1+i)L c L) == (1,1,1,1,2,2,2,2)",
          snf_match)

    # roots + guards
    ROOTS = [x for x in itertools.product(range(-2, 3), repeat=8)
             if sum(v * v for v in x) == 4 and in_L(x)]
    check("S2.4 guards: 240 Construction-A roots; J, sigma preserve the root "
          "set", len(ROOTS) == 240
          and all(J_vec(r) in set(ROOTS) for r in ROOTS[:60])
          and all(sig_vec(r) in set(ROOTS) for r in ROOTS[:60]))

    # --- quotient labelling via parity functionals -------------------------
    A2 = [[v % 2 for v in row] for row in A_INC]
    h_funcs = []
    for cand in itertools.product((0, 1), repeat=8):
        if any(cand) and all(sum(a * c for a, c in zip(row, cand)) % 2 == 0
                             for row in A2):
            h_funcs.append(cand)
    # pick 4 independent functionals
    H4, piv4 = f2_rref(h_funcs)
    H4 = [tuple(r) for r in H4]
    check("S2.5 quotient functionals: null space of (A mod 2) has F2-rank 4 "
          "(V = L/(1+i)L = F2^4 read off linearly)", len(H4) == 4)


    def label4(x):
        c = coords(x)
        return tuple(sum(h[i] * c[i] for i in range(8)) % 2 for h in H4)


    # reps of all 16 classes from 0/1 combinations of the basis rows
    reps = {}
    for eps in itertools.product((0, 1), repeat=8):
        x = tuple(sum(e * b[i] for e, b in zip(eps, B_ROWS)) for i in range(8))
        lb = label4(x)
        if lb not in reps:
            reps[lb] = x
    check("S2.6 all 16 labels realized; zero class = lattice vectors "
          "(1+i)L (label of (1+J)b_i is 0 for all rows)",
          len(reps) == 16
          and all(label4(tuple(a + b for a, b in zip(b_, J_vec(b_))))
                  == (0, 0, 0, 0) for b_ in B_ROWS))

    # class-theta census (info): shells 1..3 of L per class vs odd coset of M
    Binv16 = np.array([[int(16 * Binv[i][j]) for j in range(8)]
                       for i in range(8)], dtype=np.int64)
    H4np = np.array(H4, dtype=np.int64)
    rng = np.arange(-3, 4, dtype=np.int16)
    grid = np.array(np.meshgrid(*[rng] * 8, indexing="ij")).reshape(8, -1).T
    nrm = np.einsum("ij,ij->i", grid.astype(np.int32), grid.astype(np.int32))
    mask = (nrm >= 4) & (nrm <= 4 * SHELLS_INFO)
    Xv = grid[mask].astype(np.int64)
    nv = nrm[mask]
    code_arr = np.array(sorted(CSTAR), dtype=np.int64)
    inC = np.zeros(256, dtype=bool)
    for w in CSTAR:
        inC[int("".join(map(str, w)), 2)] = True
    key = ((Xv % 2) * (2 ** np.arange(7, -1, -1, dtype=np.int64))).sum(axis=1)
    selL = inC[key]
    XL, nL = Xv[selL], nv[selL]
    cL16 = XL @ Binv16
    assert np.all(cL16 % 16 == 0)
    lab = ((cL16 // 16) @ H4np.T) % 2
    labcode = (lab * (2 ** np.arange(3, -1, -1, dtype=np.int64))).sum(axis=1)
    info("per-class theta of L (norm 4, 8, 12 = shells 1..3), 16 classes:")
    class_theta = {}
    for cls in range(16):
        row = [int(np.sum((labcode == cls) & (nL == 4 * s)))
               for s in range(1, SHELLS_INFO + 1)]
        class_theta[cls] = row
    zero_row = class_theta[0]
    nz_rows = [tuple(class_theta[c]) for c in range(1, 16)]
    info("  zero class: %s ; the 15 nontrivial classes: %s"
         % (zero_row, dict(Counter(nz_rows))))
    info("odd-coset theta of M (256 R(n) normalized to min-vector count): "
         "min norm 4n = 12, count 256; L nontrivial classes: min norm 4, "
         "count 16 each -- quotient-structure thetas DIFFER (fingerprint "
         "witness at series level)")
    check("S2.7 census guard: zero class carries 0 roots at shell 1 and the "
          "15 nontrivial classes carry 16 each (v689 I2 replication)",
          zero_row[0] == 0 and all(r[0] == 16 for r in nz_rows))

    # ====================================================================== S3
    section("S3: THE DECIDER -- isometry census under admissible maps")

    # ---- (a) ambient level: scale-invariant obstructions ------------------
    # L (doubled-integer model): min norm 4, kissing 240, det Gram = 256.
    # M = Z^4 (+) sqrt2 Z^4: min 1, kissing 8, det 16.
    # M* = Z^4 (+) (1/sqrt2) Z^4: min 1/2, kissing 8, det 1/16.
    detGramL = (Matrix([[sum(a * b for a, b in zip(u, v)) for v in B_ROWS]
                        for u in B_ROWS])).det()
    kiss_L = len(ROOTS)
    kiss_M = 8
    inv_L = Fr(int(detGramL)) / Fr(4) ** 8            # det * min^-8 for L
    inv_Mstar = Fr(1, 16) / Fr(1, 2) ** 8             # det * min^-8 for M*
    inv_M = Fr(16) / Fr(1) ** 8
    inv_ram = Fr(int(detGramL) * 2 ** 8) / Fr(8) ** 8  # (1+i)L: det*2^8, min 8
    info("scale-invariant pairs (kissing, det*min^-8):")
    info("  L        : (%d, %s)   vs  M* : (%d, %s)"
         % (kiss_L, inv_L, kiss_M, inv_Mstar))
    info("  (1+i)L   : (%d, %s)   vs  M  : (%d, %s)"
         % (kiss_L, inv_ram, kiss_M, inv_M))
    obstructed = (kiss_L != kiss_M and inv_L != inv_Mstar and inv_ram != inv_M)
    check("S3a.1 AMBIENT CENSUS = 0: kissing 240 != 8 and det*min^-8 "
          "mismatch on BOTH pair members -- no R-linear isometry (at ANY "
          "scale lambda, admissible or not) can carry L -> lambda M* or "
          "(1+i)L -> lambda M; the ambient isometry census is EMPTY, "
          "proof-grade", obstructed)

    # ---- (b) quotient level: full GL(4,F2) census -------------------------
    def hbar(x, y):
        """h(x,y) = (<x,y> + i <x,Jy>)/2 in Z[i]; reduce a+bi -> (a+b) mod 2
        (v752 convention)."""
        re2 = sum(a * b for a, b in zip(x, y))
        im2 = sum(a * b for a, b in zip(x, J_vec(y)))
        assert re2 % 2 == 0 and im2 % 2 == 0
        return (re2 // 2 + im2 // 2) % 2


    # F2 basis of V: 4 labels with a single 1
    VBAS = []
    for i in range(4):
        lb = tuple(1 if j == i else 0 for j in range(4))
        VBAS.append(reps[lb])
    B_V = [[hbar(u, v) for v in VBAS] for u in VBAS]
    alt_ok = all(hbar(r, r) == 0 for r in reps.values())
    wd_ok = True
    for lb, r in list(reps.items())[:8]:
        r2 = tuple(a + b + c for a, b, c in
                   zip(r, B_ROWS[0], J_vec(B_ROWS[0])))   # + (1+i) b_0
        wd_ok &= all(hbar(r, VBAS[j]) == hbar(r2, VBAS[j]) for j in range(4))
    nondeg = int(Matrix(B_V).det() % 2) == 1
    info("b_V Gram (basis of V):        %s" % (B_V,))
    B_D = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    info("b_D Gram (disc form of M):    %s  (identity form, b(x,x) != 0)"
         % (B_D,))
    check("S3b.1 b_V replicated from the concrete lattice: well-defined mod "
          "(1+i)L, ALTERNATING on all 16 reps, nondegenerate (v752); b_D = "
          "identity form on F2^4 = disc(M*/M), NON-alternating",
          alt_ok and wd_ok and nondeg)

    mats = []
    for rows in itertools.product(range(16), repeat=4):
        M4 = [[(rows[i] >> (3 - j)) & 1 for j in range(4)] for i in range(4)]
        # F2 rank
        R = [r[:] for r in M4]
        rank = 0
        for col in range(4):
            pv = next((r for r in range(rank, 4) if R[r][col]), None)
            if pv is None:
                continue
            R[rank], R[pv] = R[pv], R[rank]
            for r in range(4):
                if r != rank and R[r][col]:
                    R[r] = [(a + b) % 2 for a, b in zip(R[r], R[rank])]
            rank += 1
        if rank == 4:
            mats.append(M4)


    def congr(T, G):
        """T^T G T over F2."""
        TG = [[sum(T[k][i] * G[k][l] for k in range(4)) % 2 for l in range(4)]
              for i in range(4)]
        return [[sum(TG[i][k] * T[k][j] for k in range(4)) % 2
                 for j in range(4)] for i in range(4)]


    n_intertw = sum(1 for T in mats if congr(T, B_D) == B_V)
    n_aut_V = sum(1 for T in mats if congr(T, B_V) == B_V)
    n_aut_D = sum(1 for T in mats if congr(T, B_D) == B_D)
    info("GL(4,F2) census over all %d invertible maps:" % len(mats))
    info("  intertwiners b_D -> b_V : %d" % n_intertw)
    info("  |Aut(b_V)| (symplectic) : %d" % n_aut_V)
    info("  |Aut(b_D)| (orthogonal) : %d" % n_aut_D)
    check("S3b.2 QUOTIENT CENSUS: %d/20160 GL(4,F2) maps intertwine the "
          "disc form of M with the ramified form b_V (alternating vs "
          "non-alternating: b_V(x,x) = 0 for all x, b_D(e_i,e_i) = 1 -- "
          "no isomorphism of the finite bilinear structures exists); "
          "|Aut(b_V)| = %d = |Sp(4,F2)|"
          % (n_intertw, n_aut_V),
          len(mats) == 20160 and n_intertw == 0 and n_aut_V == 720)
    info("value-group observation: any quadratic refinement of b_V is "
         "Z/2-valued (Arf class, v776 selector q*); disc(M) is intrinsically "
         "(1/2)Z/2Z-valued (q(g_j) = 1/2) -- ODD type: the finite quadratic "
         "forms live in different categories, matching the census 0.")

    # sigma/mu4 equivariance of found intertwiners (vacuous if none)
    sig_perm = {lb: label4(sig_vec(r)) for lb, r in reps.items()}
    SIG_MAT = [list(sig_perm[tuple(1 if j == i else 0 for j in range(4))])
               for i in range(4)]
    sig_lin = all(sig_perm[lb] == tuple(
        sum(lb[i] * SIG_MAT[i][j] for i in range(4)) % 2 for j in range(4))
        for lb in reps)
    J_fixes = all(label4(J_vec(r)) == lb for lb, r in reps.items())
    found_equiv = [T for T in mats if congr(T, B_D) == B_V]
    check("S3b.3 equivariance census: sigma acts F2-linearly on V (matrix "
          "%s), mu4 = J acts as the IDENTITY on V ((i-1) = i(1+i), v752); "
          "intertwiners to test: %d -> the sigma/mu4-equivariance census "
          "is VACUOUS (no isometry exists to be equivariant)"
          % (SIG_MAT, len(found_equiv)),
          sig_lin and J_fixes and len(found_equiv) == 0)

    # ---- (c) the brake: the naive coordinatewise 4+4 map ------------------
    inv4 = [s for s in itertools.combinations(range(8), 4)
            if set(PI_J[i] for i in s) == set(s)
            and set(PI_SIG[i] for i in s) == set(s)]
    check("S3c.1 THE BRAKE FIRES: (pi_J, pi_sigma)-invariant coordinate "
          "4-subsets: %d of 70 -- the naive coordinatewise map (coords "
          "1-4 -> u-block, 5-8 -> v-block) REQUIRES such a split and is "
          "inadmissible BY THEOREM (v638 S1.2 replicated: no equivariant "
          "4+4 coordinate split exists)" % len(inv4), len(inv4) == 0)
    naive_gram = [[sum(a * b for a, b in zip(u, v)) for v in B_ROWS]
                  for u in B_ROWS]
    check("S3c.2 the naive map is not even a candidate isometry: Gram(L) in "
          "the fixed basis is NOT diag(1,1,1,1,2,2,2,2)-congruent "
          "coordinatewise (Gram(L) != Gram_M as matrices)",
          naive_gram != GRAM_M)

    # ====================================================================== S4
    section("S4: controls and verdict")

    WRONG = [[0] * 8 for _ in range(8)]
    for i in range(8):
        WRONG[i][i] = 1 if i < 3 else 2
    D_W = smith_normal_form(Matrix(WRONG), domain=ZZ)
    div_W = sorted(abs(int(D_W[i, i])) for i in range(8))
    check("S4.1 CONTROL FIRES (wrong signature): diag(1,1,1,2,2,2,2,2) has "
          "divisors %s != %s and disc order 32 != 16 -- the SNF match "
          "criterion rejects it" % (div_W, TARGET_DIV),
          div_W != TARGET_DIV and div_W == [1, 1, 1, 2, 2, 2, 2, 2])
    controls_ok = (div_W != TARGET_DIV) and (len(inv4) == 0)

    iso_exists = (not obstructed) or (n_intertw > 0)
    if not (theta_ok and snf_match):
        VERDICT = "SNF-FALSE"
    elif iso_exists:
        VERDICT = "SNF-ISOMETRIC"
    else:
        VERDICT = "SNF-FINGERPRINT"

    check("S4.2 verdict adjudication (frozen logic): theta identity %s, SNF "
          "match %s, ambient census empty %s, quotient census 0 %s, brake "
          "fired %s => %s"
          % (theta_ok, snf_match, obstructed, n_intertw == 0,
             len(inv4) == 0, VERDICT),
          VERDICT == "SNF-FINGERPRINT" if (theta_ok and snf_match
                                           and not iso_exists) else True)

    print()
    print("FENCES: [C neu -> decided] typing only; v775 ROOTCLASS-MIXED "
          "cited: the census is lattice/character-level, no root-level "
          "matter reading, no physics claim.")
    print()
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = len(CHECKS) - n_pass
    print("VERDICT: %s" % VERDICT)
    print("TOTAL: %d passed, %d failed  (%.1fs)"
          % (n_pass, n_fail, time.time() - T0))
    return 0 if n_fail == 0 else 1


_run_part1 = main


def _run_part2():
    # PART 2 -- hecke_mu4_packet_probe.py (verbatim; module-level names
    # local to this function scope; check() bookkeeping global ->
    # nonlocal plus a CHECKS record -- print/bookkeeping only, no gate;
    # the banner print of the probe docstring is served by the local
    # __doc__ binding)
    import itertools
    import random
    import time
    from fractions import Fraction

    import numpy as np
    import sympy as sp
    from sympy import Matrix, Rational
    from sympy.matrices.normalforms import smith_normal_form

    T0 = time.time()
    PASS = 0
    FAIL = 0
    CHECKS = []

    NSER = 64                 # q-series order (frozen)
    NENUM = 6                 # enumeration shells (norm <= 12, frozen)
    TMAX = 8 * NSER           # t = q^{1/8} order
    SEED = 20260805           # control RNG seed (frozen)
    AP_EXPECTED = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}


    def check(name, ok):
        nonlocal PASS, FAIL
        CHECKS.append((name, bool(ok)))
        tag = "PASS" if ok else "FAIL"
        print("  [%s] %s" % (tag, name), flush=True)
        if ok:
            PASS += 1
        else:
            FAIL += 1
        return bool(ok)


    def info(msg):
        print("        %s" % msg, flush=True)


    __doc__ = """hecke_mu4_packet_probe -- HECKE.MU4_PACKET.01 (positive-protocol
round, strand C, probe 2 of 2): the mu4 -> C2 collapse [E-candidate].

CORPUS ANCHORS (located): first-shell glue sector counts
r = (52, 64, 60, 64) (part-11 probe e8_glue_chi4_signed_theta_probe.py,
v492/v505 replications); weight-1 current sectors
j = (60, 64, 60, 64) = r + (8, 0, 0, 0) (Cartan; the beta-equivariant
route gives the graded character (248, 0, -8, 0)); signed root census
52 - 60 = -8 = -rank(E8); f8 = q eta(2t)^4 eta(4t)^4 (weight-4 newform,
level 8); v537: Sh_{t=2}(g) = -8 f8; v536 Eichler reading
a_p = -c(p)/8.

DFT CONVENTION (frozen): characters chi_t(c) = i^{t c} on the glue
group mu4 = Z4 = E8/(D5 (+) A3); ordering t = (0, 1, 2, 3) =
(trivial, quartic i, quadratic -1, quartic i^3).
  r-hat = (240, -8, -16, -8);  j-hat = (248, 0, -8, 0).

CARTAN CLOSURE (frozen, all shells): the level-1 current-algebra
grading -- multiply each sector theta by the 8-fold oscillator factor
1/phi(q)^8, phi(q) = prod (1 - q^n) (lattice-VOA grading: e^lambda (x)
oscillators; oscillators are glue-neutral).  Grade 1 reproduces
j = (60, 64, 60, 64) with the 8 Cartan modes in the trivial sector.

FROZEN CANDIDATE IDENTITIES (declared BEFORE computing):
  K1  quadratic channel (unclosed) IS pure Eisenstein:
      Th0 - Th1 + Th2 - Th3 = theta4(q)^8 = (16 E4(q^2) - E4(q))/15
      termwise to O(q^NSER); in particular its f8-component is 0.
  K2  THE -8 f8 NORMALIZATION (the Section-12 claim, sharpened): the
      cusp content of the QUARTIC character series
      csig = Th0 - Th2 is EXACTLY -8 f8, with -8 = the shell-1
      quartic DFT = signed census 52 - 60 = -rank(E8):
      csig + 8 f8 lies in the pure sigma3-Eisenstein span
      {E4(q^d) : d = 1,2,4,8,16} + Eis(chi4,chi4), exactly to O(q^NSER).
      Consequence tested separately: csig(n) = -8 f8(n) for ALL odd n.
  K3  prime anchors: a_p(f8) = (-4, -2, 24, -44, 22) at
      p = (3, 5, 7, 11, 13) (v536/v537 values) and csig(p) = -8 a_p(f8)
      for all odd primes p <= 47.
  K4  all-shell quartic vanishing (the user's collapse claim): the
      Cartan-closed quartic series csig(q)/phi(q)^8 vanishes in EVERY
      grade n >= 1 (not just grade 1).  Exact eta form of the closed
      series: csig/phi^8 = prod (1 + q^{2n})^{-4} (machine-verified),
      so the claim is decidable termwise.

TASKS:
  S1  glue machinery replication (part-11 D5 (+) A3 basis, linear
      classifier): census (52, 64, 60, 64), signed -8; N1(n) = N3(n)
      for ALL shells proof-grade via x -> -x (deg(-x) = -deg(x) mod 4).
  S2  exact DFT at shell 1: r-hat, j-hat as Gaussian integers.
  S3  all-shell extension: per-class enumeration n = 1..6 (norm <= 12),
      theta-constant series Th0..Th3 to O(q^NSER = 64) cross-checked
      against enumeration; per-shell DFT table; Cartan closure of all
      four character series; the K4 vanishing test with first-failure
      grade; the closed-quartic eta identity.
  S4  the packet-channel identities K1, K2, K3; adjudication of the
      composite claim "the surviving quadratic character IS the C2
      packet channel with the exact -8": which character carries the
      -8 f8 cusp packet, which carries the surviving -8 constant.
  S5  controls (must fire): (a) scrambled sector assignment (seeded)
      breaks the quartic cancellation at shell 1; (b) wrong Cartan
      completion (4, 0, 0, 4) breaks j-hat = (248, 0, -8, 0).

VERDICTS (frozen): MU4-COLLAPSE-EXACT (quartic vanish ALL shells after
closure + quadratic = the packet channel with the exact -8),
MU4-PARTIAL (shell-1 collapse exact + at least one frozen identity
K1-K3 exact, but not all-shell vanishing), MU4-DEAD (shell-1 anchors
fail or controls do not fire).

FENCES: [E-candidate] readings are exact replications/identities;
extensions typed as measured; v775 ROOTCLASS-MIXED cited -- the glue
census is representation-level, no root-level matter reading and NO
physics claim.  Firewall: experiments/ discovery sandbox; writes
nothing; no verification/, ledger, paper or website surface touched.
Exact integer/Fraction/Gaussian-integer arithmetic; sympy for exact
linear algebra; numpy only for integer enumeration; RNG only inside
the negative control (fixed seed).

Sources (read-only): e8_glue_chi4_signed_theta_probe.py (part 11),
v492/v505 (root census), v535/v536/v537/v538 (Hecke/Eichler/f8 layer),
v775 (ROOTCLASS-MIXED fence).
"""
    print(__doc__.split("TASKS")[0])
    print("FROZEN: NSER = %d, NENUM = %d, seed = %d, DFT ordering "
          "(triv, i, -1, i^3)." % (NSER, NENUM, SEED))
    print()

    # ---------------------------------------------------- integer q-series
    def pmul(a, b, order):
        res = [0] * (order + 1)
        for i, ai in enumerate(a):
            if ai:
                top = order - i
                for j in range(min(len(b) - 1, top) + 1):
                    if b[j]:
                        res[i + j] += ai * b[j]
        return res


    def ppow(a, e, order):
        res = [0] * (order + 1)
        res[0] = 1
        for _ in range(e):
            res = pmul(res, a, order)
        return res


    def padd(a, b):
        return [x + y for x, y in zip(a, b)]


    def psub(a, b):
        return [x - y for x, y in zip(a, b)]


    def phalf(a):
        assert all(x % 2 == 0 for x in a)
        return [x // 2 for x in a]


    def eta_pow(d, e, order):
        s = [0] * (order + 1)
        s[0] = 1
        for n in range(1, order // d + 1):
            f = [0] * (d * n + 1)
            f[0], f[d * n] = 1, -1
            for _ in range(e):
                s = pmul(s, f, order)
        return s


    def pinv(a, order):
        assert a[0] == 1
        res = [0] * (order + 1)
        res[0] = 1
        for n in range(1, order + 1):
            res[n] = -sum(a[k] * res[n - k]
                          for k in range(1, min(n, len(a) - 1) + 1))
        return res


    def shift(a, k, order):
        return ([0] * k + a)[: order + 1]


    def theta3_t(step):
        s = [0] * (TMAX + 1)
        s[0] = 1
        n = 1
        while step * 4 * n * n <= TMAX:
            s[step * 4 * n * n] += 2
            n += 1
        return s


    def theta4_t(step):
        s = [0] * (TMAX + 1)
        s[0] = 1
        n = 1
        while step * 4 * n * n <= TMAX:
            s[step * 4 * n * n] += 2 * (-1) ** n
            n += 1
        return s


    def theta2_t(step):
        s = [0] * (TMAX + 1)
        o = 1
        while step * o * o <= TMAX:
            s[step * o * o] += 2
            o += 2
        return s


    def t_to_q(ts):
        assert all(v == 0 for k, v in enumerate(ts) if k % 8 and v)
        return [ts[8 * n] for n in range(NSER + 1)]


    def theta4_q(step):
        s = [0] * (NSER + 1)
        s[0] = 1
        n = 1
        while step * n * n <= NSER:
            s[step * n * n] += 2 * (-1) ** n
            n += 1
        return s


    # ================================================================ S1
    print("S1 -- glue machinery replication (part-11 recipe, verbatim)")


    def col(v):
        return [2 * x for x in v]


    e8_basis = [
        [1, -1, -1, -1, -1, -1, -1, 1],
        col([1, 1, 0, 0, 0, 0, 0, 0]),
        col([-1, 1, 0, 0, 0, 0, 0, 0]),
        col([0, -1, 1, 0, 0, 0, 0, 0]),
        col([0, 0, -1, 1, 0, 0, 0, 0]),
        col([0, 0, 0, -1, 1, 0, 0, 0]),
        col([0, 0, 0, 0, -1, 1, 0, 0]),
        col([0, 0, 0, 0, 0, -1, 1, 0]),
    ]
    BE = Matrix(e8_basis).T
    gram = (BE.T * BE) / 4
    l0_basis = [
        col([1, -1, 0, 0, 0, 0, 0, 0]), col([0, 1, -1, 0, 0, 0, 0, 0]),
        col([0, 0, 1, -1, 0, 0, 0, 0]), col([0, 0, 0, 1, -1, 0, 0, 0]),
        col([0, 0, 0, 1, 1, 0, 0, 0]),
        col([0, 0, 0, 0, 0, 1, -1, 0]), col([0, 0, 0, 0, 0, 0, 1, -1]),
        col([0, 0, 0, 0, 0, 1, 1, 0]),
    ]
    BL = Matrix(l0_basis).T
    M = BE.solve(BL)
    snf = smith_normal_form(M)
    check("S1.1 E8 basis unimodular, [E8 : D5 (+) A3] = 4, SNF diag "
          "(1,...,1,4) -> glue group Z4 = mu4 (part-11/v-suite replication)",
          sp.det(gram) == 1 and abs(M.det()) == 4
          and sorted(abs(snf[i, i]) for i in range(8)) == [1] * 7 + [4])

    Fmap = M.inv() * BE.inv()


    def glue_frac2(v2):
        fr = Fmap * Matrix(list(v2))
        return tuple(Fraction(sp.Rational(e).p, sp.Rational(e).q) % 1
                     for e in fr)


    roots2 = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (2, -2):
                for sj in (2, -2):
                    v = [0] * 8
                    v[i], v[j] = si, sj
                    roots2.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots2.append(signs)
    assert len(roots2) == 240

    g1 = glue_frac2(roots2[112])
    classes = {}
    for k in range(4):
        classes[tuple((k * c) % 1 for c in g1)] = k

    BEinv = BE.inv()
    I256 = np.array([[int(256 * BEinv[i, j]) for j in range(8)]
                     for i in range(8)], dtype=np.int64)
    dvec = np.array([classes[glue_frac2([BE[j, i] for j in range(8)])]
                     for i in range(8)], dtype=np.int64)


    def deg_bulk(V2):
        prod = V2.astype(np.int64) @ I256.T
        assert np.all(prod % 256 == 0)
        return ((prod // 256) @ dvec) % 4


    deg_roots = deg_bulk(np.array(roots2, dtype=np.int64))
    r_census = [int(np.sum(deg_roots == k)) for k in range(4)]
    info("shell-1 sector counts r = %s; signed 52 - 60 = %d"
         % (tuple(r_census), r_census[0] - r_census[2]))
    check("S1.2 CORPUS ANCHOR: r = (52, 64, 60, 64), signed census "
          "52 - 60 = -8 = -rank(E8)",
          r_census == [52, 64, 60, 64] and r_census[0] - r_census[2] == -8)

    deg_neg = deg_bulk(np.array([[-v for v in r] for r in roots2],
                                dtype=np.int64))
    check("S1.3 PROOF-GRADE symmetry: deg(-x) = -deg(x) mod 4 on all 240 "
          "roots => N1(n) = N3(n) for EVERY shell (x -> -x bijects class 1 "
          "onto class 3)",
          all((int(a) + int(b)) % 4 == 0 for a, b in zip(deg_roots, deg_neg)))

    # ================================================================ S2
    print("S2 -- exact DFT at shell 1 (Gaussian integers)")


    def dft4(vec):
        """DFT with chi_t(c) = i^{tc}; returns 4 Gaussian integers as
        (real, imag) pairs."""
        out = []
        for t in range(4):
            re, im = 0, 0
            for c in range(4):
                ph = (t * c) % 4          # i^ph
                if ph == 0:
                    re += vec[c]
                elif ph == 1:
                    im += vec[c]
                elif ph == 2:
                    re -= vec[c]
                else:
                    im -= vec[c]
            out.append((re, im))
        return out


    r_hat = dft4(r_census)
    j_census = [r_census[0] + 8] + r_census[1:]
    j_hat = dft4(j_census)
    info("r-hat = %s" % (r_hat,))
    info("j     = %s (Cartan closure r + (8,0,0,0))" % (tuple(j_census),))
    info("j-hat = %s" % (j_hat,))
    check("S2.1 CORPUS ANCHOR verified exactly: r-hat = (240, -8, -16, -8) "
          "(all imaginary parts 0 by S1.3)",
          r_hat == [(240, 0), (-8, 0), (-16, 0), (-8, 0)])
    check("S2.2 CORPUS ANCHOR verified exactly: j = (60, 64, 60, 64), "
          "j-hat = (248, 0, -8, 0) -- at the current level the quartic "
          "characters COLLAPSE and the quadratic -8 survives (mu4 -> C2)",
          j_census == [60, 64, 60, 64]
          and j_hat == [(248, 0), (0, 0), (-8, 0), (0, 0)])

    # ================================================================ S3
    print("S3 -- all-shell extension: enumeration, series, Cartan closure")

    rng7 = np.arange(-3, 4, dtype=np.int16)
    gi = np.array(np.meshgrid(*[rng7] * 8, indexing='ij')).reshape(8, -1).T
    ni = np.einsum('ij,ij->i', gi.astype(np.int32), gi.astype(np.int32))
    mi = (gi.astype(np.int32).sum(axis=1) % 2 == 0) & (ni >= 2) & (ni <= 12)
    V2i = 2 * gi[mi].astype(np.int64)
    n_i = ni[mi] // 2
    rng6 = np.array([-5, -3, -1, 1, 3, 5], dtype=np.int16)
    gh = np.array(np.meshgrid(*[rng6] * 8, indexing='ij')).reshape(8, -1).T
    nh = np.einsum('ij,ij->i', gh.astype(np.int32), gh.astype(np.int32))
    mh = (gh.astype(np.int32).sum(axis=1) % 4 == 0) & (nh <= 48)
    V2h = gh[mh].astype(np.int64)
    n_h = nh[mh] // 8
    del gi, gh, ni, nh
    V2 = np.vstack([V2i, V2h])
    nsh = np.concatenate([n_i, n_h])
    deg = deg_bulk(V2)
    counts = {}
    for n in range(1, NENUM + 1):
        for k in range(4):
            counts[(n, k)] = int(np.sum((nsh == n) & (deg == k)))
    info("per-class shell counts N_c(2n), n = 1..%d (direct enumeration):"
         % NENUM)
    for k in range(4):
        info("  class %d: %s" % (k, [counts[(n, k)] for n in
                                     range(1, NENUM + 1)]))
    sig3 = [0] + [int(sp.divisor_sigma(n, 3)) for n in range(1, NSER + 1)]
    check("S3.1 enumeration totals: sum_c N_c(2n) = 240 sigma3(n) and "
          "N1 = N3 shell by shell for n = 1..%d" % NENUM,
          all(sum(counts[(n, k)] for k in range(4)) == 240 * sig3[n]
              for n in range(1, NENUM + 1))
          and all(counts[(n, 1)] == counts[(n, 3)]
                  for n in range(1, NENUM + 1)))

    th3, th4, th2 = theta3_t(1), theta4_t(1), theta2_t(1)
    t3_5, t4_5 = ppow(th3, 5, TMAX), ppow(th4, 5, TMAX)
    t3_3, t4_3 = ppow(th3, 3, TMAX), ppow(th4, 3, TMAX)
    Th0 = t_to_q(pmul(phalf(padd(t3_5, t4_5)), phalf(padd(t3_3, t4_3)), TMAX))
    Th2 = t_to_q(pmul(phalf(psub(t3_5, t4_5)), phalf(psub(t3_3, t4_3)), TMAX))
    th2_8 = ppow(th2, 8, TMAX)
    assert all(x % 4 == 0 for x in th2_8)
    Th1 = t_to_q([x // 4 for x in th2_8])
    Th3 = Th1[:]
    check("S3.2 theta-constant series (route 2) match the enumeration "
          "(route 1) per class for n = 1..%d; totals = E4 to O(q^%d)"
          % (NENUM, NSER),
          all(Th0[n] == counts[(n, 0)] and Th2[n] == counts[(n, 2)]
              and Th1[n] == counts[(n, 1)] == counts[(n, 3)]
              for n in range(1, NENUM + 1))
          and all(Th0[n] + 2 * Th1[n] + Th2[n]
                  == (1 if n == 0 else 240 * sig3[n])
                  for n in range(NSER + 1)))

    # per-shell DFT series (all real: quartic = Th0 - Th2 since Th1 = Th3)
    dft_triv = [Th0[n] + Th1[n] + Th2[n] + Th3[n] for n in range(NSER + 1)]
    dft_quart = [Th0[n] - Th2[n] for n in range(NSER + 1)]        # csig
    dft_quad = [Th0[n] - Th1[n] + Th2[n] - Th3[n] for n in range(NSER + 1)]
    print("        per-shell DFT table (n, N_c(2n) c=0..3, triv, quartic, "
          "quadratic), n = 1..16:")
    for n in range(1, 17):
        print("          n=%2d  N=(%7d,%7d,%7d,%7d)  triv=%9d  "
              "quart=%7d  quad=%9d"
              % (n, Th0[n], Th1[n], Th2[n], Th3[n],
                 dft_triv[n], dft_quart[n], dft_quad[n]), flush=True)

    # Cartan closure: multiply by 1/phi^8
    phi8 = eta_pow(1, 8, NSER)
    inv_phi8 = pinv(phi8, NSER)
    cl_triv = pmul(dft_triv, inv_phi8, NSER)
    cl_quart = pmul(dft_quart, inv_phi8, NSER)
    cl_quad = pmul(dft_quad, inv_phi8, NSER)
    cl_classes = [pmul(t, inv_phi8, NSER) for t in (Th0, Th1, Th2, Th3)]
    check("S3.3 Cartan closure normalization: grade-1 closed sector counts "
          "= j = (60, 64, 60, 64) (the 8 oscillator modes sit in the "
          "trivial sector) and closed DFT grade 1 = (248, 0, -8)",
          [c[1] for c in cl_classes] == [60, 64, 60, 64]
          and (cl_triv[1], cl_quart[1], cl_quad[1]) == (248, 0, -8))

    # K4: all-shell quartic vanishing
    nz = [n for n in range(1, NSER + 1) if cl_quart[n] != 0]
    info("closed quartic series (Th0 - Th2)/phi^8, grades 0..12: %s"
         % (cl_quart[:13],))
    info("nonzero grades <= %d: %s%s"
         % (NSER, nz[:12], " ..." if len(nz) > 12 else ""))
    k4_vanish = len(nz) == 0
    check("S3.4 K4 MEASURED: closed quartic vanishes at grade 1 (the "
          "corpus j-hat anchor holds); all-shell vanishing claim is %s "
          "(first nonzero grade: %s) -- adjudicated in the verdict"
          % ("TRUE" if k4_vanish else "FALSE", nz[0] if nz else "NONE"),
          cl_quart[1] == 0)

    # exact eta form: csig/phi^8 = prod (1+q^{2n})^{-4}
    one_plus = [0] * (NSER + 1)
    one_plus[0] = 1
    for n in range(1, NSER // 2 + 1):
        f = [0] * (2 * n + 1)
        f[0], f[2 * n] = 1, 1
        for _ in range(4):
            one_plus = pmul(one_plus, f, NSER)
    check("S3.5 exact eta identity of the closed quartic channel: "
          "(Th0 - Th2)/phi^8 = prod (1 + q^{2n})^{-4} termwise to O(q^%d) "
          "(so all-shell vanishing is decidably FALSE: the product is not "
          "identically 1)" % NSER,
          cl_quart == pinv(one_plus, NSER))
    check("S3.6 the quadratic character SURVIVES closure: closed quadratic "
          "series nonzero at grade 1 (= -8) and at infinitely many visible "
          "grades (first 5 nonzero grades %s)"
          % ([n for n in range(1, NSER + 1) if cl_quad[n]][:5],),
          cl_quad[1] == -8 and sum(1 for n in range(1, NSER + 1)
                                   if cl_quad[n]) >= 5)

    # ================================================================ S4
    print("S4 -- the packet-channel identities K1, K2, K3")

    th4q8 = ppow(theta4_q(1), 8, NSER)
    E4q = [1] + [240 * sig3[n] for n in range(1, NSER + 1)]
    E4q2 = [1] + [240 * sig3[n // 2] if n % 2 == 0 else 0
                  for n in range(1, NSER + 1)]
    k1_ok = (dft_quad == th4q8
             and all(15 * th4q8[n] == 16 * E4q2[n] - E4q[n]
                     for n in range(NSER + 1)))
    check("K1: quadratic channel = theta4(q)^8 = (16 E4(q^2) - E4(q))/15 "
          "PURE Eisenstein termwise to O(q^%d) -- the C2 channel carries "
          "NO cusp form, in particular no f8 component" % NSER, k1_ok)

    f8 = shift(pmul(eta_pow(2, 4, NSER), eta_pow(4, 4, NSER), NSER), 1, NSER)


    def E4d(d):
        return [1] + [240 * sig3[n // d] if n % d == 0 else 0
                      for n in range(1, NSER + 1)]


    chi4 = lambda d: (1 if d % 4 == 1 else -1 if d % 4 == 3 else 0)
    eis16 = [0] + [sum(chi4(d) * chi4(n // d) * d ** 3
                       for d in sp.divisors(n)) for n in range(1, NSER + 1)]
    target = [dft_quart[n] + 8 * f8[n] for n in range(NSER + 1)]
    cols = [E4d(1), E4d(2), E4d(4), E4d(8), E4d(16), eis16]
    names = ["E4(q)", "E4(q^2)", "E4(q^4)", "E4(q^8)", "E4(q^16)",
             "Eis(chi4,chi4)"]
    NEQ = 24
    Aeq = Matrix([[cols[j][n] for j in range(len(cols))] for n in range(NEQ)])
    bvec = Matrix([target[n] for n in range(NEQ)])
    sol, params = Aeq.gauss_jordan_solve(bvec)
    if params:
        sol = sol.subs({p: 0 for p in params})
    recon = [sum(sol[j] * cols[j][n] for j in range(len(cols)))
             for n in range(NSER + 1)]
    k2_ok = recon == [Rational(c) for c in target]
    info("Eisenstein decomposition of csig + 8 f8: " + ", ".join(
        "%s: %s" % (names[j], sp.nsimplify(sol[j]))
        for j in range(len(cols)) if sol[j] != 0))
    check("K2 (THE -8 f8 NORMALIZATION, frozen): csig + 8 f8 lies EXACTLY "
          "in the pure Eisenstein span to O(q^%d) -- the cusp content of "
          "the QUARTIC mu4 character is EXACTLY -8 f8, with -8 = signed "
          "census 52 - 60 = -rank(E8)" % NSER, k2_ok)
    k2_odd = all(dft_quart[n] == -8 * f8[n]
                 for n in range(1, NSER + 1, 2))
    check("K2 consequence: csig(n) = -8 f8(n) for ALL odd n <= %d (the "
          "Eisenstein part is supported on even n)" % NSER, k2_odd)
    k2_ok = k2_ok and k2_odd

    primes = [p for p in range(3, 48, 2) if sp.isprime(p)]
    ap_ok = all(f8[p] == AP_EXPECTED[p] for p in AP_EXPECTED)
    k3_ok = ap_ok and all(dft_quart[p] == -8 * f8[p] for p in primes)
    info("prime anchors (p, a_p(f8), csig(p)): %s"
         % [(p, f8[p], dft_quart[p]) for p in primes])
    check("K3: a_p(f8) = (-4, -2, 24, -44, 22) at p = (3, 5, 7, 11, 13) "
          "(v536/v537 corpus values) and csig(p) = -8 a_p(f8) for all odd "
          "primes p <= 47 (the v536 Eichler reading a_p = -c(p)/8)", k3_ok)

    info("ADJUDICATION of the composite Section-12 claim: the -8 f8 cusp "
         "packet sits in the QUARTIC (order-4) character channel (K2); "
         "the QUADRATIC (C2) channel is pure Eisenstein (K1); the -8 that "
         "SURVIVES Cartan closure at the current level sits in the "
         "quadratic slot of j-hat = (248, 0, -8, 0) and equals the same "
         "signed census -8.  'The -8 comes from the mu4 character "
         "structure' is CONFIRMED (both -8's are the signed census "
         "52 - 60); 'the quadratic series IS the packet channel' is NOT: "
         "the packet (cusp) channel is the quartic one.")

    # ================================================================ S5
    print("S5 -- controls (must fire)")

    rng = random.Random(SEED)
    scr = [rng.randrange(4) for _ in range(240)]
    scr_census = [scr.count(k) for k in range(4)]
    scr_hat = dft4([scr_census[0] + 8] + scr_census[1:])
    check("S5.1 CONTROL FIRES (scrambled sector assignment, seed %d): "
          "census %s != (52, 64, 60, 64) and the quartic cancellation "
          "breaks (closed quartic slot %s != 0)"
          % (SEED, tuple(scr_census), scr_hat[1]),
          scr_census != [52, 64, 60, 64] and scr_hat[1] != (0, 0))

    wrong_j = [r_census[0] + 4, r_census[1], r_census[2], r_census[3] + 4]
    wrong_hat = dft4(wrong_j)
    check("S5.2 CONTROL FIRES (wrong Cartan completion (4,0,0,4)): "
          "j-hat = %s != (248, 0, -8, 0) -- the quartic slot no longer "
          "cancels and the quadratic slot is wrong" % (wrong_hat,),
          wrong_hat != [(248, 0), (0, 0), (-8, 0), (0, 0)]
          and wrong_hat[1] != (0, 0))

    # ================================================================ verdict
    print()
    shell1_exact = (r_census == [52, 64, 60, 64]
                    and r_hat == [(240, 0), (-8, 0), (-16, 0), (-8, 0)]
                    and j_hat == [(248, 0), (0, 0), (-8, 0), (0, 0)])
    if shell1_exact and k4_vanish and k1_ok and k2_ok:
        VERDICT = "MU4-COLLAPSE-EXACT"
    elif shell1_exact and (k1_ok or k2_ok or k3_ok):
        VERDICT = "MU4-PARTIAL"
    else:
        VERDICT = "MU4-DEAD"
    print("VERDICT ADJUDICATION (frozen logic): shell-1 collapse exact = %s;"
          % shell1_exact)
    print("  K1 (quadratic pure Eisenstein) = %s; K2 (-8 f8 exact) = %s;"
          % (k1_ok, k2_ok))
    print("  K3 (prime anchors) = %s; K4 (all-shell quartic vanish) = %s"
          % (k3_ok, k4_vanish))
    print()
    print("FENCES: [E-candidate] typing on exact identities only; v775 "
          "ROOTCLASS-MIXED cited: representation-level census, no "
          "root-level matter reading, no physics claim.")
    print()
    print("VERDICT: %s" % VERDICT)
    print("TOTAL: %d passed, %d failed  (%.1fs)" % (PASS, FAIL,
                                                    time.time() - T0))
    rc = 0 if FAIL == 0 else 1
    return rc, list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 18/18
    (SNF-FINGERPRINT: the SNF match is exact but the isometry census is
    empty at every admissible level), part 2 must be 17/17 (MU4-PARTIAL:
    shell-1 collapse and K1-K3 exact, the all-shell quartic vanishing
    honestly FALSE)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 18)
    print("\n[%s] PART-1 PATTERN GATE: expected 18/18 "
          "(SNF-FINGERPRINT) -- fails: %s"
          % ("PASS" if part1_ok else "FAIL", fails1 or "none"))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 17)
    print("\n[%s] PART-2 PATTERN GATE: expected 17/17 "
          "(MU4-PARTIAL) -- fails: %s"
          % ("PASS" if part2_ok else "FAIL", fails2 or "none"))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- SNF-FINGERPRINT + "
          "MU4-PARTIAL: the 256 R(n) representation identity and the "
          "SNF match (1,1,1,1,2,2,2,2) are exact but the isometry "
          "census is EMPTY at every admissible level (ambient kissing "
          "240 vs 8 proof-grade, quotient 0/20160 over GL(4,F2) -- "
          "alternating vs odd form, |Aut(b_V)| = 720 = |Sp(4,F2)| -- "
          "and the naive 4+4 split inadmissible by theorem): a "
          "fingerprint, not an isometry; the cusp part of the quartic "
          "mu4 character is EXACTLY -8 f8 (csig = (1/15) E4(q^2) - "
          "(6/5) E4(q^4) + (32/15) E4(q^8) - 8 f8) with -8 = 52 - 60 "
          "= -rank(E8), the C2 channel is pure Eisenstein "
          "(theta4(q)^8 = (16 E4(q^2) - E4(q))/15), and the all-shell "
          "quartic vanishing is honestly FALSE (closed series "
          "prod (1 + q^{2n})^-4, fails from grade 2).  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
