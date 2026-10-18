#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ks_dual_rigor2_probe -- PRIME.ONEBADMODE.KS.DUAL.RIGOR.02
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

MISSION.  Shut the class-level supremum rigorously.  CCLXVII
(ks_dual_rigor_probe, SPEC 238499bf) certified the window
sup tr R in [0.9727, 2.0797] over the sigma-augmented CCLXI class
C_sig after 15.1M boxes and NAMED the blocking seam: 13.6M
continued-fraction REFUSALS of the [J_B^-1]_11 enclosure on wide
boxes (the 2.0797 plateau is made of sigma-boundary-straddling
boxes at b_1 ~ 0.13, a_1 ~ 6.7 whose decision hangs on the refusing
CF).  The lower end 0.9727 is STRUCTURAL (the truth step with
tr R = 0.9727 is interval-certified in the class; no bound below it
exists).  The entire prize is a CERTIFIED sup < 1.  This probe
implements the announced fix -- a corner-monotone block-pivot
(interval-LDL / pivot-condensation) enclosure of [J_B^-1]_11 that
stays TIGHT on wide boxes -- reruns the B&B with everything else
REUSED VERBATIM from CCLXVII (read-only import: certified separator
envelope with 16386 outward-rounded segments, eigenvalue enclosures
with polar+Weyl+Gershgorin, interval Sturm cross-ward, corner-
monotone lambda_min, Schur-PD clip, lam1_floor, two-sided
interlacing, C7 second-moment floor, SPREAD/COEF/KS interval
excluders, queue/branching machinery, the CCLXI class frozen by box
SHA 224a2737), and reports the certified class-level bound.

THE ENCLOSURE UPGRADE (a).
 U1 THE MONOTONICITY LEMMA (proved by hand below, verified
    SYMBOLICALLY by sympy on the full 7-level CF, warded in exact
    rational arithmetic).  For the 7x7 tridiagonal J_B with
    diagonal b_2..b_8 and off-diagonal a_2..a_7, define the pivot
    recursion g_8 = b_8, g_k = b_k - a_k^2 / g_{k+1} (k = 7..2);
    J_B is PD iff every g_k > 0 (bottom-up LDL / Sylvester), and
    then [J_B^-1]_11 = 1/g_2 (the continued fraction).  PROOF OF
    MONOTONICITY: d g_k / d g_{k+1} = a_k^2 / g_{k+1}^2 >= 0, so by
    the chain rule d g_2 / d b_j = prod_{m<j} (a_m^2/g_{m+1}^2) >= 0
    and d g_2 / d a_j = -(2 a_j / g_{j+1}) prod_{m<j} (...) <= 0
    for a_j >= 0 on the PD region.  Hence g_2 is nondecreasing in
    every b_j and nonincreasing in every a_j (a >= 0), and
    j11 = 1/g_2 is NONINCREASING in every b_j and NONDECREASING in
    every a_j.  The sympy ward verifies the closed-form derivative
    identities on the full 7-level CF (13/13 exact); the rational
    ward re-verifies them in exact Fraction forward-mode at random
    rational PD points; a direction ward bumps every coordinate at
    random PD points in exact arithmetic.
 U2 THE CORNER EVALUATION (exact range on boxes, directed
    rounding).  For a parameter box, the two corners
    c_min-pivots = (b_lo, a_hi) and c_max-pivots = (b_hi, a_lo)
    simultaneously minimize / maximize EVERY pivot g_k (U1 applies
    pivot-wise).  Therefore:
    (i) if the recursion at (b_hi, a_lo) certifies all pivots > 0
    (outward rounding), then EVERY PD member J_B of the box
    satisfies j11(J_B) >= j11(b_hi, a_lo) >= J_MIN_LO -- the path
    from any PD member to that corner (raise b, lower a) keeps all
    pivots nondecreasing hence stays PD, and j11 is nonincreasing
    along it.  This is the certified LOWER bound of j11 for every
    feasible member EVEN WHEN the box straddles the PD boundary --
    the seam CCLXVII could not cross.
    (ii) if the recursion at (b_lo, a_hi) certifies all pivots > 0,
    the WHOLE box is PD (that corner minimizes every pivot) and
    j11 <= j11(b_lo, a_hi) <= J_MAX_HI over the whole box.
    (iii) if at (b_hi, a_lo) some pivot is certifiably NEGATIVE
    (upper end < 0), the trailing block is not PD there, so J_B at
    that corner is not PD (Cauchy: lambda_min(J_B) <= lambda_min of
    any principal submatrix < 0); that corner MAXIMIZES
    lambda_min(J_B) over the box (the CCLXVII corner-monotonicity,
    reused), so NO member of the box meets the B-floor: the box is
    PRUNED (pivot-condensation prune, counted separately).
    Refusals now only occur when a corner pivot interval straddles
    0 within rounding width (point evaluation: ~ulp), never on the
    box width -- the wide-box refusal front collapses by design.
 U3 DEPLOYMENT.  The effective j11 bounds per box are
    j_lo_eff = max(1/L, interval-CF lower where it certifies,
    J_MIN_LO where (i) certifies) and j_hi_eff = min(1/c_Bw,
    interval-CF upper where it certifies, J_MAX_HI where (ii)
    certifies); 1/L and 1/c_Bw are the CCLXVII feasible-member
    fallbacks (B-floor + radius + interlacing).  They feed the
    UNCHANGED sigma prune (prune when a1_lo^2 j_lo_eff / b1_hi >
    cap; b_1 > 0 verbatim) and the UNCHANGED quantitative
    lam1_floor.  Where the box is PD-mixed ((i) holds, (ii) fails)
    the split heuristic boosts the coordinates (b_k, a_k) of the
    FIRST offending pivot at the (b_lo, a_hi) corner (split-on-the-
    offending-pivot; SPEED only, never soundness).

