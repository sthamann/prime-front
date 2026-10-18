#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v819 -- PRIME.PACKET.RM14.01: the Reed-Muller identification of the 15-label channel -- the row hull is the punctured RM(1,4)* = [15,5,7], chi_NSR is ONE codeword, the self-reproduction cycle closes, and the CSS code [[15,1,3]] with triorthogonality, one probe (21/21 checks incl. the 3 must-fire controls, ~0.2 s; discovery probe prime_packet_rm14_probe.py, 2026-08-06, verdict RM14-EXACT; Lean companion TfptCarrier/PacketRM14.lean kernel-checked, 30 theorems, lake build green).  S1 THE AFFINE CODE [E neu]: the binary row hull of B (rows 1 + hbar(x,y) plus complements) = C_aff = {a + hbar(v,.)} = the punctured Reed-Muller RM(1,4)* = [15,5,7]; weight enumerator EXACTLY 1 + 15z^7 + 15z^8 + z^15 (census over all 32 words); the linear subcode C_0 = {hbar(v,.)} = the [15,4,8] SIMPLEX code (all 15 nonzero words equidistant weight 8); B B^T = 4I + 3J re-anchored.  S2 NS/R AS A CODEWORD: chi_NSR = hbar(., F_Sigma) is the C_0 word of y0 = F_Sigma -- the 7+8 split is the two sides of ONE RM codeword (word weight 8, complement weight 7), the C2 register is the affine bit a; 128 = 32 x 4 = |C_aff| x |mu4| typed [H] audit.  S3 THE SELF-REPRODUCTION CYCLE closes exactly: RM(1,3) --Construction A [E cited, v752/note_e8_gaussian_code]--> E8 --> V = F2^4 --> affine functions = RM(1,4)* --> restriction to the anchor plane chi_NSR = 1 (8 points, an affine 3-space) = [8,4,4] with enumerator 1 + 14z^4 + z^8, restriction kernel {0, 1+chi}, permutation-equivalent to the deployed e8-hat C_NAIVE with EXACTLY 1344 = |Aut(RM(1,3))| = |AGL(3,2)| equivalences (full 8!-census, both the deployed code and the restricted image).  S4 THE CSS CODE: C_0 subset C_1 = C_aff with dual C_1^perp = [15,10,4] (weight enumerator 1 + 105z^4 + 280z^6 + 435z^8 + 168z^10 + 35z^12 EXACT over all 1024 words; canonical form = shortened RM(2,4) = span{x_i, x_i x_j}, the 10 monomials an exact basis); 4 X-checks (simplex generators) + 10 Z-checks = 14 independent => [[15,1,3]] CSS with logicals Xbar = 1 + chi (weight 7, in C_1 minus C_0) and Zbar = {e0, e1, e0+e1} (weight 3), anticommuting, logical distances (dX, dZ) = (7, 3) by census; TRIORTHOGONALITY census: generator weights 8, pairwise overlaps 4, triple overlaps 2; full-code census: all 15 words weight 8, all 105 pairs overlap 4, independent triples (420) overlap 2, dependent triples (35) overlap 0; the zeta8/T-gate phase structure stays typed [H] with the pointer to the certified v798 Galois/Hadamard bit -- NO identification claimed.  S5 TFPT fingerprints typed [H], audit-only (14 checks = dim G2, distance 3 = N_fam, dX = 7, 4 = |mu4| = dim C_0 = pairwise overlap, 15 labels = |PG(3,2)|).  Controls fire (degenerate rank-3 form changes hull dimension and enumerator -- with the honest note that any NONdegenerate form yields the same code set, canonicity of hbar being v753's census [E]; scrambled point deletion breaks equidistance and B B^T; a non-RM 5-dim code fails the distance-7 census).  ROOTCLASS-MIXED cited: label combinatorics on the carrier quotient; no physics claim, no marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe prime_packet_rm14_probe.py (2026-08-06, 21/21, ~0.1 s, RM14-EXACT); re-run identically at promotion.  Promoted verbatim (the v774 import resolves against the verification directory; path swap, v795 precedent); a module-level _LAST verdict capture inserted (v791 precedent); numbers unchanged; run() encodes the pattern (v757 precedent).  Lean companion: experiments/lean4-carrier-rigidity/TfptCarrier/PacketRM14.lean (kernel-checked finite core, 30 theorems, carried in the shipped Lean manifest).

