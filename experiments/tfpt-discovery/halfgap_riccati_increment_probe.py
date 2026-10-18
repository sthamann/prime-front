#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""halfgap_riccati_increment_probe -- PRIME.PORT.HALFGAP.RICCATI.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the HALF-GAP RICCATI BARRIER -- the inductive
architecture for the registered target s >= (1/2) mu1(h), tested
transition-wise as a matrix positivity condition.  2026-08-11.)

THE BARRIER LEMMA (frozen, with proof).  For any symmetric pair
M = [[n, b*], [b, B]], M_+ = [[n_+, b_+*], [b_+, B_+]] with B, B_+
invertible, the round-59 Schur-Ward identity is EXACT:
    s_+ - s = H - r* B_+^{-1} r,
    H = Delta n - 2 <x, Delta b> + <x, Delta B x>,
    r = Delta b - Delta B x,     x = B^{-1} b,
with s, s_+ the Schur pivots.  Let mu = mu1(h), mu_+ = mu1(h_+)
(mu1(h) = 4 sin^2(pi/(2h+1)), the CLI frozen target geometry) and
define the BARRIER MATRIX
    G = [[ H + (1/2)(mu - mu_+),  r* ],
         [ r,                     B_+ ]].
LEMMA: if B_+ > 0 and G >= 0 then  s >= (1/2) mu  implies
s_+ >= (1/2) mu_+.  PROOF (two lines): G >= 0 with B_+ > 0 is,
by the Schur complement, exactly H + (1/2)(mu - mu_+) >=
r* B_+^{-1} r; the update identity then gives s_+ = s +
H - r* B_+^{-1} r >= s - (1/2)(mu - mu_+) >= (1/2) mu_+.  QED.
So a chain of transitions with G >= 0 everywhere plus the base
case propagates the half-gap by INDUCTION -- the simple inductive
architecture this probe measures.

THE CHAIN ORDER, DECLARED FIRST (frozen): the rungs' h values are
NOT monotone in kz.  The PRIMARY transition chain is the h-SORTED
ladder (rungs sorted by (h, kz), the v900/P2/CL step convention;
consecutive steps share the middle rung) -- the induction runs
along increasing h, so mu - mu_+ >= 0 on every primary transition
(warded exactly from the h order).  The kz-ADJACENT chain (rungs
in the natural zone order) is a RECORDED SECONDARY (census only).

THE BASIS, DECLARED (frozen): all primary quantities live in the
SIGN-FREE tangent basis: step k = (r1_k, r2_k), Householder frame
Q_k from the soft direction of S(r1_k) (P2 split 1+7, the fixed
8x8 v892/v900 Schur core), normalization ell_k = det(S(r1_k))^{1/8}
(round-57 ELL-B, source-only, de-circularized: no coefficient
reads a forward wall sign; DEAD on a rung iff the determinant
sign is not +1 -- recorded, never presumed).  Step matrix M_k =
Q_k^T (S(r2_k)/ell_k) Q_k; transition t_k = (M_k, M_+^(k)) with
M_+^(k) = Q_k^T (S(r2_{k+1})/ell_{k+1}) Q_k -- step k+1's
normalized matrix transported to the shared frame Q_k by identity
on the coordinates (the established DDC/round-59 route-(ii)
transport).  KNOWN CAUTION, inherited and warded: cross-rung
telescoping is dimension-consistent only within these declared
frames; the pivot is frame-covariant, so the chain has a HINGE at
every rung -- s_{k+1} (own frame Q_{k+1}) vs s_+^(k) (shared
frame Q_k) -- measured and reported as its own first-class object
(ratio ladder + census of target-crossing flips).  The TAU-TWIN
of the whole transition table (v900 normalization S(r2)/tau(r1))
is computed as a RECORDED SECONDARY: tau reads the wall scale, so
the tau twin is NOT an architecture candidate, only a
normalization-dependence diagnostic; Phase C lives there because
the CXLIV dominance chain is certified in that convention.

HALF-GAP INVARIANT ON THIS SURFACE (declared): the constant 1/2
and the form mu1(h) = 4 sin^2(pi/(2h+1)) are FROZEN UPSTREAM (CLI
registration, NO-ADJUST clause inherited verbatim: no half
adjustment, no transport change, no rung cut -- one negative real
transition kills the simple induction and is reported plainly).
The invariant is evaluated per step as s_k >= (1/2) mu1(h of
r2_k) in the declared ell basis (a THIRD surface convention next
to CLI's race surface and DDC's tau surface -- declared here
before any run; the mu-comparison target h is r2's h, the
CL/DDC convention).  The base case s_1 >= (1/2) mu_1 is printed.

HONEST EXPECTATION (frozen a priori): round 59 measured the pivot
flow with NO stable sign (raw Delta s 18+/19-, med rho 0.781) and
the mu1-increments are O(1e-4..1e-5) against O(0.1..1) pivot
scale, so the barrier is EXPECTED to fail on roughly every
down-flow transition: the a-priori expectation is
BARRIER-FAILS-BROAD.  The probe's value is the exact census + the
failure anatomy + the Phase-C residual model-quality table (the
Loewner lesson inverted), not a celebration.

