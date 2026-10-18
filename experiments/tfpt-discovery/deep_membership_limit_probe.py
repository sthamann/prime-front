#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_membership_limit_probe -- PRIME.ONEBADMODE.DEEP.MEMBERSHIP.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

DOES THE CLASS-MEMBERSHIP QUESTION HAVE A LIMIT STRUCTURE IN THE DEEP
FRAME?  The certified sigma chain is finite-complete: CCLXXVII built
the exact-rational per-step machine (P1 entry fact n > 0 + P2 certified
co-block floor + P3 Gauss-Radau K = 4 + P4 exact arithmetic) and
CCLXXIX closed it over ALL 151 built wall-legal cells at K in {4, 5, 6}
(worst certified sigma bound 0.726909 <= SIGMA_ENV 0.7809 < 1 =>
M positive definite).  CCLXXXI lifted definiteness to CLASS level: the
source-only JOINT Gauss-Radau relation

    RAD:  RADAU_K(nu_0..nu_{2K-2}; c) <= t_R * n,   t_R = 0.7809

gives inf lambda_1(J) > 0 over the whole entry-data class (8.33e-03 at
K = 4 / 3.79e-04 at K = 5), while the same class WITHOUT the relation
admits lambda_1 = -5.74e+02.  CCLXXIII proved the deployed surface
family FINITE and closed.  ONE QUANTIFIER REMAINS: new deep-frame
rungs (h -> infinity along the cofinal deep ladder) must keep their
ENTRY DATA in the class.  THIS PROBE asks whether that question has a
LIMIT STRUCTURE.

THE OBJECT.  Per wall-legal cell the deployed step assembly produces
Mt = Q_1^T (S_2 / tau_1) Q_1 (zolotarev_phase_filter.assemble_step
verbatim, CCLXV normalization).  Its ENTRY DATA -- the only inputs the
certified chain consumes -- are

    n = Mt[0,0],  nu_k = b^T B^k b (k = 0..8),  c = lambda_min(B)

with b = Mt[1:,0], B = Mt[1:,1:].  THE DECISIVE OBSERVATION, stated
before any measurement: EVERY constraint the chain uses is
SCALE-INVARIANT under Mt -> Mt/lambda (lambda > 0).  P1 (n > 0), P2
(c > 0) and RAD are invariant (both sides of RAD scale as 1/lambda),
and so are sigma = q/n and rho_K = RADAU_K(nu; c)/n.  The deployed
normalization divides by tau_1 -- the PREVIOUS rung's bottom eigenvalue
-- so the RAW entry data carry the tau_2/tau_1 ratio of the step pair,
while the class-decisive functionals do not.  The probe therefore
measures the data in TWO DECLARED NORMALIZATIONS:

 NORM-D (deployed, raw):  n, nu_0..nu_8, c, sigma, rho_4, rho_5.
 NORM-P (pivot scale-quotient, the class-decisive one):
     r     = c / n                      (floor-to-pivot ratio)
     g_k   = log10( nu_k / n^{k+2} )    (scale-invariant moment shape)
     gslope, gresid                     (the SHAPE coordinates: the
        linear fit of g_k in k -- gslope = log10 of the dominant scale
        ratio nu_{k+1}/(nu_k n), gresid = the residual RMS, which is 0
        exactly for a one-atom measure)
     sigma, rho_4, rho_5                (invariant by construction)
 The invariance is WARDED numerically (G3) at three declared scales.

 (a) THE DEEP DATA CURVES.  The deep-frame census on the CCLXIX
     depth-extension table (TAB2 = 1.6e7, bitwise-warded against the
     deployed 4e6 prefix) is enumerated in full; wall-legal cells are
     built in NB = 5 CONTIGUOUS BLOCKS of the h-sorted census at
     declared depth targets, the last one at the deepest h the frozen
     cost law affords.  CONTIGUITY IS ESSENTIAL AND IS A DECLARED
     DESIGN CHOICE (amendment A2): the deployed chain step pairs
     CENSUS NEIGHBOURS, so a log-spaced h ladder would compare
     non-neighbours and inject a spurious tau_2/tau_1 jump.  Per block
     and per datum: level (median), envelope (min/max), the per-cell
     fit vs log h with 2SE, the block-level fit vs log h with 2SE, and
     the Cauchy differences between consecutive blocks.  Verdict per
     datum: CONVERGENT-MEASURED(level, |slope| bound) / DRIFTING(law)
     / NOISY -- with CONVERGENT-MEASURED defined as h-STATIONARY
     within the measured 2SE band, NEVER as a proof of convergence.
 (b) THE LIMIT OBJECT.  Three objects, kept strictly apart.
     (i) THE LEVEL VECTOR: the per-datum median of the deepest block
     (n = 1, nu_k = 10^{g_k}, c = r).  This is a COORDINATE-WISE
     summary and, as the smoke measured, it is NOT a moment sequence:
     the deep g_k are LINEAR in k to R2 ~ 1, i.e. nu_{k+1}/(nu_k n) is
     constant, i.e. the deep moment shape has collapsed to a ONE-ATOM
     (rank-1 Hankel) shape, so the median vector's Hankel matrix is
     singular.  That collapse is reported as a first-class MEASUREMENT
     (LIM1) and it has a consequence that is used: THE MOMENT BOX IS
     NOT A PRODUCT BOX, the moments are rigidly linked, and therefore
     a BOX-CORNER envelope over the moments is VACUOUS -- this probe
     does not use one (declared design correction, see A11).
     (ii) THE MEDOID LIMIT MEMBER: the cell of the deepest block
     minimizing the max relative deviation from the level vector over
     MEDOID_KEYS.  It is an ACTUAL member of the family, so its
     moment sequence is Hankel-PD as a structural fact, and its EXACT
     scale-quotiented entry vector (moments nu_k / n^{k+2} and floor
     c / n as exact Fractions) is the LIMIT OBJECT on which RAD is
     re-evaluated in exact rational arithmetic.  The coherence ward is
     then EXACT: RADAU_K on the quotiented vector must reproduce the
     medoid's own certified rho_K to XR_TIE (this is RAD's scale
     invariance, verified rationally).
     (iii) THE MEASURED ENVELOPE: min floor and max rho_5 over the
     deepest block -- the honest worst case over BUILT members.
     Then the CCLXXXI closed form
     Lambda(n, c, rho) = ((n+c) - sqrt((n-c)^2 + 4 n c rho))/2 > 0 is
     evaluated at the medoid limit member and at the measured envelope
     worst.  The composed all-large-h
     architecture is stated with EVERY piece typed: the finite
     certified base [CERT-FINITE], the measured limit level and rate
     [MEASURED], the convergence envelope [CONJECTURE-GRADE, because
     the rate is measured and not proved], the crossover h, and the
     THIRD premise nobody has yet touched -- that the wall-legal deep
     family is COFINAL in h (legality itself is measured, not proved;
     the census records every failure).
 (c) THE MECHANISM.  On MECH cells at two declared depths the exact
     CCIII three-way split S = S_AR + S_SM + S_OSC (archimedean kernel
     / prime-free smooth surrogate / genuine prime oscillation) is
     computed and pushed through the SAME step frame, giving the exact
     additive decomposition Mt = Mt_AR + Mt_SM + Mt_OSC.  Reported per
     datum: the additive entry shares, the datum recomputed on the
     partial sums (AR, AR+SM, full), and the h-law of each share --
     i.e. which carrier holds the convergence and which the drift.
     The archimedean part is a deterministic function of (M, D) alone
     and is prime-blind by construction; the prime part is the open
     question.
 (d) GATES.  Reproduce the CCLXXIX deep values (the F5 rule verbatim,
     sigma max 0.297) and the CCLXV/CCLXIX ladder anchors (sigma max
     0.604556, lambda_min(B) min 0.3496, pivot min 0.082730); the
     exact-rational tier ties the float route at every consumed depth
     and the RB1 bound property is WARDED, never assumed; the
     scale-invariance ward; tau and CCXVII c_h relocation screens on
     every fitted level; controls-must-fire (scramble world, smooth
     world, a synthetic near-1 cell, an inflated floor claim);
     anti-circularity AST-scanned -- moments and floors from Mt's
     ENTRIES forward, NO wall eigendata in the certificate path.

EXTERNAL-CITED (facts consumed, warded numerically, never proved here).
 E2 Schur / Sylvester: M = [[n, b^T],[b, B]] symmetric is PD iff B is
    PD and s = n - b^T B^{-1} b > 0; a symmetric matrix is PD iff its
    LDL pivots are positive.  [Horn & Johnson, Matrix Analysis, 2nd
    ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE: for symmetric A with spec(A) in
    [c, inf), the K-node Gauss-Radau rule with the node prescribed at
    c is an UPPER bound for u^T A^{-1} u (f(x) = 1/x completely
    monotone); depth-uniform in K.  [Golub & Meurant, Matrices,
    Moments and Quadrature, PUP 2010, Ch. 6-7.]  THE SIGN IS WARDED
    PER CELL PER CONSUMED DEPTH (C5).
 E4 the Chebyshev algorithm: the monic three-term recurrence
    coefficients of a positive measure are rational functions of its
    power moments; exact in exact arithmetic, depth-generic.
    [Gautschi, Orthogonal Polynomials, OUP 2004, Sec. 2.1.]
 E5 interval Cholesky: if the outward-rounded interval Cholesky of a
    symmetric interval matrix completes with positive pivot lower
    bounds, every symmetric matrix in the interval is PD.  [Rump, Acta
    Numerica 19 (2010) 287-449.]
 E6 the diagonal-similarity fact [J^{-1}]_{11} = [T^{-1}]_{11} for a
    symmetric Jacobi matrix and its monic form.  [Horn & Johnson op.
    cit. Sec. 1.3.]
 E7 Hamburger/Hankel: a finite sequence nu_0..nu_{2K-2} is the moment
    sequence of a positive measure with at least K support points iff
    its K x K Hankel matrix is positive definite.  [Akhiezer, The
    Classical Moment Problem, Hafner 1965, Ch. 1.]

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seat is the DECLARED scramble control seed.  AC scans: the
    CERTIFICATE-path functions (exact_wall_data / chebyshev_monic /
    radau_exact / fr_solve / pd_exact / cert_floor_exact / chol_iv /
    hankel_pd) and the float bound-path functions (wall_moments /
    lanczos_pair / radau_upper / rho_source) carry no read, no
    eigensolver, no pivot read, no ladder identifier (CCLXV /
    CCLXXVII / CCLXXIX ban list verbatim).
 W  the registered ladder rebuilt read-only (42 surface rungs -> 68 =
    40 + 1 + 27 steps); the anchors for the CCLXIX bridge pattern.
 T  the TAB2 = 1.6e7 von-Mangoldt arrays built and warded BITWISE
    against the deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  THE DEEP CENSUS: every kz in [2, KZ2_MAX) whose deployed deep
    frame formula (D_k = G[kz]/(2 nu), nu = 4, M = ceil(alpha/D_k -
    1e-9) + 1 rounded even, h = M/2, alpha = U2[kz]) has X =
    exp(2 alpha) <= TAB2, h-sorted, printed with the frozen cost law.
 L  THE BLOCKS: NB = 5 contiguous segments at the declared targets
    BLOCK_TGT with sizes BLOCK_NC, built in ascending h behind the
    cost guard (elapsed + GUARD_FAC * COST_C * h^3 <= HARD_CAP_S, else
    UNBUILT-GUARD, honest and machine-dependent).  Cell legality is
    the CCLXXIII/CCLXIX cell_legal definition VERBATIM (core_ok,
    negA = 0, lamS > 0, tau > 0); illegal cells are CENSUSED with their
    failure reason in the LEGALITY CENSUS line and NO step is formed on
    them, so they enter NO convergence census and NO membership
    statement (amendment A3).  Steps: the CCLXIX sweep_steps formations
    -- within-block chain pairs of CENSUS NEIGHBOURS plus one bridge
    step per cell from its nearest registered anchor STRICTLY below it
    (amendment A12), with the self-bridge and DEGENERATE-B counts
    censused.
 B/I Jacobi translation and the CCLXV identity wards per cell
    (sigma == q/n == 1 - s/n at IDENT_TIE); P1 pivot sign n > 0
    warded per cell in float AND exact rational.
 SR repro anchors: ladder sigma max 0.604556, ladder lambda_min(B) min
    0.3496, ladder pivot min 0.082730 (CCLXV/CCLXIX).
 G  gates: G1 the CCLXXIX F5 rule VERBATIM (N5 = 4 deepest cells with
    h <= H5_CAP = 4200 passing the F5 filters) reproduces F5 sigma max
    0.297 and certifies <= SIGMA_ENV; G2 the exact-rational tier ties
    the float route at every consumed depth; G3 the SCALE-INVARIANCE
    ward (sigma, rho_4, rho_5 invariant under Mt -> lambda Mt for
    lambda in SCALE_SET).
 C  the certification per cell: exact-rational LDL floor (round-62
    machine verbatim, BIS_ITERS = 40), exact Chebyshev + exact monic
    Radau at K = 4 and K = 5, best = min of the INDEPENDENTLY warded
    depths (CCLXXIX A4, no monotonicity-in-K assumption), RB1 bound
    ward and node ward at every consumed depth, interval cross-tier
    (E5, refuse-only).
 CV THE CONVERGENCE CENSUS: per datum FIT-CELL (all legal cells vs
    log h), FIT-BLOCK (block medians vs log h), FIT-ENV (block
    envelope ends vs log h), Cauchy differences; the enum rule is
    frozen in CONV RULE below.
 LIM the limit object + the composed architecture with typed pieces.
 M  the mechanism split at MECH_TGT depths.
 X  controls-must-fire: X1 the scramble world (seed SCR_SEED) leaves
    legality or moves the data off the class; X2 the smooth
    (prime-free) world leaves legality or lands its data outside the
    measured deep envelope -- the DISCRIMINATION; X3 a synthetic
    near-1 cell (coupling scaled so truth sigma ~ 1.2) must NOT
    certify bound < 1; X4 an inflated floor claim must be refused by
    BOTH tiers.
 S  screens: tau and CCXVII c_h relocation screens (CCXLVII bars
    verbatim: PASS <= 0.30, RELOC >= 0.70) on every fitted level and
    on the margins t_R - rho_5 and 1 - bound.

CONV RULE (frozen BEFORE the run).  For datum d let s, e be FIT-CELL's
slope and 2SE, and let C = max over consecutive blocks of
|L_{b+1} - L_b| / max(1, |L_b|) be the relative Cauchy width.
 CONVERGENT-MEASURED  iff |s| + e <= CONV_FLAT = 0.15 AND
                          C <= CAUCHY_BAR = 0.35
 DRIFTING             iff |s| - e > 0 AND |s| > CONV_FLAT
 NOISY                otherwise.
The three cases are exhaustive and disjoint by construction; no case
is decided by a number seen in the frozen run.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum, dominance order):
 DEEP-MEMBERSHIP-BREACH(cell) -- a built WALL-LEGAL cell certifies
   rho_5 >= t_R or has truth sigma >= 1: the class-membership question
   is answered NEGATIVELY on the deployed deep frame and the whole
   limit lane is dead.  (The cell is named with its full anatomy.)
 DEEP-MEMBERSHIP-DRIFTS(law) -- no breach, but the DECISIVE datum
   (the block envelope of rho_5) DRIFTS upward: the extrapolated
   crossing h where the envelope fit reaches t_R is reported as the
   honest risk number.
 DEEP-MEMBERSHIP-LIMIT-PARTIAL(the drifting/noisy data listed) -- the
   decisive datum is stationary but part of the entry-data vector is
   not: the composed architecture is blocked at the named datum.
 DEEP-MEMBERSHIP-LIMIT-COMPOSED(limit levels, rate bound, margin) --
   every datum h-stationary, the reconstructed limit satisfies RAD
   with margin, and the all-large-h architecture is stated
   conjecture-grade with all three premises typed.
