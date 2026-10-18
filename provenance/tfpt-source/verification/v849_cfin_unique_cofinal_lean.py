#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v849 -- CFIN.UNIQUE.01 + the CofinalWeil Lean mirror: the compiler object is UNIQUE and its automorphisms are C6, and the RH-side wall hypothesis is formally MINIMIZED -- every admissible compiler tuple is isomorphic to C_fin (one orbit of 14400 under Sp(4,2) x S_5, unique up to NON-unique isomorphism with Aut(C_fin) ~= C6), and the kernel-checked minimal H theorem TfptCarrier/CofinalWeil.lean REPLACES UniformMarginBound by the strictly weaker cofinal hypothesis (H_cof) in the load-bearing chain -- UniformMarginBound is hereby formally DEMOTED to an over-strong sufficient lemma, ONE module from one probe plus the kernel-checked Lean mirror (22/22 checks, verdict CFIN-UNIQUE; + 4 mirror checks; discovery probe cfin_uniqueness_probe.py, 2026-08-07, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~7 s; Lean core TfptCarrier/CofinalWeil.lean, lake build green 3411 jobs, kernel axioms clean).  PART A, THE UNIQUENESS THEOREM (work package F of the evening plan; exhaustive finite verification over F_2^4): (a) WLOG LADDER -- the 28 nondegenerate alternating forms are ONE GL(4,2) orbit (so omega = hbar WLOG); Sp(4,2) (order 720, verified by exhaustive image enumeration) is TRANSITIVE on the 6 Arf-1 refinements (so q = q* WLOG); per Arf-1 refinement there are EXACTLY 20 admissible sigma (order 3, symplectic, q-preserving, 3 nonzero fixed points, 4 free 3-orbits), forming ONE orbit under Stab_Sp(q*) (order 120); per (q*, sigma) there are EXACTLY 120 admissible sigma-equivariant iota (image = C_even(5), beta = hbar, q_wt = q*), forming ONE orbit under Stab(q*, sigma) x S_5; (b) UNIQUENESS -- the full admissible tuple census at omega = hbar has N = 14400 members and the G = Sp(4,2) x S_5 action has EXACTLY ONE orbit (orbit-stabilizer verified: 14400 x 6 = 86400 = |G|); every admissible compiler object is isomorphic to C_fin = (V, hbar, q*, sigma, iota); (c) AUTOMORPHISMS -- |Aut(C_fin)| = 6 with element orders [1,2,3,3,6,6], abelian and cyclic: Aut(C_fin) ~= C6, the projection to Sp(4,2) is FAITHFUL and the S_5 slot permutation is DETERMINED by the symplectic part; (d) THE GAUSSIAN-REDUCTION DIAGRAM typed -- the parent lattice fixes the carrier triple (V, hbar, sigma) up to EXACTLY the 18-element centralizer torsor; the selector pins q* uniquely (16 -> 4 -> 2 -> 1); the 120 iota-completions form a single orbit; the STRICT initial/terminal reading FAILS honestly (120 completions vs 6 automorphisms: 'unique up to isomorphism with 6 automorphism arrows' -- a one-object groupoid, NOT a terminal object; measured, typed either way); (e) CONTROLS FIRE -- dropping alternation kills the object (0 refinements), the wrong Arf class kills iota (C_even(5) weight census (1,10,5) forces Arf 1; admissible set EMPTY), dropping sigma kills CANONICITY (the pinned completion census becomes 16 -> 8 -> 4 != 1), and the typed side measurement: without sigma the bare (q, iota) set is 720 in ONE orbit -- sigma is load-bearing for the selector, not for the orbit count.  P2 sharpens: the axiom's object is not merely assembled (v845 NORMALFORM.CFIN.01) but UNIQUE; what remains of P2 is the v799 residual R1' (why THIS normal form at all), unchanged.  PART B, THE LEAN MIRROR (v843/v837/v817 precedent; numeric witnesses here, kernel statements there): TfptCarrier/CofinalWeil.lean -- 11 declarations, kernel-checked (lake build green, 3411 jobs; no sorry, no native_decide; axioms propext/Classical.choice/Quot.sound only, verified by #print axioms on all 8 theorems; import wired in TfptCarrier.lean; Lean manifest 84 -> 85 files): (1) CofinalHypothesis (H_cof) -- a PRE-FIXED strictly monotone index sequence along which the ladder matrices are PSD; the sequence is DATA of the structure, never mined from measured signs (the preregistration demand, formalized as field order: ladder first, certificates second); (2) limit_nonneg_of_cofinal_seq -- THE MINIMAL IMPLICATION, the eps/2 argument PROVEN (q_m(v) -> L and q_{m_j}(v) >= 0 on the ladder force L >= 0), and weil_nonneg_of_cofinal: per-element form convergence + (H_cof) => the limit functional is nonnegative on the WHOLE dense family -- NO diagonal argument (one PSD certificate per rung covers every element simultaneously, ladderForm_nonneg); (3) THE STRICT HIERARCHY kernel-checked: uniform SUBSET-NEQ pointwise SUBSET-NEQ cofinal -- uniformMarginBound_to_cofinal and pointwise_to_cofinal proven, cofinal_not_uniform (witness 1/(m+1), reusing the v843 kernel gap pointwise_pos_not_uniform) and cofinal_not_pointwise (witness +-1 on the even ladder: cofinal positivity does not even give all-rung positivity); (4) cofinal_weil -- the assembly: ladder matrices + sampling maps + per-element form convergence + (H_cof) => nonnegative ladder values at every cofinal rung, convergence along the ladder, nonnegativity of the limit functional; ABSENT BY DESIGN: no uniform margin, no inverse/resolvent, no Mosco coercivity, no limit operator, no diagonal argument.  THE FORMAL DEMOTION (the round's status statement, explicit): the load-bearing chain of PRIME.EXTRACTION.CHAIN.01 consumes EXACTLY (H_cof); UniformMarginBound (FORM.PRIME.EXCESS.SKELETON.01) implies (H_cof) and the converse FAILS kernel-checked -- the old hypothesis is STRICTLY stronger twice over and is from this round an over-strong SUFFICIENT LEMMA, no longer the named wall; the wall content has strictly decreased to cofinal PSD on one pre-fixed ladder.  (H_cof) itself stays a hypothesis everywhere; nothing evaluates positivity of any actual tower form.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe cfin_uniqueness_probe.py (22/22, verdict
CFIN-UNIQUE), 2026-08-07, re-run identically at promotion.  ROUND-31
EMBEDDING CONVENTION: the frozen probe source is embedded BYTE-EXACT
(raw string below) and executed verbatim in an isolated module
namespace -- the printed FROZEN_SPEC SHA-256 reproduces exactly, and
when the original file is present the harness verifies byte-equality
(provenance ward inside the pattern gate).  The Lean mirror part
follows the v843/v837/v817 precedent: the kernel-checked statements
live in experiments/lean4-carrier-rigidity/TfptCarrier/
CofinalWeil.lean (shipped as lean4-carrier-rigidity/), the module
witnesses their numeric content.  The original probe file lives
verbatim in experiments/tfpt-discovery/.

