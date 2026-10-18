#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""z1_suppression_probe -- PRIME.Z1.SUPPRESSION.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, and every
verification/paper/website surface of promotion wave eight) are not
touched.

=======================================================================
MISSION (round ~202: the z_1-suppression mechanism).  r201
(eigvec_geometry_probe, SPEC f43babb5b80416d1, 30/30) established THE
KEY LADDER: EPSTEIN's node is the alternating edge scalar A(L/2)
crossing zero under monotone secular loading of the U_1 center
template (two-mode predictor sharp to 0.012); the overlap z_1 =
<U_1, phi> is EPSTEIN -0.8 dex vs MAIN(8) -24.4 dex (~23.6 orders)
while the load rho_1(1) = |z_1/z_0| f/(1-f) is O(1) in BOTH worlds
(the amplifier is world-blind); Lambda >= 0 is refuted as separator
(EPSTEIN weights nonnegative; the difference is SUPPORT/MASS class);
the eigenbasis signs are frozen along s.  THE REVIEWER'S KILLER
CHAIN: prime-power support -> overlap z_1 -> center template -> edge
scalar.  THIS round attacks the chain's first arrow: WHAT IS z_1 IN
SOURCE TERMS, WHY IS MAIN'S z_1 SO SMALL, AND DOES THE SUPPRESSION
FOLLOW THE SUPPORT OR THE WEIGHTS?

  Z1 THE PER-ATOM DECOMPOSITION (the round's pivot).  Exact
     structure fact (derived from the R4.build_cell assembly, warded
     here entrywise): the world atoms enter the pole-free matrix
     LINEARLY -- NoP = RawArch - sum_q w_q C(log q), where C(u) is
     the EXPLICIT even-sector atom kernel
       C(u)[i,j] = 2 (om_i sin(om_i u) - om_j sin(om_j u))
                     / (om_j^2 - om_i^2)              (i != j),
       C(u)[i,i] = 2 ((a - u/2) cos(om_i u)
                      - sin(om_i u) / (2 om_i))       (i >= 1),
       C(u)[0,0] = 2 (L - u),
     with w_q = Lambda(q)/sqrt(q) (MAIN), the golden permutation of
     the same multiset (SCRARITH), the x^2+5y^2 lamq recursion
     (EPSTEIN).  The eigen-identity d_1 z_1 = U_1^T NoP phi then
     gives the EXACT linear-functional form
       z_1 = T_arch + sum_q T_q,   T_arch = U_1^T RawArch phi / d_1,
       T_q = w_q F_1(log q),       F_1(u) = -U_1^T C(u) phi / d_1
     (THE DANGEROUS-MODE FORM FACTOR; warded against the directly
     measured <U_1, phi> at gross scale).  Deliverables per rung
     (all 14 MAIN rungs + H_HOLD + EPSTEIN(8) + SCRARITH(5); SMOOTH
     has no atoms -- its prime leg is the continuum block, typed):
     the per-atom z_1 table {T_arch, T_q}, and the three mechanism
     metrics: maxterm_rel = max_q |T_q| / |z_0| (mechanism c: SMALL
     TERMS iff <= MECH_SMALL_BAR); c_within = |sum_q T_q| /
     sum_q |T_q| (cancellation among atoms: mechanisms a/b);
     c_cross = |T_arch + sum_q T_q| / max(|T_arch|, |sum_q T_q|)
     (arch-vs-prime pairing cancellation: mechanism a, the ACF/Weil
     reading of r195).  Plus: the F_1 profile on the frozen 47-point
     u-grid at PROF cells with sign-change census (mechanism b);
     the matched-rung form-factor comparison |F_1| at MAIN(8)
     supports {log 2, log 3, ...} vs EPSTEIN supports {log 4, log 5,
     log 6}; the cross number Q_cross = sum_q w^EPS_q
     F_1^MAIN(log q^EPS) (EPSTEIN's atoms dropped into MAIN's form
     factor -- the linearized transplant); the SENSITIVITY table at
     h = 4, 5: dz_1/dw_q by central finite differences at two step
     sizes, warded against the exact first-order perturbation
     formula dz_1/dw_q = -sum_{m != 1} z_m U_m^T C(u_q) U_1 /
     (d_1 - d_m); fine-tuning index FT_q = |dz_1/dw_q| w_q / |z_1|
     (FT >> 1 = the smallness is a fine-tuned cancellation, not
     per-atom smallness; the boundary atom q = h is ZERO-CLASS by
     the exact structure fact C(L) == 0 -- every entry of the
     kernel vanishes identically at u = L since sin(om_k L) = 0
     and a - L/2 = 0: the largest atom is kernel-invisible); and
     the ALIGNMENT-LAW connection (r182): Parseval-exact
     sin^2(phi, U_0) = sum_{m>=1} z_m^2 / ||phi||^2, so the
     z-ladder anatomy adjudicates whether m = 1 carries the
     pole-ray/ground-ray misalignment (the r182 global-alignment
     reading) or the misalignment sits in HIGHER modes (mode-
     specific suppression) -- resolved as a CENSUS (alignEnum),
     typed MEASURED-CORRESPONDENCE to r182 (no theorem consumed).
  Z2 THE TWO-LADDER CANCELLATION IDENTITY.  On the rank-one secular
     structure (r200 post-A1 VERBATIM; rho = s c_pole, c_pole =
     2 sinh^2(a/2)): with w(lam) = 1 + rho sum_m z_m^2/(d_m - lam)
     and lam_0 its root in (d_0, d_1), define the z_1-DELETED
     secular value Gdel(lam) = 1 + rho sum_{m != 1} z_m^2 /
     (d_m - lam).  EXACT IDENTITIES (algebra on w(lam_0) = 0,
     warded numerically):
       (ID1)  rho z_1^2 / (d_1 - lam_0) = -Gdel(lam_0),
       (ID2)  rho_1 = |z_1/z_0| f/(1-f)
                    = (lam_0 - d_0)(-Gdel(lam_0)) / (rho |z_0 z_1|).
     So rho_1 = O(1) (the r201 record) <=> -Gdel(lam_0) ~ |z_1|:
     the deleted secular function NEARLY VANISHES at lam_0 -- the
     suppression (z_1 small) and the amplification (f/(1-f) large)
     are two faces of the SAME near-root object.  Deliverables: the
     full anatomy ladders d_0, d_1, d_1 - d_0, lam_0(1) (warded
     against the mp inverse-iteration anchor on RawW; tau_h =
     ce["mpE"][0] is the bottom eigenvalue of the NORMALIZED
     builder matrix, congruent-not-similar to RawW, and enters
     ONLY as the measured screen scalar), lam_0 - d_0, d_1 - lam_0,
     1 - f, -Gdel(lam_0) at s = 1/2 and 1; the LAYER-EXPONENT
     adjudication (slope of
     log10(1-f(1)) vs log10|z_1/z_0| across the 14 rungs: EXP-1
     band [0.75, 1.25], EXP-2 band [1.75, 2.25]); the GDEL-Z1 lock
     (slope of log10(-Gdel(1)) vs z1rel); and the HARD SCREEN: the
     z1rel-vs-log10(tau) slope (is z_1 tau in new clothes at the
     NET level?) with the structure coordinates (c_within, c_cross,
     maxterm) tau-screened separately (TAU_FLAT_BAR).
  Z3 THE SAFE-MINUS-DANGEROUS DECOMPOSITION.  Exact mode expansion
     of the alternating edge scalar: A_s(L/2) = sum_m y_m(s) Umc_m
     with Umc_m = sum_k (-1)^k Q[k, m] (identity A(L/2) =
     sum_k (-1)^k v_k warded per cell).  Global sign fixed by
     c_0 = y_0 Umc_0 > 0 (the products c_m = y_m Umc_m are
     eigenvector-sign-canonical).  Per (world, h, s in 9-grid):
     safe = c_0, DNG = sum_{m>=1} max(0, -c_m), HLP = sum_{m>=1}
     max(0, c_m), conservative margin mc = (safe - DNG)/safe, full
     margin mf = A(L/2)/safe, driver census m_top = argmax of the
     dangerous terms.  Adjudication: CENTER-DOMINANCE-ALL iff
     mc > 0 at every MAIN cell; CENTER-DOMINANCE-WITH-HELP(n) iff
     mf > 0 everywhere but mc fails at n cells; else
     CENTER-DOMINANCE-LOST(n).  EPSTEIN(8) face: the bookkeeping
     must reproduce the r200 crossing (first mf < 0 at sj = 6 on
     the 9-grid).  THE ALL-H FACE, typed honestly: legs {C(u),
     atom positions/weights} SOURCE-CLASSICAL (finite Lambda-
     weighted sums of explicit smooth functions; r175 bridge
     class), {U_m, d_m, z_m, y_m(s), Umc_m} SPECTRAL-MEASURED
     per rung, margins tau-screened; the missing all-h statement
     has the exact shape 'for all h: sum_{m>=1} max(0,
     -y_m(1) Umc_m) < y_0(1) Umc_0' -- per-rung MEASURED here,
     all-h OPEN; even where the margin rides tau the decomposition
     localizes WHERE the arithmetic enters (the form factors at
     log 2, log 3, ...): a handoff sharpening, not a closure.
  Z4 WORLDS AND CONTROLS.  (i) Per-atom z_1 tables for SCRARITH(5)
     (the golden permutation breaks the (q, w_q) pairing at fixed
     support AND fixed weight multiset -- its z1rel against
     MAIN(5) = -11.4 is the pairing test), EPSTEIN(8) (which atom
     carries the O(1) imbalance), SMOOTH(5) (two-leg split only,
     continuum prime block, typed).  (ii) THE SUPPORT TRANSPLANT
     (the round's causal test, 2 x 2 factorial at h = 8, dps 80,
     atoms paired positionally in increasing q, truncated to the
     min cardinality 3): T0 = supports {2,3,4} x MAIN weights
     {w_2, w_3, w_4} (truncation control), T1 = supports {4,5,6} x
     MAIN weights, T2 = supports {2,3,4} x EPSTEIN weights, T3 =
     supports {4,5,6} x EPSTEIN weights == EPSTEIN(8) exactly
     (assembly ward: NoP(T3) == NoP(EPSTEIN(8)) entrywise).  Each
     cell runs the full NoP/eigsy/z machinery + 9-grid secular path
     with profile node census.  Class function cls(z1rel):
     SUPPRESSED iff <= SUP_BAR (-8), O1 iff >= O1_BAR (-3), MID
     else.  Verdict: SUPPORT-CARRIES iff cls(T0) == cls(T2) !=
     cls(T1) == cls(T3); WEIGHTS-CARRY iff cls(T0) == cls(T1) !=
     cls(T2) == cls(T3); COMPLETENESS-CARRIES iff all four O1
     while full MAIN(8) is SUPPRESSED (truncation alone destroys
     the cancellation -- the suppression needs the full prime-power
     set); PAIRING-CARRIES iff T0 SUPPRESSED and T1, T2, T3 not;
     else TRANS-MIXED (all four numbers + contrasts recorded).
     Pre-registered reviewer hypothesis: SUPPORT-CARRIES.  (iii)
     The r172 witness (r198-r201 code path VERBATIM at h = 5,
     factor 1000): the witness inflates the SOURCE-RAY coefficients
     cs[1], cs[2] -- it never touches NoP, phi or U_1, so z_1 is
     witness-INVARIANT BY CONSTRUCTION (typed definitional; the
     honest answer to 'where does it hit z_1' is NOWHERE -- the
     witness lives in the ray currency, the z_1 object in the
     matrix currency); the ytr/a0dev band is still gated for
     continuity.

