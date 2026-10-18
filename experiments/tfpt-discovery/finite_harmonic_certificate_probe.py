#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""finite_harmonic_certificate_probe -- PRIME.PORT.FINITE.HARMONIC.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall -- the FINITE HARMONIC CERTIFICATE.  Predecessor
CLV (PRIME.PORT.TAIL.OSCPAIR.01) reduced the deep-tail pairing to
~12 windowed psi-fluctuation Fourier coefficients: 12 frozen global
bins (centers omega <= 5.25 plus two trace bins near 13.25/14.25)
carry share_red min/med/max +0.846/+1.006/+1.049 of the pairing on
all 67 rungs; the carriers are window-harmonic-locked (omega* =
j* pi/Lu, j* in {1,2,3}) and CARRIER-FAR from the zeta ordinates.
Its honest margin screen (reduced-margin slope -1.042 vs log m)
warned: the reduction changes the DIMENSION of the open statement,
maybe not its DIFFICULTY.  THE FROZEN IDEA: test exactly that with
classical bounds.  Each coefficient
    Fhat(omega_j) = sum_k f_k psi_j(u_k),
    f_k = 2 (Lambda(k) - 1)/sqrt(k)  (k = n_c+1 .. N_g),
    psi_j(u) = n_j cos(omega_j (u - u0))   (n_0 = 1/sqrt(Lu),
    n_j = sqrt(2/Lu) for j >= 1)
is a damped Mellin-type sum sum_n Lambda(n)/sqrt(n) phi_j(log n)
minus its smooth counterpart, with phi_j = 2 psi_j the explicit
windowed low-frequency test function -- a SMOOTH low-frequency
windowed functional of the psi-fluctuation, exactly the object
classical analytic bounds are best at.  Bound each coefficient by
partial summation against the SMOOTH psi_j (the anchor-price
lesson from CLVI: integrate by parts so only psi_j' appears --
|psi_j'| <= omega_j n_j is SMALL at low frequency), assemble
sum_j |c_g(omega_j)| bound_j against the demand, and measure
whether low-frequency smoothness finally beats the e^{+1.74 alpha}
gap law that killed every previous envelope (CLII/CLVI).
2026-08-11.)

THE COEFFICIENT BOUND (frozen).  With E1(k) = sum_{m=J..k} f_m
(the CLII fluctuation cumulant; J = n_c + 1) partial summation is
EXACT:
    Fhat_j = E1(N) psi_j(u_N)
             - sum_{k=J}^{N-1} E1(k) [psi_j(u_{k+1}) - psi_j(u_k)],
and |E1(k)| <= BE1(k) is the CLII windowed envelope chain
    BE1(k) = 2 [ beta(k)/sqrt(k) + sum_{m=J}^{k-1} beta(m)
             delta_m ],   beta(m) = bnd(m) + bnd(J-1),
    delta_m = m^{-1/2} - (m+1)^{-1/2},
warded in-window (|E1| <= BE1 everywhere, every rung, every
envelope).  Hence the PROVABLE per-coefficient bound
    |Fhat_j| <= bndX_j = BE1(N) |psi_j(u_N)|
                + sum_k BE1(k) |Delta psi_j(k)|         (exact-
                |Delta psi| route, used on the 12-bin carriers)
    |Fhat_j| <= bndD_j = n_j [ BE1(N)
                + sum_k BE1(k) min(2, omega_j du_k) ]   (cheap
                derivative-law route, used frame-wide)
-- the LOW-FREQUENCY PAYOFF is the omega_j factor: |Delta psi_j| ~
omega_j n_j du_k, and the carriers live at omega <= 5.25.

TWO ENVELOPE CLASSES bnd(x) (frozen; both deployed in-repo, the
fence status of each declared):
  ENV-A (Chebyshev table class, CLII amendment A1 verbatim):
    bnd_A(x) = KAPPA_INT x for x >= 100, else the table-exact
    |psi(x) - x|; KAPPA_INT = all-integer table constant
    max_{100 <= n <= 400000} |psi(n) - n|/n, in-run reproduction
    of CLII's 0.059547 (WARD).  Fence: pure finite-table
    verification, no zero content whatsoever.
  ENV-B (sqrt class, deployed at v594_unconditional_cert.py lines
    10-13 / constant line 47): |psi(x) - x| < 0.94 sqrt(x) for
    11 < x <= 1e19 (Buethe 2018, Math. Comp. 87); bnd_B(x) =
    0.94 sqrt(x) for x >= 12, else table-exact.  In-table
    re-verification on the whole deployed range (WARD).  Fence
    disclosure (honest): the PROOF PEDIGREE of this literature
    constant is zero-verification-based; the v594 typing is
    adopted verbatim -- "external data, no conjecture, no runtime
    zero input"; NO ordinate, zero datum or wall-positivity fact
    enters any computation here.  The strict table-only reading is
    served by the complete ENV-A ladder printed alongside.
  ENV-MIN = pointwise min(bnd_A, bnd_B) (each valid pointwise, so
    the min is): the certificate envelope.
THE ZERO-SIDE FENCE (frozen): the corpus' Selberg-class short-
window bounds -- v678_zero_gap_theorem.py lines 275-282 (Platt
|S| <= 2.5167 to 3.06e10; Trudgian 2014 A1 = 0.112; Bellotti 2025
Cor. 1.5 A1 = 0.10076) and v680_pinch_attack.py lines 226-231 +
A2.2 (Selberg count floors N[t +- delta/2], threshold-free where
Bellotti fails) -- are ZERO-COUNTING statements: routing them into
a psi-side coefficient bound requires the explicit formula over
the zeros, which the circularity fence forbids.  They are CITED
as a recorded comparison only and never used.  The gamma ordinates
appear ONLY in the (c) sub-gamma comparison (hardcoded literature
constants, wall_margin S2 pattern, never construction).

WHAT IS MEASURED (frozen; typed, never kills unless marked WARD):
 (a) THE 12 COEFFICIENTS AS CLASSICAL OBJECTS (WARD): the CLV
     pooling is reproduced verbatim (per-rung n90 carriers pooled
     by |t_j| into RED_BIN = 0.5 bins on the absolute omega axis,
     top K_RED = 12 centers, read-through |omega_j - center| <=
     RED_HALF = 0.5); WARDS: >= N_LOW_MIN = 10 centers <=
     CENT_LOW = 5.25 and every remaining center inside the trace
     band (13.0, 15.0); share_red min/med/max within SHARE_TOL =
     5e-3 of the CLV frozen (0.846, 1.006, 1.049).  The Mellin
     form is warded at frozen spots: Fhat_j (recurrence) ==
     2 sum Lambda(n)/sqrt(n) psi_j(u_n) - 2 sum psi_j(u_n)/sqrt(n)
     by direct cos evaluation (<= MELLIN_WARD rel).
 (b) PER-COEFFICIENT CLASSICAL BOUNDS (decisive): VALIDITY WARD
     |Fhat_j| <= bndX_j (ENV-MIN) on EVERY rung and EVERY in-bin
     coefficient (the bound is a theorem given the envelope ward
     -- a fail is a bug, kill).  THE HONESTY TABLE at the median
     rung (per in-bin j: omega, c_g, Fhat, bndX_A, bndX_B, bndX,
     ratio bndX/|Fhat|, boundary share); census of the per-rung
     median honesty ratio; boundary-vs-derivative share census
     (WHERE the certificate mass sits: the window-edge anchor
     price BE1(N) vs the omega_j-small derivative term).
 (c) THE ASSEMBLED CERTIFICATE + SLACK LADDER (decisive): with
     H = head_B(cB), Ttilde = sum (2/sqrt(k)) w_k, mu1 =
     4 sin^2(pi/(2h+1)), C0 = 1/2 (CLI registration, NO-ADJUST):
       demand: H + Ttilde - ERR >= C0 mu1;
       ERR12  = sum_{j in bins} |c_g(omega_j)| bndX_j  (certified,
                12-bin part),
       OUTD   = sum_{j notin bins} |c_g| bndD_j        (certified
                out-of-bin budget),
       ERR_full = ERR12 + OUTD  (fully classical modulo the
                measured <= 1% frame-truncation residual TRUNC,
                disclosed),
       OUT_meas = |sum_{j notin bins} c_j Fhat_j|, TRUNC =
                |P - sum_j c_j Fhat_j|  (measured, disclosed);
     slack ladder per rung (mu1 units, minus C0):
       L0 slack0 = shat - 1/2          (measured pairing; CLI
                    surface, min +2.48e-3 reproduced),
       L1 slack1 = (H + Ttilde - ERR12 - OUT_meas - TRUNC)/mu1
                    - C0               (certificate modulo the
                    measured out-of-bin + truncation reads),
       L2 slack2 = (H + Ttilde - ERR_full)/mu1 - C0  (the
                    certificate),
     each for ENV-A / ENV-B / ENV-MIN; nsplit = #(chat < C0) rungs
     (chat = (H + Ttilde)/mu1; CLII measured 3 deep rungs where
     the SPLIT ITSELF blocks -- no coefficient bound can help
     there, disclosed as split-blocked).  THE NEW GAP LAW:
     jackknife slope of log(ERR_full/mu1) and log(ERR12/mu1) vs
     alpha per envelope, against the reproduced CLII direct-route
     law (ERR_dir^A law slope within GAP_REP_TOL = 0.05 of +1.744,
     WARD) and the same-envelope direct baseline ERR_dir^MIN (the
     smoothness gain isolated from the envelope-class gain: gain =
     ERR_dir/ERR_full per rung).  Typed GAPLAW: DELTA = slope_MIN
     - slope_repro; IMPROVED iff DELTA + 2SEc < -0.2, WORSE iff
     DELTA - 2SEc > +0.2, SAME iff |DELTA| <= 0.2, else AMBIG
     (2SEc = 2(SE_MIN + SE_repro)).
 (d) OUTCOMES (frozen enum): HARMCERT-SUFFICIENT iff slack2(MIN)
     > 0 on ALL rungs (surface theorem stated with constants +
     tau-screen); HARMCERT-PARTIAL iff slack2 > 0 or slack1 > 0
     on >= 1 rung (census: ok2/ok1 counts, split-blocked rungs,
     per-failing-rung blocking center = argmax_center sum |c_j|
     bndX_j, histogram); else HARMCERT-INSUFFICIENT (the honesty
     ratios, the residual law, and the honest conclusion the CLV
     screen predicted: the difficulty relocated into the
     coefficients).
 (e) SUB-GAMMA STATEMENT (comparison only): census of the 12 bin
     centers against gamma_1 = 14.134725...; if ALL 12 sit below
     gamma_1 the statement "the certificate needs no zero
     information because the carriers are sub-gamma" is printed
     explicitly; the honest expected census is 10-11/12 (the
     13.25/14.25 trace bins), printed as measured either way.
     The bounds themselves input no zero anywhere (fence above).
 (f) SEAT SCREENS (recorded): which side carries the -1.042
     margin decay -- jackknife slopes vs log m of log sum_bins
     |c_j| (weight side), log(sum_bins |Fhat_j| / mu1)
     (fluctuation side), and the CLV reproduction log |P_red/mu1|
     (expected ~ -1.042).
 (g) TAU-SCREENS (typed, jackknife, bands PASS |s| <= 0.30 /
     RELOC s >= 0.70 / else AMBIG): vs log m of log(ERR12_MIN/
     mu1), log(ERR_full_MIN/mu1), log(median honesty ratio).