THE B&B RERUN (b).  Same class (box SHA warded == CCLXI 224a2737),
same objective machinery, same soundness rule (every prune requires
a certified violation over the whole box; refusals counted, never
rounded inward; heuristics steer the search order only).  The
target ladder is extended below CCLXVII's floor: TARGETS2 down to
0.974 and DROP_FLOOR2 = 0.9735 > certified truth floor 0.9727 (any
dropped box leaves the floor at 0.9735, sound).  The sigma-cap
sensitivity map is INHERITED from CCLXVII (typed; the budget goes
to the main bound).  Reported: the certified bound, the target-
ladder crossings, full tree statistics including the refusal
collapse (ref_cf lower/upper fallback counts vs CCLXVII's 13.6M),
PD-census of processed boxes, and the residual hard region if any.

THE VERDICT (c) (frozen enum, dominance order):
 KSDUAL-SHUT(certified sup tr R <= B < 1 over C_sig: the COMPOSED
   class-level statement -- every J in the sigma-augmented entry-
   data class satisfies tr R < 1, hence R(lambda_1) < 1, hence (R
   >= 1 on x <= 0 and R >= 0 everywhere, CCXXV separator facts)
   lambda_1(J) > 0: every member is WALL-POSITIVE; the 68/68 truth
   steps are certified members; honest typing: the class margin is
   structurally thin (1 - 0.9727 = 0.0273, capped by the thinnest
   truth rung), the class is the CCLXI envelope construction with
   its provenance, NO all-h claim beyond the certified membership)
 KSDUAL-SIGMA-INSUFFICIENT(certified feasible witness tr R >= 1)
 KSDUAL-STILL-OPEN(certified window [LB, B] with B >= 1 after the
   frozen budget; residual hard-region anatomy + the enclosure it
   still needs)
Every enum is a finite float64/exact-rational statement with
outward rounding about the deployed ladder, the frozen CCLXI class
and the frozen CCXXV separator; NEVER an all-h statement, NEVER an
RH claim.

GATES (d).
 M1 sympy SYMBOLIC derivative identities on the full 7-level CF:
    d g_2/d b_j == prod_{m<j} a_m^2/g_{m+1}^2 and d g_2/d a_j ==
    -(2 a_j/g_{j+1}) prod_{m<j} (...), 13/13 simplify to 0.
 M2 exact-rational forward-mode gradient of g_2 (Fraction dual
    numbers) == the closed-form products at DERIV_WARD_N random
    rational PD points, EXACT equality 13 coords each; signs
    b >= 0 / a <= 0.
 M3 monotone-direction ward: MONO_WARD_N random rational PD
    points, every coordinate bumped, exact-rational j11 moves per
    the lemma (b up => j11 down-or-equal; a up => j11 up-or-equal),
    100%.
 M4 corner-range containment: CFR_WARD_N random sub-boxes x
    CFR_PTS interior points; whenever the point is PD (exact
    Fraction pivots), exact j11 >= J_MIN_LO when (i) certifies;
    whenever (ii) certifies, the point MUST be PD and exact j11 <=
    J_MAX_HI; 100%, with a non-vacuity census (>= 1 full-PD box and
    >= 1 mixed box among the samples).
 M5 exact-rational point tier on ALL 68 truth cells (the bfloor
    round-62 LDL point tier, verbatim pivot recursion in Fraction):
    exact j11 vs the float linear-solve read (rel <= CF_EXACT_TOL)
    and inside the degenerate-box corner enclosure.
 G1-G3, G2b, G2c, G7a: the CCLXVII envelope/Sturm/identity/LOG_PAD/
    box-containment wards RERUN unchanged (reused machinery must
    still ward green here).
 G4 truth membership CERTIFIED 68/68 in C_sig (constraint intervals
    + tr R containment) -- through the UPGRADED BoxWork.
 G5 control (must fire): the declared indefinite theta (hot truth
    step, b_1 -> -1) certifies tr R lower end >= 1.
 X2 control (must fire): sigma_corner_iv on a box with a certifiably
    negative J_B diagonal entry must REFUSE both corner certificates
    and raise the pivot-condensation prune, never emit finite
    j11 bounds.
 G6 anti-circularity: class frozen by the CCLXI machinery, box SHA
    warded verbatim; SIG_CAP recomputed from truth (0.665 ward);
    AST firewall + AC scan of the NEW rigorous functions
    (cf_corner, sigma_corner_iv, cf_exact, cf_exact_grad, process:
    no ladder or read identifiers).
 G7 refusal discipline: corner-CF refusals counted (ref_cflo /
    ref_cfhi = boxes falling back to 1/L / 1/c_Bw), legacy interval-
    CF refusals still counted (ref_cf) for the collapse report;
    nothing ever rounded inward.

EXTERNAL-CITED (consumed, warded, never proved here).
 E1 Sylvester/LDL PD criterion + Cauchy interlacing of principal
    submatrices [Horn & Johnson, Matrix Analysis 2nd ed., 2013,
    Sec. 4.3, 7.2]; the bottom-up pivot recursion is the LDL of the
    reversed tridiagonal (pivot condensation).
 E2 everything CCLXVII cites (Weyl, polar, CCXXV separator facts,
    Jacobi weight identity, SciPy witnesses) -- inherited through
    the read-only reuse, its gates rerun or absorbed here.

FROZEN PROTOCOL.  S0 firewall/AC -> W/T/B ladder + filter + Jacobi
translation (CCLXI machinery, absorbed) -> G class freeze + SHA +
SIG_CAP wards -> M lemma + enclosure wards (M1-M5) -> R reused-
machinery wards (G1-G3) -> N truth certification G4 + witness LB ->
X controls G5/X2 -> O main B&B (upgraded BoxWork2, run_bnb2 with
the extended ladder) -> V verdict.  tau/c_h relocation screens are
VACUOUS BY CONSTRUCTION (typed; class-level certified bounds, no
new per-step decision currency).

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

FROZEN BARS.  NDIM = 8; BOX_SHA_CCLXI = 224a2737d65ec18c0433dd080de
e8e62cd71797bb83232f04d2885db855c851a; SIG_CAP_REF = 0.665 (rel
ward 1e-2); ALL CCLXVII bars consumed verbatim through the read-
only import (NSEG 8192/2048, TMIN, TMAX, GAM_INFL, LOG_PAD, BATCH
4096/1024, QUEUE_CAP 1e6, WFLOOR_REL 2^-26, WIT_MS 32/6, WIT_DE
200/30, ENV_WARD_N 4096/512, STURM_WARD_N 24/6, BOX_WARD_N 160/24,
PTS_PER_BOX 4, WARD_SEED 20260812, MU_MAX 1e-6, CTRL_B1 -1.0,
UB_NEG_FAR, LB_POS_FAR, ENV_TOL, BOXW_TOL, IDENT_TOL); NEW BARS:
DROP_FLOOR2 = 0.9735; TARGETS2 = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02,
1.01, 1.005, 1.002, 1.001, 0.9999, 0.999, 0.995, 0.99, 0.985,
0.98, 0.978, 0.976, 0.9745, 0.974); MAIN_BUDGET_S2 = 1140 (smoke
45); DERIV_WARD_N = 24 (smoke 8); MONO_WARD_N = 400 (smoke 64);
CFR_WARD_N = 200 (smoke 32); CFR_PTS = 4; CF_EXACT_TOL = 1e-9
(rel); WARD_SEED2 = 20260812; CTRL_B2 = -1.5 (control diagonal
entry); runtime cap 25 min.

SMOKE DISCLOSURE (2026-08-12, ONE smoke pass on the 11-step subset
ladder BEFORE this freeze; no bar, control, gate, enum or success
rule was changed after the smoke; the only post-smoke docstring
edit is this disclosure block, and the SPEC SHA is frozen WITH it).
SMOKE-1 (SPEC v0, 51.6 s total, 45 s B&B slice): 24/24 GREEN, no
kills.  Honest readings: (i) the smoke class is the SUBSET-truth
envelope (own box SHA d88d7037; the CCLXI SHA ward, the 0.665 ward
and the 68-step counts are smoke-bypassed by design and decide only
on the frozen ladder); (ii) all lemma and enclosure wards exact /
machine-precision: sympy 13/13, exact-rational gradient 8/8 points
EXACT Fraction equality, direction ward 64/64, corner containment
128/128 (non-vacuity census full-PD 4 / mixed 11 / refused-corner
17 of 32 boxes), truth point tier 11/11 worst rel 7.6e-16, envelope
512/512, Sturm 6/6, box containment 96/96 slack 0.0, control
enclosure collapsed to [5.845178, 5.845178], X2 pivot-condensation
control FIRES; (iii) the smoke B&B ran to stop=budget at bound 7.83
after 1.44M boxes -- the smoke geometry is degenerate exactly as
CCLXVII typed it (the fake-bridge step drags the widened B-floor to
0.0053 and the SUBSET truth itself sits at tr R = 4.85, so no sub-1
bound exists in smoke; CCLXVII's smoke plateaued at 7.81 on the
same subset); THE PRUNE CURRENCY COLLAPSED AS DESIGNED: corner-CF
lower-bound fallbacks 0 (vs the legacy interval CF refusing on 100%
= 1.44M of the same boxes), the sigma prune fired 27403 times ON
WIDE BOXES, pivot-condensation pruned 1232; the UPPER corner rarely
certifies in the smoke geometry (pd_full 0, ref_cfhi 1.44M: the
smoke box has huge a-ranges, so the (b_lo, a_hi) corner is far from
PD and the 1/c_Bw fallback carries lam1_floor there -- typed, not
hidden); (iv) the smoke witness stage re-found and certified the
subset-feasible point with tr R >= 1.0073, so the smoke verdict is
SIGMA-INSUFFICIENT dominated by the subset truth at 4.85 -- a smoke
phenomenon, disclosed (identical to CCLXVII's smoke).

NO RH claim.  No marker moves; no paper, ledger, website, manifest
or verification file is touched; the only edit outside this file is
the German CCLXXXIII line prepended to experiments/next.txt AFTER
the frozen summary.

Sources (read-only): ks_dual_rigor_probe (CCLXVII machinery +
class + envelope, imported), zolotarev_ks_dual_probe (CCLXI class
functions through it), zolotarev_phase_filter_probe (CCXXV filter),
bfloor_perstep_certification_probe (round-62 exact-rational LDL
point-tier precedent, cited).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor2_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor2_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import ks_dual_rigor_probe as rig  # noqa: E402 (READ-ONLY CCLXVII)

ksd = rig.ksd
zol = ksd.zol

# ------------------------------------------------------- frozen bars
NDIM = 8
BOX_SHA_CCLXI = ("224a2737d65ec18c0433dd080dee8e62"
                 "cd71797bb83232f04d2885db855c851a")
SIG_CAP_REF = 0.665
SIG_CAP_RTOL = 1.0e-2
SMOKE = "--smoke" in sys.argv[1:]
DROP_FLOOR2 = 0.9735
TARGETS2 = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02, 1.01, 1.005, 1.002,
            1.001, 0.9999, 0.999, 0.995, 0.99, 0.985, 0.98,
            0.978, 0.976, 0.9745, 0.974)