FROZEN PROTOCOL (pipeline verbatim from
directional_defect_correction_probe = pgram_directional_schur
= CL = CXLIV = v900 chain; ONE Gram per rung; window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W1b
     all chains complete; W1c tau finite; W2 >= 30 full-core
     rungs; W3a truth all-PSD (A, R, S); W3b >= 20 consecutive
     full-core steps; W4 REPRODUCTION P2/P3 ledger (TAU units,
     verbatim): min lam_min(B) == 0.679 (rtol 2e-2), gap min/med
     == 0.052/0.888 (rtol 5e-2), raw-B certified disaster (best
     classical bound < 0 on every step); W5 REPRODUCTION CXLIV
     V4: P_G PD on every step (float, PG_TOL) and float dominance
     negidx(B_tau - 1/2 P_G) = 0 on >= DOMHALF_MIN steps; W6
     REPRODUCTION CL Loewner baseline: med qbar/q == 91.3 (rtol
     5e-2) -- the 91x table Phase C is measured against; W7 WARD
     ELL-B alive (determinant sign +1) on every full-core truth
     rung (the declared basis exists); W8 typed (never kill):
     the ell-surface invariant census s_k >= (1/2) mu1_k with the
     shat-ell ladder (min/med/max) and the base case.

 P   TRANSITION CENSUS (kill -> PIPELINE-BROKEN): P1 >= MIN_TRANS
     = 15 primary transitions (consecutive steps sharing the
     middle rung, h-sorted).

 A   PHASE A -- THE KILL TEST (primary, sign-free basis):
     per transition: x, r, H computed in float64; WARDS (kill ->
     WARD-BROKEN): A1 identity |(s_+ - s) - (H - r*B_+^{-1}r)| /
     max(|s|+|s_+|, 1) <= ID_WARD = 1e-12 on every computed
     transition (primary + tau twin + kz secondary); A2 two-route
     pivot |1/(M^{-1})_00 - (n - b*B^{-1}b)| rel <= S2_WARD =
     1e-8; A3 B_+ PD EXACT-RATIONALLY on every primary truth
     transition (pd_exact on the float entries, v897 class); A4
     mu monotone nonincreasing along the h-sorted chain (exact
     from the h order).  THE BARRIER DECISION (exact-rational on
     the float entries, frozen): G >= 0 iff B_+ PD exact AND
     slack = (H + (1/2)(mu - mu_+)) - r*B_+^{-1}r >= 0 in exact
     Fraction arithmetic (Schur complement; equivalent to
     lam_min(G) >= 0 given B_+ > 0); float lam_min(G) printed as
     the graded ladder.  TYPED VERDICT (frozen enums, never
     kill): BARRIER-HOLDS(N/N, min slack) iff every primary
     transition passes; BARRIER-FAILS-SPARSE(k of N) iff 1 <= k
     <= max(3, ceil(SPARSE_FRAC * N)), SPARSE_FRAC = 0.15, with
     the full failure census (kz/h anatomy, lam_min(G), slack,
     |b|, |r|, H, Delta s); else BARRIER-FAILS-BROAD(k of N).
     A6 HINGE (typed): ratio s_{k+1}^{own}/s_+^(k) ladder
     (med/min/max) + census of transitions where the frame drift
     flips the target crossing (s_+^(k) >= mu_+/2 XOR s_{k+1} >=
     mu_+/2).  A7 TAU-TWIN (typed, recorded): the same exact
     barrier census in the v900 tau normalization.  A8 KZ-CHAIN
     (typed, recorded): the same census on the kz-adjacent
     chain (ell basis; mu - mu_+ signs mixed there, printed).

 B   PHASE B -- CONTROLS (must discriminate).  Rung-level firing
     wards (kill -> WARD-BROKEN if silent): B1 smooth world
     (masses 2 e^{u/2} du) neg(A) > 0 on >= 1 rung; B2 scramble
     ladder (seed 1 on every zone) neg(A) > 0 or chain death on
     >= 1 rung; B3 Epstein x^2+5y^2 comb at kz 9 fires (neg(A) >
     0; transition-level Epstein ladder DECLARED SKIPPED --
     O(X^2) divisor recursion per rung, the predecessor pattern);
     B4 off-line cosh injection (lag signature s*A*cos(gamma0
     t)(cosh(delta t) - 1), t = jD, delta = 0.05, gamma0 = 10.0,
     the healthcode-12 off-line-zero convention; deployed
     amplitude = the SMALLEST A in the frozen ladder (0.01, 0.1,
     1.0) with neg(A) > 0 on >= 1 rung -- a frozen selection
     rule, disclosed per run) fires; B5 mass-rescaled world
     (masses *= fac, deployed fac = smallest in frozen ladder
     (1.1, 2.0) that fires) fires.  B6 BARRIER DISCRIMINATION
     (typed FIRST-CLASS, never kill, as important as Phase A):
     on each control world's transition chain (relaxed step
     preconditions -- the raw construction is run wherever the
     linear algebra exists; ELL-DEAD / singular / B_+ not PD
     are counted as REFUSED = the certificate cannot be stated),
     count transitions where the barrier CERTIFIES (B_+ PD exact
     AND exact slack >= 0).  Any CERTIFY on a false world ->
     WALL-BLIND(world: count) -- reported loudly; zero across
     all control worlds -> CONTROLS-DISCRIMINATE.

 C   PHASE C -- THE P_G RESIDUAL CERTIFICATE (tau convention,
     where the CXLIV dominance is certified; source-only
     direction content).  Per primary tau-twin transition: PG_+ =
     shared-frame CD-Gram co-block of r2_{k+1}'s own positive
     chain ((Q_k^T Gc Q_k)[1:,1:], raw units, the CXLIV V4
     convention); c_dom,+ = lam_min(B_+^tau - 1/2 PG_+) (float
     scalar of the declared class -- a guard/decision, never a
     construction; c_dom,+ <= 0 -> DOM-REFUSED, counted); D_+ =
     1/2 PG_+ + c_dom,+ I.  THE MEASUREMENT: overhead ovh =
     (r* D_+^{-1} r)/(r* B_+^{-1} r) per transition -- the
     analogous ratio table to the CL 91x (which is reproduced in
     W6 on the SAME steps); typed RCERT-LIVE iff med ovh <=
     OVH_LIVE = 3.0 else RCERT-COARSE.  THE CERTIFICATE CENSUS
     (exact-rational on the float entries): a_tau - r* D_+^{-1} r
     >= 0 per transition (a_tau = H_tau + (1/2)(mu - mu_+)); D_+
     PD checked exactly.  C-WARD (kill -> WARD-BROKEN): the
     Loewner direction r*D^{-1}r >= r*B^{-1}r whenever B_+ - D_+
     >= 0 float-certifies (consistency of the model).  WOODBURY
     ESCALATION (float level, declared; only on transitions
     where the exact certificate fails and c_dom,+ > 0): D_{j+1}
     = D_j + w w*, w = sqrt(1/2) u_j, u_j = shared-frame co-block
     components of r2_{k+1}'s positive chain in ASCENDING chain
     degree (source-only, frozen order, never target eigendata);
     acceptance iff float lam_min(B_+ - D_{j+1}) >= -HIER_TOL =
     -1e-12; Sherman-Morrison update of r*D^{-1}r VERIFIED
     against the direct solve to WOODBURY_TOL = 1e-9 relative
     (kill -> WARD-BROKEN); k*(transition) = accepted updates
     until the certificate closes, INF if not reached within
     K_HIER = 64 candidates; typed census.

 D   PHASE D -- THE INGREDIENT DECOMPOSITION (exploratory,
     typed, tau convention on the transitions with PG data):
     G_tau = G0 + G1 + G2 EXACTLY (assembly ward <= ASM_WARD =
     1e-12 relative) with G0 = diag((1/2)(mu - mu_+), c_dom,+ I)
     (PSD iff mu >= mu_+ and c_dom,+ >= 0 -- both measured), G1 =
     [[H_tau, r*], [r, 1/2 PG_+]] (the arithmetic increment
     against the half positive-chain Gram), G2 = diag(0, B_+ -
     1/2 PG_+ - c_dom,+ I) (PSD by the c_dom construction, float
     tol).  Census: lam_min of each part; on barrier-fail
     transitions, G0, G2 >= 0 forces the failure INTO G1 (exact
     contrapositive) -- the carrier census printed.  TYPED:
     DECOMP-PARTIAL(counts).  The deeper symbolic G = L*L +
     sum W_m Z_m* Z_m decomposition (v899 fold / von Mangoldt
     residual ingredients) was NOT attempted -- said honestly.

 F   TAU-SCREENS (typed): log-log OLS on positive subsets vs
     tau(r1_k) for (i) the primary barrier slack, (ii) the
     Phase-C overhead, (iii) the ell-invariant margin s - mu/2;
     bands PASS |slope| <= 0.30 / RELOC >= 0.70 / else AMBIG;
     excluded counts printed.

KILLS: K1 pipeline (W1-W3b, P1) -> PIPELINE-BROKEN; K2
reproduction / identity / exactness / control-firing wards (W4-W7,
A1-A4, C-WARD, Woodbury ward, B1-B5) -> WARD-BROKEN.  All typed
outcomes (W8, A5-A8, B6, Phase C/D censuses, F) are measurements,
never kills.

VERDICT (frozen enum): RICCATI-MEASURED with typed sublabels
BARRIER-HOLDS/BARRIER-FAILS-SPARSE/BARRIER-FAILS-BROAD(...),
HINGE(...), TAU-TWIN(...), KZ-CHAIN(...),
CONTROLS-DISCRIMINATE/WALL-BLIND(...), RCERT-LIVE/RCERT-COARSE(...)
+ RCERT-CERT(...) + WOODBURY(...), DECOMP-PARTIAL(...),
SCREENS(...); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_TRANS = 15;
MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF =
0.888 (rtol 5e-2); PG_TOL = 1e-12; DOMHALF_MIN = 37; LOEW_MED_REF
= 91.3 (rtol 5e-2); ID_WARD = 1e-12; S2_WARD = 1e-8; SPARSE_FRAC
= 0.15; OVH_LIVE = 3.0; HIER_TOL = 1e-12; K_HIER = 64;
WOODBURY_TOL = 1e-9; ASM_WARD = 1e-12; PSD_TOL = 1e-12 (float
part-census tolerance); SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CTRL_KZ = 9; scramble seed 1; INJ_DELTA = 0.05; INJ_GAMMA0 =
10.0; INJ_LADDER = (0.01, 0.1, 1.0); RSC_LADDER = (1.1, 2.0);
NG not applicable (no smooth-grid comb here beyond world_smooth);
mu1(h) = 4 sin^2(pi/(2h+1)) on r2's h.  Runtime cap declared:
15 min.

