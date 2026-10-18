#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v821 -- PRIME.VACUUM35.01: the vacuum completion of the parity checks -- 140 = 105 + 35, the E7 spectral completion 112 + 21 = 133 as a matrix identity, the Weitzenboeck left factor, and the exact +-B cross-term cancellation, one probe (22/22 checks incl. the 3 must-fire controls, ~0.3 s; discovery probe prime_vacuum35_probe.py, 2026-08-06, verdict VACUUM35-EXACT).  S1: RM(2,4) = [16,11,4] (census over all 2048 codewords); its 140 weight-4 words are EXACTLY the indicators of the 140 affine 2-planes of V (35 linear subspaces = [4 choose 2]_2, each with 4 distinct cosets); shortening at the zero coordinate removes exactly the 35 planes through 0: 140 = 105 + 35.  S2 (counting lemmas FIRST, then entrywise): planes through a fixed point 35 / 7 linear / 28 non-origin, through a pair 7 / 1 / 6; H105^T H105 = 22I + 6J (spectrum {112, 22^14} exact charpoly), H35^T H35 = 6I + J ({21, 6^14}), sum = 28I + 7J ({133, 28^14}); COMPLETIONS 112 + 21 = 133 = dim E7 and 22 + 6 = 28 as matrix identities [E neu] -- the E7 x A1 corpus reading 248 = 133 + 3 + 112 typed [C] FINGERPRINT with anchor v170 (dim E7 = 133 also v79/v463/v532).  S3 WEITZENBOECK: H105^T H105 = 2 B^2 + 14 I EXACTLY (via the certified B^2 = 4I + 3J) -- R_label = H105 is a canonical LABEL-SIDE left factor with every row a named plane indicator; HONEST SCOPE: v758 / PRIME.CERTROOT.01's wall (the missing left factor for the CONTINUUM(+atoms) Schur cascade) stands UNTOUCHED -- this supplies the incidence/Stinespring layer where v758's 105 Kraus terms live; continuum, cell order and lag structure are NOT included.  S4 THE CROSS-TERM MECHANISM: the 35 origin planes split 15 totally isotropic (the GQ(2,2) lines) + 20 non-isotropic with H+^T H+ = 2I + B (charpoly (x-9)(x-4)^9 x^5) and H-^T H- = 4I + J - B ((x-12)(x-6)^5(x-2)^9) ENTRYWISE -- the +-B ANISOTROPY CANCELS inside ONE Gram (structural contrast to the killed v758 additive-block certificate: the completion acts on the SAME 15-point label algebra, not as a separate orthogonal block; typed [H] reading, the matrix identities are the content).  S5 TIGHT FRAME: H140^T H140 = 28 I_16 + 7 J_16 (charpoly (x-140)(x-28)^15), so the 140 plane indicators form a TIGHT FRAME with frame constant 28 on the mean-zero space (census: sum_P <chi_P, e_i - e_j>^2 = 56 for all 120 pairs), while the unprojected system is NOT tight; 'self-dual-ish' made exact: F2-rank 11 = dim RM(2,4) (the minimum-weight words generate) and RM(2,4)^perp = RM(1,4) is CONTAINED in RM(2,4) -- DUAL-CONTAINING, not self-dual.  Controls fire (affine 3-flats number 30 != 140 with the wrong Gram, scrambled incidence breaks 22I + 6J entrywise, deleting a NONZERO coordinate with the split kept at 0 breaks Gram and spectrum -- with the frozen honest note that '0' is pinned only relative to the split).  'Vacuum/continuum' stays [H]; ROOTCLASS-MIXED (v775) stands; no marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe prime_vacuum35_probe.py (2026-08-06, 22/22, ~0.3 s, VACUUM35-EXACT); re-run identically at promotion.  Promoted verbatim (self-contained; sympy gated to charpolys); a module-level _LAST verdict capture inserted (v791 precedent); numbers unchanged; run() encodes the pattern (v757 precedent).

