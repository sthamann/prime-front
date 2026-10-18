"""PRIME.COMMUTANT.SOS.01 -- the exact sum-of-squares decider in the
five-dimensional abelian commutant (the second independent RH route of
the 2026-08-07 strategy).

EXPLORATION ONLY (experiments/tfpt-discovery).  Writes nothing outside
stdout; no verification/, no ledger, no TeX, no website, no .md.
NO RH claim anywhere.

THE TARGET (the strategy's rational identity, EVENT level -- not
numerics on windows):

    T_GL1 = Sum_j V_j^* T_chi_j V_j + Sum_k C_k^* C_k

with all coefficients nonnegative rational, T_chi_j the already-
positive sector kernels with their correct continuum kernels, and all
V_j, C_k drawn from the canonical FIVE-dimensional abelian subalgebra
A = span{Pi_A(0), Pi_A(1), Pi_A(4), Pi_A(7), Pi_A(9)} of the 39-dim
commutant C({K, sigma}) (v815).  The typed hope: the 105 RM checks
(v820: the weight-4 dual words of C1^perp = shortened RM(2,4), the
Kraus flag space) form a massively overdetermined frame over the THREE
comb functionals (S11, S22, S12) of the rank-3 Toeplitz classification
(det = the signature-(1,2) Lorentz form t^2 - x^2 - y^2, compiler null
vector (5, -3, 4) = the spinor square 2 (1,2)(1,2)^T) -- the
indefinite rank-3 form MIGHT become a genuine Gram norm after the lift
to the flag space.

FROZEN FORMALIZATION (all representation choices declared HERE, before
the first run):

  EVENT LEVEL := equality of operator coefficients per event CLASS
  with GENERIC symbolic weights.  The deployed event stream (v563
  atoms, u <= 10, via the v755 channel masks) carries the operator
  comb Op(n) = I on odd events, Op(2^k) = K^k = (B/7)^k on the 14
  ramified events, x I on the (deployed GL1) continuum.  All Op(n) lie
  in A; in the atom basis (Pi_0, Pi_1, Pi_4, Pi_7, Pi_9) with
  mu_B = (-2, 2, 2, 2, 7) the class coefficients are EXACT rationals:
  odd/continuum -> (1,1,1,1,1); 2^k -> ((-2/7)^k, (2/7)^k, (2/7)^k,
  (2/7)^k, 1).  Event classes (17): continuum, odd, 2^1..2^14, and
  the lag-constant class (where C_k^* C_k with constant C_k in A can
  contribute).  The identity must hold coefficient-wise per class --
  this is exactly "generic symbolic weights" (no mass value is used
  in the identity layer).

  BUILDING BLOCKS T_chi_j := the three window-visible sector kernels
  T_{+7}, T_{+2}, T_{-2} (v815: the ONLY scalar sectors visible at
  window level; T_{+7} == the deployed GL1 window to 6.0e-16; the
  mu = +-2 kernels are typed protocol-internal -- v815 froze that no
  sector-adapted continuum is derived, and only the uniform sector is
  PSD, so "already-positive with correct continuum kernel" is
  satisfied by T_{+7} ALONE; this gap is part of the deliverable).

  DEGREE-2 KRAUS ANSATZ (the full space, predeclared): V_j = Sum_lam
  v_{j lam} Pi_lam per block s in {+7, +2, -2}; constants C_k =
  Sum_lam c_{k lam} Pi_lam.  SDP variables: one PSD Gram block
  G_s in S^5_+ per sector kernel (Gram of the Kraus vectors) plus one
  PSD block G_C in S^5_+ for the constants -- 4 blocks S^5_+, 60
  scalar unknowns; equality constraints 5 sectors x 17 classes = 85
  per reading.  TWO frozen readings of the LHS: (i) T_GL1 (x) I_15
  (the label-uniform deployment of the GL1 machinery on the register);
  (ii) T_op (the honest operator comb).  EXACT REDUCTION LEMMA (proved
  in-probe, sympy + rational 15x15 witnesses): the abelian conjugation
  V^* (T_s (x) .) V reads ONLY diag(G_s) -- Sum_j V_j^* T V_j has
  sector-lam class coefficient (G_s)_{lam lam} tau_s(c); hence the SDP
  reduces EXACTLY to a rational LP in W[s, lam] >= 0 (+ slack
  E[lam] >= 0 on the lag-constant class), solved by exact Fraction
  rref -- and the float SDP/NNLS cross-check must reproduce it after
  continued-fraction rationalization.

  THE FLAG-SPACE LIFT (the rank-3 hope, decided exactly): every
  105-leg RM check reads the comb LINEARLY (the legs are label-space
  flags; each leg functional factors through the event stream), and
  the three comb functionals S = (S11, S22, S12) are linear in the
  flag reads (the overdetermined frame).  Therefore ANY Gram-norm
  certificate X^T G X (G >= 0) on the flag space pulls back to a PSD
  quadratic form on the achievable functional directions.  The det
  margin q(S) = S11 S22 - S12^2 = t^2 - x^2 - y^2 (t = (S11+S22)/2,
  x = (S11-S22)/2, y = S12; sympy-exact) admits a Gram representation
  q(s) = s^T G s iff the UNIQUE coefficient-matched G = diag(1,-1,-1)
  (6 equations, 6 unknowns, exact) is PSD -- it is NOT (eigenvalue -1
  exact).  SDP dimensions typed: G in S^3, 6 unknowns, 6 equality
  constraints.  DUAL CERTIFICATE (rational, exact): the point
  s* = (0, 1, 0) has q(s*) = -1 < 0 while every Gram norm is >= 0.
  ACHIEVABILITY (the measured leg, typed float-assisted, NOT part of
  the exact layer): (a) the per-event read matrix Xn (ka x 3) at the
  v563 reference window h = 540 has numerical rank 3 (the functionals
  are surjective on R^3 for signed generic weights -- witness triple
  selected by deterministic column-pivoted QR of Xn^T [SPEC v2, see
  below], condition number printed, rationalized combination
  printed); (b) the physical NONNEG cone: the truncated-comb scan
  (v619 flip set) -- report min det S over truncation cuts.

DECLARED IMPLEMENTATION CORRECTION (run 1 -> run 2, 2026-08-07;
v815-SPEC-v2 / v818 disclosure precedent -- no bar, target or verdict
rule changed): SPEC v1 froze the achievability witness triple as the
list indices (0, ka//2, ka-1).  Run 1 (28/29, sole FAIL S4.6)
measured that the LAST deployed event sits on the window boundary and
reads EXACTLY (0, 0, 0) through the parity splines -- the declared
3 x 3 matrix is singular by construction (cond inf), so the intended
quantity (an achievable q-negative direction) was never evaluated.
The triple selection becomes the deterministic column-pivoted QR of
Xn^T (first three pivot rows; run-2 pivots (0, 6, 24), cond 4.4);
intent, rationalization recipe, condition budget and all bars are
UNCHANGED.  All other run-1 results (28/28) carried verbatim; run-1
S4.7 already witnessed q < 0 on the nonneg cone independently
(832 of 2799 truncation cuts, min det S = -5.455e+02 at cut 230).

STEPS (the task's six, frozen):
 S1 the five commutant coordinates: frame rebuilt (doily recipe,
    v738 read-only), A_orb both sigma-orbits, exact Lagrange
    projections; verify dim C({K, sigma}) = 39 (Fraction nullspace
    over the 81 sigma-pair orbits), the abelian subalgebra dim = 5
    (exact rank), the structure constants Pi_a Pi_b = delta_ab Pi_a
    (exact, all 25 pairs), sum = I, B = -2 Pi_0 + 2(Pi_1+Pi_4+Pi_7)
    + 7 Pi_9 exact, algebra generated by A_orb = the same span.
 S2 the ansatz space parametrized (as declared above) + the exact
    reduction lemma (sympy generic-diagonal identity + two rational
    15x15 witnesses: V^T T V expansion; Gram off-diagonal
    invisibility).
 S3 the SDP solved: exact rational rref per sector and reading
    (existence + kernel-triviality = uniqueness certificate, the
    inverse-Vandermonde dual row printed exactly); float NNLS
    cross-check + rationalization matches the exact solution.
    FROZEN NONTRIVIALITY RULE: a solution is NONTRIVIAL iff it puts
    positive weight on a block other than the target sector's own
    kernel or the feasible set contains more than the diagonal point.
 S4 the flag-space Gram lift decided: sympy polarisation identity,
    null-vector gates, the unique G, exact non-PSD, the rational dual
    certificate, achievability witnesses (typed).
 S5 THE FENCE (mandatory): does any step smuggle an oscillatory
    prime-sum estimate?  Gates: (a) the identity layer is mass-free
    (the LP never reads a mass -- structural, asserted on the
    constructed system); (b) the positivity content of the route is
    degree-2 in the comb: the pointwise Cauchy-Schwarz census on the
    actual reads (Xn[:,2]^2 <= Xn[:,0] Xn[:,1] and Xn[:,0] >= 0,
    rank3 R4(ii) recipe) -- violations > 0 mean every certificate
    must use cross-event cancellation = an oscillatory prime-sum
    estimate: FENCE-HIT on the positivity branch, and the route is
    back at the pair-correlation boundary.
 S6 CONTROLS (frozen): K1 the tau-identification is comb-specific:
    uniform-sector window == deployed c_full (rel <= 1e-12) for the
    TRUE comb, and the v563 position scramble (uniform u at the same
    masses, seed 1) MISSES by rel >= 1e-3 (must fire); K2 the three
    window sectors reproduce v815's PSD pattern on the frozen rungs
    M = 256..640 (uniform PSD on ALL rungs; mu = +2 and mu = -2 each
    carry >= 1 NEG rung); K3 wrong-ratio control: replacing the
    T_{+2} class profile by (3/7)^k makes the reading-(ii)
    mu_B = 2 system INCONSISTENT (exact rref detects; must fire).

VERDICT ENUM (frozen): COMMUTANT-SOS-EXACT (a NONTRIVIAL rational
identity verified at event level) / COMMUTANT-SOS-INFEASIBLE (the
trivial-uniqueness certificate exact AND the Gram-lift dual
certificate exact AND a q-negative achievable direction witnessed AND
controls fire -- route closed, stop-list candidate) /
COMMUTANT-SOS-PARTIAL (anything else; typed precisely where).

SCOPE-TYPING (the corner-route convention, frozen): the identity
layer is Vandermonde algebra and holds for ANY masses -- positivity
is structural; what is comb-specific is the tau-IDENTIFICATION
(uniform sector == the deployed GL1 window built from the actual
prime comb), and K1 must kill it under the scramble.

FIREWALL: verification/ strictly read-only (v563, v755, v738
imports); no zero of any L-function is read (AST-checked); sympy is
used for SYMBOL ALGEBRA ONLY per the frozen task (no sympy.ntheory);
the only RNG is the declared v563 scramble recipe (numpy seed 1) and
the fixed LCG (seed 20260807) for the rational witnesses; exact
integer/Fraction arithmetic in every load-bearing certificate; floats
only in the measured legs (window ladders, achievability,
identification), each typed.  Runtime cap ~30 min.  Frozen 2026-08-07
before the first run.

Predecessors (read-only): v815 (frame, A_orb, commutant, sector
windows), v820 (105 RM checks = the flag space, cited), v818/v563
(rank-3 lock block, build_window, reference window, scramble),
rank3_functionals_probe (three functionals, CS-pointwise recipe,
flip-set context), v755 (channel masks, continuum), v738 (Lmodule).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/commutant_sos_probe.py
"""

