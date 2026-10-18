#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""decider_cell_probe -- PRIME.COFINAL.DECIDER.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim.  2026-08-13.)

BUILD THE NAMED DECIDER CELL OF THE CORRECTED LEGALITY MAP.
CCCXVII (metric_map_probe) redrew the frontier legality map with the
CCCVII metric-corrected ideal tier and returned CORRECTED-AMBIGUOUS:
the termination signal beyond the corrected sub-ladder horizon
h*_corr = 8629 is metric-clean (every built cell beyond it -- 8677,
9023, 9447, 9535 -- carries an OUTWARD-enclosed ideal witness), but
the deepest bin (9500, 11000] holds only ONE built cell (9535), so
the corrected termination read rests on a SINGLE sample.  CCCXVII
NAMED the decider: the census cell h 10513 kz 341 (est ~630 s).
THIS PROBE builds the decider (and, budget permitting, up to two
more admissible census cells in the same bin), runs the FULL
corrected tier on each (raw tau + legality, d with outward
enclosure, tau_ideal_ub with outward enclosure, the A13 O-metric
refined read, the corrected type, seat localization), and delivers
the updated cofinal verdict for the corrected sub-ladder.

 (a) THE BIN CENSUS: enumerate every admissible census cell with
     9500 < h <= 11000 (the CCCV/CCXCIX deployed census formula
     VERBATIM -- a structural enumeration from nodes/weights, no
     outcome is read).  The build roster (frozen order): the two
     GATE cells (8629 kz 223, the corrected-ladder anchor; 9535
     kz 526, the existing single bin sample), then the DECIDER
     10513 kz 341 FIRST among new cells, then the remaining bin
     cells ascending in h (ascending h^3 build cost), at most
     MAX_EXTRA of them, under the self-calibrating guard.
 (b) THE CORRECTED TIER per built cell, CCCVII/CCCXVII machinery
     VERBATIM (chain_pass_values / chain_pass_project / ideal_tier
     incl. the A13 O-metric refinement / cd_route / ldl_inertia /
     outward gamma_n enclosures of the decisive scalars): raw tau
     and wall-legality (CCLXXIII cell_legal), d = c^T (O - I) c
     outward-rounded, tau_ideal_ub = 1 - lam^2/(lam + d) with
     outward enclosure, the refined read, the corrected type (rule
     below), the seat localization (LU inverse iteration, A6) --
     does the migrating-seat anatomy continue into the new cells?
 (c) THE UPDATED COFINAL VERDICT (enum below) + the updated
     MAX-TAU_IDEAL_UB-PER-BIN ladder (CCCXVII rule verbatim; the
     shallower bins enter as FROZEN CCCXVII facts, cited constants,
     not rebuilt).

THE HONEST ASYMMETRY (CCCVII/CCCXVII verbatim, load-bearing):
tau_ideal_ub is an UPPER bound for tau_ideal, so a NEGATIVE ideal
read is a WITNESS while a POSITIVE read is only "no witness found"
-- positivity of the ideal object is NEVER certified here.  The
corrected map can only REMOVE cells from the legal ladder, never
add any.

THE CORRECTED TYPE RULE (CCCXVII frozen, verbatim; ub = the witness
read with outward enclosure [ub_lo, ub_hi], ref = the refined
minimum over O-metric Rayleigh iterates, ref <= ub):
  IDEAL-WITNESS-NEGA iff ref < -IDEAL_NOISE and ub_hi < -IDEAL_NOISE;
  IDEAL-LEAN-NEGA    iff ref < -IDEAL_NOISE, not WITNESS;
  NO-WITNESS-POS     iff ref > +IDEAL_NOISE;
  IDEAL-UNRESOLVED   otherwise (the enclosure width is printed as
     the honest resolution limit).
ELIGIBILITY (CCCXVII frozen, verbatim): a built cell is
corrected-ELIGIBLE iff raw LEGAL (cell_legal OK, |tau| > TAU_NOISE)
AND NO-WITNESS-POS.

THE UPDATED VERDICT RULE (frozen BEFORE the run; the deepest-bin
roster = the built cells of THIS run with 9500 < h <= 11000, i.e.
the rebuilt 9535 + the decider + any built extras; the shallower
map enters as the frozen CCCXVII facts cited in the constants):
 CORRECTED-CONTINUES(h*_new)  iff >= 1 built bin cell is ELIGIBLE
   -- the corrected sub-ladder extends past 8629; the new horizon
   h*_new = the deepest eligible built cell; the bin pick =
   MAX tau_ub_ref over eligible bin cells.
 CORRECTED-TERMINATES(h_last = 8629)  iff the bin has >= 2 built
   cells AND none is eligible AND EVERY built bin cell is
   IDEAL-WITNESS-NEGA AND the frozen CCCXVII beyond-set (8677,
   9023, 9447 -- all IDEAL-WITNESS-NEGA, cited) stands -- the bin
   is witness-NEGA throughout: the deployed family's ideal
   legality genuinely ends at 8629 ON THE BUILT SET, stated as
   the construction fact it is (a statement about built cells of
   the deployed family, never about all h, never about RH).
 STILL-AMBIGUOUS  otherwise (< 2 built bin cells, or a bin cell
   is IDEAL-UNRESOLVED / IDEAL-LEAN-NEGA / a non-witness negative)
   -- the enclosure widths are printed with the precision that
   would decide.
Exhaustive and disjoint over the bin roster; every statement is
about BUILT cells of the deployed construction.

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only
    RNG seats are the DECLARED orthogonality-probe seed
    (OPROBE_SEED) and the DECLARED scramble seed.  AC scan: the
    chain-pass, CD and census readers see nodes, weights, entries,
    coefficients and frozen constants only.
 T  TAB2 = 1.6e7 arrays built and warded BITWISE against the
    deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  the deep census (deployed frame formula verbatim), h-sorted;
    gates: 587 cells, h max 65051, the census CONTAINS the decider
    key (10513, 341) and both gate keys; the BIN ROSTER
    (9500, 11000] is printed in full; D1a: the frozen EXTRAS are
    exactly the MAX_EXTRA cheapest roster cells (ascending h)
    excluding the bin gate cell and the decider (rule-checked
    against the census, not merely asserted).
 TIE the dissect builder (CCCVII build_cell_dissect VERBATIM) must
    tie bat.build_rung_param EXACTLY (tau, negA, lamS ==) on the
    TIE cell (nearest h 2012); PASS-TIE: the AC-scanned accumulator
    ties ob.eval_chain there.
 G  reproduction gates on the two shared cells: 8629 kz 223 must
    reproduce tau +7.245e-10 LEGAL (CCCVII print, rtol NEGA_RTOL),
    d +3.8689e-11 (CCCVII 5-digit print, rtol REPRO_D) and the
    refined ideal read +7.632e-10 (CCCXVII 4-digit print, rtol
    NEGA_RTOL) with type NO-WITNESS-POS; 9535 kz 526 must
    reproduce tau -1.743e-10 NEGA, d +4.2931e-11, refined read
    -1.3139e-10 (CCCVII 5-digit prints, rtol REPRO_D) with type
    IDEAL-WITNESS-NEGA.  G-INERTIA: the two independent inertia
    routes agree on every built cell.  G-COVERAGE: a guard refusal
    of an EXTRA cell is a BUDGET fact, typed, never charged as a
    failure; a guard refusal of the DECIDER leaves the verdict
    STILL-AMBIGUOUS with the budget fact printed.
 AN anatomy wards: W7 rank identity (#unit >= max(0, n_neg - h)),
    W8 the E8 ward lamS >= tau on PD cells (consumed nowhere),
    W9 the node accounting M == n_pos + n_neg + n_dropped.
 WO the OUTWARD-ROUNDING DISCIPLINE ward on every built cell:
    d_lo <= d <= d_hi, ub_lo <= ub <= ub_hi, ref <= ub, all
    enclosure widths finite and printed.
 X  controls-must-fire: X1 the scramble world must leave legality
    (cheap depth XCTRL_TGT); X2 the SMOOTH (prime-free) world AT
    THE DECIDER CELL ITSELF must leave legality; X2C the CORRECTED
    tier on the smooth decider must ALSO stay negative (ref <
    X2C_BAR) -- the discrimination persists under the corrected
    instrument at the decider depth (eigh-bottom witness, A6
    control route, disclosed); XO the faithfulness reader must
    FIRE on a DOCTORED recurrence (one be entry scaled by
    1 + XO_DOPE); XD the doctored metric must move the ideal read.
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION (census + decider cells only) and
    typed as such.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum): the UPDATED COFINAL case above, plus typed
