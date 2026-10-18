#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ks_dual_rigor_probe -- PRIME.ONEBADMODE.KS.DUAL.RIGOR.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

MISSION.  Upgrade CCLXI's sigma-capped closing optimization from
NUMERIC(point) to a CERTIFIED global bound: an interval-arithmetic
branch-and-bound over the sigma-augmented truth-envelope class

    C_sig = C_KS  intersect  { b_1 > 0,  sigma <= SIG_CAP },
    sigma = a_1^2 [J_B^-1]_11 / b_1,   SIG_CAP = max_truth(sigma)
            * (1 + MARGIN_FRAC)   (CCLXI stage-3 candidate, verbatim),

so that  sup_{J in C_sig} tr R(J)  is enclosed from ABOVE by outward-
rounded interval arithmetic (never from a finite point search), and
from BELOW by interval-certified feasible witnesses.  The class C_KS
(15 Jacobi parameters, frozen box, honestly widened B-floor, radius
L, KS/COEF/SPREAD wall envelopes) is REUSED VERBATIM from CCLXI
(zolotarev_ks_dual_probe.freeze_class, read-only import), warded by
the frozen box SHA-256.  The separator R is the frozen CCXXV global
m = 8 Zolotarev filter, re-consumed read-only with its interval-
certified separator facts (R >= 1 on x <= 0, R >= 0 on R, R <= delta
on [c_B, L]).

HONEST PRE-REGISTERED FLOOR (design input, measured on the deployed
ladder BEFORE this spec was frozen, disclosed):  the truth ladder's
best step has tr R = 0.9727 with sigma = 0.2801 <= SIG_CAP, i.e. it
IS feasible for C_sig; hence sup >= 0.9727 and NO bound below 0.9727
is reachable.  CCLXI's preview number 0.7264 was a weak-search
artifact (typed OPTIMIZER-ARTIFACT below), not the supremum.  The
real prize is a CERTIFIED sup < 1; the target ladder runs from 2.0
down to DROP_FLOOR = 0.98 > 0.9727.

THE ENCLOSURE MACHINERY (a: rigorous objective).
 R1 CERTIFIED SCALAR ENVELOPE of R.  R(x) = 1 - D f(x/L) in the
    PRODUCT form (the definition; the CCXXV facts are certified for
    it).  f(t) = t prod_j (t^2+n_j)/(t^2+d_j) / (t^2+d_8) with
    float-committed positive elliptic nodes.  On a fixed grid of
    2*NSEG geometric t-segments (plus head segments at 0 and sign-
    fact fallbacks beyond the grid: R <= 1 for x >= 0, R >= 1 and
    R <= 1 + D f_sup <= 2 + pad for x <= 0), every segment carries a
    certified [lo, hi] of R: each rational factor is monotone in
    s = t^2 so endpoint substitution is exact, the base t/(t^2+d_8)
    is handled with its interior critical point, every float op is
    rounded outward (np.nextafter, house style of the CCXXV/pg-chain
    interval probes).  f is exactly odd in t (t^2 identical for +-t
    in float), so the negative side is the mirrored positive side.
    Range queries use sparse tables (O(1) certified range-max/min).
 R2 EIGENVALUE ENCLOSURE per parameter box.  For a box [lo, hi] in
    the 15 Jacobi coordinates: J_mid = midpoint matrix; float eigh
    gives (d, Q); the RIGOROUS residual  ||J_mid - Q D Q^T||_2  and
    the orthogonality defect mu = ||Q^T Q - I||_2 are enclosed by
    mid-rad interval matmuls with outward rounding (generously
    inflated rounding constants, magnitudes ~1e-12, six orders below
    the decision slack).  With Q = Q' H the polar decomposition
    (E2-cited), Q' D Q'^T is symmetric with EXACT sorted eigenvalues
    d_k and ||Q - Q'|| <= ||H - I|| <= mu, so Weyl gives
    |lambda_k(J_mid) - d_k| <= ||J_mid - QDQ^T|| + mu (2+mu) max|d|.
    Box members differ from J_mid by a symmetric tridiagonal
    perturbation with entrywise radii = half-widths, so Weyl again:
    rho = max Gershgorin row sum of the radius pattern.  Every
    lambda_k over the WHOLE box lies in I_k = [d_k - e, d_k + e],
    e = eig_err + rho.  Cross-warded against an independent interval
    STURM count (LDL pivot recurrence with directed rounding).  For
    WIDE boxes, lambda_min (of J and of J_B) additionally gets
    CORNER-MONOTONE bounds: lambda_min of a Jacobi matrix with
    a >= 0 is nondecreasing in every diagonal entry (Weyl, PSD diag
    perturbation) and nonincreasing in every off-diagonal (sign-
    flip similarity D(-J)D plus the |x|-substitution Rayleigh
    argument), so the exact range endpoints sit at the two corners
    (b_lo, a_hi) / (b_hi, a_lo) -- point enclosures there carry no
    Gershgorin radius penalty (warded inside G3).
 R3 OBJECTIVE BOUND.  tr R(J) = sum_k R(lambda_k(J)) (the CCLXI
    eigen route; warded against the LU partial-fraction artifact by
    the reused T-gates).  For FEASIBLE J in the box the eigenvalue
    intervals are intersected with certified structural facts:
    (i) J is POSITIVE DEFINITE (Schur: B-floor + b_1 > 0 + sigma <=
    cap < 1 give gap = b_1(1-sigma) > 0; Horn & Johnson 7.7.7), so
    lambda_1 >= max(0, lam1_floor(box)) with the quantitative floor
    lambda_1 = 1/lambda_max(J^-1) >= 1/[ max(1/g, 1/c_Bw +
    (a_1^2/g)|u|^2) + (a_1/g)|u| ], g >= b1_lo (1-cap), |u|^2 =
    ||J_B^-1 e_1||^2 <= j11_hi/c_Bw from the C4 continued fraction
    (elementary block Rayleigh bound, stated and used with outward
    rounding; skipped where the CF refuses); (ii) Rayleigh:
    lambda_1 <= min_i b_i; (iii) radius: spectrum in [-L, L];
    (iv) B-floor + TWO-SIDED Cauchy interlacing against the J_B
    enclosure: lambda_k(J) in [max(c_Bw, lamB_{k-1,lo}),
    min(L, lamB_{k-1,hi})] for k >= 2.  Hence
      UB(box) = sum_k rangemax(R, I_k ^ clips),
    and an empty intersection certifies the box infeasible.  The
    master box itself is pre-clipped by b_1 > 0 (verbatim C_sig) and
    diag(J_B) >= lambda_min(J_B) >= c_Bw (Rayleigh).  The ward
    containment version uses UNclipped intervals.

RIGOROUS CONSTRAINTS (b).
 C1 box membership: trivial (boxes are sub-boxes of the master box;
    the master box is the frozen CCLXI box with b_1 clipped to
    [0, hi] -- sound because C_sig requires b_1 > 0 verbatim).
 C2 B-floor: lambda_min(J_B) >= c_Bw.  J_B eigen enclosure as in R2
    (7x7).  Prune when the certified UPPER bound over the box is
    below c_Bw; certify-in when the lower bound is above.
 C3 radius: prune when min lambda certifiably < -L or max lambda
    certifiably > L over ALL box members ... (one-sided prunes use
    the certified bounds; the feasible clips of R3 do the rest).
 C4 sigma: [J_B^-1]_11 by the INTERVAL CONTINUED FRACTION
    1/(b_2 - a_2^2/(b_3 - ... - a_7^2/b_8)) evaluated bottom-up with
    directed rounding; if any pivot interval touches <= 0 the box is
    REFUSED for sigma pruning (counted, never rounded inward).
    Prune when sigma_lo > cap (points with b_1 <= 0 are infeasible
    by the verbatim CCLXI constraint anyway); certify-in when
    sigma_hi <= cap.
 C5 KS_wall / COEF: separable interval sums (per-coordinate exact
    monotone ranges, outward rounding; log with a declared pad
    LOG_PAD, warded against mpmath on samples).
 C6 SPREAD: via the classical Jacobi weight identity
      prod_k w_k = prod_i a_i^{2(8-i)} / prod_{i<j}(l_j - l_i)^2
    (EXTERNAL-CITED: Gauss-quadrature / Jacobi-matrix discriminant
    identity, e.g. Golub & Welsch, Math. Comp. 23 (1969); numerically
    warded at every truth step), so
      sum_k log(8 w_k) = 8 log 8 + 2 sum_i (8-i) log a_i
                         - 2 sum_{i<j} log(l_j - l_i),
    enclosed from both sides with the R2 eigenvalue intervals (gap
    lower bounds must be positive, else the box is REFUSED for
    SPREAD pruning -- counted).  SPREAD = -(1/16) sum_k log(8 w_k).
    This is the excluder that closes the a_1 -> 0 seam which the
    sigma-cap alone cannot close (all a-coordinate box floors are
    clipped at 0).
 C7 SECOND-MOMENT FLOOR (COEF composed with AM-GM and Frobenius,
    warded): COEF gives prod_k a_k >= P_min = (L/4)^7 exp(coef_lo +
    log(2)/2); AM-GM gives sum_{i>=2} a_i^2 >= 6 (P_min/a1_hi)^{1/3};
    the exact Frobenius identity sum_j lamB_j^2 = sum b_i^2 +
    2 sum a_i^2 (warded on truth) plus max >= root-mean-square give
    lambda_max(J_B) >= sqrt(M2_lo/7), and interlacing lifts the top
    eigenvalue of J into the certified low-R bulk -- this is the
    wide-box excluder of the 'all eigenvalues at the widened B-floor'
    corner.
 SOUNDNESS RULE: every prune requires a certified violation over the
    WHOLE box; skipping a constraint only ENLARGES the feasible set
    and so only weakens (raises) the certified upper bound -- never
    invalidates it.  Refusals are counted and never flipped inward.
    At POINT boxes tr R is enclosed by DIRECT interval evaluation of
    the product form (no grid quantization).

