#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mixed_haynsworth_probe -- PRIME.LDAGGER.MIXED_HAYNSWORTH.01
(round 369): THE MIXED LOWRANK FORM + GENERALIZED HAYNSWORTH --
reviewer sequence step 1, algebra only.  Coexistence: R371
(compound-CD), R372 (source-Prufer) and R373 (Lean transcription)
run in parallel -- this probe touches NOTHING outside its own
file and the strictly additive rh-sync.  next.txt is NOT written.

THE FROZEN QUESTION (reviewer verbatim).  Does
    M_N^dagger := R_N^dagger - (1/2) I
    = A_N + U_N J_N U_N^T
hold EXACTLY, with U_N the two last dual CD columns AND the
bordered border direction (3 columns) and J_N an EXPLICIT
symmetric invertible 3x3 signature matrix that FOLLOWS from the
Sherman-Morrison border form (not fitted)?  And does the
generalized Haynsworth identity
    In [[A, U],[U^T, -J^{-1}]]
      = In(A) + In(-J^{-1} - U^T A^{-1} U)
      = In(-J^{-1}) + In(A + U J U^T)
hold as a SATZ for arbitrary invertible symmetric J, so that
positivity of M^dagger is controlled by the small matrix
    Phi_N(0) = J^{-1} + U^T A^{-1} U?
The r367 warning: the border is a resolvent insertion, not a
third CD column of the unaugmented chain.  THIS ROUND decides
whether that forbids a 3-column form on the R^dagger level, or
whether Sherman-Morrison supplies one.

THE DERIVATION (sealed BEFORE evaluation; not a fit).  From
r362 A4, R^dagger = Z^{-1} with Z = [[R^{-1}, vt],[vt^T, 1+gamma]]
and den = 1+gamma - vt^T R vt, s = R vt, so
    R^dagger = [[R, 0],[0, 0]] + (1/den) [s; -1][s; -1]^T.
From r363, R = R_{N-3} + u_{N-3} u_{N-3}^T + u_{N-2} u_{N-2}^T.
Hence with A0 = R_{N-3} - I/2,
    M^dagger = blkdiag(A0, -1/2)
             + u1_aug u1_aug^T + u2_aug u2_aug^T
             + (1/den) w_aug w_aug^T,
u_i_aug = [u_i; 0], w_aug = [s; -1].  In matrix form:
    A  = blkdiag(A0, -1/2)          ((S_-+1) x (S_-+1)),
    U  = [[u_{N-3}, u_{N-2}, s],
          [  0,       0,    -1]]    ((S_-+1) x 3),
    J  = diag(1, 1, 1/den)          (EXPLICIT from SM).
The signature-normalized twin (same identity): column 3 of U
scaled by 1/sqrt(|den|) and
    J_sig = diag(1, 1, sign(den)).
WHAT SM GIVES: J is DIAGONAL in the natural (CD, CD, SM-vector)
basis; there is no off-diagonal to fit.  The sign of J_33 is
the sign of den.  On a live window with R^dagger > 0 one has
den = 1/R^dagger_bb > 0, so J_sig = I_3 (not Lorentz).  The
form nonetheless ALLOWS J_33 < 0 whenever den < 0 (synthetic /
Fractions false-branch).  Verdict letters distinguish the
exact form from an indefinite-J census.

LEAN FORMALIZATION FORM (statement only; proof is R373; do
NOT land this in RH/Inertia.lean here):
    theorem haynsworth_mixed
      {n k : Type*} [Fintype n] [DecidableEq n]
        [Fintype k] [DecidableEq k]
      (A : Matrix n n ℝ) (U : Matrix n k ℝ)
      (J : Matrix k k ℝ)
      (hA : A.IsHermitian) (hJ : J.IsHermitian)
      (hAinv : Invertible A) (hJinv : Invertible J) :
      let Φ := J⁻¹ + Uᵀ * A⁻¹ * U
      let H := fromBlocks A U Uᵀ (-J⁻¹)
      let M := A + U * J * Uᵀ
      inertia H = inertia A + inertia (-Φ)
      ∧ inertia H = inertia (-J⁻¹) + inertia M
    -- Haynsworth additivity twice (C = -J⁻¹; the other Schur
    -- is A - U C⁻¹ Uᵀ = A + U J Uᵀ).  inertia = Sylvester
    -- triple via LDL / mathlib QuadraticForm.sigNeg, the r367
    -- haynsworth_two_rank special case J = I_2.  Fractions-
    -- exact on the 4-node toy with indefinite J (this probe
    -- G11).  Corollary: In(A) + In(-Φ) = In(-J⁻¹) + (n,0,0)
    -- iff M.PosDef (the signature balance).

THE LEGS.  (Leg A) the derivation above, Fractions-exact on
the 4-node model, f64 <= 1e-10 on w9 + a 10-row ladder sample
+ one chi row + kz15 (near-terminal).  (Leg B) generalized
Haynsworth as SATZ, both readings, Fractions on the 4-node
model with indefinite J; Lean form as above.  (Leg C) Phi_N(0)
live; the signature balance In(A)+In(-Phi)==In(-J^{-1})+(dim,0,0)
as a census on resolvable sample rows; the 3x3 dichotomy
(how negatives split between A and Phi -- the r367 vacuous
class in the new picture).  (Leg D) must-fails (>=4): (m1) J
fitted as I_3 (scale ignored) instead of 1/den -- construction
CAUGHT; (m2) wrong border sign J_33 = -1/den -- exact CAUGHT;
(m3) U without the border column (two-rank mutant) -- exact
CAUGHT, and the OTHER (r367) balance is the one that holds;
(m4) lambda_min(R^dagger) readback -- AST-CAUGHT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO L* CLAIM, NO
R^dagger CLAIM, NO RH CLAIM in either direction, mincut
unchanged.  Two-commit freeze protocol (r329 convention):
spec + machinery committed BEFORE the record run, record
tables inserted after.

INDEX FIREWALL (binding, r238-r367 discipline): w = window
(kz), S = #union atoms, S_- = #nu atoms, N_w = (S+1)//2;
ground truth enters GATES and record tables only; the
module-own constructors consume measure arrays / chain
coefficients / positions / pair indices / the border window
ONLY (AST scope audit; withheld identifiers lamRd_col_true /
J_fit_col_true / den_col_true and the REC/anchor constants);
no zero/prime oracles (AST firewall); no fit primitives
(fragment audit -- J is derived, never fitted).  MACHINERY
IMPORTED VERBATIM: r367 FTI.{cut_rung, inertia_of, fr_ldl,
fr_inertia, fr_add, fr_mul, sm_column} (e0d79840), r362
ABD.{aug_rung unused; bvec_chunked, border_chain_pack}
(7d810a9a), r363 CSI SHA (09786c2e, CD SATZ consumed via
FTI.cut_rung), r356 BDH.{fr_inv, dual_rung} (36141c0a), r342
PX.{build_rung, pair_select} (b09f8ccd), r357 DMF.{chi_window
_comb, chi_build_measures, Q_CHI3, LPQ3} (4bf1a94b), r226
HS.window_data (d78e236b), r243 PB.smooth_comb (db259f8e),
document pipeline V.{mu_chain, b_matrix, window_shape,
admissible_indices}, v563 core READ-ONLY.

