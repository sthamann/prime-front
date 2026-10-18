#!/usr/bin/env python3
"""v635 -- PRIME.PCANON.01: P-canonicity + finer Hodge-chamber invariants.

Part A (canonicity of the v624 congruence matrix P):
  A0  sanity guards: P^T J_det P = J_fix exactly, det P = -6, det J_det = 2,
      det J_fix = 72; the v600/v604 integer conjugation pair (C_U, C_V) on
      the R-fixed lattice has the compiler characteristic polynomials
      (copied-matrix guard).
  A1  Smith normal forms of J_det, J_fix, P.
  A2  word-algebra role: is P in the Q-span (or Z-span) of the 7-word
      algebra {1, C_U, C_V, C_U C_V, C_V C_U, C_V^2, C_V C_U C_V}?  Are P's
      columns (+-) word-images of the fixed-lattice basis vectors?  (Deck
      acts omega-multiplicatively and R acts as identity on the fixed
      lattice, so the words in (C_U, C_V) are the available integral
      operator combinations.)
  A3  does P conjugate the word generators into integer matrices
      (P C_U P^{-1}, P C_V P^{-1} integral)?
  A4  the census: ALL integer 3x3 Q with entries in [-4,4] and
      Q^T J_det Q = J_fix (columns satisfy q^T J_det q = 16/-2/-2 and the
      three cross products 2/4/2); count, det distribution, and the
      distinguisher scan: minimal Frobenius norm, operator compatibility
      (both conjugations integral), column sign patterns.

Part B (finer chamber invariants; the coarse chamber does not separate,
        v627 H4):
  B1  for all complete windows: theta = projective angle of z = P^{-1} y to
      the positive eigendirection of J_fix; q(z)/||z||^2; the spacelike
      component ratio c1/c2 and spacelike plane angle phi.  NOTE: J_fix has
      Lorentz signature (1,2) -- ONE positive eigendirection; the task's
      'ratio of the two J_fix-positive components' is read as the ratio of
      the two SPACELIKE (negative-eigenvalue) components.
  B2  scramble controls: seeds (1,2,3) at the reference window h = 540 and
      at 5 spread windows; per-invariant separation statistics (global
      range test + per-window shift).

Verdict enums (frozen): P-SELECTED-MOD-SYMMETRY + FINE-INVARIANTS-SEPARATE
(as measured), FINE-INVARIANTS-PARTIAL, FINE-INVARIANTS-NO-SEPARATION,
MIXED.

FIREWALL: no marker changes; no positivity claim beyond the measured
surface, no RH statement; the [-4,4] census is a box census (the full
O(J_det,Z) torsor is infinite, typed).

PROVENANCE: discovery probe p_canonicity_hodge_fine_probe.py (2026-08-02,
18/18, verdicts P-SELECTED-MOD-SYMMETRY + FINE-INVARIANTS-SEPARATE).

Machinery: v563 read-only.  Python-only, counted per GATE.WOLFRAM.02.
"""
import itertools
import math
import os
import sys
import time
from collections import Counter

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ================================================================== A
print("=" * 78)
print("PART A: canonicity of P")
print("=" * 78)

x = sp.symbols("x")
Jdet = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
P = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
CU = sp.Matrix([[3, 0, 0], [-3, 0, 0], [0, 0, 0]])
CV = sp.Matrix([[2, 1, -1], [-2, -1, 2], [-2, -1, 2]])

check("A0.1 congruence guard: P^T J_det P = J_fix, det P = -6, "
      "det J_det = 2, det J_fix = 72",
      sp.simplify(P.T * Jdet * P - Jfix) == sp.zeros(3, 3)
      and P.det() == -6 and Jdet.det() == 2 and Jfix.det() == 72)

char_ok = (CU.charpoly(x).as_expr() == sp.expand(x ** 2 * (x - 3))
           and CV.charpoly(x).as_expr() == sp.expand(x * (x - 1) * (x - 2))
           and (CU + CV).charpoly(x).as_expr()
           == sp.expand((x - 1) * (x ** 2 - 5 * x + 3))
           and sp.trace(CU * CV) == 3)
