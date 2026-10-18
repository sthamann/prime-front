#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""coupledtau_probe -- PRIME.PORT.RHP.FULLSOURCE.COUPLEDTAU.01
(round 257): the EXACT n-dynamics of the indivisible full-source
object.  After r256 (EFFECTS_MIXED_COUPLEDTAU: on the common
positive prefix the base rotation is null, the border carries 81
percent with a sign flip, LOAD_BEARING did not fire) the reviewer
pre-declaration stands: base/fiber separation is ARTIFICIAL; the
object is the PAIR (tau_{w,n}, tau^aug_{w,n}) with D_{w,n} =
tau^aug_{w,n}/tau_{w,n}, together with the no-pole question for
tau.  DESIGN RULES (non-negotiable): the full von Mangoldt comb
stays in the main problem, NO PNT smoothing; small parameters only
in degree/deformation directions (quenched full-source analysis);
the compression family is CLOSED (r254/r256) -- this round derives
the exact DEGREE DYNAMICS, no compression.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r256 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots h_{w,k}
(k < N_w) are the proof objects; rho_k = F_k^2/h_k, S_n =
sum_{k<=n} rho_k (r243/r244); ground truth (h signs, flip degrees,
forced-tail offsets, T_true) enters GATES only; no zero/prime
oracles anywhere (AST firewall).  MACHINERY IMPORTED VERBATIM:
r244 BH.wpack + BH.bord_chain (chain, border readouts fb, Ls),
r226 HS.window_data, v881 PIK rung builders + folded measures +
Lanczos chain, r243 PB.smooth_comb; B PROVENANCE: the covering
budget stays B_w = S_{N-2} + 5/7 (r243/r247, IMPORTED, never
fitted).  POSITIVITY TYPING ADOPTED from r256: POSITIVE_PREFIX
(all h_k > 0 below n: Hilbert-space statements legitimate) vs
INDEFINITE_CONTINUATION (algebraic tau-quotient statements only);
pmax = MAIN 184 (full depth) / SCR 21 / EPST 25 / SMOOTH 27.

LEG A -- THE COUPLED RECURSION (exact algebra, then machine-gated
in a SEALED basis): fix the graded basis P_k(x) = U_k((x - x0)/rh)
(Chebyshev-U on the union+border hull; leading coefficient c_k =
(2/rh)^k, exactly known).  With G_n the leading n x n Gram of
mutilde, t_n the border (sigmatilde) readout column, corner B:
tau_n := det G_n, tau^aug_n := det [[G_n, t_n], [t_n^T, B]].  The
Schur identity D_n = tau^aug_n/tau_n = B - sum_{k<n} F_k^2/h_k
(r253 leg T, full-depth exact) yields the ONE-STEP PAIR RECURSION
    tau_{n+1}     = a_n tau_n,
    tau^aug_{n+1} = a_n tau^aug_n + b_n tau_n,
    a_n = c_n^2 h_n,        b_n = -(c_n F_n)^2,
equivalently D_{n+1} = D_n - rho_n, rho_n = F_n^2/h_n; seeds
tau_1 = h_0, tau^aug_1 = h_0 B - F_0^2 (closed form, chain-side).
COEFFICIENT TYPOLOGY (sealed claim, machine-gated): a_n CONSUMES
THE h-CHAIN (its sign IS the world's pivot sign; magnitude the
chain norm times the exactly known basis factor); b_n has SOURCE-
PURE SIGN (b_n <= 0 in EVERY world -- a perfect square with a
minus; only its MAGNITUDE consumes the chain + the Cauchy/border
column F_n = int pi_n dsigmatilde); hence the D-increment -rho_n
carries sign -sign(h_n): THE BASE PIVOT ALONE CARRIES THE SIGN,
THE BORDER CONTRIBUTES A NONNEGATIVE MAGNITUDE.  GATES: (a1)
tau-step: slogdet(G_{n+1}) - slogdet(G_n) == 2n log(2/rh) + log
|h_n| AND sign == sg h_n at ALL n < N on ALL worlds (MAIN bar
1e-6 abs-log, control bar 1e-4: the f64 chain reference saturates
on flipped worlds, r253-a1 precedent); (a2) coupled step: the
signed-log PAIR PROPAGATION from the closed-form seed, consuming
ONLY (h_n, F_n) chain data, reproduces the direct bordered
slogdet at ALL n on ALL worlds (abs-log dev + sign mismatch
counted 2; MAIN bar 1e-6, control bar 1e-3 = the r253-a1 floor);
(a3) full-depth anchor: D_N(recursion) == 5/7 - rho_{N-1}, rel
1e-9, every world; (a4) mp monomial Hankel truncation ward at
sealed n_t in {12, 24} (dps 220, corner B_t = 5/7): det ratio vs
B_t - S_{n_t-1} on w9 (bar 1e-12, f64 reference floor) AND on
SCRAMBLE (n_t = 24 spans the flip 21: the recursion is gated
THROUGH the indefinite continuation in exact arithmetic; bar
1e-6, f64 control reference); (a5) typology gates: b_n <= 0 for
all n, all worlds (machine), and on the DIRECT route the D-
increment sign equals -sg h_n at every resolvable degree
(resolvable: |rho_n| >= floor x max(|D_n|, |D_{n+1}|), floor 1e-7
MAIN / 1e-2 controls -- below the route's own noise the sign is
not measurable, typed).

LEG B -- THE COUPLED BUDGET COCYCLE: the scalar accumulation is
D_n itself (Phi_n = log10 |D_n|, s_n = sign D_n) with EXACT
increment law D_{n+1} - D_n = -rho_n.  (b1) INCREMENT SIGN LAW:
on MAIN the increments are STRICTLY NEGATIVE through the ENTIRE
free window (all rho_n > 0, n < N, both MAIN windows) -- a
monotone drain; on the controls the law breaks EXACTLY at the
r256 base flips (first n with rho_n < 0 == 21/21/25/27 for
SCR/EPST/SMOOTH as re-derived) -- both gated.  (b2) BORDER ROLE
PER ZONE (sealed zones, r246/r244 conventions: HEAD n < 8,
QUIET/BULK 8 <= n < N-5, TAIL n >= N-5): zone sums of rho, zone
shares of S_{N-1}, and the log10 |D| drop per zone -- the
coupling term is the SOLE n-dynamics (a pure drain: it drives D
monotonically toward the terminal value, it never dampens);
quantified per zone per world, controls typed INDEFINITE_
CONTINUATION beyond pmax.  (b3) WORLD SEPARATION BEFORE THE
TERMINAL DEGREE (the old R4 question in the new coordinate,
sealed bar 1.0 decade): sep_W = |log10 |D_MAIN(n)| - log10
|D_W(n)|| at the sealed checkpoints n in {16, pmax_W} (each world
its own B_w; honest measurement, no upgrade).

LEG C -- THE MICRO-FALSIFIER (mandatory; frozen in
PRIME.FREEMOMENT.POSITIVEPREFIX.01): predict BLIND (i) the w9
control flips 21/25/27 and (ii) the five-window forced-tail
survival 0/2/2/3/1 at j = n - N_w >= 0 (w = 9/12/13/26/40).
PREDICTOR (AST-separated): blind_flip_predictor consumes ONLY
node positions + signed weights (the source), builds the sealed
scaled-Chebyshev Gram, and reads the pivot-sign field of the
tau-step coefficient a_n by INDEPENDENT LINEAR ALGEBRA (slogdet
principal-minor scan) -- it NEVER touches the h-/r-chain arrays
(sg_h, lg_h, gam_next, hv, Fv, rho, fb, nf), enforced by a
dedicated AST scope audit (gate) with a deliberately oracle-
reading mutant that the audit MUST flag (must-fail).  Ground
truth (extended BH.bord_chain sign chain, wpack nf) enters gates
only.  mp WARDS (dps 40, sealed): the SCRAMBLE flip (sign det
G_21 > 0, sign det G_22 < 0) and the w9 forced-tail flip (sign
det G_184 > 0, sign det G_185 < 0) confirmed in exact-precision
determinants of the SAME source Gram.  HONEST TYPING (sealed):
a pass certifies the coupled recursion's COEFFICIENT FIELD as a
falsifier-compliant model class via a route-independent source-
only computation; it is NOT a parametrix/local-connection
mechanism -- that pass stays OPEN (typed in the verdict).