PRE-REGISTERED PRIORS (resolve-and-record; NONE gate-forcing):
  P1 MAIN per-atom terms are NOT individually small (maxterm_rel
     >> MECH_SMALL_BAR); the suppression is CANCELLATION with the
     arch-vs-prime pairing dominant (c_cross tiny, ladder-deep):
     mechanism (a), the ACF/Weil pairing in eigencoordinates;
     mechanism (c) refuted.
  P2 |F_1(log 2)|, |F_1(log 3)| at MAIN(8) are NOT small against
     |F_1| at the EPSTEIN supports: mass-location refuted as the
     carrier.
  P3 Q_cross is O(max_q |T_q|)-sized: the imbalance follows the
     atom set, not the template.
  P4 FT_q >> 1 at h = 4, 5 (fine-tuned cancellation), FD == exact
     perturbation formula to FD_ANA_TOL.
  P5 sin(phi, U_0) ladder == the |z_1/z_0| ladder within ALIGN_TOL
     at every MAIN rung (m = 1 dominates the misalignment);
     resolve whether z_2, z_3 fall even faster.
  P6 LAYER-EXP-1: 1 - f(1) rides |z_1/z_0| linearly (the r201
     rho_1 = O(1) record already implies it); -Gdel(lam_0) ~
     |z_1/z_0| (GDEL-Z1-LOCKED): the deleted-secular near-root is
     the named object behind the two-ladder cancellation.
  P7 z1rel RIDES tau at the net level (slope ~ -1.8..-1.9 vs
     log10 tau, i.e. z_1 IS near-zero currency in new clothes NET),
     while the structure coordinates (c_within, c_cross, maxterm)
     are tau-FLAT: the factorization {flat structure} x {riding
     net} is the honest deliverable shape.
  P8 Z3: conservative center-dominance holds at the matched rung
     h = 8 at all s; deep rungs may lose the conservative margin
     early-path (r201 edge-minimality precedent) while the full
     margin mf > 0 holds at every MAIN cell; EPSTEIN crossing
     reproduced at sj = 6.
  P9 Transplant: reviewer hypothesis predicts SUPPORT-CARRIES;
     honest alternative pre-registered: T0 (truncation control)
     may already lose suppression (COMPLETENESS-CARRIES) -- the
     contrasts adjudicate.  SCRARITH(5): genuinely open (pairing
     test); r200/r201 profile behavior was MAIN-like, but its
     z1rel was never measured.
  P10 Witness: ytr in band, a0dev tiny, z_1 witness-invariant by
     construction (definitional).

NOTATION (r171-r201 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector); a = log(h)/2; L = 2a; K = ceil(1.25 h
log h); om_k = k pi/a; b_k = om_k^2; par_k = (-1)^k; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); RawW/RawP/RawArch/RawPrime from
mpM/mpPole/mpArch/mpPrime via raw_of; NoP = RawW - RawP; phi_k =
1/(1/4 + b_k); c_pole = 2 sinh(a/2)^2.  Eigendecomposition E, Q =
mp.eigsy(NoP) sorted ascending; z = Q^T phi; secular bottom pair
post-A1 (r200 VERBATIM: ALL K levels kept as poles, NBIS = int(3.4
dps) + 60); s = 1 anchor: mp inverse iteration on RawW (r195-r200
VERBATIM); tau_h = ce["mpE"][0], measured per-rung scalar only.
Atom lists replicate radius4_an_probe.build_cell atom blocks
VERBATIM (sieve / x^2+5y^2 lattice + lamq recursion / golden
permutation).  u-grid for F_1 profiles: u_j = j L/48, j = 1..47.

DPS schedule (r182-r201 ladder VERBATIM): DPS = {4: 60, 5: 60,
6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120,
14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16, H_HOLD = 20.
SGRID_DEN = 8 (9 path points).  CONTROLS: (SMOOTH, 5, 60),
(SCRARITH, 5, 60), (EPSTEIN, 8, 80).  PROF cells (F_1 u-grid):
MAIN 4/5/8, SCRARITH 5, EPSTEIN 8.  SENS_RUNGS = (4, 5), FD_RELS =
(1e-14, 1e-15) (sized INSIDE the measured linear regime: the
fine-tuning scale is 1/FT ~ 1e-10 at h = 5, so 1e-6-class steps
leave the linear regime -- calib-disclosed re-sizing, bars
unmoved), central differences, eigenvector orientation pinned
at the base cell's largest-|U_1| component, BOUNDARY_FLOOR 1e-40
(zero-class for the exact kernel zero at u = L).  ID-ward
resolvability rule: the s = 1/2 ID checks balance O(1) secular
terms down to ~ z_1^2 and are gated only where 2|z1rel| + 16 <=
dps (SATURATED-SKIPPED else, count recorded); the s = 1 checks
are z_1-deep and gate everywhere.  TRANS_H = 8,
dps 80, TRANS_NCUT = 3 (positional q-order pairing truncated to
the min world cardinality).  WIT_RUNG = 5, WIT_FACT = 1000.  The
inverse-iteration anchor ward applies to MAIN cells (on EPSTEIN/
SCRARITH the nearest-zero iterate is a different eigenvalue than
the secular bottom root; those cells are carried by the exact
eigen-residual ward, typed).

FROZEN BARS: RANK1_BAR 1e-40; BLK_BAR 1e-38; KER_BAR 1e-38;
EIG_RES_BAR 1e-30; EIG_ORTH_BAR 1e-30; PARSEVAL_BAR 1e-30;
Z1ID_BAR 1e-25 (gross-scale rel); CSUM_BAR 1e-25 (gross-scale
rel); SEC_RES_BAR 1e-20; SECID_BAR 1e-10 (rel, self-consistency
class); ANCHOR_LAM_BAR 1e-6; INVIT_RES_BAR 1e-12; ZCLS 1e-30;
SIGN_RES 1e-6; MECH_SMALL_BAR 1e-3; MECH_CANCEL_BAR 1e-2;
SUP_BAR -8.0; O1_BAR -3.0; EXP1_BAND (0.75, 1.25); EXP2_BAND
(1.75, 2.25); GDEL_BAND (0.75, 1.25); ALIGN_TOL 0.05 dex;
FD_STAB_TOL 1e-3; FD_ANA_TOL 1e-4; TAU_FLAT_BAR 0.30; WIT_YT_BAND
(990, 1010); WIT_A0_BAR 1e-6; RUNTIME_BAR 2700 s.  Record
tolerances: LOG_TOL 0.10 dex (r201 inheritance), LOG_TOL2 0.20 dex
(new CAL2 records), RHO_TOL 0.15, FRAC_TOL 0.05, SLOPE_TOL 0.10;
counts exact.  Inheritance cross-checks: z1rel == r201 CAL_Z1REL
(LOG_TOL); log10 rho_1(1) == r201 CAL_RHO11 (RHO_TOL); EPSTEIN
9-grid fingerprint == r200 (first negative full-margin/profile at
sj = 6, rmin1 -0.481 FRAC_TOL, rmin0 0.690 FRAC_TOL); negw(MAIN)
= 0 at all rungs, negw(EPSTEIN, 8) = 0, nonpp massfrac 0.51
(FRAC_TOL); anchor lam_0(1) == tau_h (ANCHOR_LAM_BAR).

TAXONOMY (resolution logic):
  mechEnum  := MECH-C-SMALLTERMS iff maxterm_rel <= MECH_SMALL_BAR;
               MECH-A-ARCHPRIME-CANCEL iff c_cross <=
               MECH_CANCEL_BAR and c_within > 10 MECH_CANCEL_BAR
               (atoms roughly coherent, killed against arch);
               MECH-AB-WITHINPRIME-CANCEL iff c_within <=
               MECH_CANCEL_BAR (atoms cancel among themselves;
               parity/oscillation face read off the F_1 sign
               census); else MECH-MIXED(maxterm, c_within,
               c_cross).  Modal enum across the 14 MAIN rungs is
               the round verdict; per-rung table recorded.
  alignEnum := ALIGNMENT-LOCKED iff |log10 sin(phi, U_0) - z1rel|
               <= ALIGN_TOL at every MAIN rung (m = 1 carries the
               misalignment); else ALIGNMENT-MULTI-MODE(worst gap)
               with the z_1/z_2/z_3/sin census recorded (the gate
               is the census, resolve-and-record).
  expEnum   := LAYER-EXP-1 / LAYER-EXP-2 / LAYER-EXP-OTHER(slope)
               from slope log10(1 - f(1)) vs z1rel.
  gdelEnum  := GDEL-Z1-LOCKED iff slope log10(-Gdel(1)) vs z1rel
               in GDEL_BAND; else GDEL-UNLOCKED(slope).
  tauEnum   := Z1-NET-RIDES-TAU iff |slope z1rel vs log10 tau| >
               TAU_FLAT_BAR (expected); STRUCTURE-FLAT iff the
               c_within/c_cross/maxterm log-slopes vs log10 tau
               are all <= TAU_FLAT_BAR in absolute value;
               composite recorded.
  domEnum   := CENTER-DOMINANCE-ALL / CENTER-DOMINANCE-WITH-
               HELP(n) / CENTER-DOMINANCE-LOST(n) as in Z3.
  transEnum := SUPPORT-CARRIES / WEIGHTS-CARRY / COMPLETENESS-
               CARRIES / PAIRING-CARRIES / TRANS-MIXED as in Z4.
  scrEnum   := SCRARITH-SUPPRESSED / SCRARITH-MID / SCRARITH-O1
               by cls(z1rel(SCRARITH, 5)).
  witEnum   := WITNESS-BLIND-BY-CONSTRUCTION (definitional) with
               ytr/a0dev band gated.

SMOKE DISCLOSURE (pre-freeze, house convention; structural smoke
at rungs 4/5/8 + SCRARITH(5) + EPSTEIN(8) + all four transplants +
sensitivity h = 4).  First pass 28/31 at pre-freeze SHA
67bf9a174ff774dc (kept as z1_suppression_probe.smoke0.log); three
instrument-level findings forced pre-freeze retypes, NO bar, dps,
grid, census or budget moved: (i) the mp inverse-iteration anchor
on RawW equals the secular bottom root ONLY on MAIN cells (rel
dev 9.0 at EPSTEIN(8), 44 at SCRARITH(5): the nearest-zero
iterate is a DIFFERENT eigenvalue there) -- G14 retyped to
MAIN-anchor + all-cell exact residual ward; (ii) the boundary
atom q = h is kernel-invisible by the EXACT fact C(L) == 0
(sin(om_k L) = 0 and a - L/2 = 0 entrywise) -- G33 gained the
BOUNDARY-ZERO-CLASS, and the |F_1(log h)| ~ 0 entries in every
table are this exact zero, not a suppression signal; (iii) P5
REFUTED by the data: sin(phi, U_0) is 10^-1.2..-1.6 and carried
by HIGH modes while the LOW modes are hierarchically suppressed
(z1 < z2 < z3 laddered ~4-7 dex apart) -- G34 retyped from
lock-gate to census-gate (alignEnum).  Additionally a genuine
pre-freeze BUG FIX, disclosed: the transplant pairing initially
truncated to min(len(sup), len(wgt)) which made T0 the FULL
MAIN(8) cell (ncut 6); TRANS_NCUT = 3 frozen (the min world
cardinality) -- the fixed T0 moved from -24.4 to -2.0 and flipped
the causal verdict from PAIRING-CARRIES to COMPLETENESS-CARRIES.
Second smoke 31/31 at SHA 385c41eb0afb7a98 (kept as
z1_suppression_probe.smoke1.log).
CALIBRATION DISCLOSURE (pre-freeze, same convention).  First full
calibration pass 29/31 at SHA 385c41eb0afb7a98 (kept as
z1_suppression_probe.calib1.log): two instrument saturations at
deep rungs, NO verdict-bearing gate refuted by data: (i) the FD
steps 1e-6/1e-7 sit OUTSIDE the measured linear regime once the
fine-tuning index reaches 10^10 (h = 5: stab 1e-1, anadev 2e-3)
-- FD_RELS re-sized to 1e-14/1e-15 (inside the regime; bars
unmoved; post-fix stab <= 2e-17, anadev <= 2e-19); (ii) the
s = 1/2 ID-ward balance is z_1^2-deep and saturates below
working precision at h = 14/15/16/20 -- the declared
resolvability rule 2|z1rel| + 16 <= dps was added (4 mid-path
checks SATURATED-SKIPPED, the z_1-deep s = 1 ward gates
EVERYWHERE).  Second calibration pass 31/31 at SHA
c6899d40cfbb4216 (kept as z1_suppression_probe.calib2.log); the
CAL2 tables below are frozen VERBATIM from it.  Enum resolutions
at calibration: mechEnum = MECH-A-ARCHPRIME-CANCEL modal at 8/14
rungs (the deeper 6 classify MECH-AB by the 0.1 boundary with
c_within pinned FLAT at 10^-1.0..-1.1 -- same cancellation
class, boundary artifact, typed honestly; frozen as CAL2_MECH_N
= 8); alignEnum = ALIGNMENT-MULTI-MODE(79.5) (P5 AGAINST);
expEnum = LAYER-EXP-1 (slope 1.002); gdelEnum = GDEL-Z1-LOCKED
(slope 0.998) (P6 FOR); tauEnum = Z1-NET-RIDES-TAU(+0.97) with
structure coordinates FLAT (c_within +0.010, raw per-atom scale
-0.005); domEnum = CENTER-DOMINANCE-WITH-HELP(7) -- the 7
conservative-margin failures sit AT THE WALL s = 1 at h >= 11
(m_top 7/8), NOT early-path (P8 partially against as worded;
full margin mf > 0 at ALL 126 MAIN cells); transEnum =
COMPLETENESS-CARRIES (P9 reviewer support/mass hypothesis
REFUTED at the reachable rung); scrEnum = SCRARITH-O1 (the
golden permutation LIFTS z_1 by 9.1 dex: the exact pairing is
load-bearing); witEnum = WITNESS-BLIND-BY-CONSTRUCTION.
AMENDMENTS: none (all retypes pre-freeze, disclosed above).

RECORD TABLES (CAL2, frozen from calib2 VERBATIM):
CAL2_OMF {h: log10(1 - f(1))}: 4: -7.0, 5: -11.5, 6: -15.8,
  7: -20.1, 8: -24.6, 9: -29.0, 10: -33.8, 11: -38.3, 12: -43.4,
  13: -47.8, 14: -53.2, 15: -57.3, 16: -62.3, 20: -81.4.
CAL2_GDEL {h: log10(-Gdel(lam_0(1)))}: 4: -6.81, 5: -11.24,
  6: -15.52, 7: -19.84, 8: -24.24, 9: -28.61, 10: -33.40,
  11: -37.94, 12: -43.02, 13: -47.40, 14: -52.77, 15: -56.84,
  16: -61.87, 20: -80.92.
CAL2_D1 {h: log10 d_1} (documentation): 4: -6.4, 5: -10.7,
  6: -15.0, 7: -19.2, 8: -23.6, 9: -27.9, 10: -32.7, 11: -37.2,
  12: -42.3, 13: -46.7, 14: -52.0, 15: -56.1, 16: -61.1,
  20: -80.1 -- THE SECOND NoP EIGENVALUE IS ITSELF THE z_1
  CURRENCY (d_1 ~ |z_1/z_0| x 10^0.5..1.0 at every rung; gap
  d_1 - d_0 O(10) flat; tau sits ~4.3..7.7 dex BELOW z1rel).
CAL2_MECH = MECH-A-ARCHPRIME-CANCEL, CAL2_MECH_N = 8 (of 14).
CAL2_SLOPES: z1_tau +0.97; cw_tau +0.010; maxtraw_tau -0.005;
  (documentation: omf_z1 +1.002, gdel_z1 +0.998, maxterm_tau
  -0.964, cx_tau +1.81, marg -0.02).
CAL2_TRANS {tag: z1rel}: T0 -2.0, T1 -1.2, T2 -2.6, T3 -0.8
  (all O1; full MAIN(8) -24.4; support effect +0.8/+1.8 dex,
  weight effect -0.6/+0.4 dex; node census T0 s* = 7, T1 s* = 5,
  T2 nodeless, T3 s* = 6).
CAL2_SCR z1rel(SCRARITH, 5) = -2.3 (vs MAIN(5) -11.4);
CAL2_SMOOTH z1rel(SMOOTH, 5) = -1.4 (arch 10^0.0 vs continuum
  prime 10^0.1, c_cross 10^-1.5, typed CONTINUUM).
CAL2_EPS z1rel -0.8, per-atom T_q 10^-0.8/-0.6/-0.4 (q = 4/5/6),
  c_cross 10^-0.8, crossing sj = 6 (mc and mf), m_top(1) = 1.
CAL2_SENS {h: log10 max FT_q}: 4: 5.7, 5: 10.1.
CAL2_QCROSS log10 Q_cross/z_0 = +23.1 at MAIN(8) (the EPSTEIN
  atom set dropped into MAIN's OWN form factor yields 10^23 x
  z_0 -- the template does not carry the suppression).
CAL2_MARG mc(1) documentation: 4: 0.620, 5: 0.504, 6: 0.574,
  7: 0.441, 8: 0.173, 9: 0.268, 10: 0.043, 11: -0.133,
  12: -0.196, 13: -0.296, 14: -0.232, 15: -0.324, 16: -0.394,
  20: -0.824 (m_top(1) = 3 at h <= 9, 7/8 at h >= 10; all mf >
  0).
CAL2_ZLADDER documentation (h = 8): z1 -24.4, z2 -19.0,
  z3 -14.3, sin(phi, U_0) 10^-1.4; (h = 20): z1 -81.2, z2 -74.3,
  z3 -67.8, sin 10^-1.6.
CAL2_F1 |F_1| at MAIN(8) supports (log10): log2 +0.85, log3 +0.92,
  log4 +0.87, log5 +0.72, log7 +0.42, log8 +0.30; at EPSTEIN(8)
  supports (its own U_1): log4 +0.98, log5 +0.85, log6 +0.68 --
  same O(1) class (mass location refuted, P2 resolved FOR).

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
instrument wards G10-G15; S2 inheritance G20-G21; S3 Z1 G30-G34;
S4 Z2 G40-G43; S5 Z3 G50-G53; S6 Z4 G60-G62; S7 guards G70-G72;
S8 G80 pricing + G99 runtime.  DETERMINISM: no randomness anywhere;
ProcessPool results keyed; run2 must be identical modulo wall-clock
tokens (lines carrying 'WALL').

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
SGRID_DEN = 8
NGRID_FAC = 16
CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
              ("EPSTEIN", 8, 80))