Plus typed tags: LEGALITY(the depth census of illegal cells),
MECHANISM, SCREENS, CONTROLS, CENSUS, AMENDMENTS.  Every enum is a
FINITE float64/exact-rational statement about the deployed
construction on BUILT cells plus an explicitly CONJECTURE-GRADE
extrapolation; NEVER an unconditional all-h statement, NEVER an RH
claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; IDENT_TIE =
1e-12; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7; SIGMA_MAX_REF =
0.604556 (rtol 2e-3); LAMB_MIN_REF = 0.3496, PIV_MIN_REF = 0.082730
(rtol 5e-2); F5_SIG_REF = 0.297 (rtol 5e-2); KBASE = 4; KDEEP = 5;
KMOM = 8 (nu_0..nu_8, the K = 5 requirement); SCHUR_BAR = 1 (exact);
SIGMA_ENV = T_R = 7809/10000 (CCLXIX registration at its cited
4-digit truncation -- the truncation direction makes the bar HARDER);
BIS_ITERS = 40; RADAU_SIGN_TIE = 1e-12; XR_TIE = 1e-6; COEF_TIE =
1e-6; CERT_GAP_RTOL = 1e-6; NODE_TIE = 1e-9; SCALE_SET = (1e-3, 1,
1e3), SCALE_TIE = 1e-9; TAB2 = 1.6e7; KZ2_MAX = 1200; H5_CAP = 4200;
N5 = 4; NB = 5; BLOCK_TGT = (1300, 2400, 3300, 4178, FRONTIER);
BLOCK_NC = (8, 8, 6, 8, 4); CONV_FLAT = 0.15; CAUCHY_BAR = 0.35;
MEDOID_KEYS = (r_floor, g0, gslope, gresid, sigma, rho5);
MECH_TGT = (1300, 2400); MECH_N = 3; CH_N = 4; CH_HMAX = 2900;
SCR_SEED = 1; CTRL_INFLATE = 1.01; CTRL_SIG_NEAR = 1.2; SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; COST_C = 3.88e-10 s (machine calibration,
DISCLOSED, measured in the pre-freeze reconnaissance below);
GUARD_FAC = 1.6; HARD_CAP_S = 1320 s; FRONTIER_BUDGET_S = 620 s;
runtime cap 25 min.  Smoke:
ladder 10 contiguous surface rungs + 3 lowest deep; BLOCK_TGT
(600, 900) with BLOCK_NC (3, 3); F5 gate SKIPPED (typed); MECH_TGT
(600,) MECH_N 1; CH_N 2; SR / G1 / W counts bypassed by design (the
smoke ladder is not the 68-step artifact ladder -- the CCLXI / CCLXIX
/ CCLXXVII identical smoke phenomenon) and print their subset values.

HONEST AMENDMENTS (declared before the frozen run).
 A1 PRE-FREEZE RECONNAISSANCE, fully disclosed (four throwaway runs,
    deleted; NO bar, rule, control or enum was chosen in response to
    a measured value, and the two facts below are DESIGN INPUTS, not
    results):
    (i) the COST LAW: the deep cell build cost is COST_C * h^3 with
        COST_C = 3.88e-10 s measured at h = 5167 (53.2 s) and h = 6197
        (91.8 s) and confirmed at h = 4178 (28.3 s) -- this fixes the
        block sizes and the guard, nothing else;
    (ii) the CONTIGUITY LESSON: a first reconnaissance used a
        LOG-SPACED h ladder and produced wildly incoherent raw data
        (n from 0.09 to 36.9 on neighbouring entries) because the
        deployed normalization divides by the PREVIOUS rung's tau and
        log-spaced neighbours have tau ratios of 20x and more.  The
        block design (contiguous census segments) is the corrected
        design; the failed ladder is disclosed here and is NOT part
        of the frozen run.
    The reconnaissance also observed one ILLEGAL census cell at
    h = 6197 (negA = 1, tau < 0).  That observation is what motivates
    the LEGALITY tag and amendment A3 -- disclosed; the cell is
    rebuilt inside the frozen run and its legality decided there.
 A2 the block/contiguity design is a DEPARTURE from a naive reading
    of "the deep ladder": the deployed chain step pairs adjacent
    census cells, so a limit statement about chain-step data must be
    taken along contiguous census segments.  Bridge steps (from the
    nearest registered anchor) are computed as well and are the
    SECOND declared formation; both are reported, and the class
    statement is required to hold on BOTH.
 A3 CCLXXIX's F5 selection filtered cells by (core_ok AND no build
    failure) only -- it did NOT apply the negA = 0 / lamS > 0 / tau > 0
    part of CCLXXIII's cell_legal.  This probe uses the STRICT
    cell_legal for its own family and census, and runs the F5
    reproduction gate with CCLXXIX's WEAKER filter verbatim so the
    reproduction is faithful.  The difference is printed.
 A4 best bound = min over the consumed depths K needs NO
    monotonicity-in-K assumption: each depth's exact Radau value is an
    INDEPENDENTLY warded upper bound for the same q (RB1 at that
    depth), so the minimum of finitely many warded upper bounds is an
    upper bound (CCLXXIX A4 verbatim).
 A5 the certificate object is the ASSEMBLED float64 wall matrix
    (dyadic-rational entries, CCVII v897 class) -- CCLXXVII A3 /
    CCLXXIX A5 verbatim: the float64-vs-ideal enclosure stays with the
    pg_chain interval program (round 63 / CCXLI) and is NOT retried
    here; it is the known scope edge of the composed chain.
 A6 the smooth and arch worlds are expected to leave wall-legality
    outright (the reconnaissance saw tau < 0 in both).  The
    discrimination control X2 therefore reports BOTH readings: the
    legality verdict (the primary, strongest discrimination) AND, as
    a DECLARED DIAGNOSTIC, the entry data of the refused step
    normalized by |tau_1| -- a diagnostic, never a wall-legal step,
    never counted in any census.
 A7 the mission cites the wedge saturation law (s_P/mu1 -> 1 at
    depth) and the deep flatness measurements as motivation.  NO
    number of those probes is consumed anywhere in this probe's
    gates, certificates or verdict; they are cited as motivation
    only, by name.
 A8 with 5 blocks the FIT-BLOCK 2SE band is wide by construction
    (n = 5, 3 degrees of freedom).  The CONV RULE therefore decides on
    FIT-CELL (all legal cells, ~35 points) and reports FIT-BLOCK and
    FIT-ENV as confirmation.  Declared before the run.
 A9 the frontier block's depth is set by a FROZEN BUDGET, not by a
    measured value: it is the DEEPEST contiguous BLOCK_NC[-1]-cell
    segment of the census whose guarded cost sum GUARD_FAC * COST_C *
    sum h^3 stays <= FRONTIER_BUDGET_S.  The rule is arithmetic on
    the frozen cost law, fixed before the run.
 A10 rung builds are CACHED by (kz, world): the F5 reproduction gate
    and the deep blocks overlap in the h <= 4200 range, and rebuilding
    the same cell twice would only burn budget.  The cache is keyed on
    the full frame identity and returns the identical object; no gate
    is weakened.
 A11 THE RECONSTRUCTION RULE WAS CORRECTED BEFORE THE FREEZE, driven by
    SMOKE-1 (below).  The first draft made the per-datum LEVEL vector
    the limit object and evaluated RAD on it, plus a box-corner
    "worst case" over the moments.  The smoke measured both to be
    mathematically void: the deep moment shape is one-atom, so neither
    the coordinate-wise median nor a box corner is a moment sequence at
    all (Hankel singular).  The corrected rule -- LEVEL vector as a
    reported summary + the moment-shape collapse as a MEASUREMENT + an
    ACTUAL MEDOID MEMBER as the limit object with an EXACT coherence
    ward + the MEASURED envelope as the worst case -- is strictly
    stronger (it removes a fit and adds an exact identity) and is fully
    disclosed here.  Nothing about the frozen bars, the census, the
    blocks or the gates changed.
 A12 THE BRIDGE FORMATION WAS CORRECTED AFTER FROZEN RUN 1 (disclosed
    below).  Several deep census cells ARE registered CCVII/CCXXV
    ladder rungs, so "the nearest registered anchor with h <= h(cell)"
    could be the CELL ITSELF; run 1 contained 5 such SELF-BRIDGES, and
    a self-bridge is vacuous by construction (n = 1, b = 0, sigma = 0,
    rho = 0 exactly -- no moment shape at all).  They were polluting
    the g_k statistics (the g_k spread ran to log10 nu_0 ~ -26) and
    nothing else.  The anchor is now required to be STRICTLY below the
    cell in (kz, h), the self-bridge count is CENSUSED, and any step
    with nu_0/n^2 < DEGEN_BAR is typed DEGENERATE-B and censused.  No
    bar, no gate, no certificate and no legality verdict changed.
 A13 THE ARCHITECTURE STATEMENT IS NOW GENERATED FROM THE MEASUREMENT.
    Run 1's draft text asserted "certified bound <= ... and <= t_R"
    unconditionally and then computed a NEGATIVE convergence budget
    t_R - envelope without saying so -- i.e. it printed a FALSE
    sentence and a vacuous one.  The statement now carries BOTH bars
    explicitly (the DEFINITENESS bar 1 and the registered CLASS bar
    t_R), reports which one the census holds and which it breaches,
    and states the convergence budget separately for each.  Reporting
    only; no measurement changed.
 A14 the L-section text of runs 1 and 2 promised an "ILLEGAL-R2 band"
    of steps built on wall-illegal cells.  No such band is built and
    none should be: an illegal cell has tau <= 0 or negA > 0, so its
    step frame is not defined and a "step" on it would be meaningless.
    The illegal cells are censused with their failure reason in the
    LEGALITY CENSUS line and form NO steps.  The unfulfilled promise is
    removed from the text; frozen run 3 carries the corrected spec.

FROZEN RUN 1 DISCLOSURE (SPEC_SHA e9f6659a, 838.6 s, 55/58) -- the run
 that produced the finding, kept in the record because the finding is
 the deliverable and the corrections A12/A13 do not touch it.
 VERDICT 1: DEEP-MEMBERSHIP-BREACH(block 4 bridge kz 340 h 6280:
   rho_5 = 0.787603 > t_R = 0.7809, truth sigma = 0.751875, certified
   bound 0.787603) ; LEGALITY(32/34, failures h 6197 kz 337 NEGA,
   h 6247 kz 436 NEGA) ; CERT-FINITE(worst bound 0.787603 on 59 steps).
 The three FAILED checks (BR1, CV2, LIM3) were ONE fact: the single
 frontier bridge step at h = 6280 exceeds the registered t_R bar by
 0.0067 while remaining 0.2124 below the definiteness bar 1.  The
 corrections A12/A13 were made because run 1's OTHER output was
 defective (5 vacuous self-bridges in the g_k statistics; a false
 sentence in the architecture text), NOT because of the breach.

FROZEN RUN 2 DISCLOSURE (SPEC_SHA 5daf7855, 850.7 s, 55/58): the
 verdict, the breach cell, the legality failures, the certified worst
 bound, the medoid limit member and every LIM number REPRODUCED run 1
 to the last printed digit; A12 removed the 5 self-bridges (the tau
 screens went from 3 PASS / 3 AMBIG to 6 PASS / 0 AMBIG and the g_k
 rows from 9 NOISY to 3 DRIFTING + 6 NOISY, confirming the vacuous
 rows had been the pollution) and A13 replaced the false architecture
 sentence.  Run 3 (this spec) adds A14 only, a text correction.

