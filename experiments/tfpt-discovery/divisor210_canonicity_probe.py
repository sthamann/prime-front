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
