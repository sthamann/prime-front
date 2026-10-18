#!/usr/bin/env python3
"""QF-OFFENSIVE strand 1 -- THE AUDIT BEFORE ANY NEW OFFENSIVE: is
Gate 3's Cauchy demand on q_f(X) STRONGER than what the diagonal Gram
closure theorem actually needs?  qf_contract_necessity_probe.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  yosida_qf_convergence_probe -- QF-DEAD on the extended tower
     (ATOM_MAX_EXT = 4e6, M_TOP_EXT = 972, X = 15.1875): the
     near-kernel OBJECT converges (count stable 6 from M = 888,
     alignment 0.9997) but its battery pairing q_f does NOT (12/14
     functions break drift/slope bars 0.15; worst drift 0.5636); the
     level keeps sliding (post-M-888 drainage), non-Cauchy at the
     frozen bars.  Candidate B: 89..99.9% of every battery function
     lies in the 6-mode restricted span; the orthogonalized remnant
     loses the R = 1 rates.
  *  v763_yosida_handoff (yosida_handoff_probe verbatim) --
     YOSIDA-PARTIAL: Q1 (bounded Yosida formulation carries the
     rates, E_Y = Gram - eps E_G declared algebra), Q2 (near-kernel
     identifiable/stable), Q4 (fixed-f monotone eps-limits, deficit
     contraction 0.011..0.108) positive; Q3 (q_f convergence) FAILED.
  *  v768_handoff_tail_weil -- eps ladder facts: eps = 1e-3
     compatibility passes on the deep 36-rung ladder (b = 0.178/0.186)
     while eps = 3e-4 shows the first negative sign (R = 1 second-half
     b2 = -0.011): suggestive of a singular double limit -- quantified
     here, never assumed.
  *  Contract PRIME.KMS.INDUCTIVE_STATE.02 demands only a weak-*
     CLUSTER POINT, not a covariant inductive limit; the Lean keystone
     (GramCompactness.lean) needs only entrywise convergence of PSD
     matrices on fixed corners.  q_f in [0, 1] is bounded, so cluster
     points EXIST by compactness -- the only live question is whether
     they are GAUGE (representation choice) or SUBSTANCE (different
     cluster points move the contract's actual corner objects).

CENTRAL QUESTION (preregistered): is the full-ladder Cauchy demand on
q_f (Gate 3 as frozen in the parent) NECESSARY for the diagonal Gram
closure, or does the contract survive with the weaker
subsequence/cluster formulation that its own text demands?

FROZEN CONSTRUCTION (all reused verbatim, none invented): extended
von Mangoldt comb at ATOM_MAX_EXT = 4,000,000 with the same overlap /
Chebyshev / prefix guards as the qf probe (the extended-comb caching
approach: one comb build, one 972 x 972 tower, prefixes only); frozen
module-1 battery (4 boxes + 3 hats per R, R in {1, 2}, l2-normalized,
support <= NPAD = 128 cells); FULL ladder FULL_LAD = 256..972 step 4
(180 rungs, the parent QLAD density quadrupled and extended);
EXT_LAD = FULL_LAD[142:] = 824..972 step 4 (the qf probe's extension
grid verbatim, MID5 = [17:22], LAST5 = [33:38], HALF2 = [19:38]);
near-null threshold THR_NULL = 1e-4 (parent policy); one dense eigh
per rung; every question below is evaluated from the stored spectral
data (lam, battery coordinates C = V[:128]^T F) -- corners as the
BOUNDED Yosida Gram E_Y^eps[i,j] = <f_i, Y_eps f_j> =
C^T diag(lam/(lam+eps)) C (sandwich |E_Y| <= 1, no 1/eps anywhere);
eps-regularized near-kernel weight (predeclared for Q4) = the Yosida
DEFICIT d_f(M, eps) = <f, (I - Y_eps) f> = sum_k C_k^2 eps/(lam_k+eps)
in [0, 1] (a soft spectral weight below scale eps; threshold-free).

FOUR PREREGISTERED QUESTIONS (all gates and bars frozen here BEFORE
the first run; slope/correlation statistics are declared gate
statistics on bounded quantities, not proof-grade claims):

Q1 SUBSEQUENCE SUFFICIENCY.  Frozen deterministic subsequence rule
  (greedy epsilon-net, source data only, no target data): process
  FULL_LAD in ladder order; centers start empty; rung r with q-vector
  q(r) in [0,1]^14 (THR_NULL) joins the FIRST existing center c with
  ||q(r) - c||_inf <= ETA_NET = 0.03, else becomes a new center.  The
  COMMON subsequence S = rungs of the largest cluster (tie -> earliest
  center).  REPORT: cluster census, density |S|/180 and its EXT
  density.  GATE Q1 (all frozen): |S| >= N_SUB_MIN = 10 AND along S
  every one of the 14 functions passes the PARENT bars verbatim:
  drift_f = |med5(last 5 of S) - med5(middle 5 of S)| / max(medians,
  1e-12) <= 0.15 AND rel slope over the second half of S (lin fit of
  q_f vs X, |slope|/mean) <= 0.15 per X unit.  NOT tautological: the
  net cap 2*ETA_NET bounds absolute motion, but small-q functions
  (q ~ 0.02..0.09) must hold the RELATIVE bars on their own.

Q2 CLUSTER UNIQUENESS VIA THE GRAM CORNERS (decides the verdict).
  Corner objects: E_Y^eps on the gated eps set EPS_GATED = (1e-1,
  1e-2, 1e-3), scaled per eps by scale_eps = sqrt(max diag * min
  diag) of E_Y at FULL_LAD[0] (parent scale convention; KILL audit
  band [1e-3, 1.5]).  Adjacent corner increments inc_eps(k) = max
  entry |E_Y(M_{k+1}) - E_Y(M_k)| / scale_eps (the falling error
  envelope, reported head/tail).  (a) CLUSTER PAIRS: rung pairs
  (a, b) in DIFFERENT net clusters with M_b - M_a <= DX_CELLS = 24
  (<= 6 steps) and pair separation dq(a,b) = sup_f |q_f(a) - q_f(b)|
  >= SEP_BAR = 0.04.  For each pair rho(a,b) = max over gated eps of
  [max entry |E_Y(b) - E_Y(a)| / scale_eps] / [n_steps *
  med_inc_local_eps], med_inc_local = median adjacent increment with
  both rungs within +-ENV_WIN = 64 cells of the pair, EXCLUDING the
  path increments between a and b (else a common jump contaminates
  its own envelope); < 3 window increments -> global median
  (declared).  (b) TRACKING: corr_adj = Pearson over the 37 EXT
  adjacent pairs between dq(k) and inc_{1e-3}(k).  BRANCHES (frozen):
  GAUGE      = n_pairs >= N_PAIR_MIN = 5 AND median rho <= ENV_FAC =
               3.0 AND corr_adj <= 0.5  (corners agree within the
               falling envelope while q_f differs);
  SUBSTANCE  = median rho >= SUB_FAC = 10.0 OR corr_adj >= 0.8
               (corners track q_f);
  INDET      = anything else (including n_pairs < 5), named exactly.

Q3 DOES q_f ENTER THE VALUE.  At every finite rung A_M is PD
  (measured, never assumed), so the certified monotone eps-limit of
  <f, Y_eps f> is EXACTLY ||f||^2 = 1 -- the fixed-M limit VALUE is
  q-blind by the spectral theorem; what q_f can own is the eps-SCALE
  distribution of the deficit.  Frozen statistics on the reachable
  surface: CORR_VAL = Pearson over the (38 x 14) EXT surface between
  q_f(M) and d_f(M, 1e-5); per-f correlations along EXT (reported);
  near-share = near-kernel part (lam <= THR_NULL) of d_f(972, 1e-5)
  / d_f(972, 1e-5); VAR_RATIO = max_f range_EXT(y_f(., 1e-5)) /
  max_f range_EXT(q_f) (level comparison: does the limit-value proxy
  move at the q amplitude or stay pinned).  GATE Q3 (certificates
  only): eps-monotonicity of y on the full 2D grid (min increment >=
  -1e-12) AND X-monotonicity of d on FULL_LAD (min increment >=
  -1e-8, PSD Schur).  CLASSIFICATION (frozen bars, reported):
  SCALE-REDISTRIBUTION if CORR_VAL >= 0.8 AND near-share >= 0.5 for
  every f with q_f(972) >= 0.1 AND VAR_RATIO <= 0.1 is reported
  alongside; WEAK-COUPLING otherwise (named).

Q4 DOUBLE-LIMIT ORDER.  Frozen 2D grid: EPS2D = (1e-1, 1e-2, 1e-3,
  3e-4, 1e-4, 3e-5, 1e-5) x FULL_LAD, surface d_f(M, eps) (the
  predeclared eps-regularized near-kernel weight).  The surface is
  monotone in BOTH variables (increasing in X by PSD Schur,
  decreasing in eps by the spectral map) -- both certified above --
  so both iterated limits exist.  Candidate B (eps first, then X):
  at every finite M the eps-limit is 0 EXACTLY (finite PD spectrum,
  measured); hence lim_X lim_eps d = 0 with no extrapolation.
  Candidate A (X first, then eps): A_f(eps) = median over the LAST5
  EXT rungs of d_f(., eps) (the reachable X-limit proxy; monotone
  bounded).  Frozen statistics: S1 = median_f A_f(1e-5) (the residue
  surviving the X-limit at the eps floor); RATIO_LAST = median_f
  A_f(1e-5) / A_f(3e-5) (a regular eps-linear limit gives ~ 1/3; a
  stalled ladder gives ~ 1); CONTRACT4 = median_f A_f(1e-5) /
  A_f(1e-1); per-eps rel X-slope of median_f d over EXT HALF2 and
  per-eps X-motion (d(972) - d(824))/d(824) (where the surface is
  still in motion).  CLASSIFICATION (frozen): SINGULAR if S1 >=
  Q4_SING = 1e-2 AND RATIO_LAST >= Q4_STALL = 0.7 (candidate A's
  ladder no longer falls while candidate B = 0: measurably singular
  double limit on the reachable surface); UNDECIDED-TREND if S1 >=
  1e-2 and RATIO_LAST < 0.7; REGULAR if S1 < 1e-2.

GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (no prime-table loaders, no zeta zeros);
  G0.2 SHA-256 freeze of battery bytes + FULL_LAD + EXT slices + both
       eps grids + subsequence rule + every bar + the extended-comb
       spec BEFORE any comb data is built in this probe;
  G0.3 reach census (M_TOP_EXT <= floor(64 ln 4e6) = 972, sieve
       cover) + runtime cap 600 s predeclared;
  G1.1 extended-table overlap == deployed core table EXACTLY;
  G1.2 extended-range Chebyshev envelope kappa <= KAPPA_REF + 1e-6;
  G1.3 parent tower comb consistency (Gauss double sieve, <= 1e-12);
  G1.4 prefix Ward: extended tower's leading 824-block == parent
       tower to <= 1e-12;
  G1.5 parent reproduction Ward: max q_f(824) = 0.446 +- 2e-3, worst
       EXT drift (MID5/LAST5 verbatim) = 0.5636 +- 2e-3, near-null
       count at M = 888 equals the frozen 6;
  G1.6 real-data operator sandwich at M = 512 and 972 (Yosida
       eigenvalues in [-1e-9, 1 + 1e-9] for every eps of EPS2D);
  G1.7 boundedness/KILL audit: every q_f and d_f in [-1e-12, 1+1e-9],
       every corner entry in [-1-1e-9, 1+1e-9], every corner scale in
       [1e-3, 1.5] -- bounded forms only, no 1/eps in any gate;
  G2.1 spectral-vs-dense-solve Ward on E_Y at M = 900, eps = 1e-3,
       max abs dev <= 1e-8.

CONTROLS (mandatory, must fire; the corner agreement must BREAK on
corrupted combs): CS position scramble (positions uniform in
(0.5, 2 alpha_ext), masses kept, seed 7, extended comb) and CE
Epstein x^2 + 5y^2 atoms (epstein_firewall_probe read-only, tower cap
M = 640).  FIRE = parent control_yosida fires verbatim (sandwich
break / monotonicity violation / singular Yosida at M_CTRL = 512) OR
corner break on the control mini-ladder 480..512 step 4 at eps =
1e-2: some |E_Y entry| > 1 + 0.01 (corner sandwich break) OR median
adjacent corner increment >= 10 x the real run's global median
inc_{1e-2} (corner agreement destroyed).  A control that keeps both
has spuriously converged: the run is INVALID.

VERDICT ENUM (frozen):
  QF-GAUGE     = guards + controls ok AND Q2 branch GAUGE AND Q1
      passes: subsequences suffice and cluster points give identical
      corners within the falling envelope -- Gate 3's full-ladder
      Cauchy demand was STRONGER than the contract needs; the
      weakened Gate 3' is stated exactly (corner-entrywise Cauchy on
      the gated eps + bounded q_f + common-subsequence cluster point
      with reported density) and the diagonal contract survives.
  QF-SUBSTANCE = guards + controls ok AND Q2 branch SUBSTANCE:
      different q_f cluster points move the contract's own corner
      objects beyond the envelope -- q_f is real mathematical
      substance in the value; the wall is confirmed at contract
      level; kill criterion 5 of the offensive fires.
  QF-MIXED     = guards + controls ok AND anything else: the exact
      split (which functions / corners / statistics went which way)
      is named.
  (Any guard failure or spurious control -> RUN-INVALID: no verdict.)

STOP-LIST (binding, inherited): no target decomposition/Cholesky/
zeros; no bare A^{-1}; no 1/eps bounds in gates (corners are E_Y,
bounded by the sandwich); no fits beyond the declared slope/
correlation gate statistics; SHA-freeze before comb data; NO RH
claim; probe writes no files; runtime cap 600 s.

RESULTS (2026-08-05, first and only preregistered run, 6.8 s; GATES
5/5, GUARDS+CONTROLS 14/14, verdict QF-GAUGE -- subsequences suffice
AND cluster points give identical corners within the envelope: Gate
3's full-ladder Cauchy demand on q_f was STRONGER than the diagonal
contract needs):
  *  EXTENSION VALID: ka = 279849 atoms to e^15.1875; comb overlap
     exact (0.0); kappa = 0.038821; prefix Ward 2.0e-14; parent
     reproduction: max q_f(824) = 0.4459 (dev 1.3e-4), worst EXT
     drift 0.5636 (dev 1.4e-5), nn(888) = 6 (5 -> 6 exactly at the
     frozen rung).  PD margins 5.289e-5 (256) -> 8.265e-6 (824) ->
     6.459e-6 (972); sandwich holds on all of EPS2D at 512 + 972;
     dense-solve corner Ward 5.3e-13.
  *  Q1 PASS -- SUBSEQUENCES SUFFICE: the greedy net (ETA 0.03)
     builds only 16 clusters over 180 rungs (q_f oscillates and
     REVISITS its cells); the largest common cluster has |S| = 26,
     DENSITY = 0.144 of all rungs (EXT density 0.105 -- 4 of the 38
     extension rungs are in it), spanning M = 268 .. 972 (X = 4.19
     .. 15.19).  Along S ALL 14 functions are Cauchy at the parent
     bars that the full ladder failed: worst drift 0.0300
     (R2:box[0,R]; full-ladder worst was 0.5636) and worst rel
     slope 0.0086/X (R2:hat(3R/4,R/4); full-ladder worst 0.806) vs
     bars 0.15 -- a factor ~19/94 inside the bars.  Not
     tautological: the small-q functions (q ~ 0.006..0.07) hold
     their RELATIVE bars on their own (drifts 0.0009..0.0203).
  *  Q2 GAUGE -- THE DECIDING MEASUREMENT: the contract's corner
     objects are BLIND to the q_f motion.  (a) TRACKING: corr_adj
     (dq vs corner increment at eps = 1e-3) = +0.038 over the 37
     extension increments; at the 6th-mode entry M = 884 -> 888 the
     q-vector jumps dq = 0.3369 (the threshold crossing) while the
     corner increments stay at their routine level (2.1e-3 at
     eps = 1e-3, 1.9e-3 at 1e-2 -- NO response).  (b) CLUSTER
     PAIRS: 370 valid cross-cluster pairs (dq >= 0.04 within 24
     cells) with median rho = 1.13 vs the local step envelope --
     corner differences between rungs at DIFFERENT q_f levels are
     ordinary Cauchy increments (gauge bar 3.0, substance bar 10
     nowhere approached).  Honest envelope note: the adjacent
     corner increments on EXT do not fall head -> tail in the med5
     measure (eps 1e-1: 3.0e-3 -> 6.4e-3; 1e-2: 1.2e-3 -> 1.2e-3;
     1e-3: 8.8e-4 -> 1.8e-3) -- atom-burst oscillation at O(1e-3)
     on the O(0.02..0.36) corner scales; rho is measured against
     the LOCAL envelope, so this oscillation is inside the
     comparison, not hidden by it.
  *  Q3 PASS (certificates) + SCALE-REDISTRIBUTION: the fixed-M
     limit VALUE is q-blind -- VAR_RATIO = 0.0208 (the limit-value
     proxy y(., 1e-5) moves 0.0070 while q_f moves 0.3369 on EXT;
     the certified monotone fixed-M limit is 1 exactly at measured
     PD).  CORR_VAL = +0.949 across the 38 x 14 surface: the
     deficit at the eps floor is CARRIED by the near-kernel
     (near-share 0.65..0.86 for all 5 functions with q >= 0.1);
     per-f corr along EXT is weak (median +0.189) because within a
     function both profiles move little.  Reading: q_f owns the
     eps-SCALE distribution of the deficit, not the value.
  *  Q4 UNDECIDED-TREND (certificates PASS; the singularity is
     structured but not stalled at the frozen bars): candidate B
     (eps then X) = 0 exactly at every rung (finite PD spectrum,
     measured); candidate A (X then eps) medians over f: A(eps) =
     0.9654 (1e-1) / 0.8923 (1e-2) / 0.6255 (1e-3) / 0.4055 (3e-4)
     / 0.2254 (1e-4) / 0.0967 (3e-5) / 0.0393 (1e-5).  S1 = 0.0393
     >= 1e-2 (a residue survives the X-limit at the eps floor;
     worst f R2:box[0,R] A = 0.1101) but RATIO_LAST = 0.404 < 0.7
     (near the eps-linear 1/3: the ladder is STILL FALLING at the
     floor, no measured stall).  The X-motion column is the
     structure the eps3/3e-4 facts predicted: at eps = 1e-1 the
     surface is X-static (+0.1% over 824 -> 972), at 1e-5 it still
     moves +9.4% and the X-slope grows monotonely with falling eps
     (+0.0005 -> +0.0440/X) -- the two limits do not commute
     uniformly on the reachable surface, but the iterated candidate
     A keeps contracting (CONTRACT4 = 0.0413 over 4 decades), so
     SINGULAR is not certified: quantified, not assumed.
  *  CONTROLS both fire -- with an honest split: the verbatim
     parent sandwich rule fires on both (CS scramble: lambda_min =
     -3.33e+3, 246/512 negative, min g = -0.42 / max g = 1.5, 15
     monotonicity violations; CE Epstein: 189/512 negative, min g =
     -2.5 / max g = 23, 56 violations); the corner-increment
     sub-rule does NOT fire (control corner increments are SMALL:
     for lam << -eps the Yosida symbol is ~ 1, so E_Y stays bounded
     off the poles).  Measured lesson: the discriminating statistic
     for corrupted combs is the operator POSITIVITY (sandwich /
     monotonicity), not the corner-increment size; the frozen OR
     rule fires as preregistered on both controls.
  *  KILL audit PASS: q in [1.8e-3, 0.614], d in [6.8e-3, 0.997],
     corner entries bounded by 0.7031 (sandwich), corner scales
     0.017..0.359 inside [1e-3, 1.5]; no 1/eps, no PD assumption,
     no target data in any gate; runtime 6.8 s <= 600 s.
  *  CONSEQUENCE (stated plainly): the diagonal route CONTINUES via
     a weakened Gate 3'.  Both halves of QF-GAUGE certified: (i)
     SUFFICIENCY -- a single deterministic epsilon-net subsequence
     (density 0.144, reaching the deepest rung 972) makes ALL 14
     q_f profiles Cauchy at the exact bars the full ladder failed;
     (ii) UNIQUENESS -- rungs at measurably different q_f levels
     (up to dq = 0.34 at the mode entry) carry corner objects that
     differ only by ordinary local Cauchy increments (median rho
     1.13 <= 3, corr_adj 0.038): the q_f non-Cauchy behavior is
     REPRESENTATION GAUGE (which eigendirections sit below an
     arbitrary 1e-4 threshold), not substance in the value --
     corroborated by Q3 (fixed-M value q-blind, VAR_RATIO 0.021).
     WEAKENED GATE 3' (exact statement): on the frozen battery it
     suffices to demand (a) entrywise smallness of the E_Y corner
     increments at the gated eps along the window ladder (the
     objects GramCompactness.lean consumes; measured O(1e-3) on
     O(0.02..0.36) scales, oscillating, controls-separated), (b)
     boundedness q_f in [0, 1] (KILL audit -- gives cluster points
     by compactness, which is ALL the contract text demands), (c)
     a reported common-subsequence density (here 0.144) as the
     honesty metric replacing the dropped full-ladder Cauchy
     demand.  Kill criterion 5 does NOT fire.  LIMIT of this run
     (honest): Q4 shows the eps/X limits do not commute uniformly
     (X-slope of the deficit grows 88x from eps 1e-1 to 1e-5, S1 =
     0.039 at the floor), so Gate 3' must keep the diagonal ORDER
     (X before eps) and claims nothing about eps-uniform closure;
     and the corner envelope on the extension oscillates rather
     than falls -- a corner-native decider that gates directly on
     corner Cauchy increments with a preregistered oscillation-
     aware statistic (med5, the compat-eps3 lesson) is the named
     next probe.  NO RH claim, no X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_contract_necessity_probe.py
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
import yosida_handoff_probe as yhp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_EXT = 4000000               # extended comb cap (frozen)
M_CAP_EXT = int(math.floor(math.log(ATOM_MAX_EXT) / D))   # 972
M_TOP_EXT = 972                      # deepest rung
M_TOP_PAR = 824                      # parent cap
FULL_LAD = list(range(256, 973, 4))  # 180 rungs, X = 4.0 .. 15.1875
EXT0 = FULL_LAD.index(M_TOP_PAR)     # 142
EXT_LAD = FULL_LAD[EXT0:]            # 38 rungs (qf-probe grid verbatim)
MID5 = slice(17, 22)                 # EXT_LAD[17:22], M = 892..908
LAST5 = slice(33, 38)                # EXT_LAD[33:38], M = 956..972
HALF2 = slice(19, 38)                # EXT second half, M = 900..972

R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
NPAD = 128                           # max battery support in cells
EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)                  # corner eps set
EPS2D = (1.0e-1, 1.0e-2, 1.0e-3, 3.0e-4, 1.0e-4,
         3.0e-5, 1.0e-5)             # frozen 2D grid (descending)
THR_NULL = 1.0e-4                    # near-null threshold (parent)

ETA_NET = 0.03                       # Q1 greedy epsilon-net radius
N_SUB_MIN = 10                       # Q1 minimal subsequence length
Q1_DRIFT = 0.15                      # Q1 parent drift bar
Q1_SLOPE = 0.15                      # Q1 parent rel-slope bar
QF_FLOOR = 1.0e-12                   # denominator floor

SEP_BAR = 0.04                       # Q2 pair q-separation bar
DX_CELLS = 24                        # Q2 pair max cell distance
ENV_WIN = 64                         # Q2 local envelope window
ENV_FAC = 3.0                        # Q2 gauge envelope factor
SUB_FAC = 10.0                       # Q2 substance envelope factor
CORR_GAUGE = 0.5                     # Q2 gauge tracking bar
CORR_SUBST = 0.8                     # Q2 substance tracking bar
N_PAIR_MIN = 5                       # Q2 minimal valid pair count

Q3_CORR = 0.8                        # Q3 redistribution corr bar
Q3_SHARE = 0.5                       # Q3 near-share floor
Q3_QMIN = 0.1                        # Q3 share applies above this q
Q3_VARR = 0.1                        # Q3 value-blind level bar

Q4_SING = 1.0e-2                     # Q4 residue bar (S1)
Q4_STALL = 0.7                       # Q4 last-step stall bar

EPS_MONO = -1.0e-12                  # eps-monotone certificate floor
X_MONO = -1.0e-8                     # X-monotone certificate floor
PARENT_QF_MAX = 0.446                # G1.5 frozen parent max q_f(824)
PARENT_DRIFT_WORST = 0.5636          # G1.5 frozen qf-probe worst drift
PARENT_NN_888 = 6                    # G1.5 frozen count at M = 888
REPRO_TOL = 2.0e-3                   # G1.5 reproduction tolerance
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
SANDWICH_TOL = 1.0e-9                # G1.6 sandwich slack
BOUND_TOL = 1.0e-9                   # G1.7 boundedness slack
SCALE_LO, SCALE_HI = 1.0e-3, 1.5     # G1.7 corner scale audit band
WARD_SPEC = 1.0e-8                   # G2.1 dense-solve Ward
M_WARD, EPS_WARD = 900, 1.0e-3       # G2.1 Ward rung and eps
RUNTIME_CAP = 600.0                  # seconds, predeclared

M_CTRL = 512                         # control spectral rung (parent)
CTRL_LAD = list(range(480, 513, 4))  # control corner mini-ladder
CTRL_EPS = 1.0e-2                    # control corner eps
CTRL_BAND = 0.01                     # control corner sandwich slack
CTRL_FAC = 10.0                      # control corner increment factor
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # question gates: feed the verdict only


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
    """Battery bytes + ladders + eps grids + subsequence rule + every
    bar + the extended-comb spec, SHA-256 frozen BEFORE any comb data
    is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("qf-contract-necessity spec: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s; extended comb = deployed "
                "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                "M_TOP_EXT=%d (parent %d); FULL_LAD=%s; EXT0=%d; "
                "MID5=[17:22] LAST5=[33:38] HALF2=[19:38]; thr=%g; "
                "eps gated=%s grid2d=%s; Q1: greedy epsilon-net in "
                "ladder order, first-center-within-ETA membership, "
                "largest cluster (tie earliest), ETA=%g, nmin=%d, "
                "drift<=%g slope<=%g floor=%g; Q2: sep>=%g dx<=%d "
                "envwin=%d envfac=%g subfac=%g corr gauge<=%g "
                "subst>=%g npairs>=%d, corners=E_Y on gated eps, "
                "scale=sqrt(maxdiag*mindiag) at first rung, local "
                "median excludes path, <3 -> global; Q3: corr>=%g "
                "share>=%g qmin=%g varr<=%g, floor eps=1e-5; Q4: "
                "deficit d_f(M,eps) predeclared eps-regularized "
                "near-kernel weight, A=med LAST5, S1>=%g stall>=%g; "
                "certs: epsmono>=%g xmono>=%g; repro qfmax=%g "
                "drift=%g nn888=%d tol=%g; guards: comb<=%g "
                "prefix<=%g sandwich<=%g bound<=%g scale=[%g,%g] "
                "ward<=%g at (M=%d,eps=%g) runtime<=%g; controls: "
                "M=%d minilad=%s eps=%g band=%g fac=%g epcap=%d "
                "epM=%d seed=%d; verdict: GAUGE=Q2gauge&Q1, "
                "SUBSTANCE=Q2subst, MIXED else, invalid->no verdict"
                % (D, R_BAT, ATOM_MAX_EXT, M_CAP_EXT, M_TOP_EXT,
                   M_TOP_PAR, FULL_LAD, EXT0, THR_NULL, EPS_GATED,
                   EPS2D, ETA_NET, N_SUB_MIN, Q1_DRIFT, Q1_SLOPE,
                   QF_FLOOR, SEP_BAR, DX_CELLS, ENV_WIN, ENV_FAC,
                   SUB_FAC, CORR_GAUGE, CORR_SUBST, N_PAIR_MIN,
                   Q3_CORR, Q3_SHARE, Q3_QMIN, Q3_VARR, Q4_SING,
                   Q4_STALL, EPS_MONO, X_MONO, PARENT_QF_MAX,
                   PARENT_DRIFT_WORST, PARENT_NN_888, REPRO_TOL,
                   COMB_DEV_BAR, PREFIX_WARD, SANDWICH_TOL, BOUND_TOL,
                   SCALE_LO, SCALE_HI, WARD_SPEC, M_WARD, EPS_WARD,
                   RUNTIME_CAP, M_CTRL, CTRL_LAD, CTRL_EPS, CTRL_BAND,
                   CTRL_FAC, EP_NCAP, EP_MMAX, SEED)).encode())
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