Original prime_vacuum35_probe.py docstring (verbatim):
prime_vacuum35_probe -- PRIME.VACUUM35.01 (K5 round follow-up,
cut-code strand): the vacuum completion of the parity checks -- the
140 = 105 + 35 plane split of RM(2,4), its incidence Grams with the
E7 spectral completion 112 + 21 = 133, the Weitzenboeck identity
H105^T H105 = 2 B^2 + 14 I as the LABEL-side left factor, the +-B
cross-term cancellation of the iso/non-iso split, and the tight-frame
statement of the full 140-plane system.

SETTING.  V = F2^4 with the certified symplectic form hbar (Gram
J - I in the family/anchor basis; abstract layer == lattice layer on
all 256 pairs, v774 S1.4).  B = [hbar(x,y) = 0] on the 15 nonzero
points is the certified projective Hamming incidence with
B^2 = B B^T = 4I + 3J and charpoly (x-7)(x-2)^9(x+2)^5 (v752/v774).
RM(2,4) = [16, 11, 4] is the order-2 Reed--Muller code on the 16
points of V.  All matrix computations exact (integers; sympy gated
for charpolys only).

FROZEN CLAIMS (BEFORE running; kill bars below):
 S1  THE 140 = 105 + 35 SPLIT: RM(2,4) has parameters [16, 11, 4]
     (census over all 2^11 codewords); its weight-4 words are EXACTLY
     the indicators of the 140 affine 2-planes of V (set equality);
     Gaussian binomial [4 choose 2]_2 = 35 linear 2-subspaces, each
     with 4 cosets, 35 * 4 = 140 distinct planes; 35 through 0 (= the
     linear ones) + 105 not; shortening RM(2,4) at the zero
     coordinate removes exactly the 35 planes through 0 (the
     weight-4 words with 0 not in the support are the 105).
 S2  THE INCIDENCE GRAMS (counting lemmas FIRST, then entrywise):
     lemmas -- planes through a fixed nonzero point: 35; linear ones
     through it: 7; non-origin: 28; planes through a fixed pair: 7;
     linear: 1; non-origin: 6.  Then, on the 15 nonzero coordinates:
       H105^T H105 = 22 I + 6 J,  spectrum {112, 22^14};
       H35^T H35  =  6 I +   J,  spectrum {21,   6^14};
       sum H140'^T H140' = 28 I + 7 J,  spectrum {133, 28^14}.
     COMPLETIONS: 112 + 21 = 133 = dim E7 and 22 + 6 = 28 -- matrix
     identities [E neu]; the E7 x A1 corpus reading 248 = 133 + 3 +
     112 typed [C] FINGERPRINT with anchor v170 (E7xA1 slice; 112 =
     detR detC off-block; dim E7 = 133 also v79/v463/v532).
 S3  WEITZENBOECK IDENTITY: H105^T H105 = 2 B^2 + 14 I EXACTLY (via
     the certified B^2 = 4I + 3J).  R_label = H105 is a canonical
     LEFT FACTOR on the 15-point LABEL algebra: R_label^T R_label =
     2 B^2 + 14 I with every row a named plane indicator.  HONEST
     SCOPE (v758 wall cited): v758 / PRIME.CERTROOT.01 killed the
     [continuum root (+) Kraus] certificate -- the wall IS the
     missing left factor for the CONTINUUM(+atoms) Schur cascade
     (arch+pol nowhere PSD, additive S = S^cont + Delta dead, rescue
     strictly cell-ordered).  THIS probe supplies the LABEL-SIDE
     factor only: the incidence/Stinespring layer where v758's 105
     Kraus terms live.  Continuum, cell order and lag structure are
     NOT included; v758's precise negative stands untouched.
 S4  THE CROSS-TERM MECHANISM (recomputed independently of the
     parallel planeframes probe): split the 35 origin planes by
     isotropy of hbar: 15 totally isotropic (the GQ(2,2) lines) + 20
     non-isotropic; then ENTRYWISE
       H+^T H+ = 2 I + B          (charpoly (x-9)(x-4)^9 x^5),
       H-^T H- = 4 I + J - B      (charpoly (x-12)(x-6)^5(x-2)^9),
     and the sum is 6 I + J: the +-B ANISOTROPY CANCELS.  STRUCTURAL
     CONTRAST to the killed continuum-root certificate (typed): v758
     demanded an ADDITIVE POSITIVE block on a different (continuum)
     space -- dead; here the 35-completion acts on the SAME 15-point
     label algebra and repairs the anisotropy through the +-B cross
     terms INSIDE one Gram, not as a separate orthogonal block.
 S5  TIGHT-FRAME STATEMENT (unshortened, all 16 coordinates):
     H140^T H140 = 28 I_16 + 7 J_16 entrywise, charpoly
     (x-140)(x-28)^15; hence the 140 plane indicators form a TIGHT
     FRAME with frame constant 28 on the 15-dim mean-zero space
     1-perp (census: sum_P <chi_P, e_i - e_j>^2 = 56 for all 120
     pairs); the UNPROJECTED system is NOT tight (Gram != c I) --
     stated exactly.  Self-duality is 'ish' only: F2-rank of the 140
     indicators = 11 = dim RM(2,4) (the minimum-weight words
     generate), and RM(2,4)^perp = RM(1,4) (dim 5) is CONTAINED in
     RM(2,4) -- dual-containing, not self-dual (exact F2 checks).

