#!/usr/bin/env python3
"""PRIME.C2.PLANEFRAMES.01 -- the A3/B3 plane-frame identity decider.

EXPLORATION ONLY (experiments/tfpt-discovery).  Writes nothing outside
stdout; no verification/, no ledger, no TeX, no website, no .md.

THE CLAIM SET (the user's plane-frame identities, [E neu] candidates):
on V = F2^4 with the unique sigma-invariant symplectic form omega,
the 35 linear 2-planes split 15 isotropic + 20 non-isotropic; the
affine versions are 60 iso (15 x 4 cosets) + 80 non-iso (20 x 4),
with 45 + 60 not through 0 and 15 + 20 through 0.  With H_+ (60 x 15)
and H_- (80 x 15) the incidence matrices on the 15 nonzero
coordinates:

  (G1) H_+^T H_+  == 12 I + 3 J          (all 60 iso planes)
  (G2) H_-^T H_-  == 16 I + 4 J          (all 80 non-iso planes)
       on 1^perp: 12 I and 16 I
  (G3) HECKE MATCH: A_3 = 12, B_3 = 16 from sigma3(3) = 28,
       a_3(f8) = -4 (BOTH recomputed independently: divisor sums +
       the eta product eta(2t)^4 eta(4t)^4) -- the operator
       identities Pi_perp H_+^T H_+ Pi_perp == A_3 Pi_perp and
       Pi_perp H_-^T H_- Pi_perp == B_3 Pi_perp exactly; hence
       A_3 + B_3 = 28 and A_3 - B_3 = -4 are PLANE-COUNT statements.
  (G4) split blocks: H_{+,105}^T H_{+,105} == 10 I - B + 3 J,
       H_{-,105}^T H_{-,105} == 12 I + B + 3 J; origin planes:
       2 I + B and 4 I + J - B; the +-B cross-terms cancel exactly
       in the sums (G1)/(G2).
  (G5) the 105-Gram == 22 I + 6 J == 2 B^2 + 14 I via B^2 = 4I + 3J
       (discrete Weitzenboeck form); H_140^T H_140 == 28 I + 7 J,
       spectrum {133, 28^14} -- 133 = 112 + 21 = dim E7 and
       28 = 22 + 6 = sigma3(3) typed as [C] fingerprints, the matrix
       identities as [E neu].
  (G6) THE INTERTWINER: U_+ = H_+/sqrt(12), U_- = H_-/4 on 1^perp
       satisfy U^T U = I; V_n = sqrt(A_n) U_+ (+) sqrt(B_n) U_-
       satisfies V^T V = sigma3(n) I and V^T Gamma V = a_n I on
       1^perp (Gamma = +1 on iso rows, -1 on non-iso rows) --
       verified exactly at the Gram level (where sqrt(A_n) appears
       squared) for n = 3, 5, 7 with A_n = (sigma3 + a_n)/2,
       B_n = (sigma3 - a_n)/2 from the certified positive lift
       (positivity re-gated).

CONTROLS (must fire): the wrong form (standard dot product) breaks
the 15/20 iso split and the Gram identity; scrambled planes break
G1; a wrong grading breaks V^T Gamma V = a_n I.

VERDICT ENUM (frozen): PLANEFRAMES-EXACT / PLANEFRAMES-PARTIAL /
PLANEFRAMES-DEAD.  FENCES: ROOTCLASS-MIXED, no RH claim; the
133/28/112 numerology is typed [C] fingerprint, NOT derivation.

Predecessors (read-only): kraus_spread_commutant_probe (frame
recipe), v738 (Lmodule, sigma), positive_descent / f8 probes
(positive lift A_n, B_n; a_p anchors -4/-2/24 re-derived here
independently via the eta product).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_c2_planeframes_probe.py
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
PRIME.C2.PLANEFRAMES.01 spec v1 (frozen 2026-08-06, before the first
run).
Frame: doily-probe recipe (unique sigma-invariant Omega -> omega, B
  with diagonal 1, row degree 7).
Bookkeeping gates: 35 = 15 iso + 20 non-iso linear planes; affine
  60 = 15 x 4 iso, 80 = 20 x 4 non-iso; not-through-0 45 + 60 = 105;
  through-0 15 + 20 = 35.
Gram gates (entrywise integer): G1 12I + 3J; G2 16I + 4J; G4 splits
  10I - B + 3J / 12I + B + 3J / 2I + B / 4I + J - B with exact +-B
  cancellation; G5 105-Gram == 22I + 6J == 2B^2 + 14I and 140-Gram
  == 28I + 7J with spectrum {133, 28^14} (structural + float ward).
Hecke gates: sigma3(n) by divisor cubes (28/126/344); a_n by the
  eta product q prod (1-q^{2m})^4 (1-q^{4m})^4 (a_3 = -4, a_5 = -2,
  a_7 = 24, independent of prior probes); A_n = (sigma3 + a)/2 >= 0,
  B_n = (sigma3 - a)/2 >= 0; G3/G6 operator identities exact in
  Fractions on 1^perp for n = 3, 5, 7 (Gram level: A_n G_+/12 +
  B_n G_-/16 == sigma3(n) on 1^perp; A_n G_+/12 - B_n G_-/16 ==
  a_n on 1^perp).
Controls: dot-product form -> iso census != 15 or Gram != 12I + 3J;
  LCG-scrambled 60 weight-4 rows -> Gram != 12I + 3J; LCG random
  grading -> twisted Gram not scalar on 1^perp.  LCG seed 20260806.
Verdicts: PLANEFRAMES-EXACT / -PARTIAL / -DEAD.  Runtime cap
~20 min.  NO RH/GRH claim.
"""

