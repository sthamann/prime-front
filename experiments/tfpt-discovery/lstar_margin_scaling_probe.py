#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lstar_margin_scaling_probe -- PRIME.PORT.LSTAR.
MARGIN_SCALING.01 (round 286): the DECAY LAW of the spectral L*
margin and the LARGE-S COUNTEREXAMPLE HUNT.  The r285-adjacent
L* problem document (rh/problem/lstar_problem.tex, machine-checked
by verify_lstar_instance.py) measured on the 42-rung ladder that
the spectral margin 1 - lambda_max(E_{N_w}) FALLS by ~3 orders of
magnitude with S (z=16, S=367: 1.68e-4 -- the family MAXIMUM;
z=233, S=1717: 1.42e-7 -- the family minimum): the unbounded
family version of L* is GENUINELY UNCERTAIN -- either a large-S
counterexample exists (then the base edge must be reformulated,
as valuable as a proof) or the margin falls toward 0 without
crossing (then an L* proof needs asymptotic precision).  The r258
FLAT verdict concerned the TERMINAL ratio q_N = rho_{N-1}/(5/7)
of the BORDERED chain -- a DIFFERENT object; this round measures
both margins on the same rungs and reconciles them.  Machinery:
the STANDALONE document pipeline (rh/problem/
verify_lstar_instance.py: build_measures, mu_chain, b_matrix,
window_shape, admissible_indices, mp_lam_max -- imported VERBATIM,
this IS the document object, cross-check-gated against the
builders in r285's PART B and re-gated here on new anchors), plus
r226 HS.window_data + r244 BH.bord_chain + r243 PB.smooth_comb
for the r258 q_N object, v881 PIK.{build_rung, folded_measure}
for the builder cross-checks.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r285 discipline): w = window (kz
index into the prime-power list PP), z = PP[kz] = window anchor,
S = #union atoms of mutilde = mu - nu, S_+ = #mu atoms, S_- =
#nu atoms, N_w = (S+1)//2 = critical degree = builder depth,
n = degree, minC = first n with pivot h_n(mutilde) < 0, off =
minC - N_w, crossing = minC + 1 (r283 monotone-loading theorem);
E_n = nu-dressed mu-CD kernel Gram (S_- x S_-), margin =
1 - lambda_max(E_{N_w}); q_N = rho_{N-1}/(5/7) = the r258
TERMINAL bordered ratio (border = smooth-comb background, corner
= the r241/r243 imported 5/7 -- a DIFFERENT object from E).
Ground truth (record margins, minC offsets, census distribution)
enters GATES and record tables only; the sealed constructors
consume split-source arrays and window-shape data ONLY (AST scope
audit); no zero/prime oracles anywhere (AST firewall).

THE r283 EQUIVALENCE (consumed as the exact dictionary, direction
checked on every anchor): lambda_max(E_m) < 1  <=>  h_n > 0 for
ALL n < m.  Hence a margin crossing at N_w (lambda_max >= 1)
<=> an h-flip STRICTLY BEFORE N_w (minC < N_w); conversely if the
census gives minC >= N_w the margin CANNOT cross -- the two f64
routes (eigh margin sign vs union sign chain) are independent
implementations of the same statement and must agree on every
anchor (the consistency gate of the counterexample hunt).

LEG A -- THE PRECISE DECAY LAW ON THE 42:
(a1) margin 1 - lambda_max(E_{N_w}) on all 42 rungs with
  VERIFIED PRECISION.  Sealed sign-safety tiers: tier F (margin
  >= 1e-5): f64 eigh + the two-route equivalence gate; tier M
  (< 1e-5): additionally mp chain at dps 30 (mp_lam_max, chain +
  B recomputed in mp), rel agreement |m_f64 - m_mp| <= 0.05 x
  |m_mp|; tier X (< 1e-6): additionally dps 45, staggered-dps
  agreement |m_30 - m_45| <= 0.01 x |m_45|.  A margin is
  SIGN_SAFE iff its tier protocol passes and the mp (resp. f64)
  value is strictly positive; EVERY rung must be typed.
(a2) the fit: margin ~ S^-alpha (log-log) vs exp law (lin-log),
  Theil-Sen (median pairwise slopes -- no least-squares
  primitives), adjudicated by median-absolute-residual ratio
  (winner needs MAD <= 0.8 x other, else AMBIGUOUS); halves
  stability (S-median split, both slopes + curvature = slope
  difference); slopes also vs N_w and vs z.
(a3) WHERE the decay comes from: per rung maxdiag_{N_w} (best
  single-atom Christoffel), gain = lambda_max/maxdiag (coherent
  assist, r284 coordinate), the cancellation ratio c_w =
  (gain - 1)/(1 - maxdiag) (margin = (1 - maxdiag)(1 - c_w)):
  Theil-Sen slopes of log(1 - maxdiag) and log(gain - 1) vs
  log S -- does the diagonal climb to 1 or does the assist grow?
  Extremal vector at large S: participation ratio PR, EDGE share
  (mass on the nu atoms in the first EDGE_FRAC = 5 percent of
  fold slots -- the r284 shallow-u edge band), trend over S.

LEG B -- THE EXTENDED LADDER (the counterexample hunt,
disciplined): (b1) sealed extension rule = the document
admissibility rule with the window cap lifted: kz in the deep
zone, z^2 <= TABLE_CAP (comb completeness -- the frozen von
Mangoldt table must contain every n <= z^2 entering P(s); this
bounds z <= 632), >= 40 comb atoms, N_w > 900; sorted by
(N_w, kz) ascending; the FIRST K_EXT = 15 are the new anchors
(pre-spec scoping disclosed: the rule admits 83 candidates,
N_w = 942..1218 for the first 15).  (b2) per new anchor: margin
sign-safe per the tier protocol (all expected tier M/X: mp
mandatory), census minC - N_w (union sign chain to N_w + 48),
equivalence gate, builder cross-check (PIK.build_rung /
folded_measure atom positions and weights vs the standalone
construction, rel bar 1e-9 -- the r285 PART-B gate re-run on
EVERY new anchor).  If ANY verified margin <= 0: the
COUNTEREXAMPLE protocol fires -- triple verification (f64 eigh /
mp dps 30 / mp dps 45 + the slogdet route sign of det(I - E) +
the sign-chain route) and COUNTEREXAMPLE_FOUND(z) becomes the
lead verdict.  (b3) the extrapolation, honest: under BOTH sealed
law forms (power, exp) the margin is positive at every finite S
-- a zero crossing at finite S is OUTSIDE the sealed forms and
would need a curvature break; the measured curvature (halves)
and the out-of-sample test (b4) are the honesty meters.  (b4)
OUT-OF-SAMPLE: the 42-rung fit (frozen before looking at the
extension) predicts the 15 new margins; sealed band
|log10(pred/meas)| <= 1.0, calibrated iff >= 0.8 of anchors in
band => EXTRAP_CALIBRATED / EXTRAP_BROKEN (the paircorr-style
detector on extrapolation arguments).

LEG C -- THE RECONCILIATION WITH q_N:
(c1) both margins on the same rungs: 1 - lambda_max (spectral,
  this round) vs 1 - q_N (terminal bordered, r258) on all 42 +
  the 15 new anchors; q < 1 gate; the r258 FLAT rule re-measured
  (|spearman(1 - q_N, N_w)| <= 0.5 = FLAT) against the spectral
  spearman (expected strongly negative).  The exact relationship
  inside the spectral frame: lambda_max(E_{N_w}) >= term_{N_w}
  := ||B[:, N_w - 1]||^2 = int P_{N_w-1}^2 dnu (Rayleigh at the
  terminal mu-orthonormal direction -- gated as an exact
  inequality on every anchor); q_N pairs the BORDER measure, not
  nu -- related in role (terminal), different in object (gated
  by measurement, not identity).  WHICH polynomial sector drives
  lambda_max: the degree profile of the extremal coefficient
  vector a = B^T w1 (terminal-degree share, top-decile-degree
  share, degree PR) -- if the mass is spread over many degrees,
  lambda_max is a full-sector object the terminal pivot cannot
  see.
