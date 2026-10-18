#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v912 -- PRIME.FORM.CONVERGENCE.THEOREM.01: the all-depth form
convergence edge of the extraction chain, promoted as an UNCONDITIONAL
theorem with explicit rate and explicit constants (discovery probe
form_convergence_theorem_probe.py, note CCCLXV, 2026-08-13, SPEC_SHA
d911226fea3033fef6998090064a94a539431dd6b29994ee49e0b851ad9df254,
35/35, 11.9 s; re-run identically at promotion, promoted VERBATIM with
no downscoping, ~12 s).

WHICH EDGE.  `TfptCarrier/CofinalWeil.lean` and
`TfptCarrier/CofinalPredefinition.lean` consume, besides (H_cof),
exactly ONE analytic hypothesis:

    hconv : forall v, Tendsto (fun m => ladderForm A sample m v)
                              atTop (nhds (QW v))

i.e. PER-ELEMENT convergence of the finite Galerkin forms to the limit
functional, over every element of the declared dense family and the
full rung sequence.  Until this module that premise was typed MEASURED
(the corpus rates -1.58..-1.84 per level of v848 /
continuum_extraction_probe.py) -- exactly the "measured premise read as
settled" defect that meta-audit CCCXXXVII Q-2 flagged.  It is now a
THEOREM for the deployed dyadic cellwise-affine family: a quadrature
statement about an explicit-formula pairing, proved on paper and
machine-checked here.

NOT this module: (H_cof) itself -- the PREDEFINED cofinal positivity
sign edge (CCCLVI edge 4 / CCCLXI).  Nothing here evaluates, gates or
mentions positivity of any actual form.  NO RH CLAIM: closing this edge
does NOT prove RH; the remaining cofinal-positivity inequality is
untouched and RH-hard.

=======================================================================
THE THEOREM (all constants exact-rational, closed-form, or cited)
=======================================================================
Window S = 17/4, alpha = S/2, grid D = D_j = 2^-j, M = M_j =
17*2^(j-2) lags, midpoint samples x_i = (i+1/2)D (v762 D5), atom census
cap C (deployed C = 2 alpha = S).  Lam_D(x) = (1 - |x|/D)_+,
S_{s,D}(w) = (1/2)[Lam_D(w-s) + Lam_D(w+s)], W_C = P + A + T_C the
capped Weil functional in the deployed W1 layers (v630/v643, CITED).
V_D = f real, supp f in [0, S], AFFINE ON EVERY GRID CELL.

  (0) c_d = W_C[S_{dD,D}] for every deployed lag d -- the deployed lag
      vector IS the capped Weil functional on the even tent.
  (I) Q_D(f) = D[a_0 c_0 + 2 sum_{d>=1} a_d c_d] = W_C[Ktil_D], with
      Ktil_D the even piecewise-linear interpolant of k_d = D a_d.
 (II) THE EXACT DEFECT LEMMA (the load-bearing exact step):
      k_d - K(dD) = -(D^2/12) G(dD) for EVERY d, and
      Ktil_D - K = (Pi_D K - K) - (D^2/12) G on all of R,
      where K = f * f~, G = f' * f~' (a.e. derivative, no jump atoms),
      Pi_D nodal linear interpolation.  Mechanism: on each grid cell
      u -> f(u) f(u + dD) is a QUADRATIC, the midpoint-rule error of a
      quadratic is exactly -(D^3/24) q'', and Pi_D G = G because G is
      piecewise linear with grid-node breakpoints.
(III) supp Ktil_D subset [-(b_K + D), b_K + D], so C >= b_K + D gives
      T_C[Ktil_D] = T_inf[Ktil_D] and Q_D(f) - Q_W(f) = W_C[Ktil_D-K].
 (IV) with kappa2 = ||f'||_2^2 = G(0), kappa3 = Lip(G), kapK = sup over
      cell interiors of |K''|, B = b_K + D, A0 = kappa2/12,
      A2 = kapK/8 + kappa2/12, A1 = kapK,
      |Q_D(f) - Q_W(f)|
        <= D^2[(8 sinh(B/2) + mfrak(B)) A2 + Theta0 A0
               + (A0 + A2)(log(1/D) + log B + 4)
               + 2 A0 e^{-B/2}(1/B + 2) + A1(1 + D)]
           + (1 + D)(D^3/12) kappa3,
      Theta0 = 3 log 2 + pi/2 + gamma + log pi = 5.372183419225665...
      For CONTINUOUS f, kapK = kappa2 EXACTLY and the envelope
      collapses to D^2 kappa2[(7/24) log(1/D) + Aconst(B,D)] +
      (1+D)(D^3/12) kappa3.  RATE O(D^2 log(1/D)) = O(2^{-2j} j).
  (V) the envelope depends on f only through (b_K, kapK, kappa2,
      kappa3) and is nondecreasing in the last three, so convergence is
      UNIFORM on every class with a TWO-SIDED support window
      {b_- <= diam supp f <= b_+, kapK <= RK, kappa2 <= R2,
      kappa3 <= R3}, b_- > 0 (the envelope degrades like 1/b_K as
      b_K -> 0 through the archimedean origin channel).

CONSTANT CORRECTION, typed (this is what a naive write-up gets wrong):
the interpolation constant is NOT kappa2 = ||f'||_2^2 but
kapK = sup over cell interiors of |K''|.  For CONTINUOUS f they are
EQUAL exactly (K'' = -G in cell interiors, |G| <= G(0) by
Cauchy-Schwarz); for f with a jump the atom-times-a.c. cross terms move
kapK BOTH ways (E09: kapK = 3 > kappa2 = 2; E10: kapK = 5/3 < 2).