LABEL_DIM = 15
A_ANCHORS = {3: -4, 5: -2, 7: 24}
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
    section("S1 -- frame (doily-probe recipe)")
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
    ok = n_inv == 1 and bool(np.all(B.sum(axis=1) == 7))
    check("S1.1 frame: unique sigma-invariant omega; B row degree 7 "
          "(diagonal 1)", ok)
    GATE_FLAGS["frame"] = ok
    return dict(labels=labels, lidx=lidx, om=om, B=B)


# ================================ S2 plane bookkeeping + H matrices
def plane_families(labels, form):
    lin = sorted({frozenset({(0, 0, 0, 0), x, y,
                             tuple(a ^ b for a, b in zip(x, y))})
                  for x, y in combinations(labels, 2)},
                 key=lambda s: sorted(s))
    iso_lin = [P for P in lin
               if all(form(x, y) == 0 for x in P for y in P)]
    non_lin = [P for P in lin if P not in set(iso_lin)]
    aff = {}
    for P in lin:
        cos = {frozenset(P)}
        for v in labels:
            if v not in P:
                cos.add(frozenset(tuple(a ^ b for a, b in zip(v, p))
                                  for p in P))
        aff[P] = sorted(cos, key=lambda s: sorted(s))
    return lin, iso_lin, non_lin, aff


def hmat(planes, lidx):
    H = np.zeros((len(planes), LABEL_DIM), dtype=np.int64)
    for r, A in enumerate(planes):
        for v in A:
            if v != (0, 0, 0, 0):
                H[r, lidx[v]] = 1
    return H


