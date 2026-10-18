#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verdicta_protocol_probe -- PRIME.COFINAL.VERDICTA.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim, NO all-h statement.  2026-08-13.)

THE VERDICT-A PROTOCOL.  CCCXXIII located the chain-route defect (the
float64 polynomial-evaluation resolution floor, growing monotonically
through the chain, invisible to the route's own O-metric diagnostics
because those are built from the SAME columns) and re-adjudicated the
entire deep NEGA field with the Weil-kernel-direct arbiter: all 9
former-NEGA cells are DIRECT-POSITIVE with exact block inertia
n_neg = 0.  The chain route is sign-reliable at the 1e-10 scale up to
h = 3948 and NOT from h = 5539 (measured resolution-ratio ladder
6.2e-06 -> 4.1e-04 -> 7.0e-03 | 7.2e-02 -> 1.6e-01 -> 3.54 -> 1.58
at h 878 / 2012 / 3948 | 5539 / 7233 / 9447 / 9535).  This probe
implements the lead's five-item protocol for the defective
instrument:

 (1) THE FAIL-LOUD GUARD.  A reusable function chain_sign_guard that
     REFUSES to return a chain-route sign with a LOUD TYPED ERROR
     (ChainSignRefusal) whenever (i) the measured resolution floor
     exceeds the calibrated fraction of the decisive scalar, or
     (ii) the read is deeper than the calibrated reliable domain and
     NO floor was measured.  The calibration is the CCCXXIII bracket:
     the deepest sign-reliable ratio is 7.0e-03 (h 3948) and the
     shallowest unreliable one is 7.2e-02 (h 5539); the frozen bar
     GUARD_BAR = 2.2450e-02 is the geometric midpoint of that open
     bracket (any bar inside it gives the same ward outcome -- the
     endpoints are MEASUREMENTS, the midpoint is a convention,
     declared).  WARD: on the seven CCCXXIII-measured cells the guard
     must refuse EXACTLY the four unreliable ones (5539, 7233, 9447,
     9535) and pass EXACTLY the three reliable ones (878, 2012,
     3948); in no-floor mode it must refuse all three CCCXXI decider
     readings (h > 3948) and pass a shallow read (h 878).

 (2) THE REGRESSION BATTERY.  The nine former-NEGA cells (6197, 6247,
     7958, 8003, 8642, 8677, 9023, 9447, 9535) plus the two positive
     controls (8204, 8629) as a FROZEN regression set: the arbiter
     (PATH-3 direct Weil-kernel assembly + exact Bunch-Kaufman block
     inertia, CCCXXIII verbatim) re-run per cell against the STORED
     expected results (n_neg = 0, the CCCXXIII lam_min and tau-scale
     enclosures, rtol ARB_RTOL).  The battery's wall runtime and the
     per-cell build sum are REPORTED so the lead can price routine
     re-runs.

 (3) THE BINDING SIGN DECIDER.  For every read deeper than the
     calibrated chain domain the sign of record is decided ONLY by
     the arbiter: exact-rational Bunch-Kaufman block inertia of the
     assembled Omega_weil plus the outward-rounded certified
     enclosures E1 (folded quadrature) and E3 (Weil-kernel
     contraction) at the extremal witness.  A NEGATIVE certified
     enclosure is a WITNESS; a POSITIVE one is only "no witness found
     on this instrument" -- positivity is NEVER certified.

 (4) THE RETROACTIVE CORRECTION.  Every verdict of record that
     consumed a deep chain sign is re-read under the clean instrument
     and typed in a RETRO-CORRECTION LEDGER printed in this log:
     ARTIFACT-RETRACTED (the load-bearing negative sign is
     contradicted by a certified positive enclosure with n_neg = 0),
     SUPERSEDED (the verdict's logic stands but its instrument or
     scope is replaced), or UNAFFECTED (it never consumed a deep
     1e-10-scale chain sign, or the clean instrument confirms it).
     The affected verdicts: CCXCIX (hole field, FRONTIER-AMBIGUOUS),
     CCCV (NEGA band, LEGHOR-TERMINATES-MEASURED(8204)), CCCVII (case
     census, REPLICATION-REQUIRED, deep ideal tier), CCCXVII (redrawn
     hole field, corrected sub-ladder, CORRECTED-AMBIGUOUS), CCCXXI
     (the 10513 witness, the 9557 lean, CORRECTED-CONTINUES).  The
     UNTOUCHED partition of CCCXXIII (CCXCIII, CCCIX, CCLXXXIX/CCCI,
     CCXCVII/CCCIII, every promoted verification module) is CITED,
     not re-measured.

 (5) THE BLIND-FROZEN DEEP LADDER.  A ladder of deep cells above
     h = 8200 chosen BEFORE any deep computation by a SOURCE-ONLY
     rule frozen here: the seven bins (8200, 9000], (9000, 9800],
     (9800, 10600], (10600, 11400], (11400, 12200], (12200, 13000],
     (13000, 13800], and per bin the admissible census cell with the
     MAXIMUM source gap g_kz = u_{kz+1} - u_kz (ties: smaller h, then
     smaller kz).  MAX-GAP is the frozen geometry proxy for expected
     eligibility (the widest source gap gives the coarsest lag
     spacing D = g_kz/(2 nu) of the deployed frame); NO sign data of
     any kind enters the choice, enforced by the AC scan on the
     picker.  The arbiter runs on the picks BLIND; the census is the
     first clean-instrument deep-positivity battery.  A pick that
     coincides with an already-built key of this run is REUSED and
     typed BLIND-COINCIDENT.

 PLUS THE THREE DECIDER CELLS.  CCCXXI built 9557 kz 242
 (IDEAL-LEAN-NEGA, raw +6.447e-11, ideal refined -1.391e-12 outward
 [-6.649e-12, +3.869e-12], an eligibility veto), 9585 kz 320
 (NO-WITNESS-POS, raw +2.620e-10, refined +2.298e-10 outward
 [+2.246e-10, +2.350e-10], the corrected-ladder rung h*_corr = 9585)
 and 10513 kz 341 (IDEAL-WITNESS-NEGA, raw -2.784e-10, refined
 -9.559e-11 outward [-1.022e-10, -8.902e-11]) -- ALL on the machinery
 whose sign is unreliable from h ~5539.  Protocol: the guard formally
 REFUSES each stored chain reading (fail-loud, printed), then the
 arbiter adjudicates.  Expected per the CCCXXIII pattern: the 10513
 witness and the 9557 lean do NOT survive the clean instrument --
 but this run MEASURES it and reports what it finds.

THE ARBITER (CCCXXIII PATH 3, verbatim).  A cell is (kz, alpha =
u_kz, M, D = 2 alpha / M, h = M/2); the deployed lag profile is
c_r = A(rD, D) + c^atom_r (core.arch_lags + the T115 tent load
core.atom_lags_at).  The ideal wall scalar is basis-free:
   tau_ideal = lam_min(Omega, O),  Omega = O - H the
   Toeplitz-plus-Hankel matrix of the lag profile alone,
   Omega[m,m'] = (G_{m+m'} + G_{|m-m'|})/2,
   G_r = c_r - (c_{r+1} + c_{|r-1|})/2,
no FFT, no folding, no quadrature, NO CHAIN, no arm split.  Its
bottom eigenvector is the extremal witness; the exact-sign
Bunch-Kaufman block inertia (2x2 determinant/trace signs in exact
rational arithmetic on the dyadic float64 entries) decides
definiteness; the decisive scalar Q[q] = int q^2 dmu_+ - int q^2
dmu_- is certified in three coordinates (E1 folded quadrature, E3
Weil-kernel contraction (1/2) sum_r phi_r c_r, E3t Toeplitz-Hankel
sum_r G_r b_r) with exactly-rounded fsum under OUTWARD rounding and
declared-and-warded FFT / coefficient-transform half-width models.

FROZEN PROTOCOL.
 S0 firewall AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); AC scan: the READER functions
    (e1_quad, e3_kernel, e3_th, e3_dense, node_values, cheb_coeffs,
    coef_dev, omega_weil_rows, certify_witness, fft_ward, eta_of,
    node_frame, blind_picks, chain_sign_guard) see nodes, weights,
    entries, coefficients, census geometry and frozen constants only
    -- no eigensolver, no inverse, no tau; blind_picks and
    chain_sign_guard in particular can never touch a sign.
 T  the atom table to TAB2 = 1.6e7, warded BITWISE against the
    deployed 4e6 EXT prefix and against core.von_mangoldt_table.
 D  the deep census (deployed frame formula verbatim); gates: 587
    cells, h max 65051, all frozen reference keys present (the
    eleven battery keys + the three decider keys).
 W  the guard ward (constants only, runs in full even in smoke):
    W1 floor mode refuses exactly {5539, 7233, 9447, 9535} and
    passes exactly {878, 2012, 3948} on the stored CCCXXIII ratios;
    W2 no-floor mode refuses all three CCCXXI decider readings and
    passes a shallow h 878 read.
 CAL a shallow TIE cell (h ~ 878): the arbiter with (a) the
    Weil-kernel identity Omega_weil == Omega_quad entrywise
    (IDENT_BAR), (b) exact inertia agreeing with lam_min in sign,
    (c) the certified evaluators E1 / E3 / E3t / E3d agreeing on the
    extremal witness within their joint half-widths.
 B  the regression battery (protocol item 2), cells ascending in h
    under the honest cost guard; per cell R-checks: n_neg = 0
    (exact), certified POSITIVE E1 and E3, tau-scale read inside
    ARB_RTOL of the stored CCCXXIII value, lam_min inside ARB_RTOL.
 G  the reproduction gate: the three shared cells 9447 / 9535 /
    9023 are KILL-grade (K5) -- CCCXXIII's arbiter values must
    reproduce before anything else is read.
 DC the three decider cells: guard refusal of the stored CCCXXI
    reading printed per cell, then the arbiter verdict
    DIRECT-POS(no witness found) / DIRECT-NEG(certified witness) /
    DIRECT-STRADDLE.
 X  controls-must-fire, one per declared cell class: X1 SCRAMBLE
    and X2 SMOOTH worlds at BATTERY depth (8003) and at DECIDER
    depth (10513) must destroy the arbiter's wall scalar (both
    certified reads < -1e-6); XW the certified enclosure must FIRE
    on a DOCTORED lag entry (DOPE = 1e-2 on one entry, shift > 10
    half-widths) at the battery-class cell; XI exact-inertia
    discipline: the block inertia agrees with the lam_min sign at
    EVERY built cell and no LDL is refused; XM every declared
    numerical half-width model must hold on a DISJOINT
    re-measurement at EVERY built cell (CCCXV A14 discipline).
 BL the blind ladder (protocol item 5): picks DECLARED before any
    deep build, then built under the cost guard; unbuilt picks are
    typed UNBUILT-GUARD, never silently dropped.
 L  the updated ladder: the corrected sub-ladder of record (CCCXXI:
    6191 -> 6344 -> 8204 -> 8629 -> 9585, frozen facts) extended by
    every built clean-instrument cell; the new honest horizon
    h*_clean = the deepest built DIRECT-POS cell with no DIRECT-NEG
    below it; what remains unmeasured is ENUMERATED.
 RL the retro-correction ledger (protocol item 4) printed as a
    table, each row typed from THIS RUN's measurements where
    adjudicated here, from the cited record elsewhere.
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION (no step formations of record, no
    fitted level -- a protocol run on an audited instrument) and
    are typed as such.