MUST-FAIL CONTROLS (frozen):
 C1  wrong plane census: affine 3-flats number [4 choose 3]_2 * 2 =
     30 != 140, and their non-origin incidence Gram on the 15 points
     is NOT of the form 22I + 6J.
 C2  scrambled incidence: deterministically moving one point out of
     one plane of H105 breaks the Gram identity entrywise.
 C3  removing a NONZERO coordinate instead of 0 (split kept at 0):
     restricting H105 / H35 to the 15 coordinates V \ {p} for the
     frozen p = F1-label breaks both Gram identities and the spectra
     (H105 gets an all-zero column at 0).  HONEST NOTE (frozen): pure
     shortening at p WITH the split moved to p is translation-
     isomorphic to the 0 case (affine transitivity); the control
     tests the MISMATCH of split point vs deleted coordinate -- '0'
     is pinned only relative to the split.

KILLS (frozen):
 K1  RM census / plane identification / 140 = 105 + 35 split fails.
 K2  a counting lemma, a Gram identity (S2 or S4) or a spectrum
     deviates entrywise.
 K3  (-> PARTIAL, not DEAD) the Weitzenboeck factorisation (S3) or
     the tight-frame/duality statements (S5) fail while S1/S2/S4
     hold.
VERDICTS (frozen): VACUUM35-EXACT (all green, controls fire) /
VACUUM35-PARTIAL (S1+S2+S4 green, S3 or S5 fails) / VACUUM35-DEAD
(K1 or K2 fires) / TEST-VOID (a control does not fire).

FENCES: ROOTCLASS-MIXED (v775) untouched -- nothing here is a matter
split; NO RH claim; the 'vacuum/continuum' reading is [H] -- the
matrix identities are the content; the E7 reading is a [C]
fingerprint, not a derivation.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Ganzzahl/F2-Arithmetik; sympy nur fuer charpolys
(gated); keine Floats, kein RNG, kein Fit, kein freier Parameter.

Sources (read-only): verification/v774_arf_spinor_compiler.py (hbar
abstract layer == lattice, B, B^2 = 4I + 3J, charpoly),
verification/v752_projective_hamming_incidence.py (incidence),
verification/v758_simpler_certificate.py (PRIME.CERTROOT.01, the
missing-left-factor wall, CERT-CONTINUUM-ROOT-DEAD),
verification/v170_diamond_slice_compression.py (E7xA1: 248 = 133 +
3 + 112), v79/v463/v532 (dim E7 = 133), verification/v775 (ROOTCLASS-
MIXED fence).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_vacuum35_probe.py
"""

import itertools
import time
from collections import Counter

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


# ======================================================================
# certified abstract layer (v774 conventions)
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]  # J - I


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def xor(v, w):
    return tuple((a + b) % 2 for a, b in zip(v, w))


ZERO4 = (0, 0, 0, 0)
NZ15 = sorted(w for w in W16 if any(w))
PIDX = {p: i for i, p in enumerate(NZ15)}
B15 = [[1 if hb(x, y) == 0 else 0 for y in NZ15] for x in NZ15]


def mat_eq(A, Bm):
    return all(A[i][j] == Bm[i][j]
               for i in range(len(A)) for j in range(len(A[0])))


def aI_bJ(a, b, n):
    return [[a + b if i == j else b for j in range(n)] for i in range(n)]


def gram_cols(planes, cols):
    """G[i][j] = # planes containing both cols[i] and cols[j]."""
    n = len(cols)
    G = [[0] * n for _ in range(n)]
    for P in planes:
        idx = [k for k, c in enumerate(cols) if c in P]
        for a in idx:
            for b in idx:
                G[a][b] += 1
    return G