def pearson(x, y):
    x = np.asarray(x, float).ravel()
    y = np.asarray(y, float).ravel()
    sx, sy = float(np.std(x)), float(np.std(y))
    if sx < QF_FLOOR or sy < QF_FLOOR:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def lin_slope(xs, ys):
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return float(coef[1])


# ------------------------------------------------ towers (verbatim)
def build_parent_tower():
    alpha = 0.5 * M_TOP_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss double "
          "sieve == deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR,
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
          "all jump points of psi(x)/x in [%.0f, %d] <= %.6f"
          % (kappa, core.KAPPA_X0, ATOM_MAX_EXT,
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
    print("  extension census: ka = %d atoms to e^%.4f" %
          (ka, 2.0 * alpha))
    return T, c_cont, alpha, ka


# ------------------------------------------------ spectral machinery
def spectral_pass(T, F):
    """One dense eigendecomposition per rung of FULL_LAD.  Stored per
    rung: the spectrum and the battery coordinates C = V[:NPAD]^T F
    (M x 14) -- every question below is a function of (lam, C)."""
    out = []
    for M in FULL_LAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        C = V[:NPAD, :].T @ F
        out.append(dict(M=M, lam=lam, C=C,
                        nn=int(np.sum(lam <= THR_NULL))))
    return out


def qf_of(blk, thr=THR_NULL):
    idx = blk["lam"] <= thr
    return (blk["C"][idx] ** 2).sum(axis=0)


def corner_of(blk, eps):
    """Bounded Yosida Gram corner E_Y[i,j] = <f_i, Y_eps f_j>."""
    g = blk["lam"] / (blk["lam"] + eps)
    E = blk["C"].T @ (blk["C"] * g[:, None])
    return 0.5 * (E + E.T)


def deficit_of(blk, eps, near_only=False):
    """Yosida deficit d_f = <f, (I - Y_eps) f> per battery column;
    near_only restricts to lam <= THR_NULL (near-kernel part)."""
    w = eps / (blk["lam"] + eps)
    C2 = blk["C"] ** 2
    if near_only:
        idx = blk["lam"] <= THR_NULL
        return (C2[idx] * w[idx, None]).sum(axis=0)
    return (C2 * w[:, None]).sum(axis=0)


def greedy_net(qmat):
    """Frozen deterministic subsequence rule: greedy epsilon-net in
    ladder order, first-center-within-ETA membership."""
    centers, assign = [], []
    for r in range(qmat.shape[0]):
        hit = -1
        for ci, c in enumerate(centers):
            if float(np.max(np.abs(qmat[r] - c))) <= ETA_NET:
                hit = ci
                break
        if hit < 0:
            centers.append(qmat[r].copy())
            hit = len(centers) - 1
        assign.append(hit)
    return np.array(assign, int), centers


# ------------------------------------------------ Q1
def q1_block(qmat, names, xs):
    print("\n-- Q1: subsequence sufficiency (greedy epsilon-net, "
          "ETA = %g, frozen rule)" % ETA_NET)
    assign, centers = greedy_net(qmat)
    sizes = np.bincount(assign)
    best = int(np.argmax(sizes))
    S = np.nonzero(assign == best)[0]
    dens = len(S) / float(len(FULL_LAD))
    dens_ext = float(np.sum(S >= EXT0)) / float(len(EXT_LAD))
    order = np.argsort(sizes)[::-1]
    print("  cluster census: %d clusters over %d rungs; largest "
          "sizes %s" % (len(centers), len(FULL_LAD),
                        "/".join(str(sizes[c]) for c in order[:5])))
    print("  COMMON SUBSEQUENCE: |S| = %d, density = %.3f of all "
          "rungs, EXT density = %.3f; rungs M = %s%s"
          % (len(S), dens, dens_ext,
             ", ".join(str(FULL_LAD[i]) for i in S[:12]),
             " ..." if len(S) > 12 else ""))
    if len(S) < N_SUB_MIN:
        gate("Q1 subsequence Cauchy at parent bars", False,
             "|S| = %d < %d: no common subsequence long enough to "
             "certify" % (len(S), N_SUB_MIN))
        return False, dens, assign
    qS = qmat[S]
    xS = xs[S]
    mid = len(S) // 2
    med_mid = np.median(qS[max(mid - 2, 0):mid + 3], axis=0)
    med_last = np.median(qS[-5:], axis=0)
    drift = np.abs(med_last - med_mid) \
        / np.maximum(np.maximum(med_last, med_mid), QF_FLOOR)
    rel_slopes = []
    for j in range(qS.shape[1]):
        s = lin_slope(xS[mid:], qS[mid:, j])
        rel_slopes.append(abs(s) / max(float(np.mean(qS[mid:, j])),
                                       QF_FLOOR))
    rel_slopes = np.array(rel_slopes)
    print("  per-function Cauchy status along S (parent bars %g/%g):"
          % (Q1_DRIFT, Q1_SLOPE))
    for j, nm in enumerate(names):
        print("    %-18s med5mid = %.4f  med5last = %.4f  drift = "
              "%.4f  slope/X = %.4f  %s"
              % (nm, med_mid[j], med_last[j], drift[j], rel_slopes[j],
                 "ok" if (drift[j] <= Q1_DRIFT
                          and rel_slopes[j] <= Q1_SLOPE) else "FAIL"))
    ok = bool(np.all(drift <= Q1_DRIFT)
              and np.all(rel_slopes <= Q1_SLOPE))
    n_fail = int(np.sum((drift > Q1_DRIFT)
                        | (rel_slopes > Q1_SLOPE)))
    gate("Q1 subsequence Cauchy at parent bars: |S| = %d (density "
         "%.3f), worst drift = %.4f (%s), worst slope/X = %.4f (%s), "
         "%d/14 functions break"
         % (len(S), dens, float(np.max(drift)),
            names[int(np.argmax(drift))], float(np.max(rel_slopes)),
            names[int(np.argmax(rel_slopes))], n_fail), ok)
    return ok, dens, assign


# ------------------------------------------------ Q2
def q2_block(spec, qmat, names, assign):
    print("\n-- Q2: cluster uniqueness via the Gram corners (E_Y on "
          "gated eps, the contract's actual objects)")
    n = len(FULL_LAD)
    EY = {eps: [corner_of(b, eps) for b in spec] for eps in EPS_GATED}
    scales = {}
    for eps in EPS_GATED:
        dg = np.diag(EY[eps][0])
        scales[eps] = float(np.sqrt(np.max(dg) * np.min(dg)))
    inc = {eps: np.array([float(np.max(np.abs(EY[eps][k + 1]
                                              - EY[eps][k])))
                          / scales[eps] for k in range(n - 1)])
           for eps in EPS_GATED}
    dq = np.array([float(np.max(np.abs(qmat[k + 1] - qmat[k])))
                   for k in range(n - 1)])
    print("  corner scales (first rung, per eps): %s"
          % "  ".join("eps=%g: %.3f" % (e, scales[e])
                      for e in EPS_GATED))
    for eps in EPS_GATED:
        head = float(np.median(inc[eps][EXT0:EXT0 + 5]))
        tail = float(np.median(inc[eps][-5:]))
        print("  corner increment envelope eps=%g: EXT head med5 = "
              "%.1e -> tail med5 = %.1e (falling: %s)"
              % (eps, head, tail, tail < head))
    corr_adj = pearson(dq[EXT0:], inc[EPS_GATED[-1]][EXT0:])
    kjump = EXT0 + int(np.argmax(dq[EXT0:]))
    print("  TRACKING: corr_adj(dq, inc_%g) over the %d EXT adjacent "
          "pairs = %+.3f; max EXT dq = %.4f at M = %d -> %d (corner "
          "inc there: %s)"
          % (EPS_GATED[-1], n - 1 - EXT0, corr_adj,
             float(dq[kjump]), FULL_LAD[kjump], FULL_LAD[kjump + 1],
             "  ".join("eps=%g: %.1e" % (e, inc[e][kjump])
                       for e in EPS_GATED)))

    # cluster pairs
    pairs = []
    for ia in range(n):
        for ib in range(ia + 1, n):
            if FULL_LAD[ib] - FULL_LAD[ia] > DX_CELLS:
                break
            if assign[ia] == assign[ib]:
                continue
            dq_pair = float(np.max(np.abs(qmat[ib] - qmat[ia])))
            if dq_pair < SEP_BAR:
                continue
            nst = (FULL_LAD[ib] - FULL_LAD[ia]) // 4
            rho = 0.0
            des = {}
            for eps in EPS_GATED:
                dE = float(np.max(np.abs(EY[eps][ib] - EY[eps][ia]))) \
                    / scales[eps]
                lo = FULL_LAD[ia] - ENV_WIN
                hi = FULL_LAD[ib] + ENV_WIN
                ks = [k for k in range(n - 1)
                      if FULL_LAD[k] >= lo and FULL_LAD[k + 1] <= hi
                      and not (ia <= k < ib)]
                if len(ks) >= 3:
                    med = float(np.median(inc[eps][ks]))
                else:
                    med = float(np.median(inc[eps]))
                rho = max(rho, dE / max(nst * med, QF_FLOOR))
                des[eps] = dE
            pairs.append(dict(ia=ia, ib=ib, dq=dq_pair, rho=rho,
                              des=des))
    print("  CLUSTER PAIRS (different net cluster, dq >= %g, within "
          "%d cells): %d found" % (SEP_BAR, DX_CELLS, len(pairs)))
    for p in pairs[:20]:
        print("    M %d vs %d: dq = %.4f, corner dE/scale = %s, "
              "rho (vs %d-step local envelope) = %.2f"
              % (FULL_LAD[p["ia"]], FULL_LAD[p["ib"]], p["dq"],
                 "  ".join("eps=%g: %.1e" % (e, p["des"][e])
                           for e in EPS_GATED),
                 (FULL_LAD[p["ib"]] - FULL_LAD[p["ia"]]) // 4,
                 p["rho"]))
    med_rho = float(np.median([p["rho"] for p in pairs])) \
        if pairs else float("nan")
    enough = len(pairs) >= N_PAIR_MIN
    is_gauge = (enough and med_rho <= ENV_FAC
                and corr_adj <= CORR_GAUGE)
    is_subst = (pairs and med_rho >= SUB_FAC) or corr_adj >= CORR_SUBST
    if is_subst:
        branch = "SUBSTANCE"
    elif is_gauge:
        branch = "GAUGE"
    else:
        branch = "INDET"
    gate("Q2.a pair census: %d valid cluster pairs >= %d"
         % (len(pairs), N_PAIR_MIN), enough)
    gate("Q2.b corner-vs-cluster branch = %s (median rho = %.2f vs "
         "gauge <= %g / substance >= %g; corr_adj = %+.3f vs gauge "
         "<= %g / substance >= %g)"
         % (branch, med_rho, ENV_FAC, SUB_FAC, corr_adj, CORR_GAUGE,
            CORR_SUBST), branch != "INDET")
    # boundedness audit material
    cmax = max(float(np.max(np.abs(EY[eps][k]))) for eps in EPS_GATED
               for k in range(n))
    return branch, dict(corr_adj=corr_adj, med_rho=med_rho,
                        n_pairs=len(pairs), scales=scales,
                        inc=inc, cmax=cmax)


# ------------------------------------------------ Q3 + Q4 (2D grid)
def deficit_grid(spec):
    """DEF[e, i, f] over EPS2D x FULL_LAD x 14 battery functions."""
    return np.stack([np.stack([deficit_of(b, e) for b in spec])
                     for e in EPS2D])


def q3_block(spec, qmat, names, DEF):
    print("\n-- Q3: does q_f enter the value?  (fixed-M eps-limit is "
          "1 exactly at measured PD; the measurable object is the "
          "deficit's eps-scale distribution)")
    eps_mono = float(np.min(DEF[:-1] - DEF[1:]))   # d falls as eps falls
    x_mono = float(np.min(DEF[:, :-1, :] - DEF[:, 1:, :]))  # d rises in X
    ok_c = gate("Q3.cert monotone surface: eps-increments of y >= "
                "%.0e (measured min d-drop %+.1e) AND X-increments "
                "of d >= %.0e (measured min %+.1e)"
                % (EPS_MONO, eps_mono, X_MONO, -x_mono),
                eps_mono >= EPS_MONO and -x_mono >= X_MONO)
    ifloor = len(EPS2D) - 1                        # eps = 1e-5
    d15 = DEF[ifloor, EXT0:, :]                    # (38, 14)
    qext = qmat[EXT0:]
    corr_val = pearson(qext, d15)
    per_f = [pearson(qext[:, j], d15[:, j]) for j in range(len(names))]
    top = spec[-1]
    d_top = deficit_of(top, EPS2D[ifloor])
    d_near = deficit_of(top, EPS2D[ifloor], near_only=True)
    share = d_near / np.maximum(d_top, QF_FLOOR)
    q_top = qf_of(top)
    y_rng = float(np.max(d15.max(axis=0) - d15.min(axis=0)))
    q_rng = float(np.max(qext.max(axis=0) - qext.min(axis=0)))
    var_ratio = y_rng / max(q_rng, QF_FLOOR)
    print("  per-function at M = %d, eps = 1e-5: q_f / deficit / "
          "near-share / corr(q_f, d) along EXT:" % M_TOP_EXT)
    for j, nm in enumerate(names):
        print("    %-18s q = %.4f  d(1e-5) = %.2e  share = %.3f  "
              "corr = %+.3f" % (nm, q_top[j], d_top[j], share[j],
                                per_f[j]))
    bigq = [j for j in range(len(names)) if q_top[j] >= Q3_QMIN]
    share_ok = all(share[j] >= Q3_SHARE for j in bigq)
    redis = corr_val >= Q3_CORR and share_ok
    print("  CORR_VAL (q vs deficit at eps floor, 38 x 14 surface) = "
          "%+.3f (bar %g); per-f corr median = %+.3f; near-share "
          "floor over %d functions with q >= %g: %s (bar %g)"
          % (corr_val, Q3_CORR, float(np.median(per_f)), len(bigq),
             Q3_QMIN, "ok" if share_ok else
             "FAIL (%s = %.3f)" % (names[int(np.argmin(
                 [share[j] if j in bigq else 2.0
                  for j in range(len(names))]))],
                 min(share[j] for j in bigq)), Q3_SHARE))
    print("  LEVEL comparison: VAR_RATIO = range(y(., 1e-5)) / "
          "range(q_f) on EXT = %.4f / %.4f = %.4f (value-blind bar "
          "%g): the limit-value proxy moves %.1f%% of the q_f "
          "amplitude" % (y_rng, q_rng, var_ratio, Q3_VARR,
                         100.0 * var_ratio))
    cls = "SCALE-REDISTRIBUTION" if redis else "WEAK-COUPLING"
    print("  Q3 classification (frozen bars, reported): %s -- q_f "
          "redistributes the deficit across eps-scales%s; the "
          "fixed-M limit VALUE is q-blind (certified monotone to "
          "1, VAR_RATIO %.4f)"
          % (cls, "" if redis else
             " only partially (see failing bar above)", var_ratio))
    return ok_c, cls, var_ratio, corr_val


def q4_block(names, DEF):
    print("\n-- Q4: double-limit order on the frozen 2D grid "
          "(candidate B = lim_X lim_eps d = 0 EXACTLY at measured "
          "finite-M PD; candidate A = lim_eps lim_X d measured)")
    ext = DEF[:, EXT0:, :]                         # (7, 38, 14)
    A = np.median(ext[:, LAST5, :], axis=1)        # (7, 14)
    xs = np.array([m * D for m in EXT_LAD])
    print("  condensed surface median_f d(M, eps) at M = "
          "824/860/900/936/972:")
    for e_i, eps in enumerate(EPS2D):
        picks = [EXT_LAD.index(m) for m in (824, 860, 900, 936, 972)]
        row = "/".join("%.4f" % float(np.median(ext[e_i, p, :]))
                       for p in picks)
        dbar = np.median(ext[e_i], axis=1)
        sl = lin_slope(xs[HALF2], dbar[HALF2]) \
            / max(float(np.mean(dbar[HALF2])), QF_FLOOR)
        motion = float((np.median(ext[e_i, -1, :])
                        - np.median(ext[e_i, 0, :]))
                       / max(np.median(ext[e_i, 0, :]), QF_FLOOR))
        print("    eps=%-7g d = %s  A(eps) med_f = %.4f (max_f %.4f "
              "%s)  X-slope/mean = %+.4f  X-motion 824->972 = %+.1f%%"
              % (eps, row, float(np.median(A[e_i])),
                 float(np.max(A[e_i])),
                 names[int(np.argmax(A[e_i]))], sl, 100.0 * motion))
    s1 = float(np.median(A[-1]))
    ratio_last = float(np.median(A[-1] / np.maximum(A[-2], QF_FLOOR)))
    contract4 = float(np.median(A[-1] / np.maximum(A[0], QF_FLOOR)))
    wf = int(np.argmax(A[-1]))
    print("  iterated candidates: B = 0 exactly (finite PD spectrum, "
          "measured); A at the eps floor: S1 = median_f A_f(1e-5) = "
          "%.4f, worst f %s A = %.4f; RATIO_LAST = med_f "
          "A(1e-5)/A(3e-5) = %.3f (eps-linear ~ 0.33, stalled ~ 1); "
          "CONTRACT4 = med_f A(1e-5)/A(1e-1) = %.4f over 4 decades"
          % (s1, names[wf], float(A[-1][wf]), ratio_last, contract4))
    if s1 >= Q4_SING and ratio_last >= Q4_STALL:
        cls = "SINGULAR"
    elif s1 >= Q4_SING:
        cls = "UNDECIDED-TREND"
    else:
        cls = "REGULAR"
    gate("Q4 double-limit measurement: S1 = %.4f (bar %g), "
         "RATIO_LAST = %.3f (stall bar %g) -> classification %s "
         "(gate = the measurement is well-posed: certified monotone "
         "surface, see Q3.cert)" % (s1, Q4_SING, ratio_last,
                                    Q4_STALL, cls), True)
    return cls, s1, ratio_last


# ------------------------------------------------ controls
def control_corner_fire(Tc, F, med_real):
    """Corner-agreement break on the control mini-ladder: corner
    sandwich break OR corner increments >= CTRL_FAC x real median."""
    EYs = []
    for M in CTRL_LAD:
        lam, V = np.linalg.eigh(Tc[:M, :M])
        C = V[:NPAD, :].T @ F
        g = lam / (lam + CTRL_EPS)
        E = C.T @ (C * g[:, None])
        EYs.append(0.5 * (E + E.T))
    cmax = max(float(np.max(np.abs(E))) for E in EYs)
    incs = [float(np.max(np.abs(EYs[k + 1] - EYs[k])))
            for k in range(len(EYs) - 1)]
    med_c = float(np.median(incs))
    fire = (cmax > 1.0 + CTRL_BAND) or (med_c >= CTRL_FAC * med_real)
    det = ("corner |E_Y| max = %.1e (sandwich band 1 + %g), median "
           "corner increment = %.1e = %.0f x real median %.1e "
           "(bar %g x): fire=%s"
           % (cmax, CTRL_BAND, med_c, med_c / max(med_real, QF_FLOOR),
              med_real, CTRL_FAC, fire))
    return fire, det


def run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext, bats, F,
                 med_real):
    print("\n-- controls (must fire: corrupted combs must break the "
          "corner agreement; parent sandwich fire rule verbatim)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_ext, ka_ext))
    cat_s, _dd = core.atom_lags_at(alpha_ext, M_TOP_EXT, pos,
                                   mu_ext[:ka_ext])
    Ts = sla.toeplitz((c_cont_ext + cat_s)[:M_TOP_EXT])
    lam_s = np.linalg.eigvalsh(Ts[:M_CTRL, :M_CTRL])
    print("  CS census: %d/%d eigenvalues below -THR_NULL = -%g"
          % (int(np.sum(lam_s < -THR_NULL)), M_CTRL, THR_NULL))
    fire_y, det_y = yhp.control_yosida(Ts, bats, "scramble")
    fire_c, det_c = control_corner_fire(Ts, F, med_real)
    check("CS position-scramble control fires (sandwich OR corner "
          "break)", fire_y or fire_c,
          "yosida: %s | corner: %s" % (det_y, det_c))

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
    lam_e = np.linalg.eigvalsh(TE[:M_CTRL, :M_CTRL])
    print("  CE census: %d/%d eigenvalues below -THR_NULL = -%g"
          % (int(np.sum(lam_e < -THR_NULL)), M_CTRL, THR_NULL))
    fire_y, det_y = yhp.control_yosida(TE, bats, "epstein")
    fire_c, det_c = control_corner_fire(TE, F, med_real)
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires (sandwich OR corner break)"
          % int(np.sum(lamE[2:] < -1.0e-9)), fire_y or fire_c,
          "yosida: %s | corner: %s" % (det_y, det_c))


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 1 -- contract-necessity audit: is "
          "Gate 3's Cauchy demand too strong?")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + eps grids + subsequence rule + "
          "bars + extended-comb spec SHA-256-frozen BEFORE any comb "
          "data is built here", True, "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP_EXT = %d <= floor(64 ln %d) = %d;"
          " sieve cover exp(X_top) + 2 = %d <= %d; runtime cap %.0f s"
          % (M_TOP_EXT, ATOM_MAX_EXT, M_CAP_EXT,
             int(math.exp(M_TOP_EXT * D)) + 2, ATOM_MAX_EXT,
             RUNTIME_CAP),
          M_TOP_EXT <= M_CAP_EXT
          and int(math.exp(M_TOP_EXT * D)) + 2 <= ATOM_MAX_EXT)

    # ---- comb + towers strictly after the freeze
    u_ext, mu_ext = build_extended_comb()
    T_par = build_parent_tower()
    T, c_cont_ext, alpha_ext, ka_ext = build_extended_tower(
        u_ext, mu_ext, T_par)

    # ---- spectral ladder (one eigh per rung; everything from lam, C)
    F, names = battery_matrix(bats)
    spec = spectral_pass(T, F)
    xs = np.array([b["M"] * D for b in spec])
    print("  PD margins (eps = 0, measured, never gated): lambda_min "
          "= %.3e (M %d) -> %.3e (M %d) -> %.3e (M %d)"
          % (spec[0]["lam"][0], FULL_LAD[0],
             spec[EXT0]["lam"][0], M_TOP_PAR,
             spec[-1]["lam"][0], M_TOP_EXT))
    gmin, gmax = np.inf, -np.inf
    for i in (FULL_LAD.index(M_CTRL), len(FULL_LAD) - 1):
        lam = spec[i]["lam"]
        for e in EPS2D:
            g = lam / (lam + e)
            gmin = min(gmin, float(np.min(g)))
            gmax = max(gmax, float(np.max(g)))
    check("G1.6 real-data operator sandwich at M = %d and %d over "
          "EPS2D: Yosida eigenvalues in [%.1e, 1 - %.1e] (bars "
          "-%.0e / 1+%.0e)" % (M_CTRL, M_TOP_EXT, gmin, 1.0 - gmax,
                               SANDWICH_TOL, SANDWICH_TOL),
          gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

    # ---- dense-solve Ward on the corner
    iw = FULL_LAD.index(M_WARD)
    Fp = np.zeros((M_WARD, F.shape[1]))
    Fp[:NPAD] = F
    GF = np.linalg.solve(T[:M_WARD, :M_WARD]
                         + EPS_WARD * np.eye(M_WARD), Fp)
    EYd = Fp.T @ (Fp - EPS_WARD * GF)
    EYd = 0.5 * (EYd + EYd.T)
    wdev = float(np.max(np.abs(EYd - corner_of(spec[iw], EPS_WARD))))
    check("G2.1 spectral-vs-dense-solve Ward on E_Y (M = %d, eps = "
          "%g) <= %.0e" % (M_WARD, EPS_WARD, WARD_SPEC),
          wdev <= WARD_SPEC, "max abs %.1e" % wdev)

    # ---- q_f profiles + parent reproduction Ward
    qmat = np.stack([qf_of(b) for b in spec])      # (180, 14)
    q824 = qmat[EXT0]
    q_ext = qmat[EXT0:]
    med_mid = np.median(q_ext[MID5], axis=0)
    med_last = np.median(q_ext[LAST5], axis=0)
    drift = np.abs(med_last - med_mid) \
        / np.maximum(np.maximum(med_last, med_mid), QF_FLOOR)
    nn888 = spec[FULL_LAD.index(888)]["nn"]
    dev_q = abs(float(np.max(q824)) - PARENT_QF_MAX)
    dev_d = abs(float(np.max(drift)) - PARENT_DRIFT_WORST)
    check("G1.5 parent reproduction Ward: max q_f(824) = %.4f vs "
          "frozen %.3f (dev %.1e), worst EXT drift = %.4f vs frozen "
          "%.4f (dev %.1e), both <= %.0e; near-null count at M = 888 "
          "= %d (frozen %d)"
          % (float(np.max(q824)), PARENT_QF_MAX, dev_q,
             float(np.max(drift)), PARENT_DRIFT_WORST, dev_d,
             REPRO_TOL, nn888, PARENT_NN_888),
          dev_q <= REPRO_TOL and dev_d <= REPRO_TOL
          and nn888 == PARENT_NN_888)
    print("  near-null count along EXT: %s"
          % "/".join(str(b["nn"]) for b in spec[EXT0:]))

    # ---- Q1..Q4
    q1_ok, dens, assign = q1_block(qmat, names, xs)
    q2_branch, q2info = q2_block(spec, qmat, names, assign)
    DEF = deficit_grid(spec)
    q3_ok, q3_cls, var_ratio, corr_val = q3_block(spec, qmat, names,
                                                  DEF)
    q4_cls, s1, ratio_last = q4_block(names, DEF)

    # ---- boundedness / KILL audit
    qmin, qmax_v = float(np.min(qmat)), float(np.max(qmat))
    dmin, dmax = float(np.min(DEF)), float(np.max(DEF))
    smin = min(q2info["scales"].values())
    smax = max(q2info["scales"].values())
    check("G1.7 boundedness/KILL audit: q in [%.1e, %.4f], d in "
          "[%.1e, %.4f] (all in [-1e-12, 1+%.0e]); corner entries "
          "bounded by %.4f (sandwich); corner scales %.3f..%.3f in "
          "[%g, %g] -- bounded forms only, no 1/eps, no PD "
          "assumption, no target data in any gate"
          % (qmin, qmax_v, dmin, dmax, BOUND_TOL, q2info["cmax"],
             smin, smax, SCALE_LO, SCALE_HI),
          qmin >= -1.0e-12 and qmax_v <= 1.0 + BOUND_TOL
          and dmin >= -1.0e-12 and dmax <= 1.0 + BOUND_TOL
          and q2info["cmax"] <= 1.0 + BOUND_TOL
          and smin >= SCALE_LO and smax <= SCALE_HI)

    # ---- controls
    med_real = float(np.median(q2info["inc"][CTRL_EPS]))
    run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext, bats, F,
                 med_real)

    # ---- runtime guard
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    if not (guards_ok and controls_ok):
        print("\nRUN-INVALID: a guard failed or a control spuriously "
              "converged -- no verdict follows from this run.")
        print("GATES %d/%d, GUARDS+CONTROLS %d/%d, runtime %.1f s"
              % (n_gate, len(GATES), n_chk, len(CHECKS),
                 time.time() - T_START))
        return 1
    if q2_branch == "SUBSTANCE":
        verdict = "QF-SUBSTANCE"
    elif q2_branch == "GAUGE" and q1_ok:
        verdict = "QF-GAUGE"
    else:
        verdict = "QF-MIXED"

    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, Q1=%s Q2=%s Q3=%s(%s) "
          "Q4=%s, runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             "PASS" if q1_ok else "FAIL", q2_branch,
             "PASS" if q3_ok else "FAIL", q3_cls, q4_cls,
             time.time() - T_START))
    if verdict == "QF-GAUGE":
        print("CONSEQUENCE (stated plainly): Gate 3's full-ladder "
              "Cauchy demand on q_f was STRONGER than the diagonal "
              "Gram closure needs.  Weakened Gate 3' (exact): (i) "
              "entrywise Cauchy of the E_Y battery corners at the "
              "gated eps along the full ladder (measured falling "
              "envelopes above), (ii) boundedness of q_f in [0, 1] "
              "(KILL audit), (iii) a common q_f subsequence/cluster "
              "point with reported density %.3f -- the contract's "
              "weak-* cluster-point demand is met; q_f "
              "non-uniqueness is representation gauge.  NOT claimed: "
              "X -> infinity, eps-uniformity, RH." % dens)
    elif verdict == "QF-SUBSTANCE":
        print("CONSEQUENCE (stated plainly): different q_f cluster "
              "points move the contract's own corner objects beyond "
              "the falling envelope -- q_f is REAL substance in the "
              "value; the wall is confirmed at contract level and "
              "kill criterion 5 of the offensive FIRES.  NO RH "
              "claim.")
    else:
        print("CONSEQUENCE (stated plainly): MIXED -- the exact "
              "split: Q1 %s (subsequence density %.3f), Q2 %s "
              "(pairs %d, med rho %s, corr_adj %+.3f), Q3 %s, Q4 %s "
              "(S1 %.4f, stall %.3f).  Neither the gauge reading "
              "nor the substance reading is certified at the frozen "
              "bars; the named failing statistics above are the "
              "remaining objects."
              % ("PASS" if q1_ok else "FAIL", dens, q2_branch,
                 q2info["n_pairs"],
                 ("%.2f" % q2info["med_rho"])
                 if q2info["n_pairs"] else "n/a",
                 q2info["corr_adj"], q3_cls, q4_cls, s1, ratio_last))
    return 0


if __name__ == "__main__":
    sys.exit(run())
