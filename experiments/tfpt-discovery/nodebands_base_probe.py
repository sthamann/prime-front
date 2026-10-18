#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nodebands_base_probe -- PRIME.PORT.RHP.BASE.NODEBANDS.01
(round 255): THE NODE-BAND LAYER -- where exactly does the r252
drift arise, and does a LOCAL band layer carry the ORIENTATION?
r250/r251/r252 measured: the outer model M_n carries the h RATE
(slope <= 0.007 dec/degree) but the deviation layer Delta_{w,n} =
log10|h_n| - log10 h^out_n DRIFTS -1.1..-2.1 decades end-to-end
(RATE_ONLY_NUMERICAL) and the model is ORIENTATION-BLIND
(gamma^out > 0 on all worlds; true chains flip at EPSTEIN 25 /
SMOOTH 27).  The r250 follow-up spec (FOLLOWUP_SHA 0d14a215)
defines R2: local refinement at the band edges / KKT transitions
of the constrained equilibrium.  BINDING SHARPENING (r252): a
layer that only smooths the drift but stays positive on all
worlds is WORTHLESS -- the layer must carry the orientation
(control flips), or the round must measure honestly how much
information the layer is missing.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r252 discipline): w = window (kz),
N_w = builder depth, n = chain degree; free pivots h_{w,n}
(n < N_w) are the proof objects; the forced pivot h_N is NEVER
formed (QP equilibria at mass N are support geometry, not
pivots).  Ground truth (h values / signs / flip degrees) enters
RESIDUALS, GEOGRAPHY STATISTICS, SENSITIVITY TARGETS AND GATES
ONLY -- no candidate path consumes it (AST-audited circularity
exclusion, leg D m3).  The model side is the r250 outer model
VERBATIM (r232a constrained-equilibrium g, KKT-midpoint ell,
discrete Szego D, -2 pi i calibration; machinery imported from
centered_basefiber_probe, no refit of D or ell anywhere).  No
zero/prime oracles anywhere (AST firewall).