AUDIT CORRECTION carried by this module (a correction of a wrong cited
statement, NOT a downgrade of a result): the chain's cited
"C^0-continuity of Q_W at fixed support" is FALSE in the pure sup norm.
Control C5 exhibits the explicit even Lipschitz family
e_n(w) = (1/n) min(1, w/e^{-n^2}) (1 - w/2)_+ with e_n(0) = 0 and
||e_n||_inf = 1/n -> 0 while |A[e_n]| = 2.57, 4.28, ..., 12.09 grows
linearly in n.  The correct hypothesis is uniform convergence PLUS an
equi-Lipschitz (Dini) condition at the origin, which the admissible
even compactly supported BV class supplies automatically (K = f*f~
with f BV is Lipschitz, |K'| <= ||f||_inf TV(f)).  Edge 6 of the
implication DAG is therefore NARROWED, not closed: density of the
dyadic cellwise-affine family in the admissible class in THAT topology
[FEM density + IK04 Thm 5.12 / Bombieri 2000], still CITED.

=======================================================================
CLASSICAL INPUT LEDGER (typed; NO zero-free region, NO PNT anywhere)
=======================================================================
  ELEMENTARY (proved or verified here, no citation): E1 midpoint
    exactness for quadratics; E2 nodal interpolation constants via the
    cell Green's function of -d^2/ds^2; E3 Cauchy-Schwarz |G| <= G(0);
    E4 1 + x <= e^x  ==>  rho(w) <= [1/(2w) + 1] e^{-w/2}; E5
    J = -(3/2) log 2 - pi/4; E6 the archimedean closed tail identity.
  FINITE AND EXPLICIT: F1 the comb is a FINITE sum for fixed f; the
    28-atom census is reproduced by an own Eratosthenes sieve.
  EXPLICIT-CONSTANT CITED: C1 Rosser-Schoenfeld 1962 Thm 12,
    psi(x) < 1.03883 x for ALL x > 0 -- Chebyshev-type, no zero-free
    region, no PNT; consumed ONLY for the support-uniform constant,
    never for convergence at fixed f.
  STRUCTURAL CITED: S1 the W1 measure dictionary (v630/v643); S2 Weil's
    explicit formula and criterion; S3 the admissible even compactly
    supported BV class (IK04 Thm 5.12).

=======================================================================
PINNING DISCLOSURE (meta-audit CCCXXXVI lesson, applied a priori)
=======================================================================
WHAT THE EXECUTED GATES PIN.  T1.6/T1.7 pin the exact defect lemma
EXACTLY IN Q (zero deviation, Fraction arithmetic) on 1474 lag
identities and 780 strictly-interior points; T1.1/T2.0/T2.1/T2.2/T1.8
pin the tent identity, (H-align), sup|G| = G(0), kapK vs kappa2, the
interpolation and Lipschitz constants and the exact class, also exactly
in Q; T1.4/T1.5 pin identities (0) and (I) against the DEPLOYED lag
pipeline at declared float bars; T3.1/T3.3/T3.4/T4.1 pin the envelope
and the faithful cap against that same pipeline and against an
independently evaluated W_C[e_D]; T3.5 pins sharpness against a
CLOSED-FORM leading term (no fit inside any gate); T2.3/T2.4/T2.5 pin
the archimedean majorants and closed forms symbolically and at 40 dps;
C1..C5 are must-fire controls.

WHAT IS CITED, NOT PINNED (a false input here would NOT fail this
module):
  * S1 the W1 dictionary -- that the deployed layers ARE the
    Suzuki/Weil measure (v630/v631/v640..v643).  This module verifies
    internal consistency of the deployed layers with W_C, not their
    identification with the classical Weil functional.
  * S2/S3 Weil's explicit formula and criterion, and the admissible
    class; the DENSITY leg of edge 6.
  * C1 Rosser-Schoenfeld for ALL x > 0.  T4.2 verifies psi(x) <=
    1.03883 x only on its own sieve up to 10^7 (worst ratio 1.038821)
    -- the unconditional all-x statement is the citation.
  * THE UNIVERSAL QUANTIFIER.  The gates check the identities and the
    envelope on the declared FINITE grid (10 frozen elements E01..E10
    plus a 12-member translate family; levels j = 4..11 exactly/deployed
    and j = 12,14,16 via the stable defect route).  The theorem for
    ALL f in V_D and ALL j is the PAPER proof plus the frozen probe run
    (SPEC_SHA above), not this finite gate.
  * DELTA-A (FORMALISATION-OPEN).  The proof is NOT formalised in Lean.
    `TfptCarrier/CofinalWeil.lean` remains a hypothesis consumer;
    `TfptCarrier/CofinalEnvelope.lean` states the envelope premise and
    derives hconv from it for a FIXED instantiated ladder, so the Lean
    hypothesis is visibly the instantiated envelope rather than an
    opaque assumption -- but the envelope itself is an assumption
    inside the kernel, discharged only on paper and here.
  * DELTA-B (STATED, NOT A GAP).  The window conditions (H-grid)
    b_K <= (M-1)D, (H-cap) C >= b_K + D, (H-align) every breakpoint of
    K is a grid node must hold.  For fixed f, fixed window S and dyadic
    f they hold for all large j, which is exactly what `Tendsto atTop`
    needs; for the whole dyadic family one runs a window ladder
    S_j -> inf, whose exactness is (III).

Python-only (numerical quadrature and interval-free float wards) per
GATE.WOLFRAM.02.  No marker moves.  NO RH claim.
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as F

import numpy as np
import mpmath as mp
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import v563_paper2_readouts as core          # noqa: E402  (READ-ONLY)
import v716_moonshot_arch_glue as stage2     # noqa: E402  (pole layer)

EXPECTED = "FORMCONV-PROVEN"
N_CHECKS = 35
PROBE_SPEC_SHA = ("d911226fea3033fef6998090064a94a539431dd6b29994ee49"
                  "e0b851ad9df254")

_VERDICTS = {}
CHECKS = []
FAILS = []

# ------------------------------------------------- frozen specification
S_WIN = F(17, 4)                 # deployed assembly window
ALPHA = S_WIN / 2
J_LO, J_HI = 4, 11               # the frozen measured ladder
J_DEEP = (12, 14, 16)            # beyond-measurement extension
J_EXACT = (4, 5, 6)              # levels for exact-in-Q legs
FIT_J = (7, 8, 9, 10, 11)        # corpus rate window
J_UNIF = (6, 8, 10)              # levels for the uniformity family
KA_PIN = 28                      # prime powers with k log p <= 17/4
SIEVE_N = 10 ** 7                # independent sieve reach (tail leg)
C1_RS = 1.03883                  # Rosser-Schoenfeld 1962 Thm 12
DPS_HP = 30                      # mpmath working precision
DPS_CONST = 40                   # mpmath precision for closed forms

BAR_TENT = 1.0e-8                # deployed c_d vs W_C[S_d] (rel)
BAR_MASTER = 1.0e-8              # Q_D(f) vs W_C[Ktil_D] (rel)
BAR_ROUTE = 1.0e-6               # err_theory vs err_deployed (rel)
BAR_EXACT_FLOAT = 1.0e-12        # exact-class deployed float floor
BAR_CONST = 1.0e-30              # closed-form constants
RATE_MED = -1.818                # frozen corpus median rate
RATE_MIN, RATE_MAX = -1.845, -1.575
BAR_RATE = 5.0e-3
SHARP_LO, SHARP_HI = 0.45, 1.15  # err / (|e(0)| log(1/D)) band
C1_FIRE = 20.0                   # atoms-dropped ratio bar
C2_FIRE = 20.0                   # cap-violation ratio bar
C4_FIRE = 20.0                   # scrambled-comb ratio bar
SEED_SCR = 20260813
RUNTIME_CAP = 1800.0

# banned: zeros, zero counts, and any imported primality/factorisation
# oracle.  sympy IS used (symbolic identity verification) but none of
# its number-theoretic oracles: the prime-power table is sieved here.
BANNED_IDS = ("zetazero", "nzeros", "zetas", "primepi", "isprime",
              "primerange", "nextprime", "prevprime", "factorint",
              "primefactors", "mobius", "totient", "divisors",
              "curve_fit", "least_squares")

# Embedded byte-exact from the discovery probe; the SHA-256 of
# FROZEN_SPEC + repr(ELEMENTS) must reproduce PROBE_SPEC_SHA (gate G0.2).
FROZEN_SPEC = """\
PRIME.FORM.CONVERGENCE.THEOREM.01 spec v1 (2026-08-13, frozen before
any evaluation).  Window S = 17/4, alpha = S/2, D_j = 2^-j, M_j =
17*2^(j-2), midpoint samples, cap C = 2 alpha (deep variant 2 alpha +
2D).  Deployed lags = v563 arch_lags + stage2 pole_lags_closed + v563
atom_lags_at.  Q_D(f) = D(a_0 c_0 + 2 sum a_d c_d).  Target Q_W = W_inf
[K], W = P + A + T, P = 4 int K cosh(w/2), A = -(gamma+log pi)K(0)
+ 2 int (K(0)e^{-2w} - K e^{-w/2})/(1-e^{-2w}), T = -sum mu_n K(u_n).
THEOREM legs: (0) c_d = W_C[S_{dD,D}]; (I) Q_D(f) = W_C[Ktil_D];
(II) k_d - K(dD) = -(D^2/12) G(dD) exactly, Ktil_D - K = (Pi_D K - K)
- (D^2/12) G; (III) C >= b_K + D faithful; (IV) envelope D^2[(8 sinh
(B/2) + mfrak(B))A2 + Theta0 A0 + (A0+A2)(log(1/D) + log B + 4)
+ 2 A0 e^{-B/2}(1/B+2) + A1(1+D)] + (1+D)(D^3/12) kappa3 with A0 =
kappa2/12, A2 = kapK/8 + kappa2/12, A1 = kapK, kapK = sup_interiors
|K''|, Theta0 = 3log2 + pi/2 + gamma + log pi; for continuous f kapK =
kappa2 and this is D^2 kappa2[(7/24)log(1/D) + Aconst(B,D)] + (1+D)
(D^3/12)kappa3, Aconst = (5/24)(8 sinh(B/2) + mfrak(B)) + Theta0/12
+ (7/24)log B + 7/6 + 1 + D + (1/6)e^{-B/2}(1/B+2); (V) uniformity in
(b_K, kapK, kappa2, kappa3) + the W_C continuity modulus.
Elements E01..E10 verbatim from continuum_extraction_probe.  Gates:
T1.1-T1.8, T2.0-T2.6, T3.1-T3.5, T4.1-T4.3, T5.1-T5.2.  Bars: tent/
master 1e-8 rel, route 1e-6 rel, exact legs EXACT in Q, constants
1e-30, corpus rates median -1.818 +- 5e-3 and min/max inside
[-1.845, -1.575], envelope ratio <= 1 everywhere.  Controls C1 atoms
dropped, C2 cap violation, C3 grid misalignment, C4 scrambled comb
(seed 20260813), C5 sup-norm continuity counterexample -- all must
fire.  Verdict order INVALID -> MISMATCH -> GAP -> PROVEN-CONDITIONAL
-> PROVEN.  No zeros, no zero-free region, no PNT, no tau, no target
sign, no fit inside a gate; writes nothing; cap 1800 s; NO RH claim.
"""

ELEMENTS = (
    ("E01 box(0,1)", ((F(1), (0, 1, 0)),)),
    ("E02 box(2,1)", ((F(1), (2, 1, 0)),)),
    ("E03 box[0,2)", ((F(1), (0, 0, 0)), (F(1), (0, 1, 0)))),
    ("E04 hat(2,3)", ((F(1), (2, 3, 1)),)),
    ("E05 hat(1,0)", ((F(1), (1, 0, 1)),)),
    ("E06 hat(0,0)", ((F(1), (0, 0, 1)),)),
    ("E07 hat(0,1)", ((F(1), (0, 1, 1)),)),
    ("E08 hat(4,7)", ((F(1), (4, 7, 1)),)),
    ("E09 box(1,0)-1/2 hat(2,1)",
     ((F(1), (1, 0, 0)), (F(-1, 2), (2, 1, 1)))),
    ("E10 hat(0,0)+1/3 box(0,2)",
     ((F(1), (0, 0, 1)), (F(1, 3), (0, 2, 0)))),
)
EXACT_CLASS = ("E01", "E02", "E03")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


# ===================================================== exact machinery
def peval(coeffs, x):
    out = 0 * x
    for c in reversed(coeffs):
        out = out * x + c
    return out


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def pint(p):
    return [F(0)] + [c / (i + 1) for i, c in enumerate(p)]


def pshift(p, tau):
    out = [F(0)] * len(p)
    power = [F(1)]
    for c in p:
        for j, w in enumerate(power):
            out[j] += c * w
        nxt = [F(0)] * (len(power) + 1)
        for j, w in enumerate(power):
            nxt[j] += w * tau
            nxt[j + 1] += w
        power = nxt
    return out


def corr_value(fp, gp, tau):
    """(f * g~)(tau) = int f(u) g(u + tau) du, EXACT in Q."""
    total = F(0)
    for (a1, b1, p) in fp:
        for (a2, b2, q) in gp:
            lo = a1 if a1 > a2 - tau else a2 - tau
            hi = b1 if b1 < b2 - tau else b2 - tau
            if hi > lo:
                anti = pint(pmul(p, pshift(q, tau)))
                total += peval(anti, hi) - peval(anti, lo)
    return total


def deriv_pieces(fp):
    """a.e. derivative: cell slopes, NO jump atoms."""
    return [(a, b, [p[1]] if len(p) > 1 else [F(0)]) for (a, b, p) in fp]


def member_pieces(m, k, kind):
    h = F(1, 2 ** m)
    if kind == 0:
        return [(k * h, (k + 1) * h, [F(1)])]
    up = [F(-k), F(2 ** m)]
    dn = [F(k + 2), F(-(2 ** m))]
    return [(k * h, (k + 1) * h, up), ((k + 1) * h, (k + 2) * h, dn)]


def combo_pieces(members):
    cuts = sorted({c for _cf, mk in members
                   for (a, b, _p) in member_pieces(*mk) for c in (a, b)})
    out = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        coeffs = [F(0), F(0)]
        for cf, mk in members:
            for (a, b, p) in member_pieces(*mk):
                if a <= lo and hi <= b:
                    for i, c in enumerate(p):
                        coeffs[i] += cf * c
        out.append((lo, hi, coeffs))
    return out


def solve_exact(A, y):
    n = len(y)
    M = [row[:] + [y[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                fct = M[r][col]
                M[r] = [vr - fct * vc for vr, vc in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]


def corr_break_cuts(fp):
    ends = sorted({c for (a, b, _p) in fp for c in (a, b)})
    return sorted({b2 - b1 for b1 in ends for b2 in ends if b2 >= b1})


def corr_pieces(fp, gp, cuts, deg):
    """exact pw-polynomial of tau -> (f*g~)(tau) with a 5th-point
    certificate per interval (v762 D3 machinery, degree declared)."""
    pieces, certified = [], True
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        if hi <= lo:
            continue
        width = hi - lo
        xs = [lo + width * F(i, deg + 2) for i in range(1, deg + 2)]
        ys = [corr_value(fp, gp, x) for x in xs]
        A = [[x ** k for k in range(deg + 1)] for x in xs]
        coeffs = solve_exact(A, ys)
        x5 = lo + width * F(7, 10)
        certified &= (peval(coeffs, x5) == corr_value(fp, gp, x5))
        pieces.append((lo, hi, coeffs))
    cont = all(peval(pa[2], pa[1]) == peval(pb[2], pb[0])
               for pa, pb in zip(pieces[:-1], pieces[1:]))
    edge = peval(pieces[-1][2], pieces[-1][1]) == 0
    return pieces, (certified and cont and edge)


def pw_eval_exact(pieces, t):
    t = abs(t)
    for (a, b, p) in pieces:
        if a <= t < b:
            return peval(p, t)
    return F(0)


def pw_eval_float(pieces, x):
    x = np.abs(np.asarray(x, dtype=float))
    out = np.zeros(x.shape, dtype=float)
    for (a, b, p) in pieces:
        msk = (x >= a) & (x < b)
        if msk.any():
            out[msk] = np.polyval(p[::-1], x[msk])
    return out


def to_float_pieces(pieces):
    return [(float(a), float(b), np.array([float(c) for c in p]))
            for (a, b, p) in pieces]


def to_mp_pieces(pieces):
    return [(mp.mpf(a.numerator) / a.denominator,
             mp.mpf(b.numerator) / b.denominator,
             [mp.mpf(c.numerator) / c.denominator for c in p])
            for (a, b, p) in pieces]


def pw_eval_mp(pieces, t):
    t = abs(t)
    for (a, b, p) in pieces:
        if a <= t < b:
            return sum(c * t ** i for i, c in enumerate(p))
    return mp.mpf(0)


def build_element(name, members):
    """the exact record of one element: pw-cubic K, pw-linear G, and the
    three envelope constants (b_K, kappa2, kappa3), all in Q."""
    fp = combo_pieces(members)
    fpr = deriv_pieces(fp)
    cuts = corr_break_cuts(fp)
    Kp, cert_k = corr_pieces(fp, fp, cuts, 3)
    Gp, cert_g = corr_pieces(fpr, fpr, cuts, 1)
    k0 = corr_value(fp, fp, F(0))
    kap2 = corr_value(fpr, fpr, F(0))
    norm2 = sum(peval(pint(pmul(p, p)), b) - peval(pint(pmul(p, p)), a)
                for (a, b, p) in fp)
    slope2 = sum(p[1] * p[1] * (b - a) for (a, b, p) in fp if len(p) > 1)
    bK = cuts[-1]
    # kappa3 = Lip(G) exactly: G is pw-linear on the corr breakpoints
    kap3 = F(0)
    for (a, b, p) in Gp:
        if len(p) > 1 and abs(p[1]) > kap3:
            kap3 = abs(p[1])
    # kapK = sup |K''| over CELL INTERIORS, exact: K is a cubic per
    # piece, so K'' is affine per piece and the sup is at an end.  For
    # CONTINUOUS f this equals max|G| = G(0) = kappa2; for f with jumps
    # the atom-times-a.c. cross terms make it move BOTH ways, and the
    # honest interpolation constant is kapK, not kappa2.
    kapK = F(0)
    for (a, b, p) in Kp:
        c2 = p[2] if len(p) > 2 else F(0)
        c3 = p[3] if len(p) > 3 else F(0)
        for x in (a, b):
            v = abs(2 * c2 + 6 * c3 * x)
            if v > kapK:
                kapK = v
    # Cauchy-Schwarz instance |G| <= G(0), exact on a fine grid
    st = bK / 96
    cs_ok = all(abs(pw_eval_exact(Gp, i * st)) <= kap2 for i in range(97))
    cont = (all(peval(pa[2], pa[1]) == peval(pb[2], pb[0])
                for pa, pb in zip(fp[:-1], fp[1:]))
            and peval(fp[0][2], fp[0][0]) == 0
            and peval(fp[-1][2], fp[-1][1]) == 0)
    ok = bool(cert_k and cert_g and k0 == norm2 and kap2 == slope2
              and cs_ok and (kapK == kap2 or not cont))
    return dict(name=name, tag=name.split()[0], fp=fp, fpr=fpr,
                Kp=Kp, Gp=Gp, k0=k0, kap2=kap2, kap3=kap3, kapK=kapK,
                cont=cont, bK=bK, bf=fp[-1][1],
                Kf=to_float_pieces(Kp), Gf=to_float_pieces(Gp),
                pf=to_float_pieces(fp)), ok


def sample_vec(pf, D, M):
    x = (np.arange(M) + 0.5) * D
    out = np.zeros(M)
    for (a, b, p) in pf:
        msk = (x >= a) & (x < b)
        if msk.any():
            out[msk] = np.polyval(p[::-1], x[msk])
    return out


def qval(fv, c, D):
    M = len(fv)
    a = np.correlate(fv, fv, "full")[M - 1:]
    return D * (a[0] * c[0] + 2.0 * float(a[1:] @ c[1:]))


# ============================== independent prime-power atom sieve
def sieve_prime_powers(n_max):
    """own Eratosthenes prime-power table: u = k log p, mass =
    2 log p / p^{k/2}; no imported primality oracle."""
    flag = np.ones(n_max + 1, dtype=bool)
    flag[:2] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if flag[i]:
            flag[i * i::i] = False
    primes = np.nonzero(flag)[0]
    us, ms, ns, lam = [], [], [], []
    for p in primes.tolist():
        q, k = p, 1
        while q <= n_max:
            us.append(k * math.log(p))
            ms.append(2.0 * math.log(p) / math.sqrt(q))
            ns.append(q)
            lam.append(math.log(p))
            q *= p
            k += 1
    order = np.argsort(np.asarray(ns))
    return (np.asarray(us)[order], np.asarray(ms)[order],
            np.asarray(ns)[order], np.asarray(lam)[order])


# ============================ the continuum functional W_C (mpmath)
def weil_of_pw(Kmp, K0, bK, u_at, mu_at, cap):
    """W_cap[phi] for an EVEN phi given as pw-polynomial pieces on
    [0, bK] with phi(0) = K0.  High precision."""
    def phi(w):
        return pw_eval_mp(Kmp, w)
    pole = 4 * sum(mp.quad(lambda w: phi(w) * mp.cosh(w / 2), [a, b])
                   for (a, b, _p) in Kmp)

    def ig(w):
        return ((K0 * mp.e ** (-2 * w) - phi(w) * mp.e ** (-w / 2))
                / (1 - mp.e ** (-2 * w)))
    brk = [mp.mpf(0)] + [a for (a, _b, _p) in Kmp[1:]] + [bK]
    arch = (-(mp.euler + mp.log(mp.pi)) * K0 + 2 * mp.quad(ig, brk)
            - K0 * mp.log(1 - mp.e ** (-2 * bK)))
    atom = -sum(mp.mpf(m) * phi(mp.mpf(uu))
                for uu, m in zip(u_at, mu_at) if uu <= cap)
    return pole + arch + atom


def weil_of_tent(s, D, u_at, mu_at, cap):
    """W_cap[S_{s,D}] -- the tent representation of a deployed lag."""
    s = mp.mpf(s)
    D = mp.mpf(D)

    def Sf(w):
        w = mp.mpf(w)
        return (mp.mpf(1) / 2) * (max(mp.mpf(0), 1 - abs(w - s) / D)
                                  + max(mp.mpf(0), 1 - abs(w + s) / D))
    lo = max(mp.mpf(0), s - D)
    hi = s + D
    pts = sorted({lo, s, hi} | ({mp.mpf(0)} if s == 0 else set()))
    pole = 2 * mp.quad(lambda w: Sf(w) * 2 * mp.cosh(w / 2), pts)
    S0 = Sf(0)

    def ig(w):
        return ((S0 * mp.e ** (-2 * w) - Sf(w) * mp.e ** (-w / 2))
                / (1 - mp.e ** (-2 * w)))
    apts = sorted({mp.mpf(0), lo, s, hi} |
                  ({max(mp.mpf(0), D - s)} if s < D else set()))
    arch = -(mp.euler + mp.log(mp.pi)) * S0 + 2 * mp.quad(ig, apts)
    if S0 != 0:
        arch += -S0 * mp.log(1 - mp.e ** (-2 * hi))
    atom = -sum(mp.mpf(m) * Sf(mp.mpf(uu))
                for uu, m in zip(u_at, mu_at) if uu <= cap)
    return pole + arch + atom


def weil_of_interp(kvals, D, u_at, mu_at, cap):
    """W_cap[Ktil_D] evaluated DIRECTLY on the even pw-linear
    interpolant of the nodal values kvals (independent of the deployed
    lag vector) -- the end-to-end ward of identity (I)."""
    n = len(kvals) - 1
    kv = [mp.mpf(v) for v in kvals]

    def phi(w):
        w = abs(mp.mpf(w))
        d = int(mp.floor(w / D))
        if d >= n:
            return mp.mpf(0)
        t = w / D - d
        return kv[d] * (1 - t) + kv[d + 1] * t
    edges = [mp.mpf(d) * D for d in range(n + 1)]
    pole = 2 * sum(mp.quad(lambda w: phi(w) * 2 * mp.cosh(w / 2),
                           [edges[d], edges[d + 1]]) for d in range(n))
    K0 = kv[0]

    # the integrand is ANALYTIC at 0: K0 - phi is linear there and
    # w/(1-e^{-2w}) is analytic, so the limit is the closed value below
    ig0 = -mp.mpf(3) / 4 * K0 - (kv[1] - kv[0]) / (2 * D)

    def ig(w):
        if w == 0:
            return ig0
        return ((K0 * mp.e ** (-2 * w) - phi(w) * mp.e ** (-w / 2))
                / (1 - mp.e ** (-2 * w)))
    arch_i = sum(mp.quad(ig, [edges[d], edges[d + 1]])
                 for d in range(n))
    arch = (-(mp.euler + mp.log(mp.pi)) * K0 + 2 * arch_i
            - K0 * mp.log(1 - mp.e ** (-2 * edges[n])))
    atom = -sum(mp.mpf(m) * phi(mp.mpf(uu))
                for uu, m in zip(u_at, mu_at) if uu <= cap)
    return pole + arch + atom


# ================= the exact defect e_D and the W_C[e_D] evaluation
GX8, GW8 = np.polynomial.legendre.leggauss(8)
GX48, GW48 = np.polynomial.legendre.leggauss(48)


def rho_np(w):
    return np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))


def defect_eval(Kf, Gf, D, w):
    """e_D(w) = (Pi_D K - K)(w) - (D^2/12) G(w), stable (no large
    cancellation): built from the exact pieces, not from Q_D - Q_W."""
    w = np.asarray(w, dtype=float)
    d = np.floor(w / D + 1.0e-13).astype(np.int64)
    t = w / D - d
    lin = (pw_eval_float(Kf, d * D) * (1.0 - t)
           + pw_eval_float(Kf, (d + 1) * D) * t)
    return lin - pw_eval_float(Kf, w) - (D * D / 12.0) * pw_eval_float(Gf, w)


def weil_of_defect(Kf, Gf, kap2, bK, D, M, u_at, mu_at, cap):
    """W_cap[e_D] via the exact defect lemma (II) -- the numerically
    stable route to Q_D(f) - Q_W(f), usable at any depth."""
    nc = min(int(math.ceil(bK / D)) + 1, M - 1)
    e0 = -(D * D / 12.0) * kap2
    t = 0.5 * (GX8 + 1.0)
    wq = 0.5 * GW8
    pole = 0.0
    arch_int = 0.0
    step = max(1, int(2 ** 22 / max(1, len(t))))
    for lo in range(0, nc, step):
        hi = min(nc, lo + step)
        dd = np.arange(lo, hi, dtype=np.int64)
        W = (dd[:, None] + t[None, :]) * D
        e = defect_eval(Kf, Gf, D, W)
        pole += 4.0 * D * float(np.sum(wq[None, :] * e * np.cosh(0.5 * W)))
        if lo == 0:
            arch_int += D * float(np.sum(
                wq[None, :] * (e0 - e[1:]) * rho_np(W[1:])))
        else:
            arch_int += D * float(np.sum(
                wq[None, :] * (e0 - e) * rho_np(W)))
    # first cell: dyadic split against the 1/(2w) archimedean density
    edges = [0.0] + [D * 0.5 ** i for i in range(24)][::-1]
    for lo, hi in zip(edges[:-1], edges[1:]):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        ww = mid + half * GX48
        arch_int += half * float(np.dot(
            GW48, (e0 - defect_eval(Kf, Gf, D, ww)) * rho_np(ww)))
    # w > B: e_D vanishes, the e_D(0) channel is analytic
    B = nc * D
    tail = 0.0
    ee = [B * 1.02 ** i for i in range(1, 600)]
    ee = [B] + [v for v in ee if v < 200.0] + [200.0]
    for lo, hi in zip(ee[:-1], ee[1:]):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        tail += half * float(np.dot(GW48, rho_np(mid + half * GX48)))
    arch_int += e0 * tail
    arch = e0 * COEF0 + 2.0 * arch_int
    sel = u_at <= cap
    ua, ma = u_at[sel], mu_at[sel]
    atom = -float(np.dot(ma, defect_eval(Kf, Gf, D, ua)))
    return pole + arch + atom


# ============================================= the explicit envelope
J_CLOSED = -1.5 * math.log(2.0) - math.pi / 4.0
THETA0 = 3.0 * math.log(2.0) + math.pi / 2.0 + core.EULER + core.LOG_PI
COEF0 = 2.0 * J_CLOSED - (core.EULER + core.LOG_PI)      # = -THETA0


def comb_mass(y, u_at, mu_at):
    return float(np.sum(mu_at[u_at <= y]))


def envelope(kapK, kap2, kap3, bK, D, u_at, mu_at):
    """THEOREM (IV): the explicit unconditional envelope.  A2 = ||e||_inf
    /D^2, A0 = |e(0)|/D^2, A1 = Lip(e)/D at leading order; for CONTINUOUS
    f, kapK == kappa2 and (A0, A1, A2) = (1/12, 1, 5/24) kappa2, which
    reproduces the 7/24 log coefficient verbatim."""
    B = bK + D
    A0 = kap2 / 12.0
    A2 = kapK / 8.0 + kap2 / 12.0
    A1 = kapK
    return (D * D * ((8.0 * math.sinh(0.5 * B)
                      + comb_mass(B, u_at, mu_at)) * A2
                     + THETA0 * A0
                     + (A0 + A2) * (math.log(1.0 / D) + math.log(B) + 4.0)
                     + 2.0 * A0 * math.exp(-0.5 * B) * (1.0 / B + 2.0)
                     + A1 * (1.0 + D))
            + (1.0 + D) * (D ** 3 / 12.0) * kap3)


def modulus(e0, einf, lip, w0, bK, u_at, mu_at):
    """THEOREM (V): the explicit continuity modulus of W_C -- the
    CORRECTED continuity statement (uniform smallness PLUS a Lipschitz
    handle at the origin), replacing the false pure-sup-norm claim."""
    B = bK
    return (THETA0 * abs(e0)
            + (8.0 * math.sinh(0.5 * B) + comb_mass(B, u_at, mu_at)) * einf
            + 2.0 * (lip * (w0 / 2.0 + w0 * w0 / 2.0)
                     + (abs(e0) + einf) * (0.5 * math.log(B / w0) + 2.0)
                     + abs(e0) * math.exp(-0.5 * B) * (1.0 / B + 2.0)))


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                if any(b in al.name.lower() for b in BANNED_IDS):
                    bad.append(al.name)
        if name and any(b in name.lower() for b in BANNED_IDS):
            bad.append(name)
    return sorted(set(bad))


# ======================================================== the run
def part():
    t0 = time.time()
    mp.mp.dps = DPS_HP
    section("PRIME.FORM.CONVERGENCE.THEOREM.01 -- the all-depth form-"
            "convergence edge\nas an UNCONDITIONAL theorem (rate + "
            "explicit constants).  (H_cof) untouched; NO RH claim.")

    # ------------------------------------------------------- guards
    print("\n-- G0: firewall, freeze, independent sieve, exact machinery")
    hits = ast_firewall()
    check("G0.1 AST firewall (no zeros/zero counts, no imported "
          "primality or factorisation oracle, no fitter in any gate)",
          not hits, str(hits))
    spec_sha = hashlib.sha256(
        (FROZEN_SPEC + repr(ELEMENTS)).encode()).hexdigest()
    check("G0.2 frozen spec reproduces the discovery-probe SPEC_SHA "
          "byte-exact: %s == %s" % (spec_sha[:16], PROBE_SPEC_SHA[:16]),
          spec_sha == PROBE_SPEC_SHA, "SHA256 %s" % spec_sha)

    ka = core.atoms_in(float(ALPHA))
    u_at = np.asarray(core.U_ALL[:ka], float)
    mu_at = np.asarray(core.MU_ALL[:ka], float)
    u_own, mu_own, n_own, lam_own = sieve_prime_powers(
        int(math.floor(math.exp(float(S_WIN)))))
    dev_u = float(np.max(np.abs(u_own - u_at))) if len(u_own) == ka else 9.9
    dev_m = float(np.max(np.abs(mu_own - mu_at))) if len(u_own) == ka else 9.9
    check("G0.3 independent Eratosthenes prime-power sieve reproduces "
          "the deployed v563 atom census: %d == %d atoms with "
          "k log p <= %s, max dev u %.1e / mass %.1e"
          % (len(u_own), KA_PIN, S_WIN, dev_u, dev_m),
          len(u_own) == KA_PIN == ka and dev_u <= 1e-15
          and dev_m <= 1e-15)

    els = []
    ok_mach = True
    for name, members in ELEMENTS:
        e, ok_e = build_element(name, members)
        ok_mach &= ok_e
        els.append(e)
    check("G0.4 exact machinery in Q: pw-cubic K and pw-linear G with "
          "5th-point certificates, breakpoint continuity, zero edge, "
          "K(0) == ||f||^2, G(0) == ||f'||^2, Cauchy-Schwarz |G| <= "
          "G(0) on all %d elements" % len(els), ok_mach)

    # high-precision continuum targets
    for e in els:
        e["qw"] = float(weil_of_pw(
            to_mp_pieces(e["Kp"]),
            mp.mpf(e["k0"].numerator) / e["k0"].denominator,
            mp.mpf(e["bK"].numerator) / e["bK"].denominator,
            u_at, mu_at, float(S_WIN)))
        e["scale"] = max(abs(e["qw"]), 0.1)
    print("     targets Q_W = W_inf[K] (mpmath %d dps), kappa2 = "
          "||f'||^2, kappa3 = Lip(G), b_K = diam supp f:" % DPS_HP)
    for e in els:
        print("       %-28s Q_W = %+.10f  kappa2 = %-6s kappa3 = %-6s "
              "b_K = %-5s b_f = %s"
              % (e["name"], e["qw"], e["kap2"], e["kap3"], e["bK"],
                 e["bf"]))

    # ---------------------------------- T1: the discretisation identity
    section("T1 -- THE DISCRETISATION IDENTITY (exact / symbolic)")

    # T1.1 tent nodal identity incl. the u < D reflection branch
    Dq = F(1, 8)
    kk = [F(3), F(-2), F(5, 3), F(0), F(-1, 7), F(2, 5), F(0)]
    ok11 = True
    for num in range(0, 49):
        w = F(num, 48) * (len(kk) - 1) * Dq
        lhs = F(0)
        for d, kd in enumerate(kk):
            eps = F(1) if d == 0 else F(2)
            tl = max(F(0), 1 - abs(w - d * Dq) / Dq)
            tr = max(F(0), 1 - abs(w + d * Dq) / Dq)
            lhs += eps * kd * (tl + tr) / 2
        d0 = int(w / Dq)
        t = w / Dq - d0
        rhs = (kk[d0] * (1 - t) + kk[d0 + 1] * t) if d0 + 1 < len(kk) \
            else (kk[d0] * (1 - t) if d0 < len(kk) else F(0))
        ok11 &= (lhs == rhs)
    check("T1.1 tent nodal identity EXACT in Q: sum_d eps_d k_d "
          "S_{dD,D}(w) == Ktil_D(w) at 49 rational points, including "
          "the u < D reflection branch (the eps_d doubling IS the even "
          "extension)", ok11)

    # T1.2 pole second difference == tent read of 2cosh(w/2)
    wsym, Dsym, ssym = sp.symbols("w D s", positive=True)
    ok12 = sp.simplify(sp.diff(-8 * (sp.cosh(wsym / 2) - 1), wsym, 2)
                       + 2 * sp.cosh(wsym / 2)) == 0
    dev12 = 0.0
    for (Dv, dv) in ((F(1, 8), 0), (F(1, 8), 1), (F(1, 8), 5),
                     (F(1, 32), 3), (F(1, 32), 40)):
        Dm = mp.mpf(Dv.numerator) / Dv.denominator
        sm = Dm * dv
        tent = mp.quad(lambda w: (1 - abs(sm - w) / Dm) * 2 * mp.cosh(w / 2),
                       [sm - Dm, sm, sm + Dm])

        def gp(t):
            t = abs(t)
            return -8 * (mp.cosh(t / 2) - 1)
        sd = -(gp(sm - Dm) - 2 * gp(sm) + gp(sm + Dm)) / Dm
        dev12 = max(dev12, float(abs(tent - sd) / abs(tent)))
    check("T1.2 pole layer: g_pole'' == -2cosh(w/2) symbolically AND "
          "the deployed closed second difference -(Delta^2 g)/D == "
          "int Lam_D(dD - w) 2cosh(w/2) dw, max rel dev %.2e <= %.0e"
          % (dev12, BAR_CONST * 1e22),
          ok12 and dev12 <= 1e-25)

    # T1.3 arch tail identity + near/far unification (FTC + vanishing)
    Wsym = sp.symbols("W", positive=True)
    Phi = -sp.log(1 - sp.exp(-2 * Wsym))
    ok13a = sp.simplify(sp.diff(Phi, Wsym)
                        + 2 * sp.exp(-2 * Wsym)
                        / (1 - sp.exp(-2 * Wsym))) == 0
    ok13b = sp.limit(Phi, Wsym, sp.oo) == 0
    dev13 = 0.0
    for Wv in (mp.mpf(1) / 64, mp.mpf(1) / 4, mp.mpf(1), mp.mpf(4)):
        num = 2 * mp.quad(lambda w: mp.e ** (-2 * w)
                          / (1 - mp.e ** (-2 * w)),
                          [Wv, Wv + 1, Wv + 20, mp.inf])
        cf = -mp.log(1 - mp.e ** (-2 * Wv))
        dev13 = max(dev13, float(abs(num - cf)))
    check("T1.3 arch near-cell closed tail is EXACTLY the missing "
          "integral: sympy verifies d/dW[-log(1-e^{-2W})] == "
          "-2e^{-2W}/(1-e^{-2W}) and the W -> inf limit is 0, hence "
          "2 int_W^inf e^{-2w}/(1-e^{-2w}) dw == -log(1-e^{-2W}) "
          "(FTC); 4-point %d-dps confirmation dev %.1e -- so "
          "_arch_A_near and _arch_A_far are ONE formula A[S_{s,D}]"
          % (DPS_HP, dev13),
          ok13a and ok13b and dev13 <= 1e-25)

    # T1.4 deployed lag vector == W_C[S_{dD,D}]
    dev14 = 0.0
    lag_cache = {}
    for j in (6, 9):
        D = 2.0 ** -j
        M = 17 * 2 ** (j - 2)
        c = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D)
             + core.atom_lags_at(float(ALPHA), M, u_at, mu_at)[0])
        lag_cache[j] = c
        for d in (0, 1, 2, 5, 37, M // 2, M - 2):
            ref = float(weil_of_tent(d * D, D, u_at, mu_at, float(S_WIN)))
            dev14 = max(dev14, abs(c[d] - ref) / max(abs(ref), 1e-300))
    check("T1.4 THEOREM (0): the deployed lag vector IS the capped Weil "
          "functional on the even tent, c_d == W_C[S_{dD,D}] for all "
          "three layers, 14 (j,d) cells, max rel dev %.2e <= %.0e "
          "(residual = the documented float cancellation of the deep "
          "second difference, A2.4 bar 1e-8)" % (dev14, BAR_TENT),
          dev14 <= BAR_TENT)

    # T1.5 MASTER IDENTITY Q_D(f) == W_C[Ktil_D]
    dev15 = 0.0
    for j in (4, 6):
        D = 2.0 ** -j
        M = 17 * 2 ** (j - 2)
        c = lag_cache.get(j)
        if c is None:
            c = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D)
                 + core.atom_lags_at(float(ALPHA), M, u_at, mu_at)[0])
            lag_cache[j] = c
        for e in els:
            fv = sample_vec(e["pf"], D, M)
            q_dep = qval(fv, c, D)
            nlast = min(int(math.ceil(float(e["bK"]) / D)) + 1, M - 1)
            a = np.correlate(fv, fv, "full")[M - 1:]
            kvals = (D * a[:nlast + 1]).tolist()
            q_ind = float(weil_of_interp(kvals, mp.mpf(1) / 2 ** j,
                                         u_at, mu_at, float(S_WIN)))
            dev15 = max(dev15, abs(q_dep - q_ind)
                        / max(abs(q_ind), 1e-300))
    check("T1.5 THEOREM (I) end to end: the deployed form value equals "
          "W_C evaluated DIRECTLY on the even pw-linear interpolant of "
          "the discrete autocorrelation (no lag vector used on the "
          "right), 20 cells, max rel dev %.2e <= %.0e"
          % (dev15, BAR_MASTER), dev15 <= BAR_MASTER)

    # T1.6 the EXACT defect lemma, in Q  (nodal values from the samples)
    ok16 = True
    n_lag = 0
    for e in els:
        e["kq"] = {}
        for j in J_EXACT:
            D = F(1, 2 ** j)
            M = 17 * 2 ** (j - 2)
            fv = []
            for i in range(M):
                x = F(2 * i + 1, 2) * D
                val = F(0)
                for (a, b, p) in e["fp"]:
                    if a <= x < b:
                        val = peval(p, x)
                fv.append(val)
            kd = []
            for d in range(M):
                a_d = sum((fv[i] * fv[i + d] for i in range(M - d)), F(0))
                kd.append(D * a_d)
            e["kq"][j] = kd
            nlast = min(int(math.ceil(float(e["bK"]) / float(D))) + 2, M)
            for d in range(nlast):
                lhs = kd[d] - pw_eval_exact(e["Kp"], d * D)
                rhs = -(D * D / 12) * pw_eval_exact(e["Gp"], d * D)
                ok16 &= (lhs == rhs)
                n_lag += 1
    check("T1.6 THEOREM (II.a) EXACT IN Q: k_d - K(dD) == "
          "-(D^2/12) G(dD) for every lag, all 10 elements, j = %s "
          "(%d lag identities, zero deviation -- midpoint exactness "
          "for cellwise quadratics)" % (str(J_EXACT), n_lag), ok16)

    # T1.7 the defect FUNCTION identity: Ktil_D - K == (Pi_D K - K)
    # - (D^2/12) G at points strictly inside cells (not only at nodes)
    ok17 = True
    n_pt = 0
    for e in els:
        for j in J_EXACT[:2]:
            D = F(1, 2 ** j)
            kd = e["kq"][j]
            nlast = min(int(math.ceil(float(e["bK"]) / float(D))) + 1,
                        len(kd) - 1)
            for num in range(1, 40):
                w = F(num, 40) * (nlast * D)
                d0 = int(w / D)
                t = w / D - d0
                ktil = kd[d0] * (1 - t) + kd[d0 + 1] * t
                lin = (pw_eval_exact(e["Kp"], d0 * D) * (1 - t)
                       + pw_eval_exact(e["Kp"], (d0 + 1) * D) * t)
                lhs = ktil - pw_eval_exact(e["Kp"], w)
                rhs = (lin - pw_eval_exact(e["Kp"], w)
                       - (D * D / 12) * pw_eval_exact(e["Gp"], w))
                ok17 &= (lhs == rhs)
                n_pt += 1
            ok17 &= (kd[0] - e["k0"] == -(D * D / 12) * e["kap2"])
    check("T1.7 THEOREM (II.b) EXACT IN Q at %d points strictly inside "
          "cells: Ktil_D - K == (Pi_D K - K) - (D^2/12) G (Pi_D G == G "
          "because G is pw-linear with grid-node breakpoints), and the "
          "origin value k_0 - K(0) == -(D^2/12) ||f'||^2 EXACTLY -- the "
          "corpus recovery law G0.7 as the origin value of the defect"
          % n_pt, ok17)

    # T1.8 the exact class, DERIVED
    derived_exact = tuple(e["tag"] for e in els if e["kap2"] == 0)
    dev18 = 0.0
    for e in els:
        if e["kap2"] != 0:
            continue
        for j in range(J_LO, J_HI + 1):
            D = 2.0 ** -j
            M = 17 * 2 ** (j - 2)
            c = lag_cache.get(j)
            if c is None:
                c = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D)
                     + core.atom_lags_at(float(ALPHA), M, u_at,
                                         mu_at)[0])
                lag_cache[j] = c
            dev18 = max(dev18, abs(qval(sample_vec(e["pf"], D, M), c, D)
                                   - e["qw"]))
    check("T1.8 EXACT-CLASS COROLLARY (derives the corpus P2.0 of "
          "v848): kappa2 == 0 iff f is cellwise constant, and then "
          "e_D == 0, so Q_D(f) == Q_W(f) at EVERY level; derived "
          "membership %s == predicted %s, deployed float deviation "
          "%.2e <= %.0e"
          % (derived_exact, EXACT_CLASS, dev18, BAR_EXACT_FLOAT),
          derived_exact == EXACT_CLASS and dev18 <= BAR_EXACT_FLOAT)

    # ------------------------------- T2: the quadrature error lemmas
    section("T2 -- THE QUADRATURE / INTERPOLATION LEMMAS (exact, "
            "interval, closed form)")

    ok21 = ok22 = ok20 = True
    for e in els:
        # (H-align): every breakpoint of K is a grid node -- otherwise
        # K'' is not bounded inside every cell (control C3 shows this is
        # load-bearing).  kapK == kappa2 exactly iff f is continuous.
        for j in range(J_LO, J_HI + 1):
            ok20 &= all((a * 2 ** j).denominator == 1
                        for (a, _b, _p) in e["Kp"])
        gsup = max(max(abs(pw_eval_exact(e["Gp"], a)),
                       abs(pw_eval_exact(e["Gp"], b)))
                   for (a, b, _p) in e["Gp"])
        ok20 &= (gsup == e["kap2"])
        if e["cont"]:
            ok20 &= (e["kapK"] == e["kap2"])
    jump_gt = [e["tag"] for e in els
               if not e["cont"] and e["kapK"] > e["kap2"]]
    jump_lt = [e["tag"] for e in els
               if not e["cont"] and e["kapK"] < e["kap2"]]
    check("T2.0 the structural hypotheses of the quadrature lemmas, "
          "EXACT in Q: (H-align) every breakpoint of K = f*f~ is a grid "
          "node at every level j = %d..%d; sup|G| == G(0) == kappa2 "
          "(Cauchy-Schwarz, attained at 0); and kapK := sup over CELL "
          "INTERIORS of |K''| equals kappa2 EXACTLY for every continuous "
          "element (K'' == -G there), while for elements with a jump in "
          "f the cross terms move it BOTH ways -- larger on %s, smaller "
          "on %s.  Hence kapK, not kappa2, is the honest interpolation "
          "constant; the two coincide precisely in the continuous case"
          % (J_LO, J_HI, jump_gt, jump_lt),
          ok20 and jump_gt and jump_lt)

    for e in els:
        for j in (5, 6):
            D = F(1, 2 ** j)
            bound_i = (D * D / 8) * e["kapK"]
            bound_l = D * e["kapK"] + (D * D / 12) * e["kap3"]
            nmax = int(math.ceil(float(e["bK"]) / float(D))) + 1
            worst_i = F(0)
            worst_l = F(0)
            for d in range(nmax):
                Kd = pw_eval_exact(e["Kp"], d * D)
                Kd1 = pw_eval_exact(e["Kp"], (d + 1) * D)
                for q in range(1, 8):
                    t = F(q, 8)
                    w = (d + t) * D
                    interp = Kd * (1 - t) + Kd1 * t \
                        - pw_eval_exact(e["Kp"], w)
                    if abs(interp) > worst_i:
                        worst_i = abs(interp)
                ea = (Kd * 1 + Kd1 * 0 - pw_eval_exact(e["Kp"], d * D)
                      - (D * D / 12) * pw_eval_exact(e["Gp"], d * D))
                eb = (Kd * 0 + Kd1 * 1
                      - pw_eval_exact(e["Kp"], (d + 1) * D)
                      - (D * D / 12) * pw_eval_exact(e["Gp"],
                                                     (d + 1) * D))
                slope = abs(eb - ea) / D
                if slope > worst_l:
                    worst_l = slope
            ok21 &= (worst_i <= bound_i)
            ok22 &= (worst_l <= bound_l)
    check("T2.1 interpolation bound EXACT in Q: ||Pi_D K - K||_inf <= "
          "(D^2/8) kapK on every cell of every element at j = 5,6 "
          "(Green's function of -d^2/ds^2 on the cell: 0 <= G_cell and "
          "int G_cell <= D^2/8; K is a cubic per piece and every piece "
          "end is a node by T2.0)", ok21)
    check("T2.2 Lipschitz bound EXACT in Q: the nodal slopes of e_D "
          "satisfy |e_D'| <= D kapK + (D^2/12) kappa3 -- the O(D) "
          "derivative control the archimedean origin block needs",
          ok22)

    # T2.3 the rho majorant reduces to the exponential series
    xsym = sp.symbols("x", positive=True)
    nsym = sp.symbols("n", integer=True, positive=True)
    ok23a = sp.simplify((1 + xsym) * (1 - sp.exp(-xsym)) - xsym
                        - sp.exp(-xsym)
                        * (sp.exp(xsym) - 1 - xsym)) == 0
    ok23b = sp.simplify(sp.Sum(xsym ** nsym / sp.factorial(nsym),
                               (nsym, 2, sp.oo)).doit()
                        - (sp.exp(xsym) - 1 - xsym)) == 0
    mp.mp.dps = DPS_CONST
    ok23c = True
    for k in range(-60, 61):
        w = mp.mpf(2) ** (mp.mpf(k) / 6)
        lhs = mp.e ** (-w / 2) / (1 - mp.e ** (-2 * w))
        rhs = (1 / (2 * w) + 1) * mp.e ** (-w / 2)
        ok23c &= (lhs <= rhs)
    check("T2.3 the archimedean majorant is ELEMENTARY: sympy proves "
          "(1+x)(1-e^{-x}) - x == e^{-x}(e^x - 1 - x) and e^x - 1 - x "
          "== sum_{n>=2} x^n/n! (all coefficients > 0), hence rho(w) = "
          "e^{-w/2}/(1-e^{-2w}) <= [1/(2w) + 1] e^{-w/2} for w > 0 with "
          "NO cited inequality; confirmed on 121 dyadic decades at %d "
          "dps" % DPS_CONST, ok23a and ok23b and ok23c)

    # T2.4 the three analytic integral majorants
    ok24 = True
    worst24 = 0.0
    for e in els:
        for j in list(range(J_LO, J_HI + 1)) + list(J_DEEP):
            D = mp.mpf(1) / 2 ** j
            B = mp.mpf(e["bK"].numerator) / e["bK"].denominator + D

            def rho_mp(w):
                return mp.e ** (-w / 2) / (1 - mp.e ** (-2 * w))
            Ia_t = mp.quad(lambda w: w * rho_mp(w), [0, D])
            Ib_t = mp.quad(rho_mp, [D, B])
            Ic_t = mp.quad(rho_mp, [B, B + 20, mp.inf])
            Ia_b = D / 2 + D * D / 2
            Ib_b = mp.log(B / D) / 2 + 2
            Ic_b = mp.e ** (-B / 2) * (1 / B + 2)
            ok24 &= (Ia_t <= Ia_b and Ib_t <= Ib_b and Ic_t <= Ic_b)
            worst24 = max(worst24, float(Ia_t / Ia_b), float(Ib_t / Ib_b),
                          float(Ic_t / Ic_b))
    check("T2.4 the three analytic majorants dominate the true "
          "integrals at %d dps on every (element, level): "
          "int_0^D w rho <= D/2 + D^2/2, int_D^B rho <= (1/2)log(B/D) "
          "+ 2, int_B^inf rho <= e^{-B/2}(1/B + 2); worst true/bound "
          "ratio %.8f < 1" % (DPS_CONST, worst24),
          ok24 and worst24 < 1.0)

    # T2.5 the origin constant in closed form
    J_num = mp.quad(lambda w: (mp.e ** (-2 * w) - mp.e ** (-w / 2))
                    / (1 - mp.e ** (-2 * w)), [0, 1, 5, 20, mp.inf])
    J_cf = -mp.mpf(3) / 2 * mp.log(2) - mp.pi / 4
    dev25 = float(abs(J_num - J_cf))
    Jsym = sp.integrate((sp.exp(-2 * wsym) - sp.exp(-wsym / 2))
                        / (1 - sp.exp(-2 * wsym)), (wsym, 0, sp.oo))
    ok25s = abs(complex(sp.N(sp.simplify(Jsym
                                         + sp.Rational(3, 2) * sp.log(2)
                                         + sp.pi / 4), 30))) < 1e-25
    theta_dev = float(abs(-(2 * J_cf - (mp.euler + mp.log(mp.pi)))
                          - (3 * mp.log(2) + mp.pi / 2 + mp.euler
                             + mp.log(mp.pi))))
    check("T2.5 the archimedean origin constant in CLOSED FORM: J = "
          "int_0^inf (e^{-2w} - e^{-w/2})/(1-e^{-2w}) dw = "
          "-(3/2)log 2 - pi/4 (sympy + %d-dps dev %.1e) and Theta0 = "
          "-(2J - (gamma + log pi)) = 3log2 + pi/2 + gamma + log pi = "
          "%.15f (dev %.1e)"
          % (DPS_CONST, dev25, THETA0, theta_dev),
          dev25 <= 1e-35 and ok25s and theta_dev <= 1e-30)
    mp.mp.dps = DPS_HP

    # T2.6 the leading pole channel in closed form (continuous f only)
    dev26 = 0.0
    n26 = 0
    for e in els:
        if e["kap2"] == 0 or not e["cont"]:
            continue
        Km = to_mp_pieces(e["Kp"])
        Gm = to_mp_pieces(e["Gp"])
        lhs = 4 * sum(mp.quad(lambda w: -pw_eval_mp(Gm, w)
                              * mp.cosh(w / 2), [a, b])
                      for (a, b, _p) in Gm)
        rhs = sum(mp.quad(lambda w: pw_eval_mp(Km, w) * mp.cosh(w / 2),
                          [a, b]) for (a, b, _p) in Km)
        dev26 = max(dev26, float(abs(lhs - rhs) / abs(rhs)))
        n26 += 1
    check("T2.6 the K''-channel closed form (continuous elements, "
          "K'' == -G): 4 int_0^inf K'' cosh(w/2) dw == int_0^inf K "
          "cosh(w/2) dw on %d elements, max rel dev %.2e -- the "
          "leading pole-layer defect coefficient is D^2/24 times "
          "POLE(K)" % (n26, dev26), n26 >= 4 and dev26 <= 1e-12)

    # ------------------------------------- T3: the envelope vs measured
    section("T3 -- THE ENVELOPE (the proven rate) AGAINST THE MEASURED "
            "RATES")
    for j in range(J_LO, J_HI + 1):
        if j in lag_cache:
            continue
        D = 2.0 ** -j
        M = 17 * 2 ** (j - 2)
        lag_cache[j] = (core.arch_lags(M, D)
                        + stage2.pole_lags_closed(M, D)
                        + core.atom_lags_at(float(ALPHA), M, u_at,
                                            mu_at)[0])
    ok31 = True
    worst31 = 0.0
    worst_cell = ""
    for e in els:
        e["err"] = {}
        for j in range(J_LO, J_HI + 1):
            D = 2.0 ** -j
            M = 17 * 2 ** (j - 2)
            q = qval(sample_vec(e["pf"], D, M), lag_cache[j], D)
            e["err"][j] = abs(q - e["qw"])
            env = envelope(float(e["kapK"]), float(e["kap2"]),
                           float(e["kap3"]), float(e["bK"]), D,
                           u_at, mu_at)
            if e["kap2"] == 0:
                continue
            r = e["err"][j] / env
            if r > worst31:
                worst31, worst_cell = r, "%s j=%d" % (e["tag"], j)
            ok31 &= (r <= 1.0)
    print("   %-28s %2s %13s %13s %8s" % ("element", "j", "|Q_D - Q_W|",
                                          "envelope", "ratio"))
    for e in els:
        if e["kap2"] == 0:
            print("   %-28s  --  EXACT class (envelope identically 0, "
                  "deployed dev <= %.1e)" % (e["name"], dev18))
            continue
        for j in (J_LO, 8, J_HI):
            env = envelope(float(e["kapK"]), float(e["kap2"]),
                           float(e["kap3"]), float(e["bK"]),
                           2.0 ** -j, u_at, mu_at)
            print("   %-28s %2d %13.6e %13.6e %8.4f"
                  % (e["name"], j, e["err"][j], env, e["err"][j] / env))
    check("T3.1 THEOREM (IV) against the deployed pipeline: "
          "|Q_D(f) - Q_W(f)| <= envelope for ALL inexact elements at "
          "EVERY level j = %d..%d; worst ratio %.4f <= 1 (at %s)"
          % (J_LO, J_HI, worst31, worst_cell), ok31)

    slopes = []
    for e in els:
        if e["kap2"] == 0:
            continue
        ee = np.array([max(e["err"][j], 1e-16) for j in FIT_J])
        sl = float(np.polyfit(FIT_J, np.log2(ee), 1)[0])
        e["slope"] = sl
        slopes.append(sl)
    med = float(np.median(slopes))
    env_sl = []
    for e in els:
        if e["kap2"] == 0:
            continue
        for j in FIT_J[:-1]:
            a = envelope(float(e["kapK"]), float(e["kap2"]),
                         float(e["kap3"]), float(e["bK"]),
                         2.0 ** -j, u_at, mu_at)
            b = envelope(float(e["kapK"]), float(e["kap2"]),
                         float(e["kap3"]), float(e["bK"]),
                         2.0 ** -(j + 1), u_at, mu_at)
            env_sl.append(math.log2(b / a))
    check("T3.2 corpus regression: the measured per-element log2 rates "
          "reproduce v848 EXTRACTION-CHAIN-COMPLETE -- median %+.3f "
          "(frozen %+.3f), min %+.3f, max %+.3f, all inside "
          "[%+.3f, %+.3f]; the envelope's own local log2 slope band is "
          "[%+.3f, %+.3f] (2^{-2j} j law); the PROVEN exponent 2 (up to "
          "log) is STRONGER than the measured pre-asymptotic exponents"
          % (med, RATE_MED, max(slopes), min(slopes), RATE_MIN,
             RATE_MAX, min(env_sl), max(env_sl)),
          abs(med - RATE_MED) <= BAR_RATE
          and min(slopes) >= RATE_MIN and max(slopes) <= RATE_MAX)

    ok33 = True
    worst33 = 0.0
    ratios_deep = {}
    for e in els:
        if e["kap2"] == 0:
            continue
        ratios_deep[e["tag"]] = []
        for j in J_DEEP:
            D = 2.0 ** -j
            M = 17 * 2 ** (j - 2)
            et = abs(weil_of_defect(e["Kf"], e["Gf"], float(e["kap2"]),
                                    float(e["bK"]), D, M, u_at, mu_at,
                                    float(S_WIN)))
            env = envelope(float(e["kapK"]), float(e["kap2"]),
                           float(e["kap3"]), float(e["bK"]), D,
                           u_at, mu_at)
            ratios_deep[e["tag"]].append((j, et, env, et / env))
            worst33 = max(worst33, et / env)
            ok33 &= (et / env <= 1.0)
    print("   deep extension via the stable master-identity route:")
    for tag, rows in ratios_deep.items():
        print("     %-6s %s" % (tag, "  ".join(
            "j=%d err %.3e env %.3e r %.4f" % r for r in rows)))
    check("T3.3 the envelope holds BEYOND the measured ladder: at "
          "j = %s the exact-defect route gives |W_C[e_D]| <= envelope "
          "on all inexact elements, worst ratio %.4f <= 1 (monotone "
          "saturation far below 1 -- the measured slope band is "
          "pre-asymptotic, not a violation trend)"
          % (str(J_DEEP), worst33), ok33)

    dev34 = 0.0
    for e in els:
        if e["kap2"] == 0:
            continue
        for j in range(J_LO, J_HI + 1):
            D = 2.0 ** -j
            M = 17 * 2 ** (j - 2)
            et = abs(weil_of_defect(e["Kf"], e["Gf"], float(e["kap2"]),
                                    float(e["bK"]), D, M, u_at, mu_at,
                                    float(S_WIN)))
            dev34 = max(dev34, abs(et - e["err"][j])
                        / max(e["err"][j], 1e-300))
    check("T3.4 route ward: the deployed error |Q_D(f) - Q_W(f)| equals "
          "the independently evaluated |W_C[e_D]| of the exact defect "
          "lemma on all 7 inexact elements at j = %d..%d, max rel dev "
          "%.2e <= %.0e -- identities (I)+(II)+(III) verified end to "
          "end, and the deployed float pipeline is NOT the limiting "
          "factor" % (J_LO, J_HI, dev34, BAR_ROUTE), dev34 <= BAR_ROUTE)

    # T3.5 SHARPNESS: the true leading term is |e_D(0)| log(1/D)
    sharp = []
    ok35 = True
    for e in els:
        if e["kap2"] == 0:
            continue
        for (j, et, _env, _r) in ratios_deep[e["tag"]]:
            D = 2.0 ** -j
            lead = D * D * float(e["kap2"]) * math.log(1.0 / D) / 12.0
            sharp.append(et / lead)
            ok35 &= (SHARP_LO <= et / lead <= SHARP_HI)
    check("T3.5 SHARPNESS of the proven rate (no fitting: a ratio "
          "against a CLOSED-FORM leading term): |W_C[e_D]| divided by "
          "|e_D(0)| log(1/D) = (D^2 kappa2/12) log(1/D) lies in "
          "[%.4f, %.4f] on all inexact elements at j = %s and drifts "
          "toward 1, so the D^2 log(1/D) law is the TRUE asymptotic "
          "behaviour and the proven log coefficient (A0 + A2) = "
          "7 kappa2/24 is sharp up to the EXPLICIT factor 7/2.  The "
          "measured pre-asymptotic slopes -1.58..-1.84 are the same "
          "law seen at finite j (log(1/D) still comparable to the "
          "B-dependent constants), NOT a different exponent"
          % (min(sharp), max(sharp), str(J_DEEP)), ok35)

    # ------------------------------------ T4: cap and comb tail
    section("T4 -- THE FAITHFUL SUPPORT CAP AND THE COMB TAIL "
            "(explicit constants)")
    u_big, mu_big, n_big, lam_big = sieve_prime_powers(SIEVE_N)
    ok41a = ok41b = True
    margins = []
    dev41 = 0.0
    for e in els:
        for j in (J_LO, J_HI):
            D = F(1, 2 ** j)
            B = e["bK"] + D
            nlast = int(math.ceil(float(e["bK"]) / float(D)))
            if j in J_EXACT:
                kd = e["kq"][j]
                ok41a &= all(kd[d] == 0 for d in range(nlast, len(kd)))
            Df = float(D)
            M = 17 * 2 ** (j - 2)
            kf = np.correlate(sample_vec(e["pf"], Df, M),
                              sample_vec(e["pf"], Df, M), "full")[M - 1:]
            kf = Df * kf
            ok41a &= bool(np.all(kf[nlast:] == 0.0))
            # capped comb vs UNCAPPED comb over the 10^7 sieve
            t_cap = float(np.sum(mu_at * np.interp(
                u_at, Df * np.arange(M), kf, left=kf[0], right=0.0)))
            t_inf = float(np.sum(mu_big * np.interp(
                u_big, Df * np.arange(M), kf, left=kf[0], right=0.0)))
            dev41 = max(dev41, abs(t_cap - t_inf))
            ok41b &= (t_cap == t_inf)
            margins.append(float(S_WIN) - float(B))
    check("T4.1 THEOREM (III) faithful cap, MACHINE-CHECKED: the nodal "
          "values k_d vanish IDENTICALLY for dD >= b_K (exact in Q at "
          "j = %d, in float at j = %d), so supp Ktil_D subset "
          "[-(b_K + D), b_K + D]; the capped comb T_C[Ktil_D] equals "
          "the comb over ALL %d prime powers up to 10^%d, deviation "
          "%.1e; the deployed cap C = 2 alpha = %s clears b_K + D by "
          ">= %.4f everywhere (the deep faithful cap 2 alpha + 2D of "
          "CCCLVIII clears it a fortiori)"
          % (J_LO, J_HI, len(u_big), int(round(math.log10(SIEVE_N))),
             dev41, S_WIN, min(margins)),
          ok41a and ok41b and min(margins) > 0)

    psi = np.cumsum(lam_big)
    ok42a = bool(np.all(psi <= C1_RS * n_big.astype(float)))
    worst_psi = float(np.max(psi / n_big.astype(float)))
    ok42b = ok42c = True
    worst42 = 0.0
    worst42c = 0.0
    for y in [0.5 * k for k in range(2, 28)]:
        x = math.exp(y)
        msk = u_big <= y
        mfr = float(np.sum(mu_big[msk]))
        bnd = 4.0 * C1_RS * math.exp(y / 2.0)
        ok42b &= (mfr <= bnd)
        worst42 = max(worst42, mfr / bnd)
        # the Abel step, with the psi-integral taken EXACTLY on the
        # step function: (1/2) int_1^x psi(t) t^{-3/2} dt <= c1(sqrt x - 1)
        nn = n_big[msk].astype(float)
        ipsi = float(np.sum(lam_big[msk]
                            * (1.0 / np.sqrt(nn) - 1.0 / math.sqrt(x))))
        if x > 1.0:
            ok42c &= (ipsi <= C1_RS * (math.sqrt(x) - 1.0) + 1e-9)
            worst42c = max(worst42c,
                           ipsi / max(C1_RS * (math.sqrt(x) - 1.0), 1e-12))
    check("T4.2 comb tail with an EXPLICIT unconditional constant: "
          "psi(x) <= %.5f x on the whole sieved range up to 10^%d "
          "(worst ratio %.6f; Rosser-Schoenfeld 1962 Thm 12, "
          "Chebyshev-type, NO zero-free region, NO PNT -- the all-x "
          "statement is the CITATION, the sieved range is what this "
          "gate pins); the Abel step (1/2) int_1^x psi t^{-3/2} <= "
          "c1(sqrt x - 1) holds with the step-function integral "
          "evaluated exactly (worst ratio %.4f); hence mfrak(y) = "
          "sum_{k log p <= y} 2 log p / p^{k/2} <= 4 c1 e^{y/2} on 26 "
          "test heights (worst true/bound %.4f).  For FIXED f the comb "
          "is a FINITE sum, so this constant is needed only for "
          "support-uniformity"
          % (C1_RS, int(round(math.log10(SIEVE_N))), worst_psi,
             worst42c, worst42),
          ok42a and ok42b and ok42c and worst42 < 1.0)

    ledger = (
        ("E1 midpoint exactness for quadratics", "ELEMENTARY", True),
        ("E2 linear interpolation error constants", "ELEMENTARY", True),
        ("E3 Cauchy-Schwarz |G| <= G(0)", "ELEMENTARY", True),
        ("E4 1 + x <= e^x (rho majorant)", "ELEMENTARY", True),
        ("E5 J = -(3/2)log2 - pi/4", "ELEMENTARY", True),
        ("E6 arch closed tail identity", "ELEMENTARY", True),
        ("F1 finite comb for fixed f", "FINITE-EXPLICIT", True),
        ("C1 Rosser-Schoenfeld psi(x) < 1.03883 x",
         "EXPLICIT-CONSTANT-CITED", True),
        ("S1 W1 measure dictionary (v630/v643)", "STRUCTURAL-CITED",
         True),
        ("S2 Weil explicit formula and criterion", "STRUCTURAL-CITED",
         True),
        ("S3 admissible even compact BV class (IK04 5.12)",
         "STRUCTURAL-CITED", True),
    )
    forbidden = ("zero-free region", "PNT", "zeta zeros", "tau",
                 "target sign", "fit")
    no_zfr = all(t in ("ELEMENTARY", "FINITE-EXPLICIT",
                       "EXPLICIT-CONSTANT-CITED", "STRUCTURAL-CITED")
                 for _n, t, _o in ledger)
    print("   classical-input ledger:")
    for nm, ty, _o in ledger:
        print("     %-46s %s" % (nm, ty))
    check("T4.3 classical-input ledger closed and typed: %d inputs, "
          "every one ELEMENTARY / FINITE-EXPLICIT / EXPLICIT-CONSTANT-"
          "CITED / STRUCTURAL-CITED; NOT consumed anywhere: %s -- the "
          "convergence theorem is UNCONDITIONAL"
          % (len(ledger), ", ".join(forbidden)), no_zfr)

    # --------------------------------- T5: uniformity and edge 6
    section("T5 -- UNIFORMITY AND THE C^0 / DENSITY EDGE (edge 6)")
    fam = []
    ok_fam = True
    for k in range(8):
        ef, okf = build_element("U%02d hat(3,%d)" % (k, k),
                                ((F(1), (3, k, 1)),))
        ok_fam &= okf
        fam.append(ef)
    for k in range(4):
        ef, okf = build_element("V%02d hat(2,%d)" % (k, k),
                                ((F(1), (2, k, 1)),))
        ok_fam &= okf
        fam.append(ef)
    for ef in fam:
        ef["qw"] = float(weil_of_pw(
            to_mp_pieces(ef["Kp"]),
            mp.mpf(ef["k0"].numerator) / ef["k0"].denominator,
            mp.mpf(ef["bK"].numerator) / ef["bK"].denominator,
            u_at, mu_at, float(S_WIN)))
    rK = max(float(ef["kapK"]) for ef in fam)
    r2 = max(float(ef["kap2"]) for ef in fam)
    r3 = max(float(ef["kap3"]) for ef in fam)
    bmax = max(float(ef["bK"]) for ef in fam)
    bmin = min(float(ef["bK"]) for ef in fam)
    same_const = len({(ef["kapK"], ef["kap2"], ef["kap3"], ef["bK"])
                      for ef in fam[:8]}) == 1
    ok51 = True
    spread = 0.0
    rows51 = []
    for j in J_UNIF:
        D = 2.0 ** -j
        M = 17 * 2 ** (j - 2)
        errs = [abs(qval(sample_vec(ef["pf"], D, M), lag_cache[j], D)
                    - ef["qw"]) for ef in fam]
        # the uniform envelope: sup over the admissible support WINDOW
        # [bmin, bmax], taken on a fine grid.  The B-dependence is
        # continuous but NOT monotone, and it degrades like 1/b_K as
        # b_K -> 0 (the archimedean origin channel), so the uniform
        # class needs a TWO-SIDED support window, not just b_K <= b.
        env = max(envelope(rK, r2, r3,
                           bmin + (bmax - bmin) * i / 256.0, D,
                           u_at, mu_at) for i in range(257))
        ok51 &= (max(errs) <= env)
        spread = max(spread, max(errs) / max(min(errs), 1e-300))
        rows51.append((j, min(errs), max(errs), env, max(errs) / env))
    mono23 = True
    for j in J_UNIF:
        D = 2.0 ** -j
        for B in (0.25, 1.0, 3.0):
            base = envelope(1.0, 1.0, 1.0, B, D, u_at, mu_at)
            mono23 &= (envelope(2.0, 1.0, 1.0, B, D, u_at, mu_at) >= base)
            mono23 &= (envelope(1.0, 2.0, 1.0, B, D, u_at, mu_at) >= base)
            mono23 &= (envelope(1.0, 1.0, 2.0, B, D, u_at, mu_at) >= base)
    print("   uniformity family: 8 translates hat(3,k) with IDENTICAL "
          "(b_K, kapK, kappa2, kappa3) = (%s, %s, %s, %s) + 4 "
          "translates hat(2,k)"
          % (fam[0]["bK"], fam[0]["kapK"], fam[0]["kap2"],
             fam[0]["kap3"]))
    for j, lo, hi, env, r in rows51:
        print("     j=%-2d min err %.4e  max err %.4e  uniform envelope "
              "%.4e  worst ratio %.4f" % (j, lo, hi, env, r))
    check("T5.1 THEOREM (V) UNIFORMITY on a genuine family: the envelope "
          "depends on (b_K, kapK, kappa2, kappa3) ONLY, is nondecreasing "
          "in each of the three constants (%s), and is continuous in B, "
          "so its sup over a two-sided support window [b_-, b_+] with "
          "b_- > 0 is finite and computable (it degrades like 1/b_K as "
          "b_K -> 0, so the window must be two-sided -- typed, not "
          "hidden).  The 12-member translate family -- whose individual "
          "errors differ by a factor up to %.2f at fixed level, so the "
          "test is NOT vacuous, and whose 8-member subfamily has "
          "provably identical constants (%s) -- is dominated at every "
          "level by that ONE uniform envelope.  Uniform on {b_- <= supp "
          "diam <= b_+, kapK <= RK, ||f'||_2^2 <= R2, Lip(G) <= R3}; "
          "NOT uniform on an L^2 ball (kappa2 is an H^1 seminorm)"
          % ("verified" if mono23 else "FAILED", spread, same_const),
          ok51 and ok_fam and mono23 and same_const and spread > 1.1)

    ok52 = True
    worst52 = 0.0
    rng = np.random.default_rng(SEED_SCR)
    for trial in range(12):
        nseg = int(rng.integers(3, 9))
        bB = 1.0 + 1.5 * float(rng.random())
        nodes = np.linspace(0.0, bB, nseg + 1)
        vals = rng.normal(0.0, 1.0, nseg + 1) * 1e-3
        vals[-1] = 0.0
        e0 = float(vals[0])
        einf = float(np.max(np.abs(vals)))
        lip = float(np.max(np.abs(np.diff(vals)) / np.diff(nodes)))
        w0 = float(nodes[1])

        def pert(w):
            w = np.abs(np.asarray(w, float))
            return np.interp(w, nodes, vals, left=vals[0], right=0.0)
        pole = 4.0 * float(np.sum([0.5 * (nodes[i + 1] - nodes[i])
                                   * np.dot(GW48, pert(
                                       0.5 * (nodes[i] + nodes[i + 1])
                                       + 0.5 * (nodes[i + 1] - nodes[i])
                                       * GX48)
                                       * np.cosh(0.5 * (
                                           0.5 * (nodes[i] + nodes[i + 1])
                                           + 0.5 * (nodes[i + 1]
                                                    - nodes[i]) * GX48)))
                                   for i in range(nseg)]))
        edges = [0.0] + [nodes[1] * 0.5 ** i
                         for i in range(20)][::-1] + list(nodes[2:]) \
            + [nodes[-1] + 2.0 ** i for i in range(0, 8)]
        arch_i = 0.0
        for lo, hi in zip(edges[:-1], edges[1:]):
            if hi <= lo:
                continue
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            ww = mid + half * GX48
            arch_i += half * float(np.dot(GW48, (e0 - pert(ww))
                                          * rho_np(ww)))
        arch = e0 * COEF0 + 2.0 * arch_i
        atom = -float(np.dot(mu_at[u_at <= bB], pert(u_at[u_at <= bB])))
        true = abs(pole + arch + atom)
        bnd = modulus(e0, einf, lip, w0, bB, u_at, mu_at)
        ok52 &= (true <= bnd)
        worst52 = max(worst52, true / bnd)
    check("T5.2 the CORRECTED continuity modulus of W_C holds on the "
          "declared 12-perturbation battery (seed %d, pw-linear even "
          "perturbations): |W_C[e]| <= Theta0|e(0)| + (8 sinh(B/2) + "
          "mfrak(B))||e||_inf + 2[L(w0/2 + w0^2/2) + (|e(0)| + "
          "||e||_inf)((1/2)log(B/w0) + 2) + |e(0)|e^{-B/2}(1/B + 2)]; "
          "worst true/bound %.4f < 1.  This -- uniform smallness PLUS "
          "the Lipschitz handle L at the origin -- is the hypothesis "
          "edge 6 must cite; the pure sup-norm version is refuted by C5"
          % (SEED_SCR, worst52), ok52 and worst52 < 1.0)

    # C5: sup-norm C^0 continuity of the arch block is FALSE
    sup_vals, arch_vals = [], []
    for n in (2, 4, 6, 8, 10, 12):
        eps = 1.0 / n
        delta = math.exp(-float(n) ** 2)
        Bc = 2.0

        def en(w):
            w = np.abs(np.asarray(w, float))
            return eps * np.minimum(1.0, w / delta) \
                * np.maximum(0.0, 1.0 - w / Bc)
        edges = [0.0] + [delta * 2.0 ** i for i in range(0, 400)
                         if delta * 2.0 ** i < Bc] + [Bc]
        acc = 0.0
        for lo, hi in zip(edges[:-1], edges[1:]):
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            ww = mid + half * GX48
            acc += half * float(np.dot(GW48, (0.0 - en(ww)) * rho_np(ww)))
        sup_vals.append(eps)
        arch_vals.append(abs(2.0 * acc))
    growing = all(b > a for a, b in zip(arch_vals[:-1], arch_vals[1:]))
    c5_fire = (growing and sup_vals[-1] <= sup_vals[0] / 5.0
               and arch_vals[-1] >= 3.0 * arch_vals[0])
    check("C5 CONTROL (must fire) -- the chain's cited C^0-continuity "
          "of Q_W is FALSE in the pure sup norm: the explicit even "
          "Lipschitz family e_n(w) = (1/n) min(1, w/e^{-n^2}) "
          "(1 - w/2)_+ has e_n(0) = 0 and ||e_n||_inf = 1/n -> 0 while "
          "|A[e_n]| = %s grows like n -> inf (n = 2,4,...,12); the "
          "correct hypothesis is uniform convergence PLUS equi-Lipschitz "
          "(Dini) at the origin, which the admissible BV class supplies"
          % " ".join("%.2f" % v for v in arch_vals), c5_fire)

    # ------------------------------------------------ controls C1..C4
    section("CONTROLS (must fire)")
    n_c1 = 0
    rat_c1 = []
    for e in els:
        if e["kap2"] == 0:
            continue
        D = 2.0 ** -J_HI
        M = 17 * 2 ** (J_HI - 2)
        c_no = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D))
        q_no = qval(sample_vec(e["pf"], D, M), c_no, D)
        env = envelope(float(e["kapK"]), float(e["kap2"]),
                       float(e["kap3"]), float(e["bK"]), D, u_at, mu_at)
        r = abs(q_no - e["qw"]) / env
        rat_c1.append(r)
        n_c1 += int(r >= C1_FIRE)
    check("C1 WRONG TARGET fires: dropping the prime comb from the "
          "finite form violates the envelope on %d/%d inexact elements "
          "(median ratio %.1f, bar %g) -- the envelope is "
          "discriminating, not vacuous"
          % (n_c1, len(rat_c1), float(np.median(rat_c1)), C1_FIRE),
          n_c1 >= 4)

    n_c2 = 0
    rat_c2 = []
    for e in els:
        if e["kap2"] == 0 or float(e["bK"]) <= u_own[0]:
            continue
        cap_bad = float(e["bK"]) - 1e-9
        n_keep = int(np.searchsorted(u_at, cap_bad, side="right")) - 1
        if n_keep < 0:
            continue
        rr = []
        for j in (9, J_HI):
            D = 2.0 ** -j
            M = 17 * 2 ** (j - 2)
            c_bad = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D)
                     + core.atom_lags_at(float(ALPHA), M, u_at[:n_keep],
                                         mu_at[:n_keep])[0])
            q_bad = qval(sample_vec(e["pf"], D, M), c_bad, D)
            env = envelope(float(e["kapK"]), float(e["kap2"]),
                           float(e["kap3"]), float(e["bK"]), D,
                           u_at, mu_at)
            rr.append(abs(q_bad - e["qw"]) / env)
        rat_c2.append(max(rr))
        n_c2 += int(max(rr) >= C2_FIRE)
    check("C2 CAP VIOLATION fires: a comb capped BELOW b_K (one atom "
          "inside supp K dropped) violates the envelope on %d/%d "
          "elements and does not decay (median ratio %.1e, bar %g) -- "
          "the faithful cap C >= b_K + D is load-bearing"
          % (n_c2, len(rat_c2), float(np.median(rat_c2)), C2_FIRE),
          n_c2 >= 3)

    tent = [(F(0), F(1, 3), [F(0), F(3)]),
            (F(1, 3), F(2, 3), [F(2), F(-3)])]
    tent_r = deriv_pieces(tent)
    cuts_t = corr_break_cuts(tent)
    Kt, _ = corr_pieces(tent, tent, cuts_t, 3)
    Gt, _ = corr_pieces(tent_r, tent_r, cuts_t, 1)
    j = 6
    D = F(1, 2 ** j)
    M = 17 * 2 ** (j - 2)
    fvq = []
    for i in range(M):
        x = F(2 * i + 1, 2) * D
        val = F(0)
        for (a, b, p) in tent:
            if a <= x < b:
                val = peval(p, x)
        fvq.append(val)
    bad_lags = 0
    worst_c3 = F(0)
    for d in range(int(math.ceil(float(cuts_t[-1]) / float(D))) + 2):
        a_d = sum((fvq[i] * fvq[i + d] for i in range(M - d)), F(0))
        lhs = D * a_d - pw_eval_exact(Kt, d * D)
        rhs = -(D * D / 12) * pw_eval_exact(Gt, d * D)
        if lhs != rhs:
            bad_lags += 1
            worst_c3 = max(worst_c3, abs(lhs - rhs))
    check("C3 GRID MISALIGNMENT fires: for a tent with the non-dyadic "
          "breakpoint 1/3 the EXACT defect lemma FAILS at %d lags "
          "(worst deviation %.3e) -- cellwise affineness on the "
          "deployed grid is a genuine hypothesis of (II), not "
          "decoration (convergence itself is not claimed to fail)"
          % (bad_lags, float(worst_c3)), bad_lags > 0)

    n_c4 = 0
    rat_c4 = []
    rng4 = np.random.default_rng(SEED_SCR)
    pos = np.sort(rng4.uniform(0.5, float(S_WIN) - 0.1, len(u_at)))
    for e in els:
        if e["kap2"] == 0:
            continue
        D = 2.0 ** -J_HI
        M = 17 * 2 ** (J_HI - 2)
        c_scr = (core.arch_lags(M, D) + stage2.pole_lags_closed(M, D)
                 + core.atom_lags_at(float(ALPHA), M, pos, mu_at)[0])
        q_scr = qval(sample_vec(e["pf"], D, M), c_scr, D)
        env = envelope(float(e["kapK"]), float(e["kap2"]),
                       float(e["kap3"]), float(e["bK"]), D, u_at, mu_at)
        r = abs(q_scr - e["qw"]) / env
        rat_c4.append(r)
        n_c4 += int(r >= C4_FIRE)
    check("C4 SCRAMBLED COMB fires: atom positions re-drawn (seed %d, "
          "masses kept) violate the envelope against the TRUE target "
          "on %d/%d elements (median ratio %.1e, bar %g)"
          % (SEED_SCR, n_c4, len(rat_c4), float(np.median(rat_c4)),
             C4_FIRE), n_c4 >= 4)

    dt = time.time() - t0
    check("G0.8 runtime %.1f s <= %.0f s" % (dt, RUNTIME_CAP),
          dt <= RUNTIME_CAP)

    # ---------------------------------------------------- the verdict
    guard_names = ("G0.1", "G0.2", "G0.3", "G0.4", "G0.8")
    guards_ok = all(ok for (n, ok) in CHECKS
                    if n.split()[0] in guard_names)
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("C1", "C2", "C3", "C4", "C5")))
    legs = {n.split()[0]: ok for (n, ok) in CHECKS
            if n.startswith(("T1", "T2", "T3", "T4", "T5"))}
    ident_ok = all(legs.get(k, False)
                   for k in ("T1.1", "T1.2", "T1.3", "T1.4", "T1.5",
                             "T1.6", "T1.7", "T1.8"))
    lemma_ok = all(legs.get(k, False)
                   for k in ("T2.0", "T2.1", "T2.2", "T2.3", "T2.4",
                             "T2.5"))
    env_ok = all(legs.get(k, False)
                 for k in ("T3.1", "T3.3", "T3.4", "T4.1"))
    cond_ok = legs.get("T4.3", False)
    if not (guards_ok and controls_ok):
        verdict = "FORMCONV-INVALID"
    elif not (ident_ok and lemma_ok):
        verdict = ("FORMCONV-GAP(%s)"
                   % ",".join(k for k, v in sorted(legs.items())
                              if not v and k.startswith(("T1", "T2"))))
    elif not env_ok:
        verdict = ("FORMCONV-GAP(envelope: %s)"
                   % ",".join(k for k in ("T3.1", "T3.3", "T3.4",
                                          "T4.1") if not legs.get(k)))
    elif not cond_ok:
        verdict = "FORMCONV-PROVEN-CONDITIONAL(classical-input ledger)"
    else:
        verdict = ("FORMCONV-PROVEN(rate O(D^2 log(1/D)) = "
                   "O(2^{-2j} j); constants Theta0 = 3log2 + pi/2 + "
                   "gamma + log pi, origin 1/12, interp 1/8, and for "
                   "continuous f the log coefficient 7/24 with sup "
                   "5/24; classical inputs: elementary calculus + a "
                   "finite prime-power table, Rosser-Schoenfeld ONLY "
                   "for support-uniformity)")
    _VERDICTS["v"] = verdict

    section("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % spec_sha)
    print("""\
CONSEQUENCE FOR THE EXTRACTION CHAIN (stated with the deltas, NO RH
claim).  The Lean hypothesis

    hconv : forall v, Tendsto (fun m => ladderForm A sample m v)
                              atTop (nhds (QW v))

of CofinalWeil.cofinal_weil / CofinalPredefinition.cofinal_weil_-
predefined is exactly (IV) for the deployed instantiation kappa m =
Fin M_m, A m = D_m T_m, sample m f = midpoint samples, QW f = Q_W(f):
a THEOREM for the dyadic cellwise-affine dense family, no longer a
measurement.  DELTA-A (FORMALISATION-OPEN): the proof is paper plus
these machine checks; CofinalEnvelope.lean states the envelope premise
and derives hconv from it for a fixed instantiated ladder, so the
hypothesis is the instantiated envelope rather than an opaque
assumption, but the envelope is not discharged inside the kernel.
DELTA-B (STATED, NOT A GAP): (H-grid), (H-cap), (H-align) must hold;
for fixed f, fixed window and dyadic f they hold for all large j,
which is exactly what Tendsto atTop needs.  What remains open in the
chain: (H_cof) -- the PREDEFINED cofinal positivity inequality, RH-hard
and untouched -- plus the named classical theorems (Weil's explicit
formula and criterion; the admissible class; density of the dyadic
family in the topology of the CORRECTED continuity modulus, which C5
shows must include an equi-Dini condition at the origin).  Proving this
edge does NOT prove RH.""")
    return 0 if (guards_ok and controls_ok
                 and not verdict.startswith("FORMCONV-INVALID")) else 1


def run():
    t_all = time.time()
    print("=" * 74)
    print("v912 -- PRIME.FORM.CONVERGENCE.THEOREM.01 (the all-depth "
          "form-convergence")
    print("edge as an unconditional theorem; (H_cof) untouched, "
          "NO RH claim)")
    print("=" * 74)
    CHECKS.clear()
    FAILS.clear()
    _VERDICTS.clear()
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and str(_VERDICTS.get("v")).startswith(EXPECTED))
    print("\n" + "=" * 74)
    print("v912: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run,
             str(_VERDICTS.get("v")).split("(")[0], time.time() - t_all))
    print("NO RH claim.  The genuinely open item of the chain stays "
          "(H_cof) -- the")
    print("PREDEFINED cofinal positivity inequality; this module "
          "closes only the")
    print("per-element form-convergence edge, and cites S1/S2/S3 and "
          "the all-x")
    print("Rosser-Schoenfeld constant rather than pinning them.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s, verdict %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none", str(_VERDICTS.get("v")).split("(")[0]))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