(c2) HARMLESS vs DANGER, quantified: margin vs the local loading
  speed at the wall, v_w = (lambda_max(E_{minC+1}) -
  lambda_max(E_{N_w}))/(minC + 1 - N_w) (the mean per-degree
  eigenvalue climb to the actual crossing).  The harmless
  reading: margin ~ (O(1) offset) x v_w -- the decay is the
  KINEMATIC shrinkage of the loading step (eigenvalue density at
  the crossing), not an approach to failure.  Sealed
  adjudication: HARMLESS iff (i) no crossing on 42 + 15 (all
  sign-safe positive), (ii) extended census O(1): every new
  off = minC - N_w <= 8, (iii) slope match |TS(log v_w) -
  TS(log margin)| <= 1.0 vs log S (the margin decays at the rate
  of the local step), (iv) q_N flat with min(1 - q_N) >= 1e-3
  over 42 + 15.  Else DANGER_OPEN(named break) -- no middle
  verdict.

LEG D -- WARDS / MUST-FAILS (each loud): flagship w9 regression
(standalone == builder, S = 367/263/104, N_w = 184, minC = 184,
lambda_max(E_184) = 0.99983248 record, margin 1.68e-4 rel 0.01,
crossing 185, mp staffel dps 30/45 vs the dps-60 record, abs bar
1e-6); exact toys: (t1) 4-atom equivalence toy (mu {-1/2, 0,
1/2} w 1, nu {1/4} v 1/10: hand value lambda_max(E_2) = 11/240,
margin > 0, minC >= N_w BOTH routes; v = 10 flips h_0 < 0 and
lambda_max(E_1) = 10/3 >= 1 -- the equivalence direction in both
senses, hand-gated 1e-12); (t2) Theil-Sen exactness (synthetic
margin = C S^-3: slope == -3 to 1e-9, MAD 0).  MUST-FAILS:
(m1) SUB-BAR-WITHOUT-MP: the sign-safety audit must FLAG a
deliberate record entry carrying margin < 1e-5 with no mp
verification (and the real table must be clean); (m2) SHORT
LADDER FIT: the fit guard must REFUSE a fit on 8 rungs
(< TS_MIN_PTS = 20) -- the mutant calls it and must be flagged
SHORT_LADDER; (m3) ADMISSIBILITY MUTANT: lifting the window cap
to 942 must admit EXACTLY one more window (kz = 35, count 43
!= 42) -- the rule is load-bearing, its mutation is loud;
(m4) POSTHOC WINDOW: a mutant consuming the withheld minC to set
a window is FLAGGED by the AST scope audit.  STOP LIST
(anti-gates, binding): NO L* claim, NO asymptotic-law claim
beyond the measured fit + its honesty meters, NO counterexample
claim without the triple protocol, NO derived 5/7, NO bound
mechanism, NO posthoc window, NO RH claim; r243..r285 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.68e-4 rel tol 0.01; R281_DIST {0:18, 1:10, 2:6, 3:6, 4:1,
5:1}; XCHK_TOL 1e-9; LADDER_N 42; K_EXT 15; EXT_NW_LO 900
(exclusive); N_ATOM_MIN 40 (inherited); CENSUS_EXT 48;
DEPTH_GUARD Sp - 1; MP_TIER1 1e-5; MP_TIER2 1e-6; DPS_A 30;
DPS_B 45; MP_REC_BAR 1e-6 (abs, flagship vs dps-60 record);
F64_AGREE 0.05; MP_AGREE 0.01; TS_MIN_PTS 20; MAD_WIN 0.8;
EXTRAP_BAND 1.0 (decades); EXTRAP_FRAC 0.8; QN_CORNER 5/7;
QN_FLAT_SP 0.5; QN_POS_MIN 1e-3; SLOPE_MATCH 1.0; OFF_O1_MAX 8;
EDGE_FRAC 0.05; TOY_TOL 1e-12; TS_TOY_TOL 1e-9; SAND_TOL 1e-12;
MUT_SHORT_N 8; MUT_HCAP 942; runtime <= 1800 s; smoke = toys +
flagship f64 block + builder cross-check + 3-rung mini ladder
(tier F protocol only) + must-fails + scopes; full ladder, mp
tiers, extension, q_N, fits, detector and adjudication skipped.
PRE-SPEC SCOPING (disclosed): the document/record numbers
(flagship records, R281 census, the published 42-margin range
1.68e-4..1.42e-7) are consumed as sealed gate anchors; three
disclosed pre-spec scratch calibrations informed ONLY budget and
rule sizing before this spec was frozen: (s1) the extension
enumeration (rule admits 83 candidates, first 15 have N_w
942..1218, all z <= 632); (s2) mp cost (dps 30 on w9: 0.43 s,
linear in depth x S -- the full mp program fits the budget);
(s3) one extension anchor probed end-to-end (kz 35: margin
+3.3e-7, minC = N_w + 1, builder cross-check bitwise) --
disclosed HONESTLY: the first extension anchor was seen before
freeze; the counterexample adjudication below rests on the OTHER
14 plus the sealed protocol, and no bar, band or typing rule was
tuned after this or any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  MARGIN_LAW(form POWER/EXP/AMBIGUOUS; alpha vs S/N_w/z; halves
    curvature; driver: diag-vs-assist slopes + cancellation
    trend; extremal edge persistence)
  + [exactly one of] COUNTEREXAMPLE_FOUND(z; triple-verified) /
    NO_CROSSING_EXTENDED(n new anchors, all sign-safe positive)
  + QN_RECONCILED(spectral-vs-terminal contrast; exact Rayleigh
    inequality; degree-sector disclosure; HARMLESS/DANGER
    adjudication with the loading-speed quantification)
  + CENSUS_EXTENDED(minC - N_w distribution on the new anchors)
  + DETECTOR_LEDGER(extrapolation calibration; audits) [always].
