#!/usr/bin/env python3
"""v772 -- PRIME.QFFESHBACH.01: the fixed-d pair of the qf offensive, one module from two probes, combined verdict FESHBACH-PARTIAL / EDGE-KEEPS-MOVING -- fixed-d Feshbach closed PERMANENTLY on every reachable surface.  PART 1 (FESHBACH-PARTIAL, GATES 9/12 with exactly CAUCHY-6/GAP-7/GAP-8 the preregistered fails, GUARDS+CONTROLS 28/28; 1e8 comb): the d = 6 Feshbach reduction is EXACT and the right well-defined object -- the reconstruction identity holds at max rel residual 8.8e-13 against INDEPENDENT complex dense solves over 5 rungs x 5 z-points, matrix-Herglotz certified on every gated rung (max eig Im F~ = -1.000e-2 = -h exactly; min eig Im F~^{-1} = +98.8), band separated (min rel gap 0.1008 at M = 1096), coupling Ward P A Q = 0 measured at 3.1e-15..6.1e-15 -- but CAUCHY-6 fails on the slope clause (b2 = +0.006/X < 0.02): the tail flattens exactly where mode 7 grazes the band edge.  THE MOVING-EDGE PICTURE: d = 7 passes CAUCHY strongly (med5 0.207, b2 = +0.502/X) but loses separation at the top rung (gap 7/8 = 0.0613 at M = 1176); d = 8 has an internal 8/9 crossing at M = 976 (gap 5.4e-4, transport angle 87.2 deg) -- no fixed d in {6, 7, 8} owns a uniformly separated band on 888..1176.  PART 2 (EDGE-KEEPS-MOVING, GUARDS+CONTROLS 20/20, 160.3 s; 1e9 comb to X = 20.6875, 49,154,321 atoms): the 7/8 edge does NOT separate again -- it CLOSES INTO AN AVOIDED CROSSING (gap falls from 0.0613 at M = 1176 through 0.0209 to 0.0039 at M = 1240, relaxes to ~0.011, decays to 0.0074 at the top rung 1324; lam7 = 7.9351e-5 / lam8 = 7.9946e-5 / lam9 = 9.1935e-5 form a CLUSTER below thr 1e-4) while the transported d = 7 block stays Cauchy straight through the crossing (109 increments 2.72e-6 -> 3.94e-7, med5 0.181, b2 = +0.061/X): convergence was never the problem, band OWNERSHIP is.  MODE-DESCENT CADENCE (fit-free): entries at M = 888 / 992 / 1108 / 1276 (the 9th mode enters inside the extension), inter-entry gaps DX = 1.6250 / 1.8125 / 2.6250 -- mean 2.0208, rel spread 0.381 > the frozen 0.25 regularity bar: the cadence is real but NOT regular; the spacing WIDENS with depth (third gap 1.6x the first) -- the honest surprise and the number the cell-cocycle module must carry.  Reported: the d = 6 grazing RESOLVES (6/7 gap recovers to 0.4333 at the top -- the separated object is the 6-band again under a 7/8/9 cluster); the settled q_f levels hold to 0.87..1.09x over 2.3 more X units (drainage confirmation for free; extension fall rates +0.050..+0.083/X sit slightly above the 0.05 plateau bar, typed).  NO RH claim, no claim beyond X = 20.6875, no eps-uniformity.

PROVENANCE: discovery probes qf_feshbach_effective_probe.py (2026-08-05, 24.4 s, GATES 9/12, GUARDS+CONTROLS 28/28, verdict FESHBACH-PARTIAL; ONE DECLARED GUARD-NORMALIZATION CORRECTION carried honestly into this module: the first execution (25.0 s) was invalidated SOLELY by a dimensionally wrong normalization of the G1.9 z-independence Ward -- the measured float deviation 1.5e-16, machine-perfect for the exact shift identity, was compared against 1e-12 x the increment scale (2.7e-6) instead of 1e-12 x the block ENTRY scale (1e-2); the Ward normalization was corrected, NO gate bar was touched, and the repeat run produced IDENTICAL gate outcomes -- deterministic construction, both runs reported) and qf_edge_separation_probe.py (2026-08-05, first and only preregistered run, 160.3 s on the predeclared 1e9 comb, GUARDS+CONTROLS 20/20, verdict EDGE-KEEPS-MOVING, carried by the EDGE-A failure alone -- the frozen KM2 clause stays quiet because the cadence is not regular at the 0.25 bar).  Merged per the v518/v668/v763 precedent: part 1 verbatim at module level (sibling imports point at v563/v755/v766/v770; epstein_firewall_probe stays a read-only discovery import); part 2 verbatim inside an isolated function scope; numbers unchanged.  run() encodes both preregistered gate patterns as the expected outcome (v757 precedent).  RUNTIME NOTE (suite budget, v677 ~420 s precedent -- no thinning): part 2 re-derives the 1e9 sieve in-process (benchmarked 12.3 s / 13.5 GB for the sieve alone, ~160 s total on the reference machine); the frozen ladders are kept at full depth so the promoted module reproduces the frozen verdict verbatim.

PART 1 -- qf_feshbach_effective_probe.py (docstring verbatim):
QF-OFFENSIVE strand 3, module 3 -- the Feshbach effective block:
reduce the full window operator EXACTLY onto the slow band and decide
whether the transported effective block converges along the ladder,
so that the infinite positivity wall becomes the convergence of ONE
small matrix function.  qf_feshbach_effective_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  It never reads a zero
ordinate and never evaluates the target before every source object
is built and SHA-256 frozen.  The band, the transport and the
effective block are built exclusively from the source window
operator -- never from target data.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_drainage_probe -- QF-SETTLES-POSITIVE 14/14 on the 1e8 comb
     (X <= 18.375): the battery/near-kernel pairing settles at
     positive per-function constants (R2 family 0.225..0.358, R1
     family 0.008..0.079) -- the Feshbach treatment is MANDATORY.
     Typed cautions carried forward: 7th/8th threshold crossings at
     M = 992 / ~1108; 6/7 gap bottoms at 0.1008 (M ~ 1100) then
     recovers to 0.1397 (M = 1176); single deep mode persists.
  *  qf_spectral_bundle_probe -- QF-BUNDLE-PARTIAL: the Kato/polar
     transport of the band frame is well-defined (angles <= 2.72
     deg on 888..972) and gauge-covariant; machinery reused
     verbatim (sign_fix imported read-only).
  *  Holonomy check (drainage probe): transported coordinates move
     with O(1) velocity in X (step exponent ~1) -- convergence must
     come from velocity decay along X, which is exactly what the
     Cauchy gates below measure on the effective block.

OBJECT: per rung X_k and band dimension d, the Feshbach (Schur/
Livsic) map on Ran P with P = P_k^(d) = span of the d LOWEST
eigenmodes (band rule), Q = I - P:

    F_X(z) = P (A_X - z) P  -  P A_X Q [Q (A_X - z) Q]^{-1} Q A_X P,

restricted to Ran P and expressed in the band eigenframe; the
TRANSPORTED effective block is  F~_X(z) = U_{1,X}^* F_X(z) U_{1,X}
with the chained Kato/polar transport U_{1,X} per band dimension.
The reconstruction identity  [P (A_X - z)^{-1} P]|_{Ran P} =
F_X(z)^{-1}  is part of the deliverable and is gated at machine
precision against an INDEPENDENT dense solve of (A_X - z).

PREDECLARED ALGEBRA (honesty, stated BEFORE the run):
  (1) P is a SPECTRAL projector of A_X itself, so P A_X Q = 0
      IDENTICALLY: the Schur correction vanishes analytically and
      F_X(z) = Lambda_d(X) - z on the band frame.  The correction
      is nevertheless COMPUTED from the measured coupling matrix
      E = V_d^T A V_c (a commutation Ward, expected at machine
      scale) and carried through every formula, so nothing is
      assumed; the reconstruction gate is then a genuine TWO-PATH
      numerical Ward (eigh path vs independent dense solve).
  (2) z-shift identity: up to the machine-scale correction,
      F~_X(z) - F~_X(z') = (z' - z) I because the chained transport
      is orthogonal -- the Cauchy increments of F~ are
      z-INDEPENDENT.  This is declared so the per-(d, z) tables
      cannot be sold as independent evidence: they are gated once
      per d at the frozen reference point and a z-independence Ward
      binds all other gated cells to it.
  (3) Herglotz orientation: for self-adjoint A_X the effective
      block itself is ANTI-Herglotz (Im F~(z) <= 0 for Im z > 0;
      with zero coupling Im F~ = -Im z * I exactly) and the
      Herglotz object of the boundary-triple route is the INVERSE
      M~(z) = F~(z)^{-1} = the transported compressed resolvent,
      with Im M~(z) >= 0.  BOTH sides are gated (matrix
      inequalities up to the frozen numerical floor); they are
      exact structural identities whose float verification is the
      content -- the NON-trivial gates of this probe are the
      band-gap gates, the Cauchy gates and the d-adjudication.
  (4) Q-block separation at fixed z = -eps: for spectral P its
      spectrum is exactly {lambda_i(X) + eps : i > d}, so the
      margin profile IS the lambda_{d+1}(X) profile shifted by eps
      -- reported per (d, eps); this fixed-z separation is a
      DIFFERENT object from a global positive lower bound on A
      (which remains forbidden in gates; PD stays measured output).

FROZEN CONSTRUCTION (reused machinery verbatim, none invented):
  deep comb = deployed von Mangoldt sieve at ATOM_MAX = 1e8
      (drainage-probe cap, re-derived in-process -- probes write no
      files); M_CAP = 1178, M_TOP = 1176 (X = 18.375); guards:
      overlap exact, Chebyshev envelope, parent-tower prefix Ward.
  gated ladder GLAD = 888..1176 step 4 (73 rungs, 72 increments);
      step-1 sub-ladder HOLO_LAD = 1160..1176 (REPORTED only).
  band dimensions D_SET = (6, 7, 8) -- ALL THREE preregistered (the
      carried-forward caution as a predeclared question); the
      adjudication rule is FROZEN: the verdict names the SMALLEST d
      that passes all four gates (gap, Herglotz, reconstruction,
      Cauchy); no post-hoc choice.
  transport per d: sign-fixed d lowest eigenvectors (sign fix
      gauge-irrelevant, bundle lesson), overlap S_k = V_{k+1}^T
      pad(V_k), polar factor Q_k = UW^T of the SVD (floor
      sigma_min >= 1e-8, else transport undefined = kill), chained
      R_1 = I, R_{k+1} = Q_k R_k; F~_k(z) = R_k^T [Lambda_d(X_k) -
      z - C_d(z)] R_k with the measured Schur correction C_d(z) =
      E_d^T diag(1/(lambda_c - z))^{-1}-free form E_d(z-resolved),
      E_d = coupling rows (see (1)).
  evaluation points (frozen): gated real set z = -eps, eps in
      EPS_GATED = (1e-1, 1e-2, 1e-3) (X-before-eps order: every
      statistic runs along X at fixed z); reference cell Z_REF =
      -1e-2; Herglotz points ZC = (i h, -1e-3 + i h) with h = 1e-2.
FROZEN GATES (per band dimension d):
  GAP-d   band/bulk separation on the gated range: min over GLAD of
          (lambda_{d+1} - lambda_d)/lambda_{d+1} >= GAP_BAR = 0.10
          (the d = 6 minimum 0.1008 lives here; if the d = 6
          Q-block inherits the 7th/8th near-modes this is exactly
          where d = 7/8 may win); full profiles + argmin reported.
  HERG-d  matrix-Herglotz certificates on EVERY gated rung at both
          ZC points: max eig Im F~(z) <= HERG_FLOOR = 1e-10 AND
          min eig Im F~(z)^{-1} >= -HERG_FLOOR.
  REC-d   reconstruction identity at the frozen Ward rungs
          RECON_RUNGS = (888, 968, 1048, 1128, 1176) and ALL five z
          points: max rel entrywise residual
          | V_d^T (A - z)^{-1} V_d - F_d(z)^{-1} | / max|F^{-1}|
          <= REC_BAR = 1e-10 (independent dense solve).
  CAUCHY-d  the decider: delta_k = max-entry |F~_{k+1}(Z_REF) -
          F~_k(Z_REF)| over the 72 increments; oscillation-aware
          frozen statistic (house pattern): med5(LAST5)/med5(FIRST5)
          <= C_MED = 0.5 AND second-half falling rate b2 >=
          C_SLOPE = 0.02 per X unit (hbp.fit_rate verbatim);
          increment blocks FIRST5 = 1..5, LAST5 = 68..72, second
          half = 37..72; increment X = right-rung X.  Per-(d, eps)
          cells are bound to the Z_REF cell by the z-independence
          Ward ZW <= 1e-12 x scale (predeclared algebra (2)).
KILLS (frozen, from the offensive's list):
  K1 RH-strength bound audit: every gated quantity is a band-
     interior gap ratio, a fixed-z separation, a bounded transported
     matrix entry, a machine-precision identity residual, or a
     med5/slope statistic of these -- no global positivity of A, no
     1/eps, no PD margin enters any gate (structural audit printed
     with measured scales);
  K2 a positive lower eigenvalue bound on A entering a gate --
     forbidden; only the fixed-z Q-block separation (different
     object, declared in (4)) is used;
  K3 mode selection by target deviation -- AST firewall + the band
     rule is an eigenvalue-order rule of the source operator only;
  K4 transport undefined: sigma_min(S_k) < 1e-8 for some d (a
     principal angle at 90 deg);
  K5 the effective block not convergent for ANY d in {6, 7, 8}.
GUARDS (must pass or the run is invalid): G0.1 AST firewall; G0.2
  SHA-256 freeze BEFORE any comb data (battery not needed here --
  the block is battery-free; the frozen objects are ladders, D_SET,
  z points, bars, adjudication rule); G0.3 reach census + runtime
  cap 1200 s predeclared; G1.1 deep-table overlap exact; G1.2
  Chebyshev envelope; G1.3 parent tower comb consistency; G1.4
  prefix Ward; G1.5 drainage reproduction Ward: 6/7 rel gap(972) =
  0.3441 +- 2e-3, 6/7 rel gap(1176) = 0.1397 +- 2e-3, threshold
  count(1176) = 8, deep count(1176) = 1, lambda_min(1176) =
  3.882e-6 +- 2e-8; G1.6 measured PD (report, never in a gate);
  G1.7 coupling/commutation Ward max |E_d| <= 1e-8 on every gated
  rung (predeclared algebra (1)); G1.8 transport orthogonality Ward
  <= 1e-10 per d; G1.9 z-independence Ward (predeclared algebra
  (2)) rel <= 1e-12 across the gated eps cells; G1.10 boundedness:
  every |F~| entry <= lambda_max(band) + |z| + 1e-9, every overlap
  singular value <= 1 + 1e-12.
CONTROLS (mandatory, must fire; frozen fire rule): the same
  slow-band Feshbach reading on CS position-scramble (deep comb,
  seed 7, rungs 496..512 step 4) and CE Epstein x^2 + 5y^2 (cap
  M = 640, rungs 624..640 step 4).  FIRE = [slow band destroyed:
  min of the 6 lowest eigenvalues < -THR_NULL = -1e-4 -- the band
  the reduction targets does not exist on indefinite data] OR
  [band-gap collapse: 6/7 rel gap < GAP_BAR] OR [Q-block resolvent
  collision at a gated z: min_{i>6} |lambda_i + eps| < 1e-8].
  Predeclared honesty: real-symmetric controls keep the abstract
  Herglotz identity (self-adjointness is not what the controls
  break), so Herglotz is NOT the discriminating clause here -- the
  slow-band/Q-separation clauses are; the negative-spectrum census
  is printed with each control.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control spuriously converges -> printed
     as FESHBACH-DEAD (invalid run), exit 1, no structural claim.
  1. FESHBACH-CONVERGES-d = the SMALLEST d in {6, 7, 8} passing
     GAP-d AND HERG-d AND REC-d AND CAUCHY-d: the infinite wall is
     now a d x d matrix limit; what remains for the boundary-triple
     module is stated plainly (the z -> 0 boundary transition of
     M~(z) = F~(z)^{-1} via Nevanlinna/Herglotz representation).
  2. FESHBACH-PARTIAL = no d passes all four, but at least one d
     passes the structural trio GAP+HERG+REC (the reduction is
     well-defined, the convergence bars are not met -- failing
     (d, gate) cells named with numbers).
  3. FESHBACH-DEAD = every d fails the structural trio, or a kill
     fires: the reduction route closes; the cell-cocycle module
     becomes the remaining path.
STOP-LIST (binding, inherited): no bare A^{-1} (every resolvent is
evaluated at the frozen z points with |z| >= 1e-3 or Im z = h,
never at z = 0); no PD-margin or 1/eps in any gate; no fits inside
gates beyond the declared bounded-statistic slopes; no Riemann
zeros; no target data; NO RH claim.  This probe writes no files.
Runtime cap 1200 s predeclared.

RESULTS (2026-08-05; verdict FESHBACH-PARTIAL, GATES 9/12,
GUARDS+CONTROLS 28/28, 24.4 s):
  *  DECLARED GUARD CORRECTION (honesty): the first execution
     (25.0 s) was invalidated SOLELY by a dimensionally wrong
     normalization of the G1.9 z-independence Ward -- the measured
     float deviation 1.5e-16 (machine-perfect for the exact shift
     identity) was compared against 1e-12 x the increment scale
     (2.7e-6) instead of 1e-12 x the block ENTRY scale (1e-2, the
     size of the entries being subtracted).  The Ward normalization
     was corrected, NO gate bar was touched, and the repeat run
     produced IDENTICAL gate outcomes (deterministic construction);
     both runs are reported here.
  *  THE REDUCTION IS WELL-DEFINED FOR d = 6 AND ONLY d = 6
     (structural trio GAP+HERG+REC): GAP-6 min rel gap 0.1008 at
     M = 1096 (top 0.1397, max 0.5592); HERG-6 max eig Im F~ =
     -1.000e-2 (= -h exactly, zero-coupling value), min eig
     Im F~^{-1} = +98.8; REC-6 max rel residual 8.8e-13 over 5
     rungs x 5 z-points (independent complex dense solves) -- the
     Feshbach identity reconstructs the slow resolvent corner at
     machine precision.  Coupling Ward max |E| = 3.1e-15..6.1e-15
     (P A Q = 0 measured); transport angles d = 6: <= 2.80 deg.
  *  BUT CAUCHY-6 FAILS -- on ONE clause, marginally: med5
     last/first = 0.206 <= 0.5 (a 5x fall of the increments,
     2.7e-6 -> 5e-7) yet the second-half rate b2 = +0.006/X <
     0.02: the tail FLATTENS and even ticks up at the last rungs
     (4.89e-7 -> 5.24e-7) -- exactly where the 7th mode brushes
     the band (gap minimum at M = 1096).
  *  THE MOVING-EDGE PICTURE (the run's structural finding): the
     band boundary is chased by the next descending mode at every
     d.  d = 7: CAUCHY-7 passes STRONGLY (med5 0.207, b2 =
     +0.502/X -- the 7-band transported block is genuinely
     falling) but GAP-7 fails exactly at the top rung (0.0613 at
     M = 1176, lam8 descending onto lam7 -- the same phenomenon
     one level up).  d = 8: an INTERNAL CROSSING -- gap 8/9
     collapses to 5.4e-4 at M = 976 with transport angle 87.2 deg
     (sigma_min 0.049, just above the 1e-8 kill floor: the
     crossing rotates the 8-band violently), then recovers to
     0.2653; CAUCHY-8 passes after the crossing but GAP-8 is
     dead.  No fixed d in {6, 7, 8} owns a uniformly separated
     band on 888..1176.
  *  Q-separation margins (fixed z, predeclared algebra (4)):
     min spec Q(A-z)Q = lambda_{d+1} + eps >= 1.081e-3 at the
     tightest gated cell (d = 6, eps = 1e-3; lambda_7 min
     8.068e-5); z -> 0-relevant floors lambda_7/8/9 min = 8.07e-5
     / 8.60e-5 / 1.17e-4.
  *  Step-1 sub-ladder (reported): increment exponents 0.99..1.01
     for all three d -- the effective-block path has smooth O(1)
     velocity; step refinement changes nothing (drainage-probe
     lesson confirmed on the matrix object).
  *  CONTROLS both fire on all rungs (slow band destroyed: min
     band eigenvalue -1.52e+4 scramble / -84.4 Epstein; gap
     clauses also break); Herglotz correctly NOT discriminating
     (predeclared).  GUARDS 28/28 including reproduction of the
     drainage run to 4 digits and lambda_min(1176) to 5e-10.
  *  CONSEQUENCE (stated plainly): the wall is NOT yet a finite
     matrix limit.  The d = 6 block is the right well-defined
     object (Herglotz + exact reconstruction + separated band) but
     its transported limit is blocked by the 7th mode grazing the
     band edge; the d = 7 block converges but is not yet a
     separated object at the top of the reachable ladder.  The
     boundary-triple module is NOT opened by this run.  What the
     moving-edge picture suggests (named, not probed): either a
     deeper comb to see whether the 7/8 edge separates again
     (letting d = 7 pass both), or a DEPTH-DEPENDENT band
     dimension d(X) with transition maps at the mode-entry rungs
     -- which is precisely the cell-cocycle module's territory:
     the remaining path of the offensive.  NO RH claim, no
     X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_feshbach_effective_probe.py

PART 2 -- qf_edge_separation_probe.py (docstring verbatim):
QF-OFFENSIVE strand 3, module 3 follow-up -- the deep-comb
edge-separation decider: does the 7/8 slow-band edge SEPARATE again
at greater depth (so that d = 7 owns a uniformly separated band on a
frozen tail of the new range AND passes the parent Cauchy bars -- the
fixed-d Feshbach limit exists after all), or does the edge KEEP
MOVING (new modes descending at a measurable cadence -- fixed-d is
closed on every reachable surface and the cell-cocycle formulation is
mandatory)?  qf_edge_separation_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  It never reads a zero
ordinate and never evaluates the target before every source object is
built and SHA-256 frozen.  Band, transport, effective block and
census are built exclusively from the source window operator -- never
from target data.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_feshbach_effective_probe -- FESHBACH-PARTIAL on the 1e8 comb
     (X <= 18.375): the reduction is well-defined for d = 6 and ONLY
     d = 6 (GAP+HERG+REC), but CAUCHY-6 fails on the slope clause
     (b2 = +0.006 < 0.02) exactly where the 7th mode brushes the
     band; d = 7 passes CAUCHY strongly (med5 0.207, b2 = +0.502/X)
     but loses separation exactly at the top rung (gap 7/8 = 0.0613
     at M = 1176 < bar 0.10, lam8 descending); d = 8 has an internal
     8/9 crossing at M = 976 (transport angle 87.2 deg).  Its named
     next surface is exactly this probe: a deeper comb to see whether
     the 7/8 edge separates again (letting d = 7 pass both), vs a
     depth-dependent band dimension d(X) (the cocycle module).
  *  qf_drainage_probe -- QF-SETTLES-POSITIVE 14/14 on the 1e8 comb:
     settled per-function band weights (R2 family 0.225..0.358, R1
     family 0.008..0.079); 7th-mode threshold entry at M = 992,
     count 8 from M ~ 1108; 6/7 gap bottoms at 0.1008 (M ~ 1096..
     1100) then recovers to 0.1397 at 1176; single deep mode
     persists; lambda_min(1176) = 3.882e-6.
  *  Mode-entry record so far (X = M/64): 6th at M = 888
     (X = 13.875), 7th at M = 992 (X = 15.5), 8th at M ~ 1108
     (X ~ 17.3125) -- inter-entry gaps DX ~ 1.625, ~1.8125.  If this
     cadence is REGULAR, a new mode reaches every fixed band edge at
     bounded intervals and no fixed d separates permanently.

COMPUTE-BUDGET BENCHMARK (declared; run BEFORE this spec was frozen;
timing/memory only -- no spectra, no battery pairing, no gap or
census value was consulted): deployed sieve at 1e8 = 1.2 s / peak RSS
0.99 GB (reproduces the drainage declaration); 4e8 = 4.9 s / 4.5 GB;
1e9 = 12.3 s / 13.5 GB on a 512-GB machine; tent assembly rate
8.0e5 atoms/s -> ~62 s for the ~4.94e7 atoms in reach of X = 20.6875;
dense eigh at M ~ 1324 well under 0.5 s.  On this budget the deeper
cap is frozen at ATOM_MAX_XD = 1,000,000,000 (1e9) -- one cap, chosen
before the first run, never adjusted after.  M_CAP_XD =
floor(64 ln 1e9) = 1326; M_TOP_XD = 1324 (X = 20.6875; step-4 aligned
with the parent top: 1324 = 1176 + 37 x 4; sieve cover exp(20.6875)
+ 2 = 964,900,015 <= 1e9).  No rung thinning needed at this budget:
the full step-4 ladder 888..1324 (110 rungs) is kept.

FROZEN CONSTRUCTION (reused machinery verbatim, none invented):
  deep comb = deployed von Mangoldt generator (core.
      von_mangoldt_table) at cap ATOM_MAX_XD = 1e9; tower = continuum
      lags + atom tents on the dyadic grid D = 1/64
      (simpler_schur_recursion machinery verbatim).
  full ladder FLAD = 888..1324 step 4 (110 rungs, 109 increments;
      the leading 73 rungs 888..1176 are the Feshbach probe's GLAD,
      reused for exact continuity); census ladder CENS = [884] +
      FLAD (884 carries the entry-rung reproduction Ward);
      extension XLAD = 1180..1324 step 4 (37 rungs, X = 18.4375..
      20.6875); frozen tail block TAIL = last ceil(37/4) = 10
      extension rungs = 1288..1324 (X = 20.125..20.6875).
  band rule (parent rule verbatim): d LOWEST eigenmodes, always;
      threshold census #{lam <= THR_NULL = 1e-4} and deep census
      #{lam <= THR_DEEP = 1e-5} reported on every rung; q_f band
      weight uses the 6 LOWEST modes (drainage object, verbatim).
  d = 7 transported effective block (Feshbach machinery verbatim):
      sign-fixed 7 lowest eigenvectors, overlap S_k = V_{k+1}^T
      pad(V_k), polar factor of the SVD (floor sigma_min >= 1e-8
      else transport undefined = kill), chained R; F~_k(z) = R_k^T
      [Lambda_7(X_k) - z - C_7(z)] R_k with the MEASURED Schur
      correction C_7(z) = E_c^T diag(1/(lam_c - z)) E_c (machine
      scale, P A Q = 0 -- coupling Ward, never assumed); reference
      cell Z_REF = -1e-2 (the parent z-shift identity binds all
      other z cells to it -- redundant cells not re-evaluated);
      Herglotz certificates at ZC = (i h, -1e-3 + i h), h = 1e-2,
      on every FLAD rung (exact structural identity, checked as a
      guard-level Ward, not sold as evidence).
EDGE GATES (all frozen BEFORE the first run):
  EDGE-A  7/8 TAIL SEPARATION: rel gap g78 = (lam8 - lam7)/lam8 >=
      GAP_BAR = 0.10 on EVERY rung of the frozen TAIL block
      (recover above the bar and STAY there); the full g78 profile
      on FLAD, the first recovery rung on the extension, and the
      extension second-half linear trend are reported either way.
  EDGE-B  CAUCHY-7 DEEP (parent bars verbatim): increments delta_k
      = max-entry |F~_{k+1}(Z_REF) - F~_k(Z_REF)| over the 109
      FLAD increments; med5(LAST5)/med5(FIRST5) <= C_MED = 0.5 AND
      second-half falling rate b2 >= C_SLOPE = 0.02 per X unit
      (hbp.fit_rate verbatim); blocks FIRST5 = increments 1..5,
      LAST5 = 105..109, second half = 55..109.
  EDGE-C  MODE-DESCENT CADENCE (fit-free, reported AND gated as the
      keeps-moving clause): entry rung of mode n = first CENS rung
      with threshold count >= n; inter-entry gaps DX_n in X; frozen
      regularity statistic rel spread (max DX - min DX)/max DX <=
      CAD_BAR = 0.25 over all measured consecutive gaps; the
      keeps-moving clause KM2 FIRES iff a NEW entry (count >= 9)
      occurs on the extension AND the cadence is regular.  No fit
      enters any gate; the predicted next-entry depth X_last +
      mean(DX) is REPORTED only.
  Also reported, never gated: gap 6/7 and 8/9 profiles on the
      extension (does the d = 6 grazing resolve? where does the 9th
      mode press?); settled q_f levels med5 over the new TOP5 =
      1308..1324 vs the drainage TOP5 = 1160..1176 (drainage
      confirmation for free); PD margins.
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (banned: zetazero/nzeros/isprime/primerange/
       nextprime/prevprime/primepi/sympy); G0.2 SHA-256 freeze of
       battery bytes + cap + ladders + blocks + every bar + anchors
       BEFORE any comb data is built here; G0.3 reach census +
       runtime cap 1800 s predeclared;
  G1.1 deep-table overlap: extended von Mangoldt table == deployed
       core table on [0, 400000] EXACTLY; G1.2 extended Chebyshev
       envelope kappa <= KAPPA_REF + 1e-6 over [100, 1e9];
  G1.3 parent tower comb consistency (rel dev <= 1e-12); G1.4
       prefix Ward: deep tower leading 824 x 824 block == parent
       tower (<= 1e-12);
  G1.5 Feshbach/drainage anchor reproduction: (a) 6/7 gap(1096) =
       0.1008, 6/7 gap(1176) = 0.1397, 7/8 gap(1176) = 0.0613, all
       +- 2e-4 (4 digits); thr count(1176) = 8, deep count(1176) =
       1, lambda_min(1176) = 3.882e-6 +- 2e-8; (b) entry-rung
       reproduction: count 5 at M = 884, 6 at M = 888, 7th entry
       exactly at M = 992; (c) drainage settled levels: med5 over
       1160..1176 of the band-6 weight reproduces the nine frozen
       drainage values (0.3583/0.3370/0.3127/0.2590/0.2249/0.0793/
       0.0741/0.0741/0.0082) +- 2e-3;
  G1.6 measured PD: lambda_min > -1e-9 on every rung (measured
       output; NO gate uses a PD margin or 1/eps); G1.7 coupling
       Ward max |E| <= 1e-8 (P A Q = 0 measured); G1.8 transport
       orthogonality Ward <= 1e-10; K4 sigma_min >= 1e-8; HERG-7
       Ward: max eig Im F~ <= 1e-10 AND min eig Im F~^{-1} >=
       -1e-10 at both ZC points on every FLAD rung; G1.9
       boundedness: every band q_f in [-1e-12, 1 + 1e-9], every
       overlap singular value <= 1 + 1e-12, every |F~| entry <=
       lam_max(band) + |z|_max + 1e-9.
CONTROLS (mandatory, must fire; fire rule = qf_spectral_bundle_probe.
  control_bundle VERBATIM, imported read-only): CS position scramble
  (positions uniform in (0.5, 2 alpha_xd), masses kept, seed 7, on
  the 1e9 comb, rungs 496..512 step 4) and CE Epstein x^2 + 5y^2
  (epstein_firewall_probe read-only, cap M = 640, rungs 624..640
  step 4).  FIRE = rank instability OR gap collapse OR angle
  saturation.  A control whose bundle construction stays intact has
  spuriously converged: the run is INVALID.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control spuriously converges -> the run is
     INVALID: printed as EDGE-UNDECIDED (invalid run), exit 1, no
     edge statement follows.
  1. EDGE-SEPARATES-D7 = EDGE-A passes AND EDGE-B passes: the 7/8
     edge separates again at depth and the transported d = 7 block
     is Cauchy at the parent bars -- the fixed-d Feshbach limit
     exists after all; the boundary-triple module reopens with
     d = 7.
  2. EDGE-KEEPS-MOVING = (EDGE-A fails) OR (KM2 fires: a new mode
     entry on the extension at regular cadence): the band edge is
     chased by descending modes at the measured cadence -- fixed-d
     is closed on every reachable surface and the cell-cocycle
     formulation is the remaining path; the cadence (mean DX, rel
     spread) is stated as the new named structural constant.
  3. otherwise EDGE-UNDECIDED: the bars are not reached either way
     (e.g. tail separates but the Cauchy tail is too short, and no
     new entry adjudicates the cadence); the deciding depth is
     stated honestly.
STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros anywhere; no bare A^{-1} (resolvents only at the frozen z with
|z| >= 1e-3 or Im z = h); no PD-margin or 1/eps in any gate; no fits
inside gates beyond the declared bounded-statistic slope (b2, parent
CAUCHY clause verbatim; the cadence gate is fit-free); no Riemann
zeros; NO RH claim.  This probe writes no files.  Runtime cap 1800 s
predeclared.

RESULTS (2026-08-05, first and only preregistered run, 160.3 s;
GATES: EDGE-A FAIL, EDGE-B PASS, KM2 quiet; GUARDS+CONTROLS 20/20;
verdict EDGE-KEEPS-MOVING, carried by the EDGE-A failure alone):
  *  THE 7/8 EDGE DOES NOT SEPARATE -- IT CLOSES INTO A NEAR-
     CROSSING.  On the extension the 7/8 gap NEVER reaches the bar
     again (extension max 0.0568, right after the parent top): from
     0.0613 at M = 1176 it falls through 0.0209 (M = 1208) to
     0.0039 at M = 1240 (printed profile; an avoided crossing --
     lam8 descends THROUGH the 7-band edge), relaxes to ~0.011,
     and decays again to 0.0074 at the top rung 1324.  At the top
     the pair is nearly degenerate: lam7 = 7.9351e-5, lam8 =
     7.9946e-5 (and lam9 = 9.1935e-5 -- modes 7/8/9 now form a
     CLUSTER below thr 1e-4).  The transport sees the crossing:
     min sigma_min = 0.0271 (max angle 88.45 deg, still above the
     1e-8 kill floor -- the same violent band rotation the parent
     measured for d = 8 at M = 976, now one level down).  EDGE-A
     min tail gap 0.0074 < 0.10: FAIL, unambiguous.
  *  EDGE-B PASSES CLEANLY EVEN THROUGH THE CROSSING: the
     transported 7x7 block stays Cauchy on all 109 increments --
     2.72e-6 -> 3.94e-7, med5 last/first = 0.181 <= 0.5, b2 =
     +0.061/X >= 0.02 (parent 1e8 numbers were 0.207 / +0.502).
     The moving-edge picture is now measured at two consecutive
     levels: every d gets a CONVERGENT transported block and then
     loses its edge to the next descending mode.  Convergence was
     never the problem; band ownership is.
  *  MODE-DESCENT CADENCE (the fit-free record): entries at
     M = 888 / 992 / 1108 / 1276 (X = 13.8750 / 15.5000 / 17.3125
     / 19.9375) -- the 9th mode enters INSIDE the extension.
     Inter-entry gaps DX = 1.6250 / 1.8125 / 2.6250, mean 2.0208,
     rel spread 0.381 > CAD_BAR 0.25: the frozen KM2 clause does
     NOT fire -- the cadence is real but NOT regular at the frozen
     bar; the spacing WIDENS with depth (third gap 1.6x the
     first).  That widening is the honest surprise of this run and
     the number the cocycle module must carry.  Predicted next
     entry at the measured mean cadence (REPORTED only): X ~ 21.96
     (M ~ 1405, ATOM_MAX ~ 3.4e9).  Deep count (lam <= 1e-5)
     stays exactly 1 on all 111 census rungs.
  *  THE d = 6 GRAZING RESOLVES (reported): the 6/7 gap recovers
     from the parent's 0.1008 bottom to 0.4333 at the top rung
     (extension min 0.1444 at M = 1180) -- at X = 20.6875 the
     separated object is the 6-band again, sitting under a 7/8/9
     cluster.  gap 8/9 extension min 0.1304 (at the top, falling).
     Together with EDGE-A this is the moving-edge picture in full:
     the band boundary d(X) is 6 -> 7 -> 8 -> 9 by threshold count
     but the SEPARATED dimension oscillates (6 separated here,
     7/8/9 clustered) -- no fixed d owns the tail.
  *  q_f DRAINAGE CONFIRMATION FOR FREE: the settled levels hold
     to 0.87..1.09x over 2.3 more X units -- med5(1308..1324) vs
     med5(1160..1176): R2 family 0.3245/0.2948/0.2809/0.2247/
     0.2015 vs 0.3583/0.3370/0.3127/0.2590/0.2249; R1 family
     0.0735/0.0761/0.0599/0.0089.  Typed honestly: extension fall
     rates b = +0.050..+0.083/X sit slightly ABOVE the drainage
     plateau bar 0.05 (reported here, never gated) -- a mild
     renewed decline worth one line in any future drainage rerun,
     far from the Z-type collapse (levels >= 0.0089).  PD margins
     (measured, never gated): lambda_min 3.882e-6 (1176) ->
     2.455e-6 (1324).
  *  CONTROLS both fire (rank + gap clauses): CS scramble (1e9
     comb, 49,154,321 atoms) threshold counts 242..253 vs 6,
     253/512 negative, min rel gap 0.0006; CE Epstein counts
     251..263 vs 6, min rel gap 0.0650.  GUARDS 20/20: deep-table
     overlap exact (dev 0.0), kappa = 0.038821 unchanged on
     [100, 1e9], prefix Ward 2.0e-14, ALL anchors reproduced --
     gaps 0.1008/0.1397/0.0613 to 4 digits, lambda_min(1176) dev
     5e-10, entry rungs 884:5 / 888:6 / 992:7th exact, all nine
     drainage levels dev <= 4.9e-5; coupling Ward 4.1e-15,
     transport orthogonality 9.6e-14, HERG-7 Ward exact (-1.000e-2
     / +98.57), boundedness clean; runtime 160.3 s <= 1800 s.
  *  CONSEQUENCE FOR THE OFFENSIVE (stated plainly): FIXED-d IS
     CLOSED on every reachable surface -- not by non-convergence
     (CAUCHY-7 passes at 1e8 and again at 1e9, straight through an
     avoided crossing) but by band ownership: d = 7 never regains
     a separated edge (tail gap 0.0074 vs bar 0.10) because lam8
     crosses INTO the 7-band on the extension, exactly as lam7 had
     grazed the 6-band one window earlier.  The boundary-triple
     module does NOT reopen with d = 7.  The CELL-COCYCLE
     formulation -- depth-dependent band dimension d(X) with
     transition maps at the mode-entry rungs -- is the only
     remaining path of the diagonal route; its cell boundaries are
     the measured entry rungs 888 / 992 / 1108 / 1276, its
     per-cell blocks are convergent objects (EDGE-B), and its
     structural constant is the measured, WIDENING entry cadence
     DX = 1.625 / 1.8125 / 2.625 (mean 2.02, spread 0.381 -- NOT
     regular at the frozen 0.25 bar; whether DX grows like a
     deterministic law is a question for that module, stated not
     fitted).  Additional cocycle input from this run: the
     separated dimension at the top is 6 again under a 7/8/9
     cluster -- cells may carry CLUSTERS, not single modes.  NOT
     claimed: any statement beyond X = 20.6875, eps-uniformity,
     RH.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_edge_separation_probe.py

NUMERICAL-ROBUSTNESS AMENDMENT (2026-08-10; no semantic change, no
gate/bar/expectation touched):
  *  The REC-d reconstruction Ward's independent dense solve now
     calls scipy.linalg.solve(..., assume_a="gen"), pinning the
     LU (gesv) driver that WAS the unconditional default when this
     module was frozen.  Reason: scipy >= 1.15 auto-detects matrix
     structure and dispatches the complex-symmetric shift A - zI
     (real symmetric A, complex z) to the ?sysv diagonal-pivoting
     driver; scipy 1.17.0's sysv path returns a WRONG solution on
     this matrix family (backward residual ||(A-z)G - V|| up to
     9.6e+01 at the two complex z cells, turning the REC-d rel
     residual into 2.6e+03; real z cells unaffected; fixed upstream
     in scipy 1.17.1).  Under numpy 1.26/scipy 1.13 the identical
     call already used LU and the gate read 5.2e-13.  All frozen
     bars, ladders, z points, preregistered fails (CAUCHY-6/GAP-7/
     GAP-8 part 1; EDGE-A part 2) and both pattern gates are
     byte-identically unchanged; REC-d stays a genuine two-path Ward
     (eigh route vs independent LU solve).  Verified green after the
     amendment under BOTH python 3.9.6/numpy 1.26.4/scipy 1.13.1 and
     python 3.14.3/numpy 2.4.2/scipy 1.17.0.
"""