check("A0.2 (C_U, C_V) copied-matrix guard: char C_U = x^2(x-3), "
      "char C_V = x(x-1)(x-2), char(C_U+C_V) = (x-1)(x^2-5x+3), "
      "tr(C_U C_V) = 3 (the v600 J1 identities)", char_ok)

snf_det = smith_normal_form(Jdet)
snf_fix = smith_normal_form(Jfix)
snf_P = smith_normal_form(P)
d_det = [int(abs(snf_det[i, i])) for i in range(3)]
d_fix = [int(abs(snf_fix[i, i])) for i in range(3)]
d_P = [int(abs(snf_P[i, i])) for i in range(3)]
check("A1.1 Smith normal forms computed", True,
      "SNF(J_det) = %s, SNF(J_fix) = %s, SNF(P) = %s" % (d_det, d_fix, d_P))

# ---- A2: word algebra role
words = [sp.eye(3), CU, CV, CU * CV, CV * CU, CV * CV, CV * CU * CV]
Wmat = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                  for w in words])
vecP = sp.Matrix(1, 9, [P[i, j] for i in range(3) for j in range(3)])
rank_W = Wmat.rank()
rank_aug = sp.Matrix.vstack(Wmat, vecP).rank()
in_span = (rank_aug == rank_W)
coeffs_str = "not in Q-span"
if in_span:
    a = sp.symbols("a0:7")
    sol = sp.solve(sp.Matrix(sum((a[i] * words[i] for i in range(1, 7)),
                                 a[0] * words[0]) - P),
                   list(a), dict=True)
    coeffs_str = str(sol)
check("A2.1 [measured] P in the Q-span of the 7-word algebra of "
      "(C_U, C_V)?  answer: %s" % in_span, True,
      "rank(words) = %d, rank(words+P) = %d; %s"
      % (rank_W, rank_aug, coeffs_str))

word_cols = set()
for w in words:
    for j in range(3):
        col = tuple(int(w[i, j]) for i in range(3))
        word_cols.add(col)
        word_cols.add(tuple(-c for c in col))
p_cols = [tuple(int(P[i, j]) for i in range(3)) for j in range(3)]
hits = [c for c in p_cols if c in word_cols]
check("A2.2 [measured] P columns as (+-) word-images of basis vectors: "
      "%d of 3 columns are word columns" % len(hits), True,
      "P columns %s; word-column hits: %s" % (p_cols, hits))

# ---- A3: conjugation integrality
PCU = P * CU * P.inv()
PCV = P * CV * P.inv()
int_CU = all(e.is_integer for e in PCU)
int_CV = all(e.is_integer for e in PCV)
check("A3.1 [measured] P C_U P^-1 integral? %s; P C_V P^-1 integral? %s"
      % (int_CU, int_CV), True,
      "P C_U P^-1 = %s, P C_V P^-1 = %s"
      % (sp.nsimplify(PCU).tolist(), sp.nsimplify(PCV).tolist()))

# ---- A4: the census
rng4 = range(-4, 5)
cols16 = [c for c in itertools.product(rng4, repeat=3)
          if c[0] * c[1] - c[2] * c[2] == 8]      # q^T J_det q = 16
colsm2 = [c for c in itertools.product(rng4, repeat=3)
          if c[0] * c[1] - c[2] * c[2] == -1]     # q^T J_det q = -2


def bil(u, v):
    return u[0] * v[1] + u[1] * v[0] - 2 * u[2] * v[2]


sols = []
for q1 in cols16:
    c2s = [q2 for q2 in colsm2 if bil(q1, q2) == 2]
    c3s = [q3 for q3 in colsm2 if bil(q1, q3) == 4]
    for q2 in c2s:
        for q3 in c3s:
            if bil(q2, q3) == 2:
                Q = tuple(tuple(int(v) for v in (q1[i], q2[i], q3[i]))
                          for i in range(3))
                sols.append(Q)