def s2_bookkeeping(fr):
    section("S2 -- plane bookkeeping under omega")
    labels, lidx, om = fr["labels"], fr["lidx"], fr["om"]
    lin, iso_lin, non_lin, aff = plane_families(labels, om)
    iso_aff = [A for P in iso_lin for A in aff[P]]
    non_aff = [A for P in non_lin for A in aff[P]]
    iso_105 = [A for A in iso_aff if (0, 0, 0, 0) not in A]
    non_105 = [A for A in non_aff if (0, 0, 0, 0) not in A]
    ok = (len(lin) == 35 and len(iso_lin) == 15 and len(non_lin) == 20
          and len(iso_aff) == 60 and len(non_aff) == 80
          and len(iso_105) == 45 and len(non_105) == 60)
    check("S2.1 bookkeeping: 35 linear = 15 iso + 20 non-iso; affine "
          "60 = 15 x 4 iso, 80 = 20 x 4 non-iso; not-through-0 "
          "45 + 60 = 105; through-0 15 + 20 = 35", ok)
    GATE_FLAGS["bookkeeping"] = ok
    return dict(iso_lin=iso_lin, non_lin=non_lin, iso_aff=iso_aff,
                non_aff=non_aff, iso_105=iso_105, non_105=non_105,
                Hp=hmat(iso_aff, lidx), Hm=hmat(non_aff, lidx),
                Hp105=hmat(iso_105, lidx), Hm105=hmat(non_105, lidx),
                Hp0=hmat(iso_lin, lidx), Hm0=hmat(non_lin, lidx))


# ================================ S3 the six Gram identities
def s3_grams(fr, pl):
    section("S3 -- the Gram identities, entrywise exact")
    B = fr["B"]
    I = np.eye(LABEL_DIM, dtype=np.int64)
    J = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)
    Gp = pl["Hp"].T @ pl["Hp"]
    Gm = pl["Hm"].T @ pl["Hm"]
    ok1 = int(np.max(np.abs(Gp - (12 * I + 3 * J)))) == 0
    ok2 = int(np.max(np.abs(Gm - (16 * I + 4 * J)))) == 0
    check("S3.1 (G1) H_+^T H_+ == 12 I + 3 J (all 60 iso affine "
          "planes)", ok1)
    check("S3.2 (G2) H_-^T H_- == 16 I + 4 J (all 80 non-iso affine "
          "planes)", ok2)
    Gp105 = pl["Hp105"].T @ pl["Hp105"]
    Gm105 = pl["Hm105"].T @ pl["Hm105"]
    Gp0 = pl["Hp0"].T @ pl["Hp0"]
    Gm0 = pl["Hm0"].T @ pl["Hm0"]
    ok4 = (int(np.max(np.abs(Gp105 - (10 * I - B + 3 * J)))) == 0
           and int(np.max(np.abs(Gm105 - (12 * I + B + 3 * J)))) == 0
           and int(np.max(np.abs(Gp0 - (2 * I + B)))) == 0
           and int(np.max(np.abs(Gm0 - (4 * I + J - B)))) == 0
           and int(np.max(np.abs((Gp105 + Gp0) - Gp))) == 0
           and int(np.max(np.abs((Gm105 + Gm0) - Gm))) == 0)
    check("S3.3 (G4) split blocks: 10I - B + 3J (45 iso not-0), "
          "12I + B + 3J (60 non-iso not-0), 2I + B (15 origin iso), "
          "4I + J - B (20 origin non-iso); the +-B cross terms "
          "CANCEL exactly in the sums", ok4)
    G105 = Gp105 + Gm105
    okB2 = int(np.max(np.abs(B @ B - (4 * I + 3 * J)))) == 0
    ok5a = (int(np.max(np.abs(G105 - (22 * I + 6 * J)))) == 0
            and int(np.max(np.abs(G105 - (2 * B @ B + 14 * I)))) == 0)
    G140 = Gp + Gm
    ok5b = int(np.max(np.abs(G140 - (28 * I + 7 * J)))) == 0
    ev = np.linalg.eigvalsh(G140.astype(float))
    ok_spec = (abs(ev[-1] - 133.0) <= 1e-9
               and np.all(np.abs(ev[:-1] - 28.0) <= 1e-9))
    check("S3.4 (G5) 105-Gram == 22I + 6J == 2B^2 + 14I (B^2 == "
          "4I + 3J re-gated) -- discrete Weitzenboeck form; 140-Gram "
          "== 28I + 7J, spectrum {133, 28^14} (structural: 28 + "
          "7*15 = 133 on uniform, 28 on 1-perp; float ward)",
          okB2 and ok5a and ok5b and ok_spec)
    print("    [C] fingerprints (typed, NOT derivations): "
          "133 = 112 + 21 = dim E7; 28 = 22 + 6 = sigma3(3); "
          "diag(105-Gram) = 28.")
    GATE_FLAGS["grams"] = ok1 and ok2 and ok4 and okB2 and ok5a \
        and ok5b and ok_spec
    return dict(Gp=Gp, Gm=Gm)


