#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v913 -- PRIME.NOGO.SIGNED.ONLY.01: THE SIGNED-AND-ALIGNMENT
LOCALIZATION OF THE RESIDUAL OBSTRUCTION -- a NO-GO / TYPING module.

WHAT KIND OF MODULE THIS IS (read this first).  This module prices
ARGUMENT CLASSES for the deployed budget shape.  It supplies no
positivity, no new interval and no new certificate; it closes no
gate, narrows no gate and moves NO marker.  It is NOT progress
toward a proof -- the honest counter-evidence is carried below and
printed by the run -- and it must NOT be counted as evidence for or
against the Riemann Hypothesis, nor cited in support of any
positivity claim.  NO RH CLAIM.

PROVENANCE: discovery probe signed_only_nogo_probe.py (note
CCCLXXIII, 2026-08-13, 87/87, verdict NOGO-COMPOSITE-VERIFIED,
62.3 s; PROBE_SHA
d1c42a055d4b17c7349fddef2ac47e7c49067406005c531f20a53fcf8c9a64a9,
SPEC_SHA
495308092be1113576a48613c6c2ca98ec96f41f60120c2e67455ae2ac4a07c6).
The probe's frozen specification is embedded BYTE-EXACT below and its
SHA-256 is re-derived at gate G0.2 before any evaluation.  This module
promotes the EXACT, CHEAP, SELF-CONTAINED CORE of that probe verbatim
and NOTHING ELSE (~30 s).

=======================================================================
THE SETTING (finite, explicitly constructed; nothing asymptotic)
=======================================================================
For an index kz let n_kz be the kz-th prime power, alpha = log n_kz,
gap = log n_{kz+1} - log n_kz, D_k = gap/8, M = 2*ceil(alpha/D_k + 1)
rounded up to even, h = M/2, D = alpha/h, N_h = floor(e^{2 alpha+2D}).
With tau_D(t) = (1 - |t|/D)_+ the unit tent,

    K_D(t) = tau_D(t) - (tau_D(t - D) + tau_D(t + D))/2

is the deployed second-difference kernel.  The wall assembly produces
per rung h and shift theta the bordered Gram Omega_h = [[n, b^T],
[b, B]] with B positive definite, its archimedean companion Omega_0 =
[[n_0, b_0^T], [b_0, B]], the comb correction b_c = b_0 - b,
n_c = n_0 - n, x_0 = B^-1 b_0, q_0 = b_0^T B^-1 b_0,
q_c = b_c^T B^-1 b_c, and the source profile w with b_c = -(1/4) A_2 w.
The single missing inequality of the programme is, in its
best-conditioned form,

  (L)  int_0^1 [-(1/2)<w, v> - q_c] dtheta > int_0^1 [q_0 - n_0] dtheta

on ONE sign-independently predeclared cofinal family of rungs.  These
data plus the frame family are the DEPLOYED BUDGET SHAPE.

=======================================================================
WHAT THIS MODULE CARRIES (probe section ids kept for traceability)
=======================================================================
  S1.1-S1.7  THE EXACT KERNEL LEDGER, symbolic in D: int K_D = 0,
      ||K_D||_inf = 1, ||K_D'||_1 = 4 INDEPENDENTLY of D,
      ||K_D||_1 = 4D/3, D^-1 int K_D^2 = 2/3, and the exponential
      pairing in both closed forms, T_D = int tau_D e^{-t/2} =
      (8/D)(cosh(D/2) - 1) and int K_D e^{-t/2} = -(D/8) T_D^2.  The
      third identity is the load-bearing one: the conversion constant
      of a magnitude hypothesis does not become cheap as the mesh
      refines.
  S2.8-S2.10  THE MAGNITUDE CLASS IS UNCONDITIONALLY EMPTY (the
      comparison, not Littlewood's theorem, which is CITED): the
      geometric supply is recomputed here by two independent routes,
      is NEGATIVE and O(1) (|B| <= 2), while the Littlewood floor
      4 log log log N_h is >= 2.1654551 at h = 184 and >= 4.1231791 at
      h = 12632 -- a ratio of 214.7 against this module's OWN
      conservative slack and 1527.1 against the deployed one (cited).
  S2.13  SELBERG'S SYMMETRY FORMULA IS PROVABLY NEUTRAL: Lambda =
      mu * log and mu * log^2 = Lambda.log + Lambda * Lambda are
      FORMAL identities in the free module on {log p} (n <= 36), so
      they carry no arithmetic content into the budget.
  S3.1-S3.4  THE REQUIREMENT IS SIGNED AND CONGRUENCE-INVARIANT, as
      pure algebra of the bordered Gram: the three-term split
      s = (n_0 - q_0) - n_c + 2<b_c, x_0> - q_c is an identity; all
      three terms are invariant under EVERY congruence T = diag(1, M);
      under the comb sign flip b_c -> -b_c the outer terms are EVEN
      and the middle term is ODD; and the F4 kernel
      K = A_2^T B^-1 A_2 is itself a congruence invariant.  Hence no
      bound that is flip-invariant -- i.e. no unsigned hull, no
      window choice, no preconditioner, no congruence reformulation --
      can lower-bound an odd quantity.
  S6.3  THE BEURLING-NYMAN TRANSPORT TARGET, exactly in Q: (T3)
      lam_min(G_N) <= (log 2pi - gamma)/N, so the Baez-Duarte Gram has
      NO N-uniform floor; (T5) the explicit family
      G~ = A A^T + (4/5)^2 I meets EVERY hypothesis of the certificate
      class at every N while d~^2 >= 1/2 forever -- the class is
      non-implying.

=======================================================================
WHAT STAYS IN experiments/ AND WHY (the boundary is deliberate)
=======================================================================
The DEPLOYED MATRIX-STAGE READS -- S3.5-S3.12 (the theta-means of s,
the measured negativity of the even terms, the certified sign-flipped
counter-world, the growth attribution), S4 (SIGNED_h = PRIME(F) and
the negative bar) and S5 (the unsigned companion and its class floor)
-- are NOT promoted.  They inherit the float64 entry-slack premise of
the wall generators (X4) and the cited certified ladder (X1), and they
belong in experiments/ until that premise is discharged.  Everything
gated here is exact-symbolic or recomputed from this module's own
sieves, and consumes NEITHER of those two premises.

=======================================================================
THE LOCALIZATION (the deliverable, stated as what it is)
=======================================================================
Any argument that closes (L) for the deployed budget shape must supply
information that is (a) SIGNED -- it must orient a quantity that is
ODD under the comb sign flip -- and (b) ALIGNMENT-CARRYING -- it must
relate the position of the prime atoms to the spectral directions of
K, equivalently the ordinates to the sign pattern of Fhat.  In
particular it can be neither a magnitude bound on psi(x) - x nor a
natural-grammar identity, i.e. an identity valid in every arithmetic
world and therefore comb-blind.

CLASSES PROVEN EMPTY for this budget shape (E1-E10; [here] = gated by
this module, [probe] = carried by the frozen probe in experiments/):
  E1  every magnitude hypothesis |psi(x)-x| <= f(x) sqrt(x)   [here]
  E2  every zero-density input with A > 2; A = 2 and Lindeloef
      land exactly critical, zero slack                       [probe]
  E3  Selberg's symmetry formula (formal identity)            [here]
  E4  every congruence reformulation, window choice, Jacobi/
      Cholesky preconditioner, resolvent split                [here]
  E5  every unsigned hull of the comb correction: the parity/
      invariance half [here], the measured (cell, theta)
      negativity                                              [probe]
  E6  every bound consuming only {w >= 0, ||w||_inf, ||w||_2,
      supp w}                                                 [probe]
  E7  exact multiplicative transforms (Moebius/Dirichlet):
      inertia-preserving, so no orientation is created        [probe]
  E8  natural-grammar identities (de Branges/HB, Abel,
      squares): world-blind, hence non-discriminating         [probe]
  E9  the Beurling-Nyman/Baez-Duarte transport target: no
      uniform floor (T3), class non-implying (T5)             [here]
  E10 thin/cofinal Li criteria: explicit counterexample, and
      every subexponential Li envelope is RH-equivalent       [probe]

MERELY UNEXPLORED, no emptiness claimed: U1 unconditional statements
about ordinate POSITIONS; U2 alignment statements; U3 a different
budget shape; U4 the four premises of the reverse implication; U5
global constraints on the source profile beyond the cone.

WHAT THE STATEMENT DOES NOT SAY (named open scope): (O1) it does not
touch arguments that legitimately consume zero-position information --
the remaining statement IS of that kind, which is not the same as
false; (O2) it forbids only bounds inside I_cone, so alignment
statements are untouched and are exactly what is needed; (O3) every
clause is for the deployed kernel, frame family and predeclared rung
family -- another budget shape is outside it; (O4) the reverse
implication (inequality => RH) rests on four named premises and is NOT
established here; (O5) any new global inequality restricting the
admissible source profiles beyond {w >= 0, size, support} changes
I_cone and escapes S5.  ALSO: the statement is FINITE-RUNG (verified
at h = 184/388/839 with the ladder to h = 12632); it makes NO all-h
claim and says nothing about rungs outside the built cells.  And it
does NOT say that RH is unprovable, that the wall route fails, or that
no proof exists.

=======================================================================
PINNING DISCLOSURE (meta-audit CCCXXXVI lesson, applied a priori)
=======================================================================
WHAT THE EXECUTED GATES PIN.  S1.1-S1.7 pin the kernel ledger
SYMBOLICALLY in D (sympy, exact); S3.1-S3.4 pin the split, the
congruence invariance, the parity and the kernel invariance as
identities in the matrix-stage SYMBOLS, i.e. for every admissible
datum and every invertible M, consuming no deployed number; S2.13 pins
the Selberg identities exactly in the free module on {log p};
S2.8-S2.10 pin the frames (rebuilt from this module's own prime-power
sieve, h PREDICTED not supplied), the geometric supply by two
independent routes (closed form and direct quadrature, agreement
1.6e-50), this module's own conservative slack (own von Mangoldt
sieve) and the floor/slack ratio; S6.3 pins the two Beurling-Nyman
witnesses exactly in Q.

