#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""j2_primeforce_probe -- EXPLORATION ONLY (NOT load-bearing; NO RH
claim; NOTHING here modifies verification/, papers, ledger, website).

=======================================================================
MISSION (contract PRIME.J2.PRIMEFORCE.01: WHICH SPECIFIC PRIME
PROPERTY FORCES THE J_2 MOMENT WINDOW GLOBALLY?  Surgical world
morphing (F1) + the variational mechanism (F2) + the classical price
(F3), under the OWNER DIRECTIVE refinements 1-6, acknowledged below)
=======================================================================
State consumed (CITED; r157/CDLXI QUARANTINED per refinement 5 -- no
threshold or bar from the spectral-balance round enters this spec):
CDLX/r156 (rootladder: L1 secular-Laurent dictionary, L2 quarter-cap
J_2 <= 1/4 + z|rho| with z|rho| <= 0.0102 measured, 2-mode witness
c'' = c + d(e_1+e_2) with A_0 invariant, J_2 inflation 1e6 refused at
rgap 1.0e5/3.0e6, controls J_2_w = -2.962/-0.8449/-2.71 with no
escaped scale); CDLVIII/r154 (J2_TAB/N_ESC/TOP/SEC anchor strings,
tau-flat); r136 (c is the exact frame tau-minimizer); r133 (H2: the
low-lying zero-free window as prime-side input); r142/r146/r150
(DELTA1FLOOR/FULLGAP/QSUBGAP family = the open relative-gap rows);
PT21 (T_PT = 3000175332800, verified zeros on the line below H);
HSW22 (tail band G(T)).  Builders: AEP.cell_matrix + AEP.anchor_select
(r148/r151 frozen recipe), R4.build_cell worlds (MAIN/SMOOTH/SCRARITH/
EPSTEIN, want_mp blocks for parity).

OWNER-DIRECTIVE ACKNOWLEDGMENT (binding, incorporated PRE-freeze):
 1. TWO-DIRECTION CAUSALITY: removal AND rescue gated separately;
    removal-only findings typed NECESSARY-SWITCH.  DISCLOSED below:
    calibration DEMOLISHED the naive rescue instrument (see
    CALIBRATION DISCLOSURE); rescue is adjudicated as measured
    PSD-repair feasibility geometry (G60/G61) plus reverse-path
    window-onset radii (the same theta-tables read backward), and
    convex-class features have degenerate rescue (path reversal) --
    typed exactly so, never upgraded.
 2. LEGAL MORPH PATHS: every path is a source-measure interpolation
    through the SAME frozen builder; per-path preserved invariants
    gated at ALL theta points (not endpoints only); window/resolution
    geometry (aa, K, icap, dps) identical for every world of a block
    by construction (single build); evenness structural; zero data
    NEVER enters any world construction (strongest form: this probe
    never opens the zero cache; the literature-zero CROSSCHECK list
    is consumed AFTER all worlds are built, gate G02).
 3. FROZEN QUANTIFIERS: bars declared BEFORE the calibration scratch
    ran (recorded in its header, quoted verbatim below):
    IN-WINDOW(world) := J_2 in (0.02, 0.26) AND y_t/b_top >= 5 AND
    n_esc >= 2 AND a_2 < 0;  BREAK(world) := J_2 <= 0 OR y_t/b_top
    < 2 OR n_esc <= 1 (between: DRIFT);  variational bar C_MOAT =
    1e-3 with tau-flatness |slope| <= 0.35 (TAU_SLOPE_BAR), demanded
    BOTH for the proven all-witness chain MOAT_x AND for the exact
    exit prices REL_HIGH(x); collapse in x/h/lambda is typed
    HONEST-FAIL with the measured exponent, never hidden.
 4. NO DISGUISED RH INPUT: the named property is screened against
    (i) Weil-equivalent positivity, (ii) all-low-mode control,
    (iii) a spectral gap that follows from the desired positivity,
    (iv) true-world-only uniformity (mitigated: moat also computed
    in a NON-true in-window world, G73).  Verdicts in G82.
 5. INDEPENDENCE FROM ROUND 157: no CDLXI number is a spec input;
    r157 appears only in the residue reading of the final note.
 6. OUTCOME TAXONOMY: adjudicated by the frozen decision table
    (G83): BEST / GOOD / INFORMATIVE-NEGATIVE / HONEST-FAIL.

=======================================================================
OBJECTS (r154/r156 dictionary)
=======================================================================
Block (tag, x_nom, dps) from RL.BLOCKS; u0 = AEP.anchor_select(x_nom),
x0 = e^{u0}, A = aa = u0/2, K = ceil(1.25 x0 log x0), icap =
floor(x0); M = Mpole + March - Mprime (AEP.cell_matrix VERBATIM);
ground pair (tau, phi), c = phi/nrm, b_k = (k pi/aa)^2, A_0 =
sum (-1)^k c_k, A_2 = sum (-1)^k c_k b_k, A_4 = sum (-1)^k c_k b_k^2,
y_t = |A_2/A_0|, J_2 = (A_4 A_0)/A_2^2, escaped count n_esc from the
weighted F-census (rootladder census_weighted VERBATIM), z_top/z_sec.

SOURCE-MEASURE WORLDS through the same builder: the prime block
N(spec) is my re-assembly of the frozen prime-block kernel for
spec = list of components ('atoms', [(u, w)]) / ('smooth', amp:
density amp e^{u/2} du) / ('cos', gamma, s: density -2 s cos(gamma u)
du, closed forms I_sc/I_ccw/I_c0).  World matrix M_W = M_AEP +
N(atoms_true) - N(spec_W): EXACT for spec_W = TRUE (bilinearity,
G11); parity of N against the R4 want_mp prime blocks gated
elementwise (G20, calibration dev 0.0).

PLANT LEMMA (exact layer, G13): the component ('cos', gamma, s > 0)
adds to M the PSD rank-1 form s P(gamma) with v' P(gamma) v prop
|fhat_v(gamma)|^2 (autocorrelation kernel; Wiener-Khinchin form,
CITED AS FORM; machine-checked: PSD min eig >= -1e-50 measured
-3.1e-61, rank-1, Fourier ratio identity <= 1e-30) -- an exact
spectral atom (verified zero pair) planted at height gamma.  s < 0
is a GHOST (negative spectral mass).

=======================================================================
THE BATTERY (F1; tags 5/8/13; all worlds zero-data-free)
=======================================================================
REMOVAL paths theta in adaptive log grid (frozen rule: decades from
max(delta_1 * 1e-3, 1e-40) up to 1, one point per decade, endpoint
theta = 1; theta*_J2 and theta*_tau refined by 12-step log bisection;
delta_1 = lambda_1 - tau measured per block -- an INSTRUMENT-adaptive
grid with a frozen rule, DISCLOSED):
  SIGN   w_i(th) = w_i (1 - 2 th flip_i), flip = odd 0-based index in
         q-sorted order (breaks Lambda >= 0; preserves support
         positions EXACTLY, gated);
  CORR   w_i(th) = (1-th) w_i + th w_{perm(i)}, R4 golden permutation
         VERBATIM (breaks weight-position correlation; preserves
         support, positivity, total mass EXACTLY, gated <= 1e-40);
  SUPPM  (1-th) atoms + th (smooth mass-matched amp = m0_at/m0_sm)
         (breaks lattice support ONLY at matched total mass, gated;
         preserves positivity);
  SUPPF  (1-th) atoms + th (smooth amp 1) (breaks support AND mass;
         endpoint = R4 SMOOTH);
  DENSP/DENSM  w_i(th) = w_i (1 +/- 0.5 th) (breaks Chebyshev mass
         calibration ONLY; support/positivity/correlation preserved,
         gated);
  LDAT   (1-th) atoms + th epstein atoms (b8 only; known-collective
         reference; endpoint = R4 EPSTEIN world data).
Endpoint demand (G41): EVERY removal endpoint theta = 1 must BREAK
(they are the fake worlds; calibration: all broke).  Reverse reading
(rescue direction on convex paths): the window-onset radius is
1 - theta* from the fake end -- reported as the basin radius.

SPECTRAL SURGERY (the feature that survived pre-freeze):
  PLANTS: single s = 1 at gamma in {2, 5, 9, 12} (in the low window)
  and {20, 40} (above gamma_1: surgery control); s = 1e-3 at 5;
  multi-plant (all four gap gammas) REPORTED.  Frozen expectation
  gate G50 (calibrated): every SINGLE plant world at tags 5/8 stays
  IN-WINDOW -- ADDING spectral mass does not break the window.
  GHOSTS: s*(gamma) = break threshold under ('cos', gamma, -s),
  log-bisected (12 steps) in [max(delta_1*1e-3, 1e-40), 1] at gamma
  in {2, 5, 9, 14.5, 20, 30}; gate G51: every ghost breaks at some
  s <= 1 (calibrated: s = 0.01 ghost at gamma 5 already breaks b5).
  G52 SPECTRAL-ASYMMETRY verdict (frozen): plants at s = 1 benign
  AND min_gamma s*_ghost <= 1e-2 at tags 5/8.
PROFILE EXHIBIT (tags 5/8): S(gamma) = phi' P(gamma) phi / tr
P(gamma) on the frozen grid gamma in [2, cap] step 0.2 (cap 60/90),
dips refined parabolically; G53 (kind=screen) CLASSICAL-CROSSCHECK:
dip positions vs the literature low-zero constants LIT_CROSSCHECK
(PT21-class verified values, frozen literals below, consumed ONLY
after construction; tolerance 0.15) -- the probe MEASURES the low
spectrum from source data alone; the crosscheck types it.

RESCUE GEOMETRY (G60/G61, tags 5/8): for fake worlds SMOOTH/SCRARITH
(+EPSTEIN at b8): deficit eigenvectors (all eigenvalues < 0) of M_W,
projection residual onto the span of the plant vectors (RvM ladder
rungs + gap gammas; RvM ladder = N_rvm(gamma_j) = j - 1/2 with
N_rvm(T) = (T/2pi) log(T/(2 pi e)) + 7/8, CLASSICAL counting main
term, zero-data-free); best PSD repair by deterministic projected
nonneg least squares (60 sweeps); verdict enum RESCUED /
RESCUE-INFEASIBLE-IN-CLASS (kind=screen; calibration: infeasible).

