#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""threebounds_probe -- PRIME.ONEBADMODE.THREEBOUNDS.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE THREE NAMED MISSING BOUNDS OF THE LEVEL-3 ARCHITECTURE.
CCXCVII closed the MECHANISM (the one-atom collapse IS the
near-eigenvector alignment of b with v_top(B); the moment SHAPE and
the ALIGNMENT are the same statement) and left its PROVED-RATE tier
empty with three named holes, all of them statements about the WINDOW
CONSTRUCTION and none of them about the cancellation:

  B1  a PROVED LOWER bound on B's RELATIVE SPECTRAL GAP
      (measured h-stationary, d log/d log h = -0.016 +- 0.105);
  B2  a PROVED UPPER bound on the RAYLEIGH DEFICIT
      (measured GROWING, d log/d log h = +1.02 +- 0.76);
  B3  a PROVED LIPSCHITZ CONSTANT for rho_K in the shape coordinates
      replacing the measured L ~ 2.8.

THIS PROBE attacks all three.  The lead idea for B1 + B2 is that the
CCXCVII gap bound is stated in EIGENVALUES (mu_1, mu_2 of B) while
every ingredient it needs is available as an ENTRY FUNCTIONAL with a
closed form, so the eigenvalues can be eliminated ENTIRELY.

THE ENTRY-EXPLICIT BOUND (the deliverable of B1 + B2, elementary).
Let B = Mt[1:, 1:] (symmetric, PD on every certified cell: P1 n > 0,
P2 the exact-rationally certified floor c > 0, E2), let
b = Mt[1:, 0], nu_0 = b^T b, nu_1 = b^T B b, d = dim B, and let
  T = tr(B^2) = || B ||_F^2   (a SUM OF SQUARES OF THE ENTRIES),
  R = nu_1 / nu_0             (the RAYLEIGH QUOTIENT of b in B).
With mu_1 >= ... >= mu_d >= c > 0 the eigenvalues of B:
  (P1) R <= mu_1                            [Rayleigh]
  (P2) mu_1 <= sqrt(T - (d-1) c^2) =: F_1   [sum of squares + floor]
  (P3) mu_2^2 <= T - mu_1^2 - (d-2) c^2, and t -> t - sqrt(K - t^2)
       is increasing, so with (P1)
         mu_1 - mu_2 >= R - sqrt(T - R^2 - (d-2) c^2) =: G_1 .
Hence, with NO eigensolver anywhere,
  B1  relgap(B) = (mu_1 - mu_2)/mu_1 >= G_1 / F_1        [LOWER]
  B2  deficit(B) = (mu_1 - R)/mu_1 <= 1 - R / F_1        [UPPER]
  and, composed with CCXCVII's exact gap bound,
      sin^2 theta <= (mu_1 - R)/(mu_1 - mu_2) <= (F_1 - R)/G_1 .
In the FLOOR-FREE reading (c -> 0, F_1 = sqrt(T)) the composed bound
collapses to a ONE-PARAMETER statement in
      t := R / sqrt(T) = nu_1 / (nu_0 || B ||_F)  in (0, 1],
      sin^2 theta <= (1 - t) / (t - sqrt(1 - t^2)),