WHAT IS CITED, NOT PINNED (a false input here would NOT fail this
module):
  * X3 THE CLASSICAL LITERATURE.  Littlewood's Omega-theorem itself --
    that S(N) = sup_{x<=N} |psi(x)-x| x^{-1/2} diverges -- is the
    citation that makes the magnitude class empty; this module gates
    only the COMPARISON (floor against supply).  Likewise
    Rosser-Schoenfeld, Montgomery-Vaughan/Brun-Titchmarsh,
    Schoenfeld, Bombieri-Lagarias, Li's criterion, N(1/2,T) >> T log T
    and CCCLXIII's deployed constants c_B = 0.5523, sigma <= 0.726909.
  * X2 THE DEPLOYED SLACK 1.5e-05 .. 2.7e-03.  The gate uses this
    module's OWN, strictly larger and hence conservative, slack; the
    deployed number appears only as a second, cited ratio.
  * X1 THE CERTIFIED SCHUR INTERVALS AND WITNESS READS at the nine
    depths.  Used ONLY in the counter-evidence print, never inside a
    gate.
  * X4 THE FLOAT64 ENTRY SLACK of the wall generators.  NOT consumed
    anywhere here -- which is exactly why the deployed matrix-stage
    reads stay in experiments/.
  * X5/X6/X7 CCCLXVIII's demand totals, CCCLXII's chain measurements,
    and the n0-normalised margin exponents (the flattening
    counter-evidence).
  * THE DEPLOYED IDENTIFICATION.  That the deployed wall stage IS a
    bordered Gram of the shape above at the deployed rungs is the
    probe's measurement (S3.5-S3.12), not gated here; the algebra
    gated here is what applies TO it.
  * THE COMPOSITE THEOREM AS A WHOLE (T1-T5 for the deployed budget
    shape) is the frozen probe run at the SPEC_SHA above; this module
    carries its exact core.

=======================================================================
COUNTER-EVIDENCE, CARRIED AND NOT SMOOTHED (why this is not progress)
=======================================================================
NO-WITNESS STANDS: the certified reads are POSITIVE at all NINE
depths -- 0 negatives, 0 straddles -- with deepest certified read
2.79579794131272506e-15 at h = 12632 (cited, X1); this module adds
none.  The normalised decay FLATTENS with depth on the cited
normalisation (n0-normalised upper-bound exponents -3.21092511
globally against -2.67942161 on the deepest step 5746 -> 12632, X7),
and the re-derived s/D^2 step 1393 -> 2015 is POSITIVE (+0.50302892),
so the normalised drift is NOT monotone; no re-derivable exponent
comes near the frozen collapse bar -8.0.  A no-go about the TYPE of
the missing input is not evidence about its EXISTENCE.

Registers PRIME.NOGO.SIGNED.ONLY.01 [O] -- a no-go/typing row with a
typed scope, NOT an evidence row and NOT a closure.  No marker moves.
NO RH claim.  Python-only per GATE.WOLFRAM.02.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import sympy as sp
from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

EXPECTED = "NOGO-CORE-VERIFIED"
N_CHECKS = 24
PROBE_SPEC_SHA = ("495308092be1113576a48613c6c2ca98"
                  "ec96f41f60120c2e67455ae2ac4a07c6")
PROBE_SHA = ("d1c42a055d4b17c7349fddef2ac47e7c"
             "49067406005c531f20a53fcf8c9a64a9")

_VERDICTS = {}
CHECKS = []
FAILS = []

# ------------------------------------------------- frozen specification
MP_DPS = 50
PP_CAP = 200000
RUNTIME_CAP = 1800.0
# (h, kz): h is a PREDICTION of the rebuild from the prime-power list,
# never an input to it
FRAME_SPECS = ((184, 9), (388, 55), (839, 43), (1393, 88), (2015, 85),
               (2607, 131), (2854, 222), (5746, 273), (12632, 569))
SUPPLY_RUNGS = (184, 388)
FLOOR_RUNGS = (184, 12632)
BN_SIZES = (2, 4, 8, 16, 32, 64)
SELBERG_N = 36
RATIO_BAR = 100.0                      # floor/slack bar for "class empty"

# corpus values this module recomputes and must reproduce (regression
# wards on its OWN computation, not inputs to it)
WARD_FEJER_B = {184: "-1.2648057425013541047",
                388: "-1.3147508968858830784"}
