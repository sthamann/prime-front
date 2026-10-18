#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""register_quadratic_code_probe -- E8.DIVISOR210.QUADCODE.01:
the quadratic-field / genus / QR-code layer of the 210 register.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH claim.  Frozen (spec + sha256)
before running.  Exact integer arithmetic in every decision (reduced
binary quadratic forms, F2 polynomial algebra, lattice counts); the
ONLY floats are the 50-digit mpmath Gauss-sum witnesses in S3, typed
as numeric witnesses of a cited classical theorem, never a decision.

CONTEXT (read-only): register_prime_forcing_probe (210 = rad|W(E8)|,
gears (1,2,4,6), phi-tower (2,8,48)), register_frobenius_walsh_probe
(Frobenius partition {2|ram} {5|split} {3,7|inert}, chi4 Walsh seat),
v533 (the second compiler field -7), v219/v313 (icosian/golden atoms
already deployed -- crossref targets, not rebuilt).

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  THE DISCRIMINANT MAP (exact): each register prime gets its
     PRIME DISCRIMINANT: 2 -> -4 (canonical: -4 = disc Q(i), the
     very field whose ramified prime cuts the register V=L/(1+i)L;
     the alternatives +8/-8 are recorded as the 2-adic ambiguity,
     typed), 3 -> -3, 5 -> +5, 7 -> -7 (p* = chi4(p) p for odd p).
     The label map D(v) = prod_{bits} p* sends the 16 register
     labels BIJECTIVELY to 15 fundamental discriminants + 1
     (trivial label); sign(p*) = chi4(p) -- the discriminant sign
     pattern IS the Frobenius/Walsh-seat pattern of the previous
     probe; |D(v)| = odd(d(v)) * (4 if anchor bit else 1), i.e.
     d(v) on anchor-free labels and 2 d(v) on anchor labels (-4
     REPLACES the prime 2, contributing 2^2).
     V2 AMENDMENT (honest, after run 1 = 17/19): the v1 magnitude
     claim read "d or 4d" -- a bookkeeping slip (it forgot that d
     already contains the factor 2); corrected to the identity
     above; the C3 control below was re-based on the unit-count
     pin for the same reason.  No mathematical layer changed; the
     v1 fails were spec arithmetic, not object behaviour.
     Any fail => DISCMAP-BROKEN.

 S2  THE FOUR PRIME FIELDS AND THEIR COMPILER ROLES (exact):
     (a) Q(i) (D = -4): unit count w = 4 = |mu4| (the clock);
     (b) Q(sqrt-3) (D = -3): w = 6 (Eisenstein) -- and the census
         over ALL fundamental discriminants in [-200, -3] shows
         {-3, -4} are the ONLY imaginary quadratic fields with
         w > 2: the exceptional-unit pair (4, 6) is EXACTLY the
         compiler glue-order pair (|mu4|, |R+(A3)|) -- the third
         appearance of (4,6) after the phi-ratios and the unit
         gears at (5,7) (recorded; classical beyond -200, cited);
     (c) Q(sqrt5) (D = +5): the UNIQUE real prime field = the
         split/carrier prime g_car; its fundamental unit is the
         GOLDEN RATIO phi = (1+sqrt5)/2 with norm -1 (minimality
         by exhaustive |x^2-5y^2| = 4 search) -- the icosian base
         field sits on the carrier bit (crossref v219/v313, typed);
     (d) Q(sqrt-7) (D = -7): the deployed second compiler field
         (v533 crossref, class number 1, Heegner member).
     All four prime fields have h = 1 (computed via reduced
     forms / cycles, not cited).  Any fail => FIELDS-BROKEN.

 S3  GAUSS SUMS CARRY THE CLOCK PHASE (50-digit witnesses of the
     cited Gauss sign theorem; no decision rests on floats alone):
     g_p = sum_a (a|p) e^{2 pi i a / p}: g_3 = i sqrt3, g_5 =
     sqrt5, g_7 = i sqrt7 (each to < 1e-40): the mu4 generator i
     is the Gauss-sum phase EXACTLY at the inert pair {3,7} and
     absent at the split prime 5 -- and g_p^2 = p* (< 1e-40), so
     the S1 discriminant map is the GAUSS-SUM-SQUARE map:
     D(v) = prod g_p^2 over the set bits.  Any fail =>
     GAUSS-BROKEN.

 S4  THE SINGLE-GENUS LAW (the headline; exact, all 16 labels):
     h+(D(v)) == 2^(wt(v) - 1) for every nonzero label (narrow
     class number; imaginary labels by reduced positive-definite
     form census, real labels by reduced indefinite form CYCLE
     census under the rho neighbour step; trivial label h = 1).
     Consequences, all measured: (i) ONE CLASS PER GENUS on the
     whole register -- every class group is an ELEMENTARY ABELIAN
     2-GROUP (the class groups are register-shaped: pure F2, no
     hidden odd part anywhere); (ii) the genus characters -- i.e.
     the Legendre/Walsh characters of the previous probe -- decide
     representability COMPLETELY: the quadratic-form layer of the
     register carries ZERO information beyond the register's own
     characters (the message-capacity reading; Gauss genus theory
     cited for character-completeness, the class counts computed);
     (iii) ambiguity witness: for the imaginary labels every
     reduced form is ambiguous (b = 0 or a = b or a = c) --
     exponent <= 2 verified composition-free.  Any fail =>
     FORMS-BROKEN (a mismatch would itself be a finding: record).

 S5  THE PRIMORIAL-IDONEAL LADDER (third ladder-end, exact):
     n is idoneal (Euler) iff every class of disc -4n has order
     <= 2, tested composition-free via the all-reduced-forms-
     ambiguous criterion.  MEASURED: n = 1, 2, 6, 30, 210 (the
     primorial ladder INCLUDING the register modulus) are ALL
     idoneal; n = 2310 = 11# is NOT (a non-ambiguous reduced form
     of disc -9240 exhibited).  The primorial-idoneal ladder ends
     at 210 -- the SAME endpoint as the Coxeter ladder (previous
     probe S6) and one rung past nothing: Euler's list (65
     numbers, largest 1848, conjecturally complete / complete
     under GRH, cited [C]) contains 210 but no primorial beyond.
     Any fail => IDONEAL-BROKEN.

 S6  THE QR-CODE SEAT OF 7 (the code find; exact F2 algebra):
     (a) a binary quadratic-residue code of length p exists iff 2
         is a QR mod p (p == +-1 mod 8): among the register primes
         {3, 5, 7} EXACTLY 7 qualifies (squares mod p exhaustive;
         cross-check: (x^3+1)/(x+1) = x^2+x+1 and (x^5+1)/(x+1) =
         x^4+x^3+x^2+x+1 are IRREDUCIBLE over F2 -- no QR split --
         while (x^7+1)/(x+1) splits into the two QR cubics);
     (b) the QR code at 7: g(x) = x^3+x+1 (the QR factor), cyclic
         [7,4,3] (16 words, min weight 3 by full enumeration);
         extended by parity: [8,4,4], doubly even, SELF-DUAL,
         weight enumerator {0:1, 4:14, 8:1} == the deployed
         extended Hamming class (uniqueness cited from the
         previously measured 30-labeled/1-class census);
     (c) Construction A over the extended QR code: the integer
         lattice {x in Z^8 : x mod 2 in C} has EXACTLY 240 vectors
         of norm 4 (direct census over {-2..2}^8) = the E8 root
         count: THE E8 BINARY SKELETON IS THE QUADRATIC-RESIDUE
         CODE AT THE REGISTER PRIME 7 -- the weld prime (the 7#
         rung, the hexagon gear) is the QR-code prime;
     (d) THE NEXT QR RUNG EXISTS AND IS NOT DEPLOYED: p = 23
         (next p == -1 mod 8): (x^23+1)/(x+1) factors into two
         degree-11 QR polynomials (found by exhaustive division);
         the cyclic [23,12] code extended by parity has weight
         enumerator {0:1, 8:759, 12:2576, 16:759, 24:1} == the
         BINARY GOLAY CODE (full 4096-word enumeration) -- the
         rung that would lead to Leech/Lambda24 exists in the
         mathematics and is absent from the compiler: the fourth
         ladder-end statement, typed as structural observation.
     Any fail => QRCODE-BROKEN.

 C   CONTROLS:
     C1 IDONEALITY IS NOT UNIQUE TO THE DEPLOYED QUADRUPLE
        (honesty, measured either way): the foreign top
        discriminant -660 ({2,3,5,11}) is tested by the same
        ambiguity criterion and the result RECORDED (165 is on
        Euler's list, so all-ambiguous is EXPECTED: the selective
        content of this probe is the CONJUNCTION with the previous
        pins, never idoneality alone).
     C2 QR-CODE ABSENCE fires at 3 and 5 (S6a irreducibility).
     C3 THE 2-ADIC AMBIGUITY typed (v2): +8 and -8 are also prime
        discriminants at 2 (Q(sqrt2), Q(sqrt-2): 2 ramifies in
        all three); the canonical choice -4 is FORCED twice over:
        (i) -4 = disc Q(i), the very field of the register cut
        V = L/(1+i)L; (ii) among {-4, +8, -8} ONLY -4 carries the
        clock -- w(-4) = 4 = |mu4|, w(-8) = 2, and Q(sqrt2) is
        real (infinite units, no finite clock at all); measured.

