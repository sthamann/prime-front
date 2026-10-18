#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""metric_map_probe -- PRIME.COFINAL.METRIC.MAP.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim.  2026-08-13.)

REDRAW THE FRONTIER LEGALITY MAP WITH THE METRIC-CORRECTED IDEAL
TIER.  CCCVII (cofinal_dissect_probe) proved that the deployed Gram
builder assembles A = I - sqrt(V) P P^T sqrt(V), i.e. it assumes
O = I, while the IDEAL Galerkin restriction carries the metric
O = int p p^T dmu_+; because the chain columns are exactly a
triangular degree-graded family, the metric is the ONLY ideality gap
of the Gram, it reduces in the direction of the bad mode to the ONE
scalar
    d = c^T (O - I) c = int q^2 dmu_+ - |c|^2,
    c = P^T sqrt(V) z   (z the float64 bottom mode of A),
and with lam = 1 - tau the ideal Rayleigh read at the same witness is
EXACTLY
    R_ideal = lam^2 / (lam + d),   tau_ideal_ub = 1 - R_ideal
                                              >= tau_ideal.
CCCVII measured |d|/|tau| = 0.014..3.15 at the frontier and TWO of
nine cells FLIP the sign (8003 NEGA -> ideal POSITIVE-lean, 7958
LEGAL -> ideal negative WITNESS); the float64 sign was metric-robust
only for |tau| >= 1.412e-10 on the built set.  CONSEQUENCE: the
CCXCIX/CCCV legality map on the +-1e-10 scale (the scattered holes,
the sub-ladder to h 8204, the termination signal beyond it) is
PARTLY A METRIC ARTIFACT and must be redrawn with the corrected
tier.  THIS PROBE rebuilds every previously-built frontier/deep cell
(the CCXCIX six 6191..7004 plus the CCCVII nine 7958..9535, deduped:
15 cells, plus ONE declared stretch cell near h 10500) with the
CCCVII metric-corrected machinery VERBATIM and reads:

 (a) THE CORRECTED CENSUS + THE NEW MAP: per cell d with its
     outward-rounded enclosure, tau_ideal_ub with its enclosure, the
     refined upper bound, the corrected type (rule below), the flip
     census (CCCVII A15 verbatim); the corrected hole field (holes
     as IDEAL WITNESSES instead of float signs); the corrected
     sub-ladder (rule below); the corrected termination read.
 (b) THE ROBUSTNESS FRONTIER: |d| as a function of h across
     h ~ 2012..9535 (the TIE cell is the shallow anchor), per-band
     outward |d| ceilings as the MEASURED instrument-precision
     statement (float legality signs at depth h are trusted only for
     |tau| above the band's |d| ceiling), plus a CONJECTURE-GRADE
     log-log drift fit with extrapolations (a fit, never a law).
 (c) THE CORRECTED COFINAL VERDICT (enum below) + the CCCVII case
     census recomputed under the frozen CCCVII rule (any B/D cell
     re-classified?).

THE HONEST ASYMMETRY (CCCVII verbatim, load-bearing for every rule
below): tau_ideal_ub is an UPPER bound for tau_ideal, so a NEGATIVE
ideal read is a WITNESS while a POSITIVE read is only "no witness
found" -- positivity of the ideal object is NEVER certified here.
Structurally the corrected map can therefore only REMOVE cells from
the legal ladder (witness veto), never ADD any: a raw-NEGA cell
whose ideal upper bound is positive loses its status as an ideal
witness (the hole is DOWNGRADED) but does NOT become a ladder rung.

THE CORRECTED TYPE RULE (frozen; exhaustive, disjoint; ub = the
witness read with outward enclosure [ub_lo, ub_hi], ref = the
refined minimum over O-metric Rayleigh iterates, ref <= ub by
construction, every iterate separately an upper bound, CCCVII A13):
  IDEAL-WITNESS-NEGA iff ref < -IDEAL_NOISE and ub_hi < -IDEAL_NOISE
     (the outward enclosure certifies the witness read negative --
     rigorous modulo the named residual scope edge A2);
  IDEAL-LEAN-NEGA    iff ref < -IDEAL_NOISE, not WITNESS (a float
     lean without enclosure -- typed, never consumed as a witness);
  NO-WITNESS-POS     iff ref > +IDEAL_NOISE (NO negative read exists
     at this witness; positivity NOT certified);
  IDEAL-UNRESOLVED   otherwise (|ref| <= IDEAL_NOISE; the enclosure
     width is printed as the honest resolution limit).

CORRECTED ELIGIBILITY + LADDER + COFINAL RULES (frozen BEFORE the
run).  CBINS = ((6100, 6320), (6320, 6600), (6600, 7300), (7300,
8300), (8300, 9500), (9500, 11000)).  A built cell is
corrected-ELIGIBLE iff its raw verdict is LEGAL (cell_legal OK and
|tau| > TAU_NOISE, CCXCIX verbatim) AND its corrected type is
NO-WITNESS-POS (any ideal-negative read or an unresolved read
vetoes).  The corrected sub-ladder is MAX-TAU_IDEAL_UB-PER-BIN over
eligible cells (the mission rule: rerun MAX-TAU-PER-BIN on the
corrected values, ranking by ref); the raw MAX-TAU pick is printed
alongside.  Over the built-nonempty bins:
 CORRECTED-LEGAL-CONTINUES(h*)  iff every built-nonempty bin has
   >= 1 eligible cell AND the deepest built cell is eligible.
 CORRECTED-GAPPED(h*, gaps)     iff the deepest built-nonempty bin
   has an eligible cell but >= 1 shallower built bin has none.
 CORRECTED-TERMINATES-METRIC-CLEAN(h_last) iff the deepest
   built-nonempty bin has NO eligible cell AND (the next-deepest
   built bin also has none, OR the deepest bin has >= 2 built
   cells), AND every built ineligible cell with h > h_last is
   IDEAL-WITNESS-NEGA (the termination is carried by outward
   witnesses, not by float signs).
 CORRECTED-TERMINATES-FLOAT(h_last) same but >= 1 beyond-cell is
   only LEAN / raw-negative (the termination read is NOT
   metric-clean; typed).
 CORRECTED-AMBIGUOUS            otherwise (the decider is NAMED:
   the missing sample is printed with its census key).
Exhaustive and disjoint; every statement is about BUILT cells of
THIS run, never all h.

THE RECLASSIFICATION RULE is the CCCVII frozen case rule VERBATIM
(strict precedence C > B > D on NEG cells, MARGINAL -> 0, named
defects charged only if DISCRIMINATING i.e. absent from every built
POS cell, metric defect iff NEG and ref > +IDEAL_NOISE, B iff a
built raw-POS cell exists within BFLANK_H in h, else D typed
REPLICATION-REQUIRED) with ONE disclosed restriction (A5): the
exact-rational K-membership tier is NOT re-run, so POS cells are
typed CASE 0 with the K coordinate cited from CCCVII (which
measured K-membership 9/9 aligned with raw wall-legality; CASE A
cannot fire here and did not fire there).  The recomputed letters
are compared cell-by-cell against the frozen CCCVII census
(0:4 / B:2 / C:1 / D:2 on the nine).

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seat is the DECLARED orthogonality-probe seed (OPROBE_SEED,
    inside the verbatim ideal tier) and the DECLARED scramble seed.
    AC scan: the chain-pass, CD and census readers see nodes,
    weights, entries, coefficients and frozen constants only.
 T  TAB2 = 1.6e7 arrays built and warded BITWISE against the
    deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  the deep census (deployed frame formula verbatim), h-sorted;
    gates: 587 cells, h max 65051, census CONTAINS every frozen
    priority key.
 TIE the dissect builder (CCCVII build_cell_dissect VERBATIM) must
    tie bat.build_rung_param EXACTLY (tau, negA, lamS ==) on the
    TIE cell (nearest h 2012); PASS-TIE: the AC-scanned accumulator
    ties ob.eval_chain there.
 CEN the priority census behind the self-calibrating guard (build
    item i iff elapsed + GUARD_FAC * c_hat * h^3 <= BUILD_CAP_S,
    c_hat = COST_C_ENV until >= 1 deep cell (h >= 5000) is built,
    then 1.05 * max over built deep cells of elapsed_cell / h^3;
    else UNBUILT-GUARD and the list CONTINUES -- cheaper later
    items may still fit).  The frozen order (mission priority:
    frontier band, then the termination band, then the shallow
    hole-field / sub-ladder band, then the stretch):
      F1 7958 kz 282 (the LEGAL->ideal-NEGA flip cell),
      F2 8003 kz 284 (the NEGA->ideal-POSITIVE-lean flip cell),
      F3 8204 kz 287 (the CCCV sub-ladder end),
      D1 8677 kz 299, D2 8629 kz 223 (the deepest raw-LEGAL cell,
         eligibility anchor), D3 9023 kz 506, D4 9535 kz 526,
      D5 9447 kz 196, D6 8642 kz 551 (MARGINAL),
      S1 6197 kz 337, S2 6247 kz 436, S3 6280 kz 340,
      S4 6191 kz 178, S5 6344 kz 241, S6 7004 kz 517,
      T1 the census cell nearest h 10500 (STRETCH, the ONLY not
         previously built item, A8: it is the single sample that
         would make the deepest bin decidable; expected
         UNBUILT-GUARD on the nominal machine, honest either way).
    Per cell: raw verdict LEGAL / NEGA / MARGINAL / CORE-SHORT /
    UNBUILT-GUARD, the corrected tier, the corrected type.
 G  gates: the nine CCCVII cells reproduce tau at the CCCVII
    printed values (rtol NEGA_RTOL) with the printed verdicts; d
    and the refined ideal read reproduce the CCCVII printed values
    (rtol REPRO_D on the eight cells with a printed d; the CCCVII
    print carries 5 significant digits, so agreement at rtol 1e-3
    IS digit-identity at printed precision -- the raw values are
    printed for the eye); the six CCXCIX cells reproduce the
    CCXCIX printed taus (rtol NEGA_RTOL) and verdicts; G-INERTIA
    the two independent inertia routes agree on every built cell;
    G-COVERAGE a guard refusal is a BUDGET fact, typed and carried
    into the verdict as GATE-COVERAGE, never charged as a
    reproduction failure (CCCVII A12 verbatim).
 AN anatomy wards: W7 rank identity (#unit >= max(0, n_neg - h)),
    W8 the E8 ward lamS >= tau on PD cells (consumed nowhere),
    W9 the node accounting M == n_pos + n_neg + n_dropped.
 WO the OUTWARD-ROUNDING DISCIPLINE ward on every built cell:
    d_lo <= d <= d_hi, ub_lo <= ub <= ub_hi, ref <= ub (the
    refinement only ever lowers the upper bound), all enclosure
    widths finite and printed.
 X  controls-must-fire: X1 the scramble world must leave legality;
    X2 the smooth (prime-free) world must leave legality; X2C the
    CORRECTED tier on the smooth world must ALSO stay negative
    (ref < X2C_BAR) -- the metric correction must NOT rescue the
    smooth world, i.e. the discrimination persists under the
    corrected instrument; XO the faithfulness reader must FIRE on a
    DOCTORED recurrence (one be entry scaled by 1 + XO_DOPE); XD
    the doctored metric must move the ideal read.
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION (no step formations of record, no
    fitted level -- census + corrected map only) and typed as such.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum): the CORRECTED COFINAL case, plus typed tags
CORRECTED-MAP(raw holes vs witness holes, flips),
LADDER(h*_raw, h*_corrected, picks), ROBUSTNESS(per-band |d|
ceilings, threshold statement), RECLASS(case census vs CCCVII),
IDEALITY(d census, enclosure widths), GATE-COVERAGE, MEMBERSHIP not
re-run (typed), CONTROLS, SCREENS-VACUOUS, AMENDMENTS.  Every enum
is a finite float64 statement with outward-rounded enclosures of
the decisive scalars, about BUILT cells of the deployed
construction; NEVER an all-h statement, NEVER an RH claim, NEVER a
counterexample claim.

FROZEN BARS.  NDIM = 8; TAB2 = 1.6e7; KZ2_MAX = 1200; CENSUS_N_REF
= 587; CENSUS_HMAX_REF = 65051; TAU_NOISE = 5e-12 (CCXCIX
inherited); NEGA_RTOL = 2e-3; REPRO_D = 1e-3 (digit-identity at the
CCCVII 5-digit print, see G); IDEAL_NOISE = 1e-12; CD_TIE = 1e-2;
CD_SEP = 1e-9; CD_BLOCK = 512; ORTHO_BAR = 1e-9; OPROBE_SEED = 7;
NREF = 2; BFLANK_H = 600; BAND_LO = 7300; CBINS above; COST_C_ENV =
4.6e-10 s (CCCVII envelope); GUARD_FAC = 1.05; BUILD_CAP_S = 3000
(A7); SCR_SEED = 1; X2_CHEAP = 3300; XCTRL_TGT = 1300; X2C_BAR =
-1.0; LOC_ITERS = 30; RQ_TIE = 1e-10; UNIT_TIE = 1e-9; TIE_TGT =
2012; T1_TGT = 10500; XD_DOPE = 1e-6; XO_DOPE = 1e-6.
Smoke: PRIO = (TIE cell h ~ 2012, the census cell nearest 2200),
gates SMOKE-SKIPPED (typed); X2/X2C depth 600; bins vacuous,
verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 NO new pre-freeze reconnaissance: every priority key, every
    reference value and the cost model are read from the PRINTED
    outputs of CCXCIX / CCCV / CCCVII (next.txt notes and probe
    docstrings); no throwaway script was run, no cell was built and
    no tau was read before the freeze.
 A2 the ideal tier is the CCCVII metric-corrected Galerkin object,
    reused VERBATIM (chain_pass_values / chain_pass_project /
    ideal_tier / cd_route / gamma_n outward bounds / ldl_inertia,
    including the A13 O-metric refinement).  The residual ideality
    question -- how accurately the evaluated chain columns
    represent polynomials -- is measured INDIRECTLY (diag(O)
    census, chain growth, CD entry route) and remains the named
    scope edge, not closed.  No interval enclosure of the full
    n x n matrix is attempted; the outward rounding is applied to
    the DECISIVE SCALARS.
 A3 MARGINAL cells (|tau| <= TAU_NOISE) get no raw sign claim and
    no case letter (CCXCIX A3 / CCCVII A3 verbatim); their
    corrected read is printed and typed like any other.
 A4 the corrected map is structurally ONE-SIDED (see THE HONEST
    ASYMMETRY): eligibility can only shrink the raw-legal set.  In
    particular any EXTENSION of the sub-ladder horizon beyond the
    CCCV h* = 8204 comes from the raw-LEGAL CCCVII cell 8629, not
    from the metric correction, and is reported as such.
 A5 the exact-rational certificate / K-membership tier is NOT
    re-run (CCCVII measured K-membership 9/9 aligned with raw
    wall-legality and zero CASE-A cells); POS cells are typed
    CASE 0 with the coordinate cited.  DISCLOSED restriction of
    the reclassification rule, not a silent pass.
 A6 the localization is a DIAGNOSTIC tier (CCXCIX A7 / CCCVII A6
    verbatim): deterministic start, LU inverse iteration on the
    assembled A, refusals typed.  EXCEPTION, control-only and
    disclosed: on the SMOOTH world the wall eigenvalue sits at the
    -1e2..-1e3 scale while inverse iteration converges to the
    eigenvalue nearest ZERO, so the X2C witness is the direct
    bottom eigenpair (scipy eigh subset); it enters no gate cell.
 A7 BUDGET: the cap 3000 s is chosen so the full frozen list fits
    at the CCCVII measured effective rate (~3.8e-10 s * h^3 per
    dissect build; 15 cells sum to ~2.9e3 s), per the CCCVII A16
    lesson that a budget must never decide between case letters or
    map cells.  Worst-case wall ~52 min exceeds the mission's ~40
    min by design and is disclosed here; the guard's
    continue-semantics puts refusals on the cheapest tail last.
 A8 T1 (~h 10500) is the ONLY item that was never built before.
    It is included because the corrected termination read is
    single-sample in the deepest bin without it (the CCXCIX
    depth-target 10500 was guard-refused there); it is LAST in the
    priority list, expected UNBUILT-GUARD on the nominal machine,
    and its absence is a BUDGET fact that leaves the verdict
    CORRECTED-AMBIGUOUS with the decider named.
 A9 no ladder rebuild, no scorecard row, no promotion: nothing
    measured here enters a certificate of record.

SMOKE DISCLOSURE (2026-08-13), pre-freeze, verbatim.
 SMOKE-1 (SPEC_SHA e96a24a6, 19/19 PASS, 12.1 s): every check
   green.  ONE design defect surfaced by INSPECTION of the output
   and was repaired pre-freeze: in smoke the SMOKE-A priority cell
   IS the TIE cell, so the robustness census listed h 2012 twice
   and the duplicated point distorted the smoke drift fit (slope
   -30.77 on a 3-row table with 2 identical rows); repaired by
   keying the robustness census on (h, kz) -- in the frozen run the
   priority list never contains the TIE cell, so no frozen number
   changes.  No bar, rule, control or enum was touched.  Measured:
   TIE ward EXACT (tau, negA, lamS all ==); PASS-TIE q dev
   1.68e-11 against max chain growth 1.0e+02, diag(O) dev 4.22e-15;
   both smoke cells LEGAL and NO-WITNESS-POS (h 2012 tau
   +3.302213e-09, d +2.724e-12 outward [+1.640e-12, +3.808e-12];
   h 2196 tau +1.075441e-08, d -1.844e-13 outward [-1.386e-12,
   +1.017e-12]) -- the CCCVII shallow ordering |d| << tau
   reproduced; inertia routes AGREE (0 2x2 blocks); W7/W8/W9/WO
   green; CD rel 5.1e-13 / 2.3e-13; X1 scramble tau -7.792e+89
   LEFT; X2 smooth h 606 tau -812.1 LEFT; X2C smooth CORRECTED
   ref -812.1 < -1.0 (eigh-bottom witness, rq_gap 1.1e-13: the
   metric correction does NOT rescue the smooth world); XO fires
   2.000e-06 > 1e-9 >= 1.377e-14; XD moves the ideal read by
   1.000e-06.  Case letters on the smoke cells: 0 (POS, below
   BAND_LO), reclass census vacuous by design.

NO RH claim.  NO counterexample claim.  No marker moves; no paper,
ledger, website, manifest or verification file is touched; the only
edit outside this file is the German CCCXVII line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII pipeline: EXT
tables, grid_density, folded_measure_full, lanczos_chain,
eval_chain, CORE_J, smooth_masses), sigma_stress_battery_probe
(CCLXIX bat.build_rung_param, the census builder of record),
sigma_edge_growth_probe (CCLXXIII cell_legal, reproduced verbatim),
legality_frontier_probe (CCXCIX frontier map, TAU_NOISE, the
MAX-TAU-PER-BIN rule), legality_horizon_probe (CCCV horizon cells),
cofinal_dissect_probe (CCCVII metric-corrected tier, reused
verbatim; reference values under reproduction),
v563_paper2_readouts (deployed generators: von_mangoldt_table,
arch_lags, atom_lags_at, NU_MAIN).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/metric_map_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/metric_map_probe.py
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
BFLANK_H = 600
BAND_LO = 7300
CBINS = ((6100, 6320), (6320, 6600), (6600, 7300), (7300, 8300),
         (8300, 9500), (9500, 11000))