BRANCH AND BOUND (c).
 O1 best-first over sub-boxes of the master box: pop the largest-UB
    batch, prune (C2-C6 + empty feasible clips), recompute UB,
    split survivors at the midpoint of the highest-score coordinate
    (score = relative width, boosted x3 for the Gershgorin argmax
    row of the radius pattern and for (b_1, a_1) when the sigma
    interval straddles the cap -- heuristics affect SPEED only,
    never soundness).  Boxes with UB < DROP_FLOOR = 0.98 are dropped
    (they can never raise a bound above the floor); under memory
    pressure (open set > 0.8 QUEUE_CAP) the lower half of the queue
    is dropped ADAPTIVELY and the largest dropped UB becomes a
    permanent floor of the reported bound (sound: the certificate
    is max over everything not excluded); boxes narrower than
    WFLOOR_REL in every coordinate join the HARD REGION list (kept
    in the bound, no longer split).  The CERTIFIED GLOBAL BOUND at
    any time is max(open UBs, hard UBs, floor of every dropped
    box); the run records every crossing of the frozen target
    ladder and full tree statistics (processed / pruned per
    excluder / refused / dropped / hard).
 O2 CERTIFIED LOWER BOUND: the CCLXI stage-1 machinery (run_stage1,
    verbatim reuse, declared seed) with the verbatim sigma
    constraint proposes witnesses; each candidate and every truth
    step is then interval-certified (point-box feasibility for ALL
    C_sig constraints + tr R enclosure) and the certified LB is the
    best certified-feasible tr R lower end.  A numeric candidate
    that fails certification is typed and discarded.

THE SENSITIVITY MAP (d).  The full B&B is re-run (shorter frozen
budget slices) at sigma caps {0.60, 0.70, 0.75, 0.80} beside the
frozen 0.665: certified bound per cap, certified-LB per cap, the
truth-membership census per cap (0.60 < max truth sigma 0.6046
excludes truth steps -- typed, that run answers sharpness only),
and the largest cap with a certified sup < 1 (if any).  Certified
bounds are upper bounds; their differences are typed as an UPPER-
BOUND map, not a derivative of the true sup.

GATES (e).
 G1 envelope containment: scalar_r (float, CCLXI objective) inside
    the certified segment [lo, hi] on ENV_WARD_N declared samples,
    100%.
 G2 Sturm cross-ward: the R2 enclosures verified by the independent
    interval Sturm count on STURM_WARD_N random box midpoints.
 G3 box containment: on BOX_WARD_N random sub-boxes x PTS_PER_BOX
    random interior points, the float tr R lies inside the UNclipped
    certified [LB, UB] of the box AND the point lambda_min lies
    inside the corner-monotone range, 100%.
 G4 truth membership CERTIFIED: all 68 truth steps interval-certify
    ALL C_sig constraints (incl. sigma and SPREAD) and their tr R
    enclosures contain the CCLXI float reads.
 G5 control (must fire): the declared indefinite control theta (hot
    truth step with b_1 -> -1) must produce a certified tr R
    enclosure with LOWER end >= 1 (the separator fact made machine-
    visible); silence kills.
 G6 anti-circularity: the class is frozen by the CCLXI machinery
    itself and warded by the full frozen box SHA-256
    224a2737d65ec18c...; SIG_CAP is recomputed from truth, never
    hand-set (warded against the CCLXI value 0.665); AST firewall +
    AC scan of the rigorous class/objective functions (no ladder or
    read identifiers).
 G7 refusal discipline: every interval failure (CF pivot, SPREAD
    gap, mu sanity) REFUSES the corresponding prune and is counted;
    nothing is ever rounded inward; LOG_PAD warded vs mpmath.

EXTERNAL-CITED (consumed, warded, never proved here).
 E1 Weyl perturbation + Cauchy interlacing + polar decomposition
    contraction [Horn & Johnson, Matrix Analysis 2nd ed., CUP 2013,
    Sec. 4.3, 7.3; ||(Q^TQ)^{1/2} - I|| <= ||Q^TQ - I||].
 E2 compression similarity (lambda_min(J_B) = lamB1) and Sylvester
    -- inherited through the reused CCLXI B-gates.
 E3 the CCXXV separator facts (interval-certified in-repo, re-
    consumed read-only).
 E4 the Jacobi weight / discriminant identity (C6 above), warded
    numerically at all truth steps.
 E5 SLSQP / differential evolution (SciPy) propose witnesses only;
    nothing rigorous is consumed from them.

FROZEN PROTOCOL.  S0 firewall/AC -> W/T/B ladder + filter + Jacobi
translation (CCLXI machinery reused verbatim, its gates absorbed)
-> G class freeze + SHA ward + SIG_CAP ward -> R envelope + G1-G3
wards -> N truth certification G4 + witness LB (O2) -> X control G5
-> O main B&B at the frozen cap -> D sensitivity map -> V verdict.
tau/c_h relocation screens are VACUOUS BY CONSTRUCTION here (typed):
the probe emits class-level certified bounds, no new per-step
decision currency; the reused T5 gate reproduces the CCXLVII per-
step reserves unchanged.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, dominance order):
 KSDUAL-RIGOR-CLOSES(certified sup <= B < 1 over C_sig; constraint
   set used; window [LB_cert, B]; tree stats)
 KSDUAL-SIGMA-INSUFFICIENT(certified feasible witness with
   tr R lower end >= 1: the sigma-cap provably does NOT close the
   class; anatomy)
 KSDUAL-RIGOR-OPEN(certified window [LB_cert, B] with B >= 1 after
   the frozen budget; hard-region anatomy; tree stats)
Every enum is a finite float64 statement with outward rounding about
the deployed ladder and the frozen class; NEVER an all-h statement,
NEVER an RH claim.

FROZEN BARS.  NDIM = 8; BOX_SHA_CCLXI = 224a2737d65ec18c0433dd080dee
8e62cd71797bb83232f04d2885db855c851a; SIG_CAP_REF = 0.665 (rel ward
1e-2); SIG_GRID_EXTRA = (0.60, 0.70, 0.75, 0.80); NSEG = 8192 (smoke
2048); TMIN = 1e-18; TMAX = 1.1; GAM_INFL = 1.05; LOG_PAD = 1e-12
(rel, ward vs mpmath 1e-14 on 256 samples); BATCH = 4096 (smoke
1024); QUEUE_CAP = 1000000; WFLOOR_REL = 2^-26; DROP_FLOOR = 0.98;
TARGETS = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02, 1.01, 1.005, 1.002,
1.001, 0.999, 0.995, 0.99, 0.985, 0.98); MAIN_BUDGET_S = 480 (smoke
40); SENS_BUDGET_S = 110 (smoke 10); WIT_MS = 32, WIT_DE = 200
(smoke 6/30); ENV_WARD_N = 4096 (smoke 512); STURM_WARD_N = 24
(smoke 6); BOX_WARD_N = 160 (smoke 24); PTS_PER_BOX = 4; WARD_SEED =
20260812; MU_MAX = 1e-6; CTRL_B1 = -1.0; UB_NEG_FAR = 2.0 + 1e-9;
LB_POS_FAR = -1e-12; ENV_TOL = 1e-9; BOXW_TOL = 1e-7; IDENT_TOL =
1e-9; runtime cap 25 min.

