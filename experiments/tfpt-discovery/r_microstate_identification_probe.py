#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""r_microstate_identification_probe -- HECKE.ARROW_MESSAGE.01 follow-up
(the R-microstate identification): WHAT arrow-level object does R(p)
count?  R = 1, 4, 10, 24, 43, 68 at odd n = 3, 5, 7, 9, 11, 13 is the
sheet-switch packet count of the C2 broadcast factorization (B_n =
16 R(n) arrow-exactly, per V-class switch cell = 256 R(n)); the last
attempt at an orbit realization (type-B Weyl orbit count) FAILED at
p = 7 (13 != 10).  This probe freezes a candidate dictionary, tests it
exactly at all places, and decides the identification -- or types the
honest structural boundary.

CONTEXT (corpus + siblings):
  * R(2m+3) = #{(x, y) in N^8 : m = Sum T_{x_i} + 2 Sum T_{y_j}}
    (triangular numbers; 4 unit modes + 4 double-weight modes) --
    the c2-lift certification, re-derived here from scratch.
  * broadcast probe (BROADCAST-EXACT): tab_n = A_n tab_1 + B_n
    tab_1^{sw}; the switch parity is a CHANNEL decomposition, not a
    pointwise coloring; per-class switch multiplicity = 16 B_n =
    256 R(n).
  * SNF probe: the 8-mode Smith signature (1^4, 2^4) equals the
    ramified inclusion (1+i)L in L -- FINGERPRINT ONLY, no admissible
    isometry.

FROZEN CANDIDATE DICTIONARY (predeclared BEFORE the confirmation runs;
the disclosed pilot at p = 3, 5, 7 selected nothing -- it produced only
kills, all reproduced as gates below; no free search):
  C1 sheet-switch arrow orbits under the deployed symmetry groups.
     Arrow set: the type-B Kneser lines (the only deployed odd-place
     arrow census carrying the switch weight: n_B = A_p B_p / 2).
     Group menu (all deployed): G0 = W(D5) x W(A3); G0 extended by the
     mu4 clock J, by the triality sigma, by the (associate-twisted)
     conjugation conj8; W(E8) (reflection closure); everything
     combined.  The deck does not act on the odd-place registers
     (typed).  Match requirement: counts (1, 4, 10) at p = 3, 5, 7,
     then p = 11 -> 43 (and p = 13 -> 68 if cheap) as discriminators;
     11/13 run ONLY for candidates alive after 3, 5, 7 (predeclared).
  C2 type-B line classes modulo finer invariants: the refined
     (a, deg) marked census (canonicalized: vec4, a = 0 row, sorted
     multiset of a != 0 rows -- rescaling-invariant), classes counted
     over type-B lines.
  C3 Z[i]-cell classes of the switch arrows: tower side -- NO
     pointwise switch arrows exist (odd tower layers are all-keep,
     degree * id on V; the parity is a channel split -- typed, cited);
     Kneser side -- the Z[i]-span dimension of the line (J-stability:
     dim_Fp span(v, Jv) in {1, 2}), <= 2 classes, so it must already
     fail at p = 5 (4 needed) -- measured anyway.
  C4 the 8-mode oscillator reading DIRECTLY: the count identity
     256 R(n) = #{(x, y) in Z^8, ALL coordinates odd :
     Sum x^2 + 2 Sum y^2 = 4n} (the +/- sign lift of the triangular
     system; the diagonal form diag(1^4, 2^4) on its all-odd coset)
     vs the arrow side: per-class switch multiplicity 16 B_n with B_n
     re-derived LIVE from the odd-shell glue censuses.  A GRADED
     (pointwise) arrow realization would need an admissible isometry
     onto the diagonal system -- excluded by the SNF fingerprint
     (re-verified here: minimum-vector counts 16 vs 240 already
     obstruct), so C4 can be at most count-level.