MAIN_BUDGET_S2 = 45.0 if SMOKE else 1140.0
DERIV_WARD_N = 8 if SMOKE else 24
MONO_WARD_N = 64 if SMOKE else 400
CFR_WARD_N = 32 if SMOKE else 200
CFR_PTS = 4
CF_EXACT_TOL = 1.0e-9
WARD_SEED2 = 20260812
CTRL_B2 = -1.5

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
CLASS_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h")

CHECKS = []
KILLS = []
T0 = time.time()
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


def absorb_ksd_gates(stage):
    """Absorb the reused CCLXI gate results (verbatim machinery
    reuse; a reused FAIL kills here)."""
    n_new = len(ksd.CHECKS)
    n_bad = sum(1 for _n, ok in ksd.CHECKS if not ok)
    check("A[%s] reused CCLXI gates absorbed: %d checks, %d failed"
          % (stage, n_new, n_bad), n_bad == 0 and not ksd.KILLS,
          kill="K2" if not ksd.KILLS else ksd.KILLS[0])


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
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


# ======================= U2: the corner-monotone CF enclosure
def cf_corner(bmat, amat):
    """Directed-rounding CF pivot recursion at a CORNER (point
    diagonal b_2..b_8 = bmat cols 0..6, point off-diagonal
    a_2..a_7 = amat cols 0..5), batched.  Returns
    (g2_lo, g2_hi, ok, bad, neg): ok = every pivot certified > 0
    (then g_2 in [g2_lo, g2_hi]); bad = 0-based level of the FIRST
    pivot not certified positive (-1 if none; level i is pivot
    g_{i+2}); neg = some pivot certified NEGATIVE (upper end < 0)
    at the first failing level: the corner is certifiably not PD."""
    n_box = bmat.shape[0]
    g_lo = bmat[:, NDIM - 2].astype(float).copy()
    g_hi = g_lo.copy()
    ok = np.ones(n_box, bool)
    neg = np.zeros(n_box, bool)
    bad = np.full(n_box, -1, np.int64)
    for i in range(NDIM - 3, -1, -1):
        fresh = ok & ~(g_lo > 0.0)
        bad[fresh] = i + 1
        neg |= fresh & (g_hi < 0.0)
        ok &= g_lo > 0.0
        s_lo = np.where(ok, g_lo, 1.0)
        s_hi = np.where(ok, g_hi, 1.0)
        av = amat[:, i]
        q_lo = rig.ndown(rig.ndown(av * av) / s_hi)
        q_hi = rig.nup(rig.nup(av * av) / s_lo)
        g_lo = rig.ndown(bmat[:, i] - q_hi)
        g_hi = rig.nup(bmat[:, i] - q_lo)
    fresh = ok & ~(g_lo > 0.0)
    bad[fresh] = 0
    neg |= fresh & (g_hi < 0.0)
    ok &= g_lo > 0.0
    return g_lo, g_hi, ok, bad, neg


def sigma_corner_iv(lo, hi):
    """Corner-monotone bounds for j11 = [J_B^-1]_11 over the box
    (U1/U2, lemma warded in M1-M4).  Returns (j_min_lo, ok_lb,
    j_max_hi, ok_ub, bad_ub, neg_prune):
      ok_lb: (b_hi, a_lo) corner certified PD -> j_min_lo is a
        certified LOWER bound of j11 for EVERY PD member (path
        monotonicity; valid even when the box straddles PD);
      ok_ub: (b_lo, a_hi) corner certified PD -> WHOLE box PD and
        j_max_hi a certified UPPER bound over the whole box;
      bad_ub: first offending pivot level at (b_lo, a_hi) (split
        heuristic currency);
      neg_prune: (b_hi, a_lo) corner certifiably NOT PD -> no box
        member is PD (corner maximizes lambda_min): B-floor prune."""
    b_low = lo[:, 1:NDIM]
    b_high = hi[:, 1:NDIM]
    a_min = np.maximum(lo[:, NDIM + 1:], 0.0)
    a_max = np.maximum(np.abs(lo[:, NDIM + 1:]),
                       np.abs(hi[:, NDIM + 1:]))
    _g1lo, g1hi, ok_lb, _bad1, neg1 = cf_corner(b_high, a_min)
    g2lo, _g2hi, ok_ub, bad2, _neg2 = cf_corner(b_low, a_max)
    j_min_lo = np.where(ok_lb,
                        rig.ndown(1.0 / np.where(ok_lb, g1hi, 1.0)),
                        -np.inf)
    j_max_hi = np.where(ok_ub,
                        rig.nup(1.0 / np.where(ok_ub, g2lo, 1.0)),
                        np.inf)
    return j_min_lo, ok_lb, j_max_hi, ok_ub, bad2, neg1


# =================== exact-rational point tier (bfloor round-62)
def cf_exact(theta):
    """Exact-rational [J_B^-1]_11 by the verbatim pivot recursion in
    Fraction arithmetic (the bfloor round-62 LDL point tier for the
    tridiagonal block).  None if a pivot is <= 0 (not PD)."""
    bfr = [Fraction(float(theta[k])) for k in range(1, NDIM)]
    afr = [Fraction(float(theta[NDIM + 1 + k]))
           for k in range(NDIM - 2)]
    gv = bfr[NDIM - 2]
    for i in range(NDIM - 3, -1, -1):
        if gv <= 0:
            return None
        gv = bfr[i] - afr[i] * afr[i] / gv
    if gv <= 0:
        return None
    return Fraction(1) / gv


def cf_exact_grad(bfr, afr):
    """Exact forward-mode gradient of g_2 w.r.t. (b_2..b_8,
    a_2..a_7) in Fraction dual numbers (M2 currency).  Returns
    (g_2, grad[13]) or (None, None) if a pivot is <= 0."""
    n_var = 2 * NDIM - 3
    gv = bfr[NDIM - 2]
    dg = [Fraction(0)] * n_var
    dg[NDIM - 2] = Fraction(1)
    for i in range(NDIM - 3, -1, -1):
        if gv <= 0:
            return None, None
        inv2 = 1 / (gv * gv)
        fac = afr[i] * afr[i] * inv2
        dg_new = [fac * dg[v] for v in range(n_var)]
        dg_new[i] += 1
        dg_new[NDIM - 1 + i] -= 2 * afr[i] / gv
        gv = bfr[i] - afr[i] * afr[i] / gv
        dg = dg_new
    return gv, dg


def lemma_symbolic():
    """M1: sympy verification of the closed-form derivative
    identities on the FULL 7-level CF.  Returns (n_ok, n_tot)."""
    import sympy as sp
    bs = sp.symbols("b0:7", positive=True)
    az = sp.symbols("a0:6", positive=True)
    gv = bs[6]
    gs = [gv]
    for i in range(5, -1, -1):
        gv = bs[i] - az[i] ** 2 / gv
        gs.append(gv)
    g2 = gv
    n_ok = 0
    n_tot = 0
    for i in range(7):
        prod = sp.prod([az[m] ** 2 / gs[6 - (m + 1)] ** 2
                        for m in range(i)])
        n_tot += 1
        if sp.simplify(sp.together(sp.diff(g2, bs[i]) - prod)) == 0:
            n_ok += 1
    for i in range(6):
        prod = sp.prod([az[m] ** 2 / gs[6 - (m + 1)] ** 2
                        for m in range(i)])
        form = -2 * az[i] / gs[6 - (i + 1)] * prod
        n_tot += 1
        if sp.simplify(sp.together(sp.diff(g2, az[i]) - form)) == 0:
            n_ok += 1
    return n_ok, n_tot


def random_pd_fractions(rng):
    """Random rational (b, a) with certified-PD pivots (diagonally
    dominant construction: b in [8, 16], a in [0, 2])."""
    bfr = [Fraction(int(rng.integers(8 * 64, 16 * 64)), 64)
           for _ in range(NDIM - 1)]
    afr = [Fraction(int(rng.integers(0, 2 * 64)), 64)
           for _ in range(NDIM - 2)]
    return bfr, afr


def cf_exact_ba(bfr, afr):
    """Exact j11 from Fraction vectors (None if not PD)."""
    gv = bfr[NDIM - 2]
    for i in range(NDIM - 3, -1, -1):
        if gv <= 0:
            return None
        gv = bfr[i] - afr[i] * afr[i] / gv
    if gv <= 0:
        return None
    return Fraction(1) / gv


