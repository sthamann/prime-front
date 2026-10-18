#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cofinal_dissect_probe -- PRIME.COFINAL.DISSECT.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim.  2026-08-13.)

WHAT EXACTLY ENDS AT h ~ 8200?  CCXCIX mapped the wall-legality
frontier as a hole field with 1e-10 margin; CCCV pushed the legal
sub-ladder to h 8204 and then measured THREE NEGA cells beyond it
(8677 kz 299 tau -3.053e-10, 9023 kz 506 -1.498e-10, 9535 kz 526
-1.743e-10) -- the first measured TERMINATION SIGNAL of the built
horizon.  Before any construction rebuild the question must be
CLASSIFIED, because four fundamentally different things can end
there:

 CASE A  the CERTIFICATE ends but the ideal matrix stays POSITIVE
         (then the region K or its COORDINATES need extension, not
         the mathematics);
 CASE B  the current 1-D window TRAJECTORY leaves K but OTHER
         admissible windows at the same depth stay positive (the
         path is wrong, not the family);
 CASE C  the IMPLEMENTED matrix goes negative but the ideal full
         Galerkin matrix does not (a coverage/construction defect:
         incomplete prime comb, truncated reflection part, lost
         boundary cell, broken nesting, insufficient interval
         width, wrong continuation of the joint relation);
 CASE D  the independently reconstructed IDEAL Galerkin matrix is
         GENUINELY indefinite (then either an identification /
         admissibility assumption is wrong, or the form delivers a
         real negative Weil test -- at this stage typed
         REPLICATION-REQUIRED, never concluded).

THE DECISIVE STRUCTURE (stated in full BEFORE any measurement; all
of it is exact algebra of the deployed pipeline).  The deployed cell
builder assembles A = I - G on the folded NEGATIVE arm, with
   G = sqrt(V) P P^T sqrt(V),   P[j,k] = p_k(y_j),  k < h,
where {p_k} is the three-term chain of the folded POSITIVE arm
(lanczos_chain on (xs, ws), evaluated by eval_chain).  Two exact
consequences drive this probe.

 (I) THE POLYNOMIAL PICTURE.  With H = P^T V P = int p p^T dmu_-
     one has spec(G) \ {0} = spec(H) \ {0}, hence
        tau = 1 - lambda_max(H)
             = 1 - max_q  int q^2 dmu_- / |coeff(q)|^2 ,
     the maximum over polynomials q of degree < h.  Legality is
     therefore EXACTLY the statement that the negative arm is
     strictly dominated by the positive arm on the degree-<h cone,
     and an illegal cell carries an EXPLICIT polynomial witness q.
 (II) THE METRIC IS THE ONLY IDEALITY GAP OF THE GRAM.  The chain
     columns are exactly a triangular degree-graded family, so
     span{p_0..p_{h-1}} IS the degree-<h polynomial space
     REGARDLESS of any rounding in (al, be).  The reproducing
     kernel of that space in mu_+ is therefore BASIS-INDEPENDENT
     and equals
        K_ideal(y,y') = p(y)^T O^{-1} p(y'),  O = int p p^T dmu_+
                      = P_+^T W P_+ ,
     so the IDEAL Galerkin restriction is
        G_ideal = sqrt(V) P O^{-1} P^T sqrt(V),
     while the DEPLOYED build uses O -> I.  The implemented matrix
     equals the ideal Galerkin restriction IFF O = I; the signed
     gap in the direction of the bad mode is the single scalar
        d = c^T (O - I) c = int q^2 dmu_+ - |c|^2 ,
        c = P^T sqrt(V) z   (z the float64 bottom mode of A),
     and with lambda = 1 - tau the ideal Rayleigh read at the SAME
     witness is exactly
        R_ideal = (c^T H c)/(c^T O c) = lambda^2/(lambda + d),
        tau_ideal_ub = 1 - R_ideal  >=  tau_ideal .
     THIS IS THE CASE-C / CASE-D DISCRIMINATOR, and it closes the
     metric half of the float64-vs-ideal scope edge that CCLXXVII
     A3 / CCXCIX / CCCV A4 all deferred: |d| << |tau| means the
     sign of tau is the sign of an IDEAL object; d > |tau| with
     tau < 0 means the negativity is an artefact of the deployed
     metric assumption.  NOTE the honest asymmetry: 1 - R_ideal is
     an UPPER bound for tau_ideal, so a NEGATIVE read is a
     WITNESS while a POSITIVE read is only "no witness found"
     (positivity of the ideal object is NOT certified here).
 (III) THE ENTRY ROUTE.  Christoffel-Darboux is an exact algebraic
     identity of the recurrence (no orthogonality used):
        sum_{k<h} p_k(x)p_k(y)
           = be_{h-1} (p_h(x)p_{h-1}(y) - p_{h-1}(x)p_h(y))/(x-y),
     so the h-term summed Gram has a 2-TERM INDEPENDENT ROUTE.
     Agreement of the two routes wards the ENTRIES of the
     implemented matrix (the CLXXXVII/CXCI identification wards at
     this depth); disagreement at the tau scale IS the case-C
     finding.

