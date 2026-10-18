#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hecke_mu4_packet_probe -- HECKE.MU4_PACKET.01 (positive-protocol
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

NSER = 64                 # q-series order (frozen)
NENUM = 6                 # enumeration shells (norm <= 12, frozen)
TMAX = 8 * NSER           # t = q^{1/8} order
SEED = 20260805           # control RNG seed (frozen)
AP_EXPECTED = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}


def check(name, ok):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name), flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return bool(ok)


def info(msg):
    print("        %s" % msg, flush=True)


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
raise SystemExit(0 if FAIL == 0 else 1)