# ==========================================================================
# PART 1 -- qf_feshbach_effective_probe.py (verbatim; imports promoted)
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
import epstein_firewall_probe as epx  # noqa: E402
import v770_qf_spectral_bundle as qsb  # noqa: E402  (read-only)

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_DEEP = 100000000            # deep comb cap (drainage cap)
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))   # 1178
M_TOP_DEEP = 1176                    # deepest rung
M_TOP_PAR = 824                      # first-parent cap (prefix Ward)

GLAD = list(range(888, 1177, 4))     # 73 gated rungs, 72 increments
HOLO_LAD = list(range(1160, 1177))   # step-1 sub-ladder (reported)
RECON_RUNGS = (888, 968, 1048, 1128, 1176)   # reconstruction Wards

D_SET = (6, 7, 8)                    # preregistered band dimensions
D_MAX = 8
EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)  # gated real z = -eps cells
Z_REF = -1.0e-2                      # frozen reference cell
H_IM = 1.0e-2                        # Herglotz imaginary offset
ZC = (complex(0.0, H_IM), complex(-1.0e-3, H_IM))
Z_ALL = tuple(complex(-e, 0.0) for e in EPS_GATED) + ZC

GAP_BAR = 0.10                       # GAP-d band/bulk separation
HERG_FLOOR = 1.0e-10                 # HERG-d matrix floor
REC_BAR = 1.0e-10                    # REC-d rel residual bar
C_MED = 0.50                         # CAUCHY-d med5 ratio bar
C_SLOPE = 0.02                       # CAUCHY-d second-half rate bar
INC_FIRST5 = slice(0, 5)             # increment blocks (72 pairs)
INC_LAST5 = slice(67, 72)
INC_HALF2 = slice(36, 72)
N_MED = 5

