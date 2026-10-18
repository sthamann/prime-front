#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v811 -- PRIME.KRAUS.DOILY.01: the 105 Kraus legs as a complete context protocol over the doily W(3,2), one probe (21/21 checks incl. the 3 must-fire controls, ~0.2 s; discovery probe prime_kraus_doily_probe.py, 2026-08-06, verdict KRAUS-DOILY-PROTOCOL; SPEC v2 -- ONE declared run-1 -> run-2 REPORT-TEXT repair carried verbatim: the P4.2 text embedded the prediction that measure and transport legs do NOT commute, the measured commutator is ZERO -- text made conditional, no gate or construction change).  THE ANATOMY: the 105 legs = 15 diagonal + 90 off-diagonal (the sigma-invariant symplectic form is UNIQUE and equals the canonical chart form; B = B^T, rows 7, B B^T = 4I + 3J); the 90 off-diagonal legs DOUBLE-COVER the 45 flags of W(3,2) exactly 2:1 with deck = the arrow-reversal involution.  THE CANONICAL 45 + 60: 45 pair transports = the reversal-quotient (flags), 60 context states = the 15 *-fixed diagonal legs x their 4-ray eigenfibers = the 60 v783 stabilizer rays -- canonical as (reversal-quotient) + (fiber expansion), NOT as a leg-subset partition: the Sp(4,2) obstruction is CERTIFIED (orbits {15, 90} on legs, point stabilizer transitive on the 6 neighbors => no equivariant per-class 3+4 split; the classical 45+60 doily split lives on a DIFFERENT 105-set); the literal partition is spread-relative = the ledger's T3 census (3,1,1,1,1), re-derived.  THE OPERATOR MATCH: the shared-Pauli dictionary == B on all 105 pairs with duality coherence D(P_xy) = {x, y, x+y}; the 45 pair transports are QUADRATIC (products of commuting context Paulis collapse to +-P, signs {36: +1, 9: -1}) and span with 1 the FULL End(C^4) at exact rank 16 -- the two-qubit analogue of v111's 1 + 45 + 210 (count anchor 45 = dim so(10), cited).  COVARIANCES: sigma equivariant on every layer; deck J class- and ray-trivial (its content = the mu4 fiber multiplicity 240 = 60 x 4); KMS sub-channel unitality 1 = 1/7 + 6/7 (rule A) and 1 = 3/7 + 4/7 (rule B) with beta = 1 detailed balance per sub-channel.  THE PROTOCOL: 7K = I + (B - I) with S = (B-I)/6 doubly stochastic and spec(B) = {7, 2^9, (-2)^5} exact; rule B: K = (3/7)E + (4/7)R with E = B45/3 an IDEMPOTENT conditional expectation and R doubly stochastic; THE SURPRISE (measured, report-only): [B45, B60] = 0 EXACTLY -- the conditional expectation lies in the channel commutant, a DIRECT-SUM protocol; measured: the certified spread is NOT sigma-invariant (reported, gates nothing -- selection-rule-relative; the named next falsifier).  Controls fire (scrambled flags 42/45, non-maximal triples 20/20 + fake spread, random splits 0/20).  ROOTCLASS-MIXED (v775) cited; no particle semantics.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe prime_kraus_doily_probe.py (2026-08-06, 21/21, ~0.1 s, KRAUS-DOILY-PROTOCOL; the declared v1 -> v2 report-text repair carried verbatim in the docstring below); re-run identically at promotion.  Promoted verbatim; the v738 machinery import resolves against the verification directory (path swap, v795 precedent); a module-level _LAST verdict capture inserted (v791 precedent); numbers unchanged; run() encodes the pattern (v757 precedent; the probe's main() returns the verdict string, gated directly).

Original prime_kraus_doily_probe.py docstring (verbatim):
prime_kraus_doily_probe -- PRIME.KRAUS.DOILY.01: do the 105 Kraus legs
form a COMPLETE CONTEXT PROTOCOL 105 = 45 pair transports + 60 stabilizer
states over the doily W(3,2)?

THE HYPOTHESIS (task wording): 105 = 15 contexts x (3 commuting pairs +
4 stabilizer states) = 45 + 60, the 45 = quadratic Clifford pair
transports, the 60 = Gaussian stabilizer rays.

THE ACTUAL LEG STRUCTURE (v756/v801, verified first): the legs are the
105 ORDERED incident pairs (x, y) with B[x, y] = 1 (15 labels, row degree
7, INCLUDING the 15 diagonal legs (x, x)); Kraus V_xy = 7^{-1/2}|y><x|.
So 105 = 15 + 90 as a set partition by Sp(4,2)-orbits -- NOT 45 + 60.
The frozen decomposition rules tested here:

RULE A (primary; the decomposition the ALGEBRA ITSELF provides, choice-
free): the arrow-reversal involution * (the algebra's own involution,
v756 "arrow reversal closes the generating set") acts on the legs with
orbit census 15 fixed (diagonal) + 45 free pairs.  The protocol data:
  45 PAIR TRANSPORTS = the 45 reversal-orbits of off-diagonal legs
     = the 45 unordered commuting pairs = the 45 FLAGS of W(3,2) under
     {x,y} -> (x+y, line {x,y,x+y}) (the 90 ordered legs double-cover
     the flags exactly 2:1, deck of the cover = *);
  60 CONTEXT STATES = the 15 *-fixed diagonal legs x their 4-state
     eigenfibers: each class's 4 Gaussian J-lines are the 4 joint
     eigenstates of exactly ONE Pauli context (v783 P6.1), 15 x 4 = 60
     = the 60 stabilizer rays.
  Bookkeeping: 105 = 45*2 + 60/4 (deck-2 on transports, fiber-4 on
  states); 45 + 60 is canonical as (reversal-quotient) + (fiber-
  expansion), NOT as a subset partition of the legs.

RULE B (secondary; the literal 45+60 SUBSET PARTITION): via the
certified spread (lex-first fully isotropic spread of the canonical
form -- the arf/spinor selection rule; ledger T3): legs with both ends
in one spread block (per class: self + 2 partners = 3) = 45; cross-
block legs (per class 4) = 60.  This re-derives the ledger's certified
(3,1,1,1,1) incidence census.  It is spread-RELATIVE: the honest
obstruction, gated exactly, is that Sp(4,2) acts on the legs with
orbits {15, 90} and the point stabilizer is TRANSITIVE on the 6
neighbors, so NO Sp(4,2)-equivariant per-class 3+4 subset split exists;
the classical doily split 105 = 45 + 60 (commuting + anticommuting
UNORDERED pairs, Sp-orbits {45, 60}) lives on a DIFFERENT 105-set.

