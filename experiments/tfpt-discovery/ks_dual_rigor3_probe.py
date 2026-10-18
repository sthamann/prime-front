#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ks_dual_rigor3_probe -- PRIME.ONEBADMODE.KS.DUAL.RIGOR.03
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

MISSION.  Certify the class-level supremum with ALL accumulated
upgrades.  CCLXXXIII (ks_dual_rigor2_probe) closed the wide-box
continued-fraction refusal front (corner-monotone [J_B^-1]_11
enclosure, 13.6M refusals -> 0) but exposed the true wall: on wide
boxes the good seats of the objective upper bound were pinned at
R(widened class floor 0.3146) = 0.173 EACH, because the only
available good-block currency was the single widened constant.
CCLXXXV (radau_class_close_probe) built the TIGHT-FLOOR class --
per-member certified ordered co-block floors as class data (exact
rational Jacobi-Sturm, 48 dyadic bisections, within the inherited
1e-6 certificate-quality bar of the true ordered J_B spectrum)
instead of the single widened constant -- with numeric
sup tr R = 0.972698 (the thin truth rung itself).  THIS PROBE
COMBINES BOTH: a certified interval branch-and-bound over the
tight-floor class where the seats-2..8 upper bound is computed from
the PER-MEMBER ordered floor data (class constraints, hence
available per box) instead of the global 0.3146.

THE CLASS (frozen; the CCLXXXV tight-floor class with the floor
datum extended from the scalar c to the full certified ordered
vector, same inherited quality bar).  C_TF = union over the frozen
85-branch catalog (one branch per CCLXXXI cell) of

  C_k = { J = J(theta), theta in the frozen CCLXXXI box }
        AND a_i >= 0, n = b_1 > 0                       [ENTRY]
        AND KS_wall / COEF / SPREAD / radius / B-floor
            lambda_min(J_B) >= c_Bw = 0.3146            [C_KS verbatim,
                                                         CCLXXXI]
        AND nu_j in [MOM_lo_j, MOM_hi_j], j = 0..8      [MOM, CCLXXXI]
        AND eta = nu_1/nu_0 in [eta_lo, eta_hi]         [CCLXXXV P0;
                                                         eta == b_2
                                                         EXACTLY in
                                                         Jacobi
                                                         coordinates,
                                                         warded]
        AND (1 - 1e-6) lambda_j(J_B) <= f_j^k
            <= lambda_j(J_B), j = 1..7                  [P2 TIGHT
                                                         ORDERED
                                                         FLOORS: the
                                                         member's
                                                         certified
                                                         per-member
                                                         floor data;
                                                         the A6 bar
                                                         of CCLXXXV
                                                         extended
                                                         from f_1 to
                                                         all seven]
        AND RADAU_5(nu_0..nu_8; f_1^k) <= t_R n,
            t_R = 0.7809                                [P4, CCLXXXV]

Every CCLXXXI ladder cell is a certified member of its own branch
(warded below); the 17 F0 cells contribute their certified floor
vectors to the catalog but sit OUTSIDE the CCLXXXI entry box (the
CCLXXXI A12 disclosure, restated) -- kz-45 remains covered by the
CITED CCLXXIX/CCLXXXV two-tier fallback.

THE WIDTH-TOLERANT GOOD-BLOCK CURRENCY (a).
 U1 For every member of branch k, Cauchy interlacing gives
    lambda_{m}(J) >= lambda_{m-1}(J_B) >= f_{m-1}^k for m = 2..8,
    and the spectrum lies in [-L, L] (radius), so with the CERTIFIED
    envelope maximum Rdec_cert(x) = rangemax(R, [x, L]) (the CCLXVII
    outward-rounded segment envelope, containment-warded here):
      sum_{m=2..8} R(lambda_m(J)) <= SG_k
          := sum_{j=1..7} Rdec_cert(f_j^k),
    a CONSTANT of the branch -- pointwise in the class data, hence
    WIDTH-INDEPENDENT.  On a parameter box the certified good-seat
    bound is max over the branches FEASIBLE for the box of SG_k.
 U2 branch feasibility per box: the R2 eigenvalue enclosure of J_B
    gives lambda_j(J_B) in [lb_j, ub_j] for every member; branch k
    is infeasible on the box iff some f_j^k > ub_j (no member can
    satisfy the floor) or some f_j^k/(1-1e-6) < lb_j (no member can
    satisfy the TIGHTNESS bar).  A box with NO feasible branch is
    PRUNED by exactly the ordered-floor constraint (pr_floor;
    control X3 must fire).  This is the ward against rigor-2's
    per-box widened-floor currency: the feasible-branch set, not
    the box width, prices the good seats.
 U3 the branch set also sharpens the box currencies: bw_eff =
    max(c_Bw, min feasible f_1^k) is a certified per-box B-floor
    (feeds j11 <= 1/bw_eff, the lam1 floors); min/max feasible
    floor coordinates give per-seat clips; max feasible
    f_7^k/(1-1e-6) upper-bounds lambda_max(J_B).
 U4 the remaining box-dependent pieces: the bad seat via the
    CCLXXXIII corner-monotone [J_B^-1]_11 enclosure (reused, its
    lemma wards rerun) PLUS two certified lambda_1 floors --
    (i) the block-Rayleigh floor of CCLXVII with the per-box
    q_hi = a1_hi^2 j11_hi (not just the global cap) and bw_eff,
    (ii) THE CLOSED-FORM SCHUR-RADAU FLOOR Lambda(n_lo_eff, bw_eff,
    t_R) = ((n+c) - sqrt((n-c)^2 + 4nc rho))/2 of CCLXXXI R3 (valid
    for every member: q <= RADAU_5 <= t_R n by Gauss-Radau + P4;
    Lambda strictly increasing in n and c for rho < 1, warded
    symbolically), with the per-box pivot floor n_lo_eff =
    max(box, a1_lo^2/(b2_hi t_R)) from the CCLXXXV sharp-pivot
    theorem (nu_0^2/nu_1 = a1^2/b_2 exactly).
 U5 MOM and eta are deployed per box by EXACT ENDPOINT MONOTONICITY:
    after the master pre-clips (b_j >= c_Bw > 0, a_i >= 0) the
    matrix entries are nonnegative, so nu_j = a1^2 (J_B^j)_{11} is
    nondecreasing in every coordinate and the two corner evaluations
    with directed rounding enclose it exactly (warded); eta == b_2
    is an entry-box clip.  The RADAU functional itself is consumed
    only through its Gauss-Radau corollary q <= t_R n (omitting a
    class constraint only weakens certified upper bounds -- sound).

THE B&B RERUN (b).  CCLXVII queue/branching machinery with the
rigor-2 depth tie-break, DROP_FLOOR3 = 0.9735 > certified truth
floor 0.9727, the extended target ladder down to 0.974, batched
BoxWork3 with the currencies above, per-box objective UB =
rangemax(R, seat-1 clip) + min(SG_eff, per-seat enclosure sum).
Reported: the certified bound, ladder crossings, full tree stats
including the good-seat currency census (sg_win/enc_win), the
refusal and prune census, residual hard regions.

THE VERDICT (c) (frozen enum, dominance order):
 KSDUAL-TIGHTFLOOR-CERTIFIED(certified sup tr R <= B < 1 over C_TF:
   the COMPOSED THEOREM, stated loudly -- every member of the frozen
   tight-floor entry-data class satisfies tr R <= B < 1, hence
   R(lambda_1) < 1, hence (R >= 1 on x <= 0, R >= 0 everywhere,
   CCXXV certified separator facts) lambda_1(J) > 0: every member is
   WALL-POSITIVE; the 68 ladder truth steps are certified members;
   HONEST TYPING: the class margin is structurally capped at
   1 - 0.9727 = 0.0273 by the thinnest truth rung; the floors are
   per-member certified data with their round-62/Jacobi-Sturm
   provenance; the F0 cells sit outside the entry box (kz-45 by the
   cited two-tier fallback); NO all-h claim beyond the certified
   membership)
 KSDUAL-TIGHTFLOOR-LB-GEQ-1(certified feasible witness >= 1 --
   guard enum, structurally impossible while the truth floor holds)
 KSDUAL-STILL-OPEN(certified window [LB, B] with B >= 1 after the
   frozen budget; residual hard-region anatomy + the currency still
   missing)
Every enum is a finite float64/exact-rational statement with
outward rounding about the deployed 85-cell CCLXXXI geometry, the
frozen catalog and the frozen CCXXV separator; NEVER an all-h
statement, NEVER an RH claim.