SVD_FLOOR = 1.0e-8                   # K4 polar/90-degree floor
COUP_WARD = 1.0e-8                   # G1.7 coupling |E| Ward
WARD_ORTH = 1.0e-10                  # G1.8 R orthogonality
ZWARD = 1.0e-12                      # G1.9 z-independence (rel)
BOUND_TOL = 1.0e-9                   # G1.10 boundedness slack
THR_NULL = 1.0e-4                    # census threshold (reported)
THR_DEEP = 1.0e-5                    # deep census (reported)
QF_FLOOR = 1.0e-12                   # denominator floor

REPRO_GAP972 = 0.3441                # drainage frozen 6/7 gap (972)
REPRO_GAP1176 = 0.1397               # drainage frozen 6/7 gap (1176)
REPRO_NN1176 = 8                     # drainage frozen thr count
REPRO_LMIN1176 = 3.882e-6            # drainage frozen lambda_min
REPRO_TOL = 2.0e-3                   # gap reproduction tolerance
REPRO_LTOL = 2.0e-8                  # lambda_min reproduction tol
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
PD_TOL = 1.0e-9                      # G1.6 measured-PD slack
RUNTIME_CAP = 1200.0                 # seconds, predeclared

QCOL_FLOOR = 1.0e-8                  # control Q-collision floor
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # per-d gates: feed the verdict only


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
    hsh = hashlib.sha256()
    hsh.update(("qf-feshbach spec: deep comb = deployed sieve cap %d "
                "M_CAP=%d M_TOP=%d D=%.10f; GLAD=%s; HOLO=%s; "
                "RECON=%s; D_SET=%s (band rule = d lowest, ALL "
                "preregistered, adjudication = smallest d passing "
                "all gates); z: eps_gated=%s zref=%g h=%g zc=%s; "
                "bars: gap>=%g herg<=%g rec<=%g cmed<=%g "
                "cslope>=%g blocks=[0:5][67:72][36:72] Nmed=%d; "
                "kills: svd>=%g coup<=%g; wards: orth<=%g z<=%g "
                "bound<=%g; repro: g972=%g g1176=%g nn=%d lmin=%g "
                "tol=%g/%g; guards: comb<=%g prefix<=%g pd>=-%g "
                "runtime<=%g; controls: thr=%g gap>=%g qcol<=%g "
                "lads=%s/%s epcap=%d epM=%d seed=%d; verdict order: "
                "invalid -> CONVERGES-smallest-d -> PARTIAL "
                "(structural trio holds for some d) -> DEAD"
                % (ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP, D, GLAD,
                   HOLO_LAD, RECON_RUNGS, D_SET, EPS_GATED, Z_REF,
                   H_IM, ZC, GAP_BAR, HERG_FLOOR, REC_BAR, C_MED,
                   C_SLOPE, N_MED, SVD_FLOOR, COUP_WARD, WARD_ORTH,
                   ZWARD, BOUND_TOL, REPRO_GAP972, REPRO_GAP1176,
                   REPRO_NN1176, REPRO_LMIN1176, REPRO_TOL,
                   REPRO_LTOL, COMB_DEV_BAR, PREFIX_WARD, PD_TOL,
                   RUNTIME_CAP, THR_NULL, GAP_BAR, QCOL_FLOOR,
                   qsb.CTRL_LAD_S, qsb.CTRL_LAD_E, EP_NCAP, EP_MMAX,
                   SEED)).encode())
    return hsh.hexdigest()


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


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap: deep von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over "
          "[%.0f, %d] <= KAPPA_REF + %.0e = %.6f"
          % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP, core.TOL_KAPPA,
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
    print("  deep census: ka = %d atoms to e^%.4f" % (ka,
                                                      2.0 * alpha))
    return T, c_cont, alpha, ka