THE FOUR TESTS (frozen):
 T1 INDEX MAP    D1.1-D1.6: frame + doily census + leg anatomy + flag
                 double cover + the two-105 disambiguation with the
                 exact Sp-obstruction + rule-B spread partition with
                 the ledger (3,1,1,1,1) re-derivation.
 T2 OPERATOR     O2.1-O2.5: chart layer (roots -> classes -> rays ->
    MATCH        stabilizer contexts); the share-a-Pauli dictionary
                 == B on all 105 pairs; duality coherence D(P_xy) ==
                 {x,y,x+y}; the 45 pair transports as QUADRATIC
                 operators (product of the two other context Paulis
                 collapses to +-P, sign census; span with 1 = FULL
                 End(C^4), rank 16 exact -- the two-qubit analogue of
                 v111's "the 45 quadratics generate End(S+)", corpus
                 count anchor 45 = dim so(10), 1+45+210 tower, CITED,
                 no cross-chart dictionary claimed); the 60 = 15 x 4
                 eigen-sign patterns exact.
 T3 COVARIANCE   C3.1-C3.3: sigma (label/leg/flag/ray equivariance of
                 the rule-A data), deck (J class- and ray-trivial; its
                 content = the mu4 fiber multiplicities; the 2:1 flag-
                 cover deck is the * reversal), KMS (uniform half-
                 weights; sub-channel unitality split 1/7 + 6/7 (rule
                 A) and 3/7 + 4/7 (rule B); detailed balance per
                 sub-channel exact).  Rule-B sigma-invariance of the
                 certified spread: MEASURED AND REPORTED, gates
                 nothing (a selection-rule-relative object).
 T4 PROTOCOL     P4.1-P4.3: 7K = I + (B - I), S = (B-I)/6 doubly
                 stochastic, spectra exact via polynomial identities
                 (B: {7, 2^9, (-2)^5}); rule B: K = (3/7)E + (4/7)R
                 with E the idempotent conditional expectation onto
                 the 5 spread contexts and R doubly stochastic;
                 measure-(context)+recover-(transport) reading typed
                 as OPERATOR IDENTITIES ONLY.
 CONTROLS (must fire):
 K5.1 scrambled flag assignment (non-identity Pauli permutation)
      breaks the duality/commutation census;
 K5.2 wrong context partition: non-maximal (anticommuting) triples
      break pairwise commutation 20/20 (no 15x3 flag structure), and
      a fake spread (two labels swapped across blocks) breaks the
      (3,1,1,1,1) census;
 K5.3 random 45/60 leg splits (20 LCG draws) fail the frozen
      canonicity criterion (sigma-invariant AND *-closed AND
      per-class count 3): 0/20 expected to pass.

VERDICT ENUM (frozen):
  KRAUS-DOILY-PROTOCOL : T1 core + T2 + T3 (rule-A covariances) + T4
                         all pass and every control fires.  Typed: the
                         45+60 is canonical as reversal-quotient +
                         state-fiber data; the literal subset partition
                         is spread-relative (= ledger T3).
  KRAUS-DOILY-PARTIAL  : rule-A bookkeeping holds, >= 1 other test
                         fails -> named exactly.
  KRAUS-DOILY-DEAD     : the rule-A bookkeeping itself fails (no
                         canonical 45+60 in any form).

FENCES: exploration only (experiments/tfpt-discovery/); no
verification/, ledger, .tex or website writes; no .md; no commits.
ROOTCLASS-MIXED (v775) cited: register/carrier structure statements
only, no particle semantics.  NO RH claim.  Exact integer / Z[i] /
Fraction arithmetic in every load-bearing gate; floats only as
delta-checks.  Frozen 2026-08-06 before the first run.

SPEC v2 (2026-08-06): ONE declared run-1 -> run-2 REPORT-TEXT repair,
no gate or construction change: the P4.2 check text embedded the
prediction "the measure and transport legs do NOT commute", but the
measured commutator is max|[B45, B60]| = 0 exactly -- they DO commute
(the spread conditional expectation lies in the channel commutant).
The gate never consumed the commutator (predeclared report-only); the
text now reports the measured value conditionally.  Run-1 gate pattern
21/21 PASS is unchanged by the repair.

Sources (read-only): v756 (105-leg Kraus/Stinespring), v801 (CP
intertwiner promotion), v783 (two-qubit chart: contexts, 60 stabilizer
rays, class<->context bijection, MUB spreads), v752 (incidence B),
v738 (Lmodule, roots, sigma), v111 (the 45 quadratics / 1+45+210,
count anchor), hecke_arrow_ledger_probe (T3 spread census),
prime_cp_intertwiner_probe (frame recipe).
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
N_LEGS = 105
BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "zetazero", "lcalc", "mpmath")

CHECKS = []
GATE_FLAGS = {}
_LAST = {}
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


# ============================================================ Z[i] helpers
def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


def gnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def gdiv(a, b):
    n = gnorm(b)
    num = gmul(a, gconj(b))
    assert num[0] % n == 0 and num[1] % n == 0, "not divisible"
    return (num[0] // n, num[1] // n)


def ggcd(a, b):
    while b != (0, 0):
        n = gnorm(b)
        num = gmul(a, gconj(b))
        q = ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))
        a, b = b, gsub(a, gmul(q, b))
    return a


UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
G0 = (0, 0)
G1 = (1, 0)
GI = (0, 1)


def canonical_ray(z):
    """canonical Z[i]-primitive representative of the projective ray
    (v783 recipe): divide by the Z[i]-gcd, unit-normalize the first
    nonzero entry to a > 0, b >= 0."""
    g = G0
    for c in z:
        if c != G0:
            g = c if g == G0 else ggcd(g, c)
    assert g != G0
    w = tuple(gdiv(c, g) for c in z)
    first = next(c for c in w if c != G0)
    for u in UNITS:
        f = gmul(u, first)
        if f[0] > 0 and f[1] >= 0:
            return tuple(gmul(u, c) for c in w)
    raise AssertionError("no canonical unit")


def _sumg(it):
    s = G0
    for x in it:
        s = gadd(s, x)
    return s


def mmulg(A, B):
    n = len(A)
    return tuple(tuple(_sumg(gmul(A[i][k], B[k][j]) for k in range(n))
                       for j in range(n)) for i in range(n))


def mat_apply(A, z):
    n = len(A)
    return tuple(_sumg(gmul(A[i][j], z[j]) for j in range(n))
                 for i in range(n))