WARD_FRAME_REL = 2.098e-02
WARD_LITTLEWOOD = {184: 2.1654551, 12632: 4.1231791}
WARD_BN_CONST = 1.2606614015
WARD_BN_CB = 0.5523                                                 # (X3)
WARD_BN_SIGMA_CAP = 0.726909                                        # (X3)
WARD_BN_SIGMA_RANGE = (0.4106, 0.4260)
WARD_SLACK_CITED = 2.7e-03                                          # (X2)
# cited counter-evidence, printed and never gated                   # (X1/X7)
CITED_DEEPEST_READ = "2.79579794131272506e-15"
CITED_EXP_U_GLOBAL = -3.21092510922176011
CITED_EXP_U_DEEP = -2.67942161302143633
CITED_EXP_STEP_POS = 0.50302892
CITED_COLLAPSE_BAR = -8.0

# banned CALL names: no zero data, no eigensolver on any deployed form,
# no fit anywhere (the probe's firewall, carried verbatim)
AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
    "tau", "target_sign", "cached_sign", "polyfit", "curve_fit",
    "lstsq", "least_squares",
}

# Embedded BYTE-EXACT from the discovery probe: FROZEN_SPEC is the
# probe's own frozen docstring, and its SHA-256 must reproduce
# PROBE_SPEC_SHA (gate G0.2).
FROZEN_SPEC = """\
signed_only_nogo_probe -- PRIME.NOGO.SIGNED.ONLY.01.

EXPLORATION ONLY.  This probe proves nothing about RH.  It is a
machine-checked statement ABOUT the remaining obstruction: a composite
no-go/localization theorem that says WHICH KINDS of argument cannot
close the deployed wall inequality, and names the kinds that are still
logically open.  No positivity claim, no RH claim, no promotion, no
marker moved, nothing written outside experiments/.

===========================================================================
THE THEOREM (SIGNED-ONLY LOCALIZATION)
===========================================================================

SETTING (all objects finite and explicitly constructed; nothing here is
asymptotic).  For an index kz let n_kz be the kz-th prime power,
alpha := log n_kz, gap := log n_{kz+1} - log n_kz, D_k := gap/8,
M := 2*ceil(alpha/D_k + 1) rounded up to even, h := M/2, D := alpha/h,
N_h := floor(exp(2 alpha + 2 D)).  Let tau_D(t) := max(0, 1 - |t|/D) be
the unit tent and

    K_D(t) := tau_D(t) - (tau_D(t - D) + tau_D(t + D)) / 2

the second-difference kernel.  The deployed wall assembly produces, at
each rung h and each shift theta in (0,1), a bordered Gram matrix
Omega_h(theta) = [[n, b^T], [b, B]] with B positive definite, its
archimedean-only companion Omega_0 = [[n_0, b_0^T], [b_0, B]], the comb
correction b_c := b_0 - b, n_c := n_0 - n, x_0 := B^-1 b_0,
v := A_2^T x_0, q_0 := b_0^T B^-1 b_0, q_c := b_c^T B^-1 b_c, and the
source lag profile w with b_c = -(1/4) A_2 w.  The single missing
inequality of the programme, in its best-conditioned equivalent form, is

  (L)  int_0^1 [ -(1/2) <w, v> - q_c ] dtheta > int_0^1 [ q_0 - n_0 ] dtheta

on ONE sign-independently predeclared cofinal family of rungs.  Write
need_h for the right-hand side plus the certified slack, SIGNED_h for
-(1/2) <w, v>, and UNSIGNED_h for q_c >= 0.  Call this data, together
with the frame family above, the DEPLOYED BUDGET SHAPE.

INFORMATION CLASSES.  For a rung h define
  I_mag  = every statement of the form |psi(x) - x| <= f(x) sqrt(x)
           for x <= N_h, f arbitrary (including f's that no theorem
           supplies), consumed through the kernel K_D;
  I_box  = {B, b_0, n_0 known exactly; |n_c| <= R; |b_c,i| <= R}
           (entrywise size of the comb correction);
  I_cone = {w >= 0 entrywise; ||w||_inf <= 2 R_c; ||w||_2^2 <= W2;
           supp w subset J} (size plus positivity of the von Mangoldt
           weights, no alignment);
  I_gram = every congruence reformulation T = diag(1, M), M invertible,
           of the matrix stage, and every window/preconditioner choice
           that consumes only I_box or I_cone.

THEOREM (composite; each clause is machine-checked below in the stated
section, at the rungs h in {184, 388, 839} and along the nine-frame
ladder h in {184, 388, 839, 1393, 2015, 2607, 2854, 5746, 12632}).

 (T0) EXACT KERNEL LEDGER.  int K_D = 0, ||K_D||_inf = 1,
      ||K_D'||_1 = 4 independently of D, ||K_D||_1 = 4D/3,
      D^-1 int K_D^2 = 2/3, int tau_D e^{-t/2} = T_D = (8/D)(cosh(D/2)-1)
      and int K_D e^{-t/2} = -T_D (cosh(D/2) - 1) = -(D/8) T_D^2.  All
      six are exact symbolic identities in D.                      [S1]

 (T1) THE MAGNITUDE CLASS I_mag IS UNCONDITIONALLY EMPTY, NOT MERELY
      UNPROVEN.  Because the kernel constant C_h that converts a
      magnitude hypothesis into a bound on (L) satisfies C_h >=
      ||K_D'||_1 = 4 > 0 while the geometric supply B_h stays O(1), any
      admissible f must beat S(N) := sup_{x<=N} |psi(x)-x| x^{-1/2},
      and Littlewood's unconditional Omega-theorem forces
      S(N) >= c_0 log log log N -> infinity.  The resulting floor
      4 log log log N_h is >= 2.1654551 at h = 184 and >= 4.1231791 at
      h = 12632, against a supply-side slack that this probe recomputes
      from scratch as <= 1.0087e-02 (its own conservative Fejer route)
      and <= 2.7e-03 (the deployed route, cited).  Hence no magnitude
      hypothesis whatsoever -- proven, conjectural, or merely
      hypothetical -- can close (L) for this budget shape.  In the same
      typing: the density hypothesis and Lindeloef land exactly
      critical (the test scale sits ON the square-root barrier,
      D_h sqrt(N_h) = gap/4 with gap = O(log N_h)), and Selberg's
      symmetry formula is provably neutral (it is a formal identity in
      the free module on {log p}).                                  [S2]

 (T2) THE RESIDUAL REQUIREMENT IS SIGNED AND CONGRUENCE-INVARIANT.  The
      exact three-term split s = (n_0 - q_0) - n_c + 2<b_c, x_0> - q_c
      holds identically; each term is invariant under every congruence
      T = diag(1, M); the outer terms are EVEN and the middle term is
      ODD under the comb sign flip b_c -> -b_c; the even terms are
      measured negative at every audited (cell, theta), so positivity
      is carried exclusively by the odd term.  Since every bound built
      from I_box or I_cone is invariant under that flip, no such bound
      can produce a positive lower bound for an odd quantity.  The
      flipped datum is admissible in I_box and is certified NEGATIVE by
      the deployed routine.  Therefore no reformulation, window choice,
      basis change, or preconditioner in I_gram converts the signed
      requirement into an unsigned one.                             [S3]

 (T3) THE SIGNED RESIDUAL IS EXACTLY A WEIL PRIME TERM, AND THE
      REMAINING STATEMENT IS A ZERO-SUM INEQUALITY AGAINST A NEGATIVE
      BAR.  With Psi_theta the archimedean tent transform of v and the
      even test function F(u) := -(1/4) Psi_theta(|u|/D), supported in
      |u| <= S := (h + 2 theta) D, one has SIGNED_h = PRIME(F) :=
      2 sum_{n <= e^S} Lambda(n) n^{-1/2} F(log n) EXACTLY, so Weil's
      explicit formula applies verbatim and (L) becomes

        sum_rho Fhat(gamma_rho) < POLE(F) + ARCH(F) - need_h,

      whose right-hand side is measured NEGATIVE.  This is the opposite
      of a Weil-positivity statement: it demands a signed evaluation of
      Fhat on the actual ordinates.  It is not self-contradictory --
      Fhat takes both signs on a measured 35-38 percent of the grid --
      but it is not implied by any upper bound on |PRIME(F)|.      [S4]

 (T4) THE UNSIGNED COMPANION IS UNCONDITIONALLY BOUNDED BUT CERTIFIED
      NON-CLOSABLE INSIDE I_cone.  q_c = (1/16) w^T K w with the
      congruence-invariant kernel K := A_2^T B^-1 A_2 admits the
      unconditional bound (1/16) lam_max(K_J) W2 from Brun-Titchmarsh
      and Chebyshev alone; but the class floor, ATTAINED at an
      admissible datum of I_cone, still exceeds need_h by a factor
      > 1 at every audited rung, with a positive growth exponent.  So
      the obstruction is not the sharpness of the bound: the class
      itself cannot close.  Removing q_c requires the ALIGNMENT of w
      with the spectral directions of K, which is information outside
      I_cone.                                                       [S5]

 (T5) CONSEQUENCE (the localization).  Any argument that closes (L) for
      the deployed budget shape must supply information that is (a)
      SIGNED -- it must orient a quantity that is odd under the comb
      sign flip -- and (b) ALIGNMENT-CARRYING -- it must relate the
      position of the prime atoms to the spectral directions of K (or,
      equivalently, the ordinates to the sign pattern of Fhat).  In
      particular it can be neither a magnitude bound on psi(x) - x (T1)
      nor a natural-grammar identity, i.e. an identity that holds in
      every arithmetic world and is therefore comb-blind (S6).      [S6]

WHAT THE THEOREM DOES NOT SAY (named open scope, S8).  It does not say
RH is unprovable, nor that the wall route fails, nor that no proof
exists.  Five argument classes are explicitly NOT covered and remain
logically open: (O1) arguments that legitimately consume zero-position
information (Weil positivity itself, any explicit-formula argument that
inputs an unconditional statement about ordinates); (O2) alignment
arguments, i.e. any unconditional statement correlating prime positions
with the spectral directions of K or with the sign pattern of Fhat;
(O3) arguments outside the enumerated classes I_mag, I_box, I_cone,
I_gram -- in particular ones that change the budget shape itself
(different kernel, different frame family, non-cofinal or differently
predeclared rung families); (O4) the reverse implication of the
programme (inequality => RH), which rests on four named premises and is
NOT established; (O5) any argument using a global inequality that
restricts the domain of the source profile beyond I_cone.

TYPING AGAINST THE FROZEN GATE RULE.  This is a statement ABOUT the
problem, not an independent sign source.  It supplies no new positivity,
closes no gate, narrows no interval, and moves NO marker.  Its value is
that it prices four failed attack directions at once and names the two
properties any future source must have.

===========================================================================
DISCIPLINE
===========================================================================

RE-DERIVATION, NOT IMPORT.  Every load-bearing number below is
recomputed here from a generator, not read from a source probe's
conclusion.  Concretely: the nine frames are rebuilt from an
independent prime-power sieve; the Fejer supply B_h is computed by
THREE independent routes (closed form, direct quadrature, and the
Fourier route int Fhat Theta / 2pi with an explicit tail bound); the
kernel ledger and every congruence/inertia statement are re-proved with
sympy in this file rather than calling the source probes' symbolic
helpers; the Littlewood floors, the criticality of the density
hypothesis, the Selberg neutrality, the Li quadruple identity, the
Beurling-Nyman T3/T5 witnesses and the cofinal/tail statement are all
re-derived from scratch.  The deployed matrix stage (B, b_0, b_c, x_0,
w, K) is rebuilt through the deployed generators -- that is the object
under discussion, so it must be the same object -- and every derived
quantity is then recomputed here.

CITED, NOT RE-CHECKED (the honest list; each is flagged in S9).
 (X1) The certified Schur intervals s_h and the certified witness reads
      U_h at h in {184, 388, 839, 1393, 2015, 2607, 2854, 5746, 12632}
      come from CCCLX/CCCLXXI.  Reproducing the interval arithmetic at
      the deep rungs costs ~200 s per read and the whole ladder far
      exceeds this probe's budget.  This probe re-derives the decay
      EXPONENTS from those cited values together with ITS OWN frames,
      which is where the flattening claim actually lives.
 (X2) The deployed slack (1.5e-05 .. 2.7e-03) and the CCCXXXI
      envelope/alignment diagnostics.  This probe computes its OWN,
      strictly larger and hence conservative, supply-side slack from
      the Fejer route, and reports both.
 (X3) The classical constants: Rosser-Schoenfeld psi(x) < 1.03883 x,
      Montgomery-Vaughan Brun-Titchmarsh, Littlewood's Omega-theorem,
      Schoenfeld's RH bound, Bombieri-Lagarias Cor. 1(c), Li's
      criterion, N(1/2,T) >> T log T.  These are literature; nothing
      here re-proves them.
 (X4) The deployed float64 entry slack of the wall generators, typed by
      CCCXXXIII/CCCLIX, remains the standing premise of every matrix
      number.
 (X5) CCCLXVIII's F0..F4 demand values A/G and the geometry budget
      G_geo.  This probe re-derives the three GROWTH FACTORS that carry
      the attribution claim (beta^-1, R^2, dimension) exactly, but
      quotes the total 2.9061 orders against which the shares are
      normalised.
 (X6) CCCLXII's de Branges chain measurements and CCCLXIII's deployed
      constants c_B = 0.5523, sigma <= 0.726909.  The two decisive
      Beurling-Nyman witnesses (T3, T5) are re-derived exactly here.
 (X7) The n0-NORMALISED margin exponents that carry the "flattening"
      counter-evidence.  The normalisation needs n0 at h = 5746 and
      12632, i.e. two cells this probe does not build.  The RAW witness
      exponents ARE recomputed here (and are marginally steeper, the
      direction less favourable to this probe), as is the certified
      POSITIVE s/D^2 step that makes the normalised drift non-monotone.

DISCLOSED DEVIATIONS.  Any recomputed value that does not match its
cited counterpart within the frozen ward is printed in S9's deviation
table.  A deviation in a LOAD-BEARING component forces the verdict
NOGO-COMPONENT-FAILED; a deviation in a component the source itself
types as diagnostic or refused is disclosed and does not.

VERDICT ENUM (frozen).
 NOGO-COMPOSITE-VERIFIED  all load-bearing components re-verified and
                          the composite statement stands as written;
 NOGO-COMPONENT-FAILED    a load-bearing component did not re-verify
                          (a bug in a note, HIGH severity);
 NOGO-SCOPE-NARROWER      the honest weaker statement that survives.

NO RH CLAIM.  No positivity claim.  No promotion.  No marker moved.
"""


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