SMOKE DISCLOSURE (2026-08-12), pre-freeze, verbatim.
 SMOKE-1 (46/47, WARD-BROKEN, 2.8 s, 2 blocks, 10 steps): the wards,
   the exact tier, the census and the gates all passed; the SINGLE
   failure was LIM1 in its first form -- "the reconstructed limit
   moment vector is a VALID moment sequence (E7 Hankel PD)" FAILED at
   failing minor 2 (K = 4) and 2 (K = 5).  Diagnosis (not a bug in the
   machine, a defect in the SPEC): the measured deep level vector had
   g_k = 2.1821, 5.0729, 8.0135, 10.8869, 13.7965, 16.7064, 19.6163,
   22.5263, 25.4363 -- differences 2.891, 2.941, 2.873, 2.910, 2.910,
   2.910, 2.910, 2.910, i.e. a GEOMETRIC moment sequence, whose Hankel
   matrix has rank 1 and is singular, not PD.  This is a real structural
   fact about the deep frame (b is nearly an eigenvector of B), so the
   spec was corrected per A11 rather than the ward loosened.  Secondary
   smoke findings, all fixed pre-freeze: the coherence ward passed
   VACUOUSLY on two NaNs (now requires finiteness and is exact); the
   envelope R2 print was garbled by a placeholder helper (now the
   fitted R2); the frontier block was picked against half the hard cap
   instead of its own budget (now A9).

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXXXVII line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder, rung
builder, three-way split), zolotarev_phase_filter_probe (CCXXV step
assembly), sigma_stress_battery_probe (CCLXIX families and builders,
imported READ-ONLY), bfloor_perstep_certification_probe (CCLXXVII
exact machine, reproduced verbatim), bfloor_k5_closure_probe (CCLXXIX
K = 5 tier and F5 rule, reproduced verbatim),
radau_class_assembly_probe (CCLXXXI joint relation and the Lambda
closed form, reproduced verbatim), sigma_edge_growth_probe (CCLXXIII
cell_legal and the cost-guard pattern), euler_phase_identity_probe
(CCXVII c_h), v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_membership_limit_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_membership_limit_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)
import sigma_stress_battery_probe as bat      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
IDENT_TIE = 1.0e-12
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
SIGMA_MAX_REF = 0.604556
SIGMA_RTOL = 2.0e-3
LAMB_MIN_REF = 0.3496
PIV_MIN_REF = 0.082730
REPRO_RTOL = 5.0e-2
F5_SIG_REF = 0.297
F5_RTOL = 5.0e-2
KBASE = 4
KDEEP = 5
KMOM = 8
SCHUR_BAR = Fraction(1)
SIGMA_ENV = Fraction(7809, 10000)
T_R = SIGMA_ENV
T_R_F = float(T_R)
BIS_ITERS = 40
RADAU_SIGN_TIE = 1.0e-12
XR_TIE = 1.0e-6
COEF_TIE = 1.0e-6
CERT_GAP_RTOL = 1.0e-6
NODE_TIE = 1.0e-9
SCALE_SET = (1.0e-3, 1.0, 1.0e3)
SCALE_TIE = 1.0e-9
TAB2 = 16_000_000
KZ2_MAX = 1200
H5_CAP = 4200
N5 = 4
NB = 5
BLOCK_TGT = (1300, 2400, 3300, 4178, None)   # None = the frontier
BLOCK_NC = (8, 8, 6, 8, 4)
FRONTIER_BUDGET_S = 620.0
CONV_FLAT = 0.15
CAUCHY_BAR = 0.35
DEGEN_BAR = 1e-12
MECH_TGT = (1300, 2400)
MECH_N = 3
CH_N = 4
CH_HMAX = 2900
SCR_SEED = 1
CTRL_INFLATE = 1.01
CTRL_SIG_NEAR = 1.2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
COST_C = 3.88e-10
GUARD_FAC = 1.6
HARD_CAP_S = 1320.0
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: the bound/certificate path may see wall ENTRIES and frozen
# constants only (CCLXV / CCLXXVII / CCLXXIX ban list verbatim).
DERIV_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h", "gap", "lamB1", "sigma", "sigma_quotient",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "theta", "row", "rows", "step", "steps")
CERT_FUNCS = ("exact_wall_data", "chebyshev_monic", "radau_exact",
              "fr_solve", "pd_exact", "cert_floor_exact", "chol_iv",
              "hankel_pd")
FLOAT_FUNCS = ("wall_moments", "lanczos_pair", "radau_upper",
               "rho_source")

# the datum dictionary of the normalized entry-data vector (NORM-P).
# gslope / gresid are the SHAPE coordinates of the moment sequence:
# g_k is fitted linearly in k, gslope = log10 of the dominant scale
# ratio nu_{k+1}/(nu_k n) and gresid = the residual spread (gresid = 0
# exactly for a one-atom measure).  Both scale-invariant.
DATA_KEYS = (["r_floor"] + ["g%d" % k for k in range(KMOM + 1)]
             + ["gslope", "gresid", "sigma", "rho4", "rho5"])
MEDOID_KEYS = ("r_floor", "g0", "gslope", "gresid", "sigma", "rho5")
RAW_KEYS = (["n_piv", "c_meas"]
            + ["nu%d" % k for k in range(KMOM + 1)])

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(values):
    v = np.asarray(values, float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return (float("nan"),) * 3
    return (float(np.min(v)), float(np.median(v)), float(np.max(v)))


def f4(values):
    return "%.4f/%.4f/%.4f" % trio(values)


def linfit(x, y):
    """OLS y = a + s x (CCLIII verbatim); returns s, 2SE, R^2, a."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan"), float(ym)
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * xm
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, 2.0 * se, r2, a


def screen(values, scales, label):
    """CCXLVII relocation screen, bars inherited verbatim."""
    v = np.asarray(values, float)
    s = np.asarray(scales, float)
    pos = (v > 0.0) & (s > 0.0) & np.isfinite(v) & np.isfinite(s)
    if int(np.sum(pos)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(pos))),
                "VAC")
    slope, _2se, r2, _a = linfit(np.log(s[pos]), np.log(v[pos]))
    verd = ("PASS" if abs(slope) <= SLOPE_PASS
            else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope=%+.3f,R2=%.3f,%d excl)"
            % (label, verd, slope, r2, int(np.sum(~pos))), verd)


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# =========================================== Jacobi form (CCLIII)
def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- CCLIII/CCLXI/CCLXV
    machinery reproduced verbatim.  Returns (a, b) or None."""
    if not np.all(np.isfinite(matrix)):
        return None
    n = NDIM
    qq = np.zeros((n, n))
    qq[0, 0] = 1.0
    a = np.zeros(n - 1)
    b = np.zeros(n)
    for k in range(n):
        z = matrix @ qq[:, k]
        b[k] = float(qq[:, k] @ z)
        z = z - b[k] * qq[:, k]
        if k > 0:
            z = z - a[k - 1] * qq[:, k - 1]
        for _ in range(2):
            z = z - qq[:, :k + 1] @ (qq[:, :k + 1].T @ z)
        if k == n - 1:
            break
        nz = float(np.linalg.norm(z))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b


def theta_matrices(theta):
    """theta = (b_1..b_8, a_1..a_7) -> (J, J_B) (CCLXI verbatim)."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def sigma_quotient(theta):
    """sigma = a_1^2 [J_B^-1]_11 / b_1 (CCLXI verbatim)."""
    _jm, jb = theta_matrices(theta)
    b1 = float(theta[0])
    a1 = float(theta[NDIM])
    if b1 == 0.0:
        return float("inf")
    try:
        e1 = np.zeros(NDIM - 1)
        e1[0] = 1.0
        mb = float(np.linalg.solve(jb, e1)[0])
    except np.linalg.LinAlgError:
        return float("inf")
    return a1 * a1 * mb / b1


# ============= float bound path (CCLXV verbatim, AC-scanned)
def wall_moments(matrix, kdeg):
    """nu_k = b^T B^k b, k = 0..kdeg, from the ENTRIES of the wall
    matrix.  No eigensolver, no inverse, no pivot read."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    out = []
    cur = vec.copy()
    for _k in range(kdeg + 1):
        out.append(float(vec @ cur))
        cur = blk @ cur
    return np.asarray(out, float)


def lanczos_pair(matrix, kdeg):
    """Lanczos data of (B, b/||b||) from the wall ENTRIES (CCLXV
    verbatim); forward recursion only."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    dim = blk.shape[0]
    nrm = float(np.linalg.norm(vec))
    if not math.isfinite(nrm) or nrm <= 0.0:
        return None
    frame = np.zeros((dim, kdeg))
    frame[:, 0] = vec / nrm
    alp = []
    bet = []
    for j in range(kdeg):
        zvec = blk @ frame[:, j]
        aj = float(frame[:, j] @ zvec)
        alp.append(aj)
        zvec = zvec - aj * frame[:, j]
        if j > 0:
            zvec = zvec - bet[j - 1] * frame[:, j - 1]
        for _ in range(2):
            zvec = zvec - frame[:, :j + 1] @ (frame[:, :j + 1].T
                                              @ zvec)
        if j == kdeg - 1:
            break
        nz = float(np.linalg.norm(zvec))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(aj)):
            return None
        bet.append(nz)
        frame[:, j + 1] = zvec / nz
    return np.asarray(alp, float), np.asarray(bet, float), nrm * nrm


def radau_upper(alp, bet, floor_c, mass):
    """E3 Gauss-Radau upper bound for b^T B^{-1} b at depth
    K = len(alp) with the node prescribed at floor_c (CCLXV
    verbatim); the node ward is done by the CALLER."""
    kdeg = len(alp)
    jac = np.diag(np.asarray(alp, float)).copy()
    for i in range(kdeg - 1):
        jac[i, i + 1] = jac[i + 1, i] = float(bet[i])
    if kdeg > 1:
        shifted = jac[:kdeg - 1, :kdeg - 1] - floor_c * np.eye(
            kdeg - 1)
        rhs = np.zeros(kdeg - 1)
        rhs[-1] = float(bet[kdeg - 2]) ** 2
        try:
            sol = np.linalg.solve(shifted, rhs)
        except np.linalg.LinAlgError:
            return float("nan"), None
        jac[kdeg - 1, kdeg - 1] = floor_c + float(sol[-1])
    else:
        jac[0, 0] = floor_c
    unit = np.zeros(kdeg)
    unit[0] = 1.0
    try:
        val = float(np.linalg.solve(jac, unit)[0]) * mass
    except np.linalg.LinAlgError:
        return float("nan"), None
    return val, jac


def rho_source(matrix, floor_c, kdeg):
    """THE SOURCE-ONLY RATIO rho_K = RADAU_K(nu; floor_c) / n from the
    wall ENTRIES and the floor (CCLXV verbatim, scale-invariant)."""
    piv = float(np.asarray(matrix, float)[0, 0])
    lan = lanczos_pair(matrix, kdeg)
    if lan is None or piv <= 0.0:
        return float("nan"), None
    alp, bet, mass = lan
    val, jac = radau_upper(alp, bet, floor_c, mass)
    if not math.isfinite(val):
        return float("nan"), None
    return val / piv, jac


# ============ the exact-rational tier (round 62 + E4, AC-scanned)
def exact_wall_data(matrix, kdeg):
    """Pivot n, b-weighted moments nu_0..nu_kdeg and the co-block, ALL
    as exact Fractions of the dyadic float64 ENTRIES (CCVII v897
    class).  No eigensolver, no inverse, no read."""
    mm = np.asarray(matrix, float)
    dim = mm.shape[0] - 1
    piv = Fraction(float(mm[0, 0]))
    vec = [Fraction(float(v)) for v in mm[1:, 0]]
    blk = [[Fraction(float(mm[i + 1, j + 1])) for j in range(dim)]
           for i in range(dim)]
    cur = list(vec)
    momv = []
    for _k in range(kdeg + 1):
        momv.append(sum(a * c for a, c in zip(vec, cur)))
        cur = [sum(blk[i][j] * cur[j] for j in range(dim))
               for i in range(dim)]
    return piv, momv, blk


def chebyshev_monic(momv, kdeg):
    """E4 Chebyshev algorithm, EXACT and depth-generic: monic
    recurrence al_1..al_{k-1}, be_1..be_{k-1} (be = squared symmetric
    betas) of the measure with power moments momv[0..2k-2].  None on
    degeneracy."""
    need = 2 * kdeg - 1
    if len(momv) < need or momv[0] <= 0:
        return None
    tab = {-1: [Fraction(0)] * need, 0: list(momv[:need])}
    al = [momv[1] / momv[0]]
    be = []
    for k in range(1, kdeg):
        prev = tab[k - 1]
        pprev = tab[k - 2]
        cur = [Fraction(0)] * need
        for pos in range(k, 2 * kdeg - 1 - k):
            cur[pos] = (prev[pos + 1] - al[k - 1] * prev[pos]
                        - (be[k - 2] * pprev[pos] if k >= 2
                           else Fraction(0)))
        tab[k] = cur
        if prev[k - 1] <= 0 or cur[k] <= 0:
            return None
        be.append(cur[k] / prev[k - 1])
        if 2 * kdeg - 1 - k > k + 1:
            al.append(cur[k + 1] / cur[k] - prev[k] / prev[k - 1])
    if len(al) != kdeg - 1 or len(be) != kdeg - 1:
        return None
    return al, be


def fr_solve(amat, rhs):
    """Exact Gaussian elimination with nonzero pivoting on Fractions;
    returns the solution list or None if singular."""
    dim = len(amat)
    aa = [list(r) + [rhs[i]] for i, r in enumerate(amat)]
    for k in range(dim):
        pr = None
        for i in range(k, dim):
            if aa[i][k] != 0:
                pr = i
                break
        if pr is None:
            return None
        aa[k], aa[pr] = aa[pr], aa[k]
        pv = aa[k][k]
        for i in range(k + 1, dim):
            f = aa[i][k] / pv
            if f == 0:
                continue
            for j in range(k, dim + 1):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    out = [Fraction(0)] * dim
    for k in range(dim - 1, -1, -1):
        acc = aa[k][dim]
        for j in range(k + 1, dim):
            acc = acc - aa[k][j] * out[j]
        out[k] = acc / aa[k][k]
    return out


def radau_exact(al, be, flo, mass):
    """EXACT-RATIONAL Gauss-Radau upper-bound value for the 1/x
    integral at depth K = len(al)+1 with the node prescribed at flo:
    monic form (E6).  Depth-generic (CCLXXVII verbatim)."""
    kdeg = len(al) + 1
    dim = kdeg - 1
    tm = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(dim):
        tm[i][i] = al[i] - flo
        if i + 1 < dim:
            tm[i][i + 1] = be[i]
            tm[i + 1][i] = Fraction(1)
    rhs = [Fraction(0)] * dim
    rhs[dim - 1] = Fraction(1)
    sol = fr_solve(tm, rhs)
    if sol is None:
        return None
    alr = flo + be[kdeg - 2] * sol[dim - 1]
    tt = [[Fraction(0)] * kdeg for _ in range(kdeg)]
    for i in range(kdeg):
        tt[i][i] = al[i] if i < kdeg - 1 else alr
        if i + 1 < kdeg:
            tt[i][i + 1] = be[i]
            tt[i + 1][i] = Fraction(1)
    rhs2 = [Fraction(0)] * kdeg
    rhs2[0] = Fraction(1)
    sol2 = fr_solve(tt, rhs2)
    if sol2 is None:
        return None
    return mass * sol2[0]


def pd_exact(afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision (round 62 verbatim)."""
    dim = len(afr)
    aa = [[afr[i][j] - (shift if i == j else 0) for j in range(dim)]
          for i in range(dim)]
    for k in range(dim):
        p = aa[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, dim):
            f = aa[i][k] / p
            for j in range(k + 1, dim):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    return True, -1


def cert_floor_exact(afr, lo, hi, iters=BIS_ITERS):
    """Largest certified c in [lo, hi] with A - c I PD (round 62
    verbatim: dyadic bisection, NEVER rounded inward)."""
    lo = Fraction(lo)
    hi = Fraction(hi)
    if hi < lo:
        hi = lo
    ok, _ = pd_exact(afr, lo)
    if not ok:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok, _ = pd_exact(afr, mid)
        if ok:
            lo = mid
        else:
            hi = mid
    ok, _ = pd_exact(afr, lo)
    assert ok
    return lo


def hankel_pd(momv, kdeg):
    """E7: is the K x K Hankel matrix of nu_0..nu_{2K-2} PD (exact
    Fractions)?  The validity ward of a reconstructed limit moment
    vector."""
    han = [[momv[i + j] for j in range(kdeg)] for i in range(kdeg)]
    ok, idx = pd_exact(han)
    return ok, idx


def chol_iv(blk, shift):
    """Directed-rounding float64 interval Cholesky of (blk - shift I):
    True iff every symmetric matrix within one outward ulp of the
    exact elimination is PD (E5), None on a refused pivot."""
    nxt = np.nextafter

    def i_sub(alo, ahi, blo, bhi):
        return nxt(alo - bhi, -np.inf), nxt(ahi - blo, np.inf)

    def i_mul(alo, ahi, blo, bhi):
        cand = (alo * blo, alo * bhi, ahi * blo, ahi * bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    def i_div(alo, ahi, blo, bhi):
        cand = (alo / blo, alo / bhi, ahi / blo, ahi / bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    dim = blk.shape[0]
    alo = np.array(blk, float)
    ahi = np.array(blk, float)
    for i in range(dim):
        alo[i, i], ahi[i, i] = i_sub(alo[i, i], ahi[i, i],
                                     shift, shift)
    for k in range(dim):
        plo, phi = alo[k, k], ahi[k, k]
        if not (plo > 0.0):
            return None
        for i in range(k + 1, dim):
            flo, fhi = i_div(alo[i, k], ahi[i, k], plo, phi)
            for j in range(k + 1, dim):
                qlo, qhi = i_mul(flo, fhi, alo[k, j], ahi[k, j])
                alo[i, j], ahi[i, j] = i_sub(alo[i, j], ahi[i, j],
                                             qlo, qhi)
    return True


def lambda_closed(pivot, floor_c, rho):
    """CCLXXXI R3 closed form: Lambda(n, c, rho) = ((n + c) -
    sqrt((n - c)^2 + 4 n c rho)) / 2, the SOURCE-ONLY lower bound for
    the single eigenvalue below the co-block floor.  Positive iff
    rho < 1 (with n, c > 0)."""
    if not (pivot > 0.0 and floor_c > 0.0) or not math.isfinite(rho):
        return float("nan")
    disc = (pivot - floor_c) ** 2 + 4.0 * pivot * floor_c * rho
    if disc < 0.0:
        return float("nan")
    return 0.5 * ((pivot + floor_c) - math.sqrt(disc))


# ====================================================== wall ladder
def build_ladder():
    section("W -- the registered CCVII/CCXXV ladder, rebuilt "
            "read-only (the anchors of the CCLXIX bridge pattern)")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
        print("    SMOKE: %d contiguous surface rungs" % len(zones))
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W2 all surface chains complete",
          all(r is not None for r in surface), kill="K1")
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    if SMOKE:
        census = census[:3]
    deep = []
    for kz, hz in census:
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep
               if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    combined = sorted([r for r in surface
                       if r is not None and r["core_ok"]] + deep_ok,
                      key=lambda r: (r["h"], r["kz"]))
    steps = ob.make_steps(combined)
    for st in steps:
        zol.assemble_step(st)
    steps = [st for st in steps if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in steps]
    ok = (SMOKE or (len(steps) == STEPS_EXP
                    and segs.count("surf") == 40
                    and segs.count("bridge") == 1
                    and segs.count("deep") == 27))
    check("W3 combined steps %d = surface %d + bridge %d + deep %d"
          % (len(steps), segs.count("surf"), segs.count("bridge"),
             segs.count("deep")), ok, kill="K1")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"]))
              for r in artifact["rungs"]}
    ours = {(int(st["r1"]["h"]), int(st["r1"]["kz"]),
             int(st["r2"]["h"]), int(st["r2"]["kz"]))
            for st in steps}
    n_match = len(stored & ours)
    check("W4 ladder identity: %d/%d step keys match the stored "
          "CCXLVII artifact" % (n_match, len(ours)),
          SMOKE or (n_match == STEPS_EXP and len(ours) == STEPS_EXP),
          kill="K2")
    return steps, combined


# ============================================ TAB2 + the deep census
DEEP = {}


def build_tab2():
    section("T -- the CCLXIX depth-extension table TAB2 = %.3g, "
            "warded BITWISE against the deployed 4e6 prefix" % TAB2)
    lam2 = core.von_mangoldt_table(TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    g2 = np.diff(u2)
    n_pref = len(ob.EXT["NN"])
    check("T1 TAB2 prefix ward: the 1.6e7 arrays agree BITWISE with "
          "the deployed 4e6 EXT arrays (%d atoms of %d)"
          % (n_pref, len(nn2)),
          (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
           and np.array_equal(u2[:n_pref], ob.EXT["U"])
           and np.array_equal(mu2[:n_pref], ob.EXT["MU"])),
          kill="K2")
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = g2
    return u2, mu2, g2


def deep_census():
    section("D -- THE DEEP-FRAME CENSUS on TAB2 (deployed deep frame "
            "formula verbatim), h-sorted, with the frozen cost law")
    u2, _mu2, g2 = DEEP["U"], DEEP["MU"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(core.NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        hz = mz // 2
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=hz, kz=kz, alpha=alpha, M=mz, X=x_val))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    print("    census %d cells, h %d .. %d; cost law %.3e * h^3 s "
          "(frozen, machine calibration -- amendment A1)"
          % (len(out), int(hs.min()), int(hs.max()), COST_C))
    for lo, hi in ((0, 900), (900, 2900), (2900, 4200), (4200, 6300),
                   (6300, 10 ** 9)):
        sub = hs[(hs > lo) & (hs <= hi)]
        cost = float(np.sum(COST_C * sub ** 3))
        print("      h in (%6d, %9d]: %4d cells, full-build cost "
              "%.0f s" % (lo, hi, len(sub), cost))
    check("D1 the deep census is non-empty and reaches past the "
          "CCLXXIX F5 frontier h = 4178 (%d cells above it)"
          % int(np.sum(hs > 4178)), int(np.sum(hs > 4178)) > 0,
          kill="K1")
    return out


def cell_legal(rung):
    """CCLXXIII/CCLXIX wall-legality of a single cell, VERBATIM."""
    if rung is None:
        return False, "NONE"
    if "fail" in rung:
        return False, rung["fail"]
    if not rung.get("core_ok"):
        return False, "CORE-SHORT"
    if rung["negA"] > 0:
        return False, "NEGA"
    if rung.get("lamS", -1.0) <= 0.0:
        return False, "LAMS"
    if rung["tau"] <= 0.0:
        return False, "TAU"
    return True, "OK"


_CELL_CACHE = {}


def build_cell(cell, world=None, scr_seed=None, with_split=False):
    """The deployed deep-branch rung builder at (alpha, M, atoms)
    explicit -- bat.build_rung_param VERBATIM for the default world;
    the split branch reproduces ob.build_rung's CCIII three-way
    split for the SAME parametric frame.  Cached by the full frame
    identity (amendment A10)."""
    key = (int(cell["kz"]), int(cell["M"]), world, scr_seed,
           bool(with_split))
    if key in _CELL_CACHE:
        return _CELL_CACHE[key]
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "arch":
        mm = np.zeros_like(mm)
    elif world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    if not with_split:
        rung = bat.build_rung_param(cell["kz"], alpha, mfold, uu, mm)
        rung["X"] = cell["X"]
    else:
        rung = build_cell_split(cell, uu, mm)
    _CELL_CACHE[key] = rung
    return rung


def build_cell_split(cell, uu, mm):
    """bat.build_rung_param + ob.build_rung's CCIII exact three-way
    split S = S_AR + S_SM + S_OSC on the SAME parametric frame."""
    alpha, mfold = cell["alpha"], cell["M"]
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _ufp, fdp = ob.folded_measure_full(dens, lfold, +1.0)
    ys, vs, uf_n, fdn = ob.folded_measure_full(dens, lfold, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1 or np.any(be <= 0):
        return dict(kind="param", kz=cell["kz"], h=half, fail="CHAIN")
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = sym(np.sqrt(vs)[:, None] * (pn @ pn.T)
               * np.sqrt(vs)[None, :])
    ndim = gram.shape[0]
    amat = np.eye(ndim) - gram
    eva = np.linalg.eigvalsh(amat)
    out = dict(kind="param", kz=cell["kz"], h=half, n=ndim,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               X=cell["X"], tau=float(eva[0]),
               negA=int(np.sum(eva < 0.0)))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in ob.CORE_J)
    if not out["core_ok"]:
        out["fail"] = "CORE-SHORT"
        return out
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(ndim) if k not in icset],
                  dtype=int)
    bblk = amat[np.ix_(ic, ic)]
    xc = amat[np.ix_(ic, ib)]
    rblk = amat[np.ix_(ib, ib)]
    try:
        zsol = np.linalg.solve(rblk, xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        out["fail"] = "R-SINGULAR"
        return out
    smat = sym(bblk - xc @ zsol)
    out["S"] = smat
    out["lamS"] = float(np.linalg.eigvalsh(smat)[0])
    # ---- the CCIII exact three-way split
    ug, mg = ob.smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, mfold, ug, mg)[0],
                      float)
    d_ar = ob.grid_density(c_ar)
    d_sm = ob.grid_density(c_sm)
    wpos = {"AR": ob.folded_part(d_ar, fdp),
            "SM": ob.folded_part(d_sm, fdp)}
    wneg = {"AR": ob.folded_part(d_ar, fdn),
            "SM": ob.folded_part(d_sm, fdn)}
    sqv = np.sqrt(vs)
    zl = np.zeros((ndim, NDIM))
    zl[ic, np.arange(NDIM)] = 1.0
    zl[ib, :] = -zsol
    gn = zl / sqv[:, None]
    a8 = pn.T @ (sqv[:, None] * zl)
    fneg = pn @ a8
    del pn
    ppos = ob.eval_chain(al, be, m0, xs, half)
    fpos = ppos @ a8
    del ppos
    parts = {}
    for pkey in ("AR", "SM"):
        wn = wneg[pkey]
        wp = wpos[pkey]
        t1 = gn.T @ (wn[:, None] * gn)
        t2 = gn.T @ (wn[:, None] * fneg)
        t3 = fpos.T @ (wp[:, None] * fpos)
        parts[pkey] = sym(t1 - t2 - t2.T + t3)
    parts["OSC"] = sym(smat - parts["AR"] - parts["SM"])
    out["S_parts"] = parts
    _ = ws
    return out