FROZEN PROTOCOL (ladder + frame machinery verbatim from
tail_oscillation_pairing_probe.py = round-59/60/62/63 chain; the
envelope chain verbatim from tail_abel_transport_probe.py):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN):
     W1-W8 verbatim CLV (faithful ladder >= 40; m_h > 0; exact
     bookkeepings; atom identities; scan splits; round-59/60/62
     reproduction incl. n_minB med 17, head_B(cB) med 0.388; v_sm
     branch; mu1 closed form + CXLIII shat band); W9-W12 verbatim
     CLV (grid tie; pairing tie; frame closed-form vs GL5 +
     recurrence spots; Fubini + residual share <= 0.01 on every
     rung); W13 ENVELOPES: (a) core.chebyshev_kappa() within 1e-6
     of 0.038821; (b) KAPPA_INT within 5e-6 of 0.059547; (c)
     Buethe in-table max |psi(n)-n|/(0.94 sqrt(n)) < 1 on [12,
     400000]; (d) |E1| <= BE1 in-window on every rung for ENV-A/
     B/MIN (float slack <= ENV_SLACK); (e) CLII reproduction:
     chat >= 1/2 count == 64 and the direct-route ENV-A gap law
     slope within 0.05 of +1.744; W14 Mellin spot ward as in (a).

 A/B/E/G/R/T  as (a)/(b)/(c,d)/(e)/(f)/(g) above.

 C   CONTROLS at kz 9 (kill -> WARD-BROKEN if silent): C1
     scramble (seed 1), Epstein x^2+5y^2, smooth comb: m < 0 AND
     zero covering cuts in BOTH senses (round-62 criterion, WARD).
     C2 certificate battery at the FIXED cut CTRL_CUT = 17 (CLV
     C2 pattern; all worlds on the same snapped integer grid):
     C2a the by-construction integer-continuum world Lambda == 1
     has f == 0 identically -> every Fhat == 0 exactly and the
     certificate holds trivially (WARD, exact zero); C2b scramble
     DC blowup |Fhat_scr(0)|/|Fhat_true(0)| >= SCR_BLOWUP = 5
     (WARD, the PNT cancellation is destroyed); C2c DISCRIMINATION
     DIRECTION through the measured coefficients: true world obeys
     |Fhat_true_j| <= bndX_j on every in-bin j at the control cut
     (WARD -- theorem); the scramble/Epstein in-bin violation
     census (count |Fhat_world_j| > bndX_j, max ratio) is TYPED
     and recorded: violations >= 1 mean the certificate fails on
     those worlds through the measured coefficients; 0 violations
     is the honest record that these bounds are too loose to
     discriminate (consistent with large honesty ratios) -- either
     answer is a result, no kill.

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W14, A,
B-validity, C1/C2a/C2b/C2c-true) -> WARD-BROKEN.  All typed E/G/
R/T outcomes are measurements, never kills.