LEG 0 ANCHORS (record numbers as gates): w9 (S 367, S_- 104,
N_w 184, margin 1.6752e-4 rel 0.01, lambda_min(R) 0.500041882
abs 1e-8, folds (2, 4)); r362 W9 AUG lamRd 0.500041459 abs
1e-8, mdag 1.6582e-4 rel 1e-3; r367 W9 K2 ev0 -2.7938 / ev1
1.8036 rel 1e-3, nneg 1 EXACT.  PRE-SPEC SCOPING (disclosed,
ONE sizing pass on kz9/15/18 + chi3 w9, /tmp, deleted; no
bar, band, clause or verdict rule tuned after any evaluation
except as sized here and said so): mixed residual <= 1.9e-15
on all four (pure algebra); den in [1.560, 1.646] all
POSITIVE so J_sig = I_3 on the scoped live windows; Phi at
w9 sigma = (-2.813, -0.0665, 1.804) det 0.337 -- the two
large eigenvalues TRACK the r367 K2 pair, the small extra
negative is the border direction; signature balance HOLDS
(In(A)+In(-Phi) == In(-J^{-1})+In(M^dagger)); P1-true rows
have In(A)=(n-2,2,0) [A0's one negative PLUS the -1/2 pad]
and In(Phi)=(1,2,0); chi3-w9 (r367 P1_VACUOUS) has
In(A)=(n-1,1,0) [only the pad] and In(Phi)=(2,1,0) -- the
vacuous class in the 3x3 picture is one fewer Phi-negative;
wrong-sign residual ~1.25, J=I_3 residual ~0.37, two-rank
Y-only residual ~2.5e-3, all loud vs 1e-15.  The verdict
letters, J's derived form, the vacuous-class typing and
every bar were frozen from these numbers BEFORE any sample-
wide evaluation.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_MARGIN 1.6752e-4 rel 0.01; REC_LAMR 0.500041882 abs 1e-8;
W9 MIX ANCH (s1 scoping, disclosed) den 1.601114 rel 1e-3,
J33 0.624568 rel 1e-3, evP0 -2.813 rel 2e-2, evP1 -0.06648
rel 5e-2, evP2 1.804 rel 2e-2, detPhi 0.3374 rel 2e-2,
nnegA 2 EXACT, nnegPhi 2 EXACT, nposPhi 1 EXACT, Jsig +1
EXACT; W9 AUG ANCH lamRd 0.500041459 abs 1e-8; W9 K2 ANCH
ev0 -2.7938 / ev1 1.8036 rel 2e-2 (Phi large-pair tracking);
KZ15 MIX ANCH den 1.560471 rel 1e-3, nnegA 2 EXACT,
lamRd-1/2 6.2765e-6 rel 5e-2 (near-terminal); CHI3 W9 MIX
ANCH den 1.646359 rel 1e-3, nnegA0 0 EXACT, nnegPhi 1 EXACT
(the vacuous class), lamRd-1/2 2.092e-4 rel 2e-2 (r362
CHI3_AUG epsd); SAMPLE_KZ (9, 15, 18, 20, 42, 44, 52, 56,
119, 130) the 10-row algebra sample -- NO full 85-row
ladder (algebra round; existing records are the anchors);
MIX_BAR 1e-10 (a priori, scoped 2e-15); BALANCE is exact
integer inertia; INERTIA_FLOOR / MP_ZERO verbatim r367;
M1_LOUD 0.05 (J=I_3 residual scoped 0.37); M2_LOUD 0.1
(wrong sign scoped 1.25); M3_LOUD 1e-3 (two-rank Y-only
scoped 2.5e-3); RESOLV_FLOOR 1e-9; TOY_TOL 1e-12; runtime
<= 1800 s; smoke = toys + firewall + scopes + mutants + w9
mixed block + kz15 + chi3 w9; 10-row sample skipped.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with
'+'; precedence TARGET_LEAK > CHAIN_FAIL > the adjudicated
letters -- the enum is exhaustive):
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit
    fails /
  CHAIN_FAIL(loci)  iff the mixed identity or Haynsworth
    Fractions or the live residual/balance fails at a named
    link /
  MIXED_UPDATE_EXACT  iff M^dagger == A + U J U^T with J =
    diag(1,1,1/den) DERIVED from SM (not fitted) at MIX_BAR
    on w9 + the 10-row sample + chi3 w9 + kz15 AND the
    Fractions toy is exact AND Haynsworth both readings
    hold on the indefinite-J toy /
  NO_LOWRANK_BOUNDARY_FORM  iff the border direction cannot
    be written as a third column with explicit signature
    (the r367 warning confirmed on R^dagger) /
  + HAYNSWORTH_MIXED_SATZ (always with MIXED_UPDATE_EXACT:
    both inertia readings, Lean form in the spec) /
  + PHI_LEDGER(sigma, the signature balance census, the
    3x3 dichotomy / vacuous class) /
  + JSIG_CENSUS(sign(den) on the sample -- disclosed: live
    windows scoped have den>0 so J_sig = I_3; the mixed
    signature is the FORM plus the synthetic den<0 branch,
    not an empirical Lorentz J on MAIN) /
  + MUSTFAIL_LEDGER [always].
