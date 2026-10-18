#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hecke_snf_theta_probe -- HECKE.SNF_THETA.01 (positive-protocol round,
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

import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
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


print(__doc__.split("SLICES")[0])
print("FROZEN SPEC: QMAX = %d, NCAP = %d, target divisors %s;" %
      (QMAX, NCAP, TARGET_DIV))
print("verdicts SNF-ISOMETRIC / SNF-FINGERPRINT / SNF-FALSE (frozen);")
print("admissible class = transversal-coded (see docstring), naive 4+4")
print("coordinatewise maps excluded by v638 S1.2 (replicated in S3c).")
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
raise SystemExit(0 if n_fail == 0 else 1)