P_rows = tuple(tuple(int(P[i, j]) for j in range(3)) for i in range(3))
check("A4.1 census: %d integer solutions Q with entries in [-4,4] and "
      "Q^T J_det Q = J_fix; P is among them: %s"
      % (len(sols), P_rows in sols), P_rows in sols,
      "(column candidates: %d with norm 16, %d with norm -2)"
      % (len(cols16), len(colsm2)))


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def adj3(A):
    return [[A[1][1] * A[2][2] - A[1][2] * A[2][1],
             A[0][2] * A[2][1] - A[0][1] * A[2][2],
             A[0][1] * A[1][2] - A[0][2] * A[1][1]],
            [A[1][2] * A[2][0] - A[1][0] * A[2][2],
             A[0][0] * A[2][2] - A[0][2] * A[2][0],
             A[0][2] * A[1][0] - A[0][0] * A[1][2]],
            [A[1][0] * A[2][1] - A[1][1] * A[2][0],
             A[0][1] * A[2][0] - A[0][0] * A[2][1],
             A[0][0] * A[1][1] - A[0][1] * A[1][0]]]


def matmul3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


CU_l = [[3, 0, 0], [-3, 0, 0], [0, 0, 0]]
CV_l = [[2, 1, -1], [-2, -1, 2], [-2, -1, 2]]


def conj_integral(Q, C):
    d = det3(Q)
    A = adj3(Q)
    M = matmul3(matmul3([list(r) for r in Q], C), A)
    return all(m % d == 0 for row in M for m in row)


dets = Counter(det3(Q) for Q in sols)
frob = {Q: sum(v * v for r in Q for v in r) for Q in sols}
fmin = min(frob.values())
at_min = [Q for Q in sols if frob[Q] == fmin]
op_ok = [Q for Q in sols
         if conj_integral(Q, CU_l) and conj_integral(Q, CV_l)]
col1pos = [Q for Q in sols if all(Q[i][0] > 0 for i in range(3))]
col1nn = [Q for Q in sols if all(Q[i][0] >= 0 for i in range(3))]

check("A4.2 census det distribution: %s (torsor under the infinite "
      "O(J_det,Z); box census only)" % dict(dets), True)
check("A4.3 distinguisher: minimal Frobenius norm^2 = %d, attained by %d "
      "solutions; P (norm^2 = %d) among them: %s"
      % (fmin, len(at_min), frob[P_rows], P_rows in at_min), True,
      "min-norm solutions: %s" % (at_min if len(at_min) <= 8 else
                                  str(len(at_min)) + " sols"))
check("A4.4 distinguisher: operator compatibility (BOTH P C P^-1 "
      "integral for C_U and C_V): %d of %d solutions; P among them: %s"
      % (len(op_ok), len(sols), P_rows in op_ok), True,
      "op-compatible: %s" % (op_ok if len(op_ok) <= 8 else
                             str(len(op_ok)) + " sols"))
check("A4.5 distinguisher: strictly positive first column: %d sols; "
      "nonnegative first column: %d sols; P has col1 = (3,3,-1) "
      "(mixed sign)" % (len(col1pos), len(col1nn)), True)

frob_at_op = sorted(frob[Q] for Q in op_ok) if op_ok else []
check("A4.6 combined distinguisher scan executed", True,
      "Frobenius norms of op-compatible sols: %s"
      % (frob_at_op[:20] if frob_at_op else "none"))

# A4.7: classes modulo the NATURAL prime-side symmetries (all in
# O(J_det,Z)): global sign, the X11 <-> X22 swap, the X12 sign flip
T_swap = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
T_sgn = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
T_min = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
G8 = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
frontier = [G8[0]]
while frontier:
    g = frontier.pop()
    for t in (T_swap, T_sgn, T_min):
        h = matmul3(t, g)
        if h not in G8:
            G8.append(h)
            frontier.append(h)