Original prime_packet_rm14_probe.py docstring (verbatim):
prime_packet_rm14_probe -- PRIME.PACKET.RM14.01 (Arf compiler
programme, follow-up to K5.SIXSTEP.TRANSPORT.01): the Reed-Muller
identification of the 15-label channel on the certified v752/v774
space V = L/(1+i)L = F2^4.

THE FROZEN CLAIMS (all [E neu] candidates, machine-certified):
 S1  THE AFFINE CODE: on the 15 nonzero points of V, the binary row
     hull of B (rows B_y(x) = 1 + hbar(x,y), plus complements) is
     C_aff = {c_{a,v}(x) = a + hbar(v,x)} = the punctured Reed-Muller
     RM(1,4)* = [15,5,7]; weight enumerator EXACTLY
     1 + 15z^7 + 15z^8 + z^15 (census over all 32 words); the linear
     subcode C_0 = {hbar(v,.)} = [15,4,8] = the SIMPLEX code (all 15
     nonzero words equidistant weight 8).  v752 tie: B B^T = 4I + 3J
     over Z.
 S2  NS/R AS A CODEWORD: chi_NSR = hbar(., F_Sigma) is the C_0 word
     of y0 = F_Sigma; the 7+8 split is the two sides of ONE RM
     codeword (word weight 8, complement weight 7 -- the C2 register
     is the affine bit a); 32 = 2*16 = |C_aff|; the 8 chi=1 classes
     x 16 roots/class = 128 (R sector, v752 [E]); 128 = 32*4 =
     |C_aff| * |mu4| typed [H] audit.
 S3  THE SELF-REPRODUCTION CYCLE: RM(1,3) --Construction A (cited
     [E], v752/note_e8_gaussian_code)--> E8 --> V = F2^4 --> affine
     functions = RM(1,4)* --> restriction to the anchor plane
     chi_NSR = 1 (8 points, an affine 3-space) = RM(1,3) AGAIN:
     the restricted code has 16 words, parameters [8,4,4], weight
     enumerator 1 + 14z^4 + z^8, restriction kernel = {0, 1+chi}
     (dim 1), and IS permutation-equivalent to the deployed e8-hat
     C_NAIVE (v774 G_NAIVE, [8,4,4] extended Hamming = RM(1,3)):
     full 8!-census counts the equivalences (expected |Aut(RM(1,3))|
     = 1344 > 0).
 S4  THE CSS CODE: C_0 subset C_1 = C_aff; dual C_1^perp = [15,10,4]
     with weight enumerator EXACTLY 1 + 105z^4 + 280z^6 + 435z^8 +
     168z^10 + 35z^12 (full census over all 1024 words); canonical
     form: C_1^perp = shortened RM(2,4) = span{x_i, x_i x_j} (4 + 6
     monomials -- verified as an exact basis); X-checks from C_0 (4)
     + Z-checks from C_1^perp (10) = 14 independent => [[15,1,3]]
     CSS; CSS conditions exact (C_0 subset C_1, all X-Z pairs
     orthogonal); logical operators exact: Xbar = 1 + chi (weight 7,
     in C_1 \ C_0), Zbar = {e0, e1, e0+e1} (weight 3, in C_0^perp \
     C_1^perp), <Xbar, Zbar> = 1; logical distances dX = 7 (census
     min over C_1 \ C_0) and dZ = 3 (census min over C_0^perp \
     C_1^perp, 2048 words) => distance 3.  TRIORTHOGONALITY census:
     the 4 simplex generator rows have single weights 8, pairwise
     overlaps 4, triple overlaps 2; full-code census: all 15 words
     weight 8, all 105 pairs overlap 4, independent triples (420)
     overlap 2, dependent triples (35) overlap 0.  The zeta8 phase
     structure stays typed [H] with the pointer to the certified
     Galois/Hadamard bit (v798_seam_clifford_modular_s) -- NO
     identification claimed.
 S5  TFPT FINGERPRINTS (typed [H], audit-level, carried as
     fingerprints ONLY): 14 checks = dim G2, distance 3 = N_fam,
     dX = 7, 4 = |mu4| = dim C_0 = pairwise overlap, 15 labels.