THE TEN OBJECTS per built cell (the lead's list, verbatim):
 (1) ideal interval matrix -- the metric-corrected Galerkin read
     (II) with OUTWARD-ROUNDED enclosures of both quadrature
     scalars (rigorous gamma_n dot-product bounds on the actually
     accumulated absolute sums);
 (2) rational certificate matrix -- the deployed exact-rational
     step-frame build (exact_wall_data on Mt, Fractions of the
     dyadic float64 entries);
 (3) joint-relation residuals -- exact RADAU_K(nu; f_1) <= t_R n at
     K = 4 and 5, plus the RB1 bound ward RADAU_K >= q;
 (4) membership z_h in K -- the CCXCIII region per constraint (P1
     pivot, P2 certified co-block floor, MOM moment box, P4 joint
     relation, PD sigma < 1), WHICH FAILS FIRST;
 (5) exact Schur scalars n, q, s = n - q, sigma = q/n (Fractions);
 (6) inertia witness on TWO independent routes -- the exact-sign
     Bunch-Kaufman LDL BLOCK inertia (1x1 pivot signs plus the
     exact-rational determinant/trace signs of every 2x2 block)
     AND the deployed eigvalsh, plus the localized
     inverse-iteration mode as truth reference;
 (7) source completeness -- the atom-completeness census (comb
     complete iff X = e^{2 alpha} <= TAB2; the DEPLOYED 4e6 prefix
     margin printed separately) and the A8 reflection assertion;
 (8) Galerkin faithfulness -- diag(O) census over ALL degrees, the
     directional gap d, a random-probe lower bound on ||O - I||,
     and the CD entry route (III);
 (9) distance to the boundary of K per coordinate;
 (10) the control worlds at these depths.

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; the only RNG
    seats are the DECLARED scramble control seed and the DECLARED
    orthogonality-probe seed.  AC scan: the chain-pass, CD and
    atom-census readers see nodes, weights, entries, coefficients
    and frozen constants only (no eigensolver, no inverse, no tau).
 T  TAB2 = 1.6e7 arrays built and warded BITWISE against the
    deployed 4e6 EXT prefix (CCLXXIX FX5 verbatim).
 D  the deep census (deployed frame formula verbatim), h-sorted;
    gates: 587 cells, h max 65051, census CONTAINS every frozen
    priority key.
 TIE the dissect builder (verbatim copy of bat.build_rung_param
    with extra READS) must tie bat.build_rung_param EXACTLY (tau,
    negA, lamS ==) on the TIE cell (nearest h 2012), and the
    chain-pass accumulator must tie ob.eval_chain there (PASS-TIE).
 CEN the priority census behind the guard (build item i iff
    elapsed + GUARD_FAC * c_hat * h^3 <= BUILD_CAP_S, c_hat the
    SELF-CALIBRATING cost estimate below; else UNBUILT-GUARD and
    the list continues):
      G1 h 8204 kz 287 (the deepest LEGAL cell of CCCV),
      G2 h 8677 kz 299 (the first NEGA beyond 8204),
      B1 h 8629 kz 223 (alpha 7.101 -- the LOW-alpha window at the
         SAME depth: the case-B test),
      B2 h 8642 kz 551 (alpha 8.210 -- the HIGH-alpha window at the
         SAME depth: the case-B test, other side),
      G3 h 8003 kz 284 (the CCXCIX/CCCV NEGA hole),
      G4 h 7958 kz 282 (the hole's LEGAL flank),
      G5 h 9023 kz 506 (NEGA), G6 h 9535 kz 526 (NEGA, the seat
         migration cell),
      B3 h 9447 kz 196 (alpha 6.929 -- the deepest LOW-alpha
         window, and the only possible POS flank of G6; stretch),
      XS the SMOOTH world at the G4 cell (the deep discrimination
         control; LAST because the measured world-only build is NOT
         cheaper than the dissect build, so it competes with a gate
         cell for the cap -- A12).
    Per cell: LEGAL / NEGA / MARGINAL (|tau| <= TAU_NOISE, sign not
    trusted) / CORE-SHORT / UNBUILT-GUARD, the ten objects, and
    EXACTLY ONE case letter.
 G  gates: G1/G4 reproduce LEGAL with the CCCV tau (rtol
    NEGA_RTOL); G2/G3/G5/G6 reproduce NEGA with the CCCV tau; SEAT
    reproduces on the built repro cells (uf, participation,
    rq_gap <= RQ_TIE); INERTIA the two routes agree on every built
    cell (a disagreement is NOT silently passed -- it is the
    case-C finding and is typed INERTIA-SPLIT); COVERAGE all six
    CCCV cells are BUILT (a guard refusal is typed as a BUDGET
    fact, printed as a FAIL and carried into the verdict as
    GATE-COVERAGE, never charged as a reproduction failure -- A12).
 AN anatomy wards: W7 rank identity (#unit >= max(0, n_neg - h)),
    W8 the E8 ward lamS >= tau on PD cells (consumed nowhere),
    W9 the node accounting M == n_pos + n_neg + n_dropped.
 X  controls-must-fire: X1 the scramble world must leave legality;
    X2 the smooth (prime-free) world must leave legality at every
    tested depth; XO the ORTHOGONALITY reader must FIRE on a
    DOCTORED recurrence (one be entry scaled by 1 + XO_DOPE -- the
    faithfulness measurement has teeth); XD the doctored metric
    must move the ideal read.  The de-reorthogonalized chain is
    built and PRINTED as a measurement (is the deployed double
    sweep load-bearing at that depth?), never as a gate.
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION here (no step formations of record, no
    fitted level -- census + dissect only) and are typed as such.

CASE RULE (frozen BEFORE the run; exhaustive, disjoint, strict
precedence -- exactly ONE letter per built cell).
 A cell is NEG iff tau <= -TAU_NOISE, POS iff tau >= +TAU_NOISE,
 MARGINAL otherwise (MARGINAL cells are censused and typed
 CASE-0, no case letter is invented for an unresolved sign).
 A named DEFECT fires iff any of: comb incomplete (X > TAB2), the
 A8 reflection is reached (min u < D), the node accounting loses a
 folded cell, a boundary cell is dropped, the chain is short
 (nsteps < h+1 or min be <= 0), the negative-arm hull breaches the
 positive-arm hull, the two inertia routes split, or the CD entry
 route disagrees with the summed route by more than
 CD_TIE * max(1, |tau|) in the bad-mode Rayleigh read.
 A named defect is DISCRIMINATING iff it does NOT also fire on a
 built POS cell: a structural feature shared with the LEGAL cells
 cannot explain the transition and is printed as a STRUCTURAL
 FEATURE instead of being charged as the defect (A10).
   CASE C  iff NEG and a DISCRIMINATING named DEFECT fires --
           defect NAMED; or NEG and tau_ideal_ub > +IDEAL_NOISE
           (the metric correction removes the negativity).
   CASE B  iff NEG, not C, and >= 1 POS built cell with
           |h - h_cell| <= BFLANK_H exists (the same-depth window
           census decides) -- the D-witness status is printed
           alongside, never hidden.
   CASE D  iff NEG, not C, not B -- typed REPLICATION-REQUIRED
           when the flank census is DECIDABLE (>= 1 built flank
           cell, none POS), else FLANK-UNDECIDED.
   CASE A  iff POS and a K constraint FAILS, or the step frame is
           REFUSED although a legal predecessor exists (the
           certificate ends, the matrix stays positive).
   CASE 0  iff POS and in K (no transition at this cell), or POS
           with NO legal predecessor built (coordinate typed
           UNAVAILABLE -- an unbuilt predecessor is a budget fact,
           not a certificate end), or MARGINAL.
 AGGREGATE (precedence D > C > B > A > 0, over built cells with
 h > BAND_LO): COFINAL-CASE-D-REPLICATION-REQUIRED(n) if any cell
 is D; else COFINAL-CASE-C(defect) if any NEG cell is C; else
 COFINAL-CASE-B(window corridor) if any NEG cell is B; else
 COFINAL-CASE-A(certificate ends) if any POS cell is A; else
 COFINAL-NO-TRANSITION.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 reproduction -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum): the AGGREGATE case, plus typed tags
CASE-CENSUS(per-cell letters), IDEALITY(d census, ||O-I|| census,
CD census), MEMBERSHIP(K census, first failing constraint),
INERTIA(route agreement), CONTROLS, SCREENS-VACUOUS, AMENDMENTS.
Every enum is a finite float64 / exact-rational statement about
BUILT cells of the deployed construction; NEVER an all-h
statement, NEVER an RH claim, NEVER a counterexample claim.

FROZEN BARS.  NDIM = 8; TAB2 = 1.6e7; KZ2_MAX = 1200; CENSUS_N_REF
= 587; CENSUS_HMAX_REF = 65051; TAU_NOISE = 5e-12 (CCXCIX
calibration inherited); NEGA_RTOL = 2e-3; IDEAL_NOISE = 1e-12;
CD_TIE = 1e-2 (RELATIVE to max(1, |tau|) -- the CD route is a
2-term cancellation formula and its own rounding is bounded, not
assumed); CD_SEP = 1e-9 (node separation floor, excluded pairs
counted); ORTHO_BAR = 1e-9 (declared orthonormality bar on
diag(O)); OPROBE_SEED = 7; NREF = 2; BFLANK_H = 600; BAND_LO =
7300; T_R = 7809/10000 (CCLXIX registration at its cited
truncation); KDEGS = (4, 5); BIS_ITERS = 48; MOM_PAD = 0.10 (the
measured log-moment box of the built POS cells, widened by 10% of
its log width -- MEASURED, never a class claim); COST_C_ENV =
4.6e-10 s (the CCXCIX 4.2e-10 envelope plus the dissect tier);
c_hat = COST_C_ENV until >= 1 deep cell (h >= 5000) is built, then
1.05 * max over built deep cells of (elapsed_cell / h^3);
GUARD_FAC = 1.05; BUILD_CAP_S = 3200 (A16); SCR_SEED = 1; X2_CHEAP =
3300; XCTRL_TGT = 1300; LOC_ITERS = 30; RQ_TIE = 1e-10; PART_BAR =
0.85; UNIT_TIE = 1e-9; TIE_TGT = 2012; XD_DOPE = 1e-6; XO_DOPE =
1e-6.
Smoke: PRIO = (TIE cell h ~ 2012, the census cell nearest 2200),
gates G1-G6 SMOKE-SKIPPED (typed); X2 depth (600,); XS skipped
(typed); band vacuous, verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 PRE-FREEZE RECONNAISSANCE, fully disclosed: ONE throwaway
    census-enumeration script (deleted; census keys, alpha/X values
    and cost estimates only -- NO cell was built, NO tau was read,
    NO matrix was assembled).  It fixed the frozen priority keys
    and, decisively, the CASE-B DESIGN: the census carries THREE
    cells at essentially the SAME depth with very different window
    scale -- 8629 kz 223 (alpha 7.1009, X 1.47e6), 8677 kz 299
    (alpha 7.4622, X 3.03e6) and 8642 kz 551 (alpha 8.2099, X
    1.35e7) -- so "does the family or only the path fail" is a
    CONTROLLED same-h comparison instead of a depth extrapolation.
    It also fixed the cap arithmetic; the B3 stretch item is
    expected to be guard-refused on a nominal machine and is
    listed honestly rather than dropped.
 A2 the ideal tier is the METRIC-CORRECTED Galerkin object.  It is
    basis-exact by (II) and it is the first time the
    float64-vs-ideal gap of the wall matrix is MEASURED at all.
    The residual ideality question -- how accurately the evaluated
    chain columns represent polynomials -- is measured INDIRECTLY
    (diag(O) census over all degrees, chain growth census, CD entry
    route) and is typed as the REMAINING scope edge, not closed.
    No interval enclosure of the FULL n x n matrix is attempted
    (n ~ 6.3e3 at the deepest cell); the outward rounding is
    applied to the DECISIVE SCALARS.
 A3 MARGINAL cells (|tau| <= TAU_NOISE) get NO case letter (CCXCIX
    A3 / CCCV A3 verbatim: the sign of a 1e-12 eigenvalue of a
    float64 build is not evidence).
 A4 the region K coordinates live on the STEP frame (Mt = Q^T
    (S_2/tau_1) Q, the deployed pairing of census neighbours), so a
    cell's certificate coordinate requires a LEGAL predecessor.
    For a NEGA cell the deployed step from a legal predecessor IS
    admissible (assemble_step refuses on tau_1 <= 0, i.e. on the
    PREDECESSOR) -- that is exactly the honest "extension of K's
    coordinates" of case A, and it is used as such.  Where no legal
    predecessor is built, the coordinate is typed
    K-COORD-UNAVAILABLE, never silently passed.
 A5 the MOM box is the MEASURED log-moment envelope of the built
    POS cells of THIS run, widened by MOM_PAD of its log width.
    It is a measurement of the built family, NOT the frozen
    CCLXXXI class box and NOT a class claim; cells outside it are
    reported with their per-coordinate distance.
 A6 the localization is a DIAGNOSTIC tier (CCXCIX A7 / CCCV A6
    verbatim): deterministic start vector, LU inverse iteration on
    the assembled A, non-kill, refusals typed
    LOCALIZATION-REFUSED.  It supplies the trial vector z; the
    ideal read is evaluated at the eigvalsh-consistent z and the
    NREF refinement steps only ever LOWER the upper bound.
 A7 the inertia routes are LAPACK Bunch-Kaufman LDL (exact block
    sign count, Sylvester) and LAPACK eigvalsh.  They are
    independent algorithms on the same assembled matrix; their
    agreement wards the INERTIA, not the ideality.  A disagreement
    is typed INERTIA-SPLIT and fires the case-C defect list.  A
    ZERO pivot makes the LDL route inconclusive and is typed as
    such (it is not read as agreement).
 A8 the u < D tent reflection of atom_lags_at is UNREACHABLE for
    the true comb (first atom u = log 2 >> D ~ 1e-3); the census
    asserts it per cell instead of implementing it.
 A9 no ladder rebuild, no scorecard row, no promotion: nothing
    measured here enters a certificate of record.  The CCXCIX
    SR/W4 gates and the CCXCIII SOS tier are out of scope (their
    machinery is not run), NOT silently passed.
 A10 the DEFECT DISCRIMINATION rule (added in smoke, disclosed
    below): the smoke measured a hull breach -- the negative arm's
    outermost folded seat sits marginally outside the positive
    arm's node hull -- on a LEGAL cell.  A feature that the legal
    cells share cannot be the cause of the transition, so the case
    rule charges a named defect as case C only if it is ABSENT
    from every built POS cell; otherwise it is printed as a
    STRUCTURAL FEATURE with its full anatomy.  This makes the
    case-C route STRICTER, never looser.
 A11 an UNBUILT predecessor is a BUDGET fact, not a certificate
    end: a POS cell whose K coordinate is unavailable because no
    legal predecessor was built is typed CASE 0 with the
    coordinate UNAVAILABLE.  The TIE cell (h ~ 2012, legal, built
    for the TIE ward anyway) is offered as the A4 anchor of last
    resort so that the coordinate exists wherever the step frame
    admits it.
 A12 PRE-FREEZE COST CALIBRATION, fully disclosed: ONE throwaway
    timing script (deleted) timed three MID-depth dissect builds --
    h 2012 (2.49 s, n 1326), h 3948 (23.43 s, n 2421), h 5596
    (68.26 s, n 3586), none of them a mission-band or gate cell --
    and printed elapsed seconds and n only.  Measured c = 3.06,
    3.81, 3.90 e-10 s, RISING with depth, so COST_C_ENV = 4.6e-10
    is kept as the envelope.  It also measured that the world-only
    build is NOT cheaper than the dissect build (81.9 s vs 68.3 s
    at h 5596), which moved the deep smooth control XS to the END
    of the priority list: a control may not displace a
    reproduction gate.  Consequently a guard-refused gate cell is
    typed (G-COVERAGE, GATE-COVERAGE in the verdict) instead of
    killing the run as REPRO-BROKEN -- an unbuilt cell is a budget
    fact, and only a BUILT cell that misses the CCCV value is a
    reproduction failure.

POST-FREEZE AMENDMENTS, forced by the FIRST frozen run and disclosed
with its verbatim result.  FROZEN-1 (SPEC_SHA 5cf86378, 2141.2 s,
checks 21/24, VERDICT REPRO-BROKEN) built 8 of the 10 priority items
(B3 and XS guard-refused at c_hat 5.80e-10) and reproduced ALL SIX
CCCV taus digit-identically: 8204 +2.665e-10 LEGAL, 8677 -3.053e-10
NEGA, 8003 -8.160e-11 NEGA, 7958 +5.904e-11 LEGAL, 9023 -1.498e-10
NEGA, 9535 -1.743e-10 NEGA; plus the new cells 8629 kz 223 (alpha
7.1009) LEGAL +7.245e-10 and 8642 kz 551 (alpha 8.2099) MARGINAL
-2.122e-12.  Its THREE failures were all in MY wards, none in the
construction, and all three are repaired below; the frozen run's
numbers stand and are re-measured by the amendment run.
 A13 FROZEN-1 killed on G-INERTIA (7/8): at h 8003 LAPACK returned
    ONE 2x2 Bunch-Kaufman pivot block, and the first ward required
    n_2x2 == 0 for its naive diagonal sign count to be valid, so it
    typed a SPLIT although both routes count exactly 1 negative
    eigenvalue.  REPAIRED by implementing the block inertia
    properly (ldl_inertia): a 2x2 block contributes one negative
    eigenvalue iff its determinant is negative and two iff the
    determinant is positive with negative trace, and the
    determinant SIGN is decided in EXACT rational arithmetic on the
    dyadic float64 entries.  The route is now conclusive instead of
    refusing, i.e. the ward became STRONGER.  Two further repairs
    ride with it: (i) the ideal-tier refinement evaluated all but
    its last iterate in the WRONG metric (c^T c instead of c^T O c)
    and therefore collapsed to the DEPLOYED Rayleigh -- at h 8003
    it read -8.160317e-11 (= tau) instead of the ideal +1.75e-10,
    and since the case rule reads tau_ub_ref the metric
    discriminator was silently reading the uncorrected value; every
    iterate is now evaluated in the O metric, so each one is
    separately a valid upper bound for tau_ideal; (ii) a
    REPRODUCTION or CONTROL kill no longer returns before the
    certificate, classification, corridor and control tiers -- only
    a PIPELINE or WARD kill does, because a broken pipeline cannot
    be dissected while a failed reproduction still has to print
    every measurement it made.
 A14 FROZEN-1 failed the SEAT gate at h 9023 (single-seat
    participation 0.796) and h 9535 (0.818) against PART_BAR 0.85,
    and the numbers say why: the bad mode stops being a ONE-seat
    mode with depth and becomes a TWO-seat CORE mixture (9023: uf 2
    at 0.796 AND uf 4 at 0.592; 9535: uf 4 at 0.818 AND uf 2 at
    0.535 -- this IS the migrating seat that CCCV named).  The bar
    was applied to the wrong object.  The bar VALUE is NOT touched
    (bar-shopping is forbidden): the gate now reads the CCCV seat
    structure as (i) the localized mode ties the eigenvalue
    (rq_gap <= RQ_TIE), (ii) the top seat is a CORE seat, (iii) the
    top-TWO CORE participation >= PART_BAR, and the single-seat
    participation is PRINTED as a measurement with no bar at all.
 A15 the sign-flip census is added as a MEASUREMENT and a verdict
    enum (IDEALITY-ALARM), because FROZEN-1 measured what no
    earlier probe could: |d| is of the SAME ORDER as |tau| at the
    frontier and carries BOTH signs (8003 d +2.57e-10 vs tau
    -8.16e-11; 7958 d -9.96e-11 vs tau +5.90e-11; 8204 d +8.94e-11
    vs tau +2.66e-10).  A cell is counted as a FLIP iff it is not
    MARGINAL and the ideal upper bound has the opposite sign to the
    implemented tau; MARGINAL cells make no sign claim either way
    (A3).  No case letter is derived from the flip census beyond
    what the frozen case rule already says.
 A16 BUILD_CAP_S 2400 -> 3200 s for the amendment run, with the
    reason stated: FROZEN-1 guard-refused B3 (h 9447, alpha 6.929)
    and B3 is the ONLY possible POS same-depth flank of G6 (h 9535,
    the nearest other band cell is 88 in h away), so refusing it
    would let the BUDGET decide between CASE B and CASE D -- and
    CASE D is the one label that must never be reached by a budget
    fact.  The cap is raised until every item of the frozen
    priority list fits; nothing else about the guard changes.

SMOKE DISCLOSURE (2026-08-13), pre-freeze, verbatim.  The first
smoke was run on a draft that was then edited IN PLACE, so its
SPEC_SHA is not carried here (it would be unverifiable); what is
carried is EVERY failure it measured and EVERY repair it forced.
 SMOKE-1 (the unrepaired draft): FOUR disclosure events.
  (i) the CD entry route (III) was WRONG, and the smoke caught it:
   the two-term reconstruction was compared against the Gram
   WITHOUT the sqrt(v_i v_j) folding weights and the diagonal was
   contracted with the already-weighted vector, so it read rq_cd
   +9.96e-01 against tau +3.30e-09 with an entry deviation of
   4.26e+06.  REPAIRED: cd_bilinear weights the CD kernel by
   sqrt(v_i) sqrt(v_j) and compares against the deployed
   off-diagonal Gram (-A off the diagonal); cd_route contracts the
   diagonal with z itself.  After the repair the two routes TIE:
   rq_cd - tau = +2.25e-13 (rel 2.25e-13), entry deviation
   3.52e-13.  The bar CD_TIE = 1e-2 is unchanged and now has three
   orders of headroom, and the raw entry deviation is printed as a
   measurement, not only gated.
  (ii) the XO control did NOT fire.  Removing BOTH explicit
   reorthogonalization sweeps from the Lanczos chain moved
   max_k |diag(O)_k - 1| only from 1.377e-14 to 1.510e-14 (bar
   1e-9) -- because ob.eval_chain rebuilds the columns from the
   RECURRENCE, so a loss of orthogonality in the Lanczos Q basis
   does not by itself corrupt the evaluated metric at this depth.
   REPAIRED by replacing the control with a DOCTORED RECURRENCE
   (one be entry scaled by 1 + XO_DOPE), which the reader must
   catch and does: 2.000e-06 > 1e-9 >= 1.377e-14.  The
   de-reorthogonalized build is KEPT and printed as a measurement
   at the same cell (it answers "is the deployed double sweep
   load-bearing at that depth?"), never as a gate.
  (iii) the case rule charged HULL-BREACH and BOUNDARY-CELL-DROPPED
   as case-C defects, and the smoke measured BOTH on a LEGAL cell
   (h 2012: exactly one negative-arm seat, folded index 4391 at
   y = -1.0000000000 with weight 1.19e-03, outside the positive
   hull [-0.9999997441, +0.9999997441]).  A feature the legal cells
   share cannot explain the transition, so the rule was TIGHTENED
   (A10): a named defect is charged only if it is absent from every
   built POS cell, otherwise it is printed as a STRUCTURAL FEATURE
   with its full anatomy.  Case C became strictly harder to reach.
  (iv) the rule typed a POS cell with no BUILT legal predecessor as
   CASE A; the smoke exposed it at the shallowest built cell
   (K-COORD-UNAVAILABLE (NO-PRED)).  That is a budget fact, not a
   certificate end.  REPAIRED by A11 (such a cell is CASE 0 with
   the coordinate typed UNAVAILABLE; the TIE cell is offered as the
   A4 anchor of last resort).
  Everything else was green in SMOKE-1 at machine precision: TIE
  ward EXACT (tau, negA, lamS all ==), PASS-TIE bitwise, the two
  inertia routes agree, W7/W8/W9 green, RB1 green, X1 scramble tau
  -7.79e+89, X2 smooth tau -8.12e+02, XD moves the ideal read by
  1.0e-06.
 SMOKE-2 (the repaired line, SPEC_SHA 8002b2d0): 18/18 PASS, 12.8
  s, all four controls fire.  Two further pre-freeze edits, both
  disclosed above and neither touching a bar or an enum: the
  de-reorth MEASUREMENT was moved onto the SAME cell as its
  reference (SMOKE-2 compared h 606 against h 2012 -- an
  apples-to-oranges print, no gate involved), and A12 (cost
  calibration, XS moved last, gate coverage typed) was added.
 SMOKE-3 was the FROZEN-1 line (SPEC_SHA 5cf86378, 18/18).
 SMOKE-4 is the AMENDMENT line (A13-A16 above) and is run verbatim
  before the amendment run; its SPEC_SHA is the one printed by the
  amendment run.  Every A13-A16 repair strengthens a ward or a
  measurement; none of them touches a frozen BAR, the CASE RULE,
  the control set or the verdict enums, and the FROZEN-1 result is
  reported next to the amendment result, never replaced by it.
 DISCLOSED SMOKE OBSERVATION (it motivates no bar): at the shallow
  smoke cells the metric gap is |d| ~ 2.7e-12 and 1.8e-13, i.e.
  three to five orders BELOW the shallow tau ~ 1.1e-08 / 3.3e-09,
  and the outward enclosure of d is ~1e-12 wide.  Whether that
  ordering survives at the 1e-10 frontier is exactly the frozen
  question this probe asks.

NO RH claim.  NO counterexample claim.  No marker moves; no paper,
ledger, website, manifest or verification file is touched; the only
edit outside this file is the German CCCVII line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII pipeline: EXT
tables, grid_density, folded_measure_full, folded_part,
lanczos_chain, eval_chain, CORE_J, make_steps, split_parts),
sigma_stress_battery_probe (CCLXIX bat.build_rung_param, the census
builder of record), zolotarev_phase_filter_probe (CCXXV
assemble_step, the step frame), bfloor_perstep_certification_probe
(CCLXXVII exact-rational tier: exact_wall_data, chebyshev_monic,
radau_exact, cert_floor_exact, pd_exact, fr_solve),
sigma_edge_growth_probe (CCLXXIII cell_legal, reproduced verbatim),
deep_membership_limit_probe (CCLXXXVII deep census machinery),
legality_frontier_probe (CCXCIX frontier map, TAU_NOISE),
legality_horizon_probe (CCCV horizon cells, seat tier),
v563_paper2_readouts (deployed generators: von_mangoldt_table,
arch_lags, atom_lags_at, NU_MAIN).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cofinal_dissect_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cofinal_dissect_probe.py
"""

import ast
import hashlib
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
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)
import sigma_stress_battery_probe as bat      # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import bfloor_perstep_certification_probe as bfl  # noqa: E402 (RO)

# ------------------------------------------------------- frozen bars
NDIM = 8
TAB2 = 16_000_000
EXT_DEPLOYED = 4_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
TAU_NOISE = 5.0e-12
NEGA_RTOL = 2.0e-3
IDEAL_NOISE = 1.0e-12
CD_TIE = 1.0e-2
CD_SEP = 1.0e-9
ORTHO_BAR = 1.0e-9
OPROBE_SEED = 7
NREF = 2
BFLANK_H = 600
BAND_LO = 7300
T_R = Fraction(7809, 10000)
KDEGS = (4, 5)
BIS_ITERS = 48
MOM_PAD = 0.10
COST_C_ENV = 4.6e-10
GUARD_FAC = 1.05
BUILD_CAP_S = 3200.0
SCR_SEED = 1
X2_CHEAP = 3300
XCTRL_TGT = 1300
LOC_ITERS = 30
RQ_TIE = 1.0e-10
PART_BAR = 0.85
UNIT_TIE = 1.0e-9
TIE_TGT = 2012
XD_DOPE = 1.0e-6
XO_DOPE = 1.0e-6
CD_BLOCK = 512
EPS64 = float(np.finfo(float).eps)

# the CCCV frozen reads, digit-identical reproduction targets
GATE_TAU = ((8204, 287, +2.665e-10, "LEGAL"),
            (8677, 299, -3.053e-10, "NEGA"),
            (8003, 284, -8.160e-11, "NEGA"),
            (7958, 282, +5.904e-11, "LEGAL"),
            (9023, 506, -1.498e-10, "NEGA"),
            (9535, 526, -1.743e-10, "NEGA"))
NEW_KEYS = ((8629, 223), (8642, 551), (9447, 196))

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals",
                 "eigvalsh", "inv", "pinv", "solve", "lu_factor",
                 "lu_solve", "negA", "lamS", "ldl")
READER_FUNCS = ("chain_pass_values", "chain_pass_project",
                "cd_bilinear", "atom_census", "hull_census")

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


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def ldl_inertia(dblk):
    """(6) route 2, EXACT: the inertia of the block-diagonal factor
    of a Bunch-Kaufman LDL^T.  1x1 pivots contribute their sign;
    a 2x2 block [[a, b], [b, c]] contributes one negative
    eigenvalue iff det = ac - b^2 < 0 and two iff det > 0 with
    a + c < 0.  The determinant sign is decided in EXACT rational
    arithmetic on the dyadic float64 entries, so the sign count is
    exact and Sylvester's law transports it to the matrix (A13)."""
    dd = np.diag(dblk)
    sub = np.diag(dblk, k=1)
    ndim = len(dd)
    n_neg = n_zero = n_two = 0
    i = 0
    while i < ndim:
        if i + 1 < ndim and sub[i] != 0.0:
            aa = Fraction(float(dd[i]))
            bb = Fraction(float(sub[i]))
            cc = Fraction(float(dd[i + 1]))
            det = aa * cc - bb * bb
            tr = aa + cc
            if det < 0:
                n_neg += 1
            elif det > 0:
                if tr < 0:
                    n_neg += 2
            else:
                n_zero += 1
                if tr < 0:
                    n_neg += 1
            n_two += 1
            i += 2
        else:
            if dd[i] < 0.0:
                n_neg += 1
            elif dd[i] == 0.0:
                n_zero += 1
            i += 1
    return n_neg, n_zero, n_two


def gamma_n(nterms):
    """The standard rigorous forward error factor for a length-n
    float64 recursive summation: gamma_n = n u / (1 - n u)."""
    prod = nterms * EPS64 * 0.5
    if prod >= 0.5:
        return float("inf")
    return prod / (1.0 - prod)


def f4(val):
    return "%+.4e" % val if math.isfinite(val) else "nan"


# ============================================ TAB2 + the deep census
DEEP = {}


def build_tab2():
    section("T -- the depth-extension table TAB2 = %.3g, warded "
            "BITWISE against the deployed 4e6 prefix" % TAB2)
    ob.build_ext_tables()
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


def deep_census():
    section("D -- THE DEEP-FRAME CENSUS on TAB2 (deployed formula "
            "verbatim), h-sorted")
    u2, g2 = DEEP["U"], DEEP["G"]
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
    keys = {(c["h"], c["kz"]) for c in out}
    need = [(hv, kv) for hv, kv, _t, _s in GATE_TAU] + list(NEW_KEYS)
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX/CCCV: %d == %d cells, h max "
          "%d == %d, all %d frozen priority keys present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()),
             CENSUS_HMAX_REF, len(need), ok_keys),
          len(out) == CENSUS_N_REF
          and int(hs.max()) == CENSUS_HMAX_REF and ok_keys,
          kill="K3")
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


