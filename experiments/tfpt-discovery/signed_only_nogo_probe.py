#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signed_only_nogo_probe -- PRIME.NOGO.SIGNED.ONLY.01.

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
from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
import sympy as sp
from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap                # noqa: E402  READ-ONLY
import shift_average_all_depth_probe as sad      # noqa: E402  READ-ONLY
import matrix_stage_conditioning_probe as msc    # noqa: E402  READ-ONLY

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []
DEVIATIONS: list[tuple[str, str, str]] = []

RUNTIME_BAR = 1800.0
AUDIT_TARGETS = (184, 405, 838)          # pick_cells keys; h = 184/388/839
REGISTERED_RUNGS = (184, 405)
N_THETA = 32
CTRL_THETA = tuple((k + 0.5) / 8.0 for k in range(8))
EF_THETA = 0.5 / N_THETA                 # frozen theta for the Weil readout
MP_DPS = 50
WARD_REL = 0.05                          # generic relative ward
U_RND = 0.5 * float(np.finfo(float).eps)

# frame ladder: (h, kz); h is a PREDICTION of the rebuild, not an input
FRAME_SPECS = ((184, 9), (388, 55), (839, 43), (1393, 88), (2015, 85),
               (2607, 131), (2854, 222), (5746, 273), (12632, 569))
PP_CAP = 200000

# classical constants (EXTERNAL-CITED, never re-proved here)           (X3)
PSI_CHEB = 1.03883
BT_CONST = 2.0
SCHOENFELD_DEN = 8.0 * math.pi
WIN_GRID = 8.0
N_PART = 512
GL_N = 24
GL_N_WARD = 8
GRADE_RATIO = 2.0
LAM_INFLATE = (1.02, 1.05, 1.15, 1.4, 2.0, 4.0, 16.0)
FHAT_XI_MAX = 4.0
FHAT_N = 257

# ---- cited numbers this probe must reproduce or explicitly disclose
WARD_FEJER_B = {184: "-1.2648057425013541047",
                388: "-1.3147508968858830784"}
WARD_THETA0 = ("-1.3721834192256655822329574974497422890145392516236")
WARD_R_STAR = ("6.1258715694998532087", "6.1258715695018532087")
WARD_LITTLEWOOD = {184: 2.1654551, 12632: 4.1231791}
WARD_SLACK_CITED = 2.7e-03                                            # (X2)
WARD_FRAME_REL = 2.098e-02
WARD_RH_SHORT = 108.885
WARD_RH_BLOCK = 64.9909
WARD_BETA_INV = {184: 7.26169e06, 388: 2.48510e08}
WARD_R_DEPLOYED = {184: 17.75980, 388: 60.49414}
WARD_GROWTH_ORDERS = (1.5343, 1.0646, 0.3253)
WARD_GROWTH_SHARES = (52.8, 36.6, 11.2)
WARD_GROWTH_TOTAL = 2.9061                                            # (X5)
WARD_S_MEAN = {184: 1.507357381e-1, 388: 9.991056578e-2, 839: 1.531626e-1}
WARD_EVEN_MEAN = {184: -2.303776, 388: -5.225658, 839: -4.956063}
WARD_ODD_MEAN = {184: 4.559958, 388: 10.29308, 839: 9.644332}
WARD_QC_MEAN = {184: 2.105446, 388: 4.967510, 839: 4.535107}
WARD_FLIP_WORST = -4.083267
WARD_VARIATIONAL_SLACK = 1.942126
WARD_U2_MISS = {184: 65.0, 388: 312.6, 839: 110.4}
WARD_SIGNED_BEST_MISS = {184: 7.93, 388: 14.91, 839: 8.44}
WARD_BAR = {184: -0.577, 388: -5.42, 839: -3.28}
WARD_FHAT_NEGFRAC = (0.30, 0.45)
WARD_CONE_FLOOR_EXP_MIN = 0.0
# cited certified Schur / witness reads (X1)
CITED_SCHUR = {184: ("2.55040492106466221e-06", "2.55040492106466306e-06"),
               388: ("1.22362650956722969e-07", "1.22362650956723022e-07"),
               839: ("1.05673858430073635e-08", "1.05673858430073668e-08"),
               1393: ("2.27451283174326270e-09", "2.27451283174326353e-09"),
               2015: ("1.29605297764620827e-09", "1.29605297764620869e-09"),
               2607: ("5.58561095567885030e-10", "5.58561095567885237e-10"),
               2854: ("2.12003444567896238e-10", "2.12003444567896289e-10")}
CITED_UPPER = {184: "2.55040492106466306e-06", 2854: "3.57242557243221179e-13",
               5746: "3.81272546102071277e-14",
               12632: "2.79579794131272506e-15"}
WARD_EXP_S = -3.42696317
WARD_EXP_S_D2 = -2.11200286
WARD_EXP_STEP_POS = 0.50303
WARD_EXP_U_GLOBAL = -3.21092510922176011
WARD_EXP_U_DEEP = -2.67942161302143633
WARD_COLLAPSE_BAR = -8.0
# CCCLXI / CCCLXII / CCCLXIII / CCCLXVII / CCCLXIX kernels
WARD_BN_CONST = 1.2606614015
WARD_BN_CB = 0.5523
WARD_BN_SIGMA_CAP = 0.726909
WARD_BN_SIGMA_RANGE = (0.4106, 0.4260)
WARD_LI_R = "1.05"
WARD_LI_RE_RHO = 0.51312503
WARD_LI_DENSITY = 0.333350
WARD_LI_MAXCOS = -0.500046
WARD_LI_MINLAM = 6.25185
WARD_LI_FIRSTNEG = 12
WARD_LI_NEGCOUNT = 9988
WARD_LI_BOHR = (3, 6, 1224)
WARD_LI_BL_CONST = 5413.4113
WARD_E2 = -0.905841347202

AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
    "tau", "target_sign", "cached_sign", "polyfit", "curve_fit",
    "lstsq", "least_squares",
}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""), flush=True)
    return ok


def disclose(tag, got, cited):
    DEVIATIONS.append((tag, got, cited))


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


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


def gam(k):
    return msc.gam(k)


def fsum(v):
    return msc.fsum(v)


def rel(a, b):
    b = float(b)
    return abs(float(a) - b) / max(abs(b), 1e-300)


def exponent(v_lo, v_hi, h_lo, h_hi):
    if v_lo <= 0 or v_hi <= 0:
        return float("nan")
    return math.log(v_hi / v_lo) / math.log(float(h_hi) / float(h_lo))


# ======================================================= S0  the instrument
def prime_power_list(cap):
    """Ordered prime powers >= 2 up to cap, from an independent sieve."""
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
    """von Mangoldt Lambda(n) for n <= n_max, independent sieve."""
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


# ================================================ archimedean profile Theta
def theta_mp(r):
    """Theta(r) = 1/(1/4 + r^2) + Re psi(1/4 + i r/2) - log pi."""
    r = mp.mpf(r)
    return (1 / (mp.mpf(1) / 4 + r ** 2)
            + mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, r) / 2))
            - mp.log(mp.pi))


def re_digamma_stirling(z, m_shift=40):
    """Independent Re psi(z): recurrence + Stirling asymptotic series."""
    z = mp.mpc(z)
    acc = mp.mpc(0)
    for j in range(m_shift):
        acc -= 1 / (z + j)
    w = z + m_shift
    bern = [mp.mpf(1) / 6, mp.mpf(-1) / 30, mp.mpf(1) / 42, mp.mpf(-1) / 30,
            mp.mpf(5) / 66, mp.mpf(-691) / 2730, mp.mpf(7) / 6]
    ser = mp.log(w) - 1 / (2 * w)
    for n, b_val in enumerate(bern, start=1):
        ser -= b_val / (2 * n * w ** (2 * n))
    return mp.re(acc + ser)


def theta_stirling(r):
    r = mp.mpf(r)
    return (1 / (mp.mpf(1) / 4 + r ** 2)
            + re_digamma_stirling(mp.mpf(1) / 4 + mp.mpc(0, r) / 2)
            - mp.log(mp.pi))


# ============================================= Fejer supply, three routes
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
    pole = pole_minus_pmain + p_main
    v_geo = 4 / s_len * (mp.exp(s_len / 2) - 1) - 1
    return dict(B=pole_minus_pmain + arch, pole=pole, arch=arch,
                p_main=p_main, V=v_geo)


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
    return dict(B=pole - p_main + arch, pole=pole, arch=arch, p_main=p_main)


def fejer_fourier(s_len, r_cap=mp.mpf("1e7")):
    """Third route: 2 pi B = int Fhat Theta with Fhat >= 0 and an
    explicit tail bound (|Theta(r)| <= log(r/2) + 2 for r >= 2,
    Fhat(r) <= 4/(S r^2))."""
    s_len = mp.mpf(s_len)

    def integrand(r):
        if r == 0:
            return s_len * theta_mp(0)
        return 2 * (1 - mp.cos(r * s_len)) / (s_len * r ** 2) * theta_mp(r)
    pts = [mp.mpf(0)]
    x = mp.mpf(1)
    while x < r_cap:
        pts.append(x)
        x *= 10
    pts.append(r_cap)
    val = 2 * mp.quad(integrand, pts) / (2 * mp.pi)
    tail_raw = 2 * (4 / s_len) * (mp.log(r_cap / 2) + 2) / r_cap
    tail = 2 * tail_raw / (2 * mp.pi)
    return val, tail


# ======================================== classical envelopes for the cone
def prime_count_up(a_lo, b_hi):
    """(C2) Montgomery-Vaughan Brun-Titchmarsh, with the trivial cap."""
    length = b_hi - a_lo
    if length <= 0.0:
        return 0.0
    integers = max(math.floor(b_hi) - math.ceil(a_lo) + 1.0, 0.0)
    if length < 2.0:
        return integers
    return min(integers, BT_CONST * length / math.log(length))


def prime_power_count_up(a_lo, b_hi):
    """(C6) higher prime powers in (a_lo, b_hi]."""
    if b_hi <= 4.0:
        return 0.0
    total, k = 0.0, 2
    while 2.0 ** k <= b_hi:
        total += 1.0 + max(0.0, b_hi ** (1.0 / k)
                          - max(a_lo, 1.0) ** (1.0 / k))
        k += 1
    return total