GATES (d).
 CAT1 catalog integrity: every branch floor vector is nondecreasing
    (ordered); a doctored DISORDERED vector is REFUSED by the
    builder (control fires).
 CAT2 SG dominance: SG_k >= the member's TRUE good-seat sum
    sum_{m>=2} R(lambda_m(J)) on 85/85 catalog cells (validity of
    the width-tolerant currency against truth).
 LAM1 sympy: Lambda is the smaller root of (n-lam)(c-lam) = rho c n
    (CCLXXXI A1 rerun) AND dLambda/dn > 0 via the exact identity
    (n-c)^2 + 4 n c rho - (n - c + 2 c rho)^2 = 4 c^2 rho (1 - rho)
    (> 0 for rho < 1; Lambda is symmetric in n <-> c).
 LAM2 validity: Lambda(n, c_cert, t_R) <= lambda_1(J) truth on
    85/85 cells; sharp-pivot n >= a1^2/(b_2 t_R) on every
    K5-admitted cell; eta == b_2 identity on 85/85.
 M1/M3/M4/M5 the CCLXXXIII corner-CF lemma wards RERUN (sympy
    13/13; exact-rational monotone directions; corner-range
    containment with non-vacuity census on the NEW master box;
    exact-rational point tier on all 85 cells).
 G1-G3, G2b, G2c, G7a the CCLXVII envelope/Sturm/identity/LOG_PAD/
    box-containment wards RERUN on the CCLXXXI geometry.
 G3b THE CORRECTED-INTERLACING SEAT WARD (new; the A1 defect ward):
    on random (box, point) pairs every lambda_m(J) obeys
    lambda_m(J) <= lamB_m + e (m <= 7) and lambda_m(J) >=
    lamB_{m-1} - e (m >= 2), 100%.
 X4 control (must fire): the INHERITED rigor-1/2 upper mapping
    lambda_{m+1}(J) <= lamB_m + e must be VIOLATED on the declared
    counterexample and on sampled geometry -- the disclosed A1
    defect is real and the G3b ward has discriminating power.
 MOM1 corner-moment containment: nu_0..nu_8 of random interior
    points inside the corner-monotone enclosure, 100%.
 G4 truth membership CERTIFIED 68/68 ladder cells in their OWN
    branch (all constraint intervals incl. floors/tightness + tr R
    containment); F0 census typed (entry-box A12 disclosure).
 G5 control (must fire): the declared indefinite theta (hot truth
    step, b_1 -> -1) certifies tr R lower end >= 1.
 X2 control (must fire): the corner CF on a box with a certifiably
    negative J_B diagonal refuses both corners and raises the
    pivot-condensation prune.
 X3 control (must fire): a truth point box run against a doctored
    catalog whose floors certifiably exceed the box spectrum is
    pruned with pr_floor = 1 and NO other prune counter moving --
    the ordered-floor logic, and exactly it, kills the box.
 X5 control (must fire): overclaimed floors (1.01 x spectrum) make
    the member's own certification FAIL on the floor seat.
 G6 anti-circularity: class rebuilt by the CCLXXXI machinery
    verbatim (box SHA warded against the CCLXXXI frozen-log value),
    catalog frozen + SHA before the B&B, eta/floor ranges warded
    against the CCLXXXV note values; AST firewall + AC scan of the
    new rigorous functions (no ladder or read identifiers); the
    floors are the P2 co-block premise (CCLXXXV typing) -- no wall
    eigendatum enters a class constraint.
 G7 refusal discipline: corner-CF fallbacks counted (ref_cflo /
    ref_cfhi), legacy interval-CF refusals counted, SPREAD refusals
    counted; nothing rounded inward.

HONEST AMENDMENTS (declared BEFORE the frozen run).
 A1 DEFECT FOUND IN THE REUSED MACHINERY, DISCLOSED AND CORRECTED.
    The CCLXVII/CCLXXXIII BoxWork upper interlacing clip assigns
    seat m+1 the upper bound lamB_m + e (code: cl_hi[:, 1:] clipped
    by db columns 0..6).  That inequality is FALSE: Cauchy gives
    lambda_m(J) <= lambda_m(J_B) (seat m from lamB_m), and
    lambda_8(J) has NO J_B upper bound at all -- a diagonal
    counterexample (a_1 = 0, b_1 large) violates the coded mapping
    by O(10).  Consequence, typed: the CCLXVII / CCLXXXIII per-box
    upper bounds consumed an invalid clip, so their reported
    'certified' upper ends (2.0797) and empty-clip prunes are NOT
    certified as claimed (their LOWER ends and the truth
    certifications are unaffected).  THIS probe uses the corrected
    clips (G3b warded, X4 control on the old mapping) and makes no
    reuse of the defective seat assignment.
 A2 the class B&B'd here carries the FULL certified ordered floor
    vector per member as class data -- the natural extension of
    CCLXXXV amendment A6 from the scalar c-datum to all seven
    ordered floors, with the SAME inherited 1e-6 quality bar,
    two-sided.  The catalog is the frozen 85-branch set (one branch
    per CCLXXXI cell, F0 included); it is never silently enlarged.
    A branch whose data a box cannot host is excluded by exactly
    the floor logic (X3).
 A3 MOM / eta / RAD deployment per box: MOM by exact corner
    monotonicity (U5), eta by the exact identity eta == b_2, RAD
    only through its Gauss-Radau corollary q <= t_R n and the
    sharp-pivot floor.  The RADAU functional is NOT interval-
    evaluated per box; omitting a constraint only enlarges the
    feasible set and weakens (raises) the certified upper bound.
 A4 the CCLXXXI/CCLXXXV optimizer tiers (E/D/F ladders) are CITED
    as frozen reference constants, not re-run: this probe's budget
    goes to the certified B&B, which replaces the numeric extremal
    statement they made.  The rebuilt pipeline stages (ladder, F0,
    exact floors, class freeze, membership, AC typing) ARE re-run
    and their gates absorbed.
 A5 the F0 cells lie outside the CCLXXXI entry box (A12, restated):
    the composed statement covers the box-restricted class whose
    certified members are the 68 ladder cells; kz-45 h=1359 is
    covered by the cited CCLXXIX/CCLXXXV individual K=5 certificate
    (bound 0.726909, reproduced here).

EXTERNAL-CITED (consumed, warded, never proved here).
 E1 Cauchy interlacing, Weyl, polar, Sylvester/LDL [Horn & Johnson,
    Matrix Analysis 2nd ed., 2013, Sec. 4.3, 7.2-7.3].
 E2 Gauss-Radau upper bound for b^T B^{-1} b [Golub & Meurant,
    Matrices, Moments and Quadrature, PUP 2010, Ch. 6-7]; warded
    per cell by the reused CCLXXXI RB1 gate.
 E3 the CCXXV separator facts (R >= 0 on R, R >= 1 on x <= 0,
    R <= delta on [c_B, L]), re-consumed read-only.
 E4 the Jacobi weight / discriminant identity (SPREAD), warded.
 E5 everything CCLXXXI cites through the read-only pipeline reuse.

FROZEN PROTOCOL.  S0 firewall/AC -> rc pipeline (L no-go, W ladder,
F0, T filter/reads, B/I Jacobi, SR anchors, C exact floors/Radau,
G class freeze, AC typing, N membership; gates absorbed) -> G+
tight-floor freeze (eta/floor ranges, SHA wards, censuses, kz-45) ->
GEO exact seven-floor geometry (CCLXXXV G rerun) -> M catalog +
currency wards -> R reused-machinery wards -> N truth certification
+ certified LB -> X controls -> O main B&B -> V verdict.  tau/c_h
relocation screens are VACUOUS BY CONSTRUCTION (typed: class-level
certified bounds, no new per-step decision currency).

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

FROZEN BARS.  NDIM = 8; N_MOM = 9; BOX_SHA_CCLXXXI (32-hex prefix)
= 6dfe799c61ac11f98b6bc21243b22a04; ETA_REF = [2.9308e1, 7.5185e4];
FLOOR_REF = [0.202055, 145.312]; REF_RTOL = 2e-2; SUP_TF_REF =
0.972698 (rel ward 5e-3 on the certified LB); K5_CENSUS = 85/85;
K4_CENSUS = 84/85; KZ45_H = 1359; KZ45_BOUND5 = 0.726909 (rel
2e-3); CAT_RTOL = Fraction(1, 10^6) (the inherited CCLXXXV
FLOOR_CERT_RTOL bar); T_R = 0.7809 (cap, via cls['t_r']);
DROP_FLOOR3 = 0.9735; TARGETS3 = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02,
1.01, 1.005, 1.002, 1.001, 0.9999, 0.999, 0.995, 0.99, 0.985, 0.98,
0.978, 0.976, 0.9745, 0.974); MAIN_BUDGET_S3 = 900 (smoke 45);
ENV_WARD_N3 = 4096 (smoke 512); STURM_WARD_N3 = 24 (smoke 6);
BOX_WARD_N3 = 160 (smoke 24); SEAT_WARD_N3 = 200 (smoke 32);
MOM_WARD_N3 = 120 (smoke 24); PTS_PER_BOX = 4; MONO_WARD_N3 = 128
(smoke 32); DERIV_WARD_N3 = 12 (smoke 6); CFR_WARD_N3 = 96 (smoke
24); CFR_PTS = 4; CF_EXACT_TOL = 1e-9; LAM_TIE = 1e-9; PIV_TIE =
1e-9; ETA_ID_TIE = 1e-12; WARD_SEED3 = 20260812; CTRL_B1 = -1.0;
CTRL_B2 = -1.5; CTRL_FLOOR_SCALE = 1.01; CTRL_CAT_SCALE = 1e3;
BOXW_TOL / ENV_TOL / IDENT_TOL / LOG_PAD / QUEUE_CAP / BATCH /
WFLOOR_REL consumed verbatim from the read-only CCLXVII import;
all CCLXXXI bars consumed verbatim through the read-only pipeline
reuse; runtime cap 25 min.

SMOKE DISCLOSURE (2026-08-12; ONE declared smoke pass on the
10-rung + 3-deep subset ladder with 1 F0 substitute cell BEFORE
this freeze; NO bar, control, gate, enum or success rule was
changed after the smoke; the ONLY post-smoke edit is this
disclosure block, and the SPEC SHA is frozen WITH it).
SMOKE-1 (SPEC v0 SHA 37ec3490, 50.2 s total, 45 s B&B slice):
77/77 checks GREEN, no kills.  Honest readings: (i) every lemma /
enclosure / identity ward machine-exact -- LAM1 + M1 sympy exact,
M3 32/32 exact-rational directions, M4 96/96 corner containment
(non-vacuity census full-PD 5 / mixed 10 / refused 9 of 24), M5
12/12 exact point tier worst rel 7.6e-16, G1 envelope 512/512, G2
Sturm 6/6, G2b/G2c 2.9e-15 / 1.1e-15, G3 box containment 96/96
slack 0.0, G3b corrected-seat ward 32/32, MOM1 48/48; (ii) EVERY
control fired: X4 (the inherited defective upper clip violated by
2.167 on the declared counterexample and on 14/32 sampled boxes --
amendment A1 is real), X3 (doctored catalog: pr_floor = 1, every
other counter silent), X5 (overclaimed floors refused on the floor
seat), CAT1b (disordered vector refused), G5 (indefinite control
enclosure [5.845178, 5.845178] >= 1), X2 (negative-diagonal
refusal + pivot-condensation prune); (iii) truth certification
11/11 subset ladder cells in their own branches, the 1 F0 cell
outside the entry box exactly as A12 types; (iv) the smoke B&B is
DEGENERATE BY CONSTRUCTION exactly as CCLXVII/CCLXXXIII typed it
(the fake-bridge subset cell kz=177 with tr R = 4.850599 is a
certified class member, so the smoke verdict LB-GEQ-1 is the known
smoke phenomenon, disclosed): 45 s slice, 1.30M boxes, certified
smoke bound 4.910597 -- 1.2 percent above the smoke truth floor (the
rigor-2 smoke plateaued at 7.8 on the same subset), with the new
currencies LIVE (floor-branch prunes 30407, B-floor 29682, sigma
6568, SG_eff good-seat wins 1808, 2156 boxes already dropped below
0.9735); (v) smoke-bypassed gates, all typed in-line: G+1 box SHA,
G+2 census, G+3 kz-45, G+4 eta/floor note refs, the O2
rel-to-0.972698 clause (its smoke printout shows the raw subset
value 4.85 -- bypass by design, decided only on the frozen
ladder), and the rc-inherited repro anchors.  The frozen run below
is the run of record.