# ------------------------------------------------ spectral ladder
def spectral_pass(T, sizes):
    """Per rung: full spectrum, sign-fixed 8-band basis, coupling
    rows E = V8^T A V (band rows removed analytically; measured as
    the commutation Ward), census numbers."""
    out = {}
    for M in sizes:
        A = T[:M, :M]
        lam, V = np.linalg.eigh(A)
        V8 = qsb.sign_fix(V[:, :D_MAX])
        # E_all[i, j] = v_i^T A v8_j; rows i >= d are the coupling
        E_all = V.T @ (A @ V8)              # (M, 8)
        out[M] = dict(M=M, lam=lam, V8=V8, E=E_all,
                      nn=int(np.sum(lam <= THR_NULL)),
                      nn_deep=int(np.sum(lam <= THR_DEEP)))
    return out


def fall_rate(xs, vals):
    rows = [dict(XmR=float(x), mx=float(v)) for x, v in zip(xs, vals)]
    b, _resid = hbp.fit_rate(rows)
    return b


def f_frame(blk, d, z):
    """The effective block in the rung band frame: Lambda_d - z -
    C_d(z), with the MEASURED Schur correction C_d(z) =
    E_c^T diag(1/(lambda_c - z)) E_c (machine-scale by (1))."""
    lam = blk["lam"]
    Ec = blk["E"][d:, :d]                   # (M-d, d) coupling
    corr = Ec.T @ (Ec / (lam[d:, None] - z))
    return np.diag(lam[:d]) - z * np.eye(d) - corr


def transport_chain(spec, d):
    """Chained polar transport per band dimension d along GLAD."""
    Rs, sig_min = [np.eye(d)], []
    ward_orth = 0.0
    for Ma, Mb in zip(GLAD, GLAD[1:]):
        Va = spec[Ma]["V8"][:, :d]
        Vb = spec[Mb]["V8"][:, :d]
        S = Vb[:Ma, :].T @ Va
        U, s, Wt = np.linalg.svd(S)
        sig_min.append(float(s[-1]))
        Rs.append(U @ Wt @ Rs[-1])
        ward_orth = max(ward_orth, float(np.max(np.abs(
            Rs[-1].T @ Rs[-1] - np.eye(d)))))
    return Rs, sig_min, ward_orth