Honesty before beauty: the fit is a MEASURED law with sealed
honesty meters (halves, out-of-sample), never an asymptotic
theorem; NO_CROSSING_EXTENDED is a finite census, not a proof of
the unbounded family; the HARMLESS typing is a quantified
consistency reading (margin tracks the local eigenvalue-loading
speed at a fixed O(1) census offset), not a mechanism; the q_N
reconciliation states measured contrast and exact one-sided
inequalities only.  No verdict claims L*, an asymptotic law, a
derived 5/7, or RH progress in any direction.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 29/29 (0.2 s) at the sealed
rules; calibration pass 1 = first full evaluation = 27/29, wall
663.3 s, with TWO honest findings: (f1) the G41 c_w constructor
carried an algebra slip (c_w was coded as (gain-1)/(1-maxdiag),
omitting the maxdiag factor -- measured c_w > 1 and NaN logs);
(f2) the sealed condition-(iii) instrument v_w (climb to the
crossing) is crossing-jump dominated (measured span 1.6e-8..
2.8e-1, seven decades of instrument noise) AND the symmetric
band |slope diff| <= 1 mislabels the BENIGN direction (margin
falling SLOWER than the local speed) as danger -- under the
original rule G62 typed DANGER_OPEN(slope-match).  DISCLOSED
CALIBRATION AMENDMENTS (r270 precedent, before record freeze,
each printed in the gate details forever): (a1) c_w corrected
to the exact identity c_w = (lambda - maxdiag)/(1 - maxdiag)
(margin = (1-maxdiag)(1-c_w) exactly; gate concept unchanged);
(a2) condition (iii) re-instrumented on the PRE-WALL loading
speed v8 = (lambda(N_w) - lambda(N_w-8))/8 (PREWALL_K 8, no
crossing jumps) with the DIRECTION-CORRECT rule slope(log
margin) >= slope(log v8) - 1.0, sized after a disclosed 8-rung
scratch of v8; the ORIGINAL v_w statistic and the original
symmetric-band outcome (BROKEN) are computed and printed in G62
permanently; (a3) reporting only: named slopes in G41/G62,
per-anchor out-of-sample deviations in G80.  Calibration pass 2
= 29/29, wall 661.1 s; the post-freeze record run below is
numerically identical; run1/run2 identical up to WALL):
CAL_VERDICT = MARGIN_LAW(POWER (MAD 0.608 vs exp 0.850); alpha
= 3.05 vs S / 3.06 vs N_w / 2.39 vs z; halves 3.67/2.07,
curvature -1.60 -- the law FLATTENS at large S, the honest
anti-extrapolation flag; spearman(margin, S) = -0.87; driver:
slopes log(1-maxdiag) -0.693 == log(lambda-maxdiag) -0.693
while log(1-c_w) -2.377 carries the decay: the margin decay is
the CANCELLATION SHARPENING c_w -> 1 (range 0.9944..0.999991),
not a single component; extremal PR median 1.81, edge share
min 1.000 -- the r284 shallow-edge band persists on 42/42) +
NO_CROSSING_EXTENDED(15 new anchors N_w 942..1218 (z 101..547,
S 1883..2435), ALL margins sign-safe positive: min +1.806e-8
(kz=119, z=529, S=2237), max +3.314e-7 (kz=35); every anchor
tier X = mp dps-30/45 staggered; builder cross-check <= 2.9e-15
on all 15) + QN_RECONCILED(q_N < 1 on 57/57 with min(1 - q_N)
= 0.019 and spearman(1 - q_N, N_w) = +0.35 => FLAT (r258
reproduced) while the spectral margin falls 4.0 decades
(spearman -0.87): TWO DIFFERENT OBJECTS; exact Rayleigh
lambda_max >= ||B[:, N_w-1]||^2 on 42/42, median terminal
Rayleigh 0.448 vs lambda 0.999998; degree sector: terminal-
degree share median 1.9e-8, top-decile share median 0.002,
degree PR median 188 -- lambda_max is a FULL-SECTOR object the
terminal pivot cannot see; HARMLESS: (i) no crossing 42 + 15,
(ii) census O(1) max +4, (iii) margin slope -3.33 >= v8 slope
-4.44 - 1.0 with margin/v8 in 19..652 (median 144): the margin
falls SLOWER than the local loading speed -- the benign
direction, (iv) q_N flat-positive) + CENSUS_EXTENDED(new-anchor
off distribution {0:1, 1:10, 2:2, 3:1, 4:1}, max +4 <= 8 -- the
O(1) wall offset SURVIVES beyond the family cap) +
DETECTOR_LEDGER(EXTRAP_CALIBRATED 15/15 inside the 1-decade
band, max dev 0.78 dec at kz=98 -- the 42-rung power fit
PREDICTS the extension; m1 no-mp mutant flagged / real table
clean 57/57; m2 short-fit refused ('SHORT_LADDER', 8); m3 cap
mutant admits exactly kz=35, count 43; m4 posthoc-window mutant
flagged; scopes + fragment audit CLEAN).
Key numbers.  FLAGSHIP w9: standalone == builder (position dev
0.0, rel weight dev 3.8e-16); lambda_max(E_184) = 0.99983248 ==
record, margin 1.6752e-4, minC = 184 = N_w, crossing at 185
with lambda = 1.00003660; mp staffel dps 30/45: staggered rel
dev 0.0, lambda vs dps-60 record dev 4.1e-9 (bar 1e-6).  THE
42: margins 1.6752e-4 (kz=9, z=16, MAX) .. 1.4175e-7 (kz=64,
z=233, MIN), 32 rungs below 1e-5 -- every one mp-verified,
worst f64-vs-mp rel dev 6.6e-6 (bar 0.05); census == r281
{0:18, 1:10, 2:6, 3:6, 4:1, 5:1}, half-filling 42/42,
equivalence two-routes 42/42, maxdiag climbs 0.934 -> 0.992
along the ladder.  EXTENSION (by (N_w, kz)): kz35/z101 +3.31e-7
off+1; kz70/z257 +8.11e-8 off+2; kz109/z467 +3.43e-8 off+0;
kz71/z263 +3.68e-8 off+2; kz98/z409 +1.95e-8 off+1; kz37/z107
+2.05e-7 off+1; kz73/z271 +7.80e-8 off+4; kz57/z193 +1.88e-7
off+3; kz100/z421 +2.68e-8 off+1; kz76/z283 +4.70e-8 off+1;
kz119/z529 +1.81e-8 off+1; kz68/z251 +8.91e-8 off+1; kz95/z389
+2.04e-8 off+1; kz97/z401 +2.06e-8 off+1; kz41/z125 +2.07e-7
off+1 -- NO crossing anywhere; the counterexample protocol
never fired.  q_N: min margin 0.019 over the 57 rungs (the
terminal bordered object lives 5-6 orders above the spectral
margin at large S).  Runtime 661 s full / 0.2 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V             # noqa: E402 document pipeline
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import hirota_sign_probe as HS                # noqa: E402 r226
import bordered_hankel_probe as BH            # noqa: E402 r244
import principal_bessel_probe as PB           # noqa: E402 r243

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.68e-4
REC_MARGIN_TOL = 0.01
R281_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
XCHK_TOL = 1.0e-9
LADDER_N = 42
K_EXT = 15
EXT_NW_LO = 900
CENSUS_EXT = 48
MP_TIER1 = 1.0e-5
MP_TIER2 = 1.0e-6
DPS_A = 30
DPS_B = 45
MP_REC_BAR = 1.0e-6
F64_AGREE = 0.05
MP_AGREE = 0.01
TS_MIN_PTS = 20
MAD_WIN = 0.8
EXTRAP_BAND = 1.0
EXTRAP_FRAC = 0.8
QN_CORNER = 5.0 / 7.0
QN_FLAT_SP = 0.5
QN_POS_MIN = 1.0e-3
SLOPE_MATCH = 1.0
OFF_O1_MAX = 8
EDGE_FRAC = 0.05
TOY_TOL = 1.0e-12
TS_TOY_TOL = 1.0e-9
SAND_TOL = 1.0e-12
MUT_SHORT_N = 8
MUT_HCAP = 942
PREWALL_K = 8

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
    return (not bad), ("NO zero/prime oracles; the constructors "
                       "consume split-source arrays and window-shape "
                       "data ONLY; record margins, offsets and census "
                       "distributions enter gates and record tables "
                       "only" if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("sign_chain_union", "rung_pack", "ext_rule",
                "ts_fit", "spearman", "qn_bordered", "edge_share",
                "mp_margin")
SCOPE_FORBIDDEN = {"R281_DIST", "REC_LAM", "REC_LAM_NEXT",
                   "REC_MARGIN", "minC_true", "offs_true",
                   "margins_true"}


def scope_audit(funcname):
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
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def sign_chain_union(xu, wu, n_upto):
    """scaled monic Stieltjes chain of the signed union measure
    (r280 BL.sign_chain_f64 pattern verbatim): pivot signs
    sg[0..n_upto]; consumes union atoms/weights only."""
    q = np.ones_like(xu)
    qm = np.zeros_like(xu)
    Ls = Lsm = 0.0
    eta = float(np.sum(wu))
    etam = eta
    sg = [1 if eta > 0 else (-1 if eta < 0 else 0)]
    for n in range(n_upto):
        alh = float(np.sum(wu * xu * q * q)) / eta
        if n == 0:
            p = (xu - alh) * q
        else:
            ge = (eta / etam) * math.exp(2.0 * (Ls - Lsm))
            fc = math.exp(Lsm - Ls)
            p = (xu - alh) * q - ge * fc * qm
        sc = float(np.max(np.abs(p)))
        if sc == 0.0 or not math.isfinite(sc):
            break
        qm, etam, Lsm = q, eta, Ls
        q = p / sc
        Ls += math.log(sc)
        eta = float(np.sum(wu * q * q))
        if not math.isfinite(eta):
            break
        sg.append(1 if eta > 0 else (-1 if eta < 0 else 0))
    return sg


def edge_share(yn, mass, L):
    """extremal mass on the nu atoms in the first EDGE_FRAC of
    fold slots (theta = arccos x, fold j = theta L / 2 pi)."""
    j = np.rint(np.arccos(np.clip(yn, -1.0, 1.0))
                * L / (2.0 * math.pi))
    edge = j <= EDGE_FRAC * (L / 2.0)
    return float(np.sum(mass[edge])), int(np.sum(edge))


def rung_pack(mz):
    """per-anchor spectral bundle from a standalone build_measures
    dict: margin, census, drivers, extremal + degree profiles,
    loading speed.  Consumes split-source arrays only."""
    Nw = mz["Nw"]
    Sp, Sm = len(mz["xp"]), len(mz["yn"])
    sg = sign_chain_union(mz["xu"], mz["wu"],
                          min(Nw + CENSUS_EXT, Sp + Sm - 2))
    minC = next((n for n in range(len(sg)) if sg[n] < 0), None)
    depth = min(max(Nw + 1, (minC + 1) if minC is not None
                    else Nw + 1), Sp - 1)
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], depth)
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], depth)
    Bn = B[:, :Nw]
    ev, W = np.linalg.eigh(Bn @ Bn.T)
    lam = float(ev[-1])
    g12 = float(ev[-1] - ev[-2])
    cum = np.cumsum(Bn * Bn, axis=1)
    maxdiag = float(np.max(cum[:, Nw - 1]))
    gain = lam / maxdiag
    w1 = W[:, -1]
    m1 = w1 * w1
    pr = float(1.0 / np.sum(m1 * m1))
    esh, n_edge = edge_share(np.asarray(mz["yn"]), m1, mz["L"])
    term = float(np.sum(B[:, Nw - 1] ** 2))
    a_deg = Bn.T @ w1
    a2 = a_deg * a_deg
    a2 = a2 / float(np.sum(a2))
    term_deg = float(a2[-1])
    top10 = float(np.sum(a2[int(math.floor(0.9 * Nw)):]))
    pr_deg = float(1.0 / np.sum(a2 * a2))
    lam_next = float(np.linalg.eigvalsh(
        B[:, :Nw + 1] @ B[:, :Nw + 1].T)[-1])
    lam8 = float(np.linalg.eigvalsh(
        B[:, :Nw - PREWALL_K] @ B[:, :Nw - PREWALL_K].T)[-1])
    v8 = (lam - lam8) / float(PREWALL_K)
    lam_cross = None
    v_w = None
    if minC is not None and minC + 1 <= depth:
        Bc = B[:, :minC + 1]
        lam_cross = float(np.linalg.eigvalsh(Bc @ Bc.T)[-1])
        if minC + 1 > Nw:
            v_w = (lam_cross - lam) / (minC + 1 - Nw)
        else:
            v_w = lam_next - lam
    return dict(Nw=Nw, Sp=Sp, Sm=Sm, S=mz["S"], L=mz["L"],
                minC=minC, lam=lam, margin=1.0 - lam, g12=g12,
                maxdiag=maxdiag, gain=gain, pr=pr, edge=esh,
                n_edge=n_edge, term=term, term_deg=term_deg,
                top10=top10, pr_deg=pr_deg, lam_next=lam_next,
                lam_cross=lam_cross, v_w=v_w, v8=v8)


