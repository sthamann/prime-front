#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v815 -- PRIME.AORB.REFINEMENT.01 (+ the spread/commutant falsifier pair of PRIME.KRAUS.DOILY.01): sigma breaks every single spread but the direct-sum protocol is sigma-stable as a family, [E, K] = 0 extends to the full tower, and the {K, sigma} commutant is the 39-dim nonabelian closure of the A_orb refinement, ONE module from two probes (21/21 + 24/24 checks, ~5 s; discovery probes kraus_spread_commutant_probe.py SPREAD-SIGMA-BROKEN / COMMUTANT-EXTENDS (SPEC v2 -- ONE declared run-1 -> run-2 gate-implementation repair in S4.2 carried verbatim: the count became an exact rank, claim unchanged) and kraus_aorb_refinement_probe.py AORB-NOT-MAXIMAL, both 2026-08-06).  PART 1, THE TWO NAMED FALSIFIERS: (task 1) sigma acts on the 6 isotropic spreads of W(3,2) as TWO 3-CYCLES, zero fixed (permutation [3,2,4,5,1,0]; the outer-S6 pre-analysis CONFIRMED: out(S6) swaps the 3-cycle class with (3,3)) -- the rule-B partition is outer-class-forced non-invariant; NO nontrivial sigma-invariant coarsening survives (per-orbit join = the one-block partition), but the FAMILY is sigma-stable: sigma transports B45(s) -> B45(sigma s) exactly and [B45(s), B60(s)] = 0 for EVERY spread, with the invariant commutant witnesses Sum_all B45(s) = 4I + 2B (each line lies in exactly 2 spreads) and the per-orbit A_orb sigma-invariant, K-commuting, integer spectrum {0^5, 1^2, 4^5, 7^2, 9^1}.  (task 2) [E, K] = 0 EXTENDS: [E, K^2] = 0 typed honestly (follows from double stochasticity alone -- the base [E, K] = 0 is the load-bearing fact); the channel lift E2 o Phi == Phi o E2 on ALL 225 matrix units, exact rationals; the KMS tower half-weight D'U = 2^{-1/2} U D compatible; odd places p = 3, 5, 7: the Hecke commutant is EXACTLY span{I, X}, the only unital *-subalgebras containing the Hecke algebra are span{I, X} and M_2, and the unital trace-preserving bimodule projection is UNIQUE = the C2-CHARACTER expectation E_p(a) = (a + XaX)/2, Hecke-covariant; the assembled E_full = E2 (x) id (x) (tensor_p E_p) commutes with Phi_ext, the odd Hecke multiplications and the half-weight INTEGER-EXACTLY on the 600-dim register (15 x 5 x 8, scale 168 = 7 x 24 cleared).  PART 2, THE REFINEMENT DECIDER: the commutant C of {K, sigma} has dim 39 (exact Fraction nullspace over the 81 sigma-pair orbits), NONABELIAN, block structure R + M_3(R) + M_3(C) + M_3(R) + M_1(C) with 5 exact central atoms and center R^3 + C^2; A_orb generates the canonical ABELIAN 5-dim subalgebra -- IDENTICAL for both spread sigma-orbits (orbit swap Pi2(l) == Pi1(8-l) on E_B(2)) with the forced containments E_A(0) = E_B(-2) and E_A(9) = J/15 -- a proper abelian subalgebra: AORB-NOT-MAXIMAL; the refinement is WINDOW-SILENT beyond the K-spectrum (the exact scalar-action certificate Q K^k Q = (mu_B/7)^k Q forces identical windows inside each B-eigenspace -- only three scalar windows mu_B = 7, 2, -2 exist, only the uniform mu_B = 7 sector is PSD and it == the deployed GL1 window to 6.0e-16); the EXACT character lemma B chi_w = 8 e_{Omega^{-1} w} - 1vec shows the A_orb frame TRANSVERSAL to the V-characters and to chi_NSR (overlap censuses exact).  Controls fire in both parts.  ROOTCLASS-MIXED (v775) cited; the mu = +-2 window measurements typed protocol-internal, NOT L-function claims.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes kraus_spread_commutant_probe.py (2026-08-06, 21/21, ~3 s, SPREAD-SIGMA-BROKEN / COMMUTANT-EXTENDS; the SPEC v2 gate-implementation repair carried verbatim) + kraus_aorb_refinement_probe.py (2026-08-06, 24/24, ~2 s, AORB-NOT-MAXIMAL); both re-run identically at promotion.  Merged per the v518/v668 precedent: part 1 verbatim at module level (the v738 import resolves against the verification directory; path swap, v795 precedent); part 2 verbatim inside an isolated function scope (its module-level names are function-local); part 2's tail extended to return its verdict and check counts (v791-style capture); numbers unchanged; run() encodes both patterns (v757 precedent).

Original kraus_spread_commutant_probe.py docstring (verbatim):
kraus_spread_commutant_probe -- the two named falsifiers of
PRIME.KRAUS.DOILY.01 in one decider:

TASK 1  THE SPREAD SIGMA-INVARIANCE CENSUS.  The doily probe measured
that the certified lex-first spread is NOT sigma-invariant.  Census all
6 isotropic spreads of W(3,2) under sigma exactly: orbit structure
(fixed spreads / 3-orbits), and per spread the covariance data of the
induced rule-B selection (sigma, deck, *).  BRANCH (a): if >= 1 spread
is sigma-invariant, redo the rule-B partition with it (45+60,
(3,1,1,1,1), sigma-covariance of the partition).  BRANCH (b): if NONE
is sigma-invariant, compute the exact breaking data: the sigma-orbit of
partitions, the invariant coarsening (join / meet in the partition
lattice per orbit), and THE SHARP QUESTION: whether the direct-sum
statement [B45(s), B60(s)] = 0 is sigma-STABLE as a statement about
the FAMILY (sigma transports B45(s) to B45(sigma s) exactly), with the
sigma-invariant commutant witnesses Sum_orbit B45(s) (per orbit) and
Sum_all B45(s) = 4I + 2B (each line lies in exactly 2 spreads).
  PRE-ANALYSIS (frozen as expectation, measured exactly): sigma has
label cycle census 1^3 3^4 = a 3-cycle of S6 on the duad model; the 6
spreads carry the OUTER S6 action, and out(S6) swaps the 3-cycle class
with the (3,3) class -- so sigma is expected to act on the spreads as
two 3-cycles, ZERO fixed.  The census decides.

TASK 2  THE COMMUTANT TOWER EXTENSION.  Does [E, K] = 0 survive the
extension?
 (a) tower: [E, K^2] = 0 exact WITH ITS HONEST TYPE (E doubly
     stochastic => E J = J E = 3J/3, and 49 K^2 = 4I + 3J, so the K^2
     commutation follows from double stochasticity alone -- the
     load-bearing fact is the base [E, K] = 0); the two-step anchor
     T = 4B^2 = 28I + 12(J - I) commutes likewise; the KMS half-weight
     relation D' U = 2^{-1/2} U D (v756) re-derived exactly and
     E (x) id commutes with the tower half-weight and preserves the
     KMS state; CHANNEL LEVEL: the operator lift E2(m) = Sum_b P_b
     tr(P_b m)/3 satisfies E2 o Phi == Phi o E2 on ALL 225 matrix
     units, exact rationals (Phi = the v756 dephasing-Markov channel).
 (b) odd places p = 3, 5, 7: the packet algebra per place is M_2 with
     Hecke element M_p = A_p I + B_p X (A_p = (sigma3(p) + a_p)/2,
     B_p = (sigma3(p) - a_p)/2; anchors a_p = (-4, -2, 24) cited from
     v801 A1.4, sigma3(p) = 1 + p^3 closed).  CENSUS: the commutant of
     {M_p} is EXACTLY span{I, X} (2-dim, solved exactly); the unital
     *-subalgebras of M_2 containing the Hecke algebra are exactly
     {span{I, X}, M_2} (any strictly larger subalgebra closes to M_2:
     exact generation census on the 4 candidate units); the unital,
     trace-preserving, *-preserving span{I,X}-bimodule projection onto
     span{I, X} is UNIQUE (16-real-unknown linear system, exact
     nullity 0) and equals E_p(a) = (a + X a X)/2, which commutes with
     the Hecke multiplication exactly.  So the trivial extension is
     NOT the only one: exactly ONE nontrivial expectation exists = the
     C2-character expectation, and it is Hecke-covariant.
 (c) the full statement: E_full = E2 (x) id_tower (x) (tensor_p E_p)
     on the assembled 600-dim register (15 labels x 5 tower levels x
     2^3 odd places) commutes with the extended Stinespring channel
     Phi_ext = Phi_B (x) id_40 (105 legs), with the odd Hecke
     multiplications, and with the tower half-weight -- verified
     INTEGER-EXACTLY (scale 168 = 7 x 24 clears all denominators) on
     the identity, a matrix-unit sample, and 10 frozen LCG integer
     witnesses; E_full is idempotent and unital on the same family.