def envelope_maxima(n_top, half_log, n_part=N_PART):
    """Upper bounds for the atom count and the mass Lambda/sqrt(n) in any
    window of log-length 2*half_log below n_top."""
    if n_top <= 2.0:
        return 1.0, math.log(2.0) / math.sqrt(2.0)
    edges = 2.0 * np.exp(np.linspace(0.0, math.log(n_top / 2.0), n_part + 1))
    p_max = l_max = 0.0
    for i in range(n_part):
        y_lo, y_hi = float(edges[i]), float(edges[i + 1])
        a_lo = max(1.0, y_lo * math.exp(-half_log))
        b_hi = y_hi * math.exp(half_log)
        cnt = prime_count_up(a_lo, b_hi) + prime_power_count_up(a_lo, b_hi)
        p_max = max(p_max, cnt)
        l_max = max(l_max, cnt * math.log(b_hi) / math.sqrt(a_lo))
    return p_max, l_max


def quad_form_bounds(mat, vec):
    """Outward-rounded enclosure of vec^T mat vec."""
    n = mat.shape[0]
    val = fsum(vec * (mat @ vec))
    env = gam(n + 2) * fsum(np.abs(vec) * (np.abs(mat) @ np.abs(vec)))
    return val - env, val + env


def knapsack_attained(win_max, cap, total):
    """A LOWER bound: the value of one admissible packing (non-adjacent
    windows, each filled to the cap)."""
    order = np.argsort(-np.asarray(win_max, float))
    used, left, parts = set(), float(total), []
    for j in order:
        if left < cap or win_max[j] <= 0.0:
            break
        if (j - 1) in used or (j + 1) in used:
            continue
        used.add(int(j))
        parts.append(cap * float(win_max[j]))
        left -= cap
    return fsum(parts) if parts else 0.0


def knapsack_up(win_max, cap, total):
    """The exact supremum of sum_j m_j max_j subject to 0 <= m_j <= cap,
    sum m_j <= total (greedy on a linear objective)."""
    vals = np.sort(np.asarray(win_max, float))[::-1]
    vals = vals[vals > 0.0]
    left, parts = float(total), []
    for val in vals:
        if left <= 0.0:
            break
        take = min(cap, left)
        parts.append(take * val)
        left -= take
    return fsum(parts) if parts else 0.0


def tent_interp(nodes, vals, xs):
    return np.interp(np.asarray(xs, float), nodes, vals, left=0.0, right=0.0)


def graded_edges(edges, ratio):
    out = [float(edges[0])]
    for a_val, b_val in zip(edges[:-1], edges[1:]):
        a_val, b_val = float(a_val), float(b_val)
        if a_val > 0.0 and b_val / a_val > ratio:
            n_sub = int(math.ceil(math.log(b_val / a_val) / math.log(ratio)))
            for k in range(1, n_sub):
                out.append(a_val * (b_val / a_val) ** (k / float(n_sub)))
        out.append(b_val)
    return np.array(out)


def panel_integral(fun, edges, gl_x, gl_w):
    a_e, b_e = edges[:-1], edges[1:]
    half = 0.5 * (b_e - a_e)
    mid = 0.5 * (a_e + b_e)
    xs = mid[:, None] + half[:, None] * gl_x[None, :]
    vals = fun(xs.ravel()).reshape(xs.shape)
    return float(np.dot(half, vals @ gl_w))


def pole_pmain_exact(nodes_x, fun):
    """POLE = 4 int_0^S F cosh(x/2) and P_main = 2 int_0^S F e^{x/2} in
    closed form, for an F that is linear on each panel [nodes_x[i],
    nodes_x[i+1]].  The affine piece is read from two STRICTLY INTERIOR
    points, because F carries a genuine jump at the last tent node (the
    interpolant of v is extended by zero and v does not vanish there);
    reading the endpoint values would silently interpolate across it."""
    pole = p_main = 0.0
    for i in range(len(nodes_x) - 1):
        a_val, b_val = float(nodes_x[i]), float(nodes_x[i + 1])
        if b_val <= a_val:
            continue
        t_one = (b_val - a_val) / 3.0
        t_two = 2.0 * (b_val - a_val) / 3.0
        f_one = float(fun(np.array([a_val + t_one]))[0])
        f_two = float(fun(np.array([a_val + t_two]))[0])
        slope = (f_two - f_one) / (t_two - t_one)
        icept = f_one - slope * (a_val + t_one)

        def i_exp(c, a_val=a_val, b_val=b_val, slope=slope, icept=icept):
            def prim(x):
                return math.exp(c * x) * ((icept + slope * x) / c
                                          - slope / (c * c))
            return prim(b_val) - prim(a_val)
        pole += 4.0 * 0.5 * (i_exp(0.5) + i_exp(-0.5))
        p_main += 2.0 * i_exp(0.5)
    return pole, p_main


def arch_graded(fun, edges_raw, f_zero, n_gl, ratio):
    gl_x, gl_w = np.polynomial.legendre.leggauss(n_gl)
    edges = graded_edges(edges_raw, ratio)
    s_end = float(edges[-1])

    def integ(wv):
        return ((f_zero * np.exp(-2.0 * wv) - fun(wv) * np.exp(-0.5 * wv))
                / (-np.expm1(-2.0 * wv)))
    body = panel_integral(integ, edges, gl_x, gl_w)
    tail = -0.5 * math.log1p(-math.exp(-2.0 * s_end)) * f_zero
    return -f_zero * (np.euler_gamma + math.log(math.pi)) + 2.0 * (body + tail)


# ============================================== the deployed matrix stage
def stage_rows(cell, thetas, world="truth", want_k=True):
    """Rebuild the deployed matrix stage and every derived quantity."""
    atoms_u, atoms_m = sap.cell_atoms(cell)
    wall = sap.Wall(cell, atoms_u, atoms_m)
    h = wall.h
    d_val = wall.D
    alpha = float(cell["alpha"])
    a2 = msc.second_difference_matrix(h)
    idx = np.arange(-1.0, h + 2.0)
    ci_scalar = wall.c_scalar_vec(idx)
    ci_arch = sap.core.arch_A(np.abs(idx) * d_val, d_val)
    rows = []
    for theta in thetas:
        c_ar, c_at = wall.c_ladder(theta, split=True)
        c_full = c_ar + c_at
        g_h = c_full[1:-1] - 0.5 * (c_full[2:] + c_full[:-2])
        g_ar = c_ar[1:-1] - 0.5 * (c_ar[2:] + c_ar[:-2])
        omega = wall.omega_from_gh(g_h)
        g_t_ar = ci_arch[1:h + 1] - 0.5 * (ci_arch[2:h + 2] + ci_arch[0:h])
        omega0 = 0.5 * (sla.hankel(g_ar[:h], g_ar[h - 1:2 * h - 1])
                        + sla.toeplitz(g_t_ar[:h]))
        n_true = float(omega[0, 0])
        b_vec = np.ascontiguousarray(omega[1:, 0])
        b_mat = np.ascontiguousarray(omega[1:, 1:])
        n_zero = float(omega0[0, 0])
        b_zero = np.ascontiguousarray(omega0[1:, 0])
        b_comb = b_zero - b_vec
        n_comb = n_zero - n_true
        w_src = -(c_at[:h + 2] + (ci_scalar - ci_arch)[:h + 2])
        cf = sla.cho_factor(b_mat, lower=True, check_finite=False)
        beta = sap.chol_cert_lower(b_mat, sap.lam_hint(b_mat, cf))
        if beta is None or beta <= 0.0:
            rows.append(dict(theta=theta, refused=True))
            continue
        q0_lo, q0_hi, x_zero, _ = msc.quad_encl(b_zero, b_mat, cf, beta)
        qc_lo, qc_hi, _, _ = msc.quad_encl(b_comb, b_mat, cf, beta)
        lin_lo, lin_hi = msc.bilin_encl(b_comb, b_zero, b_mat, cf, beta,
                                        q0_hi)
        v_vec = msc.second_difference_T(x_zero, h)
        fact = float(np.max(np.abs(-0.25 * (a2 @ w_src) - b_comb)))
        omega_flip = omega.copy()
        b_flip = b_zero + b_comb
        omega_flip[0, 0] = n_zero + n_comb
        omega_flip[1:, 0] = b_flip
        omega_flip[0, 1:] = b_flip
        cert_flip = sap.cert_schur(omega_flip)
        # Cholesky-free variational path: q >= 2<b,y> - y^T B y for any y
        y_hint = sla.cho_solve(cf, b_zero, check_finite=False)
        var_q0 = 2.0 * fsum(b_zero * y_hint) - fsum(y_hint * (b_mat @ y_hint))
        y_hint_c = sla.cho_solve(cf, b_comb, check_finite=False)
        var_qc = (2.0 * fsum(b_comb * y_hint_c)
                  - fsum(y_hint_c * (b_mat @ y_hint_c)))
        row = dict(theta=theta, refused=False, h=h, D=d_val, alpha=alpha,
                   n_true=n_true, n_zero=n_zero, n_comb=n_comb, beta=beta,
                   q0_lo=q0_lo, q0_hi=q0_hi, qc_lo=qc_lo, qc_hi=qc_hi,
                   lin_lo=lin_lo, lin_hi=lin_hi, w=w_src, v=v_vec,
                   b_zero=b_zero, b_comb=b_comb, x_zero=x_zero, fact=fact,
                   b_mat=b_mat, cf=cf, var_q0=var_q0, var_qc=var_qc,
                   b0_norm=math.sqrt(fsum(b_zero * b_zero)),
                   s_flip_hi=(cert_flip["s_hi"] if sap.ok_res(cert_flip)
                              else None),
                   signed=-0.5 * fsum(w_src * v_vec))
        row["need"] = ((row["q0_hi"] - row["n_zero"]) + row["qc_hi"]
                       + abs(row["n_comb"]))
        if want_k:
            y_mat = sla.cho_solve(cf, a2, check_finite=False)
            row["K"] = msc.apply_at_matrix(y_mat, h)
        rows.append(row)
    return wall, h, d_val, alpha, a2, rows