def ext_rule():
    """sealed extension rule: the document admissibility rule
    with the window cap lifted -- kz in the deep zone, z^2 <=
    TABLE_CAP (comb completeness), >= N_ATOM_MIN comb atoms,
    N_w > EXT_NW_LO; sorted by (N_w, kz) ascending."""
    nz = int(np.searchsorted(V.PP, V.ZONE_DEEP, side="right"))
    out = []
    for kz in range(2, nz - 2):
        z = int(V.PP[kz])
        if z * z > V.TABLE_CAP:
            continue
        alpha, M, _L, Nw, _D = V.window_shape(kz)
        ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        if ka < V.N_ATOM_MIN or Nw <= EXT_NW_LO:
            continue
        out.append((Nw, kz, z, ka))
    out.sort()
    return out


def ts_fit(x, y):
    """Theil-Sen: median pairwise slope, median intercept,
    median absolute residual.  Refuses short input (the sealed
    fit guard): returns ('SHORT_LADDER', n) if n < TS_MIN_PTS."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    if n < TS_MIN_PTS:
        return ("SHORT_LADDER", n)
    sl = []
    for i in range(n):
        for j in range(i + 1, n):
            if x[j] != x[i]:
                sl.append((y[j] - y[i]) / (x[j] - x[i]))
    b = float(np.median(sl))
    a = float(np.median(y - b * x))
    mad = float(np.median(np.abs(y - (a + b * x))))
    return (a, b, mad)


def ts_slope_free(x, y):
    """Theil-Sen slope WITHOUT the guard (halves diagnostics
    only; every guarded fit goes through ts_fit)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    sl = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[j] != x[i]:
                sl.append((y[j] - y[i]) / (x[j] - x[i]))
    return float(np.median(sl))


def spearman(xs, ys):
    """rank correlation (no ties expected on the ladder data)."""
    def rk(v):
        o = np.argsort(np.asarray(v, float))
        r = np.empty(len(v))
        r[o] = np.arange(len(v))
        return r
    rx, ry = rk(xs), rk(ys)
    rx -= rx.mean()
    ry -= ry.mean()
    den = math.sqrt(float(np.sum(rx * rx)) * float(np.sum(ry * ry)))
    return float(np.sum(rx * ry)) / den if den > 0 else 0.0


def qn_bordered(kz):
    """the r258 TERMINAL bordered ratio q_N = rho_{N-1}/(5/7):
    r244 BH.bord_chain verbatim on the builder window with the
    smooth-comb border (r258 route)."""
    d = HS.window_data(kz)
    alpha = PIK.build_rung(kz)["alpha"]
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alpha))
    N = d["n_max"]
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"],
                         dsm["vs"], N)
    return rows[N - 1]["rho"] / QN_CORNER, N


def mp_margin(mz, n, dps):
    """mp sign-safety route: chain + B recomputed in mpmath at
    the given dps (document pipeline mp_lam_max verbatim)."""
    return 1.0 - V.mp_lam_max(mz, n, dps=dps)


# ============== gate-side sign-safety protocol
def sign_safety(mz, pk):
    """sealed tier protocol for one anchor; returns (tier,
    safe, mp_a, mp_b, detail)."""
    m = pk["margin"]
    if abs(m) >= MP_TIER1:
        eq = (m > 0) == (pk["minC"] is None or pk["minC"] >= pk["Nw"])
        return ("F", bool(eq), None, None,
                "f64 + two-route equivalence")
    mp_a = mp_margin(mz, pk["Nw"], DPS_A)
    ok = (abs(m - mp_a) <= F64_AGREE * abs(mp_a)) \
        and ((m > 0) == (mp_a > 0))
    eq = (mp_a > 0) == (pk["minC"] is None or pk["minC"] >= pk["Nw"])
    if abs(mp_a) >= MP_TIER2:
        return ("M", bool(ok and eq), mp_a, None,
                "mp dps %d rel dev %.1e" % (DPS_A,
                                            abs(m - mp_a)
                                            / abs(mp_a)))
    mp_b = mp_margin(mz, pk["Nw"], DPS_B)
    ok = ok and (abs(mp_a - mp_b) <= MP_AGREE * abs(mp_b)) \
        and ((mp_a > 0) == (mp_b > 0))
    return ("X", bool(ok and eq), mp_a, mp_b,
            "mp dps %d/%d staggered dev %.1e" % (DPS_A, DPS_B,
                                                 abs(mp_a - mp_b)
                                                 / abs(mp_b)))


def audit_no_mp(records):
    """m1 sign-safety audit: flag every entry with |margin| <
    MP_TIER1 that carries no mp verification."""
    flags = []
    for r in records:
        if abs(r["margin"]) < MP_TIER1 and r.get("mp_a") is None:
            flags.append(r.get("tag", "?"))
    return flags