GATES:
  G1 ground truth: R(n) from the triangular system = (1, 4, 10, 24,
     43, 68); the sign-lift identity 256 R(n) = odd-vector count of
     diag(1^4, 2^4) at 4n (convolution + direct enumeration).
  G2 deployed operators: J, sigma, conj8 are integral isometries of
     the coeff lattice (J^4 = sigma^3 = conj^2 = 1); reflection set
     for the W(E8) closure verified as isometries.
  G3 C1 census at p = 3, 5, 7: G0 type-B orbit counts; invariance of
     the type-B set under each extension (counted violations); merged
     class counts.  Kill criteria applied.
  G4 C2 refined-type counts at p = 3, 5, 7.  Kill criteria applied.
  G5 C3: tower typing + J-stability census of type-B lines.
  G6 C4: 16 B_n == 256 R(n) for all n in {3, 5, 7, 9, 11, 13} with
     B_n live from the shell censuses; isometry obstruction measured
     (norm-1 vector counts; Smith signature of the ramified inclusion
     re-computed = (1^4, 2^4)).
  C  MUST-FAIL CONTROLS: scrambled type labels (LCG permutation over
     orbits) change every matching count; the wrong weight system
     (3 unit + 5 double modes) misses the R degeneracies.

VERDICT ENUM (frozen): R-IDENTIFIED-CANONICAL (a candidate matches at
ALL tested places and survives a canonicity census) /
R-IDENTIFIED-CHOICEFUL (matches everywhere but depends on unforced
choices) / R-NO-ARROW-REALIZATION (honest negative: the packet layer
and the arrow layer share the exact totals B_p = 16 R(p), but none of
the frozen arrow-level objects realizes the finer R-grading at the
tested places).

FENCES: no free search -- the dictionary above is frozen and every
kill is reported; no-free-keys discipline; ROOTCLASS-MIXED (v775)
cited and unaffected (no code -> matter assignment); [C neu] semantics
typed.  Floats only in Fincke-Pohst bounds (exact integer rechecks)
-- everything else integer / F_p.

FIREWALL: experiments/ probe; ONE new file; writes nothing; no
verification/, paper, ledger, changelog or website surface touched;
no prime table / zeta symbols (AST-enforced); no v563 window surface.
Machinery read-only from v738 / v535 / hecke_arrow_ledger_probe
(certified sibling).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/r_microstate_identification_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from collections import Counter

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v738_hecke_mod_ramified as ram              # noqa: E402
import v535_hecke_from_geometry as kg              # noqa: E402
import hecke_arrow_ledger_probe as hal             # noqa: E402

FROZEN_SPEC = """\
HECKE.ARROW_MESSAGE.01 / R-microstate identification spec v1 (frozen
2026-08-05 after the disclosed pilot at p = 3, 5, 7 -- the pilot
produced only kills, reproduced as gates; no candidate was selected by
the pilot, so nothing is fitted).
Shells n in {3,5,7,9,11,13}; R reference (1,4,10,24,43,68) re-derived
from the triangular system.  Candidates C1 (type-B line orbits under
G0 / +J / +sigma / +conj / W(E8) / all), C2 (refined (a,deg) census
types), C3 (tower: typed no-pointwise; Kneser: J-stability, <= 2
classes), C4 (count-level 8-mode identity 16 B_n == 256 R(n), with the
isometry obstruction typed via SNF fingerprint + minimum counts).
Match must hold at ALL of p = 3, 5, 7; discriminators 11 -> 43 and
13 -> 68 run only for survivors (predeclared).  Controls: LCG label
scramble; wrong weight system 3+5.  Verdict enum:
R-IDENTIFIED-CANONICAL / R-IDENTIFIED-CHOICEFUL /
R-NO-ARROW-REALIZATION.  LCG seed 20260805.  Runtime cap ~15 min.
"""

SHELLS = (3, 5, 7, 9, 11, 13)
PLACES = (3, 5, 7)
R_EXPECT = {3: 1, 5: 4, 7: 10, 9: 24, 11: 43, 13: 68}
TYPE_B = [84, 64, 28, 64]

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "mpz_zeta")
FORBIDDEN_SURFACE = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN",
                     "ATOM_MAX", "atoms_in", "atom_lags_at", "arch_lags",
                     "frame_a_zones", "build_window", "odd_toeplitz",
                     "_NN")

CHECKS = []
CONTROL_FIRED = {}
MATCHED = []            # candidates matching at all tested places
T0 = time.time()

_LCG = [20260805]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


# ==================================================================== G0
def g0_firewall():
    section("G0 -- SHA-frozen spec + AST firewall + environment")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad, leaks = [], []
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
        if name in FORBIDDEN_SURFACE:
            leaks.append(name)
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    check("G0.2 no v563 window surface (AST-enforced)", not leaks,
          "leaks %s" % leaks if leaks else "clean")
    print("    python %s, numpy %s" % (sys.version.split()[0],
                                       np.__version__))


