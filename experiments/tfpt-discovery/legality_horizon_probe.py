#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""legality_horizon_probe -- PRIME.ONEBADMODE.LEGALITY.HORIZON.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

PUSH THE LEGALITY HORIZON BEYOND h = 8003, AND READ THE SEAT.
CCXCIX (legality_frontier_probe) mapped the wall-legality frontier as
a hole field with collapsing margin: tau lives at the 1e-10 scale
with OSCILLATING sign (6191 +3.454e-10, 6197 -5.227e-11, 6247
-1.611e-10, 6280 +4.520e-11, 6344 +2.539e-10, 7004 +1.017e-10, 8003
-8.160e-11); a legal sub-ladder persists through every built bin to
h 7004 (rule MAX-TAU-PER-BIN); the deepest built cell h 8003 kz 284
is NEGA as a SINGLE SAMPLE in its bin -- cofinality OPEN at that
horizon; and the localized bad mode always sits on the SAME seat,
the lowest folded core node uf = 2 (participation 0.92-0.94,
rq_gap <= 7.5e-17).  THIS PROBE does two things:

 (a) THE NEXT HORIZON BAND.  Build the 8003 bin's flanking cells and
     the next bins up (frozen keys below): is h 8003 a HOLE in a
     still-legal bin, or the start of a WALL?  Does the legal
     sub-ladder (MAX-TAU-PER-BIN, CCXCIX rule verbatim) continue to
     a deeper horizon?
 (b) THE SEAT READ.  Since the seat is FIXED (uf = 2), isolate its
     contribution to tau per cell -- the cheap analytic read.
     STRUCTURE (stated before measurement, all linear identities of
     the deployed pipeline): the lag vector is lag = c_ar + c_at
     with c_ar = arch_lags(M, D) CLOSED-FORM and c_at the prime-comb
     tent assembly; grid_density is an FFT and hence LINEAR, so
     dens = dens_arch + dens_prime EXACTLY; at FIXED node membership
     (the kept negative-arm nodes of the FULL density) the folded
     weights split LINEARLY, vs = w_arch + w_prime (ob.folded_part,
     deployed).  Therefore the seat DIAGONAL of A = I - G obeys the
     EXACT identity
        A[j*,j*] = 1 - vs[j*] K[j*] = BASE - COIN,
        BASE = 1 - w_arch[j*] K[j*]  (arch baseline),
        COIN = w_prime[j*] K[j*]     (the prime coin),
     with K[j*] = sum_k p_k(y_j*)^2 the Christoffel read of the
     positive-arm chain at the seat.  At the LOCALIZED mode v the
     proportional weight attribution gives the EXACT mode split
        rq = BASE_m - COIN_m,  BASE_m = 1 - (1 - rq) a,
        COIN_m = (1 - rq)(1 - a),  a = sum_j v_j^2 w_arch_j / vs_j
     (a = the arch share of the mode's weight-attributed mass).
     THE FREQUENCY: circle node j reads the lag profile at angular
     frequency gamma = 2 pi j / (L D) per unit u; the folded seat
     uf = 2 therefore reads the comb weighted by cos(gamma u) with
     period L D / uf ~ 2 alpha -- the sign flip sits at u ~ alpha,
     i.e. the seat's currency is the balance of the comb below vs
     above sqrt(X).  PER-ATOM TIER: the tent assembly is linear over
     atoms and each atom occupies exactly two grid seats, so the
     seat's circle read dens_prime[uf] decomposes exactly into
     per-atom contributions (vectorized cosine read, WARDED against
     the verbatim FFT); the top atoms and the below/above-alpha
     balance are reported per cell.  ALL seat reads are a DIAGNOSTIC
     tier: legality verdicts consume ONLY the verbatim eigvalsh
     route (TIE ward below); nothing here enters a certificate.

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seat is the DECLARED scramble control seed.  AC scan: the
    per-atom / arch circle readers see entries and frozen constants
    only (no eigensolver, no inverse, no tau).
 T  TAB2 = 1.6e7 arrays built and warded BITWISE against the
    deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  the deep census (deployed frame formula verbatim), h-sorted;
    gates: 587 cells, h max 65051, census CONTAINS every frozen
    priority key below.
 TIE the seat builder (verbatim copy of bat.build_rung_param with
    extra READS of already-computed objects) must tie
    bat.build_rung_param EXACTLY (tau, negA, lamS ==) on the TIE
    cell (nearest h 2012); the seat wards SW1-SW6 are exercised
    there.
 CEN the priority census behind the guard (build item i iff
    elapsed + GUARD_FAC * COST_C * h^3 <= BUILD_CAP_S; else
    UNBUILT-GUARD, the list continues):
      G1 h 8003 kz 284 (the CCXCIX NEGA reproduction),
      G2 h 7004 kz 517 (the CCXCIX deepest-LEGAL reproduction),
      G3 h 6197 kz 337 (the CCLXXXVII/CCXCIX NEGA reproduction),
      N1 h 7958 kz 282 and N2 h 8204 kz 287 (the 8003 bin's
         flanking kz values -- hole or wall?),
      N3 h 9023 kz 506 (the cell the CCXCIX guard missed by 55 s)
         and N4 h 8677 kz 299 (second sample of the (8300, 9500]
         bin),
      XS the SMOOTH world at the N1 cell (the deep discrimination
         control, budgeted INSIDE the cap, before the stretch),
      N5 h 9535 kz 526 (stretch: opens the (9500, 11000] bin).
    Per cell: LEGAL / NEGA / MARGINAL (|tau| <= TAU_NOISE, sign not
    trusted) / CORE-SHORT / UNBUILT-GUARD, plus the localization
    and the full seat read.
 G  gates: G1/G3 the two NEGA cells reproduce (negA >= 1, tau at
    the CCXCIX printed value, rtol NEGA_RTOL); G2 the 7004 cell
    reproduces LEGAL with tau at the printed value; G4 the SEAT
    reproduces on the built NEGA repro cells: top localization seat
    uf == 2, participation >= PART_BAR, rq_gap <= RQ_TIE.
 AN the anatomy wards on every built cell: W7 rank identity
    (#unit >= max(0, n_neg - h), honest max(0,.) form), W8 the E8
    ward lamS >= tau on PD cells (consumed nowhere).
 SW the seat wards on every built cell: SW1 w_arch + w_prime == vs
    (max rel <= SPLIT_TIE); SW2 dens_arch + dens_prime == dens
    (<= DENS_TIE); SW3 BASE - COIN == A[j*,j*] (<= SEATID_TIE);
    SW4 the localization ties tau (rq_gap <= RQ_TIE REPORTED,
    LOCALIZATION-REFUSED typed, non-kill, CCXCIX A7 verbatim);
    SW5 the per-atom circle read ties the verbatim FFT at the seat
    node AND the arch cosine sum ties dens_arch there (rel <=
    ATOM_TIE); SW6 BASE_m - COIN_m == rq (<= MODE_TIE).
 X  controls-must-fire: X1 the scramble world (seed SCR_SEED) at
    the cheap control cell must leave legality; X2 the smooth
    (prime-free) world must leave legality at EVERY tested depth --
    the CCXCIX discrimination (smooth tau at the -1e3..-1e4 scale
    against +-1e-10 true) must PERSIST at the new-band cell XS;
    XA the doctored comb (the FIRST HALF of the atom masses
    reversed in place -- an asymmetric doctoring) must be REFUSED
    by the SW5 tie at the seat node (the per-atom reader is not
    insensitive to the comb).
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION here (no step formations, no fitted
    level -- census + anatomy only) and are typed as such; the
    gamma_eff and tau drift prints are MEASURED / CONJECTURE-GRADE
    fits, never screens.

HORIZON RULE (frozen BEFORE the run; CCXCIX cofinal rule verbatim on
the restricted bins).  HBINS = ((6100, 6320), (6600, 7300), (7300,
8300), (8300, 9500), (9500, 11000)).  A built cell is LEGAL only if
cell_legal says OK and |tau| > TAU_NOISE (MARGINAL censused
separately, counts NOT legal).  Over the built-nonempty bins:
 LEGHOR-CONTINUES-MEASURED(h*)  iff every built-nonempty bin has
   >= 1 legal cell AND the deepest built cell is legal.
 LEGHOR-GAPPED(h*, gaps)        iff the deepest built-nonempty bin
   has a legal cell but >= 1 shallower built bin has none.
 LEGHOR-TERMINATES-MEASURED(h_last_legal) iff the deepest
   built-nonempty bin has NO legal cell AND (the next-deepest built
   bin also has none, OR the deepest bin has >= 2 built cells).
 LEGHOR-AMBIGUOUS               otherwise.
Exhaustive and disjoint; every statement is about BUILT cells of
THIS run, never all-h.  The typed mission tag maps CONTINUES ->
LEGAL-CONTINUES, TERMINATES -> TERMINATION-SIGNAL, else MIXED.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum): the HORIZON RULE case, plus typed tags
LEGALITY-MAP(bin fractions, MAX-TAU picks), SEAT-ANATOMY(baseline
census, coin census, seat identity, gamma_eff drift),
MARGINAL(count), CONTROLS, SCREENS-VACUOUS, AMENDMENTS.  Every enum
is a finite float64 statement about BUILT cells of the deployed
construction plus explicitly CONJECTURE-GRADE fits; NEVER an all-h
statement, NEVER an RH claim.

FROZEN BARS.  NDIM = 8; TAB2 = 1.6e7; KZ2_MAX = 1200; CENSUS_N_REF
= 587; CENSUS_HMAX_REF = 65051; TAU_NOISE = 5e-12 (CCXCIX
calibration inherited); NEGA_RTOL = 2e-3; GATE_NEGA = ((8003, 284,
-8.160e-11), (6197, 337, -5.227e-11)); GATE_LEG = (7004, 517,
+1.017e-10); NEW_KEYS = ((7958, 282), (8204, 287), (9023, 506),
(8677, 299), (9535, 526)); HBINS above; COST_C = 4.2e-10 s (CCXCIX
frozen envelope kept; the re-measured law is ~3.9e-10, the envelope
stays conservative); GUARD_FAC = 1.15; BUILD_CAP_S = 2340 (runtime
ceiling ~40 min per the mission budget); SCR_SEED = 1; X2_CHEAP =
3300; XCTRL_TGT = 1300; LOC_ITERS = 30; RQ_TIE = 1e-10; PART_BAR =
0.85; UNIT_TIE = 1e-9; SPLIT_TIE = 1e-9; DENS_TIE = 1e-9;
SEATID_TIE = 1e-9 (relative to max(1, |BASE|, |COIN|)); ATOM_TIE =
1e-6; MODE_TIE = 1e-9; TIE_TGT = 2012; TOP_ATOMS = 5.
Smoke: PRIO = (TIE cell h ~2012, the census cell nearest 2200),
both with the full seat tier; gates G1-G4 SMOKE-SKIPPED (typed);
X2 depth (600,); XS skipped (typed); bins vacuous, verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 PRE-FREEZE RECONNAISSANCE, fully disclosed: ONE throwaway
    census-enumeration script (deleted; census keys and cost
    estimates only -- NO cell was built, NO tau was read).  It
    fixed the frozen priority keys (the 8003 bin's flanks 7958/8204
    at kz 282/287 with near-identical alpha ~7.39, the deep pair
    9023/8677, the stretch 9535) and the cap arithmetic: cumulative
    guard estimate over the full list 2371 s > 2340 = BUILD_CAP_S,
    so on a slow machine the N5 stretch is guard-refused honestly
    (~36 min run) while a fast machine builds it (~33 min); pure
    arithmetic on frozen constants, decided before any frontier
    read.
 A2 NO ladder rebuild, NO chain-profile, NO exact-rational tier:
    this probe is census + anatomy only; the certificate program
    stays with CCLXXVII/CCXCIX and nothing measured here enters a
    certificate.  The SR/W4/G4(rho) gates of CCXCIX are therefore
    out of scope (their machinery is not run), NOT silently passed.
 A3 MARGINAL cells (|tau| <= TAU_NOISE) count as NOT legal for the
    enum while censused separately (CCXCIX A3 verbatim): the sign
    of a 1e-12 eigenvalue of a float64 build is not evidence.
 A4 the certificate object is the ASSEMBLED float64 wall matrix
    (CCLXXVII A3 lineage): the float64-vs-ideal enclosure stays
    with the pg_chain program; MARGINAL is the honest
    acknowledgement of that scope edge at tau = 0.
 A5 the deep smooth discrimination runs at ONE new-band cell (XS at
    N1, ~200 s under the frozen cost law); the second X2 depth is
    the cheap 3300 repro of the known CCXCIX firing.  An exhaustive
    smooth sweep over all new cells (~1300 s) does not fit the
    budget and is NOT claimed.
 A6 the localization is a DIAGNOSTIC tier (CCXCIX A7 verbatim):
    deterministic start vector, LU inverse iteration on the
    assembled A, non-kill; refusals typed LOCALIZATION-REFUSED and
    printed.  The seat gate G4 consumes it ONLY on the reproduction
    cells, where CCXCIX already measured the seat.
 A7 the seat split wards SW1/SW2/SW3/SW5/SW6 are exact identities
    of the deployed pipeline (FFT linearity, folded_part at fixed
    membership, diagonal algebra); their failure is an
    implementation error and kills as WARD-BROKEN -- they make no
    claim about ideal objects.
 A8 the u < D tent reflection of atom_lags_at is UNREACHABLE for
    the true comb (first atom u = log 2 >> D ~ 1e-3); the per-atom
    reader asserts this instead of implementing the reflection, and
    the SW5 tie against the verbatim FFT would catch any violation.

SMOKE DISCLOSURE (2026-08-12), pre-freeze, verbatim.
 SMOKE-1 (SPEC_SHA 0308a3d6, 16/16 PASS, 10.9 s): NO repairs -- no
   bar, rule, control or enum was touched after the smoke.  TIE
   ward EXACT (tau, negA, lamS ==); seat wards at machine precision
   (SW1 2.7e-14, SW2 3.6e-16, SW3 2.2e-16, SW5 8.0e-16, SW6
   2.0e-17); localization rq_gap 1.9e-17, res 8.1e-18, ipr 1.6,
   seat uf = 2 part 0.875 on both smoke cells; XA fires massively
   (rel shift 4.64e-01 >> 1e-5); X1 scramble tau -7.8e+89, X2
   smooth tau -812.1 at h 606, both LEAVE legality.  DISCLOSED
   SMOKE OBSERVATIONS (they motivate no bar): at the shallow smoke
   cells the seat DIAGONAL A_jj ~ +3e-3 is six orders above tau
   ~ 3e-9 and the mode's diagonal and off-diagonal parts cancel
   (diag +3.77e-3, off -3.77e-3) -- the one-seat DIAGONAL is not
   the coin by itself there; the 3 x 3 core-seat block lam3
   +3.80e-9 lands within 15% of tau +3.30e-9; a_share ~ 0.0014
   (the mode's weight mass is ~99.9% prime).  Whether these shapes
   persist at the 1e-10 frontier is exactly the frozen question.

NO RH claim.  No marker moves; no paper, ledger, website, manifest
or verification file is touched; the only edit outside this file is
the German CCCV line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII pipeline: EXT
tables, grid_density, folded_measure_full, folded_part,
lanczos_chain, eval_chain, CORE_J), sigma_stress_battery_probe
(CCLXIX bat.build_rung_param, the census builder of record),
sigma_edge_growth_probe (CCLXXIII cell_legal, reproduced verbatim),
deep_membership_limit_probe (CCLXXXVII deep census machinery),
legality_frontier_probe (CCXCIX frontier map, gates, TAU_NOISE,
localization tier), v563_paper2_readouts (deployed generators:
von_mangoldt_table, arch_lags, atom_lags_at, NU_MAIN).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/legality_horizon_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/legality_horizon_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

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
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
TAU_NOISE = 5.0e-12
NEGA_RTOL = 2.0e-3
GATE_NEGA = ((8003, 284, -8.160e-11), (6197, 337, -5.227e-11))
GATE_LEG = (7004, 517, +1.017e-10)
NEW_KEYS = ((7958, 282), (8204, 287), (9023, 506), (8677, 299),
            (9535, 526))
HBINS = ((6100, 6320), (6600, 7300), (7300, 8300), (8300, 9500),
         (9500, 11000))
COST_C = 4.2e-10
GUARD_FAC = 1.15
BUILD_CAP_S = 2340.0
SCR_SEED = 1
X2_CHEAP = 3300
XCTRL_TGT = 1300
LOC_ITERS = 30
RQ_TIE = 1.0e-10
PART_BAR = 0.85
UNIT_TIE = 1.0e-9
SPLIT_TIE = 1.0e-9
DENS_TIE = 1.0e-9
SEATID_TIE = 1.0e-9
ATOM_TIE = 1.0e-6
XA_FIRE = 1.0e-5
MODE_TIE = 1.0e-9
TIE_TGT = 2012
TOP_ATOMS = 5

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals",
                 "eigvalsh", "inv", "pinv", "solve", "lu_factor",
                 "lu_solve", "negA", "lamS")