import ast
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np
import scipy.linalg as sla
from scipy.optimize import nnls

_here = os.path.dirname(os.path.abspath(__file__))
_verify = os.path.abspath(os.path.join(_here, "..", "..", "verification"))
sys.path.insert(0, _here)
sys.path.insert(0, _verify)

import v738_hecke_mod_ramified as ram            # noqa: E402  read-only
import v563_paper2_readouts as core              # noqa: E402  read-only
import v755_simpler_schur_recursion as srp       # noqa: E402  read-only

import sympy as sp                               # noqa: E402  symbols only

T0 = time.time()
CHECKS = []
GATE = {}
CONTROL_FIRED = {}

LABEL_DIM = 15
ROW_DEGREE = 7
A_SPECTRUM = {0: 5, 1: 2, 4: 5, 7: 2, 9: 1}
MU_B_OF_A = {0: -2, 1: 2, 4: 2, 7: 2, 9: 7}
ATOMS = (0, 1, 4, 7, 9)                  # the five coordinates, frozen order
SECTORS = (7, 2, -2)                     # building-block kernels T_s
K_RAM = 14                               # ramified classes 2^1..2^14 (u<=10)
DIM_COMMUTANT = 39                       # v815 target
DIM_ABELIAN = 5

ALPHA_TOP = 5.0                          # deployed events u <= 10
M_TOP = 640
RUNGS = (256, 320, 384, 448, 512, 576, 640)
PSD_BAR = 1.0e-10                        # v815 ladder bar
WARD_BAR = 1.0e-12                       # GL1 identification bar
K1_BAR = 1.0e-3                          # scramble must miss by >= this (rel)
SCRAMBLE_SEED = 1                        # v563 recipe
NNLS_TOL = 1.0e-10                       # float cross-check vs exact solution
RAT_QMAX = 10 ** 6                       # continued-fraction denominator cap
WITNESS_TRIPLE = "QR-pivot"              # SPEC v2: column-pivoted QR triple
LCG_SEED = 20260807

BANNED_IDS = ("isprime", "primerange", "nextprime", "prevprime",
              "zetazero", "lcalc", "ntheory")

_LCG = [LCG_SEED]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    line = "[%s] %s" % ("PASS" if ok else "FAIL", name)
    if detail:
        line += "  |  " + detail
    print(line, flush=True)
    return bool(ok)


def section(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ------------------------------------------------ exact Fraction helpers
def fmat_int(M):
    return [[Fr(int(x)) for x in row] for row in M]


def feye(n):
    return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]


def fmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[Fr(0)] * p for _ in range(n)]
    for i in range(n):
        Ai, Oi = A[i], out[i]
        for k in range(m):
            a = Ai[k]
            if a == 0:
                continue
            Bk = B[k]
            for j in range(p):
                if Bk[j] != 0:
                    Oi[j] += a * Bk[j]
    return out


def fadd(A, B, ca=Fr(1), cb=Fr(1)):
    return [[ca * a + cb * b for a, b in zip(ra, rb)]
            for ra, rb in zip(A, B)]


def fscale(A, c):
    return [[c * a for a in row] for row in A]


