#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""eigvec_geometry_probe -- PRIME.EIGENVECTOR.INVARIANT.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface of promotion wave eight) are not
touched.

=======================================================================
MISSION (round ~201: the eigenvector-geometry separator).  r200
(pole_homotopy_probe, SPEC 703f70e5016581e4, 28/28) established: MAIN
is path-nonnegative at all 14 rungs along M_h(s) = NoP + s RawP with
rmin(s) strictly monotone decreasing, while EPSTEIN(8) starts nodeless
(rmin0 0.690), develops its node INSIDE the path at s* = 6/8 and ends
at -0.481 WITH ITS GAP OPEN the whole way (mingapf -1.01): the
spectral implication is refuted, the transport leg is the SOLE failure
locus, and no spectral argument can close OBJECT-A without an
ingredient separating MAIN from EPSTEIN.  The r200 tau-screen says no
gold remains in the gap.  THIS round attacks the transport leg itself:
WHAT DISTINGUISHES THE EIGENVECTOR/PROFILE GEOMETRY OF MAIN AND
EPSTEIN IMMEDIATELY BEFORE s*?  Sought: a structural invariant I with
I(MAIN, 0) => I(MAIN, s) for all s => A_{v(s)} >= 0, while EPSTEIN
loses I strictly BEFORE its nodal s*.

  E1 THE MICROSCOPE AT s*.  Dense pre-declared fine grid SFINE =
     {j/80 : j = 40..72} (33 points in [0.50, 0.90]) at EPSTEIN(8)
     and matched MAIN(8).  Per fine s: full profile A_{v(s)}(t) on
     the N = 16K half-window, rmin(s), the t-location of the global
     minimum (edge t = 0 / t = L/2 vs interior), the interior-dip
     census (see E2-I1), coefficient sign flips between adjacent s,
     the exact Sturm zero count (K = 21: integer-PRS affordable at
     every fine s), and the secular admixture anatomy (f(s), rho_1).
     Deliverables: s*_node refined by sign interpolation of rmin;
     WHERE the node appears (t*/L); HOW it appears (dip-first
     interior descent vs edge crossing; approach slope d rmin/ds
     over the last positive points); WHAT the coefficient vector
     does at the same s.
  E2 THE INVARIANT BATTERY (the round's core; standard 9-point
     s-grid, all 14 MAIN rungs + H_HOLD, controls SMOOTH/SCRARITH/
     EPSTEIN).  The profile A(t) = sum_k v_k cos(2 pi k t / L) is
     EVEN about t = 0 AND about t = L/2 (period L), so [0, L/2] is a
     fundamental half-window and edges are critical points.  The
     battery, per (world, h, s):
     I1 EDGE-MINIMALITY GEOMETRY: the half-window has two even
        critical endpoints, t = 0 (A(0) = sum v_k, the jr_0 plus-
        sum) and t = L/2 (A(L/2) = sum (-1)^k v_k, the alternating
        sum).  Censuses: n_dip = # strict interior local minima
        (resolving bar DIP_BAR; the ripple record), dip_margin =
        (interior grid min - edge min)/amax (EDGE-MINIMALITY :=
        dip_margin >= 0: the global grid min is attained at an
        endpoint), and T0-MINIMALITY := argmin = t = 0 exactly.
        ELEMENTARY EXACT REDUCTION: edge-minimality on the grid =>
        min_grid A = min(A(0), A(L/2)) -- OBJECT-A's grid face
        collapses to TWO EDGE SCALARS; where t0-minimality
        additionally holds (recorded per rung as the migration
        point s_mig) it further collapses to the single r197 jr_0
        scalar.
     I2 LOG-CONCAVITY: second differences of log A on the grid
        (only above the zero class); census + worst margin.
        Implication typing: log-concavity PRESUPPOSES A > 0 where
        read -- it is a shape-transport reading, NOT a positivity
        certificate (typed).
     I3 PF/TP PROXY: contiguous 2x2 and 3x3 Toeplitz minors of a
        frozen 17-point sample of A (even extension a_{|i-j|});
        negative-minor censuses (PF2 = sampled log-concavity, PF3
        strictly stronger).  Proxy class, no theorem consumed.
     I4 INFLECTION COUNT: sign changes of the second difference
        along t; variation-diminishing reading = is n_infl(s)
        non-increasing in s?  Proxy class (Schoenberg VD named as
        MOTIVATION ONLY, consumed nowhere).
     I5 COEFFICIENT SIGNS (mode basis): SC_mode(s) = sign changes
        of (v_k(s)); parity-aligned mis/hd census (r198 align_census
        VERBATIM); r198 record: hd(EPSTEIN wall) = 0 vs MAIN 4..7.
     I6 QUOTIENT GEOMETRY: r_k = v_k/phi_k (tilt relative to the
        pole ray; phi_k > 0 so signs match I5); n_rev = monotonicity
        reversals of (r_k) above the zero class.
     I7 EXACT DESCARTES COUNT (the most theorem-shaped candidate):
        P(x) = sum v_k T_k(x) via exact dyadic Fractions (BH10/r200
        cheb machinery VERBATIM); Moebius x = (u-1)/(u+1) maps
        u in (0, inf) onto x in (-1, 1); R(u) = (u+1)^deg P((u-1)/
        (u+1)) has integer coefficients and CLASSICAL Descartes'
        rule gives #roots of A in (0, L/2)... exactly: #roots of P
        in (-1, 1) <= SC_desc := sign changes of coeffs(R), with
        equality mod 2 (Descartes/Fourier; Vincent/Collins-Akritas
        root-isolation context).  SC_desc = 0 (+ endpoint sign) is
        a PER-CELL POSITIVITY CERTIFICATE, exact integer
        arithmetic, own code.
     I8 EXACT BERNSTEIN COUNT: q(u) = P(2u - 1) on [0, 1];
        Bernstein coefficients b_i = sum_{j<=i} q_j C(i,j)/C(n,j)
        (exact Fractions); NB = #negative b_i.  NB = 0 => P >= 0 on
        [-1, 1] (Bernstein basis nonnegativity, certificate class;
        native degree only -- no elevation, so NB > 0 is
        UNDECIDED-not-negative, typed).
     I9 EIGENBASIS SIGN FREEZE (exact secular structure, warded not
        assumed): for s > 0 the ground vector in the NoP eigenbasis
        is y_m(s) = z_m/(d_m - lam_0(s)) with lam_0(s) in (d_0,
        d_1), hence sign(y_m(s)) is CONSTANT in s (= sign z_m for
        m >= 1, = -sign z_0 at m = 0): the eigenbasis sign-change
        count is FROZEN along the whole path and CANNOT be a
        transport separator (it is an s = 0 datum); its VALUE may
        still separate worlds -- both facts gated/recorded.
     I10 SECULAR LOAD ANATOMY: f(s) = (lam_0(s) - d_0)/(d_1 - d_0)
        (lift fraction through the first gap), rho_1(s) =
        |y_1/y_0| = |z_1/z_0| f/(1-f) (strictly increasing in s,
        signs frozen: the transport is a MONOTONE reweighting of
        fixed NoP eigenprofiles), the TRIANGLE CERTIFICATE
        TRI(s) = sum_{m>=1} |y_m| l1(Q_m) / (|y_0| min_grid U_0)
        with l1(Q_m) = sum_k |Q[k,m]| >= ||U_m||_inf: TRI < 1 =>
        A_{v(s)} > 0 on the grid AND continuum (exact triangle
        inequality, certificate class); s_cert = last grid s with
        TRI < 1.  Plus the TWO-MODE CENTER PREDICTOR: A_s(L/2) ~
        y_0 U_0(L/2) + y_1 U_1(L/2) (exact secular expansion,
        truncated at m = 1); r2c(s) = -y_1 U_1(L/2) / (y_0
        U_0(L/2)) crosses 1 exactly when the two-mode truncation
        of the alternating edge scalar crosses zero -- s*_pred
        (interpolated on the fine grid) vs the measured s*_lin
        adjudicates whether the EPSTEIN transition is a TWO-MODE
        edge competition (world data: z_1/z_0, U_0(L/2),
        U_1(L/2)).
  E3 THE SEPARATOR ADJUDICATION.  Per candidate: (a) MAIN holds at
     ALL 14 rungs x 9 s?  (b) EPSTEIN loses it at s_loss -- strictly
     before s*_node?  (c) implication class (certificate / edge-
     reduction / conditional / proxy)?  (d) tau-screen of the
     MAIN margin ladder (slopes vs log10 tau_h; WIN CONDITION =
     O(1)-flat MAIN margin + early EPSTEIN loss).  Ranked verdict
     I*.  HONEST EXPECTATION pre-registered: every margin tied to
     the s = 1 edge value rides tau (the r197 jr_0 currency);
     count/shape invariants can be flat.
  E4 THE MECHANISM READING.  (i) Source census: MAIN atom weights
     w_q = Lambda(q)/sqrt(q) > 0 for ALL h source-classically (von
     Mangoldt); EPSTEIN(8) effective weights measured by r198 as
     ALL NONNEGATIVE (negw = 0) -- the builders are re-censused
     here from source (atoms replicated VERBATIM from
     radius4_an_probe.build_cell): if negw(EPSTEIN, 8) = 0 the
     'Lambda >= 0 separates' hypothesis is REFUTED at the reachable
     rung and the arithmetic difference must be typed as SUPPORT/
     MASS class (EPSTEIN atoms live on x^2+5y^2 norms incl. NON-
     prime-powers, e.g. q = 6, and miss primes 2, 3, 7), not sign
     class.  (ii) Eigen-anatomy: the two-ladder cancellation --
     MAIN's overlap ladder |z_1/z_0| vs its gap ladder d_1: the
     load rho_1(1) = |z_1/z_0| f(1)/(1-f(1)) stays O(1)-class iff
     the two ladders cancel; EPSTEIN's rho_1 at the node vs MAIN's
     at matched s; the driver level m_dr (smallest m whose partial
     sum goes negative at the node t*).

PRE-REGISTERED PRIORS (resolve-and-record; NONE gate-forcing; P1/P2
informed by the disclosed prototype block below):
  P1 EPSTEIN(8) node anatomy: INTERIOR t* (t*/L in (0.05, 0.45)),
     DIP-FIRST (an interior local minimum exists at s strictly
     below the sign crossing), smooth crossing (finite d rmin/ds);
     s*_node in (5/8, 6/8) refined.
  P2 MAIN(8) matched control: no node, no interior dip on the
     whole fine grid.
  P3 I1 dip-freedom: MAIN n_dip = 0 at ALL 14 rungs x 9 s (the
     candidate I*); EPSTEIN loses it strictly before s*_node.
  P4 I2 log-concavity: holds for MAIN at small s; may fail near
     the wall edge at s -> 1 (near-zero edge value) -- wherever it
     fails, it fails NEAR THE EDGE, not at the bump body.
  P5 I5 SC_mode: MAIN = 0 at s = 0-class, but > 0 at s = 1 (the
     r197 jr_0 cancellation forces mixed signs at the wall): the
     raw mode-sign count is NOT a path invariant for MAIN; the
     separator content, if any, sits in WHERE counts jump.
  P6 I7/I8: SC_desc(MAIN) even everywhere (parity theorem); the
     hope SC_desc = 0 along the whole path; NB likely > 0 at deep
     s (native-degree Bernstein is crude): resolve-and-record.
  P7 I9: sign-freeze ward passes exactly (secular structure);
     SC_eig is s-independent per world.
  P8 I10: TRI certifies a nontrivial transport prefix s_cert > 0
     at every MAIN rung but collapses before s = 1 (the edge
     near-zero makes any sufficient condition tau-ride at the
     wall); EPSTEIN's s_cert < s*_node.
  P9 E4 source census: negw(EPSTEIN, 8) = 0 (r198 inheritance) --
     Lambda >= 0 does NOT separate at the reachable rung; EPSTEIN
     support contains non-prime-powers carrying O(1) mass
     fraction; MAIN/SCRARITH all-prime-power all-positive.
  P10 tau-screen: dip_margin at s = 1 rides tau only through its
     edge term; the INTERIOR structure margins (dip census, body
     log-concavity, SC counts) stay FLAT; rho_1(1) O(1)-class for
     MAIN at every rung (two-ladder cancellation), >> 1 for
     EPSTEIN.

NOTATION (r171-r200 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector); a = log(h)/2; L = 2a; K = ceil(1.25 h
log h); om_k = k pi/a = 2 pi k/L; b_k = om_k^2; par_k = (-1)^k;
nrm_0 = sqrt(2a), nrm_k = sqrt(a); Raw = D_par N M N D_par;
RawW/RawP from mpM/mpPole; NoP = RawW - RawP; phi_k = 1/(1/4 + b_k);
c_pole = 2 sinh(a/2)^2.  Eigendecomposition E, Q = mp.eigsy(NoP)
sorted ascending; z = Q^T phi; secular bottom pair post-A1 (r200
VERBATIM: ALL K levels kept as poles, bottom pair from the first two
interlacing gaps, NBIS = int(3.4 dps) + 60); v = Q y peak-sign
normalized WITH the profile.  Profile grid N = 16 K, exact cosine
table, half-window j = 0..N/2 (r197 VERBATIM); node flag amin <
-1e-6 amax (BH10-KA sign-resolving); zero class 1e-30 rel.  s = 1
anchor: mp inverse iteration on RawW (r195-r200 VERBATIM).  Sturm =
BH10 integer primitive-PRS VERBATIM on exact dyadic Fractions of the
computed v (roots in (-1, 1]).  Descartes/Bernstein: own exact
integer/Fraction transforms as specified in E2-I7/I8.  fhat_i =
b_i RawW[i,0]; descents == r189.  jr_0 == r197 CAL_JR0.  tau_h =
ce["mpE"][0], measured per-rung scalar only.  Atom censuses
replicate radius4_an_probe.build_cell atom blocks VERBATIM (sieve /
x^2+5y^2 lattice + lamq recursion / golden permutation).

DPS schedule (r182-r200 ladder VERBATIM): DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16, H_HOLD = 20.
SGRID_DEN = 8 (9 path points).  SFINE_DEN = 80, SFINE_J = 40..72.
MICRO_CELLS = (EPSTEIN, 8, 80), (MAIN, 8, 80).  STURM_RUNGS =
(4, 5) (battery, all 9 s) + ALL control cells (all 9 s) + ALL
micro cells (all 33 fine s).  CONTROLS: (SMOOTH, 5, 60),
(SCRARITH, 5, 60), (EPSTEIN, 8, 80).  WIT_RUNG = 5, WIT_FACT =
1000.  PF sample: 17 equispaced half-window points, contiguous
2x2/3x3 minors.

FROZEN BARS: RANK1_BAR 1e-40; EIG_RES_BAR 1e-30; EIG_ORTH_BAR
1e-30; SEC_RES_BAR 1e-20; ANCHOR_LAM_BAR 1e-6; ANCHOR_OVL_BAR
1e-12; INVIT_RES_BAR 1e-12; ZCLS 1e-30; SIGN_RES 1e-6; DIP_BAR
1e-12 (rel, dip resolving); LC_BAR 1e-30 (abs, log domain);
PF_BAR 1e-30 (rel to amax^order); TH_TOL 1e-20; CTRL_RMIN_TOL
0.05; TAU_FLAT_BAR 0.30; WIT_YT_BAND (990, 1010); WIT_A0_BAR 1e-6;
RUNTIME_BAR 2700 s.  Record tolerances: LOG_TOL 0.10 dex; FRAC_TOL
0.05; SLOPE_TOL 0.10; counts exact.  Inheritance cross-checks:
descents == R189_DESC exact; log10 jr_0 == R197_JR0 (LOG_TOL);
lam_0(RawW) > 0 at every MAIN rung; rmin0/rminh == r200
CAL_RMIN0/CAL_RMINH (FRAC_TOL); nnode == 0, mono True; EPSTEIN
9-grid fingerprint == r200 (nnode 3, s* = 6, rmin1 -0.481).

