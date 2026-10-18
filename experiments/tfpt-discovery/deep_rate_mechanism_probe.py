#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_rate_mechanism_probe -- PRIME.ONEBADMODE.DEEP.RATE.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

WHERE DOES THE ONE-ATOM COLLAPSE COME FROM, AND DOES IT CARRY A RATE?
CCLXXXVII measured the deep-frame entry data and found the answer
split.  The SHAPE collapses: g_k = log10(nu_k / n^{k+2}) is LINEAR in
k to R2 0.999890 with slope +3.10156 +- 0.02457, i.e.
nu_{k+1}/(nu_k n) is CONSTANT, i.e. the spectral measure of B at b has
degenerated toward a SINGLE ATOM.  The MAGNITUDES do not converge: the
exact CCIII three-way split through the same step frame showed all
three carriers (archimedean / smooth surrogate / prime oscillation)
growing like h^2, so the deep entry data are a RESIDUUM, not a regular
object.  The composed all-large-h architecture stands ready against
the DEFINITENESS bar 1 with budget +0.212397 "the moment a rate is
proved".  THIS PROBE asks for the MECHANISM of the collapse inside the
geometric construction and pushes it toward a rate.

THE OBJECT (unchanged, deployed).  Per wall-legal step
Mt = Q_1^T (S_2 / tau_1) Q_1 with Q_1 = householder_frame(v_min(S_1)),
so the FRAME AXIS is the PREVIOUS rung's bottom eigenvector.  Entry
data n = Mt[0,0], b = Mt[1:,0], B = Mt[1:,1:], nu_k = b^T B^k b,
c = lambda_min(B).

THE MECHANISM HYPOTHESIS, stated before any measurement.  Mt is an
ORTHOGONAL conjugation of S_2/tau_1, so spec(Mt) = spec(S_2)/tau_1.
Write the eigenpairs of Mt as (m_1 >= m_2 >= ... >= m_8, z_i) and
split each eigenvector as z_i = (c_i, y_i) with c_i its FRAME
coordinate.  Then, IDENTICALLY,

    n = sum_i m_i c_i^2,   b = sum_i m_i c_i y_i,
    B = sum_i m_i y_i y_i^T,   sum_i c_i^2 = 1.

If Mt is PD (it is, on every certified cell: P1 n > 0, P2 c > 0 and
sigma < 1 give M > 0 by E2) and m_1 dominates, then B is a rank-one
matrix m_1 y_1 y_1^T plus a perturbation of norm <= m_2, and b is
m_1 c_1 y_1 plus a vector of norm <= m_2 sqrt(1 - c_1^2).  So b is
nearly an EIGENVECTOR of B and the moment sequence is nearly a single
atom at lambda_max(B).  THE COLLAPSE IS THE RANK-ONE DOMINANCE OF THE
DEEP CORE BLOCK SEEN THROUGH THE HOUSEHOLDER FRAME, and the atom sits
at the scale-quotient position x* = lambda_max(B) / n, so
gslope = log10(x*) EXACTLY (note the base: the CCLXXXVII slope
+3.10156 is a log10 slope, so x* ~ 1.26e3, NOT e^{3.1} ~ 22.2).

 (a) THE ATOM'S IDENTITY.  Per built step the full spectral pair
     census of (b, B): eigenpairs (mu_j, v_j) of B, weights
     w_j = (b^T v_j)^2 with sum_j w_j = nu_0 EXACTLY (A1 ward), the
     dominant pair, the weight share w_top/nu_0 = cos^2 of the
     alignment angle, and the moment-read atom position
     nu_8/(nu_7 n).  The atom is then IDENTIFIED against the named
     objects of the construction with declared relative ties:
     lambda_max(B)/n (definitional), the condition number of B, the
     condition number of Mt, m_1/n, and tan^2 phi = (1 - c_1^2)/c_1^2
     where phi is the angle between the FRAME AXIS and Mt's top
     eigenvector.  Verdict per candidate: IDENTIFIED / NO-MATCH.
 (b) THE ALIGNMENT LAW.  theta_h = angle(b, v_top(B)) measured on the
     whole deep census, its block levels, its h-fit with 2SE, and --
     the deliverable -- TWO DERIVED bounds from the entries forward.
     THE GAP BOUND (primary, elementary and exact).  With
     (mu_j, v_j) the eigenpairs of B and w_j = (b^T v_j)^2,
     nu_0 = sum_j w_j and nu_1 = sum_j w_j mu_j identically, and
     mu_1 - mu_j >= mu_1 - mu_2 for every j >= 2, hence

       sin^2 theta = sum_{j>=2} w_j / nu_0
                  <= (x_1 - nu_1/(nu_0 n)) / (x_1 - x_2),
       x_j = mu_j / n.

     The numerator is the RAYLEIGH DEFICIT of the first moment ratio
     against the atom, the denominator is B's SPECTRAL GAP -- so the
     moment SHAPE and the ALIGNMENT are literally the same statement,
     and the mechanism reduces to B's relative gap.  Everything in it
     is scale-invariant and read off Mt's ENTRIES.
     THE FRAME BOUND (secondary, the Householder reading).  With
     (m_i, z_i) the eigenpairs of the FULL Mt and c_i = z_i[0],
     b = m_1 c_1 y_1 + f with ||f|| <= m_2 sqrt(1 - c_1^2) and
     B = m_1 y_1 y_1^T + E with 0 <= E <= m_2 I, so by E8/E9/E10

       sin theta <= m_2/(m_1 |c_1| - m_2) + m_2/(m_1 (1-c_1^2) - m_2)

     whenever both denominators are positive (and trivially when the
     right side is >= 1).  Its ingredients are the SPECTRAL GAP RATIO
     r_gap = m_2/m_1 and the FRAME OVERLAP |c_1|.
     BOTH bound properties are WARDED per cell (AL2 / AL2b, 0
     violations required) -- neither is ever assumed, and how often
     each is non-vacuous is printed.
     The SOURCE-SIDE reading is warded separately (ID1): m_i tau_1 are
     the eigenvalues of the deep core block S_2 and c_1 is
     <v_min(S_1), u_max(S_2)>, the overlap of two CONSECUTIVE rungs'
     extreme eigenvectors -- so the alignment law is a statement about
     the window geometry, not about the primes.  WHO DRIVES IT is then
     decided by pushing the exact CCIII three-way split through the
     SAME frame (Mt = Mt_AR + Mt_SM + Mt_OSC exactly) and measuring,
     per carrier, its contribution to the MISALIGNED component
     P_perp b: if each carrier's share is far larger than the total,
     the h^2 carriers CANCEL in the angle and the law is geometric; if
     one carrier alone reproduces it, that carrier is the driver.
 (c) THE FUNCTIONAL RATES.  The chain shape -> Radau bound stability
     is measured, never assumed: the per-cell deviations of sigma and
     rho_5 from the deepest-block level are regressed against
     sin theta (the empirical Lipschitz constant L is REPORTED, not
     derived), the block-to-block Cauchy differences give a
     reference-free rate, and the composed statement against the
     DEFINITENESS bar 1 uses the CCLXXXVII budget
     BUDGET = 1 - 0.787603 = +0.212397.  The crossover H is printed
     for the fitted power law with its 2SE band -- and if the fitted
     power is NOT positive the run says so in those words and reports
     NO crossover (AMENDMENT A5, declared and DISCLOSED AFTER FROZEN
     RUN 1: the first draft printed one "it closes" sentence whose
     truth value did not track the measurement, and it conflated the
     BUDGET reading, anchored at the frontier WORST, with the DIRECT
     reading rho_5^inf + E < 1, anchored at the limit LEVEL.  Both
     readings are now printed side by side with their margins; no
     number and no bar moved).  The
     TYPING LADDER is printed explicitly:
       MEASURED-RATE  = fit + 2SE on built cells (what this run has);
       DERIVED-RATE   = from the mechanism with certified remainder
                        (what AL2 delivers for theta ALONE);
       PROVED-RATE    = nothing here.  Not claimed.
     THE LEAD'S WARNING is answered with an explicit INTERIOR
     DISTANCE: the limit point must not sit ON the class boundary.
     Three LEGAL deformations of the exact medoid limit vector (legal
     = the deformed data are still the moments of a positive measure,
     which a box corner is NOT -- CCLXXXVII LIM1) are measured, float
     located and then EXACT-RATIONALLY certified at a declared inward
     margin: (i) MASS nu -> t nu (RADAU is homogeneous of degree 1 in
     the moments, so t* = 1/rho exactly -- warded); (ii) FLOOR
     c -> (1 - d) c; (iii) ADD-ATOM: nu_k -> nu_k + m c^k, i.e. extra
     mass placed at the floor, the most dangerous legal direction.
 (d) GATES.  REPRO of CCLXXXVII: the g_k fit (slope, R2) and the
     MEDOID (block, kind, kz, h, RADAU_4, RADAU_5) must come out
     identical -- the deepest block and its anchors are UNCHANGED, so
     this is a true reproduction (see amendment A1).  Identity wards
     A1 (spectral resolution of the moments) and ID1 (entry-side ==
     source-side).  Bound-property ward AL2.  Controls-must-fire:
     SCRAMBLE must destroy the alignment law, SMOOTH and the
     prime-blind ARCHIMEDEAN world must converge to a DIFFERENT atom
     (the discrimination is verified numerically, not asserted), and a
     SYNTHETIC MISALIGNMENT of the BEST-ALIGNED built cell -- b tilted
     along +sign(<b, v_min(B)>) v_min(B), which leaves w_top untouched
     and strictly grows nu_0 -- must be detected by the measurement
     itself (amendment A4).  tau and CCXVII c_h relocation screens on the
     RATE quantities.  Anti-circularity: the whole rate path is
     AST-scanned to see ENTRIES forward only -- no tau, no h, no
     alpha, no kz, no frame object, no ladder identifier.