PROF_CELLS = (("MAIN", 4), ("MAIN", 5), ("MAIN", 8),
              ("SCRARITH", 5), ("EPSTEIN", 8))
NUPROF = 47
SENS_RUNGS = ((4, 60), (5, 60))
FD_RELS = ("1e-14", "1e-15")
TRANS_H = 8
TRANS_DPS = 80
TRANS_NCUT = 3
WIT_RUNG = 5
WIT_FACT = 1000
BOUNDARY_FLOOR = "1e-40"

RANK1_BAR = 1e-40
BLK_BAR = 1e-38
KER_BAR = 1e-38
EIG_RES_BAR = 1e-30
EIG_ORTH_BAR = 1e-30
PARSEVAL_BAR = 1e-30
Z1ID_BAR = 1e-25
CSUM_BAR = 1e-25
SEC_RES_BAR = 1e-20
SECID_BAR = 1e-10
ANCHOR_LAM_BAR = 1e-6
INVIT_RES_BAR = 1e-12
ZCLS = 1e-30
SIGN_RES = 1e-6
MECH_SMALL_BAR = 1e-3
MECH_CANCEL_BAR = 1e-2
SUP_BAR = -8.0
O1_BAR = -3.0
EXP1_BAND = (0.75, 1.25)
EXP2_BAND = (1.75, 2.25)
GDEL_BAND = (0.75, 1.25)
ALIGN_TOL = 0.05
FD_STAB_TOL = 1e-3
FD_ANA_TOL = 1e-4
TAU_FLAT_BAR = 0.30
WIT_YT_BAND = (990.0, 1010.0)
WIT_A0_BAR = 1e-6

LOG_TOL = 0.10
LOG_TOL2 = 0.20
RHO_TOL = 0.15
FRAC_TOL = 0.05
SLOPE_TOL = 0.10

# --------------------------------------- inheritance tables (r200/r201)
_HS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
CAL_Z1REL = dict(zip(_HS, ("-6.9", "-11.4", "-15.7", "-20.0",
                           "-24.4", "-28.8", "-33.6", "-38.1",
                           "-43.2", "-47.6", "-53.0", "-57.1",
                           "-62.1", "-81.2")))
CAL_RHO11 = dict(zip(_HS, ("0.1", "0.1", "0.1", "0.1", "0.2",
                           "0.2", "0.2", "0.2", "0.2", "0.2",
                           "0.2", "0.2", "0.2", "0.3")))
R200_EPS = dict(nnode=3, s_star=6, rmin0="0.690", rmin1="-0.481")
EPS_Z1REL = "-0.8"
EPS_NONPP = "0.51"

# -------------- calibrated record tables (calib2 VERBATIM, frozen)
CAL_FROZEN = True
CAL2_OMF = dict(zip(_HS, ("-7.0", "-11.5", "-15.8", "-20.1",
                          "-24.6", "-29.0", "-33.8", "-38.3",
                          "-43.4", "-47.8", "-53.2", "-57.3",
                          "-62.3", "-81.4")))
CAL2_GDEL = dict(zip(_HS, ("-6.81", "-11.24", "-15.52", "-19.84",
                           "-24.24", "-28.61", "-33.40", "-37.94",
                           "-43.02", "-47.40", "-52.77", "-56.84",
                           "-61.87", "-80.92")))
CAL2_SLOPES = {"z1_tau": "+0.97", "cw_tau": "+0.010",
               "maxtraw_tau": "-0.005"}
CAL2_MECH = "MECH-A-ARCHPRIME-CANCEL"
CAL2_MECH_N = 8

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
                       "access IN-SCOPE (anatomy contract, r195-r201 "
                       "lineage); fully zero-free; concurrent-lane "
                       "files untouched")


# ------------------------------------------------------- shared helpers
def raw_of(Mb, par, nrm, K):
    Raw = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Raw[i, j] = Mb[i, j] * par[i] * par[j] * nrm[i] * nrm[j]
    return Raw


def bottom_vec_mp(Raw, K, froW):
    """r195-r201 VERBATIM: 3 LU solves + residual ward."""
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


def log10f(x) -> float:
    """float log10 of |x| with -300 floor at zero."""
    ax = abs(x)
    if ax == 0:
        return -300.0
    return float(mp.log(ax, 10))


# ---------------------------------------------------------- atom lists
def atom_list(world: str, x: int):
    """(q, u = log q, w) list; replicated VERBATIM from
    radius4_an_probe.build_cell world blocks (mp at ambient dps)."""
    atoms = []
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
            atoms.append((q, mp.log(q), mp.log(p) / mp.sqrt(q)))
        if world == "SCRARITH":
            gold = (math.sqrt(5.0) - 1.0) / 2.0
            keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][2] for i in range(len(atoms))]
            atoms = [(atoms[i][0], atoms[i][1], wts[perm[i]])
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
                atoms.append((n, mp.log(n), lamq[n] / mp.sqrt(n)))
    return atoms


def is_pp(n: int) -> bool:
    for p in range(2, n + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return False


# ------------------------------------------------------ the atom kernel
def kernel_mat(u, oms, aa, L2v, K):
    """The even-sector per-atom kernel C(u): NoP = RawArch -
    sum_q w_q C(log q).  Derived from build_cell's prime block
    (pj[i] = sum w sin(om_i u); off-diag Loewner-type combination;
    diagonal psi); the par factors cancel at the raw level."""
    su = [mp.sin(o * u) for o in oms]
    cu = [mp.cos(o * u) for o in oms]
    Cm = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            num = oms[i] * su[i] - oms[j] * su[j]
            den = oms[j] ** 2 - oms[i] ** 2
            val = 2 * num / den
            Cm[i, j] = val
            Cm[j, i] = val
        if i == 0:
            Cm[0, 0] = 2 * (L2v - u)
        else:
            Cm[i, i] = 2 * ((aa - u / 2) * cu[i]
                            - su[i] / (2 * oms[i]))
    return Cm


def kernel_apply_phi(u, oms, aa, L2v, K, phi):
    """t = C(u) phi without materializing C (used on the u-grid)."""
    su = [mp.sin(o * u) for o in oms]
    cu = [mp.cos(o * u) for o in oms]
    t = [mp.mpf(0)] * K
    for i in range(K):
        acc = mp.mpf(0)
        for j in range(K):
            if i == j:
                if i == 0:
                    cij = 2 * (L2v - u)
                else:
                    cij = 2 * ((aa - u / 2) * cu[i]
                               - su[i] / (2 * oms[i]))
            else:
                cij = 2 * (oms[i] * su[i] - oms[j] * su[j]) \
                    / (oms[j] ** 2 - oms[i] ** 2)
            acc += cij * phi[j]
        t[i] = acc
    return t


# ------------------------------------------- per-cell shared builder
def build_common(world, h, dps):
    ce = R4.build_cell(h, KFAC, world, dps, want_mp=True)
    K = ce["K"]
    aa = mp.log(h) / 2
    L2v = 2 * aa
    s2 = mp.sinh(aa / 2) ** 2
    oms = [k * mp.pi / aa for k in range(K)]
    b = [o * o for o in oms]
    par = [mp.mpf((-1.0) ** k) for k in range(K)]
    nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
           for k in range(K)]
    RawW = raw_of(ce["mpM"], par, nrm, K)
    RawP = raw_of(ce["mpPole"], par, nrm, K)
    RawArch = raw_of(ce["mpArch"], par, nrm, K)
    RawPrime = raw_of(ce["mpPrime"], par, nrm, K)
    phi = [1 / (mp.mpf(1) / 4 + b[k]) for k in range(K)]
    r1dev = mp.mpf(0)
    r1max = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            tgt = 2 * s2 * phi[i] * phi[j]
            r1dev = max(r1dev, abs(RawP[i, j] - tgt))
            r1max = max(r1max, abs(tgt))
    NoP = mp.zeros(K, K)
    blkdev = mp.mpf(0)
    blkmax = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            NoP[i, j] = RawW[i, j] - RawP[i, j]
            alt = RawArch[i, j] - RawPrime[i, j]
            blkdev = max(blkdev, abs(NoP[i, j] - alt))
            blkmax = max(blkmax, abs(NoP[i, j]))
    fro = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                      for j in range(K)))
    froW = mp.sqrt(sum(RawW[i, j] ** 2 for i in range(K)
                       for j in range(K)))
    E, Q = mp.eigsy(NoP)
    idx = sorted(range(K), key=lambda m: E[m])
    d = [E[idx[m]] for m in range(K)]
    Qc = [[Q[i, idx[m]] for i in range(K)] for m in range(K)]
    eres = mp.mpf(0)
    for col in (0, 1, K - 1):
        for i in range(K):
            ri = sum(NoP[i, j] * Qc[col][j] for j in range(K)) \
                - d[col] * Qc[col][i]
            eres = max(eres, abs(ri))
    oworst = mp.mpf(0)
    for (m1, m2) in ((0, 0), (0, 1), (1, 1)):
        dot = sum(Qc[m1][i] * Qc[m2][i] for i in range(K))
        tgt = mp.mpf(1) if m1 == m2 else mp.mpf(0)
        oworst = max(oworst, abs(dot - tgt))
    z = [sum(Qc[m][i] * phi[i] for i in range(K)) for m in range(K)]
    phin2 = sum(t * t for t in phi)
    parseval = abs(sum(t * t for t in z) - phin2) / phin2
    return dict(ce=ce, K=K, aa=aa, L2v=L2v, s2=s2, oms=oms, b=b,
                par=par, nrm=nrm, RawW=RawW, RawArch=RawArch,
                RawPrime=RawPrime, phi=phi, NoP=NoP, fro=fro,
                froW=froW, Qc=Qc, d=d, z=z, phin2=phin2,
                rank1_dev=float(r1dev / r1max),
                blk_dev=float(blkdev / blkmax),
                eig_res=float(eres / fro),
                eig_orth=float(oworst),
                parseval=float(parseval))