def charpoly_is(M, factors):
    """exact: charpoly(M) == prod (x - lam)^mult (sympy, gated)."""
    import sympy as sp
    x = sp.symbols("x")
    cp = sp.Matrix(M).charpoly(x).as_expr()
    target = sp.expand(sp.prod((x - lam) ** m for lam, m in factors))
    return sp.expand(cp - target) == 0


# ======================================================================
# S1 -- the 140 = 105 + 35 split
# ======================================================================
def rm24_codewords():
    """all 2^11 codewords of RM(2,4) as 16-bit tuples over W16."""
    monos = [tuple(1 for _ in W16)]                       # 1
    for i in range(4):
        monos.append(tuple(v[i] for v in W16))            # x_i
    for i, j in itertools.combinations(range(4), 2):
        monos.append(tuple(v[i] * v[j] for v in W16))     # x_i x_j
    words = set()
    for mask in range(1 << 11):
        w = [0] * 16
        for k in range(11):
            if (mask >> k) & 1:
                w = [(a + b) % 2 for a, b in zip(w, monos[k])]
        words.add(tuple(w))
    return words


def s1_split():
    section("S1: RM(2,4) = [16,11,4]; 140 weight-4 words = the affine "
            "2-planes; 140 = 105 + 35")
    subspaces = set()
    for x, y in itertools.combinations(NZ15, 2):
        subspaces.add(frozenset({ZERO4, x, y, xor(x, y)}))
    gauss42 = (15 * 14) // (3 * 2)
    check("S1.1 linear 2-subspaces of V: %d == 35 = [4 choose 2]_2 = "
          "15*14/(3*2)" % len(subspaces),
          len(subspaces) == 35 and gauss42 == 35, kill="K1")

    planes = set()
    for U in subspaces:
        for u in W16:
            planes.add(frozenset(xor(u, x) for x in U))
    per_sub = Counter()
    for U in subspaces:
        per_sub[U] = len({frozenset(xor(u, x) for x in U) for u in W16})
    check("S1.2 affine 2-planes: %d == 140 = 35 * 4 (each subspace has "
          "exactly 4 cosets, all distinct)" % len(planes),
          len(planes) == 140 and set(per_sub.values()) == {4}, kill="K1")

    words = rm24_codewords()
    wt4 = {w for w in words if sum(w) == 4}
    minwt = min(sum(w) for w in words if any(w))
    supp4 = {frozenset(W16[i] for i in range(16) if w[i]) for w in wt4}
    check("S1.3 RM(2,4) census: 2^11 = %d distinct codewords (dim 11), "
          "min weight %d == 4, weight-4 words %d == 140, and their "
          "supports are EXACTLY the 140 planes (set equality)"
          % (len(words), minwt, len(wt4)),
          len(words) == 2048 and minwt == 4 and len(wt4) == 140
          and supp4 == planes, kill="K1")

    through0 = {P for P in planes if ZERO4 in P}
    not0 = planes - through0
    check("S1.4 SHORTENING AT 0: planes through 0 = %d == 35 (= the "
          "linear subspaces exactly) + %d == 105 not through 0; the "
          "weight-4 words surviving the shortening (0 not in support) "
          "are exactly the 105" % (len(through0), len(not0)),
          len(through0) == 35 and through0 == subspaces
          and len(not0) == 105
          and sum(1 for w in wt4 if W16.index(ZERO4) not in
                  [i for i in range(16) if w[i]]) == 105, kill="K1")
    return subspaces, sorted(not0, key=lambda P: sorted(P)), planes