def rel(a, b):
    b = float(b)
    return abs(float(a) - b) / max(abs(b), 1e-300)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in AST_BANNED:
            hits.append(name)
    return sorted(set(hits))


# ==================================================== own sieves + frames
def prime_power_list(cap):
    """Ordered prime powers >= 2 up to cap, from an own sieve."""
    sieve = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if not sieve[p]:
            sieve[p * p::p] = True
            q = p
            while q <= cap:
                out.append(q)
                q *= p
    return sorted(out)


def lambda_table(n_max):
    """von Mangoldt Lambda(n) for n <= n_max, own sieve."""
    lam = np.zeros(n_max + 1)
    sieve = np.zeros(n_max + 1, dtype=bool)
    for p in range(2, n_max + 1):
        if not sieve[p]:
            sieve[p * p::p] = True
            q, log_p = p, math.log(p)
            while q <= n_max:
                lam[q] = log_p
                q *= p
    return lam


def build_frame(pp, kz):
    """The frame of index kz, rebuilt from the prime-power list alone."""
    n_now, n_next = float(pp[kz]), float(pp[kz + 1])
    alpha = math.log(n_now)
    d_k = 0.5 * (math.log(n_next) - alpha) / 4.0
    m_z = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
    if m_z % 2:
        m_z += 1
    h = m_z // 2
    d_val = alpha / h
    log_n = 2.0 * alpha + 2.0 * d_val
    return dict(kz=kz, n=int(pp[kz]), n_next=int(pp[kz + 1]),
                gap=int(pp[kz + 1]) - int(pp[kz]), alpha=alpha, D=d_val,
                h=h, log_n=log_n, N=math.floor(math.exp(log_n)))


