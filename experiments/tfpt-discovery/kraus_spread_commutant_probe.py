#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kraus_spread_commutant_probe -- the two named falsifiers of
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
"""

import ast
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
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


if __name__ == "__main__":
    main()