COST_C_ENV = 4.6e-10
GUARD_FAC = 1.05
BUILD_CAP_S = 3000.0
SCR_SEED = 1
X2_CHEAP = 3300
XCTRL_TGT = 1300
X2C_BAR = -1.0
LOC_ITERS = 30
RQ_TIE = 1.0e-10
UNIT_TIE = 1.0e-9
TIE_TGT = 2012
T1_TGT = 10500
XD_DOPE = 1.0e-6
XO_DOPE = 1.0e-6
EPS64 = float(np.finfo(float).eps)

# the CCCVII frozen reads, reproduction targets:
# (h, kz, tau, verdict, d, tau_ub_ref)  -- None where CCCVII did not
# print the value (8204/8629 ideal read; 8642 marginal d).
CCCVII_REF = (
    (7958, 282, +5.904e-11, "LEGAL",    -9.9587e-11, -4.0560e-11),
    (8003, 284, -8.160e-11, "NEGA",     +2.5703e-10, +1.7541e-10),
    (8204, 287, +2.665e-10, "LEGAL",    +8.9426e-11, None),
    (8629, 223, +7.245e-10, "LEGAL",    +3.8689e-11, None),
    (8642, 551, -2.122e-12, "MARGINAL", None,        None),
    (8677, 299, -3.053e-10, "NEGA",     +4.3465e-12, -3.0093e-10),
    (9023, 506, -1.498e-10, "NEGA",     +8.7360e-11, -6.2463e-11),
    (9447, 196, -1.412e-10, "NEGA",     +5.3769e-11, -8.7460e-11),
    (9535, 526, -1.743e-10, "NEGA",     +4.2931e-11, -1.3139e-10))