def block_pick(census, target, ncell):
    """A CONTIGUOUS segment of the h-sorted census (amendment A2):
    ncell cells ENDING at the census cell nearest the target.  The
    FRONTIER block (target None) is the DEEPEST contiguous ncell-cell
    segment whose guarded cost sum fits FRONTIER_BUDGET_S -- pure
    arithmetic on the frozen cost law (amendment A9)."""
    hs = np.asarray([c["h"] for c in census], float)
    if target is None:
        end = ncell - 1
        for j in range(ncell - 1, len(census)):
            cost = GUARD_FAC * COST_C * float(np.sum(
                hs[j - ncell + 1:j + 1] ** 3))
            if cost <= FRONTIER_BUDGET_S:
                end = j
            else:
                break
    else:
        end = int(np.argmin(np.abs(hs - float(target))))
    lo = max(0, end - ncell + 1)
    return census[lo:end + 1]


def build_blocks(census):
    section("L -- THE DEEP BLOCKS: %d contiguous census segments "
            "(amendment A2), built behind the cost guard" % NB)
    tgts = (600, 900) if SMOKE else BLOCK_TGT
    ncs = (3, 3) if SMOKE else BLOCK_NC
    blocks = []
    legality = []
    for bi, (tgt, nc) in enumerate(zip(tgts, ncs)):
        picked = block_pick(census, tgt, nc)
        print("    BLOCK %d (target %s): %d contiguous census cells "
              "h %d .. %d"
              % (bi, tgt if tgt is not None else "FRONTIER",
                 len(picked), picked[0]["h"], picked[-1]["h"]),
              flush=True)
        rungs = []
        for cell in picked:
            est = GUARD_FAC * COST_C * float(cell["h"]) ** 3
            if time.time() - T0 + est > HARD_CAP_S:
                legality.append((bi, cell["h"], cell["kz"],
                                 "UNBUILT-GUARD"))
                print("      cell h %-6d kz %-4d UNBUILT-GUARD (est "
                      "%.0f s, elapsed %.0f s, cap %.0f s)"
                      % (cell["h"], cell["kz"], est,
                         time.time() - T0, HARD_CAP_S), flush=True)
                continue
            tc = time.time()
            rung = build_cell(cell)
            ok, why = cell_legal(rung)
            legality.append((bi, cell["h"], cell["kz"], why))
            print("      cell h %-6d kz %-4d alpha %.4f X %-10.4g "
                  "%-11s tau %-11s  %.1f s"
                  % (cell["h"], cell["kz"], cell["alpha"], cell["X"],
                     why, ("%.4g" % rung["tau"]) if "tau" in rung
                     else "-", time.time() - tc), flush=True)
            if ok:
                rung["mode"] = "deep-block"
                rung["block"] = bi
                rungs.append(rung)
        blocks.append(dict(index=bi, target=tgt, picked=picked,
                           rungs=rungs))
    n_tot = sum(len(b["picked"]) for b in blocks)
    n_ok = sum(len(b["rungs"]) for b in blocks)
    bad = [(h, kz, why) for _bi, h, kz, why in legality if why != "OK"]
    print("    LEGALITY CENSUS (CCLXXIII cell_legal verbatim): "
          "%d/%d cells wall-legal; failures: %s"
          % (n_ok, n_tot,
             "; ".join("h %d kz %d %s" % t for t in bad) or "none"))
    check("L1 the deep blocks built %d/%d census cells wall-legal "
          "(the failures are censused, never silently dropped)"
          % (n_ok, n_tot), n_ok >= (4 if SMOKE else 20), kill="K1")
    return blocks, legality