VERDICT (frozen enum): HARMCERT-MEASURED with typed sublabels
BINS-REPRODUCED(K, med share) [WARD],
BOUNDS-VALID [WARD] + HONESTY(min/med/max per-rung med ratio,
boundary share),
LADDER(ok2/ok1/N per env, nsplit),
HARMCERT-SUFFICIENT / -PARTIAL(census) / -INSUFFICIENT(ratios,
residual law),
GAPLAW(A, B, MIN slopes vs repro +1.744, typed IMPROVED/SAME/
WORSE/AMBIG) + GAIN(direct/harmonic med),
SUBGAMMA(n/12),
SEAT(c, F, red slopes),
SCREENS(...), CTRL(...);  else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; REF_CUTS = (50, 100,
200); REF_COUNTS = (52, 26, 25); NMIN_LO, NMIN_HI = 3, 9;
NC_SHARED = 9; NB_MED = 17; NB_LO, NB_HI = 5, 47; HEADB_MED =
0.388, HEADB_TOL = 0.01; SHAT_REF = (0.502, 1.027, 2.185),
SHAT_TOL = 1.5e-3; ID_WARD = 1e-10; SCAN_WARD = 1e-9; TIE_WARD =
1e-10; PAIR_WARD = 1e-12; FUB_WARD = 1e-9; QUAD_WARD = 1e-9;
REC_WARD = 1e-9; RES_WARD = 0.01; MU_WARD = 1e-12; NG_SMOOTH =
6000; OV_MIN = 0.8; MAX_CROSS = 2; OMEGA_MAX = 240.0; J_CAP =
4096; GL5_SEG = 0.5; RED_BIN = 0.5; RED_HALF = 0.5; K_RED = 12;
KAPPA_REF = 0.038821, KAPPA_TOL = 1e-6; KINT_REF = 0.059547,
KINT_TOL = 5e-6; KAPPA_LOW_X = 100; BUETHE = 0.94, BUETHE_LO =
12; ENV_SLACK = 1e-9; BND_SLACK = 1e-9; MELLIN_WARD = 1e-9;
GAP_REF = 1.744, GAP_REP_TOL = 0.05; CHAT_REF_COUNT = 64; C0 =
1/2 (frozen, NO-ADJUST, CLI registration); CENT_LOW = 5.25;
N_LOW_MIN = 10; TRACE_LO, TRACE_HI = 13.0, 15.0; SHARE_REF =
(0.846, 1.006, 1.049), SHARE_TOL = 5e-3; GAMMA1 =
14.134725141734693 (literature comparison constant); GAPLAW_TOL
= 0.2; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9;
CTRL_CUT = 17; SCR_BLOWUP = 5.0; scramble seed 1; jackknife =
full leave-one-out, CI = +-2SE; blocked cumulative sums (block
1024) wherever a cumsum feeds a ward; CLI_MIN_REF = 2.48e-3
(print-only reproduction).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE full
smoke run (SPEC v0, 28/28 checks, 22.9 s), NO amendment -- no
bar, band, tolerance, enum or rule moved after the smoke.  Facts
frozen as the context the frozen run must confirm: (i) every
ward green on the FIRST pass: KAPPA_INT 0.059547 exact; Buethe
in-table worst ratio 0.827 < 1; |E1| <= BE1 max slack 9.3e-17
(all 3 envelopes, all rungs); chat >= 1/2 on 64/67; direct ENV-A
gap law +1.7436 ~ CLII +1.744; bins reproduced exactly (centers
0.25..5.25 ten of them + 13.25/14.25, shares 0.846/1.006/1.049);
Mellin spots 1.54e-14; bound validity worst rel excess -0.792
(ladder) / -0.800 (control cut); median rung kz 53 = the CLV
table rung.  (ii) THE HEADLINE (honest, decisive):
HARMCERT-INSUFFICIENT on 67/67 at EVERY ladder level in EVERY
envelope (ok1 = ok2 = 0; ENV-MIN ERR12/mu1 med 5.89e+05, slack2
min/med -7.78e+06/-7.09e+05; nsplit = 3, kz 95/97/100 = the CLII
chat < 1/2 rungs).  The gap-law census DECOMPOSES the exponent:
harmonic ENV-A +2.0540 is WORSE than the direct route's +1.7436
-- the triangle inequality across 12 carriers costs MORE than
the omega-smallness saves; the same-envelope gain ERR_dir^MIN/
ERR_full^MIN is min/med/max 0.07/0.14/0.22, i.e. the harmonic
certificate is ~7x MORE expensive than the direct envelope at
identical bnd(x): LOW-FREQUENCY SMOOTHNESS DOES NOT BEAT THE
ENVELOPE CURSE, it loses to it.  The entire exponent improvement
+1.74 -> +1.45 (harmonic ENV-B +1.4296, ENV-MIN +1.4530; direct
ENV-MIN +1.4497) comes from the ENVELOPE CLASS (Buethe sqrt vs
Chebyshev table) and is equally available to the direct route;
DELTA(MIN vs repro) = -0.291 with comb 2SE 0.405 -> typed AMBIG
per the frozen band.  (iii) the certificate mass is NOT
boundary-dominated: window-edge anchor share med 0.10 -- the
bulk sum BE1|Delta psi_j| carries the bound; honesty ratios
bndX_MIN/|Fhat| per-rung med min/med/max 3.6e+01/9.4e+01/
7.7e+02, and the honesty tau-screen is FLAT (-0.210 PASS): the
per-coefficient looseness does not worsen with depth -- the
demand scale does.  (iv) SEAT ANSWER to the CLV question: weight
side log sum|c_g| vs log m -0.080 (R^2 0.62, near-flat);
fluctuation side log(sum|Fhat|/mu1) vs log m -1.077 (R^2 0.94);
P_red repro -1.042 exact: THE FLUCTUATION SIDE carries the
margin decay -- Fhat grows relative to mu1, c_g barely moves.
(v) sub-gamma census 11/12: the 14.25 trace bin straddles
gamma_1 = 14.13; the 10 low-frequency centers that carry the
reduced pairing sit below gamma_1.  (vi) tau-screens ERR12
-1.081 / ERRfull -1.063 both AMBIG (anti-correlated, the CLII
pattern), honesty -0.210 PASS.  (vii) controls: C1 3/3; C2a
exact zero; C2b scramble DC blowup 32.6 >= 5 FIRES; C2c true
world obeys every in-bin bound at cut 17, and the DISCRIMINATION
DIRECTION FIRES THROUGH THE MEASURED COEFFICIENTS on scramble:
2/7 in-bin bins violate the classical bound (max ratio 6.53);
Epstein 0/7 (max ratio 0.76) recorded -- Epstein's coefficients
stay inside the classical envelope at this depth, typed.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1
(unchanged from v0): (i) the cut is INCLUSIVE at the covering
atom (grid starts at n_c + 1); (ii) N_g = max(floor(X), largest
window atom); (iii) Lambda from the deployed core.LAM_TAB, psi =
its cumsum (grid tie warded); (iv) the DC bin j = 0 is a frame
bin like any other (n_0 = 1/sqrt(Lu); its exact bound is the
pure boundary term BE1(N) n_0); (v) in-bin set per rung =
{j: min_c |omega_j - c| <= RED_HALF}; (vi) median rung = the
rung at argsort(P)[N//2] (CLV convention, kz 53 confirmed); (vii)
runtime ~ 25 s (67 eigh pairs + two spectral passes + the
envelope chains dominate).

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity or bound is
claimed (partial summation, the envelope chains and every tie are
exact bookkeeping; all trends are typed jackknife screens).

NO RH claim: everything here is float-level MEASURED SURFACE
STRUCTURE on the 67-rung ladder; the direction v is computed
per-rung data (the round-62 uniformity boundary applies
verbatim); a HARMCERT-SUFFICIENT outcome would be a per-rung
surface certificate, not a theorem; a HARMCERT-INSUFFICIENT
outcome is a measured residual law, not a proof of
impossibility.  The halfgap constant 1/2 is the CLI registration
and is NEVER adjusted here.  No marker moves.

FIREWALL: no zeros in construction, no prime oracles (AST scan;
banned ids zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime; Lambda is read from the DEPLOYED window
table only; GAMMAS and GAMMA1 are hardcoded literature tuples
used only in comparison REPORTS, wall_margin S2 pattern; BUETHE
= 0.94 is a published literature envelope constant, provenance
disclosed above, v594 typing adopted); v563 READ-ONLY; RNG only
inside the declared scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (core); ladder + frame
+ pooling machinery verbatim from tail_oscillation_pairing_probe
.py (CLV); envelope chain verbatim from tail_abel_transport_probe
.py (CLII); q_read + v_sm construction verbatim from
arithmetic_lift_race_probe.py; mu1 normalization from
moving_node_second_order_probe.py (CXLIII); halfgap constant
C0 = 1/2 from halfgap_registration_probe.py (CLI, NO-ADJUST);
Buethe envelope from v594_unconditional_cert.py (lines 10-13,
47); zero-side Selberg-class constants CITED ONLY from
v678_zero_gap_theorem.py (lines 275-282) and v680_pinch_attack.py
(lines 226-231).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/finite_harmonic_certificate_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

KZMAX = 150
MIN_RUNGS = 40
REF_CUTS = (50, 100, 200)
REF_COUNTS = (52, 26, 25)
NMIN_LO, NMIN_HI = 3, 9
NC_SHARED = 9
NB_MED = 17
NB_LO, NB_HI = 5, 47
HEADB_MED = 0.388
HEADB_TOL = 0.01
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_TOL = 1.5e-3
ID_WARD = 1e-10
SCAN_WARD = 1e-9
TIE_WARD = 1e-10
PAIR_WARD = 1e-12
FUB_WARD = 1e-9
QUAD_WARD = 1e-9
REC_WARD = 1e-9
RES_WARD = 0.01
MU_WARD = 1e-12
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
OMEGA_MAX = 240.0
J_CAP = 4096
RED_BIN = 0.5
RED_HALF = 0.5
K_RED = 12
KAPPA_REF = 0.038821
KAPPA_TOL = 1e-6
KINT_REF = 0.059547
KINT_TOL = 5e-6
KAPPA_LOW_X = 100
BUETHE = 0.94
BUETHE_LO = 12
ENV_SLACK = 1e-9
BND_SLACK = 1e-9
MELLIN_WARD = 1e-9
GAP_REF = 1.744
GAP_REP_TOL = 0.05
CHAT_REF_COUNT = 64
C0 = 0.5
CENT_LOW = 5.25
N_LOW_MIN = 10
TRACE_LO, TRACE_HI = 13.0, 15.0
SHARE_REF = (0.846, 1.006, 1.049)
SHARE_TOL = 5e-3
GAMMA1 = 14.134725141734693
GAPLAW_TOL = 0.2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
CTRL_CUT = 17
SCR_BLOWUP = 5.0
CLI_MIN_REF = 2.48e-3
BLOCK = 1024
ENVS = ("A", "B", "MIN")
# first ten zeta ordinates -- literature constants, used ONLY in
# the sub-gamma comparison reports (never construction)
GAMMAS = (14.134725141734693, 21.022039638771555,
          25.010857580145688, 30.424876125859513,
          32.935061587739190, 37.586178158825671,
          40.918719012147495, 43.327073280914999,
          48.005150881167159, 49.773832477672302)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
GL5_SEG = 0.5
GL5_X = (-0.9061798459386640, -0.5384693101056831, 0.0,
         0.5384693101056831, 0.9061798459386640)
GL5_W = (0.2369268850561891, 0.4786286704993665,
         0.5688888888888889, 0.4786286704993665,
         0.2369268850561891)

CHECKS = []
KILLS = []
T0 = time.time()

PSI_TAB = np.cumsum(core.LAM_TAB)          # psi(n) on the table


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


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def blocked_cumsum(x):
    x = np.asarray(x, float)
    n = len(x)
    if n <= BLOCK:
        return np.cumsum(x)
    pad = (-n) % BLOCK
    xb = np.concatenate([x, np.zeros(pad)]).reshape(-1, BLOCK)
    cs = np.cumsum(xb, axis=1)
    off = np.concatenate([[0.0], np.cumsum(cs[:-1, -1])])
    return (cs + off[:, None]).reshape(-1)[:n]


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface (CLV verbatim)."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D,
               m=float(w[0]), uu=uu, mu=mu, X=float(rr["X"]))
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    e_s = float(c_sm @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    row.update(e_ar=e_ar, e_t=e_t, e_s=e_s, lift=e_t - e_s,
               demand=-(e_ar + e_s),
               dev_at=max(abs(float(qa.sum()) - e_t)
                          / max(abs(e_t), 1e-30),
                          abs(float(qg.sum()) - e_s)
                          / max(abs(e_s), 1e-30)))
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    G = head_err - row["demand"]
    tail_A = row["lift"] - head_err
    cert_A = G - np.abs(tail_A)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    smoothtail = float(qg.sum()) - cg_all[idxg]
    row.update(G=G, tail_A=tail_A, cert_A=cert_A, head_B=head_B,
               tail_B=tail_B, cert_B=cert_B, smoothtail=smoothtail,
               qa=qa)
    row["Gref"] = {}
    for nc in REF_CUTS:
        ucut = math.log(nc)
        he = (float(qa[uu <= ucut].sum())
              - float(qg[ug <= ucut].sum()))
        row["Gref"][nc] = he - row["demand"]
    if need_sm:
        ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
        vsm = Vs[:, 0]
        if float(v @ vsm) < 0:
            vsm = -vsm
        ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
        jcar = int(np.argmax(ov4))
        vcar = Vs[:, jcar] * (1.0 if float(v @ Vs[:, jcar]) >= 0
                              else -1.0)
        row.update(ov=float(abs(v @ vsm)), ov4=ov4, jcar=jcar)
        row["Wsm"] = core.lag_weights_from_v(vsm, h)
        row["Wcar"] = core.lag_weights_from_v(vcar, h)
    row["Wv"] = Wv
    return row


# ----------------------------------------------------- the frame
def frame_freqs(Lu):
    J = min(J_CAP, int(math.ceil(OMEGA_MAX * Lu / math.pi)) + 1)
    return np.pi * np.arange(J) / Lu, J


def weight_pieces(row, u0, uL, W):
    D, M = row["D"], row["M"]
    i_lo = int(math.floor(u0 / D)) + 1
    i_hi = int(math.ceil(uL / D)) - 1
    knots = D * np.arange(i_lo, i_hi + 1, dtype=float)
    knots = knots[(knots > u0 + 1e-12) & (knots < uL - 1e-12)]
    edges = np.concatenate([[u0], knots, [uL]])
    a_p, b_p = edges[:-1], edges[1:]
    wa = q_read(W, a_p, D, M)
    wb = q_read(W, b_p, D, M)
    s_p = (wb - wa) / (b_p - a_p)
    return a_p, b_p, wa, s_p


def cosine_coeffs(om, Lu, u0, a_p, b_p, wa, s_p):
    J = len(om)
    ga = a_p - u0
    gb = b_p - u0
    ln = b_p - a_p
    craw = np.empty(J)
    craw[0] = float(np.sum(wa * ln + 0.5 * s_p * ln * ln))
    th = om[1:][:, None]
    sin_a = np.sin(th * ga[None, :])
    sin_b = np.sin(th * gb[None, :])
    cos_a = np.cos(th * ga[None, :])
    cos_b = np.cos(th * gb[None, :])
    I0 = (sin_b - sin_a) / th
    I1 = ln[None, :] * sin_b / th + (cos_b - cos_a) / (th * th)
    craw[1:] = I0 @ wa + I1 @ s_p
    c = craw.copy()
    c[0] /= math.sqrt(Lu)
    c[1:] *= math.sqrt(2.0 / Lu)
    return c


def gl5_coeff(om_j, Lu, u0, a_p, b_p, wa, s_p, j):
    width = b_p - a_p
    ns = max(1, int(math.ceil(float(np.max(width))
                              * max(om_j, 1.0) / GL5_SEG)))
    tt = np.arange(ns, dtype=float) / ns
    A = (a_p[:, None] + width[:, None] * tt[None, :]).ravel()
    Wd = np.repeat(width / ns, ns)
    WA = (wa[:, None]
          + s_p[:, None] * (width[:, None] * tt[None, :])).ravel()
    S = np.repeat(s_p, ns)
    mid = A + 0.5 * Wd
    half = 0.5 * Wd
    acc = 0.0
    for xg, wg in zip(GL5_X, GL5_W):
        u = mid + half * xg
        wval = WA + S * (u - A)
        acc += wg * float(np.sum(half * wval
                                 * np.cos(om_j * (u - u0))))
    return acc * (1.0 / math.sqrt(Lu) if j == 0
                  else math.sqrt(2.0 / Lu))


def spectral_pair(ug, f, cv, cs, om, Lu, u0, rec_spot=False):
    J = len(om)
    x = ug - u0
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    c1v = np.cos((math.pi / Lu) * x)
    Fh = np.empty(J)
    Rv = np.zeros(len(ug))
    Rs = np.zeros(len(ug))
    prev = np.ones(len(ug))
    cur = c1v.copy()
    rec_dev = 0.0
    for j in range(J):
        if j == 0:
            cj, nj = prev, n0
        elif j == 1:
            cj, nj = cur, n1
        else:
            nxt = 2.0 * c1v * cur - prev
            prev, cur = cur, nxt
            cj, nj = cur, n1
        Fh[j] = nj * float(f @ cj)
        Rv += (cv[j] * nj) * cj
        Rs += (cs[j] * nj) * cj
        if rec_spot and j == J - 1:
            direct = np.cos(om[j] * x)
            rec_dev = float(np.max(np.abs(cj - direct)))
    return Fh, Rv, Rs, rec_dev


def pairing_census(t, om):
    tot = float(np.sum(t))
    sgn = 1.0 if tot >= 0.0 else -1.0
    order = np.argsort(-(t * sgn), kind="stable")
    pref = np.cumsum(t[order] * sgn)
    tgt = abs(tot)
    n50 = int(np.argmax(pref >= 0.5 * tgt)) + 1
    n90 = int(np.argmax(pref >= 0.9 * tgt)) + 1
    at = np.abs(t)
    pr = float(at.sum() ** 2 / max(float((at * at).sum()),
                                   1e-300))
    jstar = int(np.argmax(at))
    return dict(tot=tot, n50=n50, n90=n90, pr=pr,
                jstar=jstar, om_star=float(om[jstar]),
                S90=order[:n90])


# ------------------------------------------- the envelope chains
def bnd_env(kf, which):
    """Pointwise psi-deviation envelope bnd(n) on integer n
    (float array kf); ENV-A = CLII table class, ENV-B = Buethe
    sqrt class, ENV-MIN = pointwise min (each valid, so the min
    is)."""
    nn = np.asarray(np.round(kf), int)
    exact = np.abs(PSI_TAB[nn] - kf)
    if which == "A":
        return np.where(kf >= KAPPA_LOW_X, KINT[0] * kf, exact)
    if which == "B":
        return np.where(kf >= BUETHE_LO, BUETHE * np.sqrt(kf),
                        exact)
    return np.minimum(
        np.where(kf >= KAPPA_LOW_X, KINT[0] * kf, exact),
        np.where(kf >= BUETHE_LO, BUETHE * np.sqrt(kf), exact))


KINT = [None]                              # set in main (in-run)


def be1_chain(kf, which):
    """BE1(k) on the deep grid (CLII chain verbatim, envelope
    `which`): BE1(k) = 2 [beta(k)/sqrt(k) + sum_{m<k} beta(m)
    delta_m], beta(m) = bnd(m) + bnd(J-1)."""
    J0 = float(kf[0]) - 1.0
    b0 = float(bnd_env(np.array([J0]), which)[0])
    beta = bnd_env(kf, which) + b0
    delta = kf[:-1] ** -0.5 - kf[1:] ** -0.5
    cum = np.concatenate([[0.0],
                          blocked_cumsum(beta[:-1] * delta)])
    return 2.0 * (beta / np.sqrt(kf) + cum)


def envelope_pack(row, nc, om, Lu, u0, ug, kf, f, wv,
                  spots=()):
    """Per-rung envelope work while the deep grid is alive:
    E1 in-window ward, direct-route ERR per envelope, cheap
    frame-wide per-coefficient bounds bndD (3 x J), Mellin spot
    ward."""
    E1 = blocked_cumsum(f)
    du = np.diff(ug)
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    out = dict(e1_slack={}, err_dir={}, bndD={})
    for which in ENVS:
        BE1 = be1_chain(kf, which)
        sc = max(float(np.max(BE1)), 1e-300)
        out["e1_slack"][which] = float(
            np.max(np.abs(E1) - BE1)) / sc
        out["err_dir"][which] = (
            float(BE1[-1]) * abs(float(wv[-1]))
            + float(BE1[:-1] @ np.abs(np.diff(wv))))
        P0 = np.concatenate([[0.0], blocked_cumsum(BE1[:-1])])
        P1 = np.concatenate([[0.0],
                             blocked_cumsum(BE1[:-1] * du)])
        J = len(om)
        bndD = np.empty(J)
        bndD[0] = n0 * float(BE1[-1])
        omp = om[1:]
        idx = np.searchsorted(-du, -(2.0 / omp), side="left")
        sumM = 2.0 * P0[idx] + omp * (P1[-1] - P1[idx])
        bndD[1:] = n1 * (float(BE1[-1]) + sumM)
        out["bndD"][which] = bndD
        out["BE1_last_" + which] = float(BE1[-1])
    # Mellin spot ward: recurrence Fhat vs the explicit damped
    # Mellin split 2 sum Lam/sqrt psi_j - 2 sum psi_j/sqrt
    if spots:
        lamg = core.LAM_TAB[int(kf[0]):int(kf[-1]) + 1]
        inv = 1.0 / np.sqrt(kf)
        x = ug - u0
        dev = 0.0
        for j, fh_j in spots:
            nj = n0 if j == 0 else n1
            cj = np.cos(om[j] * x)
            s_lam = 2.0 * float((lamg * inv) @ cj)
            s_sm = 2.0 * float(inv @ cj)
            scale = max(nj * float(np.abs(f) @ np.abs(cj)),
                        1e-300)
            dev = max(dev, abs(fh_j - nj * (s_lam - s_sm))
                      / scale)
        out["mellin_dev"] = dev
    else:
        out["mellin_dev"] = 0.0
    return out


def bndx_exact(kf, ug, u0, om, Lu, jset):
    """Exact-|Delta psi| per-coefficient bounds for the in-bin
    coefficients, all three envelopes.  Returns dict which ->
    array over jset, plus the boundary share (ENV-MIN)."""
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    x = ug - u0
    BE1 = {w: be1_chain(kf, w) for w in ENVS}
    res = {w: np.empty(len(jset)) for w in ENVS}
    bshare = np.empty(len(jset))
    for i, j in enumerate(jset):
        nj = n0 if j == 0 else n1
        cj = np.cos(om[j] * x)
        dif = np.abs(np.diff(cj))
        clast = abs(float(cj[-1]))
        for w in ENVS:
            bt = float(BE1[w][-1]) * clast
            res[w][i] = nj * (bt + float(BE1[w][:-1] @ dif))
        btm = float(BE1["MIN"][-1]) * clast
        tot = btm + float(BE1["MIN"][:-1] @ dif)
        bshare[i] = btm / max(tot, 1e-300)
    return res, bshare


def build_spectral(row, nc, spot=False):
    """The full frequency-space object of one rung (CLV verbatim)
    + the envelope pack of this probe."""
    Ng = max(int(math.floor(row["X"])),
             int(np.round(math.exp(float(row["uu"][-1])))))
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    lamg = core.LAM_TAB[nc + 1:Ng + 1]
    inv_sq = 1.0 / np.sqrt(kf)
    a = 2.0 * lamg * inv_sq
    f = a - 2.0 * inv_sq
    wv = q_read(row["Wv"], ug, row["D"], row["M"])
    Ws = row["Wcar"] if row["ov"] < OV_MIN else row["Wsm"]
    ws = q_read(Ws, ug, row["D"], row["M"])
    T = float(a @ wv)
    Tt = float((2.0 * inv_sq) @ wv)
    P_v = float(f @ wv)
    P_s = float(f @ ws)
    pair_scale = max(float(np.abs(f) @ np.abs(wv)), 1e-300)
    dev_pair = abs((T - Tt) - P_v) / pair_scale
    u0, uL = float(ug[0]), float(ug[-1])
    Lu = uL - u0
    om, J = frame_freqs(Lu)
    pv = weight_pieces(row, u0, uL, row["Wv"])
    ps = weight_pieces(row, u0, uL, Ws)
    cv = cosine_coeffs(om, Lu, u0, *pv)
    cs = cosine_coeffs(om, Lu, u0, *ps)
    Fh, Rv, Rs, rec_dev = spectral_pair(ug, f, cv, cs, om, Lu,
                                        u0, rec_spot=spot)
    P_rec_v = float(cv @ Fh)
    P_rec_s = float(cs @ Fh)
    res_v = abs(P_v - P_rec_v) / max(abs(P_v), 1e-300)
    res_s = abs(P_s - P_rec_s) / max(abs(P_s), 1e-300)
    dev_fub = max(abs(float(f @ Rv) - P_rec_v),
                  abs(float(f @ Rs) - P_rec_s)) / pair_scale
    sup_v = float(np.max(np.abs(wv - Rv))
                  / max(float(np.max(np.abs(wv))), 1e-300))
    quad_dev = 0.0
    if spot:
        for (pc, cc) in ((pv, cv), (ps, cs)):
            mxc = max(float(np.max(np.abs(cc))), 1e-300)
            for j in (1, J // 2, J - 1):
                g5 = gl5_coeff(float(om[j]), Lu, u0, *pc, j)
                quad_dev = max(quad_dev,
                               abs(cc[j] - g5) / mxc)
    t_v = cv * Fh
    cen_v = pairing_census(t_v, om)
    spots = (((1, float(Fh[1])), (J // 2, float(Fh[J // 2])),
              (J - 1, float(Fh[J - 1]))) if spot else ())
    env = envelope_pack(dict(row), nc, om, Lu, u0, ug, kf, f,
                        wv, spots=spots)
    return dict(T=T, Tt=Tt, P_v=P_v, P_s=P_s, dev_pair=dev_pair,
                res_v=res_v, res_s=res_s, dev_fub=dev_fub,
                sup_v=sup_v, quad_dev=quad_dev, rec_dev=rec_dev,
                om=om, J=J, Lu=Lu, u0=u0, Fh=Fh, cv=cv, cs=cs,
                t_v=t_v, cen_v=cen_v, nc=nc, Ng=Ng, env=env,
                P_rec_v=P_rec_v)


def regen_grid(nc, Ng):
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    return kf, np.log(kf)


def ctrl_spectral(r, cut):
    """C2 control read (CLV verbatim): comb snapped to the
    integer grid, paired through the world's OWN weight."""
    Ng = int(math.floor(r["X"]))
    nn = np.round(np.exp(np.asarray(r["uu"], float))
                  ).astype(np.int64)
    ag = np.zeros(Ng + 2)
    keep = (nn >= cut + 1) & (nn <= Ng)
    np.add.at(ag, nn[keep], np.asarray(r["mu"], float)[keep])
    kk = np.arange(cut + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    inv_sq = 1.0 / np.sqrt(kf)
    f = ag[kk] - 2.0 * inv_sq
    wv = q_read(r["Wv"], ug, r["D"], r["M"])
    P = float(f @ wv)
    u0, uL = float(ug[0]), float(ug[-1])
    Lu = uL - u0
    om, J = frame_freqs(Lu)
    x = ug - u0
    c1v = np.cos((math.pi / Lu) * x)
    Fh = np.empty(J)
    prev = np.ones(len(ug))
    cur = c1v.copy()
    for j in range(J):
        if j == 0:
            cj, nj = prev, 1.0 / math.sqrt(Lu)
        elif j == 1:
            cj, nj = cur, math.sqrt(2.0 / Lu)
        else:
            nxt = 2.0 * c1v * cur - prev
            prev, cur = cur, nxt
            cj, nj = cur, math.sqrt(2.0 / Lu)
        Fh[j] = nj * float(f @ cj)
    return dict(P=P, F0=float(Fh[0]), om=om, Fh=Fh, Lu=Lu,
                u0=u0, kf=kf, ug=ug)


def main():
    section("PRIME.PORT.FINITE.HARMONIC.01 -- the finite "
            "harmonic certificate (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; gamma ordinates are "
          "literature comparison constants only;")
    print("    envelope classes: ENV-A table Chebyshev (KAPPA_INT"
          ", CLII A1), ENV-B Buethe 0.94 sqrt(x)")
    print("    (v594_unconditional_cert.py:10-13,47 -- published "
          "literature constant, proof pedigree via")
    print("    verified zeros DISCLOSED, no runtime zero input; "
          "v594 'external data' typing adopted).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    # the in-run all-integer table constant (CLII amendment A1)
    nn = np.arange(KAPPA_LOW_X, core.ATOM_MAX + 1)
    KINT[0] = float(np.max(np.abs(PSI_TAB[nn] - nn) / nn))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        row = build_rung(kz)
        if row is not None:
            rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(max(abs((r["lift"] - r["demand"]) - r["m"]),
                     abs((r["e_ar"] + r["e_t"]) - r["m"]))
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD both exact bookkeepings: max dev %.2e <= %.0e"
          % (dev_bk, ID_WARD), dev_bk <= ID_WARD, kill="K2")
    dev_at = max(r["dev_at"] for r in rungs)
    check("W4 WARD atom identities: max rel dev %.2e <= %.0e"
          % (dev_at, ID_WARD), dev_at <= ID_WARD, kill="K2")
    dev_sc = 0.0
    for r in rungs:
        sc = max(float(np.max(np.abs((r["head_B"] + r["tail_B"])
                                     - r["m"]))),
                 float(np.max(np.abs((r["G"] + r["tail_A"])
                                     - r["m"]))),
                 float(np.max(np.abs(r["G"] - r["head_B"]
                                     - r["smoothtail"]))))
        dev_sc = max(dev_sc, sc / max(1.0, abs(r["e_t"])))
    check("W5 WARD split exactness on the full scans: max rel "
          "dev %.2e <= %.0e" % (dev_sc, SCAN_WARD),
          dev_sc <= SCAN_WARD, kill="K2")
    cnts = tuple(int(np.sum(np.array(
        [r["Gref"][nc] for r in rungs]) > 0)) for nc in REF_CUTS)
    n_min, nB_min, icBs, tB_neg = [], [], [], 0
    for r in rungs:
        nn_ = np.round(np.exp(r["uu"])).astype(int)
        covA = r["cert_A"] > 0.0
        i0 = int(np.argmax(covA)) if bool(np.any(covA)) else -1
        n_min.append(int(nn_[i0]) if i0 >= 0 else -1)
        covB = r["cert_B"] > 0.0
        icB = int(np.argmax(covB)) if bool(np.any(covB)) else -1
        icBs.append(icB)
        nB_min.append(int(nn_[icB]) if icB >= 0 else -1)
        if icB >= 0 and float(r["tail_B"][icB]) <= 0.0:
            tB_neg += 1
    i9s = [int(np.searchsorted(r["uu"],
                               math.log(NC_SHARED) + 1e-12,
                               side="right")) - 1 for r in rungs]
    cov9 = sum(1 for r, i9 in zip(rungs, i9s)
               if i9 >= 0 and r["cert_A"][i9] > 0)
    tA_neg = sum(1 for r in rungs if bool(np.any(r["cert_A"] > 0))
                 and r["tail_A"][int(np.argmax(
                     r["cert_A"] > 0))] <= 0.0)
    covB_n = sum(1 for i in icBs if i >= 0)
    hBc = np.array([float(r["head_B"][i])
                    for r, i in zip(rungs, icBs)])
    medB = float(np.median([n for n in nB_min if n > 0]))
    ok_rep = (cnts == REF_COUNTS
              and all(NMIN_LO <= nm <= NMIN_HI for nm in n_min)
              and cov9 == N and tA_neg == N and covB_n == N
              and medB == NB_MED
              and min(nB_min) >= NB_LO and max(nB_min) <= NB_HI
              and tB_neg == N
              and abs(float(np.median(hBc)) - HEADB_MED)
              <= HEADB_TOL)
    check("W6 REPRODUCTION 59/60/62: G > 0 at %s = %s == %s; "
          "n_min in [%d, %d]; cut 9 covers %d/%d; tail_A <= 0 "
          "%d/%d; B-cuts exist %d/%d, n_minB med %d in [%d, %d]; "
          "tail_B <= 0 at cB %d/%d; head_B(cB) med %.3f ~ %.3f"
          % (REF_CUTS, cnts, REF_COUNTS, NMIN_LO, NMIN_HI, cov9,
             N, tA_neg, N, covB_n, N, int(medB), min(nB_min),
             max(nB_min), tB_neg, N, float(np.median(hBc)),
             HEADB_MED), ok_rep, kill="K2")
    n_cross = sum(1 for r in rungs if r["ov"] < OV_MIN)
    cross_ok = all(max(r["ov4"]) >= OV_MIN for r in rungs
                   if r["ov"] < OV_MIN)
    check("W7 WARD v_sm branch: %d crossing rung(s) (%s; ward <= "
          "%d), carrier ok"
          % (n_cross,
             ", ".join("kz%d ov %.4f" % (r["kz"], r["ov"])
                       for r in rungs if r["ov"] < OV_MIN)
             or "none", MAX_CROSS),
          n_cross <= MAX_CROSS and cross_ok, kill="K2")
    mu1 = np.array([float(core.parity_mu(r["h"])[0])
                    for r in rungs])
    mu1_cf = np.array([4.0 * math.sin(math.pi
                                      / (2 * r["h"] + 1)) ** 2
                       for r in rungs])
    dev_mu = float(np.max(np.abs(mu1 - mu1_cf)
                          / np.maximum(mu1, 1e-300)))
    mm = np.array([r["m"] for r in rungs])
    shat = mm / mu1
    s3 = (float(np.min(shat)), float(np.median(shat)),
          float(np.max(shat)))
    ok_shat = all(abs(s3[i] - SHAT_REF[i]) <= SHAT_TOL
                  for i in range(3))
    check("W8 WARD mu1 closed form (dev %.1e) + CXLIII shat band "
          "min/med/max %.4f/%.4f/%.4f ~ %s"
          % (dev_mu, s3[0], s3[1], s3[2], SHAT_REF),
          dev_mu <= MU_WARD and ok_shat, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------- the spectral objects
    spec = []
    spot_at = (0, N // 2)
    for i, (r, icB, nc) in enumerate(zip(rungs, icBs, nB_min)):
        spec.append(build_spectral(r, nc, spot=(i in spot_at)))
    tie = max(abs(s["T"] - float(r["tail_B"][i]))
              / max(1.0, abs(float(r["tail_B"][i])))
              for s, r, i in zip(spec, rungs, icBs))
    check("W9 WARD grid tie: integer-grid tail == tail_B(cB) "
          "max rel dev %.2e <= %.0e  [%.1f s]"
          % (tie, TIE_WARD, time.time() - T0),
          tie <= TIE_WARD, kill="K2")
    dev_pr = max(s["dev_pair"] for s in spec)
    check("W10 WARD pairing tie: (T - Ttilde) - P == 0 max rel "
          "dev %.2e <= %.0e" % (dev_pr, PAIR_WARD),
          dev_pr <= PAIR_WARD, kill="K2")
    qd = max(s["quad_dev"] for s in spec)
    rd = max(s["rec_dev"] for s in spec)
    check("W11 WARD frame: closed-form c_j vs GL5 at frozen "
          "spots %.2e <= %.0e; cosine recurrence vs direct "
          "%.2e <= %.0e" % (qd, QUAD_WARD, rd, REC_WARD),
          qd <= QUAD_WARD and rd <= REC_WARD, kill="K2")
    fub = max(s["dev_fub"] for s in spec)
    res_mx = max(s["res_v"] for s in spec)
    check("W12 WARD reconstruction: Fubini max %.2e <= %.0e; "
          "residual share max %.2e <= %.2f on all %d rungs"
          % (fub, FUB_WARD, res_mx, RES_WARD, N),
          fub <= FUB_WARD and res_mx <= RES_WARD, kill="K2")
    # ---- W13: the envelope wards
    kap = core.chebyshev_kappa()
    ok_a = abs(kap - KAPPA_REF) <= KAPPA_TOL
    ok_b = abs(KINT[0] - KINT_REF) <= KINT_TOL
    nnb = np.arange(BUETHE_LO, core.ATOM_MAX + 1)
    worstB = float(np.max(np.abs(PSI_TAB[nnb] - nnb)
                          / (BUETHE * np.sqrt(nnb))))
    ok_c = worstB < 1.0
    e1w = max(max(s["env"]["e1_slack"][w] for w in ENVS)
              for s in spec)
    ok_d = e1w <= ENV_SLACK
    Tts = np.array([s["Tt"] for s in spec])
    chat = (hBc + Tts) / mu1
    n_chat = int(np.sum(chat >= C0))
    aa = np.array([r["alpha"] for r in rungs])
    errdA = np.array([s["env"]["err_dir"]["A"] for s in spec])
    slR, seR, r2R = jack_slope(aa, np.log(errdA / mu1))
    ok_e = (n_chat == CHAT_REF_COUNT
            and abs(slR - GAP_REF) <= GAP_REP_TOL)
    check("W13 WARD envelopes: (a) jump-point kappa %.6f ~ %.6f; "
          "(b) KAPPA_INT %.6f ~ %.6f; (c) Buethe in-table worst "
          "ratio %.3f < 1 on [%d, %d]; (d) |E1| <= BE1 in-window "
          "max slack %.1e <= %.0e (all 3 envelopes, all rungs); "
          "(e) CLII repro: chat >= 1/2 on %d/%d (== %d) + direct "
          "ENV-A gap law %+.4f ~ %+.3f (2SE %.3f, R^2 %.2f)"
          % (kap, KAPPA_REF, KINT[0], KINT_REF, worstB,
             BUETHE_LO, core.ATOM_MAX, e1w, ENV_SLACK, n_chat,
             N, CHAT_REF_COUNT, slR, GAP_REF, 2 * seR, r2R),
          ok_a and ok_b and ok_c and ok_d and ok_e, kill="K2")
    mel = max(s["env"]["mellin_dev"] for s in spec)
    check("W14 WARD Mellin form at frozen spots: Fhat "
          "(recurrence) == 2 sum Lam/sqrt psi_j - 2 sum psi_j/"
          "sqrt (direct cos): max rel dev %.2e <= %.0e"
          % (mel, MELLIN_WARD), mel <= MELLIN_WARD, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ A
    section("A -- (a) THE 12 COEFFICIENTS AS CLASSICAL OBJECTS "
            "(CLV pooling reproduced, warded)")
    Pv = np.array([s["P_v"] for s in spec])
    hist = {}
    for s in spec:
        for j in s["cen_v"]["S90"]:
            b = int(s["om"][j] / RED_BIN)
            hist[b] = hist.get(b, 0.0) + abs(s["t_v"][j])
    top = sorted(hist.items(), key=lambda kvv: -kvv[1])[:K_RED]
    centers = np.array(sorted((b + 0.5) * RED_BIN
                              for b, _w in top))
    shares, Pred = [], []
    for s in spec:
        d = np.min(np.abs(s["om"][:, None] - centers[None, :]),
                   axis=1)
        pin = float(s["t_v"][d <= RED_HALF].sum())
        Pred.append(pin)
        shares.append(pin / s["P_v"] if s["P_v"] != 0 else 0.0)
    shares = np.array(shares)
    Pred = np.array(Pred)
    print("    pooled top-%d carrier bins (centers): %s"
          % (K_RED, ", ".join("%.2f" % c for c in centers)))
    sh3 = (float(shares.min()), float(np.median(shares)),
           float(shares.max()))
    print("    read-through share_red min/med/max "
          "%+.3f/%+.3f/%+.3f  (CLV frozen %s)"
          % (sh3[0], sh3[1], sh3[2], SHARE_REF))
    n_low = int(np.sum(centers <= CENT_LOW))
    trace = centers[centers > CENT_LOW]
    ok_tr = all(TRACE_LO < c < TRACE_HI for c in trace)
    ok_sh = all(abs(sh3[i] - SHARE_REF[i]) <= SHARE_TOL
                for i in range(3))
    lab_a = ("BINS-REPRODUCED(K=%d, %d low <= %.2f, trace %s, "
             "med share %.3f)"
             % (K_RED, n_low, CENT_LOW,
                ",".join("%.2f" % c for c in trace), sh3[1]))
    check("A.1 WARD %s -- share band within %.0e of CLV"
          % (lab_a, SHARE_TOL),
          n_low >= N_LOW_MIN and ok_tr and ok_sh, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ B
    section("B -- (b) PER-COEFFICIENT CLASSICAL BOUNDS "
            "(exact-|Delta psi| route on the carriers)")
    # second pass: exact bounds on the in-bin coefficients
    binfo = []
    for s in spec:
        d = np.min(np.abs(s["om"][:, None] - centers[None, :]),
                   axis=1)
        jset = np.nonzero(d <= RED_HALF)[0]
        kf, ug = regen_grid(s["nc"], s["Ng"])
        bx, bsh = bndx_exact(kf, ug, s["u0"], s["om"], s["Lu"],
                             jset)
        binfo.append(dict(jset=jset, bx=bx, bsh=bsh))
    # validity ward (theorem check): |Fhat_j| <= bndX_MIN_j
    worst_v = -np.inf
    for s, b in zip(spec, binfo):
        fh = np.abs(s["Fh"][b["jset"]])
        dev = np.max((fh - b["bx"]["MIN"])
                     / np.maximum(b["bx"]["MIN"], 1e-300))
        worst_v = max(worst_v, float(dev))
    check("B.1 WARD bound validity |Fhat_j| <= bndX_j (ENV-MIN) "
          "on every rung x in-bin coefficient: worst rel excess "
          "%.4e <= %.0e" % (worst_v, BND_SLACK),
          worst_v <= BND_SLACK, kill="K2")
    if KILLS:
        return finish({})
    # honesty table at the median rung (CLV convention)
    imed = int(np.argsort(Pv)[len(Pv) // 2])
    s = spec[imed]
    b = binfo[imed]
    print("\n    HONESTY TABLE at the median rung kz %d (h %d, "
          "nc %d; CLV expected kz 53):"
          % (rungs[imed]["kz"], rungs[imed]["h"], nB_min[imed]))
    print("      omega    c_g        Fhat        bndX_A     "
          "bndX_B     bndX_MIN   ratio      bshare")
    for i, j in enumerate(b["jset"]):
        fh = float(s["Fh"][j])
        bm = float(b["bx"]["MIN"][i])
        print("      %6.3f  %+.3e %+.3e  %.3e  %.3e  %.3e  "
              "%8.1f  %.2f"
              % (float(s["om"][j]), float(s["cv"][j]), fh,
                 float(b["bx"]["A"][i]), float(b["bx"]["B"][i]),
                 bm, bm / max(abs(fh), 1e-300),
                 float(b["bsh"][i])), flush=True)
    rho_med = np.array([float(np.median(
        bb["bx"]["MIN"] / np.maximum(np.abs(ss["Fh"][bb["jset"]]),
                                     1e-300)))
        for ss, bb in zip(spec, binfo)])
    bsh_med = np.array([float(np.median(bb["bsh"]))
                        for bb in binfo])
    r3 = (float(rho_med.min()), float(np.median(rho_med)),
          float(rho_med.max()))
    print("\n    per-rung MEDIAN honesty ratio bndX_MIN/|Fhat|: "
          "min/med/max %.1e/%.1e/%.1e" % r3)
    print("    boundary share of bndX_MIN (the window-edge "
          "anchor price BE1(N)): med %.2f (min/max %.2f/%.2f)"
          % (float(np.median(bsh_med)), float(bsh_med.min()),
             float(bsh_med.max())))
    lab_b = ("HONESTY(min/med/max %.1e/%.1e/%.1e, bshare med "
             "%.2f)" % (r3[0], r3[1], r3[2],
                        float(np.median(bsh_med))))
    check("B.2 typed (b): %s" % lab_b, True)

    # ------------------------------------------------------------ E
    section("E -- (c)+(d) THE ASSEMBLED CERTIFICATE + SLACK "
            "LADDER (demand: H + Ttilde - ERR >= mu1/2)")
    err12 = {w: np.empty(N) for w in ENVS}
    errfull = {w: np.empty(N) for w in ENVS}
    outme = np.empty(N)
    trunc = np.empty(N)
    for i, (s, b) in enumerate(zip(spec, binfo)):
        mask = np.zeros(s["J"], bool)
        mask[b["jset"]] = True
        ac = np.abs(s["cv"])
        for w in ENVS:
            e12 = float(ac[b["jset"]] @ b["bx"][w])
            outd = float(ac[~mask] @ s["env"]["bndD"][w][~mask])
            err12[w][i] = e12
            errfull[w][i] = e12 + outd
        outme[i] = abs(float(s["P_rec_v"]) - Pred[i])
        trunc[i] = abs(s["P_v"] - float(s["P_rec_v"]))
    slack0 = shat - C0
    print("    L0 measured pairing: slack0 = shat - 1/2 "
          "min/med/max %+.3e/%+.3e/%+.3e (CLI min ref %+.2e)"
          % (float(slack0.min()), float(np.median(slack0)),
             float(slack0.max()), CLI_MIN_REF))
    nsplit = int(np.sum(chat < C0))
    kzsplit = [rungs[i]["kz"] for i in range(N)
               if chat[i] < C0]
    print("    split-blocked rungs (chat < 1/2, no bound can "
          "help): %d %s" % (nsplit, kzsplit))
    ok1 = {}
    ok2 = {}
    sl_full = {}
    for w in ENVS:
        s1 = (hBc + Tts - err12[w] - outme - trunc) / mu1 - C0
        s2 = (hBc + Tts - errfull[w]) / mu1 - C0
        ok1[w] = int(np.sum(s1 > 0))
        ok2[w] = int(np.sum(s2 > 0))
        sl_full[w] = s2
        print("    ENV-%-3s: ERR12/mu1 med %.3e; ERR_full/mu1 "
              "med %.3e; slack1 min/med %+.3e/%+.3e (pos %d/%d);"
              " slack2 min/med %+.3e/%+.3e (pos %d/%d)"
              % (w, float(np.median(err12[w] / mu1)),
                 float(np.median(errfull[w] / mu1)),
                 float(s1.min()), float(np.median(s1)), ok1[w],
                 N, float(s2.min()), float(np.median(s2)),
                 ok2[w], N), flush=True)
    print("    measured residual reads (disclosed): OUT_meas/"
          "|P| med %.2e; TRUNC/|P| med %.2e"
          % (float(np.median(outme / np.abs(Pv))),
             float(np.median(trunc / np.abs(Pv)))))
    # gap laws
    print("\n    GAP LAWS (jackknife vs alpha):")
    print("      direct ENV-A (CLII repro):    %+.4f (2SE %.3f, "
          "R^2 %.2f) vs CLII +1.744" % (slR, 2 * seR, r2R))
    errdM = np.array([s["env"]["err_dir"]["MIN"] for s in spec])
    slDM, seDM, r2DM = jack_slope(aa, np.log(errdM / mu1))
    print("      direct ENV-MIN:               %+.4f (2SE %.3f, "
          "R^2 %.2f)" % (slDM, 2 * seDM, r2DM))
    sl_h = {}
    for w in ENVS:
        s12, e12_, r12 = jack_slope(aa, np.log(err12[w] / mu1))
        sfu, efu, rfu = jack_slope(aa, np.log(errfull[w] / mu1))
        sl_h[w] = (sfu, efu)
        print("      harmonic ENV-%-3s: ERR12 %+.4f (2SE %.3f, "
              "R^2 %.2f); ERR_full %+.4f (2SE %.3f, R^2 %.2f)"
              % (w, s12, 2 * e12_, r12, sfu, 2 * efu, rfu))
    DELTA = sl_h["MIN"][0] - slR
    comb = 2.0 * (sl_h["MIN"][1] + seR)
    if DELTA + comb < -GAPLAW_TOL:
        glaw = "IMPROVED"
    elif DELTA - comb > GAPLAW_TOL:
        glaw = "WORSE"
    elif abs(DELTA) <= GAPLAW_TOL:
        glaw = "SAME"
    else:
        glaw = "AMBIG"
    gain = errdM / errfull["MIN"]
    print("    typed GAPLAW: DELTA(MIN vs repro) = %+.3f "
          "(comb 2SE %.3f) -> %s" % (DELTA, comb, glaw))
    print("    same-envelope gain ERR_dir^MIN/ERR_full^MIN: "
          "min/med/max %.2f/%.2f/%.2f (the smoothness gain "
          "isolated from the envelope class)"
          % (float(gain.min()), float(np.median(gain)),
             float(gain.max())))
    lab_g1 = ("GAPLAW(A %+.2f, B %+.2f, MIN %+.2f vs repro "
              "%+.2f, %s) + GAIN(med %.2f)"
              % (sl_h["A"][0], sl_h["B"][0], sl_h["MIN"][0],
                 slR, glaw, float(np.median(gain))))
    check("E.1 typed gap law: %s" % lab_g1, True)
    # outcome enum
    w = "MIN"
    if ok2[w] == N:
        outcome = "HARMCERT-SUFFICIENT"
        print("    ==> SURFACE THEOREM (float level): on all %d "
              "rungs, H + Ttilde - ERR_full >= mu1/2 with the "
              "12-bin classical coefficient bounds (ENV-MIN); "
              "constants as printed above." % N)
    elif ok2[w] > 0 or ok1[w] > 0:
        outcome = ("HARMCERT-PARTIAL(ok2 %d, ok1 %d, split %d)"
                   % (ok2[w], ok1[w], nsplit))
    else:
        outcome = ("HARMCERT-INSUFFICIENT(slack2 med %+.2e, "
                   "honesty med %.1e)"
                   % (float(np.median(sl_full[w])), r3[1]))
        print("    ==> the honest conclusion the CLV screen "
              "predicted: the difficulty RELOCATED into the "
              "coefficients -- the certified bound per carrier "
              "is med %.0fx the measured coefficient, and the "
              "certificate mass sits on the window-edge anchor "
              "price BE1(N) (med share %.2f)."
              % (r3[1], float(np.median(bsh_med))))
    # blocking census on failing rungs
    blocks = {}
    for i, (s, b) in enumerate(zip(spec, binfo)):
        if sl_full["MIN"][i] > 0:
            continue
        contrib = {}
        for ii, j in enumerate(b["jset"]):
            c = float(centers[np.argmin(np.abs(centers
                                               - s["om"][j]))])
            contrib[c] = (contrib.get(c, 0.0)
                          + abs(float(s["cv"][j]))
                          * float(b["bx"]["MIN"][ii]))
        cb = max(contrib.items(), key=lambda kv: kv[1])[0]
        blocks[cb] = blocks.get(cb, 0) + 1
    print("    blocking-center census on failing rungs "
          "(argmax sum |c| bndX per rung): %s"
          % sorted(blocks.items()))
    check("E.2 typed (d) outcome: %s" % outcome, True)

    # ------------------------------------------------------------ G
    section("G -- (e) SUB-GAMMA STATEMENT + the zero-side fence "
            "(comparison only)")
    n_sub = int(np.sum(centers < GAMMA1))
    if n_sub == K_RED:
        print("    ALL %d bin centers sit BELOW gamma_1 = "
              "%.4f: the certificate needs no zero information "
              "precisely because the carriers are sub-gamma."
              % (K_RED, GAMMA1))
    else:
        print("    %d/%d bin centers below gamma_1 = %.4f; the "
              "%d trace bin(s) %s straddle the first ordinate "
              "-- the sub-gamma statement holds for the %d "
              "low-frequency carriers that carry the reduced "
              "pairing, printed as measured."
              % (n_sub, K_RED, GAMMA1, K_RED - n_sub,
                 [float(c) for c in centers[centers >= GAMMA1]],
                 n_low))
    print("    FENCE RECORD: the deployed Selberg-class short-"
          "window bounds are ZERO-COUNTING statements --")
    print("      v678_zero_gap_theorem.py:275-282 (Platt |S| <= "
          "2.5167; Trudgian A1 = 0.112; Bellotti A1 = 0.10076),")
    print("      v680_pinch_attack.py:226-231 + A2.2 (Selberg "
          "count floors, threshold-free where Bellotti fails);")
    print("      routing them into a psi-side coefficient bound "
          "needs the explicit formula over the zeros -- the")
    print("      circularity fence forbids it; they are cited "
          "here as comparison only and never used.  No zero,")
    print("      ordinate or wall-positivity fact enters any "
          "bound computed above (ENV-A table class; ENV-B")
    print("      literature constant, pedigree disclosed in the "
          "spec).")
    lab_sg = "SUBGAMMA(%d/%d)" % (n_sub, K_RED)
    check("G.1 typed (e): %s -- comparison, never construction"
          % lab_sg, True)

    # ------------------------------------------------------------ R
    section("R -- (f) SEAT SCREENS: which side carries the "
            "-1.042 margin decay (recorded)")
    lm = np.log(mm)
    Cbin = np.array([float(np.abs(s["cv"][b["jset"]]).sum())
                     for s, b in zip(spec, binfo)])
    Fbin = np.array([float(np.abs(s["Fh"][b["jset"]]).sum())
                     for s, b in zip(spec, binfo)])
    slc, sec, r2c = jack_slope(lm, np.log(Cbin))
    slf, sef, r2f = jack_slope(lm, np.log(Fbin / mu1))
    okp = np.abs(Pred) > 0
    slp, sep, r2p = jack_slope(lm[okp],
                               np.log(np.abs(Pred[okp]
                                             / mu1[okp])))
    print("    weight side  log sum_bins |c_g| vs log m: %+.3f "
          "(2SE %.3f, R^2 %.2f)" % (slc, 2 * sec, r2c))
    print("    fluct. side  log(sum_bins |Fhat|/mu1) vs log m: "
          "%+.3f (2SE %.3f, R^2 %.2f)" % (slf, 2 * sef, r2f))
    print("    CLV repro    log|P_red/mu1| vs log m: %+.3f "
          "(2SE %.3f, R^2 %.2f; CLV -1.042)"
          % (slp, 2 * sep, r2p))
    lab_r = ("SEAT(c %+.2f, F %+.2f, red %+.2f)"
             % (slc, slf, slp))
    check("R.1 typed (f): %s" % lab_r, True)

    # ------------------------------------------------------------ T
    section("T -- (g) TAU-SCREENS (jackknife, typed)")
    scr = []
    for nm, y in (("ERR12", np.log(err12["MIN"] / mu1)),
                  ("ERRfull", np.log(errfull["MIN"] / mu1)),
                  ("honesty", np.log(rho_med))):
        sl, se, r2 = jack_slope(lm, y)
        v = ("PASS" if abs(sl) <= SLOPE_PASS else
             "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
        scr.append("%s %+.2f %s" % (nm, sl, v))
        print("    screen log %s vs log m: slope %+.3f +- 2SE "
              "%.3f (R^2 %.2f) -> %s" % (nm, sl, 2 * se, r2, v))
    lab_t = "SCREENS(%s)" % ", ".join(scr)
    check("T.1 typed (g): %s" % lab_t, True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = build_rung(CTRL_KZ, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))),
        need_sm=False)
    ctl["scramble"] = build_rung(CTRL_KZ, scramble_seed=1,
                                 need_sm=False)
    ctl["smooth"] = build_rung(CTRL_KZ, smooth_world=True,
                               need_sm=False)
    fired = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: rung dies -> fires" % name)
            continue
        ncovA = int(np.sum(r["cert_A"] > 0))
        ncovB = int(np.sum(r["cert_B"] > 0))
        f = (r["m"] < 0) and ncovA == 0 and ncovB == 0
        fired &= f
        print("    %-9s: m %+.3e  covering cuts A/B %d/%d -> %s"
              % (name, r["m"], ncovA, ncovB,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C1 WARD all three controls fire (m < 0 and zero "
          "coverage in BOTH senses)", fired, kill="K2")
    # C2a -- by-construction integer continuum: f == 0 exactly
    rtrue = build_rung(CTRL_KZ, need_sm=False)
    Ng0 = int(math.floor(rtrue["X"]))
    kk0 = np.arange(CTRL_CUT + 1, Ng0 + 1, dtype=np.int64)
    inv0 = 1.0 / np.sqrt(kk0.astype(float))
    f0 = 2.0 * np.ones(len(kk0)) * inv0 - 2.0 * inv0
    check("C2a WARD by-construction smooth world: f == 0 "
          "identically (max|f| = %.1e) -> every Fhat == 0 "
          "exactly, the certificate holds trivially"
          % float(np.max(np.abs(f0))),
          float(np.max(np.abs(f0))) == 0.0, kill="K2")
    # C2b/C2c -- spectral battery at the fixed cut
    st = ctrl_spectral(rtrue, CTRL_CUT)
    d = np.min(np.abs(st["om"][:, None] - centers[None, :]),
               axis=1)
    jset0 = np.nonzero(d <= RED_HALF)[0]
    bx0, _bsh0 = bndx_exact(st["kf"], st["ug"], st["u0"],
                            st["om"], st["Lu"], jset0)
    fh_true = np.abs(st["Fh"][jset0])
    dev_t = float(np.max((fh_true - bx0["MIN"])
                         / np.maximum(bx0["MIN"], 1e-300)))
    check("C2c-true WARD true world obeys the bounds at cut %d: "
          "worst rel excess %.4e <= %.0e (theorem)"
          % (CTRL_CUT, dev_t, BND_SLACK),
          dev_t <= BND_SLACK, kill="K2")
    sc2 = {}
    for name in ("scramble", "Epstein"):
        sc2[name] = ctrl_spectral(ctl[name], CTRL_CUT)
    blow = (abs(sc2["scramble"]["F0"])
            / max(abs(st["F0"]), 1e-300))
    check("C2b WARD scramble DC blowup: |Fhat_scr(0)|/"
          "|Fhat_true(0)| = %.3e >= %.1f (the PNT cancellation "
          "is destroyed)" % (blow, SCR_BLOWUP),
          blow >= SCR_BLOWUP, kill="K2")
    vio = {}
    for name in ("scramble", "Epstein"):
        fh = np.abs(sc2[name]["Fh"][jset0])
        nv = int(np.sum(fh > bx0["MIN"]))
        vio[name] = (nv, float(np.max(fh / bx0["MIN"])))
        print("    %-9s in-bin coefficient violation census: "
              "%d/%d bins with |Fhat| > bndX (max ratio %.2e)"
              % (name, nv, len(jset0), vio[name][1]))
    disc = ("through measured coefficients"
            if max(vio[n][0] for n in vio) >= 1 else
            "NOT through these bounds (too loose at this depth; "
            "consistent with the honesty ratios -- "
            "discrimination lives in C1/C2b, disclosed)")
    lab_c = ("CTRL(C1 3/3, smooth exact-zero, scramble blowup "
             "%.1e, violations scr %d/Eps %d: %s)"
             % (blow, vio["scramble"][0], vio["Epstein"][0],
                disc))
    check("C3 typed control battery: %s" % lab_c, True)

    return finish(dict(a=lab_a, b=lab_b, e=outcome, g1=lab_g1,
                       sg=lab_sg, r=lab_r, t=lab_t, c=lab_c))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("HARMCERT-MEASURED / %(a)s / BOUNDS-VALID / "
                   "%(b)s / %(e)s / %(g1)s / %(sg)s / %(r)s / "
                   "%(t)s / %(c)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): partial summation, the envelope
  chains, the frame expansion and every tie are EXACT bookkeeping;
  the assembled certificate is classical (ENV-A pure finite-table;
  ENV-B a published literature constant with disclosed zero-
  verification pedigree, no runtime zero input) modulo the two
  MEASURED reads disclosed at each ladder level (out-of-bin
  pairing, frame truncation).  The zeta ordinates and the zero-
  side Selberg-class constants enter ONLY as recorded comparisons.
  A SUFFICIENT outcome would be a per-rung surface certificate,
  not a theorem; an INSUFFICIENT outcome is a measured residual
  law, not an impossibility proof.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