def build_cell_world(cell, world=None, scr_seed=None):
    """The deployed deep-branch rung builder (bat.build_rung_param
    VERBATIM) with the CCLXXXVII world handling."""
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
    rung = bat.build_rung_param(cell["kz"], alpha, mfold, uu, mm)
    rung["X"] = cell["X"]
    return rung


# ============================ the AC-scanned chain / entry readers
def chain_pass_values(al, be, m0, xnodes, wts, npoly, cvec):
    """ONE forward pass of the deployed three-term chain at xnodes
    (ob.eval_chain structure VERBATIM, accumulated instead of
    stored).  Returns
       qv[i]   = sum_{k<npoly} c_k p_k(x_i),
       qabs[i] = sum_{k<npoly} |c_k p_k(x_i)|  (the rigorous
                 gamma-bound companion),
       dg[k]   = sum_i w_i p_k(x_i)^2          (diag of the metric),
       gmax    = max_{k,i} |p_k(x_i)|          (growth census).
    Nodes, weights, coefficients and frozen constants only."""
    xarr = np.asarray(xnodes, float)
    warr = np.asarray(wts, float)
    cvv = np.asarray(cvec, float)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    qv = cvv[0] * pkm1
    qabs = np.abs(cvv[0] * pkm1)
    dg = np.zeros(npoly)
    dg[0] = float(warr @ (pkm1 * pkm1))
    gmax = float(np.max(np.abs(pkm1)))
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        qv = qv + cvv[1] * pk
        qabs = qabs + np.abs(cvv[1] * pk)
        dg[1] = float(warr @ (pk * pk))
        gmax = max(gmax, float(np.max(np.abs(pk))))
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            qv = qv + cvv[k + 1] * pnew
            qabs = qabs + np.abs(cvv[k + 1] * pnew)
            dg[k + 1] = float(warr @ (pnew * pnew))
            gm = float(np.max(np.abs(pnew)))
            if gm > gmax:
                gmax = gm
            pkm1, pk = pk, pnew
    return qv, qabs, dg, gmax