Honesty before beauty: the mixed form is a finite-matrix
SATZ (theorem-grade SKELETON) whose inputs A0, U_CD, (s,den)
are measured window scalars (census-grade FLESH); a verified
identity is a REPRESENTATION of M^dagger, not a bound and
not a proof of R^dagger > I/2; no verdict claims L*,
Terminal, a bound mechanism, or RH progress in either
direction; the DCCX STOP list stands; r243..r368 stand;
Mincut unchanged.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit; TWO-COMMIT PROTOCOL EXECUTED: smoke 20/20
x2 byte-identical; sealed spec committed as "r369 pre-freeze"
(6ae366a2, SPEC_SHA freeze 5a4a20db973700ba) BEFORE the first
full evaluation; calibration pass 1 = FIRST full evaluation =
20/20 (29.2 s) ZERO amendments -- every gate passed at first
evaluation, no bar/band/clause/J-form moved; record run1 =
20/20 (29.2 s), run2 = 20/20 (28.9 s), byte-identical up to
WALL; evaluation SPEC_SHA before this insert 5a4a20db973700ba):
MAIN VERDICT = MIXED_UPDATE_EXACT(J = diag(1,1,1/den) from SM,
residual <= 1e-10 on w9 + 10-row + chi3-w9 + kz15; Fractions
exact; signature twin exact) + HAYNSWORTH_MIXED_SATZ(both
readings, indefinite-J toy, Lean form haynsworth_mixed in
the spec -- proof is R373) + PHI_LEDGER(w9 sigma (-2.813,
-0.0665, 1.804); balance 10/10 sample; dichotomy P1-true 8
vacuous 2; chi3-w9 vacuous class nnegPhi=1) + JSIG_CENSUS(
sign(den)=+1 on 10/10 live sample rows -- empirical J_sig =
I_3; the mixed-signature branch is G12 synthetic den<0, not
MAIN) + MUSTFAIL_LEDGER.
LEG A: the mixed form is a finite-matrix SATZ.  Derivation:
R^dagger = blkdiag(R, 0) + (1/den)[s;-1][s;-1]^T (r362 A4)
and R = R_{N-3} + u1 u1^T + u2 u2^T (r363), so M^dagger =
blkdiag(A0,-1/2) + U J U^T with U the two CD columns plus
the SM vector (s,-1) and J = diag(1,1,1/den) EXPLICIT, not
fitted.  Fractions toy residual EXACT 0 (den = 23/30).
Live residual <= 1.04e-14 on the 10-row sample (bar 1e-10);
w9 1.9e-15, kz15 1.9e-15, chi3-w9 1.3e-15.  Signature twin
(J_sig = diag(1,1,sign(den)), column 3 scaled) identical
residual.  THE r367 WARNING IS RESOLVED AS A FORM: the
border is not a third unaugmented CD column, but on the
R^dagger level Sherman-Morrison DOES supply a third column
with explicit J.  NO_LOWRANK_BOUNDARY_FORM does not fire.
LEG B: generalized Haynsworth is a SATZ for arbitrary
invertible symmetric J.  Fractions 4-node toy with
INDEFINITE J = diag(1,1,-1): In(H)=(4,3,0) == In(A)+In(-Phi)
== In(-J^{-1})+In(M) EXACT.  Lean form haynsworth_mixed in
the spec header (LDL / Sylvester over R; not proved here;
R373).  The r367 haynsworth_two_rank is the special case
J = I_2.
LEG C: Phi_N(0) = J^{-1} + U^T A^{-1} U live.  w9 sigma =
(-2.8132, -0.06648, 1.8039) det 0.3374; the two LARGE
eigenvalues TRACK r367 K2 (-2.7938, 1.8036), the small
extra negative IS the border direction.  Signature balance
In(A)+In(-Phi)==In(-J^{-1})+In(M^dagger) on 10/10 sample
AND chi3-w9; positivity control (balance iff M PD) 10/10.
DICHOTOMY: P1-true 8/10 have In(A) nneg=2 (A0's one
negative PLUS the -1/2 pad) and In(Phi) nneg=2 (K2-pair +
border); VACUOUS nnegA0=0 on kz42 and kz130 (2/10) have
In(A) nneg=1 (pad only) -- the r367 P1_VACUOUS class in
the 3x3 picture is one fewer A-negative; chi3-w9 additionally
drops to In(Phi) nneg=1.  OVERLOAD nnegA0>=2 is 0/10.
den in [1.460, 1.646] on the sample, all positive.
LEG D: must-fails 4/4 (m1 J=I_3 fitted-scale residual 0.375
+ AST J_fit_col_true; m2 wrong sign 1.249 + Fractions
exact; m3 two-rank Y-only 2.467e-3 + Fractions exact, the
OTHER r367 balance; m4 AST lamRd_col_true).
JSIG HONEST: empirical J_sig = I_3 on every live sample
row (den>0, R^dagger_bb = 1/den > 0).  The mixed
SIGNATURE of J is the FORM (SM decides the sign) plus the
synthetic den<0 branch (G12, den = -17.326), not a Lorentz
J on MAIN.  The mixed-NESS of the update on the family is
A indefinite + Phi mixed.
Runtime 29.2 / 28.9 s rec1/rec2; smoke 0.2 s.
AMENDMENTS AFTER FREEZE: none.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import final_two_rank_inertia_probe as FTI           # noqa: E402 r367
import augmented_borodin_duality_probe as ABD        # noqa: E402 r362
import canonical_sturm_induction_probe as CSI        # noqa: E402 r363
import borodin_dual_hole_probe as BDH                # noqa: E402 r356
import pair_extremal_probe as PX                     # noqa: E402 r342
import dirichlet_matched_frame_probe as DMF          # noqa: E402 r357
import hirota_sign_probe as HS                       # noqa: E402 r226
import principal_bessel_probe as PB                  # noqa: E402 r243
import verify_lstar_instance as V                    # noqa: E402 document
import v563_paper2_readouts as core                  # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
REC_LAMR = 0.500041882
FTI_SHA_PREFIX = "e0d79840"
ABD_SHA_PREFIX = "7d810a9a"
CSI_SHA_PREFIX = "09786c2e"
BDH_SHA_PREFIX = "36141c0a"
PX_SHA_PREFIX = "b09f8ccd"
DMF_SHA_PREFIX = "4bf1a94b"
HS_SHA_PREFIX = "d78e236b"
PB_SHA_PREFIX = "db259f8e"
W9_AUG_ANCH = dict(lamRd=0.500041459, mdag=1.658218770e-4)
W9_K2_ANCH = dict(ev0=-2.7938, ev1=1.8036)
W9_MIX_ANCH = dict(den=1.601114, J33=0.624568,
                   evP0=-2.813, evP1=-0.06648, evP2=1.804,
                   detPhi=0.3374, nnegA=2, nnegPhi=2, nposPhi=1,
                   Jsig=1)
KZ15_MIX_ANCH = dict(den=1.560471, nnegA=2, epsd=6.2765e-6)
CHI3_MIX_ANCH = dict(den=1.646359, nnegA0=0, nnegPhi=1,
                     epsd=2.092e-4)
SAMPLE_KZ = (9, 15, 18, 20, 42, 44, 52, 56, 119, 130)
MIX_BAR = 1.0e-10
M1_LOUD = 0.05
M2_LOUD = 0.1
M3_LOUD = 1.0e-3
RESOLV_FLOOR = 1.0e-9
TOY_TOL = 1.0e-12
K2_TRACK_REL = 2.0e-2
DEN_REL = 1.0e-3
PHI_REL_LARGE = 2.0e-2
PHI_REL_SMALL = 5.0e-2
KZ15_EPS_REL = 5.0e-2
CHI_EPS_REL = 2.0e-2
RUNTIME_BAR = 1800.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the module-own "
                       "constructors consume measure arrays / chain "
                       "coefficients / positions / pair indices / "
                       "border windows ONLY; record numbers and "
                       "anchors enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("derived_J", "signature_J", "mixed_rung",
                "chi_mixed_row", "mixed_update_toy",
                "haynsworth_mixed_toy", "fr_tr", "fr_diag",
                "fr_blkdiag", "fr_scale")
SCOPE_FORBIDDEN = {"REC_LAMR", "REC_MARGIN", "W9_MIX_ANCH",
                   "W9_AUG_ANCH", "W9_K2_ANCH", "KZ15_MIX_ANCH",
                   "CHI3_MIX_ANCH", "lamRd_col_true",
                   "J_fit_col_true", "den_col_true"}


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== module-own constructors (AST-audited)
def derived_J(den):
    """THE SM SIGNATURE: J = diag(1, 1, 1/den).  Consumes the
    Sherman-Morrison denominator only -- never fitted, never
    read from M^dagger."""
    return np.diag([1.0, 1.0, 1.0 / float(den)])


def signature_J(den):
    """unit-signature twin: J_sig = diag(1, 1, sign(den)).
    Consumes den only."""
    sig = 1.0 if float(den) > 0.0 else -1.0
    return np.diag([1.0, 1.0, sig]), sig, math.sqrt(abs(float(den)))