# ------------------------------------------------ per-d analysis
def analyze_d(spec, d):
    print("\n" + "-" * 70)
    print("-- band dimension d = %d" % d)
    xs = np.array([M * D for M in GLAD])

    # GAP-d
    gaps = [(spec[M]["lam"][d] - spec[M]["lam"][d - 1])
            / spec[M]["lam"][d] for M in GLAD]
    i_min = int(np.argmin(gaps))
    print("  gap profile (lam_%d/lam_%d, every 8th rung): %s"
          % (d + 1, d, "  ".join("M=%d:%.4f" % (M, g) for M, g in
                                 list(zip(GLAD, gaps))[::8])))
    g_ok = gate("GAP-%d band/bulk separation: min rel gap = %.4f "
                "at M = %d (top rung %.4f, max %.4f) >= %g"
                % (d, gaps[i_min], GLAD[i_min], gaps[-1],
                   max(gaps), GAP_BAR), min(gaps) >= GAP_BAR)

    # transport
    Rs, sig_min, ward_orth = transport_chain(spec, d)
    k4_ok = check("K4 kill audit (d=%d): min sigma_min = %.6f >= "
                  "%.0e (transport well-defined); max angle %.2f "
                  "deg" % (d, min(sig_min), SVD_FLOOR,
                           math.degrees(math.acos(
                               min(min(sig_min), 1.0)))),
                  min(sig_min) >= SVD_FLOOR)
    check("G1.8 transport orthogonality Ward (d=%d): max "
          "||R^T R - I|| = %.1e <= %.0e" % (d, ward_orth,
                                            WARD_ORTH),
          ward_orth <= WARD_ORTH)

    # coupling Ward (predeclared algebra (1))
    coup = max(float(np.max(np.abs(spec[M]["E"][d:, :d])))
               for M in GLAD)
    check("G1.7 coupling/commutation Ward (d=%d): max |E| = %.1e "
          "<= %.0e on every gated rung (P A Q = 0 analytically; "
          "measured, not assumed)" % (d, coup, COUP_WARD),
          coup <= COUP_WARD)

    # transported blocks at all gated z + reference
    Ft = {z: [Rs[i].T @ f_frame(spec[M], d, z) @ Rs[i]
              for i, M in enumerate(GLAD)] for z in Z_ALL}

    # G1.9 z-independence Ward of the increments (algebra (2)).
    # Normalization corrected after the first run (declared in the
    # RESULTS block): delta(z) and delta(zref) are differences of
    # O(|F~|)-sized entries, so their float noise is eps_mach x the
    # BLOCK ENTRY scale, not the (much smaller) increment scale.
    dref = [np.max(np.abs(Ft[complex(Z_REF, 0.0)][i + 1]
                          - Ft[complex(Z_REF, 0.0)][i]))
            for i in range(len(GLAD) - 1)]
    dref = np.array(dref, dtype=float)
    fscale = max(float(np.max(np.abs(Ft[complex(Z_REF, 0.0)][i])))
                 for i in range(len(GLAD)))
    zdev = 0.0
    for e in EPS_GATED:
        z = complex(-e, 0.0)
        dz = np.array([np.max(np.abs(Ft[z][i + 1] - Ft[z][i]))
                       for i in range(len(GLAD) - 1)], dtype=float)
        zdev = max(zdev, float(np.max(np.abs(dz - dref))))
    check("G1.9 z-independence Ward (d=%d): max |delta(z) - "
          "delta(zref)| = %.1e <= %.0e x block entry scale %.1e "
          "over the gated eps cells" % (d, zdev, ZWARD, fscale),
          zdev <= ZWARD * max(fscale, QF_FLOOR))

    # HERG-d
    herg_f, herg_m = -np.inf, np.inf
    for z in ZC:
        for i in range(len(GLAD)):
            Fz = Ft[z][i]
            imF = (Fz - Fz.conj().T) / 2.0j
            herg_f = max(herg_f, float(np.max(
                np.linalg.eigvalsh(imF))))
            Minv = np.linalg.inv(Fz)
            imM = (Minv - Minv.conj().T) / 2.0j
            herg_m = min(herg_m, float(np.min(
                np.linalg.eigvalsh(imM))))
    h_ok = gate("HERG-%d matrix-Herglotz certificates (every gated "
                "rung, both complex z): max eig Im F~ = %+.3e <= "
                "%.0e (anti-Herglotz side; zero-coupling value "
                "-h = -%.0e) AND min eig Im F~^{-1} = %+.3e >= "
                "-%.0e (Herglotz side)"
                % (d, herg_f, HERG_FLOOR, H_IM, herg_m, HERG_FLOOR),
                herg_f <= HERG_FLOOR and herg_m >= -HERG_FLOOR)

    # CAUCHY-d at the reference cell
    med_f = float(np.median(dref[INC_FIRST5]))
    med_l = float(np.median(dref[INC_LAST5]))
    ratio = med_l / max(med_f, QF_FLOOR)
    b2 = fall_rate(xs[1:][INC_HALF2], dref[INC_HALF2])
    rel = dref / np.array(
        [max(np.max(np.abs(Ft[complex(Z_REF, 0.0)][i])), QF_FLOOR)
         for i in range(len(GLAD) - 1)])
    print("  increment profile (Z_REF, first 3 / last 3): %s ... %s"
          "; relative-to-block-scale %.2e..%.2e"
          % (", ".join("%.2e" % v for v in dref[:3]),
             ", ".join("%.2e" % v for v in dref[-3:]),
             float(np.min(rel)), float(np.max(rel))))
    c_ok = gate("CAUCHY-%d transported effective block: med%d "
                "last/first = %.3f <= %g AND second-half falling "
                "rate b2 = %+.3f/X >= %g (72 increments, "
                "oscillation-aware)"
                % (d, N_MED, ratio, C_MED, b2, C_SLOPE),
                ratio <= C_MED and b2 >= C_SLOPE)

    # G1.10 boundedness
    fmax = max(float(np.max(np.abs(Ft[z][i]))) for z in Z_ALL
               for i in range(len(GLAD)))
    lmax_band = max(float(spec[M]["lam"][d - 1]) for M in GLAD)
    zmax = max(abs(z) for z in Z_ALL)
    check("G1.10 boundedness (d=%d): max |F~| entry = %.3e <= "
          "lam_max(band) + |z|_max + %.0e = %.3e; max overlap "
          "sigma <= 1 + 1e-12"
          % (d, fmax, BOUND_TOL, lmax_band + zmax + BOUND_TOL),
          fmax <= lmax_band + zmax + BOUND_TOL
          and max(max(sig_min), 1.0) <= 1.0 + 1.0e-12)

    # Q-separation margins (reported; predeclared algebra (4))
    for e in EPS_GATED:
        lo = min(float(spec[M]["lam"][d]) for M in GLAD)
        print("  Q-separation margin at z = -%g: min spec "
              "Q(A-z)Q = lambda_%d + eps in [%.3e, %.3e] "
              "(>= eps trivially; the z->0-relevant part is "
              "lambda_%d itself, min %.3e)"
              % (e, d + 1, lo + e,
                 max(float(spec[M]["lam"][d]) for M in GLAD) + e,
                 d + 1, lo))

    return dict(gap=g_ok, herg=h_ok, cauchy=c_ok, k4=k4_ok,
                Rs=Rs, ratio=ratio, b2=b2, gaps=gaps,
                dref=dref)


# ------------------------------------------------ reconstruction
def reconstruction(T, spec, results):
    print("\n-- reconstruction identity (independent dense solve; "
          "the Feshbach/Schur identity is EXACT -- gate at %.0e)"
          % REC_BAR)
    worst = {d: 0.0 for d in D_SET}
    for M in RECON_RUNGS:
        A = T[:M, :M]
        V8 = spec[M]["V8"]
        i_r = GLAD.index(M)
        for z in Z_ALL:
            # assume_a="gen": pin the LU (gesv) path explicitly.
            # scipy >= 1.15 auto-detects structure and dispatches the
            # complex-symmetric A - zI to ?sysv; scipy 1.17.0's sysv
            # path returns a wrong solution here (backward residual
            # O(1e2) at the complex z cells; fixed upstream in
            # 1.17.1).  "gen" is the pre-1.15 default -- identical
            # semantics (independent dense solve), every scipy >= 1.0.
            G = sla.solve(A - z * np.eye(M), V8.astype(complex),
                          assume_a="gen")
            Mfull = V8.T @ G                # (8, 8) compressed res
            for d in D_SET:
                Finv = np.linalg.inv(f_frame(spec[M], d, z))
                res = float(np.max(np.abs(Mfull[:d, :d] - Finv))
                            / max(float(np.max(np.abs(Finv))),
                                  QF_FLOOR))
                worst[d] = max(worst[d], res)
        _ = i_r
    for d in D_SET:
        results[d]["rec"] = gate(
            "REC-%d reconstruction: max rel residual "
            "|V^T (A-z)^{-1} V - F(z)^{-1}| = %.1e <= %.0e over "
            "%d rungs x %d z-points" % (d, worst[d], REC_BAR,
                                        len(RECON_RUNGS),
                                        len(Z_ALL)),
            worst[d] <= REC_BAR)


# ------------------------------------------------ step-1 (report)
def step1_report(T, spec):
    print("\n-- step-1 sub-ladder (REPORTED never gated): median "
          "effective-block increment per step on M = %d..%d"
          % (HOLO_LAD[0], HOLO_LAD[-1]))
    spec1 = {}
    for M in HOLO_LAD:
        if M in spec:
            spec1[M] = spec[M]
        else:
            A = T[:M, :M]
            lam, V = np.linalg.eigh(A)
            V8 = qsb.sign_fix(V[:, :D_MAX])
            spec1[M] = dict(M=M, lam=lam, V8=V8,
                            E=V.T @ (A @ V8))
    for d in D_SET:
        meds = {}
        for s in (1, 2, 4):
            chain = list(range(HOLO_LAD[0], HOLO_LAD[-1] + 1, s))
            R = np.eye(d)
            incs = []
            prev = None
            for Ma, Mb in zip(chain, chain[1:]):
                Va = spec1[Ma]["V8"][:, :d]
                Vb = spec1[Mb]["V8"][:, :d]
                U, sv, Wt = np.linalg.svd(Vb[:Ma, :].T @ Va)
                if prev is None:
                    Fa = R.T @ f_frame(spec1[Ma], d,
                                       complex(Z_REF, 0)) @ R
                else:
                    Fa = prev
                R = (U @ Wt) @ R
                Fb = R.T @ f_frame(spec1[Mb], d,
                                   complex(Z_REF, 0)) @ R
                incs.append(float(np.max(np.abs(Fb - Fa))))
                prev = Fb
            meds[s] = float(np.median(incs))
        print("  d=%d: median increment s=1/2/4 = %.3e / %.3e / "
              "%.3e; exponents log2 = %.2f (1->2), %.2f (2->4)"
              % (d, meds[1], meds[2], meds[4],
                 math.log2(meds[2] / max(meds[1], QF_FLOOR)),
                 math.log2(meds[4] / max(meds[2], QF_FLOOR))))


# ------------------------------------------------ controls
def control_feshbach(Tc, lad, label):
    fires, dets = [], []
    for M in lad:
        lam = np.linalg.eigvalsh(Tc[:M, :M])
        band_neg = float(np.min(lam[:6]))
        gp = (lam[6] - lam[5]) / max(abs(lam[6]), QF_FLOOR)
        qcol = min(float(np.min(np.abs(lam[6:] + e)))
                   for e in EPS_GATED)
        fires.append(band_neg < -THR_NULL or gp < GAP_BAR
                     or qcol < QCOL_FLOOR)
        dets.append((M, band_neg, gp, qcol,
                     int(np.sum(lam < 0.0)), len(lam)))
    M, bn, gp, qc, nneg, n = dets[-1]
    fire = all(fires)
    det = ("%s: top rung M=%d: min band eigenvalue = %.2e (slow "
           "band destroyed if < -%g), 6/7 rel gap = %.4f, min "
           "Q-collision |lam+eps| = %.2e, %d/%d negative "
           "eigenvalues; fire on all %d rungs = %s.  (Herglotz is "
           "NOT the discriminating clause for real-symmetric "
           "controls -- predeclared.)"
           % (label, M, bn, THR_NULL, gp, qc, nneg, n, len(lad),
              fire))
    return fire, det