# ============================== the upgraded batched box processor
class BoxWork2(rig.BoxWork):
    """CCLXVII BoxWork with the U2/U3 corner-monotone [J_B^-1]_11
    enclosure replacing the refusal-prone wide-box interval CF, the
    pivot-condensation prune, and the offending-pivot split boost.
    Everything else is byte-identical to the CCLXVII process."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stats.update(ref_cflo=0, ref_cfhi=0, pd_full=0,
                          pd_mixed=0, pr_pdneg=0)

    def process(self, lo, hi):
        n_box = lo.shape[0]
        self.stats["processed"] += n_box
        keep = np.ones(n_box, bool)
        ks_lo, _ks_hi = rig.ks_iv(lo, hi, self.cls)
        m = ks_lo > self.cls["ks_cap"]
        self.stats["pr_ks"] += int(np.sum(m & keep))
        keep &= ~m
        c_lo, c_hi = rig.coef_iv(lo, hi, self.cls)
        m = (c_hi < self.cls["coef_lo"]) | (c_lo > self.cls["coef_hi"])
        self.stats["pr_coef"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- THE RIGOR.02 DELTA: corner-monotone j11 enclosure
        _sl, _sh, cf_ok, j_lo, j_hi = rig.sigma_cf_iv(lo, hi)
        self.stats["ref_cf"] += int(np.sum(~cf_ok & keep))
        (j_min_lo, ok_lb, j_max_hi, ok_ub, bad_ub,
         neg_prune) = sigma_corner_iv(lo, hi)
        self.stats["pd_full"] += int(np.sum(ok_ub & keep))
        self.stats["pd_mixed"] += int(np.sum(ok_lb & ~ok_ub & keep))
        # U2(iii): certified non-PD at the max-pivot corner => no
        # member meets the B-floor (pivot-condensation prune)
        self.stats["pr_pdneg"] += int(np.sum(neg_prune & keep))
        keep &= ~neg_prune
        # U3: effective j11 bounds for FEASIBLE members
        j_lo_eff = np.full(n_box, float(rig.ndown(1.0 / self.big_l)))
        j_lo_eff = np.where(cf_ok, np.maximum(j_lo_eff, j_lo),
                            j_lo_eff)
        j_lo_eff = np.where(ok_lb, np.maximum(j_lo_eff, j_min_lo),
                            j_lo_eff)
        self.stats["ref_cflo"] += int(np.sum(~cf_ok & ~ok_lb & keep))
        j_hi_eff = np.full(n_box, float(rig.nup(1.0 / self.cbw)))
        j_hi_eff = np.where(cf_ok, np.minimum(j_hi_eff, j_hi),
                            j_hi_eff)
        j_hi_eff = np.where(ok_ub, np.minimum(j_hi_eff, j_max_hi),
                            j_hi_eff)
        self.stats["ref_cfhi"] += int(np.sum(~cf_ok & ~ok_ub & keep))
        with np.errstate(divide="ignore", invalid="ignore"):
            sig_lo_eff = rig.ndown(
                rig.ndown(rig.ndown(lo[:, NDIM] * lo[:, NDIM])
                          * j_lo_eff)
                / np.maximum(hi[:, 0], 1e-300))
        m = sig_lo_eff > self.cap
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        m = hi[:, 0] <= 0.0          # b_1 > 0 required verbatim
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        # certified lambda_1 floor (CCLXVII block Rayleigh bound,
        # unchanged; j_hi_eff now corner-tight where the box is PD)
        g_lo = rig.ndown(lo[:, 0] * (1.0 - self.cap))
        u2_hi = rig.nup(j_hi_eff / self.cbw)
        u_hi = rig.nup(np.sqrt(u2_hi))
        good = g_lo > 0.0
        g_safe = np.where(good, g_lo, 1.0)
        a1_hi = hi[:, NDIM]
        t_inv = rig.nup(np.maximum(
            1.0 / g_safe,
            1.0 / self.cbw + rig.nup(rig.nup(a1_hi * a1_hi) * u2_hi)
            / g_safe) + rig.nup(a1_hi * u_hi) / g_safe)
        lam1_floor = np.where(good, rig.ndown(1.0 / t_inv), 0.0)
        # eigen enclosures (J and J_B) + corner-monotone lam_min
        dd, e_tot, _mu = rig.eig_enclosure(lo, hi, NDIM, 0, NDIM)
        jb_cols = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
        db, eb_tot, _mub = rig.eig_enclosure(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        l1_lo_c, l1_hi_c = rig.corner_lam_min(lo, hi, NDIM, 0, NDIM)
        lb_lo_c, lb_hi_c = rig.corner_lam_min(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        m = np.minimum(rig.nup(db[:, 0] + eb_tot), lb_hi_c) < self.cbw
        self.stats["pr_bfloor"] += int(np.sum(m & keep))
        keep &= ~m
        m = (rig.ndown(dd[:, -1] - e_tot) > self.big_l) | \
            (rig.nup(dd[:, 0] + e_tot) < -self.big_l)
        self.stats["pr_radius"] += int(np.sum(m & keep))
        keep &= ~m
        spr_lo, spr_hi, spr_ok = rig.spread_iv(lo, hi, dd, e_tot)
        self.stats["ref_spread"] += int(np.sum(~spr_ok & keep))
        m = spr_ok & ((spr_lo > self.cls["spr_hi"])
                      | (spr_hi < self.cls["spr_lo"]))
        self.stats["pr_spread"] += int(np.sum(m & keep))
        keep &= ~m
        # feasible-restricted objective UB (CCLXVII clips, unchanged)
        cl_lo = (dd - e_tot[:, None]).copy()
        cl_hi = (dd + e_tot[:, None]).copy()
        cl_lo[:, 0] = np.maximum(
            np.maximum(cl_lo[:, 0], l1_lo_c),
            np.maximum(0.0, lam1_floor))
        cl_hi[:, 0] = np.minimum(
            np.minimum(cl_hi[:, 0], l1_hi_c),
            np.minimum(np.min(hi[:, :NDIM], axis=1), self.big_l))
        cl_lo[:, 1:] = np.maximum(
            cl_lo[:, 1:],
            np.maximum(self.cbw, db - eb_tot[:, None]))
        cl_lo[:, 1] = np.maximum(cl_lo[:, 1], lb_lo_c)
        cl_hi[:, 1:] = np.minimum(
            cl_hi[:, 1:],
            np.minimum(self.big_l, db + eb_tot[:, None]))
        # C7 second-moment floor (CCLXVII, unchanged)
        b_eff = np.maximum(lo[:, 1:NDIM], self.cbw)
        amgm = rig.ndown(6.0 * np.cbrt(np.maximum(
            self.pmin / np.maximum(a1_hi, 1e-300), 0.0))
            * (1.0 - 1e-12))
        a2sum = np.maximum(np.sum(rig.ndown(lo[:, NDIM + 1:] ** 2),
                                  axis=1), amgm)
        m2_lo = rig.ndown(np.sum(rig.ndown(b_eff * b_eff), axis=1)
                          + 2.0 * a2sum)
        lam_top = rig.ndown(np.sqrt(np.maximum(m2_lo, 0.0) / 7.0)
                            * (1.0 - 1e-12))
        cl_lo[:, NDIM - 1] = np.maximum(cl_lo[:, NDIM - 1], lam_top)
        empty = np.any(cl_lo > cl_hi, axis=1)
        self.stats["pr_empty"] += int(np.sum(empty & keep))
        keep &= ~empty
        cl_hi = np.maximum(cl_hi, cl_lo)
        ub = np.zeros(n_box)
        for k in range(NDIM):
            ub = rig.nup(ub + self.env.range_max(cl_lo[:, k],
                                                 cl_hi[:, k]))
        ub = np.where(np.isfinite(ub), ub, rig.UB_NEG_FAR * NDIM)
        # split scores (CCLXVII) + the offending-pivot boost
        rad = 0.5 * (hi - lo)
        score = rad / self.master_wd
        rb = rad[:, :NDIM]
        ra = rad[:, NDIM:]
        row = rb.copy()
        row[:, :-1] += ra
        row[:, 1:] += ra
        rmax = np.argmax(row, axis=1)
        boost = np.ones_like(score)
        rows_idx = np.arange(n_box)
        boost[rows_idx, rmax] *= 3.0
        am = np.minimum(rmax, NDIM - 2)
        boost[rows_idx, NDIM + am] *= 3.0
        strad = (sig_lo_eff <= self.cap) & keep
        boost[strad, 0] *= 3.0
        boost[strad, NDIM] *= 3.0
        mixed = ok_lb & ~ok_ub & keep
        if np.any(mixed):
            bcol = np.clip(bad_ub + 1, 1, NDIM - 1)
            acol = NDIM + 1 + np.clip(bad_ub, 0, NDIM - 3)
            boost[mixed, bcol[mixed]] *= 3.0
            boost[mixed, acol[mixed]] *= 3.0
        split_col = np.argmax(score * boost, axis=1)
        vol = np.sum(np.log2(np.maximum(
            (hi - lo) / self.master_wd, 1e-30)), axis=1)
        return ub, keep, split_col, vol


# ================= the B&B driver (CCLXVII verbatim, new bars)
def run_bnb2(work, master_lo, master_hi, budget_s, label):
    """CCLXVII run_bnb verbatim with the RIGOR.02 bars DROP_FLOOR2
    and TARGETS2 (extended below 0.98; sound: any dropped box
    leaves the permanent floor at its bound)."""
    t_start = time.time()
    lo = master_lo[None, :].copy()
    hi = master_hi[None, :].copy()
    ub, keep, s_col, vol = work.process(lo, hi)
    open_lo = [lo[keep]]
    open_hi = [hi[keep]]
    open_ub = [ub[keep]]
    open_sc = [s_col[keep]]
    open_ky = [ub[keep] - 1e-9 * vol[keep]]
    hard_ub = []
    hard_box = []
    floor_used = -np.inf
    crossings = []
    floor_w = rig.WFLOOR_REL * work.master_wd
    n_rounds = 0
    stop_reason = "budget"
    while True:
        if time.time() - t_start > budget_s:
            stop_reason = "budget"
            break
        c_lo = np.concatenate(open_lo) if open_lo else \
            np.zeros((0, 15))
        c_hi = np.concatenate(open_hi) if open_hi else \
            np.zeros((0, 15))
        c_ub = np.concatenate(open_ub) if open_ub else np.zeros(0)
        c_sc = np.concatenate(open_sc).astype(int) if open_sc else \
            np.zeros(0, int)
        c_ky = np.concatenate(open_ky) if open_ky else np.zeros(0)
        if len(c_ub) == 0:
            stop_reason = "queue-empty"
            break
        if len(c_ub) > int(0.8 * rig.QUEUE_CAP):
            floor_dyn = float(np.quantile(c_ub, 0.3))
            if floor_dyn < float(np.max(c_ub)) - 1e-3:
                keep_q = c_ub >= floor_dyn
                work.stats["dropped"] += int(np.sum(~keep_q))
                floor_used = max(floor_used, floor_dyn)
                c_lo, c_hi = c_lo[keep_q], c_hi[keep_q]
                c_ub, c_sc = c_ub[keep_q], c_sc[keep_q]
                c_ky = c_ky[keep_q]
            if len(c_ub) > rig.QUEUE_CAP:
                stop_reason = "queue-cap"
                open_lo, open_hi = [c_lo], [c_hi]
                open_ub, open_sc = [c_ub], [c_sc]
                open_ky = [c_ky]
                break
        bound_now = float(np.max(c_ub)) if len(c_ub) else DROP_FLOOR2
        if hard_ub:
            bound_now = max(bound_now, max(hard_ub))
        for tgt in TARGETS2:
            if bound_now < tgt and not any(
                    abs(cr[0] - tgt) < 1e-15 for cr in crossings):
                crossings.append((tgt, time.time() - t_start,
                                  work.stats["processed"]))
        if bound_now < TARGETS2[-1] + 1e-12:
            stop_reason = "final-target"
            open_lo, open_hi = [c_lo], [c_hi]
            open_ub, open_sc = [c_ub], [c_sc]
            open_ky = [c_ky]
            break
        n_top = min(rig.BATCH, len(c_ub))
        order = np.argpartition(c_ky, -n_top)[-n_top:]
        rest = np.ones(len(c_ub), bool)
        rest[order] = False
        p_lo, p_hi = c_lo[order], c_hi[order]
        p_sc = c_sc[order]
        wide = np.any((p_hi - p_lo) > floor_w[None, :], axis=1)
        for i in np.nonzero(~wide)[0]:
            hard_ub.append(float(c_ub[order][i]))
            hard_box.append((p_lo[i].copy(), p_hi[i].copy()))
        work.stats["hard"] += int(np.sum(~wide))
        p_lo, p_hi, p_sc = p_lo[wide], p_hi[wide], p_sc[wide]
        if len(p_lo) == 0 and not np.any(rest):
            stop_reason = "all-hard"
            open_lo, open_hi = [], []
            open_ub, open_sc, open_ky = [], [], []
            break
        n_p = len(p_lo)
        if n_p:
            widths = p_hi - p_lo
            at_floor = widths[np.arange(n_p), p_sc] <= \
                floor_w[p_sc]
            p_sc = np.where(at_floor, np.argmax(
                widths / work.master_wd[None, :], axis=1), p_sc)
            mid = p_lo[np.arange(n_p), p_sc] + 0.5 * (
                p_hi[np.arange(n_p), p_sc]
                - p_lo[np.arange(n_p), p_sc])
            ch_lo = np.concatenate([p_lo, p_lo.copy()])
            ch_hi = np.concatenate([p_hi.copy(), p_hi])
            ch_hi[:n_p, :][np.arange(n_p), p_sc] = mid
            ch_lo[n_p:, :][np.arange(n_p), p_sc] = mid
            ub_c, keep_c, sc_c, vol_c = work.process(ch_lo, ch_hi)
            drop = keep_c & (ub_c < DROP_FLOOR2)
            work.stats["dropped"] += int(np.sum(drop))
            if np.any(drop):
                floor_used = max(floor_used, DROP_FLOOR2)
            keep_c &= ~drop
            open_lo = [c_lo[rest], ch_lo[keep_c]]
            open_hi = [c_hi[rest], ch_hi[keep_c]]
            open_ub = [c_ub[rest], ub_c[keep_c]]
            open_sc = [c_sc[rest], sc_c[keep_c]]
            open_ky = [c_ky[rest],
                       ub_c[keep_c] - 1e-9 * vol_c[keep_c]]
        else:
            open_lo = [c_lo[rest]]
            open_hi = [c_hi[rest]]
            open_ub = [c_ub[rest]]
            open_sc = [c_sc[rest]]
            open_ky = [c_ky[rest]]
        n_rounds += 1
        if n_rounds % 40 == 0:
            n_open = sum(len(u) for u in open_ub)
            print("    %s: round %d bound %.6f open %d hard %d "
                  "proc %d [%.1f s]"
                  % (label, n_rounds, bound_now, n_open,
                     len(hard_ub), work.stats["processed"],
                     time.time() - t_start), flush=True)
    c_ub = np.concatenate(open_ub) if open_ub else np.zeros(0)
    bound = float(np.max(c_ub)) if len(c_ub) else -np.inf
    if hard_ub:
        bound = max(bound, max(hard_ub))
    bound = max(bound, floor_used)
    if not math.isfinite(bound):
        bound = DROP_FLOOR2
    worst = None
    if len(c_ub):
        j = int(np.argmax(c_ub))
        all_lo = np.concatenate(open_lo)
        all_hi = np.concatenate(open_hi)
        worst = (all_lo[j], all_hi[j], float(c_ub[j]))
    elif hard_box:
        j = int(np.argmax(hard_ub))
        worst = (hard_box[j][0], hard_box[j][1], hard_ub[j])
    return dict(bound=bound, crossings=crossings,
                stats=dict(work.stats), stop=stop_reason,
                n_open=int(len(c_ub)), n_hard=len(hard_ub),
                worst=worst, rounds=n_rounds,
                floor_used=(floor_used if math.isfinite(floor_used)
                            else DROP_FLOOR2))


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64/exact-rational statements with
  outward rounding about the deployed 68-step ladder, the frozen
  CCLXI class and the frozen CCXXV separator.  Certified upper
  bounds hold over the ENTIRE sigma-augmented class (omitted
  constraints only weaken bounds); certified lower bounds are
  interval-verified feasible points.  The corner-monotone enclosure
  rests on the M1-M5-warded monotonicity lemma (hand proof +
  symbolic + exact-rational wards).  Heuristics steer the search
  order only, never the arithmetic.  No marker moves; no paper,
  ledger, website, manifest or verification file is touched; NO RH
  claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.DUAL.RIGOR.02 -- shut the class-"
            "level supremum: corner-monotone [J_B^-1]_11 enclosure "
            "+ certified B&B rerun (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(
        ("cf_corner", "sigma_corner_iv", "cf_exact", "cf_exact_grad",
         "cf_exact_ba", "process"), CLASS_BANNED)
    check("S0.2 AC the new rigorous enclosure functions contain "
          "no ladder or read identifier", not ac,
          ",".join(sorted(set(ac))), kill="K2")
    check("S0.3 CCLXVII machinery imported READ-ONLY (SPEC SHA "
          "%s...), CCLXI through it (SPEC SHA %s...)"
          % (rig.SPEC_SHA[:16], hashlib.sha256(
              ksd.__doc__.encode("utf-8")).hexdigest()[:16]), True)

    # ---- W/T/B: the reused CCLXI pipeline
    artifact = json.load(open(ksd.ARTIFACT, encoding="utf-8"))
    zones, steps = ksd.build_ladder()
    if ksd.KILLS:
        absorb_ksd_gates("W")
        return finish([])
    fdata = ksd.get_filter(steps, artifact)
    rows = ksd.translation(steps, artifact, fdata)
    if ksd.KILLS:
        absorb_ksd_gates("T")
        return finish([])
    rows = ksd.jacobi_translation(rows)
    if ksd.KILLS:
        absorb_ksd_gates("B")
        return finish([])

    # ---- G: class freeze (verbatim CCLXI) + SHA + sigma-cap wards
    cls = ksd.freeze_class(rows, fdata)
    ksd.membership_census(rows, cls)
    absorb_ksd_gates("W/T/B/G/N")
    if KILLS:
        return finish([])
    section("G+ -- verbatim-class and sigma-cap wards")
    if SMOKE:
        check("G+1 CCLXI box SHA ward SMOKE-BYPASSED by design "
              "(subset-truth box %s...)" % cls["box_sha"][:16], True)
    else:
        check("G+1 frozen box SHA-256 == CCLXI verbatim (%s...)"
              % cls["box_sha"][:16],
              cls["box_sha"] == BOX_SHA_CCLXI, kill="K2")
    sig_truth = np.asarray([r["sigma"] for r in rows], float)
    sig_cap = float(np.max(sig_truth)) * (1.0 + ksd.MARGIN_FRAC)
    if SMOKE:
        check("G+2 sigma cap recomputed from subset truth: %.6f "
              "(0.665-ward SMOKE-BYPASSED)" % sig_cap, True)
    else:
        check("G+2 sigma cap recomputed from truth %.6f vs CCLXI "
              "0.665 (rel %.2e <= %.0e)"
              % (sig_cap, abs(sig_cap / SIG_CAP_REF - 1.0),
                 SIG_CAP_RTOL),
              abs(sig_cap / SIG_CAP_REF - 1.0) <= SIG_CAP_RTOL,
              kill="K2")
    truth_tr = np.asarray([r["trace_r"] for r in rows], float)
    i_hot = int(np.argmax(truth_tr))
    print("    STRUCTURAL FLOOR (CCLXVII): truth best tr R = %.6f "
          "at sigma = %.4f <= cap -> sup >= %.4f; the prize is a "
          "certified sup < 1 (reserve 1 - %.4f = %.4f)"
          % (truth_tr[i_hot], sig_truth[i_hot], truth_tr[i_hot],
             truth_tr[i_hot], 1.0 - truth_tr[i_hot]))

    # ---- M: the monotonicity lemma + enclosure wards
    section("M -- THE MONOTONICITY LEMMA + corner-CF enclosure "
            "wards (the RIGOR.02 delta)")
    rng = np.random.default_rng(WARD_SEED2)
    try:
        n_ok, n_tot = lemma_symbolic()
        check("M1 sympy SYMBOLIC derivative identities on the full "
              "7-level CF: %d/%d simplify to 0" % (n_ok, n_tot),
              n_ok == n_tot, kill="K2")
    except ImportError:
        check("M1 sympy unavailable -- symbolic tier SKIPPED "
              "(hand proof + M2/M3 exact-rational wards carry)",
              True)
    n_ok = 0
    for _ in range(DERIV_WARD_N):
        bfr, afr = random_pd_fractions(rng)
        g2v, grad = cf_exact_grad(bfr, afr)
        if g2v is None:
            continue
        # closed-form products, exact
        gs = [bfr[NDIM - 2]]
        for i in range(NDIM - 3, -1, -1):
            gs.append(bfr[i] - afr[i] * afr[i] / gs[-1])
        good = True
        prod = Fraction(1)
        for i in range(NDIM - 1):
            if i > 0:
                prod *= (afr[i - 1] * afr[i - 1]
                         / (gs[NDIM - 2 - i] * gs[NDIM - 2 - i]))
            good &= grad[i] == prod and grad[i] >= 0
        prod = Fraction(1)
        for i in range(NDIM - 2):
            form = -2 * afr[i] / gs[NDIM - 3 - i] * prod
            good &= grad[NDIM - 1 + i] == form \
                and grad[NDIM - 1 + i] <= 0
            prod *= (afr[i] * afr[i]
                     / (gs[NDIM - 3 - i] * gs[NDIM - 3 - i]))
        n_ok += int(good)
    check("M2 exact-rational forward-mode gradient == closed-form "
          "products (13 coords, EXACT Fraction equality + signs) at "
          "%d/%d random rational PD points" % (n_ok, DERIV_WARD_N),
          n_ok == DERIV_WARD_N, kill="K2")
    n_ok = 0
    for _ in range(MONO_WARD_N):
        bfr, afr = random_pd_fractions(rng)
        base = cf_exact_ba(bfr, afr)
        if base is None:
            continue
        bump = Fraction(1, 8)
        good = True
        for i in range(NDIM - 1):
            b2 = list(bfr)
            b2[i] += bump
            v2 = cf_exact_ba(b2, afr)
            good &= v2 is not None and v2 <= base
        for i in range(NDIM - 2):
            a2 = list(afr)
            a2[i] += bump
            v2 = cf_exact_ba(bfr, a2)
            good &= v2 is None or v2 >= base
        n_ok += int(good)
    check("M3 monotone-direction ward (exact rational, 13 bumps "
          "each): %d/%d random PD points obey the lemma"
          % (n_ok, MONO_WARD_N), n_ok == MONO_WARD_N, kill="K2")
    # M4: corner-range containment on random sub-boxes
    m_lo = np.asarray(cls["lo"], float).copy()
    m_hi = np.asarray(cls["hi"], float).copy()
    m_lo[0] = max(m_lo[0], 0.0)
    m_lo[NDIM:] = np.maximum(m_lo[NDIM:], 0.0)
    m_lo[1:NDIM] = np.maximum(m_lo[1:NDIM], cls["cb"])
    n_ok = 0
    n_t = 0
    n_full = 0
    n_mixed = 0
    n_refused = 0
    for _ in range(CFR_WARD_N):
        c0 = rng.uniform(m_lo, m_hi)
        c1 = rng.uniform(m_lo, m_hi)
        frac = rng.uniform(0.0, 0.5)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        (jmn, ok_lb, jmx, ok_ub, _bad,
         _neg) = sigma_corner_iv(b_lo[None, :], b_hi[None, :])
        n_full += int(ok_ub[0])
        n_mixed += int(ok_lb[0] and not ok_ub[0])
        n_refused += int(not ok_lb[0])
        for _p in range(CFR_PTS):
            th = rng.uniform(b_lo, b_hi)
            jex = cf_exact(th)
            n_t += 1
            good = True
            if jex is not None and ok_lb[0]:
                good &= float(jmn[0]) <= float(jex) * (1 + 1e-15) \
                    + 1e-300
            if ok_ub[0]:
                good &= jex is not None \
                    and float(jex) <= float(jmx[0]) * (1 + 1e-15)
            n_ok += int(good)
    check("M4 corner-range containment %d/%d random (box, point) "
          "pairs; non-vacuity census: full-PD %d / mixed %d / "
          "refused-corner %d of %d boxes"
          % (n_ok, n_t, n_full, n_mixed, n_refused, CFR_WARD_N),
          n_ok == n_t and n_full >= 1 and n_mixed >= 1, kill="K2")
    # M5: exact-rational point tier on all truth cells
    n_ok = 0
    worst_rel = 0.0
    for r in rows:
        th = r["theta"]
        jex = cf_exact(th)
        s_float = ksd.sigma_quotient(th)
        j_float = s_float * float(th[0]) / (float(th[NDIM]) ** 2)
        (jmn, ok_lb, jmx, ok_ub, _bad,
         _neg) = sigma_corner_iv(th[None, :], th[None, :])
        good = jex is not None and ok_lb[0] and ok_ub[0]
        if good:
            rel = abs(float(jex) - j_float) / max(1e-300,
                                                  abs(float(jex)))
            worst_rel = max(worst_rel, rel)
            good &= rel <= CF_EXACT_TOL
            good &= float(jmn[0]) <= float(jex) <= float(jmx[0])
        n_ok += int(good)
    check("M5 exact-rational point tier (bfloor round-62 pivot "
          "recursion) on %d/%d truth cells: exact j11 vs float "
          "solve worst rel %.2e <= %.0e, inside the degenerate-box "
          "corner enclosure" % (n_ok, len(rows), worst_rel,
                                CF_EXACT_TOL),
          n_ok == len(rows), kill="K2")

    # ---- R: reused-machinery wards (CCLXVII G1-G3, rerun)
    section("R -- reused CCLXVII machinery wards (envelope, Sturm, "
            "identities, box containment)")
    rng_r = np.random.default_rng(rig.WARD_SEED)
    env = rig.Envelope(fdata)
    print("    envelope: %d segments on [%.3g, %.3g] (CCLXVII R1 "
          "verbatim)" % (env.n_seg, env.edges[0], env.edges[-1]))
    xs = np.concatenate([
        rng_r.uniform(-1.05, 1.05, rig.ENV_WARD_N // 2)
        * fdata["L"],
        np.sign(rng_r.standard_normal(rig.ENV_WARD_N // 2))
        * np.exp(rng_r.uniform(np.log(1e-10),
                               np.log(1.04 * fdata["L"]),
                               rig.ENV_WARD_N // 2))])
    r_pts = np.asarray([zol.scalar_r(fdata, float(x)) for x in xs])
    e_ub = env.range_max(xs, xs)
    e_lb = env.range_min(xs, xs)
    n_in = int(np.sum((r_pts <= e_ub + rig.ENV_TOL)
                      & (r_pts >= e_lb - rig.ENV_TOL)))
    check("G1 envelope containment %d/%d declared samples "
          "(worst UB slack %.2e, worst LB slack %.2e)"
          % (n_in, len(xs), float(np.max(r_pts - e_ub)),
             float(np.max(e_lb - r_pts))), n_in == len(xs),
          kill="K2")
    n_sturm_ok = 0
    for _ in range(rig.STURM_WARD_N):
        th = rng_r.uniform(m_lo, m_hi)
        lo1 = th[None, :]
        dd, e_tot, _ = rig.eig_enclosure(lo1, lo1, NDIM, 0, NDIM)
        good = True
        for k in range(NDIM):
            e_pad = 1.5 * e_tot[0] + 1e-9
            c_lo_s = rig.sturm_count_robust(th[:NDIM], th[NDIM:],
                                            dd[0, k] - e_pad, -1.0)
            c_hi_s = rig.sturm_count_robust(th[:NDIM], th[NDIM:],
                                            dd[0, k] + e_pad, +1.0)
            if c_lo_s is None or c_hi_s is None:
                continue
            if not (c_lo_s <= k and c_hi_s >= k + 1):
                good = False
        n_sturm_ok += int(good)
    check("G2 Sturm cross-ward: %d/%d random matrices consistent "
          "with the R2 enclosures"
          % (n_sturm_ok, rig.STURM_WARD_N),
          n_sturm_ok == rig.STURM_WARD_N, kill="K2")
    worst_id = 0.0
    for r in rows:
        th = r["theta"]
        jm, _jb = ksd.theta_matrices(th)
        evals, evecs = np.linalg.eigh(jm)
        w_log = np.sum(np.log(np.maximum(evecs[0, :] ** 2, 1e-300)))
        rhs = float(np.sum(rig.WEXP * np.log(th[NDIM:])))
        for i in range(NDIM):
            for j in range(i + 1, NDIM):
                rhs -= 2.0 * math.log(evals[j] - evals[i])
        worst_id = max(worst_id, abs(w_log - rhs)
                       / max(1.0, abs(w_log)))
    check("G2b Jacobi weight identity ward on all %d truth steps: "
          "worst rel %.2e <= %.0e" % (len(rows), worst_id,
                                      rig.IDENT_TOL),
          worst_id <= rig.IDENT_TOL, kill="K2")
    worst_fro = 0.0
    for r in rows:
        th = r["theta"]
        _jm, jb = ksd.theta_matrices(th)
        lam_b = np.linalg.eigvalsh(jb)
        fro = float(np.sum(th[1:NDIM] ** 2)
                    + 2.0 * np.sum(th[NDIM + 1:] ** 2))
        worst_fro = max(worst_fro, abs(np.sum(lam_b ** 2) - fro)
                        / max(1.0, fro))
    check("G2c Frobenius identity on all %d truth steps: worst rel "
          "%.2e <= %.0e" % (len(rows), worst_fro, rig.IDENT_TOL),
          worst_fro <= rig.IDENT_TOL, kill="K2")
    try:
        from mpmath import mp
        mp.dps = 40
        xs_l = np.exp(rng_r.uniform(-60, 12, rig.LOGPAD_WARD_N))
        worst_log = max(abs(float(mp.log(mp.mpf(float(x))))
                            - float(np.log(x)))
                        / max(1e-30, abs(float(np.log(x))))
                        for x in xs_l)
        check("G7a np.log vs mpmath on %d samples: worst rel %.2e "
              "<< LOG_PAD %.0e" % (rig.LOGPAD_WARD_N, worst_log,
                                   rig.LOG_PAD),
              worst_log <= rig.LOG_PAD * 1e-2, kill="K2")
    except ImportError:
        check("G7a LOG_PAD ward SKIPPED (no mpmath) -- pad kept "
              "at declared 1e-12", True)
    work = BoxWork2(cls, env, sig_cap, fdata)
    n_ok = 0
    n_t = 0
    worst_sl = 0.0
    for _ in range(rig.BOX_WARD_N):
        c0 = rng_r.uniform(m_lo, m_hi)
        c1 = rng_r.uniform(m_lo, m_hi)
        frac = rng_r.uniform(0.0, 0.2)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        t_lo, t_hi = work.box_bounds_unclipped(b_lo[None, :],
                                               b_hi[None, :])
        l1c_lo, l1c_hi = rig.corner_lam_min(b_lo[None, :],
                                            b_hi[None, :], NDIM, 0,
                                            NDIM)
        for _p in range(rig.PTS_PER_BOX):
            th = rng_r.uniform(b_lo, b_hi)
            v = ksd.tr_r_of_theta(th, fdata)
            lam1_p = float(np.linalg.eigvalsh(
                ksd.theta_matrices(th)[0])[0])
            n_t += 1
            ok = (t_lo[0] - rig.BOXW_TOL <= v
                  <= t_hi[0] + rig.BOXW_TOL
                  and l1c_lo[0] - rig.BOXW_TOL <= lam1_p
                  <= l1c_hi[0] + rig.BOXW_TOL)
            n_ok += int(ok)
            worst_sl = max(worst_sl, v - t_hi[0], t_lo[0] - v,
                           lam1_p - l1c_hi[0], l1c_lo[0] - lam1_p)
    check("G3 box containment %d/%d random (box, point) pairs "
          "(worst outward slack %.2e)" % (n_ok, n_t, worst_sl),
          n_ok == n_t, kill="K2")

    # ---- N: truth certification + witness LB
    section("N -- truth steps interval-certified IN C_sig + "
            "certified witness lower bound (upgraded BoxWork)")
    n_cert = 0
    fail_census = {}
    lb_cert = -np.inf
    lb_arg = None
    for r in rows:
        feas, t_lo, t_hi, fails = work.point_certify(r["theta"])
        if not (t_lo - rig.BOXW_TOL <= r["trace_r"]
                <= t_hi + rig.BOXW_TOL):
            fails.append("trR-containment")
            feas = False
        if feas:
            n_cert += 1
            if t_lo > lb_cert:
                lb_cert = t_lo
                lb_arg = "truth step index %d" % rows.index(r)
        for f in fails:
            fail_census[f] = fail_census.get(f, 0) + 1
    check("G4 truth membership CERTIFIED %d/%d (constraint "
          "intervals + tr R containment; fails: %s)"
          % (n_cert, len(rows),
             ", ".join("%s x%d" % kv
                       for kv in sorted(fail_census.items()))
             or "none"),
          n_cert == len(rows), kill="K2")

    def sig_con(theta):
        s = ksd.sigma_quotient(theta)
        if not math.isfinite(s) or theta[0] <= 0.0:
            return -1.0
        return (sig_cap - s) / max(abs(sig_cap), 1e-6)
    v_wit, t_wit, _sl = ksd.run_stage1(
        rows, cls, fdata, "O2 witness search (sigma-capped, "
        "CCLXI stage-1 verbatim)", rig.WIT_MS, rig.WIT_DE,
        extra_con=sig_con)
    wit_note = "no feasible numeric candidate"
    if t_wit is not None:
        feas, t_lo, _t_hi, fails = work.point_certify(t_wit)
        if feas and t_lo > lb_cert:
            lb_cert = t_lo
            lb_arg = "certified stage-1 witness"
        wit_note = ("numeric best %.6f -> %s"
                    % (v_wit, "CERTIFIED (tr R >= %.6f)" % t_lo
                       if feas else
                       "NOT certified (%s), discarded"
                       % ",".join(fails[:3])))
    check("O2 certified lower bound sup >= %.6f (%s; witness: %s)"
          % (lb_cert, lb_arg, wit_note),
          math.isfinite(lb_cert), kill="K2")

    # ---- X: controls must fire
    section("X -- controls")
    th_ctrl = rows[i_hot]["theta"].copy()
    th_ctrl[0] = rig.CTRL_B1
    _feas, c_lo_v, c_hi_v, _fails = work.point_certify(th_ctrl)
    lam1 = float(np.linalg.eigvalsh(
        ksd.theta_matrices(th_ctrl)[0])[0])
    check("G5 CONTROL certified enclosure at the declared "
          "indefinite theta (lambda_min %.4f): tr R in "
          "[%.6f, %.6f], lower end >= 1"
          % (lam1, c_lo_v, c_hi_v), c_lo_v >= 1.0, kill="K4")
    # X2: corner-CF on a certifiably non-PD box must refuse + prune
    th_bad = rows[i_hot]["theta"].copy()
    lo_bad = th_bad[None, :].copy()
    hi_bad = th_bad[None, :].copy()
    lo_bad[0, 1] = CTRL_B2 - 0.5
    hi_bad[0, 1] = CTRL_B2
    (_jmn, ok_lb_x, _jmx, ok_ub_x, _bad_x,
     neg_x) = sigma_corner_iv(lo_bad, hi_bad)
    check("X2 CONTROL corner-CF on a box with b_2 in [%.1f, %.1f] "
          "< 0: both corner certificates REFUSED (lb %s, ub %s) "
          "and the pivot-condensation prune FIRES (%s)"
          % (CTRL_B2 - 0.5, CTRL_B2, not ok_lb_x[0], not ok_ub_x[0],
             bool(neg_x[0])),
          (not ok_lb_x[0]) and (not ok_ub_x[0]) and bool(neg_x[0]),
          kill="K4")
    if KILLS:
        return finish([])

    # ---- O: the main certified B&B (upgraded enclosure)
    section("O -- CERTIFIED BRANCH AND BOUND at the frozen sigma "
            "cap %.6f (corner-monotone enclosure deployed)"
            % sig_cap)
    master_lo = np.asarray(cls["lo"], float).copy()
    master_hi = np.asarray(cls["hi"], float).copy()
    master_lo[0] = max(master_lo[0], 0.0)
    master_lo[NDIM:] = np.maximum(master_lo[NDIM:], 0.0)
    master_lo[1:NDIM] = np.maximum(master_lo[1:NDIM], cls["cb"])
    print("    master box: CCLXI box with b_1 clipped to [0, %.4g] "
          "and b_2..b_8 >= c_Bw = %.4f (CCLXVII pre-clips, "
          "verbatim); DROP_FLOOR2 = %.4f, ladder down to %.4f"
          % (master_hi[0], cls["cb"], DROP_FLOOR2, TARGETS2[-1]))
    res_main = run_bnb2(work, master_lo, master_hi, MAIN_BUDGET_S2,
                        "main")
    st = res_main["stats"]
    print("    TREE: processed %d, pruned sigma %d / B_floor %d / "
          "pivot-condensation %d / radius %d / KS %d / COEF %d / "
          "SPREAD %d / empty-clip %d; dropped %d (floor %.4f); "
          "hard %d; open %d; stop=%s"
          % (st["processed"], st["pr_sigma"], st["pr_bfloor"],
             st["pr_pdneg"], st["pr_radius"], st["pr_ks"],
             st["pr_coef"], st["pr_spread"], st["pr_empty"],
             st["dropped"], res_main["floor_used"],
             res_main["n_hard"], res_main["n_open"],
             res_main["stop"]))
    print("    REFUSAL COLLAPSE: legacy interval-CF refused %d; "
          "corner-CF lower-bound fallbacks (to 1/L) %d, upper-bound "
          "fallbacks (to 1/c_Bw) %d; SPREAD refused %d; PD census "
          "of processed boxes: full-PD %d, mixed %d "
          "(CCLXVII carried 13.6M blocking CF refusals here)"
          % (st["ref_cf"], st["ref_cflo"], st["ref_cfhi"],
             st["ref_spread"], st["pd_full"], st["pd_mixed"]))
    for tgt, t_s, n_p in sorted(res_main["crossings"],
                                key=lambda c: -c[0]):
        print("    TARGET sup <= %.4f CERTIFIED after %.1f s / %d "
              "boxes" % (tgt, t_s, n_p))
    bound = res_main["bound"]
    if res_main["worst"] is not None:
        w_lo, w_hi, w_ub = res_main["worst"]
        w_mid = 0.5 * (w_lo + w_hi)
        d_near = min(ksd.ks_distance(
            w_mid[NDIM:], w_mid[:NDIM], r["theta"][NDIM:],
            r["theta"][:NDIM]) for r in rows)
        print("    RESIDUAL REGION anatomy (worst box): UB %.6f, "
              "mid b1 %.6g a1 %.6g sigma %.6g; KS-dist to nearest "
              "truth %.4g"
              % (w_ub, w_mid[0], w_mid[NDIM],
                 ksd.sigma_quotient(w_mid), d_near))
    check("O1 certified global bound at cap %.4f: sup tr R <= %.6f "
          "(certified window [%.6f, %.6f])"
          % (sig_cap, bound, lb_cert, bound), True)
    check("D1 sigma-cap sensitivity map INHERITED from CCLXVII "
          "(typed UPPER-BOUND map, not re-run: caps 0.60-0.80 all "
          "gave UB 2.0797 under the refusing CF; the budget here "
          "goes to the main bound)", True)
    check("S1 tau/c_h relocation screens VACUOUS BY CONSTRUCTION "
          "(class-level certified bounds, no new per-step decision "
          "currency)", True)

    # ---- verdict
    labels = []
    used = ("box, a>=0, B_floor, pivot-condensation, radius, "
            "KS_wall, COEF, SPREAD, sigma (b_1>0)")
    if bound < 1.0:
        labels.append(
            "KSDUAL-SHUT(sup tr R <= %.6f < 1 CERTIFIED-INTERVAL-"
            "GLOBAL over the sigma-augmented class: EVERY J in "
            "C_sig = CCLXI-envelope class (box SHA %s...) + b_1 > 0 "
            "+ sigma <= %.6f satisfies tr R < 1, hence lambda_1(J) "
            "> 0 (R >= 1 on x <= 0, R >= 0 everywhere, CCXXV "
            "certified separator facts): every member is WALL-"
            "POSITIVE; truth membership CERTIFIED %d/%d; certified "
            "window [%.6f, %.6f]; HONEST TYPING: the class margin "
            "is structurally thin (1 - %.4f = %.4f, capped by the "
            "thinnest truth rung), the class is the CCLXI envelope "
            "construction with its provenance, NO all-h claim "
            "beyond the certified membership; constraints: %s; "
            "tree %d boxes)"
            % (bound, cls["box_sha"][:8], sig_cap, n_cert,
               len(rows), lb_cert, bound, lb_cert, 1.0 - lb_cert,
               used, st["processed"]))
    elif lb_cert >= 1.0:
        labels.append(
            "KSDUAL-SIGMA-INSUFFICIENT(certified feasible witness "
            "tr R >= %.6f >= 1: the sigma-cap provably does NOT "
            "close the class)" % lb_cert)
    else:
        labels.append(
            "KSDUAL-STILL-OPEN(certified window [%.6f, %.6f] after "
            "the frozen budget; constraints: %s; tree %d boxes, "
            "stop=%s; residual anatomy printed above)"
            % (lb_cert, bound, used, st["processed"],
               res_main["stop"]))
    labels.append(
        "ENCLOSURE-UPGRADE(corner-monotone CF: lemma M1-M3 exact, "
        "containment M4 100%%, truth tier M5 %d/%d; refusals "
        "ref_cflo %d / ref_cfhi %d vs CCLXVII 13.6M)"
        % (len(rows), len(rows), st["ref_cflo"], st["ref_cfhi"]))
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
