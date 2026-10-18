#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""directional_lanczos_fullframe_probe --
PRIME.PORT.DIRECTIONAL.LANCZOS.02
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the decisive continuation of the directional-
Lanczos route CLVIII/CLIX -- is the certification depth k* bounded,
measured in a frame LARGE enough to make the question meaningful.
2026-08-11.)

THE QUESTION (frozen).  CLVIII/CLIX certified n - q >= (1/2) mu1(h)
on 37/39 steps of the 8x8-core co-block surface with med k* ~ 3 --
but k* was NOT measured bounded there: the two largest-|b| steps
stay open at k = 6 and k = 7 is exact in the 7-dim co-block (the
frame is too small to decide boundedness).  The named next objects
were (a) the k* ladder under b-normalization and (b) the same
measurement in a LARGER co-block where k <= K_MAX is far from the
full space.  THIS PROBE delivers both on the FULL WALL FRAME:
K_h is the deployed h x h odd-Toeplitz wall itself, on the 67
registered faithful rungs (h = 142..1433, CLI registry sha
ae292e55) PLUS the 28 deep 4e6-table holdout rungs (CLIV, h =
1219..2854) -- a 20x dimension range with co-blocks of dimension
141..2853, where k <= 30 is FAR from the full space.

THE SPLIT (frozen, anti-circular).  Direction = the CLASSICAL soft
direction v_sm: the bottom eigenvector of the PRIME-FREE smooth
wall (same window frame, atoms replaced by the PNT continuum comb
-- critical_direction_classical_probe / CI verbatim; measured
overlap with the true soft mode 0.88..0.99.  AMENDMENT A1,
disclosed after smoke 1: the comb resolution scales with the
frame, ng = max(NG_SMOOTH_MIN, NG_FACT * M) -- the predecessors'
fixed 6000-point comb develops a spurious head-localized bottom
mode at deep alpha (lam_sm -9.6/-13.3 at the two smoke deep
rungs, overlap 0); the classical branch is grid-converged and
identical at 2x..16x the amended resolution; guarded by the new
kill ward W8: lam_min(K_sm) must sit on the classical branch
band SM_BRANCH = [-2.0, -0.5] on every rung).
NO target eigendata enters the construction: v_sm is prime-free
given the window frame, n = v_sm^T K v_sm is a source-only scalar,
b = the coupling column and B = the (h-1)-dim co-block of K in the
Householder frame of v_sm.  Everything is computed in RAW K units;
tau = lam_min(K) appears ONLY in reporting/regression units and in
wards/controls, never in any construction.  The target: since the
registered halfgap holds on all 95 rungs (CLI 67/67, CLIV 28/28),
n - q >= lam_min(K) >= (1/2) mu1(h) holds EXACTLY along ANY unit
direction; the question is purely CERTIFICATION DEPTH -- the
smallest k such that the k-step Gauss-Radau upper bound R_k on
q = b^T B^{-1} b (node at the measured co-block floor) certifies
n - R_k >= (1/2) mu1(h), mu1(h) = 4 sin^2(pi/(2h+1)).

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN):
     W1 deployed faithful ladder = 67 rungs (kz 2..150, H_MIN <=
        h <= HCAP, X <= ATOM_MAX), registry lines "kz:h:shat" ==
        sha256 ae292e55... (CLI frozen registry, eigh path);
     W2 CXLIII band shat min/med/max == 0.502/1.027/2.185 (rtol
        2e-2), margin exponent p in EXPO_BAND = [-2.5, -1.5];
     W3 GAP-RATIO REPRODUCTION (the CI full-frame co-block floor
        story; AMENDMENT A3, disclosed: the first frozen run
        KILLED here at med lam_1/lam_0 = 2.888 against a
        reference frozen as 1.89 -- a reference-CONVENTION
        misread, the CI census prints med(lam_1/lam_0 - 1) =
        1.89 [the gap] and min(lam_1/lam_0) = 1.02 [the ratio];
        the measured 2.888 - 1 = 1.888 matches CI exactly, no
        measurement moved; the ward is re-keyed to the CI
        convention): med(lam_1/lam_0 - 1) == 1.89 (rtol 5e-2),
        min(lam_1/lam_0) == 1.02 (rtol 2e-2) and the min sits at
        kz 90 (the known near-degenerate exception, reported
        honestly);
     W4 CLASSICAL-DIRECTION REPRODUCTION: |<v0, v_sm>| >= 0.80 on
        every SUBSET rung (critdir bar, kz 9/13/26/40/60/90/121);
        the full 95-rung overlap census is RECORDED (the deep
        rungs are new surface, no bar);
     W5 DEEP FIDELITY (deep_blind_holdout verbatim): extended
        table == deployed on [0, ATOM_MAX] byte-exact; prefix
        arrays NN/U/MU/G bitwise; extended Chebyshev kappa <=
        KAPPA_REF + 1e-6; new-rung census >= MIN_NEW = 10 in
        H_HOLD = [128, 2900]; convention regression on REG_KZ =
        (9, 60, 121): lam_min through the extended pipeline ==
        deployed to REG_WARD = 1e-9 relative, frame ties exact;
     W6 INTERLACING WARD on every rung: measured lam_min(B) >=
        lam_min(K) (1 - INTERLACE_WARD), zero refusals in the
        true world -- the co-block floor is positive by
        interlacing; its SIZE is the measurement;
     W7 SCHUR TIE on every rung: n - q == 1/(v_sm^T K^{-1} v_sm)
        to NQTIE_WARD relative (cancellation-aware bar, declared);
        and the exact target n - q >= (1/2) mu1 must hold on
        every rung (it follows from the registered halfgap);
     W8 SMOOTH-BRANCH GUARD (A1): lam_min(K_sm) in SM_BRANCH =
        [-2.0, -0.5] on every rung -- the classical branch, not
        the low-resolution artifact.

 E1  THE LANCZOS BRACKET (per rung, k = 1..K_MAX = 30 primary;
     AMENDMENT A2, disclosed after smoke 1: additionally the
     Radau-only EXTENDED ladder to kcap = min(K_EXT = 150,
     dim(B) - 1), so the growth law is fittable -- smoke 1
     measured deficits still at -20..-177 tau at k = 30 on most
     of the subset, the primary bar alone would leave the law
     unfittable; the primary k* definition and every bar are
     unchanged; grade breakdown at GRADE_BD, values frozen at
     the grade):  WARDS (kill -> WARD-BROKEN):
     E1.w1 bracket G_k <= q <= R_k over the FULL extended ladder
           (one-sided allowance BRK_WARD relative to q);
     E1.w2 monotonicity over the full extended ladder: G_k
           nondecreasing, R_k nonincreasing (violation <=
           MONO_WARD relative to q);
     E1.w3 CG tie G_k == b^T x_k at k <= K_MAX (x_k = k-step
           Krylov minimizer; CGTIE_WARD relative);
     E1.w4 Radau == optimal Krylov defect bound given the node
           at k <= K_MAX (projected identity, CLIX E1.w4
           verbatim; OPT_WARD relative);
     E1.w5 grade exactness G_g == q at breakdown (GRADE_WARD).
     NODE CHOICE (declared): the Radau node is NODE_FACT = 0.999
     times the measured float lam_min(B) per rung -- strictly
     legal under float noise at a < 0.1% bound cost.  The floor
     is a MEASURED float quantity: this is a measurement probe; a
     certified big-frame floor is a SEPARATE FUTURE OBJECT and is
     not claimed here.

 E2  THE FLOOR CENSUS (question (a), typed, never kill): per rung
     lam_min(B)/tau (>= 1 by interlacing; the v881 bulk-margin
     story suggests O(1) above 1 away from the soft direction),
     min/med/max, the kz-90 exception explicitly, OLS slope of
     log(floor/tau) vs log h; the V_SM COST: floor/lam_1(K) per
     rung (= 1 if the split used the true v0; the measured ratio
     is the price of the classical direction), min/med/max.
     Typed FLOOR-O1(min, med, slope) iff min floor/tau >= 1 -
     1e-6 and |slope| <= SLOPE_PASS, else FLOOR-DRIFTS(...).

 E3  THE k* LADDER (question (b), THE HEADLINE, typed, never
     kill): per rung k*_pos = min k with n - R_k > 0, k*_half =
     min k with n - R_k >= (1/2) mu1(h), k*_cg = the same from
     the plain CG defect bound 2 b^T x - x^T B x + |b - Bx|^2 /
     node (INF if not reached by K_MAX); the full 95-rung table;
     census over deployed / deep separately and combined; OLS
     slope of k*_half vs log h on the reached subset.  Typed
     KSTAR-BOUNDED(max, med, census, slope) iff k*_half reached
     on ALL 95 rungs, KSTAR-NOT-REACHED(count, list) if any INF;
     the deep-vs-shallow census decides the honest boundedness
     verdict over the 20x range.  PLUS the A2 extended census:
     k*_ext = min k <= kcap certifying half from the Radau
     ladder, per-source census, linear fit k*_ext ~ log h and
     power-law fit log k*_ext ~ log h on the reached subset
     (EXT-LADDER label).  Bracket-width table: med (R_k - G_k)/q
     at k in KTAB.  tau-screen (CLIX bands PASS |s| <= 0.30 /
     RELOC >= 0.70 / AMBIG) of the half-margin n - R_{k*} -
     mu1/2 (in tau units) on the reached subset.

 E4  b-NORMALIZATION ANATOMY (question (c), typed, never kill;
     on the A2 EXTENDED reached subset, declared -- the primary
     k <= 30 subset is too small to organize): OLS of k*_ext
     against each of log(|b|/tau), log(|b|/n), log h, alpha,
     log tau -- the R^2 table and ORGANIZER(var, R2) = the
     argmax; the top-5 |b|/tau rungs vs the top-5 k*_ext rungs
     (the predecessors' outliers were |b|-organized -- census of
     the overlap).  If k*_ext is constant on the reached subset
     the regression is DEGENERATE and said so (recorded, no fit
     invented).

 E5  MOMENT ANATOMY / OBSTRUCTION (question (d), typed, never
     kill): iff k*_half <= KSTAR_SMALL = 10 on ALL 95 rungs
     (MOMENTS-REDUCED), print at the 3 representative rungs
     (shallowest / median / deepest by h) the source-only moments
     m_j = b^T B^j b, j = 0..2*kprint (kprint = med k*_half
     capped at KSTAR_SMALL) with the declared atom anatomy: in
     co-frame coordinates m_j = sum_i (b)_i (B^j b)_i, coordinate
     i attributed to grid point g by Q[g, 1+i]^2, aggregated into
     the four grid-index quartiles of the window (declared
     convention; the u-scale reading is context).  Else
     OBSTRUCTION-LAW: the growth fit of k*_ext vs log h (A2
     extended reached subset) and the deficit anatomy (n - R_k -
     mu1/2)/tau vs k in KTAB_EXT at the same 3 representative
     rungs -- where the demand concentrates.

 C   CONTROLS (kill -> WARD-BROKEN if silent, except C4 as
     declared):
     C1 SMOOTH FLOOR REFUSAL on the SUBSET rungs: the smooth wall
        K_sm split along its own bottom eigenvector must REFUSE
        (co-block floor <= 0 -- no legal Radau node; mirror of
        the CLVIII/CLIX floor-refusal pattern) on 7/7;
     C2 EPSTEIN x^2+5y^2 comb at kz CTRL_KZ = 9 (shallow only,
        the CLIV-declared depth skip applies): wall breaks
        (lam_min < 0) and the v_sm split refuses (floor <= 0);
     C3 SCRAMBLE (seed 1) at kz 9: same refusal pattern;
     C4 RANDOM SPLIT DIRECTION (seed 20260811, declared RNG use)
        on RAND_SUBSET = the 7 SUBSET rungs + the 2 shallowest
        deep rungs: k*_ext census random vs classical on the
        same rungs (extended ladder, A2 -- the primary k <= 30
        census is INF-saturated and cannot discriminate, smoke 1
        measured).  DECLARED EXPECTATION: the classical
        direction is load-bearing (random degrades k*
        dramatically).  Typed RAND-DEGRADES / RAND-UNINFORMATIVE
        (recorded honestly, CLIX C4 pattern, no kill on
        uninformative); kill -> WARD-BROKEN ONLY if random is
        strictly BETTER on median (the classical direction would
        carry nothing).