# ======================================================================
# S2 -- counting lemmas, Grams, spectra, E7 completion
# ======================================================================
def s2_grams(subspaces, planes105, planes_all):
    section("S2: counting lemmas -> incidence Grams -> spectra -> "
            "E7 completion 112 + 21 = 133")
    thr_p = {p: sum(1 for P in planes_all if p in P) for p in NZ15}
    lin_p = {p: sum(1 for U in subspaces if p in U) for p in NZ15}
    non_p = {p: sum(1 for P in planes105 if p in P) for p in NZ15}
    ok_pts = (set(thr_p.values()) == {35} and set(lin_p.values()) == {7}
              and set(non_p.values()) == {28})
    thr_pq = lin_pq = non_pq = True
    for p, q in itertools.combinations(NZ15, 2):
        if sum(1 for P in planes_all if p in P and q in P) != 7:
            thr_pq = False
        if sum(1 for U in subspaces if p in U and q in U) != 1:
            lin_pq = False
        if sum(1 for P in planes105 if p in P and q in P) != 6:
            non_pq = False
    check("S2.1 COUNTING LEMMAS: through a point 35 / 7 linear / 28 "
          "non-origin; through a pair 7 / 1 linear / 6 non-origin "
          "(census over all 15 points and 105 pairs)",
          ok_pts and thr_pq and lin_pq and non_pq, kill="K2")

    G105 = gram_cols(planes105, NZ15)
    check("S2.2 H105^T H105 == 22 I + 6 J ENTRYWISE (all 225 cells)",
          mat_eq(G105, aI_bJ(22, 6, 15)), kill="K2")
    check("S2.3 spectrum of H105^T H105 = {112, 22^14} (exact charpoly)",
          charpoly_is(G105, [(112, 1), (22, 14)]), kill="K2")

    G35 = gram_cols(subspaces, NZ15)
    check("S2.4 H35^T H35 == 6 I + J ENTRYWISE; spectrum {21, 6^14}",
          mat_eq(G35, aI_bJ(6, 1, 15))
          and charpoly_is(G35, [(21, 1), (6, 14)]), kill="K2")

    G140 = [[G105[i][j] + G35[i][j] for j in range(15)]
            for i in range(15)]
    G140_direct = gram_cols(planes_all, NZ15)
    check("S2.5 SUM: H140'^T H140' == 28 I + 7 J ENTRYWISE (= G105 + "
          "G35, and directly); spectrum {133, 28^14}",
          mat_eq(G140, aI_bJ(28, 7, 15)) and mat_eq(G140, G140_direct)
          and charpoly_is(G140, [(133, 1), (28, 14)]), kill="K2")

    check("S2.6 COMPLETIONS [E neu identities]: 112 + 21 = %d == 133 "
          "= dim E7 and 22 + 6 = 28; corpus reading 248 = 133 + 3 + "
          "112 (E7 x A1) typed [C] FINGERPRINT, anchor v170 (E7xA1 "
          "slice, 112 = detR detC off-block; dim E7 = 133 in "
          "v79/v463/v532)" % (112 + 21),
          112 + 21 == 133 and 22 + 6 == 28
          and 133 + 3 + 112 == 248, kill="K2")
    return G105


# ======================================================================
# S3 -- the Weitzenboeck identity and its honest scope
# ======================================================================
def s3_weitzenboeck(G105):
    section("S3: Weitzenboeck H105^T H105 = 2 B^2 + 14 I -- the "
            "LABEL-side left factor (v758 scope typed)")
    B2 = [[sum(B15[i][k] * B15[k][j] for k in range(15))
           for j in range(15)] for i in range(15)]
    check("S3.1 certified incidence reproduced: B^2 == 4 I + 3 J "
          "ENTRYWISE and charpoly(B) = (x-7)(x-2)^9(x+2)^5 "
          "(v752/v774)",
          mat_eq(B2, aI_bJ(4, 3, 15))
          and charpoly_is(B15, [(7, 1), (2, 9), (-2, 5)]), kill="K3")

    lhs_ok = mat_eq(G105, [[2 * B2[i][j] + (14 if i == j else 0)
                            for j in range(15)] for i in range(15)])
    check("S3.2 WEITZENBOECK: H105^T H105 == 2 B^2 + 14 I ENTRYWISE -- "
          "R_label = H105 is a canonical left factor: R^T R = "
          "2 B^2 + 14 I with every row a NAMED plane indicator",
          lhs_ok, kill="K3")

    print("    HONEST SCOPE (v758 / PRIME.CERTROOT.01, CERT-CONTINUUM-"
          "ROOT-DEAD):")
    print("    * v758's wall is the missing left factor for the "
          "CONTINUUM(+atoms) Schur")
    print("      cascade: arch+pol nowhere PSD, additive S = S^cont + "
          "Delta dead on all")
    print("      stages, rescue strictly cell-ordered.")
    print("    * THIS identity supplies the LABEL-SIDE factor only -- "
          "the incidence/")
    print("      Stinespring layer where v758's 105 Kraus terms "
          "V_xy = 7^{-1/2}|y><x| live.")
    print("    * Continuum, cell order and lag structure are NOT "
          "included; v758's precise")
    print("      negative stands untouched.  Typed honestly: a named "
          "PSD factorisation on")
    print("      the 15-point label algebra, not the missing "
          "certificate factor.")