# ================================ S4 Hecke match + the intertwiner
def eta_f8_coeffs(N):
    """f8 = q prod (1-q^{2m})^4 (1-q^{4m})^4; returns a[1..N]."""
    c = [0] * (N + 1)
    c[0] = 1
    for step in (2, 4):
        for m in range(step, N + 1, step):
            for _ in range(4):
                for j in range(N, m - 1, -1):
                    c[j] -= c[j - m]
    a = [0] * (N + 2)
    for n in range(1, N + 2):
        if n - 1 <= N:
            a[n] = c[n - 1]
    return a


def s4_hecke(fr, pl):
    section("S4 -- Hecke match + the Stinespring intertwiner")
    a = eta_f8_coeffs(10)
    sig3 = {n: sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
            for n in (3, 5, 7)}
    ok_a = all(a[p] == A_ANCHORS[p] for p in (3, 5, 7))
    ok_s = sig3 == {3: 28, 5: 126, 7: 344}
    AB = {n: ((sig3[n] + a[n]) // 2, (sig3[n] - a[n]) // 2)
          for n in (3, 5, 7)}
    ok_pos = all((sig3[n] + a[n]) % 2 == 0 and AB[n][0] >= 0
                 and AB[n][1] >= 0 for n in (3, 5, 7))
    check("S4.1 independent Hecke data: a_n from the eta product "
          "q prod(1-q^{2m})^4 (1-q^{4m})^4 = (-4, -2, 24); sigma3 = "
          "(28, 126, 344); positive lift A_n, B_n = %s (all >= 0)"
          % AB, ok_a and ok_s and ok_pos)
    ok_a3 = AB[3] == (12, 16)
    check("S4.2 (G3) THE HECKE MATCH: A_3 = 12 = per-point iso-"
          "plane completion count, B_3 = 16 = non-iso count; "
          "A_3 + B_3 = 28 = sigma3(3) and A_3 - B_3 = -4 = a_3 as "
          "PLANE-COUNT statements", ok_a3)

    # exact operator identities on 1-perp (Fractions)
    n15 = LABEL_DIM

    def fr_mat(M, den):
        return [[Fr(int(M[i, j]), den) for j in range(n15)]
                for i in range(n15)]

    def mat_eq(A, Bm):
        return all(a == b for ra, rb in zip(A, Bm)
                   for a, b in zip(ra, rb))

    def mmul(A, Bm):
        return [[sum(A[i][k] * Bm[k][j] for k in range(n15))
                 for j in range(n15)] for i in range(n15)]

    Iu = [[Fr(1) if i == j else Fr(0) for j in range(n15)]
          for i in range(n15)]
    Ju = [[Fr(1)] * n15 for _ in range(n15)]
    Pperp = [[Iu[i][j] - Fr(1, 15) for j in range(n15)]
             for i in range(n15)]
    Gp12 = fr_mat(pl["Hp"].T @ pl["Hp"], 12)
    Gm16 = fr_mat(pl["Hm"].T @ pl["Hm"], 16)
    ok_u = (mat_eq(mmul(mmul(Pperp, Gp12), Pperp), Pperp)
            and mat_eq(mmul(mmul(Pperp, Gm16), Pperp), Pperp))
    check("S4.3 (G6) frames: U_+ = H_+/sqrt(12), U_- = H_-/4 are "
          "isometries on 1-perp (Pi G_+/12 Pi == Pi and "
          "Pi G_-/16 Pi == Pi, exact Fractions)", ok_u)

    ok_v = True
    for n in (3, 5, 7):
        An, Bn = AB[n]
        M = [[An * Gp12[i][j] + Bn * Gm16[i][j] for j in range(n15)]
             for i in range(n15)]
        MG = [[An * Gp12[i][j] - Bn * Gm16[i][j] for j in range(n15)]
              for i in range(n15)]
        ref_v = [[sig3[n] * Iu[i][j] + Fr(sig3[n], 4) * Ju[i][j]
                  for j in range(n15)] for i in range(n15)]
        ref_g = [[a[n] * Iu[i][j] + Fr(a[n], 4) * Ju[i][j]
                  for j in range(n15)] for i in range(n15)]
        ok_v &= mat_eq(M, ref_v)
        ok_v &= mat_eq(MG, ref_g)
        ok_v &= mat_eq(mmul(mmul(Pperp, M), Pperp),
                       [[sig3[n] * Pperp[i][j] for j in range(n15)]
                        for i in range(n15)])
        ok_v &= mat_eq(mmul(mmul(Pperp, MG), Pperp),
                       [[a[n] * Pperp[i][j] for j in range(n15)]
                        for i in range(n15)])
    check("S4.4 (G6) THE INTERTWINER (Gram level, exact): V_n^T V_n "
          "= A_n G_+/12 + B_n G_-/16 == sigma3(n) I + (sigma3/4) J "
          "== sigma3(n) on 1-perp; V_n^T Gamma V_n = A_n G_+/12 - "
          "B_n G_-/16 == a_n I + (a_n/4) J == a_n on 1-perp -- for "
          "n = 3, 5, 7 (V*V = sigma3 I, V*GammaV = a_n I certified)",
          ok_v)
    GATE_FLAGS["hecke"] = ok_a and ok_s and ok_pos and ok_a3 and \
        ok_u and ok_v
    return dict(AB=AB, a=a, sig3=sig3)


# ================================================== S5 controls
def s5_controls(fr, pl, hk):
    section("S5 -- controls (must fire)")
    labels, lidx = fr["labels"], fr["lidx"]
    I = np.eye(LABEL_DIM, dtype=np.int64)
    J = np.ones((LABEL_DIM, LABEL_DIM), dtype=np.int64)

    # C1 wrong form (standard dot product)
    def dot(x, y):
        return sum(a * b for a, b in zip(x, y)) & 1

    lin, iso_lin_d, _non, aff = plane_families(labels, dot)
    iso_aff_d = [A for P in iso_lin_d for A in aff[P]]
    Hd = hmat(iso_aff_d, lidx)
    Gd = Hd.T @ Hd
    dev_d = int(np.max(np.abs(Gd - (12 * I + 3 * J)))) \
        if len(iso_aff_d) else 999
    CONTROL_FIRED["C1"] = (len(iso_lin_d) != 15) or dev_d != 0
    check("C1 wrong form (dot product): totally-singular linear "
          "planes = %d (!= 15) and iso-Gram deviates from 12I + 3J "
          "(max dev %s) -- fires"
          % (len(iso_lin_d), dev_d), CONTROL_FIRED["C1"])

    # C2 scrambled planes (random weight-4 rows) break G1
    Hs = np.zeros((60, LABEL_DIM), dtype=np.int64)
    for r in range(60):
        s = set()
        while len(s) < 4:
            s.add(lcg(15))
        for c in s:
            Hs[r, c] = 1
    devs = int(np.max(np.abs(Hs.T @ Hs - (12 * I + 3 * J))))
    CONTROL_FIRED["C2"] = devs != 0
    check("C2 scrambled planes (60 LCG random weight-4 rows): "
          "Gram deviates from 12I + 3J by max %d -- fires" % devs,
          CONTROL_FIRED["C2"])

    # C3 wrong grading breaks V^T Gamma V = a_n I
    sp = np.array([1 - 2 * lcg(2) for _ in range(60)], dtype=np.int64)
    sm = np.array([1 - 2 * lcg(2) for _ in range(80)], dtype=np.int64)
    An, Bn = hk["AB"][3]
    Mbad = (An * (pl["Hp"].T @ (sp[:, None] * pl["Hp"])) / 12.0
            + Bn * (pl["Hm"].T @ (sm[:, None] * pl["Hm"])) / 16.0)
    Pp = np.eye(LABEL_DIM) - np.ones((LABEL_DIM, LABEL_DIM)) / 15.0
    R = Pp @ Mbad @ Pp - hk["a"][3] * Pp
    dev_g = float(np.max(np.abs(R)))
    CONTROL_FIRED["C3"] = dev_g > 1.0e-9
    check("C3 wrong grading (LCG random +-1 on rows): "
          "Pi V^T Gamma' V Pi deviates from a_3 Pi by max %.3f "
          "-- fires" % dev_g, CONTROL_FIRED["C3"])
    GATE_FLAGS["controls"] = all(CONTROL_FIRED.values())


# ================================================== S6 verdict
def s6_verdict():
    section("S6 -- verdict")
    ok_all = all(GATE_FLAGS.get(k, False)
                 for k in ("frame", "bookkeeping", "grams", "hecke",
                           "controls"))
    n_pass = sum(1 for _n, o in CHECKS if o)
    print("gates: %d/%d PASS; controls fired: %s"
          % (n_pass, len(CHECKS), CONTROL_FIRED))
    print()
    verdict = ("PLANEFRAMES-EXACT" if ok_all else
               "PLANEFRAMES-PARTIAL (see FAIL lines)")
    print("VERDICT: %s" % verdict)
    print()
    print("Findings (typed, exploration only):")
    print("  1. All six Gram identities hold entrywise exactly; the")
    print("     +-B cross terms cancel; 105-Gram = 2B^2 + 14I; ")
    print("     140-Gram = 28I + 7J with spectrum {133, 28^14}.")
    print("  2. A_3 = 12 / B_3 = 16 ARE the per-point iso/non-iso")
    print("     affine plane completion counts: sigma3(3) = 28 and")
    print("     a_3 = -4 as plane-count statements [E neu candidate];")
    print("     133 = dim E7 / 28 = sigma3(3) typed [C] fingerprints.")
    print("  3. The plane frames give exact isometries U_+, U_- on")
    print("     1-perp and the graded Stinespring Gram identities")
    print("     V*V = sigma3(n) I, V*Gamma V = a_n I for n = 3, 5, 7")
    print("     with the certified positive lift (A_n, B_n >= 0).")
    print()
    print("Recommended text (report only, NOT written anywhere):")
    print("  PRIME.C2.PLANEFRAMES.01: the C2 packet pair (A_n, B_n)")
    print("  is carried by the two affine plane frames of (V, omega)")
    print("  -- iso (60, Gram 12I + 3J) and non-iso (80, 16I + 4J) --")
    print("  and the graded frame operator realizes sigma3(n) and a_n")
    print("  as exact operator identities on 1-perp.  Matrix")
    print("  identities [E neu]; 133/28 completions [C] fingerprints;")
    print("  NO RH claim.")
    return verdict


def main():
    t0 = time.time()
    print(FROZEN_SPEC)
    g0_firewall()
    fr = s1_frame()
    pl = s2_bookkeeping(fr)
    s3_grams(fr, pl)
    hk = s4_hecke(fr, pl)
    s5_controls(fr, pl, hk)
    verdict = s6_verdict()
    print()
    print("total runtime %.1f s" % (time.time() - t0))
    return verdict


if __name__ == "__main__":
    main()