VERDICT (frozen enums).
 (1) GUARD-SEALED(ward census) iff W1 and W2 are exact;
     GUARD-BROKEN(list) otherwise (K2).
 (2) REGRESSION-GREEN(n/n; runtime) iff every battery cell
     reproduces its stored expected result; REGRESSION-RED(list)
     otherwise (the battery exists to catch exactly this; only the
     G subset is kill-grade).
 (3) DECIDERS-ADJUDICATED(per-cell verdicts) always, with
     LADDER-EXTENDS(h*_clean) iff every built cell above 8200 is
     DIRECT-POS, else LADDER-INTERRUPTED(first DIRECT-NEG).
 (4) RETRO-LEDGER(counts by type).
 (5) BLIND-DEEP-CENSUS(built/planned; POS/NEG/STRADDLE census),
     headlined DEEP-ALL-DIRECT-POSITIVE(n) iff all built blind
     cells read n_neg = 0 with certified positive enclosures.
KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 calibration -> CALIBRATION-BROKEN; K4 a required
control silent -> CONTROL-SILENT; K5 a reproduction gate ->
REPRO-BROKEN.

FROZEN BARS.  TAB2 = 1.6e7; EXT_DEPLOYED = 4e6; KZ2_MAX = 1200;
CENSUS_N_REF = 587; CENSUS_HMAX_REF = 65051; NU_MAIN = 4;
GUARD_PASS_MAX = 7.0e-03; GUARD_REFUSE_MIN = 7.2e-02;
GUARD_BAR = 2.2450e-02 (geometric midpoint, convention declared);
H_RELIABLE = 3948; ARB_RTOL = 5e-2 (the CCCXXIII bar verbatim: the
stored lam_min values are 1e-15-scale scalars printed to 4 digits
and the decisive part is the SIGN and n_neg = 0, not the digits);
SIGN_MARGIN = 1; FFT_PROBE = 256; FFT_WARD2 = 96; ETA_SAFE = 8;
COEF_PROBE = 24; COEF_SAFE = 8; SAMP_SEED = 11; SCR_SEED = 1;
DOPE = 1e-2; IDENT_BAR = 1e-11; CAL_TGT = 900; SMOKE_TGT = 1200;
BLIND_BINS = (8200, 9000, 9800, 10600, 11400, 12200, 13000, 13800);
X_BATTERY_KEY = (8003, 284); X_DECIDER_KEY = (10513, 341);
GUARD_FAC = 1.05; COST_ARB = 1.3e-10 s (CCCXV/CCCXXIII envelope);
BUILD_CAP_S = 2400.
Smoke: the guard ward in full, CAL, and ONE shallow census cell
(h ~ 1200) end to end with its controls; battery / deciders / blind
ladder SMOKE-SKIPPED (typed); verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 NO pre-freeze reconnaissance.  Every reference value (the
    CCCXXIII resolution-ratio ladder, lam_min / tau-scale / margin
    table and AFFECTED/UNTOUCHED partition; the CCCXXI decider
    readings and corrected ladder; the CCCXVII ladder rungs) is
    quoted from the PRINTED record (next.txt notes and probe
    docstrings) and never recomputed as a substitute for a gate.
 A2 This probe never builds a Lanczos chain.  The chain route
    enters ONLY through stored readings consumed by the guard; the
    guard's floor mode is therefore warded on STORED measurements,
    and fresh floor measurement stays where that instrument lives
    (chain_audit_probe).  The arbiter's advantage is named and
    limited exactly as in CCCXXIII A2: it never evaluates a chain,
    but its own h x h assembly is float64 and its positive reads
    remain "no witness found", never "positivity certified".
 A3 GUARD_BAR sits at the geometric midpoint of the measured open
    bracket (7.0e-03, 7.2e-02); any bar inside the bracket yields
    the identical ward outcome on the built record.  The bracket
    endpoints are measurements; the midpoint is a convention and is
    NOT a claim about the true crossing.
 A4 The blind rule (bins + MAX-GAP + tie order) is frozen in this
    docstring BEFORE any deep computation of this mission; the rule
    consumes census geometry only (h, kz, gap), enforced by the AC
    scan; no smoke build touches any blind-bin cell deeper than the
    shallow smoke cell.  Coincidence of a pick with an
    already-built key is possible and is REUSED, typed, never
    recomputed as if independent.
 A5 The retro-ledger types are statements about WHICH MEASUREMENT
    each verdict of record consumed and what the clean instrument
    reads there; the decision to re-type any certificate of record
    belongs to the lead (CCCXXIII A6 verbatim).  UNAFFECTED rows
    cite the CCCXXIII partition and are not re-measured here.
 A6 No ladder rebuild of the shallow bins: the rungs 6191 / 6344 /
    8204 / 8629 / 9585 enter as frozen facts of CCCXVII / CCCXXI;
    this run re-confirms 8204 / 8629 (battery controls) and 9585
    (decider) on the clean instrument but does not re-derive the
    per-bin maxima.  h*_clean statements are about BUILT cells
    only, never all h.
 A7 The battery gates lam_min at ARB_RTOL although eigenvalues at
    the 1e-14 scale of an h x h float64 matrix carry no general
    accuracy guarantee at that resolution; the gate is honest
    because the battery re-runs the BITWISE-identical assembly on
    the same deployed inputs, so the comparison is
    reproduction-of-a-computation, not accuracy-of-an-eigenvalue.
    The load-bearing reads remain n_neg and the certified
    enclosures.
 A8 The cost model COST_ARB is the CCCXV/CCCXXIII envelope and
    over-prices actual builds by ~2x on this machine; the guard
    therefore truncates conservatively.  Truncation is typed
    UNBUILT-GUARD and reported, never hidden.

NO RH claim.  NO counterexample claim.  No paper, ledger, website,
manifest or verification file is touched; verification/ is imported
READ-ONLY for the deployed conventions, and the only edit outside
this file is the German CCCXXIX line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): v563_paper2_readouts (deployed generators:
von_mangoldt_table, arch_lags, atom_lags_at, NU_MAIN),
onebadmode_moments_probe (build_ext_tables for the bitwise T-ward,
smooth_masses for the X2 world), chain_audit_probe (CCCXXIII: the
arbiter machinery reproduced verbatim; the calibration table and
the battery expectations, quoted as constants),
decider_cell_probe (CCCXXI: the three decider readings and the
corrected ladder, quoted as constants), metric_map_probe (CCCXVII:
ladder facts, quoted as constants).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/verdicta_protocol_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/verdicta_protocol_probe.py
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

import onebadmode_moments_probe as ob        # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
TAB2 = 16_000_000
EXT_DEPLOYED = 4_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
NU_MAIN = 4
GUARD_PASS_MAX = 7.0e-03
GUARD_REFUSE_MIN = 7.2e-02
GUARD_BAR = 2.2450e-02
H_RELIABLE = 3948
ARB_RTOL = 5.0e-2
SIGN_MARGIN = 1.0
FFT_PROBE = 256
FFT_WARD2 = 96
ETA_SAFE = 8.0
COEF_PROBE = 24
COEF_SAFE = 8.0
SAMP_SEED = 11
SCR_SEED = 1
DOPE = 1.0e-2
IDENT_BAR = 1.0e-11
CAL_TGT = 900
SMOKE_TGT = 1200
GUARD_FAC = 1.05
COST_ARB = 1.3e-10
BUILD_CAP_S = 2400.0
EPS64 = float(np.finfo(float).eps)
U_RND = 0.5 * EPS64

# THE CCCXXIII CALIBRATION TABLE (printed record, quoted): the
# safety-factor-free resolution ratio |dQ|/|Q| at the chain's own
# witness, and whether CCCXXIII read the cell sign-reliable.
GUARD_CAL = (
    (878, 6.2e-06, True),
    (2012, 4.1e-04, True),
    (3948, 7.0e-03, True),
    (5539, 7.2e-02, False),
    (7233, 1.6e-01, False),
    (9447, 3.54, False),
    (9535, 1.58, False),
)