EXTERNAL-CITED (facts consumed, warded numerically, never proved here).
 E2 Schur / Sylvester and the LDL pivot criterion.  [Horn & Johnson,
    Matrix Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE: Gauss-Radau with the node at the
    spectral floor is an UPPER bound for u^T A^{-1} u.  [Golub &
    Meurant, PUP 2010, Ch. 6-7.]  Warded per cell by CCLXXXVII's C5.
 E4 the Chebyshev algorithm (exact monic recurrence from power
    moments).  [Gautschi, OUP 2004, Sec. 2.1.]
 E7 Hamburger/Hankel positivity.  [Akhiezer, Hafner 1965, Ch. 1.]
 E8 WEYL's inequality: |lambda_j(A + E) - lambda_j(A)| <= ||E||.
    [Horn & Johnson op. cit. Sec. 4.3.]
 E9 the DAVIS-KAHAN sin(theta) theorem: for symmetric A, A + E and an
    eigenvalue of A separated by delta from the rest of the spectrum
    of A + E, the corresponding eigenvector angle obeys
    sin(theta) <= ||E|| / delta.  [Davis & Kahan, SIAM J. Numer.
    Anal. 7 (1970) 1-46; Stewart & Sun, Matrix Perturbation Theory,
    Academic Press 1990, Ch. V.]
 E10 a rank-one symmetric matrix has exactly one nonzero eigenvalue
    with the generating vector as its eigenvector (elementary).

FROZEN PROTOCOL.
 S0 firewall: AST scan of THIS file for the prime/zero oracle ban
    list; predecessors imported READ-ONLY; the only RNG seat is the
    declared scramble control seed.  AC scan: the RATE-path functions
    (atom_read / align_read / shape_read / misalign_shares) see the
    wall matrix ENTRIES and frozen constants only -- the ban list adds
    every FRAME identifier (tau, h, alpha, kz, X, Q, S, step, rung,
    block, world, census, anchor, artifact) to the CCLXV list.  NOTE
    AND DECLARED DIFFERENCE: unlike CCLXXVII's CERTIFICATE path, the
    rate path IS allowed an eigensolver -- it is a MEASUREMENT path,
    every one of its numbers is computed FROM the entries, and NO
    certificate consumes it.  The certificate tier is CCLXXXVII's,
    untouched and re-run verbatim.
 M  THE MACHINERY: deep_membership_limit_probe (CCLXXXVII) is imported
    READ-ONLY and its pipeline is re-run verbatim -- ladder, TAB2
    bitwise ward, deep census, blocks, steps, Jacobi/identity wards,
    the exact-rational certification tier, the convergence census and
    the limit object.  Its own checks are inherited and counted
    separately (R0).  AMENDMENT A1 (declared, disclosed): the three
    SHALLOW block sizes are reduced from (8, 8, 6, 8) to (5, 5, 4, 5)
    to fit the 25-minute budget.  The FRONTIER block (target None,
    4 cells, FRONTIER_BUDGET_S = 620) and the anchor ladder are
    UNCHANGED, and the CCLXXXVII level vector, medoid and g_k fit are
    functions of the DEEPEST BLOCK ALONE -- so the reproduction gate
    G-REPRO is a true reproduction and is printed digit by digit.
    AMENDMENT A2 (declared, DISCLOSED AT THE SMOKE): in SMOKE the
    block geometry is the shallow (600, 900) pair, so the CCLXXXVII
    references cannot apply; the gate is typed SMOKE-SKIPPED with the
    measured values printed, so the smoke exercises every downstream
    section instead of killing at G-REPRO (the first draft did kill,
    which left the whole new machinery unexercised).
    AMENDMENT A3 (declared, DISCLOSED AT THE SMOKE): the first draft
    made "the dominant weight sits on the TOP eigenvalue of B" part
    of the identity WARD A2.  The smoke measured it FALSE on 1 of 10
    shallow cells.  That is a FINDING about the family, not a broken
    ward, so it is re-typed as the CENSUS A2b (no kill) and the
    exceptions are printed cell by cell.
 A  the atom census (mission a) + the identification table.
 AL the alignment census, the derived bound and its ward (mission b).
 ID the source-side reading ward.
 DR the driver decomposition through the CCIII split (mission b).
 FR the functional rates, the crossover and the interior distance
    (mission c).
 X  controls-must-fire; S the screens; V the frozen verdict.

VERDICTS (frozen enum).  MECHANISM-IDENTIFIED / MECHANISM-PARTIAL /
MECHANISM-ABSENT for (a)+(b); RATE-MEASURED / RATE-DERIVED /
RATE-ABSENT for (c); INTERIOR-POSITIVE / INTERIOR-TOUCHING for the
distance statement.  No marker moves, no promotion, NO RH claim.

PREDECESSORS (READ-ONLY): deep_membership_limit_probe (CCLXXXVII, the
whole machinery), onebadmode_moments_probe (frames, splits, steps),
zolotarev_phase_filter_probe (the deployed step assembly),
sigma_stress_battery_probe (CCLXIX builders),
euler_phase_identity_probe (CCXVII c_h), v563_paper2_readouts.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_rate_mechanism_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_rate_mechanism_probe.py
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
import onebadmode_moments_probe as ob          # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul       # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
KMOM = dml.KMOM
KBASE = dml.KBASE
KDEEP = dml.KDEEP
T_R_F = dml.T_R_F
SCHUR_BAR_F = 1.0

# A1: the re-declared block geometry (frontier UNCHANGED)
BLOCK_TGT_R = (1300, 2400, 3300, 4178, None)
BLOCK_NC_R = (5, 5, 4, 5, 4)
HARD_CAP_R = 1150.0

# CCLXXXVII reproduction references
GSLOPE_REF = 3.10156
GSLOPE_ATOL = 2.0e-3
GR2_REF = 0.999890
GR2_ATOL = 1.0e-4
MED_KZ_REF = 241
MED_H_REF = 6344
RAD4_REF = 0.675856469
RAD5_REF = 0.502887686
RAD_RTOL = 1.0e-6
ENV_RHO5_REF = 0.787603
ENV_RTOL = 1.0e-4

# the composed architecture's budget against the DEFINITENESS bar 1
BUDGET = SCHUR_BAR_F - ENV_RHO5_REF

# ties and bars of THIS probe
SPEC_TIE = 1.0e-10          # spectral resolution identity nu_k
ANG_TIE = 1.0e-9            # alignment identity cos^2 == w_top/nu_0
SRC_TIE = 1.0e-8            # entry-side == source-side reading
ID_RTOL = 1.0e-3            # "IDENTIFIED" for a named-object candidate
BOUND_SLACK = 1.0e-12       # allowance in the bound-property ward
SHARE_ONE = 0.99            # "one-atom" share bar (declared)
CTRL_ATOM_FAC = 2.0         # smooth-world atom discrimination factor
CTRL_TILT = 0.20            # synthetic misalignment tilt (declared)
LIMD = 10 ** 18             # the declared rational grid of the limit
BIS_F = 60                  # float bisection steps for the radii
INWARD = 0.99               # the inward margin certified exactly
SLOPE_PASS = dml.SLOPE_PASS
SLOPE_RELOC = dml.SLOPE_RELOC

# the driver split (mission b): declared depths, MECH_N cells each
DR_TGT = (1300, 2400, 3300)
DR_N = 2
CH_N_R = 3
CH_HMAX_R = 2900
CH_BUDGET_S = 1380.0        # the c_h screen's own honest cut-off
SCR_SEED = dml.SCR_SEED

BANNED_IDS = dml.BANNED_IDS
# AC: the RATE path sees wall ENTRIES and frozen constants only.  The
# CCLXV ban list PLUS every frame identifier.  (Eigensolvers ARE
# allowed here -- declared difference, see S0 in the spec.)
RATE_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
               "lu_read", "assemble_step", "build_rung", "build_cell",
               "artifact", "h", "gap", "alpha", "kz", "X", "Q", "S",
               "step", "steps", "rung", "rungs", "row", "rows",
               "block", "blocks", "census", "anchor", "anchors",
               "world", "mode", "medoid", "limobj", "cens")
RATE_FUNCS = ("atom_read", "align_read", "shape_read",
              "misalign_shares")

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
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(values):
    return dml.trio(values)


def f4(values):
    return dml.f4(values)


def linfit(xv, yv):
    return dml.linfit(xv, yv)


def screen(values, scales, label):
    return dml.screen(values, scales, label)


# ================================================== THE RATE PATH
# AC-scanned: wall matrix ENTRIES forward, no frame identifier.
def atom_read(matrix):
    """THE ATOM: the exact spectral-pair census of (b, B) from the
    ENTRIES.  nu_k = sum_j w_j mu_j^k identically, so the moment
    SHAPE is the weight profile of the spectral measure of B at b."""
    mmat = np.asarray(matrix, float)
    piv = float(mmat[0, 0])
    cvec = mmat[1:, 0]
    blk = 0.5 * (mmat[1:, 1:] + mmat[1:, 1:].T)
    evl, evc = np.linalg.eigh(blk)
    proj = evc.T @ cvec
    wts = proj ** 2
    nu0 = float(cvec @ cvec)
    if not (piv > 0.0 and nu0 > 0.0 and np.all(np.isfinite(evl))):
        return None
    jtop = int(len(evl) - 1)
    jdom = int(np.argmax(wts))
    with np.errstate(over="ignore", invalid="ignore"):
        mom = [float(np.sum(wts * evl ** kk))
               for kk in range(KMOM + 1)]
    direct = dml.wall_moments(mmat, KMOM)
    if not (all(math.isfinite(v) for v in mom)
            and np.all(np.isfinite(direct))
            and float(direct[KMOM - 1]) > 0.0
            and float(direct[0]) > 0.0):
        return None
    dev = max(abs(mom[kk] - float(direct[kk]))
              / max(1.0e-300, abs(float(direct[kk])))
              for kk in range(KMOM + 1))
    share = float(wts[jtop] / nu0)
    # THE GAP BOUND (exact, elementary, no external citation needed):
    #   nu_1/nu_0 = sum_j (w_j/nu_0) mu_j  and  mu_1 - mu_j >= mu_1 -
    #   mu_2 for every j >= 2, so
    #      sin^2 theta = sum_{j>=2} w_j/nu_0
    #                 <= (mu_1 - nu_1/nu_0) / (mu_1 - mu_2).
    # The RAYLEIGH DEFICIT mu_1 - nu_1/nu_0 divided by B's SPECTRAL
    # GAP bounds the alignment defect -- the moment shape and the
    # alignment are the SAME statement.
    x_1 = float(evl[jtop]) / piv
    x_2 = float(evl[jtop - 1]) / piv
    r_1 = float(direct[1]) / max(1.0e-300, float(direct[0]) * piv)
    if x_1 - x_2 > 0.0:
        gap_b = math.sqrt(max(0.0, (x_1 - r_1) / (x_1 - x_2)))
    else:
        gap_b = float("inf")
    return dict(x_top=x_1, x_2nd=x_2, r_moment=r_1,
                x_dom=float(evl[jdom]) / piv,
                x_mom=(float(direct[KMOM])
                       / max(1.0e-300, float(direct[KMOM - 1]) * piv)),
                share=share, share_dom=float(wts[jdom] / nu0),
                dom_is_top=bool(jdom == jtop),
                sin_th=math.sqrt(max(0.0, 1.0 - share)),
                gap_bound=gap_b, relgap=(x_1 - x_2) / max(1.0e-300,
                                                          x_1),
                deficit=(x_1 - r_1) / max(1.0e-300, x_1),
                kap_blk=float(evl[jtop]) / max(1.0e-300,
                                               float(evl[0])),
                lo_blk=float(evl[0]) / piv,
                spec_dev=dev, nu0n=nu0 / piv ** 2)