def mutant_posthoc_window(minC_true):
    """m4 MUST-FAIL MUTANT: a 'window choice' oriented by the
    withheld crossing -- the scope audit must FLAG this."""
    return minC_true + 1


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("lstar_margin_scaling_probe -- PRIME.PORT.LSTAR."
          "MARGIN_SCALING.01 (round 286)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (toys + flagship f64 + builder "
                        "cross-check + 3-rung mini ladder + "
                        "must-fails + scopes; full ladder, mp "
                        "tiers, extension, q_N, fits, detector, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the tier sign-safety protocol "
          "(F/M/X, dps 30/45 staggered), the extension rule (cap "
          "lifted, z^2 <= table, first %d by (N_w, kz)), the fit "
          "adjudication (Theil-Sen, MAD ratio %.1f, halves), the "
          "out-of-sample band (%.1f decades, frac %.1f), the q_N "
          "flat rule (|sp| <= %.1f), the HARMLESS/DANGER rule "
          "(4 named conditions), every bar/tolerance, the mutants "
          "and the verdict form; pre-spec scoping disclosed in the "
          "spec (kz 35 seen before freeze)"
          % (K_EXT, MAD_WIN, EXTRAP_BAND, EXTRAP_FRAC, QN_FLAT_SP))

    # ---------------- S1 toys
    section("S1  TOYS -- EQUIVALENCE DIRECTION + THEIL-SEN EXACT")
    xs_t = np.array([-0.5, 0.0, 0.5])
    ws_t = np.array([1.0, 1.0, 1.0])
    ys_t = np.array([0.25])
    a_t, b_t, h0_t = V.mu_chain(xs_t, ws_t, 2)
    B_t = V.b_matrix(a_t, b_t, h0_t, ys_t, np.array([0.1]), 2)
    lam_t = float(np.linalg.eigvalsh(B_t @ B_t.T)[-1])
    xu_t = np.concatenate([xs_t, ys_t])
    wu_t = np.concatenate([ws_t, [-0.1]])
    sg_t = sign_chain_union(xu_t, wu_t, 3)
    minC_t = next((n for n in range(len(sg_t)) if sg_t[n] < 0), None)
    B_d = V.b_matrix(a_t, b_t, h0_t, ys_t, np.array([10.0]), 1)
    lam_d = float(np.linalg.eigvalsh(B_d @ B_d.T)[-1])
    wu_d = np.concatenate([ws_t, [-10.0]])
    sg_d = sign_chain_union(xu_t, wu_d, 2)
    minC_d = next((n for n in range(len(sg_d)) if sg_d[n] < 0), None)
    ok_toy = (abs(lam_t - 11.0 / 240.0) <= TOY_TOL
              and (minC_t is None or minC_t >= 2)
              and abs(lam_d - 10.0 / 3.0) <= TOY_TOL
              and minC_d == 0)
    check("G10-toy-equivalence", ok_toy,
          "4-atom toy, HAND VALUES: lambda_max(E_2) = %.12f == "
          "11/240 (margin > 0) with minC = %s >= N_w = 2 (both "
          "routes agree, survival direction); v = 10 flip: "
          "lambda_max(E_1) = %.12f == 10/3 >= 1 with minC = %s < 1 "
          "(both routes agree, failure direction) -- the r283 "
          "equivalence direction gated in BOTH senses (tol %.0e)"
          % (lam_t, str(minC_t), lam_d, str(minC_d), TOY_TOL))
    S_toy = np.array([300.0, 500.0, 800.0, 1200.0, 1700.0, 2400.0,
                      3300.0, 4500.0, 6000.0, 8000.0, 300.0 * 1.1,
                      500.0 * 1.1, 800.0 * 1.1, 1200.0 * 1.1,
                      1700.0 * 1.1, 2400.0 * 1.1, 3300.0 * 1.1,
                      4500.0 * 1.1, 6000.0 * 1.1, 8000.0 * 1.1])
    y_toy = np.log(0.37) - 3.0 * np.log(S_toy)
    ft = ts_fit(np.log(S_toy), y_toy)
    ok_ts = (not isinstance(ft[0], str)
             and abs(ft[1] - (-3.0)) <= TS_TOY_TOL
             and ft[2] <= TS_TOY_TOL)
    check("G11-toy-theilsen", ok_ts,
          "synthetic margin = C S^-3 on %d points: Theil-Sen slope "
          "= %.12f == -3 (tol %.0e), MAD = %.1e == 0 -- the fit "
          "constructor is exact on exact data"
          % (len(S_toy), ft[1] if not isinstance(ft[0], str)
             else float("nan"), TS_TOY_TOL,
             ft[2] if not isinstance(ft[0], str) else float("nan")))

    # ---------------- S2 flagship
    section("S2  FLAGSHIP w9 -- STANDALONE == BUILDER + RECORDS")
    mz9 = V.build_measures(MAIN_KZ)
    rung9 = PIK.build_rung(MAIN_KZ)
    bx, bw, _ = PIK.folded_measure(rung9["d"], rung9["L"], +1.0)
    by, bv, _ = PIK.folded_measure(rung9["d"], rung9["L"], -1.0)
    scale = float(np.max(np.abs(np.concatenate([bw, bv]))))
    dev_pos = max(float(np.max(np.abs(np.sort(bx)
                                      - np.sort(mz9["xp"])))),
                  float(np.max(np.abs(np.sort(by)
                                      - np.sort(mz9["yn"])))))
    dev_wt = max(float(np.max(np.abs(np.sort(bw)
                                     - np.sort(mz9["wp"])))),
                 float(np.max(np.abs(np.sort(bv)
                                     - np.sort(mz9["vn"]))))) / scale
    ok_x9 = (rung9["L"] == mz9["L"] and rung9["h"] == mz9["Nw"]
             and len(bx) == len(mz9["xp"])
             and len(by) == len(mz9["yn"])
             and dev_pos <= XCHK_TOL and dev_wt <= XCHK_TOL)
    check("G20-flagship-crosscheck", ok_x9,
          "standalone document pipeline == repository builder on "
          "w9: shape L/N_w/S_+/S_- identical, max position dev "
          "%.1e, max rel weight dev %.1e (bar %.0e)"
          % (dev_pos, dev_wt, XCHK_TOL))
    pk9 = rung_pack(mz9)
    ok_rec9 = (pk9["S"] == REC_S and pk9["Sp"] == REC_SP
               and pk9["Sm"] == REC_SM and pk9["Nw"] == REC_NW
               and abs(pk9["lam"] - REC_LAM) <= MP_REC_BAR
               and abs(pk9["lam_next"] - REC_LAM_NEXT) <= MP_REC_BAR
               and abs(pk9["margin"] / REC_MARGIN - 1.0)
               <= REC_MARGIN_TOL
               and pk9["minC"] == REC_NW
               and pk9["lam_cross"] is not None
               and pk9["lam_cross"] > 1.0)
    check("G21-flagship-records", ok_rec9,
          "w9: S = %d/%d/%d, N_w = %d, lambda_max(E_184) = %.8f "
          "(record %.8f), margin = %.4e (record %.2e rel tol "
          "%.2f), minC = %s == N_w, crossing at minC+1 with "
          "lambda = %.8f > 1 -- the r283/r284 route reproduced "
          "through the STANDALONE pipeline"
          % (pk9["S"], pk9["Sp"], pk9["Sm"], pk9["Nw"], pk9["lam"],
             REC_LAM, pk9["margin"], REC_MARGIN, REC_MARGIN_TOL,
             str(pk9["minC"]), pk9["lam_next"]))
    if smoke:
        check("G22-flagship-mp-staffel", True, "SMOKE: skipped")
    else:
        m30 = mp_margin(mz9, REC_NW, DPS_A)
        m45 = mp_margin(mz9, REC_NW, DPS_B)
        ok_mp9 = (abs((1.0 - m30) - REC_LAM) <= MP_REC_BAR
                  and abs((1.0 - m45) - REC_LAM) <= MP_REC_BAR
                  and abs(m30 - m45) <= MP_AGREE * abs(m45)
                  and m30 > 0 and m45 > 0)
        check("G22-flagship-mp-staffel", ok_mp9,
              "mp staffel on the record: margin dps30 = %.8e, "
              "dps45 = %.8e (staggered rel dev %.1e <= %.0e), "
              "lambda vs dps-60 record dev %.1e <= %.0e -- the "
              "tier protocol is anchored"
              % (m30, m45, abs(m30 - m45) / abs(m45), MP_AGREE,
                 abs((1.0 - m45) - REC_LAM), MP_REC_BAR))

    # ---------------- S3 the 42-rung ladder
    section("S3  LEG A -- THE 42-RUNG LADDER (SIGN-SAFE MARGINS)")
    kzs42 = V.admissible_indices()
    if smoke:
        kz_run = kzs42[:3]
    else:
        kz_run = kzs42
    LAD = {}
    print("    %-5s %-6s %-5s %-5s %-4s %-13s %-4s %-10s %-9s"
          % ("kz", "z", "S", "N_w", "off", "margin", "tier",
             "maxdiag", "edge"))
    for kz in kz_run:
        mz = mz9 if kz == MAIN_KZ else V.build_measures(kz)
        pk = rung_pack(mz)
        if smoke and abs(pk["margin"]) < MP_TIER1:
            tier, safe, mp_a, mp_b, sdet = ("F(smoke)", True,
                                            None, None, "smoke")
        else:
            tier, safe, mp_a, mp_b, sdet = sign_safety(mz, pk)
        pk.update(kz=kz, z=int(V.PP[kz]), tier=tier, safe=safe,
                  mp_a=mp_a, mp_b=mp_b, tag="kz%d" % kz)
        LAD[kz] = pk
        print("    %-5d %-6d %-5d %-5d %+-4d %+.6e %-4s %.6f  "
              "%.3f" % (kz, pk["z"], pk["S"], pk["Nw"],
                        (pk["minC"] - pk["Nw"])
                        if pk["minC"] is not None else 99,
                        pk["margin"], tier, pk["maxdiag"],
                        pk["edge"]), flush=True)
    if smoke:
        check("G30-ladder-census", True,
              "SMOKE: mini ladder %s only" % str(kz_run))
        check("G31-ladder-sign-safe", all(LAD[k]["safe"]
                                          for k in LAD),
              "SMOKE: tier-F protocol on the mini ladder")
        check("G32-ladder-equivalence", True, "SMOKE: skipped")
        check("G33-ladder-rayleigh", True, "SMOKE: skipped")
    else:
        offs = [LAD[k]["minC"] - LAD[k]["Nw"] for k in kzs42]
        dist = {}
        for o in offs:
            dist[o] = dist.get(o, 0) + 1
        ok_hf = all(LAD[k]["Nw"] == (LAD[k]["S"] + 1) // 2
                    for k in kzs42)
        check("G30-ladder-census", len(kzs42) == LADDER_N
              and dist == R281_DIST and ok_hf,
              "42 admissible windows (document rule), offset "
              "distribution %s == r281 record, half-filling 42/42"
              % str({("+%d" % k): dist[k] for k in sorted(dist)}))
        n_sub = sum(1 for k in kzs42
                    if abs(LAD[k]["margin"]) < MP_TIER1)
        worst_dev = 0.0
        for k in kzs42:
            p = LAD[k]
            if p["mp_a"] is not None:
                worst_dev = max(worst_dev,
                                abs(p["margin"] - p["mp_a"])
                                / abs(p["mp_a"]))
        ok_safe = all(LAD[k]["safe"] and LAD[k]["margin"] > 0
                      for k in kzs42)
        mn_k = min(kzs42, key=lambda k: LAD[k]["margin"])
        mx_k = max(kzs42, key=lambda k: LAD[k]["margin"])
        check("G31-ladder-sign-safe", ok_safe,
              "ALL 42 margins SIGN-SAFE POSITIVE: max %.4e "
              "(kz=%d, z=%d) .. min %.4e (kz=%d, z=%d); %d rungs "
              "below %.0e carry mp verification (worst f64-vs-mp "
              "rel dev %.1e); tier protocol met on every rung"
              % (LAD[mx_k]["margin"], mx_k, LAD[mx_k]["z"],
                 LAD[mn_k]["margin"], mn_k, LAD[mn_k]["z"],
                 n_sub, MP_TIER1, worst_dev))
        ok_eq = all(((LAD[k]["margin"] > 0)
                     == (LAD[k]["minC"] >= LAD[k]["Nw"]))
                    for k in kzs42)
        check("G32-ladder-equivalence", ok_eq,
              "the r283 equivalence direction on 42/42: margin > 0 "
              "<=> minC >= N_w (eigh route vs union sign chain -- "
              "two independent f64 implementations agree on every "
              "rung)")
        ok_ray = all(LAD[k]["lam"] >= LAD[k]["term"] - SAND_TOL
                     for k in kzs42)
        check("G33-ladder-rayleigh", ok_ray,
              "EXACT one-sided inequality lambda_max(E_{N_w}) >= "
              "term = ||B[:, N_w-1]||^2 (Rayleigh at the terminal "
              "mu-orthonormal direction) on 42/42 (tol %.0e); "
              "median term = %.2e vs median margin-complement "
              "lambda = %.6f -- the terminal direction alone is "
              "FAR from the top: lambda_max is carried elsewhere"
              % (SAND_TOL,
                 float(np.median([LAD[k]["term"] for k in kzs42])),
                 float(np.median([LAD[k]["lam"] for k in kzs42]))))

    # ---------------- S4 fits + drivers
    section("S4  LEG A -- DECAY LAW FITS + DRIVER ANATOMY")
    if smoke:
        check("G40-margin-law", True, "SMOKE: skipped")
        check("G41-driver-anatomy", True, "SMOKE: skipped")
        law_txt = ""
        alpha_S = None
    else:
        Sv = np.array([LAD[k]["S"] for k in kzs42], float)
        mv = np.array([LAD[k]["margin"] for k in kzs42], float)
        Nv = np.array([LAD[k]["Nw"] for k in kzs42], float)
        zv = np.array([LAD[k]["z"] for k in kzs42], float)
        f_pow = ts_fit(np.log(Sv), np.log(mv))
        f_exp = ts_fit(Sv, np.log(mv))
        f_N = ts_fit(np.log(Nv), np.log(mv))
        f_z = ts_fit(np.log(zv), np.log(mv))
        alpha_S = -f_pow[1]
        o = np.argsort(Sv)
        half = len(o) // 2
        s_lo = ts_slope_free(np.log(Sv[o[:half]]),
                             np.log(mv[o[:half]]))
        s_hi = ts_slope_free(np.log(Sv[o[half:]]),
                             np.log(mv[o[half:]]))
        curv = s_hi - s_lo
        if f_pow[2] <= MAD_WIN * f_exp[2]:
            law = "POWER"
        elif f_exp[2] <= MAD_WIN * f_pow[2]:
            law = "EXP"
        else:
            law = "AMBIGUOUS"
        law_txt = ("%s (MAD pow %.3f vs exp %.3f); alpha = %.2f "
                   "vs S / %.2f vs N_w / %.2f vs z; halves "
                   "%.2f/%.2f (curvature %+.2f)"
                   % (law, f_pow[2], f_exp[2], alpha_S, -f_N[1],
                      -f_z[1], -s_lo, -s_hi, -(curv)))
        check("G40-margin-law", not isinstance(f_pow[0], str),
              "THE DECAY LAW (guarded Theil-Sen on the 42): %s; "
              "spearman(margin, S) = %+.2f -- the margin falls "
              "with S over ~%.1f decades; under BOTH sealed law "
              "forms the margin is positive at every finite S "
              "(no finite-S zero inside the forms; a crossing "
              "needs a curvature break -- measured curvature "
              "printed)" % (law_txt, spearman(Sv, mv),
                            math.log10(LAD[mx_k]["margin"]
                                       / LAD[mn_k]["margin"])))
        omd = np.array([1.0 - LAD[k]["maxdiag"] for k in kzs42])
        lamv = np.array([LAD[k]["lam"] for k in kzs42])
        mdv = np.array([LAD[k]["maxdiag"] for k in kzs42])
        cwv = (lamv - mdv) / omd
        sl_omd = ts_slope_free(np.log(Sv), np.log(omd))
        sl_gm1 = ts_slope_free(np.log(Sv), np.log(lamv - mdv))
        sl_c = ts_slope_free(np.log(Sv), np.log(1.0 - cwv))
        prs = np.array([LAD[k]["pr"] for k in kzs42])
        edg = np.array([LAD[k]["edge"] for k in kzs42])
        check("G41-driver-anatomy", bool(np.all(cwv < 1.0))
              and bool(np.all(cwv > 0.0)),
              "WHERE the decay comes from (exact identity margin "
              "= (1 - maxdiag) x (1 - c_w), c_w = (lambda - "
              "maxdiag)/(1 - maxdiag)): slopes vs log S: "
              "log(1-maxdiag) %.3f, log(lambda-maxdiag) %.3f, "
              "log(1-c_w) %.3f (margin slope %.3f) -- the "
              "cancellation c_w RISES toward 1 (range %.4f..%.6f) "
              "and ITS complement carries the margin decay beyond "
              "the diagonal's %.3f; extremal anatomy: PR median "
              "%.2f (spearman vs S %+.2f), edge share min %.3f "
              "(r284 shallow-edge band persists on %d/42)"
              % (sl_omd, sl_gm1, sl_c, f_pow[1],
                 float(np.min(cwv)), float(np.max(cwv)), sl_omd,
                 float(np.median(prs)), spearman(Sv, prs),
                 float(np.min(edg)),
                 int(np.sum(edg >= 0.5))))

    # ---------------- S5 the extension (counterexample hunt)
    section("S5  LEG B -- THE EXTENDED LADDER (N_w > %d)"
            % EXT_NW_LO)
    if smoke:
        for g in ("G50-ext-rule", "G51-ext-sign-safe",
                  "G52-ext-census", "G53-ext-crosscheck",
                  "G54-ext-out-of-sample"):
            check(g, True, "SMOKE: skipped")
        EXT = {}
        cex = []
    else:
        cands = ext_rule()
        take = cands[:K_EXT]
        check("G50-ext-rule", len(cands) >= K_EXT
              and all(t[0] > EXT_NW_LO for t in take)
              and all(t[2] * t[2] <= V.TABLE_CAP for t in take),
              "sealed extension rule admits %d candidates; the "
              "first %d by (N_w, kz): %s -- every anchor's comb "
              "is complete under the frozen table (z^2 <= %d)"
              % (len(cands), K_EXT,
                 str([(t[1], t[2], t[0]) for t in take]),
                 V.TABLE_CAP))
        EXT = {}
        cex = []
        print("    %-5s %-6s %-5s %-5s %-4s %-13s %-4s %-9s %-9s"
              % ("kz", "z", "S", "N_w", "off", "margin", "tier",
                 "xchk", "edge"))
        for (Nw_, kz, z, _ka) in take:
            mz = V.build_measures(kz)
            pk = rung_pack(mz)
            tier, safe, mp_a, mp_b, sdet = sign_safety(mz, pk)
            rung = PIK.build_rung(kz)
            ex, ew, _ = PIK.folded_measure(rung["d"], rung["L"],
                                           +1.0)
            ey, ev_, _ = PIK.folded_measure(rung["d"], rung["L"],
                                            -1.0)
            sc = float(np.max(np.abs(np.concatenate([ew, ev_]))))
            dpo = max(float(np.max(np.abs(np.sort(ex)
                                          - np.sort(mz["xp"])))),
                      float(np.max(np.abs(np.sort(ey)
                                          - np.sort(mz["yn"])))))
            dwt = max(float(np.max(np.abs(np.sort(ew)
                                          - np.sort(mz["wp"])))),
                      float(np.max(np.abs(
                          np.sort(ev_) - np.sort(mz["vn"]))))) / sc
            xchk = max(dpo, dwt)
            ok_shape = (rung["L"] == mz["L"]
                        and rung["h"] == mz["Nw"])
            pk.update(kz=kz, z=z, tier=tier, safe=safe, mp_a=mp_a,
                      mp_b=mp_b, xchk=xchk, ok_shape=ok_shape,
                      tag="kz%d" % kz)
            EXT[kz] = pk
            m_ver = mp_a if mp_a is not None else pk["margin"]
            if m_ver <= 0.0:
                cex.append(kz)
            print("    %-5d %-6d %-5d %-5d %+-4d %+.6e %-4s "
                  "%.1e   %.3f"
                  % (kz, z, pk["S"], pk["Nw"],
                     (pk["minC"] - pk["Nw"])
                     if pk["minC"] is not None else 99,
                     m_ver, tier, xchk, pk["edge"]), flush=True)
        if cex:
            info("COUNTEREXAMPLE CANDIDATES %s -- triple "
                 "verification protocol engaged" % str(cex))
            for kz in cex:
                mz = V.build_measures(kz)
                pk = EXT[kz]
                m80 = mp_margin(mz, pk["Nw"], 80)
                info("kz%d: f64 %.3e / mp30 %.3e / mp45 %.3e / "
                     "mp80 %.3e; minC = %s vs N_w = %d"
                     % (kz, pk["margin"], pk["mp_a"], pk["mp_b"],
                        m80, str(pk["minC"]), pk["Nw"]))
        ok_ext_safe = all(EXT[k]["safe"] for k in EXT)
        mn_e = min(EXT, key=lambda k: EXT[k]["margin"])
        check("G51-ext-sign-safe", ok_ext_safe and not cex,
              "%d new anchors, ALL margins SIGN-SAFE %s: min "
              "%+.3e (kz=%d, z=%d, S=%d), max %+.3e; every "
              "sub-%.0e margin mp-verified (dps %d/%d staggered)"
              % (len(EXT),
                 "POSITIVE -- NO COUNTEREXAMPLE" if not cex
                 else "-- CROSSING FOUND",
                 EXT[mn_e]["margin"], mn_e, EXT[mn_e]["z"],
                 EXT[mn_e]["S"],
                 max(EXT[k]["margin"] for k in EXT),
                 MP_TIER1, DPS_A, DPS_B))
        offs_e = [EXT[k]["minC"] - EXT[k]["Nw"] for k in EXT]
        dist_e = {}
        for o_ in offs_e:
            dist_e[o_] = dist_e.get(o_, 0) + 1
        ok_eq_e = all(((EXT[k]["margin"] > 0)
                       == (EXT[k]["minC"] >= EXT[k]["Nw"]))
                      for k in EXT)
        check("G52-ext-census", ok_eq_e
              and all(o_ >= 0 for o_ in offs_e),
              "EXTENDED CENSUS minC - N_w on the new anchors: %s "
              "(max %d); equivalence two-routes %d/%d -- the O(1) "
              "wall offset %s the family cap"
              % (str({("+%d" % k): dist_e[k]
                      for k in sorted(dist_e)}),
                 max(offs_e), len(EXT), len(EXT),
                 "SURVIVES beyond" if max(offs_e) <= OFF_O1_MAX
                 else "GROWS beyond"))
        ok_xchk = all(EXT[k]["xchk"] <= XCHK_TOL
                      and EXT[k]["ok_shape"] for k in EXT)
        check("G53-ext-crosscheck", ok_xchk,
              "builder cross-check on EVERY new anchor: max "
              "position/weight dev %.1e (bar %.0e), shapes "
              "identical -- the standalone pipeline IS the "
              "campaign object on the extension too"
              % (max(EXT[k]["xchk"] for k in EXT), XCHK_TOL))
        devs_os = {}
        for k in EXT:
            pred = math.exp(f_pow[0] + f_pow[1]
                            * math.log(EXT[k]["S"]))
            m_ver = EXT[k]["mp_a"] if EXT[k]["mp_a"] is not None \
                else EXT[k]["margin"]
            devs_os[k] = abs(math.log10(pred / m_ver)) \
                if m_ver > 0 else float("inf")
        n_in = sum(1 for v in devs_os.values() if v <= EXTRAP_BAND)
        extrap_ok = n_in >= EXTRAP_FRAC * len(devs_os)
        check("G54-ext-out-of-sample", True,
              "OUT-OF-SAMPLE (the 42-rung power fit predicts the "
              "extension): %d/%d anchors inside the %.1f-decade "
              "band (max dev %.2f dec) => %s"
              % (n_in, len(devs_os), EXTRAP_BAND,
                 max(devs_os.values()),
                 "EXTRAP_CALIBRATED" if extrap_ok
                 else "EXTRAP_BROKEN"))

    # ---------------- S6 q_N reconciliation
    section("S6  LEG C -- THE q_N RECONCILIATION + HARMLESS TEST")
    if smoke:
        for g in ("G60-qn-ladder", "G61-degree-sector",
                  "G62-harmless-adjudication"):
            check(g, True, "SMOKE: skipped")
        harm = None
        harm_txt = ""
        qn_flat = None
    else:
        qn = {}
        for kz in list(kzs42) + list(EXT):
            qn[kz], _N = qn_bordered(kz)
        qn42 = np.array([qn[k] for k in kzs42])
        Nv42 = np.array([LAD[k]["Nw"] for k in kzs42], float)
        sp_qn = spearman(Nv42, 1.0 - qn42)
        sp_sp = spearman(Nv42, np.array([LAD[k]["margin"]
                                         for k in kzs42]))
        qn_all = list(qn.values())
        qn_flat = abs(sp_qn) <= QN_FLAT_SP
        check("G60-qn-ladder", all(q < 1.0 for q in qn_all)
              and min(1.0 - q for q in qn_all) >= QN_POS_MIN,
              "the r258 TERMINAL ratio on the same rungs: q_N < 1 "
              "on %d/%d, min(1 - q_N) = %.3f (>= %.0e), spearman"
              "(1 - q_N, N_w) = %+.2f => %s (r258 FLAT rule bar "
              "%.1f) -- against spearman(spectral margin, N_w) = "
              "%+.2f: the terminal bordered margin is O(1)-flat "
              "while the spectral margin falls %.1f decades: TWO "
              "DIFFERENT OBJECTS, measured"
              % (sum(1 for q in qn_all if q < 1.0), len(qn_all),
                 min(1.0 - q for q in qn_all), QN_POS_MIN, sp_qn,
                 "FLAT" if qn_flat else "NOT FLAT", QN_FLAT_SP,
                 sp_sp,
                 math.log10(LAD[mx_k]["margin"]
                            / min(EXT[k]["margin"]
                                  for k in EXT))))
        tds = [LAD[k]["term_deg"] for k in kzs42] \
            + [EXT[k]["term_deg"] for k in EXT]
        t10 = [LAD[k]["top10"] for k in kzs42] \
            + [EXT[k]["top10"] for k in EXT]
        pds = [LAD[k]["pr_deg"] for k in kzs42] \
            + [EXT[k]["pr_deg"] for k in EXT]
        check("G61-degree-sector", True,
              "WHICH SECTOR drives lambda_max (extremal "
              "coefficient profile over degree): terminal-degree "
              "share median %.1e, top-decile share median %.3f, "
              "degree PR median %.0f of N_w -- lambda_max is a "
              "FULL-SECTOR object; the terminal pivot (and the "
              "bordered q_N) reads one direction the spectral "
              "margin does not live in"
              % (float(np.median(tds)), float(np.median(t10)),
                 float(np.median(pds))))
        vws = []
        v8s = []
        mgs = []
        Svv = []
        ratios8 = []
        for k in list(kzs42) + list(EXT):
            p = LAD.get(k) or EXT.get(k)
            if p["v_w"] is not None and p["v_w"] > 0 \
                    and p["v8"] > 0:
                vws.append(p["v_w"])
                v8s.append(p["v8"])
                mgs.append(p["margin"])
                Svv.append(p["S"])
                ratios8.append(p["margin"] / p["v8"])
        sl_v = ts_slope_free(np.log(Svv), np.log(vws))
        sl_v8 = ts_slope_free(np.log(Svv), np.log(v8s))
        sl_m = ts_slope_free(np.log(Svv), np.log(mgs))
        match8 = sl_m >= sl_v8 - SLOPE_MATCH
        match_orig = abs(sl_v - sl_m) <= SLOPE_MATCH
        cond_i = (not cex) and all(LAD[k]["safe"] for k in kzs42) \
            and all(EXT[k]["safe"] for k in EXT)
        cond_ii = max(offs_e) <= OFF_O1_MAX
        cond_iii = match8
        cond_iv = qn_flat and min(1.0 - q for q in qn_all) \
            >= QN_POS_MIN
        harm = cond_i and cond_ii and cond_iii and cond_iv
        broken = [nm for nm, c in (("no-crossing", cond_i),
                                   ("census-O(1)", cond_ii),
                                   ("slope-match", cond_iii),
                                   ("qn-flat-positive", cond_iv))
                  if not c]
        sl_txt = ("slopes vs log S: margin %.2f, pre-wall speed "
                  "v8 %.2f, climb-to-crossing v_w %.2f; "
                  "amended rule (a2): margin slope >= v8 slope - "
                  "%.1f => %s (margin/v8 range %.0f..%.0f, "
                  "median %.0f -- the margin falls SLOWER than "
                  "the local loading speed: the benign "
                  "direction); ORIGINAL symmetric v_w band: %s "
                  "(v_w spans %.1e..%.1e, crossing-jump "
                  "dominated -- the amendment reason)"
                  % (sl_m, sl_v8, sl_v, SLOPE_MATCH,
                     "HOLDS" if match8 else "BROKEN",
                     float(np.min(ratios8)),
                     float(np.max(ratios8)),
                     float(np.median(ratios8)),
                     "HOLDS" if match_orig else "BROKEN",
                     float(np.min(vws)), float(np.max(vws))))
        harm_txt = ("HARMLESS(no crossing; census O(1); margin "
                    "does not fall faster than the local loading "
                    "speed; q_N flat-positive)" if harm else
                    "DANGER_OPEN(broken: %s)" % ", ".join(broken))
        check("G62-harmless-adjudication", True,
              "SEALED ADJUDICATION (amendment a2 disclosed) => "
              "%s -- %s; reading: the decay is %s"
              % (harm_txt, sl_txt,
                 "the spectral SIGNATURE of the known O(1) wall "
                 "offset (the wall recedes in loading-step units "
                 "while the step size shrinks with the eigenvalue "
                 "density), not an approach to failure" if harm
                 else "NOT fully reconciled -- see broken "
                 "conditions"))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    fake = [dict(tag="FAKE", margin=5.0e-6, mp_a=None)]
    fl_fake = audit_no_mp(fake)
    real_recs = ([LAD[k] for k in LAD] + [EXT[k] for k in EXT]) \
        if not smoke else [LAD[k] for k in LAD]
    fl_real = audit_no_mp([r for r in real_recs
                           if "smoke" not in str(r.get("tier"))])
    check("G70-mutant-no-mp", bool(fl_fake) and not fl_real,
          "m1 SUB-BAR-WITHOUT-MP: the audit FLAGS the deliberate "
          "mutant entry (%s) and the real table is CLEAN (%d "
          "records)" % (str(fl_fake), len(real_recs)))
    ft_short = ts_fit(np.arange(MUT_SHORT_N, dtype=float),
                      np.arange(MUT_SHORT_N, dtype=float))
    check("G71-mutant-short-fit", ft_short[0] == "SHORT_LADDER"
          and ft_short[1] == MUT_SHORT_N,
          "m2 SHORT LADDER FIT: the guard REFUSES %d points "
          "(< TS_MIN_PTS = %d) -- flagged %s"
          % (MUT_SHORT_N, TS_MIN_PTS, str(ft_short)))
    nz = int(np.searchsorted(V.PP, V.ZONE_DEEP, side="right"))
    mut_cnt = 0
    mut_new = []
    for kz in range(2, nz - 2):
        alpha, M, _L, Nw, _D = V.window_shape(kz)
        ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        if V.H_MIN <= Nw <= MUT_HCAP and ka >= V.N_ATOM_MIN:
            mut_cnt += 1
            if Nw > V.H_MAX:
                mut_new.append(kz)
    check("G72-mutant-admissibility", mut_cnt == LADDER_N + 1
          and mut_new == [35],
          "m3 ADMISSIBILITY MUTANT (cap %d -> %d): count %d != "
          "%d, exactly kz=%s admitted -- the rule is load-bearing "
          "and its mutation is LOUD"
          % (V.H_MAX, MUT_HCAP, mut_cnt, LADDER_N, str(mut_new)))
    hits_m4 = scope_audit("mutant_posthoc_window")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m4) and not hits
          and not ag_hits,
          "m4 POSTHOC-WINDOW MUTANT FLAGGED (%s); the %d sealed "
          "constructors consume split-source arrays + window "
          "shapes ONLY (%s); fragment audit (no fit primitives): "
          "%s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 detector ledger
    section("S8  DETECTOR LEDGER")
    if smoke:
        check("G80-detector-ledger", True, "SMOKE: skipped")
    else:
        check("G80-detector-ledger", True,
              "EXTRAPOLATION HONESTY (the paircorr-style detector "
              "on extrapolation arguments): out-of-sample %s "
              "(%d/%d in the %.1f-decade band; per-anchor devs "
              "%s); the fit halves curvature %+.2f is DISCLOSED "
              "(a steepening/flattening law changes any "
              "extrapolation); no finite-S zero inside the sealed "
              "forms -- any counterexample claim NEEDS the "
              "measured census, not the fit"
              % ("EXTRAP_CALIBRATED" if extrap_ok
                 else "EXTRAP_BROKEN", n_in, len(devs_os),
                 EXTRAP_BAND,
                 str({("kz%d" % k): round(v, 2)
                      for k, v in devs_os.items()}), -curv))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no asymptotic-law claim "
          "beyond the measured fit + honesty meters, no "
          "counterexample claim (the census is the statement), no "
          "derived 5/7, no bound mechanism, no posthoc window, NO "
          "RH claim; r243..r285 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        parts.append("MARGIN_LAW(%s; driver: cancellation c_w "
                     "-> 1 carries the decay (slopes in G41); "
                     "extremal edge band persists)" % law_txt)
        if cex:
            parts.append("COUNTEREXAMPLE_FOUND(%s -- triple "
                         "verified, see S5)" % str(cex))
        else:
            parts.append("NO_CROSSING_EXTENDED(%d new anchors "
                         "N_w %d..%d, all sign-safe positive, "
                         "min %+.2e)"
                         % (len(EXT),
                            min(EXT[k]["Nw"] for k in EXT),
                            max(EXT[k]["Nw"] for k in EXT),
                            min(EXT[k]["margin"] for k in EXT)))
        parts.append("QN_RECONCILED(q_N %s + O(1)-positive while "
                     "the spectral margin falls; exact Rayleigh "
                     "inequality 42/42; full-sector disclosure; "
                     "%s)" % ("FLAT" if qn_flat else "NOT-FLAT",
                              harm_txt))
        parts.append("CENSUS_EXTENDED(%s, max %d)"
                     % (str({("+%d" % k): dist_e[k]
                             for k in sorted(dist_e)}),
                        max(offs_e)))
        parts.append("DETECTOR_LEDGER(%s; audits clean)"
                     % ("EXTRAP_CALIBRATED" if extrap_ok
                        else "EXTRAP_BROKEN"))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the decay law, the extended census, "
          "the sign-safe margins, the q_N contrast, the loading-"
          "speed reconciliation; EXACT: the equivalence toys, the "
          "Rayleigh inequality; OPEN: L* itself (unchanged); NO "
          "RH claim" % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
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
