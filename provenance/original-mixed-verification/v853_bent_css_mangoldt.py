#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v853 -- ARF.BENT.CSS.01 + PRIME.RELATION.MANGOLDT.01: the bent phase layer with its two CSS codes and the von Mangoldt commutator theorem -- the -4 becomes ONE machine-checked integer seen three independent ways (Hecke = Gauss = Walsh), the register carries [[15,5,3]] -> [[16,4,4]] with the vacuum transformation typed, and the deployed relational carrier is identified as the first row of the exact incidence-algebra commutator L = -M[D,Z] = -[D, log Z], ONE module from two probes (22/22 + 30/30 checks, zero fails, verdicts ARF-BENT-CSS-EXACT and MANGOLDT-COMMUTATOR-EXACT; discovery probes arf_bent_css_probe.py and mangoldt_incidence_probe.py, 2026-08-07, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, <1 s).  PART A, THE BENT PHASE CODE: (a) the canonical q* is BENT -- the phase vector s_q = (-1)^{q*} is a Walsh eigenvector, s_q-hat = -4 s_q on ALL 16 characters (W^2 = 16 I; perfect autocorrelation sum_x s_q(x+a) s_q(x+b) = 16 delta_{a,b} on all 256 pairs); (b) the zero set D_q = {0} u 5bar is a (16,6,2) HADAMARD DIFFERENCE SET (|D_q ^ (D_q + a)| = 2 for all 15 shifts; the five carrier slots have iota-weight 4; the 5bar is the doily ovoid); (c) A_q = C_iso^perp = <simplex, q*> = [15,5,6] with the 31-WORD STRUCTURAL CENSUS: the 15 weight-8 words ARE the linear characters, the 10 weight-6 the Arf-0 refinements, the 6 weight-10 the Arf-1 refinements (set equalities); (d) TWO CSS CODES: A_q c C_iso self-orthogonal gives [[15,5,3]] (distance words = the 15 doily lines); A_16 = RM(1,4) + <q*> = [16,6,6] self-orthogonal inside C_16 = A_16^perp = [16,10,4] gives [[16,4,4]] whose 60 minimal words are EXACTLY the 60 isotropic affine planes -- the s_Arf = 0 rows of the v852 syndrome table; (e) THE VACUUM TRANSFORMATION typed: shortening A_16 at the vacuum slot == A_q, puncturing C_16 == C_iso -- one physical slot added, one logical qubit paid, distance 3 -> 4 bought; (f) THE -4 TRIPLE POINT (one statement, three independent computations): the local Hecke count 12 - 16 = -4 (all 15 points re-counted) == the bent Gauss sum -2^{4/2} == the Walsh eigenvalue == a_3 (eta product); v785's 32 = 28 - (-4) is the gap between the two Walsh eigenvalue lines scaled by the register -- the cusp projector denominator is the bent spectral gap; (g) the 16 bent translates form a second Gram-16I frame MUTUALLY UNBIASED against the 16 characters (all 256 cross products = +-4 = sqrt(16)) -- the unbiased partner of v800's torsor Fourier rays, REPORTED with no upgrade.  Controls fire: an Arf-0 refinement flips the Walsh sign (+4, zero set 10, no (16,6,2) set); the dot form has no bent seed and its self-orthogonal [16,6,6] extension dies (dim 5 != 6).  PART B, THE VON MANGOLDT COMMUTATOR THEOREM (typed classical incidence-algebra content -- the value is the packaging and the discipline transport, NOT new mathematics): (1) L_N := -M[D,Z] == T(Lambda) verified EXACTLY three ways (sympy log-integer basis at N = 60 on all 261 divisor pairs, integer/Fraction layer at N = 360 on all 2186 pairs, scipy float ward 5.3e-15 at N = 10^4 on 93668 pairs), with the ONE-LINE PROOF termwise (mu * log = Lambda) and the per-prime commutator [V_p, Z] = -Z E_p == Chebyshev's identity prime by prime; (2) THE POWER/CHAIN FORMULA: (L^k)_{a,b} enumerates ordered factorization chains into prime powers with weight prod Lambda(r_j) (verified exactly at k = 2, 3); nilpotency degree floor(log2 N) + 1 (at N = 10^4: L^13 has nnz 1 at (1, 8192) with value (log 2)^13, L^14 = 0); (3) THE LOG: log Z is RATIONAL (entry 1/k at ratio p^k), exp(log Z) == Z in exact Fractions, and L = -Z^{-1}[D,Z] = -[D, log Z] EXACTLY because the BCH series truncates ([log Z, [log Z, D]] = 0) -- kappa = Lambda/log as a rational matrix; (4) THE FOUR-COMB DISCIPLINE AT OPERATOR LEVEL: the commutator machine ALWAYS outputs T(Lambda_f) (T is an algebra isomorphism from Dirichlet convolution) -- Selberg consistency is a SUPPORT statement: TRUE / chi4-twist / zeta_{Q(i)} (scalar AND ideal-level: 237 ideals of Z[i], Dedekind Lambda_K, norm aggregation == (1 + chi4) Lambda) are exactly prime-power-supported, while the h = 2 Epstein comb LEAKS at [6, 14, 21, ...] (33 sites <= 360; first unramified site 21 = 3 x 7, both factors non-principal; values pinned exactly, Lambda_A(6) = 2 log 6, Lambda_A(21) = 4 log 21) and the leak is REPAIRED by the class average (a_A + a_B = 1 * chi_{-20}, off-prime-power support EMPTY; the class-convolution law verified on all coprime pairs) -- the operator-level discriminator localizes the class-group obstruction; (5) THE CARRIER BRIDGE: the deployed Moebius-pairing reconstruction at TRUE positions is LITERALLY the first row of L_N (per-divisor term equality for EVERY d | m, m <= 360), the deployed pairing matrix is a sub-block of M = Z^{-1}, rows are shifts of row one (L[a, ab] = L[1, b]), and L^2 - [D, L] = T(mu * log^2) -- the untapped structure is the Selberg hierarchy, which v855 then audits for supply.  NO RH claim (nothing here bounds zeros).  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes arf_bent_css_probe.py (22/22, verdict
ARF-BENT-CSS-EXACT) and mangoldt_incidence_probe.py (30/30, verdict
MANGOLDT-COMMUTATOR-EXACT), both 2026-08-07, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: both frozen probe sources
are embedded BYTE-EXACT (raw strings below) and executed verbatim in
isolated module namespaces -- the printed FROZEN_SPEC SHA-256 values
reproduce exactly, and when the original files are present the
harness verifies byte-equality (provenance ward inside the pattern
gate).  The pattern gates encode the frozen expected censuses (22 +
30 checks, zero FAILs, both verdicts, exit 0).  The original probe
files live verbatim in experiments/tfpt-discovery/.

FIREWALL: part A is pure finite algebra over F_2 (carrier rebuilt
from scratch, tfpt_constants only); part B builds its own sieves --
the divisor/mu arithmetic is the admissible Euler-product datum, no
zeta zeros, no prime-table symbols (the probe carries and passes its
own AST firewall); no RNG outside the declared frozen-seed controls.
NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_BENT = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arf_bent_css_probe -- ARF.BENT.CSS.01: the bent phase code and the
two CSS codes.  The phase vector s_q = (-1)^{q*} is a bent function
with Walsh identity s_q-hat = -4 s_q (the Gauss sum -2^{4/2} = -4 as
an eigenvalue equation), its zero set is a (16,6,2) Hadamard
difference set {0} u ovoid, the linear span A_q = <V*, q*> = [15,5,6]
is self-orthogonal inside C_iso and yields the CSS code [[15,5,3]],
the 16-slot extension A_16 = RM(1,4) + <q*> = [16,6,6] yields
[[16,4,4]] whose dual's 60 minimal words are EXACTLY the 60 isotropic
affine planes, and the Hecke difference a_3 = -4, the Gauss sum and
the Walsh eigenvalue are ONE machine-checked integer (finite-geometry
module 3 of the 2026-08-07 evening code-complex round).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; all
statements verified over ALL objects, never samples; exact integer/F2
arithmetic; no floats, no RNG, no fits):

 S1  CARRIER: corpus form hb (J - I Gram), 16 refinements (2^16
     census), Arf 6 + 10, selector-unique q* (Arf 1); five = {q*=0}
     \{0} (the ovoid), ten = {q*=1}; s_q(x) = (-1)^{q*(x)}.

 S2  (a) THE GAUSS-SUM / WALSH IDENTITY:
     (i)  the one-line identity q*(x) + hb(a,x) = q*(x+a) + q*(a)
          holds on ALL 256 pairs (the derivation identity re-read);
     (ii) the exact integer Walsh transform obeys s_q-hat(a) =
          sum_x s_q(x) (-1)^{hb(a,x)} = -4 * s_q(a) for ALL 16 a --
          s_q is a Walsh EIGENVECTOR with eigenvalue -4 (bent,
          extremal); W^2 = 16 I for the character matrix W;
     (iii) perfect autocorrelation sum_x s_q(x+a) s_q(x+b) =
          16 delta_{a,b} on ALL 256 pairs.

 S3  (b) THE DIFFERENCE SET: D_q = {q* = 0} has 6 elements = {0} u
     the five carrier points (each of iota-weight 4 -- identified
     against the five-slot structure; the 5bar meets every doily
     line exactly once); |D_q n (D_q + a)| = 2 for ALL 15 a != 0 --
     the (16,6,2) Hadamard difference set.

 S4  (c) THE PHASE CODE A_q = C_iso^perp = <V*, q*> = [15,5,6]:
     A_q = span{hb(v,.)|_NZ} + <q*|_NZ> has dim 5, weight enumerator
     1 + 10z^6 + 15z^8 + 6z^10, min distance 6; A_q == C_iso^perp
     (set equality, C_iso = the Arf-kernel [15,10,3] of the Hamming
     code, probe-1 pencil); THE 31-WORD SEMANTIC CENSUS, each class
     identified STRUCTURALLY (set equalities, not counts): the 15
     weight-8 words ARE the linear characters hb(v,.), the 10
     weight-6 words ARE the Arf-0 (even) refinement indicators, the
     6 weight-10 words ARE the Arf-1 (odd/ovoid) refinement
     indicators.

 S5  (d1) CSS CODE ONE: A_q c A_q^perp = C_iso (self-orthogonality,
     all 32 x 32 pairs even) => [[15, 5, 3]] with k = 15 - 2*5 =
     dim C_iso - dim A_q = 5 and d = 3: the coset minimum is
     realized by the 15 explicit weight-3 isotropic-line words of
     C_iso (set equality), none of which lies in A_q (min weight 6),
     and C_iso has NO weight-1 or weight-2 word.

 S6  (d2) CSS CODE TWO: A_16 = RM(1,4) + <q*> = [16,6,6] with weight
     enumerator 1 + 16z^6 + 30z^8 + 16z^10 + z^16, SELF-ORTHOGONAL;
     dual C_16 = A_16^perp = [16,10,4] = {c in RM(2,4) : c.q* = 0}
     (set equality); the 60 minimal (weight-4) words of C_16 are
     EXACTLY the 60 isotropic affine planes = 15 through the origin
     + 45 off (SET EQUALITY -- the syndrome-table cross-link: these
     are precisely the s_Arf = 0 rows of probe 1) => [[16, 4, 4]]
     with k = 16 - 2*6 = 4 and d = 4 (weight-4 words exist in C_16
     and none lies in A_16).

 S7  (d3) THE VACUUM TRANSFORMATION [[15,5,3]] -> [[16,4,4]] typed:
     shortening A_16 at the vacuum coordinate == A_q and puncturing
     C_16 == C_iso (set equalities); one physical slot added
     (n 15 -> 16), one logical qubit paid (k 5 -> 4), distance
     bought (d 3 -> 4).

 S8  (e) THE -4 TRIPLE POINT, one machine-checked statement:
     (i)   Hecke: the per-point plane census (12 isotropic - 16
           non-isotropic off-origin planes through x, re-counted at
           ALL 15 points) gives A_3 - B_3 = -4 = a_3 (eta product
           rebuilt inline; v820 S4.2 (G3) / v535 corpus anchors);
     (ii)  Gauss: sum_x s_q(x) = 6 - 10 = -4 = -2^{4/2};
     (iii) Walsh: the eigenvalue of s_q under W is -4 (S2);
     all three integers computed independently and asserted EQUAL.
     THE 16-TRANSLATE HADAMARD BASIS vs the corpus torsor Fourier
     basis (v800, integer Gram 16 I, mutually-unbiased honest cap):
     the translates T_t = s_q(. + t) have Gram EXACTLY 16 I (an
     orthogonal Hadamard basis, same normalization as v800's rays),
     and are MUTUALLY UNBIASED against the 16 characters
     (-1)^{hb(u,.)}: ALL 256 cross inner products = +-4 = sqrt(16)
     -- the translate basis does NOT reproduce the character rays,
     it is their unbiased complement (typed REPORT, v800 cited).

 C   CONTROLS (must fire; frozen fire rules):
     C1 ARF-0 REFINEMENT q0: the Walsh identity flips sign,
        s_q0-hat = +4 s_q0 on ALL 16 (eigenvalue +4), and the zero
        set is NOT a (16,6,2) set: |{q0=0}| = 10 with all 15
        intersection sizes = 6 (the complementary (16,10,6) set --
        census printed).
     C2 DOT FORM: zero quadratic refinements (2^16 census) -- no
        bent seed exists; the direction bit is ill-defined (witness
        U = <e1,e2>); and the dot-side parity surrogate collapses:
        wt(x) mod 2 IS the linear character x1+x2+x3+x4 in RM(1,4),
        so span(RM(1,4) + <parity>) has dim 5 != 6 -- NO sixth
        generator, no [16,6,6], the self-orthogonal extension dies.

KILLS (any one fires => typed failure):
  K1 Walsh / Gauss / autocorrelation identity breaks -> WALSH-BROKEN
  K2 the (16,6,2) difference set breaks              -> DIFFSET-BROKEN
  K3 A_q census / dual / semantic identification     -> CODE-CENSUS-BROKEN
  K4 a CSS ingredient ([[15,5,3]] / [[16,4,4]])      -> CSS-BROKEN
  K5 the vacuum shorten/puncture map breaks          -> VACUUM-MAP-BROKEN
  K6 the -4 triple point / 16I / MUB check breaks    -> TRIPLE-POINT-BROKEN
  K7 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): ARF-BENT-CSS-EXACT / WALSH-BROKEN /