# ======================================================================
# S4 -- the cross-term mechanism (+-B cancellation)
# ======================================================================
def s4_cross_terms(subspaces):
    section("S4: iso/non-iso split of the 35 -- H+^T H+ = 2I + B, "
            "H-^T H- = 4I + J - B, sum 6I + J (+-B cancels)")
    iso = [U for U in subspaces
           if all(hb(x, y) == 0 for x in U for y in U)]
    noniso = [U for U in subspaces if U not in iso]
    check("S4.1 ISOTROPY CENSUS: 35 = %d totally isotropic (the "
          "GQ(2,2) lines) + %d non-isotropic == 15 + 20"
          % (len(iso), len(noniso)),
          len(iso) == 15 and len(noniso) == 20, kill="K2")

    Gp = gram_cols(iso, NZ15)
    tgt_p = [[2 * (1 if i == j else 0) + B15[i][j] for j in range(15)]
             for i in range(15)]
    check("S4.2 H+^T H+ == 2 I + B ENTRYWISE; charpoly "
          "(x-9)(x-4)^9 x^5",
          mat_eq(Gp, tgt_p) and charpoly_is(Gp, [(9, 1), (4, 9), (0, 5)]),
          kill="K2")

    Gm = gram_cols(noniso, NZ15)
    tgt_m = [[4 * (1 if i == j else 0) + 1 - B15[i][j]
              for j in range(15)] for i in range(15)]
    check("S4.3 H-^T H- == 4 I + J - B ENTRYWISE; charpoly "
          "(x-12)(x-6)^5(x-2)^9",
          mat_eq(Gm, tgt_m)
          and charpoly_is(Gm, [(12, 1), (6, 5), (2, 9)]), kill="K2")

    Gsum = [[Gp[i][j] + Gm[i][j] for j in range(15)] for i in range(15)]
    check("S4.4 SUM == 6 I + J ENTRYWISE: the +-B ANISOTROPY CANCELS "
          "between the two sub-blocks of the SAME Gram",
          mat_eq(Gsum, aI_bJ(6, 1, 15)), kill="K2")

    print("    STRUCTURAL CONTRAST (typed, [H] reading -- the matrix "
          "identities are the")
    print("    content): the killed v758 certificate demanded an "
          "ADDITIVE POSITIVE")
    print("    continuum block on a DIFFERENT space (S = S^cont + "
          "Delta, Delta >= 0 --")
    print("    dead, all stages indefinite).  The 35-completion acts "
          "on the SAME 15-point")
    print("    label algebra: the anisotropic blocks 2I + B and 4I + "
          "J - B repair each")
    print("    other through the +-B cross terms INSIDE one Gram -- "
          "NOT as a separate")
    print("    orthogonal block.")