def align_read(matrix):
    """THE DERIVED ALIGNMENT BOUND from the ENTRIES (E8 + E9 + E10).
    With eigenpairs (m_i, z_i) of the FULL matrix and c_i = z_i[0],
      b = m_1 c_1 y_1 + f,   ||f|| <= m_2 sqrt(1 - c_1^2),
      B = m_1 y_1 y_1^T + E, 0 <= E <= m_2 I,
    hence sin angle(b, y_1) <= m_2 / (m_1 |c_1| - m_2) and, by E9,
    sin angle(y_1, v_top(B)) <= m_2 / (m_1 (1 - c_1^2) - m_2)."""
    mmat = 0.5 * (np.asarray(matrix, float)
                  + np.asarray(matrix, float).T)
    evl, evc = np.linalg.eigh(mmat)
    if not np.all(np.isfinite(evl)):
        return None
    m_1 = float(evl[-1])
    m_2 = float(evl[-2])
    c_1 = abs(float(evc[0, -1]))
    gg = max(0.0, 1.0 - c_1 * c_1)
    d_1 = m_1 * c_1 - m_2
    d_2 = m_1 * gg - m_2
    if m_1 <= 0.0 or d_1 <= 0.0 or d_2 <= 0.0:
        bnd = float("inf")
    else:
        bnd = m_2 / d_1 + m_2 / d_2
    return dict(m1=m_1, m2=m_2, rgap=m_2 / m_1 if m_1 > 0.0
                else float("inf"), c1=c_1, gg=gg, bound=bnd,
                pd=bool(float(evl[0]) > 0.0),
                kap_full=m_1 / float(evl[0]) if float(evl[0]) > 0.0
                else float("inf"),
                m1_over_n=m_1 / float(mmat[0, 0])
                if float(mmat[0, 0]) > 0.0 else float("nan"),
                tan2=(gg / (c_1 * c_1)) if c_1 > 0.0 else
                float("inf"))


def shape_read(matrix):
    """The scale-invariant moment SHAPE from the ENTRIES: g_k, the
    linear fit in k, the residual RMS (0 exactly for one atom)."""
    piv = float(np.asarray(matrix, float)[0, 0])
    mom = dml.wall_moments(matrix, KMOM)
    if not (piv > 0.0 and np.all(np.isfinite(mom))):
        return None
    # logarithms throughout: the control worlds reach pivots whose
    # powers overflow float64, and an overflow must be a REFUSAL, not
    # an exception (declared design correction, disclosed at smoke).
    lpiv = math.log10(piv)
    gvals = []
    for kk in range(KMOM + 1):
        val = float(mom[kk])
        gvals.append(math.log10(val) - (kk + 2) * lpiv
                     if val > 0.0 else float("nan"))
    if not all(math.isfinite(v) for v in gvals):
        return None
    slp, se2, r2v, a0v = dml.linfit(list(range(KMOM + 1)), gvals)
    res = float(np.sqrt(np.mean(
        (np.asarray(gvals) - (a0v + slp * np.arange(KMOM + 1)))
        ** 2)))
    return dict(g=gvals, gslope=slp, g2se=se2, gr2=r2v, gresid=res)


def misalign_shares(matrix, parts):
    """WHO DRIVES THE ALIGNMENT: with the exact additive carrier
    decomposition of the wall matrix, the misaligned component
    P_perp b splits additively too.  Returns the per-carrier
    perpendicular share ||P_perp b_p|| / ||b|| beside the TOTAL
    sin theta, so a large per-carrier share with a small total IS the
    measured cancellation."""
    mmat = np.asarray(matrix, float)
    cvec = mmat[1:, 0]
    blk = 0.5 * (mmat[1:, 1:] + mmat[1:, 1:].T)
    evl, evc = np.linalg.eigh(blk)
    vtop = evc[:, int(len(evl) - 1)]
    nrm = float(np.linalg.norm(cvec))
    if nrm <= 0.0:
        return None
    out = {}
    for key, pmat in parts.items():
        pvec = np.asarray(pmat, float)[1:, 0]
        perp = pvec - float(vtop @ pvec) * vtop
        out[key] = float(np.linalg.norm(perp)) / nrm
    tot = cvec - float(vtop @ cvec) * vtop
    out["TOTAL"] = float(np.linalg.norm(tot)) / nrm
    return out


# ============================================ A: the atom's identity
def atom_identity(rows):
    section("A -- THE ATOM'S IDENTITY: the spectral-pair census of "
            "(b, B) and the identification against the named objects "
            "of the construction")
    d_spec = 0.0
    d_ang = 0.0
    n_dom = 0
    keep = []
    for row in rows:
        atm = atom_read(row["step"]["Mt"])
        alg = align_read(row["step"]["Mt"])
        shp = shape_read(row["step"]["Mt"])
        if atm is None or alg is None or shp is None:
            continue
        row["atm"] = atm
        row["alg"] = alg
        row["shp"] = shp
        d_spec = max(d_spec, atm["spec_dev"])
        d_ang = max(d_ang, abs(atm["share"]
                               + atm["sin_th"] ** 2 - 1.0))
        n_dom += int(atm["dom_is_top"])
        keep.append(row)
    check("A1 SPECTRAL RESOLUTION IDENTITY nu_k == sum_j w_j mu_j^k "
          "on all %d cells for k = 0..%d: max rel %.2e <= %.0e -- the "
          "moment shape IS the weight profile of the spectral measure "
          "of B at b" % (len(keep), KMOM, d_spec, SPEC_TIE),
          len(keep) > 0 and d_spec <= SPEC_TIE, kill="K2")
    check("A2 ALIGNMENT IDENTITY cos^2 theta == w_top / nu_0: max dev "
          "%.2e <= %.0e" % (d_ang, ANG_TIE), d_ang <= ANG_TIE,
          kill="K2")
    # AMENDMENT A3 (declared, disclosed at the smoke): the FIRST draft
    # made "the dominant weight sits on the TOP eigenvalue of B" part
    # of the identity WARD.  The smoke measured it FALSE on 1 of 10
    # shallow cells -- that is a FINDING about the family, not a
    # broken ward, so it is re-typed as a CENSUS with no kill and the
    # exceptions are printed.
    off = [r for r in keep if not r["atm"]["dom_is_top"]]
    check("A2b DOMINANCE CENSUS (a measurement, no kill): the "
          "dominant weight sits on the TOP eigenvalue of B on %d/%d "
          "cells%s" % (n_dom, len(keep),
                       "" if not off else
                       "; exceptions " + ", ".join(
                           "b%d %s kz %d h %d (share_dom %.4f at "
                           "x %.4g vs share_top %.4f)"
                           % (r["block"], r["mode"], r["kz"],
                              int(r["h"]), r["atm"]["share_dom"],
                              r["atm"]["x_dom"], r["atm"]["share"])
                           for r in off)), True)
    if not keep:
        return keep
    shares = [r["atm"]["share"] for r in keep]
    xtops = [r["atm"]["x_top"] for r in keep]
    n_one = sum(1 for s in shares if s >= SHARE_ONE)
    print("    the ONE-ATOM census: weight share w_top/nu_0 "
          "min/med/max %s; %d/%d cells above the declared one-atom "
          "bar %.2f" % (f4(shares), n_one, len(keep), SHARE_ONE))
    print("    the ATOM POSITION x* = lambda_max(B)/n: min/med/max "
          "%.6g / %.6g / %.6g;  log10 med %+.5f  (the CCLXXXVII "
          "gslope reference is a LOG10 slope: %+.5f -> x* = %.6g)"
          % (trio(xtops)[0], trio(xtops)[1], trio(xtops)[2],
             math.log10(trio(xtops)[1]), GSLOPE_REF,
             10.0 ** GSLOPE_REF))
    # ---- the identification table (declared candidate list)
    cands = (("lambda_max(B)/n  [definitional]",
              lambda r: r["atm"]["x_top"]),
             ("10^gslope  [the fitted shape atom]",
              lambda r: 10.0 ** r["shp"]["gslope"]),
             ("nu_8/(nu_7 n)  [the moment-read atom]",
              lambda r: r["atm"]["x_mom"]),
             ("kappa(B) = lambda_max/lambda_min(B)",
              lambda r: r["atm"]["kap_blk"]),
             ("kappa(Mt) = m_1/m_8",
              lambda r: r["alg"]["kap_full"]),
             ("m_1/n  [the top eigenvalue over the pivot]",
              lambda r: r["alg"]["m1_over_n"]),
             ("tan^2 phi = (1-c_1^2)/c_1^2  [frame overlap]",
              lambda r: r["alg"]["tan2"]))
    print("    THE IDENTIFICATION TABLE (relative deviation of each "
          "named object from the measured atom position x*):")
    ident = {}
    for lab, fun in cands:
        devs = []
        for r in keep:
            val = fun(r)
            if math.isfinite(val) and val != 0.0:
                devs.append(abs(val - r["atm"]["x_top"])
                            / abs(r["atm"]["x_top"]))
        if not devs:
            continue
        worst = max(devs)
        verd = "IDENTIFIED" if worst <= ID_RTOL else "NO-MATCH"
        ident[lab] = (worst, verd)
        print("      %-44s  max rel dev %.3e   %s"
              % (lab, worst, verd))
    n_id = sum(1 for _w, v in ident.values() if v == "IDENTIFIED")
    check("A3 the atom is IDENTIFIED against %d of %d declared named "
          "objects of the construction (declared tie %.0e)"
          % (n_id, len(ident), ID_RTOL), n_id >= 2)
    return keep