DIFFSET-BROKEN / CODE-CENSUS-BROKEN / CSS-BROKEN / VACUUM-MAP-BROKEN /
TRIPLE-POINT-BROKEN / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/F2 arithmetic; no floats, no RNG,
no fits.  NO physics claim.

Sources (read-only, machinery rebuilt inline):
affine_arf_vacuum_probe.py (H / C_iso pencil, syndrome table, local
Hecke counts), finite_compiler_normal_form_probe.py +
cfin_uniqueness_probe.py (q*, selector, iota), v819 (RM landscape),
v820 S4.2 (G3) + v535 + v785 (a_3 = -4 anchors), v800 (torsor Fourier
rays, 16 I Gram, mutually-unbiased cap), v774/v752 (form +
refinements), tfpt_constants (g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/arf_bent_css_probe.py
"""
import hashlib
import itertools
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "verification"))
from tfpt_constants import g_car  # noqa: E402  (read-only import)

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("ARF.BENT.CSS.01 -- bent phase code + the two CSS codes")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ------------------------------------------------------- bit machinery
PTS = list(range(16))
NZ = list(range(1, 16))


def pc(v):
    return bin(v).count("1")


def hb(v, w):
    return ((pc(v) & 1) & (pc(w) & 1)) ^ (pc(v & w) & 1)


HBT = [[hb(v, w) for w in PTS] for v in PTS]
DOT = [[pc(v & w) & 1 for w in PTS] for v in PTS]


def refinements_of(tab):
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            row = tab[i]
            for j in range(16):
                if q[i ^ j] ^ qi ^ q[j] != row[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def sig_int(v):
    b = [(v >> k) & 1 for k in range(4)]
    w = (b[2], b[0], b[1], b[3])
    return sum(w[k] << k for k in range(4))


def span_bits(gens):
    S_ = {0}
    for g in gens:
        S_ |= {s ^ g for s in S_}
    return S_


# ======================================================================
section("S1: carrier -- q*, five/ten, the phase vector s_q")
# ======================================================================
REFS = refinements_of(HBT)
ARF1 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 6)
ARF0 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 10)
siginv = [q for q in REFS if all(q[sig_int(v)] == q[v] for v in PTS)]
cand = [q for q in siginv if q[8] == 1 and q[7] == 0]
check("S1.1 16 refinements, Arf 6 + 10, selector-unique q* (Arf 1)",
      len(REFS) == 16 and len(ARF1) == 6 and len(ARF0) == 10
      and len(cand) == 1 and cand[0] in ARF1, kill="K1")
QS = cand[0]
FIVE = [v for v in NZ if QS[v] == 0]
TEN = [v for v in NZ if QS[v] == 1]
S = [1 - 2 * QS[x] for x in PTS]        # s_q = (-1)^{q*}
check("S1.2 five = %d = g_car carrier points, ten = %d; s_q takes "
      "value +1 on 6 and -1 on 10 slots" % (len(FIVE), len(TEN)),
      len(FIVE) == 5 == g_car and len(TEN) == 10
      and S.count(1) == 6 and S.count(-1) == 10, kill="K1")

# ======================================================================
section("S2: (a) the Gauss-sum / Walsh identity s_q-hat = -4 s_q")
# ======================================================================
check("S2.1 one-line identity q*(x) + hb(a,x) == q*(x+a) + q*(a) on "
      "ALL 256 pairs",
      all((QS[x] + HBT[a][x]) % 2 == (QS[x ^ a] + QS[a]) % 2
          for a in PTS for x in PTS), kill="K1")
WHAT = [sum(S[x] * (1 - 2 * HBT[a][x]) for x in PTS) for a in PTS]
W2 = [[sum((1 - 2 * HBT[a][x]) * (1 - 2 * HBT[x][b]) for x in PTS)
       for b in PTS] for a in PTS]
check("S2.2 WALSH EIGENVECTOR: s_q-hat(a) == -4 * s_q(a) for ALL 16 "
      "a (values %s); W^2 == 16 I (256 cells)"
      % sorted(set(WHAT)),
      all(WHAT[a] == -4 * S[a] for a in PTS)
      and all(W2[a][b] == (16 if a == b else 0)
              for a in PTS for b in PTS), kill="K1")
check("S2.3 PERFECT AUTOCORRELATION: sum_x s_q(x+a) s_q(x+b) == "
      "16 delta_{a,b} on ALL 256 pairs",
      all(sum(S[x ^ a] * S[x ^ b] for x in PTS)
          == (16 if a == b else 0) for a in PTS for b in PTS),
      kill="K1")

# ======================================================================
section("S3: (b) the (16,6,2) Hadamard difference set D_q = {q*=0}")
# ======================================================================
DQ = {v for v in PTS if QS[v] == 0}
SUBS = sorted({frozenset({0, u, v, u ^ v})
               for u, v in itertools.combinations(NZ, 2)}, key=sorted)
UBIT = {U: min(HBT[a][b] for a, b in
               itertools.combinations(sorted(U - {0}), 2))
        for U in SUBS}
ISO = [U for U in SUBS if UBIT[U] == 0]
check("S3.1 D_q = {0} u five (|D_q| = %d == 6 = g_car + 1); each of "
      "the five has iota-weight 4 (the 5bar slot structure); the "
      "5bar meets every doily line exactly once (ovoid)" % len(DQ),
      DQ == {0} | set(FIVE)
      and all(pc(v) + (pc(v) & 1) == 4 for v in FIVE)
      and all(sum(1 for x in U - {0} if x in FIVE) == 1 for U in ISO),
      kill="K2")
inter = sorted(len(DQ & {d ^ a for d in DQ}) for a in NZ)
check("S3.2 |D_q n (D_q + a)| == 2 for ALL 15 a != 0 (census %s) -- "
      "the (16,6,2) Hadamard difference set"
      % sorted(set(inter)), inter == [2] * 15, kill="K2")

# ======================================================================
section("S4: (c) A_q = C_iso^perp = <V*, q*> = [15,5,6] + census")
# ======================================================================


def xor_pts(m):
    s = 0
    while m:
        b = m & -m
        s ^= b.bit_length()
        m ^= b
    return s


def wmask(pts_set):
    return sum(1 << (x - 1) for x in pts_set)


H = [m for m in range(1 << 15) if xor_pts(m) == 0]
TENM = wmask(TEN)
CISO = [m for m in H if pc(m & TENM) % 2 == 0]
SIMP15 = {wmask({x for x in NZ if HBT[v][x] == 1}) for v in NZ}
AQ = span_bits([wmask({x for x in NZ if HBT[v][x] == 1})
                for v in (1, 2, 4, 8)] + [TENM])
weA = Counter(pc(m) for m in AQ)
check("S4.1 A_q = span{hb(v,.)} + <q*>: dim 5 (|A_q| = %d == 32), "
      "weight enumerator %s == 1 + 10z^6 + 15z^8 + 6z^10, min "
      "distance 6 -> [15,5,6]"
      % (len(AQ), dict(sorted(weA.items()))),
      len(AQ) == 32 and dict(weA) == {0: 1, 6: 10, 8: 15, 10: 6},
      kill="K3")


def bit_basis(vs):
    basis = []
    for v in vs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    return basis


CB = bit_basis(CISO)
DUAL_CISO = {w for w in range(1 << 15)
             if all(pc(w & b) % 2 == 0 for b in CB)}
check("S4.2 A_q == C_iso^perp (set equality; dim 10 + dim 5 = 15)",
      DUAL_CISO == AQ and len(CB) == 10, kill="K3")

refvec = {q: wmask({x for x in NZ if q[x] == 1}) for q in REFS}
w8 = {m for m in AQ if pc(m) == 8}
w6 = {m for m in AQ if pc(m) == 6}
w10 = {m for m in AQ if pc(m) == 10}
check("S4.3 THE 31-WORD SEMANTIC CENSUS (structural set equalities): "
      "15 weight-8 words == the linear characters hb(v,.); 10 "
      "weight-6 == the Arf-0 (even) refinements; 6 weight-10 == the "
      "Arf-1 (odd/ovoid) refinements",
      w8 == SIMP15 and w6 == {refvec[q] for q in ARF0}
      and w10 == {refvec[q] for q in ARF1}, kill="K3")

# ======================================================================
section("S5: (d1) CSS one: A_q c C_iso => [[15,5,3]]")
# ======================================================================
sC = set(CISO)
ISO3 = {wmask(U - {0}) for U in ISO}
check("S5.1 SELF-ORTHOGONALITY: A_q c A_q^perp = C_iso (all 32 words "
      "in C_iso; all 32 x 32 pairs have even overlap)",
      AQ <= sC and all(pc(a & b) % 2 == 0 for a in AQ for b in AQ),
      kill="K4")
check("S5.2 [[15,5,3]]: k = 15 - 2*5 = %d == dim C_iso - dim A_q; "
      "d = 3: weight-3 words of C_iso == the 15 doily lines (set "
      "equality), NONE in A_q (min wt 6), and C_iso has NO weight-1/2 "
      "word" % (15 - 2 * 5),
      15 - 2 * 5 == 5 == 10 - 5
      and {m for m in CISO if pc(m) == 3} == ISO3
      and not (ISO3 & AQ)
      and not any(pc(m) in (1, 2) for m in CISO if m), kill="K4")

# ======================================================================
section("S6: (d2) CSS two: A_16 = RM(1,4) + <q*> => [[16,4,4]]")
# ======================================================================


def m16(pts_set):
    return sum(1 << v for v in pts_set)


QM16 = m16(set(TEN))
rm1_gens = [0xFFFF] + [m16({v for v in PTS if (v >> k) & 1})
                       for k in range(4)]
A16 = span_bits(rm1_gens + [QM16])
weA16 = Counter(pc(w) for w in A16)
gens6 = rm1_gens + [QM16]
check("S6.1 A_16 = RM(1,4) + <q*> = [16,6,6]: |A_16| = %d == 64, "
      "enumerator %s == 1 + 16z^6 + 30z^8 + 16z^10 + z^16; "
      "SELF-ORTHOGONAL (all 64 x 64 pairs even)"
      % (len(A16), dict(sorted(weA16.items()))),
      len(A16) == 64
      and dict(weA16) == {0: 1, 6: 16, 8: 30, 10: 16, 16: 1}
      and all(pc(a & b) % 2 == 0 for a in A16 for b in A16),
      kill="K4")

C16 = [w for w in range(1 << 16)
       if all(pc(w & g) % 2 == 0 for g in gens6)]
rm2_gens = rm1_gens + [m16({v for v in PTS
                            if ((v >> k) & 1) and ((v >> l) & 1)})
                       for k, l in itertools.combinations(range(4), 2)]
RM2 = span_bits(rm2_gens)
check("S6.2 C_16 = A_16^perp = [16,10,4]: |C_16| = %d == 1024, min "
      "wt %d == 4; C_16 == {c in RM(2,4) : c.q* = 0} (set equality); "
      "A_16 c C_16"
      % (len(C16), min(pc(w) for w in C16 if w)),
      len(C16) == 1024 and min(pc(w) for w in C16 if w) == 4
      and set(C16) == {c for c in RM2 if pc(c & QM16) % 2 == 0}
      and A16 <= set(C16), kill="K4")

FLAT16_ISO = set()
for U in SUBS:
    if UBIT[U] != 0:
        continue
    for cs in {frozenset(t ^ u for u in U) for t in PTS}:
        FLAT16_ISO.add(m16(cs))
w4C = {w for w in C16 if pc(w) == 4}
n_orig = sum(1 for w in FLAT16_ISO if w & 1)
check("S6.3 THE 60 MINIMAL WORDS: weight-4 words of C_16 == the 60 "
      "isotropic affine planes (SET EQUALITY; %d through origin + %d "
      "off = the s_Arf = 0 rows of the probe-1 syndrome table)"
      % (n_orig, len(FLAT16_ISO) - n_orig),
      w4C == FLAT16_ISO and len(FLAT16_ISO) == 60
      and n_orig == 15 and len(FLAT16_ISO) - n_orig == 45,
      kill="K4")
check("S6.4 [[16,4,4]]: k = 16 - 2*6 = %d; d = 4 (weight-4 words in "
      "C_16 \\ A_16: %d of them, A_16 min weight 6)"
      % (16 - 2 * 6, len(w4C - A16)),
      16 - 2 * 6 == 4 and len(w4C - A16) == 60
      and min(pc(w) for w in A16 if w) == 6, kill="K4")

# ======================================================================
section("S7: (d3) the vacuum transformation [[15,5,3]] -> [[16,4,4]]")
# ======================================================================
SHORT_A16 = {w >> 1 for w in A16 if not (w & 1)}
PUNC_C16 = {w >> 1 for w in C16}
check("S7.1 shorten(A_16) at the vacuum slot == A_q (set equality, "
      "%d words); puncture(C_16) == C_iso (set equality, %d words)"
      % (len(SHORT_A16), len(PUNC_C16)),
      SHORT_A16 == AQ and PUNC_C16 == sC and len(PUNC_C16) == 1024,
      kill="K5")
check("S7.2 typed parameters: one physical slot added (15 -> 16), "
      "one logical qubit paid (5 -> 4), distance bought (3 -> 4)",
      16 - 15 == 1 and 5 - 4 == 1 and 4 - 3 == 1
      and (15, 5, 3)[1] - 1 == (16, 4, 4)[1]
      and (15, 5, 3)[2] + 1 == (16, 4, 4)[2], kill="K5")

# ======================================================================
section("S8: (e) the -4 triple point + the 16-translate basis")
# ======================================================================
FLATS = []
for U in SUBS:
    for cs in {frozenset(t ^ u for u in U) for t in PTS}:
        FLATS.append((U, cs))
ok_pp = True
for x in NZ:
    off = [(U, cs) for U, cs in FLATS if x in cs and 0 not in cs]
    n_iso = sum(1 for U, cs in off if UBIT[U] == 0)
    if not (n_iso == 12 and len(off) - n_iso == 16):
        ok_pp = False


def eta_f8_a(n_max):
    c = [0] * (n_max + 1)
    c[0] = 1
    for step in (2, 4):
        for m in range(step, n_max + 1, step):
            for _ in range(4):
                for j in range(n_max, m - 1, -1):
                    c[j] -= c[j - m]
    a = [0] * (n_max + 2)
    for n in range(1, n_max + 2):
        if n - 1 <= n_max:
            a[n] = c[n - 1]
    return a


A3ETA = eta_f8_a(10)[3]
gauss = sum(S)
eigen = set(WHAT[a] * S[a] for a in PTS)  # {-4 * s^2} = {-4}
check("S8.1 THE -4 TRIPLE POINT (one statement, three independent "
      "computations): Hecke 12 - 16 = %d (all 15 points re-counted) "
      "== Gauss sum %d = -2^{4/2} == Walsh eigenvalue %s == a_3 = %d "
      "(eta; v820 S4.2 (G3), v535, v785 anchors)"
      % (12 - 16, gauss, sorted(eigen), A3ETA),
      ok_pp and 12 - 16 == -4 and gauss == -4
      and eigen == {-4} and A3ETA == -4 and -(2 ** 2) == -4,
      kill="K6")

T = [[S[x ^ t] for x in PTS] for t in PTS]
gramT = [[sum(T[t][x] * T[u][x] for x in PTS) for u in PTS]
         for t in PTS]
CHAR = [[1 - 2 * HBT[u][x] for x in PTS] for u in PTS]
cross = [[sum(T[t][x] * CHAR[u][x] for x in PTS) for u in PTS]
         for t in PTS]
check("S8.2 16-TRANSLATE HADAMARD BASIS: Gram(T) == 16 I EXACTLY "
      "(256 cells; v800's ray normalization reproduced); MUTUALLY "
      "UNBIASED against the 16 characters: ALL 256 cross products "
      "= +-4 = sqrt(16) (values %s) -- the translate basis "
      "complements, does NOT reproduce, the corpus character rays "
      "(v800 cited: torsor Fourier Gram 16 I, weight/character "
      "mutually unbiased)"
      % sorted({abs(cross[t][u]) for t in PTS for u in PTS}),
      all(gramT[t][u] == (16 if t == u else 0)
          for t in PTS for u in PTS)
      and all(abs(cross[t][u]) == 4 for t in PTS for u in PTS),
      kill="K6")

# ======================================================================
section("C: controls (must fire)")
# ======================================================================
Q0 = ARF0[0]
S0 = [1 - 2 * Q0[x] for x in PTS]
WH0 = [sum(S0[x] * (1 - 2 * HBT[a][x]) for x in PTS) for a in PTS]
D0 = {v for v in PTS if Q0[v] == 0}
inter0 = sorted(len(D0 & {d ^ a for d in D0}) for a in NZ)
check("C1 FIRES: Arf-0 refinement: Walsh SIGN FLIPS, s_q0-hat == "
      "+4 s_q0 on ALL 16 (eigenvalue +4 != -4); zero set |D0| = %d "
      "!= 6 with intersections %s == all-6 (the complementary "
      "(16,10,6) set) -- NO (16,6,2) set"
      % (len(D0), sorted(set(inter0))),
      all(WH0[a] == 4 * S0[a] for a in PTS) and len(D0) == 10
      and inter0 == [6] * 15, kill="K7")

refs_dot = refinements_of(DOT)
PARM = m16({v for v in PTS if pc(v) & 1})
RM1 = span_bits(rm1_gens)
check("C2 FIRES: dot form: %d == 0 refinements (no bent seed); "
      "direction bit ill-defined on U = <e1,e2> (dot pair values "
      "(%d,%d) differ); parity surrogate wt mod 2 == the character "
      "x1+x2+x3+x4 IN RM(1,4) (%s), so span(RM(1,4)+<parity>) has "
      "dim %d != 6 -- no sixth generator, the self-orthogonal "
      "[16,6,6] extension dies on the dot side"
      % (len(refs_dot), DOT[1][2], DOT[1][3],
         PARM in RM1,
         len(bit_basis(sorted(RM1 | {PARM})))),
      len(refs_dot) == 0 and (DOT[1][2], DOT[1][3]) == (0, 1)
      and PARM in RM1
      and len(bit_basis(sorted(RM1 | {PARM}))) == 5, kill="K7")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "WALSH-BROKEN", "K2": "DIFFSET-BROKEN",
               "K3": "CODE-CENSUS-BROKEN", "K4": "CSS-BROKEN",
               "K5": "VACUUM-MAP-BROKEN",
               "K6": "TRIPLE-POINT-BROKEN"}.get(KILLS[0],
                                                "CONTROL-DEAD")
else:
    VERDICT = "ARF-BENT-CSS-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * THE -4 IS ONE NUMBER: v820/v535's Hecke a_3 = -4, the "
      "bent Gauss sum")
print("    -2^{4/2} and the Walsh eigenvalue of the q* phase vector "
      "are the SAME")
print("    machine-checked integer; v785's 32 = 28 - (-4) is the "
      "gap between the")
print("    two Walsh eigenvalue lines +-4 scaled by the 16-slot "
      "register -- the")
print("    cusp projector denominator is the bent spectral gap.")
print("  * v819's RM landscape gains the PHASE layer: A_q = "
      "C_iso^perp = [15,5,6]")
print("    (simplex + q*), self-orthogonal => [[15,5,3]]; the "
      "vacuum slot upgrade")
print("    A_16 = RM(1,4)+<q*> = [16,6,6] => [[16,4,4]] whose dual "
      "minimal words")
print("    are EXACTLY the 60 isotropic planes -- the s_Arf = 0 "
      "rows of the")
print("    probe-1 syndrome table (v821/v834's 45 + the 15 doily "
      "lines).")
print("  * v800's torsor Fourier rays (Gram 16 I) get their "
      "unbiased partner: the")
print("    16 bent translates form a second 16 I frame, all cross "
      "products +-4 --")
print("    a character/bent MUB pair on the 16-slot register "
      "(reported, no upgrade).")
print("  * the (16,6,2) Hadamard difference set {0} u 5bar is the "
      "arithmetic face")
print("    of the ovoid: vacuum + five carrier slots, pairwise "
      "translate overlap 2.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "ARF-BENT-CSS-EXACT") else 1)
'''

_SRC_MANGOLDT = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mangoldt_incidence_probe -- PRIME.RELATION.MANGOLDT.01
(EXPLORATION ONLY, experiments/; module 4 of the 2026-08-07 evening
code-complex: the VON MANGOLDT COMMUTATOR THEOREM -- Lambda as the
commutator of the divisibility operator, verified exactly, powered,
generalized along the four-comb discipline, and bridged to the
deployed relational carrier of PRIME.RELATION.MULT.01).

THE THEOREM (verify exactly, then generalize): for 1 <= a, b <= N
with the divisibility incidence Z_{a,b} = 1_{a|b} (unitriangular,
det 1), its integer inverse M = Z^{-1} = [1_{a|b} mu(b/a)], and
D = diag(log 1, ..., log N):

    L_N := -M [D, Z]     has entries    (L_N)_{a,b} = Lambda(b/a)

for a | b and 0 otherwise (Lambda(1) = 0 covers a = b).  The one-line
proof IS the Moebius-log identity: (M[D,Z])_{a,an} = sum_{e|n} mu(e)
(log(ae) - log(an)) = sum_{e|n} mu(e)(log e - log n) = -Lambda(n):
the generic log a cancels TERMWISE, and the classical pair
sum_{e|n} mu(e) log e = -Lambda(n), sum_{e|n} mu(e) = delta_{n,1}
finishes.  This is classical incidence-algebra arithmetic (mu * log
= Lambda in matrix clothes) -- typed as such, NOT claimed as new
mathematics.  The probe's content is the exact operator packaging:

  S1  the exact verification -- sympy entrywise at N = 60 in the
      formal log-prime basis (log n = sum_p v_p(n) L_p: exact
      "log-integers") AND with literal sympy.log; the one-line proof
      reproduced as exact algebra (generic symbol for log a, termwise
      cancellation); the exact integer layer at N = 360 (M Z = I and
      the per-prime commutator [V_p, Z] = -Z E_p, which IS Chebyshev
      1 * Lambda = log prime by prime); the float ward at N = 10^4.
  S2  the power/chain formula (L^k)_{a,b} = sum over ordered
      factorization chains b/a = r_1 ... r_k (prime powers) of
      prod_j Lambda(r_j), k = 2, 3 exact vs independent enumeration;
      nilpotency L^k = 0 for 2^k > N; the log: W := log Z =
      sum (-1)^{k+1} (Z - I)^k / k is RATIONAL with entries 1/k at
      ratio p^k (Lambda with the log stripped), exp(W) = Z exactly,
      and L = [W, D] = -[D, log Z] EXACTLY -- the BCH series for
      -Z^{-1}[D,Z] truncates because [W, [W, D]] = 0; the Chebyshev
      operator identity [D, Z] = -Z L; the semigroup anchor
      Z^2 = T(d).
  S3  the four-comb discipline at operator level: TRUE zeta / the
      chi4 twist (Z^chi = T(chi4): the commutator produces the
      twisted Lambda_chi = chi4 * Lambda -- Selberg-class-correct) /
      zeta_{Q(i)} at the IDEAL level (Z[i] ideal poset, norm <= 300,
      canonical generators x >= 1, y >= 0: the commutator produces
      ITS Lambda_K, and the norm-aggregation equals (1 + chi4)
      Lambda) / the EPSTEIN h = 2 form x^2 + 5y^2: the operator
      identity itself STILL holds (T is an algebra iso from Dirichlet
      convolution -- the machine never breaks) but the produced
      Lambda_A is NOT a consistent von Mangoldt function: its support
      LEAKS off the prime powers exactly at the class-group
      obstruction (first site 6 = 2 x 3, first UNRAMIFIED site
      21 = 3 x 7), the h = 2 class-convolution law
      a_A(mk) = a_A(m) a_A(k) + a_B(m) a_B(k) is verified exactly,
      and the class-average a_A + a_B = 1 * chi_{-20} REPAIRS the
      Euler product (off-prime-power support empty): the defect is
      exactly the class group.
  S4  the bridge: the deployed relational carrier's Moebius-pairing
      reconstruction sum_{d|m} mu(d) U(m/d) at true positions is
      LITERALLY the first row of L_N (per-divisor term equality);
      the pairing matrix B[k,j] = mu(m_k/m_j) on the deployed comb
      support (prime powers in [2, 256]) is a sub-block of Z^{-1};
      every row of L is the first row on the shifted sub-poset; the
      higher rows/powers are the untapped structure -- (L^k)_{1,n}
      enumerates ordered factorization chains, and the second
      Selberg function obeys T(mu * log^2) = L^2 - [D, L] exactly.

HONESTY: NO RH claim.  EXPLORATION ONLY: writes nothing, commits
nothing, nothing outside experiments/.  Firewall: no zeta zeros, no
prime-table symbols (own sieves; AST-checked).  The context probe
multiplicative_relation_probe.py is read-only context; its Moebius-
pairing design and measured support ward are re-declared here.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mangoldt_incidence_probe.py
"""

import ast
import hashlib
import math
import os
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sps
import sympy as sp

FROZEN_SPEC = """\
PRIME.RELATION.MANGOLDT.01 spec v1 (2026-08-07, frozen before the
run).  THE THEOREM on {1..N}: Z = [1_{a|b}], M = Z^{-1} =
[mu(b/a) 1_{a|b}], D = diag(log a); L_N := -M[D,Z] == T(Lambda)
(entries Lambda(b/a) on a|b, else 0).  NO RH claim; classical
incidence-algebra content, verified as exact operator algebra, then
generalized and bridged.
S1 EXACT VERIFICATION: (a) sympy entrywise at N_SYM = 60 -- formal
log-prime basis (log n = sum v_p(n) L_p, exact log-integers) over
ALL 60^2 pairs, plus literal sympy.log with expand_log(force) on all
divisor pairs; (b) the one-line proof as exact algebra: matrix
entries == sum_{e|n} mu(e)(log(ae) - log(an)) for all (a, n) with
an <= 60; generic-La termwise cancellation for all n <= 60;
sum_{e|n} mu(e) log e == -Lambda(n) and sum_{e|n} mu(e) ==
delta_{n,1}; (c) exact integer layer at N_INT = 360: M Z == I,
per-prime [V_p, Z] == -Z E_p for ALL primes p <= 360 (V_p = diag
v_p, E_p = indicator of p-power ratio; Chebyshev 1*Lambda = log per
prime), and -M[D,Z] == T(Lambda) entrywise in the log-p module
(Fractions); (d) float ward at N_FLT = 10^4 (scipy sparse):
max |M[D,Z] + T(Lambda)| <= BAR_FLT = 1e-8.
S2 POWERS / NILPOTENCY / LOG: (L^k)_{a,b} == sum over ordered chains
b/a = r_1...r_k (prime powers >= 2) of prod Lambda(r_j), exact sympy
at N_SYM for k = 2, 3 vs independent chain enumeration; nilpotency:
L^6 == 0 at N_SYM with L^5 != 0 and (L^5)_{1,32} == L2^5; at N_FLT
nnz(L^13) == 1 (single entry (1, 8192) == (log 2)^13 to rel 1e-9)
and nnz(L^14) == 0 (2^14 > 10^4).  THE LOG: W := log Z =
sum_{k>=1} (-1)^{k+1} (Z-I)^k / k is RATIONAL: entries 1/k at ratio
p^k, 0 else (kappa = Lambda/log); (Z-I)^9 == 0 at N_INT; exp(W) == Z
exact (Fractions); L == [W, D] == -[D, log Z] EXACTLY, and
[W, [W, D]] == 0 (so the BCH series of -Z^{-1}[D, Z] truncates at
its first term: the sign-fixed relationship is L = -Z^{-1}[D,Z] =
-[D, log Z]); [L, Z] == 0 and [L, W] == 0; Chebyshev operator form
[D, Z] == -(Z L) == -(L Z); semigroup anchor Z^2 == T(d), d = 1*1.
S3 FOUR-COMB OPERATOR TABLE (exact; scalar Lambda_f by the frozen
recursion Lambda_f(n) = f(n) log n - sum_{d|n, 1<d<n} Lambda_f(d)
f(n/d), all n <= 360; T(f) is an algebra iso, so the commutator
ALWAYS produces T(Lambda_f); Selberg-consistency criterion = support
of Lambda_f inside the prime powers): (a) TRUE f = 1: Lambda_f ==
Lambda exactly, off-pp support EMPTY; (b) chi4 TWIST f = chi4 (the
twisted incidence Z^chi = T(chi4)): M^chi Z^chi == I,
-M^chi[D, Z^chi] == T(chi4 Lambda) exact, off-pp EMPTY,
Lambda_f == chi4 * Lambda pointwise; (c) zeta_{Q(i)} at IDEAL level:
ideals of Z[i] with norm <= NK = 300, canonical generators x >= 1,
y >= 0, poset = ideal divisibility, D_K = diag(log N); own Gaussian
factorization; ward #ideals(norm n) == r2(n)/4; M_K == [mu_K] with
M_K Z_K == I; -M_K[D_K, Z_K] == T(Lambda_K) exact (Lambda_K =
log N(P) on prime-ideal powers); norm aggregation
sum_{N(A)=n} Lambda_K(A) == (1 + chi4(n)) Lambda(n) for all
n <= 300; scalar comb f = r2/4 == 1 * chi4 (ward), off-pp EMPTY,
Lambda_f == (1 + chi4) Lambda; functoriality T(1) T(chi4) ==
T(r2/4) and L_{r2/4} == L_zeta + L_chi (the log-derivative is
additive over the always-commuting Dirichlet product); (d) EPSTEIN
h = 2, f = a_A = r_{x^2+5y^2}/2 (own double loop; a_A(1) = 1):
M_A Z_A == I and -M_A[D, Z_A] == T(Lambda_A) STILL hold (the
operator identity never breaks) but Lambda_A LEAKS off the prime
powers: first three sites == [6, 14, 21], min site coprime to 10 ==
21 (= 3 x 7: the unramified class-group obstruction; 6 = 2 x 3 and
14 = 2 x 7 involve the ramified prime 2), exact values
Lambda_A(6) == 2 log 6, Lambda_A(14) == 2 log 14, Lambda_A(21) ==
4 log 21; prime-power values may differ from zeta's (Lambda_A(4) ==
2 log 2, Lambda_A(9) == 6 log 3: own Euler factors at good local
slots -- NOT the discriminator); the h = 2 CLASS-CONVOLUTION LAW
a_A(mk) == a_A(m) a_A(k) + a_B(m) a_B(k) AND a_B(mk) ==
a_A(m) a_B(k) + a_B(m) a_A(k) for ALL coprime pairs with mk <= 360
(a_B = r_{2x^2+2xy+3y^2}/2, a_B(1) = 0: the class-B comb is not
unital -- only the principal class gives an invertible incidence
operator); the CLASS-AVERAGE REPAIR b = a_A + a_B == 1 * chi_{-20}
(Kronecker character, own Euler criterion) with off-pp support
EMPTY: the leak is exactly the class group.
S4 THE BRIDGE to the deployed relational carrier (PRIME.RELATION.
MULT.01, read-only context): (a) the Moebius-pairing reconstruction
Lambdahat(m) = sum_{d|m} mu(d) U(m/d) at TRUE positions U = log is
LITERALLY the first row of L_N: per-divisor term equality
mu(d) log(m/d) == -M_{1,d} [D,Z]_{d,m} for EVERY d | m <= 360, and
the sums == L[1, m]; (b) the pairing matrix B[k, j] = mu(m_k/m_j)
on the deployed comb support (prime powers in [2, 256] plus the
unit, the context probe's measured support ward) == the sub-block
of M = Z^{-1}; (c) row self-similarity L[a, ab] == L[1, b] for all
ab <= 360 (every row is the first row on the shifted sub-poset);
(d) the untapped structure: (L^k)_{1,n} = ordered k-chain
correlations (S2), and the second Selberg function: scalar
mu * log^2 == Lambda log + Lambda*Lambda for all n <= 60 AND
operator T(mu * log^2) == L^2 - [D, L] entrywise at N_SYM.
BUDGETS: BAR_FLT = 1e-8; nilpotent-entry relative bar 1e-9; runtime
<= 20 min.  FIREWALL: no zeta zeros, no prime-table symbols (own
sieves, AST-checked), no target data, writes nothing, nothing
outside experiments/.  VERDICTS (frozen): MANGOLDT-COMMUTATOR-EXACT
(S1, S2, S3, S4 all pass as frozen) / MANGOLDT-COMMUTATOR-PARTIAL
(S1 passes, a later section fails -- typed where) / FAIL (S1
fails).  NO RH claim.
"""

N_SYM = 60
N_INT = 360
N_FLT = 10_000
NK = 300
X_SUPPORT = 256
BAR_FLT = 1.0e-8
BAR_REL = 1.0e-9
RUNTIME_BUDGET_S = 1200.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ===================================================== arithmetic layer
SPF = None      # smallest prime factor, own sieve
MU = None       # Moebius
ISPP = None     # prime-power indicator (n >= 2)
PPRIME = None   # the prime p for prime powers, else 0
CHI4 = None     # chi4(n)
DIVS = None     # divisor lists up to N_INT
LOGD = None     # exact log n in the log-p basis: {p: Fr(v_p(n))}
LAMLD = None    # exact Lambda(n) logdict: {p: Fr(1)} on prime powers


def sieve_spf(n_max):
    spf = np.zeros(n_max + 1, dtype=np.int64)
    for p in range(2, n_max + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


def factorize(n):
    out = {}
    while n > 1:
        p = int(SPF[n])
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        out[p] = k
    return out


def build_arithmetic():
    global SPF, MU, ISPP, PPRIME, CHI4, DIVS, LOGD, LAMLD
    SPF = sieve_spf(N_FLT)
    MU = np.zeros(N_FLT + 1, dtype=np.int64)
    MU[1] = 1
    ISPP = np.zeros(N_FLT + 1, dtype=bool)
    PPRIME = np.zeros(N_FLT + 1, dtype=np.int64)
    CHI4 = np.zeros(N_FLT + 1, dtype=np.int64)
    for n in range(2, N_FLT + 1):
        f = factorize(n)
        MU[n] = 0 if any(k > 1 for k in f.values()) else (-1) ** len(f)
        if len(f) == 1:
            ISPP[n] = True
            PPRIME[n] = next(iter(f))
    for n in range(1, N_FLT + 1):
        if n % 2 == 1:
            CHI4[n] = 1 if n % 4 == 1 else -1
    DIVS = {n: [] for n in range(1, N_INT + 1)}
    for d in range(1, N_INT + 1):
        for m in range(d, N_INT + 1, d):
            DIVS[m].append(d)
    LOGD = {1: {}}
    for n in range(2, N_INT + 1):
        LOGD[n] = {p: Fr(k) for p, k in factorize(n).items()}
    LAMLD = {n: ({int(PPRIME[n]): Fr(1)} if ISPP[n] else {})
             for n in range(1, N_INT + 1)}
    LAMLD[1] = {}


# ---------------------------------------------- exact log-p dict values
def ld_clean(v):
    return {p: c for p, c in v.items() if c != 0}


def ld_axpy(acc, s, v):
    for p, c in v.items():
        acc[p] = acc.get(p, Fr(0)) + s * c
    return acc


def ld_scale(v, s):
    return {} if s == 0 else {p: s * c for p, c in v.items()}


def ld_eq(u, v):
    return ld_clean(u) == ld_clean(v)


def ld_norm1(v):
    return sum(abs(c) for c in v.values())


def ld_str(v):
    v = ld_clean(v)
    if not v:
        return "0"
    return " + ".join("%s*log%d" % (c, p) for p, c in sorted(v.items()))


# --------------------------------------- sparse matrices (dict keyed ij)
def mm(A, B, expand=False):
    """Scalar sparse product (values: int / Fraction / sympy)."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            k = (a, b)
            out[k] = out.get(k, 0) + u * v
    res = {}
    for k, v in out.items():
        if expand:
            v = sp.expand(v)
        if v != 0:
            res[k] = v
    return res


def mmL(A, B):
    """A scalar-valued, B logdict-valued."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            ld_axpy(out.setdefault((a, b), {}), u, v)
    return {k: w for k, w in ((k, ld_clean(v)) for k, v in out.items())
            if w}


def mmLs(A, B):
    """A logdict-valued, B scalar-valued."""
    rows = {}
    for (c, b), v in B.items():
        rows.setdefault(c, []).append((b, v))
    out = {}
    for (a, c), u in A.items():
        lst = rows.get(c)
        if not lst:
            continue
        for b, v in lst:
            ld_axpy(out.setdefault((a, b), {}), v, u)
    return {k: w for k, w in ((k, ld_clean(v)) for k, v in out.items())
            if w}


def mat_eq(A, B):
    for k in set(A) | set(B):
        if A.get(k, 0) != B.get(k, 0):
            return False, k
    return True, None


def mat_eq_ld(A, B):
    for k in set(A) | set(B):
        if not ld_eq(A.get(k, {}), B.get(k, {})):
            return False, k
    return True, None


def mat_neg_ld(A):
    return {k: ld_scale(v, -1) for k, v in A.items()}


def mat_add_ld(A, B):
    out = {}
    for k in set(A) | set(B):
        acc = dict(A.get(k, {}))
        ld_axpy(acc, 1, B.get(k, {}))
        acc = ld_clean(acc)
        if acc:
            out[k] = acc
    return out


# ------------------------------------------- incidence-operator builders
def build_Z(n_top, f=None):
    """T(f): entries f(b/a) on divisor pairs a | b (f defaults to 1)."""
    Z = {}
    for a in range(1, n_top + 1):
        for b in range(a, n_top + 1, a):
            v = 1 if f is None else f[b // a]
            if v != 0:
                Z[(a, b)] = v
    return Z


def build_commDZ(n_top, f=None):
    """[D, T(f)]: entries (log a - log b) f(b/a) = -log(b/a) f(b/a)."""
    C = {}
    for a in range(1, n_top + 1):
        for b in range(2 * a, n_top + 1, a):
            v = 1 if f is None else f[b // a]
            if v != 0:
                C[(a, b)] = ld_scale(LOGD[b // a], -v)
    return C


def build_TLam(n_top, lam):
    """T(Lambda_f) from a logdict array lam[n]."""
    out = {}
    for a in range(1, n_top + 1):
        for b in range(2 * a, n_top + 1, a):
            v = lam[b // a]
            if v:
                out[(a, b)] = v
    return out


def dirichlet_inverse(a, n_top):
    b = [0] * (n_top + 1)
    assert a[1] == 1
    b[1] = 1
    for n in range(2, n_top + 1):
        s = 0
        for d in DIVS[n]:
            if d < n and b[d] != 0 and a[n // d] != 0:
                s += b[d] * a[n // d]
        b[n] = -s
    return b


def dirichlet_conv(a, b, n_top):
    c = [0] * (n_top + 1)
    for n in range(1, n_top + 1):
        s = 0
        for d in DIVS[n]:
            s += a[d] * b[n // d]
        c[n] = s
    return c


def lambda_of_comb(a, n_top):
    """Frozen recursion Lambda_f(n) = a(n) log n
       - sum_{d|n, 1<d<n} Lambda_f(d) a(n/d); logdict values."""
    G = {1: {}}
    for n in range(2, n_top + 1):
        acc = {}
        if a[n] != 0:
            ld_axpy(acc, Fr(a[n]), LOGD[n])
        for d in DIVS[n]:
            if 1 < d < n and G[d] and a[n // d] != 0:
                ld_axpy(acc, -Fr(a[n // d]), G[d])
        G[n] = ld_clean(acc)
    return G


# ================================================= S1 exact verification
def s1_exact():
    section("S1 -- THE EXACT VERIFICATION: L_N = -M[D,Z] == T(Lambda)")
    ok_all = True

    # S1.1 arithmetic wards
    mu_ok = all(sum(int(MU[d]) for d in DIVS[n]) == (1 if n == 1 else 0)
                for n in range(1, N_INT + 1))
    lam_ok = True
    for n in range(2, N_INT + 1):
        acc = {}
        for d in DIVS[n]:
            if MU[d]:
                ld_axpy(acc, Fr(int(MU[d])), LOGD[n // d])
        lam_ok &= ld_eq(acc, LAMLD[n])
    ok_all &= check("S1.1 [EXACT] arithmetic wards on own sieves: "
                    "(mu * 1)(n) == delta_1 and (mu * log)(n) == "
                    "Lambda(n) in the log-p basis for ALL n <= %d"
                    % N_INT, mu_ok and lam_ok)

    # S1.2 sympy, formal log-prime basis, entrywise at N_SYM
    primes60 = [p for p in range(2, N_SYM + 1) if ISPP[p] and p == PPRIME[p]]
    LS = {p: sp.Symbol("L%d" % p) for p in primes60}

    def lsym(n):
        return sp.Add(*[int(k) * LS[p] for p, k in LOGD[n].items()])

    Z60 = build_Z(N_SYM)
    M60 = {(a, b): int(MU[b // a]) for (a, b) in Z60
           if MU[b // a] != 0}
    C60 = {}
    for (a, b) in Z60:
        if a != b:
            C60[(a, b)] = lsym(a) - lsym(b)
    L60 = {k: sp.expand(-v) for k, v in mm(M60, C60, expand=True).items()}
    exp60 = {}
    for (a, b) in Z60:
        r = b // a
        if ISPP[r]:
            exp60[(a, b)] = LS[int(PPRIME[r])]
    ok_ent = True
    n_pairs = 0
    for a in range(1, N_SYM + 1):
        for b in range(1, N_SYM + 1):
            got = L60.get((a, b), sp.Integer(0))
            want = exp60.get((a, b), sp.Integer(0))
            if b % a == 0:
                n_pairs += 1
            if sp.expand(got - want) != 0:
                ok_ent = False
    ok_all &= check("S1.2 [EXACT -- sympy, log-integer basis] "
                    "(-M[D,Z])_{a,b} == Lambda(b/a) entrywise for ALL "
                    "%d^2 pairs (%d divisor pairs) at N = %d"
                    % (N_SYM, n_pairs, N_SYM), ok_ent)
    print("      sample exact entries: L[2,24] = %s (= Lambda(12)),  "
          "L[3,24] = %s (= Lambda(8)),  L[1,32] = %s (= Lambda(32))"
          % (sp.expand(L60.get((2, 24), sp.Integer(0))),
             L60.get((3, 24), 0), L60.get((1, 32), 0)))

    # S1.3 sympy, literal logs (own log-integer rewrite, no
    # dependence on expand_log internals)
    logsubs = {}
    for m in range(2, N_SYM + 1):
        f = factorize(m)
        if not (len(f) == 1 and next(iter(f.values())) == 1):
            logsubs[sp.log(m)] = sp.Add(*[k * sp.log(p)
                                          for p, k in f.items()])
    ok_lit = True
    for (a, b) in Z60:
        if a == b:
            continue
        r = b // a
        expr = sp.Integer(0)
        for c in range(a, b + 1, a):
            if b % c == 0 and MU[c // a] != 0:
                expr += int(MU[c // a]) * (sp.log(c) - sp.log(b))
        want = sp.log(int(PPRIME[r])) if ISPP[r] else sp.Integer(0)
        diff = sp.expand((-expr - want).xreplace(logsubs))
        if diff != 0:
            ok_lit = False
    ok_all &= check("S1.3 [EXACT -- sympy, literal logs] the same "
                    "identity with sympy.log integers, rewritten to "
                    "the log-prime basis by own factorization, on "
                    "all divisor pairs at N = %d" % N_SYM, ok_lit)

    # S1.4 the one-line proof as exact algebra
    ok_match = True
    for a in range(1, N_SYM + 1):
        for n in range(1, N_SYM // a + 1):
            ssum = sp.Integer(0)
            for e in DIVS[n]:
                if MU[e]:
                    ssum += int(MU[e]) * (lsym(a * e) - lsym(a * n))
            mdz = -L60.get((a, a * n), sp.Integer(0))
            if sp.expand(ssum - mdz) != 0:
                ok_match = False
    La = sp.Symbol("La")
    ok_generic = True
    ok_classic = True
    for n in range(1, N_SYM + 1):
        terms = []
        for e in DIVS[n]:
            if MU[e]:
                t = sp.expand(int(MU[e]) * ((La + lsym(e))
                                            - (La + lsym(n))))
                if t.has(La):
                    ok_generic = False
                terms.append(t)
        total = sp.expand(sp.Add(*terms))
        lam_n = (LS[int(PPRIME[n])] if (n > 1 and ISPP[n])
                 else sp.Integer(0))
        if sp.expand(total + lam_n) != 0:
            ok_generic = False
        s_mulog = sp.expand(sp.Add(*[int(MU[e]) * lsym(e)
                                     for e in DIVS[n] if MU[e]]))
        s_mu = sum(int(MU[e]) for e in DIVS[n])
        if sp.expand(s_mulog + lam_n) != 0 or s_mu != (1 if n == 1
                                                       else 0):
            ok_classic = False
    ok_all &= check("S1.4 [EXACT -- THE ONE-LINE PROOF] (M[D,Z])_{a,an} "
                    "== sum_{e|n} mu(e)(log(ae) - log(an)) for all "
                    "an <= %d; with GENERIC symbol La = log a the "
                    "cancellation is TERMWISE and the sum == -Lambda(n) "
                    "for all n; the classical pair sum mu(e) log e == "
                    "-Lambda(n), sum mu(e) == delta_{n,1}" % N_SYM,
                    ok_match and ok_generic and ok_classic)

    # S1.5 / S1.6 / S1.7 exact integer layer at N_INT
    Z = build_Z(N_INT)
    M = {(a, b): int(MU[b // a]) for (a, b) in Z if MU[b // a] != 0}
    ident = {(a, a): 1 for a in range(1, N_INT + 1)}
    okI, bad = mat_eq(mm(M, Z), ident)
    ok_all &= check("S1.5 [EXACT] M Z == I at N = %d (M = [mu(b/a)] is "
                    "the integer inverse of the unitriangular Z)"
                    % N_INT, okI, "" if okI else "first bad %s" % (bad,))

    primes360 = [p for p in range(2, N_INT + 1)
                 if ISPP[p] and p == PPRIME[p]]
    ok_cheb = True
    for p in primes360:
        Ep = {}
        for a in range(1, N_INT + 1):
            q = p
            while a * q <= N_INT:
                Ep[(a, a * q)] = 1
                q *= p
        lhs = {}
        for (a, b) in Z:
            v = int(LOGD[a].get(p, 0)) - int(LOGD[b].get(p, 0))
            if v:
                lhs[(a, b)] = v
        rhs = {k: -v for k, v in mm(Z, Ep).items()}
        okp, _ = mat_eq(lhs, rhs)
        ok_cheb &= okp
    ok_all &= check("S1.6 [EXACT] per-prime commutator [V_p, Z] == "
                    "-Z E_p for ALL %d primes p <= %d -- prime by "
                    "prime this IS Chebyshev's identity 1 * Lambda = "
                    "log (v_p(n) = #{k >= 1 : p^k | n})"
                    % (len(primes360), N_INT), ok_cheb)

    C = build_commDZ(N_INT)
    L360 = mat_neg_ld(mmL(M, C))
    TL360 = build_TLam(N_INT, LAMLD)
    okL, bad = mat_eq_ld(L360, TL360)
    ok_all &= check("S1.7 [EXACT] -M[D,Z] == T(Lambda) entrywise at "
                    "N = %d in the log-p module (%d divisor pairs; "
                    "includes the first-row control L[1,n] == "
                    "Lambda(n))" % (N_INT, len(Z)), okL,
                    "" if okL else "first bad %s" % (bad,))

    # S1.8 float ward at N_FLT
    rows, cols, ratio = [], [], []
    for a in range(1, N_FLT + 1):
        for b in range(a, N_FLT + 1, a):
            rows.append(a - 1)
            cols.append(b - 1)
            ratio.append(b // a)
    rows = np.array(rows, dtype=np.int64)
    cols = np.array(cols, dtype=np.int64)
    ratio = np.array(ratio, dtype=np.int64)
    shape = (N_FLT, N_FLT)
    logs = np.log(np.arange(0, N_FLT + 1, dtype=float))
    Zf = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=shape)
    Mf = sps.csr_matrix((MU[ratio].astype(float), (rows, cols)),
                        shape=shape)
    Cf = sps.csr_matrix((logs[rows + 1] - logs[cols + 1], (rows, cols)),
                        shape=shape)
    lamv = np.where(ISPP[ratio], logs[PPRIME[ratio]], 0.0)
    TLf = sps.csr_matrix((lamv, (rows, cols)), shape=shape)
    R = (Mf @ Cf) + TLf
    mx = float(np.max(np.abs(R.data))) if R.nnz else 0.0
    ok_all &= check("S1.8 [FLOAT WARD] max |M[D,Z] + T(Lambda)| = "
                    "%.2e <= %.0e at N = %d (%d divisor pairs, scipy "
                    "sparse)" % (mx, BAR_FLT, N_FLT, len(rows)),
                    mx <= BAR_FLT)
    return ok_all, dict(Z=Z, M=M, C=C, L360=L360, TL360=TL360,
                        Z60=Z60, M60=M60, C60=C60, L60=L60, LS=LS,
                        lsym_primes=primes60, TLf=TLf)


# ============================== S2 powers, nilpotency, log Z, resolvents
def ordered_pp_chains(n, k):
    if k == 0:
        return [()] if n == 1 else []
    out = []
    for r in DIVS[n]:
        if r >= 2 and ISPP[r]:
            for tail in ordered_pp_chains(n // r, k - 1):
                out.append((r,) + tail)
    return out


def s2_powers_log(env):
    section("S2 -- THE POWER/CHAIN FORMULA, NILPOTENCY, AND log Z")
    ok_all = True
    L60, LS = env["L60"], env["LS"]
    Z, M, C, L360 = env["Z"], env["M"], env["C"], env["L360"]

    # S2.1 / S2.2 power formula vs independent chain enumeration
    Lp = {1: L60}
    for k in (2, 3):
        Lp[k] = mm(Lp[k - 1], L60, expand=True)
        ok_k = True
        for a in range(1, N_SYM + 1):
            for b in range(a, N_SYM + 1, a):
                want = sp.Integer(0)
                for chain in ordered_pp_chains(b // a, k):
                    want += sp.Mul(*[LS[int(PPRIME[r])] for r in chain])
                got = Lp[k].get((a, b), sp.Integer(0))
                if sp.expand(got - want) != 0:
                    ok_k = False
        nz = len(Lp[k])
        ok_all &= check("S2.%d [EXACT -- sympy] (L^%d)_{a,b} == sum over "
                        "ordered chains b/a = r_1...r_%d (prime powers) "
                        "of prod Lambda(r_j), all pairs at N = %d "
                        "(%d nonzero entries)"
                        % (k - 1, k, k, N_SYM, nz), ok_k)
    print("      sample: (L^2)[1,12] = %s (chains 3*4 and 4*3);  "
          "(L^3)[1,8] = %s (chain 2*2*2)"
          % (sp.expand(Lp[2].get((1, 12), 0)), Lp[3].get((1, 8), 0)))

    # S2.3 nilpotency
    Lp[4] = mm(Lp[3], L60, expand=True)
    Lp[5] = mm(Lp[4], L60, expand=True)
    Lp[6] = mm(Lp[5], L60, expand=True)
    ok_nil60 = (len(Lp[6]) == 0 and len(Lp[5]) > 0
                and sp.expand(Lp[5].get((1, 32), sp.Integer(0))
                              - LS[2] ** 5) == 0)
    TLf = env["TLf"]
    P = TLf.copy()
    nnz = {1: P.nnz}
    for k in range(2, 15):
        P = P @ TLf
        P.eliminate_zeros()
        nnz[k] = P.nnz
        if k == 13:
            v13 = float(P[0, 8191])
    rel13 = abs(v13 - math.log(2.0) ** 13) / math.log(2.0) ** 13
    ok_nilf = (nnz[13] == 1 and nnz[14] == 0 and rel13 <= BAR_REL)
    ok_all &= check("S2.3 [EXACT + FLOAT] nilpotency L^k = 0 for 2^k > "
                    "N: at N = %d L^6 == 0 with L^5 != 0 and "
                    "(L^5)_{1,32} == L2^5; at N = %d nnz(L^13) == 1 "
                    "(only (1, 8192), value == (log 2)^13 to rel "
                    "%.1e) and nnz(L^14) == 0"
                    % (N_SYM, N_FLT, rel13), ok_nil60 and ok_nilf)

    # S2.4 W = log Z is rational with entries 1/k at p^k
    S = {k: 1 for k in Z if k[0] != k[1]}
    Spow = {1: S}
    for k in range(2, 10):
        Spow[k] = mm(Spow[k - 1], S)
    W = {}
    for k in range(1, 9):
        s = Fr((-1) ** (k + 1), k)
        for key, v in Spow[k].items():
            W[key] = W.get(key, Fr(0)) + s * v
    W = {k: v for k, v in W.items() if v != 0}
    Wexp = {}
    for (a, b) in Z:
        r = b // a
        if r > 1 and ISPP[r]:
            kk = sum(int(c) for c in LOGD[r].values())
            Wexp[(a, b)] = Fr(1, kk)
    okW, bad = mat_eq(W, Wexp)
    ok_all &= check("S2.4 [EXACT -- RATIONAL] W := log Z = sum (-1)^"
                    "{k+1} (Z-I)^k / k has entries 1/k at ratio p^k "
                    "and 0 elsewhere at N = %d ((Z-I)^9 == 0: %s) -- "
                    "log Z is Lambda with the log stripped: kappa = "
                    "Lambda/log, a RATIONAL matrix"
                    % (N_INT, len(Spow[9]) == 0),
                    okW and len(Spow[9]) == 0,
                    "" if okW else "first bad %s" % (bad,))

    # S2.5 exp(W) == Z exactly
    Wpow = {1: W}
    for k in range(2, 9):
        Wpow[k] = mm(Wpow[k - 1], W)
    expW = {(a, a): Fr(1) for a in range(1, N_INT + 1)}
    for k in range(1, 9):
        s = Fr(1, math.factorial(k))
        for key, v in Wpow[k].items():
            expW[key] = expW.get(key, Fr(0)) + s * v
    expW = {k: v for k, v in expW.items() if v != 0}
    Zfr = {k: Fr(v) for k, v in Z.items()}
    okE, _ = mat_eq(expW, Zfr)
    ok_all &= check("S2.5 [EXACT] exp(W) == Z (Fraction arithmetic; "
                    "the nilpotent log/exp pair is exact on the "
                    "incidence algebra)", okE)

    # S2.6 L == [W, D] == -[D, log Z]
    WD = {}
    for (a, b), v in W.items():
        WD[(a, b)] = ld_clean(ld_scale(LOGD[b // a], v))
    WD = {k: v for k, v in WD.items() if v}
    okWD, bad = mat_eq_ld(WD, L360)
    ok_all &= check("S2.6 [EXACT] L == [W, D] == -[D, log Z] entrywise "
                    "at N = %d: the commutator with D multiplies the "
                    "1/k weight of log Z by k log p, restoring Lambda "
                    "-- the honest structural map between L and log Z"
                    % N_INT, okWD,
                    "" if okWD else "first bad %s" % (bad,))

    # S2.7 BCH truncation: [W, [W, D]] == 0
    WL = mmL(W, L360)
    LW = mmLs(L360, W)
    okB, _ = mat_eq_ld(WL, LW)
    ok_all &= check("S2.7 [EXACT] [W, [W, D]] == 0 (W L == L W): the "
                    "BCH series of -Z^{-1}[D,Z] = -(e^{-W} D e^{W} - "
                    "D) truncates at its first term, so the sign-fixed "
                    "relationship L = -Z^{-1}[D,Z] = -[D, log Z] is "
                    "EXACT, not first-order", okB)

    # S2.8 Chebyshev operator identity + semigroup anchor
    ZL = mmL(Zfr, L360)
    LZ = mmLs(L360, Zfr)
    negC = mat_neg_ld(C)
    ok1, _ = mat_eq_ld(ZL, negC)
    ok2, _ = mat_eq_ld(LZ, negC)
    d_arr = dirichlet_conv([0] + [1] * N_INT, [0] + [1] * N_INT, N_INT)
    Td = build_Z(N_INT, d_arr)
    okZ2, _ = mat_eq(mm(Z, Z), Td)
    ok_all &= check("S2.8 [EXACT] the Chebyshev operator identity "
                    "[D, Z] == -(Z L) == -(L Z) (i.e. 1 * Lambda = "
                    "log and [L, Z] == 0) and the semigroup anchor "
                    "Z^2 == T(d), d = 1*1, at N = %d" % N_INT,
                    ok1 and ok2 and okZ2)
    return ok_all


# ===================== S3 the four-comb discipline at the operator level
def gconj(u):
    return (u[0], -u[1])


def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gnorm(u):
    return u[0] * u[0] + u[1] * u[1]


def gdiv_exact(u, v):
    n = gnorm(v)
    w = gmul(u, gconj(v))
    if w[0] % n or w[1] % n:
        return None
    return (w[0] // n, w[1] // n)


def gcanon(z):
    cands = [z, (-z[1], z[0]), (-z[0], -z[1]), (z[1], -z[0])]
    picks = [c for c in cands if c[0] >= 1 and c[1] >= 0]
    assert len(picks) == 1, z
    return picks[0]


def gaussian_primes(p_max):
    """Canonical Gaussian primes above each rational prime <= p_max."""
    gp = {}
    for p in range(2, p_max + 1):
        if SPF[p] != p:
            continue
        if p == 2:
            gp[2] = ((1, 1), None)
        elif p % 4 == 3:
            gp[p] = ((p, 0), None)
        else:
            g = 2
            while pow(g, (p - 1) // 2, p) != p - 1:
                g += 1
            s = pow(g, (p - 1) // 4, p)
            u, v = (p, 0), (s, 1)
            while gnorm(v):
                n = gnorm(v)
                w = gmul(u, gconj(v))
                q = (round(w[0] / n), round(w[1] / n))
                u, v = v, (u[0] - (q[0] * v[0] - q[1] * v[1]),
                           u[1] - (q[0] * v[1] + q[1] * v[0]))
            pi = gcanon(u)
            assert gnorm(pi) == p
            gp[p] = (pi, gcanon(gconj(pi)))
    return gp


def gfactor(z, gp):
    """Exponents of canonical Gaussian primes in z (canonical, != 0)."""
    ex = {}
    m = gnorm(z)
    for p, k in factorize(m).items():
        if p == 2:
            pi = (1, 1)
            for _ in range(k):
                z = gdiv_exact(z, pi)
                assert z is not None
            ex[pi] = ex.get(pi, 0) + k
        elif p % 4 == 3:
            assert k % 2 == 0
            pi = (p, 0)
            for _ in range(k // 2):
                z = gdiv_exact(z, pi)
                assert z is not None
            ex[pi] = ex.get(pi, 0) + k // 2
        else:
            pi, pib = gp[p]
            i = 0
            while True:
                w = gdiv_exact(z, pi)
                if w is None:
                    break
                z, i = w, i + 1
            j = k - i
            for _ in range(j):
                z = gdiv_exact(z, pib)
                assert z is not None
            if i:
                ex[pi] = i
            if j:
                ex[pib] = j
    assert gnorm(z) == 1
    return ex


def rep_counts(n_top):
    r2 = np.zeros(n_top + 1, dtype=np.int64)
    rq = np.zeros(n_top + 1, dtype=np.int64)
    rb = np.zeros(n_top + 1, dtype=np.int64)
    s = int(math.isqrt(n_top)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + y * y
            if 1 <= v <= n_top:
                r2[v] += 1
            v = x * x + 5 * y * y
            if 1 <= v <= n_top:
                rq[v] += 1
            v = 2 * x * x + 2 * x * y + 3 * y * y
            if 1 <= v <= n_top:
                rb[v] += 1
    return r2, rq, rb


def kron_m20(n_top):
    """Completely multiplicative Kronecker character chi_{-20}."""
    val = {2: 0, 5: 0}
    k = np.zeros(n_top + 1, dtype=np.int64)
    k[1] = 1
    for n in range(2, n_top + 1):
        out = 1
        for p, e in factorize(n).items():
            if p not in val:
                val[p] = 1 if pow(-20 % p, (p - 1) // 2, p) == 1 else -1
            out *= val[p] ** e
        k[n] = out
    return k


def offpp_report(lam, n_top):
    sites = [n for n in range(2, n_top + 1)
             if not ISPP[n] and lam.get(n)]
    mass = sum(ld_norm1(lam[n]) for n in sites)
    return sites, mass


def s3_four_combs():
    section("S3 -- THE FOUR-COMB DISCIPLINE AT OPERATOR LEVEL")
    ok_all = True
    r2, rq, rb = rep_counts(N_INT)

    ok_r = (r2[1] == 4 and rq[1] == 2 and rb[1] == 0 and rq[3] == 0
            and rq[7] == 0 and rq[21] == 8 and rb[2] == 2 and rb[3] == 4
            and int(np.max(rq[1:] % 2)) == 0 and int(np.max(rb[1:] % 2))
            == 0 and int(np.max(r2[1:] % 4)) == 0)
    ok_all &= check("S3.1 [EXACT] representation counts (own double "
                    "loops): r2(1)=4, rQ(1)=2, rB(1)=0; rQ(3)=rQ(7)=0 "
                    "but rQ(21)=8 (h=2 signature); all parities for "
                    "the normalizations r2/4, rQ/2, rB/2", ok_r)

    one = [0] + [1] * N_INT
    chi = [0] + [int(CHI4[n]) for n in range(1, N_INT + 1)]
    aqi = [0] + [int(r2[n]) // 4 for n in range(1, N_INT + 1)]
    aA = [0] + [int(rq[n]) // 2 for n in range(1, N_INT + 1)]
    aB = [0] + [int(rb[n]) // 2 for n in range(1, N_INT + 1)]
    k20 = kron_m20(N_INT)
    rep = [0] + [aA[n] + aB[n] for n in range(1, N_INT + 1)]

    combs = [("TRUE zeta (a=1)", one),
             ("chi4 twist (a=chi4)", chi),
             ("zeta_Q(i) scalar (a=r2/4)", aqi),
             ("EPSTEIN h=2 (a=rQ/2)", aA),
             ("class-average repair (a_A+a_B)", rep)]
    lam_of = {}
    print("    THE FOUR-COMB OPERATOR TABLE (Lambda_f = f^{-1} * "
          "(f log), exact; off-pp = support off prime powers):")
    for name, arr in combs:
        lam_of[name] = lambda_of_comb(arr, N_INT)
        sites, mass = offpp_report(lam_of[name], N_INT)
        print("      %-32s off-pp sites: %3d %-18s  off-pp L1 = %s"
              % (name, len(sites),
                 (str(sites[:5]) + ("..." if len(sites) > 5 else ""))
                 if sites else "[]",
                 "0 (EXACT)" if mass == 0 else "%.4f" % float(mass)))

    # scalar identities for the three multiplicative combs
    lam_true = lam_of["TRUE zeta (a=1)"]
    ok_t = all(ld_eq(lam_true[n], LAMLD[n]) for n in range(2, N_INT + 1))
    lam_chi = lam_of["chi4 twist (a=chi4)"]
    ok_c = all(ld_eq(lam_chi[n], ld_scale(LAMLD[n], int(CHI4[n])))
               for n in range(2, N_INT + 1))
    lam_qi = lam_of["zeta_Q(i) scalar (a=r2/4)"]
    ok_q = all(ld_eq(lam_qi[n], ld_scale(LAMLD[n], 1 + int(CHI4[n])))
               for n in range(2, N_INT + 1))
    st_t, _ = offpp_report(lam_true, N_INT)
    st_c, _ = offpp_report(lam_chi, N_INT)
    st_q, _ = offpp_report(lam_qi, N_INT)
    st_r, _ = offpp_report(lam_of["class-average repair (a_A+a_B)"],
                           N_INT)
    ok_all &= check("S3.2 [EXACT] the three multiplicative combs are "
                    "Selberg-consistent: off-pp support EMPTY and "
                    "Lambda_f == Lambda / chi4*Lambda / (1+chi4)*"
                    "Lambda for TRUE / twist / zeta_Q(i) on all "
                    "n <= %d" % N_INT,
                    ok_t and ok_c and ok_q
                    and not st_t and not st_c and not st_q)

    # matrix level: the commutator produces T(Lambda_f) for every
    # unital comb, Epstein included -- T is an algebra iso
    ident = {(a, a): 1 for a in range(1, N_INT + 1)}
    mats = {}
    ok_mat = True
    for name, arr in [c for c in combs if c[0] != "class-average "
                      "repair (a_A+a_B)"]:
        Zf = build_Z(N_INT, arr)
        Minv = dirichlet_inverse(arr, N_INT)
        Mf = build_Z(N_INT, Minv)
        okI, _ = mat_eq(mm(Mf, Zf), ident)
        Lf = mat_neg_ld(mmL(Mf, build_commDZ(N_INT, arr)))
        TLf = build_TLam(N_INT, lam_of[name])
        okL, _ = mat_eq_ld(Lf, TLf)
        ok_mat &= okI and okL
        mats[name] = (Zf, Mf, Lf)
    ok_all &= check("S3.3 [EXACT] operator level, all four unital "
                    "combs (EPSTEIN INCLUDED): M_f Z_f == I and "
                    "-M_f[D, Z_f] == T(Lambda_f) entrywise at N = %d "
                    "-- the commutator machine NEVER breaks (T(f) is "
                    "an algebra iso from Dirichlet convolution); what "
                    "breaks for h = 2 is the SUPPORT of its output"
                    % N_INT, ok_mat)

    # functoriality: T(1) T(chi4) == T(r2/4), L additive
    okF1, _ = mat_eq(mm(mats["TRUE zeta (a=1)"][0],
                        mats["chi4 twist (a=chi4)"][0]),
                     mats["zeta_Q(i) scalar (a=r2/4)"][0])
    okF2 = (dirichlet_conv(one, chi, N_INT) == aqi)
    okF3, _ = mat_eq_ld(mat_add_ld(mats["TRUE zeta (a=1)"][2],
                                   mats["chi4 twist (a=chi4)"][2]),
                        mats["zeta_Q(i) scalar (a=r2/4)"][2])
    ok_all &= check("S3.4 [EXACT] Selberg functoriality at operator "
                    "level: T(1) T(chi4) == T(r2/4) (zeta_K = zeta "
                    "L(chi4); Dirichlet-series operators always "
                    "commute) and L_{zeta_K} == L_zeta + L_chi -- the "
                    "log-derivative is additive over the product",
                    okF1 and okF2 and okF3)

    # ---- (c) zeta_{Q(i)} at the IDEAL level
    gp = gaussian_primes(NK)
    ideals = [(x, y) for x in range(1, int(math.isqrt(NK)) + 1)
              for y in range(0, int(math.isqrt(NK)) + 1)
              if x * x + y * y <= NK]
    ideals.sort(key=lambda z: (gnorm(z), z))
    idx = {z: i for i, z in enumerate(ideals)}
    norms = [gnorm(z) for z in ideals]
    cnt = np.zeros(NK + 1, dtype=np.int64)
    for z in ideals:
        cnt[gnorm(z)] += 1
    ok_cnt = all(int(cnt[n]) == int(r2[n]) // 4 for n in range(1, NK + 1))

    ZK, MK, CK, TLK = {}, {}, {}, {}
    lamK = {}
    for i, zi in enumerate(ideals):
        for j, zj in enumerate(ideals):
            if norms[j] % norms[i]:
                continue
            q = gdiv_exact(zj, zi)
            if q is None:
                continue
            ZK[(i, j)] = 1
            if i != j:
                CK[(i, j)] = ld_scale(LOGD[norms[j] // norms[i]], -1)
                ex = gfactor(gcanon(q), gp)
                muK = 0 if any(e > 1 for e in ex.values()) \
                    else (-1) ** len(ex)
                if muK:
                    MK[(i, j)] = muK
                if len(ex) == 1:
                    pi = next(iter(ex))
                    npi = gnorm(pi)
                    pr = int(SPF[npi]) if npi > 1 else 0
                    lam = {pr: Fr(2 if npi == pr * pr else 1)}
                    TLK[(i, j)] = lam
                    lamK[(i, j)] = lam
            else:
                MK[(i, j)] = 1
    identK = {(i, i): 1 for i in range(len(ideals))}
    okKI, _ = mat_eq(mm(MK, ZK), identK)
    LK = mat_neg_ld(mmL(MK, CK))
    okKL, badK = mat_eq_ld(LK, TLK)
    ok_all &= check("S3.5 [EXACT] zeta_{Q(i)} at the IDEAL level "
                    "(%d ideals of Z[i], norm <= %d, canonical "
                    "generators x>=1, y>=0): #ideals(norm n) == "
                    "r2(n)/4 (%s); M_K == [mu_K] with M_K Z_K == I; "
                    "-M_K[D_K, Z_K] == T(Lambda_K) entrywise -- the "
                    "commutator produces the DEDEKIND von Mangoldt "
                    "(log N(P) on prime-ideal powers) because ideals "
                    "factor uniquely" % (len(ideals), NK, ok_cnt),
                    ok_cnt and okKI and okKL,
                    "" if okKL else "first bad %s" % (badK,))

    unit = idx[(1, 0)]
    agg = {n: {} for n in range(2, NK + 1)}
    for (i, j), v in LK.items():
        if i == unit:
            ld_axpy(agg[norms[j]], 1, v)
    ok_agg = all(ld_eq(agg[n], ld_scale(LAMLD[n], 1 + int(CHI4[n])))
                 for n in range(2, NK + 1))
    ok_all &= check("S3.6 [EXACT] norm aggregation of the ideal-level "
                    "first row: sum_{N(A)=n} Lambda_K(A) == "
                    "(1 + chi4(n)) Lambda(n) for all n <= %d -- the "
                    "ideal operator descends to the scalar zeta_K "
                    "comb (zeta_K = zeta L(chi4))" % NK, ok_agg)
    print("      sample: Lambda_K((2+i)) = %s;  Lambda_K((1+i)^2) = %s"
          % (ld_str(LK.get((unit, idx[(2, 1)]), {})),
             ld_str(LK.get((unit, idx[(2, 0)] if (2, 0) in idx else
                            (1, 1)), {}))))

    # ---- (d) EPSTEIN h = 2: the leak localized
    lam_A = lam_of["EPSTEIN h=2 (a=rQ/2)"]
    sites, mass = offpp_report(lam_A, N_INT)
    cop = [n for n in sites if math.gcd(n, 10) == 1]
    ok_sites = (len(sites) > 0 and sites[:3] == [6, 14, 21]
                and cop and min(cop) == 21)
    ok_vals = (ld_eq(lam_A[6], {2: Fr(2), 3: Fr(2)})
               and ld_eq(lam_A[14], {2: Fr(2), 7: Fr(2)})
               and ld_eq(lam_A[21], {3: Fr(4), 7: Fr(4)})
               and ld_eq(lam_A[4], {2: Fr(2)})
               and ld_eq(lam_A[9], {3: Fr(6)}))
    heavy = sorted(((float(ld_norm1(lam_A[n])), n) for n in sites),
                   reverse=True)[:3]
    ok_all &= check("S3.7 THE EPSTEIN BREAK LOCALIZED [EXACT]: "
                    "Lambda_A leaks off the prime powers on %d sites "
                    "<= %d, first three == [6, 14, 21], min site "
                    "coprime to 10 == 21 == 3 x 7 (the UNRAMIFIED "
                    "class-group obstruction: both factors sit in the "
                    "non-principal class, their product returns to "
                    "the principal form); exact values Lambda_A(6) == "
                    "2 log 6, Lambda_A(14) == 2 log 14, Lambda_A(21) "
                    "== 4 log 21; prime-power slots differ from "
                    "zeta's (Lambda_A(4) == 2 log 2, Lambda_A(9) == "
                    "6 log 3) and are NOT leaks -- own Euler factors "
                    "are allowed, cross-prime locality is what fails"
                    % (len(sites), N_INT), ok_sites and ok_vals,
                    "sites %s..., heaviest %s"
                    % (sites[:6], [(n, round(w, 3)) for w, n in heavy]))

    ok_law = True
    for m in range(1, N_INT + 1):
        for k in range(1, N_INT // m + 1):
            if math.gcd(m, k) != 1:
                continue
            ok_law &= (aA[m * k] == aA[m] * aA[k] + aB[m] * aB[k])
            ok_law &= (aB[m * k] == aA[m] * aB[k] + aB[m] * aA[k])
    ok_rep = (rep == [0] + list(dirichlet_conv(
        one, [0] + [int(k20[n]) for n in range(1, N_INT + 1)],
        N_INT))[1:]) and not st_r
    ok_all &= check("S3.8 [EXACT] the h = 2 CLASS-CONVOLUTION LAW "
                    "a_A(mk) == a_A a_A + a_B a_B and a_B(mk) == "
                    "a_A a_B + a_B a_A on ALL coprime pairs mk <= %d "
                    "(the coefficients are a Z/2-group-ring-valued "
                    "multiplicative function; the principal slice is "
                    "not), and the CLASS-AVERAGE REPAIR a_A + a_B == "
                    "1 * chi_{-20} with off-pp support EMPTY -- the "
                    "leak is exactly the class group" % N_INT,
                    ok_law and ok_rep)
    return ok_all, lam_A, sites


# ============================ S4 the bridge to the relational carrier
def s4_bridge(env):
    section("S4 -- THE BRIDGE: the relational carrier is the first "
            "row of the incidence operator")
    ok_all = True
    M, C, L360 = env["M"], env["C"], env["L360"]
    L60, LS = env["L60"], env["LS"]

    def lsym(n):
        return sp.Add(*[int(k) * LS[p] for p, k in LOGD[n].items()])

    # S4.1 per-divisor term equality + sums
    ok_row = True
    for m in range(2, N_INT + 1):
        acc = {}
        for d in DIVS[m]:
            t_car = ld_scale(LOGD[m // d], int(MU[d]))
            t_mat = ld_scale(C.get((d, m), {}), -M.get((1, d), 0))
            if not ld_eq(t_car, t_mat):
                ok_row = False
            ld_axpy(acc, 1, t_car)
        if not ld_eq(acc, L360.get((1, m), {})):
            ok_row = False
    ok_all &= check("S4.1 [EXACT] the deployed Moebius-pairing "
                    "reconstruction sum_{d|m} mu(d) U(m/d) at TRUE "
                    "positions U = log is LITERALLY the first row of "
                    "L_N: per-divisor term equality mu(d) log(m/d) == "
                    "-M_{1,d}[D,Z]_{d,m} for EVERY d | m and every "
                    "m <= %d, and the sums == L[1, m]" % N_INT, ok_row)

    # S4.2 the pairing matrix B is a sub-block of Z^{-1}
    events = [1] + [n for n in range(2, X_SUPPORT + 1) if ISPP[n]]
    ok_B = True
    n_sub = 0
    for u in events:
        for v in events:
            if v % u:
                continue
            n_sub += 1
            if int(MU[v // u]) != M.get((u, v), 0):
                ok_B = False
    ok_all &= check("S4.2 [EXACT] the pairing matrix B[k,j] = "
                    "mu(m_k/m_j) on the deployed comb support (prime "
                    "powers in [2, %d] + unit; %d divisor pairs) == "
                    "the sub-block of M = Z^{-1} -- the deployed "
                    "design was already reading the inverse incidence "
                    "operator" % (X_SUPPORT, n_sub), ok_B)

    # S4.3 row self-similarity
    ok_shift = True
    for a in range(1, N_INT + 1):
        for b in range(a, N_INT + 1, a):
            if not ld_eq(L360.get((a, b), {}),
                         L360.get((1, b // a), {})):
                ok_shift = False
    ok_all &= check("S4.3 [EXACT] row self-similarity L[a, ab] == "
                    "L[1, b] for all ab <= %d: every row is the first "
                    "row on the shifted sub-poset -- the carrier "
                    "generalizes verbatim to all rows" % N_INT,
                    ok_shift)

    # S4.4 untapped structure: Selberg Lambda_2 scalar + operator
    ok_l2s = True
    for n in range(1, N_SYM + 1):
        lam2 = sp.Integer(0)
        for d in DIVS[n]:
            if MU[d]:
                lam2 += int(MU[d]) * lsym(n // d) ** 2
        lamn = LS[int(PPRIME[n])] if (n > 1 and ISPP[n]) else \
            sp.Integer(0)
        conv = sp.Integer(0)
        for d in DIVS[n]:
            e = n // d
            ld_ = LS[int(PPRIME[d])] if (d > 1 and ISPP[d]) else None
            le_ = LS[int(PPRIME[e])] if (e > 1 and ISPP[e]) else None
            if ld_ is not None and le_ is not None:
                conv += ld_ * le_
        if sp.expand(lam2 - (lamn * lsym(n) + conv)) != 0:
            ok_l2s = False
    L2mat = mm(L60, L60, expand=True)
    ok_l2o = True
    for a in range(1, N_SYM + 1):
        for b in range(a, N_SYM + 1, a):
            r = b // a
            lam2 = sp.Integer(0)
            for d in DIVS[r]:
                if MU[d]:
                    lam2 += int(MU[d]) * lsym(r // d) ** 2
            got = (L2mat.get((a, b), sp.Integer(0))
                   - (lsym(a) - lsym(b))
                   * L60.get((a, b), sp.Integer(0)))
            if sp.expand(got - lam2) != 0:
                ok_l2o = False
    ok_all &= check("S4.4 [EXACT -- sympy] the untapped structure is "
                    "the Selberg hierarchy: mu * log^2 == Lambda log "
                    "+ Lambda*Lambda scalar for all n <= %d AND "
                    "T(mu * log^2) == L^2 - [D, L] entrywise -- the "
                    "carrier read row 1 of L; rows are shifts (S4.3), "
                    "powers are ordered factorization chains (S2), "
                    "and the power/bracket combinations are the "
                    "higher von Mangoldt functions" % N_SYM,
                    ok_l2s and ok_l2o)
    return ok_all


# ================================================================= main
def main():
    section("PRIME.RELATION.MANGOLDT.01 -- the von Mangoldt commutator "
            "theorem (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    L_N := -M[D,Z] with Z = [1_{a|b}], M = Z^{-1}, "
          "D = diag(log a).  Classical incidence-algebra content, "
          "typed as such.  NO RH claim; writes nothing.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbols; own "
          "sieves; the divisor/mu arithmetic is admissible input "
          "(it IS the Euler-product datum)", not bad,
          "found %s" % bad if bad else "clean")

    build_arithmetic()
    ok1, env = s1_exact()
    ok2 = s2_powers_log(env)
    ok3, lam_A, sites = s3_four_combs()
    ok4 = s4_bridge(env)

    section("V -- FROZEN VERDICT")
    if ok1 and ok2 and ok3 and ok4:
        verdict = "MANGOLDT-COMMUTATOR-EXACT"
    elif ok1:
        verdict = "MANGOLDT-COMMUTATOR-PARTIAL"
    else:
        verdict = "FAIL"
    print("\n  VERDICT: %s   [S1 exact: %s | S2 powers/log: %s | "
          "S3 four-comb: %s | S4 bridge: %s]"
          % (verdict, "OK" if ok1 else "FAIL", "OK" if ok2 else "FAIL",
             "OK" if ok3 else "FAIL", "OK" if ok4 else "FAIL"))
    if verdict == "MANGOLDT-COMMUTATOR-EXACT":
        print("""
  THE FINDING (typed honestly): the von Mangoldt commutator theorem
  L_N = -M[D,Z] = T(Lambda) is verified EXACTLY (sympy log-integer
  basis at N = 60, integer/Fraction layer at N = 360, float ward at
  N = 10^4) -- it is classical incidence-algebra arithmetic (mu*log
  = Lambda in matrix clothes), NOT new mathematics; its measured
  operator packaging delivers:
    (1) the power formula: L^k enumerates ordered factorization
        chains into prime powers with weight prod Lambda(r_j);
        nilpotency degree = floor(log2 N) + 1;
    (2) the log: log Z is RATIONAL (1/k at ratio p^k) and
        L = -Z^{-1}[D,Z] = -[D, log Z] EXACTLY (the BCH series
        truncates: [log Z, [log Z, D]] = 0); [D,Z] = -Z L is
        Chebyshev's 1*Lambda = log at operator level;
    (3) the four-comb discipline transported to operator level: the
        commutator machine ALWAYS outputs T(Lambda_f) (T is an
        algebra iso) -- Selberg consistency is a SUPPORT statement;
        TRUE / chi4-twist / zeta_{Q(i)} (scalar AND ideal-level,
        with norm aggregation (1+chi4) Lambda) are exactly prime-
        power-supported; the h = 2 Epstein comb x^2+5y^2 leaks at
        [6, 14, 21, ...], first unramified site 21 = 3x7, values
        pinned exactly, and the leak is REPAIRED by the class
        average (a_A + a_B = 1 * chi_{-20}): the operator-level
        discriminator localizes the class-group obstruction;
    (4) the bridge: the deployed relational carrier's mu-pairing
        reconstruction IS the first row of L_N (per-divisor term
        equality); rows are shifts, powers are chain correlations,
        and L^2 - [D, L] = T(mu * log^2) -- the untapped structure
        is the Selberg hierarchy.
  NO RH claim: nothing here bounds zeros; the deliverable is the
  exact operator identity + the typed discriminator + the carrier
  bridge, exploration-grade only.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    dt = time.time() - T0
    check("V.1 runtime %.1f s within budget %.0f s" % (dt,
          RUNTIME_BUDGET_S), dt <= RUNTIME_BUDGET_S)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (dt, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name (cross-probe READ-ONLY imports resolve to
    the embedded copies); capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ("arf_bent_css_probe", _SRC_BENT, 22, (), "ARF-BENT-CSS-EXACT", 0),
    ("mangoldt_incidence_probe", _SRC_MANGOLDT, 30, (),
     "MANGOLDT-COMMUTATOR-EXACT", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v853 -- ARF.BENT.CSS.01 + PRIME.RELATION.MANGOLDT.01")
    print("(q* is bent with Walsh eigenvalue -4; the (16,6,2) "
          "difference set; the two")
    print("CSS codes [[15,5,3]] -> [[16,4,4]] with the vacuum "
          "transformation typed; the")
    print("-4 triple point Hecke = Gauss = Walsh; L = -M[D,Z] = "
          "-[D, log Z] = T(Lambda)")
    print("exact with the four-comb discipline at operator level and "
          "the carrier bridge;")
    print("frozen protocols embedded byte-exact; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v853: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("Part B typed honestly: classical incidence-algebra "
          "arithmetic in matrix")
    print("clothes -- the deliverable is the exact operator identity, "
          "the typed")
    print("class-group discriminator, and the carrier bridge; nothing "
          "bounds zeros.")
    print("[%s] v853 VERDICT GATE: ARF-BENT-CSS-EXACT + "
          "MANGOLDT-COMMUTATOR-EXACT" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