NO RH claim.  No marker moves; no paper, ledger, website, manifest
or verification file is touched; the only edit outside this file is
the German CCLXXXIX line prepended to experiments/next.txt AFTER
the frozen summary.

Sources (read-only): radau_class_assembly_probe (CCLXXXI class
machinery + pipeline), radau_class_close_probe (CCLXXXV exact
seven-floor geometry + eta/floor freeze), ks_dual_rigor_probe
(CCLXVII envelope / eigenvalue enclosures / Sturm / B&B driver
shape), ks_dual_rigor2_probe (CCLXXXIII corner-monotone CF
enclosure + lemma wards), zolotarev_phase_filter_probe (CCXXV
filter), bfloor_perstep_certification_probe (round-62 exact tier,
through the CCLXXXI reuse).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor3_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ks_dual_rigor3_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import radau_class_assembly_probe as rc     # noqa: E402 (READ-ONLY)
import radau_class_close_probe as rcl       # noqa: E402 (READ-ONLY)
import ks_dual_rigor_probe as rig           # noqa: E402 (READ-ONLY)
import ks_dual_rigor2_probe as r2           # noqa: E402 (READ-ONLY)

zol = rc.zol

# ------------------------------------------------------- frozen bars
NDIM = 8
N_MOM = 9
SMOKE = "--smoke" in sys.argv[1:]
BOX_SHA_CCLXXXI = "6dfe799c61ac11f98b6bc21243b22a04"
ETA_REF = (2.9308e1, 7.5185e4)
FLOOR_REF = (0.202055, 145.312)
REF_RTOL = 2.0e-2
SUP_TF_REF = 0.972698
LB_RTOL = 5.0e-3
K5_CENSUS = 85
K4_CENSUS = 84
KZ45_H = 1359
KZ45_BOUND5 = 0.726909
CAT_RTOL_FR = Fraction(1, 10 ** 6)
DROP_FLOOR3 = 0.9735
TARGETS3 = (2.0, 1.5, 1.2, 1.1, 1.05, 1.02, 1.01, 1.005, 1.002,
            1.001, 0.9999, 0.999, 0.995, 0.99, 0.985, 0.98,
            0.978, 0.976, 0.9745, 0.974)
MAIN_BUDGET_S3 = 45.0 if SMOKE else 900.0
ENV_WARD_N3 = 512 if SMOKE else 4096
STURM_WARD_N3 = 6 if SMOKE else 24
BOX_WARD_N3 = 24 if SMOKE else 160
SEAT_WARD_N3 = 32 if SMOKE else 200
MOM_WARD_N3 = 24 if SMOKE else 120
PTS_PER_BOX = 4
MONO_WARD_N3 = 32 if SMOKE else 128
DERIV_WARD_N3 = 6 if SMOKE else 12
CFR_WARD_N3 = 24 if SMOKE else 96
CFR_PTS = 4
CF_EXACT_TOL = 1.0e-9
LAM_TIE = 1.0e-9
PIV_TIE = 1.0e-9
ETA_ID_TIE = 1.0e-12
WARD_SEED3 = 20260812
CTRL_B1 = -1.0
CTRL_B2 = -1.5
CTRL_FLOOR_SCALE = 1.01
CTRL_CAT_SCALE = 1.0e3

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
NEW_AC_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                 "lu_read", "assemble_step", "build_rung",
                 "artifact", "h")
NEW_AC_FUNCS = ("tf_moment_corner", "lambda_closed_lo",
                "branch_feas", "process")

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def configure_predecessor():
    rc.CHECKS = []
    rc.KILLS = []
    rc.SMOKE = SMOKE
    rc.T0 = T0


def check(name, ok, detail="", kill=None):
    return rc.check(name, ok, detail, kill)


def section(title):
    rc.section(title)


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


# ================= U5: exact corner-monotone moment enclosure
def tf_moment_corner(lo, hi, n_mom):
    """Certified [lo, hi] of nu_j = a1^2 (J_B^j)_{11}, j = 0..n_mom-1,
    over the box.  REQUIRES the master pre-clips (b_2..b_8 >= c_Bw
    > 0, all a >= 0): then every matrix entry is nonnegative, so
    (J_B^j)_{11} is a polynomial with nonnegative coefficients in
    the entries, hence nondecreasing in every coordinate -- the two
    corner evaluations with directed rounding enclose it (warded in
    MOM1)."""
    b_lo = lo[:, 1:NDIM]
    b_hi = hi[:, 1:NDIM]
    a_lo = np.maximum(lo[:, NDIM + 1:], 0.0)
    a_hi = np.maximum(hi[:, NDIM + 1:], 0.0)
    n_box = lo.shape[0]
    a1sq_lo = rig.ndown(np.maximum(lo[:, NDIM], 0.0) ** 2)
    a1sq_hi = rig.nup(hi[:, NDIM] ** 2)
    v_lo = np.zeros((n_box, NDIM - 1))
    v_lo[:, 0] = 1.0
    v_hi = v_lo.copy()
    nu_lo = np.zeros((n_box, n_mom))
    nu_hi = np.zeros((n_box, n_mom))
    nu_lo[:, 0] = a1sq_lo
    nu_hi[:, 0] = a1sq_hi
    for j in range(1, n_mom):
        w_lo = rig.ndown(b_lo * v_lo)
        w_hi = rig.nup(b_hi * v_hi)
        w_lo[:, :-1] = rig.ndown(w_lo[:, :-1]
                                 + rig.ndown(a_lo * v_lo[:, 1:]))
        w_hi[:, :-1] = rig.nup(w_hi[:, :-1]
                               + rig.nup(a_hi * v_hi[:, 1:]))
        w_lo[:, 1:] = rig.ndown(w_lo[:, 1:]
                                + rig.ndown(a_lo * v_lo[:, :-1]))
        w_hi[:, 1:] = rig.nup(w_hi[:, 1:]
                              + rig.nup(a_hi * v_hi[:, :-1]))
        v_lo, v_hi = w_lo, w_hi
        nu_lo[:, j] = rig.ndown(a1sq_lo * v_lo[:, 0])
        nu_hi[:, j] = rig.nup(a1sq_hi * v_hi[:, 0])
    return nu_lo, nu_hi


# ================= U4(ii): the closed-form Schur-Radau lambda_1 floor
def lambda_closed_lo(n_lo, c_lo, rho_hi):
    """Certified LOWER bound of Lambda(n, c, rho) = ((n + c) -
    sqrt((n - c)^2 + 4 n c rho)) / 2 for every member with n >=
    n_lo > 0, lambda_min(J_B) >= c_lo > 0 and q <= rho_hi n
    (rho_hi < 1): Lambda is strictly increasing in n and c (LAM1
    warded), so evaluation at (n_lo, c_lo, rho_hi) with outward
    rounding is a valid floor.  Vectorized, clipped at 0."""
    d1 = rig.nup((n_lo - c_lo) * (n_lo - c_lo))
    d2 = rig.nup(4.0 * rig.nup(rig.nup(n_lo * c_lo) * rho_hi))
    disc = rig.nup(rig.nup(d1 + d2) * (1.0 + 1e-13))
    root = rig.nup(np.sqrt(np.maximum(disc, 0.0)))
    lam = rig.ndown(0.5 * rig.ndown((n_lo + c_lo) - root))
    return np.maximum(lam, 0.0)


# ============================== the frozen branch catalog
def build_catalog(rows, env, cls):
    """The frozen 85-branch tight-floor catalog: per branch the
    exact certified ordered floors rounded DOWN (f_lo), the
    tightness caps f/(1 - CAT_RTOL) rounded UP (f_hi), and the
    width-independent good-seat constant SG_k = sum_j
    rangemax(R, [f_j, L]).  REFUSES a disordered floor vector."""
    n_br = len(rows)
    f_lo = np.zeros((n_br, NDIM - 1))
    f_hi = np.zeros((n_br, NDIM - 1))
    sg = np.zeros(n_br)
    one_m = Fraction(1) - CAT_RTOL_FR
    n_disorder = 0
    big_l = float(cls["L"])
    for i, row in enumerate(rows):
        frs = row["spec_floor_fr"]
        prev = None
        for j, fr in enumerate(frs):
            if prev is not None and fr < prev:
                n_disorder += 1
            prev = fr
            fl = float(fr)
            if Fraction(fl) > fr:
                fl = float(rig.ndown(fl))
            f_lo[i, j] = fl
            cap = fr / one_m
            fh = float(cap)
            if Fraction(fh) < cap:
                fh = float(rig.nup(fh))
            f_hi[i, j] = fh
        acc = 0.0
        for j in range(NDIM - 1):
            seg = float(env.range_max(np.asarray([f_lo[i, j]]),
                                      np.asarray([big_l]))[0])
            acc = float(rig.nup(acc + seg))
        sg[i] = acc
    if n_disorder:
        return None
    sha = hashlib.sha256(f_lo.tobytes() + f_hi.tobytes()
                         + sg.tobytes()).hexdigest()
    return dict(f_lo=f_lo, f_hi=f_hi, sg=sg, sha=sha, n=n_br)