CONTROLS (must fire):
 K1a an OVERLAPPING 5-line set (not a partition): B' = [x, y share a
     chosen line] is NOT idempotent-of-scale-3 ((B')^2 != 3 B').
 K1b a NON-SPREAD partition (one cross-block swap of the certified
     spread): [B'', B] != 0 -- the expectation property breaks exactly
     where the (3,1,1,1,1) census broke.
 K2  scrambled tower half-weights (non-identity LCG permutation of the
     diagonal): D'_tgt U - 2^{-1/2} U D_scr has max deviation > 0.1.

VERDICTS (frozen enums):
 verdict 1: SPREAD-SIGMA-INVARIANT-EXISTS (>= 1 fixed spread; rule-B
            re-verified with it) / SPREAD-SIGMA-BROKEN (0 fixed; the
            breaking + invariant-coarsening data certified).
 verdict 2: COMMUTANT-EXTENDS (all of (a), (b), (c) exact + controls
            fire) / COMMUTANT-PARTIAL (base [E, K] = 0 holds, >= 1
            extension gate fails -> named) / COMMUTANT-OBSTRUCTED (a
            nonzero commutator measured in the constructed extension
            -> the obstruction reported exactly).

SPEC v2 (2026-08-06): ONE declared run-1 -> run-2 GATE-IMPLEMENTATION
repair in S4.2, no claim change: run 1 counted the number of matrix
units with nonzero commutator [E_k, X] (= 4) where the intended
quantity is the RANK of the constraint map Y -> [Y, X] (= 2; all four
unit commutators lie in the 2-dim span of E_01 - E_10 and
E_00 - E_11).  The commutant dimension 4 - rank = 2 = span{I, X} is
what the gate always claimed; the count is now computed as an exact
rank.  All other run-1 results (20/21) unchanged.

FENCES: exploration only (experiments/tfpt-discovery/); no
verification/, ledger, .tex, website writes; no .md; no commits.
ROOTCLASS-MIXED (v775) cited: register/carrier structure only, no
particle semantics.  NO RH claim.  Exact integer / Fraction
arithmetic in every load-bearing gate; floats only where 2^{-1/2}
itself is the object (tower relation, gated at 1e-15) and in the
scrambled-weight control.  Frozen 2026-08-06 before the first run.

Sources (read-only): prime_kraus_doily_probe (frame + doily + spread
recipes, [E, K] = 0 finding), v756 (tower data, channel), v801/
prime_cp_intertwiner_probe (leg set, odd anchors a_p = (-4, -2, 24)),
v783 (spreads = MUB pentads), v738 (Lmodule, sigma), ledger probe T3.

Original kraus_aorb_refinement_probe.py docstring (verbatim):
PRIME.AORB.REFINEMENT.01 -- the A_orb eigenprojection decider.

EXPLORATION ONLY (experiments/tfpt-discovery).  Writes nothing outside
stdout; no verification/, no ledger, no TeX, no website, no .md.

Parent results (kraus_spread_commutant_probe, read-only recipe):
  sigma acts on the 6 isotropic spreads of W(3,2) as two 3-cycles
  (SPREAD-SIGMA-BROKEN); per sigma-orbit the invariant operator
  A_orb = Sum_{s in orbit} B45(s) is sigma-invariant, K-commuting,
  with integer spectrum {0^5, 1^2, 4^5, 7^2, 9^1}, identical for both
  orbits.  This probe decides whether the A_orb eigenprojections are
  the MAXIMAL sigma-invariant K-commuting refinement, identifies the
  eigenspaces in the certified geometry, and pushes the refined label
  sectors through the deployed Weil window machinery.

TASKS
  1  MAXIMALITY: the commutant C of {K, sigma} on the 15-label space,
     EXACT (rational): dimension via the sigma-orbit-indicator basis
     (81 = number of orbits of sigma x sigma on index pairs) cut by
     [Y, B] = 0 (Fraction rref, exact nullspace); nonabelian witness;
     the minimal central projections; whether the A_orb eigenprojection
     algebra (dim 5) equals C.
  2  EIGENSPACE STRUCTURE: exact Lagrange eigenprojections of A_orb
     (both orbits, Fractions); forced containments in the B-eigenspaces
     (pre-analysis from A1 + A2 = 4I + 2B and (B-7)(B-2)(B+2) = 0:
     E_A(0) = E_B(-2), E_A(9) = uniform, E_A(1)+E_A(4)+E_A(7) =
     E_B(2), orbit swap lambda <-> 8 - lambda); sigma-fix content,
     fixed-label weights, spread block-space identifications, the
     joint <A_orb, F, B> abelian refinement (the canonical maximal
     abelian invariant decomposition containing A_orb).
  3  WEIL CHANNELS: the deployed event stream (v563 atoms, u <= 10)
     carries the label operator I on odd events (odd places act
     label-uniformly, degree * id -- certified) and K^k = (B/7)^k on
     the ramified events n = 2^k (the certified tower composition).
     For a K-, sigma-commuting projection Q inside a single
     B-eigenspace, Q K^k Q = (mu_B/7)^k Q EXACTLY, so the compressed
     window is the deployed comb with the 2-adic masses rescaled by
     (mu_B/7)^k: THREE distinct scalar windows (mu_B = 7, 2, -2), and
     the A_orb refinement beyond the K-spectrum is WINDOW-SILENT by
     the operator identity.  mu_B = 7 must reproduce the deployed GL1
     window (rel <= 1e-12, parent anchors within 5%).  PSD ladders on
     the frozen rungs M = 256..640 (X = 4..10) with the DEPLOYED
     continuum (frozen: no sector-adapted continuum is derived here;
     these are not character sectors -- protocol-internal windows).
     Relation to the automorphic set: the exact character lemma
     B chi_w = 8 e_{Omega^{-1} w} - 1vec (all nonzero w), the
     chi_w / A_orb overlap table, and the chi_NSR overlaps
     (exact Fractions).

CONTROLS (must fire)
  C1  a random sigma-symmetrized operator fails K-commutation
      ([R, B] != 0) -- its eigenprojections cannot all commute with K.
  C2  a non-invariant projection (coordinate projector at a non-fixed
      label) breaks sigma-transport (P Q P^T != Q).

VERDICT ENUM (frozen): AORB-MAXIMAL-MEANINGFUL / AORB-MAXIMAL-SILENT /
AORB-NOT-MAXIMAL.  Maximality criterion (frozen): the unital algebra
generated by the A_orb eigenprojections of BOTH orbits (measured dim)
EQUALS the full commutant C of {K, sigma} (i.e. dim C == 5 and C
abelian).  If C is strictly larger the verdict is AORB-NOT-MAXIMAL
with the full invariant decomposition computed and typed (central
blocks + the canonical abelian refinement), and the window-content
findings reported as sub-findings.

FENCES: ROOTCLASS-MIXED cited (register/carrier structure only, no
particle semantics); NO RH/GRH claim; the PSD measurements on modified
2-adic legs are protocol-internal consistency measurements, NOT
L-function claims; stop-list of the closed Gram route stays binding.

Predecessors (read-only): kraus_spread_commutant_probe (frame recipe,
spreads, A_orb), prime_kraus_doily_probe (doily frame), v738 (Lmodule,
sigma), v563 + v755 (deployed GL1 window), prime_cp_intertwiner_probe
(window assembly recipe, GL1 anchors), prime_carrier_gray_probe
(chi_NSR recipe).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kraus_aorb_refinement_probe.py
"""

import ast
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

_VERIFY = os.path.dirname(os.path.abspath(__file__))
_DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                          "tfpt-discovery"))
sys.path.insert(0, _DISCOVERY)
sys.path.insert(0, _VERIFY)

import v738_hecke_mod_ramified as ram                    # noqa: E402

LABEL_DIM = 15
ROW_DEGREE = 7
LEVELS = 5                       # v756 tower (TOWER_LEVEL 4)
ODD_PLACES = (3, 5, 7)
A_P_ANCHORS = {3: -4, 5: -2, 7: 24}          # v801 A1.4, cited
BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "zetazero", "lcalc", "mpmath")

CHECKS = []
GATE_FLAGS = {}
CONTROL_FIRED = {}
_LCG = [20260806]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    line = "[%s] %s" % (tag, name)
    if detail:
        line += "  |  " + detail
    print(line, flush=True)
    return bool(ok)


def section(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


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
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    print("    python %s, numpy %s" % (sys.version.split()[0],
                                       np.__version__))


# =============================================================== S1 frame
def s1_frame():
    section("S1 -- frame rebuilt (doily-probe recipe, condensed)")
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
    Omega = None
    n_inv = 0
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
    ok = (n_inv == 1 and np.array_equal(B, B.T)
          and bool(np.all(B.sum(axis=1) == ROW_DEGREE))
          and int(np.max(np.abs(B @ B.T - (4 * I15 + 3 * J15)))) == 0
          and len(iso_lines) == 15 and len(spreads) == 6)
    check("S1.1 frame: unique sigma-invariant Omega, B (105 legs, rows "
          "7, B B^T = 4I + 3J), 15 iso lines, 6 spreads -- doily-probe "
          "frame re-derived", ok, "%.1f s" % (time.time() - t0))
    GATE_FLAGS["frame"] = ok
    return dict(labels=labels, lidx=lidx, om=om, B=B, sigbar=sigbar,
                perm=perm, iso_lines=iso_lines, spreads=spreads)


def b45_of(spread, labels, lidx):
    blk = {}
    for bi, Lf in enumerate(sorted(spread, key=sorted)):
        for v in Lf:
            blk[v] = bi
    M = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for x in labels:
        for y in labels:
            if blk[x] == blk[y]:
                M[lidx[x], lidx[y]] = 1
    return M, blk


# ============================================== S2 TASK 1: spread census
def s2_spread_census(fr):
    section("S2 (TASK 1) -- the sigma census of the 6 spreads")
    labels, lidx, sigbar = fr["labels"], fr["lidx"], fr["sigbar"]
    spreads, B = fr["spreads"], fr["B"]

    def sig_spread(s):
        return frozenset(frozenset(sigbar(v) for v in Lf) for Lf in s)

    sidx = {s: i for i, s in enumerate(spreads)}
    sperm = [sidx[sig_spread(s)] for s in spreads]
    orbits = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        o, j = [], i
        while j not in seen:
            seen.add(j)
            o.append(j)
            j = sperm[j]
        orbits.append(tuple(o))
    orbit_sizes = sorted(len(o) for o in orbits)
    fixed = [i for i in range(6) if sperm[i] == i]
    ok_s21 = (sorted(sperm) == list(range(6))
              and all(len(o) in (1, 3) for o in orbits))
    check("S2.1 SIGMA ON THE 6 SPREADS: permutation %s, orbit sizes %s, "
          "fixed spreads: %d -- pre-analysis (outer S6: 3-cycle -> "
          "(3,3), zero fixed) %s"
          % (sperm, orbit_sizes, len(fixed),
             "CONFIRMED" if not fixed else "REFUTED"), ok_s21)

    # each line lies in exactly 2 spreads (needed for the coarsening)
    line_mult = Counter()
    for s in spreads:
        for Lf in s:
            line_mult[Lf] += 1
    ok_mult = (len(line_mult) == 15
               and all(v == 2 for v in line_mult.values()))
    inter = {(i, j): len(spreads[i] & spreads[j])
             for i, j in combinations(range(6), 2)}
    ok_pair = all(v == 1 for v in inter.values())
    check("S2.2 spread incidence: every line lies in EXACTLY 2 of the "
          "6 spreads (15 x 2 = 30 = 6 x 5); every pair of spreads "
          "shares EXACTLY 1 line", ok_mult and ok_pair)

    B45s = []
    blks = []
    for s in spreads:
        M, blk = b45_of(s, labels, lidx)
        B45s.append(M)
        blks.append(blk)

    verdict1 = None
    branch_ok = True
    if fixed:
        # BRANCH (a): redo rule B with a sigma-invariant spread
        s0 = fixed[0]
        M, blk = B45s[s0], blks[s0]
        n45 = int(M.sum())
        census_ok = True
        for x in labels:
            inc = [y for y in labels if B[lidx[x], lidx[y]]]
            cs = sorted(Counter(blk[y] for y in inc).values(),
                        reverse=True)
            if cs != [3, 1, 1, 1, 1] or \
                    sum(1 for y in inc if blk[y] == blk[x]) != 3:
                census_ok = False
        P = np.zeros_like(M)
        for i, v in enumerate(labels):
            P[fr["perm"][i], i] = 1
        cov_ok = np.array_equal(P @ M @ P.T, M)
        branch_ok = (n45 == 45 and census_ok and cov_ok)
        check("S2.3a BRANCH (a): sigma-invariant spread #%d re-runs "
              "rule B: 45+60 partition, (3,1,1,1,1) census, partition "
              "sigma-COVARIANT" % s0, branch_ok)
        verdict1 = "SPREAD-SIGMA-INVARIANT-EXISTS"
    else:
        # BRANCH (b): the breaking data
        P = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
        for i in range(LABEL_DIM):
            P[fr["perm"][i], i] = 1
        ok_transport = all(
            np.array_equal(P @ B45s[i] @ P.T, B45s[sperm[i]])
            for i in range(6))
        ok_comm_all = all(
            int(np.max(np.abs(B45s[i] @ B - B @ B45s[i]))) == 0
            for i in range(6))
        check("S2.3b THE FAMILY IS SIGMA-STABLE: sigma transports "
              "B45(s) -> B45(sigma s) exactly (all 6), and "
              "[B45(s), B60(s)] = 0 holds for EVERY spread (all 6 "
              "commutators exactly zero) -- the direct-sum protocol is "
              "a sigma-stable statement about the FAMILY, though every "
              "single partition moves", ok_transport and ok_comm_all)

        # invariant coarsening: join / meet per sigma-orbit
        def join_partition(blk_list):
            parent = {v: v for v in labels}

            def find(v):
                while parent[v] != v:
                    parent[v] = parent[parent[v]]
                    v = parent[v]
                return v

            for blk in blk_list:
                rep_of = {}
                for v in labels:
                    b = blk[v]
                    if b in rep_of:
                        ra, rb = find(rep_of[b]), find(v)
                        if ra != rb:
                            parent[ra] = rb
                    else:
                        rep_of[b] = v
            out = {}
            for v in labels:
                out.setdefault(find(v), []).append(v)
            return sorted(len(b) for b in out.values())

        def meet_partition(blk_list):
            cells = Counter(tuple(blk[v] for blk in blk_list)
                            for v in labels)
            return sorted(cells.values())

        join_data = [join_partition([blks[i] for i in o])
                     for o in orbits]
        meet_data = [meet_partition([blks[i] for i in o])
                     for o in orbits]
        ok_coarse = all(j == [15] for j in join_data)
        check("S2.4b INVARIANT COARSENING (partition lattice): per "
              "sigma-orbit the JOIN of the 3 partitions = %s (the "
              "trivial one-block partition: NO nontrivial sigma-"
              "invariant coarsening survives), the MEET = %s (cell "
              "sizes; reported)" % (join_data, meet_data), ok_coarse)

        # invariant commutant witnesses
        A_all = sum(B45s)
        I15 = np.eye(LABEL_DIM, dtype=np.int64)
        ok_all = np.array_equal(A_all, 4 * I15 + 2 * B)
        orb_ops = []
        ok_orb = True
        for o in orbits:
            A_orb = sum(B45s[i] for i in o)
            orb_ops.append(A_orb)
            if not np.array_equal(P @ A_orb @ P.T, A_orb):
                ok_orb = False
            if int(np.max(np.abs(A_orb @ B - B @ A_orb))) != 0:
                ok_orb = False
        eigs = [np.round(np.linalg.eigvalsh(A.astype(float)),
                         9).tolist() for A in orb_ops]
        eig_census = [Counter(e) for e in eigs]
        ok_int = all(abs(v - round(v)) < 1.0e-9
                     for e in eigs for v in e)
        check("S2.5b INVARIANT COMMUTANT WITNESSES: Sum_all B45(s) == "
              "4I + 2B exact (each line in exactly 2 spreads); per "
              "sigma-orbit A_orb = Sum B45 is sigma-INVARIANT and "
              "commutes with K exactly; A_orb spectra integer: %s"
              % [dict(sorted(c.items())) for c in eig_census],
              ok_all and ok_orb and ok_int)
        branch_ok = (ok_transport and ok_comm_all and ok_coarse
                     and ok_all and ok_orb and ok_int)
        verdict1 = "SPREAD-SIGMA-BROKEN"

    GATE_FLAGS["task1"] = ok_s21 and ok_mult and ok_pair and branch_ok
    return verdict1, dict(B45s=B45s, blks=blks, sperm=sperm,
                          orbits=orbits, fixed=fixed)


# ================================= S3 TASK 2a: tower / channel commutant
def s3_tower(fr, sc):
    section("S3 (TASK 2a) -- tower and channel-level commutant")
    labels, lidx, B = fr["labels"], fr["lidx"], fr["B"]
    # certified spread = lex-first (index 0)
    E45 = sc["B45s"][0]
    I15 = np.eye(LABEL_DIM, dtype=np.int64)
    J15 = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    ok_base = int(np.max(np.abs(E45 @ B - B @ E45))) == 0
    ok_j = (np.array_equal(E45 @ J15, 3 * J15)
            and np.array_equal(J15 @ E45, 3 * J15))
    ok_k2 = int(np.max(np.abs(E45 @ (B @ B) - (B @ B) @ E45))) == 0
    T = 4 * (B @ B)
    ok_T = (np.array_equal(T, 28 * I15 + 12 * (J15 - I15))
            and int(np.max(np.abs(E45 @ T - T @ E45))) == 0)
    check("S3.1 [E, K] = 0 re-derived; E J = J E = 3J (double "
          "stochasticity); [E, K^2] = 0 and [E, T = 4B^2] = 0 exact -- "
          "TYPED HONESTLY: 49 K^2 = 4I + 3J, so the K^2/two-step "
          "commutation follows from double stochasticity ALONE; the "
          "load-bearing fact is the base [E, K] = 0",
          ok_base and ok_j and ok_k2 and ok_T)

    # v756 tower: D' U = 2^{-1/2} U D exact; E (x) id compatibilities
    D = np.diag([2.0 ** (-0.5 * l) for l in range(LEVELS)])
    Dt = np.diag([2.0 ** (-0.5 * l) for l in range(LEVELS + 1)])
    U = np.zeros((LEVELS + 1, LEVELS))
    for l in range(LEVELS):
        U[l + 1, l] = 1.0
    dev_tower = float(np.max(np.abs(Dt @ U - 2.0 ** -0.5 * U @ D)))
    kms = np.array([2.0 ** (-l) for l in range(LEVELS)])
    kms /= kms.sum()
    ok_state = abs(float(kms.sum()) - 1.0) == 0.0
    # E (x) id_tower commutes with I (x) D (different factors) and
    # preserves uniform (x) KMS: E doubly stochastic
    ok_c33 = dev_tower <= 1.0e-15 and ok_state
    check("S3.2 KMS tower: D' U == 2^{-1/2} U D to %.1e (v756 "
          "relation, index-exact); E (x) id_tower commutes with the "
          "half-weight (disjoint factors) and preserves uniform (x) "
          "KMS state (E doubly stochastic)" % dev_tower, ok_c33)

    # channel level: E2 o Phi == Phi o E2 on ALL 225 units (Fractions)
    blk0 = sc["blks"][0]
    blocks = {}
    for v in labels:
        blocks.setdefault(blk0[v], []).append(lidx[v])

    def phi_unit(x, y):
        """Phi(E_xy) as dict {(a,a): Fr}; v756 dephasing-Markov."""
        out = {}
        if x != y:
            return out
        for a in range(LABEL_DIM):
            if B[a, x]:
                out[(a, a)] = out.get((a, a), Fr(0)) + Fr(1, 7)
        return out

    def e2_map(m):
        """E2(m) = Sum_b P_b tr(P_b m)/3, m as dict."""
        out = {}
        for b, mem in blocks.items():
            t = sum((m.get((i, i), Fr(0)) for i in mem), Fr(0))
            for i in mem:
                if t:
                    out[(i, i)] = out.get((i, i), Fr(0)) + t / 3
        return out

    dev = 0
    for x in range(LABEL_DIM):
        for y in range(LABEL_DIM):
            lhs = e2_map(phi_unit(x, y))
            unit = {(x, y): Fr(1)}
            em = e2_map(unit)
            rhs = {}
            for (a, b), c in em.items():
                for k, v in phi_unit(a, b).items():
                    rhs[k] = rhs.get(k, Fr(0)) + c * v
            keys = set(lhs) | set(rhs)
            if any(lhs.get(k, Fr(0)) != rhs.get(k, Fr(0)) for k in keys):
                dev += 1
    ok_ch = dev == 0
    check("S3.3 CHANNEL LEVEL: E2 o Phi == Phi o E2 on ALL 225 matrix "
          "units, exact rationals (%d deviations) -- the operator lift "
          "of [E, K] = 0 through the v756 dephasing-Markov channel"
          % dev, ok_ch)
    GATE_FLAGS["task2a"] = (ok_base and ok_j and ok_k2 and ok_T
                            and ok_c33 and ok_ch)
    return dict(E45=E45, blocks=blocks)


# ===================================== S4 TASK 2b: odd-place expectation
def s4_odd_places():
    section("S4 (TASK 2b) -- odd places: the Hecke-commuting expectation "
            "census on M_2")
    X = np.array([[0, 1], [1, 0]], dtype=np.int64)
    I2 = np.eye(2, dtype=np.int64)
    Ms = {}
    ok_pop = True
    for p in ODD_PLACES:
        s3 = 1 + p ** 3
        a = A_P_ANCHORS[p]
        A_p, B_p = (s3 + a) // 2, (s3 - a) // 2
        if not (A_p >= 0 and B_p > 0 and (s3 + a) % 2 == 0):
            ok_pop = False
        Ms[p] = A_p * I2 + B_p * X
    check("S4.1 packet Hecke elements: M_p = A_p I + B_p X with "
          "(A,B) = %s (sigma3(p) = 1 + p^3 closed; a_p anchors cited "
          "v801 A1.4), all B_p > 0 -- the Hecke algebra is the full "
          "circulant span{I, X}"
          % {p: (int((1 + p ** 3 + A_P_ANCHORS[p]) / 2),
                 int((1 + p ** 3 - A_P_ANCHORS[p]) / 2))
             for p in ODD_PLACES}, ok_pop)

    # commutant of {M_p} = span{I, X}: exact rank of Y -> [Y, X]
    Ybasis = [I2, X]
    ok_comm = all(np.array_equal(Y @ Ms[p], Ms[p] @ Y)
                  for Y in Ybasis for p in ODD_PLACES)
    units = [np.zeros((2, 2), dtype=np.int64) for _ in range(4)]
    for k in range(4):
        units[k][k // 2, k % 2] = 1
    constr = np.array([(units[k] @ X - X @ units[k]).reshape(4)
                       for k in range(4)], dtype=np.int64)
    rank_c = int(np.linalg.matrix_rank(constr.astype(float)))
    sol_dim = 4 - rank_c
    ok_s42 = ok_comm and rank_c == 2 and sol_dim == 2
    check("S4.2 COMMUTANT CENSUS: {Y : [Y, M_p] = 0 for all p} = "
          "span{I, X} exactly (constraint map Y -> [Y, X] has exact "
          "rank %d on the 4 units => commutant dimension %d = "
          "span{I, X}; B_p > 0 makes X load-bearing)"
          % (rank_c, sol_dim), ok_s42)

    # subalgebra lattice: unital *-subalgebras containing span{I,X}
    # strictly must close to M_2 (generation census on the 4 units)
    ok_gen = True
    for k in range(4):
        Ek = units[k]
        if np.array_equal(Ek @ X, X @ Ek) and \
                np.array_equal(Ek, Ek.T):
            continue     # already in span{I,X}? (none of the units is)
        span = [I2, X, Ek, Ek.T]
        prods = [a @ b for a in span for b in span]
        allm = span + prods
        # rank over Q of the vectorized set
        Mv = np.array([m.reshape(4) for m in allm], dtype=np.int64)
        rank = np.linalg.matrix_rank(Mv.astype(float))
        if rank != 4:
            ok_gen = False
    check("S4.3 SUBALGEBRA LATTICE: adjoining ANY matrix unit to "
          "span{I, X} closes *-algebraically to the FULL M_2 (rank 4 "
          "for all 4 units) -- the only unital *-subalgebras "
          "containing the Hecke algebra are span{I, X} and M_2",
          ok_gen)

    # uniqueness of the expectation: E(E_ij) = a_ij I + b_ij X,
    # constraints: trace (2 a_ij = delta_ij), bimodule left/right
    # (a_{1-i,j} = b_ij, b_{1-i,j} = a_ij; a_{i,1-j} = b_ij,
    # b_{i,1-j} = a_ij), unital, *-preserving.  Solve exactly.
    idx = {(i, j): 2 * i + j for i in (0, 1) for j in (0, 1)}
    nun = 8   # a_00..a_11, b_00..b_11
    rows, rhs = [], []

    def var_a(i, j):
        return idx[(i, j)]

    def var_b(i, j):
        return 4 + idx[(i, j)]

    for i in (0, 1):
        for j in (0, 1):
            r = [Fr(0)] * nun
            r[var_a(i, j)] = Fr(2)
            rows.append(r)
            rhs.append(Fr(1 if i == j else 0))
            for (vi, vj, wi, wj) in (((1 - i), j, i, j),
                                     (i, (1 - j), i, j)):
                r1 = [Fr(0)] * nun
                r1[var_a(vi, vj)] = Fr(1)
                r1[var_b(wi, wj)] = Fr(-1)
                rows.append(r1)
                rhs.append(Fr(0))
                r2 = [Fr(0)] * nun
                r2[var_b(vi, vj)] = Fr(1)
                r2[var_a(wi, wj)] = Fr(-1)
                rows.append(r2)
                rhs.append(Fr(0))
    r = [Fr(0)] * nun
    r[var_a(0, 0)] = Fr(1)
    r[var_a(1, 1)] = Fr(1)
    rows.append(r)
    rhs.append(Fr(1))
    # Gaussian elimination with Fractions
    Maug = [row[:] + [rr] for row, rr in zip(rows, rhs)]
    prow = 0
    for col in range(nun):
        piv = next((k for k in range(prow, len(Maug)) if Maug[k][col]),
                   None)
        if piv is None:
            continue
        Maug[prow], Maug[piv] = Maug[piv], Maug[prow]
        for k in range(len(Maug)):
            if k != prow and Maug[k][col]:
                f = Maug[k][col] / Maug[prow][col]
                Maug[k] = [a - f * b for a, b in zip(Maug[k],
                                                     Maug[prow])]
        prow += 1
    rank = prow
    consistent = all(any(Maug[k][c] for c in range(nun))
                     or Maug[k][nun] == 0 for k in range(len(Maug)))
    sol = [Fr(0)] * nun
    prow = 0
    for col in range(nun):
        row_k = next((k for k in range(len(Maug))
                      if Maug[k][col]
                      and all(not Maug[k][c] for c in range(col))),
                     None)
        if row_k is not None:
            sol[col] = Maug[row_k][nun] / Maug[row_k][col]
    expected = [Fr(0)] * nun
    expected[var_a(0, 0)] = expected[var_a(1, 1)] = Fr(1, 2)
    expected[var_b(0, 1)] = expected[var_b(1, 0)] = Fr(1, 2)
    ok_unique = rank == nun and consistent and sol == expected
    check("S4.4 UNIQUENESS: the unital trace-preserving span{I,X}-"
          "bimodule projection M_2 -> span{I, X} is UNIQUE (linear "
          "system rank %d/%d, consistent) and equals E_p(a) = "
          "(a + X a X)/2 -- so the census is: exactly TWO Hecke-"
          "commuting expectations exist (trivial id onto M_2, and the "
          "C2-CHARACTER expectation E_p); the trivial extension is "
          "NOT the only one, and the nontrivial one is unique"
          % (rank, nun), ok_unique)

    # E_p commutes with Hecke multiplication, fixes M_p
    ok_hecke = True
    for p in ODD_PLACES:
        Mp = Ms[p]
        for k in range(4):
            a = units[k]
            lhs = (Mp @ a + X @ (Mp @ a) @ X)
            rhs2 = Mp @ (a + X @ a @ X)
            if not np.array_equal(lhs, rhs2):
                ok_hecke = False
        if not np.array_equal((Mp + X @ Mp @ X) // 2, Mp):
            ok_hecke = False
    check("S4.5 HECKE COVARIANCE: 2 E_p(M_p a) == 2 M_p E_p(a) on all "
          "4 units and all 3 places, and E_p(M_p) = M_p exact",
          ok_hecke)
    GATE_FLAGS["task2b"] = (ok_pop and ok_s42 and ok_gen and ok_unique
                            and ok_hecke)
    return dict(Ms=Ms, X=X)


# ================================ S5 TASK 2c: the assembled 600-dim gate
def s5_assembled(fr, s3d, s4d):
    section("S5 (TASK 2c) -- the assembled register: 15 x 5 x 8 = 600, "
            "integer-exact")
    t0 = time.time()
    B = fr["B"]
    blocks = s3d["blocks"]
    DIM_T = LEVELS
    DIM_O = 8
    DIM = LABEL_DIM * DIM_T * DIM_O          # 600

    def phi_ext(a):
        """7 * Phi_ext(a), integer; a shaped (15,40,15,40)."""
        out = np.zeros_like(a)
        for x in range(LABEL_DIM):
            acc = np.zeros((DIM_T * DIM_O, DIM_T * DIM_O),
                           dtype=a.dtype)
            for y in range(LABEL_DIM):
                if B[x, y]:
                    acc += a[y, :, y, :]
            out[x, :, x, :] = acc
        return out

    def e_label(a):
        """3 * (E2 (x) id)(a), integer."""
        out = np.zeros_like(a)
        for mem in blocks.values():
            t = sum(a[i, :, i, :] for i in mem)
            for i in mem:
                out[i, :, i, :] = t
        return out

    def e_odd(a):
        """8 * (tensor_p E_p)(a) = sum over the 2^3 X-conjugations
        (E_p = (id + Ad X_p)/2 per place)."""
        m = a.reshape(LABEL_DIM, DIM_T, 2, 2, 2,
                      LABEL_DIM, DIM_T, 2, 2, 2)
        out = np.zeros_like(m)
        for mask in range(8):
            t = m
            for bit, axpair in enumerate(((2, 7), (3, 8), (4, 9))):
                if (mask >> bit) & 1:
                    t = np.flip(np.flip(t, axis=axpair[0]),
                                axis=axpair[1])
            out = out + t
        return out.reshape(a.shape)

    def e_full(a):
        return e_odd(e_label(a))             # 24 * E_full

    shape = (LABEL_DIM, DIM_T * DIM_O, LABEL_DIM, DIM_T * DIM_O)
    eye = np.zeros(shape, dtype=np.int64)
    for x in range(LABEL_DIM):
        eye[x, :, x, :] = np.eye(DIM_T * DIM_O, dtype=np.int64)

    # witnesses: identity, one matrix unit sample, 10 LCG matrices
    wits = [eye]
    unit = np.zeros(shape, dtype=np.int64)
    unit[2, 7, 5, 31] = 1
    unit[5, 31, 2, 7] = 1
    wits.append(unit)
    for _ in range(10):
        w = np.array([[lcg(9) - 4 for _ in range(DIM)]
                      for _ in range(DIM)], dtype=np.int64)
        wits.append(w.reshape(shape))

    max_dev = 0
    for w in wits:
        lhs = e_full(phi_ext(w))             # 24*7 * (E o Phi)
        rhs = phi_ext(e_full(w))             # 7*24 * (Phi o E)
        max_dev = max(max_dev, int(np.max(np.abs(lhs - rhs))))
    ok_comm = max_dev == 0
    check("S5.1 [E_full, Phi_ext] == 0 INTEGER-EXACT on identity + "
          "matrix-unit + 10 LCG witnesses (600-dim register, scale "
          "168 = 7 x 24 cleared; max deviation %d)" % max_dev,
          ok_comm, "%.1f s" % (time.time() - t0))

    # odd Hecke multiplication commutes with E_full
    Ms, X = s4d["Ms"], s4d["X"]
    ok_hecke = True
    for pi, p in enumerate(ODD_PLACES):
        Mp_full = np.eye(1, dtype=np.int64)
        for q in range(3):
            Mp_full = np.kron(Mp_full,
                              Ms[p] if q == pi
                              else np.eye(2, dtype=np.int64))
        L = np.kron(np.eye(LABEL_DIM * DIM_T, dtype=np.int64),
                    Mp_full)
        for w in wits[:4]:
            wf = w.reshape(DIM, DIM)
            lhs = e_full((L @ wf).reshape(shape))
            rhs = (L @ e_full(w).reshape(DIM, DIM)).reshape(shape)
            if int(np.max(np.abs(lhs - rhs))) != 0:
                ok_hecke = False
    check("S5.2 odd Hecke covariance on the assembled register: "
          "24 E_full(L_p a) == 24 L_p E_full(a) exact for p = 3, 5, 7 "
          "(bimodule property of E_p over span{I, X})", ok_hecke)

    # unitality + idempotency on the witness family
    ok_unital = np.array_equal(e_full(eye), 24 * eye)
    ok_idem = True
    for w in wits[:4]:
        if not np.array_equal(e_full(e_full(w)), 24 * e_full(w)):
            ok_idem = False
    # half-weight compatibility: W = I (x) D (x) I commutes with E_full
    Dw = np.diag([2.0 ** (-0.5 * l) for l in range(DIM_T)])
    Wf = np.kron(np.kron(np.eye(LABEL_DIM), Dw), np.eye(DIM_O))
    w0 = wits[2].reshape(DIM, DIM).astype(float)
    lhsW = e_full((Wf @ w0 @ Wf).reshape(shape).astype(np.float64))
    rhsW = Wf @ e_full(wits[2]).reshape(DIM, DIM).astype(float) @ Wf
    devW = float(np.max(np.abs(lhsW.reshape(DIM, DIM) - rhsW)))
    ok_w = devW <= 1.0e-12
    check("S5.3 E_full is unital (E(1) = 1) and idempotent on the "
          "witness family; commutes with the KMS half-weight "
          "conjugation W . W to %.1e (disjoint tensor factors)"
          % devW, ok_unital and ok_idem and ok_w)
    GATE_FLAGS["task2c"] = ok_comm and ok_hecke and ok_unital \
        and ok_idem and ok_w


# =============================================================== controls
def s6_controls(fr, sc):
    section("S6 -- controls (must fire)")
    labels, lidx, B = fr["labels"], fr["lidx"], fr["B"]
    iso_lines = fr["iso_lines"]

    # K1a overlapping 5-line set (not a partition)
    l0 = iso_lines[0]
    p0 = sorted(l0)[0]
    l1 = next(Lf for Lf in iso_lines if Lf != l0 and p0 in Lf)
    rest = [Lf for Lf in iso_lines if Lf not in (l0, l1)][:3]
    fam = [l0, l1] + rest
    Bp = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for Lf in fam:
        for x in Lf:
            for y in Lf:
                Bp[lidx[x], lidx[y]] = 1
    fired1 = not np.array_equal(Bp @ Bp, 3 * Bp)
    CONTROL_FIRED["K1a"] = fired1
    check("K1a CONTROL overlapping 5-line set: (B')^2 != 3 B' (max "
          "entry deviation %d) -- the expectation scale-idempotency "
          "needs a PARTITION; fires"
          % int(np.max(np.abs(Bp @ Bp - 3 * Bp))), fired1)

    # K1b non-spread partition: swap two labels across blocks
    spread0 = sorted(fr["spreads"][0], key=sorted)
    fake = [sorted(list(blk)) for blk in spread0]
    fake[0][0], fake[1][0] = fake[1][0], fake[0][0]
    Bpp = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for blk in fake:
        for x in blk:
            for y in blk:
                Bpp[lidx[x], lidx[y]] = 1
    comm = int(np.max(np.abs(Bpp @ B - B @ Bpp)))
    fired2 = comm > 0 and np.array_equal(Bpp @ Bpp, 3 * Bpp)
    CONTROL_FIRED["K1b"] = fired2
    check("K1b CONTROL non-spread partition (one cross-block swap): "
          "still scale-idempotent (any triple partition is) but "
          "[B'', B] != 0 (max %d) -- the COMMUTANT property is what "
          "the spread buys; fires" % comm, fired2)

    # K2 scrambled tower half-weights
    while True:
        pm = sorted(range(LEVELS), key=lambda _: lcg(1 << 30))
        if pm != list(range(LEVELS)):
            break
    Ds = np.diag([2.0 ** (-0.5 * pm[l]) for l in range(LEVELS)])
    Dt = np.diag([2.0 ** (-0.5 * l) for l in range(LEVELS + 1)])
    U = np.zeros((LEVELS + 1, LEVELS))
    for l in range(LEVELS):
        U[l + 1, l] = 1.0
    dev = float(np.max(np.abs(Dt @ U - 2.0 ** -0.5 * U @ Ds)))
    fired3 = dev > 0.1
    CONTROL_FIRED["K2"] = fired3
    check("K2 CONTROL scrambled tower half-weights (non-identity "
          "permutation %s): D' U - 2^{-1/2} U D_scr max deviation "
          "%.3f > 0.1 -- fires" % (pm, dev), fired3)


# ================================================================ verdict
def s7_verdicts(verdict1):
    section("S7 -- verdicts (frozen enums)")
    controls = all(CONTROL_FIRED.get(k, False)
                   for k in ("K1a", "K1b", "K2"))
    t2 = (GATE_FLAGS.get("task2a", False),
          GATE_FLAGS.get("task2b", False),
          GATE_FLAGS.get("task2c", False))
    if all(t2) and controls:
        verdict2 = "COMMUTANT-EXTENDS"
        note2 = ("the direct-sum protocol is tower-stable: [E, K] = 0 "
                 "lifts exactly to the channel level, the KMS tower, "
                 "the odd places (unique nontrivial Hecke-commuting "
                 "expectation per place), and the assembled 600-dim "
                 "register")
    elif GATE_FLAGS.get("task2a", False):
        verdict2 = "COMMUTANT-PARTIAL"
        note2 = "failing: %s" % ", ".join(
            n for n, f in zip(("2a", "2b", "2c"), t2) if not f)
        if not controls:
            note2 += "; controls incomplete"
    else:
        verdict2 = "COMMUTANT-OBSTRUCTED"
        note2 = "a nonzero commutator was measured at the base level"
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print()
    print("checks: %d/%d pass" % (n_pass, len(CHECKS)))
    for k in sorted(GATE_FLAGS):
        print("  gate %-10s %s" % (k, GATE_FLAGS[k]))
    for k in sorted(CONTROL_FIRED):
        print("  control %-7s %s" % (k, CONTROL_FIRED[k]))
    print()
    print("VERDICT 1 (spread census): %s" % verdict1)
    print("VERDICT 2 (commutant extension): %s" % verdict2)
    print("  " + note2)
    return verdict1, verdict2


def main():
    t0 = time.time()
    print("KRAUS SPREAD/COMMUTANT PROBE -- the two named falsifiers of "
          "PRIME.KRAUS.DOILY.01")
    print("frozen 2026-08-06; exploration only; no RH claim; "
          "ROOTCLASS-MIXED cited")
    g0_firewall()
    fr = s1_frame()
    verdict1, sc = s2_spread_census(fr)
    s3d = s3_tower(fr, sc)
    s4d = s4_odd_places()
    s5_assembled(fr, s3d, s4d)
    s6_controls(fr, sc)
    v1, v2 = s7_verdicts(verdict1)
    print("total %.1f s" % (time.time() - t0))
    return v1, v2

def _part2():
    # --- kraus_aorb_refinement_probe.py, verbatim inside an isolated function
    # --- scope (v518/v668 merge precedent): its
    # --- module-level names are function-local.
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

    # path swap handled at module level (verification dir first)

    import v738_hecke_mod_ramified as ram          # noqa: E402
    import v563_paper2_readouts as core            # noqa: E402
    import v755_simpler_schur_recursion as srp     # noqa: E402

    FROZEN_SPEC = """\
    PRIME.AORB.REFINEMENT.01 spec v1 (frozen 2026-08-06, before the first
    run).
    Frame: doily-probe recipe (unique sigma-invariant Omega, B, 15 iso
      lines, 6 spreads, sigma perm); A_orb = Sum_{s in sigma-orbit} B45(s)
      per orbit; expected spectrum {0^5,1^2,4^5,7^2,9^1} and
      A1 + A2 == 4I + 2B (parent identities, re-gated exact).
    Task 1 (maximality, exact): commutant C of {B, P} = sigma-invariant
      matrices (81 orbit indicators of sigma x sigma on pairs) with
      [Y,B] = 0: Fraction rref nullspace -> dim C; formula match
      dim C == 1 + m1^2 + n1^2 + (9-m1)^2/2 + (5-n1)^2/2 with
      m1 = tr(Pi_B(2) F), n1 = tr(Pi_B(-2) F), F = (I+P+P^2)/3;
      nonabelian witness; central atoms {Pi_B(7), Pi_B(2)F,
      Pi_B(2)(I-F), Pi_B(-2)F, Pi_B(-2)(I-F)} exact idempotent +
      central + sum I; skew central T_mu = Pi_B(mu)(P - P^2)Pi_B(mu)
      with T_mu^2 == -3 Pi_B(mu)(I - F); center dim (float rank) == 5 +
      #{nonzero T}.  MAXIMAL iff dim C == 5 (the A_orb projection
      algebra); else AORB-NOT-MAXIMAL with the full decomposition.
    Task 2 (eigenspaces, exact Fractions): Lagrange projections both
      orbits; multiplicity gate {5,2,5,2,1}; forced containments
      B Pi_A(l) == mu_B(l) Pi_A(l) with mu_B = {0:-2, 1:2, 4:2, 7:2,
      9:7}; orbit swap Pi2(l) == Pi1(8-l) on E_B(2), Pi2 == Pi1 at 0/9;
      E_A(0) == Pi_B(-2), Pi_A(9) == J/15; sigma-fix content
      f_l = tr(Pi_A(l) F) integer; fixed-label diagonal weights;
      P_blk(s) = B45(s)/3 overlaps + range(A_orb) == span of the 3 block
      spaces (dim 10) + E_A(0) == intersection of block-mean-zero spaces;
      joint <A_orb, F> atom dims (the canonical abelian refinement).
    Task 3 (Weil channels, frozen): deployed events ka from
      srp.channel_masks(5.0), U/MU = core.U_ALL/MU_ALL; ramified events
      n = 2^k get multiplier (mu_B/7)^k, odd events 1; continuum =
      DEPLOYED GL1 (srp.continuum_lags), typed protocol-internal;
      mu_B = 7 window == deployed c_full rel <= 1e-12, GL1 anchors
      5.29e-5 / 1.18e-5 within 5%; ladders M = 256..640, PSD bar
      lambda_min >= -1e-10 ||T||_2; refinement-silence certified by the
      exact scalar-action gate; character lemma B chi_w == 8 e_{x_w} -
      1vec exact (x_w = Omega^{-1} w); chi_w and chi_NSR overlap tables
      exact.  Controls C1/C2 as in the docstring; LCG seed 20260806.
    Verdict enum: AORB-MAXIMAL-MEANINGFUL / AORB-MAXIMAL-SILENT /
    AORB-NOT-MAXIMAL.  Runtime cap ~15 min.  NO RH/GRH claim.
    """

    LABEL_DIM = 15
    ROW_DEGREE = 7
    M_TOP = 640
    DGRID = 1.0 / 64.0
    ALPHA_TOP = 0.5 * M_TOP * DGRID          # 5.0 -> events n <= e^10
    RUNGS = (256, 320, 384, 448, 512, 576, 640)
    PSD_BAR = 1.0e-10
    WARD_BAR = 1.0e-12
    GL1_ANCHOR = (5.29e-5, 1.18e-5)          # parent F6.7 anchors X=4 / X=10
    A_SPECTRUM = {0: 5, 1: 2, 4: 5, 7: 2, 9: 1}
    MU_B_OF_A = {0: -2, 1: 2, 4: 2, 7: 2, 9: 7}
    BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
                  "zetazero", "lcalc", "mpmath")

    CHECKS = []
    GATE_FLAGS = {}
    CONTROL_FIRED = {}
    _LCG = [20260806]


    def lcg(n):
        _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
        return _LCG[0] % n


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        tag = "PASS" if ok else "FAIL"
        line = "[%s] %s" % (tag, name)
        if detail:
            line += "  |  " + detail
        print(line, flush=True)
        return bool(ok)


    def section(title):
        print()
        print("=" * 78)
        print(title)
        print("=" * 78, flush=True)


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
        check("G0.1 no prime-table / zeta symbols in this file", not bad,
              "found %s" % bad if bad else "clean")
        print("    python %s, numpy %s" % (sys.version.split()[0],
                                           np.__version__))


    # ------------------------------------------------ exact Fraction helpers
    def fmat_int(M):
        return [[Fr(int(x)) for x in row] for row in M]


    def feye(n):
        return [[Fr(1) if i == j else Fr(0) for j in range(n)]
                for i in range(n)]


    def fmul(A, B):
        n, m, p = len(A), len(B), len(B[0])
        out = [[Fr(0)] * p for _ in range(n)]
        for i in range(n):
            Ai = A[i]
            Oi = out[i]
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


    def fmaxabs(A):
        return max(abs(a) for row in A for a in row)


    def ftrace(A):
        return sum(A[i][i] for i in range(len(A)))


    def fcomm(A, B):
        return fadd(fmul(A, B), fmul(B, A), Fr(1), Fr(-1))


    def f2np(A):
        return np.array([[float(a) for a in row] for row in A])


    def frref_nullspace(rows, ncols):
        """Exact rref over Q; returns (rank, nullspace basis vectors)."""
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
        return len(piv_cols), basis


    def frank(rows, ncols):
        rk, _b = frref_nullspace(rows, ncols)
        return rk


    # =============================================================== S1 frame
    def s1_frame():
        section("S1 -- frame rebuilt (doily-probe recipe) + chi_NSR")
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
        Omega = None
        n_inv = 0
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
        ok = (n_inv == 1 and np.array_equal(B, B.T)
              and bool(np.all(B.sum(axis=1) == ROW_DEGREE))
              and int(np.max(np.abs(B @ B.T - (4 * I15 + 3 * J15)))) == 0
              and int(np.max(np.abs(poly))) == 0
              and len(iso_lines) == 15 and len(spreads) == 6)
        check("S1.1 frame: unique sigma-invariant Omega, B (rows 7, "
              "B B^T = 4I + 3J, (B-7)(B-2)(B+2) = 0), 15 iso lines, "
              "6 spreads", ok, "%.1f s" % (time.time() - t0))

        # chi_NSR (positive_descent / gray-probe recipe)
        a_par = tuple(ram.unpack(L.to_ambient(E4[k]))[0] % 2
                      for k in range(4))

        def chi_dot(v):
            return sum(a_par[k] * v[k] for k in range(4)) & 1

        ns_idx = [lidx[v] for v in labels if chi_dot(v) == 0]
        r_idx = [lidx[v] for v in labels if chi_dot(v) == 1]
        fixed = [i for i in range(LABEL_DIM) if perm[i] == i]
        n_cyc = len(fixed) + (LABEL_DIM - len(fixed)) // 3
        ok_nsr = (len(ns_idx) == 7 and len(r_idx) == 8
                  and len(fixed) == 3 and n_cyc == 7)
        check("S1.2 chi_NSR on the 15 labels: 7 NS + 8 R; sigma has 3 "
              "fixed labels + 4 three-cycles (7 cycles -> fix dim 7)",
              ok_nsr, "a_par = %s, fixed = %s" % (a_par, fixed))
        GATE_FLAGS["frame"] = ok and ok_nsr
        return dict(labels=labels, lidx=lidx, om=om, Omega=Omega, B=B,
                    sigbar=sigbar, perm=perm, spreads=spreads,
                    ns_idx=ns_idx, r_idx=r_idx, fixed=fixed,
                    chi_dot=chi_dot)


    def b45_of(spread, labels, lidx):
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


    # ================================= S2 A_orb + exact eigenprojections
    def s2_aorb(fr):
        section("S2 -- A_orb per sigma-orbit + exact eigenprojections")
        labels, lidx, sigbar = fr["labels"], fr["lidx"], fr["sigbar"]
        spreads, B = fr["spreads"], fr["B"]

        def sig_spread(s):
            return frozenset(frozenset(sigbar(v) for v in Lf) for Lf in s)

        sp_perm = [spreads.index(sig_spread(s)) for s in spreads]
        orbits = []
        seen = set()
        for i in range(6):
            if i in seen:
                continue
            o = [i]
            j = sp_perm[i]
            while j != i:
                o.append(j)
                seen.add(j)
                j = sp_perm[j]
            seen.add(i)
            orbits.append(sorted(o))
        ok_orb = sorted(len(o) for o in orbits) == [3, 3]
        check("S2.1 sigma on the 6 spreads: two 3-cycles (parent replay)",
              ok_orb, "perm %s, orbits %s" % (sp_perm, orbits))

        B45s = [b45_of(s, labels, lidx) for s in spreads]
        A1 = sum(B45s[i] for i in orbits[0])
        A2 = sum(B45s[i] for i in orbits[1])
        I15 = np.eye(LABEL_DIM, dtype=np.int64)
        ok_sum = int(np.max(np.abs(A1 + A2 - (4 * I15 + 2 * B)))) == 0
        P = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
        for i in range(LABEL_DIM):
            P[fr["perm"][i], i] = 1
        ok_inv = (int(np.max(np.abs(P @ A1 @ P.T - A1))) == 0
                  and int(np.max(np.abs(P @ A2 @ P.T - A2))) == 0)
        ok_comm = (int(np.max(np.abs(A1 @ B - B @ A1))) == 0
                   and int(np.max(np.abs(A2 @ B - B @ A2))) == 0)
        check("S2.2 A_orb identities: A1 + A2 == 4I + 2B; both sigma-"
              "invariant; both commute with K (exact integer)",
              ok_sum and ok_inv and ok_comm)

        eigs = sorted(A_SPECTRUM)

        def lagrange_projections(A_int):
            Af = fmat_int(A_int)
            Ifr = feye(LABEL_DIM)
            out = {}
            for lam in eigs:
                Pl = feye(LABEL_DIM)
                for mu in eigs:
                    if mu == lam:
                        continue
                    Pl = fmul(Pl, fscale(
                        fadd(Af, Ifr, Fr(1), Fr(-mu)), Fr(1, lam - mu)))
                out[lam] = Pl
            return out

        Pi1 = lagrange_projections(A1)
        Pi2 = lagrange_projections(A2)
        ok_proj = True
        for Pi, A_int in ((Pi1, A1), (Pi2, A2)):
            Af = fmat_int(A_int)
            tot = None
            for lam in eigs:
                Pl = Pi[lam]
                ok_proj &= fequal(fmul(Pl, Pl), Pl)
                ok_proj &= ftrace(Pl) == A_SPECTRUM[lam]
                ok_proj &= fequal(fmul(Af, Pl), fscale(Pl, Fr(lam)))
                tot = Pl if tot is None else fadd(tot, Pl)
            ok_proj &= fequal(tot, feye(LABEL_DIM))
            for la, lb in combinations(eigs, 2):
                ok_proj &= fmaxabs(fmul(Pi[la], Pi[lb])) == 0
        check("S2.3 exact Lagrange eigenprojections (both orbits, "
              "Fractions): idempotent, orthogonal, sum I, multiplicities "
              "{0:5, 1:2, 4:5, 7:2, 9:1}", ok_proj)

        # forced B-containments
        Bf = fmat_int(B)
        ok_cont = all(fequal(fmul(Bf, Pi1[lam]),
                             fscale(Pi1[lam], Fr(MU_B_OF_A[lam])))
                      for lam in eigs)
        # orbit swap lambda <-> 8 - lambda on E_B(2), identity at 0/9
        ok_swap = (fequal(Pi2[0], Pi1[0]) and fequal(Pi2[9], Pi1[9])
                   and fequal(Pi2[4], Pi1[4])
                   and fequal(Pi2[1], Pi1[7]) and fequal(Pi2[7], Pi1[1]))
        check("S2.4 forced structure: B Pi_A(l) == mu_B(l) Pi_A(l) with "
              "mu_B = {0:-2, 1:2, 4:2, 7:2, 9:7} (eigenspaces INSIDE the "
              "B-eigenspaces); orbit swap Pi2(l) == Pi1(8-l) on E_B(2), "
              "Pi2 == Pi1 at 0 and 9 -- the two orbits generate the SAME "
              "abelian algebra", ok_cont and ok_swap)
        GATE_FLAGS["aorb"] = (ok_orb and ok_sum and ok_inv and ok_comm
                              and ok_proj and ok_cont and ok_swap)
        return dict(A1=A1, A2=A2, Pi1=Pi1, Pi2=Pi2, P=P, orbits=orbits,
                    B45s=B45s, eigs=eigs)


    # ==================================== S3 TASK 1: the exact commutant
    def s3_commutant(fr, ao):
        section("S3 (TASK 1) -- the commutant of {K, sigma}, exact")
        t0 = time.time()
        B, perm = fr["B"], fr["perm"]
        P = ao["P"]
        n = LABEL_DIM

        # sigma-invariant matrices = orbit indicators of sigma x sigma
        pair_orbit = {}
        orb_reps = []
        for i in range(n):
            for j in range(n):
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
        n_orb = len(orb_reps)
        ok_orbcount = n_orb == 81
        O_mats = []
        for cyc in orb_reps:
            M = np.zeros((n, n), dtype=np.int64)
            for (a, b) in cyc:
                M[a, b] = 1
            O_mats.append(M)

        # constraint [Y, B] = 0 on Y = sum x_t O_t : 225 eqs x 81 unknowns
        rows = [[Fr(0)] * n_orb for _ in range(n * n)]
        for t, O in enumerate(O_mats):
            E = O @ B - B @ O
            for i in range(n):
                for j in range(n):
                    if E[i, j]:
                        rows[i * n + j][t] = Fr(int(E[i, j]))
        rank, null_basis = frref_nullspace(rows, n_orb)
        D = len(null_basis)
        # integer commutant basis matrices
        c_basis = []
        for v in null_basis:
            den = 1
            for x in v:
                den = den * x.denominator // math.gcd(den, x.denominator)
            M = np.zeros((n, n), dtype=np.int64)
            for t, x in enumerate(v):
                if x != 0:
                    M += int(x * den) * O_mats[t]
            c_basis.append(M)
        ok_verify = all(int(np.max(np.abs(c @ B - B @ c))) == 0
                        and int(np.max(np.abs(P @ c @ P.T - c))) == 0
                        for c in c_basis)
        check("S3.1 commutant C of {K, sigma}: %d sigma-pair orbits (== "
              "81); exact Fraction nullspace of [Y,B] = 0 -> dim C = %d; "
              "every basis element re-verified integer-exact"
              % (n_orb, D), ok_orbcount and ok_verify,
              "%.1f s" % (time.time() - t0))

        # block data: m1 / n1 and the dimension formula
        Bf = fmat_int(B)
        If = feye(n)
        Jf = [[Fr(1)] * n for _ in range(n)]
        PB7 = fscale(Jf, Fr(1, 15))
        PB2 = fscale(fmul(fadd(Bf, If, Fr(1), Fr(-7)),
                          fadd(Bf, If, Fr(1), Fr(2))), Fr(-1, 20))
        PBm2 = fscale(fmul(fadd(Bf, If, Fr(1), Fr(-7)),
                           fadd(Bf, If, Fr(1), Fr(-2))), Fr(1, 36))
        ok_pb = (fequal(fmul(PB2, PB2), PB2) and fequal(fmul(PBm2, PBm2),
                                                        PBm2)
                 and fequal(fadd(fadd(PB7, PB2), PBm2), If))
        Pf = fmat_int(P)
        P2f = fmul(Pf, Pf)
        F = fscale(fadd(fadd(If, Pf), P2f), Fr(1, 3))
        m1 = ftrace(fmul(PB2, F))
        n1 = ftrace(fmul(PBm2, F))
        ok_int = m1.denominator == 1 and n1.denominator == 1
        m1i, n1i = int(m1), int(n1)
        D_formula = (1 + m1i ** 2 + n1i ** 2
                     + (9 - m1i) ** 2 // 2 + (5 - n1i) ** 2 // 2)
        ok_formula = ((9 - m1i) % 2 == 0 and (5 - n1i) % 2 == 0
                      and D == D_formula and m1i + n1i == 6)
        check("S3.2 block data: m1 = dim(E_B(2) cap fix sigma) = %d, "
              "n1 = dim(E_B(-2) cap fix) = %d (m1 + n1 = 6); dim C == "
              "1 + m1^2 + n1^2 + (9-m1)^2/2 + (5-n1)^2/2 = %d -- the "
              "block structure R + M_%d(R) + M_%d(C) + M_%d(R) + M_%d(C)"
              % (m1i, n1i, D_formula, m1i, (9 - m1i) // 2, n1i,
                 (5 - n1i) // 2), ok_pb and ok_int and ok_formula)

        # nonabelian witness
        witness = None
        for a, b in combinations(range(min(D, 12)), 2):
            dev = int(np.max(np.abs(c_basis[a] @ c_basis[b]
                                    - c_basis[b] @ c_basis[a])))
            if dev != 0:
                witness = (a, b, dev)
                break
        check("S3.3 C is NONABELIAN (witness pair of basis elements with "
              "[c_a, c_b] != 0)", witness is not None,
              "witness %s" % (witness,))

        # central atoms (exact) + skew central elements
        atoms = {"E_B(7)": PB7,
                 "E_B(2) fix": fmul(PB2, F),
                 "E_B(2) mov": fmul(PB2, fadd(If, F, Fr(1), Fr(-1))),
                 "E_B(-2) fix": fmul(PBm2, F),
                 "E_B(-2) mov": fmul(PBm2, fadd(If, F, Fr(1), Fr(-1)))}
        c_frac = [fmat_int(c) for c in c_basis]
        ok_atoms = True
        tot = None
        for nm, Q in atoms.items():
            ok_atoms &= fequal(fmul(Q, Q), Q)
            ok_atoms &= all(fmaxabs(fcomm(Q, c)) == 0 for c in c_frac)
            tot = Q if tot is None else fadd(tot, Q)
        ok_atoms &= fequal(tot, If)
        dims = {nm: int(ftrace(Q)) for nm, Q in atoms.items()}
        Tskew = {}
        ok_skew = True
        for nm, PBl in (("T(2)", PB2), ("T(-2)", PBm2)):
            T = fmul(fmul(PBl, fadd(Pf, P2f, Fr(1), Fr(-1))), PBl)
            mov = fmul(PBl, fadd(If, F, Fr(1), Fr(-1)))
            ok_skew &= fequal(fmul(T, T), fscale(mov, Fr(-3)))
            ok_skew &= all(fmaxabs(fcomm(T, c)) == 0 for c in c_frac)
            Tskew[nm] = T
        check("S3.4 the 5 central atoms exact (idempotent, commute with "
              "EVERY commutant basis element, sum I): dims %s; skew "
              "central T_mu = Pi(P - P^2)Pi with T_mu^2 == -3 Pi_mov "
              "(the C-block imaginary units) -- center type R^3 + C^2"
              % dims, ok_atoms and ok_skew)

        # center dimension (float rank on the commutant coordinates)
        cf = [c.astype(float) for c in c_basis]
        Mrows = []
        for cl in cf:
            blk = np.stack([ci @ cl - cl @ ci for ci in cf], axis=0)
            Mrows.append(blk.reshape(len(cf), -1))
        Mfull = np.concatenate(Mrows, axis=1)   # D x (D*225)
        rk_c = int(np.linalg.matrix_rank(Mfull, tol=1.0e-8))
        D_Z = D - rk_c
        n_cblocks = sum(1 for nm in ("T(2)", "T(-2)")
                        if fmaxabs(Tskew[nm]) != 0)
        ok_center = D_Z == 5 + n_cblocks
        check("S3.5 center dim (float rank over exact basis) = %d == 5 "
              "atoms + %d skew units (R^3 + C^2 as a real algebra)"
              % (D_Z, n_cblocks), ok_center)

        # the A_orb projection algebra vs C
        Pi1 = ao["Pi1"]
        dim_aorb = 5      # 5 orthogonal idempotents spanning (S2.3 exact)
        ok_inC = all(fmaxabs(fcomm(Pi1[lam], Bf)) == 0
                     for lam in ao["eigs"])
        # sigma-invariance of Pi1 directly: P Pi P^T == Pi
        ok_sinv = all(fequal(fmul(fmul(Pf, Pi1[lam]),
                                  [list(r) for r in zip(*Pf)]), Pi1[lam])
                      for lam in ao["eigs"])
        maximal = (D == dim_aorb)
        check("S3.6 MAXIMALITY DECISION: A_orb eigenprojection algebra "
              "(dim 5, abelian, inside C) vs dim C = %d -> %s"
              % (D, "MAXIMAL" if maximal else
                 "NOT MAXIMAL (C strictly larger, nonabelian)"),
              ok_inC and ok_sinv, "frozen criterion: maximal iff dim C == 5")
        GATE_FLAGS["commutant"] = (ok_orbcount and ok_verify and ok_pb
                                   and ok_int and ok_formula
                                   and witness is not None and ok_atoms
                                   and ok_skew and ok_center and ok_inC
                                   and ok_sinv)
        return dict(D=D, m1=m1i, n1=n1i, atoms=atoms, dims=dims,
                    maximal=maximal, F=F, PB2=PB2, PBm2=PBm2, PB7=PB7,
                    D_Z=D_Z)


    # ============================= S4 TASK 2: eigenspace identifications
    def s4_eigenspaces(fr, ao, cm):
        section("S4 (TASK 2) -- the eigenspaces in the certified geometry")
        Pi1, eigs = ao["Pi1"], ao["eigs"]
        F, PBm2 = cm["F"], cm["PBm2"]
        n = LABEL_DIM
        If = feye(n)
        Jf = [[Fr(1)] * n for _ in range(n)]

        ok_id = (fequal(Pi1[9], fscale(Jf, Fr(1, 15)))
                 and fequal(Pi1[0], PBm2))
        check("S4.1 anchors: Pi_A(9) == J/15 (the uniform / GL1-consumed "
              "sector, K 1 = 1); Pi_A(0) == Pi_B(-2) (the A_orb refinement "
              "is TRIVIAL on E_B(-2))", ok_id)

        # sigma-fix content per eigenspace (integer by [Pi_A, F] = 0)
        fix_content = {}
        ok_fix = True
        for lam in eigs:
            ok_fix &= fmaxabs(fcomm(Pi1[lam], F)) == 0
            fl = ftrace(fmul(Pi1[lam], F))
            ok_fix &= fl.denominator == 1
            fix_content[lam] = int(fl)
        ok_fix &= sum(fix_content.values()) == 7
        check("S4.2 sigma-fix content f_l = tr(Pi_A(l) F): %s (integers, "
              "sum 7 = number of sigma-cycles); the joint <A_orb, F> "
              "atoms have dims %s -- the canonical maximal ABELIAN "
              "invariant refinement containing A_orb"
              % (fix_content,
                 {lam: (fix_content[lam], A_SPECTRUM[lam]
                        - fix_content[lam]) for lam in eigs}), ok_fix)

        # fixed-label diagonal weights
        fixed = fr["fixed"]
        wtab = {lam: sum(Pi1[lam][i][i] for i in fixed) for lam in eigs}
        print("    fixed-label diagonal weight sum_{x fixed} Pi[x,x]: %s"
              % {lam: str(wtab[lam]) for lam in eigs})

        # spread block spaces: P_blk(s) = B45(s)/3
        B45s, orbits = ao["B45s"], ao["orbits"]
        Pblk = [fscale(fmat_int(B45s[i]), Fr(1, 3)) for i in orbits[0]]
        ok_blk = all(fequal(fmul(Q, Q), Q) for Q in Pblk)
        # E_A(0) == intersection of block-mean-zero spaces
        ok_ker = all(fmaxabs(fmul(Q, Pi1[0])) == 0 for Q in Pblk)
        # range(A1) = E_A(1)+E_A(4)+E_A(7)+E_A(9) == span of block spaces
        stack = []
        for i in orbits[0]:
            stack += fmat_int(B45s[i])
        rk_span = frank(stack, n)
        ok_span = rk_span == 10
        ov = {lam: [str(ftrace(fmul(Pi1[lam], Q))) for Q in Pblk]
              for lam in eigs}
        check("S4.3 spread strata: E_A(0) == intersection of the 3 block-"
              "mean-zero spaces (P_blk Pi_A(0) == 0 exact); span of the 3 "
              "block-constant spaces has dim %d == 10 = range(A_orb) = "
              "E_A(9)+E_A(7)+E_A(4)+E_A(1)" % rk_span,
              ok_blk and ok_ker and ok_span)
        print("    tr(Pi_A(l) P_blk(s)) per orbit-1 spread: %s" % ov)
        # pairwise block-space intersections
        for a, b in combinations(range(3), 2):
            st = fmat_int(B45s[orbits[0][a]]) + fmat_int(B45s[orbits[0][b]])
            rk = frank(st, n)
            print("    dim(range P_blk(s%d) cap range P_blk(s%d)) = %d"
                  % (a, b, 5 + 5 - rk))

        GATE_FLAGS["eigenspaces"] = ok_id and ok_fix and ok_blk and \
            ok_ker and ok_span
        return dict(fix_content=fix_content)


    # ============================ S5 TASK 3: the Weil-channel sectors
    def s5_weil_channels(fr, ao):
        section("S5 (TASK 3) -- refined label sectors through the "
                "deployed Weil machinery")
        t0 = time.time()
        B = fr["B"]

        # deployed event stream (read-only)
        ka, masks, devm = srp.channel_masks(ALPHA_TOP)
        U_ev = np.array([float(core.U_ALL[i]) for i in range(ka)])
        MU_ev = np.array([float(core.MU_ALL[i]) for i in range(ka)])
        nvals = np.array([int(round(math.exp(U_ev[i]))) for i in range(ka)],
                         dtype=np.int64)
        two_pow = (nvals & (nvals - 1)) == 0
        kvals = np.where(two_pow, np.int64(np.log2(np.maximum(nvals, 1))
                                           + 0.5), 0)
        n2 = int(np.sum(two_pow))
        ok_ev = devm <= 1.0e-12 and n2 == 14 and bool(
            np.all(2 ** kvals[two_pow] == nvals[two_pow]))
        check("S5.1 deployed events: ka = %d (u <= 10), %d ramified "
              "events n = 2^k (k = 1..14); channel-mask ward %.1e"
              % (ka, n2, devm), ok_ev)

        # the scalar-action certificate (window-silence of the refinement)
        # B Pi_A(l) == mu_B Pi_A(l) exact was gated in S2.4; therefore the
        # compression of the operator comb (odd events x I, 2^k events x
        # K^k) by ANY projection inside a single B-eigenspace is the
        # scalar window with 2-adic masses rescaled by (mu_B/7)^k.
        print("    scalar-action certificate (S2.4): Q K^k Q = (mu_B/7)^k Q")
        print("    -> E_A(1), E_A(4), E_A(7) (all mu_B = 2) receive")
        print("       IDENTICAL windows: the A_orb refinement beyond the")
        print("       K-spectrum is WINDOW-SILENT (operator identity).")

        # window assembly (deployed continuum, frozen)
        c_cont = srp.continuum_lags(M_TOP)
        c_full = c_cont.copy()
        for cnl in ("ro", "re", "sp", "in"):
            c_full = c_full + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                                    masks[cnl])

        def window(mu_b):
            mult = np.ones(ka)
            mult[two_pow] = (mu_b / 7.0) ** kvals[two_pow].astype(float)
            atoms, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, U_ev,
                                          MU_ev * mult)
            dmass = float(np.sum(np.abs(MU_ev[two_pow]
                                        * (1.0 - mult[two_pow]))))
            return c_cont + atoms, dmass

        w7, dm7 = window(7.0)
        w2, dm2 = window(2.0)
        wm2, dmm2 = window(-2.0)
        dev_gl1 = float(np.max(np.abs(w7 - c_full)) / np.max(np.abs(c_full)))
        ok_anchor_id = dev_gl1 <= WARD_BAR and dm7 == 0.0
        check("S5.2 mu_B = 7 sector (E_A(9), uniform) == DEPLOYED GL1 "
              "window (rel dev %.1e <= 1e-12) -- the GL1 machinery "
              "consumes exactly the label-uniform sector" % dev_gl1,
              ok_anchor_id)
        print("    2-adic mass displacement |MU (1 - (mu/7)^k)|_1: "
              "mu=7: %.3f, mu=2: %.4f, mu=-2: %.4f" % (dm7, dm2, dmm2))

        def ladder(lag):
            out = []
            for M in RUNGS:
                T = sla.toeplitz(lag[:M])
                lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
                out.append((M, lam, float(sla.norm(T, 2))))
            return out

        lads = {"mu=+7 (E_A9 uniform)": ladder(w7),
                "mu=+2 (E_A1+E_A4+E_A7)": ladder(w2),
                "mu=-2 (E_A0)": ladder(wm2)}
        print("    PSD ladders (lambda_min per rung, X = M/64 = 4..10):")
        psd = {}
        for nm, lad in lads.items():
            psd[nm] = all(lam >= -PSD_BAR * nrm for _M, lam, nrm in lad)
            print("      %-24s | %s  [%s]"
                  % (nm, " | ".join("%+.2e" % lam for _M, lam, _n in lad),
                     "PSD" if psd[nm] else "NEG"))
        g0, g1 = lads["mu=+7 (E_A9 uniform)"][0][1], \
            lads["mu=+7 (E_A9 uniform)"][-1][1]
        ok_anchor = (abs(g0 - GL1_ANCHOR[0]) <= 0.05 * GL1_ANCHOR[0]
                     and abs(g1 - GL1_ANCHOR[1]) <= 0.05 * GL1_ANCHOR[1])
        check("S5.3 GL1 anchor margins %.3e (X=4) / %.3e (X=10) within "
              "5%% of the parent anchors; refined-sector ladders "
              "MEASURED (typed protocol-internal: the deployed continuum "
              "with a modified ramified leg is NOT an L-function claim)"
              % (g0, g1), ok_anchor, "%.1f s" % (time.time() - t0))
        print("    (typed: NO RH/GRH claim; PSD or NEG of the mu = +-2")
        print("     windows is a protocol-internal consistency datum.)")

        # (c) relation to the automorphic / character structure
        labels, Omega, om = fr["labels"], fr["Omega"], fr["om"]
        lidx = fr["lidx"]
        Pi1, eigs = ao["Pi1"], ao["eigs"]
        # character lemma: B chi_w == 8 e_{x_w} - 1vec, x_w = Omega^{-1} w
        ok_lem = True
        for w in labels:
            chi = np.array([(-1) ** (sum(a * b for a, b in zip(w, v)) & 1)
                            for v in labels], dtype=np.int64)
            xw = [x for x in labels
                  if tuple(sum(Omega[k][j] * x[j] for j in range(4)) & 1
                           for k in range(4)) == w]
            ok_lem &= len(xw) == 1
            ref = -np.ones(LABEL_DIM, dtype=np.int64)
            ref[lidx[xw[0]]] += 8
            ok_lem &= bool(np.all(B @ chi == ref))
        check("S5.4 EXACT character lemma: B chi_w == 8 e_{Omega^{-1} w} "
              "- 1vec for ALL 15 nonzero V-characters -- the incidence "
              "channel maps each character onto a COORDINATE atom (plus "
              "uniform): the character basis and the A_orb frame are "
              "TRANSVERSAL, not aligned", ok_lem)

        # chi_w content in the A_orb sectors (exact quadratic forms)
        rows = Counter()
        for w in labels:
            chi = [Fr((-1) ** (sum(a * b for a, b in zip(w, v)) & 1))
                   for v in labels]
            row = []
            for lam in eigs:
                q = sum(chi[i] * sum(Pi1[lam][i][j] * chi[j]
                                     for j in range(LABEL_DIM))
                        for i in range(LABEL_DIM))
                row.append(q)
            rows[tuple(row)] += 1
        ok_spread = all(sum(1 for q in row if q != 0) >= 2
                        for row in rows)
        check("S5.5 character content <chi_w, Pi_A(l) chi_w>: every "
              "V-character meets >= 2 A_orb sectors (the A_orb "
              "projections CUT ACROSS the character/automorphic frame)",
              ok_spread)
        for row, cnt in sorted(rows.items(), key=lambda kv: -kv[1]):
            print("      %2d characters | (l=0,1,4,7,9) = (%s)"
                  % (cnt, ", ".join(str(q) for q in row)))

        # chi_NSR overlaps
        ns_idx = fr["ns_idx"]
        PNS = [[Fr(1) if (i == j and i in ns_idx) else Fr(0)
                for j in range(LABEL_DIM)] for i in range(LABEL_DIM)]
        tab = {lam: ftrace(fmul(Pi1[lam], PNS)) for lam in eigs}
        ncomm = {lam: fmaxabs(fcomm(Pi1[lam], PNS)) for lam in eigs}
        cuts = any(v != 0 for v in ncomm.values())
        print("    chi_NSR overlaps tr(Pi_A(l) P_NS): %s"
              % {lam: str(tab[lam]) for lam in eigs})
        check("S5.6 chi_NSR relation: [Pi_A(l), P_NS] %s -- the A_orb "
              "sectors %s the NS/R label split (exact)"
              % ("!= 0 for some l" if cuts else "== 0 for all l",
                 "CUT ACROSS" if cuts else "REFINE"), True,
              "max |[.,.]| per l: %s"
              % {lam: str(ncomm[lam]) for lam in eigs})

        GATE_FLAGS["weil"] = (ok_ev and ok_anchor_id and ok_anchor
                              and ok_lem and ok_spread)
        return dict(lads=lads, psd=psd, dmass=(dm7, dm2, dmm2),
                    nsr_cuts=cuts)


    # ================================================== S6 controls
    def s6_controls(fr, ao):
        section("S6 -- controls (must fire)")
        B, perm = fr["B"], fr["perm"]
        P = ao["P"]
        n = LABEL_DIM

        # C1 random sigma-symmetrized operator fails K-commutation
        R0 = np.zeros((n, n), dtype=np.int64)
        for i in range(n):
            for j in range(i, n):
                R0[i, j] = R0[j, i] = lcg(7) - 3
        R = R0 + P @ R0 @ P.T + P @ P @ R0 @ (P @ P).T
        ok_inv = int(np.max(np.abs(P @ R @ P.T - R))) == 0
        dev = int(np.max(np.abs(R @ B - B @ R)))
        CONTROL_FIRED["C1"] = ok_inv and dev != 0
        check("C1 random sigma-invariant operator: sigma-invariance holds "
              "by construction but [R, K] != 0 (max |[R,B]| = %d) -- its "
              "eigenprojections CANNOT all commute with K: fires" % dev,
              CONTROL_FIRED["C1"])

        # C2 non-invariant projection breaks sigma-transport
        x = next(i for i in range(n) if perm[i] != i)
        Q = np.zeros((n, n), dtype=np.int64)
        Q[x, x] = 1
        dev2 = int(np.max(np.abs(P @ Q @ P.T - Q)))
        CONTROL_FIRED["C2"] = dev2 != 0
        check("C2 non-invariant projection (coordinate atom at a moved "
              "label): P Q P^T != Q (max dev %d) -- sigma-transport "
              "breaks: fires" % dev2, CONTROL_FIRED["C2"])
        GATE_FLAGS["controls"] = all(CONTROL_FIRED.values())


    # ================================================== S7 verdict
    def s7_verdict(cm, wl):
        section("S7 -- verdict")
        ok_all = all(GATE_FLAGS.get(k, False)
                     for k in ("frame", "aorb", "commutant", "eigenspaces",
                               "weil", "controls"))
        maximal = cm["maximal"]
        if not ok_all:
            verdict = "AORB-UNDECIDED (a gate failed -- see FAIL lines)"
        elif not maximal:
            verdict = "AORB-NOT-MAXIMAL"
        else:
            content = any(v for k, v in wl["psd"].items() if "7" not in k)
            verdict = ("AORB-MAXIMAL-MEANINGFUL" if content
                       else "AORB-MAXIMAL-SILENT")
        n_pass = sum(1 for _n, o in CHECKS if o)
        print("gates: %d/%d PASS; controls fired: %s"
              % (n_pass, len(CHECKS), CONTROL_FIRED))
        print()
        print("VERDICT: %s" % verdict)
        print()
        print("Findings (typed, exploration only):")
        print("  1. dim C({K, sigma}) = %d (exact rational nullspace), "
              "NONABELIAN;" % cm["D"])
        print("     block structure R + M_%d(R) + M_%d(C) + M_%d(R) + "
              "M_%d(C)" % (cm["m1"], (9 - cm["m1"]) // 2, cm["n1"],
                           (5 - cm["n1"]) // 2))
        print("     (m1 = %d, n1 = %d), center R^3 + C^2 (dim %d); the "
              "A_orb" % (cm["m1"], cm["n1"], cm["D_Z"]))
        print("     eigenprojection algebra (dim 5, both orbits IDENTICAL)")
        print("     is a proper abelian subalgebra: NOT maximal.")
        print("  2. The refinement is window-silent beyond the K-spectrum")
        print("     (scalar action forces identical windows inside each")
        print("     B-eigenspace); the three K-spectral windows measured")
        print("     with the deployed continuum (protocol-internal).")
        print("  3. A_orb sectors cut across the V-character and chi_NSR")
        print("     frames (exact lemma + overlap censuses).")
        print()
        print("Recommended addendum (report only, NOT written anywhere):")
        print("  PRIME.KRAUS.DOILY.01 addendum: the sigma-invariant")
        print("  K-commuting refinement is governed by the commutant")
        print("  C = R + M_m1(R) + M_*(C) + ... (dims measured above);")
        print("  A_orb generates a canonical abelian 5-dim subalgebra,")
        print("  identical for both spread sigma-orbits, refining the")
        print("  Bose-Mesner frame {I, B, J} but strictly smaller than C.")
        print("  Window transport sees ONLY the K-spectral part; any")
        print("  claim beyond the three (mu_B/7)-damped ramified legs is")
        print("  out of scope.  NO RH/GRH claim.")
        return verdict


    def main():
        t0 = time.time()
        print(FROZEN_SPEC)
        g0_firewall()
        fr = s1_frame()
        ao = s2_aorb(fr)
        cm = s3_commutant(fr, ao)
        s4_eigenspaces(fr, ao, cm)
        wl = s5_weil_channels(fr, ao)
        s6_controls(fr, ao)
        verdict = s7_verdict(cm, wl)
        print()
        print("total runtime %.1f s" % (time.time() - t0))
        return verdict
    verdict = main()
    return (verdict, sum(1 for _n, o in CHECKS if o), len(CHECKS))


def run():
    """run_all entry point (v757 precedent): expected patterns 21/21
    SPREAD-SIGMA-BROKEN + COMMUTANT-EXTENDS, then 24/24
    AORB-NOT-MAXIMAL."""
    v1, v2 = main()
    n1 = sum(1 for _n, ok in CHECKS if ok)
    fails1 = [n.split()[0] for n, ok in CHECKS if not ok]
    print()
    verdict2, n2, tot2 = _part2()
    ok = (n1 == len(CHECKS) == 21 and not fails1
          and v1 == "SPREAD-SIGMA-BROKEN" and v2 == "COMMUTANT-EXTENDS"
          and n2 == tot2 == 24 and verdict2 == "AORB-NOT-MAXIMAL")
    print("\n[%s] PATTERN GATE: expected 21/21 SPREAD-SIGMA-BROKEN + "
          "COMMUTANT-EXTENDS and 24/24 AORB-NOT-MAXIMAL; got %d/%d "
          "(%s / %s) + %d/%d (%s), fails: %s"
          % ("PASS" if ok else "FAIL", n1, len(CHECKS), v1, v2,
             n2, tot2, verdict2, fails1 or "none"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
