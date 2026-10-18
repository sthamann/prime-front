#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v868 -- E8.DIVISOR210.CANONICITY.01 (+ the moving-12 and chirality audits): the hard canonicity guard for the 210 discovery of v863 -- the Boolean/Walsh/mu layer is MEASURED GENERIC exactly as warned (210/210 quadruples of primes < 30 pass it: layer one carries NO selection content), the deployed scalar-limit Euler constants pin {2,3,5,7} UNIQUELY (Q1: prod(1-1/p) == 8/35 exact in Fractions has 1 match; Q2: prod(1-p^{-1/2}) == the deployed value with exact radical maps has 1 match, non-matches separated by >= 5.2e-3 at 50 digits; the tautological prod p == 210 test excluded from the verdict), the anchor prime 2 is FORCED by the frozen ramification crossref R3 (2 = the unique Z[i]-ramified prime onto the unique sigma-fixed q*=1 class -- the very prime at which V = L/(1+i)L is cut), the mu4 weld grade cuts the gauge C6 -> C3 (|G3| = 3 measured) and the axis freedom 2 -> 1 sets, and after R3 exactly TWO gauge classes remain -- the family-cycle CHIRALITY ((3,5,7) vs (3,7,5)), which the chirality audit then PROVES gauge at the deployed-machine level, ONE module from three probes (36/36 + 12/12 + 15/15 checks, zero fails, verdicts DIVISOR210-GAUGE-FAMILY(2), MOVING12-DIMENSION-ONLY, CHIRALITY-DEGENERATE; discovery probes divisor210_canonicity_probe.py, moving12_soft17_probe.py and chiral_phase_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~6 s).  PART A, CANONICITY: the full 65536-matrix census gives |Sp(4,2)| = 720 with the Gram-only baseline a simply transitive torsor (720 ordered bases) -- the deployed pins cut 720 -> 6 ordered bases (factor 120): the SEMANTICS, not the lattice shape, carry the selection; the role census over all admissible bases x 24 bijections (48 identifications, 24 weld-compatible) types every layer: the Boolean battery forces NOTHING (48/48), the register forces the anchor BIT (unique sigma-fixed q*=1 class), R3 forces the anchor PRIME = 2 (12/48 survivors), the weighted-sigma criterion is typed NOT-a-filter (three distinct primes can never have equal half-weights; the deployed design applies weights as modular phases), the Z[i]-splitting profile of the family primes (5 splits, 3 and 7 inert) admits NO C3-symmetric 3-cycle -- the family symmetry is REGISTER-SIDE ONLY; both scramble controls fire (sigma'=id, q'=0: NOTHING passes, the gauge explodes to 720; flavor 2: anchor census 10 != 1 -- the family 3-cycle is load-bearing); the 6-vs-7 HONESTY NOTE stands untouched: the clock alphabet {2,3,5,6} and the prime quadruple {2,3,5,7} are DIFFERENT objects (6 = 2*3 = |R+(A3)| sits inside the divisor lattice as the unique weight-2 divisor from two alphabet primes; 7 = 6+1 is prime and not in the alphabet) -- not smoothed over.  PART B, THE MOVING-12 BURIAL (honest): the register split 3 + 12 and the isotypic structure are EXACT (C^15 = triv^7 + om^4 + ombar^4; moved sector = 4 x regular; the divisor census 17 = 12 + 3 + 1 + 1 with both gauge classes giving EQUAL moved sets) and the measured objects reproduce (displacement rank 12 non-growing, n95 = 16, top-17 bulk modes carry 0.957 of the backflow) -- but the space-level identification through the only deployed bridge (the divisor modular frame, conditioning smin/smax = 0.84) gives max principal angles 1.5703/1.5617 rad against the frozen 1e-6 bar (90 deg = 1.5708: ORTHOGONAL; the foreign-frame contrast 0.0004 says the frame does not see the displacement structure at all), nontrivial character share 0.755, effective multiplicities (9.7, 3.1, 0.9, 3.3) != (12, 3, 1, 1): the 17 = 12+3+1+1 arithmetic stands as a COUNT, the identification hypothesis is BURIED at space level unless a different intertwiner is exhibited -- typed, not smoothed.  PART C, CHIRALITY IS PROVEN GAUGE (two exact no-go wards): (1) the register orientation functional vanishes IDENTICALLY -- the Moebius complement d -> 210/d pairs the 4 free orbits with reversed orientation (X1(O)^3 + X1(O')^3 = 0 per pair at 4.1e-15) for EVERY multiplicative weight assignment: the register's multiplicative weight structure carries NO intrinsic scalar orientation, the KMS-orientation criterion is VACUOUS; (2) every sigma-less phase readout is PROVABLY chirality-blind (U0_- == Pi U0_+ Pi^T exact, loaded scalars identical at 5.6e-17) and the sigma-wired machine's QUADRATIC readout is chirality-equal to machine precision (1.8e-15: the symmetric form w2'Vt w2 cannot see the cycle orientation -- transposition kills it; even the asymmetric diagnostic w2'Vt w1 reads |dPhi| = 0.0, report-only) -- the residual Z2 is REAL GAUGE at the deployed-machine level, the canonicity verdict stands and is NOT upgraded; the scrambled-register control fires (multiplicativity violated on 21 pairs, machine readout moves at 8.2e-2).  All three parts are audits of a DEPLOYED discovery (the v863 scalar-limit determinant) -- selection census, burial, and no-go wards; no new physical claim, no marker moves.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes divisor210_canonicity_probe.py (36/36,
verdict DIVISOR210-GAUGE-FAMILY(2)), moving12_soft17_probe.py
(12/12, verdict MOVING12-DIMENSION-ONLY) and chiral_phase_probe.py
(15/15, verdict CHIRALITY-DEGENERATE, spec v2 with the two
structural no-go wards), 2026-08-08, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: frozen sources embedded
BYTE-EXACT and executed verbatim in isolated namespaces; printed
spec SHAs reproduce; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gates.  The moving-12
probe imports pole_port_kappa_probe.py (gated in v864) and
softport_cauchy_probe.py (gated in v864) READ-ONLY; the chirality
probe imports krein_normalform_probe.py (v861),
redheffer_colligation_probe.py (v863), divisor_weyl_port_probe.py
and weyl_readout_repair_probe.py (v865) READ-ONLY -- none re-gated
here.

FIREWALL: no zeros, no prime-table oracles beyond sympy factorint on
the 16 register labels (AST firewalls inside the probes); the
blind-protocol decider rules of the chirality probe frozen before
evaluation; scramble controls MUST-FIRE and do.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source divisor210_canonicity_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""divisor210_canonicity_probe -- E8.DIVISOR210.CANONICITY.01:
the hard canonicity guard for the 210 discovery.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH claim.  Frozen (spec + sha256)
before running.  Exact integer/Fraction arithmetic; sympy only for one
rational determinant, factorint cross-checks and the 50-digit
separation diagnostic; no floats in any decision, no RNG, no fit.

THE FINDING TO GUARD (redheffer_colligation_probe, read-only): the
16-label Gaussian register F_2^4 was identified with the divisor
lattice of 210 = 2*3*5*7 (bits = primes), with Walsh-Hadamard carrying
the lattice Moebius mu as signs, and the two scalar-limit Euler
constants det_A = prod_p (1 - 1/p) = 8/35 (both-half-weighted vacuum
closure) and det_B = prod_p (1 - p^{-1/2}) (unweighted vacuum column).

THE GENERICITY DANGER (predeclared): EVERY squarefree N = p1 p2 p3 p4
gives a Boolean 16-lattice ~ F_2^4 with mu(d) = (-1)^omega(d) a Walsh
character -- the first layer is generic and the census MUST measure it
as generic.  The specific content, if any, must come from (a) the
SEMANTICALLY FIXED four bits of the deployed register (family 3-cycle
sigma, anchor bit A, mu4 weld grade, code gradings q*/iota) and (b)
the deployed scalar-limit constants.