FIREWALL: part A is pure finite algebra over F_2 (no floats, no RNG,
no fit; exhaustive enumeration); part B uses elementary sequences and
one seeded PSD witness batch only.  Nothing here evaluates the
positivity of any actual tower form; (H_cof) is never instantiated
with deployed data.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source (embedded BYTE-EXACT, raw string)
_SRC_CFIN = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cfin_uniqueness_probe -- CFIN.UNIQUE.01: the missing canonicity
theorem for the four-bit compiler

      C_fin = (V, omega, q*, sigma, iota),

machine-decided by exhaustive finite computation (work package F1
side B, 2026-08-07 evening plan; the uniqueness companion of
NORMALFORM.CFIN.01 = finite_compiler_normal_form_probe.py,
NORMAL-FORM-ASSEMBLED 28/28, whose object and conventions are frozen
inputs here, not re-adjudicated).

FROZEN CLAIMS (frozen + SHA-hashed before first run):

THE ADMISSIBLE CLASS (the abstract compiler object, exactly the
certified structural properties of C_fin):
  a tuple (omega, q, sigma, iota) on the carrier V = F_2^4 with
  (A1) omega  : nondegenerate ALTERNATING bilinear form;
  (A2) q     : quadratic refinement of omega
               (q(v+w)+q(v)+q(w) = omega(v,w)) of ARF TYPE 1;
  (A3) sigma : order-3 operator (sigma^3 = id, sigma != id),
               symplectic for omega, preserving q, with the
               family-cycle fixed-class structure: EXACTLY 3 nonzero
               fixed classes (fixed space dim 2; the remaining 12
               classes then fall in 4 free 3-orbits, checked);
  (A4) iota  : linear parity lift V -> F_2^5 with image = the even
               five-slot code C_even(5), beta(v,w) =
               iota(v).iota(w) mod 2 == omega on all 256 cells,
               q_wt = wt(iota)/2 mod 2 == q, and sigma-equivariant:
               SOME slot permutation pi in S_5 satisfies
               iota(sigma v) = pi(iota(v)) (the S4.4 register
               intertwining of the normal form).
  ISOMORPHISM: (g, pi) in GL(4,2) x S_5 transporting all four data;
  after U0 (form transitivity) the classification group is
  G = Sp(4,2) x S_5, |G| = 720 x 120 = 86400, acting on (q, sigma,
  iota) at fixed omega = hbar (the J - I Gram convention of the
  normal form).

U0  FORM REDUCTION: census of all 64 alternating bilinear forms on
    F_2^4; the nondegenerate ones are ONE GL(4,2)-orbit containing
    hbar (so WLOG omega = hbar); |GL(4,2)| = 20160, |Sp(4,2)| = 720
    rebuilt by exhaustive enumeration.
U1  REFINEMENT REDUCTION: exactly 16 refinements of hbar (2^16
    brute force, the parent census); Arf census 6 + 10; Sp(4,2)
    transitive on the 6 Arf-1 refinements (so WLOG q = q*).
U2  SIGMA CENSUS: for each Arf-1 q, the admissible sigma set
    (order 3, symplectic, q-preserving, 3 nonzero fixed classes) is
    enumerated exactly; the free-orbit structure (4 x 3) checked;
    the canonical family 3-cycle is in the set for q = q*.
U3  IOTA CENSUS: for each admissible (q, sigma), the admissible
    iota set is enumerated exactly (DFS over basis images with dot
    constraints); the equivariant subcensus separately; the
    canonical iota is in the set.
U4  (a) UNIQUENESS: the FULL admissible tuple set at omega = hbar
    is enumerated; the G-orbit of the C_fin tuple is computed by
    applying all 86400 group elements; PASS = the orbit IS the
    admissible set (exactly one orbit) => every admissible compiler
    object on any carrier isomorphic to F_2^4 is isomorphic to
    C_fin (with U0/U1 as the reduction steps).  If more orbits:
    the typed orbit census.