KILLS: K1 pipeline (W1 count, D1 census) -> PIPELINE-BROKEN; K2
reproduction / ward / control failures (W1 sha, W2-W7, E1.w1-w5,
C1-C3, C4 strict-better) -> WARD-BROKEN.  All E2-E5 typed
outcomes are measurements, never kills.

VERDICT (frozen enum): DIRLANCZOSFF-MEASURED with typed sublabels
FLOOR-O1/FLOOR-DRIFTS(...), VSM-COST(...), KSTAR-BOUNDED /
KSTAR-NOT-REACHED(...), ORGANIZER(...)/ORGANIZER-DEGENERATE,
MOMENTS-REDUCED / OBSTRUCTION-LAW(...), RAND-...(...),
SCREENS(...); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: K_MAX = 30; K_EXT = 150 (A2); KSTAR_SMALL = 10;
NODE_FACT = 0.999; GRADE_BD = 1e-13; BRK_WARD = 1e-7; MONO_WARD =
1e-7; CGTIE_WARD = 1e-6; OPT_WARD = 1e-5; GRADE_WARD = 1e-7;
KRY_BD = 1e-12; INTERLACE_WARD = 1e-8; NQTIE_WARD = 1e-4; REG_SHA
= ae292e55... (full below); SHAT_REF = (0.502, 1.027, 2.185)
rtol 2e-2; EXPO_BAND = (-2.5, -1.5); GAPR_MED_REF = 1.89 [=
med(lam_1/lam_0 - 1), A3] rtol 5e-2; GAPR_MIN_REF = 1.02 [=
min(lam_1/lam_0)] rtol 2e-2 at kz 90; OV_MIN = 0.80 on
SUBSET = (9, 13, 26, 40, 60, 90, 121); NG_SMOOTH_MIN = 6000,
NG_FACT = 8, SM_BRANCH = (-2.0, -0.5) (A1); TAB_EXT = 4e6;
H_HOLD = (128, 2900); MIN_NEW = 10; KZ_SCAN_MAX = 400; REG_KZ =
(9, 60, 121); REG_WARD = 1e-9; SLOPE_PASS = 0.30; SLOPE_RELOC =
0.70; CTRL_KZ = 9; scramble seed 1; random-direction seed
20260811; KTAB = (1, 2, 3, 4, 6, 8, 12, 16, 20, 24, 30);
KTAB_EXT = (1, 2, 4, 8, 16, 30, 45, 60, 90, 120, 150); mu1(h)
= 4 sin^2(pi/(2h+1)).  Runtime cap declared: 15 min.