def block_steps(blocks, anchors):
    """The CCLXIX sweep_steps formations on each block: within-block
    chain pairs of CENSUS NEIGHBOURS + one bridge step per cell from
    its nearest registered anchor STRICTLY BELOW it (amendment A12:
    several deep census cells ARE registered ladder rungs, and pairing
    such a cell with itself produces a VACUOUS step -- n = 1, b = 0,
    sigma = 0 exactly -- which carries no moment shape at all; those
    self-bridges are censused and removed).  Steps landing on an
    ILLEGAL cell cannot occur here at all: illegal cells never enter a
    block's rung list, and the LEGALITY CENSUS line carries their
    failure reason."""
    rows = []
    n_self = 0
    anc = sorted(anchors, key=lambda r: r["h"])
    for blk in blocks:
        fam = sorted(blk["rungs"], key=lambda r: (r["h"], r["kz"]))
        pairs = [(r1, r2, "chain") for r1, r2 in zip(fam, fam[1:])]
        for r2 in fam:
            below = [a for a in anc
                     if a["h"] <= r2["h"]
                     and not (int(a["kz"]) == int(r2["kz"])
                              and int(a["h"]) == int(r2["h"]))]
            n_self += len([a for a in anc
                           if int(a["kz"]) == int(r2["kz"])
                           and int(a["h"]) == int(r2["h"])])
            if not below:
                continue
            pairs.append((below[-1], r2, "bridge"))
        for r1, r2, kind in pairs:
            sts = ob.make_steps([r1, r2])
            if not sts:
                continue
            st = sts[0]
            zol.assemble_step(st)
            if st["status"] != "OK":
                continue
            rows.append(dict(step=st, block=blk["index"],
                             mode=kind,
                             h=float(r2["h"]), kz=int(r2["kz"]),
                             alpha=float(r2["alpha"]),
                             X=float(r2["X"]),
                             tau_scale=float(st["tau"]),
                             schur=float(st["gap"]),
                             n_piv=float(st["n0"]),
                             c_meas=float(st["lamB1"])))
    for i, r in enumerate(rows):
        r["index"] = i
    n_deg = 0
    keep = []
    for r in rows:
        mt = np.asarray(r["step"]["Mt"], float)
        piv = float(mt[0, 0])
        vec = mt[1:, 0]
        if piv <= 0.0 or float(vec @ vec) / piv ** 2 < DEGEN_BAR:
            n_deg += 1
            continue
        keep.append(r)
    print("    SELF-BRIDGE census (amendment A12): %d block cells ARE "
          "registered ladder rungs -- their self-bridges are removed; "
          "%d further steps typed DEGENERATE-B (nu_0/n^2 < %.0e, no "
          "moment shape) and removed"
          % (n_self, n_deg, DEGEN_BAR))
    for i, r in enumerate(keep):
        r["index"] = i
    return keep


def f5_family(census, anchors):
    """G1: the CCLXXIX F5 rule VERBATIM (amendment A3 -- CCLXXIX's
    WEAKER filter is used here so the reproduction is faithful)."""
    section("G1 -- the CCLXXIX F5 reproduction gate (F5 rule "
            "verbatim, weaker filter per amendment A3)")
    if SMOKE:
        check("G1 F5 reproduction SMOKE-SKIPPED (typed)", True)
        return []
    reg_deep = {kz for kz, _hz in ob.deep_zone_census()}
    f5_new = []
    for cell in census:
        if cell["kz"] in reg_deep:
            continue
        newly = ((2900 < cell["h"])
                 or (cell["X"] > ob.TAB_EXT and 128 <= cell["h"]))
        if newly and cell["h"] <= H5_CAP:
            f5_new.append(cell)
    f5_new.sort(key=lambda c: -c["h"])
    pick = f5_new[:N5]
    print("    %d newly reachable frames, %d picked (h %s)"
          % (len(f5_new), len(pick),
             ", ".join(str(c["h"]) for c in pick)))
    rungs = []
    for cell in pick:
        rung = build_cell(cell)
        ok_weak = rung.get("core_ok") and "fail" not in rung
        ok_str, why = cell_legal(rung)
        print("      F5 cell h %-6d kz %-4d  weak-filter %s / "
              "strict %s  [%.1f s]"
              % (cell["h"], cell["kz"], "OK" if ok_weak else "REJ",
                 why, time.time() - T0), flush=True)
        if ok_weak:
            rung["mode"] = "depth-ext"
            rungs.append(rung)
    fam, n_ref = bat.sweep_steps(rungs, "F5", None, anchors)
    sigs = []
    for d in fam:
        jf = jacobi_form(d["step"]["Mt"])
        if jf is None:
            continue
        a, b = jf
        sigs.append(sigma_quotient(np.concatenate([b, a])))
    smax = max(sigs) if sigs else float("nan")
    print("    F5 steps %d (%d refused), sigma min/med/max %s"
          % (len(fam), n_ref, f4(sigs)))
    check("G1 CCLXXIX F5 sigma max %.6f reproduces %.3f (rtol %.0e)"
          % (smax, F5_SIG_REF, F5_RTOL),
          math.isfinite(smax)
          and abs(smax / F5_SIG_REF - 1.0) <= F5_RTOL, kill="K3")
    return fam


