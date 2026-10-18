#!/usr/bin/env python3
"""v763 -- PRIME.YOSIDAQF.01: the kernel-safe eps -> 0 route via the bounded Yosida transform Y_eps = A (A + eps I)^{-1}, one module from two probes (v518/v668 merge precedent), combined verdict YOSIDA-PARTIAL / QF-DEAD.  PART 1 (YOSIDA-PARTIAL, 9/10 gates, 12/12 guards+controls): Q1 -- the bounded Yosida formulation carries the handoff rates (|b_Y - b_G| <= 1.0e-13, sandwich 0 <= diag(E_Y) <= 1 verified over all 360 evaluations, NO 1/eps bound or PD-margin anywhere: the preregistered circularity kill did NOT fire); Q2 -- the near-kernel converges as an identified stable object (alignment 0.988, count stable); Q4 -- every fixed battery f has a monotone, contraction-certified eps-limit (contraction 0.011..0.108); Q3 FAILED both frozen branches (all 14 functions pair above 1e-3, max q_f = 0.446).  PART 2 (QF-DEAD, the Q3 follow-up at honest maximal depth): the comb honestly extended to ATOM_MAX 4e6 / X = 15.1875 / 279849 atoms with all extension guards (overlap exact, Chebyshev envelope unchanged, prefix Ward 2e-14); q_f is non-Cauchy at the frozen bars on 12/14 functions (worst drift 0.564, worst slope 0.806/X vs bars 0.15) while the near-kernel OBJECT stays stable (A3: alignment 0.9997, count 6 constant from M = 888); Candidate B reveals the structural subordination -- 89..99.9% of every battery function lies in the 6-mode near-kernel span (retained norm^2 0.0007..0.107 vs floor 0.30), and the orthogonalized remnant loses the R = 1 rates (b_Y = 0.060 < 0.10 floor at eps = 1e-3): Q3 closes NEGATIVELY on the reachable surface -- the q_f wall is THE named object (density and near-kernel avoidance collide on the same function class).  What survives: Q1/Q2/Q4 untouched.  NO RH claim, no X -> infinity claim.

PROVENANCE: discovery probes yosida_handoff_probe.py (2026-08-04, GATES 9/10 with Q3 the preregistered open fail, GUARDS+CONTROLS 12/12, verdict YOSIDA-PARTIAL) and yosida_qf_convergence_probe.py (2026-08-04, GATES 7/12 with A1/A2/B1 + two B2 cells the honest fails, GUARDS+CONTROLS 14/14, iteration SPENT on Candidate B, verdict QF-DEAD).  Merged per the v518/v668 precedent: part 1 verbatim at module level (sibling imports point at v563/v755/v766/v768; epstein_firewall_probe stays a read-only discovery import); part 2 verbatim inside an isolated function scope (its module-level names are function-local; its yosida_handoff_probe alias points at this module); numbers unchanged.  run() encodes both preregistered gate patterns as the expected outcome (v757 precedent).

PART 1 -- yosida_handoff_probe.py (docstring verbatim):
GLOBAL-HANDOFF-OFFENSIVE -- the kernel-safe eps -> 0 decider via the
bounded Yosida transform, yosida_handoff_probe (strand: kernel-safe
epsilon limit; intended promotion target v763_yosida_handoff).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  handoff_bulk_probe -- HANDOFF-BULK-CONVERGES: the eps-regulated
     resolvent G^eps = (A_X + eps I)^{-1} is the admissible
     operator-system evaluation; the bare A^{-1} does NOT stabilize
     (named negative block) and stays FORBIDDEN here.
  *  handoff_tail_weil_probe -- HANDOFF-TAIL-WEIL-PARTIAL: b values
     eps 1e-1: 0.179/0.181, 1e-2: 0.216/0.129 (R = 1/2, 18-rung
     interleave); the two eps = 1e-3 cells failed its endpoint gates.
  *  handoff_compat_eps3_probe -- COMPAT-EPS3-CONVERGES on the SAME
     geometry reused here (LAD_A = 256..816 step 16, B = A + 8,
     M_TOP = 824): b(eps) table 1e-1: 0.239/0.185, 1e-2: 0.259/0.149,
     1e-3: 0.178/0.186; outlook eps = 3e-4: R = 1 second-half slope
     turns NEGATIVE (b2 = -0.011) -- the first concrete sign of the
     eps -> 0 wall; eps = 0 PD margins fall 5.289e-5 (W_256) ->
     8.265e-6 (W_824).

OBJECT (the kernel-safe route): the eps -> 0 wall of the resolvent
formulation sits in the INSTRUMENT, not necessarily in the object: the
resolvent bound ||G^eps|| <= 1/eps forces a positive-margin assumption
at the limit.  The bounded YOSIDA TRANSFORM

    Y_eps = A (A + eps I)^{-1} = I - eps (A + eps I)^{-1}

needs no margin: for PSD A it satisfies the SANDWICH 0 <= Y_eps <= I,
and as eps decreases Y_eps increases MONOTONELY (spectral map
g_eps(l) = l/(l + eps), pointwise increasing in decreasing eps for
l >= 0) with strong limit = the orthogonal projection onto the closure
of range(A).  Exact zero modes are ALLOWED -- the Ihara lesson already
typed in the repo: true RH analogues can carry exact null modes after
rank saturation; a uniform positive eigenvalue margin is stronger than
needed and the wrong instrument.  Everything below uses ONLY A >= 0
(measured, never assumed as a margin) and bounded spectral functions
of A; the bare A^{-1} is never formed.

PREDECLARED ALGEBRA (honesty, stated BEFORE the run): on nested
window prefixes the battery Gram <f_i, f_j> is window-independent, so
the Y-form cross-window defect is EXACTLY eps times the resolvent
defect: E_Y = Gram - eps E_G  =>  E_Y(B) - E_Y(A) = -eps (E_G(B) -
E_G(A)).  The measured content of Q1 is therefore NOT a new rate but
(i) that the identical falling rates are carried by an observable
BOUNDED BY 1 on an O(1) scale (no 1/eps normalization anywhere),
(ii) that the defect AMPLITUDE shrinks linearly in eps on that fixed
scale (the eps- and X-limits lose their fight on the reachable
surface), and (iii) the sandwich + double monotonicity certificates
(increasing in decreasing eps, decreasing in growing X via PSD Schur
increments).  This equality is declared here so it cannot be sold as
an independent discovery.

FINITE-M HONESTY (declared): at every finite window A_M is PD, so
Y_eps -> I strongly and every fixed-f limit exists trivially.  The
non-trivial measured content is (a) the QUANTIFIED Cauchy/contraction
profiles per fixed f on the frozen eps ladder, (b) their stability
along the X ladder, and (c) the near-null spectral structure that
would become the kernel of the limit object.  No X -> infinity claim
is made; the diagonal strategy (fixed f, then X, then eps) is
assessed, not proven.

FROZEN CONSTRUCTION (all reused verbatim, none invented): tower lag
vector and channels from simpler_schur_recursion_probe (DGRID = 1/64,
channel_masks, continuum_lags, atom_channel_lags) exactly as in
handoff_compat_eps3_probe.build_tower; local battery = module-1
handoff_bulk_probe.battery (4 boxes + 3 hats per R, l2-normalized),
R in {1, 2}; interleaved prefix ladders LAD_A = 256..816 step 16,
LAD_B = LAD_A + 8, M_TOP = 824 (deepest step-8-aligned rung under the
table cap 825); rate fit = handoff_bulk_probe.fit_rate verbatim;
resolvent rows Ward-checked against handoff_tail_weil_probe.
compat_rows verbatim; Epstein atoms from epstein_firewall_probe
(read-only); scramble via v563_paper2_readouts.atom_lags_at.

FROZEN GRIDS AND BARS (all fixed here BEFORE the first run):
  eps ladder (decadic)  EPS_LADDER = 1e-1, 1e-2, 1e-3, 1e-4, 1e-5.
  gated eps for Q1      EPS_GATED  = 1e-1, 1e-2, 1e-3 (the documented
                        cells); 1e-4 and 1e-5 are REPORTED outlook
                        cells, never gated (the wall side).
  spectral rung set     QLAD = 256..800 step 32, plus 824 (19 rungs).
  near-null threshold   THR_NULL = 1e-4 (between the top-rung PD
                        margin 8.3e-6 and the first eps decade);
                        THR_DEEP = 1e-5 reported.
  Q1 bars: rate b_Y >= 0.10 per X unit; |b_Y - b_G(same run)| <= 1e-3
      (the predeclared algebra, allowed float-cancellation slack);
      X-monotonicity certificate max diag increment of E_Y <= 1e-8;
      sandwich guard -1e-9 <= diag(E_Y) <= 1 + 1e-9 on every rung of
      every eps; med5 / b2 reported per cell (not gated).
  Q2 bars (branch (i) OR (ii), realized branch reported):
      (i)  stable object: near-null count spread over the last 5 QLAD
           rungs <= 3 AND mean consecutive subspace alignment over the
           last 4 rung pairs >= 0.80 (alignment = ||V_new^T
           pad(V_old)||_F^2 / dim_old in [0, 1]);
      (ii) stable battery weight: total near-null battery weight
           rel spread (max-min)/max over the last 5 QLAD rungs <= 0.5.
  Q3 bars (branch (i) OR (ii), realized branch reported):
      (i)  vanishing: max over the 14 battery functions of the
           near-null weight q_f = sum_{l <= THR_NULL} <v, f>^2 at
           M_TOP <= 1e-3;
      (ii) admissible stable null pairing: every f with q_f > 1e-3
           has rel spread of q_f over the last 5 QLAD rungs <= 0.5.
      The full 14-function pairing table is printed either way.
  Q4 bars (per fixed f at M_TOP; uniformity across f NOT required):
      monotone certificate min eps-increment of <f, Y_eps f> >=
      -1e-12 on EVERY QLAD rung; deficit contraction
      (1 - y(1e-5)) / (1 - y(1e-1)) <= 0.25 at M_TOP; the full
      increment/ratio profiles and their X-stability (M = 800 vs 824)
      are REPORTED, not gated.
  Guards: AST firewall; SHA-256 freeze of battery bytes + every
      ladder + eps grid + threshold + bar BEFORE any comb data load;
      reach census (824 <= floor(64 ln ATOM_MAX) = 825, sieve cover);
      comb consistency rel dev <= 1e-12; resolvent-identity Ward
      max |A_M G^eps F - (F - eps G^eps F)| / max|F| <= 1e-8
      (verifies Y f = A (A+eps)^{-1} f = f - eps G^eps f in floats);
      verbatim-machinery Ward my E_G == handoff_tail_weil_probe.
      compat_rows at eps = 1e-2 rel <= 1e-10; spectral-vs-Cholesky
      Ward on diag(E_Y) at M_TOP rel <= 1e-8; scale audit: every
      Y-defect scale in [1e-3, 1.5] (an O(1) scale -- the numeric
      form of "no 1/eps normalization entered any gate"); real-data
      operator sandwich at M = 512: all Yosida eigenvalues in
      [-1e-9, 1 + 1e-9] for every eps.
KILL (frozen): if any gate had to be normalized by ||(A + eps I)^{-1}||
(a 1/eps-sized bound) or needed a positive lower eigenvalue bound on
A, the wall sits in the assumption again -- verdict DEAD.  Structural
audit: every gated quantity above is a bounded quadratic form of
Y_eps (|.| <= 1 by the sandwich), a ratio of two such, or a rate fit
on their logs with an O(1) scale; the scale-audit guard measures this.

CONTROLS (mandatory, must fire; spectral map at M_CTRL = 512, frozen):
  CS position scramble (positions uniform in (0.5, 2 alpha), masses
  kept, seed 7) and CE Epstein x^2 + 5y^2 atoms (Lambda_E via lattice
  count + Dirichlet division, epstein_firewall_probe read-only, tower
  cap M = 640, control prefix 512).  For indefinite A the spectral map
  g_eps(l) = l/(l + eps) leaves [0, 1]: FIRE = [exists eps in
  EPS_LADDER with min g < -0.01 or max g > 1.01 (sandwich break)] OR
  [battery eps-monotonicity violation: some increment < -1e-6] OR
  [|l + eps| < 1e-12 for some eigenvalue (singular Yosida)].  A
  control that keeps the sandwich, stays monotone, and is nonsingular
  has spuriously converged: the run is DEAD.

VERDICT ENUM (frozen): YOSIDA-KERNEL-SAFE = all guards pass AND both
controls fire AND Q1 (all 6 gated cells + mono + sandwich) AND Q2 AND
Q3 AND Q4 all decided positively.  YOSIDA-PARTIAL = guards + controls
ok AND >= 2 of the four questions pass (the open ones are named with
their exact failing numbers).  YOSIDA-DEAD = any guard fails, any
control spuriously converges, <= 1 question passes, or the KILL
trigger (a 1/eps bound or positive-margin assumption inside a gate).

STOP-LIST (binding, inherited): no bare A^{-1}; no positive-margin
assumptions; no fits inside proof-grade statements (measured rates
reported as measured); no Riemann zeros; no domino variants, no layer
positivizations, no norm triangles, no perturbation theory.  NO RH
claim.  This probe writes no files.  Runtime minutes.

RESULTS (2026-08-04, first and only preregistered run, 1.7 s; GATES
9/10, GUARDS+CONTROLS 12/12, verdict YOSIDA-PARTIAL -- Q1, Q2, Q4
decided positively, Q3 OPEN as preregistered):
  *  Q1 PASS 6/6 + mono -- the handoff observable IS formulable
     entirely through Y_eps: b_Y = 0.239/0.185 (eps 1e-1),
     0.259/0.149 (1e-2), 0.178/0.186 (1e-3) for R = 1/2, reproducing
     the resolvent rates on the same geometry to |b_Y - b_G| <=
     1.0e-13 (the predeclared algebra, verified in floats, not
     assumed); SANDWICH 0.0028 <= diag(E_Y) <= 1 - 6.8e-3 over all
     360 (eps, rung) evaluations; X-MONOTONE certificate: max diag
     increment -8.3e-8 (strictly decreasing); defect scales
     0.012..0.983, all O(1).  OUTLOOK (reported, never gated): the
     wall reappears as RATE COLLAPSE two decades below the gated
     cells -- eps = 1e-4: b_Y = 0.127/0.058 (R = 2 under the 0.10
     bar, b2 = -0.026); eps = 1e-5: b_Y = 0.094/0.008 with med5 =
     1.52/1.08 (the ladder no longer falls).
  *  MEASURED CORRECTION of a predeclared expectation (honesty): the
     Y-defect amplitude does NOT shrink linearly in eps.  Final-rung
     Y-defect: R = 1: 3.9e-3 -> 4.4e-5 (~ eps^0.49 over 4 decades);
     R = 2: 5.0e-3 -> 5.9e-4 (~ eps^0.23).  The resolvent defect
     grows toward the spectral edge and eats most of the eps factor;
     the amplitude still falls monotonely in eps on the fixed O(1)
     scale, but sublinearly -- the wall is weakened, not erased, and
     its carrier is exactly the Q3 weight below.
  *  Q2 PASS branch (i) AND (ii) -- the kernel part IS explicitly
     identifiable as a stable object: near-null count (lam <= 1e-4)
     = 1 -> 5 over QLAD with last-5 spread 1 <= 3; consecutive
     subspace alignment 0.961..0.998, mean of last 4 = 0.988 >=
     0.80; a SINGLE deep mode (lam <= 1e-5) appears at M = 736 and
     persists to the top.  Branch (ii) is thin: total near-null
     battery weight 1.67..3.17 on the last 5 rungs, rel spread 0.473
     vs bar 0.5.  PD margins (reported, never gated): 5.289e-5
     (M 256) -> 8.265e-6 (M 824).
  *  Q3 FAIL both branches -- THE central honest finding: the
     near-null pairing neither vanishes nor is stable on the
     reachable surface.  ALL 14 battery functions pair above 1e-3;
     max q_f = 4.46e-1 (R2:box[0,R]; the battery parks up to ~45% of
     its mass on the near-null subspace), per-f rel spreads
     0.309..0.711 (worst R1:hat(R/4,R/4) = 0.711 > 0.5).  This
     growing/fluctuating weight is precisely what stalls the
     small-eps handoff rate in the Q1 outlook cells: the two
     failures are one phenomenon seen from two sides.
  *  Q4 PASS 14/14 -- for every fixed battery f the eps -> 0 limit
     goes through with measured certificates: monotone on every QLAD
     rung (min eps-increment +2.2e-2 >= -1e-12), deficit contraction
     0.0106..0.1079 <= 0.25 over four decades; median Cauchy-ratio
     profile 3.08/1.43/0.46 (increments PEAK at the middle decades
     -- the spectral mass of the battery sits at lam ~ 1e-3..1e-4 --
     and contract only on the last step).  HONEST LIMIT: the
     last-step contraction leans on the finite-M spectral floor
     (lambda_min = 8.3e-6 < 1e-5); the increment profile is X-stable
     to 1.5e-3 (M 800 vs 824, reported), but no X -> infinity claim
     follows.
  *  CONTROLS both fire: CS scramble lambda_min = -1.10e+3, 206/512
     negative eigenvalues, sandwich break max g = 5.1, 4 battery
     monotonicity violations (worst -8.1e-3); CE Epstein (496
     negative atom sites) lambda_min = -3.32e+1, 189/512 negative,
     min g = -2.5, max g = 23, 56 violations (worst -5.1e-2).
     Indefinite data destroys exactly the sandwich/monotonicity
     certificates the real tower satisfies.
  *  KILL audit PASS: no gate was normalized by ||(A + eps I)^{-1}||
     or a PD margin; every gated quantity is a bounded Y-form
     statistic on an O(1) scale (audit band held: 0.012..0.983);
     the PD of the real tower is measured output (G1.2 sandwich),
     never an assumption inside a gate.
  *  HONEST STATEMENT (does the kernel-safe route carry the diagonal
     strategy fixed f -> X -> eps?): PARTIALLY.  (fixed f) Every
     battery function has a monotone, contraction-certified
     eps-limit at every reachable window -- Q4.  (then X) The
     Y-observable is monotone decreasing in X and carries the
     documented falling handoff rates at the documented eps -- Q1;
     the near-null subspace converges to a stable identified object
     -- Q2.  (then eps) The joint corner (small eps AND deep X) is
     carried ONLY IF the battery null-pairing q_f(X) converges along
     the tower -- and it does NOT yet (Q3): the route BREAKS exactly
     there.  What the Yosida transform achieves: the wall is
     relocated from a forbidden instrument (a 1/eps resolvent bound
     / positive-margin assumption) into a bounded, well-posed object
     (q_f in [0, 1], the pairing of the frozen battery with the
     identified near-kernel), whose X-convergence is now THE
     remaining question.  Exact zero modes stay admissible (Ihara
     lesson); nothing here needs A > 0.  NO RH claim, no X ->
     infinity claim; deeper towers or a battery orthogonalized
     against the identified near-kernel are the two named next
     probes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/yosida_handoff_probe.py

PART 2 -- yosida_qf_convergence_probe.py (docstring verbatim):
GLOBAL-HANDOFF-OFFENSIVE -- the Q3 follow-up decider: does the
battery near-kernel pairing weight q_f(X) converge along the tower?
yosida_qf_convergence_probe (strand D2, kernel-safe epsilon limit;
intended promotion target v763b, extension of the v763 candidate).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  yosida_handoff_probe -- YOSIDA-PARTIAL (9/10 gates, 12/12
     guards+controls): Q1 (bounded Yosida formulation carries the
     handoff rates, |b_Y - b_G| <= 1.0e-13, sandwich verified), Q2
     (near-kernel identifiable and stable: alignment mean 0.988, one
     persistent deep mode), Q4 (fixed-f monotone eps-limits,
     contraction 0.011..0.108) all POSITIVE.  Q3 FAILED both frozen
     branches: ALL 14 battery functions pair above 1e-3, max q_f =
     4.46e-1 (R2:box[0,R] parks ~45% of its mass on the near-kernel),
     per-f rel spreads 0.309..0.711 over the last 5 QLAD rungs (worst
     R1:hat(R/4,R/4) = 0.711 > bar 0.5).  The wall now lives in
     exactly ONE bounded quantity: the X-convergence of q_f.
  *  handoff_compat_eps3_probe -- the oscillation lesson reused here:
     single-endpoint gates break on atom-burst rungs; robust cell
     statistics are 5-rung medians plus a fitted second-half slope.
  *  Known table facts: the internal generator capped the tower at
     ATOM_MAX = 400000 (u <= 12.899, M <= 825); all parent probes
     used M_TOP = 824.  PD margins fall 5.289e-5 (M 256) -> 8.265e-6
     (M 824) -- measured, never gated.

SINGLE QUESTION (preregistered): does q_f(X) -- the pairing weight of
each frozen battery function with the identified near-kernel of the
window operator -- converge per function along a DEEPER AND DENSER
tower, so that the kernel contribution is an admissible exact null
mode in the limit (Q3 closes positively), or does it fail at honest
maximal depth (Q3 closes negatively on the reachable surface)?

EXTENDED COMB (Candidate A legitimacy, declared): the atom table is
internal, deterministic, target-free source data -- the von Mangoldt
comb from a plain sieve (core.von_mangoldt_table), exactly the
deployed generator at a larger cap.  Extending it loads NO new
information class.  New frozen cap ATOM_MAX_EXT = 4,000,000
(u <= ln 4e6 = 15.2018); on the same dyadic grid D = 1/64 the
absolute window cap is M_CAP_EXT = floor(64 ln 4e6) = 972
(X = 15.1875); M_TOP_EXT = 972 is frozen as the deepest rung (it is
step-4 aligned with 824: 972 = 824 + 37*4).  Sieve cover:
exp(15.1875) + 2 = 3943224 <= 4000000.  Guards below tie the
extension to the deployed table (exact overlap), to the parent tower
(float-exact prefix), and to the Chebyshev envelope (extended-range
integrity).

CANDIDATE A -- DEEPER AND DENSER TOWER (default adjudication):
  spectral ladders (all frozen):
    QLAD_PAR = 256..800 step 32, plus 824  (19 rungs; the parent
        grid, recomputed for the parent-vs-extended table and a
        reproduction Ward -- never re-gated);
    EXT_LAD  = 824..972 step 4             (38 rungs; the densest
        honest rung spacing at the top plus the deeper extension;
        ALL Candidate-A gates live on EXT_LAD only).
  near-null threshold policy (parent policy, frozen): gated threshold
    THR_NULL = 1e-4; robustness REPORT (never gated) at the 3 frozen
    thresholds THR_ROB = (3e-4, 1e-4, 3e-5).
  per-function statistic on EXT_LAD (oscillation-aware, the
  compat-eps3 lesson; N_MED = 5):
    MID5  = EXT_LAD[17:22]  (M = 892..908, X ~ 13.94..14.19),
    LAST5 = EXT_LAD[33:38]  (M = 956..972, X ~ 14.94..15.19),
    drift_f = |median(q_f over LAST5) - median(q_f over MID5)|
              / max(medians, 1e-12),
    rel_slope_f = |least-squares linear slope of q_f vs X over the
              second half EXT_LAD[19:]| / max(mean q_f there, 1e-12).
  GATES (all frozen BEFORE the first run):
    A1 drift:      drift_f <= 0.15 for EVERY one of the 14 functions
                   at THR_NULL;
    A2 slope:      rel_slope_f <= 0.15 per X unit for EVERY function
                   at THR_NULL;
    A3 stability:  the near-kernel subspace itself stays stable under
                   the extension -- near-null count spread over LAST5
                   <= 3 AND mean consecutive subspace alignment over
                   the last 4 EXT rung pairs >= 0.80 (alignment =
                   ||V_new^T pad(V_old)||_F^2 / dim_old, parent
                   formula verbatim).
  A PASSES iff A1 and A2 and A3.

CANDIDATE B -- NEAR-KERNEL-ORTHOGONALIZED BATTERY (consulted if and
only if Candidate A fails at least one of A1/A2/A3; at most ONE
iteration, fully specified here BEFORE the first run):
  construction (source-side only, no target data): freeze the
  near-kernel basis V_null of the DEEPEST window (M = 972, THR_NULL)
  once.  For each battery function f with support [0, nR] use the
  SUPPORT-RESTRICTED orthogonalization g = f - W (W^T W)^+ W^T f with
  W = V_null[:nR, :] and pseudo-inverse rcond B_RCOND = 1e-10: g
  keeps the battery support (every parent evaluation stays verbatim
  legitimate) and has EXACTLY zero pairing with the frozen deepest
  near-kernel; g is l2-renormalized and the 14-function orthogonalized
  battery is SHA-256 frozen before any B evaluation.
  GATES (frozen):
    B1 substance:  retained norm^2 ||g||^2 >= 0.30 for every f before
                   renormalization (else the function was mostly
                   kernel and the correction is cosmetic);
    B2 rates:      re-run the parent Q1 machinery verbatim
                   (yosida_handoff_probe.yosida_pass + defect_rows on
                   LAD_A = 256..816 step 16, LAD_B = A + 8) on the
                   orthogonalized battery: on all 6 gated cells
                   (eps = 1e-1, 1e-2, 1e-3; R = 1, 2) b_Y >= 0.10 AND
                   |b_Y - b_parent| <= 0.10 with the parent's frozen
                   run values b_parent = 0.239/0.185, 0.259/0.149,
                   0.178/0.186 (R = 1 / R = 2);
    B3 residual:   residual q_f of the orthogonalized battery at
                   THR_NULL on the LAST5 extension rungs: max <= 5e-2
                   AND every f with residual > 1e-3 has rel spread
                   (max-min)/max <= 0.5 there (stable profile);
    B4 limits:     parent Q4 gates on the orthogonalized battery:
                   monotone certificate min eps-increment >= -1e-12
                   on EVERY EXT_LAD rung; deficit contraction
                   (1 - y(1e-5)) / (1 - y(1e-1)) <= 0.25 at M = 972.
  B PASSES iff B1 and B2 and B3 and B4.

GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (no prime-table loaders, no zeta zeros);
  G0.2 SHA-256 freeze of battery bytes + both ladders + thresholds +
       every bar + the extended-comb specification string BEFORE any
       comb data is built in this probe (the module import of the
       deployed 400000-table is declared, as in every parent);
  G0.3 reach census: M_TOP_EXT <= M_CAP_EXT = floor(64 ln ATOM_MAX_EXT)
       and exp(X_top) + 2 <= ATOM_MAX_EXT; runtime cap 600 s
       predeclared (report; exceeding it invalidates the run);
  G1.1 extended-table overlap: the extended von Mangoldt table equals
       the deployed core table EXACTLY on [0, 400000] (max abs dev 0);
  G1.2 extended-range Chebyshev envelope: kappa over all jump points
       of psi(x)/x in [100, 4e6] <= KAPPA_REF + 1e-6 (the deployed
       envelope does not degrade on the extension);
  G1.3 parent tower comb consistency verbatim (zeta-free Gauss double
       sieve == deployed masses, rel dev <= 1e-12, at M_TOP = 824);
  G1.4 prefix Ward: the extended tower's leading 824 x 824 block
       equals the parent tower to max abs dev <= 1e-12 (tent assembly
       is 1-cell local: atoms beyond X_top(824) cannot touch the
       prefix -- measured, not assumed);
  G1.5 parent reproduction Ward: max q_f at M = 824 reproduces the
       parent's frozen 4.46e-1 to 2e-3 AND the worst parent last-5
       rel spread reproduces 0.711 to 2e-3 (same construction, same
       numbers -- machinery is verbatim);
  G1.6 real-data operator sandwich (measured, PD never assumed): all
       Yosida eigenvalues in [-1e-9, 1 + 1e-9] for every eps of the
       parent ladder at M = 512 AND at M = 972;
  G1.7 boundedness/KILL audit: every q_f in [-1e-12, 1 + 1e-9] (a
       bounded quadratic form of a unit vector -- no 1/eps
       normalization, no PD-margin assumption enters any gate);
  G2.x (B only) resolvent-identity Ward of the verbatim Yosida pass
       <= 1e-8.

CONTROLS (mandatory, must fire; frozen fire rule = parent's
control_yosida verbatim at M_CTRL = 512): CS position scramble
(positions uniform in (0.5, 2 alpha_ext), masses kept, seed 7, on the
EXTENDED comb) and CE Epstein x^2 + 5y^2 atoms (Lambda_E via lattice
count + Dirichlet division, epstein_firewall_probe read-only, tower
cap M = 640).  For indefinite A the near-kernel/pairing construction
must break measurably: FIRE = sandwich break (g outside
[-0.01, 1.01]) OR battery eps-monotonicity violation (< -1e-6) OR
singular Yosida (|lam + eps| < 1e-12); the negative-spectrum census
(count lam < -THR_NULL, destroying any kernel-candidate reading) is
printed with each control.  A control that keeps the sandwich has
spuriously converged: the run is DEAD.

VERDICT ENUM (frozen):
  QF-CONVERGES          = guards + controls ok AND Candidate A passes
      (q_f limits exist per function on the reachable surface, the
      kernel contribution is an admissible exact null mode -- Q3
      closes positively; the diagonal sequence fixed f -> X -> eps is
      buildable at this depth).
  QF-ORTHOGONAL-CARRIES = guards + controls ok AND A fails AND B
      passes (the diagonal strategy carries on the near-kernel-
      orthogonalized battery -- Q3 positive in the corrected form,
      honestly labeled as a battery correction, the null-pairing is
      an inessential battery artifact).
  QF-DEAD               = any guard fails, any control spuriously
      converges, OR both candidates fail at honest maximal depth:
      the wall persists in q_f, the diagonal route cannot take
      eps -> 0 at deep X with this battery class, and Q3 closes
      negatively on the reachable surface.

STOP-LIST (binding, inherited): no bare A^{-1}; no PD-margin
assumptions or 1/eps bounds in any gate; no target data anywhere in
the construction (the near-kernel comes from the source-side window
operator only); no fits inside gates (the slope statistic is a
declared gate statistic on a bounded quantity, not a proof-grade
claim); no Riemann zeros; NO RH claim.  This probe writes no files.
Runtime cap 600 s predeclared.

RESULTS (2026-08-04, first and only preregistered run, 4.6 s; GATES
7/12, GUARDS+CONTROLS 14/14, iteration SPENT (Candidate B consulted),
verdict QF-DEAD -- Q3 closes NEGATIVELY on the reachable surface):
  *  EXTENSION VALID: ka = 279849 atoms to e^15.1875 (vs 33276 at
     the parent cap); comb overlap exact (max abs dev 0.0);
     Chebyshev envelope kappa = 0.038821 unchanged on [100, 4e6];
     prefix Ward max abs dev 2.0e-14 (the deeper tower contains the
     parent tower at machine level); parent reproduction Ward: max
     q_f(824) = 0.4459 (dev 1.3e-4 vs frozen 0.446), worst parent
     spread 0.7106 (dev 4.0e-4 vs frozen 0.711).  PD margins
     (measured, never gated): 5.289e-5 (M 256) -> 8.265e-6 (M 824)
     -> 6.459e-6 (M 972); sandwich holds at both ladder ends.
  *  CANDIDATE A FAILS A1 + A2 (A3 passes) -- q_f does NOT converge
     at honest maximal depth: 12 of 14 functions break BOTH bars;
     worst drift 0.5636 and worst rel slope 0.8061/X (both
     R1:hat(R/4,R/4)) vs bars 0.15; only R2:box[R/2,R] (0.093,
     0.108) and R2:hat(3R/4,R/4) (0.090, 0.103) pass.  The FORM of
     the failure is new and honest: on the extension q_f FALLS
     steeply (med5 mid -> last, e.g. R1:box[0,R] 0.168 -> 0.085;
     R2:box[0,R] 0.591 -> 0.453) -- the pairing is still in fast
     motion, not oscillating around a limit.  A 6th near-null mode
     enters at M = 888 (count 5 -> 6, then constant over 22 rungs)
     and its battery weight then drains; the dense-grid last-5
     spreads are small (0.038..0.102 vs parent coarse 0.309..0.711)
     but the level keeps sliding: non-Cauchy at the frozen bars.
  *  A3 PASS -- the near-kernel OBJECT stays stable under the
     extension: count spread last 5 = 0, consecutive alignment min
     0.999623, mean last 4 = 0.99969; single deep mode (lam <= 1e-5)
     persists at count 1 on every extension rung.  The object
     converges; its battery pairing weight does not.
  *  THRESHOLD ROBUSTNESS (reported, never gated): worst
     drift/slope = 0.231/0.490 (thr 3e-4, nn = 9), 0.564/0.806
     (thr 1e-4, nn = 6), 0.323/0.398 (thr 3e-5, nn = 2) -- the
     failure is NOT a threshold artifact (all three break the bars,
     same worst function).
  *  CANDIDATE B FAILS B1 + B2 (B3, B4 pass) -- the null-pairing is
     STRUCTURAL, not a removable battery artifact: (B1) the deepest
     near-kernel restricted to the battery support nearly CONTAINS
     the battery -- retained norm^2 = 0.0007 (R1:hat(R/2,R/2)) ..
     0.107 (R2:box[0,R/2]), i.e. 89..99.9% of every battery
     function lies in the span of 6 restricted near-null modes, vs
     floor 0.30; (B2) the surviving 0.1..10% remnant does NOT carry
     the parent rates on R = 1: b_Y = 0.246/0.230 (eps 1e-1, pass),
     0.117/0.156 (1e-2, R=1 off-band |diff| = 0.142), 0.060/0.152
     (1e-3, R=1 under the 0.10 floor and off-band) -- 4/6 cells
     pass, both failures on R = 1.  (B3/B4 pass trivially: residual
     q_f <= 1.9e-6, contraction 0.0004..0.0025 -- AFTER removing
     the near-kernel almost nothing with spectral weight near zero
     is left, which is the same finding from the other side.)
  *  CONTROLS both fire: CS scramble (extended comb, 279849 atoms)
     lambda_min = -3.33e+3, 246/512 negative eigenvalues, sandwich
     break min g = -0.42 / max g = 1.5, 15 monotonicity violations;
     CE Epstein (496 negative atom sites) lambda_min = -3.32e+1,
     189/512 negative, min g = -2.5, max g = 23, 56 violations.
     Indefinite data destroys the kernel-candidate reading.
  *  KILL audit PASS: every gated q_f in [5.9e-3, 0.614], bounded
     quadratic forms of unit vectors; no 1/eps bound, no PD-margin
     assumption in any gate; runtime 4.6 s <= cap 600 s.
  *  GATE-3 CONSEQUENCE (stated plainly): the wall PERSISTS in q_f
     at honest maximal depth (X = 15.1875, 4x parent rung density,
     +2.3 X units) and it SURVIVES near-kernel orthogonalization:
     the battery class is essentially subordinate to the near-kernel
     (up to 99.9% of its mass), so removing the pairing removes the
     observable content on R = 1 with it.  The diagonal route
     (fixed f -> X -> eps) CANNOT take eps -> 0 at deep X with this
     battery class -- Q3 closes NEGATIVELY on the reachable surface.
     What survives positively (parent findings, untouched): the
     bounded Yosida formulation (Q1), the convergent near-kernel
     object (Q2, re-confirmed here by A3 at greater depth), the
     fixed-f monotone limits (Q4).  Honest next surfaces (named, not
     probed here): a battery class NOT subordinate to the near-kernel
     (e.g. spectrally localized away from it), or a still deeper
     table to see whether the post-M-888 drainage settles.  NO RH
     claim, no X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/yosida_qf_convergence_probe.py
"""