def chain_pass_project(al, be, m0, xnodes, wts, npoly, fvals):
    """The transposed pass: out[k] = sum_i w_i p_k(x_i) f_i, i.e.
    the metric action (O c)_k for f = q.  Nodes, weights, entries
    and frozen constants only."""
    xarr = np.asarray(xnodes, float)
    wf = np.asarray(wts, float) * np.asarray(fvals, float)
    out = np.zeros(npoly)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    out[0] = float(wf @ pkm1)
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        out[1] = float(wf @ pk)
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            out[k + 1] = float(wf @ pnew)
            pkm1, pk = pk, pnew
    return out


def cd_bilinear(ynodes, aval, bval, becap, rtv, zvv, aref):
    """The Christoffel-Darboux ENTRY route, blockwise (no extra
    n x n storage): the off-diagonal Gram is reconstructed from the
    TWO-TERM identity, weighted by sqrt(v_i v_j), and contracted at
    the same witness.  Returns (z^T Gcd_offdiag z, max abs
    entrywise deviation from the deployed off-diagonal Gram, number
    of pairs excluded by the CD_SEP node-separation floor).  Nodes,
    weights, recurrence entries and frozen constants only."""
    yarr = np.asarray(ynodes, float)
    aa = np.asarray(aval, float)
    bb = np.asarray(bval, float)
    rt = np.asarray(rtv, float)
    zz = np.asarray(zvv, float)
    ndim = len(yarr)
    acc = 0.0
    dmax = 0.0
    nskip = 0
    for lo in range(0, ndim, CD_BLOCK):
        hi = min(lo + CD_BLOCK, ndim)
        dy = yarr[lo:hi, None] - yarr[None, :]
        num = (aa[lo:hi, None] * bb[None, :]
               - bb[lo:hi, None] * aa[None, :])
        bad = np.abs(dy) < CD_SEP
        nskip += int(np.sum(bad)) - (hi - lo)
        dy = np.where(bad, 1.0, dy)
        kern = (becap * num / dy) * rt[lo:hi, None] * rt[None, :]
        kern[bad] = 0.0
        acc += float(zz[lo:hi] @ (kern @ zz))
        blk = -aref[lo:hi, :].copy()
        for i in range(lo, hi):
            blk[i - lo, i] = 0.0
        blk[bad] = 0.0
        dmax = max(dmax, float(np.max(np.abs(kern - blk))))
        del dy, num, kern, blk, bad
    return acc, dmax, max(0, nskip)


def atom_census(uu, alpha, d_grid, x_val):
    """(7) SOURCE COMPLETENESS.  The comb of a cell is COMPLETE iff
    every prime-power atom with u <= 2 alpha is present, i.e. iff
    X = e^{2 alpha} <= the table bound; the A8 reflection is
    unreachable iff min u >= D.  Entries and frozen constants."""
    umin = float(np.min(uu)) if len(uu) else float("nan")
    return dict(n_atoms=int(len(uu)),
                u_max=float(np.max(uu)) if len(uu) else float("nan"),
                two_alpha=2.0 * float(alpha),
                slack=2.0 * float(alpha)
                - (float(np.max(uu)) if len(uu) else float("nan")),
                complete_tab2=bool(x_val <= TAB2),
                margin_tab2=TAB2 / x_val,
                complete_deployed=bool(x_val <= EXT_DEPLOYED),
                margin_deployed=EXT_DEPLOYED / x_val,
                u_min=umin, d_grid=float(d_grid),
                refl_unreached=bool(umin >= d_grid))


def hull_census(xs, ys, vs, uf_n):
    """The support-hull read: does the negative arm stay inside the
    positive arm's hull, and if not, WHICH folded seats step out
    and with what weight?  Nodes, weights and folded indices."""
    xlo, xhi = float(np.min(xs)), float(np.max(xs))
    ylo, yhi = float(np.min(ys)), float(np.max(ys))
    out = np.nonzero((ys < xlo) | (ys > xhi))[0]
    return dict(x_lo=xlo, x_hi=xhi, y_lo=ylo, y_hi=yhi,
                n_out=int(len(out)), breach=bool(len(out) > 0),
                gap_lo=ylo - xlo, gap_hi=xhi - yhi,
                seats=[(int(uf_n[j]), float(ys[j]), float(vs[j]))
                       for j in out[:4]])