def mscale(k, A):
    return tuple(tuple((k * c[0], k * c[1]) for c in row) for row in A)


def meye(n, val=G1):
    return tuple(tuple(val if i == j else G0 for j in range(n))
                 for i in range(n))


def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(gmul(A[i // m][k // m], B[i % m][k % m])
                       for k in range(n * m)) for i in range(n * m))


# =============================================================== S1 frame
def s1_frame_and_doily():
    section("S1 (T1) -- frame, doily W(3,2), leg anatomy, the two 105s, "
            "rule A / rule B")
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

    # unique sigma-invariant symplectic form; == canonical chart form
    pairs4 = list(combinations(range(4), 2))
    inv_forms = []
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
            inv_forms.append(M)
    Omega = inv_forms[0]

    def herm_amb(z, zp):
        s = G0
        for c in range(4):
            s = gadd(s, gmul(z[c], gconj(zp[c])))
        return s

    Bamb = [L.to_ambient(e) for e in E4]
    H = [[herm_amb(Bamb[k], Bamb[l]) for l in range(4)] for k in range(4)]
    ok_div4 = all(H[k][l][0] % 4 == 0 and H[k][l][1] % 4 == 0
                  for k in range(4) for l in range(4))
    Gbar = [[ram.par((H[k][l][0] // 4, H[k][l][1] // 4))
             for l in range(4)] for k in range(4)]
    ok_same = Gbar == Omega

    def om(x, y):
        return (sum(x[j] * Omega[j][k] * y[k]
                    for j in range(4) for k in range(4))) & 1

    B = np.zeros((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    for r, x in enumerate(labels):
        for c, y in enumerate(labels):
            B[r, c] = int(om(x, y) == 0)
    I15 = np.eye(LABEL_DIM, dtype=np.int64)
    J15 = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    legs = [(x, y) for x in range(LABEL_DIM) for y in range(LABEL_DIM)
            if B[x, y]]
    ok_d11 = (len(inv_forms) == 1 and ok_div4 and ok_same
              and np.array_equal(B, B.T)
              and bool(np.all(B.sum(axis=1) == ROW_DEGREE))
              and int(np.max(np.abs(B @ B.T - (4 * I15 + 3 * J15)))) == 0
              and len(legs) == N_LEGS)
    check("D1.1 frame: the sigma-invariant symplectic form is UNIQUE "
          "(n_inv = %d) and EQUALS the canonical chart form par(H/4) "
          "(v752/v783 convention) -- one form, one B; B == B^T, rows 7, "
          "B B^T == 4I + 3J, 105 legs" % len(inv_forms), ok_d11,
          "%.1f s" % (time.time() - t0))

    # D1.2 doily census
    all_lines = set()
    for a, b in combinations(labels, 2):
        c = tuple(p ^ q for p, q in zip(a, b))
        all_lines.add(frozenset({a, b, c}))
    iso_lines = sorted((Lf for Lf in all_lines
                        if all(om(x, y) == 0 for x in Lf for y in Lf)),
                       key=lambda s: sorted(s))
    lines_thru = {v: [Lf for Lf in iso_lines if v in Lf] for v in labels}
    flags = [(p, Lf) for Lf in iso_lines for p in sorted(Lf)]
    ok_d12 = (len(all_lines) == 35 and len(iso_lines) == 15
              and all(len(Lf) == 3 for Lf in iso_lines)
              and all(len(lines_thru[v]) == 3 for v in labels)
              and len(flags) == 45)
    check("D1.2 doily W(3,2): 35 lines, 15 isotropic; 3 points/line, "
          "3 lines/point, 45 flags (= 15 x 3) exact", ok_d12)

    # D1.3 leg anatomy + the * involution
    diag = [(x, y) for (x, y) in legs if x == y]
    off = [(x, y) for (x, y) in legs if x != y]
    star_fixed = [lg for lg in legs if (lg[1], lg[0]) == lg]
    star_pairs = {frozenset({lg, (lg[1], lg[0])}) for lg in off}
    per_class_ok = True
    for xi, x in enumerate(labels):
        inc = [y for y in labels if B[xi, lidx[y]]]
        nb = [y for y in inc if y != x]
        by_line = Counter(frozenset({x, y,
                                     tuple(p ^ q for p, q in zip(x, y))})
                          for y in nb)
        if not (len(inc) == 7 and x in inc and len(nb) == 6
                and len(by_line) == 3
                and all(v == 2 for v in by_line.values())
                and all(Lf in [frozenset(s) for s in lines_thru[x]]
                        for Lf in by_line)):
            per_class_ok = False
    ok_d13 = (len(diag) == 15 and len(off) == 90
              and len(star_fixed) == 15 and len(star_pairs) == 45
              and per_class_ok)
    check("D1.3 leg anatomy: 105 = 15 diagonal + 90 off-diagonal; "
          "*-involution (arrow reversal) orbits = 15 fixed + 45 pairs; "
          "per class 7 = self + 3 lines-through x 2", ok_d13)

    # D1.4 flag double cover
    flag_of = {}
    for (xi, yi) in off:
        x, y = labels[xi], labels[yi]
        z = tuple(p ^ q for p, q in zip(x, y))
        flag_of[(xi, yi)] = (z, frozenset({x, y, z}))
    cover = Counter(flag_of.values())
    ok_d14 = (set(cover) == {(p, frozenset(Lf)) for (p, Lf) in flags}
              and all(v == 2 for v in cover.values())
              and all(flag_of[(a, b)] == flag_of[(b, a)]
                      for (a, b) in off))
    check("D1.4 FLAG DOUBLE COVER: off-diagonal leg (x,y) -> flag "
          "(x+y, line{x,y,x+y}) is onto ALL 45 flags exactly 2:1; the "
          "deck of the cover IS the * reversal (fibers = orientation "
          "pairs)", ok_d14)

    # D1.5 the two 105s + the exact Sp(4,2) obstruction
    perms = set()
    frontier = []
    for v in labels:
        t = tuple(lidx[tuple(w[j] ^ (om(w, v) * v[j]) for j in range(4))]
                  for w in labels)
        if t not in perms:
            perms.add(t)
            frontier.append(t)
    gens = list(frontier)
    while frontier:
        new = []
        for p in frontier:
            for g in gens:
                q = tuple(g[p[i]] for i in range(LABEL_DIM))
                if q not in perms:
                    perms.add(q)
                    new.append(q)
        frontier = new
    leg_orbits = {}
    for lg in legs:
        key = min((p[lg[0]], p[lg[1]]) for p in perms)
        leg_orbits.setdefault(key, []).append(lg)
    pair_orbits = {}
    for a, b in combinations(range(LABEL_DIM), 2):
        key = min(tuple(sorted((p[a], p[b]))) for p in perms)
        pair_orbits.setdefault(key, []).append((a, b))
    stab0 = [p for p in perms if p[0] == 0]
    inc0 = [y for y in range(LABEL_DIM) if B[0, y] and y != 0]
    nb_orbit = set()
    seen = set()
    for y in inc0:
        if y in seen:
            continue
        o = {p[y] for p in stab0}
        seen |= o
        nb_orbit.add(frozenset(o))
    ok_d15 = (len(perms) == 720
              and sorted(len(o) for o in leg_orbits.values()) == [15, 90]
              and sorted(len(o) for o in pair_orbits.values()) == [45, 60]
              and len(nb_orbit) == 1
              and len(next(iter(nb_orbit))) == 6
              and len(stab0) == 48)
    check("D1.5 THE TWO 105s + THE OBSTRUCTION: |Sp(4,2)| = %d; "
          "Sp-orbits on the LEGS = {15, 90}; on the UNORDERED distinct "
          "pairs = {45, 60} (perp + non-perp = the classical doily "
          "split, a DIFFERENT 105-set); point stabilizer (order %d) is "
          "TRANSITIVE on the 6 neighbors => NO Sp-equivariant per-class "
          "3+4 subset split of the legs exists"
          % (len(perms), len(stab0)), ok_d15)

    # D1.6 rule B: the certified spread partition
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
    spread = sorted(spreads[0], key=sorted)
    block_of = {}
    for bi, blk in enumerate(spread):
        for v in blk:
            block_of[v] = bi
    legsB45 = [(x, y) for (x, y) in legs
               if block_of[labels[x]] == block_of[labels[y]]]
    legsB60 = [lg for lg in legs if lg not in set(legsB45)]
    census_ok = True
    for xi, x in enumerate(labels):
        inc = [labels[y] for y in range(LABEL_DIM) if B[xi, y]]
        cs = sorted(Counter(block_of[y] for y in inc).values(),
                    reverse=True)
        own = sum(1 for y in inc if block_of[y] == block_of[x])
        if cs != [3, 1, 1, 1, 1] or own != 3:
            census_ok = False
    sig_spread = {frozenset(sigbar(v) for v in blk) for blk in spread}
    sigma_inv_spread = sig_spread == {frozenset(b) for b in spread}
    ok_d16 = (len(spreads) == 6 and len(legsB45) == 45
              and len(legsB60) == 60 and census_ok
              and all(len({block_of[labels[x]], block_of[labels[y]]}) == 2
                      for (x, y) in legsB60))
    check("D1.6 RULE B (the literal 45+60 partition): %d fully isotropic "
          "spreads (= the 6 MUB pentads, v783); certified spread = "
          "lex-first; same-block legs = %d, cross-block legs = %d; "
          "per-class block census (3,1,1,1,1) with the 3-block = own "
          "block on ALL 15 classes (= the ledger's T3, re-derived); "
          "sigma-invariance of the certified spread: %s (REPORTED, "
          "gates nothing -- selection-rule-relative)"
          % (len(spreads), len(legsB45), len(legsB60), sigma_inv_spread),
          ok_d16)

    GATE_FLAGS["T1_ruleA"] = ok_d11 and ok_d12 and ok_d13 and ok_d14
    GATE_FLAGS["T1_full"] = GATE_FLAGS["T1_ruleA"] and ok_d15 and ok_d16
    return dict(L=L, labels=labels, lidx=lidx, Omega=Omega, om=om, B=B,
                legs=legs, diag=diag, off=off, iso_lines=iso_lines,
                flags=flags, flag_of=flag_of, sigbar=sigbar,
                spread=spread, block_of=block_of, spreads=spreads,
                sigma_inv_spread=sigma_inv_spread, legsB45=legsB45,
                legsB60=legsB60, perms=perms)


# ======================================================== S2 chart layer
def s2_operator_match(fr):
    section("S2 (T2) -- the chart layer: contexts, the dictionary, pair "
            "transports, state fibers")
    t0 = time.time()
    L, labels, lidx = fr["L"], fr["labels"], fr["lidx"]
    roots = ram.roots_E8()
    cls = {w: L.class_of_w(w) for w in roots}
    census = Counter(cls.values())

    def chart(r):
        return tuple((r[2 * k], r[2 * k + 1]) for k in range(4))

    # J-lines and canonical rays
    ray_of_root = {w: canonical_ray(chart(w)) for w in roots}
    rays_of_class = {}
    for w in roots:
        rays_of_class.setdefault(cls[w], set()).add(ray_of_root[w])
    all_rays = sorted(set().union(*rays_of_class.values()))
    mu4_ok = all(
        sum(1 for w in roots if ray_of_root[w] == ray) == 4
        for ray in all_rays)
    ok_o21 = (len(roots) == 240 and len(census) == 15
              and all(v == 16 for v in census.values())
              and len(all_rays) == 60 and mu4_ok
              and all(len(rays_of_class[v]) == 4 for v in labels))
    check("O2.1 roots -> classes -> rays: 240 roots, 15 classes x 16; "
          "60 canonical rays (J-lines), 240 = 60 x 4 mu4 lifts, "
          "4 rays per class", ok_o21, "%.1f s" % (time.time() - t0))

    # 15 two-qubit Paulis (exact Z[i] 4x4) and the stabilizer contexts
    I2 = ((G1, G0), (G0, G1))
    X2 = ((G0, G1), (G1, G0))
    Y2 = ((G0, (0, -1)), ((0, 1), G0))
    Z2 = ((G1, G0), (G0, (-1, 0)))
    W1Q = {(0, 0): I2, (1, 0): X2, (0, 1): Z2, (1, 1): Y2}
    bits_all = [b for b in
                [(i, j, k, l) for i in (0, 1) for j in (0, 1)
                 for k in (0, 1) for l in (0, 1)] if any(b)]
    PMAT = {b: kron(W1Q[(b[0], b[1])], W1Q[(b[2], b[3])])
            for b in bits_all}

    def eig_sign(P, z):
        pz = mat_apply(P, z)
        if pz == z:
            return 1
        if pz == tuple((-c[0], -c[1]) for c in z):
            return -1
        return 0

    ctx_of = {}
    sign_of = {}
    ok_stab = True
    for v in labels:
        rays = sorted(rays_of_class[v])
        stab = []
        for b in bits_all:
            sg = [eig_sign(PMAT[b], z) for z in rays]
            if all(s != 0 for s in sg):
                stab.append(b)
                for z, s in zip(rays, sg):
                    sign_of[(v, z, b)] = s
        if len(stab) != 3:
            ok_stab = False
        ctx_of[v] = frozenset(stab)
    pauli_use = Counter(b for v in labels for b in ctx_of[v])
    ok_closed = True
    for v in labels:
        tri = sorted(ctx_of[v])
        for a, b in combinations(tri, 2):
            c = tuple((p + q) % 2 for p, q in zip(a, b))
            if c not in ctx_of[v]:
                ok_closed = False
    ok_o22 = (ok_stab
              and len({ctx_of[v] for v in labels}) == 15
              and all(pauli_use[b] == 3 for b in bits_all)
              and ok_closed)
    check("O2.2 stabilizer contexts: every class's 4 rays are the joint "
          "eigenbasis of EXACTLY 3 Paulis forming a closed triple "
          "(context); the class -> context map is a bijection; each "
          "Pauli lies in exactly 3 contexts (dual 3-lines-per-point)",
          ok_o22)

    # dual map D: Pauli -> {classes whose context contains it}
    Dmap = {b: frozenset(v for v in labels if b in ctx_of[v])
            for b in bits_all}
    om = fr["om"]
    ok_dual_lines = True
    for b in bits_all:
        tri = sorted(Dmap[b])
        if len(tri) != 3:
            ok_dual_lines = False
            continue
        if not all(om(x, y) == 0 for x in tri for y in tri):
            ok_dual_lines = False
        if tuple(p ^ q for p, q in zip(tri[0], tri[1])) != tri[2] \
                and tuple(p ^ q for p, q in zip(tri[0], tri[1])) \
                not in Dmap[b]:
            ok_dual_lines = False
    B = fr["B"]
    ok_dict = True
    shared = {}
    for x, y in combinations(labels, 2):
        sh = ctx_of[x] & ctx_of[y]
        if (B[lidx[x], lidx[y]] == 1) != (len(sh) > 0):
            ok_dict = False
        if len(sh) > 1:
            ok_dict = False
        if sh:
            shared[frozenset({x, y})] = next(iter(sh))
    ok_coh = all(
        Dmap[shared[frozenset({x, y})]]
        == frozenset({x, y, tuple(p ^ q for p, q in zip(x, y))})
        for x, y in combinations(labels, 2)
        if frozenset({x, y}) in shared)
    ok_o23 = ok_dual_lines and ok_dict and ok_coh and len(shared) == 45
    check("O2.3 THE DICTIONARY (all 105 pairs): B[x,y] = 1 <=> the "
          "contexts share exactly ONE Pauli (v783 P6.3 in THIS frame); "
          "the dual map D(P) = an Omega-isotropic LINE of classes "
          "(bijection Paulis <-> 15 iso lines); DUALITY COHERENCE: "
          "D(P_xy) == {x, y, x+y} on all 45 perpendicular pairs -- the "
          "flag of rule A IS the shared-Pauli datum", ok_o23)

    # O2.4 pair transports as quadratic operators + completeness
    n_prod = 0
    sign_census = Counter()
    ok_quad = True
    for v in labels:
        tri = sorted(ctx_of[v])
        for a, b in combinations(tri, 2):
            c = next(q for q in ctx_of[v] if q not in (a, b))
            prod = mmulg(PMAT[a], PMAT[b])
            hit = None
            for s in (1, -1):
                if prod == mscale(s, PMAT[c]):
                    hit = s
            if hit is None:
                ok_quad = False
            else:
                sign_census[hit] += 1
                n_prod += 1
    # span{1} u {45 pair products} == End(C^4): exact rank 16 over Q
    ops = [meye(4)]
    for key in sorted(shared, key=lambda s: sorted(s)):
        x, _y = sorted(key)
        sh = shared[key]
        oth_x = sorted(b for b in ctx_of[x] if b != sh)
        ops.append(mmulg(PMAT[oth_x[0]], PMAT[oth_x[1]]))
    rows = []
    for Mz in ops:
        row = []
        for i in range(4):
            for j in range(4):
                row += [Fr(Mz[i][j][0]), Fr(Mz[i][j][1])]
        rows.append(row)
    rank = 0
    work = [r[:] for r in rows]
    ncol = 32
    prow = 0
    for col in range(ncol):
        piv = next((r for r in range(prow, len(work)) if work[r][col]),
                   None)
        if piv is None:
            continue
        work[prow], work[piv] = work[piv], work[prow]
        for r in range(len(work)):
            if r != prow and work[r][col]:
                f = work[r][col] / work[prow][col]
                work[r] = [a - f * b for a, b in zip(work[r],
                                                     work[prow])]
        prow += 1
    rank = prow
    ok_o24 = (ok_quad and n_prod == 45
              and sign_census[1] + sign_census[-1] == 45
              and rank == 16)
    check("O2.4 PAIR TRANSPORTS ARE QUADRATIC: all 45 in-context "
          "products of two distinct commuting Paulis collapse to +- the "
          "third Pauli (sign census %s, phases in {+-1} exact); "
          "span{1, 45 transports} = FULL End(C^4), exact rank 16 -- the "
          "two-qubit analogue of v111 (1+45+210: the 45 quadratics "
          "generate End(S+); count anchor 45 = dim so(10), CITED, "
          "count-level only)" % dict(sign_census), ok_o24)

    # O2.5 the 60 states = 15 diagonal legs x 4-sign fibers
    ok_pat = True
    n_states = 0
    for v in labels:
        rays = sorted(rays_of_class[v])
        tri = sorted(ctx_of[v])
        pats = set()
        for z in rays:
            pat = tuple(sign_of[(v, z, b)] for b in tri)
            pats.add(pat)
            n_states += 1
            a, b, c = tri
            prod = mmulg(PMAT[a], PMAT[b])
            eps = 1 if prod == mscale(1, PMAT[c]) else -1
            if pat[0] * pat[1] != eps * pat[2]:
                ok_pat = False
        if len(pats) != 4:
            ok_pat = False
    ok_o25 = ok_pat and n_states == 60
    check("O2.5 STATE FIBERS: the 15 *-fixed diagonal legs x their "
          "4-ray eigenfibers = 60 (context, state) data exactly; per "
          "class the 4 sign patterns are distinct and satisfy the "
          "context product constraint s_A s_B = eps s_C -- the 60 "
          "stabilizer rays of v783, indexed by the diagonal legs",
          ok_o25)
    GATE_FLAGS["T2"] = ok_o21 and ok_o22 and ok_o23 and ok_o24 and ok_o25
    GATE_FLAGS["T2_ruleA_book"] = ok_o21 and ok_o25
    return dict(roots=roots, cls=cls, rays_of_class=rays_of_class,
                all_rays=all_rays, ray_of_root=ray_of_root, PMAT=PMAT,
                bits_all=bits_all, ctx_of=ctx_of, Dmap=Dmap,
                shared=shared, sign_of=sign_of)


# ======================================================= S3 covariances
def s3_covariance(fr, ch):
    section("S3 (T3) -- sigma / deck / KMS covariance of the rule-A "
            "45+60 data")
    labels, lidx, sigbar = fr["labels"], fr["lidx"], fr["sigbar"]
    B = fr["B"]
    cls, roots = ch["cls"], ch["roots"]
    ctx_of, Dmap = ch["ctx_of"], ch["Dmap"]
    rays_of_class, ray_of_root = ch["rays_of_class"], ch["ray_of_root"]

    # sigma on labels / legs / *-structure
    perm = [lidx[sigbar(v)] for v in labels]
    cyc = Counter()
    seen = set()
    for i in range(LABEL_DIM):
        if i in seen:
            continue
        j, n = i, 0
        while True:
            seen.add(j)
            j = perm[j]
            n += 1
            if j == i:
                break
        cyc[n] += 1
    ok_leg = all(B[perm[x], perm[y]] == B[x, y]
                 for x in range(LABEL_DIM) for y in range(LABEL_DIM))
    ok_star = True   # sigma(x,y) = (sx,sy) commutes with reversal: exact
    ok_flag = all(
        frozenset(sigbar(v) for v in fr["flag_of"][(x, y)][1])
        == fr["flag_of"][(perm[x], perm[y])][1]
        and sigbar(fr["flag_of"][(x, y)][0])
        == fr["flag_of"][(perm[x], perm[y])][0]
        for (x, y) in fr["off"])
    # sigma on contexts and rays (via sig8 root permutation)
    ok_ctx_funct = True
    sig_pauli = {}
    for v in labels:
        sv = sigbar(v)
        img_rays = {canonical_ray(
            tuple((ram.sig8(w)[2 * k], ram.sig8(w)[2 * k + 1])
                  for k in range(4)))
            for w in roots if cls[w] == v}
        if img_rays != rays_of_class[sv]:
            ok_ctx_funct = False
    for b in ch["bits_all"]:
        tgt = frozenset(sigbar(v) for v in Dmap[b])
        hit = [q for q in ch["bits_all"] if Dmap[q] == tgt]
        if len(hit) == 1:
            sig_pauli[b] = hit[0]
        else:
            ok_ctx_funct = False
    ok_ctx_sets = all(
        frozenset(sig_pauli[b] for b in ctx_of[v]) == ctx_of[sigbar(v)]
        for v in labels)
    ok_shared_eq = all(
        sig_pauli[ch["shared"][frozenset({x, y})]]
        == ch["shared"][frozenset({sigbar(x), sigbar(y)})]
        for x, y in combinations(labels, 2)
        if frozenset({x, y}) in ch["shared"])
    ok_c31 = (cyc[1] == 3 and cyc[3] == 4 and ok_leg and ok_star
              and ok_flag and ok_ctx_funct and ok_ctx_sets
              and ok_shared_eq)
    check("C3.1 SIGMA: label cycle census 1^3 3^4; legs, diagonal/off "
          "split, *-orbits, flags (both components), ray fibers, "
          "contexts (Gamma_sig(x) = sigma(Gamma_x) via the dual-line "
          "transport) and shared-Pauli flags ALL sigma-equivariant "
          "exactly", ok_c31)

    # deck J
    ok_jcls = all(cls[ram.J8(w)] == cls[w] for w in roots)
    ok_jray = all(ray_of_root[ram.J8(w)] == ray_of_root[w]
                  for w in roots)
    ok_c32 = ok_jcls and ok_jray
    check("C3.2 DECK: J is class-trivial and ray-trivial (projective) "
          "on all 240 roots -- deck acts as the IDENTITY on the 45+60 "
          "doily data; its content is the mu4 fiber multiplicity "
          "(240 = 60 x 4) and the 2:1 flag-cover deck is the * "
          "reversal, not J", ok_c32)

    # KMS: sub-channel unitality + detailed balance (exact rationals)
    Bm = fr["B"]
    unit_A_diag = all(sum(1 for (x, y) in fr["diag"] if x == c) == 1
                      for c in range(LABEL_DIM))
    w_diag = Fr(1, ROW_DEGREE)
    w_off = Fr(6, ROW_DEGREE)
    ok_unit = w_diag + w_off == 1
    blkB = fr["legsB45"]
    ok_unitB = (all(sum(1 for (x, y) in blkB if x == c) == 3
                    for c in range(LABEL_DIM))
                and Fr(3, 7) + Fr(4, 7) == 1)
    # detailed balance: each sub-incidence is SYMMETRIC => trace-form
    # self-adjoint at beta = 1 with the uniform KMS state (exact)
    Bd = np.eye(LABEL_DIM, dtype=np.int64)
    Bo = Bm - Bd
    B45 = np.zeros_like(Bm)
    for (x, y) in blkB:
        B45[x, y] = 1
    B60 = Bm - B45
    ok_db = (np.array_equal(Bd, Bd.T) and np.array_equal(Bo, Bo.T)
             and np.array_equal(B45, B45.T)
             and np.array_equal(B60, B60.T))
    ok_c33 = unit_A_diag and ok_unit and ok_unitB and ok_db
    check("C3.3 KMS: uniform leg half-weight 7^{-1/2}; sub-channel "
          "unitality split 1 = 1/7 + 6/7 (rule A) and 1 = 3/7 + 4/7 "
          "(rule B) exact; every sub-incidence symmetric => beta = 1 "
          "detailed balance holds PER SUB-CHANNEL (v756 trace form)",
          ok_c33)
    GATE_FLAGS["T3"] = ok_c31 and ok_c32 and ok_c33
    return dict(sig_pauli=sig_pauli, perm=perm, B45=B45, B60=B60)


# ========================================================== S4 protocol
def s4_protocol(fr, cov):
    section("S4 (T4) -- the protocol channel decompositions, exact")
    Bm = fr["B"]
    I = np.eye(LABEL_DIM, dtype=np.int64)
    Jm = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)

    # rule A: 7K = I + (B - I), S = (B-I)/6 doubly stochastic
    Bo = Bm - I
    ok_ds = (bool(np.all(Bo.sum(axis=0) == 6))
             and bool(np.all(Bo.sum(axis=1) == 6)))
    ok_specB = (np.array_equal(Bm @ Bm, 4 * I + 3 * Jm)
                and int(np.trace(Bm)) == 15)
    # (B - 7I)(B - 2I)(B + 2I) == 0 and multiplicities from traces
    ok_min = np.array_equal(
        (Bm - 7 * I) @ (Bm - 2 * I) @ (Bm + 2 * I),
        np.zeros_like(Bm))
    # tr B = 7 + 2a - 2b, a + b = 14 -> a = 9, b = 5
    ok_mult = (7 + 2 * 9 - 2 * 5 == 15)
    # (B - I)^2 = B^2 - 2B + I = (4I + 3J) - 2B + I = 5I + 3J - 2B
    ok_s2 = np.array_equal(Bo @ Bo, 5 * I + 3 * Jm - 2 * Bm)
    ok_p41 = ok_ds and ok_specB and ok_min and ok_mult and ok_s2
    check("P4.1 RULE A CHANNEL: 7K = I + (B - I); transport S = (B-I)/6 "
          "doubly stochastic; spectrum of B = {7, 2^9, (-2)^5} exact "
          "((B-7I)(B-2I)(B+2I) = 0, trace 15); 36 S^2 = 5I + 3J - 2B "
          "exact integer -- the K^2 = (4/49)I + (45/49)Pi anchor "
          "re-derived", ok_p41)

    # rule B: K = (3/7) E + (4/7) R
    B45, B60 = cov["B45"], cov["B60"]
    E3 = B45  # blockdiag(J3)
    ok_blk = np.array_equal(E3 @ E3, 3 * E3)
    ok_R = (bool(np.all(B60.sum(axis=0) == 4))
            and bool(np.all(B60.sum(axis=1) == 4)))
    comm = E3 @ B60 - B60 @ E3
    comm_norm = int(np.max(np.abs(comm)))
    ok_spec45 = np.array_equal((B45 - 3 * I) @ B45, np.zeros_like(B45))
    ok_p42 = ok_blk and ok_R and ok_spec45
    comm_txt = ("ZERO: the conditional expectation lies in the channel "
                "COMMUTANT -- measure and transport are simultaneously "
                "block-diagonalizable (a direct-sum protocol)"
                if comm_norm == 0 else
                "NONZERO: a genuine two-step protocol, not a direct sum")
    check("P4.2 RULE B CHANNEL: K = (3/7)E + (4/7)R with E = B45/3 the "
          "IDEMPOTENT conditional expectation onto the 5 spread "
          "contexts (B45^2 = 3 B45 exact, spectrum {3^5, 0^10}) and "
          "R = B60/4 doubly stochastic; commutator max|[B45, B60]| = %d "
          "(measured, report-only: %s)" % (comm_norm, comm_txt),
          ok_p42)

    # P4.3 the protocol reading, operator identities only
    K = Bm.astype(float) / 7.0
    Pi = np.ones((LABEL_DIM, LABEL_DIM)) / LABEL_DIM
    dev_k2 = float(np.max(np.abs(K @ K - (4.0 / 49.0 * np.eye(LABEL_DIM)
                                          + 45.0 / 49.0 * Pi))))
    ok_p43 = dev_k2 <= 1.0e-14
    check("P4.3 PROTOCOL READING (typed, operator identities only): "
          "MEASURE = the *-fixed diagonal legs (rule A: (1/7) id; rule "
          "B: (3/7) x conditional expectation onto the 5 spread "
          "contexts = a measurement channel), RECOVER = the doubly "
          "stochastic cross transport ((6/7) S resp. (4/7) R); "
          "composition K^2 = (4/49)I + (45/49)Pi to %.1e (v756 E0.2) "
          "-- no semantics beyond these identities" % dev_k2, ok_p43)
    GATE_FLAGS["T4"] = ok_p41 and ok_p42 and ok_p43


# ========================================================== S5 controls
def s5_controls(fr, ch, cov):
    section("S5 -- controls (all must fire)")
    labels = fr["labels"]
    bits_all, Dmap = ch["bits_all"], ch["Dmap"]
    shared, ctx_of = ch["shared"], ch["ctx_of"]

    # K5.1 scrambled flag assignment
    while True:
        pi = sorted(range(len(bits_all)), key=lambda _: lcg(1 << 30))
        if pi != list(range(len(bits_all))):
            break
    pmap = {bits_all[i]: bits_all[pi[i]] for i in range(len(bits_all))}
    n_bad_dual = 0
    n_bad_member = 0
    for key, P in shared.items():
        x, y = sorted(key)
        z = tuple(p ^ q for p, q in zip(x, y))
        Q = pmap[P]
        if Dmap[Q] != frozenset({x, y, z}):
            n_bad_dual += 1
        if not (Q in ctx_of[x] and Q in ctx_of[y]):
            n_bad_member += 1
    fired1 = n_bad_dual >= 1 and n_bad_member >= 1
    CONTROL_FIRED["C1"] = fired1
    check("K5.1 CONTROL scrambled flag assignment (random non-identity "
          "Pauli permutation): duality coherence broken on %d/45 pairs, "
          "shared-membership broken on %d/45 -- fires"
          % (n_bad_dual, n_bad_member), fired1)

    # K5.2 wrong context partition: non-maximal triples + fake spread
    om = fr["om"]
    noniso = [Lf for Lf in
              {frozenset({a, b, tuple(p ^ q for p, q in zip(a, b))})
               for a, b in combinations(labels, 2)}
              if not all(om(x, y) == 0 for x in Lf for y in Lf)]
    PMAT = ch["PMAT"]

    def commute(a, b):
        return mmulg(PMAT[a], PMAT[b]) == mmulg(PMAT[b], PMAT[a])

    # transport a label triple to Paulis via the dual bijection:
    # the triple is NOT an iso line, so it is NOT D(P) for any P;
    # test the Pauli-side analogue directly on non-isotropic bit triples
    def symp_bits(a, b):
        return (a[0] * b[1] + a[1] * b[0] + a[2] * b[3]
                + a[3] * b[2]) % 2

    bad_triples = 0
    n_noniso_bits = 0
    seen_tri = set()
    for a, b in combinations(bits_all, 2):
        if symp_bits(a, b) == 1:
            c = tuple((p + q) % 2 for p, q in zip(a, b))
            tri = frozenset({a, b, c})
            if tri in seen_tri:
                continue
            seen_tri.add(tri)
            n_noniso_bits += 1
            if not (commute(a, b) and commute(a, c) and commute(b, c)):
                bad_triples += 1
    # fake spread: swap two labels across the first two blocks
    spread = [sorted(blk) for blk in fr["spread"]]
    fake = [list(map(tuple, blk)) for blk in spread]
    fake[0][0], fake[1][0] = fake[1][0], fake[0][0]
    fblock = {}
    for bi, blk in enumerate(fake):
        for v in blk:
            fblock[v] = bi
    B = fr["B"]
    lidx = fr["lidx"]
    viol = 0
    for x in labels:
        inc = [y for y in labels if B[lidx[x], lidx[y]]]
        own = sum(1 for y in inc if fblock[y] == fblock[x])
        cs = sorted(Counter(fblock[y] for y in inc).values(),
                    reverse=True)
        if cs != [3, 1, 1, 1, 1] or own != 3:
            viol += 1
    fired2 = (len(noniso) == 20 and n_noniso_bits == 20
              and bad_triples == 20 and viol >= 1)
    CONTROL_FIRED["C2"] = fired2
    check("K5.2 CONTROL wrong context partition: all %d non-isotropic "
          "label triples exist and all %d non-isotropic Pauli triples "
          "FAIL pairwise commutation (no 15 x 3 flag structure from "
          "non-maximal triples); fake spread (one cross-block swap) "
          "breaks the (3,1,1,1,1) census on %d/15 classes -- fires"
          % (len(noniso), bad_triples, viol), fired2)

    # K5.3 random 45/60 leg splits
    legs = fr["legs"]
    perm = cov["perm"]
    n_pass = 0
    for _ in range(20):
        idx = sorted(range(N_LEGS), key=lambda _: lcg(1 << 30))[:45]
        sub = {legs[i] for i in idx}
        ok_sig = all((perm[x], perm[y]) in sub for (x, y) in sub)
        ok_rev = all((y, x) in sub for (x, y) in sub)
        ok_cls = all(sum(1 for (x, y) in sub if x == c) == 3
                     for c in range(LABEL_DIM))
        if ok_sig and ok_rev and ok_cls:
            n_pass += 1
    fired3 = n_pass == 0
    CONTROL_FIRED["C3"] = fired3
    check("K5.3 CONTROL random 45/60 splits: %d/20 LCG draws pass the "
          "frozen canonicity criterion (sigma-invariant AND *-closed "
          "AND per-class count 3) -- fires (0 expected)" % n_pass,
          fired3)


# =========================================================== S6 verdict
def s6_verdict(fr):
    section("S6 -- verdict (frozen enum)")
    ruleA_book = (GATE_FLAGS.get("T1_ruleA", False)
                  and GATE_FLAGS.get("T2_ruleA_book", False))
    t_all = (GATE_FLAGS.get("T1_full", False)
             and GATE_FLAGS.get("T2", False)
             and GATE_FLAGS.get("T3", False)
             and GATE_FLAGS.get("T4", False))
    controls = all(CONTROL_FIRED.get(k, False)
                   for k in ("C1", "C2", "C3"))
    if t_all and controls:
        verdict = "KRAUS-DOILY-PROTOCOL"
        note = ("the 45+60 decomposition is CANONICAL as "
                "(reversal-quotient pair transports) + (diagonal-leg "
                "state fibers), operator-matched and sigma/deck/KMS-"
                "covariant; the literal SUBSET PARTITION of the legs "
                "is spread-relative (= ledger T3; Sp-obstruction "
                "certified in D1.5); certified-spread sigma-invariance "
                "measured: %s" % fr["sigma_inv_spread"])
    elif ruleA_book:
        failed = [k for k in ("T1_full", "T2", "T3", "T4")
                  if not GATE_FLAGS.get(k, False)]
        failed += ["controls"] if not controls else []
        verdict = "KRAUS-DOILY-PARTIAL"
        note = "failing: %s" % ", ".join(failed)
    else:
        verdict = "KRAUS-DOILY-DEAD"
        note = "the rule-A bookkeeping itself fails"
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print()
    print("checks: %d/%d pass" % (n_pass, len(CHECKS)))
    for k in sorted(GATE_FLAGS):
        print("  gate %-16s %s" % (k, GATE_FLAGS[k]))
    for k in sorted(CONTROL_FIRED):
        print("  control %-13s %s" % (k, CONTROL_FIRED[k]))
    print()
    print("VERDICT: %s" % verdict)
    print("  " + note)
    return verdict, n_pass


def main():
    t0 = time.time()
    print("PRIME.KRAUS.DOILY.01 -- the 105 Kraus legs as a context "
          "protocol over W(3,2)")
    print("frozen 2026-08-06; exploration only; no RH claim; "
          "ROOTCLASS-MIXED cited")
    g0_firewall()
    fr = s1_frame_and_doily()
    ch = s2_operator_match(fr)
    cov = s3_covariance(fr, ch)
    s4_protocol(fr, cov)
    s5_controls(fr, ch, cov)
    verdict, n_pass = s6_verdict(fr)
    _LAST["verdict"] = verdict
    print("total %.1f s" % (time.time() - t0))
    return verdict


def run():
    """run_all entry point (v757 precedent): expected pattern 21/21 with
    verdict KRAUS-DOILY-PROTOCOL."""
    verdict = main()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    fails = [n for n, ok in CHECKS if not ok]
    ok = (n_pass == len(CHECKS) == 21 and not fails
          and verdict == "KRAUS-DOILY-PROTOCOL")
    print("\n[%s] PATTERN GATE: expected 21/21 with verdict "
          "KRAUS-DOILY-PROTOCOL; got %d/%d, fails: %s, verdict: %s"
          % ("PASS" if ok else "FAIL", n_pass, len(CHECKS),
             fails or "none", verdict))
    print("\nCOMBINED ADJUDICATION: %s -- KRAUS-DOILY-PROTOCOL: the "
          "105 Kraus legs are 15 diagonal + 90 off-diagonal, the "
          "canonical 45 + 60 = (reversal-quotient flag transports) + "
          "(diagonal-leg state fibers = the 60 stabilizer rays), "
          "operator-matched (45 quadratic transports spanning End(C^4) "
          "at rank 16) and sigma/deck/KMS-covariant; the Sp(4,2) "
          "obstruction certifies that no leg-subset partition exists "
          "-- the literal split is spread-relative (= ledger T3); "
          "measured surprises: [B45, B60] = 0 exactly (K = (3/7)E + "
          "(4/7)R is a direct-sum protocol with E a conditional "
          "expectation) and the certified spread is NOT sigma-"
          "invariant (the named next falsifier).  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
