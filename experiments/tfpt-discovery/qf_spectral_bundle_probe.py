#!/usr/bin/env python3
"""QF-OFFENSIVE strand 3 -- the moving-frame decider: is the
diagonal-gram wall q_f(X) an artifact of FRAME RIGIDITY?
qf_spectral_bundle_probe (Kato parallel transport of the rank-6
near-kernel spectral projectors along the window ladder).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).  The frame is built
EXCLUSIVELY from the source window operator -- never from target data.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  yosida_qf_convergence_probe -- QF-DEAD on the rigid-frame scalar:
     on the extended comb (ATOM_MAX 4e6, M_TOP 972, X = 15.1875) the
     near-kernel is a STABLE OBJECT (count 5 -> 6 at M = 888, then
     constant over 22 rungs; consecutive alignment min 0.999623) but
     the battery pairing q_f measured against a rigid threshold count
     is non-Cauchy: 12/14 functions break the frozen drift/slope bars
     (worst drift 0.5636, worst rel slope 0.8061/X, both
     R1:hat(R/4,R/4)); orthogonalizing the battery against the frozen
     deepest near-kernel removes 89..99.9% of every battery function
     (the battery is essentially subordinate to the near-kernel).
  *  yosida_handoff_probe -- YOSIDA-PARTIAL: bounded Yosida
     formulation (Q1), identifiable near-kernel (Q2), fixed-f
     monotone eps-limits (Q4) all positive; Q3 (q_f convergence) is
     the single remaining wall.
  *  Prior repo lesson (transport analysis): the relevant direction
     WANDERS with the window; a fixed eigenvector comparison is the
     wrong granularity -- transports must carry the window-dependent
     macro-direction along.  This probe implements exactly that.
  *  handoff_compat_eps3_probe -- the oscillation lesson reused: cell
     statistics are 5-rung medians plus a fitted second-half slope,
     never single endpoints.

SINGLE QUESTION (preregistered): treat the 6-dimensional near-kernel
as a VECTOR BUNDLE over the ladder rungs X_k and transport the
battery coordinates with the canonical Kato partial isometries
(polar factors of P_{k+1} P_k).  Do the transported coordinates
c_k(f) become Cauchy in the moving frame where the rigid-frame
comparison broke -- i.e. was the diagonal-gram wall frame rigidity --
or do they stay non-Cauchy (the wall is in the object, not the
frame), or does the bundle picture itself degenerate (rank/gap/angle
failure) at reachable depth?

PREDECLARED ALGEBRA (honesty, stated BEFORE the run): the composite
transport U_{1,k} is a partial isometry Ran P_1 -> Ran P_k, so the
transported scalar  q_f^T(k) = ||c_k(f)||^2 = ||U_{1,k}^* P_k f||^2
= ||P_k f||^2  is IDENTICALLY the rank-6 band weight -- it is
frame-INDEPENDENT, and on rungs where the threshold count equals 6
it equals the rigid-frame thresholded q_f of the parent probe.  The
moving frame can therefore NEVER repair the scalar level slide by
itself; what it CAN repair is the DIRECTIONAL (coordinate) part.
The decider below is the full vector increment ||c_{k+1} - c_k||,
which controls the scalar (| ||c_{k+1}|| - ||c_k|| | <= ||c_{k+1} -
c_k||) and splits measurably into a radial part |Delta ||c|| | (the
level slide, frame-independent) and an angular remainder (the
directional wandering, exactly what the transport is supposed to
absorb).  The radial/angular split is REPORTED per function so the
verdict cannot be sold as more than it is.  A second declared
asymmetry: the moving-frame statistic is gauge-invariant under
per-rung sign/basis changes of the eigenvectors (Q_k and c_k are
covariant, increments invariant); the rigid-frame comparison is NOT
-- it needs the frozen deterministic sign convention below.  That
gauge dependence IS the frame-rigidity critique made concrete.

FROZEN CONSTRUCTION (everything source-native; reused machinery
verbatim, none invented):
  extended comb = deployed von Mangoldt generator
      (core.von_mangoldt_table) at cap ATOM_MAX_EXT = 4,000,000 with
      the same overlap / Chebyshev-envelope / prefix guards as
      yosida_qf_convergence_probe; tower = continuum lags + atom
      tents on the dyadic grid D = 1/64 (simpler_schur_recursion
      machinery verbatim); battery = module-1 handoff_bulk battery
      (4 boxes + 3 hats per R, l2-normalized, R in {1, 2}; 14
      functions, support <= NPAD = 128 cells).
  ladder: EXT_LAD = 824..972 step 4 (38 rungs, spectra + census);
      GATED BUNDLE RANGE = BUNDLE_LAD = 888..972 step 4 (22 rungs,
      21 neighbor pairs) -- 888 is the FROZEN parent finding for the
      entry of the 6th mode (reproduced by guard G1.5b, never
      re-adjudicated).
  1. per rung X_k: rank-6 spectral projector P_k.  BAND RULE
     (frozen, predeclared): P_k = span of the 6 LOWEST eigenmodes of
     the window operator T[:M_k,:M_k], ALWAYS; the threshold count
     #{lam <= THR_NULL = 1e-4} is computed independently and BOTH
     numbers are reported; gate (a) requires them to AGREE (= 6) on
     every gated rung, so band rule and threshold policy coincide on
     the adjudicated range.  Deterministic sign convention (rigid
     frame only): each eigenvector's largest-|entry| coordinate is
     made positive.
  2. canonical Kato partial isometries: overlap S_k =
     V_{k+1}^T pad(V_k) (6x6), SVD S_k = U Sigma W^T, polar factor
     Q_k = U W^T, i.e. U_{k+1,k} = polar(P_{k+1} P_k) =
     V_{k+1} Q_k V_k^T : Ran P_k -> Ran P_{k+1}.  SVD FLOOR
     (documented): the polar factor is accepted only if
     sigma_min(S_k) >= SVD_FLOOR = 1e-8; below the floor a principal
     angle has reached 90 degrees and the transport is undefined
     (hard kill K3).  Composite transport U_{1,k} by chaining:
     R_1 = I, R_{k+1} = Q_k R_k (so U_{1,k} = V_k R_k V_1^T).
  3. moving-frame coordinates (convention fixed EXACTLY): c_k(f) =
     U_{1,k}^* P_k f expressed in the rung-1 eigenframe, i.e. the
     6-vector c_k(f) = R_k^T a_k(f) with a_k(f) = V_k^T f;
     c_1 = a_1.  Rigid-frame comparison object: a_k(f) with
     index-ordered, sign-fixed eigenvectors (no transport).
FROZEN GRIDS AND BARS (all fixed BEFORE the first run):
  N_MED = 5; increment blocks on the 21 pairs: FIRST5 = pairs 1..5,
      LAST5 = pairs 17..21, second half = pairs 11..21; scalar
      blocks on the 22 rungs: FIRST5 = rungs 888..904, LAST5 =
      rungs 956..972, second half = rungs 932..972; increment X
      coordinate = right-rung X.
  gate (a) RANK STABILITY:   threshold count == 6 on EVERY rung of
      BUNDLE_LAD (band count is 6 by construction; agreement gated).
  gate (b) BAND SEPARATION:  rel gap g_k = (lam_7 - lam_6)/lam_7 >=
      GAP_BAR = 0.10 on every gated rung; full profile reported.
  gate (c) PRINCIPAL ANGLES: (c1) max principal angle theta_max of
      every neighbor pair <= ANG_BAR = 45 deg (bounded away from 90);
      (c2) oscillation-aware falling/flat profile: med5(last 5
      theta_max)/med5(first 5 theta_max) <= ANG_TAIL = 1.5.
  gate (d) TOTAL VARIATION:  TV = sum_k ||P_{k+1} - P_k||_2 =
      sum_k sin(theta_max,k) (equal-rank identity, Ward-checked
      densely at the middle pair to 1e-10); flattening tail
      statistic: last-ceil(21/4)=6-pair share of TV <= TV_TAIL =
      0.40 (a flat profile gives 6/21 = 0.286; growth breaks it);
      med5 ratio and second-half slope of the sin-theta profile
      reported (compat-eps3 pattern).
  gate (e) THE DECIDER (per function, all 14 must pass):
      E1 Cauchy med5:  med5(LAST5 ||c_{k+1}-c_k||) /
                       med5(FIRST5 ||c_{k+1}-c_k||) <= 0.50;
      E2 Cauchy slope: fitted second-half rate b2 of
                       log||c_{k+1}-c_k|| vs X >= 0.02 per X unit
                       (hbp.fit_rate verbatim; still falling, not
                       plateauing);
      E3 scalar:       transported q_f^T = ||c_k||^2 converges on
                       the gated range with the parent bars: med5
                       drift (FIRST5 vs LAST5 rungs) <= 0.15 AND
                       normalized second-half slope <= 0.15 per X
                       unit.  (By the predeclared algebra E3 is a
                       statement about the frame-independent band
                       weight restricted to the stable-rank range;
                       it is gated so the verdict cannot claim
                       "repair" while the level still slides.)
      The rigid-frame table (same E1/E2 statistics on
      ||a_{k+1} - a_k||) is printed SIDE BY SIDE -- this comparison
      is the point of the probe.  Radial share median(|Delta||c|||
      / ||Delta c||) reported per function.
HARD KILLS (frozen, from the offensive's kill list):
  K1 rank not stably 6 on the gated range        -> gate (a) fails;
  K2 bands 6/7 not separable                     -> gate (b) fails;
  K3 a principal angle reaches 90 degrees:
     sigma_min(S_k) < SVD_FLOOR = 1e-8 anywhere  -> transport
     undefined;
  K4 transport requiring any target information  -> AST firewall
     (house style: banned tokens zetazero/nzeros/isprime/primerange/
     nextprime/prevprime/primepi/sympy);
  gate (c) failure (angle bar / growing profile) is likewise a
  bundle-geometry failure -> DEAD.  Transported q_f still non-Cauchy
  with a WELL-DEFINED transport is NOT a kill: per the frozen enum it
  is QF-BUNDLE-PARTIAL (the honest "the wall is in the object"
  outcome).
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall; G0.2 SHA-256 freeze of battery bytes + ladders
  + threshold policy + band rule + every bar BEFORE any comb data is
  built here; G0.3 reach census + runtime cap 600 s predeclared;
  G1.1 extended-table overlap EXACT on [0, 400000]; G1.2 extended
  Chebyshev envelope kappa <= KAPPA_REF + 1e-6; G1.3 parent tower
  comb consistency (rel dev <= 1e-12); G1.4 prefix Ward extended
  tower == parent tower on 824 x 824 (<= 1e-12); G1.5 parent
  reproduction Ward: (a) max thresholded q_f(M = 824) = 0.446 +-
  2e-3, (b) threshold count 5 at M = 884 and 6 at M = 888 (the
  frozen entry rung reproduces); G1.6 measured PD: lambda_min >
  -1e-9 on every EXT rung (PD is measured output; NO gate uses a PD
  margin or 1/eps -- the projector construction needs no
  positivity); G1.7 boundedness audit: every q_f^T in
  [-1e-12, 1 + 1e-9] and every sigma in [0, 1 + 1e-12];
  G2.1 transport orthogonality Ward max||R_k^T R_k - I|| <= 1e-10;
  G2.2 isometry Ward max| ||c_k|| - ||a_k|| | <= 1e-10 (the
  predeclared algebra verified in floats); G2.3 polar Ward
  max|S_k - Q_k H_k| <= 1e-10 (H_k = W Sigma W^T); G2.4 TV identity
  Ward |dense ||P-P'||_2 - sin theta_max| <= 1e-10 at the middle
  pair.
CONTROLS (mandatory, must fire; frozen fire rule): the SAME bundle
  construction (6 lowest modes, threshold census, neighbor angles)
  on CS = position-scrambled extended comb (positions uniform in
  (0.5, 2 alpha_ext), masses kept, seed 7) over CTRL_LAD_S =
  496..512 step 4, and CE = Epstein x^2 + 5y^2 atoms
  (epstein_firewall_probe read-only, tower cap M = 640) over
  CTRL_LAD_E = 624..640 step 4.  FIRE = [rank instability: threshold
  count != 6 on any control rung] OR [gap collapse: rel gap 6/7 <
  GAP_BAR] OR [angle saturation: sigma_min < cos(80 deg) = 0.1736].
  Negative-eigenvalue census printed with each control.  A control
  whose bundle construction stays intact has spuriously converged:
  the run is DEAD.
VERDICT ENUM (frozen):
  QF-BUNDLE-CAUCHY  = guards + controls ok AND gates (a)-(e) all
      pass: the moving frame repairs Cauchy -- the wall was frame
      rigidity; the diagonal route gets its transported coordinates
      (measured rates stated).
  QF-BUNDLE-PARTIAL = guards + controls ok AND transport
      well-defined -- gates (a), (b), (c) pass and no kill -- but
      gate (d) or (e) fails: the transported coordinates still break
      the Cauchy bars (failing functions named and quantified).
  QF-BUNDLE-DEAD    = any guard fails, any control spuriously
      converges, or a hard kill fires (rank/gap/angle failure): the
      bundle picture is wrong at reachable depth.
STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros anywhere; no bare A^{-1}; no PD-margin or 1/eps in any gate;
no fits inside gates beyond the declared bounded-statistic slopes;
no Riemann zeros; NO RH claim.  This probe writes no files.  Runtime
cap 600 s predeclared (dense eigendecompositions at M <= 972).

RESULTS (2026-08-05, first and only preregistered run, 3.8 s; GATES
4/5 -- (a), (b), (c), (d) pass, decider (e) fails 0/14;
GUARDS+CONTROLS 19/19; verdict QF-BUNDLE-PARTIAL):
  *  TRANSPORT WELL-DEFINED -- the bundle picture is RIGHT at
     reachable depth, no hard kill comes close to firing: rank
     exactly 6 (threshold == band) on all 22 gated rungs, deep count
     (lam <= 1e-5) constant 1; rel gap 6/7 = 0.3441..0.5592 (median
     0.5289) vs bar 0.10; max principal angle 2.28..2.72 deg vs bar
     45 with sigma_min >= 0.99887 -- eight decades above the 1e-8
     kill floor -- and med5 tail ratio 0.919 <= 1.5; TV = 0.8877
     with last-6-pair share 0.284 <= 0.40 (per-pair sin theta flat
     at 0.040..0.048; second-half slope -0.130/X, i.e. a mildly
     RISING tail, reported not gated).  Honest outlook inside the
     pass: the 6/7 gap falls monotonically from M = 916 (0.5592) to
     M = 972 (0.3441) -- lam7 is descending toward the band; still
     3.4x the bar, but eroding.
  *  THE FRAME REPAIR IS REAL AND LARGE (the side-by-side point):
     moving-frame med5 increment ratios improve over rigid for
     14/14 functions -- median rigid 26.7 -> moving 1.004.  In the
     rigid (index-ordered, sign-fixed) frame the increments GROW
     16x..48x across the range: the fixed-eigenvector granularity
     is catastrophically wrong, quantitatively confirming the
     transport-analysis lesson that the macro-direction wanders
     with the window.
  *  BUT THE DECIDER FAILS 0/14: transported increments are FLAT,
     not falling -- med5 ratios 0.734..1.080 for 10 functions (bar
     0.50) and two late-growing R2 outliers (box[R/2,R] 18.6,
     hat(3R/4,R/4) 33.0, from near-zero early increments); every
     second-half slope b2 is negative (-0.010..-1.873 vs bar
     +0.02).  E3 scalar: drift 0.090..0.591, rel slope 0.145..0.647
     -- only R2:box[R/2,R] (0.094/0.145) passes both scalar bars;
     the frame-independent band weight drains steeply through the
     gated range, e.g. R1:box[0,R] 0.191 -> 0.081, R2:hat(R/2,R/2)
     0.595 -> 0.381, R2:box[0,R] 0.614 -> 0.440.
  *  RADIAL/ANGULAR SPLIT (the diagnostic this probe was built
     for): radial share 0.45..0.66, median ~0.64 -- the MAJORITY of
     every moving-frame increment is the frame-independent scalar
     drainage |Delta ||c|||, not residual rotation.  Verdict
     content: the Kato frame absorbs the directional wandering
     essentially completely (angles < 3 deg, 14/14 improvement);
     what remains non-Cauchy is the OBJECT-level drainage of the
     battery weight out of the stable 6-band, which no frame can
     repair (predeclared algebra).  All 14 transported levels fall
     through the range -- whether they drain to 0 (which would
     close the Q3 pairing question positively as an asymptotically
     vanishing kernel pairing) is not decidable at this depth.
  *  CONTROLS both fire on the rank AND gap clauses: CS scramble
     (extended comb, 279849 atoms) threshold counts 237..246 vs 6,
     246/512 negative eigenvalues, min rel gap 0.0078; CE Epstein
     counts 251..263 vs 6, 263/640 negative, min rel gap 0.0650.
     Indefinite data destroys rank stability and band separation
     exactly as the fire rule demands (angle clause not needed).
  *  GUARDS 19/19: comb overlap exact (dev 0.0), kappa 0.038821,
     prefix Ward 2.0e-14, parent reproduction q_f(824) = 0.4459
     (dev 1.3e-4) and entry rung 884:5 -> 888:6 reproduced; PD
     margins 8.265e-6 (M 824) -> 6.459e-6 (M 972), measured never
     gated; orthogonality / isometry / polar / TV-identity Wards
     1.1e-14 / 2.6e-15 / 4.0e-15 / 3.1e-15; runtime 3.8 s <= 600 s.
  *  CONSEQUENCE (stated plainly): the Kato transport does NOT open
     the Feshbach 6x6 reduction on this surface -- a 6x6 block
     built in this frame would inherit a non-convergent (draining)
     diagonal -- but the bundle route does NOT die either: the
     frame is sound and cheap (rank/gap/angles/TV all pass with
     wide margins) and the wall is now LOCALIZED in one
     frame-independent scalar per function.  Named next surfaces
     (not probed here): (1) the drainage limit -- does q_f^T -> 0
     on a still deeper comb (asymptotically vanishing pairing,
     Q3 branch (i) in the limit)?  (2) step-1 rung spacing -- are
     the residual angular increments O(step^2) (Kato holonomy
     scaling), so that the moving-frame coordinates have a genuine
     continuum limit with only the radial part left?  NO RH claim,
     no X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_spectral_bundle_probe.py
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

import v563_paper2_readouts as core  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_EXT = 4000000               # extended comb cap (frozen)
M_CAP_EXT = int(math.floor(math.log(ATOM_MAX_EXT) / D))   # 972
M_TOP_EXT = 972                      # deepest rung
M_TOP_PAR = 824                      # parent cap
EXT_LAD = list(range(824, 973, 4))   # 38 rungs (spectra + census)
M_ENTRY = 888                        # frozen parent entry rung (6th)
BUNDLE_LAD = list(range(888, 973, 4))  # 22 gated rungs, 21 pairs

K_RANK = 6                           # bundle rank (frozen)
THR_NULL = 1.0e-4                    # threshold policy (parent)
THR_DEEP = 1.0e-5                    # deep census (reported)
NPAD = 128                           # max battery support in cells
R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
N_MED = 5                            # median block size

# increment blocks (21 pairs) and scalar blocks (22 rungs)
INC_FIRST5 = slice(0, 5)
INC_LAST5 = slice(16, 21)
INC_HALF2 = slice(10, 21)
RUN_FIRST5 = slice(0, 5)             # rungs 888..904
RUN_LAST5 = slice(17, 22)            # rungs 956..972
RUN_HALF2 = slice(11, 22)            # rungs 932..972

GAP_BAR = 0.10                       # (b) rel gap (lam7-lam6)/lam7
ANG_BAR = 45.0                       # (c1) max principal angle, deg
ANG_TAIL = 1.5                       # (c2) med5 last/first ratio
SVD_FLOOR = 1.0e-8                   # K3: polar/90-degree floor
TV_TAIL = 0.40                       # (d) last-quarter TV share
E1_MED = 0.50                        # (e) increment med5 ratio bar
E2_SLOPE = 0.02                      # (e) second-half log-inc rate
E3_DRIFT = 0.15                      # (e) scalar med5 drift bar
E3_SLOPE = 0.15                      # (e) scalar rel slope bar
QF_FLOOR = 1.0e-12                   # denominator floor

PARENT_QF_MAX = 0.446                # parent frozen max q_f (M 824)
REPRO_TOL = 2.0e-3                   # G1.5a reproduction tolerance
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
PD_TOL = 1.0e-9                      # G1.6 measured-PD slack
BOUND_TOL = 1.0e-9                   # G1.7 boundedness slack
WARD_ORTH = 1.0e-10                  # G2.1 R orthogonality
WARD_ISO = 1.0e-10                   # G2.2 ||c|| == ||a||
WARD_POLAR = 1.0e-10                 # G2.3 S == Q H
WARD_TV = 1.0e-10                    # G2.4 dense TV identity
RUNTIME_CAP = 600.0                  # seconds, predeclared

CTRL_ANG_COS = math.cos(math.radians(80.0))   # 0.1736 saturation bar
CTRL_LAD_S = list(range(496, 513, 4))         # scramble control rungs
CTRL_LAD_E = list(range(624, 641, 4))         # Epstein control rungs
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # gates (a)..(e): feed the verdict only


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_spec():
    """Battery bytes + ladders + threshold policy + band rule + every
    bar, SHA-256 frozen BEFORE any comb data is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("qf-spectral-bundle spec: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s; extended comb = deployed "
                "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                "M_TOP=%d; EXT_LAD=%s; BUNDLE_LAD=%s (entry rung %d "
                "frozen from parent); band rule = 6 LOWEST modes "
                "always, threshold policy thr=%g must agree on gated "
                "rungs, sign fix = largest-|entry| positive (rigid "
                "frame only); K=%d; blocks inc[0:5]/[16:21]/[10:21] "
                "run[0:5]/[17:22]/[11:22] Nmed=%d; bars: gap>=%g "
                "ang<=%g tail<=%g svdfloor=%g tv<=%g e1<=%g e2>=%g "
                "e3 drift<=%g slope<=%g floor=%g; repro qfmax=%g "
                "tol=%g; guards: comb<=%g prefix<=%g pd>=-%g "
                "bound<=%g orth<=%g iso<=%g polar<=%g tvward<=%g "
                "runtime<=%g; controls: angcos=%.6f lads=%s/%s "
                "epcap=%d epM=%d seed=%d"
                % (D, R_BAT, ATOM_MAX_EXT, M_CAP_EXT, M_TOP_EXT,
                   EXT_LAD, BUNDLE_LAD, M_ENTRY, THR_NULL, K_RANK,
                   N_MED, GAP_BAR, ANG_BAR, ANG_TAIL, SVD_FLOOR,
                   TV_TAIL, E1_MED, E2_SLOPE, E3_DRIFT, E3_SLOPE,
                   QF_FLOOR, PARENT_QF_MAX, REPRO_TOL, COMB_DEV_BAR,
                   PREFIX_WARD, PD_TOL, BOUND_TOL, WARD_ORTH,
                   WARD_ISO, WARD_POLAR, WARD_TV, RUNTIME_CAP,
                   CTRL_ANG_COS, CTRL_LAD_S, CTRL_LAD_E, EP_NCAP,
                   EP_MMAX, SEED)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_matrix(bats):
    """All 14 battery functions zero-padded to NPAD cells + names."""
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(NPAD)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


# ------------------------------------------------ towers (verbatim)
def build_parent_tower():
    alpha = 0.5 * M_TOP_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss "
          "double sieve == deployed masses, rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha))
    c = srp.continuum_lags(M_TOP_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_TOP_PAR, masks[cnl])
    return sla.toeplitz(c[:M_TOP_PAR])


def build_extended_comb():
    lam_ext = core.von_mangoldt_table(ATOM_MAX_EXT)
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 extended-table overlap: extended von Mangoldt table "
          "== deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_ext > 0.0)[0]
    u_ext = np.log(nn.astype(float))
    mu_ext = 2.0 * lam_ext[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_ext[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 extended-range Chebyshev envelope: kappa = %.6f over "
          "all jump points of psi(x)/x in [%.0f, %d] <= KAPPA_REF + "
          "%.0e = %.6f" % (kappa, core.KAPPA_X0, ATOM_MAX_EXT,
                           core.TOL_KAPPA,
                           core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_ext, mu_ext


def build_extended_tower(u_ext, mu_ext, T_par):
    alpha = 0.5 * M_TOP_EXT * D
    ka = int(np.searchsorted(u_ext, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP_EXT)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP_EXT, u_ext[:ka],
                                  mu_ext[:ka])
    T = sla.toeplitz((c_cont + c_at)[:M_TOP_EXT])
    dev = float(np.max(np.abs(T[:M_TOP_PAR, :M_TOP_PAR] - T_par)))
    check("G1.4 prefix Ward: extended tower leading %d x %d block == "
          "parent tower, max abs dev %.1e <= %.0e"
          % (M_TOP_PAR, M_TOP_PAR, dev, PREFIX_WARD),
          dev <= PREFIX_WARD)
    print("  extension census: ka = %d atoms to e^%.4f" % (ka,
                                                           2.0 * alpha))
    return T, c_cont, alpha, ka


# ------------------------------------------------ spectral ladder
def sign_fix(V):
    """Frozen deterministic sign convention (rigid frame): the
    largest-|entry| coordinate of each column is made positive."""
    W = V.copy()
    for j in range(W.shape[1]):
        i = int(np.argmax(np.abs(W[:, j])))
        if W[i, j] < 0.0:
            W[:, j] = -W[:, j]
    return W


def spectral_pass(T):
    """One dense eigendecomposition per EXT rung.  Stored: spectrum,
    the sign-fixed 6-lowest band basis (full length, for projectors /
    angles), first-NPAD rows of the thresholded near-null basis (for
    the parent reproduction Ward)."""
    out = {}
    for M in EXT_LAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        idx = np.nonzero(lam <= THR_NULL)[0]
        out[M] = dict(M=M, lam=lam, Vb=sign_fix(V[:, :K_RANK]),
                      Vn128=V[:NPAD, idx].copy(),
                      nn=len(idx),
                      nn_deep=int(np.sum(lam <= THR_DEEP)),
                      lam6=float(lam[K_RANK - 1]),
                      lam7=float(lam[K_RANK]))
    return out


def lin_slope(xs, ys):
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return float(coef[1])


def fit_b2(xs, vals):
    """Second-half falling rate via hbp.fit_rate verbatim
    (log val = a - b * x; b > 0 = falling)."""
    rows = [dict(XmR=float(x), mx=float(v)) for x, v in zip(xs, vals)]
    b, _resid = hbp.fit_rate(rows)
    return b


# ------------------------------------------------ bundle transport
def bundle_transport(spec, F):
    """The frozen construction: overlaps, polar factors, chained
    transport, moving-frame coordinates.  Returns everything the
    gates need plus the Ward numbers."""
    blks = [spec[M] for M in BUNDLE_LAD]
    a = [blk["Vb"][:NPAD, :].T @ F for blk in blks]      # 6 x 14 each

    Qs, sig_min, theta_max = [], [], []
    sig_max_all = 0.0
    ward_polar = 0.0
    for bl_a, bl_b in zip(blks, blks[1:]):
        S = bl_b["Vb"][:bl_a["M"], :].T @ bl_a["Vb"]     # 6 x 6
        U, s, Wt = np.linalg.svd(S)
        Q = U @ Wt
        H = Wt.T @ np.diag(s) @ Wt
        ward_polar = max(ward_polar,
                         float(np.max(np.abs(S - Q @ H))))
        Qs.append(Q)
        sig_min.append(float(s[-1]))
        sig_max_all = max(sig_max_all, float(s[0]))
        th = np.degrees(np.arccos(np.clip(s, 0.0, 1.0)))
        theta_max.append(float(np.max(th)))

    R = np.eye(K_RANK)
    Rs = [R]
    for Q in Qs:
        R = Q @ R
        Rs.append(R)
    ward_orth = max(float(np.max(np.abs(Rk.T @ Rk - np.eye(K_RANK))))
                    for Rk in Rs)
    c = [Rk.T @ ak for Rk, ak in zip(Rs, a)]             # 6 x 14 each
    ward_iso = max(float(np.max(np.abs(
        np.linalg.norm(ck, axis=0) - np.linalg.norm(ak, axis=0))))
        for ck, ak in zip(c, a))

    # dense TV-identity Ward at the middle pair
    mid = len(Qs) // 2
    bl_a, bl_b = blks[mid], blks[mid + 1]
    Va = np.zeros((bl_b["M"], K_RANK))
    Va[:bl_a["M"], :] = bl_a["Vb"]
    Pdiff = bl_b["Vb"] @ bl_b["Vb"].T - Va @ Va.T
    tv_dense = float(np.linalg.svd(Pdiff, compute_uv=False)[0])
    tv_ident = math.sqrt(max(0.0, 1.0 - sig_min[mid] ** 2))
    ward_tv = abs(tv_dense - tv_ident)

    return dict(blks=blks, a=a, c=c, sig_min=sig_min,
                sig_max_all=sig_max_all, theta_max=theta_max,
                ward_polar=ward_polar, ward_orth=ward_orth,
                ward_iso=ward_iso, ward_tv=ward_tv, mid=mid)


# ------------------------------------------------ gates (a)-(d)
def gates_geometry(bun):
    blks = bun["blks"]
    xs = np.array([b["M"] * D for b in blks])

    # (a) rank stability: threshold count == band rank 6
    nns = [b["nn"] for b in blks]
    print("\n-- gate (a): rank stability on BUNDLE_LAD (band rule = "
          "6 lowest always; threshold count thr = %g reported and "
          "gated)" % THR_NULL)
    print("  threshold count profile: %s"
          % "/".join(str(n) for n in nns))
    print("  deep count (lam <= %g) profile: %s"
          % (THR_DEEP, "/".join(str(b["nn_deep"]) for b in blks)))
    ga = gate("(a) RANK STABILITY: threshold count == %d on every "
              "one of the %d gated rungs (band rule and threshold "
              "policy agree)" % (K_RANK, len(blks)),
              all(n == K_RANK for n in nns),
              "counts %d..%d" % (min(nns), max(nns)))

    # (b) band separation 6/7
    gaps = [(b["lam7"] - b["lam6"]) / b["lam7"] for b in blks]
    print("  gap profile (M, lam6, lam7, rel gap):")
    for b, g in zip(blks, gaps):
        print("    M=%d  lam6 = %.4e  lam7 = %.4e  gap = %.4f"
              % (b["M"], b["lam6"], b["lam7"], g))
    gb = gate("(b) BAND SEPARATION: min rel gap (lam7-lam6)/lam7 = "
              "%.4f >= %g on every gated rung (max %.4f, median "
              "%.4f)" % (min(gaps), GAP_BAR, max(gaps),
                         float(np.median(gaps))),
              min(gaps) >= GAP_BAR)

    # (c) principal angles of neighboring projectors
    th = bun["theta_max"]
    print("  max principal angle per pair (deg): %s"
          % "/".join("%.2f" % t for t in th))
    med_f = float(np.median(th[:N_MED]))
    med_l = float(np.median(th[-N_MED:]))
    tail = med_l / max(med_f, QF_FLOOR)
    c1 = max(th) <= ANG_BAR
    c2 = tail <= ANG_TAIL
    gc = gate("(c) PRINCIPAL ANGLES: max angle = %.2f deg <= %g "
              "(worst pair M=%d->%d) AND med%d tail ratio = %.3f <= "
              "%g (falling/flat profile); sigma_min overall = %.6f"
              % (max(th), ANG_BAR,
                 bun["blks"][int(np.argmax(th))]["M"],
                 bun["blks"][int(np.argmax(th)) + 1]["M"], N_MED,
                 tail, ANG_TAIL, min(bun["sig_min"])), c1 and c2)

    # K3 hard kill: 90-degree / SVD floor
    k3_ok = check("K3 kill audit: min sigma_min(S_k) = %.6e >= SVD "
                  "floor %.0e (no principal angle reaches 90 deg; "
                  "polar transport well-defined everywhere)"
                  % (min(bun["sig_min"]), SVD_FLOOR),
                  min(bun["sig_min"]) >= SVD_FLOOR)

    # (d) total variation of the projector path
    sins = [math.sqrt(max(0.0, 1.0 - s ** 2)) for s in bun["sig_min"]]
    tv = float(np.sum(sins))
    n_q = int(math.ceil(len(sins) / 4.0))
    share = float(np.sum(sins[-n_q:])) / max(tv, QF_FLOOR)
    med_ratio = float(np.median(sins[-N_MED:])) \
        / max(float(np.median(sins[:N_MED])), QF_FLOOR)
    b2_tv = fit_b2(xs[1:][INC_HALF2], np.array(sins)[INC_HALF2])
    print("  TV profile ||P_{k+1}-P_k||_2 = sin theta_max: %s"
          % "/".join("%.4f" % s for s in sins))
    print("  TV report (compat-eps3 pattern): med%d last/first = "
          "%.3f, second-half slope b2 = %+.3f/X (reported)"
          % (N_MED, med_ratio, b2_tv))
    gd = gate("(d) TOTAL VARIATION: sum = %.4f; last-%d-pair share "
              "= %.3f <= %g (flat profile would give %.3f; "
              "flattening tail)" % (tv, n_q, share, TV_TAIL,
                                    n_q / len(sins)),
              share <= TV_TAIL)
    return ga, gb, gc, gd, k3_ok


# ------------------------------------------------ gate (e): decider
def inc_stats(deltas, xs_inc):
    """Frozen oscillation-aware Cauchy statistic per function on the
    21 increments: med5 ratio + second-half falling rate."""
    med_f = np.median(deltas[INC_FIRST5], axis=0)
    med_l = np.median(deltas[INC_LAST5], axis=0)
    ratio = med_l / np.maximum(med_f, QF_FLOOR)
    b2 = np.array([fit_b2(xs_inc[INC_HALF2], deltas[INC_HALF2, j])
                   for j in range(deltas.shape[1])])
    return ratio, b2


def gate_decider(bun, names):
    blks = bun["blks"]
    xs = np.array([b["M"] * D for b in blks])
    xs_inc = xs[1:]                              # right-rung X

    A = np.stack(bun["a"])                       # (22, 6, 14)
    C = np.stack(bun["c"])                       # (22, 6, 14)
    d_rig = np.linalg.norm(np.diff(A, axis=0), axis=1)   # (21, 14)
    d_mov = np.linalg.norm(np.diff(C, axis=0), axis=1)   # (21, 14)
    q = np.sum(C ** 2, axis=1)                   # (22, 14) scalar

    rig_ratio, rig_b2 = inc_stats(d_rig, xs_inc)
    mov_ratio, mov_b2 = inc_stats(d_mov, xs_inc)

    # E3: transported scalar convergence (parent A1/A2 bars, gated
    # range) -- by the predeclared algebra this is the band weight
    med_f = np.median(q[RUN_FIRST5], axis=0)
    med_l = np.median(q[RUN_LAST5], axis=0)
    drift = np.abs(med_l - med_f) \
        / np.maximum(np.maximum(med_l, med_f), QF_FLOOR)
    rel_slope = np.array([abs(lin_slope(xs[RUN_HALF2],
                                        q[RUN_HALF2, j]))
                          / max(float(np.mean(q[RUN_HALF2, j])),
                                QF_FLOOR)
                          for j in range(q.shape[1])])

    # radial/angular split (reported): share of |Delta||c||| in the
    # full increment, median over pairs
    rad = np.abs(np.diff(np.sqrt(np.maximum(q, 0.0)), axis=0))
    rad_share = np.median(rad / np.maximum(d_mov, QF_FLOOR), axis=0)

    print("\n-- gate (e): THE DECIDER -- per-function transported-"
          "coordinate Cauchy table, RIGID vs MOVING frame side by "
          "side (med5 = med5(last)/med5(first) of ||increment||, "
          "bar <= %g; b2 = second-half falling rate/X, bar >= %g; "
          "scalar bars drift <= %g, slope <= %g/X)"
          % (E1_MED, E2_SLOPE, E3_DRIFT, E3_SLOPE))
    print("  %-18s %-17s %-17s %6s  %-15s %s"
          % ("function", "RIGID med5 / b2", "MOVING med5 / b2",
             "radsh", "scalar dr / sl", "E1 E2 E3 -> gate"))
    e_pass = []
    for j, nm in enumerate(names):
        e1 = mov_ratio[j] <= E1_MED
        e2 = mov_b2[j] >= E2_SLOPE
        e3 = drift[j] <= E3_DRIFT and rel_slope[j] <= E3_SLOPE
        ok = e1 and e2 and e3
        e_pass.append(ok)
        print("  %-18s %6.3f / %+6.3f   %6.3f / %+6.3f   %5.2f  "
              "%5.3f / %5.3f   %s %s %s -> %s"
              % (nm, rig_ratio[j], rig_b2[j], mov_ratio[j],
                 mov_b2[j], rad_share[j], drift[j], rel_slope[j],
                 "ok" if e1 else "E1", "ok" if e2 else "E2",
                 "ok" if e3 else "E3", "pass" if ok else "FAIL"))
    n_impr = int(np.sum(mov_ratio < rig_ratio))
    print("  moving-frame med5 ratio improves over rigid for %d/14 "
          "functions (median rigid %.3f -> moving %.3f)"
          % (n_impr, float(np.median(rig_ratio)),
             float(np.median(mov_ratio))))
    print("  transported q_f^T levels (frame-independent band "
          "weight): first gated rung M=%d vs deepest M=%d:"
          % (blks[0]["M"], blks[-1]["M"]))
    for j, nm in enumerate(names):
        print("    %-18s q^T(%d) = %.4f   q^T(%d) = %.4f"
              % (nm, blks[0]["M"], q[0, j], blks[-1]["M"],
                 q[-1, j]))

    qmin, qmax = float(np.min(q)), float(np.max(q))
    check("G1.7 boundedness audit: every q_f^T in [%.1e, %.4f] "
          "inside [-1e-12, 1 + %.0e]; every sigma in [%.6f, %.6f] "
          "<= 1 + 1e-12 -- bounded objects only, no 1/eps, no "
          "PD margin in any gate"
          % (qmin, qmax, BOUND_TOL, min(bun["sig_min"]),
             bun["sig_max_all"]),
          qmin >= -1.0e-12 and qmax <= 1.0 + BOUND_TOL
          and bun["sig_max_all"] <= 1.0 + 1.0e-12)

    n_fail = sum(1 for ok in e_pass if not ok)
    ge = gate("(e) DECIDER: transported coordinates Cauchy for all "
              "14 functions (E1 med5 <= %g AND E2 b2 >= %g AND E3 "
              "scalar drift/slope <= %g/%g) -- %d/14 pass, %d fail"
              % (E1_MED, E2_SLOPE, E3_DRIFT, E3_SLOPE,
                 14 - n_fail, n_fail), n_fail == 0)
    return ge, e_pass


# ------------------------------------------------ controls
def control_bundle(Tc, lad, label):
    """The SAME bundle construction on control data; frozen fire
    rule: rank instability OR gap collapse OR angle saturation."""
    blks = []
    for M in lad:
        lam, V = np.linalg.eigh(Tc[:M, :M])
        blks.append(dict(M=M, lam=lam, Vb=V[:, :K_RANK],
                         nn=int(np.sum(lam <= THR_NULL))))
    nns = [b["nn"] for b in blks]
    gaps = [(b["lam"][K_RANK] - b["lam"][K_RANK - 1])
            / max(abs(b["lam"][K_RANK]), QF_FLOOR) for b in blks]
    sigs = []
    for bl_a, bl_b in zip(blks, blks[1:]):
        S = bl_b["Vb"][:bl_a["M"], :].T @ bl_a["Vb"]
        sigs.append(float(np.linalg.svd(S, compute_uv=False)[-1]))
    nneg = int(np.sum(blks[-1]["lam"] < 0.0))
    rank_bad = any(n != K_RANK for n in nns)
    gap_bad = min(gaps) < GAP_BAR
    ang_bad = min(sigs) < CTRL_ANG_COS
    fire = rank_bad or gap_bad or ang_bad
    det = ("%s: threshold counts %s (vs %d), %d/%d negative "
           "eigenvalues at top rung; min rel gap 6/7 = %.4f (bar "
           "%g); min sigma_min = %.4f (saturation bar %.4f); fire "
           "on [rank=%s gap=%s angle=%s]"
           % (label, "/".join(str(n) for n in nns), K_RANK, nneg,
              blks[-1]["M"], min(gaps), GAP_BAR, min(sigs),
              CTRL_ANG_COS, rank_bad, gap_bad, ang_bad))
    return fire, det


def run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext):
    print("\n-- controls (must fire: indefinite data must destroy "
          "the bundle construction measurably)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_ext, ka_ext))
    cat_s, _dd = core.atom_lags_at(alpha_ext, M_TOP_EXT, pos,
                                   mu_ext[:ka_ext])
    Ts = sla.toeplitz((c_cont_ext + cat_s)[:M_TOP_EXT])
    fire_s, det_s = control_bundle(Ts, CTRL_LAD_S, "scramble")
    check("CS position-scramble control (extended comb, %d atoms) "
          "fires" % ka_ext, fire_s, det_s)

    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX, posE,
                                  masE)
    cont = srp.continuum_lags(EP_MMAX)
    TE = sla.toeplitz((cont + catE)[:EP_MMAX])
    fire_e, det_e = control_bundle(TE, CTRL_LAD_E, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 3 -- spectral bundle: Kato parallel "
          "transport of the rank-6 near-kernel along the ladder")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (K4: transport uses no target "
          "information)", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + threshold policy + band rule + "
          "bars SHA-256-frozen BEFORE any comb data is built here",
          True, "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d "
          "(X = %.6f <= %.6f); sieve cover exp(X_top) + 2 = %d <= "
          "%d; runtime cap %.0f s predeclared"
          % (M_TOP_EXT, ATOM_MAX_EXT, M_CAP_EXT, M_TOP_EXT * D,
             math.log(ATOM_MAX_EXT),
             int(math.exp(M_TOP_EXT * D)) + 2, ATOM_MAX_EXT,
             RUNTIME_CAP),
          M_TOP_EXT <= M_CAP_EXT
          and int(math.exp(M_TOP_EXT * D)) + 2 <= ATOM_MAX_EXT)

    # ---- comb + towers strictly after the freeze
    u_ext, mu_ext = build_extended_comb()
    T_par = build_parent_tower()
    T, c_cont_ext, alpha_ext, ka_ext = build_extended_tower(
        u_ext, mu_ext, T_par)

    # ---- spectra on the full EXT ladder
    spec = spectral_pass(T)
    F, names = battery_matrix(bats)
    print("  PD margins (measured, never gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[M_TOP_PAR]["lam"][0], M_TOP_PAR,
             spec[M_TOP_EXT]["lam"][0], M_TOP_EXT))
    pd_min = min(float(spec[M]["lam"][0]) for M in EXT_LAD)
    check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every EXT "
          "rung (measured output; no gate uses a PD margin or "
          "1/eps)" % (pd_min, PD_TOL), pd_min > -PD_TOL)

    # G1.5 parent reproduction Wards
    q824 = float(np.max(np.sum((spec[M_TOP_PAR]["Vn128"].T @ F) ** 2,
                               axis=0)))
    dev_q = abs(q824 - PARENT_QF_MAX)
    check("G1.5a parent reproduction Ward: max thresholded q_f(M = "
          "%d) = %.4f vs frozen %.3f (dev %.1e <= %.0e)"
          % (M_TOP_PAR, q824, PARENT_QF_MAX, dev_q, REPRO_TOL),
          dev_q <= REPRO_TOL)
    check("G1.5b entry-rung reproduction: threshold count %d at M = "
          "884 and %d at M = %d (frozen parent finding: 6th mode "
          "enters at %d)" % (spec[884]["nn"], spec[M_ENTRY]["nn"],
                             M_ENTRY, M_ENTRY),
          spec[884]["nn"] == 5 and spec[M_ENTRY]["nn"] == 6)
    print("  threshold count along full EXT ladder: %s"
          % "/".join(str(spec[M]["nn"]) for M in EXT_LAD))

    # ---- bundle transport + Wards
    bun = bundle_transport(spec, F)
    check("G2.1 transport orthogonality Ward: max ||R_k^T R_k - I|| "
          "= %.1e <= %.0e" % (bun["ward_orth"], WARD_ORTH),
          bun["ward_orth"] <= WARD_ORTH)
    check("G2.2 isometry Ward: max | ||c_k|| - ||a_k|| | = %.1e <= "
          "%.0e (predeclared algebra ||c|| = ||P f|| verified in "
          "floats)" % (bun["ward_iso"], WARD_ISO),
          bun["ward_iso"] <= WARD_ISO)
    check("G2.3 polar Ward: max |S_k - Q_k H_k| = %.1e <= %.0e"
          % (bun["ward_polar"], WARD_POLAR),
          bun["ward_polar"] <= WARD_POLAR)
    check("G2.4 TV identity Ward at middle pair (M %d -> %d): "
          "|dense ||P'-P||_2 - sin theta_max| = %.1e <= %.0e"
          % (bun["blks"][bun["mid"]]["M"],
             bun["blks"][bun["mid"] + 1]["M"], bun["ward_tv"],
             WARD_TV), bun["ward_tv"] <= WARD_TV)

    # ---- gates
    ga, gb, gc, gd, k3_ok = gates_geometry(bun)
    ge, _e_pass = gate_decider(bun, names)

    # ---- controls
    run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext)

    # ---- runtime guard (predeclared)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    hard_kill = not (ga and gb and gc and k3_ok)
    if not (guards_ok and controls_ok):
        verdict = "QF-BUNDLE-DEAD"
    elif hard_kill:
        verdict = "QF-BUNDLE-DEAD"
    elif gd and ge:
        verdict = "QF-BUNDLE-CAUCHY"
    else:
        verdict = "QF-BUNDLE-PARTIAL"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             time.time() - T_START))
    if verdict == "QF-BUNDLE-CAUCHY":
        print("CONSEQUENCE (stated plainly): the wall WAS frame "
              "rigidity -- in the Kato-transported moving frame the "
              "battery coordinates are Cauchy at the frozen bars and "
              "the transported scalar converges on the stable-rank "
              "range: the diagonal route gets its transported "
              "coordinates and the Feshbach 6x6 reduction (next "
              "module) has a well-defined convergent frame to live "
              "in.  NOT claimed: X -> infinity, eps-uniformity, RH.")
    elif verdict == "QF-BUNDLE-PARTIAL":
        print("CONSEQUENCE (stated plainly): the transport is "
              "WELL-DEFINED (rank/gap/angles pass -- the bundle "
              "picture is right) but the transported coordinates "
              "still break the Cauchy bars: the wall is in the "
              "OBJECT, not (only) the frame.  The failing functions "
              "and the radial/angular split above quantify how much "
              "is irreparable level slide vs residual rotation.  A "
              "Feshbach 6x6 reduction on this frame would inherit a "
              "non-convergent block -- it is NOT opened by this "
              "run.  NO RH claim.")
    else:
        print("CONSEQUENCE (stated plainly): a hard kill fired or "
              "the run is invalid -- the bundle picture is wrong at "
              "reachable depth (rank/gap/angle failure), and the "
              "moving-frame route dies honestly here.  NO RH claim.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