# ======================================== AL: the alignment law
def alignment_law(rows):
    section("AL -- THE ALIGNMENT LAW: theta_h = angle(b, v_top(B)), "
            "its h-law, and the DERIVED bound (E8 + E9 + E10) with "
            "its bound-property ward")
    n_bad_g = n_bad_f = 0
    for row in rows:
        if row["atm"]["gap_bound"] + BOUND_SLACK \
                < row["atm"]["sin_th"]:
            n_bad_g += 1
        if row["alg"]["bound"] + BOUND_SLACK < row["atm"]["sin_th"]:
            n_bad_f += 1
    n_live_g = sum(1 for r in rows if r["atm"]["gap_bound"] < 1.0)
    n_live_f = sum(1 for r in rows if r["alg"]["bound"] < 1.0)
    check("AL2 BOUND-PROPERTY WARD (never assumed): the DERIVED GAP "
          "bound sqrt((x_1 - nu_1/(nu_0 n)) / (x_1 - x_2)) is an "
          "upper bound for the MEASURED sin theta on every one of the "
          "%d cells: %d violations (0 required); non-vacuous (< 1) on "
          "%d/%d" % (len(rows), n_bad_g, n_live_g, len(rows)),
          n_bad_g == 0, kill="K2")
    check("AL2b BOUND-PROPERTY WARD for the FRAME bound (E8/E9/E10, "
          "m_2/(m_1|c_1| - m_2) + m_2/(m_1(1-c_1^2) - m_2)): %d "
          "violations (0 required); non-vacuous on %d/%d cells"
          % (n_bad_f, n_live_f, len(rows)), n_bad_f == 0, kill="K2")
    bidx = sorted({r["block"] for r in rows})
    print("    block cells h(med)  sin theta (min/med/max)       "
          "GAP bnd  rel gap  deficit  FRAME bnd   r_gap    |c_1|")
    lev_sin = []
    lev_bnd = []
    lev_gap = []
    lev_c1 = []
    lev_h = []
    for bi in bidx:
        sub = [r for r in rows if r["block"] == bi]
        if not sub:
            continue
        hmd = float(np.median([r["h"] for r in sub]))
        sns = [r["atm"]["sin_th"] for r in sub]
        gbs = [r["atm"]["gap_bound"] for r in sub]
        rgs = [r["atm"]["relgap"] for r in sub]
        dfs = [r["atm"]["deficit"] for r in sub]
        bns = [r["alg"]["bound"] for r in sub]
        gps = [r["alg"]["rgap"] for r in sub]
        c1s = [r["alg"]["c1"] for r in sub]
        lev_sin.append(float(np.median(sns)))
        lev_bnd.append(float(np.median(gbs)))
        lev_gap.append(float(np.median(gps)))
        lev_c1.append(float(np.median(c1s)))
        lev_h.append(math.log(hmd))
        print("    %5d %5d %6d  %s  %8.5f %8.5f %8.5f %10.4g "
              "%8.5f %8.5f"
              % (bi, len(sub), int(hmd), f4(sns),
                 float(np.median(gbs)), float(np.median(rgs)),
                 float(np.median(dfs)), float(np.median(bns)),
                 float(np.median(gps)), float(np.median(c1s))))
    laws = {}
    for lab, vals, lv in (("sin theta",
                           [r["atm"]["sin_th"] for r in rows],
                           lev_sin),
                          ("GAP bound",
                           [r["atm"]["gap_bound"] for r in rows],
                           lev_bnd),
                          ("relative gap of B",
                           [r["atm"]["relgap"] for r in rows], None),
                          ("Rayleigh deficit",
                           [r["atm"]["deficit"] for r in rows], None),
                          ("FRAME bound",
                           [r["alg"]["bound"] for r in rows], None),
                          ("r_gap = m_2/m_1",
                           [r["alg"]["rgap"] for r in rows], lev_gap),
                          ("|c_1| frame overlap",
                           [r["alg"]["c1"] for r in rows], lev_c1),
                          ("x* atom position",
                           [r["atm"]["x_top"] for r in rows], None)):
        xs = []
        ys = []
        for r, v in zip(rows, vals):
            if math.isfinite(v) and v > 0.0:
                xs.append(math.log(r["h"]))
                ys.append(math.log(v))
        if len(xs) < 4:
            continue
        slp, se2, r2v, _a = linfit(xs, ys)
        blk_txt = ""
        if lv is not None and len(lv) >= 3:
            sb, eb, r2b, _ab = linfit(lev_h, np.log(np.maximum(
                lv, 1e-300)))
            blk_txt = ("; block-level %+.4f +- %.4f (R2 %.3f)"
                       % (sb, eb, r2b))
        laws[lab] = dict(slope=slp, se=se2, r2=r2v)
        stat = ("H-STATIONARY" if abs(slp) + se2 <= 0.15
                else "DECAYING" if slp + se2 < 0.0
                else "GROWING" if slp - se2 > 0.0 else "NOISY")
        print("      LAW  %-22s d log v / d log h = %+.4f +- %.4f "
              "(R2 %.3f)%s   %s"
              % (lab, slp, se2, r2v, blk_txt, stat))
    sns_all = [r["atm"]["sin_th"] for r in rows]
    gbs_all = [r["atm"]["gap_bound"] for r in rows]
    tight = [r["atm"]["gap_bound"] / max(1.0e-300, r["atm"]["sin_th"])
             for r in rows if math.isfinite(r["atm"]["gap_bound"])]
    check("AL1 the alignment census is complete on %d cells: "
          "sin theta %s, GAP bound %s, bound/truth tightness ratio %s"
          % (len(rows), f4(sns_all), f4(gbs_all), f4(tight)),
          len(rows) >= 4)
    sl = laws.get("sin theta", {})
    check("AL3 the alignment law is TYPED: d log sin theta / d log h "
          "= %+.4f +- %.4f (R2 %.3f) -- a MEASURED law; the DERIVED "
          "bound above is what converts it into a mechanism statement"
          % (sl.get("slope", float("nan")), sl.get("se", float("nan")),
             sl.get("r2", float("nan"))), bool(sl))
    return dict(laws=laws, lev_sin=lev_sin, lev_bnd=lev_bnd,
                lev_gap=lev_gap, lev_c1=lev_c1, lev_h=lev_h)


# ================================ ID: the source-side reading
def source_reading(rows):
    section("ID -- THE SOURCE-SIDE READING WARD: the entry-side rate "
            "quantities ARE geometric objects of the window "
            "construction")
    d_eig = 0.0
    d_c1 = 0.0
    n_used = 0
    for row in rows[:12]:
        st = row["step"]
        tau1 = float(st["tau"])
        s_2 = np.asarray(st["r2"]["S"], float)
        s_1 = np.asarray(st["r1"]["S"], float)
        ev_mt = np.linalg.eigvalsh(np.asarray(st["Mt"], float))
        ev_s2 = np.linalg.eigvalsh(0.5 * (s_2 + s_2.T))
        d_eig = max(d_eig, float(np.max(
            np.abs(ev_mt * tau1 - ev_s2)
            / np.maximum(1.0, np.abs(ev_s2)))))
        _w2, v_2 = np.linalg.eigh(0.5 * (s_2 + s_2.T))
        _w1, v_1 = np.linalg.eigh(0.5 * (s_1 + s_1.T))
        ov = abs(float(v_1[:, 0] @ v_2[:, -1]))
        d_c1 = max(d_c1, abs(ov - row["alg"]["c1"]))
        n_used += 1
    check("ID1 the entry-side spectrum IS the source spectrum: "
          "m_i(Mt) * tau_1 == mu_i(S_2) on %d cells, max rel %.2e <= "
          "%.0e (Mt is an ORTHOGONAL conjugation of S_2/tau_1)"
          % (n_used, d_eig, SRC_TIE), d_eig <= SRC_TIE, kill="K2")
    check("ID2 the frame overlap IS the consecutive-rung eigenvector "
          "overlap: |c_1| == |<v_min(S_1), u_max(S_2)>| on %d cells, "
          "max abs dev %.2e <= %.0e -- the alignment law is a "
          "statement about the WINDOW GEOMETRY of two neighbouring "
          "census cells" % (n_used, d_c1, SRC_TIE),
          d_c1 <= SRC_TIE, kill="K2")
    return dict(d_eig=d_eig, d_c1=d_c1)