# ======================================================================
# S5 -- tight-frame statement on all 16 coordinates
# ======================================================================
def s5_tight_frame(planes_all):
    section("S5: the full 140-plane system -- tight frame on 1-perp, "
            "dual-containing (not self-dual)")
    G16 = gram_cols(planes_all, W16)
    check("S5.1 H140^T H140 == 28 I_16 + 7 J_16 ENTRYWISE; spectrum "
          "{140, 28^15}; trace 16*35 = 560 = 140 + 28*15",
          mat_eq(G16, aI_bJ(28, 7, 16))
          and charpoly_is(G16, [(140, 1), (28, 15)])
          and 16 * 35 == 560 == 140 + 28 * 15, kill="K3")

    ok_frame = True
    for i, j in itertools.combinations(range(16), 2):
        s = sum((int(W16[i] in P) - int(W16[j] in P)) ** 2
                for P in planes_all)
        if s != 56:
            ok_frame = False
    check("S5.2 TIGHT FRAME on 1-perp with constant 28: sum_P "
          "<chi_P, e_i - e_j>^2 == 56 = 28 * |e_i - e_j|^2 for ALL "
          "120 pairs (census); the UNPROJECTED system is NOT tight "
          "(Gram != c I: diag 35, off-diag 7)", ok_frame, kill="K3")

    # F2 structure: rank 11, dual = RM(1,4) contained in RM(2,4)
    rows = [[1 if W16[i] in P else 0 for i in range(16)]
            for P in planes_all]
    basis = []
    for r in rows:
        r = r[:]
        for b in basis:
            piv = next(i for i, a in enumerate(b) if a)
            if r[piv]:
                r = [(a + c) % 2 for a, c in zip(r, b)]
        if any(r):
            basis.append(r)
    words = rm24_codewords()
    rm14 = set()
    monos1 = [tuple(1 for _ in W16)] + \
        [tuple(v[i] for v in W16) for i in range(4)]
    for mask in range(1 << 5):
        w = [0] * 16
        for k in range(5):
            if (mask >> k) & 1:
                w = [(a + b) % 2 for a, b in zip(w, monos1[k])]
        rm14.add(tuple(w))
    ok_dual = all(sum(a * b for a, b in zip(u, w)) % 2 == 0
                  for u in rm14 for w in words)
    check("S5.3 'self-dual-ish' made exact: F2-rank of the 140 "
          "indicators = %d == 11 = dim RM(2,4) (minimum-weight words "
          "generate); RM(1,4) (dim 5, 32 words) is orthogonal to ALL "
          "of RM(2,4) and contained in it: RM(2,4)^perp = RM(1,4) "
          "(11 + 5 = 16) -- DUAL-CONTAINING, not self-dual"
          % len(basis),
          len(basis) == 11 and len(rm14) == 32 and ok_dual
          and rm14 <= words and 11 + 5 == 16, kill="K3")


# ======================================================================
# C -- must-fail controls
# ======================================================================
def c_controls(planes105):
    section("C: must-fail controls")
    # C1: 3-flats instead of 2-flats
    subs3 = set()
    for x, y, z in itertools.combinations(NZ15, 3):
        span = {ZERO4, x, y, z, xor(x, y), xor(x, z), xor(y, z),
                xor(xor(x, y), z)}
        if len(span) == 8:
            subs3.add(frozenset(span))
    flats3 = set()
    for U in subs3:
        for u in W16:
            flats3.add(frozenset(xor(u, x) for x in U))
    non0_3 = [P for P in flats3 if ZERO4 not in P]
    G3 = gram_cols(non0_3, NZ15)
    check("C1 CONTROL FIRES: affine 3-flats number %d == 30 != 140 "
          "([4 choose 3]_2 * 2 = 15 * 2), and their non-origin Gram "
          "(diag %d) is NOT 22I + 6J"
          % (len(flats3), G3[0][0]),
          len(flats3) == 30 and len(non0_3) == 15
          and not mat_eq(G3, aI_bJ(22, 6, 15)))

    # C2: scrambled incidence -- move one point out of one plane
    P0 = planes105[0]
    p_in = sorted(P0)[0]
    p_out = next(p for p in NZ15 if p not in P0)
    scrambled = [frozenset(P0 - {p_in} | {p_out})] + planes105[1:]
    Gs = gram_cols(scrambled, NZ15)
    check("C2 CONTROL FIRES: moving one point out of one plane breaks "
          "H105^T H105 == 22I + 6J entrywise",
          not mat_eq(Gs, aI_bJ(22, 6, 15)))

    # C3: delete a NONZERO coordinate, split kept at 0
    p_del = NZ15[0]
    cols = [w for w in W16 if w != p_del]     # 15 coords incl. 0
    G105d = gram_cols(planes105, cols)
    zero_col = cols.index(ZERO4)
    ok3 = (not mat_eq(G105d, aI_bJ(22, 6, 15))
           and G105d[zero_col][zero_col] == 0
           and not charpoly_is(G105d, [(112, 1), (22, 14)]))
    check("C3 CONTROL FIRES: deleting the nonzero coordinate %s "
          "instead of 0 (split kept at 0) gives an all-zero column at "
          "0, breaks the Gram identity AND the spectrum" % (p_del,),
          ok3)
    print("    HONEST NOTE (frozen): pure shortening at p WITH the "
          "split moved to p is")
    print("    translation-isomorphic to the 0 case (affine "
          "transitivity); the control")
    print("    tests the MISMATCH of split point vs deleted "
          "coordinate -- '0' is pinned")
    print("    only relative to the split.")