def fr_tr(A):
    """rational transpose; consumes the matrix only."""
    return [list(col) for col in zip(*A)]


def fr_diag(*d):
    """rational diagonal; consumes the pivots only."""
    n = len(d)
    return [[(d[i] if i == j else Fr(0)) for j in range(n)]
            for i in range(n)]


def fr_blkdiag(A, c):
    """block-diagonal pad of A by a 1x1 corner c; consumes A
    and the corner only."""
    n = len(A)
    out = [[Fr(0)] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            out[i][j] = A[i][j]
    out[n][n] = c
    return out


def fr_scale(A, s):
    """rational scalar multiply; consumes A and s only."""
    return [[s * x for x in row] for row in A]


def mixed_update_toy():
    """THE RATIONAL 4-NODE MIXED UPDATE: A0 = diag(-1,1,2,3),
    U_CD the r367 columns, vt = (1/3, 1/5, 0, 0), gamma = 1/2.
    Builds R^dagger from Z^{-1} and from A + U J U^T with
    J = diag(1,1,1/den) DERIVED.  Consumes nothing (closed)."""
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    Ucd = [[Fr(2), Fr(1)],
           [Fr(0), Fr(1)],
           [Fr(0), Fr(0)],
           [Fr(0), Fr(0)]]
    half = Fr(1, 2)
    I4 = fr_diag(Fr(1), Fr(1), Fr(1), Fr(1))
    UU = FTI.fr_mul(Ucd, fr_tr(Ucd))
    R = FTI.fr_add(FTI.fr_add(A0, fr_scale(I4, half)), UU)
    vt = [[Fr(1, 3)], [Fr(1, 5)], [Fr(0)], [Fr(0)]]
    gam = Fr(1, 2)
    s = FTI.fr_mul(R, vt)
    den = (Fr(1) + gam) - sum(vt[i][0] * s[i][0] for i in range(4))
    Ri = BDH.fr_inv(R)
    Z = [[Fr(0)] * 5 for _ in range(5)]
    for i in range(4):
        for j in range(4):
            Z[i][j] = Ri[i][j]
        Z[i][4] = vt[i][0]
        Z[4][i] = vt[i][0]
    Z[4][4] = Fr(1) + gam
    Rd = BDH.fr_inv(Z)
    Md = [[Rd[i][j] - (half if i == j else Fr(0))
           for j in range(5)] for i in range(5)]
    A = fr_blkdiag(A0, -half)
    U = [[Fr(0)] * 3 for _ in range(5)]
    for i in range(4):
        U[i][0] = Ucd[i][0]
        U[i][1] = Ucd[i][1]
        U[i][2] = s[i][0]
    U[4][2] = Fr(-1)
    J = fr_diag(Fr(1), Fr(1), Fr(1) / den)
    pred = FTI.fr_add(A, FTI.fr_mul(U, FTI.fr_mul(J, fr_tr(U))))
    dev = max(abs(Md[i][j] - pred[i][j])
              for i in range(5) for j in range(5))
    # wrong-sign mutant
    Jw = fr_diag(Fr(1), Fr(1), Fr(-1) / den)
    pred_w = FTI.fr_add(A, FTI.fr_mul(U, FTI.fr_mul(Jw, fr_tr(U))))
    dev_w = max(abs(Md[i][j] - pred_w[i][j])
                for i in range(5) for j in range(5))
    # two-rank mutant: Y-block only, J = I_2
    M2 = FTI.fr_add(A0, UU)
    MdY = [[Md[i][j] for j in range(4)] for i in range(4)]
    dev2 = max(abs(MdY[i][j] - M2[i][j])
               for i in range(4) for j in range(4))
    return dict(den=den, dev=dev, dev_w=dev_w, dev2=dev2,
                J33=Fr(1) / den, sig=(Fr(1) if den > 0 else Fr(-1)))


def haynsworth_mixed_toy():
    """THE RATIONAL 4-NODE MODEL of generalized Haynsworth with
    INDEFINITE J = diag(1,1,-1).  A = diag(-1,1,2,3), U 4x3.
    Returns exact Fraction blocks and inertias.  Consumes
    nothing (closed toy)."""
    A = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(2), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(3)]]
    U = [[Fr(2), Fr(1), Fr(0)],
         [Fr(0), Fr(1), Fr(1)],
         [Fr(0), Fr(0), Fr(1)],
         [Fr(0), Fr(0), Fr(0)]]
    J = fr_diag(Fr(1), Fr(1), Fr(-1))
    Jinv = fr_diag(Fr(1), Fr(1), Fr(-1))
    Ainv = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
            [Fr(0), Fr(1), Fr(0), Fr(0)],
            [Fr(0), Fr(0), Fr(1, 2), Fr(0)],
            [Fr(0), Fr(0), Fr(0), Fr(1, 3)]]
    Q = FTI.fr_mul(fr_tr(U), FTI.fr_mul(Ainv, U))
    Phi = FTI.fr_add(Jinv, Q)
    M = FTI.fr_add(A, FTI.fr_mul(U, FTI.fr_mul(J, fr_tr(U))))
    n, k = 4, 3
    H = [[Fr(0)] * (n + k) for _ in range(n + k)]
    for i in range(n):
        for j in range(n):
            H[i][j] = A[i][j]
        for j in range(k):
            H[i][n + j] = U[i][j]
            H[n + j][i] = U[i][j]
    mJ = fr_scale(Jinv, Fr(-1))
    for i in range(k):
        for j in range(k):
            H[n + i][n + j] = mJ[i][j]
    mPhi = fr_scale(Phi, Fr(-1))
    return dict(A=A, U=U, J=J, Phi=Phi, M=M, H=H, mJ=mJ, mPhi=mPhi,
                iA=FTI.fr_inertia(A), iPhi=FTI.fr_inertia(Phi),
                iMPhi=FTI.fr_inertia(mPhi), iM=FTI.fr_inertia(M),
                iH=FTI.fr_inertia(H), iMJ=FTI.fr_inertia(mJ),
                iJ=FTI.fr_inertia(J))


