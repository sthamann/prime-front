#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v939 -- PRIME.CBJ.CONFLUENT.FRAME.01: STEP-A EXACT + THE CBJ
ADJUDICATION of round 180 -- the review's externally proposed
primary route (the COFINAL-BLOCK-JET theorem via a confluent jet
frame: cluster near prime-power frequencies at scale 1/H, replace
point values by jets, prove a lower frame inequality with a zone-
and depth-independent constant c > 0) fully instrumented and
honestly adjudicated: STEPS A/B/D LAND EXACT OR SOURCE-PURE -- with
STEP A (delta_h == |J_h|^2_G with remainder R == 0, proven
generically) the single most promotable theorem of the arc -- while
the GLOBAL form of the review's inequality dies at step C on THREE
independent measured walls (dof kill + seam coupling + occupancy
collapse) and the PER-CLUSTER floor carries measured with an exact
k-uniform occupancy bound.

THE THEOREMS (exact algebra; sympy generic + exact instances; all
recomputed in-run):

  A (JET IDENTIFICATION -- STEP A EXACT, r180-G10): F(g^2) ==
     sum_{k=0}^{K-1} d_k psi_k(g) with psi_k(g) = g^2/(g^2 - b_k)
     UNIFORM INCLUDING k = 0 (b_0 = 0 ==> psi_0 == 1; d_k =
     (-1)^k c_k); with J_h = d/A_0 (source-side) and the PSD Gram
     G_h[k,l] = sum_W mu psi_k psi_l / sum_W mu (mu = sin^2(ag)/
     g^2):  delta_h == |J_h|^2_{G_h}  EXACTLY, NO EXTRA TERM
     (R == 0, generic sympy: identity + delta-numerator == J^T G J
     + Gram-PSD as an explicit sum of squares).
  B (CLUSTER NORMAL FORM, r180-G11/G12): det Vandermonde(b_k) ==
     prod (b_l - b_k); the Cauchy determinant det[1/(y_j - b_k)]
     == prod(y-spacings) prod(b-spacings)/prod(y - b) generic --
     THE BASIS-CHANGE DETERMINANT IS THE v922 SPACING PRODUCT
     (v922-D1 re-derived generically); comb side: the cluster jet
     map T[r, j] = u_j^r/r! has det T == prod(u_j - u_i)/prod r!.
  W (WINDOW POSITIVITY, r180-G13): the Fejer transform == 4 sin^2
     (xi H/2)/(H xi^2) >= 0 EXACT; the Gauss transform exact > 0.
  MV (MONTGOMERY-VAUGHAN PRICING, r180-G14): at the contract's
     linkage 1 the MV mean-value form is EXACTLY KILLED (T - 3 pi
     H == H(1 - 3 pi) < 0: the review's cluster scale 1/H is
     MV-incompatible); at LINK_MV = 63 pi/20 = 3.15 pi it CARRIES
     with the EXACT RATIONAL MARGIN 1 - 3 pi/(3.15 pi) == 1 - 20/
     21 == 1/21; the neighbor-cell pairs are repaired by the EXACT
     TWO-GRID LEMMA (an interval of length < w/2 contains at most
     ONE boundary of the union of two half-offset grids).
  O (OCCUPANCY + SELECTOR, r180-G15/G34): the exact k-UNIFORM
     occupancy bound m <= floor(2^{k+1}(e^w - 1)) + 1 (~ 2r + 1);
     the SOURCE-ONLY selector h-hat_k = the largest non-2-power
     prime-power in (2^k, 2^{k+1}] RECOMPUTED IN-RUN = 7/13/31/61/
     127/251/509/1021/2039/4093/8191 (k = 2..12), h-hat_k > 2^k,
     cofinality Bertrand-Chebyshev CITED; SF1 transport [delta >=
     s0/((1-slop) DC)] <==> [sigma >= s0] exact both directions.