# ======================================================================
def main():
    print("=" * 78)
    print("PRIME.VACUUM35.01 -- the vacuum completion of the parity "
          "checks and its E7 structure")
    print("=" * 78, flush=True)
    subspaces, planes105, planes_all = s1_split()
    G105 = s2_grams(subspaces, planes105, planes_all)
    s3_weitzenboeck(G105)
    s4_cross_terms(subspaces)
    s5_tight_frame(planes_all)
    c_controls(planes105)

    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    core_kills = [k for k in KILLS if k in ("K1", "K2")]
    soft_kills = [k for k in KILLS if k == "K3"]
    print("%d/%d checks passed" % (n_pass, n_all))
    if not controls_ok:
        verdict = "TEST-VOID"
        print("VERDICT: TEST-VOID -- a must-fail control does not fire; "
              "the test measures nothing.")
    elif core_kills:
        verdict = "VACUUM35-DEAD"
        print("VERDICT: VACUUM35-DEAD -- core kills fired: %s"
              % sorted(set(core_kills)))
    elif soft_kills:
        verdict = "VACUUM35-PARTIAL"
        print("VERDICT: VACUUM35-PARTIAL -- split + Grams + cross-term "
              "exact, but Weitzenboeck or tight-frame/duality failed.")
    else:
        verdict = "VACUUM35-EXACT"
        print("VERDICT: VACUUM35-EXACT -- RM(2,4) weight-4 words = the "
              "140 affine 2-planes, split 140 = 105 + 35 at the zero "
              "coordinate; Grams 22I + 6J / 6I + J / 28I + 7J with "
              "spectra {112, 22^14} / {21, 6^14} / {133, 28^14} and "
              "the E7 completion 112 + 21 = 133, 22 + 6 = 28 "
              "[identities E neu; E7 x A1 reading a [C] fingerprint, "
              "anchor v170]; Weitzenboeck H105^T H105 = 2 B^2 + 14 I "
              "(label-side left factor ONLY -- v758's continuum wall "
              "untouched); the +-B anisotropy of the iso/non-iso "
              "blocks cancels inside one Gram (no additive orthogonal "
              "block); the 140-plane system is a tight frame with "
              "constant 28 on 1-perp and RM(2,4) is dual-containing "
              "(RM(1,4) = dual). 'Vacuum/continuum' stays [H]; "
              "ROOTCLASS-MIXED (v775) stands; no RH claim.")
    _LAST["verdict"] = verdict
    print("Verdict enum: %s" % verdict)
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


def run():
    """run_all entry point (v757 precedent): expected pattern 22/22 with
    verdict VACUUM35-EXACT."""
    rc = main()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    fails = [n.split()[0] for n, ok in CHECKS if not ok]
    ok = (rc == 0 and n_pass == len(CHECKS) == 22 and not fails
          and _LAST.get("verdict") == "VACUUM35-EXACT")
    print("\n[%s] PATTERN GATE: expected 22/22 with verdict "
          "VACUUM35-EXACT; got %d/%d, fails: %s, verdict: %s"
          % ("PASS" if ok else "FAIL", n_pass, len(CHECKS),
             fails or "none", _LAST.get("verdict")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
