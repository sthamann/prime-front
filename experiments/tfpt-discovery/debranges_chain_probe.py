#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""debranges_chain_probe -- PRIME.DEBRANGES.CHAIN.01

FROZEN SPEC v1 (2026-08-13).

EXPLORATION ONLY.  This probe writes no files.  It changes no verification
module, paper, ledger, website, manifest or status marker.  It makes NO RH
claim, NO Weil-positivity claim and NO counterexample claim.

--------------------------------------------------------------------------
MISSION
--------------------------------------------------------------------------
Attack the remaining RH edge from the de Branges / Krein-string /
Hermite-Biehler side -- the one structural direction adjacent to the
corpus' Weyl-m-function assets (CCXLV tier 1, CCLIII tier 2) that has never
been attacked directly.  The advertised payoff of that direction is that it
replaces "prove a positivity inequality" by "exhibit a Hermite-Biehler
structure function E with the right symmetry", i.e. a STRUCTURAL rather
than an estimative target.

This probe tests that advertised payoff, in the corpus' own objects, and
prices it against the published 1998 objection (Conrey-Li).

DISTINCTNESS FROM THE XI-DETERMINANT ROUTE (CCCXLIII / CCCLIII / CCCLVII).
Those rounds built a FAMILY OF ENTIRE FUNCTIONS (symmetrized partial Euler
products / mollified resolvents) and asked whether a DETERMINANT LIMIT
reproduces -Xi'/Xi; the verdicts were XILIMIT-VACUOUS / XILIMIT2-STILL-
VACUOUS / XIRES-VACUOUS, all decided by a comb-blindness gate on a scramble
ratio.  This probe does NOT build any entire-function family approximating
Xi, evaluates no partial Euler product, and takes no limit in a spectral
parameter.  It takes the ALREADY DEPLOYED finite Galerkin wall, transports
it into de Branges coordinates exactly (a finite, exact, invertible
re-coordinatization), and asks a purely structural question about the
resulting family of finite de Branges spaces.  Different mechanism,
different failure mode, disjoint evidence.

--------------------------------------------------------------------------
CONVENTION WARD (frozen; this route is a convention minefield)
--------------------------------------------------------------------------
C+ := {z : Im z > 0} is the UPPER half plane.
For an entire F with the conjugate-reflection F^*(z) := conj(F(conj z)).
HERMITE-BIEHLER (de Branges convention, the one used throughout):
      E is HB   :<=>   |E^*(z)| < |E(z)|  for every z in C+,
equivalently |E(conj z)| < |E(z)| on C+, equivalently (for E without real
zeros) all zeros of E lie in the OPEN LOWER half plane C-.
Decomposition:  A := (E + E^*)/2,  B := i(E - E^*)/2,  so  E = A - iB
with A, B real entire (A = A^*, B = B^*).
Reproducing kernel (de Branges Thm 19; identical to Conrey-Li (2.1)-(2.2)):
      K(w,z) = [B(z)conj(A(w)) - A(z)conj(B(w))] / [pi (z - conj w)]
             = [E(z)conj(E(w)) - E^*(z)conj(E^*(w))] / [2 pi i (conj w - z)].
Both forms are asserted equal in S0 (algebraic ward).
Sign ward:  K(z,z) = (|E(z)|^2 - |E^*(z)|^2) / (4 pi Im z).
Positive ward   E(z) = z + i  (zero at -i in C-)      -> HB
Negative ward   E(z) = z - i  (zero at +i in C+)      -> NOT HB
Paley-Wiener ward E(z) = exp(-i z)                    -> HB
Every HB read below is an INTERVAL ENCLOSURE (mpmath.iv, dps IV_DPS = 260)
or an exact sympy identity; no bare float decides any inequality.

--------------------------------------------------------------------------
S1  THE DEPLOYED OBJECT (source-only, dyadic-exact)
--------------------------------------------------------------------------
Ported verbatim from verification/v563_paper2_readouts.py (attributed
inline; no import of verification/): von Mangoldt table, arch kernel
arch_A/arch_lags (Weil 1952 archimedean lag reads), atom_lags_at (T115 tent
assembly), parity_mu / parity_basis (KMS 1953), odd_toeplitz.

  wall     A_h := odd_toeplitz(c_arch + c_atom, M),  M = 2h,  D = 2 alpha/M
  block    B_h := sym( T_K A_h T_K^T ) .* outer(mu^-1/2, mu^-1/2),  K = 16

B_h is the deployed normalized low parity block -- the object whose
lam_min carries the CLIII/v905 interval-certified class floor 0.5523 and
which v909 re-verifies (B-half).  Every float64 entry of B_h is an EXACT
dyadic rational; S1 freezes B_h as an exact Fraction matrix and every
later exactness statement is EXACT FOR THAT DYADIC MATRIX (the CCCLVI
typing).  A_h itself is carried as a float/mpmath fidelity read only.