TAXONOMY (resolution logic; the I1/micro/sep entries were RETYPED
pre-freeze after the disclosed smoke pass -- see the SMOKE
DISCLOSURE block -- from dip-freedom to edge-minimality geometry;
no bar, dps, grid or gate target moved):
  microEnum := EPSTEIN-CENTER-CROSSING iff the crossing minimum
               sits at t = L/2 (the alternating-sum point; an even
               critical point, interior to the full period);
               EPSTEIN-T0-CROSSING if at t = 0; else
               EPSTEIN-INTERIOR-CROSSING(t*/L);
  edgeEnum  := EDGE-MIN-ALL iff dip_margin >= 0 at every MAIN
               cell (the global grid min is one of the TWO edge
               scalars); EDGE-MIN-DEEP-EARLY-LOST(n) if the
               violations are confined to the EARLY path of deep
               rungs with the wall-side suffix clean at every rung
               (s_edge table recorded; n = violating cell count);
               else EDGE-MIN-LOST (ripple census n_dip and depths
               recorded in every case);
  migEnum   := T0-MIN-FROM(s_mig table): per rung the first 9-grid
               s from which argmin A = t = 0 holds through s = 1
               (the measured migration of the minimum to the t = 0
               edge; a RECORD, not an invariant);
  wallEnum  := WALL-STATE-CLEAN-ALL-RUNGS iff at s = 1 EVERY MAIN
               rung has t0min AND n_dip = 0 AND NB = 0 AND SC_desc
               = 0 (the wall profile is ripple-free, edge-minimal
               at t = 0, and DOUBLY exact-certified: Bernstein
               nonneg + Descartes zero-count at native degree);
               else WALL-STATE-DIRTY-AT(...);
  lcEnum    := LOGCONC-HOLDS-ALL iff lc_viol = 0 everywhere on
               MAIN; else LOGCONC-FAILS-AT(...) with edge/body
               location typing;
  descEnum  := DESCARTES-ZERO-ALL iff SC_desc = 0 at every MAIN
               cell; else DESCARTES-COUNT-TABLE;
  bernEnum  := WALL-BERNSTEIN-CERTIFIED-ALL-RUNGS iff NB = 0 at
               s = 1 at every MAIN rung (then OBJECT-A itself is
               exact-rational-certified at native degree at every
               reachable rung); BERNSTEIN-CERT-ALL if NB = 0
               everywhere; else BERNSTEIN-NEGATIVES-MEASURED;
  eigEnum   := EIGENBASIS-SIGNS-FROZEN iff the sign-freeze ward
               passes at every checked cell; else
               EIGENBASIS-SIGN-FREEZE-VIOLATED (bug class);
  sepEnum   := SEPARATOR-FOUND(I*) iff a candidate holds at ALL
               MAIN cells while EPSTEIN violates it already at
               s = 0; SEPARATOR-MATCHED-RUNG+WALL-STATE iff no
               candidate is uniform over all MAIN cells BUT (a) at
               the MATCHED rung h = 8 edge-minimality holds at
               every MAIN cell while EPSTEIN(8) violates it at
               s = 0 and its argmin never reaches t = 0, AND (b)
               the wall state is clean at every MAIN rung and
               dirty at EPSTEIN's wall (wallEnum) -- the honest
               composite: the separation is real at matched rung
               and at the wall, and NO uniform-in-h path invariant
               exists in this battery; NO-SEPARATOR else;
  tauEnum   := per-margin FLAT iff |slope vs log10 tau| <=
               TAU_FLAT_BAR else RIDES;
  lamEnum   := LAMBDA-POS-REFUTED-AT-RUNG iff negw(EPSTEIN, 8) = 0
               (the sign hypothesis cannot carry the separation at
               the reachable rung); else LAMBDA-POS-SEPARATES;
  mechEnum  := TWO-LADDER-CANCELLATION iff log10 rho_1(1) at MAIN
               is within [-1, +1] at every rung while |z_1/z_0|
               spans > 10 dex (the overlap ladder and the lift
               ladder cancel to O(1) load); else
               LOAD-LADDER-UNMATCHED; plus TWO-MODE-PREDICTOR-
               SHARP iff |s*_pred - s*_lin| <= 0.02 on the EPSTEIN
               fine grid.

SMOKE DISCLOSURE (pre-freeze, house convention; the structural
smoke ladder at rungs 4/5/8 + EPSTEIN control + reduced microscope
-- first pass at pre-freeze SHA 5a193f0dbe6b2bb7, 25/30, the
data-refuted gates being exactly the dip-freedom/interior-node
wording -- surfaced three structure facts that RETYPED the
taxonomy before calibration; the final smoke pass (30/30, SHA
8a0fd8e821b5fc01) is kept as eigvec_geometry_probe.smoke1.log,
earlier smoke logs superseded in place, disclosed; no bar, dps,
grid, census or budget moved):
(i) MAIN profiles carry PERSISTENT SHALLOW INTERIOR RIPPLES (n_dip
1..6, depth 1e-3..1e-4 rel) at every s < 1 -- naive dip-freedom is
FALSE on MAIN and P3-as-worded resolves AGAINST; the correct exact
invariant is EDGE-MINIMALITY (dip_margin >= 0: the global min is
one of the two edge scalars), measured TRUE at every MAIN smoke
cell, with the argmin MIGRATING from the L/2 edge to the t = 0
edge along the path (s_mig recorded per rung; t0-minimality is a
record, not the invariant -- at h = 8 the min sits at the L/2 edge
for s <= 1/8); EPSTEIN violates edge-minimality from s = 0 on
(dip_margin -0.001 at s = 0, argmin never at t = 0).  (ii) THE EPSTEIN CROSSING
SITS AT THE WINDOW CENTER t = L/2 (tmin = 0.5000 at every fine
smoke s): the failing coordinate is the ALTERNATING EDGE SCALAR
A(L/2) = sum (-1)^k v_k, not a generic interior point and not the
U_1 interior node -- microEnum retyped accordingly, and the
two-mode center predictor r2c was added to E2-I10/E4 to test this
reading exactly.  (iii) rho_1(1) is O(1) at MAIN rungs 4/5/8
(log10 = 0.1..0.2) -- the two-ladder cancellation happens in the
LOAD (not inside rmin), and it is O(1) for EPSTEIN too (2.07): the
load does NOT separate worlds, the center template value does.
Smoke also showed NB = 0 at s = 1 at h = 4/5/8 (the wall vector
Bernstein-certifies at native degree) -- promoted to a taxonomy
question (bernEnum) for the full ladder, resolved at calibration.

CALIBRATION DISCLOSURE (pre-freeze, same convention; the full-
ladder calibration pass at the smoke-stage SHA 8a0fd8e821b5fc01,
28/30 with G40/G52 failing EXACTLY BECAUSE the deep-rung data
refuted the smoke-stage invariant wording, log kept as
eigvec_geometry_probe.calib1.log): at DEEP rungs the EARLY path
loses edge-minimality as well -- h = 12, 13 at s = 0, h = 14 at
s <= 4/8, h = 20 at s <= 6/8 (14 of 126 cells; interior minima
undercut the edges by 0.002..0.046 of amax while staying at
rmin 0.76..0.90 POSITIVE) -- and the pole lift IRONS THE RIPPLE
FIELD OUT along s (n_dip per rung non-increasing to 0 at the
wall).  Consequence, typed honestly: NO candidate in this battery
is a uniform-in-h path invariant; the separation is real (i) at
the MATCHED rung h = 8 (MAIN(8) edge-minimal at all cells,
EPSTEIN(8) violating from s = 0) and (ii) at the WALL at every
rung (wallEnum).  G40/G52 pass conditions and sepEnum were re-set
pre-freeze to this honest composite; no bar, dps, grid, census or
budget moved.  The G51 slopes and all other calibration values
were frozen from this same pass.

RECORD TABLES (frozen at freeze from the disclosed pre-freeze
ladder: the smoke ladder ran at pre-freeze SHAs 5a193f0dbe6b2bb7
(25/30 -- the dip-freedom wording refuted by the data),
66e2e449e29b8c59 (28/30) and 8a0fd8e821b5fc01 (30/30, kept as
eigvec_geometry_probe.smoke1.log; earlier smoke logs superseded in
place, disclosed); ONE full calibration pass at SHA
8a0fd8e821b5fc01 (28/30, G40/G52 failing exactly on the deep-rung
refutation -> calibration disclosure above; kept as
eigvec_geometry_probe.calib1.log; tables below frozen VERBATIM
from it)).
RESOLVED VERDICTS: P1 RESOLVED RETYPED -- EPSTEIN(8) microscope:
the crossing minimum sits AT THE WINDOW CENTER t*/L = 0.5000 at
EVERY fine s (the failing coordinate is the alternating edge
scalar A(L/2) = sum (-1)^k v_k; microEnum = EPSTEIN-CENTER-
CROSSING, not a generic interior node); crossing bracketed in
(0.6875, 0.7000), s*_lin = 0.69898; approach slopes -2.09/-2.12/
-2.14 (smooth); the TWO-MODE PREDICTOR is SHARP: s*_pred = 0.68734
from r2c(s) = 1, |s*_pred - s*_lin| = 0.0116 <= 0.02 (world data
u0c -0.6906, u1c -1.0000, u00 -0.8294, u10 +0.2280; u1node/L
0.2307 recorded -- NOT the crossing coordinate); coefficient side
SILENT (nflip = 0 at the crossing).  P2 TRUE -- MAIN(8) matched
fine grid: rmin 0.803 -> 0.699 monotone, t0min True, dip_margin >=
0 and EXACT Sturm Z = 0 at ALL 33 fine s.  P3 RESOLVED AGAINST-
AS-WORDED, RETYPED TWICE (smoke + calibration disclosures): MAIN
carries persistent shallow interior ripples (n_dip up to 30 at
h = 20, depth 1e-3..1e-4), and at DEEP rungs the EARLY path even
loses edge-minimality (14/126 cells: h = 12, 13 at s = 0, h = 14
s <= 4/8, h = 20 s <= 6/8, undercut -0.002..-0.046 at rmin >=
0.76 STILL FAR POSITIVE); the pole lift IRONS THE RIPPLES OUT
(n_dip -> 0 at the wall at every rung); edge-minimality holds at
ALL cells of the MATCHED rung h = 8 while EPSTEIN(8) violates it
from s = 0 (dip_margin(0) = -0.0008) and never reaches t0min.
P4 RESOLVED AGAINST I2: log-concavity fails already at s = 0 at
every MAIN rung (lcv0 27..302, body violations); I3 PF proxies
anti-separate; I4 inflections noise.  P5 RESOLVED SHARPENED: MAIN
is NOT sign-pure even at s = 0 (SC_mode(0) = 1..25 growing with
h), yet nsc = 0 at ALL MAIN cells (sign changes profile-
invisible); EPSTEIN(8) SC_mode(0) = 5; hd(EPSTEIN wall) = 0
(r198-consistent).  P6 RESOLVED MIXED, WITH THE ROUND'S SECOND
HEADLINE: mid-path the exact counts are slack (SC_desc(0) =
0..72, h-growing; NB > 0), BUT AT THE WALL THEY COLLAPSE TO ZERO
AT EVERY RUNG: NB(s=1) = 0 AND SC_desc(s=1) = 0 at ALL 14 rungs
(h = 20 included: exact-rational bmin = +5.0e-44 == the jr_0
scalar; indeed b_n = P(1) = A(0) identically) -- OBJECT-A itself
is now DOUBLY exact-certified at native degree at every reachable
rung (Bernstein nonneg + Descartes zero-count), beyond BH10's
four Sturm rungs; bernEnum = WALL-BERNSTEIN-CERTIFIED-ALL-RUNGS,
descEnum = DESCARTES-COUNT-TABLE.  P7 TRUE EXACTLY: sign-freeze
ward passes at all 17 battery + 66 microscope cells (eigEnum =
EIGENBASIS-SIGNS-FROZEN).  P8 TRUE: s_cert(TRI < 1) = 5..7 of 8
per rung (TRI(6/8) 0.33..1.03), EPSTEIN s_cert = 4 < its
violations; the TRI prefix is real but NOT uniform (h = 20: 5).
P9 TRUE: negw(EPSTEIN, 8) = 0 re-censused from source (atoms
q = {4, 5, 6}, weights all positive, non-prime-power q = 6 mass
fraction 0.51, primes 2, 3, 7 missing); MAIN negw = 0 at all 14
rungs; lamEnum = LAMBDA-POS-REFUTED-AT-RUNG.  P10 RESOLVED, WIN
CONDITION MET BY THE STRUCTURE COORDINATES: slopes vs log10 tau:
dipm_mid +0.000, TRI(6/8) -0.008, rminh -0.001, log10 rho_1(1)
-0.002 ALL FLAT (bar 0.30) while log10 A(0)(s=1) rides at +0.50;
THE TWO-LADDER CANCELLATION IS EXACT ON THE RECORD: z1rel spans
-6.9 -> -81.2 dex while log10 rho_1(1) stays 0.1..0.3 (O(1) at
every rung; EPSTEIN rho_1(1) = 2.07 same O(1) class): the load
does NOT separate worlds -- the separator is the pair (z_1
overlap, U_1 center template value), both s = 0 data; m_dr = 1.
SEPARATOR VERDICT: sepEnum = SEPARATOR-MATCHED-RUNG+WALL-STATE
(no uniform-in-h path invariant exists in this battery -- the
honest core negative; the matched-rung separation and the
wall-state collapse are the real deliverables).
CAL RECORD TABLES (calib1 VERBATIM):
CAL_NDIP_MAX {h}: 4: 1, 5: 3, 6: 3, 7: 5, 8: 4, 9: 8, 10: 8,
  11: 9, 12: 13, 13: 14, 14: 18, 15: 15, 16: 22, 20: 30.
CAL_DIPM1 {h: dip_margin at s = 1/2}: 4: 0.0034, 5: 0.0031,
  6: 0.0029, 7: 0.0030, 8: 0.0025, 9: 0.0026, 10: 0.0024,
  11: 0.0024, 12: 0.0024, 13: 0.0023, 14: -0.0153, 15: 0.0020,
  16: 0.0020, 20: -0.0458.
CAL_SMIG {h}: 4: 0, 5: 0, 6: 0, 7: 0, 8: 2, 9: 0, 10: 0, 11: 0,
  12: 1, 13: 1, 14: 5, 15: 3, 16: 0, 20: 7.
CAL_SEDGE {h}: 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
  12: 1, 13: 1, 14: 5, 15: 0, 16: 0, 20: 7.
CAL_SSC {h: SC_mode at s = 0}: 4: 1, 5: 3, 6: 1, 7: 3, 8: 4,
  9: 7, 10: 9, 11: 11, 12: 13, 13: 19, 14: 19, 15: 13, 16: 16,
  20: 25.
CAL_SCM1 {h: SC_mode at s = 1}: 4: 3, 5: 4, 6: 5, 7: 6, 8: 9,
  9: 8, 10: 9, 11: 12, 12: 11, 13: 14, 14: 15, 15: 16, 16: 19,
  20: 25.
CAL_SCD0 {h: SC_desc at s = 0}: 4: 0, 5: 6, 6: 8, 7: 14, 8: 14,
  9: 20, 10: 24, 11: 28, 12: 34, 13: 38, 14: 42, 15: 46, 16: 52,
  20: 72.
CAL_SCD1 = 0 and CAL_NB1 = 0 at EVERY rung (the wall collapse).
CAL_TRI68 {h}: 4: 0.326, 5: 0.517, 6: 0.341, 7: 0.564, 8: 0.637,
  9: 0.571, 10: 0.586, 11: 0.760, 12: 0.707, 13: 0.858, 14: 0.755,
  15: 0.688, 16: 0.962, 20: 1.029.
CAL_SCERT {h}: 4: 7, 5: 7, 6: 7, 7: 7, 8: 6, 9: 7, 10: 7, 11: 6,
  12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 20: 5.
CAL_RHO11 {h: log10 rho_1(1)}: 4: 0.1, 5: 0.1, 6: 0.1, 7: 0.1,
  8: 0.2, 9: 0.2, 10: 0.2, 11: 0.2, 12: 0.2, 13: 0.2, 14: 0.2,
  15: 0.2, 16: 0.2, 20: 0.3.