# THE REGRESSION BATTERY (protocol item 2): key -> (h, kz,
# lam_min(Omega_weil), n_neg, tau-scale read, margin, role) -- the
# CCCXXIII printed record, quoted as frozen expectations.
BATTERY_REF = (
    ("6197", 6197, 337, +1.107e-14, 0, +9.894e-11, 60.4, "NEGA"),
    ("6247", 6247, 436, +3.145e-14, 0, +2.082e-10, 144.9, "NEGA"),
    ("7958", 7958, 282, +4.484e-15, 0, +8.688e-11, 55.1, "NEGA"),
    ("8003", 8003, 284, +1.349e-14, 0, +2.516e-10, 573.3, "NEGA"),
    ("8204", 8204, 287, +8.557e-15, 0, +1.687e-10, None, "CTRL+"),
    ("8629", 8629, 223, +8.238e-15, 0, +2.378e-10, None, "CTRL+"),
    ("8642", 8642, 551, +5.124e-15, 0, +5.637e-11, 20.4, "NEGA"),
    ("8677", 8677, 299, +7.369e-15, 0, +1.220e-10, 139.8, "NEGA"),
    ("9023", 9023, 506, +9.042e-15, 0, +8.036e-11, 237.8, "NEGA"),
    ("9447", 9447, 196, +6.609e-15, 0, +2.044e-10, 145.8, "NEGA"),
    ("9535", 9535, 526, +3.297e-15, 0, +4.367e-11, 48.4, "NEGA"),
)
G_GATE_KEYS = ("9447", "9535", "9023")

# the chain record at the battery cells (CCCVII/CCCXVII, quoted):
# key -> (raw tau, metric-corrected tau_ideal_ub)
CHAIN_RECORD = {
    "6197": (-5.227e-11, +8.186e-12), "6247": (-1.611e-10,
                                               -1.352e-10),
    "7958": (+5.904e-11, -4.0560e-11), "8003": (-8.160e-11,
                                                +1.7541e-10),
    "8204": (+2.665e-10, +3.559e-10), "8629": (+7.245e-10,
                                               +7.632e-10),
    "8642": (-2.122e-12, None), "8677": (-3.053e-10, -3.0093e-10),
    "9023": (-1.498e-10, -6.2463e-11), "9447": (-1.412e-10,
                                                -8.7460e-11),
    "9535": (-1.743e-10, -1.3139e-10),
}

# THE THREE DECIDER CELLS (CCCXXI printed record, quoted): key ->
# (h, kz, raw tau, ideal refined, outward enclosure, CCCXXI type)
DECIDER_REF = (
    ("9557", 9557, 242, +6.447e-11, -1.391e-12,
     (-6.649e-12, +3.869e-12), "IDEAL-LEAN-NEGA(eligibility veto)"),
    ("9585", 9585, 320, +2.620e-10, +2.298e-10,
     (+2.246e-10, +2.350e-10), "NO-WITNESS-POS(eligible rung)"),
    ("10513", 10513, 341, -2.784e-10, -9.559e-11,
     (-1.022e-10, -8.902e-11), "IDEAL-WITNESS-NEGA"),
)

# THE BLIND LADDER (protocol item 5): frozen bins and the frozen
# source-only rule MAX-GAP-PER-BIN (ties: smaller h, then smaller
# kz).  Declared here, BEFORE any deep computation.
BLIND_BINS = ((8200, 9000), (9000, 9800), (9800, 10600),
              (10600, 11400), (11400, 12200), (12200, 13000),
              (13000, 13800))

# the corrected sub-ladder of record (CCCXVII/CCCXXI frozen facts)
LADDER_RECORD = ((6191, 178), (6344, 241), (8204, 287), (8629, 223),
                 (9585, 320))

# the control cell classes (declared)
X_BATTERY_KEY = (8003, 284)
X_DECIDER_KEY = (10513, 341)

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals", "eigvalsh",
                 "inv", "pinv", "solve", "lu_factor", "lu_solve",
                 "ldl", "svd", "cond", "negA", "lam_arb", "verdict")
READER_FUNCS = ("e1_quad", "e3_kernel", "e3_th", "e3_dense",
                "node_values", "cheb_coeffs", "coef_dev",
                "omega_weil_rows", "certify_witness", "fft_ward",
                "eta_of", "node_frame", "blind_picks",
                "chain_sign_guard")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
try:
    with open(os.path.abspath(__file__), "rb") as _fh:
        CODE_SHA = hashlib.sha256(_fh.read()).hexdigest()
except OSError:
    CODE_SHA = "unavailable"


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


def gamma_n(nterms):
    """The rigorous forward error factor of a length-n float64
    recursive summation: gamma_n = n u / (1 - n u)."""
    prod = nterms * U_RND
    if prod >= 0.5:
        return float("inf")
    return prod / (1.0 - prod)


def fsum_dot(av, bv):
    """Exactly-rounded sum of a_i b_i plus a RIGOROUS outward
    half-width for the product roundings."""
    pr = np.asarray(av, float) * np.asarray(bv, float)
    val = math.fsum(pr.tolist())
    wid = U_RND * math.fsum(np.abs(pr).tolist())
    return val, wid


def ldl_inertia(dblk):
    """EXACT block inertia of a Bunch-Kaufman LDL^T factor (CCCVII
    A13 / CCCXV / CCCXXIII verbatim): a 1x1 pivot contributes its
    sign, a 2x2 block one negative eigenvalue iff det < 0 and two
    iff det > 0 with negative trace, the determinant sign decided in
    EXACT rational arithmetic on the dyadic float64 entries."""
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


def f4(val):
    if val is None:
        return "n/a"
    return "%+.4e" % val if math.isfinite(val) else "nan"


# ============================================ (1) THE FAIL-LOUD GUARD
class ChainSignRefusal(Exception):
    """THE LOUD TYPED ERROR of protocol item 1: the chain-route
    instrument refuses to state a sign.  Carries the measurement
    that triggered the refusal."""

    def __init__(self, mode, h, ratio, bar, detail):
        self.mode = mode
        self.h = h
        self.ratio = ratio
        self.bar = bar
        self.detail = detail
        super().__init__(
            "CHAIN-SIGN-REFUSED[%s] at h=%d: %s (ratio %s vs bar "
            "%.4e; calibrated bracket (%.1e, %.1e), reliable domain "
            "h <= %d)" % (mode, h,
                          detail,
                          ("%.3e" % ratio) if ratio is not None
                          else "n/a",
                          bar, GUARD_PASS_MAX, GUARD_REFUSE_MIN,
                          H_RELIABLE))


def chain_sign_guard(h, q_value, floor=None):
    """PROTOCOL ITEM 1, the reusable fail-loud guard.  Given a
    chain-route decisive scalar q_value at depth h and (optionally)
    the MEASURED resolution floor of its evaluation, return
    (sign, ratio, provenance) or raise ChainSignRefusal.  Floor
    mode: refuse when floor / |q_value| > GUARD_BAR (the calibrated
    CCCXXIII bracket).  No-floor mode: refuse when h > H_RELIABLE
    (a deep chain sign without a measured floor is exactly the
    defect class CCCXXIII exposed).  Census geometry and frozen
    constants only -- this function can never touch an eigensolver
    or an arbiter read."""
    if not (isinstance(h, int) and h > 0):
        raise ChainSignRefusal("MALFORMED-DEPTH", int(h or 0), None,
                               GUARD_BAR, "h must be a positive int")
    if q_value is None or not math.isfinite(float(q_value)):
        raise ChainSignRefusal("NONFINITE-SCALAR", h, None, GUARD_BAR,
                               "decisive scalar is not finite")
    qa = abs(float(q_value))
    if floor is None:
        if h > H_RELIABLE:
            raise ChainSignRefusal(
                "UNMEASURED-BEYOND-CALIBRATION", h, None, GUARD_BAR,
                "no measured resolution floor and the depth exceeds "
                "the calibrated reliable domain")
        return (("NEG" if float(q_value) < 0.0 else "POS"), None,
                "CALIBRATED-DOMAIN(no floor measured; h <= %d)"
                % H_RELIABLE)
    fl = float(floor)
    if not math.isfinite(fl) or fl < 0.0:
        raise ChainSignRefusal("MALFORMED-FLOOR", h, None, GUARD_BAR,
                               "resolution floor is not a finite "
                               "nonnegative number")
    if qa == 0.0:
        raise ChainSignRefusal("ZERO-SCALAR", h, float("inf"),
                               GUARD_BAR,
                               "decisive scalar is exactly zero")
    ratio = fl / qa
    if ratio > GUARD_BAR:
        raise ChainSignRefusal(
            "RESOLUTION-FLOOR-EXCEEDED", h, ratio, GUARD_BAR,
            "the float64 evaluation floor is %.3e of the decisive "
            "scalar" % ratio)
    return (("NEG" if float(q_value) < 0.0 else "POS"), ratio,
            "FLOOR-MEASURED(ratio %.3e <= bar %.4e)"
            % (ratio, GUARD_BAR))