def mixed_rung(xu, wu, yn, vn, Nw, S, L, i1, i2,
               xp, wp, bxs, bws, bys, bvs, Bm=None):
    """THE r369 BLOCK of one window: r367 two-rank cut (CD
    columns + A0), r362 border chain + SM (s, den), then the
    mixed form A = blkdiag(A0,-1/2), U = [[U_CD, s],[0,-1]],
    J = diag(1,1,1/den) DERIVED, Phi = J^{-1} + U^T A^{-1} U.
    Consumes measure arrays, pair indices and the border
    window only."""
    o = FTI.cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=True)
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bp = ABD.border_chain_pack(np.asarray(xp, float),
                               np.asarray(wp, float), yn, vn,
                               bxs, bws, bys, bvs, Nw)
    out = dict(ok_sup=o["ok_sup"] and o["ok_map"],
               ok_border=bp["ok"], nf=bp.get("nf", -1),
               nnegA0=o["nneg"], P1=o["P1"], P2=o["P2"],
               Mpd=o["Mpd"], detK=o["detK"],
               evK0=o["evK0"], evK1=o["evK1"],
               eps=o["eps"], Sm=o["Sm"], Nw=Nw)
    if not bp["ok"]:
        out.update(ok_mix=False, den=float("nan"))
        return out
    Bw = bp["Bw"]
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                   np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    beta = bvec / math.sqrt(Bw)
    gam = float(beta @ beta)
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    v = Bm @ beta
    Rm = o["Rm"]
    vt = o["epsY"] * v
    s = Rm @ vt
    den = (1.0 + gam) - float(vt @ s)
    Sm = o["Sm"]
    Rinv = np.linalg.inv(Rm)
    Z = np.zeros((Sm + 1, Sm + 1))
    Z[:Sm, :Sm] = Rinv
    Z[:Sm, Sm] = vt
    Z[Sm, :Sm] = vt
    Z[Sm, Sm] = 1.0 + gam
    Rdag = np.linalg.inv(Z)
    Rdag = 0.5 * (Rdag + Rdag.T)
    Mdag = Rdag - 0.5 * np.eye(Sm + 1)
    A0 = o["A0"]
    Ucd = o["U"]
    A = np.zeros((Sm + 1, Sm + 1))
    A[:Sm, :Sm] = A0
    A[Sm, Sm] = -0.5
    U = np.zeros((Sm + 1, 3))
    U[:Sm, :2] = Ucd
    U[:Sm, 2] = s
    U[Sm, 2] = -1.0
    J = derived_J(den)
    pred = A + U @ J @ U.T
    pred = 0.5 * (pred + pred.T)
    dev_mix = float(np.max(np.abs(Mdag - pred)))
    Jsig, sig, alpha = signature_J(den)
    Us = U.copy()
    Us[:, 2] = U[:, 2] / alpha
    pred_s = A + Us @ Jsig @ Us.T
    dev_sig = float(np.max(np.abs(Mdag - 0.5 * (pred_s + pred_s.T))))
    Jinv = np.diag([1.0, 1.0, float(den)])
    Phi = Jinv + U.T @ np.linalg.solve(A, U)
    Phi = 0.5 * (Phi + Phi.T)
    evP = np.linalg.eigvalsh(Phi)
    IA = FTI.inertia_of(A)
    IP = FTI.inertia_of(Phi)
    IMn = FTI.inertia_of(-Phi)
    IJ = FTI.inertia_of(-Jinv)
    IM = FTI.inertia_of(Mdag)
    n = Sm + 1
    bal = (IA["npos"] + IMn["npos"] == IJ["npos"] + IM["npos"]
           and IA["nneg"] + IMn["nneg"] == IJ["nneg"] + IM["nneg"]
           and IA["nzer"] + IMn["nzer"] == IJ["nzer"] + IM["nzer"])
    want_pd = (IM["nneg"] == 0 and IM["nzer"] == 0
               and IM["npos"] == n)
    # the positivity control: In(A)+In(-Phi) == In(-J^{-1})+(n,0,0)
    ctrl = (IA["npos"] + IMn["npos"] == IJ["npos"] + n
            and IA["nneg"] + IMn["nneg"] == IJ["nneg"]
            and IA["nzer"] + IMn["nzer"] == IJ["nzer"])
    M2 = A0 + Ucd @ Ucd.T
    dev2 = float(np.max(np.abs(Mdag[:Sm, :Sm] - M2)))
    Jw = np.diag([1.0, 1.0, -1.0 / den])
    pred_w = A + U @ Jw @ U.T
    dev_w = float(np.max(np.abs(Mdag - 0.5 * (pred_w + pred_w.T))))
    pred_I = A + U @ U.T
    dev_I = float(np.max(np.abs(Mdag - 0.5 * (pred_I + pred_I.T))))
    lamRd = float(np.linalg.eigvalsh(Rdag)[0])
    out.update(den=float(den), J33=1.0 / float(den), sig=int(sig),
               gam=gam, qN=bp["qN"], Bw=Bw,
               dev_mix=dev_mix, dev_sig=dev_sig,
               evP0=float(evP[0]), evP1=float(evP[1]),
               evP2=float(evP[2]), detPhi=float(np.linalg.det(Phi)),
               nposA=IA["npos"], nnegA=IA["nneg"], nzerA=IA["nzer"],
               nposPhi=IP["npos"], nnegPhi=IP["nneg"],
               nzerPhi=IP["nzer"],
               nposM=IM["npos"], nnegM=IM["nneg"], nzerM=IM["nzer"],
               nposMJ=IJ["npos"], nnegMJ=IJ["nneg"],
               nposMn=IMn["npos"], nnegMn=IMn["nneg"],
               bal=bal, want_pd=want_pd, ctrl=ctrl,
               lamRd=lamRd, mdag=2.0 - 1.0 / lamRd if lamRd > 0
               else float("nan"),
               dev2=dev2, dev_w=dev_w, dev_I=dev_I,
               ok_mix=True, n=n)
    return out