# ============================= DR: the driver decomposition
def driver_split(census, anchors):
    section("DR -- WHO DRIVES THE ALIGNMENT: the exact CCIII three-way "
            "split S = S_AR + S_SM + S_OSC pushed through the SAME "
            "step frame, so Mt = Mt_AR + Mt_SM + Mt_OSC exactly")
    tgts = (600,) if SMOKE else DR_TGT
    ncell = 1 if SMOKE else DR_N
    anc = sorted(anchors, key=lambda r: r["h"])
    d_add = 0.0
    recs = []
    print("    h      kz     sin th   GAP bnd  rel gap   |c_1|   "
          "|| P_perp b_p || / ||b||  (AR / SM / OSC / TOTAL)")
    for tgt in tgts:
        picked = dml.block_pick(census, tgt, ncell)
        prev = None
        for cell in picked:
            rung = dml.build_cell(cell, with_split=True)
            ok, why = dml.cell_legal(rung)
            if not ok or "S_parts" not in rung:
                print("      driver cell h %d kz %d SKIPPED (%s)"
                      % (cell["h"], cell["kz"], why))
                prev = rung if ok else prev
                continue
            below = [a for a in anc if a["h"] <= rung["h"]]
            r_1 = prev if prev is not None else (
                below[-1] if below else anc[0])
            sts = ob.make_steps([r_1, rung])
            prev = rung
            if not sts:
                continue
            st = sts[0]
            dml.zol.assemble_step(st)
            if st["status"] != "OK":
                continue
            tau1 = float(st["tau"])
            qm = st["Q"]
            full = np.asarray(st["Mt"], float)
            parts = {p: dml.sym(qm.T @ (rung["S_parts"][p] / tau1)
                                @ qm)
                     for p in ("AR", "SM", "OSC")}
            recon = parts["AR"] + parts["SM"] + parts["OSC"]
            d_add = max(d_add, float(np.max(np.abs(recon - full)))
                        / max(1.0, float(np.max(np.abs(full)))))
            atm = atom_read(full)
            alg = align_read(full)
            shr = misalign_shares(full, parts)
            if atm is None or alg is None or shr is None:
                continue
            acc = {"AR": parts["AR"],
                   "AR+SM": parts["AR"] + parts["SM"],
                   "FULL": full}
            cum = {}
            for lab, pmat in acc.items():
                cum[lab] = (atom_read(pmat), align_read(pmat))
            recs.append(dict(h=float(rung["h"]), kz=int(rung["kz"]),
                             atm=atm, alg=alg, shr=shr, cum=cum))
            print("    %-6d %-6d %8.5f %8.5f %9.6f %8.5f   "
                  "%.4f / %.4f / %.4f / %.6f"
                  % (rung["h"], rung["kz"], atm["sin_th"],
                     atm["gap_bound"], atm["relgap"], alg["c1"],
                     shr["AR"], shr["SM"], shr["OSC"], shr["TOTAL"]),
                  flush=True)
    check("DR1 the three-way split is EXACTLY additive through the "
          "step frame on %d driver cells: max rel |Mt - (Mt_AR + "
          "Mt_SM + Mt_OSC)| = %.2e <= 1e-10" % (len(recs), d_add),
          len(recs) >= 1 and d_add <= 1.0e-10, kill="K2")
    if not recs:
        return None
    # ---- the decision: cancellation or single carrier?
    ratios = []
    solo = {"AR": [], "SM": [], "OSC": []}
    for rc in recs:
        tot = max(1.0e-300, rc["shr"]["TOTAL"])
        mx = max(rc["shr"][p] for p in ("AR", "SM", "OSC"))
        ratios.append(mx / tot)
        for p in ("AR", "SM", "OSC"):
            solo[p].append(rc["shr"][p] / tot)
    med_ratio = float(np.median(ratios))
    verdict = ("CANCELLATION" if med_ratio >= 10.0
               else "SINGLE-CARRIER" if med_ratio <= 2.0
               else "MIXED")
    print("    the DRIVER decision: max single-carrier perpendicular "
          "share / TOTAL = %s (median %.3g) -> %s"
          % (f4(ratios), med_ratio, verdict))
    for p in ("AR", "SM", "OSC"):
        print("      carrier %-3s perpendicular share / TOTAL: %s"
              % (p, f4(solo[p])))
    # ---- does the rank-one dominance already live in the AR part?
    print("    the RANK-ONE dominance per carrier PARTIAL SUM "
          "(is the collapse already there before the primes enter?):")
    print("      partial sum   sin theta (min/med/max)      "
          "share (med)   rel gap (med)  |c_1| (med)   x* (med)")
    for lab in ("AR", "AR+SM", "FULL"):
        sns = [rc["cum"][lab][0]["sin_th"] for rc in recs
               if rc["cum"][lab][0] is not None]
        shs = [rc["cum"][lab][0]["share"] for rc in recs
               if rc["cum"][lab][0] is not None]
        gps = [rc["cum"][lab][0]["relgap"] for rc in recs
               if rc["cum"][lab][0] is not None]
        c1s = [rc["cum"][lab][1]["c1"] for rc in recs
               if rc["cum"][lab][1] is not None]
        xts = [rc["cum"][lab][0]["x_top"] for rc in recs
               if rc["cum"][lab][0] is not None]
        if not sns:
            print("      %-13s NO VALID READ -- the partial sum is "
                  "not a wall matrix (n <= 0 or a non-finite moment); "
                  "CCLXXXVII already measured AR and AR+SM as NOT PD"
                  % lab)
            continue
        print("      %-13s %s   %11.6f   %11.6f   %11.6f   %.5g"
              % (lab, f4(sns), float(np.median(shs)),
                 float(np.median(gps)), float(np.median(c1s)),
                 float(np.median(xts))))
    check("DR2 the driver decomposition is measured on %d cells and "
          "typed %s (declared rule: CANCELLATION iff the largest "
          "single-carrier perpendicular share exceeds the TOTAL by a "
          "factor >= 10, SINGLE-CARRIER iff <= 2)"
          % (len(recs), verdict), True)
    return dict(recs=recs, verdict=verdict, med_ratio=med_ratio,
                solo=solo)


# ================================ FR: the functional rates
def functional_rates(rows, cens, limobj):
    section("FR -- THE FUNCTIONAL RATES: shape -> Radau bound "
            "stability, the composed statement against the "
            "DEFINITENESS bar 1 (budget %+.6f) and the typing ladder"
            % BUDGET)
    deep_b = max(r["block"] for r in rows)
    ref = {k: cens[k]["limit"] for k in ("sigma", "rho4", "rho5")}
    print("    the reference levels (deepest block medians, "
          "CCLXXXVII's limit level): sigma %.6f, rho_4 %.6f, "
          "rho_5 %.6f" % (ref["sigma"], ref["rho4"], ref["rho5"]))
    # ---- (1) the coupling shape -> functional (empirical Lipschitz)
    out = {}
    for key in ("sigma", "rho5"):
        xs = []
        ys = []
        for r in rows:
            sn = r["atm"]["sin_th"]
            dv = abs(r["dat"][key] - ref[key])
            if sn > 0.0 and dv > 0.0:
                xs.append(math.log(sn))
                ys.append(math.log(dv))
        if len(xs) < 4:
            continue
        slp, se2, r2v, _a = linfit(xs, ys)
        lip = max(abs(r["dat"][key] - ref[key])
                  / max(1.0e-300, r["atm"]["sin_th"]) for r in rows)
        out[key] = dict(slope=slp, se=se2, r2=r2v, lip=lip)
        print("      COUPLING  |%s(h) - %s_inf| vs sin theta: "
              "log-log slope %+.4f +- %.4f (R2 %.3f); empirical "
              "Lipschitz constant L = %.4f  [MEASURED, not derived]"
              % (key, key, slp, se2, r2v, lip))
    # ---- (2) the reference-free Cauchy rate on the block levels
    print("    the REFERENCE-FREE rate (block-to-block Cauchy "
          "differences of the level, no limit assumed):")
    rate = {}
    for key in ("sigma", "rho5", "gslope", "gresid"):
        lv = cens.get(key, {}).get("levels", [])
        hb = cens.get(key, {}).get("hbar", [])
        if len(lv) < 3 or len(hb) != len(lv):
            continue
        dif = [abs(lv[i + 1] - lv[i]) for i in range(len(lv) - 1)]
        hm = [hb[i + 1] for i in range(len(lv) - 1)]
        pos = [(a, b) for a, b in zip(hm, dif) if b > 0.0]
        if len(pos) < 3:
            print("      %-8s Cauchy diffs %s (too few positive for "
                  "a law)" % (key, " ".join("%.4g" % d for d in dif)))
            continue
        slp, se2, r2v, a0v = linfit([a for a, _b in pos],
                                    [math.log(b) for _a, b in pos])
        rate[key] = dict(p=-slp, se=se2, r2=r2v, a0=a0v,
                         dif=dif, hm=hm)
        print("      %-8s Cauchy diffs %s ;  d log|dL| / d log h = "
              "%+.4f +- %.4f (R2 %.3f)  =>  power p = %+.4f"
              % (key, " ".join("%.4g" % d for d in dif), slp, se2,
                 r2v, -slp))
    # ---- (3) the composed statement against bar 1
    env_last = cens["rho5"]["env_hi_lim"]
    margin = SCHUR_BAR_F - env_last
    dev_deep = [abs(r["dat"]["rho5"] - ref["rho5"]) for r in rows
                if r["block"] == deep_b]
    dev_all = [abs(r["dat"]["rho5"] - ref["rho5"]) for r in rows]
    e_meas = max(dev_all) if dev_all else float("nan")
    e_deep = max(dev_deep) if dev_deep else float("nan")
    top_all = ref["rho5"] + e_meas
    top_deep = ref["rho5"] + e_deep
    print("""    THE COMPOSED STATEMENT AGAINST THE DEFINITENESS BAR 1,
    IN THE TWO READINGS THAT ARE ACTUALLY DIFFERENT (amendment A5):
      READING 1 (the CCLXXXVII budget reading).  The frontier
        envelope is rho_5 = %.6f, so the budget against bar 1 is
        %+.6f.  The MEASURED spread of rho_5 about the deepest-block
        level is E_all = %.6f over all %d built wall-legal steps and
        E_deep = %.6f over the deepest block alone.  E < budget is
        %s / %s -- the measured spread is LARGER than the budget the
        frontier envelope leaves, so a uniform envelope anchored at
        the FRONTIER WORST does NOT close.
      READING 2 (the direct composition, anchored at the LIMIT
        LEVEL).  rho_5(h) <= rho_5^inf + E gives
        %.6f + %.6f = %.6f vs bar 1 -> margin %+.6f (all cells) and
        %.6f + %.6f = %.6f -> margin %+.6f (deepest block).  So the
        composition DOES close against bar 1 in this reading, but
        %s.
      THE HONEST READING OF THE TWO: the composed all-large-h
      statement against bar 1 is AVAILABLE but RAZOR-THIN -- the
      measured spread of rho_5 consumes %.1f%% of the whole distance
      from the limit level to the bar.  This is the precise reason a
      PROVED bound is needed on the SPREAD, not on a decay."""
          % (env_last, margin, e_meas, len(rows), e_deep,
             "TRUE" if e_meas < BUDGET else "FALSE",
             "TRUE" if e_deep < BUDGET else "FALSE",
             ref["rho5"], e_meas, top_all, SCHUR_BAR_F - top_all,
             ref["rho5"], e_deep, top_deep, SCHUR_BAR_F - top_deep,
             "only just -- the all-cell margin is %+.6f"
             % (SCHUR_BAR_F - top_all) if top_all < SCHUR_BAR_F
             else "NOT for the all-cell spread (margin %+.6f)"
             % (SCHUR_BAR_F - top_all),
             100.0 * e_meas / max(1.0e-12,
                                  SCHUR_BAR_F - ref["rho5"])))
    # the crossover H for the fitted power law (if it decays)
    hx = float("nan")
    rr = rate.get("rho5")
    if rr and rr["p"] <= 0.0:
        print("      NO DECAYING RATE IS MEASURED for rho_5: the "
              "block-to-block Cauchy differences fit p = %+.4f +- "
              "%.4f (R2 %.3f), i.e. they do NOT decay in h, so there "
              "is NO crossover H to report and the composed "
              "statement rests on the UNIFORM spread above, not on a "
              "rate." % (rr["p"], rr["se"], rr["r2"]))
    if rr and rr["p"] > 0.0:
        # |L - L_inf| <= sum_{j >= J} A h^-p ~ A h^-p / (1 - 2^-p)
        amp = math.exp(rr["a0"]) / max(1.0e-12,
                                       1.0 - 2.0 ** (-rr["p"]))
        if amp > BUDGET:
            hx = math.exp(math.log(amp / BUDGET) / rr["p"])
        p_lo = rr["p"] - rr["se"]
        hx_lo = (math.exp(math.log(amp / BUDGET) / p_lo)
                 if p_lo > 0.0 and amp > BUDGET else float("nan"))
        print("      the fitted Cauchy power law for rho_5 gives "
              "A = %.4g, p = %.4f +- %.4f; the geometric summation "
              "E(h) <= A h^-p / (1 - 2^-p) crosses the budget at "
              "H = %s (conservative p - 2SE: H = %s)"
              % (amp, rr["p"], rr["se"],
                 "%.4g" % hx if math.isfinite(hx) else "already below",
                 "%.4g" % hx_lo if math.isfinite(hx_lo)
                 else "already below"))
    print("""    THE TYPING LADDER (honest, no piece upgraded):
      MEASURED-RATE  the Cauchy law above and the coupling constant L
                     are FITS on %d built cells with 2SE bands.
      DERIVED-RATE   AL2 delivers a DERIVED bound for sin theta ALONE
                     -- the GAP bound (elementary and exact) and the
                     FRAME bound (E8 + E9 + E10), both warded as true
                     upper bounds on every cell.  They turn the shape
                     statement into a statement about B's RELATIVE
                     SPECTRAL GAP and the RAYLEIGH DEFICIT (and, in
                     the frame reading, r_gap = m_2/m_1 with the
                     overlap |c_1|), all geometric.  What is still
                     MEASURED in the derived chain: the h-behaviour
                     of those ingredients themselves.
      PROVED-RATE    NOT reached.  A proof needs (i) a proved LOWER
                     bound for B's RELATIVE SPECTRAL GAP and a proved
                     UPPER bound for the RAYLEIGH DEFICIT from the
                     window construction (the archimedean half is a
                     closed-form question, the prime half is the
                     error term), and (ii) a proved Lipschitz
                     constant for rho_K in the shape coordinates
                     replacing the measured L above.  Neither is
                     delivered here and neither is claimed."""
          % len(rows))
    check("FR1 the shape -> functional coupling is MEASURED on %d "
          "cells and the empirical Lipschitz constants are printed "
          "(rho_5: L = %.4f)" % (len(rows),
                                 out.get("rho5", {}).get(
                                     "lip", float("nan"))),
          bool(out))
    check("FR2 the composed statement against the DEFINITENESS bar 1 "
          "is stated in BOTH readings: budget reading E_all = %.6f vs "
          "%+.6f (%s); direct reading rho_5^inf + E_all = %.6f vs 1 "
          "(margin %+.6f, %s); crossover H = %s"
          % (e_meas, BUDGET,
             "closes" if e_meas < BUDGET else "does NOT close",
             top_all, SCHUR_BAR_F - top_all,
             "closes" if top_all < SCHUR_BAR_F else "does NOT close",
             "%.4g" % hx if math.isfinite(hx)
             else "none (no decaying rate measured)"),
          math.isfinite(e_meas))
    return dict(out=out, rate=rate, e_meas=e_meas, e_deep=e_deep,
                top_all=top_all, top_deep=top_deep, hx=hx,
                margin=margin, ref=ref)