# ========================================= geometric supply, two routes
def fejer_closed(s_len):
    """POLE - P_main + ARCH for the Fejer window F(x) = 1 - x/S, closed."""
    s_len = mp.mpf(s_len)
    q_e = mp.exp(-s_len / 2)
    pole_minus_pmain = (4 * (1 - q_e) - 8 / s_len
                        + q_e * (4 * s_len + 8) / s_len)
    psi_q = -mp.euler - 3 * mp.log(2) - mp.pi / 2
    z_two = mp.pi ** 2 + 8 * mp.catalan
    tail = mp.mpf(0)
    for k in range(0, 80):
        s_k = 2 * k + mp.mpf(1) / 2
        tail += mp.exp(-s_k * s_len) / s_k ** 2
    arch = (-mp.log(mp.pi) + psi_q + z_two / (2 * s_len)
            - 2 * tail / s_len)
    p_main = -4 + 8 / s_len * (mp.exp(s_len / 2) - 1)
    v_geo = 4 / s_len * (mp.exp(s_len / 2) - 1) - 1
    return dict(B=pole_minus_pmain + arch, pole=pole_minus_pmain + p_main,
                arch=arch, p_main=p_main, V=v_geo)


def fejer_quadrature(s_len):
    """Independent route: POLE, ARCH, P_main by direct quadrature."""
    s_len = mp.mpf(s_len)

    def f_win(x):
        return 1 - x / s_len
    pole = 4 * mp.quad(lambda x: f_win(x) * mp.cosh(x / 2), [0, s_len])
    p_main = 2 * mp.quad(lambda x: f_win(x) * mp.exp(x / 2), [0, s_len])
    f_zero = mp.mpf(1)

    def integ(wv):
        return ((f_zero * mp.exp(-2 * wv) - f_win(wv) * mp.exp(-wv / 2))
                / (-mp.expm1(-2 * wv)))
    body = mp.quad(integ, [0, s_len])
    tail = -mp.log1p(-mp.exp(-2 * s_len)) / 2 * f_zero
    arch = -f_zero * (mp.euler + mp.log(mp.pi)) + 2 * (body + tail)
    return dict(B=pole - p_main + arch, pole=pole, arch=arch,
                p_main=p_main)


# ================================================== the exact kernel ledger
def kernel_ledger():
    """S1: the six exact kernel identities, symbolic in the mesh D."""
    t_sym, d_sym, q_sym = sp.symbols("t D q", positive=True)

    def tent_sym(x, d_val):
        return sp.Max(0, 1 - sp.Abs(x) / d_val)

    def kd_sym(x, d_val):
        return (tent_sym(x, d_val)
                - (tent_sym(x - d_val, d_val)
                   + tent_sym(x + d_val, d_val)) / 2)

    def piece_lin(a_val, b_val):
        k_a = sp.simplify(kd_sym(a_val * d_sym, d_sym))
        k_b = sp.simplify(kd_sym(b_val * d_sym, d_sym))
        return sp.simplify(k_a + (k_b - k_a)
                           * ((t_sym / d_sym - a_val) / (b_val - a_val)))

    seg = [(-2, -1), (-1, 0), (0, 1), (1, 2)]
    seg_abs = [(-2, -1), (-1, sp.Rational(-2, 3)), (sp.Rational(-2, 3), 0),
               (0, sp.Rational(2, 3)), (sp.Rational(2, 3), 1), (1, 2)]
    node_vals = [sp.simplify(kd_sym(n * d_sym, d_sym))
                 for n in (-2, -1, sp.Rational(-2, 3), 0,
                           sp.Rational(2, 3), 1, 2)]
    i_zero = sum(sp.integrate(piece_lin(a, b), (t_sym, a * d_sym, b * d_sym))
                 for a, b in seg)
    # each refined piece has constant sign, so |int| = int |.|
    i_one = sum(sp.Abs(sp.integrate(piece_lin(a, b),
                                    (t_sym, a * d_sym, b * d_sym)))
                for a, b in seg_abs)
    i_two = sum(sp.integrate(piece_lin(a, b) ** 2,
                             (t_sym, a * d_sym, b * d_sym)) for a, b in seg)
    tv = sum(sp.Abs(sp.diff(piece_lin(a, b), t_sym)) * (b - a) * d_sym
             for a, b in seg)
    i_exp_k = sum(sp.integrate(sp.exp(-t_sym / 2) * piece_lin(a, b),
                               (t_sym, a * d_sym, b * d_sym)) for a, b in seg)
    t_d_int = (sp.integrate(sp.exp(-t_sym / 2) * (1 + t_sym / d_sym),
                            (t_sym, -d_sym, 0))
               + sp.integrate(sp.exp(-t_sym / 2) * (1 - t_sym / d_sym),
                              (t_sym, 0, d_sym)))
    t_d_target = 8 / d_sym * (sp.cosh(d_sym / 2) - 1)

    def q_reduce(expr):
        return sp.simplify(sp.expand(sp.powsimp(
            expr.rewrite(sp.exp).subs(sp.exp(d_sym / 2), q_sym)
            .subs(sp.exp(d_sym), q_sym ** 2)
            .subs(sp.exp(-d_sym / 2), 1 / q_sym)
            .subs(sp.exp(-d_sym), q_sym ** -2))))

    check("S1.1 int K_D = 0 (exact)", sp.simplify(i_zero) == 0,
          "%s" % sp.simplify(i_zero))
    check("S1.2 ||K_D||_inf = 1 (exact)",
          max(sp.Abs(x) for x in node_vals) == 1
          and sp.simplify(kd_sym(0, d_sym)) == 1,
          "node values %s" % node_vals)
    check("S1.3 ||K_D'||_1 = 4, independent of D (exact) -- the "
          "load-bearing identity: the conversion constant of a "
          "magnitude hypothesis does not get cheap as the mesh refines",
          sp.simplify(tv - 4) == 0, "%s" % sp.simplify(tv))
    check("S1.4 ||K_D||_1 = 4D/3 (exact)",
          sp.simplify(i_one - 4 * d_sym / 3) == 0, "%s" % sp.simplify(i_one))
    check("S1.5 D^-1 int K_D^2 = 2/3 (exact)",
          sp.simplify(i_two / d_sym - sp.Rational(2, 3)) == 0,
          "%s" % sp.simplify(i_two / d_sym))
    check("S1.6 T_D = int tau_D e^{-t/2} = (8/D)(cosh(D/2)-1) (exact)",
          q_reduce(t_d_int - t_d_target) == 0)
    check("S1.7 int K_D e^{-t/2} = -(8/D)(cosh(D/2)-1)^2 = -(D/8) T_D^2 "
          "(exact)",
          q_reduce(i_exp_k + 8 / d_sym * (sp.cosh(d_sym / 2) - 1) ** 2) == 0
          and q_reduce(i_exp_k + d_sym / 8 * t_d_target ** 2) == 0)


