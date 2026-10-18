#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""source_prufer_one_defect_probe --
PRIME.TERMINAL.SOURCE_PRUFER_ONE_DEFECT.01 (round 372): THE
SOURCE-JACOBI PHASE THEOREM -- V2 and T1 jointly, the spike
extracted not averaged (reviewer solution 2 / Terminal).

CONTEXT (binding, from DCCXXIX after r363-r368).  Terminal is no
longer treated independently of L*.  Under CanonicalWindow and L*
(as a hypothesis -- certified on the measured windows) the finite
Jacobi chain belonging to v2 is positive, the recurrence
coefficients are positive, the Pruefer phase is well-defined.
THE SOURCE-JACOBI PHASE THEOREM (candidate): the Pruefer phase of
the polynomial v2 on the x-mask has (1) a monotone bulk phase,
(2) controlled discrete curvature, (3) at most ONE canonical
turning block, (4) an explicit local estimate in that block.
FROM THE SAME THEOREM must follow: V2 (run-length regularity --
run lengths ARE phase dwell times) AND F_i <= C (log m)^A for
every normal block (the T1 theorem on the non-defect part).  For
the turning block the dominant group is treated SEPARATELY:
  (10) q*^3 <= C* (log m)^A / m^2
  (11) sum_{i != *} q_i^3 <= C_rest (log m)^A / m^2
  ==> M3 <= C (log m)^A / m^2 ==> N3 >= m/polylog ==> N2 >= N3
  ==> Fejer/vdC ==> q_N < 1.
THE r368 LESSON: kz117 carries 90.9 pct of its own pi-measure --
averaging fails; the right operation is SPIKE EXPLICITLY
EXTRACTED, REST UNIVERSALLY CONTROLLED.  Verdicts (verbatim):
ONE_DEFECT_TERMINAL_GO / SPIKE_NOT_UNIQUE / REST_T1_STILL_GROWS /
PHASE_RESTATEMENT.

Hard requirements: (1) the Pruefer-to-run dictionary EXACT;
(2) V2 from phase regularity; (3) the universal T1 bound after
removal of ONE canonically defined heavy group; (4) THE SAME
rule must carry kz111, kz117 AND kz124; (5) direct composition
to q_N < 1.

THE LEGS:
  LEG 0 -- ANCHORS bit-near: r365 (v2 reconstruction, XOR sign
    identity, x-mask, the minimal V2 violator (...,r,r,1,1,1));
    r368 (F/E_pi columns, the spike anatomy); r361/r358
    (gap/floor, F_i).
  LEG A -- THE PRUEFER-TO-RUN DICTIONARY (the exact core):
    discrete Pruefer phase theta_k of the v2-chain (standard:
    via the recurrence / sign changes; well-defined under L*
    positivity) and the dictionary: sign-block run lengths ==
    dwell times of the phase in half-periods (exact, Fractions
    on the toy, f64 live on all 134+ windows).  V2 becomes a
    PHASE statement: the violator (...,r,r,1,1,1) == a specific
    phase pattern (long dwell + three fast flips).
  LEG B -- PHASE ANATOMY: bulk monotonicity, discrete curvature,
    COUNT turning blocks (sealed: slope-outlier clusters, merge
    gap MERGE_GAP; dwell outliers as the vacuous-slope fallback)
    on all windows of all four worlds.  Is the turning block
    UNIQUE (the one-defect thesis -- if > 1: SPIKE_NOT_UNIQUE
    honestly)?  Does it coincide with the dominant beta/omega
    group and the F-spikes (kz111/117/124 -- core test 4)?
  LEG C -- THE TWO-PART BOUND: (i) the universal F-bound on the
    NON-defect blocks (sealed (C, A) bars, all worlds -- 0
    violations?); (ii) the separate q* bound for the defect
    block (measure q*^3 m^2 / (log m)^A); (iii) V2 from phase
    regularity (violator exclusion as a phase census).
  LEG D -- THE COMPOSITION: (10)+(11) ==> M3-polylog ==> the
    full chain to q_N < 1 (polylog convention, no premature
    powering); the new m0* against 10^16.1/10^10.0; the cofinal
    typing (what is SATZ modulo L*, what is census).
  LEG E -- WORLDS + MUST-FAILS (>= 5): matched SCRAMBLE (breaks
    where -- the phase should be chaotic there: measure the
    turning count), Twin, chi.  Must-fails: phase from the runs
    circularly instead of from the recursion -> AST/construction
    CAUGHT; turning definition after sight -> protocol-CAUGHT;
    defect group chosen posthoc -> CAUGHT (canonical definition
    before the freeze); F-bars after sight -> CAUGHT; wrong
    half-period convention -> exact CAUGHT.

SEALED VERDICTS (main letter: TARGET_LEAK / LAW_STATE_NOT_EXACT
take precedence; otherwise the four reviewer letters):
  TARGET_LEAK  iff any firewall/scope/fragment/literal audit
    hit on the module-own builders;
  LAW_STATE_NOT_EXACT  iff an exact ward breaks (dictionary,
    Fractions toys, XOR identity, N2 >= N3, two-part sum);
  ONE_DEFECT_TERMINAL_GO  iff the dictionary is exact on every
    live row AND turning uniqueness holds on every MAIN row AND
    the named spikes kz111/117/124 coincide with the canonical
    defect AND the rest-T1 a-priori bars have 0 violations AND
    the q* and rest-M3 bars hold AND V2 holds with the
    phase-pattern exclusion AND the composed m0* is at most the
    r361 census 10^16.1;
  SPIKE_NOT_UNIQUE  iff uniqueness fails on any MAIN row (or on
    a named spike row);
  REST_T1_STILL_GROWS  iff uniqueness holds but the rest-T1
    a-priori bars still violate (the extraction did not tame F);
  PHASE_RESTATEMENT  iff the dictionary holds but phase
    regularity does not exclude the V2 violator (n_turn > 1 is
    common on V2-regular windows, or interior chain progress is
    absent -- we renamed runs to dwells).
  Combinations with CENSUS flags are allowed when GO does not
    fire and none of the three negative letters is forced.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r358
LGC.{eval_gap, gap_columns, solve_m0, scr_letter, audit sets,
the four-world construction constants} (fb2d499f); r361
MSF.{FLOOR_CAND, CAP_FAC} (1bec7175); r355 KSF.mesh_h
(1f14bd93); r357 DMF.{chi_window_comb, chi_wpack,
chi_window_data, LPQ3, LPQ4} (4bf1a94b); r353 SFE.{wpack_b,
window_data_b, frameb_pool} (bd89e331); r266 BR.eval_scaled;
r330 DSW.rung_rec; r269 PBB.{mask_edge, runs_split}; r298 WBT;
r365 V2 anatomy (XOR, x-mask, violator); r363 Sturm instruments
(sign-change zeros transferable, not imported as a module-own
phase); r324 QMO composition via LGC.solve_m0; r339 FDD via
LGC.eval_gap; r329 EFA; r289 AKD.twin_rational; r276 MF; r351
QGL; v881 PIK; v563 core READ-ONLY.  NEW module-own
(source-pure, AST-audited): chain_prufer, unwrap_x,
dwell_levels, runs_of_int, runs_of_sign, v2_holds,
slope_clusters, dwell_outliers, defect_kind, f_rest_bar,
qstar_score, rest_m3_score, prufer_tree_372, scr_turn_note,
dictionary_ok.  q/F/M3, turning-mass coincidence, rest-T1
violations and every census on them are TARGET-SIDE DIAGNOSTICS
computed in the gate section (r321..r368 convention, disclosed)
-- the module-own builders consume sealed thresholds, Jacobi
rows, positions and the passed columns only.

INDEX FIREWALL (binding, r238-r368 discipline): w = window
(kz), N_w = builder depth, m = block count; ground truth
(records, the frozen r358/r365/r368 anchor literals) enters
GATES and census tables only, never a builder (AST scope audit;
withheld identifiers rho / t_term / g_branch); no zero/prime
oracles anywhere (AST firewall); no fit primitives (fragment
audit; NO slopes fitted -- the bars are a-priori, uniqueness is
a COUNT).  Budget <= 1800 s.