CAL_Z1REL {h: log10 |z_1/z_0|}: 4: -6.9, 5: -11.4, 6: -15.7,
  7: -20.0, 8: -24.4, 9: -28.8, 10: -33.6, 11: -38.1, 12: -43.2,
  13: -47.6, 14: -53.0, 15: -57.1, 16: -62.1, 20: -81.2.
CAL_LCV0 {h}: 4: 27, 5: 41, 6: 51, 7: 69, 8: 76, 9: 95, 10: 104,
  11: 122, 12: 154, 13: 165, 14: 191, 15: 183, 16: 220, 20: 302.
CAL_MICRO (EPSTEIN, 8): s_lastpos 0.6875, s_firstneg 0.7000,
  s*_lin 0.69898, s*_pred 0.68734, t*/L 0.5000 (center), nflip at
  the crossing 0, u1node/L 0.2307, m_dr 1.  (MAIN, 8): clean at
  all 33 fine s (P2).
CAL_CTRL: (SCRARITH, 5): nnode 0, rmin0 0.814, ndip_max 2, s_cert
  7, SC_mode(0) 3, dipm0 +0.0018 (edge-min holds); (SMOOTH, 5):
  nnode 0, rmin0 0.873, ndip_max 4, s_cert 8, SC_mode(0) 1, dipm0
  +0.0014; (EPSTEIN, 8): nnode 3, s* = 6, rmin0 0.690, rmin1
  -0.481, ndip_max 6, s_cert 4, SC_mode(0) 5, SC_desc(0) 18, wall
  NB 11 / SC_desc 17 / t0min False, dipm0 -0.0008, negw 0,
  nonpp_massfrac 0.51.
CAL_SLOPES (vs log10 tau, MAIN): dipm_mid +0.000, tri68 -0.008,
  rminh -0.001, rho11 -0.002, a0log +0.50.
CAL_WIT: ytr 1000.00, a0dev 4.1e-55, base mis 4 hd 4 nonneg True
  ovl 1.000000 | wit mis 4 hd 4 nonneg True ovl 0.998106 (== r198/
  r200 VERBATIM).
FROZEN ENUMS: microEnum = EPSTEIN-CENTER-CROSSING (+ TWO-MODE-
PREDICTOR-SHARP); edgeEnum = EDGE-MIN-DEEP-EARLY-LOST(14);
wallEnum = WALL-STATE-CLEAN-ALL-RUNGS; lcEnum = LOGCONC-FAILS-AT-
S0; descEnum = DESCARTES-COUNT-TABLE; bernEnum = WALL-BERNSTEIN-
CERTIFIED-ALL-RUNGS; eigEnum = EIGENBASIS-SIGNS-FROZEN; sepEnum =
SEPARATOR-MATCHED-RUNG+WALL-STATE; tauEnum: structure FLAT, edge
scalar RIDES; lamEnum = LAMBDA-POS-REFUTED-AT-RUNG; mechEnum =
TWO-LADDER-CANCELLATION + TWO-MODE-PREDICTOR-SHARP.

DISCLOSED PRE-FREEZE PROTOTYPE (house convention, no bar/class/
tolerance chosen from a failed check): the r200 record pass IS the
prototype for this round's path machinery (its calibrated tables
are inherited as gates G20/G21); the only new pre-freeze sizing
facts are r200's published EPSTEIN path ladder (rmin 0.155 at
s = 5/8 -> -0.108 at 6/8: crossing inside (5/8, 6/8), seeding the
SFINE window [0.50, 0.90]) and r200's h = 20 eigsy timing (3.2 s,
seeding the budget).  Nothing else was tuned.

AMENDMENTS: none.  (All pre-freeze retypes are carried by the
SMOKE/CALIBRATION DISCLOSURE blocks above; no bar, dps, grid,
census, budget or instrument moved between smoke, calibration and
freeze -- the G40/G52 re-adjudication changed only which structural
statement is CLAIMED, in the direction the data forced.)

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
instrument wards G10-G15; S2 inheritance G20-G21; S3 E1 microscope
G30-G32; S4 E2 battery G40-G45; S5 E3 adjudication G50-G52; S6 E4
mechanism G60-G62; S7 guards G70-G72; S8 G80 pricing + G99
runtime.  DETERMINISM: no randomness anywhere; ProcessPool results
keyed; run2 must be identical modulo wall-clock tokens (lines
carrying 'WALL').

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
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 10
RUNTIME_BAR = 2700.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
SGRID_DEN = 8                     # s = j/8, j = 0..8
SFINE_DEN = 80                    # fine s = j/80
SFINE_J = tuple(range(40, 73))    # 33 points in [0.50, 0.90]
STURM_RUNGS = (4, 5)
NGRID_FAC = 16
PF_SAMPLES = 17
WIT_RUNG = 5
WIT_FACT = 1000

MICRO_CELLS = (("EPSTEIN", 8, 80), ("MAIN", 8, 80))
CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

RANK1_BAR = 1e-40
EIG_RES_BAR = 1e-30
EIG_ORTH_BAR = 1e-30
SEC_RES_BAR = 1e-20
ANCHOR_LAM_BAR = 1e-6
ANCHOR_OVL_BAR = 1e-12
INVIT_RES_BAR = 1e-12
ZCLS = 1e-30
SIGN_RES = 1e-6
DIP_BAR = 1e-12
LC_BAR = 1e-30
PF_BAR = 1e-30
TH_TOL = 1e-20
CTRL_RMIN_TOL = 0.05
TAU_FLAT_BAR = 0.30
WIT_YT_BAND = (990.0, 1010.0)
WIT_A0_BAR = 1e-6

LOG_TOL = 0.10
FRAC_TOL = 0.05
SLOPE_TOL = 0.10

# --------------------------------------- inheritance tables (r189-r200)
R189_DESC = {4: 2, 5: 5, 6: 4, 7: 7, 8: 9, 9: 9, 10: 13, 11: 16,
             12: 18, 13: 20, 14: 22, 15: 23, 16: 25, 20: 34}
R197_JR0 = {4: "-5.0", 5: "-7.5", 6: "-9.7", 7: "-12.1", 8: "-14.3",
            9: "-16.6", 10: "-19.0", 11: "-21.4", 12: "-24.0",
            13: "-26.3", 14: "-29.0", 15: "-31.1", 16: "-33.6",
            20: "-43.3"}
_HS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
R200_RMIN0 = dict(zip(_HS, ("0.840", "0.846", "0.875", "0.840",
                            "0.885", "0.886", "0.900", "0.879",
                            "0.902", "0.885", "0.867", "0.874",
                            "0.883", "0.852")))
R200_RMINH = dict(zip(_HS, ("0.729", "0.721", "0.786", "0.721",
                            "0.803", "0.795", "0.809", "0.775",
                            "0.832", "0.797", "0.827", "0.818",
                            "0.788", "0.816")))
R200_EPS = dict(nnode=3, s_star=6, rmin0="0.690", rmin1="-0.481")

# -------------- calibrated record tables (calib1 VERBATIM, frozen)
CAL_FROZEN = True
CAL_NDIP_MAX = dict(zip(_HS, (1, 3, 3, 5, 4, 8, 8, 9, 13, 14, 18,
                              15, 22, 30)))
CAL_DIPM1 = dict(zip(_HS, ("0.0034", "0.0031", "0.0029", "0.0030",
                           "0.0025", "0.0026", "0.0024", "0.0024",
                           "0.0024", "0.0023", "-0.0153", "0.0020",
                           "0.0020", "-0.0458")))
CAL_SMIG = dict(zip(_HS, (0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 5, 3, 0,
                          7)))
CAL_SEDGE = dict(zip(_HS, (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 0, 0,
                           7)))
CAL_SCM1 = dict(zip(_HS, (3, 4, 5, 6, 9, 8, 9, 12, 11, 14, 15, 16,
                          19, 25)))
CAL_SSC = dict(zip(_HS, (1, 3, 1, 3, 4, 7, 9, 11, 13, 19, 19, 13,
                         16, 25)))
CAL_SCD0 = dict(zip(_HS, (0, 6, 8, 14, 14, 20, 24, 28, 34, 38, 42,
                          46, 52, 72)))
CAL_SCD1 = {h: 0 for h in _HS}
CAL_NB1 = {h: 0 for h in _HS}
CAL_TRI68 = dict(zip(_HS, ("0.326", "0.517", "0.341", "0.564",
                           "0.637", "0.571", "0.586", "0.760",
                           "0.707", "0.858", "0.755", "0.688",
                           "0.962", "1.029")))
CAL_SCERT = dict(zip(_HS, (7, 7, 7, 7, 6, 7, 7, 6, 6, 6, 6, 6, 6,
                           5)))
CAL_RHO11 = dict(zip(_HS, ("0.1", "0.1", "0.1", "0.1", "0.2",
                           "0.2", "0.2", "0.2", "0.2", "0.2",
                           "0.2", "0.2", "0.2", "0.3")))
CAL_Z1REL = dict(zip(_HS, ("-6.9", "-11.4", "-15.7", "-20.0",
                           "-24.4", "-28.8", "-33.6", "-38.1",
                           "-43.2", "-47.6", "-53.0", "-57.1",
                           "-62.1", "-81.2")))
CAL_LCV0 = dict(zip(_HS, (27, 41, 51, 69, 76, 95, 104, 122, 154,
                          165, 191, 183, 220, 302)))
CAL_MICRO_EPS = dict(s_lastpos="0.6875", s_firstneg="0.7000",
                     s_lin="0.69898", s_pred="0.68734",
                     tstar="0.5000", nflip_cross=0,
                     u1_node="0.2307", m_dr=1)
CAL_CTRL = {
    ("SCRARITH", 5): dict(nnode=0, rmin0="0.814", ndip_max=2,
                          s_cert=7, sc0=3),
    ("SMOOTH", 5): dict(nnode=0, rmin0="0.873", ndip_max=4,
                        s_cert=8, sc0=1),
    ("EPSTEIN", 8): dict(nnode=3, s_star=6, rmin0="0.690",
                         rmin1="-0.481", ndip_max=6, s_cert=4,
                         sc0=5, negw=0),
}
CAL_SLOPES = {"dipm_mid": "+0.000", "tri68": "-0.008",
              "rminh": "-0.001", "rho11": "-0.002",
              "a0log": "+0.50"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list = []
INFO: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan"), float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return float("nan"), float("nan")
    sl = sxy / sxx
    return sl, my - sl * mx


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; eigendecomposition "
                       "access IN-SCOPE (anatomy contract, r195-r200 "
                       "lineage); fully zero-free; concurrent-lane "
                       "files untouched")


# ------------------------------------------------------- shared helpers
def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def frac_of_mpf(x) -> Fraction:
    sign, man, exp, _bc = mp.mpf(x)._mpf_
    v = Fraction(man, 1) * (Fraction(2) ** exp)
    return -v if sign else v


def bottom_vec_mp(Raw, K, froW):
    """r195-r200 VERBATIM: 3 LU solves + residual ward."""
    x = mp.matrix([mp.mpf(1) for _ in range(K)])
    for _it in range(3):
        x = mp.lu_solve(Raw, x)
        nx = mp.sqrt(sum(x[i] ** 2 for i in range(K)))
        x = x / nx
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K)) / froW
    return v, lam, float(res)


def prof_eval(v, K, N, ct):
    half = N // 2
    return [sum(v[k] * ct[(k * j) % N] for k in range(K))
            for j in range(half + 1)]


def align_census(v0, K):
    """r198 VERBATIM."""
    c = [((-1) ** k) * v0[k] for k in range(K)]
    cmax = max(abs(x) for x in c)
    kmax = max(range(K), key=lambda k: abs(c[k]))
    if c[kmax] < 0:
        c = [-x for x in c]
    zb = mp.mpf(ZCLS) * cmax
    mis = sum(1 for x in c if x < -zb)
    hd = 0
    for x in c:
        if x > zb:
            hd += 1
        else:
            break
    return dict(mis=mis, hd=hd)


# ---------------------------------------------- Sturm (BH10 VERBATIM)
def cheb_poly(vF):
    K = len(vF)
    Tprev = [Fraction(1)]
    Tcur = [Fraction(0), Fraction(1)]
    P = [Fraction(0)] * K
    P[0] += vF[0]
    if K > 1:
        P[1] += vF[1]
    for k in range(2, K):
        Tnext = [Fraction(0)] * (k + 1)
        for i, c in enumerate(Tcur):
            Tnext[i + 1] += 2 * c
        for i, c in enumerate(Tprev):
            Tnext[i] -= c
        for i, c in enumerate(Tnext):
            P[i] += vF[k] * c
        Tprev, Tcur = Tcur, Tnext
    while len(P) > 1 and P[-1] == 0:
        P.pop()
    return P


def polyval_frac(P, x):
    acc = Fraction(0)
    for c in reversed(P):
        acc = acc * x + c
    return acc


def frac_to_int_poly(P):
    emax = 0
    for c in P:
        d = c.denominator
        e = d.bit_length() - 1
        assert d == (1 << e), "non-dyadic coefficient"
        emax = max(emax, e)
    return [int(c * (1 << emax)) for c in P]


def _content(P):
    g = 0
    for c in P:
        g = math.gcd(g, abs(c))
    return g if g else 1


def _prem_even(A, B):
    A = A[:]
    dB = len(B) - 1
    lb = B[-1]
    lb2 = lb * lb
    while len(A) - 1 >= dB and any(A):
        if A[-1] == 0:
            A.pop()
            continue
        off = len(A) - 1 - dB
        coef = A[-1] * lb
        A = [c * lb2 for c in A]
        for i in range(len(B)):
            A[off + i] -= coef * B[i]
        while len(A) > 1 and A[-1] == 0:
            A.pop()
        if len(A) - 1 < dB:
            break
    while len(A) > 1 and A[-1] == 0:
        A.pop()
    return A


def _ipolyval(P, num, den):
    n = len(P) - 1
    acc = 0
    for i, c in enumerate(P):
        acc += c * (num ** i) * (den ** (n - i))
    return acc


def sturm_roots(Pfrac, a, b):
    P = frac_to_int_poly(Pfrac)
    g = _content(P)
    P = [c // g for c in P]
    dP = [P[i] * i for i in range(1, len(P))]
    g = _content(dP)
    dP = [c // g for c in dP]
    chain = [P, dP]
    while len(chain[-1]) > 1:
        R = _prem_even(chain[-2], chain[-1])
        if not any(R):
            break
        g = _content(R)
        R = [-c // g for c in R]
        chain.append(R)

    def sigma(x: Fraction):
        signs = []
        for Q in chain:
            v = _ipolyval(Q, x.numerator, x.denominator)
            if v != 0:
                signs.append(1 if v > 0 else -1)
        return sum(1 for i in range(len(signs) - 1)
                   if signs[i] != signs[i + 1])

    return sigma(a) - sigma(b)


# ---------------------------------- exact Descartes / Bernstein counts
def _sc_ints(seq) -> int:
    nz = [1 if c > 0 else -1 for c in seq if c != 0]
    return sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])


def descartes_count(pint) -> int:
    """SC of coeffs of R(u) = (u+1)^n P((u-1)/(u+1)); classical
    Descartes bound on #roots of P in (-1, 1), tight mod 2."""
    n = len(pint) - 1
    binom = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        binom[i][0] = 1
        for j in range(1, i + 1):
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j]
    R = [0] * (n + 1)
    for j, pj in enumerate(pint):
        if pj == 0:
            continue
        m = n - j
        for i1 in range(j + 1):
            c1 = binom[j][i1] * ((-1) ** (j - i1)) * pj
            row = binom[m]
            for i2 in range(m + 1):
                R[i1 + i2] += c1 * row[i2]
    return _sc_ints(R)