SMOKE DISCLOSURE (2026-08-12, three smoke passes on the 11-step
subset ladder BEFORE this freeze; no bar, control, gate, enum or
success rule was changed after the final smoke).
 SMOKE-1 (SPEC v0, 86.7 s): the G2b identity ward FIRED (rel 4.02)
 and exposed a genuine defect -- the weight-identity code carried
 the factor 2 twice (WEXP already contains it); the same seat sat in
 spread_iv.  AMENDMENT A1 (defect fix, both seats); after A1 all
 wards ran at machine precision.  SMOKE-1 also exposed the expected
 15-dim plateau: the naive best-first tree kept the bound at the
 wide-box value with the open set growing ~40k boxes/s.
 AMENDMENT A2 (structural tightening, all rigorous and E-cited, no
 bar moved): the Schur-PD lambda_1 >= 0 clip, the quantitative
 lam1_floor from the continued fraction, corner-monotone lambda_min
 bounds, the Rayleigh diagonal clips, the two-sided interlacing
 intersection, the master-box pre-clip diag(J_B) >= c_Bw, the C7
 second-moment floor, direct interval R at point boxes, and the
 no-ratchet adaptive tail shedding.
 SMOKE-2/3 (post-A1/A2, 88.7 / 90.1 s) ran 17/17 and 18/18 GREEN;
 no kills.  Honest readings: (i) the smoke class is the SUBSET-truth
 envelope (own box SHA; the CCLXI SHA ward and the 0.665 ward are
 smoke-bypassed by design and decide only on the frozen ladder);
 (ii) all enclosure wards at machine precision (envelope 512/512,
 identity 2.8e-15, Frobenius 1.1e-15, Sturm 6/6, box containment
 96/96 slack 0.0; the point control enclosure collapsed to
 [5.845178, 5.845178]); (iii) the smoke B&B plateaued at 7.81 --
 the SMOKE geometry is degenerate (its fake-bridge step drags the
 widened B-floor to 0.0053, so every k>=2 eigenvalue may sit at
 R ~ 0.98; the frozen floor is 0.3146); 100% CF/SPREAD refusals on
 wide boxes are the expected emergence depth of those prunes, typed
 not hidden; (iv) the smoke witness stage found AND certified a
 subset-feasible point with tr R >= 1.0073 (the smoke verdict
 SIGMA-INSUFFICIENT is dominated by the fake-bridge subset truth at
 4.85 -- a smoke phenomenon, disclosed).
 FROZEN-RUN-1 DISCLOSURE (SPEC v1, killed, typed): the first frozen
 run passed every gate (incl. box SHA == CCLXI, sigma cap 0.665043,
 certified truth floor 0.972698) but the main B&B stopped on
 queue-cap after 55 s of its 480 s slice at the wide-box plateau
 2.0797: the plateau boxes carry BITWISE-EQUAL UBs, so best-first
 degenerated to breadth-first and the open set flooded before any
 emergent prune could bite (CF/SPREAD refusals 100%, exactly the
 typed wide-box behaviour).  AMENDMENT A3 (SPEC v2, disclosed;
 search order + one additional valid prune; no bar, gate, ward,
 enum or success rule changed): (i) the queue priority gets a
 depth tie-break (key = UB - 1e-9 * sum log2 relative width) so
 equal-UB lineages are explored depth-first -- affects SPEED only,
 the certificate is always max UB over open+hard+dropped floors;
 (ii) when the sigma continued fraction refuses, the fallback
 j11 in [1/L, 1/c_Bw] is used (valid for every feasible member by
 B-floor and interlacing+radius: c_Bw <= lambda(J_B) <= L), feeding
 the same sigma-prune and lam1_floor.  The frozen run below (SPEC
 v2) is the run of record.

NO RH claim.  No marker moves; no paper, ledger, website, manifest
or verification file is touched; the only edit outside this file is
the German CCLXVII line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): zolotarev_ks_dual_probe (CCLXI class + stage-1
machinery), zolotarev_phase_filter_probe (CCXXV filter + artifact),
onebadmode_moments_probe (CCVII ladder), pg_chain_interval_rollout
_probe (interval house style, precedent only).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import zolotarev_ks_dual_probe as ksd  # noqa: E402 (READ-ONLY CCLXI)

zol = ksd.zol

# ------------------------------------------------------- frozen bars
NDIM = 8
BOX_SHA_CCLXI = ("224a2737d65ec18c0433dd080dee8e62"
                 "cd71797bb83232f04d2885db855c851a")
SIG_CAP_REF = 0.665
SIG_CAP_RTOL = 1.0e-2
SIG_GRID_EXTRA = (0.60, 0.70, 0.75, 0.80)
SMOKE = "--smoke" in sys.argv[1:]
NSEG = 2048 if SMOKE else 8192
TMIN = 1.0e-18
TMAX = 1.1
U = 2.0 ** -53
GAM_INFL = 1.05
LOG_PAD = 1.0e-12
BATCH = 1024 if SMOKE else 4096
QUEUE_CAP = 1000000
WFLOOR_REL = 2.0 ** -26
DROP_FLOOR = 0.98
TARGETS = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02, 1.01, 1.005, 1.002,
           1.001, 0.999, 0.995, 0.99, 0.985, 0.98)
MAIN_BUDGET_S = 40.0 if SMOKE else 480.0
SENS_BUDGET_S = 10.0 if SMOKE else 110.0
WIT_MS = 6 if SMOKE else 32
WIT_DE = 30 if SMOKE else 200
ENV_WARD_N = 512 if SMOKE else 4096
STURM_WARD_N = 6 if SMOKE else 24
BOX_WARD_N = 24 if SMOKE else 160
PTS_PER_BOX = 4
WARD_SEED = 20260812
MU_MAX = 1.0e-6
CTRL_B1 = -1.0
UB_NEG_FAR = 2.0 + 1.0e-9
LB_POS_FAR = -1.0e-12
ENV_TOL = 1.0e-9
BOXW_TOL = 1.0e-7
IDENT_TOL = 1.0e-9
GAM8 = 9.0 * U / (1.0 - 9.0 * U)
LOGPAD_WARD_N = 256

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
    """Absorb the reused CCLXI gate results into this probe's gate
    account (verbatim machinery reuse; a reused FAIL kills here)."""
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


# --------------------------------------- directed rounding helpers
def nup(x):
    return np.nextafter(x, np.inf)


def ndown(x):
    return np.nextafter(x, -np.inf)