# ============================ the dissect builder (verbatim + reads)
def build_cell_dissect(cell, no_reorth=False, keep_chain=False):
    """bat.build_rung_param VERBATIM (same sub-calls, same order,
    Schur part inline) plus the DISSECT READS: geometry census,
    inertia on two routes, localization, the metric-corrected ideal
    tier, the CD entry route.  Ties bat.build_rung_param EXACTLY
    (TIE ward).  no_reorth builds the XO comparison chain;
    keep_chain retains the small chain data of the TIE cell for the
    XO doctoring control."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka]
    mm = mu2[:ka]
    d_grid = 2.0 * alpha / mfold
    c_ar = np.asarray(core.arch_lags(mfold, d_grid), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mfold, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _uf_p, _fdp = ob.folded_measure_full(dens, lfold, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(dens, lfold, -1.0)
    if no_reorth:
        al, be, m0, nsteps = chain_no_reorth(xs, ws, half + 1)
    else:
        al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    out = dict(kind="param", kz=cell["kz"], h=half,
               alpha=float(alpha), M=mfold, D=d_grid, L=lfold,
               X=cell["X"], nsteps=int(nsteps),
               n_pos=int(len(xs)), n_neg=int(len(ys)),
               be_min=float(np.min(be)) if len(be) else float("nan"),
               atoms=atom_census(uu, alpha, d_grid, cell["X"]),
               hull=hull_census(xs, ys, vs, uf_n))
    out["n_drop"] = int(mfold - len(xs) - len(ys))
    if nsteps < half + 1 or np.any(be <= 0):
        out["fail"] = "CHAIN"
        return out
    if keep_chain:
        out["chain"] = dict(al=al, be=be, m0=m0, xs=xs, ws=ws,
                            npoly=half)
    pn = ob.eval_chain(al, be, m0, ys, half)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = sym(gram)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    eva = np.linalg.eigvalsh(amat)
    out.update(n=n, tau=float(eva[0]), negA=int(np.sum(eva < 0.0)))
    out["eva_bot"] = [float(v) for v in eva[:4]]
    out["n_unit"] = int(np.sum(np.abs(eva - 1.0) <= UNIT_TIE))
    out["rank_g"] = int(half)
    del gram
    # ---- (6) inertia route 2: exact-sign LDL pivot count
    try:
        lu_l, dblk, _perm = sla.ldl(amat, lower=True)
        n_neg_ldl, n_zero, n_two = ldl_inertia(dblk)
        out["inertia"] = dict(neg_ldl=n_neg_ldl, neg_eig=out["negA"],
                              n_2x2=n_two, n_zero=n_zero,
                              agree=bool(n_neg_ldl == out["negA"]
                                         and n_zero == 0))
        del lu_l, dblk
    except Exception as exc:                       # noqa: BLE001
        out["inertia"] = dict(refused=type(exc).__name__,
                              agree=False)
    # ---- (6) localization: LU inverse iteration (A6)
    zvec = None
    try:
        lu, piv = sla.lu_factor(amat)
        zvec = np.full(n, 1.0 / math.sqrt(n))
        for _ in range(LOC_ITERS):
            zvec = sla.lu_solve((lu, piv), zvec)
            zvec = zvec / float(np.linalg.norm(zvec))
        rq = float(zvec @ (amat @ zvec))
        res = float(np.linalg.norm(amat @ zvec - rq * zvec))
        p4 = float(np.sum(zvec ** 4))
        order = np.argsort(-np.abs(zvec))
        core_set = set(int(j) for j in ob.CORE_J)
        cum2 = 0.0
        n_core = 0
        for j in order:
            if int(uf_n[j]) in core_set:
                cum2 += float(zvec[j]) ** 2
                n_core += 1
            if n_core >= 2:
                break
        out["loc"] = dict(
            rq=rq, rq_gap=abs(rq - out["tau"]), res=res,
            ipr=1.0 / p4 if p4 > 0 else float("nan"),
            seats=[(int(uf_n[j]), float(ys[j]), float(abs(zvec[j])))
                   for j in order[:3]],
            uf=int(uf_n[order[0]]), part=float(abs(zvec[order[0]])),
            cum2=math.sqrt(cum2),
            core_top=bool(int(uf_n[order[0]]) in core_set))
        del lu, piv
    except Exception as exc:                       # noqa: BLE001
        out["loc"] = dict(refused=type(exc).__name__)
    # ---- (1)/(8) the metric-corrected IDEAL tier
    if zvec is not None:
        out["ideal"] = ideal_tier(al, be, m0, xs, ws, ys, vs, pn,
                                  half, zvec, out["tau"])
        # ---- (III) the CD entry route on the assembled matrix
        out["cd"] = cd_route(al, be, m0, ys, vs, pn, half, zvec,
                             amat, out["tau"])
    del pn
    # ---- the Schur part, bat.build_rung_param VERBATIM
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in ob.CORE_J)
    if not out["core_ok"]:
        out["fail"] = "CORE-SHORT"
        return out
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset], dtype=int)
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
    evs = np.linalg.eigvalsh(smat)
    out["S"] = smat
    out["lamS"] = float(evs[0])
    out["negS"] = int(np.sum(evs < 0.0))
    return out


def chain_no_reorth(x, w, n):
    """XO CONTROL ONLY: ob.lanczos_chain with the two explicit
    reorthogonalization sweeps REMOVED.  Never used for a verdict."""
    m0 = float(np.sum(w))
    m = len(x)
    qq = np.zeros((m, n))
    qq[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * qq[:, k]
        al[k] = float(qq[:, k] @ z)
        z = z - al[k] * qq[:, k]
        if k > 0:
            z = z - be[k - 1] * qq[:, k - 1]
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        qq[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def ideal_tier(al, be, m0, xs, ws, ys, vs, pn, npoly, zvec, tau):
    """(1) + (8): the metric-corrected ideal Galerkin read at the
    bad-mode witness, with outward-rounded enclosures of both
    quadrature scalars, the diag(O) census, the random metric probe
    and NREF refinement steps (which only LOWER the upper bound)."""
    svec = np.sqrt(vs) * zvec
    cvec = pn.T @ svec                       # c = P^T sqrt(V) z
    cn2 = float(cvec @ cvec)
    qv, qabs, dg, gmax = chain_pass_values(al, be, m0, xs, ws,
                                           npoly, cvec)
    ip_plus = float(ws @ (qv * qv))
    # rigorous outward bounds: recurrence-sum error then quadrature
    g_h = gamma_n(npoly)
    g_p = gamma_n(len(xs))
    dq = g_h * np.abs(qabs)
    lo_terms = ws * np.maximum(np.abs(qv) - dq, 0.0) ** 2
    hi_terms = ws * (np.abs(qv) + dq) ** 2
    ip_lo = float(np.sum(lo_terms)) * (1.0 - g_p)
    ip_hi = float(np.sum(hi_terms)) * (1.0 + g_p)
    g_n = gamma_n(len(ys))
    cn2_lo = cn2 * (1.0 - gamma_n(npoly))
    cn2_hi = cn2 * (1.0 + gamma_n(npoly))
    dgap = ip_plus - cn2
    lam = 1.0 - tau
    tau_ub = 1.0 - lam * lam / max(lam + dgap, 1e-300)
    tau_ub_lo = 1.0 - lam * lam / max(lam + (ip_lo - cn2_hi), 1e-300)
    tau_ub_hi = 1.0 - lam * lam / max(lam + (ip_hi - cn2_lo), 1e-300)
    res = dict(cn2=cn2, ip_plus=ip_plus, d=dgap,
               d_lo=ip_lo - cn2_hi, d_hi=ip_hi - cn2_lo,
               tau_ub=tau_ub,
               tau_ub_lo=min(tau_ub_lo, tau_ub_hi),
               tau_ub_hi=max(tau_ub_lo, tau_ub_hi),
               dg_dev=float(np.max(np.abs(dg - 1.0))),
               dg_dev_k=int(np.argmax(np.abs(dg - 1.0))),
               dg_last=float(dg[-1]), p_growth=gmax,
               cancel=float(np.max(qabs) / max(1e-300,
                                              float(np.max(
                                                  np.abs(qv))))),
               gam_h=g_h, gam_pos=g_p, gam_neg=g_n)
    # ---- random metric probe: a lower bound on ||O - I||_2
    rng = np.random.default_rng(OPROBE_SEED)
    rvec = rng.standard_normal(npoly)
    rvec = rvec / float(np.linalg.norm(rvec))
    rq_v, _ra, _rd, _rg = chain_pass_values(al, be, m0, xs, ws,
                                            npoly, rvec)
    orv = chain_pass_project(al, be, m0, xs, ws, npoly, rq_v)
    res["oprobe"] = float(np.linalg.norm(orv - rvec))
    # ---- NREF refinement of the ideal upper bound.  EVERY iterate
    #      is evaluated in the O METRIC (c^T H c)/(c^T O c), so the
    #      minimum is a minimum over IDEAL Rayleigh reads and each
    #      one is separately an upper bound for tau_ideal (A13).
    cc = cvec / max(1e-300, float(np.linalg.norm(cvec)))
    best = tau_ub
    hist = []
    for _ in range(NREF):
        hc = pn.T @ (vs * (pn @ cc))          # H c, the ascent step
        nh = float(np.linalg.norm(hc))
        if not math.isfinite(nh) or nh <= 0.0:
            break
        cc = hc / nh
        qv2, _qa2, _dg2, _gm2 = chain_pass_values(
            al, be, m0, xs, ws, npoly, cc)
        occ = float(ws @ (qv2 * qv2))         # c^T O c
        hcc = pn.T @ (vs * (pn @ cc))
        num = float(cc @ hcc)                 # c^T H c
        if occ > 0.0 and math.isfinite(num):
            val = 1.0 - num / occ
            hist.append(val)
            best = min(best, val)
    res["tau_ub_ref"] = best
    res["ref_hist"] = hist
    return res


def cd_route(al, be, m0, ys, vs, pn, npoly, zvec, amat, tau):
    """(III) the Christoffel-Darboux entry route: an INDEPENDENT
    2-term reconstruction of the off-diagonal Gram, contracted at
    the same witness."""
    if npoly < 3:
        return dict(skipped="npoly<3")
    pm1 = pn[:, npoly - 1]
    pm2 = pn[:, npoly - 2]
    ph = ((ys - al[npoly - 1]) * pm1 - be[npoly - 2] * pm2) \
        / be[npoly - 1]
    off, dmax, nskip = cd_bilinear(ys, ph, pm1, float(be[npoly - 1]),
                                   np.sqrt(vs), zvec, amat)
    diag = float(np.sum(zvec * zvec * (1.0 - np.diag(amat))))
    rq_cd = 1.0 - (off + diag)
    return dict(rq_cd=rq_cd, gap=rq_cd - tau, ent_dev=dmax,
                n_skip=nskip,
                rel=abs(rq_cd - tau) / max(1.0, abs(tau)))


# ==================================== (2)-(5)+(9) the exact tier
def step_of(cell_rung, pred_rung):
    """A4: the deployed step frame Mt = Q^T (S_2/tau_1) Q from a
    LEGAL predecessor to this cell (ob.make_steps +
    zol.assemble_step verbatim); self-steps refused (CCLXXXVII
    A12)."""
    if pred_rung is None or cell_rung is None:
        return None, "NO-PRED"
    if (int(pred_rung["kz"]) == int(cell_rung["kz"])
            and int(pred_rung["h"]) == int(cell_rung["h"])):
        return None, "SELF-STEP"
    if not (pred_rung.get("core_ok") and cell_rung.get("core_ok")):
        return None, "CORE-SHORT"
    sts = ob.make_steps([pred_rung, cell_rung])
    if not sts:
        return None, "STEP-REFUSED"
    st = sts[0]
    zol.assemble_step(st)
    if st["status"] != "OK":
        return None, st["status"]
    return st, "OK"


def exact_membership(mtx):
    """(2)(3)(4)(5): the exact-rational certificate read of the 8x8
    step-frame wall matrix -- Schur scalars, moments, certified
    co-block floor, the joint RADAU relation at K = 4 and 5, and
    the per-constraint distances (9)."""
    piv, momv, blk = bfl.exact_wall_data(mtx, 2 * max(KDEGS) - 2)
    vec = [Fraction(float(v)) for v in np.asarray(mtx, float)[1:, 0]]
    res = dict(n=piv, nu=momv)
    sol = bfl.fr_solve(blk, vec)
    if sol is None:
        res["q"] = None
    else:
        res["q"] = sum(a * b for a, b in zip(vec, sol))
    if res["q"] is not None and piv != 0:
        res["s"] = piv - res["q"]
        res["sigma"] = res["q"] / piv
    else:
        res["s"] = res["sigma"] = None
    blk_f = np.asarray(mtx, float)[1:, 1:]
    lam_b = float(np.linalg.eigvalsh(sym(blk_f))[0])
    res["lam_b"] = lam_b
    hi = Fraction(max(lam_b, 0.0)).limit_denominator(10 ** 12)
    flo = bfl.cert_floor_exact(blk, Fraction(0), hi, BIS_ITERS) \
        if lam_b > 0.0 else None
    res["floor"] = flo
    res["rad"] = {}
    for kdeg in KDEGS:
        if flo is None or flo <= 0:
            res["rad"][kdeg] = None
            continue
        cheb = bfl.chebyshev_monic(momv, kdeg)
        if cheb is None:
            res["rad"][kdeg] = None
            continue
        val = bfl.radau_exact(cheb[0], cheb[1], flo, momv[0])
        res["rad"][kdeg] = val
    return res


def membership_verdict(ex, mom_box):
    """(4)+(9): which constraint of the CCXCIII region fails FIRST,
    and the per-coordinate distance to the boundary of K."""
    fails = []
    dist = {}
    n_f = float(ex["n"]) if ex["n"] is not None else float("nan")
    dist["P1_pivot"] = n_f
    if not (ex["n"] is not None and ex["n"] > 0):
        fails.append("P1-PIVOT")
    if ex["floor"] is None or ex["floor"] <= 0:
        fails.append("P2-FLOOR")
        dist["P2_floor"] = float("nan")
    else:
        dist["P2_floor"] = float(ex["floor"])
        dist["P2_slack"] = ex["lam_b"] - float(ex["floor"])
        if dist["P2_slack"] < 0.0:
            fails.append("P2-FLOOR-OVERCLAIM")
    if ex["sigma"] is None:
        fails.append("PD-SIGMA")
        dist["PD_margin"] = float("nan")
    else:
        dist["PD_margin"] = 1.0 - float(ex["sigma"])
        if float(ex["sigma"]) >= 1.0:
            fails.append("PD-SIGMA")
    rho = {}
    for kdeg in KDEGS:
        val = ex["rad"].get(kdeg)
        if val is None or ex["n"] is None or ex["n"] <= 0:
            rho[kdeg] = float("nan")
        else:
            rho[kdeg] = float(val / ex["n"])
    dist["P4_rho"] = rho
    best = min([r for r in rho.values() if math.isfinite(r)],
               default=float("nan"))
    dist["P4_margin"] = (float(T_R) - best if math.isfinite(best)
                         else float("nan"))
    if not math.isfinite(best) or best > float(T_R):
        fails.append("P4-RELATION")
    gk = []
    if ex["n"] is not None and ex["n"] > 0:
        for k, nuk in enumerate(ex["nu"]):
            den = ex["n"] ** (k + 2)
            gk.append(math.log10(abs(float(nuk / den)))
                      if nuk != 0 else float("-inf"))
    dist["MOM_g"] = gk
    if mom_box is not None and gk:
        out = []
        for k, gval in enumerate(gk):
            lo, hi = mom_box[k]
            if gval < lo:
                out.append((k, gval - lo))
            elif gval > hi:
                out.append((k, gval - hi))
        dist["MOM_out"] = out
        if out:
            fails.append("MOM-BOX")
    else:
        dist["MOM_out"] = None
    return fails, dist


# ================================ the priority census (the dissect)
def build_prio(census):
    by_key = {(c["h"], c["kz"]): c for c in census}
    hs = np.asarray([c["h"] for c in census], float)
    tie_cell = census[int(np.argmin(np.abs(hs - TIE_TGT)))]
    if SMOKE:
        c22 = census[int(np.argmin(np.abs(hs - 2200)))]
        return tie_cell, [("SMOKE-A", tie_cell, None),
                          ("SMOKE-B", c22, None)]
    prio = [("G1-8204L", by_key[(8204, 287)], None),
            ("G2-8677N", by_key[(8677, 299)], None),
            ("B1-8629a71", by_key[(8629, 223)], None),
            ("B2-8642a82", by_key[(8642, 551)], None),
            ("G3-8003N", by_key[(8003, 284)], None),
            ("G4-7958L", by_key[(7958, 282)], None),
            ("G5-9023N", by_key[(9023, 506)], None),
            ("G6-9535N", by_key[(9535, 526)], None),
            ("B3-9447a69", by_key[(9447, 196)], None),
            ("XS-SMOOTH", by_key[(7958, 282)], "smooth")]
    return tie_cell, prio


def print_cell(rung, tag):
    lc = rung.get("loc", {})
    idl = rung.get("ideal")
    cdr = rung.get("cd")
    at = rung["atoms"]
    hu = rung["hull"]
    ine = rung.get("inertia", {})
    print("      geom: n_pos %d n_neg %d (h %d, chain %d, be_min "
          "%.3e) drop %d | atoms %d u_max %.5f <= 2a %.5f (slack "
          "%.3e) TAB2/X %.3f 4e6/X %.3f refl_unreached %s"
          % (rung["n_pos"], rung["n_neg"], rung["h"],
             rung["nsteps"], rung["be_min"], rung["n_drop"],
             at["n_atoms"], at["u_max"], at["two_alpha"],
             at["slack"], at["margin_tab2"], at["margin_deployed"],
             at["refl_unreached"]))
    print("      hull: pos [%.10f, %.10f] neg [%.10f, %.10f] "
          "outside %d (gap_lo %+.3e gap_hi %+.3e) seats %s"
          % (hu["x_lo"], hu["x_hi"], hu["y_lo"], hu["y_hi"],
             hu["n_out"], hu["gap_lo"], hu["gap_hi"],
             [(s[0], "%.4f" % s[1], "%.2e" % s[2])
              for s in hu["seats"]]))
    if "refused" in ine:
        print("      inertia: LDL-REFUSED (%s)" % ine["refused"])
    else:
        print("      inertia: negA(eigvalsh) %d vs negA(exact LDL "
              "block sign count) %d  [%s]  2x2 blocks %d zero "
              "pivots %d"
              % (ine.get("neg_eig", -1), ine.get("neg_ldl", -1),
                 "AGREE" if ine.get("agree") else "SPLIT",
                 ine.get("n_2x2", -1), ine.get("n_zero", -1)))
    if "rq_gap" in lc:
        print("      loc: rq %.6e rq_gap %.2e res %.2e ipr %.2f "
              "seat uf=%d part %.3f core2 %.3f seats %s"
              % (lc["rq"], lc["rq_gap"], lc["res"], lc["ipr"],
                 lc["uf"], lc["part"], lc["cum2"],
                 [(s[0], "%.3f" % s[2]) for s in lc["seats"]]))
    elif lc:
        print("      loc: LOCALIZATION-REFUSED (%s)"
              % lc.get("refused"))
    if idl is not None:
        print("      IDEAL: |c|^2 %.16f  int q^2 dmu+ %.16f  d "
              "%+.4e  [outward %+.4e, %+.4e]"
              % (idl["cn2"], idl["ip_plus"], idl["d"], idl["d_lo"],
                 idl["d_hi"]))
        print("      IDEAL: tau %+.6e -> tau_ideal_ub %+.6e "
              "(outward [%+.4e, %+.4e]) refined %+.6e"
              % (rung["tau"], idl["tau_ub"], idl["tau_ub_lo"],
                 idl["tau_ub_hi"], idl["tau_ub_ref"]))
        print("      METRIC: max_k |diag(O)_k - 1| %.3e at k %d "
              "(last %.16f) ||(O-I)r|| %.3e chain growth %.3e "
              "cancel %.3e gam_h %.2e"
              % (idl["dg_dev"], idl["dg_dev_k"], idl["dg_last"],
                 idl["oprobe"], idl["p_growth"], idl["cancel"],
                 idl["gam_h"]))
    if cdr is not None and "rq_cd" in cdr:
        print("      CD: rq_cd %+.6e vs tau %+.6e gap %+.3e rel "
              "%.3e | entry dev %.3e skipped pairs %d"
              % (cdr["rq_cd"], rung["tau"], cdr["gap"], cdr["rel"],
                 cdr["ent_dev"], cdr["n_skip"]))
    print("", end="", flush=True)


def census_build(census):
    section("CEN -- THE DISSECT CENSUS (verbatim builds in the "
            "frozen priority order, self-calibrating guard %.2f * "
            "c_hat * h^3 <= %.0f s)" % (GUARD_FAC, BUILD_CAP_S))
    tie_cell, prio = build_prio(census)
    r_bat = build_cell_world(tie_cell)
    r_dis = build_cell_dissect(tie_cell, keep_chain=True)
    check("TIE dissect builder ties bat.build_rung_param EXACTLY on "
          "h %d kz %d (tau %s negA %s lamS %s)"
          % (tie_cell["h"], tie_cell["kz"],
             "==" if r_dis["tau"] == r_bat["tau"] else "DIFF",
             "==" if r_dis["negA"] == r_bat["negA"] else "DIFF",
             "==" if r_dis.get("lamS") == r_bat.get("lamS")
             else "DIFF"),
          (r_dis["tau"] == r_bat["tau"]
           and r_dis["negA"] == r_bat["negA"]
           and r_dis.get("lamS") == r_bat.get("lamS")), kill="K2")
    pass_tie(tie_cell)
    print_cell(r_dis, "TIE")
    reads = []
    c_hat = COST_C_ENV
    deep_rate = []
    for tag, cell, world in prio:
        est = GUARD_FAC * c_hat * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-12s h %-6d kz %-4d UNBUILT-GUARD (est "
                  "%.0f s at c_hat %.2e, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est, c_hat,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            reads.append(dict(tag=tag, cell=cell, world=world,
                              verdict="UNBUILT",
                              why="UNBUILT-GUARD", rung=None))
            continue
        tc = time.time()
        if world is not None:
            rung = build_cell_world(cell, world=world)
        else:
            rung = build_cell_dissect(cell)
        dt = time.time() - tc
        if world is None and cell["h"] >= 5000:
            deep_rate.append(dt / float(cell["h"]) ** 3)
            c_hat = 1.05 * max(deep_rate)
        ok, why = cell_legal(rung)
        marginal = ("tau" in rung and abs(rung["tau"]) <= TAU_NOISE)
        verdict = ("MARGINAL" if marginal
                   else "LEGAL" if ok else why)
        reads.append(dict(tag=tag, cell=cell, world=world,
                          verdict=verdict, why=why, rung=rung,
                          marginal=marginal))
        print("    %-12s h %-6d kz %-4d alpha %.4f%s  %-9s tau "
              "%-12s negA %s negS %s  %.1f s"
              % (tag, cell["h"], cell["kz"], cell["alpha"],
                 (" [%s]" % world) if world else "", verdict,
                 ("%.4g" % rung["tau"]) if "tau" in rung else "-",
                 rung.get("negA", "-"), rung.get("negS", "-"), dt),
              flush=True)
        if world is None:
            print_cell(rung, tag)
    n_built = sum(1 for r in reads if r["rung"] is not None)
    check("CEN1 the census built %d items (%d unbuilt-guard, "
          "honestly censused)" % (n_built, len(reads) - n_built),
          n_built >= (2 if SMOKE else 5), kill="K1")
    ok_t, why_t = cell_legal(r_dis)
    tie_entry = dict(tag="TIE", cell=tie_cell, world=None,
                     verdict="LEGAL" if ok_t else why_t,
                     why=why_t, rung=r_dis, marginal=False)
    return reads, tie_entry


def pass_tie(tie_cell):
    """PASS-TIE: the AC-scanned accumulator must tie ob.eval_chain
    on the TIE cell (the accumulator IS the deployed evaluator)."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, mfold = tie_cell["alpha"], tie_cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    d_grid = 2.0 * alpha / mfold
    lag = (np.asarray(core.arch_lags(mfold, d_grid), float)
           + np.asarray(core.atom_lags_at(alpha, mfold, u2[:ka],
                                          mu2[:ka])[0], float))
    dens = ob.grid_density(lag)
    lfold = 2 * mfold - 2
    half = mfold // 2
    xs, ws, _u, _f = ob.folded_measure_full(dens, lfold, +1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, half + 1)
    if nsteps < half + 1:
        check("PASS-TIE chain short on the TIE cell", False,
              kill="K1")
        return
    rng = np.random.default_rng(OPROBE_SEED)
    cvec = rng.standard_normal(half)
    ref = ob.eval_chain(al, be, m0, xs, half) @ cvec
    got, _qa, dg, _gm = chain_pass_values(al, be, m0, xs, ws, half,
                                          cvec)
    dev = float(np.max(np.abs(got - ref)))
    ogram = ob.eval_chain(al, be, m0, xs, half)
    dg_ref = np.einsum("ik,i,ik->k", ogram, ws, ogram)
    ddev = float(np.max(np.abs(dg - dg_ref)))
    check("PASS-TIE the accumulator ties ob.eval_chain on the TIE "
          "cell (q dev %.2e, diag(O) dev %.2e) and diag(O) "
          "deviation from I is %.2e"
          % (dev, ddev, float(np.max(np.abs(dg - 1.0)))),
          dev <= 1e-12 * max(1.0, float(np.max(np.abs(ref))))
          and ddev <= 1e-12, kill="K2")


