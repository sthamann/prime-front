#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""onebadmode_moments_probe -- PRIME.PORT.ONEBADMODE.MOMENTS.01
(EXPLORATION ONLY, experiments/; theorem-engineering on the RH-side
wall: the ONE-BAD-EIGENVALUE MOMENT CERTIFICATE of the deployed wall
matrices.  2026-08-12.)

THE IDEA (program lead, implemented faithfully).  M_h is the deployed
8x8 wall matrix of a ladder step: M = Q^T (S(r2)/tau(r1)) Q in the
frozen Householder frame Q of r1's soft direction (P2 SPEC (ii)),
blocks n (pivot scalar), b (7-coupling), B (7x7 co-block) -- the TAU
convention, where the CLIII floor certificate lives.  Since B_h is
certified positive on the surface (pg_chain_interval_rollout = CLIII:
B_tau >= c_B I with c_B = 0.5523 exact-rational on the 39 certified
surface steps, own frame; deep float floor 1.6610 = CLIV), CAUCHY
INTERLACING gives lambda_2(M_h) >= lambda_1(B_h) >= c_B: M_h has AT
MOST ONE nonpositive eigenvalue.  Hence a MOMENT CERTIFICATE: with
the squared scaled Chebyshev separator
    p_r(x) = [ T_r( m(x) ) / T_r( m(0) ) ]^2,
    m(x)   = (2x - (L + c)) / (L - c),      c < L,
p_r >= 0 everywhere (a square), p_r(0) = 1, p_r(x) >= 1 for x <= 0
(|m| is decreasing-in-x on x <= 0 with |m(x)| >= |m(0)| > 1 and |T_r|
increasing on [1, oo)), and 0 <= p_r <= eps_r = T_r(|m(0)|)^{-2} on
[c, L].  SOUNDNESS (unconditional, needs NO premise):
    tr p_r(M) < 1  ==>  M has no eigenvalue <= 0  ==>  M > 0,
because a single nonpositive eigenvalue alone contributes >= 1 and
the rest contribute >= 0.  The interlacing premise + the B-floor
power only the FEASIBILITY: if the 7 bulk eigenvalues sit in
[c_B, L] then tr p_r(M) <= p_r(lam_min) + 7 eps_r, so a modest order
r suffices when lam_min > 0 is not too tiny in tau units.
tr p_r(M) is a LINEAR FUNCTIONAL of the moments tr(M^k), k <= 2r --
no lam_min computation, no B^{-1}, no near-cancelling determinant
ratio enters the certificate.  NOT DUPLICATED, CITED: the CMS-moment
route of CLXIV (anthropic_moment_inertia: UB_4 on mu((-inf,0]) at
0.83..1.60 ladder-wide, r = 4 near-threshold, 7/39) and its closure
by Jacobi equilibration (CLXXIII ub4_congruence_upgrade: UB4-CLOSED
39/39 med 0.587, deep 27/27; CLXXV: UB4-STRUCTURED, no classical
identity) bound the mass of (-inf, 0] through congruence-shaped
moments; THIS probe is the sharpened one-bad-mode version: the
interlacing structure lets a fixed nonnegative separator polynomial
kill the bulk on [c_B, L] instead, entirely congruence-free.