EXACTNESS MODEL (frozen): float-level probe on the float64-
computed step matrices; ALL barrier / certificate DECISIONS are
exact-rational (Fraction) on those float entries -- the
v897/pgram certificate class (pd_exact Sylvester LDL, exact
Gaussian solves); float eigensolves appear only as printed
ladders, guards and hints, never as decisions; the Woodbury
escalation is declared FLOAT-LEVEL.  What is NOT enclosed: the
float pipeline producing the entries (the interval rollout is
CLIII's separate object, not duplicated here).  NO RH claim.

ANTI-CIRCULARITY (frozen): x = B^{-1} b uses the CURRENT step's
own consumed state (the recursive architecture reads only
already-built rungs -- declared legitimate exactly as DDC
candidate (i)); no future wall sign, no sigma_h, no defect
eigenvector, no target eigendata in the CONSTRUCTION of G beyond
the declared 1+7 split and the frozen upstream constants (1/2,
mu1 form); ell is source-only (round 57); tau appears ONLY in
reproduction wards, the declared tau-twin secondary, Phase C's
certified-convention objects (c_dom as guard scalar) and screens
-- never in the primary chain's coefficients.  RNG only inside
the declared scramble control.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; the dead Loewner route is rebuilt ONLY as the W6
comparison baseline.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (the full surface on the FIRST passage; 35/35 with
the identical bars; 9.1 s; NO bar, band, count, rule, enum or
success criterion was moved after it; ONE pre-freeze mechanical
addition after the smoke: the Woodbury accepted-component census
print in C5 -- a print, nothing decided by it) measured: pipeline
+ P2/P3 + CXLIV + Loewner-91x reproduction green (min lam_min(B)
0.6790, gap 0.0520/0.8875, raw disaster -88.2, P_G PD + dominance
39/39, med qbar/q 91.31, min/max 4.39/408.18); ELL-B alive on
41/41 full-core rungs, 0 dead steps; ell-surface invariant s_k >=
mu1_k/2 on 39/39 (shat-ell min/med/max 10.97/187.2/6797, base
case 6.45e-03 >= 2.21e-04 -- the invariant is slack-rich at step
level, the difficulty is the increment, as frozen); identity ward
max 2.50e-15, two-route pivot 2.20e-15, B_+ PD exact 37/37, mu
monotone.  PHASE A: THE BARRIER FAILS BROADLY, AS FROZEN A PRIORI
-- 21 of 37 primary transitions have exact slack < 0 (57%; every
failure is a down-flow, Delta s < 0 on 21/21: the mu-increment
allowance (mu - mu_+)/2 ~ 3e-8..4e-5 is 3..6 orders below the
O(1e-3..0.4) pivot flow, so every real down-flow kills; worst
lam_min(G) -3.543e-01 at kz 60->16->44 / h 434->436, the
largest-|b| seat |b| = 9.38 -- the same anatomy as the CLVIII k*
outliers); HINGE med ratio 1.0004 (range [0.9629, 1.0656]),
target flips 0/37 (the frame drift never flips the half-gap
crossing at these scales); TAU-TWIN fail 21/37, refused 0 (the
kill is normalization-independent); KZ-CHAIN fail 18/39 with
mu-increment signs 22+/17- (recorded).  PHASE B: all five control
worlds fire at rung level (smooth 42/42, scramble 42/42, Epstein
neg(A) 55, cosh A = 0.01 fires 39/42 -- smallest ladder amplitude
deployed per the frozen rule, rescale fac = 1.1 fires 42/42);
barrier discrimination census: smooth CERTIFY 0 (REFUSED 3/3
transitions, 16 ell-dead steps -- the ENERGY-WALL refusal
pattern), scramble CERTIFY 0 (REFUSED 6/6, 6 ell-dead), cosh
CERTIFY 15/36, rescale CERTIFY 5/17 -> typed WALL-BLIND(cosh 15,
rescale 5) FIRST-CLASS: the barrier condition G >= 0 reads ONLY
the increment geometry -- worlds that perturb the comb gently
(small off-line signature, 10% mass rescale) keep a large share
of their increments barrier-passing while the wall itself is
violated at rung level (neg(A) > 0 broadly there): by itself the
transition-wise barrier is wall-blind; ALL its wall content sits
in the base case and the B_+ > 0 premise -- reported plainly, as
frozen, as important as Phase A.  PHASE C: DOM-REFUSED 0/37;
RCERT-COARSE with ovh min/med/max 4.86/92.82/408.23 -- THE
INVERTED LOEWNER MEASUREMENT IS A CLEAN NEGATIVE: the r-overhead
median 92.8 is statistically THE SAME as the CL full-state
b-overhead 91.3 on the same surface (max even identical, 408) --
the innovation residual r is NOT a better seat for the floor
model D = 1/2 P_G + c_dom I than the full state b: D^{-1}
inflates whatever it is fed; RCERT-CERT 0/37 exact at j = 0 (37
open, of which 21 are the Phase-A failures where no r-model can
close a negative a); WOODBURY closed 0/37 with the escalation
ACCEPTANCE-BLOCKED (med residual overhead at exhaustion 92.8 =
unmoved): c_dom = lam_min(B_+ - 1/2 P_G) saturates the dominance
exactly, so B_+ - D has a zero bottom eigenvalue and no
source-only rank-1 addition is accepted -- the frozen hierarchy
has no headroom at this seat (measured honestly; the accepted
census is printed in v1).  PHASE D: assembly ward 9.73e-17, G0
PSD 37/37, G2 PSD 35/37 (two float-tolerance edge cases at the
PSD_TOL bar -- lam_min(G2) is 0 by the c_dom construction, the
two misses are eigensolve-noise class, typed census only, no
decision touched), G1 carries the failure on 21/21 fails
(lam_min(G1) min/med -5.080e+02/-5.850e+00 -- the exact
contrapositive confirmed: the obstruction lives entirely in the
arithmetic increment against the half positive-chain Gram).
SCREENS: slack PASS(-0.198, R2 0.069, 21 excluded), overhead
PASS(+0.028, R2 0.002), invariant margin AMBIG(-0.309, R2
0.164).  Fail-first preserved: nothing was weakened; bars, bands,
enums and the verdict rule are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CL/CXLIV/DDC; (iii) ELL-B via np.linalg.slogdet, dead iff sign
!= +1.0 (round 57 verbatim); (iv) steps sorted by (h, kz)
(primary) / zone order (kz secondary); consecutive full-core
pairs with r1 all-PSD, lamS > 0 on the truth side; control chains
take consecutive full-core rungs with relaxed preconditions
(declared in B6); (v) exact LDL / exact Gaussian solves verbatim
from pgram_directional_schur_probe; (vi) P_G via eval_chain on
r2's own chain at r2's core nodes (CXLIV V4, raw units, s = 1/2);
(vii) OLS population statistics as v900; screens read positive
subsets with excluded counts printed; (viii) hinge uses the own-
frame pivot of the next step's own matrix (same normalization
ell_{k+1}, frame Q_{k+1}).

