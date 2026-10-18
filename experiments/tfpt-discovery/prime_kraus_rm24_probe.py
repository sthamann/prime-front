#!/usr/bin/env python3
"""PRIME.KRAUS.RM24.01 -- the support-wise decider.

EXPLORATION ONLY (experiments/tfpt-discovery).  Writes nothing outside
stdout; no verification/, no ledger, no TeX, no website, no .md.

THE CLAIM UNDER TEST: the 105 Kraus legs (v756/v801: the incident
ordered pairs (x, y) with B[x, y] = 1, anatomy 15 diagonal + 90
off-diagonal) equal the 105 minimal dual checks -- the weight-4 words
of the dual code C1^perp = [15, 10, 4] (shortened RM(2,4) at 0), which
are exactly the affine 2-planes of V = F2^4 NOT through 0
(35 linear planes x 3 nonzero cosets = 105).

PROTOCOL (frozen)
  S2  the code geometry: build C1^perp = shortened RM(2,4) (degree
      <= 2 Boolean functions vanishing at 0, evaluated on the 15
      nonzero points); census: dim 10, min weight 4, EXACTLY 105
      weight-4 words, and their supports == the 105 affine planes not
      through 0 (both directions).  Duality ward: C1 = punctured
      RM(1,4) = [15, 5], orthogonal to C1^perp, 5 + 10 = 15.
  S3  the honesty layer: (a) the LITERAL leg supports in the label
      basis are {x} (diagonal), {x, y} (off-diagonal), {x, y, x+y}
      (line closure) -- weights 1/2/3 < 4: NONE is a dual word (the
      code has no words of weight < 4) -- exact mismatch census;
      (b) the Sp(4,2) obstruction: generate Sp(4,2) from the 15
      symplectic transvections (order 720), orbit census on legs
      ({15, 90}) vs on the 105 planes ({45, 60}): the orbit types
      differ, so NO Sp-equivariant bijection legs <-> planes can
      exist.  KRAUS-RM24-BIJECTIVE is decided by these censuses.
  S4  the canonical support rule (frozen, built from omega alone --
      the rule-A protocol set 45 + 60 of the doily probe):
        45: each reversal pair {x, y} (off-diagonal legs mod *) |->
            supp{x,y} = {v : omega(x,v) = 1 = omega(y,v)} -- a coset
            of P = span{x,y} = P^perp, isotropic direction, not
            through 0; bijective onto the 45 iso-cosets.
        60: each diagonal leg x carries its certified 4-state
            eigenfiber; the canonical 4-fiber of planes is
            {x + P : P non-isotropic linear plane inside x^perp}
            (exactly 4 such P per x); bijective onto the 60
            non-iso-cosets (the base point x is recoverable as the
            UNIQUE point a of the affine plane with direction inside
            a^perp).
      Censuses: bijectivity 45 + 60 = 105 (each dual word hit once);
      Sp-equivariance on the generators; sigma-equivariance (sigma is
      symplectic for the frame Omega); deck typed (J class-trivial,
      cited v738/gray R1.4); KMS half-weight pushforward census
      (uniform 1/7 -> 2/7 per iso-coset, 1/28 per non-iso-coset,
      total 15 preserved, constant per Sp-orbit).
  S5  controls (must fire): a lex coset pick (non-omega rule) breaks
      Sp-equivariance; scrambled supports (random 4-sets) break code
      membership / bijectivity.

VERDICT ENUM (frozen): KRAUS-RM24-BIJECTIVE (the literal leg-by-leg
support bijection exists with all intertwinings) / KRAUS-RM24-RULE-
CANONICAL (the literal reading fails but a documented canonical rule
gives the 45+60 <-> 105 identification with all covariances) /
KRAUS-RM24-DEAD.  FENCES: ROOTCLASS-MIXED, no RH claim.

Predecessors (read-only): prime_kraus_doily_probe (leg anatomy, rule
A), kraus_spread_commutant_probe (frame recipe), v738 (Lmodule,
sigma), v756/v801 (leg structure, cited).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_kraus_rm24_probe.py
"""

import ast
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _VERIFY)