# ==========================================================================
# PART 1 -- yosida_handoff_probe.py (verbatim; imports promoted)
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
import v768_handoff_tail_weil as htw  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
M_CAP = int(math.floor(math.log(core.ATOM_MAX) / D))   # 825
M_TOP = 824                          # deepest step-8-aligned rung
LAD_A = list(range(256, 817, 16))    # 36 rungs, X = 4.0 .. 12.75
LAD_OFF = 8                          # ladder B = A + 8 cells
QLAD = list(range(256, 801, 32)) + [824]   # 19 spectral rungs

R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
EPS_LADDER = (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5)  # decadic
EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)  # documented cells (gated)
EPS_WREF = 1.0e-2                    # verbatim-machinery Ward eps

THR_NULL = 1.0e-4                    # near-null threshold (Q2/Q3)
THR_DEEP = 1.0e-5                    # reported deep threshold
N_MED = 5                            # median block (reported)

Q1_RATE = 0.10                       # b_Y bar per X unit
Q1_MATCH = 1.0e-3                    # |b_Y - b_G| same-run bar
Q1_XMONO = 1.0e-8                    # X-monotone diag certificate
SANDWICH_TOL = 1.0e-9                # 0 <= diag(E_Y) <= 1 slack
SCALE_LO, SCALE_HI = 1.0e-3, 1.5     # O(1) scale audit band (KILL)
Q2_NSPREAD = 3                       # near-null count spread, last 5
Q2_ALIGN = 0.80                      # mean subspace alignment, last 4
Q2_WSPREAD = 0.5                     # battery weight rel spread
Q3_VANISH = 1.0e-3                   # vanishing-pairing bar
Q3_STAB = 0.5                        # stable-pairing rel spread bar
Q4_MONO = -1.0e-12                   # eps-monotone certificate floor
Q4_CONTRACT = 0.25                   # deficit contraction bar
WARD_RES = 1.0e-8                    # resolvent-identity Ward
WARD_REF = 1.0e-10                   # verbatim compat_rows Ward
WARD_SPEC = 1.0e-8                   # spectral vs Cholesky Ward