ANTI-CIRCULARITY (frozen): the split direction v_sm is prime-free
given the window frame (critdir CI); n, b, B and all Lanczos
matvecs are source-only reads of K along v_sm; the measured floor
lam_min(B) enters ONLY as the declared Radau/defect node of this
MEASUREMENT probe (a certified big-frame floor is a separate
future object, stated in every print); q by direct solve, tau,
lam_1 and the true v0 appear ONLY in wards, units, reporting and
controls -- decisions and diagnostics, never constructions.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; the round-61 pivot-Radau no-go does not apply (the
measure is the directional measure of B relative to b, CLIX
distinction verbatim).

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run;
TWO disclosed amendments A1/A2 after smoke 1, fail-first
preserved -- no bar, band, enum or success criterion was moved,
A1 repairs the resolution of the classical CONSTRUCTION and adds
the kill guard W8, A2 only ADDS measurement surface): everything
above and the smoke disclosures below.  Mechanical
concretizations frozen with v1: (i) Householder frame as CL/CXLIV
(sign convention Q[:, 0] = +v_sm), applied in rank-2 matrix-free
form; (ii) directional Lanczos with double full
reorthogonalization; Radau extension via beta_k (at grade:
zero-weight node, R_g = G_g = q, declared natural limit); (iii)
rungs sorted by (h, kz); registry format "%d:%d:%.12e"; (iv) OLS
population statistics; screens read positive subsets; (v) the
CG/Krylov defect bound rebuilt in-file with the CLVIII/CLIX
krylov_iterates machinery (declared reproduction, not an import);
(vi) moment/attribution tables computed in-pass for every rung at
j <= 2*KSTAR_SMALL, printed only at the representatives; (vii)
grid-index quartiles of the h-point window as the declared
attribution bands; (viii) the random-direction RNG is consumed in
build order over RAND_SUBSET (deterministic, declared).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing; two smokes,
both DIRFF_SMOKE=1: deployed pass restricted to the 7 SUBSET
rungs, deep pass to the 2 shallowest new rungs, W1/W2/W3 typed
SKIPPED-IN-SMOKE).  SMOKE 1 (22/22, 13.8 s, pre-A1/A2): all
wards green on the deployed subset (bracket/monotonicity 0.0/0.0,
CG tie 2.1e-14, Radau-opt 1.2e-07, interlacing 0.0, Schur tie
1.4e-10), deployed overlaps 0.878..0.990, deployed floor/tau
2.11..5.21 with kz-90 at 1.0162 -- BUT the two deep rungs came
out with overlap 0.000, floor/tau exactly 1.000 and n/tau ~ 1e5:
the fixed 6000-point smooth comb develops a spurious
head-localized bottom mode at deep alpha (lam_sm0 -9.61/-13.33
vs the classical branch -1.29/-1.30 sitting at index 1 with
overlap 0.972/0.994; a sizing scan measured the branch
grid-converged and IDENTICAL at ng 12000/24000/48000, deployed
rungs unchanged at every ng) -> AMENDMENT A1.  And the k <= 30
primary ladder is INF on 5/9 subset rungs with deficits still
-4.2..-177 tau at k = 30 (reached: 26, 27 at the two shallowest;
k*_cg INF on 9/9 -- the plain CG defect bound never certifies at
k <= 30) -> AMENDMENT A2 (extended Radau-only ladder, so the
growth law is fittable; primary bars untouched).  SMOKE 2
(23/23, 15.2 s, post-A1/A2, the frozen machinery): deep rungs
now ov 0.972/0.994, floor/tau 2.73/3.58, vsm-cost 0.968..0.999,
W8 branch guard -1.303..-0.973 in band 9/9, all E1 wards green
(bracket/mono 0.0/0.0 over the extended ladder, CG tie 4.1e-14,
Radau-opt 7.1e-08); k* at K_MAX = 30 reached only on the two
shallowest subset rungs (26, 27), EXTENDED ladder reached 5/9
(med 66, max 104; INF at k <= 150 on the four largest-h subset
rungs), growth kext ~ +62.3 log h (R2 0.96), power-law exponent
+1.17 (R2 0.96), ORGANIZER log|b|/tau R2 0.972 with top-5
overlap 5/5; C1 7/7 refusals (floors -1.14..-0.63), C2 Epstein
(neg 55, floor -1.0e+01), C3 scramble (neg 37, floor -7.9e+00),
C4 on the extended ladder RAND-DEGRADES (med 104 -> 151).  NO
bar, band, count, rule or enum was moved after smoke 2.
FROZEN-RUN-1 DISCLOSURE (A3): the first full frozen run KILLED
at W3 (WARD-BROKEN, 27.7 s; W1 registry sha MATCH, W2 band
exact, W4 census min/med 0.826/0.981 all green) because the W3
reference mixed the CI conventions (see W3 above); the recorded
med lam_1/lam_0 = 2.888 IS the CI med gap 1.888 + 1 and the min
1.020 at kz 90 is exact; A3 re-keys the ward to the CI
convention and nothing else; the kill is on protocol, fail-first
preserved.

NO RH claim: k* ladders, floors, moments and regressions are
SURFACE measurements on the computed float64 wall matrices of the
deployed + extended ladders ONLY; they prove neither h-uniformity
nor any tail statement; no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
and random-direction controls; stdout only.

Sources (read-only): v563_paper2_readouts (deployed tables, tent
assembly, arch lags, odd Toeplitz); halfgap_registration_probe
(CLI registry sha + shat band); rh_leverage_probe (margin law,
full-frame wall build); wall_margin_mechanism_probe /
critical_direction_classical_probe (CI: gap ratios, classical
v_sm, overlap bars); deep_blind_holdout_probe (CLIV: extended
table wards + deep census); directional_defect_correction_probe /
directional_lanczos_probe (CLVIII/CLIX: the certified route this
probe continues; Gauss/Radau/defect machinery verbatim).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/directional_lanczos_fullframe_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

K_MAX = 30
K_EXT = 150
KSTAR_SMALL = 10
NODE_FACT = 0.999
GRADE_BD = 1e-13
BRK_WARD = 1e-7
MONO_WARD = 1e-7
CGTIE_WARD = 1e-6
OPT_WARD = 1e-5
GRADE_WARD = 1e-7
KRY_BD = 1e-12
INTERLACE_WARD = 1e-8
NQTIE_WARD = 1e-4
REG_SHA = ("ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e"
           "5c652e3458df8")
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2e-2
EXPO_BAND = (-2.5, -1.5)
GAPR_MED_REF = 1.89
GAPR_MED_RTOL = 5e-2
GAPR_MIN_REF = 1.02
GAPR_MIN_RTOL = 2e-2
GAPR_MIN_KZ = 90
SUBSET = (9, 13, 26, 40, 60, 90, 121)
OV_MIN = 0.80
NG_SMOOTH_MIN = 6000
NG_FACT = 8
SM_BRANCH = (-2.0, -0.5)
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
MIN_NEW = 10
KZ_SCAN_MAX = 400
REG_KZ = (9, 60, 121)
REG_WARD = 1e-9
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
SCRAMBLE_SEED = 1
RAND_SEED = 20260811
KTAB = (1, 2, 3, 4, 6, 8, 12, 16, 20, 24, 30)
KTAB_EXT = (1, 2, 4, 8, 16, 30, 45, 60, 90, 120, 150)
SMOKE = os.environ.get("DIRFF_SMOKE", "") == "1"
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f, R2=%.3f)" % (lab, sl, r2), sl


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def smooth_comb(alpha, M):
    """PNT continuum comb; resolution scales with the frame
    (amendment A1: ng = max(NG_SMOOTH_MIN, NG_FACT * M) -- the
    fixed 6000-point comb of the deployed-depth predecessors
    develops a spurious head-localized bottom mode at deep
    alpha; the classical branch is grid-converged, measured
    identical at 2x..16x the amended resolution)."""
    ng = max(NG_SMOOTH_MIN, NG_FACT * M)
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def wall_from(alpha, M, D, uu, mm):
    c = (np.asarray(core.arch_lags(M, D), float)
         + np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0],
                      float))
    return core.odd_toeplitz(c, M)


def householder_u(v):
    """Householder data u for Q = I - 2 u u^T with Q[:, 0] = +v
    (CL/CXLIV sign convention); u = None means Q = I."""
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(len(v))
    e1[0] = 1.0
    w = e1 - v
    nw = float(np.linalg.norm(w))
    if nw < 1e-14:
        return None
    return w / nw


def apply_q(u, X):
    """Q @ X for Q = I - 2 u u^T (X matrix or vector); Q is
    symmetric, so this is also Q^T @ X."""
    if u is None:
        return np.array(X, float, copy=True)
    if X.ndim == 1:
        return X - 2.0 * u * float(u @ X)
    return X - 2.0 * np.outer(u, u @ X)