# the CCXCIX frozen raw reads (printed in CCXCIX/CCCV): (h, kz, tau,
# verdict)
CCXCIX_REF = (
    (6191, 178, +3.454e-10, "LEGAL"),
    (6197, 337, -5.227e-11, "NEGA"),
    (6247, 436, -1.611e-10, "NEGA"),
    (6280, 340, +4.520e-11, "LEGAL"),
    (6344, 241, +2.539e-10, "LEGAL"),
    (7004, 517, +1.017e-10, "LEGAL"))
# the CCCVII case census (frozen reference for the RECLASS tier)
CCCVII_CASE = {(7958, 282): "0", (8003, 284): "C", (8204, 287): "0",
               (8629, 223): "0", (8642, 551): "0", (8677, 299): "B",
               (9023, 506): "B", (9447, 196): "D", (9535, 526): "D"}

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


def linfit(x, y):
    """OLS y = a + s x (CCLIII verbatim); returns s, 2SE, R^2, a."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan"), float(ym)
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * xm
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, 2.0 * se, r2, a


def ldl_inertia(dblk):
    """CCCVII A13 verbatim: exact block inertia of the Bunch-Kaufman
    LDL^T factor (2x2 determinant signs decided in exact rational
    arithmetic on the dyadic float64 entries)."""
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
            "verbatim), h-sorted")
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
    need = ([(hv, kv) for hv, kv, _t, _s, _d, _u in CCCVII_REF]
            + [(hv, kv) for hv, kv, _t, _s in CCXCIX_REF])
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX/CCCV/CCCVII: %d == %d cells, "
          "h max %d == %d, all %d frozen priority keys present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()),
             CENSUS_HMAX_REF, len(need), ok_keys),
          len(out) == CENSUS_N_REF
          and int(hs.max()) == CENSUS_HMAX_REF and ok_keys,
          kill="K3")
    return out


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
    """THE CORRECTED TYPE RULE (frozen; see docstring)."""
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
    """Corrected eligibility (frozen): raw LEGAL and NO-WITNESS-POS."""
    return (read["verdict"] == "LEGAL"
            and read["itype"] == "NO-WITNESS-POS")


# ================================ the priority census (the rebuild)
def build_prio(census):
    by_key = {(c["h"], c["kz"]): c for c in census}
    hs = np.asarray([c["h"] for c in census], float)
    tie_cell = census[int(np.argmin(np.abs(hs - TIE_TGT)))]
    if SMOKE:
        c22 = census[int(np.argmin(np.abs(hs - 2200)))]
        return tie_cell, [("SMOKE-A", tie_cell),
                          ("SMOKE-B", c22)]
    t1_cell = census[int(np.argmin(np.abs(hs - T1_TGT)))]
    prio = [("F1-7958L", by_key[(7958, 282)]),
            ("F2-8003N", by_key[(8003, 284)]),
            ("F3-8204L", by_key[(8204, 287)]),
            ("D1-8677N", by_key[(8677, 299)]),
            ("D2-8629L", by_key[(8629, 223)]),
            ("D3-9023N", by_key[(9023, 506)]),
            ("D4-9535N", by_key[(9535, 526)]),
            ("D5-9447N", by_key[(9447, 196)]),
            ("D6-8642M", by_key[(8642, 551)]),
            ("S1-6197N", by_key[(6197, 337)]),
            ("S2-6247N", by_key[(6247, 436)]),
            ("S3-6280L", by_key[(6280, 340)]),
            ("S4-6191L", by_key[(6191, 178)]),
            ("S5-6344L", by_key[(6344, 241)]),
            ("S6-7004L", by_key[(7004, 517)]),
            ("T1-STRETCH", t1_cell)]
    return tie_cell, prio


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
              "part %s"
              % (lc["rq"], lc["rq_gap"], lc["res"], lc.get("uf"),
                 ("%.3f" % lc["part"])
                 if math.isfinite(lc.get("part", float("nan")))
                 else "-"))
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


def census_build(census):
    section("CEN -- THE CORRECTED CENSUS (verbatim builds in the "
            "frozen priority order, self-calibrating guard %.2f * "
            "c_hat * h^3 <= %.0f s)" % (GUARD_FAC, BUILD_CAP_S))
    tie_cell, prio = build_prio(census)
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
    reads = []
    c_hat = COST_C_ENV
    deep_rate = []
    for tag, cell in prio:
        est = GUARD_FAC * c_hat * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-11s h %-6d kz %-4d UNBUILT-GUARD (est "
                  "%.0f s at c_hat %.2e, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est, c_hat,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            reads.append(dict(tag=tag, cell=cell, verdict="UNBUILT",
                              why="UNBUILT-GUARD", rung=None,
                              itype="UNBUILT"))
            continue
        tc = time.time()
        rung = build_cell_dissect(cell)
        dt = time.time() - tc
        if cell["h"] >= 5000:
            deep_rate.append(dt / float(cell["h"]) ** 3)
            c_hat = 1.05 * max(deep_rate)
        ok, why = cell_legal(rung)
        marginal = ("tau" in rung and abs(rung["tau"]) <= TAU_NOISE)
        verdict = ("MARGINAL" if marginal
                   else "LEGAL" if ok else why)
        itype = ideal_type(rung)
        reads.append(dict(tag=tag, cell=cell, verdict=verdict,
                          why=why, rung=rung, marginal=marginal,
                          itype=itype))
        print("    %-11s h %-6d kz %-4d alpha %.4f  %-9s tau %-12s "
              "negA %s  %-18s %.1f s"
              % (tag, cell["h"], cell["kz"], cell["alpha"], verdict,
                 ("%.4g" % rung["tau"]) if "tau" in rung else "-",
                 rung.get("negA", "-"), itype, dt), flush=True)
        print_cell(rung)
    n_built = sum(1 for r in reads if r["rung"] is not None)
    check("CEN1 the census built %d items (%d unbuilt-guard, "
          "honestly censused)" % (n_built, len(reads) - n_built),
          n_built >= (2 if SMOKE else 6), kill="K1")
    ok_t, why_t = cell_legal(r_dis)
    tie_entry = dict(tag="TIE", cell=tie_cell,
                     verdict="LEGAL" if ok_t else why_t, why=why_t,
                     rung=r_dis, marginal=False,
                     itype=ideal_type(r_dis))
    return reads, tie_entry


# =============================================== reproduction gates
def census_gates(reads):
    section("G -- reproduction gates against CCCVII (tau, d, "
            "refined ideal read) and CCXCIX (raw tau)")
    n7, n9 = 0, 0
    if SMOKE:
        check("G CCCVII/CCXCIX reproduction SMOKE-SKIPPED (typed; "
              "no frontier cell is built in smoke)", True)
    else:
        got = {(r["cell"]["h"], r["cell"]["kz"]): r for r in reads
               if r["rung"] is not None}
        miss7 = [(hv, kv) for hv, kv, _t, _s, _d, _u in CCCVII_REF
                 if (hv, kv) not in got]
        miss9 = [(hv, kv) for hv, kv, _t, _s in CCXCIX_REF
                 if (hv, kv) not in got]
        check("G-COVERAGE CCCVII %d/9 and CCXCIX %d/6 gate cells "
              "BUILT within the cap (%s) -- a guard refusal is a "
              "BUDGET fact, typed, never charged as a reproduction "
              "failure (A12/CCCVII)"
              % (9 - len(miss7), 6 - len(miss9),
                 "complete" if not (miss7 or miss9)
                 else "MISSING " + ",".join("h %d" % k[0]
                                            for k in miss7 + miss9)),
              True)
        n7 = 9 - len(miss7)
        n9 = 6 - len(miss9)
        for hv, kv, tref, vref, dref, uref in CCCVII_REF:
            r = got.get((hv, kv))
            if r is None:
                continue
            tau = r["rung"].get("tau", float("nan"))
            idl = r["rung"].get("ideal") or {}
            if vref == "MARGINAL":
                ok = r["verdict"] == "MARGINAL"
                check("G CCCVII repro h %d kz %d: verdict %s == "
                      "MARGINAL (tau %.4g vs printed %.4g, no value "
                      "gate at noise scale, A3)"
                      % (hv, kv, r["verdict"], tau, tref), ok,
                      kill="K3")
                continue
            ok_t = (math.isfinite(tau)
                    and abs(tau / tref - 1.0) <= NEGA_RTOL
                    and r["verdict"] == vref)
            ok_d = True
            det = "tau %.6e vs %.4g" % (tau, tref)
            if dref is not None:
                dv = idl.get("d", float("nan"))
                ok_d = (math.isfinite(dv)
                        and abs(dv / dref - 1.0) <= REPRO_D)
                det += ", d %.6e vs %.5g (rel %.1e)" % (
                    dv, dref, abs(dv / dref - 1.0)
                    if math.isfinite(dv) else float("nan"))
            ok_u = True
            if uref is not None:
                uv = idl.get("tau_ub_ref", float("nan"))
                ok_u = (math.isfinite(uv)
                        and abs(uv / uref - 1.0) <= REPRO_D)
                det += ", ideal %.6e vs %.5g (rel %.1e)" % (
                    uv, uref, abs(uv / uref - 1.0)
                    if math.isfinite(uv) else float("nan"))
            check("G CCCVII repro h %d kz %d [%s]: %s"
                  % (hv, kv, vref, det), ok_t and ok_d and ok_u,
                  kill="K3")
        for hv, kv, tref, vref in CCXCIX_REF:
            r = got.get((hv, kv))
            if r is None:
                continue
            tau = r["rung"].get("tau", float("nan"))
            ok = (math.isfinite(tau)
                  and abs(tau / tref - 1.0) <= NEGA_RTOL
                  and r["verdict"] == vref)
            check("G CCXCIX repro h %d kz %d [%s]: tau %.6e vs "
                  "printed %.4g (rtol %.0e), verdict %s"
                  % (hv, kv, vref, tau, tref, NEGA_RTOL,
                     r["verdict"]), ok, kill="K3")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"]]
    n_ag = sum(1 for r in built
               if r["rung"].get("inertia", {}).get("agree"))
    check("G-INERTIA the two independent inertia routes (eigvalsh "
          "vs exact LDL block sign count) agree on %d/%d built cells"
          % (n_ag, len(built)), n_ag == len(built), kill="K3")
    return n7, n9


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


# ======================================= (a) THE CORRECTED MAP
def corrected_map(reads):
    section("MAP -- THE CORRECTED CENSUS TABLE + THE REDRAWN HOLE "
            "FIELD + THE CORRECTED SUB-LADDER")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"]]
    built.sort(key=lambda r: r["cell"]["h"])
    print("    h      kz   alpha    raw       tau          "
          "d            [outward d]                  tau_ub_ref   "
          "[outward ub]                  type                flip "
          "elig")
    for r in built:
        idl = r["rung"].get("ideal") or {}
        tau = r["rung"]["tau"]
        ref = idl.get("tau_ub_ref", float("nan"))
        r["flip"] = bool(math.isfinite(ref)
                         and abs(tau) > TAU_NOISE
                         and (ref > IDEAL_NOISE) != (tau > 0.0))
        r["elig"] = eligible(r)
        print("    %-6d %-4d %.5f %-9s %+.4e %+.4e [%+.4e,%+.4e] "
              "%+.4e [%+.4e,%+.4e] %-19s %-4s %s"
              % (r["cell"]["h"], r["cell"]["kz"], r["cell"]["alpha"],
                 r["verdict"], tau,
                 idl.get("d", float("nan")),
                 idl.get("d_lo", float("nan")),
                 idl.get("d_hi", float("nan")), ref,
                 idl.get("tau_ub_lo", float("nan")),
                 idl.get("tau_ub_hi", float("nan")),
                 r["itype"], "FLIP" if r["flip"] else
                 ("marg" if r["verdict"] == "MARGINAL" else "keep"),
                 "YES" if r["elig"] else "no"))
    # ---- the redrawn hole field
    raw_holes = [r for r in built if r["rung"]["tau"] <= -TAU_NOISE]
    wit_holes = [r for r in built
                 if r["itype"] == "IDEAL-WITNESS-NEGA"]
    lean_only = [r for r in built if r["itype"] == "IDEAL-LEAN-NEGA"]
    removed = [r for r in raw_holes
               if r["itype"] in ("NO-WITNESS-POS",
                                 "IDEAL-UNRESOLVED")]
    added = [r for r in wit_holes if r["rung"]["tau"] > -TAU_NOISE]
    print("\n    THE HOLE FIELD REDRAWN (holes as IDEAL WITNESSES "
          "instead of float signs):")
    print("      raw holes (tau <= -TAU_NOISE):        %s"
          % [(r["cell"]["h"], r["cell"]["kz"]) for r in raw_holes])
    print("      corrected holes (outward witnesses):  %s"
          % [(r["cell"]["h"], r["cell"]["kz"]) for r in wit_holes])
    print("      lean-only negatives (no enclosure):   %s"
          % [(r["cell"]["h"], r["cell"]["kz"]) for r in lean_only])
    print("      holes DOWNGRADED by the correction:   %s"
          % [(r["cell"]["h"], r["cell"]["kz"], r["itype"])
             for r in removed])
    print("      holes ADDED by the correction:        %s"
          % [(r["cell"]["h"], r["cell"]["kz"]) for r in added])
    # ---- the corrected sub-ladder
    print("\n    THE SUB-LADDER (per frozen CBIN; corrected rule "
          "MAX-TAU_IDEAL_UB-PER-BIN over eligible cells; raw "
          "MAX-TAU pick printed alongside):")
    bins = []
    for lo, hi in CBINS:
        cells = [r for r in built if lo < r["cell"]["h"] <= hi]
        if not cells:
            continue
        el = [r for r in cells if r["elig"]]
        raw_leg = [r for r in cells if r["verdict"] == "LEGAL"]
        pick = max(el, key=lambda r: r["rung"]["ideal"]
                   ["tau_ub_ref"], default=None)
        pick_raw = max(raw_leg, key=lambda r: r["rung"]["tau"],
                       default=None)
        bins.append(dict(lo=lo, hi=hi, n=len(cells),
                         n_el=len(el), pick=pick))
        print("      bin (%6d, %6d]: %d built, %d raw-LEGAL, %d "
              "eligible%s%s"
              % (lo, hi, len(cells), len(raw_leg), len(el),
                 ("; corrected pick h %d kz %d ub_ref %+.4e"
                  % (pick["cell"]["h"], pick["cell"]["kz"],
                     pick["rung"]["ideal"]["tau_ub_ref"]))
                 if pick else "; NO eligible cell",
                 ("; raw pick h %d tau %+.4e"
                  % (pick_raw["cell"]["h"], pick_raw["rung"]["tau"]))
                 if pick_raw else ""))
    h_raw = max((r["cell"]["h"] for r in built
                 if r["verdict"] == "LEGAL"), default=None)
    h_cor = max((r["cell"]["h"] for r in built if r["elig"]),
                default=None)
    print("      raw sub-ladder horizon h*_raw = %s; corrected "
          "horizon h*_corr = %s (A4: any extension beyond the CCCV "
          "8204 comes from the raw-LEGAL 8629, not from the metric)"
          % (h_raw, h_cor))
    return built, bins, h_raw, h_cor


# ======================================= (b) THE ROBUSTNESS FRONTIER
def robustness(built, tie_entry):
    section("ROB -- THE ROBUSTNESS FRONTIER (|d| vs h, per-band "
            "ceilings, the instrument-precision statement)")
    keys = {(r["cell"]["h"], r["cell"]["kz"]) for r in built}
    rows = built + ([tie_entry]
                    if (tie_entry["cell"]["h"],
                        tie_entry["cell"]["kz"]) not in keys else [])
    rows = sorted(rows, key=lambda r: r["cell"]["h"])
    print("    h      |tau|      |d|        outward|d|  "
          "width(d)   width(ub)  flip")
    pts = []
    for r in rows:
        idl = r["rung"].get("ideal") or {}
        dv = idl.get("d", float("nan"))
        if not math.isfinite(dv):
            continue
        dout = max(abs(idl["d_lo"]), abs(idl["d_hi"]))
        pts.append((r["cell"]["h"], abs(dv), dout, r))
        print("    %-6d %.3e  %.3e  %.3e  %.2e   %.2e   %s"
              % (r["cell"]["h"], abs(r["rung"]["tau"]), abs(dv),
                 dout, idl["d_hi"] - idl["d_lo"],
                 idl["tau_ub_hi"] - idl["tau_ub_lo"],
                 "FLIP" if r.get("flip") else ""))
    # ---- per-band outward |d| ceilings (MEASURED)
    bands = ((0, 6600), (6600, 8300), (8300, 11000))
    print("\n    PER-BAND CEILINGS (MEASURED on built cells, never "
          "a law): float legality signs at depth h are trusted "
          "only for |tau| ABOVE the band's outward |d| ceiling --")
    for lo, hi in bands:
        sel = [p for p in pts if lo < p[0] <= hi]
        if not sel:
            continue
        ceil = max(p[2] for p in sel)
        print("      band (%5d, %5d]: %d cells, max outward |d| = "
              "%.3e" % (lo, hi, len(sel), ceil))
    flips = [p for p in pts if p[3].get("flip")]
    keeps = [p for p in pts
             if not p[3].get("flip")
             and p[3]["verdict"] != "MARGINAL"
             and abs(p[3]["rung"]["tau"]) > TAU_NOISE]
    if flips:
        print("      on the BUILT set the float64 sign FLIPPED for "
              "|tau| <= %.3e and survived for |tau| >= %.3e"
              % (max(abs(p[3]["rung"]["tau"]) for p in flips),
                 min(abs(p[3]["rung"]["tau"]) for p in keeps)
                 if keeps else float("nan")))
    # ---- the drift fit (CONJECTURE-GRADE)
    if len(pts) >= 3:
        s, e, r2, a = linfit([math.log10(p[0]) for p in pts],
                             [math.log10(max(p[1], 1e-300))
                              for p in pts])
        print("      drift fit log10|d| = %.4f %+.4f log10 h (2SE "
              "%.4f, R2 %.3f) [CONJECTURE-GRADE, a fit]"
              % (a, s, e, r2))
        for hx in (10500, 12500, 65051):
            print("        extrapolated |d| at h %d ~ %.3e "
                  "[CONJECTURE-GRADE]"
                  % (hx, 10.0 ** (a + s * math.log10(hx))))
        return s, a
    return None, None


# ======================================= (c) reclassification tier
def named_defects(r):
    """CCCVII frozen defect list (K-membership tier excluded, A5)."""
    rung = r["rung"]
    out = []
    at = rung["atoms"]
    if not at["complete_tab2"]:
        out.append("COMB-INCOMPLETE(X %.3e > TAB2)" % rung["X"])
    if not at["refl_unreached"]:
        out.append("A8-REFLECTION-REACHED(u_min %.3e < D %.3e)"
                   % (at["u_min"], at["d_grid"]))
    if rung["n_pos"] + rung["n_neg"] + rung["n_drop"] != rung["M"]:
        out.append("NODE-ACCOUNTING-SHORT")
    if rung["n_drop"] != 0:
        out.append("BOUNDARY-CELL-DROPPED(%d)" % rung["n_drop"])
    if rung["nsteps"] < rung["h"] + 1 or not (rung["be_min"] > 0.0):
        out.append("CHAIN-SHORT/NESTING-BROKEN")
    if rung["hull"]["breach"]:
        out.append("HULL-BREACH(%d nodes outside the positive arm)"
                   % rung["hull"]["n_out"])
    if not rung.get("inertia", {}).get("agree", False):
        out.append("INERTIA-SPLIT")
    cdr = rung.get("cd") or {}
    if "rel" in cdr and cdr["rel"] > CD_TIE:
        out.append("CD-ENTRY-ROUTE-SPLIT(rel %.3e)" % cdr["rel"])
    return out


def reclassify(built):
    section("CLS -- THE CCCVII CASE RULE RECOMPUTED (verbatim minus "
            "the K tier, A5) + THE RECLASSIFICATION CENSUS")
    pos = [r for r in built if r["rung"]["tau"] >= TAU_NOISE]
    pos_names = set()
    for p in pos:
        for d in named_defects(p):
            pos_names.add(d.split("(")[0])
    if pos_names:
        print("    STRUCTURAL FEATURES (present on built LEGAL "
              "cells, therefore NOT discriminating): %s"
              % ", ".join(sorted(pos_names)))
    for r in built:
        tau = r["rung"]["tau"]
        idl = r["rung"].get("ideal") or {}
        tub = idl.get("tau_ub_ref", float("nan"))
        defects = [d for d in named_defects(r)
                   if d.split("(")[0] not in pos_names]
        flank = [p for p in pos
                 if abs(p["cell"]["h"] - r["cell"]["h"]) <= BFLANK_H
                 and p is not r]
        if abs(tau) <= TAU_NOISE:
            r["case"] = "0"
            r["case_why"] = "MARGINAL(|tau| <= TAU_NOISE)"
        elif tau > 0.0:
            r["case"] = "0"
            r["case_why"] = ("POS; K tier not re-run (A5, CCCVII: "
                             "all POS cells IN-K)")
        elif defects:
            r["case"] = "C"
            r["case_why"] = ("DISCRIMINATING NAMED DEFECT: "
                             + "; ".join(defects))
        elif math.isfinite(tub) and tub > IDEAL_NOISE:
            r["case"] = "C"
            r["case_why"] = ("METRIC DEFECT: tau_impl %+.4e < 0 but "
                             "tau_ideal_ub %+.4e > 0 (d %+.4e)"
                             % (tau, tub,
                                idl.get("d", float("nan"))))
        elif flank:
            r["case"] = "B"
            r["case_why"] = ("same-depth POS windows: "
                             + ", ".join("h %d kz %d tau %+.3e"
                                         % (p["cell"]["h"],
                                            p["cell"]["kz"],
                                            p["rung"]["tau"])
                                         for p in flank)
                             + (" | D-witness status: ideal ub "
                                "%+.4e" % tub))
        else:
            r["case"] = "D"
            r["case_why"] = ("REPLICATION-REQUIRED (ideal witness "
                             "survives: tau_ideal_ub %+.4e, d "
                             "%+.4e)" % (tub,
                                         idl.get("d", float("nan"))))
    n_re = 0
    for r in built:
        key = (r["cell"]["h"], r["cell"]["kz"])
        ref = CCCVII_CASE.get(key)
        tag = ""
        if ref is not None:
            if r["case"] != ref:
                n_re += 1
                tag = "  ** RECLASSIFIED (CCCVII: %s)" % ref
            else:
                tag = "  (CCCVII: %s, unchanged)" % ref
        print("    h %-6d kz %-4d -> CASE %s: %s%s"
              % (r["cell"]["h"], r["cell"]["kz"], r["case"],
                 r["case_why"], tag))
    band = [r for r in built if r["cell"]["h"] > BAND_LO]
    letters = {}
    for r in band:
        letters[r["case"]] = letters.get(r["case"], 0) + 1
    print("    band (h > %d) case census: %s; reclassified vs "
          "CCCVII: %d cell(s)"
          % (BAND_LO, ", ".join("%s:%d" % (k, letters[k])
                                for k in sorted(letters)), n_re))
    return letters, n_re


# ======================================= the corrected cofinal enum
def corrected_verdict(built, bins, census):
    if SMOKE:
        return "CORRECTED-SMOKE(no frontier cell built by design)"
    band = [r for r in built if r["cell"]["h"] > CBINS[0][0]]
    if not band or not bins:
        return "CORRECTED-AMBIGUOUS(no frontier cell built)"
    deepest = max(band, key=lambda r: r["cell"]["h"])
    deep_bin = bins[-1]
    gaps = [b for b in bins if b["n_el"] == 0]
    h_star = max((r["cell"]["h"] for r in band if r["elig"]),
                 default=None)
    if all(b["n_el"] >= 1 for b in bins) and deepest["elig"]:
        return ("CORRECTED-LEGAL-CONTINUES(h* = %d; every built bin "
                "has an eligible cell; rule "
                "MAX-TAU_IDEAL_UB-PER-BIN)" % h_star)
    if deep_bin["n_el"] >= 1 and gaps[:-1]:
        return ("CORRECTED-GAPPED(h* = %s; gap bins %s)"
                % (h_star, ["(%d,%d]" % (b["lo"], b["hi"])
                            for b in gaps]))
    if deep_bin["n_el"] == 0:
        second = bins[-2] if len(bins) >= 2 else None
        decidable = ((second is not None and second["n_el"] == 0)
                     or deep_bin["n"] >= 2)
        if decidable:
            beyond = [r for r in band
                      if h_star is None or r["cell"]["h"] > h_star]
            beyond = [r for r in beyond if not r["elig"]]
            clean = all(r["itype"] == "IDEAL-WITNESS-NEGA"
                        for r in beyond)
            if clean:
                return ("CORRECTED-TERMINATES-METRIC-CLEAN(last "
                        "eligible h = %s; every built cell beyond "
                        "it carries an OUTWARD ideal witness)"
                        % h_star)
            return ("CORRECTED-TERMINATES-FLOAT(last eligible h = "
                    "%s; >= 1 beyond-cell is only lean/raw "
                    "negative, NOT metric-clean)" % h_star)
    hs = np.asarray([c["h"] for c in census], float)
    t1 = census[int(np.argmin(np.abs(hs - T1_TGT)))]
    return ("CORRECTED-AMBIGUOUS(deepest built h %d %s is a SINGLE "
            "sample in its bin; the decider is a second built cell "
            "in (%d, %d], e.g. the census cell h %d kz %d)"
            % (deepest["cell"]["h"],
               "eligible" if deepest["elig"] else deepest["itype"],
               deep_bin["lo"], deep_bin["hi"], t1["h"], t1["kz"]))


# ==================================================== controls
def controls(census, tie_entry):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth, X2C "
            "smooth CORRECTED, XO doctored recurrence, XD doctored "
            "metric)")
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
    cheap = census[int(np.argmin(np.abs(hs - (600 if SMOKE
                                              else X2_CHEAP))))]
    smo = build_cell_dissect(cheap, world="smooth",
                             bottom_witness=True)
    ok, why = cell_legal(smo)
    print("    SMOOTH world h %d kz %d: legal %s (%s) tau %s"
          % (cheap["h"], cheap["kz"], ok, why,
             ("%.4g" % smo["tau"]) if "tau" in smo else "-"))
    check("X2 the SMOOTH (prime-free) world fires: legality LEFT "
          "at the tested depth h %d" % cheap["h"],
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
          "world: tau_ideal_ub refined %s < %.1f -- THE "
          "DISCRIMINATION persists under the corrected instrument"
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
  add any.  The residual ideality question (how accurately the
  evaluated chain columns represent polynomials) is measured
  indirectly (diag(O) census, chain growth, CD entry route) and
  remains the named scope edge.  The K-membership tier is not
  re-run (A5, cited from CCCVII).  Every statement is about BUILT
  cells of the frozen priority list, never all h; every fit is
  CONJECTURE-GRADE.  No marker moves, no promotion, NO RH claim,
  NO counterexample claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("metric_map_probe -- PRIME.COFINAL.METRIC.MAP.01")
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
    census = deep_census()
    if KILLS:
        return finish([])

    reads, tie_entry = census_build(census)
    if KILLS:
        return finish([])
    n7, n9 = census_gates(reads)
    anatomy_wards(reads, tie_entry)
    if any(k in ("K1", "K2") for k in KILLS):
        return finish([])       # a broken pipeline/ward cannot be
        #                         mapped; a REPRODUCTION or CONTROL
        #                         kill still prints every
        #                         measurement (CCCVII A13)

    built, bins, h_raw, h_cor = corrected_map(reads)
    slope, _icpt = robustness(built, tie_entry)
    letters, n_re = reclassify(built)
    verdict = corrected_verdict(built, bins, census)
    controls(census, tie_entry)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations of record, "
          "no fitted level -- census + corrected map only, "
          "declared)", True)

    if SMOKE:
        labels = ["CORRECTED-SMOKE(no frontier cell built by "
                  "design)"]
        return finish(labels)
    labels = [verdict,
              "GATE-COVERAGE(CCCVII %d/9, CCXCIX %d/6)" % (n7, n9)]
    flips = [r for r in built if r.get("flip")]
    wit = [r for r in built if r["itype"] == "IDEAL-WITNESS-NEGA"]
    raw_holes = [r for r in built
                 if r["rung"]["tau"] <= -TAU_NOISE]
    labels.append("CORRECTED-MAP(%d raw holes -> %d witness holes; "
                  "%d/%d flips)"
                  % (len(raw_holes), len(wit), len(flips),
                     len(built)))
    labels.append("LADDER(h*_raw %s, h*_corr %s)" % (h_raw, h_cor))
    ds = [(r["rung"].get("ideal") or {}).get("d", float("nan"))
          for r in built]
    ds = [d for d in ds if math.isfinite(d)]
    if ds:
        labels.append("IDEALITY(|d| %.2e..%.2e%s)"
                      % (min(abs(d) for d in ds),
                         max(abs(d) for d in ds),
                         (", drift slope %+.2f [fit]" % slope)
                         if slope is not None else ""))
    labels.append("RECLASS(%s; %d reclassified vs CCCVII)"
                  % (", ".join("%s:%d" % (k, letters[k])
                               for k in sorted(letters)), n_re))
    labels.append("MEMBERSHIP-NOT-RERUN(A5, cited)")
    return finish(labels)


if __name__ == "__main__":
    main()