def guard_ward():
    """W -- the calibration ward of the guard (constants only)."""
    section("W -- THE GUARD WARD (protocol item 1): the fail-loud "
            "instrument guard against the seven CCCXXIII-measured "
            "cells and the three CCCXXI decider readings")
    print("    GUARD_BAR %.4e = geometric midpoint of the measured "
          "bracket (%.1e reliable at h 3948, %.1e unreliable at h "
          "5539); reliable domain h <= %d"
          % (GUARD_BAR, GUARD_PASS_MAX, GUARD_REFUSE_MIN,
             H_RELIABLE))
    w1_bad = []
    for h, ratio, reliable in GUARD_CAL:
        try:
            sign, rr, prov = chain_sign_guard(h, 1.0, floor=ratio)
            got = "PASSED(%s, %s)" % (sign, prov)
            ok = reliable
        except ChainSignRefusal as exc:
            got = "REFUSED[%s]" % exc.mode
            ok = not reliable
        print("      h %-5d ratio %.3e expected %-7s -> %s"
              % (h, ratio, "PASS" if reliable else "REFUSE", got))
        if not ok:
            w1_bad.append(str(h))
    check("W1 floor mode refuses EXACTLY the four unreliable cells "
          "(5539, 7233, 9447, 9535) and passes EXACTLY the three "
          "reliable ones (878, 2012, 3948) (%s)"
          % (",".join(w1_bad) if w1_bad else "7/7 exact"),
          not w1_bad, kill="K2")
    w2_bad = []
    for key, h, kz, raw, ideal, _encl, ctype in DECIDER_REF:
        try:
            chain_sign_guard(h, ideal)
            got = "PASSED -- WRONG"
            ok = False
        except ChainSignRefusal as exc:
            got = "REFUSED[%s]" % exc.mode
            ok = exc.mode == "UNMEASURED-BEYOND-CALIBRATION"
        print("      CCCXXI %-6s h %-6d kz %-4d ideal %s (%s) -> %s"
              % (key, h, kz, f4(ideal), ctype, got))
        if not ok:
            w2_bad.append(key)
    try:
        sign, _rr, prov = chain_sign_guard(878, -1.0e-10)
        shallow_ok = sign == "NEG"
        print("      shallow no-floor read h 878 -> PASSED(%s, %s)"
              % (sign, prov))
    except ChainSignRefusal as exc:
        shallow_ok = False
        print("      shallow no-floor read h 878 -> REFUSED[%s] -- "
              "WRONG" % exc.mode)
    if not shallow_ok:
        w2_bad.append("878")
    check("W2 no-floor mode refuses ALL THREE CCCXXI decider "
          "readings (h > %d, no measured floor) and passes a "
          "shallow h 878 read (%s)"
          % (H_RELIABLE, ",".join(w2_bad) if w2_bad else "4/4 exact"),
          not w2_bad, kill="K2")
    return not (w1_bad or w2_bad)


# ================================================ the arbiter (PATH 3)
def node_frame(lag, M):
    """The M Chebyshev-Lobatto nodes, the SIGNED masses and the fold
    multiplicity.  Lag entries and frozen constants only."""
    L = 2 * M - 2
    ext = np.concatenate([lag, lag[-2:0:-1]])
    dv = np.fft.fft(ext).real[:M]
    th = math.pi * np.arange(M) / (M - 1)
    eps = np.full(M, 2.0)
    eps[0] = 1.0
    eps[M - 1] = 1.0
    wsig = eps * dv * 4.0 * np.sin(th / 2.0) ** 2 / (2.0 * L)
    return th, wsig, dv, L


def node_values(avec, M, L):
    """q(x_i) = sum_{m<h} a_m cos(m theta_i) at the M Lobatto nodes,
    by ONE length-L FFT.  Coefficients and frozen constants only."""
    pad = np.zeros(L)
    pad[:len(avec)] = avec
    return np.fft.fft(pad).real[:M]