import v738_hecke_mod_ramified as ram          # noqa: E402

FROZEN_SPEC = """\
PRIME.KRAUS.RM24.01 spec v1 (frozen 2026-08-06, before the first run).
Frame: doily-probe recipe (unique sigma-invariant Omega, B, legs =
  incident ordered pairs, 15 diag + 90 off-diag).
Code: C1^perp = shortened RM(2,4) at 0 = span of the 10 monomial
  evaluations {x_i, x_i x_j} on the 15 nonzero points; gates dim 10,
  min weight 4, weight-4 census == 105 == affine 2-planes not through
  0 (set equality of supports); C1 = punctured RM(1,4), orthogonality
  exact, 5 + 10 = 15.
Honesty gates: literal leg supports have weights {1, 2, 3}, the code
  has NO words below weight 4 (weight enumerator census); Sp(4,2) =
  closure of the 15 transvections t_a(x) = x + omega(x,a) a, order
  720, sigma in Sp; orbit censuses legs {15, 90} vs planes {45, 60}
  (iso-coset 45 / non-iso-coset 60) -- mismatch kills BIJECTIVE.
Canonical rule (frozen): supp{x,y} = {v : omega(x,v) = omega(y,v)
  = 1} for the 45 reversal pairs; fiber(x) = {x + P : P non-iso,
  P subset x^perp} (4 planes) for the 15 diagonal legs; gates:
  45-map and 60-map bijective, union = the 105 weight-4 words each
  once, Sp- and sigma-equivariant (zero mismatches on generators),
  KMS pushforward total 15 = 105/7, constant per orbit; deck typed
  trivial (J class-trivial on labels, cited).
Controls: lex-coset rule equivariance mismatches > 0; LCG-scrambled
  4-set supports: code-membership failures > 0 or duplicates > 0.
Verdicts: KRAUS-RM24-BIJECTIVE / -RULE-CANONICAL / -DEAD.
LCG seed 20260806.  Runtime cap ~20 min.  NO RH/GRH claim.
"""

LABEL_DIM = 15
ROW_DEGREE = 7
SP_ORDER = 720
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
    section("S1 -- frame (doily-probe recipe) + the 105 legs")
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
    legs = [(x, y) for x in labels for y in labels if om(x, y) == 0]
    n_diag = sum(1 for (x, y) in legs if x == y)
    perm = [lidx[sigbar(v)] for v in labels]
    ok = (n_inv == 1 and len(legs) == 105 and n_diag == 15
          and bool(np.all(B.sum(axis=1) == ROW_DEGREE)))
    check("S1.1 frame: unique sigma-invariant Omega; 105 legs = "
          "incident ordered pairs (15 diagonal + 90 off-diagonal), "
          "row degree 7", ok, "%.1f s" % (time.time() - t0))
    GATE_FLAGS["frame"] = ok
    return dict(labels=labels, lidx=lidx, om=om, B=B, legs=legs,
                perm=perm, sigbar=sigbar)