def main():
    mp.dps = MP_DPS
    verdict = "NOGO-COMPOSITE-VERIFIED"
    load_bearing_fail = []

    section("S0  INSTRUMENT, FIREWALL, AND THE NINE FRAMES")
    print("  SPEC_SHA        %s" % SPEC_SHA)
    with open(os.path.abspath(__file__), "rb") as fh:
        print("  PROBE_SHA       %s" % hashlib.sha256(fh.read()).hexdigest())
    for mod in (sap, sad, msc):
        with open(mod.__file__, "rb") as fh:
            print("  SOURCE_SHA %-34s %s"
                  % (os.path.basename(mod.__file__),
                     hashlib.sha256(fh.read()).hexdigest()[:32]))
    hits = ast_firewall()
    check("S0.1 AST firewall clean (no zero data, no eigensolver, no fit)",
          not hits, "hits=%s" % (hits or "none"))
    check("S0.2 mp precision frozen", mp.dps == MP_DPS, "dps=%d" % mp.dps)

    pp = prime_power_list(PP_CAP)
    check("S0.3 prime-power list starts 2,3,4,5,7,8,9,11",
          pp[:8] == [2, 3, 4, 5, 7, 8, 9, 11], "%s" % pp[:8])
    frames = {}
    worst_frame_rel = 0.0
    h_ok = True
    for want_h, kz in FRAME_SPECS:
        fr = build_frame(pp, kz)
        frames[want_h] = fr
        h_ok = h_ok and (fr["h"] == want_h)
        root = math.exp(fr["alpha"] + fr["D"])
        worst_frame_rel = max(worst_frame_rel,
                              rel(fr["D"] * root, fr["gap"] / 4.0))
    check("S0.4 all nine frames reconstructed from prime powers alone",
          h_ok, "h = %s" % [frames[k]["h"] for k, _ in FRAME_SPECS])
    check("S0.5 test scale sits ON the square-root barrier: "
          "D_h sqrt(N_h) = gap/4", worst_frame_rel < 5e-2,
          "worst rel %.4e (cited %.4e)" % (worst_frame_rel, WARD_FRAME_REL))
    if rel(worst_frame_rel, WARD_FRAME_REL) > 1e-3:
        disclose("S0.5 frame rel", "%.4e" % worst_frame_rel,
                 "%.4e" % WARD_FRAME_REL)
    gaps = [frames[k]["gap"] for k, _ in FRAME_SPECS]
    check("S0.6 integer gap is O(log N) on every frame (so the family is "
          "indexed by kz, not by h)",
          all(frames[k]["gap"] <= frames[k]["log_n"] for k, _ in FRAME_SPECS),
          "gaps %s vs log N %s" % (gaps, ["%.1f" % frames[k]["log_n"]
                                          for k, _ in FRAME_SPECS]))

    # ------------------------------------------------------------------ S1
    section("S1  (T0) THE EXACT KERNEL LEDGER  (sympy, exact in D)")
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
    check("S1.3 ||K_D'||_1 = 4, independent of D (exact)",
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
    print("  READING: the conversion constant of any magnitude hypothesis is "
          "bounded BELOW by ||K_D'||_1 = 4 uniformly in D -- the kernel does "
          "not become cheap as the frames get finer.  This is the exact fact "
          "that makes S2 unconditional.")

    # ------------------------------------------------------------------ S2
    section("S2  (T1) THE MAGNITUDE CLASS IS UNCONDITIONALLY EMPTY")
    theta_zero_closed = (4 - mp.euler - 3 * mp.log(2) - mp.pi / 2
                         - mp.log(mp.pi))
    check("S2.1 Theta(0) closed form = digamma route = Stirling route",
          mp.almosteq(theta_zero_closed, theta_mp(0),
                      abs_eps=mp.mpf(10) ** -45)
          and mp.almosteq(theta_stirling(0), theta_mp(0),
                          abs_eps=mp.mpf(10) ** -24),
          "%s | Stirling deviation %.2e"
          % (mp.nstr(theta_zero_closed, 25),
             float(abs(theta_stirling(0) - theta_mp(0)))))
    check("S2.2 Theta(0) reproduces the cited 49-digit value",
          mp.nstr(theta_zero_closed, 47) == mp.nstr(mp.mpf(WARD_THETA0), 47),
          "%s" % mp.nstr(theta_zero_closed, 20))
    r_lo, r_hi = mp.mpf(WARD_R_STAR[0]), mp.mpf(WARD_R_STAR[1])
    check("S2.3 Theta has a certified sign change in the cited bracket "
          "r* (so Theta < 0 on a band and the supply cannot be repaired by "
          "a wider window)",
          theta_mp(r_lo) < 0 < theta_mp(r_hi),
          "Theta(r_lo) %.3e, Theta(r_hi) %.3e"
          % (float(theta_mp(r_lo)), float(theta_mp(r_hi))))
    band_hi = r_lo - mp.mpf(1) / 100
    n_band = 3000
    step = band_hi / n_band
    lip = mp.mpf(0)
    band_max = -mp.inf
    for k in range(n_band + 1):
        r_pt = k * step
        band_max = max(band_max, theta_mp(r_pt))
        der = (-2 * r_pt / (mp.mpf(1) / 4 + r_pt ** 2) ** 2
               + mp.re(mp.mpc(0, mp.mpf(1) / 2)
                       * mp.polygamma(1, mp.mpf(1) / 4 + mp.mpc(0, r_pt) / 2)))
        lip = max(lip, abs(der))
    band_cert = band_max + lip * step / 2
    check("S2.4 Theta certified strictly negative on [0, r*-1/100] "
          "(Lipschitz-covered grid, 3001 nodes)", band_cert < 0,
          "sup <= %.6e (Lipschitz %.4f)" % (float(band_cert), float(lip)))

    supply = {}
    for h_key in (184, 388):
        fr = frames[h_key]
        s_len = mp.mpf(2) * mp.mpf(fr["alpha"]) * (1 + mp.mpf(1) / fr["h"])
        closed = fejer_closed(s_len)
        quadr = fejer_quadrature(s_len)
        four, four_tail = fejer_fourier(s_len)
        n_cap = int(mp.floor(mp.exp(s_len)))
        lam = lambda_table(max(n_cap, 2))
        nz = np.nonzero(lam > 0)[0]
        prime = 2.0 * float(sum(mp.mpf(lam[n]) / mp.sqrt(int(n))
                                * (1 - mp.log(int(n)) / s_len) for n in nz))
        delta = prime - float(closed["p_main"])
        slack = 0.5 * (float(closed["B"]) - delta)
        psi_cum = np.cumsum(lam)
        n_ax = np.arange(0, len(lam), dtype=float)
        eta_meas = float(np.max(np.abs(psi_cum[1:] - n_ax[1:]) / n_ax[1:]))
        supply[h_key] = dict(S=s_len, closed=closed, quad=quadr, four=four,
                             four_tail=four_tail, prime=prime, delta=delta,
                             slack=slack, eta=eta_meas, N=n_cap)
        check("S2.5 h=%d Fejer supply B by three independent routes agrees "
              "(closed | quadrature | Fourier)" % h_key,
              abs(float(closed["B"] - quadr["B"])) < 1e-15
              and abs(float(closed["B"]) - four) < 1e-4,
              "closed %s | quad dev %.2e | Fourier dev %.2e (tail %.1e)"
              % (mp.nstr(closed["B"], 18),
                 float(abs(closed["B"] - quadr["B"])),
                 abs(float(closed["B"]) - four), float(four_tail)))
        cited = mp.mpf(WARD_FEJER_B[h_key])
        ok_b = abs(float(closed["B"] - cited)) < 1e-15
        check("S2.6 h=%d B reproduces the cited value and is NEGATIVE "
              "(the supply has the WRONG SIGN)" % h_key,
              ok_b and closed["B"] < 0,
              "B %s (cited %s), B/V %.8f"
              % (mp.nstr(closed["B"], 20), WARD_FEJER_B[h_key],
                 float(closed["B"] / closed["V"])))
        if not ok_b:
            disclose("S2.6 B(h=%d)" % h_key, mp.nstr(closed["B"], 20),
                     WARD_FEJER_B[h_key])
        check("S2.7 h=%d eta = sup |psi(n)-n|/n = 1 EXACTLY (attained at "
              "n=1, so the trivial magnitude input is already saturated)"
              % h_key, abs(eta_meas - 1.0) < 1e-15, "eta = %.15f" % eta_meas)
    check("S2.8 the geometric supply is O(1) at both registered rungs "
          "(|B| <= 2), while the Littlewood floor diverges",
          all(abs(float(supply[k]["closed"]["B"])) <= 2.0 for k in supply),
          "B = %s" % ["%.6f" % float(supply[k]["closed"]["B"])
                      for k in sorted(supply)])

    floors = {}
    for h_key in (184, 12632):
        n_val = mp.exp(mp.mpf(frames[h_key]["log_n"]))
        floors[h_key] = 4 * mp.log(mp.log(mp.log(n_val)))
        ok_fl = float(floors[h_key]) >= WARD_LITTLEWOOD[h_key] - 5e-7
        check("S2.9 h=%d Littlewood floor 4 logloglog N_h >= %.7f"
              % (h_key, WARD_LITTLEWOOD[h_key]), ok_fl,
              "floor %.7f" % float(floors[h_key]))
        if not ok_fl:
            disclose("S2.9 floor(h=%d)" % h_key,
                     "%.7f" % float(floors[h_key]),
                     "%.7f" % WARD_LITTLEWOOD[h_key])
    own_slack = max(supply[k]["slack"] for k in supply)
    ratio_own = float(floors[184]) / own_slack
    ratio_cited = float(floors[12632]) / WARD_SLACK_CITED
    check("S2.10 THE CLASS IS EMPTY: floor / slack >> 1 on this probe's OWN "
          "conservative slack and on the deployed slack (X2)",
          ratio_own > 100.0 and ratio_cited > 100.0,
          "own %.1f (slack %.4e) | cited %.1f (slack %.1e)"
          % (ratio_own, own_slack, ratio_cited, WARD_SLACK_CITED))
    print("  h=%d: P_main %.6f, PRIME %.6f, Delta %.6f, own slack %.4e"
          % (184, float(supply[184]["closed"]["p_main"]),
             supply[184]["prime"], supply[184]["delta"],
             supply[184]["slack"]))

    eps_y = {}
    for want_h, _kz in FRAME_SPECS:
        fr = frames[want_h]
        eps_y[want_h] = 0.5 + math.log(fr["gap"] / 4.0) / fr["log_n"]
    a_allowed = {k: 1.0 / (1.0 - v) for k, v in eps_y.items()}
    deep = [5746, 12632, 2854, 2607]
    check("S2.11 density hypothesis is EXACTLY critical: the required "
          "exponent is eps_y = 1/2 + log(gap/4)/log N -> 1/2, so A <= 2 - "
          "delta is needed while N(1/2,T) >> T log T forces A >= 2 (X3)",
          max(abs(eps_y[k] - 0.5) for k in deep) < 0.08
          and max(a_allowed.values()) < 2.43,
          "|eps_y - 1/2| <= %.4f at the four deepest, max A allowed %.4f"
          % (max(abs(eps_y[k] - 0.5) for k in deep), max(a_allowed.values())))
    fr12 = frames[12632]
    rh_short = 4.0 * fr12["log_n"] ** 2 / fr12["gap"]
    rh_block = ((6.0 + 2.0 * fr12["D"] / 3.0) * fr12["log_n"] ** 2
                / SCHOENFELD_DEN)
    check("S2.12 even RH's short-interval asymptotic is too short by "
          "4 log^2 N / gap, and Schoenfeld's RH block envelope is O(1)-huge",
          rel(rh_short, WARD_RH_SHORT) < 1e-4
          and rel(rh_block, WARD_RH_BLOCK) < 1e-4,
          "shortfall %.3f (cited %.3f) | RH block %.4f (cited %.4f)"
          % (rh_short, WARD_RH_SHORT, rh_block, WARD_RH_BLOCK))

    # Selberg symmetry: formal identity in the free module on {log p}
    n_sel = 36
    primes_sel = [p for p in range(2, n_sel + 1)
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
    for n in range(1, n_sel + 1):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        ok_lam = ok_lam and sp.expand(
            sum(mu_int(d) * log_sym(n // d) for d in divs) - lam_sym(n)) == 0
        lhs = sum(mu_int(d) * sp.expand(log_sym(n // d) ** 2) for d in divs)
        rhs = sp.expand(lam_sym(n) * log_sym(n)
                        + sum(lam_sym(d) * lam_sym(n // d) for d in divs))
        ok_sel = ok_sel and sp.expand(lhs - rhs) == 0
    check("S2.13 Selberg symmetry is PROVABLY NEUTRAL: Lambda = mu * log and "
          "mu * log^2 = Lambda.log + Lambda * Lambda are formal identities in "
          "the free module on {log p} (n <= 36), so they add no arithmetic "
          "content -- information gain exactly 1.000",
          ok_lam and ok_sel, "both identities exact")

    # ------------------------------------------------------------------ S3
    section("S3  (T2) THE REQUIREMENT IS SIGNED AND CONGRUENCE-INVARIANT")
    h_s = 4
    bm_s = sp.Matrix(h_s - 1, h_s - 1,
                     lambda i, j: sp.Symbol("B%d%d" % (min(i, j), max(i, j))))
    m_s = sp.Matrix(h_s - 1, h_s - 1, lambda i, j: sp.Symbol("M%d%d" % (i, j)))
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
    check("S3.1 the three-term split s = (n_0 - q_0) - n_c + 2<b_c,x_0> - q_c "
          "is an identity (sympy, exact)",
          sp.simplify(s_split - s_direct) == 0)
    bt_s = m_s.T * b_s
    ct_s = m_s.T * c_s
    bmt_s = m_s.T * bm_s * m_s
    inv_t = bmt_s.inv()
    ok_inv = all(sp.simplify(x) == 0 for x in (
        (bt_s.T * inv_t * bt_s)[0] - q0_s,
        (ct_s.T * inv_t * ct_s)[0] - qc_s,
        (ct_s.T * inv_t * bt_s)[0] - lin_s))
    check("S3.2 all three terms are invariant under every congruence "
          "T = diag(1, M) (sympy, exact) -- the OBJECT is basis independent, "
          "the DEMAND is not", ok_inv)
    check("S3.3 parity under the comb sign flip b_c -> -b_c: outer terms "
          "EVEN, middle term ODD (exact)",
          sp.simplify(q0_s.subs({c_s[i, 0]: -c_s[i, 0]
                                 for i in range(h_s - 1)}) - q0_s) == 0
          and sp.simplify(qc_s.subs({c_s[i, 0]: -c_s[i, 0]
                                     for i in range(h_s - 1)}) - qc_s) == 0
          and sp.simplify(lin_s.subs({c_s[i, 0]: -c_s[i, 0]
                                      for i in range(h_s - 1)})
                          + lin_s) == 0)
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

    thetas = [(k + 0.5) / N_THETA for k in range(N_THETA)]
    stage = {}
    sap.build_tables()
    census = sap.census()
    picks = sap.pick_cells(census)
    for tgt in AUDIT_TARGETS:
        wall, h, d_val, alpha, a2, rows = stage_rows(picks[tgt], thetas)
        good = [r for r in rows if not r["refused"]]
        stage[tgt] = dict(h=h, D=d_val, alpha=alpha, rows=good, A2=a2)
        m_cnt = len(good)
        s_mean = fsum([r["n_zero"] - r["n_comb"]
                       - 0.5 * (r["q0_lo"] + r["q0_hi"])
                       + 2 * 0.5 * (r["lin_lo"] + r["lin_hi"])
                       - 0.5 * (r["qc_lo"] + r["qc_hi"])
                       for r in good]) / m_cnt
        s_mean_lo = fsum([r["n_zero"] - r["n_comb"] - r["q0_hi"]
                          + 2 * r["lin_lo"] - r["qc_hi"]
                          for r in good]) / m_cnt
        s_mean_hi = fsum([r["n_zero"] - r["n_comb"] - r["q0_lo"]
                          + 2 * r["lin_hi"] - r["qc_lo"]
                          for r in good]) / m_cnt
        even_mean = fsum([r["n_zero"] - r["q0_hi"] for r in good]) / m_cnt
        odd_mean = fsum([2 * 0.5 * (r["lin_lo"] + r["lin_hi"])
                         for r in good]) / m_cnt
        qc_mean = fsum([0.5 * (r["qc_lo"] + r["qc_hi"])
                        for r in good]) / m_cnt
        need_mean = fsum([r["need"] for r in good]) / m_cnt
        stage[tgt].update(s_mean=s_mean, even_mean=even_mean,
                          odd_mean=odd_mean, qc_mean=qc_mean,
                          need_mean=need_mean)
        ok_s = s_mean_lo <= WARD_S_MEAN[h] <= s_mean_hi
        check("S3.5 h=%d the deployed theta-mean of s lies inside this "
              "probe's independently computed enclosure (same object "
              "measured)" % h, ok_s,
              "mid %.9e in [%.9e, %.9e], cited %.9e (mid dev %.1e, half "
              "width %.1e)" % (s_mean, s_mean_lo, s_mean_hi, WARD_S_MEAN[h],
                               abs(s_mean - WARD_S_MEAN[h]),
                               0.5 * (s_mean_hi - s_mean_lo)))
        if abs(s_mean - WARD_S_MEAN[h]) > 1e-9:
            disclose("S3.5 s_mean midpoint(h=%d), cited inside enclosure" % h,
                     "%.9e" % s_mean, "%.9e" % WARD_S_MEAN[h])
        check("S3.6 h=%d n_c vanishes identically (the R summand of the "
              "deployed bound is vacuum)" % h,
              max(abs(r["n_comb"]) for r in good) == 0.0,
              "max |n_c| = %.1e" % max(abs(r["n_comb"]) for r in good))
        check("S3.7 h=%d EVEN terms negative, positivity carried ONLY by the "
              "ODD term" % h,
              even_mean < 0 and qc_mean >= 0 and odd_mean > 0
              and even_mean - qc_mean < 0,
              "even %.6f, odd %+.6f, q_c %.6f (cited %.6f / %+.6f / %.6f)"
              % (even_mean, odd_mean, qc_mean, WARD_EVEN_MEAN[h],
                 WARD_ODD_MEAN[h], WARD_QC_MEAN[h]))
        for tag, got, want in (("even", even_mean, WARD_EVEN_MEAN[h]),
                               ("odd", odd_mean, WARD_ODD_MEAN[h]),
                               ("q_c", qc_mean, WARD_QC_MEAN[h])):
            if rel(got, want) > 1e-4:
                disclose("S3.7 %s(h=%d)" % (tag, h), "%.6f" % got,
                         "%.6f" % want)
        check("S3.8 h=%d source factorization b_c = -(1/4) A_2 w exact at "
              "every audited (cell, theta)" % h,
              max(r["fact"] for r in good) < 1e-14,
              "worst residual %.2e" % max(r["fact"] for r in good))
        flips = [r["s_flip_hi"] for r in good if r["s_flip_hi"] is not None]
        check("S3.9 h=%d the sign-flipped counter-world (admissible in "
              "I_box) is certified NEGATIVE by the deployed routine" % h,
              len(flips) == len(good) and max(flips) < 0,
              "worst certified upper bound %.6f over %d/%d thetas"
              % (max(flips), len(flips), len(good)))
        var_slack = min(r["var_q0"] + r["var_qc"] - r["n_zero"]
                        - abs(r["n_comb"]) for r in good)
        check("S3.10 h=%d Cholesky-FREE variational path (q >= 2<b,y> - "
              "y^T B y, matrix-vector only) confirms q_0 + q_c > n_0 + |n_c|"
              % h, var_slack > 0, "worst slack %.6f" % var_slack)
    worst_flip = max(max(r["s_flip_hi"] for r in stage[t]["rows"]
                         if r["s_flip_hi"] is not None)
                     for t in AUDIT_TARGETS)
    check("S3.11 the counter-world bound reproduces the cited worst value",
          worst_flip <= WARD_FLIP_WORST + 1e-3,
          "%.6f (cited %.6f)" % (worst_flip, WARD_FLIP_WORST))

    # growth attribution (exact factors; total normalisation is CITED (X5))
    beta_min = {}
    r_dep = {}
    for tgt in REGISTERED_RUNGS:
        st = stage[tgt]
        beta_min[st["h"]] = min(r["beta"] for r in st["rows"])
        r_dep[st["h"]] = msc.r_deployed(st["alpha"], st["D"])[0]
    h_lo, h_hi = 184, 388
    o_beta = math.log10(beta_min[h_lo] / beta_min[h_hi])
    o_r = 2.0 * math.log10(r_dep[h_hi] / r_dep[h_lo])
    o_dim = math.log10((h_hi - 1.0) / (h_lo - 1.0))
    shares = tuple(100.0 * x / WARD_GROWTH_TOTAL for x in (o_beta, o_r, o_dim))
    ok_growth = (all(rel(beta_min[k], 1.0 / WARD_BETA_INV[k]) < 1e-4
                     for k in (h_lo, h_hi))
                 and all(rel(r_dep[k], WARD_R_DEPLOYED[k]) < 1e-6
                         for k in (h_lo, h_hi))
                 and max(abs(a - b) for a, b in
                         zip((o_beta, o_r, o_dim), WARD_GROWTH_ORDERS)) < 5e-4
                 and max(abs(a - b) for a, b in
                         zip(shares, WARD_GROWTH_SHARES)) < 0.2)
    check("S3.12 growth attribution re-derived: over half the demand growth "
          "is the inverse of the certified co-floor, not arithmetic",
          ok_growth,
          "beta^-1 %.4f ord (%.1f pct) | R^2 %.4f ord (%.1f pct) | dim %.4f "
          "ord (%.1f pct); R alone grows only %.4f ord"
          % (o_beta, shares[0], o_r, shares[1], o_dim, shares[2], o_r / 2))
    if not ok_growth:
        disclose("S3.12 growth", "%.4f/%.4f/%.4f" % (o_beta, o_r, o_dim),
                 "%.4f/%.4f/%.4f" % WARD_GROWTH_ORDERS)
    print("  READING: the signed requirement survives every congruence, "
          "every window and every preconditioner because the split terms "
          "are invariant and the carrying term is ODD; an unsigned hull is "
          "flip-invariant, hence structurally unable to bound it below.")

    # ------------------------------------------------------------------ S4
    section("S4  (T3) THE SIGNED RESIDUAL IS EXACTLY A WEIL PRIME TERM")
    weil = {}
    for tgt in AUDIT_TARGETS:
        st = stage[tgt]
        h, d_val, alpha = st["h"], st["D"], st["alpha"]
        row = st["rows"][0]
        assert abs(row["theta"] - EF_THETA) < 1e-15
        v_vec = row["v"]
        nodes = np.arange(-1.0, h + 1.0)

        def f_even(u, nodes=nodes, v_vec=v_vec, d_val=d_val):
            nu = np.abs(np.asarray(u, float)) / d_val
            return -0.25 * (tent_interp(nodes, v_vec, nu)
                            + tent_interp(nodes, v_vec, nu - 2.0 * EF_THETA))
        brk = np.unique(np.concatenate([nodes, nodes + 2.0 * EF_THETA]))
        edges = np.concatenate([[0.0], brk[brk > 0.0] * d_val])
        f_zero = float(f_even(np.array([0.0]))[0])
        pole_ex, pmain_ex = pole_pmain_exact(edges, f_even)
        gl_x, gl_w = np.polynomial.legendre.leggauss(GL_N)
        ge = graded_edges(edges, GRADE_RATIO)
        pole_gl = 4.0 * panel_integral(
            lambda x: f_even(x) * np.cosh(0.5 * x), ge, gl_x, gl_w)
        arch_fine = arch_graded(f_even, edges, f_zero, 32, 1.5)
        arch_coarse = arch_graded(f_even, edges, f_zero, GL_N_WARD, 3.0)
        signed = row["signed"]
        s_len = (h + 2.0 * EF_THETA) * d_val
        n_cap = int(math.floor(math.exp(s_len)))
        lam = lambda_table(max(n_cap, 2))
        nz = np.nonzero(lam > 0)[0]
        prime_atoms = 2.0 * fsum(lam[nz] / np.sqrt(nz.astype(float))
                                 * f_even(np.log(nz.astype(float))))
        need_t = row["need"]
        bar = pole_ex + arch_fine - need_t
        xi = np.linspace(0.0, FHAT_XI_MAX / d_val, FHAT_N)
        fhat = np.array([2.0 * panel_integral(
            lambda u, x=x: f_even(u) * np.cos(x * u), ge, gl_x, gl_w)
            for x in xi])
        weil[tgt] = dict(h=h, f0=f_zero, pole=pole_ex, pole_gl=pole_gl,
                         arch=arch_fine,
                         arch_ward=abs(arch_fine - arch_coarse),
                         p_main=pmain_ex, signed=signed,
                         prime_atoms=prime_atoms, bar=bar, need=need_t,
                         fhat_min=float(fhat.min()),
                         fhat_max=float(fhat.max()),
                         negfrac=float(np.mean(fhat < 0)), S=s_len, N=n_cap)
        check("S4.1 h=%d the signed correlation IS Weil's PRIME(F) for "
              "F(u) = -(1/4) Psi(|u|/D): matrix route = atom route" % h,
              abs(signed - prime_atoms) <= 1e-12 * max(abs(signed), 1.0),
              "matrix %.9e, atoms %.9e, deviation %.2e"
              % (signed, prime_atoms, abs(signed - prime_atoms)))
        check("S4.2 h=%d POLE exact = graded quadrature; ARCH stable under "
              "refinement" % h,
              rel(pole_gl, pole_ex) < 1e-6 and weil[tgt]["arch_ward"] < 1e-6,
              "POLE %.9e (quad dev %.1e), ARCH %.9e (ward %.1e)"
              % (pole_ex, abs(pole_gl - pole_ex), arch_fine,
                 weil[tgt]["arch_ward"]))
        ok_bar = bar < 0 and rel(bar, WARD_BAR[h]) < 0.05
        check("S4.3 h=%d the remaining statement is sum_rho Fhat(gamma_rho) "
              "< a NEGATIVE bar (the OPPOSITE of a Weil-positivity "
              "statement)" % h, ok_bar,
              "bar %.4e (cited %.3f)" % (bar, WARD_BAR[h]))
        if not ok_bar:
            disclose("S4.3 bar(h=%d)" % h, "%.4e" % bar, "%.3f" % WARD_BAR[h])
        check("S4.4 h=%d Fhat takes BOTH signs, so the demand is not "
              "self-contradictory" % h,
              weil[tgt]["fhat_min"] < 0 < weil[tgt]["fhat_max"]
              and WARD_FHAT_NEGFRAC[0] <= weil[tgt]["negfrac"]
              <= WARD_FHAT_NEGFRAC[1],
              "Fhat in [%.3e, %.3e], negative on %.0f pct of the grid"
              % (weil[tgt]["fhat_min"], weil[tgt]["fhat_max"],
                 100.0 * weil[tgt]["negfrac"]))
    print("  READING: every bound in the toolkit bounds |PRIME(F)| from "
          "ABOVE, while the statement needs a signed LOWER bound.  What "
          "remains is the position of the ordinates against the sign "
          "pattern of Fhat -- a zero-position statement, not a size one.")

    # ------------------------------------------------------------------ S5
    section("S5  (T4) THE UNSIGNED COMPANION: BOUNDED, NOT CLOSABLE")
    cone = {}
    for tgt in AUDIT_TARGETS:
        st = stage[tgt]
        h, d_val, alpha = st["h"], st["D"], st["alpha"]
        eta_vk = sad.vk_eta(max(2.0 * alpha - 2.0 * d_val, math.e),
                            sad.VK_c_OPT)
        sqrt_y = math.exp(0.5 * (alpha + 3.0 * d_val))
        rc_reach = (msc.head_source(2) + 4.0 * sqrt_y * math.sinh(0.5 * d_val)
                    + 2.0 * sad.VK_C_OPT * sqrt_y * math.exp(0.5 * d_val)
                    * math.exp(-eta_vk))
        n_top = math.exp(alpha + 3.0 * d_val)
        p_max, l_max = envelope_maxima(n_top, 0.5 * WIN_GRID * d_val)
        t_env = 2.0 * PSI_CHEB * math.sqrt(n_top)
        w2 = 4.0 * l_max * t_env
        cap_inf = 2.0 * rc_reach
        nu2 = math.log(2.0) / d_val
        j_idx = np.arange(max(int(math.floor(nu2)) - 3, 0), h + 2)
        n_win = int(math.ceil((h + 2.0) / WIN_GRID))
        nodes = np.arange(-1.0, h + 1.0)
        agg = dict(u2=0.0, fl_l2=0.0, fl_cone=0.0, s_best=0.0,
                   fl_signed=0.0, u0=0.0, adm=True, w_sup=0.0)
        s_names = ("s1", "s2", "s3", "s4")
        s_agg = {k: 0.0 for k in s_names}
        for row in st["rows"]:
            k_mat = row["K"]
            kj = np.ascontiguousarray(k_mat[np.ix_(j_idx, j_idx)])
            hint = np.ones(len(j_idx)) / math.sqrt(len(j_idx))
            for _ in range(120):
                hint = kj @ hint
                nrm = float(np.linalg.norm(hint))
                if nrm == 0.0:
                    break
                hint /= nrm
            ray_lo = (fsum(hint * (kj @ hint))
                      / (fsum(hint * hint) * (1.0 + gam(len(j_idx)))))
            lam_up = None
            for infl in LAM_INFLATE:
                mu_try = ray_lo * infl
                try:
                    np.linalg.cholesky(mu_try * np.eye(len(j_idx)) - kj)
                    lam_up = mu_try
                    break
                except np.linalg.LinAlgError:
                    continue
            if lam_up is None:
                continue
            agg["u2"] = max(agg["u2"], (1.0 / 16.0) * lam_up * w2)
            agg["fl_l2"] = max(agg["fl_l2"], (1.0 / 16.0) * ray_lo * w2)
            agg["u0"] = max(agg["u0"],
                            0.25 * msc.r_deployed(alpha, d_val)[0] ** 2
                            * fsum(np.abs(k_mat)))
            w_adm = np.maximum(hint, 0.0)
            nrm = math.sqrt(fsum(w_adm * w_adm))
            if nrm > 0.0:
                w_adm = w_adm * min(math.sqrt(w2) / nrm,
                                    cap_inf / max(w_adm.max(), 1e-300))
            agg["adm"] = (agg["adm"] and w_adm.min() >= 0.0
                          and w_adm.max() <= cap_inf * (1 + 1e-12)
                          and fsum(w_adm * w_adm) <= w2 * (1 + 1e-12))
            agg["fl_cone"] = max(agg["fl_cone"],
                                 (1.0 / 16.0) * quad_form_bounds(kj, w_adm)[0])
            psi_full = (tent_interp(nodes, row["v"], np.arange(0.0, h + 1.0))
                        + tent_interp(nodes, row["v"],
                                      np.arange(0.0, h + 1.0)
                                      - 2.0 * row["theta"]))
            w_pos, w_abs = [], []
            for j_w in range(n_win):
                lo = int(j_w * WIN_GRID)
                hi = min(int((j_w + 1) * WIN_GRID), len(psi_full))
                if hi <= lo:
                    continue
                seg_v = psi_full[lo:hi]
                w_pos.append(max(0.0, float(seg_v.max())))
                w_abs.append(float(np.abs(seg_v).max()))
            v_j = row["v"][j_idx]
            s_vals = dict(
                s1=rc_reach * fsum(np.abs(v_j)),
                s2=0.5 * math.sqrt(w2) * math.sqrt(fsum(v_j * v_j)),
                s3=0.5 * t_env * float(np.abs(psi_full).max()),
                s4=0.5 * knapsack_up(w_abs, l_max, t_env))
            for k in s_names:
                s_agg[k] = max(s_agg[k], s_vals[k])
            agg["fl_signed"] = max(agg["fl_signed"],
                                   0.5 * knapsack_attained(w_pos, l_max,
                                                           t_env))
            agg["w_sup"] = max(agg["w_sup"], float(np.max(np.abs(row["w"]))))
        need = st["need_mean"]
        agg.update(s_agg)
        agg["s_best"] = min(s_agg[k] for k in s_names)
        agg.update(need=need, w2=w2, L=l_max, T=t_env, rc_reach=rc_reach,
                   cap_inf=cap_inf, nJ=len(j_idx), h=h)
        cone[tgt] = agg
        ok_u2 = rel(agg["u2"] / need, WARD_U2_MISS[h]) < 0.05
        check("S5.1 h=%d the unsigned companion has an UNCONDITIONAL bound "
              "(Brun-Titchmarsh + Chebyshev only), miss %.1f" % (h,
                                                                 agg["u2"]
                                                                 / need),
              agg["u2"] > 0 and ok_u2,
              "U2 %.3f, need %.6f, miss %.3f (cited %.1f); deployed U0 miss "
              "%.4g" % (agg["u2"], need, agg["u2"] / need, WARD_U2_MISS[h],
                        agg["u0"] / need))
        if not ok_u2:
            disclose("S5.1 U2 miss(h=%d)" % h, "%.3f" % (agg["u2"] / need),
                     "%.1f" % WARD_U2_MISS[h])
        check("S5.2 h=%d the class floor is ATTAINED at an admissible datum "
              "of I_cone and still exceeds need: the CLASS cannot close, "
              "independently of bound sharpness" % h,
              agg["adm"] and agg["fl_cone"] > need,
              "attained floor %.3f, miss %.3f (l2-only floor %.3f, miss "
              "%.3f)" % (agg["fl_cone"], agg["fl_cone"] / need,
                         agg["fl_l2"], agg["fl_l2"] / need))
        ok_sb = rel(agg["s_best"] / need, WARD_SIGNED_BEST_MISS[h]) < 0.05
        check("S5.3 h=%d the SIGNED side: best of four Hoelder/knapsack "
              "bounds still misses, and the attained cone floor > 1" % h,
              agg["s_best"] / need > 1.0 and agg["fl_signed"] / need > 1.0
              and ok_sb,
              "best miss %.3f (cited %.2f) | attained signed cone floor "
              "%.3f, miss %.3f" % (agg["s_best"] / need,
                                   WARD_SIGNED_BEST_MISS[h],
                                   agg["fl_signed"], agg["fl_signed"] / need))
        if not ok_sb:
            disclose("S5.3 signed best miss(h=%d)" % h,
                     "%.3f" % (agg["s_best"] / need),
                     "%.2f" % WARD_SIGNED_BEST_MISS[h])
        print("     h=%d  |J| %d  W2 %.4f  L %.4f  T %.4f  R_c^reach %.5f  "
              "sup|w| %.4f vs hull %.2f" % (h, agg["nJ"], agg["w2"],
                                            agg["L"], agg["T"],
                                            agg["rc_reach"], agg["w_sup"],
                                            agg["cap_inf"]))
    fl_exp = exponent(cone[184]["fl_signed"] / cone[184]["need"],
                      cone[405]["fl_signed"] / cone[405]["need"],
                      cone[184]["h"], cone[405]["h"])
    check("S5.4 the attained signed cone floor GROWS with depth (exponent "
          "> 0), so the miss cannot be driven to 1 inside I_cone either",
          fl_exp > WARD_CONE_FLOOR_EXP_MIN,
          "floor exponent %.4f over the two registered rungs" % fl_exp)
    print("  READING: q_c is bounded unconditionally, but the class floor is "
          "attained ABOVE the need.  Closing it requires the ALIGNMENT of w "
          "with the spectral directions of K -- information strictly outside "
          "I_cone.")

    # ------------------------------------------------------------------ S6
    section("S6  (T5) CLASS TABLE: PROVEN EMPTY vs MERELY UNEXPLORED")
    # CCCLXI: unitriangular multiplicative transforms preserve the negative
    n_mu = 12

    def mu_small(n):
        out, m = 1, n
        for p in range(2, n + 1):
            if m % p == 0:
                m //= p
                out = -out
                if m % p == 0:
                    return 0
        return out if m == 1 else 0

    t_one = sp.Matrix(n_mu, n_mu,
                      lambda i, j: 1 if (j + 1) % (i + 1) == 0 else 0)
    t_mu = sp.Matrix(n_mu, n_mu,
                     lambda i, j: mu_small((j + 1) // (i + 1))
                     if (j + 1) % (i + 1) == 0 else 0)
    e_two = mp.log(2) * (mp.log(2) - 2)
    e_vec = sp.Matrix([sp.Integer(-1), sp.Integer(2), sp.Integer(1)])
    h_e = sp.zeros(4, 4)
    h_e[0, 1:] = e_vec.T / 2
    h_e[1:, 0] = e_vec / 2
    uni = sp.Matrix(4, 4, lambda i, j: 1 if i == j
                    else (sp.Rational(j - i, 3) if j > i else 0))

    def inertia(mat):
        pos = neg = zer = 0
        for lam_v, mult in mat.eigenvals().items():
            sgn = sp.sign(sp.nsimplify(sp.re(sp.N(lam_v, 30))))
            if sgn > 0:
                pos += mult
            elif sgn < 0:
                neg += mult
            else:
                zer += mult
        return (pos, neg, zer)

    in_plain = inertia(h_e)
    in_cong = inertia(sp.simplify(uni.T * h_e * uni))
    check("S6.1 CCCLXI re-derived: T_mu T_1 = I exactly (both unitriangular, "
          "det 1), the polarization matrix H_e has inertia (1,1,*) with the "
          "n=2 witness e_2 = log2(log2-2) < 0, and a unitriangular "
          "congruence PRESERVES it (Sylvester) -- no exact multiplicative "
          "transform can orient the residual",
          (t_mu * t_one) == sp.eye(n_mu) and t_one.det() == 1
          and t_mu.det() == 1 and e_two < 0 and in_plain == (1, 1, 2)
          and in_cong == (1, 1, 2),
          "e_2 = %.12f (cited %.12f), inertia %s -> %s"
          % (float(e_two), WARD_E2, in_plain, in_cong))
    # CCCLXII: an algebraic identity is world-blind, a discriminating fact
    ctrl = {}
    for world in ("scramble", "epstein"):
        res = msc.audit_cell(picks[184], 184, world=world,
                             thetas=list(CTRL_THETA), want_heavy=False)
        ctrl[world] = (res.refused, len(CTRL_THETA))
    fact_ctrl = 0.0
    for world in ("scramble", "epstein"):
        cell = dict(picks[184])
        _w, _h, _d, _a, _a2, rws = stage_rows(cell, list(CTRL_THETA)[:2],
                                              want_k=False)
        fact_ctrl = max(fact_ctrl, max(r["fact"] for r in rws
                                       if not r["refused"]))
    check("S6.2 CCCLXII/COMB-BLIND re-derived on this probe's own stage: the "
          "PD premise is refused by both control worlds at 8/8 offsets, "
          "while the algebraic source factorization holds regardless -- an "
          "identity that survives every world can never be the "
          "discriminating lemma",
          all(ctrl[w][0] == ctrl[w][1] for w in ctrl) and fact_ctrl < 1e-14,
          "refusals %s | factorization residual %.2e"
          % ({w: "%d/%d" % ctrl[w] for w in ctrl}, fact_ctrl))
    # CCCLXIII: T3 (no uniform floor) and T5 (explicit non-implying family)
    bn_const = mp.log(2 * mp.pi) - mp.euler
    bn_rows = []
    for n_bn in (2, 4, 8, 16, 32, 64):
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
    check("S6.3 CCCLXIII re-derived exactly: (T3) lam_min(G_N) <= "
          "(log 2pi - gamma)/N = %.10f/N, so the Baez-Duarte Gram has NO "
          "N-uniform floor and the deployed hypothesis is FALSE for N >= 3; "
          "(T5) the explicit family G~ = A A^T + (4/5)^2 I satisfies EVERY "
          "hypothesis of the certificate class at every N while d~^2 >= 1/2 "
          "forever" % float(bn_const),
          rel(bn_const, WARD_BN_CONST) < 1e-9
          and float(bn_const) / 3 < WARD_BN_CB
          and all(r[2] for r in bn_rows) and sig_hi <= WARD_BN_SIGMA_CAP
          and 1 - sig_hi >= 0.5 - 1e-12
          and abs(sig_lo - WARD_BN_SIGMA_RANGE[0]) < 5e-4
          and abs(sig_hi - WARD_BN_SIGMA_RANGE[1]) < 5e-4,
          "cap %.6f < c_B %.4f | sigma~ in [%.4f, %.4f] <= %.6f | d~^2 >= 1/2"
          % (float(bn_const) / 3, WARD_BN_CB, sig_lo, sig_hi,
             WARD_BN_SIGMA_CAP))
    # CCCLXVII: Li quadruple, cofinal dodge, Bohr sharpness, class no-go
    r_li = mp.mpf(WARD_LI_R)
    al_li = mp.sqrt(2) - 1
    th_li = 2 * mp.pi * al_li
    z_quad = (r_li * mp.expj(th_li), r_li * mp.expj(-th_li),
              mp.expj(th_li) / r_li, mp.expj(-th_li) / r_li)
    dev_li = max(abs(mp.re(sum(1 - z ** n for z in z_quad))
                     - (4 - 4 * mp.cosh(n * mp.log(r_li))
                        * mp.cos(n * th_li))) for n in range(1, 61))
    re_rho = max(float(mp.re(1 / (1 - z))) for z in z_quad)
    s_alpha = [n for n in range(1, 20001)
               if Fraction(1, 3) <= Fraction(float(mp.frac(n * al_li))
                                             ).limit_denominator(10 ** 12)
               <= Fraction(2, 3)]
    max_cos = max(float(mp.cos(n * th_li)) for n in s_alpha)
    min_lam = min(float(4 - 4 * mp.cosh(n * mp.log(r_li))
                        * mp.cos(n * th_li)) for n in s_alpha if n <= 4000)
    neg_idx = [n for n in range(1, 20001)
               if 4 - 4 * mp.cosh(n * mp.log(r_li)) * mp.cos(n * th_li) < 0]
    eps_bl = sp.Rational(1, 100)
    n_bl = sp.Symbol("n", positive=True)
    eps_s = sp.Symbol("eps", positive=True)
    c_bl_sym = sp.simplify(sp.maximum(n_bl ** 2 * sp.exp(-eps_s * n_bl),
                                      n_bl, sp.Interval(0, sp.oo)))
    c_bl = float(c_bl_sym.subs(eps_s, eps_bl))
    bohr = {}
    for k_ang in (1, 2, 3):
        angles = [2 * mp.pi * (mp.sqrt(pr) - int(mp.sqrt(pr)))
                  for pr in (2, 3, 5)[:k_ang]]
        for q_prog in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12):
            hit = None
            for n in range(q_prog, 200001, q_prog):
                if all(mp.cos(n * a) >= 0.8 for a in angles):
                    hit = n
                    break
            bohr[(k_ang, q_prog)] = hit
    check("S6.4 CCCLXVII re-derived: lambda_n of an off-line quadruple is "
          "EXACTLY 4 - 4 cosh(n log R) cos(n theta); a predeclared COFINAL "
          "index set of density 1/3 hides the off-line zero completely "
          "(so a thin Li variant is refuted, not merely unknown), the "
          "relaxation is sharp exactly at Bohr-recurrent sets, and every "
          "subexponential envelope would prove RH via Bombieri-Lagarias "
          "Cor. 1(c) with c(eps) = 4 e^-2 / eps^2",
          float(dev_li) < 1e-30
          and rel(re_rho, WARD_LI_RE_RHO) < 1e-6
          and rel(len(s_alpha) / 20000.0, WARD_LI_DENSITY) < 1e-4
          and abs(max_cos - WARD_LI_MAXCOS) < 1e-5
          and abs(min_lam - WARD_LI_MINLAM) < 1e-4
          and neg_idx[0] == WARD_LI_FIRSTNEG
          and len(neg_idx) == WARD_LI_NEGCOUNT
          and bohr[WARD_LI_BOHR[:2]] == WARD_LI_BOHR[2]
          and all(v is not None for v in bohr.values())
          and rel(c_bl, WARD_LI_BL_CONST) < 1e-6
          and all(n * n <= c_bl * math.exp(0.01 * n)
                  for n in range(1, 4001)),
          "identity dev %.1e | Re rho %.8f | density %.6f | max cos %.6f | "
          "min lambda %.5f | first neg n=%d, count %d | Bohr (3,6)->n=%s | "
          "c(1/100) = %s = %.4f"
          % (float(dev_li), re_rho, len(s_alpha) / 20000.0, max_cos, min_lam,
             neg_idx[0], len(neg_idx), bohr[(3, 6)],
             sp.nsimplify(c_bl_sym.subs(eps_s, eps_bl)), c_bl))
    # CCCLXIX: cofinal sets meet every tail -- the wall premise is immune
    tail_wit = {m: next((n for n in s_alpha if n >= m), None)
                for m in range(1, 2001)}
    check("S6.5 CCCLXIX re-derived: the very set that defeats a thin Li "
          "criterion meets EVERY tail [m, oo) with an explicit witness, so "
          "the wall's premise (whose catch set is a TAIL) is immune to that "
          "dodge -- the two quantifiers are not interchangeable",
          all(v is not None for v in tail_wit.values()),
          "2000 tails, worst witness offset %d"
          % max(tail_wit[m] - m for m in tail_wit))
    print("""
  PROVEN EMPTY for the deployed budget shape (with the section that proves it)
    E1  every magnitude hypothesis |psi(x)-x| <= f(x) sqrt(x)        [S2]
        (Chebyshev, PNT with any subpower decay, Vinogradov-Korobov,
         power saving theta < 1/2, Schoenfeld/RH, RH short interval)
    E2  every zero-density input with A > 2, and A = 2 (density
        hypothesis) and Lindeloef land exactly critical, zero slack  [S2]
    E3  Selberg's symmetry formula: provably neutral (formal identity) [S2]
    E4  every congruence reformulation, window choice, Jacobi/Cholesky
        preconditioner, resolvent split of the matrix stage           [S3]
    E5  every unsigned hull of the comb correction (flip-invariant)   [S3]
    E6  every bound consuming only {w >= 0, ||w||_inf, ||w||_2, supp} [S5]
    E7  exact multiplicative transforms (Moebius/Dirichlet): inertia
        preserving, so no orientation is created                      [S6]
    E8  natural-grammar identities (de Branges/HB, Abel, squares):
        world-blind, hence non-discriminating                         [S6]
    E9  the Beurling-Nyman/Baez-Duarte transport target: the class is
        provably non-implying (T5) and has no uniform floor (T3)       [S6]
    E10 thin/cofinal Li criteria: refuted by an explicit counterexample;
        and every subexponential Li envelope is RH-equivalent          [S6]

  MERELY UNEXPLORED (no claim of emptiness is made here)
    U1  unconditional statements about ordinate POSITIONS (Weil
        positivity, pair correlation with a signed conclusion)
    U2  alignment statements: any relation between prime positions and
        the spectral directions of K, or the sign pattern of Fhat
    U3  a different budget shape: other kernels, other frame families,
        other predeclared rung families
    U4  the four premises of the reverse implication (predeclared H_cof
        and non-interference, per-element form convergence, density,
        C0 continuation)
    U5  global inequalities that restrict the source profile beyond the
        cone (any new constraint on w that is not a size bound)""")

    # ------------------------------------------------------------------ S7
    section("S7  HONEST COUNTER-EVIDENCE (recomputed, not softened)")

    def mid(pair):
        return (mp.mpf(pair[0]) + mp.mpf(pair[1])) / 2

    s_lo, s_hi = mid(CITED_SCHUR[184]), mid(CITED_SCHUR[2854])
    p_s = float(mp.log(s_hi / s_lo) / mp.log(mp.mpf(2854) / 184))
    d_184 = mp.mpf(frames[184]["D"])
    d_2854 = mp.mpf(frames[2854]["D"])
    p_s_d2 = float(mp.log((s_hi / d_2854 ** 2) / (s_lo / d_184 ** 2))
                   / mp.log(mp.mpf(2854) / 184))
    d_1393 = mp.mpf(frames[1393]["D"])
    d_2015 = mp.mpf(frames[2015]["D"])
    p_step = float(mp.log((mid(CITED_SCHUR[2015]) / d_2015 ** 2)
                          / (mid(CITED_SCHUR[1393]) / d_1393 ** 2))
                   / mp.log(mp.mpf(2015) / 1393))
    u_glob = float(mp.log(mp.mpf(CITED_UPPER[12632])
                          / mp.mpf(CITED_UPPER[184]))
                   / mp.log(mp.mpf(12632) / 184))
    u_deep = float(mp.log(mp.mpf(CITED_UPPER[12632])
                          / mp.mpf(CITED_UPPER[5746]))
                   / mp.log(mp.mpf(12632) / 5746))
    u_prev = float(mp.log(mp.mpf(CITED_UPPER[5746])
                          / mp.mpf(CITED_UPPER[2854]))
                   / mp.log(mp.mpf(5746) / 2854))
    all_exps = (p_s, p_s_d2, p_step, u_glob, u_deep, u_prev)
    check("S7.1 NO-WITNESS stands: the certified reads are POSITIVE at all "
          "nine depths (cited, X1) and this probe adds none -- 0 negatives, "
          "0 straddles", all(mp.mpf(v) > 0 for v in CITED_UPPER.values())
          and all(mid(p) > 0 for p in CITED_SCHUR.values()),
          "deepest certified read %s at h=12632" % CITED_UPPER[12632])
    check("S7.2 the decay exponents re-derived from the cited reads and this "
          "probe's OWN frames reproduce the note exactly",
          rel(p_s, WARD_EXP_S) < 1e-7 and rel(p_s_d2, WARD_EXP_S_D2) < 1e-7
          and rel(p_step, WARD_EXP_STEP_POS) < 1e-4,
          "s ~ h^%.8f | s/D^2 ~ h^%.8f | step 1393->2015 s/D^2 exponent "
          "%+.8f (POSITIVE: the normalised drift is NOT monotone)"
          % (p_s, p_s_d2, p_step))
    check("S7.3 NO SUPER-POLYNOMIAL COLLAPSE anywhere in the re-derivable "
          "exponents: the frozen collapse bar -8.0 (the only condition "
          "under which a downward trend would be emitted) is not reached "
          "by any of the six exponents this probe recomputes",
          all(e > WARD_COLLAPSE_BAR for e in all_exps),
          "raw witness steps 2854->5746 %.5f, 5746->12632 %.5f; raw global "
          "184->12632 %.5f; s %.5f; s/D^2 %.5f; step %+.5f; bar %.1f"
          % (u_prev, u_deep, u_glob, p_s, p_s_d2, p_step,
             WARD_COLLAPSE_BAR))
    print("  FLATTENING (CITED, X7 -- NOT re-derived): the source reports the "
          "n0-NORMALISED upper-bound exponents as %.8f globally against "
          "%.8f on the deepest step 5746 -> 12632, i.e. the normalised decay "
          "FLATTENS with depth.  Rebuilding n0 at h = 5746 and 12632 is "
          "outside this probe's budget, so the normalisation is quoted, not "
          "checked.  What IS re-derived here points the same way at the "
          "level of TYPE: the normalised drift is not monotone (the "
          "certified POSITIVE s/D^2 step above), and nothing approaches the "
          "collapse bar.  In the RAW (unnormalised) witness reads the two "
          "deepest steps are %.5f then %.5f, i.e. marginally steeper -- "
          "reported because it is the direction LESS favourable to this "
          "probe's own reading." % (WARD_EXP_U_GLOBAL, WARD_EXP_U_DEEP,
                                    u_prev, u_deep))
    xs = sorted(CITED_SCHUR)
    a_sec, b_sec = xs[-2], xs[-1]
    y_a, y_b = float(mid(CITED_SCHUR[a_sec])), float(mid(CITED_SCHUR[b_sec]))
    h_star = a_sec + (0.0 - y_a) * (b_sec - a_sec) / (y_b - y_a)
    check("S7.4 the affine secant through the two deepest two-sided points "
          "does cross zero at a finite h*, and is REFUSED (as in the source) "
          "as an artefact of linearising a convex positive decay: the "
          "power-law fit never reaches zero",
          h_star > b_sec and all(mid(CITED_SCHUR[x]) > 0 for x in xs),
          "h* = %.4f (source reports 3017.0932 with its own normalisation; "
          "DIAGNOSTIC-ONLY, refused either way)" % h_star)
    disclose("S7.4 affine secant h* (DIAGNOSTIC, refused in source)",
             "%.4f" % h_star, "3017.0932")
    check("S7.5 margins strictly decreasing over the two-sided depths (the "
          "honest direction of the evidence)",
          all(mid(CITED_SCHUR[a]) > mid(CITED_SCHUR[b])
              for a, b in zip(xs, xs[1:])),
          "%d depths" % len(xs))
    print("  READING: the composite theorem is about the TYPE of the missing "
          "input and is compatible with both outcomes.  The counter-evidence "
          "above is the honest reason no one should read it as progress "
          "toward a proof: no negative read exists at any of the nine "
          "depths, the margins fall monotonically, and the normalised decay "
          "does not steepen -- on the cited normalisation it flattens at the "
          "deepest step (X7), and even in the raw reads nothing comes near "
          "the collapse bar.  A no-go about the TYPE of the missing input is "
          "not evidence about its EXISTENCE.")

    # ------------------------------------------------------------------ S8
    section("S8  NAMED OPEN SCOPE (what the theorem does NOT cover)")
    print("""  (O1) ZERO-POSITION ARGUMENTS.  Nothing here restricts arguments
       that legitimately consume information about the ordinates:
       Weil positivity itself, or any explicit-formula argument with an
       unconditional input about zero positions.  S4 shows the
       remaining statement IS of this kind; it does not show it false.
  (O2) ALIGNMENT ARGUMENTS.  S5 forbids only bounds inside I_cone.  An
       unconditional statement correlating prime positions with the
       spectral directions of K (equivalently: with the sign pattern of
       Fhat) is untouched, and is precisely what T5 says is needed.
  (O3) A DIFFERENT BUDGET SHAPE.  Every clause is proved for the
       deployed kernel K_D, the deployed frame family, and the deployed
       predeclared cofinal rung family.  Another kernel, another frame
       ladder, or another rung family is outside the statement.
  (O4) THE REVERSE IMPLICATION.  That the inequality implies RH rests
       on four named premises (predeclared H_cof and non-interference,
       per-element form convergence, density, C0 continuation).  None
       is established here; the theorem prices the FORWARD direction's
       missing input only.
  (O5) NEW GLOBAL CONSTRAINTS ON THE SOURCE.  Any inequality that
       restricts the admissible source profiles beyond {w >= 0, size,
       support} changes I_cone and thereby escapes S5.
  ALSO NOT COVERED: the theorem is finite-rung.  It is verified at
       h = 184/388/839 with the ladder to h = 12632; it makes no
       all-h claim, and asserts nothing about rungs outside the built
       cells.""")

    # ------------------------------------------------------------------ S9
    section("S9  VERDICT, TYPING, AND WHAT THE CORPUS SHOULD LATER CARRY")
    load_bearing = [n for n, ok in CHECKS if not ok
                    and not n.startswith(("S7.4",))]
    if load_bearing:
        verdict = "NOGO-COMPONENT-FAILED"
        load_bearing_fail = load_bearing
    print("  CITED, NOT RE-CHECKED (X1-X6, see the frozen spec):")
    for tag, txt in (("X1", "certified Schur intervals and witness reads "
                            "s_h / U_h at the nine depths"),
                     ("X2", "the deployed slack range 1.5e-05 .. 2.7e-03 "
                            "and the CCCXXXI alignment diagnostics"),
                     ("X3", "the classical literature constants (Rosser-"
                            "Schoenfeld, Montgomery-Vaughan, Littlewood, "
                            "Schoenfeld, Bombieri-Lagarias, Li, N(1/2,T))"),
                     ("X4", "the float64 entry slack of the wall generators"),
                     ("X5", "CCCLXVIII's F0..F4 demand totals and G_geo "
                            "(the growth FACTORS are re-derived here)"),
                     ("X6", "CCCLXII's chain measurements and CCCLXIII's "
                            "deployed constants c_B, sigma"),
                     ("X7", "the n0-normalised margin exponents (the "
                            "flattening counter-evidence); the raw ones are "
                            "recomputed here")):
        print("    %s  %s" % (tag, txt))
    print("\n  DISCLOSED DEVIATIONS (recomputed vs cited):")
    if DEVIATIONS:
        for tag, got, cited in DEVIATIONS:
            print("    %-52s got %-14s cited %s" % (tag, got, cited))
    else:
        print("    none")
    print("""
  TYPING AGAINST THE FROZEN GATE RULE.  This result is a statement ABOUT
  the problem, NOT an independent sign source.  It supplies no
  positivity, no new interval, no new certificate; it does not close or
  narrow any gate; it moves NO marker.  Its content is the localization
  of the missing input to a two-property class (signed AND alignment-
  carrying) plus the enumeration of the classes that are now provably
  empty for this budget shape.

  WHAT THE PAPERS SHOULD LATER CARRY (no file is edited in this pass).
  Suggested placement: the frontier paper's residual-obstruction
  section, as a subsection titled "The remaining obstruction is signed
  and alignment-carrying (localization)".  Suggested wording:

    "For the deployed budget shape the missing inequality is not a
     magnitude statement.  The conversion constant of any hypothesis of
     the form |psi(x) - x| <= f(x) sqrt(x) is bounded below by
     ||K_D'||_1 = 4 uniformly in D, while the geometric supply stays
     O(1); Littlewood's unconditional Omega-theorem therefore makes the
     entire magnitude class empty, with floor 4 log log log N_h against
     a slack that shrinks with depth.  The residual requirement is
     instead odd under the comb sign flip and invariant under every
     congruence of the matrix stage, so no reformulation, window choice
     or preconditioner can convert it; the signed part is exactly the
     Weil prime term of an explicit even test function, and the
     remaining statement is a zero-sum inequality against a negative
     bar.  Its unsigned companion is bounded unconditionally but its
     class floor, attained at an admissible datum, still exceeds the
     need.  Consequently any future input must be signed and must carry
     alignment information; neither a magnitude bound nor a
     world-blind grammatical identity can supply it."

  CANDIDATE LEDGER ROW (do NOT add in this pass; ledger wins on status).
    id            prime_front / obstruction typing
    display       [O]                (open, with a typed scope)
    fine type     no_go_typing       (a NEGATIVE/typing row: it prices
                                      argument classes; it is NOT an
                                      evidence row and NOT a closure)
    claim         "the residual requirement for the deployed budget
                   shape is signed and alignment-carrying; the
                   magnitude, unsigned-hull, congruence-reformulation
                   and world-blind-identity classes are empty"
    status        no marker moved; supersedes nothing; narrows no gate
    depends on    the CCCLIX/CCCLXVI/CCCLXVIII/CCCLXXI/CCCLXXII chain
    anti-double-counting: it must NOT be counted as evidence for or
                   against RH, and must not be cited as support for any
                   positivity claim.

  DOES IT MERIT A verification/ MODULE?  Yes for the exact, cheap,
  self-contained core; no for the whole probe.  Recommended split:
    PROMOTE  the exact kernel ledger (S1: six symbolic identities),
             the congruence-invariance and parity of the three-term
             split (S3.1-S3.4), the Selberg neutrality (S2.13), the
             Littlewood floor vs supply comparison (S2.9/S2.10) and
             the exact Beurling-Nyman T3/T5 witnesses (S6.3).  These
             are deterministic, second-scale, exact-arithmetic facts
             with no float64 premise; they would carry a \\veri{}
             citation for the localization subsection.
    KEEP OUT the deployed matrix-stage reads (S3.5-S3.12, S4, S5) --
             they inherit the float64 entry-slack premise (X4) and the
             cited certified ladder (X1), so they belong in
             experiments/ until that premise is discharged.
  A single verification module named after the localization (not after
  a positivity result) would be the correct shape; it must be typed as
  a NO-GO/typing module so that no gate reads it as progress.""")

    elapsed = time.time() - T0
    check("V1 runtime below the frozen bar", elapsed < RUNTIME_BAR,
          "%.3f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    if failed and verdict == "NOGO-COMPOSITE-VERIFIED":
        verdict = "NOGO-COMPONENT-FAILED"
    print("\n[SUMMARY] %d/%d checks pass | failed=%s | %.3f s | VERDICT %s"
          % (len(CHECKS) - len(failed), len(CHECKS),
             failed if failed else "none", elapsed, verdict))
    if load_bearing_fail:
        print("[HIGH] load-bearing components did not re-verify: %s"
              % load_bearing_fail)
    print("NO RH CLAIM.  No positivity claim.  Nothing promoted.  No marker "
          "moved.")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