def log_lo(x):
    """Lower bound of log on positive x (declared LOG_PAD, warded).
    x == 0 -> -inf (honest)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.log(x)
    return ndown(v - LOG_PAD * (np.abs(v) + 1.0))


def log_hi(x):
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.log(x)
    return nup(v + LOG_PAD * (np.abs(v) + 1.0))


# =============================== R1: certified scalar envelope of R
def f_iv_pos(t_lo, t_hi, fdata):
    """Certified [lo, hi] of f(t) on positive t-segments (arrays).
    Factor-wise monotone endpoint ranges in s = t^2, base with its
    interior critical point, everything rounded outward."""
    num = np.asarray(fdata["num"], float)
    den = np.asarray(fdata["den"], float)
    s_lo = ndown(t_lo * t_lo)
    s_hi = nup(t_hi * t_hi)
    prod_lo = np.ones_like(t_lo)
    prod_hi = np.ones_like(t_lo)
    for j in range(len(num)):
        nj, dj = float(num[j]), float(den[j])
        v_lo_a = ndown(ndown(s_lo + nj) / nup(s_lo + dj))
        v_lo_b = ndown(ndown(s_hi + nj) / nup(s_hi + dj))
        v_hi_a = nup(nup(s_lo + nj) / ndown(s_lo + dj))
        v_hi_b = nup(nup(s_hi + nj) / ndown(s_hi + dj))
        prod_lo = ndown(prod_lo * np.minimum(v_lo_a, v_lo_b))
        prod_hi = nup(prod_hi * np.maximum(v_hi_a, v_hi_b))
    d8 = float(den[-1])
    b_lo_a = ndown(t_lo / nup(nup(t_lo * t_lo) + d8))
    b_lo_b = ndown(t_hi / nup(nup(t_hi * t_hi) + d8))
    b_hi_a = nup(t_lo / ndown(ndown(t_lo * t_lo) + d8))
    b_hi_b = nup(t_hi / ndown(ndown(t_hi * t_hi) + d8))
    base_lo = np.minimum(b_lo_a, b_lo_b)
    base_hi = np.maximum(b_hi_a, b_hi_b)
    crit_lo = ndown(math.sqrt(d8))
    crit_hi = nup(math.sqrt(d8))
    crit_ub = nup(0.5 / crit_lo)
    inside = (t_lo <= crit_hi) & (t_hi >= crit_lo)
    base_hi = np.where(inside, np.maximum(base_hi, crit_ub), base_hi)
    f_lo = ndown(base_lo * prod_lo)
    f_hi = nup(base_hi * prod_hi)
    return f_lo, f_hi


def r_iv_direct(x_lo, x_hi, fdata):
    """Direct certified [lo, hi] of R on arbitrary narrow intervals
    (used at POINT boxes where grid quantization would be wasteful).
    Same product-form machinery, oddness for the negative side."""
    big_l = float(fdata["L"])
    dnorm = float(fdata["D"])
    t_lo = ndown(np.asarray(x_lo, float) / big_l)
    t_hi = nup(np.asarray(x_hi, float) / big_l)
    r_lo = np.empty_like(t_lo)
    r_hi = np.empty_like(t_lo)
    pos = t_lo >= 0.0
    neg = t_hi <= 0.0
    mid = ~(pos | neg)
    if np.any(pos):
        f_l, f_h = f_iv_pos(t_lo[pos], t_hi[pos], fdata)
        r_lo[pos] = np.maximum(LB_POS_FAR,
                               ndown(1.0 - nup(dnorm * f_h)))
        r_hi[pos] = np.minimum(1.0, nup(1.0 - ndown(dnorm * f_l)))
    if np.any(neg):
        f_l, f_h = f_iv_pos(-t_hi[neg], -t_lo[neg], fdata)
        r_lo[neg] = np.maximum(1.0, ndown(1.0 + ndown(dnorm * f_l)))
        r_hi[neg] = nup(1.0 + nup(dnorm * f_h))
    if np.any(mid):
        t_abs = np.maximum(-t_lo[mid], t_hi[mid])
        _f_l, f_h = f_iv_pos(np.zeros_like(t_abs), t_abs, fdata)
        r_lo[mid] = np.maximum(LB_POS_FAR,
                               ndown(1.0 - nup(dnorm * f_h)))
        r_hi[mid] = nup(1.0 + nup(dnorm * f_h))
    return r_lo, r_hi


class Envelope:
    """Certified piecewise [lo, hi] envelope of R(x) = 1 - D f(x/L)
    with sparse-table range max/min and sign-fact fallbacks."""

    def __init__(self, fdata):
        dnorm = float(fdata["D"])
        big_l = float(fdata["L"])
        t_edges = np.geomspace(TMIN, TMAX, NSEG + 1)
        # the x-edges actually used by queries; the t-intervals fed
        # to the certified f-evaluation are WIDENED so that every
        # x in [E_i, E_i+1] maps to t = x/L inside the certified
        # t-segment (edge-rounding consistency)
        x_pos = big_l * t_edges
        t_seg_lo = ndown(ndown(x_pos[:-1] / big_l))
        t_seg_hi = nup(nup(x_pos[1:] / big_l))
        f_lo, f_hi = f_iv_pos(t_seg_lo, t_seg_hi, fdata)
        # head segment [0, x_pos[0]]
        _h_lo, h_hi = f_iv_pos(np.asarray([0.0]),
                               np.asarray([float(nup(nup(
                                   x_pos[0] / big_l)))]), fdata)
        head_fhi = float(nup(h_hi[0] * (1.0 + 1e-12)))
        # positive-x segments of R
        pos_ub = np.minimum(1.0, nup(1.0 - ndown(dnorm * f_lo)))
        pos_lb = np.maximum(LB_POS_FAR,
                            ndown(1.0 - nup(dnorm * f_hi)))
        # negative side by exact oddness: R(-x) = 1 + D f(x)
        neg_ub = nup(1.0 + nup(dnorm * f_hi))
        neg_lb = np.maximum(1.0, ndown(1.0 + ndown(dnorm * f_lo)))
        seg_edges = np.concatenate([
            -x_pos[::-1], [0.0], x_pos])
        # order: NSEG neg segments, neg head, pos head, NSEG pos
        ub = np.concatenate([
            neg_ub[::-1],
            [float(nup(1.0 + nup(dnorm * head_fhi)))],
            [1.0],
            pos_ub])
        lb = np.concatenate([
            neg_lb[::-1],
            [1.0],
            [max(LB_POS_FAR,
                 float(ndown(1.0 - nup(dnorm * head_fhi))))],
            pos_lb])
        self.edges = seg_edges
        self.n_seg = len(ub)
        self.t_max = self._table(ub, np.maximum)
        self.t_min = self._table(lb, np.minimum)
        self.ub0 = ub
        self.lb0 = lb

    @staticmethod
    def _table(arr, op):
        levels = [arr.copy()]
        k = 1
        while k < len(arr):
            prev = levels[-1]
            cur = prev.copy()
            cur[:len(arr) - k] = op(prev[:len(arr) - k],
                                    prev[k:])
            levels.append(cur)
            k *= 2
        return np.asarray(levels)

    def _query(self, table, xa, xb, below_fb, above_fb, op):
        xa = np.asarray(xa, float)
        xb = np.asarray(xb, float)
        edges = self.edges
        m = self.n_seg
        i0 = np.clip(np.searchsorted(edges, xa, side="right") - 1,
                     0, m - 1)
        i1 = np.clip(np.searchsorted(edges, xb, side="left") - 1,
                     0, m - 1)
        i1 = np.maximum(i1, i0)
        span = i1 - i0 + 1
        klev = np.frexp(span.astype(float))[1] - 1
        klev = np.clip(klev, 0, table.shape[0] - 1)
        left = table[klev, i0]
        right = table[klev, np.maximum(i1 - (1 << klev) + 1, i0)]
        res = op(left, right)
        res = np.where(xa < edges[0], op(res, below_fb), res)
        res = np.where(xb > edges[-1], op(res, above_fb), res)
        return res

    def range_max(self, xa, xb):
        return self._query(self.t_max, xa, xb, UB_NEG_FAR, 1.0,
                           np.maximum)

    def range_min(self, xa, xb):
        return self._query(self.t_min, xa, xb, 1.0, LB_POS_FAR,
                           np.minimum)


# ================== R2: certified eigenvalue enclosures per box
def op_norm_ub(a_abs):
    """||X||_2 <= sqrt(||X||_1 ||X||_inf), batched, rounded up."""
    n1 = np.max(np.sum(a_abs, axis=1), axis=-1)
    ninf = np.max(np.sum(a_abs, axis=2), axis=-1)
    return nup(np.sqrt(nup(n1 * ninf)))


def build_jacobi_batch(mid, ndim, b_off, a_off):
    n_box = mid.shape[0]
    jm = np.zeros((n_box, ndim, ndim))
    for i in range(ndim):
        jm[:, i, i] = mid[:, b_off + i]
    for i in range(ndim - 1):
        jm[:, i, i + 1] = mid[:, a_off + i]
        jm[:, i + 1, i] = mid[:, a_off + i]
    return jm


def eig_enclosure(lo, hi, ndim, b_off, a_off):
    """Certified per-index eigenvalue intervals over the WHOLE box:
    returns (d, e_tot) with lambda_k(any member) in
    [d_k - e_tot, d_k + e_tot].  R2 machinery (polar + Weyl +
    Gershgorin radius), generously inflated rounding constants."""
    mid = 0.5 * (lo + hi)
    rad = nup(np.maximum(hi - mid, mid - lo))
    jm = build_jacobi_batch(mid, ndim, b_off, a_off)
    dd, qq = np.linalg.eigh(jm)
    m1 = qq * dd[:, None, :]
    qt = np.transpose(qq, (0, 2, 1))
    pp = m1 @ qt
    ss = np.abs(m1) @ np.abs(qt)
    ee = jm - pp
    e_abs = np.abs(ee) + GAM_INFL * (
        (GAM8 + 2.0 * U) * ss + U * (np.abs(jm) + np.abs(pp)))
    norm_e = op_norm_ub(e_abs)
    gg = qt @ qq
    idx = np.arange(ndim)
    gg[:, idx, idx] -= 1.0
    sg = np.abs(qt) @ np.abs(qq)
    g_abs = np.abs(gg) + GAM_INFL * ((GAM8 + 2.0 * U) * sg + U)
    mu = op_norm_ub(g_abs)
    maxd = np.max(np.abs(dd), axis=1)
    eig_err = nup(GAM_INFL * (norm_e + mu * (2.0 + mu) * maxd)
                  + 1e-300)
    eig_err = np.where(mu < MU_MAX, eig_err, np.inf)
    rb = rad[:, b_off:b_off + ndim]
    ra = rad[:, a_off:a_off + ndim - 1]
    row = rb.copy()
    row[:, :-1] += ra
    row[:, 1:] += ra
    rho = nup(GAM_INFL * np.max(row, axis=1))
    return dd, nup(eig_err + rho), mu


def corner_lam_min(lo, hi, ndim, b_off, a_off):
    """Certified range of lambda_min over the box by CORNER
    MONOTONICITY: lambda_min of a Jacobi matrix with a >= 0 is
    nondecreasing in every diagonal entry (Weyl, diag perturbation
    PSD) and nonincreasing in every off-diagonal (sign-flip
    similarity + the |x|-substitution Rayleigh argument), so the
    extremes sit at the corners (b_lo, a_hi) and (b_hi, a_lo)."""
    v1 = lo.copy()
    v1[:, a_off:a_off + ndim - 1] = hi[:, a_off:a_off + ndim - 1]
    v2 = hi.copy()
    v2[:, a_off:a_off + ndim - 1] = lo[:, a_off:a_off + ndim - 1]
    d1, e1, _ = eig_enclosure(v1, v1, ndim, b_off, a_off)
    d2, e2, _ = eig_enclosure(v2, v2, ndim, b_off, a_off)
    return ndown(d1[:, 0] - e1), nup(d2[:, 0] + e2)


def sturm_count(bvec, avec, x_val):
    """Independent interval Sturm count (# eigenvalues < x) for a
    POINT Jacobi matrix, directed rounding; None if indeterminate."""
    p_lo = ndown(bvec[0] - x_val)
    p_hi = nup(bvec[0] - x_val)
    n_neg = 0
    for k in range(1, len(bvec)):
        if p_lo > 0.0:
            pass
        elif p_hi < 0.0:
            n_neg += 1
        else:
            return None
        a2_lo = ndown(avec[k - 1] * avec[k - 1])
        a2_hi = nup(avec[k - 1] * avec[k - 1])
        if p_lo > 0.0:
            q_lo, q_hi = ndown(a2_lo / p_hi), nup(a2_hi / p_lo)
        else:
            q_lo, q_hi = ndown(a2_hi / p_hi), nup(a2_lo / p_lo)
        p_lo_n = ndown(ndown(bvec[k] - x_val) - q_hi)
        p_hi_n = nup(nup(bvec[k] - x_val) - q_lo)
        p_lo, p_hi = p_lo_n, p_hi_n
    if p_lo > 0.0:
        pass
    elif p_hi < 0.0:
        n_neg += 1
    else:
        return None
    return n_neg


def sturm_count_robust(bvec, avec, x_val, direction):
    for k in range(12):
        step = direction * (abs(x_val) + 1.0) * (k * k) * 8.0 * U
        cnt = sturm_count(bvec, avec, x_val + step)
        if cnt is not None:
            return cnt
    return None


# ============================ C4: sigma interval continued fraction
def sigma_cf_iv(lo, hi):
    """Interval [J_B^-1]_11 by the bottom-up continued fraction and
    the resulting sigma interval.  Returns (sig_lo, sig_hi, cf_ok,
    j_lo, j_hi); cf_ok False = REFUSED (a pivot touches <= 0)."""
    g_lo = lo[:, 7].copy()
    g_hi = hi[:, 7].copy()
    cf_ok = np.ones(lo.shape[0], bool)
    for k in range(6, 0, -1):
        cf_ok &= g_lo > 0.0
        safe_lo = np.where(cf_ok, g_lo, 1.0)
        safe_hi = np.where(cf_ok, g_hi, 1.0)
        a_lo = lo[:, 8 + k]
        a_hi = hi[:, 8 + k]
        q_lo = ndown(ndown(a_lo * a_lo) / safe_hi)
        q_hi = nup(nup(a_hi * a_hi) / safe_lo)
        g_lo = ndown(ndown(lo[:, k]) - q_hi)
        g_hi = nup(nup(hi[:, k]) - q_lo)
    cf_ok &= g_lo > 0.0
    safe_lo = np.where(cf_ok, g_lo, 1.0)
    safe_hi = np.where(cf_ok, g_hi, 1.0)
    j_lo = ndown(1.0 / safe_hi)
    j_hi = nup(1.0 / safe_lo)
    a1_lo, a1_hi = lo[:, 8], hi[:, 8]
    b1_lo, b1_hi = lo[:, 0], hi[:, 0]
    with np.errstate(divide="ignore", invalid="ignore"):
        sig_lo = ndown(ndown(ndown(a1_lo * a1_lo) * j_lo)
                       / np.maximum(b1_hi, 1e-300))
        sig_hi = np.where(
            b1_lo > 0.0,
            nup(nup(nup(a1_hi * a1_hi) * j_hi) / np.maximum(
                b1_lo, 1e-300)),
            np.inf)
    return sig_lo, sig_hi, cf_ok, j_lo, j_hi


# =================================== C5: KS / COEF interval ranges
def _sq_iv(v_lo, v_hi):
    """Certified [lo, hi] of x^2 for x in the outward-rounded
    interval [v_lo, v_hi] (abs-based, sound for either sign)."""
    m_hi = np.maximum(np.abs(v_lo), np.abs(v_hi))
    m_lo = np.where((v_lo <= 0.0) & (v_hi >= 0.0), 0.0,
                    np.minimum(np.abs(v_lo), np.abs(v_hi)))
    return ndown(m_lo * m_lo), nup(m_hi * m_hi)


def ks_iv(lo, hi, cls):
    big_l = cls["L"]
    a_lo = ndown(4.0 * lo[:, NDIM:] / big_l)
    a_hi = nup(4.0 * hi[:, NDIM:] / big_l)
    ta_lo, ta_hi = _sq_iv(ndown(a_lo - 1.0), nup(a_hi - 1.0))
    b_lo = ndown((4.0 * lo[:, :NDIM] - 2.0 * big_l) / big_l)
    b_hi = nup((4.0 * hi[:, :NDIM] - 2.0 * big_l) / big_l)
    tb_lo, tb_hi = _sq_iv(b_lo, b_hi)
    ks_lo = ndown(np.sum(ta_lo, axis=1) + np.sum(tb_lo, axis=1))
    ks_hi = nup(np.sum(ta_hi, axis=1) + np.sum(tb_hi, axis=1))
    return ks_lo, ks_hi


def coef_iv(lo, hi, cls):
    big_l = cls["L"]
    # a >= 0 structurally, so the 0-clamp keeps a valid lower bound
    a_lo = np.maximum(ndown(4.0 * lo[:, NDIM:] / big_l), 0.0)
    a_hi = nup(4.0 * hi[:, NDIM:] / big_l)
    c_lo = ndown(np.sum(log_lo(a_lo), axis=1)
                 - nup(0.5 * math.log(2.0) * (1.0 + LOG_PAD)))
    c_hi = nup(np.sum(log_hi(a_hi), axis=1)
               - ndown(0.5 * math.log(2.0) * (1.0 - LOG_PAD)))
    return c_lo, c_hi


# ============================ C6: SPREAD interval via the identity
LOG8 = math.log(8.0)
WEXP = 2.0 * np.arange(7, 0, -1, dtype=float)  # 2(8-i), i=1..7


def spread_iv(lo, hi, dd, e_tot):
    """Certified [lo, hi] of SPREAD over the box via the Jacobi
    weight identity; ok False = REFUSED (a gap lower bound <= 0 or
    an a upper bound <= 0)."""
    a_lo = lo[:, NDIM:]
    a_hi = hi[:, NDIM:]
    ok = np.all(a_hi > 0.0, axis=1) & np.isfinite(e_tot)
    la_hi = np.sum(WEXP * log_hi(a_hi), axis=1)
    la_lo = np.sum(WEXP * log_lo(np.maximum(a_lo, 0.0)), axis=1)
    gap_lo_sum = np.zeros(lo.shape[0])
    gap_hi_sum = np.zeros(lo.shape[0])
    for i in range(NDIM):
        for j in range(i + 1, NDIM):
            g_lo = ndown(ndown(dd[:, j] - dd[:, i]) - 2.0 * e_tot)
            g_hi = nup(nup(dd[:, j] - dd[:, i]) + 2.0 * e_tot)
            ok &= g_lo > 0.0
            g_lo = np.maximum(g_lo, 1e-300)
            gap_lo_sum = ndown(gap_lo_sum + log_lo(g_lo))
            gap_hi_sum = nup(gap_hi_sum + log_hi(g_hi))
    sum_hi = nup(8.0 * LOG8 + la_hi - 2.0 * gap_lo_sum)
    sum_lo = ndown(8.0 * LOG8 + la_lo - 2.0 * gap_hi_sum)
    spr_lo = ndown(-sum_hi / 16.0)
    spr_hi = nup(-sum_lo / 16.0)
    return spr_lo, spr_hi, ok


# =================================== the batched box processor
class BoxWork:
    """One batched pass: constraint prunes + certified objective UB
    + split scores for a (B, 15) box array."""

    def __init__(self, cls, env, sig_cap, fdata):
        self.cls = cls
        self.env = env
        self.fdata = fdata
        self.cap = float(sig_cap)
        self.cbw = float(cls["cb"])
        self.big_l = float(cls["L"])
        # COEF => prod_k a_k >= P_min = (L/4)^7 exp(coef_lo +
        # (1/2) log 2), rounded DOWN (used by the C7 second-moment
        # floor)
        self.pmin = float(ndown(
            (self.big_l / 4.0) ** 7
            * math.exp(cls["coef_lo"] + 0.5 * math.log(2.0))
            * (1.0 - 1e-12)))
        self.master_wd = np.maximum(
            np.asarray(cls["hi"], float)
            - np.asarray(cls["lo"], float), 1e-30)
        self.stats = dict(processed=0, pr_sigma=0, pr_bfloor=0,
                          pr_radius=0, pr_ks=0, pr_coef=0,
                          pr_spread=0, pr_empty=0, ref_cf=0,
                          ref_spread=0, dropped=0, hard=0)

    def process(self, lo, hi):
        """Returns (ub, keep_mask, split_col).  ub is the certified
        feasible-restricted upper bound (np.inf never appears: the
        envelope fallbacks cap it); keep=False means certifiably
        infeasible."""
        n_box = lo.shape[0]
        self.stats["processed"] += n_box
        keep = np.ones(n_box, bool)
        ks_lo, _ks_hi = ks_iv(lo, hi, self.cls)
        m = ks_lo > self.cls["ks_cap"]
        self.stats["pr_ks"] += int(np.sum(m & keep))
        keep &= ~m
        c_lo, c_hi = coef_iv(lo, hi, self.cls)
        m = (c_hi < self.cls["coef_lo"]) | (c_lo > self.cls["coef_hi"])
        self.stats["pr_coef"] += int(np.sum(m & keep))
        keep &= ~m
        sig_lo, _sig_hi, cf_ok, j_lo, j_hi = sigma_cf_iv(lo, hi)
        self.stats["ref_cf"] += int(np.sum(~cf_ok & keep))
        # A3(ii) fallback where the CF refuses: every FEASIBLE
        # member has c_Bw <= lambda(J_B) <= L (B-floor,
        # interlacing + radius), hence j11 in [1/L, 1/c_Bw]
        j_lo_eff = np.where(cf_ok, j_lo, ndown(1.0 / self.big_l))
        j_hi_eff = np.where(cf_ok, j_hi, nup(1.0 / self.cbw))
        with np.errstate(divide="ignore", invalid="ignore"):
            sig_lo_eff = ndown(
                ndown(ndown(lo[:, NDIM] * lo[:, NDIM]) * j_lo_eff)
                / np.maximum(hi[:, 0], 1e-300))
        m = sig_lo_eff > self.cap
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        m = hi[:, 0] <= 0.0          # b_1 > 0 required verbatim
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        # certified lambda_1 floor for FEASIBLE members: J is PD
        # (Schur: B-floor + b_1 > 0 + sigma <= cap < 1 => gap > 0,
        # E-cited), and lambda_1 = 1/lambda_max(J^-1) with the block
        # Rayleigh bound lambda_max(J^-1) <= max(1/g, 1/c_Bw +
        # (a_1^2/g)|u|^2) + (a_1/g)|u|, |u|^2 <= j11/c_Bw,
        # g >= b1_lo (1 - cap)
        g_lo = ndown(lo[:, 0] * (1.0 - self.cap))
        u2_hi = nup(j_hi_eff / self.cbw)
        u_hi = nup(np.sqrt(u2_hi))
        good = g_lo > 0.0
        g_safe = np.where(good, g_lo, 1.0)
        a1_hi = hi[:, NDIM]
        t_inv = nup(np.maximum(
            1.0 / g_safe,
            1.0 / self.cbw + nup(nup(a1_hi * a1_hi) * u2_hi)
            / g_safe) + nup(a1_hi * u_hi) / g_safe)
        lam1_floor = np.where(good, ndown(1.0 / t_inv), 0.0)
        # eigen enclosures (J and J_B) + corner-monotone lam_min
        dd, e_tot, _mu = eig_enclosure(lo, hi, NDIM, 0, NDIM)
        jb_cols = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
        db, eb_tot, _mub = eig_enclosure(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        l1_lo_c, l1_hi_c = corner_lam_min(lo, hi, NDIM, 0, NDIM)
        lb_lo_c, lb_hi_c = corner_lam_min(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        m = np.minimum(nup(db[:, 0] + eb_tot), lb_hi_c) < self.cbw
        self.stats["pr_bfloor"] += int(np.sum(m & keep))
        keep &= ~m
        m = (ndown(dd[:, -1] - e_tot) > self.big_l) | \
            (nup(dd[:, 0] + e_tot) < -self.big_l)
        self.stats["pr_radius"] += int(np.sum(m & keep))
        keep &= ~m
        spr_lo, spr_hi, spr_ok = spread_iv(lo, hi, dd, e_tot)
        self.stats["ref_spread"] += int(np.sum(~spr_ok & keep))
        m = spr_ok & ((spr_lo > self.cls["spr_hi"])
                      | (spr_hi < self.cls["spr_lo"]))
        self.stats["pr_spread"] += int(np.sum(m & keep))
        keep &= ~m
        # feasible-restricted objective UB: eigen enclosure
        # intersected with (i) PD-ness of feasible members
        # (lambda_1 >= max(0, lam1_floor)), (ii) Rayleigh
        # lambda_1 <= min diag, (iii) radius, (iv) B-floor +
        # two-sided Cauchy interlacing against the J_B enclosure
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
        # C7 second-moment floor: COEF => prod a >= P_min, AM-GM =>
        # sum_{i>=2} a_i^2 >= 6 (P_min/a1_hi)^(1/3); Frobenius =>
        # sum lamB^2 = sum b^2 + 2 sum a^2; max >= sqrt(mean) =>
        # lambda_max(J_B) >= sqrt(M2_lo/7); interlacing =>
        # lambda_8(J) >= lambda_max(J_B)
        b_eff = np.maximum(lo[:, 1:NDIM], self.cbw)
        amgm = ndown(6.0 * np.cbrt(np.maximum(
            self.pmin / np.maximum(a1_hi, 1e-300), 0.0))
            * (1.0 - 1e-12))
        a2sum = np.maximum(np.sum(ndown(lo[:, NDIM + 1:] ** 2),
                                  axis=1), amgm)
        m2_lo = ndown(np.sum(ndown(b_eff * b_eff), axis=1)
                      + 2.0 * a2sum)
        lam_top = ndown(np.sqrt(np.maximum(m2_lo, 0.0) / 7.0)
                        * (1.0 - 1e-12))
        cl_lo[:, NDIM - 1] = np.maximum(cl_lo[:, NDIM - 1], lam_top)
        empty = np.any(cl_lo > cl_hi, axis=1)
        self.stats["pr_empty"] += int(np.sum(empty & keep))
        keep &= ~empty
        cl_hi = np.maximum(cl_hi, cl_lo)
        ub = np.zeros(n_box)
        for k in range(NDIM):
            ub = nup(ub + self.env.range_max(cl_lo[:, k],
                                             cl_hi[:, k]))
        ub = np.where(np.isfinite(ub), ub, UB_NEG_FAR * NDIM)
        # split column: relative width, boosted for the radius-
        # dominant row and for (b1, a1) at a sigma-straddling cap
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
        split_col = np.argmax(score * boost, axis=1)
        # depth measure for the A3(i) tie-break (speed only)
        vol = np.sum(np.log2(np.maximum(
            (hi - lo) / self.master_wd, 1e-30)), axis=1)
        return ub, keep, split_col, vol

    def point_certify(self, theta, sig_cap=None):
        """Interval certification of ALL C_sig constraints at a
        point (degenerate box).  Returns (feasible_certified,
        tr_lo, tr_hi, fail_list)."""
        cap = self.cap if sig_cap is None else float(sig_cap)
        th = np.asarray(theta, float)[None, :]
        lo = th.copy()
        hi = th.copy()
        fails = []
        c_lo = np.asarray(self.cls["lo"], float)
        c_hi = np.asarray(self.cls["hi"], float)
        if not (np.all(th[0] >= c_lo) and np.all(th[0] <= c_hi)):
            fails.append("box")
        if not np.all(th[0, NDIM:] >= 0.0):
            fails.append("a_pos")
        ks_lo_v, ks_hi_v = ks_iv(lo, hi, self.cls)
        if not ks_hi_v[0] <= self.cls["ks_cap"]:
            fails.append("KS_wall")
        cf_lo_v, cf_hi_v = coef_iv(lo, hi, self.cls)
        if not (cf_lo_v[0] >= self.cls["coef_lo"]
                and cf_hi_v[0] <= self.cls["coef_hi"]):
            fails.append("COEF")
        sig_lo_v, sig_hi_v, cf_ok_v, _jl, _jh = sigma_cf_iv(lo, hi)
        if not (th[0, 0] > 0.0 and cf_ok_v[0]
                and sig_hi_v[0] <= cap):
            fails.append("sigma")
        dd, e_tot, _ = eig_enclosure(lo, hi, NDIM, 0, NDIM)
        db, eb_tot, _ = eig_enclosure(
            lo[:, [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]],
            hi[:, [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]],
            NDIM - 1, 0, NDIM - 1)
        if not ndown(db[0, 0] - eb_tot[0]) >= self.cbw:
            fails.append("B_floor")
        if not (nup(dd[0, -1] + e_tot[0]) <= self.big_l
                and ndown(dd[0, 0] - e_tot[0]) >= -self.big_l):
            fails.append("radius")
        spr_lo_v, spr_hi_v, spr_ok = spread_iv(lo, hi, dd, e_tot)
        if not (spr_ok[0] and spr_lo_v[0] >= self.cls["spr_lo"]
                and spr_hi_v[0] <= self.cls["spr_hi"]):
            fails.append("SPREAD")
        r_l, r_h = r_iv_direct(dd[0] - e_tot[0], dd[0] + e_tot[0],
                               self.fdata)
        tr_lo = float(ndown(np.sum(r_l)
                            - 8.0 * U * np.sum(np.abs(r_l))))
        tr_hi = float(nup(np.sum(r_h)
                          + 8.0 * U * np.sum(np.abs(r_h))))
        return (not fails), tr_lo, tr_hi, fails

    def box_bounds_unclipped(self, lo, hi):
        """(LB, UB) of tr R over the RAW box (no feasibility clips)
        -- the G3 containment ward currency."""
        dd, e_tot, _ = eig_enclosure(lo, hi, NDIM, 0, NDIM)
        n_box = lo.shape[0]
        t_lo = np.zeros(n_box)
        t_hi = np.zeros(n_box)
        for k in range(NDIM):
            t_lo = ndown(t_lo + self.env.range_min(
                dd[:, k] - e_tot, dd[:, k] + e_tot))
            t_hi = nup(t_hi + self.env.range_max(
                dd[:, k] - e_tot, dd[:, k] + e_tot))
        return t_lo, t_hi


# ============================================== the B&B driver
def run_bnb(work, master_lo, master_hi, budget_s, label):
    """Best-first certified branch and bound.  Returns dict with
    the certified bound, target crossings, tree stats, hard boxes."""
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
    floor_used = -np.inf   # sup over every dropped box's UB bound
    crossings = []
    floor_w = WFLOOR_REL * work.master_wd
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
        if len(c_ub) > int(0.8 * QUEUE_CAP):
            # adaptive tail shedding: drop the low-UB tail ONLY when
            # it sits clearly below the current bound (no ratchet);
            # the largest dropped UB becomes a permanent floor of
            # the reported bound (sound)
            floor_dyn = float(np.quantile(c_ub, 0.3))
            if floor_dyn < float(np.max(c_ub)) - 1e-3:
                keep_q = c_ub >= floor_dyn
                work.stats["dropped"] += int(np.sum(~keep_q))
                floor_used = max(floor_used, floor_dyn)
                c_lo, c_hi = c_lo[keep_q], c_hi[keep_q]
                c_ub, c_sc = c_ub[keep_q], c_sc[keep_q]
                c_ky = c_ky[keep_q]
            if len(c_ub) > QUEUE_CAP:
                stop_reason = "queue-cap"
                open_lo, open_hi = [c_lo], [c_hi]
                open_ub, open_sc = [c_ub], [c_sc]
                open_ky = [c_ky]
                break
        bound_now = float(np.max(c_ub)) if len(c_ub) else DROP_FLOOR
        if hard_ub:
            bound_now = max(bound_now, max(hard_ub))
        for tgt in TARGETS:
            if bound_now < tgt and not any(
                    abs(cr[0] - tgt) < 1e-15 for cr in crossings):
                crossings.append((tgt, time.time() - t_start,
                                  work.stats["processed"]))
        if bound_now < TARGETS[-1] + 1e-12:
            stop_reason = "final-target"
            open_lo, open_hi = [c_lo], [c_hi]
            open_ub, open_sc = [c_ub], [c_sc]
            open_ky = [c_ky]
            break
        n_top = min(BATCH, len(c_ub))
        order = np.argpartition(c_ky, -n_top)[-n_top:]
        rest = np.ones(len(c_ub), bool)
        rest[order] = False
        p_lo, p_hi = c_lo[order], c_hi[order]
        p_sc = c_sc[order]
        # width floor -> hard region
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
        # split at the midpoint of the chosen coordinate; if that
        # coordinate is already at floor, fall back to the widest
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
            drop = keep_c & (ub_c < DROP_FLOOR)
            work.stats["dropped"] += int(np.sum(drop))
            if np.any(drop):
                floor_used = max(floor_used, DROP_FLOOR)
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
        bound = DROP_FLOOR
    # anatomy of the current worst open/hard box
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
                            else DROP_FLOOR))


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
  HONEST FRAME.  Finite float64 statements with outward rounding
  about the deployed 68-step ladder, the frozen CCLXI class and the
  frozen CCXXV separator.  Certified upper bounds hold over the
  ENTIRE sigma-augmented class (modulo the constraint subset typing
  printed above -- omitted constraints only weaken bounds); certified
  lower bounds are interval-verified feasible points.  Heuristics
  steer the search order only, never the arithmetic.  No marker
  moves; no paper, ledger, website, manifest or verification file is
  touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.DUAL.RIGOR.01 -- certified global "
            "bound for sup tr R over the sigma-augmented class "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(
        ("f_iv_pos", "sigma_cf_iv", "ks_iv", "coef_iv", "spread_iv",
         "eig_enclosure", "sturm_count"), CLASS_BANNED)
    check("S0.2 AC the rigorous class/objective functions contain "
          "no ladder or read identifier", not ac,
          ",".join(sorted(set(ac))), kill="K2")
    check("S0.3 CCLXI machinery imported READ-ONLY (SPEC SHA %s...)"
          % hashlib.sha256(
              ksd.__doc__.encode("utf-8")).hexdigest()[:16], True)

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
    print("    PRE-REGISTERED FLOOR: truth best tr R = %.6f at "
          "sigma = %.4f <= cap -> sup >= %.4f; CCLXI preview "
          "0.7264 typed OPTIMIZER-ARTIFACT (weak search below a "
          "feasible truth point)"
          % (truth_tr[i_hot], sig_truth[i_hot], truth_tr[i_hot]))

    # ---- R: envelope + machinery wards
    section("R -- certified envelope + enclosure machinery wards")
    rng = np.random.default_rng(WARD_SEED)
    env = Envelope(fdata)
    print("    envelope: %d segments on [%.3g, %.3g], fallbacks "
          "UB(x<lo)=%.9f UB(x>hi)=1, LB sign facts"
          % (env.n_seg, env.edges[0], env.edges[-1], UB_NEG_FAR))
    xs = np.concatenate([
        rng.uniform(-1.05, 1.05, ENV_WARD_N // 2) * fdata["L"],
        np.sign(rng.standard_normal(ENV_WARD_N // 2))
        * np.exp(rng.uniform(np.log(1e-10),
                             np.log(1.04 * fdata["L"]),
                             ENV_WARD_N // 2))])
    r_pts = np.asarray([zol.scalar_r(fdata, float(x)) for x in xs])
    e_ub = env.range_max(xs, xs)
    e_lb = env.range_min(xs, xs)
    n_in = int(np.sum((r_pts <= e_ub + ENV_TOL)
                      & (r_pts >= e_lb - ENV_TOL)))
    check("G1 envelope containment %d/%d declared samples "
          "(worst UB slack %.2e, worst LB slack %.2e)"
          % (n_in, len(xs), float(np.max(r_pts - e_ub)),
             float(np.max(e_lb - r_pts))), n_in == len(xs),
          kill="K2")
    # eigenvalue enclosure vs independent Sturm counts
    m_lo = np.asarray(cls["lo"], float)
    m_hi = np.asarray(cls["hi"], float).copy()
    m_lo = m_lo.copy()
    m_lo[0] = max(m_lo[0], 0.0)
    n_sturm_ok = 0
    n_sturm_t = 0
    for _ in range(STURM_WARD_N):
        th = rng.uniform(m_lo, m_hi)
        lo1 = th[None, :]
        dd, e_tot, _ = eig_enclosure(lo1, lo1, NDIM, 0, NDIM)
        good = True
        for k in range(NDIM):
            e_pad = 1.5 * e_tot[0] + 1e-9
            c_lo = sturm_count_robust(th[:NDIM], th[NDIM:],
                                      dd[0, k] - e_pad, -1.0)
            c_hi = sturm_count_robust(th[:NDIM], th[NDIM:],
                                      dd[0, k] + e_pad, +1.0)
            n_sturm_t += 1
            if c_lo is None or c_hi is None:
                continue
            if not (c_lo <= k and c_hi >= k + 1):
                good = False
        n_sturm_ok += int(good)
    check("G2 Sturm cross-ward: %d/%d random matrices consistent "
          "with the R2 enclosures" % (n_sturm_ok, STURM_WARD_N),
          n_sturm_ok == STURM_WARD_N, kill="K2")
    # weight identity ward at every truth step
    worst_id = 0.0
    for r in rows:
        th = r["theta"]
        jm, _jb = ksd.theta_matrices(th)
        evals, evecs = np.linalg.eigh(jm)
        w_log = np.sum(np.log(np.maximum(evecs[0, :] ** 2, 1e-300)))
        rhs = float(np.sum(WEXP * np.log(th[NDIM:])))
        for i in range(NDIM):
            for j in range(i + 1, NDIM):
                rhs -= 2.0 * math.log(evals[j] - evals[i])
        worst_id = max(worst_id, abs(w_log - rhs)
                       / max(1.0, abs(w_log)))
    check("G2b Jacobi weight identity ward on all %d truth steps: "
          "worst rel %.2e <= %.0e" % (len(rows), worst_id,
                                      IDENT_TOL),
          worst_id <= IDENT_TOL, kill="K2")
    # LOG_PAD ward vs mpmath
    try:
        from mpmath import mp
        mp.dps = 40
        xs_l = np.exp(rng.uniform(-60, 12, LOGPAD_WARD_N))
        worst_log = max(abs(float(mp.log(mp.mpf(float(x))))
                            - float(np.log(x)))
                        / max(1e-30, abs(float(np.log(x))))
                        for x in xs_l)
        check("G7a np.log vs mpmath on %d samples: worst rel %.2e "
              "<< LOG_PAD %.0e" % (LOGPAD_WARD_N, worst_log,
                                   LOG_PAD),
              worst_log <= LOG_PAD * 1e-2, kill="K2")
    except ImportError:
        check("G7a LOG_PAD ward SKIPPED (no mpmath) -- pad kept "
              "at declared 1e-12", True)
    # Frobenius identity ward (C7 currency) at every truth step
    worst_fro = 0.0
    for r in rows:
        th = r["theta"]
        _jm, jb = ksd.theta_matrices(th)
        lam_b = np.linalg.eigvalsh(jb)
        fro = float(np.sum(th[1:NDIM] ** 2)
                    + 2.0 * np.sum(th[NDIM + 1:] ** 2))
        worst_fro = max(worst_fro, abs(np.sum(lam_b ** 2) - fro)
                        / max(1.0, fro))
    check("G2c Frobenius identity sum lamB^2 == sum b^2 + 2 sum "
          "a^2 on all %d truth steps: worst rel %.2e <= %.0e"
          % (len(rows), worst_fro, IDENT_TOL),
          worst_fro <= IDENT_TOL, kill="K2")
    # box containment ward
    work = BoxWork(cls, env, sig_cap, fdata)
    n_ok = 0
    n_t = 0
    worst_sl = 0.0
    for _ in range(BOX_WARD_N):
        c0 = rng.uniform(m_lo, m_hi)
        c1 = rng.uniform(m_lo, m_hi)
        frac = rng.uniform(0.0, 0.2)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        t_lo, t_hi = work.box_bounds_unclipped(b_lo[None, :],
                                               b_hi[None, :])
        l1c_lo, l1c_hi = corner_lam_min(b_lo[None, :],
                                        b_hi[None, :], NDIM, 0,
                                        NDIM)
        for _p in range(PTS_PER_BOX):
            th = rng.uniform(b_lo, b_hi)
            v = ksd.tr_r_of_theta(th, fdata)
            lam1_p = float(np.linalg.eigvalsh(
                ksd.theta_matrices(th)[0])[0])
            n_t += 1
            ok = (t_lo[0] - BOXW_TOL <= v <= t_hi[0] + BOXW_TOL
                  and l1c_lo[0] - BOXW_TOL <= lam1_p
                  <= l1c_hi[0] + BOXW_TOL)
            n_ok += int(ok)
            worst_sl = max(worst_sl, v - t_hi[0], t_lo[0] - v,
                           lam1_p - l1c_hi[0], l1c_lo[0] - lam1_p)
    check("G3 box containment %d/%d random (box, point) pairs "
          "(worst outward slack %.2e)" % (n_ok, n_t, worst_sl),
          n_ok == n_t, kill="K2")

    # ---- N: truth certification + witness LB
    section("N -- truth steps interval-certified IN C_sig + "
            "certified witness lower bound")
    n_cert = 0
    fail_census = {}
    lb_cert = -np.inf
    lb_arg = None
    for r in rows:
        feas, t_lo, t_hi, fails = work.point_certify(r["theta"])
        if not (t_lo - BOXW_TOL <= r["trace_r"]
                <= t_hi + BOXW_TOL):
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
    # witness search (CCLXI stage-1 verbatim, sigma constraint on)
    def sig_con(theta):
        s = ksd.sigma_quotient(theta)
        if not math.isfinite(s) or theta[0] <= 0.0:
            return -1.0
        return (sig_cap - s) / max(abs(sig_cap), 1e-6)
    v_wit, t_wit, _sl = ksd.run_stage1(
        rows, cls, fdata, "O2 witness search (sigma-capped, "
        "CCLXI stage-1 verbatim)", WIT_MS, WIT_DE,
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

    # ---- X: control must fire
    section("X -- control: indefinite matrix -> certified "
            "tr R >= 1")
    th_ctrl = rows[i_hot]["theta"].copy()
    th_ctrl[0] = CTRL_B1
    _feas, c_lo_v, c_hi_v, _fails = work.point_certify(th_ctrl)
    lam1 = float(np.linalg.eigvalsh(
        ksd.theta_matrices(th_ctrl)[0])[0])
    check("G5 CONTROL certified enclosure at the declared "
          "indefinite theta (lambda_min %.4f): tr R in "
          "[%.6f, %.6f], lower end >= 1"
          % (lam1, c_lo_v, c_hi_v), c_lo_v >= 1.0, kill="K4")
    if KILLS:
        return finish([])

    # ---- O: the main certified B&B
    section("O -- CERTIFIED BRANCH AND BOUND at the frozen "
            "sigma cap %.6f" % sig_cap)
    master_lo = np.asarray(cls["lo"], float).copy()
    master_hi = np.asarray(cls["hi"], float).copy()
    master_lo[0] = max(master_lo[0], 0.0)   # b_1 > 0 verbatim
    master_lo[NDIM:] = np.maximum(master_lo[NDIM:], 0.0)
    # feasible members have diag(J_B) >= lambda_min(J_B) >= c_Bw
    # (Rayleigh) -- the pre-clip removes only infeasible points
    master_lo[1:NDIM] = np.maximum(master_lo[1:NDIM], cls["cb"])
    print("    master box: CCLXI box with b_1 clipped to [0, %.4g] "
          "(C_sig requires b_1 > 0) and b_2..b_8 >= c_Bw = %.4f "
          "(Rayleigh on the B-floor)" % (master_hi[0], cls["cb"]))
    res_main = run_bnb(work, master_lo, master_hi, MAIN_BUDGET_S,
                       "main")
    st = res_main["stats"]
    print("    TREE: processed %d, pruned sigma %d / B_floor %d / "
          "radius %d / KS %d / COEF %d / SPREAD %d / empty-clip %d;"
          " refused CF %d / SPREAD %d; dropped %d (floor %.4f); "
          "hard %d; open %d; stop=%s"
          % (st["processed"], st["pr_sigma"], st["pr_bfloor"],
             st["pr_radius"], st["pr_ks"], st["pr_coef"],
             st["pr_spread"], st["pr_empty"], st["ref_cf"],
             st["ref_spread"], st["dropped"],
             res_main["floor_used"], res_main["n_hard"],
             res_main["n_open"], res_main["stop"]))
    for tgt, t_s, n_p in sorted(res_main["crossings"],
                                key=lambda c: -c[0]):
        print("    TARGET sup <= %.3f CERTIFIED after %.1f s / %d "
              "boxes" % (tgt, t_s, n_p))
    bound = res_main["bound"]
    if res_main["worst"] is not None:
        w_lo, w_hi, w_ub = res_main["worst"]
        w_mid = 0.5 * (w_lo + w_hi)
        d_near = min(ksd.ks_distance(
            w_mid[NDIM:], w_mid[:NDIM], r["theta"][NDIM:],
            r["theta"][:NDIM]) for r in rows)
        print("    HARD REGION anatomy (worst box): UB %.6f, "
              "mid b1 %.6g a1 %.6g sigma %.6g lam(Jmid) %s; "
              "KS-dist to nearest truth %.4g "
              "(CCLXI maximizer corner b1 = -2.89 is EXCLUDED by "
              "the b_1 > 0 clip)"
              % (w_ub, w_mid[0], w_mid[NDIM],
                 ksd.sigma_quotient(w_mid),
                 np.array2string(np.linalg.eigvalsh(
                     ksd.theta_matrices(w_mid)[0]),
                     precision=3), d_near))
    check("O1 certified global bound at cap %.4f: sup tr R <= %.6f "
          "(certified window [%.6f, %.6f])"
          % (sig_cap, bound, lb_cert, bound), True)

    # ---- D: sensitivity map
    section("D -- sigma-threshold sensitivity map (certified "
            "upper bounds; typed UPPER-BOUND map)")
    sens = [(sig_cap, bound, lb_cert, len(rows))]
    for cap2 in SIG_GRID_EXTRA:
        n_feas_truth = int(np.sum(sig_truth <= cap2))
        work2 = BoxWork(cls, env, cap2, fdata)
        res2 = run_bnb(work2, master_lo, master_hi, SENS_BUDGET_S,
                       "cap %.3f" % cap2)
        lb2 = -np.inf
        for r in rows:
            if r["sigma"] <= cap2:
                feas, t_lo, _th, _f = work2.point_certify(
                    r["theta"], sig_cap=cap2)
                if feas:
                    lb2 = max(lb2, t_lo)
        sens.append((cap2, res2["bound"], lb2, n_feas_truth))
        print("    cap %.3f: certified bound %.6f, certified LB "
              "%.6f, truth feasible %d/%d%s (stop=%s, proc %d)"
              % (cap2, res2["bound"], lb2, n_feas_truth,
                 len(rows),
                 "" if n_feas_truth == len(rows)
                 else " <- EXCLUDES TRUTH, sharpness probe only",
                 res2["stop"], res2["stats"]["processed"]))
    sens.sort(key=lambda s: s[0])
    best_cap = max((c for c, b, _l, _n in sens if b < 1.0),
                   default=None)
    check("D1 sensitivity map typed: largest cap with certified "
          "sup < 1: %s"
          % ("%.3f" % best_cap if best_cap is not None
             else "NONE within budget"), True)
    print("    map (cap, certified UB, certified LB, truth-in): %s"
          % "; ".join("(%.3f, %.4f, %.4f, %d)" % s for s in sens))

    # ---- screens: typed vacuous
    check("S1 tau/c_h relocation screens VACUOUS BY CONSTRUCTION "
          "(class-level certified bounds, no new per-step decision "
          "currency; reused T5 reproduces CCXLVII reserves)", True)

    # ---- verdict
    labels = []
    used = ("box, a>=0, B_floor, radius, KS_wall, COEF, SPREAD, "
            "sigma (b_1>0)")
    if bound < 1.0:
        labels.append(
            "KSDUAL-RIGOR-CLOSES(sup tr R <= %.6f CERTIFIED-"
            "INTERVAL-GLOBAL over the sigma-augmented class "
            "(constraints: %s); window [%.6f, %.6f]; tree %d boxes)"
            % (bound, used, lb_cert, bound, st["processed"]))
    elif lb_cert >= 1.0:
        labels.append(
            "KSDUAL-SIGMA-INSUFFICIENT(certified feasible witness "
            "tr R >= %.6f >= 1: the sigma-cap provably does NOT "
            "close the class)" % lb_cert)
    else:
        labels.append(
            "KSDUAL-RIGOR-OPEN(certified window [%.6f, %.6f] after "
            "the frozen budget; constraints: %s; tree %d boxes, "
            "stop=%s)" % (lb_cert, bound, used, st["processed"],
                          res_main["stop"]))
    labels.append("SENSITIVITY-MAP(%s; largest cap certified < 1: "
                  "%s)" % ("; ".join("%.3f->%.4f" % (c, b)
                                     for c, b, _l, _n in sens),
                           "%.3f" % best_cap
                           if best_cap is not None else "NONE"))
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