# ============================= B/I: translation + identity wards
def jacobi_identity_wards(rows, label):
    section("B/I -- Jacobi translation + the CCLXV identity wards on "
            "every %s cell" % label)
    d_b1 = d_a1 = d_bfl = d_m0 = d_q = d_sig = d_gap = 0.0
    n_bad = 0
    for row in rows:
        st = row["step"]
        jf = jacobi_form(st["Mt"])
        if jf is None:
            n_bad += 1
            row["theta"] = None
            continue
        a, b = jf
        theta = np.concatenate([b, a])
        row["theta"] = theta
        _jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(b[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(a[0] - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(_jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["schur"] - 1.0))
        piv = float(st["n0"])
        vec = np.asarray(st["bvec"], float)
        blk = np.asarray(st["Bblk"], float)
        q_wall = float(vec @ np.linalg.solve(blk, vec))
        sig = sigma_quotient(theta)
        row["sigma"] = sig
        row["q_wall"] = q_wall
        d_q = max(d_q, abs(sig * piv - q_wall) / max(1.0, abs(q_wall)))
        d_sig = max(d_sig, abs(sig - q_wall / piv)
                    / max(1.0, abs(sig)))
        d_gap = max(d_gap, abs(sig - (1.0 - row["schur"] / piv))
                    / max(1.0, abs(sig)))
    check("B1 Lanczos form of (M, e_0) exists on all %d %s cells"
          % (len(rows), label), n_bad == 0,
          "breakdowns %d" % n_bad, kill="K2")
    check("B2 TRANSLATE b_1 == M[0,0], a_1 == ||M[1:,0]||: %.2e / "
          "%.2e <= %.0e" % (d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill="K2")
    check("B3 TRANSLATE lambda_min(J_B) == lamB1 (E2 compression): "
          "max rel %.2e <= %.0e" % (d_bfl, TRANSLATE_TIE),
          d_bfl <= TRANSLATE_TIE, kill="K2")
    check("B4 WARD m(0) * gap == 1: max %.2e <= %.0e"
          % (d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill="K2")
    check("I1/I2 IDENTITY sigma * n == q == b^T B^-1 b: max rel "
          "%.2e / %.2e <= %.0e" % (d_q, d_sig, IDENT_TIE),
          d_q <= IDENT_TIE and d_sig <= IDENT_TIE, kill="K2")
    check("I3 IDENTITY sigma == 1 - s/n: max rel %.2e <= %.0e"
          % (d_gap, IDENT_TIE), d_gap <= IDENT_TIE, kill="K2")
    keep = [r for r in rows if r["theta"] is not None]
    pivs = [r["n_piv"] for r in keep]
    n_pos = sum(1 for r in keep if r["n_piv"] > 0.0)
    n_pos_x = sum(1 for r in keep
                  if Fraction(float(r["step"]["Mt"][0, 0])) > 0)
    check("P1 PIVOT SIGN n = M[0,0] > 0 on all %d %s cells (float AND "
          "exact rational): %d / %d positive, min %.6f"
          % (len(keep), label, n_pos, n_pos_x,
             min(pivs) if pivs else float("nan")),
          n_pos == len(keep) and n_pos_x == len(keep), kill="K2")
    return keep


def repro_anchors(lad_rows):
    section("SR -- repro anchors against CCLXV / CCLXIX")
    sig_max = max(r["sigma"] for r in lad_rows)
    lam_min = min(r["c_meas"] for r in lad_rows)
    piv_min = min(r["n_piv"] for r in lad_rows)
    check("SR1 ladder sigma max %.6f reproduces %.6f (rtol %.0e)"
          % (sig_max, SIGMA_MAX_REF, SIGMA_RTOL),
          SMOKE or abs(sig_max / SIGMA_MAX_REF - 1.0) <= SIGMA_RTOL,
          kill="K3")
    check("SR2 ladder lambda_min(B) min %.4f reproduces %.4f "
          "(rtol %.0e)" % (lam_min, LAMB_MIN_REF, REPRO_RTOL),
          SMOKE or abs(lam_min / LAMB_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")
    check("SR3 ladder pivot min %.6f reproduces %.6f (rtol %.0e)"
          % (piv_min, PIV_MIN_REF, REPRO_RTOL),
          SMOKE or abs(piv_min / PIV_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")


# ============================= E: the normalized entry-data vector
def entry_data(rows):
    """The entry-data vector per cell in BOTH declared
    normalizations, plus the exact-rational certification."""
    section("E/C -- the normalized entry-data vector (NORM-D raw + "
            "NORM-P scale-quotient) and the exact-rational "
            "certification at K = %d, %d" % (KBASE, KDEEP))
    d_coef = d_xr = d_gapc = 0.0
    sign_fail = node_fail = n_ref = n_deg = n_exceed = 0
    iv_conf = iv_ref = 0
    for row in rows:
        mat = row["step"]["Mt"]
        piv = float(mat[0, 0])
        mom = wall_moments(mat, KMOM)
        row["raw"] = dict(n_piv=piv, c_meas=row["c_meas"])
        for k in range(KMOM + 1):
            row["raw"]["nu%d" % k] = float(mom[k])
        pivf, momv, blkf = exact_wall_data(mat, 2 * KDEEP - 2)
        hi_hint = Fraction(float(row["c_meas"])) * (
            Fraction(1) + Fraction(1, 10 ** 6))
        c_cert = cert_floor_exact(blkf, Fraction(0), hi_hint)
        if c_cert is None:
            n_ref += 1
            row["c_cert"] = None
            row["bound_fr"] = None
            continue
        row["c_cert"] = c_cert
        c_f = float(c_cert)
        row["c_cert_f"] = c_f
        if c_f > row["c_meas"] * (1.0 + 1e-9):
            n_exceed += 1
        d_gapc = max(d_gapc, (row["c_meas"] - c_f)
                     / max(1.0, row["c_meas"]))
        lan = lanczos_pair(mat, KDEEP)
        cheb5 = chebyshev_monic(momv, KDEEP)
        if lan is not None and cheb5 is not None:
            alp, bet, _mass = lan
            for k in range(KDEEP - 1):
                d_coef = max(d_coef, abs(float(cheb5[0][k]) - alp[k])
                             / max(1.0, abs(alp[k])))
                d_coef = max(d_coef, abs(float(cheb5[1][k])
                                         - bet[k] ** 2)
                             / max(1.0, bet[k] ** 2))
        vals = {}
        for kd in (KBASE, KDEEP):
            cheb = chebyshev_monic(momv, kd)
            if cheb is None:
                n_deg += 1
                continue
            val_fr = radau_exact(cheb[0], cheb[1], c_cert, momv[0])
            if val_fr is None:
                n_deg += 1
                continue
            vals[kd] = val_fr / pivf
        if not vals:
            row["bound_fr"] = None
            continue
        for kd, bfr in sorted(vals.items()):
            if float(bfr) * piv < row["q_wall"] \
                    - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                sign_fail += 1
            val_f, jac = rho_source(mat, c_f, kd)
            if math.isfinite(val_f):
                d_xr = max(d_xr, abs(float(bfr) - val_f)
                           / max(1.0, abs(val_f)))
            if jac is not None:
                node = float(np.linalg.eigvalsh(jac)[0])
                if node < c_f - NODE_TIE * max(1.0, c_f):
                    node_fail += 1
        best = min(vals.values())
        row["bound_fr"] = best
        row["bound_f"] = float(best)
        row["k_used"] = min(kd for kd, v in vals.items() if v == best)
        row["vals"] = {kd: float(v) for kd, v in vals.items()}
        got = chol_iv(np.asarray(row["step"]["Bblk"], float), c_f)
        if got:
            iv_conf += 1
        else:
            iv_ref += 1
        # ---------- NORM-P: the scale-invariant entry-data vector
        rho4, _ = rho_source(mat, c_f, KBASE)
        rho5, _ = rho_source(mat, c_f, KDEEP)
        dat = dict(r_floor=c_f / piv, sigma=row["sigma"],
                   rho4=rho4, rho5=rho5)
        gs = []
        for k in range(KMOM + 1):
            val = float(mom[k]) / piv ** (k + 2)
            gk = math.log10(abs(val)) if val > 0.0 else float("nan")
            dat["g%d" % k] = gk
            gs.append(gk)
        if all(math.isfinite(v) for v in gs):
            sl, _e, _r2, a0 = linfit(list(range(KMOM + 1)), gs)
            dat["gslope"] = sl
            dat["gresid"] = float(np.sqrt(np.mean(
                (np.asarray(gs) - (a0 + sl * np.arange(KMOM + 1)))
                ** 2)))
        else:
            dat["gslope"] = float("nan")
            dat["gresid"] = float("nan")
        row["dat"] = dat
        row["exact"] = (pivf, momv, c_cert)
        row["closes_schur"] = best < SCHUR_BAR
        row["closes_env"] = best <= T_R
    check("C1 exact-rational LDL floor certified on %d/%d cells "
          "(%d REFUSED)" % (len(rows) - n_ref, len(rows), n_ref),
          n_ref == 0, kill="K2")
    check("C2 floor quality: the certified floor never exceeds the "
          "float truth (%d exceed) and sits within rel %.2e <= %.0e"
          % (n_exceed, d_gapc, CERT_GAP_RTOL),
          n_exceed == 0 and d_gapc <= CERT_GAP_RTOL, kill="K2")
    check("C3 exact Chebyshev monic coefficients == float Lanczos at "
          "K = %d: max rel %.2e <= %.0e" % (KDEEP, d_coef, COEF_TIE),
          d_coef <= COEF_TIE, kill="K2")
    check("C4 exact-rational Radau value == float route at EVERY "
          "consumed depth: max rel %.2e <= %.0e (%d degenerate)"
          % (d_xr, XR_TIE, n_deg), d_xr <= XR_TIE and n_deg == 0,
          kill="K2")
    check("C5 RB1 BOUND PROPERTY WARD: the EXACT Radau value is an "
          "upper bound for the truth q at EVERY consumed depth on "
          "every cell: %d violations (0 required)" % sign_fail,
          sign_fail == 0, kill="K2")
    check("C6 node ward at the certified floor, every consumed "
          "depth: %d rules with a node below the floor" % node_fail,
          node_fail == 0, kill="K2")
    check("C7 interval cross-tier (E5, refuse-only) at the certified "
          "floor: %d confirmed, %d REFUSED-WIDTH, 0 denials possible"
          % (iv_conf, iv_ref), True)
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    n_schur = sum(1 for r in ok_rows if r["closes_schur"])
    n_env = sum(1 for r in ok_rows if r["closes_env"])
    m1 = [1.0 - r["bound_f"] for r in ok_rows]
    me = [T_R_F - r["bound_f"] for r in ok_rows]
    check("C8 CLOSING CENSUS on the deep blocks: certified bound < 1 "
          "on %d/%d steps (worst margin %.4f); bound <= t_R %.4f on "
          "%d/%d (worst margin %.4f)"
          % (n_schur, len(ok_rows), min(m1) if m1 else float("nan"),
             T_R_F, n_env, len(ok_rows),
             min(me) if me else float("nan")), True)
    return ok_rows


def scale_invariance_ward(rows):
    """G3: sigma, rho_4, rho_5 are invariant under Mt -> lambda Mt."""
    d_max = 0.0
    n_used = 0
    for row in rows[:12]:
        mat = row["step"]["Mt"]
        base = None
        for lam in SCALE_SET:
            scl = mat * lam
            c_s = float(np.linalg.eigvalsh(np.asarray(scl)[1:, 1:])[0])
            jf = jacobi_form(scl)
            if jf is None:
                continue
            a, b = jf
            sig = sigma_quotient(np.concatenate([b, a]))
            r4, _ = rho_source(scl, c_s, KBASE)
            r5, _ = rho_source(scl, c_s, KDEEP)
            vec = np.asarray([sig, r4, r5], float)
            if base is None:
                base = vec
                n_used += 1
            else:
                d_max = max(d_max, float(np.max(
                    np.abs(vec - base) / np.maximum(1.0, np.abs(base))
                )))
    check("G3 SCALE-INVARIANCE ward: sigma, rho_4, rho_5 invariant "
          "under Mt -> lambda Mt for lambda in %s on %d cells: max "
          "rel %.2e <= %.0e"
          % (str(SCALE_SET), n_used, d_max, SCALE_TIE),
          d_max <= SCALE_TIE, kill="K2")


# ================================== CV: the convergence census
def convergence_census(rows):
    section("CV -- THE CONVERGENCE CENSUS (CONV RULE frozen in the "
            "spec: CONVERGENT-MEASURED iff |s| + 2SE <= %.2f AND "
            "Cauchy <= %.2f)" % (CONV_FLAT, CAUCHY_BAR))
    bidx = sorted({r["block"] for r in rows})
    out = {}
    print("    datum      FIT-CELL slope +- 2SE (R2)      block levels"
          " (median per block)                  Cauchy  verdict")
    for key in DATA_KEYS:
        xs = []
        ys = []
        for r in rows:
            val = r["dat"].get(key)
            if val is None or not math.isfinite(val):
                continue
            xs.append(math.log(r["h"]))
            ys.append(val)
        if len(xs) < 4:
            out[key] = dict(verdict="NOISY", note="too few points")
            continue
        s_c, e_c, r2_c, _a = linfit(xs, ys)
        levels = []
        hbar = []
        env_lo = []
        env_hi = []
        for bi in bidx:
            sub = [r["dat"][key] for r in rows if r["block"] == bi
                   and math.isfinite(r["dat"].get(key, float("nan")))]
            if not sub:
                continue
            levels.append(float(np.median(sub)))
            env_lo.append(float(np.min(sub)))
            env_hi.append(float(np.max(sub)))
            hbar.append(math.log(float(np.median(
                [r["h"] for r in rows if r["block"] == bi]))))
        cauchy = 0.0
        for i in range(len(levels) - 1):
            cauchy = max(cauchy, abs(levels[i + 1] - levels[i])
                         / max(1.0, abs(levels[i])))
        s_b, e_b, r2_b, _ab = (linfit(hbar, levels)
                               if len(levels) >= 3
                               else (0.0, float("inf"),
                                     float("nan"), 0.0))
        s_e, e_e, r2_e, a_e = (linfit(hbar, env_hi)
                               if len(env_hi) >= 3
                               else (0.0, float("inf"),
                                     float("nan"), 0.0))
        if abs(s_c) + e_c <= CONV_FLAT and cauchy <= CAUCHY_BAR:
            verd = "CONVERGENT-MEASURED"
        elif abs(s_c) - e_c > 0.0 and abs(s_c) > CONV_FLAT:
            verd = "DRIFTING"
        else:
            verd = "NOISY"
        out[key] = dict(verdict=verd, s_cell=s_c, e_cell=e_c,
                        r2_cell=r2_c, s_block=s_b, e_block=e_b,
                        r2_block=r2_b, s_env=s_e, e_env=e_e,
                        r2_env=r2_e, a_env=a_e, levels=levels,
                        env_lo=env_lo, env_hi=env_hi,
                        hbar=hbar, cauchy=cauchy,
                        limit=levels[-1] if levels else float("nan"),
                        env_lo_lim=env_lo[-1] if env_lo else
                        float("nan"),
                        env_hi_lim=env_hi[-1] if env_hi else
                        float("nan"))
        print("    %-10s %+8.4f +- %7.4f (%.3f)   %s   %6.3f  %s"
              % (key, s_c, e_c, r2_c,
                 " ".join("%9.4f" % v for v in levels), cauchy, verd))
    n_conv = sum(1 for v in out.values()
                 if v["verdict"] == "CONVERGENT-MEASURED")
    n_drift = sum(1 for v in out.values()
                  if v["verdict"] == "DRIFTING")
    n_noisy = sum(1 for v in out.values() if v["verdict"] == "NOISY")
    check("CV1 convergence census over the %d entry data: %d "
          "CONVERGENT-MEASURED, %d DRIFTING, %d NOISY"
          % (len(DATA_KEYS), n_conv, n_drift, n_noisy), True)
    # the DECISIVE datum: the rho_5 block ENVELOPE (the sup end)
    dec = out.get("rho5", {})
    if dec.get("env_hi"):
        s_e, e_e = dec["s_env"], dec["e_env"]
        env_last = dec["env_hi"][-1]
        rising = (s_e - e_e > 0.0)
        h_cross = float("inf")
        if rising and s_e > 0.0:
            h_cross = math.exp((T_R_F - dec["a_env"]) / s_e)
        print("    DECISIVE datum rho_5 block ENVELOPE: %s"
              % " ".join("%.4f" % v for v in dec["env_hi"]))
        print("      envelope slope %+.4f +- %.4f (R2 %.3f); last "
              "envelope %.6f; t_R %.4f; margin %+.6f; extrapolated "
              "crossing h %s"
              % (s_e, e_e, dec["r2_env"], env_last, T_R_F,
                 T_R_F - env_last,
                 "%.3g" % h_cross if math.isfinite(h_cross)
                 else "none (not rising)"))
        check("CV2 the DECISIVE datum (rho_5 block envelope) is NOT "
              "rising: slope %+.4f - 2SE %.4f <= 0 and the last "
              "envelope %.6f < t_R %.4f (margin %+.6f)"
              % (s_e, e_e, env_last, T_R_F, T_R_F - env_last),
              (not rising) and env_last < T_R_F)
    return out


# ================================ LIM: the limit object
def limit_object(cens, rows):
    section("LIM -- THE LIMIT OBJECT: the level vector, the "
            "moment-shape collapse, the MEDOID limit member and its "
            "class membership")
    need = ["rho4", "rho5", "sigma", "r_floor", "gslope", "gresid"] \
        + ["g%d" % k for k in range(KMOM + 1)]
    have = all(k in cens and cens[k].get("levels") for k in need)
    check("LIM0 every entry datum has a measured block level (the "
          "limit object is only defined if it does)", have, kill="K1")
    if not have:
        return None
    lim = {k: cens[k]["limit"] for k in DATA_KEYS if k in cens}
    print("    (i) THE LEVEL VECTOR (per-datum median of the deepest "
          "block; n normalized to 1):")
    print("      r_floor(c/n) = %.6f;  sigma = %.6f;  rho_4 = "
          "%.6f;  rho_5 = %.6f"
          % (lim["r_floor"], lim["sigma"], lim["rho4"], lim["rho5"]))
    for k in range(KMOM + 1):
        print("      g%d = log10(nu_%d / n^%d) = %+9.4f"
              % (k, k, k + 2, lim["g%d" % k]))
    # ---- the MOMENT-SHAPE COLLAPSE diagnostic (a measurement)
    gv = [lim["g%d" % k] for k in range(KMOM + 1)]
    sl, se, r2, a0 = linfit(list(range(KMOM + 1)), gv)
    resid = float(np.sqrt(np.mean(
        (np.asarray(gv) - (a0 + sl * np.arange(KMOM + 1))) ** 2)))
    lvlv = [Fraction(10.0 ** g) for g in gv]
    ok_l4, idx4 = hankel_pd(lvlv, KBASE)
    ok_l5, idx5 = hankel_pd(lvlv, KDEEP)
    print("    (ii) THE MOMENT-SHAPE COLLAPSE (a MEASUREMENT, not a "
          "gate): g_k is linear in k with slope %+.5f +- %.5f "
          "(R2 %.6f), residual RMS %.2e -- i.e. nu_{k+1}/(nu_k n) is "
          "CONSTANT to that accuracy, so the deep moment sequence is "
          "a ONE-ATOM (rank-1 Hankel) shape.  CONSEQUENCE: the "
          "per-datum LEVEL vector is NOT a valid moment sequence "
          "(E7 Hankel PD at K = %d / %d: %s / %s, failing minor "
          "%d / %d) -- the moment box is NOT a product box, the "
          "moments are rigidly linked, and a BOX-CORNER envelope over "
          "them is VACUOUS."
          % (sl, se, r2, resid, KBASE, KDEEP,
             "PD" if ok_l4 else "not PD",
             "PD" if ok_l5 else "not PD", idx4, idx5))
    check("LIM1 the moment-shape collapse is measured and reported: "
          "g_k linear in k to R2 %.6f with residual RMS %.2e; the "
          "level vector's Hankel status is stated (%s / %s) and NOT "
          "used as the limit object"
          % (r2, resid, "PD" if ok_l4 else "singular",
             "PD" if ok_l5 else "singular"), r2 > 0.99)
    # ---- the MEDOID: an ACTUAL family member closest to the level
    deep_b = max(r["block"] for r in rows)
    pool = [r for r in rows if r["block"] == deep_b
            and r.get("exact") is not None]
    med = {k: cens[k]["limit"] for k in MEDOID_KEYS}

    def dist(row):
        return max(abs(row["dat"][k] - med[k]) / max(1.0, abs(med[k]))
                   for k in MEDOID_KEYS)

    medoid = min(pool, key=dist) if pool else None
    check("LIM2a the deepest block supplies a MEDOID member (declared "
          "rule: the cell of the deepest block minimizing the max "
          "relative deviation from the level vector over %s)"
          % ",".join(MEDOID_KEYS), medoid is not None, kill="K1")
    if medoid is None:
        return None
    pivf, momv, c_cert = medoid["exact"]
    momn = [momv[k] / pivf ** (k + 2) for k in range(len(momv))]
    flon = c_cert / pivf
    print("    (iii) THE MEDOID LIMIT MEMBER: block %d %s kz %d "
          "h %d, distance %.4f from the level vector; its EXACT "
          "normalized entry vector (n = 1) is the limit object."
          % (medoid["block"], medoid["mode"], medoid["kz"],
             int(medoid["h"]), dist(medoid)))
    ok_h4, i4 = hankel_pd(momn, KBASE)
    ok_h5, i5 = hankel_pd(momn, KDEEP)
    check("LIM2b the MEDOID's exact normalized moment vector IS a "
          "valid moment sequence (E7 Hankel PD at K = %d and K = %d; "
          "failing minor %d / %d) -- it is an actual member of the "
          "family, so this is a structural fact, not a fit"
          % (KBASE, KDEEP, i4, i5), ok_h4 and ok_h5, kill="K2")
    rec = {}
    d_coh = 0.0
    for kd in (KBASE, KDEEP):
        cheb = chebyshev_monic(momn, kd)
        val = (radau_exact(cheb[0], cheb[1], flon, momn[0])
               if cheb is not None else None)
        rec[kd] = float(val) if val is not None else float("nan")
        own = medoid["vals"].get(kd, float("nan"))
        if math.isfinite(rec[kd]) and math.isfinite(own):
            d_coh = max(d_coh, abs(rec[kd] - own) / max(1e-12, own))
        else:
            d_coh = float("inf")
        print("      RADAU_%d on the EXACT normalized medoid vector: "
              "%.9f   (the medoid's own certified rho_%d: %.9f)"
              % (kd, rec[kd], kd, own))
    check("LIM2c COHERENCE ward (EXACT): the Radau functional on the "
          "scale-quotiented exact moment vector reproduces the "
          "medoid's own certified rho_K -- max rel %.2e <= %.0e "
          "(this is the scale-invariance of RAD, verified in exact "
          "rational arithmetic)" % (d_coh, XR_TIE), d_coh <= XR_TIE,
          kill="K2")
    # ---- class membership: RAD at the medoid, at the level, at the
    #      MEASURED envelope
    lvl_ok = {}
    for kd, key in ((KBASE, "rho4"), (KDEEP, "rho5")):
        lvl = lim[key]
        lvl_ok[kd] = math.isfinite(lvl) and lvl <= T_R_F
        print("      RAD at the LIMIT LEVEL, K = %d: rho = %.6f <= "
              "t_R = %.4f ?  %s  (margin %+.6f)"
              % (kd, lvl, T_R_F, "YES" if lvl_ok[kd] else "NO",
                 T_R_F - lvl))
    med_ok = all(math.isfinite(rec[kd]) and rec[kd] <= T_R_F
                 for kd in (KBASE, KDEEP))
    check("LIM3a RAD holds at the MEDOID limit member (exact, both "
          "depths) and at the LIMIT LEVEL (both depths)",
          med_ok and all(lvl_ok.values()))
    env_hi_rho = cens["rho5"]["env_hi_lim"]
    env_lo_flo = cens["r_floor"]["env_lo_lim"]
    check("LIM3 the limit ENVELOPE satisfies RAD: the MEASURED "
          "deepest-block rho_5 envelope %.6f <= t_R %.4f (margin "
          "%+.6f).  The box-corner reading is deliberately NOT used: "
          "LIM1 measured the moment box to be non-product, so a "
          "corner is not a moment sequence at all."
          % (env_hi_rho, T_R_F, T_R_F - env_hi_rho),
          env_hi_rho <= T_R_F)
    # ---- CCLXXXI definiteness closed form
    lam_lim = lambda_closed(1.0, float(flon), rec[KDEEP])
    lam_env = lambda_closed(1.0, env_lo_flo, env_hi_rho)
    print("      CCLXXXI closed form (n = 1): Lambda = %.6e at the "
          "MEDOID limit member, %.6e at the measured envelope worst "
          "(min floor %.6f with max rho_5 %.6f)"
          % (lam_lim, lam_env, env_lo_flo, env_hi_rho))
    check("LIM4 the CCLXXXI closed form is POSITIVE at the medoid "
          "limit member and at the measured envelope worst: Lambda = "
          "%.6e / %.6e > 0 => M positive definite at the limit"
          % (lam_lim, lam_env), lam_lim > 0.0 and lam_env > 0.0)
    return dict(lim=lim, rec=rec, lam_lim=lam_lim, lam_env=lam_env,
                medoid=medoid, gslope=sl, gr2=r2, gresid=resid,
                env_hi_rho=env_hi_rho)


def composed_architecture(cens, rows, limobj):
    section("ARCH -- THE COMPOSED ALL-LARGE-h ARCHITECTURE, every "
            "piece typed (this is the deliverable statement)")
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    worst = max((r["bound_f"] for r in ok_rows), default=float("nan"))
    hs = [r["h"] for r in ok_rows]
    dec = cens.get("rho5", {})
    s_e = dec.get("s_env", float("nan"))
    e_e = dec.get("e_env", float("nan"))
    cau = dec.get("cauchy", float("nan"))
    env_last = dec.get("env_hi_lim", float("nan"))
    n_tr = sum(1 for r in ok_rows if r["bound_f"] <= T_R_F)
    closes = worst <= T_R_F
    print("""    (1) [CERT-FINITE]  Every built wall-legal cell in the
        %d blocks (%d steps, h %d .. %d) carries an EXACT-RATIONAL
        certified bound rho <= %.6f (worst) < 1; with P1 (n > 0,
        warded exactly) and P2 (the certified co-block floor) the
        Schur criterion gives M POSITIVE DEFINITE on every one of
        them, with worst margin %+.6f against the DEFINITENESS bar 1.
        Against the CCLXXXI registered CLASS bar t_R = %.4f the same
        census reads %d/%d, worst margin %+.6f -- i.e. the class bar
        is %s.  Both are FINITE statements about BUILT objects and
        both are CERTIFIED exact-rationally.
    (2) [MEASURED]  The class-decisive datum rho_5 has block
        envelope %s with fitted slope %+.4f +- %.4f per log h and
        relative Cauchy width %.3f between consecutive blocks; the
        deepest block's envelope is %.6f, i.e. %+.6f against t_R and
        %+.6f against the definiteness bar 1.
        This is a MEASUREMENT on %d cells, not a theorem.
    (3) [CONJECTURE-GRADE ENVELOPE]  The composition needs a bar B and
        a proved rate.  Given a source-side bound
        |rho_5(h) - rho_5^inf| <= D(h) with D decreasing, RAD at bar B
        would hold for every h with D(h) < B - %.6f.  Against
        B = 1 (definiteness) that budget is %+.6f and the composition
        is AVAILABLE the moment a rate is proved; against
        B = t_R = %.4f the budget is %+.6f, so with THIS measurement
        the composition DOES NOT CLOSE at the registered class bar --
        no rate, however good, can repair a breached envelope.  The
        rate is MEASURED in either case, so (3) stays a CONJECTURE.
    (4) [OPEN PREMISE, unquantified]  The wall-legal deep family must
        be COFINAL in h.  Legality (core_ok, negA = 0, lamS > 0,
        tau > 0) is MEASURED cell by cell; this run's census records
        every failure.  Nothing here proves that arbitrarily deep
        census cells are wall-legal, and a legality failure at depth
        does not merely weaken the statement -- it removes the cells
        from the question entirely.
    WHAT A PROOF OF THE RATE WOULD NEED (source-side, honest):
      (i)  the ARCHIMEDEAN carrier: a deterministic function of
           (M, D) alone, prime-blind by construction -- its limit is
           a closed-form question about the Weil kernel's lag arm and
           is the tractable half (measured in section M below);
      (ii) the PRIME carrier: a uniform bound on the comb read's
           fluctuation over the window, i.e. exactly the error-term
           problem the hardness decision already names.  The measured
           stationarity says that fluctuation does NOT grow in the
           normalized data -- that is the honest content, and it is
           the whole difficulty compressed into one sentence.
      (iii) the LEGALITY premise (4), which is a separate question
           about tau's sign at depth and is not a rate question at
           all."""
          % (len({r["block"] for r in ok_rows}), len(ok_rows),
             int(min(hs)) if hs else 0, int(max(hs)) if hs else 0,
             worst, 1.0 - worst, T_R_F, n_tr, len(ok_rows),
             T_R_F - worst, "HELD" if closes else "BREACHED",
             " ".join("%.4f" % v for v in dec.get("env_hi", [])),
             s_e, e_e, cau, env_last, T_R_F - env_last,
             1.0 - env_last, len(ok_rows),
             env_last, 1.0 - env_last, T_R_F, T_R_F - env_last))
    if limobj:
        print("    the LIMIT OBJECT feeding (2)/(3): the MEDOID "
              "member of the deepest block (h %d, kz %d), whose exact "
              "normalized data give rho_5 = %.6f and CCLXXXI Lambda = "
              "%.6e; the measured envelope worst gives Lambda = %.6e."
              "  The moment shape is one-atom to R2 %.6f (LIM1), so "
              "the limit is a ONE-PARAMETER family, not a box."
              % (int(limobj["medoid"]["h"]), limobj["medoid"]["kz"],
                 limobj["rec"][KDEEP], limobj["lam_lim"],
                 limobj["lam_env"], limobj["gr2"]))
    check("ARCH1 the composed architecture is stated with all four "
          "pieces typed (CERT-FINITE / MEASURED / CONJECTURE-GRADE / "
          "OPEN PREMISE) and no piece silently upgraded", True)
    return dict(worst=worst, env_last=env_last)


# ================================ M: the mechanism decomposition
def mechanism(census, anchors):
    section("M -- THE MECHANISM: the exact CCIII three-way split "
            "S = S_AR + S_SM + S_OSC pushed through the SAME step "
            "frame, so Mt = Mt_AR + Mt_SM + Mt_OSC exactly")
    tgts = (600,) if SMOKE else MECH_TGT
    mech_n = 1 if SMOKE else MECH_N
    d_add = 0.0
    n_cells = 0
    print("    depth  h      kz    part   n share    nu0 share   "
          "sigma(partial sums)        rho5(partial sums)")
    laws = {"AR": [], "SM": [], "OSC": []}
    hs_law = []
    anc = sorted(anchors, key=lambda r: r["h"])
    for tgt in tgts:
        picked = block_pick(census, tgt, mech_n)
        prev = None
        for cell in picked:
            rung = build_cell(cell, with_split=True)
            ok, why = cell_legal(rung)
            if not ok or "S_parts" not in rung:
                print("      mech cell h %d kz %d SKIPPED (%s)"
                      % (cell["h"], cell["kz"], why))
                prev = rung if ok else prev
                continue
            below = [a for a in anc if a["h"] <= rung["h"]]
            r1 = prev if prev is not None else (
                below[-1] if below else anc[0])
            sts = ob.make_steps([r1, rung])
            prev = rung
            if not sts:
                continue
            st = sts[0]
            zol.assemble_step(st)
            if st["status"] != "OK":
                continue
            tau1 = float(st["tau"])
            qmat = st["Q"]
            full = st["Mt"]
            mparts = {p: sym(qmat.T @ (rung["S_parts"][p] / tau1)
                             @ qmat)
                      for p in ("AR", "SM", "OSC")}
            recon = mparts["AR"] + mparts["SM"] + mparts["OSC"]
            d_add = max(d_add, float(np.max(np.abs(recon - full)))
                        / max(1.0, float(np.max(np.abs(full)))))
            n_cells += 1
            n_full = float(full[0, 0])
            nu0_full = float(np.asarray(full)[1:, 0]
                             @ np.asarray(full)[1:, 0])
            hs_law.append(math.log(float(rung["h"])))
            for p in ("AR", "SM", "OSC"):
                pm = mparts[p]
                share_n = float(pm[0, 0]) / n_full
                vec = np.asarray(pm)[1:, 0]
                share_nu = float(vec @ vec) / nu0_full
                laws[p].append(abs(share_n))
                # partial sums: AR, AR+SM, full
                acc = {"AR": mparts["AR"],
                       "SM": mparts["AR"] + mparts["SM"],
                       "OSC": full}
                pmat = acc[p]
                jf = jacobi_form(pmat)
                sig_p = (sigma_quotient(np.concatenate(jf))
                         if jf is not None else float("nan"))
                try:
                    c_p = float(np.linalg.eigvalsh(
                        np.asarray(pmat)[1:, 1:])[0])
                except np.linalg.LinAlgError:
                    c_p = float("nan")
                rho_p = (rho_source(pmat, c_p, KDEEP)[0]
                         if math.isfinite(c_p) and c_p > 0.0
                         else float("nan"))
                print("    %-6d %-6d %-5d %-6s %+10.4f %+11.4f   "
                      "%-24s   %-10s"
                      % (tgt, rung["h"], rung["kz"], p, share_n,
                         share_nu,
                         ("cum(%s) %+.6f" % (p, sig_p)),
                         ("%.6f" % rho_p) if math.isfinite(rho_p)
                         else "REFUSED(c<=0)"), flush=True)
    check("M1 the three-way split is EXACTLY additive through the "
          "step frame on %d mechanism cells: max rel |Mt - (Mt_AR + "
          "Mt_SM + Mt_OSC)| = %.2e <= 1e-10" % (n_cells, d_add),
          n_cells >= 1 and d_add <= 1e-10, kill="K2")
    for p in ("AR", "SM", "OSC"):
        if len(hs_law) >= 3:
            s, e, r2, _a = linfit(hs_law, np.log(np.maximum(
                laws[p], 1e-300)))
            print("      carrier %-3s |pivot share| law: d log share / "
                  "d log h = %+.4f +- %.4f (R2 %.3f), shares %s"
                  % (p, s, e, r2,
                     " ".join("%.4f" % v for v in laws[p])))
        else:
            print("      carrier %-3s shares %s (too few cells for a "
                  "law)" % (p, " ".join("%.4f" % v for v in laws[p])))
    check("M2 the mechanism decomposition is reported per carrier "
          "(archimedean / smooth surrogate / prime oscillation) with "
          "its h-law", len(hs_law) >= 1)
    return laws


# ==================================== X: controls-must-fire
def controls(census, anchors, rows):
    section("X -- CONTROLS-MUST-FIRE")
    tgt = (600,) if SMOKE else (MECH_TGT[0],)
    cell = block_pick(census, tgt[0], 1)[0]
    anc = sorted(anchors, key=lambda r: r["h"])
    below = [a for a in anc if a["h"] <= cell["h"]]
    r1 = below[-1] if below else anc[0]
    print("    control cell: h %d kz %d alpha %.4f X %.4g; anchor "
          "%s kz %d h %d" % (cell["h"], cell["kz"], cell["alpha"],
                             cell["X"], r1["kind"], r1["kz"],
                             r1["h"]))

    def world_read(world, seed=None):
        """The world's cell: legality first (the primary control),
        then the DECLARED DIAGNOSTIC (amendment A6) -- the refused
        step's entry data normalized by |tau_1|."""
        rung = build_cell(cell, world=world, scr_seed=seed)
        ok, why = cell_legal(rung)
        out = dict(world=world, legal=ok, why=why,
                   tau=rung.get("tau", float("nan")))
        if "S" not in rung:
            return out
        sts = ob.make_steps([r1, rung])
        if not sts:
            return out
        st = sts[0]
        mat = sym(st["Q"].T @ (rung["S"] / abs(float(st["tau"])))
                  @ st["Q"])
        piv = float(mat[0, 0])
        try:
            c_w = float(np.linalg.eigvalsh(np.asarray(mat)[1:, 1:])[0])
        except np.linalg.LinAlgError:
            return out
        jf = jacobi_form(mat)
        out["piv"] = piv
        out["c"] = c_w
        out["sigma"] = (sigma_quotient(np.concatenate(jf))
                        if jf is not None else float("nan"))
        out["rho5"] = (rho_source(mat, c_w, KDEEP)[0]
                       if c_w > 0.0 and piv > 0.0 else float("nan"))
        mom = wall_moments(mat, KMOM)
        out["g"] = [math.log10(abs(mom[k] / piv ** (k + 2)))
                    if (mom[k] > 0.0 and piv > 0.0) else float("nan")
                    for k in range(KMOM + 1)]
        return out

    scr = world_read("scramble", seed=SCR_SEED)
    smo = world_read("smooth")
    arc = world_read("arch")
    for w in (scr, smo, arc):
        print("      world %-9s legal %-5s (%s) tau %-11s sigma %-11s "
              "rho5 %-11s g0 %s"
              % (w["world"], w["legal"], w["why"],
                 "%.3e" % w["tau"] if math.isfinite(w["tau"]) else "-",
                 "%.6f" % w["sigma"] if math.isfinite(
                     w.get("sigma", float("nan"))) else "-",
                 "%.6f" % w["rho5"] if math.isfinite(
                     w.get("rho5", float("nan"))) else "-",
                 "%.4f" % w["g"][0] if w.get("g") else "-"))
    # the measured deep envelope the worlds are compared against
    sig_hi = max(r["dat"]["sigma"] for r in rows)
    rho_hi = max(r["dat"]["rho5"] for r in rows)
    g0_lo = min(r["dat"]["g0"] for r in rows)
    g0_hi = max(r["dat"]["g0"] for r in rows)
    print("      the measured deep envelope: sigma <= %.6f, rho_5 <= "
          "%.6f, g0 in [%.4f, %.4f]" % (sig_hi, rho_hi, g0_lo, g0_hi))

    def outside(w):
        if not math.isfinite(w.get("sigma", float("nan"))):
            return True, "sigma non-finite"
        if w["sigma"] > sig_hi or w["sigma"] <= 0.0:
            return True, "sigma %.4f outside" % w["sigma"]
        if math.isfinite(w.get("rho5", float("nan"))) \
                and w["rho5"] > rho_hi:
            return True, "rho_5 %.4f outside" % w["rho5"]
        if w.get("g") and math.isfinite(w["g"][0]) \
                and not (g0_lo <= w["g"][0] <= g0_hi):
            return True, ("moment shape g0 %.4f outside [%.4f, %.4f] "
                          "(%.1f log decades)"
                          % (w["g"][0], g0_lo, g0_hi,
                             min(abs(w["g"][0] - g0_lo),
                                 abs(w["g"][0] - g0_hi))))
        return False, "inside the deep envelope"

    scr_out, scr_why = outside(scr)
    smo_out, smo_why = outside(smo)
    check("X1 the SCRAMBLE world (seed %d) fires: legality %s / %s"
          % (SCR_SEED, "LEFT" if not scr["legal"] else "kept",
             scr_why), (not scr["legal"]) or scr_out, kill="K4")
    check("X2 the SMOOTH (prime-free) world fires -- THE "
          "DISCRIMINATION: legality %s / %s"
          % ("LEFT" if not smo["legal"] else "kept", smo_why),
          (not smo["legal"]) or smo_out, kill="K4")
    # X3: a synthetic near-1 cell must NOT certify
    base = rows[0]["step"]["Mt"].copy()
    piv0 = float(base[0, 0])
    vec0 = np.asarray(base)[1:, 0]
    blk0 = np.asarray(base)[1:, 1:]
    q0 = float(vec0 @ np.linalg.solve(blk0, vec0))
    scale = math.sqrt(CTRL_SIG_NEAR * piv0 / q0)
    ctrl = base.copy()
    ctrl[1:, 0] = vec0 * scale
    ctrl[0, 1:] = vec0 * scale
    sig_c = (float(np.asarray(ctrl)[1:, 0]
                   @ np.linalg.solve(blk0, np.asarray(ctrl)[1:, 0]))
             / piv0)
    c_c = float(np.linalg.eigvalsh(blk0)[0])
    _pv, momc, blkc = exact_wall_data(ctrl, 2 * KDEEP - 2)
    cc = cert_floor_exact(blkc, Fraction(0),
                          Fraction(float(c_c)) * (Fraction(1)
                                                  + Fraction(1,
                                                             10 ** 6)))
    bnd_c = float("nan")
    if cc is not None:
        cheb = chebyshev_monic(momc, KDEEP)
        if cheb is not None:
            vv = radau_exact(cheb[0], cheb[1], cc, momc[0])
            if vv is not None:
                bnd_c = float(vv / Fraction(float(ctrl[0, 0])))
    check("X3 the synthetic NEAR-1 control (coupling scaled to truth "
          "sigma %.4f > 1) must NOT certify bound < 1: certified "
          "K = %d bound %.6f" % (sig_c, KDEEP, bnd_c),
          math.isfinite(bnd_c) and bnd_c >= 1.0, kill="K4")
    # X4: an inflated floor claim must be refused by BOTH tiers
    n_ref_x = n_try = 0
    for row in rows[:3]:
        n_try += 1
        bad = Fraction(float(row["c_meas"])) * Fraction(
            int(CTRL_INFLATE * 100), 100)
        okx, _ = pd_exact(exact_wall_data(row["step"]["Mt"],
                                          2)[2], bad)
        oki = chol_iv(np.asarray(row["step"]["Bblk"], float),
                      float(bad))
        if (not okx) and (oki is None):
            n_ref_x += 1
    check("X4 an INFLATED floor claim (x %.2f) is refused by BOTH "
          "tiers on %d/%d cells" % (CTRL_INFLATE, n_ref_x, n_try),
          n_ref_x == n_try, kill="K4")
    return dict(scr=scr, smo=smo, arc=arc)


# ==================================== S: the screens
def screens(rows):
    section("S -- tau and CCXVII c_h relocation screens (CCXLVII "
            "bars verbatim: PASS <= %.2f, RELOC >= %.2f) on every "
            "fitted level" % (SLOPE_PASS, SLOPE_RELOC))
    taus = [r["tau_scale"] for r in rows]
    verds = []
    for key in ("sigma", "rho4", "rho5", "r_floor"):
        vals = [r["dat"][key] for r in rows]
        txt, vd = screen(vals, taus, "tau-screen %s" % key)
        print("    " + txt)
        verds.append(vd)
    for lab, vals in (("t_R - rho5",
                       [T_R_F - r["dat"]["rho5"] for r in rows]),
                      ("1 - bound",
                       [1.0 - r["bound_f"] for r in rows])):
        txt, vd = screen(vals, taus, "tau-screen %s" % lab)
        print("    " + txt)
        verds.append(vd)
    n_reloc = sum(1 for v in verds if v == "RELOC")
    check("S1 tau relocation screens on the fitted levels and "
          "margins: %d PASS, %d AMBIG, %d RELOC, %d vacuous"
          % (verds.count("PASS"), verds.count("AMBIG"), n_reloc,
             verds.count("VAC")), n_reloc == 0)
    # ---- the c_h screen: only where the deployed surface window is
    # legitimate (X <= ATOM_MAX and h <= CH_HMAX), rest OUT-OF-SURFACE
    ch_n = 2 if SMOKE else CH_N
    pool = [r for r in rows
            if r["X"] <= core.ATOM_MAX and r["h"] <= CH_HMAX]
    seen = set()
    picks = []
    for r in sorted(pool, key=lambda r: r["h"]):
        if r["kz"] in seen:
            continue
        seen.add(r["kz"])
        picks.append(r)
        if len(picks) >= ch_n:
            break
    n_out = len(rows) - len(pool)
    chs = []
    sigs = []
    for r in picks:
        try:
            rr = ob.window_of(r["kz"])
            c_at = np.asarray(core.atom_lags_at(
                rr["alpha"], rr["M"], rr["uu"], 2.0 * rr["lam"])[0],
                float)
            dens = eul.grid_density(rr["c_ar"] + c_at)
            pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                     rr["M"])
            neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                     rr["M"])
            last = pos.shape[0] - 1
            top = float(sla.eigh(neg, pos, eigvals_only=True,
                                 subset_by_index=[last, last])[0])
            chs.append(1.0 - top)
            sigs.append(r["dat"]["sigma"])
            print("    c_h cell kz %-4d h %-6d c_h %.4e sigma %.6f "
                  "[%.1f s]" % (r["kz"], r["h"], 1.0 - top,
                                r["dat"]["sigma"], time.time() - T0),
                  flush=True)
        except Exception as exc:                 # noqa: BLE001
            print("    c_h cell kz %d REFUSED (%s)" % (r["kz"], exc))
    if len(chs) >= 3:
        txt, vd = screen(sigs, chs, "c_h-screen sigma")
        print("    " + txt)
        check("S2 CCXVII c_h relocation screen on %d in-surface deep "
              "cells (%d cells typed OUT-OF-SURFACE): %s"
              % (len(chs), n_out, vd), vd != "RELOC")
    else:
        check("S2 CCXVII c_h relocation screen: VACUOUS (%d "
              "in-surface cells of %d; %d typed OUT-OF-SURFACE -- "
              "the deployed surface window is only defined for "
              "X <= %.0e)" % (len(chs), len(rows), n_out,
                              float(core.ATOM_MAX)), True)


# =============================================================== main
def print_table(rows):
    print("\n    THE DEEP ENTRY-DATA TABLE (all wall-legal block "
          "steps; NORM-D raw | NORM-P scale-quotient | certified):")
    print("    idx b mode    kz    h      n_raw       c_raw      "
          "c/n      sigma     rho4      rho5      K  bound_cert  "
          "m_1")
    for row in rows:
        d = row["dat"]
        print("    %3d %d %-7s %-5d %6d %11.4g %10.4g %8.4f %9.6f "
              "%9.6f %9.6f %2d %11.6f %9.6f"
              % (row["index"], row["block"], row["mode"], row["kz"],
                 int(row["h"]), row["n_piv"], row["c_meas"],
                 d["r_floor"], d["sigma"], d["rho4"], d["rho5"],
                 row.get("k_used", 0), row["bound_f"],
                 1.0 - row["bound_f"]))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 + exact-rational measurements on the
  deployed deep-frame construction, on CONTIGUOUS segments of the
  TAB2 = 1.6e7 census (amendment A2).  The class-membership question
  is SCALE-INVARIANT (P1, P2, RAD, sigma and rho_K are all invariant
  under Mt -> Mt/lambda) and is measured in the declared
  scale-quotient normalization NORM-P, with the raw deployed data
  NORM-D printed beside it.  Every limit statement is an
  EXTRAPOLATION of a MEASURED rate and is typed CONJECTURE-GRADE; the
  finite per-cell certificates are exact-rational and typed
  CERT-FINITE.  The cofinality of the wall-legal deep family is an
  OPEN PREMISE, measured cell by cell and never assumed.  No marker
  moves, no promotion, NO RH claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("deep_membership_limit_probe -- "
          "PRIME.ONEBADMODE.DEEP.MEMBERSHIP.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_c = ast_scan_functions(CERT_FUNCS, DERIV_BANNED)
    check("S0.2 AC certificate path (%s) sees ENTRIES and frozen "
          "constants only (%s)" % ("/".join(CERT_FUNCS),
                                   ",".join(sorted(set(bad_c)))
                                   or "clean"),
          not bad_c, kill="K1")
    bad_f = ast_scan_functions(FLOAT_FUNCS, DERIV_BANNED)
    check("S0.3 AC float bound path (%s) sees ENTRIES and frozen "
          "constants only (%s)" % ("/".join(FLOAT_FUNCS),
                                   ",".join(sorted(set(bad_f)))
                                   or "clean"),
          not bad_f, kill="K1")

    lad_steps, anchors = build_ladder()
    if KILLS:
        return finish([])
    build_tab2()
    census = deep_census()
    if KILLS:
        return finish([])

    lad_rows = [dict(step=st, block=-1, mode=ob.seg_of(st),
                     h=float(st["r2"]["h"]), kz=int(st["r2"]["kz"]),
                     alpha=float(st["r2"]["alpha"]),
                     X=math.exp(2.0 * float(st["r2"]["alpha"])),
                     tau_scale=float(st["tau"]),
                     schur=float(st["gap"]),
                     n_piv=float(st["n0"]),
                     c_meas=float(st["lamB1"]), index=i)
                for i, st in enumerate(lad_steps)]
    lad_rows = jacobi_identity_wards(lad_rows, "registered ladder")
    repro_anchors(lad_rows)
    f5_family(census, anchors)
    if KILLS:
        return finish([])

    blocks, legality = build_blocks(census)
    rows = block_steps(blocks, anchors)
    check("L2 the block step census admitted %d wall-legal steps "
          "(%d chain, %d bridge) over %d blocks"
          % (len(rows), sum(1 for r in rows if r["mode"] == "chain"),
             sum(1 for r in rows if r["mode"] == "bridge"),
             len({r["block"] for r in rows})),
          len(rows) >= (4 if SMOKE else 20), kill="K1")
    if KILLS:
        return finish([])
    rows = jacobi_identity_wards(rows, "deep block")
    rows = entry_data(rows)
    scale_invariance_ward(rows)
    if KILLS:
        return finish([])
    print_table(rows)

    # ---- the breach test comes FIRST (dominance order)
    breach = [r for r in rows
              if r["dat"]["rho5"] >= T_R_F or r["dat"]["sigma"] >= 1.0
              or r["bound_f"] >= 1.0]
    check("BR1 no built WALL-LEGAL deep cell breaches the class: %d "
          "breach cells (rho_5 >= t_R %.4f, or truth sigma >= 1, or "
          "certified bound >= 1)" % (len(breach), T_R_F),
          not breach)
    for r in breach:
        print("      BREACH cell: block %d %s kz %d h %d -- rho_5 "
              "%.6f, truth sigma %.6f, certified bound %.6f, n %.4g, "
              "c %.4g" % (r["block"], r["mode"], r["kz"], int(r["h"]),
                          r["dat"]["rho5"], r["dat"]["sigma"],
                          r["bound_f"], r["n_piv"], r["c_meas"]))

    cens = convergence_census(rows)
    limobj = limit_object(cens, rows)
    if KILLS:
        return finish([])
    arch = composed_architecture(cens, rows, limobj)
    mechanism(census, anchors)
    controls(census, anchors, rows)
    screens(rows)

    # ------------------------------------------------ verdict labels
    labels = []
    dec = cens.get("rho5", {})
    rising = (dec.get("s_env", 0.0) - dec.get("e_env", float("inf"))
              > 0.0)
    drift_keys = [k for k, v in cens.items()
                  if v["verdict"] != "CONVERGENT-MEASURED"]
    if breach:
        r = max(breach, key=lambda r: r["dat"]["rho5"])
        labels.append("DEEP-MEMBERSHIP-BREACH(block %d %s kz %d "
                      "h %d: rho_5 = %.6f, sigma = %.6f, bound = "
                      "%.6f)" % (r["block"], r["mode"], r["kz"],
                                 int(r["h"]), r["dat"]["rho5"],
                                 r["dat"]["sigma"], r["bound_f"]))
    elif rising:
        labels.append("DEEP-MEMBERSHIP-DRIFTS(rho_5 envelope slope "
                      "%+.4f +- %.4f per log h; last envelope %.6f "
                      "vs t_R %.4f)"
                      % (dec.get("s_env", float("nan")),
                         dec.get("e_env", float("nan")),
                         dec.get("env_hi_lim", float("nan")), T_R_F))
    elif drift_keys:
        labels.append("DEEP-MEMBERSHIP-LIMIT-PARTIAL(non-stationary "
                      "data: %s; decisive rho_5 envelope %.6f <= t_R "
                      "%.4f, margin %+.6f)"
                      % (", ".join("%s=%s" % (k, cens[k]["verdict"])
                                   for k in sorted(drift_keys)),
                         dec.get("env_hi_lim", float("nan")), T_R_F,
                         T_R_F - dec.get("env_hi_lim", float("nan"))))
    else:
        labels.append("DEEP-MEMBERSHIP-LIMIT-COMPOSED(rho_5 limit "
                      "level %.6f, envelope %.6f, |slope| <= %.4f, "
                      "margin to t_R %+.6f; Lambda(limit) = %.3e)"
                      % (dec.get("limit", float("nan")),
                         dec.get("env_hi_lim", float("nan")),
                         abs(dec.get("s_cell", float("nan")))
                         + dec.get("e_cell", float("nan")),
                         T_R_F - dec.get("env_hi_lim", float("nan")),
                         limobj["lam_lim"] if limobj else
                         float("nan")))
    bad_leg = [(h, kz, why) for _bi, h, kz, why in legality
               if why != "OK"]
    labels.append("LEGALITY(%d/%d census cells wall-legal in the "
                  "blocks%s)"
                  % (len(legality) - len(bad_leg), len(legality),
                     "; failures " + ", ".join("h %d kz %d %s" % t
                                               for t in bad_leg)
                     if bad_leg else ""))
    labels.append("CERT-FINITE(worst certified bound %.6f on %d "
                  "wall-legal deep steps)"
                  % (arch["worst"], len(rows)))
    return finish(labels)


if __name__ == "__main__":
    main()