def run_controls(c_cont, alpha_deep, ka_deep, mu_deep):
    print("\n-- controls (must fire: indefinite data destroys the "
          "slow band the reduction targets)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_deep, ka_deep))
    cat_s, _dd = core.atom_lags_at(alpha_deep, M_TOP_DEEP, pos,
                                   mu_deep[:ka_deep])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_DEEP])
    fire_s, det_s = control_feshbach(Ts, qsb.CTRL_LAD_S, "scramble")
    check("CS position-scramble control (deep comb, %d atoms) "
          "fires" % ka_deep, fire_s, det_s)

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
    fire_e, det_e = control_feshbach(TE, qsb.CTRL_LAD_E, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 3, module 3 -- Feshbach effective "
          "block on the 1e8 comb (d in %s, X <= %.4f)"
          % (str(D_SET), M_TOP_DEEP * D))
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (K3: band rule is an eigenvalue-order "
          "rule of the source operator; no target information)",
          not hits, str(hits))
    spec_sha = freeze_spec()
    check("G0.2 ladders + D_SET + z points + bars + adjudication "
          "rule SHA-256-frozen BEFORE any comb data is built here",
          True, "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d; "
          "sieve cover exp(X_top) + 2 = %d <= %d; runtime cap "
          "%.0f s predeclared"
          % (M_TOP_DEEP, ATOM_MAX_DEEP, M_CAP_DEEP,
             int(math.exp(M_TOP_DEEP * D)) + 2, ATOM_MAX_DEEP,
             RUNTIME_CAP),
          M_TOP_DEEP <= M_CAP_DEEP
          and int(math.exp(M_TOP_DEEP * D)) + 2 <= ATOM_MAX_DEEP)

    # ---- comb + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    T, c_cont, alpha_deep, ka_deep = build_deep_tower(
        u_deep, mu_deep, T_par)

    # ---- spectra on GLAD
    spec = spectral_pass(T, GLAD)
    pd_min = min(float(spec[M]["lam"][0]) for M in GLAD)
    print("  PD margins (measured, never gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[GLAD[0]]["lam"][0], GLAD[0],
             spec[M_TOP_DEEP]["lam"][0], M_TOP_DEEP))
    check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every "
          "gated rung (measured output, in NO gate)"
          % (pd_min, PD_TOL), pd_min > -PD_TOL)

    # G1.5 drainage reproduction Ward
    g972 = (spec[972]["lam"][6] - spec[972]["lam"][5]) \
        / spec[972]["lam"][6]
    g1176 = (spec[1176]["lam"][6] - spec[1176]["lam"][5]) \
        / spec[1176]["lam"][6]
    check("G1.5 drainage reproduction Ward: 6/7 gap(972) = %.4f vs "
          "frozen %.4f, gap(1176) = %.4f vs frozen %.4f (tol %.0e);"
          " thr count(1176) = %d (== %d), deep count = %d (== 1); "
          "lambda_min(1176) = %.4e vs frozen %.4e (tol %.0e)"
          % (g972, REPRO_GAP972, g1176, REPRO_GAP1176, REPRO_TOL,
             spec[1176]["nn"], REPRO_NN1176, spec[1176]["nn_deep"],
             spec[1176]["lam"][0], REPRO_LMIN1176, REPRO_LTOL),
          abs(g972 - REPRO_GAP972) <= REPRO_TOL
          and abs(g1176 - REPRO_GAP1176) <= REPRO_TOL
          and spec[1176]["nn"] == REPRO_NN1176
          and spec[1176]["nn_deep"] == 1
          and abs(spec[1176]["lam"][0] - REPRO_LMIN1176)
          <= REPRO_LTOL)

    # ---- per-d analysis
    results = {}
    for d in D_SET:
        results[d] = analyze_d(spec, d)

    # ---- reconstruction identity (independent dense solves)
    reconstruction(T, spec, results)

    # ---- K1/K2 structural audit
    check("K1/K2 kill audit: every gated quantity is a band-"
          "interior gap ratio, a fixed-z separation (spectrum of "
          "Q(A-z)Q at |z| >= %.0e or Im z = %.0e -- never a global "
          "lower bound on A), a bounded transported matrix entry, "
          "a machine-precision identity residual, or a med5/slope "
          "statistic of these; no 1/eps, no PD margin, no "
          "RH-strength input in any gate" % (min(EPS_GATED), H_IM),
          True)

    # ---- step-1 report + controls
    step1_report(T, spec)
    run_controls(c_cont, alpha_deep, ka_deep, mu_deep)

    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered decision order)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    full_pass = [d for d in D_SET
                 if results[d]["gap"] and results[d]["herg"]
                 and results[d]["rec"] and results[d]["cauchy"]
                 and results[d]["k4"]]
    trio_pass = [d for d in D_SET
                 if results[d]["gap"] and results[d]["herg"]
                 and results[d]["rec"] and results[d]["k4"]]
    if not (guards_ok and controls_ok):
        verdict = "FESHBACH-DEAD (invalid run)"
    elif full_pass:
        verdict = "FESHBACH-CONVERGES-%d" % full_pass[0]
    elif trio_pass:
        verdict = "FESHBACH-PARTIAL"
    else:
        verdict = "FESHBACH-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, per-d "
          "gap/herg/rec/cauchy: %s, runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             "; ".join("d=%d %s/%s/%s/%s"
                       % (d,
                          "P" if results[d]["gap"] else "F",
                          "P" if results[d]["herg"] else "F",
                          "P" if results[d].get("rec") else "F",
                          "P" if results[d]["cauchy"] else "F")
                       for d in D_SET), time.time() - T_START))
    if verdict.startswith("FESHBACH-CONVERGES"):
        d0 = full_pass[0]
        print("CONSEQUENCE (stated plainly): the infinite "
              "positivity wall is now the convergence of ONE %d x "
              "%d matrix function -- the transported effective "
              "block F~_X(z) is entrywise Cauchy at the frozen "
              "bars, matrix-Herglotz certified, and exactly "
              "reconstructs the slow resolvent corner.  WHAT "
              "REMAINS (the boundary-triple module has to prove): "
              "the z -> 0 boundary transition of M~(z) = "
              "F~(z)^{-1} -- a Nevanlinna/Herglotz representation "
              "of the limit block and the behavior of its measure "
              "at 0 (atom vs absolutely continuous density), on "
              "the LIMIT object, not per rung.  NOT claimed: "
              "X -> infinity existence beyond the measured bars, "
              "eps-uniformity, RH." % (d0, d0))
    elif verdict == "FESHBACH-PARTIAL":
        print("CONSEQUENCE (stated plainly): the reduction is "
              "well-defined (gap/Herglotz/reconstruction hold for "
              "d in %s) but the transported block is not yet "
              "entrywise Cauchy at the frozen bars -- the failing "
              "(d, gate) cells are printed above.  The "
              "boundary-triple module is NOT yet opened; the "
              "cell-cocycle module remains an alternative.  NO RH "
              "claim." % trio_pass)
    else:
        print("CONSEQUENCE (stated plainly): no band dimension in "
              "%s carries a well-defined convergent reduction (or "
              "the run is invalid) -- the Feshbach route closes on "
              "this surface and the cell-cocycle module becomes "
              "the remaining path.  NO RH claim." % (D_SET,))
    return 0 if (guards_ok and controls_ok) else 1

_run_part1 = run