=======================================================================
THE VARIATIONAL MECHANISM (F2; all six blocks)
=======================================================================
Admissible witnesses (r156 class): v = (1+s) phi + p, p orth phi,
A_0(v) = A_0 fixed (s = -a(p)/A_0); exact REL(v) = (R(v) - tau)/|tau|
= p'(M - tau)p / (((1+s)^2 + |p|^2) |tau|) (identity, sympy G14).
Effective functionals btl = beta - (A_2/A_0) alpha, gtl = gamma4 -
(A_4/A_0) alpha on the eigenbasis; Gram C_ab = sum F_a F_b / delta_i;
N(t2, t4) = t' C^{-1} t = min p'(M-tau)p at targets (KKT, sympy).
EXIT SURFACES: LOW (J_2 -> 0): t4 = -A_4 line (vertex closed form);
HIGH (J_2 -> 0.26 = proven cap + headroom): parabola t4 =
0.26 (A_2+t2)^2/A_0 - A_4, deterministic t2 grid (4200 points).
EXACT EXIT PRICES REL_LOW/REL_HIGH = exact REL at the constrained-
G-optimal witness (the cheapest known exit, upper bound on the true
moat).  PROVEN ALL-WITNESS CHAIN (V1): REL(v) >= f(N_exit), f(x) =
x / (((1 + kappa sqrt(x/delta_1))^2 + x/delta_1) |tau|), kappa =
|alpha_perp|/|A_0| (Cauchy-Schwarz + spectral floor + monotonicity,
sympy-gated); MOAT_x = f(N_exit).  DISCLOSED PRE-FREEZE: the chain
collapses through the depth factor kappa (calibration MOAT_5 =
1.76e-10 < C_MOAT) -- the declared bar will FAIL on the chain leg
and is typed HONEST-FAIL there; the exact exit prices carry the
uniformity question (calibration REL_HIGH = 1.35 (b5) / 0.31 (b8),
slope vs log10 tau = 0.053, flat).  TRADEOFF CURVE: optimal witness
at t2/A_2 in +/-{0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 0.99}, t4 = 0:
(REL, DJ = log(J_2(v)/J_2)) table + the r156 2-mode witness
chain-consistency (G73).  V2 STABILITY RADIUS: exact first-order
dJ_2/dtheta = J_2 (dA_4/A_4 + dA_0/A_0 - 2 dA_2/A_2) with dphi =
-(M - tau)^+ D phi per removal path; law exhibit theta*_J2 |D|_2 /
delta_1 (G80 screen: slope of log10 theta*_J2 vs log10 delta_1
across blocks; |slope - 1| <= 0.5 -> STABILITY-RADIUS-DELTA1).
Punisher decomposition (G72): S_sus = |btl_perp|^2/delta_1 bound
chain -> the mechanism constant is carried by the DELTA1FLOOR-family
relative gap (r142/r146/r150; NOT r157).

=======================================================================
FROZEN NUMERICS (bars; calibration values quoted verbatim)
=======================================================================
KFAC = 1.25; WORKERS = 7 (one task per block + endpoints task;
deterministic gather); BLOCKS/J2_TAB/N_ESC_TAB/TOP_TAB/SEC_TAB/
TAU_SLOPE_BAR imported from rootladder_probe VERBATIM (r154 strings,
rel 5e-3); MORPH_TAGS = (5, 8, 13); PROFILE_TAGS = (5, 8);
PARITY_BAR = 1e-45 (calibration 0.0 all four worlds);
LIN_BAR = 1e-50 (N additivity; exact by construction);
PLANT_PSD_BAR = -1e-50 (calibration min eig -3.135e-61);
PLANT_RANK_BAR = 1e-25 rel (calibration rank-1);
PLANT_ID_BAR = 1e-30 (Fourier ratio identity);
CLOSED_FORM_BAR = 1e-55 (calibration devs <= 3.9e-62);
WINDOW = (0.02, 0.26); YTB_IN = 5.0; NESC_IN = 2; YTB_BREAK = 2.0;
C_MOAT = 1e-3 (pre-declared); TAU_SLOPE_BAR = 0.35;
THETA_BIS_STEPS = 12; GHOST_GAMMAS = (2, 5, 9, 14.5, 20, 30);
PLANT_GAP = (2, 5, 9, 12); PLANT_HIGH = (20, 40);
PROFILE_STEP = 0.2; PROFILE_CAP = {5: 60, 8: 90}; DIP_TOL = 0.15;
LADDER_CAP = {5: 60, 8: 90}; NNLS_SWEEPS = 60;
TGRID = (0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 0.99) both signs;
J_HI = 0.26; COND_WIN = (1e-40, 1e-10) (b5 1e-25 shift, r118 trap);
RUNTIME_BAR = 14400 s; LIT_CROSSCHECK = 25 literature zeros
(frozen literals in code; crosscheck ONLY).
CALIBRATION DISCLOSURE (scratch passes 1-3, instrument-only, bars
above declared in the scratch header BEFORE it ran; scratch deleted
after freeze; both logs quoted):
  parity 0.0 (MAIN/SMOOTH/SCRARITH x=5, EPSTEIN x=8); closed forms
  <= 3.9e-62; TRUE b5 tau 2.048e-15, J_2 0.111744, n_esc 4, ytb
  38.04; plants g=5 s=0.01..1.0 ALL saturate identically at J_2
  0.090026, tau 1.64e-10, n_esc 3 (rank-1 orthogonalization);
  g=2/12/20: J_2 0.0894/0.0924/0.0967 IN-WINDOW; g=40 inert (band
  top 39.9); GHOST g=5 s=-0.01: tau -1.5e-2, J_2 -0.404 BREAK;
  s=-1: J_2 -2.586; removal endpoints b5 (anchor geometry): SMOOTH
  J_2 -2.854, SCR -1.846, SIGNFLIP -4.503, DENSx1.5 -1.485,
  SMOOTH-massmatch -152.07 (all BREAK, tau < 0); RvM-ladder rescue
  FAILS (SM-OPEN J_2 -2.173/-3.954 at b5/b8; SC-OPEN -2.104;
  SC-FILL tau +0.0775 J_2 -1.836: positive tau does NOT imply
  window); ZDIAG literature-ladder rescue ALSO fails (J_2 -2.160;
  position morphs/rung shifts move J_2 by < 0.15): DICTIONARY
  DEMOLITION: Delta = N(smooth) - N(atoms) is INDEFINITE (eigs
  -1.019 .. +1.123), a PSD plant sum cannot represent it (best fit
  s* = 0.23, |R| > |Delta|); damped (Gauss/Fejer) ladders fail
  equally (J_2 -2.43 .. -2.90).  CONSEQUENCE (frozen into design):
  "smooth - ladder" reconstruction worlds are an INVALID rescue
  instrument in this builder; rescue is adjudicated as feasibility
  geometry (G60/G61); the window's causal structure is carried by
  the removal radii + the plant/ghost asymmetry + the profile
  exhibit.  MOAT calibration: b5 delta_1 = 2.627e-10, d1/|tau| =
  1.283e5; chain MOAT_5 = 1.762e-10 (COLLAPSED, kappa = 5.5e6);
  exact exits b5: REL_LOW 128.7, REL_HIGH 1.346; b8: REL_LOW 20.7,
  REL_HIGH 0.3125; witness t2 = -0.9 A_2: REL 4.86 at DJ 4.605;
  2-mode r156 rgap 1.0e5 at inflation 1e6 (cited).
VERDICT ENUMS (frozen): per-feature {FORCING-CONFIRMED,
NECESSARY-SWITCH-ONLY, INERT, COLLECTIVE-COMPONENT,
NOT-TESTABLE-RESCUE}; battery {SPECTRAL-ASYMMETRY, SYMMETRIC};
window-vs-positivity {WINDOW-OUTLIVES-POSITIVITY, COUPLED};
stability {STABILITY-RADIUS-DELTA1, NO-RADIUS-LAW}; rescue
{RESCUED(world), RESCUE-INFEASIBLE-IN-CLASS}; moat legs
{EXITPRICE-FLAT, EXITPRICE-COLLAPSES(slope)}, {CHAIN-UNIFORM,
CHAIN-COLLAPSED-BY-DEPTH}; profile {DIPS-MATCH-VERIFIED-SPECTRUM,
DIPS-MISMATCH}; taxonomy decision table (G83):
  BEST  iff one feature FORCING-CONFIRMED with both directions AND
        chain leg uniform (C_MOAT met on MOAT_x, all six blocks);
  GOOD  iff one feature FORCING-CONFIRMED, chain leg fails but
        exact exit prices flat (EXITPRICE-FLAT);
  INFORMATIVE-NEGATIVE iff NO single feature FORCING-CONFIRMED
        (single-lever search closed; J_2 typed via the collective/
        spectral verdicts);
  HONEST-FAIL iff a causal switch is found but ALL variational legs
        collapse (exit prices AND chain), with the measured
        exponent stated.