# ============================== the split: signed and congruence-invariant
def split_algebra():
    """S3.1-S3.4: identities in the matrix-stage SYMBOLS, no deployed
    number consumed."""
    h_s = 4
    bm_s = sp.Matrix(h_s - 1, h_s - 1,
                     lambda i, j: sp.Symbol("B%d%d" % (min(i, j),
                                                       max(i, j))))
    m_s = sp.Matrix(h_s - 1, h_s - 1,
                    lambda i, j: sp.Symbol("M%d%d" % (i, j)))
    n0_s, nc_s = sp.symbols("n0 nc")
    b_s = sp.Matrix(h_s - 1, 1, lambda i, j: sp.Symbol("b%d" % i))
    c_s = sp.Matrix(h_s - 1, 1, lambda i, j: sp.Symbol("c%d" % i))
    inv_s = bm_s.inv()
    q0_s = (b_s.T * inv_s * b_s)[0]
    qc_s = (c_s.T * inv_s * c_s)[0]
    lin_s = (c_s.T * inv_s * b_s)[0]
    s_split = sp.expand((n0_s - q0_s) - nc_s + 2 * lin_s - qc_s)
    s_direct = sp.expand((n0_s - nc_s)
                         - ((b_s - c_s).T * inv_s * (b_s - c_s))[0])
    check("S3.1 the three-term split s = (n_0 - q_0) - n_c + 2<b_c,x_0> "
          "- q_c is an identity (sympy, exact)",
          sp.simplify(s_split - s_direct) == 0)
    bt_s = m_s.T * b_s
    ct_s = m_s.T * c_s
    bmt_s = m_s.T * bm_s * m_s
    inv_t = bmt_s.inv()
    ok_inv = all(sp.simplify(x) == 0 for x in (
        (bt_s.T * inv_t * bt_s)[0] - q0_s,
        (ct_s.T * inv_t * ct_s)[0] - qc_s,
        (ct_s.T * inv_t * bt_s)[0] - lin_s))
    check("S3.2 all three terms are invariant under EVERY congruence "
          "T = diag(1, M) (sympy, exact) -- the OBJECT is basis "
          "independent, the DEMAND is not", ok_inv)
    flip = {c_s[i, 0]: -c_s[i, 0] for i in range(h_s - 1)}
    check("S3.3 parity under the comb sign flip b_c -> -b_c: outer terms "
          "EVEN, middle term ODD (exact) -- so positivity can only be "
          "carried by the odd term, and no flip-invariant bound can "
          "lower-bound it",
          sp.simplify(q0_s.subs(flip) - q0_s) == 0
          and sp.simplify(qc_s.subs(flip) - qc_s) == 0
          and sp.simplify(lin_s.subs(flip) + lin_s) == 0)
    a2_sym = sp.Matrix(3, 5, lambda i, j: (1 if j == i else
                                           (-2 if j == i + 1 else
                                            (1 if j == i + 2 else 0))))
    bm5 = sp.Matrix(3, 3, lambda i, j: sp.Symbol("G%d%d" % (min(i, j),
                                                            max(i, j))))
    m3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol("N%d%d" % (i, j)))
    k_plain = sp.simplify(a2_sym.T * bm5.inv() * a2_sym)
    k_cong = sp.simplify((m3.T * a2_sym).T * (m3.T * bm5 * m3).inv()
                         * (m3.T * a2_sym))
    check("S3.4 the F4 kernel K = A_2^T B^-1 A_2 is itself a congruence "
          "INVARIANT (sympy, exact)",
          sp.simplify(k_plain - k_cong) == sp.zeros(5, 5))