tags BIN-CENSUS(roster, built, unbuilt-guard), LADDER(h*_corr,
per-bin picks incl. the frozen CCCXVII bins), SEAT(the decider
seat vs the 9535 seat -- anatomy observation, consumed nowhere),
IDEALITY(bin d census, enclosure widths, the CCCXVII drift-fit
extrapolation |d| ~ 7.7e-11 at h 10500 compared as
CONJECTURE-GRADE print, never a gate), GATE-COVERAGE, CONTROLS,
SCREENS-VACUOUS, AMENDMENTS.  Every enum is a finite float64
statement with outward-rounded enclosures of the decisive scalars,
about BUILT cells of the deployed construction; NEVER an all-h
statement, NEVER an RH claim, NEVER a counterexample claim.

FROZEN BARS.  NDIM = 8; TAB2 = 1.6e7; KZ2_MAX = 1200; CENSUS_N_REF
= 587; CENSUS_HMAX_REF = 65051; TAU_NOISE = 5e-12; NEGA_RTOL =
2e-3; REPRO_D = 1e-3; IDEAL_NOISE = 1e-12; CD_TIE = 1e-2; CD_SEP =
1e-9; CD_BLOCK = 512; ORTHO_BAR = 1e-9; OPROBE_SEED = 7; NREF = 2;
BIN_LO = 9500; BIN_HI = 11000; DECIDER = (10513, 341); EXTRAS =
((9557, 242), (9585, 320)) (the two cheapest bin roster cells by
the frozen rule, read from the smoke census print); MAX_EXTRA =
2; COST_C_ENV = 4.6e-10 s; GUARD_FAC = 1.05; BUILD_CAP_S = 2700
(A5); SCR_SEED = 1; XCTRL_TGT = 1300; X2C_BAR = -1.0; LOC_ITERS =
30; UNIT_TIE = 1e-9; TIE_TGT = 2012; XD_DOPE = 1e-6; XO_DOPE =
1e-6; DRIFT_EXTRAP = 7.7e-11 (CCCXVII conjecture-grade print,
compared, never gated).
Smoke: the roster is (TIE cell, census cell nearest h 2200); the
gates are SMOKE-SKIPPED (typed); X2/X2C at depth 600; the bin
roster is PRINTED (census enumeration only, no bin cell is built);
verdict SMOKE.

FROZEN REFERENCE CONSTANTS (all cited from the PRINTED outputs of
CCCVII / CCCXVII -- next.txt notes and probe docstrings; no cell
was built and no tau was read before the freeze):
 GATES: (8629, 223, tau +7.245e-10, LEGAL, d +3.8689e-11, ref_ub
   +7.632e-10, NO-WITNESS-POS); (9535, 526, tau -1.743e-10, NEGA,
   d +4.2931e-11, ref_ub -1.3139e-10, IDEAL-WITNESS-NEGA).
 THE CCCXVII CORRECTED LADDER (frozen facts, not rebuilt):
   (6100, 6320] -> 6191 kz 178 ub_ref +3.954e-10;
   (6320, 6600] -> 6344 kz 241 ub_ref +2.700e-10;
   (6600, 7300] -> NO SAMPLE (7004 guard-refused in CCCXVII);
   (7300, 8300] -> 8204 kz 287 ub_ref +3.559e-10;
   (8300, 9500] -> 8629 kz 223 ub_ref +7.632e-10 = h*_corr.
 THE CCCXVII BEYOND-SET (frozen facts): 8677 kz 299 (-3.009e-10),
   9023 kz 506 (-6.246e-11), 9447 kz 196 (-8.746e-11), all
   IDEAL-WITNESS-NEGA with outward enclosures; 8642 kz 551
   MARGINAL (no raw sign claim, A3; see A4).

HONEST AMENDMENTS (declared before the frozen run).
 A1 NO new pre-freeze reconnaissance: every reference value is
    read from the PRINTED outputs of CCCVII / CCCXVII; the bin
    roster keys are read from the SMOKE census print (a structural
    enumeration from nodes/weights via the deployed frame formula
    -- no tau, no eigenvalue, no outcome of any kind is read
    pre-freeze).
 A2 the ideal tier is the CCCVII metric-corrected Galerkin object,
    reused VERBATIM.  The residual ideality question (how
    accurately the evaluated chain columns represent polynomials)
    is measured INDIRECTLY (diag(O) census, chain growth, CD entry
    route) and remains the named scope edge, not closed.  Outward
    rounding is applied to the DECISIVE SCALARS, not the full
    n x n matrix.
 A3 MARGINAL cells (|tau| <= TAU_NOISE) get no raw sign claim
    (CCXCIX A3 verbatim); their corrected read is printed and
    typed like any other.
 A4 the CCCXVII beyond-set contains ONE marginal cell (8642
    kz 551) whose corrected type CCCXVII did not print; the
    TERMINATES statement here is about witness-carrying cells and
    the deepest bin, with 8642 disclosed as a typed MARGINAL
    (no sign claim) -- an honest edge of the frozen citation, not
    a silent pass.
 A5 BUDGET: the cap 2700 s covers TAB2 + census (~80 s), the TIE
    ward, both gates (~600 s), the decider (~430-630 s at the
    CCCXVII measured rate), the smooth-decider control (~ the
    same), and leaves the extras to the guard's
    continue-semantics; a refusal of an extra is a BUDGET fact.
    The smooth-decider control is NOT guarded (it is a mandated
    control); worst-case wall ~48 min is disclosed here.
 A6 the localization is a DIAGNOSTIC tier (CCXCIX A7 verbatim):
    deterministic start, LU inverse iteration on the assembled A,
    refusals typed.  EXCEPTION, control-only and disclosed: on the
    SMOOTH world the X2C witness is the direct bottom eigenpair
    (scipy eigh subset); it enters no gate cell.  The SEAT tag is
    an anatomy OBSERVATION, consumed nowhere.
 A7 the exact-rational K-membership tier is NOT run (CCCVII
    measured K-membership 9/9 aligned with raw wall-legality);
    POS cells carry no CASE letter here -- this probe types the
    corrected tier only, the CCCVII case rule is not recomputed
    (the reclassification census was CCCXVII's job and is cited,
    not repeated).
 A8 no ladder rebuild of the shallow bins, no scorecard row, no
    promotion: nothing measured here enters a certificate of
    record.

SMOKE DISCLOSURE (2026-08-13), pre-freeze, verbatim.
 SMOKE-1 (SPEC_SHA at smoke time 63034924, 19/19 PASS, 16.8 s):
   every check green.  THE BIN ROSTER READ FROM THE CENSUS
   (structural enumeration only, no outcome read, no bin cell
   built): (9500, 11000] holds 29 admissible census cells; the
   mission decider key (10513, 341, alpha 7.63192, est 534 s) IS
   a census key; the two cheapest roster cells excluding the gate
   sample (9535, 526) and the decider are (9557, 242, est 402 s)
   and (9585, 320, est 405 s) -- these fill EXTRAS by the frozen
   ascending-cost rule.  Pre-freeze changes after smoke, both
   disclosed: EXTRAS filled with the two keys above; D1a retyped
   from a placeholder equality to the rule check (frozen keys in
   the roster AND EXTRAS == the MAX_EXTRA cheapest non-gate,
   non-decider roster cells).  No bar, rule, control or enum was
   touched otherwise.  Measured in smoke: TIE ward EXACT on h 2012
   kz 230 (tau, negA, lamS all ==); PASS-TIE q dev 1.68e-11,
   diag(O) dev 4.22e-15; TIE cell d +2.723932e-12 outward
   [+1.639910e-12, +3.808176e-12], NO-WITNESS-POS; smoke cell
   h 2196 kz 118 LEGAL tau +1.075441e-08, d -1.844080e-13 outward
   [-1.386002e-12, +1.017186e-12], NO-WITNESS-POS; inertia routes
   AGREE (0 2x2 blocks); W7/W8/W9/WO green; CD rel 5.077e-13 /
   2.251e-13; X1 scramble tau -7.792e+89 LEFT; X2 smooth h 606
   tau -812.1 LEFT; X2C smooth CORRECTED ref -812.1 < -1.0
   (eigh-bottom witness, rq_gap 1.1e-13); XO fires 2.000e-06 >
   1e-9 >= 1.377e-14; XD moves the ideal read by 1.000e-06.