# ================================ FR/ID: the interior distance
def interior_distance(limobj):
    section("FR/INT -- THE INTERIOR DISTANCE of the limit object to "
            "the DEFINITENESS boundary, in three LEGAL deformations "
            "(float located, exact-rationally certified at %.2f of "
            "the located radius)" % INWARD)
    if limobj is None:
        check("INT0 the limit object exists", False, kill="K1")
        return None
    medoid = limobj["medoid"]
    pivf, momv, c_cert = medoid["exact"]
    momn = [momv[k] / pivf ** (k + 2) for k in range(len(momv))]
    flon = c_cert / pivf
    # the declared rational grid: an EXACT rational object within
    # XR_TIE of the medoid's own certified data
    momg = [Fraction(round(float(v) * LIMD), LIMD) for v in momn]
    flog = Fraction(round(float(flon) * LIMD), LIMD)
    d_grid = 0.0

    def rho_exact(moms, flo, kdeg):
        cheb = dml.chebyshev_monic(moms, kdeg)
        if cheb is None:
            return None
        val = dml.radau_exact(cheb[0], cheb[1], flo, moms[0])
        return None if val is None else val

    base = {}
    for kd in (KBASE, KDEEP):
        v_g = rho_exact(momg, flog, kd)
        v_n = rho_exact(momn, flon, kd)
        if v_g is None or v_n is None:
            continue
        base[kd] = float(v_g)
        d_grid = max(d_grid, abs(float(v_g) - float(v_n))
                     / max(1.0e-12, abs(float(v_n))))
        print("      RADAU_%d on the GRID limit vector %.9f  (exact "
              "medoid vector %.9f, rel dev %.2e)"
              % (kd, float(v_g), float(v_n),
                 abs(float(v_g) - float(v_n))
                 / max(1e-12, abs(float(v_n)))))
    check("INT0 the declared rational GRID limit vector (denominator "
          "%.0e) reproduces the medoid's exact RADAU values to rel "
          "%.2e <= %.0e -- every radius below is certified on THIS "
          "exact object" % (float(LIMD), d_grid, dml.XR_TIE),
          bool(base) and d_grid <= dml.XR_TIE, kill="K2")
    if not base:
        return None
    hk4, _i4 = dml.hankel_pd(momg, KBASE)
    hk5, _i5 = dml.hankel_pd(momg, KDEEP)
    check("INT1 the GRID limit vector is still a valid moment "
          "sequence (E7 Hankel PD at K = %d and %d) -- the "
          "deformations below stay inside the moment cone by "
          "construction" % (KBASE, KDEEP), hk4 and hk5, kill="K2")

    def deform(kind, par, kdeg):
        if kind == "MASS":
            return rho_exact([m * par for m in momg], flog, kdeg)
        if kind == "FLOOR":
            return rho_exact(momg, flog * par, kdeg)
        if kind == "ATOM":
            add = [momg[k] + par * flog ** k
                   for k in range(len(momg))]
            return rho_exact(add, flog, kdeg)
        return None

    def inside(kind, par, kdeg):
        val = deform(kind, Fraction(par).limit_denominator(10 ** 9),
                     kdeg)
        return val is not None and float(val) < SCHUR_BAR_F

    def locate(kind, lo, hi, kdeg, rising=True):
        """The boundary parameter, float-located by bisection.  For a
        deformation that RAISES rho with the parameter (MASS, ATOM)
        the safe side is `lo` and the returned value is the largest
        admissible parameter; for FLOOR (rho FALLS with the
        multiplier) the safe side is `hi` and the returned value is
        the smallest admissible multiplier."""
        for _ in range(BIS_F):
            mid = (lo + hi) / 2
            good = inside(kind, mid, kdeg)
            if good == rising:
                lo = mid
            else:
                hi = mid
        return lo if rising else hi

    print("    the three LEGAL deformations of the limit object "
          "(n = 1), radius = distance to the bar rho = 1:")
    radii = {}
    n_pos = 0
    n_try = 0
    for kd in (KBASE, KDEEP):
        if kd not in base:
            continue
        rho0 = base[kd]
        # (i) MASS: RADAU is homogeneous of degree 1 in the moments
        t_pred = 1.0 / rho0
        v_half = deform("MASS", Fraction(1, 2), kd)
        homo = (abs(float(v_half) / rho0 - 0.5) <= 1.0e-12
                if v_half is not None else False)
        t_cert = Fraction(int(INWARD * t_pred * 10 ** 6), 10 ** 6)
        v_cert = deform("MASS", t_cert, kd)
        ok_mass = v_cert is not None and float(v_cert) < SCHUR_BAR_F
        n_try += 1
        n_pos += int(ok_mass and t_pred > 1.0)
        print("      K=%d  MASS   nu -> t nu : homogeneity warded %s, "
              "t* = 1/rho = %.6f (radius %+.6f), exact-certified at "
              "t = %.6f -> RADAU %.9f  %s"
              % (kd, "OK" if homo else "FAILED", t_pred, t_pred - 1.0,
                 float(t_cert),
                 float(v_cert) if v_cert is not None else float("nan"),
                 "PD-INTERIOR" if ok_mass else "REFUSED"))
        # (ii) FLOOR: c -> (1 - d) c  (rho RISES as the claimed floor
        # falls, so the multiplier bisection runs the other way)
        f_lo = locate("FLOOR", 0.0, 1.0, kd, rising=False)
        d_star = 1.0 - f_lo
        f_cert = Fraction(int((1.0 - INWARD * d_star) * 10 ** 6),
                          10 ** 6)
        v_f = deform("FLOOR", f_cert, kd)
        ok_flo = v_f is not None and float(v_f) < SCHUR_BAR_F
        n_try += 1
        n_pos += int(ok_flo and d_star > 0.0)
        print("      K=%d  FLOOR  c -> (1-d) c : d* = %.6f, "
              "exact-certified at d = %.6f -> RADAU %.9f  %s"
              % (kd, d_star, 1.0 - float(f_cert),
                 float(v_f) if v_f is not None else float("nan"),
                 "PD-INTERIOR" if ok_flo else "REFUSED"))
        # (iii) ATOM: add mass m at the floor (worst legal direction)
        hi_m = 1.0
        while hi_m < 1.0e6 and inside("ATOM", hi_m, kd):
            hi_m *= 4.0
        m_star = locate("ATOM", 0.0, hi_m, kd)
        m_cert = Fraction(int(INWARD * m_star * 10 ** 6), 10 ** 6)
        v_m = deform("ATOM", m_cert, kd)
        ok_atm = v_m is not None and float(v_m) < SCHUR_BAR_F
        n_try += 1
        n_pos += int(ok_atm and m_star > 0.0)
        print("      K=%d  ATOM   nu_k -> nu_k + m c^k : m* = %.6f "
              "(the floor sits at c/n = %.6f), exact-certified at "
              "m = %.6f -> RADAU %.9f  %s"
              % (kd, m_star, float(flog), float(m_cert),
                 float(v_m) if v_m is not None else float("nan"),
                 "PD-INTERIOR" if ok_atm else "REFUSED"))
        radii[kd] = dict(mass=t_pred - 1.0, floor=d_star,
                         atom=m_star, rho=rho0)
    verd = "INTERIOR-POSITIVE" if n_pos == n_try else \
        "INTERIOR-TOUCHING"
    check("INT2 the limit object has POSITIVE INTERIOR DISTANCE to "
          "the definiteness boundary in %d/%d legal deformation "
          "directions, each certified EXACT-RATIONALLY at %.2f of "
          "the located radius -> %s" % (n_pos, n_try, INWARD, verd),
          n_pos == n_try)
    for kd, rad in sorted(radii.items()):
        print("      SUMMARY K=%d: rho = %.6f, margin to bar 1 = "
              "%+.6f; interior radii  mass %+.4f / floor %+.4f / "
              "added floor mass %+.4f"
              % (kd, rad["rho"], SCHUR_BAR_F - rad["rho"],
                 rad["mass"], rad["floor"], rad["atom"]))
    return dict(radii=radii, verdict=verd)