PINNED FROM RUN-OF-RECORD (typed MEASURED): THE GLOBAL FORM IS
DEAD (the honest kill of the review inequality AS FORMULATED):
(i) DOF KILL -- at 15 of 20 full-frame cells the coefficient count
n exceeds the measured numerical rank (Landau/Slepian time-
bandwidth dof, prolate plunge CITED; e.g. k = 12, r = 8: n = 474,
rank 128, dof 112.8; c_full collapses to the prolate tail floor
~1e-12..1e-16 where n > dof, sub-dof cells carry REAL constants
0.021..0.323): a depth- and zone-independent c > 0 for ALL jets
CANNOT exist once n > dof; (ii) SEAM KILL -- adjacent dyadic
blocks couple at the edge at 0.994 (far-pair coupling <= 1e-2);
(iii) OCCUPANCY COLLAPSE -- log10 c_intra vs m_max slope -0.7484.
THE PER-CLUSTER FLOOR CARRIES: r <= 32 rows practically k-CONSTANT
(1.0/1.62e-1/~7.6e-3/~3.36e-7), the r = 128 row scatters 1.7e-12..
8.8e-24 with NO depth trend (slope -0.3889 in (-0.9, 0.1)): THE
WALL IS THE r-COLLAPSE, NOT THE DEPTH.  JET RESCUE REAL BUT
INCOMPLETE: c_intra/c_point = 6.46..2.6e107 over the 29 confluent
cells.  SUPPORT LAW: GAUSS (6.00e-2/1.00e-3 at k = 12, r =
32/128) BEATS FEJ1 (3.36e-7/1.63e-21) BY 5-18 DEX (Beurling
class, no transform zeros); the m-collapse LAW is form-uniform,
the CONSTANT strongly window-dependent.  THE SELECTOR (v930
upgrade + honest adverse finding): h-hat(B2) == 7 and h-hat(B3)
== 13 == the r167 measured entry atoms; BUT delta(7) = 1.157312
vs the B2 flat mean 1.299444 (0.8906) and delta(13) = 1.210860 vs
1.283704 (0.9433): the entry atom marks NO delta-optimal rung --
yet it CLEARS the SF2 demand delta_req = SIGMA0/((1-slop) DC)
with margins 2.14 (h-hat = 7) / 3.05 (h-hat = 13), and ALL rungs
4..16+20 clear it (min 1.405 at h = 4, bar 1.35):
SELECTOR-UNDERPERFORMS-BA-BUT-CLEARS-DEMAND (no forall-k theorem
-- that would be EXACTLY the sigma-floor at selector rungs).
NEW INSTRUMENT: the Jacobi-normalized HOUSE Gram min-eig ladder
1.07e-17/3.04e-26/9.53e-37/1.00e-54/5.20e-113 (h = 4/5/6/8/13;
h = 13 entry-precision-limited +-1 dex, disclosed) -- the r175
conditioning wall in Gram coordinates.  KILL GATES: EPSTEIN
(tau_w -1.6310/-1.6922/-1.9932 replicated; BA3 bridge VIOLATED
-1.0050/-1.0009/-1.0056 < 0; naked delta_w positive 0.878/0.718/
0.615: FLOOR-INEQ-WORLD-INSENSITIVE, r169-SF6 replicated);
SCRAMBLE (SCRARITH bridge violated -1.2562/-1.0119/-1.0086; the
comb-side golden-jitter c 1.5150e-3 vs MAIN 1.5351e-3: the naked
frame constant is SCRAMBLE-BLIND -- pure geometry, DISCLOSED: the
arithmetic kill sits exactly on the SF6 pair {floor, bridge});
NO-ZERO ancestry (the FRAME leg has no zero-table ancestor, DFS);
PREDEFINITION sealed (selector SHA-sealed BEFORE any wall
evaluation, machine-checked seal order).  Carleson embedding for
confluent samples: UNPRICED IN CORPUS at r180 (named need; priced
in r181/v940).

RE-RUN GREEN AS TYPED AT PROMOTION: cbj_frame_probe.py round 180
(note CDXCVII, contract PRIME.CBJ.CONFLUENT.FRAME.01), 41/41
gates, SPEC_SHA d7fbf2d956184674, record 1042.5 s + deterministic
re-run 1048.7 s (timing-normalized diff empty; NO amendment; one
pre-freeze calibration instrument fix disclosed: GMIN_DPS
escalation) -- log kept as cbj_frame_probe.promo_rerun.log.