NO RH claim.  NO counterexample claim.  No marker moves; no paper,
ledger, website, manifest or verification file is touched; the
only edit outside this file is the German CCCXXI line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII pipeline),
sigma_stress_battery_probe (CCLXIX bat.build_rung_param),
sigma_edge_growth_probe (CCLXXIII cell_legal, reproduced verbatim),
legality_frontier_probe (CCXCIX TAU_NOISE / frontier map),
legality_horizon_probe (CCCV horizon census),
cofinal_dissect_probe (CCCVII metric-corrected tier),
metric_map_probe (CCCXVII corrected map machinery, reused
VERBATIM; reference values under reproduction),
v563_paper2_readouts (deployed generators).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/decider_cell_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/decider_cell_probe.py
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
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)
import sigma_stress_battery_probe as bat      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
TAB2 = 16_000_000
EXT_DEPLOYED = 4_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
TAU_NOISE = 5.0e-12
NEGA_RTOL = 2.0e-3
REPRO_D = 1.0e-3
IDEAL_NOISE = 1.0e-12
CD_TIE = 1.0e-2
CD_SEP = 1.0e-9
CD_BLOCK = 512
ORTHO_BAR = 1.0e-9
OPROBE_SEED = 7
NREF = 2
BIN_LO = 9500
BIN_HI = 11000
DECIDER = (10513, 341)          # the CCCXVII-named decider key;
#                                 confirmed against the census in
#                                 smoke (see SMOKE DISCLOSURE).
EXTRAS = ((9557, 242), (9585, 320))
#                                 the two cheapest bin roster cells
#                                 (frozen ascending-cost rule, read
#                                 from the smoke census print).
MAX_EXTRA = 2
H_LAST = 8629
COST_C_ENV = 4.6e-10
GUARD_FAC = 1.05
BUILD_CAP_S = 2700.0
SCR_SEED = 1
XCTRL_TGT = 1300
X2C_BAR = -1.0
LOC_ITERS = 30
UNIT_TIE = 1.0e-9
TIE_TGT = 2012
XD_DOPE = 1.0e-6
XO_DOPE = 1.0e-6
DRIFT_EXTRAP = 7.7e-11
EPS64 = float(np.finfo(float).eps)

# frozen reproduction targets (h, kz, tau, verdict, d, ub_ref,
# itype); tau/d from the CCCVII prints, ub_ref for 8629 from the
# CCCXVII 4-digit print (gated at NEGA_RTOL), 9535 from the CCCVII
# 5-digit print (gated at REPRO_D).
GATE_REF = (
    (8629, 223, +7.245e-10, "LEGAL", +3.8689e-11, +7.632e-10,
     NEGA_RTOL, "NO-WITNESS-POS"),
    (9535, 526, -1.743e-10, "NEGA", +4.2931e-11, -1.3139e-10,
     REPRO_D, "IDEAL-WITNESS-NEGA"))
# the frozen CCCXVII corrected ladder (facts of record, not rebuilt)
CCCXVII_LADDER = (
    ((6100, 6320), 6191, 178, +3.954e-10),
    ((6320, 6600), 6344, 241, +2.700e-10),
    ((6600, 7300), None, None, None),
    ((7300, 8300), 8204, 287, +3.559e-10),
    ((8300, 9500), 8629, 223, +7.632e-10))
# the frozen CCCXVII beyond-set (h > 8629, outside the deepest bin)
CCCXVII_BEYOND = (
    (8677, 299, "IDEAL-WITNESS-NEGA", -3.009e-10),
    (9023, 506, "IDEAL-WITNESS-NEGA", -6.246e-11),
    (9447, 196, "IDEAL-WITNESS-NEGA", -8.746e-11),
    (8642, 551, "MARGINAL-NO-SIGN-CLAIM", None))

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals",
                 "eigvalsh", "inv", "pinv", "solve", "lu_factor",
                 "lu_solve", "negA", "lamS", "ldl")
READER_FUNCS = ("chain_pass_values", "chain_pass_project",
                "cd_bilinear", "atom_census", "hull_census")

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


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def ldl_inertia(dblk):
    """CCCVII A13 verbatim: exact block inertia of the Bunch-Kaufman
    LDL^T factor."""
    dd = np.diag(dblk)
    sub = np.diag(dblk, k=1)
    ndim = len(dd)
    n_neg = n_zero = n_two = 0
    i = 0
    while i < ndim:
        if i + 1 < ndim and sub[i] != 0.0:
            aa = Fraction(float(dd[i]))
            bb = Fraction(float(sub[i]))
            cc = Fraction(float(dd[i + 1]))
            det = aa * cc - bb * bb
            tr = aa + cc
            if det < 0:
                n_neg += 1
            elif det > 0:
                if tr < 0:
                    n_neg += 2
            else:
                n_zero += 1
                if tr < 0:
                    n_neg += 1
            n_two += 1
            i += 2
        else:
            if dd[i] < 0.0:
                n_neg += 1
            elif dd[i] == 0.0:
                n_zero += 1
            i += 1
    return n_neg, n_zero, n_two


def gamma_n(nterms):
    """Rigorous forward error factor for a length-n float64
    recursive summation: gamma_n = n u / (1 - n u)."""
    prod = nterms * EPS64 * 0.5
    if prod >= 0.5:
        return float("inf")
    return prod / (1.0 - prod)


# ============================================ TAB2 + the deep census
DEEP = {}


def build_tab2():
    section("T -- the depth-extension table TAB2 = %.3g, warded "
            "BITWISE against the deployed 4e6 prefix" % TAB2)
    ob.build_ext_tables()
    lam2 = core.von_mangoldt_table(TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    g2 = np.diff(u2)
    n_pref = len(ob.EXT["NN"])
    check("T1 TAB2 prefix ward: the 1.6e7 arrays agree BITWISE with "
          "the deployed 4e6 EXT arrays (%d atoms of %d)"
          % (n_pref, len(nn2)),
          (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
           and np.array_equal(u2[:n_pref], ob.EXT["U"])
           and np.array_equal(mu2[:n_pref], ob.EXT["MU"])),
          kill="K2")
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = g2


def deep_census():
    section("D -- THE DEEP-FRAME CENSUS on TAB2 (deployed formula "
            "verbatim), h-sorted + THE BIN ROSTER (%d, %d]"
            % (BIN_LO, BIN_HI))
    u2, g2 = DEEP["U"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        hz = mz // 2
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=hz, kz=kz, alpha=alpha, M=mz, X=x_val))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    keys = {(c["h"], c["kz"]) for c in out}
    need = [DECIDER] + [(hv, kv) for hv, kv, *_r in GATE_REF]
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX/CCCV/CCCVII: %d == %d cells, "
          "h max %d == %d, decider + gate keys present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()),
             CENSUS_HMAX_REF, ok_keys),
          len(out) == CENSUS_N_REF
          and int(hs.max()) == CENSUS_HMAX_REF and ok_keys,
          kill="K3")
    roster = [c for c in out if BIN_LO < c["h"] <= BIN_HI]
    print("    THE BIN ROSTER (%d, %d], %d admissible census "
          "cells:" % (BIN_LO, BIN_HI, len(roster)))
    for c in roster:
        role = ("GATE/bin-sample" if (c["h"], c["kz"])
                == (GATE_REF[1][0], GATE_REF[1][1])
                else "DECIDER" if (c["h"], c["kz"]) == DECIDER
                else "extra" if (c["h"], c["kz"]) in EXTRAS
                else "UNROSTERED")
        print("      h %-6d kz %-4d alpha %.5f  est %.0f s  [%s]"
              % (c["h"], c["kz"], c["alpha"],
                 COST_C_ENV * float(c["h"]) ** 3, role))
    bin_keys = {(c["h"], c["kz"]) for c in roster}
    gate_bin = (GATE_REF[1][0], GATE_REF[1][1])
    rest = [(c["h"], c["kz"]) for c in roster
            if (c["h"], c["kz"]) not in (gate_bin, DECIDER)]
    rule_extras = tuple(rest[:MAX_EXTRA])
    check("D1a the frozen build keys are census bin cells and "
          "EXTRAS %s == the %d cheapest non-gate, non-decider "
          "roster cells %s (rule check)"
          % (EXTRAS, MAX_EXTRA, rule_extras),
          gate_bin in bin_keys and DECIDER in bin_keys
          and set(EXTRAS) <= bin_keys
          and (SMOKE or EXTRAS == rule_extras), kill="K3")
    return out, roster


def cell_legal(rung):
    """CCLXXIII/CCLXIX wall-legality of a single cell, VERBATIM."""
    if rung is None:
        return False, "NONE"
    if "fail" in rung:
        return False, rung["fail"]
    if not rung.get("core_ok"):
        return False, "CORE-SHORT"
    if rung["negA"] > 0:
        return False, "NEGA"
    if rung.get("lamS", -1.0) <= 0.0:
        return False, "LAMS"
    if rung["tau"] <= 0.0:
        return False, "TAU"
    return True, "OK"