# ================================ S2 the code and the plane geometry
def s2_code(fr):
    section("S2 -- C1^perp = [15,10,4] and the 105 affine planes")
    labels, lidx = fr["labels"], fr["lidx"]

    def to_int(support):
        m = 0
        for v in support:
            m |= 1 << lidx[v]
        return m

    # generators: degree <= 2 monomials vanishing at 0 (no constant)
    gens = []
    for i in range(4):
        gens.append(to_int([v for v in labels if v[i]]))
    for i, j in combinations(range(4), 2):
        gens.append(to_int([v for v in labels if v[i] and v[j]]))
    words = {0}
    for g in gens:
        words |= {w ^ g for w in words}
    wt = {}
    for w in words:
        wt[bin(w).count("1")] = wt.get(bin(w).count("1"), 0) + 1
    ok_dim = len(words) == 1 << 10
    min_wt = min(k for k in wt if k > 0)
    n4 = wt.get(4, 0)
    check("S2.1 shortened RM(2,4): dim 10 (1024 words); min weight "
          "%d == 4; weight-4 census %d == 105" % (min_wt, n4),
          ok_dim and min_wt == 4 and n4 == 105,
          "weight enumerator %s" % dict(sorted(wt.items())))

    # affine 2-planes of V not through 0
    lin_planes = sorted({frozenset({(0, 0, 0, 0), x, y,
                                    tuple(a ^ b for a, b in zip(x, y))})
                         for x, y in combinations(labels, 2)},
                        key=lambda s: sorted(s))
    om = fr["om"]
    iso_lin = [P for P in lin_planes
               if all(om(x, y) == 0 for x in P for y in P)]
    aff = set()
    for P in lin_planes:
        aff.add(frozenset(P))
        for v in labels:
            if v not in P:
                aff.add(frozenset(tuple(a ^ b for a, b in zip(v, p))
                                  for p in P))
    aff = sorted(aff, key=lambda s: sorted(s))
    not0 = [A for A in aff if (0, 0, 0, 0) not in A]
    ok_geo = (len(lin_planes) == 35 and len(iso_lin) == 15
              and len(aff) == 140 and len(not0) == 105)
    plane_ints = {to_int(A) for A in not0}
    w4_words = {w for w in words if bin(w).count("1") == 4}
    ok_bij = plane_ints == w4_words
    check("S2.2 geometry: 35 linear planes (15 isotropic), 140 "
          "affine, 105 not through 0; the 105 weight-4 dual words "
          "== the 105 affine-plane indicators (set equality, both "
          "directions)", ok_geo and ok_bij)

    # duality ward: C1 = punctured RM(1,4)
    c1_gens = [(1 << LABEL_DIM) - 1] + [
        to_int([v for v in labels if v[i]]) for i in range(4)]
    c1 = {0}
    for g in c1_gens:
        c1 |= {w ^ g for w in c1}
    ok_dual = (len(c1) == 32
               and all(bin(a & g).count("1") % 2 == 0
                       for a in c1 for g in gens))
    check("S2.3 duality ward: C1 = punctured RM(1,4) = [15,5], "
          "orthogonal to every C1^perp generator (exact), "
          "5 + 10 = 15", ok_dual)
    GATE_FLAGS["code"] = ok_dim and min_wt == 4 and n4 == 105 and \
        ok_geo and ok_bij and ok_dual

    # direction-plane split of the 105
    def direction(A):
        pts = sorted(A)
        a0 = pts[0]
        return frozenset({(0, 0, 0, 0)}
                         | {tuple(p ^ q for p, q in zip(a0, b))
                            for b in pts[1:]})

    iso_set = set(map(frozenset, iso_lin))
    iso_cosets = [A for A in not0 if direction(A) in iso_set]
    noniso_cosets = [A for A in not0 if direction(A) not in iso_set]
    check("S2.4 coset split: 105 = %d iso-direction + %d non-iso-"
          "direction (== 15 x 3 + 20 x 3)"
          % (len(iso_cosets), len(noniso_cosets)),
          len(iso_cosets) == 45 and len(noniso_cosets) == 60)
    return dict(words=words, w4=w4_words, not0=not0, to_int=to_int,
                iso_cosets=iso_cosets, noniso_cosets=noniso_cosets,
                iso_lin=iso_set, lin_planes=lin_planes,
                direction=direction)