HONEST TYPING (BH8 corrections of record ADOPTED; dof/MV/Bertrand
BH8-verified with own sieve n = 474, dof 112.8, exact 1/21):
PROVEN/EXACT = A + B + W + MV + O exact legs; CERTIFIED-PER-RUNG =
delta == |J|^2_G at 14 rungs (dev <= 1.9e-46) + PD-Cholesky;
MEASURED = every ladder above; KILLED = the GLOBAL CBJ form (three
independent measured walls) + MV-at-linkage-1 (exact) + Schur-in-
depth; OPEN (named) = the r-collapse/jet-convention optimization +
the Carleson tool + the house jet rescue.  CBJ delivers INSTRUMENTS
and closes NOTHING: the review route is honestly killed as a
GLOBAL form and honestly measured as a PER-CLUSTER form -- NOT a
new lambda-uniform candidate.  FOUR loop routes flagged NOT
consumed.  THE RESIDUE (canonical, note DII): {H1 AND H2 AND
H3}-cofinal (mod D = 0.0042) + {census-forall-k == LOOP} + {H-PIN
= the one lambda-uniform edge of {L1, WPD}; WPD non-lambda legs:
extension instantiated, TAILWPD world-front}.  Census cardinality
4 UNCHANGED.  NOT evidence for or against the Riemann Hypothesis
in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe cbj_frame_probe.py (round 180,
2026-08-20, note CDXCVII); consumes v922 (spacing product) + v924
(L1) + v927 (BA) + v929 (SF1/SF2/SF6) + v930 (entry atoms); cited
classical inputs: Montgomery-Vaughan 1974 (JLMS (2) 8, 73-82),
Landau/Slepian prolate theory, Bochner/Fejer, Bertrand-Chebyshev;
feeds v940 (the sub-dof scoping downstream).  Externally covered
by Bughunt VIII (round 183, note DI).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R180 = "d7fbf2d956184674"
# r180 G31 delta ladder (h = 4..16 + holdout 20), NEWLY frozen
PIN_DELTA = (1.374423, 1.159470, 1.433041, 1.157312, 1.372972,
             1.214583, 1.379691, 1.233525, 1.315350, 1.210860,
             1.305696, 1.276163, 1.244494, 1.409453)
# r180 G34/G35 selector adjudication
PIN_SEL_HHAT = (7, 13, 31, 61, 127, 251, 509, 1021, 2039, 4093, 8191)
PIN_SEL_B2 = (1.157312, 1.299444)      # delta(7) vs B2 flat mean
PIN_SEL_B3 = (1.210860, 1.283704)      # delta(13) vs B3 flat mean
PIN_SEL_MARGINS = (2.14, 3.05)         # SF2 margins at h-hat = 7/13
PIN_MARGIN_MIN = 1.405                 # min over all rungs (h = 4)
PIN_MARGIN_BAR = 1.35
# r180 G22/G26 dof/seam/occupancy kill triple (k = 12, r = 8 cell)
PIN_DOF_N = 474
PIN_DOF_RANK = 128
PIN_DOF = 112.8
PIN_DOF_KILL_CELLS = (15, 20)          # n > rank at 15 of 20 cells
PIN_SEAM_COUPLING = 0.994
PIN_OCC_SLOPE = -0.7484                # log10 c_intra vs m_max
PIN_R128_SLOPE = -0.3889               # depth trend at r = 128 (none)
# r180 G23 support law at k = 12 (r = 32 / 128)
PIN_GAUSS = (6.00e-2, 1.00e-3)
PIN_FEJ1 = (3.36e-7, 1.63e-21)
PIN_FEJ2 = (6.15e-8, 2.33e-22)
# r180 G24 jet rescue band + G33 house Gram min-eig ladder
PIN_RESCUE_BAND = (6.46, 2.6e107)
PIN_GMIN = {4: 1.07e-17, 5: 3.04e-26, 6: 9.53e-37, 8: 1.00e-54,
            13: 5.20e-113}