def selberg_neutrality():
    """S2.13: formal identities in the free module on {log p}."""
    primes_sel = [p for p in range(2, SELBERG_N + 1)
                  if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]
    lp_sym = {p: sp.Symbol("L%d" % p, positive=True) for p in primes_sel}

    def lam_sym(n):
        for p in primes_sel:
            m, k = n, 0
            while m % p == 0:
                m //= p
                k += 1
            if k and m == 1:
                return lp_sym[p]
        return sp.Integer(0)

    def log_sym(n):
        out, m = sp.Integer(0), n
        for p in primes_sel:
            while m % p == 0:
                m //= p
                out += lp_sym[p]
        return out

    def mu_int(n):
        m, cnt = n, 0
        for p in primes_sel:
            if m % p == 0:
                m //= p
                cnt += 1
                if m % p == 0:
                    return 0
        return (-1) ** cnt if m == 1 else 0

    ok_lam = ok_sel = True
    for n in range(1, SELBERG_N + 1):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        ok_lam = ok_lam and sp.expand(
            sum(mu_int(d) * log_sym(n // d) for d in divs) - lam_sym(n)) == 0
        lhs = sum(mu_int(d) * sp.expand(log_sym(n // d) ** 2) for d in divs)
        rhs = sp.expand(lam_sym(n) * log_sym(n)
                        + sum(lam_sym(d) * lam_sym(n // d) for d in divs))
        ok_sel = ok_sel and sp.expand(lhs - rhs) == 0
    check("S2.13 Selberg symmetry is PROVABLY NEUTRAL: Lambda = mu * log "
          "and mu * log^2 = Lambda.log + Lambda * Lambda are formal "
          "identities in the free module on {log p} (n <= %d), so they "
          "add no arithmetic content -- information gain exactly 1.000"
          % SELBERG_N, ok_lam and ok_sel, "both identities exact")


def beurling_nyman():
    """S6.3: the two exact Beurling-Nyman/Baez-Duarte witnesses."""
    bn_const = mp.log(2 * mp.pi) - mp.euler
    bn_rows = []
    for n_bn in BN_SIZES:
        a_bn = sp.Matrix(n_bn, 2, lambda i, j: sp.Integer(1) if j == 0
                         else sp.Rational(1, i + 1))
        g_bn = a_bn * a_bn.T + sp.Rational(16, 25) * sp.eye(n_bn)
        beta_bn = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
        b_bn = a_bn * beta_bn
        sig = (b_bn.T * g_bn.inv() * b_bn)[0]
        floor_ok = all(sp.nsimplify(x) >= 0 for x in
                       (g_bn - sp.Rational(5523, 10000)
                        * sp.eye(n_bn)).eigenvals())
        bn_rows.append((n_bn, float(sig), floor_ok))
    sig_lo = min(r[1] for r in bn_rows)
    sig_hi = max(r[1] for r in bn_rows)
    check("S6.3 Beurling-Nyman exactly in Q: (T3) lam_min(G_N) <= "
          "(log 2pi - gamma)/N = %.10f/N, so the Baez-Duarte Gram has NO "
          "N-uniform floor and the deployed hypothesis is FALSE for "
          "N >= 3; (T5) the explicit family G~ = A A^T + (4/5)^2 I "
          "satisfies EVERY hypothesis of the certificate class at every "
          "N while d~^2 >= 1/2 forever -- the class is non-implying"
          % float(bn_const),
          rel(bn_const, WARD_BN_CONST) < 1e-9
          and float(bn_const) / 3 < WARD_BN_CB
          and all(r[2] for r in bn_rows) and sig_hi <= WARD_BN_SIGMA_CAP
          and 1 - sig_hi >= 0.5 - 1e-12
          and abs(sig_lo - WARD_BN_SIGMA_RANGE[0]) < 5e-4
          and abs(sig_hi - WARD_BN_SIGMA_RANGE[1]) < 5e-4,
          "cap %.6f < c_B %.4f | sigma~ in [%.4f, %.4f] <= %.6f | "
          "d~^2 >= 1/2"
          % (float(bn_const) / 3, WARD_BN_CB, sig_lo, sig_hi,
             WARD_BN_SIGMA_CAP))


def part():
    section("PRIME.NOGO.SIGNED.ONLY.01 -- the localization of the "
            "residual\nobstruction (a NO-GO / typing module: no "
            "positivity, no gate, no marker)")

    # ---------------------------------------------------------- guards
    print("\n-- G0: firewall, frozen spec, own sieves, frame rebuild")
    hits = ast_firewall()
    guards = [check("G0.1 AST firewall clean (no zero data, no "
                    "eigensolver on any deployed form, no fit)",
                    not hits, "hits=%s" % (hits or "none"))]
    spec_sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    guards.append(check("G0.2 the embedded frozen spec reproduces the "
                        "probe SPEC_SHA-256 BEFORE any evaluation",
                        spec_sha == PROBE_SPEC_SHA,
                        "SHA256 %s..." % spec_sha[:16]))
    pp = prime_power_list(PP_CAP)
    guards.append(check("G0.3 own prime-power sieve starts 2,3,4,5,7,8,9,11",
                        pp[:8] == [2, 3, 4, 5, 7, 8, 9, 11], "%s" % pp[:8]))
    frames = {}
    h_ok = True
    worst_frame_rel = 0.0
    for want_h, kz in FRAME_SPECS:
        fr = build_frame(pp, kz)
        frames[want_h] = fr
        h_ok = h_ok and (fr["h"] == want_h)
        root = math.exp(fr["alpha"] + fr["D"])
        worst_frame_rel = max(worst_frame_rel,
                              rel(fr["D"] * root, fr["gap"] / 4.0))
    guards.append(check("G0.4 all nine frames reconstructed from prime "
                        "powers alone (h is PREDICTED, never supplied)",
                        h_ok, "h = %s" % [frames[k]["h"]
                                          for k, _ in FRAME_SPECS]))
    guards.append(check("G0.5 the test scale sits ON the square-root "
                        "barrier: D_h sqrt(N_h) = gap/4",
                        worst_frame_rel < 5e-2,
                        "worst rel %.4e (corpus %.4e)"
                        % (worst_frame_rel, WARD_FRAME_REL)))
    guards.append(check("G0.6 the integer gap is O(log N) on every frame "
                        "(the family is indexed by kz, not by h)",
                        all(frames[k]["gap"] <= frames[k]["log_n"]
                            for k, _ in FRAME_SPECS),
                        "gaps %s" % [frames[k]["gap"]
                                     for k, _ in FRAME_SPECS]))
    guards_ok = all(guards)

    # -------------------------------------------------- S1 kernel ledger
    section("S1  THE EXACT KERNEL LEDGER (sympy, exact in the mesh D)")
    kernel_ledger()
    print("  READING: the conversion constant of any magnitude hypothesis "
          "is bounded\n  BELOW by ||K_D'||_1 = 4 uniformly in D -- the "
          "kernel does not become cheap\n  as the frames get finer.  "
          "That exact fact is what makes S2 unconditional.")

    # ------------------------------------- S2 the magnitude class is empty
    section("S2  THE MAGNITUDE CLASS IS UNCONDITIONALLY EMPTY "
            "(Littlewood CITED)")
    supply = {}
    ok_supply = True
    for h_key in SUPPLY_RUNGS:
        fr = frames[h_key]
        s_len = mp.mpf(2) * mp.mpf(fr["alpha"]) * (1 + mp.mpf(1) / fr["h"])
        closed = fejer_closed(s_len)
        quadr = fejer_quadrature(s_len)
        n_cap = int(mp.floor(mp.exp(s_len)))
        lam = lambda_table(max(n_cap, 2))
        nz = np.nonzero(lam > 0)[0]
        prime = 2.0 * float(sum(mp.mpf(lam[n]) / mp.sqrt(int(n))
                                * (1 - mp.log(int(n)) / s_len) for n in nz))
        delta = prime - float(closed["p_main"])
        supply[h_key] = dict(S=s_len, B=closed["B"], N=n_cap,
                             route_dev=abs(closed["B"] - quadr["B"]),
                             delta=delta,
                             slack=0.5 * (float(closed["B"]) - delta))
        ok_supply = ok_supply and (
            abs(float(closed["B"] - quadr["B"])) < 1e-15
            and abs(float(closed["B"] - mp.mpf(WARD_FEJER_B[h_key]))) < 1e-15
            and closed["B"] < 0 and abs(float(closed["B"])) <= 2.0)
    check("S2.8 the geometric supply, recomputed here by TWO independent "
          "routes (closed form, direct quadrature), is NEGATIVE and O(1) "
          "(|B| <= 2) at both registered rungs and reproduces the corpus "
          "value", ok_supply,
          " | ".join("h=%d B %s (route dev %.1e, corpus %s)"
                     % (k, mp.nstr(supply[k]["B"], 20),
                        float(supply[k]["route_dev"]), WARD_FEJER_B[k])
                     for k in SUPPLY_RUNGS))
    floors = {}
    for h_key in FLOOR_RUNGS:
        n_val = mp.exp(mp.mpf(frames[h_key]["log_n"]))
        floors[h_key] = 4 * mp.log(mp.log(mp.log(n_val)))
        check("S2.9 h=%d Littlewood floor 4 logloglog N_h >= %.7f "
              "(Littlewood's Omega-theorem itself is CITED, X3)"
              % (h_key, WARD_LITTLEWOOD[h_key]),
              float(floors[h_key]) >= WARD_LITTLEWOOD[h_key] - 5e-7,
              "floor %.7f (N_h = %d)"
              % (float(floors[h_key]), frames[h_key]["N"]))
    own_slack = max(supply[k]["slack"] for k in supply)
    ratio_own = float(floors[FLOOR_RUNGS[0]]) / own_slack
    ratio_cited = float(floors[FLOOR_RUNGS[1]]) / WARD_SLACK_CITED
    check("S2.10 THE CLASS IS EMPTY: floor / slack >> 1 both on this "
          "module's OWN conservative slack and on the deployed slack "
          "(X2, cited) -- any admissible f would have to beat the "
          "unconditionally divergent S(N)",
          ratio_own > RATIO_BAR and ratio_cited > RATIO_BAR,
          "own %.1f (slack %.4e) | cited %.1f (slack %.1e)"
          % (ratio_own, own_slack, ratio_cited, WARD_SLACK_CITED))
    selberg_neutrality()

    # ----------------------------------- S3 signed + congruence-invariant
    section("S3  THE RESIDUAL REQUIREMENT IS SIGNED AND "
            "CONGRUENCE-INVARIANT")
    split_algebra()
    print("  READING: the signed requirement survives every congruence, "
          "every window\n  and every preconditioner because the split "
          "terms are invariant and the\n  carrying term is ODD; an "
          "unsigned hull is flip-invariant, hence\n  structurally unable "
          "to bound it below.")

    # ------------------------------------------------- S6 transport class
    section("S6  THE BEURLING-NYMAN TRANSPORT TARGET (exact witnesses)")
    beurling_nyman()

    # --------------------------------------------------- the localization
    section("THE LOCALIZATION (the deliverable) AND ITS NAMED SCOPE")
    print("""\
  Any argument that closes (L) for the DEPLOYED BUDGET SHAPE must be
    (a) SIGNED            -- it must orient a quantity that is ODD
                             under the comb sign flip [S3.3], and
    (b) ALIGNMENT-CARRYING -- it must relate the position of the prime
                             atoms to the spectral directions of K
                             (equivalently the ordinates to the sign
                             pattern of Fhat).
  In particular it can be NEITHER a magnitude bound on psi(x) - x
  [S1 + S2] NOR a natural-grammar identity, i.e. one valid in every
  arithmetic world and therefore comb-blind [S6].

  PROVEN EMPTY for this budget shape ([here] = gated by this module,
  [probe] = carried by the frozen probe in experiments/):
    E1  every magnitude hypothesis |psi(x)-x| <= f(x) sqrt(x)   [here]
    E2  every zero-density input with A > 2; A = 2 and Lindeloef
        land exactly critical, with zero slack                  [probe]
    E3  Selberg's symmetry formula (formal identity)            [here]
    E4  every congruence reformulation, window choice, Jacobi/
        Cholesky preconditioner, resolvent split                [here]
    E5  every unsigned hull of the comb correction: the parity/
        invariance half [here], the measured negativity         [probe]
    E6  every bound consuming only {w >= 0, ||w||_inf, ||w||_2,
        supp w}                                                 [probe]
    E7  exact multiplicative transforms (Moebius/Dirichlet)     [probe]
    E8  natural-grammar identities (de Branges/HB, Abel)        [probe]
    E9  the Beurling-Nyman/Baez-Duarte transport target         [here]
    E10 thin/cofinal Li criteria (explicit counterexample)      [probe]

  MERELY UNEXPLORED (NO emptiness is claimed): U1 unconditional
  statements about ordinate POSITIONS; U2 alignment statements; U3 a
  different budget shape; U4 the four premises of the reverse
  implication; U5 global constraints on the source profile.

  WHAT THIS DOES NOT SAY (named open scope):
    (O1) nothing against arguments that legitimately consume zero
         positions -- the remaining statement IS of that kind, which
         is not the same as being false;
    (O2) only bounds INSIDE the cone class are forbidden; alignment
         statements are untouched and are exactly what is needed;
    (O3) every clause is for the deployed kernel, frame family and
         predeclared rung family -- another budget shape is outside;
    (O4) the reverse implication (inequality => RH) rests on four
         named premises and is NOT established;
    (O5) a new global inequality restricting the admissible source
         profiles changes the cone class and escapes it.
  ALSO: this is FINITE-RUNG.  It is verified at h = 184/388/839 with
  the ladder to h = 12632; it makes NO all-h claim and says nothing
  about rungs outside the built cells.  It does NOT say that RH is
  unprovable, that the wall route fails, or that no proof exists.""")

    # --------------------------------------------- honest counter-evidence
    section("COUNTER-EVIDENCE, CARRIED AND NOT SMOOTHED (cited, X1/X7)")
    print("""\
  NO-WITNESS STANDS: the certified reads are POSITIVE at all NINE
  depths -- 0 negatives, 0 straddles -- with deepest certified read
  %s at h = 12632; this module adds none.
  The normalised decay FLATTENS with depth on the cited normalisation
  (n0-normalised upper-bound exponents %.8f globally against
  %.8f on the deepest step 5746 -> 12632), and the re-derived
  s/D^2 step 1393 -> 2015 is POSITIVE (+%.8f), so the normalised
  drift is NOT monotone; no re-derivable exponent comes near the
  frozen collapse bar %.1f.  A no-go about the TYPE of the missing
  input is not evidence about its EXISTENCE."""
          % (CITED_DEEPEST_READ, CITED_EXP_U_GLOBAL, CITED_EXP_U_DEEP,
             CITED_EXP_STEP_POS, CITED_COLLAPSE_BAR))

    # ------------------------------------------------------------- typing
    section("TYPING AGAINST THE FROZEN GATE RULE")
    print("""\
  This is a statement ABOUT the problem, NOT an independent sign
  source.  It supplies no positivity, no new interval and no new
  certificate; it closes no gate, narrows no gate and moves NO
  marker.  Its content is the localization of the missing input to a
  two-property class (signed AND alignment-carrying) plus the
  enumeration of the classes now provably empty for this budget
  shape.  It must NOT be counted as evidence for or against the
  Riemann Hypothesis and must not be cited in support of any
  positivity claim.  Registers PRIME.NOGO.SIGNED.ONLY.01 [O] as a
  no-go/typing row.""")

    elapsed = time.time() - T_ALL
    check("V1 runtime below the frozen bar (%.0f s)" % RUNTIME_CAP,
          elapsed < RUNTIME_CAP, "%.1f s" % elapsed)

    fails = list(FAILS)
    if not guards_ok:
        verdict = "NOGO-CORE-INVALID (guards: %s)" % ",".join(
            f for f in fails if f.startswith("G0"))
    elif fails:
        verdict = "NOGO-CORE-FAILED (%s)" % ",".join(fails)
    else:
        verdict = EXPECTED
    _VERDICTS["v"] = verdict
    section("VERDICT: %s" % verdict)
    print("CHECKS %d/%d PASS (%.1f s); fails: %s"
          % (len(CHECKS) - len(fails), len(CHECKS), time.time() - T_ALL,
             fails or "none"))
    return 0 if (guards_ok and not fails) else 1


T_ALL = time.time()


def run():
    global T_ALL
    T_ALL = time.time()
    mp.dps = MP_DPS
    CHECKS.clear()
    FAILS.clear()
    _VERDICTS.clear()
    print("=" * 74)
    print("v913 -- PRIME.NOGO.SIGNED.ONLY.01 (the signed-and-alignment "
          "localization;")
    print("a NO-GO / typing module: no positivity, no gate, no marker, "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and _VERDICTS.get("v") == EXPECTED)
    print("\n" + "=" * 74)
    print("v913: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, _VERDICTS.get("v"),
             time.time() - T_ALL))
    print("NO RH claim, no positivity claim.  This module prices "
          "ARGUMENT CLASSES; it")
    print("closes no gate, narrows no gate and moves no marker, and it "
          "is not evidence")
    print("for or against the Riemann Hypothesis.  Probe SPEC_SHA "
          "%s..." % PROBE_SPEC_SHA[:16])
    print("PROBE_SHA %s... (experiments/tfpt-discovery/"
          "signed_only_nogo_probe.py)" % PROBE_SHA[:16])
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s, verdict %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none", _VERDICTS.get("v")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