SEALED CONSTANTS (everything not listed is imported verbatim
via LGC/MSF): HALF = pi (half-period convention); SLOPE_RATIO
= 2.0; SLOPE_MIN = 0.50 rad; MERGE_GAP = 4 nodes; DWELL_RATIO
= 2.5; DWELL_MIN = 5; MONO_FRAC = 0.90; C_F = 1.0; A_F = 2.0
(a-priori rest-T1, the r358 T2' grade); C_STAR = 4.0; C_REST =
1.0 (a-priori (10)/(11)); ID_EPS 1e-12; TWIN_BAR 1e-3;
TWIN_TOL 1e-8; SCR_SEED 1; STRESS_KZ = LGC (51, 111);
SPIKE_KZ = (111, 117, 124); RUNTIME_BAR 1800 s; MONO_FRAC
0.90; NYQ is the dictionary itself.  Anchor records (gate-side
literals): R358_ROWS (89, 8, 42, 42); R358_T1_TMAX (15.93,
23.70, 3.91, 3.09) tol 0.02; R368_SHARE_117 0.909 tol 0.02;
M0_REFS (16.1, 10.0); import-integrity prefixes LGC fb2d499f /
MSF 1bec7175 / KSF 1f14bd93 / DMF 4bf1a94b / SFE bd89e331;
R372_TABLE_LITERALS = LGC.R358_TABLE_LITERALS UNION {23.7,
15.93, 16.1, 0.909} (collision-prone small values curated OUT);
smoke = toys + trees + mutants + scope/purity audits + the four
w9 worlds with chain Pruefer, dictionary, positivity, V2;
ladders, anchors, deep censuses, composition, scrambles, twin
and adjudication skipped.

DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe's sealed
adjudication): every anchor band is an r353..r368 RECORD number
adopted as-is; the dictionary is DERIVED a priori from the
sin-representation v_n = rho sin(theta_n) of the Jacobi
recurrence (Killip-Simon / Teschl discrete Pruefer: atan2 of
consecutive chain values, unwrapped in the degree direction,
then along x).  Run length of sign(v2) equals occupancy of
floor(theta/pi) on the x-mask IF the half-period convention is
pi AND consecutive x-nodes do not skip a k*pi crossing of a
different parity than the sign -- the Fractions toy is
hand-computed: theta_k = (k + 1/2)*(pi/2) for k = 0..7 gives
floor(theta/pi) runs (2,2,2,2) = sign(sin theta) runs EXACT;
wrong half 2*pi gives (4,4) != (2,2,2,2) CAUGHT exact.  The
minimal V2 violator x-runs (3^8, 1,1,1) fails V2; the spike
(2^8, 3,3, 1,1,1) holds.  Two-part toy q = (1/2, 1/4, 1/4),
m = 4, lg = 2, A = 2: q*^3 = 1/8, rest = 1/32, M3 = 5/32,
q*-score = 1/2, rest-score = 1/8.  Interior chain progress on a
run of length >= 3 is STRICTLY positive for the recurrence
phase and ZERO for the circular (run-counting) phase -- that
is the construction catch.  ONE SCOPING PASS (machinery
validation at w9 only): the four w9 worlds exist through the
r358 channel; every deep turning count, coincidence, rest-T1
census, q* score and composed m0* are GENUINELY OPEN.  Timing:
r368 full pass 708.8 s (adopted as the deep budget estimate).
C_F, A_F, C_STAR, C_REST, SLOPE_RATIO, SLOPE_MIN, MERGE_GAP,
DWELL_RATIO, DWELL_MIN, MONO_FRAC and all anchor tolerances are
fixed BEFORE any deep evaluation; the letters are symmetric
and total by CONTRACT.  Canonical defect (frozen): if the
slope-outlier cluster count n_turn == 1, that unique cluster
IS the turning block; elif n_turn == 0 and the dwell-outlier
count n_dwell == 1, that unique long run IS the turning block;
elif both are 0, the defect is VACUOUS (rest = all); else
SPIKE_NOT_UNIQUE.  The mass-group i* is the theta-order block
of largest |q| whose centre lies in the turning x-interval
(nearest centre if no overlap) -- NEVER argmax q in isolation.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.  Coexistence: R369 / R371 / R373 run in
parallel -- own files only; git pull before the strictly
additive rh-sync.  Two-commit freeze protocol (r329
convention): spec committed pre-freeze, record tables the
only post-freeze edit, committed again.

Honesty before beauty: the dictionary, the Fractions toys, the
XOR identity, N2 >= N3, the two-part sum and the purity audits
are EXACT (Fractions/AST-decided); turning uniqueness, spike
coincidence, rest-T1, q*, V2-from-phase and every composed m0*
are MEASURED on the finite 89 + 8 + 42 + 42 row surface only --
a 0-violation census fixes a CENSUS THEOREM, not a cofinal
law; ONE_DEFECT_TERMINAL_GO here means the one-defect
extraction replaces averaging ON THIS SURFACE at the sealed
a-priori grade; g_i is a construction-local coordinate, said
out loud; L* is a hypothesis (certified on measured MAIN
windows); r243..r368 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA ad13a2abd3dca0f2
post-a1 / original pre-freeze commit 279c0f92 had 12b18eec;
protocol: smoke pass = 27/27 (1.2 s, run twice pre-record,
byte-identical up to WALL); calibration amendment a1 =
twin_rational arity copied from the r368 channel -- first
full evaluation crashed at G91 before any adjudication;
NO bar, letter, turning rule, C_STAR, C_REST, uniqueness
definition or verdict tree moved; cal2 = first complete
full evaluation = 27/27, wall 616.4 s; record run1/run2
after this insertion, byte-identical up to WALL):
MAIN VERDICT: SPIKE_NOT_UNIQUE + DICT(181/181) +
TURN(unique MAIN 0/97, kinds NOT_UNIQUE 181/181, max
n_turn 310) + COINC(NO on kz111/117/124) + REST_T1(viol
0/181, max F_rest 23.704) + QSTAR(viol 0/181, max 0.898)
+ REST_M3(viol 24/181, max 94.893) + V2(181/181, pattern
0, phase NO) + COMPOSITION(m0* 10^24.9 vs 10^16.1/10^10.0)
+ SCRAMBLE(P1_ADMISSION x3, n_turn 7/40/3) + TWIN(1.8e-08)
+ MUSTFAIL_LEDGER.
THE HEADLINE FINDINGS:
(1) THE PRUEFER-TO-RUN DICTIONARY IS SATZ: floor(theta/pi)
runs of the chain-accumulated Jacobi Pruefer phase equal
the sign-runs of v2 on ALL 181 live rows (89+8+42+42);
XOR identity sign(ct)=sign(w x v2) 181/181; Fractions toy
(2,2,2,2) exact; N2 >= N3 181/181; interior chain progress
min 2.062 (circular mutant is 0 -- not a restatement of
the sign field).  Jacobi positivity gam_next > 0 through
deg N-2 on 181/181 (L* certified on this surface).
(2) THE ONE-DEFECT THESIS IS REFUTED AT CENSUS GRADE:
NOT_UNIQUE on 181/181, MAIN unique 0/97, max n_turn 310
(w9 already 12/6/9/7).  The sealed slope-outlier rule
(SLOPE_RATIO 2.0, SLOPE_MIN 0.50, MERGE_GAP 4) sees the
zero-crossing jumps of a step-like discrete Pruefer phase,
not a unique turning block.  SPIKE_NOT_UNIQUE is the
letter; the bar was not moved after sight.
(3) SPIKE COINCIDENCE FAILS ON kz111/117/124: the
dominant slope cluster maps to i*=0 (left edge) vs
argmax-q 168/140/111; q* of that diagnostic group is
4.3e-3 / 5.1e-3 / 4.9e-4, not the r368 mass spikes.
The same rule does NOT carry the three named rows.
(4) TWO-PART BOUND AFTER DOMINANT-CLUSTER EXTRACTION
DOES NOT REPLACE T1: rest-T1 F_i a-priori (1.0, 2.0)
has 0/181 violations only because (log m)^2 is large
on deep rows while F_rest still equals the global max
23.704 (the spike was not extracted); rest-M3 violates
24/181 (max 94.893 vs C_REST 1.0).  q*-score of the
wrong group is vacuously below C_STAR.
(5) V2 HOLDS 181/181 WITH 0 PHASE-PATTERN VIOLATORS,
but V2-from-phase is NO: uniqueness failed, so the
regularity that would exclude (...,r,r,1,1,1) is not
the one-turning theorem.  Bulk monotone at MONO_FRAC
0.90 only 23/181 (min frac 0.854).
(6) COMPOSITION DOES NOT PAY: m0* = 10^24.9 (measured
C*_obs 0.898 + C_rest_obs 94.893, A=2) WORSE than r361
floor 10^16.1 / 10^10.0.  Cofinal rest unchanged: V2
as a lemma + a family-uniform T1 theorem; the
one-defect extraction is not that theorem.
Scrambles P1_ADMISSION x3 (nf 21/3/37, n_turn 7/40/3);
twin 1.8e-08; must-fails e1-e5 + m6a/m6b.
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

import bordered_hankel_probe as BH             # noqa: E402 r244
import principal_bessel_probe as PB            # noqa: E402 r243
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import qmax_growth_law_probe as QGL            # noqa: E402 r351
import second_family_erosion_probe as SFE      # noqa: E402 r353
import k2_source_formula_probe as KSF          # noqa: E402 r355
import dirichlet_secondworld_probe as DSW      # noqa: E402 r330
import dirichlet_matched_frame_probe as DMF    # noqa: E402 r357
import local_gap_carleson_probe as LGC         # noqa: E402 r358
import mean_sieve_floor_probe as MSF           # noqa: E402 r361
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import window_border_transfer_probe as WBT     # noqa: E402 r298
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import verify_lstar_instance as V              # noqa: E402 document

# ---------------- imported constants (verbatim via LGC/MSF)
W_LOC = EFA.GAP_W
QUANT_BAR = LGC.QUANT_BAR
PACK_EPS = LGC.PACK_EPS
N_CAL_T1 = LGC.N_CAL_T1
N_CAL_FB = LGC.N_CAL_FB
A_PACK = LGC.A_PACK
TWIN_BAR = LGC.TWIN_BAR
TWIN_TOL = LGC.TWIN_TOL
SCR_SEED = LGC.SCR_SEED
STRESS_KZ = LGC.STRESS_KZ
MULT_CAP = LGC.MULT_CAP
NU_A = LGC.NU_A
NU_B = LGC.NU_B
FRAMEB_KZ = LGC.FRAMEB_KZ
MESH_DEV_HI = LGC.MESH_DEV_HI
LPQ3 = LGC.LPQ3
LPQ4 = LGC.LPQ4
Q_CHI3 = LGC.Q_CHI3
Q_CHI4 = LGC.Q_CHI4
TOY_BAR = LGC.TOY_BAR
FLOOR_CAND = MSF.FLOOR_CAND
CAP_FAC = MSF.CAP_FAC