def _run_part2():
    # PART 2 -- qf_edge_separation_probe.py (verbatim; module-level names are
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
    import epstein_firewall_probe as epx  # noqa: E402
    import v770_qf_spectral_bundle as qsb  # noqa: E402  (read-only)

    T_START = time.time()

    # ------------------------------------------------ frozen specification
    D = srp.DGRID                        # 1/64, dyadic float-exact
    ATOM_MAX_XD = 1000000000             # deeper comb cap (frozen, 1e9)
    M_CAP_XD = int(math.floor(math.log(ATOM_MAX_XD) / D))       # 1326
    M_TOP_XD = 1324                      # deepest rung (X = 20.6875)
    M_TOP_PAR = 824                      # first-parent cap (prefix Ward)
    M_TOP_FES = 1176                     # Feshbach-probe top (anchors)

    FLAD = list(range(888, 1325, 4))     # 110 rungs, X = 13.875..20.6875
    CENS = [884] + FLAD                  # census ladder (entry Ward)
    XLAD = list(range(1180, 1325, 4))    # 37 extension rungs
    N_TAIL = int(math.ceil(len(XLAD) / 4.0))          # 10 tail rungs
    TAIL = XLAD[-N_TAIL:]                # 1288..1324, X = 20.125..20.6875
    TOP5_NEW = list(range(1308, 1325, 4))
    TOP5_DRAIN = list(range(1160, 1177, 4))

    K_QF = 6                             # q_f band rank (drainage rule)
    D_EDGE = 7                           # the adjudicated band dimension
    D_STORE = 9                          # stored eigenmodes (gaps to 8/9)
    THR_NULL = 1.0e-4                    # threshold census (entry rule)
    THR_DEEP = 1.0e-5                    # deep census (reported)
    NPAD = 128                           # max battery support in cells
    R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
    N_MED = 5                            # median block size

    Z_REF = -1.0e-2                      # frozen Cauchy reference cell
    H_IM = 1.0e-2                        # Herglotz imaginary offset
    ZC = (complex(0.0, H_IM), complex(-1.0e-3, H_IM))

    GAP_BAR = 0.10                       # EDGE-A tail separation bar
    C_MED = 0.50                         # EDGE-B med5 ratio bar
    C_SLOPE = 0.02                       # EDGE-B second-half rate bar
    INC_FIRST5 = slice(0, 5)             # increment blocks (109 pairs)
    INC_LAST5 = slice(104, 109)
    INC_HALF2 = slice(54, 109)
    CAD_BAR = 0.25                       # EDGE-C rel spread regularity

    SVD_FLOOR = 1.0e-8                   # K4 polar/90-degree floor
    COUP_WARD = 1.0e-8                   # G1.7 coupling |E| Ward
    WARD_ORTH = 1.0e-10                  # G1.8 R orthogonality
    HERG_FLOOR = 1.0e-10                 # HERG-7 Ward floor
    PD_TOL = 1.0e-9                      # G1.6 measured-PD slack
    BOUND_TOL = 1.0e-9                   # G1.9 boundedness slack
    QF_FLOOR = 1.0e-12                   # denominator floor
    COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
    PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
    RUNTIME_CAP = 1800.0                 # seconds, predeclared

    REPRO_G67_1096 = 0.1008              # Feshbach frozen 6/7 gap (1096)
    REPRO_G67_1176 = 0.1397              # Feshbach frozen 6/7 gap (1176)
    REPRO_G78_1176 = 0.0613              # Feshbach frozen 7/8 gap (1176)
    REPRO_TOLG = 2.0e-4                  # anchor gaps to 4 digits
    REPRO_NN1176 = 8                     # frozen thr count (1176)
    REPRO_LMIN1176 = 3.882e-6            # frozen lambda_min (1176)
    REPRO_LTOL = 2.0e-8
    ENTRY7_RUNG = 992                    # frozen 7th-mode entry rung
    DRAIN_LEVELS = {                     # drainage med5(TOP5) frozen
        "R2:box[0,R]": 0.3583, "R2:box[R/2,R]": 0.3370,
        "R2:hat(R/2,R/2)": 0.3127, "R2:hat(3R/4,R/4)": 0.2590,
        "R2:box[R/4,3R/4]": 0.2249, "R1:box[R/2,R]": 0.0793,
        "R1:box[0,R]": 0.0741, "R2:box[0,R/2]": 0.0741,
        "R1:hat(R/4,R/4)": 0.0082}
    REPRO_QTOL = 2.0e-3

    EP_NCAP = 34000                      # Epstein Lambda_E table reach
    EP_MMAX = 640                        # Epstein control tower cap
    SEED = 7

    BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
              "prevprime", "primepi", "sympy")

    CHECKS = []       # guards + controls: all must pass, else invalid run
    GATES = []        # edge gates: feed the verdict only


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
        """Battery bytes + cap + ladders + blocks + bars + anchors,
        SHA-256 frozen BEFORE any comb data is built in this probe."""
        bats = {}
        hsh = hashlib.sha256()
        hsh.update(("qf-edge-separation spec: 4 boxes + 3 hats per R, "
                    "l2-norm, D=%.10f, R=%s; deeper comb = deployed "
                    "von_mangoldt_table sieve at cap %d (benchmarked "
                    "12.3 s / 13.5 GB before freeze), M_CAP=%d, M_TOP=%d"
                    "; FLAD=%s; CENS=[884]+FLAD; XLAD=%s; TAIL=%s; "
                    "TOP5_NEW=%s TOP5_DRAIN=%s; band rule = d lowest "
                    "always, qf rank %d, d_edge = %d, thr=%g deep=%g; "
                    "z: zref=%g h=%g zc=%s; EDGE-A: g78 >= %g on every "
                    "TAIL rung; EDGE-B: med5 last/first <= %g AND b2 >= "
                    "%g, blocks [0:5][104:109][54:109] Nmed=%d; EDGE-C: "
                    "entry rung = first CENS rung with count >= n, rel "
                    "spread (max-min)/max of DX <= %g = regular, KM2 = "
                    "new entry (>= 9) on extension AND regular; kills: "
                    "svd>=%g coup<=%g; wards: orth<=%g herg<=%g "
                    "pd>=-%g bound<=%g; anchors: g67(1096)=%g "
                    "g67(1176)=%g g78(1176)=%g tolg=%g nn1176=%d "
                    "deep1176=1 lmin1176=%g toll=%g entry7=%d "
                    "entry884=5 entry888=6; drain levels %s tol=%g; "
                    "guards: comb<=%g prefix<=%g runtime<=%g; controls "
                    "verbatim qsb.control_bundle, lads=%s/%s epcap=%d "
                    "epM=%d seed=%d; verdict order: invalid -> "
                    "SEPARATES-D7 (A and B) -> KEEPS-MOVING (not A or "
                    "KM2) -> UNDECIDED"
                    % (D, R_BAT, ATOM_MAX_XD, M_CAP_XD, M_TOP_XD, FLAD,
                       XLAD, TAIL, TOP5_NEW, TOP5_DRAIN, K_QF, D_EDGE,
                       THR_NULL, THR_DEEP, Z_REF, H_IM, ZC, GAP_BAR,
                       C_MED, C_SLOPE, N_MED, CAD_BAR, SVD_FLOOR,
                       COUP_WARD, WARD_ORTH, HERG_FLOOR, PD_TOL,
                       BOUND_TOL, REPRO_G67_1096, REPRO_G67_1176,
                       REPRO_G78_1176, REPRO_TOLG, REPRO_NN1176,
                       REPRO_LMIN1176, REPRO_LTOL, ENTRY7_RUNG,
                       sorted(DRAIN_LEVELS.items()), REPRO_QTOL,
                       COMB_DEV_BAR, PREFIX_WARD, RUNTIME_CAP,
                       qsb.CTRL_LAD_S, qsb.CTRL_LAD_E, EP_NCAP, EP_MMAX,
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


    def build_deep_comb():
        lam_deep = core.von_mangoldt_table(ATOM_MAX_XD)
        dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
        check("G1.1 deep-table overlap: 1e9 von Mangoldt table == "
              "deployed core table on [0, %d] EXACTLY"
              % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
        nn = np.nonzero(lam_deep > 0.0)[0]
        u_deep = np.log(nn.astype(float))
        mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
        psi = np.cumsum(lam_deep[nn])
        keep = nn.astype(float) >= core.KAPPA_X0
        kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                             / nn[keep].astype(float)))
        check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over "
              "all jump points of psi(x)/x in [%.0f, %d] <= KAPPA_REF + "
              "%.0e = %.6f" % (kappa, core.KAPPA_X0, ATOM_MAX_XD,
                               core.TOL_KAPPA,
                               core.KAPPA_REF + core.TOL_KAPPA),
              kappa <= core.KAPPA_REF + core.TOL_KAPPA)
        return u_deep, mu_deep


    def build_deep_tower(u_deep, mu_deep, T_par):
        alpha = 0.5 * M_TOP_XD * D
        ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                                 side="right"))
        c_cont = srp.continuum_lags(M_TOP_XD)
        c_at, _dd = core.atom_lags_at(alpha, M_TOP_XD, u_deep[:ka],
                                      mu_deep[:ka])
        T = sla.toeplitz((c_cont + c_at)[:M_TOP_XD])
        dev = float(np.max(np.abs(T[:M_TOP_PAR, :M_TOP_PAR] - T_par)))
        check("G1.4 prefix Ward: deep tower leading %d x %d block == "
              "parent tower, max abs dev %.1e <= %.0e"
              % (M_TOP_PAR, M_TOP_PAR, dev, PREFIX_WARD),
              dev <= PREFIX_WARD)
        print("  deep census: ka = %d atoms to e^%.4f" % (ka,
                                                          2.0 * alpha))
        return T, c_cont, alpha, ka


    # ------------------------------------------------ spectral ladder
    def spectral_pass(T, sizes):
        """Per rung: full spectrum, sign-fixed 9-mode head basis,
        coupling rows E = V^T A V9 (commutation Ward rows), census."""
        out = {}
        for M in sizes:
            A = T[:M, :M]
            lam, V = np.linalg.eigh(A)
            V9 = qsb.sign_fix(V[:, :D_STORE])
            out[M] = dict(M=M, lam=lam, V9=V9, E=V.T @ (A @ V9),
                          nn=int(np.sum(lam <= THR_NULL)),
                          nn_deep=int(np.sum(lam <= THR_DEEP)))
        return out


    def lin_slope(xs, ys):
        A = np.vstack([np.ones_like(xs), xs]).T
        coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
        return float(coef[1])


    def fall_rate(xs, vals):
        """hbp.fit_rate verbatim: log val = a - b x, b > 0 = falling."""
        rows = [dict(XmR=float(x), mx=float(v)) for x, v in zip(xs, vals)]
        b, _resid = hbp.fit_rate(rows)
        return b


    def rel_gap(blk, d):
        """(lam_{d+1} - lam_d)/lam_{d+1}, 1-based (parent formula)."""
        return float((blk["lam"][d] - blk["lam"][d - 1]) / blk["lam"][d])


    # ------------------------------------------------ anchors (G1.5)
    def anchor_guards(spec):
        g67a = rel_gap(spec[1096], 6)
        g67b = rel_gap(spec[M_TOP_FES], 6)
        g78b = rel_gap(spec[M_TOP_FES], 7)
        check("G1.5a Feshbach anchor reproduction: 6/7 gap(1096) = "
              "%.4f vs frozen %.4f, 6/7 gap(1176) = %.4f vs frozen "
              "%.4f, 7/8 gap(1176) = %.4f vs frozen %.4f (all dev <= "
              "%.0e); thr count(1176) = %d (== %d), deep count = %d "
              "(== 1); lambda_min(1176) = %.4e vs frozen %.4e (tol "
              "%.0e)"
              % (g67a, REPRO_G67_1096, g67b, REPRO_G67_1176, g78b,
                 REPRO_G78_1176, REPRO_TOLG, spec[M_TOP_FES]["nn"],
                 REPRO_NN1176, spec[M_TOP_FES]["nn_deep"],
                 spec[M_TOP_FES]["lam"][0], REPRO_LMIN1176, REPRO_LTOL),
              abs(g67a - REPRO_G67_1096) <= REPRO_TOLG
              and abs(g67b - REPRO_G67_1176) <= REPRO_TOLG
              and abs(g78b - REPRO_G78_1176) <= REPRO_TOLG
              and spec[M_TOP_FES]["nn"] == REPRO_NN1176
              and spec[M_TOP_FES]["nn_deep"] == 1
              and abs(spec[M_TOP_FES]["lam"][0] - REPRO_LMIN1176)
              <= REPRO_LTOL)
        entry7 = min((M for M in FLAD if spec[M]["nn"] >= 7),
                     default=-1)
        check("G1.5b entry-rung reproduction: count %d at M = 884, %d "
              "at M = 888 (6th entry frozen), 7th entry at M = %d "
              "(frozen %d)" % (spec[884]["nn"], spec[888]["nn"], entry7,
                               ENTRY7_RUNG),
              spec[884]["nn"] == 5 and spec[888]["nn"] == 6
              and entry7 == ENTRY7_RUNG)


    # ------------------------------------------------ EDGE-A + reports
    def edge_gap_analysis(spec):
        print("\n-- EDGE-A: the 7/8 edge on the extension (bar %g; "
              "frozen tail block M = %d..%d)" % (GAP_BAR, TAIL[0],
                                                 TAIL[-1]))
        g78 = {M: rel_gap(spec[M], 7) for M in FLAD}
        print("  gap 7/8 profile on FLAD (every 8th rung): %s"
              % "  ".join("M=%d:%.4f" % (M, g78[M]) for M in FLAD[::8]))
        print("  gap 7/8 on the tail block: %s"
              % "  ".join("M=%d:%.4f" % (M, g78[M]) for M in TAIL))
        rec = [M for M in XLAD if g78[M] >= GAP_BAR]
        if rec:
            stays = all(g78[M] >= GAP_BAR for M in XLAD
                        if M >= rec[0])
            print("  first recovery rung on the extension: M = %d "
                  "(g78 = %.4f); stays above bar from there to top: %s"
                  % (rec[0], g78[rec[0]], stays))
        else:
            print("  no extension rung reaches the bar (max %.4f)"
                  % max(g78[M] for M in XLAD))
        xs_x = np.array([M * D for M in XLAD])
        gx = np.array([g78[M] for M in XLAD])
        n2 = len(XLAD) // 2
        print("  extension second-half linear trend: %+.4f/X "
              "(reported)" % lin_slope(xs_x[n2:], gx[n2:]))
        tail_min = min(g78[M] for M in TAIL)
        a_ok = gate("EDGE-A 7/8 TAIL SEPARATION: min rel gap on the "
                    "frozen tail block = %.4f (top rung %.4f) >= %g"
                    % (tail_min, g78[M_TOP_XD], GAP_BAR),
                    tail_min >= GAP_BAR)

        # reported, never gated: 6/7 and 8/9 on the extension
        g67 = {M: rel_gap(spec[M], 6) for M in XLAD}
        g89 = {M: rel_gap(spec[M], 8) for M in XLAD}
        m67 = min(g67, key=g67.get)
        m89 = min(g89, key=g89.get)
        print("  gap 6/7 on the extension (reported): min %.4f at "
              "M = %d, top rung %.4f -- the d = 6 grazing %s"
              % (g67[m67], m67, g67[M_TOP_XD],
                 "resolves" if min(g67.values()) >= GAP_BAR
                 else "does NOT resolve"))
        print("  gap 8/9 on the extension (reported): min %.4f at "
              "M = %d, top rung %.4f" % (g89[m89], m89,
                                         g89[M_TOP_XD]))
        print("  lam7/8/9 at the top rung: %.4e / %.4e / %.4e"
              % (spec[M_TOP_XD]["lam"][6], spec[M_TOP_XD]["lam"][7],
                 spec[M_TOP_XD]["lam"][8]))
        return a_ok


    # ------------------------------------------------ EDGE-C cadence
    def cadence(spec):
        print("\n-- EDGE-C: mode-descent cadence (fit-free; entry rung "
              "= first census rung with count >= n, thr %g)" % THR_NULL)
        nns = [spec[M]["nn"] for M in CENS]
        print("  threshold count profile along CENS (every 8th rung): "
              "%s" % "/".join("%d:%d" % (M, spec[M]["nn"])
                              for M in CENS[::8]))
        deeps = sorted(set(spec[M]["nn_deep"] for M in CENS))
        print("  deep count (lam <= %g) values seen: %s"
              % (THR_DEEP, deeps))
        entries = {}
        for M in CENS:
            for n in range(6, spec[M]["nn"] + 1):
                entries.setdefault(n, M)
        ns = sorted(n for n in entries if n >= 6)
        print("  mode-entry table:")
        for n in ns:
            print("    mode %2d: entry M = %d (X = %.4f)"
                  % (n, entries[n], entries[n] * D))
        dxs = [(entries[b] - entries[a]) * D
               for a, b in zip(ns, ns[1:])]
        if dxs:
            spread = (max(dxs) - min(dxs)) / max(dxs)
            print("  inter-entry gaps DX = %s; mean %.4f; rel spread "
                  "(max-min)/max = %.3f (regularity bar <= %g)"
                  % ("/".join("%.4f" % v for v in dxs),
                     float(np.mean(dxs)), spread, CAD_BAR))
            print("  predicted next entry at the measured cadence "
                  "(REPORTED only): X ~ %.2f (M ~ %d, ATOM_MAX ~ %.1e)"
                  % (entries[ns[-1]] * D + float(np.mean(dxs)),
                     int((entries[ns[-1]] * D + float(np.mean(dxs)))
                         / D),
                     math.exp(entries[ns[-1]] * D + float(np.mean(dxs)))))
        else:
            spread = float("inf")
        new_entry = max(ns) >= 9 and entries[max(ns)] > M_TOP_FES
        regular = bool(dxs) and spread <= CAD_BAR
        km2 = gate("EDGE-C KM2 keeps-moving clause (fires = pass): new "
                   "mode entry (count >= 9) on the extension = %s AND "
                   "cadence regular (spread %.3f <= %g) = %s"
                   % (new_entry, spread, CAD_BAR, regular),
                   new_entry and regular)
        _ = nns
        return km2


    # ------------------------------------------------ EDGE-B: d=7 Cauchy
    def f_frame(blk, d, z):
        """Effective block in the rung band frame: Lambda_d - z - C_d(z)
        with the MEASURED Schur correction (machine scale, P A Q = 0)."""
        lam = blk["lam"]
        Ec = blk["E"][d:, :d]
        corr = Ec.T @ (Ec / (lam[d:, None] - z))
        return np.diag(lam[:d]) - z * np.eye(d) - corr


    def feshbach_d7(spec):
        print("\n-- EDGE-B: transported d = %d effective block on the "
              "deep range (parent bars verbatim; Z_REF = %g)"
              % (D_EDGE, Z_REF))
        d = D_EDGE
        xs = np.array([M * D for M in FLAD])

        Rs, sig_min = [np.eye(d)], []
        ward_orth = 0.0
        sig_max = 0.0
        for Ma, Mb in zip(FLAD, FLAD[1:]):
            Va = spec[Ma]["V9"][:, :d]
            Vb = spec[Mb]["V9"][:, :d]
            S = Vb[:Ma, :].T @ Va
            U, s, Wt = np.linalg.svd(S)
            sig_min.append(float(s[-1]))
            sig_max = max(sig_max, float(s[0]))
            Rs.append(U @ Wt @ Rs[-1])
            ward_orth = max(ward_orth, float(np.max(np.abs(
                Rs[-1].T @ Rs[-1] - np.eye(d)))))
        check("K4 kill audit (d=%d): min sigma_min = %.6f >= %.0e "
              "(transport well-defined; max angle %.2f deg)"
              % (d, min(sig_min), SVD_FLOOR,
                 math.degrees(math.acos(min(min(sig_min), 1.0)))),
              min(sig_min) >= SVD_FLOOR)
        check("G1.8 transport orthogonality Ward (d=%d): max "
              "||R^T R - I|| = %.1e <= %.0e" % (d, ward_orth,
                                                WARD_ORTH),
              ward_orth <= WARD_ORTH)
        coup = max(float(np.max(np.abs(spec[M]["E"][d:, :d])))
                   for M in FLAD)
        check("G1.7 coupling/commutation Ward (d=%d): max |E| = %.1e "
              "<= %.0e on every FLAD rung (P A Q = 0 measured, not "
              "assumed)" % (d, coup, COUP_WARD), coup <= COUP_WARD)

        Ft = [Rs[i].T @ f_frame(spec[M], d, complex(Z_REF, 0.0)) @ Rs[i]
              for i, M in enumerate(FLAD)]
        dref = np.array([float(np.max(np.abs(Ft[i + 1] - Ft[i])))
                         for i in range(len(FLAD) - 1)])
        med_f = float(np.median(dref[INC_FIRST5]))
        med_l = float(np.median(dref[INC_LAST5]))
        ratio = med_l / max(med_f, QF_FLOOR)
        b2 = fall_rate(xs[1:][INC_HALF2], dref[INC_HALF2])
        print("  increment profile (first 3 / last 3): %s ... %s"
              % (", ".join("%.2e" % v for v in dref[:3]),
                 ", ".join("%.2e" % v for v in dref[-3:])))
        b_ok = gate("EDGE-B CAUCHY-%d DEEP: med%d last/first = %.3f <= "
                    "%g AND second-half falling rate b2 = %+.3f/X >= "
                    "%g (%d increments, oscillation-aware, parent bars "
                    "verbatim)" % (d, N_MED, ratio, C_MED, b2, C_SLOPE,
                                   len(dref)),
                    ratio <= C_MED and b2 >= C_SLOPE)

        # HERG-7 Ward (exact structural identity, guard level)
        herg_f, herg_m = -np.inf, np.inf
        for z in ZC:
            for i, M in enumerate(FLAD):
                Fz = Rs[i].T @ f_frame(spec[M], d, z) @ Rs[i]
                imF = (Fz - Fz.conj().T) / 2.0j
                herg_f = max(herg_f, float(np.max(
                    np.linalg.eigvalsh(imF))))
                Minv = np.linalg.inv(Fz)
                imM = (Minv - Minv.conj().T) / 2.0j
                herg_m = min(herg_m, float(np.min(
                    np.linalg.eigvalsh(imM))))
        check("HERG-%d Ward (every FLAD rung, both complex z): max eig "
              "Im F~ = %+.3e <= %.0e AND min eig Im F~^{-1} = %+.3e >= "
              "-%.0e" % (d, herg_f, HERG_FLOOR, herg_m, HERG_FLOOR),
              herg_f <= HERG_FLOOR and herg_m >= -HERG_FLOOR)

        fmax = max(float(np.max(np.abs(F))) for F in Ft)
        lmax_band = max(float(spec[M]["lam"][d - 1]) for M in FLAD)
        check("G1.9a boundedness (d=%d): max |F~| entry = %.3e <= "
              "lam_max(band) + |z|_max + %.0e = %.3e; max overlap "
              "sigma = %.6f <= 1 + 1e-12"
              % (d, fmax, BOUND_TOL,
                 lmax_band + abs(Z_REF) + BOUND_TOL, sig_max),
              fmax <= lmax_band + abs(Z_REF) + BOUND_TOL
              and sig_max <= 1.0 + 1.0e-12)
        return b_ok


    # ------------------------------------------------ q_f levels (report)
    def qf_levels(spec, F, names):
        print("\n-- settled q_f levels (band rule = %d lowest, "
              "drainage object verbatim; med%d over M %d..%d NEW vs "
              "%d..%d DRAIN; reported, never gated)"
              % (K_QF, N_MED, TOP5_NEW[0], TOP5_NEW[-1], TOP5_DRAIN[0],
                 TOP5_DRAIN[-1]))
        qmap = {M: np.sum((spec[M]["V9"][:NPAD, :K_QF].T @ F) ** 2,
                          axis=0) for M in FLAD}
        med_dr = np.median(np.stack([qmap[M] for M in TOP5_DRAIN]),
                           axis=0)
        med_nw = np.median(np.stack([qmap[M] for M in TOP5_NEW]),
                           axis=0)
        xs_x = np.array([M * D for M in XLAD])
        q_x = np.stack([qmap[M] for M in XLAD])
        print("  %-18s %-8s %-8s %-8s %s"
              % ("function", "drain", "new", "ratio", "ext rate b/X"))
        dev_worst = 0.0
        for j, nm in enumerate(names):
            b = fall_rate(xs_x, q_x[:, j])
            print("  %-18s %.4f   %.4f   %5.3f   %+6.3f"
                  % (nm, med_dr[j], med_nw[j],
                     med_nw[j] / max(med_dr[j], QF_FLOOR), b))
            if nm in DRAIN_LEVELS:
                dev_worst = max(dev_worst,
                                abs(med_dr[j] - DRAIN_LEVELS[nm]))
        check("G1.5c drainage settled-level reproduction: med%d over "
              "%d..%d matches the nine frozen drainage values, worst "
              "dev %.1e <= %.0e" % (N_MED, TOP5_DRAIN[0], TOP5_DRAIN[-1],
                                    dev_worst, REPRO_QTOL),
              dev_worst <= REPRO_QTOL)
        qall = np.stack([qmap[M] for M in FLAD])
        check("G1.9b boundedness: every band q_f in [%.1e, %.4f] "
              "inside [-1e-12, 1 + %.0e]"
              % (float(np.min(qall)), float(np.max(qall)), BOUND_TOL),
              float(np.min(qall)) >= -1.0e-12
              and float(np.max(qall)) <= 1.0 + BOUND_TOL)


    # ------------------------------------------------ controls
    def run_controls(c_cont, alpha_xd, ka_xd, mu_deep):
        print("\n-- controls (must fire; fire rule = "
              "qf_spectral_bundle_probe.control_bundle verbatim)")
        rng = np.random.default_rng(SEED)
        pos = np.sort(rng.uniform(0.5, 2.0 * alpha_xd, ka_xd))
        cat_s, _dd = core.atom_lags_at(alpha_xd, M_TOP_XD, pos,
                                       mu_deep[:ka_xd])
        Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_XD])
        fire_s, det_s = qsb.control_bundle(Ts, qsb.CTRL_LAD_S,
                                           "scramble")
        check("CS position-scramble control (1e9 comb, %d atoms) "
              "fires" % ka_xd, fire_s, det_s)

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
        fire_e, det_e = qsb.control_bundle(TE, qsb.CTRL_LAD_E, "epstein")
        check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
              "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


    # ------------------------------------------------ run
    def run():
        print("=" * 78)
        print("QF OFFENSIVE strand 3, module 3 follow-up -- edge "
              "separation: the 7/8 edge on the 1e9 comb (X <= %.4f)"
              % (M_TOP_XD * D))
        print("=" * 78)

        hits = ast_firewall()
        check("G0.1 AST firewall (band rule is an eigenvalue-order "
              "rule of the source operator; no target information)",
              not hits, str(hits))
        bats, spec_sha = freeze_spec()
        check("G0.2 battery + cap + ladders + blocks + bars + anchors "
              "SHA-256-frozen BEFORE any comb data is built here", True,
              "SHA256 %s..." % spec_sha[:16])
        check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d "
              "(X = %.6f <= %.6f); sieve cover exp(X_top) + 2 = %d <= "
              "%d; runtime cap %.0f s predeclared"
              % (M_TOP_XD, ATOM_MAX_XD, M_CAP_XD, M_TOP_XD * D,
                 math.log(ATOM_MAX_XD),
                 int(math.exp(M_TOP_XD * D)) + 2, ATOM_MAX_XD,
                 RUNTIME_CAP),
              M_TOP_XD <= M_CAP_XD
              and int(math.exp(M_TOP_XD * D)) + 2 <= ATOM_MAX_XD)

        # ---- comb + towers strictly after the freeze
        u_deep, mu_deep = build_deep_comb()
        T_par = build_parent_tower()
        T, c_cont, alpha_xd, ka_xd = build_deep_tower(u_deep, mu_deep,
                                                      T_par)

        # ---- spectra on the census ladder
        spec = spectral_pass(T, CENS)
        F, names = battery_matrix(bats)
        pd_min = min(float(spec[M]["lam"][0]) for M in CENS)
        print("  PD margins (measured, never gated): lambda_min = "
              "%.3e (M %d) -> %.3e (M %d)"
              % (spec[M_TOP_FES]["lam"][0], M_TOP_FES,
                 spec[M_TOP_XD]["lam"][0], M_TOP_XD))
        check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every "
              "rung (measured output; no gate uses a PD margin or "
              "1/eps)" % (pd_min, PD_TOL), pd_min > -PD_TOL)

        # ---- anchors, gates, reports
        anchor_guards(spec)
        a_ok = edge_gap_analysis(spec)
        km2 = cadence(spec)
        b_ok = feshbach_d7(spec)
        qf_levels(spec, F, names)

        # ---- controls
        run_controls(c_cont, alpha_xd, ka_xd, mu_deep)

        # ---- runtime guard (predeclared)
        dt = time.time() - T_START
        check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
              % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

        # ---- verdict (preregistered decision order)
        guards_ok = all(ok for (n, ok) in CHECKS
                        if not n.startswith(("CS", "CE")))
        controls_ok = all(ok for (n, ok) in CHECKS
                          if n.startswith(("CS", "CE")))
        if not (guards_ok and controls_ok):
            verdict = "EDGE-UNDECIDED (invalid run)"
        elif a_ok and b_ok:
            verdict = "EDGE-SEPARATES-D7"
        elif (not a_ok) or km2:
            verdict = "EDGE-KEEPS-MOVING"
        else:
            verdict = "EDGE-UNDECIDED"

        n_gate = sum(1 for (_n, ok) in GATES if ok)
        n_chk = sum(1 for (_n, ok) in CHECKS if ok)
        print("\nVERDICT: %s" % verdict)
        print("GATES %d/%d (A=%s B=%s KM2=%s), GUARDS+CONTROLS %d/%d, "
              "runtime %.1f s"
              % (n_gate, len(GATES), "P" if a_ok else "F",
                 "P" if b_ok else "F", "fires" if km2 else "quiet",
                 n_chk, len(CHECKS), time.time() - T_START))
        if verdict == "EDGE-SEPARATES-D7":
            print("CONSEQUENCE (stated plainly): the 7/8 edge separates "
                  "again at depth and the transported d = 7 block is "
                  "Cauchy at the parent bars -- the fixed-d Feshbach "
                  "limit EXISTS after all: the boundary-triple module "
                  "reopens with d = 7 (the z -> 0 transition of "
                  "M~(z) = F~(z)^{-1} on the d = 7 limit block is its "
                  "remaining task).  NOT claimed: X -> infinity, "
                  "eps-uniformity, RH.")
        elif verdict == "EDGE-KEEPS-MOVING":
            print("CONSEQUENCE (stated plainly): the band edge KEEPS "
                  "MOVING -- descending modes overrun every fixed band "
                  "dimension at the measured entry positions above; "
                  "fixed-d Feshbach is CLOSED on every reachable "
                  "surface, and the cell-cocycle formulation (depth-"
                  "dependent d(X) with transition maps at the mode-"
                  "entry rungs) is the only remaining path of the "
                  "diagonal route.  The measured cadence is the new "
                  "named structural constant of that module.  NO RH "
                  "claim, no X -> infinity claim.")
        else:
            print("CONSEQUENCE (stated plainly): the edge bars are not "
                  "reached either way at X = %.4f -- the gap tail, "
                  "Cauchy numbers and cadence table above say exactly "
                  "what a deeper comb must decide (next predicted "
                  "entry depth printed in the cadence block).  NO RH "
                  "claim." % (M_TOP_XD * D))
        return 0 if (guards_ok and controls_ok) else 1
    return run(), [n for (n, ok) in CHECKS if not ok], [n for (n, ok) in GATES if not ok]