READER_FUNCS = ("circle_factors", "atom_circle_read",
                "arch_circle_read")

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


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


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
    need = ([(hv, kv) for hv, kv, _t in GATE_NEGA]
            + [(GATE_LEG[0], GATE_LEG[1])] + list(NEW_KEYS))
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX: %d == %d cells, h max %d == "
          "%d, all %d frozen priority keys present (%s)"
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


_CELL_CACHE = {}


def build_cell(cell, world=None, scr_seed=None):
    """The deployed deep-branch rung builder (bat.build_rung_param
    VERBATIM) with the CCLXXXVII world handling; cached by the full
    frame identity."""
    key = (int(cell["kz"]), int(cell["M"]), world, scr_seed)
    if key in _CELL_CACHE:
        return _CELL_CACHE[key]
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "arch":
        mm = np.zeros_like(mm)
    elif world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    rung = bat.build_rung_param(cell["kz"], alpha, mfold, uu, mm)
    rung["X"] = cell["X"]
    _CELL_CACHE[key] = rung
    return rung


# ================================ the per-atom / arch circle readers
def circle_factors(mfold, j_circle):
    """dens[j] = sum_i fac_i c[i] for the symmetric L = 2M-2
    extension: fac_0 = 1, fac_{M-1} = (-1)^j, fac_i = 2 cos(2 pi j i
    / L) otherwise.  Entries and frozen constants only."""
    lfold = 2 * mfold - 2
    ii = np.arange(mfold)
    fac = 2.0 * np.cos(2.0 * math.pi * j_circle * ii / lfold)
    fac[0] = 1.0
    fac[mfold - 1] = math.cos(math.pi * j_circle)
    return fac