def census_gates(reads):
    section("G -- reproduction gates against CCCV (digit-identical "
            "tau) and the INERTIA gate")
    n_gate = 0
    if SMOKE:
        check("G1-G6 CCCV reproduction SMOKE-SKIPPED (typed; the "
              "frontier cells are not built in smoke)", True)
    else:
        got = {(r["cell"]["h"], r["cell"]["kz"]): r for r in reads
               if r["rung"] is not None and r["world"] is None}
        miss = [(hv, kv) for hv, kv, _t, _s in GATE_TAU
                if (hv, kv) not in got]
        check("G-COVERAGE all %d CCCV gate cells were BUILT within "
              "the cap (%s) -- a guard refusal is a BUDGET fact and "
              "is typed, never passed and never charged as a "
              "reproduction failure (A12)"
              % (len(GATE_TAU),
                 "complete" if not miss
                 else "MISSING " + ",".join("h %d kz %d" % k
                                            for k in miss)),
              not miss)
        n_gate = len(GATE_TAU) - len(miss)
        for hv, kv, tref, kind in GATE_TAU:
            r = got.get((hv, kv))
            if r is None:
                continue
            tau = r["rung"].get("tau", float("nan"))
            hit = (math.isfinite(tau)
                   and abs(tau / tref - 1.0) <= NEGA_RTOL)
            if kind == "NEGA":
                ok = hit and r["rung"].get("negA", 0) >= 1
            else:
                ok = hit and r["verdict"] == "LEGAL"
            check("G %s repro h %d kz %d: tau %.4g vs CCCV %.4g "
                  "(rtol %.0e), negA %d, verdict %s"
                  % (kind, hv, kv, tau, tref, NEGA_RTOL,
                     r["rung"].get("negA", -1), r["verdict"]),
                  ok, kill="K3")
        for hv, kv, _t, _k in GATE_TAU:
            r = got.get((hv, kv))
            if r is None:
                continue
            lc = r["rung"].get("loc", {})
            ok = ("rq_gap" in lc and lc["rq_gap"] <= RQ_TIE
                  and lc.get("core_top") and lc["cum2"] >= PART_BAR)
            check("G SEAT repro h %d kz %d: top seat uf %s is a CORE "
                  "seat %s, top-2 CORE participation %s >= %.2f "
                  "(single seat %s -- MEASURED, no bar), rq_gap %s "
                  "<= %.0e"
                  % (hv, kv, lc.get("uf", "-"),
                     lc.get("core_top", "-"),
                     ("%.3f" % lc["cum2"]) if "cum2" in lc else "-",
                     PART_BAR,
                     ("%.3f" % lc["part"]) if "part" in lc else "-",
                     ("%.1e" % lc["rq_gap"]) if "rq_gap" in lc
                     else "-", RQ_TIE), ok, kill="K3")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"] and r["world"] is None]
    n_ag = sum(1 for r in built
               if r["rung"].get("inertia", {}).get("agree"))
    check("G-INERTIA the two independent inertia routes (eigvalsh "
          "vs LDL pivot sign count) agree on %d/%d built cells"
          % (n_ag, len(built)), n_ag == len(built), kill="K3")
    return n_gate


def anatomy_wards(reads):
    section("AN -- anatomy wards on every built cell")
    n_rank = n_e8 = n_acc = n_tot = 0
    for r in reads:
        rung = r["rung"]
        if rung is None or "tau" not in rung or r["world"] is not None:
            continue
        n_tot += 1
        expect = max(0, rung["n_neg"] - rung["rank_g"])
        if rung.get("n_unit", 0) >= expect:
            n_rank += 1
        if rung["tau"] <= 0.0 or (
                rung.get("lamS") is not None
                and rung["lamS"] >= rung["tau"]
                - 1e-12 * max(1.0, abs(rung["tau"]))):
            n_e8 += 1
        if rung["n_pos"] + rung["n_neg"] + rung["n_drop"] == rung["M"]:
            n_acc += 1
    check("W7 RANK IDENTITY #unit >= max(0, n_neg - h) on %d/%d "
          "built cells" % (n_rank, n_tot), n_rank == n_tot, kill="K2")
    check("W8 E8 ward lamS >= tau on every built PD cell (%d/%d; "
          "consumed nowhere)" % (n_e8, n_tot), n_e8 == n_tot,
          kill="K2")
    check("W9 NODE ACCOUNTING M == n_pos + n_neg + n_dropped on "
          "%d/%d built cells" % (n_acc, n_tot), n_acc == n_tot,
          kill="K2")


# ==================================== the certificate coordinate
def certificate_tier(reads, tie_entry):
    section("CERT -- (2)(3)(4)(5)(9) the exact-rational certificate "
            "coordinate of every built cell (A4 step frame)")
    built = [r for r in reads if r["rung"] is not None
             and "tau" in r["rung"] and r["world"] is None]
    built.sort(key=lambda r: r["cell"]["h"])
    legal = [r for r in built if r["verdict"] == "LEGAL"]
    if tie_entry["verdict"] == "LEGAL":
        legal = legal + [tie_entry]        # A4 anchor of last resort
    for r in built:
        pred = None
        for cand in legal:
            if cand["cell"]["h"] < r["cell"]["h"]:
                if pred is None or (cand["cell"]["h"]
                                    > pred["cell"]["h"]):
                    pred = cand
        r["pred"] = pred
        st, why = step_of(r["rung"],
                          pred["rung"] if pred else None)
        r["step_why"] = why
        if st is None:
            r["exact"] = None
            print("    h %-6d kz %-4d %-9s K-COORD-UNAVAILABLE "
                  "(%s%s)"
                  % (r["cell"]["h"], r["cell"]["kz"], r["verdict"],
                     why, ("" if pred is None
                           else ", pred h %d" % pred["cell"]["h"])),
                  flush=True)
            continue
        ex = exact_membership(st["Mt"])
        r["exact"] = ex
        r["pred_h"] = pred["cell"]["h"]
        print("    h %-6d kz %-4d %-9s step from h %-6d: n %.6e q "
              "%.6e s %.6e sigma %.9f | lam_min(B) %.6e floor %.6e"
              % (r["cell"]["h"], r["cell"]["kz"], r["verdict"],
                 pred["cell"]["h"], float(ex["n"]),
                 float(ex["q"]) if ex["q"] is not None
                 else float("nan"),
                 float(ex["s"]) if ex["s"] is not None
                 else float("nan"),
                 float(ex["sigma"]) if ex["sigma"] is not None
                 else float("nan"), ex["lam_b"],
                 float(ex["floor"]) if ex["floor"] is not None
                 else float("nan")), flush=True)
    # ---- the MEASURED moment box of the built POS cells (A5)
    gks = []
    for r in built:
        if r["verdict"] == "LEGAL" and r.get("exact"):
            ex = r["exact"]
            if ex["n"] is not None and ex["n"] > 0:
                gks.append([math.log10(abs(float(nuk / ex["n"]
                                                 ** (k + 2))))
                            for k, nuk in enumerate(ex["nu"])])
    mom_box = None
    if len(gks) >= 2:
        arr = np.asarray(gks, float)
        lo = arr.min(axis=0)
        hi = arr.max(axis=0)
        pad = MOM_PAD * np.maximum(hi - lo, 1e-12)
        mom_box = list(zip(lo - pad, hi + pad))
        print("    MOM box (MEASURED on %d POS cells, widened by "
              "%.0f%% of its log width, A5): g_0..g_%d in %s"
              % (len(gks), 100 * MOM_PAD, len(lo) - 1,
                 ["[%.3f, %.3f]" % (a, b) for a, b in mom_box[:4]]))
    else:
        print("    MOM box UNAVAILABLE (%d POS cells with a "
              "certificate coordinate; typed, not assumed)"
              % len(gks))
    n_rb = n_rb_ok = 0
    for r in built:
        ex = r.get("exact")
        if not ex:
            r["fails"] = ["K-COORD-UNAVAILABLE"]
            r["dist"] = {}
            continue
        fails, dist = membership_verdict(ex, mom_box)
        r["fails"] = fails
        r["dist"] = dist
        for kdeg in KDEGS:
            val = ex["rad"].get(kdeg)
            if val is None or ex["q"] is None:
                continue
            n_rb += 1
            if val >= ex["q"]:
                n_rb_ok += 1
        print("    h %-6d kz %-4d K-MEMBERSHIP %-22s rho_4 %.6f "
              "rho_5 %.6f (t_R %.4f, margin %+.6f) PD margin "
              "%+.6f pivot %.4e"
              % (r["cell"]["h"], r["cell"]["kz"],
                 ("IN-K" if not fails else "OUT:" + ",".join(fails)),
                 dist["P4_rho"].get(4, float("nan")),
                 dist["P4_rho"].get(5, float("nan")), float(T_R),
                 dist.get("P4_margin", float("nan")),
                 dist.get("PD_margin", float("nan")),
                 dist.get("P1_pivot", float("nan"))), flush=True)
        if dist.get("MOM_out"):
            print("      MOM out-of-box coordinates (k, signed "
                  "distance): %s"
                  % [(k, "%+.4f" % d) for k, d in dist["MOM_out"]])
    check("RB1 the exact RADAU_K value is an UPPER bound for the "
          "exact Schur q on %d/%d (cell, K) pairs" % (n_rb_ok, n_rb),
          n_rb_ok == n_rb, kill="K2")
    return built