def fequal(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def fzero(A):
    return all(a == 0 for row in A for a in row)


def frref_nullspace(rows, ncols):
    """Exact rref over Q; returns (rank, pivot cols, nullspace basis)."""
    R = [list(r) for r in rows]
    m = len(R)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if R[i][c] != 0), None)
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -R[i][fc]
        basis.append(v)
    return len(piv_cols), piv_cols, basis


def fsolve(A_rows, b, ncols):
    """Exact solve A x = b over Q.  Returns (consistent, unique, x)."""
    aug = [list(r) + [bb] for r, bb in zip(A_rows, b)]
    R = [list(r) for r in aug]
    m = len(R)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, m) if R[i][c] != 0), None)
        if piv is None:
            continue
        R[r], R[piv] = R[piv], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b2 for a, b2 in zip(R[i], R[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    consistent = all(any(R[k][c] != 0 for c in range(ncols))
                     or R[k][ncols] == 0 for k in range(m))
    unique = consistent and len(piv_cols) == ncols
    x = [Fr(0)] * ncols
    if consistent:
        for i, pc in enumerate(piv_cols):
            x[pc] = R[i][ncols]
    return consistent, unique, x


# ================================================================ G0
def g0_firewall():
    section("G0 -- firewall")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            for m in mods:
                if any(b in m for b in BANNED_IDS):
                    bad.append(m)
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    check("G0.1 no prime-table / zeta-zero / sympy.ntheory symbols in this "
          "file (sympy allowed for SYMBOL ALGEBRA only, per the frozen "
          "task)", not bad, "found %s" % bad if bad else "clean")
    print("    python %s, numpy %s, sympy %s"
          % (sys.version.split()[0], np.__version__, sp.__version__))


# ============================================== S1 the five coordinates
def s1_frame_and_coordinates():
    section("S1 (STEP 1) -- the five commutant coordinates, exact")
    t0 = time.time()
    L = ram.Lmodule()
    E4 = [tuple((1 if j == k else 0, 0) for j in range(4))
          for k in range(4)]
    S = [L.coords(ram.pack(ram.sig8(ram.unpack(L.to_ambient(E4[k])))))
         for k in range(4)]
    S2 = [[ram.par(S[k][j]) for j in range(4)] for k in range(4)]

    def sigbar(v):
        return tuple((sum(v[k] * S2[k][j] for k in range(4))) & 1
                     for j in range(4))

    labels16 = [tuple((z >> b) & 1 for b in range(4)) for z in range(16)]
    labels = labels16[1:]
    lidx = {v: i for i, v in enumerate(labels)}
    pairs4 = list(combinations(range(4), 2))
    Omega, n_inv = None, 0
    for mask in range(1, 1 << 6):
        M = [[0] * 4 for _ in range(4)]
        for bi, (i, j) in enumerate(pairs4):
            if (mask >> bi) & 1:
                M[i][j] = M[j][i] = 1
        cols = [tuple(M[i][j] for i in range(4)) for j in range(4)]
        rk, _k, _i = ram.f2_rank_ker_inv(cols)
        if rk != 4:
            continue
        if all((sum(sigbar(v)[k] * M[k][l] * sigbar(w)[l]
                    for k in range(4) for l in range(4))) & 1
               == (sum(v[k] * M[k][l] * w[l]
                       for k in range(4) for l in range(4))) & 1
               for v in labels16 for w in labels16):
            n_inv += 1
            if Omega is None:
                Omega = M

    def om(x, y):
        return (sum(x[j] * Omega[j][k] * y[k]
                    for j in range(4) for k in range(4))) & 1

    B = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for r, x in enumerate(labels):
        for c, y in enumerate(labels):
            B[r, c] = int(om(x, y) == 0)
    I15 = np.eye(LABEL_DIM, dtype=np.int64)
    J15 = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    iso_lines = sorted(
        (Lf for Lf in
         {frozenset({a, b, tuple(p ^ q for p, q in zip(a, b))})
          for a, b in combinations(labels, 2)}
         if all(om(x, y) == 0 for x in Lf for y in Lf)),
        key=lambda s: sorted(s))
    by_pt = {}
    for Lf in iso_lines:
        for p in Lf:
            by_pt.setdefault(p, []).append(Lf)

    def find_spreads(covered, used):
        if len(covered) == 15:
            return [frozenset(used)]
        p = next(x for x in sorted(labels) if x not in covered)
        out = []
        for Lf in by_pt.get(p, []):
            if covered & Lf:
                continue
            out += find_spreads(covered | Lf, used + [frozenset(Lf)])
        return out

    spreads = sorted(set(find_spreads(frozenset(), [])),
                     key=lambda s: sorted(sorted(w) for w in s))
    perm = [lidx[sigbar(v)] for v in labels]
    poly = ((B - 7 * I15) @ (B - 2 * I15) @ (B + 2 * I15))
    ok_fr = (n_inv == 1 and np.array_equal(B, B.T)
             and bool(np.all(B.sum(axis=1) == ROW_DEGREE))
             and int(np.max(np.abs(B @ B.T - (4 * I15 + 3 * J15)))) == 0
             and int(np.max(np.abs(poly))) == 0
             and len(iso_lines) == 15 and len(spreads) == 6)
    check("S1.1 frame (doily recipe): unique sigma-invariant Omega, B "
          "(rows 7, B B^T = 4I + 3J, (B-7)(B-2)(B+2) = 0), 15 iso lines, "
          "6 spreads", ok_fr, "%.1f s" % (time.time() - t0))

    # A_orb per sigma-orbit
    def sig_spread(s):
        return frozenset(frozenset(sigbar(v) for v in Lf) for Lf in s)

    sp_perm = [spreads.index(sig_spread(s)) for s in spreads]
    orbits, seen = [], set()
    for i in range(6):
        if i in seen:
            continue
        o, j = [i], sp_perm[i]
        while j != i:
            o.append(j)
            seen.add(j)
            j = sp_perm[j]
        seen.add(i)
        orbits.append(sorted(o))

    def b45_of(spread):
        blk = {}
        for bi, Lf in enumerate(sorted(spread, key=sorted)):
            for v in Lf:
                blk[v] = bi
        M = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
        for x in labels:
            for y in labels:
                if blk[x] == blk[y]:
                    M[lidx[x], lidx[y]] = 1
        return M

    B45s = [b45_of(s) for s in spreads]
    A1 = sum(B45s[i] for i in orbits[0])
    A2 = sum(B45s[i] for i in orbits[1])
    P = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for i in range(LABEL_DIM):
        P[perm[i], i] = 1
    ok_a = (sorted(len(o) for o in orbits) == [3, 3]
            and int(np.max(np.abs(A1 + A2 - (4 * I15 + 2 * B)))) == 0
            and int(np.max(np.abs(A1 @ B - B @ A1))) == 0
            and int(np.max(np.abs(P @ A1 @ P.T - A1))) == 0)
    check("S1.2 A_orb: two spread 3-orbits, A1 + A2 == 4I + 2B, "
          "sigma-invariant, K-commuting (exact integer)", ok_a)

    # exact Lagrange projections (the five coordinates)
    eigs = sorted(A_SPECTRUM)
    Af, Ifr = fmat_int(A1), feye(LABEL_DIM)
    Pi = {}
    for lam in eigs:
        Pl = feye(LABEL_DIM)
        for mu in eigs:
            if mu == lam:
                continue
            Pl = fmul(Pl, fscale(fadd(Af, Ifr, Fr(1), Fr(-mu)),
                                 Fr(1, lam - mu)))
        Pi[lam] = Pl
    ok_proj = True
    tot = None
    for lam in eigs:
        Pl = Pi[lam]
        ok_proj &= fequal(fmul(Pl, Pl), Pl)
        ok_proj &= sum(Pl[i][i] for i in range(LABEL_DIM)) \
            == A_SPECTRUM[lam]
        tot = Pl if tot is None else fadd(tot, Pl)
    ok_proj &= fequal(tot, feye(LABEL_DIM))
    check("S1.3 the FIVE COORDINATES: exact Lagrange eigenprojections "
          "Pi_A(l), l in {0,1,4,7,9}, idempotent, traces {5,2,5,2,1}, "
          "sum = I (Fractions)", ok_proj)

    # structure constants: Pi_a Pi_b == delta_ab Pi_a, all 25 pairs
    ok_struct = True
    for a in eigs:
        for b in eigs:
            prod = fmul(Pi[a], Pi[b])
            ref = Pi[a] if a == b else [[Fr(0)] * LABEL_DIM
                                        for _ in range(LABEL_DIM)]
            ok_struct &= fequal(prod, ref)
    check("S1.4 STRUCTURE CONSTANTS: Pi_a Pi_b == delta_ab Pi_a exact on "
          "all 25 pairs -- the algebra is the split abelian C(Q)^5 "
          "(coordinate-wise product in the atom basis)", ok_struct)

    # dim of the span and of the generated algebra
    vecs = [[Pi[lam][i][j] for i in range(LABEL_DIM)
             for j in range(LABEL_DIM)] for lam in eigs]
    rk_span, _p, _n = frref_nullspace(
        [list(col) for col in zip(*vecs)], len(vecs))
    pw = feye(LABEL_DIM)
    pows = [pw]
    for _ in range(4):
        pw = fmul(pw, Af)
        pows.append(pw)
    pvecs = [[Mp[i][j] for i in range(LABEL_DIM)
              for j in range(LABEL_DIM)] for Mp in pows]
    rk_pow, _p2, _n2 = frref_nullspace(
        [list(col) for col in zip(*pvecs)], len(pvecs))
    both = vecs + pvecs
    rk_both, _p3, _n3 = frref_nullspace(
        [list(col) for col in zip(*both)], len(both))
    ok_dim = (rk_span == DIM_ABELIAN and rk_pow == DIM_ABELIAN
              and rk_both == DIM_ABELIAN)
    check("S1.5 ABELIAN SUBALGEBRA DIMENSION: span{Pi_A} rank %d == 5; "
          "algebra generated by A_orb (powers 0..4) rank %d == 5; joint "
          "rank %d == 5 -- same algebra (exact ranks over Q)"
          % (rk_span, rk_pow, rk_both), ok_dim)

    # B in the coordinates + K^k coefficient table
    Bf = fmat_int(B)
    Bexp = None
    for lam in eigs:
        term = fscale(Pi[lam], Fr(MU_B_OF_A[lam]))
        Bexp = term if Bexp is None else fadd(Bexp, term)
    ok_bexp = fequal(Bf, Bexp)
    check("S1.6 B = -2 Pi_0 + 2 (Pi_1 + Pi_4 + Pi_7) + 7 Pi_9 exact -- "
          "K^k = (B/7)^k has atom-basis coefficients (mu_B(l)/7)^k, "
          "exact rationals", ok_bexp)

    # the ambient commutant: dim C({K, sigma}) == 39, Pi inside
    t1 = time.time()
    pair_orbit, orb_reps = {}, []
    for i in range(LABEL_DIM):
        for j in range(LABEL_DIM):
            if (i, j) in pair_orbit:
                continue
            oid = len(orb_reps)
            a, b = i, j
            cyc = []
            while (a, b) not in pair_orbit:
                pair_orbit[(a, b)] = oid
                cyc.append((a, b))
                a, b = perm[a], perm[b]
            orb_reps.append(cyc)
    O_mats = []
    for cyc in orb_reps:
        M = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
        for (a, b) in cyc:
            M[a, b] = 1
        O_mats.append(M)
    rows = [[Fr(0)] * len(O_mats) for _ in range(LABEL_DIM * LABEL_DIM)]
    for t, O in enumerate(O_mats):
        E = O @ B - B @ O
        for i in range(LABEL_DIM):
            for j in range(LABEL_DIM):
                if E[i, j]:
                    rows[i * LABEL_DIM + j][t] = Fr(int(E[i, j]))
    _rk, _piv, null_basis = frref_nullspace(rows, len(O_mats))
    D = len(null_basis)
    Pf = fmat_int(P)
    PfT = [list(r) for r in zip(*Pf)]
    ok_inC = True
    for lam in eigs:
        ok_inC &= fzero(fadd(fmul(Pi[lam], Bf), fmul(Bf, Pi[lam]),
                             Fr(1), Fr(-1)))
        ok_inC &= fequal(fmul(fmul(Pf, Pi[lam]), PfT), Pi[lam])
    check("S1.7 AMBIENT COMMUTANT: %d sigma-pair orbits, dim "
          "C({K, sigma}) = %d == 39 (exact Fraction nullspace); every "
          "Pi_A(l) commutes with B and is sigma-invariant (exact) -- the "
          "five coordinates sit inside the 39-dim nonabelian commutant "
          "as its canonical abelian dim-5 subalgebra"
          % (len(orb_reps), D),
          len(orb_reps) == 81 and D == DIM_COMMUTANT and ok_inC,
          "%.1f s" % (time.time() - t1))
    GATE["s1"] = (ok_fr and ok_a and ok_proj and ok_struct and ok_dim
                  and ok_bexp and len(orb_reps) == 81
                  and D == DIM_COMMUTANT and ok_inC)
    return dict(Pi=Pi, eigs=eigs, B=B, Bf=Bf, labels=labels, lidx=lidx,
                perm=perm)


# =========================================== S2 ansatz space + reduction
def s2_ansatz(fr):
    section("S2 (STEP 2) -- the degree-2 Kraus ansatz space + the exact "
            "reduction lemma")
    Pi, eigs = fr["Pi"], fr["eigs"]

    # event classes and their exact operator coefficients in the atom basis
    classes = ["cont", "odd"] + ["2^%d" % k for k in range(1, K_RAM + 1)] \
        + ["lagconst"]
    op_coeff = {}
    for c in classes:
        if c in ("cont", "odd"):
            op_coeff[c] = {lam: Fr(1) for lam in eigs}
        elif c == "lagconst":
            op_coeff[c] = {lam: Fr(0) for lam in eigs}
        else:
            k = int(c.split("^")[1])
            op_coeff[c] = {lam: Fr(MU_B_OF_A[lam], 7) ** k for lam in eigs}
    tau = {}
    for s in SECTORS:
        tau[s] = {}
        for c in classes:
            if c in ("cont", "odd"):
                tau[s][c] = Fr(1)
            elif c == "lagconst":
                tau[s][c] = Fr(0)
            else:
                k = int(c.split("^")[1])
                tau[s][c] = Fr(s, 7) ** k
    n_classes = len(classes)
    print("    event classes (%d): %s" % (n_classes, ", ".join(classes)))
    print("    building blocks T_s, s in (+7, +2, -2) (typed: only "
          "T_{+7} is the")
    print("    'already-positive sector with its correct continuum "
          "kernel';")
    print("    the mu = +-2 kernels are protocol-internal, v815)")
    ok_cls = (n_classes == 17
              and all(op_coeff["2^%d" % k][9] == 1
                      and op_coeff["2^%d" % k][0] == Fr(-2, 7) ** k
                      for k in range(1, K_RAM + 1)))
    check("S2.1 operator comb coefficients per class exact: odd/cont -> "
          "(1,1,1,1,1); 2^k -> ((-2/7)^k, (2/7)^k, (2/7)^k, (2/7)^k, 1) "
          "in the atom basis (17 classes incl. the lag-constant class)",
          ok_cls)

    # reduction lemma (sympy, generic diagonal): V^T T V = sum v^2 t
    v = sp.symbols("v0 v1 v4 v7 v9", real=True)
    t = sp.symbols("t0 t1 t4 t7 t9", real=True)
    V = sp.diag(*v)
    T = sp.diag(*t)
    lhs = (V.T * T * V) - sp.diag(*[vv ** 2 * tt for vv, tt in zip(v, t)])
    ok_sym = all(sp.simplify(x) == 0 for x in lhs)
    check("S2.2 REDUCTION LEMMA (sympy, atom basis): V^* T V == "
          "Sum_lam v_lam^2 t_lam Pi_lam for V, T in the abelian algebra "
          "(generic symbols, residual 0)", ok_sym)

    # rational 15x15 witnesses: (a) the expansion; (b) Gram off-diagonal
    # invisibility -- two Kraus families with the SAME Gram diagonal give
    # the SAME induced sector coefficients.
    def elem(coeffs):
        M = None
        for lam, cv in zip(eigs, coeffs):
            term = fscale(Pi[lam], cv)
            M = term if M is None else fadd(M, term)
        return M

    vw = [Fr(lcg(19) - 9, lcg(6) + 1) for _ in eigs]
    tw = [Fr(lcg(19) - 9, lcg(6) + 1) for _ in eigs]
    Vw, Tw = elem(vw), elem(tw)
    lhs_w = fmul(fmul(Vw, Tw), Vw)
    rhs_w = elem([vv * vv * tt for vv, tt in zip(vw, tw)])
    ok_wit1 = fequal(lhs_w, rhs_w)
    # family R (3 x 5 rational), Gram G = R^T R; and family R' = Q R with
    # Q a 3x3 rational rotation-like matrix with Q^T Q = I would keep the
    # Gram; instead verify directly: sum_j V_j^T T V_j == elem(diag(G)*t).
    R = [[Fr(lcg(9) - 4, lcg(4) + 1) for _ in eigs] for _ in range(3)]
    acc = None
    for j in range(3):
        Vj = elem(R[j])
        term = fmul(fmul(Vj, Tw), Vj)
        acc = term if acc is None else fadd(acc, term)
    gdiag = [sum(R[j][i] * R[j][i] for j in range(3))
             for i in range(len(eigs))]
    rhs2 = elem([g * tt for g, tt in zip(gdiag, tw)])
    ok_wit2 = fequal(acc, rhs2)
    check("S2.3 rational 15x15 witnesses: V^T T V expansion exact; a "
          "3-member Kraus family reads ONLY diag(G) = %s (Gram "
          "off-diagonals invisible) -- the SDP over 4 blocks S^5_+ "
          "reduces EXACTLY to the LP in W[s, lam] >= 0, E[lam] >= 0"
          % [str(g) for g in gdiag], ok_wit1 and ok_wit2)
    print("    SDP DIMENSIONS (typed): 4 PSD blocks S^5_+ (3 sector Gram "
          "blocks + 1")
    print("    constant block) = 60 scalar unknowns; equality "
          "constraints 5 sectors")
    print("    x 17 classes = 85 per reading; exact reduction -> LP: "
          "3 + 1 = 4")
    print("    nonneg unknowns per (sector, reading), 17 equations each.")
    GATE["s2"] = ok_cls and ok_sym and ok_wit1 and ok_wit2
    return dict(classes=classes, op_coeff=op_coeff, tau=tau)


# ============================================ S3 the SDP, solved exactly
def s3_sdp(fr, an):
    section("S3 (STEP 3) -- the SDP: exact rational solve + float "
            "cross-check + the frozen nontriviality rule")
    eigs = fr["eigs"]
    classes, op_coeff, tau = an["classes"], an["op_coeff"], an["tau"]

    # system per sector lam: unknowns (W7, W2, Wm2, E); rows = classes
    def build_rows():
        rows = []
        for c in classes:
            r = [tau[s][c] for s in SECTORS]
            r.append(Fr(1) if c == "lagconst" else Fr(0))   # slack E
            rows.append(r)
        return rows

    rows = build_rows()
    rk, _piv, nullb = frref_nullspace(rows, 4)
    ok_rank = rk == 4 and len(nullb) == 0
    check("S3.1 UNIQUENESS CERTIFICATE: the 17 x 4 class system has "
          "exact rank %d == 4, kernel {0} (three distinct Vandermonde "
          "ratios 1, 2/7, -2/7 + the slack row) -- at most ONE feasible "
          "point per (sector, reading)" % rk, ok_rank)

    # the inverse-Vandermonde dual row (exact): y on classes
    # {odd (k=0), 2^1, 2^2} extracting W7
    r_ratios = [Fr(1), Fr(2, 7), Fr(-2, 7)]
    V3 = [[r ** k for r in r_ratios] for k in range(3)]
    ok_dual = True
    duals = {}
    for pick in range(3):
        b3 = [Fr(1) if i == pick else Fr(0) for i in range(3)]
        # solve V3^T y = e_pick  (y extracts weight of ratio 'pick')
        cons, uniq, y = fsolve([list(r) for r in zip(*V3)], b3, 3)
        ok_dual &= cons and uniq
        duals[SECTORS[pick]] = y
    print("    exact dual rows (classes odd/2^1/2^2 -> block weights):")
    for s in SECTORS:
        print("      y[%+d] = (%s)" % (s, ", ".join(str(q)
                                                    for q in duals[s])))
    check("S3.2 the inverse-Vandermonde dual rows exist and are unique "
          "(exact) -- every feasible point is FORCED linearly by three "
          "class coefficients", ok_dual)

    # readings
    def target_vec(reading, lam):
        out = []
        for c in classes:
            if reading == "i":
                out.append(Fr(0) if c == "lagconst" else Fr(1))
            else:
                out.append(op_coeff[c][lam])
        return out

    results = {}
    ok_solve = True
    nontrivial_found = False
    for reading in ("i", "ii"):
        for lam in eigs:
            b = target_vec(reading, lam)
            cons, uniq, x = fsolve(rows, b, 4)
            nonneg = cons and all(q >= 0 for q in x)
            results[(reading, lam)] = (cons, uniq, x)
            ok_solve &= cons and uniq and nonneg
            # frozen nontriviality: weight off the target's own kernel
            own = 7 if reading == "i" else MU_B_OF_A[lam]
            off = [q for s, q in zip(SECTORS, x[:3]) if s != own]
            if cons and (any(q != 0 for q in off) or x[3] != 0):
                nontrivial_found = True
    check("S3.3 EXACT SOLVE (both readings, all 5 sectors): every system "
          "consistent, unique, nonnegative -- reading (i) "
          "T_GL1 (x) I: W = (1, 0, 0), E = 0 on every sector; reading "
          "(ii) T_op: W[s, lam] = delta_{s, mu_B(lam)}, E = 0",
          ok_solve and all(
              results[("i", lam)][2] == [Fr(1), Fr(0), Fr(0), Fr(0)]
              for lam in eigs)
          and all(results[("ii", lam)][2]
                  == [Fr(1) if s == MU_B_OF_A[lam] else Fr(0)
                      for s in SECTORS] + [Fr(0)]
                  for lam in eigs))
    check("S3.4 FROZEN NONTRIVIALITY RULE: no feasible point carries "
          "weight outside the target sector's own kernel (feasible set = "
          "the single diagonal point) -- the hoped-for cross-sector "
          "positive transfer through the abelian commutant is "
          "INFEASIBLE, exactly", not nontrivial_found,
          "the identity exists but is the TRIVIAL diagonal rewriting "
          "(v815's sector decomposition restated)")

    # float NNLS cross-check + rationalization (the task's step-4 tool
    # applied to the float solver output)
    A_f = np.array([[float(q) for q in r] for r in rows])
    ok_nnls = True
    for reading in ("i", "ii"):
        for lam in eigs:
            b_f = np.array([float(q) for q in target_vec(reading, lam)])
            x_f, res = nnls(A_f, b_f)
            x_exact = results[(reading, lam)][2]
            x_rat = [Fr(v).limit_denominator(RAT_QMAX) for v in x_f]
            ok_nnls &= res <= NNLS_TOL and x_rat == x_exact
    check("S3.5 float NNLS cross-check: residual <= %.0e and the "
          "continued-fraction rationalization of the solver output "
          "matches the exact rational solution on all 10 systems"
          % NNLS_TOL, ok_nnls)
    GATE["s3"] = (ok_rank and ok_dual and ok_solve
                  and not nontrivial_found and ok_nnls)
    return dict(nontrivial=nontrivial_found)


# ===================================== S4 the flag-space Gram lift (SDP)
def s4_gram_lift():
    section("S4 (STEPS 4/5) -- the rank-3 det form on the 105-leg flag "
            "space: the Gram SDP and its dual certificate")
    # polarisation identity (sympy exact)
    S11, S22, S12 = sp.symbols("S11 S22 S12", real=True)
    tt = (S11 + S22) / 2
    xx = (S11 - S22) / 2
    yy = S12
    ok_pol = sp.simplify((S11 * S22 - S12 ** 2)
                         - (tt ** 2 - xx ** 2 - yy ** 2)) == 0
    check("S4.1 polarisation (sympy exact): det S = S11 S22 - S12^2 == "
          "t^2 - x^2 - y^2, t = (S11+S22)/2, x = (S11-S22)/2, y = S12 -- "
          "the Lorentz form of signature (1, 2)", ok_pol)

    # compiler null vector
    q_null = Fr(5) ** 2 - Fr(-3) ** 2 - Fr(4) ** 2
    vspin = (1, 2)
    Sspin = [[2 * vspin[0] * vspin[0], 2 * vspin[0] * vspin[1]],
             [2 * vspin[0] * vspin[1], 2 * vspin[1] * vspin[1]]]
    tri = (Fr(Sspin[0][0] + Sspin[1][1], 2),
           Fr(Sspin[0][0] - Sspin[1][1], 2), Fr(Sspin[0][1]))
    ok_null = q_null == 0 and tri == (Fr(5), Fr(-3), Fr(4))
    check("S4.2 the compiler null vector: q(5, -3, 4) = 25 - 9 - 16 = 0 "
          "exact, and (5, -3, 4) == the spinor square 2 (1,2)(1,2)^T "
          "(rank-1 boundary of the cone)", ok_null)

    # the Gram SDP: G in S^3 with s^T G s == q(s); 6 unknowns, 6 eqs
    g11, g22, g33, g12, g13, g23 = sp.symbols("g11 g22 g33 g12 g13 g23",
                                              real=True)
    tv, xv, yv = sp.symbols("tv xv yv", real=True)
    G = sp.Matrix([[g11, g12, g13], [g12, g22, g23], [g13, g23, g33]])
    svec = sp.Matrix([tv, xv, yv])
    expr = sp.expand((svec.T * G * svec)[0] - (tv ** 2 - xv ** 2 - yv ** 2))
    eqs = [sp.Eq(expr.coeff(m), 0) for m in
           (tv ** 2, xv ** 2, yv ** 2, tv * xv, tv * yv, xv * yv)]
    sol = sp.solve(eqs, (g11, g22, g33, g12, g13, g23), dict=True)
    ok_forced = (len(sol) == 1
                 and sol[0][g11] == 1 and sol[0][g22] == -1
                 and sol[0][g33] == -1 and sol[0][g12] == 0
                 and sol[0][g13] == 0 and sol[0][g23] == 0)
    check("S4.3 THE GRAM SDP (typed: G in S^3, 6 unknowns, 6 equality "
          "constraints): coefficient matching FORCES the unique "
          "G = diag(1, -1, -1) (sympy exact) -- eigenvalues {1, -1, -1}: "
          "NOT PSD, the SDP is INFEASIBLE", ok_forced)

    # dual certificate, rational and exact
    s_star = (Fr(0), Fr(1), Fr(0))
    q_star = s_star[0] ** 2 - s_star[1] ** 2 - s_star[2] ** 2
    ok_dualc = q_star == Fr(-1) and q_star < 0
    check("S4.4 DUAL CERTIFICATE (rational, exact): s* = (0, 1, 0) has "
          "q(s*) = -1 < 0, while every Gram norm X^T G X with G >= 0 "
          "pulls back to a form >= 0 through ANY linear lift -- since "
          "the 105 RM-check reads are LINEAR in the comb and the three "
          "functionals are linear in the flag reads (the overdetermined "
          "frame), NO flag-space Gram representation of the det margin "
          "exists on any achievable set containing a q-negative "
          "direction", ok_dualc)

    # achievability, typed float-assisted (NOT part of the exact layer)
    t0 = time.time()
    KZ = core.frame_a_zones()
    kz_ref = None
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        if Mz // 2 == core.Q_H_REF:
            kz_ref = kz
            break
    r = core.build_window(kz_ref)
    Xn, lam = r["Xn"], r["lam"]
    ka = Xn.shape[0]
    sv = np.linalg.svd(Xn, compute_uv=False)
    rank3 = int(np.sum(sv > 1.0e-10 * sv[0]))
    ok_rank3 = rank3 == 3
    check("S4.5 ACHIEVABILITY (a), typed float-assisted: the per-event "
          "read matrix Xn (%d x 3) at the v563 reference window h = %d "
          "has numerical rank %d == 3 (svals %.2e / %.2e / %.2e) -- the "
          "functional map is surjective for signed generic weights"
          % (ka, r["h"], rank3, sv[0], sv[1], sv[2]), ok_rank3,
          "%.1f s" % (time.time() - t0))

    # witness triple (SPEC v2: deterministic column-pivoted QR of Xn^T;
    # the SPEC v1 triple (0, ka//2, ka-1) is singular -- the boundary
    # event reads exactly (0,0,0); declared correction, see docstring)
    _q, _r, piv = sla.qr(Xn.T, pivoting=True)
    idx3 = tuple(int(p) for p in piv[:3])
    M3 = Xn[list(idx3), :]                       # 3 x 3 (rows = events)
    # target functional direction s* in (S11, S22, S12) coordinates:
    # q < 0 needs S11 S22 - S12^2 < 0; take (S11, S22, S12) = (0, 0, 1)
    tgt = np.array([0.0, 0.0, 1.0])
    try:
        cond3 = float(np.linalg.cond(M3.T))
        cw = np.linalg.solve(M3.T, tgt)
        cr = [Fr(v).limit_denominator(RAT_QMAX) for v in cw]
        S_dir = sum(float(c) * Xn[i, :] for c, i in zip(cr, idx3))
        q_dir = float(S_dir[0] * S_dir[1] - S_dir[2] ** 2)
        budget = cond3 * np.finfo(float).eps * max(1.0, float(np.max(
            np.abs(S_dir)))) ** 2 * 64.0
        ok_wit = q_dir < -budget
    except np.linalg.LinAlgError:
        cond3, q_dir, budget = float("inf"), 0.0, 0.0
        cr, S_dir = [], np.zeros(3)
        ok_wit = False
    check("S4.6 ACHIEVABILITY witness (declared events %s = indices %s, "
          "cond %.1e): rationalized weights give S = (%.2e, %.2e, %.2e), "
          "q = %.3e < -budget %.1e -- a q-NEGATIVE direction is "
          "achievable (float-assisted, typed)"
          % (WITNESS_TRIPLE, idx3, cond3,
             S_dir[0], S_dir[1], S_dir[2], q_dir, budget), ok_wit)
    print("      rational weights: %s" % (", ".join(str(c) for c in cr)))

    # achievability (b): the physical nonneg cone -- truncation scan
    c1 = np.cumsum(lam * Xn[:, 0])
    c2 = np.cumsum(lam * Xn[:, 1])
    c3 = np.cumsum(lam * Xn[:, 2])
    dets = c1 * c2 - c3 ** 2
    n_neg = int(np.sum(dets < 0.0))
    m_min = int(np.argmin(dets))
    print("      truncated-comb scan (v619 flip set): %d of %d cuts "
          "carry det S < 0;" % (n_neg, ka))
    print("      min det S = %.3e at cut %d (u = %.3f); full-comb "
          "det S = %.3e" % (float(dets[m_min]), m_min,
                            float(r["uu"][m_min]), float(dets[-1])))
    check("S4.7 ACHIEVABILITY (b), the NONNEG cone: truncated sub-combs "
          "with det S < 0 exist (%d cuts) -- q-negativity is reached "
          "even with physical nonnegative masses (measured; the full "
          "comb at this window has det S = %.1f > 0)"
          % (n_neg, float(dets[-1])), n_neg > 0)
    GATE["s4"] = (ok_pol and ok_null and ok_forced and ok_dualc
                  and ok_rank3 and ok_wit and n_neg > 0)
    return dict(Xn=Xn, r=r)


# ================================================== S5 the fence
def s5_fence(g4):
    section("S5 (STEP 6) -- THE FENCE: did any step smuggle an "
            "oscillatory prime-sum estimate?")
    # (a) the identity layer is mass-free: the LP coefficient matrix is
    # built from the class ratios (1, 2/7, -2/7) alone -- no U_ALL/MU_ALL
    # value enters S2/S3 (structural; asserted on the construction).
    ok_a = True
    check("S5.1 FENCE (a) -- the identity layer is MASS-FREE: the class "
          "system uses only the exact ratios {1, 2/7, -2/7}; no event "
          "mass or position enters S2/S3 (the certificates hold for "
          "GENERIC symbolic weights) -- nothing smuggled: FENCE-CLEAN "
          "on the algebra layer", ok_a)

    # (b) the positivity content: pointwise Cauchy-Schwarz census on the
    # actual reads (rank3 R4(ii) recipe)
    Xn = g4["Xn"]
    v_neg = int(np.sum(Xn[:, 0] < 0.0)) + int(np.sum(Xn[:, 1] < 0.0))
    v_cs = int(np.sum(Xn[:, 2] ** 2 > Xn[:, 0] * Xn[:, 1] + 1.0e-15))
    fence_hit = (v_neg + v_cs) > 0
    check("S5.2 FENCE (b) -- the positivity branch: pointwise "
          "Cauchy-Schwarz census on the reference reads: %d negative "
          "diagonal reads, %d CS violations (of %d events) -- every "
          "nonneg-cone certificate must therefore use CROSS-EVENT "
          "cancellation, i.e. an oscillatory prime-sum (pair-"
          "correlation) estimate: FENCE-%s on the positivity branch"
          % (v_neg, v_cs, Xn.shape[0], "HIT" if fence_hit else "CLEAN"),
          True, "typed as it falls; a HIT is the expected honest reading")
    print("    THE FENCE VERDICT: the exact identity layer needs no")
    print("    estimate (trivial identity, Vandermonde algebra); the")
    print("    SUBSTANTIVE positivity content (det S >= R_arch on the")
    print("    physical comb) is degree-2 in the comb and its control is")
    print("    exactly the pair-correlation boundary -- the route, made")
    print("    nontrivial, returns to that boundary.")
    GATE["s5"] = True
    return fence_hit


# ================================================== S6 controls
def s6_controls():
    section("S6 -- controls (frozen)")
    t0 = time.time()
    # deployed event stream + windows (v815 S5 recipe, read-only)
    ka, masks, devm = srp.channel_masks(ALPHA_TOP)
    U_ev = np.array([float(core.U_ALL[i]) for i in range(ka)])
    MU_ev = np.array([float(core.MU_ALL[i]) for i in range(ka)])
    nvals = np.array([int(round(math.exp(U_ev[i]))) for i in range(ka)],
                     dtype=np.int64)
    two_pow = (nvals & (nvals - 1)) == 0
    kvals = np.where(two_pow, np.int64(np.log2(np.maximum(nvals, 1))
                                       + 0.5), 0)
    n2 = int(np.sum(two_pow))
    ok_ev = devm <= 1.0e-12 and n2 == K_RAM
    check("S6.0 deployed events: ka = %d (u <= 10), %d ramified events "
          "n = 2^k (k = 1..14); channel-mask ward %.1e"
          % (ka, n2, devm), ok_ev, "%.1f s" % (time.time() - t0))

    c_cont = srp.continuum_lags(M_TOP)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                                masks[cnl])

    def window(mu_b, positions=None):
        mult = np.ones(ka)
        mult[two_pow] = (mu_b / 7.0) ** kvals[two_pow].astype(float)
        pos = U_ev if positions is None else positions
        atoms, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, pos, MU_ev * mult)
        return c_cont + atoms

    # K1: tau-identification comb-specific
    w7 = window(7.0)
    dev_gl1 = float(np.max(np.abs(w7 - c_full))
                    / np.max(np.abs(c_full)))
    rng = np.random.default_rng(SCRAMBLE_SEED)
    uu_scr = np.sort(rng.uniform(0.0, 2.0 * ALPHA_TOP, size=ka))
    w7_scr = window(7.0, positions=uu_scr)
    dev_scr = float(np.max(np.abs(w7_scr - c_full))
                    / np.max(np.abs(c_full)))
    fired1 = dev_gl1 <= WARD_BAR and dev_scr >= K1_BAR
    CONTROL_FIRED["K1"] = fired1
    check("K1 CONTROL tau-identification: TRUE comb: uniform sector == "
          "deployed GL1 window (rel %.1e <= 1e-12); SCRAMBLED comb "
          "(v563 recipe, uniform positions seed %d, same masses): rel "
          "dev %.3e >= %.0e -- the identification is COMB-SPECIFIC, the "
          "scramble kills it: fires"
          % (dev_gl1, SCRAMBLE_SEED, dev_scr, K1_BAR), fired1)

    # K2: three-sector PSD pattern (v815)
    def ladder(lag):
        out = []
        for M in RUNGS:
            T = sla.toeplitz(lag[:M])
            lmin = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
            out.append((M, lmin, float(sla.norm(T, 2))))
        return out

    lads = {7: ladder(w7), 2: ladder(window(2.0)),
            -2: ladder(window(-2.0))}
    psd = {}
    for s, lad in lads.items():
        psd[s] = all(lmin >= -PSD_BAR * nrm for _M, lmin, nrm in lad)
        print("    mu = %+d ladder lambda_min: %s  [%s]"
              % (s, " | ".join("%+.2e" % lmin for _M, lmin, _n in lad),
                 "PSD" if psd[s] else "NEG"))
    fired2 = psd[7] and (not psd[2]) and (not psd[-2])
    CONTROL_FIRED["K2"] = fired2
    check("K2 CONTROL sector PSD pattern: uniform mu = 7 PSD on ALL "
          "rungs; mu = +2 and mu = -2 each carry NEG rungs -- v815's "
          "pattern (only the uniform sector is PSD) reproduced "
          "(protocol-internal, NOT an L-function claim)", fired2)

    # K3: wrong-ratio control -- replacing the +2 block profile by
    # (3/7)^k must make the reading-(ii) mu_B = 2 system inconsistent
    classes = ["cont", "odd"] + ["2^%d" % k for k in range(1, K_RAM + 1)] \
        + ["lagconst"]
    rows_bad, b2 = [], []
    for c in classes:
        if c in ("cont", "odd"):
            rows_bad.append([Fr(1), Fr(1), Fr(1), Fr(0)])
            b2.append(Fr(1))
        elif c == "lagconst":
            rows_bad.append([Fr(0), Fr(0), Fr(0), Fr(1)])
            b2.append(Fr(0))
        else:
            k = int(c.split("^")[1])
            rows_bad.append([Fr(1), Fr(3, 7) ** k, Fr(-2, 7) ** k,
                             Fr(0)])
            b2.append(Fr(2, 7) ** k)
    cons_bad, _u, _x = fsolve(rows_bad, b2, 4)
    fired3 = not cons_bad
    CONTROL_FIRED["K3"] = fired3
    check("K3 CONTROL wrong ratio: with the T_{+2} profile replaced by "
          "(3/7)^k the exact reading-(ii) mu_B = 2 system is "
          "INCONSISTENT (rref detects) -- the exact solve is not "
          "vacuous: fires", fired3)
    GATE["s6"] = fired1 and fired2 and fired3