SBRK = 0.01                          # control sandwich break bar
CTRL_MONO = 1.0e-6                   # control monotonicity break bar
POLE_TOL = 1.0e-12                   # singular Yosida detection
M_CTRL = 512                         # control spectral rung
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7
COMB_DEV_BAR = 1.0e-12

# documented parent rates for the REPORTED comparison (same geometry:
# handoff_compat_eps3_probe; task-quoted mixed-source values in
# parentheses in the printout)
PARENT_B = {1.0e-1: (0.239, 0.185), 1.0e-2: (0.259, 0.149),
            1.0e-3: (0.178, 0.186)}

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # Q1..Q4 gates: feed the verdict only


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
    """Battery bytes + every ladder + eps grid + threshold + bar,
    SHA-256 frozen BEFORE any comb/deployed data is loaded."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("yosida-handoff spec: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s; LAD_A=%d..%d step 16, "
                "LAD_B=A+%d, M_TOP=%d (cap %d); QLAD=%s; "
                "eps ladder=%s gated=%s; thr null=%g deep=%g; "
                "Q1: b>=%g match<=%g xmono<=%g sandwich<=%g "
                "scale=[%g,%g]; Q2: nspread<=%d align>=%g wspread<=%g;"
                " Q3: vanish<=%g stab<=%g; Q4: mono>=%g contract<=%g;"
                " wards res<=%g ref<=%g spec<=%g; controls: sbrk=%g "
                "mono=%g pole=%g M=%d seed=%d"
                % (D, R_BAT, LAD_A[0], LAD_A[-1], LAD_OFF, M_TOP,
                   M_CAP, QLAD, EPS_LADDER, EPS_GATED, THR_NULL,
                   THR_DEEP, Q1_RATE, Q1_MATCH, Q1_XMONO,
                   SANDWICH_TOL, SCALE_LO, SCALE_HI, Q2_NSPREAD,
                   Q2_ALIGN, Q2_WSPREAD, Q3_VANISH, Q3_STAB, Q4_MONO,
                   Q4_CONTRACT, WARD_RES, WARD_REF, WARD_SPEC, SBRK,
                   CTRL_MONO, POLE_TOL, M_CTRL, SEED)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_all(bats, M):
    """All 14 battery functions zero-padded to window size M."""
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(M)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


# ------------------------------------------------ tower (verbatim)
def build_tower():
    alpha_full = 0.5 * M_TOP * D
    ka, masks, dev_m = srp.channel_masks(alpha_full)
    check("G1.1 tower comb consistency (zeta-free Gauss double sieve "
          "== deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha_full))
    c_cont = srp.continuum_lags(M_TOP)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(alpha_full, M_TOP,
                                                masks[cnl])
    return sla.toeplitz(c_full[:M_TOP]), c_cont, alpha_full, ka


# ================================================== Q1: Y-form handoff
def yosida_pass(T, bats):
    """One Cholesky per (eps, M); from the SAME solve both the
    resolvent Gram E_G and the Yosida Gram E_Y = F^T (F - eps G F)
    are assembled -- Y f is computed as f - eps G^eps f and the
    resolvent identity A (G F) = F - eps G F is Ward-checked."""
    ladB = [m + LAD_OFF for m in LAD_A]
    sizes = sorted(set(LAD_A) | set(ladB))
    Fms = {R: np.stack([v for _n, v in bats[R]], axis=1)
           for R in R_BAT}
    res = {}
    for eps in EPS_LADDER:
        EG, EY = {}, {}
        ward = 0.0
        mid = sizes[len(sizes) // 2]
        for M in sizes:
            cf = sla.cho_factor(T[:M, :M] + eps * np.eye(M))
            perG, perY = {}, {}
            for R in R_BAT:
                nR = int(round(R / D))
                F = np.zeros((M, Fms[R].shape[1]))
                F[:nR] = Fms[R]
                GF = sla.cho_solve(cf, F)
                YF = F - eps * GF
                perG[R] = F.T @ GF
                EYm = F.T @ YF
                perY[R] = 0.5 * (EYm + EYm.T)
                if M == mid:
                    r = float(np.max(np.abs(T[:M, :M] @ GF - YF))
                              / max(np.max(np.abs(F)), 1.0e-300))
                    ward = max(ward, r)
            EG[M], EY[M] = perG, perY
        res[eps] = dict(EG=EG, EY=EY, ward=ward)
    return res, sizes, ladB


def defect_rows(E, ladB, R):
    d0 = np.diag(E[LAD_A[0]][R])
    scale = float(np.sqrt(np.max(d0) * np.min(d0)))
    rows = [dict(X=Ma * D, XmR=Ma * D - R,
                 mx=float(np.max(np.abs(E[Mb][R] - E[Ma][R])))
                 / scale)
            for Ma, Mb in zip(LAD_A, ladB)]
    return rows, scale


def stat_of(rows):
    mxs = [r["mx"] for r in rows]
    b, resid = hbp.fit_rate(rows)
    b2, _r2 = hbp.fit_rate(rows[len(rows) // 2:])
    med = float(np.median(mxs[-N_MED:])
                / max(np.median(mxs[:N_MED]), 1.0e-300))
    return b, resid, b2, med, mxs


def q1_block(T, bats):
    print("\n-- Q1: the handoff observable through Y_eps alone "
          "(bounded, O(1) scale)")
    res, sizes, ladB = yosida_pass(T, bats)

    # guards on the pass
    wmax = max(res[eps]["ward"] for eps in EPS_LADDER)
    check("G2.1 resolvent-identity Ward A(G^eps F) = F - eps G^eps F "
          "(mid rung, every eps) <= %.0e" % WARD_RES, wmax <= WARD_RES,
          "max rel %.1e" % wmax)
    rows_ref, E_ref = htw.compat_rows(T, LAD_A, ladB, EPS_WREF, bats)
    dref = 0.0
    for M in sorted(set(LAD_A) | set(ladB)):
        for R in R_BAT:
            num = float(np.max(np.abs(E_ref[M][R]
                                      - res[EPS_WREF]["EG"][M][R])))
            dref = max(dref, num / max(
                float(np.max(np.abs(E_ref[M][R]))), 1.0e-300))
    check("G2.2 verbatim-machinery Ward: E_G(this probe) == "
          "handoff_tail_weil_probe.compat_rows at eps = %g, rel <= "
          "%.0e" % (EPS_WREF, WARD_REF), dref <= WARD_REF,
          "max rel %.1e" % dref)

    # sandwich + X-monotone certificates over every eps and rung
    dmin, dmax, xmono = np.inf, -np.inf, -np.inf
    for eps in EPS_LADDER:
        for R in R_BAT:
            prev = None
            for M in sizes:
                dg = np.diag(res[eps]["EY"][M][R])
                dmin = min(dmin, float(np.min(dg)))
                dmax = max(dmax, float(np.max(dg)))
                if prev is not None:
                    xmono = max(xmono, float(np.max(dg - prev)))
                prev = dg
    check("G2.3 SANDWICH on real data: %.4f <= diag(E_Y) <= 1 - "
          "%.1e over all %d (eps, rung) evaluations (bars -%.0e / "
          "1+%.0e)" % (dmin, 1.0 - dmax, len(EPS_LADDER) * len(sizes),
                       SANDWICH_TOL, SANDWICH_TOL),
          dmin >= -SANDWICH_TOL and dmax <= 1.0 + SANDWICH_TOL)
    ok_xm = gate("Q1.mono X-MONOTONE certificate: diag(E_Y) is "
                 "non-increasing along the window ladder (PSD Schur "
                 "increments of E_G); max positive increment %.1e <= "
                 "%.0e, over every eps" % (xmono, Q1_XMONO),
                 xmono <= Q1_XMONO)

    # gated cells + reported outlook cells
    cells_ok = ok_xm
    scale_lo, scale_hi = np.inf, -np.inf
    for eps in EPS_LADDER:
        gated = eps in EPS_GATED
        for R in R_BAT:
            rowsY, scY = defect_rows(res[eps]["EY"], ladB, R)
            rowsG, _scG = defect_rows(res[eps]["EG"], ladB, R)
            scale_lo, scale_hi = min(scale_lo, scY), max(scale_hi,
                                                         scY)
            bY, resid, b2, med, mxs = stat_of(rowsY)
            bG, _rg, _b2g, _mg, _mxg = stat_of(rowsG)
            det = ("b_Y = %.3f (>= %g; resid %.2f reported), "
                   "|b_Y - b_G| = %.1e (<= %g), b2 = %.3f, med%d = "
                   "%.3f, Y-defect %s ... %s over X-R = %.2f..%.2f, "
                   "scale %.3f"
                   % (bY, Q1_RATE, resid, abs(bY - bG), Q1_MATCH, b2,
                      N_MED, med,
                      ", ".join("%.1e" % v for v in mxs[:2]),
                      ", ".join("%.1e" % v for v in mxs[-2:]),
                      rowsY[0]["XmR"], rowsY[-1]["XmR"], scY))
            if gated:
                ok = bY >= Q1_RATE and abs(bY - bG) <= Q1_MATCH
                cells_ok &= gate("Q1.eps=%g,R=%g (parent b_G = %.3f)"
                                 % (eps, R, PARENT_B[eps][
                                     0 if R == 1.0 else 1]), ok, det)
            else:
                print("  Q1 OUTLOOK eps=%g,R=%g (reported, never "
                      "gated): %s" % (eps, R, det))
    check("K1 KILL/scale audit: every Y-defect scale in [%g, %g] "
          "(O(1), bounded by the sandwich -- no 1/eps normalization "
          "entered any gate)" % (SCALE_LO, SCALE_HI),
          scale_lo >= SCALE_LO and scale_hi <= SCALE_HI,
          "scales %.3f .. %.3f" % (scale_lo, scale_hi))

    # eps-scaling of the final-rung Y defect (reported)
    print("  Q1 report -- final-rung Y-defect vs eps (the amplitude "
          "side of the kernel-safe claim):")
    for R in R_BAT:
        line = []
        for eps in EPS_LADDER:
            rowsY, _s = defect_rows(res[eps]["EY"], ladB, R)
            line.append("eps=%g: %.1e" % (eps, rowsY[-1]["mx"]))
        print("    R=%g: %s" % (R, "  ".join(line)))
    return cells_ok, res


# ================================================== Q2/Q3: spectral
def spectral_block(T, bats):
    out = []
    for M in QLAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        Fall, names = battery_all(bats, M)
        wt = (V.T @ Fall) ** 2
        idx = np.nonzero(lam <= THR_NULL)[0]
        out.append(dict(M=M, lam=lam, wt=wt, Vn=V[:, idx],
                        nn=len(idx),
                        nn_deep=int(np.sum(lam <= THR_DEEP)),
                        qf=wt[idx].sum(axis=0)))
    return out, names


def y_profile(blk, eps_set):
    return np.stack([blk["wt"].T @ (blk["lam"] / (blk["lam"] + e))
                     for e in eps_set])   # (n_eps, 14)


def q2_block(spec):
    print("\n-- Q2: is the kernel part explicitly identifiable?")
    print("  PD margins (eps = 0, reported not gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[0]["lam"][0], spec[0]["M"], spec[-1]["lam"][0],
             spec[-1]["M"]))
    nns = [b["nn"] for b in spec]
    print("  near-null count (lam <= %g) along QLAD: %s"
          % (THR_NULL, "/".join(str(n) for n in nns)))
    print("  deep count (lam <= %g): %s"
          % (THR_DEEP, "/".join(str(b["nn_deep"]) for b in spec)))
    aligns = []
    for a, b in zip(spec, spec[1:]):
        if a["nn"] == 0 or b["nn"] == 0:
            aligns.append(None)
            continue
        Vp = np.zeros((b["M"], a["nn"]))
        Vp[:a["M"]] = a["Vn"]
        pr = b["Vn"].T @ Vp
        aligns.append(float(np.sum(pr ** 2) / a["nn"]))
    astr = "/".join("%.3f" % a if a is not None else "-"
                    for a in aligns)
    last5 = nns[-5:]
    spread = max(last5) - min(last5)
    a4 = [a for a in aligns[-4:] if a is not None]
    br1 = (spread <= Q2_NSPREAD and len(a4) == 4
           and float(np.mean(a4)) >= Q2_ALIGN)
    Qw = [float(np.sum(b["qf"])) for b in spec]
    w5 = Qw[-5:]
    wspread = (max(w5) - min(w5)) / max(max(w5), 1.0e-300)
    br2 = wspread <= Q2_WSPREAD
    return gate("Q2 kernel identifiability: branch(i) STABLE OBJECT "
                "%s (count spread last 5 = %d <= %d; consecutive "
                "subspace alignment %s, mean last 4 = %.3f >= %g) / "
                "branch(ii) STABLE BATTERY WEIGHT %s (total near-null"
                " weight last 5 = %s, rel spread %.3f <= %g)"
                % (br1, spread, Q2_NSPREAD, astr,
                   float(np.mean(a4)) if len(a4) == 4 else -1.0,
                   Q2_ALIGN, br2,
                   "/".join("%.2e" % w for w in w5), wspread,
                   Q2_WSPREAD), br1 or br2)


def q3_block(spec, names):
    print("\n-- Q3: does the kernel contribution vanish on the "
          "battery, or is it an admissible stable null pairing?")
    qtop = spec[-1]["qf"]
    qhist = np.stack([b["qf"] for b in spec[-5:]])
    spread_f = (qhist.max(axis=0) - qhist.min(axis=0)) \
        / np.maximum(qhist.max(axis=0), 1.0e-300)
    dfc = 1.0 - y_profile(spec[-1], (EPS_LADDER[-1],))[0]
    print("  pairing with EVERY battery function (M = %d): "
          "q_f = near-null weight (lam <= %g), spread = rel spread "
          "last 5 rungs, deficit = 1 - <f, Y_(1e-5) f>:"
          % (spec[-1]["M"], THR_NULL))
    for i, nm in enumerate(names):
        print("    %-18s q_f = %.2e  spread = %.3f  deficit = %.2e"
              % (nm, qtop[i], spread_f[i], dfc[i]))
    br1 = float(np.max(qtop)) <= Q3_VANISH
    big = [i for i in range(len(names)) if qtop[i] > Q3_VANISH]
    br2 = all(spread_f[i] <= Q3_STAB for i in big)
    return gate("Q3 battery pairing: branch(i) VANISHING %s (max q_f "
                "= %.2e vs %g) / branch(ii) ADMISSIBLE STABLE NULL "
                "PAIRING %s (%d funcs above %g, worst spread %.3f <= "
                "%g)" % (br1, float(np.max(qtop)), Q3_VANISH, br2,
                         len(big), Q3_VANISH,
                         max((spread_f[i] for i in big), default=0.0),
                         Q3_STAB), br1 or br2)


# ================================================== Q4: fixed-f limit
def q4_block(spec, names, res):
    print("\n-- Q4: fixed-f eps -> 0 limit via the spectral theorem "
          "(monotone + measured Cauchy rate)")
    mono_worst = np.inf
    for blk in spec:
        Y = y_profile(blk, EPS_LADDER)
        mono_worst = min(mono_worst, float(np.min(np.diff(Y,
                                                          axis=0))))
    top, prev = spec[-1], spec[-2]
    Yt = y_profile(top, EPS_LADDER)
    Yp = y_profile(prev, EPS_LADDER)
    dt, dp = np.diff(Yt, axis=0), np.diff(Yp, axis=0)
    contract = (1.0 - Yt[-1]) / np.maximum(1.0 - Yt[0], 1.0e-300)
    xstab = float(np.max(np.abs(dt - dp)))
    med_ratio = [float(np.median(dt[j + 1] / np.maximum(dt[j],
                                                        1.0e-300)))
                 for j in range(dt.shape[0] - 1)]
    print("  per-f profiles at M = %d (y = <f, Y_eps f> over eps = "
          "%s):" % (top["M"], "/".join("%g" % e for e in EPS_LADDER)))
    for i, nm in enumerate(names):
        rat = "/".join("%.2f" % (dt[j + 1, i]
                                 / max(dt[j, i], 1.0e-300))
                       for j in range(dt.shape[0] - 1))
        print("    %-18s y = %s  incr = %s  ratios = %s  "
              "contraction = %.4f"
              % (nm, "/".join("%.4f" % v for v in Yt[:, i]),
                 "/".join("%.1e" % v for v in dt[:, i]), rat,
                 contract[i]))
    print("  median Cauchy-ratio profile over the battery: %s; "
          "X-stability of the increments |d(M=%d) - d(M=%d)| <= %.1e "
          "(reported)" % ("/".join("%.2f" % r for r in med_ratio),
                          top["M"], prev["M"], xstab))
    # spectral-vs-Cholesky Ward on diag(E_Y) at the top rung
    wspec = 0.0
    for j, eps in enumerate(EPS_LADDER):
        ycho = np.concatenate([np.diag(res[eps]["EY"][M_TOP][R])
                               for R in R_BAT])
        wspec = max(wspec, float(np.max(np.abs(ycho - Yt[j]))))
    check("G3.1 spectral-vs-Cholesky Ward on diag(E_Y) at M = %d, "
          "every eps <= %.0e" % (M_TOP, WARD_SPEC),
          wspec <= WARD_SPEC, "max abs %.1e" % wspec)
    ok = (mono_worst >= Q4_MONO
          and float(np.max(contract)) <= Q4_CONTRACT)
    return gate("Q4 fixed-f limit: MONOTONE certificate min "
                "eps-increment = %+.1e >= %.0e on every QLAD rung; "
                "deficit contraction (1-y(1e-5))/(1-y(1e-1)) = "
                "%.4f..%.4f <= %g for all 14 f (uniformity across f "
                "NOT required and not claimed)"
                % (mono_worst, Q4_MONO, float(np.min(contract)),
                   float(np.max(contract)), Q4_CONTRACT), ok)


# ================================================== controls
def control_yosida(Tc, bats, label):
    A = Tc[:M_CTRL, :M_CTRL]
    lam, V = np.linalg.eigh(A)
    Fall, _names = battery_all(bats, M_CTRL)
    wt = (V.T @ Fall) ** 2
    nneg = int(np.sum(lam < 0.0))
    pole = min(float(np.min(np.abs(lam + e))) for e in EPS_LADDER)
    if pole < POLE_TOL:
        return True, ("SINGULAR Yosida: |lam + eps| = %.1e < %.0e "
                      "(lambda_min = %.2e, %d negative eigenvalues)"
                      % (pole, POLE_TOL, lam[0], nneg))
    gmin, gmax = np.inf, -np.inf
    Yb = []
    for e in EPS_LADDER:
        g = lam / (lam + e)
        gmin, gmax = min(gmin, float(np.min(g))), \
            max(gmax, float(np.max(g)))
        Yb.append(wt.T @ g)
    difs = np.diff(np.stack(Yb), axis=0)
    viol = float(np.min(difs))
    nviol = int(np.sum(difs < -CTRL_MONO))
    fire = (gmin < -SBRK) or (gmax > 1.0 + SBRK) \
        or (viol < -CTRL_MONO)
    return fire, ("lambda_min(A) = %.2e, %d/%d negative eigenvalues; "
                  "SANDWICH: min g = %.1e, max g = %.1e (bars "
                  "-%g / 1+%g); MONOTONICITY: %d battery violations, "
                  "worst increment %.1e (bar -%.0e): fire=%s"
                  % (lam[0], nneg, M_CTRL, gmin, gmax, SBRK, SBRK,
                     nviol, viol, CTRL_MONO, fire))


def run_controls(c_cont, alpha_full, ka, bats):
    print("\n-- controls (must fire: indefinite A destroys the "
          "sandwich / monotonicity of the Yosida map)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_full, ka))
    cat_s, _dd = core.atom_lags_at(alpha_full, M_TOP, pos,
                                   core.MU_ALL[:ka])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP])
    fire_s, det_s = control_yosida(Ts, bats, "scramble")
    check("CS position-scramble control fires", fire_s, det_s)

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
    fire_e, det_e = control_yosida(TE, bats, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ================================================== run
def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- kernel-safe eps -> 0 decider (bounded "
          "Yosida transform)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + eps grids + thresholds + bars "
          "SHA-256-frozen BEFORE any comb data load", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= table cap %d (X = %.6f "
          "<= ln(ATOM_MAX) = %.6f); sieve cover exp(X_top) + 2 = %d "
          "<= ATOM_MAX = %d"
          % (M_TOP, M_CAP, M_TOP * D, math.log(core.ATOM_MAX),
             int(math.exp(M_TOP * D)) + 2, core.ATOM_MAX),
          M_TOP <= M_CAP
          and int(math.exp(M_TOP * D)) + 2 <= core.ATOM_MAX)

    # ---- first comb/deployed data touch strictly after the freeze
    T, c_cont, alpha_full, ka = build_tower()

    # ---- real-data operator sandwich at the control rung
    lamR = np.linalg.eigvalsh(T[:M_CTRL, :M_CTRL])
    gmin = min(float(np.min(lamR / (lamR + e))) for e in EPS_LADDER)
    gmax = max(float(np.max(lamR / (lamR + e))) for e in EPS_LADDER)
    check("G1.2 real-data operator sandwich at M = %d: all Yosida "
          "eigenvalues in [%.1e, 1 - %.1e] for every eps (bars "
          "-%.0e / 1+%.0e) -- PD is MEASURED output, never a gate "
          "assumption" % (M_CTRL, gmin, 1.0 - gmax, SANDWICH_TOL,
                          SANDWICH_TOL),
          gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

    # ---- Q1
    q1_ok, res = q1_block(T, bats)

    # ---- Q2 / Q3 / Q4 (spectral)
    spec, names = spectral_block(T, bats)
    q2_ok = q2_block(spec)
    q3_ok = q3_block(spec, names)
    q4_ok = q4_block(spec, names, res)

    # ---- controls
    run_controls(c_cont, alpha_full, ka, bats)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    qs = dict(Q1=q1_ok, Q2=q2_ok, Q3=q3_ok, Q4=q4_ok)
    n_q = sum(1 for v in qs.values() if v)
    if guards_ok and controls_ok and n_q == 4:
        verdict = "YOSIDA-KERNEL-SAFE"
    elif guards_ok and controls_ok and n_q >= 2:
        verdict = "YOSIDA-PARTIAL"
    else:
        verdict = "YOSIDA-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, questions %s, "
          "runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             " ".join("%s=%s" % (k, "PASS" if v else "FAIL")
                      for k, v in qs.items()), time.time() - T_START))
    if verdict == "YOSIDA-KERNEL-SAFE":
        print("CONSEQUENCE: the eps -> 0 limit is treated WITHOUT a "
              "positive eigenvalue margin -- the handoff observable "
              "lives on the bounded Yosida transform (sandwich + "
              "double monotonicity certificates), the near-null part "
              "is an identified stable object with a quantified, "
              "admissible battery pairing (Ihara lesson: exact null "
              "modes allowed), and every fixed test function has a "
              "monotone, contraction-certified eps-limit.  The "
              "resolvent wall is BYPASSED, not solved: no statement "
              "beyond the reachable surface, no X -> infinity claim, "
              "NO RH claim.")
    elif verdict == "YOSIDA-PARTIAL":
        print("HONEST READING: the open questions are %s -- their "
              "exact failing numbers are printed above; the "
              "kernel-safe route carries only the decided part."
              % ", ".join(k for k, v in qs.items() if not v))
    else:
        print("KILL: a guard failed, a control spuriously converged, "
              "or the route needs the forbidden 1/eps bound -- the "
              "kernel-safe formulation closes honestly at this "
              "surface.")
    return 0 if (guards_ok and controls_ok) else 1

_run_part1 = run


def _run_part2():
    # PART 2 -- yosida_qf_convergence_probe.py (verbatim; module-level names are
    # local to this function scope; the alias import of the
    # parent points at this module)


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
    yhp = sys.modules[__name__]  # part 1 of this module
    import epstein_firewall_probe as epx  # noqa: E402

    T_START = time.time()

    # ------------------------------------------------ frozen specification
    D = srp.DGRID                        # 1/64, dyadic float-exact
    ATOM_MAX_EXT = 4000000               # extended comb cap (frozen)
    M_CAP_EXT = int(math.floor(math.log(ATOM_MAX_EXT) / D))   # 972
    M_TOP_EXT = 972                      # deepest rung (step-4 aligned)
    M_TOP_PAR = 824                      # parent cap (step-8 aligned)
    QLAD_PAR = list(range(256, 801, 32)) + [824]   # parent grid, reported
    EXT_LAD = list(range(824, 973, 4))   # 38 rungs, X = 12.875..15.1875
    MID5 = slice(17, 22)                 # EXT_LAD[17:22], M = 892..908
    LAST5 = slice(33, 38)                # EXT_LAD[33:38], M = 956..972
    HALF2 = slice(19, 38)                # second half, M = 900..972

    R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
    NPAD = 128                           # max battery support in cells
    EPS_LADDER = yhp.EPS_LADDER          # (1e-1 .. 1e-5), verbatim
    EPS_GATED = yhp.EPS_GATED            # (1e-1, 1e-2, 1e-3), verbatim

    THR_NULL = 1.0e-4                    # gated near-null threshold
    THR_ROB = (3.0e-4, 1.0e-4, 3.0e-5)   # robustness report thresholds
    THR_DEEP = 1.0e-5                    # deep-mode census (reported)
    N_MED = 5                            # median block size

    QF_DRIFT = 0.15                      # A1: med5 drift bar
    QF_SLOPE = 0.15                      # A2: rel slope bar per X unit
    QF_FLOOR = 1.0e-12                   # denominator floor
    NN_SPREAD = 3                        # A3: count spread over LAST5
    ALIGN_BAR = 0.80                     # A3: mean alignment, last 4

    B_RCOND = 1.0e-10                    # B: pseudo-inverse rcond
    B_KEEP = 0.30                        # B1: retained norm^2 floor
    B_RATE = 0.10                        # B2: b_Y floor
    B_BAND = 0.10                        # B2: |b_Y - b_parent| band
    B_RESID = 5.0e-2                     # B3: residual q_f cap on LAST5
    B_RESID_LO = 1.0e-3                  # B3: spread applies above this
    B_SPREAD = 0.5                       # B3: residual rel spread bar
    B_MONO = -1.0e-12                    # B4: eps-monotone floor
    B_CONTRACT = 0.25                    # B4: deficit contraction bar
    WARD_RES = 1.0e-8                    # B: resolvent-identity Ward

    # parent's frozen first-run b_Y values (R = 1, R = 2), gated band ref
    PARENT_BY = {1.0e-1: (0.239, 0.185), 1.0e-2: (0.259, 0.149),
                 1.0e-3: (0.178, 0.186)}
    PARENT_QF_MAX = 0.446                # parent frozen max q_f (M 824)
    PARENT_SPREAD_WORST = 0.711          # parent frozen worst spread
    REPRO_TOL = 2.0e-3                   # G1.5 reproduction tolerance

    COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
    PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
    SANDWICH_TOL = 1.0e-9                # G1.6 sandwich slack
    QF_BOUND_TOL = 1.0e-9                # G1.7 boundedness audit slack
    RUNTIME_CAP = 600.0                  # seconds, predeclared

    M_CTRL = 512                         # control spectral rung (parent)
    EP_NCAP = 34000                      # Epstein Lambda_E table reach
    EP_MMAX = 640                        # Epstein control tower cap
    SEED = 7

    BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
              "prevprime", "primepi", "sympy")

    CHECKS = []       # guards + controls: all must pass, else invalid run
    GATES = []        # candidate gates: feed the verdict only


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
        """Battery bytes + both ladders + thresholds + every bar + the
        extended-comb specification, SHA-256 frozen BEFORE any comb data
        is built in this probe."""
        bats = {}
        hsh = hashlib.sha256()
        hsh.update(("yosida-qf-convergence spec: 4 boxes + 3 hats per R, "
                    "l2-norm, D=%.10f, R=%s; extended comb = deployed "
                    "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                    "M_TOP_EXT=%d (parent %d); QLAD_PAR=%s; EXT_LAD=%s; "
                    "MID5=[17:22] LAST5=[33:38] HALF2=[19:38]; thr "
                    "null=%g rob=%s deep=%g; A1 drift<=%g A2 slope<=%g "
                    "floor=%g; A3 nspread<=%d align>=%g; B: rcond=%g "
                    "keep>=%g b>=%g band<=%g resid<=%g/%g spread<=%g "
                    "mono>=%g contract<=%g ward<=%g parentB=%s; repro "
                    "qfmax=%g spread=%g tol=%g; guards: comb<=%g "
                    "prefix<=%g sandwich<=%g bound<=%g runtime<=%g; "
                    "controls: M=%d epcap=%d epM=%d seed=%d; iteration: "
                    "B iff A fails any of A1/A2/A3, else unused"
                    % (D, R_BAT, ATOM_MAX_EXT, M_CAP_EXT, M_TOP_EXT,
                       M_TOP_PAR, QLAD_PAR, EXT_LAD, THR_NULL, THR_ROB,
                       THR_DEEP, QF_DRIFT, QF_SLOPE, QF_FLOOR, NN_SPREAD,
                       ALIGN_BAR, B_RCOND, B_KEEP, B_RATE, B_BAND,
                       B_RESID, B_RESID_LO, B_SPREAD, B_MONO, B_CONTRACT,
                       WARD_RES, sorted(PARENT_BY.items()),
                       PARENT_QF_MAX, PARENT_SPREAD_WORST, REPRO_TOL,
                       COMB_DEV_BAR, PREFIX_WARD, SANDWICH_TOL,
                       QF_BOUND_TOL, RUNTIME_CAP, M_CTRL, EP_NCAP,
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


    # ------------------------------------------------ towers
    def build_parent_tower():
        """The parent tower verbatim (channel construction + Gauss
        double-sieve consistency guard), M_TOP_PAR cells."""
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
        """The deployed von Mangoldt generator at the extended cap, with
        overlap + Chebyshev-envelope guards."""
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
              "parent tower, max abs dev %.1e <= %.0e (tent assembly is "
              "1-cell local; measured, not assumed)"
              % (M_TOP_PAR, M_TOP_PAR, dev, PREFIX_WARD),
              dev <= PREFIX_WARD)
        print("  extension census: ka = %d atoms to e^%.4f (parent had "
              "atoms to e^%.4f)" % (ka, 2.0 * alpha, M_TOP_PAR * D))
        return T, c_cont, alpha, ka


    # ------------------------------------------------ spectral ladder
    def spectral_pass(T):
        """One dense eigendecomposition per rung.  Stored per rung: the
        spectrum, the first-NPAD rows of the eigenvector matrix (enough
        to pair ANY battery supported on <= NPAD cells with the full
        spectrum), and the full-length near-null basis (for alignments)."""
        sizes = sorted(set(QLAD_PAR) | set(EXT_LAD))
        out = {}
        for M in sizes:
            lam, V = np.linalg.eigh(T[:M, :M])
            idx = np.nonzero(lam <= THR_NULL)[0]
            out[M] = dict(M=M, lam=lam, V128=V[:NPAD, :].copy(),
                          Vn=V[:, idx].copy(), nn=len(idx),
                          nn_deep=int(np.sum(lam <= THR_DEEP)))
        return out


    def qf_of(blk, F, thr):
        """Near-null pairing weights q_f = sum_{lam <= thr} <v, f>^2 for
        every battery column of F (NPAD x n, unit vectors)."""
        idx = blk["lam"] <= thr
        W = blk["V128"][:, idx]
        return ((W.T @ F) ** 2).sum(axis=0)


    def y_profile(blk, F, eps_set):
        """<f, Y_eps f> per battery column via the spectral map."""
        wt = (blk["V128"].T @ F) ** 2          # (M, n)
        return np.stack([wt.T @ (blk["lam"] / (blk["lam"] + e))
                         for e in eps_set])    # (n_eps, n)


    def lin_slope(xs, ys):
        A = np.vstack([np.ones_like(xs), xs]).T
        coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
        return float(coef[1])


    def alignment(blk_a, blk_b):
        """Parent formula verbatim: ||V_new^T pad(V_old)||_F^2 / dim_old."""
        if blk_a["nn"] == 0 or blk_b["nn"] == 0:
            return None
        Vp = np.zeros((blk_b["M"], blk_a["nn"]))
        Vp[:blk_a["M"]] = blk_a["Vn"]
        pr = blk_b["Vn"].T @ Vp
        return float(np.sum(pr ** 2) / blk_a["nn"])


    # ------------------------------------------------ Candidate A
    def drift_stats(q_ext, xs_ext):
        """Frozen per-function statistics on the EXT ladder: med5 drift +
        normalized second-half linear slope."""
        med_mid = np.median(q_ext[MID5], axis=0)
        med_last = np.median(q_ext[LAST5], axis=0)
        drift = np.abs(med_last - med_mid) \
            / np.maximum(np.maximum(med_last, med_mid), QF_FLOOR)
        slopes, rel_slopes = [], []
        for j in range(q_ext.shape[1]):
            s = lin_slope(xs_ext[HALF2], q_ext[HALF2, j])
            slopes.append(s)
            rel_slopes.append(abs(s) / max(float(np.mean(q_ext[HALF2, j])),
                                           QF_FLOOR))
        return med_mid, med_last, drift, np.array(slopes), \
            np.array(rel_slopes)


    def candidate_a(spec, F, names):
        print("\n-- Candidate A: q_f(X) on the deeper + denser tower "
              "(gated threshold %g)" % THR_NULL)
        ext = [spec[M] for M in EXT_LAD]
        par = [spec[M] for M in QLAD_PAR]
        xs_ext = np.array([b["M"] * D for b in ext])

        # parent reproduction Ward (G1.5) on the recomputed parent grid
        q_par_top = qf_of(par[-1], F, THR_NULL)
        q_par_hist = np.stack([qf_of(b, F, THR_NULL) for b in par[-5:]])
        spread_par = (q_par_hist.max(axis=0) - q_par_hist.min(axis=0)) \
            / np.maximum(q_par_hist.max(axis=0), QF_FLOOR)
        dev_q = abs(float(np.max(q_par_top)) - PARENT_QF_MAX)
        dev_s = abs(float(np.max(spread_par)) - PARENT_SPREAD_WORST)
        check("G1.5 parent reproduction Ward: max q_f(M=%d) = %.4f vs "
              "frozen %.3f (dev %.1e), worst parent last-5 spread = "
              "%.4f vs frozen %.3f (dev %.1e), both <= %.0e"
              % (M_TOP_PAR, float(np.max(q_par_top)), PARENT_QF_MAX,
                 dev_q, float(np.max(spread_par)), PARENT_SPREAD_WORST,
                 dev_s, REPRO_TOL),
              dev_q <= REPRO_TOL and dev_s <= REPRO_TOL)

        # per-function table + gates
        q_ext = np.stack([qf_of(b, F, THR_NULL) for b in ext])
        med_mid, med_last, drift, slopes, rel_slopes = \
            drift_stats(q_ext, xs_ext)
        q_top = q_ext[-1]
        print("  per-function q_f table (thr %g): parent M=%d vs "
              "extended M=%d; drift = |med5(LAST5)-med5(MID5)|/max; "
              "slope = |lin fit dq/dX| / mean over EXT[19:]:"
              % (THR_NULL, M_TOP_PAR, M_TOP_EXT))
        for j, nm in enumerate(names):
            print("    %-18s q(824) = %.4f  q(972) = %.4f  med5mid = "
                  "%.4f  med5last = %.4f  drift = %.4f  slope/X = %.4f "
                  " %s" % (nm, q_par_top[j], q_top[j], med_mid[j],
                           med_last[j], drift[j], rel_slopes[j],
                           "ok" if (drift[j] <= QF_DRIFT
                                    and rel_slopes[j] <= QF_SLOPE)
                           else "FAIL"))
        spread_ext = (q_ext[LAST5].max(axis=0) - q_ext[LAST5].min(axis=0)) \
            / np.maximum(q_ext[LAST5].max(axis=0), QF_FLOOR)
        print("  last-5 rel spreads on the dense extension: %.4f..%.4f "
              "(parent coarse-grid spreads were 0.309..0.711)"
              % (float(np.min(spread_ext)), float(np.max(spread_ext))))

        a1 = gate("A1 drift: max per-function med5 drift = %.4f (%s) <= "
                  "%g for all 14 functions"
                  % (float(np.max(drift)),
                     names[int(np.argmax(drift))], QF_DRIFT),
                  bool(np.all(drift <= QF_DRIFT)))
        a2 = gate("A2 slope: max normalized second-half slope = %.4f/X "
                  "(%s) <= %g for all 14 functions"
                  % (float(np.max(rel_slopes)),
                     names[int(np.argmax(rel_slopes))], QF_SLOPE),
                  bool(np.all(rel_slopes <= QF_SLOPE)))

        # A3 near-kernel stability under the extension
        nns = [b["nn"] for b in ext]
        deeps = [b["nn_deep"] for b in ext]
        aligns = [alignment(a, b) for a, b in zip(ext, ext[1:])]
        a4 = [a for a in aligns[-4:] if a is not None]
        nn5 = nns[LAST5]
        spread_nn = max(nn5) - min(nn5)
        mean_a4 = float(np.mean(a4)) if len(a4) == 4 else -1.0
        print("  near-null count along EXT: %s"
              % "/".join(str(n) for n in nns))
        print("  deep count (lam <= %g) along EXT: %s"
              % (THR_DEEP, "/".join(str(n) for n in deeps)))
        print("  consecutive alignment along EXT: min %.6f, mean last 4 "
              "= %.6f" % (min(a for a in aligns if a is not None),
                          mean_a4))
        a3 = gate("A3 near-kernel stability under extension: count "
                  "spread last 5 = %d <= %d AND mean consecutive "
                  "alignment last 4 = %.5f >= %g"
                  % (spread_nn, NN_SPREAD, mean_a4, ALIGN_BAR),
                  spread_nn <= NN_SPREAD and mean_a4 >= ALIGN_BAR)

        # threshold-robustness report (never gated)
        print("  threshold-robustness report (never gated):")
        for thr in THR_ROB:
            q_t = np.stack([qf_of(b, F, thr) for b in ext])
            _mm, _ml, dr_t, _s, rs_t = drift_stats(q_t, xs_ext)
            nn_t = int(np.sum(ext[-1]["lam"] <= thr))
            print("    thr = %-7g nn(%d) = %d  worst drift = %.4f (%s)  "
                  "worst slope/X = %.4f (%s)"
                  % (thr, M_TOP_EXT, nn_t, float(np.max(dr_t)),
                     names[int(np.argmax(dr_t))], float(np.max(rs_t)),
                     names[int(np.argmax(rs_t))]))

        # boundedness / KILL audit over everything gated
        qmin = float(np.min(q_ext))
        qmax = float(np.max(q_ext))
        check("G1.7 boundedness/KILL audit: every gated q_f in "
              "[%.1e, %.4f], inside [-1e-12, 1 + %.0e] -- bounded "
              "quadratic forms of unit vectors, no 1/eps normalization, "
              "no PD-margin assumption in any gate"
              % (qmin, qmax, QF_BOUND_TOL),
              qmin >= -1.0e-12 and qmax <= 1.0 + QF_BOUND_TOL)
        return (a1 and a2 and a3), q_par_top, q_top


    # ------------------------------------------------ Candidate B
    def orthogonalize_battery(bats, spec):
        """Support-restricted orthogonalization against the frozen
        deepest near-kernel: g = f - W (W^T W)^+ W^T f, W = V_null[:nR].
        g keeps the battery support and has exactly zero pairing with the
        frozen basis; renormalized and SHA-frozen."""
        top = spec[M_TOP_EXT]
        keeps, bats_o = [], {}
        hsh = hashlib.sha256()
        hsh.update(("qf-orthogonalized battery: support-restricted, "
                    "kernel M=%d thr=%g rcond=%g"
                    % (M_TOP_EXT, THR_NULL, B_RCOND)).encode())
        for R in R_BAT:
            nR = int(round(R / D))
            W = top["Vn"][:nR, :]
            Ginv = np.linalg.pinv(W.T @ W, rcond=B_RCOND)
            fs = []
            for nm, v in bats[R]:
                g = v - W @ (Ginv @ (W.T @ v))
                keep = float(g @ g)
                keeps.append((("R%g:%s" % (R, nm)), keep))
                g = g / max(math.sqrt(keep), 1.0e-300)
                fs.append((nm + "-perp", g))
                hsh.update(nm.encode())
                hsh.update(g.tobytes())
            bats_o[R] = fs
        return bats_o, keeps, hsh.hexdigest()


    def candidate_b(T, bats, spec, names):
        print("\n-- Candidate B: near-kernel-orthogonalized battery "
              "(declared iteration SPENT)")
        bats_o, keeps, sha_o = orthogonalize_battery(bats, spec)
        print("  orthogonalized battery SHA256 %s..." % sha_o[:16])
        for nm, keep in keeps:
            print("    %-18s retained norm^2 = %.4f" % (nm, keep))
        b1 = gate("B1 substance: min retained norm^2 = %.4f >= %g"
                  % (min(k for _n, k in keeps), B_KEEP),
                  all(k >= B_KEEP for _n, k in keeps))

        # B2: parent Q1 machinery verbatim on the orthogonalized battery
        res, sizes, ladB = yhp.yosida_pass(T, bats_o)
        wmax = max(res[eps]["ward"] for eps in EPS_LADDER)
        check("G2.1 (B) resolvent-identity Ward A(G^eps F) = F - eps "
              "G^eps F <= %.0e" % WARD_RES, wmax <= WARD_RES,
              "max rel %.1e" % wmax)
        b2 = True
        for eps in EPS_GATED:
            for i, R in enumerate(R_BAT):
                rowsY, _sc = yhp.defect_rows(res[eps]["EY"], ladB, R)
                bY, resid, b2f, med, _mxs = yhp.stat_of(rowsY)
                ref = PARENT_BY[eps][i]
                ok = bY >= B_RATE and abs(bY - ref) <= B_BAND
                b2 &= gate("B2 rate eps=%g,R=%g: b_Y = %.3f (>= %g, "
                           "parent %.3f, |diff| = %.3f <= %g; resid "
                           "%.2f, b2 = %.3f, med%d = %.3f reported)"
                           % (eps, R, bY, B_RATE, ref, abs(bY - ref),
                              B_BAND, resid, b2f, N_MED, med), ok)

        # B3: residual pairing on the last 5 extension rungs
        Fo, names_o = battery_matrix(bats_o)
        ext5 = [spec[M] for M in EXT_LAD[LAST5]]
        q_res = np.stack([qf_of(b, Fo, THR_NULL) for b in ext5])
        mx = float(np.max(q_res))
        spread = (q_res.max(axis=0) - q_res.min(axis=0)) \
            / np.maximum(q_res.max(axis=0), QF_FLOOR)
        big = [j for j in range(len(names_o))
               if float(np.max(q_res[:, j])) > B_RESID_LO]
        worst_sp = max((float(spread[j]) for j in big), default=0.0)
        for j, nm in enumerate(names_o):
            print("    %-23s residual q_f (LAST5) = %s"
                  % (nm, "/".join("%.1e" % v for v in q_res[:, j])))
        b3 = gate("B3 residual pairing: max residual q_f over LAST5 = "
                  "%.2e <= %g; %d functions above %g, worst rel spread "
                  "%.3f <= %g" % (mx, B_RESID, len(big), B_RESID_LO,
                                  worst_sp, B_SPREAD),
                  mx <= B_RESID and worst_sp <= B_SPREAD)

        # B4: parent Q4 gates on the orthogonalized battery
        mono_worst = np.inf
        for M in EXT_LAD:
            Y = y_profile(spec[M], Fo, EPS_LADDER)
            mono_worst = min(mono_worst,
                             float(np.min(np.diff(Y, axis=0))))
        Yt = y_profile(spec[M_TOP_EXT], Fo, EPS_LADDER)
        contract = (1.0 - Yt[-1]) / np.maximum(1.0 - Yt[0], 1.0e-300)
        b4 = gate("B4 fixed-f limits: monotone min eps-increment = "
                  "%+.1e >= %.0e on every EXT rung; deficit contraction "
                  "= %.4f..%.4f <= %g at M = %d"
                  % (mono_worst, B_MONO, float(np.min(contract)),
                     float(np.max(contract)), B_CONTRACT, M_TOP_EXT),
                  mono_worst >= B_MONO
                  and float(np.max(contract)) <= B_CONTRACT)
        return b1 and b2 and b3 and b4


    # ------------------------------------------------ controls
    def run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext, bats):
        print("\n-- controls (must fire: indefinite A destroys the "
              "kernel-candidate reading; parent fire rule verbatim)")
        rng = np.random.default_rng(SEED)
        pos = np.sort(rng.uniform(0.5, 2.0 * alpha_ext, ka_ext))
        cat_s, _dd = core.atom_lags_at(alpha_ext, M_TOP_EXT, pos,
                                       mu_ext[:ka_ext])
        Ts = sla.toeplitz((c_cont_ext + cat_s)[:M_TOP_EXT])
        lam_s = np.linalg.eigvalsh(Ts[:M_CTRL, :M_CTRL])
        print("  CS census: %d/%d eigenvalues below -THR_NULL = -%g "
              "(the 'near-kernel' is not a kernel candidate)"
              % (int(np.sum(lam_s < -THR_NULL)), M_CTRL, THR_NULL))
        fire_s, det_s = yhp.control_yosida(Ts, bats, "scramble")
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
        lam_e = np.linalg.eigvalsh(TE[:M_CTRL, :M_CTRL])
        print("  CE census: %d/%d eigenvalues below -THR_NULL = -%g"
              % (int(np.sum(lam_e < -THR_NULL)), M_CTRL, THR_NULL))
        fire_e, det_e = yhp.control_yosida(TE, bats, "epstein")
        check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
              "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


    # ------------------------------------------------ run
    def run():
        print("=" * 78)
        print("GLOBAL HANDOFF -- Q3 follow-up decider: q_f(X) "
              "convergence on the extended tower")
        print("=" * 78)

        hits = ast_firewall()
        check("G0.1 AST firewall", not hits, str(hits))
        bats, spec_sha = freeze_spec()
        check("G0.2 battery + ladders + thresholds + bars + extended-"
              "comb spec SHA-256-frozen BEFORE any comb data is built "
              "here", True, "SHA256 %s..." % spec_sha[:16])
        check("G0.3 reach census: M_TOP_EXT = %d <= floor(64 ln %d) = %d "
              "(X = %.6f <= %.6f); sieve cover exp(X_top) + 2 = %d <= %d;"
              " runtime cap %.0f s predeclared"
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

        # ---- spectral ladder (one eigh per rung, everything reusable)
        spec = spectral_pass(T)
        print("  PD margins (eps = 0, measured, never gated): "
              "lambda_min = %.3e (M %d) -> %.3e (M %d) -> %.3e (M %d)"
              % (spec[QLAD_PAR[0]]["lam"][0], QLAD_PAR[0],
                 spec[M_TOP_PAR]["lam"][0], M_TOP_PAR,
                 spec[M_TOP_EXT]["lam"][0], M_TOP_EXT))
        gmin, gmax = np.inf, -np.inf
        for M in (M_CTRL, M_TOP_EXT):
            lam = spec[M]["lam"]
            for e in EPS_LADDER:
                g = lam / (lam + e)
                gmin = min(gmin, float(np.min(g)))
                gmax = max(gmax, float(np.max(g)))
        check("G1.6 real-data operator sandwich at M = %d and M = %d: "
              "all Yosida eigenvalues in [%.1e, 1 - %.1e] for every eps "
              "(bars -%.0e / 1+%.0e) -- PD is MEASURED output, never a "
              "gate assumption" % (M_CTRL, M_TOP_EXT, gmin, 1.0 - gmax,
                                   SANDWICH_TOL, SANDWICH_TOL),
              gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

        # ---- Candidate A
        F, names = battery_matrix(bats)
        a_pass, _qp, _qt = candidate_a(spec, F, names)

        # ---- Candidate B (iff A failed; single declared iteration)
        b_pass = None
        if a_pass:
            print("\n  Candidate A passes: the declared iteration to "
                  "Candidate B is UNUSED (B never consulted).")
        else:
            print("\n!! DECLARED ITERATION TRIGGERED: Candidate A fails "
                  "-- the single predeclared iteration to Candidate B "
                  "(near-kernel-orthogonalized battery) is spent.")
            b_pass = candidate_b(T, bats, spec, names)

        # ---- controls
        run_controls(c_cont_ext, alpha_ext, ka_ext, mu_ext, bats)

        # ---- runtime guard (predeclared)
        dt = time.time() - T_START
        check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
              % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

        # ---- verdict (preregistered rules)
        guards_ok = all(ok for (n, ok) in CHECKS
                        if not n.startswith(("CS", "CE")))
        controls_ok = all(ok for (n, ok) in CHECKS
                          if n.startswith(("CS", "CE")))
        if not (guards_ok and controls_ok):
            verdict = "QF-DEAD"
        elif a_pass:
            verdict = "QF-CONVERGES"
        elif b_pass:
            verdict = "QF-ORTHOGONAL-CARRIES"
        else:
            verdict = "QF-DEAD"

        n_gate = sum(1 for (_n, ok) in GATES if ok)
        n_chk = sum(1 for (_n, ok) in CHECKS if ok)
        print("\nVERDICT: %s" % verdict)
        print("GATES %d/%d, GUARDS+CONTROLS %d/%d, iteration %s, "
              "runtime %.1f s"
              % (n_gate, len(GATES), n_chk, len(CHECKS),
                 "UNUSED (A decided)" if b_pass is None
                 else "SPENT (Candidate B)", time.time() - T_START))
        if verdict == "QF-CONVERGES":
            print("GATE-3 CONSEQUENCE (stated plainly): q_f(X) converges "
                  "per battery function at 4x parent rung density and "
                  "%.2f X units of new depth -- the kernel contribution "
                  "is an admissible exact null mode on the reachable "
                  "surface (Ihara lesson) and the DIAGONAL SEQUENCE "
                  "fixed f -> X -> eps IS buildable: Q3 closes "
                  "POSITIVELY at honest maximal depth.  NOT claimed: "
                  "X -> infinity, eps-uniformity, any spectral gap, RH."
                  % (M_TOP_EXT * D - M_TOP_PAR * D))
        elif verdict == "QF-ORTHOGONAL-CARRIES":
            print("GATE-3 CONSEQUENCE (stated plainly): the raw battery "
                  "null-pairing does NOT converge, but the handoff "
                  "observable survives on the near-kernel-orthogonalized "
                  "battery with rates inside the parent band -- the "
                  "null-pairing is an inessential battery artifact and "
                  "Q3 closes positively IN THE CORRECTED FORM (honestly "
                  "labeled as a battery correction).  NOT claimed: "
                  "X -> infinity, eps-uniformity, RH.")
        else:
            if not (guards_ok and controls_ok):
                print("KILL (invalid or spurious): a guard failed or a "
                      "control spuriously converged -- no statement "
                      "about Q3 follows from this run.")
            else:
                print("GATE-3 CONSEQUENCE (stated plainly): the wall "
                      "PERSISTS in q_f at honest maximal depth (X = "
                      "%.4f, 4x rung density) and survives the "
                      "orthogonalized battery -- the diagonal route "
                      "cannot take eps -> 0 at deep X with this battery "
                      "class: Q3 closes NEGATIVELY on the reachable "
                      "surface." % (M_TOP_EXT * D))
        return 0 if (guards_ok and controls_ok) else 1
    return run(), [n for (n, ok) in CHECKS if not ok], [n for (n, ok) in GATES if not ok]


def run():
    """run_all entry point (combined adjudication, frozen): part 1
    must reproduce its preregistered pattern (guards+controls 12/12,
    gates 9/10 with EXACTLY the Q3 gate failing, YOSIDA-PARTIAL);
    part 2 must reproduce its pattern (guards+controls 14/14, gates
    7/12 with EXACTLY A1/A2/B1 + two B2 cells failing, QF-DEAD) --
    the honest combined verdict is YOSIDA-PARTIAL/QF-DEAD with the
    q_f wall as THE named open object."""
    rc1 = _run_part1()
    gate_fails1 = [n for (n, ok) in GATES if not ok]
    part1_ok = (rc1 == 0 and len(gate_fails1) == 1
                and gate_fails1[0].startswith("Q3"))
    print("\n[%s] PART-1 PATTERN GATE: expected exactly the "
          "preregistered Q3 fail (YOSIDA-PARTIAL) -- failing gates: %s"
          % ("PASS" if part1_ok else "FAIL",
             [f.split()[0] for f in gate_fails1]))
    rc2, chk_fails2, gate_fails2 = _run_part2()
    toks2 = sorted(n.split()[0].split(".")[0] for n in gate_fails2)
    part2_ok = (rc2 == 0 and not chk_fails2
                and toks2 == ["A1", "A2", "B1", "B2", "B2"])
    print("\n[%s] PART-2 PATTERN GATE: expected exactly the "
          "preregistered A1/A2/B1 + two B2-cell fails (QF-DEAD) -- "
          "failing gates: %s"
          % ("PASS" if part2_ok else "FAIL", toks2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- YOSIDA-PARTIAL / QF-DEAD: "
          "the bounded Yosida formulation, the convergent near-kernel "
          "object, and the fixed-f monotone limits stand (Q1/Q2/Q4); "
          "the battery near-kernel pairing q_f is non-Cauchy at "
          "honest maximal depth and survives orthogonalization by "
          "structural subordination -- Q3 closes NEGATIVELY on the "
          "reachable surface; the q_f wall is the named open object.  "
          "NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(run())