CONTROLS (must fire):
 C1  a DEGENERATE form (rank-3 Gram) changes the hull dimension and
     the weight enumerator.  HONEST NOTE printed: any NONDEGENERATE
     form yields the same code SET (the code is the set of all
     affine functionals, basis-free); the canonicity of hbar itself
     is v753's census [E] -- the control therefore targets
     degeneracy.
 C2  a SCRAMBLED point deletion (delete the nonzero point F_Sigma,
     keep 0) breaks the puncture structure: C_0 loses equidistance
     (weights {7,8}), and B B^T != 4I + 3J.
 C3  a non-RM 5-dim code (five disjoint weight-3 rows) fails the
     distance-7 census (min weight 3).

KILLS (frozen, any one fires => RM14-FALSE):
  K1  hull != C_aff, or enumerator != 1 + 15z^7 + 15z^8 + z^15, or
      C_aff != punctured RM(1,4), or C_0 not the [15,4,8] simplex,
      or B B^T != 4I + 3J.
  K2  chi_NSR not the F_Sigma codeword, or the 7+8 split fails, or
      a count (32 = 2*16, 8 classes, 128) fails.
  K3  the restricted code is not [8,4,4] with enumerator
      1 + 14z^4 + z^8, or kernel != {0, 1+chi}, or NOT permutation-
      equivalent to the deployed C_NAIVE.
  K4  the dual enumerator, the monomial basis, a CSS condition, the
      logical operators, a logical distance, or the triorthogonality
      census fails.
VERDICT (frozen): RM14-EXACT (all checks pass, controls fire) /
RM14-PARTIAL (no kill, but a non-kill check failed) / RM14-FALSE
(a kill fired OR a control does not fire).

TYPING: [E] cited corpus facts (v752/v753/v774 chain, Construction
A); [E neu] the machine-certified censuses here; [H] the zeta8
pointer and the TFPT fingerprints.  ROOTCLASS-MIXED cited: label
combinatorics on the carrier quotient; NO RH claim, no physics
claim.

FIREWALL: experiments/-Probe; schreibt nichts ausser sich selbst;
kein verification/-, Paper-, Ledger-, Changelog- oder Website-
Surface (eine Promotionsrunde laeuft parallel).  Exakte F2/Integer-
Arithmetik (Bitmasken); keine Floats, kein RNG, kein Fit.

Quellen (read-only): verification/v774_arf_spinor_compiler.py (hb,
GJI, W16, NZ15, FSIG, G_NAIVE/C_NAIVE -- die v752-Maschinerie),
verification/v752_projective_hamming_incidence.py (B B^T = 4I+3J,
15x16-Zensus, chi_NSR [E]), verification/v753_ramified_polarity.py
(Kanonizitaet von hbar [E]), note_e8_gaussian_code.tex (Construction
A [E]), verification/v798_seam_clifford_modular_s.py (zeta8/Galois-
Hadamard-Bit [E], nur Pointer).

