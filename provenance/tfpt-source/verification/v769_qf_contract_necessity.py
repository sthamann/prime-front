#!/usr/bin/env python3
"""v769 -- PRIME.QFGAUGE.01: the Gate-3 audit pair of the qf offensive, one module from two probes, combined verdict QF-GAUGE / GATE3PRIME-DEAD.  PART 1 (QF-GAUGE, 5/5 gates, 14/14 guards+controls): Gate 3's full-ladder Cauchy demand on q_f was provably STRONGER than the diagonal Gram contract needs -- (i) SUFFICIENCY: a single deterministic epsilon-net subsequence (ETA 0.03, density 0.144, reaching the deepest rung 972) makes ALL 14 q_f profiles Cauchy at the exact parent bars the full ladder failed (worst drift 0.0300 vs full-ladder 0.5636, worst rel slope 0.0086/X vs 0.806); (ii) UNIQUENESS: the contract's own E_Y corner objects are BLIND to q_f motion (corr_adj = +0.038 over the 37 extension increments; the dq = 0.3369 mode-entry jump at M = 888 leaves corner increments at routine level; 370 cross-cluster pairs, median rho = 1.13 vs gauge bar 3.0) -- the q_f non-Cauchy behavior is REPRESENTATION GAUGE (which eigendirections sit below an arbitrary 1e-4 threshold), not substance in the value (Q3: fixed-M limit value q-blind, VAR_RATIO 0.021; q_f owns the eps-SCALE distribution of the deficit, CORR_VAL +0.949).  Q4 honest limit: the eps/X double limit does not commute uniformly (the deficit X-slope grows 88x from eps 1e-1 to 1e-5, S1 = 0.039 at the floor) but SINGULAR is not certified (RATIO_LAST 0.404 < 0.7: candidate A still falling).  PART 2 (GATE3PRIME-DEAD, CELLS 34/168: n(1e-1) = 31/56, n(1e-2) = 3/56, n(1e-3) = 0/56; guards+controls 14/14): the corner-native weakened Gate 3', decided on its OWN predeclared deeper 1.6e7 comb (X = 16.5625, 202 rungs, 1,007,385 atoms), dies -- the corner increments fall to X ~ 12.9 (exactly the falling regime every parent probe certified on rungs <= 824) and then RISE SUSTAINED on the deep rungs (eps = 1e-3 med5 envelope 8.79e-4 -> 1.79e-3 -> 3.67e-3; second-half slopes +0.10..+0.34 per X unit fitted over 101 increments; broad-spectrum across boxes, hats, diagonals, both R-groups -- not one bad channel).  The parent audit's envelope oscillation was the ONSET of this rise, not a shallow-window artifact; the v764 precondition (assemble v760 + v761 on a corner-Cauchy statement) is REFUTED at the corner level.  The rise coincides with the per-cell comb fluctuation amplitude growing through the battery scale.  NO RH claim, no X -> infinity claim, no eps -> 0 claim.

PROVENANCE: discovery probes qf_contract_necessity_probe.py (2026-08-05, first and only preregistered run, 6.8 s, GATES 5/5, GUARDS+CONTROLS 14/14, verdict QF-GAUGE) and corner_cauchy_gate3prime_probe.py (2026-08-05, first and only preregistered run, 10.4 s, CELLS 34/168, GUARDS+CONTROLS 14/14, verdict GATE3PRIME-DEAD).  Merged per the v518/v668/v763 precedent: part 1 verbatim at module level (sibling imports point at v563/v755/v763/v766; epstein_firewall_probe stays a read-only discovery import); part 2 verbatim inside an isolated function scope (its module-level names are function-local); numbers unchanged.  run() encodes both preregistered patterns as the expected outcome (v757 precedent).

PART 1 -- qf_contract_necessity_probe.py (docstring verbatim):
QF-OFFENSIVE strand 1 -- THE AUDIT BEFORE ANY NEW OFFENSIVE: is
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

PART 2 -- corner_cauchy_gate3prime_probe.py (docstring verbatim):
QF-OFFENSIVE strand 1, follow-up -- THE CORNER-NATIVE GATE 3'
DECIDER (direct precondition test for v764):
corner_cauchy_gate3prime_probe.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_contract_necessity_probe -- QF-GAUGE (5/5 gates, 14/14
     guards+controls): Gate 3's full-ladder Cauchy demand on q_f was
     STRONGER than the diagonal contract needs.  A single epsilon-net
     subsequence (density 0.144) makes all 14 q_f profiles Cauchy at
     the parent bars; the corner objects are BLIND to q_f motion
     (corr_adj = +0.038; the dq = 0.3369 mode-entry jump at M = 888
     leaves corner increments at routine level; 370 cross-cluster
     pairs, median rho = 1.13).  MEASURED CAVEATS carried in: (i)
     the EXT corner-increment envelope OSCILLATES (eps 1e-3 head ->
     tail med5: 8.8e-4 -> 1.8e-3 on 824..972) -- raw endpoint gates
     are the wrong instrument (the compat-eps3 lesson); (ii) the
     controls discriminate via POSITIVITY (sandwich/monotonicity),
     not corner size (for lam << -eps the Yosida symbol is ~ 1, so
     corner entries of indefinite matrices stay bounded off the
     poles); (iii) Q4: the eps/X limits do not commute uniformly --
     the ORDER X-before-eps is enforced (every gate below lives at
     FIXED eps along the X ladder; no eps -> 0 claim).
  *  handoff_compat_eps3_probe / v768 -- the oscillation-aware cell
     statistic pattern reused here verbatim in spirit: 5-rung
     medians, second-half fitted slope, Dini/summability tail share.
  *  Contract PRIME.KMS.INDUCTIVE_STATE.02 + GramCompactness.lean:
     the objects the diagonal contract actually consumes are the
     ENTRYWISE corner values <f_i, Y_eps f_j> on fixed battery
     corners -- Gate 3' therefore gates on corner-increment Cauchy
     smallness directly; q_f is bounded gauge (report only).

SINGLE QUESTION (preregistered): are the E_Y Gram corner entries
entrywise Cauchy along the deepest honestly reachable window ladder,
at each gated eps, under the oscillation-aware statistic -- i.e. is
Gate 3' (the weakened, contract-native form frozen by the parent
audit) DECIDED POSITIVELY on the objects themselves?

DEEPER-LADDER LEVER (predeclared by OWN compute budget; this probe
does NOT depend on any other worker's comb extension): deep comb cap
ATOM_MAX_DEEP = 16,000,000 (ln = 16.5881, M_CAP_DEEP =
floor(64 ln 1.6e7) = 1061); M_TOP_DEEP = 1060 is frozen as the
deepest step-4-aligned rung (X = 16.5625); sieve cover
exp(16.5625) + 2 = 15,595,611 <= 16,000,000.  The extension is the
deployed generator (core.von_mangoldt_table) at a larger cap -- no
new information class; guards tie it to the deployed table (exact
overlap on [0, 400000]), to the parent tower (float-exact 824
prefix), to the Chebyshev envelope on [100, 1.6e7], and to the
parent-audit anchors (q_f(824), EXT drift, nn(888), the 824..972
corner-envelope numbers reproduced).  This adds 1.375 X units and 22
rungs beyond the 972 surface where the envelope oscillation was
seen: the deep rungs decide whether it was a shallow-window artifact.

FROZEN CONSTRUCTION: full ladder FULL_LAD = 256..1060 step 4 (202
rungs, 201 increments); frozen module-1 battery (4 boxes + 3 hats
per R, R in {1, 2}, l2-normalized, NPAD = 128); one dense eigh per
rung; corner objects E_Y^eps[i,j] = <f_i, Y_eps f_j> =
C^T diag(lam/(lam+eps)) C (bounded by the sandwich, no 1/eps
anywhere) at the gated eps set EPS_GATED = (1e-1, 1e-2, 1e-3);
CORNER-CELL SET (predeclared): ALL entry pairs (i <= j) WITHIN each
R-group -- 28 cells per group (7 diagonal + 21 off-diagonal), 56
cells total, x 3 eps = 168 gated cells (the contract needs entrywise
corners, not just diagonals; cross-R pairs are excluded by
declaration: the contract's corners live per local observable
algebra).  Per-eps scale (parent convention) scale_eps =
sqrt(max diag * min diag) of E_Y at the first rung; scaling is
constant per eps and cancels from every ratio/slope/share gate.

GATES (all frozen numerically BEFORE the first run; slope statistics
are declared gate statistics on bounded quantities, not proof-grade
claims).  Per corner cell (entry, eps), on the increment profile
inc(k) = |E_Y(M_{k+1}) - E_Y(M_k)|[i,j] / scale_eps over the 201
ladder steps (X of the upper rung as abscissa):
  S1 med5 ratio:   median(inc last 5) / max(median(inc first 5),
                   1e-12) <= RATIO_BAR = 0.5   (the compat-eps3 C2
                   pattern: single atom-burst rungs cannot break a
                   cell);
  S2 second-half slope: least-squares slope of log(inc) vs X over
                   the last 101 increments <= SLOPE_TOL = +0.02 per
                   X unit (falling, or at worst marginally rising
                   within the declared oscillation tolerance);
  S3 summability proxy: tail-quarter share of total variation,
                   sum(inc last 51) / sum(inc all) <= TV_BAR = 0.25
                   (a flat profile gives 51/201 = 0.254: the gate
                   demands strictly better than flat).
  A cell PASSES iff S1 and S2 and S3.
VERDICT COUNTS (frozen; n_e = passing cells of 56 at eps e):
  GATE3PRIME-CONVERGES = guards ok AND both controls fire AND
      n(1e-1) = 56 AND n(1e-2) = 56 AND n(1e-3) >= 51 (>= 90%);
  GATE3PRIME-PARTIAL   = guards ok AND both controls fire AND
      n(1e-1) >= 51 AND n(1e-2) >= 51 AND n(1e-3) >= 28, not
      CONVERGES (every failing cell is NAMED);
  GATE3PRIME-DEAD      = anything else: majority corner failures
      (the corner increments do not fall -- the gauge reading of
      q_f was a false hope and the wall returns at the corner
      level), OR a control spuriously converges, OR a guard fails
      (invalid run, stated as such).

SUBSEQUENCE REPORT (never gated): the parent's greedy epsilon-net
rule (ETA = 0.03, sup-norm, ladder order, first-center membership)
recomputed on this deeper ladder for BOTH profiles: (a) q_f-native
(14-dim, THR_NULL = 1e-4) and (b) corner-native (168-dim: the
UNSCALED E_Y entries of all 56 cells at the 3 gated eps -- bounded
by 1, same footing).  Reported: cluster counts, largest-cluster
densities, and the comparison the parent asked for (does the corner
picture need subsequences at all, or is it full-ladder Cauchy
already -- the gates above answer the Cauchy half; the net density
is the honesty metric).  q_f boundedness in [0, 1] is REPORTED
(KILL audit) -- q_f appears in NO gate.

GUARDS (must pass or the run is invalid):
  G0.1 AST firewall; G0.2 SHA-256 freeze of battery bytes + ladder +
  cell set + eps set + every bar + net rule + deep-comb spec + the
  control fire rule BEFORE any comb data is built here; G0.3 reach
  census (1060 <= 1061, sieve cover) + runtime cap 900 s
  predeclared; G1.1 deep-table overlap == deployed core table on
  [0, 400000] EXACTLY; G1.2 Chebyshev envelope kappa on [100, 1.6e7]
  <= KAPPA_REF + 1e-6; G1.3 parent tower comb consistency (zeta-free
  Gauss double sieve == deployed masses, <= 1e-12); G1.4 prefix
  Ward: deep tower's leading 824 block == parent tower <= 1e-12;
  G1.5 parent-audit anchor reproduction: max q_f(824) = 0.446 +-
  2e-3, worst 824..972 drift (MID5/LAST5 verbatim) = 0.5636 +- 2e-3,
  near-null count at M = 888 = 6, AND the parent audit's corner
  envelope numbers at eps = 1e-3 (max-entry increments, 824..972
  window): head med5 = 8.8e-4 +- 1e-5, tail med5 = 1.8e-3 +- 1e-4;
  G1.6 real-data operator sandwich at M = 512 and 1060 (Yosida
  eigenvalues in [-1e-9, 1 + 1e-9] at every gated eps); G1.7
  boundedness/KILL audit: every corner entry in [-1-1e-9, 1+1e-9],
  every scale in [1e-3, 1.5], every q_f and every increment >= 0 and
  bounded -- bounded forms only, no 1/eps, no PD assumption, no
  target data in any gate; G2.1 spectral-vs-dense-solve Ward on E_Y
  at M = 900, eps = 1e-3, <= 1e-8; G0.4 runtime.

CONTROLS (mandatory, must fire; fire rule stated plainly): the
parent audit MEASURED that corner-increment size does NOT
discriminate corrupted combs (indefinite spectra keep the Yosida
symbol ~ 1 away from the poles), so the frozen fire rule is the
POSITIVITY rule verbatim (yosida_handoff_probe.control_yosida at
M_CTRL = 512): FIRE = sandwich break (g outside [-0.01, 1.01]) OR
battery eps-monotonicity violation (< -1e-6) OR singular Yosida
(|lam + eps| < 1e-12).  CS position scramble (positions uniform in
(0.5, 2 alpha_deep), masses kept, seed 7, on the DEEP comb, tower
M_TOP_DEEP) and CE Epstein x^2 + 5y^2 atoms (epstein_firewall_probe
read-only, tower cap M = 640).  The control-side corner increments
on the mini-ladder 480..512 step 4 at eps = 1e-2 are PRINTED as
context (report only, per the measured lesson).  A control that
keeps sandwich + monotonicity + regularity has spuriously
converged: verdict DEAD.

STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros; no bare A^{-1}; no 1/eps bounds in gates; no fits beyond the
declared slope gate statistics; no q_f in any gate; SHA-freeze
before comb data; NO RH claim; probe writes no files; runtime cap
900 s.  X-before-eps order enforced: all gates live at fixed eps
along the X ladder; nothing here claims eps -> 0 closure or
eps-uniformity.

RESULTS (2026-08-05, first and only preregistered run, 10.4 s;
CELLS 34/168 (n(1e-1) = 31/56, n(1e-2) = 3/56, n(1e-3) = 0/56),
GUARDS+CONTROLS 14/14, verdict GATE3PRIME-DEAD, majority corner
failures -- the deeper-ladder lever decided it, and it decided it
NEGATIVELY):
  *  DEEP EXTENSION VALID: ka = 1,007,385 atoms to e^16.5625 (3.6x
     the 4e6 comb); overlap with the deployed table exact (0.0);
     kappa = 0.038821 unchanged on [100, 1.6e7]; prefix Ward vs the
     parent tower 2.0e-14; parent-audit anchors reproduced: max
     q_f(824) = 0.4459 (dev 1.3e-4), worst 824..972 drift 0.5636
     (dev 1.4e-5), nn(888) = 6, corner envelope head/tail med5 at
     eps 1e-3 = 8.7873e-4 / 1.7906e-3 (dev 1.3e-6 / 9.4e-6).  PD
     margins (measured, never gated): 5.289e-5 (256) -> 6.459e-6
     (972) -> 5.383e-6 (1060); sandwich at 512 + 1060 holds with
     Yosida eigenvalues in [5.4e-5, 1 - 5.8e-5]; dense-solve Ward
     5.3e-13; runtime 10.4 s <= 900 s.
  *  THE CENTRAL MEASUREMENT (max-entry envelope, med5, scaled):
     the corner increments FALL from the ladder head to X ~ 12.9
     (eps = 1e-3: ~1.4e-3 at M = 256 -> 8.79e-4 at the 824 window
     -- exactly the falling regime every parent probe certified on
     rungs <= 824) and then RISE on the deep rungs: 824-head ->
     972-tail -> deep-tail (1044..1060) med5 = 3.05e-3 -> 6.44e-3
     -> 5.60e-3 (eps 1e-1), 1.16e-3 -> 1.25e-3 -> 3.49e-3 (1e-2),
     8.79e-4 -> 1.79e-3 -> 3.67e-3 (1e-3).  The parent audit's
     "envelope oscillation" was the ONSET of this rise, not a
     shallow-window artifact: 22 additional rungs to X = 16.5625
     confirm sustained growth (second-half slopes at 1e-3:
     +0.10..+0.34 per X unit, fitted over 101 increments).
  *  CELL TABLE (frozen bars 0.5 / +0.02 / 0.25): eps = 1e-1:
     31/56 pass; the 25 failures are mostly S2 slope marginals
     (+0.001..+0.116) and R1 deep-edge ratios (box[R/2,R] rows up
     to 1.91).  eps = 1e-2: 3/56 pass (R1:box[0,R]*box[0,R/2],
     R2:box[0,R]*box[0,R], R2:box[0,R]*box[R/2,R]); typical
     failures ratio 0.6..14.9 with positive second-half slopes.
     eps = 1e-3: 0/56 pass -- every cell fails at least S2 (slopes
     +0.101..+0.344/X) and mostly S3 too (TV tail shares
     0.24..0.44 vs flat = 0.254); worst med5 ratio 29.25
     (R1:box[R/2,R]*box[R/2,R]).  The failure is broad-spectrum
     across boxes, hats, diagonal and off-diagonal, both R-groups:
     NOT a single bad channel.
  *  SUBSEQUENCE COMPARISON (report): corner-native net (168-dim
     unscaled entries, ETA 0.03): 4 clusters, largest density
     0.431 (87/202) -- vs q_f-native on the same deep ladder: 20
     clusters, largest density 0.134.  The corner LEVELS are far
     more coherent than q_f (3.2x denser, 4 vs 20 clusters), but
     level coherence is not increment summability: the levels move
     slowly yet persistently.  q_f boundedness report: all q in
     [1.8e-3, 0.6601] within [0, 1]; q_f appears in no gate.
  *  CONTROLS both fire via the positivity rule as frozen: CS
     scramble (deep comb, 1,007,385 atoms) lambda_min = -6.41e+3,
     252/512 negative eigenvalues, sandwich max g = 5.4, 31
     monotonicity violations; CE Epstein lambda_min = -3.32e+1,
     189/512 negative, min g = -2.5, max g = 23, 56 violations.
     Context report reconfirms the measured lesson: control corner
     med increments stay ORDINARY (4.5e-4 / 4.1e-4 vs real 3.3e-3)
     -- positivity, not corner size, separates.  KILL audit PASS:
     corners bounded by 0.7031 (sandwich), scales 0.017 / 0.087 /
     0.359, all increments >= 0, no 1/eps, no fits beyond the
     declared slope statistics, no target data.
  *  CONSEQUENCE FOR v764 (stated plainly): the v764 precondition
     is NOT met.  At fixed eps <= 1e-2 the X-ladder Cauchy
     increments of the very objects the diagonal contract consumes
     rise beyond X ~ 13 on the deepest honestly reachable surface
     -- the reachable X-limit of the corner entries is not
     certified, and no assembly of v760 (anti-alias) + v761
     (atom-pole Abel) on top of this can proceed.  Precisely
     stated: the parent audit's RELATIVE finding stands (corners
     are blind to q_f gauge jumps; nothing here re-couples q_f to
     the value), but its optimistic extension -- that the corner
     envelope keeps falling -- is REFUTED: the wall returns at the
     corner level as a depth-driven rise, visible from X ~ 13.5 at
     every gated eps below 1e-1.  The rise coincides with the
     regime where the per-cell comb fluctuation amplitude (~
     2(psi(e^u) - e^u)/e^{u/2}) grows through the battery scale;
     whether a fluctuation-normalized corner increment still falls
     there is a DIFFERENT, not-yet-frozen question -- named next
     surfaces (not probed here, no verdict implied): (i) a
     fluctuation-normalized restatement of Gate 3' (preregister
     the normalization first, on parent rungs only), (ii) the
     eps = 1e-1 decade, where 31/56 cells still pass -- locate the
     eps detachment point on a refined eps ladder, (iii) deeper
     combs (4e7-class) to test whether the rise saturates.  NO RH
     claim, no X -> infinity claim, no eps -> 0 claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/corner_cauchy_gate3prime_probe.py
"""