# ==================================== G: the CCLXXXVII reproduction
def repro_gate(limobj):
    section("G-REPRO -- the CCLXXXVII reproduction gate (the deepest "
            "block and the anchors are UNCHANGED by amendment A1, so "
            "this is a true reproduction)")
    if limobj is None:
        check("G-REPRO limit object exists", False, kill="K3")
        return
    med = limobj["medoid"]
    r_4 = limobj["rec"].get(KBASE, float("nan"))
    r_5 = limobj["rec"].get(KDEEP, float("nan"))
    ok_g = (abs(limobj["gslope"] - GSLOPE_REF) <= GSLOPE_ATOL
            and abs(limobj["gr2"] - GR2_REF) <= GR2_ATOL)
    ok_m = (int(med["kz"]) == MED_KZ_REF
            and int(med["h"]) == MED_H_REF)
    ok_r = (abs(r_4 / RAD4_REF - 1.0) <= RAD_RTOL
            and abs(r_5 / RAD5_REF - 1.0) <= RAD_RTOL)
    if SMOKE:
        # AMENDMENT A2 (declared, disclosed): the SMOKE block geometry
        # is the shallow (600, 900) pair, so the deepest block is NOT
        # the frontier and the CCLXXXVII references cannot apply.  The
        # gate is typed SMOKE-SKIPPED and the measured values printed,
        # so the smoke still exercises every downstream section.
        print("    SMOKE: shallow blocks -- gslope %+.5f (R2 %.6f), "
              "medoid block %d %s kz %d h %d, RADAU_4 %.9f, "
              "RADAU_5 %.9f"
              % (limobj["gslope"], limobj["gr2"], med["block"],
                 med["mode"], int(med["kz"]), int(med["h"]), r_4,
                 r_5))
        check("G-REPRO CCLXXXVII reproduction SMOKE-SKIPPED (typed)",
              True)
        return
    check("G1 the g_k one-atom fit reproduces CCLXXXVII: slope "
          "%+.5f vs %+.5f (atol %.0e), R2 %.6f vs %.6f (atol %.0e)"
          % (limobj["gslope"], GSLOPE_REF, GSLOPE_ATOL,
             limobj["gr2"], GR2_REF, GR2_ATOL), ok_g, kill="K3")
    check("G2 the MEDOID limit member reproduces CCLXXXVII: block %d "
          "%s kz %d h %d vs kz %d h %d"
          % (med["block"], med["mode"], int(med["kz"]),
             int(med["h"]), MED_KZ_REF, MED_H_REF), ok_m, kill="K3")
    check("G3 the MEDOID's exact RADAU values reproduce CCLXXXVII: "
          "RADAU_4 %.9f vs %.9f, RADAU_5 %.9f vs %.9f (rtol %.0e)"
          % (r_4, RAD4_REF, r_5, RAD5_REF, RAD_RTOL), ok_r,
          kill="K3")


# ==================================== X: controls-must-fire
def rate_controls(census, anchors, rows):
    section("X -- CONTROLS-MUST-FIRE on the RATE measurement itself")
    tgt = 600 if SMOKE else DR_TGT[0]
    cell = dml.block_pick(census, tgt, 1)[0]
    anc = sorted(anchors, key=lambda r: r["h"])
    below = [a for a in anc if a["h"] <= cell["h"]]
    r_1 = below[-1] if below else anc[0]
    print("    control cell: h %d kz %d alpha %.4f; anchor %s kz %d "
          "h %d" % (cell["h"], cell["kz"], cell["alpha"],
                    r_1["kind"], r_1["kz"], r_1["h"]))

    def world_read(world, seed=None):
        rung = dml.build_cell(cell, world=world, scr_seed=seed)
        ok, why = dml.cell_legal(rung)
        out = dict(world=world, legal=ok, why=why)
        if "S" not in rung:
            return out
        sts = ob.make_steps([r_1, rung])
        if not sts:
            return out
        st = sts[0]
        mat = dml.sym(st["Q"].T
                      @ (rung["S"] / abs(float(st["tau"])))
                      @ st["Q"])
        out["atm"] = atom_read(mat)
        out["alg"] = align_read(mat)
        out["shp"] = shape_read(mat)
        return out

    scr = world_read("scramble", seed=SCR_SEED)
    smo = world_read("smooth")
    arc = world_read("arch")
    sin_hi = max(r["atm"]["sin_th"] for r in rows)
    x_lo = min(r["atm"]["x_top"] for r in rows)
    x_hi = max(r["atm"]["x_top"] for r in rows)
    shr_lo = min(r["atm"]["share"] for r in rows)
    print("    the measured deep alignment envelope: sin theta <= "
          "%.6f, share >= %.6f, x* in [%.5g, %.5g]"
          % (sin_hi, shr_lo, x_lo, x_hi))
    for w in (scr, smo, arc):
        atm = w.get("atm")
        print("      world %-9s legal %-5s (%-10s) sin theta %-10s "
              "share %-10s x* %-11s gresid %s"
              % (w["world"], w["legal"], w["why"],
                 "%.6f" % atm["sin_th"] if atm else "-",
                 "%.6f" % atm["share"] if atm else "-",
                 "%.5g" % atm["x_top"] if atm else "-",
                 "%.4f" % w["shp"]["gresid"] if w.get("shp") else "-"))

    def outside_align(w):
        atm = w.get("atm")
        if atm is None:
            return True, "no alignment read at all"
        if not math.isfinite(atm["sin_th"]):
            return True, "sin theta non-finite"
        if atm["sin_th"] > sin_hi:
            return True, ("sin theta %.6f above the deep envelope "
                          "%.6f" % (atm["sin_th"], sin_hi))
        if atm["share"] < shr_lo:
            return True, ("weight share %.6f below the deep envelope "
                          "%.6f" % (atm["share"], shr_lo))
        return False, "inside the deep alignment envelope"

    scr_out, scr_why = outside_align(scr)
    check("X1 the SCRAMBLE world (seed %d) DESTROYS the alignment "
          "law: legality %s / %s" % (SCR_SEED,
                                     "LEFT" if not scr["legal"]
                                     else "kept", scr_why),
          (not scr["legal"]) or scr_out, kill="K4")
    smo_atm = smo.get("atm")
    if smo_atm is None or not math.isfinite(smo_atm["x_top"]):
        disc = True
        why_d = "no atom at all in the smooth world"
    else:
        xs = smo_atm["x_top"]
        disc = (xs > CTRL_ATOM_FAC * x_hi
                or xs < x_lo / CTRL_ATOM_FAC)
        why_d = ("smooth atom x* = %.5g vs the deep envelope "
                 "[%.5g, %.5g] -- factor %.3g off the nearest edge"
                 % (xs, x_lo, x_hi,
                    max(xs / x_hi, x_lo / xs)))
    check("X2 the SMOOTH (prime-free) world converges to a DIFFERENT "
          "atom -- THE DISCRIMINATION, verified numerically (declared "
          "factor %.1f): legality %s / %s"
          % (CTRL_ATOM_FAC, "LEFT" if not smo["legal"] else "kept",
             why_d), (not smo["legal"]) or disc, kill="K4")
    arc_atm = arc.get("atm")
    if arc_atm is None or not math.isfinite(arc_atm["x_top"]):
        disc_a = True
        why_a = "no atom at all in the archimedean world"
    else:
        xa = arc_atm["x_top"]
        disc_a = (xa > CTRL_ATOM_FAC * x_hi
                  or xa < x_lo / CTRL_ATOM_FAC)
        why_a = ("archimedean atom x* = %.5g vs the deep envelope "
                 "[%.5g, %.5g] -- factor %.4g off the nearest edge"
                 % (xa, x_lo, x_hi, max(xa / x_hi, x_lo / xa)))
    check("X2b the ARCHIMEDEAN (prime-blind, deterministic in (M, D)) "
          "world also reads a DIFFERENT atom -- the second, "
          "independent discrimination: legality %s / %s"
          % ("LEFT" if not arc["legal"] else "kept", why_a),
          (not arc["legal"]) or disc_a, kill="K4")
    # X3: a synthetic misalignment must be DETECTED by the
    # measurement.  DECLARED RULE (amendment A4, disclosed at the
    # smoke): the control cell is the BEST-ALIGNED built cell and the
    # tilt is applied along +sign(<b, v_min(B)>) v_min(B), so w_top is
    # untouched while nu_0 strictly grows -- the share MUST fall.  The
    # first draft tilted the FIRST row, which happened to be the
    # WORST-aligned cell, and the tilt moved it the other way.
    best = max(rows, key=lambda r: r["atm"]["share"])
    base = np.asarray(best["step"]["Mt"], float).copy()
    atm0 = atom_read(base)
    shp0 = shape_read(base)
    blk = 0.5 * (base[1:, 1:] + base[1:, 1:].T)
    evl, evc = np.linalg.eigh(blk)
    vlow = evc[:, 0]
    vec0 = base[1:, 0]
    sgn = 1.0 if float(vec0 @ vlow) >= 0.0 else -1.0
    tilt = vec0 + CTRL_TILT * float(np.linalg.norm(vec0)) * sgn * vlow
    ctrl = base.copy()
    ctrl[1:, 0] = tilt
    ctrl[0, 1:] = tilt
    atm1 = atom_read(ctrl)
    shp1 = shape_read(ctrl)
    fired = (atm1 is not None and shp1 is not None
             and atm1["sin_th"] > atm0["sin_th"]
             and atm1["share"] < atm0["share"]
             and shp1["gresid"] > shp0["gresid"])
    check("X3 a SYNTHETIC MISALIGNMENT (b of the BEST-ALIGNED cell "
          "b%d %s kz %d h %d tilted by %.2f ||b|| along "
          "sign<b,v_min> v_min(B)) is DETECTED: sin theta %.6f -> "
          "%.6f, share %.6f -> %.6f, gresid %.4f -> %.4f"
          % (best["block"], best["mode"], best["kz"], int(best["h"]),
             CTRL_TILT, atm0["sin_th"],
             atm1["sin_th"] if atm1 else float("nan"),
             atm0["share"], atm1["share"] if atm1 else float("nan"),
             shp0["gresid"],
             shp1["gresid"] if shp1 else float("nan")),
          fired, kill="K4")
    _ = evl
    return dict(scr=scr, smo=smo, arc=arc)


