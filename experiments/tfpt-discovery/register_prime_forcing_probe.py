#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""register_prime_forcing_probe -- E8.DIVISOR210.PRIMEFORCE.01:
the arithmetic seat of the register modulus 210.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH claim.  Frozen (spec + sha256)
before running.  Exact integer/Fraction arithmetic in every decision;
sympy only for factorint cross-checks; no floats, no RNG, no fit.

THE OPEN NOTE TO ATTACK (divisor210_canonicity_probe, read-only,
verdict DIVISOR210-GAUGE-FAMILY(2)): the quadruple {2,3,5,7} was
pinned by the DEPLOYED scalar-limit Euler constants (empirical pin);
the count 210 = C(10,4) was typed as a pleasing coincidence; the
6-vs-7 mismatch with the clock alphabet {2,3,5,6} was typed, not
resolved.  QUESTION (frozen): does 210 have a STRUCTURE-side seat --
computable from the compiler's own Lie-theoretic objects -- and a
COMPILER-side forcing -- computable from a deployed compiler
multiplicity -- independent of the Euler pin?

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  ROOT-SYSTEM FOUNDRY (actual objects, not tables): build the
     root systems of ALL simple types of rank <= 8 (A1..A8, B2..B8,
     C3..C8, D4..D8, G2, F4, E6, E7, E8) from coordinates; positive
     system via a generic functional; simple system = positive roots
     that are not sums of two positive roots; heights by exact
     Fraction solve; exponents = the dual partition of the height
     distribution (Kostant); degrees = exponents + 1; |W| = prod of
     degrees.  WARDS: #simple roots == rank, #exponents == rank,
     sum(exponents) == #positive roots, |W| == the closed-form order
     (A: (n+1)!, B/C: 2^n n!, D: 2^{n-1} n!, G2: 12, F4: 1152,
     E6: 51840, E7: 2903040, E8: 696729600); DIRECT BFS group
     generation cross-check |W| for A1, A2, A3, B2, G2, D4, D5, F4
     (matrix closure, exact Fractions).  Any fail => FOUNDRY-BROKEN.

 S2  THE PRIMORIAL TOWER (the structure-side seat of 210): with
     rad(n) = prod of distinct primes dividing n,
       rad|W(A3)|      = 6   = 2*3     = 3#   (the gear),
       rad|W(D5)|      = 30  = 2*3*5   = 5#   (the carrier),
       rad|W(D5xA3)|   = 30                    (the compiler source),
       rad|W(E8)|      = 210 = 2*3*5*7 = 7#   (the hull);
     the register modulus IS rad|W(E8)| -- the squarefree kernel of
     the E8 Weyl order; the compiler chain A3 -> D5(+A3) -> E8 climbs
     the primorial ladder 3# -> 5# -> 7#, one new prime per stage:
     5 enters at the carrier (the "5" of D5 = g_car), 7 enters at
     the E8 weld (via the degree 14 = 2*7; 7 is itself an E8
     exponent).  Any fail => TOWER-BROKEN.

 S3  THE TOTIENT TOWER (the compiler numbers): phi(6) = 2 = |Z2|,
     phi(30) = 8 = rank(E8), phi(210) = 48 = Omega_adm (the
     admissible multiplicity 48 = 3 x 16 = N_fam x |register| of
     v483/v484/v485: dtop = 48 c3^4, Lambda prefactor 48 c3^2);
     step ratios phi(30)/phi(6) = 4 = |mu4| and phi(210)/phi(30) =
     6 = 2 N_fam = |R+(A3)| (the two glue orders); the divisor count
     tau(210) = 16 = the register label count = [Z^8 : L];
     KOSTANT CHECK from the actual heights: exponents(E8) == the
     totatives of 30 == units of Z/30 (so rank = phi(h) is REALIZED,
     not just numerical).  Any fail => TOTIENT-BROKEN.

 S4  THE GEAR DECOMPOSITION (exact unit groups): by CRT,
     (Z/210)* = (Z/2)* x (Z/3)* x (Z/5)* x (Z/7)* with orders
     (1, 2, 4, 6): verify each factor cyclic by exhibiting a
     generator (brute force, exact orders); the four gears are the
     compiler inventory {trivial, |Z2|, |mu4|, |R+(A3)|} =
     {anchor, sheet, clock, hexagon}; total order 1*2*4*6 = 48 =
     Omega_adm; element-order census of (Z/210)* (exponent lcm = 12,
     the clock wall 12 = |mu4| x N_fam); THE 6-vs-7 CANDIDATE
     READING (recorded next to the frozen v868 candidates, NO
     selection): 6 = phi(7) = the unit-gear order AT 7 -- the clock
     alphabet {2,3,5,6} and the quadruple {2,3,5,7} differ exactly
     by p <-> phi(p) at the last slot.  Any fail => GEAR-BROKEN.

 S5  THE FORCING CENSUS (the compiler-side pin, independent of the
     Euler pin): enumerate ALL quadruples of distinct primes with
     prod(p_i - 1) = 48 (complete: any member satisfies p - 1 <= 48,
     so p <= 49; census over primes < 50).  FROZEN EXPECTATION:
     exactly one quadruple, {2,3,5,7}.  Consequence: "four bits" +
     "phi(N) = Omega_adm" + "N squarefree" FORCES N = 210 with no
     reference to the deployed Euler constants.  Context censuses
     (measured, typed): quadruples with prod(p-1) in {24, 96}.
     Any fail => FORCING-BROKEN.

 S6  THE LADDER-END THEOREM (the message-shaped fact, exact): the
     cyclotomic-Coxeter census over ALL simple types rank <= 8:
     types with rank == phi(h) (i.e. exponents = totatives of h).
     V2 AMENDMENT (honest, after run 1 = 25/27): the v1 frozen list
     (A1, A2, B2, G2, B4, F4, B8, E8) was INCOMPLETE -- it missed
     A4 (h = 5), A6 (h = 7) (A_{p-1} has rank p-1 = phi(p) for every
     prime p <= 8+1) and C4, C8 (same h as B4, B8).  The MEASURED
     census (A1, A2, A4, A6, B2, B4, B8, C4, C8, E8, F4, G2) is the
     v2 expectation; the mathematical content SHARPENS: the
     squarefree-h subfamily realizes h in {2, 3, 5, 7} u {6, 30} --
     the four register primes THEMSELVES (via A_{p-1} = SU(p)) plus
     the two composite primorials (G2, E8); the primorial-h
     subfamily (A1 (h=2=2#), G2 (h=6=3#), E8 (h=30=5#)) is UNCHANGED
     and E8 is the TOP.  v1 miss recorded here, no criterion beyond
     the census lists changed.  THE NEXT RUNG DOES NOT EXIST IN LIE THEORY: a rung-4
     group would need h = 7# = 210 and rank = phi(210) = 48; over
     all four infinite families the Coxeter numbers at EVERY rank
     are h(A_n) = n+1, h(B_n/C_n) = 2n, h(D_n) = 2n-2, so h = 210
     forces rank in {209, 105, 106} != 48, and all exceptional types
     have h <= 30 (closed-form check, exact).  The rung-4 pair
     (210, 48) is realized ONLY by the register: modulus 210 with
     phi(210) = 48 = Omega_adm state multiplicity -- the primorial
     tower leaves Lie theory and continues in the state space.
     Typed as structural observation; no physics claim.

 C   CONTROLS (must fire / must measure generic where predeclared):
     C1 RADICAL NON-UNIQUENESS (honesty): the rad|W| census over all
        30 types; PREDECLARED: many high-rank types also hit 210
        (any |W| containing 7!); the radical alone selects nothing --
        the selective statement is the TOWER along the compiler
        chain + S5/S6, NOT the single value.  Measured list printed.
     C2 FOREIGN QUADRUPLES: {2,3,5,11} has prod(p-1) = 80 != 48 and
        unit gears (1,2,4,10) -- the order 10 is not a compiler gear
        order; {3,5,7,11} has prod(p-1) = 480 and NO trivial gear
        (no ramified/anchor slot).  Both fire.
     C3 WRONG-TOWER CONTROL: the OTHER natural chains miss the
        primorial ladder: rad|W(A3)| -> rad|W(D4)| -> rad|W(E8)| =
        (6, 6, 210) skips 30; rad|W(A2)| -> rad|W(D5)| gives
        (6, 30) but A2 is not the compiler gear (A3 is); measured.

VERDICT (frozen precedence): FOUNDRY-BROKEN / TOWER-BROKEN /
TOTIENT-BROKEN / GEAR-BROKEN / FORCING-BROKEN / CONTROL-DEAD if the
corresponding kill fires; else PRIMEFORCE-EXACT if S5 returns
exactly {2,3,5,7} and all S1-S6 checks pass; else PRIMEFORCE-PARTIAL.

Sources (read-only): divisor210_canonicity_probe.py (the open notes),
verification/v483/v484/v485 (Omega_adm = 48 = 3x16),
tfpt_constants (N_fam = 3, g_car = 5, |Z2| = 2, |mu4| = 4).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/register_prime_forcing_probe.py
"""

import hashlib
import itertools
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
MU4_ORDER = 4
RPLUS_A3 = 6
OMEGA_ADM = 48          # v483/v484/v485: 48 = 3 x 16 admissible states
REGISTER_LABELS = 16    # v845: |L/(1+i)L| = 16

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


def rad(n):
    return int(sp.prod(sorted(sp.factorint(n).keys())))


def primorial(p):
    """product of all primes <= p"""
    out = 1
    for q in range(2, p + 1):
        if sp.isprime(q):
            out *= q
    return out


# ======================================================================
# root-system foundry (exact Fractions throughout)
# ======================================================================

def e(i, dim):
    v = [Fraction(0)] * dim
    v[i] = Fraction(1)
    return tuple(v)


def vadd(u, v):
    return tuple(a + b for a, b in zip(u, v))


def vneg(u):
    return tuple(-a for a in u)


def vsub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def vscale(c, u):
    return tuple(c * a for a in u)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def roots_A(n):
    d = n + 1
    return [vsub(e(i, d), e(j, d)) for i in range(d) for j in range(d)
            if i != j]


def roots_B(n):
    R = []
    for i in range(n):
        R.append(e(i, n))
        R.append(vneg(e(i, n)))
    for i in range(n):
        for j in range(i + 1, n):
            for si in (1, -1):
                for sj in (1, -1):
                    R.append(vadd(vscale(Fraction(si), e(i, n)),
                                  vscale(Fraction(sj), e(j, n))))
    return R


def roots_C(n):
    R = []
    for i in range(n):
        R.append(vscale(Fraction(2), e(i, n)))
        R.append(vscale(Fraction(-2), e(i, n)))
    for i in range(n):
        for j in range(i + 1, n):
            for si in (1, -1):
                for sj in (1, -1):
                    R.append(vadd(vscale(Fraction(si), e(i, n)),
                                  vscale(Fraction(sj), e(j, n))))
    return R


def roots_D(n):
    R = []
    for i in range(n):
        for j in range(i + 1, n):
            for si in (1, -1):
                for sj in (1, -1):
                    R.append(vadd(vscale(Fraction(si), e(i, n)),
                                  vscale(Fraction(sj), e(j, n))))
    return R


def roots_G2():
    # in the plane sum x_i = 0 of R^3
    R = []
    for i in range(3):
        for j in range(3):
            if i != j:
                R.append(vsub(e(i, 3), e(j, 3)))
    for i in range(3):
        j, k = [x for x in range(3) if x != i]
        long_r = vsub(vscale(Fraction(2), e(i, 3)),
                      vadd(e(j, 3), e(k, 3)))
        R.append(long_r)
        R.append(vneg(long_r))
    return R


def roots_F4():
    R = []
    for i in range(4):
        R.append(e(i, 4))
        R.append(vneg(e(i, 4)))
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    R.append(vadd(vscale(Fraction(si), e(i, 4)),
                                  vscale(Fraction(sj), e(j, 4))))
    h = Fraction(1, 2)
    for signs in itertools.product((1, -1), repeat=4):
        R.append(tuple(h * s for s in signs))
    return R


def roots_E8():
    R = roots_D(8)
    h = Fraction(1, 2)
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            R.append(tuple(h * s for s in signs))
    return R


def roots_E7():
    # E8 roots orthogonal to a fixed root r0 = e7 + e8 -> 126 roots
    r0 = vadd(e(6, 8), e(7, 8))
    return [r for r in roots_E8() if dot(r, r0) == 0]


def roots_E6():
    # E8 roots orthogonal to an A2: r0 = e7+e8, r1 = half-sum root
    r0 = vadd(e(6, 8), e(7, 8))
    h = Fraction(1, 2)
    r1 = tuple([-h] * 6 + [h, h])
    assert dot(r0, r1) == 1  # they span an A2 (angle 60 deg, norms 2)
    return [r for r in roots_E8()
            if dot(r, r0) == 0 and dot(r, r1) == 0]


def analyze(roots):
    """positive system, simple roots, heights, exponents, degrees, |W|"""
    dim = len(roots[0])
    # generic functional: exact integers on doubled coordinates
    def f(r):
        return sum(int(2 * a) * (10 ** (3 * k)) + int(2 * a) * 7 ** k
                   for k, a in enumerate(r))
    pos = [r for r in roots if f(r) > 0]
    if 2 * len(pos) != len(roots):
        raise RuntimeError("functional not generic")
    posset = set(pos)
    simple = [r for r in pos
              if not any(vsub(r, s) in posset for s in pos
                         if s != r and f(vsub(r, s)) > 0
                         and vsub(r, s) != r)]
    # cleaner: r is simple iff r != s + t for positive s, t
    simple = []
    for r in pos:
        decomposable = False
        for s in pos:
            t = vsub(r, s)
            if t in posset and t != r and s != r:
                decomposable = True
                break
        if not decomposable:
            simple.append(r)
    rank = len(simple)
    # heights: solve r = sum c_i alpha_i by exact Gaussian elimination
    # build matrix with columns = simple roots
    def solve_coords(r):
        m = [[simple[j][i] for j in range(rank)] + [r[i]]
             for i in range(dim)]
        # gaussian elimination (Fractions), possibly overdetermined
        row = 0
        pivots = []
        for col in range(rank):
            sel = None
            for rr in range(row, dim):
                if m[rr][col] != 0:
                    sel = rr
                    break
            if sel is None:
                continue
            m[row], m[sel] = m[sel], m[row]
            pv = m[row][col]
            m[row] = [x / pv for x in m[row]]
            for rr in range(dim):
                if rr != row and m[rr][col] != 0:
                    fac = m[rr][col]
                    m[rr] = [x - fac * y for x, y in zip(m[rr], m[row])]
            pivots.append(col)
            row += 1
        if len(pivots) != rank:
            raise RuntimeError("simple system not independent")
        coords = [Fraction(0)] * rank
        for k, col in enumerate(pivots):
            coords[col] = m[k][rank]
        # consistency of remaining rows
        for rr in range(row, dim):
            if m[rr][rank] != 0:
                raise RuntimeError("inconsistent solve")
        return coords
    heights = []
    for r in pos:
        c = solve_coords(r)
        h = sum(c)
        if h.denominator != 1 or h <= 0:
            raise RuntimeError("non-integer/nonpositive height")
        if any(ci.denominator != 1 or ci < 0 for ci in c):
            raise RuntimeError("non-integral simple coordinates")
        heights.append(int(h))
    # exponents = dual partition of the height distribution
    from collections import Counter
    hc = Counter(heights)
    maxh = max(heights)
    nk = [hc.get(k, 0) for k in range(1, maxh + 1)]
    # weakly decreasing ward
    if any(nk[i] < nk[i + 1] for i in range(len(nk) - 1)):
        raise RuntimeError("height distribution not weakly decreasing")
    exps = sorted(sum(1 for x in nk if x >= i)
                  for i in range(1, nk[0] + 1))
    degrees = [m + 1 for m in exps]
    W = 1
    for d in degrees:
        W *= d
    return {"pos": pos, "simple": simple, "rank": rank,
            "exponents": exps, "degrees": degrees, "W": W,
            "h": max(exps) + 1, "npos": len(pos)}


def weyl_order_bfs(simple, cap=25000):
    """order of the group generated by simple reflections (exact)"""
    dim = len(simple[0])
    def reflect_matrix(a):
        n2 = dot(a, a)
        return tuple(tuple((Fraction(1) if i == j else Fraction(0))
                           - 2 * a[i] * a[j] / n2
                           for j in range(dim)) for i in range(dim))
    def matmul(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(dim))
                           for j in range(dim)) for i in range(dim))
    gens = [reflect_matrix(a) for a in simple]
    ident = tuple(tuple(Fraction(1) if i == j else Fraction(0)
                        for j in range(dim)) for i in range(dim))
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = matmul(s, g)
                if h not in seen:
                    seen.add(h)
                    nxt.append(h)
                    if len(seen) > cap:
                        raise RuntimeError("BFS cap exceeded")
        frontier = nxt
    return len(seen)


# closed-form orders
def fact(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


CLOSED = {}
for n in range(1, 9):
    CLOSED["A%d" % n] = fact(n + 1)
for n in range(2, 9):
    CLOSED["B%d" % n] = (2 ** n) * fact(n)
for n in range(3, 9):
    CLOSED["C%d" % n] = (2 ** n) * fact(n)
for n in range(4, 9):
    CLOSED["D%d" % n] = (2 ** (n - 1)) * fact(n)
CLOSED.update({"G2": 12, "F4": 1152, "E6": 51840,
               "E7": 2903040, "E8": 696729600})

BUILDERS = {}
for n in range(1, 9):
    BUILDERS["A%d" % n] = (lambda n=n: roots_A(n))
for n in range(2, 9):
    BUILDERS["B%d" % n] = (lambda n=n: roots_B(n))
for n in range(3, 9):
    BUILDERS["C%d" % n] = (lambda n=n: roots_C(n))
for n in range(4, 9):
    BUILDERS["D%d" % n] = (lambda n=n: roots_D(n))
BUILDERS.update({"G2": roots_G2, "F4": roots_F4,
                 "E6": roots_E6, "E7": roots_E7, "E8": roots_E8})

# ======================================================================
section("S1: root-system foundry (all simple types rank <= 8)")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

DATA = {}
foundry_ok = True
for name in sorted(BUILDERS):
    roots = BUILDERS[name]()
    info = analyze(roots)
    DATA[name] = info
    ok = (info["W"] == CLOSED[name]
          and len(info["exponents"]) == info["rank"]
          and sum(info["exponents"]) == info["npos"])
    foundry_ok = foundry_ok and ok
    if not ok:
        print("    !! %s: W=%d closed=%d rank=%d exps=%s"
              % (name, info["W"], CLOSED[name], info["rank"],
                 info["exponents"]))

check("S1.1 all %d types: |W| from measured exponents == closed form; "
      "#exponents == rank; sum(exponents) == #positive roots"
      % len(BUILDERS), foundry_ok, kill="FOUNDRY-BROKEN")

bfs_ok = True
for name in ("A1", "A2", "A3", "B2", "G2", "D4", "D5", "F4"):
    got = weyl_order_bfs(DATA[name]["simple"])
    ok = got == CLOSED[name]
    bfs_ok = bfs_ok and ok
    print("    BFS |W(%s)| = %d (closed %d) %s"
          % (name, got, CLOSED[name], "OK" if ok else "MISMATCH"))
check("S1.2 direct BFS group generation matches |W| on 8 small types",
      bfs_ok, kill="FOUNDRY-BROKEN")

check("S1.3 E8 sanity: 240 roots, 120 positive, rank 8, h = 30, "
      "exponents %s" % (DATA["E8"]["exponents"],),
      DATA["E8"]["npos"] == 120 and DATA["E8"]["rank"] == 8
      and DATA["E8"]["h"] == 30
      and DATA["E8"]["exponents"] == [1, 7, 11, 13, 17, 19, 23, 29],
      kill="FOUNDRY-BROKEN")

# ======================================================================
section("S2: the primorial tower (structure-side seat of 210)")
# ======================================================================
W_A3 = DATA["A3"]["W"]
W_D5 = DATA["D5"]["W"]
W_E8 = DATA["E8"]["W"]
rad_A3, rad_D5, rad_E8 = rad(W_A3), rad(W_D5), rad(W_E8)
rad_D5A3 = rad(W_D5 * W_A3)

check("S2.1 rad|W(A3)| = %d == 6 == 2*3 == 3# (|W| = %d)"
      % (rad_A3, W_A3), rad_A3 == 6 == primorial(3),
      kill="TOWER-BROKEN")
check("S2.2 rad|W(D5)| = %d == 30 == 2*3*5 == 5# (|W| = %d)"
      % (rad_D5, W_D5), rad_D5 == 30 == primorial(5),
      kill="TOWER-BROKEN")
check("S2.3 rad|W(D5 x A3)| = %d == 30 (the compiler source keeps 5#)"
      % rad_D5A3, rad_D5A3 == 30, kill="TOWER-BROKEN")
check("S2.4 rad|W(E8)| = %d == 210 == 2*3*5*7 == 7# (|W| = %d) -- "
      "THE REGISTER MODULUS IS THE SQUAREFREE KERNEL OF THE E8 WEYL "
      "ORDER" % (rad_E8, W_E8),
      rad_E8 == 210 == primorial(7), kill="TOWER-BROKEN")
check("S2.5 one new prime per compiler stage: 5 enters at the carrier "
      "(D5, g_car = %d), 7 enters at the E8 weld; 7 divides exactly "
      "one E8 degree (14 = 2*7) and 7 is itself an E8 exponent"
      % G_CAR,
      G_CAR == 5 and 5 not in sp.factorint(W_A3)
      and 5 in sp.factorint(W_D5) and 7 not in sp.factorint(W_D5)
      and 7 in sp.factorint(W_E8)
      and [d for d in DATA["E8"]["degrees"] if d % 7 == 0] == [14]
      and 7 in DATA["E8"]["exponents"],
      kill="TOWER-BROKEN")

# ======================================================================
section("S3: the totient tower (the compiler numbers)")
# ======================================================================
phi6 = int(sp.totient(6))
phi30 = int(sp.totient(30))
phi210 = int(sp.totient(210))
tau210 = len(sp.divisors(210))

check("S3.1 phi(6) = %d == |Z2| = %d" % (phi6, Z2_ORDER),
      phi6 == Z2_ORDER, kill="TOTIENT-BROKEN")
check("S3.2 phi(30) = %d == rank(E8) = %d" % (phi30, DATA["E8"]["rank"]),
      phi30 == DATA["E8"]["rank"], kill="TOTIENT-BROKEN")
check("S3.3 phi(210) = %d == Omega_adm = %d == N_fam x |register| "
      "= %d x %d" % (phi210, OMEGA_ADM, N_FAM, REGISTER_LABELS),
      phi210 == OMEGA_ADM == N_FAM * REGISTER_LABELS,
      kill="TOTIENT-BROKEN")
check("S3.4 step ratios: phi(30)/phi(6) = %d == |mu4| = %d; "
      "phi(210)/phi(30) = %d == 2 N_fam = |R+(A3)| = %d (the two "
      "glue orders)" % (phi30 // phi6, MU4_ORDER, phi210 // phi30,
                        RPLUS_A3),
      phi30 // phi6 == MU4_ORDER and phi210 // phi30 == RPLUS_A3,
      kill="TOTIENT-BROKEN")
check("S3.5 tau(210) = %d == register label count %d"
      % (tau210, REGISTER_LABELS), tau210 == REGISTER_LABELS,
      kill="TOTIENT-BROKEN")

totatives30 = sorted(k for k in range(1, 30) if sp.gcd(k, 30) == 1)
check("S3.6 KOSTANT CHECK from actual heights: exponents(E8) == "
      "totatives(30) == %s (rank = phi(h) REALIZED)" % totatives30,
      DATA["E8"]["exponents"] == totatives30, kill="TOTIENT-BROKEN")

# ======================================================================
section("S4: the gear decomposition of (Z/210)*")
# ======================================================================
gears = {}
gear_ok = True
for p in (2, 3, 5, 7):
    units = [a for a in range(1, p) if sp.gcd(a, p) == 1]
    order = len(units)
    gen = None
    for g in units:
        x, o = g % p, 1
        while x != 1:
            x = (x * g) % p
            o += 1
        if o == order:
            gen = g
            break
    cyclic = (gen is not None) or (order == 1)
    gears[p] = order
    gear_ok = gear_ok and cyclic
    print("    (Z/%d)*: order %d, cyclic %s (generator %s)"
          % (p, order, cyclic, gen))

check("S4.1 CRT gear orders (1, 2, 4, 6) at (2, 3, 5, 7): each factor "
      "cyclic; orders == {trivial anchor, |Z2|, |mu4|, |R+(A3)|} = "
      "the compiler gear inventory",
      gear_ok and [gears[p] for p in (2, 3, 5, 7)] == [1, 2, 4, 6]
      and gears[3] == Z2_ORDER and gears[5] == MU4_ORDER
      and gears[7] == RPLUS_A3, kill="GEAR-BROKEN")

check("S4.2 total |(Z/210)*| = 1*2*4*6 = %d == Omega_adm = %d"
      % (1 * 2 * 4 * 6, OMEGA_ADM), 1 * 2 * 4 * 6 == OMEGA_ADM,
      kill="GEAR-BROKEN")

units210 = [a for a in range(1, 210) if sp.gcd(a, 210) == 1]
orders = {}
for a in units210:
    x, o = a, 1
    while x != 1:
        x = (x * a) % 210
        o += 1
    orders[a] = o
lam = 1
for o in set(orders.values()):
    lam = sp.lcm(lam, o)
check("S4.3 group exponent lambda(210) = %d == 12 == |mu4| x N_fam "
      "(the clock wall); %d units total" % (lam, len(units210)),
      int(lam) == 12 == MU4_ORDER * N_FAM and len(units210) == 48,
      kill="GEAR-BROKEN")

check("S4.4 6-vs-7 CANDIDATE READING (typed, no selection): the "
      "clock-alphabet slot 6 == phi(7) = %d -- alphabet {2,3,5,6} vs "
      "quadruple {2,3,5,7} differ exactly by p <-> phi(p) at the "
      "last slot; recorded next to the frozen v868 candidates"
      % gears[7], gears[7] == 6, kill=None)

# ======================================================================
section("S5: the forcing census (prod(p-1) = 48)")
# ======================================================================
primes50 = [p for p in range(2, 50) if sp.isprime(p)]
hits48 = [q for q in itertools.combinations(primes50, 4)
          if (q[0] - 1) * (q[1] - 1) * (q[2] - 1) * (q[3] - 1) == 48]
hits24 = [q for q in itertools.combinations(primes50, 4)
          if (q[0] - 1) * (q[1] - 1) * (q[2] - 1) * (q[3] - 1) == 24]
hits96 = [q for q in itertools.combinations(primes50, 4)
          if (q[0] - 1) * (q[1] - 1) * (q[2] - 1) * (q[3] - 1) == 96]

check("S5.1 COMPLETENESS: any quadruple member has p - 1 <= 48, so "
      "p <= 49; census field = all C(%d, 4) quadruples of primes < 50"
      % len(primes50), primes50[-1] == 47, kill="FORCING-BROKEN")
check("S5.2 THE FORCING: quadruples with prod(p-1) = 48: %s -- "
      "EXACTLY {2,3,5,7}: 'four bits' + 'phi(N) = Omega_adm' + "
      "'N squarefree' forces N = 210 with NO reference to the "
      "deployed Euler constants" % (hits48,),
      hits48 == [(2, 3, 5, 7)], kill="FORCING-BROKEN")
check("S5.3 context (measured, typed): prod(p-1) = 24 hits %s; "
      "prod(p-1) = 96 hits %s -- the neighbours are non-unique or "
      "empty, 48 is a clean pin" % (hits24, hits96),
      True, kill=None)

# ======================================================================
section("S6: the ladder-end theorem (cyclotomic-Coxeter census)")
# ======================================================================
cyclo = []
for name in sorted(DATA):
    h = DATA[name]["h"]
    if DATA[name]["rank"] == int(sp.totient(h)):
        tot = sorted(k for k in range(1, h + 1) if sp.gcd(k, h) == 1)
        realized = DATA[name]["exponents"] == tot
        cyclo.append((name, h, realized))
        print("    rank = phi(h): %s (h = %d, exponents == totatives: %s)"
              % (name, h, realized))

names_cyclo = sorted(n for n, _, _ in cyclo)
check("S6.1 rank = phi(h) census over all 30 types (v2 expectation, "
      "v1 miss recorded in header): %s; every member REALIZES "
      "exponents == totatives(h)" % names_cyclo,
      names_cyclo == ["A1", "A2", "A4", "A6", "B2", "B4", "B8",
                      "C4", "C8", "E8", "F4", "G2"]
      and all(r for _, _, r in cyclo), kill="CONTROL-DEAD")

sqfree = sorted((n, h) for n, h, _ in cyclo if rad(h) == h)
prim = sorted((n, h) for n, h, _ in cyclo
              if rad(h) == h and h in (2, 6, 30, 210))
sq_h = sorted(h for _, h in sqfree)
check("S6.2 squarefree-h subfamily %s realizes h in {2,3,5,7} u "
      "{6,30}: the four REGISTER PRIMES themselves (A_{p-1} = SU(p)) "
      "plus the two composite primorials; primorial-h subfamily %s "
      "== [A1 (2 = 2#), G2 (6 = 3#), E8 (30 = 5#)] -- E8 is the TOP "
      "of the primorial-Coxeter ladder" % (sqfree, prim),
      sq_h == [2, 3, 5, 6, 7, 30]
      and sorted(h for _, h in sqfree if sp.isprime(h)) == [2, 3, 5, 7]
      and prim == [("A1", 2), ("E8", 30), ("G2", 6)],
      kill="CONTROL-DEAD")

# rung 4 does not exist in Lie theory (closed form over all ranks)
no_rung4 = True
targets = []
# h(A_n) = n + 1 = 210  -> n = 209, phi-rank needed 48
if int(sp.totient(210)) == 48:
    targets.append(("A209", 209))
    targets.append(("B105/C105", 105))
    targets.append(("D106", 106))
for nm, rk in targets:
    if rk == 48:
        no_rung4 = False
excep_h = {"G2": 6, "F4": 12, "E6": 12, "E7": 18, "E8": 30}
check("S6.3 THE LADDER END: a rung-4 group needs h = 210 and rank = "
      "phi(210) = 48; the families give h = 210 only at ranks "
      "{209, 105, 106} (A/BC/D), all != 48; every exceptional type "
      "has h <= 30 -- the (210, 48) rung exists ONLY as the register "
      "modulus with its Omega_adm = 48 state multiplicity",
      no_rung4 and all(v <= 30 for v in excep_h.values())
      and 209 + 1 == 210 and 2 * 105 == 210 and 2 * 106 - 2 == 210,
      kill="CONTROL-DEAD")

# ======================================================================
section("C: controls")
# ======================================================================
rad210_types = sorted(n for n in DATA if rad(DATA[n]["W"]) == 210)
check("C1 RADICAL NON-UNIQUENESS (honesty, must measure non-unique): "
      "types with rad|W| = 210: %s -- the single value selects "
      "nothing; the content is the TOWER (S2) + the forcing (S5) + "
      "the ladder end (S6)" % rad210_types,
      len(rad210_types) > 1 and "E8" in rad210_types,
      kill="CONTROL-DEAD")

q1 = (2, 3, 5, 11)
q2 = (3, 5, 7, 11)
prod_q1 = 1
for p in q1:
    prod_q1 *= p - 1
prod_q2 = 1
for p in q2:
    prod_q2 *= p - 1
check("C2 FOREIGN QUADRUPLES fire: {2,3,5,11}: prod(p-1) = %d != 48, "
      "gear order 10 not in compiler inventory {1,2,4,6}; "
      "{3,5,7,11}: prod(p-1) = %d != 48 and NO ramified/anchor slot "
      "(2 missing)" % (prod_q1, prod_q2),
      prod_q1 == 80 and prod_q2 == 480 and 10 not in (1, 2, 4, 6)
      and 2 not in q2, kill="CONTROL-DEAD")

alt1 = (rad(DATA["A3"]["W"]), rad(DATA["D4"]["W"]), rad(DATA["E8"]["W"]))
alt2 = (rad(DATA["A2"]["W"]), rad(DATA["D5"]["W"]))
check("C3 WRONG-TOWER CONTROL: A3 -> D4 -> E8 gives rad tower %s "
      "(skips 30); A2 -> D5 gives %s but A2 is not the compiler gear "
      "-- the primorial ladder is carried by the deployed chain"
      % (alt1, alt2),
      alt1 == (6, 6, 210) and alt2 == (6, 30), kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
if KILLS:
    verdict = KILLS[0]
elif n_pass == len(CHECKS) and hits48 == [(2, 3, 5, 7)]:
    verdict = "PRIMEFORCE-EXACT"
else:
    verdict = "PRIMEFORCE-PARTIAL"

print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS ADDS (measured, exploration only):
 * STRUCTURE SEAT: 210 = rad|W(E8)| -- the register modulus is the
   squarefree kernel of the E8 Weyl order, and the compiler chain
   A3 -> D5(+A3) -> E8 climbs the primorial ladder 3# -> 5# -> 7#
   (one new prime per stage; 5 enters at the carrier = g_car, 7 at
   the weld).  The v868 'pleasing coincidence' note gets a seat.
 * COMPILER FORCING: {2,3,5,7} is the UNIQUE quadruple of distinct
   primes with prod(p-1) = 48 = Omega_adm -- a second, independent
   pin next to the deployed Euler constants.
 * GEARS: (Z/210)* = C1 x C2 x C4 x C6 -- the anchor (trivial), the
   sheet (|Z2|), the clock (|mu4|), the hexagon (|R+(A3)|); total 48;
   exponent 12 = the clock wall.  6-vs-7 candidate reading: 6 = phi(7).
 * LADDER END: the primorial-Coxeter family A1 (2#), G2 (3#), E8 (5#)
   terminates in Lie theory; the (210, 48) rung is realized only by
   the register + its admissible state multiplicity.
NO ledger/paper/website claim; NO RH claim; NO physics claim beyond
the recorded exact identities.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