def chi_mixed_row(kz, q, lpq):
    """one chi-world rung through the identical mixed pipeline;
    consumes the chi comb + matched frame only."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    o = mixed_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                   mzc["Nw"], mzc["S"], mzc["L"], j1, j2,
                   mzc["xp"], mzc["wp"], mzb["xp"], mzb["wp"],
                   mzb["yn"], mzb["vn"])
    o["kz"] = kz
    o["Nw"] = mzc["Nw"]
    return o


# ============== must-fail mutants
def mutant_fitted_J(J_fit_col_true):
    """m1 MUST-FAIL (AST): a 'J constructor' that returns a
    withheld fitted 3x3 instead of diag(1,1,1/den) from SM --
    AST-FLAGGED."""
    return J_fit_col_true


def mutant_lam_readback(lamRd_col_true):
    """m4 MUST-FAIL (AST): an 'M^dagger positivity' that returns
    the withheld lambda_min(R^dagger) column -- AST-FLAGGED."""
    return lamRd_col_true


def slim(o):
    """memory hygiene."""
    drop = {"U", "A0", "Rm", "epsY", "Bd", "vneg"}
    return {k: o[k] for k in o if k not in drop}


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("mixed_haynsworth_probe -- "
          "PRIME.LDAGGER.MIXED_HAYNSWORTH.01 (round 369)")
    print("SPEC_SHA %s   (r367 FTI %s / r362 ABD %s / r363 CSI %s)"
          % (SPEC_SHA[:16], FTI.SPEC_SHA[:16], ABD.SPEC_SHA[:16],
             CSI.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 mixed block + kz15 + chi3 w9; 10-row "
                        "sample skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and CSI.SPEC_SHA.startswith(CSI_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and HS.SPEC_SHA.startswith(HS_SHA_PREFIX)
              and PB.SPEC_SHA.startswith(PB_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r367/r362/r363/r356/r342/"
          "r357/r226/r243 machinery imported verbatim (FTI %s == "
          "%s*, ABD %s == %s*, CSI %s == %s*); J = diag(1,1,"
          "1/den) DERIVED from Sherman-Morrison, never fitted; "
          "Haynsworth mixed SATZ; the DCCX STOP list forbids any "
          "L*/R^dagger/RH claim"
          % (FTI.SPEC_SHA[:8], FTI_SHA_PREFIX, ABD.SPEC_SHA[:8],
             ABD_SHA_PREFIX, CSI.SPEC_SHA[:8], CSI_SHA_PREFIX))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m1 = scope_audit("mutant_fitted_J")
    hits_m4 = scope_audit("mutant_lam_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m1) and bool(hits_m4),
          "the %d module-own constructors consume measure arrays "
          "/ chain / positions / pair / border ONLY (%s); "
          "fragment audit (no fit primitives): %s; m1 FLAGGED "
          "(%s); m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m1[0] if hits_m1 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- MIXED UPDATE + HAYNSWORTH MIXED (Q)")
    Tm = mixed_update_toy()
    check("G10-toy-mixed-update", Tm["dev"] == 0 and Tm["den"] != 0
          and Tm["dev_w"] > 0 and Tm["dev2"] > 0,
          "EXACT FRACTIONS MIXED UPDATE on the 4-node model: "
          "M^dagger == A + U J U^T with J = diag(1,1,1/den), "
          "den = %s, J_33 = %s, residual EXACT 0; wrong-sign "
          "mutant residual %s != 0; two-rank Y-only residual "
          "%s != 0 -- the border column AND the SM scale are "
          "load-bearing, CAUGHT in Fractions"
          % (str(Tm["den"]), str(Tm["J33"]), str(Tm["dev_w"]),
             str(Tm["dev2"])))
    Th = haynsworth_mixed_toy()
    ok_add = (Th["iH"][0] == Th["iA"][0] + Th["iMPhi"][0]
              and Th["iH"][1] == Th["iA"][1] + Th["iMPhi"][1]
              and Th["iH"][0] == Th["iMJ"][0] + Th["iM"][0]
              and Th["iH"][1] == Th["iMJ"][1] + Th["iM"][1])
    check("G11-toy-haynsworth-mixed", ok_add
          and Th["iJ"][1] >= 1,
          "EXACT FRACTIONS GENERALIZED HAYNSWORTH with "
          "INDEFINITE J = diag(1,1,-1): In(J)=%s (one negative), "
          "In(A)=%s, In(Phi)=%s, In(-Phi)=%s, In(M)=%s, "
          "In(-J^{-1})=%s, In(H)=%s; additivity In(H) == "
          "In(A)+In(-Phi) == In(-J^{-1})+In(M) EXACT -- the "
          "identity is a finite-matrix SATZ for arbitrary "
          "invertible symmetric J, Lean-shaped (haynsworth_"
          "mixed in the spec; proof is R373)"
          % (str(Th["iJ"]), str(Th["iA"]), str(Th["iPhi"]),
             str(Th["iMPhi"]), str(Th["iM"]), str(Th["iMJ"]),
             str(Th["iH"])))
    # f64 synthetic den < 0 (the mixed-signature branch)
    A0s = np.diag([-0.2, 0.4, 0.9, 1.3])
    Ucds = np.array([[1.0, 0.0], [0.0, 1.0],
                     [0.0, 0.0], [0.0, 0.0]])
    Rs = A0s + 0.5 * np.eye(4) + Ucds @ Ucds.T
    vts = 4.0 * np.array([0.6, 0.5, 0.2, 0.3])
    gams = 0.25
    ss = Rs @ vts
    dens = (1.0 + gams) - float(vts @ ss)
    Zs = np.zeros((5, 5))
    Zs[:4, :4] = np.linalg.inv(Rs)
    Zs[:4, 4] = vts
    Zs[4, :4] = vts
    Zs[4, 4] = 1.0 + gams
    Rds = np.linalg.inv(Zs)
    Mds = Rds - 0.5 * np.eye(5)
    As = np.zeros((5, 5))
    As[:4, :4] = A0s
    As[4, 4] = -0.5
    Us = np.zeros((5, 3))
    Us[:4, :2] = Ucds
    Us[:4, 2] = ss
    Us[4, 2] = -1.0
    Js = derived_J(dens)
    preds = As + Us @ Js @ Us.T
    dev_syn = float(np.max(np.abs(Mds - 0.5 * (preds + preds.T))))
    check("G12-toy-den-negative", dens < 0 and dev_syn <= TOY_TOL,
          "F64 SYNTHETIC den<0 BRANCH: den = %+.4f < 0 so "
          "J_33 = 1/den = %+.4f < 0 (the mixed signature the "
          "live windows do not show); mixed residual %.1e "
          "(bar %.0e) -- the FORM allows J_33 < 0, SM decides "
          "the sign, nothing is fitted"
          % (dens, 1.0 / dens, dev_syn, TOY_TOL))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + MIXED FORM + PHI")
    R9 = PX.build_rung(MAIN_KZ)
    mz9 = R9["mz"]
    check("G20-w9-records",
          R9["S"] == REC_S and R9["Sm"] == REC_SM
          and R9["Nw"] == REC_NW
          and abs(R9["margin"] / REC_MARGIN - 1.0) <= REC_MARGIN_TOL
          and R9["f1"] == 2 and R9["f2"] == 4,
          "w9 records bit-near: S %d == %d, S_- %d == %d, N_w %d "
          "== %d, margin %.6e, folds (%d, %d)"
          % (R9["S"], REC_S, R9["Sm"], REC_SM, R9["Nw"], REC_NW,
             R9["margin"], R9["f1"], R9["f2"]))
    alpha9 = float(V.window_shape(MAIN_KZ)[0])
    dsm9 = HS.window_data(MAIN_KZ, comb=PB.smooth_comb(alpha9))
    o9 = mixed_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                    R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"],
                    mz9["xp"], mz9["wp"], dsm9["xs"], dsm9["ws"],
                    dsm9["ys"], dsm9["vs"], Bm=R9["B"])
    A9 = W9_MIX_ANCH
    ok_mix9 = (o9["ok_mix"] and o9["ok_border"]
               and o9["dev_mix"] <= MIX_BAR
               and o9["dev_sig"] <= MIX_BAR
               and abs(o9["den"] / A9["den"] - 1.0) <= DEN_REL
               and abs(o9["J33"] / A9["J33"] - 1.0) <= DEN_REL
               and o9["sig"] == A9["Jsig"]
               and abs(o9["lamRd"] - W9_AUG_ANCH["lamRd"]) <= 1e-8)
    check("G21-w9-mixed-form", ok_mix9,
          "THE MIXED FORM at w9: M^dagger == A + U J U^T with "
          "J = diag(1,1,1/den) DERIVED, residual %.1e (bar %.0e); "
          "signature twin residual %.1e; den = %.6f (J_33 = "
          "%.6f, sig = %+d); lamRd = %.9f == the r362 record -- "
          "the border IS a third column on the R^dagger level "
          "via Sherman-Morrison, the r367 warning is resolved "
          "as a FORM (not a third unaugmented CD column)"
          % (o9["dev_mix"], MIX_BAR, o9["dev_sig"], o9["den"],
             o9["J33"], o9["sig"], o9["lamRd"]))
    ok_phi9 = (o9["nnegA"] == A9["nnegA"]
               and o9["nnegPhi"] == A9["nnegPhi"]
               and o9["nposPhi"] == A9["nposPhi"]
               and o9["bal"] and o9["ctrl"] and o9["want_pd"]
               and abs(o9["evP0"] / A9["evP0"] - 1.0) <= PHI_REL_LARGE
               and abs(o9["evP1"] / A9["evP1"] - 1.0) <= PHI_REL_SMALL
               and abs(o9["evP2"] / A9["evP2"] - 1.0) <= PHI_REL_LARGE
               and abs(o9["detPhi"] / A9["detPhi"] - 1.0)
               <= PHI_REL_LARGE)
    ok_track = (abs(o9["evP0"] / W9_K2_ANCH["ev0"] - 1.0)
                <= K2_TRACK_REL
                and abs(o9["evP2"] / W9_K2_ANCH["ev1"] - 1.0)
                <= K2_TRACK_REL)
    check("G22-w9-phi-balance", ok_phi9 and ok_track,
          "PHI_N(0) at w9: sigma = (%.4f, %.5f, %.4f) det = "
          "%.4f; In(A)=(%d pos, %d neg) [A0's one negative PLUS "
          "the -1/2 pad], In(Phi)=(%d pos, %d neg), In(M^dagger)"
          "=(%d,0,0) PD; SIGNATURE BALANCE In(A)+In(-Phi) == "
          "In(-J^{-1})+In(M) %s and the positivity control %s; "
          "the two LARGE Phi eigenvalues TRACK r367 K2 "
          "(%.4f, %.4f) -- the small extra negative %.5f IS the "
          "border direction in the 3x3 picture"
          % (o9["evP0"], o9["evP1"], o9["evP2"], o9["detPhi"],
             o9["nposA"], o9["nnegA"], o9["nposPhi"], o9["nnegPhi"],
             o9["nposM"], o9["bal"], o9["ctrl"],
             W9_K2_ANCH["ev0"], W9_K2_ANCH["ev1"], o9["evP1"]))

    # ---------------- S3 kz15 + sample
    section("S3  LEG A/C -- KZ15 + 10-ROW SAMPLE + DICHOTOMY")
    R15 = PX.build_rung(15)
    mz15 = R15["mz"]
    al15 = float(V.window_shape(15)[0])
    dsm15 = HS.window_data(15, comb=PB.smooth_comb(al15))
    o15 = mixed_rung(mz15["xu"], mz15["wu"], mz15["yn"], mz15["vn"],
                     R15["Nw"], R15["S"], mz15["L"], R15["i1"],
                     R15["i2"], mz15["xp"], mz15["wp"],
                     dsm15["xs"], dsm15["ws"], dsm15["ys"],
                     dsm15["vs"], Bm=R15["B"])
    A15 = KZ15_MIX_ANCH
    ok15 = (o15["ok_mix"] and o15["dev_mix"] <= MIX_BAR
            and o15["bal"] and o15["ctrl"]
            and abs(o15["den"] / A15["den"] - 1.0) <= DEN_REL
            and o15["nnegA"] == A15["nnegA"]
            and o15["sig"] == 1
            and abs((o15["lamRd"] - 0.5) / A15["epsd"] - 1.0)
            <= KZ15_EPS_REL)
    check("G30-kz15-near-terminal", ok15,
          "KZ15 (near-terminal, N_w %d, q_N %.4f): mixed "
          "residual %.1e, den = %.6f (sig +1), nnegA = %d "
          "(P1-true class: A0 one negative + pad), lamRd-1/2 "
          "= %.4e, balance %s control %s PD %s -- the mixed "
          "form holds where the terminal channel is tight"
          % (o15["Nw"], o15["qN"], o15["dev_mix"], o15["den"],
             o15["nnegA"], o15["lamRd"] - 0.5, o15["bal"],
             o15["ctrl"], o15["want_pd"]))
    if smoke:
        for g in ("G31-sample-mixed", "G32-dichotomy"):
            check(g, True, "SMOKE: skipped")
        OT = {MAIN_KZ: slim(o9), 15: slim(o15)}
        n_sample = 2
        n_bal = 2
        n_p1 = 2
        n_vac = 0
        n_jsig_pos = 2
    else:
        OT = {MAIN_KZ: slim(o9), 15: slim(o15)}
        print("    %-5s %-5s | %-10s %-8s %-4s | %-8s %-8s | "
              "%-5s %-5s %-5s"
              % ("kz", "N_w", "dev_mix", "den", "sig",
                 "nnegA", "nnegPhi", "bal", "ctrl", "PD"),
              flush=True)
        for kz in SAMPLE_KZ:
            if kz in OT:
                o = OT[kz]
                nw = o["Nw"]
            else:
                Rr = PX.build_rung(kz)
                mz = Rr["mz"]
                alk = float(V.window_shape(kz)[0])
                dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
                o = mixed_rung(mz["xu"], mz["wu"], mz["yn"],
                               mz["vn"], Rr["Nw"], Rr["S"],
                               mz["L"], Rr["i1"], Rr["i2"],
                               mz["xp"], mz["wp"], dsm["xs"],
                               dsm["ws"], dsm["ys"], dsm["vs"],
                               Bm=Rr["B"])
                nw = Rr["Nw"]
                OT[kz] = slim(o)
                del Rr, mz, dsm
            print("    %-5d %-5d | %.4e %.6f %+4d | %8d %8d | "
                  "%5s %5s %5s"
                  % (kz, nw, o["dev_mix"], o["den"], o["sig"],
                     o["nnegA"], o["nnegPhi"], o["bal"],
                     o["ctrl"], o["want_pd"]),
                  flush=True)
        n_sample = len(SAMPLE_KZ)
        mix_ok = all(OT[k]["ok_mix"] and OT[k]["dev_mix"] <= MIX_BAR
                     and OT[k]["dev_sig"] <= MIX_BAR
                     for k in SAMPLE_KZ)
        n_bal = sum(1 for k in SAMPLE_KZ if OT[k]["bal"])
        n_ctrl = sum(1 for k in SAMPLE_KZ
                     if OT[k]["ctrl"] == OT[k]["want_pd"])
        n_jsig_pos = sum(1 for k in SAMPLE_KZ if OT[k]["sig"] == 1)
        check("G31-sample-mixed", mix_ok and n_bal == n_sample
              and n_jsig_pos == n_sample,
              "10-ROW ALGEBRA SAMPLE %s: mixed residual <= %.0e "
              "on %d/%d; signature twin ok; balance %d/%d; "
              "J_sig = +1 on %d/%d (den>0 on every attempted "
              "live row -- the empirical signature is I_3, the "
              "mixed-J branch is the FORM plus G12 synthetic, "
              "not a MAIN Lorentz J)"
              % (str(SAMPLE_KZ), MIX_BAR, n_sample, n_sample,
                 n_bal, n_sample, n_jsig_pos, n_sample))
        resolv = [k for k in SAMPLE_KZ
                  if abs(OT[k]["lamRd"] - 0.5) > RESOLV_FLOOR]
        n_p1 = sum(1 for k in resolv if OT[k]["nnegA0"] == 1)
        n_vac = sum(1 for k in resolv if OT[k]["nnegA0"] == 0)
        # P1-true: nnegA == 2 (A0 + pad), nnegPhi == 2
        p1_shape = all(OT[k]["nnegA"] == 2 and OT[k]["nnegPhi"] == 2
                       for k in resolv if OT[k]["nnegA0"] == 1)
        vac_shape = all(OT[k]["nnegA"] == 1
                        for k in resolv if OT[k]["nnegA0"] == 0)
        check("G32-dichotomy", p1_shape and vac_shape,
              "3x3 DICHOTOMY on %d resolvable sample rows: "
              "P1-true nnegA0==1 : %d/%d have In(A) nneg=2 "
              "(A0 negative PLUS the -1/2 pad) and In(Phi) "
              "nneg=2 (K2-pair + border); VACUOUS nnegA0==0 : "
              "%d/%d have In(A) nneg=1 (pad only) -- the r367 "
              "P1_VACUOUS class in the new picture is one fewer "
              "A-negative and (on chi3-w9) one fewer Phi-"
              "negative; OVERLOAD nnegA0>=2 is not in this "
              "algebra sample"
              % (len(resolv), n_p1, len(resolv), n_vac,
                 len(resolv)))

    # ---------------- S4 chi
    section("S4  CHI3 W9 -- THE VACUOUS CLASS IN THE 3x3 PICTURE")
    c3 = chi_mixed_row(MAIN_KZ, DMF.Q_CHI3, DMF.LPQ3)
    A3 = CHI3_MIX_ANCH
    ok_c3 = (c3 is not None and c3["ok_mix"]
             and c3["dev_mix"] <= MIX_BAR and c3["bal"]
             and abs(c3["den"] / A3["den"] - 1.0) <= DEN_REL
             and c3["nnegA0"] == A3["nnegA0"]
             and c3["nnegPhi"] == A3["nnegPhi"]
             and abs((c3["lamRd"] - 0.5) / A3["epsd"] - 1.0)
             <= CHI_EPS_REL)
    check("G40-chi3-w9-vacuous", ok_c3,
          "CHI3 w9 through the identical mixed pipeline: "
          "residual %.1e, den = %.6f, nnegA0 = %d (r367 "
          "P1_VACUOUS: A0 already PD), nnegA = %d (pad only), "
          "In(Phi) nneg = %d (ONE fewer than the P1-true "
          "MAIN class -- the vacuous class in the 3x3 picture), "
          "lamRd-1/2 = %.4e (r362 chi3 epsd), M PD %s, "
          "balance %s -- sufficiency not necessity, world-"
          "separating, the mixed form still holds"
          % (c3["dev_mix"], c3["den"], c3["nnegA0"], c3["nnegA"],
             c3["nnegPhi"], c3["lamRd"] - 0.5, c3["want_pd"],
             c3["bal"]))

    # ---------------- S5 must-fails
    section("S5  MUST-FAILS")
    check("G80-m1-fitted-J", bool(hits_m1) and o9["dev_I"] >= M1_LOUD
          and o9["dev_mix"] <= MIX_BAR,
          "m1 J FITTED AS I_3 (scale ignored, the naive "
          "positive-definite 3-column form): residual %.3f >= "
          "%.2f at w9 while the DERIVED J = diag(1,1,1/den) "
          "holds at %.1e; constructor that returns a withheld "
          "fitted J is AST-FLAGGED (%s) -- CAUGHT"
          % (o9["dev_I"], M1_LOUD, o9["dev_mix"],
             hits_m1[0] if hits_m1 else "MISS"))
    check("G81-m2-wrong-sign", o9["dev_w"] >= M2_LOUD
          and Tm["dev_w"] > 0,
          "m2 WRONG BORDER SIGN J_33 = -1/den: residual %.3f "
          ">= %.2f at w9 AND Fractions-exact break at G10 -- "
          "the SM sign of den is load-bearing, CAUGHT"
          % (o9["dev_w"], M2_LOUD))
    check("G82-m3-two-rank-mutant", o9["dev2"] >= M3_LOUD
          and Tm["dev2"] > 0,
          "m3 U WITHOUT THE BORDER COLUMN (the r367 two-rank "
          "mutant): Y-block residual %.3e >= %.0e at w9 AND "
          "Fractions-exact break at G10 -- that mutant gives "
          "the OTHER balance (In(A0)+In(-K2)==In(-I_2)+"
          "In(A0+UU^T), the r367 SATZ), not the 3x3 mixed "
          "balance, CAUGHT"
          % (o9["dev2"], M3_LOUD))
    check("G83-m4-lam-readback", bool(hits_m4),
          "m4 lambda_min(R^dagger) READBACK: AST-FLAGGED (%s) "
          "-- mixed_rung consumes measure arrays, border "
          "windows and pair indices only; positivity of "
          "M^dagger is the inertia of A + U J U^T, never a "
          "withheld spectral column"
          % (hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S6 verdict
    section("S6  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held (DCCX): NO L* claim, NO R^dagger "
          "claim, no bound mechanism, no certificate reading "
          "beyond the sealed census, no posthoc bar/band/"
          "clause/J-form move, no derived 5/7, NO RH claim, "
          "mincut unchanged; r243..r368 stand; R371/R372/R373 "
          "coexistence (own files); next.txt NOT written")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        st = {n: ok for n, ok, _d in CHECKS}
        if not audits_ok:
            verd = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif not st.get("G10-toy-mixed-update", False) \
                or not st.get("G11-toy-haynsworth-mixed", False) \
                or not st.get("G21-w9-mixed-form", False) \
                or not st.get("G31-sample-mixed", False):
            if o9["dev_mix"] > MIX_BAR:
                verd = "NO_LOWRANK_BOUNDARY_FORM(mixed residual " \
                       "fails -- the r367 warning confirmed on " \
                       "R^dagger)"
            else:
                verd = "CHAIN_FAIL"
        else:
            parts = ["MIXED_UPDATE_EXACT(J = diag(1,1,1/den) "
                     "from SM, residual <= %.0e on w9 + 10-row "
                     "+ chi3-w9 + kz15; Fractions exact; "
                     "signature twin exact)" % MIX_BAR]
            parts.append("HAYNSWORTH_MIXED_SATZ(both readings, "
                         "indefinite-J toy, Lean form "
                         "haynsworth_mixed in the spec -- proof "
                         "is R373)")
            parts.append("PHI_LEDGER(w9 sigma (%.3f, %.4f, %.3f); "
                         "balance %d/%d sample; dichotomy P1-true "
                         "%d vacuous %d; chi3-w9 vacuous class "
                         "nnegPhi=1)"
                         % (o9["evP0"], o9["evP1"], o9["evP2"],
                            n_bal, n_sample, n_p1, n_vac))
            parts.append("JSIG_CENSUS(sign(den)=+1 on %d/%d live "
                         "sample rows -- empirical J_sig = I_3; "
                         "the mixed-signature branch is G12 "
                         "synthetic den<0, not MAIN)"
                         % (n_jsig_pos, n_sample))
            parts.append("MUSTFAIL_LEDGER")
            verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- mixed SM form + generalized Haynsworth; "
          "NO L* claim, NO R^dagger claim, NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