def atom_circle_read(uu, mm, alpha, mfold, j_circle):
    """Per-atom contribution to dens_prime[j_circle]: each tent atom
    occupies exactly two grid seats (i0, i0+1) with weights (1-f, f)
    -- the u < D reflection is unreachable for the true comb (A8,
    asserted).  Entries and frozen constants only; vectorized."""
    d_grid = 2.0 * alpha / mfold
    assert float(np.min(uu)) >= d_grid
    pos = np.asarray(uu, float) / d_grid
    i0 = np.floor(pos).astype(int)
    frac = pos - i0
    fac = circle_factors(mfold, j_circle)
    in0 = (i0 >= 0) & (i0 < mfold)
    in1 = (i0 + 1 >= 0) & (i0 + 1 < mfold)
    f0 = np.where(in0, fac[np.clip(i0, 0, mfold - 1)], 0.0)
    f1 = np.where(in1, fac[np.clip(i0 + 1, 0, mfold - 1)], 0.0)
    mmv = np.asarray(mm, float)
    return -mmv * 0.5 * ((1.0 - frac) * f0 + frac * f1)


def arch_circle_read(c_ar, mfold, j_circle):
    """dens_arch[j_circle] as the explicit cosine sum over the
    CLOSED-FORM arch lag profile."""
    return float(np.asarray(c_ar, float)
                 @ circle_factors(mfold, j_circle))