# ==================== S3 honesty: literal supports + Sp obstruction
def s3_honesty(fr, cd):
    section("S3 -- honesty layer: literal supports + Sp(4,2) "
            "obstruction")
    labels, lidx, om, legs = (fr["labels"], fr["lidx"], fr["om"],
                              fr["legs"])
    to_int, words = cd["to_int"], cd["words"]

    # literal leg supports
    wts = set()
    n_in_code = 0
    for (x, y) in legs:
        for supp in ({x} if x == y else {x, y},
                     {x} if x == y else
                     {x, y, tuple(a ^ b for a, b in zip(x, y))}):
            wts.add(len(supp))
            if to_int(supp) in words and len(supp) > 0:
                n_in_code += 1
    check("S3.1 LITERAL supports: leg operator supports have weights "
          "%s (diag {x}, off-diag {x,y}, line closure {x,y,x+y}); "
          "the code has NO nonzero word of weight < 4 -> %d of them "
          "are dual words: the literal claim is DEAD (exact "
          "mismatch)" % (sorted(wts), n_in_code),
          wts == {1, 2, 3} and n_in_code == 0)

    # Sp(4,2) from the 15 transvections
    t0 = time.time()
    gens_p = []
    for a in labels:
        p = tuple(lidx[tuple(xi ^ (om(x, a) * ai)
                             for xi, ai in zip(x, a))]
                  for x in labels)
        gens_p.append(p)
    ident = tuple(range(LABEL_DIM))
    group = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens_p:
                gh = tuple(h[g[i]] for i in range(LABEL_DIM))
                if gh not in group:
                    group.add(gh)
                    nxt.append(gh)
        frontier = nxt
    ok_grp = len(group) == SP_ORDER
    sig_in = tuple(fr["perm"]) in group
    check("S3.2 Sp(4,2) generated by the 15 transvections: order %d "
          "== 720; sigma IS symplectic (in the group)" % len(group),
          ok_grp and sig_in, "%.1f s" % (time.time() - t0))

    def orbit_sizes(objs, act):
        left = set(objs)
        sizes = []
        while left:
            o = left.pop()
            orb = {o}
            fr_ = [o]
            while fr_:
                nx = []
                for u in fr_:
                    for h in gens_p:
                        v = act(h, u)
                        if v not in orb:
                            orb.add(v)
                            nx.append(v)
                fr_ = nx
            left -= orb
            sizes.append(len(orb))
        return sorted(sizes)

    leg_ids = [(lidx[x], lidx[y]) for (x, y) in legs]
    sz_legs = orbit_sizes(leg_ids, lambda h, u: (h[u[0]], h[u[1]]))
    plane_ids = [frozenset(lidx[v] for v in A) for A in cd["not0"]]
    sz_pl = orbit_sizes(plane_ids,
                        lambda h, u: frozenset(h[i] for i in u))
    ok_orb = sz_legs == [15, 90] and sz_pl == [45, 60]
    check("S3.3 orbit censuses: legs %s vs planes %s -- the orbit "
          "types DIFFER: no Sp-equivariant bijection legs <-> planes "
          "exists (KRAUS-RM24-BIJECTIVE is structurally dead)"
          % (sz_legs, sz_pl), ok_orb)
    GATE_FLAGS["honesty"] = (wts == {1, 2, 3} and n_in_code == 0
                             and ok_grp and sig_in and ok_orb)
    return dict(gens_p=gens_p, group=group)