# ==================================================================== G1
def tri_census(unit, double, m_max):
    """level-m degeneracies of `unit` unit + `double` double-weight
    triangular modes (exact convolution)."""
    tri = []
    k = 0
    while k * (k + 1) // 2 <= m_max:
        tri.append(k * (k + 1) // 2)
        k += 1
    one = [0] * (m_max + 1)
    for t in tri:
        one[t] += 1
    two = [0] * (m_max + 1)
    for t in tri:
        if 2 * t <= m_max:
            two[2 * t] += 1

    def conv(a, b):
        out = [0] * (m_max + 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if i + j <= m_max and bj:
                        out[i + j] += ai * bj
        return out

    res = [0] * (m_max + 1)
    res[0] = 1
    for _ in range(unit):
        res = conv(res, one)
    for _ in range(double):
        res = conv(res, two)
    return res


def odd_diag_count(target):
    """#{(x, y) in Z^8, all coords odd : Sum x^2 + 2 Sum y^2 = target}
    by exact convolution of one-mode theta series."""
    one = [0] * (target + 1)
    x = 1
    while x * x <= target:
        one[x * x] += 2
        x += 2
    two = [0] * (target + 1)
    x = 1
    while 2 * x * x <= target:
        two[2 * x * x] += 2
        x += 2

    def conv(a, b):
        out = [0] * (target + 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if i + j <= target and bj:
                        out[i + j] += ai * bj
        return out

    res = [0] * (target + 1)
    res[0] = 1
    for _ in range(4):
        res = conv(res, one)
    for _ in range(4):
        res = conv(res, two)
    return res[target]


def g1_ground_truth():
    section("G1 -- ground truth: the triangular system and its sign "
            "lift")
    m_max = (max(SHELLS) - 3) // 2
    cens = tri_census(4, 4, m_max)
    Rs = {n: cens[(n - 3) // 2] for n in SHELLS}
    ok_R = (Rs == R_EXPECT)
    check("G1.1 R(2m+3) from 4 unit + 4 double triangular modes = %s "
          "== (1, 4, 10, 24, 43, 68)" % [Rs[n] for n in SHELLS], ok_R)
    ok_lift = all(odd_diag_count(4 * n) == 256 * R_EXPECT[n]
                  for n in SHELLS)
    # direct enumeration cross-check at n = 3, 5, 7
    ok_dir = True
    for n in (3, 5, 7):
        cnt = 0
        b1 = int(math.isqrt(4 * n))
        xs = [x for x in range(-b1, b1 + 1) if x % 2]
        for x0 in xs:
            for x1 in xs:
                for x2 in xs:
                    for x3 in xs:
                        r = 4 * n - x0 * x0 - x1 * x1 - x2 * x2 - x3 * x3
                        if r < 8:
                            continue
                        for y0 in xs:
                            for y1 in xs:
                                for y2 in xs:
                                    for y3 in xs:
                                        if 2 * (y0 * y0 + y1 * y1
                                                + y2 * y2 + y3 * y3) == r:
                                            cnt += 1
        ok_dir &= (cnt == 256 * R_EXPECT[n])
    check("G1.2 sign lift: 256 R(n) == #odd vectors of diag(1^4, 2^4) "
          "at 4n, all shells (convolution) + direct enumeration at "
          "n = 3, 5, 7", ok_lift and ok_dir)
    return Rs


# ==================================================================== G2
BE = kg.BE_np.astype(np.int64)
G8 = kg.G


def amb_op_to_coeff(f):
    cols = []
    for j in range(8):
        img = np.array(f(tuple(int(v) for v in BE[:, j])), np.int64)
        num = kg.Adj @ img
        assert np.all(num % kg.detBE == 0)
        cols.append(num // kg.detBE)
    return np.stack(cols, axis=1)


def g2_operators():
    section("G2 -- deployed operators on the coeff lattice")
    Jc = amb_op_to_coeff(lambda w: ram.unpack(
        tuple(ram.gmul((0, 1), z) for z in ram.pack(w))))
    Sc = amb_op_to_coeff(ram.sig8)
    Cc = amb_op_to_coeff(ram.conj8)
    eye = np.eye(8, dtype=np.int64)
    ok_ord = (np.array_equal(np.linalg.matrix_power(Jc, 4), eye)
              and np.array_equal(np.linalg.matrix_power(Sc, 3), eye)
              and np.array_equal(Cc @ Cc, eye))
    ok_iso = all(np.array_equal(M.T @ G8 @ M, G8) for M in (Jc, Sc, Cc))
    check("G2.1 J (mu4 clock), sigma (triality), conj8: integral, "
          "J^4 = sigma^3 = conj^2 = 1, isometries of q", ok_ord
          and ok_iso)
    # reflections for the W(E8) closure
    U = np.linalg.cholesky(G8.astype(np.float64)).T
    roots = []
    x = [0] * 8
    eps = 1e-7

    def go(k, right):
        if k < 0:
            c = np.array(x, dtype=np.int64)
            if int(c @ G8 @ c) == 2:
                roots.append(c.copy())
            return
        s = 0.0
        for j in range(k + 1, 8):
            s += U[k, j] * x[j]
        ukk = U[k, k]
        thr = math.sqrt(max(0.0, right))
        for xk in range(math.ceil((-thr - s) / ukk - eps),
                        math.floor((thr - s) / ukk + eps) + 1):
            x[k] = xk
            t = ukk * xk + s
            go(k - 1, right - t * t)
        x[k] = 0

    go(7, 2.0 + eps)
    refls = []
    for _ in range(5):
        r = roots[lcg(len(roots))]
        S = np.eye(8, dtype=np.int64) - np.outer(r, G8 @ r)
        refls.append(S)
    ok_r = (len(roots) == 240
            and all(np.array_equal(S.T @ G8 @ S, G8) for S in refls))
    check("G2.2 240 roots; 5 LCG root reflections are isometries "
          "(W(E8) closure generators)", ok_r)
    return dict(J=Jc, sig=Sc, conj=Cc, refls=refls)


# ==================================================================== C1/C2
def orbit_data(p, Mint):
    mats = Mint % p
    orbs, nlines = kg.orbit_reps(p, mats)
    lin2orb = {}
    types = []
    for oi, (c0, osz) in enumerate(orbs):
        orb = {kg.canon_line(img, p)
               for img in (mats @ np.asarray(c0, np.int64)) % p}
        assert len(orb) == osz
        for k in orb:
            lin2orb[k] = oi
        vadj = kg.adjust_isotropic_lift(np.asarray(c0, np.int64), p)
        vec4, refined, _t = hal.marked_census_line(vadj, p)
        types.append(dict(is_b=(vec4 == TYPE_B), vec4=vec4,
                          refined=refined, osz=osz))
    return orbs, lin2orb, types, nlines


def merged_counts(p, orbs, lin2orb, types, gens):
    parent = list(range(len(orbs)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    n_viol = 0
    lines = list(lin2orb.items())
    for g in gens:
        gp = g % p
        for k, oi in lines:
            img = kg.canon_line((gp @ np.array(k, np.int64)) % p, p)
            oj = lin2orb[img]
            if types[oi]["is_b"] != types[oj]["is_b"]:
                n_viol += 1
            ra, rb = find(oi), find(oj)
            if ra != rb:
                parent[ra] = rb
    classes = {}
    for oi in range(len(orbs)):
        classes.setdefault(find(oi), []).append(oi)
    nb = sum(1 for cs in classes.values()
             if any(types[o]["is_b"] for o in cs))
    return nb, len(classes), n_viol


def refined_inv(t, p):
    a0 = tuple(t["refined"].get((0, d), 0) for d in range(4))
    rows = sorted(tuple(t["refined"].get((a, d), 0) for d in range(4))
                  for a in range(1, p))
    return (tuple(t["vec4"]), a0, tuple(rows))


def g3_g4_g5(ops):
    section("G3/G4/G5 -- candidate censuses at p = 3, 5, 7 "
            "(kill tables)")
    Mint = hal.weyl_int_mats()
    menu = [("G0", []),
            ("G0+J", [ops["J"]]),
            ("G0+sigma", [ops["sig"]]),
            ("G0+conj", [ops["conj"]]),
            ("G0+J+sigma", [ops["J"], ops["sig"]]),
            ("WE8", list(ops["refls"])),
            ("WE8+J+conj", [ops["J"], ops["conj"]] + list(ops["refls"]))]
    table = {name: {} for name, _g in menu}
    c2 = {}
    c3 = {}
    data = {}
    for p in PLACES:
        t0 = time.time()
        orbs, lin2orb, types, nlines = orbit_data(p, Mint)
        data[p] = (orbs, lin2orb, types)
        for name, gens in menu:
            if not gens:
                nb = sum(1 for t in types if t["is_b"])
                table[name][p] = (nb, len(orbs), 0)
            else:
                table[name][p] = merged_counts(p, orbs, lin2orb, types,
                                               gens)
        c2[p] = len({refined_inv(t, p) for t in types if t["is_b"]})
        # C3: J-stability census of type-B LINES
        Jp = ops["J"] % p
        stab = mov = 0
        for k, oi in lin2orb.items():
            if not types[oi]["is_b"]:
                continue
            img = kg.canon_line((Jp @ np.array(k, np.int64)) % p, p)
            if img == k:
                stab += 1
            else:
                mov += 1
        c3[p] = (stab, mov)
        print("    p = %d done (%.1f s): %d lines, %d G0 orbits"
              % (p, time.time() - t0, nlines, len(orbs)))

    # ---- C1 verdicts
    print("\n    C1 kill table (type-B classes; R target (1, 4, 10)):")
    for name, _g in menu:
        row = [table[name][p][0] for p in PLACES]
        viol = [table[name][p][2] for p in PLACES]
        tot = [table[name][p][1] for p in PLACES]
        well = all(v == 0 for v in viol) or name == "G0"
        match = (row == [R_EXPECT[p] for p in PLACES]) and well
        if match:
            MATCHED.append("C1:" + name)
        print("      %-12s B-classes %-12s total %-14s typeB-set "
              "violations %-18s -> %s"
              % (name, row, tot, viol,
                 "MATCH" if match else
                 ("KILL (ill-defined: type-B not invariant)"
                  if not well else "KILL (count)")))
    ok_g0 = (table["G0"][3][0], table["G0"][5][0],
             table["G0"][7][0]) == (1, 4, 13)
    check("G3.1 C1 base measurement reproduced: G0 type-B orbit "
          "counts (1, 4, 13) -- kills at p = 7 (13 != 10)", ok_g0)
    n_bad = sum(1 for name, _g in menu[1:]
                if any(table[name][p][2] == 0 for p in PLACES))
    check("G3.2 C1 extensions: the type-B set is NOT invariant under "
          "ANY deployed extension (J / sigma / conj / W(E8)) -- the "
          "A/B typing is glue-frame data, the extensions are "
          "ill-defined on it", n_bad == 0)

    check("G4.1 C2 refined-type counts (%d, %d, %d) -- every G0 orbit "
          "carries a distinct refined census; kills at p = 7 "
          "(13 != 10)" % (c2[3], c2[5], c2[7]),
          (c2[3], c2[5], c2[7]) == (1, 4, 13))
    if (c2[3], c2[5], c2[7]) == tuple(R_EXPECT[p] for p in PLACES):
        MATCHED.append("C2")

    print("    C3 tower side: no pointwise switch arrows exist -- the "
          "broadcast parity is a\n    channel decomposition and odd "
          "tower arrows are all-keep (degree * id on V,\n    sibling "
          "G4.4); typed, no count to match.")
    n_cls = {p: sum(1 for x in c3[p] if x) for p in PLACES}
    ok_tot = all(c3[p][0] + c3[p][1]
                 == sum(t["osz"] for t in data[p][2] if t["is_b"])
                 for p in PLACES)
    check("G5.1 C3 Kneser side: J-stability census of type-B lines "
          "(stable, moved) = %s -> class counts %s -- at most 2 "
          "classes, kills at p = 5 (4 needed) and p = 7 (10 needed)"
          % (c3, [n_cls[p] for p in PLACES]),
          ok_tot and n_cls[5] <= 2 and n_cls[5] != R_EXPECT[5])
    return data


# ==================================================================== G6
CHOL_U = np.linalg.cholesky(G8.astype(np.float64)).T


def enum_shell(n):
    out = []
    x = [0] * 8
    eps = 1e-7
    U = CHOL_U

    def go(k, right):
        if k < 0:
            c = np.array(x, dtype=np.int64)
            if int(c @ G8 @ c) == 2 * n:
                out.append(c.copy())
            return
        s = 0.0
        for j in range(k + 1, 8):
            s += U[k, j] * x[j]
        ukk = U[k, k]
        thr = math.sqrt(max(0.0, right))
        for xk in range(math.ceil((-thr - s) / ukk - eps),
                        math.floor((thr - s) / ukk + eps) + 1):
            x[k] = xk
            t = ukk * xk + s
            go(k - 1, right - t * t)
        x[k] = 0

    go(7, 2.0 * n + eps)
    return np.stack(out)


def g6_count_level(Rs):
    section("G6 -- C4: the count-level 8-mode identity and its "
            "obstruction")
    DVEC = np.asarray(kg.DVEC, dtype=np.int64)
    ok_id = True
    for n in SHELLS:
        C = enum_shell(n)
        N = len(C)
        deg = (C @ DVEC) % 4
        th = [int(np.sum(deg == j)) for j in range(4)]
        B = (N // 240 + (th[0] - th[2]) // 8) // 2
        ok = (16 * B == 256 * Rs[n])
        ok_id &= ok
        print("    n = %2d: B_n = %4d live; per-class switch 16 B = "
              "%5d == 256 R = %5d (%s)"
              % (n, B, 16 * B, 256 * Rs[n], ok))
    check("G6.1 count identity: per-class switch multiplicity "
          "16 B_n == 256 R(n) on every odd shell (B live from the "
          "glue census)", ok_id)

    # obstruction to a GRADED realization: no admissible isometry
    diag_min = odd_min_count = 0
    # diag(1^4,2^4): norm-1 vectors = +/- e_1..e_4 -> 8; E8: q-min 1
    # with 240 vectors (shell 1)
    diag_min = 8
    e8_min = len(enum_shell(1))
    # Smith signature of the ramified inclusion (1+i)L in L; the
    # Z-basis of L is {m_k, i m_k} from the Z[i]-HNF basis rows of
    # Lmodule (z_basis_L gives Z[i]-GENERATORS only, not a Z-basis)
    Lm = ram.Lmodule()
    zb = []
    for k in range(4):
        mk = tuple(Lm.M[k])
        zb.append(np.array(ram.unpack(mk), dtype=np.int64))
        imk = tuple(ram.gmul((0, 1), z) for z in mk)
        zb.append(np.array(ram.unpack(imk), dtype=np.int64))
    two_gens = []
    for b in zb:
        img = ram.pack(tuple(int(v) for v in b))
        img = tuple(ram.gmul((1, 1), z) for z in img)
        two_gens.append(np.array(ram.unpack(img), dtype=np.int64))
    Bz = np.stack(zb, axis=1)
    M = np.stack(two_gens, axis=1)
    X = np.linalg.solve(Bz.astype(np.float64), M.astype(np.float64))
    X = np.rint(X).astype(np.int64)
    ok_x = np.array_equal(Bz @ X, M)

    # elementary divisors via gcd of k x k minors (exact, foolproof)
    def snf_minor_gcd(Xi):
        from itertools import combinations
        n = Xi.shape[0]
        rowsA = list(range(n))

        def det_int(sub):
            # entries are in {-1, 0, 1}; k <= 8, so |det| <= 8! and
            # the rounded float determinant is exact
            return int(round(np.linalg.det(sub.astype(np.float64))))

        dks = [1]
        for k in range(1, n + 1):
            g = 0
            for rs in combinations(rowsA, k):
                for cs in combinations(rowsA, k):
                    g = math.gcd(g, abs(det_int(Xi[np.ix_(rs, cs)])))
                    if g == 1:
                        break
                if g == 1:
                    break
            dks.append(g)
        return sorted(dks[k] // dks[k - 1] for k in range(1, n + 1))

    sig = snf_minor_gcd(X)
    ok_snf = (sig == [1, 1, 1, 1, 2, 2, 2, 2])
    check("G6.2 obstruction: Smith signature of (1+i)L in L = %s == "
          "(1^4, 2^4) (the shared fingerprint), but the minimum-vector "
          "counts differ (diag form: %d at norm 1; E8: %d at q = 1) "
          "-- no isometry, so C4 is COUNT-LEVEL ONLY (SNF sibling "
          "typed fingerprint-only; no graded arrow realization)"
          % (sig, diag_min, e8_min),
          ok_x and ok_snf and diag_min == 8 and e8_min == 240)
    return ok_id


# ==================================================================== C
def c_controls(data, Rs):
    section("C -- must-fail controls")
    # C-a: scrambled type labels at p = 7 (LCG permutation over orbits)
    orbs, lin2orb, types = data[7]
    flags = [t["is_b"] for t in types]
    perm = list(range(len(flags)))
    for i in range(len(perm) - 1, 0, -1):
        j = lcg(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    scr = [flags[perm[i]] for i in range(len(flags))]
    nb_scr = sum(1 for f in scr if f)
    lines_scr = sum(types[i]["osz"] for i, f in enumerate(scr) if f)
    lines_true = sum(t["osz"] for t in types if t["is_b"])
    fired1 = (scr != flags and lines_scr != lines_true)
    CONTROL_FIRED["Ca"] = fired1
    check("C-a scrambled type labels (LCG orbit permutation, p = 7): "
          "type-B line total %d != true %d (orbit count %d vs 13) -- "
          "any matching candidate's count breaks"
          % (lines_scr, lines_true, nb_scr), fired1)
    # C-b: wrong weight system (3 unit + 5 double modes)
    m_max = (max(SHELLS) - 3) // 2
    wrong = tri_census(3, 5, m_max)
    row = [wrong[(n - 3) // 2] for n in SHELLS]
    fired2 = (row != [Rs[n] for n in SHELLS])
    CONTROL_FIRED["Cb"] = fired2
    check("C-b wrong weight system (3 + 5 modes): degeneracies %s != "
          "R %s -- the 4 + 4 split is load-bearing"
          % (row, [Rs[n] for n in SHELLS]), fired2)


# ================================================================ verdict
def verdict():
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False) for c in ("Ca", "Cb"))
    if MATCHED:
        v = "R-IDENTIFIED-CHOICEFUL (%s; canonicity census required)" \
            % ",".join(MATCHED)
    elif controls_ok and n_pass == n_all:
        v = "R-NO-ARROW-REALIZATION"
    else:
        v = "R-NO-ARROW-REALIZATION (with %d failed checks -- inspect)" \
            % (n_all - n_pass)
    print("VERDICT: %s" % v)
    if v == "R-NO-ARROW-REALIZATION":
        print("""
HECKE.ARROW_MESSAGE.01 / R-IDENTIFICATION: R-NO-ARROW-REALIZATION --
the honest negative.  R(p) is an ANALYTIC packet count without an
arrow-level realization at the tested places:
  * C1: the type-B orbit counts under G0 are (1, 4, 13) -- killed at
    p = 7; under EVERY deployed extension (mu4 clock J, triality
    sigma, conjugation, W(E8) closure) the type-B set itself is not
    invariant (the A/B typing is glue-frame data), so the extended
    orbit counts are ill-defined;
  * C2: the refined (a, deg) census separates all 13 orbits at p = 7
    (1, 4, 13) -- killed;
  * C3: pointwise switch arrows do not exist (the broadcast parity is
    a channel decomposition; odd tower arrows are all-keep), and the
    Kneser J-stability census has at most 2 classes -- killed at
    p = 5;
  * C4: the COUNT identity is exact everywhere (per-class switch
    multiplicity 16 B_n = 256 R(n) = the odd-vector count of
    diag(1^4, 2^4) at 4n), but the graded realization is obstructed:
    the Smith signature (1^4, 2^4) is shared while the minimum-vector
    counts (8 vs 240) exclude any isometry -- count-level only.
STRUCTURAL BOUNDARY (typed): the packet layer and the arrow layer
share exact totals (B_p = 16 R(p), arrow-exact per V-class) but NOT
the finer R-grading; the 8-mode oscillator lives on the analytic side
of the trace.  [C neu]; no-free-keys respected (frozen dictionary, all
kills reported); ROOTCLASS-MIXED (v775) unaffected.""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def main():
    print("=" * 74)
    print("HECKE.ARROW_MESSAGE.01 follow-up -- the R-microstate "
          "identification")
    print("=" * 74)
    g0_firewall()
    Rs = g1_ground_truth()
    ops = g2_operators()
    hal.DVEC_ARR = np.asarray(kg.DVEC, dtype=np.int64)
    data = g3_g4_g5(ops)
    g6_count_level(Rs)
    c_controls(data, Rs)
    v = verdict()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)
                 and v.startswith("R-")) else 1


if __name__ == "__main__":
    sys.exit(main())