iso_ok = all(matmul3(matmul3([list(r) for r in
                              zip(*g)], [[0, 1, 0], [1, 0, 0],
                                         [0, 0, -2]]), g)
             == [[0, 1, 0], [1, 0, 0], [0, 0, -2]] for g in G8)


def orbit_class(Q):
    return frozenset(tuple(tuple(r) for r in matmul3(g, [list(r_)
                                                         for r_ in Q]))
                     for g in G8)


classes = {}
for Q in sols:
    classes.setdefault(orbit_class(Q), []).append(Q)
P_class = orbit_class(P_rows)
min_is_P_class = set(at_min) == set(P_class) & set(sols)
op_classes = {orbit_class(Q) for Q in op_ok}
check("A4.7 modulo the order-%d natural prime-side symmetry group "
      "(global sign, X11<->X22, X12-sign; all verified in O(J_det,Z)): "
      "%d classes; the minimal-Frobenius set IS exactly P's class: %s; "
      "op-compatible classes: %d of %d"
      % (len(G8), len(classes), min_is_P_class, len(op_classes),
         len(classes)), len(G8) == 8 and iso_ok,
      "class sizes %s" % sorted(len(v) for v in classes.values()))

verdict_A = "P-CANONICITY-OPEN"
if op_ok == [P_rows] or at_min == [P_rows]:
    verdict_A = "P-SELECTED"
elif min_is_P_class and P_rows in op_ok:
    verdict_A = ("P-SELECTED-MOD-SYMMETRY (unique minimal-Frobenius "
                 "class, op-compatible)")
elif P_rows in op_ok and len(op_ok) <= 8:
    verdict_A = "P-NARROWED"

# ================================================================== B
print("=" * 78)
print("PART B: finer chamber invariants vs scramble")
print("=" * 78)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)

PinvN = np.array(sp.Matrix(P).inv().evalf(20).tolist(), dtype=float)
JfixN = np.array(Jfix.tolist(), dtype=float)
w_, V_ = np.linalg.eigh(JfixN)
for j in range(3):
    k = int(np.argmax(np.abs(V_[:, j])))
    if V_[k, j] < 0:
        V_[:, j] *= -1.0
check("B0.1 J_fix eigenvalues (ascending): %s -- signature (1,2), ONE "
      "positive direction (the task's 'two positive components' is read "
      "as the two SPACELIKE components)"
      % np.array2string(w_, precision=6), w_[0] < 0 and w_[1] < 0
      and w_[2] > 0)


def invariants(S):
    y = np.array([S[0, 0], S[1, 1], S[0, 1]], dtype=float)
    z = PinvN @ y
    nz = float(np.linalg.norm(z))
    c = V_.T @ z
    theta = math.degrees(math.acos(min(1.0, abs(float(c[2])) / nz)))
    qn = float(z @ (JfixN @ z)) / nz ** 2
    ratio = float(c[0] / c[1]) if c[1] != 0 else float("inf")
    phi = math.degrees(math.atan2(float(c[1]), float(c[0]))) % 180.0
    return theta, qn, ratio, phi, float(np.linalg.det(S))


u_max = float(core.U_ALL[-1])
rows = []
for kz in core.frame_a_zones():
    r = core.build_window(kz)
    if r["h"] == 1292 or 2.0 * r["alpha"] > u_max:
        continue
    rows.append((kz, r["h"], r["S"]))

true_inv = {kz: invariants(S) for kz, h, S in rows}
qz_resid = 0.0
for kz, h, S in rows:
    y = np.array([S[0, 0], S[1, 1], S[0, 1]], dtype=float)
    z = PinvN @ y
    qz_resid = max(qz_resid,
                   abs(float(z @ (JfixN @ z))
                       - 2.0 * float(np.linalg.det(S))))
check("B1.1 transport bookkeeping: %d complete windows, max "
      "|q(z) - 2 det S| = %.2e" % (len(rows), qz_resid),
      len(rows) == 67 and qz_resid < 1e-9)