NO RH claim: the barrier lemma is exact finite linear algebra; a
BARRIER-HOLDS (had it held) would be a SURFACE statement about
the float64-computed step matrices of the deployed ladder
conditional on the base case -- it proves neither h-uniformity
nor any tail statement; a BARRIER-FAILS census is a route
measurement on the declared architecture.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G + exact-rational machinery verbatim from
directional_defect_correction_probe (CLVIII) /
pgram_directional_schur_probe (CL) / bfloor_pg_dominance_probe
(CXLIV); the update identity + transition frames from
schur_ward_identity_probe (round 59); ELL-B from
port_signfree_normalization_probe (round 57); mu1 + 1/2 +
NO-ADJUST from halfgap_registration_probe (CLI, declared input);
cosh-injection signature from arith_healthcode12_probe (declared
convention).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/halfgap_riccati_increment_probe.py
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
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MIN_TRANS = 15
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
PG_TOL = 1e-12
DOMHALF_MIN = 37
LOEW_MED_REF = 91.3
LOEW_RTOL = 5e-2
ID_WARD = 1e-12
S2_WARD = 1e-8
SPARSE_FRAC = 0.15
OVH_LIVE = 3.0
HIER_TOL = 1e-12
K_HIER = 64
WOODBURY_TOL = 1e-9
ASM_WARD = 1e-12
PSD_TOL = 1e-12
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
SCR_SEED = 1
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
INJ_LADDER = (0.01, 0.1, 1.0)
RSC_LADDER = (1.1, 2.0)
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


# --------------- pipeline, verbatim (DDC / pgram / CXLIV / v900)
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