Lean-Begleiter: experiments/lean4-carrier-rigidity/TfptCarrier/
PacketRM14.lean (endlicher Kern, kernel decide / norm_num).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_packet_rm14_probe.py
"""

import itertools
import os
import sys
import time
from collections import Counter

_VERIFY = os.path.dirname(os.path.abspath(__file__))
_DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                          "tfpt-discovery"))
sys.path.insert(0, _DISCOVERY)
sys.path.insert(0, _VERIFY)

import v774_arf_spinor_compiler as v774  # noqa: E402  (read-only)

T0 = time.time()
CHECKS = []
KILLS = []
_LAST = {}


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ------------------------------------------------------------- setup
PTS = list(v774.NZ15)                       # frozen point order (15)
NPT = 15
ONES = (1 << NPT) - 1


def word_of(fn):
    """bitmask of the function fn on the frozen 15-point order."""
    m = 0
    for k, x in enumerate(PTS):
        if fn(x) % 2:
            m |= 1 << k
    return m


def wt(m):
    return bin(m).count("1")


def f2_span(gens):
    """full span set + rank via bitmask Gaussian elimination."""
    basis = []
    for g in gens:
        cur = g
        for b in basis:
            cur = min(cur, cur ^ b)
        if cur:
            basis.append(cur)
            basis.sort(reverse=True)
    span = {0}
    for b in basis:
        span |= {s ^ b for s in span}
    return span, len(basis)


def nullspace(gens):
    """basis of {w : <w, g> = 0 for all g} over F2 (bitmask words)."""
    A = [[(g >> k) & 1 for k in range(NPT)] for g in gens]
    pivots = []
    r = 0
    for c in range(NPT):
        piv = next((i for i in range(r, len(A)) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(len(A)):
            if i != r and A[i][c]:
                A[i] = [(a + b) % 2 for a, b in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(NPT) if c not in pivots]
    out = []
    for fc in free:
        vec = [0] * NPT
        vec[fc] = 1
        for i, pc in enumerate(pivots):
            vec[pc] = A[i][fc]
        out.append(sum(b << k for k, b in enumerate(vec)))
    return out


def enum(spanset):
    return dict(Counter(wt(w) for w in spanset))


# the certified structures
F_LIN = {v: word_of(lambda x, vv=v: v774.hb(vv, x)) for v in v774.W16}
C0 = set(F_LIN.values())                     # {hbar(v, .)}
C_AFF = C0 | {ONES ^ c for c in C0}          # plus affine bit
CHI = F_LIN[v774.FSIG]


# ==================================================================== S1
def s1_affine_code():
    section("S1: der affine Code -- Zeilenhuelle von B = RM(1,4)* = "
            "[15,5,7], C_0 = Simplex [15,4,8]")
    rowsB = [word_of(lambda x, yy=y: 1 + v774.hb(x, yy)) for y in PTS]
    ok_bbt = True
    for i, y in enumerate(PTS):
        for j, z in enumerate(PTS):
            e = wt(rowsB[i] & rowsB[j])
            if e != (7 if i == j else 3) + (0 if i != j else 0):
                # diagonal 7 = 4 + 3, off-diagonal 3
                ok_bbt = False
    check("S1.1 v752-Anker: Zeilen B_y(x) = 1 + hbar(x,y) haben "
          "Gewicht 7; B B^T = 4I + 3J ueber Z (Diagonale 7 = 4+3, "
          "sonst 3)",
          all(wt(r) == 7 for r in rowsB) and ok_bbt, kill="K1")

    hull, rank = f2_span(rowsB + [ONES ^ r for r in rowsB])
    check("S1.2 ZEILENHUELLE: span(B-Zeilen + Komplemente) hat "
          "Dimension %d == 5, 32 Woerter, und IST C_aff = "
          "{a + hbar(v, .)}" % rank,
          rank == 5 and hull == C_AFF and len(C_AFF) == 32, kill="K1")

    check("S1.3 GEWICHTS-ENUMERATOR (Zensus ueber alle 32): %s == "
          "{0: 1, 7: 15, 8: 15, 15: 1} -- 1 + 15z^7 + 15z^8 + z^15"
          % enum(C_AFF),
          enum(C_AFF) == {0: 1, 7: 15, 8: 15, 15: 1}, kill="K1")

    # independent RM(1,4)* construction from coordinates
    rm14 = set()
    for a in (0, 1):
        for lam in itertools.product((0, 1), repeat=4):
            rm14.add(word_of(
                lambda x, a=a, lam=lam:
                a + sum(l * xi for l, xi in zip(lam, x))))
    check("S1.4 RM-IDENTIFIKATION: C_aff == punktiertes RM(1,4) "
          "(affine Funktionen in Koordinaten, bei 0 punktiert) als "
          "MENGE -- Parameter [15,5,7], Minimalgewicht 7",
          rm14 == C_AFF
          and min(wt(w) for w in C_AFF if w) == 7, kill="K1")

    _, r0 = f2_span(sorted(C0))
    check("S1.5 C_0 = {hbar(v, .)} = [15,4,8] SIMPLEX: Dimension %d "
          "== 4, alle 15 Nichtnull-Woerter aequidistant Gewicht 8"
          % r0,
          r0 == 4 and len(C0) == 16
          and all(wt(w) == 8 for w in C0 if w), kill="K1")


# ==================================================================== S2
def s2_nsr_codeword():
    section("S2: NS/R als Codewort -- der 7+8-Split als affines Bit")
    ok_anchor = all(v774.hb(x, v774.FSIG) == x[3] for x in v774.W16)
    check("S2.1 chi_NSR = hbar(., F_Sigma) = das C_0-Wort von y0 = "
          "F_Sigma; chi(x) = x_3 (Anker-Bit, v752 P5.3/v774) -- "
          "Gewicht 8, Komplement 7: der 7+8-Split ist EIN RM-"
          "Codewort und seine zwei Seiten, das C2-Register ist das "
          "affine Bit a",
          CHI in C0 and wt(CHI) == 8 and (ONES ^ CHI) in C_AFF
          and wt(ONES ^ CHI) == 7 and ok_anchor, kill="K2")

    n_chi1 = sum(1 for x in PTS if v774.hb(x, v774.FSIG) == 1)
    check("S2.2 ZAEHLUNGEN: |C_aff| = 32 = 2*16 (affines Bit x "
          "Woerter); %d chi=1-Klassen x 16 Wurzeln/Klasse = 128 "
          "(R-Sektor, v752 [E]); 128 = 32*4 = |C_aff|*|mu4| "
          "(typisiert [H], Audit)" % n_chi1,
          len(C_AFF) == 32 == 2 * 16 and n_chi1 == 8
          and 8 * 16 == 128 == 32 * 4, kill="K2")


# ==================================================================== S3
def s3_cycle():
    section("S3: der Selbstreproduktions-Zyklus RM(1,3) -> E8 -> V -> "
            "RM(1,4)* -> RM(1,3)")
    # (i) RM(1,3) from scratch on F2^3
    pts8 = list(itertools.product((0, 1), repeat=3))
    rm13 = set()
    for a in (0, 1):
        for lam in itertools.product((0, 1), repeat=3):
            w = tuple((a + sum(l * x for l, x in zip(lam, p))) % 2
                      for p in pts8)
            rm13.add(w)
    enum13 = dict(Counter(sum(w) for w in rm13))
    check("S3.1 RM(1,3) = [8,4,4]: 16 Woerter, Enumerator %s == "
          "{0: 1, 4: 14, 8: 1}" % enum13,
          len(rm13) == 16 and enum13 == {0: 1, 4: 14, 8: 1},
          kill="K3")

    # (ii) deployed e8-hat: v774 C_NAIVE ([E] Construction A -> E8 cited)
    cn = v774.C_NAIVE
    enum_cn = dict(Counter(sum(w) for w in cn))
    n_equiv_cn = sum(
        1 for p in itertools.permutations(range(8))
        if all(tuple(w[p[k]] for k in range(8)) in cn for w in rm13))
    check("S3.2 DEPLOYETES e8-hat: C_NAIVE (v774/v752 G_NAIVE) ist "
          "[8,4,4] mit Enumerator {0:1, 4:14, 8:1}; Permutations-"
          "Aequivalenz-Zensus RM(1,3) -> C_NAIVE: %d Permutationen "
          "(erwartet |Aut| = 1344 > 0); Construction A e8-hat -> E8 "
          "zitiert [E] (v752-Kette, note_e8_gaussian_code)"
          % n_equiv_cn,
          len(cn) == 16 and enum_cn == {0: 1, 4: 14, 8: 1}
          and n_equiv_cn == 1344, kill="K3")

    # (iii) restriction to the anchor plane chi = 1
    plane = [x for x in v774.W16 if v774.hb(x, v774.FSIG) == 1]
    ok_coset = all(
        tuple((a + b + c) % 2 for a, b, c in zip(x, y, z)) in plane
        for x in plane for y in plane for z in plane)
    check("S3.3 ANKER-EBENE: chi_NSR = 1 hat 8 Punkte und ist ein "
          "affiner 3-Raum (abgeschlossen unter x+y+z)",
          len(plane) == 8 and ok_coset, kill="K3")

    def restrict(fn):
        return tuple(fn(x) % 2 for x in plane)

    restricted = set()
    kernel = set()
    for a in (0, 1):
        for v in v774.W16:
            w = restrict(lambda x, a=a, vv=v: a + v774.hb(vv, x))
            restricted.add(w)
            if not any(w):
                kernel.add((a, v))
    enum_r = dict(Counter(sum(w) for w in restricted))
    check("S3.4 RESTRIKTION: das eingeschraenkte Code-Bild hat 16 "
          "Woerter (Kern der Restriktion = {0, 1+chi}: %s == "
          "{(0, 0), (1, F_Sigma)}), Parameter [8,4,4], Enumerator %s "
          "== {0: 1, 4: 14, 8: 1}"
          % (sorted(kernel), enum_r),
          len(restricted) == 16
          and kernel == {(0, tuple([0, 0, 0, 0])), (1, v774.FSIG)}
          and enum_r == {0: 1, 4: 14, 8: 1}, kill="K3")

    n_equiv = sum(
        1 for p in itertools.permutations(range(8))
        if all(tuple(w[p[k]] for k in range(8)) in cn
               for w in restricted))
    check("S3.5 DER ZYKLUS SCHLIESST: das restringierte Code-Bild IST "
          "permutations-aequivalent zum deployeten e8-hat/RM(1,3) -- "
          "Zensus: %d Permutationen (= |Aut(RM(1,3))| = 1344); "
          "RM(1,3) -> E8 -> V -> RM(1,4)* -> RM(1,3) [E neu]"
          % n_equiv,
          n_equiv == 1344, kill="K3")


# ==================================================================== S4
def s4_css():
    section("S4: der CSS-Code [[15,1,3]] -- Dual, Checks, Logicals, "
            "Triorthogonalitaet")
    dual_basis = nullspace(sorted(C_AFF))
    dual, rdual = f2_span(dual_basis)
    enum_d = enum(dual)
    check("S4.1 DUAL C_1^perp = [15,10,4]: Dimension %d == 10, "
          "voller Zensus ueber alle 1024 Woerter: Enumerator %s == "
          "{0:1, 4:105, 6:280, 8:435, 10:168, 12:35} (Summe 1024); "
          "Minimalgewicht 4" % (rdual, enum_d),
          rdual == 10 and len(dual) == 1024
          and enum_d == {0: 1, 4: 105, 6: 280, 8: 435, 10: 168,
                         12: 35}
          and min(wt(w) for w in dual if w) == 4, kill="K4")

    # canonical monomial form: shortened RM(2,4) = span{x_i, x_i x_j}
    monos = []
    for i in range(4):
        monos.append(word_of(lambda x, i=i: x[i]))
    for i in range(4):
        for j in range(i + 1, 4):
            monos.append(word_of(lambda x, i=i, j=j: x[i] * x[j]))
    span_m, rank_m = f2_span(monos)
    check("S4.2 KANONISCHE FORM: C_1^perp == span{x_i (4), x_i x_j "
          "(6)} = verkuerztes RM(2,4) -- die 10 Monome sind eine "
          "exakte Basis (Rang %d)" % rank_m,
          rank_m == 10 and span_m == dual, kill="K4")

    gens_x = [F_LIN[tuple(1 if k == i else 0 for k in range(4))]
              for i in range(4)]
    _, rk_x = f2_span(gens_x)
    ok_css = all((C0 <= C_AFF)
                 for _ in (0,)) and all(
        wt(gx & wz) % 2 == 0 for gx in gens_x for wz in dual)
    check("S4.3 CSS-BEDINGUNGEN: C_0 subset C_1; alle X-Checks (4 "
          "Simplex-Generatoren, Rang %d) orthogonal zu allen Z-Checks"
          " (C_1^perp); 4 + 10 = 14 unabhaengige Checks => "
          "[[15, 15-14 = 1, d]] CSS" % rk_x,
          C0 <= C_AFF and ok_css and rk_x == 4
          and rk_x + rdual == 14 and 15 - 14 == 1, kill="K4")

    xbar = ONES ^ CHI
    e0 = (1, 0, 0, 0)
    e1 = (0, 1, 0, 0)
    e01 = (1, 1, 0, 0)
    zbar = 0
    for k, x in enumerate(PTS):
        if x in (e0, e1, e01):
            zbar |= 1 << k
    ok_zbar_c0perp = all(wt(zbar & c) % 2 == 0 for c in C0)
    ok_zbar_not = any(wt(zbar & c) % 2 == 1 for c in C_AFF)
    dX = min(wt(w) for w in C_AFF - C0)
    dZ = None
    c0perp, r0p = f2_span(nullspace(sorted(C0)))
    dZ = min(wt(w) for w in c0perp if w not in dual)
    check("S4.4 LOGICALS exakt: Xbar = 1 + chi (Gewicht 7, in C_1 \\ "
          "C_0); Zbar = {e0, e1, e0+e1} (Gewicht 3, in C_0^perp "
          "[Rang %d = 11, Hamming] \\ C_1^perp); <Xbar, Zbar> = %d "
          "== 1 (antikommutierend); dX = min wt(C_1 \\ C_0) = %d == 7"
          "; dZ = min wt(C_0^perp \\ C_1^perp) = %d == 3 => "
          "[[15,1,3]] mit logischen Distanzen (7, 3)"
          % (r0p, wt(xbar & zbar) % 2, dX, dZ),
          wt(xbar) == 7 and xbar in C_AFF and xbar not in C0
          and wt(zbar) == 3 and ok_zbar_c0perp and ok_zbar_not
          and zbar in c0perp and zbar not in dual
          and wt(xbar & zbar) % 2 == 1 and dX == 7 and dZ == 3
          and r0p == 11, kill="K4")

    # triorthogonality census
    singles = [wt(g) for g in gens_x]
    pairs = [wt(gens_x[i] & gens_x[j])
             for i in range(4) for j in range(i + 1, 4)]
    triples = [wt(gens_x[i] & gens_x[j] & gens_x[k])
               for i in range(4) for j in range(i + 1, 4)
               for k in range(j + 1, 4)]
    nz = sorted(C0 - {0})
    full_pairs = {wt(a & b) for a, b in itertools.combinations(nz, 2)}
    tri_indep, tri_dep = set(), set()
    for a, b, c in itertools.combinations(nz, 3):
        (tri_dep if (a ^ b) == c or (a ^ c) == b or (b ^ c) == a
         else tri_indep).add(wt(a & b & c))
    n_dep = sum(1 for a, b, c in itertools.combinations(nz, 3)
                if (a ^ b) == c)
    check("S4.5 TRIORTHOGONALITAET (Zensus): 4 Generator-Zeilen "
          "Gewichte %s == 8; 6 Paar-Overlaps %s == 4; 4 Tripel-"
          "Overlaps %s == 2; VOLLZENSUS: alle 105 Paare Overlap {4},"
          " unabhaengige Tripel (420) Overlap {2}, abhaengige Tripel "
          "(%d == 35) Overlap {0}"
          % (sorted(set(singles)), sorted(set(pairs)),
             sorted(set(triples)), n_dep),
          singles == [8] * 4 and pairs == [4] * 6
          and triples == [2] * 4 and full_pairs == {4}
          and tri_indep == {2} and tri_dep == {0} and n_dep == 35,
          kill="K4")
    print("    [H] ZETA8-POINTER: die Phasenstruktur der "
          "triorthogonalen Matrix (T-Gate/zeta8) bleibt typisiert "
          "[H] mit Verweis auf das zertifizierte Galois/Hadamard-Bit "
          "(v798_seam_clifford_modular_s); KEINE Identifikation "
          "behauptet.")


# ==================================================================== S5
def s5_fingerprints():
    section("S5: TFPT-Fingerabdruecke (typisiert [H], nur Audit)")
    dimG2, N_fam, mu4 = 14, 3, 4
    check("S5.1 [H] FINGERPRINTS (nur mitgefuehrt, keine Claims): "
          "14 unabhaengige CSS-Checks = dim G2 = %d; Distanz 3 = "
          "N_fam = %d; dX = 7; 4 = |mu4| = dim C_0 = Paar-Overlap; "
          "15 Labels = |PG(3,2)|" % (dimG2, N_fam),
          4 + 10 == dimG2 and 3 == N_fam and mu4 == 4 and NPT == 15)


# ==================================================================== C
def c_controls():
    section("C: Must-fail-Kontrollen")
    # C1: degenerate Gram (rank 3): zero out the anchor row/col
    def hb_bad(v, w):
        g = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
        return sum(v[i] * g[i][j] * w[j] for i in range(4)
                   for j in range(4)) % 2

    rows_bad = [word_of(lambda x, yy=y: 1 + hb_bad(x, yy)) for y in PTS]
    hull_bad, rank_bad = f2_span(rows_bad + [ONES ^ r for r in rows_bad])
    check("C1 KONTROLLE FEUERT (degenerierte Form, Rang-3-Gram): "
          "Huellen-Dimension %d != 5, Enumerator %s != frozen"
          % (rank_bad, enum(hull_bad)),
          rank_bad != 5 and enum(hull_bad)
          != {0: 1, 7: 15, 8: 15, 15: 1})
    print("    HONEST NOTE: jede NICHTDEGENERIERTE Form liefert "
          "dieselbe Code-MENGE (alle affinen Funktionale, basisfrei);"
          " die Kanonizitaet von hbar selbst ist v753's Zensus [E] "
          "-- die Kontrolle zielt daher auf Degeneriertheit.")

    # C2: scrambled deletion -- delete F_Sigma, keep 0
    pts_scr = [x for x in v774.W16 if x != v774.FSIG]

    def word_scr(fn):
        m = 0
        for k, x in enumerate(pts_scr):
            if fn(x) % 2:
                m |= 1 << k
        return m

    c0_scr = {word_scr(lambda x, vv=v: v774.hb(vv, x))
              for v in v774.W16}
    en_scr = dict(Counter(wt(w) for w in c0_scr))
    rows_scr = [word_scr(lambda x, yy=y: 1 + v774.hb(x, yy))
                for y in pts_scr if any(y)]
    ok_bbt_scr = all(
        wt(rows_scr[i] & rows_scr[j]) == (7 if i == j else 3)
        for i in range(len(rows_scr)) for j in range(len(rows_scr)))
    check("C2 KONTROLLE FEUERT (verwuerfelte Punkt-Loeschung: "
          "F_Sigma geloescht, 0 behalten): C_0 verliert die "
          "Aequidistanz (Enumerator %s, Gewichte {7,8} statt {8}); "
          "B B^T = 4I + 3J bricht (%s)"
          % (en_scr, not ok_bbt_scr),
          en_scr != {0: 1, 8: 15} and not ok_bbt_scr)

    # C3: a non-RM 5-dim code fails the distance-7 census
    gens3 = [0b111 << (3 * i) for i in range(5)]
    code3, r3 = f2_span(gens3)
    check("C3 KONTROLLE FEUERT (Nicht-RM 5-dim Code, fuenf disjunkte "
          "Gewicht-3-Zeilen): Dimension %d = 5, aber Minimalgewicht "
          "%d != 7 -- der Distanz-7-Zensus schlaegt fehl"
          % (r3, min(wt(w) for w in code3 if w)),
          r3 == 5 and min(wt(w) for w in code3 if w) == 3)


# ======================================================================
def main():
    print("=" * 78)
    print("PRIME.PACKET.RM14.01 -- die Reed-Muller-Identifikation des "
          "15-Label-Kanals")
    print("=" * 78, flush=True)
    s1_affine_code()
    s2_nsr_codeword()
    s3_cycle()
    s4_css()
    s5_fingerprints()
    c_controls()

    section("ZUSAMMENFASSUNG / VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    if KILLS or not controls_ok:
        verdict = "RM14-FALSE"
        print("VERDIKT: RM14-FALSE -- Kills: %s%s"
              % (sorted(set(KILLS)),
                 "" if controls_ok else " (+ Kontrolle feuert nicht)"))
    elif n_pass == n_all:
        verdict = "RM14-EXACT"
        print("VERDIKT: RM14-EXACT -- Zeilenhuelle = RM(1,4)* = "
              "[15,5,7] mit Enumerator 1+15z^7+15z^8+z^15, C_0 = "
              "Simplex [15,4,8], chi_NSR = EIN Codewort (7+8 = die "
              "zwei Seiten, C2 = affines Bit), der Zyklus RM(1,3) -> "
              "E8 -> V -> RM(1,4)* -> RM(1,3) schliesst exakt "
              "(1344 Aequivalenzen), CSS [[15,1,3]] mit Dual "
              "[15,10,4] (= verkuerztes RM(2,4)), logischen "
              "Distanzen (7,3) und Triorthogonalitaet (8/4/2).")
    else:
        verdict = "RM14-PARTIAL"
        print("VERDIKT: RM14-PARTIAL -- kein Kill, aber Nicht-Kill-"
              "Checks gescheitert; siehe FAIL-Zeilen.")
    _LAST["verdict"] = verdict
    print("Verdikt-Enum: %s" % verdict)
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


def run():
    """run_all entry point (v757 precedent): expected pattern 21/21 with
    verdict RM14-EXACT."""
    rc = main()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    fails = [n.split()[0] for n, ok in CHECKS if not ok]
    ok = (rc == 0 and n_pass == len(CHECKS) == 21 and not fails
          and _LAST.get("verdict") == "RM14-EXACT")
    print("\n[%s] PATTERN GATE: expected 21/21 with verdict RM14-EXACT; "
          "got %d/%d, fails: %s, verdict: %s"
          % ("PASS" if ok else "FAIL", n_pass, len(CHECKS),
             fails or "none", _LAST.get("verdict")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