def split_along(K, v):
    """Householder split of K along unit v: returns (u, n, b, B)
    with n = v^T K v, b = coupling column, B = co-block."""
    u = householder_u(v)
    KQ = apply_q(u, apply_q(u, K).T)        # Q^T K Q, rank-2 form
    KQ = 0.5 * (KQ + KQ.T)
    n = float(KQ[0, 0])
    b = KQ[1:, 0].copy()
    B = np.ascontiguousarray(KQ[1:, 1:])
    return u, n, b, B


# ---------------- directional Lanczos + quadrature (CLIX verbatim)
def dir_lanczos(B, b, kmax):
    beta0 = float(np.linalg.norm(b))
    V = [b / beta0]
    alphas, betas = [], []
    grade = None
    for k in range(kmax):
        w = B @ V[k]
        a = float(V[k] @ w)
        alphas.append(a)
        w = w - a * V[k]
        if k > 0:
            w = w - betas[k - 1] * V[k - 1]
        for _ in range(2):
            for uv in V:
                w = w - float(uv @ w) * uv
        bn = float(np.linalg.norm(w))
        if bn <= GRADE_BD:
            betas.append(0.0)
            grade = k + 1
            break
        betas.append(bn)
        V.append(w / bn)
    return alphas, betas, beta0, grade


def jk_of(alphas, betas, k):
    J = np.diag(np.array(alphas[:k], float))
    if k > 1:
        off = np.array(betas[:k - 1], float)
        J += np.diag(off, 1) + np.diag(off, -1)
    return J


def gauss_lower(alphas, betas, beta0, k):
    J = jk_of(alphas, betas, k)
    e1 = np.zeros(k)
    e1[0] = 1.0
    return beta0 * beta0 * float(np.linalg.solve(J, e1)[0])


def radau_upper(alphas, betas, beta0, k, node):
    J = jk_of(alphas, betas, k)
    bk = float(betas[k - 1])
    ek = np.zeros(k)
    ek[-1] = 1.0
    if bk == 0.0:                      # grade: zero-weight node
        ahat = node
    else:
        delta = np.linalg.solve(J - node * np.eye(k),
                                bk * bk * ek)
        ahat = node + float(delta[-1])
    Jt = np.zeros((k + 1, k + 1))
    Jt[:k, :k] = J
    Jt[k, k] = ahat
    Jt[k - 1, k] = Jt[k, k - 1] = bk
    e1 = np.zeros(k + 1)
    e1[0] = 1.0
    return beta0 * beta0 * float(np.linalg.solve(Jt, e1)[0])


def krylov_opt_defect(alphas, betas, beta0, k, node):
    J = jk_of(alphas, betas, k)
    bk = float(betas[k - 1])
    ek = np.zeros(k)
    ek[-1] = 1.0
    J2 = J @ J + (bk * bk) * np.outer(ek, ek)
    e1 = np.zeros(k)
    e1[0] = 1.0
    H = J2 / node - J
    rhs = (beta0 / node) * (J @ e1) - beta0 * e1
    y = np.linalg.solve(H, rhs)
    return (2.0 * beta0 * y[0] - float(y @ (J @ y))
            + (beta0 * beta0 - 2.0 * beta0 * float((J @ y)[0])
               + float(y @ (J2 @ y))) / node)


def krylov_iterates(b, B, kmax):
    """CLVIII/CLIX CG-equivalent Krylov minimizers (declared
    reproduction)."""
    V = []
    v = b.copy()
    n0 = float(np.linalg.norm(v))
    xs = []
    for k in range(kmax):
        nv = float(np.linalg.norm(v))
        if nv <= KRY_BD * max(n0, 1e-300):
            break
        v = v / nv
        for _ in range(2):
            for uv in V:
                v = v - float(uv @ v) * uv
        nv2 = float(np.linalg.norm(v))
        if nv2 <= KRY_BD:
            break
        V.append(v / nv2)
        Vm = np.array(V).T
        Bp = Vm.T @ B @ Vm
        Bp = 0.5 * (Bp + Bp.T)
        y = np.linalg.solve(Bp, Vm.T @ b)
        xs.append(Vm @ y)
        v = B @ V[-1]
    while xs and len(xs) < kmax:
        xs.append(xs[-1].copy())
    return xs


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