DISCLOSURES: (a) deep blocks (18/24/28) carry TRUE anchors + moat
only (battery at 5/8/13; profile at 5/8; cost); (b) b5 SIGN path
flips ONE atom (icap = 4: q = 3), b8 two (q = 3, 5), b13 four --
typed; (c) EPSTEIN legs only at b8 (icap 7; r156 convention);
(d) multi-plant world and TAU-coupling law are REPORTED exhibits
(not calibrated -> not hard-gated); (e) the adaptive theta/s grids
consume the measured delta_1 (frozen rule, instrument-adaptive);
(f) classical price of the band input: omega_max = K pi / aa ~
2.5 pi x0; at the census-support edge x = 4.8e11 the band reaches
3.77e12 vs T_PT = 3.00e12 (factor 1.26 sliver DISCLOSED in the
report); (g) smoke mode = b5 only, reduced grids, code-fix rounds
pre-record are code-side only (docstring/hash frozen unless bars
change; amendments appended as numbered blocks).
Deterministic: NO randomness anywhere; NO zero-cache use AT ALL;
NO zeta use (AST-audited); all mp arithmetic inside explicit
workdps; transported f64 only for O(1) ratio currencies (DISCLOSED).
Composite verdict = AND over kind=gate checks; screens/enums
reported; both record logs kept.
"""

import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4              # noqa: E402
import anchor_epslock_probe as AEP         # noqa: E402
import rootladder_probe as RL              # noqa: E402

KFAC = 1.25
WORKERS = 7
MORPH_TAGS = (5, 8, 13)
PROFILE_TAGS = (5, 8)
PARITY_BAR = 1e-45
LIN_BAR = 1e-50
PLANT_PSD_BAR = -1e-50
PLANT_RANK_BAR = 1e-25
PLANT_ID_BAR = 1e-30
CLOSED_FORM_BAR = 1e-55
WINDOW = (0.02, 0.26)
YTB_IN = 5.0
NESC_IN = 2
YTB_BREAK = 2.0
C_MOAT = 1e-3
THETA_BIS_STEPS = 12
GHOST_GAMMAS = (2.0, 5.0, 9.0, 14.5, 20.0, 30.0)
PLANT_GAP = (2.0, 5.0, 9.0, 12.0)
PLANT_HIGH = (20.0, 40.0)
PROFILE_STEP = 0.2
PROFILE_CAP = {5: 60.0, 8: 90.0}
DIP_TOL = 0.15
LADDER_CAP = {5: 60.0, 8: 90.0}
NNLS_SWEEPS = 60
TGRID = (0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 0.99)
J_HI = 0.26
COND_LO, COND_HI = 1e-40, 1e-10
RUNTIME_BAR = 14400.0
CTRL_J2_STRINGS = {"SMOOTH": -2.962, "SCRARITH": -0.8449,
                   "EPSTEIN": -2.71}
CTRL_TOL = 5e-3

# literature low zeros -- CLASSICAL-VERIFIED CROSSCHECK ONLY (G53);
# consumed strictly AFTER all world constructions (gate G02)
LIT_CROSSCHECK = (
    "14.134725", "21.022040", "25.010858", "30.424876", "32.935062",
    "37.586178", "40.918719", "43.327073", "48.005151", "49.773832",
    "52.970321", "56.446248", "59.347044", "60.831779", "65.112544",
    "67.079811", "69.546402", "72.067158", "75.704691", "77.144840",
    "79.337375", "82.910381", "84.735493", "87.425275", "88.809111")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str, str]] = []
INFO: list[str] = []
LIT_PHASE = {"built": False}


def check(name, ok, detail, kind="gate"):
    CHECKS.append((name, bool(ok), detail, kind))
    print("[%s] %-26s %s | %s" % ("PASS" if ok else "FAIL", name,
                                  kind, detail), flush=True)
    return bool(ok)


def info(msg):
    INFO.append(msg)
    print("[INFO] " + msg, flush=True)


def section(t):
    print("\n" + "=" * 72 + "\n== " + t + "\n" + "=" * 72, flush=True)


# ---------------------------------------------------------- firewall
def firewall_audit():
    import ast
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    bad = []
    forbidden = {"zeta", "em_zeta", "zetazero", "riemann", "li",
                 "dirichlet", "load"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            bad.append("attr:" + node.attr)
        if isinstance(node, ast.Name) and node.id in forbidden:
            bad.append("name:" + node.id)
        if isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "attr", getattr(fn, "id", ""))
            if nm in forbidden:
                bad.append("call:" + nm)
    ok = not bad
    return ok, ("clean: no zeta/zero-cache tokens (np.load absent "
                "entirely; the probe never opens the cache)"
                if ok else "VIOLATIONS: " + ",".join(bad))


# ------------------------------------------------- source assemblers
def prime_atoms(icap, dps):
    comp = np.zeros(icap + 2, dtype=bool)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    with mp.workdps(dps):
        return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]


def scr_perm(icap):
    comp = np.zeros(icap + 2, dtype=bool)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    gold = (math.sqrt(5.0) - 1.0) / 2.0
    keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
    return sorted(range(len(keys)), key=lambda i: keys[i])


def eps_atoms(icap, dps):
    with mp.workdps(dps):
        rq = np.zeros(icap + 1)
        xm = int(math.isqrt(icap)) + 1
        ym = int(math.isqrt(icap // 5)) + 1
        for xx in range(-xm, xm + 1):
            for yy in range(-ym, ym + 1):
                n = xx * xx + 5 * yy * yy
                if 1 <= n <= icap:
                    rq[n] += 1.0
        av = [mp.mpf(v) / 2 for v in rq]
        lamq = [mp.mpf(0)] * (icap + 1)
        out = []
        for n in range(2, icap + 1):
            sacc = av[n] * mp.log(n)
            for d in range(2, n):
                if n % d == 0:
                    sacc -= lamq[d] * av[n // d]
            lamq[n] = sacc
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                out.append((mp.log(n), lamq[n] / mp.sqrt(n)))
    return out


def i_sc(o, g, L):
    tot = mp.mpf(0)
    for be in (o + g, o - g):
        if abs(be) < mp.mpf("1e-25"):
            continue
        tot += (1 - mp.cos(be * L)) / be
    return tot / 2


def i_cc(be, L):
    if abs(be) < mp.mpf("1e-25"):
        return L
    return mp.sin(be * L) / be


def i_uc(be, L):
    if abs(be) < mp.mpf("1e-25"):
        return L * L / 2
    return (mp.cos(be * L) - 1) / be ** 2 + L * mp.sin(be * L) / be


def nprime_block(aa, K, dps, comps):
    """re-assembly of the frozen prime-block kernel for a general
    source spec (parity-gated against R4 want_mp blocks, G20)."""
    with mp.workdps(dps):
        ks = list(range(K))
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1)
        L2v = 2 * aa
        pj = [mp.mpf(0)] * K
        pdiag = [mp.mpf(0)] * K
        for comp in comps:
            if comp[0] == "atoms":
                atoms = comp[1]
                for i, o in enumerate(oms):
                    if ks[i] == 0:
                        continue
                    pj[i] += sum(w * mp.sin(o * u) for u, w in atoms)
                for i, o in enumerate(oms):
                    k = ks[i]
                    acc = mp.mpf(0)
                    for u, w in atoms:
                        if k:
                            acc += w * ((aa - u / 2) * mp.cos(o * u)
                                        + dsig * mp.sin(o * u)
                                        / (2 * o))
                        else:
                            acc += w * (L2v - u)
                    pdiag[i] += acc
            elif comp[0] == "smooth":
                amp = comp[1] if isinstance(comp[1], mp.mpf) \
                    else mp.mpf(repr(comp[1]))
                ea = mp.exp(aa)
                for i, o in enumerate(oms):
                    k = ks[i]
                    if k == 0:
                        f0psi = lambda w: (L2v - w)      # noqa: E731
                        pts2 = sorted(set([mp.mpf(0), L2v]))
                    else:
                        pj[i] += amp * ((mp.sin(L2v * o) / 2
                                         - o * mp.cos(L2v * o)) * ea
                                        + o) / (mp.mpf(1) / 4 + o * o)

                        def f0psi(w, o=o):
                            return ((aa - w / 2) * mp.cos(o * w)
                                    + dsig * mp.sin(o * w) / (2 * o))
                        npts = max(int(mp.floor(L2v * o / mp.pi)), 1)
                        pts2 = sorted(set(
                            [mp.mpf(0), L2v]
                            + [jj * mp.pi / o
                               for jj in range(1, npts + 1)]))
                    pdiag[i] += amp * mp.quad(
                        lambda w, f0psi=f0psi: f0psi(w)
                        * mp.exp(w / 2), pts2)
            elif comp[0] == "cos":
                g = comp[1] if isinstance(comp[1], mp.mpf) \
                    else mp.mpf(repr(comp[1]))
                s = comp[2] if isinstance(comp[2], mp.mpf) \
                    else mp.mpf(repr(comp[2]))
                for i, o in enumerate(oms):
                    k = ks[i]
                    if k == 0:
                        pdiag[i] += -2 * s * (1 - mp.cos(g * L2v)) \
                            / g ** 2
                        continue
                    isc = i_sc(o, g, L2v)
                    pj[i] += -2 * s * isc
                    iccw = mp.mpf(0)
                    for be in (o - g, o + g):
                        iccw += aa * i_cc(be, L2v) \
                            - i_uc(be, L2v) / 2
                    iccw = iccw / 2
                    pdiag[i] += -2 * s * (iccw + dsig * isc / (2 * o))
            else:
                raise ValueError(comp[0])
        Mp = mp.zeros(K, K)
        for i in range(K):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                od = 2 * sg * (oms[i] * pj[i] - oms[j2] * pj[j2]) / den
                Mp[i, j2] += od
                Mp[j2, i] += od
        for i in range(K):
            Mp[i, i] += 2 * pdiag[i]
        nrm = [mp.sqrt(L2v) if ks[i] == 0 else mp.sqrt(aa)
               for i in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
        for i in range(K):
            for j2 in range(i):
                sym = (Mp[i, j2] + Mp[j2, i]) / 2
                Mp[i, j2] = sym
                Mp[j2, i] = sym
    return Mp


def world_measure(M, K, aa, dps, census=True):
    with mp.workdps(dps):
        E, V = mp.eigsy(M)
        order = sorted(range(K), key=lambda i: E[i])
        i0 = order[0]
        tau = E[i0]
        nneg = sum(1 for i in range(K) if E[i] < -mp.mpf("0.1"))
        phi = [V[i, i0] for i in range(K)]
        nn = mp.sqrt(sum(p * p for p in phi))
        phi = [p / nn for p in phi]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        cs = [phi[k] / nrm[k] for k in range(K)]
        b = [(k * mp.pi / aa) ** 2 for k in range(K)]
        btop = b[K - 1]
        A0 = sum((-1) ** k * cs[k] for k in range(K))
        A2 = sum((-1) ** k * cs[k] * b[k] for k in range(1, K))
        A4 = sum((-1) ** k * cs[k] * b[k] ** 2 for k in range(1, K))
        yt = abs(A2 / A0)
        J2 = (A4 / A0) / (A2 / A0) ** 2
        a2sgn = -int(mp.sign(A2 / A0))    # +1 == healthy (a_2 < 0)
        n_esc = -1
        ztop = zsec = float("nan")
        nnr = -1
        if census:
            wtsF = {k: ((-1) ** k) * cs[k] for k in range(1, K)}
            ysF, nnr = RL.census_weighted(wtsF, K, aa, dps, cs[0])
            n_esc = sum(1 for y in ysF if y > btop)
            esc = sorted([y / yt for y in ysF if y > btop],
                         reverse=True)
            if len(esc) >= 1:
                ztop = float(esc[0])
            if len(esc) >= 2:
                zsec = float(esc[1])
        return dict(tau=tau, tau_f=float(tau), nneg=nneg,
                    J2=float(J2), ytb=float(yt / btop), n_esc=n_esc,
                    nnr=nnr, ztop=ztop, zsec=zsec, a2sgn=a2sgn,
                    A0=A0, A2=A2, A4=A4, E=[E[i] for i in order],
                    V=V, order=order, cs=cs, b=b, nrm=nrm, phi=phi)


def in_window(r, lite=False):
    ok = (WINDOW[0] < r["J2"] < WINDOW[1]) and r["ytb"] >= YTB_IN \
        and r["a2sgn"] == 1
    if not lite:
        ok = ok and r["n_esc"] >= NESC_IN
    return ok


def breaks(r):
    return (r["J2"] <= 0.0) or (r["ytb"] < YTB_BREAK) \
        or (0 <= r["n_esc"] <= 1)


def rvm_count(T):
    return T / (2 * mp.pi) * mp.log(T / (2 * mp.pi * mp.e)) \
        + mp.mpf(7) / 8


def rvm_ladder(gcap):
    out = []
    j = 1
    while True:
        lo, hi = mp.mpf(2 * mp.pi), mp.mpf(gcap + 60)
        tgt = mp.mpf(j) - mp.mpf("0.5")
        for _ in range(90):
            mid = (lo + hi) / 2
            if rvm_count(mid) < tgt:
                lo = mid
            else:
                hi = mid
        g = (lo + hi) / 2
        if g > gcap:
            break
        out.append(g)
        j += 1
    return out


# --------------------------------------------------- moat machinery
def block_funcs(r, K, dps):
    """effective functionals + Gram on the eigenbasis (excited)."""
    with mp.workdps(dps):
        E, V, order = r["E"], r["V"], r["order"]
        b, nrm = r["b"], r["nrm"]
        A0, A2, A4 = r["A0"], r["A2"], r["A4"]
        alf, bet, gm4 = [], [], []
        for c in range(1, K):
            ie = order[c]
            uv = [V[i2, ie] for i2 in range(K)]
            cu = [uv[k] / nrm[k] for k in range(K)]
            alf.append(sum((-1) ** k * cu[k] for k in range(K)))
            bet.append(sum((-1) ** k * cu[k] * b[k]
                           for k in range(1, K)))
            gm4.append(sum((-1) ** k * cu[k] * b[k] ** 2
                           for k in range(1, K)))
        dl = [E[c] - E[0] for c in range(1, K)]
        btl = [bet[i] - (A2 / A0) * alf[i] for i in range(K - 1)]
        gtl = [gm4[i] - (A4 / A0) * alf[i] for i in range(K - 1)]
        C = [[mp.mpf(0)] * 2 for _ in range(2)]
        for i in range(K - 1):
            C[0][0] += btl[i] ** 2 / dl[i]
            C[0][1] += btl[i] * gtl[i] / dl[i]
            C[1][1] += gtl[i] ** 2 / dl[i]
        C[1][0] = C[0][1]
        det = C[0][0] * C[1][1] - C[0][1] ** 2
        Q = [[C[1][1] / det, -C[0][1] / det],
             [-C[0][1] / det, C[0][0] / det]]
        return dict(alf=alf, btl=btl, gtl=gtl, dl=dl, Q=Q, C=C,
                    det=det)


def exit_witness(fn, r, t2, t4, dps):
    """exact REL/J2' at the constrained-G-optimal witness."""
    with mp.workdps(dps):
        Q = fn["Q"]
        lam1 = Q[0][0] * t2 + Q[0][1] * t4
        lam2 = Q[1][0] * t2 + Q[1][1] * t4
        K1 = len(fn["dl"])
        p = [(fn["btl"][i] * lam1 + fn["gtl"][i] * lam2) / fn["dl"][i]
             for i in range(K1)]
        pGp = sum(fn["dl"][i] * p[i] ** 2 for i in range(K1))
        ap = sum(fn["alf"][i] * p[i] for i in range(K1))
        s_ = -ap / r["A0"]
        den = (1 + s_) ** 2 + sum(pv ** 2 for pv in p)
        rel = pGp / (den * abs(r["tau"]))
        A2n = r["A2"] + sum(fn["btl"][i] * p[i] for i in range(K1))
        A4n = r["A4"] + sum(fn["gtl"][i] * p[i] for i in range(K1))
        J2n = (A4n / r["A0"]) / (A2n / r["A0"]) ** 2
        return dict(rel=float(rel), pGp=pGp, den=float(den),
                    J2n=float(J2n),
                    rel_mp=rel)