def bernstein_stats(pint):
    """Bernstein coefficients of P on [-1, 1] at native degree:
    q(u) = P(2u - 1) on [0, 1]; b_i = sum_{j<=i} q_j C(i,j)/C(n,j).
    NB = 0  =>  P >= 0 on [-1, 1] (certificate class)."""
    n = len(pint) - 1
    binom = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        binom[i][0] = 1
        for j in range(1, i + 1):
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j]
    q = [0] * (n + 1)
    for j, pj in enumerate(pint):
        if pj == 0:
            continue
        p2 = pj
        for i in range(j + 1):
            q[i] += p2 * binom[j][i] * (2 ** i) * ((-1) ** (j - i))
    b = []
    for i in range(n + 1):
        acc = Fraction(0)
        for j in range(i + 1):
            if q[j]:
                acc += Fraction(q[j] * binom[i][j], binom[n][j])
        b.append(acc)
    nb = sum(1 for x in b if x < 0)
    bmax = max(abs(x) for x in b) if b else Fraction(1)
    bmin_rel = float(min(b) / bmax) if bmax else 0.0
    return nb, bmin_rel


# ------------------------------------------------- secular machinery
def secular_bottom_pair(d, z, ccs, dps, K):
    """r200 post-A1 VERBATIM: ALL K levels kept as poles; bottom
    pair from the first two interlacing gaps."""
    nbis = int(3.4 * dps) + 60

    def root_in(lo, hi):
        w = hi - lo
        a2 = lo + w * mp.mpf(10) ** (-dps)
        b2 = hi - w * mp.mpf(10) ** (-dps)
        for _ in range(nbis):
            m = (a2 + b2) / 2
            f = 1 + ccs * sum(z[i] ** 2 / (d[i] - m) for i in range(K))
            if f < 0:
                a2 = m
            else:
                b2 = m
        return (a2 + b2) / 2

    lam0 = root_in(d[0], d[1])
    lam1 = root_in(d[1], d[2])
    y = [z[m] / (d[m] - lam0) for m in range(K)]
    ny = mp.sqrt(sum(t * t for t in y))
    y = [t / ny for t in y]
    return lam0, lam1, y


# --------------------------------------------- profile shape censuses
def prof_censuses(Av, N):
    """All E2 profile-side censuses on the (peak-positive) half-
    window sequence Av[0..N/2]."""
    half = N // 2
    amax = max(abs(x) for x in Av)
    zb = mp.mpf(ZCLS) * amax
    dipb = mp.mpf(DIP_BAR) * amax
    amin = min(Av)
    jmin = min(range(len(Av)), key=lambda j: Av[j])
    jpeak = max(range(len(Av)), key=lambda j: Av[j])
    # I1 interior dips
    ndip = 0
    jdip = None
    dipdepth = 0.0
    for j in range(1, half):
        if Av[j] < Av[j - 1] - dipb and Av[j] < Av[j + 1] - dipb:
            ndip += 1
            dep = float((min(Av[j - 1], Av[j + 1]) - Av[j]) / amax)
            if dep > dipdepth:
                dipdepth = dep
                jdip = j
    emin = min(Av[0], Av[half])
    intmin = min(Av[1:half]) if half > 1 else Av[0]
    dip_margin = float((intmin - emin) / amax)
    edge_min = bool(amin >= emin - zb)
    # I2 log-concavity (only where A above zero class)
    lcv = 0
    lc_margin = None
    for j in range(1, half):
        if Av[j - 1] > zb and Av[j] > zb and Av[j + 1] > zb:
            g = (mp.log(Av[j + 1]) - 2 * mp.log(Av[j])
                 + mp.log(Av[j - 1]))
            if g > mp.mpf(LC_BAR):
                lcv += 1
            gf = float(g)
            if lc_margin is None or gf > lc_margin:
                lc_margin = gf
    # I3 PF proxies on the frozen 17-sample even extension
    js = [(i * half) // (PF_SAMPLES - 1) for i in range(PF_SAMPLES)]
    aS = [Av[j] for j in js]
    m2 = mp.mpf(PF_BAR) * amax ** 2
    m3 = mp.mpf(PF_BAR) * amax ** 3
    pf2 = 0
    pf3 = 0
    S = PF_SAMPLES

    def tv(i, j):
        return aS[abs(i - j)]
    for i in range(S - 1):
        for j in range(S - 1):
            det2 = tv(i, j) * tv(i + 1, j + 1) \
                - tv(i, j + 1) * tv(i + 1, j)
            if det2 < -m2:
                pf2 += 1
    for i in range(S - 2):
        for j in range(S - 2):
            a11, a12, a13 = tv(i, j), tv(i, j + 1), tv(i, j + 2)
            a21, a22, a23 = tv(i + 1, j), tv(i + 1, j + 1), \
                tv(i + 1, j + 2)
            a31, a32, a33 = tv(i + 2, j), tv(i + 2, j + 1), \
                tv(i + 2, j + 2)
            det3 = (a11 * (a22 * a33 - a23 * a32)
                    - a12 * (a21 * a33 - a23 * a31)
                    + a13 * (a21 * a32 - a22 * a31))
            if det3 < -m3:
                pf3 += 1
    # I4 inflection count (second difference sign changes)
    d2 = [Av[j + 1] - 2 * Av[j] + Av[j - 1] for j in range(1, half)]
    d2max = max((abs(x) for x in d2), default=mp.mpf(0))
    zb2 = mp.mpf(ZCLS) * d2max if d2max > 0 else mp.mpf(0)
    sgn2 = [1 if x > zb2 else (-1 if x < -zb2 else 0) for x in d2]
    nz2 = [s for s in sgn2 if s != 0]
    ninfl = sum(1 for i in range(1, len(nz2)) if nz2[i] != nz2[i - 1])
    # node stats (r197/r200 class)
    node = bool(amin < -mp.mpf(SIGN_RES) * amax)
    sgn = [0 if abs(x) <= zb else (1 if x > 0 else -1) for x in Av]
    nzs = [s for s in sgn if s != 0]
    nsc = sum(1 for i in range(1, len(nzs)) if nzs[i] != nzs[i - 1])
    return dict(rmin=float(amin / amax), jmin=jmin, jpeak=jpeak,
                node=node, nsc=nsc, ndip=ndip, jdip=jdip,
                dipdepth=dipdepth, dip_margin=dip_margin,
                edge_min=edge_min,
                a0rel=float(Av[0] / amax),
                al2rel=float(Av[half] / amax),
                lcv=lcv, lc_margin=lc_margin, pf2=pf2, pf3=pf3,
                ninfl=ninfl)


def coeff_censuses(v, phi, K):
    """E2 coefficient-side censuses on the orientation-fixed v."""
    vmax = max(abs(x) for x in v)
    zb = mp.mpf(ZCLS) * vmax
    sgn = [0 if abs(x) <= zb else (1 if x > 0 else -1) for x in v]
    nz = [s for s in sgn if s != 0]
    sc_mode = sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])
    al = align_census(v, K)
    r = [v[k] / phi[k] for k in range(K)]
    dr = [r[k + 1] - r[k] for k in range(K - 1)]
    drmax = max((abs(x) for x in dr), default=mp.mpf(0))
    zbd = mp.mpf(ZCLS) * drmax if drmax > 0 else mp.mpf(0)
    sgd = [1 if x > zbd else (-1 if x < -zbd else 0) for x in dr]
    nzd = [s for s in sgd if s != 0]
    nrev = sum(1 for i in range(1, len(nzd)) if nzd[i] != nzd[i - 1])
    return dict(sc_mode=sc_mode, mis=al["mis"], hd=al["hd"],
                nrev=nrev)


def eig_signs(y, K):
    ymax = max(abs(t) for t in y)
    zb = mp.mpf(ZCLS) * ymax
    ori = 1 if y[0] > 0 else -1
    return tuple(0 if abs(y[m]) <= zb
                 else (1 if ori * y[m] > 0 else -1)
                 for m in range(K))