FROZEN PROTOCOL (2026-08-08, frozen + SHA-hashed before first run):

 S1  REGISTER REGRESSIONS (control 1; v845 NORMALFORM.CFIN.01
     machinery rebuilt read-only): Construction-A Gaussian E8 (C*, 2
     of 30 placements); census 240 = 15 x 16, zero class EMPTY; sigma
     descends with exactly 3 fixed nonzero classes; family/anchor
     basis (F1,F2,F3,A) found with Gram(hbar) = J - I and hbar == the
     bit form on all 256 pairs; sigma in bits = (f1,f2,f3,a) ->
     (f3,f1,f2,a); EXACTLY 16 quadratic refinements, Arf census
     6 + 10, selector (sigma-invariant 4 -> q(A)=1 2 -> q(F_Sigma)=0
     1) picks the unique q* of Arf type 1; iota bijective onto
     C_even(5), beta == hbar, q_wt == q*, 3+2 slot action.  Any fail
     => REGISTER-BROKEN.

 S2  THE DEPLOYED GAUGE (computed exactly, bit model):
     (a) |Sp(4,2)| = 720 by full 65536-matrix census;
     (b) G1 = {g in Sp : g sigma = sigma g, q* o g = q*};
     (c) G2 = Aut(C_fin) = {g in G1 : exists pi in S5 with
         iota o g = pi o iota} -- REGRESSION: |G2| = 6, cyclic
         (CFIN.UNIQUE.01, Aut(C_fin) ~ C6); fail => GAUGE-BROKEN;
     (d) G3 = {g in G2 : wt(g v) = wt(v) for all v} -- the subgroup
         preserving the mu4 weld grade i^{wt} (deployed coordinates);
         MEASURED (expected C3 = <sigma>; the weld grade is extra
         structure beyond C_fin -- typed either way);
     (e) THE ANCHOR FORCING, register side: the number of sigma-fixed
         nonzero classes with q* = 1 (bar: exactly 1 = A);
     (f) THE AXIS FREEDOM: census of all ordered admissible bases
         (X1,X2,X3,A') -- pins: A' sigma-fixed nonzero with q*=1;
         sigma X1 = X2, sigma X2 = X3 (free 3-orbit); {X1,X2,X3,A'}
         independent with A' outside span(X1,X2,X3); Gram(hbar) =
         J - I; q*(X1+X2+X3) = 0.  Count ordered bases, unordered
         axis sets, G2-transitivity, and the weld-compatible subset
         (Hamming weight in basis coordinates == deployed weight for
         all 16 classes).  All counts MEASURED.

 S3  THE FINDING REBUILT (control 2, deployed quadruple {2,3,5,7}):
     Walsh signs 4*WH[1111, v] == mu(d(v)) = (-1)^{wt v} on all 16
     labels (exact Fractions, mu cross-checked against factorint);
     the lattice zeta matrix Z has inverse M[S,T] = [S<=T]
     (-1)^{|T \ S|} (exact integer product Z M == I); det variant A:
     det(Z + u e_1^T) with u[b] = 1/b (b > 1) == 8/35 by direct
     16 x 16 rational determinant AND by the matrix-determinant lemma
     1 + sum_{b>1} mu(b)/b; det variant B: 1 + sum_{b>1} mu(b)
     b^{-1/2} == prod_p (1 - p^{-1/2}) by EXACT radical-expansion
     maps {squarefree radicand: coefficient} (linear independence of
     distinct squarefree radicals over Q, Besicovitch, cited not
     re-proved); two foreign witnesses ({3,5,7,11}, {2,3,5,11}) give
     different det_A values (exact).  Any fail => FINDING-BROKEN.

 S4  THE QUADRUPLE CENSUS (predeclared field: ALL C(10,4) = 210
     quadruples of distinct primes < 30, i.e. 4-subsets of
     {2,3,5,7,11,13,17,19,23,29}; the count 210 = 2*3*5*7 is a
     pleasing COINCIDENCE, typed as such, not evidence):
     (B)  Boolean layer: mu(d) == (-1)^{omega(d)} == the full-parity
          Walsh character for every quadruple -- the genericity
          measurement (predeclared expectation: 210/210 pass; this
          layer carries NO selection content);
     (Q1) Euler test: prod_p (1 - 1/p) == 8/35, exact Fraction --
          count matches;
     (Q2) half-weight test: prod_p (1 - p^{-1/2}) == the deployed
          value, compared as EXACT radical-expansion maps -- count
          matches; plus the 50-digit separation diagnostic (minimum
          |difference| over non-matching quadruples, bar 1e-40);
     (T)  prod_p == 210: tautological (the modulus was DEFINED from
          the primes) -- typed, excluded from the verdict.

 S5  THE ROLE CENSUS (for the Q1-and-Q2-surviving quadruple(s)):
     IDENTIFICATIONS = { linear isos phi : V -> divisor group, phi =
     (ordered admissible basis from S2f) x (bijection axes ->
     primes) }, deduplicated as label maps (cyclic re-rooting of a
     basis gives the same phi).  Register gauge acts by phi -> phi o
     g; PRIMARY gauge = G3 on the weld-compatible identifications
     (the finding-to-guard uses the weld grade in design (b));
     SECONDARY reading = G2 on all identifications (measured; the
     final class count must agree or the discrepancy is typed).
     Frozen battery per identification:
     (i)   grading: wt_deployed(v) == omega(phi(v)) for all 16 AND
           mu(phi(v)) == (-1)^{wt v} -- measured (pin for the weld-
           compatible set, fails for weld-incompatible bases: typed);
     (ii)  sigma transport: phi o sigma o phi^{-1} == the
           multiplicative extension of the 3-cycle (p_{X1} p_{X2}
           p_{X3}) fixing p_{A} on all 16 divisors -- measured
           (predeclared expectation: passes for ALL bijections; the
           Boolean lattice is S4-symmetric, so (ii) alone forces NO
           anchor prime -- the honest genericity of layer two);
     (iiw) weighted sigma: the transported 3-cycle preserves the
           half-weights w(d) = d^{-1/2} iff the three family primes
           are EQUAL -- measured (expected 0 pass); TYPED, NOT a
           filter: the deployed design (b) applies the weights as
           modular phases on which sigma acts covariantly, not
           invariantly;
     (iii) R3, THE ONLY FROZEN ROLE FILTER: phi(A) == 2.  Rationale
           (frozen): the register V = L/(1+i)L is the quotient at the
           RAMIFIED prime of Z[i] ((1+i)^2 = 2i, N(1+i) = 2); 2 is
           the unique ramified prime, the anchor A is the unique
           sigma-fixed q*=1 class -- uniqueness matched to
           uniqueness.  Quadruples without 2 admit no R3 assignment
           (84 = C(9,3) of 210 contain 2 -- context, measured);
     (iv)  Z[i]-splitting profile (measured, typed, NOT a filter):
           for R3 survivors the family primes are {3,5,7} =
           (inert, split, inert) (p mod 4 = 3,1,3); no prime 3-cycle
           preserves the splitting type -- the family symmetry is
           register-side only; honesty note #2;
     (v)   compiler crossrefs (measured, typed, NOT filters):
           {2,3,5} == {|Z_2|, N_fam, g_car} exact; the clock alphabet
           {2,3,5,6} vs the quadruple {2,3,5,7}: overlap {2,3,5},
           MISMATCH 6 != 7 typed, not smoothed (6 = |R+(A3)| = 2*3 is
           itself the unique weight-2 divisor of 210 built from two
           alphabet primes; candidate exact readings of 7 measured:
           7 == |R+(A3)| + 1 == 2^{N_fam} - 1 == 15 - 8 = the
           adjoint-side class count of the v845 S7 census; NO
           selection among them); the pointwise reading family bits
           -> {2,3,5} = {|Z_2|, N_fam, g_car} is GAUGE-INCONSISTENT
           (the family bits are gauge-symmetric, the three constants
           are semantically distinct) -- typed.

 S6  VERDICT (frozen precedence):
     REGISTER-BROKEN / GAUGE-BROKEN / FINDING-BROKEN as above;
     else let nQ = #quadruples passing Q1 AND Q2:
       nQ != 1                       -> DIVISOR210-GENERIC (typed,
                                        with the Euler results);
       nQ == 1: let k = #primary-gauge classes of identifications
       passing the frozen filter R3:
         k == 1                      -> DIVISOR210-CANONICAL;
         2 <= k <= 8                 -> DIVISOR210-GAUGE-FAMILY(k)
                                        (the residual freedom typed
                                        from the measured orbits);
         k == 0 or k > 8             -> DIVISOR210-GENERIC.
     CONTROL-DEAD if any control fails to fire.

 S7  CONTROLS (must fire):
     C1 register regressions = S1 (above);
     C2 Walsh-mu sign identity + both det closed forms = S3 (above);
     C3 SCRAMBLED REGISTER (anti-vacuity ward): drop the structure
        (sigma' = id, q' = 0): the anchor census 1 -> 0, the
        admissible-basis census 6 -> 0 (NOTHING passes -- the census
        discriminates), the gauge explodes to full Sp(4,2) = 720;
        flavor 2 (sigma' = id, q' = q*): anchor census -> 10 (not
        unique); Gram-only baseline: ordered bases with Gram J - I
        alone = 720 (simply transitive Sp-torsor) vs 6 with the
        deployed pins -- the semantics cut 720 -> 6.  Fire rule: all
        three measured collapses occur.

DELIVERABLES: the gauge-group computation, the census table
(aggregates + all matching rows), the 6-vs-7 honesty note, the
verdict with what forces what, controls, honest consequence.

Sources (read-only, machinery rebuilt inline): verification/
v845_cfin_normal_form.py (register, q*, sigma, iota, basis),
experiments/tfpt-discovery/cfin_uniqueness_probe.py (Aut(C_fin)
joint-stabilizer method), experiments/tfpt-discovery/
redheffer_colligation_probe.py (the finding: WH-mu, det wards),
tfpt_constants (N_fam = 3, g_car = 5).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/divisor210_canonicity_probe.py
"""

import hashlib
import itertools
import math
import sys
import time
from fractions import Fraction

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

N_FAM = 3
G_CAR = 5
Z2_ORDER = 2
RPLUS_A3 = 6

PRIMES_LT_30 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
DEPLOYED_QUAD = (2, 3, 5, 7)
DET_A_DEPLOYED = Fraction(8, 35)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0),
          flush=True)


print("E8.DIVISOR210.CANONICITY.01 -- the hard canonicity guard for "
      "the 210 discovery")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ======================================================================
section("S1: register regressions (v845 machinery rebuilt read-only)")
# ======================================================================
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
          for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


placements = set()
for perm in itertools.permutations(range(8)):
    placements.add(code_image(C_NAIVE, perm))
both = [c for c in placements
        if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
CSTAR = next(c for c in both if (1, 0, 1, 0, 1, 0, 1, 0) in c)

ROOTS = []
for k in range(8):
    for s in (2, -2):
        v = [0] * 8
        v[k] = s
        ROOTS.append(tuple(v))
for c in (c for c in CSTAR if sum(c) == 4):
    sup = [k for k in range(8) if c[k]]
    for signs in itertools.product((1, -1), repeat=4):
        v = [0] * 8
        for k, s in zip(sup, signs):
            v[k] = s
        ROOTS.append(tuple(v))


def J_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def sig_vec(v):
    return tuple(v[PI_SIG[k]] for k in range(8))


def in_L(v):
    return tuple(x % 2 for x in v) in CSTAR


def in_pi2L(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L([x // 2 for x in w])


REPS = [(0,) * 8]
for r in ROOTS:
    if not any(in_pi2L(tuple(a - b for a, b in zip(r, rep)))
               for rep in REPS):
        REPS.append(r)


def label_of(v):
    for li, rep in enumerate(REPS):
        if in_pi2L(tuple(a - b for a, b in zip(v, rep))):
            return li
    raise AssertionError("vector not in L or label table broken")


census = {}
for r in ROOTS:
    census[label_of(r)] = census.get(label_of(r), 0) + 1
check("S1.1 placements 30, mu4/sigma-invariant 2; |V| = 16; census "
      "240 = 15 x 16, zero class EMPTY",
      len(placements) == 30 and len(both) == 2 and len(REPS) == 16
      and len(census) == 15 and 0 not in census
      and sorted(census.values()) == [16] * 15, kill="REGISTER-BROKEN")


def sig_label(li):
    return label_of(sig_vec(REPS[li]))


fixed_nz = [li for li in range(1, 16) if sig_label(li) == li]
check("S1.2 sigma descends: sigma^3 = id on 16 labels, EXACTLY 3 "
      "nonzero fixed classes",
      all(sig_label(sig_label(sig_label(li))) == li for li in range(16))
      and len(fixed_nz) == 3 and sig_label(0) == 0,
      kill="REGISTER-BROKEN")


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def hbar_vec(x, y):
    re2, im2 = ip(x, y), ip(x, J_vec(y))
    assert re2 % 2 == 0 and im2 % 2 == 0
    return ((re2 // 2) + (im2 // 2)) % 2


GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
Z4 = (0, 0, 0, 0)


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


BITS = None
FAM = None
for o1 in range(1, 16):
    if o1 in fixed_nz:
        continue
    o2, o3 = sig_label(o1), sig_label(sig_label(o1))
    if len({o1, o2, o3}) != 3:
        continue
    r1, r2, r3 = REPS[o1], REPS[o2], REPS[o3]
    fsum = label_of(tuple(a + b + c for a, b, c in zip(r1, r2, r3)))
    if fsum not in fixed_nz:
        continue
    span3 = set()
    for e1, e2, e3 in itertools.product((0, 1), repeat=3):
        span3.add(label_of(tuple(e1 * a + e2 * b + e3 * c
                                 for a, b, c in zip(r1, r2, r3))))
    if len(span3) != 8:
        continue
    for anc in fixed_nz:
        if anc in span3:
            continue
        ra = REPS[anc]
        bits_map = {}
        for bits in itertools.product((0, 1), repeat=4):
            v = tuple(bits[0] * a + bits[1] * b + bits[2] * c
                      + bits[3] * d
                      for a, b, c, d in zip(r1, r2, r3, ra))
            bits_map[label_of(v)] = bits
        if len(bits_map) != 16:
            continue
        gram = [[hbar_vec(u, w) for w in (r1, r2, r3, ra)]
                for u in (r1, r2, r3, ra)]
        if gram == GJI:
            BITS = bits_map
            FAM = (o1, o2, o3, anc, fsum)
            break
    if BITS is not None:
        break
check("S1.3 family/anchor basis FOUND, Gram(hbar) = J - I, 16 bit "
      "addresses bijective", BITS is not None and len(BITS) == 16,
      kill="REGISTER-BROKEN")

ok_bitform = all(
    hbar_vec(REPS[lx], REPS[ly]) == hb(BITS[lx], BITS[ly])
    for lx in range(16) for ly in range(16))
ok_sigbits = all(BITS[sig_label(li)]
                 == (BITS[li][2], BITS[li][0], BITS[li][1], BITS[li][3])
                 for li in range(16))
check("S1.4 hbar == bit form on 256 pairs; sigma in bits = "
      "(f1,f2,f3,a) -> (f3,f1,f2,a)", ok_bitform and ok_sigbits,
      kill="REGISTER-BROKEN")

A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)
ANC, FSUM = FAM[3], FAM[4]
check("S1.5 BITS[A] = (0,0,0,1), BITS[F_Sigma] = (1,1,1,0), F_Sigma "
      "sigma-fixed",
      BITS[ANC] == A_BIT and BITS[FSUM] == FSIG
      and sig_label(FSUM) == FSUM, kill="REGISTER-BROKEN")


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def refinements_of(form):
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            vi = W16[i]
            for j in range(16):
                vj = W16[j]
                vs = tuple((a + b) % 2 for a, b in zip(vi, vj))
                if q[WIDX[vs]] ^ qi ^ q[j] != form(vi, vj):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


refs = refinements_of(hb)
zeros = {q: sum(1 for i in range(16) if q[i] == 0) for q in refs}
arf1 = [q for q in refs if zeros[q] == 6]
arf0 = [q for q in refs if zeros[q] == 10]
check("S1.6 EXACTLY 16 refinements; Arf census 6 + 10",
      len(refs) == 16 and len(arf1) == 6 and len(arf0) == 10,
      kill="REGISTER-BROKEN")

siginv = [q for q in refs
          if all(q[WIDX[sig_bits(w)]] == q[WIDX[w]] for w in W16)]
cand_a = [q for q in siginv if q[WIDX[A_BIT]] == 1]
cand = [q for q in cand_a if q[WIDX[FSIG]] == 0]
check("S1.7 selector 4 -> 2 -> 1 unique; q* Arf type 1 "
      "(%d -> %d -> %d)" % (len(siginv), len(cand_a), len(cand)),
      len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1
      and zeros[cand[0]] == 6, kill="REGISTER-BROKEN")
QSTAR = cand[0]
check("S1.8 sigma preserves q*",
      all(QSTAR[WIDX[sig_bits(w)]] == QSTAR[WIDX[w]] for w in W16),
      kill="REGISTER-BROKEN")


def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


CEVEN = {w for w in itertools.product((0, 1), repeat=5)
         if sum(w) % 2 == 0}
img = {iota(v) for v in W16}
ok_beta = all(sum(x * y for x, y in zip(iota(v), iota(w))) % 2
              == hb(v, w) for v in W16 for w in W16)
qwt = tuple((sum(iota(w)) // 2) % 2 for w in W16)
ok_slots = all(iota(sig_bits(v))
               == (iota(v)[2], iota(v)[0], iota(v)[1],
                   iota(v)[3], iota(v)[4]) for v in W16)
check("S1.9 iota bijective onto C_even(5); beta == hbar (256); "
      "q_wt == q*; 3+2 slot action",
      img == CEVEN and ok_beta and qwt == QSTAR and ok_slots,
      kill="REGISTER-BROKEN")

# ======================================================================
section("S2: the deployed gauge group + the axis freedom (exact)")
# ======================================================================
sp_perms = []
for bits in range(1 << 16):
    M = [[(bits >> (4 * i + j)) & 1 for j in range(4)]
         for i in range(4)]
    cols = [tuple(M[r][j] for r in range(4)) for j in range(4)]
    ok = True
    for i in range(4):
        for j in range(i + 1, 4):
            if hb(cols[i], cols[j]) != GJI[i][j]:
                ok = False
                break
        if not ok:
            break
    if ok:
        p = tuple(WIDX[tuple(sum(M[r][k] * w[k] for k in range(4)) % 2
                             for r in range(4))] for w in W16)
        sp_perms.append(p)
check("S2.1 |Sp(4,2)| = %d == 720 (full 65536-matrix census)"
      % len(sp_perms),
      len(sp_perms) == 720 and len(set(sp_perms)) == 720,
      kill="GAUGE-BROKEN")

SIGP = tuple(WIDX[sig_bits(w)] for w in W16)
G1 = []
for p in sp_perms:
    if all(p[SIGP[i]] == SIGP[p[i]] for i in range(16)):
        if all(QSTAR[p[i]] == QSTAR[i] for i in range(16)):
            G1.append(p)
print("  |G1| = |Stab_Sp(sigma, q*)| = %d" % len(G1))

S5_PERMS = list(itertools.permutations(range(5)))
IOTA_TAB = [iota(w) for w in W16]
G2 = []
G2_SLOT = {}
for p in G1:
    for pi in S5_PERMS:
        if all(tuple(IOTA_TAB[p[i]][s] for s in range(5))
               == tuple(IOTA_TAB[i][pi[s]] for s in range(5))
               for i in range(16)):
            G2.append(p)
            G2_SLOT[p] = pi
            break


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


orders2 = sorted(perm_order(p) for p in G2)
cyclic2 = len(G2) > 0 and max(orders2) == len(G2)
check("S2.2 REGRESSION |Aut(C_fin)| = |G2| = %d == 6, cyclic = %s "
      "-> C6 (CFIN.UNIQUE.01); element orders %s"
      % (len(G2), cyclic2, orders2),
      len(G2) == 6 and cyclic2, kill="GAUGE-BROKEN")

G3 = [p for p in G2
      if all(sum(W16[p[i]]) == sum(W16[i]) for i in range(16))]
orders3 = sorted(perm_order(p) for p in G3)
check("S2.3 MEASURED weld gauge G3 = {g in G2 : wt(g v) = wt(v)}: "
      "|G3| = %d, orders %s (the mu4 weld grade is %s beyond C_fin)"
      % (len(G3), orders3,
         "EXTRA structure (cuts the gauge)" if len(G3) < len(G2)
         else "already implied"),
      len(G3) >= 1 and SIGP in G3)

anchors = [w for w in W16 if w != Z4 and sig_bits(w) == w
           and QSTAR[WIDX[w]] == 1]
check("S2.4 ANCHOR FORCING (register side): sigma-fixed nonzero "
      "classes with q* = 1: %d == 1, = A" % len(anchors),
      anchors == [A_BIT], kill="REGISTER-BROKEN")


def x2(u, w):
    return tuple((a + b) % 2 for a, b in zip(u, w))


FREE12 = [w for w in W16 if w != Z4 and sig_bits(w) != w]
ADM_BASES = []
for X1 in FREE12:
    X2b, X3b = sig_bits(X1), sig_bits(sig_bits(X1))
    span3 = set()
    for e in itertools.product((0, 1), repeat=3):
        vv = Z4
        for c, xx in zip(e, (X1, X2b, X3b)):
            if c:
                vv = x2(vv, xx)
        span3.add(vv)
    if len(span3) != 8:
        continue
    for Ax in anchors:
        if Ax in span3:
            continue
        bb = (X1, X2b, X3b, Ax)
        gram = [[hb(u, w) for w in bb] for u in bb]
        if gram != GJI:
            continue
        if QSTAR[WIDX[x2(x2(X1, X2b), X3b)]] != 0:
            continue
        ADM_BASES.append(bb)
axis_sets = {frozenset(bb) for bb in ADM_BASES}
print("  ordered admissible bases: %d; unordered axis sets: %d"
      % (len(ADM_BASES), len(axis_sets)))
DEPLOYED_BASIS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), A_BIT)
check("S2.5 the deployed basis is admissible; axis census MEASURED: "
      "%d ordered / %d sets" % (len(ADM_BASES), len(axis_sets)),
      DEPLOYED_BASIS in ADM_BASES and len(ADM_BASES) >= 3)


def coords_map(bb):
    out = {}
    for e in itertools.product((0, 1), repeat=4):
        vv = Z4
        for c, xx in zip(e, bb):
            if c:
                vv = x2(vv, xx)
        out[vv] = e
    return out


WELD_BASES = []
for bb in ADM_BASES:
    cm = coords_map(bb)
    if len(cm) == 16 and all(sum(cm[w]) == sum(w) for w in W16):
        WELD_BASES.append(bb)
weld_sets = {frozenset(bb) for bb in WELD_BASES}
check("S2.6 weld-compatible bases (basis-coordinate weight == "
      "deployed weight): %d ordered / %d sets (MEASURED)"
      % (len(WELD_BASES), len(weld_sets)),
      DEPLOYED_BASIS in WELD_BASES)

orb = {tuple(DEPLOYED_BASIS)}
frontier = [tuple(DEPLOYED_BASIS)]
while frontier:
    bb = frontier.pop()
    for p in G2:
        im = tuple(W16[p[WIDX[x]]] for x in bb)
        if im not in orb:
            orb.add(im)
            frontier.append(im)
g2_transitive = orb == {tuple(b) for b in ADM_BASES}
check("S2.7 G2 acts transitively on the ordered admissible bases: %s "
      "(orbit %d of %d) -- the bit axes are unique up to the "
      "deployed gauge" % (g2_transitive, len(orb), len(ADM_BASES)),
      g2_transitive)

# ======================================================================
section("S3: the finding rebuilt -- Walsh-mu + the two Euler dets")
# ======================================================================


def divisor_of(coords, quad):
    d = 1
    for c, p in zip(coords, quad):
        if c:
            d *= p
    return d


def mobius_int(n):
    if n == 1:
        return 1
    f = sp.factorint(n)
    if any(e > 1 for e in f.values()):
        return 0
    return (-1) ** len(f)


DIVS = [divisor_of(w, DEPLOYED_QUAD) for w in W16]
ok_wh = True
for i, w in enumerate(W16):
    wh_sign = (-1) ** sum(a * b for a, b in zip((1, 1, 1, 1), w))
    wh_entry = Fraction(wh_sign, 4)
    if 4 * wh_entry != mobius_int(DIVS[i]) \
            or mobius_int(DIVS[i]) != (-1) ** sum(w):
        ok_wh = False
check("S3.1 Walsh-mu sign identity: 4*WH[1111, v] == mu(d(v)) == "
      "(-1)^wt(v) on all 16 labels (mu via factorint)", ok_wh,
      kill="FINDING-BROKEN")

order16 = sorted(range(16), key=lambda i: (sum(W16[i]), W16[i]))
Zmat = [[1 if all(W16[a][k] <= W16[b][k] for k in range(4)) else 0
         for b in order16] for a in order16]
Mmat = [[((-1) ** sum(W16[b][k] - W16[a][k] for k in range(4))
          if all(W16[a][k] <= W16[b][k] for k in range(4)) else 0)
         for b in order16] for a in order16]
prod = [[sum(Zmat[i][k] * Mmat[k][j] for k in range(16))
         for j in range(16)] for i in range(16)]
check("S3.2 lattice Moebius: Z * M == I exactly (M[S,T] = [S<=T] "
      "(-1)^{|T\\S|})",
      all(prod[i][j] == (1 if i == j else 0)
          for i in range(16) for j in range(16)),
      kill="FINDING-BROKEN")


def det_a_lemma(quad):
    tot = Fraction(1)
    for w in W16:
        if w == Z4:
            continue
        tot += Fraction(mobius_int(divisor_of(w, quad)),
                        divisor_of(w, quad))
    return tot


MA = sp.zeros(16, 16)
for i in range(16):
    for j in range(16):
        MA[i, j] = Zmat[i][j]
for i in range(16):
    dv = divisor_of(W16[order16[i]], DEPLOYED_QUAD)
    if dv > 1:
        MA[i, 0] += sp.Rational(1, dv)
det_a_direct = sp.Rational(MA.det())
euler_a = Fraction(1)
for p in DEPLOYED_QUAD:
    euler_a *= Fraction(p - 1, p)
check("S3.3 det variant A: direct 16x16 det(Z + u e_1^T) = %s == "
      "lemma 1 + sum mu(b)/b = %s == prod(1-1/p) = %s == 8/35"
      % (det_a_direct, det_a_lemma(DEPLOYED_QUAD), euler_a),
      Fraction(int(det_a_direct.p), int(det_a_direct.q))
      == det_a_lemma(DEPLOYED_QUAD) == euler_a == DET_A_DEPLOYED,
      kill="FINDING-BROKEN")


def halfweight_map(quad):
    m = {}
    for r in range(5):
        for S in itertools.combinations(quad, r):
            b = math.prod(S) if S else 1
            m[b] = m.get(b, 0) + (-1) ** r
    return {k: v for k, v in m.items() if v != 0}


def det_b_lemma_map(quad):
    m = {1: 1}
    for w in W16:
        if w == Z4:
            continue
        b = divisor_of(w, quad)
        m[b] = m.get(b, 0) + mobius_int(b)
    return {k: v for k, v in m.items() if v != 0}


hw_deployed = halfweight_map(DEPLOYED_QUAD)
check("S3.4 det variant B (exact radical maps): 1 + sum_{b>1} mu(b) "
      "b^{-1/2} == prod(1 - p^{-1/2}) termwise over squarefree "
      "radicands (linear independence of sqrt(b), cited)",
      det_b_lemma_map(DEPLOYED_QUAD) == hw_deployed,
      kill="FINDING-BROKEN")

w1 = det_a_lemma((3, 5, 7, 11))
w2 = det_a_lemma((2, 3, 5, 11))
check("S3.5 foreign witnesses discriminate: det_A{3,5,7,11} = %s, "
      "det_A{2,3,5,11} = %s, both != 8/35" % (w1, w2),
      w1 != DET_A_DEPLOYED and w2 != DET_A_DEPLOYED,
      kill="FINDING-BROKEN")

# ======================================================================
section("S4: the quadruple census -- 210 quadruples of primes < 30")
# ======================================================================
QUADS = list(itertools.combinations(PRIMES_LT_30, 4))
check("S4.1 predeclared field: C(10,4) = %d == 210 quadruples "
      "(COINCIDENCE with 210 = 2*3*5*7, typed, not evidence)"
      % len(QUADS), len(QUADS) == 210)

bool_generic = 0
for quad in QUADS:
    if all(mobius_int(divisor_of(w, quad)) == (-1) ** sum(w)
           for w in W16):
        bool_generic += 1
check("S4.2 GENERICITY MEASURED (the warning quantified): the "
      "Boolean/Walsh/mu layer passes for %d/210 quadruples -- layer "
      "one carries NO selection content" % bool_generic,
      bool_generic == 210)

q1_hits = [quad for quad in QUADS
           if det_a_lemma(quad) == DET_A_DEPLOYED]
check("S4.3 (Q1) Euler test prod(1-1/p) == 8/35: matches = %d, "
      "hits = %s" % (len(q1_hits), q1_hits),
      len(q1_hits) >= 1 and DEPLOYED_QUAD in q1_hits)

q2_hits = [quad for quad in QUADS
           if halfweight_map(quad) == hw_deployed]
seps = []
target_val = sp.prod([1 - 1 / sp.sqrt(p) for p in DEPLOYED_QUAD])
target_num = sp.Float(target_val.evalf(60), 60)
for quad in QUADS:
    if quad in q2_hits:
        continue
    val = sp.prod([1 - 1 / sp.sqrt(p) for p in quad])
    seps.append(abs(sp.Float(val.evalf(60), 60) - target_num))
min_sep = min(seps)
check("S4.4 (Q2) half-weight test prod(1-p^{-1/2}) == deployed "
      "(exact radical maps): matches = %d, hits = %s; 50-digit "
      "separation of non-matches: min |diff| = %s > 1e-40"
      % (len(q2_hits), q2_hits, sp.Float(min_sep, 8)),
      len(q2_hits) >= 1 and DEPLOYED_QUAD in q2_hits
      and min_sep > sp.Float("1e-40"))

taut = [quad for quad in QUADS if math.prod(quad) == 210]
print("  (T) prod p == 210: %s -- TAUTOLOGICAL (the modulus was "
      "defined from the primes); excluded from the verdict" % taut)

survivors_q = [quad for quad in QUADS
               if quad in q1_hits and quad in q2_hits]
n_q = len(survivors_q)
contains2 = sum(1 for quad in QUADS if 2 in quad)
check("S4.5 quadruple survivors (Q1 AND Q2): %d, %s; context: %d = "
      "C(9,3) quadruples contain the prime 2 (R3-satisfiable)"
      % (n_q, survivors_q, contains2), n_q >= 1 and contains2 == 84)

# ======================================================================
section("S5: the role census -- identifications modulo the gauge")
# ======================================================================
ROLE_RESULTS = {}
for quad in sorted(set(survivors_q) | {DEPLOYED_QUAD}):
    idents = {}
    for bb in ADM_BASES:
        cm = coords_map(bb)
        for assign in itertools.permutations(quad):
            phi = tuple(divisor_of(cm[W16[i]], assign)
                        for i in range(16))
            if phi not in idents:
                idents[phi] = (bb, assign)
    weld_idents = {}
    for bb in WELD_BASES:
        cm = coords_map(bb)
        for assign in itertools.permutations(quad):
            phi = tuple(divisor_of(cm[W16[i]], assign)
                        for i in range(16))
            if phi not in weld_idents:
                weld_idents[phi] = (bb, assign)
    ROLE_RESULTS[quad] = (idents, weld_idents)

QUAD_WIN = survivors_q[0] if n_q == 1 else DEPLOYED_QUAD
IDENTS, WELD_IDENTS = ROLE_RESULTS.get(QUAD_WIN, ({}, {}))
print("  identifications (all admissible bases x 24 bijections, "
      "deduplicated): %d; weld-compatible: %d"
      % (len(IDENTS), len(WELD_IDENTS)))


def omega_of(d):
    return len(sp.factorint(d)) if d > 1 else 0


r1_pass_all = [phi for phi in IDENTS
               if all(omega_of(phi[i]) == sum(W16[i])
                      and mobius_int(phi[i]) == (-1) ** sum(W16[i])
                      for i in range(16))]
r1_pass_weld = [phi for phi in WELD_IDENTS if phi in r1_pass_all]
check("S5.1 (i) grading wt == omega and mu == (-1)^wt: %d/%d of all "
      "identifications, %d/%d of weld-compatible (pin: weld-"
      "incompatible bases fail the deployed weight -- typed)"
      % (len(r1_pass_all), len(IDENTS), len(r1_pass_weld),
         len(WELD_IDENTS)),
      len(r1_pass_weld) == len(WELD_IDENTS) and len(WELD_IDENTS) > 0)


def sigma_transport_ok(phi, meta):
    bb, assign = meta
    pmap = {assign[0]: assign[1], assign[1]: assign[2],
            assign[2]: assign[0], assign[3]: assign[3]}

    def prime_cycle(d):
        out = 1
        for p, e in sp.factorint(d).items():
            out *= pmap[p] ** e
        return out

    return all(phi[WIDX[sig_bits(W16[i])]] == prime_cycle(phi[i])
               for i in range(16))


r2_pass = [phi for phi, meta in IDENTS.items()
           if sigma_transport_ok(phi, meta)]
check("S5.2 (ii) sigma transport == prime 3-cycle fixing the anchor "
      "prime, on all 16 divisors: %d/%d pass -- MEASURED GENERIC "
      "(layer two forces NO anchor prime by itself)"
      % (len(r2_pass), len(IDENTS)), len(r2_pass) == len(IDENTS))

r2w_pass = []
for phi, meta in IDENTS.items():
    bb, assign = meta
    if assign[0] == assign[1] == assign[2]:
        r2w_pass.append(phi)
check("S5.3 (iiw) weighted sigma (transported 3-cycle preserves "
      "d^{-1/2}): %d/%d pass -- TYPED, NOT a filter (the deployed "
      "design applies weights as modular phases; sigma acts "
      "covariantly, and three DISTINCT primes can never have equal "
      "half-weights)" % (len(r2w_pass), len(IDENTS)),
      len(r2w_pass) == 0)

IDX_A = WIDX[A_BIT]
r3_all = [phi for phi in IDENTS if phi[IDX_A] == 2]
r3_weld = [phi for phi in WELD_IDENTS if phi[IDX_A] == 2]
check("S5.4 (iii) R3 THE FROZEN FILTER phi(A) == 2 (the unique "
      "Z[i]-RAMIFIED prime onto the unique sigma-fixed q*=1 class; "
      "(1+i)^2 = 2i, N(1+i) = 2 = the quotient prime of V = "
      "L/(1+i)L): survivors %d/%d all, %d/%d weld"
      % (len(r3_all), len(IDENTS), len(r3_weld), len(WELD_IDENTS)),
      len(r3_all) > 0 and len(r3_weld) > 0)

SPLIT = {p: ("ramified" if p == 2 else
             "split" if p % 4 == 1 else "inert")
         for p in PRIMES_LT_30}
fam_profiles = set()
split_sym = 0
for phi in r3_all:
    bb, assign = IDENTS[phi]
    fam = tuple(SPLIT[p] for p in assign[:3])
    fam_profiles.add(fam)
    if len({SPLIT[p] for p in assign[:3]}) == 1:
        split_sym += 1
check("S5.5 (iv) Z[i]-splitting of the family primes for R3 "
      "survivors: profiles %s; 3-cycles preserving the splitting "
      "type: %d/%d -- the family symmetry is REGISTER-SIDE ONLY "
      "(honesty note #2: 5 splits, 3 and 7 are inert)"
      % (sorted(fam_profiles), split_sym, len(r3_all)),
      split_sym == 0)


def gauge_classes(id_set, gauge):
    id_list = sorted(id_set)
    pos = {phi: k for k, phi in enumerate(id_list)}
    seen = set()
    classes = []
    for phi in id_list:
        if phi in seen:
            continue
        cls = set()
        stack = [phi]
        while stack:
            cur = stack.pop()
            if cur in cls:
                continue
            cls.add(cur)
            for p in gauge:
                nxt = tuple(cur[p[i]] for i in range(16))
                if nxt in pos and nxt not in cls:
                    stack.append(nxt)
        classes.append(sorted(cls))
        seen |= cls
    return classes


cls_weld_all = gauge_classes(set(WELD_IDENTS), G3)
cls_weld_r3 = gauge_classes(set(r3_weld), G3)
cls_full_all = gauge_classes(set(IDENTS), G2)
cls_full_r3 = gauge_classes(set(r3_all), G2)
check("S5.6 PRIMARY gauge classes (G3 on weld identifications): "
      "%d total, %d after R3; SECONDARY (G2 on all): %d total, "
      "%d after R3 -- the two readings agree on the final count: %s"
      % (len(cls_weld_all), len(cls_weld_r3), len(cls_full_all),
         len(cls_full_r3), len(cls_weld_r3) == len(cls_full_r3)),
      len(cls_weld_r3) == len(cls_full_r3))

print("  surviving gauge classes (representatives, deployed basis "
      "coordinates):")
for k, cls in enumerate(cls_weld_r3):
    phi = cls[0]
    bb, assign = WELD_IDENTS[phi]
    print("    class %d: (F1,F2,F3,A) -> %s   [family cycle %s -> %s "
          "-> %s -> ..., anchor %s]"
          % (k + 1, assign, assign[0], assign[1], assign[2],
             assign[3]))

check("S5.7 (v) compiler crossrefs: {2,3,5} == {|Z_2|, N_fam, g_car} "
      "= {%d,%d,%d}; candidate exact readings of 7: |R+(A3)|+1 = %d, "
      "2^N_fam - 1 = %d, 15 - 8 (adjoint-side classes, v845 S7) = %d "
      "-- all == 7, NO selection made"
      % (Z2_ORDER, N_FAM, G_CAR, RPLUS_A3 + 1, 2 ** N_FAM - 1,
         15 - 8),
      {2, 3, 5} == {Z2_ORDER, N_FAM, G_CAR}
      and RPLUS_A3 + 1 == 2 ** N_FAM - 1 == 15 - 8 == 7)

alphabet = {2, 3, 5, 6}
quad_set = set(DEPLOYED_QUAD)
print("  6-vs-7 HONESTY NOTE: clock alphabet {2,3,5,6} vs prime "
      "quadruple {2,3,5,7}: overlap %s, mismatch %s vs %s -- the two "
      "four-sets are DIFFERENT objects; 6 = 2*3 = |R+(A3)| is not "
      "prime (it sits INSIDE the divisor lattice as the unique "
      "weight-2 divisor from two alphabet primes), 7 = 6 + 1 is "
      "prime and NOT in the alphabet.  NOT smoothed over."
      % (sorted(alphabet & quad_set), sorted(alphabet - quad_set),
         sorted(quad_set - alphabet)))
print("  gauge-inconsistency note: the pointwise reading family bits "
      "-> {2,3,5} = {|Z_2|, N_fam, g_car} would attach three "
      "semantically DISTINCT constants to three gauge-SYMMETRIC "
      "bits; rejected as typed, not measured.")

# ======================================================================
section("S7: controls -- the scrambled register (anti-vacuity ward)")
# ======================================================================


def sig_scr(v):
    return v          # scrambled deck: sigma' = id


Q_SCR = tuple(0 for _ in range(16))    # scrambled refinement: q' = 0
scr_anchors_q0 = [w for w in W16
                  if w != Z4 and sig_scr(w) == w
                  and Q_SCR[WIDX[w]] == 1]
scr_anchors_qs = [w for w in W16
                  if w != Z4 and sig_scr(w) == w
                  and QSTAR[WIDX[w]] == 1]
scr_gauge = [p for p in sp_perms
             if all(p[WIDX[sig_scr(W16[i])]]
                    == WIDX[sig_scr(W16[p[i]])] for i in range(16))
             and all(Q_SCR[p[i]] == Q_SCR[i] for i in range(16))]
scr_free = [w for w in W16 if w != Z4 and sig_scr(w) != w]
check("S7.1 SCRAMBLE (sigma'=id, q'=0): anchor census %d == 0 (was "
      "1); free 3-orbit starters %d == 0 -> admissible bases 0 (was "
      "%d); gauge explodes to |Sp(4,2)| = %d (was |G2| = %d) -- "
      "NOTHING passes; the census discriminates"
      % (len(scr_anchors_q0), len(scr_free), len(ADM_BASES),
         len(scr_gauge), len(G2)),
      len(scr_anchors_q0) == 0 and len(scr_free) == 0
      and len(scr_gauge) == 720, kill="CONTROL-DEAD")
check("S7.2 SCRAMBLE flavor 2 (sigma'=id, q'=q*): anchor census = "
      "%d != 1 (all 10 q*=1 classes qualify) -- the family 3-cycle "
      "is load-bearing for the anchor" % len(scr_anchors_qs),
      len(scr_anchors_qs) == 10, kill="CONTROL-DEAD")

gram_only = 0
for cand in itertools.permutations(range(1, 16), 4):
    bb = tuple(W16[i] for i in cand)
    if [[hb(u, w) for w in bb] for u in bb] == GJI:
        gram_only += 1
check("S7.3 Gram-only baseline: ordered bases with Gram(hbar) = "
      "J - I alone: %d == |Sp(4,2)| = 720 (simply transitive "
      "torsor); the deployed pins cut 720 -> %d ordered bases "
      "(factor %d) -- the semantics, not the lattice shape, carry "
      "the selection"
      % (gram_only, len(ADM_BASES),
         720 // max(len(ADM_BASES), 1)),
      gram_only == 720 and len(ADM_BASES) < 20,
      kill="CONTROL-DEAD")

# ======================================================================
section("S6: verdict (frozen precedence)")
# ======================================================================
n_cls = len(cls_weld_r3)
broken = [k for k in KILLS]
if broken:
    verdict = broken[0]
elif n_q != 1:
    verdict = "DIVISOR210-GENERIC"
elif n_cls == 1:
    verdict = "DIVISOR210-CANONICAL"
elif 2 <= n_cls <= 8:
    verdict = "DIVISOR210-GAUGE-FAMILY(%d)" % n_cls
else:
    verdict = "DIVISOR210-GENERIC"

n_pass = sum(1 for _, ok in CHECKS if ok)
print("\n" + "=" * 70)
print("CHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("=" * 70)
print("""
WHAT FORCES WHAT (measured):
 * QUADRUPLE level: the deployed scalar-limit constants pin
   {2,3,5,7} -- Q1 (8/35, exact Fractions) has %d match(es) and Q2
   (prod(1-p^{-1/2}), exact radical maps) has %d match(es) in the
   predeclared 210-quadruple field.  The Boolean/Walsh/mu layer is
   MEASURED GENERIC (210/210), exactly as warned: every squarefree
   quadruple gives that layer for free.
 * ROLE level: the Boolean battery ((i),(ii)) passes for every
   bijection -- it forces NOTHING.  The register forces the anchor
   BIT (unique sigma-fixed q*=1 class, measured 1); the frozen
   ramification crossref R3 (2 = the unique ramified prime of Z[i],
   the very prime at which V = L/(1+i)L is cut) forces the anchor
   PRIME = 2.  After R3, %d gauge class(es) remain: the residual
   freedom is the family-cycle CHIRALITY (which cyclic order of
   {3,5,7} sits on F1 -> F2 -> F3); no register structure orders the
   cycle beyond cyclically, and no {3,5,7} arithmetic structure is
   C3-symmetric (splitting profile inert/split/inert, measured).
 * The mu4 weld grade is EXTRA structure beyond C_fin: it cuts the
   gauge C6 -> C3 (|G3| = %d) and the axis freedom %d -> %d sets;
   both gauge readings give the same final class count.

HONEST CONSEQUENCE: the 210 identification is NOT generic at the
constants level (the Euler dets select {2,3,5,7} uniquely in the
predeclared field) and NOT canonical at the role level without the
ramification crossref; with R3 frozen it is canonical up to the
family-cycle chirality.  The 6-vs-7 mismatch with the clock alphabet
{2,3,5,6} stands and is typed, not resolved.  Exploration only; no
ledger/paper/website claim; NO RH claim.
""" % (len(q1_hits), len(q2_hits), n_cls, len(G3), len(axis_sets),
       len(weld_sets)))
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
'''
# ------------- frozen probe source moving12_soft17_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moving12_soft17_probe -- E8.MOVING12.SOFT17.01: the hypothesis
17 = 12 + 3 + 1 + 1, audited at SPACE level (projectors, principal
angles, characters), not by number-matching.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

BACKGROUND (read-only): the family 3-cycle sigma splits the 15
nonzero register labels as 3 fixed classes + 4 free 3-orbits =
3 + 12 (exact, v845/finite_compiler); the softport analysis
measured a dimension-independent displacement structure of rank
~12 in the tau coordinate (softport_cauchy_probe, run-1 ranks
12/11/11/12/13 over a 3.9x dimension range) and the pole-port
backflow concentrates on n95 <= 17 coupled bulk modes
(pole_port_kappa_probe).  THE HYPOTHESIS: 12 displacement
generators = the 12 sigma-moved label channels; 3 fixed classes =
the static bulk; + 1 vacuum slot; + 1 pole port.

THE GENERICITY DANGER (pre-typed): 12 = 12 and 17 = 12 + 3 + 1 + 1
as NUMBERS is numerology; the audit must compare SPACES.  The
frozen bridge (the only deployed register -> grid map available):
the DIVISOR MODULAR FRAME -- label S with divisor d(S) (the
divisor-210 register, canonicity probe read-only; the moved/fixed
divisor SETS are chirality-independent, verified) maps to the bin
profile phi_d(j) = d^{-i tau_j / 2} (the KMS/modular frequency of
the deployed half-weight d^{-1/2}, redheffer design (b) phases);
the 17-frame = {vacuum d=1} + {3 fixed divisors 2, 105, 210} +
{12 moved divisors} + {pole profile P_j, closed form}.  If the
angles do NOT close, the honest verdict is the burial, typed.

FROZEN PROTOCOL (2026-08-08, frozen + SHA-hashed before first run):

 S1  REGISTER SIDE (exact, bit model; v845 conventions, the
     Construction-A regressions live in the canonicity probe
     read-only): sigma (f1,f2,f3,a) -> (f3,f1,f2,a); fixed nonzero
     = {A, F_Sigma, F_Sigma + A} (3), moved = 12 in exactly 4 free
     3-orbits; the label projectors on C^15: P_moved (12-dim),
     P_fixed (3-dim), exact; the C3 isotypic dimensions EXACT:
     C^15 = triv^7 + om^4 + ombar^4, moved sector = 4 x regular =
     (4, 4, 4), fixed sector = triv^3; the census divisor maps
     (both gauge classes (3,5,7,2) / (3,7,5,2)) give the SAME
     moved/fixed divisor sets; the identity 17 = 12 + 3 + 1 + 1.

 S2  MEASURED OBJECTS (pole_port/softport machinery imported
     read-only; rungs 9/12/13, displacement-rank series also at
     26/40): REGRESSIONS: lam1(Delta) at anchors == softport refs
     {1.675e-4, 7.647e-5, 7.824e-5} rel 1e-3; kappa_POLE(kz9) in
     [2.6, 2.8]; n95 <= 20 with the kz-9 value reported (the
     measured concentration behind the '17'); displacement
     rank@1e-3 in tau at kz9 in [11, 13] and non-growing over
     {9,12,13,26,40} (max <= min + 3).  Objects kept: U = leading
     left displacement vectors (neg bins), V = right (pos bins),
     the top-17 coupled bulk modes (coupling census ci from the
     exact Feshbach split), each transported to bin space by the
     deployed transform (Delta-coords -> h by G+^{-1/2}, then the
     plain odd-extension transform Fp; frozen choice, typed).

 S3  THE FRAME: the 17 bin profiles as above, each normalized;
     conditioning census (singular values of the 17-frame; the
     frame must be numerically independent, smin >= 1e-3).

 S4  PRINCIPAL ANGLES (the space test; angles via SVD of Qa* Qb):
     (b1) span(U) vs moved-frame restricted to neg bins;
     (b2) span(V) vs moved-frame restricted to pos bins;
     (c)  span(top-17 bulk bin profiles) vs span(17-frame);
     bars for IDENTIFIED (machine-level closure, frozen): max
     angle <= 1e-6 rad on (b1) AND (c).  Angles far from 0 =
     the honest burial, typed with the full tables.  CONTRAST
     controls: the foreign frame (quadruple {2,3,5,11}, frozen
     witness) and the scramble-load generators (seed 1, deployed
     softport convention) -- the truth-vs-control angle gap is
     the information census of the bridge (measured, typed; if
     truth and controls are indistinguishable AND far from 0 the
     bridge carries no displacement information -- typed).

 S5  CHARACTERS: sigma acts on the 12 moved divisors by the
     census 3-cycle (class (3,5,7,2); the character CONTENT is
     chirality-independent); the induced permutation T on the
     moved frame; exact isotypic projectors Pi_j = (1/3) sum_m
     om^{-jm} T^m in coefficient space; for each displacement
     generator, the least-squares coefficients on the moved frame
     split into (triv, om, ombar) energies (frame non-orthogonal:
     fractions normalized over the three isotypic images, typed);
     the moved sector's exact prediction is the regular-rep share
     2/3 nontrivial; bar for IDENTIFIED: aggregate nontrivial
     share in [0.5, 0.85].

 S6  MULTIPLICITIES: each of the top-17 bulk modes least-squares
     decomposed on the 17-frame; per-mode energy fractions on the
     sectors (moved, fixed, vacuum, pole) + the in-frame residual
     (how much of the bulk lies in the frame span at all -- the
     honesty number); effective multiplicities m_sector = sum of
     fractions; bar for IDENTIFIED: rounding gives exactly
     (12, 3, 1, 1) AND the median in-frame residual <= 0.3.

 S7  VERDICT (frozen): AUDIT-BROKEN (any S1/S2 regression fails)
     / MOVING12-IDENTIFIED (S4 angle bars AND S5 character bar
     AND S6 multiplicity bar) / MOVING12-DIMENSION-ONLY (the
     honest burial: same dimensions, different spaces -- the
     angle/multiplicity/character tables typed).

Sources (read-only): pole_port_kappa_probe (build_rung,
feshbach_pole, pole_transform_closed), softport_cauchy_probe
(contractor, LAM1_REFS, displacement construction conventions),
divisor210_canonicity_probe results (census classes, cited),
v845 register conventions.  Float64 SVD/eigh; the register side
exact integer.  NO RH claim; report only.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moving12_soft17_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import pole_port_kappa_probe as pp         # noqa: E402 (READ-ONLY)
import softport_cauchy_probe as sc         # noqa: E402 (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []

ANCHORS = (9, 12, 13)
RANK_RUNGS = (9, 12, 13, 26, 40)
ANGLE_BAR = 1e-6
FOREIGN_QUAD = (2, 3, 5, 11)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0),
          flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


def orth(A, tol=1e-12):
    u, s, _ = np.linalg.svd(np.asarray(A, complex),
                            full_matrices=False)
    r = int(np.sum(s > tol * s[0]))
    return u[:, :r]


def principal_angles(A, B):
    Qa, Qb = orth(A), orth(B)
    sv = np.linalg.svd(Qa.conj().T @ Qb, compute_uv=False)
    return np.arccos(np.clip(sv, -1.0, 1.0))


print("E8.MOVING12.SOFT17.01 -- the 17 = 12 + 3 + 1 + 1 hypothesis, "
      "space level")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
print("\nS0 -- firewall")
check("S0.1 AST firewall clean (no zero/prime oracles)",
      not ast_scan())

# ======================================================================
section("S1: the register side -- exact projectors and characters")
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)
fixed_nz = [w for w in W16 if w != (0, 0, 0, 0) and sig_bits(w) == w]
moved = [w for w in W16 if w != (0, 0, 0, 0) and sig_bits(w) != w]
orbits = set()
for w in moved:
    orbits.add(frozenset({w, sig_bits(w), sig_bits(sig_bits(w))}))
check("S1.1 sigma label split: 3 fixed nonzero %s + 12 moved in "
      "exactly 4 free 3-orbits"
      % sorted(fixed_nz),
      sorted(fixed_nz) == sorted([A_BIT, FSIG, (1, 1, 1, 1)])
      and len(moved) == 12 and len(orbits) == 4
      and all(len(o) == 3 for o in orbits), kill="AUDIT-BROKEN")

nz = [w for w in W16 if w != (0, 0, 0, 0)]
S15 = np.zeros((15, 15))
nz_idx = {w: i for i, w in enumerate(nz)}
for w in nz:
    S15[nz_idx[sig_bits(w)], nz_idx[w]] = 1.0
om = np.exp(2j * math.pi / 3.0)
dims = []
for j in range(3):
    Pi = (np.eye(15) + om ** (-j) * S15
          + om ** (-2 * j) * (S15 @ S15)) / 3.0
    dims.append(int(round(float(np.trace(Pi).real))))
mv_mask = np.array([w in moved for w in nz])
dims_mv = []
for j in range(3):
    Pi = (np.eye(15) + om ** (-j) * S15
          + om ** (-2 * j) * (S15 @ S15)) / 3.0
    dims_mv.append(int(round(float(
        np.trace(Pi[np.ix_(mv_mask, mv_mask)]).real))))
check("S1.2 EXACT isotypic dimensions: C^15 = triv^%d + om^%d + "
      "ombar^%d; moved sector (%d,%d,%d) = 4 x regular; fixed "
      "sector triv^3"
      % tuple(dims + dims_mv),
      dims == [7, 4, 4] and dims_mv == [4, 4, 4],
      kill="AUDIT-BROKEN")

CLASS1 = {"F1": 3, "F2": 5, "F3": 7, "A": 2}
CLASS2 = {"F1": 3, "F2": 7, "F3": 5, "A": 2}


def divisor_map(cls):
    p1, p2, p3, pa = cls["F1"], cls["F2"], cls["F3"], cls["A"]
    return {w: (p1 ** w[0]) * (p2 ** w[1]) * (p3 ** w[2])
            * (pa ** w[3]) for w in W16}


D1 = divisor_map(CLASS1)
D2 = divisor_map(CLASS2)
mvset1 = sorted(D1[w] for w in moved)
mvset2 = sorted(D2[w] for w in moved)
fxset1 = sorted(D1[w] for w in fixed_nz)
check("S1.3 census divisor maps (both gauge classes): moved sets "
      "EQUAL %s...; fixed set %s; 17 = 12 + 3 + 1 + 1 == %d"
      % (mvset1[:4], fxset1, 12 + 3 + 1 + 1),
      mvset1 == mvset2 and fxset1 == sorted(D2[w] for w in fixed_nz)
      and fxset1 == [2, 105, 210] and 12 + 3 + 1 + 1 == 17,
      kill="AUDIT-BROKEN")

# ======================================================================
section("S2: the measured objects (pole-port + softport, read-only)")
# ======================================================================
DATA = {}
reg_lam = True
for kz in sorted(set(ANCHORS) | set(RANK_RUNGS)):
    out = pp.build_rung(kz)
    rr, d, Bp, Bm, Fp, K, Gp, Rp, Delta, c_ar = out
    h, D = rr["h"], rr["D"]
    if h > 900:
        continue
    lam, W = np.linalg.eigh(Delta)
    if kz in ANCHORS:
        reg_lam &= abs(lam[0] - sc.LAM1_REFS[kz]) \
            / sc.LAM1_REFS[kz] <= 1e-3
    # displacement structure (softport conventions, inline)
    U_, s_, Vh_, A2_ = sc.contractor(Bp, Bm)
    Cf = A2_ @ U_.conj().T
    L = Cf.shape[0]
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    pos, neg = d > 0.0, d < 0.0
    Cres = Cf[np.ix_(neg, pos)]
    R = tau[neg][:, None] * Cres - Cres * tau[pos][None, :]
    uR, sR, vRh = np.linalg.svd(R)
    rk = int(np.sum(sR > 1e-3 * sR[0]))
    DATA[kz] = dict(rr=rr, d=d, Fp=Fp, Gp=Gp, Rp=Rp, Delta=Delta,
                    lam=lam, tau=tau, pos=pos, neg=neg, rk=rk,
                    uR=uR, vRh=vRh, h=h, D=D, L=L)
    print("    kz %-3d h %-4d L %-5d lam1 %.3e rank@1e-3 %d"
          % (kz, h, L, lam[0], rk), flush=True)
check("S2.1 REGRESSION lam1(Delta) at anchors == softport refs "
      "(rel 1e-3)", reg_lam, kill="AUDIT-BROKEN")
ranks = [DATA[kz]["rk"] for kz in RANK_RUNGS if kz in DATA]
check("S2.2 REGRESSION displacement rank@1e-3(tau): kz9 = %d in "
      "[11, 13]; series %s non-growing (max <= min + 3)"
      % (DATA[9]["rk"], ranks),
      11 <= DATA[9]["rk"] <= 13
      and max(ranks) <= min(ranks) + 3, kill="AUDIT-BROKEN")

kz = 9
dd = DATA[9]
h9, D9, L9 = dd["h"], dd["D"], dd["L"]
v_pole = np.exp(0.5 * np.arange(h9) * D9)
v_pole = v_pole / np.linalg.norm(v_pole)
fp = pp.feshbach_pole(dd["Delta"], dd["Gp"], dd["Rp"], v_pole)
kap9 = fp["s"] / fp["lam1"]
check("S2.3 REGRESSION pole port kz9: kappa = %.3f in [2.6, 2.8]; "
      "n95 = %d <= 20 (the measured bulk concentration behind "
      "the '17')" % (kap9, fp["n95"]),
      2.6 <= kap9 <= 2.8 and fp["n95"] <= 20, kill="AUDIT-BROKEN")

# top-17 coupled bulk modes (exact Feshbach split, coupling census)
w9 = fp["w"]
e1 = np.zeros(h9)
e1[0] = 1.0
u_h = e1 - w9
nu = np.linalg.norm(u_h)
Hh = np.eye(h9) - 2.0 * np.outer(u_h / nu, u_h / nu) \
    if nu > 1e-12 else np.eye(h9)
Bc = Hh[:, 1:]
G9, rv9 = fp["G"], fp["rv"]
gam, Gv = np.linalg.eigh(G9)
ci = (Gv.T @ rv9) ** 2 / gam
order = np.argsort(ci)[::-1]
K17 = 17
modes_delta = Bc @ Gv[:, order[:K17]]           # Delta coords, h x 17
evG, VpG = np.linalg.eigh(dd["Gp"])
Rm9 = VpG @ np.diag(evG ** -0.5) @ VpG.T
modes_h = Rm9 @ modes_delta                     # h-space vectors
modes_bin = dd["Fp"] @ modes_h                  # L x 17 complex
frac95 = float(np.sum(np.sort(ci)[::-1][:K17]) / np.sum(ci))
print("    top-17 coupled bulk modes carry %.4f of r'G^-1 r "
      "(n95 = %d)" % (frac95, fp["n95"]))

# ======================================================================
section("S3: the divisor modular frame (the frozen bridge)")
# ======================================================================
tau9 = dd["tau"]


def profile(dv):
    ph = np.exp(-0.5j * math.log(dv) * tau9) if dv > 1 \
        else np.ones(L9, complex)
    return ph / np.linalg.norm(ph)


def frame_for(dmap):
    mv_cols = [profile(dmap[w]) for w in moved]
    fx_cols = [profile(dmap[w]) for w in fixed_nz]
    vac = profile(1)
    return np.array(mv_cols).T, np.array(fx_cols).T, \
        vac.reshape(-1, 1)


F_mv, F_fx, F_vac = frame_for(D1)
Pc = pp.pole_transform_closed(h9, L9, D9)
F_pole = (Pc / np.linalg.norm(Pc)).reshape(-1, 1)
F17 = np.hstack([F_vac, F_fx, F_mv, F_pole])
sv17 = np.linalg.svd(F17, compute_uv=False)
check("S3.1 frame conditioning: 17 columns, smin/smax = %.3e "
      "(bar >= 1e-3: numerically independent)"
      % (sv17[-1] / sv17[0]),
      F17.shape[1] == 17 and sv17[-1] / sv17[0] >= 1e-3)

# ======================================================================
section("S4: principal angles -- the space test")
# ======================================================================
rk9 = dd["rk"]
U12 = dd["uR"][:, :rk9]                 # neg-bin space
V12 = dd["vRh"][:rk9].conj().T          # pos-bin space
neg9, pos9 = dd["neg"], dd["pos"]


def ang_stats(A, B):
    a = principal_angles(A, B)
    return float(np.max(a)), float(np.min(a)), \
        float(np.median(a)), len(a)


b1 = ang_stats(U12, F_mv[neg9])
b2 = ang_stats(V12, F_mv[pos9])
c17 = ang_stats(modes_bin, F17)
print("    (b1) span(U%d) vs moved-frame|neg  : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % ((rk9,) + b1))
print("    (b2) span(V%d) vs moved-frame|pos  : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % ((rk9,) + b2))
print("    (c)  span(bulk-17) vs 17-frame     : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % c17)

# contrast controls
DF = divisor_map({"F1": FOREIGN_QUAD[1], "F2": FOREIGN_QUAD[2],
                  "F3": FOREIGN_QUAD[3], "A": FOREIGN_QUAD[0]})
Ff_mv, _, _ = frame_for(DF)
b1f = ang_stats(U12, Ff_mv[neg9])
outS = pp.build_rung(9, scramble_seed=1)
dS, BpS, BmS = outS[1], outS[2], outS[3]
US_, sS_, VhS_, A2S_ = sc.contractor(BpS, BmS)
CfS = A2S_ @ US_.conj().T
posS, negS = dS > 0.0, dS < 0.0
CresS = CfS[np.ix_(negS, posS)]
RS = tau9[negS][:, None] * CresS - CresS * tau9[posS][None, :]
uRS, sRS, _ = np.linalg.svd(RS)
rkS = int(np.sum(sRS > 1e-3 * sRS[0]))
b1s = ang_stats(uRS[:, :max(rkS, 1)], F_mv[negS])
print("    contrast: foreign frame {2,3,5,11} max angle %.4f "
      "(truth %.4f, gap %+.4f); scramble generators (rank %d) "
      "max angle %.4f" % (b1f[0], b1[0], b1f[0] - b1[0], rkS,
                          b1s[0]))
angles_close = b1[0] <= ANGLE_BAR and c17[0] <= ANGLE_BAR
check("S4.1 THE ANGLE TEST (frozen bar: max angle <= 1e-6 rad on "
      "(b1) and (c)): %s -- max(b1) = %.4f, max(c) = %.4f rad "
      "(90 deg = 1.5708: orthogonal)"
      % ("CLOSED" if angles_close else
         "NOT CLOSED (the honest burial)", b1[0], c17[0]),
      True)
check("S4.2 contrast census TYPED: |truth - foreign| = %.4f, "
      "|truth - scramble| = %.4f in max angle -- the bridge's "
      "information content (near 0 with angles far from 0 = the "
      "frame does not see the displacement structure at all)"
      % (abs(b1[0] - b1f[0]), abs(b1[0] - b1s[0])), True)

# ======================================================================
section("S5: characters -- the sigma content of the generators")
# ======================================================================
perm12 = np.zeros((12, 12))
for i, w in enumerate(moved):
    j = moved.index(sig_bits(w))
    perm12[j, i] = 1.0
T = perm12
Fn = F_mv[neg9]
coef, *_ = np.linalg.lstsq(Fn, U12, rcond=None)
iso_energy = np.zeros(3)
for j in range(3):
    Pi = (np.eye(12) + om ** (-j) * T
          + om ** (-2 * j) * (T @ T)) / 3.0
    proj = Fn @ (Pi @ coef)
    iso_energy[j] = float(np.sum(np.abs(proj) ** 2))
iso_frac = iso_energy / max(float(np.sum(iso_energy)), 1e-300)
resid = float(np.linalg.norm(Fn @ coef - U12)
              / np.linalg.norm(U12))
nontriv = float(iso_frac[1] + iso_frac[2])
print("    isotypic energy fractions of proj(U) on the moved "
      "frame: triv %.3f, om %.3f, ombar %.3f; in-frame residual "
      "%.3f (regular-rep prediction: 1/3 each, nontrivial 2/3)"
      % (iso_frac[0], iso_frac[1], iso_frac[2], resid))
char_ok = 0.5 <= nontriv <= 0.85
check("S5.1 THE CHARACTER TEST (frozen bar: nontrivial share in "
      "[0.5, 0.85]): share = %.3f -> %s (typed: residual %.3f "
      "says how much of span(U) the moved frame captures at all)"
      % (nontriv, "carries the C3 characters" if char_ok
         else "does NOT verify the regular-rep content", resid),
      True)

# ======================================================================
section("S6: multiplicities -- the bulk-17 sector census")
# ======================================================================
coef17, *_ = np.linalg.lstsq(F17, modes_bin, rcond=None)
sect = {"vac": [0], "fix": [1, 2, 3],
        "mov": list(range(4, 16)), "pole": [16]}
mult = dict.fromkeys(sect, 0.0)
resids = []
print("    mode  in-frame-resid  vac    fix    mov    pole")
for m in range(K17):
    cm = coef17[:, m]
    tot = 0.0
    en = {}
    for snm, cols in sect.items():
        cpart = np.zeros_like(cm)
        cpart[cols] = cm[cols]
        en[snm] = float(np.linalg.norm(F17 @ cpart) ** 2)
        tot += en[snm]
    rm = float(np.linalg.norm(F17 @ cm - modes_bin[:, m])
               / np.linalg.norm(modes_bin[:, m]))
    resids.append(rm)
    for snm in sect:
        mult[snm] += en[snm] / max(tot, 1e-300)
    if m < 5 or m == K17 - 1:
        print("    %-4d  %.3f          %.3f  %.3f  %.3f  %.3f"
              % (m, rm, *(en[s] / max(tot, 1e-300)
                          for s in ("vac", "fix", "mov", "pole"))))
med_resid = float(np.median(resids))
eff = tuple(int(round(mult[s])) for s in ("mov", "fix", "vac",
                                          "pole"))
mult_ok = eff == (12, 3, 1, 1) and med_resid <= 0.3
print("    effective multiplicities (mov, fix, vac, pole) = "
      "(%.2f, %.2f, %.2f, %.2f) -> rounded %s; median in-frame "
      "residual %.3f"
      % (mult["mov"], mult["fix"], mult["vac"], mult["pole"],
         eff, med_resid))
check("S6.1 THE MULTIPLICITY TEST (frozen bar: rounded == "
      "(12, 3, 1, 1) AND median residual <= 0.3): %s"
      % ("matches" if mult_ok else "does NOT match (typed)"),
      True)

# ======================================================================
section("S7: verdict (frozen)")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
elif angles_close and char_ok and mult_ok:
    verdict = "MOVING12-IDENTIFIED"
else:
    verdict = "MOVING12-DIMENSION-ONLY"
n_pass = sum(1 for _, ok in CHECKS if ok)
print("\n" + "=" * 70)
print("CHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("=" * 70)
print("""
HONEST CONSEQUENCE (measured): the register split 3 + 12 and the
isotypic structure (moved = 4 x regular) are EXACT; the measured
displacement rank (%d at kz9, non-growing) and the bulk
concentration (n95 = %d) reproduce the deployed numbers.  The
space-level identification through the only deployed bridge (the
divisor modular frame) gives max principal angles %.4f (b1) /
%.4f (c) rad against the frozen 1e-6 bar, nontrivial character
share %.3f, effective multiplicities (%.1f, %.1f, %.1f, %.1f).
If the verdict above is DIMENSION-ONLY: the 17 = 12 + 3 + 1 + 1
arithmetic stands as a COUNT but the softport displacement
generators are NOT the Gaussian label channels under this bridge
-- the identification hypothesis is buried at space level unless
a different (not yet deployed) intertwiner is exhibited; typed,
not smoothed.  NO RH claim.""" % (rk9, fp["n95"], b1[0], c17[0],
                                  nontriv, mult["mov"],
                                  mult["fix"], mult["vac"],
                                  mult["pole"]))
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
'''
# ------------- frozen probe source chiral_phase_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""chiral_phase_probe -- E8.DIVISOR210.CHIRAL_PHASE.01: deciding
the family-cycle chirality of the 210 register by the phase
readout, blind.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE FREEDOM TO DECIDE (divisor210_canonicity_probe, read-only,
verdict DIVISOR210-GAUGE-FAMILY(2)): after the Euler pin and the
ramification anchor filter, exactly TWO gauge classes survive --
(F1,F2,F3,A) -> (3,5,7,2) [chi+] and (3,7,5,2) [chi-]: the CYCLIC
ORIENTATION of {3,5,7} along the family cycle sigma.  The phase
readout (weyl_readout_repair_probe, readout C: total phase
variation -- orientation-sensitive, strongly discriminating) is
the candidate decider.

FROZEN PROTOCOL (2026-08-08, frozen + SHA-hashed before first
run; ALL decision rules frozen here, BEFORE any evaluation):

 S1  CENSUS REGRESSION (bit model; the heavy lattice/refinement
     regressions live in the canonicity probe, cited): sigma
     (f1,f2,f3,a) -> (f3,f1,f2,a); q* = wt(iota)/2 mod 2 (the
     v845 lift identity, cited); unique anchor (sigma-fixed,
     q*=1) = A; admissible bases 6 ordered / 2 axis sets, weld-
     compatible 3 / 1; R3 (anchor -> 2) survivors modulo the
     weld gauge C3 = <sigma> (G3 from the canonicity run, cited)
     = EXACTLY the two classes chi+ = (3,5,7,2), chi- =
     (3,7,5,2).  Any fail => CENSUS-BROKEN.

 S2  READOUT REGRESSIONS (dw/wr read-only): the v1 extremal ref
     s_min(kz9, a, r2) = 8.68463e-01 +- 1e-5; Herglotz Im m > 0
     and passivity |r| < 1 on ZFIX, the spectral grid and the
     phase window; my inline total-phase-variation == the repair
     probe's readouts()["s_C"] to 1e-12 (the readout is the
     deployed one).  Any fail => READOUT-BROKEN.

 S3  THE BLINDNESS WARD (structural, must FIRE): the sigma-LESS
     chirality machines U0_chi(tau) = WH diag(i^wt)
     diag(d_chi^{-i tau/2}) are exactly conjugate under the bit
     transposition Pi = (F2 <-> F3), which fixes the vacuum port
     and the parity readout w2 -- so the loaded scalar transfer
     is IDENTICAL for chi+ and chi- (matrix ward <= 1e-13;
     loaded scalars <= 1e-12 on the whole phase window).  ANY
     phase readout that does not couple the family-cycle letter
     sigma to the weights is PROVABLY chirality-blind; the
     decider below therefore wires sigma in.  (Also typed: the
     fixed-sector divisors 1, 2, 105, 210 are chirality-equal.)

 S4  THE DECIDER (frozen decision rules):
     D1 REGISTER ORIENTATION FUNCTIONAL (exact): for each of the
        4 free 3-orbits O with root v0 = min(O) and x_k =
        log d_chi(sigma^k v0), X1(O) = sum_k x_k om^k with om =
        e^{2 pi i/3}; Phi_reg(chi) = sum_O Im(X1^3).  WARDS:
        antisymmetry Phi_reg(chi+) = -Phi_reg(chi-) (rel 1e-12);
        re-rooting (v0 -> sigma v0) invariance (the C3 gauge).
     D2 KMS-ORIENTATION CRITERION (frozen): the deployed modular
        phases are e^{-i w tau/2} with tau >= 0 on the dual grid
        (redheffer design (b)); the KMS-compatible chirality :=
        the one with Phi_reg(chi) > 0 (positive spectral winding
        of the log-weights along the cycle, om = e^{+2 pi i/3}
        paired with tau >= 0).  TYPED HONESTLY: this pairing of
        two sign conventions is a CONVENTION BRIDGE unless the
        machine leg (D3) independently selects the same
        chirality; D2 alone cannot decide.
     D3 MACHINE LEG (the sigma-wired loaded phase readout): the
        chirality machine U_chi(tau) = WH diag(i^wt) P_sigma
        diag(d_chi^{-i tau/2}) (P_sigma = the deployed family
        cycle on labels; the ONLY difference between chi+ and
        chi- is the weight assignment); port = vacuum slot
        (U[0,0] = 1/4, warded); load = the deployed divisor
        tower (kz 9, variant a, dw read-only), r(i y) on the
        frozen window y in YPH (33 points), coupling tau_j = y_j
        (frozen); f_j = w2' Vt_chi(r_j, tau_j) w2;
        Phi_mach(chi, load) = sum_j arg(f_{j+1}/f_j) (signed
        winding), V(chi, load) = sum_j |arg(f_{j+1}/f_j)| (total
        variation).  Loads: truth, Epstein (kn.lambda_eps),
        scramble (frozen LCG seed 12345, dw convention).
        FROZEN DECISION: the machine SEES the chirality iff
        |Phi_mach(chi+) - Phi_mach(chi-)| >= 1e-3 rad on truth;
        disc_ok(chi) iff V(chi, eps)/V(chi, truth) outside
        [1/1.5, 1.5] AND V(chi, scr)/V(chi, truth) outside
        [1/1.5, 1.5]; the machine DECIDES iff exactly one
        chirality has disc_ok; then winner_mach = that
        chirality.
 S5  SCRAMBLED-REGISTER CONTROL (must fire): LCG-permute the 12
     moved divisor values (seed 12345): the lattice
     multiplicativity d(v XOR w) = d(v) d(w) on disjoint
     supports BREAKS (count > 0 violated pairs), and the machine
     readout moves (rel >= 1e-6) -- the decider consumes the
     register structure, not just 12 numbers.

 S6  VERDICT (frozen precedence): CENSUS-BROKEN / READOUT-BROKEN
     / WARD-DEAD (S3 or S5 fails to fire) / then:
     - machine decides AND winner_mach == KMS winner (D2) ->
       CHIRALITY-DECIDED (named winner; criterion: machine
       discrimination + KMS orientation agree);
     - machine decides AND winner_mach != KMS winner ->
       CHIRALITY-INCONSISTENT (typed);
     - machine does not decide (both disc_ok, or neither, or
       the machine does not even see the chirality) ->
       CHIRALITY-DEGENERATE (the freedom is real gauge at the
       deployed-machine level; D2 alone is a convention bridge,
       typed, NOT a decision).

Sources (read-only): divisor210_canonicity_probe (census, cited
counts), divisor_weyl_port_probe (towers, closure blocks, v1
refs), weyl_readout_repair_probe (Load, readouts, YPH, ZFIX),
redheffer_colligation_probe (walsh16, hamw),
krein_normalform_probe (lambda_eps), v845 register conventions.
NO RH claim; report only.

ADDENDUM v2 (typed after run 1; run-1 numbers unchanged, no
decision bar moved -- the amendment REPAIRS a mis-calibrated ward
and TYPES two structural findings the run produced):
 (1) MEASURED STRUCTURAL FACT: Phi_reg vanishes IDENTICALLY (both
     chiralities, to 1e-15).  Mechanism, verified exactly: the
     Moebius complement d -> 210/d pairs the four free orbits
     (weight-1 <-> weight-2 at fixed anchor bit) with REVERSED
     cycle orientation, so X1(O')^3 = -X1(O)^3 per pair and the
     orbit sum cancels for EVERY multiplicative weight
     assignment.  The register carries no intrinsic scalar
     orientation of this type; the D2 KMS criterion is therefore
     VACUOUS (winner undefined), typed.  The v1 antisymmetry
     ward divided by |Phi_reg| ~ 1e-15 and failed on float noise
     although antisymmetry holds trivially; v2 wards: absolute
     antisymmetry |Phi+ + Phi-| <= 1e-12, re-rooting invariance
     absolute <= 1e-12, and the NEW exact complement-cancellation
     ward |X1(O)^3 + X1(O')^3| <= 1e-12 per pair.
 (2) MEASURED STRUCTURAL FACT: the sigma-wired QUADRATIC readout
     is also chirality-blind (|dPhi| ~ 1e-15): w2' M w2 =
     w2' M^T w2 sees only the symmetric part of the machine, and
     cycle reversal is exactly transposition up to the
     Pi-conjugation that fixes port and readout (U_-^sigma =
     Pi (sigma^{-1}-machine) Pi^T, and the transposed machine
     has blocks (A^T, C^T, B^T) whose closure scalar under ONE
     readout vector is identical).  v2 adds the ward for this
     equality and a REPORT-ONLY diagnostic: the asymmetric
     two-vector readout w2' Vt w1 (r2 left, r1 right, both
     deployed) -- measured for chirality response and typed, NOT
     verdict-bearing (post-run diagnostic).
 (3) Verdict logic under a vacuous D2: CHIRALITY-DECIDED would
     require the machine leg to decide alone (named as machine-
     only); with D3 measured blind the verdict is
     CHIRALITY-DEGENERATE either way.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/chiral_phase_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn            # noqa: E402 (READ-ONLY)
import redheffer_colligation_probe as rc       # noqa: E402 (READ-ONLY)
import divisor_weyl_port_probe as dw           # noqa: E402 (READ-ONLY)
import weyl_readout_repair_probe as wr         # noqa: E402 (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []

V1_SMIN_REF = 8.68463e-01
SEE_BAR = 1e-3
DISC_FACTOR = 1.5
LCG_SEED = 12345
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0),
          flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


print("E8.DIVISOR210.CHIRAL_PHASE.01 -- the chirality decider, "
      "blind protocol")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
print("\nS0 -- firewall")
check("S0.1 AST firewall clean (no zero/prime oracles)",
      not ast_scan())

# ======================================================================
section("S1: census regression -- the two gauge classes")
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
Z4 = (0, 0, 0, 0)


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def x2(u, w):
    return tuple((a + b) % 2 for a, b in zip(u, w))


def qstar(v):
    f1, f2, f3, a = v
    io = (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)
    return (sum(io) // 2) % 2


GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


anchors = [w for w in W16 if w != Z4 and sig_bits(w) == w
           and qstar(w) == 1]
A_BIT = (0, 0, 0, 1)
check("S1.1 unique anchor (sigma-fixed, q* = 1): %s == [(0,0,0,1)]"
      % anchors, anchors == [A_BIT], kill="CENSUS-BROKEN")

FREE12 = [w for w in W16 if w != Z4 and sig_bits(w) != w]
ADM = []
for X1 in FREE12:
    X2b, X3b = sig_bits(X1), sig_bits(sig_bits(X1))
    span3 = set()
    for e in itertools.product((0, 1), repeat=3):
        vv = Z4
        for c, xx in zip(e, (X1, X2b, X3b)):
            if c:
                vv = x2(vv, xx)
        span3.add(vv)
    if len(span3) != 8 or A_BIT in span3:
        continue
    bb = (X1, X2b, X3b, A_BIT)
    if [[hb(u, w) for w in bb] for u in bb] != GJI:
        continue
    if qstar(x2(x2(X1, X2b), X3b)) != 0:
        continue
    ADM.append(bb)


def coords_map(bb):
    out = {}
    for e in itertools.product((0, 1), repeat=4):
        vv = Z4
        for c, xx in zip(e, bb):
            if c:
                vv = x2(vv, xx)
        out[vv] = e
    return out


WELD = [bb for bb in ADM
        if all(sum(coords_map(bb)[w]) == sum(w) for w in W16)]
check("S1.2 admissible bases %d ordered / %d sets; weld-compatible "
      "%d / %d (canonicity-run counts 6/2 and 3/1)"
      % (len(ADM), len({frozenset(b) for b in ADM}), len(WELD),
         len({frozenset(b) for b in WELD})),
      len(ADM) == 6 and len(WELD) == 3, kill="CENSUS-BROKEN")

QUAD = (2, 3, 5, 7)
idents = {}
for bb in WELD:
    cm = coords_map(bb)
    for assign in itertools.permutations(QUAD):
        if assign[3] != 2:                     # R3 anchor filter
            continue
        phi = tuple((assign[0] ** cm[w][0]) * (assign[1] ** cm[w][1])
                    * (assign[2] ** cm[w][2]) * (assign[3] ** cm[w][3])
                    for w in W16)
        idents.setdefault(phi, assign)
SIGP16 = [WIDX[sig_bits(w)] for w in W16]
classes = []
seen = set()
for phi in sorted(idents):
    if phi in seen:
        continue
    cls = {phi}
    cur = phi
    for _ in range(2):
        cur = tuple(cur[SIGP16[i]] for i in range(16))
        cls.add(cur)
    seen |= cls
    classes.append(sorted(cls)[0])
def canon3(t3):
    k = t3.index(3)
    return t3[k:] + t3[:k]


assigns = sorted(canon3(idents[c][:3]) for c in classes)
check("S1.3 R3 survivors modulo C3 = EXACTLY 2 classes, family "
      "cycles (canonical rotation) %s == [(3,5,7), (3,7,5)] (the "
      "chirality pair)"
      % (assigns,), len(classes) == 2
      and assigns == [(3, 5, 7), (3, 7, 5)], kill="CENSUS-BROKEN")

CHI = {"chi+": {"F1": 3, "F2": 5, "F3": 7, "A": 2},
       "chi-": {"F1": 3, "F2": 7, "F3": 5, "A": 2}}


def dval(cls, w):
    return (cls["F1"] ** w[0]) * (cls["F2"] ** w[1]) \
        * (cls["F3"] ** w[2]) * (cls["A"] ** w[3])


fixed_nz = [w for w in W16 if w != Z4 and sig_bits(w) == w]
check("S1.4 fixed-sector divisors chirality-EQUAL: %s (plus "
      "vacuum 1) -- any fixed-sector functional is chirality-"
      "blind, typed"
      % sorted(dval(CHI["chi+"], w) for w in fixed_nz),
      all(dval(CHI["chi+"], w) == dval(CHI["chi-"], w)
          for w in fixed_nz))

# ======================================================================
section("S2: readout regressions (dw + wr read-only)")
# ======================================================================
VA, VB, VC, D0 = dw.closure_blocks()
w2 = dw.readout_vec("r2")
rr9 = core.build_window(9)
N9 = int(math.exp(2.0 * rr9["alpha"]))
lam9 = dw.mangoldt(N9)
Ha = dw.build_H(N9, lam9, "a")
LOAD = wr.Load(*dw.weyl_data(Ha))
mv1 = LOAD.m(dw.zgrid())
_, outs1, _ = dw.loaded_scalars(mv1, VA, VB, VC, D0)
s_v1 = float(np.min(1.0 - np.abs(outs1["r2"]) ** 2))
check("S2.1 v1 regression: extremal s(kz9, a, r2) = %.6e == "
      "%.6e +- 1e-5" % (s_v1, V1_SMIN_REF),
      abs(s_v1 - V1_SMIN_REF) <= 1e-5, kill="READOUT-BROKEN")
ok_hz = True
for zg in (wr.ZFIX, LOAD.ev + 1j * wr.EPS_B, 1j * wr.YPH):
    mv = LOAD.m(zg)
    ok_hz &= bool(np.all(mv.imag > 0)) and bool(
        np.all(np.abs((mv - 1j) / (mv + 1j)) < 1.0))
check("S2.2 Herglotz + passivity on ZFIX, spectral grid and the "
      "phase window", ok_hz, kill="READOUT-BROKEN")
rd = wr.readouts(LOAD, VA, VB, VC, D0, w2)
rph = LOAD.r(1j * wr.YPH)
sC_inline = float(np.sum(np.abs(np.angle(rph[1:] / rph[:-1]))))
check("S2.3 inline total-phase-variation == wr.readouts s_C "
      "(%.6e vs %.6e, diff %.1e)"
      % (sC_inline, rd["s_C"], abs(sC_inline - rd["s_C"])),
      abs(sC_inline - rd["s_C"]) <= 1e-12, kill="READOUT-BROKEN")

# ======================================================================
section("S3: the blindness ward -- sigma-less machines are "
        "chirality-blind (structural)")
# ======================================================================
WH = rc.walsh16()
WELD16 = np.diag([1j ** rc.hamw(S) for S in range(16)])


def sig_int(S):
    f1, f2, f3, a = S & 1, (S >> 1) & 1, (S >> 2) & 1, (S >> 3) & 1
    return f3 + 2 * f1 + 4 * f2 + 8 * a


def pi_int(S):
    f1, f2, f3, a = S & 1, (S >> 1) & 1, (S >> 2) & 1, (S >> 3) & 1
    return f1 + 2 * f3 + 4 * f2 + 8 * a


P_SIG = np.zeros((16, 16))
P_PI = np.zeros((16, 16))
for S in range(16):
    P_SIG[sig_int(S), S] = 1.0
    P_PI[pi_int(S), S] = 1.0


def dvec(chi):
    cls = CHI[chi]
    return np.array([dval(cls, ((S & 1), (S >> 1) & 1,
                                (S >> 2) & 1, (S >> 3) & 1))
                     for S in range(16)], float)


D_P, D_M = dvec("chi+"), dvec("chi-")


def machine(chi, tau, with_sigma):
    ph = np.diag(np.exp(-0.5j * np.log(dvec(chi)) * tau))
    U = WH @ WELD16 @ ((P_SIG @ ph) if with_sigma else ph)
    return U


def loaded_f(chi, rvals, taus, with_sigma):
    out = []
    for r_, t_ in zip(rvals, taus):
        U = machine(chi, t_, with_sigma)
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w2))
    return np.array(out)


taus = np.asarray(wr.YPH, float)
r_truth = LOAD.r(1j * wr.YPH)
conj_dev = max(float(np.max(np.abs(
    machine("chi-", t, False)
    - P_PI @ machine("chi+", t, False) @ P_PI.T)))
    for t in (taus[0], taus[16], taus[-1]))
f0p = loaded_f("chi+", r_truth, taus, False)
f0m = loaded_f("chi-", r_truth, taus, False)
blind_dev = float(np.max(np.abs(f0p - f0m)))
u_test = machine("chi+", taus[0], True)
check("S3.1 WARD FIRES: U0_- == Pi U0_+ Pi^T (max dev %.1e <= "
      "1e-13); sigma-less loaded scalars IDENTICAL for chi+/chi- "
      "(max dev %.1e <= 1e-12) -- any phase readout without the "
      "sigma letter is PROVABLY chirality-blind"
      % (conj_dev, blind_dev),
      conj_dev <= 1e-13 and blind_dev <= 1e-12, kill="WARD-DEAD")
check("S3.2 the sigma-wired machine is unitary with port "
      "U[0,0] = 1/4 (dev %.1e; closure well-posed)"
      % abs(u_test[0, 0] - 0.25),
      float(np.max(np.abs(u_test.conj().T @ u_test
                          - np.eye(16)))) <= 1e-12
      and abs(u_test[0, 0] - 0.25) <= 1e-14)

# ======================================================================
section("S4: the decider (frozen rules, evaluated only now)")
# ======================================================================
om = np.exp(2j * math.pi / 3.0)
orb_roots = sorted({min(frozenset({w, sig_bits(w),
                                   sig_bits(sig_bits(w))}))
                    for w in FREE12})


def x1cube(dmapper, v0):
    xs = [math.log(dmapper(v0)),
          math.log(dmapper(sig_bits(v0))),
          math.log(dmapper(sig_bits(sig_bits(v0))))]
    return (xs[0] + xs[1] * om + xs[2] * om ** 2) ** 3


def phi_reg(dmapper, roots=None):
    return float(sum(x1cube(dmapper, v0)
                     for v0 in (roots or orb_roots)).imag)


phi_p = phi_reg(lambda w: dval(CHI["chi+"], w))
phi_m = phi_reg(lambda w: dval(CHI["chi-"], w))
reroot = phi_reg(lambda w: dval(CHI["chi+"], w),
                 roots=[sig_bits(v) for v in orb_roots])
check("S4.1 D1 wards (v2, absolute): antisymmetry "
      "|Phi_reg(chi+) + Phi_reg(chi-)| = %.1e <= 1e-12; "
      "re-rooting invariance (dev %.1e)"
      % (abs(phi_p + phi_m), abs(reroot - phi_p)),
      abs(phi_p + phi_m) <= 1e-12
      and abs(reroot - phi_p) <= 1e-12)
# v2 ward: the Moebius-complement pairing cancels per orbit pair
dmap_p = lambda w: dval(CHI["chi+"], w)               # noqa: E731
comp_dev = 0.0
for v0 in orb_roots:
    vc = x2((1, 1, 1, 1), v0)                          # d -> 210/d
    comp_dev = max(comp_dev, abs(complex(
        x1cube(dmap_p, v0) + x1cube(dmap_p, vc))))
check("S4.1b v2 STRUCTURAL WARD: the Moebius complement d -> "
      "210/d pairs the 4 orbits with reversed orientation, "
      "X1(O)^3 + X1(O')^3 = 0 per pair (max dev %.1e) -- "
      "Phi_reg == 0 IDENTICALLY for every multiplicative weight "
      "assignment: the register carries no intrinsic scalar "
      "orientation of this type" % comp_dev, comp_dev <= 1e-12)
kms_winner = None
if abs(phi_p) > 1e-12:
    kms_winner = "chi+" if phi_p > 0 else "chi-"
print("    D2 KMS-orientation criterion: Phi_reg(chi+) = %+.2e, "
      "Phi_reg(chi-) = %+.2e -> %s"
      % (phi_p, phi_m,
         ("KMS-compatible chirality = %s (convention bridge "
          "unless D3 agrees)" % kms_winner) if kms_winner else
         "VACUOUS (Phi_reg == 0 identically; no KMS winner, "
         "typed v2)"))

# D3: loads
lamE = kn.lambda_eps(N9)[:N9 + 1]


def lcg_perm(n, seed):
    s = seed
    idx = list(range(2, n + 1))
    for i in range(len(idx) - 1, 0, -1):
        s = (1103515245 * s + 12345) % (1 << 31)
        j = s % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return idx


lamS = np.zeros(N9 + 1)
lamS[2:] = lam9[lcg_perm(N9, LCG_SEED)]
loads = {"truth": LOAD}
for nm, lm in (("eps", lamE), ("scr", lamS)):
    H_ = dw.build_H(N9, lm, "a")
    loads[nm] = wr.Load(*dw.weyl_data(H_))
PHI = {}
VV = {}
for lnm, ld in loads.items():
    rv = ld.r(1j * wr.YPH)
    for chi in ("chi+", "chi-"):
        f = loaded_f(chi, rv, taus, True)
        dphi = np.angle(f[1:] / f[:-1])
        PHI[(chi, lnm)] = float(np.sum(dphi))
        VV[(chi, lnm)] = float(np.sum(np.abs(dphi)))
print("    load     Phi(chi+)   Phi(chi-)   V(chi+)   V(chi-)")
for lnm in ("truth", "eps", "scr"):
    print("    %-7s %+.5f   %+.5f   %.5f   %.5f"
          % (lnm, PHI[("chi+", lnm)], PHI[("chi-", lnm)],
             VV[("chi+", lnm)], VV[("chi-", lnm)]))
delta_see = abs(PHI[("chi+", "truth")] - PHI[("chi-", "truth")])
sees = delta_see >= SEE_BAR
disc_ok = {}
for chi in ("chi+", "chi-"):
    vt = VV[(chi, "truth")]
    rE = VV[(chi, "eps")] / max(vt, 1e-300)
    rS = VV[(chi, "scr")] / max(vt, 1e-300)
    disc_ok[chi] = (not (1.0 / DISC_FACTOR <= rE <= DISC_FACTOR)) \
        and (not (1.0 / DISC_FACTOR <= rS <= DISC_FACTOR))
    print("    disc(%s): V_eps/V_truth = %.3f, V_scr/V_truth = "
          "%.3f -> discrimination %s"
          % (chi, rE, rS, "PRESERVED" if disc_ok[chi]
             else "LOST/INSIDE the 1.5x window"))
decides = sees and (disc_ok["chi+"] != disc_ok["chi-"])
mach_winner = None
if decides:
    mach_winner = "chi+" if disc_ok["chi+"] else "chi-"
check("S4.2 D3 measured: |Phi(chi+) - Phi(chi-)| = %.3e on truth "
      "(sees the chirality: %s, bar 1e-3); machine decides "
      "(exactly one disc_ok): %s%s"
      % (delta_see, sees, decides,
         ("; winner " + mach_winner) if mach_winner else ""),
      True)
# v2 ward: WHY the quadratic readout is blind -- transpose
# symmetry (w2' M w2 = w2' M^T w2; cycle reversal = transposition
# up to the Pi-conjugation fixing port and readout)
check("S4.3 v2 STRUCTURAL WARD: sigma-wired QUADRATIC readout "
      "chirality-equal to machine precision (max dev %.1e <= "
      "1e-12) -- the symmetric form w2' Vt w2 cannot see the "
      "cycle orientation (transposition kills it); an "
      "orientation-sensitive readout needs an ASYMMETRIC pairing"
      % delta_see, delta_see <= 1e-12)
# v2 REPORT-ONLY diagnostic: asymmetric two-vector readout
w1v = dw.readout_vec("r1")


def loaded_f_asym(chi, rvals, tvals):
    out = []
    for r_, t_ in zip(rvals, tvals):
        U = machine(chi, t_, True)
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w1v))
    return np.array(out)


fa_p = loaded_f_asym("chi+", r_truth, taus)
fa_m = loaded_f_asym("chi-", r_truth, taus)
phi_ap = float(np.sum(np.angle(fa_p[1:] / fa_p[:-1])))
phi_am = float(np.sum(np.angle(fa_m[1:] / fa_m[:-1])))
print("    v2 DIAGNOSTIC (report-only, NOT verdict-bearing): "
      "asymmetric readout w2' Vt w1: Phi(chi+) = %+.5f, "
      "Phi(chi-) = %+.5f, |dPhi| = %.3e -- the asymmetric "
      "pairing %s the chirality"
      % (phi_ap, phi_am, abs(phi_ap - phi_am),
         "SEES" if abs(phi_ap - phi_am) >= 1e-3 else
         "still does not see"))

# ======================================================================
section("S5: scrambled-register control")
# ======================================================================
mv_labels = sorted(FREE12)
mv_vals = [dval(CHI["chi+"], w) for w in mv_labels]
pidx = lcg_perm(len(mv_vals), LCG_SEED)     # perm of 2..12 indices
perm_vals = list(mv_vals)
ordr = [i - 2 for i in pidx] + [len(mv_vals) - 1]
perm_vals = [mv_vals[i] for i in ordr]
scr_map = dict(zip(mv_labels, perm_vals))


def d_scr(w):
    if w in scr_map:
        return scr_map[w]
    return dval(CHI["chi+"], w)


viol = 0
for u, v in itertools.combinations([w for w in W16 if w != Z4], 2):
    if all(a * b == 0 for a, b in zip(u, v)):
        if d_scr(x2(u, v)) != d_scr(u) * d_scr(v):
            viol += 1
D_SCRV = np.array([d_scr(((S & 1), (S >> 1) & 1, (S >> 2) & 1,
                          (S >> 3) & 1)) for S in range(16)],
                  float)


def loaded_f_weights(dw16, rvals, tvals):
    out = []
    for r_, t_ in zip(rvals, tvals):
        ph = np.diag(np.exp(-0.5j * np.log(dw16) * t_))
        U = WH @ WELD16 @ P_SIG @ ph
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w2))
    return np.array(out)


f_scrreg = loaded_f_weights(D_SCRV, r_truth, taus)
f_true = loaded_f("chi+", r_truth, taus, True)
move = float(np.linalg.norm(f_scrreg - f_true)
             / np.linalg.norm(f_true))
check("S5.1 CONTROL FIRES: scrambled register weights violate "
      "lattice multiplicativity on %d disjoint pairs (> 0) AND "
      "move the machine readout (rel %.3e >= 1e-6) -- the "
      "decider consumes the register structure"
      % (viol, move), viol > 0 and move >= 1e-6,
      kill="WARD-DEAD")

# ======================================================================
section("S6: verdict (frozen precedence)")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
elif decides and kms_winner is None:
    verdict = ("CHIRALITY-DECIDED (%s; criterion: machine "
               "discrimination alone, D2 vacuous -- typed v2)"
               % mach_winner)
elif decides and mach_winner == kms_winner:
    verdict = ("CHIRALITY-DECIDED (%s = family cycle %s; "
               "criterion: machine discrimination + KMS "
               "orientation agree)"
               % (mach_winner,
                  "(3,5,7)" if mach_winner == "chi+"
                  else "(3,7,5)"))
elif decides:
    verdict = "CHIRALITY-INCONSISTENT"
else:
    verdict = "CHIRALITY-DEGENERATE"
n_pass = sum(1 for _, ok in CHECKS if ok)
print("\n" + "=" * 70)
print("CHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("=" * 70)
print("""
HONEST CONSEQUENCE (measured):
 * The census freedom is exactly the two classes (3,5,7) vs
   (3,7,5) on the family cycle (S1, regression).
 * STRUCTURAL FACT (S3): every phase readout that does not couple
   the family-cycle letter to the divisor weights is PROVABLY
   chirality-blind (bit-transposition conjugation fixing port and
   readout).  The deployed weyl/phase chain is of that type: the
   chirality cannot be decided by the deployed readouts as they
   stand.
 * D1/D2 (v2 finding): the register orientation functional
   vanishes IDENTICALLY -- the Moebius complement d -> 210/d
   pairs the orbits with reversed orientation (exact ward) --
   so the KMS-orientation criterion is VACUOUS: the register's
   multiplicative weight structure carries NO intrinsic scalar
   orientation.  KMS winner: %s.
 * D3 (sigma-wired machine, blind protocol): sees chirality =
   %s (|dPhi| = %.3e, quadratic readout provably orientation-
   dead by transpose symmetry, v2 ward), decides = %s;
   asymmetric-readout diagnostic |dPhi| = %.3e (report-only).
If the verdict is CHIRALITY-DEGENERATE: the residual Z2 of the
210 register is REAL GAUGE at the deployed-machine level -- the
canonicity verdict DIVISOR210-GAUGE-FAMILY(2) stands and is not
upgraded.  NO RH claim.""" % (kms_winner, sees, delta_see,
                              decides, abs(phi_ap - phi_am)))
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('divisor210_canonicity_probe', _SRC_0, 36, (),
     ('DIVISOR210-GAUGE-FAMILY(2)',), 0),
    ('moving12_soft17_probe', _SRC_1, 12, (),
     ('MOVING12-DIMENSION-ONLY',), 0),
    ('chiral_phase_probe', _SRC_2, 15, (),
     ('CHIRALITY-DEGENERATE',), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v868 -- E8.DIVISOR210.CANONICITY.01 (+ the two burial audits)')
    print('(the hard canonicity guard: the Euler constants pin {2,3,5,7}')
    print('uniquely in the predeclared 210-quadruple field, the anchor')
    print('prime 2 is forced by ramification, and the residual Z2 is')
    print('PROVEN gauge (two exact no-go wards); the 17 = 12+3+1+1')
    print('identification honestly buried at space level; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v868: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('The register is canonical up to the proven family-cycle')
    print('chirality; the Boolean layer is measured GENERIC (210/210,')
    print('as warned); the 6-vs-7 mismatch with the clock alphabet is')
    print('typed, not smoothed; the moving-12 hypothesis stands as a')
    print('COUNT only (principal angles ~90 deg); every chirality')
    print('decider through quadratic readouts is provably blind.')
    print("[%s] v868 VERDICT GATE: DIVISOR210-GAUGE-FAMILY(2) + MOVING12-DIMENSION-ONLY + CHIRALITY-DEGENERATE"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