# --------------------- the extended (deep) surface, CLIV verbatim
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def rung_certify(K, vdir, mu1, want_moments=True):
    """One full-frame directional certification pass; returns the
    per-rung record (scalars + ladders + optional moment table)
    and the ward deviations."""
    u, nsc, b, B = split_along(K, vdir)
    floor = float(np.linalg.eigvalsh(B)[0])
    rec = dict(n=nsc, bnorm=float(np.linalg.norm(b)), floor=floor)
    if floor <= 0.0:
        rec["refused"] = True
        return rec, {}
    rec["refused"] = False
    node = NODE_FACT * floor
    rec["node"] = node
    q = float(b @ np.linalg.solve(B, b))     # ward/report only
    rec["q"] = q
    kcap = min(K_EXT, B.shape[0] - 1)        # extended ladder cap
    rec["kcap"] = kcap
    al, be, b0, grade = dir_lanczos(B, b, kcap)
    keff = len(al)
    G_l, R_l, O_l = [], [], []
    for k in range(1, keff + 1):
        G_l.append(gauss_lower(al, be, b0, k))
        R_l.append(radau_upper(al, be, b0, k, node))
        if k <= K_MAX:
            O_l.append(krylov_opt_defect(al, be, b0, k, node))
    while len(G_l) < kcap:                   # frozen at grade
        G_l.append(G_l[-1])
        R_l.append(R_l[-1])
    while len(O_l) < K_MAX:
        O_l.append(O_l[-1])
    xs = krylov_iterates(b, B, K_MAX)
    cg_l = []
    for k in range(K_MAX):
        xk = xs[k]
        rv = b - B @ xk
        cg_l.append(2.0 * float(b @ xk) - float(xk @ (B @ xk))
                    + float(rv @ rv) / node)
    dev = dict(brk=0.0, mono=0.0, tie=0.0, opt=0.0, grade=0.0,
               n_grade=int(grade is not None))
    qs = max(abs(q), 1e-300)
    for k in range(kcap):
        dev["brk"] = max(dev["brk"], (G_l[k] - q) / qs,
                         (q - R_l[k]) / qs)
    for k in range(K_MAX):
        dev["opt"] = max(dev["opt"], abs(R_l[k] - O_l[k])
                         / max(abs(R_l[k]), 1e-300))
        gk = float(b @ xs[k])
        kk = min(k, keff - 1)
        dev["tie"] = max(dev["tie"], abs(G_l[kk] - gk)
                         / max(abs(gk), 1e-300))
    for k in range(1, kcap):
        dev["mono"] = max(dev["mono"], (G_l[k - 1] - G_l[k]) / qs,
                          (R_l[k] - R_l[k - 1]) / qs)
    if grade is not None:
        dev["grade"] = abs(G_l[grade - 1] - q) / qs
    rec["G"], rec["R"], rec["cg"] = G_l, R_l, cg_l
    rec["kpos"] = next((k + 1 for k in range(K_MAX)
                        if nsc - R_l[k] > 0.0), None)
    rec["khalf"] = next((k + 1 for k in range(K_MAX)
                         if nsc - R_l[k] >= 0.5 * mu1), None)
    rec["kcg"] = next((k + 1 for k in range(K_MAX)
                       if nsc - cg_l[k] >= 0.5 * mu1), None)
    rec["kext"] = next((k + 1 for k in range(kcap)
                        if nsc - R_l[k] >= 0.5 * mu1), None)
    if want_moments:
        h = K.shape[0]
        qb = [0, h // 4, h // 2, 3 * h // 4, h]
        Bj = b.copy()
        moms, shares = [], []
        uu2 = None if u is None else u * u
        for j in range(2 * KSTAR_SMALL + 1):
            if j > 0:
                Bj = B @ Bj
            pi_ = b * Bj
            moms.append(float(pi_.sum()))
            # attribution: share_g = sum_i pv_i Q[g, i]^2 with
            # pv = [0, pi_]; Q = I - 2 u u^T gives Q[g, i]^2 =
            # delta_gi - 4 delta_gi u_g u_i + 4 u_g^2 u_i^2
            pv = np.concatenate([[0.0], pi_])
            if uu2 is None:
                sg = pv
            else:
                sg = (pv - 4.0 * uu2 * pv
                      + 4.0 * uu2 * float(np.sum(uu2 * pv)))
            shares.append([float(np.sum(sg[qb[t]:qb[t + 1]]))
                           for t in range(4)])
        rec["moms"], rec["shares"] = moms, shares
    return rec, dev


def process_rung(r, K, rng, do_rand):
    """Certify rung r on wall K, accumulate wards into r, run the
    in-pass random-direction control if requested, free K."""
    rec, dv = rung_certify(K, r["vsm"], r["mu1"])
    r["rec"], r["dev"] = rec, dv
    if not rec["refused"]:
        x = np.linalg.solve(K, r["vsm"])
        r["nq_inv"] = 1.0 / float(r["vsm"] @ x)
        kk = (rec["khalf"] or K_MAX) - 1
        r["hm"] = (rec["n"] - rec["R"][kk]
                   - 0.5 * r["mu1"]) / r["tau"]
        if do_rand:
            g = rng.standard_normal(K.shape[0])
            g = g / float(np.linalg.norm(g))
            r["rand"] = rung_certify(K, g, r["mu1"],
                                     want_moments=False)[0]


def main():
    section("PRIME.PORT.DIRECTIONAL.LANCZOS.02 -- the k* ladder of "
            "the directional Gauss-Radau certification on the FULL "
            "h x h wall frame, split along the classical v_sm; 67 "
            "registered + 28 deep rungs (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  The co-block floor "
          "is a MEASURED float quantity (Radau node %.3f x "
          "measured lam_min(B)); a certified big-frame floor is a "
          "separate future object." % NODE_FACT)
    if SMOKE:
        print("    *** SMOKE MODE: SUBSET rungs + 2 deep only; "
              "W1/W2/W3 typed SKIPPED-IN-SMOKE ***")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    rng = np.random.default_rng(RAND_SEED)

    # -------------------------------------------------- W deployed
    section("W -- deployed ladder: registry, bands, gap ratios, "
            "classical direction (+ in-pass certification)")
    dep = []
    for kz in range(2, 151):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        if SMOKE and kz not in SUBSET:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        K = wall_from(alpha, M, D, uu, mu)
        w, V = np.linalg.eigh(K)
        ug, mg = smooth_comb(alpha, M)
        Ksm = wall_from(alpha, M, D, ug, mg)
        ws, Vs = np.linalg.eigh(Ksm)
        r = dict(kz=kz, h=h, alpha=alpha, M=M, D=D, src="dep",
                 tau=float(w[0]), lam1=float(w[1]),
                 vsm=Vs[:, 0].copy(), lam_sm=float(ws[0]),
                 shat=float(w[0]) / mu1_of(h), mu1=mu1_of(h),
                 ov=abs(float(V[:, 0] @ Vs[:, 0])))
        process_rung(r, K, rng, do_rand=(kz in SUBSET))
        dep.append(r)
        del K, V, Vs, Ksm
    dep.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d deployed faithful rungs certified  [%.1f s]"
          % (len(dep), time.time() - T0))
    if SMOKE:
        check("W1 registry reproduction SKIPPED-IN-SMOKE (subset "
              "pass)", True)
        check("W2 band/exponent reproduction SKIPPED-IN-SMOKE",
              True)
    else:
        lines = "\n".join("%d:%d:%.12e" % (r["kz"], r["h"],
                                           r["shat"])
                          for r in dep)
        sha = hashlib.sha256(lines.encode("utf-8")).hexdigest()
        check("W1 deployed ladder: %d rungs, registry sha %s.. "
              "== ae292e55.." % (len(dep), sha[:8]),
              len(dep) == 67 and sha == REG_SHA,
              kill="K1" if len(dep) != 67 else "K2")
        sh = np.array([r["shat"] for r in dep])
        trio = (float(sh.min()), float(np.median(sh)),
                float(sh.max()))
        _a, p_dep, _r2 = ols_line(
            np.log(np.array([float(r["h"]) for r in dep])),
            np.log(np.array([r["tau"] for r in dep])))
        check("W2 shat band %.3f/%.3f/%.3f == 0.502/1.027/2.185; "
              "exponent %+.3f in [%.1f, %.1f]"
              % (trio[0], trio[1], trio[2], p_dep, EXPO_BAND[0],
                 EXPO_BAND[1]),
              all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio, SHAT_REF))
              and EXPO_BAND[0] <= p_dep <= EXPO_BAND[1],
              kill="K2")
    gr = np.array([r["lam1"] / r["tau"] for r in dep])
    i_min = int(np.argmin(gr))
    if SMOKE:
        check("W3 gap-ratio reproduction SKIPPED-IN-SMOKE (census "
              "min %.3f med %.3f)" % (float(gr.min()),
                                      float(np.median(gr))), True)
    else:
        check("W3 gap-ratio reproduction (A3, CI convention): "
              "med(lam_1/lam_0 - 1) = %.3f == %.2f (rtol %.0e); "
              "min(lam_1/lam_0) = %.3f == %.2f (rtol %.0e) at "
              "kz %d (== %d, the known near-degenerate "
              "exception)"
              % (float(np.median(gr - 1.0)), GAPR_MED_REF,
                 GAPR_MED_RTOL, float(gr.min()), GAPR_MIN_REF,
                 GAPR_MIN_RTOL, dep[i_min]["kz"], GAPR_MIN_KZ),
              abs(float(np.median(gr - 1.0)) / GAPR_MED_REF
                  - 1.0) <= GAPR_MED_RTOL
              and abs(float(gr.min()) / GAPR_MIN_REF - 1.0)
              <= GAPR_MIN_RTOL
              and dep[i_min]["kz"] == GAPR_MIN_KZ, kill="K2")
    ov_sub = [r["ov"] for r in dep if r["kz"] in SUBSET]
    ov_all = np.array([r["ov"] for r in dep])
    check("W4 classical direction: |<v0, v_sm>| = %.3f..%.3f on "
          "the %d SUBSET rungs (bar >= %.2f); deployed census "
          "min/med %.3f/%.3f (recorded)"
          % (min(ov_sub), max(ov_sub), len(ov_sub), OV_MIN,
             float(ov_all.min()), float(np.median(ov_all))),
          all(o >= OV_MIN for o in ov_sub), kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------ W deep
    section("W -- deep surface: extended 4e6 table + census + "
            "convention regression (+ in-pass certification)")
    lam_ext = build_ext_tables()
    dev_tab = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
               and np.array_equal(EXT["U"][:nP], core.U_ALL)
               and np.array_equal(EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep])
                         / nnf[keep]))
    dev_reg = 0.0
    for kz in REG_KZ:
        rr = core.build_window(kz)
        uu_d = np.asarray(rr["uu"], float)
        mu_d = 2.0 * np.asarray(rr["lam"], float)
        lam_d = float(np.linalg.eigvalsh(
            wall_from(rr["alpha"], rr["M"], rr["D"], uu_d,
                      mu_d))[0])
        a_e, M_e, h_e, ka_e = ext_frame(kz)
        c_at_e, D_e = core.atom_lags_at(a_e, M_e, EXT["U"][:ka_e],
                                        EXT["MU"][:ka_e])
        lam_e = float(np.linalg.eigvalsh(core.odd_toeplitz(
            np.asarray(core.arch_lags(M_e, D_e), float)
            + np.asarray(c_at_e, float), M_e))[0])
        ok_f = (a_e == rr["alpha"] and M_e == rr["M"]
                and h_e == rr["h"] and ka_e == rr["n_atom"])
        dev_reg = max(dev_reg, abs(lam_e - lam_d)
                      / max(abs(lam_d), 1e-300)
                      + (0.0 if ok_f else 1.0))
    check("W5 deep fidelity: table overlap dev %.1e == 0; prefix "
          "arrays bitwise %s; kappa %.6f <= %.6f + 1e-6; "
          "convention regression max rel dev %.1e <= %.0e"
          % (dev_tab, ok_pref, kappa, core.KAPPA_REF, dev_reg,
             REG_WARD),
          dev_tab == 0.0 and ok_pref
          and kappa <= core.KAPPA_REF + 1e-6
          and dev_reg <= REG_WARD, kill="K2")
    new_kz = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        alpha = float(EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        _a, _M, h, _ka = ext_frame(kz)
        if H_HOLD[0] <= h <= H_HOLD[1]:
            new_kz.append(kz)
    order = sorted(new_kz, key=lambda k: (ext_frame(k)[2], k))
    if SMOKE:
        order = order[:2]
    deep = []
    for i_o, kz in enumerate(order):
        alpha, M, h, ka = ext_frame(kz)
        c_at, D = core.atom_lags_at(alpha, M, EXT["U"][:ka],
                                    EXT["MU"][:ka])
        K = core.odd_toeplitz(
            np.asarray(core.arch_lags(M, D), float)
            + np.asarray(c_at, float), M)
        w, V = np.linalg.eigh(K)
        ug, mg = smooth_comb(alpha, M)
        Ksm = wall_from(alpha, M, D, ug, mg)
        ws, Vs = np.linalg.eigh(Ksm)
        r = dict(kz=kz, h=h, alpha=alpha, M=M, D=D, src="deep",
                 tau=float(w[0]), lam1=float(w[1]),
                 vsm=Vs[:, 0].copy(), lam_sm=float(ws[0]),
                 shat=float(w[0]) / mu1_of(h), mu1=mu1_of(h),
                 ov=abs(float(V[:, 0] @ Vs[:, 0])))
        process_rung(r, K, rng, do_rand=(i_o < 2))
        deep.append(r)
        print("    NEW kz %3d h %5d X %.4g shat %.4f ov %.3f  "
              "[%.1f s]" % (kz, h, math.exp(2 * alpha), r["shat"],
                            r["ov"], time.time() - T0), flush=True)
        del K, V, Vs, Ksm
    check("D1 deep census: %d new rungs (>= %d), h %d..%d, all "
          "outside the ae292e55 registry"
          % (len(deep), MIN_NEW if not SMOKE else 2,
             deep[0]["h"], deep[-1]["h"]),
          len(deep) >= (MIN_NEW if not SMOKE else 2), kill="K1")
    if KILLS:
        return finish({})

    # -------------------------------------- E: table + exact wards
    section("E -- the directional certification table (split "
            "along v_sm, node at %.3f x measured floor)"
            % NODE_FACT)
    rows = dep + deep
    rows.sort(key=lambda r: (r["h"], r["kz"]))
    live = [r for r in rows if not r["rec"]["refused"]]
    print("     src  kz    h    floor/tau  vsmcost  |b|/tau   "
          "n/tau     k*pos k*half k*cg  halfmarg@k*/tau")
    for r in rows:
        rec = r["rec"]
        if rec["refused"]:
            print("    %4s %4d %5d  REFUSED (floor %.3e)"
                  % (r["src"], r["kz"], r["h"], rec["floor"]),
                  flush=True)
            continue
        print("    %4s %4d %5d   %8.4f   %6.4f  %8.3e %8.3e   "
              "%-4s  %-4s  %-4s  %+9.3e"
              % (r["src"], r["kz"], r["h"],
                 rec["floor"] / r["tau"],
                 rec["floor"] / r["lam1"],
                 rec["bnorm"] / r["tau"], rec["n"] / r["tau"],
                 str(rec["kpos"]) if rec["kpos"] else "INF",
                 str(rec["khalf"]) if rec["khalf"] else "INF",
                 str(rec["kcg"]) if rec["kcg"] else "INF",
                 r["hm"]), flush=True)
    dev = dict(brk=0.0, mono=0.0, tie=0.0, opt=0.0, grade=0.0)
    n_grade = 0
    dev_int = 0.0
    dev_nq = 0.0
    n_exact = 0
    for r in live:
        for kk in ("brk", "mono", "tie", "opt", "grade"):
            dev[kk] = max(dev[kk], r["dev"][kk])
        n_grade += r["dev"]["n_grade"]
        dev_int = max(dev_int, (r["tau"] - r["rec"]["floor"])
                      / max(abs(r["tau"]), 1e-300))
        nq = r["rec"]["n"] - r["rec"]["q"]
        dev_nq = max(dev_nq, abs(nq - r["nq_inv"])
                     / max(abs(nq), 1e-300))
        n_exact += int(nq >= 0.5 * r["mu1"])
    check("W6 INTERLACING WARD: measured lam_min(B) >= lam_min(K) "
          "on %d/%d rungs (max one-sided dev %.2e <= %.0e); %d "
          "refusals in the true world (0 expected)"
          % (len(live), len(rows), max(dev_int, 0.0),
             INTERLACE_WARD, len(rows) - len(live)),
          dev_int <= INTERLACE_WARD and len(live) == len(rows),
          kill="K2")
    check("W7 SCHUR TIE n - q == 1/(v^T K^-1 v): max rel dev "
          "%.2e <= %.0e; exact target n - q >= mu1/2 on %d/%d "
          "(follows from the registered halfgap)"
          % (dev_nq, NQTIE_WARD, n_exact, len(live)),
          dev_nq <= NQTIE_WARD and n_exact == len(live),
          kill="K2")
    sm_vals = [r["lam_sm"] for r in rows]
    check("W8 SMOOTH-BRANCH GUARD (A1 artifact guard): lam_min("
          "K_sm) = %.3f..%.3f in [%.1f, %.1f] on %d/%d rungs -- "
          "the classical branch, not the low-resolution artifact"
          % (min(sm_vals), max(sm_vals), SM_BRANCH[0],
             SM_BRANCH[1],
             sum(1 for v in sm_vals
                 if SM_BRANCH[0] <= v <= SM_BRANCH[1]),
             len(rows)),
          all(SM_BRANCH[0] <= v <= SM_BRANCH[1]
              for v in sm_vals), kill="K2")
    check("E1.w1 WARD bracket G_k <= q <= R_k: max violation "
          "%.2e <= %.0e" % (max(dev["brk"], 0.0), BRK_WARD),
          dev["brk"] <= BRK_WARD, kill="K2")
    check("E1.w2 WARD monotonicity: max violation %.2e <= %.0e"
          % (max(dev["mono"], 0.0), MONO_WARD),
          dev["mono"] <= MONO_WARD, kill="K2")
    check("E1.w3 WARD CG tie: max rel dev %.2e <= %.0e"
          % (dev["tie"], CGTIE_WARD), dev["tie"] <= CGTIE_WARD,
          kill="K2")
    check("E1.w4 WARD Radau == optimal Krylov defect bound: max "
          "rel dev %.2e <= %.0e" % (dev["opt"], OPT_WARD),
          dev["opt"] <= OPT_WARD, kill="K2")
    check("E1.w5 WARD grade exactness on %d graded rungs: max "
          "rel dev %.2e <= %.0e" % (n_grade, dev["grade"],
                                    GRADE_WARD),
          dev["grade"] <= GRADE_WARD, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E2
    section("E2 -- the big-frame floor census (measured; a "
            "certified floor is a separate future object)")
    fl = np.array([r["rec"]["floor"] / r["tau"] for r in live])
    vc = np.array([r["rec"]["floor"] / r["lam1"] for r in live])
    hs = np.array([float(r["h"]) for r in live])
    _a, sl_f, r2_f = ols_line(np.log(hs), np.log(fl))
    i90 = [i for i, r in enumerate(live) if r["kz"] == 90
           and r["src"] == "dep"]
    print("    floor/tau min/med/max = %.4f/%.4f/%.4f; slope vs "
          "log h %+.3f (R2 %.2f)"
          % (float(fl.min()), float(np.median(fl)),
             float(fl.max()), sl_f, r2_f))
    print("    v_sm cost floor/lam_1 min/med/max = %.4f/%.4f/"
          "%.4f" % (float(vc.min()), float(np.median(vc)),
                    float(vc.max())))
    if i90:
        print("    kz-90 exception: floor/tau = %.4f (gap ratio "
              "%.4f) -- reported honestly"
              % (fl[i90[0]], live[i90[0]]["lam1"]
                 / live[i90[0]]["tau"]))
    floor_o1 = (float(fl.min()) >= 1.0 - 1e-6
                and abs(sl_f) <= SLOPE_PASS)
    fl_lab = (("FLOOR-O1(min %.3f, med %.3f, slope %+.3f)"
               if floor_o1 else
               "FLOOR-DRIFTS(min %.3f, med %.3f, slope %+.3f)")
              % (float(fl.min()), float(np.median(fl)), sl_f))
    check("E2 typed: %s + VSM-COST(min %.3f, med %.3f)"
          % (fl_lab, float(vc.min()), float(np.median(vc))), True)

    # ----------------------------------------------------------- E3
    section("E3 -- THE k* LADDER over %d rungs (h %d..%d, the "
            "boundedness measurement)" % (len(live),
                                          live[0]["h"],
                                          live[-1]["h"]))
    kh = [r["rec"]["khalf"] for r in live]
    n_inf = sum(1 for k in kh if k is None)
    reach = [(r, k) for r, k in zip(live, kh) if k is not None]
    cen_all, cen_dep, cen_deep = {}, {}, {}
    for r, k in reach:
        cen_all[k] = cen_all.get(k, 0) + 1
        d = cen_dep if r["src"] == "dep" else cen_deep
        d[k] = d.get(k, 0) + 1
    print("    census (all):      %s" % dict(sorted(
        cen_all.items())))
    print("    census (deployed): %s" % dict(sorted(
        cen_dep.items())))
    print("    census (deep):     %s" % dict(sorted(
        cen_deep.items())))
    if reach:
        kv = np.array([float(k) for _r, k in reach])
        hv = np.array([float(r["h"]) for r, _k in reach])
        _a, sl_k, r2_k = ols_line(np.log(hv), kv)
    else:
        kv = np.array([])
        sl_k = r2_k = float("nan")
    if n_inf == 0:
        kst = ("KSTAR-BOUNDED(max=%d, med=%.1f over h %d..%d = "
               "20x, slope vs log h %+.3f R2 %.2f)"
               % (int(kv.max()), float(np.median(kv)),
                  live[0]["h"], live[-1]["h"], sl_k, r2_k))
    else:
        infl = [r for r, k in zip(live, kh) if k is None]
        kst = ("KSTAR-NOT-REACHED(%d of %d: %s)"
               % (n_inf, len(live),
                  ", ".join("kz%d/h%d" % (r["kz"], r["h"])
                            for r in infl[:6])))
    ke = [r["rec"]["kext"] for r in live]
    n_inf_e = sum(1 for k in ke if k is None)
    reach_e = [(r, k) for r, k in zip(live, ke)
               if k is not None]
    if reach_e:
        kev = np.array([float(k) for _r, k in reach_e])
        hev = np.array([float(r["h"]) for r, _k in reach_e])
        _a, sl_e, r2_e = ols_line(np.log(hev), kev)
        _a, sl_p, r2_p = ols_line(np.log(hev), np.log(kev))
        ext_lab = ("EXT-LADDER(k <= %d Radau-only: reached %d/%d,"
                   " med %.0f, max %.0f; kext ~ %+.1f log h (R2 "
                   "%.2f), power-law exponent %+.2f (R2 %.2f))"
                   % (K_EXT, len(reach_e), len(live),
                      float(np.median(kev)), float(kev.max()),
                      sl_e, r2_e, sl_p, r2_p))
        for srcnm in ("dep", "deep"):
            sel = [k for r, k in reach_e if r["src"] == srcnm]
            inf_s = sum(1 for r, k in zip(live, ke)
                        if r["src"] == srcnm and k is None)
            if sel:
                print("    extended census (%s): min/med/max "
                      "%d/%.0f/%d, INF %d"
                      % (srcnm, int(min(sel)),
                         float(np.median(sel)), int(max(sel)),
                         inf_s))
    else:
        ext_lab = "EXT-LADDER(reached 0)"
    print("    %s" % ext_lab)
    print("\n    bracket width med (R_k - G_k)/q per k:")
    for k in KTAB:
        wid = [(r["rec"]["R"][k - 1] - r["rec"]["G"][k - 1])
               / max(abs(r["rec"]["q"]), 1e-300) for r in live]
        print("      k=%2d: %.3e" % (k, float(np.median(wid))))
    hm_pos = [r["hm"] for r in live if r["hm"] > 0]
    tau_pos = [r["tau"] for r in live if r["hm"] > 0]
    scr_l, _sl = (screen(hm_pos, tau_pos) if hm_pos
                  else ("vacuous(pos=0)", float("nan")))
    check("E3 typed: %s; %s; half-margin@k* tau-screen %s"
          % (kst, ext_lab, scr_l), True)

    # ----------------------------------------------------------- E4
    section("E4 -- b-normalization anatomy: what organizes k* "
            "(extended ladder, declared)")
    if reach_e and len(set(int(k) for _r, k in reach_e)) > 1:
        y = np.array([float(k) for _r, k in reach_e])
        cov = {
            "log |b|/tau": np.log(np.array(
                [r["rec"]["bnorm"] / r["tau"]
                 for r, _k in reach_e])),
            "log |b|/n": np.log(np.array(
                [r["rec"]["bnorm"] / r["rec"]["n"]
                 for r, _k in reach_e])),
            "log h": np.log(np.array(
                [float(r["h"]) for r, _k in reach_e])),
            "alpha": np.array(
                [r["alpha"] for r, _k in reach_e]),
            "log tau": np.log(np.array(
                [r["tau"] for r, _k in reach_e])),
        }
        best = (None, -1.0)
        for nm, xv in cov.items():
            _a, sl_v, r2_v = ols_line(xv, y)
            print("    k*_ext vs %-11s: slope %+.4f  R2 %.4f"
                  % (nm, sl_v, r2_v))
            if np.isfinite(r2_v) and r2_v > best[1]:
                best = (nm, r2_v)
        org = "ORGANIZER(%s, R2 %.3f)" % best
    else:
        org = ("ORGANIZER-DEGENERATE(k*_ext constant at %s on "
               "the reached subset -- no variance to organize)"
               % (reach_e[0][1] if reach_e else "-"))
        print("    k*_ext has no variance across the reached "
              "subset; regression degenerate (recorded).")
    bt = sorted(live, key=lambda r: -r["rec"]["bnorm"]
                / r["tau"])[:5]
    kt = sorted(live, key=lambda r: -(r["rec"]["kext"]
                                      or K_EXT + 1))[:5]
    n_ovl = len({r["kz"] for r in bt} & {r["kz"] for r in kt})
    print("    top-5 |b|/tau rungs:  %s"
          % [(r["kz"], r["h"]) for r in bt])
    print("    top-5 k*_ext rungs:   %s (overlap %d/5; only "
          "meaningful if k* varies)"
          % ([(r["kz"], r["h"]) for r in kt], n_ovl))
    check("E4 typed: %s; top-5 |b| vs top-5 k* overlap %d/5"
          % (org, n_ovl), True)

    # ----------------------------------------------------------- E5
    section("E5 -- moment anatomy / obstruction")
    small = (n_inf == 0 and all(k <= KSTAR_SMALL
                                for _r, k in reach))
    reps = [live[0], live[len(live) // 2], live[-1]]
    if small:
        kprint = int(min(np.median([k for _r, k in reach]),
                         KSTAR_SMALL))
        for r in reps:
            print("\n    representative %s kz %d h %d (k*_half "
                  "%s): moments m_j = b^T B^j b, j = 0..%d, with "
                  "grid-quartile shares [q1|q2|q3|q4]:"
                  % (r["src"], r["kz"], r["h"],
                     r["rec"]["khalf"], 2 * kprint))
            for j in range(2 * kprint + 1):
                mj = r["rec"]["moms"][j]
                sh = r["rec"]["shares"][j]
                print("      m_%-2d = %+.6e   [%s]"
                      % (j, mj,
                         " | ".join("%+.2e" % s for s in sh)),
                      flush=True)
        mom_lab = ("MOMENTS-REDUCED(k* <= %d on %d/%d: per rung "
                   "the wall demand reduces to <= %d source-only "
                   "moments b^T B^j b + the measured floor)"
                   % (KSTAR_SMALL, len(live), len(live),
                      2 * KSTAR_SMALL + 1))
    else:
        if reach_e:
            _a, slg, r2g = ols_line(
                np.log(np.array([float(r["h"])
                                 for r, _k in reach_e])),
                np.array([float(k) for _r, k in reach_e]))
        else:
            slg = r2g = float("nan")
        for r in reps:
            print("\n    representative %s kz %d h %d deficit "
                  "(n - R_k - mu1/2)/tau vs k (extended "
                  "ladder):" % (r["src"], r["kz"], r["h"]))
            for k in KTAB_EXT:
                if k > r["rec"]["kcap"]:
                    break
                d = (r["rec"]["n"] - r["rec"]["R"][k - 1]
                     - 0.5 * r["mu1"]) / r["tau"]
                print("      k=%3d: %+.3e" % (k, d))
        mom_lab = ("OBSTRUCTION-LAW(k*_ext growth %+.1f per "
                   "log h, R2 %.2f; INF %d at k <= %d, %d at "
                   "k <= %d)"
                   % (slg, r2g, n_inf, K_MAX, n_inf_e, K_EXT))
    check("E5 typed: %s" % mom_lab, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    n_ref = 0
    for r in [x for x in rows if x["src"] == "dep"
              and x["kz"] in SUBSET]:
        ug, mg = smooth_comb(r["alpha"], r["M"])
        Ksm = wall_from(r["alpha"], r["M"], r["D"], ug, mg)
        vs = np.linalg.eigh(Ksm)[1][:, 0]
        _u, _n, _b, Bs = split_along(Ksm, vs)
        fs = float(np.linalg.eigvalsh(Bs)[0])
        fired = fs <= 0.0
        n_ref += int(fired)
        print("    smooth kz %3d: lam_min(K_sm) %+.3e, co-block "
              "floor %+.3e -> %s"
              % (r["kz"], r["lam_sm"], fs,
                 "REFUSES" if fired else "runs"), flush=True)
        del Ksm, Bs
    check("C1 WARD smooth floor refusal on %d/%d SUBSET rungs "
          "(no legal Radau node in the prime-free world)"
          % (n_ref, len(SUBSET)), n_ref == len(SUBSET),
          kill="K2")
    rr9 = core.build_window(CTRL_KZ)
    a9, M9, D9 = rr9["alpha"], rr9["M"], rr9["D"]
    ug9, mg9 = smooth_comb(a9, M9)
    Ksm9 = wall_from(a9, M9, D9, ug9, mg9)
    vsm9 = np.linalg.eigh(Ksm9)[1][:, 0]
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    K_E = wall_from(a9, M9, D9, np.log(nn.astype(float)),
                    2.0 * lamE[nn] / np.sqrt(nn.astype(float)))
    negE = int(np.sum(np.linalg.eigvalsh(K_E) < 0.0))
    _u, _n, _b, B_E = split_along(K_E, vsm9)
    fE = float(np.linalg.eigvalsh(B_E)[0])
    check("C2 WARD Epstein comb at kz %d: wall breaks (neg %d) "
          "and the split REFUSES (floor %+.3e <= 0)"
          % (CTRL_KZ, negE, fE), negE > 0 and fE <= 0.0,
          kill="K2")
    rngs = np.random.default_rng(SCRAMBLE_SEED)
    uu9 = np.asarray(rr9["uu"], float)
    mu9 = 2.0 * np.asarray(rr9["lam"], float)
    uus = np.sort(rngs.uniform(0.0, 2.0 * a9, size=len(uu9)))
    K_S = wall_from(a9, M9, D9, uus, mu9)
    negS = int(np.sum(np.linalg.eigvalsh(K_S) < 0.0))
    _u, _n, _b, B_S = split_along(K_S, vsm9)
    fS = float(np.linalg.eigvalsh(B_S)[0])
    check("C3 WARD scramble at kz %d: wall breaks (neg %d) and "
          "the split REFUSES (floor %+.3e <= 0)"
          % (CTRL_KZ, negS, fS), negS > 0 and fS <= 0.0,
          kill="K2")
    rsub = [r for r in rows if "rand" in r]
    kc = [float(r["rec"]["kext"] or K_EXT + 1) for r in rsub]
    kr = [float(K_EXT + 1) if r["rand"]["refused"]
          else float(r["rand"]["kext"] or K_EXT + 1)
          for r in rsub]
    med_c, med_r = float(np.median(kc)), float(np.median(kr))
    for r, a_, b_ in zip(rsub, kc, kr):
        print("    rand-dir %4s kz %3d h %5d: k*_ext classical "
              "%s vs random %s"
              % (r["src"], r["kz"], r["h"],
                 int(a_) if a_ <= K_EXT else "INF",
                 int(b_) if b_ <= K_EXT else "INF"), flush=True)
    if med_r > med_c:
        rand_lab = ("RAND-DEGRADES(med %g -> %g on %d rungs)"
                    % (med_c, med_r, len(rsub)))
    elif med_r == med_c:
        rand_lab = ("RAND-UNINFORMATIVE(med %g == %g -- at this "
                    "strength the control does not discriminate;"
                    " recorded per the frozen no-kill rule)"
                    % (med_c, med_r))
    else:
        rand_lab = ("RAND-BEATS-CLASSICAL(med %g < %g)"
                    % (med_r, med_c))
    check("C4 typed random-direction control: %s" % rand_lab,
          med_r >= med_c, kill="K2")

    labels = dict(
        fl=fl_lab, vc="VSM-COST(%.3f/%.3f)"
        % (float(vc.min()), float(np.median(vc))),
        kstar=kst, org=org, mom=mom_lab.split("(")[0],
        rand=rand_lab.split("(")[0], scr="SCREENS(%s)" % scr_l)
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DIRLANCZOSFF-MEASURED / %s / %s / %s / %s / "
                   "%s / %s / %s"
                   % (labels.get("fl", "-"),
                      labels.get("vc", "-"),
                      labels.get("kstar", "-"),
                      labels.get("org", "-"),
                      labels.get("mom", "-"),
                      labels.get("rand", "-"),
                      labels.get("scr", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): float-level MEASUREMENT probe on the
  float64-computed walls of the deployed 67-rung ladder and the
  extended 4e6-table holdout ladder.  The co-block floor is a
  measured float quantity consumed as the Radau/defect node; a
  CERTIFIED big-frame floor is a separate future object.  The k*
  ladder, floor census, organizer regression and moment anatomy
  are SURFACE measurements; they prove neither h-uniformity nor
  any tail statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