def cheb_coeffs(avec, M, L):
    """The cosine coefficients b_r of q^2 and phi_r of
    4 sin^2(theta/2) q(cos theta)^2 by EXACT polynomial algebra on a
    4L grid (no aliasing).  Coefficients and frozen constants only."""
    nf = 4 * L
    pad = np.zeros(nf)
    pad[:len(avec)] = avec
    qv = np.fft.fft(pad).real
    thf = 2.0 * math.pi * np.arange(nf) / nf
    bh = np.fft.fft(qv * qv).real / nf
    ph = np.fft.fft(4.0 * np.sin(thf / 2.0) ** 2 * qv * qv).real / nf
    bb = np.concatenate([[bh[0]], 2.0 * bh[1:2 * (M // 2)]])
    pp = np.concatenate([[ph[0]], 2.0 * ph[1:M]])
    return bb, pp, qv, thf


def coef_dev(fnc, thf, idx, ref):
    """max_r |fft coefficient - exactly rounded coefficient| over the
    sampled orders.  Coefficients and frozen constants only."""
    nf = len(fnc)
    dev = 0.0
    for r in idx:
        exact = 2.0 * math.fsum((fnc * np.cos(r * thf)).tolist()) / nf
        dev = max(dev, abs(exact - ref[r]))
    return dev


def omega_weil_rows(G, h, out):
    """Omega[m,m'] = (G_{m+m'} + G_{|m-m'|}) / 2, assembled row by row
    from the lag-derived sequence G.  Lag entries only."""
    for m in range(h):
        row = out[m]
        np.add(G[m:m + h], 0.0, out=row)
        row[:m + 1] += G[m::-1]
        if m + 1 < h:
            row[m + 1:] += G[1:h - m]
        row *= 0.5
    return out


def e1_quad(qv, wsig, eta):
    """The rebuilt folded quadrature with OUTWARD rounding: returns
    (Q, halfwidth, D_plus, D_plus_lo).  Node values, signed masses
    and frozen constants only."""
    aq = np.abs(qv)
    lo = np.maximum(aq - eta, 0.0) ** 2
    hi = (aq + eta) ** 2
    pos = wsig > 0.0
    neg = wsig < 0.0
    wp = wsig[pos]
    wn = -wsig[neg]
    d_lo = math.fsum((wp * lo[pos]).tolist())
    d_hi = math.fsum((wp * hi[pos]).tolist())
    n_lo = math.fsum((wn * lo[neg]).tolist())
    n_hi = math.fsum((wn * hi[neg]).tolist())
    rnd = U_RND * (math.fsum(np.abs(wp * hi[pos]).tolist())
                   + math.fsum(np.abs(wn * hi[neg]).tolist()))
    q_lo = d_lo - n_hi - rnd
    q_hi = d_hi - n_lo + rnd
    return 0.5 * (q_lo + q_hi), 0.5 * (q_hi - q_lo), \
        0.5 * (d_lo + d_hi), d_lo - rnd


def e3_kernel(phi, phi_dev, lag_dep, c1n):
    """The assembled Weil-kernel Galerkin restriction contracted in
    its stable coordinate a^T Omega_weil a = (1/2) sum_r phi_r c_r.
    Kernel entries, coefficients and frozen constants only."""
    nr = min(len(phi), len(lag_dep))
    val, wid = fsum_dot(phi[:nr], lag_dep[:nr])
    return 0.5 * val, 0.5 * (wid + phi_dev * c1n)


def e3_th(bcoef, b_dev, gseq):
    """The Toeplitz-Hankel CONSISTENCY read: a^T Omega_weil a =
    sum_r G_r b_r.  Kernel entries and coefficients only."""
    nr = min(len(bcoef), len(gseq))
    val, wid = fsum_dot(gseq[:nr], bcoef[:nr])
    wid += b_dev * math.fsum(np.abs(gseq[:nr]).tolist())
    return val, wid


def e3_dense(avec, omega, blk=1024):
    """The same bilinear form on the ASSEMBLED h x h matrix with the
    rigorous (deliberately crude) gamma_n bound."""
    hdim = len(avec)
    absacc = 0.0
    parts = []
    aabs = np.abs(avec)
    for lo in range(0, hdim, blk):
        hi = min(hdim, lo + blk)
        parts.append(float(avec[lo:hi] @ (omega[lo:hi] @ avec)))
        absacc += float(aabs[lo:hi] @ (np.abs(omega[lo:hi]) @ aabs))
    return math.fsum(parts), gamma_n(hdim + 1) * absacc


def eta_of(avec, L):
    """The DECLARED FFT forward-error model half-width for the node
    values (8 log2(L) u ||a||_1)."""
    return 8.0 * math.log2(max(4, L)) * U_RND * float(
        math.fsum(np.abs(avec).tolist()))


def fft_ward(avec, qv, th, idx):
    """MEASURE the FFT node-value deviation against an exactly-rounded
    dense reference on the sampled nodes."""
    mi = np.arange(len(avec), dtype=float)
    worst = 0.0
    for k in idx:
        ref = math.fsum((avec * np.cos(mi * th[k])).tolist())
        worst = max(worst, abs(ref - float(qv[k])))
    return worst


def certify_witness(avec, dat, th, wsig, L, gseq, om3=None,
                    label="W"):
    """The certified enclosures of the wall scalar at ONE coefficient
    vector: the folded quadrature E1, the Weil-kernel contraction E3,
    the Toeplitz-Hankel coordinate E3t, the assembled-matrix read
    E3d, and the declared-and-warded numerical half-width models."""
    M, lag = dat["M"], dat["lag"]
    rng = np.random.default_rng(SAMP_SEED)
    eta_mod = eta_of(avec, L)
    qv = node_values(avec, M, L)
    nidx = sorted(set(int(x) for x in rng.choice(
        M, size=min(FFT_PROBE, M), replace=False)))
    wdev = fft_ward(avec, qv, th, nidx)
    eta = max(eta_mod, ETA_SAFE * wdev)
    n2 = sorted(set(int(x) for x in rng.choice(
        M, size=min(FFT_WARD2, M), replace=False)) - set(nidx))
    wdev2 = fft_ward(avec, qv, th, n2)
    bb, phi, qf, thf = cheb_coeffs(avec, M, L)
    ridx = sorted(set(int(x) for x in rng.choice(
        M, size=min(COEF_PROBE, M), replace=False)))
    sq = qf * qf
    pfn = 4.0 * np.sin(thf / 2.0) ** 2 * sq
    d_phi = coef_dev(pfn, thf, ridx, phi)
    d_bb = coef_dev(sq, thf, [r for r in ridx if r < len(bb)], bb)
    r2 = sorted(set(int(x) for x in rng.choice(
        M, size=min(COEF_PROBE, M), replace=False)) - set(ridx))
    w_phi = coef_dev(pfn, thf, r2, phi)
    w_bb = coef_dev(sq, thf, [r for r in r2 if r < len(bb)], bb)
    phi_dev = COEF_SAFE * d_phi
    b_dev = COEF_SAFE * d_bb
    c1n = math.fsum(np.abs(lag).tolist())
    q1, d1, dp, dp_lo = e1_quad(qv, wsig, eta)
    q3, d3 = e3_kernel(phi, phi_dev, lag, c1n)
    q3t, d3t = e3_th(bb, b_dev, gseq)
    out = dict(label=label, eta=eta, eta_mod=eta_mod, fft_dev=wdev,
               fft_dev2=wdev2, E1=(q1, d1), E3=(q3, d3),
               E3t=(q3t, d3t), phi_dev=phi_dev, b_dev=b_dev,
               w_phi=w_phi, w_bb=w_bb, dplus=dp, dplus_lo=dp_lo,
               a1n=float(math.fsum(np.abs(avec).tolist())))
    if om3 is not None:
        out["E3d"] = e3_dense(avec, om3)
    out["tau_ub"] = q1 / max(dp_lo, 1e-300)
    out["tau_lo"] = (q1 - d1) / max(dp_lo, 1e-300)
    out["tau_hi"] = (q1 + d1) / max(dp_lo, 1e-300)
    return out


def sign_of(val, hw):
    if val + SIGN_MARGIN * hw < 0.0:
        return "NEG"
    if val - SIGN_MARGIN * hw > 0.0:
        return "POS"
    return "STRADDLE"


def arb_verdict(row):
    """PROTOCOL ITEM 3, the binding sign decider: exact inertia plus
    the outward-rounded certified enclosures, nothing else."""
    cen = row["cen"]
    s1 = sign_of(cen["E1"][0], cen["E1"][1])
    s3 = sign_of(cen["E3"][0], cen["E3"][1])
    ine = row.get("inertia", {})
    nneg = ine.get("n_neg")
    if s1 == "NEG" and s3 == "NEG":
        return "DIRECT-NEG(certified witness at the extremal " \
            "coefficient vector; n_neg = %s)" % nneg
    if s1 == "POS" and s3 == "POS" and nneg == 0:
        return "DIRECT-POS(no witness found; positivity NOT " \
            "certified)"
    if s1 == "STRADDLE" or s3 == "STRADDLE":
        return "DIRECT-STRADDLE(E1 %s / E3 %s; n_neg %s)" \
            % (s1, s3, nneg)
    return "DIRECT-INCONSISTENT(E1 %s / E3 %s; n_neg %s)" \
        % (s1, s3, nneg)


# ===================================================== tables + census
DEEP = {}


def build_tables():
    section("T -- the atom table to TAB2 = %.3g, warded BITWISE "
            "against the deployed 4e6 EXT prefix and against "
            "core.von_mangoldt_table" % TAB2)
    ob.build_ext_tables()
    lam2 = core.von_mangoldt_table(TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    n_pref = len(ob.EXT["NN"])
    ok = (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
          and np.array_equal(u2[:n_pref], ob.EXT["U"])
          and np.array_equal(mu2[:n_pref], ob.EXT["MU"]))
    check("T1 the 1.6e7 arrays agree BITWISE with the deployed 4e6 "
          "EXT arrays (%d atoms of %d)" % (n_pref, len(nn2)), ok,
          kill="K2")
    check("T2 the deployed frame constant NU_MAIN == %d" % NU_MAIN,
          int(core.NU_MAIN) == NU_MAIN, kill="K1")
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = np.diff(u2)


def deep_census():
    section("D -- the deep-frame census (deployed formula verbatim)")
    u2, g2 = DEEP["U"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=mz // 2, kz=kz, alpha=alpha, M=mz,
                            X=x_val, gap=float(g2[kz])))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    keys = {(c["h"], c["kz"]) for c in out}
    need = [(r[1], r[2]) for r in BATTERY_REF] \
        + [(r[1], r[2]) for r in DECIDER_REF]
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces the deployed frame: %d == %d cells, "
          "h max %d == %d, all %d reference keys (battery + "
          "deciders) present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()), CENSUS_HMAX_REF,
             len(need), ok_keys),
          len(out) == CENSUS_N_REF and int(hs.max()) == CENSUS_HMAX_REF
          and ok_keys, kill="K1")
    return out


def window_data(cell, world=None, scr_seed=None, dope=False):
    """The shared window data of a cell: the deployed lag profile and
    the atom census (CCCXXIII verbatim)."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, M = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    D = 2.0 * alpha / M
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    lag = c_ar + c_at
    if dope:
        lag = lag.copy()
        lag[M // 3] *= (1.0 + DOPE)
    return dict(alpha=alpha, M=M, D=D, h=M // 2, uu=uu, mm=mm,
                lag=lag, n_atom=int(ka), X=cell["X"])


def arbiter_cell(tag, cell, dat=None, world=None, scr_seed=None,
                 dope=False, keep_omega=False):
    """PATH 3 (CCCXXIII verbatim): assemble Omega_weil DIRECTLY from
    the lag profile, take its bottom eigenvector as the extremal
    witness, decide definiteness by the EXACT block inertia of its
    LDL factor, and certify the decisive scalar."""
    t_c = time.time()
    if dat is None:
        dat = window_data(cell, world=world, scr_seed=scr_seed,
                          dope=dope)
    M, h, lag = dat["M"], dat["h"], dat["lag"]
    row = dict(tag=tag, cell=cell, world=world, dope=dope, dat=dat,
               kind="ARB")
    th, wsig, dv, L = node_frame(lag, M)
    row["n_pos"] = int(np.sum(wsig > 0.0))
    row["n_neg"] = int(np.sum(wsig < 0.0))
    aext = np.concatenate([lag, [lag[M - 2]]])
    rr = np.arange(2 * h)
    gseq = aext[rr] - 0.5 * (aext[rr + 1] + aext[np.abs(rr - 1)])
    om3 = np.empty((h, h))
    omega_weil_rows(gseq, h, om3)
    w3v, w3 = sla.eigh(om3, subset_by_index=[0, 0])
    a3 = np.ascontiguousarray(w3[:, 0])
    a3 = a3 / float(np.linalg.norm(a3))
    row["lam_arb"] = float(w3v[0])
    try:
        _l, dblk, _p = sla.ldl(om3, lower=True)
        nneg, nzero, ntwo = ldl_inertia(dblk)
        row["inertia"] = dict(n_neg=nneg, n_zero=nzero, n_2x2=ntwo,
                              agree=bool((nneg > 0)
                                         == (float(w3v[0]) < 0.0)))
        del dblk, _l
    except Exception as exc:                          # noqa: BLE001
        row["inertia"] = dict(refused=type(exc).__name__, agree=False)
    row["cen"] = certify_witness(a3, dat, th, wsig, L, gseq, om3)
    if keep_omega:
        row["omega"] = om3
        row["frame"] = dict(th=th, wsig=wsig, L=L, gseq=gseq)
    else:
        del om3
    row["t_cell"] = time.time() - t_c
    row["verdict"] = arb_verdict(row)
    return row


def print_arb(row, chain_note=None):
    cen = row["cen"]
    ine = row.get("inertia", {})
    print("      %-6s h %-6d kz %-4d  lam_min(Omega_weil) %+.6e  "
          "n_neg %s (2x2 %s, zero %s)  |  Q %+.6e +-%.1e (margin "
          "%.2f)  E3 %+.6e +-%.1e  |  tau-scale %+.6e outward "
          "[%+.4e, %+.4e]  |  %s   %.1f s"
          % (row["tag"], row["cell"]["h"], row["cell"]["kz"],
             row["lam_arb"], ine.get("n_neg", "-"),
             ine.get("n_2x2", "-"), ine.get("n_zero", "-"),
             cen["E1"][0], cen["E1"][1],
             abs(cen["E1"][0]) / max(cen["E1"][1], 1e-300),
             cen["E3"][0], cen["E3"][1], cen["tau_ub"],
             cen["tau_lo"], cen["tau_hi"], row["verdict"],
             row["t_cell"]), flush=True)
    if chain_note:
        print("             %s" % chain_note)


def honest_est(h):
    return GUARD_FAC * COST_ARB * float(h) ** 3


def cost_guarded(tag, cell):
    est = honest_est(cell["h"])
    if time.time() - T0 + est > BUILD_CAP_S:
        print("      %-6s h %-6d kz %-4d UNBUILT-GUARD (est %.0f s, "
              "elapsed %.0f s, cap %.0f s)"
              % (tag, cell["h"], cell["kz"], est, time.time() - T0,
                 BUILD_CAP_S), flush=True)
        return False
    return True


# ========================================================== calibration
def calibration(census):
    section("CAL -- the shallow TIE cell: the Weil-kernel identity, "
            "exact-inertia agreement and the evaluator tie")
    hs = np.asarray([c["h"] for c in census], float)
    cell = census[int(np.argmin(np.abs(hs - CAL_TGT)))]
    print("    CAL cell: h %d kz %d alpha %.6f M %d"
          % (cell["h"], cell["kz"], cell["alpha"], cell["M"]),
          flush=True)
    dat = window_data(cell)
    arow = arbiter_cell("CAL", cell, dat=dat, keep_omega=True)
    th, wsig = arow["frame"]["th"], arow["frame"]["wsig"]
    h = dat["h"]
    mi = np.arange(h)
    cp = np.cos(np.outer(th[wsig > 0.0], mi))
    cn = np.cos(np.outer(th[wsig < 0.0], mi))
    oq = (cp.T * wsig[wsig > 0.0]) @ cp \
        - (cn.T * (-wsig[wsig < 0.0])) @ cn
    oq = 0.5 * (oq + oq.T)
    idd = float(np.max(np.abs(arow["omega"] - oq)))
    check("CAL1 the Weil-kernel identity: Omega_weil (lag profile "
          "only -- no fft, no fold, no quadrature) == Omega_quad "
          "(rebuilt signed measure) entrywise to %.3e <= %.0e "
          "(scale %.3e)" % (idd, IDENT_BAR, float(np.max(np.abs(oq)))),
          idd <= IDENT_BAR, kill="K2")
    del cp, cn, oq
    ine = arow.get("inertia", {})
    check("CAL2 exact block inertia agrees with lam_min in sign at "
          "the TIE cell (lam %+.6e, n_neg %s, agree %s)"
          % (arow["lam_arb"], ine.get("n_neg", "-"),
             ine.get("agree")), bool(ine.get("agree")), kill="K3")
    cen = arow["cen"]
    spread = abs(cen["E1"][0] - cen["E3"][0])
    check("CAL3 the certified evaluators agree on the extremal "
          "witness: E1 %+.8e +-%.1e, E3 %+.8e +-%.1e, E3t %+.8e "
          "+-%.1e, E3d %+.8e +-%.1e; spread %.3e"
          % (cen["E1"][0], cen["E1"][1], cen["E3"][0], cen["E3"][1],
             cen["E3t"][0], cen["E3t"][1], cen["E3d"][0],
             cen["E3d"][1], spread),
          spread <= cen["E1"][1] + cen["E3"][1]
          and abs(cen["E3t"][0] - cen["E3"][0]) <= cen["E3t"][1]
          + cen["E3"][1]
          and abs(cen["E3d"][0] - cen["E3"][0]) <= cen["E3d"][1]
          + cen["E3"][1], kill="K3")
    print_arb(arow)
    del arow["omega"]
    return arow


# ================================================ (2) the battery
def battery(census, by_key):
    section("B -- THE REGRESSION BATTERY (protocol item 2): the nine "
            "former-NEGA cells + the two positive controls, arbiter "
            "vs the STORED CCCXXIII expectations")
    t_b0 = time.time()
    rows = {}
    r_bad = []
    g_bad = []
    t_cells = 0.0
    for key, h, kz, lam_ref, nneg_ref, tau_ref, margin_ref, role \
            in BATTERY_REF:
        cell = by_key[(h, kz)]
        if not cost_guarded(key, cell):
            r_bad.append("%s UNBUILT" % key)
            if key in G_GATE_KEYS:
                g_bad.append("%s UNBUILT" % key)
            continue
        row = arbiter_cell(key, cell)
        rows[key] = row
        raw, ideal = CHAIN_RECORD[key]
        print_arb(row, chain_note="chain record: raw tau %s, "
                  "metric-corrected ideal %s (%s)"
                  % (f4(raw), f4(ideal), role))
        cen = row["cen"]
        ine = row.get("inertia", {})
        rel_tau = abs(cen["tau_ub"] - tau_ref) / max(abs(tau_ref),
                                                     1e-300)
        rel_lam = abs(row["lam_arb"] - lam_ref) / max(abs(lam_ref),
                                                      1e-300)
        margin = abs(cen["E1"][0]) / max(cen["E1"][1], 1e-300)
        ok = (ine.get("n_neg") == nneg_ref
              and row["verdict"].startswith("DIRECT-POS")
              and rel_tau <= ARB_RTOL and rel_lam <= ARB_RTOL)
        print("             R %-5s n_neg %s == %d | tau-scale rel "
              "%.3e | lam rel %.3e | margin %.1f (stored %s) -> %s"
              % (key, ine.get("n_neg"), nneg_ref, rel_tau, rel_lam,
                 margin,
                 ("%.1f" % margin_ref) if margin_ref else "n/a",
                 "GREEN" if ok else "RED"), flush=True)
        if not ok:
            r_bad.append(key)
            if key in G_GATE_KEYS:
                g_bad.append(key)
    t_battery = time.time() - t_b0
    t_cells = sum(r["t_cell"] for r in rows.values())
    print("    BATTERY RUNTIME: %.1f s wall for %d cells (cell-build "
          "sum %.1f s; excludes the one-off %.3g-atom table build) "
          "-- this is the routine re-run price."
          % (t_battery, len(rows), t_cells, TAB2))
    check("G  THE REPRODUCTION GATE: the three shared cells %s "
          "reproduce CCCXXIII's arbiter values (n_neg = 0, "
          "DIRECT-POS, tau-scale and lam_min inside rtol %.0e) (%s)"
          % ("/".join(G_GATE_KEYS), ARB_RTOL,
             ",".join(g_bad) if g_bad else "3/3 clean"),
          not g_bad, kill="K5")
    check("R  THE BATTERY: all %d cells reproduce their stored "
          "expected results (%s)"
          % (len(BATTERY_REF),
             ",".join(r_bad) if r_bad else "%d/%d GREEN"
             % (len(rows), len(BATTERY_REF))), not r_bad)
    return rows, r_bad, t_battery


# ================================================ (c) the deciders
def deciders(by_key):
    section("DC -- THE THREE DECIDER CELLS (CCCXXI 9557 / 9585 / "
            "10513): guard refusal of the stored chain reading, then "
            "the arbiter as the binding sign decider")
    rows = {}
    for key, h, kz, raw, ideal, encl, ctype in DECIDER_REF:
        print("\n  --- %s: h %d kz %d -- CCCXXI read: raw %s, ideal "
              "refined %s outward [%s, %s] -> %s"
              % (key, h, kz, f4(raw), f4(ideal), f4(encl[0]),
                 f4(encl[1]), ctype), flush=True)
        try:
            chain_sign_guard(h, ideal)
            print("      GUARD: PASSED -- UNEXPECTED (the ward would "
                  "have caught this)")
        except ChainSignRefusal as exc:
            print("      GUARD: %s" % exc)
        cell = by_key[(h, kz)]
        if not cost_guarded(key, cell):
            continue
        row = arbiter_cell(key, cell)
        rows[key] = row
        print_arb(row)
        survives = row["verdict"].startswith("DIRECT-NEG")
        if key == "10513":
            print("      -> does the 10513 WITNESS survive the clean "
                  "instrument?  %s"
                  % ("YES -- the witness is real on this instrument"
                     if survives else
                     "NO -- the CCCXXI witness does not survive; it "
                     "was a read of the defective chain machinery"))
        elif key == "9557":
            print("      -> does the 9557 LEAN survive the clean "
                  "instrument?  %s"
                  % ("YES" if survives or
                     row["verdict"].startswith("DIRECT-STRADDLE")
                     else "NO -- the eligibility veto had no basis "
                     "on the clean instrument"))
        else:
            print("      -> CCCXXI's eligible rung 9585: the clean "
                  "instrument %s its NO-WITNESS-POS reading"
                  % ("CONFIRMS" if
                     row["verdict"].startswith("DIRECT-POS")
                     else "does NOT confirm"))
    return rows


# ================================================ (5) the blind ladder
def blind_picks(census):
    """PROTOCOL ITEM 5, the frozen SOURCE-ONLY rule: per frozen bin
    the admissible census cell with MAXIMUM source gap g_kz (ties:
    smaller h, then smaller kz).  Census geometry (h, kz, gap) and
    frozen constants only -- this function can never touch a sign,
    a lag profile or an eigensolver (AC-scanned)."""
    picks = []
    for lo, hi in BLIND_BINS:
        cand = [c for c in census if lo < c["h"] <= hi]
        if not cand:
            picks.append(((lo, hi), None))
            continue
        best = max(cand, key=lambda c: (c["gap"], -c["h"], -c["kz"]))
        picks.append(((lo, hi), best))
    return picks


def blind_ladder(census, built_keys):
    section("BL -- THE BLIND-FROZEN DEEP LADDER (protocol item 5): "
            "bins and MAX-GAP rule frozen in the spec BEFORE any "
            "deep computation; the arbiter runs the picks BLIND")
    picks = blind_picks(census)
    print("    THE FROZEN PICKS (declared before building):")
    for (lo, hi), c in picks:
        if c is None:
            print("      bin (%d, %d]: EMPTY in the census" % (lo, hi))
        else:
            print("      bin (%d, %d]: h %d kz %d gap %.6f%s"
                  % (lo, hi, c["h"], c["kz"], c["gap"],
                     "  [BLIND-COINCIDENT with an already-built key]"
                     if (c["h"], c["kz"]) in built_keys else ""))
    rows = []
    for (lo, hi), c in picks:
        if c is None:
            continue
        key = (c["h"], c["kz"])
        if key in built_keys:
            row = built_keys[key]
            print("      REUSED %-6s h %-6d kz %-4d (built earlier "
                  "this run as %s): %s"
                  % ("BL", c["h"], c["kz"], row["tag"],
                     row["verdict"]), flush=True)
            rows.append(dict(row, blind_bin=(lo, hi),
                             coincident=True))
            continue
        tag = "BL%d" % c["h"]
        if not cost_guarded(tag, c):
            continue
        row = arbiter_cell(tag, c)
        row["blind_bin"] = (lo, hi)
        row["coincident"] = False
        rows.append(row)
        print_arb(row)
    n_pos = sum(1 for r in rows
                if r["verdict"].startswith("DIRECT-POS"))
    n_neg = sum(1 for r in rows
                if r["verdict"].startswith("DIRECT-NEG"))
    n_str = len(rows) - n_pos - n_neg
    print("\n    THE BLIND DEEP CENSUS: %d of %d planned picks "
          "built; DIRECT-POS %d, DIRECT-NEG %d, STRADDLE/other %d "
          "(the first clean-instrument deep-positivity battery; a "
          "positive read is 'no witness found', never 'positivity "
          "certified')" % (len(rows), len([p for p in picks
                                           if p[1] is not None]),
                           n_pos, n_neg, n_str))
    return rows, picks, (n_pos, n_neg, n_str)


# ============================================================= controls
def controls(base_rows, by_key, all_rows):
    section("X -- CONTROLS-MUST-FIRE, one per declared cell class "
            "(BATTERY depth %s, DECIDER depth %s)"
            % (X_BATTERY_KEY, X_DECIDER_KEY))
    class_cells = (("BATTERY", X_BATTERY_KEY),
                   ("DECIDER", X_DECIDER_KEY))
    for cls, keyt in class_cells:
        cell = by_key[keyt]
        for world, name in (("scramble", "X1"), ("smooth", "X2")):
            tag = "%s-%s" % (name, cls[:3])
            if not cost_guarded(tag, cell):
                check("%s %s world at %s depth UNBUILT-GUARD "
                      "(typed, not silently passed)" % (name, world,
                                                        cls),
                      False, kill="K4")
                continue
            r = arbiter_cell(tag, cell, world=world,
                             scr_seed=SCR_SEED)
            all_rows.append(r)
            cen = r["cen"]
            ine = r.get("inertia", {})
            fired = cen["E1"][0] < -1.0e-6 and cen["E3"][0] < -1.0e-6
            print("    %s %s world at h %d kz %d: lam_min %+.4e | "
                  "Q(E1) %+.4e Q(E3) %+.4e | exact inertia n_neg %s "
                  "of %d" % (name, world.upper(), cell["h"],
                             cell["kz"], r["lam_arb"], cen["E1"][0],
                             cen["E3"][0], ine.get("n_neg", "-"),
                             cell["h"]), flush=True)
            check("%s the %s world DESTROYS the arbiter's wall "
                  "scalar at %s depth (both certified reads < "
                  "-1e-6)" % (name, world.upper(), cls), fired,
                  kill="K4")
            del r
    base = base_rows.get("8003")
    if base is None:
        check("XW no battery base cell for the doped-lag control",
              False, kill="K4")
        return
    cell = by_key[X_BATTERY_KEY]
    if cost_guarded("XW", cell):
        r = arbiter_cell("XW", cell, dope=True)
        all_rows.append(r)
        shift = abs(r["cen"]["E1"][0] - base["cen"]["E1"][0])
        hw = base["cen"]["E1"][1]
        print("    XW DOPED lag entry c[M/3] scaled by 1 + %.0e: Q "
              "%+.6e vs %+.6e (shift %.3e, half-width %.3e, factor "
              "%.1f)" % (DOPE, r["cen"]["E1"][0],
                         base["cen"]["E1"][0], shift, hw,
                         shift / max(hw, 1e-300)), flush=True)
        check("XW the certified enclosure FIRES on a DOCTORED lag "
              "entry (shift %.3e > 10 x half-width %.3e)"
              % (shift, hw), shift > 10.0 * hw, kill="K4")
        del r
    else:
        check("XW doped-lag control UNBUILT-GUARD (typed)", False,
              kill="K4")


def inertia_and_model_wards(all_rows):
    bad_i = []
    bad_m = []
    n_base = 0
    for r in all_rows:
        ine = r.get("inertia", {})
        if "refused" in ine or not ine.get("agree", False):
            bad_i.append("%s(%s)" % (r["tag"],
                                     ine.get("refused", "disagree")))
        cen = r["cen"]
        n_base += 1
        if cen["fft_dev2"] > cen["eta"]:
            bad_m.append("%s node %.2e>%.2e" % (r["tag"],
                                                cen["fft_dev2"],
                                                cen["eta"]))
        if cen["w_phi"] > cen["phi_dev"]:
            bad_m.append("%s phi %.2e>%.2e" % (r["tag"], cen["w_phi"],
                                               cen["phi_dev"]))
        if cen["w_bb"] > cen["b_dev"]:
            bad_m.append("%s b %.2e>%.2e" % (r["tag"], cen["w_bb"],
                                             cen["b_dev"]))
    check("XI exact-inertia discipline: the block inertia agrees "
          "with the lam_min sign at EVERY built cell and no LDL is "
          "refused (%s)"
          % (";".join(bad_i) if bad_i else "%d cells clean" % n_base),
          not bad_i, kill="K2")
    check("XM every declared numerical half-width model holds on a "
          "DISJOINT re-measurement at EVERY built cell (%s)"
          % ("; ".join(bad_m) if bad_m else
             "%d cells x 3 models clean" % n_base),
          not bad_m, kill="K2")


# ================================= (4) the retro-correction ledger
def retro_ledger(bat_rows, dec_rows, h_clean):
    """PROTOCOL ITEM 4: every verdict of record that consumed the
    defective deep chain sign, re-read under the clean instrument
    and typed.  Types from THIS RUN's measurements where adjudicated
    here, from the cited CCCXXIII record elsewhere."""
    section("RL -- THE RETRO-CORRECTION LEDGER (protocol item 4)")

    def vd(key, rows):
        r = rows.get(key)
        return r["verdict"].split("(")[0] if r else "UNBUILT"

    def all_pos(keys, rows):
        return all(vd(k, rows) == "DIRECT-POS" for k in keys)

    rows = []
    rows.append((
        "CCXCIX", "hole field {6197, 6247} + FRONTIER-AMBIGUOUS",
        "deep chain tau at the 1e-10 scale",
        "6197 %s, 6247 %s (this run)" % (vd("6197", bat_rows),
                                         vd("6247", bat_rows)),
        "ARTIFACT-RETRACTED" if all_pos(("6197", "6247"), bat_rows)
        else "UNRESOLVED"))
    rows.append((
        "CCCV", "NEGA band {8677, 9023, 9535} + "
        "LEGHOR-TERMINATES-MEASURED(8204)",
        "deep chain tau at the 1e-10 scale",
        "8677 %s, 9023 %s, 9535 %s, 8204 %s (this run)"
        % (vd("8677", bat_rows), vd("9023", bat_rows),
           vd("9535", bat_rows), vd("8204", bat_rows)),
        "ARTIFACT-RETRACTED"
        if all_pos(("8677", "9023", "9535", "8204"), bat_rows)
        else "UNRESOLVED"))
    rows.append((
        "CCCVII", "case census (C/B/D typing of 8003/8677/9023/"
        "9447/9535) + REPLICATION-REQUIRED",
        "deep chain columns (the typing IS a chain read)",
        "all five DIRECT-POS in the battery; the required "
        "replication was delivered by CCCXV/CCCXXIII",
        "SUPERSEDED"
        if all_pos(("8003", "8677", "9023", "9447", "9535"),
                   bat_rows) else "UNRESOLVED"))
    rows.append((
        "CCCVII", "metric-corrected ideal tier as a DEEP sign "
        "decider",
        "chain-column evaluation beyond the calibrated domain",
        "the binding sign decider for h > %d is the arbiter; the "
        "guard refuses the chain there (this probe)" % H_RELIABLE,
        "SUPERSEDED"))
    rows.append((
        "CCCXVII", "redrawn hole field (6 witness holes) + "
        "robustness frontier",
        "deep chain reads at the 1e-10 scale",
        "every hole cell in the battery reads DIRECT-POS with "
        "n_neg = 0 (this run + CCCXXIII)",
        "ARTIFACT-RETRACTED"))
    rows.append((
        "CCCXVII", "CORRECTED-AMBIGUOUS verdict + corrected "
        "sub-ladder rungs {6191, 6344, 8204, 8629}",
        "the rungs are POSITIVE reads (chain-legal anchors)",
        "8204/8629 re-confirmed DIRECT-POS here; the rungs stand, "
        "the AMBIGUOUS verdict is replaced by the clean-instrument "
        "map", "SUPERSEDED"))
    d10513 = vd("10513", dec_rows)
    rows.append((
        "CCCXXI", "10513 IDEAL-WITNESS-NEGA",
        "the metric-corrected chain machinery (defect inherited, "
        "CCCXXIII A7)",
        "10513 %s (this run, arbiter)" % d10513,
        "ARTIFACT-RETRACTED" if d10513 == "DIRECT-POS"
        else ("CONFIRMED-WITNESS" if d10513 == "DIRECT-NEG"
              else "UNRESOLVED")))
    d9557 = vd("9557", dec_rows)
    rows.append((
        "CCCXXI", "9557 IDEAL-LEAN-NEGA (eligibility veto)",
        "same machinery; the lean sat INSIDE its own outward "
        "enclosure straddle",
        "9557 %s (this run, arbiter)" % d9557,
        "ARTIFACT-RETRACTED" if d9557 == "DIRECT-POS"
        else ("CONFIRMED-WITNESS" if d9557 == "DIRECT-NEG"
              else "UNRESOLVED")))
    d9585 = vd("9585", dec_rows)
    rows.append((
        "CCCXXI", "9585 NO-WITNESS-POS + CORRECTED-CONTINUES"
        "(h*_corr = 9585)",
        "positive chain read (direction unaffected by the defect "
        "class)",
        "9585 %s; the continuation direction is CONFIRMED and the "
        "horizon moves to h*_clean = %s (this run)"
        % (d9585, h_clean if h_clean else "n/a"),
        "UNAFFECTED" if d9585 == "DIRECT-POS" else "UNRESOLVED"))
    rows.append((
        "CCXCIII / CCCIX / CCLXXXIX / CCCI / CCXCVII / CCCIII / "
        "every promoted verification module",
        "the UNTOUCHED partition of CCCXXIII",
        "ENTRY data on the 8x8 step frame + certified rational "
        "floors; no deep 1e-10-scale chain sign",
        "cited from the CCCXXIII partition, not re-measured (A5)",
        "UNAFFECTED"))
    print("    %-12s %-52s %-24s" % ("VERDICT OF", "OBJECT",
                                     "TYPE"))
    for src, obj, consumed, replaced, typ in rows:
        print("    %-12s %-52s %-24s" % (src, obj[:52], typ))
        print("                 consumed: %s" % consumed)
        print("                 clean instrument: %s" % replaced)
    counts = {}
    for _s, _o, _c, _r, typ in rows:
        counts[typ] = counts.get(typ, 0) + 1
    print("\n    LEDGER CENSUS: %s"
          % ", ".join("%s x%d" % (t, n)
                      for t, n in sorted(counts.items())))
    return rows, counts


# ==================================== (c) the updated ladder + horizon
def updated_ladder(bat_rows, dec_rows, bl_rows):
    section("L -- THE UPDATED LADDER under the clean instrument")
    print("    the corrected sub-ladder of record (CCCXVII/CCCXXI "
          "frozen facts): %s"
          % " -> ".join("%d" % h for h, _kz in LADDER_RECORD))
    deep = []
    for r in list(bat_rows.values()) + list(dec_rows.values()) \
            + list(bl_rows):
        if r["cell"]["h"] > 8200 and not r.get("world") \
                and not r.get("dope"):
            deep.append(r)
    seen = set()
    uniq = []
    for r in sorted(deep, key=lambda x: (x["cell"]["h"],
                                         x["cell"]["kz"])):
        key = (r["cell"]["h"], r["cell"]["kz"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)
    print("    every built clean-instrument cell above h 8200 "
          "(battery + deciders + blind ladder):")
    first_nonpos = None
    first_nonpos_v = None
    h_clean = None
    for r in uniq:
        v = r["verdict"].split("(")[0]
        print("      h %-6d kz %-4d %s  (lam %+.3e, n_neg %s, "
              "tau-scale %+.3e)"
              % (r["cell"]["h"], r["cell"]["kz"], v, r["lam_arb"],
                 r.get("inertia", {}).get("n_neg", "-"),
                 r["cen"]["tau_ub"]))
        if v != "DIRECT-POS" and first_nonpos is None:
            first_nonpos = r["cell"]["h"]
            first_nonpos_v = v
        if v == "DIRECT-POS" and first_nonpos is None:
            h_clean = r["cell"]["h"]
    if first_nonpos is None and h_clean is not None:
        print("\n    THE NEW HONEST HORIZON: every built cell above "
              "8200 is DIRECT-POS -- the corrected sub-ladder "
              "extends through EVERYTHING BUILT, h*_clean = %d "
              "(deepest built clean-instrument cell with no "
              "certified witness and no straddle below it)."
              % h_clean)
    elif first_nonpos is not None:
        print("\n    LADDER STOPS ADVANCING at h %d (%s); h*_clean "
              "= %s below it."
              % (first_nonpos, first_nonpos_v,
                 h_clean if h_clean else "none"))
    print("    WHAT REMAINS UNMEASURED: everything not built -- the "
          "census holds %d admissible cells to h %d and this run "
          "has arbiter-adjudicated %d of them (plus the 13 of the "
          "CCCXXIII record, largely shared); within each blind bin "
          "only the single MAX-GAP pick is read; every bin above "
          "h %d is untouched; and a positive read is never a "
          "positivity certificate."
          % (CENSUS_N_REF, CENSUS_HMAX_REF,
             len(bat_rows) + len(dec_rows)
             + sum(1 for r in bl_rows if not r.get("coincident")),
             BLIND_BINS[-1][1]))
    return h_clean, first_nonpos, uniq


# ================================================================ main
def main():
    print("verdicta_protocol_probe -- PRIME.COFINAL.VERDICTA.01")
    print("SPEC_SHA %s  CODE_SHA %s%s"
          % (SPEC_SHA[:16], CODE_SHA[:16],
             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the readers (evaluators, transforms, guard, "
          "blind picker) see nodes, weights, entries, coefficients, "
          "census geometry and frozen constants only -- no "
          "eigensolver, no inverse, no tau, no verdict (%s)"
          % (",".join(sorted(set(bad_r))) or "clean"), not bad_r,
          kill="K1")
    check("S0.3 the calibrated bracket is well-formed: "
          "GUARD_PASS_MAX %.1e < GUARD_BAR %.4e < GUARD_REFUSE_MIN "
          "%.1e" % (GUARD_PASS_MAX, GUARD_BAR, GUARD_REFUSE_MIN),
          GUARD_PASS_MAX < GUARD_BAR < GUARD_REFUSE_MIN, kill="K1")

    guard_ward()
    if KILLS:
        return finish([])

    build_tables()
    if KILLS:
        return finish([])
    census = deep_census()
    if KILLS:
        return finish([])
    by_key = {(c["h"], c["kz"]): c for c in census}

    cal_row = calibration(census)
    if any(k in ("K1", "K2", "K3") for k in KILLS):
        return finish([])
    all_rows = [cal_row]

    if SMOKE:
        section("SMOKE -- one shallow census cell end to end; every "
                "frontier tier SMOKE-SKIPPED (typed)")
        hs = np.asarray([c["h"] for c in census], float)
        scell = census[int(np.argmin(np.abs(hs - SMOKE_TGT)))]
        srow = arbiter_cell("SMK", scell)
        all_rows.append(srow)
        print_arb(srow)
        for world, name in (("scramble", "XS1"), ("smooth", "XS2")):
            r = arbiter_cell(name, scell, world=world,
                             scr_seed=SCR_SEED)
            all_rows.append(r)
            fired = r["cen"]["E1"][0] < -1.0e-6 \
                and r["cen"]["E3"][0] < -1.0e-6
            check("%s the %s world destroys the wall scalar at the "
                  "smoke cell" % (name, world.upper()), fired,
                  kill="K4")
        rd = arbiter_cell("XSW", scell, dope=True)
        all_rows.append(rd)
        shift = abs(rd["cen"]["E1"][0] - srow["cen"]["E1"][0])
        check("XSW the doped-lag control fires at the smoke cell "
              "(shift %.3e > 10 x half-width %.3e)"
              % (shift, srow["cen"]["E1"][1]),
              shift > 10.0 * srow["cen"]["E1"][1], kill="K4")
        print("    battery / deciders / blind ladder / retro ledger "
              "SMOKE-SKIPPED (typed, not silently passed)")
        inertia_and_model_wards(all_rows)
        return finish(["VERDICTA-SMOKE(guard ward + CAL + one "
                       "shallow cell end to end; all frontier tiers "
                       "typed SMOKE-SKIPPED)"])

    bat_rows, r_bad, t_battery = battery(census, by_key)
    if KILLS:
        return finish([])
    all_rows.extend(bat_rows.values())

    dec_rows = deciders(by_key)
    all_rows.extend(dec_rows.values())

    controls(bat_rows, by_key, all_rows)

    built_keys = {}
    for r in list(bat_rows.values()) + list(dec_rows.values()):
        built_keys[(r["cell"]["h"], r["cell"]["kz"])] = r
    bl_rows, picks, bl_census = blind_ladder(census, built_keys)
    for r in bl_rows:
        if not r.get("coincident"):
            all_rows.append(r)

    inertia_and_model_wards(all_rows)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations of record, "
          "no fitted level -- a protocol run on an audited "
          "instrument, declared)", True)

    h_clean, first_nonpos, _deep = updated_ladder(bat_rows,
                                                  dec_rows,
                                                  bl_rows)
    ledger_rows, ledger_counts = retro_ledger(bat_rows, dec_rows,
                                              h_clean)

    # ---------------- the verdict tiers
    labels = []
    labels.append("GUARD-SEALED(7/7 floor-mode ward + 4/4 "
                  "no-floor-mode ward; bar %.4e in the measured "
                  "bracket)" % GUARD_BAR)
    if not r_bad:
        labels.append("REGRESSION-GREEN(%d/%d cells; battery wall "
                      "%.0f s)" % (len(bat_rows), len(BATTERY_REF),
                                   t_battery))
    else:
        labels.append("REGRESSION-RED(%s)" % ",".join(r_bad))
    dparts = []
    for key, h, _kz, _raw, _ideal, _encl, _ct in DECIDER_REF:
        r = dec_rows.get(key)
        dparts.append("%s %s" % (key, r["verdict"].split("(")[0]
                                 if r else "UNBUILT"))
    labels.append("DECIDERS-ADJUDICATED(%s)" % "; ".join(dparts))
    if first_nonpos is None and h_clean is not None:
        labels.append("LADDER-EXTENDS(h*_clean = %d on the built "
                      "set)" % h_clean)
    elif first_nonpos is not None:
        labels.append("LADDER-INTERRUPTED(first non-POS read at "
                      "h %d)" % first_nonpos)
    labels.append("RETRO-LEDGER(%s)"
                  % ", ".join("%s x%d" % (t, n)
                              for t, n in sorted(
                                  ledger_counts.items())))
    n_pos, n_neg, n_str = bl_census
    if bl_rows and n_neg == 0 and n_str == 0:
        labels.append("BLIND-DEEP-CENSUS(%d/%d built) + "
                      "DEEP-ALL-DIRECT-POSITIVE(%d)"
                      % (len(bl_rows), len([p for p in picks
                                            if p[1] is not None]),
                         n_pos))
    else:
        labels.append("BLIND-DEEP-CENSUS(%d built: POS %d / NEG %d "
                      "/ STRADDLE %d)" % (len(bl_rows), n_pos,
                                          n_neg, n_str))
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        vmap = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "CALIBRATION-BROKEN", "K4": "CONTROL-SILENT",
                "K5": "REPRO-BROKEN"}
        print("\n  VERDICT: %s" % vmap[KILLS[0]])
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements of ONE ideal object on
  the Weil-kernel-direct arbiter (CCCXXIII PATH 3 verbatim), with
  OUTWARD-ROUNDED enclosures of the decisive scalars and
  exact-rational Bunch-Kaufman block inertia on the computed LDL
  factor.  The h x h assembly itself is float64; a NEGATIVE
  certified enclosure is a WITNESS that the ideal form is
  indefinite; a POSITIVE one is only "no witness found" --
  positivity is NOT certified anywhere here.  The guard, the
  battery expectations, the decider readings and the ladder facts
  are the PRINTED record of CCCXXIII / CCCXXI / CCCXVII, quoted and
  then re-measured where this run builds.  Every statement is about
  BUILT cells of the frozen mission list, never all h.  No marker
  moves, no promotion, no re-typing of any certificate of record
  (the retro-ledger types are measurements plus citations; the
  decision belongs to the lead).  NO RH claim, NO counterexample
  claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; CODE_SHA %s; "
          "runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], CODE_SHA[:8],
             time.time() - T0, "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


if __name__ == "__main__":
    main()