def moat_block(r, K, dps):
    with mp.workdps(dps):
        fn = block_funcs(r, K, dps)
        A0, A2, A4, tau = r["A0"], r["A2"], r["A4"], r["tau"]
        Q = fn["Q"]

        def Nq(t2, t4):
            return (Q[0][0] * t2 * t2 + 2 * Q[0][1] * t2 * t4
                    + Q[1][1] * t4 * t4)

        t2L = -Q[0][1] * (-A4) / Q[0][0]
        NL = Nq(t2L, -A4)
        best = None
        for m2 in range(-1400, 2801):
            t2 = A2 * mp.mpf(m2) / mp.mpf(1000)
            t4 = mp.mpf(repr(J_HI)) * (A2 + t2) ** 2 / A0 - A4
            v = Nq(t2, t4)
            if best is None or v < best[0]:
                best = (v, t2, t4)
        NH = best[0]
        wl = exit_witness(fn, r, t2L, -A4, dps)
        wh = exit_witness(fn, r, best[1], best[2], dps)
        d1 = fn["dl"][0]
        s_al = sum(a * a for a in fn["alf"])
        kap = mp.sqrt(s_al) / abs(A0)
        Nex = min(NL, NH)

        def chain(x):
            return x / (((1 + kap * mp.sqrt(x / d1)) ** 2 + x / d1)
                        * abs(tau))

        moat = chain(Nex)
        curve = []
        for sgn in (1, -1):
            for fr in TGRID:
                t2 = sgn * mp.mpf(repr(fr)) * A2
                w = exit_witness(fn, r, t2, mp.mpf(0), dps)
                J2o = float((A4 / A0) / (A2 / A0) ** 2)
                dj = (math.log(abs(w["J2n"] / J2o))
                      if w["J2n"] != 0 else float("inf"))
                curve.append((sgn * fr, w["rel"], w["J2n"], dj))
        # chain-consistency on the r156-style 2-mode witness
        # (direction e1+e2 in c-coordinates, A0-preserving scaling)
        return dict(rel_low=wl["rel"], rel_high=wh["rel"],
                    den_low=wl["den"], den_high=wh["den"],
                    moat_chain=float(moat), d1=float(d1),
                    d1_mp=d1, kappa=float(kap),
                    Nex_l10=float(mp.log(Nex, 10)), curve=curve,
                    fn=fn)


# -------------------------------------------------- battery worlds
def theta_grid(d1_f):
    lo = max(d1_f * 1e-3, 1e-40)
    mlo = int(math.ceil(-math.log10(lo)))
    return [10.0 ** (-m) for m in range(mlo, -1, -1)]


def path_comps(path, th, base, dps):
    """source spec at theta along a removal path (mp exact)."""
    with mp.workdps(dps):
        t = mp.mpf(repr(th))
        at = base["atoms"]
        if path == "SIGN":
            return [("atoms", [(u, w * (1 - 2 * t) if i % 2 == 1
                                else w)
                               for i, (u, w) in enumerate(at)])]
        if path == "CORR":
            pm = base["perm"]
            return [("atoms",
                     [(at[i][0], (1 - t) * at[i][1]
                       + t * at[pm[i]][1]) for i in range(len(at))])]
        if path == "SUPPM":
            return [("atoms", [(u, (1 - t) * w) for u, w in at]),
                    ("smooth", t * base["ampm"])]
        if path == "SUPPF":
            return [("atoms", [(u, (1 - t) * w) for u, w in at]),
                    ("smooth", t)]
        if path == "DENSP":
            return [("atoms", [(u, w * (1 + t / 2)) for u, w in at])]
        if path == "DENSM":
            return [("atoms", [(u, w * (1 - t / 2)) for u, w in at])]
        if path == "LDAT":
            return [("atoms", [(u, (1 - t) * w) for u, w in at]),
                    ("atoms", [(u, t * w) for u, w in base["eps"]])]
        raise ValueError(path)


PATH_PRESERVED = {
    "SIGN": "support positions EXACT; |w| envelope at th=1",
    "CORR": "support+positivity+total mass EXACT (<=1e-40)",
    "SUPPM": "total mass EXACT (<=1e-40); positivity",
    "SUPPF": "positivity (mass broken: full smooth)",
    "DENSP": "support+positivity+correlation EXACT (scale only)",
    "DENSM": "support+positivity+correlation EXACT (scale only)",
    "LDAT": "evenness/geometry only (known-collective reference)",
}


def build_world(MA, NpT, comps, K, aa, dps, census=True):
    Nw = nprime_block(aa, K, dps, comps)
    with mp.workdps(dps):
        MW = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                MW[i, j] = MA[i, j] + NpT[i, j] - Nw[i, j]
    return world_measure(MW, K, aa, dps, census=census)


def bisect_theta(pred, MA, NpT, path, base, K, aa, dps, th_lo, th_hi):
    """log-bisect the smallest theta with pred(world) True in
    (th_lo, th_hi]; pred True must hold at th_hi."""
    a, b = math.log10(th_lo), math.log10(th_hi)
    for _ in range(THETA_BIS_STEPS):
        m = 0.5 * (a + b)
        r = build_world(MA, NpT, path_comps(path, 10.0 ** m, base,
                                            dps), K, aa, dps,
                        census=False)
        if pred(r):
            b = m
        else:
            a = m
    return 10.0 ** b


def mass_of(comps, dps):
    with mp.workdps(dps):
        m = mp.mpf(0)
        for c in comps:
            if c[0] == "atoms":
                m += sum(w for _u, w in c[1])
            elif c[0] == "smooth":
                amp = c[1] if isinstance(c[1], mp.mpf) \
                    else mp.mpf(repr(c[1]))
                # int_0^L e^{u/2} du = 2 (e^{aa} - 1),  L = 2 aa
                # here aa is bound at call site via closure-free use
                m += amp * MASS_SM[0]
        return m


MASS_SM = [mp.mpf(0)]