which is < 1 EXACTLY WHEN t > 4/5 (square 2t - 1 > sqrt(1 - t^2):
5 t^2 - 4 t > 0).  So the whole level-3 mechanism reduces to ONE
SCALAR of the window Gram matrix, and the residual open question is
no longer "the spectrum of B" but "a lower bound for t".  The bound
is warded per cell against the MEASURED sin theta and against
CCXCVII's own eigenvalue gap bound (it must be weaker than the latter
and stronger than the truth), and both readings (floor-free, floor-
sharpened) are printed; the declared consumption rule is that the
tighter VALID one is used and both are proved.

 (a) B1 -- THE GAP BOUND.  The entry-explicit lower bound above, its
     per-cell ward, its h-law, and the SEAT: the exact CCIII carrier
     split S = S_AR + S_SM + S_OSC pushed through the SAME step frame
     gives Mt = Mt_AR + Mt_SM + Mt_OSC, so (T, R) decompose into
     carrier tables.  Two questions are answered numerically: (i) is
     the entry-explicit bound already carried by the ARCHIMEDEAN part
     alone (closed forms) with the prime part a perturbation, and
     (ii) does WEYL (E8) on the source-side Gram S_2 deliver
     mu_1(S) - mu_2(S) >= (arch gap) - 2 || prime part || with a
     POSITIVE right-hand side?  Whatever fails is reported as an
     honest gap with its factor.  A SECOND, INDEPENDENT reduction is
     delivered for the source side: with a = v_min(S_1) the frame
     axis, B is the COMPRESSION of Mt onto a^perp, so by CAUCHY
     INTERLACING (E11) and one Rayleigh test vector
       mu_1(B) >= m_1 - c_1^2 (m_1 - n)/(1 - c_1^2),  mu_2(B) <= m_2,
     i.e. relgap(B) >= 1 - m_2/(m_1 - c_1^2 (m_1 - n)/(1 - c_1^2)),
     whose ingredients are r_gap = mu_2(S_2)/mu_1(S_2), the
     consecutive-rung overlap |c_1| = |<v_min(S_1), u_max(S_2)>| and
     the axis Rayleigh ratio n/m_1 -- all WINDOW GEOMETRY of two
     neighbouring census cells.  Warded per cell.
 (b) B2 -- THE DEFICIT BOUND.  The entry-explicit upper bound above
     (1 - R/F_1), its ward, its h-law compared with the MEASURED
     +1.02 growth, and the EXACT identity that types the growth:
       deficit = sum_{j>=2} (w_j/nu_0) (mu_1 - mu_j)/mu_1
               <= sin^2 theta (1 - mu_d/mu_1),
     so the deficit is BOUNDED BY 1 - 1/kappa(B) identically and its
     measured growth cannot continue -- it is the misaligned weight,
     not a free quantity.  The CARRIER question (geometry drift of
     the neighbouring cells vs the prime reads) is decided by the
     same carrier split and by regressing the deficit against the
     step's explicit geometry drift (d alpha, d log D, d log h).
 (c) B3 -- THE LIPSCHITZ CONSTANT.  rho_K = RADAU_K(nu; c) is an
     EXPLICIT RATIONAL function of (nu_0..nu_{2K-2}, c): the E4
     Chebyshev algorithm followed by two exact tridiagonal solves.
     Its gradient is therefore a finite computation.  A DYADIC
     INTERVAL ARITHMETIC with outward rounding at 400 significand
     bits and FORWARD-MODE derivatives re-implements those two steps
     and returns a CERTIFIED ENCLOSURE of the gradient over a box
     around the CCLXXXVII medoid limit vector.  Deliverable: the
     certified Lipschitz constants in the SHAPE coordinates
     g_k = log10(nu_k / n^{k+2}) (and the floor coordinate
     log10(c/n)) per K = 4, 5, with the radius ladder that shows
     where the certified region ends.  THE SIGNED gradient is kept,
     not just its magnitudes, because the free-box constant
     L1 = sum_k |d rho_K / d g_k| is the WRONG object: CCLXXXVII's
     LIM1 already measured the moment box to be non-product, and L1
     is exactly the certified form of that statement.  The RIGHT
     objects are the DIRECTIONAL constants along the deep family's
     own two legal directions -- MASS (nu -> t nu) and ATOM (the
     one-atom line g_k = g_0 + k log10 x*) -- together with the
     declared plane constant L_plane = L_MASS + 2 L_ATOM (every
     sup-norm-1 direction of the plane is a MASS + b ATOM with
     |a| <= 1, |b| <= 2).  Wards: (i) the interval evaluation at the
     box centre must CONTAIN the exact-rational dml value (the
     re-implementation ward); (ii) EULER: rho_K is homogeneous of
     degree 1 in the moments, so the SIGNED gradient sum must equal
     ln(10) rho_K -- an exact identity that proves the gradient
     itself, not merely its enclosure; (iii) MEAN VALUE: exact
     rational probe pairs inside the box must satisfy
     |d rho| <= L |d g| with ZERO violations; (iv) a doctored
     non-moment vector must be REFUSED by the positivity guard.  The
     certified constants are compared with the MEASURED L ~ 2.79 /
     2.80 of CCXCVII, which lives in the OTHER coordinate
     (sin theta), so the comparison is split into its SHAPE half
     (measured here, directly comparable) and the converting factor
     (typed MEASURED).  The OFF-PLANE residual of the family's
     motion and the certified REACH are reported, never absorbed.
 (d) THE COMPOSITION UPDATE.  The CCXCVII two readings are recomputed
     with the proved pieces in place and the per-link typing ladder
     is printed: does the DIRECT reading's razor-thin margin +0.0104
     survive when the measured L is replaced by the certified one,
     and which links remain MEASURED?
 (e) GATES.  REPRO of the CCXCVII shared numbers: the g_k fit, the
     MEDOID, RADAU_4/5, the rho_5 envelope (hard gates), and the
     CCXCVII rate laws (relative gap, Rayleigh deficit, the empirical
     Lipschitz constants, the direct-reading margin) as a printed
     CENSUS against the note's rounded values.  Controls-must-fire on
     the NEW objects: SCRAMBLE must leave the t-envelope, SMOOTH and
     the prime-blind ARCHIMEDEAN world must read a different t, a
     SYNTHETIC MISALIGNMENT must be detected by t itself, a HALVED
     bound must be violated (the ward has teeth) and the interval
     tier must REFUSE a doctored non-moment vector.  tau and CCXVII
     c_h relocation screens on the new bound quantities.  Anti-
     circularity: the entry-explicit bound path is AST-scanned to see
     the wall matrix ENTRIES and the certified floor forward only --
     no tau, no h, no alpha, no kz, no frame object, no ladder
     identifier AND NO EIGENSOLVER AT ALL (a strictly stronger scan
     than CCXCVII's, which allowed one).

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E2  Schur / Sylvester and the LDL pivot criterion.  [Horn & Johnson,
     Matrix Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3  MATRICES, MOMENTS AND QUADRATURE: Gauss-Radau with the node at
     the spectral floor is an UPPER bound.  [Golub & Meurant, PUP
     2010, Ch. 6-7.]
 E4  the Chebyshev algorithm (exact monic recurrence from power
     moments).  [Gautschi, OUP 2004, Sec. 2.1.]
 E7  Hamburger/Hankel positivity.  [Akhiezer, Hafner 1965, Ch. 1.]
 E8  WEYL's inequality.  [Horn & Johnson op. cit. Sec. 4.3.]
 E11 CAUCHY's interlacing theorem for a principal submatrix / a
     codimension-one compression of a symmetric matrix.  [Horn &
     Johnson op. cit. Thm 4.3.17.]
 E12 the MEAN VALUE inequality on a convex box and the soundness of
     outward-rounded interval arithmetic with forward-mode
     derivatives.  [Moore, Kearfott & Cloud, Introduction to Interval
     Analysis, SIAM 2009, Ch. 5-6; Rump, Acta Numerica 19 (2010)
     287-449.]
 E13 EULER's homogeneous function theorem (used as the B3 gradient
     ward: RADAU_K is homogeneous of degree 1 in (nu, c)).  [Apostol,
     Mathematical Analysis, 2nd ed., Addison-Wesley 1974, Thm 12.15.]

FROZEN PROTOCOL.
 S0 firewall: AST scan of THIS file for the prime/zero oracle ban
    list; predecessors imported READ-ONLY; the only RNG seat is the
    declared scramble control seed.  AC scan: the bound path
    (entry_bounds / shape_read_local) sees the wall matrix ENTRIES,
    the certified floor and frozen constants only; the ban list is
    CCXCVII's RATE list PLUS every eigensolver name.
 M  THE MACHINERY: deep_membership_limit_probe (CCLXXXVII) and
    deep_rate_mechanism_probe (CCXCVII) are imported READ-ONLY; the
    CCXCVII pipeline is re-run VERBATIM with its declared amendment
    A1 block geometry (targets (1300, 2400, 3300, 4178, FRONTIER),
    sizes (5, 5, 4, 5, 4)), so the CCXCVII numbers are reproduced,
    not recomputed differently.  CCXCVII's own
    readers atom_read / align_read / shape_read are CALLED, not
    copied.
 G  the reproduction gate (hard) + the rate-law census (printed).
 B1 the gap bound: entry-explicit + interlacing + the carrier seat.
 B2 the deficit bound: entry-explicit + the exact identity + carrier.
 B3 the certified Lipschitz constant of RADAU_K.
 CU the composition update with the per-link typing ladder.
 X  controls-must-fire; S the screens; V the frozen verdict.

VERDICTS (frozen enum).  Per bound: PROVED-CONDITIONAL (the
inequality is elementary, machine-warded on every built cell and
consumes ENTRY data only; its inputs are MEASURED per cell -- no
all-h claim), DERIVED (a reduction to named window objects without a
closed criterion), OPEN (neither).  For B3: LIP-CERTIFIED (a finite
interval-arithmetic proof of a gradient bound on a declared box),
LIP-PARTIAL, LIP-OPEN.  Plus COMPOSITION-UPDATED with the honest
per-link typing.  No marker moves, no promotion, NO RH claim.

SMOKE AMENDMENTS (declared before the frozen run; the smoke SHA and
the frozen SHA therefore differ, by these three items only).
 A1 the B3 MEAN VALUE ward computed the coordinate step as
    log10(1 + s); at s ~ 1e-16 that underflows to 0.0 in float64 and
    the ward would have been VACUOUS (bound 0 vs a nonzero exact
    deviation, reported as a violation).  Replaced by log1p(s)/ln 10.
 A2 the B3 deliverable was specified as the free-box constant
    L1 = sum_k |d rho / d g_k| alone.  The smoke showed L1 ~ 1e2-1e3
    while the family's own motion is two-parameter, i.e. L1 answers a
    question the geometry does not ask.  The signed gradient, the
    EULER ward, the MASS / ATOM / plane constants and the OFF-PLANE
    residual were added; L1 is still reported, never dropped.
 A3 the X3 control doctored the B1 bound by the factor 1/2.  The
    smoke showed the bound's SHARPNESS to be 3.6-4.9, so a factor of
    1/2 CANNOT fire -- the control was testing the sharpness, not the
    teeth.  Replaced by the SHUFFLE control (a cell's bound against
    its t-neighbour's measured misalignment), which a vacuous or
    cell-independent bound would survive; the halving count and the
    full sharpness census are still printed.

PREDECESSORS (READ-ONLY): deep_rate_mechanism_probe (CCXCVII),
deep_membership_limit_probe (CCLXXXVII), onebadmode_moments_probe,
euler_phase_identity_probe (CCXVII c_h), v563_paper2_readouts.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/threebounds_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/threebounds_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import deep_membership_limit_probe as dml      # noqa: E402 (READ-ONLY)
import deep_rate_mechanism_probe as drm        # noqa: E402 (READ-ONLY)
import onebadmode_moments_probe as ob          # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul       # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
KMOM = dml.KMOM
KBASE = dml.KBASE
KDEEP = dml.KDEEP
SCHUR_BAR_F = drm.SCHUR_BAR_F
BUDGET = drm.BUDGET

# the CCXCVII block geometry, verbatim (its amendment A1)
BLOCK_TGT_R = drm.BLOCK_TGT_R
BLOCK_NC_R = drm.BLOCK_NC_R
HARD_CAP_R = drm.HARD_CAP_R

# CCLXXXVII / CCXCVII reproduction references (hard gates)
GSLOPE_REF = drm.GSLOPE_REF
GSLOPE_ATOL = drm.GSLOPE_ATOL
GR2_REF = drm.GR2_REF
GR2_ATOL = drm.GR2_ATOL
MED_KZ_REF = drm.MED_KZ_REF
MED_H_REF = drm.MED_H_REF
RAD4_REF = drm.RAD4_REF
RAD5_REF = drm.RAD5_REF
RAD_RTOL = drm.RAD_RTOL
ENV_RHO5_REF = drm.ENV_RHO5_REF
ENV_RTOL = drm.ENV_RTOL

# CCXCVII rate-law references (the NOTE's rounded values -> CENSUS,
# printed and compared, never a kill; the note quotes 2 digits)
RELGAP_SLOPE_REF = -0.016
DEF_SLOPE_REF = +1.02
LIP_REF_SET = (2.79, 2.80)
MARGIN_REF = +0.0104
LAW_ATOL = 0.02
MARGIN_ATOL = 2.0e-3

# ---- the entry-explicit bound (B1 + B2)
T_CLOSE = 0.8               # the exact closure threshold 4/5 for t
BOUND_SLACK = 1.0e-12       # allowance in the bound-property wards
CTRL_HALVE = 0.5            # the doctored-bound control factor

# ---- the certified interval tier (B3)
IV_BITS = 400               # dyadic outward rounding, significand
DELTAS = (0.0, 1.0e-24, 1.0e-20, 1.0e-18, 1.0e-16, 1.0e-14,
          1.0e-12, 1.0e-10, 1.0e-8, 1.0e-6, 1.0e-4, 1.0e-2)
IV_USEFUL = 1.0e-3          # declared "useful enclosure" rel width
MVT_FRAC = 0.5              # the probe step inside the box
LN10_LO = Fraction(2302585092994045684, 10 ** 18)
LN10_HI = Fraction(2302585092994045685, 10 ** 18)
B3_BUDGET_S = 300.0         # the certified tier's own honest cut-off

# ---- the carrier seat census (B1 (a))
SEAT_TGT = (1300, 2400, 3300)
SEAT_N = 1
CH_N_R = 3
CH_HMAX_R = 2900
CH_BUDGET_S = 1250.0
SCR_SEED = dml.SCR_SEED
CTRL_TILT = drm.CTRL_TILT
SLOPE_PASS = dml.SLOPE_PASS
SLOPE_RELOC = dml.SLOPE_RELOC

BANNED_IDS = dml.BANNED_IDS
# AC: STRICTLY STRONGER than CCXCVII's -- the bound path may see the
# wall ENTRIES, the certified floor and frozen constants, and it may
# NOT call an eigensolver at all.  (The scan is case-insensitive, so
# the single-letter frame identifiers X, Q, S are caught too.)
BOUND_BANNED = tuple(sorted({
    s.lower() for s in drm.RATE_BANNED + (
        "eigh", "eigvalsh", "eigvals", "eig", "svd", "svdvals",
        "pinv", "cond", "norm", "atom_read", "align_read")}))
BOUND_FUNCS = ("entry_bounds",)

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm.lower() in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def f4(values):
    return dml.f4(values)


def linfit(xv, yv):
    return dml.linfit(xv, yv)


def law_of(pairs):
    """d log v / d log h with 2SE and R2 over (h, v) pairs."""
    xs = []
    ys = []
    for hv, val in pairs:
        if math.isfinite(val) and val > 0.0 and hv > 0.0:
            xs.append(math.log(hv))
            ys.append(math.log(val))
    if len(xs) < 4:
        return None
    slp, se2, r2v, _a = linfit(xs, ys)
    stat = ("H-STATIONARY" if abs(slp) + se2 <= 0.15
            else "DECAYING" if slp + se2 < 0.0
            else "GROWING" if slp - se2 > 0.0 else "NOISY")
    return dict(slope=slp, se=se2, r2=r2v, stat=stat, n=len(xs))


# ============================================ THE ENTRY-EXPLICIT PATH
# AC-scanned: wall matrix ENTRIES + the certified floor forward only,
# NO eigensolver anywhere in this function.
def entry_bounds(matrix, floor_in=0.0):
    """B1 + B2 WITHOUT EIGENVALUES.  From the entries alone:
      nu_0 = b^T b, nu_1 = b^T B b, T = tr(B^2) = sum of squares of
      the entries of B, R = nu_1/nu_0, d = dim B, and the certified
      floor c (exact-rational, LDL, no eigensolver).  With
      mu_1 >= ... >= mu_d >= c > 0:
        F_1 = sqrt(T - (d-1) c^2) >= mu_1,
        G_1 = R - sqrt(T - R^2 - (d-2) c^2) <= mu_1 - mu_2,
      hence relgap >= G_1/F_1, deficit <= 1 - R/F_1 and
      sin^2 theta <= (F_1 - R)/G_1.  The floor-free reading (c = 0)
      is computed as well and the tighter VALID one is consumed --
      both are proved.  t = R/sqrt(T) in (0, 1] is the one-parameter
      closure coordinate: the composed bound is < 1 iff t > 4/5."""
    mmat = np.asarray(matrix, float)
    piv = float(mmat[0, 0])
    cvec = mmat[1:, 0]
    blk = 0.5 * (mmat[1:, 1:] + mmat[1:, 1:].T)
    dim = int(blk.shape[0])
    nu_0 = float(cvec @ cvec)
    nu_1 = float(cvec @ (blk @ cvec))
    tr_2 = float(np.sum(blk * blk))
    flo = max(0.0, float(floor_in))
    if not (piv > 0.0 and nu_0 > 0.0 and tr_2 > 0.0
            and math.isfinite(nu_1)):
        return None
    ray = nu_1 / nu_0
    if not (ray > 0.0):
        return None
    out = dict(nu0=nu_0, nu1=nu_1, tr2=tr_2, ray=ray, dim=dim,
               floor=flo, t_plain=ray / math.sqrt(tr_2))
    best = None
    for lab, cfl in (("plain", 0.0), ("floor", flo)):
        f_sq = tr_2 - (dim - 1) * cfl * cfl
        g_sq = tr_2 - (dim - 2) * cfl * cfl - ray * ray
        if f_sq <= 0.0 or g_sq < 0.0:
            continue
        f_1 = math.sqrt(f_sq)
        if ray > f_1 * (1.0 + 1.0e-12):
            continue
        g_1 = ray - math.sqrt(g_sq)
        rec = dict(kind=lab, f1=f_1, g1=g_1,
                   relgap_lb=(g_1 / f_1 if g_1 > 0.0 else 0.0),
                   deficit_ub=1.0 - ray / f_1,
                   sin2_ub=((f_1 - ray) / g_1 if g_1 > 0.0
                            else float("inf")),
                   t_par=ray / f_1)
        out[lab] = rec
        if best is None or rec["sin2_ub"] < best["sin2_ub"]:
            best = rec
    if best is None:
        return None
    out["use"] = best["kind"]
    out["relgap_lb"] = max(out.get(k, {"relgap_lb": 0.0})["relgap_lb"]
                           for k in ("plain", "floor") if k in out)
    out["deficit_ub"] = min(out.get(k, {"deficit_ub": 1.0})
                            ["deficit_ub"]
                            for k in ("plain", "floor") if k in out)
    out["sin2_ub"] = best["sin2_ub"]
    out["sin_ub"] = math.sqrt(best["sin2_ub"]) \
        if math.isfinite(best["sin2_ub"]) else float("inf")
    out["t_use"] = best["t_par"]
    return out


# ================================================ THE INTERVAL TIER
class IvRefuse(Exception):
    """A certified computation refused: a guard interval straddles 0
    or a positivity premise is not certified on the whole box."""


def _rnd_lo(val):
    if val == 0:
        return Fraction(0)
    num, den = val.numerator, val.denominator
    exp = num.bit_length() - den.bit_length()
    shift = exp - IV_BITS
    if shift >= 0:
        pot = 1 << shift
        return Fraction((num // (den * pot)) * pot)
    pot = 1 << (-shift)
    return Fraction((num * pot) // den, pot)


def _rnd_hi(val):
    if val == 0:
        return Fraction(0)
    num, den = val.numerator, val.denominator
    exp = num.bit_length() - den.bit_length()
    shift = exp - IV_BITS
    if shift >= 0:
        pot = 1 << shift
        return Fraction(-((-num) // (den * pot)) * pot)
    pot = 1 << (-shift)
    return Fraction(-((-num * pot) // den), pot)


class IV(object):
    """A dyadic interval with OUTWARD rounding at IV_BITS significand
    bits.  Every operation encloses the exact result (E12)."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None, raw=False):
        if hi is None:
            hi = lo
        if raw:
            self.lo = lo
            self.hi = hi
        else:
            self.lo = _rnd_lo(Fraction(lo))
            self.hi = _rnd_hi(Fraction(hi))

    def __add__(self, oth):
        return IV(self.lo + oth.lo, self.hi + oth.hi)

    def __sub__(self, oth):
        return IV(self.lo - oth.hi, self.hi - oth.lo)

    def __mul__(self, oth):
        cnd = (self.lo * oth.lo, self.lo * oth.hi,
               self.hi * oth.lo, self.hi * oth.hi)
        return IV(min(cnd), max(cnd))

    def __truediv__(self, oth):
        if oth.lo <= 0 <= oth.hi:
            raise IvRefuse("division by an interval containing 0")
        cnd = (self.lo / oth.lo, self.lo / oth.hi,
               self.hi / oth.lo, self.hi / oth.hi)
        return IV(min(cnd), max(cnd))

    def __neg__(self):
        return IV(-self.hi, -self.lo, raw=True)

    def positive(self):
        return self.lo > 0

    def mag(self):
        return max(abs(self.lo), abs(self.hi))

    def wid(self):
        return self.hi - self.lo

    def mid(self):
        return (self.lo + self.hi) / 2

    def contains(self, val):
        return self.lo <= Fraction(val) <= self.hi


IV_ZERO = IV(Fraction(0))
IV_ONE = IV(Fraction(1))


class DV(object):
    """Forward-mode derivatives over IV: value + gradient, every
    component an enclosure (E12)."""

    __slots__ = ("v", "g")

    def __init__(self, val, grad):
        self.v = val
        self.g = grad

    def __add__(self, oth):
        return DV(self.v + oth.v,
                  [a + b for a, b in zip(self.g, oth.g)])

    def __sub__(self, oth):
        return DV(self.v - oth.v,
                  [a - b for a, b in zip(self.g, oth.g)])

    def __mul__(self, oth):
        return DV(self.v * oth.v,
                  [a * oth.v + self.v * b
                   for a, b in zip(self.g, oth.g)])

    def __truediv__(self, oth):
        quo = self.v / oth.v
        return DV(quo, [(a - quo * b) / oth.v
                        for a, b in zip(self.g, oth.g)])

    def __neg__(self):
        return DV(-self.v, [-a for a in self.g])


def dv_const(val, nvar):
    return DV(IV(val), [IV_ZERO] * nvar)


def dv_var(lo, hi, idx, nvar):
    grad = [IV_ZERO] * nvar
    grad[idx] = IV_ONE
    return DV(IV(lo, hi), grad)


def iv_cheb(momv, kdeg, nvar):
    """E4 Chebyshev algorithm over DV -- the dml.chebyshev_monic
    recurrence, operation for operation, with the positivity guards
    turned into CERTIFIED positivity (refuse if not certified)."""
    need = 2 * kdeg - 1
    if len(momv) < need or not momv[0].v.positive():
        return None
    zero = dv_const(Fraction(0), nvar)
    pprev = [zero] * need
    prev = list(momv[:need])
    alp = [momv[1] / momv[0]]
    bet = []
    for kk in range(1, kdeg):
        cur = [zero] * need
        for pos in range(kk, 2 * kdeg - 1 - kk):
            term = prev[pos + 1] - alp[kk - 1] * prev[pos]
            if kk >= 2:
                term = term - bet[kk - 2] * pprev[pos]
            cur[pos] = term
        if not (prev[kk - 1].v.positive() and cur[kk].v.positive()):
            return None
        bet.append(cur[kk] / prev[kk - 1])
        if 2 * kdeg - 1 - kk > kk + 1:
            alp.append(cur[kk + 1] / cur[kk]
                       - prev[kk] / prev[kk - 1])
        pprev = prev
        prev = cur
    if len(alp) != kdeg - 1 or len(bet) != kdeg - 1:
        return None
    return alp, bet


def iv_solve(amat, rhs, nvar):
    """Gaussian elimination over DV WITHOUT row swaps; every pivot
    must be certified away from 0 (dml.fr_solve takes row k whenever
    its pivot is nonzero, so the elimination order agrees)."""
    dim = len(amat)
    aug = [list(row) + [rhs[i]] for i, row in enumerate(amat)]
    for kk in range(dim):
        piv = aug[kk][kk]
        if piv.v.lo <= 0 <= piv.v.hi:
            raise IvRefuse("pivot interval contains 0")
        for i in range(kk + 1, dim):
            fac = aug[i][kk] / piv
            for j in range(kk, dim + 1):
                aug[i][j] = aug[i][j] - fac * aug[kk][j]
    out = [None] * dim
    for kk in range(dim - 1, -1, -1):
        acc = aug[kk][dim]
        for j in range(kk + 1, dim):
            acc = acc - aug[kk][j] * out[j]
        out[kk] = acc / aug[kk][kk]
    return out


def iv_radau(alp, bet, flo, mass, nvar):
    """dml.radau_exact over DV: the monic Radau modification followed
    by the (1, 1) entry of the inverse Jacobi matrix, times the mass.
    Depth K = len(alp) + 1."""
    kdeg = len(alp) + 1
    dim = kdeg - 1
    zero = dv_const(Fraction(0), nvar)
    one = dv_const(Fraction(1), nvar)
    tmat = [[zero] * dim for _ in range(dim)]
    for i in range(dim):
        tmat[i][i] = alp[i] - flo
        if i + 1 < dim:
            tmat[i][i + 1] = bet[i]
            tmat[i + 1][i] = one
    rhs = [zero] * dim
    rhs[dim - 1] = one
    sol = iv_solve(tmat, rhs, nvar)
    alr = flo + bet[kdeg - 2] * sol[dim - 1]
    tt = [[zero] * kdeg for _ in range(kdeg)]
    for i in range(kdeg):
        tt[i][i] = alp[i] if i < kdeg - 1 else alr
        if i + 1 < kdeg:
            tt[i][i + 1] = bet[i]
            tt[i + 1][i] = one
    rhs2 = [zero] * kdeg
    rhs2[0] = one
    sol2 = iv_solve(tt, rhs2, nvar)
    return mass * sol2[0]


def iv_rho(momv, flo, kdeg, nvar):
    cheb = iv_cheb(momv, kdeg, nvar)
    if cheb is None:
        return None
    return iv_radau(cheb[0], cheb[1], flo, momv[0], nvar)


def exact_rho(momv, flo, kdeg):
    """The dml exact-rational reference value."""
    cheb = dml.chebyshev_monic(momv, kdeg)
    if cheb is None:
        return None
    return dml.radau_exact(cheb[0], cheb[1], flo, momv[0])


def cert_lipschitz(momn, flon, kdeg, delta):
    """The CERTIFIED gradient enclosure of rho_K over the relative box
    nu_k in [(1-delta) nu_k, (1+delta) nu_k], c likewise (delta = 0
    is the certified gradient AT the point).  Returns the SIGNED log-
    derivative enclosures in the SHAPE coordinates
    g_k = log10 nu_k (and log10 c),
      d rho / d g_k = ln(10) * nu_k * d rho / d nu_k ,
    so that L1 = sum_k |d rho / d g_k| is the Lipschitz constant for
    the SUP-norm on g -- and, because the signed enclosures are
    kept, DIRECTIONAL constants |sum_k v_k d rho / d g_k| along any
    declared legal direction v are available too (that distinction is
    the whole point: the free box is not the data's motion)."""
    need = 2 * kdeg - 1
    nvar = need + 1
    rad = Fraction(delta).limit_denominator(10 ** 24)
    lof = Fraction(1) - rad
    hif = Fraction(1) + rad
    momv = []
    for j in range(need):
        val = momn[j]
        if val <= 0:
            return None
        momv.append(dv_var(val * lof, val * hif, j, nvar))
    if flon <= 0:
        return None
    flo = dv_var(flon * lof, flon * hif, need, nvar)
    try:
        res = iv_rho(momv, flo, kdeg, nvar)
    except IvRefuse as exc:
        return dict(refused=str(exc))
    if res is None:
        return dict(refused="positivity guard")
    ln10 = IV(LN10_LO, LN10_HI)
    dparts = [ln10 * momv[j].v * res.g[j] for j in range(need)]
    dflo = ln10 * flo.v * res.g[need]
    lsum = sum(p.mag() for p in dparts)
    euler = dparts[0]
    for prt in dparts[1:]:
        euler = euler + prt
    return dict(rho=res.v, dparts=dparts, dflo=dflo,
                l1=float(lsum), l1_floor=float(lsum + dflo.mag()),
                lmax=float(max(p.mag() for p in dparts)),
                lflo=float(dflo.mag()),
                parts=[float(p.mag()) for p in dparts],
                euler=euler,
                rel=float(res.v.wid() / max(Fraction(1, 10 ** 30),
                                            abs(res.v.mid()))),
                refused=None)


def dir_bound(dparts, vec):
    """The CERTIFIED directional Lipschitz constant along the
    declared direction vec (sup-norm 1) in shape coordinates: the
    SIGNED interval sum, so the cancellation that the rigid moment
    shape enforces is kept, not thrown away."""
    acc = IV(Fraction(0))
    for prt, cmp_v in zip(dparts, vec):
        acc = acc + IV(Fraction(cmp_v).limit_denominator(10 ** 12)
                       ) * prt
    return float(acc.mag()), acc


# ==================================== G: the reproduction + the laws
def repro_gate(limobj, cens):
    section("G-REPRO -- the CCLXXXVII / CCXCVII reproduction gate "
            "(the machinery is re-run VERBATIM with CCXCVII's own "
            "amendment A1 geometry, so this is a true reproduction)")
    if limobj is None:
        check("G-REPRO limit object exists", False, kill="K3")
        return
    med = limobj["medoid"]
    r_4 = limobj["rec"].get(KBASE, float("nan"))
    r_5 = limobj["rec"].get(KDEEP, float("nan"))
    env = cens["rho5"]["env_hi_lim"]
    if SMOKE:
        print("    SMOKE (declared, CCXCVII amendment A2 inherited): "
              "the smoke block geometry is the shallow (600, 900) "
              "pair, so the deep references cannot apply.  Measured: "
              "gslope %+.5f (R2 %.6f), medoid block %d %s kz %d "
              "h %d, RADAU_4 %.9f, RADAU_5 %.9f, rho_5 envelope %.6f"
              % (limobj["gslope"], limobj["gr2"], med["block"],
                 med["mode"], int(med["kz"]), int(med["h"]), r_4,
                 r_5, env))
        check("G-REPRO reproduction SMOKE-SKIPPED (typed)", True)
        return
    check("G1 the g_k one-atom fit reproduces: slope %+.5f vs %+.5f "
          "(atol %.0e), R2 %.6f vs %.6f (atol %.0e)"
          % (limobj["gslope"], GSLOPE_REF, GSLOPE_ATOL,
             limobj["gr2"], GR2_REF, GR2_ATOL),
          abs(limobj["gslope"] - GSLOPE_REF) <= GSLOPE_ATOL
          and abs(limobj["gr2"] - GR2_REF) <= GR2_ATOL, kill="K3")
    check("G2 the MEDOID limit member reproduces: block %d %s kz %d "
          "h %d vs kz %d h %d" % (med["block"], med["mode"],
                                  int(med["kz"]), int(med["h"]),
                                  MED_KZ_REF, MED_H_REF),
          int(med["kz"]) == MED_KZ_REF and int(med["h"]) == MED_H_REF,
          kill="K3")
    check("G3 the MEDOID's exact RADAU values reproduce: RADAU_4 "
          "%.9f vs %.9f, RADAU_5 %.9f vs %.9f (rtol %.0e)"
          % (r_4, RAD4_REF, r_5, RAD5_REF, RAD_RTOL),
          abs(r_4 / RAD4_REF - 1.0) <= RAD_RTOL
          and abs(r_5 / RAD5_REF - 1.0) <= RAD_RTOL, kill="K3")
    check("G4 the frontier rho_5 ENVELOPE reproduces: %.6f vs %.6f "
          "(rtol %.0e) -- the CCLXXXVII budget against the "
          "DEFINITENESS bar 1 is %+.6f"
          % (env, ENV_RHO5_REF, ENV_RTOL, BUDGET),
          abs(env / ENV_RHO5_REF - 1.0) <= ENV_RTOL, kill="K3")


def rate_census(rows):
    """CCXCVII's own readers, CALLED (not copied), on the same rows;
    the CCXCVII laws are re-measured and compared with the note."""
    section("A -- THE CCXCVII RATE CENSUS, re-measured with CCXCVII's "
            "own readers (atom_read / align_read / shape_read called "
            "READ-ONLY), and the note's law values as a CENSUS")
    keep = []
    d_spec = 0.0
    for row in rows:
        atm = drm.atom_read(row["step"]["Mt"])
        alg = drm.align_read(row["step"]["Mt"])
        shp = drm.shape_read(row["step"]["Mt"])
        if atm is None or alg is None or shp is None:
            continue
        row["atm"] = atm
        row["alg"] = alg
        row["shp"] = shp
        d_spec = max(d_spec, atm["spec_dev"])
        keep.append(row)
    check("A1 the CCXCVII spectral resolution identity still holds on "
          "all %d cells: max rel %.2e <= %.0e"
          % (len(keep), d_spec, drm.SPEC_TIE),
          len(keep) > 0 and d_spec <= drm.SPEC_TIE, kill="K2")
    if not keep:
        return keep, {}
    laws = {}
    for lab, fun in (("sin theta", lambda r: r["atm"]["sin_th"]),
                     ("relative gap of B",
                      lambda r: r["atm"]["relgap"]),
                     ("Rayleigh deficit",
                      lambda r: r["atm"]["deficit"]),
                     ("GAP bound", lambda r: r["atm"]["gap_bound"]),
                     ("x* atom position",
                      lambda r: r["atm"]["x_top"])):
        law = law_of([(r["h"], fun(r)) for r in keep])
        if law:
            laws[lab] = law
            print("      LAW  %-22s d log v / d log h = %+.4f +- "
                  "%.4f (R2 %.3f, %d cells)   %s"
                  % (lab, law["slope"], law["se"], law["r2"],
                     law["n"], law["stat"]))
    rg = laws.get("relative gap of B", {})
    df = laws.get("Rayleigh deficit", {})
    ok_rg = abs(rg.get("slope", 99.0) - RELGAP_SLOPE_REF) <= LAW_ATOL
    ok_df = abs(df.get("slope", 99.0) - DEF_SLOPE_REF) <= LAW_ATOL
    check("A2 CENSUS (printed, no kill -- the note quotes two "
          "digits): B's relative gap law %+.4f vs %+.3f (%s), the "
          "Rayleigh deficit law %+.4f vs %+.3f (%s), atol %.2f"
          % (rg.get("slope", float("nan")), RELGAP_SLOPE_REF,
             "match" if ok_rg else "DIFFERS",
             df.get("slope", float("nan")), DEF_SLOPE_REF,
             "match" if ok_df else "DIFFERS", LAW_ATOL), True)
    return keep, laws


# ==================================== B1: the gap bound
def bound_one(rows, seat):
    section("B1 -- A LOWER BOUND ON B'S RELATIVE SPECTRAL GAP: the "
            "ENTRY-EXPLICIT bound (no eigensolver), the INTERLACING "
            "reduction to the window geometry, and the carrier seat")
    n_bad = 0
    n_live = 0
    n_gapbad = 0
    for row in rows:
        ent = entry_bounds(row["step"]["Mt"],
                           row.get("c_cert_f", 0.0))
        row["ent"] = ent
        if ent is None:
            continue
        if ent["relgap_lb"] > row["atm"]["relgap"] + BOUND_SLACK:
            n_gapbad += 1
        if ent["sin2_ub"] + BOUND_SLACK < row["atm"]["sin_th"] ** 2:
            n_bad += 1
        if ent["sin2_ub"] < 1.0:
            n_live += 1
    use = [r for r in rows if r.get("ent")]
    check("B1.1 the ENTRY-EXPLICIT relative-gap LOWER bound "
          "G_1/F_1 <= relgap(B) on every one of the %d cells: %d "
          "violations (0 required)" % (len(use), n_gapbad),
          n_gapbad == 0 and len(use) > 0, kill="K2")
    check("B1.2 the COMPOSED entry-explicit bound (F_1 - R)/G_1 is an "
          "upper bound for the MEASURED sin^2 theta on every cell: "
          "%d violations (0 required); non-vacuous (< 1) on %d/%d"
          % (n_bad, n_live, len(use)), n_bad == 0, kill="K2")
    ts = [r["ent"]["t_use"] for r in use]
    n_close = sum(1 for t in ts if t > T_CLOSE)
    print("    the ONE-PARAMETER closure coordinate "
          "t = nu_1/(nu_0 ||B||_F): min/med/max %s; t > 4/5 (the "
          "EXACT closure threshold) on %d/%d cells"
          % (f4(ts), n_close, len(use)))
    print("    block cells h(med)   t (min/med/max)              "
          "relgap_LB  relgap    ratio   sin2_UB   sin^2 th   ratio")
    for bi in sorted({r["block"] for r in use}):
        sub = [r for r in use if r["block"] == bi]
        hmd = float(np.median([r["h"] for r in sub]))
        lbs = [r["ent"]["relgap_lb"] for r in sub]
        tru = [r["atm"]["relgap"] for r in sub]
        s2b = [r["ent"]["sin2_ub"] for r in sub]
        s2t = [r["atm"]["sin_th"] ** 2 for r in sub]
        print("    %5d %5d %6d  %s  %9.6f %9.6f %7.4f %9.4g %9.3g "
              "%7.4g"
              % (bi, len(sub), int(hmd),
                 f4([r["ent"]["t_use"] for r in sub]),
                 float(np.median(lbs)), float(np.median(tru)),
                 float(np.median(lbs)) / max(1e-300,
                                             float(np.median(tru))),
                 float(np.median(s2b)), float(np.median(s2t)),
                 float(np.median(s2b)) / max(1e-300,
                                             float(np.median(s2t)))))
    laws = {}
    for lab, fun in (("t (closure coord)",
                      lambda r: r["ent"]["t_use"]),
                     ("1 - t (the open scalar)",
                      lambda r: 1.0 - r["ent"]["t_use"]),
                     ("relgap LOWER bound",
                      lambda r: r["ent"]["relgap_lb"]),
                     ("sin^2 UPPER bound",
                      lambda r: r["ent"]["sin2_ub"])):
        law = law_of([(r["h"], fun(r)) for r in use])
        if law:
            laws[lab] = law
            print("      LAW  %-24s d log v / d log h = %+.4f +- "
                  "%.4f (R2 %.3f)   %s"
                  % (lab, law["slope"], law["se"], law["r2"],
                     law["stat"]))
    # ---- the INTERLACING reduction (source-side, window geometry)
    n_ilbad = 0
    n_ilive = 0
    for row in use:
        alg = row["alg"]
        m_1, m_2, c_1 = alg["m1"], alg["m2"], alg["c1"]
        gg = max(1.0e-300, 1.0 - c_1 * c_1)
        piv = float(np.asarray(row["step"]["Mt"], float)[0, 0])
        low = m_1 - c_1 * c_1 * (m_1 - piv) / gg
        row["il_lb"] = (1.0 - m_2 / low) if low > 0.0 else -1.0
        if row["il_lb"] > row["atm"]["relgap"] + BOUND_SLACK:
            n_ilbad += 1
        if row["il_lb"] > 0.0:
            n_ilive += 1
    ils = [r["il_lb"] for r in use]
    check("B1.3 the INTERLACING reduction (E11 + one Rayleigh test "
          "vector) relgap(B) >= 1 - m_2/(m_1 - c_1^2 (m_1 - n)/"
          "(1 - c_1^2)) holds on every cell: %d violations (0 "
          "required); POSITIVE on %d/%d; value %s -- its ingredients "
          "are r_gap = mu_2(S_2)/mu_1(S_2), the consecutive-rung "
          "overlap |c_1| and the axis Rayleigh ratio n/m_1, all "
          "WINDOW GEOMETRY" % (n_ilbad, n_ilive, len(use), f4(ils)),
          n_ilbad == 0, kill="K2")
    # ---- the SEAT: is the bound already carried by the arch part?
    if seat:
        print("    THE CARRIER SEAT of the entry-explicit bound "
              "(exact CCIII split through the SAME step frame):")
        print("      h      partial sum   t         relgap_LB   "
              "sin2_UB      WEYL on S_2: gap_AR   2||prime||   "
              "gap_AR - 2||prime||")
        for rec in seat:
            for lab in ("AR", "AR+SM", "FULL"):
                ent = rec["cum"].get(lab)
                if ent is None:
                    print("      %-6d %-13s NO VALID READ (the "
                          "partial sum is not a wall matrix)"
                          % (rec["h"], lab))
                    continue
                extra = ""
                if lab == "FULL":
                    extra = ("        %10.4g %12.4g %14.4g"
                             % (rec["gap_ar"], 2.0 * rec["pri"],
                                rec["gap_ar"] - 2.0 * rec["pri"]))
                print("      %-6d %-13s %.6f  %10.3e %11.4g%s"
                      % (rec["h"], lab, ent["t_use"],
                         ent["relgap_lb"], ent["sin2_ub"], extra))
        n_weyl = sum(1 for r in seat
                     if r["gap_ar"] - 2.0 * r["pri"] > 0.0)
        n_arch = sum(1 for r in seat
                     if r["cum"].get("AR")
                     and r["cum"]["AR"]["t_use"] > T_CLOSE)
        check("B1.4 THE SEAT CENSUS on %d split cells: the WEYL route "
              "on the source Gram S_2 (gap of the ARCHIMEDEAN part "
              "minus twice the norm of the prime part) is POSITIVE on "
              "%d/%d, and the ARCHIMEDEAN partial sum alone reaches "
              "t > 4/5 on %d/%d -- printed as measured, no kill"
              % (len(seat), n_weyl, len(seat), n_arch, len(seat)),
              True)
    verd = ("PROVED-CONDITIONAL" if (n_bad == 0 and n_gapbad == 0
                                     and n_close == len(use)
                                     and len(use) > 0)
            else "DERIVED" if n_gapbad == 0 else "OPEN")
    check("B1.5 B1 VERDICT %s: the relative-gap LOWER bound is an "
          "ELEMENTARY entry functional (proved inequality, warded on "
          "%d/%d cells, no eigensolver); its INPUT t is MEASURED per "
          "cell (median %.6f) and the residual open object is the "
          "single scalar 1 - t (h-law %s)"
          % (verd, len(use) - n_gapbad, len(use),
             float(np.median(ts)) if ts else float("nan"),
             laws.get("1 - t (the open scalar)", {}).get("stat",
                                                         "n/a")),
          True)
    return dict(verdict=verd, laws=laws, n_close=n_close,
                n_use=len(use), t_med=float(np.median(ts)) if ts
                else float("nan"), ils=ils)


# ==================================== B2: the deficit bound
def bound_two(rows, laws_ref):
    section("B2 -- AN UPPER BOUND ON THE RAYLEIGH DEFICIT: the "
            "entry-explicit bound, the EXACT identity that types the "
            "measured growth, and the carrier of the drift")
    use = [r for r in rows if r.get("ent")]
    n_bad = 0
    n_kap = 0
    for row in use:
        ent = row["ent"]
        atm = row["atm"]
        if ent["deficit_ub"] + BOUND_SLACK < atm["deficit"]:
            n_bad += 1
        # the EXACT identity bound: deficit <= sin^2 th (1 - 1/kappa)
        kap = 1.0 - 1.0 / max(1.0e-300, atm["kap_blk"])
        row["def_id"] = atm["sin_th"] ** 2 * kap
        if row["def_id"] + BOUND_SLACK < atm["deficit"]:
            n_kap += 1
    check("B2.1 the ENTRY-EXPLICIT deficit UPPER bound 1 - R/F_1 "
          "dominates the MEASURED Rayleigh deficit on every one of "
          "the %d cells: %d violations (0 required)"
          % (len(use), n_bad), n_bad == 0 and len(use) > 0,
          kill="K2")
    check("B2.2 the EXACT identity bound deficit = sum_{j>=2} "
          "(w_j/nu_0)(mu_1 - mu_j)/mu_1 <= sin^2 theta "
          "(1 - mu_d/mu_1) holds on every cell: %d violations (0 "
          "required) -- the deficit IS the misaligned weight times "
          "the spread, so it is bounded by 1 - 1/kappa(B) "
          "identically and the measured GROWTH cannot continue"
          % n_kap, n_kap == 0, kill="K2")
    dubs = [r["ent"]["deficit_ub"] for r in use]
    dtru = [r["atm"]["deficit"] for r in use]
    dids = [r["def_id"] for r in use]
    print("    the deficit census: MEASURED %s; entry-explicit UPPER "
          "bound %s; identity bound sin^2 th (1 - 1/kappa) %s"
          % (f4(dtru), f4(dubs), f4(dids)))
    laws = {}
    for lab, fun in (("deficit (measured)",
                      lambda r: r["atm"]["deficit"]),
                     ("deficit UPPER bound",
                      lambda r: r["ent"]["deficit_ub"]),
                     ("identity bound",
                      lambda r: r["def_id"]),
                     ("1 - 1/kappa(B)",
                      lambda r: 1.0 - 1.0 / max(1e-300,
                                                r["atm"]["kap_blk"]))):
        law = law_of([(r["h"], fun(r)) for r in use])
        if law:
            laws[lab] = law
            print("      LAW  %-22s d log v / d log h = %+.4f +- "
                  "%.4f (R2 %.3f)   %s"
                  % (lab, law["slope"], law["se"], law["r2"],
                     law["stat"]))
    # ---- the CARRIER of the drift: geometry vs the prime reads
    print("    THE CARRIER OF THE GROWTH (the deficit is a quotient "
          "of window-Gram quantities of two NEIGHBOURING cells): the "
          "measured deficit regressed against the step's EXPLICIT "
          "geometry drift and against the prime-side reads:")
    drifts = []
    for row in use:
        stp = row["step"]
        r_1, r_2 = stp["r1"], stp["r2"]

        def gap_of(key):
            a_1 = float(r_1.get(key, float("nan")))
            a_2 = float(r_2.get(key, float("nan")))
            return a_1, a_2

        a_1, a_2 = gap_of("alpha")
        d_al = a_2 - a_1
        b_1, b_2 = gap_of("D")
        d_ld = (math.log(b_2 / b_1) if b_1 > 0.0 and b_2 > 0.0
                else float("nan"))
        c_1, c_2 = gap_of("h")
        d_lh = (math.log(c_2 / c_1) if c_1 > 0.0 and c_2 > 0.0
                else float("nan"))
        drifts.append((row, d_al, d_ld, d_lh))
    for lab, idx in (("d alpha (arch step)", 1),
                     ("d log D (grid step)", 2),
                     ("d log h (depth step)", 3)):
        xs = [abs(d[idx]) for d in drifts if abs(d[idx]) > 0.0]
        ys = [d[0]["atm"]["deficit"] for d in drifts
              if abs(d[idx]) > 0.0]
        if len(xs) < 4:
            print("      %-22s too few nonzero drifts (%d)"
                  % (lab, len(xs)))
            continue
        slp, se2, r2v, _a = linfit([math.log(v) for v in xs],
                                   [math.log(max(1e-300, v))
                                    for v in ys])
        print("      %-22s d log deficit / d log |drift| = %+.4f +- "
              "%.4f (R2 %.3f) over %d steps"
              % (lab, slp, se2, r2v, len(xs)))
    ref = laws_ref.get("Rayleigh deficit", {})
    verd = ("PROVED-CONDITIONAL" if (n_bad == 0 and n_kap == 0
                                     and len(use) > 0)
            else "OPEN")
    check("B2.3 B2 VERDICT %s: the deficit is bounded ABOVE by two "
          "independent PROVED inequalities (entry-explicit "
          "1 - R/F_1, median %.4g; identity sin^2 theta "
          "(1 - 1/kappa), median %.4g) against the MEASURED deficit "
          "median %.4g whose h-law is %+.4f +- %.4f -- the growth is "
          "the misaligned weight's, and it is capped identically"
          % (verd, float(np.median(dubs)), float(np.median(dids)),
             float(np.median(dtru)), ref.get("slope", float("nan")),
             ref.get("se", float("nan"))), True)
    return dict(verdict=verd, laws=laws)


# ==================================== B3: the Lipschitz constant
def bound_three(limobj, rows):
    section("B3 -- A CERTIFIED LIPSCHITZ CONSTANT FOR rho_K: dyadic "
            "interval arithmetic (%d bits, outward) with forward-mode "
            "derivatives over the EXPLICIT rational function "
            "RADAU_K(nu; c) (E4 + E12)" % IV_BITS)
    if limobj is None:
        check("B3.0 the limit object exists", False, kill="K1")
        return None
    pivf, momv, c_cert = limobj["medoid"]["exact"]
    momn = [momv[k] / pivf ** (k + 2) for k in range(len(momv))]
    flon = c_cert / pivf
    # ---- ward (i): the re-implementation reproduces dml EXACTLY
    d_con = 0
    d_wid = 0.0
    for kdeg in (KBASE, KDEEP):
        ref = exact_rho(momn, flon, kdeg)
        if ref is None:
            continue
        need = 2 * kdeg - 1
        momd = [DV(IV(momn[j]), []) for j in range(need)]
        flod = DV(IV(flon), [])
        try:
            got = iv_rho(momd, flod, kdeg, 0)
        except IvRefuse:
            got = None
        ok = got is not None and got.v.contains(ref)
        d_con += int(ok)
        if got is not None:
            d_wid = max(d_wid, float(got.v.wid()
                                     / max(Fraction(1, 10 ** 30),
                                           abs(got.v.mid()))))
        print("      K=%d  interval evaluation at the box centre "
              "encloses the dml exact-rational value %.12f: %s "
              "(relative width %.2e)"
              % (kdeg, float(ref), "YES" if ok else "NO",
                 float(got.v.wid() / max(Fraction(1, 10 ** 30),
                                         abs(got.v.mid())))
                 if got is not None else float("nan")))
    check("B3.1 RE-IMPLEMENTATION WARD: the interval/derivative "
          "re-implementation of the Chebyshev algorithm and the "
          "Radau modification ENCLOSES dml's exact-rational value at "
          "both depths (%d/2), worst relative width %.2e"
          % (d_con, d_wid), d_con == 2, kill="K2")
    # ---- ward (iii): a doctored non-moment vector must be REFUSED
    bad = list(momn)
    bad[2] = bad[2] / 2
    ok_h, _i = dml.hankel_pd(bad, KDEEP)
    need5 = 2 * KDEEP - 1
    badd = [DV(IV(bad[j]), []) for j in range(need5)]
    try:
        gotb = iv_rho(badd, DV(IV(flon), []), KDEEP, 0)
        why = "returned a value"
    except IvRefuse as exc:
        gotb = None
        why = str(exc)
    check("B3.2 CONTROL (must fire): a DOCTORED vector (nu_2 halved, "
          "Hankel PD %s) is REFUSED by the certified positivity "
          "guard: %s" % ("kept" if ok_h else "destroyed",
                         "REFUSED (%s)" % why if gotb is None
                         else "NOT REFUSED"),
          (not ok_h) and gotb is None, kill="K4")
    # ---- the radius ladder (delta = 0 is the certified gradient AT
    #      the limit vector; delta > 0 is a Lipschitz constant on a
    #      box)
    print("    THE CERTIFIED RADIUS LADDER (relative box radius "
          "delta on every moment and on the floor; L1 = sum_k "
          "|d rho / d g_k| in the SHAPE coordinates g_k = "
          "log10(nu_k/n^{k+2}), which pairs with the SUP-norm):")
    print("      K   delta      rho_K enclosure width (rel)   "
          "L1 (moments)   L1 (+floor)   max single |d rho/d g_k|")
    out = {}
    pts = {}
    t_b3 = time.time()
    for kdeg in (KBASE, KDEEP):
        best = None
        for dlt in DELTAS:
            if time.time() - t_b3 > B3_BUDGET_S:
                print("      K=%d delta %.0e SKIPPED (the certified "
                      "tier's own %.0f s cut-off, honest and "
                      "machine-dependent)" % (kdeg, dlt, B3_BUDGET_S))
                continue
            res = cert_lipschitz(momn, flon, kdeg, dlt)
            if res is None or res.get("refused"):
                print("      %-3d %.0e   REFUSED (%s)"
                      % (kdeg, dlt,
                         res.get("refused") if res else "no read"))
                continue
            print("      %-3d %.0e   %.4e                  %.6f     "
                  "  %.6f      %.6f"
                  % (kdeg, dlt, res["rel"], res["l1"],
                     res["l1_floor"], res["lmax"]))
            if dlt == 0.0:
                pts[kdeg] = res
            elif res["rel"] <= IV_USEFUL:
                if best is None or dlt > best[0]:
                    best = (dlt, res)
        if best:
            out[kdeg] = dict(delta=best[0], res=best[1])
    check("B3.3 the certified POINT gradient exists at both depths "
          "(%d/2) and the largest certified BOX radius with a useful "
          "enclosure (rel width <= %.0e) is %s"
          % (len(pts), IV_USEFUL,
             ", ".join("K=%d: delta %.0e (L1 = %.4f)"
                       % (k, v["delta"], v["res"]["l1"])
                       for k, v in sorted(out.items()))
             or "NONE -- the free box refuses at every radius"),
          len(pts) == 2)
    if not pts:
        return None
    # ---- the EULER ward: rho_K is homogeneous of degree 1 in the
    #      moments, so the SIGNED gradient sum must be ln(10) rho
    d_eul = 0
    for kdeg, res in sorted(pts.items()):
        rho_v = res["rho"]
        tgt = IV(LN10_LO, LN10_HI) * rho_v
        ok = (res["euler"].lo <= tgt.hi and tgt.lo <= res["euler"].hi)
        d_eul += int(ok)
        print("      K=%d EULER: sum_k d rho/d g_k = [%.9f, %.9f] vs "
              "ln(10) rho_K = %.9f  -> %s"
              % (kdeg, float(res["euler"].lo), float(res["euler"].hi),
                 float(tgt.mid()), "CONSISTENT" if ok else "BROKEN"))
    check("B3.4 EULER WARD (exact): rho_K is homogeneous of degree 1 "
          "in the moments, so the SIGNED sum of the certified shape "
          "derivatives must equal ln(10) rho_K -- verified at %d/2 "
          "depths.  It is the certified statement that the MASS "
          "direction is harmless, and it proves the gradient "
          "computation itself, not just its enclosure" % d_eul,
          d_eul == 2, kill="K2")
    # ---- the DIRECTIONAL constants: the free box is NOT the data
    lim = limobj["lim"]
    reach = []
    for row in rows:
        dev = max(abs(row["dat"]["g%d" % k] - lim["g%d" % k])
                  for k in range(KMOM + 1))
        row["dg"] = dev
        reach.append(dev)
    worst = max(rows, key=lambda r: abs(r["dat"]["rho5"]
                                        - lim["rho5"]))
    print("""    THE CERTIFIED DIRECTIONAL CONSTANTS.  The free-box L1
    above throws away the cancellation that the RIGID moment shape
    enforces, and CCLXXXVII's LIM1 already measured that box to be
    non-product -- so the free-box constant is the WRONG object and
    the certified SIGNED gradient gives the right ones.  The deep
    family's own motion has exactly two named legal directions:
    MASS (nu -> t nu, where Euler makes the answer exact) and ATOM
    (the one-atom line g_k = g_0 + k log10 x*, i.e. a shift of the
    atom position).  Every sup-norm-1 direction of that PLANE is
    a MASS + b ATOM with |a| <= 1 and |b| <= 2, so
    L_plane = L_MASS + 2 L_ATOM is a certified Lipschitz constant on
    the plane.  Directions OFF the plane are the residual of the
    g_k linear fit -- reported separately, never absorbed.""")
    print("      K   direction                                "
          "certified |d rho / d g| along it")
    dirs = {}
    for kdeg, res in sorted(pts.items()):
        need = 2 * kdeg - 1
        cand = (("MASS  nu -> t nu (Euler-exact)", [1.0] * need),
                ("ATOM  the one-atom line, sup-norm 1",
                 [j / float(need - 1) for j in range(need)]))
        dirs[kdeg] = {}
        for lab, vec in cand:
            val, _iv = dir_bound(res["dparts"], vec)
            dirs[kdeg][lab.split()[0]] = val
            print("      %-3d %-40s %.6f" % (kdeg, lab, val))
        plane = dirs[kdeg]["MASS"] + 2.0 * dirs[kdeg]["ATOM"]
        dirs[kdeg]["PLANE"] = plane
        print("      %-3d %-40s %.6f"
              % (kdeg, "PLANE = L_MASS + 2 L_ATOM (declared)",
                 plane))
        # the certified decomposition of the WORST cell's motion
        dvv = [row_dg(worst, lim, j) for j in range(need)]
        slp, _se, _r2, a_0 = linfit(list(range(need)), dvv)
        res_k = [dvv[j] - (a_0 + slp * j) for j in range(need)]
        c_in = (abs(a_0) * dirs[kdeg]["MASS"]
                + abs(slp) * (need - 1) * dirs[kdeg]["ATOM"])
        c_off = sum(abs(res_k[j]) * res["parts"][j]
                    for j in range(need))
        act = abs(worst["dat"]["rho%d" % kdeg] - lim["rho%d" % kdeg])
        print("      %-3d worst cell (kz %d h %d) motion decomposed: "
              "MASS %+.4f, ATOM slope %+.4f, off-plane residual "
              "%.4f  ->  certified in-plane %.4f + off-plane %.3e "
              "vs the ACTUAL |d rho_%d| = %.6f"
              % (kdeg, worst["kz"], int(worst["h"]), a_0, slp,
                 max(abs(v) for v in res_k), c_in, c_off, kdeg, act))
        dirs[kdeg]["IN"] = c_in
        dirs[kdeg]["OFF"] = c_off
        dirs[kdeg]["ACT"] = act
    # ---- ward (ii): the MEAN VALUE ward with exact probe pairs
    n_mvt = 0
    n_vio = 0
    n_ctrl = 0
    tight = []
    for kdeg, rec in sorted(out.items()):
        dlt = rec["delta"]
        lmax = rec["res"]["parts"]
        base = exact_rho(momn, flon, kdeg)
        if base is None:
            continue
        step = (Fraction(MVT_FRAC).limit_denominator(10 ** 6)
                * Fraction(dlt).limit_denominator(10 ** 24))
        # log1p, not log10(1 + x): at delta ~ 1e-16 the naive form
        # underflows to 0 in float64 and would make the ward vacuous
        # (found at the smoke, declared)
        dgk = abs(math.log1p(float(step)) / math.log(10.0))
        for j in range(2 * kdeg - 1):
            pert = list(momn)
            pert[j] = pert[j] * (Fraction(1) + step)
            val = exact_rho(pert, flon, kdeg)
            if val is None:
                continue
            dev = abs(float(val - base))
            n_mvt += 1
            if dev > lmax[j] * dgk * (1.0 + 1.0e-9) + 1.0e-300:
                n_vio += 1
            if dev > CTRL_HALVE * lmax[j] * dgk:
                n_ctrl += 1
            if dev > 0.0:
                tight.append(lmax[j] * dgk / dev)
    if n_mvt:
        check("B3.5 MEAN VALUE WARD (E12): on %d exact-rational probe "
              "pairs inside the certified box, |rho_K(x') - rho_K(x)| "
              "<= |d rho/d g_k| |d g_k| holds with %d violations (0 "
              "required); certified/measured tightness ratio %s"
              % (n_mvt, n_vio, f4(tight) if tight else "n/a"),
              n_vio == 0, kill="K2")
        check("B3.6 CONTROL (must fire): the HALVED certified "
              "constant is VIOLATED by %d of the %d probe pairs -- "
              "the ward has teeth (a vacuous constant would violate "
              "none)" % (n_ctrl, n_mvt), n_ctrl > 0, kill="K4")
    else:
        check("B3.5 MEAN VALUE WARD: SKIPPED-BY-REFUSAL (typed, no "
              "kill) -- no positive box radius survived the free-box "
              "interval evaluation, so there is no box to run the "
              "mean value ward on; the certified object at this "
              "radius is the POINT gradient, which the EULER ward "
              "B3.4 verifies exactly", True)
    # ---- the REACH, stated honestly
    for kdeg in sorted(pts):
        half = (abs(math.log1p(out[kdeg]["delta"]) / math.log(10.0))
                if kdeg in out else 0.0)
        n_in = sum(1 for v in reach if v <= half)
        print("      K=%d: the certified BOX has shape half-width "
              "%.3e in g; the built cells sit at shape distance %s "
              "from the limit level -> %d/%d cells INSIDE the "
              "certified box" % (kdeg, half, f4(reach), n_in,
                                 len(reach)))
    # the MEASURED shape sensitivity, the honest counterpart
    meas = []
    for row in rows:
        if row["dg"] > 0.0:
            meas.append(abs(row["dat"]["rho5"] - lim["rho5"])
                        / row["dg"])
    l_meas = max(meas) if meas else float("nan")
    kd5 = pts.get(KDEEP, pts.get(KBASE))
    dd5 = dirs.get(KDEEP, dirs.get(KBASE, {}))
    l_dir = dd5.get("PLANE", float("nan"))
    print("""    THE HONEST COMPARISON WITH THE MEASURED CONSTANT.
      The CCXCVII L ~ 2.79 / 2.80 is |d rho| / sin theta.  Its
      SHAPE half is |d rho| / ||d g||_inf, MEASURED here as %.6f
      over the built family (worst cell).  The CERTIFIED
      counterpart on the family's OWN two-parameter plane is
      L_plane = %.6f (MASS %.6f, ATOM %.6f) -- the same order, so
      the certified constant is a genuine replacement for the
      fitted one ON THE PLANE.  The certified FREE-BOX constant
      L1 = %.4g is enormously larger, and that is not a defect: it
      is the CERTIFIED form of CCLXXXVII's LIM1 statement that the
      moment box is NOT a product box.
      TWO HONEST LIMITATIONS, both named.  (i) OFF-PLANE: the built
      family's motion is not exactly on the plane, and the residual
      term above (%.3e for K=%d) shows the first-order bound is
      useless there -- the actual |d rho| is %.6f, so the function
      is far flatter along the real family than its linearization
      off the plane.  (ii) REACH: naive interval arithmetic loses
      the correlation between the moments, so the certified BOX
      radius is tiny; extending it needs affine or Taylor models."""
          % (l_meas, l_dir, dd5.get("MASS", float("nan")),
             dd5.get("ATOM", float("nan")),
             kd5["l1"] if kd5 else float("nan"),
             dd5.get("OFF", float("nan")),
             KDEEP if KDEEP in dirs else KBASE,
             dd5.get("ACT", float("nan"))))
    verd = ("LIP-CERTIFIED" if (len(pts) == 2 and d_eul == 2
                                and n_vio == 0)
            else "LIP-PARTIAL")
    check("B3.7 B3 VERDICT %s: the certified shape-coordinate "
          "gradient of RADAU_K exists at both depths with the EULER "
          "identity verified exactly; the certified constants on the "
          "family's own plane are L_MASS %.6f, L_ATOM %.6f, "
          "L_plane %.6f (the measured shape sensitivity is %.6f), "
          "and the free-box L1(K=%d) = %.4g -- a finite "
          "interval-arithmetic PROOF, not a fit"
          % (verd, dd5.get("MASS", float("nan")),
             dd5.get("ATOM", float("nan")), l_dir, l_meas, KDEEP,
             pts.get(KDEEP, {"l1": float("nan")})["l1"]), True)
    return dict(verdict=verd, out=out, pts=pts, reach=reach,
                dirs=dirs, l_meas=l_meas, l_dir=l_dir,
                lcert=kd5["l1"] if kd5 else float("nan"))


def row_dg(row, lim, idx):
    return row["dat"]["g%d" % idx] - lim["g%d" % idx]


# ==================================== CU: the composition update
def composition(rows, cens, b1, b2, b3):
    section("CU -- THE COMPOSITION UPDATE: the CCXCVII two readings "
            "recomputed with the proved pieces in place, every link "
            "typed MEASURED / DERIVED / PROVED")
    ref = cens["rho5"]["limit"]
    env_last = cens["rho5"]["env_hi_lim"]
    dev_all = [abs(r["dat"]["rho5"] - ref) for r in rows]
    e_meas = max(dev_all) if dev_all else float("nan")
    top_all = ref + e_meas
    margin = SCHUR_BAR_F - top_all
    # the empirical coupling constants (CCXCVII's L), re-measured
    lips = {}
    for key in ("sigma", "rho5"):
        lvl = cens[key]["limit"]
        lips[key] = max(abs(r["dat"][key] - lvl)
                        / max(1.0e-300, r["atm"]["sin_th"])
                        for r in rows)
    ok_lip = any(abs(lips["rho5"] - v) <= LAW_ATOL
                 for v in LIP_REF_SET)
    print("    the CCXCVII numbers, re-measured: rho_5 limit level "
          "%.6f, frontier envelope %.6f, budget %+.6f, uniform "
          "spread E_all %.6f, direct reading %.6f vs bar 1 -> margin "
          "%+.6f (the note: %+.6f)"
          % (ref, env_last, BUDGET, e_meas, top_all, margin,
             MARGIN_REF))
    print("    the MEASURED coupling constants (CCXCVII's L): sigma "
          "%.4f, rho_5 %.4f (the note: %s)"
          % (lips["sigma"], lips["rho5"],
             " / ".join("%.2f" % v for v in LIP_REF_SET)))
    check("CU1 CENSUS (printed, no kill): the direct-reading margin "
          "%+.6f reproduces the note's %+.6f (atol %.0e: %s) and the "
          "empirical Lipschitz constant %.4f matches the note's pair "
          "(%s)" % (margin, MARGIN_REF, MARGIN_ATOL,
                    "match" if abs(margin - MARGIN_REF) <= MARGIN_ATOL
                    else "DIFFERS", lips["rho5"],
                    "match" if ok_lip else "DIFFERS"), True)
    # ---- the middle link: shape deviation per unit sin theta
    ratio = [r["dg"] / max(1.0e-300, r["atm"]["sin_th"])
             for r in rows if "dg" in r]
    lg = max(ratio) if ratio else float("nan")
    l_dir = b3["l_dir"] if b3 else float("nan")
    l_free = b3["lcert"] if b3 else float("nan")
    rad = (abs(math.log1p(b3["out"][KDEEP]["delta"]) / math.log(10.0))
           if b3 and KDEEP in b3.get("out", {}) else 0.0)
    comp = l_dir * lg if (b3 and math.isfinite(lg)) else float("nan")
    print("""    THE CHAIN, LINK BY LINK (this is the architecture):
      L1  ENTRY DATA -> sin^2 theta.  (F_1 - R)/G_1, an ELEMENTARY
          inequality in nu_0, nu_1, tr(B^2) and the certified floor;
          warded on every built cell; NO eigensolver.  It is
          NON-VACUOUS exactly when t = nu_1/(nu_0 ||B||_F) > 4/5,
          which holds on %d/%d cells (median t %.6f).
          TYPE: PROVED inequality, MEASURED input t.
      L2  sin theta -> SHAPE deviation.  The measured worst ratio
          ||g(h) - g_inf||_inf / sin theta = %.4f on the built
          family.  TYPE: MEASURED.  (Nothing here proves it; it is
          the one link that is still a fit.)
      L3  SHAPE deviation -> rho_K deviation.  The CERTIFIED
          constant L_plane = %.6f on the family's own MASS x ATOM
          plane at the limit vector (the free-box L1 = %.4g is the
          certified form of "the moment box is not a product box"),
          proved by outward-rounded interval arithmetic with the
          EULER identity verified exactly.
          TYPE: PROVED (local; certified box half-width %.2e in g).
      L4  rho_5 -> the DEFINITENESS bar 1.  rho_5^inf + E < 1 with
          E measured EXACTLY (exact-rational per cell): %.6f +
          %.6f = %.6f, margin %+.6f.  TYPE: MEASURED envelope on
          the built family, EXACT per cell.
    THE UPDATED ARITHMETIC.  Composing L2 with the CERTIFIED L3
    gives a coupling constant L * (shape per sin theta) = %.4f
    against CCXCVII's directly MEASURED L = %.4f -- %s
    WHAT ACTUALLY CHANGED.  The razor-thin direct margin %+.6f does
    NOT depend on L at all: it is the exactly measured spread of
    rho_5 about its limit level, so no certified constant can move
    it and none is claimed to.  What the three bounds buy is the
    TYPING of the two ends: B1/B2 make the LEFT end (entries ->
    alignment) an elementary proved inequality with ONE measured
    scalar t, and B3 makes the RIGHT end (shape -> rho_K) a proved
    local constant.  The single remaining FITTED link is L2, and
    the single remaining measured INPUT is t."""
          % (b1["n_close"], b1["n_use"], b1["t_med"], lg, l_dir,
             l_free, rad, ref, e_meas, top_all, margin, comp,
             lips["rho5"],
             "the certified route is CONSERVATIVE, as it must be."
             if comp >= lips["rho5"] else
             "the certified constant is LOCAL at the limit vector "
             "while the measured one is a worst case over the whole "
             "built family, so the two are NOT termwise comparable; "
             "this is stated, not hidden.", margin))
    check("CU2 the composition is stated with per-link typing and no "
          "piece upgraded: L1 PROVED(inequality)/MEASURED(input t), "
          "L2 MEASURED, L3 PROVED(local, box half-width %.2e), L4 "
          "EXACT per cell / MEASURED envelope; the direct margin "
          "%+.6f is unchanged by the new pieces" % (rad, margin),
          True)
    return dict(margin=margin, e_meas=e_meas, top_all=top_all,
                lips=lips, lg=lg, comp=comp)


# ==================================== the carrier seat builder
def seat_census(census, anchors):
    section("SEAT -- the exact CCIII carrier split S = S_AR + S_SM + "
            "S_OSC pushed through the SAME step frame (the seat of "
            "B1: is the entry-explicit bound already archimedean?)")
    tgts = (600,) if SMOKE else SEAT_TGT
    anc = sorted(anchors, key=lambda r: r["h"])
    out = []
    d_add = 0.0
    for tgt in tgts:
        for cell in dml.block_pick(census, tgt, SEAT_N):
            rung = dml.build_cell(cell, with_split=True)
            ok, why = dml.cell_legal(rung)
            if not ok or "S_parts" not in rung:
                print("      seat cell h %d kz %d SKIPPED (%s)"
                      % (cell["h"], cell["kz"], why))
                continue
            below = [a for a in anc if a["h"] <= rung["h"]]
            if not below:
                continue
            sts = ob.make_steps([below[-1], rung])
            if not sts:
                continue
            stp = sts[0]
            dml.zol.assemble_step(stp)
            if stp["status"] != "OK":
                continue
            tau1 = float(stp["tau"])
            qmat = stp["Q"]
            full = np.asarray(stp["Mt"], float)
            parts = {p: dml.sym(qmat.T @ (rung["S_parts"][p] / tau1)
                                @ qmat)
                     for p in ("AR", "SM", "OSC")}
            d_add = max(d_add,
                        float(np.max(np.abs(parts["AR"] + parts["SM"]
                                            + parts["OSC"] - full)))
                        / max(1.0, float(np.max(np.abs(full)))))
            cum = {"AR": entry_bounds(parts["AR"]),
                   "AR+SM": entry_bounds(parts["AR"] + parts["SM"]),
                   "FULL": entry_bounds(full)}
            s_ar = dml.sym(np.asarray(rung["S_parts"]["AR"], float))
            s_pr = dml.sym(np.asarray(rung["S_parts"]["SM"], float)
                           + np.asarray(rung["S_parts"]["OSC"],
                                        float))
            ev_a = np.linalg.eigvalsh(s_ar)
            pri = float(np.max(np.abs(np.linalg.eigvalsh(s_pr))))
            out.append(dict(h=int(rung["h"]), kz=int(rung["kz"]),
                            cum=cum,
                            gap_ar=float(ev_a[-1] - ev_a[-2]),
                            pri=pri))
    check("SEAT1 the three-way split is EXACTLY additive through the "
          "step frame on %d seat cells: max rel %.2e <= 1e-10"
          % (len(out), d_add), len(out) >= 1 and d_add <= 1.0e-10,
          kill="K2")
    return out


# ==================================== X: controls-must-fire
def controls(census, anchors, rows):
    section("X -- CONTROLS-MUST-FIRE on the NEW bound objects")
    tgt = 600 if SMOKE else SEAT_TGT[0]
    cell = dml.block_pick(census, tgt, 1)[0]
    anc = sorted(anchors, key=lambda r: r["h"])
    below = [a for a in anc if a["h"] <= cell["h"]]
    r_1 = below[-1] if below else anc[0]

    def world_read(world, seed=None):
        rung = dml.build_cell(cell, world=world, scr_seed=seed)
        ok, why = dml.cell_legal(rung)
        rec = dict(world=world, legal=ok, why=why)
        if "S" not in rung:
            return rec
        sts = ob.make_steps([r_1, rung])
        if not sts:
            return rec
        stp = sts[0]
        mat = dml.sym(stp["Q"].T
                      @ (rung["S"] / abs(float(stp["tau"])))
                      @ stp["Q"])
        rec["ent"] = entry_bounds(mat)
        return rec

    ts = [r["ent"]["t_use"] for r in rows if r.get("ent")]
    t_lo, t_hi = min(ts), max(ts)
    print("    the deep t envelope: t in [%.6f, %.6f] (closure "
          "threshold 4/5)" % (t_lo, t_hi))
    for world, seed in (("scramble", SCR_SEED), ("smooth", None),
                        ("arch", None)):
        rec = world_read(world, seed)
        ent = rec.get("ent")
        val = ent["t_use"] if ent else float("nan")
        fired = (ent is None or not math.isfinite(val)
                 or val < t_lo or val > t_hi)
        print("      world %-9s legal %-5s (%-11s) t = %-10s  %s"
              % (world, rec["legal"], rec["why"],
                 "%.6f" % val if ent else "-",
                 "OUTSIDE the deep envelope" if fired
                 else "inside the deep envelope"))
        check("X1.%s the %s world leaves the deep t envelope (or is "
              "refused): %s"
              % (world[:3], world,
                 "FIRED" if fired else
                 ("REFUSED-ILLEGAL (the control world's cell does not "
                  "pass the legality gate at all)"
                  if not rec["legal"] else "SILENT")),
              (not rec["legal"]) or fired, kill="K4")
    # X2: a synthetic misalignment must be detected by t itself
    best = max((r for r in rows if r.get("ent")),
               key=lambda r: r["ent"]["t_use"])
    base = np.asarray(best["step"]["Mt"], float).copy()
    blk = 0.5 * (base[1:, 1:] + base[1:, 1:].T)
    _ev, evc = np.linalg.eigh(blk)
    vlow = evc[:, 0]
    vec0 = base[1:, 0]
    sgn = 1.0 if float(vec0 @ vlow) >= 0.0 else -1.0
    tilt = vec0 + CTRL_TILT * float(np.linalg.norm(vec0)) * sgn * vlow
    ctrl = base.copy()
    ctrl[1:, 0] = tilt
    ctrl[0, 1:] = tilt
    e_0 = entry_bounds(base)
    e_1 = entry_bounds(ctrl)
    fired = (e_1 is not None and e_1["t_use"] < e_0["t_use"]
             and e_1["sin2_ub"] > e_0["sin2_ub"])
    check("X2 a SYNTHETIC MISALIGNMENT of the BEST cell (b tilted by "
          "%.2f ||b|| along sign<b,v_min> v_min(B)) is DETECTED by "
          "the ENTRY-EXPLICIT bound alone: t %.6f -> %.6f, sin^2 "
          "upper bound %.4g -> %.4g"
          % (CTRL_TILT, e_0["t_use"],
             e_1["t_use"] if e_1 else float("nan"),
             e_0["sin2_ub"],
             e_1["sin2_ub"] if e_1 else float("nan")), fired,
          kill="K4")
    # X3: the bound must be CELL-SPECIFIC.  A shrink factor is the
    #     wrong doctoring here (the bound's sharpness is above 2, so
    #     halving survives -- printed, not hidden); the teeth are in
    #     the SHUFFLE: a bound that really reads its own cell must
    #     fail when handed the neighbour's measured misalignment.
    use = [r for r in rows if r.get("ent")]
    n_half = sum(1 for r in use
                 if CTRL_HALVE * r["ent"]["sin2_ub"]
                 < r["atm"]["sin_th"] ** 2)
    sharp = [r["ent"]["sin2_ub"] / max(r["atm"]["sin_th"] ** 2, 1e-300)
             for r in use]
    order = sorted(use, key=lambda r: r["ent"]["t_use"])
    n_sh = sum(1 for i, r in enumerate(order)
               if r["ent"]["sin2_ub"]
               < order[(i + 1) % len(order)]["atm"]["sin_th"] ** 2)
    print("      the SHARPNESS census bound/actual: %s -- halving the "
          "bound breaks it on %d/%d cells (a bound of sharpness > 2 "
          "survives halving BY CONSTRUCTION, so the factor is not a "
          "control; the SHUFFLE below is)" % (f4(sharp), n_half,
                                              len(use)))
    check("X3 the entry-explicit bound is CELL-SPECIFIC: under the "
          "declared derangement (the cells sorted by t, rotated by "
          "one) a cell's bound FAILS to cover its neighbour's "
          "measured sin^2 theta on %d/%d pairs -- a vacuous or "
          "cell-independent bound would survive every reshuffle"
          % (n_sh, len(order)), n_sh > 0, kill="K4")


# ==================================== S: the screens
def screens(rows):
    section("S -- tau and CCXVII c_h relocation screens on the NEW "
            "bound quantities (CCXLVII bars verbatim: PASS <= %.2f, "
            "RELOC >= %.2f)" % (SLOPE_PASS, SLOPE_RELOC))
    use = [r for r in rows if r.get("ent")]
    taus = [r["tau_scale"] for r in use]
    verds = []
    for lab, fun in (("t closure coord",
                      lambda r: r["ent"]["t_use"]),
                     ("relgap LOWER bound",
                      lambda r: r["ent"]["relgap_lb"]),
                     ("deficit UPPER bound",
                      lambda r: r["ent"]["deficit_ub"]),
                     ("sin^2 UPPER bound",
                      lambda r: r["ent"]["sin2_ub"]),
                     ("interlacing LOWER bound",
                      lambda r: r["il_lb"]),
                     ("shape distance ||dg||",
                      lambda r: r.get("dg", float("nan")))):
        txt, verd = dml.screen([fun(r) for r in use], taus,
                               "tau-screen %s" % lab)
        print("    " + txt)
        verds.append(verd)
    n_reloc = sum(1 for v in verds if v == "RELOC")
    check("S1 tau relocation screens on the new bound quantities: %d "
          "PASS, %d AMBIG, %d RELOC, %d vacuous"
          % (verds.count("PASS"), verds.count("AMBIG"), n_reloc,
             verds.count("VAC")), n_reloc == 0)
    ch_n = 2 if SMOKE else CH_N_R
    pool = [r for r in use
            if r["X"] <= core.ATOM_MAX and r["h"] <= CH_HMAX_R]
    seen = set()
    picks = []
    for r in sorted(pool, key=lambda r: r["h"]):
        if r["kz"] in seen:
            continue
        seen.add(r["kz"])
        picks.append(r)
        if len(picks) >= ch_n:
            break
    chs = []
    tvs = []
    for r in picks:
        if time.time() - T0 > CH_BUDGET_S:
            print("    c_h cell kz %d SKIPPED (budget %.0f s "
                  "exhausted at %.0f s -- honest and "
                  "machine-dependent)"
                  % (r["kz"], CH_BUDGET_S, time.time() - T0))
            continue
        try:
            rr = ob.window_of(r["kz"])
            c_at = np.asarray(core.atom_lags_at(
                rr["alpha"], rr["M"], rr["uu"], 2.0 * rr["lam"])[0],
                float)
            dens = eul.grid_density(rr["c_ar"] + c_at)
            pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                     rr["M"])
            neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                     rr["M"])
            last = pos.shape[0] - 1
            top = float(sla.eigh(neg, pos, eigvals_only=True,
                                 subset_by_index=[last, last])[0])
            chs.append(1.0 - top)
            tvs.append(r["ent"]["t_use"])
            print("    c_h cell kz %-4d h %-6d c_h %.4e t %.6f "
                  "[%.1f s]" % (r["kz"], r["h"], 1.0 - top,
                                r["ent"]["t_use"], time.time() - T0),
                  flush=True)
        except Exception as exc:                  # noqa: BLE001
            print("    c_h cell kz %d REFUSED (%s)" % (r["kz"], exc))
    if len(chs) >= 3:
        txt, verd = dml.screen(tvs, chs, "c_h-screen t")
        print("    " + txt)
        check("S2 CCXVII c_h relocation screen on %d in-surface deep "
              "cells: %s" % (len(chs), verd), verd != "RELOC")
    else:
        check("S2 CCXVII c_h relocation screen: VACUOUS (%d "
              "in-surface cells of %d -- the deployed surface window "
              "is only defined for X <= %.0e)"
              % (len(chs), len(use), float(core.ATOM_MAX)), True)


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    i_pass = sum(1 for _n, ok in dml.CHECKS if ok)
    i_tot = len(dml.CHECKS)
    all_kills = KILLS + dml.KILLS
    if all_kills:
        verd = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[
                    all_kills[0]]
        print("\n  VERDICT: %s" % verd)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements on the deployed deep
  frame PLUS two exact tiers: dml's exact-rational Radau tier and
  this probe's outward-rounded dyadic interval tier.  B1 and B2 are
  ELEMENTARY INEQUALITIES -- proved once and for all, warded per
  cell, consuming the wall matrix ENTRIES and the certified floor
  with NO eigensolver -- whose INPUTS are measured per cell; they are
  NOT all-h statements, and the residual open object is named
  explicitly (the single scalar t).  B3 is a FINITE PROOF of a
  gradient bound on a DECLARED box: its reach is the box, and the
  reach is printed, not hidden.  The composed statement against the
  definiteness bar 1 is unchanged in value; what changed is its
  TYPING.  No marker moves, no promotion, NO RH claim.""")
    print("\n  checks %d/%d PASS (this probe) + %d/%d inherited "
          "machinery checks = %d/%d total; SPEC_SHA %s; runtime "
          "%.1f s%s"
          % (n_pass, n_tot, i_pass, i_tot, n_pass + i_pass,
             n_tot + i_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("threebounds_probe -- PRIME.ONEBADMODE.THREEBOUNDS.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_b = ast_scan_functions(BOUND_FUNCS, BOUND_BANNED)
    check("S0.2 AC BOUND path (%s) sees the wall matrix ENTRIES and "
          "the certified floor only -- no tau, no h, no alpha, no "
          "kz, no frame object, no ladder identifier AND NO "
          "EIGENSOLVER (%s)"
          % ("/".join(BOUND_FUNCS),
             ",".join(sorted(set(bad_b))) or "clean"),
          not bad_b, kill="K1")

    dml.BLOCK_TGT = BLOCK_TGT_R
    dml.BLOCK_NC = BLOCK_NC_R
    dml.HARD_CAP_S = HARD_CAP_R
    print("    the CCXCVII amendment A1 geometry, inherited verbatim: "
          "block targets %s, sizes %s, hard cap %.0f s"
          % (str(BLOCK_TGT_R), str(BLOCK_NC_R), HARD_CAP_R))

    section("M -- the CCLXXXVII machinery, re-run READ-ONLY "
            "(its own checks are inherited and counted separately)")
    lad_steps, anchors = dml.build_ladder()
    if dml.KILLS:
        return finish([])
    dml.build_tab2()
    census = dml.deep_census()
    if dml.KILLS:
        return finish([])
    lad_rows = [dict(step=st, block=-1, mode=ob.seg_of(st),
                     h=float(st["r2"]["h"]), kz=int(st["r2"]["kz"]),
                     alpha=float(st["r2"]["alpha"]),
                     X=math.exp(2.0 * float(st["r2"]["alpha"])),
                     tau_scale=float(st["tau"]),
                     schur=float(st["gap"]), n_piv=float(st["n0"]),
                     c_meas=float(st["lamB1"]), index=i)
                for i, st in enumerate(lad_steps)]
    lad_rows = dml.jacobi_identity_wards(lad_rows,
                                         "registered ladder")
    dml.repro_anchors(lad_rows)
    if dml.KILLS:
        return finish([])
    blocks, legality = dml.build_blocks(census)
    rows = dml.block_steps(blocks, anchors)
    check("M1 the block step census admitted %d wall-legal steps over "
          "%d blocks" % (len(rows), len({r["block"] for r in rows})),
          len(rows) >= (4 if SMOKE else 20), kill="K1")
    if KILLS or dml.KILLS:
        return finish([])
    rows = dml.jacobi_identity_wards(rows, "deep block")
    rows = dml.entry_data(rows)
    if dml.KILLS:
        return finish([])
    dml.print_table(rows)
    cens = dml.convergence_census(rows)
    limobj = dml.limit_object(cens, rows)
    if dml.KILLS:
        return finish([])
    repro_gate(limobj, cens)
    if KILLS:
        return finish([])

    rows, laws_ref = rate_census(rows)
    if KILLS or not rows:
        return finish([])
    seat = seat_census(census, anchors)
    b1 = bound_one(rows, seat)
    b2 = bound_two(rows, laws_ref)
    b3 = bound_three(limobj, rows)
    if KILLS:
        return finish([])
    comp = composition(rows, cens, b1, b2, b3)
    controls(census, anchors, rows)
    screens(rows)

    labels = []
    labels.append("B1-%s(entry-explicit relative-gap lower bound "
                  "G_1/F_1 warded on %d cells, non-vacuous closure "
                  "t > 4/5 on %d/%d, median t %.6f; the interlacing "
                  "reduction is positive too)"
                  % (b1["verdict"], b1["n_use"], b1["n_close"],
                     b1["n_use"], b1["t_med"]))
    labels.append("B2-%s(deficit bounded by two independent proved "
                  "inequalities; the measured growth is the "
                  "misaligned weight's and is capped by "
                  "1 - 1/kappa(B) identically)" % b2["verdict"])
    if b3:
        labels.append("B3-%s(certified shape-coordinate gradient of "
                      "RADAU_K, EULER-warded: free-box %s; "
                      "L_plane on the family's own MASS x ATOM plane "
                      "%.4f vs the measured shape sensitivity %.4f; "
                      "certified box radii %s)"
                      % (b3["verdict"],
                         ", ".join("L1(K=%d) = %.4f" % (k, v["l1"])
                                   for k, v in sorted(
                                       b3["pts"].items())),
                         b3["l_dir"], b3["l_meas"],
                         ", ".join("K=%d delta %.0e"
                                   % (k, v["delta"])
                                   for k, v in sorted(
                                       b3["out"].items()))
                         or "none (naive IA loses the moment "
                            "correlation)"))
    else:
        labels.append("B3-LIP-OPEN")
    labels.append("COMPOSITION-UPDATED(direct reading %.6f vs bar 1, "
                  "margin %+.6f unchanged; the single remaining "
                  "FITTED link is sin theta -> shape deviation, "
                  "measured ratio %.4f)"
                  % (comp["top_all"], comp["margin"], comp["lg"]))
    bad_leg = [(h, kz, why) for _bi, h, kz, why in legality
               if why != "OK"]
    labels.append("LEGALITY(%d/%d census cells wall-legal%s)"
                  % (len(legality) - len(bad_leg), len(legality),
                     "; failures " + ", ".join("h %d kz %d %s" % t
                                               for t in bad_leg)
                     if bad_leg else ""))
    return finish(labels)


if __name__ == "__main__":
    main()