LEG A -- DRIFT GEOGRAPHY (localize first, model second): QP
equilibrium at EVERY mass n in [2, N_w] (warm ascending) on the
four mp-warded main windows.  Discrete band geometry of the
minimizer rho_n on the sorted union nodes: SATURATED RUNS =
maximal runs of >= 3 consecutive nodes with rho >= 0.99 (the
density AT the cap: the KKT-active bands); CLUSTERS = maximal
selected groups (rho > 1e-9) separated by voids of >= 3
consecutive empty nodes; SOFT COUNT = #nodes with 0.01 < rho <
0.99 (the open-band interior); KKT gap per mass; ENTERING
DISTANCE d_enter(n) = node-index distance of the entering
selection (top-n minus top-(n-1)) to the nearest saturated-run
edge of mass n-1.  TRANSITION DEGREES T = {n : #satruns or
#clusters changes vs n-1} (bands open/close).  Per window over
n in [3, N_w - 1]: eta_n = d(Delta)/dn = log10|gamma_n /
gamma^out_n|; sealed statistics: TRANS_CONC = median|eta| on T /
median|eta| off T, drift share on T, Spearman(|eta|; transition
magnitude), Spearman(|eta|; d_enter), Spearman(|eta|; |d gap|).
SEALED PREMISE RULE: a window SUPPORTS band localization iff
#T >= 5 AND frac(T) <= 0.5 AND TRANS_CONC >= 2.0;
DRIFT_BAND_LOCALIZED iff >= 3/4 main windows support, else
DRIFT_NOT_BAND_LOCALIZED.
(a2) CONTROLS GEOGRAPHY: the same per-degree band geometry on
EPSTEIN/SMOOTH (masses 2..flip+10): BANDGEO_FLIP_MARKED iff on
BOTH controls a transition degree lies within +-2 of the true
flip (25/27) -- the first test whether the band geometry carries
orientation-relevant signal at all.
(a3) N-STABILITY: 3 BLIND rungs of the r233 42-rung ladder
(frame-A arithmetic h <= 900, main windows excluded, h-sorted,
odd positions, first/middle/last; flipped rungs typed+skipped),
masses [N//2 - 12, N//2 + 12]: TRANS_CONC per rung;
LADDER_GEO_STABLE iff >= 2 computable rungs agree with the
main-window majority on (TRANS_CONC >= 2.0).

LEG B -- THE NODE-BAND LAYER (max 2 sealed candidates, ZERO
fitted constants, forms derived at design time):
(b1) DISCRETE KKT-EDGE CORRECTION: the outer model reads n*ell
  from the MIDPOINT of the KKT multiplier window [max_sel F,
  min_unsel F].  The first-order band-edge refinement evaluates
  the multiplier AT the band edge instead: the field of the
  first OPEN level lambda* = min_unsel F (the discrete chemical
  potential where the next band opens -- band-edge position,
  density slope and cap distance enter through the exact KKT
  field).  SEALED FORM: log10 h^b1_n = log10 h^out_n +
  (lambda_mid - lambda*)/ln 10 = log10 h^out_n - kkt_gap_n /
  (2 ln 10).  Cap-free anchor: a fractional (cap-inactive)
  equilibrium collapses the multiplier window (gap -> 0), so the
  correction VANISHES on the Chebyshev toy by construction.  No
  sign channel (positive by construction -- typed).
(b2) EXACT DISCRETE SADDLE (degree-wise saddle-point evaluation
  of the discrete energy functional): Heine identity D_n =
  sum_{|S|=n} prod_{j in S} wt_j prod_{i<j in S} (x_i - x_j)^2;
  the dominant subset is the 0/1 energy minimizer.  SEALED FORM:
  S*_n = top-n nodes by QP mass (stable tie-break by index),
  E(S) = rho_S^T A rho_S + V^T rho_S (the exact QP functional,
  A = -log|x_i - x_j|, V = -log|wt|), log10|h^b2_n| = (E(S*_n) -
  E(S*_{n+1}))/ln 10, and the SIGN CHANNEL sg^b2_n =
  parity(S*_{n+1}) * parity(S*_n) with parity(S) = prod_{j in S}
  sign(wt_j) (the saddle of the SIGNED Heine sum -- the first
  outer-layer candidate with an orientation channel).  Consumes
  node positions + weights + the QP minimizer ONLY -- no h_n.
ADJUDICATION per candidate on the 4 main windows over n in
[3, N-1]: DRIFT iff |Delta^cand_{N-1} - Delta^cand_3| < 0.3 dec
on 4/4; RATE iff |slope(Delta^cand; n)| <= 0.01 dec/degree on
4/4; ORIENT iff sg^cand_n > 0 for ALL n <= N-1 on 4/4 MAIN
windows AND the first model flip on EPSTEIN/SMOOTH lands within
+-2 of the true flips 25/27 (b1 has no sign channel: ORIENT
fails by construction, typed POSITIVE_BY_CONSTRUCTION).

LEG C -- HONEST ALTERNATIVE MEASUREMENT (orientation
dimensionality): per control at the TRUE flip degree n_f
(gate-side input, disclosed): if sg^b2_{n_f} < 0 already ->
dim 0.  Else the minimal single-swap perturbation of the saddle
input: over pairs (i in S*, o notin S*) with sign(wt_i) *
sign(wt_o) = -1, the exact energy cost Delta E = -2 A_io +
2[(A rho)_o - (A rho)_i] + V_o - V_i, minimized over the two
masses {n_f, n_f + 1} (flipping either parity flips the model
sign).  SEALED METRIC: margin_1 = min Delta E / ln 10 (decades).
ORIENTATION_LOWDIM(dim<=1)(margin) iff margin_1 <= 1.0 dec on
BOTH controls, else ORIENTATION_EXTENSIVE (only k <= 1 swaps are
searched -- disclosed: EXTENSIVE means "not 1-dimensional within
1 decade").  Swap location is reported against the leg-A band
edges (does the orientation sit at a band edge?).
(c2) r254 HANDOVER: the true gamma band around the flip degree
(log10|gamma_n|, sign for n in [n_f - 3, n_f]) on EPSTEIN/SMOOTH
printed as exact handover quantities -- ground truth in the
handover/gates only, nothing adjudicated from it.

LEG D -- MUST-FAILS (each loud) + TOY ANCHOR:
(m1) band-formula with WRONG EXPONENT: Vandermonde pair energy
  counted once instead of twice (E' = rho^T A rho / 2 + V rho)
  must move |log10 h^b2| at w9, n = N//2 by >= 10 decades;
(m2) CAP-DISTANCE SIGN: b1 built from the LOWER KKT edge
  (max_sel F) instead of the upper must FLIP THE SIGN of the
  median per-degree correction on w9 (both medians nonzero,
  bar 1e-6 dec) -- the edge orientation is structural;
(m3) CIRCULARITY: any candidate path consuming h_n / chain data
  is EXCLUDED AST-side: the sealed candidate functions
  (band_stats, sel_top, parity01, energy01, corr_b1_dec,
  swap_margins) must not reference chain identifiers (rows,
  lg_h, sg_h, gam_next, wpack, hlog, lgt, nf) -- audited, loud;
(m4) CHEBYSHEV TOY ANCHOR (64 nodes, discrete U-weight, exact
  f64 chain, masses 5..17; r252 calibration duty): hard gate =
  QP residual + (t1) toy parities all +1 (positive weights: the
  sign layer is EXACTLY trivial cap-free); candidate ANCHOR
  adjudications (amended a1, consumed by the leg-B acceptance:
  a candidate can be accepted only with its anchor OK): (t2) b2
  anchor OK iff toy residual |median| <= 0.75 dec AND |slope| <=
  0.05 dec/degree; (t3) b1 anchor OK iff it does not DEGRADE the
  exact toy: |median resid_b1| <= |median resid_raw| + 0.25 dec
  (the smoke pass refuted the draft claim "cap-free => KKT
  window collapses": on discrete nodes the multiplier window is
  O(1) wide even with zero saturated runs -- disclosed below).

SEALED CONSTANTS: windows (9, 12, 13, 26); control flips
EPSTEIN/SCRAMBLE/SMOOTH = 25/21/27; masses [2, N] step 1 (truth
degrees end at N-1; mass N feeds E01 only); QP: FISTA iters
8000, tol 1e-8, residual bar 1e-6, warm ascending; RHO_SEL 1e-9;
SAT_HI 0.99; SOFT_LO 0.01; SATRUN_MIN 3; VOID_MIN 3; eta from
n = 3; geography bars: #T >= 5, frac(T) <= 0.5, TRANS_CONC >=
2.0, localized on >= 3/4; candidate bars: drift < 0.3 dec
end-to-end, rate <= 0.01 dec/degree, flip tol +-2, control scan
flip+10; margin bar 1.0 dec; ladder: h cap 900, blind odd
positions, picks first/middle/last, half-width 12 masses;
mp chain ward w9 dps 120, bar 1e-6 on |lg h| (signs exact);
toy: 64 nodes, masses 5..17, depth 18, bars 0.75 / 0.05 /
degrade 0.25; must-fail bars: m1 >= 10 dec at w9 n = N//2, m2
median sign flip (floor 1e-6); runtime <= 1800 s; smoke = w9
masses 2..42, toy kept, controls / ladder / leg C / mp ward
skipped, must-fail loudness measured at degree 20 but
adjudicated in FULL mode only (amendment a2), no adjudication.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+',
priority order sealed; a candidate is ELIGIBLE only if its toy
anchor holds -- the r252 calibration duty):
  NODEBAND_LAYER_CARRIES(rest dec, flip hits) iff some eligible
    candidate passes DRIFT AND RATE AND ORIENT;
  else NODEBAND_RATE_ONLY iff some eligible candidate passes
    DRIFT AND RATE (the drift falls, the orientation does not --
    honest: the base layer stays arithmetic);
  else DRIFT_NOT_BAND_LOCALIZED iff the leg-A premise is refuted
    (geography kills R2 as a route; the base waits for r254);
  else NODEBAND_LAYER_FAILS (geography localized, no candidate
    carries -- honest fallback);
+ DRIFT_BAND_LOCALIZED(med conc) / DRIFT_NOT_BAND_LOCALIZED
    (always, from leg A)
+ BANDGEO_FLIP_MARKED / BANDGEO_FLIP_UNMARKED (from a2)
+ ORIENTATION_LOWDIM(dim, margin) / ORIENTATION_EXTENSIVE
    (min margin) (from leg C)
[+ LADDER_GEO_STABLE / LADDER_GEO_UNSTABLE from a3,
   informational].
Honesty before beauty: no verdict claims a bound mechanism; the
budget bound and the base law stay OPEN (r243 PAIRCORR_REENCODED,
r247 B discipline, r250 error map, r252 gauge bill all stand).

CALIBRATION AMENDMENTS (disclosed, frozen; both caught by the
FIRST smoke pass -- w9 masses 2..42 -- BEFORE any full-ladder
evaluation; the geography rule, the candidate forms, the drift/
rate/orientation bars and the verdict priority never moved):
(a1) TOY ANCHOR t3 RE-ANCHORED + ANCHOR DUTY MADE r252-SHAPED:
  the draft derivation "cap-free equilibrium => multiplier
  window collapses => b1 correction vanishes" is FALSE on a
  discrete node set: the smoke toy shows KKT gaps O(1) (b1 corr
  up to 0.8 dec) at zero saturated runs -- the window width is a
  node-spacing effect, not a cap effect.  t3 is re-anchored to
  the non-degradation form |median resid_b1| <= |median
  resid_raw| + 0.25 dec, and t2/t3 are candidate ANCHOR
  adjudications consumed by the leg-B acceptance (exactly the
  r252 leg-4 pattern "toy ANCHOR-FAIL -> reject"), not suite
  reds; the hard toy gate is QP residual + parity triviality.
  The b1 MAIN adjudication (drift/rate on differences, where
  any constant cancels) is untouched.
(a2) MUST-FAIL ADJUDICATION IS FULL-MODE ONLY: the m1 loudness
  at the smoke degree 20 is 5.4 dec (the pair-energy difference
  grows with n); the sealed bar 10 dec is adjudicated at the
  sealed degree N//2 = 92 in full mode; smoke prints the
  reduced-degree values unadjudicated.
No other amendment; bars, forms and verdict rules above are
exactly the ones adjudicated.

RECORD TABLES (frozen after calibration pass 1; run 2 must
reproduce bit-for-bit up to the WALL line):
* SWEEPS: 863 QP equilibria on the mains (+ controls + 3 ladder
  rungs), QP residual worst 1.0e-08 (bar 1e-6), every rounded
  mass integer-exact; w9 mp chain ward (dps 120) max |lg h| dev
  1.6e-11, signs all match.  THE LOUDEST GEOMETRIC FACT: cap
  contact is ESSENTIALLY ABSENT on the mains -- saturated runs
  0..0 on w9/w12/w13 and 0..2 on w26 (soft count 0..2, KKT gap
  0.005..4.4): the "KKT-active bands" of the R2 premise barely
  exist; all band transitions are cluster fission/fusion of the
  0/1 selection.
* LEG A GEOGRAPHY (eta vs transitions, n in [3, N-1]):
    w9  (N=184): #T 102/181 (frac 0.56) conc 0.48 shareT 0.41
      Sp(|eta|;tmag) -0.37 Sp(|eta|;d_enter) n/a
      Sp(|eta|;|dgap|) -0.02 drift -1.888
    w12 (N=151): #T  81/148 (frac 0.55) conc 0.55 shareT 0.43
      Sp -0.20 / n/a / -0.11 drift -1.465
    w13 (N=168): #T  91/165 (frac 0.55) conc 0.72 shareT 0.50
      Sp -0.10 / n/a / +0.01 drift -1.147
    w26 (N=364): #T 228/361 (frac 0.63) conc 0.62 shareT 0.55
      Sp -0.14 / +0.02 / -0.13 drift -2.098
  => support 0/4 (median conc 0.59): transitions are DENSE
  (55-63% of all degrees, frac > 0.5 alone kills the premise)
  and |eta| AT transitions is SMALLER than off transitions
  (conc < 1 on 4/4, Sp(|eta|;tmag) negative on 4/4): the drift
  is ANTI-correlated with band transitions =>
  DRIFT_NOT_BAND_LOCALIZED -- the R2 premise is refuted by the
  geography, in the strongest possible way (not "no signal",
  but the opposite sign of the premise).  (a2) controls:
  EPSTEIN/SMOOTH nearest transition at distance 0 of the flips
  25/27 => BANDGEO_FLIP_MARKED, but the transition fraction is
  0.88/0.75 there -- the mark carries NO selectivity (typed).
  (a3) ladder kz23/kz44/kz52 (N=149/436/878): conc 1.07/0.64/
  0.86, support False 3/3, agree 3/3 => LADDER_GEO_STABLE (the
  non-localization is N-stable).
* LEG B CANDIDATES (n in [3, N-1]; rest / slope / scatter):
    RAW  rest -2.07/-1.62/-1.10/-1.51, slope -0.0032/-0.0046/
         -0.0026/-0.0018 (w9/w12/w13/w26)
    b1   rest -2.13/-1.66/-0.99/-1.16, slope -0.0033/-0.0049/
         -0.0026/-0.0016, scat 0.24..0.27 -- drift 0/4, rate
         4/4, toy ANCHOR-FAIL (0.520 vs 0.259 + 0.25):
         INELIGIBLE; the KKT-edge term is real but tiny and
         moves the toy anchor the wrong way;
    b2   rest -1.88/-1.54/-1.81/-1.85, slope -0.0063/-0.0077/
         -0.0063/-0.0035, scat 0.28..0.35 -- drift 0/4, rate
         4/4 (the saddle HOLDS the rate bar), toy ANCHOR-OK
         (med +0.249, slope -0.0462);
    ORIENTATION: b1 POSITIVE_BY_CONSTRUCTION (typed); b2 MAIN
    parity flips 4/1/4/20 per window (first at n = 27/73/66/34
    -- gate A FAILS 4/4); controls: EPSTEIN first model flip 8
    vs true 25, SMOOTH 18 vs true 27 (both MISS): the saddle
    parity is a REAL but MISPLACED sign channel.
  => no eligible candidate passes DRIFT: top verdict follows
  leg A.
* LEG C SENSITIVITY: sg^b2 at the true flip degree is +1 on
  both controls (dim 0 not triggered); single-swap margins at
  the flip masses: EPSTEIN margin_1 -0.16 dec at mass 26 (swap
  node 348 -> 353), SMOOTH +0.19 dec at mass 28 (361 -> 364);
  no satrun edges exist (edge dist n/a) => both |margin| <= 1.0
  => ORIENTATION_LOWDIM(1): ONE swap within 0.2 decades of the
  saddle flips the model parity at the true flip degree -- the
  orientation sits in a 1-dimensional direction of the saddle
  configuration (a targeted layer is possible in principle; the
  saddle's failure is a SELECTION error of O(0.2 dec), not an
  extensive information gap).  (c2) r254 handover, true gamma
  band (lg10|gamma|, sign): EPSTEIN n=22..25: -0.650+, -0.712+,
  -1.268+, +1.164-; SMOOTH n=24..27: -0.645+, -0.695+, -0.996+,
  +0.413- (the flip degree carries |gamma| > 1 on both
  controls: the flip is a JUMP, not a soft crossing).
* LEG D: m1 wrong Vandermonde exponent: 26.9 dec at w9 n = 92
  (bar 10, LOUD); m2 lower-KKT-edge sign: median correction
  flips -0.3041 -> +0.3041 dec (sign FLIPPED, LOUD); m3
  circularity audit clean (6 candidate functions, 0 chain
  identifiers); m4 toy: parities 13/13 all +1, anchors as in
  leg B.
* VERDICT: DRIFT_NOT_BAND_LOCALIZED + BANDGEO_FLIP_MARKED +
  ORIENTATION_LOWDIM(1) + LADDER_GEO_STABLE; 17/17 gates, wall
  68.2 s.  READING: R2 (node-band local parametrix) is DEAD as
  a drift route -- there is almost no cap contact, transitions
  are dense and ANTI-correlated with the drift; the b2 saddle
  is the first outer-layer object that HOLDS the h-rate bar
  (4/4) AND owns a sign channel, and leg C shows that channel
  fails by a single 0.2-decade swap at the true flip degrees:
  the orientation is LOW-DIMENSIONAL in the saddle
  configuration -- the exact quantity to hand to r254.
AMENDMENTS AFTER FREEZE: NONE.

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

import base_gauge_constant_probe as GC       # noqa: E402 r252
import bordered_hankel_probe as BH           # noqa: E402 r244
import centered_basefiber_probe as CB        # noqa: E402 r250
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import szego_equilibrium_probe as SZ         # noqa: E402 r232a
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

WINDOWS = (9, 12, 13, 26)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
QP_ITERS = 8000
QP_TOL = 1e-8
QP_RES_BAR = 1e-6
RHO_SEL = 1e-9
SAT_HI = 0.99
SOFT_LO = 0.01
SATRUN_MIN = 3
VOID_MIN = 3
ETA_LO = 3
TRANS_MIN = 5
TRANS_FRACMAX = 0.5
CONC_BAR = 2.0
LOC_MIN_W = 3
DRIFT_BAR = 0.3
RATE_BAR = 0.01
FLIP_TOL = 2
FLIP_SCAN = 10
MARGIN_BAR = 1.0
LAD_HALF = 12
LADDER_H_CAP = 900
MP_WARD_DPS = 120
MP_WARD_BAR = 1e-6
TOY_M = 64
TOY_MASSES = tuple(range(5, 18))
TOY_DEPTH = 18
TOY_B2_MED_BAR = 0.75
TOY_B2_SLOPE_BAR = 0.05
TOY_B1_DEGRADE = 0.25
M1_LOUD_DEC = 10.0
M2_MED_MIN = 1e-6
L10 = math.log(10.0)
CAND_FUNCS = ("band_stats", "sel_top", "parity01", "energy01",
              "corr_b1_dec", "swap_margins")
CHAIN_IDS = {"rows", "lg_h", "sg_h", "gam_next", "wpack",
             "hlog", "lgt", "nf"}
CAL_VERDICT = ("DRIFT_NOT_BAND_LOCALIZED + BANDGEO_FLIP_MARKED "
               "+ ORIENTATION_LOWDIM(1) + LADDER_GEO_STABLE")

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
    """standing zero/prime firewall + the m3 circularity audit on
    the sealed candidate functions."""
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
    circ = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.FunctionDef)
                and node.name in CAND_FUNCS):
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif (isinstance(sub, ast.Constant)
                        and isinstance(sub.value, str)):
                    nm = sub.value
                if nm in CHAIN_IDS:
                    circ.append("%s:%s@%d" % (node.name, nm,
                                              sub.lineno))
    ok = (not bad) and (not circ)
    return ok, ("NO zero/prime oracles; m3 circularity audit "
                "CLEAN: %d candidate functions consume node "
                "positions + weights + the QP minimizer only "
                "(chain identifiers %s excluded); h_N never "
                "formed; truth enters residuals/geography/"
                "sensitivity targets/gates only"
                % (len(CAND_FUNCS), sorted(CHAIN_IDS))
                if ok else "; ".join(bad + circ))


# --------------------------------------- sealed candidate functions
def band_stats(rho):
    """discrete band geometry of the QP minimizer (leg A):
    saturated runs (>= SATRUN_MIN nodes at the cap), clusters
    (voids >= VOID_MIN empty nodes), soft count, satrun edges."""
    sel = rho > RHO_SEL
    sat = rho >= SAT_HI
    soft = int(np.sum((rho > SOFT_LO) & (rho < SAT_HI)))
    edges = []
    nsat = 0
    idx = np.flatnonzero(sat)
    if len(idx):
        brk = np.flatnonzero(np.diff(idx) > 1)
        starts = np.concatenate([[0], brk + 1])
        ends = np.concatenate([brk, [len(idx) - 1]])
        for s0, e0 in zip(starts, ends):
            if int(idx[e0]) - int(idx[s0]) + 1 >= SATRUN_MIN:
                nsat += 1
                edges.append(int(idx[s0]))
                edges.append(int(idx[e0]))
    sidx = np.flatnonzero(sel)
    nclust = (1 + int(np.sum(np.diff(sidx) > VOID_MIN))
              if len(sidx) else 0)
    return dict(sel=sel, nsat=nsat, nclust=nclust, soft=soft,
                edges=np.asarray(sorted(set(edges)), int))


def sel_top(rho, n):
    """the saddle subset S*_n: top-n nodes by QP mass, stable
    tie-break by node index (sealed rounding rule)."""
    order = np.lexsort((np.arange(len(rho)), -rho))
    b = np.zeros(len(rho), bool)
    b[order[:int(n)]] = True
    return b


def parity01(sgw, b):
    """parity(S) = prod sign(wt_j) over the selected subset."""
    return -1 if (int(np.sum(sgw[b] < 0)) % 2) else 1


def energy01(A, V, b):
    """exact discrete energy of a 0/1 configuration:
    E = rho^T A rho + V^T rho; returns (E, pair part)."""
    r = b.astype(float)
    q = float(r @ (A @ r))
    return q + float(V @ r), q


def corr_b1_dec(kkt_gap):
    """b1 sealed form: (lambda_mid - lambda_upper)/ln 10 =
    -gap/(2 ln 10) decades."""
    return -0.5 * float(kkt_gap) / L10


def swap_margins(A, V, sgw, b):
    """leg C: minimal single-swap energy cost (decades) over
    parity-flipping pairs (i in S, o notin S, sign product -1);
    returns (margin_dec, i*, o*) or (inf, -1, -1)."""
    r = b.astype(float)
    base = 2.0 * (A @ r) + V
    iS = np.flatnonzero(b)
    iO = np.flatnonzero(~b)
    if not len(iS) or not len(iO):
        return float("inf"), -1, -1
    mask = (sgw[iS][:, None] * sgw[iO][None, :]) < 0
    if not np.any(mask):
        return float("inf"), -1, -1
    dE = (base[iO][None, :] - base[iS][:, None]
          - 2.0 * A[np.ix_(iS, iO)])
    dE = np.where(mask, dE, np.inf)
    k = int(np.argmin(dE))
    ii, oo = np.unravel_index(k, dE.shape)
    return (float(dE[ii, oo]) / L10, int(iS[ii]), int(iO[oo]))


# ------------------------------------------------------------ sweep
def sweep(d, masses, keep_b=frozenset()):
    """QP equilibrium at every mass (warm ascending) + the sealed
    per-mass data: model h^out, KKT gap, band geometry, saddle
    energy/parity, entering distance.  Consumes SOURCE data only
    (the truth column is joined outside)."""
    x, wt, A, Lip, V = CB.eq_field(d)
    sgw = np.sign(wt)
    out = dict(ns=[], hmod=[], kkt=[], corr=[], E01=[], q01=[],
               par=[], nsat=[], nclust=[], soft=[], d_ent=[])
    kept = {}
    rho = None
    prev_b = None
    prev_edges = None
    res_worst = 0.0
    mass_ok = True
    for n in masses:
        rho, res = SZ.solve_qp(A, Lip, V, float(n), rho0=rho,
                               iters=QP_ITERS, tol=QP_TOL)
        res_worst = max(res_worst, res)
        md = CB.model_data(x, wt, A, V, rho, n)
        mass_ok = mass_ok and (md["nround"] == n)
        bs = band_stats(rho)
        b = sel_top(rho, n)
        E, q = energy01(A, V, b)
        d_ent = float("nan")
        if prev_b is not None and prev_edges is not None \
                and len(prev_edges):
            ent = np.flatnonzero(b & ~prev_b)
            if len(ent):
                d_ent = float(np.min(np.abs(
                    ent[:, None] - prev_edges[None, :])))
        out["ns"].append(n)
        out["hmod"].append(md["hmod_l10"])
        out["kkt"].append(md["kkt"])
        out["corr"].append(corr_b1_dec(md["kkt"]))
        out["E01"].append(E)
        out["q01"].append(q)
        out["par"].append(parity01(sgw, b))
        out["nsat"].append(bs["nsat"])
        out["nclust"].append(bs["nclust"])
        out["soft"].append(bs["soft"])
        out["d_ent"].append(d_ent)
        if n in keep_b:
            kept[n] = dict(b=b.copy(), edges=bs["edges"].copy())
        prev_b = b
        prev_edges = bs["edges"]
    for k in ("ns", "hmod", "kkt", "corr", "E01", "q01", "par",
              "nsat", "nclust", "soft", "d_ent"):
        out[k] = np.asarray(out[k], float)
    out["kept"] = kept
    out["A"] = A
    out["V"] = V
    out["sgw"] = sgw
    return out, res_worst, mass_ok


def truth_l10(rows, ns):
    """log10|h_n| from the wpack chain for the free degrees
    (residual/gate side); nan where no free pivot exists."""
    lg = np.full(len(ns), np.nan)
    for i, n in enumerate(ns):
        n = int(n)
        if n < 0 or n >= len(rows):
            continue
        lg[i] = rows[n]["lg_h"] / L10
    return lg


# -------------------------------------------------------- geography
def geo_stats(sw, lgt):
    """leg-A geography over n in [ETA_LO, N-1]: eta vs the band
    transitions (sealed statistics)."""
    ns = sw["ns"].astype(int)
    ok = np.isfinite(lgt)
    eta, tmag, dgap, dent, en = [], [], [], [], []
    for i in range(1, len(ns)):
        n = ns[i]
        if n < ETA_LO or not (ok[i] and ok[i - 1]):
            continue
        eta.append((lgt[i] - lgt[i - 1])
                   - (sw["hmod"][i] - sw["hmod"][i - 1]))
        tmag.append(abs(sw["nsat"][i] - sw["nsat"][i - 1])
                    + abs(sw["nclust"][i] - sw["nclust"][i - 1]))
        dgap.append(abs(sw["kkt"][i] - sw["kkt"][i - 1]))
        dent.append(sw["d_ent"][i])
        en.append(n)
    eta = np.asarray(eta)
    tmag = np.asarray(tmag)
    dgap = np.asarray(dgap)
    dent = np.asarray(dent)
    en = np.asarray(en, int)
    T = tmag > 0
    nT = int(np.sum(T))
    frac = nT / max(len(eta), 1)
    if nT >= TRANS_MIN and (len(eta) - nT) >= TRANS_MIN:
        conc = (float(np.median(np.abs(eta[T])))
                / max(float(np.median(np.abs(eta[~T]))), 1e-12))
    else:
        conc = float("nan")
    share = (float(np.sum(np.abs(eta[T])))
             / max(float(np.sum(np.abs(eta))), 1e-300))
    sp_t = BH.spearman(np.abs(eta), tmag)
    sp_g = BH.spearman(np.abs(eta), dgap)
    vd = np.isfinite(dent)
    sp_d = (BH.spearman(np.abs(eta[vd]), dent[vd])
            if int(np.sum(vd)) >= 10 else float("nan"))
    support = (nT >= TRANS_MIN and frac <= TRANS_FRACMAX
               and np.isfinite(conc) and conc >= CONC_BAR)
    delta = lgt[ok] - sw["hmod"][ok]
    drift = float(delta[-1] - delta[0]) if len(delta) > 1 else 0.0
    trans_deg = en[T]
    return dict(eta=eta, en=en, nT=nT, frac=frac, conc=conc,
                share=share, sp_t=sp_t, sp_g=sp_g, sp_d=sp_d,
                support=support, drift=drift, trans=trans_deg)


def cand_series(sw, lgt, which):
    """Delta^cand over n in [ETA_LO, N-1]; rest drift, slope,
    scatter; for b2 also the sign channel (first flips)."""
    ns = sw["ns"].astype(int)
    ok = np.isfinite(lgt)
    dd, en = [], []
    flips = []
    for i in range(len(ns)):
        n = ns[i]
        if n < ETA_LO or not ok[i]:
            continue
        if which == "b1":
            hc = sw["hmod"][i] + sw["corr"][i]
        else:
            if i + 1 >= len(ns):
                continue
            hc = (sw["E01"][i] - sw["E01"][i + 1]) / L10
            if sw["par"][i + 1] * sw["par"][i] < 0:
                flips.append(n)
        dd.append(lgt[i] - hc)
        en.append(n)
    dd = np.asarray(dd)
    en = np.asarray(en, float)
    rest = float(dd[-1] - dd[0]) if len(dd) > 1 else 0.0
    slope = (float(np.polyfit(en, dd, 1)[0]) if len(dd) > 2
             else 0.0)
    scat = (float(np.median(np.abs(np.diff(dd))))
            if len(dd) > 2 else 0.0)
    return dict(rest=rest, slope=slope, scat=scat, flips=flips)


# --------------------------------------------------------------- toy
def toy_block():
    """discrete Chebyshev-U toy: cap-free anchor for both sealed
    candidates (leg D m4)."""
    xt = np.sort(np.cos(np.pi * (np.arange(TOY_M) + 0.5) / TOY_M))
    wtt = (1.0 - xt * xt) * (np.pi / TOY_M)
    Dm = np.abs(xt[:, None] - xt[None, :])
    np.fill_diagonal(Dm, 1.0)
    At = -np.log(Dm)
    np.fill_diagonal(At, 0.0)
    v = np.ones(TOY_M) / math.sqrt(TOY_M)
    for _ in range(80):
        v2 = At @ v
        nv = float(np.linalg.norm(v2))
        v = v2 / nv
    Lipt = 2.0 * nv
    Vt = -np.log(wtt)
    _als, hs = CB.toy_chain_f64(xt, wtt, TOY_DEPTH)
    sgt = np.sign(wtt)
    rho = None
    res_w = 0.0
    E01 = {}
    par = {}
    corr = {}
    nsat = {}
    hmod = {}
    for n in TOY_MASSES:
        rho, res = SZ.solve_qp(At, Lipt, Vt, float(n), rho0=rho,
                               iters=QP_ITERS, tol=QP_TOL)
        res_w = max(res_w, res)
        md = CB.model_data(xt, wtt, At, Vt, rho, n)
        bs = band_stats(rho)
        b = sel_top(rho, n)
        E, _q = energy01(At, Vt, b)
        E01[n] = E
        par[n] = parity01(sgt, b)
        corr[n] = corr_b1_dec(md["kkt"])
        nsat[n] = bs["nsat"]
        hmod[n] = md["hmod_l10"]
    resid = []
    ns_r = []
    for n in TOY_MASSES[:-1]:
        lhb2 = (E01[n] - E01[n + 1]) / L10
        resid.append(math.log10(hs[n]) - lhb2)
        ns_r.append(n)
    med = float(np.median(resid))
    slope = float(np.polyfit(ns_r, resid, 1)[0])
    par_ok = all(par[n] == 1 for n in TOY_MASSES)
    r_raw = [math.log10(hs[n]) - hmod[n] for n in TOY_MASSES]
    r_b1 = [math.log10(hs[n]) - (hmod[n] + corr[n])
            for n in TOY_MASSES]
    med_raw = float(np.median(r_raw))
    med_b1 = float(np.median(r_b1))
    anch_b1 = abs(med_b1) <= abs(med_raw) + TOY_B1_DEGRADE
    anch_b2 = (abs(med) <= TOY_B2_MED_BAR
               and abs(slope) <= TOY_B2_SLOPE_BAR)
    return dict(res=res_w, med=med, slope=slope, par_ok=par_ok,
                n_masses=len(TOY_MASSES), anch_b1=anch_b1,
                anch_b2=anch_b2, med_raw=med_raw, med_b1=med_b1,
                max_nsat=max(nsat.values()),
                max_corr=max(abs(corr[n]) for n in TOY_MASSES))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else WINDOWS

    print("=" * 78)
    print("nodebands_base_probe -- PRIME.PORT.RHP.BASE."
          "NODEBANDS.01 (round 255)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 masses 2..42; controls/ladder/"
                        "leg C/mp ward skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall+circularity", okf, det)
    check("G02-predefinition", True,
          "geography rule (#T >= %d, frac <= %.1f, conc >= %.1f, "
          "localized on >= %d/4), candidate bars (drift < %.1f "
          "dec, rate <= %.2f dec/deg, flip tol +-%d, scan "
          "flip+%d), margin bar %.1f dec, ladder half-width %d, "
          "toy bars %.2f/%.2f/%.2f, must-fail bars m1 >= %.0f "
          "dec / m2 median sign flip: ALL sealed in the frozen "
          "spec BEFORE evaluation; verdict priority CARRIES > "
          "RATE_ONLY > NOT_LOCALIZED > FAILS sealed"
          % (TRANS_MIN, TRANS_FRACMAX, CONC_BAR, LOC_MIN_W,
             DRIFT_BAR, RATE_BAR, FLIP_TOL, FLIP_SCAN,
             MARGIN_BAR, LAD_HALF, TOY_B2_MED_BAR,
             TOY_B2_SLOPE_BAR, TOY_B1_DEGRADE, M1_LOUD_DEC))

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS")
    packs = {kz: BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    okC = all(packs[kz]["nf"] is None for kz in windows)
    check("G10-census-controls", okC and okCf,
          "free prefix positive on %d/%d windows (%s); control "
          "flips re-derived %s (EPSTEIN/SMOOTH feed geography a2 "
          "+ orientation; SCRAMBLE armed for battery integrity)"
          % (sum(1 for kz in windows if packs[kz]["nf"] is None),
             len(windows),
             "; ".join("w%d N=%d" % (kz, packs[kz]["N"])
                       for kz in windows),
             str({c: ctrl[c]["nf"] for c in ctrl})))

    # ---------------- S2: toy anchors
    section("S2  CHEBYSHEV TOY ANCHORS (cap-free)")
    toy = toy_block()
    ok_toy = toy["res"] <= QP_RES_BAR and toy["par_ok"]
    check("G20-toy-anchors", ok_toy,
          "hard gate: QP residual %.1e (bar %.0e), (t1) "
          "parities %d/%d all +1 (positive weights: sign layer "
          "exactly trivial); ANCHOR ADJUDICATIONS (a1, r252 "
          "duty): (t2) b2 resid median %+.3f dec (bar %.2f), "
          "slope %+.4f (bar %.2f) -> %s; (t3) b1 non-"
          "degradation |med resid_b1| %.3f vs |med resid_raw| "
          "%.3f + %.2f -> %s (max |corr| %.2f dec at %d "
          "satruns: the discrete multiplier window is O(1) "
          "wide even cap-free, disclosed)"
          % (toy["res"], QP_RES_BAR, toy["n_masses"],
             toy["n_masses"], toy["med"], TOY_B2_MED_BAR,
             toy["slope"], TOY_B2_SLOPE_BAR,
             "ANCHOR-OK" if toy["anch_b2"] else "ANCHOR-FAIL",
             abs(toy["med_b1"]), abs(toy["med_raw"]),
             TOY_B1_DEGRADE,
             "ANCHOR-OK" if toy["anch_b1"] else "ANCHOR-FAIL"
             " (b1 ineligible)", toy["max_corr"],
             toy["max_nsat"]))

    # ---------------- S3: full-degree sweeps + wards
    section("S3  FULL-DEGREE SWEEPS (QP at every mass 2..N)")
    W = {}
    LG = {}
    res_worst = 0.0
    mass_ok = True
    nQP = 0
    for kz in windows:
        p = packs[kz]
        N = p["N"]
        masses = (list(range(2, 43)) if smoke
                  else list(range(2, N + 1)))
        sw, rw, mo = sweep(p["d"], masses)
        res_worst = max(res_worst, rw)
        mass_ok = mass_ok and mo
        nQP += len(masses)
        W[kz] = sw
        LG[kz] = truth_l10(p["rows"], sw["ns"])
        info("w%-3d N=%d: %d masses swept; satruns %d..%d, "
             "clusters %d..%d, soft %d..%d, kkt gap %.3f..%.3f"
             % (kz, N, len(masses), int(sw["nsat"].min()),
                int(sw["nsat"].max()), int(sw["nclust"].min()),
                int(sw["nclust"].max()), int(sw["soft"].min()),
                int(sw["soft"].max()), float(sw["kkt"].min()),
                float(sw["kkt"].max())))
    check("G30-sweep-qp-wards", res_worst <= QP_RES_BAR
          and mass_ok,
          "QP residual worst %.1e (bar %.0e) over %d main-window "
          "equilibria; every rounded mass integer-exact; model "
          "objects (D, ell) = r250 verbatim, untouched"
          % (res_worst, QP_RES_BAR, nQP))
    if smoke:
        check("G31-mp-chain-ward", True,
              "SMOKE: mp ward skipped (r252 chain ward stands)")
    else:
        p9 = packs[9]
        N9 = p9["N"]
        zfar = [float(np.max(np.concatenate(
            [p9["d"]["xs"], p9["d"]["ys"]]))) + 1000.0]
        _o, _g, hlog9 = CB.mp_y_pass(p9["d"], {N9 - 1}, zfar,
                                     MP_WARD_DPS, N9)
        dev = 0.0
        sg_ok = True
        for n in range(2, N9):
            dev = max(dev, abs(float(hlog9[n][0])
                               - p9["rows"][n]["lg_h"]))
            sg_ok = sg_ok and (float(hlog9[n][1])
                               == p9["rows"][n]["sg_h"])
        check("G31-mp-chain-ward", dev <= MP_WARD_BAR and sg_ok,
              "w9 mp chain (dps %d) vs the f64 wpack chain over "
              "all sweep degrees: max |lg h| dev %.1e (bar "
              "%.0e), signs %s -- the geography statistics are "
              "not an f64 artifact"
              % (MP_WARD_DPS, dev, MP_WARD_BAR,
                 "all match" if sg_ok else "MISMATCH"))

    # ---------------- S4: leg A -- drift geography
    section("S4  LEG A -- DRIFT GEOGRAPHY (band transitions)")
    GEO = {}
    n_support = 0
    concs = []
    for kz in windows:
        g = geo_stats(W[kz], LG[kz])
        GEO[kz] = g
        if g["support"]:
            n_support += 1
        if np.isfinite(g["conc"]):
            concs.append(g["conc"])
        info("w%-3d #T %d/%d (frac %.2f) conc %s shareT %.2f "
             "Sp(|eta|;tmag) %+.2f Sp(|eta|;d_enter) %s "
             "Sp(|eta|;|dgap|) %+.2f drift %+.3f -> %s"
             % (kz, g["nT"], len(g["eta"]), g["frac"],
                ("%.2f" % g["conc"]) if np.isfinite(g["conc"])
                else "n/a", g["share"], g["sp_t"],
                ("%+.2f" % g["sp_d"]) if np.isfinite(g["sp_d"])
                else "n/a", g["sp_g"], g["drift"],
                "SUPPORTS band localization" if g["support"]
                else "NOT band-localized"))
    localized = (not smoke) and (n_support >= LOC_MIN_W)
    med_conc = (float(np.median(concs)) if concs
                else float("nan"))
    check("G40-geography-adjudicated", True,
          "SEALED PREMISE RULE: %d/%d windows support band "
          "localization (need >= %d) => %s (median conc %s)"
          % (n_support, len(windows), LOC_MIN_W,
             "SMOKE_NO_ADJUDICATION" if smoke else
             ("DRIFT_BAND_LOCALIZED" if localized
              else "DRIFT_NOT_BAND_LOCALIZED -- the R2 premise "
                   "is refuted by the geography"),
             ("%.2f" % med_conc) if np.isfinite(med_conc)
             else "n/a"))
    # (a2) controls geography
    ctrl_sw = {}
    if smoke:
        bandgeo = None
        check("G41-controls-geography", True,
              "SMOKE: controls geography skipped")
    else:
        marks = []
        for cname in ("EPSTEIN", "SMOOTH"):
            pc = ctrl[cname]
            nfc = pc["nf"]
            top = min(nfc + FLIP_SCAN, pc["N"] - 1)
            swc, rwc, _mo = sweep(
                pc["d"], list(range(2, top + 2)),
                keep_b={nfc, nfc + 1})
            res_worst = max(res_worst, rwc)
            ctrl_sw[cname] = swc
            gc = geo_stats(swc, truth_l10(pc["rows"], swc["ns"]))
            dmin = (int(np.min(np.abs(gc["trans"] - nfc)))
                    if len(gc["trans"]) else 10 ** 9)
            marks.append((cname, nfc, dmin, gc["frac"]))
        bandgeo = all(d <= FLIP_TOL for _c, _f, d, _fr in marks)
        check("G41-controls-geography", True,
              "(a2) %s => %s (transition fraction %s: dense "
              "transitions carry no selectivity if frac is "
              "high -- typed, informational)"
              % ("; ".join("%s flip %d: nearest transition "
                           "distance %d" % (c, f, d)
                           for c, f, d, _fr in marks),
                 "BANDGEO_FLIP_MARKED" if bandgeo
                 else "BANDGEO_FLIP_UNMARKED",
                 str(["%.2f" % fr for _c, _f, _d, fr
                      in marks])))
    # (a3) ladder
    if smoke:
        lad_tok = "SMOKE"
        check("G42-ladder-stability", True,
              "SMOKE: ladder skipped")
    else:
        elig = sorted((GC.ladder_h(kz), kz)
                      for kz in core.frame_a_zones()
                      if kz not in WINDOWS
                      and GC.ladder_h(kz) <= LADDER_H_CAP)
        blind = elig[1::2]
        picks = sorted({blind[0], blind[len(blind) // 2],
                        blind[-1]})
        lad_note = []
        agree = 0
        ncomp = 0
        for _h, kz in picks:
            pL = BH.wpack(kz)
            if pL["nf"] is not None:
                lad_note.append("kz%d FLIP@%d typed+skipped"
                                % (kz, pL["nf"]))
                continue
            NL = pL["N"]
            lo = max(3, NL // 2 - LAD_HALF)
            hi = min(NL - 1, NL // 2 + LAD_HALF)
            swl, rwl, _mo = sweep(pL["d"],
                                  list(range(lo - 1, hi + 1)))
            res_worst = max(res_worst, rwl)
            gl = geo_stats(swl, truth_l10(pL["rows"],
                                          swl["ns"]))
            ncomp += 1
            loc_l = (np.isfinite(gl["conc"])
                     and gl["conc"] >= CONC_BAR
                     and gl["nT"] >= TRANS_MIN
                     and gl["frac"] <= TRANS_FRACMAX)
            if loc_l == localized:
                agree += 1
            lad_note.append("kz%d N=%d conc %s frac %.2f -> "
                            "support %s"
                            % (kz, NL,
                               ("%.2f" % gl["conc"])
                               if np.isfinite(gl["conc"])
                               else "n/a", gl["frac"],
                               str(loc_l)))
        lad_tok = ("LADDER_GEO_STABLE"
                   if (ncomp >= 2 and agree >= 2)
                   else "LADDER_GEO_UNSTABLE")
        check("G42-ladder-stability", True,
              "(a3) BLIND ladder sample: %s -- %d/%d computable "
              "rungs agree with the main-window majority => %s "
              "(informational)"
              % ("; ".join(lad_note), agree, max(ncomp, 1),
                 lad_tok))

    # ---------------- S5: leg B -- candidates
    section("S5  LEG B -- NODE-BAND LAYER CANDIDATES")
    CAND = {"b1": {}, "b2": {}}
    raw_note = []
    for kz in windows:
        sw = W[kz]
        lgt = LG[kz]
        ns = sw["ns"].astype(int)
        ok = np.isfinite(lgt) & (ns >= ETA_LO)
        dr = lgt[ok] - sw["hmod"][ok]
        raw_note.append("w%d %+.2f/%+.4f" % (
            kz, float(dr[-1] - dr[0]),
            float(np.polyfit(ns[ok], dr, 1)[0])))
        for c in ("b1", "b2"):
            CAND[c][kz] = cand_series(sw, lgt, c)
    info("RAW outer model rest/slope: " + "; ".join(raw_note))
    for c in ("b1", "b2"):
        note = []
        for kz in windows:
            r = CAND[c][kz]
            note.append("w%d rest %+.2f slope %+.4f scat %.2f%s"
                        % (kz, r["rest"], r["slope"], r["scat"],
                           (" flips %d(first@%s)"
                            % (len(r["flips"]),
                               str(r["flips"][0])
                               if r["flips"] else "-"))
                           if c == "b2" else ""))
        info("%s: %s" % (c, "; ".join(note)))
    drift_ok = {c: all(abs(CAND[c][kz]["rest"]) < DRIFT_BAR
                       for kz in windows) for c in CAND}
    rate_ok = {c: all(abs(CAND[c][kz]["slope"]) <= RATE_BAR
                      for kz in windows) for c in CAND}
    anchor = {"b1": toy["anch_b1"], "b2": toy["anch_b2"]}
    check("G50-candidate-drift-rate", True,
          "SEALED BARS (drift < %.1f dec end-to-end, rate <= "
          "%.2f dec/deg, n in [%d, N-1]; eligibility = toy "
          "anchor): b1 drift %s rate %s anchor %s; b2 drift %s "
          "rate %s anchor %s (b1 = KKT-edge correction "
          "-gap/(2 ln10); b2 = exact discrete saddle)"
          % (DRIFT_BAR, RATE_BAR, ETA_LO,
             "4/4" if drift_ok["b1"] else "FAIL",
             "4/4" if rate_ok["b1"] else "FAIL",
             "OK" if anchor["b1"] else "FAIL",
             "4/4" if drift_ok["b2"] else "FAIL",
             "4/4" if rate_ok["b2"] else "FAIL",
             "OK" if anchor["b2"] else "FAIL"))
    # orientation gates
    if smoke:
        orient_ok = {"b1": False, "b2": False}
        check("G51-orientation-gates", True,
              "SMOKE: orientation gates skipped")
    else:
        main_pos = all(len(CAND["b2"][kz]["flips"]) == 0
                       for kz in windows)
        oc_note = []
        flips_hit = True
        for cname in ("EPSTEIN", "SMOOTH"):
            nfc = ctrl[cname]["nf"]
            swc = ctrl_sw[cname]
            rc = cand_series(swc, truth_l10(ctrl[cname]["rows"],
                                            swc["ns"]), "b2")
            nf_mod = rc["flips"][0] if rc["flips"] else None
            hit = (nf_mod is not None
                   and abs(nf_mod - nfc) <= FLIP_TOL)
            flips_hit = flips_hit and hit
            oc_note.append("%s: true %d, model first flip %s -> "
                           "%s" % (cname, nfc, str(nf_mod),
                                   "HIT" if hit else "MISS"))
        orient_ok = {"b1": False, "b2": main_pos and flips_hit}
        mf_note = "; ".join(
            "w%d %d flips" % (kz, len(CAND["b2"][kz]["flips"]))
            for kz in windows)
        check("G51-orientation-gates", True,
              "b1: POSITIVE_BY_CONSTRUCTION (no sign channel, "
              "typed); b2 gate A (MAIN sg > 0 to N-1): %s (%s); "
              "gate B (controls, tol +-%d): %s => b2 orientation "
              "%s" % ("PASS" if main_pos else "FAIL", mf_note,
                      FLIP_TOL, "; ".join(oc_note),
                      "CARRIED" if orient_ok["b2"]
                      else "NOT carried"))

    # ---------------- S6: leg C -- sensitivity + handover
    section("S6  LEG C -- ORIENTATION SENSITIVITY + HANDOVER")
    if smoke:
        orient_tok = "SMOKE"
        check("G60-sensitivity", True, "SMOKE: leg C skipped")
        check("G61-handover", True, "SMOKE: handover skipped")
    else:
        dims = []
        sens_note = []
        for cname in ("EPSTEIN", "SMOOTH"):
            nfc = ctrl[cname]["nf"]
            swc = ctrl_sw[cname]
            ns = swc["ns"].astype(int)
            i_f = int(np.flatnonzero(ns == nfc)[0])
            sg_f = int(swc["par"][i_f + 1] * swc["par"][i_f])
            if sg_f < 0:
                dims.append(0)
                sens_note.append("%s: sg^b2(%d) = -1 already "
                                 "-> dim 0" % (cname, nfc))
                continue
            best = (float("inf"), -1, -1, -1)
            for m in (nfc, nfc + 1):
                kb = swc["kept"][m]
                mg, ii, oo = swap_margins(swc["A"], swc["V"],
                                          swc["sgw"], kb["b"])
                if mg < best[0]:
                    best = (mg, ii, oo, m)
            mg, ii, oo, m = best
            kb = swc["kept"][m]
            de = (int(np.min(np.abs(kb["edges"] - ii)))
                  if len(kb["edges"]) else -1,
                  int(np.min(np.abs(kb["edges"] - oo)))
                  if len(kb["edges"]) else -1)
            dims.append(1 if abs(mg) <= MARGIN_BAR else 99)
            sens_note.append("%s: margin_1 %+.2f dec at mass %d "
                             "(swap %d->%d, edge dist %s)"
                             % (cname, mg, m, ii, oo, str(de)))
        dmax = max(dims)
        if dmax <= 1:
            orient_tok = "ORIENTATION_LOWDIM(%d)" % dmax
        else:
            orient_tok = "ORIENTATION_EXTENSIVE"
        check("G60-sensitivity", True,
              "(c1) sealed metric (single-swap energy margin, "
              "bar %.1f dec, k <= 1 searched -- disclosed): %s "
              "=> %s" % (MARGIN_BAR, "; ".join(sens_note),
                         orient_tok))
        ho_note = []
        for cname in ("EPSTEIN", "SMOOTH"):
            nfc = ctrl[cname]["nf"]
            rowsc = ctrl[cname]["rows"]
            band = []
            for n in range(max(1, nfc - 3), nfc + 1):
                lgg = (rowsc[n]["lg_h"] - rowsc[n - 1]["lg_h"]) \
                    / L10
                sgg = rowsc[n]["sg_h"] * rowsc[n - 1]["sg_h"]
                band.append("%+.3f%s" % (lgg,
                                         "+" if sgg > 0
                                         else "-"))
            ho_note.append("%s n=%d..%d lg|gamma| [%s]"
                           % (cname, max(1, nfc - 3), nfc,
                              ", ".join(band)))
        check("G61-handover", True,
              "(c2) r254 handover -- the true gamma band around "
              "the flip (ground truth, handover only, nothing "
              "adjudicated): %s" % "; ".join(ho_note))

    # ---------------- S7: must-fails
    section("S7  MUST-FAILS")
    sw9 = W[windows[0]]
    ns9 = sw9["ns"].astype(int)
    n_mf = 20 if smoke else packs[9]["N"] // 2
    i_mf = int(np.flatnonzero(ns9 == n_mf)[0])
    m1_dev = abs(sw9["q01"][i_mf] - sw9["q01"][i_mf + 1]) \
        / (2.0 * L10)
    ok_m1 = m1_dev >= M1_LOUD_DEC
    ok9 = np.isfinite(LG[windows[0]]) & (ns9 >= ETA_LO)
    med_hon = float(np.median(sw9["corr"][ok9]))
    med_bad = float(np.median(0.5 * sw9["kkt"][ok9] / L10))
    ok_m2 = (med_hon < -M2_MED_MIN and med_bad > M2_MED_MIN)
    ok_mf = True if smoke else (ok_m1 and ok_m2)
    check("G70-must-fails-fire", ok_mf,
          "%sm1 wrong Vandermonde exponent (pair energy once): "
          "moves |log10 h^b2| at w9 n = %d by %.1f dec (bar "
          "%.0f at the sealed degree N//2, amendment a2); m2 "
          "cap-distance sign (lower KKT edge): median "
          "correction flips %+.4f -> %+.4f dec (sign %s, floor "
          "%.0e); m3 circularity: candidate functions "
          "AST-audited in G01 (chain identifiers excluded, "
          "loud); m4 toy anchors adjudicated in G20"
          % ("SMOKE (reduced degree, unadjudicated): "
             if smoke else "", n_mf, m1_dev, M1_LOUD_DEC,
             med_hon, med_bad,
             "FLIPPED" if (med_hon < 0 < med_bad) else "NOT "
             "FLIPPED", M2_MED_MIN))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    if smoke:
        top = "SMOKE_NO_ADJUDICATION"
        toks = [top]
    else:
        carries = [c for c in ("b1", "b2")
                   if anchor[c] and drift_ok[c] and rate_ok[c]
                   and orient_ok[c]]
        rateonly = [c for c in ("b1", "b2")
                    if anchor[c] and drift_ok[c] and rate_ok[c]]
        if carries:
            c = carries[0]
            top = ("NODEBAND_LAYER_CARRIES(%s, rest %.2f)"
                   % (c, max(abs(CAND[c][kz]["rest"])
                             for kz in windows)))
        elif rateonly:
            top = "NODEBAND_RATE_ONLY(%s)" % rateonly[0]
        elif not localized:
            top = "DRIFT_NOT_BAND_LOCALIZED"
        else:
            top = "NODEBAND_LAYER_FAILS"
        geo_tok = (("DRIFT_BAND_LOCALIZED(%.2f)" % med_conc)
                   if localized else "DRIFT_NOT_BAND_LOCALIZED")
        toks = [top]
        if top != geo_tok:
            toks.append(geo_tok)
        toks.append("BANDGEO_FLIP_MARKED" if bandgeo
                    else "BANDGEO_FLIP_UNMARKED")
        toks.append(orient_tok)
        toks.append(lad_tok)
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a geography/"
          "candidate adjudication moves no edge); what the round "
          "adds: the drift geography (transition concentration, "
          "world comparison, N-stability), the sealed b1/b2 "
          "candidate bills, the orientation sensitivity margins, "
          "and the r254 handover band")
    verd = " + ".join(toks)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G81-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: transition geography (4 mains + 2 "
          "controls + 3 ladder rungs), candidate drift/rate/"
          "orientation bills, swap margins, handover band; OPEN: "
          "the budget bound and the base law themselves (r243/"
          "r247/r250/r252 stand); NO RH claim"
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