# ============================== the upgraded batched box processor
class BoxWork3(rig.BoxWork):
    """The RIGOR.03 processor: CCLXVII machinery with (i) the
    CORRECTED two-sided interlacing clips (amendment A1), (ii) the
    width-tolerant branch-catalog good-seat currency (U1-U3),
    (iii) the corner-monotone CF enclosure of CCLXXXIII (U4), (iv)
    the closed-form Schur-Radau lambda_1 floor and the sharp-pivot
    per-box pivot floor (U4), (v) exact corner-monotone MOM and the
    eta == b_2 clip (U5).  cap = t_R (P4 through Gauss-Radau)."""

    def __init__(self, cls, env, fdata, cat):
        super().__init__(cls, env, float(cls["t_r"]), fdata)
        self.cat = cat
        self.eta_lo = float(cls["eta_lo"])
        self.eta_hi = float(cls["eta_hi"])
        self.mlo = np.asarray(cls["mlo"], float)
        self.mhi = np.asarray(cls["mhi"], float)
        self.trh = float(rig.nup(float(cls["t_r"])))
        self.stats.update(pr_eta=0, pr_mom=0, pr_piv=0, pr_floor=0,
                          pr_pdneg=0, ref_cflo=0, ref_cfhi=0,
                          pd_full=0, pd_mixed=0, sg_win=0,
                          enc_win=0)

    def branch_feas(self, ub_b, lb_b):
        """(n_box, n_branch) feasibility: branch k can host a box
        member iff f_j^k <= ub_j (floor satisfiable) AND
        f_j^k/(1-rtol) >= lb_j (tightness satisfiable) for all j."""
        f_lo = self.cat["f_lo"]
        f_hi = self.cat["f_hi"]
        ok_up = np.all(f_lo[None, :, :] <= ub_b[:, None, :], axis=2)
        ok_dn = np.all(f_hi[None, :, :] >= lb_b[:, None, :], axis=2)
        return ok_up & ok_dn

    def process(self, lo, hi):
        n_box = lo.shape[0]
        self.stats["processed"] += n_box
        keep = np.ones(n_box, bool)
        # ---- C_KS wall functionals (CCLXVII interval versions)
        ks_lo, _ks_hi = rig.ks_iv(lo, hi, self.cls)
        m = ks_lo > self.cls["ks_cap"]
        self.stats["pr_ks"] += int(np.sum(m & keep))
        keep &= ~m
        c_lo, c_hi = rig.coef_iv(lo, hi, self.cls)
        m = (c_hi < self.cls["coef_lo"]) | (c_lo > self.cls["coef_hi"])
        self.stats["pr_coef"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- eta datum (== b_2 exactly, LAM2-warded)
        m = (lo[:, 1] > self.eta_hi) | (hi[:, 1] < self.eta_lo)
        self.stats["pr_eta"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- MOM box by exact corner monotonicity (U5)
        nu_lo, nu_hi = tf_moment_corner(lo, hi, N_MOM)
        m = np.any((nu_lo > self.mhi[None, :])
                   | (nu_hi < self.mlo[None, :]), axis=1)
        self.stats["pr_mom"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- sharp-pivot per-box floor (U4): n >= a1^2/(b_2 t_R)
        n_floor = rig.ndown(rig.ndown(
            rig.ndown(np.maximum(lo[:, NDIM], 0.0) ** 2)
            / rig.nup(np.maximum(hi[:, 1], 1e-300))) / self.trh)
        m = hi[:, 0] < n_floor
        self.stats["pr_piv"] += int(np.sum(m & keep))
        keep &= ~m
        n_lo_eff = np.maximum(lo[:, 0], n_floor)
        # ---- eigenvalue enclosures + corner lambda_min
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
        # ---- U1/U2: the width-tolerant branch currency
        ub_b = rig.nup(db + eb_tot[:, None])
        lb_b = rig.ndown(db - eb_tot[:, None])
        ub_b[:, 0] = np.minimum(ub_b[:, 0], lb_hi_c)
        lb_b[:, 0] = np.maximum(lb_b[:, 0], lb_lo_c)
        feas = self.branch_feas(ub_b, lb_b)
        anyf = np.any(feas, axis=1)
        self.stats["pr_floor"] += int(np.sum(~anyf & keep))
        keep &= ~(~anyf)
        sg_arr = self.cat["sg"]
        f_lo_c = self.cat["f_lo"]
        f_hi_c = self.cat["f_hi"]
        sg_eff = np.max(np.where(feas, sg_arr[None, :], -np.inf),
                        axis=1)
        f1min = np.min(np.where(feas, f_lo_c[None, :, 0], np.inf),
                       axis=1)
        fminj = np.min(np.where(feas[:, :, None],
                                f_lo_c[None, :, :], np.inf), axis=1)
        fhimaxj = np.max(np.where(feas[:, :, None],
                                  f_hi_c[None, :, :], -np.inf),
                         axis=1)
        safe = anyf
        f1min = np.where(safe, f1min, self.cbw)
        fminj = np.where(safe[:, None], fminj, 0.0)
        fhimaxj = np.where(safe[:, None], fhimaxj, self.big_l)
        sg_eff = np.where(safe, sg_eff, np.inf)
        bw_eff = np.maximum(self.cbw, f1min)
        ublast_eff = np.minimum(self.big_l, fhimaxj[:, -1])
        # ---- U4: corner-monotone [J_B^-1]_11 (CCLXXXIII, reused)
        _sl, _sh, cf_ok, j_lo, j_hi = rig.sigma_cf_iv(lo, hi)
        self.stats["ref_cf"] += int(np.sum(~cf_ok & keep))
        (j_min_lo, ok_lb, j_max_hi, ok_ub, bad_ub,
         neg_prune) = r2.sigma_corner_iv(lo, hi)
        self.stats["pd_full"] += int(np.sum(ok_ub & keep))
        self.stats["pd_mixed"] += int(np.sum(ok_lb & ~ok_ub & keep))
        self.stats["pr_pdneg"] += int(np.sum(neg_prune & keep))
        keep &= ~neg_prune
        lam_top_b = np.minimum(rig.nup(db[:, -1] + eb_tot),
                               ublast_eff)
        j_lo_eff = rig.ndown(1.0 / np.maximum(lam_top_b, 1e-300))
        j_lo_eff = np.where(cf_ok, np.maximum(j_lo_eff, j_lo),
                            j_lo_eff)
        j_lo_eff = np.where(ok_lb, np.maximum(j_lo_eff, j_min_lo),
                            j_lo_eff)
        self.stats["ref_cflo"] += int(np.sum(~cf_ok & ~ok_lb & keep))
        j_hi_eff = rig.nup(1.0 / bw_eff)
        j_hi_eff = np.where(cf_ok, np.minimum(j_hi_eff, j_hi),
                            j_hi_eff)
        j_hi_eff = np.where(ok_ub, np.minimum(j_hi_eff, j_max_hi),
                            j_hi_eff)
        self.stats["ref_cfhi"] += int(np.sum(~cf_ok & ~ok_ub & keep))
        # ---- sigma prune at cap = t_R (P4 + Gauss-Radau)
        with np.errstate(divide="ignore", invalid="ignore"):
            sig_lo_eff = rig.ndown(
                rig.ndown(rig.ndown(np.maximum(lo[:, NDIM], 0.0)
                                    ** 2) * j_lo_eff)
                / np.maximum(hi[:, 0], 1e-300))
        m = sig_lo_eff > self.cap
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        m = hi[:, 0] <= 0.0          # b_1 > 0 verbatim
        self.stats["pr_sigma"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- the two certified lambda_1 floors (U4)
        a1_hi = hi[:, NDIM]
        q_hi = rig.nup(rig.nup(a1_hi * a1_hi) * j_hi_eff)
        g_lo = np.maximum(
            rig.ndown(n_lo_eff * (1.0 - self.cap)),
            rig.ndown(n_lo_eff - q_hi))
        u2_hi = rig.nup(j_hi_eff / bw_eff)
        u_hi = rig.nup(np.sqrt(u2_hi))
        good_g = g_lo > 0.0
        g_safe = np.where(good_g, g_lo, 1.0)
        t_inv = rig.nup(np.maximum(
            1.0 / g_safe,
            1.0 / bw_eff + rig.nup(rig.nup(a1_hi * a1_hi) * u2_hi)
            / g_safe) + rig.nup(a1_hi * u_hi) / g_safe)
        lam1_a = np.where(good_g, rig.ndown(1.0 / t_inv), 0.0)
        lam1_b = lambda_closed_lo(np.maximum(n_lo_eff, 0.0),
                                  bw_eff, self.trh)
        lam1_lo = np.maximum(lam1_a, lam1_b)
        # ---- SPREAD prune (CCLXVII)
        spr_lo, spr_hi, spr_ok = rig.spread_iv(lo, hi, dd, e_tot)
        self.stats["ref_spread"] += int(np.sum(~spr_ok & keep))
        m = spr_ok & ((spr_lo > self.cls["spr_hi"])
                      | (spr_hi < self.cls["spr_lo"]))
        self.stats["pr_spread"] += int(np.sum(m & keep))
        keep &= ~m
        # ---- CORRECTED two-sided interlacing clips (amendment A1):
        # seat m: lambda_m(J) >= lamB_{m-1} (m >= 2) and
        #         lambda_m(J) <= lamB_m (m <= 7); seat 8 upper only L
        cl_lo = (dd - e_tot[:, None]).copy()
        cl_hi = (dd + e_tot[:, None]).copy()
        cl_lo[:, 0] = np.maximum(
            np.maximum(cl_lo[:, 0], l1_lo_c),
            np.maximum(0.0, lam1_lo))
        cl_hi[:, 0] = np.minimum(
            np.minimum(cl_hi[:, 0], l1_hi_c),
            np.minimum(np.min(hi[:, :NDIM], axis=1), self.big_l))
        cl_lo[:, 1:] = np.maximum(
            cl_lo[:, 1:],
            np.maximum(self.cbw, np.maximum(lb_b, fminj)))
        cl_lo[:, 1] = np.maximum(cl_lo[:, 1], lb_lo_c)
        cl_hi[:, :NDIM - 1] = np.minimum(
            cl_hi[:, :NDIM - 1],
            np.minimum(self.big_l, np.minimum(ub_b, fhimaxj)))
        cl_hi[:, NDIM - 1] = np.minimum(cl_hi[:, NDIM - 1],
                                        self.big_l)
        # ---- C7 second-moment top floor (CCLXVII, unchanged)
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
        # ---- the objective UB: bad seat + min(SG_eff, enclosure)
        seat1 = self.env.range_max(cl_lo[:, 0], cl_hi[:, 0])
        good_enc = np.zeros(n_box)
        for k in range(1, NDIM):
            good_enc = rig.nup(good_enc + self.env.range_max(
                cl_lo[:, k], cl_hi[:, k]))
        good_ub = np.minimum(sg_eff, good_enc)
        self.stats["sg_win"] += int(np.sum((sg_eff < good_enc)
                                           & keep))
        self.stats["enc_win"] += int(np.sum((good_enc <= sg_eff)
                                            & keep))
        ub = rig.nup(seat1 + good_ub)
        ub = np.where(np.isfinite(ub), ub, rig.UB_NEG_FAR * NDIM)
        # ---- split scores (CCLXVII/CCLXXXIII heuristics, speed only)
        rad = 0.5 * (hi - lo)
        score = rad / self.master_wd
        rb = rad[:, :NDIM]
        ra = rad[:, NDIM:]
        row_r = rb.copy()
        row_r[:, :-1] += ra
        row_r[:, 1:] += ra
        rmax = np.argmax(row_r, axis=1)
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

    def point_certify_tf(self, theta, br_idx):
        """Full tight-floor point certification: the CCLXVII base
        (box, a>=0, KS, COEF, sigma <= t_R, B-floor, radius,
        SPREAD, tr R enclosure) + eta + MOM + the OWN-branch floor
        and tightness seats."""
        feas, t_lo, t_hi, fails = self.point_certify(theta)
        th = np.asarray(theta, float)[None, :]
        if not (self.eta_lo <= th[0, 1] <= self.eta_hi):
            fails.append("eta")
        nu_lo, nu_hi = tf_moment_corner(th, th, N_MOM)
        if not (np.all(nu_hi[0] >= self.mlo)
                and np.all(nu_lo[0] <= self.mhi)):
            fails.append("MOM")
        jb_cols = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
        db, eb_tot, _ = rig.eig_enclosure(
            th[:, jb_cols], th[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        f_lo = self.cat["f_lo"][br_idx]
        f_hi = self.cat["f_hi"][br_idx]
        up = rig.nup(db[0] + eb_tot[0])
        dn = rig.ndown(db[0] - eb_tot[0])
        if not np.all(f_lo <= up):
            fails.append("floor")
        if not np.all(f_hi >= dn):
            fails.append("floor-tight")
        return (not fails), t_lo, t_hi, fails


# ================= the B&B driver (CCLXVII/CCLXXXIII shape)
def run_bnb3(work, master_lo, master_hi, budget_s, label):
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
        bound_now = float(np.max(c_ub)) if len(c_ub) else DROP_FLOOR3
        if hard_ub:
            bound_now = max(bound_now, max(hard_ub))
        for tgt in TARGETS3:
            if bound_now < tgt and not any(
                    abs(cr[0] - tgt) < 1e-15 for cr in crossings):
                crossings.append((tgt, time.time() - t_start,
                                  work.stats["processed"]))
        if bound_now < TARGETS3[-1] + 1e-12:
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
            drop = keep_c & (ub_c < DROP_FLOOR3)
            work.stats["dropped"] += int(np.sum(drop))
            if np.any(drop):
                floor_used = max(floor_used, DROP_FLOOR3)
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
        bound = DROP_FLOOR3
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
                            else DROP_FLOOR3))


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in rc.CHECKS if ok)
    n_tot = len(rc.CHECKS)
    if rc.KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN",
             "K4": "CONTROL-SILENT"}[rc.KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64/exact-rational statements with
  outward rounding about the deployed 85-cell CCLXXXI geometry, the
  frozen tight-floor branch catalog and the frozen CCXXV separator.
  Certified upper bounds hold over the ENTIRE frozen tight-floor
  class (omitted constraints only weaken bounds); certified lower
  bounds are interval-verified feasible points.  The floors are
  per-member certified data (exact Jacobi-Sturm / round-62
  provenance), consumed as the P2 co-block premise -- no wall
  eigendatum enters a class constraint.  The corrected interlacing
  clips are seat-warded; the inherited defective clip is disclosed
  (A1) and excluded.  Heuristics steer the search order only, never
  the arithmetic.  No marker moves; no paper, ledger, website,
  manifest or verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(rc.KILLS) if rc.KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not rc.KILLS else 1


def main():
    configure_predecessor()
    section("PRIME.ONEBADMODE.KS.DUAL.RIGOR.03 -- certified B&B on "
            "the TIGHT-FLOOR class: per-member ordered floors as "
            "the width-tolerant good-seat currency (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(NEW_AC_FUNCS, NEW_AC_BANNED)
    check("S0.2 AC the new rigorous functions (%s) contain no "
          "ladder or read identifier" % ",".join(NEW_AC_FUNCS),
          not ac, ",".join(sorted(set(ac))), kill="K2")
    check("S0.3 predecessors imported READ-ONLY: CCLXXXI %s..., "
          "CCLXXXV %s..., CCLXVII %s..., CCLXXXIII %s..."
          % (rc.SPEC_SHA[:8], rcl.SPEC_SHA[:8], rig.SPEC_SHA[:8],
             r2.SPEC_SHA[:8]), True)

    # ---- the CCLXXXI pipeline, rebuilt verbatim (gates absorbed)
    rc.no_go_lemma()
    if rc.KILLS:
        return finish([])
    steps, combined = rc.build_ladder()
    if rc.KILLS:
        return finish([])
    artifact = rc.artifact_key_ward(steps)
    f0_cells = rc.build_f0(combined)
    if rc.KILLS:
        return finish([])
    fdata = rc.get_filter(steps, artifact)
    rows = rc.make_rows(steps, f0_cells, artifact, fdata)
    rows = rc.jacobi_identity_wards(rows)
    if rc.KILLS:
        return finish([])
    rc.repro_anchors(rows)
    rc.certify_cells(rows)
    if rc.KILLS:
        return finish([])
    cls = rc.freeze_class(rows, fdata)
    rc.ac_typing(rows, cls)
    rc.membership(rows, cls)
    if rc.KILLS:
        return finish([])

    # ---- G+: tight-floor data freeze + verbatim-class wards
    section("G+ -- tight-floor freeze: verbatim-class, census and "
            "note-cited wards")
    if SMOKE:
        check("G+1 CCLXXXI box SHA ward SMOKE-BYPASSED by design "
              "(subset box %s...)" % cls["box_sha"][:16], True)
    else:
        check("G+1 frozen box SHA-256 == CCLXXXI verbatim (%s...)"
              % cls["box_sha"][:32],
              cls["box_sha"][:32] == BOX_SHA_CCLXXXI, kill="K2")
    n_k5 = sum(1 for r in rows
               if r["bound5"] <= cls["t_r"] + rcl.RATIO_TIE)
    n_k4 = sum(1 for r in rows
               if r["bound4"] <= cls["t_r"] + rcl.RATIO_TIE)
    check("G+2 RAD census reproduces CCLXXXV: K=5 %d/%d (ref "
          "%d/%d), K=4 %d (ref %d)"
          % (n_k5, len(rows), K5_CENSUS, K5_CENSUS, n_k4,
             K4_CENSUS),
          SMOKE or (n_k5 == K5_CENSUS == len(rows)
                    and n_k4 == K4_CENSUS), kill="K3")
    kz45 = sorted((r for r in rows
                   if r["seg"] == "F0" and r["kz"] == 45),
                  key=lambda r: -r["sigma"])[:1]
    target45 = kz45[0] if kz45 else None
    check("G+3 the CCLXXIX exception cell kz=45 h=%s rebuilt with "
          "cited K=5 bound %.6f (ref %.6f)"
          % ("%d" % int(target45["h"]) if target45 is not None
             else "-",
             target45["bound5"] if target45 is not None
             else float("nan"), KZ45_BOUND5),
          SMOKE or (target45 is not None
                    and int(target45["h"]) == KZ45_H
                    and abs(target45["bound5"] / KZ45_BOUND5 - 1.0)
                    <= 2.0e-3), kill="K3")
    rcl.freeze_new_data(rows, cls)
    if SMOKE:
        check("G+4 eta/floor note-cited range wards SMOKE-BYPASSED "
              "by design (subset data)", True)
    else:
        d_eta = max(abs(cls["eta_lo"] / ETA_REF[0] - 1.0),
                    abs(cls["eta_hi"] / ETA_REF[1] - 1.0))
        d_flo = max(abs(cls["floor_lo"] / FLOOR_REF[0] - 1.0),
                    abs(cls["floor_hi"] / FLOOR_REF[1] - 1.0))
        check("G+4 eta range [%.4e, %.4e] and floor range "
              "[%.6f, %.2f] reproduce the CCLXXXV note values "
              "(worst rel %.2e / %.2e <= %.0e)"
              % (cls["eta_lo"], cls["eta_hi"], cls["floor_lo"],
                 cls["floor_hi"], d_eta, d_flo, REF_RTOL),
              d_eta <= REF_RTOL and d_flo <= REF_RTOL, kill="K3")

    # ---- GEO: the exact seven-floor geometry (CCLXXXV G rerun)
    rcl.certify_geometry(rows)
    if rc.KILLS:
        return finish([])

    # ---- M: envelope + catalog + currency wards
    section("M -- the FROZEN BRANCH CATALOG + width-tolerant "
            "currency wards (the RIGOR.03 delta)")
    env = rig.Envelope(fdata)
    print("    envelope: %d certified segments on [%.3g, %.3g] "
          "(CCLXVII R1 verbatim)" % (env.n_seg, env.edges[0],
                                     env.edges[-1]))
    cat = build_catalog(rows, env, cls)
    check("CAT1 catalog built: %d branches, every floor vector "
          "nondecreasing (ordered); SHA-256 %s..."
          % (cat["n"] if cat else 0,
             cat["sha"][:16] if cat else "-"),
          cat is not None, kill="K2")
    if cat is None:
        return finish([])
    # the disorder REFUSAL control: doctor one vector and rebuild
    rows_bad = [dict(rows[0])]
    frs = list(rows[0]["spec_floor_fr"])
    frs[0], frs[1] = frs[1], frs[0]
    rows_bad[0]["spec_floor_fr"] = frs
    cat_bad = build_catalog(rows_bad, env, cls)
    check("CAT1b CONTROL a doctored DISORDERED floor vector is "
          "REFUSED by the catalog builder", cat_bad is None,
          kill="K4")
    sg = cat["sg"]
    i_hot = int(np.argmax([r["trace_r"] for r in rows]))
    print("    SG_k = sum_j rangemax(R, [f_j^k, L]): min/med/max "
          "%s; argmax branch kz=%d seg=%s; SG at the thin rung "
          "(kz=%d, tr R=%.6f) = %.6f"
          % (rc.e3(sg), rows[int(np.argmax(sg))]["kz"],
             rows[int(np.argmax(sg))]["seg"], rows[i_hot]["kz"],
             rows[i_hot]["trace_r"], sg[i_hot]))
    n_dom = 0
    worst_gap = -np.inf
    for i, r in enumerate(rows):
        lam_j = np.asarray(r["lam_j"], float)
        good_true = math.fsum(zol.scalar_r(fdata, float(v))
                              for v in lam_j[1:])
        gap = sg[i] - good_true
        worst_gap = max(worst_gap, -gap)
        if gap >= -1e-12:
            n_dom += 1
    check("CAT2 SG dominance: SG_k >= the member's TRUE good-seat "
          "sum on %d/%d cells (worst defect %.2e)"
          % (n_dom, len(rows), worst_gap), n_dom == len(rows),
          kill="K2")
    # LAM1: the closed-form floor, symbolically warded
    import sympy as sp
    nn, cc, rr, lam_s = sp.symbols("n c rho lam", positive=True)
    quad = sp.expand((nn - lam_s) * (cc - lam_s) - rr * cc * nn)
    closed = ((nn + cc) - sp.sqrt((nn - cc) ** 2
                                  + 4 * nn * cc * rr)) / 2
    lam_sol = sp.solve(sp.Eq(quad, 0), lam_s)
    w1 = any(sp.simplify(s - closed) == 0 for s in lam_sol)
    mono_id = sp.simplify(((nn - cc) ** 2 + 4 * nn * cc * rr)
                          - (nn - cc + 2 * cc * rr) ** 2
                          - 4 * cc ** 2 * rr * (1 - rr))
    w2 = mono_id == 0
    w3 = bool((4 * cc ** 2 * rr * (1 - rr)).subs(rr, sp.Rational(
        7809, 10000)).is_positive)
    check("LAM1 sympy: Lambda is the smaller root of (n-lam)(c-lam)"
          " = rho c n AND the monotonicity identity (n-c)^2+4ncr - "
          "(n-c+2cr)^2 == 4c^2 r(1-r) (> 0 at rho = t_R < 1: "
          "dLambda/dn > 0, symmetric in n <-> c)",
          w1 and w2 and w3, kill="K2")
    n_lam = 0
    n_piv = 0
    n_eta = 0
    for r in rows:
        th = np.asarray(r["theta"], float)
        lam1_t = float(np.min(r["lam_j"]))
        lam_f = float(lambda_closed_lo(
            np.asarray([th[0]]), np.asarray([r["c_cert"]]),
            float(rig.nup(cls["t_r"])))[0])
        if r["bound5"] <= cls["t_r"] + rcl.RATIO_TIE:
            if lam_f <= lam1_t + LAM_TIE:
                n_lam += 1
            if th[0] >= th[NDIM] ** 2 / (th[1] * cls["t_r"]) \
                    - PIV_TIE * max(1.0, abs(th[0])):
                n_piv += 1
        else:
            n_lam += 1
            n_piv += 1
        if abs(rcl.eta_value(th) - th[1]) \
                <= ETA_ID_TIE * max(1.0, abs(th[1])):
            n_eta += 1
    check("LAM2 validity on %d cells: Lambda(n, c_cert, t_R) <= "
          "lambda_1 truth %d/%d; sharp-pivot n >= a1^2/(b_2 t_R) "
          "%d/%d; eta == b_2 identity %d/%d"
          % (len(rows), n_lam, len(rows), n_piv, len(rows), n_eta,
             len(rows)),
          n_lam == n_piv == n_eta == len(rows), kill="K2")
    # the CCLXXXIII corner-CF lemma wards, rerun
    rng = np.random.default_rng(WARD_SEED3)
    try:
        n_ok, n_tot = r2.lemma_symbolic()
        check("M1 sympy corner-CF derivative identities: %d/%d"
              % (n_ok, n_tot), n_ok == n_tot, kill="K2")
    except ImportError:
        check("M1 sympy unavailable -- symbolic tier SKIPPED "
              "(exact-rational M3 carries)", True)
    n_ok = 0
    for _ in range(MONO_WARD_N3):
        bfr, afr = r2.random_pd_fractions(rng)
        base = r2.cf_exact_ba(bfr, afr)
        if base is None:
            continue
        bump = Fraction(1, 8)
        good = True
        for i in range(NDIM - 1):
            b2v = list(bfr)
            b2v[i] += bump
            v2 = r2.cf_exact_ba(b2v, afr)
            good &= v2 is not None and v2 <= base
        for i in range(NDIM - 2):
            a2v = list(afr)
            a2v[i] += bump
            v2 = r2.cf_exact_ba(bfr, a2v)
            good &= v2 is None or v2 >= base
        n_ok += int(good)
    check("M3 exact-rational monotone-direction ward: %d/%d random "
          "PD points obey the corner-CF lemma"
          % (n_ok, MONO_WARD_N3), n_ok == MONO_WARD_N3, kill="K2")
    # master box (pre-clips = class constraints, typed)
    master_lo = np.asarray(cls["lo"], float).copy()
    master_hi = np.asarray(cls["hi"], float).copy()
    master_lo[0] = max(master_lo[0], 0.0)
    master_lo[NDIM:] = np.maximum(master_lo[NDIM:], 0.0)
    master_lo[1:NDIM] = np.maximum(master_lo[1:NDIM], cls["cb"])
    master_lo[1] = max(master_lo[1], float(cls["eta_lo"]))
    master_hi[1] = min(master_hi[1], float(cls["eta_hi"]))
    a1_lo_m = float(rig.ndown(math.sqrt(max(cls["mlo"][0], 0.0))
                              * (1.0 - 1e-14)))
    a1_hi_m = float(rig.nup(math.sqrt(cls["mhi"][0])
                            * (1.0 + 1e-14)))
    master_lo[NDIM] = max(master_lo[NDIM], a1_lo_m)
    master_hi[NDIM] = min(master_hi[NDIM], a1_hi_m)
    master_lo[0] = max(master_lo[0], float(rig.ndown(
        a1_lo_m * a1_lo_m / (cls["eta_hi"] * cls["t_r"])
        * (1.0 - 1e-12))))
    n_in = sum(1 for r in rows if r["seg"] != "F0"
               and np.all(np.asarray(r["theta"], float)
                          >= master_lo - 1e-12)
               and np.all(np.asarray(r["theta"], float)
                          <= master_hi + 1e-12))
    n_lad = sum(1 for r in rows if r["seg"] != "F0")
    check("M6 pre-clipped master box (n > 0, a >= 0, b_j >= c_Bw, "
          "eta = b_2 box, a_1 in sqrt(MOM_0) box, sharp-pivot n "
          "floor %.3e) contains all %d/%d ladder cells"
          % (master_lo[0], n_in, n_lad), n_in == n_lad, kill="K2")
    # M4: corner-range containment on the new master box
    n_ok = 0
    n_t = 0
    n_full = 0
    n_mixedc = 0
    n_refused = 0
    for _ in range(CFR_WARD_N3):
        c0 = rng.uniform(master_lo, master_hi)
        c1 = rng.uniform(master_lo, master_hi)
        frac = rng.uniform(0.0, 0.5)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        (jmn, ok_lb, jmx, ok_ub, _bad,
         _neg) = r2.sigma_corner_iv(b_lo[None, :], b_hi[None, :])
        n_full += int(ok_ub[0])
        n_mixedc += int(ok_lb[0] and not ok_ub[0])
        n_refused += int(not ok_lb[0])
        for _p in range(CFR_PTS):
            th = rng.uniform(b_lo, b_hi)
            jex = r2.cf_exact(th)
            n_t += 1
            good = True
            if jex is not None and ok_lb[0]:
                good &= float(jmn[0]) <= float(jex) * (1 + 1e-15) \
                    + 1e-300
            if ok_ub[0]:
                good &= jex is not None \
                    and float(jex) <= float(jmx[0]) * (1 + 1e-15)
            n_ok += int(good)
    check("M4 corner-range containment %d/%d (box, point) pairs on "
          "the NEW master box; census full-PD %d / mixed %d / "
          "refused %d of %d"
          % (n_ok, n_t, n_full, n_mixedc, n_refused, CFR_WARD_N3),
          n_ok == n_t and n_full >= 1, kill="K2")
    # M5: exact-rational point tier on all cells
    n_ok = 0
    worst_rel = 0.0
    for r in rows:
        th = np.asarray(r["theta"], float)
        jex = r2.cf_exact(th)
        s_float = rc.sigma_quotient(th)
        j_float = s_float * float(th[0]) / (float(th[NDIM]) ** 2)
        (jmn, ok_lb, jmx, ok_ub, _bad,
         _neg) = r2.sigma_corner_iv(th[None, :], th[None, :])
        good = jex is not None and ok_lb[0] and ok_ub[0]
        if good:
            rel = abs(float(jex) - j_float) / max(1e-300,
                                                  abs(float(jex)))
            worst_rel = max(worst_rel, rel)
            good &= rel <= CF_EXACT_TOL
            good &= float(jmn[0]) <= float(jex) <= float(jmx[0])
        n_ok += int(good)
    check("M5 exact-rational point tier on %d/%d cells: exact j11 "
          "vs float read worst rel %.2e <= %.0e, inside the "
          "degenerate-box corner enclosure"
          % (n_ok, len(rows), worst_rel, CF_EXACT_TOL),
          n_ok == len(rows), kill="K2")

    # ---- R: reused-machinery wards on the CCLXXXI geometry
    section("R -- reused CCLXVII machinery wards (envelope, Sturm, "
            "identities, box containment, CORRECTED seat clips)")
    rng_r = np.random.default_rng(WARD_SEED3)
    xs = np.concatenate([
        rng_r.uniform(-1.05, 1.05, ENV_WARD_N3 // 2) * fdata["L"],
        np.sign(rng_r.standard_normal(ENV_WARD_N3 // 2))
        * np.exp(rng_r.uniform(np.log(1e-10),
                               np.log(1.04 * fdata["L"]),
                               ENV_WARD_N3 // 2))])
    r_pts = np.asarray([zol.scalar_r(fdata, float(x)) for x in xs])
    e_ub = env.range_max(xs, xs)
    e_lb = env.range_min(xs, xs)
    n_in = int(np.sum((r_pts <= e_ub + rig.ENV_TOL)
                      & (r_pts >= e_lb - rig.ENV_TOL)))
    check("G1 envelope containment %d/%d declared samples (worst "
          "UB slack %.2e)" % (n_in, len(xs),
                              float(np.max(r_pts - e_ub))),
          n_in == len(xs), kill="K2")
    n_sturm_ok = 0
    for _ in range(STURM_WARD_N3):
        th = rng_r.uniform(master_lo, master_hi)
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
          "with the enclosures" % (n_sturm_ok, STURM_WARD_N3),
          n_sturm_ok == STURM_WARD_N3, kill="K2")
    worst_id = 0.0
    worst_fro = 0.0
    for r in rows:
        th = np.asarray(r["theta"], float)
        jm, jb = rc.theta_matrices(th)
        evals, evecs = np.linalg.eigh(jm)
        w_log = np.sum(np.log(np.maximum(evecs[0, :] ** 2, 1e-300)))
        rhs = float(np.sum(rig.WEXP * np.log(th[NDIM:])))
        for i in range(NDIM):
            for j in range(i + 1, NDIM):
                rhs -= 2.0 * math.log(evals[j] - evals[i])
        worst_id = max(worst_id, abs(w_log - rhs)
                       / max(1.0, abs(w_log)))
        lam_b = np.linalg.eigvalsh(jb)
        fro = float(np.sum(th[1:NDIM] ** 2)
                    + 2.0 * np.sum(th[NDIM + 1:] ** 2))
        worst_fro = max(worst_fro, abs(np.sum(lam_b ** 2) - fro)
                        / max(1.0, fro))
    check("G2b/G2c Jacobi weight + Frobenius identity wards on all "
          "%d cells: worst rel %.2e / %.2e <= %.0e"
          % (len(rows), worst_id, worst_fro, rig.IDENT_TOL),
          worst_id <= rig.IDENT_TOL and worst_fro <= rig.IDENT_TOL,
          kill="K2")
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
        check("G7a LOG_PAD ward SKIPPED (no mpmath) -- pad kept at "
              "declared 1e-12", True)
    work = BoxWork3(cls, env, fdata, cat)
    n_ok = 0
    n_t = 0
    worst_sl = 0.0
    for _ in range(BOX_WARD_N3):
        c0 = rng_r.uniform(master_lo, master_hi)
        c1 = rng_r.uniform(master_lo, master_hi)
        frac = rng_r.uniform(0.0, 0.2)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        t_lo, t_hi = work.box_bounds_unclipped(b_lo[None, :],
                                               b_hi[None, :])
        l1c_lo, l1c_hi = rig.corner_lam_min(b_lo[None, :],
                                            b_hi[None, :], NDIM, 0,
                                            NDIM)
        for _p in range(PTS_PER_BOX):
            th = rng_r.uniform(b_lo, b_hi)
            v = rc.tr_r_of_theta(th, fdata)
            lam1_p = float(np.linalg.eigvalsh(
                rc.theta_matrices(th)[0])[0])
            n_t += 1
            ok = (t_lo[0] - rig.BOXW_TOL <= v
                  <= t_hi[0] + rig.BOXW_TOL
                  and l1c_lo[0] - rig.BOXW_TOL <= lam1_p
                  <= l1c_hi[0] + rig.BOXW_TOL)
            n_ok += int(ok)
            worst_sl = max(worst_sl, v - t_hi[0], t_lo[0] - v)
    check("G3 box containment %d/%d random (box, point) pairs "
          "(worst outward slack %.2e)" % (n_ok, n_t, worst_sl),
          n_ok == n_t, kill="K2")
    # G3b: the CORRECTED interlacing seat ward + X4 defect control
    jb_cols = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
    n_ok = 0
    n_t = 0
    n_old_viol = 0
    for _ in range(SEAT_WARD_N3):
        c0 = rng_r.uniform(master_lo, master_hi)
        c1 = rng_r.uniform(master_lo, master_hi)
        frac = rng_r.uniform(0.0, 0.3)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        db, eb_tot, _ = rig.eig_enclosure(
            b_lo[None, jb_cols], b_hi[None, jb_cols],
            NDIM - 1, 0, NDIM - 1)
        th = rng_r.uniform(b_lo, b_hi)
        lam_j = np.linalg.eigvalsh(rc.theta_matrices(th)[0])
        n_t += 1
        up = db[0] + eb_tot[0] + rig.BOXW_TOL
        dn = db[0] - eb_tot[0] - rig.BOXW_TOL
        ok = (np.all(lam_j[:NDIM - 1] <= up)
              and np.all(lam_j[1:] >= dn))
        n_ok += int(ok)
        if np.any(lam_j[1:] > up):
            n_old_viol += 1
    check("G3b CORRECTED-INTERLACING seat ward: lambda_m(J) <= "
          "lamB_m + e (m <= 7) and >= lamB_{m-1} - e (m >= 2) on "
          "%d/%d samples" % (n_ok, n_t), n_ok == n_t, kill="K2")
    th_ctr = np.asarray(rows[i_hot]["theta"], float).copy()
    th_ctr[NDIM] = 0.0
    th_ctr[0] = float(master_hi[0])
    db, eb_tot, _ = rig.eig_enclosure(
        th_ctr[None, jb_cols], th_ctr[None, jb_cols],
        NDIM - 1, 0, NDIM - 1)
    lam_j = np.linalg.eigvalsh(rc.theta_matrices(th_ctr)[0])
    old_viol = float(np.max(lam_j[1:] - (db[0] + eb_tot[0])))
    check("X4 CONTROL the INHERITED rigor-1/2 upper mapping "
          "lambda_(m+1)(J) <= lamB_m is VIOLATED (declared "
          "counterexample defect %.3e > 0; %d/%d sampled boxes "
          "also violate) -- amendment A1 is real and the G3b ward "
          "has power" % (old_viol, n_old_viol, n_t),
          old_viol > 0.0, kill="K4")
    # MOM1: corner-moment containment
    n_ok = 0
    n_t = 0
    for _ in range(MOM_WARD_N3):
        c0 = rng_r.uniform(master_lo, master_hi)
        c1 = rng_r.uniform(master_lo, master_hi)
        frac = rng_r.uniform(0.0, 0.4)
        b_lo = np.minimum(c0, c1 * frac + c0 * (1 - frac))
        b_hi = np.maximum(c0, c1 * frac + c0 * (1 - frac))
        nu_lo, nu_hi = tf_moment_corner(b_lo[None, :],
                                        b_hi[None, :], N_MOM)
        for _p in range(2):
            th = rng_r.uniform(b_lo, b_hi)
            momv = rc.moment_vector(th, rc.KDEG5)
            n_t += 1
            n_ok += int(np.all(momv >= nu_lo[0] - 1e-9 * np.abs(
                momv) - 1e-300)
                and np.all(momv <= nu_hi[0] + 1e-9 * np.abs(momv)
                           + 1e-300))
    check("MOM1 corner-moment containment %d/%d (box, point) "
          "pairs" % (n_ok, n_t), n_ok == n_t, kill="K2")

    # ---- N: truth certification in the OWN branch + certified LB
    section("N -- truth cells interval-certified in their OWN "
            "branch + certified lower bound")
    n_cert = 0
    fail_census = {}
    lb_cert = -np.inf
    lb_arg = None
    n_f0_box = 0
    for i, r in enumerate(rows):
        feas, t_lo, t_hi, fails = work.point_certify_tf(
            r["theta"], i)
        if not (t_lo - rig.BOXW_TOL <= r["trace_r"]
                <= t_hi + rig.BOXW_TOL):
            fails.append("trR-containment")
            feas = False
        if r["seg"] == "F0":
            if "box" in fails:
                n_f0_box += 1
            continue
        if feas:
            n_cert += 1
            if t_lo > lb_cert:
                lb_cert = t_lo
                lb_arg = "ladder cell kz=%d seg=%s" % (r["kz"],
                                                       r["seg"])
        for f in fails:
            fail_census[f] = fail_census.get(f, 0) + 1
    n_f0 = sum(1 for r in rows if r["seg"] == "F0")
    check("G4 truth membership CERTIFIED %d/%d ladder cells in "
          "their own branch (fails: %s)"
          % (n_cert, n_lad,
             ", ".join("%s x%d" % kv
                       for kv in sorted(fail_census.items()))
             or "none"), n_cert == n_lad, kill="K2")
    print("    F0 census (typed, CCLXXXI A12 restated): %d/%d F0 "
          "cells fail the ladder-frozen ENTRY BOX -- they are NOT "
          "members of the box-restricted class; their floor "
          "vectors enter the catalog as class data only; kz-45 "
          "h=1359 is covered by the CITED CCLXXIX/CCLXXXV "
          "individual K=5 certificate" % (n_f0_box, n_f0))
    check("O2 certified lower bound sup >= %.6f (%s) vs CCLXXXV "
          "numeric sup %.6f (rel %.2e <= %.0e)"
          % (lb_cert, lb_arg, SUP_TF_REF,
             abs(lb_cert / SUP_TF_REF - 1.0) if math.isfinite(
                 lb_cert) else float("nan"), LB_RTOL),
          math.isfinite(lb_cert)
          and (SMOKE or abs(lb_cert / SUP_TF_REF - 1.0) <= LB_RTOL),
          kill="K3")

    # ---- X: controls must fire
    section("X -- controls")
    th_ctrl = np.asarray(rows[i_hot]["theta"], float).copy()
    th_ctrl[0] = CTRL_B1
    _f, c_lo_v, c_hi_v, _fl = work.point_certify(th_ctrl)
    lam1 = float(np.linalg.eigvalsh(
        rc.theta_matrices(th_ctrl)[0])[0])
    check("G5 CONTROL certified enclosure at the declared "
          "indefinite theta (lambda_min %.4f): tr R in [%.6f, "
          "%.6f], lower end >= 1" % (lam1, c_lo_v, c_hi_v),
          c_lo_v >= 1.0, kill="K4")
    th_bad = np.asarray(rows[i_hot]["theta"], float)
    lo_bad = th_bad[None, :].copy()
    hi_bad = th_bad[None, :].copy()
    lo_bad[0, 1] = CTRL_B2 - 0.5
    hi_bad[0, 1] = CTRL_B2
    (_jmn, ok_lb_x, _jmx, ok_ub_x, _bad_x,
     neg_x) = r2.sigma_corner_iv(lo_bad, hi_bad)
    check("X2 CONTROL corner-CF on a box with b_2 in [%.1f, %.1f] "
          "< 0: both corners REFUSED and the pivot-condensation "
          "prune FIRES (%s)"
          % (CTRL_B2 - 0.5, CTRL_B2, bool(neg_x[0])),
          (not ok_lb_x[0]) and (not ok_ub_x[0]) and bool(neg_x[0]),
          kill="K4")
    # X3: the ordered-floor prune, and exactly it, kills a truth box
    cat_far = dict(cat)
    cat_far = dict(f_lo=cat["f_lo"] * CTRL_CAT_SCALE,
                   f_hi=cat["f_hi"] * CTRL_CAT_SCALE,
                   sg=cat["sg"].copy(), sha="control", n=cat["n"])
    work_x3 = BoxWork3(cls, env, fdata, cat_far)
    th_pt = np.asarray(rows[i_hot]["theta"], float)
    _ub_x, keep_x, _sc_x, _v_x = work_x3.process(th_pt[None, :],
                                                 th_pt[None, :])
    others = sum(work_x3.stats[k] for k in work_x3.stats
                 if k.startswith("pr_") and k != "pr_floor")
    check("X3 CONTROL a certified truth point box against a "
          "doctored catalog (floors x %g) is PRUNED with pr_floor "
          "= %d and every other prune counter silent (%d)"
          % (CTRL_CAT_SCALE, work_x3.stats["pr_floor"], others),
          (not keep_x[0]) and work_x3.stats["pr_floor"] == 1
          and others == 0, kill="K4")
    # X5: overclaimed floors refuse the member's own certification
    cat_over = dict(f_lo=cat["f_lo"].copy(), f_hi=cat["f_hi"].copy(),
                    sg=cat["sg"].copy(), sha="control", n=cat["n"])
    cat_over["f_lo"][i_hot] = np.asarray(
        sorted(np.asarray(rows[i_hot]["lam_jb"], float)
               * CTRL_FLOOR_SCALE))
    cat_over["f_hi"][i_hot] = cat_over["f_lo"][i_hot] * (1 + 1e-6)
    work_x5 = BoxWork3(cls, env, fdata, cat_over)
    feas_o, _tl, _th2, fails_o = work_x5.point_certify_tf(
        rows[i_hot]["theta"], i_hot)
    check("X5 CONTROL overclaimed floors (%.2f x spectrum) REFUSE "
          "the member's own certification on the floor seat (%s)"
          % (CTRL_FLOOR_SCALE,
             ",".join(f for f in fails_o if "floor" in f) or "-"),
          (not feas_o) and any("floor" in f for f in fails_o),
          kill="K4")
    if rc.KILLS:
        return finish([])

    # ---- O: the main certified B&B
    section("O -- CERTIFIED BRANCH AND BOUND on the tight-floor "
            "class (cap = t_R = %.4f via Gauss-Radau; %d-branch "
            "catalog)" % (cls["t_r"], cat["n"]))
    print("    master box: CCLXXXI box with the typed pre-clips; "
          "DROP_FLOOR3 = %.4f, target ladder down to %.4f, budget "
          "%.0f s" % (DROP_FLOOR3, TARGETS3[-1], MAIN_BUDGET_S3))
    res = run_bnb3(work, master_lo, master_hi, MAIN_BUDGET_S3,
                   "main")
    st = res["stats"]
    print("    TREE: processed %d, pruned KS %d / COEF %d / eta %d "
          "/ MOM %d / pivot %d / B_floor %d / FLOOR-BRANCH %d / "
          "pivot-condensation %d / sigma %d / radius %d / SPREAD "
          "%d / empty-clip %d; dropped %d (floor %.4f); hard %d; "
          "open %d; stop=%s"
          % (st["processed"], st["pr_ks"], st["pr_coef"],
             st["pr_eta"], st["pr_mom"], st["pr_piv"],
             st["pr_bfloor"], st["pr_floor"], st["pr_pdneg"],
             st["pr_sigma"], st["pr_radius"], st["pr_spread"],
             st["pr_empty"], st["dropped"], res["floor_used"],
             res["n_hard"], res["n_open"], res["stop"]))
    print("    CURRENCY CENSUS: width-tolerant SG_eff bound the "
          "good seats on %d boxes, the per-seat enclosure on %d; "
          "corner-CF fallbacks lower %d / upper %d, legacy "
          "interval-CF refusals %d, SPREAD refusals %d; PD census "
          "full %d / mixed %d"
          % (st["sg_win"], st["enc_win"], st["ref_cflo"],
             st["ref_cfhi"], st["ref_cf"], st["ref_spread"],
             st["pd_full"], st["pd_mixed"]))
    for tgt, t_s, n_p in sorted(res["crossings"],
                                key=lambda c: -c[0]):
        print("    TARGET sup <= %.4f CERTIFIED after %.1f s / %d "
              "boxes" % (tgt, t_s, n_p))
    bound = res["bound"]
    if res["worst"] is not None:
        w_lo, w_hi, w_ub = res["worst"]
        w_mid = 0.5 * (w_lo + w_hi)
        print("    RESIDUAL REGION anatomy (worst box): UB %.6f, "
              "mid n %.6g a1 %.6g b2 %.6g sigma %.6g; widths "
              "max/med %.3g/%.3g"
              % (w_ub, w_mid[0], w_mid[NDIM], w_mid[1],
                 rc.sigma_quotient(w_mid),
                 float(np.max(w_hi - w_lo)),
                 float(np.median(w_hi - w_lo))))
    check("O1 certified global bound: sup tr R <= %.6f over the "
          "tight-floor class (certified window [%.6f, %.6f])"
          % (bound, lb_cert, bound), True)
    check("S1 tau/c_h relocation screens VACUOUS BY CONSTRUCTION "
          "(class-level certified bounds, no new per-step decision "
          "currency)", True)

    # ---- verdict
    labels = []
    used = ("box, a>=0, n>0, B_floor, KS_wall, COEF, SPREAD, "
            "radius, eta, MOM, sharp-pivot, ordered-floor branch "
            "catalog, sigma<=t_R (b_1>0)")
    if bound < 1.0 and not SMOKE:
        labels.append(
            "KSDUAL-TIGHTFLOOR-CERTIFIED(sup tr R <= %.6f < 1 "
            "CERTIFIED-INTERVAL-GLOBAL over the frozen tight-floor "
            "entry-data class: EVERY J in C_TF = CCLXXXI box (SHA "
            "%s...) + %s, floors from the frozen %d-branch catalog "
            "(SHA %s..., inherited 1e-6 quality bar), satisfies "
            "tr R < 1, hence R(lambda_1) < 1, hence lambda_1(J) > "
            "0 (R >= 1 on x <= 0, R >= 0 everywhere, CCXXV "
            "certified separator facts): every member is WALL-"
            "POSITIVE; truth membership CERTIFIED %d/%d ladder "
            "cells; certified window [%.6f, %.6f]; HONEST TYPING: "
            "the class margin is structurally capped at 1 - %.4f "
            "= %.4f by the thinnest truth rung; the floors are "
            "per-member certified data (exact Jacobi-Sturm / "
            "round-62 provenance); F0 cells sit outside the entry "
            "box (kz-45 by the cited two-tier fallback); NO all-h "
            "claim beyond the certified membership; tree %d boxes)"
            % (bound, cls["box_sha"][:8], used, cat["n"],
               cat["sha"][:8], n_cert, n_lad, lb_cert, bound,
               lb_cert, 1.0 - lb_cert, st["processed"]))
    elif lb_cert >= 1.0:
        labels.append(
            "KSDUAL-TIGHTFLOOR-LB-GEQ-1(certified feasible witness "
            "tr R >= %.6f >= 1)" % lb_cert)
    else:
        labels.append(
            "KSDUAL-STILL-OPEN(certified window [%.6f, %.6f] after "
            "the frozen budget%s; constraints: %s; tree %d boxes, "
            "stop=%s; residual anatomy printed above)"
            % (lb_cert, bound,
               " -- SMOKE geometry is degenerate by construction"
               if SMOKE else "", used, st["processed"],
               res["stop"]))
    labels.append(
        "CURRENCY-UPGRADE(width-tolerant per-member ordered-floor "
        "good-seat bound live: SG census %d/%d boxes, pr_floor %d; "
        "corrected interlacing clips deployed, the inherited "
        "defective clip disclosed as amendment A1 and excluded)"
        % (st["sg_win"], st["sg_win"] + st["enc_win"],
           st["pr_floor"]))
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