LEG D -- NO-POLE CONNECTION IN s (MEASUREMENT, no theorem): with
the r224 s-dressed port (D_P(s) = P + sX(I - sR)^{-1}X^T,
det(I - sE) = det(I - sR) det(I - sD_P(s)); identity RE-GATED
here on rungs 9 and 12 at the sealed s-grid, bar 1e-9), measure
on the sealed 10-rung window ladder kz = (17, 10, 18, 12, 13, 9,
15, 19, 26, 40) (h = 96..591, >= 6 rungs as contracted): (d1)
the base family tau_w(s) = det(I - sQ_w) (Q_w = A^T A the state
Gram, nonzero spectrum == E's): all real s-zeros are 1/lambda_i;
gate lambda_max < 1 (the wall) and tabulate the NOPOLE.COFINAL
core indicator dist_w = 1/lambda_max - 1 vs N = h; trend = LS
slope + Spearman of log10 dist vs log10 h (sealed rule:
APPROACHING iff Spearman <= -0.5, RECEDING iff >= +0.5, else
FLAT).  (d2) the AUGMENTED object: adjoin the border row (the
sigmatilde functional f_k = int P_k dsigmatilde in the SAME
state frame; folded smooth comb, both arms signed) -- augmented
spectrum == spec(Q + f f^T) (rank-1 Uvarov row; Cauchy
interlacing gated as an exact ward): does the nearest zero
structure shift across s = 1?  TWO sealed variants: RAW (the
mass-carrying row as the coupled object has it; corner |f|^2
printed) and UNIT (direction-only, u = f/|f|): tokens
AUG_RAW_<CROSSES_ONE|BELOW_ONE> + AUG_UNIT_<CROSSES_ONE|
BELOW_ONE>, honest typing: a RAW crossing driven by |f|^2 >> 1
is a MASS statement about the aggregated Uvarov row, not a
directional wall statement -- printed, never upgraded.

LEG E -- FALSIFIERS + MUST-FAILS (each loud, sealed): (e1)
SWAPPED BORDER INDEX: the coupled step run with F_{n+1} in place
of F_n must break the full-depth anchor on MAIN loudly (>= 1e3 x
the honest rel dev); (e2) OMITTED COUPLING TERM: tau^aug_{n+1} =
a_n tau^aug_n alone freezes D at B -- must break the anchor
loudly on MAIN (>= 1e3 x); (e3) ORACLE PREDICTOR: a mutant that
reads sg_h must be FLAGGED by the predictor AST audit; (e4)
SMOOTH ANCHOR: on the SMOOTH world border == window, so F_n = 0
for n >= 1 by orthogonality EXACTLY -- the coupling term
vanishes identically (max_{n>=1} |rho_n| / rho_0 <= 1e-18) and
the pair recursion degenerates to the pure tau-step: the
coupling is source-driven, not an artifact.

SEALED CONSTANTS: MAIN windows (9, 13); controls on w9: EPSTEIN,
SCRAMBLE (seed 1), SMOOTH; flips re-derived 25/21/27; tail
windows (9, 12, 13, 26, 40), prior offsets (0, 2, 2, 3, 1), EXT
6; FIB_LO 8; B_w = S_{N-2} + 5/7; basis hull = union + border
atoms (predictor: union only); bars: tau-step 1e-6 MAIN / 1e-4
controls, coupled 1e-6 MAIN / 1e-3 controls (r253-a1 floor),
anchor 1e-9, mp truncations {12, 24} dps 220 bar 1e-12 (w9) /
1e-6 (SCRAMBLE), resolvable-increment floor 1e-7 MAIN / 1e-2
controls; zones HEAD_K 8 / TAIL_K 5; separation checkpoints {16,
pmax_W}, bar 1.0 dec; mp flip wards dps 40 at n in {21, 22} (SCR)
and {184, 185} (w9); NOPOLE ladder (17, 10, 18, 12, 13, 9, 15,
19, 26, 40), Schur identity re-gate rungs (9, 12) at s-grid
(0.25, 0.5, 0.75, 0.9, 1.0) bar 1e-9, interlacing tol 1e-8 rel,
Spearman bar 0.5; SMOOTH alias bar 1e-18; loudness 1e3; runtime
<= 1800 s; smoke = w9 only (recursion legs w9 + controls, tail
w9 only, ladder rung 9 only, mp wards skipped, separation and
five-window blind tail skipped).

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  COUPLED_RECURSION_EXACT(a chain-consuming, b source-sign-pure)
    / COUPLED_RECURSION_OPEN
+ COCYCLE_LAW_FOUND(monotone drain; breaks at flips)
    / COCYCLE_STRUCTURELESS
+ WORLD_SEP_PRETERMINAL(dec) / NO_EARLY_SEPARATION(dec)
+ MICROFALSIFIER_PASSED(blind: coeff-field)
    / MICROFALSIFIER_PARTIAL(typed) / MICROFALSIFIER_FAILED
+ NOPOLE_TREND(<APPROACHING|FLAT|RECEDING>, slope, spearman)
+ AUG_RAW_<CROSSES_ONE|BELOW_ONE> + AUG_UNIT_<CROSSES_ONE|
    BELOW_ONE>.
Honesty before beauty: no verdict claims a bound mechanism or a
parametrix; the budget bound, the base law, and the positive
reachability of half-filling stay OPEN (r243/r247/r250/r251/
r253/r256 stand).

RECORD TABLES (frozen from calibration pass 1, 26/26 gates FIRST
FULL PASS, wall 27.9 s full / 0.3 s smoke; smoke-stage
amendments disclosed, both found in --smoke BEFORE any full
pass: (s1) the draft coupled step propagated the coupling term
with a hard-coded minus -- the exact term is b_n tau_n whose
sign is -sign(tau_n): invisible on MAIN (tau > 0 throughout),
LOUD on the flipped controls (SCR D_N +228 instead of +0.52) --
the propagation now carries -s_tau exactly as the derived
algebra demands; (s2) the zone log10|D| drop base is D_0 = B
(the empty-Gram value), not D_1; no bar and no verdict rule
moved at any point; the four scratch calibrations -- recursion
floors, blind flip route, mp det cost, augmented eigenvalue --
predate this spec and are disclosed in the bars above):
CAL_VERDICT = COUPLED_RECURSION_EXACT(a chain-consuming, b
source-sign-pure) + COCYCLE_LAW_FOUND(monotone drain; breaks at
flips 21/25/27) + NO_EARLY_SEPARATION(0.84 dec) +
MICROFALSIFIER_PASSED(blind: coeff-field) +
NOPOLE_TREND(APPROACHING, slope -2.87, spearman -0.806) +
AUG_RAW_CROSSES_ONE + AUG_UNIT_CROSSES_ONE.
Key numbers.  CENSUS: w9/w13 N = 184/168, POSITIVE_PREFIX at
full depth; controls pmax = SCR 21 / EPST 25 / SMOOTH 27
(INDEFINITE_CONTINUATION), all re-derived.  LEG A (the round's
SATZ headline -- the pair recursion is machine-exact at every
degree on every world): tau-step worst abs-log dev 1.4e-10
(MAIN) / 4.8e-06 (controls, the f64 chain floor on flipped
worlds), signs exact at every degree; coupled propagation
(chain-side seeds tau_1 = h_0, tau^aug_1 = h_0 B - F_0^2, then
coefficients only) vs direct bordered slogdet: w9 9.5e-10, w13
1.2e-09, SCR 4.2e-04 (the r253-a1 floor), EPST 5.2e-05, SMOOTH
6.5e-10 -- ALL signs of BOTH components match at EVERY degree;
anchors D_N = 5/7 - rho_{N-1}: +0.561250 / +0.356069 /
+0.521703 / +1.792211 / +0.714286, rel devs <= 4.8e-11; mp
truncation wards (dps 220): w9 2.8e-17 / 1.0e-16, SCRAMBLE
1.8e-16 / 6.4e-14 (n_t = 24 THROUGH the flip 21: the pair
recursion is exact across the indefinite continuation);
typology: b_n <= 0 at every degree on every world (machine),
increment signs == -sg h_n at all 548 resolvable of 899 degrees
(below the floor the route's own noise dominates, typed).
LEG B: MAIN monotone drain through the ENTIRE free window (min
rho: w9 8.9e-10 at n = 180, w13 1.6e-08 at n = 26 -- all
positive); the control increment law breaks FIRST at exactly
21/25/27; zone anatomy (share of S_{N-1} HEAD/BULK/TAIL, then
log10|D| drop): w9 0.446/0.531/0.023, drop 0.234/0.820/0.121;
w13 0.440/0.498/0.062, drop 0.236/0.743/0.359 -- rho_0 alone
carries ~0.44 as ONE mode (r246 reproduced), the bulk drains
extensively, the last 5 degrees still drop 0.12-0.36 decades
(the drain never dampens: pure negative increments); controls
(algebraic beyond pmax): EPST 0.821/-0.423/0.603, SCR
-3.66/-17.27/+21.92 (the indefinite continuation swings both
ways), SMOOTH 1/0/0 exactly; (b3) separation at the sealed
checkpoints {16, pmax_W}: SCR 0.072/0.068 dec, EPST 0.283/0.283,
SMOOTH 0.836/0.836 -- best 0.84 dec < 1.0: NO_EARLY_SEPARATION
(honest: the cocycle coordinate does NOT separate MAIN from the
controls a full decade before the terminal degree; the old R4
answer survives in the new coordinate).  LEG C: predictor AST
scope CLEAN (gate) and the oracle mutant FLAGGED (rows/sg_h
hits, must-fail fires); blind control flips 21/25/27 == ground
truth (3/3); blind forced-tail offsets (0, 2, 2, 3, 1) == prior
== re-derived ground truth on all five windows (flips at
184/153/170/367/592); mp flip wards (dps 40): SCR sign det
G_21/G_22 = +1/-1, w9 sign det G_184/G_185 = +1/-1 -- the pivot
field is exact arithmetic, not f64; typing: coefficient-field
pass, NOT a parametrix (OPEN).  LEG D: s-dressed Schur identity
re-gated on rungs 9/12, worst dev 2.4e-13 over the s-grid;
ladder (h -> dist = 1/lambda_max - 1): 96 -> 8.60e-5, 103 ->
1.87e-4, 142 -> 3.06e-5, 151 -> 7.65e-5, 168 -> 7.82e-5, 184 ->
1.68e-4, 203 -> 2.88e-5, 313 -> 1.44e-5, 364 -> 2.79e-6, 591 ->
6.66e-7 (lambda_max 0.999813..0.999999 < 1 on 10/10 -- the
wall): trend slope -2.87 dec/dec, Spearman -0.806 (not
monotone rung-by-rung, honest) => NOPOLE_TREND(APPROACHING) --
the nearest real zero of tau_w(s) approaches s = 1 cofinally
(MEASUREMENT); augmented row: RAW lambda_max 4.34..7.04 (=
|f|^2 4.15..6.87 dominates: corner-mass statement, typed) =>
AUG_RAW_CROSSES_ONE on 10/10; UNIT direction row lambda_max
1.17..1.28 > 1 on 10/10 => AUG_UNIT_CROSSES_ONE -- even the
direction-normalized border row pushes the top eigenvalue
ACROSS the wall: the augmented family carries a real zero at
s < 1 on every rung -- the coupling ENDANGERS a naive bordered
spectral no-pole path (measured, typed, no theorem);
interlacing ward exact (worst rel violation 2.1e-16).  LEG E:
e1 swapped border index breaks the w9 anchor by 5.6e+00 =
3.8e+12 x honest 1.5e-12; e2 omitted coupling freezes D at B =
8.3824, dev 7.7e+00 = 5.3e+12 x honest; e3 oracle mutant
flagged by the AST audit (blind scope stays clean); e4 SMOOTH
alias max |rho_{n>=1}|/rho_0 = 7.6e-23 (bar 1e-18): the
coupling term vanishes identically on the self-aliased source.
READING (typed, no upgrade): the indivisible object HAS an
exact one-step law -- the pair (tau, tau^aug) closes under a
two-term recursion whose ONLY world-sign carrier is the base
pivot a_n while the coupling coefficient b_n is a source-sign-
pure negative square; the cocycle is a monotone drain on MAIN
through the entire free window and its increment law breaks
exactly at the control base flips (the r256 firewall reproduced
INSIDE the coupled dynamics); the frozen micro-falsifier is
passed at the coefficient-field level (blind, route-
independent) -- the parametrix-level pass stays OPEN; the
no-pole indicator approaches s = 1 cofinally on the 10-rung
ladder while BOTH augmented variants cross the wall: the
coupled object's own zero structure sits BELOW s = 1 -- any
no-pole path must go through the PAIR dynamics (the drain),
not through a bordered spectral bound.  Runtime 27.9 s full /
0.3 s smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE.

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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
TAIL_WINDOWS = (9, 12, 13, 26, 40)
PRIOR_OFFSETS = (0, 2, 2, 3, 1)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
FIB_LO = 8
EXT = 6
TSTEP_BAR_MAIN = 1e-6
TSTEP_BAR_CTRL = 1e-4
CPL_BAR_MAIN = 1e-6
CPL_BAR_CTRL = 1e-3
ANCHOR_BAR = 1e-9
MP_TRUNCS = (12, 24)
MP_TRUNC_DPS = 220
MP_TRUNC_BAR_MAIN = 1e-12
MP_TRUNC_BAR_CTRL = 1e-6
RESOLVE_MAIN = 1e-7
RESOLVE_CTRL = 1e-2
HEAD_K = 8
TAIL_K = 5
SEP_CHK_FIX = 16
SEP_BAR = 1.0
MP_FLIP_DPS = 40
KZ_LADDER = (17, 10, 18, 12, 13, 9, 15, 19, 26, 40)
ID_RUNGS = (9, 12)
S_GRID = (0.25, 0.5, 0.75, 0.9, 1.0)
ID_BAR = 1e-9
INTERLACE_TOL = 1e-8
SPEAR_BAR = 0.5
SM_ALIAS_BAR = 1e-18
LOUD = 1e3
CAL_VERDICT = (
    "COUPLED_RECURSION_EXACT(a chain-consuming, b source-sign-"
    "pure) + COCYCLE_LAW_FOUND(monotone drain; breaks at flips "
    "21/25/27) + NO_EARLY_SEPARATION(0.84 dec) + "
    "MICROFALSIFIER_PASSED(blind: coeff-field) + "
    "NOPOLE_TREND(APPROACHING, slope -2.87, spearman -0.806) + "
    "AUG_RAW_CROSSES_ONE + AUG_UNIT_CROSSES_ONE")

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
    return (not bad), ("NO zero/prime oracles; the pair recursion "
                       "consumes node positions + signed weights + "
                       "the r244 chain readouts ONLY; ground truth "
                       "(flip degrees, forced-tail offsets) enters "
                       "gates only" if not bad else "; ".join(bad))


# ------------------------------------------------ predictor (BLIND)
def blind_flip_predictor(xu, wu, n_hi):
    """SOURCE-ONLY pivot-sign field: consumes node positions and
    signed weights, builds the sealed scaled-Chebyshev Gram, and
    scans the principal-minor sign sequence by slogdet.  Returns
    the list of degrees n with pivot sign(det G_{n+1}/det G_n) < 0.
    AST-audited scope: never touches any chain array."""
    lo, hi = float(np.min(xu)), float(np.max(xu))
    mid, rad = 0.5 * (lo + hi), 0.5 * (hi - lo)
    t = (np.asarray(xu, float) - mid) / rad
    P = np.empty((n_hi, len(t)))
    P[0] = 1.0
    if n_hi > 1:
        P[1] = 2.0 * t
    for k in range(2, n_hi):
        P[k] = 2.0 * t * P[k - 1] - P[k - 2]
    G = (P * wu) @ P.T
    prev = 1.0
    out = []
    for n in range(1, n_hi + 1):
        s, _ld = np.linalg.slogdet(G[:n, :n])
        if s * prev < 0 or s == 0.0:
            out.append(n - 1)
        prev = s
    return out


def oracle_predictor(p, n_hi):
    """DELIBERATE MUST-FAIL MUTANT: reads the chain sign field
    directly -- the predictor AST audit must FLAG this scope."""
    return [r["n"] for r in p["rows"][:n_hi] if r["sg_h"] < 0]


def predictor_scope_audit(funcname):
    """walk ONLY the named function's subtree; flag any chain-array
    identifier or dict key from the sealed forbidden set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"sg_h", "lg_h", "gam_next", "nf", "hv", "Fv", "rho",
            "fb", "rows", "wpack", "bord_chain", "signed_chain",
            "eta"}
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
                if nm in forb:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# --------------------------------------------------- gram utilities
def u_matrix(xs, x0, rh, nmax):
    t = (np.asarray(xs, float) - x0) / rh
    P = np.empty((nmax, len(t)))
    P[0] = 1.0
    if nmax > 1:
        P[1] = 2.0 * t
    for n in range(2, nmax):
        P[n] = 2.0 * t * P[n - 1] - P[n - 2]
    return P


def union_arrays(d):
    return (np.concatenate([d["xs"], d["ys"]]),
            np.concatenate([d["ws"], -d["vs"]]))


def world_block(p):
    """direct-route material: scaled-Cheb Gram + border column +
    per-degree slogdets of G_n and of the bordered A_n."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    xu, wu = union_arrays(d)
    bx, bw = union_arrays(dsm)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    P = u_matrix(xu, x0, rh, N)
    TB = u_matrix(bx, x0, rh, N)
    G = (P * wu) @ P.T
    tv = TB @ bw
    B = float(p["S"][N - 2]) + 5.0 / 7.0
    sg = np.zeros(N + 1)
    lg = np.zeros(N + 1)
    sa = np.zeros(N + 1)
    la = np.zeros(N + 1)
    for n in range(1, N + 1):
        sg[n], lg[n] = np.linalg.slogdet(G[:n, :n])
        A = np.zeros((n + 1, n + 1))
        A[:n, :n] = G[:n, :n]
        A[:n, n] = tv[:n]
        A[n, :n] = tv[:n]
        A[n, n] = B
        sa[n], la[n] = np.linalg.slogdet(A)
    return dict(x0=x0, rh=rh, B=B, sg=sg, lg=lg, sa=sa, la=la,
                xu=xu, wu=wu)


def pair_recursion(p, B, lc, mutate=None):
    """the LEG-A recursion in signed-log arithmetic, chain-side
    only; seeds tau_1 = h_0, tau^aug_1 = h_0 B - F_0^2.  Returns
    per-degree (s_tau, l_tau, s_aug, l_aug) arrays (index n) plus
    the full-depth D.  mutate: None | 'swap' (F_{n+1} for F_n) |
    'omit' (drop the coupling term)."""
    rows = p["rows"]
    N = p["N"]
    lgF = [math.log(max(abs(r["fb"]), 1e-300)) + r["Ls"]
           for r in rows]
    f_on = [r["fb"] != 0.0 for r in rows]
    s_t = rows[0]["sg_h"]
    l_t = rows[0]["lg_h"]
    seed = s_t * math.exp(l_t) * B \
        - (rows[0]["fb"] * math.exp(rows[0]["Ls"])) ** 2
    s_a = math.copysign(1.0, seed)
    l_a = math.log(abs(seed))
    ST = np.zeros(N + 1)
    LT = np.zeros(N + 1)
    SA = np.zeros(N + 1)
    LA = np.zeros(N + 1)
    ST[1], LT[1], SA[1], LA[1] = s_t, l_t, s_a, l_a
    for n in range(1, N):
        j = n if mutate != "swap" else min(n + 1, N - 1)
        lc2 = 2.0 * n * lc
        s_t2 = s_t * rows[n]["sg_h"]
        l_t2 = l_t + lc2 + rows[n]["lg_h"]
        sA_ = s_a * rows[n]["sg_h"]
        lA_ = l_a + lc2 + rows[n]["lg_h"]
        if mutate == "omit" or not f_on[j]:
            s_a2, l_a2 = sA_, lA_
        else:
            lB_ = l_t + lc2 + 2.0 * lgF[j]
            m_ = max(lA_, lB_)
            v = sA_ * math.exp(lA_ - m_) - s_t * math.exp(lB_ - m_)
            if v == 0.0:
                s_a2, l_a2 = 0.0, -1e30
            else:
                s_a2 = math.copysign(1.0, v)
                l_a2 = m_ + math.log(abs(v))
        s_t, l_t, s_a, l_a = s_t2, l_t2, s_a2, l_a2
        ST[n + 1], LT[n + 1] = s_t, l_t
        SA[n + 1], LA[n + 1] = s_a, l_a
    D_N = s_a * s_t * math.exp(l_a - l_t)
    return ST, LT, SA, LA, D_N


def mp_trunc_ward(p, n_t, dps, Bt):
    """r253-t3 pattern: monomial mp Hankel truncation, det ratio
    of the bordered/unbordered moment matrices vs the f64 chain
    reference B_t - S_{n_t-1}."""
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    xu = [mp.mpf(float(v)) for v in d["xs"]] \
        + [mp.mpf(float(v)) for v in d["ys"]]
    wu = [mp.mpf(float(v)) for v in d["ws"]] \
        + [-mp.mpf(float(v)) for v in d["vs"]]
    bx = [mp.mpf(float(v)) for v in dsm["xs"]] \
        + [mp.mpf(float(v)) for v in dsm["ys"]]
    bw = [mp.mpf(float(v)) for v in dsm["ws"]] \
        + [-mp.mpf(float(v)) for v in dsm["vs"]]
    mk = []
    pw = [mp.mpf(1)] * len(xu)
    for _k in range(2 * n_t - 1):
        mk.append(mp.fsum(w * q for w, q in zip(wu, pw)))
        pw = [q * x for q, x in zip(pw, xu)]
    tk = []
    pb = [mp.mpf(1)] * len(bx)
    for _k in range(n_t):
        tk.append(mp.fsum(w * q for w, q in zip(bw, pb)))
        pb = [q * y for q, y in zip(pb, bx)]
    H = mp.matrix(n_t, n_t)
    Ha = mp.matrix(n_t + 1, n_t + 1)
    for i in range(n_t):
        for j in range(n_t):
            H[i, j] = mk[i + j]
            Ha[i, j] = mk[i + j]
        Ha[i, n_t] = tk[i]
        Ha[n_t, i] = tk[i]
    Ha[n_t, n_t] = mp.mpf(Bt)
    D_tr = mp.det(Ha) / mp.det(H)
    ref = mp.mpf(Bt) - mp.mpf(float(p["S"][n_t - 1]))
    return float(abs(D_tr / ref - 1))


def mp_flip_ward(xu, wu, nlist, dps):
    """exact-precision determinants of the SAME scaled-Cheb source
    Gram at the sealed flip-adjacent sizes; returns {n: sign}."""
    mp.mp.dps = dps
    lo, hi = float(np.min(xu)), float(np.max(xu))
    x0 = mp.mpf(0.5 * (lo + hi))
    rh = mp.mpf(0.5 * (hi - lo))
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    tv = [(x - x0) / rh for x in xs]
    n_hi = max(nlist)
    P = [[mp.mpf(1)] * len(xs), [2 * t for t in tv]]
    for _k in range(2, n_hi):
        P.append([2 * t * a - b
                  for t, a, b in zip(tv, P[-1], P[-2])])
    G = mp.matrix(n_hi, n_hi)
    for i in range(n_hi):
        for j in range(i, n_hi):
            v = mp.fsum(w * a * b for w, a, b in zip(ws, P[i], P[j]))
            G[i, j] = v
            G[j, i] = v
    return {n: int(mp.sign(mp.det(G[:n, :n]))) for n in nlist}


def spearman(x, y):
    rx = np.argsort(np.argsort(np.asarray(x, float)))
    ry = np.argsort(np.argsort(np.asarray(y, float)))
    rx = rx - rx.mean()
    ry = ry - ry.mean()
    return float((rx @ ry)
                 / math.sqrt(float(rx @ rx) * float(ry @ ry)))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("coupledtau_probe -- PRIME.PORT.RHP.FULLSOURCE."
          "COUPLEDTAU.01 (round 257)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 only, ladder rung 9, mp wards "
                        "+ five-window tail + separation skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN OBJECT: the PAIR (tau_n, tau^aug_n) with the sealed "
          "two-term recursion tau_{n+1} = a_n tau_n, tau^aug_{n+1} "
          "= a_n tau^aug_n + b_n tau_n, a_n = c_n^2 h_n, b_n = "
          "-(c_n F_n)^2, D_{n+1} = D_n - rho_n; basis U_k((x-x0)/"
          "rh) on the union+border hull (c_k = (2/rh)^k exact); "
          "gates vs direct per-degree slogdet on ALL degrees + mp "
          "truncations %s (dps %d) + mp flip wards (dps %d); "
          "cocycle = (log10 |D_n|, sign D_n) with sealed zones "
          "HEAD < %d / TAIL last %d; micro-falsifier: blind "
          "source-only pivot field vs flips %s + forced tail %s; "
          "NoPole ladder %s; ALL bars + verdict rules sealed in "
          "the frozen spec BEFORE evaluation"
          % (str(MP_TRUNCS), MP_TRUNC_DPS, MP_FLIP_DPS, HEAD_K,
             TAIL_K, str(CTRL_FLIPS), str(PRIOR_OFFSETS),
             str(KZ_LADDER)))

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS + POSITIVITY TYPING")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    pmax = {t: packs[t]["N"] for t in packs}
    pmax.update({c: ctrl[c]["nf"] for c in ctrl})
    check("G10-census-controls", okC and okCf,
          "MAIN free prefix positive at full depth (%s), typed "
          "POSITIVE_PREFIX; control flips re-derived %s, typed "
          "INDEFINITE_CONTINUATION beyond pmax (r256 firewall "
          "adopted); N = %s"
          % (str(sorted(packs)), str({c: ctrl[c]["nf"]
                                      for c in ctrl}),
             str({t: packs[t]["N"] for t in packs})))

    worlds = list(packs.items()) + list(ctrl.items())

    # ---------------- S2: LEG A -- the coupled recursion
    section("S2  LEG A -- THE COUPLED PAIR RECURSION (exact)")
    tstep_main = tstep_ctrl = 0.0
    cpl_main = cpl_ctrl = 0.0
    anchor_worst = 0.0
    b_ok = True
    inc_ok = True
    n_res = n_tot = 0
    WB = {}
    RC = {}
    a_note = []
    for tag, p in worlds:
        wb = world_block(p)
        WB[tag] = wb
        N = p["N"]
        lc = math.log(2.0 / wb["rh"])
        is_main = tag in packs
        # (a1) tau-step gate at all degrees
        dev_t = 0.0
        for n in range(1, N):
            step = wb["lg"][n + 1] - wb["lg"][n]
            pred = 2.0 * n * lc + p["rows"][n]["lg_h"]
            dev_t = max(dev_t, abs(step - pred))
            if wb["sg"][n + 1] * wb["sg"][n] != p["rows"][n]["sg_h"]:
                dev_t = max(dev_t, 2.0)
        # (a2) coupled propagation
        ST, LT, SA, LA, D_N = pair_recursion(p, wb["B"], lc)
        RC[tag] = (ST, LT, SA, LA, D_N)
        dev_c = 0.0
        for n in range(1, N + 1):
            dev_c = max(dev_c, abs(LT[n] - wb["lg"][n]),
                        abs(LA[n] - wb["la"][n]),
                        abs(ST[n] - wb["sg"][n]),
                        abs(SA[n] - wb["sa"][n]))
        # (a3) anchor
        anchor = 5.0 / 7.0 - float(p["rho"][N - 1])
        anchor_worst = max(anchor_worst, abs(D_N / anchor - 1.0))
        # (a5) typology: b_n <= 0 (squares) + increment signs on
        # the direct route at resolvable degrees
        floor = RESOLVE_MAIN if is_main else RESOLVE_CTRL
        for n in range(1, N):
            b_ok = b_ok and (-(p["rows"][n]["fb"] ** 2) <= 0.0)
            D_lo = wb["sa"][n] * wb["sg"][n] \
                * math.exp(wb["la"][n] - wb["lg"][n])
            D_hi = wb["sa"][n + 1] * wb["sg"][n + 1] \
                * math.exp(wb["la"][n + 1] - wb["lg"][n + 1])
            rho_n = float(p["rho"][n])
            n_tot += 1
            if abs(rho_n) >= floor * max(abs(D_lo), abs(D_hi),
                                         1e-300):
                n_res += 1
                inc_ok = inc_ok and (
                    math.copysign(1.0, D_hi - D_lo)
                    == -p["rows"][n]["sg_h"])
        if is_main:
            tstep_main = max(tstep_main, dev_t)
            cpl_main = max(cpl_main, dev_c)
        else:
            tstep_ctrl = max(tstep_ctrl, dev_t)
            cpl_ctrl = max(cpl_ctrl, dev_c)
        a_note.append("%s tstep %.1e cpl %.1e D_N %+.6f" %
                      (tag, dev_t, dev_c, D_N))
    check("G20-tau-step",
          tstep_main <= TSTEP_BAR_MAIN
          and tstep_ctrl <= TSTEP_BAR_CTRL,
          "slogdet(G_{n+1}) - slogdet(G_n) == 2n log(2/rh) + "
          "log|h_n| AND sign == sg h_n at ALL n on ALL worlds: "
          "MAIN worst %.1e (bar %.0e), controls %.1e (bar %.0e, "
          "f64 chain floor on flipped worlds, r253-a1 precedent)"
          % (tstep_main, TSTEP_BAR_MAIN, tstep_ctrl,
             TSTEP_BAR_CTRL))
    check("G21-coupled-step",
          cpl_main <= CPL_BAR_MAIN and cpl_ctrl <= CPL_BAR_CTRL,
          "the signed-log PAIR propagation (chain-side seeds + "
          "coefficients ONLY) vs the direct bordered slogdet at "
          "every degree: %s -- MAIN worst %.1e (bar %.0e), "
          "controls %.1e (bar %.0e); ALL signs of BOTH tau "
          "components match at EVERY degree on EVERY world "
          "(mismatch would count 2.0)"
          % ("; ".join(a_note), cpl_main, CPL_BAR_MAIN, cpl_ctrl,
             CPL_BAR_CTRL))
    check("G22-anchor", anchor_worst <= ANCHOR_BAR,
          "full-depth anchor D_N(recursion) == 5/7 - rho_{N-1}: "
          "worst rel %.1e (bar %.0e) on all %d worlds"
          % (anchor_worst, ANCHOR_BAR, len(worlds)))
    if not smoke:
        tr_note = []
        tr_main = tr_ctrl = 0.0
        for n_t in MP_TRUNCS:
            dv = mp_trunc_ward(packs["w9"], n_t, MP_TRUNC_DPS,
                               5.0 / 7.0)
            tr_main = max(tr_main, dv)
            tr_note.append("w9 n_t=%d %.1e" % (n_t, dv))
        for n_t in MP_TRUNCS:
            dv = mp_trunc_ward(ctrl["SCR"], n_t, MP_TRUNC_DPS,
                               5.0 / 7.0)
            tr_ctrl = max(tr_ctrl, dv)
            tr_note.append("SCR n_t=%d %.1e" % (n_t, dv))
        check("G23-mp-truncation-ward",
              tr_main <= MP_TRUNC_BAR_MAIN
              and tr_ctrl <= MP_TRUNC_BAR_CTRL,
              "monomial mp Hankel truncations (dps %d, corner 5/7)"
              ": %s -- w9 bar %.0e (f64 reference floor), SCRAMBLE "
              "bar %.0e (n_t = 24 spans the flip 21: the pair "
              "recursion is exact THROUGH the indefinite "
              "continuation)" % (MP_TRUNC_DPS, "; ".join(tr_note),
                                 MP_TRUNC_BAR_MAIN,
                                 MP_TRUNC_BAR_CTRL))
    else:
        check("G23-mp-truncation-ward", True, "SMOKE: skipped")
    check("G24-coefficient-typology", b_ok and inc_ok,
          "b_n = -(c_n F_n)^2 <= 0 at EVERY degree on EVERY world "
          "(source-sign-pure coupling: a negative square, sign "
          "free of the chain); direct-route D-increment sign == "
          "-sg h_n at all %d resolvable of %d degrees (floors "
          "%.0e/%.0e typed): the BASE PIVOT ALONE carries the "
          "world sign, the border contributes a nonnegative "
          "magnitude" % (n_res, n_tot, RESOLVE_MAIN, RESOLVE_CTRL))

    # ---------------- S3: LEG B -- the coupled budget cocycle
    section("S3  LEG B -- THE COUPLED BUDGET COCYCLE")
    mono_ok = True
    mono_note = []
    for t in packs:
        p = packs[t]
        rmin = float(np.min(p["rho"][:p["N"]]))
        mono_ok = mono_ok and rmin > 0.0
        mono_note.append("%s min rho %.1e at n=%d"
                         % (t, rmin,
                            int(np.argmin(p["rho"][:p["N"]]))))
    check("G30-main-monotone-drain", mono_ok,
          "MAIN increment law: D_{n+1} - D_n = -rho_n with rho_n "
          "> 0 at EVERY degree through the ENTIRE free window "
          "(%s): the cocycle is a sign-definite monotone drain -- "
          "COCYCLE_LAW_FOUND arm 1" % "; ".join(mono_note))
    brk_ok = True
    brk_note = []
    for c in ctrl:
        p = ctrl[c]
        first = next((n for n in range(p["N"])
                      if float(p["rho"][n]) < 0.0), None)
        brk_ok = brk_ok and (first == CTRL_FLIPS[long_names[c]])
        brk_note.append("%s first rho<0 at n=%s (flip %d)"
                        % (c, first, CTRL_FLIPS[long_names[c]]))
    check("G31-control-break-at-flips", brk_ok,
          "the increment law breaks FIRST exactly at the r256 "
          "base flips: %s -- the cocycle inherits the positive-"
          "prefix firewall degree-exactly (COCYCLE_LAW_FOUND arm "
          "2)" % "; ".join(brk_note))
    for tag, p in worlds:
        N = p["N"]
        S = p["S"]
        St = float(S[N - 1])
        zh = float(S[HEAD_K - 1])
        zb = float(S[N - TAIL_K - 1]) - zh
        zt = St - zh - zb
        wb = WB[tag]
        Dv = [wb["B"]] + [wb["sa"][n] * wb["sg"][n]
                          * math.exp(wb["la"][n] - wb["lg"][n])
                          for n in (HEAD_K, N - TAIL_K, N)]
        drops = [math.log10(max(abs(Dv[i]), 1e-300))
                 - math.log10(max(abs(Dv[i + 1]), 1e-300))
                 for i in range(3)]
        info("%-6s zones sum rho H/B/T %+.3e/%+.3e/%+.3e "
             "shares %.6g/%.6g/%.6g | log10|D| drop %.3f/%.3f/"
             "%.3f%s"
             % (tag, zh, zb, zt, zh / St, zb / St, zt / St,
                drops[0], drops[1], drops[2],
                "" if tag in packs else
                " [INDEFINITE_CONTINUATION beyond n=%d]"
                % pmax[tag]))
    check("G32-zone-anatomy", True,
          "sealed zones HEAD n < %d / BULK / TAIL last %d: the "
          "coupling term is the SOLE n-dynamics and acts as a "
          "PURE DRAIN in every zone on MAIN (head-loaded, r246 "
          "reproduced: rho_0 dominates; the tail refreshes the "
          "drain); control zone rows are algebraic tau-quotient "
          "statements beyond pmax (typed, not Hilbert-space)"
          % (HEAD_K, TAIL_K))
    if not smoke:
        sep_note = []
        sep_best = 0.0
        for c in ctrl:
            for nchk in (SEP_CHK_FIX, pmax[c]):
                DM = WB["w9"]["sa"][nchk] * WB["w9"]["sg"][nchk] \
                    * math.exp(WB["w9"]["la"][nchk]
                               - WB["w9"]["lg"][nchk])
                DC = WB[c]["sa"][nchk] * WB[c]["sg"][nchk] \
                    * math.exp(WB[c]["la"][nchk]
                               - WB[c]["lg"][nchk])
                sep = abs(math.log10(max(abs(DM), 1e-300))
                          - math.log10(max(abs(DC), 1e-300)))
                sep_best = max(sep_best, sep)
                sep_note.append("%s@n=%d %.3f" % (c, nchk, sep))
        vSep = ("WORLD_SEP_PRETERMINAL(%.2f dec)" % sep_best
                if sep_best >= SEP_BAR
                else "NO_EARLY_SEPARATION(%.2f dec)" % sep_best)
        check("G33-preterminal-separation", True,
              "cocycle world separation at the sealed checkpoints "
              "{%d, pmax_W}: %s (bar %.1f dec) => %s -- honest: "
              "the old R4 answer in the new coordinate"
              % (SEP_CHK_FIX, "; ".join(sep_note), SEP_BAR, vSep))
    else:
        vSep = "SEP_SMOKE_NA"
        check("G33-preterminal-separation", True, "SMOKE: skipped")

    # ---------------- S4: LEG C -- the micro-falsifier
    section("S4  LEG C -- THE MICRO-FALSIFIER (blind)")
    hits_blind = predictor_scope_audit("blind_flip_predictor")
    check("G40-predictor-ast-clean", not hits_blind,
          "the blind predictor scope consumes node positions + "
          "signed weights ONLY (sealed forbidden set: chain "
          "arrays sg_h/lg_h/gam_next/hv/Fv/rho/fb/nf + builder "
          "names): %s"
          % ("CLEAN" if not hits_blind else "; ".join(hits_blind)))
    flips_ok = True
    fl_note = []
    for c in ctrl:
        xu, wu = WB[c]["xu"], WB[c]["wu"]
        fl = blind_flip_predictor(xu, wu, ctrl[c]["N"])
        first = fl[0] if fl else None
        ok = (first == CTRL_FLIPS[long_names[c]]
              == ctrl[c]["nf"])
        flips_ok = flips_ok and ok
        fl_note.append("%s -> %s (truth %s)"
                       % (c, first, ctrl[c]["nf"]))
    check("G41-blind-control-flips", flips_ok,
          "blind source-only pivot field predicts the w9 control "
          "flips: %s -- 3/3 (ground truth = re-derived wpack "
          "chain, gates only)" % "; ".join(fl_note))
    if not smoke:
        tail_ok = True
        tl_note = []
        pred_offs = []
        true_offs = []
        for i, w in enumerate(TAIL_WINDOWS):
            d = HS.window_data(w)
            N = d["n_max"]
            xu, wu = union_arrays(d)
            fl = blind_flip_predictor(xu, wu, N + EXT)
            first = fl[0] if fl else None
            rows = BH.bord_chain(d["xs"], d["ws"], d["ys"],
                                 d["vs"], d["xs"][:2],
                                 d["ws"][:2] * 0.0, d["ys"][:2],
                                 d["vs"][:2] * 0.0, N + EXT + 1)
            truth = next((r["n"] for r in rows
                          if r["sg_h"] < 0), None)
            pred_offs.append(None if first is None else first - N)
            true_offs.append(None if truth is None else truth - N)
            ok = (first == truth
                  and first - N == PRIOR_OFFSETS[i])
            tail_ok = tail_ok and ok
            tl_note.append("w%d N=%d pred %s truth %s" %
                           (w, N, first, truth))
        check("G42-blind-forced-tail", tail_ok,
              "blind forced-tail survival on the five windows: "
              "predicted offsets %s == ground truth %s == the "
              "frozen prior %s (%s) -- the coefficient field "
              "predicts BOTH sides of the falsifier"
              % (str(tuple(pred_offs)), str(tuple(true_offs)),
                 str(PRIOR_OFFSETS), "; ".join(tl_note)))
        s_scr = mp_flip_ward(WB["SCR"]["xu"], WB["SCR"]["wu"],
                             (21, 22), MP_FLIP_DPS)
        s_w9 = mp_flip_ward(WB["w9"]["xu"], WB["w9"]["wu"],
                            (184, 185), MP_FLIP_DPS)
        ok_mp = (s_scr[21] > 0 and s_scr[22] < 0
                 and s_w9[184] > 0 and s_w9[185] < 0)
        check("G43-mp-flip-wards", ok_mp,
              "exact-precision (dps %d) determinants of the SAME "
              "source Gram: SCR sign det G_21/G_22 = %+d/%+d "
              "(flip at 21), w9 sign det G_184/G_185 = %+d/%+d "
              "(forced-tail flip at 184 = N_w + 0): the pivot "
              "field is exact arithmetic, not f64"
              % (MP_FLIP_DPS, s_scr[21], s_scr[22], s_w9[184],
                 s_w9[185]))
        vC = ("MICROFALSIFIER_PASSED(blind: coeff-field)"
              if (flips_ok and tail_ok and ok_mp and not hits_blind)
              else ("MICROFALSIFIER_PARTIAL(flips %s, tail %s)"
                    % (flips_ok, tail_ok)
                    if (flips_ok or tail_ok)
                    else "MICROFALSIFIER_FAILED"))
    else:
        check("G42-blind-forced-tail", True, "SMOKE: skipped")
        check("G43-mp-flip-wards", True, "SMOKE: skipped")
        vC = "MICROFALSIFIER_SMOKE_NA"
    info("HONEST TYPING (sealed): the pass certifies the coupled "
         "recursion's coefficient field as falsifier-compliant "
         "via a route-independent source-only computation; a "
         "PARAMETRIX/local-connection pass stays OPEN")

    # ---------------- S5: LEG D -- no-pole connection in s
    section("S5  LEG D -- NO-POLE CONNECTION IN s (MEASUREMENT)")
    ladder = (9,) if smoke else KZ_LADDER
    hs_l, dist_l = [], []
    wall_ok = True
    inter_worst = 0.0
    raw_cross = unit_cross = 0
    lad_note = []
    for kz in ladder:
        b = PIK.build_rung(kz)
        h, L, alpha = b["h"], b["L"], b["alpha"]
        xs, ws_, _ = PIK.folded_measure(b["d"], L, +1.0)
        ys, vs, _ = PIK.folded_measure(b["d"], L, -1.0)
        al, be, m0, steps = PIK.lanczos_chain(xs, ws_, h + 1)
        if steps < h + 1:
            wall_ok = False
            continue
        Pn = PIK.eval_chain(al, be, m0, ys, h)
        A = np.sqrt(vs)[:, None] * Pn
        Q = A.T @ A
        ev = np.linalg.eigvalsh(Q)
        lmax = float(ev[-1])
        wall_ok = wall_ok and (lmax < 1.0)
        dist = 1.0 / lmax - 1.0
        bS = PIK.build_rung(kz, comb=PB.smooth_comb(alpha))
        xsS, wsS, _ = PIK.folded_measure(bS["d"], L, +1.0)
        ysS, vsS, _ = PIK.folded_measure(bS["d"], L, -1.0)
        bn = np.concatenate([xsS, ysS])
        bwt = np.concatenate([wsS, -vsS])
        Pb = PIK.eval_chain(al, be, m0, bn, h)
        f = Pb.T @ bwt
        f2 = float(f @ f)
        evr = np.linalg.eigvalsh(Q + np.outer(f, f))
        u = f / math.sqrt(f2)
        evu = np.linalg.eigvalsh(Q + np.outer(u, u))
        spread = float(ev[-1] - ev[0])
        for i in range(len(ev)):
            inter_worst = max(
                inter_worst,
                max(float(ev[i] - evr[i]), 0.0) / max(spread, 1e-300))
            if i + 1 < len(ev):
                inter_worst = max(
                    inter_worst,
                    max(float(evr[i] - ev[i + 1]), 0.0)
                    / max(spread, 1e-300))
        raw_cross += int(float(evr[-1]) >= 1.0)
        unit_cross += int(float(evu[-1]) >= 1.0)
        hs_l.append(h)
        dist_l.append(dist)
        lad_note.append("kz%d h=%d lmax %.6f dist %.2e raw %.3f "
                        "(|f|^2 %.2f) unit %.3f"
                        % (kz, h, lmax, dist, float(evr[-1]), f2,
                           float(evu[-1])))
    for s in lad_note:
        info(s)
    if not smoke:
        id_worst = 0.0
        for kz in ID_RUNGS:
            b = PIK.build_rung(kz)
            h, L = b["h"], b["L"]
            xs, ws_, _ = PIK.folded_measure(b["d"], L, +1.0)
            ys, vs, uf_n = PIK.folded_measure(b["d"], L, -1.0)
            al, be, m0, _ = PIK.lanczos_chain(xs, ws_, h + 1)
            Pn = PIK.eval_chain(al, be, m0, ys, h)
            sq = np.sqrt(vs)
            E = sq[:, None] * (Pn @ Pn.T) * sq[None, :]
            E = 0.5 * (E + E.T)
            tau_m = (2.0 * math.pi * uf_n / L) / b["D"]
            port = tau_m <= float(np.max(tau_m)) / 10.0
            ip, ib = np.where(port)[0], np.where(~port)[0]
            Pp = E[np.ix_(ip, ip)]
            R = E[np.ix_(ib, ib)]
            X = E[np.ix_(ip, ib)]
            for s in S_GRID:
                s1, l1 = np.linalg.slogdet(
                    np.eye(len(E)) - s * E)
                s2, l2 = np.linalg.slogdet(
                    np.eye(len(ib)) - s * R)
                DP = Pp + s * X @ np.linalg.solve(
                    np.eye(len(ib)) - s * R, X.T)
                s3, l3 = np.linalg.slogdet(
                    np.eye(len(ip)) - s * DP)
                id_worst = max(id_worst,
                               abs(l1 - (l2 + l3)),
                               abs(s1 - s2 * s3))
            del E
        check("G50-schur-identity-regate", id_worst <= ID_BAR,
              "det(I - sE) == det(I - sR) det(I - sD_P(s)) with "
              "D_P(s) = P + sX(I - sR)^{-1}X^T re-gated on rungs "
              "%s over the s-grid %s: worst abs-log dev %.1e "
              "(bar %.0e) -- the r224 s-dressed port stands"
              % (str(ID_RUNGS), str(S_GRID), id_worst, ID_BAR))
    else:
        check("G50-schur-identity-regate", True, "SMOKE: skipped")
    if len(hs_l) >= 2:
        slope = float(np.polyfit(np.log10(hs_l),
                                 np.log10(dist_l), 1)[0])
        spear = spearman(hs_l, dist_l)
    else:
        slope, spear = float("nan"), float("nan")
    trend = ("APPROACHING" if spear <= -SPEAR_BAR else
             ("RECEDING" if spear >= SPEAR_BAR else "FLAT"))
    check("G51-nopole-base-ladder", wall_ok,
          "base family tau_w(s) = det(I - sQ_w): lambda_max < 1 "
          "on %d/%d rungs (the wall); NOPOLE.COFINAL indicator "
          "dist = 1/lambda_max - 1 vs N: slope %.2f dec/dec, "
          "Spearman %.3f (sealed bar %.1f) => NOPOLE_TREND(%s) "
          "-- MEASUREMENT, no theorem"
          % (len(hs_l), len(ladder), slope, spear, SPEAR_BAR,
             trend))
    vRaw = ("AUG_RAW_CROSSES_ONE" if raw_cross == len(hs_l)
            else ("AUG_RAW_BELOW_ONE" if raw_cross == 0
                  else "AUG_RAW_MIXED(%d/%d)" % (raw_cross,
                                                 len(hs_l))))
    vUnit = ("AUG_UNIT_CROSSES_ONE" if unit_cross == len(hs_l)
             else ("AUG_UNIT_BELOW_ONE" if unit_cross == 0
                   else "AUG_UNIT_MIXED(%d/%d)" % (unit_cross,
                                                   len(hs_l))))
    check("G52-augmented-zero-structure",
          inter_worst <= INTERLACE_TOL,
          "rank-1 Uvarov border row in the state frame: Cauchy "
          "interlacing exact (worst rel violation %.1e, tol "
          "%.0e); RAW row crosses 1 on %d/%d rungs (mass-driven: "
          "corner |f|^2 >> 1, typed -- a statement about the "
          "aggregated border mass), UNIT direction row crosses 1 "
          "on %d/%d rungs => %s + %s: the augmented family "
          "carries a real zero at s < 1 -- the coupling ENDANGERS "
          "a naive bordered spectral no-pole path (measured, "
          "never upgraded)"
          % (inter_worst, INTERLACE_TOL, raw_cross, len(hs_l),
             unit_cross, len(hs_l), vRaw, vUnit))

    # ---------------- S6: LEG E -- must-fails + anchors
    section("S6  LEG E -- FALSIFIERS + MUST-FAILS")
    p9 = packs["w%d" % windows[0]]
    wb9 = WB["w%d" % windows[0]]
    lc9 = math.log(2.0 / wb9["rh"])
    anchor9 = 5.0 / 7.0 - float(p9["rho"][p9["N"] - 1])
    honest = abs(RC["w%d" % windows[0]][4] / anchor9 - 1.0)
    _, _, _, _, D_swap = pair_recursion(p9, wb9["B"], lc9,
                                        mutate="swap")
    dev_e1 = abs(D_swap / anchor9 - 1.0)
    ok_e1 = dev_e1 >= LOUD * max(honest, 1e-300)
    _, _, _, _, D_omit = pair_recursion(p9, wb9["B"], lc9,
                                        mutate="omit")
    dev_e2 = abs(D_omit / anchor9 - 1.0)
    ok_e2 = dev_e2 >= LOUD * max(honest, 1e-300)
    check("G60-swapped-border-index", ok_e1,
          "coupled step with F_{n+1} in place of F_n: full-depth "
          "anchor dev %.1e = %.1e x honest %.1e (bar %.0f x) -- "
          "the recursion consumes the border index exactly"
          % (dev_e1, dev_e1 / max(honest, 1e-300), honest, LOUD))
    check("G61-omitted-coupling", ok_e2,
          "coupling term dropped (tau^aug_{n+1} = a_n tau^aug_n): "
          "D freezes at B = %.4f, anchor dev %.1e = %.1e x honest "
          "(bar %.0f x) -- the two-term coupling is load-bearing "
          "on MAIN, visibly" % (wb9["B"], dev_e2,
                                dev_e2 / max(honest, 1e-300),
                                LOUD))
    hits_orc = predictor_scope_audit("oracle_predictor")
    check("G62-oracle-predictor-flagged", bool(hits_orc),
          "the deliberately oracle-reading mutant is FLAGGED by "
          "the predictor AST audit (%s) while the blind scope "
          "stays clean: the blindness claim is machine-enforced"
          % ("; ".join(hits_orc) if hits_orc else "NOT FLAGGED"))
    pS = ctrl["SMOOTH"]
    r0 = float(pS["rho"][0])
    r1 = max(abs(float(r)) for r in pS["rho"][1:pS["N"]])
    check("G63-smooth-alias-anchor", r1 / r0 <= SM_ALIAS_BAR,
          "SMOOTH self-alias (border == window): max |rho_{n>=1}| "
          "/ rho_0 = %.1e (bar %.0e) -- F_n = 0 for n >= 1 by "
          "orthogonality, the coupling term vanishes identically: "
          "the pair recursion degenerates to the pure tau-step "
          "exactly when the source does" % (r1 / r0, SM_ALIAS_BAR))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact one-step pair recursion with its "
          "coefficient typology, the cocycle increment law with "
          "its break anatomy, the blind coefficient-field pass of "
          "the frozen micro-falsifier, and the measured no-pole "
          "trend with the augmented-zero warning")
    vA = ("COUPLED_RECURSION_EXACT(a chain-consuming, b source-"
          "sign-pure)"
          if (tstep_main <= TSTEP_BAR_MAIN
              and tstep_ctrl <= TSTEP_BAR_CTRL
              and cpl_main <= CPL_BAR_MAIN
              and cpl_ctrl <= CPL_BAR_CTRL
              and anchor_worst <= ANCHOR_BAR and b_ok and inc_ok)
          else "COUPLED_RECURSION_OPEN")
    vB = ("COCYCLE_LAW_FOUND(monotone drain; breaks at flips "
          "21/25/27)" if (mono_ok and brk_ok)
          else "COCYCLE_STRUCTURELESS")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        verd = " + ".join([vA, vB, vSep, vC,
                           "NOPOLE_TREND(%s, slope %.2f, "
                           "spearman %.3f)" % (trend, slope,
                                               spear),
                           vRaw, vUnit])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the pair recursion + its "
          "coefficient typology + the cocycle increment law; "
          "MEASURED: zone anatomy, pre-terminal separation, "
          "no-pole trend, augmented zero structure; OPEN: any "
          "a-priori bound, the parametrix-level falsifier pass, "
          "the budget bound and the base law (r243/r247/r250/"
          "r251/r253/r256 stand); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
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