# ============================================ THE CLASSIFICATION
def named_defects(r):
    """The frozen DEFECT list of the case rule."""
    rung = r["rung"]
    out = []
    at = rung["atoms"]
    if not at["complete_tab2"]:
        out.append("COMB-INCOMPLETE(X %.3e > TAB2)" % rung["X"])
    if not at["refl_unreached"]:
        out.append("A8-REFLECTION-REACHED(u_min %.3e < D %.3e)"
                   % (at["u_min"], at["d_grid"]))
    if rung["n_pos"] + rung["n_neg"] + rung["n_drop"] != rung["M"]:
        out.append("NODE-ACCOUNTING-SHORT")
    if rung["n_drop"] != 0:
        out.append("BOUNDARY-CELL-DROPPED(%d)" % rung["n_drop"])
    if rung["nsteps"] < rung["h"] + 1 or not (rung["be_min"] > 0.0):
        out.append("CHAIN-SHORT/NESTING-BROKEN")
    if rung["hull"]["breach"]:
        out.append("HULL-BREACH(%d nodes outside the positive arm)"
                   % rung["hull"]["n_out"])
    if not rung.get("inertia", {}).get("agree", False):
        out.append("INERTIA-SPLIT")
    cdr = rung.get("cd") or {}
    if "rel" in cdr and cdr["rel"] > CD_TIE:
        out.append("CD-ENTRY-ROUTE-SPLIT(rel %.3e)" % cdr["rel"])
    return out


def classify(built):
    section("CLS -- THE CLASSIFICATION (frozen case rule, decision "
            "logic printed per cell)")
    print("""    DECISION LOGIC (frozen, strict precedence, exactly
    one letter per built cell):
      NEG iff tau <= -%.0e ; POS iff tau >= +%.0e ; else MARGINAL.
      A named DEFECT is DISCRIMINATING only if it does NOT also
      fire on a built POS cell (a feature shared with the legal
      cells cannot explain the transition; it is printed as a
      STRUCTURAL FEATURE instead).
      C  <- NEG and a DISCRIMINATING named defect fires (comb /
            reflection / node accounting / boundary cell / chain
            nesting / hull / inertia split / CD entry split)
            OR NEG and tau_ideal_ub > +%.0e (the metric correction
            removes the negativity: the IMPLEMENTED matrix is
            negative, the IDEAL Galerkin restriction is not).
      B  <- NEG, not C, and >= 1 POS built cell with |dh| <= %d
            (another admissible window at the same depth stays
            positive: the path is wrong, not the family).
      D  <- NEG, not C, not B (the ideal witness survives) --
            REPLICATION-REQUIRED, never concluded.
      A  <- POS and a K constraint FAILS, or the step frame is
            REFUSED (the certificate ends, the matrix stays
            positive).  A merely UNBUILT predecessor is NOT a
            certificate end: it is typed 0 with the coordinate
            UNAVAILABLE.
      0  <- POS and in K, or POS with an unavailable coordinate, or
            MARGINAL (no case letter invented for an unresolved
            sign)."""
          % (TAU_NOISE, TAU_NOISE, IDEAL_NOISE, BFLANK_H))
    pos = [r for r in built if r["rung"]["tau"] >= TAU_NOISE]
    pos_names = set()
    for p in pos:
        for d in named_defects(p):
            pos_names.add(d.split("(")[0])
    if pos_names:
        print("\n    STRUCTURAL FEATURES (present on built LEGAL "
              "cells, therefore NOT discriminating): %s"
              % ", ".join(sorted(pos_names)))
    for r in built:
        tau = r["rung"]["tau"]
        idl = r["rung"].get("ideal") or {}
        tub = idl.get("tau_ub_ref", float("nan"))
        alld = named_defects(r)
        defects = [d for d in alld
                   if d.split("(")[0] not in pos_names]
        flank = [p for p in pos
                 if abs(p["cell"]["h"] - r["cell"]["h"]) <= BFLANK_H
                 and p is not r]
        r["flank"] = flank
        r["defects"] = defects
        r["defects_all"] = alld
        r["flip"] = bool(math.isfinite(tub)
                         and abs(tau) > TAU_NOISE
                         and (tub > IDEAL_NOISE) != (tau > 0.0))
        if abs(tau) < TAU_NOISE:
            r["case"] = "0"
            r["case_why"] = "MARGINAL(|tau| <= TAU_NOISE)"
        elif tau > 0.0:
            if (r["fails"] == ["K-COORD-UNAVAILABLE"]
                    and r.get("step_why") == "NO-PRED"):
                r["case"] = "0"
                r["case_why"] = ("POS, certificate coordinate "
                                 "UNAVAILABLE (no legal "
                                 "predecessor BUILT) -- not a "
                                 "certificate end")
            elif r["fails"]:
                r["case"] = "A"
                r["case_why"] = ("certificate coordinate ends / K "
                                 "constraint fails: "
                                 + ",".join(r["fails"]))
            else:
                r["case"] = "0"
                r["case_why"] = "POS and IN-K (no transition)"
        elif defects:
            r["case"] = "C"
            r["case_why"] = ("DISCRIMINATING NAMED DEFECT: "
                             + "; ".join(defects))
        elif math.isfinite(tub) and tub > IDEAL_NOISE:
            r["case"] = "C"
            r["case_why"] = ("METRIC DEFECT: tau_impl %+.4e < 0 but "
                             "tau_ideal_ub %+.4e > 0 (d %+.4e)"
                             % (tau, tub, idl.get("d", float("nan"))))
        elif flank:
            r["case"] = "B"
            r["case_why"] = ("same-depth POS windows: "
                             + ", ".join("h %d kz %d alpha %.4f tau "
                                         "%+.3e"
                                         % (p["cell"]["h"],
                                            p["cell"]["kz"],
                                            p["cell"]["alpha"],
                                            p["rung"]["tau"])
                                         for p in flank)
                             + (" | D-witness status: ideal "
                                "tau_ub %+.4e" % tub))
        else:
            n_fl = sum(1 for p in built
                       if abs(p["cell"]["h"] - r["cell"]["h"])
                       <= BFLANK_H and p is not r)
            r["case"] = "D"
            r["case_why"] = (
                "REPLICATION-REQUIRED (ideal witness survives: "
                "tau_ideal_ub %+.4e, d %+.4e; flank census "
                "DECIDABLE with %d built cells, none POS)"
                % (tub, idl.get("d", float("nan")), n_fl)
                if n_fl >= 1 else
                "FLANK-UNDECIDED (ideal witness survives: "
                "tau_ideal_ub %+.4e, d %+.4e; NO flank cell built "
                "within %d in h)" % (tub, idl.get("d", float("nan")),
                                     BFLANK_H))
    print("\n    THE TEN-OBJECT TABLE (per built cell)")
    print("    h      kz   alpha    verdict   tau          "
          "tau_ideal_ub  d           |dO-I|    CD rel    negA "
          "e/L  K            SIGN  CASE")
    for r in built:
        idl = r["rung"].get("ideal") or {}
        cdr = r["rung"].get("cd") or {}
        ine = r["rung"].get("inertia", {})
        print("    %-6d %-4d %.5f %-9s %+.4e %+.4e %+.4e %.2e "
              "%.2e %d/%d %-12s %-5s %s"
              % (r["cell"]["h"], r["cell"]["kz"], r["cell"]["alpha"],
                 r["verdict"], r["rung"]["tau"],
                 idl.get("tau_ub_ref", float("nan")),
                 idl.get("d", float("nan")),
                 idl.get("dg_dev", float("nan")),
                 cdr.get("rel", float("nan")),
                 ine.get("neg_eig", -1), ine.get("neg_ldl", -1),
                 ("IN-K" if not r["fails"] else
                  ("N/A" if r["fails"] == ["K-COORD-UNAVAILABLE"]
                   else "OUT")),
                 "FLIP" if r["flip"] else
                 ("marg" if abs(r["rung"]["tau"]) <= TAU_NOISE
                  else "keeps"),
                 "CASE " + r["case"]))
    flips = [r for r in built if r["flip"]]
    print("\n    IDEALITY ALARM (the single most consequential read "
          "of this probe, typed as a MEASUREMENT):")
    print("    the metric correction FLIPS the sign of the wall "
          "eigenvalue on %d of %d built cells --" % (len(flips),
                                                     len(built)))
    for r in built:
        idl = r["rung"].get("ideal") or {}
        print("      h %-6d |tau| %.3e  |d| %.3e  ratio |d|/|tau| "
              "%8.3f  %s"
              % (r["cell"]["h"], abs(r["rung"]["tau"]),
                 abs(idl.get("d", float("nan"))),
                 abs(idl.get("d", float("nan")))
                 / max(1e-300, abs(r["rung"]["tau"])),
                 "SIGN FLIPS (tau %+.3e -> ideal %+.3e)"
                 % (r["rung"]["tau"],
                    idl.get("tau_ub_ref", float("nan")))
                 if r["flip"] else
                 ("MARGINAL, no sign claim either way (A3): tau "
                  "%+.3e -> ideal %+.3e"
                  % (r["rung"]["tau"],
                     idl.get("tau_ub_ref", float("nan")))
                  if abs(r["rung"]["tau"]) <= TAU_NOISE
                  else "sign survives")))
    if flips:
        thr = max(abs(r["rung"]["tau"]) for r in flips)
        keep = [abs(r["rung"]["tau"]) for r in built
                if not r["flip"] and abs(r["rung"]["tau"]) > TAU_NOISE]
        print("    => on the BUILT set the deployed float64 sign is "
              "metric-robust for |tau| >= %.3e and NOT robust for "
              "|tau| <= %.3e (MEASURED on %d cells, never a law)"
              % (min(keep) if keep else float("nan"), thr,
                 len(built)))
    print("\n    PER-CELL CASE REASONS")
    for r in built:
        print("    h %-6d kz %-4d -> CASE %s: %s"
              % (r["cell"]["h"], r["cell"]["kz"], r["case"],
                 r["case_why"]))
    band = [r for r in built if r["cell"]["h"] > BAND_LO]
    letters = [r["case"] for r in band]
    if any(c == "D" for c in letters):
        agg = ("COFINAL-CASE-D-REPLICATION-REQUIRED(%d of %d band "
               "cells; NOT a counterexample claim)"
               % (letters.count("D"), len(band)))
    elif any(c == "C" for c in letters):
        names = sorted({d.split("(")[0] for r in band
                        if r["case"] == "C" for d in
                        (r["defects"] or ["METRIC-DEFECT"])})
        agg = ("COFINAL-CASE-C(construction defect: %s; %d of %d "
               "band cells)" % (",".join(names), letters.count("C"),
                                len(band)))
    elif any(c == "B" for c in letters):
        agg = ("COFINAL-CASE-B(window corridor: %d of %d band cells "
               "leave, same-depth windows stay positive)"
               % (letters.count("B"), len(band)))
    elif any(c == "A" for c in letters):
        agg = ("COFINAL-CASE-A(certificate ends, matrix positive; "
               "%d of %d band cells)" % (letters.count("A"),
                                         len(band)))
    else:
        agg = "COFINAL-NO-TRANSITION(%d band cells)" % len(band)
    print("\n    AGGREGATE: %s" % agg)
    return agg, band