names = ["theta_deg", "q/|z|^2", "c1/c2", "phi_deg"]
tvals = {n: [true_inv[kz][i] for kz, h, S in rows]
         for i, n in enumerate(names)}
for n in names:
    v = tvals[n]
    print("    true %-9s: min %.6g  max %.6g  mean %.6g  std %.6g"
          % (n, min(v), max(v), float(np.mean(v)), float(np.std(v))))
check("B1.2 true-family invariant ranges recorded (67 windows)", True)

# scramble windows: reference h=540 + 5 spread picks
kz_ref = [kz for kz, h, S in rows if h == 540][0]
order = sorted(range(len(rows)), key=lambda i: rows[i][1])
pick_idx = [order[0], order[len(rows) // 4], order[len(rows) // 2],
            order[3 * len(rows) // 4], order[-1]]
extra = []
for i in pick_idx:
    if rows[i][0] != kz_ref and rows[i][0] not in extra:
        extra.append(rows[i][0])
scr_kz = [kz_ref] + extra
SEEDS = (1, 2, 3)
scr_inv = {}
for kz in scr_kz:
    for seed in SEEDS:
        rs = core.build_window(kz, scramble_seed=seed)
        scr_inv[(kz, seed)] = invariants(rs["S"])

h_of = {kz: h for kz, h, S in rows}
print("    scramble table (window h | seed | theta, q/|z|^2, c1/c2, phi "
      "| true values):")
for kz in scr_kz:
    ti = true_inv[kz]
    print("      h=%-5d true : theta %.6g  qn %.6g  ratio %.6g  phi %.6g"
          % (h_of[kz], ti[0], ti[1], ti[2], ti[3]))
    for seed in SEEDS:
        si = scr_inv[(kz, seed)]
        print("      h=%-5d s=%d  : theta %.6g  qn %.6g  ratio %.6g  "
              "phi %.6g" % (h_of[kz], seed, si[0], si[1], si[2], si[3]))

n_scr = len(scr_inv)
sep_stats = {}
for i, n in enumerate(names):
    lo, hi = min(tvals[n]), max(tvals[n])
    outside = sum(1 for v in scr_inv.values()
                  if not (lo <= v[i] <= hi))
    sep_stats[n] = outside
check("B2.1 separation census: scrambles outside the true 67-window "
      "range, per invariant: %s (of %d scrambles each)"
      % (sep_stats, n_scr), True)

shift_stats = {}
for i, n in enumerate(names):
    tstd = float(np.std(tvals[n]))
    shifts = [abs(scr_inv[(kz, s)][i] - true_inv[kz][i])
              / (tstd if tstd > 0 else 1.0)
              for kz in scr_kz for s in SEEDS]
    shift_stats[n] = (min(shifts), float(np.median(shifts)), max(shifts))
check("B2.2 per-window shift in units of the true-family std "
      "(min/median/max): %s"
      % {k: tuple(round(v, 3) for v in vv)
         for k, vv in shift_stats.items()}, True)

sep_verdicts = {}
for n in names:
    if sep_stats[n] == n_scr:
        sep_verdicts[n] = "SEPARATES"
    elif sep_stats[n] == 0:
        sep_verdicts[n] = "NO-SEPARATION"
    else:
        sep_verdicts[n] = "PARTIAL(%d/%d)" % (sep_stats[n], n_scr)
verdict_B = ("FINE-INVARIANTS-SEPARATE"
             if any(v == "SEPARATES" for v in sep_verdicts.values())
             else ("FINE-INVARIANTS-PARTIAL"
                   if any(v.startswith("PARTIAL")
                          for v in sep_verdicts.values())
                   else "FINE-INVARIANTS-NO-SEPARATION"))

# ================================================================== summary
print("=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print("VERDICT A: %s" % verdict_A)
print("VERDICT B: %s -- per invariant: %s" % (verdict_B, sep_verdicts))
print("elapsed: %.1f s" % (time.time() - T0))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