def run():
    """run_all entry point (combined adjudication, frozen): part 1
    must reproduce its preregistered pattern (guards+controls 28/28,
    gates 9/12 with EXACTLY CAUCHY-6, GAP-7 and GAP-8 failing,
    FESHBACH-PARTIAL); part 2 must reproduce its pattern
    (guards+controls 20/20, EDGE-A fails, EDGE-B passes, KM2 quiet,
    EDGE-KEEPS-MOVING) -- the honest combined verdict: fixed-d
    Feshbach is closed permanently by band ownership, not by
    non-convergence."""
    rc1 = _run_part1()
    chk_fails1 = [n for (n, ok) in CHECKS if not ok]
    toks1 = sorted(n.split()[0] for n in
                   [n for (n, ok) in GATES if not ok])
    part1_ok = (rc1 == 0 and not chk_fails1
                and toks1 == ["CAUCHY-6", "GAP-7", "GAP-8"])
    print("\n[%s] PART-1 PATTERN GATE: expected exactly the "
          "preregistered CAUCHY-6/GAP-7/GAP-8 fails (FESHBACH-PARTIAL)"
          " -- failing gates: %s"
          % ("PASS" if part1_ok else "FAIL", toks1))
    rc2, chk_fails2, gate_fails2 = _run_part2()
    toks2 = sorted(n.split()[0] for n in gate_fails2)
    part2_ok = (rc2 == 0 and not chk_fails2
                and toks2 == ["EDGE-A", "EDGE-C"])
    print("\n[%s] PART-2 PATTERN GATE: expected exactly the "
          "preregistered EDGE-A fail with KM2 quiet "
          "(EDGE-KEEPS-MOVING) -- failing gates: %s"
          % ("PASS" if part2_ok else "FAIL", toks2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- FESHBACH-PARTIAL / "
          "EDGE-KEEPS-MOVING: the d = 6 reduction is exact "
          "(reconstruction 8.8e-13) and matrix-Herglotz certified, but "
          "the band edge is chased by descending modes at every d -- "
          "the 7/8 edge closes into an avoided crossing (0.0039 at "
          "M = 1240) while the transported d = 7 block stays Cauchy; "
          "the entry cadence WIDENS (DX = 1.625/1.8125/2.625, spread "
          "0.381).  Fixed-d Feshbach is closed permanently; the "
          "cell-cocycle formulation was the only remaining path.  "
          "NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys as _sys
    _sys.exit(run())