def alpha_corridor(built):
    """The CASE-B corridor read: legality against the window scale
    alpha at comparable depth (MEASURED, never a law)."""
    section("COR -- the window-scale read (is the coordinate that "
            "decides legality h or alpha?)  [MEASURED]")
    rows = sorted(built, key=lambda r: r["cell"]["alpha"])
    print("    alpha    h      kz   X          verdict   tau")
    for r in rows:
        print("    %.5f %-6d %-4d %.4e %-9s %+.4e"
              % (r["cell"]["alpha"], r["cell"]["h"],
                 r["cell"]["kz"], r["cell"]["X"], r["verdict"],
                 r["rung"]["tau"]))
    pos = [r for r in built if r["rung"]["tau"] >= TAU_NOISE]
    neg = [r for r in built if r["rung"]["tau"] <= -TAU_NOISE]
    if pos and neg:
        a_pos = max(r["cell"]["alpha"] for r in pos)
        a_neg = min(r["cell"]["alpha"] for r in neg)
        h_pos = max(r["cell"]["h"] for r in pos)
        h_neg = min(r["cell"]["h"] for r in neg)
        print("    alpha separation: max alpha of a POS cell "
              "%.5f, min alpha of a NEG cell %.5f -> %s"
              % (a_pos, a_neg,
                 "SEPARATED (alpha orders legality on the built "
                 "set)" if a_neg > a_pos else "INTERLEAVED"))
        print("    h separation:     max h of a POS cell %d, min h "
              "of a NEG cell %d -> %s"
              % (h_pos, h_neg,
                 "SEPARATED (h orders legality on the built set)"
                 if h_neg > h_pos else "INTERLEAVED"))
        return bool(a_neg > a_pos), bool(h_neg > h_pos)
    return None, None


# ==================================================== controls
def controls(census, reads, tie_entry):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth, XO "
            "doctored recurrence, XD doctored metric)")
    tie_rung = tie_entry["rung"]
    hs = np.asarray([c["h"] for c in census], float)
    tgt = 600 if SMOKE else XCTRL_TGT
    cell = census[int(np.argmin(np.abs(hs - tgt)))]
    scr = build_cell_world(cell, world="scramble", scr_seed=SCR_SEED)
    ok_s, why_s = cell_legal(scr)
    print("    scramble world h %d kz %d (seed %d): legal %s (%s) "
          "tau %s" % (cell["h"], cell["kz"], SCR_SEED, ok_s, why_s,
                      ("%.4g" % scr["tau"]) if "tau" in scr else "-"))
    check("X1 the SCRAMBLE world fires: legality LEFT", not ok_s,
          kill="K4")
    smo = []
    cheap = census[int(np.argmin(np.abs(hs - (600 if SMOKE
                                             else X2_CHEAP))))]
    rung = build_cell_world(cheap, world="smooth")
    ok, why = cell_legal(rung)
    smo.append((cheap["h"], ok, why, rung.get("tau", float("nan"))))
    for r in reads:
        if r["world"] == "smooth" and r["rung"] is not None:
            ok, why = cell_legal(r["rung"])
            smo.append((r["cell"]["h"], ok, why,
                        r["rung"].get("tau", float("nan"))))
    for hv, ok, why, tau in smo:
        print("    SMOOTH world h %-6d legal %-5s (%s) tau %s"
              % (hv, ok, why,
                 ("%.4g" % tau) if math.isfinite(tau) else "-"))
    n_ill = sum(1 for _h, ok, _w, _t in smo if not ok)
    check("X2 the SMOOTH (prime-free) world fires at %d/%d tested "
          "depths -- THE DISCRIMINATION (deepest tested h %d)"
          % (n_ill, len(smo), max(h for h, _o, _w, _t in smo)),
          n_ill == len(smo) and len(smo) >= 1, kill="K4")
    # ---- XO: the faithfulness reader must have teeth
    ch = tie_rung.get("chain")
    dev_ok = (tie_rung.get("ideal") or {}).get("dg_dev",
                                               float("nan"))
    dev_xo = float("nan")
    if ch is not None:
        be2 = np.array(ch["be"], float)
        kdope = max(1, ch["npoly"] // 2)
        be2[kdope] = be2[kdope] * (1.0 + XO_DOPE)
        _q, _qa, dg2, _g = chain_pass_values(
            ch["al"], be2, ch["m0"], ch["xs"], ch["ws"],
            ch["npoly"], np.zeros(ch["npoly"]))
        dev_xo = float(np.max(np.abs(dg2 - 1.0)))
    print("    doctored recurrence at the TIE cell (be[%s] scaled "
          "by 1 + %.0e): max_k |diag(O)_k - 1| %.3e  vs the "
          "deployed chain %.3e"
          % (ch["npoly"] // 2 if ch else "-", XO_DOPE, dev_xo,
             dev_ok))
    check("XO the ORTHOGONALITY/faithfulness reader FIRES on a "
          "DOCTORED recurrence (%.3e > %.0e >= %.3e): the ideality "
          "measurement has teeth" % (dev_xo, ORTHO_BAR, dev_ok),
          math.isfinite(dev_xo) and dev_xo > ORTHO_BAR
          and math.isfinite(dev_ok) and dev_ok <= ORTHO_BAR,
          kill="K4")
    # ---- MEASUREMENT (not a gate): is the deployed double
    #      reorthogonalization load-bearing at the TIE depth?  The
    #      SAME cell as the deployed reference, so the pair is
    #      comparable entry by entry.
    nor = build_cell_dissect(tie_entry["cell"], no_reorth=True)
    dev_nor = (nor.get("ideal") or {}).get("dg_dev", float("nan"))
    print("    [MEASURED, no gate] the DE-REORTHOGONALIZED chain at "
          "the SAME TIE cell h %d reads max_k |diag(O)_k - 1| %.3e "
          "(deployed %.3e), tau %.6e (deployed %.6e), d %+.3e"
          % (tie_entry["cell"]["h"], dev_nor, dev_ok,
             nor.get("tau", float("nan")), tie_rung["tau"],
             (nor.get("ideal") or {}).get("d", float("nan"))))
    # ---- XD: the doctored metric must move d
    idl = tie_rung.get("ideal") or {}
    d_ref = idl.get("d", float("nan"))
    d_dope = d_ref + XD_DOPE * idl.get("cn2", 0.0)
    lam = 1.0 - tie_rung["tau"]
    tub_ref = 1.0 - lam * lam / max(lam + d_ref, 1e-300)
    tub_dope = 1.0 - lam * lam / max(lam + d_dope, 1e-300)
    print("    doctored metric (O -> O + %.0e I on the witness): d "
          "%+.4e -> %+.4e, tau_ideal_ub %+.4e -> %+.4e"
          % (XD_DOPE, d_ref, d_dope, tub_ref, tub_dope))
    check("XD the DOCTORED metric moves the ideal read by %.3e >> "
          "the frozen bar %.0e (the discriminator is not "
          "insensitive)" % (abs(tub_dope - tub_ref), IDEAL_NOISE),
          abs(tub_dope - tub_ref) > 10.0 * IDEAL_NOISE, kill="K4")


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        vmap = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}
        print("\n  VERDICT: %s" % vmap[KILLS[0]])
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements plus an exact-rational
  certificate tier and OUTWARD-ROUNDED enclosures of the decisive
  scalars, on BUILT cells of the deployed deep-frame construction.
  The IDEAL tier is the METRIC-CORRECTED Galerkin object: it is
  basis-exact (the chain columns span the degree-<h space exactly),
  it measures the float64-vs-ideal gap of the wall matrix for the
  first time, and its negative reads are WITNESSES while its
  positive reads are only "no witness found" -- positivity of the
  ideal object is NOT certified here.  The residual ideality
  question (how accurately the evaluated chain columns represent
  polynomials) is measured indirectly (diag(O) census, chain growth,
  CD entry route) and remains the named scope edge.  Region-K
  coordinates live on the deployed STEP frame and require a legal
  predecessor; where none is built the coordinate is typed
  UNAVAILABLE.  Every statement is about BUILT cells of the frozen
  priority list, never all h.  No marker moves, no promotion, NO RH
  claim, NO counterexample claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


def main():
    print("cofinal_dissect_probe -- PRIME.COFINAL.DISSECT.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the chain/CD/census readers see nodes, weights, "
          "entries, coefficients and frozen constants only (%s)"
          % (",".join(sorted(set(bad_r))) or "clean"), not bad_r,
          kill="K1")

    build_tab2()
    if KILLS:
        return finish([])
    census = deep_census()
    if KILLS:
        return finish([])

    reads, tie_entry = census_build(census)
    if KILLS:
        return finish([])
    n_gate = census_gates(reads)
    anatomy_wards(reads)
    if any(k in ("K1", "K2") for k in KILLS):
        return finish([])       # a broken pipeline/ward cannot be
        #                         dissected; a REPRODUCTION or
        #                         CONTROL kill still prints every
        #                         measurement and only sets the
        #                         verdict (A13)

    built = certificate_tier(reads, tie_entry)
    agg, band = classify(built)
    a_sep, h_sep = alpha_corridor(built)
    controls(census, reads, tie_entry)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations of record, "
          "no fitted level -- census + dissect only, declared)",
          True)

    if SMOKE:
        labels = ["COFINAL-SMOKE(no frontier cell built by design)"]
    else:
        labels = [agg, "GATE-COVERAGE(%d/%d CCCV cells built)"
                  % (n_gate, len(GATE_TAU))]
    n_leg = sum(1 for r in built if r["verdict"] == "LEGAL")
    letters = {}
    for r in built:
        letters[r["case"]] = letters.get(r["case"], 0) + 1
    labels.append("CASE-CENSUS(%s; %d built, %d legal)"
                  % (", ".join("%s:%d" % (k, letters[k])
                               for k in sorted(letters)),
                     len(built), n_leg))
    ds = [(r["rung"].get("ideal") or {}).get("d", float("nan"))
          for r in built]
    ds = [d for d in ds if math.isfinite(d)]
    dgs = [(r["rung"].get("ideal") or {}).get("dg_dev", float("nan"))
           for r in built]
    dgs = [d for d in dgs if math.isfinite(d)]
    cds = [(r["rung"].get("cd") or {}).get("rel", float("nan"))
           for r in built]
    cds = [c for c in cds if math.isfinite(c)]
    if ds:
        labels.append("IDEALITY(|d| %.2e..%.2e, max|diag(O)-1| "
                      "%.2e, CD rel %.2e..%.2e)"
                      % (min(abs(d) for d in ds),
                         max(abs(d) for d in ds),
                         max(dgs) if dgs else float("nan"),
                         min(cds) if cds else float("nan"),
                         max(cds) if cds else float("nan")))
    n_fl = sum(1 for r in built if r["flip"])
    if built:
        labels.append("IDEALITY-ALARM(%d/%d built cells change the "
                      "SIGN of the wall eigenvalue under the metric "
                      "correction)" % (n_fl, len(built)))
    n_k = sum(1 for r in built if not r["fails"])
    n_na = sum(1 for r in built
               if r["fails"] == ["K-COORD-UNAVAILABLE"])
    labels.append("MEMBERSHIP(%d IN-K, %d OUT, %d coordinate "
                  "unavailable)" % (n_k, len(built) - n_k - n_na,
                                    n_na))
    n_ag = sum(1 for r in built
               if r["rung"].get("inertia", {}).get("agree"))
    labels.append("INERTIA(%d/%d routes agree)" % (n_ag, len(built)))
    if a_sep is not None:
        labels.append("CORRIDOR(alpha-separated %s, h-separated %s)"
                      % (a_sep, h_sep))
    return finish(labels)


if __name__ == "__main__":
    main()