# ============================== the seat builder (verbatim + reads)
def build_cell_seat(cell):
    """bat.build_rung_param VERBATIM (same sub-calls, same order,
    Schur part inline) plus EXTRA READS of already-computed objects:
    the bottom of spec(A), the unit count, the LU-inverse-iteration
    localization (A6), and the full SEAT READ (spec part (b)).
    Ties bat.build_rung_param EXACTLY (TIE ward)."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka]
    mm = mu2[:ka]
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _uf_p, _fdp = ob.folded_measure_full(dens, lfold, +1.0)
    ys, vs, uf_n, fdn = ob.folded_measure_full(dens, lfold, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1 or np.any(be <= 0):
        return dict(kind="param", kz=cell["kz"], h=half,
                    fail="CHAIN")
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = sym(gram)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    eva = np.linalg.eigvalsh(amat)
    out = dict(kind="param", kz=cell["kz"], h=half, n=n,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               tau=float(eva[0]), negA=int(np.sum(eva < 0.0)))
    out["X"] = cell["X"]
    # ---- anatomy extras (reads only; nothing above changed)
    out["eva_bot"] = [float(v) for v in eva[:4]]
    out["n_unit"] = int(np.sum(np.abs(eva - 1.0) <= UNIT_TIE))
    out["n_neg_nodes"] = int(n)
    out["rank_g"] = int(half)
    # ---- the weight split (SW1/SW2): exact linear identities
    dens_ar = ob.grid_density(c_ar)
    dens_at = ob.grid_density(c_at)
    out["sw2"] = float(np.max(np.abs(dens_ar + dens_at - dens))
                       / max(1.0, float(np.max(np.abs(dens)))))
    w_ar = ob.folded_part(dens_ar, fdn)
    w_at = ob.folded_part(dens_at, fdn)
    out["sw1"] = float(np.max(np.abs(w_ar + w_at - vs))
                       / max(1e-300, float(np.max(np.abs(vs)))))
    # ---- Christoffel read + diagonal of A at every negative node
    kk = np.einsum("jk,jk->j", pn, pn)
    adiag = 1.0 - vs * kk
    # ---- localization (LU inverse iteration, deterministic; A6)
    try:
        lu, piv = sla.lu_factor(amat)
        vloc = np.full(n, 1.0 / math.sqrt(n))
        for _ in range(LOC_ITERS):
            vloc = sla.lu_solve((lu, piv), vloc)
            vloc = vloc / float(np.linalg.norm(vloc))
        rq = float(vloc @ (amat @ vloc))
        res = float(np.linalg.norm(amat @ vloc - rq * vloc))
        p4 = float(np.sum(vloc ** 4))
        order = np.argsort(-np.abs(vloc))
        top3 = order[:3]
        j_star = int(top3[0])
        out["loc"] = dict(
            rq=rq, rq_gap=abs(rq - out["tau"]), res=res,
            ipr=1.0 / p4 if p4 > 0 else float("nan"),
            seats=[(int(uf_n[j]), float(ys[j]), float(abs(vloc[j])))
                   for j in top3])
        # ---- the seat read (exact diagonal split, SW3)
        base = 1.0 - float(w_ar[j_star]) * float(kk[j_star])
        coin = float(w_at[j_star]) * float(kk[j_star])
        out["seat"] = dict(
            uf=int(uf_n[j_star]), part=float(abs(vloc[j_star])),
            k_chr=float(kk[j_star]), w_arch=float(w_ar[j_star]),
            w_prime=float(w_at[j_star]),
            a_diag=float(adiag[j_star]), base=base, coin=coin,
            sw3=abs((base - coin) - adiag[j_star])
            / max(1.0, abs(base), abs(coin)))
        # ---- mode decomposition: diagonal vs off-diagonal carry
        diag_part = float(np.sum(vloc ** 2 * adiag))
        out["seat"]["diag"] = diag_part
        out["seat"]["off"] = rq - diag_part
        sub = amat[np.ix_(top3, top3)]
        out["seat"]["lam3"] = float(np.linalg.eigvalsh(sub)[0])
        # ---- exact mode split (SW6): rq = base_m - coin_m
        safe = vs > 1e-300
        a_share = float(np.sum((vloc[safe] ** 2) * w_ar[safe]
                               / vs[safe]))
        base_m = 1.0 - (1.0 - rq) * a_share
        coin_m = (1.0 - rq) * (1.0 - a_share)
        out["seat"]["a_share"] = a_share
        out["seat"]["base_m"] = base_m
        out["seat"]["coin_m"] = coin_m
        out["seat"]["sw6"] = abs((base_m - coin_m) - rq)
        # ---- the frequency read + per-atom tier (SW5)
        j_circ = int(uf_n[j_star])
        gam = 2.0 * math.pi * j_circ / (lfold * d_grid)
        out["seat"]["gamma"] = gam
        out["seat"]["period_over_alpha"] = (
            (lfold * d_grid / j_circ) / alpha if j_circ else
            float("inf"))
        contrib = atom_circle_read(uu, mm, alpha, mfold, j_circ)
        tot = float(np.sum(contrib))
        fft_pr = float(dens_at[j_circ])
        fft_ar = float(dens_ar[j_circ])
        ar_sum = arch_circle_read(c_ar, mfold, j_circ)
        out["seat"]["sw5"] = max(
            abs(tot - fft_pr) / max(1.0, abs(fft_pr)),
            abs(ar_sum - fft_ar) / max(1.0, abs(fft_ar)))
        out["seat"]["dens_pr"] = fft_pr
        out["seat"]["dens_ar"] = fft_ar
        below = uu < alpha
        out["seat"]["bal_below"] = float(np.sum(contrib[below]))
        out["seat"]["bal_above"] = float(np.sum(contrib[~below]))
        top_a = np.argsort(-np.abs(contrib))[:TOP_ATOMS]
        out["seat"]["atoms"] = [
            (int(round(math.exp(uu[i]))), float(contrib[i]))
            for i in top_a]
        del lu
    except Exception as exc:                       # noqa: BLE001
        out["loc"] = dict(refused=type(exc).__name__)
    del pn, gram
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


def seat_wards(rung, label):
    """SW1/SW2/SW3/SW5/SW6 census on one built cell (A7: exact
    pipeline identities, K2 on failure).  SW4 is reported."""
    ok = True
    det = []
    for key, bar in (("sw1", SPLIT_TIE), ("sw2", DENS_TIE)):
        val = rung.get(key, float("nan"))
        det.append("%s %.1e" % (key, val))
        ok = ok and math.isfinite(val) and val <= bar
    st = rung.get("seat")
    if st is not None:
        for key, bar in (("sw3", SEATID_TIE), ("sw5", ATOM_TIE),
                         ("sw6", MODE_TIE)):
            val = st.get(key, float("nan"))
            det.append("%s %.1e" % (key, val))
            ok = ok and math.isfinite(val) and val <= bar
    return ok, "; ".join(det)


def print_seat(rung):
    lc = rung.get("loc", {})
    if "refused" in lc:
        print("      loc: LOCALIZATION-REFUSED (%s)" % lc["refused"])
        return
    if "rq_gap" not in lc:
        return
    print("      loc: rq %.6e rq_gap %.2e res %.2e ipr %.1f seats %s"
          % (lc["rq"], lc["rq_gap"], lc["res"], lc["ipr"],
             [(s[0], "%.4f" % s[1], "%.3f" % s[2])
              for s in lc["seats"]]), flush=True)
    st = rung.get("seat")
    if st is None:
        return
    print("      seat uf=%d part %.3f: A_jj %+.4e = BASE %+.4e - "
          "COIN %+.4e (K %.4e, w_arch %.4e, w_prime %+.4e)"
          % (st["uf"], st["part"], st["a_diag"], st["base"],
             st["coin"], st["k_chr"], st["w_arch"], st["w_prime"]))
    print("      mode: diag %+.4e off %+.4e lam3 %+.4e | a_share "
          "%.8f BASE_m %+.4e COIN_m %+.4e"
          % (st["diag"], st["off"], st["lam3"], st["a_share"],
             st["base_m"], st["coin_m"]))
    print("      freq: gamma_eff %.4e (period/alpha %.3f) "
          "dens_pr %+.4e (below %+.4e above %+.4e) top atoms %s"
          % (st["gamma"], st["period_over_alpha"], st["dens_pr"],
             st["bal_below"], st["bal_above"],
             [(a, "%+.2e" % c) for a, c in st["atoms"]]),
          flush=True)


# ================================ the priority census (the horizon)
def build_prio(census):
    by_key = {(c["h"], c["kz"]): c for c in census}
    hs = np.asarray([c["h"] for c in census], float)
    tie_cell = census[int(np.argmin(np.abs(hs - TIE_TGT)))]
    if SMOKE:
        c2200 = census[int(np.argmin(np.abs(hs - 2200)))]
        return tie_cell, [("SMOKE-A", tie_cell, None),
                          ("SMOKE-B", c2200, None)]
    prio = [("G1-8003", by_key[(8003, 284)], None),
            ("G2-7004", by_key[(7004, 517)], None),
            ("G3-6197", by_key[(6197, 337)], None),
            ("N1-BIN8003", by_key[(7958, 282)], None),
            ("N2-BIN8003", by_key[(8204, 287)], None),
            ("N3-DEEP", by_key[(9023, 506)], None),
            ("N4-DEEP", by_key[(8677, 299)], None),
            ("XS-SMOOTH", by_key[(7958, 282)], "smooth"),
            ("N5-STRETCH", by_key[(9535, 526)], None)]
    return tie_cell, prio


def census_build(census):
    section("CEN -- THE HORIZON CENSUS (verbatim builds in the "
            "frozen priority order, guard %.2f * %.2e * h^3 <= "
            "%.0f s)" % (GUARD_FAC, COST_C, BUILD_CAP_S))
    tie_cell, prio = build_prio(census)
    # ---- TIE ward: seat builder == bat builder, exactly
    r_bat = build_cell(tie_cell)
    r_seat = build_cell_seat(tie_cell)
    check("TIE seat builder ties bat.build_rung_param EXACTLY on "
          "h %d kz %d (tau %s negA %s lamS %s)"
          % (tie_cell["h"], tie_cell["kz"],
             "==" if r_seat["tau"] == r_bat["tau"] else "DIFF",
             "==" if r_seat["negA"] == r_bat["negA"] else "DIFF",
             "==" if r_seat.get("lamS") == r_bat.get("lamS")
             else "DIFF"),
          (r_seat["tau"] == r_bat["tau"]
           and r_seat["negA"] == r_bat["negA"]
           and r_seat.get("lamS") == r_bat.get("lamS")), kill="K2")
    ok_sw, det = seat_wards(r_seat, "TIE")
    check("SW1-SW6 seat wards on the TIE cell (%s)" % det, ok_sw,
          kill="K2")
    print_seat(r_seat)
    # ---- XA doctored-comb control on the TIE cell (pre-declared)
    xa_fired = False
    st = r_seat.get("seat")
    if st is not None:
        u2, mu2 = DEEP["U"], DEEP["MU"]
        alpha, mfold = tie_cell["alpha"], tie_cell["M"]
        ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        uu = u2[:ka]
        mm_doc = mu2[:ka].copy()
        nh = ka // 2
        mm_doc[:nh] = mm_doc[:nh][::-1]
        doc = float(np.sum(atom_circle_read(uu, mm_doc, alpha,
                                            mfold, st["uf"])))
        rel = abs(doc - st["dens_pr"]) / max(1.0, abs(st["dens_pr"]))
        xa_fired = rel > XA_FIRE
        check("XA the DOCTORED comb (first-half masses reversed) is "
              "REFUSED by the SW5 tie at the seat node: rel shift "
              "%.2e > %.0e" % (rel, XA_FIRE), xa_fired, kill="K4")
    else:
        check("XA doctored-comb control: seat read unavailable on "
              "the TIE cell", False, kill="K4")
    reads = []
    for tag, cell, world in prio:
        est = GUARD_FAC * COST_C * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-12s h %-6d kz %-4d UNBUILT-GUARD (est "
                  "%.0f s, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            reads.append(dict(tag=tag, cell=cell, world=world,
                              verdict="UNBUILT",
                              why="UNBUILT-GUARD", rung=None))
            continue
        tc = time.time()
        if world is not None:
            rung = build_cell(cell, world=world)
        else:
            rung = build_cell_seat(cell)
        ok, why = cell_legal(rung)
        marginal = ("tau" in rung
                    and abs(rung["tau"]) <= TAU_NOISE)
        verdict = ("MARGINAL" if marginal
                   else "LEGAL" if ok else why)
        reads.append(dict(tag=tag, cell=cell, world=world,
                          verdict=verdict, why=why, rung=rung,
                          marginal=marginal))
        tau_s = ("%.4g" % rung["tau"]) if "tau" in rung else "-"
        print("    %-12s h %-6d kz %-4d alpha %.4f%s  %-9s tau "
              "%-12s negA %s negS %s unit %s/%s  %.1f s"
              % (tag, cell["h"], cell["kz"], cell["alpha"],
                 (" [%s]" % world) if world else "", verdict,
                 tau_s, rung.get("negA", "-"), rung.get("negS", "-"),
                 rung.get("n_unit", "-"),
                 max(0, rung.get("n_neg_nodes", 0)
                     - rung.get("rank_g", 0)),
                 time.time() - tc), flush=True)
        if world is None:
            print_seat(rung)
    n_built = sum(1 for r in reads if r["rung"] is not None)
    check("CEN1 the census built %d items (%d unbuilt-guard, "
          "honestly censused)"
          % (n_built, len(reads) - n_built),
          n_built >= (2 if SMOKE else 4), kill="K1")
    return reads


def census_gates(reads):
    section("G -- reproduction gates against CCXCIX")
    if SMOKE:
        check("G1-G4 CCXCIX reproduction SMOKE-SKIPPED (typed; the "
              "frontier cells are not built in smoke)", True)
        return
    got = {(r["cell"]["h"], r["cell"]["kz"]): r for r in reads
           if r["rung"] is not None and r["world"] is None}
    for hv, kv, tref in GATE_NEGA:
        r = got.get((hv, kv))
        if r is None:
            check("G1/G3 NEGA cell h %d kz %d NOT BUILT" % (hv, kv),
                  False, kill="K3")
            continue
        tau = r["rung"].get("tau", float("nan"))
        ok = (r["rung"].get("negA", 0) >= 1
              and math.isfinite(tau)
              and abs(tau / tref - 1.0) <= NEGA_RTOL)
        check("G1/G3 NEGA repro h %d kz %d: tau %.4g vs CCXCIX "
              "%.4g (rtol %.0e), negA %d >= 1"
              % (hv, kv, tau, tref, NEGA_RTOL,
                 r["rung"].get("negA", 0)), ok, kill="K3")
    hv, kv, tref = GATE_LEG
    r = got.get((hv, kv))
    if r is None:
        check("G2 LEGAL cell h %d kz %d NOT BUILT" % (hv, kv),
              False, kill="K3")
    else:
        tau = r["rung"].get("tau", float("nan"))
        ok = (r["verdict"] == "LEGAL" and math.isfinite(tau)
              and abs(tau / tref - 1.0) <= NEGA_RTOL)
        check("G2 LEGAL repro h %d kz %d: %s, tau %.4g vs CCXCIX "
              "%.4g (rtol %.0e)"
              % (hv, kv, r["verdict"], tau, tref, NEGA_RTOL), ok,
              kill="K3")
    # G4: the seat reproduces on the built NEGA repro cells
    for hv, kv, _t in GATE_NEGA:
        r = got.get((hv, kv))
        if r is None:
            continue
        lc = r["rung"].get("loc", {})
        st = r["rung"].get("seat")
        ok = (st is not None and "rq_gap" in lc
              and st["uf"] == 2 and st["part"] >= PART_BAR
              and lc["rq_gap"] <= RQ_TIE)
        check("G4 SEAT repro h %d kz %d: top seat uf %s (== 2), "
              "part %s >= %.2f, rq_gap %s <= %.0e"
              % (hv, kv, st["uf"] if st else "-",
                 ("%.3f" % st["part"]) if st else "-", PART_BAR,
                 ("%.1e" % lc["rq_gap"]) if "rq_gap" in lc else "-",
                 RQ_TIE), ok, kill="K3")


# ============================================= anatomy + seat wards
def anatomy_wards(reads):
    section("AN/SW -- anatomy + seat wards on every built cell")
    n_rank = n_e8 = n_tot = 0
    n_sw = n_sw_ok = 0
    n_loc = n_loc_ok = 0
    for r in reads:
        rung = r["rung"]
        if rung is None or "tau" not in rung:
            continue
        if r["world"] is not None:
            continue
        n_tot += 1
        if "n_unit" in rung:
            expect = max(0, rung["n_neg_nodes"] - rung["rank_g"])
            if rung["n_unit"] >= expect:
                n_rank += 1
        if (rung["tau"] > 0.0 and rung.get("lamS") is not None
                and rung["lamS"] >= rung["tau"]
                - 1e-12 * max(1.0, abs(rung["tau"]))):
            n_e8 += 1
        elif rung["tau"] <= 0.0:
            n_e8 += 1
        n_sw += 1
        ok_sw, _det = seat_wards(rung, r["tag"])
        if ok_sw:
            n_sw_ok += 1
        lc = rung.get("loc", {})
        if "rq_gap" in lc:
            n_loc += 1
            if lc["rq_gap"] <= RQ_TIE:
                n_loc_ok += 1
    check("W7 RANK IDENTITY: #unit >= max(0, n_neg - rank(G)) on "
          "%d/%d built cells" % (n_rank, n_tot), n_rank == n_tot,
          kill="K2")
    check("W8 E8 ward lamS >= tau on every built PD cell (%d/%d; "
          "consumed nowhere)" % (n_e8, n_tot), n_e8 == n_tot,
          kill="K2")
    check("SW1-SW6 seat wards green on %d/%d built cells"
          % (n_sw_ok, n_sw), n_sw_ok == n_sw, kill="K2")
    check("SW4 localization tie rq_gap <= %.0e on %d/%d localized "
          "cells (refusals typed, non-kill per A6)"
          % (RQ_TIE, n_loc_ok, n_loc), True)


# ================================= the map + the horizon verdict
def legality_map(reads):
    section("MAP -- THE HORIZON MAP (bin fractions, MAX-TAU picks, "
            "seat anatomy census)")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"] and r["world"] is None]
    bins = []
    for lo, hi in HBINS:
        cells = [r for r in built if lo < r["cell"]["h"] <= hi]
        if not cells:
            continue
        n_leg = sum(1 for r in cells if r["verdict"] == "LEGAL")
        n_marg = sum(1 for r in cells if r["verdict"] == "MARGINAL")
        best = max((r for r in cells if r["verdict"] == "LEGAL"),
                   key=lambda r: r["rung"]["tau"], default=None)
        bins.append(dict(lo=lo, hi=hi, n=len(cells), n_leg=n_leg,
                         n_marg=n_marg, best=best))
        print("    bin (%6d, %6d]: %d built, %d LEGAL, %d MARGINAL"
              "%s"
              % (lo, hi, len(cells), n_leg, n_marg,
                 ("; MAX-TAU pick h %d kz %d tau %.4g"
                  % (best["cell"]["h"], best["cell"]["kz"],
                     best["rung"]["tau"])) if best else ""))
    # ---- the seat anatomy census
    rows = [r for r in built if r["rung"].get("seat") is not None]
    if rows:
        print("\n    SEAT ANATOMY TABLE (diagnostic tier):")
        print("    h      kz   verdict   tau          uf part  "
              "A_jj         BASE        COIN         a_share      "
              "gamma_eff")
        for r in sorted(rows, key=lambda r: r["cell"]["h"]):
            st = r["rung"]["seat"]
            print("    %-6d %-4d %-9s %+.4e %2d %.3f %+.4e "
                  "%+.4e %+.4e %.10f %.4e"
                  % (r["cell"]["h"], r["cell"]["kz"], r["verdict"],
                     r["rung"]["tau"], st["uf"], st["part"],
                     st["a_diag"], st["base"], st["coin"],
                     st["a_share"], st["gamma"]))
        sgn_track = sum(
            1 for r in rows
            if (r["rung"]["seat"]["a_diag"] > 0)
            == (r["rung"]["tau"] > 0))
        print("    sign(A_jj) tracks sign(tau) on %d/%d cells "
              "[MEASURED]" % (sgn_track, len(rows)))
        uf2 = sum(1 for r in rows if r["rung"]["seat"]["uf"] == 2)
        print("    seat identity: top seat uf = 2 on %d/%d cells "
              "[MEASURED]" % (uf2, len(rows)))
        if len(rows) >= 3:
            hs = [math.log10(r["cell"]["h"]) for r in rows]
            gs = [math.log10(r["rung"]["seat"]["gamma"])
                  for r in rows]
            s, e, r2, a = linfit(hs, gs)
            print("    gamma_eff drift: log10 gamma = %.4f %+.4f "
                  "log10 h (2SE %.4f, R2 %.3f) [CONJECTURE-GRADE, "
                  "a fit]" % (a, s, e, r2))
    return bins, built


def horizon_verdict(reads, bins):
    if SMOKE:
        return "LEGHOR-SMOKE(no frontier cells built by design)"
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"] and r["world"] is None
             and r["cell"]["h"] > HBINS[0][0]]
    if not built or not bins:
        return "LEGHOR-AMBIGUOUS(no frontier cell built)"
    deepest = max(built, key=lambda r: r["cell"]["h"])
    deep_bin = bins[-1]
    gaps = [b for b in bins if b["n_leg"] == 0]
    h_star = max((r["cell"]["h"] for r in built
                  if r["verdict"] == "LEGAL"), default=None)
    if all(b["n_leg"] >= 1 for b in bins) \
            and deepest["verdict"] == "LEGAL":
        return ("LEGHOR-CONTINUES-MEASURED(h* = %d; every built bin "
                "legal; rule MAX-TAU-PER-BIN)" % h_star)
    if deep_bin["n_leg"] >= 1 and gaps:
        return ("LEGHOR-GAPPED(h* = %d; gap bins %s)"
                % (h_star, ["(%d,%d]" % (b["lo"], b["hi"])
                            for b in gaps]))
    if deep_bin["n_leg"] == 0:
        second = bins[-2] if len(bins) >= 2 else None
        if (second is not None and second["n_leg"] == 0) \
                or deep_bin["n"] >= 2:
            return ("LEGHOR-TERMINATES-MEASURED(last legal h = %s "
                    "on the built horizon)" % h_star)
    return ("LEGHOR-AMBIGUOUS(deepest built h %d %s; single-sample)"
            % (deepest["cell"]["h"], deepest["verdict"]))


# ==================================================== controls
def controls(census, reads):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth "
            "profile incl. the new-band cell)")
    hs = np.asarray([c["h"] for c in census], float)
    tgt = 600 if SMOKE else XCTRL_TGT
    cell = census[int(np.argmin(np.abs(hs - tgt)))]
    scr = build_cell(cell, world="scramble", scr_seed=SCR_SEED)
    ok_s, why_s = cell_legal(scr)
    print("    scramble world h %d kz %d (seed %d): legal %s (%s) "
          "tau %s"
          % (cell["h"], cell["kz"], SCR_SEED, ok_s, why_s,
             ("%.4g" % scr["tau"]) if "tau" in scr else "-"))
    check("X1 the SCRAMBLE world fires: legality LEFT", not ok_s,
          kill="K4")
    smo = []
    cheap = census[int(np.argmin(np.abs(hs - (600 if SMOKE
                                              else X2_CHEAP))))]
    rung = build_cell(cheap, world="smooth")
    ok, why = cell_legal(rung)
    smo.append((cheap["h"], ok, why, rung.get("tau", float("nan"))))
    for r in reads:
        if r["world"] == "smooth" and r["rung"] is not None:
            ok, why = cell_legal(r["rung"])
            smo.append((r["cell"]["h"], ok, why,
                        r["rung"].get("tau", float("nan"))))
    for hv, ok, why, tau in smo:
        print("    SMOOTH world h %-6d legal %-5s (%s) tau %s"
              % (hv, ok, why,
                 ("%.4g" % tau) if math.isfinite(tau) else "-"))
    n_illegal = sum(1 for _h, ok, _w, _t in smo if not ok)
    deep_ok = SMOKE or any(hv >= 7000 for hv, ok, _w, _t in smo
                           if not ok)
    check("X2 the SMOOTH world LEGALITY PROFILE fires -- THE "
          "DISCRIMINATION: illegal at %d/%d tested depths%s"
          % (n_illegal, len(smo),
             "" if SMOKE else (", incl. the new-band cell (%s)"
                               % deep_ok)),
          n_illegal == len(smo) and len(smo) >= 1 and deep_ok,
          kill="K4")


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
  HONEST FRAME.  Finite float64 measurements on BUILT cells of the
  deployed deep-frame construction (TAB2 census, builder verbatim).
  Wall-legality is the CCLXXIII/CCLXIX cell_legal read of the
  ASSEMBLED float64 matrix (the known scope edge, A4); MARGINAL
  cells acknowledge the tau = 0 boundary of that object.  The seat
  reads are a DIAGNOSTIC tier consumed in no legality verdict; the
  weight split is exact at fixed node membership, and the arch part
  is closed-form in the LAG PROFILE seat only (the Christoffel read
  K is a per-cell measured number of the full world).  The horizon
  statement is about BUILT cells and the frozen bins, never all h;
  every extrapolation is a fit, typed CONJECTURE-GRADE.  No marker
  moves, no promotion, NO RH claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("legality_horizon_probe -- "
          "PRIME.ONEBADMODE.LEGALITY.HORIZON.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the circle readers see ENTRIES and frozen "
          "constants only (%s)" % (",".join(sorted(set(bad_r)))
                                   or "clean"), not bad_r, kill="K1")

    build_tab2()
    if KILLS:
        return finish([])
    census = deep_census()
    if KILLS:
        return finish([])

    reads = census_build(census)
    if KILLS:
        return finish([])
    census_gates(reads)
    anatomy_wards(reads)
    if KILLS:
        return finish([])

    bins, built = legality_map(reads)
    verdict = horizon_verdict(reads, bins)
    controls(census, reads)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations, no fitted "
          "level -- census + anatomy only, declared in spec)", True)

    labels = [verdict]
    n_leg = sum(1 for r in built if r["verdict"] == "LEGAL")
    n_nega = sum(1 for r in built if r["rung"]["tau"] <= 0.0)
    n_marg = sum(1 for r in built if r.get("marginal"))
    labels.append("LEGALITY-MAP(%d built, %d legal, %d tau<0, %d "
                  "marginal; horizon h %d)"
                  % (len(built), n_leg, n_nega, n_marg,
                     max((r["cell"]["h"] for r in built),
                         default=0)))
    rows = [r for r in built if r["rung"].get("seat") is not None]
    if rows:
        uf2 = sum(1 for r in rows if r["rung"]["seat"]["uf"] == 2)
        trk = sum(1 for r in rows
                  if (r["rung"]["seat"]["a_diag"] > 0)
                  == (r["rung"]["tau"] > 0))
        bases = [r["rung"]["seat"]["base"] for r in rows]
        coins = [r["rung"]["seat"]["coin"] for r in rows]
        labels.append("SEAT-ANATOMY(uf2 %d/%d, sign-track %d/%d, "
                      "BASE %.3g..%.3g, COIN %.3g..%.3g)"
                      % (uf2, len(rows), trk, len(rows),
                         min(bases), max(bases), min(coins),
                         max(coins)))
    if n_marg:
        labels.append("MARGINAL(%d)" % n_marg)
    return finish(labels)


if __name__ == "__main__":
    main()