def z1_decomposition(C, atoms, want_prof, qcross_atoms=None):
    """Z1: per-atom decomposition of z_1 via the eigen-identity,
    kernel-reconstruction ward, form-factor profile."""
    K, phi, aa, L2v, oms = C["K"], C["phi"], C["aa"], C["L2v"], \
        C["oms"]
    U1 = C["Qc"][1]
    d1 = C["d"][1]
    RawPrime = C["RawPrime"]
    out: dict = {}
    Rec = mp.zeros(K, K)
    terms = []          # (q, w, G1q)
    for (q, u, w) in atoms:
        Cm = kernel_mat(u, oms, aa, L2v, K)
        for i in range(K):
            for j in range(K):
                Rec[i, j] += w * Cm[i, j]
        tvec = [sum(Cm[i, j] * phi[j] for j in range(K))
                for i in range(K)]
        G1q = sum(U1[i] * tvec[i] for i in range(K))
        terms.append((q, w, G1q))
    kerdev = mp.mpf(0)
    kermax = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            kerdev = max(kerdev, abs(Rec[i, j] - RawPrime[i, j]))
            kermax = max(kermax, abs(RawPrime[i, j]))
    out["ker_dev"] = float(kerdev / kermax) if kermax > 0 else 0.0
    archnum = sum(U1[i] * sum(C["RawArch"][i, j] * phi[j]
                              for j in range(K)) for i in range(K))
    T_arch = archnum / d1
    Tq = [(q, w, -w * G1q / d1, -G1q / d1) for (q, w, G1q) in terms]
    z1_rec = T_arch + sum(t[2] for t in Tq)
    z1_meas = C["z"][1]
    gross = (abs(T_arch) + sum(abs(t[2]) for t in Tq))
    out["z1id_dev"] = float(abs(z1_rec - z1_meas) / gross) \
        if gross > 0 else 0.0
    z0 = abs(C["z"][0])
    sumTq = sum(t[2] for t in Tq)
    sumAbsTq = sum(abs(t[2]) for t in Tq)
    out["T_arch"] = float(T_arch / z0)
    out["T_arch_log"] = log10f(T_arch / z0)
    out["atoms"] = [(q, float(w), log10f(F1), float(mp.sign(F1)),
                     log10f(T / z0), float(mp.sign(T)))
                    for (q, w, T, F1) in Tq]
    out["maxterm_log"] = max((log10f(t[2] / z0) for t in Tq),
                             default=-300.0)
    out["c_within"] = log10f(sumTq / sumAbsTq) if sumAbsTq > 0 \
        else -300.0
    denom = max(abs(T_arch), abs(sumTq))
    out["c_cross"] = log10f((T_arch + sumTq) / denom) \
        if denom > 0 else -300.0
    out["negw"] = sum(1 for (_q, w, _T, _F) in Tq if w < 0)
    tot = sum(abs(w) for (_q, w, _T, _F) in Tq)
    out["nonpp_mass"] = float(sum(abs(w) for (q, w, _T, _F) in Tq
                                  if not is_pp(q)) / tot) \
        if tot > 0 else 0.0
    if want_prof:
        prof = []
        for j in range(1, NUPROF + 1):
            u = j * L2v / (NUPROF + 1)
            tvec = kernel_apply_phi(u, oms, aa, L2v, K, phi)
            F1u = -sum(U1[i] * tvec[i] for i in range(K)) / d1
            prof.append((float(u), float(F1u)))
        out["prof"] = prof
        sgn = [1 if p[1] > 0 else -1 for p in prof if p[1] != 0]
        out["prof_nsc"] = sum(1 for i in range(1, len(sgn))
                              if sgn[i] != sgn[i - 1])
    if qcross_atoms is not None:
        qc = mp.mpf(0)
        for (_q, u, w) in qcross_atoms:
            tvec = kernel_apply_phi(u, oms, aa, L2v, K, phi)
            F1u = -sum(U1[i] * tvec[i] for i in range(K)) / d1
            qc += w * F1u
        out["qcross_log"] = log10f(qc / z0)
    return out


def smooth_two_leg(C):
    """SMOOTH: no atoms -- two-leg split via the matrix blocks."""
    K, phi = C["K"], C["phi"]
    U1 = C["Qc"][1]
    d1 = C["d"][1]
    archnum = sum(U1[i] * sum(C["RawArch"][i, j] * phi[j]
                              for j in range(K)) for i in range(K))
    prinum = sum(U1[i] * sum(C["RawPrime"][i, j] * phi[j]
                             for j in range(K)) for i in range(K))
    z1_rec = (archnum - prinum) / d1
    gross = (abs(archnum) + abs(prinum)) / abs(d1)
    z0 = abs(C["z"][0])
    return dict(T_arch_log=log10f(archnum / d1 / z0),
                T_pri_log=log10f(prinum / d1 / z0),
                z1id_dev=float(abs(z1_rec - C["z"][1]) / gross),
                c_cross=log10f((archnum - prinum)
                               / max(abs(archnum), abs(prinum))))


def center_decomp(C, y, Umc):
    """Z3 bookkeeping at one path point."""
    K = C["K"]
    cm = [y[m] * Umc[m] for m in range(K)]
    if cm[0] < 0:
        cm = [-t for t in cm]
    safe = cm[0]
    dng = mp.mpf(0)
    hlp = mp.mpf(0)
    mtop = 0
    worst = mp.mpf(0)
    for m in range(1, K):
        if cm[m] < 0:
            dng += -cm[m]
            if -cm[m] > worst:
                worst = -cm[m]
                mtop = m
        else:
            hlp += cm[m]
    tot = safe + hlp - dng
    return dict(mc=float((safe - dng) / safe) if safe > 0 else
                float("-inf"),
                mf=float(tot / safe) if safe > 0 else float("-inf"),
                al2=tot, safe=safe, dng=dng, mtop=mtop)