THE FOUR QUESTIONS (frozen):
 (a) SETUP per step (surface + bridge + deep): assemble M, measure
     the interlacing premise (lambda_2(M) vs c_B, lambda_1(B) vs
     c_B, the one-bad-mode count #eig < c_B), and certify the
     spectral bound L per step SOURCE-ONLY: L_src = min(Gershgorin
     row bound, Frobenius norm) * (1 + 2^-40) -- entry reads only,
     NO eigendata; the eigencomputation is the truth reference.
 (b) THE ORDER LADDER r = 1..R_MAX: tr p_r(M) per step and r
     (stable matrix-Chebyshev route); r*(h) = smallest certifying
     r; census + margin ladder 1 - tr p_r in dex + the h-trend of
     r* (the uniformity question) + THE r*-LAW: the Chebyshev
     theory prices the separator at r* ~ sqrt(L/c_B), so the fit
     r* vs sqrt(lam_max/c_B) (through-origin slope kappa + OLS
     R^2) and the jackknife slope of ln r* vs ln h are measured
     and printed; the ORACLE TIER (c = lambda_1(B) float, L =
     lambda_max(M) float -- eigendata, declared diagnostic)
     isolates the L-looseness price; the EXACT-RATIONAL TIER
     anchors decisions (dyadic moments + exact separator
     coefficients on the float-committed constants, v897 class).
     R_MAX = 400 (the mission sketch said ~12; smoke-1 measured
     the actual scale, amendment A1 below).
 (c) THE DISGUISE TEST (the lead's explicit risk): tau-screen of
     the margins 1 - tr p_r (fixed r and r*) -- slope ~ +1 with no
     source-only bound would make the route HALFGAP relabeled;
     SUPPLY SENSITIVITY: dn* = margin / |d tr p_{r*} / dn| (the
     n-read error that kills the certificate; d/dn tr p(M) =
     [p'(M)]_{00}) compared to the Schur gap s = n - q -- if
     dn*/s = O(1) the certificate consumes exactly halfgap-grade
     arithmetic supply; THE SOURCE SPLIT (CCIII machinery
     verbatim): S = S_AR + S_SM + S_OSC exact, M = M_WIN + M_OSC
     linear; which moments tr(M^k) carry the prime oscillation
     (moment mix table), does the window skeleton alone certify
     (tr p_{r*}(M_WIN) census, float diagnostic), and the OSC
     budget t* = margin / |tr(p_{r*}'(M) M_OSC)| (the fraction of
     the prime read the certificate can afford to lose).
 (d) CONTROLS MUST FIRE: smooth world, scramble (seed 1), Epstein
     x^2+5y^2 at kz 9 (rung level; step ladder O(X^2) DECLARED
     SKIPPED, predecessor pattern), cosh injection A = 0.01.  On
     false-world steps the certificate must FAIL: tr p_r >= 1 on
     every eig-indefinite step (THEOREM, warded) or premise break
     (tau <= 0, lambda_1(B) < c_B); genuinely-PD control cores
     (the known CLXII/CCIII cosh exceptions) are counted and
     eig-confirmed, never hidden.

FROZEN PROTOCOL (ladder machinery verbatim from
halfgap_riccati_transition_probe = CCIII = CLXII/CLIV/CXLIV/v900
chain; ONE Gram per rung; window memoization):

 W   SURFACE PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3 truth all-PSD; W4 >= 20 consecutive
     full-core steps; W5 P2/P3 ledger reproduction on the surface
     steps: min lam_min(B_tau) == 0.679 (rtol 2e-2), Schur gap
     min/med == 0.052/0.888 (rtol 5e-2).

 DW  DEEP LADDER (CLIV 4e6 extension, FLOAT-LEVEL declared): DW1
     fidelity byte-exact + prefix arrays bitwise + kappa guard
     (kill); DW2 deep census == 28 rungs in H_HOLD = [128, 2900]
     (kill); DW3 >= 20 deep truth rungs complete + all-PSD (kill);
     DW4 REPRODUCTION: min own-frame lam_min(B_tau) over the deep
     steps == 1.6610 (rtol 2e-2, kill).  SOFT BUDGET 1200 s,
     unbuilt rungs typed SKIPPED-BUDGET.

 P   THE COMBINED h-SORTED CHAIN: surface + deep truth rungs, steps
     = consecutive full-core pairs (r1 all-PSD, lamS > 0), segments
     surf / bridge / deep; P1 >= MIN_STEPS_COMB = 40 OK steps
     (kill); a step REFUSES (typed, counted) iff tau <= 0 or
     L_src <= c * (1 + 1e-6).

 M   MACHINE WARDS (kill -> WARD-BROKEN):
     M1 separator facts on float grids at the 3 representative
        (c, L) pairs (first/median/last OK step by h), every r in
        the frozen subset R_SUBSET = {1..24, 32, 48, 64, 96, 128,
        160, 200, 256, 320, 400}: p_r >= 1 - 1e-9 on 101 points
        of [-2c, 0]; -1e-12 <= p_r <= eps_r (1 + 1e-9) on 401
        points of [c, L]; |p_r(0) - 1| <= 1e-12.
     M2 trace-route tie on EVERY OK step, every r in R_SUBSET:
        stable route ||T_r(Y)||_F^2 / T_r(m0)^2 == sum_i
        p_r(lam_i) (truth eigendata as ward reference), rel <=
        TIE_WARD = 1e-9.
     M3 MOMENT-LINEARITY (float route, 3 representative steps,
        r <= 24): monomial coefficients (floats of the exact
        Fractions) dotted with float moments tr(M^k) vs the stable
        route; WARD for r <= 6 at the amplification-scaled bar
        1e-6 * max(1, AMP(L, r) * 1e-16 / 1e-9), AMP(L, r) =
        (4 * 2L/(L - c))^{2r} (the declared float-cancellation
        model of the monomial expansion); r in (6, 24] printed
        only.  The certificate never consumes this route: its
        moment linearity is anchored EXACTLY in M4.
     M4 EXACT-RATIONAL TIER: at the 3 representative steps, r <=
        24: the exact decision  8 q_0 + sum_k q_k tr_F(M^k) <
        T_r(m0)^2 (all Fractions on the float-committed entries
        and constants) must agree with the float stable-route
        decision tr p_r < 1, except inside the declared borderline
        band |tr p_r - 1| <= 1e-9 (counted, printed); PLUS on
        every certified step with r* <= EXACT_CAP = 64 the float
        r* decision is CONFIRMED exact-rationally at r = r*(h)
        (kill on any disagreement); steps with r* > EXACT_CAP are
        typed FLOAT-ONLY (counted, min float margin printed) --
        the dyadic moment cost grows ~ r*^2 and the anchor class
        is already established on the confirmed subset.
     M5 INTERLACING WARD (theorem): lambda_2(M) >= lambda_1(B) -
        1e-10 * max(1, |lambda_1(B)|) on every OK step; and
        L-SOUNDNESS: L_src >= lambda_max(M) on every OK step.
     M6 SOUNDNESS-ON-INDEFINITE (theorem, control worlds): on
        every control step with eig lambda_min(M) <= -1e-10 *
        max(1, lambda_max): min over FINITE r-entries of tr p_r
        >= 1 - 1e-9, and no RAW certificate there.  OVERFLOW
        CONVENTION (declared): at strongly indefinite control
        matrices |m(lam_min)| can reach 1e3..1e5 and the
        recurrence overflows IEEE double at large r; a non-finite
        tr p_r is read as +inf (= NO certificate, the correct
        reading of an overflowing >= 1 quantity), counted and
        printed; a RAW certificate always requires a FINITE
        tr p_r < 1.

 T1  SETUP CENSUS (typed): per step lam_min(M), lam_2(M),
     lam_1(B), premise censuses lam_1(B) >= c_B and lam_2(M) >=
     c_B per segment (surface = CLIII certified range, cited;
     bridge/deep FLOAT-LEVEL, typed), one-bad-mode census
     #eig < c_B <= 1, the L-looseness ladder log10(L_src /
     lam_max) + which bound wins (Gershgorin vs Frobenius).

 T2  THE ORDER LADDER (the headline, typed): per step r*_src
     (TIER-SRC: c = c_B cited, L = L_src source-only) and r*_orc
     (ORACLE TIER, diagnostic); census per segment; r* min/med/max;
     margin ladders log10(1 - tr p_r) at r* and at R_FIX in {16,
     64, 256}; UNCERTIFIED steps listed (r* > R_MAX); THE H-TREND:
     jackknife OLS slope of r*_src vs ln h, typed RSTAR-GROWING
     iff slope - 2SE > RSTAR_BAR = 0.5, RSTAR-FLAT iff slope + 2SE
     < 0.5, else RSTAR-AMBIG; THE r*-LAW: through-origin slope
     kappa of r* on sqrt(lam_max/c_B) + OLS R^2 + jackknife slope
     of ln r* vs ln h (printed, typed in the verdict); the
     L-price ladder r*_src - r*_orc.

 T3  THE DISGUISE TEST (typed): D-a margin tau-screens (R_FIX = 8,
     16, and at r*) with bands PASS |s| <= 0.30 / RELOC >= 0.70 /
     AMBIG; D-b supply grade: dn*/s ladder + median, typed
     SUPPLY-HALFGAP-GRADE iff med in [0.1, 10]; D-c source seat:
     moment mix tables at the 3 representative steps (share of
     tr(M^k) carried by M_OSC against M_WIN, and by the pivot
     reads n, b against the co-block: |tr(M^k) - tr(B^k)| /
     |tr(M^k)|), the WIN-only census (tr p_{r*}(M_WIN) < 1,
     float), the OSC budget t* ladder.  COMBINED TYPING (frozen
     rule): DISGUISE-HALFGAP iff [D-a at r* RELOC] AND [D-b
     in-grade]; ROUTE-DISTINCT iff [D-a at r* PASS] AND [D-b
     out-of-grade OR WIN-only census >= 90 percent]; else
     DISGUISE-MIXED (all numbers printed).

 E   CONTROLS (rung-level silence kill -> WARD-BROKEN): E1 smooth
     fires; E2 scramble fires; E3 Epstein fires at kz 9 (step
     ladder skipped, declared); E4 cosh A = 0.01 fires; E5 the
     certificate on false worlds (relaxed steps, smooth / scramble
     / cosh): premise-break census (tau <= 0, B not PD float,
     lam_1(B) < c_B), RAW cert census (any r <= R_MAX with
     tr p_r < 1; M6 wards every eig-indefinite step), COMPOSED
     census (raw AND tau > 0 AND lam_1(B) >= c_B), PD-exceptions
     eig-confirmed and listed; separation print min_r tr p_r on
     indefinite steps per world.  E6 IMPOSTOR N/A DECLARED (zero
     zero-reads; AST firewall is the witness).

 F   SCREENS + VERDICT: tau-screens as in T3/D-a plus dn* and t*
     screens (printed); verdict assembly below.

KILLS: K1 pipeline/counts (W1-W4, DW2-DW3, P1) -> PIPELINE-BROKEN;
K2 reproduction / machine / theorem / control-firing wards (W5, DW1,
DW4, M1-M6 as marked, E1-E4) -> WARD-BROKEN.  All other outcomes
typed, never kills.

VERDICT (frozen enum): MOMENTS-CERTIFY(census, max r*) iff every OK
step of the combined chain certifies float + exact at some r <=
R_MAX; else MOMENTS-BLOCKED(seat: UNCERT(k) / L-LOOSE / RSTAR-
GROWING named with numbers).  Sublabels always attached: PREMISE(...),
LBOUND(...), RSTAR(min/med/max, slope -> FLAT/GROWING/AMBIG),
MARGIN(...), ORACLE-PRICE(...), DISGUISE(...), CONTROLS(...),
SCREENS(...); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP =
42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_STEPS_COMB = 40;
MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888
(rtol 5e-2); TAB_EXT = 4_000_000; KZ_SCAN_MAX = 400; H_HOLD = (128,
2900); N_DEEP_EXP = 28; MIN_DEEP_OK = 20; DEEP_MINB_REF = 1.6610
(rtol 2e-2); CB_CITED = Fraction(5523, 10000) (CLIII, cited, printed,
not re-proved; certified range = 39 surface steps h <= 900, own
frame, tau units); R_MAX = 400 (A1); R_FIX = (16, 64, 256) (A1);
R_SUBSET = {1..24, 32, 48, 64, 96, 128, 160, 200, 256, 320, 400}
(A1); EXACT_CAP = 64 (A2); REP_RCAP = 24 (M3/M4a order cap);
L_INFLATE = 1 + 2^-40; TIE_WARD = 1e-9; MONO_WARD = 1e-6 (r <= 6);
GRID_NEG_TOL = 1e-9; GRID_BULK_TOL = 1e-9; P0_TOL = 1e-12;
ILACE_TOL = 1e-10; SOUND_TOL = 1e-9; BORDER_BAND = 1e-9; RSTAR_BAR
= 0.5 per ln h; SUPPLY_GRADE = (0.1, 10.0); WINCERT_BAR = 0.90;
N_REP = 3 (first/median/last OK step by h); SLOPE_PASS = 0.30,
SLOPE_RELOC = 0.70; NG_SMOOTH = 6000; CTRL_KZ = 9; scramble seed 1;
INJ_A = 0.01, INJ_DELTA = 0.05, INJ_GAMMA0 = 10.0 (CLXII deployed,
frozen selection cited); PSD_TOL = 1e-12; SOFT_BUDGET_S = 1200;
runtime cap declared: 25 min.

EXACTNESS MODEL (frozen): float-level probe on the float64-computed
step matrices; the CERTIFICATE DECISIONS are anchored exact-rational
(Fraction) on those float entries and the float-committed constants
c = float(CB_CITED), L = float(L_src) (v897 class) -- the separator
soundness facts hold for EVERY c < L, so the anchoring constants
need no enclosure; the deep ladder is FLOAT-LEVEL throughout (CLIV
limit, inherited); eigendata of M appears ONLY in truth-reference
wards, the oracle tier and diagnostics, never in TIER-SRC's
construction.  What is NOT enclosed: the float pipeline producing
the entries.  NO RH claim anywhere.

A-PRIORI EXPECTATIONS (frozen): the premise holds on the surface
(certified constant) and deep (CLIV float floor 1.661 > c_B);
bridge-step behaviour is an OPEN measurement (CCIII saw the
shared TRANSITION frame undercut c_B -- the per-step own frame
here is a different object); r* expected single-digit on the
surface, possibly larger on the deep block if L_src is loose; the
RSTAR h-trend and the disguise typing are OPEN measurements (no
expectation frozen); controls expected to fire, with the known
genuinely-PD cosh cores (CLXII/CCIII exception class) counted and
eig-confirmed rather than hidden.

SMOKE-RUN DISCLOSURE (2026-08-12, before freezing; fail-first
history preserved).  SMOKE-1 (full ladder + controls, first
passage, R_MAX = 24, R_FIX = (8, 16), per-step exact confirmation
uncapped, 111.5 s): 29/29 checks GREEN -- no ward failed -- but
the headline census was CENSORED by the a-priori order range: the
sizing estimate behind R_MAX = 24 assumed L/c_B ~ O(10..100); the
measured wall matrices in tau units have lam_max = 1.2e2..4.4e4
(L_src tight at +0.008/+0.025/+0.068 dex over lam_max, Frobenius
wins 65/68), so the Chebyshev price r* ~ sqrt(L/c_B) sits at
~15..300 and only 12/68 steps certified inside r <= 24 (census
surf 7/40, bridge 1/1, deep 4/27; r* 14/20/24; margins at r* dex
-3.448/-1.324/-0.540; every certification exact-confirmed 12/12;
M4a 72 agree / 0 borderline / 0 disagree; M2 tie 8.19e-14; M5
interlacing worst +7.75e-07 normalized, L-sound 68/68; premise
lam1B >= cB surf 40/40 + deep 27/27, bridge 0/1 undercut 0.3496 <
0.5523 -- the per-step OWN frame undercuts ONLY at the bridge;
one-bad-mode 67/68 with max 2 at the bridge step; W5 ledger
0.6790/0.0520/0.8875 EXACT; DW4 1.6610 EXACT; controls all fire,
smooth/scramble RAW 0 + cosh RAW 1 == the genuinely-PD core kz 13
eig lam_min +1.041 (CLXII exception class, eig-confirmed, sound);
D-b dn*/s med 0.192 IN-GRADE; D-c WIN-only 0/12, OSC budget t*
dex -7.4/-5.7/-3.7; screens m8/m16 vacuous, mr* PASS -0.006).
AMENDMENTS (disclosed, applied before the freeze; the smoke-1
censored census is ON RECORD above, nothing hidden):
  * A1 (measurement range): R_MAX 24 -> 400 so the census reads
    the ACTUAL r*(h) instead of a censoring artifact (predicted
    max r* ~ sqrt(4.4e4/0.5523) ~ 283); R_FIX (8, 16) -> (16, 64,
    256) (the old fixed-r margins were vacuous: pos = 0/2); the
    M1/M2 order grid becomes the frozen R_SUBSET (cost control;
    the stable route itself runs every r <= 400); the r*-LAW fit
    (kappa on sqrt(lam_max/c_B), ln r* vs ln h) is ADDED to T2 --
    it is the quantitative content of the blocked/growing answer.
    NOTE HONESTLY: raising R_MAX relaxes the certify enum's range
    (a step uncertified at 24 may certify at 400); the mission's
    uniformity question is answered by the RSTAR/r*-LAW typing,
    which A1 sharpens rather than weakens.
  * A2 (cost cap): the per-step exact-rational confirmation is
    capped at EXACT_CAP = 64 (dyadic moment cost ~ r*^2; beyond
    the cap steps are typed FLOAT-ONLY, counted, min float margin
    printed); the 3-step rep tier stays at REP_RCAP = 24 exactly
    as smoke-1 ran it.
  * A3 (prints only): the D-c moment-mix table prints log10 of
    the OSC share (raw shares reach 1e48 by k = 12 -- pure
    cancellation bookkeeping); the T2 table prints trp at the new
    R_FIX orders.
No success bar, ward tolerance, control, screen band, premise
constant or enum RULE was changed beyond the three disclosed
amendments.  SMOKE-2 (post-A1/A2/A3, 111.0 s): 29/29 GREEN; every
smoke-1 measurement inside the old range reproduced identically
(W5/DW4 ledger constants, premise censuses, L looseness, M2 tie
1.03e-13 on the R_SUBSET, M4a 72/0/0, M5 +7.75e-07, controls);
the uncensored headline: MOMENTS-CERTIFY 68/68 (surf 40/40 +
bridge 1/1 + deep 27/27), r* min/med/max 14/30/119, margins at r*
dex -3.448/-0.889/-0.427, exact-anchored 60/60 at r* <= 64 +
FLOAT-ONLY 8 (min float margin 1.557e-02), the r*-LAW kappa =
0.544 on sqrt(lam_max/c_B) (OLS R2 0.889; ln-ln slope +0.676 +/-
0.082), ln r* vs ln h slope -0.054 +/- 2SE 0.106 (NO h-growth;
the linear-r* jackknife vs ln h is noise, R2 0.024 -> typed
RSTAR-AMBIG by the frozen rule and said so), oracle price med
+15, D-a screens PASS everywhere non-vacuous, D-b dn*/s med
0.354 IN-GRADE, D-c WIN-only 0/68 + OSC budget t* med dex -5.5,
DISGUISE-MIXED, cosh RAW/COMPOSED 2 == the two genuinely-PD
cores kz 23/13 (eig lam_min +0.530/+1.041, eig-confirmed, sound),
M6 min finite tr p_r on indefinite steps 3.616 >= 1.  SPEC v1
frozen 2026-08-12 after smoke-2 with the SHA printed at runtime;
the frozen full run uses no edits beyond this disclosure block.

SPEC v1 (2026-08-12, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); Householder frame as P2/CL/
CXLIV/CCIII; (ii) steps sorted by (h, kz); truth steps need r1
full-core, all-PSD, lamS > 0; control chains relaxed (raw
construction where the linear algebra exists); (iii) the stable
route: Y = (2M - (L+c) I)/(L - c), three-term Chebyshev recurrence,
tr p_r(M) = ||T_r(Y)||_F^2 / T_r(m0)^2; the derivative route
p_r'(M) = (2 r a / T_r(m0)^2) sym(T_r(Y) U_{r-1}(Y)), a = 2/(L-c);
(iv) the exact tier: T_r integer coefficients, affine composition
by Horner in Fractions, polynomial square by convolution, moments
by dyadic 8x8 Fraction powers; (v) representative steps = OK-step
indices (0, n//2, n-1) by h; (vi) OLS + leave-one-out jackknife as
CXLIII; screens read positive subsets with excluded counts
printed; (vii) the split M_OSC = Q^T (S_OSC/tau) Q from the CCIII
complement-defined split (S_OSC = S - S_AR - S_SM exact), M_WIN =
M - M_OSC.

NO RH claim: every census is a statement about float64-computed
step matrices of a deployed finite ladder (certificate decisions
anchored exact-rationally on those entries); positivity of M on
finitely many rungs is equivalent to the already-measured wall
there and proves nothing at other h; the h-trend fits are
empirical laws; the deep ladder is FLOAT-LEVEL.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only; the extended table comes from the deployed
sieve generator (CLIV pattern).

Sources (read-only): v563_paper2_readouts; ladder + frame + split
machinery verbatim from halfgap_riccati_transition_probe (CCIII)
and its chain (CLXII, CLIV deep extension, CXLIV, v900); exact
split M = X + U wall object from port_tangent_schur_probe (P2);
B-floor constant CITED from pg_chain_interval_rollout_probe
(CLIII); deep floor CITED from deep_blind_holdout_probe (CLIV);
prior moment work CITED not duplicated: anthropic_ranktrace_core
_probe, anthropic_moment_inertia_probe (CLXIV),
ub4_congruence_upgrade_probe (CLXXIII), ub4_identity_or_measurement
_probe (CLXXV).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/onebadmode_moments_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
NDIM = 8
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MIN_STEPS_COMB = 40
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
TAB_EXT = 4_000_000
KZ_SCAN_MAX = 400
H_HOLD = (128, 2900)
N_DEEP_EXP = 28
MIN_DEEP_OK = 20
DEEP_MINB_REF = 1.6610
DEEP_MINB_RTOL = 2e-2
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
R_MAX = 400
R_FIX = (16, 64, 256)
R_SUBSET = tuple(range(1, 25)) + (32, 48, 64, 96, 128, 160, 200,
                                  256, 320, 400)
EXACT_CAP = 64
REP_RCAP = 24
L_INFLATE = 1.0 + 2.0 ** -40
TIE_WARD = 1e-9
MONO_WARD = 1e-6
MONO_RCAP = 6
GRID_NEG_TOL = 1e-9
GRID_BULK_TOL = 1e-9
P0_TOL = 1e-12
ILACE_TOL = 1e-10
SOUND_TOL = 1e-9
BORDER_BAND = 1e-9
RSTAR_BAR = 0.5
SUPPLY_GRADE = (0.1, 10.0)
WINCERT_BAR = 0.90
NG_SMOOTH = 6000
CTRL_KZ = 9
SCR_SEED = 1
INJ_A = 0.01
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
PSD_TOL = 1e-12
SOFT_BUDGET_S = 1200
PARTS = ("AR", "SM", "OSC")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


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


# --------------- pipeline, verbatim (CCIII / CLXII / CLIV / v900)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def folded_measure_full(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    fd = dict(jj=jj, th=th, inv=inv, n_uf=len(uf), mask=m,
              sign=sign, L=L)
    return xs[m], wagg[m], uf[m], fd


def folded_part(d_part, fd):
    vals = (fd["sign"] * d_part[fd["jj"]]) / (2.0 * fd["L"]) \
        * 4.0 * np.sin(fd["th"] / 2.0) ** 2
    wagg = np.zeros(fd["n_uf"])
    np.add.at(wagg, fd["inv"], vals)
    return wagg[fd["mask"]]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return ("%s(slope=%+.3f, R2=%.3f, %d excluded)"
            % (lab, sl, r2, int(np.sum(~pos)))), sl


def sym(M):
    return 0.5 * (M + M.T)


def split_parts(Mt):
    return float(Mt[0, 0]), Mt[1:, 0].copy(), Mt[1:, 1:].copy()


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


# ------------- deep extension (deep_blind_holdout verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def deep_zone_census():
    out = []
    for kz in range(2, KZ_SCAN_MAX):
        alpha, Mz, hz, _ka = ext_frame(kz)
        X = math.exp(2.0 * alpha)
        if (X > core.ATOM_MAX and X <= TAB_EXT
                and H_HOLD[0] <= hz <= H_HOLD[1]):
            out.append((kz, hz))
    return out


# ------------------- the unified rung builder (CCIII verbatim)
def build_rung(kind, kz, world=None, scramble_seed=None, comb=None,
               lag_fn=None, with_split=False):
    if kind == "surf":
        rr = window_of(kz, scramble_seed=scramble_seed)
        M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
        uu = rr["uu"]
        mm = 2.0 * rr["lam"]
        c_ar = rr["c_ar"]
    else:
        alpha, M, h, ka = ext_frame(kz)
        D = 2.0 * alpha / M
        uu = EXT["U"][:ka].copy()
        mm = EXT["MU"][:ka].copy()
        c_ar = np.asarray(core.arch_lags(M, D), float)
    if world == "smooth":
        mm = smooth_masses(uu)
    if comb is not None:
        uu, mm = comb
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0],
                      float)
    lag = c_ar + c_at
    if lag_fn is not None:
        lag = lag + lag_fn(dict(M=M, D=D))
    d = grid_density(lag)
    L = 2 * M - 2
    xs, ws, _uf_p, fdp = folded_measure_full(d, L, +1.0)
    ys, vs, uf_n, fdn = folded_measure_full(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = sym(G)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kind=kind, kz=kz, h=h, n=n, alpha=float(alpha),
               M=M, D=D, L=L, tau=float(evA[0]),
               negA=int(np.sum(evA < 0.0)))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["negR"] = int(np.sum(evR < 0.0))
    try:
        Z = np.linalg.solve(R, Xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        return out
    S = sym(B - Xc @ Z)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if not with_split:
        return out
    # ---- the exact three-way split at frozen lifts (CCIII A1)
    ug, mg = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                      float)
    d_ar = grid_density(c_ar)
    d_sm = grid_density(c_sm)
    wpos = {"AR": folded_part(d_ar, fdp),
            "SM": folded_part(d_sm, fdp)}
    wneg = {"AR": folded_part(d_ar, fdn),
            "SM": folded_part(d_sm, fdn)}
    sqv = np.sqrt(vs)
    Zl = np.zeros((n, 8))
    Zl[ic, np.arange(8)] = 1.0
    Zl[ib, :] = -Z
    Gn = Zl / sqv[:, None]
    A8 = Pn.T @ (sqv[:, None] * Zl)
    Fneg = Pn @ A8
    del Pn
    Ppos = eval_chain(al, be, m0, xs, h)
    Fpos = Ppos @ A8
    del Ppos
    Sp = {}
    for p in ("AR", "SM"):
        wn = wneg[p]
        wp = wpos[p]
        T1 = Gn.T @ (wn[:, None] * Gn)
        T2 = Gn.T @ (wn[:, None] * Fneg)
        T3 = Fpos.T @ (wp[:, None] * Fpos)
        Sp[p] = sym(T1 - T2 - T2.T + T3)
    Sp["OSC"] = sym(S - Sp["AR"] - Sp["SM"])
    out["S_parts"] = Sp
    return out


def make_steps(rungs, relax=False):
    steps = []
    for r1, r2 in zip(rungs, rungs[1:]):
        if not (isinstance(r1, dict) and isinstance(r2, dict)):
            continue
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if not relax:
            if r1["lamS"] <= 0.0 or r1["negA"] > 0:
                continue
        wS, VS = np.linalg.eigh(r1["S"])
        Q = householder_frame(VS[:, 0])
        steps.append(dict(r1=r1, r2=r2, Q=Q, tau=r1["tau"]))
    return steps


def seg_of(st):
    k1, k2 = st["r1"]["kind"], st["r2"]["kind"]
    return ("surf" if (k1, k2) == ("surf", "surf")
            else "deep" if (k1, k2) == ("deep", "deep")
            else "bridge")


# ------------------- the separator machinery (this probe)
def cheb_scalar_ladder(y, rmax):
    """[T_0(y) .. T_rmax(y)] by the three-term recurrence."""
    out = [1.0, y]
    for _ in range(rmax - 1):
        out.append(2.0 * y * out[-1] - out[-2])
    return out[:rmax + 1]


def sep_scalar(x, c, L, r, t0lad):
    m = (2.0 * x - (L + c)) / (L - c)
    tm = cheb_scalar_ladder(m, r)[r]
    return (tm / t0lad[r]) ** 2


def sep_traces(Mt, c, L, rmax):
    """tr p_r(M) for r = 1..rmax, stable matrix Chebyshev route.
    Returns (list indexed by r, t0 ladder)."""
    m0 = -(L + c) / (L - c)
    t0lad = cheb_scalar_ladder(m0, rmax)
    Y = (2.0 * Mt - (L + c) * np.eye(NDIM)) / (L - c)
    Tp = np.eye(NDIM)
    Tc = Y.copy()
    out = [float("nan")] * (rmax + 1)
    for r in range(1, rmax + 1):
        fro2 = float(np.sum(Tc * Tc))
        t0sq = t0lad[r] ** 2
        # overflow guard: a non-finite numerator or denominator
        # can never certify (declared A2 reading: +inf)
        if np.isfinite(fro2) and np.isfinite(t0sq):
            out[r] = fro2 / t0sq
        else:
            out[r] = float("inf")
        Tn = 2.0 * (Y @ Tc) - Tp
        Tp, Tc = Tc, Tn
    return out, t0lad


def sep_deriv_mat(Mt, c, L, r):
    """p_r'(M) = (2 r a / T_r(m0)^2) sym(T_r(Y) U_{r-1}(Y))."""
    a = 2.0 / (L - c)
    m0 = -(L + c) / (L - c)
    t0 = cheb_scalar_ladder(m0, r)[r]
    Y = (2.0 * Mt - (L + c) * np.eye(NDIM)) / (L - c)
    Tp = np.eye(NDIM)
    Tc = Y.copy()
    Up = np.eye(NDIM)
    Uc = 2.0 * Y
    for _ in range(r - 1):
        Tn = 2.0 * (Y @ Tc) - Tp
        Tp, Tc = Tc, Tn
        Un = 2.0 * (Y @ Uc) - Up
        Up, Uc = Uc, Un
    Ur1 = Up if r >= 1 else np.eye(NDIM)
    # after the loop: Tc = T_r(Y); Up = U_{r-1}(Y)
    return (2.0 * r * a / t0 ** 2) * sym(Tc @ Ur1)


def gersh_bound(Mt):
    return float(np.max(np.sum(np.abs(Mt), axis=1)))


def fro_bound(Mt):
    return float(np.sqrt(np.sum(Mt * Mt)))


# ------------------- exact-rational tier (v897 class; pure
# integer arithmetic on the dyadic float entries)
def dyadic(x):
    """(num, e) with x = num / 2^e exact (float64 is dyadic)."""
    fr = Fraction(float(x))
    return fr.numerator, fr.denominator.bit_length() - 1


def sep_poly_int(r, cf, Lf):
    """Integer separator data: with c = cn/2^s, L = Ln/2^s
    (common dyadic scale) and P = Ln - cn, Q = Ln + cn, the
    scaled Chebyshev R_j(x) = P^j T_j(m(x)) obeys the INTEGER
    recurrence R_{j+1} = 2 (2^{s+1} x - Q) R_j - P^2 R_{j-1}.
    Returns (w, R0): w = integer coefficients of R_r(x)^2
    (ascending), R0 = R_r(0) = P^r T_r(m(0)); the decision
    tr p_r(M) < 1  <=>  sum_k w_k tr(M^k) < R0^2 (exact)."""
    nL, eL = dyadic(Lf)
    nc, ec = dyadic(cf)
    s = max(eL, ec)
    Ln = nL << (s - eL)
    cn = nc << (s - ec)
    P, Q, A = Ln - cn, Ln + cn, 1 << (s + 1)
    P2 = P * P
    Rp = [1]
    Rc = [-Q, A]
    for _ in range(r - 1):
        Rn = [0] * (len(Rc) + 1)
        for i, ci in enumerate(Rc):
            Rn[i] -= 2 * Q * ci
            Rn[i + 1] += 2 * A * ci
        for i, ci in enumerate(Rp):
            Rn[i] -= P2 * ci
        Rp, Rc = Rc, Rn
    w = [0] * (2 * len(Rc) - 1)
    for i, ci in enumerate(Rc):
        if ci == 0:
            continue
        for j, cj in enumerate(Rc):
            if cj != 0:
                w[i + j] += ci * cj
    return w, Rc[0]


def moments_int(Mt, K):
    """(T, E): T[k] = tr(N^k) integer with N = 2^E M (common
    dyadic scale), so tr(M^k) = T[k] / 2^{kE} exactly."""
    frs = [[Fraction(float(Mt[i, j])) for j in range(NDIM)]
           for i in range(NDIM)]
    E = max(f.denominator.bit_length() - 1
            for row in frs for f in row)
    N = [[f.numerator << (E - (f.denominator.bit_length() - 1))
          for f in row] for row in frs]
    T = [NDIM]
    P = N
    for k in range(1, K + 1):
        T.append(sum(P[i][i] for i in range(NDIM)))
        if k < K:
            P = [[sum(P[i][t] * N[t][j] for t in range(NDIM))
                  for j in range(NDIM)] for i in range(NDIM)]
    return T, E


def exact_decision_int(w, R0, T, E):
    """Exact decision tr p_r(M) < 1 and the exact trace as a
    Fraction (for printing)."""
    K = len(w) - 1
    lhs = 0
    for k, wk in enumerate(w):
        if wk != 0:
            lhs += wk * T[k] * (1 << ((K - k) * E))
    rhs = R0 * R0 * (1 << (K * E))
    return lhs < rhs, Fraction(lhs, rhs)


def fmt_ladder(v):
    if not len(v):
        return "n/a"
    v = np.asarray(v, float)
    return "%+.3f/%+.3f/%+.3f" % (float(np.min(v)),
                                  float(np.median(v)),
                                  float(np.max(v)))


def main():
    section("PRIME.PORT.ONEBADMODE.MOMENTS.01 -- the one-bad-"
            "eigenvalue moment certificate of the wall matrices "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level probe; "
          "certificate decisions anchored exact-rationally on the "
          "float entries (v897 class).  c_B = 0.5523 CITED (CLIII "
          "certified surface; CLIV deep float), printed, not "
          "re-proved.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- surface ladder + P2/P3 ledger reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = build_rung("surf", kz, with_split=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth_h = sorted(truth, key=lambda r: (r["h"], r["kz"]))
    full = [r for r in truth_h if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3 WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps_s = make_steps(truth_h)
    check("W4 >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps_s) >= MIN_STEPS, "%d steps" % len(steps_s),
          kill="K1")
    print("    surface h range %d..%d  [%.1f s]"
          % (truth_h[0]["h"], truth_h[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    def assemble(st):
        """M in tau units + blocks + bounds + truth eigs."""
        tau = st["tau"]
        if tau <= 0.0:
            st["status"] = "REFUSED-TAU"
            return st
        Mt = sym(st["Q"].T @ (st["r2"]["S"] / tau) @ st["Q"])
        st["Mt"] = Mt
        nn, b, B = split_parts(Mt)
        st["n0"], st["bvec"], st["Bblk"] = nn, b, B
        evB = np.linalg.eigvalsh(B)
        st["lamB1"] = float(evB[0])
        try:
            x = np.linalg.solve(B, b)
            st["gap"] = nn - float(b @ x)
        except np.linalg.LinAlgError:
            st["gap"] = float("nan")
        ev = np.linalg.eigvalsh(Mt)
        st["eigs"] = ev
        lg, lf = gersh_bound(Mt), fro_bound(Mt)
        st["L_gersh"], st["L_fro"] = lg, lf
        st["L_src"] = min(lg, lf) * L_INFLATE
        st["L_win"] = "G" if lg <= lf else "F"
        if st["L_src"] <= CB_F * (1.0 + 1e-6):
            st["status"] = "REFUSED-L"
            return st
        st["status"] = "OK"
        if "S_parts" in st["r2"]:
            st["M_osc"] = sym(st["Q"].T
                              @ (st["r2"]["S_parts"]["OSC"] / tau)
                              @ st["Q"])
            st["M_win"] = Mt - st["M_osc"]
        return st

    for st in steps_s:
        assemble(st)
    ok_s = [st for st in steps_s if st["status"] == "OK"]
    minB_all = float(np.min([st["lamB1"] for st in ok_s]))
    gaps = np.array([st["gap"] for st in ok_s])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    check("W5 REPRODUCTION P2/P3 ledger: min lam_min(B_tau) %.4f "
          "== %.3f; gap min/med %.4f/%.4f == %.3f/%.3f"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF),
          (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
           and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
           and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL),
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ DW
    section("DW -- the deep ladder (CLIV 4e6 extension, "
            "FLOAT-LEVEL declared)")
    lam_ext = build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
               and np.array_equal(EXT["U"][:nP], core.U_ALL)
               and np.array_equal(EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep]) / nnf[keep]))
    check("DW1 fidelity: table overlap dev %.1e == 0; prefixes "
          "bitwise %s; kappa %.6f <= %.6f + 1e-6"
          % (dev, ok_pref, kappa, core.KAPPA_REF),
          dev == 0.0 and ok_pref
          and kappa <= core.KAPPA_REF + 1e-6, kill="K2")
    dz = deep_zone_census()
    check("DW2 deep census %d rungs (expected %d; h %d..%d)"
          % (len(dz), N_DEEP_EXP,
             min(h for _k, h in dz) if dz else -1,
             max(h for _k, h in dz) if dz else -1),
          len(dz) == N_DEEP_EXP, kill="K1")
    if KILLS:
        return finish({})
    deep = []
    n_skip = 0
    for kz, hz in sorted(dz, key=lambda p: (p[1], p[0])):
        if time.time() - T0 > SOFT_BUDGET_S:
            n_skip += 1
            continue
        r = build_rung("deep", kz, with_split=True)
        if r is None:
            print("    deep kz %-4d h %-5d: CHAIN SHORT"
                  % (kz, hz), flush=True)
            continue
        deep.append(r)
        print("    deep kz %-4d h %-5d n %-5d tau %.3e negA %d "
              "lamS %+.3e  [%.0f s]"
              % (kz, r["h"], r["n"], r["tau"], r["negA"],
                 r.get("lamS", float("nan")), time.time() - T0),
              flush=True)
    if n_skip:
        print("    SKIPPED-BUDGET: %d deep rungs not built "
              "(honest partial coverage)" % n_skip)
    deep_ok = [r for r in deep if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    check("DW3 deep truth rungs complete + all-PSD: %d of %d "
          "built (>= %d)" % (len(deep_ok), len(deep), MIN_DEEP_OK),
          len(deep_ok) >= MIN_DEEP_OK, kill="K1")
    if KILLS:
        return finish({})
    deep_h = sorted(deep_ok, key=lambda r: (r["h"], r["kz"]))
    steps_d = make_steps(deep_h)
    for st in steps_d:
        assemble(st)
    ok_d = [st for st in steps_d if st["status"] == "OK"]
    minB_deep = float(np.min([st["lamB1"] for st in ok_d]))
    check("DW4 REPRODUCTION CLIV: min own-frame lam_min(B_tau) "
          "over %d deep steps %.4f == %.4f (rtol %g)"
          % (len(ok_d), minB_deep, DEEP_MINB_REF, DEEP_MINB_RTOL),
          abs(minB_deep / DEEP_MINB_REF - 1.0) <= DEEP_MINB_RTOL,
          kill="K2")

    # ------------------------------------------------------------ P
    section("P -- the combined h-sorted chain (surface + bridge + "
            "deep)")
    comb_rungs = sorted([r for r in truth_h if r["core_ok"]]
                        + deep_h, key=lambda r: (r["h"], r["kz"]))
    steps_c = make_steps(comb_rungs)
    for st in steps_c:
        assemble(st)
    ok_c = [st for st in steps_c if st["status"] == "OK"]
    n_ref = len(steps_c) - len(ok_c)
    segs = [seg_of(st) for st in ok_c]
    check("P1 combined chain: %d steps, %d OK (>= %d; refused %d)"
          % (len(steps_c), len(ok_c), MIN_STEPS_COMB, n_ref),
          len(ok_c) >= MIN_STEPS_COMB, kill="K1")
    if KILLS:
        return finish({})
    print("    segments: surface %d, bridge %d, deep %d"
          % (segs.count("surf"), segs.count("bridge"),
             segs.count("deep")))
    rep_idx = (0, len(ok_c) // 2, len(ok_c) - 1)
    print("    representative steps (frozen rule idx 0, n//2, "
          "n-1): %s" % ", ".join(
              "h %d (kz %d, %s)" % (ok_c[i]["r2"]["h"],
                                    ok_c[i]["r2"]["kz"],
                                    seg_of(ok_c[i]))
              for i in rep_idx))

    # trace tables (both tiers) for every OK step
    for st in ok_c:
        st["trp_src"], st["t0_src"] = sep_traces(
            st["Mt"], CB_F, st["L_src"], R_MAX)
        lam_max = float(st["eigs"][-1])
        c_or = st["lamB1"]
        L_or = lam_max * (1.0 + 1e-12)
        st["c_or"], st["L_or"] = c_or, L_or
        if 0.0 < c_or < L_or:
            st["trp_orc"], _ = sep_traces(st["Mt"], c_or, L_or,
                                          R_MAX)
        else:
            st["trp_orc"] = None

        def rstar_of(tab):
            if tab is None:
                return None
            for r in range(1, R_MAX + 1):
                if np.isfinite(tab[r]) and tab[r] < 1.0:
                    return r
            return None
        st["rstar"] = rstar_of(st["trp_src"])
        st["rstar_orc"] = rstar_of(st["trp_orc"])

    # ------------------------------------------------------------ M
    section("M -- machine wards (separator facts, route ties, "
            "exact-rational anchor, interlacing)")
    # M1 grids at the representative (c, L) pairs
    worst_neg, worst_bulk, worst_p0 = 0.0, 0.0, 0.0
    for i in rep_idx:
        L = ok_c[i]["L_src"]
        m0 = -(L + CB_F) / (L - CB_F)
        t0lad = cheb_scalar_ladder(m0, R_MAX)
        xs_neg = np.linspace(-2.0 * CB_F, 0.0, 101)
        xs_blk = np.linspace(CB_F, L, 401)
        for r in R_SUBSET:
            eps_r = 1.0 / t0lad[r] ** 2
            pn = np.array([sep_scalar(x, CB_F, L, r, t0lad)
                           for x in xs_neg])
            pb = np.array([sep_scalar(x, CB_F, L, r, t0lad)
                           for x in xs_blk])
            worst_neg = max(worst_neg, float(np.max(1.0 - pn)))
            worst_bulk = max(worst_bulk,
                             float(np.max(pb - eps_r
                                          * (1.0 + GRID_BULK_TOL))),
                             float(np.max(-pb)))
            worst_p0 = max(worst_p0,
                           abs(sep_scalar(0.0, CB_F, L, r, t0lad)
                               - 1.0))
    check("M1 WARD separator facts on grids (3 rep pairs, "
          "R_SUBSET to %d): neg-side 1-p max %.2e <= %.0e; bulk "
          "excess max %.2e <= 0; |p(0)-1| max %.2e <= %.0e"
          % (R_MAX, worst_neg, GRID_NEG_TOL, worst_bulk,
             worst_p0, P0_TOL),
          worst_neg <= GRID_NEG_TOL and worst_bulk <= 0.0
          and worst_p0 <= P0_TOL, kill="K2")

    # M2 route tie: stable vs eig on every OK step, every r
    tie_max = 0.0
    for st in ok_c:
        t0lad = st["t0_src"]
        for r in R_SUBSET:
            te = sum(sep_scalar(float(x), CB_F, st["L_src"], r,
                                t0lad) for x in st["eigs"])
            dev = (abs(st["trp_src"][r] - te)
                   / max(abs(te), 1.0))
            tie_max = max(tie_max, dev)
    check("M2 WARD trace-route tie (stable == eig-sum) max rel "
          "%.2e <= %.0e on %d steps x %d orders (R_SUBSET)"
          % (tie_max, TIE_WARD, len(ok_c), len(R_SUBSET)),
          tie_max <= TIE_WARD, kill="K2")

    # M3 float moment-linearity + M4 exact tier at rep steps
    mono_max_low, mono_max_all = 0.0, 0.0
    n_agree, n_border, n_dis = 0, 0, 0
    for i in rep_idx:
        st = ok_c[i]
        momT, momE = moments_int(st["Mt"], 2 * REP_RCAP)
        momf = [float(NDIM)]
        Pk = np.eye(NDIM)
        for _k in range(2 * REP_RCAP):
            Pk = Pk @ st["Mt"]
            momf.append(float(np.trace(Pk)))
        for r in range(1, REP_RCAP + 1):
            w, R0 = sep_poly_int(r, CB_F, st["L_src"])
            # float monomial route (normalized coefficients)
            R02 = R0 * R0
            qf = [float(Fraction(wk, R02)) for wk in w]
            trf = (NDIM * qf[0] + sum(
                qf[k] * momf[k] for k in range(1, len(qf))))
            dev = (abs(trf - st["trp_src"][r])
                   / max(abs(st["trp_src"][r]), 1.0))
            mono_max_all = max(mono_max_all, dev)
            if r <= MONO_RCAP:
                amp = (4.0 * (2.0 * st["L_src"]
                              / (st["L_src"] - CB_F))) ** (2 * r)
                bar = MONO_WARD * max(1.0, amp * 1e-16 / 1e-9)
                if dev > bar:
                    mono_max_low = max(mono_max_low, dev / bar)
            # exact decision
            lt1, ratF = exact_decision_int(w, R0, momT, momE)
            flt1 = st["trp_src"][r] < 1.0
            if lt1 == flt1:
                n_agree += 1
            elif abs(st["trp_src"][r] - 1.0) <= BORDER_BAND:
                n_border += 1
            else:
                n_dis += 1
        print("    rep h %-5d: exact tier r <= %d done; float-"
              "monomial max rel dev %.1e (declared cancellation)"
              ", L_src %.4g" % (st["r2"]["h"], REP_RCAP,
                                mono_max_all, st["L_src"]))
    check("M3 WARD float moment-linearity r <= %d within the "
          "declared amplification-scaled bar (worst bar-ratio "
          "%.2f <= 1; raw max dev all r %.1e printed)"
          % (MONO_RCAP, mono_max_low, mono_max_all),
          mono_max_low <= 1.0, kill="K2")
    check("M4a WARD exact-rational tier decisions agree with the "
          "stable float route: %d agree, %d borderline (|tr-1| <= "
          "%.0e), %d disagree == 0"
          % (n_agree, n_border, BORDER_BAND, n_dis),
          n_dis == 0, kill="K2")

    # M4b exact confirmation of r* (capped at EXACT_CAP, A2)
    n_conf, n_conf_fail, n_fonly = 0, 0, 0
    fonly_mrg = []
    for st in ok_c:
        if st["rstar"] is None:
            continue
        r = st["rstar"]
        if r > EXACT_CAP:
            n_fonly += 1
            fonly_mrg.append(1.0 - st["trp_src"][r])
            continue
        momT, momE = moments_int(st["Mt"], 2 * r)
        w, R0 = sep_poly_int(r, CB_F, st["L_src"])
        lt1, ratF = exact_decision_int(w, R0, momT, momE)
        st["exact_tr"] = float(ratF)
        if lt1:
            n_conf += 1
        else:
            n_conf_fail += 1
    check("M4b WARD exact-rational confirmation of the float r* "
          "decision (r* <= %d): %d/%d confirmed, %d failed == 0; "
          "FLOAT-ONLY beyond cap: %d steps (min float margin %s, "
          "declared A2)"
          % (EXACT_CAP, n_conf, n_conf + n_conf_fail, n_conf_fail,
             n_fonly, "%.3e" % min(fonly_mrg) if fonly_mrg
             else "n/a"),
          n_conf_fail == 0, kill="K2")

    # M5 interlacing + L soundness (per-step normalized)
    il_worst = float("inf")
    l_ok = 0
    for st in ok_c:
        il_worst = min(il_worst,
                       (float(st["eigs"][1]) - st["lamB1"])
                       / max(1.0, abs(st["lamB1"])))
        if st["L_src"] >= float(st["eigs"][-1]):
            l_ok += 1
    check("M5 WARD interlacing lam_2(M) >= lam_1(B) (worst "
          "normalized lam_2 - lam_1(B) = %+.2e >= -%.0e) + "
          "L-soundness L_src >= lam_max on %d/%d"
          % (il_worst, ILACE_TOL, l_ok, len(ok_c)),
          il_worst >= -ILACE_TOL and l_ok == len(ok_c),
          kill="K2")

    # ------------------------------------------------------------ T1
    section("T1 -- setup census: premise, one-bad-mode, L bounds")
    print("    seg    h1->h2      tau        lam_min    lam_2     "
          " lam_1(B)  L_src     lam_max   loose(dex) win")
    for st in ok_c:
        st["loose"] = math.log10(st["L_src"]
                                 / float(st["eigs"][-1]))
        print("    %-6s %4d->%-4d %.3e %+.3e %+.3e %+.3e %.3e "
              "%.3e  %+.3f   %s"
              % (seg_of(st), st["r1"]["h"], st["r2"]["h"],
                 st["tau"], st["eigs"][0], st["eigs"][1],
                 st["lamB1"], st["L_src"], st["eigs"][-1],
                 st["loose"], st["L_win"]), flush=True)
    prem = {}
    for sg in ("surf", "bridge", "deep"):
        sub = [st for st in ok_c if seg_of(st) == sg]
        nB = sum(1 for st in sub if st["lamB1"] >= CB_F)
        n2 = sum(1 for st in sub
                 if float(st["eigs"][1]) >= CB_F)
        prem[sg] = (nB, n2, len(sub))
    onebad = [int(np.sum(st["eigs"] < CB_F)) for st in ok_c]
    n_onebad_ok = sum(1 for k in onebad if k <= 1)
    loose = np.array([st["loose"] for st in ok_c])
    winG = sum(1 for st in ok_c if st["L_win"] == "G")
    t1 = ("PREMISE(lam1B >= cB: surf %d/%d [CLIII certified "
          "range], bridge %d/%d [float], deep %d/%d [float]; "
          "lam2M >= cB: %d/%d/%d)"
          % (prem["surf"][0], prem["surf"][2],
             prem["bridge"][0], prem["bridge"][2],
             prem["deep"][0], prem["deep"][2],
             prem["surf"][1], prem["bridge"][1],
             prem["deep"][1]))
    t1b = ("ONEBAD(%d/%d steps with #eig < cB <= 1, max %d)"
           % (n_onebad_ok, len(ok_c), max(onebad)))
    t1c = ("LBOUND(loose dex %s; Gershgorin wins %d/%d)"
           % (fmt_ladder(loose), winG, len(ok_c)))
    print("    " + t1)
    print("    " + t1b)
    print("    " + t1c)
    check("T1 typed: %s + %s + %s" % (t1, t1b, t1c), True)

    # ------------------------------------------------------------ T2
    section("T2 -- the order ladder: r* census, margins, h-trend, "
            "the r*-law")
    print("    seg    h2     r*src r*orc  tr_p(r*)   margin(dex) "
          " trp@16     trp@64     trp@256    exact_tr(r*)")
    for st in ok_c:
        r = st["rstar"]
        mg = (1.0 - st["trp_src"][r]) if r is not None else None
        st["margin"] = mg
        for rf in R_FIX:
            st["m%d" % rf] = 1.0 - st["trp_src"][rf]
        print("    %-6s %-5d  %-5s %-5s %10s %11s %10.3e %10.3e "
              "%10.3e %s"
              % (seg_of(st), st["r2"]["h"],
                 r if r is not None else ">%d" % R_MAX,
                 st["rstar_orc"] if st["rstar_orc"] is not None
                 else "-",
                 "%.4f" % st["trp_src"][r] if r is not None
                 else "n/a",
                 "%+.3f" % math.log10(mg) if mg and mg > 0
                 else "n/a",
                 st["trp_src"][R_FIX[0]],
                 st["trp_src"][R_FIX[1]],
                 st["trp_src"][R_FIX[2]],
                 "%.6f" % st["exact_tr"]
                 if "exact_tr" in st else "-"), flush=True)
    cert = [st for st in ok_c if st["rstar"] is not None]
    uncert = [st for st in ok_c if st["rstar"] is None]
    cen = {}
    for sg in ("surf", "bridge", "deep"):
        sub = [st for st in ok_c if seg_of(st) == sg]
        cen[sg] = (sum(1 for st in sub
                       if st["rstar"] is not None), len(sub))
    rstars = np.array([st["rstar"] for st in cert], float)
    t2 = ("CENSUS(surf %d/%d, bridge %d/%d, deep %d/%d; r* "
          "min/med/max %d/%d/%d)"
          % (cen["surf"] + cen["bridge"] + cen["deep"]
             + (int(rstars.min()), int(np.median(rstars)),
                int(rstars.max()))))
    print("    " + t2)
    if uncert:
        print("    UNCERTIFIED steps (r* > %d): %s" % (R_MAX,
              ", ".join("h %d (%s)" % (st["r2"]["h"], seg_of(st))
                        for st in uncert)))
    mrg = [math.log10(st["margin"]) for st in cert
           if st["margin"] > 0]
    t2b = "MARGIN(at r*: dex %s)" % fmt_ladder(mrg)
    print("    " + t2b)
    # h-trend
    sl, se, r2t = jack_slope(
        [math.log(st["r2"]["h"]) for st in cert], rstars)
    if sl - 2 * se > RSTAR_BAR:
        rlab = "RSTAR-GROWING"
    elif sl + 2 * se < RSTAR_BAR:
        rlab = "RSTAR-FLAT"
    else:
        rlab = "RSTAR-AMBIG"
    t2c = ("RSTAR(%s: slope %+.3f +/- 2SE %.3f per ln h, R2 "
           "%.3f, bar %.2f)" % (rlab, sl, 2 * se, r2t, RSTAR_BAR))
    print("    " + t2c)
    # the r*-law (A1): r* vs sqrt(lam_max / c_B)
    sq = np.array([math.sqrt(float(st["eigs"][-1]) / CB_F)
                   for st in cert])
    kappa = float(np.sum(sq * rstars) / np.sum(sq * sq))
    _a0, sl_sq, r2_sq = ols_line(sq, rstars)
    sl_ln, se_ln, r2_ln = jack_slope(
        [math.log(math.sqrt(float(st["eigs"][-1]) / CB_F))
         for st in cert], np.log(rstars))
    sl_h, se_h, r2_h = jack_slope(
        [math.log(st["r2"]["h"]) for st in cert], np.log(rstars))
    t2e = ("RSTAR-LAW(kappa = %.3f on r* = kappa sqrt(lam_max/"
           "c_B), OLS slope %.3f R2 %.3f; ln r* vs ln sqrt(L/c) "
           "slope %+.3f +/- 2SE %.3f R2 %.3f; ln r* vs ln h "
           "slope %+.3f +/- 2SE %.3f R2 %.3f)"
           % (kappa, sl_sq, r2_sq, sl_ln, 2 * se_ln, r2_ln,
              sl_h, 2 * se_h, r2_h))
    print("    " + t2e)
    # oracle price
    lp = [st["rstar"] - st["rstar_orc"] for st in cert
          if st["rstar_orc"] is not None]
    t2d = ("ORACLE-PRICE(r*src - r*orc med %+.1f, max %+d; "
           "r*orc med %d)"
           % (float(np.median(lp)), int(np.max(lp)),
              int(np.median([st["rstar_orc"] for st in cert
                             if st["rstar_orc"] is not None]))))
    print("    " + t2d)
    check("T2 typed: %s + %s + %s + %s + %s"
          % (t2, t2b, t2c, t2e, t2d), True)

    # ------------------------------------------------------------ T3
    section("T3 -- the disguise test: tau-screens, supply "
            "sensitivity, source seat")
    taus = [st["tau"] for st in cert]
    scr_fix = {}
    for rf in R_FIX:
        scr_fix[rf], _ = screen([st["m%d" % rf] for st in cert],
                                taus)
    scrR, slR = screen([st["margin"] for st in cert], taus)
    print("    D-a margin screens vs tau:")
    for rf in R_FIX:
        print("      margin @ r=%-3d: %s" % (rf, scr_fix[rf]))
    print("      margin @ r*   : %s" % scrR)
    # D-b supply sensitivity
    ratios = []
    for st in cert:
        Pp = sep_deriv_mat(st["Mt"], CB_F, st["L_src"],
                           st["rstar"])
        gn = float(Pp[0, 0])
        st["gn"] = gn
        st["dnstar"] = (st["margin"] / abs(gn)
                        if gn != 0 else float("inf"))
        if np.isfinite(st["dnstar"]) and st["gap"] > 0:
            st["dn_ratio"] = st["dnstar"] / st["gap"]
            ratios.append(st["dn_ratio"])
        st["osc_dd"] = (float(np.sum(Pp * st["M_osc"]))
                        if "M_osc" in st else float("nan"))
    ratios = np.array(ratios)
    med_ratio = float(np.median(ratios))
    in_grade = SUPPLY_GRADE[0] <= med_ratio <= SUPPLY_GRADE[1]
    scrDn, _ = screen([st["dnstar"] for st in cert
                       if np.isfinite(st["dnstar"])],
                      [st["tau"] for st in cert
                       if np.isfinite(st["dnstar"])])
    d_b = ("SUPPLY(dn*/s dex %s, med %.3f -> %s; dn* screen %s)"
           % (fmt_ladder(np.log10(ratios)), med_ratio,
              "HALFGAP-GRADE" if in_grade else "OUT-OF-GRADE",
              scrDn))
    print("    D-b " + d_b)
    # D-c source seat (A3: log10 of the shares printed)
    print("    D-c moment mix at the representative steps "
          "(log10 share of tr(M^k)):")
    print("      h      k:  " + "  ".join("%7d" % k
                                          for k in range(1, 13)))
    for i in rep_idx:
        st = ok_c[i]
        mixo, mixp = [], []
        Pk = np.eye(NDIM)
        Wk = np.eye(NDIM)
        Bk = np.eye(NDIM - 1)
        for k in range(1, 13):
            Pk = Pk @ st["Mt"]
            Wk = Wk @ st["M_win"]
            Bk = Bk @ st["Bblk"]
            trM = float(np.trace(Pk))
            mixo.append(abs(trM - float(np.trace(Wk)))
                        / max(abs(trM), 1e-300))
            mixp.append(abs(trM - float(np.trace(Bk)))
                        / max(abs(trM), 1e-300))
        print("      %-5d OSC:  " % st["r2"]["h"]
              + "  ".join("%+7.2f" % (math.log10(max(v, 1e-300)))
                          for v in mixo))
        print("            n,b:  "
              + "  ".join("%+7.2f" % (math.log10(max(v, 1e-300)))
                          for v in mixp))
    n_win = 0
    tstars = []
    for st in cert:
        if "M_win" not in st:
            continue
        with np.errstate(over="ignore", invalid="ignore"):
            trw, _ = sep_traces(st["M_win"], CB_F, st["L_src"],
                                st["rstar"])
        if np.isfinite(trw[st["rstar"]]) \
                and trw[st["rstar"]] < 1.0:
            n_win += 1
        if np.isfinite(st["osc_dd"]) and st["osc_dd"] != 0:
            tstars.append(st["margin"] / abs(st["osc_dd"]))
    win_frac = n_win / max(len(cert), 1)
    d_c = ("SOURCE-SEAT(WIN-only certifies %d/%d = %.2f; OSC "
           "budget t* dex %s)"
           % (n_win, len(cert), win_frac,
              fmt_ladder(np.log10(np.array(tstars)))))
    print("    " + d_c)
    # combined typing (frozen rule)
    lab_a = scrR.split("(")[0]
    if lab_a == "RELOC" and in_grade:
        dtype = "DISGUISE-HALFGAP"
    elif lab_a == "PASS" and ((not in_grade)
                              or win_frac >= WINCERT_BAR):
        dtype = "ROUTE-DISTINCT"
    else:
        dtype = "DISGUISE-MIXED"
    d_all = ("%s(D-a %s / D-b %s med %.3f / D-c WIN %.2f)"
             % (dtype, lab_a,
                "IN-GRADE" if in_grade else "OUT", med_ratio,
                win_frac))
    print("    " + d_all)
    check("T3 typed: %s + %s + %s" % (d_b, d_c, d_all), True)

    # ------------------------------------------------------------ E
    section("E -- controls (rung firing + the certificate on "
            "false worlds)")
    worlds = {}
    sm = [build_rung("surf", kz, world="smooth") for kz in zones]
    n_f = sum(1 for r in sm if isinstance(r, dict)
              and r["negA"] > 0)
    check("E1 WARD smooth world fires (neg(A) > 0 on %d rungs)"
          % n_f, n_f > 0, kill="K2")
    worlds["smooth"] = sm
    scr_w = [build_rung("surf", kz, scramble_seed=SCR_SEED)
             for kz in zones]
    n_f = sum(1 for r in scr_w if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E2 WARD scramble fires (%d rungs)" % n_f, n_f > 0,
          kill="K2")
    worlds["scramble"] = scr_w
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    rE = build_rung("surf", CTRL_KZ,
                    comb=(np.log(nn.astype(float)),
                          2.0 * lamE_[nn]
                          / np.sqrt(nn.astype(float))))
    eps_fire = (rE is None) or rE["negA"] > 0
    check("E3 WARD Epstein comb fires at kz %d (neg(A) %s); "
          "step-level Epstein DECLARED SKIPPED (O(X^2), "
          "predecessor pattern)"
          % (CTRL_KZ, rE["negA"] if isinstance(rE, dict)
             else "chain death"), eps_fire, kill="K2")

    def inj(rr):
        tt = np.arange(rr["M"]) * rr["D"]
        return (INJ_A * np.cos(INJ_GAMMA0 * tt)
                * (np.cosh(INJ_DELTA * tt) - 1.0))
    cosh_w = [build_rung("surf", kz, lag_fn=inj) for kz in zones]
    n_f = sum(1 for r in cosh_w if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E4 WARD cosh injection A = %g fires (%d rungs; CLXII "
          "deployed amplitude, frozen selection cited)"
          % (INJ_A, n_f), n_f > 0, kill="K2")
    worlds["cosh"] = cosh_w

    sound_min = float("inf")
    n_overflow = 0
    n_leak = 0
    e5_rows = []
    for name, lad in worlds.items():
        rungs_w = sorted([r for r in lad if isinstance(r, dict)],
                         key=lambda r: (r["h"], r["kz"]))
        steps_w = make_steps(rungs_w, relax=True)
        n_tau, n_bpd, n_prem = 0, 0, 0
        n_indef, n_raw, n_comp = 0, 0, 0
        pd_exc = []
        min_tr_indef = float("inf")
        for st in steps_w:
            assemble(st)
            if st["status"] == "REFUSED-TAU":
                n_tau += 1
                continue
            if st["status"] != "OK":
                continue
            if st["lamB1"] <= 0.0:
                n_bpd += 1
            if st["lamB1"] < CB_F:
                n_prem += 1
            with np.errstate(over="ignore", invalid="ignore"):
                trp, _ = sep_traces(st["Mt"], CB_F, st["L_src"],
                                    R_MAX)
            fin = [trp[r] for r in range(1, R_MAX + 1)
                   if np.isfinite(trp[r])]
            n_overflow += (R_MAX - len(fin))
            raw = bool(fin) and min(fin) < 1.0
            lam_min = float(st["eigs"][0])
            lam_max = float(st["eigs"][-1])
            indef = lam_min <= -1e-10 * max(1.0, lam_max)
            if indef:
                n_indef += 1
                if fin:
                    sound_min = min(sound_min, min(fin))
                    min_tr_indef = min(min_tr_indef, min(fin))
                if raw:
                    n_leak += 1
            if raw:
                n_raw += 1
                if not indef:
                    pd_exc.append((st["r2"]["kz"], lam_min))
                if st["tau"] > 0 and st["lamB1"] >= CB_F:
                    n_comp += 1
        e5_rows.append((name, len(steps_w), n_tau, n_bpd, n_prem,
                        n_indef, n_raw, n_comp, pd_exc,
                        min_tr_indef))
    print("\n    E5 the certificate on false worlds (relaxed "
          "steps; RAW = finite tr p_r < 1 for some r; COMPOSED = "
          "RAW and tau > 0 and lam1B >= cB):")
    for (name, ns, ntau, nbpd, nprem, nind, nraw, ncomp, exc,
         mtr) in e5_rows:
        print("    %-9s: steps %2d  tau<=0 %2d  B-not-PD %2d  "
              "lam1B<cB %2d  eig-indef %2d  RAW %2d  COMPOSED %2d"
              "  min tr_p(indef) %s"
              % (name, ns, ntau, nbpd, nprem, nind, nraw, ncomp,
                 "%.3e" % mtr if np.isfinite(mtr) else "inf"),
              flush=True)
        for kz, lm in exc:
            print("      PD-exception kz %d: eig lam_min %+.3e "
                  "> 0 (genuinely PD control core, cert SOUND)"
                  % (kz, lm))
    check("M6/E5 WARD soundness on eig-indefinite control steps: "
          "RAW certs there %d == 0; min finite tr p_r %.3e >= "
          "1 - %.0e (%d overflow entries -> +inf, declared A2)"
          % (n_leak,
             sound_min if np.isfinite(sound_min) else float("inf"),
             SOUND_TOL, n_overflow),
          n_leak == 0 and (not np.isfinite(sound_min)
                           or sound_min >= 1.0 - SOUND_TOL),
          kill="K2")
    e5 = " ".join("%s[RAW %d, COMP %d, PDexc %d]"
                  % (name, nraw, ncomp, len(exc))
                  for (name, _ns, _t, _b, _p, _i, nraw, ncomp,
                       exc, _m) in e5_rows)
    check("E5 typed: CONTROLS-SEPARATE(%s)" % e5, True)
    check("E6 typed: IMPOSTOR-NA(zero zero-reads in this probe; "
          "AST firewall is the witness)", True)

    # ------------------------------------------------------------ F
    section("F -- screens + verdict assembly")
    scrT, _ = screen(tstars, [st["tau"] for st in cert
                              if np.isfinite(st["osc_dd"])
                              and st["osc_dd"] != 0])
    print("    " + " | ".join("margin@%d %s" % (rf, scr_fix[rf])
                              for rf in R_FIX))
    print("    margin@r* %s" % scrR)
    print("    dn* %s | t*(OSC) %s" % (scrDn, scrT))
    scr_lab = ("SCREENS(%s | mr* %s | dn* %s | t* %s)"
               % (" | ".join("m%d %s"
                             % (rf, scr_fix[rf].split("(")[0])
                             for rf in R_FIX),
                  scrR.split("(")[0], scrDn.split("(")[0],
                  scrT.split("(")[0]))
    check("F1 typed: %s" % scr_lab, True)

    if not uncert:
        head = ("MOMENTS-CERTIFY(surf %d/%d + bridge %d/%d + "
                "deep %d/%d, max r* %d, exact-anchored %d/%d)"
                % (cen["surf"] + cen["bridge"] + cen["deep"]
                   + (int(rstars.max()), n_conf, len(cert))))
    else:
        head = ("MOMENTS-BLOCKED(UNCERT %d of %d at R_MAX %d; "
                "%s)" % (len(uncert), len(ok_c), R_MAX, t2c))
    return finish(dict(
        head=head, t1=t1, t1b=t1b, t1c=t1c, t2=t2, t2b=t2b,
        t2c=t2c, t2e=t2e, t2d=t2d, db=d_b, dc=d_c, dall=d_all,
        e5="CONTROLS-SEPARATE(%s)" % e5, scr=scr_lab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = " / ".join(labels.get(k, "-") for k in
                             ("head", "t1", "t1b", "t1c", "t2",
                              "t2b", "t2c", "t2e", "t2d", "db",
                              "dc", "dall", "e5", "scr"))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every census is a statement about the
  float64-computed step matrices of a deployed finite ladder;
  certificate decisions are anchored exact-rationally on those
  float entries and float-committed constants (v897 class); the
  B-floor constant is CITED from CLIII with its certified range
  said plainly (39 surface steps, own frame, tau units); the deep
  ladder is FLOAT-LEVEL (CLIV limit, inherited); positivity of M
  on finitely many rungs is equivalent to the measured wall there
  and proves nothing at other h; fits are empirical laws.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