def build_cell_world(cell, world=None, scr_seed=None):
    """The deployed deep-branch rung builder (bat.build_rung_param
    VERBATIM) with the CCLXXXVII world handling."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    rung = bat.build_rung_param(cell["kz"], alpha, mfold, uu, mm)
    rung["X"] = cell["X"]
    return rung


# ============================ the AC-scanned chain / entry readers
def chain_pass_values(al, be, m0, xnodes, wts, npoly, cvec):
    """CCCVII VERBATIM: one forward pass of the deployed three-term
    chain at xnodes (ob.eval_chain structure, accumulated instead of
    stored).  Nodes, weights, coefficients, frozen constants only."""
    xarr = np.asarray(xnodes, float)
    warr = np.asarray(wts, float)
    cvv = np.asarray(cvec, float)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    qv = cvv[0] * pkm1
    qabs = np.abs(cvv[0] * pkm1)
    dg = np.zeros(npoly)
    dg[0] = float(warr @ (pkm1 * pkm1))
    gmax = float(np.max(np.abs(pkm1)))
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        qv = qv + cvv[1] * pk
        qabs = qabs + np.abs(cvv[1] * pk)
        dg[1] = float(warr @ (pk * pk))
        gmax = max(gmax, float(np.max(np.abs(pk))))
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            qv = qv + cvv[k + 1] * pnew
            qabs = qabs + np.abs(cvv[k + 1] * pnew)
            dg[k + 1] = float(warr @ (pnew * pnew))
            gm = float(np.max(np.abs(pnew)))
            if gm > gmax:
                gmax = gm
            pkm1, pk = pk, pnew
    return qv, qabs, dg, gmax


def chain_pass_project(al, be, m0, xnodes, wts, npoly, fvals):
    """CCCVII VERBATIM: the transposed pass, out[k] = sum_i w_i
    p_k(x_i) f_i."""
    xarr = np.asarray(xnodes, float)
    wf = np.asarray(wts, float) * np.asarray(fvals, float)
    out = np.zeros(npoly)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    out[0] = float(wf @ pkm1)
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        out[1] = float(wf @ pk)
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            out[k + 1] = float(wf @ pnew)
            pkm1, pk = pk, pnew
    return out


def cd_bilinear(ynodes, aval, bval, becap, rtv, zvv, aref):
    """CCCVII VERBATIM: the Christoffel-Darboux entry route,
    blockwise."""
    yarr = np.asarray(ynodes, float)
    aa = np.asarray(aval, float)
    bb = np.asarray(bval, float)
    rt = np.asarray(rtv, float)
    zz = np.asarray(zvv, float)
    ndim = len(yarr)
    acc = 0.0
    dmax = 0.0
    nskip = 0
    for lo in range(0, ndim, CD_BLOCK):
        hi = min(lo + CD_BLOCK, ndim)
        dy = yarr[lo:hi, None] - yarr[None, :]
        num = (aa[lo:hi, None] * bb[None, :]
               - bb[lo:hi, None] * aa[None, :])
        bad = np.abs(dy) < CD_SEP
        nskip += int(np.sum(bad)) - (hi - lo)
        dy = np.where(bad, 1.0, dy)
        kern = (becap * num / dy) * rt[lo:hi, None] * rt[None, :]
        kern[bad] = 0.0
        acc += float(zz[lo:hi] @ (kern @ zz))
        blk = -aref[lo:hi, :].copy()
        for i in range(lo, hi):
            blk[i - lo, i] = 0.0
        blk[bad] = 0.0
        dmax = max(dmax, float(np.max(np.abs(kern - blk))))
        del dy, num, kern, blk, bad
    return acc, dmax, max(0, nskip)


def atom_census(uu, alpha, d_grid, x_val):
    """CCCVII VERBATIM: source completeness census."""
    umin = float(np.min(uu)) if len(uu) else float("nan")
    return dict(n_atoms=int(len(uu)),
                u_max=float(np.max(uu)) if len(uu) else float("nan"),
                two_alpha=2.0 * float(alpha),
                slack=2.0 * float(alpha)
                - (float(np.max(uu)) if len(uu) else float("nan")),
                complete_tab2=bool(x_val <= TAB2),
                margin_tab2=TAB2 / x_val,
                complete_deployed=bool(x_val <= EXT_DEPLOYED),
                margin_deployed=EXT_DEPLOYED / x_val,
                u_min=umin, d_grid=float(d_grid),
                refl_unreached=bool(umin >= d_grid))


def hull_census(xs, ys, vs, uf_n):
    """CCCVII VERBATIM: the support-hull read."""
    xlo, xhi = float(np.min(xs)), float(np.max(xs))
    ylo, yhi = float(np.min(ys)), float(np.max(ys))
    out = np.nonzero((ys < xlo) | (ys > xhi))[0]
    return dict(x_lo=xlo, x_hi=xhi, y_lo=ylo, y_hi=yhi,
                n_out=int(len(out)), breach=bool(len(out) > 0),
                gap_lo=ylo - xlo, gap_hi=xhi - yhi,
                seats=[(int(uf_n[j]), float(ys[j]), float(vs[j]))
                       for j in out[:4]])


# ============================ the dissect builder (CCCVII verbatim)
def build_cell_dissect(cell, world=None, keep_chain=False,
                       bottom_witness=False):
    """CCCVII build_cell_dissect VERBATIM (bat.build_rung_param
    sub-calls in the same order, Schur part inline) with the world
    handling of build_cell_world and the A6 control-only
    bottom_witness route (X2C).  Ties bat.build_rung_param EXACTLY
    on the TIE cell (TIE ward)."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka]
    mm = mu2[:ka]
    if world == "smooth":
        mm = ob.smooth_masses(uu)
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _uf_p, _fdp = ob.folded_measure_full(dens, lfold, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(dens, lfold, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    out = dict(kind="param", kz=cell["kz"], h=half,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               X=cell["X"], nsteps=int(nsteps),
               n_pos=int(len(xs)), n_neg=int(len(ys)),
               be_min=float(np.min(be)) if len(be) else float("nan"),
               atoms=atom_census(uu, alpha, d_grid, cell["X"]),
               hull=hull_census(xs, ys, vs, uf_n))
    out["n_drop"] = int(mfold - len(xs) - len(ys))
    if nsteps < half + 1 or np.any(be <= 0):
        out["fail"] = "CHAIN"
        return out
    if keep_chain:
        out["chain"] = dict(al=al, be=be, m0=m0, xs=xs, ws=ws,
                            npoly=half)
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = sym(gram)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    eva = np.linalg.eigvalsh(amat)
    out.update(n=n, tau=float(eva[0]), negA=int(np.sum(eva < 0.0)))
    out["eva_bot"] = [float(v) for v in eva[:4]]
    out["n_unit"] = int(np.sum(np.abs(eva - 1.0) <= UNIT_TIE))
    out["rank_g"] = int(half)
    del gram
    # ---- inertia route 2: exact-sign LDL block pivot count (A13)
    try:
        lu_l, dblk, _perm = sla.ldl(amat, lower=True)
        n_neg_ldl, n_zero, n_two = ldl_inertia(dblk)
        out["inertia"] = dict(neg_ldl=n_neg_ldl, neg_eig=out["negA"],
                              n_2x2=n_two, n_zero=n_zero,
                              agree=bool(n_neg_ldl == out["negA"]
                                         and n_zero == 0))
        del lu_l, dblk
    except Exception as exc:                       # noqa: BLE001
        out["inertia"] = dict(refused=type(exc).__name__,
                              agree=False)
    # ---- localization: LU inverse iteration (A6); the X2C control
    #      uses the direct bottom eigenpair instead (disclosed)
    zvec = None
    if bottom_witness:
        try:
            wbt, vbt = sla.eigh(amat, subset_by_index=[0, 0])
            zvec = vbt[:, 0]
            rq = float(wbt[0])
            out["loc"] = dict(rq=rq, rq_gap=abs(rq - out["tau"]),
                              res=float(np.linalg.norm(
                                  amat @ zvec - rq * zvec)),
                              ipr=float("nan"), seats=[],
                              uf=-1, part=float("nan"),
                              cum2=float("nan"), core_top=False,
                              route="eigh-bottom (A6 control)")
        except Exception as exc:                   # noqa: BLE001
            out["loc"] = dict(refused=type(exc).__name__)
    else:
        try:
            lu, piv = sla.lu_factor(amat)
            zvec = np.full(n, 1.0 / math.sqrt(n))
            for _ in range(LOC_ITERS):
                zvec = sla.lu_solve((lu, piv), zvec)
                zvec = zvec / float(np.linalg.norm(zvec))
            rq = float(zvec @ (amat @ zvec))
            res = float(np.linalg.norm(amat @ zvec - rq * zvec))
            p4 = float(np.sum(zvec ** 4))
            order = np.argsort(-np.abs(zvec))
            core_set = set(int(j) for j in ob.CORE_J)
            cum2 = 0.0
            n_core = 0
            for j in order:
                if int(uf_n[j]) in core_set:
                    cum2 += float(zvec[j]) ** 2
                    n_core += 1
                if n_core >= 2:
                    break
            out["loc"] = dict(
                rq=rq, rq_gap=abs(rq - out["tau"]), res=res,
                ipr=1.0 / p4 if p4 > 0 else float("nan"),
                seats=[(int(uf_n[j]), float(ys[j]),
                        float(abs(zvec[j]))) for j in order[:3]],
                uf=int(uf_n[order[0]]),
                part=float(abs(zvec[order[0]])),
                cum2=math.sqrt(cum2),
                core_top=bool(int(uf_n[order[0]]) in core_set))
            del lu, piv
        except Exception as exc:                   # noqa: BLE001
            out["loc"] = dict(refused=type(exc).__name__)
    # ---- the metric-corrected IDEAL tier + the CD entry route
    if zvec is not None:
        out["ideal"] = ideal_tier(al, be, m0, xs, ws, ys, vs, pn,
                                  half, zvec, out["tau"])
        out["cd"] = cd_route(al, be, m0, ys, vs, pn, half, zvec,
                             amat, out["tau"])
    del pn
    # ---- the Schur part, bat.build_rung_param VERBATIM
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in ob.CORE_J)
    if not out["core_ok"]:
        out["fail"] = "CORE-SHORT"
        return out
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset], dtype=int)
    bblk = amat[np.ix_(ic, ic)]
    xc = amat[np.ix_(ic, ib)]
    rblk = amat[np.ix_(ib, ib)]
    try:
        zsol = np.linalg.solve(rblk, xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        out["fail"] = "R-SINGULAR"
        return out
    smat = sym(bblk - xc @ zsol)
    evs = np.linalg.eigvalsh(smat)
    out["lamS"] = float(evs[0])
    out["negS"] = int(np.sum(evs < 0.0))
    return out


def ideal_tier(al, be, m0, xs, ws, ys, vs, pn, npoly, zvec, tau):
    """CCCVII VERBATIM (incl. A13 O-metric refinement): the
    metric-corrected ideal Galerkin read at the bad-mode witness,
    with outward-rounded enclosures of both quadrature scalars."""
    svec = np.sqrt(vs) * zvec
    cvec = pn.T @ svec                       # c = P^T sqrt(V) z
    cn2 = float(cvec @ cvec)
    qv, qabs, dg, gmax = chain_pass_values(al, be, m0, xs, ws,
                                           npoly, cvec)
    ip_plus = float(ws @ (qv * qv))
    g_h = gamma_n(npoly)
    g_p = gamma_n(len(xs))
    dq = g_h * np.abs(qabs)
    lo_terms = ws * np.maximum(np.abs(qv) - dq, 0.0) ** 2
    hi_terms = ws * (np.abs(qv) + dq) ** 2
    ip_lo = float(np.sum(lo_terms)) * (1.0 - g_p)
    ip_hi = float(np.sum(hi_terms)) * (1.0 + g_p)
    g_n = gamma_n(len(ys))
    cn2_lo = cn2 * (1.0 - gamma_n(npoly))
    cn2_hi = cn2 * (1.0 + gamma_n(npoly))
    dgap = ip_plus - cn2
    lam = 1.0 - tau
    tau_ub = 1.0 - lam * lam / max(lam + dgap, 1e-300)
    tau_ub_lo = 1.0 - lam * lam / max(lam + (ip_lo - cn2_hi), 1e-300)
    tau_ub_hi = 1.0 - lam * lam / max(lam + (ip_hi - cn2_lo), 1e-300)
    res = dict(cn2=cn2, ip_plus=ip_plus, d=dgap,
               d_lo=ip_lo - cn2_hi, d_hi=ip_hi - cn2_lo,
               tau_ub=tau_ub,
               tau_ub_lo=min(tau_ub_lo, tau_ub_hi),
               tau_ub_hi=max(tau_ub_lo, tau_ub_hi),
               dg_dev=float(np.max(np.abs(dg - 1.0))),
               dg_dev_k=int(np.argmax(np.abs(dg - 1.0))),
               dg_last=float(dg[-1]), p_growth=gmax,
               cancel=float(np.max(qabs) / max(1e-300,
                                              float(np.max(
                                                  np.abs(qv))))),
               gam_h=g_h, gam_pos=g_p, gam_neg=g_n)
    rng = np.random.default_rng(OPROBE_SEED)
    rvec = rng.standard_normal(npoly)
    rvec = rvec / float(np.linalg.norm(rvec))
    rq_v, _ra, _rd, _rg = chain_pass_values(al, be, m0, xs, ws,
                                            npoly, rvec)
    orv = chain_pass_project(al, be, m0, xs, ws, npoly, rq_v)
    res["oprobe"] = float(np.linalg.norm(orv - rvec))
    # ---- NREF refinement, every iterate in the O METRIC (A13)
    cc = cvec / max(1e-300, float(np.linalg.norm(cvec)))
    best = tau_ub
    hist = []
    for _ in range(NREF):
        hc = pn.T @ (vs * (pn @ cc))          # H c, the ascent step
        nh = float(np.linalg.norm(hc))
        if not math.isfinite(nh) or nh <= 0.0:
            break
        cc = hc / nh
        qv2, _qa2, _dg2, _gm2 = chain_pass_values(
            al, be, m0, xs, ws, npoly, cc)
        occ = float(ws @ (qv2 * qv2))         # c^T O c
        hcc = pn.T @ (vs * (pn @ cc))
        num = float(cc @ hcc)                 # c^T H c
        if occ > 0.0 and math.isfinite(num):
            val = 1.0 - num / occ
            hist.append(val)
            best = min(best, val)
    res["tau_ub_ref"] = best
    res["ref_hist"] = hist
    return res


def cd_route(al, be, m0, ys, vs, pn, npoly, zvec, amat, tau):
    """CCCVII VERBATIM: the Christoffel-Darboux entry route."""
    if npoly < 3:
        return dict(skipped="npoly<3")
    pm1 = pn[:, npoly - 1]
    pm2 = pn[:, npoly - 2]
    ph = ((ys - al[npoly - 1]) * pm1 - be[npoly - 2] * pm2) \
        / be[npoly - 1]
    off, dmax, nskip = cd_bilinear(ys, ph, pm1, float(be[npoly - 1]),
                                   np.sqrt(vs), zvec, amat)
    diag = float(np.sum(zvec * zvec * (1.0 - np.diag(amat))))
    rq_cd = 1.0 - (off + diag)
    return dict(rq_cd=rq_cd, gap=rq_cd - tau, ent_dev=dmax,
                n_skip=nskip,
                rel=abs(rq_cd - tau) / max(1.0, abs(tau)))


# ================================ the corrected type + eligibility
def ideal_type(rung):
    """THE CORRECTED TYPE RULE (CCCXVII frozen, verbatim)."""
    idl = rung.get("ideal")
    if idl is None:
        return "NO-IDEAL"
    ref = idl.get("tau_ub_ref", float("nan"))
    hi = idl.get("tau_ub_hi", float("nan"))
    if not math.isfinite(ref):
        return "NO-IDEAL"
    if ref < -IDEAL_NOISE and math.isfinite(hi) and hi < -IDEAL_NOISE:
        return "IDEAL-WITNESS-NEGA"
    if ref < -IDEAL_NOISE:
        return "IDEAL-LEAN-NEGA"
    if ref > IDEAL_NOISE:
        return "NO-WITNESS-POS"
    return "IDEAL-UNRESOLVED"


def eligible(read):
    """Corrected eligibility (CCCXVII frozen): raw LEGAL and
    NO-WITNESS-POS."""
    return (read["verdict"] == "LEGAL"
            and read["itype"] == "NO-WITNESS-POS")


def print_cell(rung):
    lc = rung.get("loc", {})
    idl = rung.get("ideal")
    cdr = rung.get("cd")
    ine = rung.get("inertia", {})
    if "refused" in ine:
        print("      inertia: LDL-REFUSED (%s)" % ine["refused"])
    else:
        print("      inertia: negA(eigvalsh) %d vs negA(exact LDL) "
              "%d [%s] 2x2 %d zero %d"
              % (ine.get("neg_eig", -1), ine.get("neg_ldl", -1),
                 "AGREE" if ine.get("agree") else "SPLIT",
                 ine.get("n_2x2", -1), ine.get("n_zero", -1)))
    if "rq_gap" in lc:
        print("      loc: rq %.6e rq_gap %.2e res %.2e seat uf=%s "
              "part %s seats %s"
              % (lc["rq"], lc["rq_gap"], lc["res"], lc.get("uf"),
                 ("%.3f" % lc["part"])
                 if math.isfinite(lc.get("part", float("nan")))
                 else "-",
                 [(s[0], "%.3f" % s[2]) for s in
                  lc.get("seats", [])]))
    elif lc:
        print("      loc: LOCALIZATION-REFUSED (%s)"
              % lc.get("refused"))
    if idl is not None:
        print("      IDEAL: |c|^2 %.16f  int q^2 dmu+ %.16f"
              % (idl["cn2"], idl["ip_plus"]))
        print("      IDEAL: d %+.6e outward [%+.6e, %+.6e] (width "
              "%.2e)" % (idl["d"], idl["d_lo"], idl["d_hi"],
                         idl["d_hi"] - idl["d_lo"]))
        print("      IDEAL: tau %+.6e -> tau_ideal_ub %+.6e outward "
              "[%+.6e, %+.6e] refined %+.6e"
              % (rung["tau"], idl["tau_ub"], idl["tau_ub_lo"],
                 idl["tau_ub_hi"], idl["tau_ub_ref"]))
        print("      METRIC: max_k |diag(O)_k - 1| %.3e at k %d "
              "||(O-I)r|| %.3e growth %.3e cancel %.3e"
              % (idl["dg_dev"], idl["dg_dev_k"], idl["oprobe"],
                 idl["p_growth"], idl["cancel"]))
    if cdr is not None and "rq_cd" in cdr:
        print("      CD: rq_cd %+.6e vs tau %+.6e rel %.3e | entry "
              "dev %.3e skipped %d"
              % (cdr["rq_cd"], rung["tau"], cdr["rel"],
                 cdr["ent_dev"], cdr["n_skip"]))
    print("", end="", flush=True)


def pass_tie(tie_cell):
    """PASS-TIE (CCCVII verbatim): the AC-scanned accumulator must
    tie ob.eval_chain on the TIE cell."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = tie_cell["alpha"], tie_cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    d_grid = 2.0 * alpha / mfold
    lag = (np.asarray(core.arch_lags(mfold, d_grid), float)
           + np.asarray(core.atom_lags_at(alpha, mfold, u2[:ka],
                                          mu2[:ka])[0], float))
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _u, _f = ob.folded_measure_full(dens, lfold, +1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1:
        check("PASS-TIE chain short on the TIE cell", False,
              kill="K1")
        return
    rng = np.random.default_rng(OPROBE_SEED)
    cvec = rng.standard_normal(half)
    ref = ob.eval_chain(al, be, m0, xs, half) @ cvec
    got, _qa, dg, _gm = chain_pass_values(al, be, m0, xs, ws, half,
                                          cvec)
    dev = float(np.max(np.abs(got - ref)))
    ogram = ob.eval_chain(al, be, m0, xs, half)
    dg_ref = np.einsum("ik,i,ik->k", ogram, ws, ogram)
    ddev = float(np.max(np.abs(dg - dg_ref)))
    check("PASS-TIE the accumulator ties ob.eval_chain on the TIE "
          "cell (q dev %.2e, diag(O) dev %.2e)"
          % (dev, ddev),
          dev <= 1e-12 * max(1.0, float(np.max(np.abs(ref))))
          and ddev <= 1e-12, kill="K2")


# ==================================== the build roster + the gates
def tie_ward(census):
    hs = np.asarray([c["h"] for c in census], float)
    tie_cell = census[int(np.argmin(np.abs(hs - TIE_TGT)))]
    r_bat = build_cell_world(tie_cell)
    r_dis = build_cell_dissect(tie_cell, keep_chain=True)
    check("TIE dissect builder ties bat.build_rung_param EXACTLY on "
          "h %d kz %d (tau %s negA %s lamS %s)"
          % (tie_cell["h"], tie_cell["kz"],
             "==" if r_dis["tau"] == r_bat["tau"] else "DIFF",
             "==" if r_dis["negA"] == r_bat["negA"] else "DIFF",
             "==" if r_dis.get("lamS") == r_bat.get("lamS")
             else "DIFF"),
          (r_dis["tau"] == r_bat["tau"]
           and r_dis["negA"] == r_bat["negA"]
           and r_dis.get("lamS") == r_bat.get("lamS")), kill="K2")
    pass_tie(tie_cell)
    print_cell(r_dis)
    ok_t, why_t = cell_legal(r_dis)
    return dict(tag="TIE", cell=tie_cell,
                verdict="LEGAL" if ok_t else why_t, why=why_t,
                rung=r_dis, marginal=False, itype=ideal_type(r_dis))


def build_one(tag, cell):
    tc = time.time()
    rung = build_cell_dissect(cell)
    dt = time.time() - tc
    ok, why = cell_legal(rung)
    marginal = ("tau" in rung and abs(rung["tau"]) <= TAU_NOISE)
    verdict = ("MARGINAL" if marginal else "LEGAL" if ok else why)
    itype = ideal_type(rung)
    read = dict(tag=tag, cell=cell, verdict=verdict, why=why,
                rung=rung, marginal=marginal, itype=itype, dt=dt)
    print("    %-11s h %-6d kz %-4d alpha %.4f  %-9s tau %-12s "
          "negA %s  %-18s %.1f s"
          % (tag, cell["h"], cell["kz"], cell["alpha"], verdict,
             ("%.4g" % rung["tau"]) if "tau" in rung else "-",
             rung.get("negA", "-"), itype, dt), flush=True)
    print_cell(rung)
    return read


def census_build(census, roster):
    section("CEN -- THE ROSTER BUILDS (gates, then the DECIDER, "
            "then extras ascending cost; self-calibrating guard "
            "%.2f * c_hat * h^3 <= %.0f s)" % (GUARD_FAC,
                                               BUILD_CAP_S))
    by_key = {(c["h"], c["kz"]): c for c in census}
    if SMOKE:
        hs = np.asarray([c["h"] for c in census], float)
        c22 = census[int(np.argmin(np.abs(hs - 2200)))]
        queue = [("SMOKE-B", c22, False)]
    else:
        queue = [("G1-8629L", by_key[(8629, 223)], False),
                 ("G2-9535N", by_key[(9535, 526)], False),
                 ("DECIDER", by_key[DECIDER], True)]
        for i, key in enumerate(EXTRAS[:MAX_EXTRA]):
            queue.append(("EXTRA-%d" % (i + 1), by_key[key], True))
    reads = []
    c_hat = COST_C_ENV
    deep_rate = []
    for tag, cell, guarded in queue:
        est = GUARD_FAC * c_hat * float(cell["h"]) ** 3
        if guarded and time.time() - T0 + est > BUILD_CAP_S:
            print("    %-11s h %-6d kz %-4d UNBUILT-GUARD (est "
                  "%.0f s at c_hat %.2e, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est, c_hat,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            reads.append(dict(tag=tag, cell=cell, verdict="UNBUILT",
                              why="UNBUILT-GUARD", rung=None,
                              itype="UNBUILT"))
            continue
        read = build_one(tag, cell)
        reads.append(read)
        if cell["h"] >= 5000:
            deep_rate.append(read["dt"] / float(cell["h"]) ** 3)
            c_hat = 1.05 * max(deep_rate)
    n_built = sum(1 for r in reads if r["rung"] is not None)
    check("CEN1 the roster built %d items (%d unbuilt-guard, "
          "honestly censused)" % (n_built, len(reads) - n_built),
          n_built >= (1 if SMOKE else 3), kill="K1")
    return reads, c_hat


def gates(reads):
    section("G -- reproduction gates on the two shared cells "
            "(CCCVII tau/d prints, CCCXVII refined-read print)")
    if SMOKE:
        check("G reproduction SMOKE-SKIPPED (typed; no gate cell is "
              "built in smoke)", True)
        return
    got = {(r["cell"]["h"], r["cell"]["kz"]): r for r in reads
           if r["rung"] is not None}
    for hv, kv, tref, vref, dref, uref, urtol, iref in GATE_REF:
        r = got.get((hv, kv))
        if r is None:
            check("G gate cell h %d kz %d BUILT" % (hv, kv), False,
                  kill="K3")
            continue
        tau = r["rung"].get("tau", float("nan"))
        idl = r["rung"].get("ideal") or {}
        dv = idl.get("d", float("nan"))
        uv = idl.get("tau_ub_ref", float("nan"))
        ok_t = (math.isfinite(tau)
                and abs(tau / tref - 1.0) <= NEGA_RTOL
                and r["verdict"] == vref)
        ok_d = (math.isfinite(dv)
                and abs(dv / dref - 1.0) <= REPRO_D)
        ok_u = (math.isfinite(uv)
                and abs(uv / uref - 1.0) <= urtol)
        ok_i = (r["itype"] == iref)
        check("G repro h %d kz %d [%s/%s]: tau %.6e vs %.4g, "
              "d %.6e vs %.5g (rel %.1e), ideal %.6e vs %.5g "
              "(rel %.1e, rtol %.0e), type %s"
              % (hv, kv, vref, iref, tau, tref, dv, dref,
                 abs(dv / dref - 1.0) if math.isfinite(dv)
                 else float("nan"),
                 uv, uref,
                 abs(uv / uref - 1.0) if math.isfinite(uv)
                 else float("nan"), urtol, r["itype"]),
              ok_t and ok_d and ok_u and ok_i, kill="K3")


def anatomy_wards(reads, tie_entry):
    section("AN/WO -- anatomy + outward-rounding wards on every "
            "built cell")
    rows = [r for r in reads if r["rung"] is not None
            and "tau" in r["rung"]] + [tie_entry]
    n_rank = n_e8 = n_acc = n_out = n_tot = 0
    for r in rows:
        rung = r["rung"]
        n_tot += 1
        expect = max(0, rung["n_neg"] - rung["rank_g"])
        if rung.get("n_unit", 0) >= expect:
            n_rank += 1
        if rung["tau"] <= 0.0 or (
                rung.get("lamS") is not None
                and rung["lamS"] >= rung["tau"]
                - 1e-12 * max(1.0, abs(rung["tau"]))):
            n_e8 += 1
        if rung["n_pos"] + rung["n_neg"] + rung["n_drop"] == rung["M"]:
            n_acc += 1
        idl = rung.get("ideal")
        if idl is not None:
            ok_o = (idl["d_lo"] <= idl["d"] <= idl["d_hi"]
                    and idl["tau_ub_lo"] <= idl["tau_ub"]
                    <= idl["tau_ub_hi"]
                    and idl["tau_ub_ref"] <= idl["tau_ub"]
                    and math.isfinite(idl["d_hi"] - idl["d_lo"])
                    and math.isfinite(idl["tau_ub_hi"]
                                      - idl["tau_ub_lo"]))
            if ok_o:
                n_out += 1
        else:
            n_out += 1          # no ideal read, nothing to ward
    check("W7 RANK IDENTITY #unit >= max(0, n_neg - h) on %d/%d "
          "built cells" % (n_rank, n_tot), n_rank == n_tot,
          kill="K2")
    check("W8 E8 ward lamS >= tau on every built PD cell (%d/%d; "
          "consumed nowhere)" % (n_e8, n_tot), n_e8 == n_tot,
          kill="K2")
    check("W9 NODE ACCOUNTING M == n_pos + n_neg + n_dropped on "
          "%d/%d built cells" % (n_acc, n_tot), n_acc == n_tot,
          kill="K2")
    check("WO OUTWARD DISCIPLINE d in [d_lo, d_hi], ub in [lo, hi], "
          "ref <= ub, finite widths on %d/%d built cells"
          % (n_out, n_tot), n_out == n_tot, kill="K2")


# =========================== the map, the ladder and the verdict
def bin_table(reads):
    section("MAP -- THE CORRECTED-TIER TABLE (this run) + THE "
            "UPDATED LADDER + THE SEAT READ")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"]]
    built.sort(key=lambda r: r["cell"]["h"])
    print("    h      kz   alpha    raw       tau          "
          "d            [outward d]                  tau_ub_ref   "
          "[outward ub]                  type                elig")
    for r in built:
        idl = r["rung"].get("ideal") or {}
        r["elig"] = eligible(r)
        print("    %-6d %-4d %.5f %-9s %+.4e %+.4e [%+.4e,%+.4e] "
              "%+.4e [%+.4e,%+.4e] %-19s %s"
              % (r["cell"]["h"], r["cell"]["kz"], r["cell"]["alpha"],
                 r["verdict"], r["rung"]["tau"],
                 idl.get("d", float("nan")),
                 idl.get("d_lo", float("nan")),
                 idl.get("d_hi", float("nan")),
                 idl.get("tau_ub_ref", float("nan")),
                 idl.get("tau_ub_lo", float("nan")),
                 idl.get("tau_ub_hi", float("nan")),
                 r["itype"], "YES" if r["elig"] else "no"))
    bin_reads = [r for r in reads
                 if BIN_LO < r["cell"]["h"] <= BIN_HI]
    bin_built = [r for r in bin_reads if r["rung"] is not None]
    # ---- the seat read (anatomy observation, consumed nowhere)
    print("\n    SEAT LOCALIZATION (does the migrating-seat anatomy "
          "continue?):")
    for r in built:
        lc = r["rung"].get("loc", {})
        if "rq_gap" in lc:
            print("      h %-6d kz %-4d seat uf=%-6s part %.3f "
                  "ipr %.1f core_top %s seats %s"
                  % (r["cell"]["h"], r["cell"]["kz"], lc.get("uf"),
                     lc.get("part", float("nan")),
                     lc.get("ipr", float("nan")),
                     lc.get("core_top"),
                     [(s[0], "%.3f" % s[2]) for s in
                      lc.get("seats", [])]))
    # ---- the CONJECTURE-GRADE drift comparison (print, no gate)
    for r in bin_built:
        idl = r["rung"].get("ideal") or {}
        if math.isfinite(idl.get("d", float("nan"))):
            dout = max(abs(idl["d_lo"]), abs(idl["d_hi"]))
            print("      drift check h %d: outward |d| %.3e vs the "
                  "CCCXVII extrapolation ~%.1e at h 10500 "
                  "[CONJECTURE-GRADE print, no gate]"
                  % (r["cell"]["h"], dout, DRIFT_EXTRAP))
    # ---- the updated ladder
    print("\n    THE UPDATED SUB-LADDER (MAX-TAU_IDEAL_UB-PER-BIN "
          "over eligible cells; shallow bins = FROZEN CCCXVII "
          "facts, cited):")
    for (lo, hi), hp, kp, ub in CCCXVII_LADDER:
        if hp is None:
            print("      bin (%6d, %6d]: NO SAMPLE (CCCXVII, 7004 "
                  "guard-refused there)" % (lo, hi))
        else:
            print("      bin (%6d, %6d]: pick h %d kz %d ub_ref "
                  "%+.4e [CCCXVII frozen]" % (lo, hi, hp, kp, ub))
    el = [r for r in bin_built if r.get("elig")]
    pick = max(el, key=lambda r: r["rung"]["ideal"]["tau_ub_ref"],
               default=None)
    print("      bin (%6d, %6d]: %d built THIS RUN, %d eligible%s"
          % (BIN_LO, BIN_HI, len(bin_built), len(el),
             ("; corrected pick h %d kz %d ub_ref %+.4e"
              % (pick["cell"]["h"], pick["cell"]["kz"],
                 pick["rung"]["ideal"]["tau_ub_ref"]))
             if pick else "; NO eligible cell"))
    h_corr = (max(r["cell"]["h"] for r in el)
              if el else H_LAST)
    print("      corrected horizon h*_corr = %d (%s)"
          % (h_corr, "EXTENDED past 8629 by this run" if el
             else "unchanged: the CCCXVII anchor 8629"))
    return built, bin_built, h_corr


def updated_verdict(bin_built):
    if SMOKE:
        return "CORRECTED-SMOKE(no bin cell built by design)"
    el = [r for r in bin_built if r.get("elig")]
    if el:
        h_new = max(r["cell"]["h"] for r in el)
        return ("CORRECTED-CONTINUES(h*_new = %d; an eligible "
                "raw-LEGAL NO-WITNESS-POS cell extends the "
                "corrected sub-ladder past %d)" % (h_new, H_LAST))
    if len(bin_built) >= 2:
        all_wit = all(r["itype"] == "IDEAL-WITNESS-NEGA"
                      for r in bin_built)
        if all_wit:
            return ("CORRECTED-TERMINATES(h_last = %d; the bin "
                    "(%d, %d] is witness-NEGA throughout on %d "
                    "built cells and the frozen CCCXVII beyond-set "
                    "8677/9023/9447 stands: the deployed family's "
                    "ideal legality genuinely ends at %d ON THE "
                    "BUILT SET -- a construction fact, not an "
                    "all-h statement)"
                    % (H_LAST, BIN_LO, BIN_HI, len(bin_built),
                       H_LAST))
        soft = [(r["cell"]["h"], r["itype"]) for r in bin_built
                if r["itype"] != "IDEAL-WITNESS-NEGA"]
        widths = []
        for r in bin_built:
            idl = r["rung"].get("ideal") or {}
            wd = idl.get("tau_ub_hi", float("nan")) \
                - idl.get("tau_ub_lo", float("nan"))
            widths.append((r["cell"]["h"], wd))
        return ("STILL-AMBIGUOUS(non-witness bin cells %s; "
                "enclosure widths %s -- the precision that would "
                "decide)" % (soft,
                             [(hh, "%.1e" % w) for hh, w in widths]))
    return ("STILL-AMBIGUOUS(only %d built bin cell(s); the "
            "decider build did not complete)" % len(bin_built))


# ==================================================== controls
def controls(census, tie_entry):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth AT "
            "THE DECIDER, X2C smooth CORRECTED, XO doctored "
            "recurrence, XD doctored metric)")
    tie_rung = tie_entry["rung"]
    hs = np.asarray([c["h"] for c in census], float)
    tgt = 600 if SMOKE else XCTRL_TGT
    cell = census[int(np.argmin(np.abs(hs - tgt)))]
    scr = build_cell_world(cell, world="scramble", scr_seed=SCR_SEED)
    ok_s, why_s = cell_legal(scr)
    print("    scramble world h %d kz %d (seed %d): legal %s (%s) "
          "tau %s" % (cell["h"], cell["kz"], SCR_SEED, ok_s, why_s,
                      ("%.4g" % scr["tau"]) if "tau" in scr else "-"))
    check("X1 the SCRAMBLE world fires: legality LEFT", not ok_s,
          kill="K4")
    if SMOKE:
        cheap = census[int(np.argmin(np.abs(hs - 600)))]
    else:
        by_key = {(c["h"], c["kz"]): c for c in census}
        cheap = by_key[DECIDER]
    smo = build_cell_dissect(cheap, world="smooth",
                             bottom_witness=True)
    ok, why = cell_legal(smo)
    print("    SMOOTH world h %d kz %d: legal %s (%s) tau %s"
          % (cheap["h"], cheap["kz"], ok, why,
             ("%.4g" % smo["tau"]) if "tau" in smo else "-"))
    check("X2 the SMOOTH (prime-free) world fires AT THE DECIDER "
          "DEPTH h %d: legality LEFT" % cheap["h"],
          (not ok) and "tau" in smo, kill="K4")
    idl_s = smo.get("ideal") or {}
    ref_s = idl_s.get("tau_ub_ref", float("nan"))
    lc_s = smo.get("loc", {})
    print("    X2C smooth CORRECTED tier (eigh-bottom witness, A6): "
          "tau %s d %s -> tau_ideal_ub refined %s (rq_gap %s)"
          % (("%.4g" % smo["tau"]) if "tau" in smo else "-",
             ("%.4g" % idl_s.get("d", float("nan")))
             if idl_s else "-",
             ("%.4g" % ref_s) if math.isfinite(ref_s) else "-",
             ("%.1e" % lc_s["rq_gap"]) if "rq_gap" in lc_s else "-"))
    check("X2C the metric correction does NOT rescue the smooth "
          "world at the decider depth: tau_ideal_ub refined %s < "
          "%.1f -- THE DISCRIMINATION persists"
          % (("%.4g" % ref_s) if math.isfinite(ref_s) else "-",
             X2C_BAR),
          math.isfinite(ref_s) and ref_s < X2C_BAR, kill="K4")
    # ---- XO: the faithfulness reader must have teeth (CCCVII)
    ch = tie_rung.get("chain")
    dev_ok = (tie_rung.get("ideal") or {}).get("dg_dev",
                                               float("nan"))
    dev_xo = float("nan")
    if ch is not None:
        be2 = np.array(ch["be"], float)
        kdope = max(1, ch["npoly"] // 2)
        be2[kdope] = be2[kdope] * (1.0 + XO_DOPE)
        _q, _qa, dg2, _g = chain_pass_values(
            ch["al"], be2, ch["m0"], ch["xs"], ch["ws"],
            ch["npoly"], np.zeros(ch["npoly"]))
        dev_xo = float(np.max(np.abs(dg2 - 1.0)))
    check("XO the ORTHOGONALITY/faithfulness reader FIRES on a "
          "DOCTORED recurrence (%.3e > %.0e >= %.3e)"
          % (dev_xo, ORTHO_BAR, dev_ok),
          math.isfinite(dev_xo) and dev_xo > ORTHO_BAR
          and math.isfinite(dev_ok) and dev_ok <= ORTHO_BAR,
          kill="K4")
    # ---- XD: the doctored metric must move the ideal read (CCCVII)
    idl = tie_rung.get("ideal") or {}
    d_ref = idl.get("d", float("nan"))
    d_dope = d_ref + XD_DOPE * idl.get("cn2", 0.0)
    lam = 1.0 - tie_rung["tau"]
    tub_ref = 1.0 - lam * lam / max(lam + d_ref, 1e-300)
    tub_dope = 1.0 - lam * lam / max(lam + d_dope, 1e-300)
    check("XD the DOCTORED metric (O -> O + %.0e I) moves the "
          "ideal read by %.3e >> the frozen bar %.0e"
          % (XD_DOPE, abs(tub_dope - tub_ref), IDEAL_NOISE),
          abs(tub_dope - tub_ref) > 10.0 * IDEAL_NOISE, kill="K4")


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        vmap = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}
        print("\n  VERDICT: %s" % vmap[KILLS[0]])
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements with OUTWARD-ROUNDED
  enclosures of the decisive scalars, on BUILT cells of the deployed
  deep-frame construction.  The corrected tier is the CCCVII
  metric-corrected Galerkin object, reused verbatim: its negative
  reads are WITNESSES, its positive reads are only "no witness
  found" -- positivity of the ideal object is NOT certified, so the
  corrected map can only REMOVE cells from the legal ladder, never
  add any.  A TERMINATES verdict is a statement about the BUILT
  cells of the deployed family -- the construction's ideal legality
  ends on the built set -- never about all h, never about zeta.
  The residual ideality question (chain-column representation
  accuracy) is measured indirectly and remains the named scope
  edge.  The K-membership tier is not run (A7, cited).  No marker
  moves, no promotion, NO RH claim, NO counterexample claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("decider_cell_probe -- PRIME.COFINAL.DECIDER.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the chain/CD/census readers see nodes, weights, "
          "entries, coefficients and frozen constants only (%s)"
          % (",".join(sorted(set(bad_r))) or "clean"), not bad_r,
          kill="K1")

    build_tab2()
    if KILLS:
        return finish([])
    census, roster = deep_census()
    if KILLS:
        return finish([])

    section("TIE -- the dissect builder ward on the TIE cell "
            "(nearest h %d)" % TIE_TGT)
    tie_entry = tie_ward(census)
    if KILLS:
        return finish([])

    reads, c_hat = census_build(census, roster)
    if KILLS:
        return finish([])
    gates(reads)
    anatomy_wards(reads, tie_entry)
    if any(k in ("K1", "K2") for k in KILLS):
        return finish([])       # a broken pipeline/ward cannot be
        #                         mapped; a REPRODUCTION or CONTROL
        #                         kill still prints every
        #                         measurement (CCCVII A13)

    built, bin_built, h_corr = bin_table(reads)
    verdict = updated_verdict(bin_built)
    controls(census, tie_entry)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (census + decider cells only, "
          "declared)", True)

    if SMOKE:
        return finish(["CORRECTED-SMOKE(no bin cell built by "
                       "design)"])
    n_bin_built = len(bin_built)
    n_unbuilt = sum(1 for r in reads if r["rung"] is None)
    labels = [verdict,
              "BIN-CENSUS(%d admissible cells in (%d, %d]; %d "
              "built this run, %d unbuilt-guard)"
              % (len(roster), BIN_LO, BIN_HI, n_bin_built,
                 n_unbuilt),
              "LADDER(h*_corr %d; shallow bins frozen CCCXVII)"
              % h_corr]
    ds = []
    for r in bin_built:
        idl = r["rung"].get("ideal") or {}
        if math.isfinite(idl.get("d", float("nan"))):
            ds.append(max(abs(idl["d_lo"]), abs(idl["d_hi"])))
    if ds:
        labels.append("IDEALITY(bin outward |d| %.2e..%.2e vs "
                      "CCCXVII extrapolation ~%.1e [fit])"
                      % (min(ds), max(ds), DRIFT_EXTRAP))
    seats = []
    for r in bin_built:
        lc = r["rung"].get("loc", {})
        if "uf" in lc:
            seats.append("h %d uf %s" % (r["cell"]["h"],
                                         lc.get("uf")))
    labels.append("SEAT(%s; observation, consumed nowhere)"
                  % "; ".join(seats))
    labels.append("MEMBERSHIP-NOT-RUN(A7, cited)")
    return finish(labels)


if __name__ == "__main__":
    main()