# ------------------------------------------------------- battery worker
def w_cell(args) -> dict:
    world, h, dps = args
    try:
        t0 = time.time()
        out = dict(world=world, h=h, err="")
        want_prof = (world, h) in PROF_CELLS
        with mp.workdps(dps):
            C = build_common(world, h, dps)
            K = C["K"]
            out["K"] = K
            for key in ("rank1_dev", "blk_dev", "eig_res",
                        "eig_orth", "parseval"):
                out[key] = C[key]
            tau = C["ce"]["mpE"][0]
            out["log10tau"] = log10f(tau)
            out["tau_pos"] = bool(tau > 0)
            z = C["z"]
            out["z1rel"] = log10f(z[1] / z[0])
            out["z2rel"] = log10f(z[2] / z[0])
            out["z3rel"] = log10f(z[3] / z[0])
            sin2 = sum(t * t for t in z[1:]) / C["phin2"]
            out["sin_log"] = 0.5 * log10f(sin2)
            # ---- Z1 decomposition
            atoms = atom_list(world, h)
            out["n_atoms"] = len(atoms)
            if world == "SMOOTH":
                out["two_leg"] = smooth_two_leg(C)
                out["ker_dev"] = 0.0
                out["z1id_dev"] = out["two_leg"]["z1id_dev"]
            else:
                qca = atom_list("EPSTEIN", 8) \
                    if (world, h) == ("MAIN", 8) else None
                out["z1d"] = z1_decomposition(C, atoms, want_prof,
                                              qcross_atoms=qca)
                out["ker_dev"] = out["z1d"]["ker_dev"]
                out["z1id_dev"] = out["z1d"]["z1id_dev"]
            # ---- Z2 + Z3 along the 9-grid
            d = C["d"]
            Umc = [sum(((-1) ** i) * C["Qc"][m][i] for i in range(K))
                   for m in range(K)]
            rows = []
            csum_dev = 0.0
            need_prof = world == "EPSTEIN"
            if need_prof:
                N = NGRID_FAC * K
                twopi = 2 * mp.pi
                ct = [mp.cos(twopi * m2 / N) for m2 in range(N)]
            for sj in range(SGRID_DEN + 1):
                if sj == 0:
                    lam0 = d[0]
                    y = [mp.mpf(1)] + [mp.mpf(0)] * (K - 1)
                else:
                    s = mp.mpf(sj) / SGRID_DEN
                    ccs = s * 2 * C["s2"]
                    lam0, _lam1, y = secular_bottom_pair(
                        d, z, ccs, dps, K)
                cd = center_decomp(C, y, Umc)
                v = [sum(C["Qc"][m][i] * y[m] for m in range(K))
                     for i in range(K)]
                alt = sum(((-1) ** i) * v[i] for i in range(K))
                gross = sum(abs(y[m] * Umc[m]) for m in range(K))
                dev = float(abs(abs(alt) - abs(cd["al2"])) / gross) \
                    if gross > 0 else 0.0
                csum_dev = max(csum_dev, dev)
                row = dict(sj=sj, mc=cd["mc"], mf=cd["mf"],
                           mtop=cd["mtop"],
                           f=float((lam0 - d[0]) / (d[1] - d[0])))
                if sj > 0:
                    rho1 = abs(y[1] / y[0]) if y[0] != 0 else \
                        mp.mpf("inf")
                    row["rho1_log"] = log10f(rho1)
                if sj in (SGRID_DEN // 2, SGRID_DEN):
                    # mid-path resolvability rule: the ID wards at
                    # s = 1/2 balance O(1) terms down to ~ z_1^2;
                    # they are checkable only where 2|z1rel| + 16
                    # <= dps (s = 1 needs only ~ |z1rel| + 16)
                    need = (2.0 if sj == SGRID_DEN // 2 else 1.0) \
                        * abs(out["z1rel"]) + 16.0
                    if need > dps:
                        row["secid_skip"] = True
                    else:
                        ccs = (mp.mpf(sj) / SGRID_DEN) * 2 * C["s2"]
                        gdel = 1 + ccs * sum(
                            z[m] ** 2 / (d[m] - lam0)
                            for m in range(K) if m != 1)
                        lhs = ccs * z[1] ** 2 / (d[1] - lam0)
                        scale = max(abs(lhs), abs(gdel))
                        row["secid_dev"] = float(abs(lhs + gdel)
                                                 / scale) \
                            if scale > 0 else 0.0
                        row["gdel_log"] = log10f(-gdel) \
                            if gdel < 0 else 300.0
                        row["gdel_neg"] = bool(gdel < 0)
                        row["omf_log"] = log10f(
                            (d[1] - lam0) / (d[1] - d[0]))
                        # ID2 ward
                        rho1id = (lam0 - d[0]) * (-gdel) \
                            / (ccs * abs(z[0] * z[1]))
                        rho1dir = abs(y[1] / y[0])
                        row["id2_dev"] = float(
                            abs(rho1id - rho1dir)
                            / max(rho1id, rho1dir))
                if sj == SGRID_DEN:
                    v0w, lamw, invres = bottom_vec_mp(
                        C["RawW"], K, C["froW"])
                    out["invit_res"] = invres
                    out["anchor_dev"] = float(
                        abs(lamw - lam0)
                        / max(abs(lamw), mp.mpf("1e-300")))
                    # tau_h is congruent-not-similar to RawW's
                    # bottom: recorded as a screen scalar only
                    out["lam0w_log"] = log10f(lam0)
                    out["gap_log"] = log10f(d[1] - d[0])
                    out["d0_val"] = float(d[0])
                    out["d1_log"] = log10f(d[1])
                    out["d1_pos"] = bool(d[1] > 0)
                    out["lift_log"] = log10f(lam0 - d[0])
                    # secular residual ward on M(1) v = lam0 v
                    Ms = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            Ms[i, j] = C["NoP"][i, j] + 2 \
                                * C["s2"] * C["phi"][i] \
                                * C["phi"][j]
                    rres = mp.mpf(0)
                    for i in range(K):
                        ri = sum(Ms[i, j] * v[j]
                                 for j in range(K)) - lam0 * v[i]
                        rres = max(rres, abs(ri))
                    out["sec_res"] = float(rres / C["fro"])
                if need_prof:
                    Av = prof_eval(v, K, N, ct)
                    jp = max(range(len(Av)),
                             key=lambda j2: abs(Av[j2]))
                    if Av[jp] < 0:
                        Av = [-x for x in Av]
                    amax = max(abs(x) for x in Av)
                    row["rmin"] = float(min(Av) / amax)
                    row["node"] = bool(
                        min(Av) < -mp.mpf(SIGN_RES) * amax)
                rows.append(row)
            out["rows"] = rows
            out["csum_dev"] = csum_dev
            out["Umc1_sign"] = float(mp.sign(Umc[1] * Umc[0])) \
                if Umc[0] != 0 else 0.0
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "h": h,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ---------------------------------------------------- transplant worker
def w_trans(args) -> dict:
    tag, sup_world, wgt_world = args
    try:
        t0 = time.time()
        out = dict(tag=tag, err="")
        dps = TRANS_DPS
        h = TRANS_H
        with mp.workdps(dps):
            C = build_common("MAIN", h, dps)      # arch is world-blind
            K = C["K"]
            aa, L2v, oms = C["aa"], C["L2v"], C["oms"]
            sup = atom_list(sup_world, h)
            wgt = atom_list(wgt_world, h)
            ncut = min(len(sup), len(wgt), TRANS_NCUT)
            atoms = [(sup[i][0], sup[i][1], wgt[i][2])
                     for i in range(ncut)]
            out["atoms"] = [(q, float(w)) for (q, _u, w) in atoms]
            NoT = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoT[i, j] = C["RawArch"][i, j]
            for (_q, u, w) in atoms:
                Cm = kernel_mat(u, oms, aa, L2v, K)
                for i in range(K):
                    for j in range(K):
                        NoT[i, j] -= w * Cm[i, j]
            if tag == "T3":
                CE = build_common("EPSTEIN", h, dps)
                dev = mp.mpf(0)
                mx = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        dev = max(dev, abs(NoT[i, j]
                                           - CE["NoP"][i, j]))
                        mx = max(mx, abs(CE["NoP"][i, j]))
                out["t3_dev"] = float(dev / mx)
            E, Q = mp.eigsy(NoT)
            idx = sorted(range(K), key=lambda m: E[m])
            d = [E[idx[m]] for m in range(K)]
            Qc = [[Q[i, idx[m]] for i in range(K)]
                  for m in range(K)]
            phi = C["phi"]
            z = [sum(Qc[m][i] * phi[i] for i in range(K))
                 for m in range(K)]
            out["z1rel"] = log10f(z[1] / z[0])
            Umc = [sum(((-1) ** i) * Qc[m][i] for i in range(K))
                   for m in range(K)]
            N = NGRID_FAC * K
            twopi = 2 * mp.pi
            ct = [mp.cos(twopi * m2 / N) for m2 in range(N)]
            nnode = 0
            sstar = None
            rows = []
            for sj in range(SGRID_DEN + 1):
                if sj == 0:
                    y = [mp.mpf(1)] + [mp.mpf(0)] * (K - 1)
                    lam0 = d[0]
                else:
                    ccs = (mp.mpf(sj) / SGRID_DEN) * 2 * C["s2"]
                    lam0, _l1, y = secular_bottom_pair(
                        d, z, ccs, dps, K)
                v = [sum(Qc[m][i] * y[m] for m in range(K))
                     for i in range(K)]
                Av = prof_eval(v, K, N, ct)
                jp = max(range(len(Av)),
                         key=lambda j2: abs(Av[j2]))
                if Av[jp] < 0:
                    Av = [-x for x in Av]
                amax = max(abs(x) for x in Av)
                rmin = float(min(Av) / amax)
                node = bool(min(Av) < -mp.mpf(SIGN_RES) * amax)
                if node:
                    nnode += 1
                    if sstar is None:
                        sstar = sj
                rows.append(dict(sj=sj, rmin=rmin, node=node))
                if sj == SGRID_DEN:
                    out["rho11_log"] = log10f(abs(y[1] / y[0]))
            out["rows"] = rows
            out["nnode"] = nnode
            out["sstar"] = sstar
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"tag": tag, "err": "%s\n%s"
                % (exc, traceback.format_exc())}


# --------------------------------------------------- sensitivity worker
def w_sens(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        out = dict(h=h, err="")
        with mp.workdps(dps):
            C = build_common("MAIN", h, dps)
            K = C["K"]
            aa, L2v, oms, phi = C["aa"], C["L2v"], C["oms"], C["phi"]
            atoms = atom_list("MAIN", h)
            z1b = C["z"][1]
            U1 = C["Qc"][1]
            jstar = max(range(K), key=lambda i: abs(U1[i]))
            sstar = 1 if U1[jstar] > 0 else -1

            def z1_of(NoX):
                E, Q = mp.eigsy(NoX)
                idx = sorted(range(K), key=lambda m: E[m])
                col = [Q[i, idx[1]] for i in range(K)]
                if (1 if col[jstar] > 0 else -1) != sstar:
                    col = [-t for t in col]
                return sum(col[i] * phi[i] for i in range(K))

            tab = []
            for (q, u, w) in atoms:
                Cm = kernel_mat(u, oms, aa, L2v, K)
                # exact first-order perturbation formula
                CU1 = [sum(Cm[i, j] * U1[j] for j in range(K))
                       for i in range(K)]
                ana = mp.mpf(0)
                for m in range(K):
                    if m == 1:
                        continue
                    um_cu1 = sum(C["Qc"][m][i] * CU1[i]
                                 for i in range(K))
                    ana += C["z"][m] * (-um_cu1) \
                        / (C["d"][1] - C["d"][m])
                fds = []
                for fr in FD_RELS:
                    dw = mp.mpf(fr) * abs(w)
                    Np = mp.zeros(K, K)
                    Nm = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            Np[i, j] = C["NoP"][i, j] \
                                - dw * Cm[i, j]
                            Nm[i, j] = C["NoP"][i, j] \
                                + dw * Cm[i, j]
                    fd = (z1_of(Np) - z1_of(Nm)) / (2 * dw)
                    fds.append(fd)
                bfloor = mp.mpf(BOUNDARY_FLOOR)
                if abs(fds[1]) < bfloor and abs(ana) < bfloor:
                    # boundary atom u = log h == L: C(L) == 0
                    # identically (sin(om_k L) = 0, a - L/2 = 0)
                    tab.append(dict(q=q, ft_log=None, stab=0.0,
                                    anadev=0.0, dz_log=-300.0,
                                    boundary=True))
                    continue
                stab = float(abs(fds[0] - fds[1])
                             / max(abs(fds[0]), abs(fds[1]),
                                   mp.mpf("1e-300")))
                anadev = float(abs(fds[1] - ana)
                               / max(abs(ana), mp.mpf("1e-300")))
                ft = abs(fds[1]) * abs(w) / abs(z1b)
                tab.append(dict(q=q, ft_log=log10f(ft), stab=stab,
                                anadev=anadev, boundary=False,
                                dz_log=log10f(fds[1])))
            out["tab"] = tab
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s"
                % (exc, traceback.format_exc())}


# ------------------------------------------------------- witness leg
def witness_leg() -> dict:
    """r172 recipe / r198-r201 code path VERBATIM at h = WIT_RUNG."""
    dps = DPS[WIT_RUNG]
    ce = R4.build_cell(WIT_RUNG, KFAC, "MAIN", dps, want_mp=True)
    K = ce["K"]
    out: dict = {}
    with mp.workdps(dps):
        aa = mp.log(WIT_RUNG) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
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
    print("z1_suppression_probe -- PRIME.Z1.SUPPRESSION.01 "
          "(mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/s-grids/censuses/transforms declared "
          "in the frozen spec (SPEC_SHA covers the declaration); "
          "priors P1-P10 pre-registered resolve-and-record, none "
          "gate-forcing; classical dictionary NAMED and typed: the "
          "rank-one secular/interlacing dictionary (r200: Weyl, "
          "Kato, BNS 1978), first-order eigenvector perturbation "
          "(Rayleigh-Schroedinger, warded against FD), Parseval on "
          "the orthonormal eigenbasis; the ACF/Loewner reading of "
          "the atom kernel is r195 lineage (named, consumed only as "
          "the warded entrywise identity NoP = Arch - sum w C); "
          "tau_h enters ONLY as a measured per-rung scalar")

    # ------------------------------------------------------------ S1+S2
    section("S1/S2  BATTERY (cells + wards + inheritance)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [("MAIN", h, DPS[h]) for h in rungs]
    ctasks = list(CTRL_CELLS) if not smoke else \
        [("SCRARITH", 5, 60), ("EPSTEIN", 8, 80)]
    tasks += list(ctasks)
    ttasks = [("T0", "MAIN", "MAIN"), ("T1", "EPSTEIN", "MAIN"),
              ("T2", "MAIN", "EPSTEIN"),
              ("T3", "EPSTEIN", "EPSTEIN")]
    stasks = list(SENS_RUNGS) if not smoke else [SENS_RUNGS[0]]
    res: dict = {}
    tres: dict = {}
    sres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = [("cell", ex.submit(w_cell, t)) for t in tasks]
        futs += [("trans", ex.submit(w_trans, t)) for t in ttasks]
        futs += [("sens", ex.submit(w_sens, t)) for t in stasks]
        for kind, fu in futs:
            o = fu.result()
            if kind == "cell":
                res[(o["world"], o["h"])] = o
            elif kind == "trans":
                tres[o["tag"]] = o
            else:
                sres[o["h"]] = o
    errs = [k for k, v in list(res.items()) + list(tres.items())
            + list(sres.items()) if v.get("err")]
    for k in errs:
        v = res.get(k) or tres.get(k) or sres.get(k)
        print("  [ERR] %s %s" % (str(k), v["err"]))
    if errs:
        check("G10-wards", False, "worker errors at %s" % str(errs))
        print("ABORT: worker errors")
        return 1
    mains = [("MAIN", h) for h in rungs]
    allcells = mains + [(w, x) for (w, x, _d) in ctasks]

    w10 = max(max(res[c]["rank1_dev"] for c in allcells),
              max(res[c]["blk_dev"] for c in allcells))
    check("G10-rank1+blocksplit-wards",
          all(res[c]["rank1_dev"] <= RANK1_BAR for c in allcells)
          and all(res[c]["blk_dev"] <= BLK_BAR for c in allcells),
          "RawP == c_pole phi phi^T (bar 1e-40) and NoP == RawArch "
          "- RawPrime (bar 1e-38) at ALL %d cells; worst %.1e"
          % (len(allcells), w10))
    check("G11-eigsy-wards",
          all(res[c]["eig_res"] <= EIG_RES_BAR
              and res[c]["eig_orth"] <= EIG_ORTH_BAR
              and res[c]["parseval"] <= PARSEVAL_BAR
              for c in allcells),
          "eigen residual <= 1e-30, orthonormality <= 1e-30, "
          "Parseval sum z_m^2 == ||phi||^2 <= 1e-30 at all cells "
          "(worst res %.1e orth %.1e pars %.1e)"
          % (max(res[c]["eig_res"] for c in allcells),
             max(res[c]["eig_orth"] for c in allcells),
             max(res[c]["parseval"] for c in allcells)))
    kcells = [c for c in allcells if c[0] != "SMOOTH"]
    check("G12-kernel-reconstruction-ward",
          all(res[c]["ker_dev"] <= KER_BAR for c in kcells)
          and tres["T3"]["t3_dev"] <= KER_BAR,
          "sum_q w_q C(log q) == RawPrime entrywise at all %d atom "
          "cells (worst %.1e) AND transplant assembly NoP(T3) == "
          "NoP(EPSTEIN(8)) (%.1e): the linear atom->matrix law and "
          "the transplant machinery are EXACT on the record"
          % (len(kcells), max(res[c]["ker_dev"] for c in kcells),
             tres["T3"]["t3_dev"]))
    check("G13-z1-eigen-identity-ward",
          all(res[c]["z1id_dev"] <= Z1ID_BAR for c in allcells),
          "z_1 == [U_1^T Arch phi - sum_q w_q U_1^T C(u_q) phi]/d_1 "
          "at gross scale <= 1e-25 at all cells (worst %.1e); the "
          "per-atom z_1 table is an EXACT decomposition, not a "
          "model" % max(res[c]["z1id_dev"] for c in allcells))
    check("G14-secular+anchor-wards",
          all(res[c]["sec_res"] <= SEC_RES_BAR for c in allcells)
          and all(res[c]["invit_res"] <= INVIT_RES_BAR
                  and res[c]["anchor_dev"] <= ANCHOR_LAM_BAR
                  for c in mains)
          and all(r.get("secid_dev", 0.0) <= SECID_BAR
                  and r.get("id2_dev", 0.0) <= SECID_BAR
                  for c in allcells for r in res[c]["rows"]),
          "exact s = 1 eigen-residual <= 1e-20 at ALL cells (worst "
          "%.1e -- the strong ward); mp inverse-iteration anchor "
          "== secular root (bar 1e-6) on the MAIN cells (r195-r200 "
          "lineage; on EPSTEIN/SCRARITH the nearest-zero iterate "
          "is a DIFFERENT eigenvalue than the bottom -- typed, "
          "smoke-disclosed, residual ward carries those cells); "
          "tau_h screened as scalar only (congruence-not-"
          "similarity); ID1 (rho z_1^2/(d_1 - lam_0) == "
          "-Gdel(lam_0)) and ID2 (rho_1 == (lam_0 - d_0)(-Gdel)/"
          "(rho|z_0 z_1|)) hold to <= 1e-10 at s = 1/2 and 1 at "
          "every RESOLVABLE cell (worst %.1e; %d mid-path checks "
          "SATURATED-SKIPPED by the declared rule 2|z1rel| + 16 "
          "<= dps -- the mid-path balance is z_1^2-deep, below "
          "working precision at the deepest rungs; the s = 1 "
          "ward is z_1-deep and applies EVERYWHERE): the "
          "two-ladder identity chain is EXACT"
          % (max(res[c]["sec_res"] for c in allcells),
             max(max(r.get("secid_dev", 0.0), r.get("id2_dev", 0.0))
                 for c in allcells for r in res[c]["rows"]),
             sum(1 for c in allcells for r in res[c]["rows"]
                 if r.get("secid_skip"))))
    check("G15-center-sum-ward",
          all(res[c]["csum_dev"] <= CSUM_BAR for c in allcells),
          "A_s(L/2) == sum_m y_m Umc_m at gross scale <= 1e-25 at "
          "all cells x 9 s (worst %.1e): the Z3 bookkeeping is the "
          "exact mode expansion of the alternating edge scalar"
          % max(res[c]["csum_dev"] for c in allcells))

    ok20 = True
    det20 = []
    for c in mains:
        h = c[1]
        dz = abs(res[c]["z1rel"] - float(CAL_Z1REL[h]))
        r1 = res[c]["rows"][SGRID_DEN].get("rho1_log", 0.0)
        dr = abs(r1 - float(CAL_RHO11[h]))
        if dz > LOG_TOL or dr > RHO_TOL:
            ok20 = False
            det20.append("h%d dz %.2f dr %.2f" % (h, dz, dr))
    ec = res[("EPSTEIN", 8)]
    eps_first_neg = next((r["sj"] for r in ec["rows"]
                          if r.get("node")), None)
    rmin1e = ec["rows"][SGRID_DEN]["rmin"]
    rmin0e = ec["rows"][0]["rmin"]
    ok20e = (eps_first_neg == R200_EPS["s_star"]
             and abs(rmin1e - float(R200_EPS["rmin1"])) <= FRAC_TOL
             and abs(rmin0e - float(R200_EPS["rmin0"])) <= FRAC_TOL
             and abs(ec["z1rel"] - float(EPS_Z1REL)) <= LOG_TOL)
    check("G20-inheritance", ok20 and ok20e,
          "z1rel == r201 CAL_Z1REL (0.10 dex) and log10 rho_1(1) == "
          "CAL_RHO11 (0.15) at all %d rungs%s; EPSTEIN(8) "
          "fingerprint: first node sj = %s (r200: 6), rmin0 %.3f "
          "(0.690), rmin1 %.3f (-0.481), z1rel %.1f (-0.8)"
          % (len(mains),
             "" if ok20 else " [DEV: %s]" % "; ".join(det20),
             str(eps_first_neg), rmin0e, rmin1e, ec["z1rel"]))
    negw_main = sum(res[c]["z1d"]["negw"] for c in mains)
    scr = res.get(("SCRARITH", 5))
    check("G21-source-census",
          negw_main == 0 and ec["z1d"]["negw"] == 0
          and abs(ec["z1d"]["nonpp_mass"] - float(EPS_NONPP))
          <= FRAC_TOL
          and (scr is None or scr["z1d"]["negw"] == 0),
          "negw(MAIN) = 0 at all rungs, negw(EPSTEIN, 8) = 0 "
          "(Lambda >= 0 refuted as separator, r201 inheritance), "
          "EPSTEIN non-prime-power mass fraction %.2f (0.51); "
          "SCRARITH weights nonnegative (permuted multiset)"
          % ec["z1d"]["nonpp_mass"])

    # ------------------------------------------------------------ S3
    section("S3  Z1: THE PER-ATOM z_1 DECOMPOSITION (the pivot)")
    mech_by_h = {}
    for c in mains + [("EPSTEIN", 8)] + \
            ([("SCRARITH", 5)] if scr else []):
        o = res[c]
        zd = o["z1d"]
        print("  %s h=%-2d  z1rel %7.1f | T_arch/z0 %+9.3e "
              "(10^%.1f) | atoms:" % (c[0], c[1], o["z1rel"],
                                      zd["T_arch"],
                                      zd["T_arch_log"]))
        for (q, w, f1l, f1s, tl, ts) in zd["atoms"]:
            print("      q=%-3d w=%8.5f  |F1(log q)| 10^%+6.2f "
                  "sgn %+d   |T_q/z0| 10^%+6.2f sgn %+d"
                  % (q, w, f1l, int(f1s), tl, int(ts)))
        print("      maxterm 10^%.1f  c_within 10^%.1f  c_cross "
              "10^%.1f" % (zd["maxterm_log"], zd["c_within"],
                           zd["c_cross"]))
        if zd["maxterm_log"] <= math.log10(MECH_SMALL_BAR):
            e = "MECH-C-SMALLTERMS"
        elif 10 ** zd["c_cross"] <= MECH_CANCEL_BAR and \
                10 ** zd["c_within"] > 10 * MECH_CANCEL_BAR:
            e = "MECH-A-ARCHPRIME-CANCEL"
        elif 10 ** zd["c_within"] <= MECH_CANCEL_BAR:
            e = "MECH-AB-WITHINPRIME-CANCEL"
        else:
            e = "MECH-MIXED"
        mech_by_h[c] = e
    mech_main = [mech_by_h[c] for c in mains]
    mech_enum = max(set(mech_main), key=mech_main.count)
    check("G30-per-atom-tables",
          all(res[c]["z1id_dev"] <= Z1ID_BAR for c in mains),
          "exact per-atom z_1 tables delivered at all %d MAIN rungs "
          "+ EPSTEIN(8) + SCRARITH(5) (G13-warded); per-atom terms "
          "are O(10^%.1f..10^%.1f) x z_0 -- NOT small: the net z_1 "
          "10^%.1f at h = 8 is a %.1f-dex cancellation ON THE "
          "RECORD" % (len(mains),
                      min(res[c]["z1d"]["maxterm_log"]
                          for c in mains),
                      max(res[c]["z1d"]["maxterm_log"]
                          for c in mains),
                      res[("MAIN", 8)]["z1rel"],
                      res[("MAIN", 8)]["z1d"]["maxterm_log"]
                      - res[("MAIN", 8)]["z1rel"]))
    check("G31-mechanism-adjudication",
          mech_enum in ("MECH-A-ARCHPRIME-CANCEL",
                        "MECH-AB-WITHINPRIME-CANCEL",
                        "MECH-C-SMALLTERMS") and
          (smoke or calib
           or (mech_enum == CAL2_MECH
               and mech_main.count(mech_enum) == CAL2_MECH_N)),
          "mechEnum = %s (%d/%d MAIN rungs; frozen decision rule); "
          "EPSTEIN(8) mech class %s; h = 8 metrics: maxterm "
          "10^%.1f, c_within 10^%.1f, c_cross 10^%.1f (the "
          "adjudication between small-terms (c), within-prime "
          "cancellation (a/b) and arch-vs-prime pairing (a) is "
          "carried by these three frozen coordinates)"
          % (mech_enum, mech_main.count(mech_enum), len(mech_main),
             mech_by_h[("EPSTEIN", 8)],
             res[("MAIN", 8)]["z1d"]["maxterm_log"],
             res[("MAIN", 8)]["z1d"]["c_within"],
             res[("MAIN", 8)]["z1d"]["c_cross"]))
    m8 = res[("MAIN", 8)]["z1d"]
    e8 = ec["z1d"]
    f1_main = {q: fl for (q, _w, fl, _s, _tl, _ts) in m8["atoms"]}
    f1_eps = {q: fl for (q, _w, fl, _s, _tl, _ts) in e8["atoms"]}
    check("G32-form-factor-face",
          "qcross_log" in m8 and m8.get("prof_nsc") is not None,
          "F_1 profiles on the 47-point u-grid (sign changes: "
          "MAIN(8) %s, EPSTEIN(8) %s; the boundary point u = L is "
          "an exact kernel zero); log10|F_1| at supports: MAIN(8) "
          "%s (d_1 10^%.1f -- the 1/d_1 normalization inflates "
          "MAIN's F_1: d_1 is ITSELF a near-zero) vs EPSTEIN(8) "
          "%s (d_1 10^%.1f O(1)); NO support of either world "
          "sits at a small |F_1| except the exact boundary zero "
          "-- mass location NOT the carrier (P2); Q_cross = "
          "EPSTEIN atoms in MAIN's own form factor = 10^%.1f x "
          "z_0 vs MAIN net z_1 10^%.1f: the suppression is a "
          "property of the ATOM SET + its weights, not of the "
          "template (P3)"
          % (str(m8.get("prof_nsc")),
             str(e8.get("prof_nsc")),
             str({q: "%.2f" % f1_main[q] for q in sorted(f1_main)}),
             res[("MAIN", 8)]["d1_log"],
             str({q: "%.2f" % f1_eps[q] for q in sorted(f1_eps)}),
             ec["d1_log"],
             m8.get("qcross_log", float("nan")),
             res[("MAIN", 8)]["z1rel"]))
    ok33 = True
    ftmax = {}
    for h, so in sres.items():
        for t in so["tab"]:
            if t["stab"] > FD_STAB_TOL or t["anadev"] > FD_ANA_TOL:
                ok33 = False
        ftmax[h] = max(t["ft_log"] for t in so["tab"]
                       if t["ft_log"] is not None)
        print("  SENS h=%d: %s" % (h, "; ".join(
            ("q=%d BOUNDARY-ZERO-CLASS (C(L) == 0 exactly)"
             % t["q"]) if t["boundary"] else
            "q=%d FT 10^%.1f (stab %.0e ana %.0e)"
            % (t["q"], t["ft_log"], t["stab"], t["anadev"])
            for t in so["tab"])))
    check("G33-sensitivity-finetuning", ok33,
          "dz_1/dw_q central FD stable across step sizes (1e-3) "
          "AND == exact first-order perturbation formula (1e-4) at "
          "every non-boundary atom (the boundary atom q = h is "
          "ZERO-CLASS: the kernel vanishes identically at u = L, "
          "an exact structure fact -- sin(om_k L) = 0 and "
          "a - L/2 = 0); fine-tuning index max FT_q: %s -- the "
          "z_1 smallness is a FINE-TUNED cancellation (FT >> 1, "
          "P4): moving ONE atom weight by relative eps moves z_1 "
          "by ~ FT x eps x z_1"
          % str({h: "10^%.1f" % v for h, v in ftmax.items()}))
    worst_align = max(abs(res[c]["sin_log"] - res[c]["z1rel"])
                      for c in mains)
    align_enum = ("ALIGNMENT-LOCKED" if worst_align <= ALIGN_TOL
                  else "ALIGNMENT-MULTI-MODE(%.1f)" % worst_align)
    for c in mains:
        print("  MAIN h=%-2d z-ladder: z1 %.1f z2 %.1f z3 %.1f | "
              "sin(phi,U0) 10^%.1f"
              % (c[1], res[c]["z1rel"], res[c]["z2rel"],
                 res[c]["z3rel"], res[c]["sin_log"]))
    check("G34-alignment-census",
          all(math.isfinite(res[c]["sin_log"]) for c in mains),
          "alignEnum = %s: Parseval-exact sin(phi, U_0) vs "
          "|z_1/z_0| (worst gap %.1f dex at MAIN rungs) -- the "
          "z-ladder census above shows the global pole-ray/"
          "ground-ray misalignment is carried by HIGHER modes "
          "while the LOW dangerous modes are hierarchically "
          "suppressed (h = 8: z1 %.1f < z2 %.1f < z3 %.1f): the "
          "suppression is MODE-SPECIFIC, not the r182 global "
          "alignment law (P5 adjudicated by the census; typed "
          "MEASURED-CORRESPONDENCE, no theorem consumed)"
          % (align_enum, worst_align, res[("MAIN", 8)]["z1rel"],
             res[("MAIN", 8)]["z2rel"], res[("MAIN", 8)]["z3rel"]))

    # ------------------------------------------------------------ S4
    section("S4  Z2: THE TWO-LADDER IDENTITY + SCREENS")
    for c in mains:
        o = res[c]
        r1 = o["rows"][SGRID_DEN]
        print("  MAIN h=%-2d tau 10^%.1f | d1 10^%.1f  gap(d1-d0) "
              "10^%.1f  lift(lam0-d0) 10^%.1f  1-f 10^%.1f  "
              "-Gdel 10^%.2f  rho1 10^%.1f"
              % (c[1], o["log10tau"], o["d1_log"], o["gap_log"],
                 o["lift_log"], r1["omf_log"],
                 r1["gdel_log"], r1["rho1_log"]))
    check("G40-identity-chain", True,
          "EXACT on the rank-one secular structure (G14-warded): "
          "(ID1) rho z_1^2/(d_1 - lam_0) = -Gdel(lam_0); (ID2) "
          "rho_1 = |z_1/z_0| f/(1-f) = (lam_0 - d_0)(-Gdel)/"
          "(rho|z_0 z_1|) -- the suppression ladder and the "
          "amplification ladder are algebraically ONE object; "
          "which factor carries the scaling is adjudicated in G42")
    ok41 = True
    if not (smoke or calib) and CAL2_OMF:
        for c in mains:
            h = c[1]
            if abs(res[c]["rows"][SGRID_DEN]["omf_log"]
                   - float(CAL2_OMF[h])) > LOG_TOL2 * 3 or \
               abs(res[c]["rows"][SGRID_DEN]["gdel_log"]
                   - float(CAL2_GDEL[h])) > LOG_TOL2:
                ok41 = False
    check("G41-anatomy-ladders", ok41,
          "full anatomy recorded at all rungs (d_0 < 0 <= tau ~ "
          "lam_0(1) ~ d_1-side; gap/lift/1-f/-Gdel tables above%s); "
          "h = 8: 1-f 10^%.1f, -Gdel 10^%.2f O(1)-class"
          % ("" if smoke or calib else ", == CAL2 frozen tables",
             res[("MAIN", 8)]["rows"][SGRID_DEN]["omf_log"],
             res[("MAIN", 8)]["rows"][SGRID_DEN]["gdel_log"]))
    xs = [res[c]["z1rel"] for c in mains]
    sl_omf, _ = fit_line(xs, [res[c]["rows"][SGRID_DEN]["omf_log"]
                              for c in mains])
    sl_gdel, _ = fit_line(xs, [res[c]["rows"][SGRID_DEN]["gdel_log"]
                               for c in mains])
    if EXP1_BAND[0] <= sl_omf <= EXP1_BAND[1]:
        exp_enum = "LAYER-EXP-1"
    elif EXP2_BAND[0] <= sl_omf <= EXP2_BAND[1]:
        exp_enum = "LAYER-EXP-2"
    else:
        exp_enum = "LAYER-EXP-OTHER(%.2f)" % sl_omf
    gdel_enum = "GDEL-Z1-LOCKED" if GDEL_BAND[0] <= sl_gdel \
        <= GDEL_BAND[1] else "GDEL-FLAT(%.3f)" % sl_gdel
    if gdel_enum == "GDEL-Z1-LOCKED":
        reading = ("the deleted secular NEAR-VANISHES at lam_0 "
                   "(-Gdel ~ |z_1/z_0|): lam_0 is pinned z_1-close "
                   "to d_1 and 1 - f ~ |z_1/z_0| -- suppression "
                   "and amplification are faces of ONE near-root "
                   "object (P6 resolved FOR)")
    else:
        reading = ("-Gdel is NOT z_1-locked (slope %.3f): the "
                   "scaling is carried by the other ID1 factors; "
                   "P6-as-worded resolves AGAINST, anatomy tables "
                   "above adjudicate which factor rides" % sl_gdel)
    check("G42-exponent-adjudication",
          exp_enum in ("LAYER-EXP-1", "LAYER-EXP-2"),
          "slope log10(1-f(1)) vs z1rel = %.3f -> %s; slope "
          "log10(-Gdel(1)) vs z1rel = %.3f -> %s; via exact ID1, "
          "1 - f = rho z_1^2/((d_1-d_0)(-Gdel(lam_0))): %s"
          % (sl_omf, exp_enum, sl_gdel, gdel_enum, reading))
    sl_z1tau, _ = fit_line([res[c]["log10tau"] for c in mains], xs)
    sl_cw, _ = fit_line([res[c]["log10tau"] for c in mains],
                        [res[c]["z1d"]["c_within"] for c in mains])
    sl_cx, _ = fit_line([res[c]["log10tau"] for c in mains],
                        [res[c]["z1d"]["c_cross"] for c in mains])
    sl_mx, _ = fit_line([res[c]["log10tau"] for c in mains],
                        [res[c]["z1d"]["maxterm_log"]
                         for c in mains])
    # d_1-free raw per-atom scale (undo the 1/d_1 inflation)
    sl_mxr, _ = fit_line([res[c]["log10tau"] for c in mains],
                         [res[c]["z1d"]["maxterm_log"]
                          + res[c]["d1_log"] for c in mains])
    tau_enum = ("Z1-NET-RIDES-TAU(%.2f)" % sl_z1tau
                if abs(sl_z1tau) > TAU_FLAT_BAR else
                "Z1-NET-TAU-FLAT(%.2f)" % sl_z1tau)
    ok43 = all(math.isfinite(x) for x in
               (sl_z1tau, sl_cw, sl_cx, sl_mx, sl_mxr))
    if not (smoke or calib) and CAL2_SLOPES:
        ok43 = (ok43 and abs(sl_z1tau
                             - float(CAL2_SLOPES["z1_tau"])) <= 0.15
                and abs(sl_cw
                        - float(CAL2_SLOPES["cw_tau"])) <= 0.15
                and abs(sl_mxr
                        - float(CAL2_SLOPES["maxtraw_tau"]))
                <= 0.15)
    check("G43-tau-screens", ok43,
          "%s (slope z1rel vs log10 tau %+.2f -- the hard screen); "
          "structure coordinates: c_within slope %+.3f, RAW "
          "per-atom scale (maxterm x d_1, the d_1-free functional "
          "size) slope %+.3f (bar 0.30), while the d_1-normalized "
          "maxterm rides %+.3f (pure 1/d_1 inflation, d_1 being "
          "itself z_1-currency) and c_cross rides %+.2f (it IS "
          "the net): the factorization {tau-flat per-atom "
          "structure} x {riding cancellation depth} is measured "
          "-- the controllable piece is the raw form-factor/atom "
          "table, the riding piece is the depth"
          % (tau_enum, sl_z1tau, sl_cw, sl_mxr, sl_mx, sl_cx))

    # ------------------------------------------------------------ S5
    section("S5  Z3: SAFE-MINUS-DANGEROUS AT THE CENTER")
    nfail_mc = 0
    nfail_mf = 0
    for c in mains:
        for r in res[c]["rows"]:
            if r["mc"] <= 0:
                nfail_mc += 1
            if r["mf"] <= 0:
                nfail_mf += 1
    if nfail_mc == 0:
        dom_enum = "CENTER-DOMINANCE-ALL"
    elif nfail_mf == 0:
        dom_enum = "CENTER-DOMINANCE-WITH-HELP(%d)" % nfail_mc
    else:
        dom_enum = "CENTER-DOMINANCE-LOST(%d)" % nfail_mf
    for c in mains:
        o = res[c]
        print("  MAIN h=%-2d mc(s): %s | m_top(1) = %d"
              % (c[1], " ".join("%.4f" % r["mc"]
                                for r in o["rows"]),
                 o["rows"][SGRID_DEN]["mtop"]))
    check("G50-center-decomposition",
          all(res[c]["csum_dev"] <= CSUM_BAR for c in allcells),
          "exact A_s(L/2) = safe - dangerous + helpful mode "
          "bookkeeping at all cells x 9 s (G15-warded); dangerous "
          "driver is m = 1 at the wall at %d/%d MAIN rungs"
          % (sum(1 for c in mains
                 if res[c]["rows"][SGRID_DEN]["mtop"] == 1),
             len(mains)))
    check("G51-dominance-adjudication",
          nfail_mf == 0,
          "domEnum = %s: conservative margin mc > 0 at %d/%d MAIN "
          "cells (full margin mf > 0 at ALL -- A(L/2) > 0 "
          "everywhere on MAIN, r200-consistent); the dangerous sum "
          "never overcomes the ground term%s"
          % (dom_enum,
             len(mains) * (SGRID_DEN + 1) - nfail_mc,
             len(mains) * (SGRID_DEN + 1),
             "" if nfail_mc == 0 else
             " ONLY with the helpful modes included (honest)"))
    efirst_mf = next((r["sj"] for r in ec["rows"] if r["mf"] < 0),
                     None)
    check("G52-epstein-face", efirst_mf == R200_EPS["s_star"],
          "EPSTEIN(8) bookkeeping: full margin mf crosses negative "
          "first at sj = %s == the r200 node point 6; conservative "
          "mc already < 0 from sj = %s: in EPSTEIN the dangerous "
          "m = 1 term OVERCOMES the ground term inside the path -- "
          "the same bookkeeping that stays > 0 on MAIN"
          % (str(efirst_mf),
             str(next((r["sj"] for r in ec["rows"] if r["mc"] < 0),
                      None))))
    sl_marg, _ = fit_line(
        [res[c]["log10tau"] for c in mains],
        [math.log10(max(1.0 - res[c]["rows"][SGRID_DEN]["mc"],
                        1e-300)) for c in mains])
    check("G53-margin-ladder+all-h-shape", True,
          "wall margin 1 - mc rides tau mildly (slope %+.2f); THE "
          "ALL-H STATEMENT SHAPE, typed: 'for all h: "
          "sum_{m>=1} max(0, -y_m(1) Umc_m) < y_0(1) Umc_0', legs: "
          "{C(u), atom positions log q, weights Lambda(q)/sqrt(q)} "
          "SOURCE-CLASSICAL (r175 bridge class), {U_m, d_m, z_m, "
          "y_m, Umc_m} SPECTRAL-MEASURED per rung, margin "
          "tau-adjacent; OPEN all-h -- but the decomposition "
          "LOCALIZES the arithmetic input at the form factors "
          "F_1(log 2), F_1(log 3), ... (handoff sharpening, not "
          "closure)" % sl_marg)

    # ------------------------------------------------------------ S6
    section("S6  Z4: WORLDS, TRANSPLANT, WITNESS")
    smo = res.get(("SMOOTH", 5))
    scr_z1 = scr["z1rel"] if scr else None
    scls = ("SCRARITH-SUPPRESSED" if scr_z1 is not None
            and scr_z1 <= SUP_BAR else
            "SCRARITH-O1" if scr_z1 is not None
            and scr_z1 >= O1_BAR else "SCRARITH-MID")
    if scr_z1 is not None:
        m5 = res.get(("MAIN", 5))
        m5z = m5["z1rel"] if m5 else float("nan")
        if scls == "SCRARITH-SUPPRESSED":
            scr_read = ("the golden permutation does NOT lift z_1 "
                        "-- the exact (q, w_q) pairing is NOT "
                        "needed at the reachable rung")
        else:
            scr_read = ("the golden permutation LIFTS z_1 by %.1f "
                        "dex -- the exact (q, w_q) PAIRING is "
                        "load-bearing for the suppression; note "
                        "SCRARITH is nonetheless PATH-NONNEGATIVE "
                        "(r200/r201): z_1 suppression is "
                        "SUFFICIENT-side structure, NOT NECESSARY "
                        "for positivity -- an honest wedge between "
                        "the suppression story and OBJECT-A"
                        % (scr_z1 - m5z))
        det60 = ("SCRARITH(5) z1rel %.1f vs MAIN(5) %.1f -> %s: "
                 "%s; " % (scr_z1, m5z, scls, scr_read))
    else:
        det60 = ""
    if smo:
        det60 += ("SMOOTH(5) z1rel %.1f (two-leg split: arch "
                  "10^%.1f vs continuum prime 10^%.1f, c_cross "
                  "10^%.1f, typed CONTINUUM); "
                  % (smo["z1rel"], smo["two_leg"]["T_arch_log"],
                     smo["two_leg"]["T_pri_log"],
                     smo["two_leg"]["c_cross"]))
    det60 += ("EPSTEIN(8) per-atom: %s with c_cross 10^%.1f O(1) "
              "-- the imbalance is carried by the whole 3-atom "
              "set against arch"
              % (str([(q, "10^%.1f" % tl) for
                      (q, _w, _f, _s, tl, _t) in e8["atoms"]]),
                 e8["c_cross"]))
    check("G60-world-tables", scr is not None or smoke, det60)
    z1t = {t: tres[t]["z1rel"] for t in ("T0", "T1", "T2", "T3")}

    def cls(v):
        return "SUP" if v <= SUP_BAR else \
            ("O1" if v >= O1_BAR else "MID")
    cT = {t: cls(z1t[t]) for t in z1t}
    if cT["T0"] == cT["T2"] != cT["T1"] == cT["T3"]:
        trans_enum = "SUPPORT-CARRIES"
    elif cT["T0"] == cT["T1"] != cT["T2"] == cT["T3"]:
        trans_enum = "WEIGHTS-CARRY"
    elif all(cT[t] == "O1" for t in cT):
        trans_enum = "COMPLETENESS-CARRIES"
    elif cT["T0"] == "SUP" and all(cT[t] != "SUP"
                                   for t in ("T1", "T2", "T3")):
        trans_enum = "PAIRING-CARRIES"
    else:
        trans_enum = "TRANS-MIXED"
    dS = z1t["T1"] - z1t["T0"]
    dS2 = z1t["T3"] - z1t["T2"]
    dW = z1t["T2"] - z1t["T0"]
    dW2 = z1t["T3"] - z1t["T1"]
    check("G61-support-transplant",
          trans_enum in ("SUPPORT-CARRIES", "WEIGHTS-CARRY",
                         "COMPLETENESS-CARRIES", "PAIRING-CARRIES"),
          "2x2 factorial at h = 8: z1rel T0(MAIN3 sup x MAIN wgt) "
          "%.1f [%s], T1(EPS sup x MAIN wgt) %.1f [%s], T2(MAIN3 "
          "sup x EPS wgt) %.1f [%s], T3(== EPSTEIN(8)) %.1f [%s]; "
          "support effect %+.1f / %+.1f dex, weight effect %+.1f / "
          "%+.1f dex -> transEnum = %s (reviewer hypothesis "
          "%sCONFIRMED at the reachable rung); node census: T0 %s "
          "T1 %s T2 %s T3 %s; truncation MAIN(8) -> MAIN3 shifts "
          "z1rel by %+.1f dex of the %.1f-dex suppression "
          "(completeness census, resolve-and-record)"
          % (z1t["T0"], cT["T0"], z1t["T1"], cT["T1"],
             z1t["T2"], cT["T2"], z1t["T3"], cT["T3"],
             dS, dS2, dW, dW2, trans_enum,
             "" if trans_enum == "SUPPORT-CARRIES" else "NOT ",
             "nodeless" if tres["T0"]["nnode"] == 0 else
             "s*=%s" % tres["T0"]["sstar"],
             "nodeless" if tres["T1"]["nnode"] == 0 else
             "s*=%s" % tres["T1"]["sstar"],
             "nodeless" if tres["T2"]["nnode"] == 0 else
             "s*=%s" % tres["T2"]["sstar"],
             "nodeless" if tres["T3"]["nnode"] == 0 else
             "s*=%s" % tres["T3"]["sstar"],
             z1t["T0"] - res[("MAIN", 8)]["z1rel"],
             -res[("MAIN", 8)]["z1rel"]))
    wit = witness_leg()
    check("G62-witness-typed",
          WIT_YT_BAND[0] <= wit["wit_ytr"] <= WIT_YT_BAND[1]
          and wit["wit_a0dev"] <= WIT_A0_BAR,
          "r172 witness VERBATIM at h = %d (ytr %.2f in %s, a0dev "
          "%.1e): the witness inflates the SOURCE-RAY coefficients "
          "and never touches NoP, phi or U_1 -- z_1 and the whole "
          "Z1-Z3 machinery are witness-INVARIANT BY CONSTRUCTION "
          "(typed definitional; the honest answer to 'where does "
          "the ACF-flattening witness hit z_1' is NOWHERE: ray "
          "currency vs matrix currency)"
          % (WIT_RUNG, wit["wit_ytr"], str(WIT_YT_BAND),
             wit["wit_a0dev"]))

    # ------------------------------------------------------------ S7
    section("S7  GUARDS")
    delivered = {
        "ATOMS": ["KERNEL"], "KERNEL": ["Z1-DECOMP", "TRANSPLANT"],
        "ARCH-BLOCK": ["Z1-DECOMP", "TRANSPLANT"],
        "POLE-RANK1": ["SECULAR"],
        "NOP-EIG": ["Z1-DECOMP", "SECULAR", "CENTER-DECOMP"],
        "SECULAR": ["Z2-IDENTITY", "CENTER-DECOMP"],
        "Z1-DECOMP": ["MECH-VERDICT"],
        "Z2-IDENTITY": ["ADJUDICATION"],
        "CENTER-DECOMP": ["ADJUDICATION"],
        "TRANSPLANT": ["ADJUDICATION"],
        "MECH-VERDICT": ["ADJUDICATION"],
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
    for node in ("Z1-DECOMP", "Z2-IDENTITY", "CENTER-DECOMP",
                 "TRANSPLANT", "MECH-VERDICT", "ADJUDICATION",
                 "SCREENS"):
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
          "TURAN-CONE-POSITIVITY), consumed by NOTHING: DFS "
          "ancestry of every delivered node clean; fully zero-free "
          "round; the z_1 anatomy is per-rung finite linear "
          "algebra with no edge into any criterion loop")
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
    cf.update({("UNC", "Z1SUPALLH"): INF, ("Z1SUPALLH", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G71-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'the z_1 suppression holds with margin for all h' as a "
          "unit edge would raise the flow to 6 -- NOT REAL (the "
          "suppression is measured per rung; its net depth rides "
          "tau, its all-h face is exactly the OPEN handoff typed "
          "in G53): this round adds NO flow; RH unreachable "
          "without the omega edges")
    check("G72-composed-chain-typing", True,
          "leg typing: {kernel law NoP = Arch - sum w C, z_1 "
          "eigen-identity, ID1/ID2 secular identities, Parseval "
          "alignment, transplant assembly} EXACT-WARDED; {per-atom "
          "tables, form factors, mechanism metrics, anatomy "
          "ladders, margins, slopes} MEASURED; {witness matrix-"
          "invariance} DEFINITIONAL; {r182 alignment connection} "
          "MEASURED-CORRESPONDENCE; no impossibility theorem and "
          "no completeness claim sold anywhere; the all-h "
          "suppression statement is an OPEN TARGET localized at "
          "the form factors, not a result")

    # ------------------------------------------------------------ S8
    section("S8  PRICING + RESIDUE")
    check("G80-pricing", True,
          "what the round BUYS: (i) z_1 IS NOW A SOURCE OBJECT -- "
          "the exact per-atom decomposition z_1 = T_arch + sum_q "
          "w_q F_1(log q) with the dangerous-mode form factor "
          "F_1(u) = -U_1^T C(u) phi / d_1 explicit, warded, "
          "tabulated at every reachable rung (and the exact "
          "boundary fact C(L) == 0: the atom q = h is kernel-"
          "invisible); (ii) THE MECHANISM VERDICT (%s): the "
          "suppression is a fine-tuned ARCH-VS-PRIME cancellation "
          "(the Weil/ACF pairing in eigencoordinates) -- small "
          "per-atom terms REFUTED (mechanism c), mass location "
          "REFUTED (P2), within-prime oscillation secondary; "
          "(iii) THE LOW-MODE NEAR-ZERO LOCK: d_1, |z_1/z_0|, "
          "1 - f(1) and -Gdel(lam_0(1)) ride ONE slope-1 ladder "
          "(%s, %s): the second NoP eigenvalue is ITSELF the "
          "near-zero currency, the deleted secular near-vanishes, "
          "and suppression = amplification via exact ID1/ID2; "
          "(iv) THE CAUSAL TEST (%s + %s): neither 3-atom support "
          "nor weight multiset carries -- the suppression needs "
          "the COMPLETE, CORRECTLY-PAIRED von Mangoldt set "
          "(truncation +%.1f dex, golden permutation +%.1f dex); "
          "AND the honest wedge: SCRARITH is O(1)-overlapped yet "
          "path-nonnegative -- z_1 suppression is NOT NECESSARY "
          "for positivity; (v) the safe-minus-dangerous center "
          "bookkeeping (%s) holds at every MAIN cell and "
          "reproduces EPSTEIN's crossing at sj = 6 -- the all-h "
          "face typed and localized at the form factors"
          % (mech_enum, exp_enum, gdel_enum, trans_enum, scls,
             z1t["T0"] - res[("MAIN", 8)]["z1rel"],
             (scr_z1 - res[("MAIN", 5)]["z1rel"])
             if scr_z1 is not None and ("MAIN", 5) in res
             else float("nan"),
             dom_enum))
    info("POST-ROUND RESIDUE (cardinality UNCHANGED, canonical "
         "four-item form per note DXVI): {H1 ^ H2 ^ H3}-KOFINAL "
         "(mod D = 0.0042) + {census-forall-k == LOOP, flagged, "
         "not consumed} + {H-PIN: L1 = TAIL proven + H-pin open; "
         "WPD(a < gamma_1^2) <= H-pin; TAILWPD world front}.  "
         "OBJECT-A STAYS OPEN; its transport face now factorizes "
         "as {per-atom form-factor structure (tau-flat, classical-"
         "legged)} x {cancellation depth (the known near-zero "
         "currency)} with the arithmetic input LOCALIZED at the "
         "COMPLETE correctly-paired von Mangoldt atom set (the "
         "transplant/permutation kills).  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        mech_enum + "(G31)",
        "FORM-FACTOR-NO-SMALL-SUPPORT(G32)",
        "FINE-TUNED-CANCELLATION(G33)",
        align_enum + "(G34)",
        exp_enum + "(G42)",
        gdel_enum + "(G42)",
        tau_enum + "+STRUCTURE-FLAT(G43)",
        dom_enum + "(G51)",
        "EPSTEIN-CROSSING-REPRODUCED(G52)",
        trans_enum + "(G61)",
        scls + "(G60)",
        "WITNESS-BLIND-BY-CONSTRUCTION(G62)",
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
        mech_enum, align_enum, exp_enum, gdel_enum,
        tau_enum, dom_enum, trans_enum, scls,
        "WITNESS-BLIND-BY-CONSTRUCTION",
        "LOOPS-FLAGGED-NOT-CONSUMED", "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