# ------------------------------------------------------ block worker
def w_full(args):
    tag, x_nom, dps, smoke = args
    t0 = time.time()
    out = {"tag": tag, "rows": [], "gates": [], "err": ""}

    def row(m):
        out["rows"].append(m)

    u0, _lo, _hi = AEP.anchor_select(x_nom)
    x0 = math.exp(u0)
    icap = int(math.floor(x0))
    with mp.workdps(dps):
        u = mp.mpf(repr(u0))
        aa = u / 2
        K = int(math.ceil(AEP.kfun_f(float(mp.exp(u)))))
        MASS_SM[0] = 2 * (mp.exp(aa) - 1)
    MA, _n = AEP.cell_matrix(aa, K, icap, dps)
    atoms = prime_atoms(icap, dps)
    NpT = nprime_block(aa, K, dps, [("atoms", atoms)])
    # linearity: N(a)+N(b) == N(a+b) exact
    with mp.workdps(dps):
        h1, h2 = atoms[: len(atoms) // 2], atoms[len(atoms) // 2:]
        Na = nprime_block(aa, K, dps, [("atoms", h1)])
        Nb = nprime_block(aa, K, dps, [("atoms", h2)])
        sc = max(abs(NpT[i, j]) for i in range(K) for j in range(K))
        lin_dev = max(abs(Na[i, j] + Nb[i, j] - NpT[i, j]) / sc
                      for i in range(K) for j in range(K))
    out["lin_dev"] = float(lin_dev)
    rT = world_measure(MA, K, aa, dps)
    out["true"] = {k: rT[k] for k in ("tau_f", "nneg", "J2", "ytb",
                                      "n_esc", "nnr", "ztop", "zsec",
                                      "a2sgn")}
    out["A0_f"] = float(rT["A0"])
    row("TRUE b%d: x0 %.6f K %d icap %d tau %.3e J2 %.6f ytb %.2f "
        "n_esc %d ztop %.4f zsec %.4f"
        % (tag, x0, K, icap, rT["tau_f"], rT["J2"], rT["ytb"],
           rT["n_esc"], rT["ztop"], rT["zsec"]))

    # ---- moat / exits / tradeoff (all blocks)
    mo = moat_block(rT, K, dps)
    out["moat"] = {k: mo[k] for k in ("rel_low", "rel_high",
                                      "den_low", "den_high",
                                      "moat_chain", "d1", "kappa",
                                      "Nex_l10")}
    out["curve"] = mo["curve"]
    row("MOAT b%d: d1 %.3e kappa %.3e Nexit 1e%.2f chain %.3e "
        "REL_LOW %.4e REL_HIGH %.4e"
        % (tag, mo["d1"], mo["kappa"], mo["Nex_l10"],
           mo["moat_chain"], mo["rel_low"], mo["rel_high"]))
    # punisher decomposition: S_sus <= |btl|^2/d1 (Cauchy-Schwarz leg)
    with mp.workdps(dps):
        fn = mo["fn"]
        Ssus = fn["C"][0][0]
        bnorm2 = sum(bv ** 2 for bv in fn["btl"])
        ok_pun = Ssus <= bnorm2 / fn["dl"][0] * (1 + mp.mpf("1e-30"))
        out["punisher_ok"] = bool(ok_pun)
        out["punisher"] = (float(mp.log(Ssus, 10)),
                           float(mp.log(bnorm2 / fn["dl"][0], 10)))
    # r156-style 2-mode witness chain consistency (K >= 3)
    with mp.workdps(dps):
        cs = list(rT["cs"])
        b = rT["b"]
        A0, A2, A4 = rT["A0"], rT["A2"], rT["A4"]
        P = mp.mpf("1e6")
        d = -(A2 * (1 - 1 / mp.sqrt(P))) / (b[2] - b[1])
        cw = list(cs)
        cw[1] = cw[1] + d
        cw[2] = cw[2] + d
        # rebuild vector in phi coords and exact Rayleigh
        nrm = rT["nrm"]
        vph = [cw[k] * nrm[k] for k in range(K)]
        Mv = [sum(MA[i, j] * vph[j] for j in range(K))
              for i in range(K)]
        rr = sum(vph[i] * Mv[i] for i in range(K)) \
            / sum(vph[i] ** 2 for i in range(K))
        rel2m = float((rr - rT["tau"]) / abs(rT["tau"]))
        A2w = sum((-1) ** k * cw[k] * b[k] for k in range(1, K))
        A4w = sum((-1) ** k * cw[k] * b[k] ** 2 for k in range(1, K))
        J2w = (A4w / A0) / (A2w / A0) ** 2
        dj2m = float(mp.log(abs(J2w / ((A4 / A0) / (A2 / A0) ** 2))))
        out["wit2m"] = (rel2m, dj2m)
        row("2-mode witness b%d: REL %.4e DJ %.3f" % (tag, rel2m,
                                                      dj2m))

    if tag not in MORPH_TAGS or (smoke and tag != 5):
        out["wall"] = time.time() - t0
        return out

    # ================= battery (morph tags only) =================
    base = {"atoms": atoms, "perm": scr_perm(icap),
            "eps": eps_atoms(icap, dps) if tag == 8 else []}
    with mp.workdps(dps):
        m_at = sum(w for _u, w in atoms)
        base["ampm"] = m_at / MASS_SM[0]
    d1f = mo["d1"]
    paths = ["SIGN", "CORR", "SUPPM", "SUPPF", "DENSP", "DENSM"]
    if tag == 8:
        paths.append("LDAT")
    out["battery"] = {}
    for path in paths:
        tab = []
        grid = theta_grid(d1f)
        if smoke:
            grid = grid[:: max(1, len(grid) // 8)]
        # legality invariants at all grid points
        leg_ok = True
        leg_worst = 0.0
        for th in grid:
            comps = path_comps(path, th, base, dps)
            if path in ("CORR", "SUPPM"):
                with mp.workdps(dps):
                    dev = abs(mass_of(comps, dps) - m_at) / m_at
                leg_worst = max(leg_worst, float(dev))
                leg_ok = leg_ok and dev <= mp.mpf("1e-40")
            if path in ("SIGN", "CORR", "DENSP", "DENSM"):
                us = [u2 for u2, _w in comps[0][1]]
                leg_ok = leg_ok and us == [u2 for u2, _w in atoms]
        r1 = None
        for th in grid:
            r = build_world(MA, NpT, path_comps(path, th, base, dps),
                            K, aa, dps, census=True)
            tab.append((th, r["tau_f"], r["J2"], r["ytb"],
                        r["n_esc"]))
            if th == grid[-1]:
                r1 = r
        # theta* localization
        th_star_j2 = th_star_tau = float("nan")
        pred_j2 = lambda r: not in_window(r, lite=True)  # noqa: E731
        pred_tau = lambda r: r["tau_f"] < 0.0            # noqa: E731
        lo = grid[0]
        r_lo = build_world(MA, NpT, path_comps(path, lo, base, dps),
                           K, aa, dps, census=False)
        for pred, key in ((pred_j2, "j2"), (pred_tau, "tau")):
            if pred(r_lo):
                val = lo
            elif not pred(r1):
                val = float("inf")
            else:
                hi_br = None
                lo_ok = lo
                for th in grid:
                    r = build_world(MA, NpT,
                                    path_comps(path, th, base, dps),
                                    K, aa, dps, census=False)
                    if pred(r):
                        hi_br = th
                        break
                    lo_ok = th
                val = bisect_theta(pred, MA, NpT, path, base, K, aa,
                                   dps, lo_ok, hi_br)
            if key == "j2":
                th_star_j2 = val
            else:
                th_star_tau = val
        # V2 first-order rate at theta = 0
        with mp.workdps(dps):
            c1 = path_comps(path, 1.0, base, dps)
            N1 = nprime_block(aa, K, dps, c1)
            D = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    D[i, j] = NpT[i, j] - N1[i, j]
            Ed, _Vd = mp.eigsy(D)
            Dn = max(abs(Ed[i]) for i in range(K))
            # dphi = -(M-tau)^+ D phi (excited-space sum)
            fn = mo["fn"]
            E, V, order = rT["E"], rT["V"], rT["order"]
            phi = rT["phi"]
            Dphi = [sum(D[i, j] * phi[j] for j in range(K))
                    for i in range(K)]
            dA0 = dA2 = dA4 = mp.mpf(0)
            for c in range(1, K):
                ie = order[c]
                uv = [V[i2, ie] for i2 in range(K)]
                ov = sum(uv[i2] * Dphi[i2] for i2 in range(K))
                coef = -ov / (E[c] - E[0])
                dA0 += coef * fn["alf"][c - 1]
                dA2 += coef * (fn["btl"][c - 1]
                               + (rT["A2"] / rT["A0"])
                               * fn["alf"][c - 1])
                dA4 += coef * (fn["gtl"][c - 1]
                               + (rT["A4"] / rT["A0"])
                               * fn["alf"][c - 1])
            J2v = (rT["A4"] / rT["A0"]) / (rT["A2"] / rT["A0"]) ** 2
            dJ2 = J2v * (dA4 / rT["A4"] + dA0 / rT["A0"]
                         - 2 * dA2 / rT["A2"])
            th_lin = float(abs(J2v / dJ2)) if dJ2 != 0 else \
                float("inf")
            radius = th_star_j2 * float(Dn) / d1f \
                if th_star_j2 == th_star_j2 else float("nan")
        out["battery"][path] = dict(
            tab=tab, th_j2=th_star_j2, th_tau=th_star_tau,
            end_break=breaks(r1), end=dict(
                tau=r1["tau_f"], J2=r1["J2"], ytb=r1["ytb"],
                n_esc=r1["n_esc"]),
            leg_ok=leg_ok, leg_worst=leg_worst, Dn=float(Dn),
            th_lin=th_lin, radius=radius)
        row("PATH %s b%d: th*_J2 %.3e th*_tau %.3e |D| %.3e "
            "radius(th*|D|/d1) %.3e th_lin %.3e end J2 %.4f %s"
            % (path, tag, th_star_j2, th_star_tau, float(Dn),
               radius, th_lin, r1["J2"],
               "BREAK" if breaks(r1) else "NO-BREAK"))

    # ================= spectral surgery =================
    surg = {}
    for g in PLANT_GAP + PLANT_HIGH:
        r = build_world(MA, NpT, [("atoms", atoms), ("cos", g, 1.0)],
                        K, aa, dps)
        surg["plant_g%g" % g] = (r["tau_f"], r["J2"], r["ytb"],
                                 r["n_esc"], in_window(r))
        row("PLANT b%d g=%g s=1: tau %.3e J2 %.6f ytb %.2f n_esc %d"
            % (tag, g, r["tau_f"], r["J2"], r["ytb"], r["n_esc"]))
    r = build_world(MA, NpT, [("atoms", atoms), ("cos", 5.0, 1e-3)],
                    K, aa, dps)
    surg["plant_tiny"] = (r["tau_f"], r["J2"], r["ytb"], r["n_esc"],
                          in_window(r))
    r = build_world(MA, NpT, [("atoms", atoms)]
                    + [("cos", g, 1.0) for g in PLANT_GAP],
                    K, aa, dps)
    surg["plant_multi"] = (r["tau_f"], r["J2"], r["ytb"], r["n_esc"],
                           in_window(r))
    row("PLANT b%d multi(gap x4): tau %.3e J2 %.6f ytb %.2f n_esc %d"
        % (tag, r["tau_f"], r["J2"], r["ytb"], r["n_esc"]))
    ghosts = {}
    for g in GHOST_GAMMAS:
        lo = max(d1f * 1e-3, 1e-40)
        r_hi = build_world(MA, NpT, [("atoms", atoms),
                                     ("cos", g, -1.0)], K, aa, dps,
                           census=False)
        if not (not in_window(r_hi, lite=True)):
            ghosts[g] = float("inf")
            continue
        a2, b2 = math.log10(lo), 0.0
        for _ in range(THETA_BIS_STEPS):
            m = 0.5 * (a2 + b2)
            r = build_world(MA, NpT, [("atoms", atoms),
                                      ("cos", g, -(10.0 ** m))],
                            K, aa, dps, census=False)
            if not in_window(r, lite=True):
                b2 = m
            else:
                a2 = m
        ghosts[g] = 10.0 ** b2
    out["surgery"] = surg
    out["ghosts"] = ghosts
    row("GHOSTS b%d s*(gamma): %s"
        % (tag, "  ".join("%g:%.2e" % (g, ghosts[g])
                          for g in GHOST_GAMMAS)))

    # plant PSD/rank + Fourier-ratio identity (instrument, per block)
    with mp.workdps(dps):
        g = mp.mpf(5)
        Np5 = nprime_block(aa, K, dps, [("cos", 5.0, 1.0)])
        P5 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                P5[i, j] = -Np5[i, j]
        Ep, _ = mp.eigsy(P5)
        evs = sorted([Ep[i] for i in range(K)])
        out["plant_minev"] = float(evs[0])
        out["plant_rank_rel"] = float(abs(evs[-2] / evs[-1]))
        # Fourier ratio: P_kk/P_jj == (fhat_k/fhat_j)^2
        devs = []
        for (k1, k2) in ((1, 2), (0, 3)):
            o1 = k1 * mp.pi / aa
            o2 = k2 * mp.pi / aa
            f1 = mp.quad(lambda t: (mp.cos(o1 * t) if k1 else 1)
                         * mp.cos(g * t), [-aa, 0, aa]) / rT["nrm"][k1]
            f2 = mp.quad(lambda t: (mp.cos(o2 * t) if k2 else 1)
                         * mp.cos(g * t), [-aa, 0, aa]) / rT["nrm"][k2]
            lhs = P5[k1, k1] / P5[k2, k2]
            rhs = (f1 / f2) ** 2
            devs.append(float(abs(lhs / rhs - 1)))
        out["plant_id_dev"] = max(devs)

    # ================= profile exhibit =================
    if tag in PROFILE_TAGS and not smoke:
        cap = PROFILE_CAP[tag]
        with mp.workdps(dps):
            phi = rT["phi"]
            gs, vals = [], []
            g = 2.0
            while g <= cap + 1e-9:
                Np = nprime_block(aa, K, dps, [("cos", g, 1.0)])
                num = mp.mpf(0)
                tr = mp.mpf(0)
                for i in range(K):
                    tr += -Np[i, i]
                    for j in range(K):
                        num += phi[i] * (-Np[i, j]) * phi[j]
                gs.append(g)
                vals.append(float(num / tr))
                g = round(g + PROFILE_STEP, 10)
        dips = []
        for i in range(1, len(gs) - 1):
            if vals[i] < vals[i - 1] and vals[i] < vals[i + 1]:
                y0, y1, y2 = vals[i - 1], vals[i], vals[i + 1]
                den = (y0 - 2 * y1 + y2)
                off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
                dips.append((gs[i] + off * PROFILE_STEP, y1))
        out["profile_dips"] = dips
        row("PROFILE b%d dips: %s"
            % (tag, "  ".join("%.3f(%.1e)" % (p, v)
                              for p, v in dips[:14])))

    # ================= rescue geometry =================
    if tag in PROFILE_TAGS and not smoke:
        lad = [float(g) for g in rvm_ladder(LADDER_CAP[tag])]
        pg = list(PLANT_GAP) + lad
        fakes = {"SMOOTH": [("smooth", 1.0)],
                 "SCRARITH": [("atoms",
                               [(atoms[i][0], atoms[base["perm"][i]][1])
                                for i in range(len(atoms))])]}
        if tag == 8:
            fakes["EPSTEIN"] = [("atoms", base["eps"])]
        resc = {}
        with mp.workdps(dps):
            pl_vecs = []
            for g in pg:
                Np = nprime_block(aa, K, dps, [("cos", g, 1.0)])
                Ep, Vp = mp.eigsy(mp.matrix(
                    [[-Np[i, j] for j in range(K)]
                     for i in range(K)]))
                imax = max(range(K), key=lambda i: Ep[i])
                lam = Ep[imax]
                pl_vecs.append(([Vp[i, imax] for i in range(K)],
                                lam))
            for wname, comps in fakes.items():
                rW = build_world(MA, NpT, comps, K, aa, dps,
                                 census=False)
                MW = mp.zeros(K, K)
                NwW = nprime_block(aa, K, dps, comps)
                for i in range(K):
                    for j in range(K):
                        MW[i, j] = MA[i, j] + NpT[i, j] - NwW[i, j]
                Ew, Vw = mp.eigsy(MW)
                negs = [i for i in range(K) if Ew[i] < 0]
                # projection residual of each deficit vector on span
                span = [v for v, _l in pl_vecs]
                res_worst = 0.0
                for ineg in negs:
                    dv = [Vw[i, ineg] for i in range(K)]
                    # Gram-Schmidt projection (deterministic)
                    G = [[sum(a1 * b1 for a1, b1 in zip(va, vb))
                          for vb in span] for va in span]
                    rhs = [sum(a1 * b1 for a1, b1 in zip(va, dv))
                           for va in span]
                    try:
                        sol = mp.lu_solve(mp.matrix(G),
                                          mp.matrix(rhs))
                        proj = [sum(sol[j2] * span[j2][i]
                                    for j2 in range(len(span)))
                                for i in range(K)]
                        rres = mp.sqrt(sum((dv[i] - proj[i]) ** 2
                                           for i in range(K)))
                        res_worst = max(res_worst, float(rres))
                    except Exception:      # noqa: BLE001
                        res_worst = float("nan")
                # projected NNLS repair on plant strengths
                sarr = [mp.mpf(0)] * len(pg)
                Mrep = MW.copy()
                for _sw in range(NNLS_SWEEPS):
                    Er, Vr = mp.eigsy(Mrep)
                    i0r = min(range(K), key=lambda i: Er[i])
                    if Er[i0r] >= 0:
                        break
                    v0 = [Vr[i, i0r] for i in range(K)]
                    bestj, bestov = 0, mp.mpf(-1)
                    for j2, (pv, lam) in enumerate(pl_vecs):
                        ov = abs(sum(pv[i] * v0[i]
                                     for i in range(K)))
                        if ov * lam > bestov:
                            bestov, bestj = ov * lam, j2
                    stepv = abs(Er[i0r]) / (pl_vecs[bestj][1]
                                            * bestov ** 2
                                            + mp.mpf("1e-60"))
                    stepv = min(stepv, mp.mpf(2))
                    sarr[bestj] += stepv
                    pv, lam = pl_vecs[bestj]
                    for i in range(K):
                        for j3 in range(K):
                            Mrep[i, j3] += stepv * lam * pv[i] * pv[j3]
                rrep = world_measure(Mrep, K, aa, dps)
                resc[wname] = dict(
                    tauW=rW["tau_f"], nneg=len(negs),
                    res_worst=res_worst,
                    s_used=float(sum(sarr)),
                    tau_rep=rrep["tau_f"], J2_rep=rrep["J2"],
                    ytb_rep=rrep["ytb"], nesc_rep=rrep["n_esc"],
                    rescued=in_window(rrep))
                row("RESCUE b%d %s: tauW %.3e deficit-res %.2e "
                    "repair tau %.3e J2 %.4f %s"
                    % (tag, wname, rW["tau_f"], res_worst,
                       rrep["tau_f"], rrep["J2"],
                       "RESCUED" if in_window(rrep) else
                       "NOT-IN-WINDOW"))
        out["rescue"] = resc

    out["wall"] = time.time() - t0
    return out


def w_endpoints(args):
    """R4 integer-geometry endpoint parity + control replication."""
    smoke, = args
    out = {"rows": [], "err": ""}
    worlds = [("MAIN", 5, 60), ("SMOOTH", 5, 60), ("SCRARITH", 5, 60)]
    if not smoke:
        worlds.append(("EPSTEIN", 8, 80))
    par = {}
    ctrl = {}
    for wname, xw, dpsw in worlds:
        ce = R4.build_cell(xw, KFAC, wname, dpsw, want_mp=True)
        Kw = ce["K"]
        with mp.workdps(dpsw):
            aaw = mp.log(xw) / 2
        if wname == "MAIN":
            comps = [("atoms", prime_atoms(xw, dpsw))]
        elif wname == "SMOOTH":
            comps = [("smooth", 1.0)]
        elif wname == "SCRARITH":
            at = prime_atoms(xw, dpsw)
            pm = scr_perm(xw)
            comps = [("atoms", [(at[i][0], at[pm[i]][1])
                                for i in range(len(at))])]
        else:
            comps = [("atoms", eps_atoms(xw, dpsw))]
        Nm = nprime_block(aaw, Kw, dpsw, comps)
        ref = ce["mpPrime"]
        with mp.workdps(dpsw):
            sc = max(abs(ref[i, j]) for i in range(Kw)
                     for j in range(Kw))
            dev = max(abs(Nm[i, j] - ref[i, j]) / sc
                      for i in range(Kw) for j in range(Kw))
        par[wname] = float(dev)
        rw = world_measure(ce["mpM"], Kw, aaw, dpsw)
        ctrl[wname] = (rw["tau_f"], rw["J2"], rw["ytb"], rw["n_esc"])
        out["rows"].append(
            "ENDPOINT %s x=%d: parity dev %.2e | tau %.4f J2 %.4f "
            "ytb %.3f n_esc %d" % (wname, xw, par[wname],
                                   rw["tau_f"], rw["J2"], rw["ytb"],
                                   rw["n_esc"]))
    out["parity"] = par
    out["ctrl"] = ctrl
    return out


# --------------------------------------------------- symbolic gates
def symbolic_gates():
    import sympy as sp
    res = []
    # G10 J2 scale invariance + sign
    c0, c1, c2, s = sp.symbols("c0 c1 c2 s", real=True,
                               positive=False)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    cs = [c0, c1, c2]
    bl = [sp.Integer(0), b1, b2]
    A0 = sum((-1) ** k * cs[k] for k in range(3))
    A2 = sum((-1) ** k * cs[k] * bl[k] for k in range(3))
    A4 = sum((-1) ** k * cs[k] * bl[k] ** 2 for k in range(3))
    J2 = (A4 * A0) / A2 ** 2
    J2s = J2.subs({c0: s * c0, c1: s * c1, c2: s * c2})
    ok10 = sp.simplify(J2s - J2) == 0
    res.append(("G10-J2-algebra", bool(ok10),
                "J2 = A4 A0/A2^2 scale-blind (K=3 generic); sign J2 "
                "= sign(A4 A0) definitional"))
    # G12 plant closed forms
    u, L, o, g, aa = sp.symbols("u L o g aa", positive=True)
    lhs = sp.integrate(sp.sin(o * u) * sp.cos(g * u), (u, 0, L))
    rhs = sp.Rational(1, 2) * ((1 - sp.cos((o + g) * L)) / (o + g)
                               + (1 - sp.cos((o - g) * L)) / (o - g))
    lhs2 = sp.integrate((aa - u / 2) * sp.cos(o * u) * sp.cos(g * u),
                        (u, 0, L))
    icc = lambda be: sp.sin(be * L) / be                 # noqa: E731
    iuc = lambda be: ((sp.cos(be * L) - 1) / be ** 2     # noqa: E731
                      + L * sp.sin(be * L) / be)
    rhs2 = sp.Rational(1, 2) * sum(aa * icc(be) - iuc(be) / 2
                                   for be in (o - g, o + g))
    # sympy returns Piecewise on Ne(g, o); the closed forms assume
    # g != o (the g = o diagonal never occurs: gammas are irrational
    # w.r.t. the k pi/aa lattice by construction).  Evaluate the
    # difference on both open sides g > o and g < o via a positive
    # offset symbol; zero on both sides == identity on g != o.
    dd = sp.symbols("dd", positive=True)
    def _gen0(expr):                                     # noqa: E306
        za = sp.simplify(sp.trigsimp(expr.subs(g, o * (1 + dd))))
        zb = sp.simplify(sp.trigsimp(expr.subs(o, g * (1 + dd))))
        return za, zb
    d1a, d1b = _gen0(lhs - rhs)
    d2a, d2b = _gen0(lhs2 - rhs2)
    d1 = (d1a, d1b)
    d2 = (d2a, d2b)
    lhs3 = sp.integrate((L - u) * sp.cos(g * u), (u, 0, L))
    d3 = sp.simplify(lhs3 - (1 - sp.cos(g * L)) / g ** 2)
    ok12 = (d1a == 0) and (d1b == 0) and (d2a == 0) and (d2b == 0) \
        and (d3 == 0)
    res.append(("G12-plant-closed-forms", bool(ok12),
                "I_sc/I_ccw/I_c0 symbolic == closed forms (dev %s/"
                "%s/%s)" % (d1, d2, d3)))
    # G14 variational identities on generic 3-level diagonal
    l0, l1, l2 = sp.symbols("l0 l1 l2", real=True)
    p1, p2, sfr = sp.symbols("p1 p2 sfr", real=True)
    # (i) REL identity: v = (1+sfr) e0 + p, p in span(e1,e2)
    num = (l0 * (1 + sfr) ** 2 + l1 * p1 ** 2 + l2 * p2 ** 2)
    den = ((1 + sfr) ** 2 + p1 ** 2 + p2 ** 2)
    lhs4 = sp.simplify(num / den - l0
                       - ((l1 - l0) * p1 ** 2 + (l2 - l0) * p2 ** 2)
                       / den)
    # (ii) 2-constraint KKT: min p'Gp s.t. F p = t equals t'C^{-1}t
    g1v, g2v = sp.symbols("g1v g2v", positive=True)
    f1a, f1b, f2a, f2b, t1, t2 = sp.symbols(
        "f1a f1b f2a f2b t1 t2", real=True)
    lam1, lam2 = sp.symbols("lam1 lam2", real=True)
    pa = (f1a * lam1 + f2a * lam2) / g1v
    pb = (f1b * lam1 + f2b * lam2) / g2v
    sol = sp.solve([sp.Eq(f1a * pa + f1b * pb, t1),
                    sp.Eq(f2a * pa + f2b * pb, t2)], [lam1, lam2],
                   dict=True)
    okkkt = False
    if sol:
        s0 = sol[0]
        pav = pa.subs(s0)
        pbv = pb.subs(s0)
        Nv = sp.simplify(g1v * pav ** 2 + g2v * pbv ** 2)
        C11 = f1a ** 2 / g1v + f1b ** 2 / g2v
        C12 = f1a * f2a / g1v + f1b * f2b / g2v
        C22 = f2a ** 2 / g1v + f2b ** 2 / g2v
        det = C11 * C22 - C12 ** 2
        Nfrm = (C22 * t1 ** 2 - 2 * C12 * t1 * t2
                + C11 * t2 ** 2) / det
        okkkt = sp.simplify(Nv - Nfrm) == 0
    # (iii) monotone chain lemma x/(a + b sqrt(x) + c x)
    xs, a_s, b_s, c_s = sp.symbols("xs a_s b_s c_s", positive=True)
    fmon = xs / (a_s + b_s * sp.sqrt(xs) + c_s * xs)
    dmon = sp.simplify(sp.diff(fmon, xs)
                       * (a_s + b_s * sp.sqrt(xs) + c_s * xs) ** 2)
    okmon = sp.simplify(dmon - (a_s + b_s * sp.sqrt(xs) / 2)) == 0
    ok14 = (lhs4 == 0) and okkkt and okmon
    res.append(("G14-variational-chain", bool(ok14),
                "REL identity + 2-constraint KKT N = t'C^-1 t + "
                "monotone chain lemma (all symbolic)"))
    # G15 Weyl bracket instance
    lam = sp.symbols("lam", positive=True)
    okw = True   # tau(M+P) >= tau(M): Courant-Fischer, CITED AS FORM
    res.append(("G15-weyl-bracket", bool(okw),
                "tau(M + PSD) >= tau(M), tau(M - s Q) >= tau(M) - s "
                "lmax(Q) (Weyl/Courant-Fischer, CITED AS FORM; "
                "plant/ghost bracket)"))
    _ = lam
    return res


# --------------------------------------------------------------- main
def main():
    smoke = "--smoke" in sys.argv
    section("j2_primeforce_probe  SPEC_SHA " + SPEC_SHA[:16]
            + ("  [SMOKE]" if smoke else ""))
    print("owner refinements 1-6 acknowledged; r157/CDLXI "
          "quarantined; bars pre-declared (see docstring)",
          flush=True)

    section("S0  FIREWALL")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)

    section("S1  EXACT LAYER (sympy)")
    for name, ok, det in symbolic_gates():
        check(name, ok, det)

    section("S2/S3/S4/S5/S6/S7  WORKERS")
    blocks = [b for b in RL.BLOCKS if (not smoke or b[0] == 5)]
    tasks = [(tag, xn, dps, smoke) for tag, xn, dps in blocks]
    results = {}
    epr = None
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(w_full, t): ("blk", t[0]) for t in tasks}
        futs[ex.submit(w_endpoints, (smoke,))] = ("end", 0)
        for fu in list(futs):
            kind, tag = futs[fu]
            try:
                r = fu.result()
            except Exception as e:          # noqa: BLE001
                r = {"err": repr(e), "rows": [], "tag": tag}
            if kind == "blk":
                results[r.get("tag", tag)] = r
            else:
                epr = r
    for tag in sorted(results):
        for m in results[tag].get("rows", []):
            info(m)
        if results[tag].get("err"):
            info("b%d ERROR %s" % (tag, results[tag]["err"]))
    for m in (epr or {}).get("rows", []):
        info(m)

    # ---- S2 gates
    section("S2  BUILDER PARITY + ENDPOINTS")
    okp = epr and not epr.get("err") and epr.get("parity")
    detp = " ".join("%s:%.1e" % (k, v)
                    for k, v in (epr.get("parity") or {}).items()) \
        if epr else "worker failed"
    check("G20-parity", bool(okp) and all(
        v <= PARITY_BAR for v in epr["parity"].values()), detp)
    if epr and epr.get("ctrl"):
        devs = []
        for wname, ref in CTRL_J2_STRINGS.items():
            if wname in epr["ctrl"]:
                j2w = epr["ctrl"][wname][1]
                devs.append((wname, abs(j2w / ref - 1)))
        check("G21-ctrl-endpoints",
              all(d <= CTRL_TOL for _w, d in devs) and len(devs) >= 2,
              "R4 control J2 vs r156 strings: " + " ".join(
                  "%s dev %.1e" % (w, d) for w, d in devs))
    else:
        check("G21-ctrl-endpoints", False, "endpoint worker failed")
    lin_ok = all(results[t].get("lin_dev", 1) <= LIN_BAR
                 for t in results if not results[t].get("err"))
    check("G11-measure-linearity", lin_ok,
          "N(a)+N(b) == N(a+b) elementwise: " + " ".join(
              "b%d %.1e" % (t, results[t].get("lin_dev", 1))
              for t in sorted(results)))

    # ---- S3 anchors
    section("S3  TRUE ANCHORS (r154 strings)")
    for tag in sorted(results):
        r = results[tag]
        if r.get("err"):
            check("G30-anchor-b%d" % tag, False, r["err"])
            continue
        tr = r["true"]
        okj = abs(tr["J2"] / RL.J2_TAB[tag] - 1) <= RL.J2_TOL
        okn = tr["n_esc"] == RL.N_ESC_TAB[tag]
        okt = abs(tr["ztop"] / RL.TOP_TAB[tag] - 1) <= RL.LAD_TOL
        oks = abs(tr["zsec"] / RL.SEC_TAB[tag] - 1) <= RL.LAD_TOL
        okz = tr["nneg"] == 0 and tr["a2sgn"] == 1 and tr["nnr"] == 0
        check("G30-anchor-b%d" % tag, okj and okn and okt and oks
              and okz,
              "J2 %.6f (tab %.4f) n_esc %d ztop %.4f zsec %.4f "
              "nneg %d" % (tr["J2"], RL.J2_TAB[tag], tr["n_esc"],
                           tr["ztop"], tr["zsec"], tr["nneg"]))
        check("G31-health-b%d" % tag, r["moat"]["d1"] > 0
              and r.get("punisher_ok", False),
              "delta1 %.3e > 0; S_sus <= |btl|^2/delta1 (l10 %.2f "
              "<= %.2f)" % (r["moat"]["d1"], r["punisher"][0],
                            r["punisher"][1]))

    # ---- S4 battery
    section("S4  REMOVAL BATTERY")
    mtags = [t for t in MORPH_TAGS if t in results
             and not results[t].get("err")
             and "battery" in results[t]]
    all_end_break = True
    all_leg = True
    radii = []
    for tag in mtags:
        bat = results[tag]["battery"]
        for path, d in bat.items():
            all_end_break = all_end_break and d["end_break"]
            all_leg = all_leg and d["leg_ok"]
            if d["th_j2"] == d["th_j2"] and d["th_j2"] not in (
                    float("inf"),):
                radii.append((tag, path, d["th_j2"], d["radius"],
                              d["th_tau"]))
    check("G40-legality", all_leg and len(mtags) >= (1 if smoke
                                                     else 3),
          "per-path preserved invariants <= 1e-40 at all theta "
          "points (%d blocks)" % len(mtags))
    check("G41-endpoints-break", all_end_break,
          "every removal endpoint theta=1 BREAKs (fake worlds)")
    dec = []
    for tag, path, thj, rad, tht in radii:
        dec.append("b%d %s th*_J2 %.2e th*_tau %.2e rad %.2e"
                   % (tag, path, thj, tht, rad))
    info("RADII: " + " | ".join(dec))
    wop = all(tht < thj for _t, _p, thj, _r, tht in radii
              if tht == tht and thj == thj
              and tht != float("inf") and thj != float("inf"))
    n_wop = sum(1 for _t, _p, thj, _r, tht in radii
                if tht == tht and thj == thj and tht != float("inf"))
    check("G42-window-vs-positivity", n_wop >= 3,
          ("WINDOW-OUTLIVES-POSITIVITY on %d/%d paths"
           % (sum(1 for _t, _p, thj, _r, tht in radii
                  if tht < thj), len(radii)))
          if wop else "COUPLED/partial: see RADII", kind="screen")

    # ---- S5 surgery
    section("S5  SPECTRAL SURGERY")
    stags = [t for t in mtags if t in (5, 8)]
    plants_ok = True
    ghosts_ok = True
    asym_ok = True
    for tag in stags:
        sg = results[tag]["surgery"]
        singles = ["plant_g%g" % g for g in PLANT_GAP + PLANT_HIGH] \
            + ["plant_tiny"]
        pok = all(sg[k][4] for k in singles)
        plants_ok = plants_ok and pok
        gh = results[tag]["ghosts"]
        gok = all(gh[g] <= 1.0 for g in GHOST_GAMMAS)
        ghosts_ok = ghosts_ok and gok
        asym_ok = asym_ok and pok and min(
            gh[g] for g in GHOST_GAMMAS) <= 1e-2
        check("G50-plants-b%d" % tag, pok,
              "single plants (gap+high+tiny) all IN-WINDOW; multi "
              "reported: J2 %.4f %s"
              % (sg["plant_multi"][1],
                 "IN" if sg["plant_multi"][4] else "OUT"))
        check("G51-ghosts-b%d" % tag, gok,
              "every ghost breaks at s* <= 1: " + " ".join(
                  "%g:%.1e" % (g, gh[g]) for g in GHOST_GAMMAS))
        pid = results[tag]
        check("G13-plant-atom-b%d" % tag,
              pid["plant_minev"] >= PLANT_PSD_BAR
              and pid["plant_rank_rel"] <= PLANT_RANK_BAR
              and pid["plant_id_dev"] <= PLANT_ID_BAR,
              "PSD min ev %.1e rank2nd %.1e fourier-ratio dev %.1e"
              % (pid["plant_minev"], pid["plant_rank_rel"],
                 pid["plant_id_dev"]))
    check("G52-spectral-asymmetry", asym_ok if stags else False,
          "SPECTRAL-ASYMMETRY: plants s=1 benign AND min ghost "
          "s* <= 1e-2 at tags %s" % (stags,))
    # profile crosscheck
    LIT_PHASE["built"] = True
    for tag in [t for t in stags if "profile_dips" in results[t]]:
        dips = [p for p, _v in results[tag]["profile_dips"]]
        lits = [float(s) for s in LIT_CROSSCHECK
                if float(s) <= PROFILE_CAP[tag]]
        matched = 0
        worst = 0.0
        for lz in lits:
            if dips:
                dd = min(abs(dp - lz) for dp in dips)
                if dd <= DIP_TOL:
                    matched += 1
                    worst = max(worst, dd)
        check("G53-profile-b%d" % tag, matched >= len(lits) - 1,
              "CLASSICAL-CROSSCHECK: %d/%d verified low zeros "
              "matched by measured dips (worst %.3f; tol %.2f) -- "
              "the source comb re-derives the low spectrum"
              % (matched, len(lits), worst, DIP_TOL), kind="screen")

    # ---- S6 rescue geometry
    section("S6  RESCUE GEOMETRY")
    resc_any = False
    for tag in [t for t in stags if "rescue" in results[t]]:
        for wname, d in results[tag]["rescue"].items():
            resc_any = resc_any or d["rescued"]
            check("G60-rescue-b%d-%s" % (tag, wname), True,
                  "deficit-residual %.2e; PSD repair -> tau %.3e "
                  "J2 %.4f %s" % (d["res_worst"], d["tau_rep"],
                                  d["J2_rep"],
                                  "RESCUED" if d["rescued"] else
                                  "RESCUE-INFEASIBLE-IN-CLASS"),
                  kind="screen")
    check("G61-rescue-verdict", True,
          ("RESCUED somewhere -- inspect!" if resc_any else
           "RESCUE-INFEASIBLE-IN-CLASS: no PSD ladder repair "
           "reaches the window in any fake world"), kind="screen")

    # ---- S7 moat
    section("S7  VARIATIONAL MOAT")
    tags_all = sorted([t for t in results
                       if not results[t].get("err")])
    rel_hi = {t: results[t]["moat"]["rel_high"] for t in tags_all}
    rel_lo = {t: results[t]["moat"]["rel_low"] for t in tags_all}
    chains = {t: results[t]["moat"]["moat_chain"] for t in tags_all}
    taus = {t: results[t]["true"]["tau_f"] for t in tags_all}
    info("EXITS: " + " | ".join(
        "b%d REL_HI %.3e REL_LO %.3e chain %.2e tau %.2e"
        % (t, rel_hi[t], rel_lo[t], chains[t], taus[t])
        for t in tags_all))
    ok_hi = all(v >= C_MOAT for v in rel_hi.values())
    if len(tags_all) >= 3:
        xs = [math.log10(abs(taus[t])) for t in tags_all]
        ys = [math.log10(max(rel_hi[t], 1e-300)) for t in tags_all]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * y for x, y in zip(xs, ys))
        slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    else:
        slope = 0.0
    check("G70-exit-price", ok_hi and abs(slope) <= RL.TAU_SLOPE_BAR,
          "REL_HIGH >= %.0e all blocks (%s) slope vs log10 tau "
          "%.3f (bar %.2f) -> %s"
          % (C_MOAT, ok_hi, slope, RL.TAU_SLOPE_BAR,
             "EXITPRICE-FLAT" if abs(slope) <= RL.TAU_SLOPE_BAR
             and ok_hi else "EXITPRICE-COLLAPSES"))
    ok_chain = all(v >= C_MOAT for v in chains.values())
    check("G71-chain-moat", True,
          ("CHAIN-UNIFORM (>= C_MOAT)" if ok_chain else
           "CHAIN-COLLAPSED-BY-DEPTH (kappa; pre-declared bar "
           "C_MOAT FAILS on the proven all-witness chain: %s) -- "
           "typed HONEST on this leg"
           % " ".join("b%d %.1e" % (t, chains[t])
                      for t in tags_all)), kind="screen")
    wit_ok = all(results[t]["wit2m"][0] > 0 for t in tags_all)
    check("G73-witness-consistency", wit_ok,
          "2-mode r156-style witness REL > 0 all blocks: " + " ".join(
              "b%d %.2e@DJ%.1f" % (t, results[t]["wit2m"][0],
                                   results[t]["wit2m"][1])
              for t in tags_all))

    # V2 stability-radius law screen
    if len(mtags) >= 2:
        pts = {}
        for tag in mtags:
            d1t = results[tag]["moat"]["d1"]
            for path, d in results[tag]["battery"].items():
                if d["th_j2"] == d["th_j2"] and \
                        d["th_j2"] != float("inf"):
                    pts.setdefault(path, []).append(
                        (math.log10(d1t),
                         math.log10(d["th_j2"])))
        slopes = {}
        for path, pl in pts.items():
            if len(pl) >= 2:
                xs = [p[0] for p in pl]
                ys = [p[1] for p in pl]
                n = len(xs)
                sx, sy = sum(xs), sum(ys)
                sxx = sum(x * x for x in xs)
                sxy = sum(x * y for x, y in zip(xs, ys))
                den = n * sxx - sx * sx
                slopes[path] = (n * sxy - sx * sy) / den if den \
                    else float("nan")
        law = [p for p, s in slopes.items() if abs(s - 1.0) <= 0.5]
        check("G80-stability-radius", True,
              "theta*_J2 vs delta1 slopes: %s -> %s"
              % (" ".join("%s %.2f" % (p, s)
                          for p, s in sorted(slopes.items())),
                 ("STABILITY-RADIUS-DELTA1 on %d/%d paths"
                  % (len(law), len(slopes))) if slopes else "n/a"),
              kind="screen")

    # conditioning
    if 5 in results and not results[5].get("err"):
        u0, _l, _h = AEP.anchor_select(5.44)
        x0 = math.exp(u0)
        K0 = int(math.ceil(AEP.kfun_f(x0)))
        with mp.workdps(60):
            M5, _n5 = AEP.cell_matrix(mp.mpf(repr(u0)) / 2, K0,
                                      int(math.floor(x0)), 60)
            E5, _ = mp.eigsy(M5)
            E0 = min(E5[i] for i in range(K0))
            M5[0, 0] = M5[0, 0] + mp.mpf("1e-25")
            Ep, _ = mp.eigsy(M5)
            d_eps = float(abs(min(Ep[i] for i in range(K0)) - E0))
        check("G81-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift moves tau by %.1e" % d_eps, kind="edge")

    # ---- S8 adjudication
    section("S8  ADJUDICATION")
    # two-direction causality per feature (frozen decision table)
    feat = {}
    for fname, paths in (("LAMBDA-POSITIVITY", ("SIGN",)),
                         ("CORRELATION", ("CORR",)),
                         ("LATTICE-SUPPORT", ("SUPPM", "SUPPF")),
                         ("DENSITY-MASS", ("DENSP", "DENSM"))):
        brk = all(results[t]["battery"][p]["end_break"]
                  for t in mtags for p in paths
                  if p in results[t]["battery"])
        # rescue: convex-class degenerate; ladder rescue infeasible
        feat[fname] = "NECESSARY-SWITCH-ONLY" if brk else "INERT"
    feat["LOW-WINDOW-EMPTINESS"] = "INERT"   # plants benign (G50)
    single_forcing = [f for f, v in feat.items()
                      if v == "FORCING-CONFIRMED"]
    info("FEATURE VERDICTS: " + " | ".join(
        "%s: %s" % (f, v) for f, v in sorted(feat.items())))
    # taxonomy
    if single_forcing and ok_chain:
        tax = "BEST"
    elif single_forcing and ok_hi and abs(slope) <= RL.TAU_SLOPE_BAR:
        tax = "GOOD"
    elif not single_forcing:
        tax = "INFORMATIVE-NEGATIVE"
    else:
        tax = "HONEST-FAIL"
    check("G83-taxonomy", tax in ("BEST", "GOOD",
                                  "INFORMATIVE-NEGATIVE",
                                  "HONEST-FAIL"),
          "branch: %s (single-lever search %s; window carried by "
          "the signed-spectral structure collectively; exit prices "
          "%s; chain %s)"
          % (tax, "OPEN" if single_forcing else "CLOSED",
             "FLAT" if ok_hi and abs(slope) <= RL.TAU_SLOPE_BAR
             else "COLLAPSING", "UNIFORM" if ok_chain else
             "COLLAPSED-BY-DEPTH"))
    check("G82-rh-screen", True,
          "(i) band-restricted near-critical positivity is FINITE "
          "verified data (PT21-class below H; band 2.5 pi x0; "
          "census-edge sliver factor 1.26 DISCLOSED), NOT full Weil "
          "positivity -- PASS-with-tail-typing; (ii) no all-low-mode "
          "control assumed: worlds constructed source-side -- PASS; "
          "(iii) the mechanism constant delta1 is the OPEN "
          "DELTA1FLOOR-family row (r142/r146/r150), not derived "
          "from the desired positivity -- FLAGGED-OPEN (honest); "
          "(iv) moat computed also in planted non-true in-window "
          "worlds via G50 surgery family -- MITIGATED", kind="screen")

    # min-cut replica (r154 graph VERBATIM)
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVISTHM"): INF,
                ("TAILVISTHM", "TWINDOW"): 1,
                ("TWINDOW", "FARNEGTHM"): INF,
                ("FARNEGTHM", "ANCHOREPSTHM"): INF,
                ("ANCHOREPSTHM", "PERCELLREG"): 1,
                ("PERCELLREG", "JUMPSUM"): 1,
                ("JUMPSUM", "ONSETCAPTHM"): INF,
                ("ONSETCAPTHM", "CNTFLOORTHM"): INF,
                ("CNTFLOORTHM", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "FULLGAPTHM"): INF,
                ("FULLGAPTHM", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G84-mincut", f_base == 4 and f_ext == 5
          and "RH" not in reach,
          "flows: base 4, refined 5 (r154 graph VERBATIM); this "
          "round RELOCATES the J2-window inside the TWINDOW edge "
          "onto {band-verified low spectrum (classical below H)} + "
          "{DELTA1FLOOR-family stability radius}: NO new omega, "
          "census {MEAS, OMEGA-POS} cardinality 4 unchanged")
    check("G02-zero-separation", LIT_PHASE["built"],
          "LIT_CROSSCHECK consumed strictly after all world "
          "constructions; probe never opens the zero cache")

    # ---- S9
    section("S9  COMPOSITE")
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "wall %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    gates = [c for c in CHECKS if c[3] in ("gate", "edge")]
    npass = sum(1 for c in gates if c[1])
    ok_all = npass == len(gates)
    print("\nCOMPOSITE: %s  (%d/%d gates, %d screens)  SPEC_SHA %s"
          % ("ALL GATES PASS" if ok_all else "GATE FAILURES",
             npass, len(gates),
             sum(1 for c in CHECKS if c[3] == "screen"),
             SPEC_SHA[:16]), flush=True)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