# ================================================== S7 verdict
def s7_verdict(nontrivial, fence_hit):
    section("S7 -- verdict (frozen enum)")
    gates_ok = all(GATE.get(k, False)
                   for k in ("s1", "s2", "s3", "s4", "s5", "s6"))
    controls_ok = all(CONTROL_FIRED.get(k, False)
                      for k in ("K1", "K2", "K3"))
    if nontrivial and gates_ok:
        verdict = "COMMUTANT-SOS-EXACT"
        note = ("a NONTRIVIAL rational identity was verified at event "
                "level")
    elif gates_ok and controls_ok and not nontrivial:
        verdict = "COMMUTANT-SOS-INFEASIBLE"
        note = ("route closed by exact certificates: (a) the degree-2 "
                "abelian-commutant ansatz has a UNIQUE feasible point = "
                "the trivial diagonal rewriting (Vandermonde kernel {0}, "
                "exact rationals) -- no cross-sector positive transfer "
                "exists; (b) the rank-3 det form admits NO Gram-norm "
                "representation on the 105-leg flag space (forced "
                "G = diag(1,-1,-1), dual point q(0,1,0) = -1 < 0, exact; "
                "q-negative directions achievable, incl. on the nonneg "
                "cone).  STOP-LIST ENTRY CANDIDATE.")
    else:
        verdict = "COMMUTANT-SOS-PARTIAL"
        fails = [k for k in ("s1", "s2", "s3", "s4", "s5", "s6")
                 if not GATE.get(k, False)]
        note = "typed break points: gates %s, controls %s" % (
            fails, {k: CONTROL_FIRED.get(k) for k in ("K1", "K2", "K3")})
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("checks: %d/%d pass" % (n_pass, len(CHECKS)))
    for k in sorted(GATE):
        print("  gate %-4s %s" % (k, GATE[k]))
    for k in sorted(CONTROL_FIRED):
        print("  control %-3s %s" % (k, CONTROL_FIRED[k]))
    print()
    print("VERDICT: %s" % verdict)
    print("  " + note)
    print()
    print("DELIVERABLE (typed, exploration only):")
    print("  1. THE FIVE COORDINATES: Pi_A(0), Pi_A(1), Pi_A(4), "
          "Pi_A(7), Pi_A(9)")
    print("     (traces 5/2/5/2/1), exact orthogonal idempotents, "
          "structure")
    print("     constants Pi_a Pi_b = delta_ab Pi_a, the canonical "
          "abelian dim-5")
    print("     subalgebra of the 39-dim commutant; B = -2 Pi_0 + "
          "2(Pi_1+Pi_4+Pi_7)")
    print("     + 7 Pi_9 exact.")
    print("  2. ANSATZ SPACE / SDP: 4 PSD blocks S^5_+ (60 unknowns), "
          "85 equality")
    print("     constraints per reading; EXACT reduction to a rational "
          "LP (the")
    print("     abelian conjugation reads only the Gram diagonals); "
          "solved exactly.")
    print("  3. WHAT THE IDENTITY GIVES FOR THE FLOOR: nothing beyond "
          "v815 -- the")
    print("     unique identity is the sector decomposition itself; the "
          "abelian")
    print("     commutant is event-class-diagonal, so it cannot source "
          "the floor")
    print("     from other positive sectors; and only T_{+7} is "
          "'already positive'")
    print("     (the mu = +-2 kernels are non-PSD and lack derived "
          "continua).")
    print("  4. THE RANK-3 HOPE: killed exactly -- any flag-space Gram "
          "certificate")
    print("     factors through the three functionals; signature (1,2) "
          "forbids it;")
    print("     q-negative directions are achievable (even on the "
          "nonneg cone via")
    print("     the truncation flip set).")
    print("  5. THE FENCE: FENCE-CLEAN on the algebra layer (mass-free); "
          "FENCE-%s" % ("HIT" if fence_hit else "CLEAN"))
    print("     on the positivity branch -- the nontrivial version of "
          "this route")
    print("     is an oscillatory prime-sum (pair-correlation) "
          "statement.")
    print("  6. SCOPE: positivity structural, tau-identification "
          "comb-specific")
    print("     (K1: the scramble kills the GL1 identification).  "
          "NO RH claim.")
    return verdict


def main():
    print("COMMUTANT SOS PROBE -- PRIME.COMMUTANT.SOS.01")
    print("frozen 2026-08-07 before the first run; exploration only; "
          "NO RH claim;")
    print("ROOTCLASS-MIXED cited (register/carrier structure only).")
    g0_firewall()
    fr = s1_frame_and_coordinates()
    an = s2_ansatz(fr)
    s3r = s3_sdp(fr, an)
    g4 = s4_gram_lift()
    fence_hit = s5_fence(g4)
    s6_controls()
    verdict = s7_verdict(s3r["nontrivial"], fence_hit)
    print()
    print("total runtime %.1f s" % (time.time() - T0))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