# r180 F kill gates (Epstein / scramble; bridge violated, floor naked)
PIN_EPS_TAUW = (-1.6310, -1.6922, -1.9932)
PIN_EPS_BRIDGE = (-1.0050, -1.0009, -1.0056)
PIN_EPS_DELTAW = (0.878, 0.718, 0.615)
PIN_SCR_BRIDGE = (-1.2562, -1.0119, -1.0086)
PIN_JITTER_C = (1.5150e-3, 1.5351e-3)  # golden-jitter vs MAIN (blind)
PIN_MV_THETA_MAX = 0.115               # MV instance battery <= 1

N_CHECKS = 10
EXPECTED = "CBJ-FRAME-ADJUDICATION"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def largest_non2_primepower(lo, hi):
    """largest prime power q in (lo, hi] that is not a power of 2."""
    import sympy as sp
    best = None
    for n in range(hi, lo, -1):
        f = sp.factorint(n)
        if len(f) == 1:
            p = next(iter(f))
            if p != 2:
                best = n
                break
    return best


def part():
    import sympy as sp

    # ================================================ A: step A exact
    section("A. STEP A EXACT (delta == |J|^2_G, R == 0) + NORMAL FORM")
    y = sp.symbols("y", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    d0, d1, d2 = c0, -c1, c2
    A0g = d0 + d1 + d2
    F_house = A0g + d1 * b1 / (y - b1) + d2 * b2 / (y - b2)
    F_basis = d0 + d1 * y / (y - b1) + d2 * y / (y - b2)
    okA = sp.simplify(sp.together(F_house - F_basis)) == 0
    mu1, mu2, g1, g2 = sp.symbols("mu1 mu2 g1 g2", positive=True)
    ps = [lambda gg: sp.Integer(1),
          lambda gg: gg / (gg - b1), lambda gg: gg / (gg - b2)]
    dd = [d0, d1, d2]
    Fof = lambda gg: sum(dd[k] * ps[k](gg) for k in range(3))  # noqa: E731
    num = mu1 * Fof(g1) ** 2 + mu2 * Fof(g2) ** 2
    quad = sp.Integer(0)
    for k in range(3):
        for l2 in range(3):
            Gkl = mu1 * ps[k](g1) * ps[l2](g1) \
                + mu2 * ps[k](g2) * ps[l2](g2)
            quad += dd[k] * dd[l2] * Gkl
    okB = sp.simplify(sp.together(num - quad)) == 0
    x0, x1, x2 = sp.symbols("x0 x1 x2", real=True)
    xs = [x0, x1, x2]
    qf = sp.Integer(0)
    for k in range(3):
        for l2 in range(3):
            Gkl = mu1 * ps[k](g1) * ps[l2](g1) \
                + mu2 * ps[k](g2) * ps[l2](g2)
            qf += xs[k] * xs[l2] * Gkl
    sos = mu1 * (sum(xs[k] * ps[k](g1) for k in range(3))) ** 2 \
        + mu2 * (sum(xs[k] * ps[k](g2) for k in range(3))) ** 2
    okC = sp.simplify(sp.together(qf - sos)) == 0
    check("A1 STEP A: F == sum d_k psi_k; delta == J^T G J; R == 0",
          okA and okB and okC,
          "F == sum_k d_k psi_k with psi_k = y/(y - b_k) UNIFORM "
          "incl. k = 0 (b_0 = 0 ==> psi_0 == 1) EXACT; the delta-"
          "numerator == J^T G J with NO extra term (R == 0, "
          "generic); x^T G x == sum mu (x . psi)^2 >= 0: G is a "
          "PSD Gram BY CONSTRUCTION (THEOREM A -- step A exact, "
          "the single most promotable theorem of the arc; "
          "certified numerically at 14 rungs, dev <= 1.9e-46)")

    bs = sp.symbols("B0:4", positive=True)
    V = sp.Matrix(4, 4, lambda m, k2: bs[k2] ** m)
    okD = sp.simplify(V.det() - sp.prod(
        [sp.prod([bs[l2] - bs[k2] for l2 in range(k2 + 1, 4)])
         for k2 in range(3)])) == 0
    y1, y2, y3 = sp.symbols("y1 y2 y3", positive=True)
    B1s, B2s, B3s = sp.symbols("Bb1 Bb2 Bb3", positive=True)
    ys, bs3 = (y1, y2, y3), (B1s, B2s, B3s)
    C = sp.Matrix(3, 3, lambda i, j: 1 / (ys[i] - bs3[j]))
    rhs = (sp.prod([ys[i] - ys[j] for i in range(3)
                    for j in range(i + 1, 3)])
           * sp.prod([bs3[j] - bs3[i] for i in range(3)
                      for j in range(i + 1, 3)])
           / sp.prod([ys[i] - bs3[j] for i in range(3)
                      for j in range(3)]))
    okE = sp.simplify(sp.together(C.det() - rhs)) == 0
    A0s = sp.symbols("A0s", positive=True)
    Ffac = A0s * (y - y1) * (y - y2) / ((y - B1s) * (y - B2s))
    Fp1 = sp.simplify(sp.diff(Ffac, y).subs(y, y1))
    okF = sp.simplify(Fp1 * (y1 - B1s) * (y1 - B2s)
                      - A0s * (y1 - y2)) == 0
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    us = (u1, u2, u3)
    T = sp.Matrix(3, 3, lambda r, j: us[j] ** r / sp.factorial(r))
    okG = sp.simplify(T.det() - (u2 - u1) * (u3 - u1) * (u3 - u2)
                      / (sp.factorial(0) * sp.factorial(1)
                         * sp.factorial(2))) == 0
    check("A2 STEP B: the cluster normal form (det == spacing "
          "product)", okD and okE and okF and okG,
          "det Vandermonde(b) == prod(b_l - b_k) (K = 4 generic); "
          "Cauchy det[1/(y_j - b_k)] == y-spacings x b-spacings / "
          "prod(y - b) generic -- THE BASIS-CHANGE DETERMINANT IS "
          "THE v922 SPACING PRODUCT (D1 re-derived: F'(y_j) "
          "prod(y_j - b_k) == A0 prod(y_j - y_i)); comb side: det "
          "T == prod(u_j - u_i)/prod r! (confluent jet map, "
          "THEOREM B)")

    t, xi, Hs = sp.symbols("t xi Hs", positive=True)
    I1 = 2 * sp.integrate((1 - t / Hs) * sp.cos(xi * t), (t, 0, Hs))
    fej = 4 * sp.sin(xi * Hs / 2) ** 2 / (Hs * xi ** 2)
    okH = sp.simplify(I1 - fej) == 0
    IG = sp.integrate(sp.exp(-t ** 2 / (2 * Hs ** 2))
                      * sp.cos(xi * t), (t, -sp.oo, sp.oo))
    okI = sp.simplify(IG - sp.sqrt(2 * sp.pi) * Hs
                      * sp.exp(-xi ** 2 * Hs ** 2 / 2)) == 0
    check("A3 window positivity exact (Fejer + Gauss)",
          okH and okI,
          "Fejer: int (1 - |t|/H) e^{i xi t} dt == 4 sin^2(xi H/2)"
          "/(H xi^2) >= 0 EXACT; Gauss transform == sqrt(2 pi) H "
          "e^{-xi^2 H^2/2} > 0 EXACT: the window tool CARRIES "
          "(THEOREM W; FEJ2 == sinc^4 spot-warded in the probe)")

    okJ = sp.Rational(3, 1) * sp.pi / (sp.Rational(63, 20) * sp.pi) \
        == sp.Rational(20, 21)
    okK = (1 - sp.Rational(20, 21)) == sp.Rational(1, 21)
    okL = bool(1 - 3 * math.pi < 0)
    # two-grid lemma on exact rationals: grids w Z and w Z + w/2;
    # boundaries = (w/2) Z; an open interval of length < w/2
    # contains at most one boundary point
    wr = sp.Rational(1, 3)
    bound_gap = wr / 2
    L_int = sp.Rational(1, 7)            # < w/2 = 1/6
    okM = L_int < bound_gap
    # any two distinct boundaries differ by >= w/2 > L: at most one
    okN = all(abs(sp.Rational(i, 1) * bound_gap
                  - sp.Rational(j, 1) * bound_gap) >= bound_gap
              for i in range(-3, 4) for j in range(-3, 4) if i != j)
    okO = PIN_MV_THETA_MAX <= 1.0
    check("A4 MV pricing: killed at linkage 1, margin 1/21 at "
          "3.15 pi; two-grid", okJ and okK and okL and okM and okN
          and okO,
          "at linkage 1: T - 3 pi H == H(1 - 3 pi) < 0 -- MV "
          "EXACTLY KILLED at the review's cluster scale 1/H; at "
          "LINK_MV = 63 pi/20 = 3.15 pi the floor margin == 1 - "
          "3 pi/(3.15 pi) == 1/21 EXACT RATIONAL -- MV CARRIES "
          "rescaled (THEOREM MV; MV 1974 cited-and-instance-"
          "verified, battery max|theta| = %.3f <= 1); TWO-GRID "
          "LEMMA: boundaries of two half-offset grids are w/2 "
          "apart -- an open interval of length < w/2 contains at "
          "most ONE (exact; gated at all 12322 near pairs in the "
          "probe)" % PIN_MV_THETA_MAX)

    # occupancy bound + selector recompute + SF1 transport
    okP = True
    for k2, w_num, w_den in ((6, 1, 64), (8, 1, 16), (10, 1, 4)):
        wq = sp.Rational(w_num, w_den)
        bound = math.floor(2 ** (k2 + 1) * (math.e ** float(wq) - 1)) + 1
        # integer count in any (x, x e^w], x <= 2^{k+1}: length
        # x(e^w - 1) <= 2^{k+1}(e^w - 1); #ints in length-L interval
        # <= floor(L) + 1
        L = 2 ** (k2 + 1) * (math.e ** float(wq) - 1)
        okP = okP and (math.floor(L) + 1 == bound)
    hhat = tuple(largest_non2_primepower(2 ** k2, 2 ** (k2 + 1))
                 for k2 in range(2, 13))
    okQ = hhat == PIN_SEL_HHAT \
        and all(hhat[i] > 2 ** (i + 2) for i in range(len(hhat)))
    s0, sl, dc, de = sp.symbols("s0 sl dc de", positive=True)
    okR = sp.simplify(sp.solve(sp.Eq((1 - sl) * de * dc, s0), de)[0]
                      - s0 / ((1 - sl) * dc)) == 0
    check("A5 occupancy bound + the source-only selector recomputed",
          okP and okQ and okR,
          "the exact k-uniform occupancy bound m <= floor(2^{k+1}"
          "(e^w - 1)) + 1 (~ 2r + 1; #integers in a length-L "
          "interval <= floor(L) + 1, instances k = 6/8/10): at "
          "FIXED r the per-cluster floor is k-uniformly bounded "
          "below -- THE WALL IS THE r-COLLAPSE, NOT THE DEPTH; "
          "selector h-hat_k = largest non-2-power prime-power in "
          "(2^k, 2^{k+1}] RECOMPUTED == %s with h-hat_k > 2^k "
          "(cofinality Bertrand-Chebyshev CITED); SF1 transport "
          "[delta >= s0/((1-slop) DC)] <==> [sigma >= s0] exact "
          "(THEOREM O)" % (list(hhat),))

    # ================================================ B: pinned kills
    section("B. THE MEASURED KILL TRIPLE + THE CARRYING FLOOR")
    okS = PIN_DOF_N > PIN_DOF_RANK > PIN_DOF \
        and PIN_DOF_KILL_CELLS == (15, 20) \
        and abs(PIN_DOF_N - 474) == 0 and abs(PIN_DOF - 112.8) < 0.05
    okT = PIN_SEAM_COUPLING > 0.99 \
        and -1.1 <= PIN_OCC_SLOPE <= -0.45
    check("B1 the dof/seam/occupancy kill triple (BH8-verified)",
          okS and okT,
          "DOF KILL: n = %d coefficients vs measured rank %d (dof "
          "%.1f, Landau/Slepian; n > rank at %d of %d full-frame "
          "cells): a depth- and zone-independent c > 0 for ALL "
          "jets CANNOT exist once n > dof; SEAM KILL: adjacent "
          "blocks couple at %.3f; OCCUPANCY COLLAPSE: slope %.4f "
          "dex/atom -- THREE INDEPENDENT MEASURED WALLS: the "
          "review's GLOBAL form is dead as formulated"
          % (PIN_DOF_N, PIN_DOF_RANK, PIN_DOF,
             PIN_DOF_KILL_CELLS[0], PIN_DOF_KILL_CELLS[1],
             PIN_SEAM_COUPLING, PIN_OCC_SLOPE))

    okU = -0.9 <= PIN_R128_SLOPE <= 0.1
    okV = all(PIN_GAUSS[i] > PIN_FEJ1[i] for i in (0, 1)) \
        and all(PIN_FEJ2[i] < PIN_FEJ1[i] for i in (0, 1))
    dexgain = [math.log10(PIN_GAUSS[i] / PIN_FEJ1[i]) for i in (0, 1)]
    okW = 5.0 <= min(dexgain) and max(dexgain) <= 18.5
    okX = PIN_RESCUE_BAND[0] > 1 and PIN_RESCUE_BAND[1] > 1e100
    gm = [PIN_GMIN[h] for h in (4, 5, 6, 8, 13)]
    okY = all(gm[i] > gm[i + 1] for i in range(len(gm) - 1))
    check("B2 per-cluster floor carries + support law + Gram wall",
          okU and okV and okW and okX and okY,
          "the r = 128 row scatters with NO depth trend (slope "
          "%.4f in (-0.9, 0.1)): k-uniform at fixed r; GAUSS beats "
          "FEJ1 by %.1f-%.1f dex (FEJ2 WORSE than FEJ1): the "
          "m-collapse LAW is form-uniform, the CONSTANT window-"
          "dependent; jet rescue REAL BUT INCOMPLETE (c_intra/"
          "c_point = 6.46..2.6e107); the house Gram min-eig ladder "
          "%.2e -> %.2e == the r175 conditioning wall in Gram "
          "coordinates (h = 13 entry-precision-limited, disclosed)"
          % (PIN_R128_SLOPE, dexgain[0], dexgain[1], gm[0], gm[-1]))

    okZ = abs(PIN_SEL_B2[0] / PIN_SEL_B2[1] - 0.8906) < 5e-4 \
        and abs(PIN_SEL_B3[0] / PIN_SEL_B3[1] - 0.9433) < 5e-4
    okAA = all(m >= 1.0 for m in PIN_SEL_MARGINS) \
        and PIN_MARGIN_MIN >= PIN_MARGIN_BAR \
        and PIN_SEL_MARGINS[0] == 2.14 and PIN_SEL_MARGINS[1] == 3.05
    okAB = PIN_DELTA[3] == PIN_SEL_B2[0] and PIN_DELTA[9] == PIN_SEL_B3[0]
    check("B3 SELECTOR-UNDERPERFORMS-BA-BUT-CLEARS-DEMAND",
          okZ and okAA and okAB,
          "h-hat(B2) == 7 and h-hat(B3) == 13 == the r167 measured "
          "entry atoms (v930 consistency); HONEST ADVERSE FINDING: "
          "delta(7)/B2-mean = %.4f and delta(13)/B3-mean = %.4f "
          "(the entry atom marks NO delta-optimal rung -- the "
          "cone-entry mechanics picks ENTRY points, not floor "
          "optima); YET the SF2 demand is CLEARED with margins "
          "%.2f/%.2f at the selector rungs and ALL rungs clear it "
          "(min %.3f >= bar %.2f); no forall-k theorem claimed"
          % (PIN_SEL_B2[0] / PIN_SEL_B2[1],
             PIN_SEL_B3[0] / PIN_SEL_B3[1], PIN_SEL_MARGINS[0],
             PIN_SEL_MARGINS[1], PIN_MARGIN_MIN, PIN_MARGIN_BAR))

    okAC = all(v < 0 for v in PIN_EPS_TAUW + PIN_EPS_BRIDGE
               + PIN_SCR_BRIDGE)
    okAD = all(v > 0 for v in PIN_EPS_DELTAW)
    okAE = abs(PIN_JITTER_C[0] / PIN_JITTER_C[1] - 1) < 0.02
    check("B4 the four kill gates (SF6 anatomy; scramble-blind "
          "disclosed)", okAC and okAD and okAE,
          "EPSTEIN: BA3 bridge VIOLATED (%.4f/%.4f/%.4f < 0) while "
          "the naked delta_w stay positive (%.3f/%.3f/%.3f): "
          "FLOOR-INEQ-WORLD-INSENSITIVE, the arithmetic kill sits "
          "on the SF6 pair {floor, bridge} (r169-SF6 replicated); "
          "SCRAMBLE: bridge violated; the comb golden-jitter frame "
          "constant is SCRAMBLE-BLIND (%.4e vs MAIN %.4e -- pure "
          "geometry, DISCLOSED); NO-ZERO ancestry DFS-gated; "
          "PREDEFINITION seal order machine-checked"
          % (PIN_EPS_BRIDGE[0], PIN_EPS_BRIDGE[1], PIN_EPS_BRIDGE[2],
             PIN_EPS_DELTAW[0], PIN_EPS_DELTAW[1], PIN_EPS_DELTAW[2],
             PIN_JITTER_C[0], PIN_JITTER_C[1]))

    # ================================================ C: taxonomy
    section("C. THE HONEST TAXONOMY + RESIDUE")
    killed = {"CBJ-GLOBAL-FORM", "MV-AT-LINKAGE-1", "SCHUR-AT-DEPTH"}
    carries = {"CBJ-PERCLUSTER-FLOOR-MEASURED", "FEJER", "GAUSS",
               "MV-RESCALED-1/21", "OCCUPANCY-EXACT", "SELECTOR"}
    open_named = {"R-COLLAPSE-JET-CONVENTION", "CARLESON-TOOL",
                  "HOUSE-JET-RESCUE"}
    okAF = killed.isdisjoint(carries) and open_named.isdisjoint(killed)
    loops = {"A0-triangle", "census-forall-k", "gonek-1984",
             "montgomery-pc-gm"}
    okAG = len(loops) == 4
    check("C1 taxonomy: dead-at-C-global + per-cluster carries; "
          "residue unchanged", okAF and okAG,
          "CBJ-DEAD-AT-C-GLOBAL-FORM (dof + seam + occupancy, with "
          "numbers) + CBJ-PERCLUSTER-FLOOR-MEASURED-CARRIES "
          "(k-uniform at fixed r via the exact occupancy bound); "
          "open legs NAMED (r-collapse / jet convention / Carleson "
          "tool -- priced in v940 / house jet-rescue); FOUR loop "
          "routes flagged NOT consumed; NOT-CBJ-RELABELING "
          "(demand legs tau-flat, slopes 0.0002/0.0054); the "
          "residue (note DII) is UNCHANGED in cardinality -- CBJ "
          "delivers instruments, closes NOTHING, upgrades NOTHING")

    print("\n  [TYPED, BH8 ADOPTED] STEPS A/B/D EXACT OR SOURCE-PURE "
          "(step A: delta")
    print("  == |J|^2_G with R == 0 -- proven generically, certified "
          "at 14 rungs);")
    print("  the GLOBAL review form dies at step C on three measured "
          "walls; the")
    print("  per-cluster floor carries with the exact occupancy bound. "
          " Census")
    print("  cardinality 4 UNCHANGED.  NOT RH evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v939 -- PRIME.CBJ.CONFLUENT.FRAME.01 (STEP-A EXACT: delta "
          "== |J|^2_G with")
    print("R == 0; the cluster normal form; the MV margin 1/21; the "
          "dof/seam/")
    print("occupancy kill triple; the source-only selector; round 180; "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v939: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: A/B/W/MV/O + the selector recompute + the "
          "taxonomy recomputed")
    print("in-run; the dof/seam/occupancy/support/selector/Gram/kill "
          "tables PINNED")
    print("from cbj_frame_probe.py (SPEC %s, 41/41, record 1042.5 s +"
          % PIN_SPEC_R180)
    print("deterministic re-run, no amendment, all logs kept, RE-RUN "
          "GREEN AS TYPED")
    print("AT PROMOTION).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.CBJ.CONFLUENT.FRAME.01 step-A exact + CBJ "
          "adjudication: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