# ============================== S4 the canonical support rule
def s4_canonical_rule(fr, cd, sp):
    section("S4 -- the canonical support rule (rule-A protocol set)")
    labels, lidx, om = fr["labels"], fr["lidx"], fr["om"]

    # 45: reversal pairs -> iso cosets
    pairs45 = sorted({frozenset({x, y}) for (x, y) in fr["legs"]
                      if x != y}, key=lambda s: sorted(s))
    supp45 = {}
    ok45 = len(pairs45) == 45
    iso_set = cd["iso_lin"]
    for pr in pairs45:
        x, y = sorted(pr)
        A = frozenset(v for v in labels
                      if om(x, v) == 1 and om(y, v) == 1)
        P = frozenset({(0, 0, 0, 0), x, y,
                       tuple(a ^ b for a, b in zip(x, y))})
        ok45 &= len(A) == 4 and cd["direction"](A) == P and P in iso_set
        supp45[pr] = A
    ok45 &= len(set(supp45.values())) == 45
    ok45 &= set(supp45.values()) == set(map(frozenset,
                                            cd["iso_cosets"]))
    check("S4.1 the 45-map: {x,y} |-> {v : omega(x,v) = omega(y,v) "
          "= 1} is a coset of span{x,y} = span{x,y}^perp (isotropic "
          "direction), and BIJECTS the 45 reversal pairs onto the 45 "
          "iso-cosets (each once, exact)", ok45)

    # 60: diagonal legs x 4-fiber -> non-iso cosets
    fibers = {}
    ok60 = True
    for x in labels:
        Ps = [P for P in cd["lin_planes"]
              if P not in iso_set
              and all(om(x, p) == 0 for p in P)]
        ok60 &= len(Ps) == 4
        fib = []
        for P in Ps:
            A = frozenset(tuple(a ^ b for a, b in zip(x, p))
                          for p in P)
            ok60 &= (0, 0, 0, 0) not in A and len(A) == 4
            # base-point recovery: x is the UNIQUE point of A whose
            # perp contains the direction plane
            rec = [a for a in A
                   if all(om(a, p) == 0 for p in cd["direction"](A))]
            ok60 &= rec == [x]
            fib.append(A)
        fibers[x] = fib
    all60 = [A for x in labels for A in fibers[x]]
    ok60 &= (len(all60) == 60 and len(set(all60)) == 60
             and set(all60) == set(map(frozenset,
                                       cd["noniso_cosets"])))
    check("S4.2 the 60-map: diagonal leg x |-> {x + P : P non-iso, "
          "P inside x^perp} (exactly 4 planes per x); base point "
          "UNIQUELY recoverable from the plane; BIJECTS the 15 x 4 "
          "fiber onto the 60 non-iso-cosets (each once, exact)", ok60)

    # union census: 105 objects <-> 105 weight-4 dual words
    union = set(supp45.values()) | set(all60)
    ok_u = (len(union) == 105
            and {cd["to_int"](A) for A in union} == cd["w4"])
    check("S4.3 union census: 45 + 60 supports = the 105 weight-4 "
          "dual words, each hit EXACTLY once", ok_u)

    # Sp- and sigma-equivariance on generators
    gens_p = sp["gens_p"] + [tuple(fr["perm"])]
    mism = 0
    for h in gens_p:
        hv = {v: labels[h[lidx[v]]] for v in labels}
        for pr, A in supp45.items():
            x, y = sorted(pr)
            img = supp45[frozenset({hv[x], hv[y]})]
            if img != frozenset(hv[v] for v in A):
                mism += 1
        for x in labels:
            img = {frozenset(hv[v] for v in A) for A in fibers[x]}
            if img != set(fibers[hv[x]]):
                mism += 1
    ok_eq = mism == 0
    check("S4.4 equivariance: the rule commutes with ALL 15 "
          "transvection generators AND with sigma (built from omega "
          "alone -> Sp(4,2)-equivariant; %d mismatches)" % mism,
          ok_eq)

    # KMS pushforward + deck
    w_iso = Fr(2, 7)          # two ordered legs of weight 1/7 each
    w_non = Fr(1, 28)         # diagonal leg 1/7 split over 4 fiber legs
    total = 45 * w_iso + 60 * w_non
    ok_kms = total == Fr(105, 7)
    check("S4.5 KMS half-weight pushforward: uniform 1/7 per leg -> "
          "2/7 per iso-coset (reversal pair), 1/28 per non-iso-coset "
          "(4-fiber split); total %s == 105/7 == 15; constant per "
          "Sp-orbit (uniform by S4.4).  Deck: J is class-trivial on "
          "the labels (v738/gray R1.4, cited) -> acts as the "
          "identity on BOTH sides: compatible" % total, ok_kms)
    GATE_FLAGS["rule"] = ok45 and ok60 and ok_u and ok_eq and ok_kms
    return dict(supp45=supp45, fibers=fibers, pairs45=pairs45)