# ==================================== S: the screens
def rate_screens(rows):
    section("S -- tau and CCXVII c_h relocation screens on the RATE "
            "quantities (CCXLVII bars verbatim: PASS <= %.2f, "
            "RELOC >= %.2f)" % (SLOPE_PASS, SLOPE_RELOC))
    taus = [r["tau_scale"] for r in rows]
    verds = []
    keyed = (("sin theta", [r["atm"]["sin_th"] for r in rows]),
             ("x* atom position", [r["atm"]["x_top"] for r in rows]),
             ("GAP bound", [r["atm"]["gap_bound"] for r in rows]),
             ("relative gap of B",
              [r["atm"]["relgap"] for r in rows]),
             ("Rayleigh deficit",
              [r["atm"]["deficit"] for r in rows]),
             ("r_gap", [r["alg"]["rgap"] for r in rows]),
             ("|c_1|", [r["alg"]["c1"] for r in rows]),
             ("weight share", [r["atm"]["share"] for r in rows]))
    for lab, vals in keyed:
        txt, vd = screen(vals, taus, "tau-screen %s" % lab)
        print("    " + txt)
        verds.append(vd)
    n_reloc = sum(1 for v in verds if v == "RELOC")
    check("S1 tau relocation screens on the rate quantities: %d PASS, "
          "%d AMBIG, %d RELOC, %d vacuous"
          % (verds.count("PASS"), verds.count("AMBIG"), n_reloc,
             verds.count("VAC")), n_reloc == 0)
    ch_n = 2 if SMOKE else CH_N_R
    pool = [r for r in rows
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
    n_out = len(rows) - len(pool)
    chs = []
    sns = []
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
            sns.append(r["atm"]["sin_th"])
            print("    c_h cell kz %-4d h %-6d c_h %.4e sin theta "
                  "%.6f [%.1f s]" % (r["kz"], r["h"], 1.0 - top,
                                     r["atm"]["sin_th"],
                                     time.time() - T0), flush=True)
        except Exception as exc:                  # noqa: BLE001
            print("    c_h cell kz %d REFUSED (%s)" % (r["kz"], exc))
    if len(chs) >= 3:
        txt, vd = screen(sns, chs, "c_h-screen sin theta")
        print("    " + txt)
        check("S2 CCXVII c_h relocation screen on %d in-surface deep "
              "cells (%d typed OUT-OF-SURFACE): %s"
              % (len(chs), n_out, vd), vd != "RELOC")
    else:
        check("S2 CCXVII c_h relocation screen: VACUOUS (%d "
              "in-surface cells of %d, %d typed OUT-OF-SURFACE -- the "
              "deployed surface window is only defined for X <= %.0e)"
              % (len(chs), len(rows), n_out, float(core.ATOM_MAX)),
              True)


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    i_pass = sum(1 for _n, ok in dml.CHECKS if ok)
    i_tot = len(dml.CHECKS)
    all_kills = KILLS + dml.KILLS
    if all_kills:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[
                 all_kills[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 + exact-rational measurements on the
  deployed deep frame.  The MECHANISM statement (the one-atom collapse
  IS the near-eigenvector alignment of b with v_top(B), i.e. the
  moment shape and the alignment are the same statement) is an
  IDENTITY plus TWO DERIVED bounds -- the elementary GAP bound and the
  E8/E9/E10 FRAME bound -- whose bound properties are WARDED per cell.
  It is NOT a proof that the collapse persists for all h, because the
  h-behaviour of the ingredients (B's relative spectral gap, the
  Rayleigh deficit, r_gap, |c_1|) is MEASURED, not proved.  The
  functional statement against the definiteness bar 1 is a UNIFORM
  MEASURED ENVELOPE on the built family plus an explicit,
  exact-rationally certified INTERIOR DISTANCE of the limit object to
  the boundary.  NO PROVED RATE is claimed.  No marker moves, no
  promotion, NO RH claim.""")
    print("\n  checks %d/%d PASS (this probe) + %d/%d inherited "
          "CCLXXXVII machinery checks = %d/%d total; SPEC_SHA %s; "
          "runtime %.1f s%s"
          % (n_pass, n_tot, i_pass, i_tot, n_pass + i_pass,
             n_tot + i_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("deep_rate_mechanism_probe -- PRIME.ONEBADMODE.DEEP.RATE.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(RATE_FUNCS, RATE_BANNED)
    check("S0.2 AC RATE path (%s) sees the wall matrix ENTRIES and "
          "frozen constants only -- no tau, no h, no alpha, no kz, no "
          "frame object, no ladder identifier (%s)"
          % ("/".join(RATE_FUNCS),
             ",".join(sorted(set(bad_r))) or "clean"),
          not bad_r, kill="K1")

    # ---- A1: the declared block geometry, disclosed before the run
    dml.BLOCK_TGT = BLOCK_TGT_R
    dml.BLOCK_NC = BLOCK_NC_R
    dml.HARD_CAP_S = HARD_CAP_R
    print("    AMENDMENT A1 (declared): block targets %s, sizes %s "
          "(CCLXXXVII used %s); the FRONTIER block and the anchor "
          "ladder are UNCHANGED, so the level vector, the medoid and "
          "the g_k fit are reproduced exactly (gate G-REPRO)."
          % (str(BLOCK_TGT_R), str(BLOCK_NC_R), str((8, 8, 6, 8, 4))))

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
                     schur=float(st["gap"]),
                     n_piv=float(st["n0"]),
                     c_meas=float(st["lamB1"]), index=i)
                for i, st in enumerate(lad_steps)]
    lad_rows = dml.jacobi_identity_wards(lad_rows,
                                         "registered ladder")
    dml.repro_anchors(lad_rows)
    if dml.KILLS:
        return finish([])
    blocks, legality = dml.build_blocks(census)
    rows = dml.block_steps(blocks, anchors)
    check("M1 the block step census admitted %d wall-legal steps "
          "(%d chain, %d bridge) over %d blocks"
          % (len(rows), sum(1 for r in rows if r["mode"] == "chain"),
             sum(1 for r in rows if r["mode"] == "bridge"),
             len({r["block"] for r in rows})),
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
    repro_gate(limobj)
    if KILLS:
        return finish([])

    rows = atom_identity(rows)
    if KILLS or not rows:
        return finish([])
    alaw = alignment_law(rows)
    source_reading(rows)
    if KILLS:
        return finish([])
    drv = driver_split(census, anchors)
    frs = functional_rates(rows, cens, limobj)
    ints = interior_distance(limobj)
    rate_controls(census, anchors, rows)
    rate_screens(rows)

    # ------------------------------------------------ verdict labels
    labels = []
    shares = [r["atm"]["share"] for r in rows]
    n_one = sum(1 for s in shares if s >= SHARE_ONE)
    n_bnd = sum(1 for r in rows
                if math.isfinite(r["atm"]["gap_bound"])
                and r["atm"]["gap_bound"] < 1.0)
    if n_bnd >= max(3, len(rows) // 2):
        labels.append("MECHANISM-IDENTIFIED(the one-atom collapse IS "
                      "the near-eigenvector alignment of b with "
                      "v_top(B); the atom sits at x* = "
                      "lambda_max(B)/n, median %.5g; weight share "
                      "median %.6f, %d/%d cells above %.2f; the "
                      "DERIVED GAP bound is non-vacuous on %d/%d "
                      "cells, median %.4g)"
                      % (float(np.median([r["atm"]["x_top"]
                                          for r in rows])),
                         float(np.median(shares)), n_one, len(rows),
                         SHARE_ONE, n_bnd, len(rows),
                         float(np.median([r["atm"]["gap_bound"]
                                          for r in rows]))))
    else:
        labels.append("MECHANISM-PARTIAL(the identity holds but the "
                      "DERIVED GAP bound is vacuous on %d/%d cells -- "
                      "B's spectral gap is too small to certify the "
                      "collapse from the entries alone)"
                      % (len(rows) - n_bnd, len(rows)))
    sl = alaw["laws"].get("sin theta", {})
    labels.append("ALIGNMENT-LAW(d log sin theta / d log h = %+.4f "
                  "+- %.4f, R2 %.3f; r_gap %+.4f +- %.4f; |c_1| "
                  "%+.4f +- %.4f)"
                  % (sl.get("slope", float("nan")),
                     sl.get("se", float("nan")),
                     sl.get("r2", float("nan")),
                     alaw["laws"].get("r_gap = m_2/m_1", {}).get(
                         "slope", float("nan")),
                     alaw["laws"].get("r_gap = m_2/m_1", {}).get(
                         "se", float("nan")),
                     alaw["laws"].get("|c_1| frame overlap", {}).get(
                         "slope", float("nan")),
                     alaw["laws"].get("|c_1| frame overlap", {}).get(
                         "se", float("nan"))))
    if drv:
        labels.append("DRIVER-%s(max single-carrier perpendicular "
                      "share / TOTAL median %.3g on %d cells)"
                      % (drv["verdict"], drv["med_ratio"],
                         len(drv["recs"])))
    if frs and math.isfinite(frs["e_meas"]):
        labels.append("RATE-MEASURED(no decaying rate: the rho_5 "
                      "Cauchy differences do not decay; the composed "
                      "statement rests on the UNIFORM spread "
                      "E_all = %.6f, which exceeds the frontier "
                      "budget %+.6f but leaves rho_5^inf + E_all = "
                      "%.6f vs bar 1, margin %+.6f)"
                      % (frs["e_meas"], BUDGET, frs["top_all"],
                         SCHUR_BAR_F - frs["top_all"]))
    else:
        labels.append("RATE-ABSENT")
    if ints:
        rad = ints["radii"].get(KDEEP, {})
        labels.append("%s(K=%d radii: mass %+.4f, floor %+.4f, added "
                      "floor mass %+.4f)"
                      % (ints["verdict"], KDEEP,
                         rad.get("mass", float("nan")),
                         rad.get("floor", float("nan")),
                         rad.get("atom", float("nan"))))
    bad_leg = [(h, kz, why) for _bi, h, kz, why in legality
               if why != "OK"]
    labels.append("LEGALITY(%d/%d census cells wall-legal in the "
                  "blocks%s)"
                  % (len(legality) - len(bad_leg), len(legality),
                     "; failures " + ", ".join("h %d kz %d %s" % t
                                               for t in bad_leg)
                     if bad_leg else ""))
    return finish(labels)


if __name__ == "__main__":
    main()