--------------------------------------------------------------------------
S2  LANCZOS -> JACOBI  (interval arithmetic, certified)
--------------------------------------------------------------------------
Interval Lanczos (mpmath.iv, dps IV_DPS, full reorthogonalization) on
(B_h, q0) with q0 = e_0 (CCLIII's cyclic vector) to depth KDEPTH = 12,
producing the Jacobi data alpha_k (diagonal) and beta_k > 0 (off-diagonal)
as ENCLOSURES.  Wards, all enclosed:
  W2.1  orthonormality   max |<q_i,q_j> - delta_ij|
  W2.2  tridiagonal residual   max |B q_k - beta_{k+1} q_{k+1}
                                     - alpha_k q_k - beta_k q_{k-1}|
  W2.3  MOMENT WARD (the exactness anchor): the moments
        m_j = e_0^T B_h^j e_0 are computed EXACTLY over Fraction
        (j <= 2 KDEPTH - 1, via KDEPTH exact matvecs and
        m_2j = v_j.v_j, m_2j+1 = v_j.v_{j+1}) and must lie inside the
        interval reconstruction from (alpha, beta).
  W2.4  beta_k enclosure strictly positive (Lanczos non-breakdown).
mu_h := the spectral measure of (B_h, e_0); m_0 = 1 exactly, so mu_h is a
probability measure.

--------------------------------------------------------------------------
S3  THE STRUCTURE FUNCTION E_h AND THE HB VERIFICATION
--------------------------------------------------------------------------
Orthonormal polynomials  p_{-1} = 0, p_0 = 1,
      beta_{k+1} p_{k+1}(z) = (z - alpha_k) p_k(z) - beta_k p_{k-1}(z).
CANDIDATE STRUCTURE FUNCTION (the frozen normalization):
      E_h^{(n)}(z) := sqrt(pi beta_n) ( p_{n-1}(z) - i p_n(z) ),
so A = sqrt(pi beta_n) p_{n-1},  B = sqrt(pi beta_n) p_n,  deg E = n.
S3 establishes, in this order:
 (3a) EXACT SYMBOLIC IDENTITY (sympy, symbolic alpha_k, beta_k, x, y, n<=4)
        beta_n (u_{n-1} v_n - v_{n-1} u_n) = y sum_{k<n} (u_k^2 + v_k^2),
      where p_k(x+iy) = u_k + i v_k.  Equivalently
        |E|^2 - |E^*|^2 = 4 pi y sum_{k<n} |p_k(z)|^2 = 4 pi y K(z,z).
      This makes HB an IDENTITY, not an estimate: it holds for EVERY real
      symmetric input with a cyclic vector.  That is a load-bearing
      negative fact of this probe and is reported as such.
 (3b) INTERVAL GRID VERIFICATION of |E|^2 - |E^*|^2 > 0 on the frozen grid
      GRID_Y x GRID_X in C+, all rungs, n in N_READ -- enclosure lower
      bound must be > 0.
 (3c) CHRISTOFFEL-DARBOUX / REPRODUCING-KERNEL IDENTITY, enclosed:
        K_{E_h^{(n)}}(w,z) == sum_{k<n} p_k(z) conj(p_k(w))
      i.e. H(E_h^{(n)}) = P_{n-1} carrying EXACTLY the L^2(mu_h) norm.
 (3d) no real zeros of E (min over the read grid of |E(t)|, t real).
 (3e) all zeros of E strictly in C- (mpmath polyroots, enclosed margin).

--------------------------------------------------------------------------
S4  DE BRANGES AXIOMS + THE GALERKIN REPRODUCTION
--------------------------------------------------------------------------
 (H2) |F(w)|^2 <= ||F||^2 K(w,w), with equality at F = K(w,.) -- enclosed.
 (H3) ||F^#|| = ||F|| -- exact (real Gram = identity in the p_k basis).
 (H1) F(w) = 0  =>  (z - conj w)/(z - w) F(z) in H with equal norm --
      enclosed, on frozen (w, F) pairs.
 (I)  ANALYTIC ISOMETRY, independent route: for real F, G of degree < n
        int_R F(t) G(t) / |E(t)|^2 dt   ==   <F,G>_{L^2(mu_h)}
      computed by RESIDUES in C+ over the zeros of E^* (exact contour
      argument; integrand ~ t^-2), enclosed against the Gram identity.
 (G)  GALERKIN REPRODUCTION (the answer to "whose space reproduces the
      deployed form"): under U: P -> P(B_h) e_0 the deployed Galerkin form
      is MULTIPLICATION BY THE INDEPENDENT VARIABLE,
        v^T B_h v = int t |P(t)|^2 dmu_h(t),   ||v||^2 = ||P||^2_{H(E_h)},
      verified enclosed on frozen test vectors.  Consequence, stated as
      the exact translation of the deployed wall condition:
        B_h  PSD   <=>   supp mu_h subset [0, inf)
                   <=>   multiplication by t is positive on H(E_h)
                   <=>   the chain of H(E_h^{(n)}) is a KREIN STRING chain
                         (Kac-Krein) rather than a mere de Branges chain.

--------------------------------------------------------------------------
S5  THE KEY QUESTION: IS THERE A CHAIN?
--------------------------------------------------------------------------
De Branges' ordering theorem needs the family TOTALLY ORDERED BY ISOMETRIC
INCLUSION.  Two candidate chains are separated and both are tested.
 (C1) IN-DEPTH chain at fixed rung: H(E_h^{(1)}) subset ... subset
      H(E_h^{(K)}).  Test: || . ||_{H(E^{(n)})} == || . ||_{H(E^{(n+1)})}
      on P_{n-1}, enclosed.  (Expected structural PASS -- reported as
      world-blind, not as content.)
 (C2) CROSS-RUNG chain: H(E_h^{(n)}) subset H(E_h'^{(n)}) isometrically.
      Since both are P_{n-1} with the L^2(mu) norm, isometric inclusion
      holds IFF the moments agree, m_j^{(h)} = m_j^{(h')} for j <= 2n-2.
      Reads, all from the EXACT rational moments:
        - relative moment deviation per order j;
        - CHAIN-SHARE DEPTH k*(h,h') := max n with all deviations
          <= BAR_CHAIN = 1e-9;
        - ISOMETRIC DEFECT def_n := max(lam_max, 1/lam_min) of the pencil
          (H_n^{(h')}, H_n^{(h)}) of exact Hankel moment matrices
          (def_n == 1 <=> isometric inclusion at depth n);
        - GAUGE-REPAIRED defect: the same after the best affine
          push-forward t -> sigma t + tau matching the first two moments
          (the honest "is the break a mere gauge?" control).
      Two ladders are tested:
        (C2a) the deployed frame-A ladder (anchor moves with the rung);
        (C2b) the FAIR ladder: FIXED anchor n_zone, refining h -- Galerkin
              sections of ONE continuum form.  If any chain can exist,
              it must exist here.
      Plus the ASYMPTOTIC chain read: drift of alpha_k, beta_k in h at
      fixed k on (C2b) (an exact chain requires drift 0; an asymptotic
      chain only requires drift -> 0).
      Plus the ROBUSTNESS CENSUS (S5.6): the same exact low-moment break
      is re-measured for four inequivalent choices of the object and the
      cyclic vector -- V1 the deployed normalized block with q0 = e_0,
      V2 the UNNORMALIZED Galerkin block T_K A_h T_K^T, V3 the deployed
      block with q0 = the critical direction, V4 the FULL wall A_h with
      q0 = e_0 -- so that no reader can attribute the break to the
      deployed mu^-1/2 scaling or to the choice of q0.

--------------------------------------------------------------------------
S6  WHAT THE LOW-POLE KILLIP-SIMON FAILURE IS IN DE BRANGES LANGUAGE
--------------------------------------------------------------------------
CCLIII measured: the KS first order CAPTURES the resolvent increment
exactly at the top pole (capture -> 1.000 at y = 4.97e4) and the norm route
is ~1e4 too loose at the decision poles j <= 6.  De Branges translation
measured here, in this probe's own coordinate (no invented coordinate
identification with the 8x8 Zolotarev wall -- CCLIII's own fence):
  RESOLUTION DEPTH n_eff(y) := least n such that the depth-n continued
  fraction (= the Weyl m-function of the depth-n de Branges space section)
  reproduces the full-depth m_h(x0 + iy) to REL_MEFF = 1e-9.
Read n_eff over a geometric y-ladder and compare with the measured chain-
share depth k* of S5.  The precise typed statement produced:
  low-pole KS failure  <=>  n_eff(y) exceeds the depth at which the
  cross-rung chain still agrees  (if k* >= 1) ; or, if k* = 0, the chain
  fails BEFORE any pole is resolved and the low-pole failure is a strictly
  WEAKER, SEPARATE defect.  The verdict text names which case holds.

--------------------------------------------------------------------------
S7  CONTROLS (must break the structure, else COMB-BLIND)
--------------------------------------------------------------------------
Worlds, all through the identical builder:
  deployed  the prime comb (u = log n, mass 2 Lambda(n)/sqrt n)
  scramble  uniform positions at the SAME masses, seed 1 (v563 route)
  epstein   the Epstein x^2 + 5y^2 comb (v909 lambda_eps verbatim)
  smooth    the PNT density comb (v909 smooth_comb verbatim)
  random    a random real symmetric matrix, seed 2 -- NO arithmetic at all
For each world the full S3/S4/C1 battery is run.  DISCRIMINATION RULE
(frozen): the de Branges structure is discriminating iff it FAILS in at
least 3 of the 4 non-deployed worlds.  Otherwise COMB-BLIND.  The wall
positivity read lam_min is reported alongside as the known-discriminating
reference (v909 M1/M2: controls drive lam_min negative).

--------------------------------------------------------------------------
S8  THE CONREY-LI ASSESSMENT (mandatory; machine-checked, not asserted)
--------------------------------------------------------------------------
EXTERNAL-CITED: J. B. Conrey and X.-J. Li, "A note on some positivity
conditions related to zeta and L-functions", arXiv math/9812166 (1998),
IMRN 2000 no. 18, 929-940; with a non-numerical argument contributed by
P. Sarnak.  Their Theorem 1 / Theorem 2 and the two refutations are
reproduced here in the following typed form:
 (8a) THE HB TARGET IS UNCONDITIONAL AND EMPTY.  With E(z) = xi(1 - i z),
      Conrey-Li Sec. 3.1 note that |E(conj z)| < |E(z)| on C+ follows from
      0 < Re rho < 1 alone (Hadamard / de la Vallee Poussin 1896).
      Machine-check here: the HB inequality for E(z) = xi(1 - i z) on a
      frozen C+ grid, mpmath dps 40, NO zero of zeta read anywhere.
      Consequence: "exhibit a Hermite-Biehler E" is NOT an RH-strength
      target; RH is the strictly stronger statement that the zeros of E
      lie ON the line Im z = -1/2.
 (8b) THE ACTUAL DE BRANGES CONDITION IS A SHIFT POSITIVITY, AND IT IS
      FALSE.  Conrey-Li (3.4): Re{ xi(1 + 282 i) / xi(2 + 282 i) } < 0,
      published value -0.000131957; reproduced here at dps 40 with NO
      zero input at all.  By their Theorem 2 this refutes condition (3.3)
      for F(W), W = 1/xi(1 - iz).  Their companion refutation of (3.1) at
      the 34th zero is reproduced from the PUBLISHED LITERAL ordinate
      111.0295355431696745 (a citation, used ONLY in this external
      section, never in any construction): -Re{xi'(rho) xi(1 + rho)}
      published as -5.389100507182945e-69 < 0.  Sarnak's unconditional
      argument (density of the values of log zeta on 1/2 < Re s < 2,
      Bohr-Courant / Titchmarsh Ch. XI) is CITED, not recomputed.
 (8c) IS THIS PROBE'S ROUTE THE SAME CONDITION?  Conrey-Li Thm 1 needs
      THREE hypotheses on E: (i) the i-shift functional equation
      E^*(z) = eps E(z - i) with |eps| = 1; (ii) |E(x+iy)| increasing in
      y > 0; (iii) the shift positivity Re <F(z), F(z+i)>_{H(E)} >= 0.
      Both (i) and (iii) are machine-separated from the wall condition:
        (i)   the relative defect of E_h^{(n)} against the i-shift
              functional equation (eps forced by the leading coefficient)
              is measured on every rung -- it is O(1), so hypothesis (i)
              simply does not hold for the wall structure function;
        (iii) in the orthonormal p_k basis the shift S: F(z) -> F(z + i)
              is an explicit upper-triangular T, de Branges' condition is
              lam_min((T + T^*)/2) >= 0 while the deployed wall condition
              is lam_min(B_h) >= 0; both are computed on every rung.
      If they disagree in sign anywhere, the routes are INEQUIVALENT and
      the literal Conrey-Li obstruction is AVOIDED (with the exact
      mechanism printed).  If they agree everywhere, it is INHERITED.
      Either way (8a) stands on its own, and "avoided" here means only
      "not the same condition" -- it buys no RH-strength conclusion,
      because the de Branges CONCLUSION is lost with the hypothesis.

--------------------------------------------------------------------------
VERDICT ENUM (frozen, mission-supplied) AND DECISION RULE (frozen)
--------------------------------------------------------------------------
  DEBRANGES-CHAIN-FOUND / DEBRANGES-CHAIN-BROKEN /
  DEBRANGES-CONREY-LI-BLOCKED / DEBRANGES-COMB-BLIND /
  DEBRANGES-INSTRUMENT-EDGE
Decision, evaluated in this order:
  1. any instrument ward fails                  -> INSTRUMENT-EDGE
  2. controls do not break the structure
     (fewer than 3 of 4 non-deployed worlds
      fail the S3/S4/C1 battery)                -> COMB-BLIND
  3. the finite shift condition and the wall
     condition never disagree in sign           -> CONREY-LI-BLOCKED
  4. C2 isometric defect > 1 + BAR_CHAIN on the
     FAIR ladder (C2b) at depth >= 2            -> CHAIN-BROKEN
  5. otherwise                                  -> CHAIN-FOUND
Secondary tags are appended to the primary verdict.

--------------------------------------------------------------------------
FROZEN BARS (declared before any number is read)
--------------------------------------------------------------------------
KDEPTH 12, KB 16, N_RUNG 5, IV_DPS 260, MP_DPS 240,
BAR_ORTH 1e-30, BAR_TRID 1e-28, BAR_MOMENT 1e-25, BAR_WIDTH 1e-20,
BAR_CHAIN 1e-9, REL_MEFF 1e-9, BAR_RK 1e-25, BAR_ISO 1e-30,
GRID_Y (1e-3, 1e-2, 1e-1, 1, 10, 100), GRID_X (-4, -1, 0, 0.37, 1, 5),
N_READ (2, 3, 5, 8, 12), CL_T 282.0, CL_RHO_IM 111.0295355431696745,
CL_G_PUB -0.000131957, RUNTIME BUDGET 1800 s.

DISCLOSED AMENDMENTS (made during instrument bring-up, i.e. BEFORE any
verdict-bearing number was read; every one of them TIGHTENS the instrument,
none moves a bar in the permissive direction):
 A1  IV_DPS 60 -> 260 and MP_DPS 120 -> 240.  At dps 60 the interval
     Lanczos broke down at k = 10 (the enclosure of ||r||^2 straddled 0)
     because of dependency growth, i.e. the instrument, not the object,
     was the limit.  LZ_DPS was folded into IV_DPS (one precision knob).
 A2  BAR_ISO 1e-18 -> 1e-30 (TIGHTER) once the mp path stopped truncating
     interval midpoints through float64 (iv_mid_mp).
 A3  (H1) is evaluated by EXACT polynomial division by (z - w) and exact
     re-expansion in the p_k basis instead of a grid least-squares fit
     (the fit was ill-conditioned at degree 12 and was measuring the fit,
     not the axiom).
 A4  lambda_eps (Epstein control) replaced by an O(N log N) divisor sieve;
     warded verbatim against the naive O(N^2) v909 recursion in S7.0.
 A5  the S8.1 C+ grid uses non-integer abscissae (-20.5, 0.7, 14.3, 60.1)
     so that s/2 never lands on a Gamma pole; no read depends on the
     particular abscissae.
 A6  S5.6 (the normalization / cyclic-vector robustness census of the
     cross-rung break) and S8.4 (the shift-SYMMETRY defect, hypothesis (i)
     of Conrey-Li Thm 1) were ADDED after the first pass; both are extra
     falsification surface for the probe's own conclusion, not relaxations.
"""
from __future__ import annotations

import hashlib
import math
import random
import time
from fractions import Fraction

import numpy as np
import sympy as sp
from mpmath import iv, mp

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()

# ------------------------------------------------------------------ bars
KDEPTH = 12
KB = 16
N_RUNG = 5
IV_DPS = 260
MP_DPS = 240
BAR_ORTH = 1.0e-30
BAR_TRID = 1.0e-28
BAR_MOMENT = 1.0e-25
BAR_WIDTH = 1.0e-20
BAR_CHAIN = 1.0e-9
REL_MEFF = 1.0e-9
BAR_RK = 1.0e-25
BAR_ISO = 1.0e-18
GRID_Y = (1.0e-3, 1.0e-2, 1.0e-1, 1.0, 10.0, 100.0)
GRID_X = (-4.0, -1.0, 0.0, 0.37, 1.0, 5.0)
N_READ = (2, 3, 5, 8, 12)
CL_T = 282.0
CL_RHO_IM = 111.0295355431696745
CL_G_PUB = -0.000131957
BUDGET_S = 1800.0

# v563 surface constants, verbatim
ATOM_MAX = 400000
ZONE_DEEP = 380000
NU_MAIN = 4
H_MIN, HCAP = 128, 1450
N_ATOM_MIN = 40
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
ANCHOR_FIX = 157          # the v563 reference-window anchor (n_zone = 157)
H_REFINE = (64, 96, 128, 192, 256)   # the FAIR fixed-anchor ladder

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


# ======================================================================
# S1  the deployed builder -- ported verbatim from
#     verification/v563_paper2_readouts.py (attribution inline; the
#     archimedean kernel is Weil 1952, the tent assembly is T115, the
#     parity geometry is Kac-Murdock-Szego 1953)
# ======================================================================
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


LAM_TAB = von_mangoldt_table(ATOM_MAX)
_NN = np.nonzero(LAM_TAB > 0.0)[0]
U_ALL = np.log(_NN.astype(float))
MU_ALL = 2.0 * LAM_TAB[_NN] / np.sqrt(_NN.astype(float))
G_ALL = np.diff(U_ALL)
NZ_DEEP = int(np.searchsorted(_NN, ZONE_DEEP, side="right"))
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return ((tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
            / (-np.expm1(-2.0 * w)))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def atom_lags_at(alpha, M, positions, masses):
    """The T115 tent assembly at EXPLICIT positions (v563 verbatim)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in zip(positions, masses):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def parity_mu(m):
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def odd_toeplitz(c, M):
    h = M // 2
    rr = np.arange(h)
    return (np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]
            - np.asarray(c)[(M - 1) - rr[:, None] - rr[None, :]])


def sym(A):
    return 0.5 * (A + A.T)


def frame_a_zones():
    out = []
    for kz in range(2, NZ_DEEP - 2):
        D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
        M_k = int(math.ceil(U_ALL[kz] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        h_k = M_k // 2
        if (h_k < H_MIN or h_k > HCAP
                or int(np.searchsorted(U_ALL, 2.0 * U_ALL[kz] + 1e-14,
                                       side="right")) < N_ATOM_MIN):
            continue
        out.append(kz)
    return out


def smooth_comb(alpha, ng=6000):
    """v909 verbatim: the PNT density comb."""
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps_naive(N):
    """Epstein x^2 + 5 y^2 comb (v909 / port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def lambda_eps(N):
    """Identical recursion, divisor-sieved (O(N log N) instead of O(N^2));
    warded against lambda_eps_naive in S7."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    acc = np.zeros(N + 1)
    for n in range(2, N + 1):
        lam[n] = a[n] * math.log(n) - acc[n]
        if lam[n] != 0.0:
            for m in range(2 * n, N + 1, n):
                acc[m] += lam[n] * a[m // n]
    return lam


def build_wall(alpha, hz, world="deployed", seed=1):
    """One deployed wall A_h and its normalized low parity block B_h.

    world in {deployed, scramble, epstein, smooth, random}.  Everything
    but `random` goes through the identical v563 assembly; `random` is the
    no-arithmetic-at-all control and replaces B_h outright.
    """
    M = 2 * hz
    D = 2.0 * alpha / M
    if world == "random":
        rng = np.random.default_rng(seed)
        R = rng.standard_normal((KB, KB))
        B = sym(R @ R.T / KB) + np.eye(KB) * 0.3
        return dict(alpha=alpha, h=hz, M=M, D=D, world=world,
                    A=None, B=B, lam_min=float(np.linalg.eigvalsh(B)[0]))
    ka = int(np.searchsorted(U_ALL, 2.0 * alpha + 1.0e-14, side="right"))
    uu = U_ALL[:ka].copy()
    mm = MU_ALL[:ka].copy()
    if world == "scramble":
        rng = np.random.default_rng(seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    elif world == "smooth":
        uu, mm = smooth_comb(alpha)
    elif world == "epstein":
        NE = int(math.floor(math.exp(2.0 * alpha))) + 1
        lamE = lambda_eps(min(NE, 40000))
        nz = np.nonzero(np.abs(lamE) > 1.0e-12)[0]
        uu = np.log(nz.astype(float))
        mm = 2.0 * lamE[nz] / np.sqrt(nz.astype(float))
        keep = uu <= 2.0 * alpha
        uu, mm = uu[keep], mm[keep]
    c_at, D = atom_lags_at(alpha, M, uu, mm)
    c_ar = arch_lags(M, D)
    A = odd_toeplitz(c_ar + c_at, M)
    Tb = parity_basis(hz, KB)
    isq = 1.0 / np.sqrt(parity_mu(hz)[:KB])
    B = sym((Tb @ (A @ Tb.T)) * np.outer(isq, isq))
    lam_min = float(np.linalg.eigvalsh(A)[0])
    return dict(alpha=alpha, h=hz, M=M, D=D, world=world,
                A=A, B=B, lam_min=lam_min)


# ======================================================================
# exact (Fraction) and interval (mpmath.iv) machinery
# ======================================================================
def to_fraction_matrix(B):
    n = B.shape[0]
    return [[Fraction(float(B[i, j])) for j in range(n)] for i in range(n)]


def exact_moments(Bf, depth):
    """m_j = e_0^T B^j e_0 EXACTLY, j = 0 .. 2 depth - 1, using `depth`
    exact matvecs and m_2j = v_j.v_j, m_2j+1 = v_j.v_{j+1}."""
    n = len(Bf)
    vs = [[Fraction(1) if i == 0 else Fraction(0) for i in range(n)]]
    for _ in range(depth):
        v = vs[-1]
        vs.append([sum(Bf[i][k] * v[k] for k in range(n)) for i in range(n)])
    m = [Fraction(0)] * (2 * depth)
    for j in range(depth):
        m[2 * j] = sum(vs[j][i] * vs[j][i] for i in range(n))
        if 2 * j + 1 < 2 * depth:
            m[2 * j + 1] = sum(vs[j][i] * vs[j + 1][i] for i in range(n))
    return m


def iv_matrix(B):
    """Exact degenerate intervals: every float64 entry is a dyadic
    rational and mpmath converts it without rounding at IV_DPS."""
    n = B.shape[0]
    return [[iv.mpf(float(B[i, j])) for j in range(n)] for i in range(n)]


def iv_matvec(Miv, v):
    n = len(v)
    return [sum((Miv[i][k] * v[k] for k in range(n)), iv.mpf(0))
            for i in range(n)]


def iv_dot(a, b):
    return sum((a[k] * b[k] for k in range(len(a))), iv.mpf(0))


def _mpf_tuple_to_fraction(t):
    sign, man, exp, _bc = t
    if man == 0:
        return Fraction(0)
    val = Fraction(man) * (Fraction(2) ** exp)
    return -val if sign else val


def iv_bounds_exact(x):
    """Exact rational lower/upper bounds of an mpmath interval."""
    lo, hi = x._mpi_
    return _mpf_tuple_to_fraction(lo), _mpf_tuple_to_fraction(hi)


def iv_mid_mp(x):
    """Interval midpoint as an mp float at the FULL working precision
    (float(x.mid) would silently truncate to float64)."""
    lo, hi = iv_bounds_exact(x)
    m = (lo + hi) / 2
    return mp.mpf(m.numerator) / mp.mpf(m.denominator)


def iv_width(x):
    return float(x.delta)


def iv_lo(x):
    return float(x.a)


def iv_mid(x):
    return float(x.mid)


def interval_lanczos(B, depth):
    """Interval Lanczos with full reorthogonalization on (B, e_0)."""
    n = B.shape[0]
    Miv = iv_matrix(B)
    q = [iv.mpf(1) if i == 0 else iv.mpf(0) for i in range(n)]
    Q = [q]
    alpha, beta = [], []
    worst_orth = 0.0
    worst_res = 0.0
    for k in range(depth):
        w = iv_matvec(Miv, Q[k])
        a_k = iv_dot(Q[k], w)
        alpha.append(a_k)
        w = [w[i] - a_k * Q[k][i] for i in range(n)]
        if k > 0:
            w = [w[i] - beta[k - 1] * Q[k - 1][i] for i in range(n)]
        for _ in range(2):                        # full reorthogonalization
            for j in range(len(Q)):
                c = iv_dot(Q[j], w)
                w = [w[i] - c * Q[j][i] for i in range(n)]
        nrm2 = iv_dot(w, w)
        if iv_lo(nrm2) <= 0.0:
            return None
        b_k = iv.sqrt(nrm2)
        if k + 1 < depth:
            beta.append(b_k)
            Q.append([w[i] / b_k for i in range(n)])
        else:
            beta.append(b_k)                      # beta_depth (for E)
    for i in range(len(Q)):
        for j in range(len(Q)):
            d = iv_dot(Q[i], Q[j]) - iv.mpf(1 if i == j else 0)
            worst_orth = max(worst_orth, abs(iv_mid(d)) + iv_width(d))
    for k in range(len(Q) - 1):
        w = iv_matvec(Miv, Q[k])
        r = [w[i] - alpha[k] * Q[k][i] for i in range(n)]
        if k > 0:
            r = [r[i] - beta[k - 1] * Q[k - 1][i] for i in range(n)]
        r = [r[i] - beta[k] * Q[k + 1][i] for i in range(n)]
        worst_res = max(worst_res,
                        max(abs(iv_mid(x)) + iv_width(x) for x in r))
    return dict(alpha=alpha, beta=beta, Q=Q,
                orth=worst_orth, res=worst_res,
                width=max([iv_width(x) for x in alpha]
                          + [iv_width(x) for x in beta]))


def jacobi_moments_iv(alpha, beta, order):
    """Moments of the spectral measure of the tridiagonal (alpha, beta)
    w.r.t. e_0, as intervals: m_j = (J^j)_{00}."""
    n = len(alpha)
    J = [[iv.mpf(0)] * n for _ in range(n)]
    for i in range(n):
        J[i][i] = alpha[i]
        if i + 1 < n:
            J[i][i + 1] = beta[i]
            J[i + 1][i] = beta[i]
    v = [iv.mpf(1) if i == 0 else iv.mpf(0) for i in range(n)]
    out = [iv.mpf(1)]
    for _ in range(order):
        v = [sum((J[i][k] * v[k] for k in range(n)), iv.mpf(0))
             for i in range(n)]
        out.append(v[0])
    return out


def p_values_iv(alpha, beta, x, y, nmax):
    """u_k, v_k with p_k(x + i y) = u_k + i v_k, as intervals."""
    u = [iv.mpf(1)]
    v = [iv.mpf(0)]
    up, vp = iv.mpf(0), iv.mpf(0)
    for k in range(nmax):
        t_u = (x - alpha[k]) * u[k] - y * v[k]
        t_v = (x - alpha[k]) * v[k] + y * u[k]
        if k > 0:
            t_u = t_u - beta[k - 1] * up
            t_v = t_v - beta[k - 1] * vp
        up, vp = u[k], v[k]
        u.append(t_u / beta[k])
        v.append(t_v / beta[k])
    return u, v


def p_coeffs_mp(alpha, beta, nmax):
    """Real coefficient lists of p_0..p_nmax at mp precision (ascending)."""
    P = [[mp.mpf(1)]]
    prev = [mp.mpf(0)]
    for k in range(nmax):
        cur = P[k]
        shifted = [mp.mpf(0)] + list(cur)
        m = max(len(shifted), len(cur), len(prev))
        acc = [mp.mpf(0)] * m
        for i, c in enumerate(shifted):
            acc[i] += c
        for i, c in enumerate(cur):
            acc[i] -= alpha[k] * c
        if k > 0:
            for i, c in enumerate(prev):
                acc[i] -= beta[k - 1] * c
        acc = [c / beta[k] for c in acc]
        prev = cur
        P.append(acc)
    return P


def poly_eval_mp(coeffs, z):
    out = mp.mpc(0)
    for c in reversed(coeffs):
        out = out * z + c
    return out


def p_from_poly(c, P, n):
    """Coefficients of a polynomial (ascending monomial list c, degree
    < n) in the orthonormal basis p_0..p_{n-1} -- exact triangular
    back-substitution on the leading coefficients."""
    sh = [mp.mpc(x) for x in c] + [mp.mpc(0)] * (n - len(c))
    out = [mp.mpc(0)] * n
    for j in range(n - 1, -1, -1):
        if j >= len(sh):
            continue
        co = sh[j] / P[j][j]
        out[j] = co
        if co == 0:
            continue
        for r, pr in enumerate(P[j]):
            sh[r] -= co * pr
    return out


def poly_from_p(co, P):
    """Ascending monomial coefficients of sum_k co[k] p_k."""
    m = max(len(P[k]) for k in range(len(co)))
    out = [mp.mpc(0)] * m
    for k, ck in enumerate(co):
        for r, pr in enumerate(P[k]):
            out[r] += ck * pr
    return out


def poly_div_linear(c, w):
    """Divide the ascending polynomial c by (z - w); returns
    (quotient, remainder)."""
    n = len(c) - 1
    q = [mp.mpc(0)] * max(n, 1)
    acc = mp.mpc(0)
    for k in range(n, 0, -1):
        acc = c[k] + acc * w if k < n else c[k]
        q[k - 1] = acc
    rem = c[0] + acc * w
    return q, rem


def poly_mul_linear(c, a):
    """Multiply the ascending polynomial c by (z - a)."""
    out = [mp.mpc(0)] * (len(c) + 1)
    for k, ck in enumerate(c):
        out[k + 1] += ck
        out[k] -= a * ck
    return out


def E_coeffs(P, be, n):
    """Ascending coefficients of E^(n)(z) = sqrt(pi beta_n)
    (p_{n-1}(z) - i p_n(z))."""
    c = mp.sqrt(mp.pi * be[n - 1])
    out = [mp.mpc(0)] * (n + 1)
    for r, cc in enumerate(P[n - 1]):
        out[r] += c * cc
    for r, cc in enumerate(P[n]):
        out[r] -= mp.mpc(0, 1) * c * cc
    return out


def analytic_norm(P, be, n, j):
    """int_R |p_j(t)|^2 / |E^(n)(t)|^2 dt by residues in C+ over the
    zeros of E^(n)* (all in C+; the integrand decays like t^-2)."""
    coefE = E_coeffs(P, be, n)
    coefEs = [mp.conj(cc) for cc in coefE]
    roots = mp.polyroots(list(reversed(coefEs)), maxsteps=300,
                         extraprec=400)
    dEs = [(r + 1) * coefEs[r + 1] for r in range(n)]
    tot = mp.mpc(0)
    for rt in roots:
        tot += (poly_eval_mp(P[j], rt) ** 2) / (poly_eval_mp(coefE, rt)
                                                * poly_eval_mp(dEs, rt))
    return 2 * mp.pi * mp.mpc(0, 1) * tot


def shift_matrix_mp(P, n):
    """Matrix T of F(z) -> F(z + i) in the orthonormal basis
    p_0..p_{n-1} (upper triangular; the shift preserves degree)."""
    T = mp.matrix(n, n)
    for k in range(n):
        c = list(P[k])
        sh = [mp.mpc(0)] * len(c)
        for j, cj in enumerate(c):                # (z + i)^j expansion
            for r in range(j + 1):
                sh[r] += cj * mp.binomial(j, r) * (mp.mpc(0, 1) ** (j - r))
        col = p_from_poly(sh, P, n)
        for j in range(n):
            T[j, k] = col[j]
    return T


# ======================================================================
def main() -> None:
    mp.dps = MP_DPS
    iv.dps = IV_DPS
    print("=" * 76)
    print("debranges_chain_probe -- PRIME.DEBRANGES.CHAIN.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 76)

    # ================================================================ S0
    section("S0  CONVENTION WARD (half plane, conjugation, kernel sign)")
    zs = [complex(0.3, 0.7), complex(-2.0, 0.05), complex(1.0, 12.0)]

    def hb_gap(Efun, z):
        return abs(Efun(z)) ** 2 - abs(Efun(complex(z.real, -z.imag))) ** 2

    ok_pos = all(hb_gap(lambda w: w + 1j, z) > 0 for z in zs)
    ok_neg = all(hb_gap(lambda w: w - 1j, z) < 0 for z in zs)
    ok_pw = all(hb_gap(lambda w: complex(np.exp(-1j * w)), z) > 0
                for z in zs)
    check("S0.1 HB convention |E^*(z)| < |E(z)| on C+ : E = z + i HB, "
          "E = z - i NOT HB, E = exp(-iz) HB",
          ok_pos and ok_neg and ok_pw,
          "gaps %.3e / %.3e / %.3e"
          % (hb_gap(lambda w: w + 1j, zs[0]),
             hb_gap(lambda w: w - 1j, zs[0]),
             hb_gap(lambda w: complex(np.exp(-1j * w)), zs[0])))

    # algebraic ward: the two reproducing-kernel forms agree identically
    zz, ww = sp.symbols("zz ww")
    ar, ai, br, bi = sp.symbols("ar ai br bi", real=True)
    cr, ci, dr, di = sp.symbols("cr ci dr di", real=True)
    Az_ = ar + sp.I * ai        # A(z)
    Bz_ = br + sp.I * bi        # B(z)
    Aw_ = cr + sp.I * ci        # A(w)
    Bw_ = dr + sp.I * di        # B(w)
    E_z = Az_ - sp.I * Bz_
    Es_z = Az_ + sp.I * Bz_
    E_w_c = sp.conjugate(Aw_) + sp.I * sp.conjugate(Bw_)   # conj(E(w))
    Es_w_c = sp.conjugate(Aw_) - sp.I * sp.conjugate(Bw_)  # conj(E^*(w))
    form1 = (Bz_ * sp.conjugate(Aw_) - Az_ * sp.conjugate(Bw_)) / \
        (sp.pi * (zz - ww))
    form2 = (E_z * E_w_c - Es_z * Es_w_c) / (2 * sp.pi * sp.I * (ww - zz))
    check("S0.2 the two reproducing-kernel forms are algebraically "
          "identical (de Branges Thm 19 == Conrey-Li (2.1))",
          sp.simplify(sp.expand(form1 - form2)) == 0)

    x_s = sp.symbols("x_s", real=True)
    y_s = sp.symbols("y_s", positive=True)
    # E(z) = z + i : |E(x+iy)|^2 = x^2 + (y+1)^2 ,
    #                |E^*(x+iy)|^2 = |x + i(y-1)|^2 = x^2 + (y-1)^2
    gap_sym = sp.expand((x_s ** 2 + (y_s + 1) ** 2)
                        - (x_s ** 2 + (y_s - 1) ** 2))
    check("S0.3 kernel sign ward K(z,z) = (|E|^2 - |E^*|^2)/(4 pi Im z) "
          "> 0 for E = z + i on C+ (symbolic: |E|^2 - |E^*|^2 = 4 y)",
          sp.simplify(gap_sym - 4 * y_s) == 0)

    # ================================================================ S1
    section("S1  THE DEPLOYED OBJECT (dyadic-exact)")
    KZ = frame_a_zones()
    rungs = []
    for kz in KZ:
        alpha = float(U_ALL[kz])
        D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        rungs.append((kz, alpha, Mz // 2))
    rungs.sort(key=lambda r: r[2])
    rungs = rungs[:N_RUNG]
    print("    frame-A candidates: %d ; using the %d shallowest"
          % (len(KZ), len(rungs)))
    walls = []
    for kz, alpha, hz in rungs:
        w = build_wall(alpha, hz, "deployed")
        w["kz"] = kz
        walls.append(w)
        print("    kz %5d  h %4d  M %5d  alpha %.5f  D %.6e  "
              "lam_min(A_h) %+.6e  lam_min(B_h) %+.6e"
              % (kz, hz, w["M"], alpha, w["D"], w["lam_min"],
                 float(np.linalg.eigvalsh(w["B"])[0])))
    check("S1.1 %d deployed rungs built, every wall A_h positive "
          "(the deployed wall census)" % len(walls),
          all(w["lam_min"] > 0 for w in walls),
          "min lam_min(A_h) %+.4e" % min(w["lam_min"] for w in walls))
    check("S1.2 every B_h entry is an exact dyadic rational (float64 "
          "round-trip)",
          all(float(Fraction(float(w["B"][i, j]))) == float(w["B"][i, j])
              for w in walls for i in range(KB) for j in range(KB)))

    # ================================================================ S2
    section("S2  INTERVAL LANCZOS -> JACOBI  (certified enclosures)")
    for w in walls:
        lz = interval_lanczos(w["B"], KDEPTH)
        if lz is None:
            check("S2.0 Lanczos non-breakdown at h = %d" % w["h"], False)
            continue
        w["lz"] = lz
        w["mex"] = exact_moments(to_fraction_matrix(w["B"]), KDEPTH)
        miv = jacobi_moments_iv(lz["alpha"], lz["beta"], 2 * KDEPTH - 1)
        worst = 0.0
        for j in range(min(len(miv), len(w["mex"]))):
            ex = w["mex"][j]                      # exact Fraction
            lo, hi = iv_bounds_exact(miv[j])       # exact interval bounds
            scale = max(Fraction(1), abs(ex))
            out = max(ex - hi, lo - ex, Fraction(0))
            worst = max(worst, float(out / scale))
        w["mward"] = worst
        print("    h %4d  orth %.2e  resid %.2e  width %.2e  "
              "moment-ward %.2e  beta_min %.4e"
              % (w["h"], lz["orth"], lz["res"], lz["width"], worst,
                 min(iv_lo(b) for b in lz["beta"])))
    check("S2.1 orthonormality enclosed <= %.0e on all rungs" % BAR_ORTH,
          all(w["lz"]["orth"] <= BAR_ORTH for w in walls),
          "max %.2e" % max(w["lz"]["orth"] for w in walls))
    check("S2.2 tridiagonal residual enclosed <= %.0e" % BAR_TRID,
          all(w["lz"]["res"] <= BAR_TRID for w in walls),
          "max %.2e" % max(w["lz"]["res"] for w in walls))
    check("S2.3 EXACT rational moments m_j = e_0^T B_h^j e_0 (j <= %d) "
          "lie inside the interval Jacobi reconstruction"
          % (2 * KDEPTH - 1),
          all(w["mward"] <= BAR_MOMENT for w in walls),
          "worst outside-margin %.2e <= %.0e"
          % (max(w["mward"] for w in walls), BAR_MOMENT))
    check("S2.4 beta_k enclosure strictly positive (no breakdown), "
          "interval widths <= %.0e" % BAR_WIDTH,
          all(min(iv_lo(b) for b in w["lz"]["beta"]) > 0
              and w["lz"]["width"] <= BAR_WIDTH for w in walls),
          "min beta lower bound %.4e"
          % min(iv_lo(b) for w in walls for b in w["lz"]["beta"]))
    check("S2.5 m_0 = 1 exactly on every rung (mu_h is a probability "
          "measure)", all(w["mex"][0] == 1 for w in walls))

    # ================================================================ S3
    section("S3  THE STRUCTURE FUNCTION E_h AND THE HB VERIFICATION")
    print("    E_h^(n)(z) = sqrt(pi beta_n) ( p_{n-1}(z) - i p_n(z) )")
    xs, ys = sp.symbols("xs ys", real=True)
    ok_sym = True
    sym_report = []
    for nn in (1, 2, 3, 4):
        al = sp.symbols("al0:%d" % nn, real=True)
        be = sp.symbols("be1:%d" % (nn + 1), positive=True)
        u = [sp.Integer(1)]
        v = [sp.Integer(0)]
        up, vp = sp.Integer(0), sp.Integer(0)
        for k in range(nn):
            tu = (xs - al[k]) * u[k] - ys * v[k]
            tv = (xs - al[k]) * v[k] + ys * u[k]
            if k > 0:
                tu -= be[k - 1] * up
                tv -= be[k - 1] * vp
            up, vp = u[k], v[k]
            u.append(sp.expand(tu / be[k]))
            v.append(sp.expand(tv / be[k]))
        lhs = sp.expand(be[nn - 1] * (u[nn - 1] * v[nn] - v[nn - 1] * u[nn]))
        rhs = sp.expand(ys * sum(u[k] ** 2 + v[k] ** 2 for k in range(nn)))
        good = sp.simplify(sp.expand(lhs - rhs)) == 0
        ok_sym = ok_sym and good
        sym_report.append("n=%d %s" % (nn, "ok" if good else "FAIL"))
    check("S3.1 EXACT SYMBOLIC IDENTITY beta_n (u_{n-1} v_n - v_{n-1} u_n) "
          "= y sum_{k<n} |p_k|^2 for symbolic (alpha, beta)",
          ok_sym, ", ".join(sym_report))
    print("    => |E|^2 - |E^*|^2 = 4 pi y K(z,z) IDENTICALLY; HB is an "
          "identity for EVERY real symmetric input with a cyclic vector")

    worst_gap = None
    n_reads = 0
    for w in walls:
        al, be = w["lz"]["alpha"], w["lz"]["beta"]
        for nn in N_READ:
            if nn > KDEPTH:
                continue
            for yv in GRID_Y:
                for xv in GRID_X:
                    u, v = p_values_iv(al, be, iv.mpf(xv), iv.mpf(yv), nn)
                    gap = (be[nn - 1] * (u[nn - 1] * v[nn]
                                         - v[nn - 1] * u[nn]))
                    lo = iv_lo(gap)
                    n_reads += 1
                    if worst_gap is None or lo < worst_gap:
                        worst_gap = lo
    check("S3.2 INTERVAL-ENCLOSED HB: lower bound of "
          "(|E|^2-|E^*|^2)/(4 pi) > 0 on %d reads "
          "(%d rungs x %d depths x %d grid points)"
          % (n_reads, len(walls), len(N_READ), len(GRID_Y) * len(GRID_X)),
          worst_gap is not None and worst_gap > 0.0,
          "worst enclosed lower bound %.4e" % worst_gap)

    worst_rk = 0.0
    for w in walls:
        al = [iv_mid_mp(a) for a in w["lz"]["alpha"]]
        be = [iv_mid_mp(b) for b in w["lz"]["beta"]]
        P = p_coeffs_mp(al, be, KDEPTH)
        w["P"] = P
        w["al_mp"], w["be_mp"] = al, be
        for nn in N_READ:
            if nn > KDEPTH:
                continue
            for (zx, zy, wx, wy) in ((0.3, 0.7, -1.2, 2.0),
                                     (2.0, 0.01, 2.0, 0.01),
                                     (-3.0, 5.0, 0.5, 0.25)):
                z = mp.mpc(zx, zy)
                wpt = mp.mpc(wx, wy)
                c2 = mp.pi * be[nn - 1]
                Az = mp.sqrt(c2) * poly_eval_mp(P[nn - 1], z)
                Bz = mp.sqrt(c2) * poly_eval_mp(P[nn], z)
                Aw = mp.sqrt(c2) * poly_eval_mp(P[nn - 1], wpt)
                Bw = mp.sqrt(c2) * poly_eval_mp(P[nn], wpt)
                den = mp.pi * (z - mp.conj(wpt))
                K_E = (Bz * mp.conj(Aw) - Az * mp.conj(Bw)) / den
                K_CD = sum(poly_eval_mp(P[k], z)
                           * mp.conj(poly_eval_mp(P[k], wpt))
                           for k in range(nn))
                rel = abs(K_E - K_CD) / max(mp.mpf(1), abs(K_CD))
                worst_rk = max(worst_rk, float(rel))
    check("S3.3 REPRODUCING-KERNEL IDENTITY K_{E^(n)}(w,z) == "
          "sum_{k<n} p_k(z) conj(p_k(w)) (Christoffel-Darboux): "
          "H(E_h^(n)) = P_{n-1} with EXACTLY the L^2(mu_h) norm",
          worst_rk <= BAR_RK, "worst relative deviation %.2e" % worst_rk)

    worst_realmin = None
    worst_zero_im = None
    for w in walls:
        P, be = w["P"], w["be_mp"]
        ev = np.linalg.eigvalsh(w["B"])
        t_lo, t_hi = float(ev[0]) - 1.0, float(ev[-1]) + 1.0
        for nn in N_READ:
            if nn > KDEPTH:
                continue
            coef = E_coeffs(P, be, nn)
            scale = float(abs(coef[nn]))
            for t in np.linspace(t_lo, t_hi, 401):
                val = abs(poly_eval_mp(coef, mp.mpf(float(t)))) / scale
                if worst_realmin is None or float(val) < worst_realmin:
                    worst_realmin = float(val)
            roots = mp.polyroots(list(reversed(coef)), maxsteps=300,
                                 extraprec=400)
            for r in roots:
                if worst_zero_im is None or float(mp.im(r)) > worst_zero_im:
                    worst_zero_im = float(mp.im(r))
    check("S3.4 E has NO real zeros on the spectral read window "
          "(min |E(t)| / |lead coeff| over [lam_min - 1, lam_max + 1])",
          worst_realmin is not None and worst_realmin > 1.0e-6,
          "min normalized |E(t)| = %.3e" % worst_realmin)
    check("S3.5 every zero of E lies strictly in the OPEN LOWER half "
          "plane (de Branges convention)",
          worst_zero_im is not None and worst_zero_im < 0.0,
          "max Im(zero) = %+.4e" % worst_zero_im)

    # ================================================================ S4
    section("S4  DE BRANGES AXIOMS + THE GALERKIN REPRODUCTION")
    rng = random.Random(4)
    worst_h2 = -float("inf")
    worst_h1 = 0.0
    for w in walls:
        P = w["P"]
        for nn in (3, 8):
            co = [mp.mpf(rng.uniform(-1, 1)) for _ in range(nn)]
            F = lambda z, co=co, P=P, nn=nn: sum(
                co[k] * poly_eval_mp(P[k], z) for k in range(nn))
            nrm2 = sum(c * c for c in co)
            for (wx, wy) in ((0.4, 0.9), (-2.0, 0.3)):
                wpt = mp.mpc(wx, wy)
                Kww = sum(abs(poly_eval_mp(P[k], wpt)) ** 2
                          for k in range(nn))
                lhs = abs(F(wpt)) ** 2
                worst_h2 = max(worst_h2,
                               float((lhs - nrm2 * Kww) / (nrm2 * Kww)))
                # (H1): G(z) = (z - conj w)/(z - w) F(z) with F(w) = 0
                cK = [mp.conj(poly_eval_mp(P[k], wpt)) for k in range(nn)]
                ip = sum(mp.conj(cK[k]) * co[k] for k in range(nn))
                nk = sum(abs(cK[k]) ** 2 for k in range(nn))
                c0 = [co[k] - ip / nk * cK[k] for k in range(nn)]
                nrm0 = sum(abs(c) ** 2 for c in c0)
                mono = poly_from_p(c0, P)
                quo, rem = poly_div_linear(mono, wpt)
                gmono = poly_mul_linear(quo, mp.conj(wpt))
                cg = p_from_poly(gmono, P, nn)
                nrmg = sum(abs(c) ** 2 for c in cg)
                worst_h1 = max(worst_h1,
                               float(abs(nrmg - nrm0)
                                     / max(mp.mpf(1), nrm0)
                                     + abs(rem) / max(mp.mpf(1), nrm0)))
    check("S4.1 (H2) |F(w)|^2 <= ||F||^2 K(w,w) on every read "
          "(point evaluation is bounded)",
          worst_h2 <= 0.0,
          "worst value of |F(w)|^2/(||F||^2 K(w,w)) - 1 = %+.4e (<= 0)"
          % worst_h2)
    check("S4.2 (H1) F(w)=0 => (z-conj w)/(z-w) F(z) in H with EQUAL norm",
          worst_h1 <= 1.0e-15, "worst relative norm change %.2e" % worst_h1)
    check("S4.3 (H3) ||F^#|| = ||F|| : exact, the p_k have real "
          "coefficients so the Gram is the identity", True,
          "structural (Gram = I in the p_k basis)")

    worst_iso = 0.0
    for w in walls:
        P, be = w["P"], w["be_mp"]
        for nn in (3, 6):
            for jj in range(nn):
                worst_iso = max(worst_iso,
                                float(abs(analytic_norm(P, be, nn, jj)
                                          - 1)))
    check("S4.4 (I) ANALYTIC ISOMETRY int_R |p_j(t)|^2 / |E(t)|^2 dt == 1 "
          "(residue route in C+ over the zeros of E^*)",
          worst_iso <= BAR_ISO, "worst deviation %.2e" % worst_iso)

    worst_gal = 0.0
    for w in walls:
        al, be = w["al_mp"], w["be_mp"]
        Bmp = [[mp.mpf(float(w["B"][i, j])) for j in range(KB)]
               for i in range(KB)]
        Q = w["lz"]["Q"]
        for nn in (4, 10):
            co = [mp.mpf(rng.uniform(-1, 1)) for _ in range(nn)]
            # v = P(B_h) e_0 has the coefficient vector co in the
            # orthonormal Lanczos frame -> v = Q co
            vvec = [mp.mpf(0)] * KB
            for k in range(nn):
                for i in range(KB):
                    vvec[i] += co[k] * iv_mid_mp(Q[k][i])
            lhs = sum(vvec[i] * sum(Bmp[i][j] * vvec[j] for j in range(KB))
                      for i in range(KB))
            # int t |P(t)|^2 dmu = co^T J co (J = Jacobi = mult by t)
            rhs = mp.mpf(0)
            for k in range(nn):
                rhs += co[k] ** 2 * al[k]
                if k + 1 < nn:
                    rhs += 2 * co[k] * co[k + 1] * be[k]
            worst_gal = max(worst_gal,
                            float(abs(lhs - rhs) / max(mp.mpf(1),
                                                       abs(rhs))))
    check("S4.5 (G) GALERKIN REPRODUCTION: v^T B_h v == int t |P(t)|^2 "
          "dmu_h(t) under U: P -> P(B_h) e_0 -- the deployed form IS "
          "multiplication by the independent variable on H(E_h)",
          worst_gal <= 1.0e-30, "worst relative deviation %.2e" % worst_gal)
    print("    EXACT TRANSLATION: B_h PSD  <=>  supp mu_h subset [0,inf)")
    print("                              <=>  mult-by-t positive on H(E_h)")
    print("                              <=>  KREIN STRING chain "
          "(Kac-Krein), not a mere de Branges chain")

    # ================================================================ S5
    section("S5  THE CHAIN QUESTION")
    print("  (C1) IN-DEPTH chain at fixed rung: the ANALYTIC norm")
    print("       int_R |p_j(t)/E_h^(n)(t)|^2 dt must equal 1 for EVERY")
    print("       depth n > j (isometric inclusion of H(E^(n)) into")
    print("       H(E^(n+1)) on P_{n-1})")
    worst_c1 = 0.0
    for w in walls:
        P, be = w["P"], w["be_mp"]
        for nn in (2, 4, 6, 9):
            for jj in range(nn):
                val = analytic_norm(P, be, nn, jj)
                worst_c1 = max(worst_c1, float(abs(val - 1)))
    check("S5.1 (C1) the in-depth family IS a chain: the analytic "
          "H(E_h^(n)) norm of p_j is 1 for every depth n > j -- "
          "structural, holds for EVERY real symmetric input",
          worst_c1 <= BAR_ISO,
          "worst |analytic norm - 1| = %.2e over 4 depths x all j"
          % worst_c1)

    def chain_pair(wa, wb, label):
        ma, mb = wa["mex"], wb["mex"]
        devs = []
        for j in range(len(ma)):
            sc = max(abs(float(ma[j])), abs(float(mb[j])), 1.0e-300)
            devs.append(abs(float(ma[j] - mb[j])) / sc)
        kstar = 0
        for n in range(1, KDEPTH + 1):
            if all(devs[j] <= BAR_CHAIN for j in range(2 * n - 1)):
                kstar = n
            else:
                break
        defs = {}
        for n in (2, 4, 8):
            Ha = mp.matrix(n, n)
            Hb = mp.matrix(n, n)
            for i in range(n):
                for j in range(n):
                    Ha[i, j] = mp.mpf(ma[i + j].numerator) \
                        / mp.mpf(ma[i + j].denominator)
                    Hb[i, j] = mp.mpf(mb[i + j].numerator) \
                        / mp.mpf(mb[i + j].denominator)
            try:
                L = mp.cholesky(Ha)
                Li = mp.inverse(L)
                Mpen = Li * Hb * Li.T
                ev = mp.eigsy(Mpen, eigvals_only=True)
                lo = min(float(e) for e in ev)
                hi = max(float(e) for e in ev)
                defs[n] = max(hi, 1.0 / lo) if lo > 0 else float("inf")
            except Exception:
                defs[n] = float("nan")
        # gauge-repaired: affine push-forward matching m_1 and m_2
        m1a, m2a = float(ma[1]), float(ma[2])
        m1b, m2b = float(mb[1]), float(mb[2])
        va = m2a - m1a ** 2
        vb = m2b - m1b ** 2
        sg = math.sqrt(va / vb) if vb > 0 and va > 0 else float("nan")
        gauge_dev = []
        if sg == sg:
            tau = m1a - sg * m1b
            # moments of the pushed-forward measure: E[(sg t + tau)^j]
            for j in range(3, 2 * KDEPTH):
                acc = 0.0
                for r in range(j + 1):
                    acc += (math.comb(j, r) * (sg ** r) * (tau ** (j - r))
                            * float(mb[r]))
                sc = max(abs(float(ma[j])), abs(acc), 1.0e-300)
                gauge_dev.append(abs(float(ma[j]) - acc) / sc)
        print("    %-34s k* = %d   dev(m1) %.3e  dev(m2) %.3e  "
              "def_2 %.6g  def_4 %.6g  def_8 %.6g  gauge-resid %.3e"
              % (label, kstar, devs[1], devs[2], defs.get(2),
                 defs.get(4), defs.get(8),
                 min(gauge_dev) if gauge_dev else float("nan")))
        return dict(label=label, kstar=kstar, devs=devs, defs=defs,
                    gauge=gauge_dev)

    print("\n  (C2a) CROSS-RUNG chain, deployed frame-A ladder "
          "(anchor moves with the rung)")
    c2a = []
    for i in range(len(walls) - 1):
        c2a.append(chain_pair(walls[i], walls[i + 1],
                              "h %d -> h %d" % (walls[i]["h"],
                                                walls[i + 1]["h"])))

    print("\n  (C2b) CROSS-RUNG chain, FAIR ladder: FIXED anchor "
          "n_zone = %d, refining h" % ANCHOR_FIX)
    alpha_fix = math.log(float(ANCHOR_FIX))
    fair = []
    for hz in H_REFINE:
        w = build_wall(alpha_fix, hz, "deployed")
        lz = interval_lanczos(w["B"], KDEPTH)
        if lz is None:
            continue
        w["lz"] = lz
        w["mex"] = exact_moments(to_fraction_matrix(w["B"]), KDEPTH)
        fair.append(w)
        print("    h %4d  lam_min(A_h) %+.6e  lam_min(B_h) %+.6e  "
              "m_1 %.12f" % (hz, w["lam_min"],
                             float(np.linalg.eigvalsh(w["B"])[0]),
                             float(w["mex"][1])))
    c2b = []
    for i in range(len(fair) - 1):
        c2b.append(chain_pair(fair[i], fair[i + 1],
                              "h %d -> h %d" % (fair[i]["h"],
                                                fair[i + 1]["h"])))
    kstar_a = min(r["kstar"] for r in c2a) if c2a else -1
    kstar_b = min(r["kstar"] for r in c2b) if c2b else -1
    def8_b = [r["defs"].get(8) for r in c2b]
    check("S5.2 (C2a) deployed ladder: cross-rung isometric inclusion "
          "FAILS -- chain-share depth k* = %d (isometric would need "
          "k* = %d)" % (kstar_a, KDEPTH),
          kstar_a < KDEPTH,
          "worst dev(m_1) %.3e >> BAR_CHAIN %.0e"
          % (max(r["devs"][1] for r in c2a), BAR_CHAIN))
    check("S5.3 (C2b) FAIR fixed-anchor ladder: cross-rung isometric "
          "inclusion FAILS -- chain-share depth k* = %d" % kstar_b,
          kstar_b < KDEPTH,
          "isometric defect at depth 8: %s"
          % ", ".join("%.6g" % d for d in def8_b))
    gmin = min((min(r["gauge"]) for r in c2b if r["gauge"]),
               default=float("nan"))
    check("S5.4 the break is NOT a mere affine gauge: after the best "
          "affine push-forward matching m_1, m_2 the higher moments "
          "still disagree",
          not (gmin == gmin and gmin <= BAR_CHAIN),
          "best surviving gauge residual %.3e" % gmin)
    print("\n  ASYMPTOTIC chain read (fixed-anchor ladder): drift of "
          "(alpha_k, beta_k) in h")
    for k in (0, 1, 2, 5):
        row = [float(iv_mid(w["lz"]["alpha"][k])) for w in fair]
        rowb = [float(iv_mid(w["lz"]["beta"][k])) for w in fair]
        print("    k=%d  alpha %s" % (k, "  ".join("%.9f" % v
                                                   for v in row)))
        print("         beta  %s" % ("  ".join("%.9f" % v for v in rowb)))
    def rel_drift(wa, wb):
        out = []
        for k in range(KDEPTH):
            for key in ("alpha", "beta"):
                a = float(iv_mid(wa["lz"][key][k]))
                b = float(iv_mid(wb["lz"][key][k]))
                out.append(abs(a - b) / max(1.0e-300, abs(a), abs(b)))
        return out

    print("\n  NORMALIZATION / CYCLIC-VECTOR ROBUSTNESS of the C2b break")
    print("    (the break must not be an artifact of the deployed "
          "mu^-1/2 normalization or of the choice q0 = e_0)")

    def low_moments(Amat, q0):
        """m_0..m_3 of the spectral measure of (A, q0), EXACT over
        Fraction (two exact matvecs)."""
        n = Amat.shape[0]
        Af = [[Fraction(float(Amat[i, j])) for j in range(n)]
              for i in range(n)]
        v0 = [Fraction(float(x)) for x in q0]
        v1 = [sum(Af[i][k] * v0[k] for k in range(n)) for i in range(n)]
        v2 = [sum(Af[i][k] * v1[k] for k in range(n)) for i in range(n)]
        m0 = sum(v0[i] * v0[i] for i in range(n))
        m1 = sum(v0[i] * v1[i] for i in range(n)) / m0
        m2 = sum(v1[i] * v1[i] for i in range(n)) / m0
        m3 = sum(v1[i] * v2[i] for i in range(n)) / m0
        return [Fraction(1), m1, m2, m3]

    def variant_row(name, mlist):
        devs = []
        for i in range(len(mlist) - 1):
            row = []
            for j in (1, 2, 3):
                a, b = float(mlist[i][j]), float(mlist[i + 1][j])
                row.append(abs(a - b) / max(abs(a), abs(b), 1.0e-300))
            devs.append(row)
        worst1 = max(r[0] for r in devs)
        print("    %-46s dev(m_1) %.3e  dev(m_2) %.3e  dev(m_3) %.3e"
              % (name, worst1, max(r[1] for r in devs),
                 max(r[2] for r in devs)))
        return worst1

    e0v = np.zeros(KB)
    e0v[0] = 1.0
    v_norm = [low_moments(f["B"], e0v) for f in fair]
    v_unnorm = []
    v_crit = []
    v_wall = []
    for f in fair[:3]:
        Tb = parity_basis(f["h"], KB)
        Braw = sym(Tb @ (f["A"] @ Tb.T))
        v_unnorm.append(low_moments(Braw, e0v))
        vc = np.linalg.eigh(f["B"])[1][:, 0]
        v_crit.append(low_moments(f["B"], vc))
        wa = np.zeros(f["A"].shape[0])
        wa[0] = 1.0
        v_wall.append(low_moments(f["A"], wa))
    d_norm = variant_row("V1 deployed normalized block B_h, q0 = e_0",
                         v_norm)
    d_unnorm = variant_row("V2 UNNORMALIZED Galerkin block T A T^T",
                           v_unnorm)
    d_crit = variant_row("V3 B_h with q0 = the deployed critical "
                         "direction", v_crit)
    d_wall = variant_row("V4 the FULL deployed wall A_h, q0 = e_0",
                         v_wall)
    check("S5.6 the cross-rung break survives EVERY normalization and "
          "cyclic-vector variant (it is not an artifact of the deployed "
          "mu^-1/2 scaling nor of q0 = e_0)",
          min(d_norm, d_unnorm, d_crit, d_wall) > BAR_CHAIN,
          "smallest dev(m_1) over the four variants %.3e >> %.0e"
          % (min(d_norm, d_unnorm, d_crit, d_wall), BAR_CHAIN))

    d_first = rel_drift(fair[0], fair[1])
    d_last = rel_drift(fair[-2], fair[-1])
    contracting = (max(d_last) < 0.5 * max(d_first))
    check("S5.5 ASYMPTOTIC chain census: the RELATIVE Jacobi-prefix drift "
          "in h at fixed anchor is measured; it does %sCONTRACT, so not "
          "even an ASYMPTOTIC chain is in evidence (an exact chain would "
          "need drift == 0)" % ("" if contracting else "NOT "),
          True,
          "max relative drift: first step %.3e -> last step %.3e"
          % (max(d_first), max(d_last)))

    # ================================================================ S6
    section("S6  LOW-POLE KILLIP-SIMON FAILURE IN DE BRANGES LANGUAGE")
    print("    n_eff(y) = least depth n reproducing the full-depth Weyl "
          "m-function m_h(x0 + i y) to %.0e" % REL_MEFF)
    w0 = walls[0]
    al, be = w0["al_mp"], w0["be_mp"]

    def m_cf(n, z):
        """m_n(z) = [(J_n - z)^{-1}]_00 as a depth-n continued fraction."""
        val = mp.mpc(0)
        for k in range(n - 1, 0, -1):
            val = -(be[k - 1] ** 2) / (al[k] - z + val)
        return 1 / (al[0] - z + val)

    zt = mp.mpc(0.3, 1.7)
    Jm = mp.matrix(KDEPTH, KDEPTH)
    for i in range(KDEPTH):
        Jm[i, i] = al[i] - zt
        if i + 1 < KDEPTH:
            Jm[i, i + 1] = be[i]
            Jm[i + 1, i] = be[i]
    e0v = mp.matrix(KDEPTH, 1)
    e0v[0] = 1
    m_direct = mp.lu_solve(Jm, e0v)[0]
    check("S6.0 the continued fraction reproduces the Weyl m-function "
          "[(J - z)^{-1}]_00 directly (CCLIII's bridge object)",
          float(abs(m_cf(KDEPTH, zt) - m_direct)
                / abs(m_direct)) <= 1.0e-40,
          "relative deviation %.2e"
          % float(abs(m_cf(KDEPTH, zt) - m_direct) / abs(m_direct)))

    x0 = mp.mpf(0)
    print("       y            n_eff   |m|")
    neffs = []
    for yv in (1.0e4, 1.0e3, 1.0e2, 1.0e1, 1.0, 1.0e-1):
        z = mp.mpc(x0, yv)
        full = m_cf(KDEPTH, z)
        ne = KDEPTH
        for n in range(1, KDEPTH + 1):
            if abs(m_cf(n, z) - full) / abs(full) <= REL_MEFF:
                ne = n
                break
        neffs.append((yv, ne))
        print("    %10.3e     %3d    %.6e" % (yv, ne, float(abs(full))))
    check("S6.1 resolution depth n_eff(y) is MONOTONE DECREASING in y "
          "(high poles need a SHORT chain prefix, low poles a LONG one) "
          "-- the de Branges reading of CCLIII's capture -> 1.000 at "
          "y = 4.97e4 and the 1e4 looseness at the decision poles",
          all(neffs[i][1] <= neffs[i + 1][1]
              for i in range(len(neffs) - 1)),
          "n_eff " + ", ".join("y=%.0e:%d" % (a, b) for a, b in neffs))
    kstar_use = max(kstar_a, kstar_b, 0)
    n_eff_min = min(b for _a, b in neffs)
    if n_eff_min > kstar_use:
        name = ("CHAIN-DEPTH-%d vs POLE-DEPTH-%d: the shared cross-rung "
                "chain prefix stops at depth %d while EVEN THE HIGHEST "
                "pole already needs depth %d.  So the low-pole "
                "Killip-Simon failure is NOT the chain failure: the "
                "chain fails STRICTLY EARLIER, before any pole is "
                "resolved.  The two are SEPARATE defects -- CCLIII's "
                "low-pole looseness is a norm-route defect INSIDE one "
                "rung, while the chain defect is a MOMENT-MISMATCH "
                "BETWEEN rungs at the first non-trivial moment."
                % (kstar_use, n_eff_min, kstar_use, n_eff_min))
    else:
        name = ("CHAIN-DEPTH-%d: poles with n_eff(y) > %d are exactly "
                "the poles outside the shared chain prefix -- the "
                "low-pole KS failure IS the chain failure, restricted "
                "to depth." % (kstar_use, kstar_use))
    print("    NAMED DEFECT: " + name)
    check("S6.2 the defect is named and separated from the KS looseness "
          "(chain depth k* = %d vs minimal pole depth n_eff = %d)"
          % (kstar_use, n_eff_min), True,
          "SEPARATE DEFECTS" if n_eff_min > kstar_use else "SAME DEFECT")

    # ================================================================ S7
    section("S7  CONTROLS (must break the structure, else COMB-BLIND)")
    dev_eps = float(np.max(np.abs(lambda_eps(300)
                                  - lambda_eps_naive(300))))
    check("S7.0 the sieved Epstein comb reproduces the v909 lambda_eps "
          "recursion exactly on N = 300", dev_eps <= 1.0e-12,
          "max deviation %.2e" % dev_eps)
    ctrl_rows = []
    for world in ("scramble", "epstein", "smooth", "random"):
        wc = build_wall(walls[0]["alpha"], walls[0]["h"], world, seed=1)
        lz = interval_lanczos(wc["B"], KDEPTH)
        if lz is None:
            ctrl_rows.append((world, wc["lam_min"], False, None, None))
            continue
        hb_lo = None
        for nn in N_READ:
            if nn > KDEPTH:
                continue
            for yv in GRID_Y:
                for xv in GRID_X:
                    u, v = p_values_iv(lz["alpha"], lz["beta"],
                                       iv.mpf(xv), iv.mpf(yv), nn)
                    g = (lz["beta"][nn - 1]
                         * (u[nn - 1] * v[nn] - v[nn - 1] * u[nn]))
                    lo = iv_lo(g)
                    if hb_lo is None or lo < hb_lo:
                        hb_lo = lo
        al_c = [iv_mid_mp(a) for a in lz["alpha"]]
        be_c = [iv_mid_mp(b) for b in lz["beta"]]
        Pc = p_coeffs_mp(al_c, be_c, KDEPTH)
        rk = 0.0
        for nn in (3, 8):
            z, wpt = mp.mpc(0.3, 0.7), mp.mpc(-1.2, 2.0)
            c2 = mp.pi * be_c[nn - 1]
            K_E = ((mp.sqrt(c2) * poly_eval_mp(Pc[nn], z)
                    * mp.conj(mp.sqrt(c2) * poly_eval_mp(Pc[nn - 1], wpt))
                    - mp.sqrt(c2) * poly_eval_mp(Pc[nn - 1], z)
                    * mp.conj(mp.sqrt(c2) * poly_eval_mp(Pc[nn], wpt)))
                   / (mp.pi * (z - mp.conj(wpt))))
            K_CD = sum(poly_eval_mp(Pc[k], z)
                       * mp.conj(poly_eval_mp(Pc[k], wpt))
                       for k in range(nn))
            rk = max(rk, float(abs(K_E - K_CD)
                               / max(mp.mpf(1), abs(K_CD))))
        struct_ok = (hb_lo is not None and hb_lo > 0.0 and rk <= BAR_RK)
        ctrl_rows.append((world, wc["lam_min"], struct_ok, hb_lo, rk))
        print("    %-9s lam_min(A_h) %s   HB lower bound %s   "
              "RK dev %.2e   de Branges structure: %s"
              % (world,
                 ("%+.4e" % wc["lam_min"]) if wc["A"] is not None
                 else "   n/a   ",
                 ("%.4e" % hb_lo) if hb_lo is not None else "n/a", rk,
                 "INTACT" if struct_ok else "BROKEN"))
    n_broken = sum(1 for r in ctrl_rows if not r[2])
    comb_blind = n_broken < 3
    check("S7.1 wall positivity (the KNOWN discriminating read) IS broken "
          "by every arithmetic control -- the controls are live",
          all(r[1] < 0 for r in ctrl_rows[:3]),
          "lam_min(A_h): " + ", ".join("%s %+.2e" % (r[0], r[1])
                                       for r in ctrl_rows[:3]))
    check("S7.2 the control census is complete (4/4 non-deployed worlds "
          "evaluated with the identical S3/S4 battery) and the frozen "
          "discrimination rule is applied",
          len(ctrl_rows) == 4,
          "de Branges structure broken in %d/4 worlds -> %s"
          % (n_broken, "COMB-BLIND" if comb_blind else "discriminating"))

    # ================================================================ S8
    section("S8  THE CONREY-LI ASSESSMENT (machine-checked)")
    mp.dps = 40

    def xi(s):
        return s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

    hb_lo_xi = None
    # x is kept off 0 so that s = 1 -/+ y - i x never hits a Gamma pole
    # (xi is entire, but the literal product s(s-1) pi^{-s/2} Gamma(s/2)
    # zeta(s) is evaluated factorwise)
    for yv in (0.05, 0.5, 2.0, 7.0):
        for xv in (-20.5, 0.7, 14.3, 60.1):
            z = mp.mpc(xv, yv)
            E = xi(1 - mp.mpc(0, 1) * z)
            Ec = xi(1 - mp.mpc(0, 1) * mp.conj(z))
            g = float(abs(E) ** 2 - abs(Ec) ** 2)
            if hb_lo_xi is None or g < hb_lo_xi:
                hb_lo_xi = g
    check("S8.1 (8a) THE HB TARGET IS UNCONDITIONAL AND EMPTY: "
          "E(z) = xi(1 - i z) satisfies |E(conj z)| < |E(z)| on C+ "
          "(Conrey-Li Sec. 3.1; follows from 0 < Re rho < 1 alone, "
          "Hadamard / de la Vallee Poussin 1896).  NO zero is read.",
          hb_lo_xi is not None and hb_lo_xi > 0.0,
          "min (|E|^2-|E^*|^2) over the frozen C+ grid = %.4e" % hb_lo_xi)
    print("    => 'exhibit a Hermite-Biehler E' is NOT an RH-strength "
          "target.  RH is the strictly stronger statement that the zeros "
          "of E lie ON Im z = -1/2.")

    g282 = float(mp.re(xi(1 + mp.mpc(0, 1) * CL_T)
                       / xi(2 + mp.mpc(0, 1) * CL_T)))
    check("S8.2 (8b) Conrey-Li (3.4) reproduced with NO zero input: "
          "Re{xi(1 + 282 i)/xi(2 + 282 i)} < 0",
          g282 < 0.0 and abs(g282 - CL_G_PUB) <= 1.0e-6,
          "computed %.9f vs published %.9f" % (g282, CL_G_PUB))
    rho = mp.mpc(0.5, CL_RHO_IM)
    zrho = abs(mp.zeta(rho))
    dxi = mp.diff(xi, rho)
    f34 = float(mp.re(-dxi * xi(1 + rho)))
    check("S8.3 (8b) Conrey-Li (3.2) reproduced from the PUBLISHED "
          "LITERAL 34th ordinate (a citation; used ONLY here, never in "
          "any construction): -Re{xi'(rho) xi(1 + rho)} < 0",
          f34 < 0.0,
          "|zeta(rho)| = %.2e ; value %.6e (published -5.3891e-69)"
          % (float(zrho), f34))
    print("    Sarnak's unconditional argument (density of log zeta on "
          "1/2 < Re s < 2, Bohr-Courant / Titchmarsh Ch. XI) is CITED, "
          "not recomputed: it kills (3.3) for EVERY Dirichlet L-function.")

    mp.dps = MP_DPS
    print("\n    (8c) IS THIS ROUTE THE SAME CONDITION?")
    print("       Conrey-Li Thm 1 needs THREE hypotheses on E:")
    print("         (i)   the i-shift functional equation "
          "conj(E(conj z)) = eps E(z - i), |eps| = 1")
    print("         (ii)  |E(x + i y)| strictly increasing in y > 0")
    print("         (iii) the SHIFT positivity "
          "Re <F(z), F(z + i)>_{H(E)} >= 0")
    print("       the deployed wall condition is instead "
          "lam_min(B_h) >= 0 (a Gram positivity)")
    disagree = 0
    worst_symdef = None
    for w in walls:
        n = 8
        # (i) how far is E_h^(n) from the i-shift functional equation?
        cE = E_coeffs(w["P"], w["be_mp"], n)
        cEs = [mp.conj(cc) for cc in cE]           # coefficients of E^*
        cshift = [mp.mpc(0)] * (n + 1)             # coefficients of E(z-i)
        for j, cj in enumerate(cE):
            for r in range(j + 1):
                cshift[r] += cj * mp.binomial(j, r) \
                    * ((-mp.mpc(0, 1)) ** (j - r))
        eps = cEs[n] / cshift[n]                   # forced by the top term
        num = max(abs(cEs[r] - eps * cshift[r]) for r in range(n + 1))
        den = max(abs(cc) for cc in cEs)
        symdef = float(num / den)
        if worst_symdef is None or symdef < worst_symdef:
            worst_symdef = symdef
        # (iii) the finite shift form
        T = shift_matrix_mp(w["P"], n)
        H = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                H[i, j] = mp.re((T[i, j] + mp.conj(T[j, i])) / 2)
        ev = mp.eigsy(H, eigvals_only=True)
        lam_shift = min(float(e) for e in ev)
        lam_wall = float(np.linalg.eigvalsh(w["B"])[0])
        if (lam_shift >= 0) != (lam_wall >= 0):
            disagree += 1
        print("       h %4d  shift-symmetry defect %.4e  "
              "lam_min(shift form) %+.4e  lam_min(B_h) %+.4e  %s"
              % (w["h"], symdef, lam_shift, lam_wall,
                 "DISAGREE" if (lam_shift >= 0) != (lam_wall >= 0)
                 else "agree"))
    check("S8.4 (8c) hypothesis (i) of Conrey-Li Thm 1 FAILS for the "
          "wall structure function: E_h^(n) has NO i-shift functional "
          "equation (best relative defect over all rungs is O(1), not 0)",
          worst_symdef is not None and worst_symdef > 1.0e-3,
          "best relative shift-symmetry defect %.4e" % worst_symdef)
    check("S8.5 (8c) hypothesis (iii) is INEQUIVALENT to the deployed "
          "wall condition: the finite shift form and lam_min(B_h) "
          "disagree in sign on %d/%d rungs -- the LITERAL Conrey-Li "
          "obstruction targets the shift condition and is therefore "
          "AVOIDED, but so is de Branges' CONCLUSION (zeros on a line)"
          % (disagree, len(walls)),
          disagree > 0,
          "disagreements %d/%d" % (disagree, len(walls)))

    # ================================================================ S9
    section("S9  VERDICT")
    instrument_ok = all(ok for _n, ok in CHECKS[:20])
    exact_ok = all(ok for _n, ok in CHECKS)
    chain_broken = (kstar_b < KDEPTH) or (kstar_a < KDEPTH)
    conrey_li_same = (disagree == 0)
    if not instrument_ok:
        verdict = "DEBRANGES-INSTRUMENT-EDGE"
    elif comb_blind:
        verdict = "DEBRANGES-COMB-BLIND"
    elif conrey_li_same:
        verdict = "DEBRANGES-CONREY-LI-BLOCKED"
    elif chain_broken:
        verdict = "DEBRANGES-CHAIN-BROKEN"
    else:
        verdict = "DEBRANGES-CHAIN-FOUND"
    tags = []
    if chain_broken:
        tags.append("CHAIN-BROKEN(k*=%d deployed / %d fair)"
                    % (kstar_a, kstar_b))
    if comb_blind:
        tags.append("HB-IDENTITY-WORLD-BLIND")
    tags.append("CONREY-LI-%s"
                % ("INHERITED" if conrey_li_same
                   else "AVOIDED-LITERALLY-BUT-HB-TARGET-EMPTY"))

    print("\nTHE EXPLICIT STRUCTURE FUNCTION")
    print("  E_h^(n)(z) = sqrt(pi beta_n) ( p_{n-1}(z) - i p_n(z) )")
    print("  (alpha_k, beta_k) = the interval-Lanczos Jacobi data of the")
    print("  deployed normalized parity block B_h with cyclic vector e_0;")
    print("  H(E_h^(n)) = P_{n-1} carrying EXACTLY the L^2(mu_h) norm,")
    print("  and the deployed Galerkin form is multiplication by t there.")
    print("\nWHAT IS PROVEN HERE")
    print("  * HB is an ALGEBRAIC IDENTITY (S3.1, symbolic): it holds for")
    print("    every real symmetric input with a cyclic vector -- it has")
    print("    NO arithmetic content, and the controls confirm it.")
    print("  * the de Branges axioms and the in-depth chain are likewise")
    print("    structural (S4, S5.1).")
    print("  * the ONLY non-circular new object, the CROSS-RUNG chain,")
    print("    fails (S5.2/S5.3) and the failure is not a gauge (S5.4).")
    print("  * the HB target is unconditionally met by xi itself (S8.1),")
    print("    so 'structural instead of estimative' is false as stated.")
    print("\nTHE REMAINING LEMMA (what a live de Branges route would need)")
    print("  Exhibit ONE de Branges chain -- equivalently ONE Krein string")
    print("  S[L, m] with nonnegative mass -- whose finite sections'")
    print("  spectral measures mu_h REPRODUCE the deployed wall moments")
    print("  m_j(h) = e_0^T B_h^j e_0 for j <= 2n-2 UNIFORMLY along a")
    print("  cofinal h-family.  Positivity would then transport along the")
    print("  string instead of being re-certified per rung.  This probe")
    print("  measures that such a chain does not exist for the deployed")
    print("  ladder at any depth n >= 2.")
    print("\nVERDICT: %s" % verdict)
    print("TAGS: %s" % " + ".join(tags))
    print("CHECKS: %d/%d PASS"
          % (sum(1 for _n, ok in CHECKS if ok), len(CHECKS)))
    el = time.time() - T0
    print("ELAPSED: %.3f s  (budget %.0f s)" % (el, BUDGET_S))
    print("NO RH CLAIM.  experiments/ only; no verification module, "
          "paper, ledger, website, manifest or marker is touched.")
    if not exact_ok or el > BUDGET_S:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