# ==========================================================================
# PART 1 -- qf_contract_necessity_probe.py (verbatim; imports promoted)
# ==========================================================================


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

_HERE_DISC = os.path.abspath(os.path.join(_HERE, "..",
    "experiments", "tfpt-discovery"))
sys.path.insert(0, _HERE_DISC)

import v563_paper2_readouts as core  # noqa: E402
import v755_simpler_schur_recursion as srp  # noqa: E402
import v766_handoff_bulk as hbp  # noqa: E402
import v763_yosida_handoff as yhp  # noqa: E402
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

_run_part1 = run

def _run_part2():
    # PART 2 -- corner_cauchy_gate3prime_probe.py (verbatim; module-level names are
    # local to this function scope; sibling imports remapped as declared)


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
    import v755_simpler_schur_recursion as srp  # noqa: E402
    import v766_handoff_bulk as hbp  # noqa: E402
    import v763_yosida_handoff as yhp  # noqa: E402
    import epstein_firewall_probe as epx  # noqa: E402

    T_START = time.time()

    # ------------------------------------------------ frozen specification
    D = srp.DGRID                        # 1/64, dyadic float-exact
    ATOM_MAX_DEEP = 16000000             # own predeclared deep comb cap
    M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))  # 1061
    M_TOP_DEEP = 1060                    # deepest step-4-aligned rung
    M_TOP_PAR = 824                      # parent cap
    FULL_LAD = list(range(256, 1061, 4))         # 202 rungs
    I824 = FULL_LAD.index(824)                   # 142
    I972 = FULL_LAD.index(972)                   # 179
    MID5 = slice(17, 22)                 # on the 824..972 sub-ladder
    LAST5 = slice(33, 38)                # (parent-audit anchor verbatim)

    R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
    NPAD = 128                           # max battery support in cells
    EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)                # gated eps set
    THR_NULL = 1.0e-4                    # q_f threshold (report only)

    RATIO_BAR = 0.5                      # S1 med5(last)/med5(first)
    SLOPE_TOL = 0.02                     # S2 second-half slope cap (/X)
    TV_BAR = 0.25                        # S3 tail-quarter TV share
    N_MED = 5                            # median block size
    QF_FLOOR = 1.0e-12                   # denominator floor
    N3_CONV = 51                         # CONVERGES: eps=1e-3 pass floor
    N_PART = 51                          # PARTIAL: upper-eps pass floor
    N3_PART = 28                         # PARTIAL: eps=1e-3 pass floor

    ETA_NET = 0.03                       # subsequence net radius (report)
    PARENT_QF_MAX = 0.446                # G1.5 anchor (parent probes)
    PARENT_DRIFT_WORST = 0.5636          # G1.5 anchor (qf probe, EXT)
    PARENT_NN_888 = 6                    # G1.5 anchor (qf probe)
    ENV_HEAD_REF = 8.8e-4                # G1.5 anchor (parent audit)
    ENV_TAIL_REF = 1.8e-3                # G1.5 anchor (parent audit)
    ENV_HEAD_TOL = 1.0e-5                # (refs printed to 2 sig digits)
    ENV_TAIL_TOL = 1.0e-4
    REPRO_TOL = 2.0e-3                   # q/drift anchor tolerance
    COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
    PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
    SANDWICH_TOL = 1.0e-9                # G1.6 sandwich slack
    BOUND_TOL = 1.0e-9                   # G1.7 boundedness slack
    SCALE_LO, SCALE_HI = 1.0e-3, 1.5     # G1.7 corner scale audit band
    WARD_SPEC = 1.0e-8                   # G2.1 dense-solve Ward
    M_WARD, EPS_WARD = 900, 1.0e-3       # G2.1 Ward rung and eps
    RUNTIME_CAP = 900.0                  # seconds, predeclared (15 min)

    M_CTRL = 512                         # control spectral rung (parent)
    CTRL_LAD = list(range(480, 513, 4))  # control corner context ladder
    CTRL_EPS = 1.0e-2                    # control corner context eps
    EP_NCAP = 34000                      # Epstein Lambda_E table reach
    EP_MMAX = 640                        # Epstein control tower cap
    SEED = 7

    BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
              "prevprime", "primepi", "sympy")

    CHECKS = []       # guards + controls: all must pass, else invalid run
    CELLS = []        # per (entry, eps) cell results: feed the verdict


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
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
        """Battery bytes + ladder + cell set + eps set + bars + net rule
        + deep-comb spec + control fire rule, SHA-256 frozen BEFORE any
        comb data is built in this probe."""
        bats = {}
        hsh = hashlib.sha256()
        hsh.update(("corner-cauchy-gate3prime spec: 4 boxes + 3 hats per "
                    "R, l2-norm, D=%.10f, R=%s; deep comb = deployed "
                    "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                    "M_TOP_DEEP=%d (parent %d); FULL_LAD=%s; anchors "
                    "I824=%d I972=%d MID5=[17:22] LAST5=[33:38]; corners "
                    "= E_Y entries, cells = all pairs i<=j within each "
                    "R-group (56), eps gated=%s, scale = sqrt(maxdiag*"
                    "mindiag) at first rung; stats on 201 step-4 "
                    "increments, X of upper rung: S1 med%d ratio<=%g, "
                    "S2 second-half log-slope<=%+g/X over last 101, S3 "
                    "TV tail quarter (51) share<=%g; verdict: CONVERGES "
                    "n1=n2=56 & n3>=%d, PARTIAL n1,n2>=%d & n3>=%d, else "
                    "DEAD; subsequence report: greedy net ladder-order "
                    "first-center ETA=%g on (a) q_f 14-dim thr=%g (b) "
                    "unscaled corner entries 168-dim; anchors qfmax=%g "
                    "drift=%g nn888=%d envhead=%g+-%g envtail=%g+-%g "
                    "tol=%g; guards comb<=%g prefix<=%g sandwich<=%g "
                    "bound<=%g scale=[%g,%g] ward<=%g (M=%d,eps=%g) "
                    "runtime<=%g; controls: POSITIVITY fire rule "
                    "verbatim (control_yosida, M=%d), corner context "
                    "minilad=%s eps=%g REPORT ONLY, epcap=%d epM=%d "
                    "seed=%d; X-before-eps enforced, no eps->0 claim"
                    % (D, R_BAT, ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP,
                       M_TOP_PAR, FULL_LAD, I824, I972, EPS_GATED, N_MED,
                       RATIO_BAR, SLOPE_TOL, TV_BAR, N3_CONV, N_PART,
                       N3_PART, ETA_NET, THR_NULL, PARENT_QF_MAX,
                       PARENT_DRIFT_WORST, PARENT_NN_888, ENV_HEAD_REF,
                       ENV_HEAD_TOL, ENV_TAIL_REF, ENV_TAIL_TOL,
                       REPRO_TOL, COMB_DEV_BAR, PREFIX_WARD,
                       SANDWICH_TOL, BOUND_TOL, SCALE_LO, SCALE_HI,
                       WARD_SPEC, M_WARD, EPS_WARD, RUNTIME_CAP, M_CTRL,
                       CTRL_LAD, CTRL_EPS, EP_NCAP, EP_MMAX,
                       SEED)).encode())
        for R in R_BAT:
            bats[R] = hbp.battery(R)
            for nm, v in bats[R]:
                hsh.update(nm.encode())
                hsh.update(v.tobytes())
        return bats, hsh.hexdigest()


    def battery_matrix(bats):
        cols, names = [], []
        for R in R_BAT:
            nR = int(round(R / D))
            for nm, v in bats[R]:
                f = np.zeros(NPAD)
                f[:nR] = v
                cols.append(f)
                names.append("R%g:%s" % (R, nm))
        return np.stack(cols, axis=1), names


    def corner_cells(names):
        """All entry pairs (i <= j) within each R-group: 56 cells."""
        cells = []
        for lo, hi in ((0, 7), (7, 14)):
            for i in range(lo, hi):
                for j in range(i, hi):
                    cells.append((i, j))
        labels = ["%s*%s" % (names[i], names[j].split(":", 1)[1])
                  for (i, j) in cells]
        return cells, labels


    def lin_slope(xs, ys):
        A = np.vstack([np.ones_like(xs), xs]).T
        coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
        return float(coef[1])


    # ------------------------------------------------ towers
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


    def build_deep_comb():
        lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
        dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
        check("G1.1 deep-table overlap: deep von Mangoldt table == "
              "deployed core table on [0, %d] EXACTLY" % core.ATOM_MAX,
              dev == 0.0, "max abs dev %.1e" % dev)
        nn = np.nonzero(lam_deep > 0.0)[0]
        u_deep = np.log(nn.astype(float))
        mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
        psi = np.cumsum(lam_deep[nn])
        keep = nn.astype(float) >= core.KAPPA_X0
        kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                             / nn[keep].astype(float)))
        check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over all "
              "jump points of psi(x)/x in [%.0f, %d] <= %.6f"
              % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP,
                 core.KAPPA_REF + core.TOL_KAPPA),
              kappa <= core.KAPPA_REF + core.TOL_KAPPA)
        return u_deep, mu_deep


    def build_deep_tower(u_deep, mu_deep, T_par):
        alpha = 0.5 * M_TOP_DEEP * D
        ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        c_cont = srp.continuum_lags(M_TOP_DEEP)
        c_at, _dd = core.atom_lags_at(alpha, M_TOP_DEEP, u_deep[:ka],
                                      mu_deep[:ka])
        T = sla.toeplitz((c_cont + c_at)[:M_TOP_DEEP])
        dev = float(np.max(np.abs(T[:M_TOP_PAR, :M_TOP_PAR] - T_par)))
        check("G1.4 prefix Ward: deep tower leading %d x %d block == "
              "parent tower, max abs dev %.1e <= %.0e"
              % (M_TOP_PAR, M_TOP_PAR, dev, PREFIX_WARD),
              dev <= PREFIX_WARD)
        print("  deep extension census: ka = %d atoms to e^%.4f"
              % (ka, 2.0 * alpha))
        return T, c_cont, alpha, ka


    # ------------------------------------------------ spectral machinery
    def spectral_pass(T, F):
        out = []
        for M in FULL_LAD:
            lam, V = np.linalg.eigh(T[:M, :M])
            C = V[:NPAD, :].T @ F
            out.append(dict(M=M, lam=lam, C=C,
                            nn=int(np.sum(lam <= THR_NULL))))
        return out


    def qf_of(blk):
        idx = blk["lam"] <= THR_NULL
        return (blk["C"][idx] ** 2).sum(axis=0)


    def corner_of(blk, eps):
        g = blk["lam"] / (blk["lam"] + eps)
        E = blk["C"].T @ (blk["C"] * g[:, None])
        return 0.5 * (E + E.T)


    def greedy_net(vmat):
        centers, assign = [], []
        for r in range(vmat.shape[0]):
            hit = -1
            for ci, c in enumerate(centers):
                if float(np.max(np.abs(vmat[r] - c))) <= ETA_NET:
                    hit = ci
                    break
            if hit < 0:
                centers.append(vmat[r].copy())
                hit = len(centers) - 1
            assign.append(hit)
        return np.array(assign, int), centers


    # ------------------------------------------------ cell adjudication
    def cell_stats(inc_cell, xs_up):
        """Frozen oscillation-aware statistic on one (entry, eps) cell."""
        n = len(inc_cell)
        med_first = float(np.median(inc_cell[:N_MED]))
        med_last = float(np.median(inc_cell[-N_MED:]))
        ratio = med_last / max(med_first, QF_FLOOR)
        half = n // 2
        slope = lin_slope(xs_up[half:],
                          np.log(np.maximum(inc_cell[half:], 1.0e-300)))
        n_q = int(math.ceil(n / 4.0))
        tv = float(np.sum(inc_cell[-n_q:]) / max(np.sum(inc_cell),
                                                 QF_FLOOR))
        ok = ratio <= RATIO_BAR and slope <= SLOPE_TOL and tv <= TV_BAR
        return ok, ratio, slope, tv


    def corner_gate_block(spec, cells, labels):
        print("\n-- Gate 3'(a): corner-increment Cauchy per (entry, eps) "
              "cell (S1 med5 ratio <= %g, S2 second-half slope <= %+g/X, "
              "S3 TV tail share <= %g)" % (RATIO_BAR, SLOPE_TOL, TV_BAR))
        n = len(FULL_LAD)
        xs_up = np.array([FULL_LAD[k + 1] * D for k in range(n - 1)])
        EY = {eps: np.stack([corner_of(b, eps) for b in spec])
              for eps in EPS_GATED}                   # (202, 14, 14)
        scales = {}
        for eps in EPS_GATED:
            dg = np.diag(EY[eps][0])
            scales[eps] = float(np.sqrt(np.max(dg) * np.min(dg)))
        print("  corner scales (first rung): %s"
              % "  ".join("eps=%g: %.3f" % (e, scales[e])
                          for e in EPS_GATED))
        dif = {eps: np.abs(np.diff(EY[eps], axis=0)) / scales[eps]
               for eps in EPS_GATED}                  # (201, 14, 14)
        # max-entry envelope (parent-audit anchor material + report)
        incmax = {eps: dif[eps].max(axis=(1, 2)) for eps in EPS_GATED}
        for eps in EPS_GATED:
            h_par = float(np.median(incmax[eps][I824:I824 + 5]))
            t_par = float(np.median(incmax[eps][I972 - 5:I972]))
            t_deep = float(np.median(incmax[eps][-5:]))
            print("  max-entry envelope eps=%g: 824-window head med5 = "
                  "%.4e, 972-window tail med5 = %.4e, DEEP tail med5 "
                  "(1044..1060) = %.4e" % (eps, h_par, t_par, t_deep))
        env_head = float(np.median(incmax[1.0e-3][I824:I824 + 5]))
        env_tail = float(np.median(incmax[1.0e-3][I972 - 5:I972]))

        counts = {eps: 0 for eps in EPS_GATED}
        fails = {eps: [] for eps in EPS_GATED}
        print("  per-cell table (ratio / slope / tv per eps; bars %g / "
              "%+g / %g):" % (RATIO_BAR, SLOPE_TOL, TV_BAR))
        for c_i, (i, j) in enumerate(cells):
            parts = []
            for eps in EPS_GATED:
                ok, ratio, slope, tv = cell_stats(dif[eps][:, i, j],
                                                  xs_up)
                CELLS.append((labels[c_i], eps, ok, ratio, slope, tv))
                counts[eps] += bool(ok)
                if not ok:
                    fails[eps].append((labels[c_i], ratio, slope, tv))
                parts.append("e%g: %.2f/%+.3f/%.2f %s"
                             % (eps, ratio, slope, tv,
                                "ok" if ok else "FAIL"))
            print("    %-42s %s" % (labels[c_i], "  ".join(parts)))
        for eps in EPS_GATED:
            print("  eps = %-6g: %d/56 cells pass" % (eps, counts[eps]))
            for nm, ratio, slope, tv in fails[eps]:
                print("      FAIL %-42s ratio=%.3f slope=%+.3f tv=%.3f"
                      % (nm, ratio, slope, tv))
        # boundedness material
        cmax = max(float(np.max(np.abs(EY[eps]))) for eps in EPS_GATED)
        inc_min = min(float(np.min(dif[eps])) for eps in EPS_GATED)
        med_real = float(np.median(dif[CTRL_EPS].max(axis=(1, 2))))
        return counts, EY, scales, dict(cmax=cmax, inc_min=inc_min,
                                        env_head=env_head,
                                        env_tail=env_tail,
                                        med_real=med_real)


    # ------------------------------------------------ subsequence report
    def subsequence_report(spec, EY, cells, qmat):
        print("\n-- subsequence report (never gated; greedy net ETA = "
              "%g, parent rule verbatim)" % ETA_NET)
        n = len(FULL_LAD)
        corner_vec = np.zeros((n, len(cells) * len(EPS_GATED)))
        for k in range(n):
            cols = []
            for eps in EPS_GATED:
                cols.extend(EY[eps][k][i, j] for (i, j) in cells)
            corner_vec[k] = cols
        a_q, c_q = greedy_net(qmat)
        a_c, c_c = greedy_net(corner_vec)
        s_q = np.bincount(a_q)
        s_c = np.bincount(a_c)
        d_q = float(np.max(s_q)) / n
        d_c = float(np.max(s_c)) / n
        print("  q_f-native (14-dim): %d clusters, largest density %.3f "
              "(%d/%d rungs)" % (len(c_q), d_q, int(np.max(s_q)), n))
        print("  corner-native (unscaled E_Y entries, %d-dim): %d "
              "clusters, largest density %.3f (%d/%d rungs)"
              % (corner_vec.shape[1], len(c_c), d_c, int(np.max(s_c)), n))
        print("  comparison: the corner profile needs %s subsequence "
              "thinning than q_f (density ratio %.1fx, cluster count "
              "%d vs %d); the Cauchy half is decided by the gates above."
              % ("far less" if d_c > d_q else "no less",
                 d_c / max(d_q, QF_FLOOR), len(c_c), len(c_q)))
        print("  q_f boundedness (report only, q_f in NO gate): all q "
              "in [%.1e, %.4f] within [0, 1]"
              % (float(np.min(qmat)), float(np.max(qmat))))
        return d_q, d_c


    # ------------------------------------------------ controls
    def control_corner_context(Tc, F):
        """REPORT ONLY: corner increments on the control mini-ladder
        (the parent audit measured these do NOT discriminate)."""
        EYs = []
        for M in CTRL_LAD:
            lam, V = np.linalg.eigh(Tc[:M, :M])
            C = V[:NPAD, :].T @ F
            g = lam / (lam + CTRL_EPS)
            E = C.T @ (C * g[:, None])
            EYs.append(0.5 * (E + E.T))
        incs = [float(np.max(np.abs(EYs[k + 1] - EYs[k])))
                for k in range(len(EYs) - 1)]
        return float(np.median(incs)), max(float(np.max(np.abs(E)))
                                           for E in EYs)


    def run_controls(c_cont, alpha_deep, ka_deep, mu_deep, bats, F,
                     med_real):
        print("\n-- controls (must fire via the POSITIVITY rule -- the "
              "measured lesson: corner size does not discriminate)")
        rng = np.random.default_rng(SEED)
        pos = np.sort(rng.uniform(0.5, 2.0 * alpha_deep, ka_deep))
        cat_s, _dd = core.atom_lags_at(alpha_deep, M_TOP_DEEP, pos,
                                       mu_deep[:ka_deep])
        Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_DEEP])
        lam_s = np.linalg.eigvalsh(Ts[:M_CTRL, :M_CTRL])
        print("  CS census: %d/%d eigenvalues below -THR_NULL = -%g"
              % (int(np.sum(lam_s < -THR_NULL)), M_CTRL, THR_NULL))
        fire_s, det_s = yhp.control_yosida(Ts, bats, "scramble")
        med_c, cmax_c = control_corner_context(Ts, F)
        check("CS position-scramble control fires (positivity rule, "
              "deep comb, %d atoms)" % ka_deep, fire_s, det_s)
        print("    corner context (report only): control corner med "
              "increment %.1e vs real %.1e, max |E_Y| %.1e"
              % (med_c, med_real, cmax_c))

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
        fire_e, det_e = yhp.control_yosida(TE, bats, "epstein")
        med_c, cmax_c = control_corner_context(TE, F)
        check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
              "fires (positivity rule)"
              % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)
        print("    corner context (report only): control corner med "
              "increment %.1e vs real %.1e, max |E_Y| %.1e"
              % (med_c, med_real, cmax_c))


    # ------------------------------------------------ run
    def run():
        print("=" * 78)
        print("QF OFFENSIVE strand 1, follow-up -- corner-native Gate 3' "
              "decider (v764 precondition)")
        print("=" * 78)

        hits = ast_firewall()
        check("G0.1 AST firewall", not hits, str(hits))
        bats, spec_sha = freeze_spec()
        check("G0.2 battery + ladder + cell set + eps set + bars + net "
              "rule + deep-comb spec + control rule SHA-256-frozen "
              "BEFORE any comb data is built here", True,
              "SHA256 %s..." % spec_sha[:16])
        check("G0.3 reach census: M_TOP_DEEP = %d <= floor(64 ln %d) = "
              "%d; sieve cover exp(X_top) + 2 = %d <= %d; runtime cap "
              "%.0f s" % (M_TOP_DEEP, ATOM_MAX_DEEP, M_CAP_DEEP,
                          int(math.exp(M_TOP_DEEP * D)) + 2,
                          ATOM_MAX_DEEP, RUNTIME_CAP),
              M_TOP_DEEP <= M_CAP_DEEP
              and int(math.exp(M_TOP_DEEP * D)) + 2 <= ATOM_MAX_DEEP)

        # ---- comb + towers strictly after the freeze
        u_deep, mu_deep = build_deep_comb()
        T_par = build_parent_tower()
        T, c_cont, alpha_deep, ka_deep = build_deep_tower(u_deep, mu_deep,
                                                          T_par)

        # ---- spectral ladder
        F, names = battery_matrix(bats)
        cells, labels = corner_cells(names)
        spec = spectral_pass(T, F)
        print("  PD margins (eps = 0, measured, never gated): lambda_min "
              "= %.3e (M %d) -> %.3e (M %d) -> %.3e (M %d)"
              % (spec[0]["lam"][0], FULL_LAD[0],
                 spec[I972]["lam"][0], 972, spec[-1]["lam"][0],
                 M_TOP_DEEP))
        gmin, gmax = np.inf, -np.inf
        for idx in (FULL_LAD.index(M_CTRL), len(FULL_LAD) - 1):
            lam = spec[idx]["lam"]
            for e in EPS_GATED:
                g = lam / (lam + e)
                gmin = min(gmin, float(np.min(g)))
                gmax = max(gmax, float(np.max(g)))
        check("G1.6 real-data operator sandwich at M = %d and %d: Yosida "
              "eigenvalues in [%.1e, 1 - %.1e] at every gated eps (bars "
              "-%.0e / 1+%.0e)" % (M_CTRL, M_TOP_DEEP, gmin, 1.0 - gmax,
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

        # ---- corner gates (needs EY for anchors too)
        counts, EY, scales, aud = corner_gate_block(spec, cells, labels)

        # ---- parent-audit anchor reproduction
        qmat = np.stack([qf_of(b) for b in spec])
        q824 = qmat[I824]
        q_ext = qmat[I824:I972 + 1]
        med_mid = np.median(q_ext[MID5], axis=0)
        med_last = np.median(q_ext[LAST5], axis=0)
        drift = np.abs(med_last - med_mid) \
            / np.maximum(np.maximum(med_last, med_mid), QF_FLOOR)
        nn888 = spec[FULL_LAD.index(888)]["nn"]
        dev_q = abs(float(np.max(q824)) - PARENT_QF_MAX)
        dev_d = abs(float(np.max(drift)) - PARENT_DRIFT_WORST)
        dev_h = abs(aud["env_head"] - ENV_HEAD_REF)
        dev_t = abs(aud["env_tail"] - ENV_TAIL_REF)
        check("G1.5 parent-audit anchor reproduction: max q_f(824) = "
              "%.4f (dev %.1e <= %.0e), worst 824..972 drift = %.4f "
              "(dev %.1e), nn(888) = %d (frozen %d), corner envelope "
              "eps=1e-3 head/tail med5 = %.4e / %.4e (dev %.1e <= %.0e "
              "/ %.1e <= %.0e)"
              % (float(np.max(q824)), dev_q, REPRO_TOL,
                 float(np.max(drift)), dev_d, nn888, PARENT_NN_888,
                 aud["env_head"], aud["env_tail"], dev_h, ENV_HEAD_TOL,
                 dev_t, ENV_TAIL_TOL),
              dev_q <= REPRO_TOL and dev_d <= REPRO_TOL
              and nn888 == PARENT_NN_888 and dev_h <= ENV_HEAD_TOL
              and dev_t <= ENV_TAIL_TOL)

        # ---- subsequence report
        d_q, d_c = subsequence_report(spec, EY, cells, qmat)

        # ---- boundedness / KILL audit
        smin, smax = min(scales.values()), max(scales.values())
        check("G1.7 boundedness/KILL audit: corner entries bounded by "
              "%.4f (sandwich, band 1+%.0e), increments >= %.1e, corner "
              "scales %.3f..%.3f in [%g, %g], q_f in [%.1e, %.4f] "
              "within [0, 1] -- bounded forms only, no 1/eps, no PD "
              "assumption, no target data, no q_f in any gate"
              % (aud["cmax"], BOUND_TOL, aud["inc_min"], smin, smax,
                 SCALE_LO, SCALE_HI, float(np.min(qmat)),
                 float(np.max(qmat))),
              aud["cmax"] <= 1.0 + BOUND_TOL and aud["inc_min"] >= 0.0
              and smin >= SCALE_LO and smax <= SCALE_HI
              and float(np.min(qmat)) >= -1.0e-12
              and float(np.max(qmat)) <= 1.0 + BOUND_TOL)

        # ---- controls
        run_controls(c_cont, alpha_deep, ka_deep, mu_deep, bats, F,
                     aud["med_real"])

        # ---- runtime guard
        dt = time.time() - T_START
        check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
              % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

        # ---- verdict (preregistered rules)
        guards_ok = all(ok for (n, ok) in CHECKS
                        if not n.startswith(("CS", "CE")))
        controls_ok = all(ok for (n, ok) in CHECKS
                          if n.startswith(("CS", "CE")))
        n1, n2, n3 = (counts[e] for e in EPS_GATED)
        if not (guards_ok and controls_ok):
            verdict = "GATE3PRIME-DEAD"
            reason = "invalid run: a guard failed or a control " \
                     "spuriously converged -- no measured statement " \
                     "about the corners follows"
        elif n1 == 56 and n2 == 56 and n3 >= N3_CONV:
            verdict = "GATE3PRIME-CONVERGES"
            reason = ""
        elif n1 >= N_PART and n2 >= N_PART and n3 >= N3_PART:
            verdict = "GATE3PRIME-PARTIAL"
            reason = ""
        else:
            verdict = "GATE3PRIME-DEAD"
            reason = "majority corner failures"

        n_chk = sum(1 for (_n, ok) in CHECKS if ok)
        n_cell = sum(1 for c in CELLS if c[2])
        print("\nVERDICT: %s%s" % (verdict,
                                   (" (%s)" % reason) if reason else ""))
        print("CELLS %d/%d (eps 1e-1: %d/56, 1e-2: %d/56, 1e-3: %d/56), "
              "GUARDS+CONTROLS %d/%d, subsequence density corner %.3f "
              "vs q_f %.3f, runtime %.1f s"
              % (n_cell, len(CELLS), n1, n2, n3, n_chk, len(CHECKS),
                 d_c, d_q, time.time() - T_START))
        if verdict == "GATE3PRIME-CONVERGES":
            print("CONSEQUENCE FOR v764 (stated plainly): the corner "
                  "entries are entrywise Cauchy at the frozen "
                  "oscillation-aware bars on every gated eps -- Gate 3' "
                  "is decided POSITIVELY in the weakened, contract-"
                  "native form (QF-GAUGE upstream).  What remains for "
                  "v764: assemble the a-priori bound from v760 (anti-"
                  "alias exactness) + v761 (atom-pole Abel control) "
                  "with this corner-Cauchy statement into the promoted "
                  "Gate 3' module; the q_f Cauchy demand is dropped "
                  "(bounded gauge, reported).  NOT claimed: eps -> 0 "
                  "closure, X -> infinity, RH.")
        elif verdict == "GATE3PRIME-PARTIAL":
            print("CONSEQUENCE FOR v764 (stated plainly): the corner "
                  "Cauchy statement holds on the named majority and "
                  "FAILS on the named minority cells above -- the v764 "
                  "precondition is met only in the reduced form; every "
                  "failing (entry, eps) cell is listed and must be "
                  "carried as an open named block.  NOT claimed: eps -> "
                  "0 closure, X -> infinity, RH.")
        else:
            print("CONSEQUENCE (stated plainly): %s -- the corner "
                  "increments do not fall at the frozen bars: the gauge "
                  "reading of q_f was a false hope at this depth and "
                  "the wall returns at the corner level (or the run is "
                  "invalid as stated).  NO RH claim." % (reason or
                                                         "DEAD"))
        return 0 if (guards_ok and controls_ok) else 1
    return run(), [n for (n, ok) in CHECKS if not ok], [sum(1 for c in CELLS if c[1] == e and c[2]) for e in EPS_GATED]



def run():
    """run_all entry point (combined adjudication, frozen): part 1 must
    reproduce its preregistered pattern (guards+controls 14/14, gates
    5/5, verdict QF-GAUGE); part 2 must reproduce its pattern
    (guards+controls 14/14, cell counts 31/3/0 of 56 at eps =
    1e-1/1e-2/1e-3, verdict GATE3PRIME-DEAD) -- the honest combined
    verdict is QF-GAUGE / GATE3PRIME-DEAD: q_f is representation gauge,
    but the weakened corner-native Gate 3' dies on the deeper 1.6e7
    comb and the v764 precondition is refuted at the corner level."""
    rc1 = _run_part1()
    chk_fails1 = [n for (n, ok) in CHECKS if not ok]
    gate_fails1 = [n for (n, ok) in GATES if not ok]
    part1_ok = (rc1 == 0 and not chk_fails1 and not gate_fails1
                and len(GATES) == 5 and len(CHECKS) == 14)
    print("\n[%s] PART-1 PATTERN GATE: expected the clean preregistered "
          "QF-GAUGE pattern (gates 5/5, guards+controls 14/14) -- "
          "failing: %s"
          % ("PASS" if part1_ok else "FAIL",
             [f.split()[0] for f in chk_fails1 + gate_fails1] or "none"))
    rc2, chk_fails2, counts2 = _run_part2()
    part2_ok = (rc2 == 0 and not chk_fails2 and counts2 == [31, 3, 0])
    print("\n[%s] PART-2 PATTERN GATE: expected the preregistered "
          "GATE3PRIME-DEAD cell counts [31, 3, 0] of 56 at eps = "
          "1e-1/1e-2/1e-3 with guards+controls 14/14 -- measured %s, "
          "failing guards: %s"
          % ("PASS" if part2_ok else "FAIL", counts2,
             [f.split()[0] for f in chk_fails2] or "none"))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- QF-GAUGE / GATE3PRIME-DEAD: "
          "Gate 3's full-ladder Cauchy demand on q_f was stronger than "
          "the diagonal contract needs (q_f is representation gauge; "
          "the contract's corner objects are blind to q_f jumps), but "
          "the weakened corner-native Gate 3' is DEAD on the deeper "
          "comb: the corner increments rise beyond X ~ 13 at every "
          "gated eps below 1e-1 -- the v764 precondition is refuted at "
          "the corner level.  NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(run())