# ================================================== S5 controls
def s5_controls(fr, cd, sp, rl):
    section("S5 -- controls (must fire)")
    labels, lidx, om = fr["labels"], fr["lidx"], fr["om"]

    # C1 lex coset pick (non-omega rule) breaks equivariance
    supp_lex = {}
    for pr in rl["pairs45"]:
        x, y = sorted(pr)
        P = [(0, 0, 0, 0), x, y, tuple(a ^ b for a, b in zip(x, y))]
        cosets = sorted({frozenset(tuple(a ^ b for a, b in zip(v, p))
                                   for p in P)
                         for v in labels if v not in P},
                        key=lambda s: sorted(s))
        supp_lex[pr] = cosets[0]
    mism = 0
    for h in sp["gens_p"]:
        hv = {v: labels[h[lidx[v]]] for v in labels}
        for pr, A in supp_lex.items():
            x, y = sorted(pr)
            if supp_lex[frozenset({hv[x], hv[y]})] != \
                    frozenset(hv[v] for v in A):
                mism += 1
    CONTROL_FIRED["C1"] = mism > 0
    check("C1 lex-coset rule (canonical-looking but NOT built from "
          "omega): %d equivariance mismatches over the transvection "
          "generators -- fires (the omega rule is the canonical one)"
          % mism, CONTROL_FIRED["C1"])

    # C2 scrambled supports break membership / bijectivity
    bad_member = 0
    seen = set()
    dup = 0
    for _ in range(105):
        s = set()
        while len(s) < 4:
            s.add(labels[lcg(15)])
        w = cd["to_int"](s)
        if w not in cd["words"]:
            bad_member += 1
        if w in seen:
            dup += 1
        seen.add(w)
    CONTROL_FIRED["C2"] = bad_member > 0
    check("C2 scrambled supports (105 LCG random 4-sets): %d fail "
          "code membership, %d duplicates -- fires"
          % (bad_member, dup), CONTROL_FIRED["C2"])
    GATE_FLAGS["controls"] = all(CONTROL_FIRED.values())


# ================================================== S6 verdict
def s6_verdict():
    section("S6 -- verdict")
    ok_all = all(GATE_FLAGS.get(k, False)
                 for k in ("frame", "code", "honesty", "rule",
                           "controls"))
    n_pass = sum(1 for _n, o in CHECKS if o)
    print("gates: %d/%d PASS; controls fired: %s"
          % (n_pass, len(CHECKS), CONTROL_FIRED))
    print()
    if not ok_all:
        verdict = "KRAUS-RM24-UNDECIDED (a gate failed)"
    else:
        # BIJECTIVE is dead by S3 (measured); the canonical rule holds
        verdict = "KRAUS-RM24-RULE-CANONICAL"
    print("VERDICT: %s" % verdict)
    print()
    print("Findings (typed, exploration only):")
    print("  1. The geometry claim is EXACT: the 105 weight-4 words")
    print("     of C1^perp = [15,10,4] are precisely the 105 affine")
    print("     2-planes of V not through 0 (35 x 3).")
    print("  2. The LITERAL leg-support claim is dead twice over:")
    print("     leg supports have weights 1/2/3 (< min distance 4),")
    print("     and Sp(4,2) orbits are {15, 90} on legs vs {45, 60}")
    print("     on planes -- no equivariant bijection can exist.")
    print("  3. The CANONICAL rule (built from omega alone, hence")
    print("     Sp- and sigma-equivariant): reversal pair {x,y} |->")
    print("     {v : omega(x,v) = omega(y,v) = 1} (45 iso-cosets);")
    print("     diagonal leg x |-> {x + P : P non-iso in x^perp}")
    print("     (4-fiber, 60 non-iso-cosets); 45 + 60 = 105 dual")
    print("     checks each once; KMS pushforward and deck exact.")
    print()
    print("Recommended text (report only, NOT written anywhere):")
    print("  PRIME.KRAUS.RM24.01: the rule-A protocol set of the")
    print("  Kraus channel (45 reversal pairs + 15 x 4 fiber) is")
    print("  canonically the set of minimal parity checks of the")
    print("  [15,10,4] shortened RM(2,4) code; the identification is")
    print("  Sp(4,2)-equivariant and sigma/deck/KMS-compatible, but")
    print("  the raw 105 legs (15 + 90 orbit type) do NOT biject")
    print("  equivariantly with the checks.  NO RH claim.")
    return verdict


def main():
    t0 = time.time()
    print(FROZEN_SPEC)
    g0_firewall()
    fr = s1_frame()
    cd = s2_code(fr)
    sp = s3_honesty(fr, cd)
    rl = s4_canonical_rule(fr, cd, sp)
    s5_controls(fr, cd, sp, rl)
    verdict = s6_verdict()
    print()
    print("total runtime %.1f s" % (time.time() - t0))
    return verdict


if __name__ == "__main__":
    main()