VERDICT (frozen): DISCMAP-BROKEN / FIELDS-BROKEN / GAUSS-BROKEN /
FORMS-BROKEN / IDONEAL-BROKEN / QRCODE-BROKEN / CONTROL-DEAD on
kill; else QUADCODE-EXACT.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/register_quadratic_code_probe.py
"""

import hashlib
import itertools
import sys
import time
from math import isqrt

import mpmath
import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

MU4_ORDER = 4
RPLUS_A3 = 6
G_CAR = 5
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
# exact form-class machinery
# ======================================================================

def is_fundamental(d):
    if d == 1:
        return True   # trivial label convention
    if d % 4 == 1:
        return sp.factorint(abs(d)) and all(
            e == 1 for e in sp.factorint(abs(d)).values())
    if d % 4 == 0:
        m = d // 4
        return m % 4 in (2, 3) and all(
            e == 1 for e in sp.factorint(abs(m)).values())
    return False


def reduced_forms_neg(D):
    """all reduced positive-definite forms of discriminant D < 0"""
    assert D < 0 and D % 4 in (0, 1)
    forms = []
    amax = isqrt(-D // 3)
    for a in range(1, amax + 1):
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if b < 0 and (a == c or -b == a):
                continue   # boundary convention: b >= 0 there
            forms.append((a, b, c))
    return forms


def h_neg(D):
    return len(reduced_forms_neg(D))


def all_ambiguous_neg(D):
    return all(b == 0 or a == b or a == c
               for a, b, c in reduced_forms_neg(D))


def reduced_forms_pos(D):
    """all reduced indefinite forms of nonsquare discriminant D > 0:
    0 < b < sqrt(D) and sqrt(D) - b < 2|a| < sqrt(D) + b"""
    assert D > 0 and isqrt(D) ** 2 != D and D % 4 in (0, 1)
    fs = isqrt(D)
    forms = []
    for b in range(1, fs + 1):
        if (D - b) % 2:
            continue
        for aa in range(1, fs + b):        # aa = 2|a|
            if aa % 2:
                continue
            # sqrt(D) - b < aa  <=>  (aa + b)^2 > D
            if (aa + b) ** 2 <= D:
                continue
            # aa < sqrt(D) + b  <=>  aa <= b or (aa - b)^2 < D
            if aa > b and (aa - b) ** 2 >= D:
                continue
            a2 = aa // 2
            for a in (a2, -a2):
                if (b * b - D) % (4 * a):
                    continue
                c = (b * b - D) // (4 * a)
                forms.append((a, b, c))
    return forms


def rho_step(form, D):
    """the reduction/neighbour step on reduced indefinite forms"""
    a, b, c = form
    fs = isqrt(D)
    m = 2 * abs(c)
    lo = fs - m + 1                       # b' in [fs - m + 1, fs]
    r = (-b) % m
    b2 = lo + ((r - lo) % m)
    c2 = (b2 * b2 - D) // (4 * c)
    return (c, b2, c2)


def h_pos_narrow(D):
    """narrow class number = number of rho-cycles of reduced forms"""
    forms = set(reduced_forms_pos(D))
    seen = set()
    cycles = 0
    for f in sorted(forms):
        if f in seen:
            continue
        cycles += 1
        g = f
        while True:
            seen.add(g)
            g = rho_step(g, D)
            if g == f:
                break
            if g not in forms:
                raise RuntimeError("rho left the reduced set: %s" % (g,))
    return cycles


# ======================================================================
# F2 polynomial helpers (ints as bit masks, LSB = x^0)
# ======================================================================

def pdeg(p):
    return p.bit_length() - 1


def pmul(p, q):
    out = 0
    while q:
        if q & 1:
            out ^= p
        p <<= 1
        q >>= 1
    return out


def pdivmod(p, q):
    dq = pdeg(q)
    quo = 0
    while pdeg(p) >= dq and p:
        sh = pdeg(p) - dq
        quo |= 1 << sh
        p ^= q << sh
    return quo, p


# ======================================================================
section("S1: the discriminant map")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

PSTAR = {2: -4, 3: -3, 5: 5, 7: -7}
CHI_PLUS = (3, 5, 7, 2)                  # (F1, F2, F3, A) -> primes
V16 = list(itertools.product((0, 1), repeat=4))


def divisor(v):
    return (3 ** v[0]) * (5 ** v[1]) * (7 ** v[2]) * (2 ** v[3])


def disc(v):
    D = 1
    for bit, p in zip(v, CHI_PLUS):
        if bit:
            D *= PSTAR[p]
    return D


DISCS = {v: disc(v) for v in V16}
vals = sorted(DISCS.values())
check("S1.1 all 16 label discriminants fundamental (incl. trivial 1); "
      "bijective; values %s" % vals,
      len(set(vals)) == 16 and all(is_fundamental(D) for D in vals),
      kill="DISCMAP-BROKEN")

sign_ok = all((DISCS[v] < 0) == (sum(v[k] for k in (0, 2, 3)) % 2 == 1)
              for v in V16 if DISCS[v] != 1)
check("S1.2 sign structure: D(v) < 0 iff an odd number of "
      "chi4-negative bits {3, 7, 2(-4)} is set -- the discriminant "
      "sign pattern is the Frobenius/Walsh-seat pattern",
      sign_ok, kill="DISCMAP-BROKEN")

mag_ok = all(abs(DISCS[v])
             == (divisor(v) // (2 if v[3] else 1)) * (4 if v[3] else 1)
             for v in V16)
check("S1.3 |D(v)| = odd(d(v)) * (4 if anchor else 1) = d(v) resp. "
      "2 d(v) (-4 replaces the prime 2; v2 spec, slip recorded in "
      "header)", mag_ok, kill="DISCMAP-BROKEN")

# ======================================================================
section("S2: the four prime fields and their compiler roles")
# ======================================================================


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


fund_neg = [d for d in range(-3, -201, -1) if d != 1 and
            is_fundamental(d) and d < 0]
extra = sorted((d, unit_count(d)) for d in fund_neg if unit_count(d) > 2)
check("S2.a/b exceptional units: over all %d fundamental D in "
      "[-200,-3] exactly %s have w > 2 -- the pair (w=4 at -4, w=6 "
      "at -3) == (|mu4|, |R+(A3)|) = the compiler glue orders "
      "(third appearance of (4,6); classical beyond range, cited)"
      % (len(fund_neg), extra),
      extra == [(-4, 4), (-3, 6)] and unit_count(-4) == MU4_ORDER
      and unit_count(-3) == RPLUS_A3, kill="FIELDS-BROKEN")

# golden unit at the split prime
sols = [(x, y) for x in range(1, 11) for y in range(1, 11)
        if abs(x * x - 5 * y * y) == 4]
min_sol = min(sols, key=lambda s: s[0] + s[1])
norm_phi = (1 * 1 - 5 * 1 * 1) // 4
real_primes = [p for p in (3, 5, 7) if PSTAR[p] > 0]
check("S2.c Q(sqrt5): the UNIQUE real prime field (positive prime "
      "discriminant only at %s = g_car); minimal |x^2-5y^2| = 4 "
      "solution %s -> fundamental unit phi = (1+sqrt5)/2, norm %d "
      "== -1 (the golden ratio; icosian crossref v219/v313 typed)"
      % (real_primes, min_sol, norm_phi),
      real_primes == [G_CAR] and min_sol == (1, 1) and norm_phi == -1,
      kill="FIELDS-BROKEN")

h_primes = {d: h_neg(d) for d in (-3, -4, -7)}
check("S2.d prime-field class numbers h(-3), h(-4), h(-7) = %s all "
      "== 1 (reduced-form census); -7 = the deployed second "
      "compiler field (v533)" % h_primes,
      all(h == 1 for h in h_primes.values()), kill="FIELDS-BROKEN")

# ======================================================================
section("S3: Gauss sums carry the clock phase (50-digit witnesses)")
# ======================================================================
mpmath.mp.dps = 60


def gauss_sum(p):
    return sum(int(sp.jacobi_symbol(a, p))
               * mpmath.e ** (2j * mpmath.pi * a / p)
               for a in range(1, p))


gauss_ok = True
for p in (3, 5, 7):
    g = gauss_sum(p)
    target = (mpmath.mpc(0, 1) if PSTAR[p] < 0 else mpmath.mpf(1)) \
        * mpmath.sqrt(abs(PSTAR[p]))
    sq_dev = abs(g * g - PSTAR[p])
    ph_dev = abs(g - target)
    ok = sq_dev < mpmath.mpf("1e-40") and ph_dev < mpmath.mpf("1e-40")
    gauss_ok = gauss_ok and ok
    print("    g_%d = %s;  g^2 - p* = %.1e;  phase dev = %.1e"
          % (p, mpmath.nstr(g, 8), float(sq_dev), float(ph_dev)))
check("S3.1 g_p^2 == p* and phases (i, 1, i) at (3, 5, 7): the mu4 "
      "generator i is the Gauss-sum phase EXACTLY at the inert "
      "pair; D(v) = prod g_p^2 (Gauss sign theorem cited, 50-digit "
      "witnesses)", gauss_ok, kill="GAUSS-BROKEN")

# ======================================================================
section("S4: the single-genus law h+(D(v)) = 2^(wt-1) on all 16 labels")
# ======================================================================
law_ok = True
ambig_ok = True
rows = []
for v in sorted(V16, key=lambda w: (sum(w), divisor(w))):
    D = DISCS[v]
    wt = sum(v)
    if D == 1:
        rows.append((v, D, 1, "-"))
        continue
    if D < 0:
        h = h_neg(D)
        amb = all_ambiguous_neg(D)
        ambig_ok = ambig_ok and amb
        tag = "amb" if amb else "NON-AMB"
    else:
        h = h_pos_narrow(D)
        tag = "cycles"
    rows.append((v, D, h, tag))
    if h != 2 ** (wt - 1):
        law_ok = False
for v, D, h, tag in rows:
    print("    v=%s  d=%3d  D=%5d  h+=%2d  (2^(wt-1)=%2d)  [%s]"
          % ("".join(map(str, v)), divisor(v), D, h,
             2 ** (max(sum(v), 1) - 1), tag))
check("S4.1 THE LAW: h+(D(v)) == 2^(wt(v)-1) for every nonzero "
      "label -- one class per genus on the WHOLE register; every "
      "class group an elementary abelian 2-group (register-shaped, "
      "no hidden odd part)", law_ok, kill="FORMS-BROKEN")
check("S4.2 ambiguity witness (imaginary labels): every reduced "
      "form has b = 0, a = b or a = c -- exponent <= 2 verified "
      "composition-free", ambig_ok, kill="FORMS-BROKEN")
check("S4.3 message reading (typed): genus characters == the "
      "register's Legendre/Walsh characters decide representability "
      "completely (Gauss genus theory cited; the class counts "
      "computed above) -- ZERO bits beyond the register's own "
      "characters in the quadratic-form layer", law_ok and ambig_ok,
      kill=None)

# ======================================================================
section("S5: the primorial-idoneal ladder (third ladder-end)")
# ======================================================================
idoneal_rows = []
for n in (1, 2, 6, 30, 210, 2310):
    D = -4 * n
    forms = reduced_forms_neg(D)
    amb = all(b == 0 or a == b or a == c for a, b, c in forms)
    nonamb = [f for f in forms if not (f[1] == 0 or f[0] == f[1]
                                       or f[0] == f[2])]
    idoneal_rows.append((n, len(forms), amb, nonamb[:2]))
    print("    n = %4d: h(-4n) = %2d, all ambiguous: %s%s"
          % (n, len(forms), amb,
             ("  witness " + str(nonamb[0])) if nonamb else ""))
check("S5.1 primorial ladder 1, 2, 6, 30, 210 ALL idoneal "
      "(every reduced form of disc -4n ambiguous); 2310 = 11# is "
      "NOT (non-ambiguous witness exhibited) -- the ladder ends at "
      "the register modulus, same endpoint as the Coxeter ladder "
      "(Euler's 65-number list, largest 1848, cited [C])",
      all(amb for n, _, amb, _ in idoneal_rows if n != 2310)
      and not idoneal_rows[-1][2], kill="IDONEAL-BROKEN")

# ======================================================================
section("S6: the QR-code seat of 7 (and the undeployed Golay rung)")
# ======================================================================
qr_primes = [p for p in (3, 5, 7)
             if any(a * a % p == 2 % p for a in range(1, p))]
check("S6.a 2 is a QR mod p only at p = 7 among the register "
      "primes: %s (7 == -1 mod 8; 3, 5 !== +-1 mod 8)" % qr_primes,
      qr_primes == [7], kill="QRCODE-BROKEN")

# irreducibility of (x^p+1)/(x+1) over F2 for p = 3, 5
def irreducible(p_mask):
    d = pdeg(p_mask)
    for q in range(2, 1 << (d // 2 + 1)):
        if pdeg(q) >= 1 and pdivmod(p_mask, q)[1] == 0:
            return False
    return True


q3 = pdivmod((1 << 3) | 1, 0b11)[0]          # x^2+x+1
q5 = pdivmod((1 << 5) | 1, 0b11)[0]          # x^4+..+1
q7 = pdivmod((1 << 7) | 1, 0b11)[0]
g7 = 0b1011                                   # x^3 + x + 1
quo7, rem7 = pdivmod(q7, g7)
check("S6.a' no QR split at 3, 5: x^2+x+1 and x^4+x^3+x^2+x+1 "
      "irreducible over F2 (%s, %s); at 7 the quotient splits: "
      "(x^7+1)/(x+1) = (x^3+x+1)(x^3+x^2+1), remainder %d"
      % (irreducible(q3), irreducible(q5), rem7),
      irreducible(q3) and irreducible(q5) and rem7 == 0
      and quo7 == 0b1101, kill="QRCODE-BROKEN")


def cyclic_code(gen, n, k):
    words = []
    for m in range(1 << k):
        c = pmul(gen, m)
        words.append(tuple((c >> i) & 1 for i in range(n)))
    return words


def wdist(words):
    from collections import Counter
    return dict(Counter(sum(w) for w in words))


qr7 = cyclic_code(g7, 7, 4)
w7 = wdist(qr7)
ext7 = [w + (sum(w) % 2,) for w in qr7]
w8 = wdist(ext7)
ext7_set = frozenset(ext7)
dual8 = all(sum(a * b for a, b in zip(u, w)) % 2 == 0
            for u in ext7 for w in ext7)
check("S6.b QR(7) = cyclic [7,4,3] (weights %s); extended = "
      "[8,4,4] with enumerator %s == {0:1, 4:14, 8:1}, self-"
      "orthogonal & dim 4 => SELF-DUAL, doubly even -- the deployed "
      "extended-Hamming class (uniqueness cited)" % (w7, w8),
      w7 == {0: 1, 3: 7, 4: 7, 7: 1} and w8 == {0: 1, 4: 14, 8: 1}
      and dual8 and len(ext7_set) == 16, kill="QRCODE-BROKEN")

count240 = 0
for x in itertools.product((-2, -1, 0, 1, 2), repeat=8):
    if sum(t * t for t in x) == 4:
        if tuple(t % 2 for t in x) in ext7_set:
            count240 += 1
check("S6.c Construction A over the extended QR(7) code: exactly "
      "%d norm-4 vectors in {x in Z^8 : x mod 2 in C} == 240 = "
      "|R(E8)| -- the E8 binary skeleton IS the quadratic-residue "
      "code at the register prime 7" % count240,
      count240 == 240, kill="QRCODE-BROKEN")

# the Golay rung at p = 23
q23 = pdivmod((1 << 23) | 1, 0b11)[0]
g23 = None
for cand in range(1 << 11, 1 << 12):
    if cand & 1 and pdivmod(q23, cand)[1] == 0:
        g23 = cand
        break
qr23 = cyclic_code(g23, 23, 12)
ext23 = [w + (sum(w) % 2,) for w in qr23]
w24 = wdist(ext23)
check("S6.d the NEXT QR rung p = 23: degree-11 QR factor found "
      "(0b%s); extended [24,12] enumerator %s == the binary GOLAY "
      "{0:1, 8:759, 12:2576, 16:759, 24:1} -- exists in the "
      "mathematics, ABSENT from the compiler (fourth ladder-end, "
      "typed)" % (bin(g23)[2:], w24),
      w24 == {0: 1, 8: 759, 12: 2576, 16: 759, 24: 1},
      kill="QRCODE-BROKEN")

# ======================================================================
section("C: controls")
# ======================================================================
forms660 = reduced_forms_neg(-660)
amb660 = all(b == 0 or a == b or a == c for a, b, c in forms660)
check("C1 idoneality NOT unique to the deployed quadruple "
      "(measured, typed): foreign top disc -660 ({2,3,5,11}): "
      "h = %d, all ambiguous = %s (165 is on Euler's list -- "
      "expected; the selective content is the CONJUNCTION with the "
      "forcing/gear/Coxeter pins, never idoneality alone)"
      % (len(forms660), amb660), True, kill=None)

check("C2 QR-code absence at 3 and 5 fired in S6.a/S6.a'",
      qr_primes == [7], kill="CONTROL-DEAD")

# the three prime discriminants at 2 and their unit counts
w_minus4 = unit_count(-4)
w_minus8 = unit_count(-8)
# Q(sqrt2) is real: unit group infinite (Pell x^2 - 2y^2 = 1 has the
# nontrivial solution (3,2)) -- exhibit it exactly
pell2 = (3 * 3 - 2 * 2 * 2 == 1)
check("C3 the 2-adic ambiguity typed (v2): among the prime "
      "discriminants at 2, only -4 carries the clock: w(-4) = %d "
      "== |mu4|, w(-8) = %d == 2, Q(sqrt2) real with infinite "
      "units (Pell witness 3^2 - 2*2^2 = 1: %s); plus -4 = disc "
      "Q(i) = the register-cut field itself"
      % (w_minus4, w_minus8, pell2),
      w_minus4 == 4 and w_minus8 == 2 and pell2,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
verdict = KILLS[0] if KILLS else (
    "QUADCODE-EXACT" if n_pass == len(CHECKS) else "QUADCODE-PARTIAL")

print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS ADDS (measured, exploration only):
 * THE REGISTER IS A DISCRIMINANT CODE: label -> fundamental
   discriminant D(v) = prod p* (= prod Gauss-sum squares); sign
   pattern = Frobenius/Walsh seat; the four prime fields carry the
   compiler roles (Q(i) clock w=4; Eisenstein w=6 = hexagon; the
   golden field at the carrier prime, norm -1 unit; -7 = the
   deployed second compiler field).
 * THE SINGLE-GENUS LAW: h+(D(v)) = 2^(wt-1) on all 16 labels --
   class groups are elementary 2-groups, the genus characters (=
   the register's own Walsh/Legendre characters) decide everything:
   zero hidden bits in the quadratic-form layer.
 * THIRD LADDER-END: the primorials 1, 2, 6, 30, 210 are idoneal,
   2310 is not -- Euler's idoneal ladder ends at the register
   modulus, in step with the Coxeter ladder.
 * FOURTH LADDER-END: the E8 binary skeleton is the QR code at the
   register prime 7 (the unique QR-code prime of the register);
   the next QR rung (23 -> Golay -> Leech direction) exists and is
   not deployed.
NO ledger/paper/website claim; NO RH claim; NO physics claim beyond
the recorded exact identities.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