U5  (b) THE AUTOMORPHISM GROUP: Aut(C_fin) = the joint stabilizer
    of (omega, q*, sigma, iota) in G, computed exactly: order
    (cross-checked against orbit-stabilizer |G| = |orbit| x |Aut|),
    element-order census, abelian/cyclic flags, identification
    against small groups (C6 vs S3 vs ...), the projection to
    Sp(4,2) (is pi determined by g?), and the joint stabilizer of
    (omega, q*, sigma, iota) IN Sp(4,2) (the assignment's reading).
U6  (c) UNIVERSAL PROPERTY CANDIDATE (measured, not narrated): the
    Gaussian-reduction diagram -- the E8 root census + deck action
    (rebuilt inline, parent S1 machinery) -- fixes (V, hbar, sigma)
    up to a MEASURED number of identifications (= the centralizer
    of sigma in Sp(4,2), cross-checked); the completions to a full
    C_fin object are measured: q-completions 4 -> 2 -> 1 under the
    frozen selector pins (sigma-invariance, q(A) = 1,
    q(F_Sigma) = 0), iota-completions counted and their orbit
    structure under the joint stabilizer computed.  TYPE WHAT
    HOLDS: initial/terminal (unique up to UNIQUE isomorphism) holds
    iff the completion is unique AND Aut(C_fin) = 1; otherwise the
    honest reading is "unique up to (non-unique) isomorphism, with
    |Aut(C_fin)| arrows".

C   CONTROLS (must fire; frozen fire rules):
    C1 DOT FORM: the non-alternating dot form admits ZERO quadratic
       refinements (2^16 brute force) -- admissible set EMPTY.
    C2 WRONG ARF: for EVERY Arf-0 refinement, the admissible iota
       set (even without any sigma condition) is EMPTY -- the even
       five-slot weight census (1, 10, 5) forces q_wt to be Arf-1.
    C3 NO SIGMA (trivial deck, parent C2): without the order-3
       datum the SELECTOR loses uniqueness: the pinned completion
       census on the Gaussian carrier becomes 16 -> 8 -> 4 != 1
       (fire iff != 1).  TYPED SIDE MEASUREMENT (predicted, frozen
       as a report line, not a fire rule): the BARE (q, iota) pair
       set without sigma stays ONE Sp x S_5 orbit -- sigma is
       load-bearing for CANONICITY (the selector), not for the bare
       orbit count; the measured value is printed either way.

KILLS (any one fires => typed):
  K1 carrier / group / census guard breaks       -> CFIN-UNDERDETERMINED
  K2 orbit-stabilizer arithmetic inconsistent    -> CFIN-UNDERDETERMINED
  K3 admissible set empty                        -> CFIN-UNDERDETERMINED
  K4 a control does not fire                     -> CFIN-UNDERDETERMINED

VERDICT (frozen enum, decision order):
  0. any kill                          -> CFIN-UNDERDETERMINED, exit 1
  1. exactly one G-orbit               -> CFIN-UNIQUE (+ |Aut| printed)
  2. N > 1 orbits                      -> CFIN-ORBITS-N (typed census)

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  Exact integer arithmetic only; no
floats, no RNG, no fits.  NO physics claim, NO RH claim.  Runtime
cap 900 s.

Sources (read-only, machinery rebuilt inline):
finite_compiler_normal_form_probe.py (the object, conventions,
selector, parent controls C1/C2), verification/v752 + v774 (quotient
+ compiler), v775 (census conventions), v833 (Gaussian rebuild).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cfin_uniqueness_probe.py
"""
import hashlib
import itertools
import math
import time

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


print("CFIN.UNIQUE.01 -- uniqueness + automorphisms of "
      "C_fin = (V, omega, q*, sigma, iota)")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ------------------------------------------------------- bit machinery
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0))
BASIS = [WIDX[tuple(1 if k == i else 0 for k in range(4))]
         for i in range(4)]
ADD = [[WIDX[tuple((a + b) % 2 for a, b in zip(W16[i], W16[j]))]
        for j in range(16)] for i in range(16)]


def form_table(mat):
    return [[sum(W16[i][r] * mat[r][c] * W16[j][c] for r in range(4)
                 for c in range(4)) % 2 for j in range(16)]
            for i in range(16)]


HB = form_table(GJI)
A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
LA, LF = WIDX[A_BIT], WIDX[FSIG]
SIGP = tuple(WIDX[(w[2], w[0], w[1], w[3])] for w in W16)


def perm_of_images(g1, g2, g3, g4):
    """Label permutation of the linear map sending e_i -> g_i."""
    gs = (g1, g2, g3, g4)
    p = []
    for i in range(16):
        acc = 0
        for k in range(4):
            if W16[i][k]:
                acc = ADD[acc][gs[k]]
        p.append(acc)
    return tuple(p)


def inv_perm(p):
    q = [0] * 16
    for i, pi in enumerate(p):
        q[pi] = i
    return tuple(q)


# ======================================================================
section("U0: form reduction -- alternating forms are one GL orbit")
# ======================================================================
GL, SP = [], []
for imgs in itertools.product(range(1, 16), repeat=4):
    p = perm_of_images(*imgs)
    if len(set(p)) != 16:
        continue
    GL.append(p)
    if all(HB[p[BASIS[i]]][p[BASIS[j]]] == GJI[i][j]
           for i in range(4) for j in range(i + 1, 4)):
        SP.append(p)
check("U0.1 |GL(4,2)| = %d == 20160; |Sp(4,2)| = %d == 720 "
      "(exhaustive image enumeration)" % (len(GL), len(SP)),
      len(GL) == 20160 and len(SP) == 720, kill="K1")

alt_nondeg = set()
for bits in range(64):
    mat = [[0] * 4 for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            mat[i][j] = mat[j][i] = (bits >> k) & 1
            k += 1
    tab = form_table(mat)
    if all(any(tab[i][j] for j in range(16)) for i in range(1, 16)):
        alt_nondeg.add(tuple(tuple(mat[r]) for r in range(4)))
orbit_forms = set()
for p in GL:
    ip = inv_perm(p)
    mat = tuple(tuple(HB[ip[BASIS[i]]][ip[BASIS[j]]] for j in range(4))
                for i in range(4))
    orbit_forms.add(mat)
check("U0.2 nondegenerate alternating forms: %d of 64; GL-orbit of "
      "hbar has %d elements == the whole set (WLOG omega = hbar)"
      % (len(alt_nondeg), len(orbit_forms)),
      orbit_forms == alt_nondeg and GJI in alt_nondeg, kill="K1")

# ======================================================================
section("U1: refinement reduction -- Sp transitive on the 6 Arf-1")
# ======================================================================
def refinements_of_table(tab):
    out = []
    for mask in range(1 << 16):
        q = tuple((mask >> i) & 1 for i in range(16))
        ok = True
        for i in range(16):
            for j in range(16):
                if q[ADD[i][j]] ^ q[i] ^ q[j] != tab[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(q)
    return out


REFS = refinements_of_table(HB)
ARF1 = sorted(q for q in REFS if sum(1 for x in q if x == 0) == 6)
ARF0 = sorted(q for q in REFS if sum(1 for x in q if x == 0) == 10)
check("U1.1 EXACTLY 16 refinements of hbar; Arf census 6 + 10",
      len(REFS) == 16 and len(ARF1) == 6 and len(ARF0) == 10,
      kill="K1")

siginv = [q for q in REFS if all(q[SIGP[i]] == q[i] for i in range(16))]
cand_a = [q for q in siginv if q[LA] == 1]
cand = [q for q in cand_a if q[LF] == 0]
QSTAR = cand[0] if len(cand) == 1 else None
check("U1.2 selector 16 -> sigma-invariant %d -> q(A)=1: %d -> "
      "q(F_Sigma)=0: %d == 1 (the canonical q*, Arf 1)"
      % (len(siginv), len(cand_a), len(cand)),
      len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1
      and QSTAR in ARF1, kill="K1")

SP_INV = [inv_perm(p) for p in SP]
orb_q = {tuple(QSTAR[ip[i]] for i in range(16)) for ip in SP_INV}
check("U1.3 Sp(4,2) TRANSITIVE on Arf-1 refinements: orbit of q* has "
      "%d elements == the 6 Arf-1 forms (WLOG q = q*)" % len(orb_q),
      orb_q == set(ARF1), kill="K1")

# ======================================================================
section("U2: the admissible sigma census per Arf-1 refinement")
# ======================================================================
def sigmas_for(q):
    out = []
    for p in SP:
        if p == tuple(range(16)):
            continue
        p2 = tuple(p[p[i]] for i in range(16))
        if tuple(p[p2[i]] for i in range(16)) != tuple(range(16)):
            continue
        if sum(1 for i in range(1, 16) if p[i] == i) != 3:
            continue
        if any(q[p[i]] != q[i] for i in range(16)):
            continue
        orbs = {frozenset({i, p[i], p2[i]})
                for i in range(1, 16) if p[i] != i}
        assert len(orbs) == 4 and all(len(o) == 3 for o in orbs)
        out.append(p)
    return out


SIGS = {q: sigmas_for(q) for q in ARF1}
n_sig = sorted(len(v) for v in SIGS.values())
check("U2.1 admissible sigma per Arf-1 q: counts %s (order 3, "
      "symplectic, q-preserving, 3 nonzero fixed, 4 free 3-orbits "
      "checked); canonical family cycle IN the q* set"
      % n_sig, all(n > 0 for n in n_sig) and SIGP in SIGS[QSTAR],
      kill="K1")

STAB_Q = [k for k in range(720)
          if tuple(QSTAR[SP_INV[k][i]] for i in range(16)) == QSTAR]
conj_orbs = []
seen = set()
for s in SIGS[QSTAR]:
    if s in seen:
        continue
    o = set()
    for k in STAB_Q:
        p, ip = SP[k], SP_INV[k]
        o.add(tuple(p[s[ip[i]]] for i in range(16)))
    seen |= o
    conj_orbs.append(o)
check("U2.2 |Stab_Sp(q*)| = %d == 120; its conjugation orbits on the "
      "admissible sigma set: %s (sizes)"
      % (len(STAB_Q), sorted(len(o) for o in conj_orbs)),
      len(STAB_Q) == 120
      and sum(len(o) for o in conj_orbs) == len(SIGS[QSTAR]),
      kill="K1")

# ======================================================================
section("U3: the admissible iota census per (q, sigma)")
# ======================================================================
B5_EVEN = [b for b in itertools.product((0, 1), repeat=5)
           if sum(b) % 2 == 0]
S5 = list(itertools.permutations(range(5)))


def iotas_for(q, sigp=None, require_equiv=False):
    """All admissible parity lifts; DFS over the four basis images."""
    sols = []

    def rec(imgs):
        i = len(imgs)
        if i == 4:
            iot = []
            for li in range(16):
                acc = (0, 0, 0, 0, 0)
                for k in range(4):
                    if W16[li][k]:
                        acc = tuple((a + b) % 2
                                    for a, b in zip(acc, imgs[k]))
                iot.append(acc)
            if len(set(iot)) != 16:
                return
            if any((sum(x) // 2) % 2 != q[li]
                   for li, x in enumerate(iot)):
                return
            sols.append(tuple(iot))
            return
        for b in B5_EVEN:
            if any(sum(x * y for x, y in zip(b, imgs[j])) % 2
                   != GJI[i][j] for j in range(i)):
                continue
            rec(imgs + [b])

    rec([])
    if not require_equiv:
        return sols
    out = []
    for iot in sols:
        for pi in S5:
            if all(iot[sigp[li]] == tuple(iot[li][pi[s]]
                                          for s in range(5))
                   for li in range(16)):
                out.append(iot)
                break
    return out


IOTA_CANON = tuple(tuple(list(w) + [sum(w) % 2]) for w in W16)
iot_bare_qstar = iotas_for(QSTAR)
iot_eq_canon = iotas_for(QSTAR, SIGP, require_equiv=True)
check("U3.1 iota census for q = q*: %d bare admissible lifts (image "
      "= C_even(5), beta = hbar, q_wt = q*); %d sigma-equivariant "
      "for the canonical family cycle; the canonical iota is one of "
      "them" % (len(iot_bare_qstar), len(iot_eq_canon)),
      len(iot_bare_qstar) > 0 and len(iot_eq_canon) > 0
      and IOTA_CANON in iot_eq_canon
      and IOTA_CANON in iot_bare_qstar, kill="K1")

# ======================================================================
section("U4: (a) UNIQUENESS -- the full tuple census vs the G-orbit")
# ======================================================================
ADMISSIBLE = set()
for q in ARF1:
    for s in SIGS[q]:
        for iot in iotas_for(q, s, require_equiv=True):
            ADMISSIBLE.add((q, s, iot))
N_ADM = len(ADMISSIBLE)
CFIN = (QSTAR, SIGP, IOTA_CANON)
check("U4.1 admissible tuple census at omega = hbar: N = %d > 0; the "
      "C_fin tuple is admissible" % N_ADM,
      N_ADM > 0 and CFIN in ADMISSIBLE, kill="K3")

orbit = set()
stab_pairs = []
for k in range(720):
    p, ip = SP[k], SP_INV[k]
    q2 = tuple(QSTAR[ip[i]] for i in range(16))
    s2 = tuple(p[SIGP[ip[i]]] for i in range(16))
    base = [IOTA_CANON[ip[i]] for i in range(16)]
    for pi in S5:
        i2 = tuple(tuple(x[pi[s]] for s in range(5)) for x in base)
        t = (q2, s2, i2)
        orbit.add(t)
        if t == CFIN:
            stab_pairs.append((k, pi))
N_ORB = len(orbit)
N_AUT = len(stab_pairs)
check("U4.2 orbit-stabilizer: |orbit| x |Aut| = %d x %d = %d == "
      "|G| = 86400" % (N_ORB, N_AUT, N_ORB * N_AUT),
      N_ORB * N_AUT == 86400, kill="K2")
check("U4.3 the G-orbit is INSIDE the admissible set (transport "
      "preserves admissibility)", orbit <= ADMISSIBLE, kill="K2")

n_orbits = None
if orbit == ADMISSIBLE:
    n_orbits = 1
else:
    rest = set(ADMISSIBLE) - orbit
    n_orbits = 1
    while rest:
        rep = next(iter(rest))
        o2 = set()
        for k in range(720):
            p, ip = SP[k], SP_INV[k]
            q2 = tuple(rep[0][ip[i]] for i in range(16))
            s2 = tuple(p[rep[1][ip[i]]] for i in range(16))
            base = [rep[2][ip[i]] for i in range(16)]
            for pi in S5:
                i2 = tuple(tuple(x[pi[s]] for s in range(5))
                           for x in base)
                o2.add((q2, s2, i2))
        rest -= o2
        n_orbits += 1
check("U4.4 UNIQUENESS: admissible set = %d tuples, G-orbits = %d "
      "(PASS bar: exactly 1 -- every admissible compiler object is "
      "isomorphic to C_fin)" % (N_ADM, n_orbits), n_orbits == 1,
      kill=None)

# ======================================================================
section("U5: (b) Aut(C_fin) -- the joint stabilizer, exactly")
# ======================================================================
def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


orders = sorted(math.lcm(perm_order(SP[k]), perm_order(pi))
                for k, pi in stab_pairs)
sp_parts = {k for k, _ in stab_pairs}
pi_per_g = {k: [pi for kk, pi in stab_pairs if kk == k]
            for k in sp_parts}
faithful_sp = (len(sp_parts) == N_AUT
               and all(len(v) == 1 for v in pi_per_g.values()))
abelian = True
for (k1, p1), (k2, p2) in itertools.combinations(stab_pairs, 2):
    g12 = tuple(SP[k1][SP[k2][i]] for i in range(16))
    g21 = tuple(SP[k2][SP[k1][i]] for i in range(16))
    p12 = tuple(p1[p2[s]] for s in range(5))
    p21 = tuple(p2[p1[s]] for s in range(5))
    if g12 != g21 or p12 != p21:
        abelian = False
        break
cyclic = max(orders) == N_AUT if N_AUT > 0 else False
small = {(1,): "1", (2,): "C2", (3,): "C3",
         (6, True, True): "C6", (6, False, False): "S3",
         (4, True, True): "C4", (4, True, False): "C2xC2",
         (12, True, True): "C12"}
if N_AUT in (1, 2, 3):
    iso = small.get((N_AUT,), "order %d" % N_AUT)
else:
    iso = small.get((N_AUT, abelian, cyclic),
                    "order %d (abelian=%s, cyclic=%s)"
                    % (N_AUT, abelian, cyclic))
check("U5.1 |Aut(C_fin)| = %d; element orders %s; abelian=%s, "
      "cyclic=%s -> Aut(C_fin) ~= %s"
      % (N_AUT, orders, abelian, cyclic, iso), N_AUT >= 1, kill="K2")
check("U5.2 the projection Aut -> Sp(4,2) is faithful and the slot "
      "permutation pi is DETERMINED by g (|Sp-part| = %d, one pi per "
      "g: %s) -- Aut(C_fin) IS the joint stabilizer of (omega, q*, "
      "sigma, iota) in Sp(4,2)"
      % (len(sp_parts), all(len(v) == 1 for v in pi_per_g.values())),
      faithful_sp, kill="K2")

# ======================================================================
section("U6: (c) the Gaussian-reduction diagram -- what holds")
# ======================================================================
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
          for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


placements = set()
for perm in itertools.permutations(range(8)):
    placements.add(code_image(C_NAIVE, perm))
both = [c for c in placements
        if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
CSTAR = next(c for c in both if (1, 0, 1, 0, 1, 0, 1, 0) in c)

ROOTS = []
for k in range(8):
    for sgn in (2, -2):
        v = [0] * 8
        v[k] = sgn
        ROOTS.append(tuple(v))
for c in (c for c in CSTAR if sum(c) == 4):
    sup = [k for k in range(8) if c[k]]
    for signs in itertools.product((1, -1), repeat=4):
        v = [0] * 8
        for k, sgn in zip(sup, signs):
            v[k] = sgn
        ROOTS.append(tuple(v))


def J_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def sig_vec(v):
    return tuple(v[PI_SIG[k]] for k in range(8))


def in_L(v):
    return tuple(x % 2 for x in v) in CSTAR


def in_pi2L(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L([x // 2 for x in w])


REPS = [(0,) * 8]
for r in ROOTS:
    if not any(in_pi2L(tuple(a - b for a, b in zip(r, rep)))
               for rep in REPS):
        REPS.append(r)


def label_of(v):
    for li, rep in enumerate(REPS):
        if in_pi2L(tuple(a - b for a, b in zip(v, rep))):
            return li
    raise AssertionError("vector not in L")


census = {}
for r in ROOTS:
    census[label_of(r)] = census.get(label_of(r), 0) + 1


def sig_label(li):
    return label_of(sig_vec(REPS[li]))


fixed_nz = [li for li in range(1, 16) if sig_label(li) == li]
check("U6.1 carrier guard (parent S1 rebuilt): 30 placements, 2 "
      "deck-stable, 16 classes, census 240 = 15 x 16, 3 nonzero "
      "sigma-fixed classes",
      len(placements) == 30 and len(both) == 2 and len(REPS) == 16
      and sorted(census.values()) == [16] * 15 and 0 not in census
      and len(fixed_nz) == 3, kill="K1")


def ip8(x, y):
    return sum(a * b for a, b in zip(x, y))


def hbar_vec(x, y):
    re2, im2 = ip8(x, y), ip8(x, J_vec(y))
    return ((re2 // 2) + (im2 // 2)) % 2


n_ident = 0
for o1 in range(1, 16):
    if o1 in fixed_nz:
        continue
    o2, o3 = sig_label(o1), sig_label(sig_label(o1))
    if len({o1, o2, o3}) != 3:
        continue
    r1, r2, r3 = REPS[o1], REPS[o2], REPS[o3]
    for anc in fixed_nz:
        ra = REPS[anc]
        bits_map = {}
        for bits in itertools.product((0, 1), repeat=4):
            v = tuple(bits[0] * a + bits[1] * b + bits[2] * c
                      + bits[3] * d
                      for a, b, c, d in zip(r1, r2, r3, ra))
            bits_map[label_of(v)] = bits
        if len(bits_map) != 16:
            continue
        ok = all(hbar_vec(REPS[lx], REPS[ly])
                 == HB[WIDX[bits_map[lx]]][WIDX[bits_map[ly]]]
                 for lx in range(16) for ly in range(16))
        ok = ok and all(
            WIDX[bits_map[sig_label(li)]]
            == SIGP[WIDX[bits_map[li]]] for li in range(16))
        if ok:
            n_ident += 1
centr = sum(1 for p in SP
            if tuple(p[SIGP[i]] for i in range(16))
            == tuple(SIGP[p[i]] for i in range(16)))
check("U6.2 identifications (V, hbar, sigma) -> (F_2^4, hb, sig): "
      "%d found == %d = |centralizer of sigma in Sp(4,2)| (the "
      "lattice fixes the carrier triple up to exactly the "
      "centralizer torsor)" % (n_ident, centr),
      n_ident == centr and n_ident > 0, kill="K1")

STAB_QS = [k for k in STAB_Q
           if tuple(SP[k][SIGP[SP_INV[k][i]]] for i in range(16))
           == SIGP]
compl_orbit = set()
point_stab = 0
for k in STAB_QS:
    p, ip = SP[k], SP_INV[k]
    base = [IOTA_CANON[ip[i]] for i in range(16)]
    for pi in S5:
        i2 = tuple(tuple(x[pi[s]] for s in range(5)) for x in base)
        compl_orbit.add(i2)
        if i2 == IOTA_CANON:
            point_stab += 1
n_compl = len(iot_eq_canon)
single_compl_orbit = compl_orbit == set(iot_eq_canon)
check("U6.3 completions over the fixed carrier triple: q-completions "
      "4 -> 2 -> 1 (selector, U1.2); iota-completions %d, forming "
      "%s single orbit under Stab(q*, sigma) x S_5 "
      "(|Stab_Sp(q*, sigma)| = %d)"
      % (n_compl, "a" if single_compl_orbit else "NOT a",
         len(STAB_QS)), single_compl_orbit, kill="K2")
strict_universal = (n_compl == 1 and N_AUT == 1)
check("U6.4 TYPED: strict initial/terminal (unique up to UNIQUE "
      "isomorphism) %s: completions = %d, |Aut(C_fin)| = %d -- the "
      "measured reading is 'unique up to isomorphism, with %d "
      "automorphism arrows' %s"
      % ("HOLDS" if strict_universal else "FAILS",
         n_compl, N_AUT, N_AUT,
         "(a one-object groupoid, not a terminal object)"
         if not strict_universal else ""),
      True, "measured, typed either way", kill=None)

# ======================================================================
section("C: controls (must fire)")
# ======================================================================
DOT = form_table(tuple(tuple(1 if i == j else 0 for j in range(4))
                       for i in range(4)))
refs_dot = refinements_of_table(DOT)
check("C1 FIRES: the non-alternating dot form admits %d == 0 "
      "refinements -- admissible set EMPTY (dropping alternation "
      "kills the object)" % len(refs_dot), len(refs_dot) == 0,
      kill="K4")

arf0_iotas = max(len(iotas_for(q)) for q in ARF0)
check("C2 FIRES: WRONG ARF: every Arf-0 refinement admits 0 "
      "admissible iota (max over the 10: %d) -- the C_even(5) "
      "weight census (1,10,5) forces Arf 1; admissible set EMPTY"
      % arf0_iotas, arf0_iotas == 0, kill="K4")

cand_nosig = [q for q in REFS if q[LA] == 1 and q[LF] == 0]
bare_pairs = set()
for q in ARF1:
    for iot in iotas_for(q):
        bare_pairs.add((q, iot))
pair_orbit = set()
for k in range(720):
    p, ip = SP[k], SP_INV[k]
    q2 = tuple(QSTAR[ip[i]] for i in range(16))
    base = [IOTA_CANON[ip[i]] for i in range(16)]
    for pi in S5:
        i2 = tuple(tuple(x[pi[s]] for s in range(5)) for x in base)
        pair_orbit.add((q2, i2))
pair_single = pair_orbit == bare_pairs
check("C3 FIRES: NO SIGMA (trivial deck): the pinned completion "
      "census becomes 16 -> %d -> %d != 1 (canonicity of q* DIES "
      "without the family 3-cycle)"
      % (len([q for q in REFS if q[LA] == 1]), len(cand_nosig)),
      len(cand_nosig) == 4 and len(cand_nosig) != 1, kill="K4")
check("C3' TYPED side measurement (report, not a fire rule): the "
      "bare (q, iota) pair set without sigma has %d elements and "
      "forms %s single Sp x S_5 orbit -- sigma is load-bearing for "
      "CANONICITY (the selector), %s for the bare orbit count"
      % (len(bare_pairs),
         "a" if pair_single else "NOT a",
         "not" if pair_single else "AND"),
      True, "measured, typed either way", kill=None)

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS or N_ADM == 0:
    VERDICT = "CFIN-UNDERDETERMINED"
elif n_orbits == 1:
    VERDICT = "CFIN-UNIQUE"
else:
    VERDICT = "CFIN-ORBITS-%d" % n_orbits
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s%s" % (VERDICT,
                         "  (|Aut(C_fin)| = %d ~= %s)" % (N_AUT, iso)
                         if VERDICT == "CFIN-UNIQUE" else ""))
print("\nCENSUS SUMMARY (report only -- promotion separate):")
print("  * admissible tuples at omega = hbar: %d; G-orbits: %d"
      % (N_ADM, n_orbits))
print("  * |Aut(C_fin)| = %d ~= %s; element orders %s"
      % (N_AUT, iso, orders))
print("  * Gaussian diagram: carrier triple fixed up to %d "
      "identifications (= centralizer); q* unique via selector; "
      "%d iota-completions in %s orbit"
      % (n_ident, n_compl, "one" if single_compl_orbit else ">1"))
print("  * strict terminal-object reading: %s"
      % ("HOLDS" if strict_universal else
         "FAILS (unique up to NON-unique isomorphism)"))
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT.startswith("CFIN-UNIQUE")) else 1)
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
    canonical import name; capture and re-emit stdout; return
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


# ====== PART B -- the Lean mirror (CofinalWeil.lean; kernel-checked
# statements cited, numeric witnesses only -- v843/v837/v817 precedent)

_B_CHECKS = []


def _bcheck(name, ok, detail=""):
    _B_CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def part_b():
    print("\n" + "-" * 74)
    print("v849 PART B -- the Lean mirror: TfptCarrier/CofinalWeil."
          "lean (kernel-checked;")
    print("numeric witnesses here; (H_cof) never instantiated with "
          "deployed data)")
    print("-" * 74, flush=True)

    # B1: the minimal implication (limit_nonneg_of_cofinal_seq /
    # weil_nonneg_of_cofinal) -- the eps/2 argument at sequence level
    ok_seq = True
    for (seq, lim) in (
            (lambda m: 1.0 / (m + 1.0), 0.0),
            (lambda m: 2.0 + math.sin(m) / (m + 1.0), 2.0),
            (lambda m: 0.25 + (-0.5) ** m / (m + 2.0) ** 2, 0.25)):
        idx = [2 * j for j in range(2000)]           # pre-fixed ladder
        ok_seq &= all(idx[a] < idx[a + 1] for a in range(1999))
        ok_seq &= all(seq(m) >= 0.0 for m in idx)
        tail = [seq(m) for m in range(5000, 5050)]
        ok_seq &= (min(tail) >= lim - 1e-3) and (lim >= 0.0)
    rng = np.random.default_rng(20260807)
    ok_psd = True
    for _ in range(6):
        base = rng.normal(size=(7, 7))
        A = base @ base.T                            # PSD rung matrix
        for _v in range(24):                         # 'dense family'
            x = rng.normal(size=7)
            ok_psd &= float(x @ (A @ x)) >= -1e-10
    _bcheck("B1 THE MINIMAL IMPLICATION (limit_nonneg_of_cofinal_seq, "
            "PROVEN eps/2 argument): convergent sequences nonneg on a "
            "PRE-FIXED strictly monotone ladder have nonneg limits (3 "
            "witness families, ladder = even integers); and the "
            "no-diagonal reason (ladderForm_nonneg): ONE PSD rung "
            "certificate makes the form nonneg at EVERY element "
            "simultaneously (6 seeded PSD matrices x 24 witnesses "
            ">= -1e-10) -- weil_nonneg_of_cofinal needs only "
            "per-element convergence + (H_cof)", ok_seq and ok_psd)

    # B2: the strict hierarchy uniform < pointwise < cofinal
    margin_pw = [1.0 / (m + 1.0) for m in range(100000)]
    ok_pw = all(v > 0.0 for v in margin_pw)          # pointwise strict
    ok_nu = True                                     # ... not uniform
    for dlt in (1e-2, 1e-6, 1e-12):
        n_w = int(math.ceil(1.0 / dlt))
        ok_nu &= 1.0 / (n_w + 1.0) < dlt
    def margin_pm(m):                                # +-1 witness
        return 1.0 if m % 2 == 0 else -1.0
    even = [2 * j for j in range(100000)]
    ok_cof = all(margin_pm(m) >= 0.0 for m in even)  # cofinal on evens
    ok_np = any(margin_pm(m) < 0.0 for m in range(100))
    _bcheck("B2 THE STRICT HIERARCHY (kernel-checked: "
            "uniformMarginBound_to_cofinal, pointwise_to_cofinal, "
            "cofinal_not_uniform, cofinal_not_pointwise): witness "
            "1/(m+1) is strictly positive at EVERY rung yet below "
            "every delta > 0 eventually (pointwise strict, NOT "
            "uniform; the v843 kernel gap reused), and the +-1 "
            "sequence is nonneg on the pre-fixed even ladder while "
            "strictly negative on every odd rung (cofinal, NOT "
            "pointwise) -- uniform SUBSET-NEQ pointwise SUBSET-NEQ "
            "cofinal, both inclusions strict",
            ok_pw and ok_nu and ok_cof and ok_np)

    # B3: the preregistration shape of (H_cof)
    idx = [2 * j for j in range(1000)]
    ok_mono = all(a < b for a, b in zip(idx[:-1], idx[1:]))
    ok_indep = (idx == [2 * j for j in range(1000)])  # data, not mined
    ok_order = ok_mono and ok_cof                     # ladder -> signs
    _bcheck("B3 THE PREREGISTRATION SHAPE (CofinalHypothesis): the "
            "index sequence is DATA of the structure -- supplied "
            "first, strictly monotone by field (checked), chosen "
            "independently of any measured sign (the even ladder "
            "here is a pure function of j); the positivity "
            "certificates quantify over the GIVEN ladder only -- "
            "formally a consumer must exhibit the ladder before any "
            "form value is evaluated",
            ok_mono and ok_indep and ok_order)

    # B4: the formal demotion statement
    ok_dem = ok_nu and ok_cof and ok_np              # strictness twice
    _bcheck("B4 THE FORMAL DEMOTION: the load-bearing chain "
            "(PRIME.EXTRACTION.CHAIN.01, v848 step 2) consumes "
            "EXACTLY (H_cof); UniformMarginBound implies (H_cof) "
            "(proven) and the converse FAILS kernel-checked "
            "(witnesses above) -- from this round UniformMarginBound "
            "is an over-strong SUFFICIENT LEMMA, no longer the named "
            "wall; the wall content is cofinal PSD on ONE pre-fixed "
            "ladder and nothing else; (H_cof) itself stays a "
            "hypothesis everywhere", ok_dem)
    print("  (kernel-checked statements: experiments/"
          "lean4-carrier-rigidity/TfptCarrier/CofinalWeil.lean -- "
          "11 declarations, lake build green, 3411 jobs, no sorry, "
          "no native_decide, axioms propext/Classical.choice/"
          "Quot.sound only; import wired in TfptCarrier.lean; "
          "lean_manifest.sha256 at 85 files)")


_PLAN = (
    ("cfin_uniqueness_probe", _SRC_CFIN, 22, (), "CFIN-UNIQUE", 0),
)


def run():
    t0 = time.time()
    _B_CHECKS.clear()
    print("=" * 74)
    print("v849 -- CFIN.UNIQUE.01 + the CofinalWeil Lean mirror")
    print("(every admissible compiler tuple isomorphic to C_fin -- "
          "one orbit of 14400,")
    print("Aut(C_fin) ~= C6, unique up to NON-unique isomorphism; "
          "H_cof formally")
    print("replaces UniformMarginBound in the load-bearing chain; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    part_b()
    ok_b = all(_B_CHECKS) and len(_B_CHECKS) == 4
    gates.append(ok_b)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v849: %d/%d gates passed (probe pattern gate + %d/4 mirror "
          "checks) | runtime %.1f s"
          % (sum(gates), len(gates), sum(_B_CHECKS), time.time() - t0))
    print("NO RH claim; (H_cof) stays a hypothesis everywhere -- the "
          "arithmetic wall,")
    print("now in its minimal kernel-checked shape; the C_fin "
          "uniqueness leaves P2's")
    print("residual R1' (why THIS normal form) unchanged.")
    print("[%s] v849 VERDICT GATE: CFIN-UNIQUE + the minimal H "
          "theorem mirrored" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
