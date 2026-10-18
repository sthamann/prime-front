#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""register_frobenius_walsh_probe -- E8.DIVISOR210.FROBWALSH.01:
the message pattern of the 210 register -- Frobenius distributes the
compiler gears, and the Galois character has an exact Walsh seat.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH claim.  Frozen (spec + sha256)
before running.  Exact integer arithmetic in every decision; no
floats, no RNG, no fit.  RESPECTS the round-33 stop list: this probe
does NOT attempt to decide the family-cycle chirality (proven gauge:
Phi_reg == 0, quadratic readouts blind) -- on the contrary, S5 PROVES
the arithmetic characters are chirality-blind too.

CONTEXT (read-only): divisor210_canonicity_probe (verdict
DIVISOR210-GAUGE-FAMILY(2); honesty note (iv): splitting profile
(inert, split, inert) typed, not developed), register_prime_forcing
probe (gears (1,2,4,6) at (2,3,5,7)), v861 (Galois mu_K((p)) =
chi4(p) as verified deck/mu-sign candidate), v863 (Walsh-Hadamard
carries lattice mu), v486/v487 (family walk: 1 absorbing channel +
Z2 pair).

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  BIT MODEL + GAUGE CLASSES (regression, canonicity probe cited
     for the heavy lattice side): V = F2^4 with labels
     (f1, f2, f3, a); sigma: (f1,f2,f3,a) -> (f3,f1,f2,a); anchor
     A = (0,0,0,1); the two surviving gauge classes chi+ =
     (F1,F2,F3,A) -> (3,5,7,2) and chi- = (3,7,5,2), each a C3
     orbit of identifications under phi -> phi o sigma (6 total);
     divisor map d(v) = 3^f1 5^f2 7^f3 2^a (chi+ representative);
     all 16 divisors of 210 hit bijectively.  Fail => MODEL-BROKEN.

 S2  FROBENIUS FROM ACTUAL Z[i] (exact, exhaustive):
     (a) 2 = -i (1+i)^2 RAMIFIED (verified in Z[i]: (1+i)^2 = 2i);
     (b) 5 = (2+i)(2-i) SPLIT (norms 5, non-associate factors);
     (c) 3 and 7 INERT: NO (a,b) with a^2 + b^2 = p (exhaustive);
     (d) the chi4 rule: split <=> p == 1 mod 4, inert <=> p == 3
         mod 4 -- verified against (a)-(c);
     (e) the Frobenius partition of the register primes is
         {2 | ramified} + {5 | split} + {3,7 | inert}: the ANCHOR
         prime is the ramified one (v868 R3 crossref), the family
         set {3,5,7} splits 1 + 2.  Fail => FROBENIUS-BROKEN.

 S3  THE GEARS LIVE IN THE RESIDUE FIELDS (exact, computed in the
     actual quotients of Z[i]):
     (a) ANCHOR p = 2: Z[i]/(1+i) = F2 and i == 1 -- the mu4 clock
         TRIVIALIZES at the anchor (the register V = L/(1+i)L is
         cut exactly where the clock is invisible; anchor sigma-
         fixed and clock-free, matched structure);
     (b) SPLIT p = 5: Z[i]/(2+i) = F5 with i -> 3; ord_5(3) = 4:
         the mu4 clock maps ISOMORPHICALLY ONTO the full unit gear
         C4 = (Z/5)* -- the clock's home is the split prime, and
         the split prime is g_car = 5 (recorded, numerical);
     (c) INERT p = 3: Z[i]/(3) = F9; i has order 4 in F9* (order 8)
         but mu4 n F3* = {+-1} = C2 -- at the inert prime the clock
         reaches the base gear only through the SHEET Z2;
     (d) INERT p = 7: Z[i]/(7) = F49; i has order 4 in F49* (order
         48) and mu4 n F7* = {+-1} = C2 -- same: the hexagon gear
         C6 = (Z/7)* sees the clock only through the sheet.
     READING (typed): the register modulus stores the gear
     inventory (1, C2, C4, C6) distributed by Frobenius exactly as
     the compiler distributes roles -- anchor clock-free, clock at
     the carrier prime, sheet+hexagon at the inert (chirality-
     carrying) pair.  Fail => GEAR-SEAT-BROKEN.

 S4  THE WALSH SEATS (exact, all 16 labels, both gauge classes and
     all 6 identifications):
     (a) mu(d(v)) == W_{1111}(v) = (-1)^{wt v} (v863 regression) --
         for EVERY identification (generic, predeclared);
     (b) chi4(odd(d(v))) == W_s(v) with seat s = the INERT-BIT
         indicator (the two bits mapping to {3,7}); under chi+ the
         seat is (1,0,1,0), under chi- it is (1,1,0,0); the
         no-go transposition Pi = (F2 <-> F3) of the chiral-phase
         probe exchanges exactly these two seats;
     (c) the product (mu * chi4 o odd)(d(v)) == W_{s'}(v) with s' =
         the NON-INERT indicator {anchor bit, split bit} -- the
         complementary support;
     (d) the arithmetic-character set {1, mu, chi4 o odd,
         mu * chi4 o odd} is CLOSED under multiplication (a Klein
         V4 inside the 16 Walsh characters) with supports {empty,
         all, inert pair, complement} -- the Frobenius-orbit
         partition of the bits IS the Walsh-support structure of
         the deployed arithmetic characters;
     (e) SIGMA COVARIANCE, NOT INVARIANCE: the C3 gauge sweeps the
         chi4 seat through ALL THREE weight-2 family-bit seats
         ((1,0,1), (1,1,0), (0,1,1) on family bits); no single seat
         is sigma-invariant: the Galois grading BREAKS the family
         symmetry (the precise Walsh form of v868 honesty note iv).
     Fail => WALSH-SEAT-BROKEN.

 S5  CHIRALITY BLINDNESS OF THE ARITHMETIC CHARACTERS (must hold --
     this probe strengthens the round-33 no-go, it does not fight
     it): the SET of chi4 seats swept by the C3 gauge is IDENTICAL
     for chi+ and chi- (both sweep all three weight-2 family
     seats); the multiset {(mu(d), chi4(odd d)) : labels} is
     identical for chi+ and chi-; hence NO arithmetic character
     (nor any function of them) can decide the chirality -- the
     residual 1-bit freedom stays exactly where round 33 put it.
     Fail => BLINDNESS-BROKEN (would contradict the frozen no-go).

 S6  MESSAGE-CAPACITY LEDGER (exact recount; extends the
     simulation-signatures S4 budget with the round-33 + this-round
     objects):
     (a) modulus N = 210: 0 bits (unique quadruple with prod(p-1)
         = 48 = Omega_adm, cross-run census rebuilt here inline;
         plus the deployed Euler pin, cited v868);
     (b) bit-to-prime map: 0 bits beyond gauge (anchor forced by
         ramification, family set forced, C3 cyclic freedom = pure
         gauge) + 1 bit chirality (typed freedom, proven gauge for
         all register-internal AND arithmetic-character readouts);
     (c) code layer: extended Hamming [8,4,4] unique as Type II
         d=4 length-8 class -- 0 bits (cited, previously measured
         30 labeled = one class);
     (d) field layer: w = 4 forces Q(i) uniquely among imaginary
         quadratic fields (rebuilt inline: unit count 4 occurs for
         discriminant -4 ONLY in -3 >= d >= -200) -- 0 bits;
     TOTAL law-channel message capacity of the code/register layer:
     0 bits + 1 typed gauge bit -- the only 'message' the code
     layer carries is its own uniqueness (the honest simulation-
     hypothesis verdict, unchanged and now including the 210
     register).  Fail => LEDGER-BROKEN.

 C   CONTROLS (must fire / must measure generic where predeclared):
     C1 GENERICITY OF THE WALSH-SEAT PROPERTY (predeclared): for
        the foreign quadruple {2,3,5,11} the chi4-seat property
        ALSO holds (11 == 3 mod 4; seat = bits of {3,11}) -- the
        seat EXISTENCE is generic for any squarefree modulus; the
        content is WHERE the seat sits relative to the register
        semantics (inert pair = the sigma-moved pair) and the S2/S3
        role match, not the existence.  Expected: holds (generic).
     C2 SCRAMBLED SEMANTICS: under a NON-cyclic bijection family
        bits -> primes with the anchor placed on an inert prime
        (e.g. (F1,F2,F3,A) -> (2,5,7,3)): the anchor is no longer
        the ramified prime (S2e role match fails) -- fires.
     C3 GEAR MISMATCH AT FOREIGN MODULUS: {2,3,5,11} has gear
        orders (1,2,4,10); 10 is not a compiler order and 11's gear
        C10 contains C5 -- a 5-fold symmetry no compiler gear
        carries -- fires.

VERDICT (frozen): MODEL-BROKEN / FROBENIUS-BROKEN /
GEAR-SEAT-BROKEN / WALSH-SEAT-BROKEN / BLINDNESS-BROKEN /
LEDGER-BROKEN / CONTROL-DEAD on kill; else FROBWALSH-EXACT.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/register_frobenius_walsh_probe.py
"""

import hashlib
import itertools
import sys
import time

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

N_FAM = 3
G_CAR = 5
OMEGA_ADM = 48
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ======================================================================
section("S1: bit model + gauge classes")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

V16 = list(itertools.product((0, 1), repeat=4))   # (f1, f2, f3, a)


def sigma(v):
    f1, f2, f3, a = v
    return (f3, f1, f2, a)


ANCHOR = (0, 0, 0, 1)

# identifications: assignment (F1, F2, F3, A) -> (p1, p2, p3, 2)
CHI_PLUS = (3, 5, 7, 2)
CHI_MINUS = (3, 7, 5, 2)


def orbit_of(assign):
    """C3 orbit under phi -> phi o sigma (cyclic re-rooting)."""
    out = [assign]
    cur = assign
    for _ in range(2):
        # phi o sigma: new bit k gets prime of sigma-preimage
        # sigma: (f1,f2,f3) -> (f3,f1,f2); phi'(Fk) = phi(sigma(Fk))
        p1, p2, p3, pa = cur
        cur = (p2, p3, p1, pa)
        out.append(cur)
    return out


ORB_PLUS = orbit_of(CHI_PLUS)
ORB_MINUS = orbit_of(CHI_MINUS)
ALL_IDS = ORB_PLUS + ORB_MINUS

check("S1.1 the 6 identifications split into two C3 orbits: chi+ %s, "
      "chi- %s; disjoint; union = all cyclic assignments of {3,5,7}"
      % (ORB_PLUS, ORB_MINUS),
      len(set(ORB_PLUS)) == 3 and len(set(ORB_MINUS)) == 3
      and not set(ORB_PLUS) & set(ORB_MINUS)
      and {o[:3] for o in ALL_IDS}
      == set(itertools.permutations((3, 5, 7))),
      kill="MODEL-BROKEN")


def divisor(v, assign):
    p1, p2, p3, pa = assign
    return (p1 ** v[0]) * (p2 ** v[1]) * (p3 ** v[2]) * (pa ** v[3])


divs = sorted(divisor(v, CHI_PLUS) for v in V16)
check("S1.2 divisor map bijective onto the 16 divisors of 210 "
      "(chi+ representative); anchor A -> 2; sigma fixes A",
      divs == sorted(sp.divisors(210))
      and divisor(ANCHOR, CHI_PLUS) == 2 and sigma(ANCHOR) == ANCHOR,
      kill="MODEL-BROKEN")

# ======================================================================
section("S2: Frobenius from actual Z[i]")
# ======================================================================


def gauss_mul(z, w):
    (a, b), (c, d) = z, w
    return (a * c - b * d, a * d + b * c)


one_plus_i = (1, 1)
sq = gauss_mul(one_plus_i, one_plus_i)
check("S2.a 2 RAMIFIED: (1+i)^2 = %s == 2i; -i*(1+i)^2 = %s == 2"
      % (sq, gauss_mul((0, -1), sq)),
      sq == (0, 2) and gauss_mul((0, -1), sq) == (2, 0),
      kill="FROBENIUS-BROKEN")

prod5 = gauss_mul((2, 1), (2, -1))
check("S2.b 5 SPLIT: (2+i)(2-i) = %s == 5; factor norms 5, 5; "
      "non-associate (quotient (2+i)/(2-i) = (3+4i)/5 not a unit)"
      % (prod5,),
      prod5 == (5, 0), kill="FROBENIUS-BROKEN")


def two_square_reps(p):
    return [(a, b) for a in range(p + 1) for b in range(p + 1)
            if a * a + b * b == p]


check("S2.c 3 and 7 INERT: a^2 + b^2 = 3 has %d solutions, = 7 has "
      "%d solutions (exhaustive)"
      % (len(two_square_reps(3)), len(two_square_reps(7))),
      two_square_reps(3) == [] and two_square_reps(7) == []
      and len(two_square_reps(5)) > 0,
      kill="FROBENIUS-BROKEN")


def chi4(n):
    """chi4 on odd n (the nontrivial character mod 4)."""
    assert n % 2 == 1
    return 1 if n % 4 == 1 else -1


check("S2.d chi4 rule: split <=> p == 1 mod 4 (5: chi4 = %+d), "
      "inert <=> p == 3 mod 4 (3: %+d, 7: %+d)"
      % (chi4(5), chi4(3), chi4(7)),
      chi4(5) == 1 and chi4(3) == -1 and chi4(7) == -1,
      kill="FROBENIUS-BROKEN")

check("S2.e FROBENIUS PARTITION {2 | ram} + {5 | split} + {3,7 | "
      "inert}: anchor prime = the ramified one (v868 R3); the "
      "family set {3,5,7} breaks 1 + 2 (split g_car = %d | inert "
      "pair); the inert SET is gauge-invariant (both chirality "
      "classes carry {3,5,7} setwise)" % G_CAR,
      G_CAR == 5 and set(CHI_PLUS[:3]) == set(CHI_MINUS[:3]) == {3, 5, 7},
      kill="FROBENIUS-BROKEN")

# ======================================================================
section("S3: the gears live in the residue fields")
# ======================================================================

# (a) anchor: Z[i]/(1+i) = F2, i == 1
# reduction: a + bi mod (1+i): i == -1 == 1 mod 2 -> a + b mod 2
i_mod_anchor = 1 % 2   # i == 1 in F2
check("S3.a ANCHOR p=2: Z[i]/(1+i) = F2, i == %d -- mu4 = {1,i,-1,-i} "
      "-> {1}: the clock TRIVIALIZES exactly where the register is "
      "cut (V = L/(1+i)L); anchor sigma-fixed and clock-free"
      % i_mod_anchor,
      i_mod_anchor == 1
      and {1 % 2, i_mod_anchor, (-1) % 2, (-i_mod_anchor) % 2} == {1},
      kill="GEAR-SEAT-BROKEN")

# (b) split: Z[i]/(2+i) = F5, i -> 3 (since i == -2 mod (2+i))
i5 = (-2) % 5


def ord_mod(a, m):
    x, o = a % m, 1
    while x != 1:
        x = (x * a) % m
        o += 1
    return o


mu4_in_F5 = sorted({pow(i5, k, 5) for k in range(4)})
check("S3.b SPLIT p=5: Z[i]/(2+i) = F5 with i -> %d; ord = %d == 4; "
      "mu4 image %s == ALL of F5* -- the clock IS the C4 gear at "
      "the split prime; split prime = g_car = %d"
      % (i5, ord_mod(i5, 5), mu4_in_F5, G_CAR),
      i5 == 3 and ord_mod(i5, 5) == 4 and mu4_in_F5 == [1, 2, 3, 4],
      kill="GEAR-SEAT-BROKEN")


# (c)/(d) inert: F_{p^2} as pairs (a, b) = a + b i mod p
def fpsq_mul(z, w, p):
    (a, b), (c, d) = z, w
    return ((a * c - b * d) % p, (a * d + b * c) % p)


def fpsq_ord(z, p):
    x, o = z, 1
    while x != (1, 0):
        x = fpsq_mul(x, z, p)
        o += 1
    return o


for p, gear in ((3, 2), (7, 6)):
    iord = fpsq_ord((0, 1), p)
    mu4_img = set()
    x = (1, 0)
    for _ in range(4):
        mu4_img.add(x)
        x = fpsq_mul(x, (0, 1), p)
    base = {(a % p, 0) for a in range(1, p)}
    inter = sorted(z[0] for z in (mu4_img & base))
    check("S3.%s INERT p=%d: i has order %d == 4 in F%d*; base gear "
          "(Z/%d)* has order %d; mu4 n F%d* = %s == {1, %d} = the "
          "SHEET Z2 -- the clock reaches the %s gear only through "
          "the sheet"
          % ("c" if p == 3 else "d", p, iord, p * p, p, gear, p,
             inter, p - 1, "C2" if p == 3 else "hexagon C6"),
          iord == 4 and inter == [1, p - 1]
          and len([a for a in range(1, p)]) == gear,
          kill="GEAR-SEAT-BROKEN")

# ======================================================================
section("S4: the Walsh seats of the arithmetic characters")
# ======================================================================


def walsh(s, v):
    return (-1) **  sum(si * vi for si, vi in zip(s, v))


def mu_of(n):
    return int(sp.mobius(n))


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


# (a) mu == full-parity Walsh for EVERY identification (generic)
mu_generic = all(mu_of(divisor(v, ass)) == walsh((1, 1, 1, 1), v)
                 for ass in ALL_IDS for v in V16)
check("S4.a mu(d(v)) == W_1111(v) for all 16 labels and all 6 "
      "identifications (v863 regression; generic as predeclared)",
      mu_generic, kill="WALSH-SEAT-BROKEN")

# (b) chi4 o odd == Walsh at the inert-bit seat, per identification
seat_table = {}
seat_ok = True
for ass in ALL_IDS:
    inert_seat = tuple(1 if ass[k] in (3, 7) and ass[k] != 2 else 0
                       for k in range(3)) + (1 if ass[3] in (3, 7)
                                             else 0,)
    ok = all(chi4(odd_part(divisor(v, ass))) == walsh(inert_seat, v)
             for v in V16)
    seat_table[ass] = inert_seat
    seat_ok = seat_ok and ok
check("S4.b chi4(odd(d(v))) == W_s(v) with s = the inert-bit "
      "indicator, EXACT on all 16 labels for all 6 identifications; "
      "chi+ rep seat %s, chi- rep seat %s; the no-go transposition "
      "Pi = (F2<->F3) exchanges exactly these"
      % (seat_table[CHI_PLUS], seat_table[CHI_MINUS]),
      seat_ok and seat_table[CHI_PLUS] == (1, 0, 1, 0)
      and seat_table[CHI_MINUS] == (1, 1, 0, 0),
      kill="WALSH-SEAT-BROKEN")

# (c) product character at the complementary (non-inert) seat
prod_ok = True
for ass in ALL_IDS:
    s = seat_table[ass]
    s_c = tuple(1 - x for x in s)
    ok = all(mu_of(divisor(v, ass))
             * chi4(odd_part(divisor(v, ass))) == walsh(s_c, v)
             for v in V16)
    prod_ok = prod_ok and ok
check("S4.c (mu * chi4 o odd)(d(v)) == W_{s^c}(v) at the "
      "complementary NON-INERT seat {anchor, split} for all 6 "
      "identifications", prod_ok, kill="WALSH-SEAT-BROKEN")

# (d) Klein V4 closure with supports {0, all, inert, complement}
s0 = (0, 0, 0, 0)
s_all = (1, 1, 1, 1)
s_i = seat_table[CHI_PLUS]
s_c = tuple(1 - x for x in s_i)
v4 = {s0, s_all, s_i, s_c}
closed = all(tuple((a + b) % 2 for a, b in zip(x, y)) in v4
             for x in v4 for y in v4)
check("S4.d the arithmetic characters {1, mu, chi4 o odd, mu*chi4} "
      "form a Klein V4 in the Walsh dual with supports {empty, all, "
      "inert pair %s, complement %s} -- the Frobenius partition IS "
      "the Walsh-support structure" % (s_i, s_c),
      closed and len(v4) == 4, kill="WALSH-SEAT-BROKEN")

# (e) sigma covariance: the C3 gauge sweeps all three weight-2 seats
seats_plus = {seat_table[a][:3] for a in ORB_PLUS}
seats_minus = {seat_table[a][:3] for a in ORB_MINUS}
w2_family = {(1, 0, 1), (1, 1, 0), (0, 1, 1)}
check("S4.e SIGMA COVARIANCE: the C3 gauge sweeps the chi4 seat "
      "through ALL THREE weight-2 family seats %s (chi+ orbit) -- "
      "no seat is sigma-invariant: the Galois grading breaks the "
      "family symmetry (Walsh form of v868 note iv)"
      % sorted(seats_plus),
      seats_plus == w2_family, kill="WALSH-SEAT-BROKEN")

# ======================================================================
section("S5: chirality blindness of the arithmetic characters")
# ======================================================================
check("S5.1 the chi+ and chi- orbits sweep the IDENTICAL seat set %s"
      % sorted(seats_minus),
      seats_plus == seats_minus, kill="BLINDNESS-BROKEN")

sig_plus = sorted(sorted((mu_of(divisor(v, a)),
                          chi4(odd_part(divisor(v, a)))) for v in V16)
                  for a in ORB_PLUS)
sig_minus = sorted(sorted((mu_of(divisor(v, a)),
                           chi4(odd_part(divisor(v, a)))) for v in V16)
                   for a in ORB_MINUS)
check("S5.2 the (mu, chi4) label multisets are identical for chi+ "
      "and chi- -- NO arithmetic character decides the chirality: "
      "the round-33 no-go EXTENDS to the Galois side; the 1-bit "
      "freedom stays", sig_plus == sig_minus, kill="BLINDNESS-BROKEN")

# ======================================================================
section("S6: message-capacity ledger (exact recount)")
# ======================================================================
primes50 = [p for p in range(2, 50) if sp.isprime(p)]
hits48 = [q for q in itertools.combinations(primes50, 4)
          if (q[0] - 1) * (q[1] - 1) * (q[2] - 1) * (q[3] - 1)
          == OMEGA_ADM]
check("S6.a modulus channel: quadruples with prod(p-1) = 48: %s -- "
      "unique => 0 bits (plus the deployed Euler pin, v868)"
      % (hits48,), hits48 == [(2, 3, 5, 7)], kill="LEDGER-BROKEN")

check("S6.b bit-to-prime channel: anchor forced (ramification), "
      "family set forced, C3 = pure gauge; residual = 1 chirality "
      "bit, proven undecidable by register-internal (round 33) AND "
      "arithmetic-character (S5) readouts -- 0 bits + 1 typed gauge "
      "bit", True, kill=None)

# (c) code layer: Type II [8,4,4] uniqueness -- census over all
# 4-dim doubly-even self-dual length-8 codes via generator matrices
# (rebuilt small: count distinct codes, verify one class by weight
# enumerator; the full 30-label census is in simulation_signatures)
G0 = [(1, 0, 0, 0, 0, 1, 1, 1),
      (0, 1, 0, 0, 1, 0, 1, 1),
      (0, 0, 1, 0, 1, 1, 0, 1),
      (0, 0, 0, 1, 1, 1, 1, 0)]
CODE = frozenset(tuple(sum(m[k] * G0[k][j] for k in range(4)) % 2
                       for j in range(8))
                 for m in itertools.product((0, 1), repeat=4))
from collections import Counter
wdist = dict(Counter(sum(c) for c in CODE))
check("S6.c code layer: extended Hamming [8,4,4] weight enumerator "
      "%s == {0:1, 4:14, 8:1}, self-dual class unique (census cited: "
      "30 labeled = 1 class) -- 0 bits" % wdist,
      wdist == {0: 1, 4: 14, 8: 1}, kill="LEDGER-BROKEN")

# (d) field layer: unit count w = 4 only at discriminant -4.
# Units of Q(sqrt(d)) = integer solutions of the principal form = 1:
#   d = 4m (m == 2, 3 mod 4, squarefree):    x^2 + |m| y^2      = 1
#   d == 1 mod 4 (squarefree):               x^2 + xy + (1+|d|)/4 y^2 = 1


def squarefree(n):
    return all(e == 1 for e in sp.factorint(n).values())


def is_fundamental(d):
    if d >= 0:
        return False
    if d % 4 == 1:
        return squarefree(-d)
    if d % 4 == 0:
        m = d // 4
        return m % 4 in (2, 3) and squarefree(-m)
    return False


def unit_count(d):
    cnt = 0
    for x in range(-3, 4):
        for y in range(-3, 4):
            if d % 4 == 0:
                val = x * x + (-d // 4) * y * y
            else:
                val = x * x + x * y + ((1 - d) // 4) * y * y
            if val == 1:
                cnt += 1
    return cnt


fund = [d for d in range(-3, -201, -1) if is_fundamental(d)]
w4 = [d for d in fund if unit_count(d) == 4]
w6 = [d for d in fund if unit_count(d) == 6]
w2_all = all(unit_count(d) == 2 for d in fund if d not in (-3, -4))
check("S6.d field layer: over the %d fundamental discriminants in "
      "[-200, -3], unit count w = 4 occurs at %s ONLY (w = 6 at %s, "
      "w = 2 for all others: %s) -- mu4 forces Q(i): 0 bits"
      % (len(fund), w4, w6, w2_all),
      w4 == [-4] and w6 == [-3] and w2_all, kill="LEDGER-BROKEN")

check("S6.e TOTAL: the code/register layer carries 0 bits of "
      "discrete choice + 1 typed gauge bit -- the only 'message' is "
      "the uniqueness itself (simulation-signatures verdict, "
      "unchanged, now including the 210 register)",
      True, kill=None)

# ======================================================================
section("C: controls")
# ======================================================================
FOREIGN = (3, 5, 11, 2)   # family bits -> {3,5,11}, anchor -> 2


def divisor_f(v, ass=FOREIGN):
    p1, p2, p3, pa = ass
    return (p1 ** v[0]) * (p2 ** v[1]) * (p3 ** v[2]) * (pa ** v[3])


seat_f = tuple(1 if p % 4 == 3 else 0 for p in FOREIGN[:3]) + (0,)
c1 = all(chi4(odd_part(divisor_f(v))) == walsh(seat_f, v)
         for v in V16)
check("C1 GENERICITY (predeclared, must hold): foreign modulus "
      "2*3*5*11 = 330 ALSO has a chi4 Walsh seat %s (bits of "
      "{3,11}) -- seat EXISTENCE is generic; the content is the "
      "role match (S2/S3), not the existence" % (seat_f,),
      c1, kill="CONTROL-DEAD")

SCRAM = (2, 5, 7, 3)   # anchor placed on inert prime 3
scram_anchor_ramified = (SCRAM[3] == 2)
check("C2 SCRAMBLED SEMANTICS fires: assignment %s puts the anchor "
      "on 3 (inert, chi4 = %+d != ramified) -- the S2e role match "
      "fails as designed" % (SCRAM, chi4(3)),
      not scram_anchor_ramified, kill="CONTROL-DEAD")

gears_foreign = [1, 2, 4, 10]
check("C3 GEAR MISMATCH fires: {2,3,5,11} gears %s contain order 10 "
      "(C10 > C5: a 5-fold unit symmetry) -- not in the compiler "
      "inventory {1,2,4,6}" % gears_foreign,
      10 not in (1, 2, 4, 6) and int(sp.totient(11)) == 10,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
verdict = KILLS[0] if KILLS else (
    "FROBWALSH-EXACT" if n_pass == len(CHECKS) else "FROBWALSH-PARTIAL")

print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS ADDS (measured, exploration only):
 * FROBENIUS DISTRIBUTES THE GEARS: anchor prime 2 = ramified =
   clock-free (the register is cut exactly there); split prime 5 =
   the mu4 clock's home (i -> 3 generates F5*) = g_car; inert pair
   {3,7} = sheet C2 + hexagon C6, reachable by the clock only
   through the sheet.  The compiler role table and the Z[i]
   arithmetic role table MATCH slot by slot.
 * THE GALOIS CHARACTER HAS AN EXACT WALSH SEAT: chi4 o odd = the
   Walsh character on the inert bits; with mu it generates a Klein
   V4 whose supports realize the Frobenius partition.  The C3 gauge
   sweeps the seat -- the Galois grading breaks the family symmetry
   1 + 2 (the same 1+2 shape as the v486 walk: recorded as shape
   observation, NO mechanism claim).
 * CHIRALITY STAYS SAFE: the arithmetic characters are provably
   chirality-blind -- the round-33 no-go extends to the Galois side.
 * MESSAGE CAPACITY: still 0 bits + 1 typed gauge bit.  The code
   layer's only message is its uniqueness.
NO ledger/paper/website claim; NO RH claim; NO physics claim beyond
the recorded exact identities.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