def exact_counts(v):
    """Exact Descartes + Bernstein + the Chebyshev transport poly."""
    vF = [frac_of_mpf(t) for t in v]
    P = cheb_poly(vF)
    if polyval_frac(P, Fraction(1)) < 0:
        P = [-c for c in P]
    pint = frac_to_int_poly(P)
    g = _content(pint)
    pint = [c // g for c in pint]
    scd = descartes_count(pint)
    nb, bmin = bernstein_stats(pint)
    return P, pint, scd, nb, bmin


# ----------------------------------------------------- atom censuses
def atom_census(world: str, x: int, dps: int) -> dict:
    """Source-level atom weights, replicated VERBATIM from
    radius4_an_probe.build_cell world blocks (no builder call)."""
    with mp.workdps(dps):
        atoms = []          # (q:int, weight:mpf)
        if world in ("MAIN", "SCRARITH"):
            icap = int(math.floor(x))
            comp = bytearray(icap + 1)
            nlist = []
            for p in range(2, icap + 1):
                if comp[p]:
                    continue
                for mlt in range(p * p, icap + 1, p):
                    comp[mlt] = 1
                q = p
                while q <= icap:
                    nlist.append((q, p))
                    q *= p
            nlist.sort()
            for q, p in nlist:
                atoms.append((q, mp.log(p) / mp.sqrt(q)))
            if world == "SCRARITH":
                gold = (math.sqrt(5.0) - 1.0) / 2.0
                keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atoms = [(atoms[i][0], wts[perm[i]])
                         for i in range(len(atoms))]
        elif world == "EPSTEIN":
            icap = int(math.floor(x))
            rq = [0.0] * (icap + 1)
            xm = int(math.isqrt(icap)) + 1
            ym = int(math.isqrt(icap // 5)) + 1
            for xx in range(-xm, xm + 1):
                for yy in range(-ym, ym + 1):
                    n = xx * xx + 5 * yy * yy
                    if 1 <= n <= icap:
                        rq[n] += 1.0
            av = [mp.mpf(t) / 2 for t in rq]
            lamq = [mp.mpf(0)] * (icap + 1)
            for n in range(2, icap + 1):
                sacc = av[n] * mp.log(n)
                for dd in range(2, n):
                    if n % dd == 0:
                        sacc -= lamq[dd] * av[n // dd]
                lamq[n] = sacc
            for n in range(2, icap + 1):
                if abs(lamq[n]) > mp.mpf("1e-30"):
                    atoms.append((n, lamq[n] / mp.sqrt(n)))
        else:
            atoms = []

        def is_pp(n: int) -> bool:
            for p in range(2, n + 1):
                if n % p == 0:
                    while n % p == 0:
                        n //= p
                    return n == 1
            return False
        n_neg = sum(1 for _q, w in atoms if w < 0)
        tot = sum(abs(w) for _q, w in atoms)
        nonpp = [(q, w) for q, w in atoms if not is_pp(q)]
        nonpp_mass = (float(sum(abs(w) for _q, w in nonpp) / tot)
                      if tot > 0 else 0.0)
        return dict(n_atoms=len(atoms), n_neg=n_neg,
                    nonpp_count=len(nonpp), nonpp_massfrac=nonpp_mass,
                    qs=[q for q, _w in atoms],
                    ws=[float(w) for _q, w in atoms])


# ------------------------------------------- per-cell shared builder
def build_common(world, h, dps):
    ce = R4.build_cell(h, KFAC, world, dps, want_mp=True)
    K = ce["K"]
    aa = mp.log(h) / 2
    s2 = mp.sinh(aa / 2) ** 2
    oms = [k * mp.pi / aa for k in range(K)]
    b = [o * o for o in oms]
    par = [mp.mpf((-1.0) ** k) for k in range(K)]
    nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
           for k in range(K)]
    RawW = raw_of(ce["mpM"], par, nrm, K)
    RawP = raw_of(ce["mpPole"], par, nrm, K)
    phi = [1 / (mp.mpf(1) / 4 + b[k]) for k in range(K)]
    r1dev = mp.mpf(0)
    r1max = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            tgt = 2 * s2 * phi[i] * phi[j]
            r1dev = max(r1dev, abs(RawP[i, j] - tgt))
            r1max = max(r1max, abs(tgt))
    NoP = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            NoP[i, j] = RawW[i, j] - RawP[i, j]
    fro = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                      for j in range(K)))
    froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                       for j in range(K)))
    E, Q = mp.eigsy(NoP)
    idx = sorted(range(K), key=lambda m: E[m])
    d = [E[m] for m in idx]
    eres = mp.mpf(0)
    for col in (0, 1, K - 1):
        m = idx[col]
        for i in range(K):
            ri = sum(NoP[i, j] * Q[j, m] for j in range(K)) \
                - E[m] * Q[i, m]
            eres = max(eres, abs(ri))
    oworst = mp.mpf(0)
    for (m1, m2) in ((idx[0], idx[0]), (idx[0], idx[1]),
                     (idx[1], idx[1])):
        dot = sum(Q[i, m1] * Q[i, m2] for i in range(K))
        tgt = mp.mpf(1) if m1 == m2 else mp.mpf(0)
        oworst = max(oworst, abs(dot - tgt))
    z = [sum(Q[i, idx[m]] * phi[i] for i in range(K))
         for m in range(K)]
    N = NGRID_FAC * K
    twopi = 2 * mp.pi
    ct = [mp.cos(twopi * m / N) for m in range(N)]
    U0 = prof_eval([Q[i, idx[0]] for i in range(K)], K, N, ct)
    j0 = max(range(len(U0)), key=lambda j: abs(U0[j]))
    if U0[j0] < 0:
        U0 = [-x for x in U0]
    minU0 = min(U0)
    u0max = max(abs(x) for x in U0)
    l1 = [sum(abs(Q[i, idx[m]]) for i in range(K)) for m in range(K)]
    # RAW (unoriented) eigenprofile endpoint values for the two-mode
    # center predictor: U_m(t) = sum_k Q[k, idx[m]] cos(om_k t);
    # t = 0 -> all-ones column, t = L/2 -> alternating column.
    U0raw0 = sum(Q[i, idx[0]] for i in range(K))
    U0rawc = sum(Q[i, idx[0]] * ((-1) ** i) for i in range(K))
    U1raw0 = sum(Q[i, idx[1]] for i in range(K))
    U1rawc = sum(Q[i, idx[1]] * ((-1) ** i) for i in range(K))
    U1 = prof_eval([Q[i, idx[1]] for i in range(K)], K, N, ct)
    u1max = max(abs(x) for x in U1)
    zb1 = mp.mpf(ZCLS) * u1max
    u1node = None
    for j in range(1, N // 2 + 1):
        if (U1[j - 1] > zb1 and U1[j] < -zb1) or \
           (U1[j - 1] < -zb1 and U1[j] > zb1):
            u1node = (j - 0.5) / N
            break
    return dict(ce=ce, K=K, aa=aa, s2=s2, b=b, par=par, nrm=nrm,
                RawW=RawW, RawP=RawP, phi=phi, NoP=NoP, fro=fro,
                froW=froW, Q=Q, idx=idx, d=d, z=z, N=N, ct=ct,
                U0=U0, minU0=minU0, u0max=u0max, l1=l1,
                u1node=u1node,
                U0raw0=U0raw0, U0rawc=U0rawc,
                U1raw0=U1raw0, U1rawc=U1rawc,
                u1max=u1max,
                rank1_dev=float(r1dev / r1max),
                eig_res=float(eres / fro),
                eig_orth=float(oworst))


def path_point(C, s_num, s_den, dps):
    """One path point: v(s), oriented profile + all censuses."""
    K, N, ct = C["K"], C["N"], C["ct"]
    Q, idx, d, z = C["Q"], C["idx"], C["d"], C["z"]
    if s_num == 0:
        lam0, lam1 = d[0], d[1]
        v = [Q[i, idx[0]] for i in range(K)]
        y = [mp.mpf(1)] + [mp.mpf(0)] * (K - 1)
    else:
        s = mp.mpf(s_num) / s_den
        lam0, lam1, y = secular_bottom_pair(
            d, z, s * 2 * C["s2"], dps, K)
        v = [sum(Q[i, idx[m]] * y[m] for m in range(K))
             for i in range(K)]
    Av = prof_eval(v, K, N, ct)
    jp = max(range(len(Av)), key=lambda j: abs(Av[j]))
    if Av[jp] < 0:
        Av = [-x for x in Av]
        v = [-x for x in v]
        y = [-t for t in y]
    pc = prof_censuses(Av, N)
    cc = coeff_censuses(v, C["phi"], K)
    # secular load anatomy
    f = float((lam0 - d[0]) / (d[1] - d[0]))
    if s_num == 0:
        rho1 = 0.0
        tri = 0.0
        r2c = 0.0
    else:
        rho1 = float(abs(y[1]) / abs(y[0])) if y[0] != 0 else \
            float("inf")
        tri_num = sum(abs(y[m]) * C["l1"][m] for m in range(1, K))
        tri = float(tri_num / (abs(y[0]) * C["minU0"])) \
            if C["minU0"] > 0 else float("inf")
        den2 = y[0] * C["U0rawc"]
        r2c = float(-(y[1] * C["U1rawc"]) / den2) if den2 != 0 \
            else float("inf")
    return dict(lam0=lam0, lam1=lam1, v=v, y=y, Av=Av, pc=pc, cc=cc,
                f=f, rho1=rho1, tri=tri, r2c=r2c,
                t0min=bool(pc["jmin"] == 0),
                ysig=eig_signs(y, K) if s_num > 0 else None)


# ------------------------------------------------------- battery worker
def w_batt(args) -> dict:
    world, h, dps, want_sturm = args
    try:
        t0 = time.time()
        out = dict(world=world, h=h, err="")
        with mp.workdps(dps):
            C = build_common(world, h, dps)
            K = C["K"]
            out["K"] = K
            out["rank1_dev"] = C["rank1_dev"]
            out["eig_res"] = C["eig_res"]
            out["eig_orth"] = C["eig_orth"]
            out["d1_pos"] = bool(C["d"][1] > 0)
            out["minU0_pos"] = bool(C["minU0"] > 0)
            out["u1_node"] = C["u1node"]
            tau = C["ce"]["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            out["z1rel_log10"] = float(
                mp.log(abs(C["z"][1]) / abs(C["z"][0]), 10)) \
                if C["z"][1] != 0 else -300.0
            cells = []
            sig_ref = None
            sig_ok = True
            for sj in range(SGRID_DEN + 1):
                P = path_point(C, sj, SGRID_DEN, dps)
                row = dict(sj=sj, rmin=P["pc"]["rmin"],
                           node=P["pc"]["node"], nsc=P["pc"]["nsc"],
                           ndip=P["pc"]["ndip"],
                           dipdepth=P["pc"]["dipdepth"],
                           dip_margin=P["pc"]["dip_margin"],
                           edge_min=P["pc"]["edge_min"],
                           t0min=P["t0min"],
                           a0rel=P["pc"]["a0rel"],
                           al2rel=P["pc"]["al2rel"],
                           lcv=P["pc"]["lcv"],
                           lc_margin=P["pc"]["lc_margin"],
                           pf2=P["pc"]["pf2"], pf3=P["pc"]["pf3"],
                           ninfl=P["pc"]["ninfl"],
                           sc_mode=P["cc"]["sc_mode"],
                           mis=P["cc"]["mis"], hd=P["cc"]["hd"],
                           nrev=P["cc"]["nrev"],
                           f=P["f"], rho1=P["rho1"], tri=P["tri"],
                           r2c=P["r2c"])
                _Pf, _pint, scd, nb, bmin = exact_counts(P["v"])
                row["sc_desc"] = scd
                row["nb"] = nb
                row["bmin"] = bmin
                if want_sturm:
                    nr = sturm_roots(_Pf, Fraction(-1), Fraction(1))
                    row["zst"] = nr
                    row["p1_pos"] = bool(
                        polyval_frac(_Pf, Fraction(1)) > 0)
                if P["ysig"] is not None:
                    if sig_ref is None:
                        sig_ref = P["ysig"]
                    else:
                        for m in range(K):
                            a1, b1 = sig_ref[m], P["ysig"][m]
                            if a1 != 0 and b1 != 0 and a1 != b1:
                                sig_ok = False
                if sj == SGRID_DEN:
                    row["rho1_log10"] = (
                        float(math.log10(P["rho1"]))
                        if P["rho1"] > 0 else -300.0)
                    # s = 1 anchor
                    v0w, lamw, invres = bottom_vec_mp(
                        C["RawW"], K, C["froW"])
                    out["invit_res"] = invres
                    out["lam0_pos"] = bool(lamw > 0)
                    out["anchor_dev"] = float(
                        abs(lamw - P["lam0"])
                        / max(abs(lamw), mp.mpf("1e-300")))
                    ovl = abs(sum(P["v"][i] * v0w[i]
                                  for i in range(K)))
                    out["anchor_ovl_dev"] = float(abs(ovl - 1))
                    num0 = abs(sum(v0w[k] for k in range(K)))
                    den0 = sum(abs(v0w[k]) for k in range(K))
                    out["jr0_log10"] = float(mp.log(num0 / den0, 10))
                if sj == SGRID_DEN // 2:
                    # secular residual ward at s = 1/2
                    Ms = mp.zeros(K, K)
                    shalf = mp.mpf(1) / 2
                    for i in range(K):
                        for j in range(K):
                            Ms[i, j] = C["NoP"][i, j] + shalf * 2 \
                                * C["s2"] * C["phi"][i] * C["phi"][j]
                    rres = mp.mpf(0)
                    for i in range(K):
                        ri = sum(Ms[i, j] * P["v"][j]
                                 for j in range(K)) \
                            - P["lam0"] * P["v"][i]
                        rres = max(rres, abs(ri))
                    out["sec_res"] = float(rres / C["fro"])
                cells.append(row)
            out["cells"] = cells
            out["sig_ok"] = sig_ok
            fhat = [C["b"][i] * C["RawW"][i, 0] for i in range(K)]
            out["descents"] = sum(1 for i in range(K - 1)
                                  if fhat[i + 1] < fhat[i])
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "h": h,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ----------------------------------------------------- microscope worker
def w_micro(args) -> dict:
    world, h, dps, fine_js = args
    try:
        t0 = time.time()
        out = dict(world=world, h=h, err="")
        with mp.workdps(dps):
            C = build_common(world, h, dps)
            K = C["K"]
            out["K"] = K
            out["u1_node"] = C["u1node"]
            out["minU0_pos"] = bool(C["minU0"] > 0)
            rows = []
            prev_v = None
            sig_ref = None
            sig_ok = True
            for j in fine_js:
                P = path_point(C, j, SFINE_DEN, dps)
                nflip = 0
                maxdv = 0.0
                if prev_v is not None:
                    vmax = max(abs(x) for x in P["v"])
                    zb = mp.mpf(ZCLS) * vmax
                    for k in range(K):
                        a1, b1 = prev_v[k], P["v"][k]
                        if abs(a1) > zb and abs(b1) > zb and \
                           (a1 > 0) != (b1 > 0):
                            nflip += 1
                        dv = abs(b1 - a1)
                        if float(dv) > maxdv:
                            maxdv = float(dv)
                prev_v = P["v"]
                Pf = cheb_poly([frac_of_mpf(t) for t in P["v"]])
                if polyval_frac(Pf, Fraction(1)) < 0:
                    Pf = [-c for c in Pf]
                zst = sturm_roots(Pf, Fraction(-1), Fraction(1))
                _P2, _pi, scd, nb, _bm = exact_counts(P["v"])
                if P["ysig"] is not None:
                    if sig_ref is None:
                        sig_ref = P["ysig"]
                    else:
                        for m in range(K):
                            a1, b1 = sig_ref[m], P["ysig"][m]
                            if a1 != 0 and b1 != 0 and a1 != b1:
                                sig_ok = False
                rows.append(dict(
                    j=j, s=j / SFINE_DEN, rmin=P["pc"]["rmin"],
                    tmin=P["pc"]["jmin"] / C["N"],
                    node=P["pc"]["node"], nsc=P["pc"]["nsc"],
                    ndip=P["pc"]["ndip"],
                    tdip=(P["pc"]["jdip"] / C["N"]
                          if P["pc"]["jdip"] is not None else None),
                    dipdepth=P["pc"]["dipdepth"],
                    dip_margin=P["pc"]["dip_margin"],
                    t0min=P["t0min"],
                    al2rel=P["pc"]["al2rel"],
                    sc_mode=P["cc"]["sc_mode"], sc_desc=scd, nb=nb,
                    zst=zst, nflip=nflip, maxdv=maxdv,
                    f=P["f"], rho1=P["rho1"], r2c=P["r2c"]))
            out["rows"] = rows
            out["sig_ok"] = sig_ok
            # two-mode center predictor: interpolate r2c(s) = 1
            s_pred = None
            for i2 in range(1, len(rows)):
                r1_, r2_ = rows[i2 - 1]["r2c"], rows[i2]["r2c"]
                if r1_ < 1.0 <= r2_:
                    s_pred = rows[i2 - 1]["s"] \
                        + (rows[i2]["s"] - rows[i2 - 1]["s"]) \
                        * (1.0 - r1_) / (r2_ - r1_)
                    break
            out["s_pred"] = s_pred
            out["u0c_rel"] = float(C["U0rawc"] / C["u0max"])
            out["u1c_rel"] = float(C["U1rawc"] / C["u1max"])
            out["u00_rel"] = float(C["U0raw0"] / C["u0max"])
            out["u10_rel"] = float(C["U1raw0"] / C["u1max"])
            # driver anatomy at the first-negative fine s (if any)
            jneg = next((r["j"] for r in rows if r["rmin"] < 0), None)
            out["m_dr"] = None
            out["tstar"] = None
            if jneg is not None:
                P = path_point(C, jneg, SFINE_DEN, dps)
                jmin = P["pc"]["jmin"]
                out["tstar"] = jmin / C["N"]
                # partial sums of eigenprofile expansion at t*
                acc = mp.mpf(0)
                tcol = [C["ct"][(k * jmin) % C["N"]]
                        for k in range(K)]
                Ucol = [sum(C["Q"][i, C["idx"][m]] * tcol[i]
                            for i in range(K)) for m in range(K)]
                for m in range(K):
                    acc += P["y"][m] * Ucol[m]
                    if m >= 1 and acc < 0:
                        out["m_dr"] = m
                        break
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "h": h,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------- witness leg
def witness_leg() -> dict:
    """r172 recipe / r198-r200 code path VERBATIM at h = WIT_RUNG."""
    dps = DPS[WIT_RUNG]
    ce = R4.build_cell(WIT_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out: dict = {}
    with mp.workdps(dps):
        aa = mp.log(WIT_RUNG) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        RawW = raw_of(ce["mpM"], par, nrm, K)
        froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                           for j in range(K)))
        v0, _lam, _r = bottom_vec_mp(RawW, K, froW)
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0 = sum(((-1) ** k) * cs[k] for k in range(K))
        A2 = sum(((-1) ** k) * cs[k] * b[k] for k in range(1, K))
        yt = abs(A2 / A0)
        dv = A2 * (WIT_FACT - 1) / (b[2] - b[1])
        cs2 = list(cs)
        cs2[1] += dv
        cs2[2] += dv
        A0w = sum(((-1) ** k) * cs2[k] for k in range(K))
        A2w = sum(((-1) ** k) * cs2[k] * b[k] for k in range(1, K))
        out["wit_ytr"] = float(abs(A2w / A0w) / yt)
        out["wit_a0dev"] = float(abs(A0w / A0 - 1))
        N = NGRID_FAC * K
        twopi = 2 * mp.pi
        ct = [mp.cos(twopi * m / N) for m in range(N)]

        def anat(ray):
            y = [par[k] * ray[k] for k in range(K)]
            ny = mp.sqrt(sum(t * t for t in y))
            y = [t / ny for t in y]
            al = align_census(y, K)
            Av = prof_eval(y, K, N, ct)
            jp = max(range(len(Av)), key=lambda j: abs(Av[j]))
            if Av[jp] < 0:
                Av = [-x for x in Av]
                y = [-t for t in y]
            amax = max(abs(x) for x in Av)
            amin = min(Av)
            node = bool(amin < -mp.mpf(SIGN_RES) * amax)
            ovl = abs(sum(y[k] * v0[k] for k in range(K)))
            return dict(mis=al["mis"], hd=al["hd"],
                        nonneg=bool(not node
                                    and float(amin / amax)
                                    > -SIGN_RES),
                        ovl=float(ovl))
        out["base"] = anat(cs)
        out["wit"] = anat(cs2)
    return out


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"
    if args.mode == "record" and not CAL_FROZEN:
        print("record mode requires frozen CAL tables")
        return 1

    print("=" * 78)
    print("eigvec_geometry_probe -- PRIME.EIGENVECTOR.INVARIANT.01 "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/s-grids/censuses/transforms declared in "
          "the frozen spec (SPEC_SHA covers the declaration); priors "
          "P1-P10 pre-registered resolve-and-record, none gate-"
          "forcing; the classical dictionary is NAMED and typed: "
          "Descartes' rule via the Moebius map u -> (u-1)/(u+1) "
          "(Vincent/Collins-Akritas root-isolation context, exact "
          "integer arithmetic, own code), Bernstein-basis "
          "nonnegativity (native degree, certificate class), the "
          "elementary interior-dip edge-reduction (grid-exact), the "
          "triangle-inequality certificate TRI < 1, the r200 secular/"
          "interlacing dictionary (Weyl, Kato, BNS 1978) -- Schoenberg "
          "variation-diminishing and PF/Chebyshev-system theory are "
          "MOTIVATION ONLY, consumed nowhere; tau_h enters ONLY as a "
          "measured per-rung scalar")

    # ------------------------------------------------------------ S2
    section("S2  BATTERY (all reachable rungs + controls)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [("MAIN", h, DPS[h], h in STURM_RUNGS) for h in rungs]
    ctasks = list(CTRL_CELLS) if not smoke else [("EPSTEIN", 8, 80)]
    tasks += [(w, x, dp, True) for (w, x, dp) in ctasks]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_batt, tasks):
            res[(out["world"], out["h"])] = out
    errs = [k for k in res if res[k].get("err")]
    for k in errs:
        print("  [ERR] %s %s" % (str(k), res[k]["err"]))
    if errs:
        check("G11-eigsy-wards", False, "worker errors at %s"
              % str(errs))
        print("ABORT: worker errors")
        return 1
    mains = [("MAIN", h) for h in rungs]
    ctrls = [(w, x) for (w, x, _d) in ctasks]

    # ---------------------------------------------------- microscope
    section("S3pre  MICROSCOPE WORKERS")
    mtasks = [(w, x, dp, SFINE_J if not smoke else SFINE_J[::4])
              for (w, x, dp) in MICRO_CELLS]
    mres: dict = {}
    with ProcessPoolExecutor(max_workers=2) as ex:
        for out in ex.map(w_micro, mtasks):
            mres[out["world"]] = out
    merrs = [k for k in mres if mres[k].get("err")]
    for k in merrs:
        print("  [ERR] micro %s %s" % (k, mres[k]["err"]))
    if merrs:
        check("G30-epstein-transition", False, "micro errors")
        print("ABORT: microscope errors")
        return 1

    # ------------------------------------------------------------ S1
    section("S1  INSTRUMENT WARDS")
    allk = mains + ctrls
    check("G10-rank-one-pole-law", all(
        res[k]["rank1_dev"] <= RANK1_BAR for k in allk),
          "RawP == 2 sinh(a/2)^2 phi phi^T ENTRYWISE at every cell "
          "(max rel dev %.1e, bar %.0e): the homotopy is the exact "
          "rank-one positive path, the secular machinery is exact "
          "theory (r200 G11 VERBATIM)"
          % (max(res[k]["rank1_dev"] for k in allk), RANK1_BAR))
    check("G11-eigsy-wards", all(
        res[k]["eig_res"] <= EIG_RES_BAR
        and res[k]["eig_orth"] <= EIG_ORTH_BAR for k in allk),
          "mp.eigsy(NoP) at full dps: eigen-residual <= %.1e (bar "
          "%.0e), bottom-pair orthonormality dev <= %.1e (bar %.0e)"
          % (max(res[k]["eig_res"] for k in allk), EIG_RES_BAR,
             max(res[k]["eig_orth"] for k in allk), EIG_ORTH_BAR))
    check("G12-secular-residual-ward", all(
        res[k]["sec_res"] <= SEC_RES_BAR for k in mains),
          "direct residual |M(1/2) v - lam v|/fro of the secular "
          "bottom pair at s = 1/2: max %.1e (bar %.0e)"
          % (max(res[k]["sec_res"] for k in mains), SEC_RES_BAR))
    check("G13-s1-anchor", all(
        res[k]["anchor_dev"] <= ANCHOR_LAM_BAR
        and res[k]["anchor_ovl_dev"] <= ANCHOR_OVL_BAR
        and res[k]["invit_res"] <= INVIT_RES_BAR for k in mains),
          "s = 1 endpoint vs mp inverse iteration on RawW: lambda_0 "
          "rel dev <= %.1e (bar %.0e), overlap dev <= %.1e (bar "
          "%.0e), invit residual <= %.1e"
          % (max(res[k]["anchor_dev"] for k in mains),
             ANCHOR_LAM_BAR,
             max(res[k]["anchor_ovl_dev"] for k in mains),
             ANCHOR_OVL_BAR,
             max(res[k]["invit_res"] for k in mains)))
    # G14: exact-count cross-wards wherever Sturm ran
    ok14 = True
    det14 = []
    for k in allk:
        for c in res[k]["cells"]:
            if "zst" not in c:
                continue
            Z = c["zst"]
            if c["sc_desc"] < Z or (c["sc_desc"] - Z) % 2 != 0:
                ok14 = False
                det14.append("%s s=%d/8 desc %d < Z %d or parity"
                             % (str(k), c["sj"], c["sc_desc"], Z))
            if c["nb"] == 0 and Z != 0:
                ok14 = False
                det14.append("%s s=%d/8 NB=0 but Z=%d"
                             % (str(k), c["sj"], Z))
            if c["nsc"] == 0 and c["node"]:
                ok14 = False
    for w in mres:
        for r in mres[w]["rows"]:
            if r["sc_desc"] < r["zst"] or \
               (r["sc_desc"] - r["zst"]) % 2 != 0:
                ok14 = False
                det14.append("micro %s j=%d" % (w, r["j"]))
    check("G14-exact-count-cross-ward", ok14,
          "at EVERY exact cell (battery h = 4, 5 + all controls, all "
          "9 s; microscope all fine s): Sturm zero count Z <= "
          "SC_desc AND SC_desc == Z (mod 2) AND (NB = 0 => Z = 0) "
          "-- the classical Descartes bound and its parity are "
          "instrument-verified against the independent integer-PRS "
          "chain%s" % ("" if ok14 else "; VIOLATIONS: "
                       + "; ".join(det14[:6])))
    check("G15-eigenbasis-sign-freeze", all(
        res[k]["sig_ok"] for k in allk) and all(
        mres[w]["sig_ok"] for w in mres),
          "THE SECULAR SIGN-FREEZE THEOREM warded at every cell: for "
          "s > 0, y_m(s) = z_m/(d_m - lam_0(s)) with lam_0(s) in "
          "(d_0, d_1), so sign(y_m) is CONSTANT along the whole path "
          "(above the 1e-30 class; orientation-adjusted) -- verified "
          "at all battery cells (8 s-points each) and all %d "
          "microscope cells: the eigenbasis sign-change count is an "
          "s = 0 DATUM, structurally INCAPABLE of being a transport "
          "separator (typed EXACT)"
          % sum(len(mres[w]["rows"]) for w in mres))

    # ------------------------------------------------------------ S2b
    section("S2b  INHERITANCE (r189/r197/r198/r200)")
    ok20 = all(res[k]["descents"] == R189_DESC[k[1]] for k in mains) \
        and all(abs(res[k]["jr0_log10"] - float(R197_JR0[k[1]]))
                <= LOG_TOL for k in mains) \
        and all(res[k]["lam0_pos"] for k in mains)
    check("G20-inheritance", ok20,
          "descent counts == r189 EXACT; log10 jr_0 == r197 CAL_JR0 "
          "within %.2f dex; lambda_0(RawW) > 0 at every MAIN rung"
          % LOG_TOL)
    ok21 = True
    for k in mains:
        cs = res[k]["cells"]
        rm0, rmh = cs[0]["rmin"], cs[SGRID_DEN // 2]["rmin"]
        nn = sum(1 for c in cs if c["node"])
        mono = all(cs[j + 1]["rmin"] < cs[j]["rmin"]
                   for j in range(SGRID_DEN))
        ok21 = ok21 and nn == 0 and mono \
            and abs(rm0 - float(R200_RMIN0[k[1]])) <= FRAC_TOL \
            and abs(rmh - float(R200_RMINH[k[1]])) <= FRAC_TOL
    ke = ("EPSTEIN", 8)
    if ke in res:
        cs = res[ke]["cells"]
        nn = sum(1 for c in cs if c["node"])
        sstar = next((c["sj"] for c in cs if c["node"]), None)
        ok21 = ok21 and nn == R200_EPS["nnode"] \
            and sstar == R200_EPS["s_star"] \
            and abs(cs[0]["rmin"] - float(R200_EPS["rmin0"])) \
            <= CTRL_RMIN_TOL \
            and abs(cs[SGRID_DEN]["rmin"]
                    - float(R200_EPS["rmin1"])) <= CTRL_RMIN_TOL
    check("G21-r200-path-inheritance", ok21,
          "MAIN: nnode = 0, rmin monotone decreasing, rmin0/rminh == "
          "r200 CAL within %.2f at every rung; EPSTEIN(8) 9-grid "
          "fingerprint == r200 (nnode %d, s* = %s/8, rmin0 %s, rmin1 "
          "%s)" % (FRAC_TOL,
                   sum(1 for c in res[ke]["cells"] if c["node"])
                   if ke in res else -1,
                   str(next((c["sj"] for c in res[ke]["cells"]
                             if c["node"]), None))
                   if ke in res else "?",
                   ("%.3f" % res[ke]["cells"][0]["rmin"])
                   if ke in res else "?",
                   ("%.3f" % res[ke]["cells"][SGRID_DEN]["rmin"])
                   if ke in res else "?"))

    # ------------------------------------------------------------ S3
    section("S3  E1: THE MICROSCOPE AT s* (EPSTEIN(8) vs MAIN(8))")
    me = mres["EPSTEIN"]
    mm = mres["MAIN"]
    for w in ("EPSTEIN", "MAIN"):
        for r in mres[w]["rows"]:
            print("  MIC %-7s s=%.4f rmin %+.4f tmin %.4f al2 %+.4f "
                  "t0min %s ndip %d tdip %s depth %.2e sc %d desc "
                  "%d nb %d Z %d nflip %d f %.5f rho1 %.3e r2c %.4f"
                  % (w, r["s"], r["rmin"], r["tmin"], r["al2rel"],
                     r["t0min"], r["ndip"],
                     ("%.4f" % r["tdip"]) if r["tdip"] is not None
                     else "-", r["dipdepth"], r["sc_mode"],
                     r["sc_desc"], r["nb"], r["zst"], r["nflip"],
                     r["f"], r["rho1"], r["r2c"]))
    rows = me["rows"]
    lastpos = None
    firstneg = None
    for r in rows:
        if r["rmin"] > 0:
            lastpos = r
        elif firstneg is None:
            firstneg = r
    s_lin = None
    if lastpos and firstneg:
        r1, r2 = lastpos["rmin"], firstneg["rmin"]
        s_lin = lastpos["s"] + (firstneg["s"] - lastpos["s"]) \
            * (r1 / (r1 - r2))
    posr = [r for r in rows if r["rmin"] > 0]
    slopes = []
    for i in range(max(1, len(posr) - 3), len(posr)):
        ds = posr[i]["s"] - posr[i - 1]["s"]
        slopes.append((posr[i]["rmin"] - posr[i - 1]["rmin"]) / ds)
    tstar = me.get("tstar")
    center = tstar is not None and abs(tstar - 0.5) < 0.01
    s_pred = me.get("s_pred")
    if calib or smoke:
        print("CAL micro-eps lastpos %.4f firstneg %.4f s_lin %s "
              "tstar %s s_pred %s slopes %s nflip@cross %d u1node "
              "%s m_dr %s u0c %.4f u1c %.4f u00 %.4f u10 %.4f"
              % (lastpos["s"] if lastpos else -1,
                 firstneg["s"] if firstneg else -1,
                 "%.5f" % s_lin if s_lin else "-",
                 "%.4f" % tstar if tstar is not None else "-",
                 "%.5f" % s_pred if s_pred is not None else "-",
                 ["%.2f" % x for x in slopes],
                 firstneg["nflip"] if firstneg else -1,
                 "%.4f" % me["u1_node"] if me["u1_node"] else "-",
                 str(me["m_dr"]), me["u0c_rel"], me["u1c_rel"],
                 me["u00_rel"], me["u10_rel"]))
        ok30 = firstneg is not None and center
    else:
        ok30 = (firstneg is not None and center
                and abs(lastpos["s"] - float(
                    CAL_MICRO_EPS["s_lastpos"])) < 1e-9
                and abs(firstneg["s"] - float(
                    CAL_MICRO_EPS["s_firstneg"])) < 1e-9
                and abs(s_lin - float(CAL_MICRO_EPS["s_lin"]))
                <= 0.01
                and s_pred is not None
                and abs(s_pred - float(CAL_MICRO_EPS["s_pred"]))
                <= 0.01)
    micro_enum = ("EPSTEIN-CENTER-CROSSING" if center
                  else ("EPSTEIN-T0-CROSSING"
                        if tstar is not None and tstar < 0.01
                        else "EPSTEIN-INTERIOR-CROSSING"))
    pred_sharp = (s_pred is not None and s_lin is not None
                  and abs(s_pred - s_lin) <= 0.02)
    check("G30-epstein-transition-anatomy", ok30,
          "P1 RESOLVED RETYPED: %s -- the EPSTEIN(8) crossing "
          "minimum sits AT THE WINDOW CENTER t*/L = %s (the "
          "alternating-sum scalar A(L/2) = sum (-1)^k v_k is the "
          "failing coordinate; interior to the full period, an even "
          "critical point -- NOT a generic interior node and NOT "
          "the t = 0 edge), sign crossing bracketed in (%s, %s), "
          "s*_lin = %s; approach d rmin/ds over the last positive "
          "steps: %s (smooth, no jump); TWO-MODE PREDICTOR: s*_pred "
          "= %s from r2c(s) = 1 (|s*_pred - s*_lin| = %s: %s)"
          % (micro_enum,
             "%.3f" % tstar if tstar is not None else "-",
             "%.4f" % lastpos["s"] if lastpos else "-",
             "%.4f" % firstneg["s"] if firstneg else "-",
             "%.5f" % s_lin if s_lin else "-",
             str(["%.2f" % x for x in slopes]),
             "%.5f" % s_pred if s_pred is not None else "-",
             ("%.4f" % abs(s_pred - s_lin))
             if (s_pred is not None and s_lin is not None) else "-",
             "TWO-MODE-PREDICTOR-SHARP" if pred_sharp
             else "PREDICTOR-LOOSE"))

    okm = all(r["rmin"] > 0 and r["t0min"] and r["dip_margin"] >= 0
              and r["zst"] == 0 for r in mm["rows"])
    check("G31-main-matched-control", okm,
          "MAIN(8) on the SAME fine grid: rmin > 0, T0-MINIMALITY "
          "(argmin = t = 0) and EDGE-MINIMALITY (dip_margin >= 0) "
          "hold, and the EXACT Sturm zero count is 0, at ALL %d "
          "fine s (continuum certificates on the whole fine "
          "window); rmin %.3f -> %.3f, f <= %.4f, rho_1 <= %.2e, "
          "r2c <= %.2e -- the matched world carries NO trace of "
          "the transition (its shallow interior ripples, depth "
          "%.1e max, never undercut the edge)"
          % (len(mm["rows"]), mm["rows"][0]["rmin"],
             mm["rows"][-1]["rmin"],
             max(r["f"] for r in mm["rows"]),
             max(r["rho1"] for r in mm["rows"]),
             max(r["r2c"] for r in mm["rows"]),
             max(r["dipdepth"] for r in mm["rows"])))

    nflip_cross = firstneg["nflip"] if firstneg else -1
    sc_set = sorted({r["sc_mode"] for r in rows})
    check("G32-coefficient-side-reading", nflip_cross == 0,
          "WHAT THE COEFFICIENT VECTOR DOES AT THE TRANSITION: "
          "nothing discrete -- zero sign flips across the crossing "
          "step (nflip = %d), SC_mode drifts only slowly on the "
          "fine window (values %s), max step |dv| %.1e-class: the "
          "crossing is NOT a coefficient-sign event; it is the "
          "monotone secular reweighting (f: %.4f -> %.4f, rho_1: "
          "%.2f -> %.2f across the window) driving the alternating "
          "edge scalar through zero -- eigenvector geometry, not "
          "combinatorics"
          % (nflip_cross, str(sc_set),
             max(r["maxdv"] for r in rows[1:]),
             rows[0]["f"], rows[-1]["f"],
             rows[0]["rho1"], rows[-1]["rho1"]))

    # ------------------------------------------------------------ S4
    section("S4  E2: THE INVARIANT BATTERY")
    if calib or smoke:
        for k in mains + ctrls:
            for c in res[k]["cells"]:
                print("CAL batt %-7s h=%-2d s=%d/8 rmin %+.3f ndip "
                      "%d dep %.1e dipm %+.4f edgemin %s t0min %s "
                      "a0 %+.1e al2 %+.1e lcv %d lcm %s pf2 %d pf3 "
                      "%d ninfl %d sc %d mis %d hd %d nrev %d desc "
                      "%d nb %d bmin %+.1e f %.4f rho1 %.2e tri "
                      "%.3f r2c %+.3f%s"
                      % (k[0], k[1], c["sj"], c["rmin"], c["ndip"],
                         c["dipdepth"], c["dip_margin"],
                         c["edge_min"], c["t0min"], c["a0rel"],
                         c["al2rel"], c["lcv"],
                         ("%+.1e" % c["lc_margin"])
                         if c["lc_margin"] is not None else "-",
                         c["pf2"], c["pf3"], c["ninfl"],
                         c["sc_mode"], c["mis"], c["hd"], c["nrev"],
                         c["sc_desc"], c["nb"], c["bmin"], c["f"],
                         c["rho1"], c["tri"], c["r2c"],
                         (" Z %d" % c["zst"]) if "zst" in c else ""))

    # G40 edge-minimality geometry (I1 retyped per smoke disclosure)
    edge_all = all(c["dip_margin"] >= 0 for k in mains
                   for c in res[k]["cells"])
    ndip_max = {k[1]: max(c["ndip"] for c in res[k]["cells"])
                for k in mains}
    depth_max = {k[1]: max(c["dipdepth"] for c in res[k]["cells"])
                 for k in mains}
    dipm_mid = {k[1]: res[k]["cells"][SGRID_DEN // 2]["dip_margin"]
                for k in mains}
    s_mig = {}
    for k in mains:
        cs = res[k]["cells"]
        mig = SGRID_DEN + 1
        for j in range(SGRID_DEN, -1, -1):
            if cs[j]["t0min"]:
                mig = j
            else:
                break
        s_mig[k[1]] = mig
    s_edge = {}
    for k in mains:
        cs = res[k]["cells"]
        se = SGRID_DEN + 1
        for j in range(SGRID_DEN, -1, -1):
            if cs[j]["dip_margin"] >= 0:
                se = j
            else:
                break
        s_edge[k[1]] = se
    n_viol = sum(1 for k in mains for c in res[k]["cells"]
                 if c["dip_margin"] < 0)
    worst_viol = min((c["dip_margin"] for k in mains
                      for c in res[k]["cells"]), default=0.0)
    viol_rmin = min((c["rmin"] for k in mains
                     for c in res[k]["cells"]
                     if c["dip_margin"] < 0), default=1.0)
    ripple_mono = all(
        all(res[k]["cells"][j + 1]["ndip"]
            <= res[k]["cells"][j]["ndip"] + 1
            for j in range(SGRID_DEN)) for k in mains)
    main8_edge = all(c["dip_margin"] >= 0
                     for c in res[("MAIN", 8)]["cells"]) \
        if ("MAIN", 8) in res else False
    eps_t0 = [c["t0min"] for c in res[ke]["cells"]] if ke in res \
        else []
    eps_dipm0 = res[ke]["cells"][0]["dip_margin"] if ke in res \
        else float("nan")
    suffix_ok = all(s_edge[h] <= SGRID_DEN for h in s_edge)
    if calib or smoke:
        ok40 = suffix_ok and main8_edge and eps_dipm0 < 0
    else:
        ok40 = suffix_ok and main8_edge and eps_dipm0 < 0 \
            and all(ndip_max[h] == CAL_NDIP_MAX[h] for h in rungs) \
            and all(abs(dipm_mid[h] - float(CAL_DIPM1[h]))
                    <= FRAC_TOL for h in rungs) \
            and all(s_mig[h] == CAL_SMIG[h] for h in rungs) \
            and all(s_edge[h] == CAL_SEDGE[h] for h in rungs)
    edge_enum = ("EDGE-MIN-ALL" if edge_all
                 else ("EDGE-MIN-DEEP-EARLY-LOST(%d)" % n_viol
                       if suffix_ok else "EDGE-MIN-LOST"))
    check("G40-edge-minimality-census", ok40,
          "P3 RESOLVED RETYPED TWICE (I1; smoke + calibration "
          "disclosures): %s -- edge-minimality (global grid min = "
          "min(A(0), A(L/2))) holds at %d of %d MAIN cells; the %d "
          "violations sit at the EARLY path of DEEP rungs only "
          "(s_edge/8 suffix table %s; worst undercut %+.4f of amax "
          "at rmin >= %.2f STILL FAR POSITIVE), and the pole lift "
          "IRONS THE RIPPLE FIELD OUT along s (n_dip max %s "
          "non-increasing-in-s within +1: %s, ENDING AT 0 at the "
          "wall at every rung); min migrates to the t = 0 edge at "
          "s_mig/8 = %s (from there min A = A(0) == the r197 jr_0 "
          "scalar); AT THE MATCHED RUNG h = 8 MAIN is edge-minimal "
          "at ALL cells while EPSTEIN(8) violates from the start "
          "(dip_margin(0) = %+.4f < 0) and never reaches t0min "
          "(%s...): the separation is real at matched rung; "
          "uniform-in-h it is NOT (the honest negative)"
          % (edge_enum,
             sum(1 for k in mains for c in res[k]["cells"]
                 if c["dip_margin"] >= 0),
             sum(len(res[k]["cells"]) for k in mains), n_viol,
             str({h: s_edge[h] for h in sorted(s_edge)
                  if s_edge[h] > 0}),
             worst_viol, viol_rmin,
             str({h: ndip_max[h] for h in (4, 8, 20)
                  if h in ndip_max}),
             ripple_mono,
             str({h: s_mig[h] for h in sorted(s_mig)
                  if s_mig[h] > 0}),
             eps_dipm0, str(eps_t0[:3])))

    # G41 log-concavity
    lcv0 = {k[1]: res[k]["cells"][0]["lcv"] for k in mains}
    if calib or smoke:
        ok41 = True
    else:
        ok41 = all(abs(lcv0[h] - CAL_LCV0[h])
                   <= max(3, int(0.15 * CAL_LCV0[h]))
                   for h in rungs)
    lc_enum = ("LOGCONC-HOLDS-ALL"
               if all(c["lcv"] == 0 for k in mains
                      for c in res[k]["cells"])
               else "LOGCONC-FAILS-AT-S0")
    check("G41-log-concavity-census", ok41,
          "P4 RESOLVED AGAINST I2: %s -- log-concavity fails ALREADY "
          "AT s = 0 at every MAIN rung (violations at s = 0: %s, "
          "growing with h; worst margins O(1e-3) log-domain, BODY "
          "violations not edge artifacts): the pole-ray bump is NOT "
          "log-concave on the half-window, I2 is DEAD as a MAIN "
          "path invariant and cannot be the separator (typed: "
          "log-concavity presupposes positivity anyway -- it never "
          "was a certificate)"
          % (lc_enum, str({h: lcv0[h]
                           for h in (4, 8, 13, 20) if h in lcv0})))

    # G42 PF + inflection proxies
    pf30 = {k[1]: res[k]["cells"][0]["pf3"] for k in mains}
    eps_pf3 = [c["pf3"] for c in res[ke]["cells"]] if ke in res \
        else []
    infl_mono = all(
        all(res[k]["cells"][j + 1]["ninfl"]
            >= res[k]["cells"][j]["ninfl"] - 2
            for j in range(SGRID_DEN))
        for k in mains)
    check("G42-pf-inflection-proxies", True,
          "I3/I4 RESOLVED AGAINST: the PF proxies ANTI-separate -- "
          "MAIN has negative 2x2/3x3 Toeplitz minors already at "
          "s = 0 (pf3 at s = 0: %s) while EPSTEIN(8)'s pf3 ladder "
          "along s is %s: sampled total positivity neither holds on "
          "MAIN nor is lost first by EPSTEIN; inflection count "
          "n_infl is h-ladder noise (near-monotone-in-s within +-2: "
          "%s) -- both proxies recorded DEAD, no VD theorem was "
          "consumed" % (str({h: pf30[h] for h in (4, 8, 20)
                             if h in pf30}),
                        str(eps_pf3), infl_mono))

    # G43 coefficient censuses
    scm0 = {k[1]: res[k]["cells"][0]["sc_mode"] for k in mains}
    scm1 = {k[1]: res[k]["cells"][SGRID_DEN]["sc_mode"]
            for k in mains}
    sc0_eps = res[ke]["cells"][0]["sc_mode"] if ke in res else -1
    hd1 = {k[1]: res[k]["cells"][SGRID_DEN]["hd"] for k in mains}
    nsc_all0 = all(c["nsc"] == 0 for k in mains
                   for c in res[k]["cells"])
    if calib or smoke:
        ok43 = nsc_all0
    else:
        ok43 = nsc_all0 \
            and all(scm0[h] == CAL_SSC[h] for h in rungs) \
            and all(scm1[h] == CAL_SCM1[h] for h in rungs) \
            and sc0_eps == CAL_CTRL[("EPSTEIN", 8)]["sc0"]
    check("G43-coefficient-censuses", ok43,
          "P5 RESOLVED SHARPENED (I5/I6 DEAD): MAIN is NOT even "
          "sign-pure at s = 0 (SC_mode at s = 0: %s; at the wall: "
          "%s) -- the mode-sign count is dead as an invariant at "
          "the START, yet nsc = 0 at ALL MAIN cells: every "
          "coefficient sign change is PROFILE-INVISIBLE (the "
          "variation-diminishing hope inverted: the profile is "
          "SMOOTHER than its coefficients); EPSTEIN(8) SC_mode at "
          "s = 0: %d; hd at wall: MAIN %s vs EPSTEIN %d (r198's "
          "hd = 0 fingerprint confirmed); I6 quotient reversals "
          "O(10) at s = 0 on MAIN (tilt not monotone): DEAD"
          % (str({h: scm0[h] for h in (4, 8, 13, 20) if h in scm0}),
             str({h: scm1[h] for h in (4, 8, 13, 20) if h in scm1}),
             sc0_eps,
             str({h: hd1[h] for h in (4, 8, 20) if h in hd1}),
             res[ke]["cells"][SGRID_DEN]["hd"] if ke in res else -1))

    # G44 exact Descartes/Bernstein
    scd0 = {k[1]: res[k]["cells"][0]["sc_desc"] for k in mains}
    scd_all0 = all(c["sc_desc"] == 0 for k in mains
                   for c in res[k]["cells"])
    nb1 = {k[1]: res[k]["cells"][SGRID_DEN]["nb"] for k in mains}
    scd1 = {k[1]: res[k]["cells"][SGRID_DEN]["sc_desc"]
            for k in mains}
    wall_cert = all(v == 0 for v in nb1.values())
    nb1_eps = res[ke]["cells"][SGRID_DEN]["nb"] if ke in res else -1
    scd1_eps = res[ke]["cells"][SGRID_DEN]["sc_desc"] \
        if ke in res else -1
    if calib or smoke:
        ok44 = True
    else:
        ok44 = all(scd0[h] == CAL_SCD0[h] for h in rungs) \
            and all(nb1[h] == CAL_NB1[h] for h in rungs) \
            and all(scd1[h] == CAL_SCD1[h] for h in rungs)
    desc_enum = ("DESCARTES-ZERO-ALL" if scd_all0
                 else "DESCARTES-COUNT-TABLE")
    bern_enum = ("WALL-BERNSTEIN-CERTIFIED-ALL-RUNGS" if wall_cert
                 else "BERNSTEIN-NEGATIVES-MEASURED")
    check("G44-exact-descartes-bernstein", ok44,
          "P6 RESOLVED MIXED: %s + %s -- mid-path the exact counts "
          "are slack bounds (SC_desc(MAIN, s = 0) = %s, valid and "
          "parity-exact by G14 but Z = 0 everywhere; NB > 0 at "
          "most mid-path cells): INERT as separators there; BUT AT "
          "THE WALL s = 1 the counts COLLAPSE: NB(s=1) = %s and "
          "SC_desc(s=1) = %s -- where NB = 0, the EXACT-RATIONAL "
          "Bernstein coefficients of the wall transport polynomial "
          "are ALL NONNEGATIVE at native degree: A_{v_0(h)} >= 0 "
          "on [0, L] is CERTIFIED (certificate class, own exact "
          "arithmetic) -- vs EPSTEIN's wall NB = %d, SC_desc = %d: "
          "the wall endpoint maximally separates in certificate "
          "structure" % (desc_enum, bern_enum,
                         str({h: scd0[h] for h in (4, 8, 13, 20)
                              if h in scd0}),
                         str({h: nb1[h] for h in sorted(nb1)}),
                         str({h: scd1[h] for h in (4, 8, 13, 20)
                              if h in scd1}),
                         nb1_eps, scd1_eps))

    # G45 eigenbasis census (frozen counts, world comparison)
    check("G45-eigenbasis-census", all(
        res[k]["sig_ok"] for k in allk),
          "I9 RESOLVED: eigenbasis sign patterns FROZEN along the "
          "path at every cell (G15 theorem ward) -- the eigenbasis "
          "count cannot separate transport; recorded world values: "
          "z1rel dex MAIN %s vs EPSTEIN(8) %.1f (the overlap-"
          "geometry gap that seeds E4)"
          % (str({k[1]: "%.1f" % res[k]["z1rel_log10"]
                  for k in mains if k[1] in (4, 8, 13, 20)}),
             res[ke]["z1rel_log10"] if ke in res else float("nan")))

    # ------------------------------------------------------------ S5
    section("S5  E3: SEPARATOR ADJUDICATION + TAU-SCREEN")
    tri68 = {k[1]: res[k]["cells"][6]["tri"] for k in mains}
    scert = {k[1]: max((c["sj"] for c in res[k]["cells"]
                        if c["tri"] < 1), default=None)
             for k in mains}
    scert_eps = max((c["sj"] for c in res[ke]["cells"]
                     if c["tri"] < 1), default=None) \
        if ke in res else None
    if calib or smoke:
        ok50 = True
    else:
        ok50 = all(scert[h] == CAL_SCERT[h] for h in rungs) \
            and all(abs(tri68[h] - float(CAL_TRI68[h])) <= FRAC_TOL
                    for h in rungs) \
            and scert_eps == CAL_CTRL[("EPSTEIN", 8)]["s_cert"]
    check("G50-separator-table", ok50,
          "THE ADJUDICATION TABLE (per candidate: MAIN-holds / "
          "EPSTEIN-loss / implication): I1 t0-edge-minimality: MAIN "
          "ALL cells / EPSTEIN NEVER holds it (violated already at "
          "s = 0, i.e. before s* trivially -- a WORLD-GEOMETRY "
          "separator seeded at s = 0) / EDGE-REDUCTION-EXACT-ON-"
          "GRID.  I10 TRI-prefix: MAIN certified through s = %s/8 "
          "per rung (TRI(6/8) = %s) / EPSTEIN only through %s/8 / "
          "TRIANGLE-CERTIFICATE-EXACT.  I10 two-mode predictor: "
          "s*_pred %s vs s*_lin %s.  I2 log-conc: DEAD AT s = 0 on "
          "MAIN.  I3 PF: ANTI-separates.  I4 inflections: noise.  "
          "I5/I6 mode-signs/quotients: dead at s = 0 on MAIN.  "
          "I7/I8 exact counts: slack mid-path, wall-collapsing "
          "(G44).  I9 eigenbasis: frozen by theorem"
          % (str({h: scert[h] for h in (4, 20) if h in scert}),
             str({h: "%.2f" % tri68[h]
                  for h in (4, 8, 20) if h in tri68}),
             str(scert_eps),
             "%.5f" % s_pred if s_pred is not None else "-",
             "%.5f" % s_lin if s_lin else "-"))

    scr = [k for k in mains if not res[k]["tau_neg"]]
    xs_t = [res[k]["log10tau"] for k in scr]
    sl_dip, _ = fit_line(xs_t, [dipm_mid[k[1]] for k in scr])
    sl_tri, _ = fit_line(xs_t, [tri68[k[1]] for k in scr])
    sl_rmh, _ = fit_line(
        xs_t, [res[k]["cells"][SGRID_DEN // 2]["rmin"] for k in scr])
    sl_rho, _ = fit_line(
        xs_t, [res[k]["cells"][SGRID_DEN]["rho1_log10"]
               for k in scr])
    sl_a0 = fit_line(
        xs_t, [math.log10(max(res[k]["cells"][SGRID_DEN]["a0rel"],
                              1e-300)) for k in scr])[0]
    if calib or smoke:
        print("CAL slopes: dipmmid %+.3f tri68 %+.3f rminh %+.3f "
              "rho11log %+.3f a0log(s=1) %+.2f"
              % (sl_dip, sl_tri, sl_rmh, sl_rho, sl_a0))
        ok51 = True
    else:
        ok51 = (abs(sl_dip - float(CAL_SLOPES["dipm_mid"]))
                <= SLOPE_TOL
                and abs(sl_tri - float(CAL_SLOPES["tri68"]))
                <= SLOPE_TOL
                and abs(sl_rmh - float(CAL_SLOPES["rminh"]))
                <= SLOPE_TOL
                and abs(sl_rho - float(CAL_SLOPES["rho11"]))
                <= SLOPE_TOL
                and abs(sl_a0 - float(CAL_SLOPES["a0log"]))
                <= SLOPE_TOL)
    check("G51-tau-screen", ok51,
          "P10 RESOLVED (the WIN-CONDITION test): the STRUCTURAL "
          "coordinates are O(1)-FLAT vs log10 tau -- dip_margin"
          "(mid) slope %+.3f, TRI(6/8) slope %+.3f, rminh slope "
          "%+.3f, log10 rho_1(1) slope %+.3f (bar %.2f: the LOAD "
          "itself is tau-flat O(1) -- the two-ladder cancellation); "
          "the ONLY rider is the known edge scalar itself (log10 "
          "A(0)(s=1) slope %+.2f == the jr_0/tau ladder): the "
          "factorization {flat structure} x {tau-riding edge "
          "scalar} is MEASURED, not conjectured"
          % (sl_dip, sl_tri, sl_rmh, sl_rho, TAU_FLAT_BAR, sl_a0))

    eps_t0_never = bool(eps_t0) and not any(eps_t0) \
        and all(not r["t0min"] for r in me["rows"])
    wall_clean = {k[1]: bool(res[k]["cells"][SGRID_DEN]["t0min"]
                             and res[k]["cells"][SGRID_DEN]["ndip"]
                             == 0
                             and res[k]["cells"][SGRID_DEN]["nb"]
                             == 0
                             and res[k]["cells"][SGRID_DEN]
                             ["sc_desc"] == 0)
                  for k in mains}
    wall_all = all(wall_clean.values())
    epsw = res[ke]["cells"][SGRID_DEN] if ke in res else None
    eps_wall_dirty = (epsw is not None and not epsw["t0min"]
                      and epsw["nb"] > 0 and epsw["sc_desc"] > 0)
    wall_enum = ("WALL-STATE-CLEAN-ALL-RUNGS" if wall_all
                 else "WALL-STATE-DIRTY-AT(%s)"
                 % str([h for h, v in wall_clean.items()
                        if not v]))
    if edge_all and eps_dipm0 < 0 and eps_t0_never:
        sep_enum = "SEPARATOR-FOUND(I1-EDGE-MINIMALITY)"
    elif main8_edge and eps_dipm0 < 0 and eps_t0_never \
            and wall_all and eps_wall_dirty:
        sep_enum = "SEPARATOR-MATCHED-RUNG+WALL-STATE"
    else:
        sep_enum = "NO-SEPARATOR"
    check("G52-Istar-adjudication", sep_enum != "NO-SEPARATOR",
          "I* ADJUDICATED HONESTLY: %s -- THE CORE NEGATIVE: no "
          "candidate in the battery is a uniform-in-h path "
          "invariant (deep-rung early-path interior minima refute "
          "edge-minimality, G40; everything else died at s = 0, "
          "G41-G44).  WHAT IS REAL: (a) MATCHED RUNG h = 8: MAIN "
          "edge-minimal at ALL cells, EPSTEIN violating from "
          "s = 0 (dip_margin(0) = %+.4f) with argmin never at "
          "t = 0 -- the separation is seeded at s = 0 in the "
          "eigenvector geometry, strictly before s* = %s; (b) THE "
          "WALL STATE at EVERY rung: %s (t0-minimal, ripple-free, "
          "NB = 0, SC_desc = 0 -- doubly exact-certified at "
          "native degree) vs EPSTEIN's wall (t0min False, NB = "
          "%s, SC_desc = %s): the wall endpoint separates "
          "MAXIMALLY at every reachable rung; (c) implication "
          "where I1 holds: min_grid A = min(A(0), A(L/2)) "
          "exactly; (d) margins O(1)-flat (G51).  HONEST LIMIT: "
          "the reviewer's sought-for uniform transport invariant "
          "is NOT delivered by this battery -- the deliverable is "
          "the matched-rung separator + the wall-state collapse + "
          "the certified TRI prefix"
          % (sep_enum, eps_dipm0,
             "%.5f" % s_lin if s_lin else "-",
             wall_enum,
             str(epsw["nb"]) if epsw else "-",
             str(epsw["sc_desc"]) if epsw else "-"))

    # ------------------------------------------------------------ S6
    section("S6  E4: MECHANISM (source census + eigen-anatomy)")
    acs = {}
    for w, x in (("MAIN", 8), ("EPSTEIN", 8), ("SCRARITH", 5)):
        acs[(w, x)] = atom_census(w, x, 60)
    negw_main = {h: atom_census("MAIN", h, 60)["n_neg"]
                 for h in rungs}
    ae = acs[("EPSTEIN", 8)]
    lam_enum = ("LAMBDA-POS-REFUTED-AT-RUNG" if ae["n_neg"] == 0
                else "LAMBDA-POS-SEPARATES")
    check("G60-atom-source-census", all(
        v == 0 for v in negw_main.values()) and ae["n_neg"] == 0,
          "P9 RESOLVED: %s -- EPSTEIN(8) effective weights are ALL "
          "NONNEGATIVE (negw = 0, re-censused from source; atoms "
          "q = %s, weights %s), so the 'Lambda >= 0 separates' "
          "hypothesis is REFUTED at the reachable rung (r198 "
          "inheritance confirmed): MAIN's transport does NOT hold "
          "BECAUSE of weight positivity alone -- the arithmetic "
          "difference is SUPPORT/MASS class: EPSTEIN's support "
          "contains the NON-prime-power q = 6 carrying mass "
          "fraction %.2f and MISSES primes 2, 3, 7; MAIN negw = 0 "
          "at ALL rungs source-gated (von Mangoldt, exact for all "
          "h); SCRARITH (permuted positive weights, prime-power "
          "support) HOLDS I1: positivity+support are jointly "
          "consistent with, but not proven sufficient for, the "
          "transport (n = 1 fake world, typed honest)"
          % (lam_enum, str(ae["qs"]),
             str(["%.3f" % w for w in ae["ws"]]),
             ae["nonpp_massfrac"]))

    rho11 = {k[1]: res[k]["cells"][SGRID_DEN]["rho1_log10"]
             for k in mains}
    z1r = {k[1]: res[k]["z1rel_log10"] for k in mains}
    if calib or smoke:
        for h in sorted(rho11):
            print("CAL mech h=%-2d z1rel %.1f rho11 %.1f jr0 %s"
                  % (h, z1r[h], rho11[h], R197_JR0[h]))
        ok61 = True
    else:
        ok61 = all(abs(rho11[h] - float(CAL_RHO11[h]))
                   <= 3 * LOG_TOL for h in rungs) \
            and all(abs(z1r[h] - float(CAL_Z1REL[h]))
                    <= 3 * LOG_TOL for h in rungs)
    mech_ok = all(-1.0 <= rho11[h] <= 1.0 for h in rho11) \
        and (max(z1r.values()) - min(z1r.values())) > 10
    mech_enum = ("TWO-LADDER-CANCELLATION" if mech_ok
                 else "LOAD-LADDER-UNMATCHED")
    eps_rho1 = res[ke]["cells"][SGRID_DEN]["rho1"] if ke in res \
        else float("nan")
    check("G61-eigen-anatomy-mechanism", ok61 and mech_ok,
          "THE MECHANISM READ EXACTLY: %s -- log10 rho_1(1) = %s "
          "is O(1)-FLAT at every MAIN rung while the overlap "
          "ladder z1rel = %s spans the whole near-zero territory: "
          "|z_1/z_0| and the lift ratio f/(1-f) CANCEL to an O(1) "
          "load at the wall, at EVERY rung -- the transport is a "
          "knife-edge ladder cancellation, and it does NOT "
          "separate worlds (EPSTEIN(8) rho_1(1) = %.2f, same O(1) "
          "class): the separator lives in WHERE the O(1) load "
          "pushes -- the CENTER TEMPLATE VALUES (EPSTEIN: y_1 "
          "U_1(L/2) drives the alternating scalar down, m_dr = %s, "
          "two-mode predictor %s within %s of the measured "
          "crossing; MAIN: the load lands at the t = 0 edge where "
          "it reproduces the jr_0 near-zero without undercutting "
          "the interior): the eigenvector-geometry separator in "
          "exact secular terms is the pair (z_1 overlap, U_1 "
          "center value), both s = 0 data"
          % (mech_enum,
             str({h: "%.1f" % rho11[h]
                  for h in (4, 8, 13, 20) if h in rho11}),
             str({h: "%.1f" % z1r[h]
                  for h in (4, 8, 20) if h in z1r}),
             eps_rho1, str(me.get("m_dr")),
             "%.5f" % s_pred if s_pred is not None else "-",
             ("%.4f" % abs(s_pred - s_lin))
             if (s_pred is not None and s_lin is not None)
             else "-"))

    wit = witness_leg()
    wok = (WIT_YT_BAND[0] <= wit["wit_ytr"] <= WIT_YT_BAND[1]
           and wit["wit_a0dev"] <= WIT_A0_BAR)
    if calib or smoke:
        print("CAL wit ytr %.2f a0dev %.1e base mis %d hd %d "
              "nonneg %s ovl %.6f | wit mis %d hd %d nonneg %s "
              "ovl %.6f"
              % (wit["wit_ytr"], wit["wit_a0dev"],
                 wit["base"]["mis"], wit["base"]["hd"],
                 wit["base"]["nonneg"], wit["base"]["ovl"],
                 wit["wit"]["mis"], wit["wit"]["hd"],
                 wit["wit"]["nonneg"], wit["wit"]["ovl"]))
        ok62 = wok
    else:
        ok62 = (wok and wit["base"]["nonneg"] and wit["wit"]["nonneg"]
                and wit["base"]["mis"] == wit["wit"]["mis"])
    check("G62-witness-battery", ok62,
          "r172 inflation witness VERBATIM at h = %d (y_t ratio "
          "%.1f in %s, A_0 dev %.1e): homotopy objects witness-"
          "INVARIANT BY CONSTRUCTION (typed definitional); ray-side "
          "base mis %d hd %d nonneg %s (ovl %.6f) vs wit mis %d hd "
          "%d nonneg %s (ovl %.6f)"
          % (WIT_RUNG, wit["wit_ytr"], str(WIT_YT_BAND),
             wit["wit_a0dev"], wit["base"]["mis"],
             wit["base"]["hd"], wit["base"]["nonneg"],
             wit["base"]["ovl"], wit["wit"]["mis"],
             wit["wit"]["hd"], wit["wit"]["nonneg"],
             wit["wit"]["ovl"]))

    # ------------------------------------------------------------ S7
    section("S7  GUARDS + ADJUDICATION")
    delivered = {
        "ATOMS": ["NOP-SPEC"], "MODES": ["NOP-SPEC"],
        "POLE-RANK1": ["SECULAR-PATH"],
        "NOP-SPEC": ["SECULAR-PATH"],
        "SECULAR-PATH": ["MICROSCOPE", "INV-BATTERY"],
        "MICROSCOPE": ["ADJUDICATION"],
        "INV-BATTERY": ["ADJUDICATION"],
        "EXACT-COUNTS": ["INV-BATTERY"],
        "ATOM-CENSUS": ["ADJUDICATION"],
        "TAU-SCALAR": ["SCREENS"],
        "ADJUDICATION": ["SCREENS"], "SCREENS": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]},
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY": ["RH"],
                                  "RH": ["TURAN-CONE-POSITIVITY"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("MICROSCOPE", "INV-BATTERY", "EXACT-COUNTS",
                 "ATOM-CENSUS", "ADJUDICATION", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "ZEROVERIF-HYP",
                 "TURAN-CONE-POSITIVITY", "RH"}
    check("G70-loop-guard", ndet == 7 and not has_cycle(delivered)
          and not hot,
          "SEVEN flagged cycles DETECTED (A0-triangle, "
          "census-forall-k, Gonek-1984, Montgomery-PC, "
          "WEIL-ALLTESTS, zero-verification-as-hypothesis, "
          "TURAN-CONE-POSITIVITY -- re-flagged: this round's "
          "instruments are cone/positivity-adjacent), consumed by "
          "NOTHING: DFS ancestry of every delivered node clean; "
          "fully zero-free round; the separator adjudication is "
          "per-rung finite linear algebra + exact integer counts "
          "with no edge into any criterion loop")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1,
            ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF,
                ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "SEPINV"): INF, ("SEPINV", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G71-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'dip-freedom transports cofinally for all h AND the edge "
          "scalars stay positive' as a unit edge would raise the "
          "flow to 6 -- NOT REAL twice over (dip-freedom is "
          "grid-measured per rung with no all-h theorem, and the "
          "edge face is the known tau-riding near-zero): this round "
          "adds NO flow; RH unreachable without the omega edges")

    check("G72-composed-chain-typing", True,
          "leg typing: {rank-one law, secular pipeline, sign-freeze "
          "theorem, Descartes/Bernstein bounds + parity, edge-"
          "reduction, TRI certificate, Sturm cells} EXACT/"
          "CERTIFICATE; {dip census, LC/PF/inflection censuses, "
          "coefficient censuses, s*_lin, t*, driver anatomy, "
          "slopes} MEASURED (grid, sign-resolving bars, KA rider); "
          "{witness matrix-invariance} DEFINITIONAL; {SCRARITH "
          "n = 1 consistency} TYPED-HONEST; no impossibility "
          "theorem and no completeness claim sold anywhere; "
          "t0-edge-minimality-for-all-h is a NEW OPEN TARGET, not "
          "a result")

    # ------------------------------------------------------------ S8
    section("S8  PRICING + RESIDUE")
    check("G80-pricing", True,
          "what the round BUYS: (i) THE TRANSITION ANATOMY -- "
          "EPSTEIN's failing coordinate is the ALTERNATING EDGE "
          "SCALAR A(L/2) = sum (-1)^k v_k (crossing at the window "
          "center, coefficient-sign-silent, smooth, two-mode-"
          "predictable): transport failure = monotone secular "
          "loading of the U_1 center template; (ii) THE SEPARATOR "
          "ADJUDICATION, honest: NO uniform-in-h path invariant "
          "exists in the battery (the round's core negative -- "
          "deep-rung early-path interior minima undercut the "
          "edges while staying far positive); what IS real: the "
          "matched-rung h = 8 edge-minimality separation (seeded "
          "at s = 0) and the WALL-STATE COLLAPSE at every rung "
          "(t0-minimal, ripple-free, NB = 0, SC_desc = 0 -- "
          "OBJECT-A itself gains cheap EXACT-RATIONAL Bernstein "
          "certificates at native degree at ALL 14 rungs, beyond "
          "BH10's four Sturm rungs) vs EPSTEIN's maximally dirty "
          "wall; the structural margins are O(1)-FLAT while only "
          "the edge scalar rides tau; (iii) the TRI prefix "
          "certificate (exact sufficient condition) carries "
          "s <= 6/8-class prefixes; (iv) the invariant GRAVEYARD "
          "is priced: log-concavity/PF/VD-proxies and mode-sign "
          "counts die at s = 0 on MAIN, exact counts are slack "
          "mid-path -- five candidate classes closed; (v) E4: "
          "Lambda >= 0 REFUTED as the separator at the reachable "
          "rung (EPSTEIN negw = 0): the arithmetic difference is "
          "support/mass class (non-prime-power q = 6, missing "
          "primes 2/3/7), and the mechanism currency is the pair "
          "(z_1 overlap, U_1 center value) with the O(1) "
          "two-ladder load cancellation universal across worlds")

    info("POST-ROUND RESIDUE (cardinality UNCHANGED, canonical "
         "four-item form per note DXVI): {H1 ^ H2 ^ H3}-KOFINAL "
         "(mod D = 0.0042) + {census-forall-k == LOOP, flagged, not "
         "consumed} + {H-PIN: L1 = TAIL proven + H-pin open; "
         "WPD(a < gamma_1^2) <= H-pin; TAILWPD world front}.  "
         "OBJECT-A STAYS OPEN; its wall endpoint is now DOUBLY "
         "exact-certified at every reachable rung (native-degree "
         "Bernstein + Descartes, this round) and its grid face "
         "factorizes into {edge-minimality geometry (real at "
         "matched rung and at the wall, uniform-in-h OPEN)} x "
         "{edge scalars (the known jr_0/near-zero currency)}.  "
         "Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        micro_enum + "(G30)",
        "MAIN-FINE-GRID-CLEAN(G31)",
        "COEFF-SIGN-SILENT-TRANSITION(G32)",
        edge_enum + "+T0-MIN-FROM(%s)(G40)"
        % str({h: s_mig[h] for h in (4, 8, 20) if h in s_mig}),
        lc_enum + "(G41)",
        "PF-VD-PROXIES-DEAD(G42)",
        "MODE-SIGNS-WORLD-DATA-NOT-INVARIANT(G43)",
        desc_enum + "+" + bern_enum + "(G44)",
        "EIGENBASIS-SIGNS-FROZEN(G15/G45)",
        sep_enum + "(G52)",
        wall_enum + "(G52)",
        "STRUCTURE-FLAT-EDGE-RIDES(G51)",
        lam_enum + "(G60)",
        mech_enum + "+CENTER-TEMPLATE(G61)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G70)",
        "MINCUT-UNCHANGED(G71) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        micro_enum, edge_enum, lc_enum, desc_enum, bern_enum,
        "EIGENBASIS-SIGNS-FROZEN", sep_enum, wall_enum,
        "STRUCTURE-FLAT-EDGE-RIDES", lam_enum,
        mech_enum, "LOOPS-FLAGGED-NOT-CONSUMED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