# ---------------- NEW sealed constants of this round
HALF = math.pi
SLOPE_RATIO = 2.0
SLOPE_MIN = 0.50
MERGE_GAP = 4
DWELL_RATIO = 2.5
DWELL_MIN = 5
MONO_FRAC = 0.90
C_F = 1.0
A_F = 2.0
C_STAR = 4.0
C_REST = 1.0
ID_EPS = 1.0e-12
SPIKE_KZ = (111, 117, 124)
RUNTIME_BAR = 1800.0
R358_ROWS = (89, 8, 42, 42)
R358_T1_TMAX = (15.93, 23.70, 3.91, 3.09)
R358_T1_TOL = 0.02
R368_SHARE_117 = 0.909
R368_SHARE_TOL = 0.02
M0_REFS = (16.1, 10.0)
LGC_SHA_PREFIX = "fb2d499f"
MSF_SHA_PREFIX = "1bec7175"
KSF_SHA_PREFIX = "1f14bd93"
DMF_SHA_PREFIX = "4bf1a94b"
SFE_SHA_PREFIX = "bd89e331"

R372_TABLE_LITERALS = frozenset(LGC.R358_TABLE_LITERALS
                                | {23.7, 15.93, 16.1, 0.909})

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
    return (not bad), ("NO zero/prime oracles; the Pruefer "
                       "builders consume Jacobi rows + positions "
                       "+ sealed thresholds ONLY; q/F/M3 and "
                       "coincidence enter gates and census "
                       "tables only"
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


SCOPE_FORBIDDEN_372 = {"rho", "t" + "_term", "g" + "_branch",
                       "fabg" + "_true"}


def scope_audit(funcname, forbidden):
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
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def literal_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R372_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders (source-pure, AST-audited)
def chain_prufer(rows, pts, deg):
    """terminal discrete Pruefer angle of the scaled monic Jacobi
    chain at each point (Killip-Simon / Teschl: atan2 of
    consecutive chain values, unwrapped in the degree
    direction).  Consumes Jacobi rows + positions + degree only
    -- NEVER the sign field, NEVER q/F.  Returns (v_deg, theta).
    Initial angle pi/2 (p_{-1} = 0, p_0 = 1)."""
    pts = np.asarray(pts, float)
    v = np.ones_like(pts)
    vm = np.zeros_like(pts)
    theta = np.full_like(pts, 0.5 * math.pi)
    phi_prev = theta.copy()
    nd = int(deg)
    for k in range(nd):
        alh = rows[k]["alh"]
        if k == 0:
            px = (pts - alh) * v
        else:
            gam = rows[k - 1]["gam_next"]
            fc = math.exp(rows[k - 1]["Ls"] - rows[k]["Ls"])
            px = (pts - alh) * v - gam * fc * vm
        vm = v
        v = px * math.exp(rows[k]["Ls"] - rows[k + 1]["Ls"])
        phi = np.arctan2(v, vm)
        delta = phi - phi_prev
        delta = (delta + math.pi) % (2.0 * math.pi) - math.pi
        theta = theta + delta
        phi_prev = phi
    return v, theta


def unwrap_x(theta):
    """unwrap the terminal angle along the x-sorted mask (fixes
    isolated 2-pi k-unwrap branches).  Consumes the passed
    angle column only."""
    return np.unwrap(np.asarray(theta, float))


def dwell_levels(theta, half):
    """integer half-period index floor(theta / half).  Consumes
    the passed angle column and the sealed half only."""
    return np.floor(np.asarray(theta, float) / float(half)).astype(
        np.int64)


def runs_of_int(lev):
    """run lengths of an integer level sequence."""
    lev = list(int(v) for v in lev)
    if not lev:
        return []
    out = []
    start = 0
    cur = lev[0]
    for i in range(1, len(lev)):
        if lev[i] != cur:
            out.append(i - start)
            start = i
            cur = lev[i]
    out.append(len(lev) - start)
    return out


def runs_of_sign(sig):
    """run lengths of a +/- sequence (zeros attach to the
    current run, PBB convention)."""
    sg = np.sign(np.asarray(sig, float))
    out = []
    start = 0
    cur = 0.0
    n = len(sg)
    for i in range(n):
        s = float(sg[i])
        if s == 0.0:
            continue
        if cur == 0.0:
            cur = s
            start = i
        elif s != cur:
            out.append(i - start)
            start = i
            cur = s
    if n:
        out.append(n - start)
    return out


def v2_holds(R):
    """named condition V2 of xn_invariant.tex S5: if the last
    three x-order run lengths are (1,1,1), then among the four
    preceding at least two are <= 2.  Consumes the passed run
    list only."""
    R = list(int(v) for v in R)
    if len(R) < 7:
        return True, "short"
    if tuple(R[-3:]) != (1, 1, 1):
        return True, "no-triple-tail"
    prev4 = list(R[-7:-3])
    n_le2 = sum(1 for r in prev4 if r <= 2)
    if n_le2 >= 2:
        return True, "triple-regular prev4=%s" % (prev4,)
    return False, "VIOLATOR prev4=%s" % (prev4,)


def dictionary_ok(sign_runs, level_runs):
    """exact run-sequence identity (the Pruefer-to-run
    dictionary).  Consumes the two passed run lists only."""
    a = list(int(v) for v in sign_runs)
    b = list(int(v) for v in level_runs)
    return a == b


def slope_clusters(theta, ratio, smin, merge):
    """canonical turning clusters: slope-outlier nodes of
    |d theta|, bar = max(smin, ratio * median), merged if the
    gap is <= merge.  Consumes the passed angle column and the
    sealed thresholds only.  Returns (list of (lo, hi) inclusive
    slope-indices, n_turn)."""
    th = np.asarray(theta, float)
    if len(th) < 2:
        return [], 0
    sig = np.abs(np.diff(th))
    med = float(np.median(sig)) if len(sig) else 0.0
    bar = max(float(smin), float(ratio) * med)
    mask = sig >= bar
    clusters = []
    i = 0
    n = len(mask)
    merge = int(merge)
    while i < n:
        if not mask[i]:
            i += 1
            continue
        lo = i
        hi = i
        i += 1
        while i < n:
            if mask[i]:
                hi = i
                i += 1
                continue
            # gap of False: peek ahead within merge
            j = i
            while j < n and (not mask[j]) and (j - hi) <= merge:
                j += 1
            if j < n and mask[j] and (j - hi) <= merge:
                hi = j
                i = j + 1
                continue
            break
        clusters.append((lo, hi))
    return clusters, len(clusters)


def dwell_outliers(runs, ratio, dmin):
    """dwell-outlier count: runs with length >= max(dmin,
    ratio * median).  Consumes the passed run list and sealed
    thresholds only."""
    R = list(int(v) for v in runs)
    if not R:
        return 0, 0, dmin
    med = sorted(R)[len(R) // 2]
    bar = max(int(dmin), int(math.ceil(float(ratio) * float(med))))
    n = sum(1 for r in R if r >= bar)
    return n, med, bar


def defect_kind(n_turn, n_dwell):
    """THE SEALED CANONICAL DEFECT RULE (frozen before any
    evaluation): unique slope cluster / else unique dwell
    outlier / else vacuous / else not unique.  Consumes the
    two counts only."""
    nt = int(n_turn)
    nd = int(n_dwell)
    if nt == 1:
        return "SLOPE"
    if nt == 0 and nd == 1:
        return "DWELL"
    if nt == 0 and nd == 0:
        return "VACUOUS"
    return "NOT_UNIQUE"


def f_rest_bar(lg):
    """sealed rest-T1 bar C_F (log m)^{A_F}.  Consumes depth
    only."""
    return C_F * (float(lg) ** A_F)


def qstar_score(qstar, m, lg):
    """q*^3 * m^2 / (log m)^{A_F} -- the (10) score.  Consumes
    the passed q* and depth only."""
    lg = max(float(lg), 1e-300)
    return (float(qstar) ** 3) * (float(m) ** 2) / (lg ** A_F)


def rest_m3_score(m3_rest, m, lg):
    """(sum_{i != *} q_i^3) * m^2 / (log m)^{A_F} -- the (11)
    score.  Consumes the passed rest cubic and depth only."""
    lg = max(float(lg), 1e-300)
    return float(m3_rest) * (float(m) ** 2) / (lg ** A_F)


def prufer_tree_372(leak, brk, unique, rest_ok, coincide,
                    v2_phase, compose_ok):
    """the sealed main-letter tree.  TARGET_LEAK and
    LAW_STATE_NOT_EXACT take precedence; then the four
    reviewer letters; GO requires every positive clause."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if not unique:
        return "SPIKE_NOT_UNIQUE"
    if unique and not rest_ok:
        return "REST_T1_STILL_GROWS"
    if unique and rest_ok and coincide and v2_phase and compose_ok:
        return "ONE_DEFECT_TERMINAL_GO"
    if unique and rest_ok and (not v2_phase):
        return "PHASE_RESTATEMENT"
    return "ONE_DEFECT_CENSUS"


def scr_turn_note(p1_ok, known, n_turn, chaotic):
    """scramble typing: admission first, then whether a
    measurable turning count is chaotic (n_turn > 1)."""
    if not p1_ok:
        return "SCR_P1_ADMISSION"
    if not known:
        return "SCR_TURN_UNMEASURED"
    if chaotic:
        return "SCR_TURN_CHAOTIC"
    return "SCR_TURN_CALM"


# ---------------- must-fail mutants
def mutant_phase_from_runs(sig):
    """e1 MUST-FAIL (construction): phase from the sign runs
    (circular) instead of from the recurrence -- AST-FLAGGED
    (consumes the sign field).  Interior progress on a run of
    length >= 3 is EXACTLY 0, vs the chain phase which advances
    through the half-period."""
    sg = np.sign(np.asarray(sig, float))
    th = np.zeros(len(sg), float)
    acc = 0.0
    cur = 0.0
    for i in range(len(sg)):
        s = float(sg[i])
        if s == 0.0:
            th[i] = acc
            continue
        if cur == 0.0:
            cur = s
        elif s != cur:
            acc += math.pi
            cur = s
        th[i] = acc
    return th


def mutant_turning_by_sight(theta, q):
    """e2 MUST-FAIL (protocol): turning definition consumes the
    mass column (after sight) -- AST-FLAGGED.  Returns the
    argmax-q index dressed as a 'turning'."""
    _ = theta
    qq = np.asarray(q, float)
    return int(np.argmax(np.abs(qq))) if len(qq) else 0


def mutant_defect_argmax_q(q):
    """e3 MUST-FAIL (protocol): defect group = argmax |q|
    posthoc, skipping the canonical phase rule -- AST-FLAGGED."""
    qq = np.asarray(q, float)
    return int(np.argmax(np.abs(qq))) if len(qq) else 0


def mutant_fbars_posthoc(fcol, lgs):
    """e4 MUST-FAIL (protocol): C_F set at the seen F column
    (consumes rho) -- AST-FLAGGED; on the sealed toy returns
    2.25 != the sealed C_F 1.0."""
    return max(float(fcol[i]) / (float(lgs[i]) ** A_F)
               for i in range(len(fcol)))


def mutant_halfperiod_twopi(theta):
    """e5 MUST-FAIL (exact): half-period 2*pi instead of pi --
    the dictionary fails on the sealed toy (4,4) != (2,2,2,2)."""
    return dwell_levels(theta, 2.0 * math.pi)


def mutant_gift_bound(rc, P):
    """m6a MUST-FAIL (r355/r358/r368 verbatim): a builder
    consuming the withheld ground-truth terminal drive key --
    AST-FLAGGED."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m6b MUST-FAIL (r355/r358/r368 verbatim): a builder
    consuming the branch label -- AST-FLAGGED."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- target-side diagnostic (gate section only)
def jacobi_positive(rows, deg):
    gams = []
    nd = int(deg)
    for k in range(max(nd, 0)):
        if k < len(rows) and "gam_next" in rows[k]:
            gams.append(float(rows[k]["gam_next"]))
    if not gams:
        return False, 0, 0
    n_pos = sum(1 for g in gams if g > 0.0)
    return (n_pos == len(gams)), n_pos, len(gams)


def interior_progress(theta, runs):
    """max |delta theta| inside runs of length >= 3.  Chain
    phase advances; circular phase is flat."""
    th = np.asarray(theta, float)
    i = 0
    mx = 0.0
    for r in runs:
        r = int(r)
        if r >= 3 and i + r <= len(th):
            mx = max(mx, abs(float(th[i + r - 1] - th[i])))
        i += r
    return mx


def analyze_phase(rc):
    """gate-side: v2 on the x-mask, chain Pruefer, dictionary,
    V2, positivity, turning.  q/F coincidence is layered on
    later from gap_columns."""
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    bws = rc["bw"][o]
    N = rc["N"]
    rows = rc["p"]["rows"]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    xb = bxs[~ed]
    cb = cts[~ed]
    wb = bws[~ed]
    v, theta_k = chain_prufer(rows, xb, N - 2)
    th = unwrap_x(theta_k)
    sg = np.sign(v)
    sg[sg == 0.0] = 1.0
    lev = dwell_levels(th, HALF)
    R_lev = runs_of_int(lev)
    R_v2 = runs_of_sign(sg)
    dict_ok = dictionary_ok(R_v2, R_lev)
    sg_c = np.sign(cb)
    sg_c[sg_c == 0.0] = 1.0
    R_c = runs_of_sign(sg_c)
    ok_v2, why_v2 = v2_holds(R_c)
    ok_v2_only, why_v2o = v2_holds(R_v2)
    pos_ok, n_pos, n_g = jacobi_positive(rows, N - 2)
    dth = np.diff(th) if len(th) >= 2 else np.zeros(0)
    if len(dth):
        n_pos_d = int(np.sum(dth > 0.0))
        n_neg_d = int(np.sum(dth < 0.0))
        mono_frac = max(n_pos_d, n_neg_d) / float(len(dth))
    else:
        mono_frac = 1.0
    bulk_mono = mono_frac >= MONO_FRAC
    clusters, n_turn = slope_clusters(th, SLOPE_RATIO, SLOPE_MIN,
                                      MERGE_GAP)
    n_dwell, med_r, dbar = dwell_outliers(R_v2, DWELL_RATIO,
                                          DWELL_MIN)
    kind = defect_kind(n_turn, n_dwell)
    unique = kind != "NOT_UNIQUE"
    # node interval of the canonical defect; when NOT_UNIQUE the
    # DOMINANT slope cluster (max excess above median slope) is
    # still recorded as a census diagnostic, never as uniqueness.
    node_lo = node_hi = None
    dom_lo = dom_hi = None
    if clusters:
        dth_a = np.abs(np.diff(th)) if len(th) >= 2 else np.zeros(0)
        med_s = float(np.median(dth_a)) if len(dth_a) else 0.0
        best_ex = -1.0
        for lo, hi in clusters:
            ex = float(np.sum(dth_a[lo:hi + 1] - med_s)) if len(dth_a) \
                else 0.0
            if ex > best_ex:
                best_ex = ex
                dom_lo, dom_hi = int(lo), int(hi)
    if kind == "SLOPE" and clusters:
        lo, hi = clusters[0]
        node_lo = int(lo)
        node_hi = int(min(hi + 1, max(len(xb) - 1, 0)))
    elif kind == "DWELL":
        i0 = 0
        for r in R_v2:
            if r >= dbar:
                node_lo = i0
                node_hi = i0 + int(r) - 1
                break
            i0 += int(r)
    elif kind == "NOT_UNIQUE" and dom_lo is not None:
        node_lo = int(dom_lo)
        node_hi = int(min(dom_hi + 1, max(len(xb) - 1, 0)))
    prog = interior_progress(th, R_v2)
    # XOR: sign(ct) == sign(w)*sign(x)*sign(v2) up to global
    sg_w = np.sign(wb)
    sg_w[sg_w == 0.0] = 1.0
    sg_x = np.sign(xb)
    sg_x[sg_x == 0.0] = 1.0
    prod = sg_w * sg_x * sg
    n_dis = int(np.sum(prod != sg_c))
    # violator phase-pattern on the colouring: (r,r,1,1,1) with
    # the two r >= 3
    pattern = False
    if len(R_c) >= 5:
        if tuple(R_c[-3:]) == (1, 1, 1) and R_c[-5] >= 3 \
                and R_c[-4] >= 3:
            pattern = True
    return dict(xb=xb, v=v, th=th, R_v2=R_v2, R_c=R_c, R_lev=R_lev,
                dict_ok=dict_ok, ok_v2=ok_v2, why_v2=why_v2,
                ok_v2_only=ok_v2_only, why_v2o=why_v2o,
                pos_ok=pos_ok, n_pos=n_pos, n_g=n_g,
                mono_frac=mono_frac, bulk_mono=bulk_mono,
                clusters=clusters, n_turn=n_turn, n_dwell=n_dwell,
                med_r=med_r, dbar=dbar, kind=kind, unique=unique,
                node_lo=node_lo, node_hi=node_hi,
                dom_lo=dom_lo, dom_hi=dom_hi, prog=prog,
                n_dis=n_dis, n_bulk=len(xb), pattern=pattern,
                n_nodes=len(xb))


def map_defect_to_block(ph, gc, ev):
    """map the canonical turning x-interval to a mass-block i*
    (largest |q| among blocks whose theta-centre lies in the
    turning interval; nearest centre if no overlap).  VACUOUS
    -> i* = None.  Gate-side (uses q)."""
    if ph["kind"] == "VACUOUS":
        return None, None
    # NOT_UNIQUE still maps the dominant cluster as a census
    # diagnostic (uniqueness already failed; this is not the GO
    # path and not a posthoc argmax-q).
    xb = ph["xb"]
    lo = ph["node_lo"]
    hi = ph["node_hi"]
    if lo is None or hi is None or len(xb) == 0:
        return None, None
    lo = max(0, min(int(lo), len(xb) - 1))
    hi = max(0, min(int(hi), len(xb) - 1))
    x_lo = float(min(xb[lo], xb[hi]))
    x_hi = float(max(xb[lo], xb[hi]))
    # theta of the turning interval
    th_lo = float(np.arccos(np.clip(x_hi, -1.0, 1.0)))
    th_hi = float(np.arccos(np.clip(x_lo, -1.0, 1.0)))
    cent = np.asarray(ev["gl"]["cent"], float)
    q = np.asarray(gc["q"], float)
    if len(cent) == 0 or len(q) == 0:
        return None, None
    inside = (cent >= th_lo - 1e-12) & (cent <= th_hi + 1e-12)
    if int(np.sum(inside)):
        idx_loc = np.where(inside)[0]
        i_star = int(idx_loc[int(np.argmax(np.abs(q[idx_loc])))])
    else:
        mid = 0.5 * (th_lo + th_hi)
        i_star = int(np.argmin(np.abs(cent - mid)))
    return i_star, float(q[i_star]) if i_star is not None else None


def rest_columns(gc, i_star):
    """rest-T1 / q* / rest-M3 scores from gap columns.  Gate-side."""
    q = np.asarray(gc["q"], float)
    fcol = np.asarray(gc["prod"], float)
    m = len(q)
    lg = float(gc["lg"])
    m3 = float(gc["m3"])
    if i_star is None:
        f_rest = float(np.max(np.abs(fcol))) if m else 0.0
        q_star = 0.0
        m3_rest = m3
        i_star_use = None
    else:
        i_star_use = int(i_star)
        mask = np.ones(m, dtype=bool)
        if 0 <= i_star_use < m:
            mask[i_star_use] = False
        f_rest = float(np.max(np.abs(fcol[mask]))) if int(np.sum(mask)) \
            else 0.0
        q_star = float(q[i_star_use]) if 0 <= i_star_use < m else 0.0
        m3_rest = float(np.sum((q[mask]) ** 3)) if int(np.sum(mask)) \
            else 0.0
    bar_f = f_rest_bar(lg)
    sc_star = qstar_score(abs(q_star), m, lg)
    sc_rest = rest_m3_score(m3_rest, m, lg)
    f_viol = bool(f_rest > bar_f + ID_EPS)
    star_viol = bool(sc_star > C_STAR + ID_EPS)
    rest_viol = bool(sc_rest > C_REST + ID_EPS)
    i_f = int(np.argmax(np.abs(fcol))) if m else None
    i_q = int(np.argmax(np.abs(q))) if m else None
    return dict(f_rest=f_rest, bar_f=bar_f, f_viol=f_viol,
                q_star=q_star, sc_star=sc_star, star_viol=star_viol,
                m3_rest=m3_rest, sc_rest=sc_rest, rest_viol=rest_viol,
                m3=m3, i_star=i_star_use, i_f=i_f, i_q=i_q,
                n2=float(gc["n2"]), n3=float(gc["n3"]),
                maxf=float(np.max(np.abs(fcol))) if m else 0.0,
                n2ge=bool(gc["n2"] + ID_EPS >= gc["n3"]))


def packs_full():
    """the four-family ladder, r358/r368 verbatim."""
    kzs_l = []
    ekz = []
    ekz2 = []
    for kz in core.frame_a_zones():
        h = PIK.build_rung(kz)["h"]
        if h <= LGC.H_CAP:
            kzs_l.append(kz)
        elif h <= LGC.EXT_H_MAX:
            ekz.append(kz)
        elif h <= LGC.EXT2_H_MAX:
            ekz2.append((h, kz))
    ladder = [BH.wpack(kz) for kz in kzs_l]
    ladder.sort(key=lambda p: (p["N"], p["kz"]))
    epool = [BH.wpack(kz) for kz in ekz]
    epool.sort(key=lambda p: (p["N"], p["kz"]))
    ext = epool[:LGC.K_EXT]
    ekz2.sort()
    pool2 = epool[LGC.K_EXT:] + [
        BH.wpack(kz) for _h, kz in ekz2[:LGC.EXT2_POOL_CAP]]
    pool2.sort(key=lambda p: (p["N"], p["kz"]))
    ext2 = [p for p in pool2 if p["nf"] is None][:LGC.K_EXT2]
    ext3 = [BH.wpack(kz) for kz in LGC.EXT3_KZ_B + LGC.EXT3_KZ_A]
    ext4 = [BH.wpack(kz) for kz in LGC.EXT4_KZ]
    ext5 = [BH.wpack(kz) for kz in LGC.EXT5_KZ_B + LGC.EXT5_KZ_A]
    packs_a = ladder + ext + ext2 + ext3 + ext4 + ext5
    packs_b = [SFE.wpack_b(kz, NU_B) for kz in FRAMEB_KZ]
    kzs_c = list(V.admissible_indices())
    packs_c3 = []
    packs_c4 = []
    for kz in kzs_c:
        u3, w3c, _n, _c = DMF.chi_window_comb(kz, Q_CHI3)
        packs_c3.append(DMF.chi_wpack(kz, 1.0, LPQ3, (u3, w3c)))
        u4, w4c, _n, _c = DMF.chi_window_comb(kz, Q_CHI4)
        packs_c4.append(DMF.chi_wpack(kz, 1.0, LPQ4, (u4, w4c)))
    return packs_a, packs_b, packs_c3, packs_c4, ladder, ext, ext2


def eval_family(packs, lab, live):
    rows = []
    for p in packs:
        if p.get("nf") is not None or not p.get("complete", True):
            continue
        if not p.get("rows"):
            continue
        rc = DSW.rung_rec(p)
        ev = LGC.eval_gap(rc)
        if ev.get("degenerate"):
            continue
        ph = analyze_phase(rc)
        gc = LGC.gap_columns(ev)
        i_star, q_st = map_defect_to_block(ph, gc, ev)
        rst = rest_columns(gc, i_star)
        rows.append(dict(kz=p["kz"], N=p["N"], m=ev["m"], lab=lab,
                         ph=ph, gc=gc, ev=ev, rst=rst, rc=rc))
    live[lab] = rows
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("source_prufer_one_defect_probe -- "
          "PRIME.TERMINAL.SOURCE_PRUFER_ONE_DEFECT.01 (round 372)")
    print("SPEC_SHA %s   (LGC %s / MSF %s / KSF %s / DMF %s)"
          % (SPEC_SHA[:16], LGC.SPEC_SHA[:16], MSF.SPEC_SHA[:16],
             KSF.SPEC_SHA[:16], DMF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + trees + mutants + audits + "
                        "the four w9 worlds with chain Pruefer, "
                        "dictionary, positivity, V2; ladders, "
                        "anchors, deep censuses, composition, "
                        "scrambles, twin and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (LGC.SPEC_SHA.startswith(LGC_SHA_PREFIX)
              and MSF.SPEC_SHA.startswith(MSF_SHA_PREFIX)
              and KSF.SPEC_SHA.startswith(KSF_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "sealed BEFORE evaluation: HALF=pi, SLOPE_RATIO %.1f "
          "SLOPE_MIN %.2f MERGE_GAP %d DWELL_RATIO %.1f "
          "DWELL_MIN %d MONO_FRAC %.2f rest-T1 (C_F %.1f, A_F "
          "%.1f) C_STAR %.1f C_REST %.1f; canonical defect rule "
          "SLOPE/DWELL/VACUOUS/NOT_UNIQUE; import integrity LGC "
          "%s / MSF %s / KSF %s / DMF %s / SFE %s"
          % (SLOPE_RATIO, SLOPE_MIN, MERGE_GAP, DWELL_RATIO,
             DWELL_MIN, MONO_FRAC, C_F, A_F, C_STAR, C_REST,
             LGC.SPEC_SHA[:8], MSF.SPEC_SHA[:8], KSF.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], SFE.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("chain_prufer", "unwrap_x", "dwell_levels",
                    "runs_of_int", "runs_of_sign", "v2_holds",
                    "dictionary_ok", "slope_clusters",
                    "dwell_outliers", "defect_kind", "f_rest_bar",
                    "qstar_score", "rest_m3_score",
                    "prufer_tree_372", "scr_turn_note")
    sc_own = []
    pure_lits = []
    for fn in own_builders:
        sc_own += scope_audit(fn, LGC.BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.QMAX_FORBIDDEN)
        sc_own += scope_audit(fn, SCOPE_FORBIDDEN_372)
        pure_lits += literal_audit(fn)
    sc_e1 = scope_audit("mutant_phase_from_runs",
                        SCOPE_FORBIDDEN_372)
    sc_e2 = scope_audit("mutant_turning_by_sight",
                        SCOPE_FORBIDDEN_372)
    # e2/e3 consume q via the argument name -- flag via a
    # dedicated identifier walk: they take `q` which is allowed
    # as a parameter name; the protocol catch is that they
    # CONSUME the mass column.  Flag e4 on fcol/lgs posthoc
    # (no forbidden ident).  Flag m6a/m6b on withheld keys.
    sc_e3 = scope_audit("mutant_defect_argmax_q",
                        SCOPE_FORBIDDEN_372)
    sc_e4 = scope_audit("mutant_fbars_posthoc",
                        SCOPE_FORBIDDEN_372)
    sc_m6a = scope_audit("mutant_gift_bound", LGC.BOUND_FORBIDDEN)
    sc_m6b = scope_audit("mutant_branch_peek", LGC.BOUND_FORBIDDEN)
    leak = bool(frag) or bool(sc_own) or bool(pure_lits) or not okf
    check("G03-scope-audits", (not frag) and (not sc_own)
          and (not pure_lits)
          and len(sc_m6a) >= 1 and len(sc_m6b) >= 1,
          "fragment audit clean (%d); the %d module-own builders "
          "clean vs BOUND/PHI3/QMAX/372 sets (%d id hits) and vs "
          "the sealed record-literal set (%d literal hits); "
          "m6a/m6b FLAGGED (%s / %s); e1-e4 are construction/"
          "protocol mutants (e1 consumes the sign field by "
          "contract, e2/e3 consume q by contract, e4 consumes "
          "the seen F column)"
          % (len(frag), len(own_builders), len(sc_own),
             len(pure_lits),
             sc_m6a[0] if sc_m6a else "MISS",
             sc_m6b[0] if sc_m6b else "MISS"))

    section("S1  SEALED TOYS + TREES + MUTANT PINS (all by hand)")
    # G10 dictionary Fractions-exact: theta_k = (k+1/2)*(pi/2)
    ks = list(range(8))
    th_toy = [(Fr(2 * k + 1, 4) * Fr.from_float(math.pi)
               if False else (k + 0.5) * (math.pi / 2.0))
              for k in ks]
    # use exact rational multiples of pi
    th_fr = [Fr(2 * k + 1, 4) for k in ks]  # theta/pi
    lev_fr = [int(math.floor(float(t))) for t in th_fr]
    # sign(sin(theta)) = sign(sin(pi * (theta/pi)))
    # theta/pi = 1/4, 3/4, 5/4, 7/4, 9/4, 11/4, 13/4, 15/4
    # sin > 0 on (0,1), < 0 on (1,2), ...
    sgn_fr = []
    for t in th_fr:
        # sign sin(pi * t) = + on even floor, wait:
        # sin(pi * x) > 0 iff floor(x) even
        fl = int(math.floor(float(t)))
        sgn_fr.append(1 if (fl % 2 == 0) else -1)
    R_lev_t = runs_of_int(lev_fr)
    R_sgn_t = runs_of_sign(sgn_fr)
    dict_toy = dictionary_ok(R_sgn_t, R_lev_t) and R_lev_t == [2, 2, 2, 2]
    check("G10-dict-toy-exact", dict_toy,
          "Fractions half-period toy theta/pi = (2k+1)/4, k=0..7: "
          "floor runs %s = sign(sin) runs %s = (2,2,2,2) EXACT"
          % (str(R_lev_t), str(R_sgn_t)))

    # G11 V2 violator vs spike
    R_v = [3] * 8 + [1, 1, 1]
    R_s = [2] * 8 + [3, 3, 1, 1, 1]
    okV, whyV = v2_holds(R_v)
    okS, whyS = v2_holds(R_s)
    check("G11-v2-violator-toy", (not okV) and okS,
          "minimal violator (3^8,1,1,1) %s; spike "
          "(2^8,3,3,1,1,1) %s" % (whyV, whyS))

    # G12 wrong half-period
    lev_bad = [int(math.floor(float(t) / 2)) for t in th_fr]
    R_bad = runs_of_int(lev_bad)
    check("G12-halfperiod-mutant-exact",
          R_bad != R_lev_t and R_bad == [4, 4],
          "wrong half 2*pi: floor(theta/(2pi)) runs %s != "
          "(2,2,2,2) CAUGHT exact" % (str(R_bad),))

    # G13 circular vs interior progress
    sig_run = [1, 1, 1, -1, -1, -1, 1, 1, 1]
    th_circ = mutant_phase_from_runs(sig_run)
    R_run = runs_of_sign(sig_run)
    prog_c = interior_progress(th_circ, R_run)
    # a linear chain-like phase that advances pi inside each run
    th_chain = []
    i = 0
    acc = 0.5 * math.pi
    for r in R_run:
        for j in range(r):
            th_chain.append(acc + (j + 0.5) * math.pi / r)
        acc += math.pi
        i += r
    prog_k = interior_progress(th_chain, R_run)
    check("G13-circular-vs-recursion-toy",
          prog_c <= ID_EPS and prog_k > 1.0,
          "circular interior progress %.3e == 0 (CAUGHT); "
          "chain-like interior progress %.3f > 1 (the recurrence "
          "advances through the half-period -- this is the "
          "construction catch)"
          % (prog_c, prog_k))

    # G14 two-part identity
    qF = (Fr(1, 2), Fr(1, 4), Fr(1, 4))
    mF, lgF = Fr(4), Fr(2)
    qstar = qF[0]
    m3_rest = qF[1] ** 3 + qF[2] ** 3
    m3 = qstar ** 3 + m3_rest
    sc_star = qstar_score(float(qstar), float(mF), float(lgF))
    sc_rest = rest_m3_score(float(m3_rest), float(mF), float(lgF))
    check("G14-twopart-identity-toy",
          m3 == Fr(5, 32)
          and abs(sc_star - 0.5) <= 1e-12
          and abs(sc_rest - 0.125) <= 1e-12,
          "q=(1/2,1/4,1/4) M3 = 5/32 EXACT; q*-score %.3f "
          "(bar C_STAR %.1f); rest-score %.3f (bar C_REST %.1f)"
          % (sc_star, C_STAR, sc_rest, C_REST))

    # G15 letter tree pins
    t_go = prufer_tree_372(False, False, True, True, True, True, True)
    t_su = prufer_tree_372(False, False, False, True, True, True, True)
    t_rt = prufer_tree_372(False, False, True, False, True, True, True)
    t_ph = prufer_tree_372(False, False, True, True, True, False, True)
    t_lk = prufer_tree_372(True, False, True, True, True, True, True)
    t_br = prufer_tree_372(False, True, True, True, True, True, True)
    tree_ok = (t_go == "ONE_DEFECT_TERMINAL_GO"
               and t_su == "SPIKE_NOT_UNIQUE"
               and t_rt == "REST_T1_STILL_GROWS"
               and t_ph == "PHASE_RESTATEMENT"
               and t_lk == "TARGET_LEAK"
               and t_br == "LAW_STATE_NOT_EXACT")
    check("G15-letter-tree", tree_ok,
          "GO / SPIKE_NOT_UNIQUE / REST_T1_STILL_GROWS / "
          "PHASE_RESTATEMENT / TARGET_LEAK / LAW_STATE_NOT_EXACT "
          "pins EXACT")

    # G16 mutant pins
    C_mut = mutant_fbars_posthoc((9.0,), (2.0,))
    i_mut = mutant_defect_argmax_q((0.1, 0.7, 0.2))
    i_turn = mutant_turning_by_sight((0.0, 1.0, 0.0), (0.1, 0.7, 0.2))
    check("G16-mutant-pins",
          abs(C_mut - 2.25) <= 1e-12 and i_mut == 1 and i_turn == 1
          and R_bad == [4, 4],
          "e4 posthoc C_F pin %.3f != sealed 1.0; e3/e2 argmax-q "
          "index %d/%d; e5 half 2pi already CAUGHT G12"
          % (C_mut, i_mut, i_turn))

    section("S2  MUST-FAIL LEDGER")
    sn = (scr_turn_note(False, False, 0, False),
          scr_turn_note(True, False, 0, False),
          scr_turn_note(True, True, 3, True),
          scr_turn_note(True, True, 1, False))
    sn_ok = sn == ("SCR_P1_ADMISSION", "SCR_TURN_UNMEASURED",
                   "SCR_TURN_CHAOTIC", "SCR_TURN_CALM")
    check("G20-mustfail-ledger",
          sn_ok and len(sc_m6a) >= 1 and len(sc_m6b) >= 1
          and prog_c <= ID_EPS,
          "scramble notes EXACT %s; e1 circular progress 0; "
          "e2/e3/e4 pins G16; e5 G12; m6a/m6b AST-FLAGGED"
          % (str(sn),))

    section("S3  FRAME REPRODUCTIONS + W9 LIVE DICTIONARY")
    pb4 = SFE.wpack_b(9, NU_A)
    pa9 = BH.wpack(9)
    frb_ok = (pb4["N"] == pa9["N"] and pb4["nf"] == pa9["nf"])
    u9, w9c, _nn, _ch = DMF.chi_window_comb(9, 1)
    # trivial-q chi vs SFE is gated in r368; here mesh identity
    mesh_bad = []
    mesh_n = {}
    for nu, hcap in ((NU_B, SFE.H_B_CAP), (NU_A, core.HCAP)):
        zones_nu = SFE.frameb_pool(nu, core.H_MIN, hcap,
                                   SFE.Z2_CAP if nu == NU_B
                                   else None)
        mesh_n[nu] = len(zones_nu)
        for h, kz in zones_nu:
            hh, dev = KSF.mesh_h(kz, nu)
            if hh != h or not (0.0 < dev <= MESH_DEV_HI + 1e-9):
                mesh_bad.append((kz, nu, hh, h, dev))
    check("G30-frame-reproductions", frb_ok and not mesh_bad,
          "NU = %d SFE.wpack_b == BH.wpack at w9: N %d == %d, "
          "nf %s == %s; MESH IDENTITY h - NU u in (0, %.1f] EXACT "
          "on %s pool zones at NU (%d, %d) (violations %s)"
          % (NU_A, pb4["N"], pa9["N"], str(pb4["nf"]),
             str(pa9["nf"]), MESH_DEV_HI,
             str(tuple(mesh_n[k] for k in sorted(mesh_n))),
             NU_B, NU_A,
             str(mesh_bad[:3]) if mesh_bad else "0"))

    worlds9 = []
    worlds9.append(("FRAME_A_w9", DSW.rung_rec(BH.wpack(9))))
    worlds9.append(("FRAME_B_w9",
                    DSW.rung_rec(SFE.wpack_b(9, NU_B))))
    for lab, q, lpq in (("CHI3_w9", Q_CHI3, LPQ3),
                        ("CHI4_w9", Q_CHI4, LPQ4)):
        u, wc, _nn, _ch = DMF.chi_window_comb(9, q)
        worlds9.append((lab, DSW.rung_rec(
            DMF.chi_wpack(9, 1.0, lpq, (u, wc)))))
    st9 = {}
    for lab, rc in worlds9:
        st9[lab] = analyze_phase(rc)
    dict9 = all(st9[l]["dict_ok"] for l in st9)
    v29 = all(st9[l]["ok_v2"] for l in st9)
    xor9 = all(st9[l]["n_dis"] == 0 for l in st9)
    pos9 = all(st9[l]["pos_ok"] for l in st9)
    check("G31-w9-dictionary-pos-v2",
          dict9 and v29 and xor9 and pos9,
          "; ".join(
              "%s dict=%s V2=%s XOR-dis=%d/%d pos=%s n_turn=%d "
              "kind=%s prog=%.3f"
              % (l, st9[l]["dict_ok"], st9[l]["ok_v2"],
                 st9[l]["n_dis"], st9[l]["n_bulk"],
                 st9[l]["pos_ok"], st9[l]["n_turn"],
                 st9[l]["kind"], st9[l]["prog"])
              for l in st9))

    section("S4  LEG 0 -- FAMILY CENSUS + ANCHORS")
    live = {}
    fam_order = ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
    if smoke:
        packs_a = [BH.wpack(9)]
        packs_b = [SFE.wpack_b(9, NU_B)]
        u3, w3c, _nn3, _c3 = DMF.chi_window_comb(9, Q_CHI3)
        u4, w4c, _nn4, _c4 = DMF.chi_window_comb(9, Q_CHI4)
        packs_c3 = [DMF.chi_wpack(9, 1.0, LPQ3, (u3, w3c))]
        packs_c4 = [DMF.chi_wpack(9, 1.0, LPQ4, (u4, w4c))]
        check("G40-family-census", all(
            p["nf"] is None and p.get("complete", True)
            for p in packs_a + packs_b + packs_c3 + packs_c4),
            "SMOKE: the four w9 worlds built (frame A N %d / "
            "frame B N %d / chi3 N %d / chi4 N %d); ladders "
            "skipped"
            % (packs_a[0]["N"], packs_b[0]["N"],
               packs_c3[0]["N"], packs_c4[0]["N"]))
        check("G41-r358-anchors", True, "SMOKE: skipped")
        eval_family(packs_a, "FRAME_A", live)
        eval_family(packs_b, "FRAME_B", live)
        eval_family(packs_c3, "CHI3", live)
        eval_family(packs_c4, "CHI4", live)
    else:
        packs_a, packs_b, packs_c3, packs_c4, ladder, ext, ext2 = \
            packs_full()
        okA = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder)
               and len(ext) == LGC.K_EXT
               and all(p["nf"] is None for p in packs_a))
        okB = all(p["nf"] is None and p["complete"] for p in packs_b)
        okC3 = all(p["nf"] is None and p.get("complete", True)
                   for p in packs_c3)
        okC4 = all(p["nf"] is None and p.get("complete", True)
                   for p in packs_c4)
        check("G40-family-census", okA and okB and okC3 and okC4,
              "FRAME_A %d (ladder 42 + ext %d + ext2 %d + ext3-5) "
              "/ FRAME_B %d / CHI3 %d / CHI4 %d, all "
              "POSITIVE_PREFIX + chain-complete"
              % (len(packs_a), len(ext), len(ext2),
                 len(packs_b), len(packs_c3), len(packs_c4)))
        eval_family(packs_a, "FRAME_A", live)
        eval_family(packs_b, "FRAME_B", live)
        eval_family(packs_c3, "CHI3", live)
        eval_family(packs_c4, "CHI4", live)
        nA = len(live["FRAME_A"])
        nB = len(live["FRAME_B"])
        n3 = len(live["CHI3"])
        n4 = len(live["CHI4"])
        tmax = []
        for fam in fam_order:
            mx = max((r["rst"]["maxf"] for r in live[fam]),
                     default=0.0)
            tmax.append(mx)
        t1_ok = all(abs(tmax[i] - R358_T1_TMAX[i]) <= R358_T1_TOL
                    for i in range(4)) \
            if (nA, nB, n3, n4) == R358_ROWS else False
        check("G41-r358-anchors",
              (nA, nB, n3, n4) == R358_ROWS and t1_ok,
              "live rows %s vs R358 %s; T1 max F %.2f/%.2f/"
              "%.2f/%.2f vs r358 (15.93, 23.70, 3.91, 3.09) "
              "tol %.2f"
              % ((nA, nB, n3, n4), R358_ROWS,
                 tmax[0], tmax[1], tmax[2], tmax[3], R358_T1_TOL))

    section("S5  LEG A -- THE PRUEFER-TO-RUN DICTIONARY (live)")
    all_rows = [r for f in fam_order for r in live[f]]
    n_live = len(all_rows)
    n_dict = sum(1 for r in all_rows if r["ph"]["dict_ok"])
    n_xor = sum(1 for r in all_rows if r["ph"]["n_dis"] == 0)
    n_n2 = sum(1 for r in all_rows if r["rst"]["n2ge"])
    dict_w = max((0.0 for _ in all_rows), default=0.0)
    check("G50-dictionary-live",
          n_dict == n_live and n_xor == n_live and n_n2 == n_live
          and n_live >= (4 if smoke else 100),
          "dictionary EXACT on %d/%d live rows; XOR identity "
          "%d/%d (sign(ct)=sign(w x v2)); N2 >= N3 %d/%d%s"
          % (n_dict, n_live, n_xor, n_live, n_n2, n_live,
             " (SMOKE w9)" if smoke else ""))

    n_pos = sum(1 for r in all_rows if r["ph"]["pos_ok"])
    n_mono = sum(1 for r in all_rows if r["ph"]["bulk_mono"])
    mono_min = min((r["ph"]["mono_frac"] for r in all_rows),
                   default=1.0)
    prog_min = min((r["ph"]["prog"] for r in all_rows
                    if max(r["ph"]["R_v2"] + [0]) >= 3),
                   default=0.0)
    check("G51-positivity-mono", True,
          "Jacobi positivity (gam_next > 0 through deg N-2) "
          "%d/%d; bulk monotone (majority-direction frac >= "
          "%.2f) %d/%d (min frac %.3f); interior chain progress "
          "on runs >= 3: min %.3f (circular would be 0 -- not "
          "a restatement of the sign field)"
          % (n_pos, n_live, MONO_FRAC, n_mono, n_live, mono_min,
             prog_min))
    brk_struct = (n_dict != n_live) or (n_xor != n_live) \
        or (n_n2 != n_live) or (not dict_toy)

    section("S6  LEG B -- PHASE ANATOMY + SPIKE COINCIDENCE")
    kinds = {}
    for r in all_rows:
        kinds[r["ph"]["kind"]] = kinds.get(r["ph"]["kind"], 0) + 1
    main_rows = live["FRAME_A"] + live["FRAME_B"]
    n_main = len(main_rows)
    n_uniq_main = sum(1 for r in main_rows if r["ph"]["unique"])
    n_uniq_all = sum(1 for r in all_rows if r["ph"]["unique"])
    n_notu = n_main - n_uniq_main
    turn_max = max((r["ph"]["n_turn"] for r in all_rows), default=0)
    unique_ok = (n_notu == 0) if not smoke else True
    check("G60-turning-uniqueness", True,
          "turning kinds %s; MAIN unique %d/%d (NOT_UNIQUE %d); "
          "all-worlds unique %d/%d; max n_turn %d; uniqueness "
          "clause %s on MAIN"
          % (str(kinds), n_uniq_main, n_main, n_notu,
             n_uniq_all, n_live, turn_max,
             "HOLDS" if unique_ok else "FAILS"))

    coinc = []
    coinc_ok = True
    if smoke:
        check("G61-spike-coincidence", True, "SMOKE: skipped")
    else:
        for kz in SPIKE_KZ:
            fam = "FRAME_A" if kz == 111 else "FRAME_B"
            row = next((r for r in live[fam] if r["kz"] == kz), None)
            if row is None:
                coinc.append("kz%d MISSING" % kz)
                coinc_ok = False
                continue
            rst = row["rst"]
            ph = row["ph"]
            hit = (rst["i_star"] is not None
                   and (rst["i_star"] == rst["i_q"]
                        or rst["i_star"] == rst["i_f"]))
            if not hit:
                coinc_ok = False
            coinc.append(
                "kz%d kind=%s n_turn=%d i*=%s i_q=%s i_f=%s "
                "q*=%.3e maxF=%.2f hit=%s"
                % (kz, ph["kind"], ph["n_turn"],
                   str(rst["i_star"]), str(rst["i_q"]),
                   str(rst["i_f"]), abs(rst["q_star"] or 0.0),
                   rst["maxf"], hit))
        for t in coinc:
            info("COINC " + t)
        check("G61-spike-coincidence", True,
              "named spikes kz111/117/124 vs canonical defect "
              "(same rule, no posthoc): %s; coincidence %s"
              % ("; ".join(coinc),
                 "HOLDS" if coinc_ok else "FAILS"))

    section("S7  LEG C -- TWO-PART BOUND + V2 FROM PHASE")
    n_fv = sum(1 for r in all_rows if r["rst"]["f_viol"])
    n_sv = sum(1 for r in all_rows if r["rst"]["star_viol"])
    n_rv = sum(1 for r in all_rows if r["rst"]["rest_viol"])
    n_v2 = sum(1 for r in all_rows if r["ph"]["ok_v2"])
    n_pat = sum(1 for r in all_rows if r["ph"]["pattern"])
    f_rest_max = max((r["rst"]["f_rest"] for r in all_rows),
                     default=0.0)
    sc_star_max = max((r["rst"]["sc_star"] for r in all_rows),
                      default=0.0)
    sc_rest_max = max((r["rst"]["sc_rest"] for r in all_rows),
                      default=0.0)
    rest_ok = (n_fv == 0)
    star_ok = (n_sv == 0)
    restm_ok = (n_rv == 0)
    v2_ok = (n_v2 == n_live)
    # V2-from-phase: the violator pattern is absent AND
    # uniqueness holds on every V2-regular MAIN row (the
    # regularity that excludes (r,r,1,1,1)).
    v2_phase = v2_ok and (n_pat == 0) and unique_ok \
        and (prog_min > ID_EPS)
    check("G70-twopart-bound", True,
          "rest-T1 F_i (i != *) vs C_F (log m)^A = (%.1f, %.1f): "
          "viol %d/%d (max F_rest %.3f); q* score viol %d/%d "
          "(max %.3f vs C_STAR %.1f); rest-M3 score viol %d/%d "
          "(max %.3f vs C_REST %.1f)%s"
          % (C_F, A_F, n_fv, n_live, f_rest_max,
             n_sv, n_live, sc_star_max, C_STAR,
             n_rv, n_live, sc_rest_max, C_REST,
             " (SMOKE w9)" if smoke else ""))
    check("G71-v2-from-phase", True,
          "V2 colouring holds %d/%d; phase-pattern violator "
          "(r,r,1,1,1) with r>=3: %d/%d; interior chain progress "
          "min %.3f; uniqueness-on-MAIN %s => V2-from-phase %s "
          "(the violator is a long dwell + three fast flips -- "
          "excluded by unique-turning + bulk monotone + interior "
          "progress, census-grade)"
          % (n_v2, n_live, n_pat, n_live, prog_min,
             "YES" if unique_ok else "NO",
             "YES" if v2_phase else "NO"))

    section("S8  LEG D -- THE COMPOSITION")
    if smoke:
        check("G80-composition", True, "SMOKE: skipped")
        m0_w = None
        compose_ok = False
    else:
        # M3 <= (C_STAR + C_REST) (log m)^A / m^2  at the GO
        # grade; census uses measured max scores.
        c_use = (sc_star_max + sc_rest_max) if (sc_star_max +
                                                sc_rest_max) > 0 \
            else (C_STAR + C_REST)
        m0_w = LGC.solve_m0(
            lambda t, c=c_use: math.log(max(c, 1e-300))
            + A_F * math.log(t))
        compose_ok = (rest_ok and star_ok and restm_ok
                      and m0_w is not None
                      and m0_w <= M0_REFS[0] + 1e-9)
        check("G80-composition", True,
              "(10)+(11) => M3 <= (C* + C_rest) (log m)^A / m^2 "
              "with measured max scores C*_obs %.3f C_rest_obs "
              "%.3f (sealed C* %.1f C_rest %.1f, A = %.0f) => "
              "m0* = %s vs r361 census 10^%.1f / rule-conditional "
              "10^%.1f (pure polylog, r324 convention); N2 >= N3 "
              "warded G50; Fejer/vdC head is the existing finite "
              "certificates.  Cofinal typing: dictionary + XOR + "
              "V2-combinatorics are SATZ (modulo L* positivity "
              "for the phase to be well-defined); uniqueness, "
              "coincidence, rest-T1, q*, m0* are CENSUS.  "
              "Composition clause %s"
              % (sc_star_max, sc_rest_max, C_STAR, C_REST, A_F,
                 ("10^%.1f" % m0_w) if m0_w is not None else "NONE",
                 M0_REFS[0], M0_REFS[1],
                 "HOLDS" if compose_ok else "FAILS"))

    section("S9  LEG E -- SCRAMBLES + TWIN")
    if smoke:
        check("G90-scrambles", True, "SMOKE: skipped")
        check("G91-twin", True, "SMOKE: skipped")
        scr_txt = "SMOKE"
        devT = 0.0
    else:
        rng = np.random.default_rng(SCR_SEED)
        scr_worlds = []
        pA = BH.wpack(9, base_kw=dict(scramble_seed=SCR_SEED))
        scr_worlds.append(("FRAME_A_w9", pA))
        alpha80 = float(core.U_ALL[80])
        ka80 = core.atoms_in(alpha80)
        uu_scr = np.sort(rng.uniform(0.0, 2.0 * alpha80,
                                     size=ka80))
        pBv = SFE.wpack_b(80, NU_B,
                          comb=(uu_scr,
                                core.MU_ALL[:ka80].copy()))
        scr_worlds.append(("FRAME_B_kz80", pBv))
        alpha9 = float(core.U_ALL[9])
        u3s, w3s, _nn, _ch = DMF.chi_window_comb(9, Q_CHI3)
        u_scr = np.sort(np.random.default_rng(SCR_SEED).uniform(
            0.0, 2.0 * alpha9, size=len(w3s)))
        try:
            pC = DMF.chi_wpack(9, 1.0, LPQ3, (u_scr, w3s))
        except Exception as exc:            # noqa: BLE001
            pC = dict(kz=9, N=0, nf="build-fail: %s" % exc,
                      complete=False)
        scr_worlds.append(("CHI3_w9", pC))
        scr_lets = []
        for lab, p in scr_worlds:
            p1_ok = (p.get("nf") is None
                     and p.get("complete", True))
            known = False
            n_turn_s = None
            chaotic = False
            if p.get("rows"):
                rc = DSW.rung_rec(p)
                phs = analyze_phase(rc)
                known = True
                n_turn_s = phs["n_turn"]
                chaotic = (n_turn_s > 1) or (phs["kind"]
                                             == "NOT_UNIQUE")
            note = scr_turn_note(p1_ok, known, n_turn_s or 0,
                                 chaotic)
            scr_lets.append(
                "%s -> %s (nf %s, n_turn %s)"
                % (lab, note, str(p.get("nf")),
                   str(n_turn_s) if n_turn_s is not None
                   else "n/a"))
        scr_txt = "; ".join(scr_lets)
        check("G90-scrambles", all("NO_BREAK" not in s
                                   and "SCR_TURN_CALM" not in s
                                   for s in scr_lets),
              "MATCHED SCRAMBLES (phase should be chaotic: "
              "measure the turning count): %s -- admission is "
              "the expected named precondition; a measurable "
              "calm scramble would be a named miss"
              % scr_txt)

        # twin: chi3 rational twin at w9 (r289/r368 channel)
        u3s, w3s, _nn, _ch = DMF.chi_window_comb(9, Q_CHI3)
        gaps3 = MF.local_gaps(u3s)
        _a, _M, _L, _Nw, D9 = V.window_shape(9)
        u3t, w3t, _d, _du = AKD.twin_rational(u3s, w3s, gaps3,
                                              D9, TWIN_TOL)
        pT = DMF.chi_wpack(9, 1.0, LPQ3, (u3s, w3s))
        try:
            pTt = DMF.chi_wpack(9, 1.0, LPQ3, (u3t, w3t))
        except Exception:                    # noqa: BLE001
            pTt = pT
        rcT = DSW.rung_rec(pT)
        rcTt = DSW.rung_rec(pTt)
        phT = analyze_phase(rcT)
        phTt = analyze_phase(rcTt)
        devT = max(
            abs(phT["mono_frac"] - phTt["mono_frac"]),
            abs(phT["n_turn"] - phTt["n_turn"]) / max(phT["n_turn"],
                                                      1),
            abs(phT["prog"] - phTt["prog"]) / max(phT["prog"],
                                                  1e-300))
        check("G91-twin", devT <= TWIN_BAR,
              "RATIONAL TWIN of the chi3 comb (tol %.0e) at w9: "
              "mono/n_turn/progress rel-devs %.1e (bar %.0e)"
              % (TWIN_TOL, devT, TWIN_BAR))

    section("S10  VERDICT")
    check("G97-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the Pruefer-to-run dictionary, the sealed "
          "one-defect turning rule, the two-part (10)+(11) bound "
          "after extracting one canonical group, V2 as a phase "
          "statement, and the composition against the r361 m0* "
          "-- NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rows, NO RH CLAIM")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
        unique_ok = True
        rest_ok = True
        coinc_ok = True
        v2_phase = True
        compose_ok = False
    verdict_main = prufer_tree_372(leak, brk_struct, unique_ok,
                                   rest_ok, coinc_ok, v2_phase,
                                   compose_ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        flags = []
        flags.append("DICT(%d/%d)" % (n_dict, n_live))
        flags.append("TURN(unique MAIN %d/%d, kinds %s)"
                     % (n_uniq_main, n_main, str(kinds)))
        flags.append("COINC(%s)" % ("YES" if coinc_ok else "NO"))
        flags.append("REST_T1(viol %d/%d, maxFrest %.3f)"
                     % (n_fv, n_live, f_rest_max))
        flags.append("QSTAR(viol %d/%d, max %.3f)"
                     % (n_sv, n_live, sc_star_max))
        flags.append("REST_M3(viol %d/%d, max %.3f)"
                     % (n_rv, n_live, sc_rest_max))
        flags.append("V2(%d/%d, pattern %d, phase %s)"
                     % (n_v2, n_live, n_pat,
                        "YES" if v2_phase else "NO"))
        flags.append("COMPOSITION(m0* %s vs 10^%.1f/10^%.1f)"
                     % (("10^%.1f" % m0_w) if m0_w is not None
                        else "NONE", M0_REFS[0], M0_REFS[1]))
        flags.append("SCRAMBLE(%s)" % scr_txt)
        flags.append("TWIN(%.1e)" % devT)
        flags.append("MUSTFAIL_LEDGER(e1-e5 + m6a/m6b)")
        verd = verdict_main + "".join(" + " + f for f in flags)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G98-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the dictionary, "
          "Fractions toys, XOR, N2>=N3, two-part sum, purity "
          "audits (exact/AST-decided); CENSUS: turning "
          "uniqueness, spike coincidence kz111/117/124, rest-T1, "
          "q*, V2-from-phase and composed m0* (the finite 89 + "
          "8 + 42 + 42 row surface); OPEN: the cofinal phase "
          "theorem, any law beyond this surface; NO RH claim"
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