def folded_measure(d_arm, L, sign=+1.0):
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
    return xs[m], wagg[m], uf[m]


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


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 keep_chain=False, lag_fn=None):
    """v900 verbatim wall + fixed-core split; lag_fn(rr) is the
    declared cosh-injection hook (adds to the lag vector)."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    lag = rr["c_ar"] + np.asarray(c_at, float)
    if lag_fn is not None:
        lag = lag + lag_fn(rr)
    d = grid_density(lag)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
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
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    try:
        Z = np.linalg.solve(R, Xc.T)
    except np.linalg.LinAlgError:
        out["core_ok"] = False
        return out
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


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


# ------------------------------ certified bounds (P3 verbatim)
def gersh_min(B):
    d = np.diag(B)
    r = np.sum(np.abs(B), axis=1) - np.abs(d)
    return float(np.min(d - r))


def gersh_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    lamg = float(np.min(1.0 - r))
    return lamg * (float(np.min(d)) if lamg >= 0.0
                   else float(np.max(d)))


def cassini_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    rr = np.sort(r)[::-1]
    lamc = 1.0 - math.sqrt(float(rr[0]) * float(rr[1]))
    return lamc * (float(np.min(d)) if lamc >= 0.0
                   else float(np.max(d)))


def best_cert(B):
    return max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))


# ------------------------- exact-rational class (pgram verbatim)
def mat_fr(M):
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision: is A - shift I PD?"""
    n = len(Afr)
    A = [[Afr[i][j] - (shift if i == j else 0) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return True, -1


def solve_fr(Afr, bfr):
    n = len(Afr)
    A = [list(Afr[i]) + [bfr[i]] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[p][k] == 0:
            return None
        if p != k:
            A[k], A[p] = A[p], A[k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] = A[i][j] - f * A[k][j]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        s = A[i][n]
        for j in range(i + 1, n):
            s = s - A[i][j] * x[j]
        x[i] = s / A[i][i]
    return x


def quad_fr(Afr, bfr):
    x = solve_fr(Afr, bfr)
    if x is None:
        return None
    s = Fraction(0)
    for bi, xi in zip(bfr, x):
        s = s + bi * xi
    return s


# ---------------------------------- probe-specific machinery
def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def ell_of(S):
    """ELL-B det-core normalization (round 57 verbatim).
    None = ELL-DEAD (determinant sign not +1)."""
    sg, ld = np.linalg.slogdet(S)
    return math.exp(ld / 8.0) if sg == 1.0 else None


def sym(M):
    return 0.5 * (M + M.T)


def split_parts(Mt):
    return float(Mt[0, 0]), Mt[1:, 0].copy(), Mt[1:, 1:].copy()


def pivot_of(Mt):
    """(s, dev of two-route ward, x); None on singular solves."""
    n, b, B = split_parts(Mt)
    try:
        x = np.linalg.solve(B, b)
        s = n - float(b @ x)
        s2 = 1.0 / float(np.linalg.inv(Mt)[0, 0])
    except np.linalg.LinAlgError:
        return None
    return s, abs(s2 - s) / max(abs(s), 1e-300), x


def make_steps(rungs, relax=False):
    """Steps = consecutive full-core pairs of the given rung
    order.  Truth conditions (r1 all-PSD, lamS > 0) unless relax
    (control worlds: raw construction wherever it exists)."""
    steps = []
    n_dead_ell = 0
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
        e1 = ell_of(r1["S"])
        if e1 is None:
            n_dead_ell += 1
            continue
        steps.append(dict(r1=r1, r2=r2, Q=Q, ell=e1,
                          tau=r1["tau"], mu1=mu1_of(r2["h"])))
    return steps, n_dead_ell


def step_mat(st, scale):
    return sym(st["Q"].T @ (st["r2"]["S"] / scale) @ st["Q"])


def transition_table(steps, scale_key):
    """All transitions (consecutive steps sharing the middle
    rung) in the given normalization ('ell' or 'tau').  Returns
    list of dicts with the exact-rationally decided barrier."""
    out = []
    for s1, s2 in zip(steps, steps[1:]):
        if s1["r2"] is not s2["r1"]:
            continue
        t = dict(s1=s1, s2=s2, status="OK")
        Mt = step_mat(s1, s1[scale_key])
        Mp = sym(s1["Q"].T @ (s2["r2"]["S"] / s2[scale_key])
                 @ s1["Q"])
        p1 = pivot_of(Mt)
        p2 = pivot_of(Mp)
        if p1 is None or p2 is None:
            t["status"] = "REFUSED-SINGULAR"
            out.append(t)
            continue
        s, dev_s2, x = p1
        sp, dev_s2p, _xp = p2
        n0, b0, B0 = split_parts(Mt)
        n1, b1, B1 = split_parts(Mp)
        rvec = (b1 - b0) - (B1 - B0) @ x
        H = ((n1 - n0) - 2.0 * float(x @ (b1 - b0))
             + float(x @ ((B1 - B0) @ x)))
        try:
            adap = float(rvec @ np.linalg.solve(B1, rvec))
        except np.linalg.LinAlgError:
            t["status"] = "REFUSED-SINGULAR"
            out.append(t)
            continue
        mu, mup = s1["mu1"], s2["mu1"]
        a = H + 0.5 * (mu - mup)
        id_dev = (abs((sp - s) - (H - adap))
                  / max(abs(s) + abs(sp), 1.0))
        # exact-rational barrier decision on the float entries
        Bfr = mat_fr(B1)
        ok_pd, _piv = pd_exact(Bfr)
        slack_fr = None
        if ok_pd:
            qfr = quad_fr(Bfr, [Fraction(float(v)) for v in rvec])
            if qfr is not None:
                slack_fr = Fraction(float(a)) - qfr
        Gm = np.zeros((8, 8))
        Gm[0, 0] = a
        Gm[0, 1:] = rvec
        Gm[1:, 0] = rvec
        Gm[1:, 1:] = B1
        t.update(s=s, sp=sp, H=H, adap=adap, rvec=rvec, a=a,
                 mu=mu, mup=mup, id_dev=id_dev,
                 dev_s2=max(dev_s2, dev_s2p),
                 bnorm=float(np.linalg.norm(b0)),
                 rnorm=float(np.linalg.norm(rvec)),
                 lamG=float(np.linalg.eigvalsh(Gm)[0]),
                 B1=B1, x=x,
                 pd=ok_pd, slack_fr=slack_fr,
                 slack=float(slack_fr) if slack_fr is not None
                 else float("nan"))
        if not ok_pd or slack_fr is None:
            t["status"] = "REFUSED-BPLUS"
        out.append(t)
    return out


def barrier_census(trans):
    """(n_pass, n_fail, n_refused) under the exact decision."""
    n_pass = n_fail = n_ref = 0
    for t in trans:
        if t["status"] != "OK":
            n_ref += 1
        elif t["slack_fr"] >= 0:
            n_pass += 1
        else:
            n_fail += 1
    return n_pass, n_fail, n_ref


def build_pg_shared(step_next, Q_shared):
    """CXLIV V4 P_G co-block of step_next's r2 chain, expressed
    in the SHARED frame (raw units)."""
    r2 = step_next["r2"]
    ch = r2.get("chain")
    if ch is None:
        return None
    al, be, m0 = ch
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = sym(Gc)
    PG = (Q_shared.T @ Gc @ Q_shared)[1:, 1:]
    return sym(PG)


def pg_components_shared(step_next, Q_shared):
    """Rank-1 CD-Gram summands in the shared frame, ascending
    chain degree (pgram E3 convention, source-only)."""
    r2 = step_next["r2"]
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    sq = np.sqrt(r2["v_core"])
    out = []
    for k in range(Pc.shape[1]):
        g = sq * Pc[:, k]
        out.append((Q_shared.T @ g)[1:])
    return out


def main():
    section("PRIME.PORT.HALFGAP.RICCATI.01 -- the half-gap "
            "Riccati barrier G = [[H + (mu - mu_+)/2, r*], [r, "
            "B_+]] on the sign-free transition chain "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level probe; "
          "all barrier/certificate DECISIONS exact-rational on "
          "the float entries (v897 class).  The 1/2 and mu1 are "
          "frozen upstream (CLI NO-ADJUST, inherited verbatim).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 + CXLIV + Loewner-91x "
            "reproduction + the sign-free surface")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz, keep_chain=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth_h = sorted(truth, key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth_h if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps, n_dead = make_steps(truth_h)
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth_h[0]["h"], truth_h[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    # W4 reproduction in TAU units (DDC verbatim) + per-step data
    for st in steps:
        Mt_tau = step_mat(st, st["tau"])
        nsc, b, B = split_parts(Mt_tau)
        st["minB_tau"] = float(np.linalg.eigvalsh(B)[0])
        x = np.linalg.solve(B, b)
        st["q_tau"] = float(b @ x)
        st["gap_tau"] = nsc - st["q_tau"]
        st["bestg"] = best_cert(B)
        st["B_tau"] = B
        st["b_tau"] = b
        # sign-free (primary) step objects
        Mt_ell = step_mat(st, st["ell"])
        p = pivot_of(Mt_ell)
        st["s_ell"] = p[0]
        st["dev_s2_step"] = p[1]
    minB_all = float(np.min([st["minB_tau"] for st in steps]))
    gaps = np.array([st["gap_tau"] for st in steps])
    bests = np.array([st["bestg"] for st in steps])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL
                and float(np.max(bests)) < 0.0)
    check("W4 REPRODUCTION P2/P3 ledger (tau units): min "
          "lam_min(B) %.4f == %.3f; gap min/med %.4f/%.4f == "
          "%.3f/%.3f; raw-B certified disaster (best max %+.1f < "
          "0 on %d steps)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF, float(np.max(bests)), len(steps)),
          ok_repro, kill="K2")

    # W5 CXLIV dominance + W6 Loewner baseline (own frame, tau)
    pg_ok = True
    n_dom = 0
    for st in steps:
        PG = build_pg_shared(dict(r2=st["r2"]), st["Q"])
        if PG is None:
            pg_ok = False
            continue
        if float(np.linalg.eigvalsh(PG)[0]) <= PG_TOL:
            pg_ok = False
        st["PG_own"] = PG
        Dm = sym(st["B_tau"] - 0.5 * PG)
        evd = np.linalg.eigvalsh(Dm)
        st["cdom_own"] = float(evd[0])
        if int(np.sum(evd < 0.0)) == 0:
            n_dom += 1
    check("W5 REPRODUCTION CXLIV V4: P_G PD on every step; float "
          "dominance negidx(B_tau - 1/2 P_G) = 0 on %d/%d (>= %d)"
          % (n_dom, len(steps), DOMHALF_MIN),
          pg_ok and n_dom >= DOMHALF_MIN, kill="K2")
    qr = []
    for st in steps:
        D = 0.5 * st["PG_own"] + st["cdom_own"] * np.eye(7)
        qbar = float(st["b_tau"] @ np.linalg.solve(D, st["b_tau"]))
        qr.append(qbar / st["q_tau"])
    med_qr = float(np.median(qr))
    check("W6 REPRODUCTION CL Loewner baseline: med qbar/q %.2f "
          "== %.1f (rtol %.0e); min/max %.2f/%.2f -- the 91x "
          "table Phase C is measured against"
          % (med_qr, LOEW_MED_REF, LOEW_RTOL, float(np.min(qr)),
             float(np.max(qr))),
          abs(med_qr / LOEW_MED_REF - 1.0) <= LOEW_RTOL,
          kill="K2")
    check("W7 WARD ELL-B alive (det sign +1) on every full-core "
          "truth rung (%d dead of %d rungs; %d dead steps)"
          % (sum(1 for r in full if ell_of(r["S"]) is None),
             len(full), n_dead),
          n_dead == 0 and all(ell_of(r["S"]) is not None
                              for r in full), kill="K2")
    if KILLS:
        return finish({})

    # W8 the ell-surface invariant (typed)
    shat_ell = np.array([st["s_ell"] / st["mu1"] for st in steps])
    n_inv = int(np.sum(shat_ell >= 0.5))
    print("    W8 ell-surface invariant s_k >= mu1_k/2: %d/%d; "
          "shat-ell min/med/max %.4g/%.4g/%.4g; BASE CASE s_1 = "
          "%.6e vs mu1_1/2 = %.6e -> %s"
          % (n_inv, len(steps), float(shat_ell.min()),
             float(np.median(shat_ell)), float(shat_ell.max()),
             steps[0]["s_ell"], 0.5 * steps[0]["mu1"],
             "HOLDS" if steps[0]["s_ell"] >= 0.5 * steps[0]["mu1"]
             else "FAILS"))
    check("W8 typed: INVARIANT-SURFACE(%d/%d, min shat-ell %.4g)"
          % (n_inv, len(steps), float(shat_ell.min())), True)

    # ------------------------------------------------------------ P
    section("P -- transition census")
    trans = transition_table(steps, "ell")
    check("P1 >= %d primary transitions (h-sorted, shared middle "
          "rung)" % MIN_TRANS, len(trans) >= MIN_TRANS,
          "%d transitions" % len(trans), kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ A
    section("A -- PHASE A: the kill test (sign-free basis, exact "
            "barrier decisions)")
    trans_tau = transition_table(steps, "tau")
    id_max = max([t["id_dev"] for t in trans if t["status"] == "OK"]
                 + [t["id_dev"] for t in trans_tau
                    if t["status"] == "OK"])
    s2_max = max([t["dev_s2"] for t in trans if t["status"] == "OK"]
                 + [st["dev_s2_step"] for st in steps])
    check("A1 WARD identity s_+ - s = H - r*B_+^{-1}r: max rel "
          "dev %.2e <= %.0e (primary + tau twin)"
          % (id_max, ID_WARD), id_max <= ID_WARD, kill="K2")
    check("A2 WARD two-route pivot: max rel dev %.2e <= %.0e"
          % (s2_max, S2_WARD), s2_max <= S2_WARD, kill="K2")
    n_pd = sum(1 for t in trans if t["status"] == "OK")
    check("A3 WARD B_+ PD exact-rationally on every primary "
          "truth transition (%d/%d)" % (n_pd, len(trans)),
          n_pd == len(trans), kill="K2")
    ok_mu = all(t["mu"] >= t["mup"] for t in trans
                if t["status"] == "OK")
    check("A4 WARD mu monotone nonincreasing along the h-sorted "
          "chain (exact from the h order)", ok_mu, kill="K2")

    print("\n    THE BARRIER LADDER (primary; exact slack = "
          "a - r*B_+^{-1}r, a = H + (mu - mu_+)/2):")
    print("      hB->hC        s          s_+        H         "
          "ADAP      (mu-mu+)/2   slack      lam_min(G)  verdict")
    for t in trans:
        if t["status"] != "OK":
            print("      %s: %s" % ("?", t["status"]))
            continue
        ok = t["slack_fr"] >= 0
        print("    %5d->%-5d %+.3e %+.3e %+.3e %.3e  %.3e  "
              "%+.3e %+.3e  %s"
              % (t["s1"]["r2"]["h"], t["s2"]["r2"]["h"], t["s"],
                 t["sp"], t["H"], t["adap"],
                 0.5 * (t["mu"] - t["mup"]), t["slack"],
                 t["lamG"], "PASS" if ok else "FAIL"),
              flush=True)
    n_pass, n_fail, n_ref = barrier_census(trans)
    N = len(trans)
    sparse_cap = max(3, math.ceil(SPARSE_FRAC * N))
    if n_fail == 0 and n_ref == 0:
        slacks = [t["slack"] for t in trans]
        a5 = ("BARRIER-HOLDS(%d/%d, min slack %+.3e)"
              % (n_pass, N, float(np.min(slacks))))
        headline = ("THE SIMPLE HALF-GAP INDUCTION IS LIVE ON "
                    "THIS SURFACE (conditional on base case + "
                    "B_+ > 0): G >= 0 on ALL %d transitions." % N)
    elif 1 <= n_fail <= sparse_cap and n_ref == 0:
        a5 = "BARRIER-FAILS-SPARSE(%d of %d)" % (n_fail, N)
        headline = ("THE SIMPLE INDUCTION IS DEAD (sparse "
                    "failure set); per the frozen protocol no "
                    "adjustment is attempted.")
    else:
        a5 = ("BARRIER-FAILS-BROAD(%d of %d%s)"
              % (n_fail, N,
                 ", %d refused" % n_ref if n_ref else ""))
        headline = ("THE SIMPLE INDUCTION IS DEAD, BROADLY -- as "
                    "frozen a priori: the mu-increment allowance "
                    "is orders of magnitude below the pivot flow "
                    "scale; no half adjustment, no transport "
                    "change, no cut.")
    print("\n    %s" % headline)
    fails = [t for t in trans if t["status"] == "OK"
             and t["slack_fr"] < 0]
    if fails:
        print("    FAILURE CENSUS (anatomy):")
        print("      kzA->kzB->kzC   hB->hC     lam_min(G)  "
              "slack       |b|        |r|        Delta s")
        for t in fails:
            print("      %3d->%3d->%3d  %5d->%-5d %+.3e %+.3e "
                  "%.3e  %.3e  %+.3e"
                  % (t["s1"]["r1"]["kz"], t["s1"]["r2"]["kz"],
                     t["s2"]["r2"]["kz"], t["s1"]["r2"]["h"],
                     t["s2"]["r2"]["h"], t["lamG"], t["slack"],
                     t["bnorm"], t["rnorm"], t["sp"] - t["s"]),
                  flush=True)
        ds_neg = sum(1 for t in fails if t["sp"] - t["s"] < 0)
        print("      down-flow (Delta s < 0) on %d/%d failures"
              % (ds_neg, len(fails)))
    check("A5 typed: %s" % a5, True)

    # A6 the hinge
    hinges = []
    n_flip = 0
    for t in trans:
        if t["status"] != "OK":
            continue
        s_own = t["s2"]["s_ell"]
        hinges.append(s_own / t["sp"] if t["sp"] != 0
                      else float("nan"))
        half = 0.5 * t["mup"]
        if (t["sp"] >= half) != (s_own >= half):
            n_flip += 1
    a6 = ("HINGE(med %.4f, range [%.4f, %.4f], target flips "
          "%d/%d)" % (float(np.median(hinges)),
                      float(np.min(hinges)), float(np.max(hinges)),
                      n_flip, len(hinges)))
    print("    A6 hinge s_{k+1}^own / s_+^shared: the frame "
          "drift the induction must absorb at every rung")
    check("A6 typed: %s" % a6, True)

    # A7 tau twin (recorded)
    p_t, f_t, r_t = barrier_census(trans_tau)
    a7 = "TAU-TWIN(pass %d, fail %d, refused %d of %d)" % (
        p_t, f_t, r_t, len(trans_tau))
    check("A7 typed (recorded secondary): %s" % a7, True)

    # A8 kz-adjacent chain (recorded)
    kz_index = {kz: i for i, kz in enumerate(zones)}
    truth_kz = sorted([r for r in truth if isinstance(r, dict)],
                      key=lambda r: kz_index[r["kz"]])
    steps_kz, _dead_kz = make_steps(truth_kz)
    trans_kz = transition_table(steps_kz, "ell")
    p_k, f_k, r_k = barrier_census(trans_kz)
    mu_up = sum(1 for t in trans_kz if t["status"] == "OK"
                and t["mu"] >= t["mup"])
    mu_dn = sum(1 for t in trans_kz if t["status"] == "OK"
                and t["mu"] < t["mup"])
    id_kz = max([t["id_dev"] for t in trans_kz
                 if t["status"] == "OK"] or [0.0])
    a8 = ("KZ-CHAIN(pass %d, fail %d, refused %d of %d; "
          "mu-increment signs %d+/%d-; id ward %.1e)"
          % (p_k, f_k, r_k, len(trans_kz), mu_up, mu_dn, id_kz))
    check("A8 typed (recorded secondary): %s (identity ward "
          "folded into A1 class)" % a8,
          id_kz <= ID_WARD, kill="K2")

    # ------------------------------------------------------------ B
    section("B -- PHASE B: controls (rung firing wards + barrier "
            "discrimination census)")
    worlds = {}
    sm = [gram_anatomy(kz, world_fn=world_smooth) for kz in zones]
    n_fire_sm = sum(1 for r in sm if isinstance(r, dict)
                    and r["negA"] > 0)
    check("B1 WARD smooth world fires (neg(A) > 0 on %d rungs)"
          % n_fire_sm, n_fire_sm > 0, kill="K2")
    worlds["smooth"] = sm
    scr = [gram_anatomy(kz, scramble_seed=SCR_SEED)
           for kz in zones]
    n_fire_scr = sum(1 for r in scr
                     if r is None or (isinstance(r, dict)
                                      and r["negA"] > 0))
    check("B2 WARD scramble ladder fires (neg(A) > 0 or chain "
          "death on %d rungs)" % n_fire_scr, n_fire_scr > 0,
          kill="K2")
    worlds["scramble"] = scr
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    rE = gram_anatomy(CTRL_KZ,
                      comb=(np.log(nn.astype(float)),
                            2.0 * lamE_[nn]
                            / np.sqrt(nn.astype(float))))
    eps_fire = (rE is None) or rE["negA"] > 0
    check("B3 WARD Epstein comb fires at kz %d (neg(A) %s); "
          "transition-level Epstein ladder DECLARED SKIPPED "
          "(O(X^2) per rung)"
          % (CTRL_KZ, rE["negA"] if isinstance(rE, dict)
             else "chain death"), eps_fire, kill="K2")
    # B4 cosh injection: smallest firing amplitude in the ladder
    cosh_world = None
    cosh_A = None
    for A in INJ_LADDER:
        def inj(rr, _A=A):
            tt = np.arange(rr["M"]) * rr["D"]
            return (_A * np.cos(INJ_GAMMA0 * tt)
                    * (np.cosh(INJ_DELTA * tt) - 1.0))
        lad = [gram_anatomy(kz, lag_fn=inj) for kz in zones]
        n_fire = sum(1 for r in lad
                     if r is None or (isinstance(r, dict)
                                      and r["negA"] > 0))
        print("    cosh injection A = %-5g: fires on %d/%d rungs"
              % (A, n_fire, len(zones)), flush=True)
        if n_fire > 0:
            cosh_world, cosh_A = lad, A
            break
    check("B4 WARD off-line cosh injection fires (deployed A = "
          "%s, frozen selection rule: smallest firing amplitude)"
          % str(cosh_A), cosh_world is not None, kill="K2")
    if cosh_world is not None:
        worlds["cosh(A=%g)" % cosh_A] = cosh_world
    # B5 mass-rescaled world
    rsc_world = None
    rsc_f = None
    for fac in RSC_LADDER:
        def wf(uu, mm, rr, _f=fac):
            return uu, _f * mm
        lad = [gram_anatomy(kz, world_fn=wf) for kz in zones]
        n_fire = sum(1 for r in lad
                     if r is None or (isinstance(r, dict)
                                      and r["negA"] > 0))
        print("    mass rescale fac = %-4g: fires on %d/%d rungs"
              % (fac, n_fire, len(zones)), flush=True)
        if n_fire > 0:
            rsc_world, rsc_f = lad, fac
            break
    check("B5 WARD mass-rescaled world fires (deployed fac = %s)"
          % str(rsc_f), rsc_world is not None, kill="K2")
    if rsc_world is not None:
        worlds["rescale(%g)" % rsc_f] = rsc_world

    # B6 barrier discrimination census on the control chains
    blind = []
    print("\n    B6 barrier discrimination (relaxed chains, ell "
          "basis, exact decisions):")
    for name, lad in worlds.items():
        rungs_w = sorted([r for r in lad if isinstance(r, dict)],
                         key=lambda r: (r["h"], r["kz"]))
        steps_w, dead_w = make_steps(rungs_w, relax=True)
        trans_w = transition_table(steps_w, "ell")
        pw, fw, rw = barrier_census(trans_w)
        print("    %-14s: transitions %2d (ell-dead steps %d)  "
              "CERTIFY %2d  INDEFINITE %2d  REFUSED %2d"
              % (name, len(trans_w), dead_w, pw, fw, rw),
              flush=True)
        if pw > 0:
            blind.append("%s:%d" % (name, pw))
    if blind:
        b6 = "WALL-BLIND(%s)" % ", ".join(blind)
        print("    FIRST-CLASS FINDING: the transition-wise "
              "barrier CERTIFIES on false worlds -- G >= 0 reads "
              "only the increment geometry; the wall content "
              "lives in the base case and the B_+ > 0 premise, "
              "which is where those worlds die (neg(A) > 0 at "
              "rung level).  Said plainly: by itself the barrier "
              "certificate is wall-blind.")
    else:
        b6 = "CONTROLS-DISCRIMINATE(0 certify anywhere)"
    check("B6 typed: %s" % b6, True)

    # ------------------------------------------------------------ C
    section("C -- PHASE C: the P_G residual certificate (tau "
            "convention; the Loewner lesson inverted)")
    ovh_list = []
    cert_open = []
    n_cert = 0
    n_domref = 0
    cw_max = 0.0
    print("      hB->hC        ovh=rD/rB   a_tau      r*D^-1r    "
          "cert(exact)  cdom_+")
    for t in trans_tau:
        if t["status"] != "OK":
            continue
        PG = build_pg_shared(t["s2"], t["s1"]["Q"])
        cdom = float(np.linalg.eigvalsh(
            sym(t["B1"] - 0.5 * PG))[0])
        t["PG_sh"] = PG
        t["cdom_sh"] = cdom
        if cdom <= 0.0:
            n_domref += 1
            t["cstat"] = "DOM-REFUSED"
            continue
        D = 0.5 * PG + cdom * np.eye(7)
        rD = float(t["rvec"] @ np.linalg.solve(D, t["rvec"]))
        ovh = rD / t["adap"] if t["adap"] > 0 else float("inf")
        ovh_list.append(ovh)
        # consistency ward: Loewner direction where B - D >= 0
        if float(np.linalg.eigvalsh(
                sym(t["B1"] - D))[0]) >= -PSD_TOL:
            cw_max = max(cw_max, (t["adap"] - rD)
                         / max(abs(t["adap"]), 1e-300))
        Dfr = mat_fr(D)
        okD, _ = pd_exact(Dfr)
        qfrD = quad_fr(Dfr, [Fraction(float(v))
                             for v in t["rvec"]]) if okD else None
        certd = (okD and qfrD is not None
                 and Fraction(float(t["a"])) - qfrD >= 0)
        t["cstat"] = "CERT" if certd else "OPEN"
        t["rD"] = rD
        t["D"] = D
        if certd:
            n_cert += 1
        else:
            cert_open.append(t)
        print("    %5d->%-5d  %9.3f   %+.3e %.3e  %-11s %.3e"
              % (t["s1"]["r2"]["h"], t["s2"]["r2"]["h"], ovh,
                 t["a"], rD, t["cstat"], cdom), flush=True)
    check("C1 WARD Loewner consistency r*D^{-1}r >= r*B_+^{-1}r "
          "whenever B_+ - D PSD-certifies (max violation %.2e "
          "<= %.0e)" % (max(cw_max, 0.0), WOODBURY_TOL),
          cw_max <= WOODBURY_TOL, kill="K2")
    ovh_arr = np.array(ovh_list)
    n_avail = len(ovh_list)
    med_ovh = float(np.median(ovh_arr)) if n_avail else float("nan")
    live = ("RCERT-LIVE" if n_avail and med_ovh <= OVH_LIVE
            else "RCERT-COARSE")
    c2 = ("%s(ovh min/med/max %.2f/%.2f/%.2f on %d; vs the "
          "step-level Loewner med %.1f)"
          % (live, float(np.min(ovh_arr)) if n_avail else
             float("nan"), med_ovh,
             float(np.max(ovh_arr)) if n_avail else float("nan"),
             n_avail, med_qr))
    check("C2 typed: %s (bar med <= %.1f); DOM-REFUSED %d"
          % (c2, OVH_LIVE, n_domref), True)
    n_afail_open = sum(1 for t in cert_open
                       if t["slack_fr"] is not None
                       and t["slack_fr"] < 0)
    c3 = ("RCERT-CERT(%d/%d exact at j=0; %d open, of which %d "
          "are Phase-A failures where no r-model can close)"
          % (n_cert, n_avail + n_domref, len(cert_open),
             n_afail_open))
    check("C3 typed: %s" % c3, True)

    # Woodbury escalation (float level, declared) on open cases
    wb_max = 0.0
    kstars = []
    for t in cert_open:
        if t.get("cdom_sh", 0.0) <= 0.0:
            continue
        D = t["D"].copy()
        Dinv_r = np.linalg.solve(D, t["rvec"])
        rD = float(t["rvec"] @ Dinv_r)
        comps = pg_components_shared(t["s2"], t["s1"]["Q"])
        kacc = 0
        kstar = None
        for u in comps[:K_HIER]:
            w = math.sqrt(0.5) * u
            Dn = D + np.outer(w, w)
            if float(np.linalg.eigvalsh(
                    sym(t["B1"] - Dn))[0]) < -HIER_TOL:
                continue
            Dw = np.linalg.solve(D, w)
            denom = 1.0 + float(w @ Dw)
            z = float(w @ Dinv_r)
            rD_sm = rD - z * z / denom
            D = Dn
            Dinv_r = np.linalg.solve(D, t["rvec"])
            rD_direct = float(t["rvec"] @ Dinv_r)
            wb_max = max(wb_max, abs(rD_sm - rD_direct)
                         / max(abs(rD_direct), 1e-300))
            rD = rD_direct
            kacc += 1
            if t["a"] - rD >= 0.0:
                kstar = kacc
                break
        kstars.append((t, kstar, kacc, rD))
    if kstars:
        check("C4 WARD Sherman-Morrison vs direct solve: max rel "
              "dev %.2e <= %.0e" % (wb_max, WOODBURY_TOL),
              wb_max <= WOODBURY_TOL, kill="K2")
        n_closed = sum(1 for _t, k, _ka, _r in kstars
                       if k is not None)
        cen = {}
        for _t, k, _ka, _r in kstars:
            key = k if k is not None else "INF"
            cen[key] = cen.get(key, 0) + 1
        res_ovh = [r / t["adap"] for t, k, _ka, r in kstars
                   if k is None and t["adap"] > 0]
        accs = [ka for _t, _k, ka, _r in kstars]
        print("    accepted source-only components per attempted "
              "transition: min/med/max %d/%.1f/%d (of %d "
              "candidates each) -- acceptance requires B_+ - D "
              "to stay PSD"
              % (int(np.min(accs)), float(np.median(accs)),
                 int(np.max(accs)), K_HIER))
        c4 = ("WOODBURY(closed %d/%d, census %s, accepted "
              "med %.1f%s)"
              % (n_closed, len(kstars), cen,
                 float(np.median(accs)),
                 ", med residual ovh at exhaustion %.3f"
                 % float(np.median(res_ovh)) if res_ovh else ""))
    else:
        c4 = "WOODBURY(not triggered)"
    check("C5 typed: %s (float level, declared)" % c4, True)

    # ------------------------------------------------------------ D
    section("D -- PHASE D: the ingredient decomposition (typed, "
            "tau convention)")
    asm_max = 0.0
    n_g0 = n_g2 = n_avail_d = 0
    g1_mins = []
    n_carrier = 0
    n_fail_d = 0
    for t in trans_tau:
        if t["status"] != "OK" or "PG_sh" not in t:
            continue
        n_avail_d += 1
        PG, cdom = t["PG_sh"], t["cdom_sh"]
        G0 = np.zeros((8, 8))
        G0[0, 0] = 0.5 * (t["mu"] - t["mup"])
        G0[1:, 1:] = cdom * np.eye(7)
        G1 = np.zeros((8, 8))
        G1[0, 0] = t["H"]
        G1[0, 1:] = t["rvec"]
        G1[1:, 0] = t["rvec"]
        G1[1:, 1:] = 0.5 * PG
        G2 = np.zeros((8, 8))
        G2[1:, 1:] = sym(t["B1"] - 0.5 * PG) - cdom * np.eye(7)
        Gm = np.zeros((8, 8))
        Gm[0, 0] = t["a"]
        Gm[0, 1:] = t["rvec"]
        Gm[1:, 0] = t["rvec"]
        Gm[1:, 1:] = t["B1"]
        asm = (float(np.linalg.norm(Gm - (G0 + G1 + G2)))
               / max(float(np.linalg.norm(Gm)), 1e-300))
        asm_max = max(asm_max, asm)
        ok0 = (t["mu"] >= t["mup"]) and cdom >= 0.0
        ok2 = float(np.linalg.eigvalsh(G2)[0]) >= -PSD_TOL
        n_g0 += ok0
        n_g2 += ok2
        lm1 = float(np.linalg.eigvalsh(G1)[0])
        g1_mins.append(lm1)
        if t["slack_fr"] is not None and t["slack_fr"] < 0:
            n_fail_d += 1
            if lm1 < 0:
                n_carrier += 1
    check("D1 WARD assembly G = G0 + G1 + G2: max rel dev %.2e "
          "<= %.0e" % (asm_max, ASM_WARD), asm_max <= ASM_WARD,
          kill="K2")
    d2 = ("DECOMP-PARTIAL(G0 PSD %d/%d, G2 PSD %d/%d, "
          "lam_min(G1) min/med %+.3e/%+.3e, G1 carries the "
          "failure on %d/%d fails)"
          % (n_g0, n_avail_d, n_g2, n_avail_d,
             float(np.min(g1_mins)) if g1_mins else float("nan"),
             float(np.median(g1_mins)) if g1_mins
             else float("nan"), n_carrier, n_fail_d))
    print("    the deeper symbolic G = L*L + sum W_m Z_m*Z_m "
          "(v899 fold / von Mangoldt residual ingredients) was "
          "NOT attempted -- said honestly.")
    check("D2 typed: %s" % d2, True)

    # ------------------------------------------------------------ F
    section("F -- tau-screens")
    taus1 = [t["s1"]["tau"] for t in trans if t["status"] == "OK"]
    scr1, _ = screen([t["slack"] for t in trans
                      if t["status"] == "OK"], taus1)
    taus_c = [t["s1"]["tau"] for t in trans_tau
              if t["status"] == "OK" and "rD" in t]
    scr2, _ = screen([t["rD"] / t["adap"] for t in trans_tau
                      if t["status"] == "OK" and "rD" in t],
                     taus_c)
    scr3, _ = screen([st["s_ell"] - 0.5 * st["mu1"]
                      for st in steps],
                     [st["tau"] for st in steps])
    print("    barrier slack vs tau: %s" % scr1)
    print("    Phase-C overhead vs tau: %s" % scr2)
    print("    ell-invariant margin vs tau: %s" % scr3)
    check("F1 typed: SCREENS(slack %s / ovh %s / margin %s)"
          % (scr1.split("(")[0], scr2.split("(")[0],
             scr3.split("(")[0]), True)

    return finish(dict(a5=a5, a6=a6, a7=a7, a8=a8, b6=b6, c2=c2,
                       c3=c3, c4=c4, d2=d2,
                       scr="SCREENS(%s | %s | %s)"
                       % (scr1, scr2, scr3)))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("RICCATI-MEASURED / %s / %s / %s / %s / %s / "
                   "%s / %s / %s / %s / %s"
                   % (labels.get("a5", "-"), labels.get("a6", "-"),
                      labels.get("a7", "-"), labels.get("a8", "-"),
                      labels.get("b6", "-"), labels.get("c2", "-"),
                      labels.get("c3", "-"), labels.get("c4", "-"),
                      labels.get("d2", "-"),
                      labels.get("scr", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the barrier lemma is exact finite
  linear algebra on the float64-computed step matrices, decided
  exact-rationally on their entries; a holding barrier would be a
  SURFACE statement conditional on the base case and B_+ > 0; a
  failing census is a route measurement on the declared
  architecture -- per the frozen protocol nothing is adjusted.
  The 1/2 and mu1 are frozen upstream (CLI NO-ADJUST).  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
